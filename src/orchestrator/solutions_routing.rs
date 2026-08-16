/// What kind of gain an attempt reported.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
enum Progress {
    /// A fact, bound, structure, or refutation that stands on its own.
    Mathematical,
    /// A larger instance of a computation the run had already done.
    Computational,
    /// Nothing, or nothing this could read.
    Unstated,
}

/// Reads the reflection's `KIND` field from an already-uppercased reply.
///
/// Deliberately conservative: anything other than an explicit, recognised
/// answer is [`Progress::Unstated`], which moves no counter. The field decides
/// whether a run that reports progress every attempt still gets pushed into
/// diversifying, and a misread there either strands a run that was working or
/// spends three child runs on one that did not need it.
fn kind_of(upper: &str) -> Progress {
    for (marker, kind) in [
        ("KIND: MATHEMATICAL", Progress::Mathematical),
        ("KIND:MATHEMATICAL", Progress::Mathematical),
        ("KIND: COMPUTATIONAL", Progress::Computational),
        ("KIND:COMPUTATIONAL", Progress::Computational),
    ] {
        if upper.contains(marker) {
            return kind;
        }
    }
    Progress::Unstated
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

/// The gather-and-read arm: the librarian fetches, then the scholar reads.
///
/// Sequential inside one node on purpose. The scholar reads what the librarian
/// just downloaded, so a digest written before the documents land describes
/// nothing — and acquiring without reading is the gap this closes, since a
/// downloaded paper nobody has read has cost the run context and taught it
/// nothing. Two nodes would say the same thing with an extra edge.
pub(in crate::orchestrator) async fn diversify_library_arm(
    subagents: &AsyncSubagentManager,
    state: &SolutionState,
) -> Vec<Finding> {
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
    )
    .await;
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
    vec![
        Finding::new(Slot::Library, library),
        Finding::new(Slot::Digest, digest),
    ]
}

/// The structure arm: what the numbers this run has already produced show.
pub(in crate::orchestrator) async fn diversify_pattern_arm(
    subagents: &AsyncSubagentManager,
    state: &SolutionState,
) -> Vec<Finding> {
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
    )
    .await;
    vec![Finding::new(Slot::Patterns, patterns)]
}

/// The refutation arm: spend a bounded budget trying to break the statement.
///
/// It runs concurrently with the arms that assess the attempt, and that timing
/// is the point rather than a convenience. The runtime had four ways to prove
/// something — `sat_solver`, `smt_solver`, `theorem_prover`, `lean_prover` —
/// and every one of them is *delegated to* when a role decides to ask. None was
/// ever scheduled *against* the statement the run was pursuing, so a false
/// conjecture was attacked by proof for as long as the budget lasted.
///
/// The Equational Theories Project is the measurement that justifies the slot:
/// 524 small finite structures refuted 13.6 million of its 22 million
/// implications, 13.3 million at size 3 alone, for 165 CPU-hours, before any
/// clever proof search ran. Most false statements are false small, and finding
/// that out cheaply is worth more than the proof attempt it replaces.
///
/// What it attacks is read off disk rather than passed in, and from the two
/// ledgers that hold statements the run has committed to: the open gaps of the
/// proof skeletons, and the current rung of each difficulty ladder. Those are
/// exactly the propositions somebody has decided are worth proving, which makes
/// them exactly the ones worth trying to break. With neither on disk the arm
/// falls back to the goal itself.
pub(in crate::orchestrator) async fn refutation_arm(
    subagents: &AsyncSubagentManager,
    workspace: Option<&Path>,
    state: &SolutionState,
) -> Vec<Finding> {
    let targets = refutation_targets(workspace);
    let report = delegate(
        subagents,
        "refuter",
        format!(
            "Try to break one of the statements this run is currently trying to prove. Pick the \
             one most likely to be false rather than the one most central to the argument.\n\n\
             Look by hand first — n = 0, 1, 2, the empty case, the degenerate case where two \
             things coincide — because most false statements are false small and a counterexample \
             you can write in one line beats any search. Then encode the smallest fragment that \
             could still be false as a TPTP problem under `code/refute/<slug>.p` and call \
             `find_counterexample` on it.\n\n\
             Report which statement you attacked and which of the four answers came back. A \
             counterexample is a result the run banks, and it needs checking against the original \
             statement before you report it — the engine answers about what you wrote. A search \
             that found nothing is also a result: say which sizes were covered, and do not \
             upgrade that into `probably true`.\n\nProblem:\n{}\n\n{targets}",
            state.problem()
        ),
    )
    .await;
    // Beside the report rather than instead of it. The verdicts say what the
    // engine established; the report says which statement was attacked and
    // whether the counterexample survived being checked against the original,
    // which is a judgement no file records.
    let filed = workspace.map(super::refute::briefing).unwrap_or_default();
    let merged = merge_context(&[
        ("What the refuter reports", report.as_str()),
        ("Verdicts on disk", filed.as_str()),
    ]);
    vec![Finding::new(Slot::Refutation, merged)]
}

/// The verification arm: hand the statement graph's first entry to the kernel.
///
/// The refutation arm's argument, one engine over. The runtime had four ways to
/// prove something and every one of them was *delegated to* — and `lean_prover`
/// is the one where that costs the most, because everything else this runtime
/// produces is a reason to believe something and a proof the kernel accepted is
/// the thing itself. Across three live calibration runs nothing was formalised
/// at all, and no file on disk could tell a lemma Lean had checked from a
/// sentence a model had typed.
///
/// Three things make it affordable, and they are the same three decision.
///
/// **It picks rather than sweeps.** [`super::verify::next`] takes the first
/// entry of a ranking over the statement graph — what the run is already
/// building on, ordered by how much rests on it — so one check per pass goes to
/// the node whose mistake would cost the most. A fleet of provers is the other
/// way to cover a blueprint; this is the one that fits the container's memory
/// ceiling, and the queue is written into `research/BLUEPRINT.md` so what was
/// not reached is visible.
///
/// **It asks for something different the second time.** A node that survived a
/// proof attempt is asked to be decomposed, and its sub-lemmas become gaps —
/// which become blueprint nodes, which come back through this same ranking once
/// their dependencies are settled. That is the recursion, and it runs at the
/// speed of the loop rather than inside one turn.
///
/// **It stops.** `MAX_ATTEMPTS` is two and the attempt is recorded *before* the
/// prover is delegated to, so a node nobody can close stops being the
/// highest-ranked target instead of being re-attempted every pass for the rest
/// of the run. A record that cannot be written means no delegation: an
/// uncounted attempt is an unbounded one.
///
/// It returns nothing at all when there is no graph yet, which is the ordinary
/// state of an early run and costs a child run to discover any other way.
pub(in crate::orchestrator) async fn verification_arm(
    subagents: &AsyncSubagentManager,
    workspace: Option<&Path>,
    state: &SolutionState,
) -> Vec<Finding> {
    let Some(workspace) = workspace else {
        return Vec::new();
    };
    // Choosing and recording are one critical section, and the lock is what
    // makes them one. Schools share a workspace and run this arm concurrently:
    // without it, two of them read the same ranking, see the same zero attempts
    // on the same top-ranked node, and both spend the run's scarcest budget
    // proving it. Taken at the arm's boundary and released before the
    // delegation, so nothing the prover writes can meet it again — the rule
    // `worklock` states, since the mutex is not reentrant.
    let assignment = {
        let _writing = super::worklock::writes().await;
        let Some(assignment) = super::verify::next(workspace) else {
            return Vec::new();
        };
        if let Err(error) =
            super::verify::note_attempt(workspace, &assignment.target.id, assignment.stage).await
        {
            return vec![Finding::new(
                Slot::Verification,
                format!(
                    "No formalisation was attempted this pass: the attempt record under `{}` \
                     could not be written ({error}). Nothing was delegated, because an attempt \
                     this runtime cannot count is one it cannot stop repeating.",
                    super::verify::LEDGER_DIR
                ),
            )];
        }
        assignment
    };
    let instruction = match assignment.stage {
        super::verify::Stage::Prove => {
            "State this in Lean 4 against Mathlib and prove it. Add a `#print axioms` line for \
             every theorem the statement rests on, then call `lean_check` on the file.\n\n\
             Get the *statement* right before you get the proof right. A Lean proof of a \
             neighbouring statement is worth less than no proof at all, because it reads as a \
             check that passed — so write the statement, read it back against the source file \
             above, and say in your report which of the original's hypotheses each binder \
             carries.\n\n\
             If it passes, file it as a `claim` block with `status: formalised` and a \
             `formalisation:` line naming the file. Do not mark anything formalised that \
             `lean_check` did not pass."
        }
        super::verify::Stage::Decompose => {
            "You are not being asked to prove this again. The last attempt did not close it, so \
             break it down instead.\n\n\
             Split the statement into named sub-lemmas that would together give it, state each \
             one in Lean, and prove the ones you can. Leave `sorry` in the ones you cannot — a \
             `sorry` here is the point rather than a failure, because it says exactly where the \
             argument is missing. Then write the combining step: the theorem that follows from \
             the sub-lemmas, so the decomposition is checked even while its leaves are open.\n\n\
             Write each unproved sub-lemma into the skeleton file above as a fenced `gap` block \
             with `id`, `lemma`, `status` and `next` lines, so the statement graph carries it and \
             the run can pick it up on its own. A sub-lemma with no `next` a role could act on \
             today is a research request rather than a task — decompose further until each one \
             has one.\n\n\
             Call `lean_check` on the file whatever the outcome. A file that compiles with three \
             `sorry` in it is a recorded decomposition; a file nobody checked is nothing."
        }
    };
    let report = delegate(
        subagents,
        super::lean::LEAN_ROLE,
        format!(
            "{instruction}\n\nThis node was chosen by the statement graph rather than by \
             preference, so do not substitute a different one.\n\n{}\n\nProblem:\n{}",
            assignment.briefing(),
            state.problem()
        ),
    )
    .await;
    // Beside the report rather than instead of it, on the argument the
    // refutation arm makes: the verdicts say what the kernel established, and
    // the report says what the prover believes the Lean statement means — which
    // is the judgement no file records and the one place this arm can still be
    // wrong.
    let filed = super::lean::briefing(workspace);
    let merged = merge_context(&[
        ("What the kernel recorded", filed.as_str()),
        ("What the prover reports", report.as_str()),
    ]);
    vec![Finding::new(Slot::Verification, merged)]
}

/// Checks the literature *after* the run believes it is done.
///
/// Every other literature sweep in this runtime runs while the run is stuck, to
/// find a way forward. This one runs when the run thinks it has finished, and
/// it is asking the opposite question: has this already been done, and is the
/// argument too short for what it claims?
///
/// Tao's rule, and he states it about his own work: a proof that came out
/// surprisingly quickly is more likely to be wrong or already known than to be
/// a breakthrough, so the check after a solve is not optional politeness — it
/// is the step that separates a result from a rediscovery. Until this node
/// existed the runtime did the exact inverse: [`super::open_library`] returns
/// early when `state.solved`, so the one moment the literature is most worth
/// reading was the one moment nothing read it.
///
/// It cannot un-solve the run, and that is deliberate. What it produces is a
/// finding filed beside the answer, for the reader who has to decide whether to
/// believe it — a runtime that retracted its own verdict on a search result
/// would be trusting a web query over a verified program.
pub(in crate::orchestrator) async fn novelty_arm(
    subagents: &AsyncSubagentManager,
    workspace: Option<&Path>,
    state: &SolutionState,
) -> Vec<Finding> {
    if !state.solved {
        return Vec::new();
    }
    let established = workspace
        .map(|workspace| super::claims::collect(workspace).established())
        .unwrap_or_default();
    let report = delegate(
        subagents,
        "research",
        format!(
            "This run believes it has solved the problem below. Do not try to solve it. Find out \
             whether the result is already known, and whether the argument is strong enough for \
             what it claims.\n\n\
             Search for the statement itself, for the numbers the run produced, and for the named \
             theory it sits in. Report, with URLs: whether this result is published and by whom, \
             whether the method used here is the standard one, and anything the sources say that \
             contradicts what the run concluded.\n\n\
             Be blunt about the second question. A proof that arrived quickly is far more often \
             wrong or already known than it is new, and saying so late is worth nothing. If the \
             run reached this in {} attempt(s) on {established} established claim(s), say whether \
             that is plausible for a result of this size.\n\n\
             If it is already known, that is the finding, and it is a useful one: name the source \
             so the derivation can cite it. If you cannot find it, say that plainly rather than \
             padding the report — an unsuccessful search is evidence too.\n\nProblem:\n{}\n\n\
             What the run concluded:\n{}",
            state.attempts,
            state.problem(),
            state.last_attempt
        ),
    )
    .await;
    vec![Finding::new(Slot::Digest, report)]
}

/// The statements worth attacking, read off the two ledgers that hold them.
fn refutation_targets(workspace: Option<&Path>) -> String {
    let Some(workspace) = workspace else {
        return String::new();
    };
    let gaps = open_gap_briefing(Some(workspace));
    let rungs = super::weakened::collect(workspace).briefing();
    let sections: Vec<(&str, &str)> = vec![
        ("Open lemmas the run needs", gaps.as_str()),
        ("The weakened target currently being attacked", rungs.as_str()),
    ];
    let targets = merge_context(&sections);
    if targets.trim().is_empty() {
        // Deliberately not a heading with nothing under it. An arm told
        // "statements to attack:" followed by silence reasonably concludes
        // there are none, where the truth is that the ledgers have not been
        // written yet and the goal is the only statement there is.
        return String::new();
    }
    format!("Statements the run has committed to:\n{targets}")
}

/// The invention arm: propose, ground, converge.
pub(in crate::orchestrator) async fn diversify_invention_arm(
    subagents: &AsyncSubagentManager,
    workspace: Option<&Path>,
    state: &SolutionState,
) -> Vec<Finding> {
    let (grounding, chosen) = invention_arm(subagents, workspace, state).await;
    vec![
        Finding::new(Slot::Grounding, grounding),
        Finding::new(Slot::Chosen, chosen),
    ]
}

/// The barrier every arm converges on, and the only node that reads them all.
///
/// Reached once all three arms have arrived — that is what the waiting edges
/// registering them buy — so it can fold the slots into one briefing without
/// checking whether anything is still running.
pub(in crate::orchestrator) fn diversify_merge(mut state: SolutionState) -> SolutionState {
    // Merged rather than assigned: the reflection that routed here has already
    // put this attempt's pattern analysis, and possibly a literature rescue,
    // into the same field. Overwriting would throw away the findings that
    // motivated diversifying in the first place.
    let carried = state.fresh_context.clone();
    let findings = state.diversify.sections();
    let mut sections: Vec<(&str, &str)> = vec![("Carried forward", carried.as_str())];
    sections.extend(findings);
    state.fresh_context = merge_context(&sections);
    // Cleared so the next diversify starts from nothing rather than inheriting
    // this one's slots, which would let a stale arm's report be merged twice.
    state.diversify = DiversifyFindings::default();
    state.unproductive = 0;
    // Diversifying *is* the answer to a run that has only been scaling, so the
    // count that routed here is cleared with the other one. Leaving it set
    // would send the very next reflection straight back here.
    state.computational = 0;
    state
}

/// Runs the invention arm: propose, ground, converge.
///
/// The other two arms are errands — fetch this, analyse that — and finish in
/// one delegation. This one is three, in sequence, because the thing being
/// produced does not exist in either agent alone. The inventor knows the shape
/// of the problem and what has failed; research knows what is already named,
/// proved, and tried. An idea that is genuinely new *and* not already closed in
/// the literature is the intersection, and the intersection is only reachable
/// by passing the candidates across and back.
///
/// It ran as a single inventor call before, concurrent with the library arm and
/// blind to it. That produced a paragraph of prose, once, which was merged into
/// the next attempt's context and then lost — so an idea proposed at attempt
/// three could be proposed again at attempt six, and the literature check that
/// would have killed it never happened. The exchange writes to
/// `research/approaches/`, so the next round starts from what this one closed.
///
/// Three sequential children rather than one. The arm still runs beside the
/// library arm's two, so a diversify costs roughly one extra child run, not
/// three.
/// The approach files on disk, by name.
///
/// Used to check that a proposing turn wrote something, not to read what it
/// wrote — [`super::approaches::collect`] does that. A missing directory is an
/// empty set rather than an error, which is the ordinary state of a workspace
/// that has never reached a diversify.
fn approach_slugs(workspace: Option<&Path>) -> BTreeSet<OsString> {
    let Some(workspace) = workspace else {
        return BTreeSet::new();
    };
    let Ok(entries) = std::fs::read_dir(workspace.join(super::approaches::APPROACHES_DIR)) else {
        return BTreeSet::new();
    };
    entries
        .flatten()
        .filter(|entry| entry.path().is_file())
        .map(|entry| entry.file_name())
        .collect()
}

/// Re-issues the proposing turn once when it reported without writing.
///
/// The inventor's system prompt asks it to write each candidate to
/// `research/approaches/<slug>.md` *before* reporting, and the loop's prompt
/// asks again. A live Project Euler 597 run ignored both: five model calls and
/// nine tool calls, every one a read, and the three candidates left in a turn
/// that hit the output cap. Across three concurrent runs the directory had
/// never been created at all. A prompt instruction is not a control, which is
/// this repository's own rule; this is the control.
///
/// The comparison is by *name added*, not by count or mtime. Proposing means
/// new slugs, so a turn that rewrote an existing file without adding one has
/// not done what was asked, and mtime would call that a success.
///
/// Once, not until it complies. A second refusal means this turn is not going
/// to write, and the prose it did report is still worth carrying into the
/// attempt — losing that to a retry loop costs more than the missing files. So
/// the re-issue's reply is appended rather than substituted, and the caller
/// gets what the inventor said either way.
async fn ensure_approaches_written(
    subagents: &AsyncSubagentManager,
    workspace: Option<&Path>,
    before: &BTreeSet<OsString>,
    reported: String,
) -> String {
    if approach_slugs(workspace) != *before {
        return reported;
    }
    let retry = delegate(
        subagents,
        "inventor",
        format!(
            "You reported these candidates without writing them. Nothing was added to \
             `research/approaches/`, so nothing survives this turn: the next round has no record \
             of them and will spend itself proposing them again. Write each one now with \
             `write_document` to `research/approaches/<slug>.md`, as a fenced `approach` block \
             with `idea`, `mechanism`, `status: proposed`, and `first-step` lines. Do not revise \
             the mathematics, do not reconsider, and do not propose anything new — write down \
             what you already have, one file per candidate, then report the slugs you \
             wrote.\n\n\
             What you reported:\n{reported}"
        ),
    )
    .await;
    format!("{reported}\n\n{retry}")
}

/// What a reduction turn has to move for it to have done anything.
///
/// A missing directory is an empty set rather than an error, which is the
/// ordinary state of a workspace that has never been decomposed.
fn skeleton_fingerprint(
    workspace: Option<&Path>,
) -> BTreeSet<(String, String, super::backward::GapStance)> {
    let Some(workspace) = workspace else {
        return BTreeSet::new();
    };
    super::backward::collect(workspace).fingerprint()
}

/// Re-issues the reduction once when it reported without writing.
///
/// The same control [`ensure_approaches_written`] is, against the same failure
/// — a role that reports three candidates and leaves nothing on disk, so the
/// next round has no record and pays for them again — and once rather than
/// until it complies, for the same reason: a second refusal means this turn is
/// not going to write, and the prose it did report is worth more than a retry
/// loop.
///
/// The discriminator differs, and the difference is the point. Approaches are
/// compared by *name added*, because proposing means new files. That is wrong
/// here from the second cadence onward: refining a live skeleton — moving a gap
/// to `discharged`, adding a lemma the run now needs — is exactly the correct
/// work and adds no name. So this compares the fingerprint of every
/// (skeleton, gap, status) triple instead, which is strictly stronger: an
/// unchanged fingerprint means the turn changed nothing any downstream reader
/// consumes, whatever it did to the bytes, and mtime would call that a success.
///
/// A plain before-and-after comparison is sound in a runtime where everything
/// else is racing because `research/backward/` is written by exactly one role
/// and the reduction gate admits one of it at a time.
async fn ensure_skeleton_written(
    subagents: &AsyncSubagentManager,
    workspace: Option<&Path>,
    before: &BTreeSet<(String, String, super::backward::GapStance)>,
    reported: String,
) -> String {
    if skeleton_fingerprint(workspace) != *before {
        return reported;
    }
    let retry = delegate(
        subagents,
        "reducer",
        format!(
            "You reported a decomposition without writing it. Nothing under `research/backward/` \
             changed, so nothing survives this turn: the ledger has no record of these lemmas and \
             the next attempt will not be handed one of them to attack. Write it now with \
             `write_document` to `research/backward/<slug>.md`, as a fenced `skeleton` block with \
             `goal`, `implies`, `status`, and `rests-on` lines, followed by one fenced `gap` block \
             per missing lemma with `id`, `lemma`, `status`, and `next` lines. Do not revise the \
             mathematics, do not reconsider, and do not decompose anything further — write down \
             what you already have, then report the slug and the gap ids you wrote.\n\n\
             What you reported:\n{reported}"
        ),
    )
    .await;
    format!("{reported}\n\n{retry}")
}

/// Decomposes the goal and reports the gaps that are still open.
///
/// One delegation, where [`invention_arm`] is three. The inventor's output has
/// to be checked against the literature before it is worth adopting, and only
/// research can do that; a skeleton is checked by the forward loop attacking
/// its gaps, which is the loop itself and costs no child run here.
///
/// What travels back is read off disk rather than taken from the reply. The
/// reducer's prose is a summary of its own work, and the ledger is the record —
/// the same argument the dossier is built on. It also means a turn that wrote
/// good files and then produced a truncated report still delivers its gaps.
async fn reduction_arm(
    subagents: &AsyncSubagentManager,
    workspace: Option<&Path>,
    state: &SolutionState,
) -> String {
    let dossier = workspace.map(super::dossier::reducer).unwrap_or_default();
    let before = skeleton_fingerprint(workspace);
    let reported = delegate(
        subagents,
        "reducer",
        format!(
            "Work backward from this problem's goal and write down what would suffice to prove \
             it. Not another route to it — the lemmas that, if somebody had them, would give it, \
             and the inference that combines them. Write the result to \
             `research/backward/<slug>.md` as a fenced `skeleton` block with `goal`, `implies`, \
             `status`, and `rests-on` lines, followed by one fenced `gap` block per missing lemma \
             with `id`, `lemma`, `status`, and `next` lines.\n\n\
             Check each lemma against `research/CLAIMS.md` and `search_claims` before you call it \
             a gap: a decomposition into three statements two of which the run has already proved \
             is nearly a proof, and finding that is the cheapest result available to you. Mark \
             those `discharged` with the claim id. Every gap you leave open needs a `next` a \
             tool_builder could run today or a theorem_prover could be handed today — a lemma \
             with no first move is a research request, not a task.\n\n\
             Report the slug, the gaps you left open, and which lemma you would attack \
             first.\n\nProblem:\n{}\n\n{}\n\n{dossier}",
            state.problem(),
            state.lesson_briefing()
        ),
    )
    .await;
    let reported = ensure_skeleton_written(subagents, workspace, &before, reported).await;
    let gaps = open_gap_briefing(workspace);
    // The graph, beside the flat list, because the two answer different
    // questions and the second one is the one that schedules work. The gap
    // list says what is unproved; the blueprint says which of it rests on
    // nothing still open, and is therefore the part somebody can start on
    // without holding the rest of the argument in their head. It also carries
    // the one fault a per-file ledger cannot show — a reduction that proves
    // its own hypothesis — and that has to reach the attempt before the
    // attempt spends itself inside the loop.
    let graph = workspace
        .map(|workspace| super::blueprint::collect(workspace).briefing())
        .unwrap_or_default();
    merge_context(&[
        ("What the run says would suffice", &reported),
        ("Open gaps, read from the ledger", &gaps),
        ("The statement graph: what is ready, and what is circular", &graph),
    ])
}

/// The ladder as it stands, so a turn that changed nothing can be told so.
///
/// A fingerprint of `(ladder, rung, stance)` triples rather than a set of
/// filenames, and the discriminator is inverted from the approach ledger's for
/// the reason `ensure_skeleton_written` records: proposing means new files, but
/// *refining* a live ladder — settling a rung, marking one failed, adding the
/// next one up — is exactly the correct work from the second cadence onward and
/// adds no name.
fn ladder_fingerprint(
    workspace: Option<&Path>,
) -> BTreeSet<(String, String, super::weakened::RungStance)> {
    workspace
        .map(|workspace| super::weakened::collect(workspace).fingerprint())
        .unwrap_or_default()
}

/// Re-issues once when the weakener reported a ladder it did not write.
///
/// The same control `ensure_skeleton_written` is, against the same measured
/// failure: a live inventor ignored both its system prompt and its arm prompt
/// and left its candidates in a turn that hit the output cap, and across three
/// concurrent runs the ledger directory had never been created. A prompt
/// instruction is not a control.
///
/// Re-issued once rather than until compliance. A second refusal means this
/// turn is not going to write, and the prose it did report is still worth
/// carrying into the attempt — so the reply is appended to it rather than
/// replacing it.
async fn ensure_ladder_written(
    subagents: &AsyncSubagentManager,
    workspace: Option<&Path>,
    before: &BTreeSet<(String, String, super::weakened::RungStance)>,
    reported: String,
) -> String {
    if ladder_fingerprint(workspace) != *before {
        return reported;
    }
    let retry = delegate(
        subagents,
        "weakener",
        format!(
            "You reported a ladder without writing it. Nothing under `research/weakened/` \
             changed, so nothing survives this turn: no rung reaches the next attempt and the \
             difficulties you named are lost with your context. Write it now with \
             `write_document` to `research/weakened/<slug>.md`, as a fenced `ladder` block with \
             `goal`, `difficulties`, and `status` lines, followed by one fenced `rung` block per \
             weakened target with `id`, `statement`, `off`, `stance`, and `merge` lines. Do not \
             revise the mathematics and do not add rungs — write down what you already have, then \
             report the slug and the rung ids you wrote.\n\n\
             What you reported:\n{reported}"
        ),
    )
    .await;
    format!("{reported}\n\n{retry}")
}

/// Lowers the goal and reports the rung the run should attack next.
///
/// Shaped exactly as [`reduction_arm`] is, and running beside it, because the
/// two answer the same *kind* of question — what should the run attack instead
/// of the goal as stated — and differ only in the direction of the answer. The
/// reducer breaks the goal into lemmas that would imply it; this breaks it into
/// targets that deliberately would not.
///
/// It is deliberately *not* gated on the run being stuck, and that is a lesson
/// this repository already paid for once. `open_invention`'s stuck-gate was
/// reachable in principle and not in practice — a diversify needs two
/// consecutive unproductive attempts, which needs two completed cycles, and a
/// run whose attempts take the better part of an hour spends its whole clock
/// inside the first one. Across a day of live runs the inventor was spawned
/// once. A ladder is most useful before the run has burned its budget on the
/// full-strength statement, not after.
async fn weakening_arm(
    subagents: &AsyncSubagentManager,
    workspace: Option<&Path>,
    state: &SolutionState,
) -> String {
    let before = ladder_fingerprint(workspace);
    let reported = delegate(
        subagents,
        "weakener",
        format!(
            "Name the difficulties that make this problem hard, then build the ladder of weakened \
             versions of it. Not another route to the goal and not the lemmas that would imply \
             it — smaller problems, each one the goal with named difficulties switched off. Write \
             the result to `research/weakened/<slug>.md` as a fenced `ladder` block with `goal`, \
             `difficulties`, and `status` lines, followed by one fenced `rung` block per weakened \
             target with `id`, `statement`, `off`, `stance`, and `merge` lines.\n\n\
             The bottom rung should be one an attempt could settle today — small n, one case, \
             every convenience assumed. Check `research/CLAIMS.md` and `search_claims` before you \
             call a rung open: a rung the run has already established is `settled`, and noticing \
             that is the cheapest result available to you. A rung that was attacked and failed \
             stays on the ladder with the reason, because deleting it is how the same one gets \
             proposed again three attempts later.\n\n\
             Report the slug, the rung you would attack next, and which difficulty you expect to \
             be the one that actually bites.\n\nProblem:\n{}\n\n{}",
            state.problem(),
            state.lesson_briefing()
        ),
    )
    .await;
    let reported = ensure_ladder_written(subagents, workspace, &before, reported).await;
    let ladder = workspace
        .map(|workspace| super::weakened::collect(workspace).briefing())
        .unwrap_or_default();
    merge_context(&[
        ("What the run says would be easier", &reported),
        ("The ladder, read from the ledger", &ladder),
    ])
}

/// Renders the open gaps on disk for the next attempt.
///
/// Empty when nothing is open, so [`Mailbox::post`] drops it rather than
/// leaving the attempt a heading with nothing under it.
fn open_gap_briefing(workspace: Option<&Path>) -> String {
    let Some(workspace) = workspace else {
        return String::new();
    };
    let skeletons = super::backward::collect(workspace);
    let gaps = skeletons.open_gaps();
    if gaps.is_empty() {
        return String::new();
    }
    gaps.iter()
        .map(|gap| gap.briefing())
        .collect::<Vec<_>>()
        .join("\n")
}

async fn invention_arm(
    subagents: &AsyncSubagentManager,
    workspace: Option<&Path>,
    state: &SolutionState,
) -> (String, String) {
    // Read from disk now rather than from the prompt loaded at startup. On a
    // twelve-hour conjecture run this is the difference between the inventor
    // seeing the work and seeing the empty workspace it began with.
    let dossier = workspace.map(super::dossier::inventor).unwrap_or_default();
    // Sampled before the delegation, so what the turn added is what is
    // compared. Reading it afterwards would compare against a directory the
    // turn had already changed.
    let before = approach_slugs(workspace);
    let candidates = delegate(
        subagents,
        "inventor",
        format!(
            "Propose three genuinely different lines of attack, and write each one to \
             `research/approaches/<slug>.md` as a fenced `approach` block with `idea`, \
             `mechanism`, `status: proposed`, and `first-step` lines. The approaches tried so far \
             have not worked; do not restate them, and do not re-propose anything the record \
             below already closed. Diverge: three variations on one idea are worth less here than \
             three ideas, and a proposal you are unsure of is worth more than a safe one, because \
             research is about to check all three. Name the actual mathematics in each — a \
             transform, a bijection, an invariant, a named theorem — rather than describing a \
             direction. Report the three slugs and what each one is.\n\n\
             Problem:\n{}\n\n{}\n\n{dossier}",
            state.problem,
            state.lesson_briefing()
        ),
    )
    .await;
    let candidates = ensure_approaches_written(subagents, workspace, &before, candidates).await;
    let grounding = delegate(
        subagents,
        "research",
        format!(
            "The inventor has proposed these lines of attack for the problem below. Take each one \
             to the literature and report, per candidate: what the reformulation is actually \
             called, the precise statement of any theorem it relies on and whether its hypotheses \
             hold here, whether anyone has applied it to this problem, and what it would buy. \
             Then update that candidate's file under `research/approaches/`: fill `precedent` \
             with the source URLs and claim ids you found, and set `status` to `grounded` when \
             the literature supports it or `refuted` with a `killed-by` line when it does not. \
             Refuting one is as useful as backing one — it is what stops the next round \
             proposing it again — but refute on evidence, not on absence: say plainly when you \
             simply could not find anything.\n\n\
             Candidates:\n{candidates}\n\nProblem:\n{}\n\n{dossier}",
            state.problem
        ),
    )
    .await;
    let chosen = delegate(
        subagents,
        "inventor",
        format!(
            "Research has checked your candidates against the literature. Decide. Either adopt \
             the one that now looks best, or — if what research turned up suggests something \
             neither of you named — propose that instead, which is the better outcome when it is \
             available: the combination of your reformulation and what the literature actually \
             says is where a new line of attack usually comes from. Write the choice to its file \
             with `status: adopted` and a `first-step` a tool_builder could start on today, and \
             set the others to `refuted` with a `killed-by` line each. Report the adopted \
             approach, why it beat the others, and its first concrete step.\n\n\
             Your candidates:\n{candidates}\n\nWhat research found:\n{grounding}\n\n\
             Problem:\n{}",
            state.problem
        ),
    )
    .await;
    (grounding, chosen)
}
