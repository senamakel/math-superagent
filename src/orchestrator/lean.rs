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

/// The namespace an axiom must sit in to be read as *cited* rather than *assumed*.
///
/// A library written in Lean has to be able to say "this theorem is in the
/// literature and is not proved here". Written as a bare `axiom` that is
/// indistinguishable from an assumption somebody slipped in, which is the
/// failure [`TRUSTED_AXIOMS`] exists to catch — so the two are separated by
/// where the axiom lives rather than by what it is called. `Cited.mihailescu`
/// is a citation; `key_estimate` is a hole.
///
/// The namespace buys no trust. A proof resting on one is [`Outcome::Conditional`]
/// and never [`Outcome::Verified`]: the kernel checked the implication and
/// nothing checked the hypothesis. What it buys is that the implication can be
/// *recorded* — before this, compressing a paper into Lean produced a file the
/// verdict could only fail, so the honest thing and the unrecordable thing were
/// the same thing.
const CITED_NAMESPACE: &str = "Cited.";

/// What a verdict amounts to, once the axioms have been read.
///
/// Three outcomes rather than a boolean, because the middle one is a real
/// state that the boolean had to round to failure. A file that compiles with no
/// `sorry` while resting on `Cited.faltings` is not a proof of its theorem and
/// is not nothing either — it is a proof of its theorem *given* the literature,
/// which is what most of a research library actually consists of.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub enum Outcome {
    /// The kernel checked it, resting on nothing but Lean's own three axioms.
    Verified,
    /// The kernel checked it, resting additionally on cited results under the
    /// `Cited` namespace that nothing here proved.
    Conditional,
    /// It does not stand: it failed to compile, carries a `sorry`, states no
    /// axioms, or rests on an axiom nobody proved and nobody attributed.
    Failed,
}

impl Outcome {
    /// The word this outcome is written as, in a record and in a ledger row.
    #[must_use]
    pub fn as_str(self) -> &'static str {
        match self {
            Self::Verified => "verified",
            Self::Conditional => "conditional",
            Self::Failed => "failed",
        }
    }
}

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
pub struct Verdict {
    /// The workspace-relative source this verdict is about.
    pub(super) file: String,
    /// Whether `lean` accepted the file.
    pub(super) compiled: bool,
    /// Every `declaration uses 'sorry'` warning, verbatim.
    pub(super) sorries: Vec<String>,
    /// Every `#print axioms` line, verbatim.
    pub(super) axioms: Vec<String>,
    /// Declarations whose statement is `X = X`.
    ///
    /// The one wrong statement a kernel check cannot object to on its own, and
    /// the one a Lean-first mandate invites — see [`super::lemmas::tautologies`]
    /// for the live instance that put this here.
    pub(super) tautologies: Vec<String>,
    /// Modules the file imported that this Mathlib does not have.
    ///
    /// Parsed rather than left inside the error text, because it is the one
    /// compile failure whose fix is mechanical and whose message is opaque.
    /// Lean reports it as a missing `.olean` *object file*, which reads like a
    /// broken toolchain and is nothing of the kind: the import names a module
    /// that does not exist. Two of the seven failures in the first bench run
    /// were this, and both files were otherwise correct.
    pub(super) missing_modules: Vec<String>,
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
        self.outcome() == Outcome::Verified
    }

    /// What this verdict amounts to.
    ///
    /// The four structural conditions are shared by both passing outcomes and
    /// checked first; the axioms then decide which one it is. Keeping the order
    /// this way is what stops a `Cited.` axiom from rescuing a file that has a
    /// `sorry` in it — a citation says where a *hypothesis* came from, and says
    /// nothing at all about a hole in the proof.
    pub(super) fn outcome(&self) -> Outcome {
        let structurally_sound = self.compiled
            && self.tautologies.is_empty()
            && self.sorries.is_empty()
            && !self.axioms.is_empty()
            && !self.axioms.iter().any(|line| line.contains("sorryAx"));
        if !structurally_sound || !self.unproved_axioms().is_empty() {
            return Outcome::Failed;
        }
        if self.cited_axioms().is_empty() {
            Outcome::Verified
        } else {
            Outcome::Conditional
        }
    }

    /// The axioms this proof rests on that are neither Lean's own three nor
    /// attributed to the literature.
    ///
    /// Returned rather than counted, because naming them is the whole value: a
    /// role told "an untrusted axiom" learns nothing, and one told
    /// "`key_estimate`" knows precisely which line to go and prove.
    ///
    /// `sorryAx` is not listed here even though it fails the same test. It has
    /// its own objection above, which says what a reader needs to hear — the
    /// proof is incomplete — where this list means something different and
    /// worse: the proof is complete, and rests on something nobody proved.
    pub(super) fn unproved_axioms(&self) -> Vec<String> {
        self.extra_axioms()
            .into_iter()
            .filter(|axiom| !axiom.starts_with(CITED_NAMESPACE))
            .collect()
    }

    /// The axioms this proof rests on that are attributed to the literature.
    ///
    /// Listed rather than merely counted for the same reason as the unproved
    /// ones, and read by a different audience: these are the hypotheses a
    /// reader has to go and check against the papers, so a verdict that hid
    /// them would be claiming more than it checked.
    pub(super) fn cited_axioms(&self) -> Vec<String> {
        self.extra_axioms()
            .into_iter()
            .filter(|axiom| axiom.starts_with(CITED_NAMESPACE))
            .collect()
    }

    /// Every axiom named in the `#print axioms` lines that is not one of
    /// Lean's own three, in first-seen order and deduplicated.
    fn extra_axioms(&self) -> Vec<String> {
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
            if !self.missing_modules.is_empty() {
                return Some(format!(
                    "`{}` imports {}, which this Mathlib does not have — the error names a \
                     missing `.olean`, but the toolchain is fine and the import is wrong. Find \
                     the real module with `ls /opt/mathlib4/Mathlib/<Area>` or \
                     `grep -rl \"theorem <name>\" /opt/mathlib4/Mathlib` before guessing again",
                    self.file,
                    names(&self.missing_modules)
                ));
            }
            return Some(format!("`{}` does not compile", self.file));
        }
        if !self.sorries.is_empty() {
            return Some(format!(
                "`{}` compiles with {} `sorry` still in it",
                self.file,
                self.sorries.len()
            ));
        }
        if !self.tautologies.is_empty() {
            return Some(format!(
                "`{}` states {}, whose two sides are identical — a theorem of the form `X = X` \
                 compiles, needs no axiom and proves nothing, so it cannot carry a claim. State \
                 what the value *is a consequence of*, not that it equals itself",
                self.file,
                names(&self.tautologies)
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
        let unproved = self.unproved_axioms();
        if !unproved.is_empty() {
            return Some(format!(
                "`{}` rests on {}, which nothing proved and nothing attributed — a theorem given \
                 an assumed axiom is a conditional result, so prove the assumption, or move it \
                 under `namespace {}` with the source it came from and file this claim as \
                 `status: conditional`",
                self.file,
                names(&unproved),
                CITED_NAMESPACE.trim_end_matches('.')
            ));
        }
        let cited = self.cited_axioms();
        if !cited.is_empty() {
            return Some(format!(
                "`{}` is proved only given {}, cited from the literature and not checked here — \
                 which is a real result and is `status: conditional`, not `status: formalised`",
                self.file,
                names(&cited)
            ));
        }
        None
    }

    /// Renders the verdict as the record on disk.
    ///
    /// `verified` is kept alongside `outcome` rather than replaced by it. The
    /// verdicts already on disk carry the boolean, [`Verdict::from_record`]
    /// does not read either field back, and a reader — or a script — that
    /// learned the old shape should not silently start seeing nothing where it
    /// used to see `false`.
    fn record(&self) -> serde_json::Value {
        json!({
            "file": self.file,
            "compiled": self.compiled,
            "sorries": self.sorries,
            "axioms": self.axioms,
            "missing_modules": self.missing_modules,
            "tautologies": self.tautologies,
            "cited": self.cited_axioms(),
            "verified": self.verified(),
            "outcome": self.outcome().as_str(),
        })
    }

    /// Reads a verdict back out of one written record.
    fn from_record(value: &serde_json::Value) -> Option<Self> {
        Some(Self {
            file: value.get("file")?.as_str()?.to_string(),
            compiled: value.get("compiled")?.as_bool()?,
            sorries: strings(value.get("sorries")),
            axioms: strings(value.get("axioms")),
            missing_modules: strings(value.get("missing_modules")),
            tautologies: strings(value.get("tautologies")),
        })
    }

    /// Renders the verdict for the model that asked for it.
    fn render(&self) -> String {
        let mut out = format!(
            "file: {}\ncompiled: {}\noutcome: {}\n",
            self.file,
            self.compiled,
            self.outcome().as_str()
        );
        out.push_str(&list("sorry warnings", &self.sorries));
        out.push_str(&list("#print axioms", &self.axioms));
        out.push_str(&list("cited axioms", &self.cited_axioms()));
        match (self.outcome(), self.objection()) {
            (Outcome::Conditional, _) => out.push_str(
                "\nThis verdict stands behind a `status: conditional` claim, and not a \
                 `formalised` one: the kernel checked the implication, and the cited axioms above \
                 are hypotheses nothing here proved. Cite it with a `formalisation:` line naming \
                 this file, and give each cited axiom its own claim carrying the source.\n",
            ),
            (_, Some(objection)) => {
                let _ = writeln!(
                    out,
                    "\nThis does not yet stand behind a `status: formalised` claim: {objection}."
                );
            }
            (_, None) => out.push_str(
                "\nThis verdict stands behind a `status: formalised` claim. Cite it with a \
                 `formalisation:` line naming this file.\n",
            ),
        }
        out
    }
}

/// Renders a list of axiom names as backticked prose.
fn names(axioms: &[String]) -> String {
    axioms
        .iter()
        .map(|axiom| format!("`{axiom}`"))
        .collect::<Vec<_>>()
        .join(", ")
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

/// Every verdict filed for this workspace, weakest news first.
///
/// Read off disk rather than taken from the prover's reply, which is the
/// argument `refute.rs` already makes about its own verdicts: a role's prose is
/// a summary of its own work and the record is the work. It matters more here,
/// because the ordinary way a formalisation turn ends is the run cap killing it
/// — which destroys the report and leaves every `.lean` file and every verdict
/// beside it.
///
/// Ordered so a reader skimming one line sees the check that did *not* pass.
/// A verified proof needs no action; a file that compiles with three `sorry`
/// still in it is the one somebody has to go back to.
pub(super) fn collect(workspace: &Path) -> Vec<Verdict> {
    let Ok(entries) = std::fs::read_dir(workspace.join(VERDICT_DIR)) else {
        return Vec::new();
    };
    let mut paths: Vec<PathBuf> = entries.flatten().map(|entry| entry.path()).collect();
    paths.sort();
    let mut verdicts: Vec<Verdict> = paths
        .iter()
        .filter_map(|path| {
            let text = std::fs::read_to_string(path).ok()?;
            let value = serde_json::from_str::<serde_json::Value>(&text).ok()?;
            Verdict::from_record(&value)
        })
        .collect();
    verdicts.sort_by_key(Verdict::verified);
    verdicts
}

/// One line per filed verdict, for a reader who is not the prover.
///
/// The objection is carried rather than a bare pass/fail, because the two say
/// different things to whoever reads this next: "does not compile" is work for
/// the same role again, and "rests on `key_estimate`, which nothing proved" is
/// a new statement somebody has to go and prove.
pub(super) fn briefing(workspace: &Path) -> String {
    let mut out = String::new();
    for verdict in collect(workspace) {
        match verdict.objection() {
            Some(objection) => {
                let _ = writeln!(out, "- {objection}");
            }
            None => {
                let _ = writeln!(
                    out,
                    "- `{}` — the kernel checked it, on Lean's three axioms alone",
                    verdict.file
                );
            }
        }
    }
    out
}

/// How many formalisations passed, out of how many were attempted.
///
/// Counted for the judge, which reads what is on disk rather than what an
/// attempt reported. A failed check is deliberately in the denominator: a run
/// that tried to formalise four lemmas and closed one has done something the
/// count of claims cannot show, and a statistic that hid the three would make
/// the honest run and the run that never tried look identical.
pub(super) fn counts(workspace: &Path) -> (usize, usize) {
    let verdicts = collect(workspace);
    let passed = verdicts.iter().filter(|verdict| verdict.verified()).count();
    (passed, verdicts.len())
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
    let mut missing_modules = Vec::new();
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
            // `object file '…/Mathlib/Data/Nat/Parity.olean' of module
            // Mathlib.Data.Nat.Parity does not exist`
            if trimmed.contains("does not exist")
                && let Some((_, after)) = trimmed.split_once("of module ")
                && let Some(module) = after.split_whitespace().next()
                && !missing_modules.iter().any(|seen| seen == module)
            {
                missing_modules.push(module.to_string());
            }
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
        tautologies: Vec::new(),
        missing_modules,
    }
}

/// Runs `lean` over one workspace file and records what the kernel said.
#[derive(Debug)]
pub(super) struct LeanCheck {
    workspace: PathBuf,
    timeout: Duration,
    /// The write path, held so a check can re-derive `derived/LEMMAS.md`.
    ///
    /// Optional because [`check_file`] runs this same kernel path from the host
    /// binary, where there is no run and nothing to re-derive. Held rather than
    /// looked up so the derivation goes through `write_runtime` — a derived
    /// ledger written any other way is one the write path would refuse.
    documents: Option<super::documents::WorkspaceDocuments>,
}

impl LeanCheck {
    pub(super) fn new(workspace: PathBuf, timeout: Duration) -> Self {
        Self {
            workspace,
            timeout,
            documents: None,
        }
    }

    /// Gives the check the write path, so it re-derives the lemma index.
    pub(super) fn deriving(mut self, documents: super::documents::WorkspaceDocuments) -> Self {
        self.documents = Some(documents);
        self
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

/// The `X = X` declarations in one source, or none when it cannot be read.
///
/// Unreadable is treated as none rather than as an error: the file has just
/// been compiled, so it plainly exists, and a verdict that failed because a
/// second read raced a writer would be worse than one that misses a tautology.
async fn read_tautologies(path: &Path) -> Vec<String> {
    match tokio::fs::read_to_string(path).await {
        Ok(source) => super::lemmas::tautologies(&source),
        Err(_) => Vec::new(),
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
        let mut verdict = parse(&relative, exit_ok, &output);
        // Read off the source rather than off Lean's output, because Lean has
        // no complaint to make: `X = X` is a theorem it proves gladly.
        verdict.tautologies = read_tautologies(&path).await;
        self.file_verdict(&verdict).await?;
        // After the verdict is on disk and not before: half of every row in the
        // lemma index is the standing this check just decided, so a derivation
        // run first would publish a table saying `unchecked` about the file the
        // kernel had accepted a line earlier.
        let derived = if let Some(documents) = &self.documents {
            super::lemmas::refresh(documents).await;
            format!("\nre-derived {}\n", super::lemmas::LEMMAS_PATH)
        } else {
            String::new()
        };
        Ok(ToolResult::text(
            call.id,
            self.name(),
            format!("{}{derived}\nlean output:\n{output}", verdict.render()),
        ))
    }
}

/// What a caller outside this crate may read off a verdict.
///
/// A separate block from the `pub(super)` methods above so the public surface
/// is a deliberate list rather than whatever happened to be reachable. It is
/// the read side only: a verdict is produced by [`check_file`] and by nothing
/// else, because the one way to obtain one has to be running the kernel.
impl Verdict {
    /// The workspace-relative source this verdict is about.
    #[must_use]
    pub fn file(&self) -> &str {
        &self.file
    }

    /// Whether `lean` accepted the file.
    #[must_use]
    pub fn compiled(&self) -> bool {
        self.compiled
    }

    /// What the verdict amounts to once the axioms have been read.
    #[must_use]
    pub fn verdict(&self) -> Outcome {
        self.outcome()
    }

    /// Every `declaration uses 'sorry'` warning, verbatim.
    #[must_use]
    pub fn sorry_warnings(&self) -> &[String] {
        &self.sorries
    }

    /// Every `#print axioms` line, verbatim.
    #[must_use]
    pub fn axiom_lines(&self) -> &[String] {
        &self.axioms
    }

    /// Why this verdict does not stand behind a `status: formalised` claim,
    /// or `None` when it does.
    #[must_use]
    pub fn reason(&self) -> Option<String> {
        self.objection()
    }

    /// The verdict as the JSON record `code/out/lean/` holds.
    ///
    /// The same rendering the tool files, so a check run from the host and a
    /// check run inside an attempt cannot disagree about what they found.
    #[must_use]
    pub fn to_json(&self) -> serde_json::Value {
        self.record()
    }

    /// The verdict as the prose the `lean_prover` role is shown.
    #[must_use]
    pub fn to_report(&self) -> String {
        self.render()
    }
}

/// Runs the Lean kernel over one workspace file and returns what it found.
///
/// The entry point for every caller that is not the tool: the host-side
/// `lean-check` wrapper and the replay that scores past runs both come through
/// here, so there is one implementation of *what counts as verified* and not a
/// second one written in shell. `file` is workspace-relative, exactly as the
/// tool's argument is.
///
/// `write_verdict` is off by default at every call site that is not an
/// attempt. A convenience check run from the host must not leave a record in
/// `code/out/lean/`, because that directory is the evidence `research/CLAIMS.md`
/// consults, and a claim's standing should rest on a check the run actually
/// performed rather than on one somebody ran afterwards from a terminal.
///
/// Returns the verdict and what `lean` printed, clipped to the same ceiling the
/// tool keeps. The raw output is returned rather than summarised because it is
/// the only thing a caller can act on: a verdict says a file did not compile,
/// and the error text says which goal is left after which tactic, which is what
/// the next edit is decided from. The tool hands the model both for that
/// reason, and a host caller iterating on a proof needs it more, not less.
///
/// # Errors
///
/// Returns an error when `file` escapes the workspace, is not a `.lean` file,
/// does not exist, when `lean` cannot be executed, or when `write_verdict` is
/// set and the verdict cannot be written.
pub async fn check_file(
    workspace: &Path,
    file: &str,
    timeout: Duration,
    write_verdict: bool,
) -> Result<(Verdict, String)> {
    let path = paths::checked_workspace_path(workspace, file)?;
    if path.extension().is_none_or(|extension| extension != "lean") {
        return Err(tinyagents::TinyAgentsError::Validation(format!(
            "`{file}` is not a .lean file, and the Lean check reads Lean sources only"
        )));
    }
    if !path.is_file() {
        return Err(tinyagents::TinyAgentsError::Validation(format!(
            "`{file}` does not exist in the workspace"
        )));
    }
    let checker = LeanCheck::new(workspace.to_path_buf(), timeout);
    let relative = paths::strip_workspace_prefix(file).to_string();
    let (exit_ok, output) = checker.run(&path).await?;
    let mut verdict = parse(&relative, exit_ok, &output);
    verdict.tautologies = read_tautologies(&path).await;
    if write_verdict {
        checker.file_verdict(&verdict).await?;
    }
    Ok((verdict, output))
}

#[cfg(test)]
#[path = "lean_test.rs"]
mod test;
