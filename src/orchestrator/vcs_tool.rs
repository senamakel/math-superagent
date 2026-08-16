//! The five git tools, and the boundary between reading a candidate and
//! keeping one.
//!
//! [`super::vcs`] gives the runtime verbs over the workspace's repository. This
//! turns four of them into tools, and it splits them in the one place that
//! matters: **reading what a candidate did is granted widely, and changing the
//! trunk because of it is granted to one role.**
//!
//! That split is the reason the module exists rather than a convenience. Half a
//! dozen roles benefit from seeing that a candidate already tried the sieve and
//! it did not help — that is the same argument recall is granted broadly on.
//! Deciding that a candidate's `solution.py` becomes *the* `solution.py` is a
//! different kind of act: it is the only operation here that makes one line of
//! work authoritative, and a runtime where any role can perform it has no
//! answer to "who decided this was the answer".
//!
//! # There is no `git` tool
//!
//! Every operation below is a named verb with checked arguments. A tool taking
//! an arbitrary git command line would be [`super::exec`] by another name,
//! reachable by roles that were deliberately never given a shell — and no
//! amount of argument validation puts that back, because the argument *is* a
//! program. `git checkout` alone would let any holder overwrite the trunk with
//! any branch's contents, which is precisely the authority this module spends
//! its structure withholding.
//!
//! # Adoption is not a merge
//!
//! [`Kind::Adopt`] copies *named paths* out of a candidate's branch. A merge
//! would take everything the branch touched — the candidate's own notes, its
//! ledger writes, its account of why it was right — and a losing candidate's
//! self-assessment landing in the trunk is worse than useless, because the next
//! attempt reads it as the trunk's own record. See [`super::vcs::Git::adopt_paths`].

use std::fmt::Write as _;
use std::path::{Path, PathBuf};
use std::sync::Arc;

use async_trait::async_trait;
use serde_json::{Value, json};

use super::vcs::{ATTEMPT_PREFIX, ATTEMPTS_DIR, Git, TRUNK};
use crate::agent::{Result, Tool, ToolCall, ToolResult, ToolSchema};

/// How many commit subjects one `attempt_log` returns.
const LOG_LIMIT: usize = 20;

/// How many paths one adoption may name.
///
/// Generous, because a coherent change genuinely spans a program and the note
/// that describes it. Bounded so a malformed argument cannot ask git to check
/// out a thousand paths in one call.
const MAX_ADOPTED_PATHS: usize = 32;

/// What one instance of the tool does.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub(super) enum Kind {
    /// Every candidate branch, with its head and whether it is checked out.
    List,
    /// What one candidate changed, as a diff or a summary.
    Diff,
    /// One candidate's commit subjects.
    Log,
    /// Copy named paths from a candidate into the trunk.
    Adopt,
    /// Remove a candidate's checkout, keeping its branch and the reason.
    Abandon,
}

impl Kind {
    /// The tools any role may hold: they read and change nothing.
    pub(super) const READING: [Self; 3] = [Self::List, Self::Diff, Self::Log];

    /// The tools that change the trunk, held by the archivist alone.
    pub(super) const WRITING: [Self; 2] = [Self::Adopt, Self::Abandon];

    fn name(self) -> &'static str {
        match self {
            Self::List => "list_attempts",
            Self::Diff => "attempt_diff",
            Self::Log => "attempt_log",
            Self::Adopt => "adopt_attempt",
            Self::Abandon => "abandon_attempt",
        }
    }

    fn description(self) -> &'static str {
        match self {
            Self::List => {
                "Lists every candidate solution this run has branched, with its head commit and \
                 whether its checkout still exists. Start here: it is the cheapest way to find \
                 out what has already been tried, and re-proposing something a candidate already \
                 ruled out is the most expensive mistake available."
            }
            Self::Diff => {
                "Shows what one candidate changed, relative to where it left the trunk. Ask for \
                 `stat` first — it names the files and their sizes in a few lines — and only then \
                 read the full diff, optionally narrowed to one path. This is how to judge a \
                 candidate without reading its files: a diff is what it did, and the files are \
                 mostly what everyone else already did."
            }
            Self::Log => {
                "Shows one candidate's commit subjects, newest first. Read this to see how a \
                 candidate got where it did — whether it converged or thrashed — which the final \
                 diff alone does not say."
            }
            Self::Adopt => {
                "Takes the named files from a candidate into the trunk, and commits them. This is \
                 the decision that makes one candidate's work the run's work, so name the files \
                 deliberately: it copies exactly what you list and nothing else, never the \
                 candidate's own notes or its account of why it was right. Record the reason on \
                 the attempts ledger."
            }
            Self::Abandon => {
                "Removes a candidate's working checkout, with the reason it was not kept. The \
                 branch survives, so the work stays readable and the reason stays on the record — \
                 only the disk is reclaimed. Use it as soon as a candidate is decided, so the \
                 list stays about live work."
            }
        }
    }

    fn schema_properties(self) -> Value {
        let attempt = json!({
            "type": "string",
            "description": "The candidate's id, as `list_attempts` reports it."
        });
        match self {
            Self::List => json!({}),
            Self::Diff => json!({
                "attempt": attempt,
                "stat": {
                    "type": "boolean",
                    "description": "True for a per-file summary instead of the diff itself. Ask \
                                    for this first; a full diff of a candidate that rewrote a \
                                    pool file is mostly noise."
                },
                "path": {
                    "type": "string",
                    "description": "Narrow the diff to one workspace-relative path. Optional."
                }
            }),
            Self::Log => json!({ "attempt": attempt }),
            Self::Adopt => json!({
                "attempt": attempt,
                "paths": {
                    "type": "array",
                    "items": { "type": "string" },
                    "description": "The workspace-relative files to take, exactly. \
                                    `code/solution.py`, not `code/`."
                },
                "reason": {
                    "type": "string",
                    "description": "Why this candidate won, in a sentence. It becomes the commit \
                                    subject, which is the trunk's own record of the decision."
                }
            }),
            Self::Abandon => json!({
                "attempt": attempt,
                "reason": {
                    "type": "string",
                    "description": "Why it was not kept. 'Slower than 03 and no more accurate' is \
                                    worth recording; 'did not work' is not."
                }
            }),
        }
    }

    fn required(self) -> Vec<&'static str> {
        match self {
            Self::List => vec![],
            Self::Diff | Self::Log => vec!["attempt"],
            Self::Adopt => vec!["attempt", "paths", "reason"],
            Self::Abandon => vec!["attempt", "reason"],
        }
    }
}

/// One git operation, bound to a workspace.
#[derive(Debug)]
pub(super) struct VcsTool {
    workspace: PathBuf,
    kind: Kind,
}

impl VcsTool {
    /// The tools every role that reviews candidates may hold.
    pub(super) fn reading(workspace: &Path) -> Vec<Arc<dyn Tool<()>>> {
        Self::build(workspace, &Kind::READING)
    }

    /// Every tool, including the two that change the trunk.
    pub(super) fn all(workspace: &Path) -> Vec<Arc<dyn Tool<()>>> {
        Self::build(workspace, &Kind::READING)
            .into_iter()
            .chain(Self::build(workspace, &Kind::WRITING))
            .collect()
    }

    fn build(workspace: &Path, kinds: &[Kind]) -> Vec<Arc<dyn Tool<()>>> {
        kinds
            .iter()
            .map(|kind| {
                Arc::new(Self {
                    workspace: workspace.to_path_buf(),
                    kind: *kind,
                }) as Arc<dyn Tool<()>>
            })
            .collect()
    }

    fn git(&self) -> Git {
        Git::history(&self.workspace)
    }

    /// The branch one call names, refusing anything that is not a candidate id.
    ///
    /// This is a traversal boundary, not a tidiness one: the id is concatenated
    /// into a ref name and passed to git, so an unchecked value reaches
    /// `--upload-pack=` or `../../refs/heads/work` and stops being an id at
    /// all. Only the characters a branch name may carry survive.
    fn branch_of(arguments: &Value) -> Result<String> {
        let raw = arguments
            .get("attempt")
            .and_then(Value::as_str)
            .unwrap_or_default()
            .trim();
        let id: String = raw
            .strip_prefix(ATTEMPT_PREFIX)
            .unwrap_or(raw)
            .chars()
            .filter(|character| character.is_ascii_alphanumeric() || *character == '-')
            .collect();
        let id = id.trim_matches('-').to_string();
        if id.is_empty() || id.len() > 64 {
            return Err(tinyagents::TinyAgentsError::Validation(
                "attempt must be a candidate id made of letters, digits and hyphens".into(),
            ));
        }
        Ok(format!("{ATTEMPT_PREFIX}{id}"))
    }

    /// A workspace-relative path a call may name.
    ///
    /// Absolute paths and traversal are refused rather than normalised. The
    /// same rule the file tools apply, for the same reason: a path that leaves
    /// the workspace is not a mistake this runtime corrects on the caller's
    /// behalf.
    fn relative(raw: &str) -> Result<String> {
        let path = Path::new(raw.trim());
        if raw.trim().is_empty()
            || path.is_absolute()
            || path
                .components()
                .any(|part| !matches!(part, std::path::Component::Normal(_)))
        {
            return Err(tinyagents::TinyAgentsError::Validation(format!(
                "`{raw}` must be a path inside the workspace, with no `..` and no leading `/`"
            )));
        }
        Ok(path.to_string_lossy().into_owned())
    }

    async fn list(&self) -> Result<String> {
        let git = self.git();
        if !git.exists() {
            return Ok("No candidates yet: this run has not branched one.".to_string());
        }
        let branches = git.attempt_branches().await?;
        if branches.is_empty() {
            return Ok(
                "No candidates yet. `spawn_candidates` starts several on their own branches."
                    .to_string(),
            );
        }
        let checked_out = git.worktrees().await.unwrap_or_default();
        let mut out = format!("{} candidate(s):\n", branches.len());
        for branch in &branches {
            let id = branch.strip_prefix(ATTEMPT_PREFIX).unwrap_or(branch);
            let head = git.head_of(branch).await.unwrap_or_else(|| "—".to_string());
            let subject = git
                .subject_of(branch)
                .await
                .unwrap_or_else(|| "(nothing committed)".to_string());
            let live = checked_out.iter().any(|(_, found)| found == branch);
            let state = if live { "live" } else { "closed" };
            let _ = writeln!(out, "- {id} [{state}] {head} {subject}");
        }
        out.push_str(
            "\nRead one with `attempt_diff {\"attempt\": \"<id>\", \"stat\": true}` before the \
             full diff.\n",
        );
        Ok(out)
    }

    async fn diff(&self, arguments: &Value) -> Result<String> {
        let branch = Self::branch_of(arguments)?;
        let git = self.git();
        if arguments
            .get("stat")
            .and_then(Value::as_bool)
            .unwrap_or(false)
        {
            let stat = git.diff_stat(TRUNK, &branch).await?;
            return Ok(if stat.trim().is_empty() {
                format!("`{branch}` has changed nothing against `{TRUNK}`.")
            } else {
                stat
            });
        }
        let path = match arguments.get("path").and_then(Value::as_str) {
            Some(raw) => Some(Self::relative(raw)?),
            None => None,
        };
        let diff = git.diff(TRUNK, &branch, path.as_deref()).await?;
        Ok(if diff.trim().is_empty() {
            format!("`{branch}` has changed nothing against `{TRUNK}`.")
        } else {
            diff
        })
    }

    async fn log(&self, arguments: &Value) -> Result<String> {
        let branch = Self::branch_of(arguments)?;
        let log = self.git().log(&branch, LOG_LIMIT).await?;
        Ok(if log.trim().is_empty() {
            format!("`{branch}` has no commits.")
        } else {
            log
        })
    }

    async fn adopt(&self, arguments: &Value) -> Result<String> {
        let branch = Self::branch_of(arguments)?;
        let reason = arguments
            .get("reason")
            .and_then(Value::as_str)
            .unwrap_or_default()
            .trim()
            .to_string();
        if reason.is_empty() {
            return Err(tinyagents::TinyAgentsError::Validation(
                "adopting a candidate needs the reason it won; it becomes the trunk's own record \
                 of the decision"
                    .into(),
            ));
        }
        let requested: Vec<&str> = arguments
            .get("paths")
            .and_then(Value::as_array)
            .map(|items| items.iter().filter_map(Value::as_str).collect())
            .unwrap_or_default();
        if requested.is_empty() {
            return Err(tinyagents::TinyAgentsError::Validation(
                "adopting a candidate needs the paths to take; it is a decision about named \
                 files, not a merge"
                    .into(),
            ));
        }
        if requested.len() > MAX_ADOPTED_PATHS {
            return Err(tinyagents::TinyAgentsError::Validation(format!(
                "{MAX_ADOPTED_PATHS} paths at most in one adoption; {} were named",
                requested.len()
            )));
        }
        let paths: Vec<String> = requested
            .iter()
            .map(|raw| Self::relative(raw))
            .collect::<Result<Vec<_>>>()?;

        let git = self.git();
        // A path the branch never had cannot be adopted, and git's own message
        // for that is `pathspec '...' did not match any file(s) known to git`,
        // which does not say *which* branch or suggest what to do. Refusing
        // here, before anything is touched, keeps adoption atomic: a single bad
        // path in a list of five must not leave the other four checked out.
        let present = git.files_on(&branch).await.unwrap_or_default();
        let missing: Vec<&str> = paths
            .iter()
            .filter(|path| !present.contains(path))
            .map(String::as_str)
            .collect();
        if !missing.is_empty() {
            return Err(tinyagents::TinyAgentsError::Validation(format!(
                "`{branch}` has no {}. Check `attempt_diff {{\"attempt\": \"{}\", \"stat\": \
                 true}}` for the paths it actually changed.",
                missing.join(", "),
                branch.strip_prefix(ATTEMPT_PREFIX).unwrap_or(&branch)
            )));
        }
        // Say which of the named paths the candidate did not actually change,
        // rather than silently adopting a copy of what the trunk already had.
        // A role that mistyped a path otherwise reads "adopted" and believes a
        // change landed that did not.
        let changed = git.changed_files(TRUNK, &branch).await.unwrap_or_default();
        let untouched: Vec<&String> = paths
            .iter()
            .filter(|path| !changed.contains(path))
            .collect();

        // One lock across the checkout *and* the commit: both touch the trunk's
        // index, and a checkpoint landing between them would commit a
        // half-adopted tree under someone else's subject.
        let _guard = super::worklock::commits().await;
        git.adopt_paths(&branch, &paths).await?;
        // Staged and committed by *pathspec*, never `add --all`. The run writes
        // the trunk continuously around this call — derived ledgers, research
        // notes, its own queues — and a whole-tree commit files all of it under
        // "adopt 01: <reason>". See `Git::commit_paths`.
        let staged = git.staged_among(&paths).await?;
        if staged.trim().is_empty() {
            return Ok(format!(
                "`{branch}` changed nothing in {}; the trunk already had those bytes.",
                paths.join(", ")
            ));
        }
        let id = branch.strip_prefix(ATTEMPT_PREFIX).unwrap_or(&branch);
        let commit = git
            .commit_paths(&format!("adopt {id}: {reason}"), &paths)
            .await?;

        let mut out = format!(
            "adopted {} from `{branch}` into `{TRUNK}` as {commit}: {}\n",
            paths.join(", "),
            reason
        );
        if !untouched.is_empty() {
            let _ = writeln!(
                out,
                "note: {} was not changed by this candidate, so adopting it copied what was \
                 already there.",
                untouched
                    .iter()
                    .map(|path| path.as_str())
                    .collect::<Vec<_>>()
                    .join(", ")
            );
        }
        out.push_str("Record the decision on the `attempts` ledger with `record_entry`.\n");
        Ok(out)
    }

    async fn abandon(&self, arguments: &Value) -> Result<String> {
        let branch = Self::branch_of(arguments)?;
        let reason = arguments
            .get("reason")
            .and_then(Value::as_str)
            .unwrap_or_default()
            .trim()
            .to_string();
        if reason.is_empty() {
            return Err(tinyagents::TinyAgentsError::Validation(
                "abandoning a candidate needs the reason, or the run pays to rediscover it".into(),
            ));
        }
        let id = branch.strip_prefix(ATTEMPT_PREFIX).unwrap_or(&branch);
        let checkout = self.workspace.join(ATTEMPTS_DIR).join(id);

        let _guard = super::worklock::commits().await;
        let git = self.git();
        // A checkout that is already gone is not an error: a candidate whose
        // directory was removed some other way still needs its branch recorded
        // as closed, and failing here would leave the caller unable to say so.
        if checkout.exists() {
            git.worktree_remove(&checkout).await?;
        } else {
            git.worktree_prune().await?;
        }
        Ok(format!(
            "closed `{branch}`: {reason}\nIts branch is kept, so `attempt_diff` and `attempt_log` \
             still read it. Record the outcome on the `attempts` ledger."
        ))
    }
}

#[async_trait]
impl Tool<()> for VcsTool {
    fn name(&self) -> &'static str {
        self.kind.name()
    }

    fn description(&self) -> &'static str {
        self.kind.description()
    }

    fn schema(&self) -> ToolSchema {
        ToolSchema::new(
            self.name(),
            self.description(),
            json!({
                "type": "object",
                "properties": self.kind.schema_properties(),
                "required": self.kind.required(),
                "additionalProperties": false
            }),
        )
    }

    async fn call(&self, _state: &(), call: ToolCall) -> Result<ToolResult> {
        self.schema().validate_call(&call)?;
        let outcome = match self.kind {
            Kind::List => self.list().await,
            Kind::Diff => self.diff(&call.arguments).await,
            Kind::Log => self.log(&call.arguments).await,
            Kind::Adopt => self.adopt(&call.arguments).await,
            Kind::Abandon => self.abandon(&call.arguments).await,
        };
        match outcome {
            Ok(text) => Ok(ToolResult::text(&call.id, self.name(), text)),
            // A git failure is reported to the caller rather than raised: the
            // model can act on "that branch does not exist" and cannot act on a
            // failed turn.
            Err(error) => Ok(ToolResult::error(&call.id, self.name(), error.to_string())),
        }
    }
}

#[cfg(test)]
#[path = "vcs_tool_test.rs"]
mod test;
