//! Run budgets for long mathematical investigations.
//!
//! `TinyAgents` defaults a run to 25 model calls, 50 tool calls, and no wall
//! clock cap, and fails the whole run when a cap trips. Those defaults suit a
//! short question-answering turn. A research problem that has to be understood,
//! researched, derived, implemented, and verified needs a much larger budget,
//! and losing every intermediate result at the cap is the worst possible
//! outcome. This module centralises the budget and reads overrides from the
//! environment so a single run can be widened without a rebuild.

use std::time::Duration;

use tinyagents::harness::limits::LimitBehavior;
use tinyagents::harness::runtime::{PayloadCapture, RunPolicy};

/// Model calls allowed in one agent run before it stops with partial results.
const DEFAULT_MAX_MODEL_CALLS: usize = 250;
/// Tool calls allowed in one agent run.
///
/// Deliberately far above what `DEFAULT_MAX_MODEL_CALLS` turns of parallel tool
/// calling can reach, so the model-call cap is the one that actually trips.
/// `LimitBehavior::StopWithPartial` is honoured on the model-call path in the
/// vendored agent loop but not on the tool-call path, which still fails the run
/// outright (`vendor/tinyagents/src/harness/agent_loop/tools.rs`). Until that is
/// fixed upstream, keeping the tool cap out of reach is what makes a budgeted
/// stop graceful instead of destructive. Do not narrow this to "just above" the
/// model cap: one model turn can request several tool calls at once.
const DEFAULT_MAX_TOOL_CALLS: usize = 4_000;
/// Wall-clock ceiling for one agent run, in minutes.
///
/// Sixty, raised from thirty on 2026-08-17, and the number trades one real
/// failure against another rather than fixing either.
///
/// The case for thirty was about the *solution loop*, not about any single
/// agent. The loop's attempt is one `goals` run, and the judge only scores an
/// attempt once it returns — so on an open conjecture, where `goals` is told to
/// pursue the goal until it is met, the attempt never concludes and nothing is
/// ever judged. Four live runs sat inside attempt 1 for thirty-six minutes with
/// zero judge verdicts, zero reflections and zero inventor spawns between them,
/// while all the work happened in children the attempt had spawned. Thirty
/// minutes bought four verdicts a session where two hours bought one.
///
/// The case against it is the other side of the same clock, and it falls on the
/// children. This bounds *every* agent run, not only the attempt, and a live
/// `tool_builder` spent 1,362 seconds inside a single model call — twenty-three
/// minutes of one turn — which left almost nothing of a thirty-minute run. A
/// specialist whose job is a certificate sweep or a Lean development cannot do
/// it in what remains, and unlike the model-call cap this path does not honour
/// `StopWithPartial`: the run loses its context and its report. What is on disk
/// survives, and `continuation_briefing` is what lets the next attempt pick the
/// work up rather than starting over.
///
/// Sixty was chosen deliberately, giving the children room at the cost of
/// halving the judge's cadence — roughly two verdicts a session where there
/// were four. If a run stops being scored often enough to reach
/// `STUCK_THRESHOLD` or `open_invention`, that is this constant, and
/// `MATH_AGENT_RUN_MINUTES` narrows it for a run that wants the old cadence
/// back.
const DEFAULT_RUN_MINUTES: u64 = 60;
/// Wall-clock ceiling for a single tool call, in minutes.
///
/// Thirty, raised from ten on 2026-08-17, and the raise is about a shape of
/// work rather than about slow tools. The tool call is where a run's whole
/// computational arm lives — the enumeration, the exact-rational sweep, the
/// `lean_check`. Ten minutes bounds all three below anything a certificate
/// argument needs: the `ProofAtlas` Sendov bundle's finite arm regenerates
/// 16,862 exact leaves and its Lean build takes twenty minutes at one worker,
/// so at ten a run cannot even attempt that shape, and the timeout answers the
/// question before the mathematics does.
///
/// It stays *below* [`DEFAULT_RUN_MINUTES`] on purpose, and that is what caps
/// the raise at half of it. A tool ceiling at or above the run ceiling means
/// the run clock trips first, and that path does not honour `StopWithPartial` —
/// the run loses its context and its report, where an expired tool call returns
/// the output captured so far with the timeout reported as the exit status.
/// Keeping the tool ceiling the inner bound is what makes a slow computation
/// evidence instead of a loss, and `budget_test.rs` asserts the ordering.
/// Raising this past the run ceiling needs `MATH_AGENT_RUN_MINUTES` raised with
/// it.
const DEFAULT_TOOL_MINUTES: u64 = 30;
/// Output tokens allowed in one model turn.
///
/// Left unset, a turn ran to 9,361 tokens and took 2.9 minutes, and longer
/// turns took over seven. The model was not hanging: it was writing an essay
/// where a decision was wanted. Generation is linear in output length, so an
/// uncapped turn is an uncapped wall clock, and a run spends its budget on
/// prose nobody reads instead of on executing anything.
///
/// This is a safety ceiling, not a behavioural control, and the difference
/// matters. Set to 4,000 it bound a normal turn exactly: the model was
/// truncated mid-generation, emitted no usable tool call, and the loop retried
/// — spending 66 seconds to accomplish nothing, which is worse than the long
/// turn it was meant to shorten. A cap that trips routinely does not make a
/// model concise, it makes it repeat itself.
///
/// Twelve thousand sat above the largest *visible* turn observed (9,361), and
/// that was the wrong quantity to measure. This cap bounds total generated
/// tokens, and on a reasoning model most of them are never visible: across
/// 4,180 accounted calls on a live Erdős–Gyárfás run, **77.8%** of all output
/// tokens went to the hidden reasoning channel (4,079,727 of 5,246,058). Every
/// turn that reached the re-issue ceiling reported `out=24000` with
/// `reasoning_tokens=23999` — one visible token. So a 12,000 cap was not
/// budgeting twelve thousand tokens of answer; it was budgeting roughly 2,600,
/// and cutting the model off mid-thought before it could act.
///
/// The measured distribution is heavily skewed rather than broadly large: over
/// 152 turns, the median was 461 tokens and the 90th percentile 5,352. Only 3
/// turns in 152 hit the cap. Raising it therefore costs nothing on the common
/// path — a cap is not an allowance, and a turn that needs 500 tokens still
/// takes 500 — while removing the ceiling from the 2% that were being
/// truncated into a wasted re-issue.
///
/// Forty-eight thousand, and it stays a safety ceiling: generation is linear in
/// output length, so this is also the wall clock for one turn. The evidence
/// that it is not an invitation to spend is the same distribution — the median
/// turn uses one percent of it.
const DEFAULT_TURN_OUTPUT_TOKENS: u32 = 48_000;

/// Attempts allowed for one model call, counting the first try.
///
/// The vendored defaults are four attempts backing off from 200ms, which suits
/// a fast API returning a clean 503. They do not suit this runtime: a provider
/// stream that drops mid-body surfaces as a decode failure, and three retries
/// spaced under two seconds all hit the same bad minute and exhaust before the
/// condition clears. Both a longer ladder and a slower one are needed.
const DEFAULT_MODEL_ATTEMPTS: usize = 7;
/// First backoff between model-call attempts, in milliseconds.
const DEFAULT_BACKOFF_MS: u64 = 2_000;
/// Longest backoff between model-call attempts, in milliseconds.
const DEFAULT_MAX_BACKOFF_MS: u64 = 60_000;

/// Model calls one judging run may spend.
///
/// Twelve. A verdict needs the report, and at most a look at one or two files
/// to check a claim in it against what is on disk. Everything past that is the
/// judge starting to solve the problem, which is the thing it exists not to
/// do.
const JUDGING_MODEL_CALLS: usize = 12;

/// Model calls one scribing run may spend.
///
/// Twenty, and the number comes from a live run rather than a guess. Given
/// document tools and no bound, the scribe spent 180 of 191 tool calls
/// re-issuing one identical `grep_workspace` for `SimpleGraph`, 19 output
/// tokens at a time, and never wrote a file. A small model that has lost the
/// thread does not notice; it repeats. The tools that fuelled that are gone,
/// and this is the backstop for the next shape the same failure takes.
///
/// Twenty is enough for the work: write the file, check it, and repair it a
/// handful of times, which is what a measured repair loop took.
const SCRIBING_MODEL_CALLS: usize = 20;

/// Tool calls one scribing run may spend.
///
/// Two per model call is the natural shape here — write, then check — and the
/// margin is for the reads a repair needs.
const SCRIBING_TOOL_CALLS: usize = 50;

/// Tool calls one judging run may spend.
///
/// Kept well above the model-call cap for the reason the main budget is: one
/// turn can request several reads, and the graceful cap must be the model one.
const JUDGING_TOOL_CALLS: usize = 60;

/// Wall clock one judging run may spend.
///
/// Five minutes, against an attempt that takes the better part of an hour.
/// This is the ceiling for a pathological turn, not the expected cost — a
/// judge answering as instructed returns in seconds.
const JUDGING_RUN_TIMEOUT: Duration = Duration::from_mins(5);

/// Model calls a housekeeping run may spend.
///
/// Same argument as [`JUDGING_MODEL_CALLS`] and the same evidence. Filing is a
/// bounded job — read a directory listing, write a row per file — against a
/// default budget sized for an investigation, and a role left with an
/// investigation's budget investigates. Two live runs spent 60% and 64% of
/// every model call they made inside the organizer, and the cause was not that
/// it ran often: it ran nine and ten times. It ran *long*. One organizer run
/// spent 62 model calls tidying, another 56, against a solve that had spent 14
/// on the mathematics.
///
/// Reaching this cap is safe, which is what makes a tight one right rather than
/// a gamble. `StopWithPartial` keeps whatever rows were written, and a file
/// left undescribed shows in `INDEX.md` as a visible gap rather than as an
/// index that quietly disagrees with its folder — which is the behaviour the
/// index tools were designed around in the first place.
const HOUSEKEEPING_MODEL_CALLS: usize = 25;

/// Tool calls a housekeeping run may spend.
///
/// Well above the model-call cap for the reason the global tool cap is: one
/// model turn can request several tool calls, and the tool-call path still
/// fails a run outright rather than stopping with partial results.
const HOUSEKEEPING_TOOL_CALLS: usize = 300;

/// Output tokens the inventor may spend in one turn.
///
/// The one role whose product *is* the long turn. Everywhere else a turn that
/// reaches [`DEFAULT_TURN_OUTPUT_TOKENS`] is a model writing an essay where a
/// decision was wanted, which is the failure that cap exists to bound. The
/// inventor is asked for three genuinely different lines of attack with the
/// actual mathematics named in each — a transform, a bijection, an invariant —
/// and that is legitimately several thousand tokens before it has written
/// anything to disk.
///
/// Twelve thousand was binding on it in practice. A live Project Euler 597 run
/// cut the inventor off mid-answer with no tool call at all, and the re-issue
/// that followed spent a second full turn reaching the same place: five model
/// calls, nine tool calls, every one a read, and the three candidates left in
/// prose that never reached `research/approaches/`. A cap that trips routinely
/// does not make a model concise — the note on [`DEFAULT_TURN_OUTPUT_TOKENS`]
/// already says so, and this is that argument applied to the role it binds.
///
/// Thirty-two thousand, and it stays a safety ceiling rather than an
/// allowance: generation is linear in output length, so this is also the
/// inventor's wall clock. It is paired with a control that checks the files
/// were actually written, because a larger cap buys room to comply and does
/// not make complying more likely.
///
/// It now sits *below* [`DEFAULT_TURN_OUTPUT_TOKENS`], which measuring the
/// reasoning channel raised to 48,000, so on a default run this is inert —
/// [`RunBudget::for_invention`] takes the larger of the two. It is kept rather
/// than deleted because it is a floor, not a value: an operator who narrows
/// `MATH_AGENT_TURN_OUTPUT_TOKENS` for a cheap run narrows every role, and the
/// inventor is the one whose product is the long turn. Deleting it would make
/// that narrowing silently reintroduce the truncation it was written for.
const INVENTION_TURN_OUTPUT_TOKENS: u32 = 32_000;

/// Wall-clock ceiling for a role whose children run inside its own clock.
///
/// Three hours, and the number is a ratio rather than a duration: it is the
/// same invariant as [`DEFAULT_TOOL_MINUTES`] sitting below
/// [`DEFAULT_RUN_MINUTES`], applied one level up. A tool call must fit inside
/// the run that makes it; a *delegating* run must likewise fit its children,
/// and `goals` is the role that fans out and collects. Left on the default it
/// was given exactly the ceiling its own children have, so a single child that
/// used its allowance exhausted the parent's — the parent could not finish
/// inside a bound it shared with the work it was waiting on.
///
/// Measured on the ten-run Erdős fleet on 2026-08-19, before this existed:
/// **52 of 57 `goals` runs failed**, every one on
/// `run timed out: exceeded its remaining wall-clock`. The call caps were
/// nowhere near binding — the failures spent a median of 31 model calls
/// against [`DEFAULT_MAX_MODEL_CALLS`] of 250, and 25–94 tool calls against
/// 4,000 — so the ceiling that fails a run outright was tripping at under a
/// quarter of the one that stops gracefully. That is the inversion the note on
/// housekeeping already forbids, and this is that rule applied to the role it
/// binds.
///
/// A model-call cap deliberately is *not* the fix here, and the measurement is
/// why: completed runs spent a median of 30 model calls and failed runs 31, so
/// the two are indistinguishable by call count. What separates them is time per
/// call, which no call cap can see — narrowing one would cut the runs that
/// succeed by exactly as much as the ones that time out.
///
/// It widens rather than narrows, like [`RunBudget::for_invention`], and `max`
/// rather than assignment so an operator who raised `MATH_AGENT_RUN_MINUTES`
/// above it keeps their value. [`DEFAULT_TOOL_MINUTES`] stays the inner bound,
/// so an expired tool call still returns its output rather than failing the
/// run.
const ORCHESTRATION_RUN_MINUTES: u64 = 180;

// There is deliberately no housekeeping wall-clock ceiling. Narrowing one to
// ten minutes was tried and was a mistake: 25 model calls at the turn lengths
// this runtime actually sees do not fit in ten minutes, so the organizer
// reliably hit the clock instead of the call cap. Two live organizer runs died
// on `run timed out: exceeded its remaining wall-clock` after spending 20 and
// 13 model calls, and the wall-clock path does not honour `StopWithPartial` —
// so every row they had written was discarded and the filing had to be redone.
// That is the same rule the tool-call cap already follows: whatever else is
// bounded, the *graceful* cap must be the one that trips, so any ceiling that
// fails a run outright has to stay out of reach.

/// The resolved budget shared by the orchestrator and every specialist.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub struct RunBudget {
    /// Maximum model calls in one agent run.
    pub max_model_calls: usize,
    /// Maximum tool calls in one agent run.
    pub max_tool_calls: usize,
    /// Maximum wall-clock time for one agent run.
    pub run_timeout: Duration,
    /// Maximum wall-clock time for one tool call.
    pub tool_timeout: Duration,
    /// Maximum output tokens for one model turn.
    pub max_turn_output_tokens: u32,
}

impl Default for RunBudget {
    fn default() -> Self {
        Self {
            max_model_calls: DEFAULT_MAX_MODEL_CALLS,
            max_tool_calls: DEFAULT_MAX_TOOL_CALLS,
            run_timeout: Duration::from_secs(DEFAULT_RUN_MINUTES * 60),
            tool_timeout: Duration::from_secs(DEFAULT_TOOL_MINUTES * 60),
            max_turn_output_tokens: DEFAULT_TURN_OUTPUT_TOKENS,
        }
    }
}

impl RunBudget {
    /// Reads the budget from the environment, falling back to the defaults.
    ///
    /// Recognised variables are `MATH_AGENT_MAX_MODEL_CALLS`,
    /// `MATH_AGENT_MAX_TOOL_CALLS`, `MATH_AGENT_RUN_MINUTES`, and
    /// `MATH_AGENT_TOOL_MINUTES`. A missing, empty, unparsable, or zero value
    /// keeps the default, so a malformed override never silently disables a
    /// budget.
    #[must_use]
    pub fn from_env() -> Self {
        let defaults = Self::default();
        Self {
            max_model_calls: positive_env("MATH_AGENT_MAX_MODEL_CALLS")
                .and_then(|value| usize::try_from(value).ok())
                .unwrap_or(defaults.max_model_calls),
            max_tool_calls: positive_env("MATH_AGENT_MAX_TOOL_CALLS")
                .and_then(|value| usize::try_from(value).ok())
                .unwrap_or(defaults.max_tool_calls),
            run_timeout: positive_env("MATH_AGENT_RUN_MINUTES")
                .map_or(defaults.run_timeout, |value| {
                    Duration::from_secs(value.saturating_mul(60))
                }),
            tool_timeout: positive_env("MATH_AGENT_TOOL_MINUTES")
                .map_or(defaults.tool_timeout, |value| {
                    Duration::from_secs(value.saturating_mul(60))
                }),
            max_turn_output_tokens: positive_env("MATH_AGENT_TURN_OUTPUT_TOKENS")
                .and_then(|value| u32::try_from(value).ok())
                .unwrap_or(defaults.max_turn_output_tokens),
        }
    }

    /// Returns this budget narrowed to what judging one attempt should cost.
    ///
    /// The judge sits on the critical path: every attempt waits for it before
    /// it can be reflected on. Its job is to read a report and answer in four
    /// lines, so an investigation's budget is the wrong size for it — and left
    /// with one, it investigates. A live judge spent four minutes, fifteen
    /// model calls, and a 6,906-token turn reading `CONTEXT.md` and the
    /// programs the attempt had written, while the attempt it was judging sat
    /// finished and waiting.
    ///
    /// Reaching the cap is safe by construction, which is what makes a tight
    /// one the right answer rather than a gamble. The run stops with partial
    /// results, so a judge cut off before its verdict returns something the
    /// loop cannot parse — and an unparsable verdict is PROCEED, because a
    /// judge the loop cannot read must not throw work away by accident.
    #[must_use]
    pub fn for_judging(self) -> Self {
        Self {
            max_model_calls: self.max_model_calls.min(JUDGING_MODEL_CALLS),
            max_tool_calls: self.max_tool_calls.min(JUDGING_TOOL_CALLS),
            run_timeout: self.run_timeout.min(JUDGING_RUN_TIMEOUT),
            ..self
        }
    }

    /// Narrows this budget to what writing one Lean file needs.
    ///
    /// Only ever narrows, like [`Self::for_judging`]. The wall clock is left
    /// alone: Mathlib elaboration is the slowest thing in the image and a tight
    /// timeout would fail a file the kernel was about to accept.
    #[must_use]
    pub fn for_scribing(self) -> Self {
        Self {
            max_model_calls: self.max_model_calls.min(SCRIBING_MODEL_CALLS),
            max_tool_calls: self.max_tool_calls.min(SCRIBING_TOOL_CALLS),
            ..self
        }
    }

    /// Narrows this budget to what a filing run needs.
    ///
    /// Only ever narrows, like [`Self::for_judging`]: an environment override
    /// that lowered the defaults below these numbers must stay lowered.
    ///
    /// The wall clock is deliberately left alone. Unlike the model-call cap it
    /// fails a run outright rather than stopping with partial results, so a
    /// tight one turns a bounded filing job into discarded work.
    #[must_use]
    pub fn for_housekeeping(self) -> Self {
        Self {
            max_model_calls: self.max_model_calls.min(HOUSEKEEPING_MODEL_CALLS),
            max_tool_calls: self.max_tool_calls.min(HOUSEKEEPING_TOOL_CALLS),
            ..self
        }
    }

    /// Widens this budget to what proposing a line of attack needs.
    ///
    /// The one place a budget widens rather than narrows, and the exception is
    /// deliberate. [`Self::for_judging`] and [`Self::for_housekeeping`] bound
    /// *authority* — how far a role may wander from its job — and an operator
    /// who lowered the defaults meant to lower them. The turn cap bounds
    /// nothing of the sort: it is a safety ceiling on one generation, and on
    /// this role it was cutting the work off rather than bounding a
    /// pathological turn. See `INVENTION_TURN_OUTPUT_TOKENS` for the evidence.
    ///
    /// `max` rather than assignment, so an operator who raised
    /// `MATH_AGENT_TURN_OUTPUT_TOKENS` above this keeps their value.
    #[must_use]
    pub fn for_invention(self) -> Self {
        Self {
            max_turn_output_tokens: self
                .max_turn_output_tokens
                .max(INVENTION_TURN_OUTPUT_TOKENS),
            ..self
        }
    }

    /// Widens this budget for a role that delegates and waits on the result.
    ///
    /// The second place a budget widens rather than narrows, and for the same
    /// kind of reason as [`Self::for_invention`]: the wall clock is a safety
    /// ceiling, not a grant of authority, and on this role it was failing the
    /// work rather than bounding a pathological run. See
    /// `ORCHESTRATION_RUN_MINUTES` for the 52-of-57 measurement.
    ///
    /// Only the run clock moves. The call caps are left alone so they stay the
    /// graceful trip, and the tool clock is left alone so it stays the inner
    /// bound.
    #[must_use]
    pub fn for_orchestration(self) -> Self {
        Self {
            run_timeout: self
                .run_timeout
                .max(Duration::from_secs(ORCHESTRATION_RUN_MINUTES * 60)),
            ..self
        }
    }

    /// Returns the tool timeout in milliseconds, saturating at `u64::MAX`.
    #[must_use]
    pub fn tool_timeout_ms(&self) -> u64 {
        u64::try_from(self.tool_timeout.as_millis()).unwrap_or(u64::MAX)
    }

    /// Returns the run timeout in milliseconds, saturating at `u64::MAX`.
    #[must_use]
    pub fn run_timeout_ms(&self) -> u64 {
        u64::try_from(self.run_timeout.as_millis()).unwrap_or(u64::MAX)
    }

    /// Builds the run policy that enforces this budget.
    ///
    /// The policy stops with partial results instead of erroring at a cap, so a
    /// long investigation still returns the work it completed, and it captures
    /// model and tool payloads — but only when something is going to read them;
    /// see [`payload_capture`].
    #[must_use]
    pub fn run_policy(&self) -> RunPolicy {
        let mut policy = RunPolicy::default();
        policy.limits.max_model_calls = self.max_model_calls;
        policy.limits.max_tool_calls = self.max_tool_calls;
        policy.limits.max_wall_clock_ms = Some(self.run_timeout_ms());
        policy.limits.behavior = LimitBehavior::StopWithPartial;
        policy.capture = payload_capture();

        // The loop takes the stricter of these two caps, so raising the retry
        // policy alone would change nothing: `RunLimits::max_retries_per_call`
        // defaults to 3 and would silently win.
        policy.limits.max_retries_per_call = DEFAULT_MODEL_ATTEMPTS.saturating_sub(1);
        policy.retry.max_attempts = DEFAULT_MODEL_ATTEMPTS;
        policy.retry.initial_backoff_ms = DEFAULT_BACKOFF_MS;
        policy.retry.max_backoff_ms = DEFAULT_MAX_BACKOFF_MS;
        // Jitter matters because runs are launched together and retry in
        // lockstep otherwise, so every attempt lands in the same bad instant.
        policy.retry.jitter = true;
        policy
    }
}

/// Reads a positive integer from the environment, or nothing.
///
/// Shared with the solution loop's own wall-clock ceiling rather than copied
/// there: "a missing, empty, unparsable, or zero value keeps the default" is a
/// rule about how this runtime treats overrides, and a second implementation of
/// it is a second answer to that question.
pub(crate) fn positive_env(name: &str) -> Option<u64> {
    std::env::var(name)
        .ok()?
        .trim()
        .parse::<u64>()
        .ok()
        .filter(|value| *value > 0)
}

/// Whether this run's telemetry is switched on, and therefore whether anything
/// will read a captured payload.
///
/// `MATH_AGENT_LANGFUSE=off` is the switch, on the same convention as
/// `MATH_AGENT_RESEARCH` and `MATH_AGENT_RLM`. It is *off by default* while the
/// retention below is unfixed, which is the one place in this runtime a default
/// says "less observability" — stated here rather than in a prompt, because a
/// capability that is withheld is withheld by not being wired up.
///
/// Langfuse being unconfigured counts as off too. Reading it here rather than
/// asking `LangfuseClient::from_env()` keeps the decision on one line and out
/// of an error path, and the two agree: the client is built from exactly these
/// variables.
pub(crate) fn telemetry_enabled() -> bool {
    let configured = |name: &str| std::env::var(name).is_ok_and(|value| !value.trim().is_empty());
    telemetry_from(
        std::env::var("MATH_AGENT_LANGFUSE").ok().as_deref(),
        configured("TINYHUMANS_LANGFUSE_PROXY_URL") && configured("TINYHUMANS_AUTH_TOKEN"),
        configured("LANGFUSE_BASE_URL")
            && configured("LANGFUSE_PUBLIC_KEY")
            && configured("LANGFUSE_SECRET_KEY"),
    )
}

/// The decision itself, with the environment already read.
///
/// Split out because it is the only part worth testing and the only part that
/// can be: this crate is Rust 2024, where `set_var` is `unsafe` and racy across
/// parallel tests, so a test that mutated the environment to check a switch
/// would be less trustworthy than the switch.
fn telemetry_from(switch: Option<&str>, proxy_configured: bool, direct_configured: bool) -> bool {
    let switched_on = match switch.map(str::trim) {
        // Off by default, and an empty or unparsable value is not an opt-in:
        // the cost this withholds is paid by the run rather than by whoever
        // set the variable, so only an explicit word turns it on.
        None | Some("") => false,
        Some(value) => {
            let value = value.to_ascii_lowercase();
            value == "on" || value == "1" || value == "true"
        }
    };
    switched_on && (proxy_configured || direct_configured)
}

/// What a run retains of its own model and tool traffic.
///
/// Payload capture is what makes a Langfuse trace show the prompt and the
/// completion rather than a timing, and it is not free in the way an
/// observability switch usually is. Captured payloads go into the in-memory
/// event journal, whose per-run `Vec` is read once when the run *ends*, so
/// nothing trims it while the run is going. Each `ModelCompleted` carries the
/// whole request — which is the whole conversation so far — so call *n* retains
/// a copy of everything calls 1..n-1 already retained. Retention is quadratic
/// in the number of model calls, not linear.
///
/// Measured on a live `conjectures/hilbert-16` run: 337 model calls against
/// 1.8 GiB of anonymous memory, ~5.5 MB retained per call at inputs of ~114k
/// tokens, climbing about 1.9 MiB/s and monotonic. Under a 4 GiB container cap
/// that is an OOM in twenty minutes.
///
/// So the capture follows the consumer. With telemetry off nothing will ever
/// read these bytes, and retaining them is pure cost; with it on, the run is
/// paying for its traces knowingly. The real fix is upstream — export
/// incrementally and trim the journal behind the export, so that having traces
/// does not mean keeping every one of them resident — and this is the half that
/// can be decided here.
fn payload_capture() -> PayloadCapture {
    capture_for(telemetry_enabled())
}

/// What is retained for a given telemetry posture.
///
/// Separate from [`payload_capture`] for the reason [`telemetry_from`] is
/// separate: it is the assertion worth making, and it can be made without
/// touching the environment.
fn capture_for(telemetry: bool) -> PayloadCapture {
    if telemetry {
        PayloadCapture::all()
    } else {
        PayloadCapture::default()
    }
}

#[cfg(test)]
#[path = "budget_test.rs"]
mod test;
