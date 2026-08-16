//! The shared brief, `CONTEXT.md`, and what it is allowed to cost.
//!
//! `CONTEXT.md` is the one workspace file routed into nearly every reasoning
//! role's system prompt, so it is re-sent on every model call those roles make.
//! That makes it the run's most valuable file and its most expensive one at the
//! same time: what it holds, nobody has to re-derive; what it holds
//! needlessly, every agent pays for on every turn.
//!
//! Two things follow, and this module is both of them.
//!
//! The budget is a *number*, not an adjective. It was a sentence in the
//! template — "a thousand tokens, hard" — which is a prompt instruction, and a
//! prompt instruction is not a control. Nothing measured the file, so nothing
//! could say whether the rule held, and the only way to find out what the brief
//! now cost every role was to render the prompts and read the count.
//! [`budget_tokens`] reads it from the environment, [`standing`] measures the
//! file against it, and [`fit`] clamps it on the way into a prompt so a brief
//! that has run away cannot silently double every role's bill.
//!
//! The budget is also *ten thousand tokens*, not one thousand, and the
//! difference is a change of purpose. A thousand tokens buys a list of what the
//! library established, which is close to what `research/INDEX.md` already
//! says. Ten thousand buys the thing an agent would otherwise spend a quarter
//! of an hour rebuilding from disk: what the run believes and why, which
//! approaches are dead and for what reason, what the numbers look like, what
//! the durable memory relates this problem to. That is worth re-sending. A
//! catalogue is not.
//!
//! The clamp is deliberately not a refusal in the write path. Refusing a write
//! costs the run whatever the agent was about to record, and the failure mode
//! here is a file that grew a little past its budget rather than one that
//! doubled — so the honest response is to keep the material, cut the prompt
//! copy at the budget, and tell the curator in its next brief that it now has
//! compressing to do.

use std::path::Path;

use tinyagents::harness::summarization::estimate_tokens;

/// The shared brief's path within a workspace.
pub(super) const CONTEXT_FILE: &str = "CONTEXT.md";

/// What the brief may cost when nothing says otherwise.
///
/// See the module documentation for why this is ten thousand rather than the
/// thousand the template used to ask for.
const DEFAULT_CONTEXT_TOKENS: u64 = 10_000;


/// Characters per token used when clamping.
///
/// `estimate_tokens` is itself an estimate, and the clamp has to cut a string
/// at a byte offset rather than at a token, so this converts the budget into
/// something a slice can be taken at. Four is the estimator's own ratio.
///
/// Shared with [`super::dossier`], which clamps on the same argument. A second
/// copy is exactly the drift [`super::text`] was written to end.
pub(super) const CHARS_PER_TOKEN: usize = 4;

/// Reads the shared brief's token budget from the environment.
///
/// `MATH_AGENT_CONTEXT_TOKENS` overrides it. A missing, empty, unparsable, or
/// zero value keeps [`DEFAULT_CONTEXT_TOKENS`], so a malformed override never
/// silently removes the budget — the same rule [`crate::agent::budget`] applies
/// to every other limit in the runtime.
pub(super) fn budget_tokens() -> u64 {
    positive_env("MATH_AGENT_CONTEXT_TOKENS").unwrap_or(DEFAULT_CONTEXT_TOKENS)
}

/// Reads the ceiling every routed file is held to.
///
/// `MATH_AGENT_PROMPT_FILE_TOKENS` overrides it, under the rule the other two
/// budgets follow: a missing, empty, unparsable or zero value keeps the default
/// rather than silently removing the bound.
///
/// The same ten thousand as the brief and the ledgers, and one number rather
/// than a third: the question this answers is not *what may a brief cost* or
/// *what may a ledger cost* but *what may *any* file cost a prompt*, and a
/// separate value for it would be a second opinion about the same thing.
fn ceiling_tokens() -> u64 {
    positive_env("MATH_AGENT_PROMPT_FILE_TOKENS").unwrap_or(DEFAULT_CONTEXT_TOKENS)
}

/// The ceiling every file routed into a system prompt is held to.
///
/// [`fit`] bounds the brief and [`super::ledger::fit`] bounds the derived
/// ledgers, which between them covered two categories and left every other
/// routed file — `GOAL.md`, `AGENTS.md`, `TASKS.md`, `teams/BOARD.md`, the
/// folder indexes — with no token bound at all. Each of those is written by an
/// agent or by a run, grows by a paragraph a cycle, and is paid for on every
/// model call in every role that carries it. Nothing was watching, and the
/// sizes that need catching are already on disk: `gilbreath-supply/TASKS.md` is
/// 18,532 tokens and `gilbreath/CONTEXT.md` is 11,063.
///
/// Applied *after* every specialised bound, so it never pre-empts one that can
/// cut intelligently — an index drops its fortieth row and says so, where this
/// stops mid-sentence. It is the guard that should never fire, and a file that
/// reaches it is one nothing else is bounding: the fix is a bound where that
/// file is written, not a larger ceiling.
///
/// Returns `None` when the file already fits, which is every file today.
pub(super) fn ceiling(relative: &str, content: &str) -> Option<String> {
    let budget = ceiling_tokens();
    clamp(
        content,
        budget,
        &format!(
            "`{relative}` exceeds the {budget}-token ceiling every file routed into a prompt is \
             held to, and was cut here for this prompt. The whole file is on disk — open it, or \
             grep it, for the rest. A file reaching this ceiling is one nothing else is bounding, \
             which is a defect in whatever writes it."
        ),
    )
}


/// What the brief currently costs, against what it is allowed to cost.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub(super) struct Standing {
    /// Estimated tokens the brief now holds. Zero when it does not exist.
    pub(super) tokens: u64,
    /// Estimated tokens it may hold.
    pub(super) budget: u64,
}

impl Standing {
    /// Tokens still available, or zero when the brief is over budget.
    pub(super) const fn headroom(self) -> u64 {
        self.budget.saturating_sub(self.tokens)
    }

    /// Tokens the brief is over by, or zero when it is within budget.
    pub(super) const fn excess(self) -> u64 {
        self.tokens.saturating_sub(self.budget)
    }
}

/// Measures the workspace's brief against the configured budget.
///
/// A brief that cannot be read — absent, or not UTF-8 — measures as empty
/// rather than as an error. The caller is a background team deciding what to
/// tell an agent, and a missing brief is the ordinary state of a fresh
/// workspace.
pub(super) fn standing(workspace: &Path) -> Standing {
    let tokens = std::fs::read_to_string(workspace.join(CONTEXT_FILE))
        .map(|content| estimate_tokens(&content))
        .unwrap_or_default();
    Standing {
        tokens,
        budget: budget_tokens(),
    }
}

/// Clamps the brief to its budget on the way into a system prompt.
///
/// Returns `None` when the content is already within budget, so the caller
/// keeps its own string in the ordinary case. The replacement keeps the
/// *leading* portion, because the brief is written most-established-first, and
/// says plainly that it was cut — an agent told the brief is truncated reads
/// the file, where one that is not silently believes it has the whole thing.
pub(super) fn fit(content: &str) -> Option<String> {
    let budget = budget_tokens();
    clamp(
        content,
        budget,
        &format!(
            "{CONTEXT_FILE} exceeds its {budget}-token budget and was cut here for this prompt. \
             Read the file for the rest, and compress it."
        ),
    )
}

/// Cuts `content` to `budget` tokens and appends `notice`, or `None` if it fits.
///
/// The one place a prompt-bound file is actually shortened. Three callers wanted
/// the same four lines — [`fit`], [`super::ledger::fit`], and the ceiling in
/// [`super::orchestrator_environment`] — and the four lines are the kind that
/// look trivial until one of them is wrong: a cut that lands mid-character
/// panics inside prompt assembly, which happens at container start, so the run
/// fails before doing any work. Every one of these files carries mathematics, so
/// `δ`, `≤`, `→` and `ν₂` are the norm rather than an edge case.
///
/// The cut keeps the *leading* portion, which is a claim about how these files
/// are written rather than an arbitrary choice: the brief is
/// most-established-first, and every derived ledger puts its table first and its
/// diagnostics last. The head is the part a reader came for.
///
/// `notice` is the caller's because what to do about it is: compress the brief,
/// fix the renderer, or bound the writer. A cut that does not say what it was
/// leaves the model reading a fragment as though it were the whole file.
pub(super) fn clamp(content: &str, budget: u64, notice: &str) -> Option<String> {
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
    Some(format!("{}\n\n_[{notice}]_", &content[..cut]))
}

/// The line the curator wakes up to, telling it what its file now costs.
///
/// The standing is computed per cycle rather than baked into the team's brief
/// at spawn, because it is the one fact that changes between cycles and the one
/// that decides what the cycle is for: adding, or compressing.
pub(super) fn briefing(workspace: &Path) -> String {
    let standing = standing(workspace);
    let Standing { tokens, budget } = standing;
    if standing.excess() > 0 {
        return format!(
            "{CONTEXT_FILE} currently holds ~{tokens} tokens against a budget of {budget}. It is \
             {} over. This cycle is a compression, not an addition: merge duplicated statements, \
             move detail into the file that already holds it and link to it, and drop anything \
             the run has since disproved. Add nothing until it is back within budget.",
            standing.excess()
        );
    }
    format!(
        "{CONTEXT_FILE} currently holds ~{tokens} tokens against a budget of {budget}, so ~{} \
         remain. Spend them only on what an agent would otherwise have to rebuild from disk, and \
         stay within the budget rather than filling it.",
        standing.headroom()
    )
}

/// Reads a strictly positive integer from the environment.
///
/// Duplicated from [`crate::agent::budget`] rather than shared, because that
/// one is private to a module about what a single agent run may spend and this
/// is about what a file may cost; joining them would make one of the two
/// modules import the other for a four-line parser.
pub(super) fn positive_env(name: &str) -> Option<u64> {
    std::env::var(name)
        .ok()?
        .trim()
        .parse::<u64>()
        .ok()
        .filter(|value| *value > 0)
}

#[cfg(test)]
#[path = "shared_context_test.rs"]
mod test;
