//! The channel a human uses to direct a run that is already going.
//!
//! Until now a run was closed once it started. It is launched with argv, and
//! nothing reads standard input, listens on a socket, or watches a control
//! file; the budget environment variables are read at launch, and every role's
//! system prompt is assembled exactly once, when the orchestrator is built. So
//! an operator watching a run take a wrong turn could only keep watching, and
//! editing `GOAL.md` on the host mid-run changed no prompt at all — the file
//! had already been read into every system message that would ever be sent.
//!
//! A directive is the missing input. It never blocks: it is left in a queue
//! and picked up at the next point the loop is between steps, in the same
//! spirit as the pattern team's mailbox, which was deliberately detached after
//! a live run spent 56 of its 74 minutes waiting on a support agent it had
//! been made to synchronise with. A human is slower than any support agent, so
//! making the run wait on one would be that failure with a worse constant.
//!
//! # Two files, one writer each
//!
//! The queue lives on the bind mount the container already has, because that
//! is the only thing crossing the sandbox boundary and the sandbox is worth
//! keeping: capabilities dropped, no new privileges, a read-only root
//! filesystem, and exactly one mount. An inbound port would be the first hole
//! in it, and it would buy nothing a file does not already give.
//!
//! Two files, and each has exactly one writer:
//!
//! - [`QUEUE`] is written only by the host, by appending one JSON object per
//!   line, and only read by the runtime.
//! - `config/.directives-cursor` is written only by the runtime, and holds how many lines it has
//!   consumed.
//!
//! Splitting the roles that way is what removes the race rather than managing
//! it. Neither side needs a lock, because neither side ever writes what the
//! other writes, and the one number they share — how far through the file the
//! run has got — is owned by the side that advances it.
//!
//! A reader skips a line it cannot parse instead of failing on it, and still
//! counts it. A host append can in principle interleave with the checkpoint
//! commit that runs over the workspace after every writing tool, and a run
//! that stopped taking direction because one line was torn would be a bad
//! trade for a guarantee nobody needs. Counting the skipped line is what keeps
//! the identifiers and the cursor aligned with the file.

mod types;

#[cfg(test)]
mod test;

use std::fmt::Write as _;
use std::io::Write as _;
use std::path::Path;
use std::time::{SystemTime, UNIX_EPOCH};

use serde_json::{Value, json};

pub use types::Directive;

use crate::{Error, Result};

/// The queue itself, written by the host and read by the run.
pub const QUEUE: &str = "config/directives.jsonl";

/// How many queue lines the run has consumed, written only by the run.
const CURSOR: &str = "config/.directives-cursor";

/// Where the cursor is staged before being renamed over [`CURSOR`].
///
/// A rename within one directory is atomic, and a half-written cursor is the
/// one corruption that would matter here: an unparsable cursor reads as zero,
/// which redelivers every directive the run has already acted on.
const CURSOR_STAGE: &str = "config/.directives-cursor.tmp";

/// The human-readable record of what arrived and what became of it.
pub const LEDGER: &str = "config/DIRECTIVES.md";

/// Characters one directive may hold.
///
/// Chosen so the rendered JSON line stays comfortably under the 4 KiB an
/// append is written in one piece at. A directive is a sentence of direction,
/// not a document; anything longer belongs in a workspace file the run can be
/// pointed at.
const MAX_TEXT: usize = 2000;

/// Characters a sender label may hold.
const MAX_FROM: usize = 64;

/// Queues one directive for a run to pick up.
///
/// `workspace` is the resolved directory that is mounted at `/workspace`, and
/// resolving it is the caller's job: `euler-tui` and `scripts/steer` each
/// refuse traversal and absolute paths before they get here, and this function
/// only ever joins constants onto what it is given. The untrusted input at this
/// layer is the text, which is what is checked.
///
/// The returned identifier is read back after the append, so a second host
/// appending at the same instant can make it one too low. It is a display
/// value; nothing depends on it, and delivery is decided by the cursor.
///
/// # Errors
///
/// Returns [`Error::DirectiveEmpty`] when the text is blank,
/// [`Error::DirectiveTooLong`] when it is longer than the queue accepts, and
/// [`Error::DirectiveQueue`] when the queue cannot be written.
pub fn enqueue(workspace: &Path, from: &str, text: &str) -> Result<Directive> {
    let text = text.trim();
    if text.is_empty() {
        return Err(Error::DirectiveEmpty);
    }
    let length = text.chars().count();
    if length > MAX_TEXT {
        return Err(Error::DirectiveTooLong {
            limit: MAX_TEXT,
            actual: length,
        });
    }
    let from: String = from.trim().chars().take(MAX_FROM).collect();
    let from = if from.is_empty() {
        "unknown".to_string()
    } else {
        from
    };
    let at = now_ms();
    let path = workspace.join(QUEUE);
    if let Some(parent) = path.parent() {
        std::fs::create_dir_all(parent).map_err(|error| queue_error(&path, &error))?;
    }
    // One `write_all` of a complete line, on a handle opened for append. Two
    // senders can then interleave lines but never halves of one line, which is
    // what keeps every reader's skip path an unusual case rather than the
    // normal one.
    let line = format!("{}\n", json!({ "at": at, "from": from, "text": text }));
    let mut file = std::fs::OpenOptions::new()
        .create(true)
        .append(true)
        .open(&path)
        .map_err(|error| queue_error(&path, &error))?;
    file.write_all(line.as_bytes())
        .map_err(|error| queue_error(&path, &error))?;
    let id = count_lines(&path)?;
    Ok(Directive {
        id,
        at,
        from,
        text: text.to_string(),
    })
}

/// Reads the directives a run has not consumed yet, without consuming them.
///
/// This is the read the standing team gates on, so it must stay cheap: an
/// empty queue costs one file read and no model call, which is the same shape
/// as the fingerprint gates the pattern and context teams already use.
///
/// # Errors
///
/// Returns [`Error::DirectiveQueue`] when the queue or cursor cannot be read.
pub fn pending(workspace: &Path) -> Result<Vec<Directive>> {
    let consumed = cursor(workspace)?;
    let queued = read_queue(workspace)?;
    Ok(queued
        .into_iter()
        .filter(|directive| directive.id > consumed)
        .collect())
}

/// Takes every directive the run has not consumed and advances the cursor past
/// them.
///
/// The cursor is advanced to the end of the *file*, not to the last directive
/// returned, so a line that could not be parsed is stepped over once rather
/// than being re-read forever by a reader that keeps failing on it.
///
/// # Errors
///
/// Returns [`Error::DirectiveQueue`] when the queue cannot be read or the
/// cursor cannot be written.
pub(crate) fn drain(workspace: &Path) -> Result<Vec<Directive>> {
    let taken = pending(workspace)?;
    let lines = count_lines(&workspace.join(QUEUE))?;
    write_cursor(workspace, lines)?;
    Ok(taken)
}

/// Appends one directive and what the run did about it to [`LEDGER`].
///
/// The receipt is not decoration. On a channel that never blocks, an operator
/// who sends a directive and sees nothing cannot tell "not picked up yet" from
/// "silently dropped", and the second is the one worth knowing about. This file
/// and the console note the runtime writes beside it are the two places that
/// answer it.
///
/// # Errors
///
/// Returns [`Error::DirectiveQueue`] when the ledger cannot be written.
pub(crate) fn record(workspace: &Path, directive: &Directive, outcome: &str) -> Result<()> {
    let path = workspace.join(LEDGER);
    if let Some(parent) = path.parent() {
        std::fs::create_dir_all(parent).map_err(|error| queue_error(&path, &error))?;
    }
    let mut entry = String::new();
    if !path.exists() {
        entry.push_str(
            "# Directives\n\n\
             What an operator asked this run to do, and what the run did about it. Written by \
             the runtime; edit the queue, not this file.\n",
        );
    }
    let _ = write!(
        entry,
        "\n## {} — from {}\n\n{}\n\n{}\n",
        directive.id,
        directive.from,
        directive.text.trim(),
        outcome.trim()
    );
    let mut file = std::fs::OpenOptions::new()
        .create(true)
        .append(true)
        .open(&path)
        .map_err(|error| queue_error(&path, &error))?;
    file.write_all(entry.as_bytes())
        .map_err(|error| queue_error(&path, &error))
}

/// Reads every directive in the queue, numbered by position.
///
/// A line that is not an object with a usable `text` is counted and skipped.
/// Counting it is what keeps an identifier equal to a line number, and so
/// keeps the cursor meaningful across a torn write.
fn read_queue(workspace: &Path) -> Result<Vec<Directive>> {
    let path = workspace.join(QUEUE);
    let text = match std::fs::read_to_string(&path) {
        Ok(text) => text,
        Err(error) if error.kind() == std::io::ErrorKind::NotFound => return Ok(Vec::new()),
        Err(error) => return Err(queue_error(&path, &error)),
    };
    let mut directives = Vec::new();
    for (index, line) in text.lines().enumerate() {
        let position = u64::try_from(index).unwrap_or(u64::MAX).saturating_add(1);
        if let Some(directive) = parse(line, position) {
            directives.push(directive);
        }
    }
    Ok(directives)
}

/// Turns one queue line into a directive, or nothing when it cannot.
fn parse(line: &str, id: u64) -> Option<Directive> {
    let value: Value = serde_json::from_str(line.trim()).ok()?;
    let text = value.get("text")?.as_str()?.trim();
    if text.is_empty() {
        return None;
    }
    Some(Directive {
        id,
        at: value.get("at").and_then(Value::as_u64).unwrap_or_default(),
        from: value
            .get("from")
            .and_then(Value::as_str)
            .unwrap_or("unknown")
            .to_string(),
        text: text.to_string(),
    })
}

/// Reads how many queue lines the run has already consumed.
///
/// An absent or unreadable cursor is zero, which redelivers the queue rather
/// than losing it. That is the right way round: a directive delivered twice is
/// visible to the operator and harmless, and one dropped is neither.
fn cursor(workspace: &Path) -> Result<u64> {
    let path = workspace.join(CURSOR);
    match std::fs::read_to_string(&path) {
        Ok(text) => Ok(text.trim().parse().unwrap_or_default()),
        Err(error) if error.kind() == std::io::ErrorKind::NotFound => Ok(0),
        Err(error) => Err(queue_error(&path, &error)),
    }
}

/// Stores the cursor by writing it beside the target and renaming it over.
fn write_cursor(workspace: &Path, consumed: u64) -> Result<()> {
    let path = workspace.join(CURSOR);
    let stage = workspace.join(CURSOR_STAGE);
    if let Some(parent) = path.parent() {
        std::fs::create_dir_all(parent).map_err(|error| queue_error(&path, &error))?;
    }
    std::fs::write(&stage, format!("{consumed}\n")).map_err(|error| queue_error(&stage, &error))?;
    std::fs::rename(&stage, &path).map_err(|error| queue_error(&path, &error))
}

/// Counts the lines the queue holds, treating an absent queue as empty.
fn count_lines(path: &Path) -> Result<u64> {
    match std::fs::read_to_string(path) {
        Ok(text) => Ok(u64::try_from(text.lines().count()).unwrap_or(u64::MAX)),
        Err(error) if error.kind() == std::io::ErrorKind::NotFound => Ok(0),
        Err(error) => Err(queue_error(path, &error)),
    }
}

/// Milliseconds since the Unix epoch, or zero on a clock before it.
fn now_ms() -> u64 {
    SystemTime::now()
        .duration_since(UNIX_EPOCH)
        .map_or(0, |since| {
            u64::try_from(since.as_millis()).unwrap_or(u64::MAX)
        })
}

/// Builds the queue error for one path, keeping the message lowercase.
fn queue_error(path: &Path, error: &std::io::Error) -> Error {
    Error::DirectiveQueue {
        path: path.display().to_string(),
        reason: error.to_string(),
    }
}
