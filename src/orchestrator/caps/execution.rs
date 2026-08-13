//! Why a workflow cannot execute code directly here.
//!
//! `TinyFlows` has two node kinds that run something: `code`, backed by the
//! required [`CodeRunner`] capability, and `shell`, backed by the optional
//! [`ShellRunner`](tinyflows::caps::ShellRunner). This crate supplies a
//! [`CodeRunner`] that refuses every call, and supplies no `ShellRunner` at all.
//!
//! That is a decision, not an omission.
//!
//! # The gate a second execution path would skip
//!
//! Running a command in this crate goes through the `execute_command` tool,
//! which requires the caller to declare `complexity` and `complexity_class`
//! first, and to name an `oracle_bound` before it will accept an exponential or
//! factorial one. That check is the enforcement of the shared method policy —
//! the rule that a run must not search the answer space — and it is enforced in
//! code precisely because a prompt instruction is not a control.
//!
//! A `code` node reaching a runner that shells out would be a second way to
//! execute, with no declaration and no check. The method policy would still be
//! written down, still be in every role's prompt, and no longer be enforced
//! anywhere a workflow could reach. That is the exact failure this repository
//! keeps recording about itself.
//!
//! So execution stays on one path. A workflow that needs to run something uses
//! a `tool_call` node naming `execute_command`, declares its complexity like
//! every other caller, and is bounded by the same container limits.
//!
//! # Why refuse rather than omit
//!
//! `Capabilities::code` is not optional, so something has to be there. A runner
//! that returned an empty result would let a workflow "run" code and quietly
//! compute nothing, which is worse than either alternative. Refusing names the
//! reason and points at the supported path, so the failure is legible the first
//! time somebody writes a `code` node. The `shell` capability *is* optional, and
//! `TinyFlows` fails a `shell` node with a capability error when none is
//! injected — which is the same outcome, so it is left unset rather than
//! stubbed.

use async_trait::async_trait;
use serde_json::Value;
use tinyflows::caps::{CodeLanguage, CodeRunner};
use tinyflows::error::{EngineError, Result as EngineResult};

/// A [`CodeRunner`] that refuses, and says where to go instead.
#[derive(Clone, Copy, Debug, Default)]
pub(crate) struct RefusingCodeRunner;

#[async_trait]
impl CodeRunner for RefusingCodeRunner {
    /// Always fails.
    ///
    /// # Errors
    ///
    /// Always returns a capability error naming the supported path. See the
    /// module documentation for why this is not a gap to be filled in later.
    async fn run(
        &self,
        language: CodeLanguage,
        _source: &str,
        _input: Value,
    ) -> EngineResult<Value> {
        Err(EngineError::Capability(format!(
            "this host does not run {language:?} from a `code` node: execution goes through the \
             `execute_command` tool, which requires a declared complexity class. Use a \
             `tool_call` node naming `execute_command`"
        )))
    }
}

#[cfg(test)]
#[path = "execution_test.rs"]
mod test;
