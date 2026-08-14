//! The semantic second stage, and why it is allowed to exist.
//!
//! The deterministic stage matches names, titles and identifiers. It cannot
//! match a paraphrase — a survey that lays out the proof idea without naming
//! anybody, a lecture note that gives the construction and attributes nothing.
//! For a *solved* conjecture that is the dominant leak, because the answer is
//! not a secret string, it is a piece of mathematics that can be said many
//! ways.
//!
//! So flagged text goes to a model, which is asked one question: does this
//! materially reveal a solution to the problem the run is working on?
//!
//! # It is a supplement, never the control
//!
//! `CLAUDE.md` is explicit that a prompt instruction is not a control, and this
//! module does not pretend otherwise. The control is the deterministic stage in
//! [`super::policy`] and the proxy's host allowlist. This stage only ever
//! *adds* denials on top of those, and it runs solely on text the deterministic
//! stage already flagged.
//!
//! # It fails closed
//!
//! A provider error, a timeout, an unparsable reply, or a missing adjudicator
//! all deny the text. The reasoning is asymmetric: wrongly withholding a source
//! costs the run one source, and wrongly delivering one costs the entire
//! calibration, silently, because the run then solves a problem it was handed
//! the answer to and nothing in the output says so.
//!
//! # It is given no secret
//!
//! The adjudicator is asked about *the de-named statement the run already has*.
//! It is never told the real name of the conjecture, its solver, or its
//! solution — so no answer key crosses into the container, and this stage does
//! not reintroduce the leak that hashing the blocklist was there to close.

use std::sync::Arc;
use std::time::Duration;

use tinyagents::harness::message::Message;
use tinyagents::harness::model::{ChatModel, ModelRequest};

/// What the adjudicator concluded.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub(crate) enum Ruling {
    /// The text does not reveal a solution; deliver it.
    Allow,
    /// The text reveals a solution, or the adjudicator could not say so
    /// safely. Withhold it.
    Deny,
}

/// The instruction the adjudicating model is given.
///
/// Written to be answerable from the text alone. It carries no answer key: the
/// problem statement it refers to is the one already in the workspace, which
/// the run wrote or was seeded with.
const INSTRUCTION: &str = "\
You are screening source material for a mathematics research run that is \
working on an open problem. Your only job is to decide whether a piece of text \
would hand the run its answer.

Answer DENY if the text contains or materially reveals any of:
- a complete proof of the problem, or of the problem's main open case;
- an explicit construction, witness, or counterexample that settles it;
- the specific mechanism of a known solution, stated well enough to reproduce;
- a statement that the problem is solved, together with who solved it or how.

Answer ALLOW for everything else, including: background, definitions, partial \
results, related problems, techniques stated generally, historical context that \
does not say the problem was settled, and material about weaker or different \
versions of the problem.

Bias toward ALLOW for ordinary mathematical literature. Bias toward DENY when \
the text reads like a summary or announcement of a settled result.

Reply with exactly one word: ALLOW or DENY.";

/// Asks the model whether `text` reveals a solution to `problem`.
///
/// `problem` is the de-named statement the run is working on, taken from the
/// workspace. `text` is truncated by the caller to the policy's bound.
///
/// Never returns an error: every failure mode is a [`Ruling::Deny`], for the
/// reason in the module documentation. The returned string is a short,
/// non-revealing note for the ledger.
pub(crate) async fn adjudicate(
    model: &Arc<dyn ChatModel<()>>,
    problem: &str,
    text: &str,
    timeout: Duration,
) -> (Ruling, String) {
    let request = ModelRequest::new(vec![
        Message::system(INSTRUCTION),
        Message::user(format!(
            "THE PROBLEM THE RUN IS WORKING ON:\n{problem}\n\n\
             THE TEXT TO SCREEN:\n{text}\n\nALLOW or DENY?"
        )),
    ])
    // One word is the whole answer. The bound is not tight, so a model that
    // reasons briefly before answering is still parsed rather than truncated
    // into an unparsable reply — which would fail closed and cost a source.
    .with_max_tokens(512);

    let response = match tokio::time::timeout(timeout, model.invoke(&(), request)).await {
        Ok(Ok(response)) => response,
        Ok(Err(error)) => {
            return (
                Ruling::Deny,
                format!("adjudicator unavailable ({error}); failing closed"),
            );
        }
        Err(_) => {
            return (
                Ruling::Deny,
                format!(
                    "adjudicator timed out after {}s; failing closed",
                    timeout.as_secs()
                ),
            );
        }
    };

    match parse(&response.text()) {
        Some(ruling) => (ruling, "adjudicated".to_string()),
        None => (
            Ruling::Deny,
            "adjudicator reply was neither ALLOW nor DENY; failing closed".to_string(),
        ),
    }
}

/// Reads a ruling out of a model reply.
///
/// Deliberately strict about which word wins. A reply that reasons before
/// answering may contain both words, and the *last* one is the conclusion —
/// "this could be ALLOW, but ... DENY" means deny. A reply containing neither
/// is not a ruling at all and the caller fails closed on `None`.
fn parse(reply: &str) -> Option<Ruling> {
    let upper = reply.to_ascii_uppercase();
    let allow = upper.rfind("ALLOW");
    let deny = upper.rfind("DENY");
    match (allow, deny) {
        (Some(allow_at), Some(deny_at)) => Some(if deny_at > allow_at {
            Ruling::Deny
        } else {
            Ruling::Allow
        }),
        (Some(_), None) => Some(Ruling::Allow),
        (None, Some(_)) => Some(Ruling::Deny),
        (None, None) => None,
    }
}

#[cfg(test)]
#[path = "adjudicator_test.rs"]
mod test;
