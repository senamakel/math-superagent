//! The record of what the screen withheld.
//!
//! Two files, following the pattern the rest of the workspace already uses for
//! derived state: hidden machine-readable JSON beside a committed human-readable
//! ledger, as `research/FRONTIER.md` sits beside `config/.frontier.json`.
//!
//! - `config/screen.jsonl` — one object per decision, appended.
//! - `research/SCREEN.md` — the same decisions as a table a reader opens.
//!
//! # This is evidence, not plumbing
//!
//! The count of denials is one of the two numbers a calibration run exists to
//! produce. A run that never tripped the screen was working from its own
//! reasoning; a run that tripped it forty times was trying to look the answer
//! up and its result means something different. Neither is visible without this
//! ledger, and neither can be reconstructed afterwards from the trace, because
//! a denied result is precisely the thing that never reached the model.
//!
//! What is recorded is the *decision*, never the matched term. Writing the term
//! into a workspace file would undo the whole reason the compiled blocklist is
//! hashed — the ledger is inside the container, and the run can read it.

use std::fmt::Write as _;
use std::path::Path;

use serde_json::json;

/// Where the machine-readable record goes, under the workspace.
const LEDGER_JSONL: &str = "config/screen.jsonl";

/// Where the human-readable record goes, under the workspace.
const LEDGER_MARKDOWN: &str = "research/SCREEN.md";

/// The header the Markdown ledger opens with.
const MARKDOWN_HEADER: &str = "\
# Screen ledger

Every decision the evidence screen made this run. This workspace is a
**calibration** workspace: the problem in `problem.md` is stated as open, and
sources that would hand the run a published solution are withheld in code.

A row here is not a fault. It records that a source was reached for and not
delivered, which is information about how the run was working — and a run with
no rows is as informative as a run with many.

The matched term is deliberately not recorded. Naming it here would put the
withheld name into this workspace, which is the one thing the screen exists to
prevent.

| when | tool | stage | decision | detail |
| --- | --- | --- | --- | --- |
";

/// What the screen was looking at when it decided.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub(crate) enum Stage {
    /// The arguments the model passed, before the call ran.
    Arguments,
    /// The text the tool returned, before the model saw it.
    Result,
}

impl Stage {
    /// The word used for this stage in both ledgers.
    const fn as_str(self) -> &'static str {
        match self {
            Self::Arguments => "arguments",
            Self::Result => "result",
        }
    }
}

/// One decision, ready to be recorded.
#[derive(Clone, Debug)]
pub(crate) struct Entry {
    /// The tool whose call was screened.
    pub(crate) tool: String,
    /// Which side of the call this decision was about.
    pub(crate) stage: Stage,
    /// What was decided, as one lowercase word: `denied`, `redacted`,
    /// `allowed-by-adjudicator`, `denied-by-adjudicator`, `denied-host`, or
    /// `denied-adjudicator-unavailable`.
    pub(crate) decision: &'static str,
    /// A short, non-revealing note — a host, a size, a reason. Never the term
    /// that matched.
    pub(crate) detail: String,
}

/// Appends one decision to both ledgers.
///
/// Best effort by design. A screen that cannot write its ledger has still
/// withheld the text, and failing the tool call because a log line did not land
/// would turn a bookkeeping problem into a lost attempt. The decision itself is
/// also written to the run trace by the caller, so a lost line here is
/// recoverable from the host.
pub(crate) fn record(workspace: &Path, entry: &Entry) {
    let stamp = timestamp();
    append_jsonl(workspace, entry, &stamp);
    append_markdown(workspace, entry, &stamp);
}

fn append_jsonl(workspace: &Path, entry: &Entry, stamp: &str) {
    let line = json!({
        "at": stamp,
        "tool": entry.tool,
        "stage": entry.stage.as_str(),
        "decision": entry.decision,
        "detail": entry.detail,
    });
    let path = workspace.join(LEDGER_JSONL);
    if let Some(parent) = path.parent() {
        let _ = std::fs::create_dir_all(parent);
    }
    if let Ok(mut file) = std::fs::OpenOptions::new()
        .create(true)
        .append(true)
        .open(&path)
    {
        use std::io::Write as _;
        let _ = writeln!(file, "{line}");
    }
}

fn append_markdown(workspace: &Path, entry: &Entry, stamp: &str) {
    let path = workspace.join(LEDGER_MARKDOWN);
    if let Some(parent) = path.parent() {
        let _ = std::fs::create_dir_all(parent);
    }
    let mut row = String::new();
    let _ = write!(
        row,
        "| {stamp} | `{}` | {} | {} | {} |\n",
        entry.tool,
        entry.stage.as_str(),
        entry.decision,
        // A pipe in the detail would break the table, and the detail is host
        // and size text that has no reason to contain one.
        entry.detail.replace('|', "/")
    );
    let existing = std::fs::read_to_string(&path).unwrap_or_default();
    let body = if existing.is_empty() {
        format!("{MARKDOWN_HEADER}{row}")
    } else {
        format!("{existing}{row}")
    };
    let _ = std::fs::write(&path, body);
}

/// Seconds since the Unix epoch, as a string.
///
/// Deliberately not a formatted date: the crate carries no date library, and
/// the ledger's consumer is `scripts/eval-report` on the host, which correlates
/// these against `config/trace.jsonl` and wants a sortable number.
fn timestamp() -> String {
    std::time::SystemTime::now()
        .duration_since(std::time::UNIX_EPOCH)
        .map_or_else(|_| "0".to_string(), |since| since.as_secs().to_string())
}

#[cfg(test)]
#[path = "ledger_test.rs"]
mod test;
