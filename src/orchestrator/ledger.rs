//! What every derived ledger shares.
//!
//! The nine ledgers in [`docs/ledgers.md`](../../docs/ledgers.md) each walk
//! their own source and render their own file, and that part is genuinely
//! per-ledger: a claim block and a proof skeleton have nothing in common but
//! being fenced. What they *do* share is the pair of questions every list
//! section below a table has to answer — how many rows, and how long a prose
//! field may be — and each module answered them separately, or not at all.
//!
//! Not at all is the common case, and it is what this module exists to fix.
//! Every one of the five capped its *table*, with a `MAX_ROWS` and a
//! `FIELD_CHARS`, and then rendered the sections underneath whole.
//! `research/APPROACHES.md` on one live workspace was 86 KB, of which the table
//! was about 2 KB: `## What closed, and why` printed each refuted approach's
//! entire `killed-by` field, one of them 5 KB of prose, and there was no bound
//! on the count either. That one file was a third of the orchestrator's
//! 63,833-token system prompt, which every model call in that role pays for.
//!
//! [`budget::listed`] is the missing primitive, taken from the one place that
//! did it right — [`super::board`] renders at most forty posts and says how
//! many it left — and given to everybody. Its two rules are worth stating
//! because a section that breaks either reintroduces the same file:
//!
//! - **Say what was dropped.** A truncated list that reads as complete is worse
//!   than a long one: the reader concludes the run holds nothing more. Every
//!   caller renders the count and the path the rest is on.
//! - **Bound the prose, not just the rows.** Twenty rows of 5 KB each is the
//!   same file by a different route, which is exactly how the table's own
//!   `MAX_ROWS` failed to help.

pub(super) mod budget;
pub(super) mod engine;
pub(super) mod registry;
pub(super) mod spec;

#[cfg(test)]
#[path = "ledger/ceiling_test.rs"]
mod ceiling_test;

#[cfg(test)]
#[path = "ledger/fit_test.rs"]
mod fit_test;

use std::fmt::Write as _;
use std::path::Path;

use tinyagents::harness::summarization::estimate_tokens;

use super::shared_context::{CHARS_PER_TOKEN, positive_env};

/// What one derived ledger may cost a system prompt when nothing says
/// otherwise.
///
/// The same ten thousand tokens `CONTEXT.md` gets, and deliberately so: the
/// shared brief is the most valuable file a role is sent, so no derived table
/// has an argument for costing more than it. Six of the nine are an order of
/// magnitude under this and always will be — the cap is for the seventh.
const DEFAULT_LEDGER_TOKENS: u64 = 10_000;

/// Reads the per-ledger prompt budget from the environment.
///
/// `MATH_AGENT_LEDGER_TOKENS` overrides it. A missing, empty, unparsable, or
/// zero value keeps [`DEFAULT_LEDGER_TOKENS`], so a malformed override never
/// silently removes the bound — the rule every other limit here follows.
fn budget_tokens() -> u64 {
    positive_env("MATH_AGENT_LEDGER_TOKENS").unwrap_or(DEFAULT_LEDGER_TOKENS)
}

/// Whether `relative` is a derived ledger routed into system prompts.
pub(super) fn is_routed(relative: &str) -> bool {
    ROUTED.contains(&relative)
}

/// Clamps a derived ledger to its budget on the way into a system prompt.
///
/// Returns `None` when it already fits, so the caller keeps its own string in
/// the ordinary case — which is every case, until it is not.
///
/// This is a backstop, not the mechanism. What keeps these files small is each
/// renderer bounding its own sections, which is where a cut can be made
/// intelligently: drop the fortieth closed approach and say so, rather than
/// stop mid-sentence. This fires only when a renderer has failed to, and its
/// job is to make that failure cost one truncated file instead of a prompt
/// nobody budgeted. `research/APPROACHES.md` reached 86 KB — a third of a
/// 63,833-token prompt — with no bound of any kind between it and the model,
/// which is the situation this removes for good.
///
/// The cut keeps the *leading* portion, on the same reasoning as
/// [`super::shared_context::fit`]: every one of these files puts its table
/// first and its diagnostics last, so the leading portion is the part a reader
/// came for.
pub(super) fn fit(relative: &str, content: &str) -> Option<String> {
    if !is_routed(relative) {
        return None;
    }
    let budget = budget_tokens();
    if estimate_tokens(content) <= budget {
        return None;
    }
    let limit = usize::try_from(budget)
        .unwrap_or(usize::MAX)
        .saturating_mul(CHARS_PER_TOKEN);
    let mut cut = limit.min(content.len());
    while cut > 0 && !content.is_char_boundary(cut) {
        cut -= 1;
    }
    Some(format!(
        "{}\n\n_[`{relative}` exceeds the {budget}-token per-ledger budget and was cut here for \
         this prompt. The whole file is on disk. A derived ledger reaching this bound means a \
         section of it is rendering unbounded — that is a defect in the module that renders it, \
         not something to work around.]_",
        &content[..cut]
    ))
}

/// Every derived ledger that is routed into at least one role's system prompt.
///
/// The list is here rather than in each module because the question it answers
/// — *what does the derived state cost the run* — is not any one ledger's, and
/// on the workspace that prompted this module the answer was that nine files
/// were 51% of all twenty-two assembled prompts. Nothing measured that.
const ROUTED: [&str; 9] = [
    super::claims::CLAIMS_PATH,
    super::threads::THREADS_PATH,
    super::approaches::APPROACHES_PATH,
    super::backward::BACKWARD_PATH,
    super::weakened::WEAKENED_PATH,
    super::blueprint::BLUEPRINT_PATH,
    super::closure::CLOSURE_PATH,
    super::frontier::FRONTIER_PATH,
    super::requests::REQUESTS_PATH,
];

/// Reports what each derived ledger currently costs a prompt that carries it.
///
/// Two columns, and the difference between them is the reason this exists. The
/// first is the file *on disk*, which is what
/// [`super::orchestrator_environment::load_workspace_files`] reads into a
/// system prompt. The second is what today's code would render from the same
/// sources. A ledger is only re-derived when something writes to it, so after a
/// bound changes the two disagree until the next write — and a run started
/// before the change keeps paying the old price. Reading only the first column
/// would report a fix as landed while every prompt still carried the old file.
///
/// The five with a pure `collect`/`render` pair are re-rendered here. The rest
/// need a `WorkspaceDocuments` or another ledger to render against, so they
/// report their size on disk alone.
pub(super) fn costs(workspace: &Path) -> String {
    let ledger = super::claims::collect(workspace);
    let fresh: [(&str, Option<usize>); 9] = [
        (
            super::claims::CLAIMS_PATH,
            Some(ledger.render().chars().count()),
        ),
        (
            super::threads::THREADS_PATH,
            Some(super::threads::collect(workspace).render(&ledger).chars().count()),
        ),
        (
            super::approaches::APPROACHES_PATH,
            Some(super::approaches::collect(workspace).render().chars().count()),
        ),
        (
            super::backward::BACKWARD_PATH,
            Some(
                super::backward::collect(workspace)
                    .render(&ledger)
                    .chars()
                    .count(),
            ),
        ),
        (
            super::weakened::WEAKENED_PATH,
            Some(super::weakened::collect(workspace).render().chars().count()),
        ),
        (super::blueprint::BLUEPRINT_PATH, None),
        (super::closure::CLOSURE_PATH, None),
        (super::frontier::FRONTIER_PATH, None),
        (super::requests::REQUESTS_PATH, None),
    ];
    debug_assert_eq!(fresh.len(), ROUTED.len());

    let mut out = String::from(
        "## What the derived ledgers cost\n\nCharacters, and the tokens a role prompt carrying the \
         file pays — re-sent on every model call in every role routed them. *On disk* is what a \
         prompt loads today; *re-rendered* is what this build would write on the next derivation. \
         They disagree until something writes to that ledger.\n\n\
         | Ledger | On disk | ~Tokens | Re-rendered | ~Tokens |\n| --- | ---: | ---: | ---: | ---: |\n",
    );
    let (mut on_disk_total, mut fresh_total) = (0_usize, 0_usize);
    for (relative, rendered) in fresh {
        let on_disk = std::fs::read_to_string(workspace.join(relative))
            .map_or(0, |text| text.chars().count());
        on_disk_total += on_disk;
        fresh_total += rendered.unwrap_or(on_disk);
        let (size, tokens) = rendered.map_or_else(
            || ("—".to_string(), "—".to_string()),
            |count| (count.to_string(), (count / CHARS_PER_TOKEN).to_string()),
        );
        let _ = writeln!(
            out,
            "| `{relative}` | {on_disk} | {} | {size} | {tokens} |",
            on_disk / CHARS_PER_TOKEN
        );
    }
    let _ = writeln!(
        out,
        "| **total** | **{on_disk_total}** | **{}** | **{fresh_total}** | **{}** |",
        on_disk_total / CHARS_PER_TOKEN,
        fresh_total / CHARS_PER_TOKEN
    );
    out
}
