//! Re-issues a turn the provider cut off at the output cap.
//!
//! The vendored loop already recovers one shape of truncation: a turn that
//! ends with `finish_reason == "length"`, no tool calls, and *no text* — the
//! model spent its whole budget on the hidden reasoning channel — is re-issued
//! with the cap doubled. That recovery requires the text to be empty
//! (`response.text().trim().is_empty()`), so it never fires for the shape that
//! costs the most.
//!
//! When a turn ends at the cap having produced text but no tool call, the loop
//! treats it as the turn's final answer and ends the run. The answer is a
//! sentence cut in half. A live run reached exactly this: its root agent
//! truncated at 12,000 tokens, recovered into a 24,000-token turn, spent that
//! entire doubled budget too, and its run then completed on the fragment —
//! after the mathematics underneath it was finished and cross-checked. The
//! result existed; the agent that would report it stopped mid-word, and the
//! child runs still working had nobody left to collect them.
//!
//! So this wrapper applies the same recovery to the case upstream excludes.
//! It sits outside the timeout, affinity, and accounting wrappers, so each
//! re-issue is bounded and routed on its own terms rather than inheriting the
//! cut-off attempt's, and is recorded as the separate paid call it is.
//!
//! It cannot fix a turn that has genuinely run out of things to say within any
//! budget, so growth is clamped exactly as upstream clamps it and the last
//! response is returned rather than an error: degrading to today's behaviour
//! is right, because a truncated answer still beats no answer.

use std::sync::Arc;

use async_trait::async_trait;
use tinyagents::harness::message::Message;
use tinyagents::harness::model::{
    ChatModel, ModelProfile, ModelRequest, ModelResponse, ModelStream,
};

use crate::agent::Result;
use crate::agent::trace::RunTracer;

/// How many times one turn may be re-issued after being cut off.
///
/// One. This was two, matching upstream's 4x clamp, and the second doubling
/// turned out to be pure cost. The evidence is one-sided: a re-issue at twice
/// the cap is what unblocked a run whose every attempt had been ending on a
/// truncated fragment, while a turn that then truncated *again* at twice the
/// cap went on to spend 22.8 minutes generating the full 48,000 tokens and
/// still emitted no tool call. Generation time is linear in output length, so
/// the third attempt is always the most expensive and, on the evidence, the
/// least likely to work.
///
/// A turn that has already failed at twice its budget is not short of room. It
/// is doing something else — usually spending everything on the hidden
/// reasoning channel — and the answer to that is a prompt, not another
/// half-hour of generation. Returning the fragment hands it to upstream's own
/// recovery, which still has its ladder.
const MAX_REISSUES: u32 = 1;

/// Ceiling on cap growth, as a multiple of the run's configured turn cap.
///
/// Twice, so the single re-issue above can double once and no further. Kept as
/// its own bound rather than folded into the count, because they answer
/// different questions: how many extra calls a turn may cost, and how large
/// any one of them may get.
///
/// A multiple of the *configured* cap rather than of whatever this request
/// happens to carry, because this is not the only thing that doubles. The
/// vendored loop recovers its own shape of truncation the same way, so a turn
/// it has already re-issued arrives here at twice the cap — and read as an
/// original, that doubles again. A live `goals` agent reached a 48,000-token
/// re-issue exactly this way, four times the configured ceiling and some
/// twelve minutes of generation, against a wrapper documented to allow twice.
/// Measuring growth from the configured cap makes the two ladders share one
/// ceiling instead of composing into it.
const MAX_CAP_GROWTH: u32 = 2;

/// What a re-issued turn is told, beside being given more room.
///
/// More room alone is not the fix, and four live runs say so. `cut_off`
/// already requires *no tool call at all*, and a turn doing genuine long work
/// emits tool calls — so what reaches this wrapper is almost always a model
/// writing an essay, and doubling its budget buys a longer essay. Project
/// Euler 236's `tool_builder` truncated at 12,000, was re-issued at 24,000, and
/// had still produced nothing five minutes later, with the workspace's `code/`
/// directory empty fifteen minutes into the run.
///
/// So the re-issue carries the one fact the model does not have: that its last
/// turn was discarded. It is phrased as a report of what happened rather than
/// as an instruction to be brief, because brevity is not the goal — a tool call
/// is, and a turn may legitimately be long on the way to one.
const REISSUE_INSTRUCTION: &str = "Your previous turn ran to the output limit without calling \
     a tool, so it produced nothing: the text of a turn is discarded, and only a tool call \
     advances the run. Do not write that analysis again. Call a tool now — the most useful one \
     you can name from what you already know. An imperfect call you can correct next turn is \
     worth more than another turn of reasoning about which call to make.";

/// Wraps a chat model so a turn cut off at the cap is asked for again.
pub struct UntruncatedModel<S: Send + Sync> {
    inner: Arc<dyn ChatModel<S>>,
    tracer: Option<Arc<RunTracer>>,
    agent: String,
    /// The run's configured per-turn output cap, when it is known.
    configured: Option<u32>,
}

impl<S: Send + Sync> std::fmt::Debug for UntruncatedModel<S> {
    fn fmt(&self, formatter: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        formatter
            .debug_struct("UntruncatedModel")
            .finish_non_exhaustive()
    }
}

impl<S: Send + Sync> UntruncatedModel<S> {
    /// Wraps `inner` so its truncated turns are re-issued.
    #[must_use]
    pub fn new(inner: Arc<dyn ChatModel<S>>) -> Self {
        Self {
            inner,
            tracer: None,
            agent: String::new(),
            configured: None,
        }
    }

    /// Tells the wrapper the run's configured per-turn output cap.
    ///
    /// Growth is measured from this rather than from the request's own cap, so
    /// a turn the vendored loop has already doubled is recognised as such and
    /// not doubled a second time. Left unset, growth falls back to the
    /// request's cap, which is the old behaviour and the right degradation:
    /// re-issuing once too generously still beats never re-issuing.
    #[must_use]
    pub fn with_turn_cap(mut self, tokens: u32) -> Self {
        self.configured = Some(tokens);
        self
    }

    /// Announces each re-issue on the operator console.
    ///
    /// Without this a re-issue is invisible where it matters most. The console
    /// prints one line per call the *loop* made, and a re-issue happens inside
    /// one of those, so a turn spending two attempts shows as `model call #2`
    /// followed by many minutes of nothing — indistinguishable from a wedged
    /// request, and the wrong diagnosis leads straight to killing a container
    /// that was working. The cost lands in `trace.jsonl` either way; what was
    /// missing is knowing to look.
    ///
    /// The note names `agent`, because the tracer it prints through belongs to
    /// the run as a whole. Several specialists truncate independently and
    /// concurrently, so an unattributed line says a turn was cut off without
    /// saying whose — which is most of what the reader needs.
    #[must_use]
    pub fn with_tracer(mut self, tracer: Arc<RunTracer>, agent: impl Into<String>) -> Self {
        self.tracer = Some(tracer);
        self.agent = agent.into();
        self
    }
}

/// Builds the re-issued request: more room, and the reason it is being asked again.
///
/// The instruction is appended as a system message rather than folded into the
/// existing one, so it arrives *after* the conversation the model was cut off
/// in the middle of. Prepended, it is one more line of standing policy at the
/// top of a long prompt; appended, it is the most recent thing said.
fn reissued(request: &ModelRequest, cap: u32) -> ModelRequest {
    let mut retry = request.clone().with_max_tokens(cap);
    retry.messages.push(Message::system(REISSUE_INSTRUCTION));
    retry
}

/// Returns whether a response was cut off with no tool call to act on.
///
/// A response carrying tool calls is not truncated in any way that matters:
/// the loop runs them and asks again, so the turn continues regardless of what
/// the provider says about length.
fn cut_off(response: &ModelResponse) -> bool {
    response.finish_reason.as_deref() == Some("length") && response.tool_calls().is_empty()
}

#[async_trait]
impl<S: Send + Sync + 'static> ChatModel<S> for UntruncatedModel<S> {
    fn profile(&self) -> Option<&ModelProfile> {
        self.inner.profile()
    }

    async fn invoke(&self, state: &S, request: ModelRequest) -> Result<ModelResponse> {
        let mut response = self.inner.invoke(state, request.clone()).await?;
        let Some(original) = request.max_tokens else {
            // With no cap of our own to raise, a re-issue would ask for the
            // identical thing and get the identical answer.
            return Ok(response);
        };
        let ceiling = self
            .configured
            .unwrap_or(original)
            .saturating_mul(MAX_CAP_GROWTH);
        let mut cap = original;
        for _ in 0..MAX_REISSUES {
            if !cut_off(&response) || cap >= ceiling {
                break;
            }
            cap = cap.saturating_mul(2).min(ceiling);
            if let Some(tracer) = self.tracer.as_ref() {
                tracer.note(&format!(
                    "{} model TRUNCATED at {} output tokens with no tool call; re-issuing at {cap}",
                    self.agent,
                    cap / 2
                ));
            }
            response = self
                .inner
                .invoke(state, reissued(&request, cap))
                .await?;
        }
        Ok(response)
    }

    async fn stream(&self, state: &S, request: ModelRequest) -> Result<ModelStream> {
        // The streaming path yields incrementally, so there is no completed
        // response to inspect before the caller has already consumed it.
        self.inner.stream(state, request).await
    }
}

#[cfg(test)]
#[path = "untruncated_test.rs"]
mod test;
