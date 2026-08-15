//! Unit tests for the chunked recursive read.
#![allow(clippy::expect_used)]

use std::path::PathBuf;
use std::sync::{Arc, Mutex};

use async_trait::async_trait;
use serde_json::json;
use tinyagents::harness::model::{ChatModel, ModelRequest, ModelResponse, ModelStream};

use super::{CHUNK_BYTES, MapTool, chunk};
use crate::agent::{Result, Tool, ToolCall};
use crate::orchestrator::documents::WorkspaceDocuments;

fn workspace(name: &str) -> Result<PathBuf> {
    let path = std::env::temp_dir().join(format!("math-agent-recursive-{name}"));
    let _ = std::fs::remove_dir_all(&path);
    std::fs::create_dir_all(&path).map_err(|error| {
        tinyagents::TinyAgentsError::Tool(format!("failed to create test workspace: {error}"))
    })?;
    path.canonicalize().map_err(|error| {
        tinyagents::TinyAgentsError::Tool(format!("failed to resolve test workspace: {error}"))
    })
}

/// A model that answers every chunk with the same reply and records what it
/// was sent, so a test can assert what actually reached a sub-call.
struct ScriptedModel {
    reply: String,
    /// Every user message this model was handed, in call order.
    seen: Arc<Mutex<Vec<String>>>,
    /// When set, the first call fails instead of answering.
    fail_first: bool,
}

impl ScriptedModel {
    fn new(reply: &str) -> (Arc<Self>, Arc<Mutex<Vec<String>>>) {
        let seen = Arc::new(Mutex::new(Vec::new()));
        (
            Arc::new(Self {
                reply: reply.to_string(),
                seen: seen.clone(),
                fail_first: false,
            }),
            seen,
        )
    }

    fn failing(reply: &str) -> Arc<Self> {
        Arc::new(Self {
            reply: reply.to_string(),
            seen: Arc::new(Mutex::new(Vec::new())),
            fail_first: true,
        })
    }
}

#[async_trait]
impl ChatModel<()> for ScriptedModel {
    async fn invoke(&self, _state: &(), request: ModelRequest) -> Result<ModelResponse> {
        let rendered = request
            .messages
            .iter()
            .map(|message| message.text())
            .collect::<Vec<_>>()
            .join("\n");
        let first = {
            let mut seen = self.seen.lock().expect("recorded prompts are not poisoned");
            seen.push(rendered);
            seen.len() == 1
        };
        if self.fail_first && first {
            return Err(tinyagents::TinyAgentsError::Tool("provider refused".into()));
        }
        Ok(ModelResponse::assistant(&self.reply))
    }

    async fn stream(&self, _state: &(), _request: ModelRequest) -> Result<ModelStream> {
        Err(tinyagents::TinyAgentsError::Tool(
            "the recursive read never streams".into(),
        ))
    }
}

async fn run(documents: &WorkspaceDocuments, arguments: serde_json::Value) -> Result<String> {
    let tool: Arc<dyn Tool<()>> = documents
        .tools()
        .into_iter()
        .find(|tool| tool.name() == "map_document")
        .ok_or_else(|| tinyagents::TinyAgentsError::Tool("map_document is not registered".into()))?;
    let result = tool
        .call(
            &(),
            ToolCall {
                id: "1".to_string(),
                name: "map_document".to_string(),
                arguments,
                invalid: None,
            },
        )
        .await?;
    Ok(result.content)
}

#[test]
fn chunks_cut_at_lines_and_number_them_continuously() {
    // Every finding cites lines, so a chunk that began mid-line would make its
    // own citations wrong by one.
    let text = ("x".repeat(100) + "\n").repeat(1_000);

    let chunks = chunk(&text, 1);

    assert!(chunks.len() > 1);
    assert_eq!(chunks[0].first_line, 1);
    for pair in chunks.windows(2) {
        assert_eq!(pair[0].last_line + 1, pair[1].first_line);
        assert!(pair[0].text.ends_with('\n'));
        assert!(pair[0].text.len() <= CHUNK_BYTES);
    }
    assert_eq!(
        chunks.last().map(|c| c.last_line),
        Some(text.lines().count())
    );
}

#[test]
fn a_region_that_starts_late_is_numbered_from_where_it_started() {
    let chunks = chunk("a\nb\nc\n", 500);

    assert_eq!(chunks.len(), 1);
    assert_eq!((chunks[0].first_line, chunks[0].last_line), (500, 502));
}

#[tokio::test]
async fn the_tool_is_absent_when_the_run_has_no_reader_model() -> Result<()> {
    // Absent rather than present-and-failing: a tool that is not registered
    // cannot be called, and one that always errors spends a turn teaching that.
    let documents = WorkspaceDocuments::new(workspace("absent")?)?;

    assert!(
        !documents
            .tools()
            .iter()
            .any(|tool| tool.name() == "map_document")
    );
    Ok(())
}

#[tokio::test]
async fn the_source_never_reaches_the_caller_but_the_answer_does() -> Result<()> {
    let (model, seen) = ScriptedModel::new("Lines 3-4 give the bound as 2n.");
    let documents = WorkspaceDocuments::new(workspace("answer")?)?.with_reader(model);
    let body = ("filler line\n".repeat(40) + "the bound is 2n\n").repeat(200);
    documents.write_document("research/big.md", &body).await?;

    let out = run(
        &documents,
        json!({ "path": "research/big.md", "question": "what is the bound?" }),
    )
    .await?;

    // Several chunks were needed, so this genuinely recursed.
    let calls = seen.lock().expect("prompts are not poisoned").len();
    assert!(calls > 2, "{calls} calls");
    assert!(out.contains("the bound as 2n"), "{out}");
    // The whole point: the caller is charged for an answer, not for a source.
    assert!(out.len() < body.len() / 10, "{} bytes", out.len());
    assert!(!out.contains("filler line"), "{out}");
    // And it is presented as evidence to check, not as a fact.
    assert!(out.contains("read the cited lines"), "{out}");
    Ok(())
}

#[tokio::test]
async fn the_chunk_precedes_the_question_so_a_second_question_hits_the_cache() -> Result<()> {
    // Providers cache on a prompt prefix. Putting the question first would move
    // the varying part to the front and discard every hit.
    let (model, seen) = ScriptedModel::new("something");
    let documents = WorkspaceDocuments::new(workspace("order")?)?.with_reader(model);
    documents
        .write_document("n.md", "the marker line\nmore text\n")
        .await?;

    run(
        &documents,
        json!({ "path": "n.md", "question": "the question text" }),
    )
    .await?;

    let prompts = seen.lock().expect("prompts are not poisoned");
    let first = prompts.first().expect("one chunk was read");
    let marker = first.find("the marker line").expect("the chunk is present");
    let question = first.find("the question text").expect("the question is present");
    assert!(marker < question, "the question came before the chunk");
    Ok(())
}

#[tokio::test]
async fn a_chunk_with_nothing_to_say_contributes_nothing() -> Result<()> {
    let (model, _) = ScriptedModel::new("NOTHING");
    let documents = WorkspaceDocuments::new(workspace("silent")?)?.with_reader(model);
    documents.write_document("n.md", "unrelated text\n").await?;

    let out = run(&documents, json!({ "path": "n.md", "question": "the bound?" })).await?;

    assert!(out.contains("0 bore on the question"), "{out}");
    // And it says what to try next rather than reporting an empty answer.
    assert!(out.contains("grep_workspace"), "{out}");
    Ok(())
}

#[tokio::test]
async fn a_failed_chunk_is_named_rather_than_silently_dropped() -> Result<()> {
    // Fifty-nine chunks that answered are worth more than one failure that
    // discards them — but an answer with a hole in it must say where the hole
    // is, or it will be read as complete.
    let documents =
        WorkspaceDocuments::new(workspace("failure")?)?.with_reader(ScriptedModel::failing("found"));
    let body = ("filler\n".repeat(4_000)).repeat(2);
    documents.write_document("n.md", &body).await?;

    let out = run(&documents, json!({ "path": "n.md", "question": "anything?" })).await?;

    assert!(out.contains("never read"), "{out}");
    assert!(out.contains("provider refused"), "{out}");
    Ok(())
}

#[tokio::test]
async fn the_reading_can_be_narrowed_to_one_section() -> Result<()> {
    let (model, seen) = ScriptedModel::new("noted");
    let documents = WorkspaceDocuments::new(workspace("section")?)?.with_reader(model);
    documents
        .write_document("n.md", "## First\nalpha\n## Second\nbeta\n")
        .await?;

    run(
        &documents,
        json!({ "path": "n.md", "question": "q", "section": "Second" }),
    )
    .await?;

    let prompts = seen.lock().expect("prompts are not poisoned");
    let first = prompts.first().expect("one chunk was read");
    assert!(first.contains("beta"), "{first}");
    assert!(!first.contains("alpha"), "{first}");
    Ok(())
}
