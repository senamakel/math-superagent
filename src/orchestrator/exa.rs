//! The three Exa endpoints beyond a query: similarity, contents, and synthesis.
//!
//! `exa_search` answers *what exists under this phrasing*, and for a long time
//! that was the run's only way onto the web. It is the weakest of the four
//! questions a librarian actually has, because every one of its answers is
//! bounded by how well the run guessed at the name of a subject it is trying to
//! learn. The failure that produces is recorded in the librarian's own brief: a
//! run reasoning from what the model remembers instead of from what it can
//! read, because the search for the thing it half-remembered returned nothing
//! and there was no second move.
//!
//! The three tools here are the other three questions.
//!
//! - [`FindSimilarTool`] asks *what is like this*, with a page rather than a
//!   phrase as the query. It is the only discovery path here that needs no
//!   guess at vocabulary at all, which makes it the one that works when the run
//!   does not yet know what the subject is called — exactly the position a run
//!   is in at the start, and exactly when a query is worst.
//! - [`SourceContentsTool`] asks *what do these twenty pages actually say*, in
//!   one request, storing nothing. It is triage, and the step it replaces is a
//!   librarian downloading twenty papers to find the three that matter.
//! - [`DeepResearchTool`] asks the question the run cannot decompose itself,
//!   and hands it to Exa's own agent, which runs many searches and synthesises
//!   across them.
//!
//! # What they all do, that a search does not
//!
//! Every one of them feeds [`super::frontier`]. A search result the model did
//! not act on in that turn is gone; a frontier row survives the turn, the
//! agent, and the restart, and is ranked against everything else the library
//! has ever cited. That is what turns three tools into a library rather than
//! three transcripts.
//!
//! # Why these are separate tools rather than flags on `exa_search`
//!
//! Because they cost differently and a run should be seen to have chosen.
//! `deep-reasoning` spends twelve to forty seconds and real money on one call;
//! a contents request over twenty URLs is cheap but returns twenty pages of
//! text. Folding either into `exa_search` behind an argument would put that
//! decision where nobody reviewing a run can see it, and would make the cheap
//! call and the expensive one indistinguishable in a trace.

use std::fmt::Write as _;
use std::sync::Arc;

use async_trait::async_trait;
use serde_json::{Value, json};

use super::documents::WorkspaceDocuments;
use super::readable::LinkRecord;
use crate::agent::{Result, Tool, ToolCall, ToolResult, ToolSchema};

/// Where similarity expansion goes.
const FIND_SIMILAR_URL: &str = "https://api.exa.ai/findSimilar";

/// Where a contents request goes.
const CONTENTS_URL: &str = "https://api.exa.ai/contents";

/// Where a synthesised research request goes.
///
/// The same endpoint an ordinary search uses. Exa's separate `/research/v1`
/// task API — create, then poll — was deprecated on 1 May 2026 in favour of
/// this, and building on it now would mean writing a polling loop against an
/// endpoint already past its retirement date. The depth is a `type` on the
/// search a run already makes, which is also why it needs no task lifecycle:
/// the reply comes back on the request.
const SEARCH_URL: &str = "https://api.exa.ai/search";

/// The search tier that reasons across what it finds rather than listing it.
const DEEP_TYPE: &str = "deep-reasoning";

/// Results one similarity expansion returns.
const MAX_SIMILAR: u64 = 25;

/// Results one similarity expansion returns when the caller says nothing.
const DEFAULT_SIMILAR: u64 = 10;

/// URLs one contents request may carry.
///
/// The endpoint accepts a hundred. Twenty is what fits in a tool result a model
/// will actually read: the point of this call is to decide which handful to
/// download, and a decision over a hundred summaries is not a decision.
const MAX_CONTENTS_URLS: usize = 20;

/// Characters kept from one page's text.
const MAX_TEXT_CHARS: u64 = 3_000;

/// Characters kept from one rendered result.
const RESULT_CHARS: usize = 2_000;

/// Characters kept across a whole rendered reply.
///
/// A wider reach must not become a context bill. Every tool here bounds the set
/// as well as each member of it, because twenty results that individually fit
/// still do not collectively.
const TOTAL_CHARS: usize = 24_000;

/// Links kept from one page.
///
/// These go to the frontier rather than into the reply, so the bound is about
/// what one navigation-heavy page may contribute to the ranking — the same
/// concern [`super::frontier`] caps per source for its own reasons.
const MAX_LINKS_PER_PAGE: u64 = 40;

/// The Exa endpoints reached with one key and one client.
#[derive(Clone, Debug)]
struct Exa {
    client: reqwest::Client,
    api_key: String,
    documents: WorkspaceDocuments,
}

impl Exa {
    /// Posts one request and returns the parsed reply.
    async fn post(&self, url: &str, body: &Value) -> Result<Value> {
        let response = self
            .client
            .post(url)
            .header("x-api-key", &self.api_key)
            .json(body)
            .send()
            .await
            .map_err(|error| {
                tinyagents::TinyAgentsError::Tool(format!("the Exa request failed: {error}"))
            })?;
        let status = response.status();
        let parsed: Value = response.json().await.map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!("the Exa reply was invalid: {error}"))
        })?;
        if !status.is_success() {
            let message = parsed
                .get("error")
                .and_then(Value::as_str)
                .unwrap_or("unknown Exa API error");
            return Err(tinyagents::TinyAgentsError::Tool(format!(
                "Exa returned {status}: {message}"
            )));
        }
        Ok(parsed)
    }

    /// Files what a reply's pages point at as leads.
    ///
    /// Best effort and unreported, like every other frontier write: the answer
    /// is already in the caller's hands, and a lost lead must not turn a
    /// successful lookup into a failed tool call.
    async fn file_leads(&self, source_url: &str, links: &[LinkRecord]) {
        if links.is_empty() {
            return;
        }
        super::frontier::record(
            &self.documents,
            source_url,
            "",
            links,
            &self.documents.goal().await,
        )
        .await;
    }
}

/// Builds the tool set this module contributes, or nothing when research is
/// off.
///
/// Withheld by not being built rather than by being told to abstain, which is
/// the rule the whole research gate rests on: all three of these reach the open
/// web, so all three are exactly what `MATH_AGENT_RESEARCH=off` is for.
///
/// # Errors
///
/// Returns an error when the Exa key is missing while research is enabled.
pub(in crate::orchestrator) fn tools(
    research_enabled: bool,
    documents: &WorkspaceDocuments,
) -> Result<Vec<Arc<dyn Tool<()>>>> {
    if !research_enabled {
        return Ok(Vec::new());
    }
    let api_key = std::env::var("EXA_API_KEY")
        .map_err(|_| tinyagents::TinyAgentsError::Validation("EXA_API_KEY is required".into()))?;
    let exa = Exa {
        client: reqwest::Client::new(),
        api_key,
        documents: documents.clone(),
    };
    Ok(vec![
        Arc::new(FindSimilarTool { exa: exa.clone() }),
        Arc::new(SourceContentsTool { exa: exa.clone() }),
        Arc::new(DeepResearchTool { exa }),
    ])
}

/// Reads the shared domain-filter arguments onto a request body.
///
/// Shared because all three endpoints take the same `CommonRequest`, and a
/// filter spelled differently on one of them would be a filter that silently
/// does nothing on that one.
fn apply_common(body: &mut Value, call: &ToolCall) {
    let Some(object) = body.as_object_mut() else {
        return;
    };
    for (argument, field) in [
        ("include_domains", "includeDomains"),
        ("exclude_domains", "excludeDomains"),
    ] {
        let domains: Vec<&str> = call
            .arguments
            .get(argument)
            .and_then(Value::as_array)
            .into_iter()
            .flatten()
            .filter_map(Value::as_str)
            .map(str::trim)
            .filter(|domain| !domain.is_empty())
            .collect();
        if !domains.is_empty() {
            object.insert(field.to_string(), json!(domains));
        }
    }
    for (argument, field) in [
        ("start_published_date", "startPublishedDate"),
        ("end_published_date", "endPublishedDate"),
    ] {
        if let Some(date) = call
            .arguments
            .get(argument)
            .and_then(Value::as_str)
            .map(str::trim)
            .filter(|date| !date.is_empty())
        {
            object.insert(field.to_string(), json!(date));
        }
    }
}

/// The schema fragment for the filters every endpoint here shares.
fn common_properties() -> Value {
    json!({
        "include_domains": {
            "type": "array",
            "items": { "type": "string" },
            "description": "Only return results from these domains, e.g. \
                            [\"arxiv.org\", \"ams.org\"]. Use it to reach the literature \
                            directly when a subject's name collides with something popular."
        },
        "exclude_domains": {
            "type": "array",
            "items": { "type": "string" },
            "description": "Never return results from these domains. Use it to push past the \
                            encyclopedic retellings once the run has them."
        },
        "start_published_date": {
            "type": "string",
            "description": "ISO 8601 date; only results published after it. Use it to find \
                            what came after a result the run is stuck on."
        },
        "end_published_date": {
            "type": "string",
            "description": "ISO 8601 date; only results published before it. Use it to find \
                            the original treatment rather than its retellings."
        }
    })
}

/// Truncates on a character boundary, marking that it did.
fn clip(text: &str, limit: usize) -> String {
    let trimmed = text.trim();
    if trimmed.chars().count() <= limit {
        return trimmed.to_string();
    }
    let kept: String = trimmed.chars().take(limit).collect();
    format!("{kept}…")
}

fn field(result: &Value, key: &str) -> String {
    result
        .get(key)
        .and_then(Value::as_str)
        .unwrap_or_default()
        .trim()
        .to_string()
}

/// Joins a result's highlight strings.
fn highlights(result: &Value) -> String {
    result
        .get("highlights")
        .and_then(Value::as_array)
        .map(|items| {
            items
                .iter()
                .filter_map(Value::as_str)
                .collect::<Vec<_>>()
                .join(" … ")
        })
        .unwrap_or_default()
}

/// Renders one result: what it is, who wrote it, and what it says.
fn render(index: usize, result: &Value) -> String {
    let title = result
        .get("title")
        .and_then(Value::as_str)
        .filter(|value| !value.trim().is_empty())
        .unwrap_or("Untitled");
    let mut out = format!("{}. {title}\n{}", index + 1, field(result, "url"));
    // Provenance, so a source can be weighed rather than merely cited: a paper
    // by the author a problem is named after is worth more than a blog post
    // about it, and neither the title nor the summary says which is which.
    let author = field(result, "author");
    let published = field(result, "publishedDate");
    if !author.is_empty() || !published.is_empty() {
        let _ = write!(out, "\n{author}{}{published}", if author.is_empty() || published.is_empty() { "" } else { " · " });
    }
    for (label, key) in [("", "summary"), ("Matching passages: ", "text")] {
        let value = field(result, key);
        if !value.is_empty() {
            let _ = write!(out, "\n{label}{}", clip(&value, RESULT_CHARS));
        }
    }
    let matched = highlights(result);
    if !matched.is_empty() {
        let _ = write!(out, "\nWhy it matched: {}", clip(&matched, RESULT_CHARS));
    }
    out
}

/// Renders a whole result set, bounded.
fn render_all(results: &[Value]) -> String {
    clip(
        &results
            .iter()
            .enumerate()
            .map(|(index, result)| render(index, result))
            .collect::<Vec<_>>()
            .join("\n\n"),
        TOTAL_CHARS,
    )
}

/// Reads the results array out of a reply.
fn results_of(reply: &Value) -> Vec<Value> {
    reply
        .get("results")
        .and_then(Value::as_array)
        .cloned()
        .unwrap_or_default()
}

/// Turns a result set into leads for the frontier.
fn result_leads(results: &[Value], context: &str) -> Vec<LinkRecord> {
    let mut out: Vec<LinkRecord> = Vec::new();
    for result in results {
        let url = field(result, "url");
        if url.is_empty() || out.iter().any(|record| record.url == url) {
            continue;
        }
        out.push(LinkRecord {
            url,
            label: result
                .get("title")
                .and_then(Value::as_str)
                .unwrap_or("(untitled)")
                .to_string(),
            context: context.to_string(),
        });
    }
    out
}

/// Reads the links a contents reply extracted from each page.
///
/// This is the same citation-graph argument [`super::frontier`] makes, applied
/// to a page the run decided *not* to download. A triage read that keeps only
/// the verdict throws away every reference the page carried, which is most of
/// what the page was worth when the verdict was "not this one".
fn extracted_leads(results: &[Value]) -> Vec<LinkRecord> {
    let mut out: Vec<LinkRecord> = Vec::new();
    for result in results {
        let from = field(result, "url");
        let title = result
            .get("title")
            .and_then(Value::as_str)
            .unwrap_or("a triaged page")
            .to_string();
        let links = result
            .get("extras")
            .and_then(|extras| extras.get("links"))
            .and_then(Value::as_array)
            .cloned()
            .unwrap_or_default();
        for link in links.iter().filter_map(Value::as_str) {
            let link = link.trim();
            if link.is_empty() || link == from || out.iter().any(|record| record.url == link) {
                continue;
            }
            out.push(LinkRecord {
                url: link.to_string(),
                label: String::new(),
                context: format!("linked from {title}"),
            });
        }
    }
    out
}

include!("exa_similar.rs");
include!("exa_contents.rs");
include!("exa_deep.rs");

#[cfg(test)]
#[path = "exa_test.rs"]
mod test;
