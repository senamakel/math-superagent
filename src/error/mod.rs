//! Crate-wide error and result types.
//!
//! Every fallible public function in this crate returns [`Result`], and every
//! failure mode is a distinct [`Error`] variant. Add a variant rather than
//! encoding new context into an existing message: callers match on variants,
//! and message text is not a stable API.
//!
//! Variants carry the data a caller needs to react, keep their `#[error]`
//! message lowercase and free of trailing punctuation, and are documented so
//! the rendered rustdoc explains when each one occurs.

/// Errors returned by this crate.
#[derive(Debug, thiserror::Error, PartialEq, Eq)]
#[non_exhaustive]
pub enum Error {
    /// A required name was empty or contained only whitespace.
    #[error("name must not be empty")]
    EmptyName,
    /// A directive was queued with no text, or only whitespace.
    #[error("directive must not be empty")]
    DirectiveEmpty,
    /// A directive was longer than the queue accepts.
    ///
    /// A directive is a sentence of direction. Something longer belongs in a
    /// workspace file the run can be pointed at, which also keeps one queued
    /// line short enough to be appended in one piece.
    #[error("directive is {actual} characters, over the limit of {limit}")]
    DirectiveTooLong {
        /// Characters a directive may hold.
        limit: usize,
        /// Characters the rejected directive held.
        actual: usize,
    },
    /// A workflow document could not be read, written, or changed.
    ///
    /// Carries what was being attempted as well as what went wrong, because the
    /// same underlying failure — a validation refusal — means something
    /// different when previewing a change than when saving one.
    #[error("could not {action} the workflow: {reason}")]
    Workflow {
        /// What was being attempted, as a gerund.
        action: String,
        /// What the store or the validator reported.
        reason: String,
    },
    /// A workflow diagram could not be rendered to an image file.
    ///
    /// Carries the path rather than only the reason, because the two failures
    /// behind it — an extension the renderer does not support, and a directory
    /// that does not exist — are both answered by looking at the path.
    #[error("could not render the graph diagram to {path}: {reason}")]
    GraphRender {
        /// The image file that could not be written.
        path: String,
        /// What the renderer reported.
        reason: String,
    },
    /// The directive queue, its cursor, or its ledger could not be read or
    /// written.
    #[error("directive queue at {path} is unusable: {reason}")]
    DirectiveQueue {
        /// The file that could not be used.
        path: String,
        /// What the filesystem reported, lowercased by the source.
        reason: String,
    },
}

/// The crate's standard result type.
///
/// Use this alias in public signatures instead of spelling out
/// `std::result::Result<T, Error>`.
pub type Result<T> = std::result::Result<T, Error>;

#[cfg(test)]
#[path = "error_test.rs"]
mod test;
