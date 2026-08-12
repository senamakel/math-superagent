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

/// Runs three arms concurrently to break a stalled loop.
///
/// Two are gathering: the library arm fetches and reads, the pattern arm looks
/// at the numbers already computed. The third is invention, and unlike the
/// other two it is a conversation rather than an errand — see
/// [`invention_arm`]. The three do not read each other, which is what lets them
/// run at once.
async fn diversify_step(
    subagents: &AsyncSubagentManager,
    tracer: Option<&Arc<RunTracer>>,
    workspace: Option<&Path>,
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
    let invention = invention_arm(subagents, workspace, &state);
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
    let ((library, digest), patterns, (grounding, chosen)) =
        tokio::join!(reading, patterns, invention);

    // Merged rather than assigned: the reflection that routed here has already
    // put this attempt's pattern analysis, and possibly a literature rescue,
    // into the same field. Overwriting would throw away the findings that
    // motivated diversifying in the first place.
    state.fresh_context = merge_context(&[
        ("Carried forward", &state.fresh_context.clone()),
        ("Reference material", &library),
        ("What the sources establish", &digest),
        ("Structural observations", &patterns),
        ("What the literature says about the candidates", &grounding),
        ("Line of attack chosen", &chosen),
    ]);
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
