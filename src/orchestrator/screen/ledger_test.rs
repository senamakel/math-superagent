use super::*;

fn workspace(name: &str) -> std::path::PathBuf {
    let root = std::env::temp_dir().join(format!("math-agent-screen-ledger-{name}"));
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(&root).expect("the fixture workspace must be creatable");
    root
}

fn entry(decision: &'static str) -> Entry {
    Entry {
        tool: "exa_search".to_string(),
        stage: Stage::Result,
        decision,
        detail: "term matched in 2400 characters".to_string(),
    }
}

#[test]
fn a_decision_reaches_both_ledgers() {
    let root = workspace("both");
    record(&root, &entry("denied"));

    let jsonl = std::fs::read_to_string(root.join("config/screen.jsonl"))
        .expect("the machine-readable ledger must exist");
    assert!(jsonl.contains(r#""tool":"exa_search""#));
    assert!(jsonl.contains(r#""decision":"denied""#));
    assert!(jsonl.contains(r#""stage":"result""#));

    let markdown = std::fs::read_to_string(root.join("research/SCREEN.md"))
        .expect("the human-readable ledger must exist");
    assert!(markdown.starts_with("# Screen ledger"));
    assert!(markdown.contains("| `exa_search` | result | denied |"));
}

#[test]
fn the_markdown_header_is_written_once() {
    let root = workspace("header-once");
    record(&root, &entry("denied"));
    record(&root, &entry("denied-by-adjudicator"));

    let markdown = std::fs::read_to_string(root.join("research/SCREEN.md"))
        .expect("the human-readable ledger must exist");
    assert_eq!(
        markdown.matches("# Screen ledger").count(),
        1,
        "appending a second row must not repeat the header"
    );
    assert_eq!(
        markdown.lines().filter(|line| line.contains("exa_search")).count(),
        2
    );
}

#[test]
fn the_ledger_never_records_the_matched_term() {
    // The ledger is inside the container and the run can read it. Writing the
    // matched term here would put the withheld name into the workspace, which
    // is what hashing the compiled blocklist exists to prevent.
    let root = workspace("no-term");
    record(&root, &entry("denied"));
    let jsonl = std::fs::read_to_string(root.join("config/screen.jsonl"))
        .expect("the machine-readable ledger must exist");
    let markdown = std::fs::read_to_string(root.join("research/SCREEN.md"))
        .expect("the human-readable ledger must exist");
    for text in [&jsonl, &markdown] {
        assert!(
            !text.contains("de Grey") && !text.contains("term=") && !text.contains("matched `"),
            "no ledger may carry the term itself"
        );
    }
}

#[test]
fn a_pipe_in_the_detail_does_not_break_the_table() {
    let root = workspace("pipe");
    record(
        &root,
        &Entry {
            tool: "download_document".to_string(),
            stage: Stage::Arguments,
            decision: "denied-host",
            detail: "host `a|b`".to_string(),
        },
    );
    let markdown = std::fs::read_to_string(root.join("research/SCREEN.md"))
        .expect("the human-readable ledger must exist");
    let row = markdown
        .lines()
        .find(|line| line.contains("download_document"))
        .expect("the row must be written");
    assert_eq!(
        row.matches('|').count(),
        6,
        "a five-column row has exactly six pipes, so the detail must be escaped: {row}"
    );
}

#[test]
fn a_missing_workspace_directory_is_created() {
    let root = workspace("nested");
    // `config/` and `research/` do not exist yet; the ledger must make them
    // rather than dropping the decision.
    record(&root, &entry("denied"));
    assert!(root.join("config/screen.jsonl").is_file());
    assert!(root.join("research/SCREEN.md").is_file());
}
