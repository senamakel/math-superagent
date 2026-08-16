//! A bounded window over output that may be arbitrarily long.
//!
//! Two things in this runtime read output they do not control the size of: a
//! shell command ([`super::exec`]) and a git invocation ([`super::vcs`]). Both
//! face the same problem and it is not only a context-window one. A program
//! printing a megabyte a second was charged against the container's memory in
//! full before anything trimmed it, so the bound has to apply *as the bytes
//! arrive* rather than to a `Vec<u8>` shortened afterwards.
//!
//! So this keeps the first `head` bytes and a rolling window of the last
//! `tail`, counts everything, and says how much it dropped. Memory is flat in
//! the length of the stream rather than linear in it.
//!
//! # Why the middle rather than the end
//!
//! The two ends are where the information is. A command says what it is doing
//! at the start and whether it worked at the end; a diff names the files first
//! and carries the last hunk last. Keeping a prefix alone loses the verdict,
//! which is the part a caller acts on.
//!
//! The tail gets the larger share, and that is the correction of a measured
//! loss rather than a preference. A program prints its setup first and its
//! conclusion last — the final answer, the assertion that passed, the traceback
//! explaining the failure. Keeping only the head threw away exactly that: a
//! live verification script printed a ~65 KB reconstructed binary string and
//! then its answer, and the answer was what fell off the end, so the run
//! executed correctly and learned nothing from it. The head is kept too,
//! because the first lines carry the command's own echo of what it was doing
//! and a lone tail can be unreadable.

use std::collections::VecDeque;
use std::fmt::Write as _;

/// How much of a budget the beginning of a stream keeps.
///
/// A quarter, so the larger share goes to the end. See the module docs.
const HEAD_SHARE: usize = 4;

/// One stream's output, bounded in memory as it arrives.
#[derive(Debug)]
pub(super) struct Capture {
    head: Vec<u8>,
    tail: VecDeque<u8>,
    total: usize,
    head_budget: usize,
    tail_budget: usize,
}

impl Capture {
    /// Creates a capture keeping at most `budget` bytes in total.
    ///
    /// The split between the two ends is this module's decision rather than the
    /// caller's, so every bounded output in the runtime has the same shape and
    /// a reader who has learnt to read one has learnt to read them all.
    pub(super) fn bounded(budget: usize) -> Self {
        let head_budget = budget / HEAD_SHARE;
        Self {
            head: Vec::new(),
            tail: VecDeque::new(),
            total: 0,
            head_budget,
            tail_budget: budget.saturating_sub(head_budget),
        }
    }

    /// Adds one freshly read chunk, discarding the middle of the stream.
    pub(super) fn push(&mut self, chunk: &[u8]) {
        self.total += chunk.len();
        let mut chunk = chunk;
        if self.head.len() < self.head_budget {
            let take = (self.head_budget - self.head.len()).min(chunk.len());
            self.head.extend_from_slice(&chunk[..take]);
            chunk = &chunk[take..];
        }
        self.tail.extend(chunk.iter().copied());
        while self.tail.len() > self.tail_budget {
            self.tail.pop_front();
        }
    }

    /// How many bytes passed through, including the ones that were dropped.
    ///
    /// The render already reports what it dropped, so only tests read this —
    /// they assert the bound holds on the *input* rather than on the output.
    #[cfg(test)]
    pub(super) fn total(&self) -> usize {
        self.total
    }

    /// Renders what was kept, saying so when anything was dropped.
    ///
    /// Both ends are decoded lossily rather than refused: a program that prints
    /// one invalid byte has still told the run something, and the boundary
    /// between the kept head and the kept tail can fall mid-character anyway.
    pub(super) fn render(&self) -> String {
        let tail = self.tail.iter().copied().collect::<Vec<_>>();
        let kept = self.head.len() + tail.len();
        if self.total <= kept {
            // Nothing was dropped, so the two halves are the whole stream and
            // concatenate back into it exactly.
            let mut whole = self.head.clone();
            whole.extend_from_slice(&tail);
            return String::from_utf8_lossy(&whole).into_owned();
        }
        let dropped = self.total - kept;
        let mut rendered = String::from_utf8_lossy(&self.head).into_owned();
        let _ = write!(
            rendered,
            "\n[{dropped} bytes truncated from the middle; the end of the output follows]\n"
        );
        rendered.push_str(&String::from_utf8_lossy(&tail));
        rendered
    }
}

/// Bounds a string that is already in memory.
///
/// The streaming case is the one [`Capture`] exists for, but a caller holding a
/// complete `String` — a git invocation's stdout, say — wants the same bound and
/// the same "how much was dropped" wording, and should not get a second
/// implementation of it.
pub(super) fn clamp(text: &str, budget: usize) -> String {
    if text.len() <= budget {
        return text.to_string();
    }
    let mut capture = Capture::bounded(budget);
    capture.push(text.as_bytes());
    capture.render()
}

#[cfg(test)]
#[path = "capture_test.rs"]
mod test;
