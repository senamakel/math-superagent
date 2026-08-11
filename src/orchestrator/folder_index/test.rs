//! Unit tests for the per-folder index.
#![allow(clippy::expect_used)]

use std::collections::BTreeMap;

use crate::agent::Result;

use super::{INDEX_FILE, brief, folder_name, index_for, parse, render, split};

fn entries(pairs: &[(&str, &str)]) -> BTreeMap<String, String> {
    pairs
        .iter()
        .map(|(name, purpose)| ((*name).to_string(), (*purpose).to_string()))
        .collect()
}

#[test]
fn a_rendered_index_round_trips_through_the_parser() {
    // Descriptions survive a refresh only if what we write is what we read.
    let original = entries(&[
        ("brute.py", "naive oracle; validates the real method"),
        (
            "solution.py",
            "efficient peel solver; the answer comes from here",
        ),
    ]);

    let parsed = parse(&render("", &original, ""));

    assert_eq!(parsed, original);
}

#[test]
fn a_reformatted_index_does_not_lose_its_descriptions() {
    // An index a human or an agent has rewritten must still yield its rows,
    // because losing them silently is worse than an ugly table.
    let hand_written = "# Notes\n\
        | File | Purpose |\n\
        |------|---------|\n\
        |`brute.py`| naive oracle |\n\
        | solution.py | the real method |\n\
        \nsome prose that is not a row\n";

    let parsed = parse(hand_written);

    assert_eq!(
        parsed.get("brute.py").map(String::as_str),
        Some("naive oracle")
    );
    assert_eq!(
        parsed.get("solution.py").map(String::as_str),
        Some("the real method")
    );
    // The header and separator are not files.
    assert!(!parsed.contains_key("File"));
    assert_eq!(parsed.len(), 2);
}

#[test]
fn a_tree_level_is_described_in_the_index_at_its_root() {
    // One index per tree, not one per level. A live organizer refreshed
    // `research` after the levels went in, found no files directly in it, and
    // dropped all fourteen descriptions as stale.
    assert_eq!(
        split("research/L1.0/paper.md"),
        ("research".to_string(), "L1.0/paper.md".to_string())
    );
    assert_eq!(
        split("reflections/L0.0/1700_01_learnings.md"),
        (
            "reflections".to_string(),
            "L0.0/1700_01_learnings.md".to_string()
        )
    );
    // An ordinary subfolder still keeps its own index.
    assert_eq!(
        split("toolkits/pell.py"),
        ("toolkits".to_string(), "pell.py".to_string())
    );
    assert!(super::is_level("L0") && super::is_level("L0.0") && super::is_level("L12.3"));
    assert!(!super::is_level("L") && !super::is_level("Lib") && !super::is_level("folds"));
}

#[tokio::test]
async fn describing_a_sources_full_text_points_at_the_digest_instead() -> Result<()> {
    // `refresh` never lists a full text, so a description of one is discarded
    // on the next pass. A live organizer spent seventeen calls that way.
    let root =
        std::env::temp_dir().join(format!("math-agent-describe-full-{}", std::process::id()));
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(root.join("research/L0.0")).expect("temporary workspace is creatable");
    std::fs::create_dir_all(root.join("research/L1.0")).expect("digest level is creatable");
    let root = root.canonicalize().expect("workspace resolves");
    // The digest lives a level above the original it reads, so the hint has to
    // name that batch and not the original's own.
    std::fs::write(root.join("research/L0.0/paper.full.md"), "full").expect("original is writable");
    std::fs::write(root.join("research/L1.0/paper.md"), "digest").expect("digest is writable");
    let documents = super::super::documents::WorkspaceDocuments::new(root.clone())?;
    let tools = super::FolderIndexTool::all(&documents);
    let tool = tools
        .iter()
        .find(|tool| tool.name() == "describe_file")
        .expect("describe_file is registered");

    let refused = tool
        .call(
            &(),
            crate::agent::ToolCall {
                id: "call-1".into(),
                name: "describe_file".into(),
                invalid: None,
                arguments: serde_json::json!({
                    "path": "research/L0.0/paper.full.md",
                    "purpose": "the whole converted paper"
                }),
            },
        )
        .await;

    let message = refused
        .err()
        .map(|error| error.to_string())
        .unwrap_or_default();
    assert!(message.contains("L1.0/paper.md"), "{message}");
    assert!(!message.contains("L0.0/paper.md"), "{message}");
    // A source nothing has digested yet has no row to describe, and saying so
    // beats naming a file that is not there.
    let _ = std::fs::write(root.join("research/L0.0/orphan.full.md"), "full");
    let orphan = tool
        .call(
            &(),
            crate::agent::ToolCall {
                id: "call-2".into(),
                name: "describe_file".into(),
                invalid: None,
                arguments: serde_json::json!({
                    "path": "research/L0.0/orphan.full.md",
                    "purpose": "the whole converted paper"
                }),
            },
        )
        .await;
    let message = orphan
        .err()
        .map(|error| error.to_string())
        .unwrap_or_default();
    assert!(message.contains("nothing digests it yet"), "{message}");

    let _ = std::fs::remove_dir_all(&root);
    Ok(())
}

#[tokio::test]
async fn a_refresh_says_how_many_originals_it_passed_over() -> Result<()> {
    // Without it the caller sees a folder holding sources and an index
    // listing none of them, and its next move is to describe each in turn.
    let root =
        std::env::temp_dir().join(format!("math-agent-refresh-skips-{}", std::process::id()));
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(root.join("research/L0.0")).expect("workspace is creatable");
    let root = root.canonicalize().expect("workspace resolves");
    std::fs::write(root.join("research/L0.0/a.full.md"), "full").expect("original is writable");
    std::fs::write(root.join("research/L0.0/b.full.md"), "full").expect("original is writable");
    let documents = super::super::documents::WorkspaceDocuments::new(root.clone())?;
    let tools = super::FolderIndexTool::all(&documents);
    let tool = tools
        .iter()
        .find(|tool| tool.name() == "refresh_index")
        .expect("refresh_index is registered");

    let result = tool
        .call(
            &(),
            crate::agent::ToolCall {
                id: "call-1".into(),
                name: "refresh_index".into(),
                invalid: None,
                arguments: serde_json::json!({ "path": "research" }),
            },
        )
        .await?;
    assert!(
        result.content.contains("2 source full text"),
        "{}",
        result.content
    );
    assert!(
        result.content.contains("never indexed"),
        "{}",
        result.content
    );
    let _ = std::fs::remove_dir_all(&root);
    Ok(())
}

#[test]
fn a_row_written_as_a_wikilink_still_names_its_file() {
    // A live research index came back with every row keyed
    // `L2/[[rank_lehmer]]`, because the tree tells agents to link notes that
    // way. Every row then matched nothing on disk and the next refresh
    // dropped twelve descriptions as stale.
    let index = "| File | Purpose |\n| --- | --- |\n\
                 | L2.0/[[rank_lehmer]] | Lehmer digits are the lex rank |\n\
                 | L2.0/[[mechanism_pair_inversions]]* | **Core**: gap-affine probabilities |\n\
                 | `L1.0/paper.md` | the ordinary spelling still works |\n";
    let parsed = parse(index);
    assert_eq!(
        parsed.get("L2.0/rank_lehmer.md").map(String::as_str),
        Some("Lehmer digits are the lex rank")
    );
    assert_eq!(
        parsed
            .get("L2.0/mechanism_pair_inversions.md")
            .map(String::as_str),
        Some("**Core**: gap-affine probabilities")
    );
    assert_eq!(
        parsed.get("L1.0/paper.md").map(String::as_str),
        Some("the ordinary spelling still works")
    );
}

#[test]
fn an_index_is_never_a_row_in_another_index() {
    // `file_names` reports a tree's levels as `L1/paper.md`, so a whole-name
    // comparison against `INDEX.md` stops catching `L0/INDEX.md`. A live
    // research index grew rows for two indexes nobody could describe.
    for name in ["INDEX.md", "L0.0/INDEX.md", "L1.2/INDEX.md"] {
        assert_eq!(
            name.rsplit('/').next(),
            Some(INDEX_FILE),
            "{name} must be recognised as an index"
        );
    }
}

#[test]
fn a_synthesis_survives_the_refresh_that_rewrites_the_table_beneath_it() {
    // `research/INDEX.md` is the root of the summary tree, so a refresh that
    // re-derives the file list must not take the fold down with it.
    let folded = "Establishes the bound. See [the source](paper.md).";
    let first = render("research", &entries(&[("paper.md", "a source")]), folded);
    assert_eq!(brief(&first), folded);

    let refreshed = render(
        "research",
        &entries(&[("paper.md", "a source"), ("later.md", "another")]),
        &brief(&first),
    );
    assert_eq!(brief(&refreshed), folded);
    assert!(refreshed.contains("`later.md`"), "{refreshed}");
}

#[test]
fn an_index_that_never_carried_a_synthesis_reads_as_carrying_none() {
    assert_eq!(brief("# Index — notes\n\n| File | Purpose |\n"), "");
    // An opening marker with no close is a half-written file, not a synthesis
    // running to the end of the table.
    assert_eq!(brief("# Index\n\n<!-- brief -->\nlost"), "");
}

#[test]
fn an_undescribed_file_is_marked_rather_than_left_blank() {
    let rendered = render("research", &entries(&[("paper.md", "")]), "");
    assert!(rendered.contains("_(undescribed)_"), "{rendered}");
    assert!(rendered.contains("# Index — research"), "{rendered}");
}

#[test]
fn an_empty_folder_still_renders_a_usable_table() {
    let rendered = render("notes", &BTreeMap::new(), "");
    assert!(rendered.contains("This folder is empty"), "{rendered}");
    // The placeholder must not be a table row: parsed back it would become a
    // file the next refresh carries forward as though it existed.
    assert_eq!(parse(&rendered).len(), 0, "{rendered}");
}

#[test]
fn a_path_resolves_to_the_index_beside_it() {
    assert_eq!(split("research/papers/pell.md").0, "research/papers");
    assert_eq!(split("research/papers/pell.md").1, "pell.md");
    assert_eq!(split("solution.py"), (String::new(), "solution.py".into()));
    assert_eq!(
        split("./solution.py"),
        (String::new(), "solution.py".into())
    );

    assert_eq!(index_for("research"), format!("research/{INDEX_FILE}"));
    assert_eq!(index_for(""), INDEX_FILE);
}

#[test]
fn naming_the_mount_point_from_inside_it_resolves_to_the_folder_meant() {
    // A live run failed three refreshes in a row on exactly these spellings.
    assert_eq!(folder_name("workspace"), "");
    assert_eq!(folder_name("workspace/toolkits"), "toolkits");
    assert_eq!(folder_name("workspace/research"), "research");
    assert_eq!(folder_name("/workspace/research"), "research");
    assert_eq!(folder_name("research"), "research");
    // `.` is how a model asks for the folder it is already in.
    assert_eq!(folder_name("."), "");
    assert_eq!(folder_name("./"), "");
    assert_eq!(folder_name("/workspace"), "");
    // The root index is what `workspace` should have named all along.
    assert_eq!(index_for(&folder_name("workspace")), INDEX_FILE);
    assert_eq!(
        split("workspace/toolkits/frames.py"),
        ("toolkits".into(), "frames.py".into())
    );
}

#[tokio::test]
async fn the_workspace_root_can_be_refreshed_by_every_spelling_of_itself() -> Result<()> {
    // A live organizer lost its root refresh to this: the front door normalises
    // `.` to the empty string, and the folder listing turned it straight back
    // into `.`, which the path checker refuses as traversal. Every spelling an
    // agent standing in /workspace would reach for has to mean the same folder.
    let root = std::env::temp_dir().join(format!("math-agent-root-refresh-{}", std::process::id()));
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(&root).expect("temporary workspace is creatable");
    let root = root.canonicalize().expect("workspace resolves");
    std::fs::write(root.join("solution.py"), "print(1)").expect("a file is writable");
    let documents = super::super::documents::WorkspaceDocuments::new(root.clone())?;
    let tools = super::FolderIndexTool::all(&documents);
    let tool = tools
        .iter()
        .find(|tool| tool.name() == "refresh_index")
        .expect("refresh_index is registered");

    for spelling in [".", "", "/workspace", "workspace", "./"] {
        let result = tool
            .call(
                &(),
                crate::agent::ToolCall {
                    id: "call-1".into(),
                    name: "refresh_index".into(),
                    invalid: None,
                    arguments: serde_json::json!({ "path": spelling }),
                },
            )
            .await?;
        assert!(
            result.content.contains("solution.py") || result.content.contains("1 files"),
            "`{spelling}` must name the workspace root, got: {}",
            result.content
        );
    }
    let _ = std::fs::remove_dir_all(&root);
    Ok(())
}
