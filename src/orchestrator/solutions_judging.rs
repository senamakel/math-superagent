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
///
/// It is given the workspace as well as the report, and the reason is that the
/// report is the first thing lost. `RunBudget` caps an agent run, and a `goals`
/// run pursuing an open goal does not stop on its own, so the ordinary way an
/// attempt ends is the cap killing it — which destroys its context and its
/// report while leaving every file it wrote on disk. One evening, all three live
/// Euler attempts were killed at exactly 30:00 and every verdict that followed
/// was 1/5 or 2/5 with "progress no". One of those runs had reproduced both
/// check values its problem supplied, to all ten digits, and had 38 exact points
/// cross-validated by two independent enumerators. The judge could not see any
/// of it: it was scoring silence and calling it no progress.
pub(in crate::orchestrator) async fn judge_step(
    subagents: &AsyncSubagentManager,
    tracer: Option<&Arc<RunTracer>>,
    workspace: Option<&Path>,
    mut state: SolutionState,
) -> SolutionState {
    let prompt = format!(
        "Judge how this attempt was conducted.\n\nProblem:\n{}\n\n\
         This is attempt {} of at most {MAX_ATTEMPTS}. {}\n\n\
         The attempt reported:\n{}\n{}",
        state.problem,
        state.attempts,
        if state.restarts >= MAX_RESTARTS {
            "The run has already been restarted as often as it may be, so RESTART is no \
             longer available to you: score, and PROCEED or STEER."
        } else {
            "RESTART is available but expensive; it discards this direction and spends a \
             fresh attempt."
        },
        state.last_attempt,
        workspace.map_or_else(String::new, evidence_briefing)
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

/// How many of a folder's entries to count before giving up.
///
/// Counting is bounded for the same reason every other walk here is: a
/// workspace is agent-written and nothing stops it holding ten thousand files.
/// The number only has to separate "none" from "some" from "a lot".
const MAX_COUNTED: usize = 500;

/// Renders what the attempt left on disk, for a judge that cannot see it.
///
/// Deliberately counts rather than reads. What each file *means* is a
/// judgement, and the judge is about to make it from the report; whether the
/// attempt executed anything, established anything, or proposed anything is not
/// a judgement, so it is measured — the same split the rest of this crate makes
/// between an agent's work and a check on it.
///
/// The counts are chosen to be the ones a timed-out attempt cannot tell you
/// itself. Captured output is what a program *produced*, which separates a run
/// writing programs from a run running them; the claim split separates what the
/// run established from what it read somewhere; approaches say whether the
/// inventor's proposals survived to disk; and the gap counts say whether the
/// run has written down what a proof would consist of and how much of it it now
/// has — the one measure here that separates an investigation closing in on a
/// theorem from one accumulating verified data beside it.
fn evidence_briefing(workspace: &Path) -> String {
    let captured = captured_outputs(workspace);
    let ledger = super::claims::collect(workspace);
    let approaches = count_entries(&workspace.join("research/approaches"));
    let threads = count_entries(&workspace.join("research/threads"));
    // Counted from the parsed skeletons rather than from the directory, because
    // the number that matters is not how many files exist but how many lemmas
    // are still owed — and how many the run has already closed, which is the
    // only measure here that can go up without anything new being computed.
    let skeletons = super::backward::collect(workspace);
    let gaps_open = skeletons.open_gaps().len();
    let gaps_discharged = skeletons.discharged_ids().len();

    format!(
        "\nWhat the attempt left on disk, counted rather than reported — the report above is \
         written last and is the first thing lost when an attempt is cut off, so treat this as \
         the more reliable of the two when they disagree:\n\
         - captured output under `code/`: {} file(s) a program produced\n\
         - claims: {} established here, {} taken from a source's word, {} read out of a \
         catalogue\n\
         - approaches proposed: {approaches}\n\
         - threads open: {threads}\n\
         - gaps in the proof skeletons: {gaps_open} open, {gaps_discharged} discharged\n\
         An attempt that reported nothing and wrote nothing is stalled. An attempt that reported \
         nothing and left work here is not — score what is here.{}{}{}",
        captured.len(),
        ledger.established(),
        ledger.asserted(),
        ledger.catalogued(),
        disagreement_warning(workspace, &captured),
        if unclaimed_results(&captured, &ledger) {
            "\n\nOne thing to weigh against the score: programs here have produced output and \
             the claim ledger records nothing this run established — every claim in it is \
             somebody else's word. A result that stays in a captured file reaches nobody: the \
             ledger is what the planning roles read, and work absent from it will be done \
             again. Name the established result and say it belongs in a claim block."
        } else {
            ""
        },
        if oracle_unchecked(workspace, &captured) {
            "\n\nOne thing to weigh against the score: `code/` holds the naive oracle and at \
             least one faster program, and no captured output records the oracle having been \
             run. A fast method nobody has checked against the oracle is not a result yet, \
             however confident its comments are — say so in your steer."
        } else {
            ""
        }
    )
}

/// What a program prints when a check against a known value came out wrong.
///
/// Matched against output whose whitespace has been collapsed and lowercased,
/// so `agree?  False` and `Agree? False` both land. Each marker pairs a
/// comparison word with a negative rather than standing on one: a bare `FAIL`
/// is what a legitimate row of a classification table says — one live run's
/// output has `20  -  FAIL  -  -  NotAlgebraic` for a value that genuinely is
/// not algebraic — and reading that as a broken check would cry wolf on every
/// run that enumerates cases honestly.
const DISAGREEMENT_MARKERS: [&str; 7] = [
    "agree? false",
    "agrees? false",
    "match? false",
    "matches? false",
    "mismatch",
    "disagree",
    "does not match",
];

/// How many disagreeing files to name before the list stops helping.
const MAX_NAMED: usize = 3;

/// Reports captured output whose own text says a check came out wrong.
///
/// [`oracle_unchecked`] asks whether the oracle was ever run. This asks the next
/// question, which is the one Project Euler 761 turns on: it *was* run, and it
/// disagreed. That workspace holds `code/indep_game_encoding_OUTPUT.txt`, whose
/// every line reads `agree? False` — the run's only independent solver returns
/// 4.14159265 for the circle against a published 4.60333885, 4.09372236 for the
/// square against 5.78859314 — and nothing in the runtime read a word of it. The
/// run went on holding an answer supported by one route while the file that
/// would have said so sat unread beside it, and the loop's verdicts were
/// decided entirely by a report that never mentioned it.
///
/// Whether the disagreement is fatal stays a judgement — a deliberately
/// falsified model *should* print that it disagrees, and one of 761's does. What
/// is counted is only that the run's own output contains the words, which is
/// what nobody was looking at.
fn disagreement_warning(workspace: &Path, captured: &[PathBuf]) -> String {
    let failing: Vec<String> = captured
        .iter()
        .filter(|path| {
            std::fs::read_to_string(path).is_ok_and(|text| {
                let flattened = flatten(&text);
                DISAGREEMENT_MARKERS
                    .iter()
                    .any(|marker| flattened.contains(marker))
            })
        })
        .map(|path| {
            path.strip_prefix(workspace)
                .unwrap_or(path)
                .display()
                .to_string()
        })
        .collect();
    if failing.is_empty() {
        return String::new();
    }
    format!(
        "\n\nWeigh this before anything the report says: {} captured output(s) record a check \
         that came out wrong — {}. A program whose own output says it disagrees with a value \
         the run already trusts has not been reconciled, and an answer standing beside an \
         unreconciled disagreement is supported by one route, not two. Open the file rather \
         than taking the report's word, decide whether the disagreement is a falsified model \
         behaving correctly or a result the run is quietly ignoring, and name in your steer \
         which one to reconcile first.",
        failing.len(),
        failing
            .iter()
            .take(MAX_NAMED)
            .cloned()
            .collect::<Vec<_>>()
            .join(", ")
    )
}

/// Lowercases text and collapses every run of whitespace to one space.
fn flatten(text: &str) -> String {
    text.to_ascii_lowercase()
        .split_whitespace()
        .collect::<Vec<_>>()
        .join(" ")
}

/// How deep under `code/` to look for captured output.
const MAX_OUTPUT_DEPTH: usize = 3;

/// Collects the files under `code/` that a program wrote rather than a person.
///
/// This used to read `code/out/` alone, which is where the layout says captured
/// output belongs, and a live run showed what "says" is worth. Project Euler 761
/// captures every run as `code/<program>_OUTPUT.txt` beside the program, so its
/// `code/out/` held one empty file named `Untitled` while a dozen real outputs
/// sat one level up — and the briefing would have told the judge the run had
/// produced nothing and then accused it of never running its oracle, on a run
/// whose `brute.py` output reproduces the published circle value to eight
/// digits. A check that only sees the tidy layout reports the untidy run as
/// idle, which is the opposite of the truth.
///
/// Source and notes are excluded by extension: `.py` and `.sh` are what a person
/// wrote, and `.md` is the run's commentary, already counted as a claim. What
/// remains is what something printed.
fn captured_outputs(workspace: &Path) -> Vec<PathBuf> {
    let mut found = Vec::new();
    collect_outputs(&workspace.join(super::layout::CODE_DIR), MAX_OUTPUT_DEPTH, &mut found);
    found
}

/// Walks one folder into `found`, bounded in both depth and count.
fn collect_outputs(folder: &Path, depth: usize, found: &mut Vec<PathBuf>) {
    if depth == 0 || found.len() >= MAX_COUNTED {
        return;
    }
    let Ok(entries) = std::fs::read_dir(folder) else {
        return;
    };
    for entry in entries.flatten().take(MAX_COUNTED) {
        if found.len() >= MAX_COUNTED {
            return;
        }
        let name = entry.file_name();
        let name = name.to_string_lossy();
        // Caches and hidden state are neither source nor result.
        if name.starts_with('.') || name == "__pycache__" {
            continue;
        }
        let path = entry.path();
        if path.is_dir() {
            collect_outputs(&path, depth - 1, found);
        } else if !super::layout::is_authored(&name) {
            found.push(path);
        }
    }
}



/// Reports a run whose programs have produced output that reached no claim.
///
/// The claim ledger is what every planning role reads; a result that stays in a
/// captured file reaches nobody, and the next attempt does the work again. The
/// magic-square-of-squares run is what that costs. Across seventy minutes it
/// proved its parametrisation complete by an exact rank computation over Q
/// (8x9 incidence matrix, rank 7, kernel dimension 2), verified both of the
/// literature's seven-square near-misses digit by digit against Bremner 1999
/// with provenance, and established that its own four-million-grid scan reaches
/// only five square entries among distinct ones — and `research/CLAIMS.md` held
/// three rows, exactly one of them with a readable status, none of them the
/// run's own. It survived a judge verdict and a reflection unchanged.
///
/// Deliberately the crudest form of the question: are there captured outputs at
/// all, and has the run established *anything*. A file-by-file "is this one
/// claimed" would need to know what a claim is about, which is a judgement and
/// belongs to the agent. Whether the established column is empty is a count.
fn unclaimed_results(captured: &[PathBuf], ledger: &super::claims::Ledger) -> bool {
    !captured.is_empty() && ledger.established() == 0
}

/// The naive oracle's path, as [`oracle_prompt`] names it.
const ORACLE_FILE: &str = "brute.py";

/// Reports a fast method that has never been checked against the oracle.
///
/// `code/AGENTS.md` already requires keeping the naive oracle, and keeping it is
/// enforced. *Agreeing* with it was not, and Project Euler 241 is what that
/// costs. Its `solution.py` carries a confident justification for its central
/// pruning rule — "e > a leaves surplus d in the numerator that no later sigma
/// factor can cancel (all coprime to d)" — which is false: σ(13) = 14, so a
/// larger prime can contribute the very factor the argument says cannot appear.
/// The program finds 5 of the 9 terms below 10^8. `brute.py` sat in the same
/// folder, correct by construction, and the two were never run against each
/// other. The run then reported a correct answer it had taken from a catalogue,
/// so nothing anywhere disagreed with anything.
///
/// The check is a substring, deliberately. Whether two methods agree *on the
/// mathematics* is a judgement and stays with the agent; whether any captured
/// output so much as mentions the oracle is a count, so it is counted. A run
/// that has executed the oracle and captured the result clears this
/// immediately; a run that has never run it cannot.
fn oracle_unchecked(workspace: &Path, captured: &[PathBuf]) -> bool {
    let code = workspace.join(super::layout::CODE_DIR);
    if !code.join(ORACLE_FILE).is_file() {
        // No oracle to disagree with. That is a different fault, and
        // `oracle_prompt` is what addresses it.
        return false;
    }
    let others = std::fs::read_dir(&code).map_or(0, |entries| {
        entries
            .flatten()
            .take(MAX_COUNTED)
            .filter(|entry| {
                let name = entry.file_name();
                let name = name.to_string_lossy();
                name.ends_with(".py") && name != ORACLE_FILE
            })
            .count()
    });
    if others == 0 {
        // Only the oracle exists, so there is no faster method to check.
        return false;
    }
    !mentions_oracle(captured)
}

/// Whether any captured output names the oracle, by filename or in its text.
fn mentions_oracle(captured: &[PathBuf]) -> bool {
    let stem = ORACLE_FILE.trim_end_matches(".py");
    captured.iter().any(|path| {
        if path
            .file_name()
            .is_some_and(|name| name.to_string_lossy().contains(stem))
        {
            return true;
        }
        std::fs::read_to_string(path).is_ok_and(|text| text.contains(stem))
    })
}

/// Counts a folder's entries, bounded, and answers zero for a missing folder.
///
/// Scaffolding does not count. `workspace/template` seeds
/// `research/approaches/` and `research/threads/` so the roles told to write
/// there find a directory, and each seeded folder carries a `README.md` saying
/// what belongs in it — which git needs anyway, since it cannot track an empty
/// directory. Counting those would tell the judge every run had proposed an
/// approach and opened a thread before it did anything at all, which is the
/// briefing inventing evidence rather than measuring it.
fn count_entries(folder: &Path) -> usize {
    std::fs::read_dir(folder).map_or(0, |entries| {
        entries
            .flatten()
            .take(MAX_COUNTED)
            .filter(|entry| {
                let name = entry.file_name();
                let name = name.to_string_lossy();
                !name.starts_with('.') && !name.eq_ignore_ascii_case("README.md")
            })
            .count()
    })
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
pub(in crate::orchestrator) async fn reflect_step(
    subagents: &AsyncSubagentManager,
    tracer: Option<&Arc<RunTracer>>,
    workspace: Option<&Path>,
    memory: &VectorStore,
    beside: &Beside,
    mut state: SolutionState,
) -> SolutionState {
    let mailbox = &beside.patterns;
    let prompt = format!(
        "Judge one attempt at a problem and extract the lesson.\n\nProblem:\n{}\n\n\
         Attempt report:\n{}\n\n{}\n\n\
         Answer exactly these four things:\n\
         VERDICT: SOLVED if the attempt reached a specific final answer AND verified it by a \
         second independent route. UNVERIFIED if it reached a specific final answer, exactly \
         one route supports it, and you can say concretely why no second route is available — \
         the literature leaves this case open, or every independent construction the run built \
         fails to reproduce values that are already known. Name the answer and the missing \
         route in LESSON when you say UNVERIFIED; it ends the run, so do not use it while a \
         second route is merely unbuilt. Otherwise UNSOLVED.\n\
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
    tell_teams(&beside.teams, &state, progressed, &lesson);
    state.lessons.push(lesson);
    // Every completed cycle opens a line-of-attack search, not only a stuck
    // one. Spawned last, once the verdict and the lesson are in the state, so
    // the inventor is told what this attempt actually established.
    open_invention(subagents, tracer, workspace, mailbox, &state);
    // And the other question nothing in the loop asks by itself: not what else
    // could get us there, but what would be enough. The cadence is counted here
    // and read by the `goals` sub-workflow, which decides whether this cycle is
    // the one that decomposes — see `super::workflow_goals`. Counting it here
    // rather than there keeps the loop head the accumulator's sole writer.
    state.since_reduction += 1;
    state
}

/// What the reduction cadence does not count as the workspace having moved.
///
/// Both halves of what the reducer itself writes: the folder of skeletons and
/// the table derived from it. `fingerprint_excluding` matches on file *names*,
/// so the folder entry skips the whole directory.
const REDUCTION_BLIND_SPOTS: [&str; 2] = ["backward", "BACKWARD.md"];

/// Everything running beside the loop that a reflection has to reach.
///
/// Grouped rather than passed as three more parameters, for the reason
/// [`Mailboxes`] is grouped: they are one idea — the work the loop starts and
/// does not wait for — and the alternative is a signature nobody can read.
#[derive(Clone)]
pub(super) struct Beside {
    /// What the pattern team found, drained here and by the attempt.
    pub(super) patterns: Mailbox,
    /// The reduction arm's outbox and the gate admitting one of it at a time.
    pub(super) reduction: Reduction,
    /// The standing teams, told after every verdict how the attempt went.
    pub(super) teams: Vec<TeamHandle>,
}

/// The one reduction a run may have in flight, and where its report goes.
///
/// Grouped rather than passed as two more parameters for the reason
/// [`Mailboxes`] groups its own: they are one idea, and a caller holding the
/// outbox without the gate could open a second reduction over the first.
#[derive(Clone)]
pub(super) struct Reduction {
    /// Where the open gaps are left for the next attempt.
    pub(super) outbox: Mailbox,
    /// What stops two reducers writing the same skeleton file.
    pub(super) gate: ReductionGate,
}

/// Admits one reduction at a time, for the whole run.
///
/// [`open_invention`] needs no such thing: two inventors produce two approach
/// files under two slugs, which is untidy and nothing more. Two reducers is a
/// different failure. They decompose the same goal, so they write the same
/// `research/backward/<slug>.md`, `write_document` is last-writer-wins, and the
/// gaps the loser found are gone with no error anywhere — the workspace's own
/// version of two containers on one workspace, where both runs work, both
/// write, and the damage only shows up in what is missing later.
///
/// Claimed before the spawn and released inside it, so a reduction that outlives
/// the cycle that opened it still holds the gate.
/// It also remembers the workspace it last decomposed, which is the second
/// bound: the reducer's inputs are what the run has established, so a cadence
/// tick over a tree that has not moved would rewrite the same skeleton from the
/// same evidence. Kept here rather than in [`SolutionState`] because it is a
/// fact about the arm rather than about the loop, and the loop does not route
/// on it.
#[derive(Clone, Default)]
pub(super) struct ReductionGate {
    /// Whether a reduction holds the gate right now.
    busy: Arc<std::sync::atomic::AtomicBool>,
    /// The workspace fingerprint the last opened reduction saw.
    seen: Arc<std::sync::atomic::AtomicU64>,
    /// Whether anything has been decomposed yet, so a genuinely empty
    /// workspace whose fingerprint happens to hash to zero is still decomposed
    /// once.
    ever: Arc<std::sync::atomic::AtomicBool>,
}

impl ReductionGate {
    /// Takes the gate, or reports that somebody already has it.
    fn claim(&self) -> bool {
        self.busy
            .compare_exchange(
                false,
                true,
                std::sync::atomic::Ordering::AcqRel,
                std::sync::atomic::Ordering::Acquire,
            )
            .is_ok()
    }

    /// Gives it back once the reduction has finished, however it finished.
    fn release(&self) {
        self.busy
            .store(false, std::sync::atomic::Ordering::Release);
    }

    /// Whether the workspace has changed since the last reduction was opened.
    fn moved(&self, fingerprint: u64) -> bool {
        !self.ever.load(std::sync::atomic::Ordering::Acquire)
            || self.seen.load(std::sync::atomic::Ordering::Acquire) != fingerprint
    }

    /// Records the workspace this reduction is being opened against.
    fn remember(&self, fingerprint: u64) {
        self.seen
            .store(fingerprint, std::sync::atomic::Ordering::Release);
        self.ever.store(true, std::sync::atomic::Ordering::Release);
    }
}

/// Opens a decomposition of the goal beside the loop, on a cadence.
///
/// The loop asks, every cycle, how the last attempt went. Nothing in it ever
/// asks what a proof of the goal would consist of, and the two questions have
/// different answers: an investigation can report genuine progress every single
/// attempt — a bound pushed further, more cases verified — and end its budget
/// with a great deal of data and no statement of what would have been enough.
/// A live Gilbreath workspace contains that statement and it took sixteen
/// operator directives to produce.
///
/// Detached, and that is [`open_invention`]'s argument rather than a new one: a
/// skeleton is worth as much an attempt later, nothing in [`route`] reads it,
/// and awaiting one would put a child run of unbounded length between the
/// reflection and the next attempt — which is the failure [`Mailbox`] was
/// written about, where a live run sat 33 minutes unable to start an attempt it
/// was ready for.
///
/// Three conditions, because there are three different ways this can go wrong.
/// The interval bounds what the ledger costs. The fingerprint bounds waste: the
/// reducer's inputs are the claim ledger and the threads, so a tick over a
/// research tree that has not moved would rewrite the same skeleton from the
/// same evidence. The gate bounds collision. A tick that fails the fingerprint
/// test deliberately does *not* reset the counter, so the next cycle tries
/// again rather than waiting another full interval.
///
/// The first of those three — the cadence — is no longer here. It is the
/// `goals` sub-workflow's opening switch (see `super::workflow_goals`), because
/// "how often" is exactly the kind of decision an operator wants to change
/// without a rebuild. The other two stay: a fingerprint and a claim are facts
/// about the workspace and about what is already running, and neither is
/// expressible as jq over the loop's state.
///
/// Returns whether a reduction was opened, which is what the caller resets the
/// cadence counter on.
pub(in crate::orchestrator) fn open_reduction(
    subagents: &AsyncSubagentManager,
    tracer: Option<&Arc<RunTracer>>,
    workspace: Option<&Path>,
    reduction: &Reduction,
    state: &SolutionState,
) -> bool {
    // Excluding what the reducer itself writes, or it would wake forever on its
    // own output — the reason `fingerprint_excluding` exists at all.
    let fingerprint = workspace.map(|workspace| {
        super::teams::fingerprint_excluding(workspace, &REDUCTION_BLIND_SPOTS)
    });
    if let Some(fingerprint) = fingerprint
        && !reduction.gate.moved(fingerprint)
    {
        if let Some(tracer) = tracer {
            tracer.note(
                "solution loop: nothing has landed since the last decomposition, not opening one",
            );
        }
        // Deliberately reported as "not opened": the cadence has come due and
        // been declined, so the caller leaves the counter where it is and the
        // next cycle asks again rather than waiting another full interval for
        // evidence that may have arrived meanwhile.
        return false;
    }
    if !reduction.gate.claim() {
        if let Some(tracer) = tracer {
            tracer.note("solution loop: a reduction is already in flight, not opening another");
        }
        return false;
    }
    if let Some(fingerprint) = fingerprint {
        reduction.gate.remember(fingerprint);
    }
    if let Some(tracer) = tracer {
        tracer.note("solution loop: decomposing the goal beside the next attempt");
    }
    let subagents = subagents.clone();
    let workspace = workspace.map(Path::to_path_buf);
    let outbox = reduction.outbox.clone();
    let gate = reduction.gate.clone();
    let state = state.clone();
    tokio::spawn(async move {
        let report = reduction_arm(&subagents, workspace.as_deref(), &state).await;
        outbox.post(report);
        gate.release();
    });
    true
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
///
/// Ending the run is the one decision here that cannot be walked back, so
/// `state.solved` carries three independent conditions rather than one: the
/// explicit positive verdict, an executable artifact on disk, and a reflection
/// that does not contradict itself by reporting no progress. Each was added
/// after a live run ended on the case it rules out.
pub(in crate::orchestrator) fn record_verdict(
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
    // The qualified close. It carries the same evidence requirement as SOLVED —
    // an answer nothing computed is not an answer, whether or not the reflection
    // hedged about how many routes reached it — and, unlike SOLVED, it has to be
    // said twice before it ends anything.
    let unverified = upper.contains("VERDICT: UNVERIFIED") || upper.contains("VERDICT:UNVERIFIED");
    let evidenced = workspace.is_none_or(has_executable_artifact);
    // ...and require the reflection to agree with itself. Solving the problem
    // is progress, so `VERDICT: SOLVED` beside `PROGRESS: NO` is not a close
    // call to resolve in favour of stopping — it is a reply that contradicts
    // itself, and the loop must not end on one.
    //
    // A live Gilbreath run ended exactly there. Its `goals` agent timed out,
    // the salvage path re-ran an already-queued script that re-confirmed an
    // already-hand-checked refutation, and the reflection wrote SOLVED over
    // PROGRESS: NO. The evidence test above passed, because the salvage really
    // had run a program; what it could not see is that the program established
    // nothing new. The reflection knew — its own lesson for the next attempt
    // said the salvage "was reported as task completion when it advanced
    // nothing" — but the verdict had already routed the run to `done`.
    let progressed = upper.contains("PROGRESS: YES") || upper.contains("PROGRESS:YES");
    state.solved = claimed && evidenced && progressed;
    if unverified && evidenced {
        state.unverified += 1;
    } else {
        state.unverified = 0;
    }
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
    if claimed && evidenced && !progressed {
        state.lessons.push(
            "Reported SOLVED while reporting PROGRESS: NO. Solving the problem is progress, so \
             those cannot both be true: either the attempt established something, in which case \
             say what and mark progress, or it did not, in which case it did not solve anything. \
             Re-running a program whose result the run already had is not a solution."
                .to_string(),
        );
        if let Some(tracer) = tracer {
            tracer.note("solution loop: SOLVED rejected, the reflection also reported no progress");
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
