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
    merge_context(&[
        ("What the run says would suffice", &reported),
        ("Open gaps, read from the ledger", &gaps),
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
