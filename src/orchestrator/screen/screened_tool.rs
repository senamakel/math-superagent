//! The decorator that puts the screen in front of a tool.
//!
//! Wraps any [`Tool`], screening the arguments before the call and the result
//! text after it, and returns a neutral refusal in place of anything withheld.
//!
//! # Why a decorator, and why at construction
//!
//! The alternative was middleware on the harness. That would have covered the
//! agent path and missed the workflow path: `caps::tools::WorkspaceTools` is
//! built from the same `Arc<dyn Tool<()>>` values and invokes them directly,
//! with no harness and no middleware stack in between. Wrapping the `Arc` where
//! it is *created* means both paths get the same object, and there is no second
//! place to remember.
//!
//! It also puts the screen inside `ResilientTool` rather than outside it, which
//! is the right order: a refusal here is an ordinary result the model reads and
//! acts on, not an error to be converted into one.
//!
//! # What the refusal says, and what it must not
//!
//! It says a screen exists. That is deliberate — a run told nothing would
//! retry the same query in different words until its budget ran out, and the
//! screen would then be measuring the run's persistence rather than its
//! mathematics.
//!
//! It never says what matched. Naming the withheld term in a tool result puts
//! it straight into the model's context, which is the single thing this whole
//! mechanism exists to prevent, and it would make the hashed blocklist
//! pointless.

use std::path::PathBuf;
use std::sync::Arc;
use std::time::Duration;

use async_trait::async_trait;
use serde_json::Value;
use tinyagents::harness::model::ChatModel;
use tinyagents::harness::tool::ToolPolicy;

use super::adjudicator::{self, Ruling};
use super::ledger::{self, Entry, Stage};
use super::policy::{ScreenPolicy, Verdict};
use crate::agent::{Result, Tool, ToolCall, ToolResult, ToolSchema};

/// What a screened call returns in place of the arguments it refused.
const REFUSED_ARGUMENTS: &str = "\
This call was not made. It was withheld by the run's evidence policy, which \
screens sources that would supply a published answer to the problem in \
`problem.md`.

This is expected and is not a fault in your reasoning. Do not rephrase the \
query to get around it, and do not try another route to the same source — the \
policy is enforced in the runtime and at the network boundary, so it will \
refuse those too, and the attempts are recorded.

Establish the point yourself instead: derive it, compute it, or find a primary \
source that develops the technique rather than one that reports the result.";

/// What a call naming an unreachable host returns.
///
/// Deliberately different from [`REFUSED_ARGUMENTS`]. Nothing is being withheld
/// here — the host is simply outside what this run's network boundary permits —
/// and saying so is what lets the run stop retrying and reach for a tool that
/// works. A live run failed sixteen downloads out of sixteen against a
/// transport error that carried none of this.
const UNREACHABLE_HOST: &str = "\
This call was not made. That host is not reachable from this run: the network \
boundary permits only the search and data APIs, so publisher and preprint sites \
fail regardless of the URL.

This is a property of the environment, not of the source, and not a finding \
about the mathematics. Retrying, or trying a mirror, will fail the same way.

Fetch the same material with `read_sources` or `deep_research`, which retrieve \
server-side and return the text. If a source is genuinely unreachable by any \
route, record the gap in `research/FRONTIER.md` and move on.";

/// The tools whose URL argument is a destination this container dials itself.
///
/// The distinction decides whether the egress allowlist has anything to say
/// about a call, and getting it wrong is not a harmless over-block. Every other
/// URL-taking tool here hands the URL to a *remote* API — `read_sources`,
/// `deep_research`, `find_similar_sources` and `citation_graph` all post it to
/// `api.exa.ai` or `api.openalex.org`, which fetch server-side and return text.
/// The proxy never sees `arxiv.org` on those calls and could not block them if
/// it wanted to, so refusing one for reachability withholds a source the screen
/// was perfectly placed to adjudicate on its actual contents instead.
///
/// A live run showed the shape: [`UNREACHABLE_HOST`] tells the caller to fetch
/// the same material with `read_sources`, and `read_sources` then refused the
/// same host — eleven times. An instruction the runtime immediately
/// contradicts is worse than no instruction, and the run has no way to tell
/// that the second refusal was a bug rather than the policy.
const DIALS_ITS_OWN_URL: [&str; 1] = ["download_document"];

/// What a screened call returns in place of a result it refused.
const REFUSED_RESULT: &str = "\
The source was reached but its contents were withheld by the run's evidence \
policy, which screens material that would supply a published answer to the \
problem in `problem.md`.

This is expected and is not a fault in your reasoning. Do not look for another \
copy of this source. Record the gap in `research/FRONTIER.md` if it matters, \
and establish the point by derivation, computation, or a source that develops \
the technique rather than reporting the result.";

/// A tool whose arguments and results pass through the evidence screen.
pub(crate) struct ScreenedTool {
    inner: Arc<dyn Tool<()>>,
    policy: Arc<ScreenPolicy>,
    /// The workspace root, where the ledger is written.
    workspace: PathBuf,
    /// The de-named problem statement handed to the adjudicator. Read once at
    /// construction: `problem.md` is seeded before the run starts and the file
    /// the adjudicator needs is the statement, not whatever the run has since
    /// written beside it.
    problem: Arc<String>,
    /// The model the adjudicator uses. `None` disables the semantic stage, in
    /// which case flagged text is delivered — the deterministic stage remains
    /// the control either way.
    model: Option<Arc<dyn ChatModel<()>>>,
}

impl std::fmt::Debug for ScreenedTool {
    fn fmt(&self, formatter: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        formatter
            .debug_struct("ScreenedTool")
            .field("tool", &self.inner.name())
            .field("problem", &self.policy.slug)
            .field("adjudicator", &self.model.is_some())
            .finish_non_exhaustive()
    }
}

impl ScreenedTool {
    /// Wraps `inner` so its arguments and results are screened.
    pub(crate) fn new(
        inner: Arc<dyn Tool<()>>,
        policy: Arc<ScreenPolicy>,
        workspace: PathBuf,
        problem: Arc<String>,
        model: Option<Arc<dyn ChatModel<()>>>,
    ) -> Self {
        Self {
            inner,
            policy,
            workspace,
            problem,
            model,
        }
    }

    /// Records one decision in the workspace ledger.
    fn record(&self, stage: Stage, decision: &'static str, detail: String) {
        ledger::record(
            &self.workspace,
            &Entry {
                tool: self.inner.name().to_string(),
                stage,
                decision,
                detail,
            },
        );
    }

    /// Screens the arguments of a call, before it runs.
    ///
    /// Three checks. Any URL-shaped argument is tested against the host
    /// denylist, so a denied source is refused here rather than surfacing later
    /// as an opaque proxy error. If this tool dials its own URL — see
    /// [`DIALS_ITS_OWN_URL`], and only `download_document` does — the URL is
    /// also tested for reachability, because that call really will fail at the
    /// proxy and saying so beats a transport error. Then the whole argument
    /// object is screened as text, which is what catches a query that names the
    /// thing being looked up.
    async fn screen_arguments(&self, arguments: &Value) -> Option<String> {
        for url in url_arguments(arguments) {
            if self.policy.denies_host(&url) {
                let host = url.split('/').nth(2).unwrap_or("").to_string();
                self.record(Stage::Arguments, "denied-host", format!("host `{host}`"));
                return Some(REFUSED_ARGUMENTS.to_string());
            }
            if DIALS_ITS_OWN_URL.contains(&self.inner.name()) && self.policy.host_unreachable(&url)
            {
                let host = url.split('/').nth(2).unwrap_or("").to_string();
                self.record(
                    Stage::Arguments,
                    "unreachable-host",
                    format!("host `{host}` is not on the egress allowlist"),
                );
                return Some(UNREACHABLE_HOST.to_string());
            }
        }

        let rendered = arguments.to_string();
        match self.policy.screen_text(&rendered) {
            Verdict::Allow => None,
            Verdict::Deny => {
                self.record(Stage::Arguments, "denied", "term matched".to_string());
                Some(REFUSED_ARGUMENTS.to_string())
            }
            Verdict::Adjudicate => match self.adjudicate(&rendered).await {
                Ruling::Allow => {
                    self.record(
                        Stage::Arguments,
                        "allowed-by-adjudicator",
                        "flagged, then allowed".to_string(),
                    );
                    None
                }
                Ruling::Deny => Some(REFUSED_ARGUMENTS.to_string()),
            },
        }
    }

    /// Runs the semantic stage, recording whatever it decides.
    ///
    /// With no model configured the flagged text is allowed: the deterministic
    /// stage is the control, and a missing adjudicator must not silently
    /// promote every flag into a denial — `[flag]` terms are chosen precisely
    /// because they are too common to block.
    async fn adjudicate(&self, text: &str) -> Ruling {
        let Some(model) = self.model.as_ref() else {
            return Ruling::Allow;
        };
        let bounded: String = text
            .chars()
            .take(self.policy.adjudicator_max_chars)
            .collect();
        let (ruling, note) = adjudicator::adjudicate(
            model,
            &self.problem,
            &bounded,
            Duration::from_secs(self.policy.adjudicator_timeout_seconds),
        )
        .await;
        if ruling == Ruling::Deny {
            self.record(Stage::Result, "denied-by-adjudicator", note);
        }
        ruling
    }
}

#[async_trait]
impl Tool<()> for ScreenedTool {
    fn name(&self) -> &str {
        self.inner.name()
    }

    fn description(&self) -> &str {
        self.inner.description()
    }

    fn schema(&self) -> ToolSchema {
        self.inner.schema()
    }

    /// Forwards the wrapped tool's safety classification.
    ///
    /// Falling back to the default would declassify every network tool this
    /// wrapper is put in front of, which is the opposite of the point.
    fn policy(&self) -> ToolPolicy {
        self.inner.policy()
    }

    fn display_label(&self, call: &ToolCall) -> Option<String> {
        self.inner.display_label(call)
    }

    fn display_detail(&self, call: &ToolCall) -> Option<String> {
        self.inner.display_detail(call)
    }

    async fn call(&self, state: &(), call: ToolCall) -> Result<ToolResult> {
        let call_id = call.id.clone();
        let name = self.inner.name().to_string();

        if let Some(refusal) = self.screen_arguments(&call.arguments).await {
            return Ok(ToolResult::text(call_id, name, refusal));
        }

        let result = self.inner.call(state, call).await?;

        // An error result carries the tool's own diagnostic, not fetched
        // material, so there is nothing to screen and screening it would turn
        // a useful failure message into a refusal the model cannot act on.
        if result.error.is_some() {
            return Ok(result);
        }

        match self.policy.screen_text(&result.content) {
            Verdict::Allow => Ok(result),
            Verdict::Deny => {
                self.record(
                    Stage::Result,
                    "denied",
                    format!("term matched in {} characters", result.content.len()),
                );
                Ok(ToolResult::text(call_id, name, REFUSED_RESULT.to_string()))
            }
            Verdict::Adjudicate => match self.adjudicate(&result.content).await {
                Ruling::Allow => {
                    self.record(
                        Stage::Result,
                        "allowed-by-adjudicator",
                        format!("flagged, then allowed ({} characters)", result.content.len()),
                    );
                    Ok(result)
                }
                Ruling::Deny => Ok(ToolResult::text(call_id, name, REFUSED_RESULT.to_string())),
            },
        }
    }
}

/// Every URL-shaped string anywhere in an argument object.
///
/// Walks the whole value rather than looking at known field names, because the
/// tools being screened spell the field `url`, `urls`, `source`, and `links`,
/// and a new one would otherwise be missed silently.
fn url_arguments(arguments: &Value) -> Vec<String> {
    fn walk(value: &Value, found: &mut Vec<String>) {
        match value {
            Value::String(text) => {
                if text.starts_with("http://") || text.starts_with("https://") {
                    found.push(text.clone());
                }
            }
            Value::Array(entries) => entries.iter().for_each(|entry| walk(entry, found)),
            Value::Object(fields) => fields.values().for_each(|field| walk(field, found)),
            _ => {}
        }
    }
    let mut found = Vec::new();
    walk(arguments, &mut found);
    found
}

#[cfg(test)]
#[path = "screened_tool_test.rs"]
mod test;
