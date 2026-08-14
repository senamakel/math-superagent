//! Withholding a published answer from a run that is being measured.
//!
//! The harness runs against open conjectures, and nothing measures whether it
//! is working. A run produces notes, code and ledgers, but with no known-good
//! trajectory to compare against there is no way to distinguish a harness
//! closing in on a proof from one generating plausible mathematical activity.
//!
//! A **calibration run** supplies the missing reference: a conjecture that has
//! already been solved, stated as open, with the literature carrying its answer
//! withheld. Then the trajectory can be scored against a milestone ladder, and
//! a change to the framework can be judged by whether it moves runs up it. The
//! problems live under `evals/` at the repository root, which is deliberately
//! outside `workspace/` — only `workspace/conjectures/<slug>/` is bind-mounted,
//! so the answer keys are unreachable from a run by construction.
//!
//! This module is the part of that which runs inside the container.
//!
//! # The three layers, and which two are controls
//!
//! 1. **The proxy.** Under `compose.eval.yaml` the agent container is joined to
//!    an internal network with no default route out, and all egress goes
//!    through a proxy holding a host allowlist. This is what closes
//!    `execute_command`, which otherwise runs Python with unrestricted network
//!    and would make everything below decorative. HTTPS `CONNECT` shows a proxy
//!    only `host:port`, so it decides *which hosts are reachable* and nothing
//!    finer.
//! 2. **This module.** Wraps every research tool and `download_document` at
//!    construction. It sees plaintext — including PDF text, which
//!    `super::readable` extracts before a tool returns — so it is the only
//!    layer that can decide *whether an allowed source reveals the answer*.
//! 3. **The leakage audit**, host-side, after the run. Not a control: it
//!    catches what the first two missed, and it catches **recall**, which no
//!    control can stop, by checking the order of events in the trace against
//!    the answer key.
//!
//! # Absent means off
//!
//! With `MATH_AGENT_SCREEN` unset there is no policy and nothing is wrapped, so
//! an ordinary run against a genuinely open problem is untouched. A policy that
//! is named but unreadable stops the run; see [`policy`] for why that is the
//! only safe direction.

mod adjudicator;
mod ledger;
mod policy;
mod screened_tool;
mod terms;

use std::path::{Path, PathBuf};
use std::sync::Arc;

use tinyagents::harness::model::ChatModel;

pub(super) use policy::ScreenPolicy;
use screened_tool::ScreenedTool;

use crate::agent::Tool;

/// Where the de-named statement is read from, relative to the workspace.
const PROBLEM_FILE: &str = "problem.md";

/// The screen, ready to wrap tools.
///
/// Cheap to clone: everything inside is shared. Cloning is the normal case,
/// because the tools it wraps are constructed in more than one place.
#[derive(Clone)]
pub(super) struct Screen {
    policy: Arc<ScreenPolicy>,
    workspace: PathBuf,
    problem: Arc<String>,
    model: Option<Arc<dyn ChatModel<()>>>,
}

impl std::fmt::Debug for Screen {
    /// Names the problem and whether the semantic stage is armed, and nothing
    /// about the terms — a `Debug` line ends up in logs the run can read.
    fn fmt(&self, formatter: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        formatter
            .debug_struct("Screen")
            .field("problem", &self.policy.slug)
            .field("adjudicator", &self.model.is_some())
            .finish_non_exhaustive()
    }
}

impl Screen {
    /// Builds the screen from `MATH_AGENT_SCREEN`, or `None` when unset.
    ///
    /// `model` is used by the semantic stage. Passing `None` leaves the
    /// deterministic stage — the actual control — in force on its own.
    ///
    /// # Errors
    ///
    /// Returns an error when the variable names a policy that cannot be read or
    /// parsed. A calibration run must not continue unscreened.
    pub(super) fn from_env(
        workspace: &Path,
        model: Option<Arc<dyn ChatModel<()>>>,
    ) -> crate::agent::Result<Option<Self>> {
        let Some(policy) = ScreenPolicy::from_env()? else {
            return Ok(None);
        };
        // The statement is what the adjudicator is asked about. Read once, at
        // startup: it is seeded before the run begins, and re-reading it later
        // would hand the adjudicator whatever the run has since written into
        // the file, which is not the question being asked.
        let problem = std::fs::read_to_string(workspace.join(PROBLEM_FILE)).unwrap_or_default();
        // `enabled: false` in the compiled policy turns the semantic stage off
        // without changing any wiring — what an operator wants when a provider
        // is failing and the run should continue on the deterministic stage
        // alone, which is the control in any case.
        let model = model.filter(|_| policy.adjudicator_enabled);
        Ok(Some(Self {
            policy: Arc::new(policy),
            workspace: workspace.to_path_buf(),
            problem: Arc::new(problem),
            model,
        }))
    }

    /// The calibration problem this screen belongs to.
    pub(super) fn slug(&self) -> &str {
        &self.policy.slug
    }

    /// Wraps one tool.
    pub(super) fn wrap(&self, tool: Arc<dyn Tool<()>>) -> Arc<dyn Tool<()>> {
        Arc::new(ScreenedTool::new(
            tool,
            Arc::clone(&self.policy),
            self.workspace.clone(),
            Arc::clone(&self.problem),
            self.model.clone(),
        ))
    }

    /// Wraps every tool in an iterator.
    ///
    /// The common shape at the call sites, which build lists of tools.
    pub(super) fn wrap_all(
        &self,
        tools: impl IntoIterator<Item = Arc<dyn Tool<()>>>,
    ) -> Vec<Arc<dyn Tool<()>>> {
        tools.into_iter().map(|tool| self.wrap(tool)).collect()
    }
}

/// Wraps `tools` when a screen is active, and returns them untouched otherwise.
///
/// The helper exists so a call site reads as one expression rather than as a
/// branch, which is what keeps the wrapping from being forgotten on one of the
/// two paths that construct these tools.
pub(super) fn wrap_all(
    screen: Option<&Screen>,
    tools: impl IntoIterator<Item = Arc<dyn Tool<()>>>,
) -> Vec<Arc<dyn Tool<()>>> {
    match screen {
        Some(screen) => screen.wrap_all(tools),
        None => tools.into_iter().collect(),
    }
}

#[cfg(test)]
#[path = "screen_test.rs"]
mod test;
