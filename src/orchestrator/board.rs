//! The board: what one school tells the others while the work is still running.
//!
//! Several schools attack one problem in one workspace, and everything they
//! *establish* already reaches each other — the nine derived ledgers are
//! re-rendered from one-file-per-item directories, so a claim filed by one
//! school is in `research/CLAIMS.md` for all of them on the next write. That
//! covers finished work and nothing else, and finished work is the smaller half
//! of what a collaborator wants.
//!
//! The larger half is the thing that is not a claim yet. Gowers designed a
//! collaboration around exactly this — *"just give quick reactions"*, with the
//! ideal outcome being a solution *"with no single individual having to think
//! all that hard"* — and this runtime is built to refuse it. Every ledger
//! demands a well-formed block, and the scratch is deliberately unreachable
//! from durable recall so that nothing unchecked can come back looking
//! established. `docs/methods-gap-analysis.md` records the consequence as
//! **absent, deliberately**: no role can see another's provisional work at all.
//!
//! That separation is right for a *claim* and wrong for a *hunch*. "The
//! generating-function route is dead, here is why" is worth nothing after the
//! run and everything during it, and it is the single most useful thing one
//! school can say to another — because it is the thing none of the others will
//! discover for themselves. The board is where it goes.
//!
//! # What keeps it honest
//!
//! A post is **asserted, not established**, and the boundary is enforced rather
//! than requested. `BOARD.md` is never an input to any derived ledger: nothing
//! here can become a claim without somebody writing the claim, with its
//! hypotheses, in a note. This is the `director` rule applied to a second
//! source of unevidenced text — the director acts on what a human asserts and
//! is deliberately not given `research/CLAIMS.md`, for fear a role holding the
//! evidence ledger while reading an instruction files the instruction as a
//! finding.
//!
//! # Why there is no lock
//!
//! [`QUEUE`] is append-only, one `write_all` of one complete line on a handle
//! opened for append — the same construction, for the same reason, as
//! [`crate::directives`]. Concurrent posters interleave whole lines and never
//! halves of one, so several schools may post at once with no coordination.
//! [`PATH`] is *derived* from the queue, exactly as every ledger is derived
//! from its notes, so it is never edited and two schools cannot lose each
//! other's rewrites.

use std::fmt::Write as _;
use std::io::Write as _;
use std::path::Path;

use serde_json::{Value, json};

use super::text::truncate;

/// The queue itself: one JSON object per line, appended by any school.
pub(super) const QUEUE: &str = "teams/board.jsonl";

/// The rendered board, derived from [`QUEUE`] and read by every school.
pub(super) const PATH: &str = "teams/BOARD.md";

/// Posts one board may render.
///
/// Bounded because the board is routed into prompts: an unbounded board would
/// grow until it crowded out the work it is about. The newest are kept, since a
/// stale hunch is exactly what stops being worth re-sending.
const MAX_POSTS: usize = 40;

/// Characters one rendered post body is held to.
const BODY_CHARS: usize = 600;

/// Characters a post may be submitted with.
pub(super) const MAX_BODY: usize = 2000;

/// Characters a sender or reference label may hold.
const MAX_LABEL: usize = 64;

/// What a post is for.
///
/// A closed set rather than free text, because the kind decides how another
/// school should read it, and "is this a finding or a guess" is precisely the
/// distinction the board exists to carry without letting the guess become a
/// finding.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub(super) enum Kind {
    /// Something that turned out not to work, and why.
    ///
    /// The most valuable kind, and the reason the board exists: a dead end
    /// found once should be paid for once.
    DeadEnd,
    /// Something learned that is not yet a claim.
    Lesson,
    /// A half-formed thought, offered precisely because it is not finished.
    Hunch,
    /// Something this school has and another may want.
    Offer,
    /// Something this school wants and cannot get to.
    Ask,
}

impl Kind {
    /// Parses the wire name, defaulting to the most conservative reading.
    ///
    /// An unrecognised kind becomes a [`Hunch`](Self::Hunch) rather than being
    /// refused: the post is already written, and losing it to a typo is worse
    /// than filing it under the label that claims the least.
    pub(super) fn parse(value: &str) -> Self {
        match value.trim().to_ascii_lowercase().as_str() {
            "dead-end" | "dead_end" | "deadend" => Self::DeadEnd,
            "lesson" => Self::Lesson,
            "offer" => Self::Offer,
            "ask" => Self::Ask,
            _ => Self::Hunch,
        }
    }

    /// The wire name.
    pub(super) const fn label(self) -> &'static str {
        match self {
            Self::DeadEnd => "dead-end",
            Self::Lesson => "lesson",
            Self::Hunch => "hunch",
            Self::Offer => "offer",
            Self::Ask => "ask",
        }
    }

    /// Every kind, for the schema that lists them.
    pub(super) const ALL: [Self; 5] = [
        Self::DeadEnd,
        Self::Lesson,
        Self::Hunch,
        Self::Offer,
        Self::Ask,
    ];
}

/// One thing a school said to the others.
#[derive(Clone, Debug)]
pub(super) struct Post {
    /// The school that posted it.
    pub(super) from: String,
    /// What kind of thing it is.
    pub(super) kind: Kind,
    /// What was said.
    pub(super) body: String,
    /// Claim ids, thread slugs or paths it refers to. May be empty.
    pub(super) refers: Vec<String>,
}

/// Appends one post to the queue.
///
/// The append is a single `write_all` of a complete line, which is what lets
/// several schools post concurrently without a lock. See the module
/// documentation.
///
/// # Errors
///
/// Returns an error when the body is blank or longer than the queue accepts, or
/// when the queue cannot be written.
pub(super) fn post(
    workspace: &Path,
    from: &str,
    kind: Kind,
    body: &str,
    refers: &[String],
) -> crate::agent::Result<()> {
    let body = body.trim();
    if body.is_empty() {
        return Err(tinyagents::TinyAgentsError::Validation(
            "a board post needs a body".into(),
        ));
    }
    if body.chars().count() > MAX_BODY {
        return Err(tinyagents::TinyAgentsError::Validation(format!(
            "a board post is held to {MAX_BODY} characters; post the summary and file the rest"
        )));
    }
    let from: String = label(from);
    let refers: Vec<Value> = refers
        .iter()
        .map(|item| Value::String(label(item)))
        .filter(|item| !item.as_str().unwrap_or_default().is_empty())
        .collect();
    let path = workspace.join(QUEUE);
    if let Some(parent) = path.parent() {
        std::fs::create_dir_all(parent).map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!("failed to create the board directory: {error}"))
        })?;
    }
    let line = format!(
        "{}\n",
        json!({
            "at": now_ms(),
            "from": from,
            "kind": kind.label(),
            "body": body,
            "refers": refers,
        })
    );
    let mut file = std::fs::OpenOptions::new()
        .create(true)
        .append(true)
        .open(&path)
        .map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!("failed to open the board: {error}"))
        })?;
    file.write_all(line.as_bytes()).map_err(|error| {
        tinyagents::TinyAgentsError::Tool(format!("failed to write to the board: {error}"))
    })?;
    render_to_disk(workspace);
    Ok(())
}

/// Re-derives [`PATH`] from the queue, beside the append that changed it.
///
/// The render belongs *here*, not at a call site. It used to sit in the
/// `post_board` tool, and a live run showed what that costs: the automatic
/// decomposition offer in [`super::loop_steps`] calls [`post`] directly, so two
/// schools posted, `teams/board.jsonl` held both, and `teams/BOARD.md` was never
/// written at all — the board every school is told to read did not exist. A
/// second posting path is ordinary; a second place that has to remember to
/// render is the bug.
///
/// Best effort, like every ledger refresh: a board that will not render must not
/// fail the post that succeeded.
fn render_to_disk(workspace: &Path) {
    let posts = collect(workspace);
    let _ = std::fs::write(workspace.join(PATH), render(&posts));
}

/// Reads every readable post from the queue, oldest first.
///
/// A line that will not parse is skipped rather than failing the read. The
/// append discipline makes a torn line unusual, and one unreadable post must
/// not cost the board every other post on it.
pub(super) fn collect(workspace: &Path) -> Vec<Post> {
    let Ok(raw) = std::fs::read_to_string(workspace.join(QUEUE)) else {
        return Vec::new();
    };
    raw.lines()
        .filter_map(|line| serde_json::from_str::<Value>(line).ok())
        .filter_map(|value| {
            let body = value.get("body")?.as_str()?.trim().to_string();
            if body.is_empty() {
                return None;
            }
            Some(Post {
                from: value
                    .get("from")
                    .and_then(Value::as_str)
                    .unwrap_or("unknown")
                    .to_string(),
                kind: Kind::parse(value.get("kind").and_then(Value::as_str).unwrap_or_default()),
                body,
                refers: value
                    .get("refers")
                    .and_then(Value::as_array)
                    .map(|items| {
                        items
                            .iter()
                            .filter_map(Value::as_str)
                            .map(ToOwned::to_owned)
                            .collect()
                    })
                    .unwrap_or_default(),
            })
        })
        .collect()
}

/// Renders the board that every school reads.
///
/// Newest first, because a board is read to find out what has just happened,
/// and grouped by kind rather than by school: a reader wants the dead ends
/// before the asks regardless of who found them.
pub(super) fn render(posts: &[Post]) -> String {
    let mut out = String::from(
        "# Board\n\nWhat each school has told the others while the work is running. Derived from \
         `teams/board.jsonl`; do not edit.\n\nEverything here is **asserted, not established**. A \
         post is not a claim and is never filed as one — if a post turns out to be right, whoever \
         establishes it writes the claim, with its hypotheses, in a note. Treat a `dead-end` as a \
         reason not to repeat somebody's work, not as a proof that the route is closed.\n",
    );
    if posts.is_empty() {
        out.push_str("\nNothing posted yet.\n");
        return out;
    }
    let shown = posts.len().saturating_sub(MAX_POSTS);
    for kind in Kind::ALL {
        let matching: Vec<&Post> = posts
            .iter()
            .skip(shown)
            .rev()
            .filter(|post| post.kind == kind)
            .collect();
        if matching.is_empty() {
            continue;
        }
        let _ = write!(out, "\n## {}\n\n", kind.label());
        for post in matching {
            let _ = write!(out, "- **{}**: {}", post.from, truncate(&post.body, BODY_CHARS));
            if !post.refers.is_empty() {
                let _ = write!(out, " (refers: {})", post.refers.join(", "));
            }
            out.push('\n');
        }
    }
    if shown > 0 {
        let _ = write!(
            out,
            "\n{shown} older post(s) are in `{QUEUE}` and not shown here.\n"
        );
    }
    out
}

/// Trims a label to something that cannot dominate a rendered row.
fn label(value: &str) -> String {
    value.trim().chars().take(MAX_LABEL).collect()
}

/// Milliseconds since the epoch, or zero if the clock is before it.
fn now_ms() -> u64 {
    std::time::SystemTime::now()
        .duration_since(std::time::UNIX_EPOCH)
        .map_or(0, |since| u64::try_from(since.as_millis()).unwrap_or(u64::MAX))
}

#[cfg(test)]
#[path = "board_test.rs"]
mod test;
