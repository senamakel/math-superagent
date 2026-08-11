use super::{Holds, Status, collect, is_note, parse};

fn note(body: &str) -> String {
    format!("# A note\n\nSome prose.\n\n```claim\n{body}\n```\n\nMore prose.\n")
}

/// The block the whole design rests on: a statement with its hypotheses, its
/// standing here, and where to check it.
#[test]
fn a_claim_block_is_read_field_by_field() {
    let text = note(
        "id: li-zugzwang\n\
         statement: A loopy game is a zugzwang game iff it equals x & y\n\
           for dyadic rationals x <= y.\n\
         hypotheses: x, y dyadic with x <= y\n\
         holds-here: yes\n\
         status: proved\n\
         bearing: warrants the (A,B) stopper model for the skip\n\
         anchor: research/L0.1/siegel.full.md",
    );
    let (claims, faults) = parse(&text, "research/L1.1/siegel.md");
    assert!(faults.is_empty());
    assert_eq!(claims.len(), 1);

    let claim = &claims[0];
    assert_eq!(claim.id, "li-zugzwang");
    // A value running to a second line continues the field rather than
    // starting a new one, so a statement need not be reflowed into one line.
    assert!(claim.statement.contains("for dyadic rationals x <= y"));
    assert_eq!(claim.holds, Holds::Yes);
    assert_eq!(claim.status, Status::Proved);
    assert_eq!(claim.source, "research/L1.1/siegel.md");
    assert_eq!(claim.anchor, "research/L0.1/siegel.full.md");
}

/// A colon inside a statement does not open a new field. `S(n): the skip
/// count` would otherwise become a field named after the function it defines.
#[test]
fn a_colon_in_prose_does_not_start_a_field() {
    let text = note(
        "id: skip-count\n\
         statement: Define S(n): the least number of skips One needs.\n\
         status: asserted",
    );
    let (claims, _) = parse(&text, "research/L1.0/skip.md");
    assert_eq!(claims.len(), 1);
    assert!(claims[0].statement.contains("S(n): the least number"));
}

/// A block that claims nothing, or that nothing can refer to, is reported
/// rather than dropped: a claim silently discarded leaves the note reading as
/// though it recorded something.
#[test]
fn a_block_missing_its_id_or_statement_is_reported() {
    let (claims, faults) = parse(&note("statement: Something is true."), "research/L1.0/a.md");
    assert!(claims.is_empty());
    assert_eq!(faults.len(), 1);
    assert!(faults[0].contains("no `id`"));

    let (claims, faults) = parse(&note("id: bare"), "research/L1.0/b.md");
    assert!(claims.is_empty());
    assert!(faults[0].contains("no `statement`"));
}

/// The ledger is derived from disk, and only from the notes: a full text is
/// the untouched original and reading megabytes of converted paper to find
/// blocks that cannot be there is the one way the walk could get expensive.
#[test]
fn the_ledger_is_derived_from_the_notes_on_disk() -> std::io::Result<()> {
    let root = std::env::temp_dir().join("math-agent-claims-derive");
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(root.join("research/L1.0"))?;
    std::fs::create_dir_all(root.join("research/L0.0"))?;
    std::fs::write(
        root.join("research/L1.0/trollope.md"),
        note("id: trollope-delange\nstatement: The summatory bit count has a closed form.\nstatus: proved\nholds-here: yes"),
    )?;
    std::fs::write(
        root.join("research/L0.0/trollope.full.md"),
        note("id: not-a-claim\nstatement: A full text carries no claims."),
    )?;

    let ledger = collect(&root);
    let rendered = ledger.render();
    assert!(rendered.contains("trollope-delange"));
    assert!(
        !rendered.contains("not-a-claim"),
        "the untouched original is not a note: {rendered}"
    );
    Ok(())
}

/// The scholar prompt calls a contradiction the most valuable thing it can
/// find; until this table existed nothing mechanically noticed one.
#[test]
fn contradictions_between_claims_are_surfaced() -> std::io::Result<()> {
    let root = std::env::temp_dir().join("math-agent-claims-contradict");
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(root.join("research/L1.0"))?;
    std::fs::write(
        root.join("research/L1.0/pass.md"),
        note(
            "id: skip-differs\n\
             statement: S(n) is not the no-skip board value A-B.\n\
             status: proved\n\
             contradicts: skip-equals-difference",
        ),
    )?;
    std::fs::write(
        root.join("research/L1.0/counting.md"),
        note(
            "id: skip-equals-difference\n\
             statement: S(n) equals A(n)-B(n).\n\
             status: heuristic",
        ),
    )?;

    let rendered = collect(&root).render();
    assert!(rendered.contains("## Contradictions"));
    assert!(rendered.contains("`skip-differs`"));
    assert!(rendered.contains("contradicts `skip-equals-difference`"));
    Ok(())
}

/// A contradiction naming a claim nobody wrote down is reported too: a belief
/// that cannot be located is not resolved by leaving it unmentioned.
#[test]
fn a_contradiction_naming_an_unknown_claim_says_so() -> std::io::Result<()> {
    let root = std::env::temp_dir().join("math-agent-claims-dangling");
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(root.join("research/L1.0"))?;
    std::fs::write(
        root.join("research/L1.0/one.md"),
        note("id: only-claim\nstatement: Something.\ncontradicts: never-written-down"),
    )?;
    let rendered = collect(&root).render();
    assert!(rendered.contains("no claim of that id is on disk"));
    Ok(())
}

/// A claim taken to hold here on a source's word alone is what the method
/// policy asks to be distinguished, and what a long run forgets it did.
#[test]
fn load_bearing_but_unverified_claims_are_listed() -> std::io::Result<()> {
    let root = std::env::temp_dir().join("math-agent-claims-unverified");
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(root.join("research/L1.0"))?;
    std::fs::write(
        root.join("research/L1.0/asserted.md"),
        note("id: taken-on-trust\nstatement: The bound is tight.\nholds-here: yes\nstatus: asserted"),
    )?;
    std::fs::write(
        root.join("research/L1.0/proved.md"),
        note("id: established\nstatement: The recurrence terminates.\nholds-here: yes\nstatus: proved"),
    )?;
    let rendered = collect(&root).render();
    assert!(rendered.contains("## Load-bearing but unverified"));
    assert!(rendered.contains("`taken-on-trust`"));
    assert!(
        !rendered.contains("- `established`"),
        "a proved claim is not unverified: {rendered}"
    );
    Ok(())
}

/// Retrieval is the point: a query naming an object finds the claims about it.
#[test]
fn search_ranks_by_how_much_of_the_query_a_claim_carries() -> std::io::Result<()> {
    let root = std::env::temp_dir().join("math-agent-claims-search");
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(root.join("research/L1.0"))?;
    std::fs::write(
        root.join("research/L1.0/on-point.md"),
        note("id: popcount-closed-form\nstatement: The summatory popcount admits a closed form.\nbearing: lets A(n) be evaluated in polylog time"),
    )?;
    std::fs::write(
        root.join("research/L1.0/off-point.md"),
        note("id: unrelated\nstatement: Chomp is not equivalent to Nim."),
    )?;

    let ledger = collect(&root);
    let found = ledger.search("summatory popcount closed form polylog");
    assert_eq!(found.len(), 1);
    assert_eq!(found[0].id, "popcount-closed-form");
    assert!(ledger.search("bijection between lattice paths").is_empty());
    Ok(())
}

/// The write path re-derives on a note and leaves everything else alone.
#[test]
fn only_a_research_note_triggers_a_rederivation() {
    assert!(is_note("research/L1.0/siegel.md"));
    assert!(is_note("research/ROOT.md"));
    // The originals carry no claims, and the ledger must not re-derive itself.
    assert!(!is_note("research/L0.0/siegel.full.md"));
    assert!(!is_note("research/CLAIMS.md"));
    // Nor does work outside the library.
    assert!(!is_note("code/solve.py"));
    assert!(!is_note("MEMORY.md"));
}
