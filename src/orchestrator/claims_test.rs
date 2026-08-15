use super::{Holds, Status, collect, identifiers, is_note, parse};

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

/// Naming a curve mid-statement is ordinary mathematical prose, and `E` is a
/// field name on the word alone. An indented line is a continuation whatever it
/// contains, so the rest of the statement survives. A live claim lost its
/// arithmetic-progression condition and its `2E(Q)` criterion to this while
/// still rendering as `proved`.
#[test]
fn an_indented_colon_line_continues_the_value() {
    let text = note(concat!(
        "id: robertson-elliptic-reduction\n",
        "statement: A magic square of squares exists iff there are P0, P1, P2 on\n",
        "  E: y^2 = x(x^2 - c^2) with x-coordinates in 2E(Q),\n",
        "  satisfying x2P2 - x2P1 = x2P1 - x2P0.\n",
        "status: proved",
    ));
    let (claims, faults) = parse(&text, "research/L1.1/bremner.md");
    assert!(faults.is_empty());
    assert_eq!(claims.len(), 1);

    let claim = &claims[0];
    assert!(claim.statement.contains("E: y^2 = x(x^2 - c^2)"));
    // The condition the whole claim turns on, and the first thing lost.
    assert!(claim.statement.contains("x2P2 - x2P1 = x2P1 - x2P0"));
    assert_eq!(claim.status, Status::Proved);
}

/// A key the reader does not act on still opens a field when it sits at the
/// column the other keys do. Folding it into the previous value instead would
/// append prose to whatever came before it, which for `answers` is a list of
/// request identifiers.
#[test]
fn an_unrecognised_key_at_the_margin_does_not_extend_the_previous_field() {
    let text = note(concat!(
        "id: a-claim\n",
        "statement: Something holds.\n",
        "answers: exact-reduction-magic-507c\n",
        "verified-by: traced through the paper\n",
        "status: proved",
    ));
    let (claims, _) = parse(&text, "research/L1.0/a.md");
    assert_eq!(claims.len(), 1);
    assert_eq!(claims[0].answers, vec!["exact-reduction-magic-507c"]);
    assert_eq!(claims[0].status, Status::Proved);
}

/// A block written with every line indented has no line at the left margin, so
/// the column its field names start at is read from the block rather than
/// assumed.
#[test]
fn a_uniformly_indented_block_still_parses() {
    let text = note(concat!(
        "    id: indented\n",
        "    statement: A holds because of B\n",
        "      where B: the second condition.\n",
        "    status: checked",
    ));
    let (claims, faults) = parse(&text, "research/L1.0/a.md");
    assert!(faults.is_empty());
    assert_eq!(claims.len(), 1);
    assert_eq!(claims[0].id, "indented");
    assert_eq!(claims[0].status, Status::Checked);
    assert!(claims[0].statement.contains("B: the second condition"));
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
        note(
            "id: trollope-delange\nstatement: The summatory bit count has a closed form.\nstatus: proved\nholds-here: yes",
        ),
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
        note(
            "id: taken-on-trust\nstatement: The bound is tight.\nholds-here: yes\nstatus: asserted",
        ),
    )?;
    std::fs::write(
        root.join("research/L1.0/proved.md"),
        note(
            "id: established\nstatement: The recurrence terminates.\nholds-here: yes\nstatus: proved",
        ),
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

/// A lookup and somebody's unproved word are different debts.
///
/// Project Euler 241 is the case. Its answer came from a hardcoded copy of an
/// OEIS b-file while its own enumeration was missing four of nine terms, and
/// nothing on disk said which file the number came from. `catalogued` exists so
/// that a lookup asks for the one thing that would settle it — a program that
/// reproduces the terms — rather than being filed beside an unproved theorem,
/// which asks for a proof instead.
#[test]
fn a_catalogued_claim_is_separated_from_an_asserted_one() -> std::io::Result<()> {
    let root = std::env::temp_dir().join("math-agent-claims-catalogued");
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(root.join("research/L1.0"))?;
    std::fs::write(
        root.join("research/L1.0/looked-up.md"),
        note(
            "id: hemiperfect-terms\nstatement: The terms below 1e18 are the 22 A159907 \
             entries.\nholds-here: yes\nstatus: catalogued",
        ),
    )?;
    std::fs::write(
        root.join("research/L1.0/asserted.md"),
        note("id: taken-on-trust\nstatement: The bound is tight.\nholds-here: yes\nstatus: asserted"),
    )?;
    let rendered = collect(&root).render();

    assert!(rendered.contains("## Taken from a catalogue"));
    assert!(rendered.contains("`hemiperfect-terms`"));
    // The row itself has to carry the status, because the section is derived
    // and a reader who scrolls the table never reaches it.
    assert!(
        rendered.contains("catalogued"),
        "the status must appear on the row: {rendered}"
    );
    // Separation is the whole point: a lookup filed under "unverified" asks
    // for a proof, which is not what would settle it.
    let unverified = rendered
        .split("## Load-bearing but unverified")
        .nth(1)
        .unwrap_or_default();
    let unverified = unverified.split("## ").next().unwrap_or_default();
    assert!(
        !unverified.contains("hemiperfect-terms"),
        "a catalogued claim must not be filed as merely unverified: {rendered}"
    );
    assert!(unverified.contains("taken-on-trust"));
    Ok(())
}

/// What the run computed counts as much as what it read.
///
/// The ledger walked only `research/`, so a claim could originate only in a
/// note about a *source* — the run recorded what it had read and forgot what it
/// had proved. Project Euler 597 sat at `proved=0` for fourteen consecutive
/// sweeps while holding the check value its own problem statement supplies,
/// reproduced exactly, and 38 points cross-validated two ways.
#[test]
fn a_claim_computed_in_code_out_reaches_the_ledger() -> std::io::Result<()> {
    let root = std::env::temp_dir().join("math-agent-claims-computed");
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(root.join("research/L1.0"))?;
    std::fs::create_dir_all(root.join("code/out"))?;
    std::fs::write(
        root.join("code/out/NOTES.md"),
        note(
            "id: p4-400-reproduced\nstatement: p(4,400) = 521/1020, matching the stated \
             check to ten digits.\nholds-here: yes\nstatus: checked",
        ),
    )?;
    std::fs::write(
        root.join("research/L1.0/read.md"),
        note("id: from-a-paper\nstatement: The bound is tight.\nholds-here: yes\nstatus: proved"),
    )?;
    let ledger = collect(&root);
    let rendered = ledger.render();

    assert!(
        rendered.contains("`p4-400-reproduced`"),
        "a computed claim must reach the ledger: {rendered}"
    );
    assert!(rendered.contains("`from-a-paper`"));
    // Both are things this run stands behind, so both count as established —
    // that total is what the judge is shown when an attempt is cut off before
    // it can report.
    assert_eq!(ledger.established(), 2);
    assert_eq!(ledger.asserted(), 0);
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
        note(
            "id: popcount-closed-form\nstatement: The summatory popcount admits a closed form.\nbearing: lets A(n) be evaluated in polylog time",
        ),
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
    assert!(is_note("research/summaries/siegel.md"));
    assert!(!is_note("research/ROOT.md"));
    assert!(!is_note("research/INDEX.md"));
    // The originals carry no claims, and the ledger must not re-derive itself.
    assert!(!is_note("research/sources/siegel.full.md"));
    assert!(!is_note("research/CLAIMS.md"));
    // A note beside a program's output is a note: what the run computed is
    // evidence on the same terms as what it read, and the trigger has to match
    // what `collect` walks or a recorded claim never reaches the table.
    assert!(is_note("code/out/NOTES.md"));
    assert!(is_note("code/out/cutvertex/findings.md"));
    assert!(!is_note("code/out/INDEX.md"));
    // Programs and their raw captures are not notes, and neither is work
    // outside the library.
    assert!(!is_note("code/solve.py"));
    assert!(!is_note("code/out/run26.log"));
    assert!(!is_note("code/lib/hemisum.py"));
    assert!(!is_note("SCRATCHPAD.md"));
}

/// A refutation with its reason attached must still read as a refutation.
///
/// `Status::parse` matched on a prefix and `Holds::parse` demanded an exact
/// value, and the inconsistency cost PE620 its own best finding. That run
/// established its oracle model was wrong — `g(16,5,5,6) = 0` against a stated
/// `9` — and wrote `holds-here: false — contradicts the worked oracle value 9.`
/// The trailing clause is exactly what every other field here asks for, and it
/// turned a checked refutation into `**unchecked**` in the ledger every
/// planning role reads.
#[test]
fn a_holds_field_may_carry_the_reason_beside_the_answer() {
    use super::Holds;

    assert_eq!(Holds::parse("false — contradicts the worked oracle value 9."), Holds::No);
    assert_eq!(Holds::parse("no, the hypotheses need a prime modulus"), Holds::No);
    assert_eq!(Holds::parse("yes (checked against n=3..9)"), Holds::Yes);
    assert_eq!(Holds::parse("fails: the graph is not simple"), Holds::No);

    // Bare values keep working.
    assert_eq!(Holds::parse("yes"), Holds::Yes);
    assert_eq!(Holds::parse("no"), Holds::No);
    assert_eq!(Holds::parse("unchecked"), Holds::Unchecked);

    // A prefix must not be read out of a longer word: `notation` is not `no`,
    // and a hedge is never read as a decision.
    assert_eq!(Holds::parse("notation differs"), Holds::Unchecked);
    assert_eq!(Holds::parse("yesterday's run said so"), Holds::Unchecked);
    assert_eq!(Holds::parse("probably not"), Holds::Unchecked);
}

/// A formalised claim is the one row the ledger checks rather than believes.
///
/// The failure being closed is the whole reason `Status::Formalised` exists:
/// with Lean installed and no Rust running it, `research/CLAIMS.md` could not
/// tell a kernel-checked lemma from a sentence claiming one, so it recorded
/// both the same way. Here the same note is derived twice — once with a passing
/// verdict on disk beside it and once without — and the two must disagree.
#[test]
fn a_formalised_claim_stands_only_when_the_kernel_backs_it() -> std::io::Result<()> {
    let root = std::env::temp_dir().join("math-agent-claims-formalised");
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(root.join("code/out"))?;
    std::fs::write(
        root.join("code/out/NOTES.md"),
        note(
            "id: pigeonhole-bound\nstatement: Every 3-colouring of K_17 has a monochromatic \
             triangle.\nholds-here: yes\nstatus: formalised\nformalisation: code/ramsey.lean",
        ),
    )?;

    // No verdict on disk: the claim said `formalised` and nothing supports it.
    let bare = collect(&root);
    assert_eq!(bare.established(), 0, "an unbacked claim is not established");
    assert_eq!(bare.asserted(), 1, "it is downgraded, not dropped");
    let rendered = bare.render();
    assert!(rendered.contains("`pigeonhole-bound`"), "the claim survives the downgrade");
    assert!(rendered.contains("Called formalised, not backed by the kernel"));
    assert!(
        rendered.contains("no `lean_check` verdict exists"),
        "the reason names what to do next: {rendered}"
    );

    // The same note, with a passing verdict beside it.
    std::fs::create_dir_all(root.join(super::super::lean::VERDICT_DIR))?;
    std::fs::write(
        root.join(super::super::lean::VERDICT_DIR)
            .join("code_ramsey.lean.json"),
        r#"{"file":"code/ramsey.lean","compiled":true,"sorries":[],
            "axioms":["'ramsey' depends on axioms: [propext, Classical.choice]"]}"#,
    )?;
    let backed = collect(&root);
    assert_eq!(backed.established(), 1, "a kernel-backed claim is established");
    assert_eq!(backed.asserted(), 0);
    assert!(!backed.render().contains("Called formalised"));
    Ok(())
}

/// A verdict that exists and does not pass is worse than none, so it is named.
#[test]
fn a_formalisation_with_a_sorry_in_it_is_downgraded_and_says_why() -> std::io::Result<()> {
    let root = std::env::temp_dir().join("math-agent-claims-sorry");
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(root.join("code/out"))?;
    std::fs::create_dir_all(root.join(super::super::lean::VERDICT_DIR))?;
    std::fs::write(
        root.join("code/out/NOTES.md"),
        note(
            "id: half-proved\nstatement: The bound holds for every n.\nholds-here: yes\n\
             status: formalised\nformalisation: code/bound.lean",
        ),
    )?;
    std::fs::write(
        root.join(super::super::lean::VERDICT_DIR)
            .join("code_bound.lean.json"),
        r#"{"file":"code/bound.lean","compiled":true,
            "sorries":["bound.lean:9:2: warning: declaration uses 'sorry'"],"axioms":[]}"#,
    )?;
    let ledger = collect(&root);
    assert_eq!(ledger.established(), 0);
    assert!(
        ledger.render().contains("`sorry` still in it"),
        "the objection must name the sorry rather than say the check failed"
    );
    Ok(())
}

/// A claim that names no file at all is the easiest way to fake the status.
#[test]
fn a_formalised_claim_naming_no_file_is_refused() -> std::io::Result<()> {
    let root = std::env::temp_dir().join("math-agent-claims-nofile");
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(root.join("code/out"))?;
    std::fs::write(
        root.join("code/out/NOTES.md"),
        note(
            "id: bare-assertion\nstatement: It is formalised, honestly.\nholds-here: yes\n\
             status: formalised",
        ),
    )?;
    let ledger = collect(&root);
    assert_eq!(ledger.established(), 0);
    assert!(ledger.render().contains("names no `formalisation:` file"));
    Ok(())
}

/// `formally proved` must not be read as the weaker, unchecked status.
#[test]
fn the_status_parse_prefers_formalised_over_proved() {
    for spelling in [
        "formalised",
        "formalized",
        "formally proved",
        "lean",
        "kernel-checked",
    ] {
        assert_eq!(
            Status::parse(spelling),
            Status::Formalised,
            "`{spelling}` names a kernel check"
        );
    }
    // The source proving it is still a different, weaker thing.
    assert_eq!(Status::parse("proved"), Status::Proved);
    assert_eq!(Status::parse("proven in the paper"), Status::Proved);
}

/// A measurement this run computed is `checked`, not `asserted`.
///
/// A run told "a measurement is not a proof — label it" writes exactly
/// `measured, not proved`. That phrase used to match no arm and fall through
/// to `asserted`, whose rendered line reads "asserted by the source, not
/// proved there and not checked here" — the opposite of what happened, and in
/// the direction that loses the check. A live run's counts fell as its
/// evidence improved.
#[test]
fn a_measured_status_is_checked_not_asserted() {
    for spelling in [
        "measured",
        "measured, not proved",
        "measured-not-proved",
        "Measured (streamed to N=40000)",
    ] {
        assert_eq!(
            Status::parse(spelling),
            Status::Checked,
            "`{spelling}` names a computation this run performed"
        );
    }
}

/// A claim citing the counterexample engine is checked against what it found.
///
/// The asymmetry with `formalised` is deliberate and worth pinning down: a
/// `refutation:` line is optional, because a counterexample can be established
/// by hand. What is checked is only the claim that *cites the engine* — and
/// citing it falsely is the worst case available, since a refutation does not
/// merely fail to establish the goal, it asserts the goal is false.
#[test]
fn a_claim_citing_a_refutation_needs_the_engine_to_have_made_one() -> std::io::Result<()> {
    let root = std::env::temp_dir().join("math-agent-claims-refutation");
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(root.join("code/out"))?;
    std::fs::create_dir_all(root.join(super::super::refute::VERDICT_DIR))?;
    std::fs::write(
        root.join("code/out/NOTES.md"),
        note(
            "id: girth-five-fails\nstatement: No such graph exists at order 7.\nholds-here: yes\n\
             status: checked\nrefutation: code/refute/girth.p",
        ),
    )?;

    // Nothing filed: the claim cites an engine run that never happened.
    let bare = collect(&root);
    assert_eq!(bare.established(), 0, "an uncited refutation is not established");
    assert!(
        bare.render().contains("no `find_counterexample` verdict exists"),
        "the reason must name what is missing: {}",
        bare.render()
    );

    // Filed, but the engine did not refute anything — it timed out.
    std::fs::write(
        root.join(super::super::refute::VERDICT_DIR)
            .join("code_refute_girth.p.json"),
        r#"{"problem":"code/refute/girth.p","finding":"undecided","status":"Timeout","model":""}"#,
    )?;
    let weak = collect(&root);
    assert_eq!(weak.established(), 0);
    assert!(
        weak.render().contains("was not refuted"),
        "a search that settled nothing is not a counterexample"
    );

    // Filed, and it really did find one.
    std::fs::write(
        root.join(super::super::refute::VERDICT_DIR)
            .join("code_refute_girth.p.json"),
        r#"{"problem":"code/refute/girth.p","finding":"refuted",
            "status":"CounterSatisfiable","model":"tff(d,type,d: $tType)."}"#,
    )?;
    let backed = collect(&root);
    assert_eq!(backed.established(), 1, "a real refutation stands");
    assert!(!backed.render().contains("was not refuted"));
    Ok(())
}

/// A claim with no `refutation:` line is untouched by the refutation check.
#[test]
fn an_ordinary_claim_is_not_asked_for_a_counterexample() -> std::io::Result<()> {
    let root = std::env::temp_dir().join("math-agent-claims-no-refutation");
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(root.join("code/out"))?;
    std::fs::write(
        root.join("code/out/NOTES.md"),
        note("id: plain\nstatement: The sum is 12.\nholds-here: yes\nstatus: checked"),
    )?;
    let ledger = collect(&root);
    assert_eq!(ledger.established(), 1);
    assert!(!ledger.render().contains("find_counterexample"));
    Ok(())
}

/// Both of these are sentences a live run actually wrote into a `rests-on:`
/// field, and the whitespace split turned each into a handful of identifiers
/// that no file could ever carry. Eleven invented dangling edges hide the one
/// real misspelling the same report exists to catch.
#[test]
fn a_field_that_says_there_is_nothing_lists_nothing() {
    assert!(
        identifiers("none (research/CLAIMS.md is empty; no claim in the ledger covers this)")
            .is_empty(),
        "an answer that opens with `none` is an answer, not a list"
    );
    assert!(identifiers("n/a").is_empty());
    assert!(identifiers("  ").is_empty());
}

/// The shape filter drops prose without touching a real list — including the
/// misspelled entries the dangling-edge report is for.
#[test]
fn prose_is_dropped_while_identifiers_survive() {
    assert_eq!(
        identifiers("alpha-lemma, beta/gamma.2"),
        vec!["alpha-lemma".to_string(), "beta/gamma.2".to_string()]
    );
    assert_eq!(
        identifiers("alpha-lemma (proved; see below)"),
        vec!["alpha-lemma".to_string()],
        "the id survives and the parenthetical does not"
    );
    assert_eq!(
        identifiers("mispelt-lemma"),
        vec!["mispelt-lemma".to_string()],
        "a misspelling is still id-shaped, so it is still reported as dangling"
    );
}
