use super::{Stance, collect, is_approach};

fn approach(root: &std::path::Path, slug: &str, block: &str) -> std::io::Result<()> {
    std::fs::write(
        root.join(format!("{}/{slug}.md", super::APPROACHES_DIR)),
        format!("# {slug}\n\n```approach\n{block}\n```\n\nWorking notes.\n"),
    )
}

fn workspace(name: &str) -> std::io::Result<std::path::PathBuf> {
    let root = std::env::temp_dir().join(format!("math-agent-approaches-{name}"));
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(root.join(super::APPROACHES_DIR))?;
    Ok(root)
}

/// The table is one row per candidate line of attack, carrying whether the
/// literature has been consulted and what the first move is.
#[test]
fn an_approach_becomes_a_row_naming_its_precedent() -> std::io::Result<()> {
    let root = workspace("row")?;
    approach(
        &root,
        "generating-function",
        "idea: Encode the skip budget as a bivariate generating function\n\
         mechanism: the recursion is linear in the budget, so the transform factors\n\
         status: grounded\n\
         precedent: https://example.org/wilf-generatingfunctionology\n\
         first-step: write F(x, y) for n <= 6 and check the coefficients against brute.py",
    )?;

    let rendered = collect(&root).render();
    assert!(rendered.contains("[[generating-function]]"));
    assert!(rendered.contains("bivariate generating function"));
    assert!(rendered.contains("grounded"));
    assert!(rendered.contains("wilf-generatingfunctionology"));
    assert!(rendered.contains("check the coefficients"));
    // Its precedent is recorded, so it is not listed as unchecked.
    assert!(!rendered.contains("## Not yet taken to the literature"));
    Ok(())
}

/// The whole point of the ledger: a refuted idea keeps the reason it died, so
/// the next inventor does not propose it again in different words.
#[test]
fn a_refuted_approach_keeps_its_reason() -> std::io::Result<()> {
    let root = workspace("refuted")?;
    approach(
        &root,
        "sprague-grundy",
        "idea: Reduce the board with Sprague-Grundy values\n\
         status: refuted\n\
         killed-by: the game is strictly partizan, so Grundy values do not apply",
    )?;
    let rendered = collect(&root).render();
    assert!(rendered.contains("| [[sprague-grundy]] |"));
    assert!(rendered.contains("## What closed, and why"));
    assert!(rendered.contains("strictly partizan"));
    Ok(())
}

/// A closed approach with no reason is worthless to the role reading it, and
/// the table says so rather than presenting it as a settled matter.
#[test]
fn a_closed_approach_without_a_reason_is_called_out() -> std::io::Result<()> {
    let root = workspace("reasonless")?;
    approach(&root, "vague", "idea: Try something else\nstatus: spent")?;
    let rendered = collect(&root).render();
    assert!(rendered.contains("no reason recorded"));
    Ok(())
}

/// Empty `precedent` means nobody checked, which is a different statement from
/// nothing having been found, and the table keeps the two apart.
#[test]
fn an_unchecked_approach_is_distinguished_from_a_fruitless_one() -> std::io::Result<()> {
    let root = workspace("unchecked")?;
    approach(
        &root,
        "guesswork",
        "idea: Bijection to labelled forests\n\
         mechanism: the degree condition looks like a Prufer constraint\n\
         status: proposed",
    )?;
    let rendered = collect(&root).render();
    assert!(rendered.contains("_unchecked_"));
    assert!(rendered.contains("## Not yet taken to the literature"));
    assert!(rendered.contains("Prufer constraint"));
    Ok(())
}

/// Every stance the life cycle defines survives a round trip through the file.
#[test]
fn every_stance_parses() -> std::io::Result<()> {
    let root = workspace("stances")?;
    for (slug, written) in [
        ("a", "proposed"),
        ("b", "grounded"),
        ("c", "refuted"),
        ("d", "adopted"),
        ("e", "spent"),
    ] {
        approach(&root, slug, &format!("idea: An idea\nstatus: {written}"))?;
    }
    let approaches = collect(&root);
    let stances: Vec<Stance> = approaches
        .approaches
        .iter()
        .map(|approach| approach.stance)
        .collect();
    assert_eq!(
        stances,
        vec![
            Stance::Proposed,
            Stance::Grounded,
            Stance::Refuted,
            Stance::Adopted,
            Stance::Spent
        ]
    );
    // Only the two that end an approach count as closed.
    assert_eq!(approaches.closed().count(), 2);
    Ok(())
}

/// An unrecognised status is treated as unchecked rather than as closed: an
/// approach wrongly read as refuted would be silently dropped from the run's
/// options, which is the expensive direction to be wrong in.
#[test]
fn an_unknown_stance_falls_back_to_proposed() -> std::io::Result<()> {
    let root = workspace("unknown")?;
    approach(&root, "odd", "idea: An idea\nstatus: percolating")?;
    let approaches = collect(&root);
    assert_eq!(approaches.closed().count(), 0);
    assert!(approaches.render().contains("proposed"));
    Ok(())
}

/// A file under `approaches/` with no approach block is a note, and saying so
/// is better than listing it as a line of attack nobody can act on.
#[test]
fn a_file_without_an_approach_block_is_reported() -> std::io::Result<()> {
    let root = workspace("noblock")?;
    std::fs::write(
        root.join(format!("{}/stray.md", super::APPROACHES_DIR)),
        "# Stray\n\nJust some prose.\n",
    )?;
    let rendered = collect(&root).render();
    assert!(rendered.contains("## Approaches that could not be read"));
    assert!(rendered.contains("`stray` has no approach block"));
    Ok(())
}

/// An unclosed fence is reported rather than silently yielding no approach.
#[test]
fn an_unclosed_block_is_reported() -> std::io::Result<()> {
    let root = workspace("unclosed")?;
    std::fs::write(
        root.join(format!("{}/torn.md", super::APPROACHES_DIR)),
        "# Torn\n\n```approach\nidea: An idea\nstatus: proposed\n",
    )?;
    let rendered = collect(&root).render();
    assert!(rendered.contains("never closed"));
    Ok(())
}

/// The full rendering gathers one approach whole, including the idea the table
/// row truncates — which is what the dossier needs and the table does not.
#[test]
fn the_full_rendering_keeps_an_idea_a_row_would_cut() -> std::io::Result<()> {
    let root = workspace("full")?;
    let long = "reduce to the bipartite case by contracting each odd cycle to a single vertex, \
                which preserves the degree bound everywhere except at the contracted vertices, \
                where it can be restored by a local exchange argument on the girth";
    approach(
        &root,
        "bipartite-reduction",
        &format!(
            "idea: {long}\n\
             status: refuted\n\
             killed-by: the construction produces an odd cycle at every order above 11"
        ),
    )?;
    let approaches = collect(&root);
    let full: String = approaches.closed().map(super::Approach::full).collect();
    // The idea arrives whole, and the reason it closed arrives with it.
    assert!(full.contains("local exchange argument on the girth"));
    assert!(full.contains("odd cycle at every order above 11"));
    // The table truncates the same idea in its row, which is why `full` exists.
    assert!(
        !approaches
            .render()
            .contains("local exchange argument on the girth")
    );
    Ok(())
}

/// An empty folder says how to record the first approach rather than nothing.
#[test]
fn an_empty_folder_says_how_to_start() -> std::io::Result<()> {
    let root = workspace("empty")?;
    let rendered = collect(&root).render();
    assert!(rendered.contains("No approaches yet"));
    assert!(rendered.contains("research/approaches/<name>.md"));
    Ok(())
}

/// The table is bounded, and says how many it left out rather than pretending
/// it showed everything.
#[test]
fn the_table_is_capped_and_says_so() -> std::io::Result<()> {
    let root = workspace("capped")?;
    for index in 0..super::MAX_ROWS + 3 {
        approach(
            &root,
            &format!("idea-{index:02}"),
            "idea: One of many\nstatus: proposed",
        )?;
    }
    let rendered = collect(&root).render();
    assert!(rendered.contains("_3 further approaches not shown._"));
    Ok(())
}

/// Only an approach file re-derives the approach table.
#[test]
fn the_write_path_recognises_an_approach() {
    assert!(is_approach("research/approaches/generating-function.md"));
    assert!(!is_approach("research/approaches/INDEX.md"));
    assert!(!is_approach("research/threads/passes.md"));
    assert!(!is_approach("research/APPROACHES.md"));
}
