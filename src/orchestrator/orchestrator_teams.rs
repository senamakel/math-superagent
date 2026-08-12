/// The teams that run beside the solve, each with the brief it wakes up to.
///
/// Lifted out of [`OrchestratorAgent::spawn_support_teams`] so the briefs — the
/// longest text in this file and the part most often edited — are not wedged
/// inside the spawning logic that reads them.
fn standing_teams() -> [(
    &'static str,
    &'static str,
    teams::Completion,
    teams::TeamBudget,
    &'static str,
); 4] {
    [
        (
            "director",
            "director",
            teams::Completion::Standing,
            teams::TeamBudget::attentive(),
            "Carry out what the operator running this investigation has just asked for. Their \
             directive is below, and it is the one input this run gets that nothing else can \
             reconstruct: everything else you could read is the run's own account of its own \
             work, while this is a person who can see the whole run saying where it should go. \
             Treat it as an instruction, not as evidence — it is asserted rather than \
             established, so do not file it as a claim.\n\
             The next attempt is already given the directive verbatim, so do not simply restate \
             it. Your job is the part that reaches everything the prompt does not: read the \
             workspace, work out what the directive means for the work in flight, and change the \
             files that carry it. Rewrite TASKS.md so the order of work reflects what was asked. \
             Amend CONTEXT.md when the directive changes what every role should know, staying \
             inside its budget. Open a thread under research/threads/ for a direction it starts, \
             mark one dead that it abandons, and file a request_research for a gap it names. \
             Prefer editing what is already there to adding beside it.\n\
             Do not compute, do not write or run programs, and do not answer the mathematics \
             yourself — the roles that can execute are already doing that, and a second opinion \
             from you would arrive as an instruction rather than a result. If a directive asks \
             for something the run has already established is wrong, say so in your reply rather \
             than quietly obeying or quietly ignoring it; your reply is written to the ledger the \
             operator reads. Report in two or three sentences what you changed and why. Change \
             nothing you cannot justify from the directive itself.",
        ),
        (
            "research",
            "librarian",
            teams::Completion::Standing,
            teams::TeamBudget::acquiring(),
            "Build this run's reference library, and keep building it. A run cannot use what \
                 it has no source for, and the failure this team exists to prevent is not an \
                 over-full library — it is a run reasoning from what the model remembers \
                 instead of from what it can read. A live Erdős–Gyárfás workspace cited \
                 Wikipedia and Wolfram MathWorld in three notes with neither on disk, and a \
                 live Project Euler run invented plausible arXiv identifiers and filed \
                 unrelated papers under the names it wanted them to have. Both are what an \
                 empty library looks like from the inside.\n\
                 Search first and search widely. `exa_search` is the strongest instrument \
                 here and the one most often left unused: a query costs a fraction of a \
                 download and tells you what exists, what it is called, and who wrote it, \
                 which is what turns a guess at a URL into a citation. Never download a URL \
                 you have not seen in a search result, in `research/FRONTIER.md`, or in a \
                 source you already hold — a fetch of an invented address succeeds and \
                 stores the wrong paper.\n\
                 Cover the subject rather than one thread of it. Each cycle, pick the angle \
                 the library is thinnest on: the encyclopedic and problem-collection entries \
                 that fix the statement and the names, the surveys, the methods that failed \
                 and why, the adjacent problems, the computational attacks, the \
                 counterexample constructions, and whatever the run's own sources cite. \
                 `research/FRONTIER.md` is ranked by how many of your own sources cite each \
                 target; work the top of it, because a source three of your papers cite is \
                 the standard reference and no rephrasing of a query surfaces that.\n\
                 Two things still bound you, and they are about waste rather than volume. \
                 Use `recall_memory` before fetching so known material is not fetched twice, \
                 and prefer the primary statement to a retelling of it. When a cycle genuinely \
                 has nothing to add — every angle covered, the frontier worked, no request \
                 open — say NOTHING FURTHER and spend nothing; you will be asked again, so \
                 that is a pause and not a retirement. File what you gather under `research/`, \
                 describe it, and store the verified finding with `remember_memory` so later \
                 runs can recall it."
        ),
        (
            "patterns",
            "pattern_finder",
            teams::Completion::Standing,
            teams::TeamBudget::custodial(),
            "Look for exploitable structure in the results this run has already computed.                  Read what is on disk, extract the integer sequences in it, and run the                  sequence tools over them. Where a check needs terms the run has not                  computed, write and run the program yourself or commission it — a                  conjecture tested only on the data that suggested it is untested. Report                  only regularities that hold exactly over every term supplied, say plainly                  that they are conjectures, and give the first term that would falsify                  each. An invented pattern costs the run more than no pattern, so when the                  results have not changed since you last looked, or hold too few terms to                  say anything exact, reply NOTHING FURTHER rather than reaching. Record                  provisional work with note_scratch; after it survives an attempt to break                  it, store the verified finding with remember_memory.",
        ),
        (
            "context",
            "context_curator",
            teams::Completion::Standing,
            teams::TeamBudget::paced(shared_context::cycle_interval()),
            "Keep CONTEXT.md current with what this run and durable memory now establish. \
             It is sent to nearly every role on every model call, so it is the cheapest way \
             for the run to know something and the most expensive place to be wrong or \
             verbose. Carry what an agent would otherwise rebuild from disk: the established \
             results with their basis, the approaches that failed and why, what the computed \
             numbers look like, and what recall_memory and relate_memory hold about this \
             problem from earlier runs. Cut what the run has since disproved, and link the \
             file that still holds any detail you compress away. Your brief below states what \
             the file currently costs against its budget; when it is over, this cycle is a \
             compression and nothing else. When nothing has changed that would change what an \
             agent should know, reply NOTHING FURTHER — a brief that says the same thing in \
             more words has made every role in the run pay more for the same knowledge.",
        ),
    ]
}

/// Folders holding what a program produced, which is what the pattern agent
/// analyses.
///
/// Only what programs produced, and never the team's own notes: it writes
/// those itself, so treating them as new input would make every cycle look
/// like it had something fresh to read — the team would wake itself up forever
/// on its own notes. That is now free rather than arranged, because its scratch
/// went to `note_scratch` and is no longer a file in the workspace at all.
///
/// `code/out` sits inside `code`, so it is walked twice. That is deliberate
/// rather than an oversight: [`teams::fingerprint`] stops after a fixed number
/// of files, and naming the output folder separately gives it a budget of its
/// own. Without that, a `code/` grown past the cap could hide every result the
/// team exists to read behind the programs that produced them. Hashing the same
/// bytes twice is free and changes nothing about the comparison.
const RESULT_FOLDERS: [&str; 2] = ["code/out", "code"];

/// Reads a team's last-seen fingerprint, recovering a poisoned lock.
///
/// A poisoned lock means some thread panicked while holding it, not that the
/// value inside is unusable — it is one `Option<u64>`, written under the guard
/// with nothing between that can fail. Treating the poison as "unknown" is what
/// costs something: the caller read it as *changed*, so the team ran, and
/// because the same read is what stores the new fingerprint, it stayed changed.
/// One panic anywhere would have turned an idle gate into a model call every
/// cycle for the rest of the run — the exact expense the gate exists to avoid.
fn last_seen(
    analysed: &Arc<std::sync::Mutex<Option<u64>>>,
) -> std::sync::MutexGuard<'_, Option<u64>> {
    analysed
        .lock()
        .unwrap_or_else(std::sync::PoisonError::into_inner)
}

/// Whether an operator has queued anything for the run to act on.
///
/// Returns the cycle outcome to report when they have not, and `None` when they
/// have — the same shape as the fingerprint gates beside it, and for the same
/// reason. This is the check that keeps a team which wakes every twenty seconds
/// from costing anything: an empty queue is one file read, and no model is
/// asked whether it has been given work.
///
/// A queue that cannot be read is treated as empty. The alternative is a run
/// that starts a model call every twenty seconds because a file is unreadable,
/// and the operator would see a run spending its budget on nothing rather than
/// a run quietly not being directed.
fn directives_waiting(workspace: &Path) -> Option<teams::Cycle> {
    match directives::pending(workspace) {
        Ok(waiting) if waiting.is_empty() => Some(teams::Cycle::Idle),
        Ok(_) => None,
        Err(_) => Some(teams::Cycle::Idle),
    }
}

/// Consumes what the operator has queued and hands it to the loop verbatim.
///
/// Two deliveries come out of one read, and they are deliberately unequal. The
/// text goes to the mailbox exactly as typed, which is what the next attempt is
/// briefed with; the director agent gets the same text to act on, and may fail
/// without costing the first delivery anything.
fn take_directives(
    workspace: &Path,
    mailbox: &solutions::Mailbox,
    tracer: &Arc<RunTracer>,
) -> Vec<crate::Directive> {
    let taken = match directives::drain(workspace) {
        Ok(taken) => taken,
        Err(error) => {
            tracer.note(&format!("directive queue unreadable: {error}"));
            return Vec::new();
        }
    };
    for directive in &taken {
        tracer.note(&format!(
            "directive {} from {}: {}",
            directive.id, directive.from, directive.text
        ));
        mailbox.post(directive.text.clone());
    }
    taken
}

/// Whether the run's computed results are the same as last time this looked.
///
/// Returns the cycle outcome to report when there is nothing new, and `None`
/// when there is. The comparison is by fingerprint — path, size and
/// modification time — so it costs a directory walk rather than a model call,
/// which is the whole point: a team that has to *ask* whether anything changed
/// has already spent most of what a working cycle costs.
///
/// A workspace with no results at all reads as unchanged, so an early cycle on
/// a run that has computed nothing idles instead of analysing an empty folder.
fn results_unchanged(
    workspace: &Path,
    analysed: &Arc<std::sync::Mutex<Option<u64>>>,
) -> Option<teams::Cycle> {
    let mut hasher = std::collections::hash_map::DefaultHasher::new();
    let mut any = false;
    for folder in RESULT_FOLDERS {
        let path = workspace.join(folder);
        if path.is_dir() {
            any = true;
            std::hash::Hash::hash(&teams::fingerprint(&path), &mut hasher);
        }
    }
    if !any {
        return Some(teams::Cycle::Idle);
    }
    let current = std::hash::Hasher::finish(&hasher);
    let mut seen = last_seen(analysed);
    if *seen == Some(current) {
        return Some(teams::Cycle::Idle);
    }
    *seen = Some(current);
    None
}

/// Whether the workspace is the same as last time this team looked, ignoring
/// the files the team writes itself.
///
/// The same argument as [`results_unchanged`] one folder wider: deciding to
/// idle has to cost a directory walk rather than a model call, or the cheap
/// case — nothing has changed — costs most of what a working cycle costs. The
/// exclusions are what stop a team that writes into the tree it watches waking
/// itself forever on its own output.
fn workspace_unchanged(
    workspace: &Path,
    analysed: &Arc<std::sync::Mutex<Option<u64>>>,
    excluded: &[&str],
) -> Option<teams::Cycle> {
    let current = teams::fingerprint_excluding(workspace, excluded);
    let mut seen = last_seen(analysed);
    if *seen == Some(current) {
        return Some(teams::Cycle::Idle);
    }
    *seen = Some(current);
    None
}
