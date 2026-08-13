//! The dossier: everything the run has written, handed to the role that has to
//! think of something new.
//!
//! Every other role's workspace context is assembled once, by
//! [`super::RolePrompts::load`], when the container starts. That is right for
//! roles whose job is stated up front and does not depend on what the run has
//! since discovered. It is wrong for the inventor, and on a long run it is
//! badly wrong: a conjecture launcher defaults to twelve hours, the inventor is
//! first delegated to hours in, and the `GOAL.md`, `THREADS.md` and `CLAIMS.md`
//! in its system prompt are the versions that existed before any of the work it
//! is being asked to invent past. The role that most needs to know what has
//! already been tried was the role least equipped to know it.
//!
//! So this is assembled per delegation, from disk, at the moment the inventor
//! is spawned. It is delivered in the spawn message rather than in the system
//! prompt for two reasons: the shared method policy has to lead every prompt so
//! the provider can cache the common prefix, and a harness's prompt is fixed
//! when it is registered — a per-invocation system prompt would mean
//! re-registering the harness on every call. The message reaches the same child
//! run.
//!
//! It is packed in priority order against a token budget, because the useful
//! failure mode is losing the least important section rather than erroring. The
//! order is an argument about what invention needs: the goal, then what has
//! already been ruled out, then what is established, then everything else. And
//! every cut is announced — an inventor silently handed half of `CLAIMS.md`
//! re-proposes what was in the other half, which is the exact failure the
//! dossier exists to prevent.

use std::fmt::Write as _;
use std::path::Path;

use super::shared_context::{CHARS_PER_TOKEN, positive_env};

/// What the dossier may cost when nothing says otherwise.
///
/// Sixteen thousand tokens is deliberately large. The inventor is delegated to
/// a handful of times in a run, not once per attempt, and what it costs is set
/// against re-proposing an idea the run already closed — which costs a whole
/// diversify, three child runs, and the attempt that follows them.
const DEFAULT_DOSSIER_TOKENS: u64 = 16_000;

/// Reads the dossier's token budget from the environment.
///
/// `MATH_AGENT_DOSSIER_TOKENS` overrides it. A missing, empty, unparsable, or
/// zero value keeps [`DEFAULT_DOSSIER_TOKENS`], so a malformed override never
/// silently removes the bound — the rule every other limit in this runtime
/// follows.
fn budget_tokens() -> u64 {
    positive_env("MATH_AGENT_DOSSIER_TOKENS").unwrap_or(DEFAULT_DOSSIER_TOKENS)
}

/// Files that fill whatever budget the ranked sections leave.
///
/// Ordered, and last on purpose: useful to have, and the first thing that
/// should go when the run has written enough that everything cannot fit.
const REMAINDER: [&str; 4] = [
    "TASKS.md",
    "research/FRONTIER.md",
    "research/REQUESTS.md",
    "code/lib/INDEX.md",
];

/// Characters below which a section is dropped rather than included.
///
/// A heading with two lines under it costs more attention than it returns, and
/// reads as "this file holds almost nothing" rather than "this file did not
/// fit".
const USABLE_SECTION: usize = 400;

/// A dossier under construction, with what is left of its budget.
struct Packed {
    body: String,
    /// Characters still available. Saturating: a section that overruns leaves
    /// zero rather than wrapping, and every later section is then skipped.
    remaining: usize,
}

impl Packed {
    fn new(budget: usize) -> Self {
        Self {
            body: String::new(),
            remaining: budget,
        }
    }

    /// Appends a section whole, whatever it costs.
    ///
    /// Reserved for `GOAL.md`. Truncating the statement of what a result must
    /// satisfy would make every other section unreadable against it, and a
    /// goal large enough to threaten the budget is itself worth seeing.
    fn verbatim(&mut self, label: &str, content: &str) {
        let content = content.trim();
        if content.is_empty() {
            return;
        }
        let _ = write!(self.body, "\n\n## {label}\n{content}");
        self.remaining = self.remaining.saturating_sub(content.chars().count());
    }

    /// Appends a section, cutting it at the budget and saying so if it cuts.
    fn section(&mut self, label: &str, content: &str) {
        let content = content.trim();
        if content.is_empty() {
            return;
        }
        if self.remaining < USABLE_SECTION {
            return;
        }
        let (rendered, cut) = clamp(content, self.remaining);
        let _ = write!(self.body, "\n\n## {label}\n{rendered}");
        if cut {
            let _ = write!(
                self.body,
                "\n\n_[`{label}` was cut here to fit this dossier's budget. Read the file for the \
                 rest before concluding it holds nothing more.]_"
            );
        }
        self.remaining = self.remaining.saturating_sub(rendered.chars().count());
    }
}

/// Cuts `content` to `limit` characters at a character boundary.
///
/// Returns the text and whether anything was removed, so the caller can say so.
fn clamp(content: &str, limit: usize) -> (String, bool) {
    if content.chars().count() <= limit {
        return (content.to_string(), false);
    }
    (content.chars().take(limit).collect(), true)
}

/// Reads a workspace file, or an empty string when it is absent or unreadable.
///
/// Absence is the ordinary state of most of these files for most of a run, so
/// it is not an error and does not stop the dossier being built. Traversal is
/// not a concern here: every path is a constant in this module.
fn read(workspace: &Path, relative: &str) -> String {
    std::fs::read_to_string(workspace.join(relative)).unwrap_or_default()
}

/// Assembles the inventor's dossier for `workspace`.
///
/// The order is the argument. `GOAL.md` first, because it says what a result
/// has to satisfy. The approaches next, in full for the closed ones, because
/// not re-proposing a closed idea is the inventor's one hard obligation and a
/// truncated row cannot discharge it. Then the threads, whose table already
/// carries each dead direction's reason untruncated. Then what the library
/// establishes, then the shared brief, then the recent lessons, then whatever
/// fits.
pub(super) fn inventor(workspace: &Path) -> String {
    build(workspace, budget_tokens())
}

/// Assembles the reducer's dossier for `workspace`.
///
/// The order is the argument here too, and it is nearly the inverse of the
/// inventor's. The goal first, for the same reason. Then what the run has
/// *established*, because the reducer's cheapest possible result is noticing
/// that a lemma it was about to call a gap is already in the claim ledger — and
/// a claim ledger truncated away is a lemma proved twice. Then its own ledger
/// and the closed skeletons in full, which is the obligation the inventor has
/// about approaches: a gap discharged three cycles ago must not come back as an
/// open one. Then the threads, then the brief, then whatever fits.
///
/// `research/APPROACHES.md` is absent on purpose, as it is from this role's
/// prompt context. The approach ledger is about method, and a role holding it
/// drifts into proposing methods.
pub(super) fn reducer(workspace: &Path) -> String {
    build_reduction(workspace, budget_tokens())
}

/// Assembles the reducer's dossier against an explicit budget.
///
/// Split from [`reducer`] for the reason [`build`] is split from [`inventor`].
fn build_reduction(workspace: &Path, tokens: u64) -> String {
    let budget = usize::try_from(tokens)
        .unwrap_or(usize::MAX)
        .saturating_mul(CHARS_PER_TOKEN);
    let mut packed = Packed::new(budget);

    packed.verbatim("GOAL.md", &read(workspace, "GOAL.md"));

    packed.section(
        super::claims::CLAIMS_PATH,
        &read(workspace, super::claims::CLAIMS_PATH),
    );

    packed.section(
        super::backward::BACKWARD_PATH,
        &read(workspace, super::backward::BACKWARD_PATH),
    );
    let skeletons = super::backward::collect(workspace);
    let closed: String = skeletons
        .closed()
        .map(super::backward::Skeleton::full)
        .collect::<Vec<_>>()
        .join("\n");
    packed.section("Decompositions this run has already closed", &closed);

    packed.section(
        super::threads::THREADS_PATH,
        &read(workspace, super::threads::THREADS_PATH),
    );

    let brief = read(workspace, super::shared_context::CONTEXT_FILE);
    let brief = super::shared_context::fit(&brief).unwrap_or(brief);
    packed.section(super::shared_context::CONTEXT_FILE, &brief);

    for relative in REMAINDER {
        packed.section(relative, &read(workspace, relative));
    }

    if packed.body.trim().is_empty() {
        return String::new();
    }
    format!(
        "What this run has written down so far, read from the workspace just now rather than at \
         the start of the run. A lemma the claim ledger below already establishes is not a gap, \
         and a gap this ledger records as discharged must not be stated as open again.\n{}",
        packed.body
    )
}

/// Assembles the dossier against an explicit budget.
///
/// Split from [`inventor`] so the packing can be tested at a budget the test
/// chooses. The alternative is setting the environment variable from a test,
/// which this crate cannot do — `set_var` is `unsafe` and `unsafe` is
/// forbidden here — and which would make the tests share process-wide state
/// besides.
fn build(workspace: &Path, tokens: u64) -> String {
    let budget = usize::try_from(tokens)
        .unwrap_or(usize::MAX)
        .saturating_mul(CHARS_PER_TOKEN);
    let mut packed = Packed::new(budget);

    packed.verbatim("GOAL.md", &read(workspace, "GOAL.md"));

    packed.section(
        super::approaches::APPROACHES_PATH,
        &read(workspace, super::approaches::APPROACHES_PATH),
    );
    let approaches = super::approaches::collect(workspace);
    let closed: String = approaches
        .closed()
        .map(super::approaches::Approach::full)
        .collect::<Vec<_>>()
        .join("\n");
    packed.section("Lines of attack this run has already closed", &closed);

    packed.section(
        super::threads::THREADS_PATH,
        &read(workspace, super::threads::THREADS_PATH),
    );
    packed.section(
        super::claims::CLAIMS_PATH,
        &read(workspace, super::claims::CLAIMS_PATH),
    );

    let brief = read(workspace, super::shared_context::CONTEXT_FILE);
    let brief = super::shared_context::fit(&brief).unwrap_or(brief);
    packed.section(super::shared_context::CONTEXT_FILE, &brief);

    packed.section(
        "reflections/INDEX.md",
        &read(workspace, "reflections/INDEX.md"),
    );
    for relative in REMAINDER {
        packed.section(relative, &read(workspace, relative));
    }

    if packed.body.trim().is_empty() {
        return String::new();
    }
    format!(
        "What this run has written down so far, read from the workspace just now rather than at \
         the start of the run. This is the record you are working against: an idea it has already \
         closed is not a new line of attack, however differently it is worded.\n{}",
        packed.body
    )
}

#[cfg(test)]
#[path = "dossier_test.rs"]
mod test;
