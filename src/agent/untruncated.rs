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
//! It does not enlarge the cap to do so, and measuring the reasoning channel is
//! why. A turn that reaches the ceiling is spending it on hidden reasoning —
//! `out=24000` against `reasoning_tokens=23999` on every observed case — so it
//! is not short of room, it is failing to emerge, and more room buys a longer
//! silence. The room belongs in the cap itself (`RunBudget`, 48,000 on the same
//! measurement); the re-issue spends its one attempt telling the model that its
//! last turn was discarded. If that fails too, the last response is returned
//! rather than an error, because a truncated answer still beats no answer.

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

// There is deliberately no cap growth here any more, and measuring the hidden
// reasoning channel is what removed it. Every turn that reached the old doubled
// ceiling reported `out=24000` with `reasoning_tokens=23999`: one visible token
// against twenty-four thousand spent thinking. A turn in that state is not short
// of room — it is not emerging — so doubling bought a longer silence and a
// second full generation to pay for it. PE236's `tool_builder` truncated at
// 12,000, was re-issued at 24,000, and had still written nothing five minutes
// later.
//
// The room now lives in the cap itself, which `RunBudget` raised to 48,000 on
// the same evidence, and the re-issue spends its one attempt on telling the
// model what happened instead. See `REISSUE_INSTRUCTION`.

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
        }
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

/// The room a re-issue gets, and it is deliberately far less than the first
/// attempt had.
///
/// The comment on [`MAX_REISSUES`] settled that the cap must not *grow* — a turn
/// reporting `out=24000` with `reasoning_tokens=23999` is not short of room, so
/// doubling bought a longer silence. It stopped there, and the case it did not
/// consider is the one PE620 hit: re-issuing at the *same* 48,000 tokens invites
/// exactly the turn that just failed. Its `tool_builder` truncated at 48,000
/// with no tool call, was asked again with 48,000, and had emitted nothing six
/// and a half minutes later — while the run's own pattern agent wrote in its
/// scratch that `code/` was empty and it was blocked. Across eighteen minutes
/// that run made zero `write_tool_file` and zero `execute_command` calls.
///
/// So the re-issue is given a ceiling low enough that committing to a tool call
/// is the only way to finish inside it. That bounds the wait as well as the
/// behaviour: the request allowance is derived from the cap, so 48,000 tokens
/// can legitimately sit for the full twenty-minute ceiling before anything gives
/// up, and 6,000 cannot.
const REISSUE_OUTPUT_TOKENS: u32 = 6_000;

/// Builds the re-issued request: less room than last time, and the reason it is
/// being asked again.
///
/// The instruction is appended as a system message rather than folded into the
/// existing one, so it arrives *after* the conversation the model was cut off
/// in the middle of. Prepended, it is one more line of standing policy at the
/// top of a long prompt; appended, it is the most recent thing said.
///
/// `min` rather than a flat constant, because a role already running on a small
/// cap must not have its room silently *raised* by being cut off — that would
/// make truncation a way to buy tokens.
fn reissued(request: &ModelRequest, cap: u32) -> ModelRequest {
    let mut retry = request.clone().with_max_tokens(cap.min(REISSUE_OUTPUT_TOKENS));
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
        let Some(cap) = request.max_tokens else {
            // With no cap of our own there is nothing to tell the model about
            // why its turn ended, and no reason to think an identical request
            // would answer differently.
            return Ok(response);
        };
        for _ in 0..MAX_REISSUES {
            if !cut_off(&response) {
                break;
            }
            if let Some(tracer) = self.tracer.as_ref() {
                tracer.note(&format!(
                    "{} model TRUNCATED at {cap} output tokens with no tool call; re-issuing with \
                     the reason at {}",
                    self.agent,
                    cap.min(REISSUE_OUTPUT_TOKENS)
                ));
            }
            response = self.inner.invoke(state, reissued(&request, cap)).await?;
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
