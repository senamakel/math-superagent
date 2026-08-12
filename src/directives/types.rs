//! What one piece of human direction is.

/// One directive an operator sent to a run.
///
/// The identifier is the directive's 1-based position in the queue file rather
/// than a stored field. That is what makes delivery exactly-once without a
/// lock: the runtime's cursor counts consumed lines, so a directive's position
/// and its delivery state are the same number, and there is no stored counter
/// for two writers to disagree about.
#[derive(Clone, Debug, PartialEq, Eq)]
pub struct Directive {
    /// Position in the queue, counted from one over every line including any
    /// the reader could not parse.
    pub id: u64,
    /// When the directive was queued, in milliseconds since the Unix epoch.
    pub at: u64,
    /// Who sent it — `euler-tui`, `steer`, or a caller-supplied label.
    pub from: String,
    /// What the operator asked for.
    pub text: String,
}
