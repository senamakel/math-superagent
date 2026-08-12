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
    mailbox: &Mailbox,
    teams: &[TeamHandle],
    mut state: SolutionState,
) -> SolutionState {
    let prompt = format!(
        "Judge one attempt at a problem and extract the lesson.\n\nProblem:\n{}\n\n\
         Attempt report:\n{}\n\n{}\n\n\
         Answer exactly these four things:\n\
         VERDICT: SOLVED if the attempt reached a specific final answer AND verified it by a \
         second independent route; otherwise UNSOLVED. An unverified answer is UNSOLVED.\n\
         PROGRESS: YES if this attempt established something the previous ones had not; \
         otherwise NO.\n\
         KIND: MATHEMATICAL if what it established is a fact, bound, structure, or refutation \
         that holds independently of how far a program was run. COMPUTATIONAL if it is a larger \
         instance of something an earlier attempt already computed — the same method at a bigger \
         size, a bound pushed further, more cases checked. NONE if it established nothing. \
         Verifying more cases of a conjecture is COMPUTATIONAL; finding out why the cases hold \
         is MATHEMATICAL.\n\
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
    let patterns = mailbox.collect();
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

    let progressed = record_verdict(&reflection, tracer, workspace, &mut state);
    let lesson = extract_lesson(&reflection);
    tell_teams(teams, &state, progressed, &lesson);
    state.lessons.push(lesson);
    // Every completed cycle opens a line-of-attack search, not only a stuck
    // one. Spawned last, once the verdict and the lesson are in the state, so
    // the inventor is told what this attempt actually established.
    open_invention(subagents, tracer, workspace, mailbox, &state);
    state
}

/// Opens a line-of-attack search beside the loop at the end of a full cycle.
///
/// The inventor used to run only inside `diversify`, on two consecutive
/// unproductive attempts. That gate is reachable in principle and was not
/// reached in practice: it needs two completed attempt/judge/reflect cycles,
/// and a run whose attempts take the better part of an hour spends its whole
/// wall clock inside the first one. Across a day of live runs on three
/// workspaces the inventor was spawned once, and the approach ledger it writes
/// to never existed on disk — so the cheapest question in the runtime, "is
/// there a different line of attack", was the one never asked.
///
/// This is the pattern agent's argument one role wider. A proposal is worth as
/// much an attempt later, so nothing waits on it: the arm is detached and its
/// report is posted to the same mailbox the next attempt drains. Diversify
/// still runs its own arm and still *awaits* it, because there the whole point
/// is to change direction before trying again.
///
/// It runs only on `Retry`. `Diversify` runs the same arm one step later and
/// would make it twice; `Solved` and `Blocked` end the loop, and proposing new
/// mathematics to a run that has stopped is spending a child run on nobody.
fn open_invention(
    subagents: &AsyncSubagentManager,
    tracer: Option<&Arc<RunTracer>>,
    workspace: Option<&Path>,
    outbox: &Mailbox,
    state: &SolutionState,
) {
    if route(state) != Route::Retry {
        return;
    }
    if let Some(tracer) = tracer {
        tracer.note("solution loop: opening a line-of-attack search beside the next attempt");
    }
    let subagents = subagents.clone();
    let workspace = workspace.map(Path::to_path_buf);
    let outbox = outbox.clone();
    let state = state.clone();
    tokio::spawn(async move {
        let (candidates, grounding) = invention_arm(&subagents, workspace.as_deref(), &state).await;
        let report = merge_context(&[
            ("Proposed lines of attack", &candidates),
            ("What the literature says about them", &grounding),
        ]);
        outbox.post(report);
    });
}

/// Reads the reflection's verdict into the state, and returns whether the
/// attempt progressed.
///
/// Split out of [`reflect_step`] because it is where every counter the loop
/// routes on is moved, and those rules are worth reading in one piece rather
/// than interleaved with the delegation that produced the reply.
fn record_verdict(
    reflection: &str,
    tracer: Option<&Arc<RunTracer>>,
    workspace: Option<&Path>,
    state: &mut SolutionState,
) -> bool {
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
    // Counted only on an explicit COMPUTATIONAL. A reflection that omitted the
    // field, or whose wording could not be parsed, leaves the count where it
    // was: an unparsed verdict must never be what drives the loop somewhere,
    // and treating silence as "scaling again" would send a run diversifying on
    // the strength of two malformed replies. MATHEMATICAL clears it, because
    // the run has changed what it is doing.
    let kind = kind_of(&upper);
    match kind {
        Progress::Computational => state.computational += 1,
        Progress::Mathematical => state.computational = 0,
        Progress::Unstated => {}
    }
    if let Some(tracer) = tracer {
        // The kind is on the line because it is the one signal here that can
        // send a run to diversify while it is reporting progress every time.
        // Without it that turn reads, to anyone watching, as the loop giving up
        // on an attempt that had just succeeded.
        tracer.note(&format!(
            "solution loop: verdict {}, progress {} ({}, {} consecutive scaling), next {}",
            if state.solved { "solved" } else { "unsolved" },
            if progressed { "yes" } else { "no" },
            match kind {
                Progress::Mathematical => "mathematical",
                Progress::Computational => "computational",
                Progress::Unstated => "kind unstated",
            },
            state.computational,
            route(state)
        ));
    }
    progressed
}
