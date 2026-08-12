//! Unit tests for workspace placement.
#![allow(clippy::expect_used)]

use super::*;

#[test]
fn the_root_keeps_the_runs_prose_and_its_configuration() {
    for name in [
        "GOAL.md",
        "SCRATCHPAD.md",
        "solution.md",
        "CONTEXT.md",
        "AGENTS.md",
        "problem.md",
    ] {
        assert_eq!(placed(name), name);
    }
}

#[test]
fn the_runs_plumbing_is_not_the_roots_business() {
    // Configuration, the trace, the document index and the source URL are
    // things the runtime writes and reads. None of them is work, and none of
    // them earns a line in the listing every agent reads first.
    assert_eq!(placed("config.toml"), "config/config.toml");
    assert_eq!(placed("problem.url"), "config/problem.url");
    assert_eq!(placed("trace.jsonl"), "config/trace.jsonl");
}

#[test]
fn a_program_written_to_the_root_is_filed_under_code() {
    // One live run reached thirty-one of these at the root.
    assert_eq!(placed("brute.py"), "code/brute.py");
    assert_eq!(placed("solution.py"), "code/solution.py");
    assert_eq!(placed("check.sh"), "code/check.sh");
    assert_eq!(placed("solve.ipynb"), "code/solve.ipynb");
    // Case is not a placement decision.
    assert_eq!(placed("Brute.PY"), "code/Brute.PY");
}

#[test]
fn what_a_program_produced_is_kept_apart_from_the_program() {
    assert_eq!(placed("fdtable.json"), "code/out/fdtable.json");
    assert_eq!(placed("explore.out.txt"), "code/out/explore.out.txt");
    assert_eq!(placed("results.csv"), "code/out/results.csv");
    // An extension nobody anticipated is still not the root's problem.
    assert_eq!(placed("table.parquet"), "code/out/table.parquet");
    assert_eq!(placed("notes"), "code/out/notes");
}

#[test]
fn a_path_naming_a_folder_is_left_where_the_caller_put_it() {
    // An agent that said where something goes knows something this module
    // does not.
    assert_eq!(placed("research/L1/paper.md"), "research/L1/paper.md");
    assert_eq!(placed("code/lib/pell.py"), "code/lib/pell.py");
    assert_eq!(placed("code/chains/probe.py"), "code/chains/probe.py");
    assert_eq!(placed("code/out/run.log"), "code/out/run.log");
    assert_eq!(
        placed("experiments/first/try.py"),
        "experiments/first/try.py"
    );
}

#[test]
fn the_common_spellings_of_the_root_do_not_survive_into_a_folder_name() {
    assert_eq!(placed("/workspace/brute.py"), "code/brute.py");
    assert_eq!(placed("./brute.py"), "code/brute.py");
    assert_eq!(placed("/brute.py"), "code/brute.py");
    assert_eq!(placed("  GOAL.md  "), "GOAL.md");
}

#[test]
fn a_moved_file_is_reported_and_an_unmoved_one_is_not() {
    // A model not told where its file went writes the next one to the same
    // place and then cannot read either back.
    let moved = note("brute.py", &placed("brute.py"));
    assert!(moved.contains("code/brute.py"), "{moved}");
    assert!(moved.contains("code/out"), "{moved}");
    assert_eq!(note("GOAL.md", &placed("GOAL.md")), "");
}

#[tokio::test]
async fn a_program_written_through_the_shell_is_filed_after_the_command() {
    // The hole the write path cannot close: a heredoc and a redirect reach the
    // filesystem directly, so the tool sees a command and an exit code. One
    // live workspace collected six root programs in nineteen minutes this way.
    let root = std::env::temp_dir().join(format!("math-agent-sweep-{}", std::process::id()));
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(&root).expect("the sweep workspace is creatable");
    for name in ["dyadic.py", "table.json", "GOAL.md", ".keep"] {
        std::fs::write(root.join(name), "x").expect("a workspace file is writable");
    }

    let moved = sweep(&root).await;

    assert!(root.join("code/dyadic.py").is_file(), "a program is filed");
    assert!(
        root.join("code/out/table.json").is_file(),
        "what a program produced is filed apart from it"
    );
    assert!(root.join("GOAL.md").is_file(), "the run's prose stays put");
    assert!(
        root.join(".keep").is_file(),
        "machinery is not the run's work"
    );
    assert_eq!(moved.moved.len(), 2, "{:?}", moved.moved);

    let note = swept_note(&moved);
    assert!(note.contains("code/dyadic.py"), "{note}");
    assert!(
        swept_note(&Swept::default()).is_empty(),
        "a command that moved nothing says nothing"
    );
    let _ = std::fs::remove_dir_all(&root);
}

#[tokio::test]
async fn a_sweep_never_overwrites_a_file_already_filed() {
    // A file carrying a result must not be replaced by one that happens to
    // share its name — the earlier run's output is the record of how an answer
    // was reached.
    let root = std::env::temp_dir().join(format!("math-agent-sweep-keep-{}", std::process::id()));
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(root.join("code")).expect("the sweep workspace is creatable");
    std::fs::write(root.join("code/solve.py"), "the real one")
        .expect("a filed program is writable");
    std::fs::write(root.join("solve.py"), "a later stray").expect("a stray is writable");

    let moved = sweep(&root).await;

    assert!(moved.moved.is_empty(), "{:?}", moved.moved);
    // Silence would leave the stray at the root for the rest of the run with
    // nothing to say which of the two files is current.
    let note = swept_note(&moved);
    assert!(note.contains("the filed name is taken"), "{note}");
    assert!(note.contains("solve.py"), "{note}");
    assert_eq!(
        std::fs::read_to_string(root.join("code/solve.py")).expect("the filed program is readable"),
        "the real one"
    );
    assert!(
        root.join("solve.py").is_file(),
        "the stray is left in place"
    );
    let _ = std::fs::remove_dir_all(&root);
}
