//! Reading a document that does not fit, by recursion instead of by truncation.
//!
//! [`super::outline`] and [`super::grep`] let a role find the part of a file it
//! needs. They do not help when the question is *about the whole file* — "what
//! does this survey establish about large prime gaps", "which of these 47
//! approaches were already refuted, and by what" — because the answer is
//! distributed across every section and no selection is the right one.
//!
//! The recursive-language-model answer to that is to stop treating the context
//! window as the place where reading happens. The document is split into
//! chunks; each chunk is read by its own model call that sees that chunk and
//! nothing else; the short findings are merged. Only the merged answer reaches
//! the caller's context. A 428 KB bibliography costs the caller about two
//! hundred tokens of answer instead of a hundred and seven thousand of source,
//! and every finding carries the line range it came from, so the caller can go
//! and read the four hundred bytes that actually mattered.
//!
//! # Why the chunk goes before the question
//!
//! Each sub-call is `[fixed instruction][chunk][question]`, in that order, and
//! the order is the design. Providers cache on a prompt *prefix*, so a run that
//! asks a second question of the same source re-sends a prefix it has already
//! paid for and is charged the cached rate for the expensive half. A run
//! interrogating one survey five ways pays for its text roughly once. Putting
//! the question first would move the varying part to the front and discard
//! every one of those hits.
//!
//! # What it is not
//!
//! It is not a summariser and must not be used as one: a chunk that does not
//! bear on the question is required to say so and contribute nothing, so the
//! output is an answer with citations rather than a compression of the source.
//! And it is not a claim. What comes back is what a model read in a chunk it
//! saw alone, which is evidence to check by reading the cited lines — the same
//! standing as a search result, and for the same reason.

use std::fmt::Write as _;
use std::sync::Arc;
use std::time::Duration;

use async_trait::async_trait;
use serde_json::json;
use tinyagents::harness::model::{ChatModel, ModelRequest};

use super::documents::WorkspaceDocuments;
use crate::agent::{Message, Result, Tool, ToolCall, ToolResult, ToolSchema};

/// Bytes of source one sub-call reads.
///
/// Roughly six thousand tokens: small enough that a model attends to all of it
/// rather than to its ends, and large enough that a section of a paper usually
/// survives inside one chunk instead of being cut across two.
const CHUNK_BYTES: usize = 24 * 1024;

/// Chunks one call will read.
///
/// At [`CHUNK_BYTES`] this covers a 1.5 MB region — every document in a live
/// workspace, with room over. A region larger than this is answered over the
/// first sixty chunks and *says* so, because a partial answer presented as a
/// complete one is the failure this tool exists to avoid.
const MAX_CHUNKS: usize = 60;

/// Sub-calls in flight at once.
///
/// The container shares one provider connection pool with the run that is
/// waiting on this tool, and sixty concurrent requests would starve it.
const CONCURRENCY: usize = 6;

/// How long one sub-call is given.
const CALL_TIMEOUT: Duration = Duration::from_secs(180);

/// Tokens one chunk's finding may run to.
const CHUNK_TOKENS: u32 = 700;

/// Tokens the merged answer may run to.
const MERGE_TOKENS: u32 = 1_800;

/// What a chunk reader replies when its chunk says nothing about the question.
const NOTHING: &str = "NOTHING";

/// The instruction every chunk reader is given.
///
/// First in the prompt and byte-identical across every call, so it is the front
/// of the cached prefix rather than a per-call cost.
const CHUNK_INSTRUCTION: &str = "\
You are reading one chunk of a larger document on behalf of a mathematics \
research run. You can see only this chunk. Another reader has every other \
chunk, and their findings will be merged with yours.

Answer only from the text in front of you. Report what this chunk says that \
bears on the question, in at most 120 words, and cite the line numbers you \
took it from — the chunk's own line numbering is given in its header.

If this chunk contains nothing that bears on the question, reply with the \
single word NOTHING. Contributing something irrelevant is worse than \
contributing nothing: the merge cannot tell a weak match from a real one.

Never guess at what the rest of the document says, and never repeat the \
question back.";

/// The instruction the merge is given.
const MERGE_INSTRUCTION: &str = "\
You are merging findings from readers who each saw one chunk of a single \
document and could not see each other's chunks.

Write the answer to the question from their findings alone. Keep every line \
citation, attached to the statement it supports. Where two findings disagree, \
say so and give both with their citations rather than choosing. Where the \
findings do not answer the question, say what they do establish and what is \
missing. Add nothing that is not in front of you.";

/// One chunk of the region being read.
#[derive(Clone, Debug)]
struct Chunk {
    first_line: usize,
    last_line: usize,
    text: String,
}

/// What one chunk's reader came back with.
#[derive(Clone, Debug)]
enum Finding {
    /// The chunk bore on the question, and this is what it said.
    Said(String),
    /// The chunk bore on nothing.
    Silent,
    /// The call failed, so this chunk was never read.
    Failed(String),
}

/// Splits `text` into chunks at line boundaries, numbering from `first_line`.
///
/// Cut at a line rather than at a byte because every finding cites lines, and a
/// chunk that begins mid-line makes its own citations wrong by one.
fn chunk(text: &str, first_line: usize) -> Vec<Chunk> {
    let mut chunks = Vec::new();
    let mut body = String::new();
    let mut start = first_line;
    let mut line = first_line;
    for content in text.lines() {
        if !body.is_empty() && body.len() + content.len() + 1 > CHUNK_BYTES {
            chunks.push(Chunk {
                first_line: start,
                last_line: line - 1,
                text: std::mem::take(&mut body),
            });
            start = line;
        }
        body.push_str(content);
        body.push('\n');
        line += 1;
    }
    if !body.is_empty() {
        chunks.push(Chunk {
            first_line: start,
            last_line: line.saturating_sub(1).max(start),
            text: body,
        });
    }
    chunks
}

/// Reads one chunk against the question.
///
/// A provider failure is a [`Finding::Failed`] rather than an error: fifty-nine
/// chunks that answered are worth more than one failure that discards them, and
/// the gap is named in the output so nobody mistakes the answer for complete.
async fn read_chunk(
    model: Arc<dyn ChatModel<()>>,
    path: String,
    chunk: Chunk,
    question: String,
) -> Finding {
    let request = ModelRequest::new(vec![
        Message::system(CHUNK_INSTRUCTION),
        // The chunk precedes the question deliberately; see the module
        // documentation on prefix caching.
        Message::user(format!(
            "DOCUMENT: {path}\nCHUNK: lines {}-{}\n\n{}\n\nQUESTION: {question}",
            chunk.first_line, chunk.last_line, chunk.text
        )),
    ])
    .with_max_tokens(CHUNK_TOKENS);
    match tokio::time::timeout(CALL_TIMEOUT, model.invoke(&(), request)).await {
        Ok(Ok(response)) => {
            let text = response.text().trim().to_string();
            // A model told to reply with one word sometimes wraps it in a
            // sentence, and a finding that is only a refusal is noise in the
            // merge either way.
            if text.is_empty() || text.trim_matches(['.', '"', '*', ' ']).eq_ignore_ascii_case(NOTHING)
            {
                Finding::Silent
            } else {
                Finding::Said(text)
            }
        }
        Ok(Err(error)) => Finding::Failed(error.to_string()),
        Err(_) => Finding::Failed(format!("timed out after {}s", CALL_TIMEOUT.as_secs())),
    }
}

/// Reads every chunk, at most [`CONCURRENCY`] at a time, in order.
async fn read_all(
    model: &Arc<dyn ChatModel<()>>,
    path: &str,
    chunks: &[Chunk],
    question: &str,
) -> Vec<(Chunk, Finding)> {
    let mut out = Vec::with_capacity(chunks.len());
    for batch in chunks.chunks(CONCURRENCY) {
        let mut set = tokio::task::JoinSet::new();
        for (offset, chunk) in batch.iter().enumerate() {
            let model = model.clone();
            let path = path.to_string();
            let chunk = chunk.clone();
            let question = question.to_string();
            set.spawn(async move {
                let finding = read_chunk(model, path, chunk.clone(), question).await;
                (offset, chunk, finding)
            });
        }
        let mut done: Vec<(usize, Chunk, Finding)> = Vec::with_capacity(batch.len());
        while let Some(joined) = set.join_next().await {
            match joined {
                Ok(result) => done.push(result),
                // A panicked reader is a failed chunk like any other. The
                // position is unknown, so it cannot be reported against a
                // range; the count in the summary still shows it.
                Err(error) => done.push((
                    usize::MAX,
                    Chunk {
                        first_line: 0,
                        last_line: 0,
                        text: String::new(),
                    },
                    Finding::Failed(error.to_string()),
                )),
            }
        }
        done.sort_by_key(|(offset, _, _)| *offset);
        out.extend(done.into_iter().map(|(_, chunk, finding)| (chunk, finding)));
    }
    out
}

/// Merges the findings into one answer.
///
/// A single finding is returned as it stands. Merging one thing is a model call
/// that can only lose information, and it costs the run a round trip to do it.
async fn merge(
    model: &Arc<dyn ChatModel<()>>,
    path: &str,
    question: &str,
    findings: &[(Chunk, String)],
) -> Result<String> {
    match findings {
        [] => Ok(String::new()),
        [(chunk, only)] => Ok(format!("{only}\n\n(from lines {}-{} alone)", chunk.first_line, chunk.last_line)),
        many => {
            let mut body = String::new();
            for (chunk, said) in many {
                let _ = writeln!(
                    body,
                    "--- from lines {}-{} ---\n{said}\n",
                    chunk.first_line, chunk.last_line
                );
            }
            let request = ModelRequest::new(vec![
                Message::system(MERGE_INSTRUCTION),
                Message::user(format!(
                    "DOCUMENT: {path}\n\nFINDINGS:\n{body}\nQUESTION: {question}"
                )),
            ])
            .with_max_tokens(MERGE_TOKENS);
            let response = tokio::time::timeout(CALL_TIMEOUT, model.invoke(&(), request))
                .await
                .map_err(|_| {
                    tinyagents::TinyAgentsError::Tool(format!(
                        "merging {} findings timed out after {}s",
                        many.len(),
                        CALL_TIMEOUT.as_secs()
                    ))
                })?
                .map_err(|error| {
                    tinyagents::TinyAgentsError::Tool(format!("merging findings failed: {error}"))
                })?;
            Ok(response.text().trim().to_string())
        }
    }
}

/// The `map_document` tool.
pub(super) struct MapTool {
    documents: WorkspaceDocuments,
    model: Arc<dyn ChatModel<()>>,
}

impl std::fmt::Debug for MapTool {
    fn fmt(&self, formatter: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        formatter.debug_struct("MapTool").finish_non_exhaustive()
    }
}

impl MapTool {
    /// Builds the tool, or nothing when the run has no reader model.
    ///
    /// Absent rather than present-and-failing, on the same argument the
    /// research gate is built on: a tool that is not registered cannot be
    /// called, and a tool that is registered but always errors spends a turn
    /// teaching that.
    pub(super) fn all(
        documents: &WorkspaceDocuments,
        model: Option<&Arc<dyn ChatModel<()>>>,
    ) -> Vec<Arc<dyn Tool<()>>> {
        model
            .map(|model| {
                Arc::new(Self {
                    documents: documents.clone(),
                    model: model.clone(),
                }) as Arc<dyn Tool<()>>
            })
            .into_iter()
            .collect()
    }
}

#[async_trait]
impl Tool<()> for MapTool {
    fn name(&self) -> &'static str {
        "map_document"
    }

    fn description(&self) -> &'static str {
        "Answers a question about a document too large to read, by reading it in chunks with \
         separate model calls and merging the findings. Returns a short cited answer instead of \
         the source."
    }

    fn schema(&self) -> ToolSchema {
        ToolSchema::new(
            self.name(),
            self.description(),
            json!({
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Relative path below /workspace."
                    },
                    "question": {
                        "type": "string",
                        "description": "What to find out. Every chunk is read against this alone, \
                                        so state it fully rather than by reference."
                    },
                    "section": {
                        "type": "string",
                        "description": "Restrict the reading to one section, matched by heading."
                    },
                    "lines": {
                        "type": "string",
                        "description": "Restrict the reading to a line range, as \"120-2600\"."
                    }
                },
                "required": ["path", "question"],
                "additionalProperties": false
            }),
        )
    }

    async fn call(&self, _state: &(), call: ToolCall) -> Result<ToolResult> {
        self.schema().validate_call(&call)?;
        let path = super::string_argument(&call, "path")?;
        let question = super::string_argument(&call, "question")?;
        let section = call.arguments.get("section").and_then(|v| v.as_str());
        let lines = call.arguments.get("lines").and_then(|v| v.as_str());
        let content = self.documents.read_document(&path).await?;
        // The whole document is the default here, unlike `read_document`:
        // reading all of it is what this tool is for, and none of it reaches
        // the caller's context.
        let region = super::outline::region(&path, &content, section, lines)?;
        let chunks = chunk(&region.text, region.first_line);
        let total = chunks.len();
        let capped = total > MAX_CHUNKS;
        let chunks = &chunks[..total.min(MAX_CHUNKS)];
        if chunks.is_empty() {
            return Ok(ToolResult::text(
                call.id,
                self.name(),
                format!("{path} is empty over the requested range; nothing to read"),
            ));
        }
        let findings = read_all(&self.model, &path, chunks, &question).await;
        let said: Vec<(Chunk, String)> = findings
            .iter()
            .filter_map(|(chunk, finding)| match finding {
                Finding::Said(text) => Some((chunk.clone(), text.clone())),
                _ => None,
            })
            .collect();
        let failed: Vec<(&Chunk, &str)> = findings
            .iter()
            .filter_map(|(chunk, finding)| match finding {
                Finding::Failed(why) => Some((chunk, why.as_str())),
                _ => None,
            })
            .collect();
        let answer = merge(&self.model, &path, &question, &said).await?;

        let mut out = format!(
            "{path}, lines {}-{} read in {} chunks; {} bore on the question.\n\n",
            region.first_line,
            region.last_line,
            chunks.len(),
            said.len()
        );
        if answer.is_empty() {
            out.push_str(
                "No chunk contained anything bearing on the question. The document may not \
                 discuss it, or the question may name it differently than the source does — try \
                 grep_workspace for the source's own wording.\n",
            );
        } else {
            out.push_str(&answer);
            out.push('\n');
        }
        if let Some((_, why)) = failed.first() {
            let ranges: Vec<String> = failed
                .iter()
                .map(|(chunk, _)| format!("{}-{}", chunk.first_line, chunk.last_line))
                .collect();
            // The reason is carried through rather than counted, because the
            // two that occur want opposite responses: a timeout is worth
            // retrying over a narrower range, and a refusal is not.
            let _ = write!(
                out,
                "\n[{} chunk(s) were never read — lines {} — first failure: {why}. The answer \
                 above does not cover them.]\n",
                failed.len(),
                ranges.join(", ")
            );
        }
        if capped {
            let _ = write!(
                out,
                "\n[the range needed {total} chunks and was read to {MAX_CHUNKS}; lines after {} \
                 were not read. Narrow with `section` or `lines` to cover them.]\n",
                chunks.last().map_or(0, |chunk| chunk.last_line)
            );
        }
        out.push_str(
            "\nThis is what chunk readers reported, not an established fact: read the cited lines \
             before relying on it.\n",
        );
        Ok(ToolResult::text(call.id, self.name(), out))
    }
}

#[cfg(test)]
#[path = "recursive_test.rs"]
mod test;
