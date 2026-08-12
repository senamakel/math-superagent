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
use std::time::Duration;

use tinyagents::harness::summarization::estimate_tokens;

/// The shared brief's path within a workspace.
pub(super) const CONTEXT_FILE: &str = "CONTEXT.md";

/// What the brief may cost when nothing says otherwise.
///
/// See the module documentation for why this is ten thousand rather than the
/// thousand the template used to ask for.
const DEFAULT_CONTEXT_TOKENS: u64 = 10_000;

/// How long the curator waits between cycles when nothing says otherwise.
///
/// Enrichment is custodial work over a workspace that changes underneath it, so
/// it is paced by rate rather than by having run out of things to say.
///
/// Five minutes was the first value and it was not a rounding error against the
/// solve: on three live runs the curator was the largest consumer in the run,
/// once at 28 model calls against `pattern_finder`'s 9 and `tool_builder`'s 7.
/// Narrowing its per-run budget was necessary and not sufficient — that bounds
/// what one cycle may spend, and at five minutes it simply bought more cycles.
/// Fifteen is what a fourth run measured at, one cycle costing six calls, and
/// the cost of the trade is staleness: an attempt now reads a brief that may
/// not know about the last fifteen minutes rather than the last five.
///
/// It stays overridable because staleness is the one property here an operator
/// may reasonably want to buy back, and it stays a *default* rather than a
/// per-launch environment variable because a bound only one workspace's
/// launcher sets is a bound the other workspaces do not have.
const DEFAULT_CYCLE_MINUTES: u64 = 15;

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

/// Reads how often the curator may run.
///
/// `MATH_AGENT_CONTEXT_MINUTES` overrides it, under the same rule.
pub(super) fn cycle_interval() -> Duration {
    Duration::from_secs(
        positive_env("MATH_AGENT_CONTEXT_MINUTES")
            .unwrap_or(DEFAULT_CYCLE_MINUTES)
            .saturating_mul(60),
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
        "{}\n\n_[{CONTEXT_FILE} exceeds its {budget}-token budget and was cut here for this \
         prompt. Read the file for the rest, and compress it.]_",
        &content[..cut]
    ))
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
mod test;
