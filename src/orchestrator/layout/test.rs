//! Unit tests for workspace placement.

use super::*;

#[test]
fn the_root_keeps_the_runs_prose_and_its_configuration() {
    for name in [
        "GOAL.md",
        "MEMORY.md",
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
