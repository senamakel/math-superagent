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

use std::sync::Arc;

use tinyagents::graph::{GraphBuilder, NodeContext, NodeResult};

use crate::agent::Result;
use crate::agent::trace::RunTracer;

use super::async_subagents::AsyncSubagentManager;

/// Attempts allowed before the loop reports what it has.
const MAX_ATTEMPTS: usize = 6;
/// Consecutive unproductive attempts before diversifying rather than retrying.
const STUCK_THRESHOLD: usize = 2;

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
            rendered.push_str(&format!("{}. {lesson}\n", index + 1));
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
async fn delegate(
    subagents: &AsyncSubagentManager,
    agent: &str,
    prompt: String,
) -> String {
    match subagents.run_to_completion(agent, prompt).await {
        Ok(text) => text,
        Err(error) => format!("[{agent} failed: {error}]"),
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
    state: SolutionState,
) -> Result<SolutionState> {
    let attempt_agents = subagents.clone();
    let attempt_tracer = tracer.clone();
    let reflect_agents = subagents.clone();
    let reflect_tracer = tracer.clone();
    let diversify_agents = subagents.clone();
    let diversify_tracer = tracer;

    let graph = GraphBuilder::<SolutionState, SolutionState>::overwrite()
        .add_node("attempt", move |mut state: SolutionState, _ctx: NodeContext| {
            let subagents = attempt_agents.clone();
            let tracer = attempt_tracer.clone();
            async move {
                state.attempts += 1;
                if let Some(tracer) = tracer.as_ref() {
                    tracer.note(&format!("solution loop: attempt {}", state.attempts));
                }
                let prompt = format!(
                    "Solve this problem and verify the result.\n\nProblem:\n{}\n\n{}\n{}\n\n\
                     Follow the method policy: understand, find the governing structure, derive, \
                     implement, then verify by a second independent route. Report the answer, the \
                     method, and the verification, or state precisely where you are blocked and \
                     what you established along the way.",
                    state.problem,
                    state.lesson_briefing(),
                    if state.fresh_context.is_empty() {
                        String::new()
                    } else {
                        format!("New material gathered since the last attempt:\n{}", state.fresh_context)
                    }
                );
                state.last_attempt = delegate(&subagents, "goals", prompt).await;
                state.fresh_context.clear();
                Ok(NodeResult::Update(state))
            }
        })
        .add_node("reflect", move |mut state: SolutionState, _ctx: NodeContext| {
            let subagents = reflect_agents.clone();
            let tracer = reflect_tracer.clone();
            async move {
                let prompt = format!(
                    "Judge one attempt at a problem and extract the lesson.\n\nProblem:\n{}\n\n\
                     Attempt report:\n{}\n\n{}\n\n\
                     Answer exactly these three things:\n\
                     VERDICT: SOLVED if the attempt reached a specific final answer AND verified \
                     it by a second independent route; otherwise UNSOLVED. An unverified answer \
                     is UNSOLVED.\n\
                     PROGRESS: YES if this attempt established something the previous ones had \
                     not; otherwise NO.\n\
                     LESSON: one or two sentences naming the specific thing to do differently \
                     next time. Name the misstep and the concrete alternative. Do not restate the \
                     problem or give generic advice.",
                    state.problem,
                    state.last_attempt,
                    state.lesson_briefing()
                );
                let reflection = delegate(&subagents, "reflection", prompt).await;

                let upper = reflection.to_uppercase();
                // Require the explicit positive verdict: anything unparsable or
                // hedged leaves the loop running rather than declaring success.
                state.solved = upper.contains("VERDICT: SOLVED")
                    || upper.contains("VERDICT:SOLVED");
                let progressed = upper.contains("PROGRESS: YES") || upper.contains("PROGRESS:YES");
                if progressed {
                    state.unproductive = 0;
                } else {
                    state.unproductive += 1;
                }
                let lesson = extract_lesson(&reflection);
                if let Some(tracer) = tracer.as_ref() {
                    tracer.note(&format!(
                        "solution loop: verdict {}, progress {}, next {}",
                        if state.solved { "solved" } else { "unsolved" },
                        if progressed { "yes" } else { "no" },
                        route(&state)
                    ));
                }
                state.lessons.push(lesson);
                Ok(NodeResult::Update(state))
            }
        })
        .add_node("diversify", move |mut state: SolutionState, _ctx: NodeContext| {
            let subagents = diversify_agents.clone();
            let tracer = diversify_tracer.clone();
            async move {
                if let Some(tracer) = tracer.as_ref() {
                    tracer.note("solution loop: stuck, gathering new angles");
                }
                // Three independent angles, run concurrently: what is already
                // written down, what the numbers themselves say, and what a
                // different method would be.
                let library = delegate(
                    &subagents,
                    "librarian",
                    format!(
                        "Build a local reference set for this problem. Find primary treatments of \
                         the mathematics involved, download them into the workspace reference \
                         library, index them, and report what is now available locally with its \
                         source URLs.\n\nProblem:\n{}\n\n{}",
                        state.problem,
                        state.lesson_briefing()
                    ),
                );
                let patterns = delegate(
                    &subagents,
                    "pattern_finder",
                    format!(
                        "Look for exploitable structure in the data this investigation has already \
                         produced. Read the workspace results, extract the relevant integer \
                         sequences, and run the sequence tools on them. Report only regularities \
                         that hold exactly over every term, and say plainly that they are \
                         conjectures.\n\nProblem:\n{}",
                        state.problem
                    ),
                );
                let invention = delegate(
                    &subagents,
                    "inventor",
                    format!(
                        "Propose a genuinely different line of attack. The approaches tried so far \
                         have not worked; do not restate them. Name a specific alternative \
                         formulation, transform, or theory, say why it suits this problem, and \
                         give the first concrete step.\n\nProblem:\n{}\n\n{}",
                        state.problem,
                        state.lesson_briefing()
                    ),
                );
                let (library, patterns, invention) = tokio::join!(library, patterns, invention);

                state.fresh_context = format!(
                    "Reference material:\n{library}\n\nStructural observations:\n{patterns}\n\n\
                     Proposed alternative approach:\n{invention}"
                );
                state.unproductive = 0;
                Ok(NodeResult::Update(state))
            }
        })
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
        .add_node("done", |state: SolutionState, _ctx: NodeContext| async move {
            Ok(NodeResult::Update(state))
        })
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
