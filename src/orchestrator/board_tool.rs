//! The `post_board` tool.
//!
//! Given to the roles that discover something worth interrupting another school
//! for — the reflection that just learned why an attempt failed, the inventor
//! that just closed a line of attack, the goals agent that is about to spend a
//! run on something a sibling has already tried.
//!
//! # The sender is not an argument
//!
//! The posting school is baked into the tool instance at registration and is
//! **not** a field the model fills in. A school able to name its own sender
//! could attribute a hunch to a sibling, and the board's whole value is that a
//! reader can tell who found what — a dead end reported by the school that
//! actually walked into it is evidence, and the same sentence attributed to
//! nobody in particular is noise. This is the same reasoning that keeps every
//! other authority boundary here in code rather than in a prompt.
//!
//! # It cannot establish anything
//!
//! A post is asserted, not established. Nothing this tool writes reaches
//! `research/CLAIMS.md`, and it deliberately has no way to: filing a claim
//! means writing a note with hypotheses and a status, which is a different tool
//! and a different standard. See [`super::board`] for why the board exists
//! anyway.

use std::sync::Arc;

use async_trait::async_trait;
use serde_json::{Value, json};

use super::board::{self, Kind};
use crate::agent::{Result, Tool, ToolCall, ToolResult, ToolSchema};
use crate::orchestrator::documents::WorkspaceDocuments;

/// Posts a note from one school to the others.
#[derive(Debug)]
pub(crate) struct BoardTool {
    documents: WorkspaceDocuments,
    /// The school this instance posts as. See the module documentation.
    from: String,
}

impl BoardTool {
    /// Builds the tool set this module contributes for one school.
    pub(in crate::orchestrator) fn all(
        documents: &WorkspaceDocuments,
        from: &str,
    ) -> Vec<Arc<dyn Tool<()>>> {
        vec![Arc::new(Self {
            documents: documents.clone(),
            from: from.to_string(),
        })]
    }
}

#[async_trait]
impl Tool<()> for BoardTool {
    fn name(&self) -> &'static str {
        "post_board"
    }

    fn description(&self) -> &'static str {
        "Tells the other schools working this problem something they would otherwise pay to \
         discover for themselves. Use it the moment a line of attack dies, with the reason — a \
         dead end found once should be paid for once. Half-formed is welcome here and nowhere \
         else: a hunch posted now is worth more than a certainty posted after the run. This is \
         not a claim and is never filed as one; when something becomes established, write the \
         note."
    }

    fn schema(&self) -> ToolSchema {
        let kinds: Vec<&str> = Kind::ALL.iter().map(|kind| kind.label()).collect();
        ToolSchema::new(
            self.name(),
            self.description(),
            json!({
                "type": "object",
                "properties": {
                    "kind": {
                        "type": "string",
                        "enum": kinds,
                        "description": "dead-end: something that did not work, with the reason — \
                                        the most valuable kind. lesson: something learned that is \
                                        not yet a claim. hunch: a suspicion, offered because it is \
                                        unfinished. offer: something you have that another school \
                                        may want. ask: something you want and cannot reach."
                    },
                    "body": {
                        "type": "string",
                        "description": "What the other schools need to know, in a few sentences. \
                                        For a dead end, say what was tried and what killed it — \
                                        'it needs f to be D-finite and it is not' saves an \
                                        attempt; 'that approach failed' saves nothing."
                    },
                    "refers": {
                        "type": "array",
                        "items": { "type": "string" },
                        "description": "Claim ids, thread slugs or workspace paths this is about. \
                                        Optional."
                    }
                },
                "required": ["kind", "body"],
                "additionalProperties": false
            }),
        )
    }

    async fn call(&self, _state: &(), call: ToolCall) -> Result<ToolResult> {
        self.schema().validate_call(&call)?;
        let body = string(&call.arguments, "body");
        let kind = Kind::parse(&string(&call.arguments, "kind"));
        let refers: Vec<String> = call
            .arguments
            .get("refers")
            .and_then(Value::as_array)
            .map(|items| {
                items
                    .iter()
                    .filter_map(Value::as_str)
                    .map(ToOwned::to_owned)
                    .collect()
            })
            .unwrap_or_default();
        board::post(self.documents.root(), &self.from, kind, &body, &refers)?;
        board::refresh(&self.documents).await;
        Ok(ToolResult::text(
            call.id,
            self.name(),
            format!(
                "posted a {} to {} as `{}`",
                kind.label(),
                board::PATH,
                self.from
            ),
        ))
    }
}

fn string(arguments: &Value, name: &str) -> String {
    arguments
        .get(name)
        .and_then(Value::as_str)
        .unwrap_or_default()
        .to_string()
}

#[cfg(test)]
#[path = "board_tool_test.rs"]
mod test;
