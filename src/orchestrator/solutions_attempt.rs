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

/// Consecutive attempts whose only gain was a larger instance, before the loop
/// treats scaling as the thing to break out of.
///
/// This exists because "did the attempt establish something new" and "is the
/// run getting anywhere" turned out to be different questions, and the loop
/// only asked the first. Pushing an exhaustive search from n=14 to n=16
/// honestly establishes something the run did not have, so reflection answers
/// PROGRESS: YES, which resets [`SolutionState::unproductive`] — and an
/// unproductive count that never reaches [`STUCK_THRESHOLD`] means the run
/// never diversifies and never reaches the inventor at all. A run can spend its
/// whole budget that way, each attempt genuinely progressing and the method
/// never changing. Two is the same evidence bar the unproductive count uses:
/// once is what an attempt looks like, twice is a pattern.
const COMPUTATIONAL_THRESHOLD: usize = 2;

/// Consecutive attempts reaching the same single-route answer before the loop
/// stops asking for a second route and reports what it has.
///
/// The loop had two words for an attempt and needed three. Project Euler 761
/// reached `V_hexagon = 5.05505046`, reduced it to the exact surd
/// `2 + 2*sqrt(21)/3`, and reproduced the formula's published anchors at n=3,
/// n=4 and n→∞ — and then could not close, correctly, because the value rests
/// on one Math.SE answer and the nearest peer-reviewed treatment (Abel et al.,
/// arXiv:2007.08965) lists regular n-gons with n>4 as an *open problem*. There
/// is no second route to build. The only verdict available for that was
/// UNSOLVED, so the run was sent back to retry, and would have spent every
/// remaining attempt re-deriving a number it already held — its own workspace
/// recording the contradiction, `GOAL.md` ticking "verified by a second
/// independent route" while `CONTEXT.md` called that an overclaim.
///
/// Two rather than one, for the reason every other threshold here is two: the
/// first UNVERIFIED is an attempt saying it could not find a second route, and
/// the run should try once more with the lesson before that becomes the
/// finding. Twice is the run having tried.
const UNVERIFIED_THRESHOLD: usize = 2;

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
    /// Consecutive attempts whose only gain was a larger instance of something
    /// an earlier attempt already computed.
    computational: usize,
    /// Consecutive attempts that reached a specific final answer supported by
    /// exactly one route, with no second route available to build.
    unverified: usize,
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
            computational: 0,
            unverified: 0,
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
        } else if self.unverified >= UNVERIFIED_THRESHOLD {
            // Distinct from both endings on purpose. "Solved" would present a
            // single-route answer as a verified one, which is the failure the
            // verification bar exists to stop; "not solved" would throw away a
            // specific final answer with an exact closed form, which is the
            // failure of reporting nothing rather than reporting honestly. The
            // provenance gap is the result here, and it is stated rather than
            // rounded to either neighbour.
            format!(
                "Answered but not independently verified, after {} attempt(s). The run reached a \
                 specific final answer and could not build a second route to it; the reflection \
                 below names the answer and the route that is missing. Treat the answer as \
                 resting on the single route stated, not as confirmed.\n\n",
                self.attempts
            )
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
    /// An answer was reached that only one route supports, and no second route
    /// is available to build. The loop stops and says so.
    Reported,
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
            Self::Reported => "reported unverified",
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
    } else if state.computational >= COMPUTATIONAL_THRESHOLD {
        // Progress that is only ever a bigger instance of the same computation
        // routes here too. This arm is the one that catches a run doing well by
        // its own report and going nowhere: every attempt establishes something
        // and none of them changes the method, so the arm above never fires.
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
    format!("Reported beside the loop since the last attempt:\n{observations}\n\n")
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
         - Before running any computation at a larger size than one this run has already run, \
           say in one line what the larger run would settle that the smaller one did not. If you \
           cannot name it, the bigger run is not the next step and doing it anyway spends the \
           attempt for nothing: the next step is a different formulation, and \
           `research/APPROACHES.md` holds the ones this run has opened and what closed each.\n\
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
