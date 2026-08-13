
mod approaches;
mod authoring;
pub(crate) mod async_subagents;
mod backward;
mod caps;
mod checkpoint;
mod claims;
// The renderer writes files and pulls in raster encoders, so it is compiled
// only when somebody asks to draw the loop.
#[cfg(feature = "graph-debug")]
mod diagram;
mod definitions;
mod digest;
mod documents;
mod dossier;
mod exec;
mod folder_index;
mod frontier;
mod layout;
mod oeis;
mod patch;
// Test-only, and deliberately so: this exists to compare the two engines'
// decisions, and nothing a run does should ever call it.
#[cfg(test)]
mod parity;
mod paths;
mod patterns;
mod readable;
mod reflection_tool;
mod requests;
mod runner;
mod runs;
mod shared_context;
mod solutions;
mod teams;
mod text;
mod threads;
mod vector;
mod workflow;

use std::fmt::Write as _;
use std::path::{Path, PathBuf};
use std::sync::Arc;

use async_trait::async_trait;
use tinyagents::harness::message::estimate_slice_tokens;
use tinyagents::harness::middleware::ContextCompressionMiddleware;
use tinyagents::harness::model::{ChatModel, ModelRequest};
use tinyagents::harness::summarization::{
    CompressionProvenance, SummarizationPolicy, Summarizer, SummaryRecord, estimate_tokens,
    render_message_for_summary,
};

use crate::agent::accounting::AccountingModel;
use crate::agent::budget::RunBudget;
use crate::agent::reflection::ReflectionMiddleware;
use crate::agent::reroute::ReroutingModel;
use crate::agent::resilient::{BoundedTimeoutModel, ResilientTool};
use crate::agent::sticky::StickyProviderModel;
use crate::agent::trace::RunTracer;
use crate::agent::untruncated::UntruncatedModel;
use crate::agent::{
    AgentHarness, Message, ObservedAgent, Result, Tool, ToolCall, configure_run_budget,
    openrouter_model_from_env, openrouter_reasoning_model,
};
use crate::hello_agent::ExaSearchTool;
use async_subagents::AsyncSubagentManager;
use documents::WorkspaceDocuments;

use crate::directives;
use exec::ExecuteCommand;
use paths::strip_workspace_prefix;
use paths::{WriteToolFile, checked_workspace_path};
use patterns::PatternTool;
use vector::{
    NoteScratchTool, RecallMemoryTool, RecallScratchTool, RelateMemoryTool, RememberMemoryTool,
    VectorStore,
};

pub use authoring::WorkflowCatalog;
pub use runner::{SubagentAgentRunner, SubagentTaskRunner};
pub use tinyagents::harness::host::AgentDefinition;
#[cfg(feature = "graph-debug")]
pub use diagram::render_solution_loop;

/// Specialists the goals agent may delegate to.
const SPECIALISTS: [&str; 13] = [
    "research",
    "tool_builder",
    "coder",
    "sat_solver",
    "smt_solver",
    "theorem_prover",
    "symbolic_math",
    "lean_prover",
    "pattern_finder",
    "inventor",
    "reducer",
    "librarian",
    "scholar",
];

/// Agents the pattern agent may commission work from.
///
/// Only the tool-builder. A sequence check that needs more terms than the
/// pattern agent should compute inline is a programming job, and that is the
/// role that does programming jobs. Nothing else is offered, because every
/// further delegate is a way for a bounded structural question to turn into a
/// second investigation running beside the first.
const PATTERN_DELEGATES: [&str; 1] = ["tool_builder"];

/// Agents the inventor may delegate to.
///
/// Only research, and that is the whole point rather than a restriction. A new
/// line of attack has to be two things at once: different from what this run
/// has tried, and not something the literature already closed. The inventor
/// knows the first and cannot know the second; research knows the second and
/// has no view on the first. The solution loop passes candidates between them
/// at a diversify, and this bench is the same exchange available mid-thought,
/// for the single check that would settle whether an idea is worth writing
/// down at all.
///
/// Recursion is bounded at one level by construction, not by instruction:
/// research holds no delegation tools, so nothing it is handed can spawn
/// further. That is why this is safe to grant to a role whose job is to
/// generate possibilities.
const INVENTION_BENCH: [&str; 1] = ["research"];

/// Roles that run on the stronger reasoning model rather than the run's
/// default.
///
/// The test for membership is two questions, and a role has to pass both. Is
/// its output a *judgement* no tool can check — as against a report of what a
/// program did, which the method policy already routes through something
/// mechanical? And is it cheap: short output, few calls, and not on a schedule?
///
/// - `inventor` — whether a reformulation is genuinely different, whether a
///   theorem's hypotheses hold here, whether the literature suggests something
///   better than what was proposed. Runs only at a diversify.
/// - `reducer` — whether a set of lemmas actually implies the goal. That is the
///   definition of a judgement no tool can check: a decomposition into three
///   attractive statements that do not recombine reads exactly like one that
///   does. It writes one file and is opened at most a handful of times in a run.
/// - `judge` — scores how an attempt was conducted and rarely stops the run.
///   Capped at twelve calls and five minutes, and answers in four lines.
/// - `reflection` — solved, progressed, and now what *kind* of progress. That
///   last one decides whether a run reporting progress every attempt is sent to
///   diversify anyway, and telling a new bound from a new fact is exactly the
///   subtle call a fast model gets wrong. Its output is three fields and a
///   sentence.
/// - `director` — reads a human directive against what the run is doing.
///   Housekeeping's budget, and it only wakes when somebody steers.
///
/// Deliberately excluded, each for a stated reason. `context_curator` is a
/// judgement role and fails the second question outright: it is the measured
/// top consumer of a run, once at 28 model calls, and it runs on a schedule.
/// `scholar` and `research` read whole documents, so their turns are large.
/// `pattern_finder` and the code writers execute rather than judge, and the
/// planners drive every turn of the run.
const REASONING_ROLES: [&str; 5] = ["inventor", "reducer", "judge", "reflection", "director"];

/// Agents the top-level orchestrator may delegate to directly.
const DELEGATES: [&str; 15] = [
    "research",
    "tool_builder",
    "coder",
    "sat_solver",
    "smt_solver",
    "theorem_prover",
    "symbolic_math",
    "lean_prover",
    "goals",
    "reflection",
    "pattern_finder",
    "inventor",
    "reducer",
    "librarian",
    "scholar",
];

const COMPRESSION_TRIGGER_TOKENS: u64 = 300_000;
const RECENT_MESSAGES_TO_KEEP: usize = 12;
const MAX_WORKSPACE_CONTEXT_BYTES: usize = 256 * 1024;

/// The discipline every role shares: understand the problem and gather context
/// before computing, and never search the answer space directly.
///
/// The bar for these problems is a structural result, not a large loop. A
/// search over candidate answers is the failure mode this text exists to
/// prevent, and it is stated as a rule about the *shape* of the method rather
/// than about asymptotics, because the naive method for a problem whose input
/// is a single bound is usually "linear in that bound" and still hopeless.
const SHARED_METHOD_POLICY: &str = include_str!("../prompts/method_policy.md");

const ORCHESTRATOR_PROMPT: &str = include_str!("../prompts/orchestrator.md");

const RESEARCH_PROMPT: &str = include_str!("../prompts/research.md");

const TOOL_BUILDER_PROMPT: &str = include_str!("../prompts/tool_builder.md");
const CODER_PROMPT: &str = include_str!("../prompts/coder.md");
const SAT_SOLVER_PROMPT: &str = include_str!("../prompts/sat_solver.md");
const SMT_SOLVER_PROMPT: &str = include_str!("../prompts/smt_solver.md");
const THEOREM_PROVER_PROMPT: &str = include_str!("../prompts/theorem_prover.md");
const SYMBOLIC_MATH_PROMPT: &str = include_str!("../prompts/symbolic_math.md");
const LEAN_PROVER_PROMPT: &str = include_str!("../prompts/lean_prover.md");

const REFLECTION_PROMPT: &str = include_str!("../prompts/reflection.md");

const JUDGE_PROMPT: &str = include_str!("../prompts/judge.md");

const PATTERN_PROMPT: &str = include_str!("../prompts/pattern_finder.md");

const INVENTOR_PROMPT: &str = include_str!("../prompts/inventor.md");

/// The role that works backward from the goal rather than forward from what the
/// run holds.
const REDUCER_PROMPT: &str = include_str!("../prompts/reducer.md");

const LIBRARIAN_PROMPT: &str = include_str!("../prompts/librarian.md");

const SCHOLAR_PROMPT: &str = include_str!("../prompts/scholar.md");

const CONTEXT_CURATOR_PROMPT: &str = include_str!("../prompts/context_curator.md");

/// The role that turns one operator directive into changes across the workspace.
const DIRECTOR_PROMPT: &str = include_str!("../prompts/director.md");

const GOALS_PROMPT: &str = include_str!("../prompts/goals.md");

/// A small in-memory catalogue of named, executable child agents.
#[derive(Default)]
pub struct AgentRegistry {
    entries: Vec<RegisteredAgent>,
}

struct RegisteredAgent {
    definition: AgentDefinition,
}

impl std::fmt::Debug for AgentRegistry {
    fn fmt(&self, formatter: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        formatter
            .debug_struct("AgentRegistry")
            .field("agents", &self.names())
            .finish()
    }
}

impl AgentRegistry {
    /// Creates an empty registry.
    #[must_use]
    pub fn new() -> Self {
        Self::default()
    }

    /// Registers one asynchronous agent's model-visible metadata.
    ///
    /// # Errors
    ///
    /// Returns an error when the id is empty or is already registered.
    pub fn register(&mut self, definition: AgentDefinition) -> Result<&mut Self> {
        if definition.id.trim().is_empty() {
            return Err(tinyagents::TinyAgentsError::Validation(
                "agent id cannot be empty".into(),
            ));
        }
        if self.contains(&definition.id) {
            return Err(tinyagents::TinyAgentsError::Validation(format!(
                "agent `{}` is already registered",
                definition.id
            )));
        }
        self.entries.push(RegisteredAgent { definition });
        Ok(self)
    }

    /// Returns whether `id` is registered.
    #[must_use]
    pub fn contains(&self, id: &str) -> bool {
        self.entries.iter().any(|entry| entry.definition.id == id)
    }

    /// Returns registered ids in stable insertion order.
    #[must_use]
    pub fn names(&self) -> Vec<&str> {
        self.entries
            .iter()
            .map(|entry| entry.definition.id.as_str())
            .collect()
    }

    /// Returns the model-visible definitions in stable insertion order.
    #[must_use]
    pub fn definitions(&self) -> Vec<&AgentDefinition> {
        self.entries.iter().map(|entry| &entry.definition).collect()
    }

    /// Resolves an agent definition by id.
    #[must_use]
    pub fn get(&self, id: &str) -> Option<&AgentDefinition> {
        self.entries
            .iter()
            .find(|entry| entry.definition.id == id)
            .map(|entry| &entry.definition)
    }
}

/// OpenRouter-backed orchestrator over the registered specialist agents.
pub struct OrchestratorAgent {
    inner: ObservedAgent,
    registry: Arc<AgentRegistry>,
    system_prompt: String,
    subagents: AsyncSubagentManager,
    tracer: Arc<RunTracer>,
    workspace: PathBuf,
    memory: VectorStore,
}

impl OrchestratorAgent {
    /// This orchestrator's specialists, offered to `TinyFlows` as background
    /// work a workflow can start and not wait for.
    ///
    /// The registry is already populated when this is called, so the runner
    /// starts exactly the roles this orchestrator knows — a workflow cannot
    /// spawn a specialist that was never registered, and finds that out at the
    /// spawn rather than at a gate.
    ///
    /// Public because the caller is outside this crate by definition: it is a
    /// host assembling `TinyFlows` capabilities for a workflow run. Nothing in
    /// this crate's own solution loop uses it — that loop is built on the
    /// state-graph runtime, which has no `spawn` node. See
    /// [`crate::agent::flow`].
    #[must_use]
    pub fn task_runner(&self) -> SubagentTaskRunner {
        SubagentTaskRunner::new(self.subagents.clone())
    }

    /// The capability bundle a `TinyFlows` workflow run is handed.
    ///
    /// `tools` is the run's authority and is deliberately a parameter rather
    /// than this orchestrator's whole registry: a `tool_call` node can reach
    /// anything the bundle holds, so handing over everything would dissolve the
    /// per-role tool boundaries this crate maintains. Pass exactly what the
    /// workflow may use.
    ///
    /// State is kept under this orchestrator's workspace, and background work
    /// goes to its specialists. Execution and outbound HTTP are refused — see
    /// `caps::execution` and `caps::network` for why that is a decision rather
    /// than an omission.
    ///
    /// The roles a workflow may name in an `agent_ref`, derived from this
    /// orchestrator's own registry.
    ///
    /// Derived rather than restated, so a workflow's view of what a role may
    /// touch cannot drift from the run's. See `definitions` for why that is the
    /// one thing this must not be a second list of.
    #[must_use]
    pub fn workflow_agents(&self) -> Vec<tinyflows::model::AgentDefinition> {
        definitions::workflow_agents(&self.registry)
    }

    /// The solution loop as a workflow graph.
    ///
    /// The same attempt/judge/reflect loop the run executes, authored
    /// declaratively: a `loop` head carrying the counters as its accumulator,
    /// `switch` nodes carrying the routing ladder as jq, and the diversify arms
    /// as parallel successors converging on a `merge`. Every threshold in it is
    /// the Rust constant, generated rather than typed, so the document and the
    /// running loop cannot disagree about a number.
    ///
    /// Not yet what a run executes — the state graph still is. This is the
    /// document that has to be proven equivalent to it first.
    #[must_use]
    pub fn workflow_graph(&self, problem: &str) -> tinyflows::model::WorkflowGraph {
        workflow::solution_loop(problem, self.workflow_agents())
    }

    /// # Errors
    ///
    /// Returns an error when the provider model cannot be configured from the
    /// environment.
    pub fn workflow_capabilities(
        &self,
        tools: impl IntoIterator<Item = Arc<dyn Tool<()>>>,
    ) -> Result<tinyflows::caps::Capabilities> {
        // The reflection parser is added rather than left to the caller. It is
        // not a tool a workflow author chooses — the loop cannot route without
        // it, and a caller who forgot it would get a graph that runs, folds
        // nulls, and never leaves the first verdict.
        let tools = tools.into_iter().chain(std::iter::once(Arc::new(
            reflection_tool::ParseReflection::new(Some(self.workspace.clone())),
        )
            as Arc<dyn Tool<()>>));
        Ok(caps::bundle(
            openrouter_model_from_env()?,
            &self.workspace,
            tools,
            self.task_runner(),
            SubagentAgentRunner::new(self.subagents.clone()),
        ))
    }
}

impl std::fmt::Debug for OrchestratorAgent {
    fn fmt(&self, formatter: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        formatter
            .debug_struct("OrchestratorAgent")
            .field("registry", &self.registry)
            .finish_non_exhaustive()
    }
}
