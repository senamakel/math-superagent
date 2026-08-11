//! Looking a computed sequence up in the OEIS.
//!
//! This is the one search in the runtime whose query is not a phrasing
//! problem. Every other lookup depends on guessing what a subject is called —
//! and the research prompt spends a paragraph on that, telling the agent to
//! try the named theorem, the objects, the classification, and the standard
//! treatment, because one query returns what the problem is called rather than
//! how it is solved. A sequence of integers has no such ambiguity: the terms
//! either are in the encyclopedia or they are not, and if they are, the entry
//! carries the closed form, the recurrence, and the cross-references to every
//! related sequence.
//!
//! It was a sentence in the research prompt — "when the run has computed them,
//! the numbers themselves, which often lead straight to a catalogued sequence"
//! — which is to say it happened when a model remembered. Making it a tool
//! makes it something a run can be seen not to have done. One live workspace
//! recorded exactly this as a finding: `S(n) ∉ OEIS`, filed as a dead end,
//! which is a result worth having and one nobody can obtain by rephrasing a
//! query.
//!
//! Two things it does beyond answering. The entry is filed under `research/`
//! like any other source, because a formula quoted into a tool result and
//! nowhere else is a citation the run cannot check later. And the entry's
//! cross-references — the `Cf.` line, which is the encyclopedia's own citation
//! graph — go into the frontier, so a hit on one sequence surfaces the
//! neighbours that describe the same structure.

use std::fmt::Write as _;
use std::sync::Arc;

use async_trait::async_trait;
use serde_json::{Value, json};

use super::documents::WorkspaceDocuments;
use super::readable::LinkRecord;
use crate::agent::{Result, Tool, ToolCall, ToolResult, ToolSchema};

/// Where a lookup sends its query.
const SEARCH_URL: &str = "https://oeis.org/search";

/// Entries one lookup reports.
///
/// A search on few terms matches broadly, and the encyclopedia is happy to
/// return hundreds. The first few are the ones whose terms actually line up;
/// past that the run is reading a list rather than an answer.
const MAX_ENTRIES: usize = 4;

/// Terms one query may carry.
///
/// Enough to identify a sequence uniquely in practice, few enough that the
/// query stays a URL. More terms narrow the match, so a caller with many
/// should send its first ones rather than all of them.
const MAX_TERMS: usize = 24;

/// Characters kept from one entry's formula, comment, and cross-reference
/// lines.
const MAX_SECTION: usize = 1_600;

/// Looks a computed integer sequence up in the OEIS.
#[derive(Debug)]
pub(crate) struct OeisTool {
    documents: WorkspaceDocuments,
}

impl OeisTool {
    /// Builds the tool set this module contributes.
    pub(in crate::orchestrator) fn all(documents: &WorkspaceDocuments) -> Vec<Arc<dyn Tool<()>>> {
        vec![Arc::new(Self {
            documents: documents.clone(),
        })]
    }

    /// Runs the query and returns the matching entries.
    async fn lookup(&self, terms: &[i64]) -> Result<Vec<Value>> {
        let query = terms
            .iter()
            .map(ToString::to_string)
            .collect::<Vec<_>>()
            .join(",");
        let body = self
            .documents
            .fetch_text(&format!("{SEARCH_URL}?q={query}&fmt=json"))
            .await?;
        // The encyclopedia answers a query with no matches by returning
        // `null`, not an empty list, and that is the answer the run most wants
        // recorded: a sequence absent from it is a real finding.
        let parsed: Value = serde_json::from_str(&body).map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!("the OEIS reply could not be read: {error}"))
        })?;
        Ok(match parsed {
            Value::Array(entries) => entries.into_iter().take(MAX_ENTRIES).collect(),
            Value::Object(map) => map
                .get("results")
                .and_then(Value::as_array)
                .map(|entries| entries.iter().take(MAX_ENTRIES).cloned().collect())
                .unwrap_or_default(),
            _ => Vec::new(),
        })
    }
}

/// Renders one entry as the note filed under `research/`.
fn note(entry: &Value) -> (String, String) {
    let number = entry.get("number").and_then(Value::as_i64).unwrap_or(0);
    let id = format!("A{number:06}");
    let name = entry
        .get("name")
        .and_then(Value::as_str)
        .unwrap_or("(unnamed)");
    let mut out = format!("# {id} — {name}\n\n<!-- source: https://oeis.org/{id} -->\n\n");
    let _ = writeln!(out, "**Terms.** {}\n", string(entry, "data"));
    for (heading, key) in [
        ("Formula", "formula"),
        ("Recurrence and program", "maple"),
        ("Comments", "comment"),
        ("References", "reference"),
        ("Cross-references", "xref"),
    ] {
        let section = lines(entry, key);
        if section.is_empty() {
            continue;
        }
        let _ = writeln!(out, "## {heading}\n\n{}\n", truncate(&section, MAX_SECTION));
    }
    out.push_str(
        "\n> Filed by an OEIS lookup, not read. Replace this with what it establishes for this \
         problem: which formula is exact, what its hypotheses are, and whether they hold here. \
         The closed form is the point — a catalogued sequence with a closed form turns an \
         enumeration into an evaluation.\n",
    );
    (id, out)
}

/// Joins one field's lines, whether the reply gives a list or a string.
fn lines(entry: &Value, key: &str) -> String {
    match entry.get(key) {
        Some(Value::Array(values)) => values
            .iter()
            .filter_map(Value::as_str)
            .map(|line| format!("- {line}"))
            .collect::<Vec<_>>()
            .join("\n"),
        Some(Value::String(value)) => value.clone(),
        _ => String::new(),
    }
}

fn string(entry: &Value, key: &str) -> String {
    entry
        .get(key)
        .and_then(Value::as_str)
        .unwrap_or_default()
        .to_string()
}

/// Reads the A-numbers an entry cross-references.
///
/// The encyclopedia's own citation graph: a `Cf.` line names the sequences
/// that describe the same structure differently, which is exactly the kind of
/// lead the frontier exists to hold.
fn cross_references(entry: &Value, from: &str) -> Vec<LinkRecord> {
    let text = format!("{} {}", lines(entry, "xref"), lines(entry, "comment"));
    let mut out: Vec<LinkRecord> = Vec::new();
    let bytes: Vec<char> = text.chars().collect();
    for (index, character) in bytes.iter().enumerate() {
        if *character != 'A' {
            continue;
        }
        let digits: String = bytes[index + 1..]
            .iter()
            .take(6)
            .take_while(char::is_ascii_digit)
            .collect();
        if digits.len() != 6 {
            continue;
        }
        let url = format!("https://oeis.org/A{digits}");
        if url.ends_with(from) || out.iter().any(|record| record.url == url) {
            continue;
        }
        out.push(LinkRecord {
            url,
            label: format!("A{digits}"),
            context: format!("cross-referenced from {from}"),
        });
    }
    out
}

fn truncate(text: &str, limit: usize) -> String {
    if text.chars().count() <= limit {
        return text.to_string();
    }
    let head: String = text.chars().take(limit).collect();
    format!("{}…", head.trim_end())
}

#[async_trait]
impl Tool<()> for OeisTool {
    fn name(&self) -> &'static str {
        "oeis_lookup"
    }

    fn description(&self) -> &'static str {
        "Looks an integer sequence this run has computed up in the OEIS, and files each matching \
         entry — its name, closed forms, recurrences, and cross-references — under research/. \
         Unlike a web search this needs no guess at what the subject is called: the terms either \
         match a catalogued sequence or they do not, and a match usually carries the closed form \
         that turns an enumeration into an evaluation. A miss is a result too — record it, so \
         nobody looks again."
    }

    fn schema(&self) -> ToolSchema {
        ToolSchema::new(
            self.name(),
            self.description(),
            json!({
                "type": "object",
                "properties": {
                    "terms": {
                        "type": "array",
                        "items": { "type": "integer" },
                        "minItems": 4,
                        "maxItems": MAX_TERMS,
                        "description": "Consecutive terms the run has actually computed, in \
                                        order and starting from the beginning of the sequence. \
                                        Four is the fewest worth sending; a wrong or invented \
                                        term matches nothing, so send only terms a program \
                                        produced."
                    }
                },
                "required": ["terms"],
                "additionalProperties": false
            }),
        )
    }

    async fn call(&self, _state: &(), call: ToolCall) -> Result<ToolResult> {
        self.schema().validate_call(&call)?;
        let terms: Vec<i64> = call
            .arguments
            .get("terms")
            .and_then(Value::as_array)
            .map(|values| {
                values
                    .iter()
                    .filter_map(Value::as_i64)
                    .take(MAX_TERMS)
                    .collect()
            })
            .unwrap_or_default();
        if terms.len() < 4 {
            return Err(tinyagents::TinyAgentsError::Validation(
                "send at least four consecutive computed terms; fewer matches everything".into(),
            ));
        }

        let entries = self.lookup(&terms).await?;
        if entries.is_empty() {
            return Ok(ToolResult::text(
                call.id,
                self.name(),
                format!(
                    "no OEIS entry matches {terms:?}. That is a finding, not a dead end: the \
                     sequence is not catalogued, so no closed form is going to be looked up and \
                     the structure has to come from the problem. Record it — in a note, or as a \
                     dead thread — so nobody searches for it again."
                ),
            ));
        }

        let mut report = String::new();
        for entry in &entries {
            let (id, body) = note(entry);
            let path = super::documents::research_path(
                self.documents.root(),
                &format!("oeis_{}.md", id.to_ascii_lowercase()),
            );
            // Filed rather than only reported: a formula quoted into a tool
            // result and nowhere else is a citation nobody can check later.
            let stored = self.documents.write_runtime(&path, &body).await.is_ok();
            super::frontier::record(
                &self.documents,
                &format!("https://oeis.org/{id}"),
                if stored { &path } else { "" },
                &cross_references(entry, &id),
                &self.documents.goal().await,
            )
            .await;
            let _ = writeln!(
                report,
                "- **{id}** — {}{}",
                entry
                    .get("name")
                    .and_then(Value::as_str)
                    .unwrap_or("(unnamed)"),
                if stored {
                    format!(" — filed at `{path}`")
                } else {
                    String::new()
                }
            );
        }
        Ok(ToolResult::text(
            call.id,
            self.name(),
            format!(
                "{} OEIS entr{} match these terms. Read the filed note for the closed form and \
                 check its hypotheses hold for this problem before using it; cross-referenced \
                 sequences were added to {}.\n\n{report}",
                entries.len(),
                if entries.len() == 1 { "y" } else { "ies" },
                super::frontier::FRONTIER_PATH
            ),
        ))
    }
}

#[cfg(test)]
mod test;
