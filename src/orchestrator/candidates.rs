//! Several candidate solutions, each on its own branch and its own checkout.
//!
//! An attempt is serial by design: attempt, judge, route, attempt, so each one
//! is briefed by the lesson of the last. That is right when the next move
//! follows from the last one's failure, and wrong when it does not — when the
//! run has five plausible programs and no argument for preferring one, the
//! serial loop spends five attempts learning what five concurrent ones would
//! learn at once.
//!
//! This is the concurrent case. `spawn_candidates` gives each candidate a git
//! branch, a checkout of its own, and a slot's worth of tools rooted at that
//! checkout — so five of them write `code/solution.py` at the same time without
//! writing the same file. [`super::vcs_tool`] is how the archivist reads the
//! results back and keeps one.
//!
//! # What forks and what does not
//!
//! **Forked:** everything in the workspace tree. Each candidate's checkout is a
//! linked worktree, so it has its own `code/`, its own `research/`, and its own
//! ledgers. A candidate recording a task records it in its own file.
//!
//! **Shared:** memory. `remember_memory` and `recall_memory` reach a store that
//! lives outside the workspace entirely — a different container on a shared
//! network — so nothing here re-roots them and nothing needs to. That is the
//! split that makes concurrency worth having: candidates must not overwrite each
//! other's files, and they *should* see what each other established.
//!
//! # Why the slots are fixed
//!
//! A subagent's harness is registered once, at container start, with its tools
//! already built and already rooted. There is no way to root a tool at a
//! directory chosen later in the run, so the directories are chosen up front:
//! [`SLOTS`] of them, `attempts/01` … `attempts/06`, each with a role registered
//! against it. A slot is reused once its candidate is decided, which is what
//! `abandon_attempt` frees.
//!
//! Six rather than ten. The point of this is a handful of *educated* guesses —
//! programs a role had a reason to write — not a population to be sampled, which
//! is what [`super::search`] is for and is scored rather than reviewed.

use std::fmt::Write as _;
use std::path::{Path, PathBuf};
use std::sync::Arc;

use async_trait::async_trait;
use serde_json::{Value, json};

use super::async_subagents::AsyncSubagentManager;
use super::vcs::{ATTEMPT_PREFIX, ATTEMPTS_DIR, Git, TRUNK};
use crate::agent::{Result, Tool, ToolCall, ToolResult, ToolSchema};

/// How many candidates may exist at once.
///
/// Each is a registered role and a directory, so this is a real cost paid at
/// start whether or not a run uses them. Six is more than any observed round
/// has wanted and small enough that the registry stays readable.
pub(super) const SLOTS: usize = 6;

/// The slot ids, in order. Zero-padded so they sort as they read.
pub(super) fn slots() -> Vec<String> {
    (1..=SLOTS).map(|n| format!("{n:02}")).collect()
}

/// The role name that works in slot `id`.
pub(super) fn role_for(id: &str) -> String {
    format!("candidate{id}")
}

/// Where slot `id` is checked out, relative to the workspace.
pub(super) fn checkout_of(workspace: &Path, id: &str) -> PathBuf {
    workspace.join(ATTEMPTS_DIR).join(id)
}

/// Starts several candidates at once, each on its own branch.
#[derive(Debug)]
pub(super) struct SpawnCandidates {
    workspace: PathBuf,
    manager: AsyncSubagentManager,
}

impl SpawnCandidates {
    /// Builds the tool this module contributes.
    pub(super) fn all(workspace: &Path, manager: &AsyncSubagentManager) -> Vec<Arc<dyn Tool<()>>> {
        vec![Arc::new(Self {
            workspace: workspace.to_path_buf(),
            manager: manager.clone(),
        })]
    }

    /// Launches every named approach, returning what started and what did not.
    async fn launch(&self, git: &Git, brief: &str, approaches: &[String]) -> (Vec<Value>, Vec<String>) {
        let ids = slots();
        let mut started = Vec::new();
        let mut failures = Vec::new();
        for (index, approach) in approaches.iter().enumerate() {
            let Some(id) = ids.get(index) else { break };
            let branch = match self.prepare(git, id).await {
                Ok(branch) => branch,
                Err(error) => {
                    failures.push(format!("{id}: {error}"));
                    continue;
                }
            };
            match self.manager.spawn(&role_for(id), candidate_brief(id, &branch, brief, approach)) {
                Ok(run_id) => started.push(json!({
                    "candidate": id,
                    "branch": branch,
                    "run_id": run_id,
                    "approach": approach,
                })),
                Err(error) => failures.push(format!("{id}: {error}")),
            }
        }
        (started, failures)
    }

    /// Prepares one slot: a branch, a checkout, and the brief its role gets.
    ///
    /// A slot whose checkout already exists is reused rather than refused. The
    /// alternative is a run that cannot start a second round until somebody
    /// abandons the first, which turns a bookkeeping detail into a stall.
    async fn prepare(&self, git: &Git, id: &str) -> Result<String> {
        let branch = format!("{ATTEMPT_PREFIX}{id}");
        let checkout = checkout_of(&self.workspace, id);
        if checkout.exists() {
            git.worktree_remove(&checkout).await?;
        }
        // A branch left behind by an earlier round would make `worktree add -b`
        // fail, so the slot has to be cleared — but *deleting* it is only safe
        // when there is nothing on it.
        //
        // An earlier version deleted it unconditionally, on the reasoning that
        // the round's ledger entry made the work reviewable. Nothing enforces
        // that entry: a live run reached three finished branches with the
        // attempts ledger still unrendered, because the planner timed out
        // before recording anything. So a second round would have destroyed
        // three candidates' work and left no record that they had existed.
        //
        // A branch carrying commits the trunk does not have is therefore moved
        // aside under its own head, not dropped. It costs one ref.
        if let Some(head) = git.head_of(&branch).await {
            if git.commits_ahead(TRUNK, &branch).await > 0 {
                git.rename_branch(&branch, &format!("{branch}-{head}")).await?;
            } else {
                git.delete_branch(&branch).await?;
            }
        }
        git.worktree_add(&checkout, &branch, TRUNK).await?;
        Ok(branch)
    }
}

#[async_trait]
impl Tool<()> for SpawnCandidates {
    fn name(&self) -> &'static str {
        "spawn_candidates"
    }

    fn description(&self) -> &'static str {
        "Starts several candidate solutions at once, each on its own git branch with its own \
         checkout of the workspace, and returns their run ids immediately. Use it when the run \
         has more than one plausible program and no argument for preferring one — five concurrent \
         candidates learn in one round what five serial attempts learn in five. Give each a \
         *different* approach: five spellings of the same idea cost five times as much and settle \
         nothing. Read the results with `attempt_diff`; the archivist keeps the one that won."
    }

    fn schema(&self) -> ToolSchema {
        ToolSchema::new(
            self.name(),
            self.description(),
            json!({
                "type": "object",
                "properties": {
                    "shared_brief": {
                        "type": "string",
                        "description": "What every candidate is being asked to do: the problem, \
                                        what counts as an answer, and what to verify against. \
                                        Sent to each one, so say it once here rather than in \
                                        every approach."
                    },
                    "approaches": {
                        "type": "array",
                        "items": { "type": "string" },
                        "minItems": 2,
                        "description": "One line per candidate, saying what makes that candidate \
                                        different — the method it should try. Between two and six."
                    }
                },
                "required": ["shared_brief", "approaches"],
                "additionalProperties": false
            }),
        )
    }

    async fn call(&self, _state: &(), call: ToolCall) -> Result<ToolResult> {
        self.schema().validate_call(&call)?;
        let brief = call
            .arguments
            .get("shared_brief")
            .and_then(Value::as_str)
            .unwrap_or_default()
            .trim()
            .to_string();
        let approaches: Vec<String> = call
            .arguments
            .get("approaches")
            .and_then(Value::as_array)
            .map(|items| {
                items
                    .iter()
                    .filter_map(Value::as_str)
                    .map(|line| line.trim().to_string())
                    .filter(|line| !line.is_empty())
                    .collect()
            })
            .unwrap_or_default();

        if brief.is_empty() {
            return Ok(ToolResult::error(
                &call.id,
                self.name(),
                "`shared_brief` must say what every candidate is being asked to do",
            ));
        }
        if approaches.len() < 2 {
            return Ok(ToolResult::error(
                &call.id,
                self.name(),
                "name at least two approaches; one candidate is an attempt, and the serial loop \
                 already does those better",
            ));
        }
        if approaches.len() > SLOTS {
            return Ok(ToolResult::error(
                &call.id,
                self.name(),
                format!("at most {SLOTS} candidates may run at once; {} were named", approaches.len()),
            ));
        }

        let git = Git::history(&self.workspace);
        if let Err(error) = git.initialise().await {
            return Ok(ToolResult::error(&call.id, self.name(), error.to_string()));
        }
        // A candidate branches from the trunk, so the trunk's current state has
        // to be committed first. Without this a candidate starts from whatever
        // the last checkpoint caught and silently loses the work in between.
        {
            let _guard = super::worklock::commits().await;
            if !git.stage_all().await.unwrap_or_default().trim().is_empty() {
                let _ = git.commit("branching candidates").await;
            }
        }

        let (started, failures) = self.launch(&git, &brief, &approaches).await;

        if started.is_empty() {
            return Ok(ToolResult::error(
                &call.id,
                self.name(),
                format!("no candidate started: {}", failures.join("; ")),
            ));
        }
        let mut out = format!(
            "started {} candidate(s):\n{}\n\nRecord each on the `attempts` ledger now, while you \
             know what you asked for.\n\nThen **do not sit in `await_agents` waiting for them**. \
             A candidate writes and runs programs, so it takes as long as the work takes, and a \
             live run lost its whole attempt this way: it awaited four candidates, timed out, and \
             never reached the archivist — so three finished branches were thrown away. Their \
             work is on their branches as they commit it, which is the point of the branches. \
             Spawn the archivist and let it read what is committed with `attempt_diff`, or come \
             back and check `list_attempts` between other work.",
            started.len(),
            serde_json::to_string_pretty(&Value::Array(started))
                .unwrap_or_else(|_| "[]".to_string())
        );
        if !failures.is_empty() {
            let _ = write!(out, "\n\nnot started: {}", failures.join("; "));
        }
        Ok(ToolResult::text(&call.id, self.name(), out))
    }
}

/// What one candidate is told when it starts.
///
/// Built here rather than in the prompt because it is the part that differs per
/// candidate, and a per-candidate system prompt would give each slot its own
/// provider-cache namespace. The shared brief goes in the spawn message for the
/// same reason the inventor's dossier does — see `dossier.rs`.
fn candidate_brief(id: &str, branch: &str, shared: &str, approach: &str) -> String {
    format!(
        "You are candidate {id}, working in your own checkout on branch `{branch}`. Every file \
         tool you hold is already rooted there, so write `code/solution.py` as usual — it is \
         yours alone and no other candidate can overwrite it.\n\n\
         **Use relative paths, and never an absolute `/workspace/...` one.** Your shell starts in \
         your checkout, at `/workspace/{ATTEMPTS_DIR}/{id}`, so `python3 code/brute.py` runs your \
         program. `/workspace/code/brute.py` is the *trunk's* copy: reading it gets you somebody \
         else's file and writing it overwrites work you were not given.\n\n\
         ## What everyone is doing\n\n{shared}\n\n\
         ## What makes you different\n\n{approach}\n\n\
         Follow your approach even if another looks more promising; the run is buying several \
         different answers, and a candidate that converges on its neighbour's method has cost a \
         slot and returned nothing. Verify against the oracle before you report. Finish by saying \
         what you did, what it produced, and what you checked it against — that summary is what \
         decides whether your work is kept."
    )
}

#[cfg(test)]
#[path = "candidates_test.rs"]
mod test;
