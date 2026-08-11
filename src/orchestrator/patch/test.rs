//! Unit tests for the `apply_patch` envelope.
#![allow(clippy::expect_used)]
#![allow(clippy::panic)]

use super::{FileOp, apply_hunk, parse};

fn update_hunks(op: &FileOp) -> &[super::Hunk] {
    match op {
        FileOp::Update { hunks, .. } => hunks,
        _ => panic!("expected an update operation"),
    }
}

#[test]
fn parses_the_documented_multi_operation_example() {
    let ops = parse(
        "*** Begin Patch\n\
         *** Add File: hello.txt\n\
         +Hello world\n\
         *** Update File: src/app.py\n\
         *** Move to: src/main.py\n\
         @@ def greet():\n\
         -print(\"Hi\")\n\
         +print(\"Hello, world!\")\n\
         *** Delete File: obsolete.txt\n\
         *** End Patch\n",
    )
    .expect("the documented example parses");

    assert_eq!(ops.len(), 3);
    assert_eq!(
        ops[0],
        FileOp::Add {
            path: "hello.txt".into(),
            contents: "Hello world\n".into()
        }
    );
    match &ops[1] {
        FileOp::Update {
            path,
            move_to,
            hunks,
        } => {
            assert_eq!(path, "src/app.py");
            assert_eq!(move_to.as_deref(), Some("src/main.py"));
            assert_eq!(hunks.len(), 1);
        }
        other => panic!("expected an update, got {other:?}"),
    }
    assert_eq!(
        ops[2],
        FileOp::Delete {
            path: "obsolete.txt".into()
        }
    );
}

#[test]
fn a_context_line_missing_its_leading_space_is_still_read_as_context() {
    // The most common way a small model malforms this envelope. The reading is
    // unambiguous, so accepting it saves a wasted turn.
    let ops = parse(
        "*** Begin Patch\n\
         *** Update File: solution.py\n\
         @@\n\
         def peel(p, q):\n\
         -    return None\n\
         +    return p - q\n\
         *** End Patch\n",
    )
    .expect("the patch parses");
    let before = "def peel(p, q):\n    return None\n";

    let after =
        apply_hunk("solution.py", before, &update_hunks(&ops[0])[0]).expect("the hunk applies");
    assert_eq!(after, "def peel(p, q):\n    return p - q\n");
}

#[test]
fn a_hunk_rewrites_only_the_lines_it_names() {
    let ops = parse(
        "*** Begin Patch\n\
         *** Update File: solution.py\n\
         @@\n\
         \x20def peel(p, q):\n\
         -    return None\n\
         +    return p - q\n\
         *** End Patch\n",
    )
    .expect("the patch parses");
    let before = "def peel(p, q):\n    return None\n\nprint(peel(3, 1))\n";

    let after =
        apply_hunk("solution.py", before, &update_hunks(&ops[0])[0]).expect("the hunk applies");

    assert_eq!(
        after,
        "def peel(p, q):\n    return p - q\n\nprint(peel(3, 1))\n"
    );
}

#[test]
fn an_ambiguous_hunk_is_refused_rather_than_guessed() {
    // Landing in the wrong place produces a program that runs and computes the
    // wrong thing, which is worse than a failed tool call.
    let ops = parse(
        "*** Begin Patch\n\
         *** Update File: t.py\n\
         @@\n\
         -    total = 0\n\
         +    total = 1\n\
         *** End Patch\n",
    )
    .expect("the patch parses");
    let before = "def a():\n    total = 0\ndef b():\n    total = 0\n";

    let error = apply_hunk("t.py", before, &update_hunks(&ops[0])[0])
        .expect_err("an ambiguous hunk is refused");
    assert!(format!("{error}").contains("matches 2 places"), "{error}");
}

#[test]
fn a_header_selects_between_otherwise_identical_contexts() {
    let ops = parse(
        "*** Begin Patch\n\
         *** Update File: t.py\n\
         @@ def b():\n\
         -    total = 0\n\
         +    total = 1\n\
         *** End Patch\n",
    )
    .expect("the patch parses");
    let before = "def a():\n    total = 0\ndef b():\n    total = 0\n";

    let after = apply_hunk("t.py", before, &update_hunks(&ops[0])[0]).expect("the hunk applies");
    assert_eq!(after, "def a():\n    total = 0\ndef b():\n    total = 1\n");
}

#[test]
fn context_that_does_not_match_is_reported_with_the_lines_it_wanted() {
    let ops = parse(
        "*** Begin Patch\n\
         *** Update File: t.py\n\
         @@\n\
         -    missing = True\n\
         +    missing = False\n\
         *** End Patch\n",
    )
    .expect("the patch parses");

    let error = apply_hunk("t.py", "print(1)\n", &update_hunks(&ops[0])[0])
        .expect_err("a hunk that matches nothing fails");
    let rendered = format!("{error}");
    assert!(rendered.contains("was not found"), "{rendered}");
    // The model has to see what it asked for to correct itself.
    assert!(rendered.contains("missing = True"), "{rendered}");
}

#[test]
fn malformed_envelopes_are_rejected_with_the_reason() {
    for (patch, expected) in [
        ("*** Update File: a.py\n@@\n-x\n+y\n", "must start with"),
        ("*** Begin Patch\n*** Add File: a.py\n+x\n", "must end with"),
        ("*** Begin Patch\n*** End Patch\n", "no file operations"),
        (
            "*** Begin Patch\nnonsense\n*** End Patch\n",
            "expected a file header",
        ),
        (
            "*** Begin Patch\n*** Update File: a.py\n*** End Patch\n",
            "no `@@` hunk",
        ),
        (
            "*** Begin Patch\n*** Add File: /etc/passwd\n+x\n*** End Patch\n",
            "is absolute",
        ),
        (
            "*** Begin Patch\n*** Add File: a.py\n+x\n*** Delete File: a.py\n*** End Patch\n",
            "appears twice",
        ),
    ] {
        let error = parse(patch).expect_err("the malformed patch is rejected");
        assert!(
            format!("{error}").contains(expected),
            "expected `{expected}` in `{error}`"
        );
    }
}

#[test]
fn a_workspace_prefixed_path_is_accepted_rather_than_refused() {
    // The model is told its working directory is /workspace and writes the
    // absolute form; refusing it would spend a turn on punctuation.
    let ops = parse("*** Begin Patch\n*** Delete File: /workspace/a.py\n*** End Patch\n")
        .expect("the prefixed path is accepted");
    assert_eq!(
        ops[0],
        FileOp::Delete {
            path: "a.py".into()
        }
    );
}
