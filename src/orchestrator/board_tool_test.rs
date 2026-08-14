use serde_json::json;

use super::BoardTool;
use crate::agent::{Tool as _, ToolCall};
use crate::orchestrator::board;
use crate::orchestrator::documents::WorkspaceDocuments;

/// Builds a tool over a throwaway workspace.
fn tool(root: &std::path::Path, from: &str) -> BoardTool {
    let documents = WorkspaceDocuments::new(root.to_path_buf())
        .expect("a workspace under a temporary directory must be accepted");
    BoardTool {
        documents,
        from: from.to_string(),
    }
}

/// A post reaches the queue and the derived board.
#[tokio::test]
async fn a_post_reaches_the_queue_and_the_board() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    let tool = tool(workspace.path(), "adversarial");
    let call = ToolCall {
        id: "1".to_string(),
        name: "post_board".to_string(),
        arguments: json!({
            "kind": "dead-end",
            "body": "the generating-function route is dead: it needs f to be D-finite and it is not",
            "refers": ["claim-4"]
        }),
        invalid: None,
    };
    let result = tool.call(&(), call).await.expect("the post must succeed");
    assert!(!result.is_error(), "a well-formed post must not error");
    let posts = board::collect(workspace.path());
    assert_eq!(posts.len(), 1);
    assert_eq!(posts[0].kind, board::Kind::DeadEnd);
    let rendered = std::fs::read_to_string(workspace.path().join(board::PATH))
        .expect("the board must have been re-derived");
    assert!(rendered.contains("D-finite"));
}

/// The sender is the tool's, not the model's.
///
/// The board's value rests on a reader being able to tell who found what, so a
/// school must not be able to attribute a post to a sibling. The schema having
/// no `from` field is the control; this asserts that supplying one anyway
/// changes nothing.
#[tokio::test]
async fn the_sender_cannot_be_chosen_by_the_caller() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    let tool = tool(workspace.path(), "rising-sea");
    let call = ToolCall {
        id: "1".to_string(),
        name: "post_board".to_string(),
        arguments: json!({
            "kind": "hunch",
            "body": "this may factor through the sheaf setting",
            "from": "chisel"
        }),
        invalid: None,
    };
    // `additionalProperties: false` should refuse the extra field outright; if
    // validation is ever loosened, the attribution must still be the tool's.
    match tool.call(&(), call).await {
        Ok(_) => {
            let posts = board::collect(workspace.path());
            assert_eq!(
                posts[0].from, "rising-sea",
                "a school must not be able to post as another"
            );
        }
        Err(_) => {
            assert!(
                board::collect(workspace.path()).is_empty(),
                "a refused post must leave nothing behind"
            );
        }
    }
}

/// An empty body is refused.
#[tokio::test]
async fn an_empty_body_is_refused() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    let tool = tool(workspace.path(), "chisel");
    let call = ToolCall {
        id: "1".to_string(),
        name: "post_board".to_string(),
        arguments: json!({ "kind": "lesson", "body": "   " }),
        invalid: None,
    };
    assert!(
        tool.call(&(), call).await.is_err(),
        "a blank body must not reach the board"
    );
}

/// Every kind the schema advertises is one the parser recognises.
///
/// A schema offering a value the parser silently downgrades would file a dead
/// end as a hunch, which is the one distinction the board exists to carry.
#[test]
fn every_advertised_kind_parses_back_to_itself() {
    for kind in board::Kind::ALL {
        assert_eq!(
            board::Kind::parse(kind.label()),
            kind,
            "kind `{}` does not survive the round trip",
            kind.label()
        );
    }
}
