#![allow(clippy::expect_used)]


use super::{LadderStance, RungStance, collect, is_weakened};

fn ladder(root: &std::path::Path, slug: &str, body: &str) -> std::io::Result<()> {
    std::fs::write(
        root.join(format!("{}/{slug}.md", super::WEAKENED_DIR)),
        format!("# {slug}\n\n{body}\n\nWorking notes.\n"),
    )
}

/// A ladder block and its rung blocks, in the shape the prompt asks for.
fn rungs(header: &str, blocks: &[&str]) -> String {
    let mut out = format!("```ladder\n{header}\n```\n");
    for block in blocks {
        let _ = write!(out, "\n```rung\n{block}\n```\n");
    }
    out
}

fn workspace(name: &str) -> std::io::Result<std::path::PathBuf> {
    let root = std::env::temp_dir().join(format!("math-agent-weakened-{name}"));
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(root.join(super::WEAKENED_DIR))?;
    Ok(root)
}

/// A three-difficulty header with three rungs turning them off one at a time,
/// which is the shape the whole ledger is built around.
fn erdos_ladder() -> String {
    rungs(
        "goal: every graph with n vertices and n+k edges has a cycle of length divisible by 3\n\
         difficulties: unbounded k, arbitrary minimum degree, no girth assumption\n\
         status: open",
        &[
            "id: R-0\n\
             statement: the bound holds for k = 1 on 3-regular graphs of girth at least 5\n\
             off: unbounded k, arbitrary minimum degree, no girth assumption\n\
             status: settled\n\
             settled-by: claim-base-case\n\
             merge: drop the girth hypothesis and re-run the counting argument",
            "id: R-1\n\
             statement: the bound holds for k = 1 on 3-regular graphs\n\
             off: unbounded k, arbitrary minimum degree\n\
             status: open\n\
             merge: allow degree 4 and check the discharging step still closes",
            "id: R-2\n\
             statement: the bound holds for k = 1\n\
             off: unbounded k\n\
             status: open\n\
             merge: induct on k once the k = 1 case is unconditional",
        ],
    )
}

/// The header, the difficulties, and every rung reach the table.
#[test]
fn a_full_ladder_becomes_a_header_row_and_a_rung_per_weakening() -> std::io::Result<()> {
    let root = workspace("full")?;
    ladder(&root, "cycle-length", &erdos_ladder())?;

    let ladders = collect(&root);
    let rendered = ladders.render();
    assert!(rendered.contains("| [[cycle-length]] |"));
    assert!(rendered.contains("cycle of length divisible by 3"));
    assert!(rendered.contains("arbitrary minimum degree"));
    assert!(rendered.contains("## The rungs, weakest first"));
    assert!(rendered.contains("| `R-0` |"));
    assert!(rendered.contains("| `R-1` |"));
    assert!(rendered.contains("| `R-2` |"));
    // Two of the three are unproved, and both are offered as work.
    assert_eq!(ladders.open_rungs().len(), 2);
    assert!(!rendered.contains("## Ladders that could not be read"));
    Ok(())
}

/// Weakest first is the order they are meant to be climbed, so it is the order
/// they are rendered in — whatever order the file wrote them.
#[test]
fn rungs_are_ordered_weakest_first() -> std::io::Result<()> {
    let root = workspace("order")?;
    ladder(
        &root,
        "reversed",
        &rungs(
            "goal: G\ndifficulties: a, b, c",
            &[
                "id: R-strong\nstatement: G with a off\noff: a\nstatus: open\nmerge: turn a on",
                "id: R-weak\n\
                 statement: G with a, b and c off\n\
                 off: a, b, c\n\
                 status: open\n\
                 merge: turn c on",
                "id: R-middle\nstatement: G with a and b off\noff: a, b\nstatus: open\nmerge: turn b on",
            ],
        ),
    )?;
    let ladders = collect(&root);
    let ids: Vec<&str> = ladders
        .open_rungs()
        .iter()
        .map(|rung| rung.id.as_str())
        .collect();
    assert_eq!(ids, vec!["R-weak", "R-middle", "R-strong"]);

    let rendered = ladders.render();
    let weak = rendered.find("`R-weak`").expect("the weakest rung is listed");
    let middle = rendered
        .find("`R-middle`")
        .expect("the middle rung is listed");
    let strong = rendered
        .find("`R-strong`")
        .expect("the strongest rung is listed");
    assert!(weak < middle, "weakest rung renders before the middle one");
    assert!(middle < strong, "middle rung renders before the strongest");
    Ok(())
}

/// The single fact the next attempt needs. Aiming three rungs up fails for the
/// same reason the full-strength goal does.
#[test]
fn the_current_rung_is_the_weakest_one_still_open() -> std::io::Result<()> {
    let root = workspace("current")?;
    ladder(&root, "cycle-length", &erdos_ladder())?;
    let ladders = collect(&root);
    let rendered = ladders.render();
    assert!(rendered.contains("## The current rung — attack this one"));
    // R-0 is settled, so the weakest still open is R-1 and not R-2.
    assert!(rendered.contains("[[cycle-length]] → `R-1`"));
    assert!(!rendered.contains("[[cycle-length]] → `R-2`"));
    assert!(rendered.contains("allow degree 4 and check the discharging step"));
    Ok(())
}

/// The rung and the header disagreeing about what makes the goal hard means the
/// rungs stop being weakenings of the stated goal.
#[test]
fn a_rung_naming_an_undeclared_difficulty_is_reported() -> std::io::Result<()> {
    let root = workspace("undeclared")?;
    ladder(
        &root,
        "drifted",
        &rungs(
            "goal: G\ndifficulties: unbounded k, arbitrary degree",
            &["id: R-1\n\
               statement: G for planar graphs\n\
               off: unbounded k, planarity\n\
               status: open\n\
               merge: drop planarity"],
        ),
    )?;
    let rendered = collect(&root).render();
    assert!(rendered.contains("## Ladders that could not be read"));
    assert!(rendered.contains("rung `R-1` switches off `planarity`"));
    assert!(rendered.contains("never declared as a difficulty"));
    Ok(())
}

/// A declared difficulty written back in a different case is the same
/// difficulty, not a disagreement.
#[test]
fn a_difficulty_matches_its_declaration_regardless_of_case() -> std::io::Result<()> {
    let root = workspace("case")?;
    ladder(
        &root,
        "cased",
        &rungs(
            "goal: G\ndifficulties: Unbounded K, Arbitrary Degree",
            &["id: R-1\n\
               statement: G for bounded k\n\
               off: unbounded k\n\
               status: open\n\
               merge: induct on k"],
        ),
    )?;
    let rendered = collect(&root).render();
    assert!(!rendered.contains("never declared as a difficulty"));
    Ok(())
}

/// A weakened version that did not work is information about the difficulty it
/// left on, and a rung deleted from the file is a rung somebody proposes again.
#[test]
fn a_failed_rung_keeps_its_reason() -> std::io::Result<()> {
    let root = workspace("failed")?;
    ladder(
        &root,
        "counting",
        &rungs(
            "goal: G\ndifficulties: unbounded k, no girth assumption",
            &["id: R-count\n\
               statement: G for girth at least 5\n\
               off: no girth assumption\n\
               status: failed\n\
               failed-by: the counting argument needs girth 6 and the extra edge case is real\n\
               merge: drop girth entirely"],
        ),
    )?;
    let rendered = collect(&root).render();
    assert!(rendered.contains("## Rungs that failed, and why"));
    assert!(rendered.contains("needs girth 6 and the extra edge case is real"));
    // A failed rung is not handed to the next attempt as the current one, and
    // a ladder left with nothing open and nothing reached says so.
    assert!(!rendered.contains("→ `R-count`"));
    assert!(rendered.contains("[[counting]] has no open rung"));
    assert!(collect(&root).open_rungs().is_empty());
    assert!(collect(&root).briefing().is_empty());
    Ok(())
}

/// A failed rung with no reason cannot stop a re-proposal, so the ledger says
/// so rather than presenting it as informative.
#[test]
fn a_failed_rung_without_a_reason_is_called_out() -> std::io::Result<()> {
    let root = workspace("reasonless")?;
    ladder(
        &root,
        "silent",
        &rungs(
            "goal: G\ndifficulties: a",
            &["id: R-1\nstatement: G with a off\noff: a\nstatus: failed\nmerge: turn a on"],
        ),
    )?;
    let rendered = collect(&root).render();
    assert!(rendered.contains("no reason recorded"));
    Ok(())
}

/// A settled rung quoted without the hypotheses it assumed reads as a proof of
/// the goal, which is the misreading most likely to reach a write-up.
#[test]
fn a_settled_rung_records_what_was_switched_off_when_it_landed() -> std::io::Result<()> {
    let root = workspace("settled")?;
    ladder(&root, "cycle-length", &erdos_ladder())?;
    let ladders = collect(&root);
    let banked: Vec<&str> = ladders.settled().map(|rung| rung.id.as_str()).collect();
    assert_eq!(banked, vec!["R-0"]);

    let rendered = ladders.render();
    assert!(rendered.contains("## Settled — what this run owns"));
    assert!(rendered.contains("off: unbounded k, arbitrary minimum degree, no girth assumption"));
    assert!(rendered.contains("established by claim-base-case"));
    Ok(())
}

/// An abandoned ladder's rungs buy the run nothing, so none of them is offered
/// as a target.
#[test]
fn an_abandoned_ladder_offers_no_rungs_to_attack() -> std::io::Result<()> {
    let root = workspace("abandoned")?;
    ladder(
        &root,
        "dead-end",
        &rungs(
            "goal: G\ndifficulties: a, b\nstatus: abandoned",
            &["id: R-1\nstatement: G with a and b off\noff: a, b\nstatus: open\nmerge: turn b on"],
        ),
    )?;
    let ladders = collect(&root);
    assert!(ladders.open_rungs().is_empty());
    assert!(ladders.briefing().is_empty());
    assert!(!ladders.render().contains("## The current rung"));
    Ok(())
}

/// A ladder marked exhausted stops being worked, so one marked exhausted by
/// mistake silently retires every rung nobody proved.
#[test]
fn an_exhausted_ladder_with_an_open_rung_is_contradictory() -> std::io::Result<()> {
    let root = workspace("contradiction")?;
    ladder(
        &root,
        "premature",
        &rungs(
            "goal: G\ndifficulties: a, b\nstatus: exhausted",
            &[
                "id: R-1\n\
                 statement: G with a and b off\n\
                 off: a, b\n\
                 status: settled\n\
                 settled-by: claim-1\n\
                 merge: turn b on",
                "id: R-2\nstatement: G with a off\noff: a\nstatus: open\nmerge: turn a on",
            ],
        ),
    )?;
    let rendered = collect(&root).render();
    assert!(rendered.contains("## Exhausted while a rung is open"));
    assert!(rendered.contains("[[premature]] is marked exhausted while 1 of its rungs"));
    Ok(())
}

/// The value of a weakened version is entirely in what it teaches about the
/// version above it, so a rung that does not say how to climb is called out.
#[test]
fn a_current_rung_with_no_merge_step_is_called_out() -> std::io::Result<()> {
    let root = workspace("mergeless")?;
    ladder(
        &root,
        "flat",
        &rungs(
            "goal: G\ndifficulties: a, b",
            &["id: R-1\nstatement: G with a and b off\noff: a, b\nstatus: open"],
        ),
    )?;
    let rendered = collect(&root).render();
    assert!(rendered.contains("does not say how to climb off it"));
    Ok(())
}

/// Faults for the shapes that cannot be used: no goal, no difficulties, no
/// block, no rungs, and a rung that cannot be tracked between two writes.
#[test]
fn the_unusable_shapes_are_each_named() -> std::io::Result<()> {
    let root = workspace("faults")?;
    let rung = "id: R-1\nstatement: G with a off\noff: a\nstatus: open\nmerge: turn a on";
    ladder(
        &root,
        "goalless",
        &rungs("difficulties: a, b", &[rung]),
    )?;
    ladder(
        &root,
        "featureless",
        &rungs("goal: G", &["id: R-1\nstatement: G, easier\nstatus: open\nmerge: harden it"]),
    )?;
    ladder(&root, "prose", "Just a paragraph, no block at all.\n")?;
    ladder(
        &root,
        "rungless",
        "```ladder\ngoal: G\ndifficulties: a, b\nstatus: open\n```\n",
    )?;
    ladder(
        &root,
        "anonymous",
        &rungs("goal: G\ndifficulties: a", &["statement: G with a off\noff: a\nstatus: open"]),
    )?;
    ladder(
        &root,
        "statementless",
        &rungs("goal: G\ndifficulties: a", &["id: R-1\noff: a\nstatus: open"]),
    )?;
    ladder(&root, "unclosed", "```ladder\ngoal: G\ndifficulties: a\n")?;

    let rendered = collect(&root).render();
    assert!(rendered.contains("`goalless` names no full-strength goal"));
    assert!(rendered.contains("`featureless` names no difficulties"));
    assert!(rendered.contains("`prose` has no ladder block"));
    assert!(rendered.contains("`rungless` has no rungs"));
    assert!(rendered.contains("`anonymous` has a rung with no id"));
    assert!(rendered.contains("`statementless` rung `R-1` states no weakened target"));
    assert!(rendered.contains("`unclosed` has a ladder block that was never closed"));
    Ok(())
}

/// An empty ledger says how to start one rather than rendering a bare heading.
#[test]
fn an_empty_ledger_says_how_to_write_the_first_ladder() -> std::io::Result<()> {
    let root = workspace("empty")?;
    let rendered = collect(&root).render();
    assert!(rendered.contains("_No ladders yet."));
    assert!(rendered.contains("research/weakened/<name>.md"));
    Ok(())
}

/// A missing directory is the ordinary state of a workspace nobody has weakened
/// anything in, not an error.
#[test]
fn a_missing_directory_reads_as_no_ladders() {
    let root = std::env::temp_dir().join("math-agent-weakened-absent");
    let _ = std::fs::remove_dir_all(&root);
    assert!(collect(&root).open_rungs().is_empty());
    assert!(collect(&root).fingerprint().is_empty());
    assert!(collect(&root).briefing().is_empty());
}

/// The stance vocabulary, including that reaching the top is not the same kind
/// of terminal state as giving up.
#[test]
fn stances_parse_leniently_and_only_abandonment_closes() {
    assert_eq!(LadderStance::parse("open"), LadderStance::Open);
    assert_eq!(LadderStance::parse("nonsense"), LadderStance::Open);
    assert_eq!(LadderStance::parse(""), LadderStance::Open);
    assert_eq!(LadderStance::parse("Exhausted"), LadderStance::Exhausted);
    assert_eq!(LadderStance::parse("reached"), LadderStance::Exhausted);
    assert_eq!(
        LadderStance::parse("abandoned — went nowhere"),
        LadderStance::Abandoned
    );
    assert!(LadderStance::Abandoned.is_closed());
    assert!(!LadderStance::Exhausted.is_closed());
    assert!(!LadderStance::Open.is_closed());

    assert_eq!(RungStance::parse("nonsense"), RungStance::Open);
    assert_eq!(RungStance::parse(""), RungStance::Open);
    assert_eq!(RungStance::parse("Settled"), RungStance::Settled);
    assert_eq!(RungStance::parse("established"), RungStance::Settled);
    assert_eq!(RungStance::parse("failed — no bound"), RungStance::Failed);
    assert_eq!(RungStance::parse("merged"), RungStance::Merged);
}

/// The alternative spellings a model reaches for are accepted, keys nobody
/// defined are ignored, and a semicolon separated list parses like a comma
/// separated one.
#[test]
fn aliases_and_separators_are_accepted_and_unknown_keys_ignored() -> std::io::Result<()> {
    let root = workspace("aliases")?;
    ladder(
        &root,
        "aliased",
        &rungs(
            "target: G holds for every n\n\
             hard-because: unbounded k; arbitrary degree\n\
             stance: open\n\
             mood: hopeful",
            &["rung: R-1\n\
               weakened: G holds for bounded k\n\
               switched-off: unbounded k\n\
               stance: open\n\
               merge-next: induct on k\n\
               confidence: medium"],
        ),
    )?;
    let rendered = collect(&root).render();
    assert!(rendered.contains("| [[aliased]] |"));
    assert!(rendered.contains("G holds for every n"));
    assert!(rendered.contains("unbounded k, arbitrary degree"));
    assert!(rendered.contains("| `R-1` |"));
    assert!(rendered.contains("induct on k"));
    assert!(!rendered.contains("## Ladders that could not be read"));
    Ok(())
}

/// A pipe in a field would otherwise split the row it is rendered into.
#[test]
fn a_pipe_in_a_field_does_not_break_the_table() -> std::io::Result<()> {
    let root = workspace("pipe")?;
    ladder(
        &root,
        "piped",
        &rungs(
            "goal: |S| >= 2 for every S\ndifficulties: unbounded S",
            &["id: R-1\n\
               statement: |S| >= 2 for finite S\n\
               off: unbounded S\n\
               status: open\n\
               merge: let S grow"],
        ),
    )?;
    let rendered = collect(&root).render();
    assert!(rendered.contains("\\|S\\| >= 2 for every S"));
    Ok(())
}

/// The write path derives the table from these files and must never treat the
/// table itself as one of them — a refresh triggering a refresh is a loop
/// nothing bounds.
#[test]
fn only_ladder_files_drive_the_table() {
    assert!(is_weakened("research/weakened/cycle-length.md"));
    assert!(!is_weakened("research/WEAKENED.md"));
    assert!(!is_weakened("research/weakened/INDEX.md"));
    assert!(!is_weakened("research/weakened/notes.txt"));
    assert!(!is_weakened("research/weakening/cycle-length.md"));
    assert!(!is_weakened("research/backward/event-rate.md"));
    assert!(!is_weakened("research/approaches/generating-function.md"));
}

/// The control behind a weakener turn: what it has to move for it to have done
/// anything a downstream reader can see. Refining a ladder adds no new
/// filename, so comparing names would score a real refinement as a no-op.
#[test]
fn the_fingerprint_moves_on_a_stance_and_not_on_prose() -> std::io::Result<()> {
    let root = workspace("fingerprint")?;
    let header = "goal: G\ndifficulties: a, b\nstatus: open";
    let body = "id: R-1\nstatement: G with a and b off\noff: a, b\nstatus: open\nmerge: turn b on";
    ladder(&root, "tracked", &rungs(header, &[body]))?;
    let before = collect(&root).fingerprint();

    // The same blocks under different prose: nothing downstream changed.
    std::fs::write(
        root.join(format!("{}/tracked.md", super::WEAKENED_DIR)),
        format!(
            "# tracked\n\n{}\n\nEntirely different working notes.\n",
            rungs(header, &[body])
        ),
    )?;
    assert_eq!(collect(&root).fingerprint(), before);

    // The rung is settled: the fingerprint moves.
    ladder(
        &root,
        "tracked",
        &rungs(
            header,
            &["id: R-1\n\
               statement: G with a and b off\n\
               off: a, b\n\
               status: settled\n\
               settled-by: claim-1\n\
               merge: turn b on"],
        ),
    )?;
    assert_ne!(collect(&root).fingerprint(), before);
    Ok(())
}

/// What the next attempt is handed: the weakened statement, what it may assume,
/// and the move that climbs off it. Without the last one an attempt proves the
/// rung and learns nothing about the goal above it.
#[test]
fn the_current_rung_briefs_the_next_attempt_with_its_merge() -> std::io::Result<()> {
    let root = workspace("briefing")?;
    ladder(&root, "cycle-length", &erdos_ladder())?;
    let briefing = collect(&root).briefing();
    assert!(briefing.contains("`R-1` (cycle-length)"));
    assert!(briefing.contains("3-regular graphs"));
    assert!(briefing.contains("switched off: unbounded k, arbitrary minimum degree"));
    assert!(briefing.contains("then merge back: allow degree 4"));
    // Only the current rung travels; the ones above it would be too hard.
    assert!(!briefing.contains("`R-2`"));
    Ok(())
}

/// An open rung carries the ladder it came from, so a briefing can name its
/// source and a reader can open the file it was written in.
#[test]
fn an_open_rung_names_the_ladder_it_came_from() -> std::io::Result<()> {
    let root = workspace("provenance")?;
    ladder(&root, "cycle-length", &erdos_ladder())?;
    let ladders = collect(&root);
    let rungs = ladders.open_rungs();
    let first = rungs.first().expect("the ladder has an open rung");
    assert_eq!(first.ladder, "cycle-length");
    assert_eq!(first.id, "R-1");
    assert_eq!(first.stance, RungStance::Open);
    assert_eq!(first.off.len(), 2);
    Ok(())
}
