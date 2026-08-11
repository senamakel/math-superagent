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
use super::folder_index;
use super::teams::TeamHandle;

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
    workspace: Option<&Path>,
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
    // Resumption is a property of the workspace, not of the loop's counter:
    // every restart resets the counter while the files survive.
    let continuation = continuation_briefing(
        state.attempts,
        workspace.is_some_and(has_executable_artifact),
    );
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
    if state.attempts == 1 {
        open_with_execution(subagents, tracer, &state.problem);
    }
    state.last_attempt = delegate(subagents, "goals", prompt).await;
    state.fresh_context.clear();
    state
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
         program, run that instead of writing a second one. Report the command you ran and \
         its exact output, and say for each worked example whether it matched."
    )
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
        return "This run continues work already in the workspace: earlier programs, notes and \
                beliefs are on disk. Read GOAL.md and MEMORY.md, then CONTINUE from what they \
                say. Do not re-extract the statement or re-derive what MEMORY.md already \
                records — establish the next unresolved thing and run a program that settles it. \
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
            "This is attempt {attempt}. Earlier attempts already wrote the workspace files; read \
             GOAL.md and MEMORY.md and CONTINUE from there. Do not re-extract or re-document the \
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
///
/// It lands in `L0/` because a reflection is an original: the judgement of one
/// attempt, written once, never rewritten. Folds of it are what the levels
/// above hold.
fn reflection_filename(workspace: Option<&Path>, millis: u128, learnings: usize) -> String {
    let batch = workspace.map_or(0, |workspace| {
        super::context_tree::open_batch(workspace, "reflections", 0)
    });
    let folder = format!("reflections/{}", super::context_tree::batch_dir(0, batch));
    if learnings == 0 {
        format!("{folder}/{millis}_nothing.md")
    } else {
        format!("{folder}/{millis}_{learnings:02}_learnings.md")
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
    let relative = reflection_filename(Some(workspace), millis, learnings);
    let path = workspace.join(&relative);
    if let Some(parent) = path.parent() {
        let _ = tokio::fs::create_dir_all(parent).await;
    }
    let body = format!(
        "# Reflection after attempt {attempt}\n\n{}\n",
        reflection.trim()
    );
    if tokio::fs::write(&path, body).await.is_ok() {
        index_reflection(workspace, &relative, attempt, reflection, learnings).await;
        if let Some(tracer) = tracer {
            tracer.note(&format!("logged {relative}"));
        }
    }
}

/// Records the new reflection in `reflections/INDEX.md`.
///
/// The folder carries an index for the same reason `research/` and `toolkits/`
/// do: a directory of `1786436304918_01_learnings.md` says when each attempt
/// was judged and nothing about what any of them found, so anyone looking for
/// the attempt that established something has to open all of them. The
/// filename already encodes whether a reflection taught the run anything; the
/// index is what says *what*.
///
/// Written directly rather than through the index tools because no agent is in
/// the loop here — the solution graph writes this file itself — and best
/// effort for the same reason the reflection body is: the lesson is already in
/// the loop state, and losing a row must not cost the run anything.
async fn index_reflection(
    workspace: &Path,
    relative: &str,
    attempt: usize,
    reflection: &str,
    learnings: usize,
) {
    let index_path = workspace.join("reflections").join(folder_index::INDEX_FILE);
    let existing = tokio::fs::read_to_string(&index_path)
        .await
        .unwrap_or_default();
    let mut entries = folder_index::parse(&existing);
    // Rows name the level the reflection sits in, not just the file, because
    // the index is the root of the reflections tree rather than a listing of
    // the folder it happens to share a name with.
    let name = relative.strip_prefix("reflections/").unwrap_or(relative);
    let verdict = if reflection.to_uppercase().contains("VERDICT: SOLVED") {
        "solved"
    } else {
        "unsolved"
    };
    let summary = extract_lesson(reflection);
    let summary = summary.trim().replace('\n', " ");
    let description = format!(
        "Attempt {attempt}, judged {verdict}, {learnings} learning(s). {}",
        if summary.is_empty() {
            "No actionable lesson.".to_string()
        } else {
            summary
        }
    );
    entries.insert(name.to_string(), description);
    // The reflections index is written by the loop and read by the planners;
    // no agent folds it, so it carries no synthesis to preserve.
    let rendered = folder_index::render("reflections", &entries, &folder_index::brief(&existing));
    let _ = tokio::fs::write(&index_path, rendered).await;
}

/// Judges the last attempt and records the lesson it yields.
async fn reflect_step(
    subagents: &AsyncSubagentManager,
    tracer: Option<&Arc<RunTracer>>,
    workspace: Option<&Path>,
    patterns: &PatternMailbox,
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
    // It is *detached*, not awaited: see [`PatternMailbox`]. The loop routes on
    // the reflection alone, so making it wait for a sequence analysis bought
    // nothing and cost a live run half an hour of stalled loop.
    let pattern_prompt = format!(
        "Look for exploitable structure in the data this attempt just produced. Read the \
         workspace results, extract the integer sequences in them, and run the sequence tools \
         on them. Where a check needs a computation the tools do not do, write and run the \
         program yourself, or delegate it. Report only regularities that hold exactly over \
         every term supplied, say plainly that they are conjectures, and give the first term \
         that would falsify each one.\n\nProblem:\n{}",
        state.problem
    );
    let pattern_agents = subagents.clone();
    let pattern_outbox = patterns.clone();
    tokio::spawn(async move {
        let report = delegate(&pattern_agents, "pattern_finder", pattern_prompt).await;
        pattern_outbox.post(report);
    });
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
    let lesson = extract_lesson(&reflection);
    // Tell the teams what this attempt learned. They run beside the loop and
    // would otherwise keep enriching the workspace against the run's opening
    // understanding of the problem, which is the understanding the attempts
    // have been busy correcting. Posting never waits: a full inbox drops the
    // note rather than stalling the solve to deliver it.
    for team in teams {
        team.post("solver", format!("Attempt {}: {lesson}", state.attempts));
    }
    state.lessons.push(lesson);
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
                 contradicts what MEMORY.md currently asserts.\n\n\
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

/// Where a detached pattern run leaves its report for a later attempt.
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
#[derive(Clone, Default)]
struct PatternMailbox(Arc<std::sync::Mutex<Vec<String>>>);

impl PatternMailbox {
    /// Leaves a finished report for the next attempt.
    fn post(&self, report: String) {
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
    fn collect(&self) -> String {
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
    teams: Vec<TeamHandle>,
    state: SolutionState,
) -> Result<SolutionState> {
    let attempt_agents = subagents.clone();
    let attempt_tracer = tracer.clone();
    let reflect_agents = subagents.clone();
    let reflect_tracer = tracer.clone();
    let attempt_workspace = workspace.clone();
    let reflect_workspace = workspace;
    let diversify_agents = subagents.clone();
    let diversify_tracer = tracer;
    let pattern_mailbox = PatternMailbox::default();
    let reflect_teams = teams;

    let graph = GraphBuilder::<SolutionState, SolutionState>::overwrite()
        .add_node("attempt", move |state: SolutionState, _ctx: NodeContext| {
            let subagents = attempt_agents.clone();
            let tracer = attempt_tracer.clone();
            let workspace = attempt_workspace.clone();
            async move {
                Ok(NodeResult::Update(
                    attempt_step(&subagents, tracer.as_ref(), workspace.as_deref(), state).await,
                ))
            }
        })
        .add_node("reflect", move |state: SolutionState, _ctx: NodeContext| {
            let subagents = reflect_agents.clone();
            let mailbox = pattern_mailbox.clone();
            let teams = reflect_teams.clone();
            let tracer = reflect_tracer.clone();
            let workspace = reflect_workspace.clone();
            async move {
                Ok(NodeResult::Update(
                    reflect_step(
                        &subagents,
                        tracer.as_ref(),
                        workspace.as_deref(),
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
