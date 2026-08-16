#![allow(clippy::expect_used)]

use serde_json::json;

use super::super::vcs::{ATTEMPTS_DIR, Git, TRUNK};
use super::{Kind, VcsTool};
use crate::agent::{Tool, ToolCall};

/// A workspace with a trunk commit and one candidate that changed two files.
async fn seeded(name: &str) -> std::path::PathBuf {
    let path = std::env::temp_dir().join(format!("vcs-tool-{name}"));
    let _ = std::fs::remove_dir_all(&path);
    std::fs::create_dir_all(path.join("code")).expect("the workspace is created");
    std::fs::write(path.join("code").join("solution.py"), "print('trunk')\n")
        .expect("the trunk program is written");

    let git = Git::history(&path);
    git.initialise().await.expect("history");
    git.stage_all().await.expect("staged");
    git.commit("seed").await.expect("committed");

    let checkout = path.join(ATTEMPTS_DIR).join("01");
    git.worktree_add(&checkout, "attempt/01", TRUNK)
        .await
        .expect("the candidate is branched");
    let candidate = Git::worktree(&path, &checkout);
    std::fs::write(
        checkout.join("code").join("solution.py"),
        "print('candidate')\n",
    )
    .expect("written");
    std::fs::write(checkout.join("SCRATCH.md"), "my own account\n").expect("written");
    candidate.stage_all().await.expect("staged");
    candidate.commit("try a sieve").await.expect("committed");
    path
}

fn call(name: &str, arguments: serde_json::Value) -> ToolCall {
    ToolCall {
        id: "call-1".into(),
        name: name.into(),
        invalid: None,
        arguments,
    }
}

async fn run(tool: &dyn Tool<()>, arguments: serde_json::Value) -> String {
    tool.call(&(), call(tool.name(), arguments))
        .await
        .expect("the tool returns a result")
        .content
}

fn pick(tools: &[std::sync::Arc<dyn Tool<()>>], name: &str) -> std::sync::Arc<dyn Tool<()>> {
    tools
        .iter()
        .find(|tool| tool.name() == name)
        .expect("the tool is registered")
        .clone()
}

#[test]
fn reading_and_writing_are_separate_grants() {
    // The whole point of the module: a role may be able to read every candidate
    // without being able to make one of them authoritative.
    let reading: Vec<&str> = Kind::READING.iter().map(|kind| kind.name()).collect();
    let writing: Vec<&str> = Kind::WRITING.iter().map(|kind| kind.name()).collect();
    assert!(reading.contains(&"attempt_diff"));
    assert!(!reading.contains(&"adopt_attempt"));
    assert!(writing.contains(&"adopt_attempt"));
    assert!(writing.contains(&"abandon_attempt"));
    for name in &reading {
        assert!(!writing.contains(name), "`{name}` is in both sets");
    }
}

#[tokio::test]
async fn a_reading_grant_does_not_carry_the_trunk_changing_tools() {
    let path = seeded("grants").await;
    let reading = VcsTool::reading(&path);
    let names: Vec<&str> = reading.iter().map(|tool| tool.name()).collect();
    assert_eq!(names.len(), 3);
    assert!(!names.contains(&"adopt_attempt"));

    let every = VcsTool::all(&path);
    let all: Vec<&str> = every.iter().map(|tool| tool.name()).collect();
    assert_eq!(all.len(), 5);
    assert!(all.contains(&"adopt_attempt"));
}

#[tokio::test]
async fn there_is_no_tool_that_runs_an_arbitrary_git_command() {
    // A `git` tool would be `execute_command` reachable by roles that were
    // deliberately never given a shell.
    let path = seeded("noexec").await;
    for tool in VcsTool::all(&path) {
        let name = tool.name();
        assert!(
            !name.contains("exec") && name != "git",
            "`{name}` looks like a general git escape hatch"
        );
        let schema = serde_json::to_string(&tool.schema().parameters).expect("the schema renders");
        assert!(
            !schema.contains("\"command\"") && !schema.contains("\"args\""),
            "`{name}` takes a command line: {schema}"
        );
    }
}

#[tokio::test]
async fn listing_names_each_candidate_and_whether_it_is_live() {
    let path = seeded("list").await;
    let listed = run(&*pick(&VcsTool::all(&path), "list_attempts"), json!({})).await;
    assert!(listed.contains("01"), "{listed}");
    assert!(listed.contains("try a sieve"), "{listed}");
    assert!(listed.contains("live"), "{listed}");
}

#[tokio::test]
async fn listing_an_empty_workspace_says_so_rather_than_failing() {
    let path = std::env::temp_dir().join("vcs-tool-empty");
    let _ = std::fs::remove_dir_all(&path);
    std::fs::create_dir_all(&path).expect("created");
    let listed = run(&*pick(&VcsTool::all(&path), "list_attempts"), json!({})).await;
    assert!(listed.contains("No candidates"), "{listed}");
}

#[tokio::test]
async fn a_stat_diff_summarises_and_a_full_diff_carries_the_change() {
    let path = seeded("diff").await;
    let tool = pick(&VcsTool::all(&path), "attempt_diff");

    let stat = run(&*tool, json!({ "attempt": "01", "stat": true })).await;
    assert!(stat.contains("solution.py"), "{stat}");
    assert!(!stat.contains("print('candidate')"), "a stat is not a diff");

    let full = run(&*tool, json!({ "attempt": "01" })).await;
    assert!(full.contains("print('candidate')"), "{full}");

    let narrowed = run(&*tool, json!({ "attempt": "01", "path": "SCRATCH.md" })).await;
    assert!(narrowed.contains("my own account"), "{narrowed}");
    assert!(
        !narrowed.contains("print('candidate')"),
        "a narrowed diff must not carry the other file: {narrowed}"
    );
}

#[tokio::test]
async fn an_attempt_id_may_be_given_with_or_without_its_prefix() {
    let path = seeded("prefix").await;
    let tool = pick(&VcsTool::all(&path), "attempt_log");
    let bare = run(&*tool, json!({ "attempt": "01" })).await;
    let prefixed = run(&*tool, json!({ "attempt": "attempt/01" })).await;
    assert!(bare.contains("try a sieve"), "{bare}");
    assert_eq!(bare, prefixed);
}

#[tokio::test]
async fn an_attempt_id_cannot_smuggle_a_ref_or_an_option() {
    let path = seeded("injection").await;
    let tool = pick(&VcsTool::all(&path), "attempt_diff");
    for hostile in [
        "../../refs/heads/work",
        "--upload-pack=touch /tmp/pwned",
        "work",
        "",
        "   ",
    ] {
        let result = tool
            .call(&(), call("attempt_diff", json!({ "attempt": hostile })))
            .await
            .expect("the tool returns a result");
        assert!(
            result.is_error(),
            "`{hostile}` was accepted as a candidate id: {}",
            result.content
        );
    }
}

#[tokio::test]
async fn a_path_that_leaves_the_workspace_is_refused() {
    let path = seeded("traversal").await;
    let tool = pick(&VcsTool::all(&path), "attempt_diff");
    for hostile in ["/etc/passwd", "../outside.txt", "code/../../escape"] {
        let result = tool
            .call(
                &(),
                call("attempt_diff", json!({ "attempt": "01", "path": hostile })),
            )
            .await
            .expect("the tool returns a result");
        assert!(result.is_error(), "`{hostile}` was accepted");
    }
}

#[tokio::test]
async fn adopting_takes_the_named_file_and_leaves_the_candidates_own_notes() {
    let path = seeded("adopt").await;
    let adopted = run(
        &*pick(&VcsTool::all(&path), "adopt_attempt"),
        json!({
            "attempt": "01",
            "paths": ["code/solution.py"],
            "reason": "twice as fast and agrees with the oracle"
        }),
    )
    .await;
    assert!(adopted.contains("adopted"), "{adopted}");

    assert_eq!(
        std::fs::read_to_string(path.join("code").join("solution.py")).expect("read"),
        "print('candidate')\n",
        "the named file must land in the trunk"
    );
    assert!(
        !path.join("SCRATCH.md").exists(),
        "the candidate's own account must not be adopted with it"
    );

    // The trunk records the decision, with the reason, as its own commit.
    let subject = Git::history(&path)
        .subject_of(TRUNK)
        .await
        .expect("the trunk has a head");
    assert!(subject.contains("adopt 01"), "{subject}");
    assert!(subject.contains("twice as fast"), "{subject}");
}

#[tokio::test]
async fn adopting_reports_a_path_the_candidate_never_touched() {
    // Otherwise a mistyped path reads as a successful adoption of a change that
    // never happened.
    let path = seeded("untouched").await;
    let adopted = run(
        &*pick(&VcsTool::all(&path), "adopt_attempt"),
        json!({
            "attempt": "01",
            "paths": ["code/solution.py", "SCRATCH.md"],
            "reason": "keeping both"
        }),
    )
    .await;
    assert!(!adopted.contains("was not changed"), "{adopted}");

    // A path the branch *has* but did not change is adopted, with a note: it
    // copies what the trunk already had, which is worth saying but not worth
    // refusing. `code/` existed at the branch point and the candidate left
    // `SCRATCH.md` alone in the trunk, so seed a file both sides share.
    let path = seeded("untouched2").await;
    let git = Git::history(&path);
    let shared = path.join("code").join("lib.py");
    std::fs::write(&shared, "shared\n").expect("written");
    git.stage_all().await.expect("staged");
    git.commit("shared helper").await.expect("committed");
    let checkout = path.join(ATTEMPTS_DIR).join("02");
    git.worktree_add(&checkout, "attempt/02", TRUNK)
        .await
        .expect("branched after the shared file exists");
    let candidate = Git::worktree(&path, &checkout);
    std::fs::write(checkout.join("code").join("solution.py"), "print('two')\n").expect("written");
    candidate.stage_all().await.expect("staged");
    candidate.commit("candidate 02").await.expect("committed");

    let adopted = run(
        &*pick(&VcsTool::all(&path), "adopt_attempt"),
        json!({
            "attempt": "02",
            "paths": ["code/solution.py", "code/lib.py"],
            "reason": "keeping"
        }),
    )
    .await;
    assert!(
        adopted.contains("code/lib.py") && adopted.contains("was not changed"),
        "an unchanged path must be reported: {adopted}"
    );
}

#[tokio::test]
async fn adopting_a_path_the_candidate_never_had_is_refused_before_anything_moves() {
    // git's own message for this names neither the branch nor a way forward,
    // and a bad path in a list of five must not leave the other four adopted.
    let path = seeded("absent-path").await;
    let result = pick(&VcsTool::all(&path), "adopt_attempt")
        .call(
            &(),
            call(
                "adopt_attempt",
                json!({
                    "attempt": "01",
                    "paths": ["code/solution.py", "code/nonexistent.py"],
                    "reason": "keeping"
                }),
            ),
        )
        .await
        .expect("the tool returns a result");
    assert!(result.is_error(), "{}", result.content);
    assert!(
        result.content.contains("nonexistent.py") && result.content.contains("attempt_diff"),
        "the refusal must name the path and the way to find the real ones: {}",
        result.content
    );
    assert_eq!(
        std::fs::read_to_string(path.join("code").join("solution.py")).expect("read"),
        "print('trunk')\n",
        "the good path in the same call must not have been adopted"
    );
}

#[tokio::test]
async fn adopting_needs_paths_and_a_reason() {
    let path = seeded("required").await;
    let tool = pick(&VcsTool::all(&path), "adopt_attempt");

    for arguments in [
        json!({ "attempt": "01", "paths": [], "reason": "because" }),
        json!({ "attempt": "01", "paths": ["code/solution.py"], "reason": "  " }),
    ] {
        let result = tool
            .call(&(), call("adopt_attempt", arguments.clone()))
            .await
            .expect("the tool returns a result");
        assert!(result.is_error(), "{arguments} was accepted");
    }
}

#[tokio::test]
async fn abandoning_removes_the_checkout_and_keeps_the_branch() {
    let path = seeded("abandon").await;
    let checkout = path.join(ATTEMPTS_DIR).join("01");
    assert!(checkout.is_dir());

    let closed = run(
        &*pick(&VcsTool::all(&path), "abandon_attempt"),
        json!({ "attempt": "01", "reason": "slower than 03 and no more accurate" }),
    )
    .await;
    assert!(closed.contains("closed"), "{closed}");
    assert!(!checkout.exists(), "the disk is reclaimed");

    // The work stays readable, which is the reason the branch is kept.
    let diff = run(
        &*pick(&VcsTool::all(&path), "attempt_diff"),
        json!({ "attempt": "01" }),
    )
    .await;
    assert!(diff.contains("print('candidate')"), "{diff}");
}

#[tokio::test]
async fn abandoning_needs_a_reason() {
    let path = seeded("noreason").await;
    // Omitting a declared-required field is refused by the schema, before the
    // handler runs; a blank one has to be refused by the handler.
    assert!(
        pick(&VcsTool::all(&path), "abandon_attempt")
            .call(&(), call("abandon_attempt", json!({ "attempt": "01" })))
            .await
            .is_err(),
        "a missing reason must not reach the handler"
    );
    let blank = pick(&VcsTool::all(&path), "abandon_attempt")
        .call(
            &(),
            call("abandon_attempt", json!({ "attempt": "01", "reason": "  " })),
        )
        .await
        .expect("the tool returns a result");
    assert!(blank.is_error(), "{}", blank.content);
}

#[tokio::test]
async fn a_missing_candidate_is_reported_rather_than_raised() {
    // The model can act on "that branch does not exist"; it cannot act on a
    // failed turn.
    let path = seeded("missing").await;
    let result = pick(&VcsTool::all(&path), "attempt_diff")
        .call(&(), call("attempt_diff", json!({ "attempt": "99" })))
        .await
        .expect("the tool returns a result rather than erroring the turn");
    assert!(result.is_error());
    assert!(!result.content.is_empty());
}

#[test]
fn every_tool_refuses_arguments_it_does_not_declare() {
    let path = std::env::temp_dir().join("vcs-tool-schema");
    for tool in VcsTool::all(&path) {
        let schema = tool.schema().parameters;
        assert_eq!(
            schema.get("additionalProperties"),
            Some(&serde_json::Value::Bool(false)),
            "`{}` accepts undeclared arguments",
            tool.name()
        );
    }
}
