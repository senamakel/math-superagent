//! Unit tests for the shape of `code/`.
#![allow(clippy::expect_used)]

use std::fs;
use std::path::PathBuf;

use super::*;

/// Writes a file and every folder above it.
fn write(root: &Path, relative: &str, body: &str) {
    let path = root.join(relative);
    if let Some(parent) = path.parent() {
        let _ = fs::create_dir_all(parent);
    }
    let _ = fs::write(path, body);
}

/// A workspace under the crate's target directory, named for its test.
fn empty(name: &str) -> PathBuf {
    let root = Path::new(env!("CARGO_MANIFEST_DIR"))
        .join("target")
        .join("code-layout-tests")
        .join(name);
    let _ = fs::remove_dir_all(&root);
    let _ = fs::create_dir_all(&root);
    root
}

/// A workspace holding nothing but an empty `code/`.
fn workspace(name: &str) -> PathBuf {
    let root = empty(name);
    let _ = fs::create_dir_all(root.join(CODE_DIR));
    root
}

#[test]
fn a_tidy_folder_asks_for_nothing() {
    let root = workspace();
    write(root.path(), "code/INDEX.md", "# Index");
    write(root.path(), "code/brute.py", "def count(n):\n    return n\n");
    assert!(plan(root.path()).is_empty());
    assert!(briefing(root.path()).is_none());
}

#[test]
fn only_top_level_definitions_count_as_a_routine() {
    // A method and a closure are not importable on their own, so neither is
    // the thing this module is looking for.
    let source = "class Walker:\n    def step(self):\n        def inner():\n            pass\n";
    assert_eq!(symbols(source), vec!["Walker".to_string()]);
    assert_eq!(symbols("async def fetch(url):\n    pass\n"), vec!["fetch"]);
    // Every script has an entry point and a test is named for what it tests.
    assert!(symbols("def main():\n    pass\n").is_empty());
    assert!(symbols("def test_count():\n    pass\n").is_empty());
    assert!(symbols("def _helper():\n    pass\n").is_empty());
    // A file defining the same name twice has still only defined it once.
    assert_eq!(symbols("def f(n):\n    pass\ndef f(n, m):\n    pass\n"), ["f"]);
}

#[test]
fn a_routine_written_out_three_times_is_the_first_thing_reported() {
    let root = workspace();
    write(root.path(), "code/INDEX.md", "# Index");
    for name in ["aj", "aj2", "fit"] {
        write(
            root.path(),
            &format!("code/{name}.py"),
            "def lex_ranks(n):\n    return {}\n\ndef main():\n    pass\n",
        );
    }
    let tasks = plan(root.path());
    assert_eq!(
        tasks.first().map(|task| task.fault.clone()),
        Some(Fault::Duplicated {
            symbol: "lex_ranks".to_string(),
            files: vec![
                "code/aj.py".to_string(),
                "code/aj2.py".to_string(),
                "code/fit.py".to_string(),
            ],
            shelved: false,
        })
    );
    let brief = briefing(root.path()).expect("a duplicated routine is reported");
    assert!(brief.contains("lex_ranks"), "{brief}");
    assert!(brief.contains(LIB_DIR), "{brief}");
}

#[test]
fn two_copies_are_a_program_and_its_oracle() {
    // `code/AGENTS.md` asks for the naive program to be kept as the oracle the
    // fast one is checked against, so the second definition is the arrangement
    // working rather than the fault.
    let root = workspace();
    write(root.path(), "code/INDEX.md", "# Index");
    for name in ["brute", "solution"] {
        write(
            root.path(),
            &format!("code/{name}.py"),
            "def count(n):\n    return n\n",
        );
    }
    assert!(plan(root.path()).is_empty());
}

#[test]
fn a_copy_of_something_already_shelved_is_reported_as_such() {
    let root = workspace();
    write(root.path(), "code/INDEX.md", "# Index");
    write(root.path(), "code/lib/INDEX.md", "# Index");
    write(
        root.path(),
        "code/lib/perms.py",
        "def lex_ranks(n):\n    return {}\n",
    );
    for name in ["aj", "fit"] {
        write(
            root.path(),
            &format!("code/{name}.py"),
            "def lex_ranks(n):\n    return {}\n",
        );
    }
    let brief = briefing(root.path()).expect("the ignored shelf is reported");
    assert!(brief.contains("already has it"), "{brief}");
}

#[test]
fn a_folder_past_the_fan_out_is_asked_to_group() {
    let root = workspace();
    write(root.path(), "code/INDEX.md", "# Index");
    for index in 0..=LOOSE {
        write(
            root.path(),
            &format!("code/probe{index}.py"),
            &format!("def probe{index}(n):\n    return n\n"),
        );
    }
    let brief = briefing(root.path()).expect("an ungrouped folder is reported");
    assert!(brief.contains("Group them"), "{brief}");
    // Exactly the fan-out is still a listing a reader takes in at a glance.
    fs::remove_file(root.path().join(format!("code/probe{LOOSE}.py")))
        .expect("the test workspace is writable");
    assert!(plan(root.path()).is_empty());
}

#[test]
fn what_a_program_produced_is_not_a_program() {
    // `code/out/` holds captures, and a `.py` file emitted by a run is not
    // source the next agent is meant to group or import.
    let root = workspace();
    write(root.path(), "code/INDEX.md", "# Index");
    for index in 0..=LOOSE {
        write(
            root.path(),
            &format!("code/out/generated{index}.py"),
            "def probe(n):\n    return n\n",
        );
    }
    write(
        root.path(),
        "code/__pycache__/cached.py",
        "def probe(n):\n    return n\n",
    );
    assert!(plan(root.path()).is_empty());
}

#[test]
fn a_folder_of_programs_with_no_index_is_reported_last() {
    let root = workspace();
    write(root.path(), "code/INDEX.md", "# Index");
    write(
        root.path(),
        "code/chains/probe.py",
        "def probe(n):\n    return n\n",
    );
    let tasks = plan(root.path());
    assert_eq!(
        tasks.first().map(|task| task.fault.clone()),
        Some(Fault::Unindexed {
            folder: "code/chains".to_string(),
            programs: 1,
        })
    );
    // A duplicated routine outranks it: an index that is merely missing costs
    // legibility, where two copies of a routine can disagree.
    for name in ["a", "b", "c"] {
        write(
            root.path(),
            &format!("code/chains/{name}.py"),
            "def walk(n):\n    return n\n",
        );
    }
    let tasks = plan(root.path());
    assert!(
        matches!(
            tasks.first().map(|task| &task.fault),
            Some(Fault::Duplicated { .. })
        ),
        "{tasks:?}"
    );
}

#[test]
fn a_workspace_without_a_code_folder_is_not_a_fault() {
    let root = TempDir::new().expect("a temporary directory is available");
    assert!(plan(root.path()).is_empty());
    assert!(briefing(root.path()).is_none());
}
