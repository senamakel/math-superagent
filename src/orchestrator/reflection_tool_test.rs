//! Tests that the parsed counters are the state graph's counters.
#![allow(clippy::expect_used)]

use std::path::Path;

use super::*;

fn call(arguments: Value) -> ToolCall {
    ToolCall {
        id: "t".into(),
        name: "parse_reflection".into(),
        arguments,
        invalid: None,
    }
}

async fn parse(reflection: &str, state: Value, last_attempt: &str) -> Value {
    ParseReflection::new(None)
        .call(
            &(),
            call(json!({
                "reflection": reflection,
                "state": state,
                "last_attempt": last_attempt,
                "problem": "a problem",
            })),
        )
        .await
        .expect("a reflection parses")
        .raw
        .expect("the counters are published structurally")
}

fn zeroed() -> Value {
    json!({
        "attempts": 1, "solved": false, "unproductive": 0, "blocked": 0,
        "computational": 0, "unverified": 0, "restarts": 0
    })
}

/// The property the whole design rests on: the tool calls `record_verdict`, so
/// its counters and the state graph's are identical by construction. This
/// checks the two really do agree rather than assuming the wiring is right.
#[tokio::test]
async fn the_tool_and_the_state_graph_agree_on_every_counter() {
    let reflections = [
        "VERDICT: SOLVED\nPROGRESS: YES\nKIND: MATHEMATICAL\nLESSON: done",
        "VERDICT: UNSOLVED\nPROGRESS: NO\nLESSON: stuck",
        "VERDICT: UNVERIFIED\nPROGRESS: YES\nKIND: MATHEMATICAL",
        "VERDICT: SOLVED\nPROGRESS: NO",
        "VERDICT: UNSOLVED\nPROGRESS: YES\nKIND: COMPUTATIONAL",
        "nothing parseable here at all",
    ];
    for reflection in reflections {
        // The state graph's own path.
        let mut expected = SolutionState::new("a problem");
        expected.attempts = 1;
        expected.last_attempt = "the attempt".to_string();
        let progressed = record_verdict(reflection, None, None, &mut expected);

        let parsed = parse(reflection, zeroed(), "the attempt").await;
        assert_eq!(parsed["solved"], json!(expected.solved), "{reflection}");
        assert_eq!(
            parsed["unproductive"],
            json!(expected.unproductive),
            "{reflection}"
        );
        assert_eq!(parsed["blocked"], json!(expected.blocked), "{reflection}");
        assert_eq!(
            parsed["computational"],
            json!(expected.computational),
            "{reflection}"
        );
        assert_eq!(
            parsed["unverified"],
            json!(expected.unverified),
            "{reflection}"
        );
        assert_eq!(parsed["progressed"], json!(progressed), "{reflection}");
    }
}

/// The fold in `workflow.rs` reads a fixed set of keys off this tool. A key it
/// expects and this never emits resolves to null and silently freezes that
/// counter for the whole run.
#[tokio::test]
async fn every_counter_the_fold_reads_is_published() {
    let parsed = parse("VERDICT: UNSOLVED\nPROGRESS: YES", zeroed(), "").await;
    for counter in COUNTERS {
        assert!(
            parsed.get(counter).is_some(),
            "`{counter}` is folded but never published"
        );
    }
}

/// A provider failure is counted before progress is judged, or reflection on an
/// HTTP error registers as an unproductive attempt and drives the run into
/// diversifying — three more child runs into the same wall.
///
/// The detection is deliberately narrow: it needs the `[agent] failed:` wrapper
/// a failed delegation produces, not merely an error string somewhere in the
/// text, so an attempt that ran and *mentioned* a 403 is not mistaken for one
/// that never started.
#[tokio::test]
async fn a_provider_failure_in_the_attempt_is_counted_as_blocked() {
    let parsed = parse(
        "VERDICT: UNSOLVED\nPROGRESS: NO",
        zeroed(),
        // The wrapper shape `delegate` produces for a failed child, which is
        // what `provider_blocked` keys on — a bare error string in a real
        // report is an attempt that mentioned an error, not one that never ran.
        "[goals] failed: model error: HTTP 403: Key limit exceeded",
    )
    .await;
    assert_eq!(parsed["blocked"], json!(1), "{parsed}");
}

/// An unparsable reply must move nothing towards ending the run.
#[tokio::test]
async fn an_unreadable_reflection_declares_nothing() {
    let parsed = parse("the model said something else entirely", zeroed(), "").await;
    assert_eq!(parsed["solved"], json!(false));
    // Silence is not "scaling again": an unstated kind leaves the count alone.
    assert_eq!(parsed["computational"], json!(0));
}

/// Counters arrive from the accumulator and have to survive the round trip, or
/// every pass would restart the run's history from zero.
#[tokio::test]
async fn the_incoming_counters_are_carried_rather_than_reset() {
    let parsed = parse(
        "VERDICT: UNSOLVED\nPROGRESS: NO",
        json!({
            "attempts": 5, "solved": false, "unproductive": 2, "blocked": 0,
            "computational": 1, "unverified": 0, "restarts": 1
        }),
        "",
    )
    .await;
    assert_eq!(parsed["attempts"], json!(5));
    assert_eq!(parsed["restarts"], json!(1));
    // Consecutive, so no progress increments rather than resets.
    assert_eq!(parsed["unproductive"], json!(3));
}

#[tokio::test]
async fn a_call_without_a_reflection_is_refused() {
    let refused = ParseReflection::new(None)
        .call(&(), call(json!({ "state": zeroed() })))
        .await;
    assert!(refused.is_err());
}

#[test]
fn the_workspace_is_carried_for_the_disk_checks() {
    // Two of the three conditions on `solved` are questions about disk, so a
    // tool built without a workspace is the unit-test case, not the run's.
    let tool = ParseReflection::new(Some(PathBuf::from("/workspace")));
    assert_eq!(workspace_of(&tool), Some(Path::new("/workspace")));
}
