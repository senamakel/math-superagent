//! The kernel check, and the record it leaves behind.
//!
//! Lean 4 and a pre-built Mathlib are the largest thing in the runtime image,
//! and until this file existed no line of Rust ran either. `lean_prover` was
//! given `execute_command` and a prompt telling it to report `#print axioms`
//! and every remaining `sorry` — which is the arrangement this repository
//! names as its recurring failure. A prompt instruction is not a control, and
//! a formalisation is the one place where that costs the most: everything else
//! the runtime produces is a *reason to believe* something, and a proof the
//! kernel accepted is the thing itself. Held to a prompt, the two are
//! indistinguishable on disk. `research/CLAIMS.md` could not tell a lemma
//! Lean had checked from a sentence a model had typed, so it did not try, and
//! the strongest artifact the runtime can make was ledgered as prose.
//!
//! So the check is a tool with a parsed result, and the result is written where
//! the claim ledger can find it. What that buys is narrow and worth stating
//! exactly: it does not make a formalisation correct — a Lean proof of the
//! wrong statement is still the wrong statement, which is why the verdict
//! records the axioms rather than only the exit code — but it makes the
//! *claim* of one checkable by something other than the role that made it.

use std::fmt::Write as _;
use std::path::{Path, PathBuf};
use std::time::Duration;

use async_trait::async_trait;
use serde_json::json;

use super::{paths, string_argument};
use crate::agent::{Result, Tool, ToolCall, ToolResult, ToolSchema};

/// The one role this tool is granted to.
///
/// A constant rather than two string literals, because the registry names the
/// role and the harness assembly grants the tool, and those two agreeing is
/// the whole of the boundary. A rename that moved one and not the other would
/// silently leave the kernel check ungranted, and the failure would look like
/// a model declining to formalise.
pub(super) const LEAN_ROLE: &str = "lean_prover";

/// Where a verdict is filed, one JSON file per checked source.
///
/// Under `code/out/` rather than in a hidden `config/.*.json`, because a
/// reader would open it: it is the evidence behind the strongest row the claim
/// ledger can carry, and this repository commits what a reader would open. It
/// sits in the folder the ledger already walks for `claim` blocks, so a
/// formalisation and the note describing it end up in the same place.
pub(super) const VERDICT_DIR: &str = "code/out/lean";

/// How much of `lean`'s output is kept.
///
/// Smaller than the shell tool's ceiling on purpose. Lean reports errors and
/// finishes; a run of it that prints megabytes is one whose file is wrong in a
/// way the first few errors already show, and the verdict this tool exists to
/// produce is decided by the presence of an error rather than by its hundredth
/// repetition.
const MAX_LEAN_OUTPUT_BYTES: usize = 32 * 1024;

/// The axioms a proof may rest on and still be a proof.
///
/// Lean's own three, and nothing else. Mathlib is built on exactly these, so a
/// theorem that needs a fourth is not a theorem in the sense this runtime means
/// — it is a theorem *given* something the run assumed, and the assumption is
/// invisible in every other artifact the run produces.
///
/// This is the gap `lean4checker` exists to close, and closing it needs no
/// second binary. Replaying the kernel over the compiled `.olean` guards
/// against an environment that lied about what it checked; what actually
/// happens here is simpler and more likely, because it is one line a model can
/// write while doing exactly what it was asked. A file containing
///
/// ```text
/// axiom key_estimate : ∀ n, f n ≤ 2 * n
/// theorem main : ... := by ... key_estimate ...
/// ```
///
/// compiles cleanly, carries no `sorry`, prints its axioms as instructed, and
/// proves nothing at all. Every check this file had before would pass it, and
/// the claim ledger would carry it as `formalised` — the strongest row it has.
///
/// `Lean.ofReduceBool` and `Lean.ofReduceNat` are deliberately excluded even
/// though Lean emits them for legitimate uses of `native_decide`. That tactic
/// trusts the compiler and the machine rather than the kernel, and a runtime
/// whose whole argument for Lean is "the kernel checked it" cannot then accept
/// the one tactic that means it did not.
const TRUSTED_AXIOMS: [&str; 3] = ["propext", "Classical.choice", "Quot.sound"];

/// What Lean did with one file.
///
/// The three fields are separate because the three ways a formalisation lies
/// are separate. A file that does not compile proves nothing. A file that
/// compiles with `sorry` proves nothing and *looks* like it does. And a file
/// that compiles cleanly while resting on `sorryAx` — reachable through a
/// declaration proved elsewhere in the same file — proves nothing while
/// reporting no `sorry` at all, which is why the axioms are parsed rather than
/// trusted to the warning list.
#[derive(Clone, Debug, Default, PartialEq, Eq)]
pub(super) struct Verdict {
    /// The workspace-relative source this verdict is about.
    pub(super) file: String,
    /// Whether `lean` accepted the file.
    pub(super) compiled: bool,
    /// Every `declaration uses 'sorry'` warning, verbatim.
    pub(super) sorries: Vec<String>,
    /// Every `#print axioms` line, verbatim.
    pub(super) axioms: Vec<String>,
}

impl Verdict {
    /// Whether this verdict may stand behind a formalised claim.
    ///
    /// Four conditions, and the fourth is the one that reads as strict. It is
    /// not enough that no `sorry` was *reported*: the file must have asked. A
    /// source with no `#print axioms` line has told the runtime nothing about
    /// what its proof rests on, and `roles.md` already holds the role to
    /// printing them — this is that rule stated somewhere it can be enforced.
    /// The cost of the strictness is one line in a Lean file; the cost of
    /// relaxing it is a claim marked `formalised` whose proof nobody can see
    /// the foundations of.
    pub(super) fn verified(&self) -> bool {
        self.compiled
            && self.sorries.is_empty()
            && !self.axioms.is_empty()
            && !self.axioms.iter().any(|line| line.contains("sorryAx"))
            && self.untrusted_axioms().is_empty()
    }

    /// The axioms this proof rests on that are not Lean's own three.
    ///
    /// Returned rather than counted, because naming them is the whole value: a
    /// role told "an untrusted axiom" learns nothing, and one told
    /// "`key_estimate`" knows precisely which line to go and prove.
    ///
    /// `sorryAx` is not listed here even though it fails the same test. It has
    /// its own objection above, which says what a reader needs to hear — the
    /// proof is incomplete — where this list means something different and
    /// worse: the proof is complete, and rests on something nobody proved.
    pub(super) fn untrusted_axioms(&self) -> Vec<String> {
        let mut found: Vec<String> = Vec::new();
        for line in &self.axioms {
            // Everything after the colon is the bracketed list Lean prints.
            // Parsed rather than string-searched for each trusted name, because
            // the containment test answers the wrong question: a line listing
            // only `propext` and a line listing `propext` beside a bespoke
            // axiom both contain it.
            let Some((_, listed)) = line.split_once(':') else {
                continue;
            };
            for axiom in listed
                .trim()
                .trim_start_matches('[')
                .trim_end_matches(']')
                .split(',')
                .map(str::trim)
                .filter(|axiom| !axiom.is_empty())
            {
                if !TRUSTED_AXIOMS.contains(&axiom)
                    && axiom != "sorryAx"
                    && !found.iter().any(|seen| seen == axiom)
                {
                    found.push(axiom.to_string());
                }
            }
        }
        found
    }

    /// Why this verdict does not stand behind a claim, for a reader.
    ///
    /// Returns `None` when it does. The wording is what reaches
    /// `research/CLAIMS.md`, so it names the specific failure rather than
    /// saying the check did not pass: a role reading "no `#print axioms` line"
    /// knows what to write next, and one reading "not verified" does not.
    pub(super) fn objection(&self) -> Option<String> {
        if !self.compiled {
            return Some(format!("`{}` does not compile", self.file));
        }
        if !self.sorries.is_empty() {
            return Some(format!(
                "`{}` compiles with {} `sorry` still in it",
                self.file,
                self.sorries.len()
            ));
        }
        if self.axioms.is_empty() {
            return Some(format!(
                "`{}` has no `#print axioms` line, so what the proof rests on is unstated",
                self.file
            ));
        }
        if self.axioms.iter().any(|line| line.contains("sorryAx")) {
            return Some(format!("`{}` depends on `sorryAx`", self.file));
        }
        let untrusted = self.untrusted_axioms();
        if !untrusted.is_empty() {
            return Some(format!(
                "`{}` rests on {}, which nothing proved — a theorem given an assumed axiom is a \
                 conditional result, so state the assumption as its own claim and prove it, or \
                 file this one as `status: asserted`",
                self.file,
                untrusted
                    .iter()
                    .map(|axiom| format!("`{axiom}`"))
                    .collect::<Vec<_>>()
                    .join(", ")
            ));
        }
        None
    }

    /// Renders the verdict as the record on disk.
    fn record(&self) -> serde_json::Value {
        json!({
            "file": self.file,
            "compiled": self.compiled,
            "sorries": self.sorries,
            "axioms": self.axioms,
            "verified": self.verified(),
        })
    }

    /// Reads a verdict back out of one written record.
    fn from_record(value: &serde_json::Value) -> Option<Self> {
        Some(Self {
            file: value.get("file")?.as_str()?.to_string(),
            compiled: value.get("compiled")?.as_bool()?,
            sorries: strings(value.get("sorries")),
            axioms: strings(value.get("axioms")),
        })
    }

    /// Renders the verdict for the model that asked for it.
    fn render(&self) -> String {
        let mut out = format!(
            "file: {}\ncompiled: {}\nverified: {}\n",
            self.file,
            self.compiled,
            self.verified()
        );
        out.push_str(&list("sorry warnings", &self.sorries));
        out.push_str(&list("#print axioms", &self.axioms));
        match self.objection() {
            Some(objection) => {
                let _ = writeln!(
                    out,
                    "\nThis does not yet stand behind a `status: formalised` claim: {objection}."
                );
            }
            None => out.push_str(
                "\nThis verdict stands behind a `status: formalised` claim. Cite it with a \
                 `formalisation:` line naming this file.\n",
            ),
        }
        out
    }
}

/// Reads a `Vec<String>` out of a record field, tolerating its absence.
fn strings(value: Option<&serde_json::Value>) -> Vec<String> {
    value
        .and_then(serde_json::Value::as_array)
        .map(|items| {
            items
                .iter()
                .filter_map(|item| item.as_str().map(str::to_string))
                .collect()
        })
        .unwrap_or_default()
}

/// Renders one labelled list, saying so when it is empty.
fn list(label: &str, lines: &[String]) -> String {
    if lines.is_empty() {
        return format!("{label}: none\n");
    }
    let mut out = format!("{label}:\n");
    for line in lines {
        out.push_str("  ");
        out.push_str(line);
        out.push('\n');
    }
    out
}

/// The file a source's verdict is filed under.
///
/// The separator is folded rather than nested, so the folder stays one level
/// deep and a verdict is found by name without walking. `.lean` is kept in the
/// slug because `a/b.lean` and `a/b.md` are different files and a slug that
/// dropped the extension would let one claim the other's verdict.
fn slug(file: &str) -> String {
    file.replace(['/', '\\'], "_")
}

/// Returns the recorded verdict for one workspace-relative Lean source.
///
/// This is the reader the claim ledger uses, and it is deliberately a plain
/// function of the workspace rather than a handle held by anything: a verdict
/// outlives the attempt that produced it, and the ledger is re-derived long
/// after the `lean_prover` run has ended.
pub(super) fn verdict(workspace: &Path, file: &str) -> Option<Verdict> {
    let name = paths::strip_workspace_prefix(file);
    let path = workspace.join(VERDICT_DIR).join(format!("{}.json", slug(name)));
    let text = std::fs::read_to_string(path).ok()?;
    let value = serde_json::from_str::<serde_json::Value>(&text).ok()?;
    Verdict::from_record(&value)
}

/// Parses one `lean` invocation's output into a verdict.
///
/// Split from the process handling so the parse is testable without Lean
/// installed, which matters more here than it usually does: the deterministic
/// suite runs on a host that has no Mathlib, and a parser only exercised inside
/// the container is one nothing checks.
/// Both forms of each line are matched, and a live container is why. Lean 4
/// prints ``declaration uses `sorry` `` with backticks rather than the straight
/// quotes this parser first looked for, so every `sorry` warning was passing
/// through unrecorded — caught downstream only because the same proof also
/// prints `sorryAx`, which meant the verdict was right for the wrong reason and
/// the `sorries` list on disk was empty. And a proof that needs no axiom at all
/// prints `does not depend on any axioms`, with no `axioms:` in it: the
/// strictest possible result was being read as *no `#print axioms` line*, so
/// the one kind of proof this whole file exists to reward was the one kind it
/// refused.
fn parse(file: &str, exit_ok: bool, output: &str) -> Verdict {
    let mut sorries = Vec::new();
    let mut axioms = Vec::new();
    let mut errored = false;
    for line in output.lines() {
        let trimmed = line.trim();
        if trimmed.contains("declaration uses") && trimmed.contains("sorry") {
            sorries.push(trimmed.to_string());
        } else if trimmed.contains("depends on axioms:")
            || trimmed.contains("does not depend on any axioms")
        {
            axioms.push(trimmed.to_string());
        } else if trimmed.contains("error:") {
            errored = true;
        }
    }
    Verdict {
        file: file.to_string(),
        // Both, and the conjunction is the point. A non-zero exit is the
        // ordinary signal, but `lean` reports some failures while exiting
        // cleanly, and treating exit status alone as the answer is how a file
        // with an error in it would be recorded as having compiled.
        compiled: exit_ok && !errored,
        sorries,
        axioms,
    }
}

/// Runs `lean` over one workspace file and records what the kernel said.
#[derive(Debug)]
pub(super) struct LeanCheck {
    workspace: PathBuf,
    timeout: Duration,
}

impl LeanCheck {
    pub(super) fn new(workspace: PathBuf, timeout: Duration) -> Self {
        Self { workspace, timeout }
    }

    /// Invokes `lean`, returning its exit success and what it printed.
    ///
    /// Unlike the shell tool beside it, this uses `output()` inside the
    /// timeout and accepts that a run meeting the ceiling returns nothing.
    /// That tool keeps partial output because a killed computation still says
    /// how far it got; a killed `lean` does not, because the thing being asked
    /// for is a kernel verdict and there is no partial one. A timeout is
    /// therefore reported as "did not compile", which is what it means here.
    async fn run(&self, file: &Path) -> Result<(bool, String)> {
        let mut command = tokio::process::Command::new("lean");
        let child = command
            .arg(file)
            .current_dir(&self.workspace)
            .kill_on_drop(true)
            .stdout(std::process::Stdio::piped())
            .stderr(std::process::Stdio::piped())
            .output();
        let Ok(finished) = tokio::time::timeout(self.timeout, child).await else {
            return Ok((
                false,
                format!(
                    "error: lean did not finish within {} seconds",
                    self.timeout.as_secs()
                ),
            ));
        };
        let output = finished.map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!("failed to run lean: {error}"))
        })?;
        let mut text = String::from_utf8_lossy(&output.stdout).into_owned();
        text.push_str(&String::from_utf8_lossy(&output.stderr));
        Ok((output.status.success(), clipped(&text)))
    }

    /// Writes the verdict where the claim ledger reads it.
    ///
    /// A failure to write is an error rather than a best-effort omission, which
    /// is the opposite of how the shell tool treats its log — and the asymmetry
    /// is deliberate. That log is a record of something that already happened;
    /// this file is what a later claim's standing is checked against, so a
    /// verdict the model believes was filed and was not is exactly the silent
    /// gap this whole change exists to close.
    ///
    /// # Errors
    ///
    /// Returns an error when the verdict directory or file cannot be written.
    async fn file_verdict(&self, verdict: &Verdict) -> Result<()> {
        let directory = self.workspace.join(VERDICT_DIR);
        tokio::fs::create_dir_all(&directory).await.map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!("failed to create {VERDICT_DIR}: {error}"))
        })?;
        let path = directory.join(format!("{}.json", slug(&verdict.file)));
        let body = serde_json::to_string_pretty(&verdict.record()).map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!("failed to render lean verdict: {error}"))
        })?;
        tokio::fs::write(&path, body + "\n")
            .await
            .map_err(|error| {
                tinyagents::TinyAgentsError::Tool(format!("failed to write lean verdict: {error}"))
            })
    }
}

/// Shortens Lean's output, keeping the beginning.
///
/// The head rather than the tail, which is the reverse of the shell tool's
/// choice and for the reverse reason. A program's conclusion is at the end; a
/// compiler's first error is the one that caused the rest, and the hundredth is
/// usually its echo.
fn clipped(text: &str) -> String {
    if text.len() <= MAX_LEAN_OUTPUT_BYTES {
        return text.to_string();
    }
    let cut = text
        .char_indices()
        .map(|(at, _)| at)
        .take_while(|at| *at <= MAX_LEAN_OUTPUT_BYTES)
        .last()
        .unwrap_or(0);
    format!("{}\n[later output dropped]\n", &text[..cut])
}

#[async_trait]
impl Tool<()> for LeanCheck {
    fn name(&self) -> &'static str {
        "lean_check"
    }

    fn description(&self) -> &'static str {
        "Runs the Lean kernel over one .lean file in /workspace and records what it checked: \
         whether it compiled, every remaining `sorry`, and every `#print axioms` line. A claim \
         may only be marked `status: formalised` when this verdict passed."
    }

    fn schema(&self) -> ToolSchema {
        ToolSchema::new(
            self.name(),
            self.description(),
            json!({
                "type": "object",
                "properties": {
                    "file": {
                        "type": "string",
                        "description": "Workspace-relative path of the .lean file to check, \
                                        such as `code/lemma.lean`. Include a `#print axioms` \
                                        line for every theorem the claim rests on; a proof \
                                        whose axioms are unstated does not pass."
                    }
                },
                "required": ["file"],
                "additionalProperties": false
            }),
        )
    }

    async fn call(&self, _state: &(), call: ToolCall) -> Result<ToolResult> {
        let requested = string_argument(&call, "file")?;
        let path = paths::checked_workspace_path(&self.workspace, &requested)?;
        if path.extension().is_none_or(|extension| extension != "lean") {
            return Err(tinyagents::TinyAgentsError::Validation(format!(
                "`{requested}` is not a .lean file, and lean_check reads Lean sources only"
            )));
        }
        if !path.is_file() {
            return Err(tinyagents::TinyAgentsError::Validation(format!(
                "`{requested}` does not exist in the workspace; write it before checking it"
            )));
        }
        let relative = paths::strip_workspace_prefix(&requested).to_string();
        let (exit_ok, output) = self.run(&path).await?;
        let verdict = parse(&relative, exit_ok, &output);
        self.file_verdict(&verdict).await?;
        Ok(ToolResult::text(
            call.id,
            self.name(),
            format!("{}\nlean output:\n{output}", verdict.render()),
        ))
    }
}

#[cfg(test)]
#[path = "lean_test.rs"]
mod test;
