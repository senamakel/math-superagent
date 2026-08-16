//! Which ledgers exist: the ones the runtime ships, and the ones a run adds.
//!
//! # Why the built-ins are registered but not re-implemented
//!
//! Nine ledgers already have modules, and eight of the nine stay exactly as
//! they are. The engine could render `threads` — there is a parity test proving
//! it — but `closure` computes a transitive closure to a fixed point,
//! `blueprint` detects cycles across files, `claims` reconciles a `formalised`
//! status against kernel verdicts on disk, and none of that is expressible as a
//! declaration or should be. Rewriting them onto the engine would trade working
//! checks that `docs/ledgers.md` argues for against a uniformity nobody asked
//! for.
//!
//! They are registered anyway, as [`Source::Derived`], for one reason: so
//! `list_ledgers` lists every ledger and `read_ledger` reads every ledger. A
//! discovery tool that covers eight of twelve is one an agent stops trusting,
//! and then stops using.
//!
//! # Why a run may add one
//!
//! `docs/ledgers.md` records a live workspace that grew an undesigned
//! `research/folds/` folder — `game-core.md`, `passes.md`,
//! `counting-arithmetic.md`, `deadends.md` — because it needed a topic axis and
//! the runtime had none. `threads` was written in response, later, by a human.
//! The pattern will repeat, and `define_ledger` is the answer that does not
//! require a release.
//!
//! Three rules keep that safe, and all three are here rather than in a prompt:
//!
//! - A run-defined slug may not shadow a built-in, so `tasks` is always the
//!   task list and every prompt naming it stays correct.
//! - A run-defined ledger may not write to a built-in's derived path, so it
//!   cannot quietly become the renderer of `research/CLAIMS.md`.
//! - The count is capped, and what is past the cap is reported rather than
//!   silently refused.

use std::path::Path;

use serde_json::{Value, json};

use super::spec::{LedgerSpec, Source, parse};
use crate::agent::Result;

/// Where a run's own declarations live.
pub(in crate::orchestrator) const SPEC_DIR: &str = "config/ledgers";

/// Ledgers a run may declare beyond the built-in set.
///
/// Bounded on the argument `code_layout::plan` makes about programs: a folder
/// nobody counted is how `code/` reached forty-six sibling files defining the
/// same routine seven times. Twelve is far more axes than any investigation has
/// been observed to need — the live workspace that prompted this invented one —
/// so the cap is a runaway guard rather than a budget to spend.
pub(in crate::orchestrator) const MAX_DEFINED: usize = 12;

/// What each candidate solution tried, and what became of it.
///
/// A run that explores five programs at once has five branches, five diffs and
/// one question — which one do we keep, and why not the others. Git answers the
/// first half: the branches are on disk and `attempt_diff` reads them. It
/// cannot answer the second, because the reason a candidate lost is not in its
/// diff. Without somewhere to put it the run re-proposes a dead candidate,
/// which is the same failure `TASKS.md` had and the same fix.
///
/// A queue rather than one file per entry, and for the reason the board is one:
/// several candidates finish at once and each records itself, so the writers are
/// concurrent. One `write_all` of one whole line needs no lock, and the events
/// fold — a candidate that is proposed, then scored, then adopted is three
/// events and one row.
///
/// `score` is a plain field rather than a status because it is a number the
/// scorer produced and the ledger has no opinion about it; the *decision* is
/// the status. Keeping them apart is what lets a candidate be the highest
/// scoring one and still be rejected, with the reason saying why — which is
/// exactly the case a search over programs produces and the case worth
/// recording.
fn attempts() -> Value {
    json!({
        "slug": "attempts",
        "title": "Attempts",
        "purpose": "Every candidate solution this run has branched: what it tried, what it \
                    scored, and for each closed one the reason it was not kept. Read it before \
                    proposing a candidate — re-proposing something already ruled out is the \
                    cheapest mistake available, and the reason beside it is what prevents it.",
        "source": "queue",
        "path": "config/attempts.jsonl",
        "derived": super::super::vcs::ATTEMPTS_PATH,
        // Two prose fields, and the restraint is deliberate. The engine gives
        // every prose field its own bounded line on every rendered row, so a
        // field costs `REASON_CHARS` times the row cap whether or not anybody
        // fills it in — which is how a ledger with nothing wrong in it still
        // arrives at tens of kilobytes. `branch` is not a field because the id
        // determines it (`attempt/<id>`), and an "approach" field would say
        // again what the headline says.
        "fields": [
            { "name": "id", "role": "id", "required": true },
            { "name": "headline", "role": "title", "required": true },
            { "name": "score", "role": "prose" },
            { "name": "reason", "role": "prose" },
            { "name": "refs", "role": "refs" },
            { "name": "status", "role": "status" }
        ],
        "statuses": [
            { "name": "proposed" },
            { "name": "running" },
            { "name": "scored" },
            { "name": "adopted", "closed": true, "needs_reason": true },
            { "name": "rejected", "closed": true, "needs_reason": true },
            { "name": "abandoned", "closed": true, "needs_reason": true }
        ],
        "sections": [
            // Capped well below the engine's default of forty. This ledger is
            // read at the top of every round, unlike the ones a role opens
            // once — so its cost is paid over and over, and a round explores at
            // most ten candidates. Forty rows here would be thirty rows of
            // last hour's decisions on every prompt that carries it.
            {
                "heading": "In flight",
                "blurb": "Candidates still being written or still being judged, most recently \
                          touched first. Read one with `attempt_diff`.",
                "statuses": ["proposed", "running", "scored"],
                "cap": 12,
                "order": "recent"
            },
            // The two archives stay in recorded order: they are read for what
            // is on them rather than worked from the top, and a stable list is
            // what makes "have I already tried this" cheap to answer.
            {
                "heading": "Kept",
                "blurb": "Candidates whose work is now in the trunk, with what made each the one \
                          to keep.",
                "statuses": ["adopted"],
                "cap": 12
            },
            {
                "heading": "Ruled out — do not re-propose",
                "blurb": "Candidates that were not kept, each with the reason. A reason naming \
                          what killed it — 'disagreed with the oracle at n=12' — saves the next \
                          candidate; 'did not work' saves nothing and costs the same to write.",
                "statuses": ["rejected", "abandoned"],
                "cap": 16
            }
        ],
        "checks": ["required-field", "known-status", "closed-needs-reason"],
        // The archivist decides and records; the two planners open a candidate
        // when they start one; reflection closes one it has just judged. The
        // searcher is deliberately absent — it holds no write tool at all, and
        // a role that could record its own candidate's verdict is one that can
        // grade its own homework. See `search.rs`.
        "writers": ["archivist", "goals", "orchestrator", "reflection"]
    })
}

/// The task list: what to do next, what is ruled out, and what was done.
///
/// The one genuinely new ledger. `TASKS.md` was free-form Markdown that two
/// roles rewrote whole — forty-eight rewrites on one workspace, 1,647 lines
/// written to reach a net 165 — and every rewrite dropped the finished rows, so
/// nothing recorded what had been done or why anything was ruled out. The
/// file's own hand-maintained `## Do not do` section was that loss being worked
/// around by the agents themselves.
fn tasks() -> Value {
    json!({
        "slug": "tasks",
        "title": "Tasks",
        "purpose": "What this run is doing next, what it has decided not to do and why, and what \
                    it has finished. Ordered: the first open row is the most recently added or \
                    updated, and is the next thing to work on. Recording against an existing task \
                    moves it back to the top.",
        "source": "queue",
        "path": "config/tasks.jsonl",
        "derived": "TASKS.md",
        "fields": [
            { "name": "id", "role": "id", "required": true },
            { "name": "title", "role": "title", "required": true },
            { "name": "detail", "role": "prose" },
            { "name": "reason", "role": "prose" },
            { "name": "blocked-by", "role": "prose" },
            { "name": "refs", "role": "refs" },
            { "name": "status", "role": "status" }
        ],
        "statuses": [
            { "name": "open" },
            { "name": "blocked" },
            { "name": "done", "closed": true, "needs_reason": true },
            { "name": "dropped", "closed": true, "needs_reason": true }
        ],
        "sections": [
            // The two work queues sort most-recently-touched first. A live
            // director filed a directive's work correctly and could not get it
            // read: the new row rendered last, under a blurb telling the next
            // role to work the first one. See `docs/ledgers.md`.
            {
                "heading": "Do next",
                "blurb": "Most recently added or updated first. Work the first one you can. To \
                          raise an older task, record against it — that moves it back to the top.",
                "statuses": ["open"],
                "order": "recent"
            },
            {
                "heading": "Blocked",
                "blurb": "Waiting on something named, most recently touched first. A blocked row \
                          with no blocker is a mood, and is reported as a fault below.",
                "statuses": ["blocked"],
                "order": "recent"
            },
            // The two archives stay in recorded order. They are read for what is
            // on them rather than worked from the top, and a stable list is
            // what makes "have I already ruled this out" cheap to answer.
            {
                "heading": "Do not do",
                "blurb": "Ruled out, with the reason. Re-proposing one of these is the cheapest \
                          mistake available, and the reason beside it is what prevents it.",
                "statuses": ["dropped"]
            },
            {
                "heading": "Recently done",
                "blurb": "Finished, with what came of it. Kept, because a run that cannot see \
                          what it already did repeats it.",
                "statuses": ["done"]
            }
        ],
        "checks": ["required-field", "known-status", "closed-needs-reason"],
        "writers": ["goals", "orchestrator", "director", "reflection"]
    })
}

/// The nine that keep their own modules, registered so every tool reaches them.
///
/// `written_by` is not decoration. None of these takes `record_entry`, so the
/// write guard has to name each one's real path or it sends a refused caller to
/// a tool that refuses them again — which is exactly what happened to a live
/// librarian on `teams/BOARD.md`.
fn derived(slug: &str, title: &str, purpose: &str, path: &str, written_by: &str) -> Value {
    json!({
        "slug": slug,
        "title": title,
        "purpose": purpose,
        "source": "derived",
        "derived": path,
        "written_by": written_by,
        "fields": [{ "name": "id", "role": "id" }],
        "statuses": [{ "name": "recorded" }]
    })
}

/// Every built-in declaration, in the order `list_ledgers` shows them.
fn builtins() -> Vec<Value> {
    vec![
        tasks(),
        attempts(),
        // `goals` is the sub-goal decomposition under another name. A planner
        // asking this runtime for "the goals" means the propositions that would
        // suffice, which is what a skeleton's gaps are — and `GOAL.md` itself
        // is one statement written once, not a ledger.
        json!({
            "slug": "goals",
            "title": "Sub-goals",
            "purpose": "The goal decomposed into propositions that can each be attacked alone. \
                        An approach is a route to the goal; one of these is a piece of it.",
            "source": "items",
            "dir": super::super::backward::BACKWARD_DIR,
            "block": "skeleton",
            "derived": super::super::backward::BACKWARD_PATH,
            "fields": [
                { "name": "id", "role": "id" },
                { "name": "goal", "role": "title" },
                { "name": "implies", "role": "prose" },
                { "name": "killed-by", "role": "prose" },
                { "name": "rests-on", "role": "refs" },
                { "name": "status", "role": "status" }
            ],
            "statuses": [
                { "name": "sketched" },
                { "name": "live" },
                { "name": "discharged", "closed": true },
                { "name": "broken", "closed": true, "needs_reason": true },
                { "name": "spent", "closed": true, "needs_reason": true }
            ]
        }),
    ]
    .into_iter()
    .chain(runtime_rendered())
    .collect()
}

/// The nine rendered in Rust, each naming the route that actually writes it.
fn runtime_rendered() -> Vec<Value> {
    vec![
        derived(
            "board",
            "Board",
            "What each school has told the others while the work is running. Asserted, never \
             established: a post is not a claim and is never filed as one.",
            super::super::board::PATH,
            "`post_board`, which is the only way onto the board and is held by the roles that \
             decide what to do next",
        ),
        derived(
            "claims",
            "Claims",
            "What the library establishes, statement by statement, with hypotheses and status. \
             Search it with `search_claims`.",
            super::super::claims::CLAIMS_PATH,
            "a fenced `claim` block in the note that establishes it, written with \
             `write_document` — a claim is filed with its hypotheses or not at all",
        ),
        derived(
            "threads",
            "Threads",
            "The directions of attack the run is pursuing, and the ones it has closed.",
            super::super::threads::THREADS_PATH,
            "a fenced `thread` block in `research/threads/<slug>.md`, written with \
             `write_document`",
        ),
        derived(
            "approaches",
            "Approaches",
            "Candidate reformulations, and for each closed one the reason it closed.",
            super::super::approaches::APPROACHES_PATH,
            "a fenced `approach` block in `research/approaches/<slug>.md`, written with \
             `write_document`",
        ),
        derived(
            "weakened",
            "Weakened",
            "The goal with its difficulties switched off, rung by rung, weakest first.",
            super::super::weakened::WEAKENED_PATH,
            "fenced `ladder` and `rung` blocks in `research/weakened/<slug>.md`, written with \
             `write_document`",
        ),
        derived(
            "blueprint",
            "Blueprint",
            "The statement graph: what rests on what, which lemmas are ready now, and whether \
             the argument is circular.",
            super::super::blueprint::BLUEPRINT_PATH,
            "nothing directly — it is computed from the skeletons and the claims, so change one \
             of those and this re-derives",
        ),
        derived(
            "entailment",
            "Entailment",
            "What the library already gives without new work, closed transitively.",
            super::super::closure::CLOSURE_PATH,
            "nothing directly — it is the transitive closure of the claims' `follows-from` \
             edges, so add the edge to a claim block",
        ),
        derived(
            "frontier",
            "Frontier",
            "The citation graph: sources the library's own sources point at, ranked.",
            super::super::frontier::FRONTIER_PATH,
            "nothing directly — it is derived from the citations in downloaded sources, so \
             `download_document` a source and this re-derives",
        ),
        derived(
            "requests",
            "Requests",
            "What the run knows it is missing, and what would settle each gap.",
            super::super::requests::REQUESTS_PATH,
            "`request_research`, which states what is missing and what would settle it",
        ),
    ]
}

/// Every ledger available in `workspace`.
///
/// Built-ins first, then whatever `config/ledgers/` declares. A malformed
/// declaration is skipped with a fault rather than failing the read: a run that
/// wrote one bad spec must still be able to reach its tasks.
pub(in crate::orchestrator) fn all(workspace: &Path) -> (Vec<LedgerSpec>, Vec<String>) {
    let mut specs: Vec<LedgerSpec> = Vec::new();
    let mut faults: Vec<String> = Vec::new();
    for document in builtins() {
        match parse(&document, true) {
            Ok(spec) => specs.push(spec),
            // A built-in that will not parse is this crate's bug, not a run's,
            // and it is worth seeing rather than swallowing.
            Err(error) => faults.push(format!("a built-in ledger is malformed: {error}")),
        }
    }
    let Ok(listing) = std::fs::read_dir(workspace.join(SPEC_DIR)) else {
        return (specs, faults);
    };
    let mut paths: Vec<std::path::PathBuf> = listing
        .flatten()
        .map(|entry| entry.path())
        .filter(|path| path.extension().is_some_and(|kind| kind == "json"))
        .collect();
    paths.sort();
    let mut defined = 0_usize;
    for path in paths {
        let name = path.file_name().unwrap_or_default().to_string_lossy().to_string();
        let Ok(text) = std::fs::read_to_string(&path) else {
            continue;
        };
        let parsed = serde_json::from_str::<Value>(&text)
            .map_err(|error| {
                tinyagents::TinyAgentsError::Validation(format!("`{name}` is not JSON: {error}"))
            })
            .and_then(|document| parse(&document, false));
        match parsed {
            Ok(spec) => {
                if let Some(reason) = rejected(&spec, &specs) {
                    faults.push(format!("`{name}` was not loaded: {reason}"));
                    continue;
                }
                defined += 1;
                if defined > MAX_DEFINED {
                    faults.push(format!(
                        "`{name}` was not loaded: this workspace already defines {MAX_DEFINED} \
                         ledgers, which is the cap. Retire one that nothing reads before adding \
                         another."
                    ));
                    continue;
                }
                specs.push(spec);
            }
            Err(error) => faults.push(format!("`{name}` was not loaded: {error}")),
        }
    }
    (specs, faults)
}

/// Why a run-defined spec may not join the registry, if it may not.
fn rejected(spec: &LedgerSpec, existing: &[LedgerSpec]) -> Option<String> {
    if existing.iter().any(|other| other.slug == spec.slug) {
        return Some(format!(
            "`{}` is already a ledger. A built-in slug cannot be redefined — every prompt naming \
             it would then be wrong about what it holds.",
            spec.slug
        ));
    }
    if let Some(clash) = existing
        .iter()
        .find(|other| other.derived == spec.derived)
    {
        return Some(format!(
            "`{}` is already written by the `{}` ledger. Two writers on one derived file is how \
             each one's work disappears.",
            spec.derived, clash.slug
        ));
    }
    if matches!(spec.source, Source::Derived) {
        return Some(
            "`derived` is for ledgers this runtime renders in Rust. A ledger you define keeps a \
             `queue` or `items` source, so the engine can actually read it."
                .to_string(),
        );
    }
    None
}

/// The spec named `slug`, if there is one.
pub(in crate::orchestrator) fn find(workspace: &Path, slug: &str) -> Option<LedgerSpec> {
    all(workspace)
        .0
        .into_iter()
        .find(|spec| spec.slug == slug.trim())
}

/// Whether `relative` is a derived path some ledger owns.
///
/// The write guard: an agent editing one of these would have its edit erased by
/// the next derivation, having believed it landed. Refusing the write and
/// naming the tool is the only honest answer.
pub(in crate::orchestrator) fn owns_derived(
    workspace: &Path,
    relative: &str,
) -> Option<(String, String)> {
    all(workspace)
        .0
        .into_iter()
        .find(|spec| spec.derived == relative.trim())
        .map(|spec| (spec.slug, spec.written_by))
}

/// Writes a run's declaration to `config/ledgers/<slug>.json`.
///
/// # Errors
///
/// Returns an error when the declaration is malformed, when it collides with an
/// existing ledger, when the cap is reached, or when the file cannot be written.
pub(in crate::orchestrator) fn define(workspace: &Path, document: &Value) -> Result<LedgerSpec> {
    let spec = parse(document, false)?;
    let (existing, _) = all(workspace);
    if let Some(reason) = rejected(&spec, &existing) {
        return Err(tinyagents::TinyAgentsError::Validation(reason));
    }
    let defined = existing.iter().filter(|spec| !spec.builtin).count();
    if defined >= MAX_DEFINED {
        return Err(tinyagents::TinyAgentsError::Validation(format!(
            "this workspace already defines {MAX_DEFINED} ledgers, which is the cap. Retire one \
             nothing reads with `retire_ledger` before adding another."
        )));
    }
    let directory = workspace.join(SPEC_DIR);
    std::fs::create_dir_all(&directory).map_err(|error| {
        tinyagents::TinyAgentsError::Tool(format!("failed to create `{SPEC_DIR}`: {error}"))
    })?;
    let target = directory.join(format!("{}.json", spec.slug));
    let body = serde_json::to_string_pretty(document).map_err(|error| {
        tinyagents::TinyAgentsError::Tool(format!("failed to serialize the declaration: {error}"))
    })?;
    std::fs::write(&target, body).map_err(|error| {
        tinyagents::TinyAgentsError::Tool(format!(
            "failed to write `{SPEC_DIR}/{}.json`: {error}",
            spec.slug
        ))
    })?;
    Ok(spec)
}

/// Removes a run-defined declaration.
///
/// The entries themselves are left on disk. A ledger nobody reads is worth
/// retiring; the work recorded in it is not, and deleting a queue to tidy a
/// registry is exactly the kind of loss this whole module exists to prevent.
///
/// # Errors
///
/// Returns an error when the slug names a built-in, when nothing of that name
/// is defined, or when the file cannot be removed.
pub(in crate::orchestrator) fn retire(workspace: &Path, slug: &str) -> Result<String> {
    let slug = slug.trim();
    let Some(spec) = find(workspace, slug) else {
        return Err(tinyagents::TinyAgentsError::Validation(format!(
            "there is no ledger called `{slug}`"
        )));
    };
    if spec.builtin {
        return Err(tinyagents::TinyAgentsError::Validation(format!(
            "`{slug}` is built in and cannot be retired. Every role's prompt is written against \
             it existing."
        )));
    }
    let target = workspace.join(SPEC_DIR).join(format!("{slug}.json"));
    std::fs::remove_file(&target).map_err(|error| {
        tinyagents::TinyAgentsError::Tool(format!("failed to remove `{slug}`: {error}"))
    })?;
    Ok(source_of(&spec))
}

/// Where a retired ledger's entries were left.
fn source_of(spec: &LedgerSpec) -> String {
    match &spec.source {
        Source::Queue { path } => path.clone(),
        Source::Items { dir, .. } => dir.clone(),
        Source::Derived => spec.derived.clone(),
    }
}

#[cfg(test)]
#[path = "registry_test.rs"]
mod test;
