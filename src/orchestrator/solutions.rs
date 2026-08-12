//! The solution loop: a graph that attempts, reflects, and diversifies.
//!
//! A single agent asked to "solve this" retries the approach it already has.
//! When that approach is wrong, more turns of it produce more of the same
//! failure, and the run ends having learned nothing it can act on. This graph
//! makes the control flow explicit instead of leaving it to the model's
//! judgement:
//!
//! ```text
//!   attempt ──> judge ──┬─ restart ──────────────────> attempt
//!      ▲                └─ reflect ──┬─ solved ──────> done
//!      │                             ├─ retry ───────> attempt
//!      │                             └─ stuck ──> diversify ──┐
//!      └──────────────────────────────────────────────────────┘
//! ```
//!
//! The two judgements are separate on purpose. `reflect` asks whether the
//! answer is right and what the run learned, and it alone can end the loop.
//! `judge` asks the narrower question of whether the attempt was *conducted*
//! in a way the next one should inherit, scores it, and may throw the current
//! direction away — bounded by `MAX_RESTARTS`, and never on an unreadable
//! reply. It runs first so a restart costs a judge call rather than a judge
//! call plus a reflection about to be discarded.
//!
//! `reflect` runs after *every* attempt, not only after a failure, because the
//! lesson from a partial success is what stops the next attempt repeating it.
//! `diversify` is what breaks a loop the reflection alone cannot: it gathers
//! reference material, looks for structure in the results already computed, and
//! asks for a genuinely different approach, in parallel, before trying again.

use std::fmt::Write as _;
use std::path::{Path, PathBuf};
use std::sync::Arc;

use tinyagents::graph::{GraphBuilder, NodeContext, NodeResult};

use super::vector::VectorStore;
use crate::agent::Result;
use crate::agent::trace::RunTracer;

use super::async_subagents::AsyncSubagentManager;
use super::teams::TeamHandle;

/// Attempts allowed before the loop reports what it has.
///
/// Raised past the research rescue below so the rescue has attempts left to
/// pay off in. A ceiling that trips first would spend a fresh literature
/// search and then stop.
const MAX_ATTEMPTS: usize = 8;
/// Consecutive unproductive attempts before diversifying rather than retrying.
const STUCK_THRESHOLD: usize = 2;
/// Consecutive attempts lost to the provider before the loop stops trying.
///
/// Two rather than one, because a single upstream blip is exactly what the
/// retry ladder and `ReroutingModel` exist to absorb, and ending a run on one
/// would throw away work they would have recovered. Two in a row is a wall
/// rather than a blip, and no number of further attempts gets past it.
const BLOCKED_THRESHOLD: usize = 2;
/// Attempts after which each reflection also re-opens the literature.
///
/// Diversification triggers on *consecutive* unproductive attempts, so a run
/// making thin but genuine progress every time never reaches it, and can grind
/// most of its budget away on a method that was never going to arrive. Five
/// attempts is enough evidence that the approach in hand is not the intended
/// one. The search is re-run rather than recalled because the workspace has
/// changed since the first one: by now the run knows what it tried, what
/// failed, and what the numbers look like, which is a far better query than
/// anything available at the start.
const RESEARCH_RESCUE_ATTEMPTS: usize = 5;

/// Restarts the judge may force in one run.
///
/// A restart throws away the direction an attempt was taking and spends a
/// fresh one, so it has to be rare and it has to be bounded. Unbounded, a
/// judge that dislikes the run's whole approach would keep resetting it until
/// the attempt ceiling stopped the loop, and the run would end having explored
/// nothing to its conclusion. Two is enough for the fault the judge exists to
/// catch — a run building on something untrue — to be caught twice, and few
/// enough that the loop still spends most of its attempts attempting.
const MAX_RESTARTS: usize = 2;

/// State carried around the solution loop.
#[derive(Clone, Debug)]
pub(super) struct SolutionState {
    /// The problem as posed.
    problem: String,
    /// Attempts made so far.
    attempts: usize,
    /// Consecutive attempts that did not advance the work.
    unproductive: usize,
    /// The most recent attempt's report.
    last_attempt: String,
    /// Accumulated lessons, newest last.
    lessons: Vec<String>,
    /// Material gathered by the diversify step, fed into the next attempt.
    fresh_context: String,
    /// Whether reflection judged the problem solved and verified.
    solved: bool,
    /// The judge's steer for the next attempt, if it gave one.
    steer: String,
    /// Restarts the judge has already forced.
    restarts: usize,
    /// The judge's score for each attempt so far, oldest first.
    scores: Vec<u8>,
    /// What the judge made of the attempt just finished.
    judged: Verdict,
    /// Consecutive attempts that produced nothing but a provider failure.
    blocked: usize,
}

impl SolutionState {
    pub(super) fn new(problem: impl Into<String>) -> Self {
        Self {
            problem: problem.into(),
            attempts: 0,
            unproductive: 0,
            last_attempt: String::new(),
            lessons: Vec::new(),
            fresh_context: String::new(),
            solved: false,
            steer: String::new(),
            restarts: 0,
            scores: Vec::new(),
            judged: Verdict::Proceed,
            blocked: 0,
        }
    }

    /// Returns the problem as posed, for briefing work that runs beside the
    /// loop rather than inside it.
    pub(super) fn problem(&self) -> &str {
        &self.problem
    }

    /// Renders the accumulated lessons for a child prompt.
    fn lesson_briefing(&self) -> String {
        if self.lessons.is_empty() {
            return "No previous attempts.".to_string();
        }
        let mut rendered = String::from("Lessons from previous attempts, newest last:\n");
        for (index, lesson) in self.lessons.iter().enumerate() {
            let _ = writeln!(rendered, "{}. {lesson}", index + 1);
        }
        rendered
    }

    /// Returns the loop's outcome for the caller.
    pub(super) fn outcome(&self) -> String {
        let mut report = if self.solved {
            format!("Solved after {} attempt(s).\n\n", self.attempts)
        } else if self.blocked >= BLOCKED_THRESHOLD {
            // Said plainly, because the default wording reports a count of
            // attempts and reads as a mathematical failure. This run did not
            // fail at the mathematics; it never got to try.
            format!(
                "Stopped after {} attempt(s): the model provider refused every call, so no \
                 attempt reached the problem. This is an infrastructure failure, not a result \
                 about the mathematics. The workspace is unchanged and the run continues from \
                 disk once the provider accepts calls again.\n\n",
                self.attempts
            )
        } else {
            format!(
                "Not solved within {} attempt(s); reporting the furthest progress reached.\n\n",
                self.attempts
            )
        };
        report.push_str(&self.last_attempt);
        if !self.lessons.is_empty() {
            report.push_str("\n\n");
            report.push_str(&self.lesson_briefing());
        }
        report
    }
}

/// Routes taken out of the reflection node.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
enum Route {
    /// Reflection judged the work complete and verified.
    Solved,
    /// Try again with the lesson just learned.
    Retry,
    /// Repeated attempts are not advancing; gather new angles first.
    Diversify,
    /// The provider, not the mathematics, is what stopped the run.
    Blocked,
}

impl std::fmt::Display for Route {
    fn fmt(&self, formatter: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        let label = match self {
            Self::Solved => "solved",
            Self::Retry => "retry",
            Self::Diversify => "diversify",
            Self::Blocked => "blocked",
        };
        formatter.write_str(label)
    }
}

/// Decides where the loop goes after a reflection.
///
/// Kept as a free function so the policy is unit-testable without a provider:
/// the routing rule is the part of this design most likely to be wrong, and it
/// is the part a live run is least able to demonstrate cheaply.
fn route(state: &SolutionState) -> Route {
    // Checked before anything else, and before the attempt ceiling. An attempt
    // that died on the provider is not evidence about the mathematics, so
    // spending the ceiling on more of them is spending the run's one budget on
    // a condition no attempt can affect: a live pair of runs met an
    // `HTTP 403: Key limit exceeded` and burned all eight attempts in seconds,
    // each one recording the same quota error as the lesson learned, and ended
    // reporting "not solved within 8 attempts" — which reads as a mathematical
    // failure and is not one.
    if state.blocked >= BLOCKED_THRESHOLD {
        Route::Blocked
    } else if state.solved || state.attempts >= MAX_ATTEMPTS {
        Route::Solved
    } else if state.unproductive >= STUCK_THRESHOLD {
        Route::Diversify
    } else {
        Route::Retry
    }
}

/// Where the loop goes after the judge has spoken.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
enum Judged {
    /// Carry on to the reflection, which decides whether the run is done.
    Reflect,
    /// Discard this direction and attempt again.
    Restart,
}

impl std::fmt::Display for Judged {
    fn fmt(&self, formatter: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        formatter.write_str(match self {
            Self::Reflect => "reflect",
            Self::Restart => "restart",
        })
    }
}

/// Routes out of the judge node.
///
/// A plain function of the state for the same reason [`route`] is: it is a
/// policy, it is easy to get wrong, and a live run is an expensive place to
/// find that out. The attempt ceiling outranks a restart — a run at its last
/// attempt must reflect on what it has rather than throw it away and stop with
/// nothing.
fn judged_route(state: &SolutionState) -> Judged {
    if state.judged == Verdict::Restart && state.attempts < MAX_ATTEMPTS {
        Judged::Restart
    } else {
        Judged::Reflect
    }
}

/// Whether an attempt's report is nothing but the model provider refusing.
///
/// `delegate` turns a child's failure into text so the loop survives it, which
/// is right — but it makes a provider outage indistinguishable from a poor
/// attempt unless something reads the text. The markers are the ones a failed
/// delegation actually carries: the `[<agent> failed:` wrapper `delegate`
/// writes, and a model-layer error inside it.
///
/// Deliberately narrow. It must not fire on an attempt that did real work and
/// merely *mentions* a rate limit in its report, so the failure wrapper has to
/// be present and the report has to be substantially nothing else. A false
/// positive stops a run that was working, which is worse than the eight wasted
/// attempts this exists to prevent.
fn provider_blocked(report: &str) -> bool {
    let trimmed = report.trim();
    if !trimmed.starts_with('[') || !trimmed.contains("failed:") {
        return false;
    }
    let lowered = trimmed.to_ascii_lowercase();
    let refused = [
        "model error",
        "http 403",
        "http 429",
        "key limit",
        "rate limit",
    ]
    .iter()
    .any(|marker| lowered.contains(marker));
    // A report that carried a real attempt alongside the failure is not a
    // blocked attempt; the wrapper is short by construction.
    refused && trimmed.len() < 2_000
}

/// Runs one child agent and returns its text, or a description of the failure.
///
/// A child that fails must not end the loop: the failure is itself information
/// the reflection step should see and act on.
async fn delegate(subagents: &AsyncSubagentManager, agent: &str, prompt: String) -> String {
    match subagents.run_to_completion(agent, prompt).await {
        Ok(text) => text,
        Err(error) => format!("[{agent} failed: {error}]"),
    }
}

/// Carries out one attempt at the problem, briefed with every lesson so far.
async fn attempt_step(
    subagents: &AsyncSubagentManager,
    tracer: Option<&Arc<RunTracer>>,
    workspace: Option<&Path>,
    patterns: &Mailbox,
    directives: &Mailbox,
    mut state: SolutionState,
) -> SolutionState {
    state.attempts += 1;
    if let Some(tracer) = tracer {
        tracer.note(&format!("solution loop: attempt {}", state.attempts));
    }
    // The attempt drains the mailbox too, not only the reflection that follows
    // it. Reflection was the sole collector, and that made the pattern team's
    // findings reachable exactly once per completed attempt — so a run whose
    // first attempt is long never sees them at all. A live Erdős–Gyárfás run
    // spent forty minutes in attempt 1 while its pattern team computed the
    // survivor counts, identified the sequence, and pushed it past the data
    // that suggested it; none of that reached the agent directing the work,
    // which re-commissioned the same enumeration from `tool_builder`.
    //
    // Collecting here as well costs nothing when reflection has already run —
    // the mailbox is empty and the section is omitted — and it is the only
    // path that exists on the first attempt of every run.
    let observations = observations_briefing(patterns);
    // The attempt is the *only* collector of operator direction, unlike the
    // pattern mailbox above which reflection drains as well. A second collector
    // would be a second place a directive could be taken out of the mailbox and
    // then rendered under some other heading — reflection folds what it
    // collects into `fresh_context`, which reaches the next attempt as material
    // gathered rather than as an instruction. Losing the distinction is the one
    // failure that matters here: the whole point of the channel is that a human
    // asked for this, and it outranks what the run inferred.
    let direction = direction_briefing(directives);
    // Every attempt after the first continues work already on disk. Without
    // saying so, each one restarts at "read the statement and write it down",
    // and a run can spend its whole budget re-documenting the problem without
    // ever executing anything.
    // Resumption is a property of the workspace, not of the loop's counter:
    // every restart resets the counter while the files survive.
    let continuation = continuation_briefing(
        state.attempts,
        workspace.is_some_and(has_executable_artifact),
    );
    let prompt = attempt_prompt(&state, &continuation, &observations, &direction);
    if !direction.is_empty()
        && let Some(tracer) = tracer
    {
        tracer.note("solution loop: this attempt carries direction from the operator");
    }
    if state.attempts == 1 {
        open_with_execution(subagents, tracer, &state.problem);
    }
    state.last_attempt = delegate(subagents, "goals", prompt).await;
    state.fresh_context.clear();
    state.steer.clear();
    state
}

/// Renders what the pattern team has posted, or nothing when it has posted
/// nothing.
///
/// Draining here is what makes the team reach the work at all on a long first
/// attempt. Reflection stays a collector too: whichever gets there first
/// delivers, and an empty mailbox renders an empty section rather than a
/// heading announcing that no analysis arrived.
fn observations_briefing(patterns: &Mailbox) -> String {
    let observations = patterns.collect();
    if observations.is_empty() {
        return String::new();
    }
    format!("Structural observations from the pattern team:\n{observations}\n\n")
}

/// Renders what an operator has asked for, or nothing when they have asked for
/// nothing.
///
/// The text is passed through exactly as it was typed. Everything else in this
/// prompt is one model's account of another model's work, and is hedged
/// accordingly; this is the one line in it that a person wrote on purpose, and
/// summarising it would be discarding the only part nothing else can
/// reconstruct.
///
/// It is also the one input here that cannot be checked. A directive is
/// asserted, not evidenced, so it is labelled as coming from the operator
/// rather than presented as something the run established — an instruction the
/// attempt should follow, not a fact it may build on.
fn direction_briefing(directives: &Mailbox) -> String {
    let direction = directives.collect();
    if direction.is_empty() {
        return String::new();
    }
    format!(
        "Direction from the operator running this investigation, which takes precedence over the \
         judge's steer and over the plan you would otherwise continue:\n{direction}\n\n\
         Follow it in this attempt. If it asks for something you can show is wrong, say so plainly \
         in your report and say what you did instead — do not silently ignore it, and do not \
         abandon verified work to comply with it.\n\n"
    )
}

/// Builds the task one attempt is given, as a plain function of the state.
///
/// Kept separate from `attempt_step` so what an attempt is actually told is
/// testable without a provider — the same argument `route` makes.
fn attempt_prompt(
    state: &SolutionState,
    continuation: &str,
    observations: &str,
    direction: &str,
) -> String {
    let fresh = if state.fresh_context.is_empty() {
        String::new()
    } else {
        format!(
            "New material gathered since the last attempt:\n{}",
            state.fresh_context
        )
    };
    let steer = if state.steer.is_empty() {
        String::new()
    } else {
        format!(
            "The judge reviewed the last attempt and says: {}\n\n",
            state.steer
        )
    };
    format!(
        "Solve this problem and verify the result.\n\nProblem:\n{}\n\n{continuation}\n\n\
         {direction}{steer}{}\n\
         {observations}{fresh}\n\n\
         Requirements for this attempt, all of them:\n\
         - You must end this attempt with at least one program written to the workspace and \
           executed. An attempt that produces only notes, plans, or restatements has failed, \
           however well written they are.\n\
         - Reproduce every worked example in the statement with that program before running \
           anything at full size.\n\
         - Delegate the writing and running to tool_builder; it is the only role that can \
           execute.\n\
         - Then report the answer, the method, and how you verified it by a second independent \
           route; or state precisely where you are blocked, what you executed, and what its \
           output was.",
        state.problem,
        state.lesson_briefing()
    )
}

/// Starts the first execution itself, beside the attempt rather than inside it.
///
/// The method policy's first step is to write a naive oracle and run it against
/// the statement's worked examples, and the goals agent is asked to delegate
/// that immediately. Two live runs did not: their goals agents spent ten
/// minutes each on `read_document` and `list_workspace`, and both burned a
/// whole 12,000-token turn on hidden reasoning without emitting a single tool
/// call. Two prompt revisions failed to move it, so the loop stopped asking.
///
/// Fire-and-forget, and only on the first attempt. It never blocks the
/// attempt, it duplicates nothing a later attempt would do, and if the goals
/// agent does delegate promptly then the two runs simply agree — a second
/// oracle run costs one child, where no oracle at all costs the whole attempt.
fn open_with_execution(
    subagents: &AsyncSubagentManager,
    tracer: Option<&Arc<RunTracer>>,
    problem: &str,
) {
    let subagents = subagents.clone();
    let prompt = oracle_prompt(problem);
    if let Some(tracer) = tracer {
        tracer.note("solution loop: opening the attempt with an oracle run");
    }
    tokio::spawn(async move {
        let _ = subagents.run_to_completion("tool_builder", prompt).await;
    });
}

/// The task the loop hands its opening oracle run.
fn oracle_prompt(problem: &str) -> String {
    format!(
        "Write the naive oracle for this problem and run it now.\n\nProblem:\n{problem}\n\n\
         Write it to code/brute.py — obviously correct rather than fast, exact integer or \
         rational arithmetic — and execute it against every worked example the statement \
         gives. Do not optimise, do not derive the efficient method, and do not write a plan: \
         another agent is doing that in parallel. If the workspace already holds such a \
         program, run that instead of writing a second one.\n\n\
         Run it only at the sizes the worked examples use. The oracle exists to pin down \
         what the statement means, and it earns that in seconds; the bound in the statement \
         is chosen to defeat exactly this method, so pointing it at full size buys nothing \
         and costs the attempt. If a run has not finished in about a minute, it is at the \
         wrong size — stop it, drop to a smaller case, and report that instead. Cap it \
         yourself so a slow case cannot run away.\n\n\
         Report the command you ran and its exact output, and say for each worked example \
         whether it matched."
    )
}

/// What the judge decided about how an attempt was conducted.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub(super) enum Verdict {
    /// Conducted acceptably, whatever it found.
    Proceed,
    /// Worth continuing, pointed slightly wrong.
    Steer,
    /// Wrong in a way continuing will not repair.
    Restart,
}

/// Reads the judge's reply.
///
/// Unparsable is [`Verdict::Proceed`], deliberately and in the same spirit as
/// an unparsable reflection not counting as solved: the expensive outcome
/// needs the explicit word. A judge whose reply the loop cannot read must not
/// be able to throw an attempt away by accident.
pub(super) fn judge_verdict(reply: &str) -> Verdict {
    let upper = reply.to_uppercase();
    if upper.contains("VERDICT: RESTART") || upper.contains("VERDICT:RESTART") {
        Verdict::Restart
    } else if upper.contains("VERDICT: STEER") || upper.contains("VERDICT:STEER") {
        Verdict::Steer
    } else {
        Verdict::Proceed
    }
}

/// Reads the judge's score, if it gave a readable one.
pub(super) fn judge_score(reply: &str) -> Option<u8> {
    let upper = reply.to_uppercase();
    let rest = upper.split("SCORE:").nth(1)?;
    let digits: String = rest
        .trim_start()
        .chars()
        .take_while(char::is_ascii_digit)
        .collect();
    digits.parse().ok().filter(|score| (1..=5).contains(score))
}

/// Pulls the judge's one-sentence guidance out of its reply.
pub(super) fn judge_guidance(reply: &str) -> String {
    for line in reply.lines() {
        let trimmed = line.trim();
        if let Some(rest) = trimmed
            .strip_prefix("NEXT:")
            .or_else(|| trimmed.strip_prefix("next:"))
            && !rest.trim().is_empty()
        {
            return rest.trim().to_string();
        }
    }
    String::new()
}

/// Scores how the attempt was conducted and decides whether to start over.
///
/// This is not the reflection: reflection asks whether the answer is right and
/// what the run learned, and it is the only thing that can end the loop. The
/// judge asks a narrower question — was this attempt *conducted* in a way the
/// next one should inherit — and its expensive answer is bounded by
/// [`MAX_RESTARTS`], because a judge that dislikes the run's whole direction
/// could otherwise reset it until the attempt ceiling stopped the loop.
///
/// It runs before the reflection rather than after, so a restart costs the run
/// a judge call rather than a judge call plus a reflection it is about to
/// discard.
async fn judge_step(
    subagents: &AsyncSubagentManager,
    tracer: Option<&Arc<RunTracer>>,
    mut state: SolutionState,
) -> SolutionState {
    let prompt = format!(
        "Judge how this attempt was conducted.\n\nProblem:\n{}\n\n\
         This is attempt {} of at most {MAX_ATTEMPTS}. {}\n\n\
         The attempt reported:\n{}",
        state.problem,
        state.attempts,
        if state.restarts >= MAX_RESTARTS {
            "The run has already been restarted as often as it may be, so RESTART is no \
             longer available to you: score, and PROCEED or STEER."
        } else {
            "RESTART is available but expensive; it discards this direction and spends a \
             fresh attempt."
        },
        state.last_attempt
    );
    let reply = delegate(subagents, "judge", prompt).await;
    let score = judge_score(&reply);
    if let Some(score) = score {
        state.scores.push(score);
    }
    let mut verdict = judge_verdict(&reply);
    if verdict == Verdict::Restart && state.restarts >= MAX_RESTARTS {
        // The ceiling outranks the verdict, exactly as the attempt ceiling
        // outranks the stuck rule: a bound that a model can talk its way past
        // is not a bound.
        verdict = Verdict::Steer;
    }
    state.steer = match verdict {
        Verdict::Proceed => String::new(),
        Verdict::Steer | Verdict::Restart => judge_guidance(&reply),
    };
    if verdict == Verdict::Restart {
        state.restarts += 1;
        // A restart is not progress, and saying so is what keeps the loop from
        // treating a discarded direction as an advance.
        state.unproductive += 1;
    }
    if let Some(tracer) = tracer {
        tracer.note(&format!(
            "solution loop: judge scored {} and returned {}",
            score.map_or_else(|| "unreadably".to_string(), |score| format!("{score}/5")),
            match verdict {
                Verdict::Proceed => "proceed",
                Verdict::Steer => "steer",
                Verdict::Restart => "restart",
            }
        ));
    }
    state.judged = verdict;
    state
}

/// Tells an attempt whether it is starting fresh or continuing existing work.
///
/// Without this every attempt restarts at "read the statement and write it
/// down": the workspace files it would continue from are exactly the ones it
/// re-creates. A run can then spend its whole budget re-documenting the problem
/// and never execute anything, which is precisely what two live runs did.
fn continuation_briefing(attempt: usize, resumed: bool) -> String {
    if attempt <= 1 && resumed {
        // A restarted run begins at attempt 1 with a workspace full of earlier
        // work, and telling it to start fresh is how that work gets re-read
        // instead of used. A live solver spent fourteen minutes and fifty-nine
        // model calls on seventeen `read_document` calls and nothing else,
        // reconciling a statement it had been told to extract afresh against
        // thirty-one programs already on disk.
        //
        // The attempt counter is in memory and the workspace is on disk, so
        // only the workspace can say whether this run is continuing something.
        return "This run continues earlier work. Read GOAL.md, inspect existing artifacts, and \
                call recall_memory for prior results, lessons, and failed approaches, then CONTINUE. \
                Do not re-extract the statement or re-derive what Cognee already recalls — \
                establish the next unresolved thing and run a program that settles it. \
                Your very next action is a spawn: name the next unresolved thing and hand it to \
                tool_builder. Two live runs spent ten minutes and two whole 12,000-token turns \
                deciding what to spawn and never spawned anything."
            .to_string();
    }
    if attempt <= 1 {
        "This is the first attempt. Start by reading the statement, then immediately write and \
         run a program that reproduces the worked examples it gives."
            .to_string()
    } else {
        format!(
            "This is attempt {attempt}. Earlier attempts already produced artifacts and stored lessons; \
             read GOAL.md, call recall_memory, and CONTINUE from there. Do not re-extract or re-document the \
             statement — that work is done, and repeating it is how this run fails."
        )
    }
}

/// Returns whether the workspace holds a program the run could have executed.
///
/// A deliberately shallow check: it asks whether any `.py` or `.sh` file
/// exists, not whether it is correct. That is enough to catch the failure it
/// exists for — a confident answer with nothing behind it — without pretending
/// to judge mathematics from the filesystem.
fn has_executable_artifact(workspace: &Path) -> bool {
    // `code/` first, then the root. Programs are filed under `code/` now, and
    // a check that looked only at the root started answering "no programs" for
    // every workspace the moment they moved — which told each restarted run it
    // was starting fresh, so it re-read a workspace it should have continued
    // from. The root is still searched because a shell redirect can put a
    // program there and because older workspaces predate the move.
    [
        workspace.join(super::layout::CODE_DIR),
        workspace.to_path_buf(),
    ]
    .iter()
    .filter_map(|folder| std::fs::read_dir(folder).ok())
    .flatten()
    .filter_map(std::result::Result::ok)
    .any(|entry| {
        let name = entry.file_name();
        let name = name.to_string_lossy();
        (name.ends_with(".py") || name.ends_with(".sh"))
            && entry.metadata().is_ok_and(|meta| meta.len() > 0)
    })
}

/// Persists the reflection in Cognee without making memory availability a
/// precondition for continuing the solution loop.
async fn log_reflection(
    memory: &VectorStore,
    attempt: usize,
    reflection: &str,
    tracer: Option<&Arc<RunTracer>>,
) {
    let source = format!("reflection agent, attempt {attempt}");
    match memory.remember(reflection.trim(), &source).await {
        Ok(id) => {
            if let Some(tracer) = tracer {
                tracer.note(&format!("stored reflection memory {id}"));
            }
        }
        Err(error) => {
            if let Some(tracer) = tracer {
                tracer.note(&format!("reflection memory failed: {error}"));
            }
        }
    }
}

/// Judges the last attempt and records the lesson it yields.
async fn reflect_step(
    subagents: &AsyncSubagentManager,
    tracer: Option<&Arc<RunTracer>>,
    workspace: Option<&Path>,
    memory: &VectorStore,
    patterns: &Mailbox,
    teams: &[TeamHandle],
    mut state: SolutionState,
) -> SolutionState {
    let prompt = format!(
        "Judge one attempt at a problem and extract the lesson.\n\nProblem:\n{}\n\n\
         Attempt report:\n{}\n\n{}\n\n\
         Answer exactly these three things:\n\
         VERDICT: SOLVED if the attempt reached a specific final answer AND verified it by a \
         second independent route; otherwise UNSOLVED. An unverified answer is UNSOLVED.\n\
         PROGRESS: YES if this attempt established something the previous ones had not; \
         otherwise NO.\n\
         LESSON: one or two sentences naming the specific thing to do differently next time. \
         Name the misstep and the concrete alternative. Do not restate the problem or give \
         generic advice.",
        state.problem,
        state.last_attempt,
        state.lesson_briefing()
    );
    let reflection = delegate(subagents, "reflection", prompt);
    // Reflection judges; the pattern agent looks at the same attempt for
    // structure the judgement cannot see. They run concurrently because
    // neither reads the other's output, and because reflection is on the
    // critical path of every single attempt — making it wait for a sequence
    // analysis would tax the common case to serve the occasional one.
    //
    // The pattern agent runs after *every* attempt rather than only when the
    // loop is stuck, because the exploitable regularity in a sequence is
    // usually visible in the first few terms a run computes. Waiting for two
    // consecutive unproductive attempts means the run has already spent the
    // budget the pattern would have saved.
    //
    // Whatever earlier pattern runs have finished by now joins this attempt's
    // context. The report is no less true for arriving an attempt late.
    let patterns = patterns.collect();
    // Past the rescue threshold the literature is re-opened on every
    // reflection, with what the run now knows rather than what it knew at the
    // start.
    let rescue = async {
        if state.solved || state.attempts < RESEARCH_RESCUE_ATTEMPTS {
            return String::new();
        }
        if let Some(tracer) = tracer {
            tracer.note(&format!(
                "solution loop: {} attempts without a verified answer, re-opening the literature",
                state.attempts
            ));
        }
        delegate(
            subagents,
            "research",
            format!(
                "This investigation has made {} attempts without reaching a verified answer. \
                 Search for how this problem, or the structure it reduces to, has actually been \
                 solved. Read the workspace first so your queries use what the run now knows — \
                 the methods it tried, why they failed, and the numbers it computed — rather than \
                 the statement alone. Search several distinct phrasings, including the named \
                 theory, the sequence values themselves, and any classification the objects \
                 belong to. Return concrete methods with source URLs, and say which of the \
                 approaches already tried each one supersedes.\n\nProblem:\n{}\n\n{}",
                state.attempts,
                state.problem,
                state.lesson_briefing()
            ),
        )
        .await
    };
    let (reflection, rescue) = tokio::join!(reflection, rescue);
    log_reflection(memory, state.attempts, &reflection, tracer).await;
    state.fresh_context = merge_context(&[("Pattern analysis", &patterns), ("Research", &rescue)]);

    let upper = reflection.to_uppercase();
    // Require the explicit positive verdict: anything unparsable or hedged
    // leaves the loop running rather than declaring success.
    let claimed = upper.contains("VERDICT: SOLVED") || upper.contains("VERDICT:SOLVED");
    // ...and require evidence on disk that a program was actually written.
    //
    // The verdict comes from a model, and this runtime deliberately uses a
    // small fast one that confabulates. A claimed answer with no program in
    // the workspace is the signature failure: a confident final report,
    // plausible numbers, and nothing that ever ran. Ending the loop on that
    // is worse than not finishing, because it presents a guess as a result.
    let evidenced = workspace.is_none_or(has_executable_artifact);
    state.solved = claimed && evidenced;
    if claimed && !evidenced {
        state.lessons.push(
            "Reported SOLVED but the workspace contains no program. An answer that was never \
             computed is not an answer: write the program, run it, and show its output."
                .to_string(),
        );
        if let Some(tracer) = tracer {
            tracer.note("solution loop: SOLVED rejected, no program in the workspace");
        }
    }
    // A blocked attempt is counted before progress is judged, because
    // reflection on a provider error cannot report progress and would
    // otherwise register as an unproductive attempt — driving the run into
    // diversification, which is three more child runs into the same wall.
    if provider_blocked(&state.last_attempt) {
        state.blocked += 1;
    } else {
        state.blocked = 0;
    }
    let progressed = upper.contains("PROGRESS: YES") || upper.contains("PROGRESS:YES");
    if progressed {
        state.unproductive = 0;
    } else {
        state.unproductive += 1;
    }
    if let Some(tracer) = tracer {
        tracer.note(&format!(
            "solution loop: verdict {}, progress {}, next {}",
            if state.solved { "solved" } else { "unsolved" },
            if progressed { "yes" } else { "no" },
            route(&state)
        ));
    }
    let lesson = extract_lesson(&reflection);
    tell_teams(teams, &state, progressed, &lesson);
    state.lessons.push(lesson);
    state
}

/// Tells the support teams how the attempt went.
///
/// They run beside the loop and would otherwise keep enriching the workspace
/// against the run's opening understanding of the problem — the understanding
/// the attempts have been busy correcting. Posting never waits: a full inbox
/// drops the note rather than stalling the solve to deliver it.
///
/// The verdict travels with the lesson in a form a team can act on without
/// interpreting prose. The research team gathers only when the run is actually
/// short of something, and "did this attempt get anywhere" is the signal that
/// says so: a run making progress every time needs no rescue, and a team that
/// fetches regardless fills the workspace with sources nobody asked for.
fn tell_teams(teams: &[TeamHandle], state: &SolutionState, progressed: bool, lesson: &str) {
    let verdict = if progressed { "PROGRESSING" } else { "STUCK" };
    for team in teams {
        team.post(
            "solver",
            format!(
                "Attempt {} — {verdict} ({} consecutive without progress): {lesson}",
                state.attempts, state.unproductive
            ),
        );
    }
}

/// Gathers three independent angles concurrently to break a stalled loop.
async fn diversify_step(
    subagents: &AsyncSubagentManager,
    tracer: Option<&Arc<RunTracer>>,
    mut state: SolutionState,
) -> SolutionState {
    if let Some(tracer) = tracer {
        tracer.note("solution loop: stuck, gathering new angles");
    }
    let library = delegate(
        subagents,
        "librarian",
        format!(
            "Build a local reference set for this problem. Find primary treatments of the \
             mathematics involved, download them into the workspace reference library, index \
             them, and report what is now available locally with its source URLs.\n\n\
             Problem:\n{}\n\n{}",
            state.problem,
            state.lesson_briefing()
        ),
    );
    let patterns = delegate(
        subagents,
        "pattern_finder",
        format!(
            "Look for exploitable structure in the data this investigation has already produced. \
             Read the workspace results, extract the relevant integer sequences, and run the \
             sequence tools on them. Report only regularities that hold exactly over every term, \
             and say plainly that they are conjectures.\n\nProblem:\n{}",
            state.problem
        ),
    );
    let invention = delegate(
        subagents,
        "inventor",
        format!(
            "Propose a genuinely different line of attack. The approaches tried so far have not \
             worked; do not restate them. Name a specific alternative formulation, transform, or \
             theory, say why it suits this problem, and give the first concrete \
             step.\n\nProblem:\n{}\n\n{}",
            state.problem,
            state.lesson_briefing()
        ),
    );
    // Gathering and digesting are one sequential arm, run concurrently with
    // the other two. The scholar has to follow the librarian rather than join
    // it: it reads what was just downloaded, and a digest written before the
    // documents land describes nothing. Acquiring without reading is the gap
    // this closes — a downloaded paper nobody has read has cost the run
    // context and taught it nothing.
    let reading = async {
        let library = library.await;
        let digest = delegate(
            subagents,
            "scholar",
            format!(
                "Read the reference library against this investigation and turn it into usable \
                 knowledge. For each source that bears on the problem, record what it actually \
                 establishes and what it implies here. Store source-backed durable findings with \
                 remember_memory. Say which sources do not help and why. Flag anything that \
                 contradicts recalled memory.\n\n\
                 Problem:\n{}\n\nJust gathered:\n{library}\n\n{}",
                state.problem,
                state.lesson_briefing()
            ),
        )
        .await;
        (library, digest)
    };
    let ((library, digest), patterns, invention) = tokio::join!(reading, patterns, invention);

    // Merged rather than assigned: the reflection that routed here has already
    // put this attempt's pattern analysis, and possibly a literature rescue,
    // into the same field. Overwriting would throw away the findings that
    // motivated diversifying in the first place.
    state.fresh_context = merge_context(&[
        ("Carried forward", &state.fresh_context.clone()),
        ("Reference material", &library),
        ("What the sources establish", &digest),
        ("Structural observations", &patterns),
        ("Proposed alternative approach", &invention),
    ]);
    state.unproductive = 0;
    state
}

/// Joins the labelled sections that have content into one briefing.
///
/// Empty sections are dropped rather than rendered as a heading with nothing
/// under it: a child asked to act on "Research:\n\n" reasonably concludes the
/// research found nothing, which is a different claim from its not having run.
fn merge_context(sections: &[(&str, &str)]) -> String {
    let mut merged = String::new();
    for (label, body) in sections {
        if body.trim().is_empty() {
            continue;
        }
        if !merged.is_empty() {
            merged.push_str("\n\n");
        }
        let _ = write!(merged, "{label}:\n{}", body.trim());
    }
    merged
}

/// Where something working outside the loop leaves text for a later attempt.
///
/// The pattern agent used to be awaited beside the reflection, and that made
/// it a gate on the whole loop: a live run sat 33 minutes unable to start its
/// next attempt because the pattern agent it had already collected a verdict
/// beside was still working. Nothing bounds a pattern run against the loop —
/// it has its own budget of hundreds of model calls — so the gate had no
/// ceiling.
///
/// Detaching it is safe precisely because nothing in the routing decision
/// reads it: `route` turns on the reflection's verdict alone. So the run is
/// spawned, the loop proceeds on the reflection, and whatever the pattern
/// agent finds is posted here and picked up by the next attempt that asks. A
/// structural observation is worth as much one attempt later; a stalled loop
/// is not.
///
/// Human direction arrives the same way and for a stronger version of the same
/// reason. A person is slower than any support agent, so a loop that waited on
/// one would be that 33-minute gate with no bound at all. Two mailboxes are
/// therefore built from this one type — one carrying what the pattern team
/// found, one carrying what an operator asked for — and they differ only in
/// the heading their contents are rendered under.
#[derive(Clone, Default)]
pub(super) struct Mailbox(Arc<std::sync::Mutex<Vec<String>>>);

impl Mailbox {
    /// Leaves a finished report for the next attempt.
    pub(super) fn post(&self, report: String) {
        if report.trim().is_empty() {
            return;
        }
        if let Ok(mut slot) = self.0.lock() {
            slot.push(report);
        }
    }

    /// Takes every report that has arrived since the last collection.
    ///
    /// More than one can be waiting when a pattern run outlives the attempt
    /// that started it, which is the normal case now that they are detached.
    pub(super) fn collect(&self) -> String {
        let Ok(mut slot) = self.0.lock() else {
            return String::new();
        };
        let reports = std::mem::take(&mut *slot);
        reports.join("\n\n")
    }
}

/// Builds and runs the solution loop over the registered specialists.
///
/// # Errors
///
/// Returns an error only when the graph itself cannot be compiled or executed;
/// a failing child agent is folded into the state as a lesson instead.
pub(super) async fn run(
    subagents: AsyncSubagentManager,
    tracer: Option<Arc<RunTracer>>,
    workspace: Option<PathBuf>,
    memory: VectorStore,
    teams: Vec<TeamHandle>,
    patterns: Mailbox,
    directives: Mailbox,
    state: SolutionState,
) -> Result<SolutionState> {
    let attempt_agents = subagents.clone();
    let attempt_tracer = tracer.clone();
    let judge_agents = subagents.clone();
    let judge_tracer = tracer.clone();
    let reflect_agents = subagents.clone();
    let reflect_tracer = tracer.clone();
    let attempt_workspace = workspace.clone();
    let reflect_workspace = workspace;
    let reflect_memory = memory;
    let diversify_agents = subagents.clone();
    let diversify_tracer = tracer;
    let attempt_mailbox = patterns.clone();
    let pattern_mailbox = patterns;
    let attempt_directives = directives;
    let reflect_teams = teams;

    let graph = GraphBuilder::<SolutionState, SolutionState>::overwrite()
        .add_node("attempt", move |state: SolutionState, _ctx: NodeContext| {
            let subagents = attempt_agents.clone();
            let tracer = attempt_tracer.clone();
            let workspace = attempt_workspace.clone();
            let mailbox = attempt_mailbox.clone();
            let directives = attempt_directives.clone();
            async move {
                Ok(NodeResult::Update(
                    attempt_step(
                        &subagents,
                        tracer.as_ref(),
                        workspace.as_deref(),
                        &mailbox,
                        &directives,
                        state,
                    )
                    .await,
                ))
            }
        })
        .add_node("judge", move |state: SolutionState, _ctx: NodeContext| {
            let subagents = judge_agents.clone();
            let tracer = judge_tracer.clone();
            async move {
                Ok(NodeResult::Update(
                    judge_step(&subagents, tracer.as_ref(), state).await,
                ))
            }
        })
        .add_node("reflect", move |state: SolutionState, _ctx: NodeContext| {
            let subagents = reflect_agents.clone();
            let mailbox = pattern_mailbox.clone();
            let teams = reflect_teams.clone();
            let tracer = reflect_tracer.clone();
            let workspace = reflect_workspace.clone();
            let memory = reflect_memory.clone();
            async move {
                Ok(NodeResult::Update(
                    reflect_step(
                        &subagents,
                        tracer.as_ref(),
                        workspace.as_deref(),
                        &memory,
                        &mailbox,
                        &teams,
                        state,
                    )
                    .await,
                ))
            }
        })
        .add_node(
            "diversify",
            move |state: SolutionState, _ctx: NodeContext| {
                let subagents = diversify_agents.clone();
                let tracer = diversify_tracer.clone();
                async move {
                    Ok(NodeResult::Update(
                        diversify_step(&subagents, tracer.as_ref(), state).await,
                    ))
                }
            },
        )
        .add_node(
            "done",
            |state: SolutionState, _ctx: NodeContext| async move { Ok(NodeResult::Update(state)) },
        );
    let graph = wire_routes(graph).compile()?;

    Ok(graph.run(state).await?.state)
}

/// Connects the loop's nodes, separately from building them.
///
/// The routing is the part of this design most likely to be wrong, so it is
/// worth reading in one piece rather than at the tail of the wiring.
fn wire_routes(
    builder: GraphBuilder<SolutionState, SolutionState>,
) -> GraphBuilder<SolutionState, SolutionState> {
    builder
        .set_entry("attempt")
        .add_edge("attempt", "judge")
        .add_conditional_edges(
            "judge",
            judged_route,
            [(Judged::Reflect, "reflect"), (Judged::Restart, "attempt")],
        )
        .add_conditional_edges(
            "reflect",
            route,
            [
                (Route::Solved, "done"),
                (Route::Retry, "attempt"),
                (Route::Diversify, "diversify"),
                // Same terminal node as a finished run. The loop stops rather
                // than diversifying, because diversification is three more
                // child runs into the same refusal.
                (Route::Blocked, "done"),
            ],
        )
        .add_edge("diversify", "attempt")
        .set_finish("done")
}

/// Pulls the `LESSON:` line out of a reflection, falling back to the whole text.
fn extract_lesson(reflection: &str) -> String {
    for line in reflection.lines() {
        let trimmed = line.trim();
        if let Some(rest) = trimmed
            .strip_prefix("LESSON:")
            .or_else(|| trimmed.strip_prefix("lesson:"))
        {
            let lesson = rest.trim();
            if !lesson.is_empty() {
                return lesson.to_string();
            }
        }
    }
    let condensed = reflection.trim();
    if condensed.is_empty() {
        "The reflection step returned nothing usable.".to_string()
    } else {
        condensed.chars().take(400).collect()
    }
}

#[cfg(test)]
mod test;
