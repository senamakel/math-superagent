//! The `search_claims` tool.
//!
//! It travels with the document tools rather than being granted to one role,
//! for the same reason the index tools do: every agent that can read the
//! library can ask what the library establishes, and confining the question to
//! the scholar would make every other role re-read notes to recover a
//! statement somebody has already written down.
//!
//! It is read-only. Deciding what a source establishes is a judgement and
//! belongs in a note; this only reports what the notes already say.

use std::sync::Arc;

use async_trait::async_trait;
use serde_json::{Value, json};

use super::{CLAIMS_PATH, detail, refresh};
use crate::agent::{Result, Tool, ToolCall, ToolResult, ToolSchema};
use crate::orchestrator::documents::WorkspaceDocuments;

/// Reports what the library establishes, claim by claim.
#[derive(Debug)]
pub(crate) struct ClaimsTool {
    documents: WorkspaceDocuments,
}

impl ClaimsTool {
    /// Builds the tool set this module contributes.
    pub(in crate::orchestrator) fn all(documents: &WorkspaceDocuments) -> Vec<Arc<dyn Tool<()>>> {
        vec![Arc::new(Self {
            documents: documents.clone(),
        })]
    }
}

#[async_trait]
impl Tool<()> for ClaimsTool {
    fn name(&self) -> &'static str {
        "search_claims"
    }

    fn description(&self) -> &'static str {
        "Searches what the reference library establishes, one claim at a time, returning each \
         claim's statement, its hypotheses, whether they hold for this problem, what evidence \
         stands behind it, and which note to check. Call it before re-deriving a result or \
         re-reading a source. With no query it re-derives the whole ledger and reports what it \
         found, including contradictions between claims and claims taken to hold here on a \
         source's word alone."
    }

    fn schema(&self) -> ToolSchema {
        ToolSchema::new(
            self.name(),
            self.description(),
            json!({
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "What the claim should be about — an object, a theorem \
                                        name, or a quantity. Omit to re-derive the whole ledger."
                    }
                },
                "additionalProperties": false
            }),
        )
    }

    async fn call(&self, _state: &(), call: ToolCall) -> Result<ToolResult> {
        self.schema().validate_call(&call)?;
        // Derived on every call rather than read from the file: the ledger's
        // whole value is that it agrees with the notes, and a search answering
        // from a stale table would be the one failure mode it exists to
        // prevent.
        let ledger = refresh(&self.documents).await;
        let query = call
            .arguments
            .get("query")
            .and_then(Value::as_str)
            .unwrap_or_default()
            .trim()
            .to_string();
        let output = if query.is_empty() {
            format!(
                "re-derived {CLAIMS_PATH} from the notes under research/.\n\n{}",
                ledger.render()
            )
        } else {
            let found = ledger.search(&query);
            if found.is_empty() {
                format!(
                    "no claim in the library matches `{query}`. Either nobody has written one \
                     down — a source read but not turned into a claim block leaves the run \
                     nothing to retrieve — or the library does not cover it and this is a gap \
                     worth naming."
                )
            } else {
                found
                    .into_iter()
                    .map(detail)
                    .collect::<Vec<_>>()
                    .join("\n")
            }
        };
        Ok(ToolResult::text(call.id, self.name(), output))
    }
}
