//! The `request_research` tool.
//!
//! Given to every role, because the role that discovers a gap is whichever one
//! walked into it — a solver whose recurrence will not close, a tool-builder
//! whose complexity bound needs a theorem, a pattern agent whose conjecture
//! needs a name. Confining it to the research roles would mean the gap is
//! stated by whoever is going looking rather than by whoever is stuck, which
//! is how a search ends up aimed at the subject instead of at the question.
//!
//! It cannot fetch anything. Stating a need and going to find it are different
//! jobs, and keeping them apart is what lets the run see demand it has not yet
//! met.

use std::sync::Arc;

use async_trait::async_trait;
use serde_json::{Value, json};

use super::post;
use crate::agent::{Result, Tool, ToolCall, ToolResult, ToolSchema};
use crate::orchestrator::documents::WorkspaceDocuments;

/// Records a gap the run has walked into.
#[derive(Debug)]
pub(crate) struct RequestTool {
    documents: WorkspaceDocuments,
}

impl RequestTool {
    /// Builds the tool set this module contributes.
    pub(in crate::orchestrator) fn all(documents: &WorkspaceDocuments) -> Vec<Arc<dyn Tool<()>>> {
        vec![Arc::new(Self {
            documents: documents.clone(),
        })]
    }
}

#[async_trait]
impl Tool<()> for RequestTool {
    fn name(&self) -> &'static str {
        "request_research"
    }

    fn description(&self) -> &'static str {
        "Records something this run needs from outside it and cannot derive: a theorem's exact \
         statement, a classification, a standard treatment, a catalogued sequence. Checks the \
         library first and answers from it when it can, so state the gap precisely rather than \
         naming a subject. It does not search — it records demand, which is what lets a later \
         search be aimed at the question rather than at the topic."
    }

    fn schema(&self) -> ToolSchema {
        ToolSchema::new(
            self.name(),
            self.description(),
            json!({
                "type": "object",
                "properties": {
                    "need": {
                        "type": "string",
                        "description": "The specific thing that is missing. Not a subject — a \
                                        question a source could answer or fail to."
                    },
                    "why": {
                        "type": "string",
                        "description": "What you would do with it: the step it unblocks, or the \
                                        computation it makes possible."
                    },
                    "falsifies": {
                        "type": "string",
                        "description": "What would show the belief you are working from is \
                                        wrong. The most useful field: it turns a topic into a \
                                        question, and it is what a later search is aimed at."
                    }
                },
                "required": ["need", "why"],
                "additionalProperties": false
            }),
        )
    }

    async fn call(&self, _state: &(), call: ToolCall) -> Result<ToolResult> {
        self.schema().validate_call(&call)?;
        let need = string(&call.arguments, "need");
        if need.trim().is_empty() {
            return Err(tinyagents::TinyAgentsError::Validation(
                "need must say what is missing".into(),
            ));
        }
        let output = post(
            &self.documents,
            &call.agent_hint(),
            &need,
            &string(&call.arguments, "why"),
            &string(&call.arguments, "falsifies"),
        )
        .await;
        Ok(ToolResult::text(call.id, self.name(), output))
    }
}

fn string(arguments: &Value, name: &str) -> String {
    arguments
        .get(name)
        .and_then(Value::as_str)
        .unwrap_or_default()
        .to_string()
}
