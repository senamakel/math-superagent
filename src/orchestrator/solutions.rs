//! The solution loop: a graph that attempts, reflects, and diversifies.
//!
//! A single agent asked to "solve this" retries the approach it already has.
//! When that approach is wrong, more turns of it produce more of the same
//! failure, and the run ends having learned nothing it can act on. This graph
//! makes the control flow explicit instead of leaving it to the model's
//! judgement:
//!
//! ```text
//!   attempt ──> reflect ──┬─ solved ────────────────> done
//!      ▲                  ├─ retry ─────────────────> attempt
//!      │                  └─ stuck ──> diversify ────┘
//!      └────────────────────────────────────────────┘
//! ```
//!
//! `reflect` runs after *every* attempt, not only after a failure, because the
//! lesson from a partial success is what stops the next attempt repeating it.
//! `diversify` is what breaks a loop the reflection alone cannot: it gathers
//! reference material, looks for structure in the results already computed, and
//! asks for a genuinely different approach, in parallel, before trying again.

use std::fmt::Write as _;
use std::path::{Path, PathBuf};
use std::sync::Arc;
use std::time::{SystemTime, UNIX_EPOCH};

use tinyagents::graph::{GraphBuilder, NodeContext, NodeResult};

use crate::agent::Result;
use crate::agent::trace::RunTracer;

use super::async_subagents::AsyncSubagentManager;

/// Attempts allowed before the loop reports what it has.
///
/// Raised past the research rescue below so the rescue has attempts left to
/// pay off in. A ceiling that trips first would spend a fresh literature
/// search and then stop.
const MAX_ATTEMPTS: usize = 8;
/// Consecutive unproductive attempts before diversifying rather than retrying.
const STUCK_THRESHOLD: usize = 2;
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
        }
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
}

impl std::fmt::Display for Route {
    fn fmt(&self, formatter: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        let label = match self {
            Self::Solved => "solved",
            Self::Retry => "retry",
            Self::Diversify => "diversify",
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
    if state.solved || state.attempts >= MAX_ATTEMPTS {
        Route::Solved
    } else if state.unproductive >= STUCK_THRESHOLD {
        Route::Diversify
    } else {
        Route::Retry
    }
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
    mut state: SolutionState,
) -> SolutionState {
    state.attempts += 1;
    if let Some(tracer) = tracer {
        tracer.note(&format!("solution loop: attempt {}", state.attempts));
    }
    let fresh = if state.fresh_context.is_empty() {
        String::new()
    } else {
        format!(
            "New material gathered since the last attempt:\n{}",
            state.fresh_context
        )
    };
    // Every attempt after the first continues work already on disk. Without
    // saying so, each one restarts at "read the statement and write it down",
    // and a run can spend its whole budget re-documenting the problem without
    // ever executing anything.
    let continuation = continuation_briefing(state.attempts);
    let prompt = format!(
        "Solve this problem and verify the result.\n\nProblem:\n{}\n\n{continuation}\n\n{}\n\
         {fresh}\n\n\
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
    );
    state.last_attempt = delegate(subagents, "goals", prompt).await;
    state.fresh_context.clear();
    state
}

/// Tells an attempt whether it is starting fresh or continuing existing work.
///
/// Without this every attempt restarts at "read the statement and write it
/// down": the workspace files it would continue from are exactly the ones it
/// re-creates. A run can then spend its whole budget re-documenting the problem
/// and never execute anything, which is precisely what two live runs did.
fn continuation_briefing(attempt: usize) -> String {
    if attempt <= 1 {
        "This is the first attempt. Start by reading the statement, then immediately write and \
         run a program that reproduces the worked examples it gives."
            .to_string()
    } else {
        format!(
            "This is attempt {attempt}. Earlier attempts already wrote the workspace files; read \
             goal.md and memory.md and CONTINUE from there. Do not re-extract or re-document the \
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
    let Ok(entries) = std::fs::read_dir(workspace) else {
        return false;
    };
    entries.filter_map(std::result::Result::ok).any(|entry| {
        let name = entry.file_name();
        let name = name.to_string_lossy();
        (name.ends_with(".py") || name.ends_with(".sh"))
            && entry.metadata().is_ok_and(|meta| meta.len() > 0)
    })
}

/// Counts the distinct lessons a reflection produced.
///
/// A `LESSON:` line may carry several points as bullets; each is a separate
/// thing the next attempt could act on, so they are counted individually.
fn count_learnings(reflection: &str) -> usize {
    let mut inside = false;
    let mut count = 0;
    for line in reflection.lines() {
        let trimmed = line.trim();
        if trimmed.to_uppercase().starts_with("LESSON:") {
            inside = true;
            if !trimmed[7..].trim().is_empty() {
                count += 1;
            }
            continue;
        }
        if inside {
            if trimmed.is_empty() {
                continue;
            }
            if trimmed.starts_with('-') || trimmed.starts_with('*') {
                count += 1;
            } else if trimmed
                .chars()
                .next()
                .is_some_and(|c| c.is_ascii_uppercase())
                && trimmed.contains(':')
            {
                // A new labelled section ends the lesson block.
                break;
            }
        }
    }
    count
}

/// Builds the file name a reflection is logged under.
///
/// The name carries the outcome so a directory listing alone shows which
/// attempts taught the run something: `<ms>_nothing.md` when a reflection
/// yielded no actionable lesson, `<ms>_<n>_learnings.md` otherwise.
fn reflection_filename(millis: u128, learnings: usize) -> String {
    if learnings == 0 {
        format!("reflections/{millis}_nothing.md")
    } else {
        format!("reflections/{millis}_{learnings:02}_learnings.md")
    }
}

/// Writes a reflection to the workspace log.
///
/// Failure is deliberately silent to the caller: the reflection has already
/// been folded into the loop state, and losing its archive copy must not cost
/// the run the lesson itself.
async fn log_reflection(
    workspace: Option<&Path>,
    attempt: usize,
    reflection: &str,
    tracer: Option<&Arc<RunTracer>>,
) {
    let Some(workspace) = workspace else {
        return;
    };
    let millis = SystemTime::now()
        .duration_since(UNIX_EPOCH)
        .map(|elapsed| elapsed.as_millis())
        .unwrap_or_default();
    let learnings = count_learnings(reflection);
    let relative = reflection_filename(millis, learnings);
    let path = workspace.join(&relative);
    if let Some(parent) = path.parent() {
        let _ = tokio::fs::create_dir_all(parent).await;
    }
    let body = format!(
        "# Reflection after attempt {attempt}\n\n{}\n",
        reflection.trim()
    );
    if tokio::fs::write(&path, body).await.is_ok()
        && let Some(tracer) = tracer
    {
        tracer.note(&format!("logged {relative}"));
    }
}

/// Judges the last attempt and records the lesson it yields.
async fn reflect_step(
    subagents: &AsyncSubagentManager,
    tracer: Option<&Arc<RunTracer>>,
    workspace: Option<&Path>,
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
    let patterns = delegate(
        subagents,
        "pattern_finder",
        format!(
            "Look for exploitable structure in the data this attempt just produced. Read the \
             workspace results, extract the integer sequences in them, and run the sequence tools \
             on them. Where a check needs a computation the tools do not do, write and run the \
             program yourself, or delegate it. Report only regularities that hold exactly over \
             every term supplied, say plainly that they are conjectures, and give the first term \
             that would falsify each one.\n\nProblem:\n{}",
            state.problem
        ),
    );
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
    let (reflection, patterns, rescue) = tokio::join!(reflection, patterns, rescue);
    log_reflection(workspace, state.attempts, &reflection, tracer).await;
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
    state.lessons.push(extract_lesson(&reflection));
    state
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
                 establishes and what it implies here, and keep research/INDEX.md current as \
                 the way in. Say which sources do not help and why. Flag anything that \
                 contradicts what memory.md currently asserts.\n\n\
                 Problem:\n{}\n\nJust gathered:\n{library}\n\n{}",
                state.problem,
                state.lesson_briefing()
            ),
        )
        .await;
        (library, digest)
    };
    let ((library, digest), patterns, invention) = tokio::join!(reading, patterns, invention);

    state.fresh_context = format!(
        "Reference material:\n{library}\n\nWhat the sources establish:\n{digest}\n\n\
         Structural observations:\n{patterns}\n\n\
         Proposed alternative approach:\n{invention}"
    );
    state.unproductive = 0;
    state
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
    state: SolutionState,
) -> Result<SolutionState> {
    let attempt_agents = subagents.clone();
    let attempt_tracer = tracer.clone();
    let reflect_agents = subagents.clone();
    let reflect_tracer = tracer.clone();
    let reflect_workspace = workspace;
    let diversify_agents = subagents.clone();
    let diversify_tracer = tracer;

    let graph = GraphBuilder::<SolutionState, SolutionState>::overwrite()
        .add_node("attempt", move |state: SolutionState, _ctx: NodeContext| {
            let subagents = attempt_agents.clone();
            let tracer = attempt_tracer.clone();
            async move {
                Ok(NodeResult::Update(
                    attempt_step(&subagents, tracer.as_ref(), state).await,
                ))
            }
        })
        .add_node("reflect", move |state: SolutionState, _ctx: NodeContext| {
            let subagents = reflect_agents.clone();
            let tracer = reflect_tracer.clone();
            let workspace = reflect_workspace.clone();
            async move {
                Ok(NodeResult::Update(
                    reflect_step(&subagents, tracer.as_ref(), workspace.as_deref(), state).await,
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
        )
        .set_entry("attempt")
        .add_edge("attempt", "reflect")
        .add_conditional_edges(
            "reflect",
            route,
            [
                (Route::Solved, "done"),
                (Route::Retry, "attempt"),
                (Route::Diversify, "diversify"),
            ],
        )
        .add_edge("diversify", "attempt")
        .set_finish("done")
        .compile()?;

    Ok(graph.run(state).await?.state)
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
