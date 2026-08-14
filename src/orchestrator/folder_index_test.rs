//! Unit tests for the per-folder index.
#![allow(clippy::expect_used)]

use std::collections::BTreeMap;

use crate::agent::Result;

use super::{INDEX_FILE, folder_name, index_for, parse, render, split};

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

    let parsed = parse(&render("", &original));

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
fn an_undescribed_file_is_marked_rather_than_left_blank() {
    let rendered = render("research", &entries(&[("paper.md", "")]));
    assert!(rendered.contains("_(undescribed)_"), "{rendered}");
    assert!(rendered.contains("# Index — research"), "{rendered}");
}

#[test]
fn an_empty_folder_still_renders_a_usable_table() {
    let rendered = render("notes", &BTreeMap::new());
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
    // A live filing pass lost its root refresh to this: the front door normalises
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

#[test]
fn knowledge_folders_refuse_index_calls() {
    for folder in ["research", "learning", "reflections"] {
        assert!(super::index_allowed(folder).is_err(), "{folder}");
    }
}

/// A search catalogues itself, so nothing may file a second catalogue over it.
///
/// `SEARCH.md` is derived from the score ledger and carries what each program
/// scored, which is the only fact anyone wants about a candidate. An `INDEX.md`
/// beside it would answer the same question worse, and would cost hundreds of
/// `describe_file` calls on a role already measured spending 60% of a run's
/// model calls on filing.
#[test]
fn a_search_tree_is_catalogued_by_its_board_rather_than_an_index() {
    for folder in [
        "code/search",
        "code/search/capset",
        "code/search/capset/candidates",
    ] {
        let refused = super::index_allowed(folder);
        assert!(refused.is_err(), "`{folder}` must not take an INDEX.md");
    }
    // The rest of `code/` is unaffected: the toolkit index is what tells the
    // planners what has already been built and verified.
    assert!(super::index_allowed("code").is_ok());
    assert!(super::index_allowed("code/lib").is_ok());
}
