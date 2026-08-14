//! Looking for the counterexample, and recording what the model builder found.
//!
//! The runtime had four ways to prove something and none whose job was to
//! break it. `sat_solver`, `smt_solver`, `theorem_prover` and `lean_prover` are
//! all delegated *to* — a role asks them a question — and none of them is ever
//! scheduled *against* the statement the run is currently trying to prove. So a
//! false conjecture was attacked by proof for as long as the budget lasted.
//!
//! Tao's advice is the opposite way round — spend the first minutes hunting a
//! counterexample — and the Equational Theories Project measured what that is
//! worth at scale: 524 small finite magmas refuted 13.6 million of its 22
//! million implications, 13.3 million at order 3 alone, for 165 CPU-hours,
//! before any clever proof search ran. Refutation was not the consolation prize
//! for a failed proof. It was the cheap majority of the work.
//!
//! # Why this needs Vampire specifically
//!
//! `eprover` saturates toward a refutation of the *negated* conjecture, so on a
//! statement that is actually false it runs until its clock stops and reports
//! nothing usable. Vampire's `--saturation_algorithm fmb` searches for a finite
//! model of the axioms *plus the negated conjecture* instead — and such a model
//! is exactly a counterexample. It answers `SZS status CounterSatisfiable` and
//! prints the interpretation, which is a thing a person can read and check.
//!
//! # The verdict that matters most is neither of the two obvious ones
//!
//! One run distinguishes four outcomes, and `ContradictoryAxioms` is the one
//! worth having built this for. From contradictory hypotheses everything
//! follows, so a broken axiomatisation *proves the goal* — which is how a bad
//! encoding comes to look like a triumph. The SMT role is held to checking for
//! that in its prompt; here the engine reports it as a status of its own, so it
//! is a fact the runtime reads rather than a discipline it hopes for.
//!
//! A refutation is also the one result this runtime used to have no word for.
//! It is not the goal and never will be, so an attempt producing one reported
//! UNSOLVED — see the `BANKED` verdict, which exists so that settling something
//! short of the goal counts. A counterexample belongs in `research/CLAIMS.md`
//! as a claim this run established.

use std::fmt::Write as _;
use std::path::{Path, PathBuf};
use std::time::Duration;

use async_trait::async_trait;
use serde_json::json;

use super::{paths, string_argument};
use crate::agent::{Result, Tool, ToolCall, ToolResult, ToolSchema};

/// The engine. Present in the image; see the `Dockerfile` for why it is fetched
/// from the project's release rather than from apt.
const VAMPIRE: &str = "vampire";

/// Where a verdict is filed, one JSON file per refuted statement.
///
/// Beside the Lean verdicts and for the same reason: it is evidence a later
/// reader would open, and it outlives the attempt that produced it.
pub(super) const VERDICT_DIR: &str = "code/out/refute";

/// How long one search may take.
///
/// A minute rather than the shell tool's ten. Model building over small domains
/// either succeeds quickly or is not going to: the sizes that refute most
/// statements are the ones an exhaustive search reaches in seconds, and a
/// search that has run a minute is usually looking for a model that does not
/// exist. Cheap and often is the whole method.
const SEARCH_TIMEOUT: Duration = Duration::from_mins(1);

/// How much of the engine's output is kept.
///
/// A printed finite model is the useful part and it is small. What is large is
/// a proof object, which this tool never wants: the head is kept because the
/// status line and the model come first.
const MAX_OUTPUT: usize = 32 * 1024;

/// What the model builder established about one statement.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub(super) enum Finding {
    /// A finite model of the axioms and the negated conjecture — a
    /// counterexample, with the interpretation that witnesses it.
    Refuted,
    /// The conjecture follows from the axioms after all.
    Proved,
    /// The axioms contradict each other, so nothing they entail means anything.
    Contradictory,
    /// Neither settled inside the budget.
    Undecided,
}

impl Finding {
    /// Reads an SZS status word.
    ///
    /// Matched on the vocabulary rather than on Vampire's prose, because SZS is
    /// the standard every prover in this image speaks and the prose is not.
    fn from_status(status: &str) -> Option<Self> {
        match status {
            "CounterSatisfiable" | "Satisfiable" => Some(Self::Refuted),
            "Theorem" | "Unsatisfiable" => Some(Self::Proved),
            "ContradictoryAxioms" => Some(Self::Contradictory),
            "Timeout" | "GaveUp" | "Unknown" | "ResourceOut" | "InputError" => {
                Some(Self::Undecided)
            }
            _ => None,
        }
    }

    /// What the finding is called on disk and in a report.
    fn label(self) -> &'static str {
        match self {
            Self::Refuted => "refuted",
            Self::Proved => "proved",
            Self::Contradictory => "contradictory-axioms",
            Self::Undecided => "undecided",
        }
    }

    /// What the run should do about it, in one sentence.
    ///
    /// Carried here rather than left to the prompt because each of the four is
    /// a different instruction, and three of them are easy to misread. A
    /// refutation is a *result* and reads like a failure; a proof from this
    /// engine is real but rests on an axiomatisation nobody checked; and
    /// contradictory axioms look like the best possible news until you notice
    /// that everything follows from them.
    fn guidance(self) -> &'static str {
        match self {
            Self::Refuted => {
                "This is a result, not a failure. The model below is a counterexample: read it, \
                 check by hand that it really does satisfy the axioms and falsify the \
                 conjecture, and then write it into a note as a `claim` block with `status: \
                 checked`. A refutation nobody recorded is a discovery the next attempt will \
                 make again."
            }
            Self::Proved => {
                "The statement follows from the axioms *you wrote*, which is a weaker fact than \
                 it looks: the axiomatisation is the whole risk here. Say `proved from these \
                 axioms` and list them, never `proved`."
            }
            Self::Contradictory => {
                "The axioms contradict each other, so they entail everything and nothing they \
                 entail is evidence. This is a fault in the encoding, not a result about the \
                 mathematics. Find the two axioms that clash before running anything else."
            }
            Self::Undecided => {
                "No counterexample of the sizes reached, and no proof. That is weak evidence for \
                 the statement and nothing more — say so in exactly those terms. If the smallest \
                 counterexample is plausibly larger than the domains searched, say that too."
            }
        }
    }
}

/// One statement the engine was asked about.
#[derive(Clone, Debug)]
pub(super) struct Verdict {
    /// The workspace-relative TPTP problem this is about.
    pub(super) problem: String,
    /// What the engine established.
    pub(super) finding: Finding,
    /// The status word it printed, kept verbatim.
    pub(super) status: String,
    /// The finite model, when there is one.
    pub(super) model: String,
}

impl Verdict {
    /// Whether this verdict actually establishes a counterexample.
    pub(super) fn refuted(&self) -> bool {
        self.finding == Finding::Refuted
    }

    /// Renders the verdict as the record on disk.
    fn record(&self) -> serde_json::Value {
        json!({
            "problem": self.problem,
            "finding": self.finding.label(),
            "status": self.status,
            "model": self.model,
        })
    }

    /// Renders the verdict for the model that asked for it.
    fn render(&self) -> String {
        let mut out = format!(
            "problem: {}\nfinding: {}\nSZS status: {}\n\n{}\n",
            self.problem,
            self.finding.label(),
            self.status,
            self.finding.guidance()
        );
        if !self.model.is_empty() {
            let _ = write!(out, "\nThe counterexample:\n{}\n", self.model.trim_end());
        }
        out
    }
}

/// Reads the engine's output into a verdict.
///
/// The *last* recognised status wins, because a portfolio prints what each
/// strategy concluded before it reports the run's answer. An output carrying no
/// recognised status at all is `Undecided` rather than an error: the engine ran
/// and settled nothing, which is a fact about the statement worth recording,
/// where a tool error would end the refuter's turn on the most ordinary outcome
/// in the loop.
pub(super) fn parse(problem: &str, output: &str) -> Verdict {
    let mut finding = Finding::Undecided;
    let mut status = String::new();
    for line in output.lines() {
        let Some(rest) = line.trim().split_once("SZS status ") else {
            continue;
        };
        let word = rest.1.split_whitespace().next().unwrap_or_default();
        if let Some(read) = Finding::from_status(word) {
            finding = read;
            status = word.to_string();
        }
    }
    if status.is_empty() {
        status = "none reported".to_string();
    }
    Verdict {
        problem: problem.to_string(),
        finding,
        model: if finding == Finding::Refuted {
            extract_model(output)
        } else {
            String::new()
        },
        status,
    }
}

/// Pulls the printed interpretation out of the engine's output.
///
/// Bounded by its own markers rather than by a line count, and empty when the
/// markers are absent — a `CounterSatisfiable` with no model printed is still a
/// refutation, and inventing a model for it would be worse than saying nothing.
fn extract_model(output: &str) -> String {
    let mut model = String::new();
    let mut inside = false;
    for line in output.lines() {
        if line.contains("SZS output start FiniteModel") {
            inside = true;
            continue;
        }
        if line.contains("SZS output end FiniteModel") {
            break;
        }
        if inside {
            model.push_str(line);
            model.push('\n');
        }
    }
    model
}

/// Returns the recorded verdict for one workspace-relative TPTP problem.
pub(super) fn verdict(workspace: &Path, problem: &str) -> Option<Verdict> {
    let name = paths::strip_workspace_prefix(problem);
    let path = workspace
        .join(VERDICT_DIR)
        .join(format!("{}.json", slug(name)));
    read_record(&path)
}

/// Reads one filed record back into a verdict.
fn read_record(path: &Path) -> Option<Verdict> {
    let text = std::fs::read_to_string(path).ok()?;
    let value = serde_json::from_str::<serde_json::Value>(&text).ok()?;
    let read = |key: &str| {
        value
            .get(key)
            .and_then(serde_json::Value::as_str)
            .unwrap_or_default()
            .to_string()
    };
    let label = read("finding");
    Some(Verdict {
        problem: read("problem"),
        finding: match label.as_str() {
            "refuted" => Finding::Refuted,
            "proved" => Finding::Proved,
            "contradictory-axioms" => Finding::Contradictory,
            _ => Finding::Undecided,
        },
        status: read("status"),
        model: read("model"),
    })
}

/// Every verdict filed for this workspace, worst news first.
///
/// Read off disk rather than taken from the refuter's reply, which is the
/// argument the reduction arm already makes about its ledger: a role's prose is
/// a summary of its own work and the record is the work. It also means a turn
/// that ran the engine and then produced a truncated report still delivers what
/// the engine found.
///
/// Ordered by how much the run needs to hear it. A contradictory axiomatisation
/// comes first because it invalidates anything built on the same encoding, then
/// refutations, then everything else — a reader skimming one line should see
/// the finding that changes what happens next.
pub(super) fn collect(workspace: &Path) -> Vec<Verdict> {
    let Ok(entries) = std::fs::read_dir(workspace.join(VERDICT_DIR)) else {
        return Vec::new();
    };
    let mut paths: Vec<PathBuf> = entries.flatten().map(|entry| entry.path()).collect();
    paths.sort();
    let mut verdicts: Vec<Verdict> = paths.iter().filter_map(|path| read_record(path)).collect();
    verdicts.sort_by_key(|verdict| match verdict.finding {
        Finding::Contradictory => 0,
        Finding::Refuted => 1,
        Finding::Proved => 2,
        Finding::Undecided => 3,
    });
    verdicts
}

/// One line per filed verdict, for a reader who is not the refuter.
///
/// The model is omitted: it is often long, it is already on disk beside the
/// problem, and what a later reader needs from this is which statements are
/// settled and which way. The refuter's own report carries the counterexample.
pub(super) fn briefing(workspace: &Path) -> String {
    let mut out = String::new();
    for verdict in collect(workspace) {
        let _ = writeln!(
            out,
            "- `{}` — {} ({})",
            verdict.problem,
            verdict.finding.label(),
            verdict.status
        );
    }
    out
}

/// How many statements have been settled each way.
///
/// Counted for the judge, which reads what is on disk rather than what an
/// attempt reported — the ordinary way an attempt ends is the run cap killing
/// it, which destroys the report and leaves every file. A refutation is exactly
/// the kind of result that would otherwise be invisible: it is not the goal, so
/// an attempt producing one reports UNSOLVED.
pub(super) fn counts(workspace: &Path) -> (usize, usize) {
    let verdicts = collect(workspace);
    let refuted = verdicts
        .iter()
        .filter(|verdict| verdict.finding == Finding::Refuted)
        .count();
    (refuted, verdicts.len())
}

/// The file a problem's verdict is filed under.
fn slug(problem: &str) -> String {
    problem.replace(['/', '\\'], "_")
}

/// Searches for a finite model that breaks a stated conjecture.
#[derive(Debug)]
pub(super) struct FindCounterexample {
    workspace: PathBuf,
}

impl FindCounterexample {
    pub(super) fn new(workspace: PathBuf) -> Self {
        Self { workspace }
    }

    /// Runs the model builder over one TPTP problem.
    ///
    /// A timeout is `Undecided` rather than an error, for the reason the parse
    /// treats an unrecognised status that way: not settling is the ordinary
    /// outcome of asking a hard question cheaply, and it still tells the run
    /// that no small counterexample exists.
    async fn run(&self, problem: &Path) -> Result<String> {
        let mut command = tokio::process::Command::new(VAMPIRE);
        let run = command
            // The mode that looks for a model rather than for a refutation.
            // Without it this is `eprover` with a different name.
            .arg("--saturation_algorithm")
            .arg("fmb")
            .arg("--time_limit")
            .arg(SEARCH_TIMEOUT.as_secs().to_string())
            .arg(problem)
            .current_dir(&self.workspace)
            .kill_on_drop(true)
            .stdout(std::process::Stdio::piped())
            .stderr(std::process::Stdio::piped())
            .output();
        // Its own ceiling above the engine's, so a build where `--time_limit`
        // is not honoured cannot hold the tool open.
        let Ok(finished) = tokio::time::timeout(SEARCH_TIMEOUT * 2, run).await else {
            return Ok(String::new());
        };
        let output = finished.map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!("failed to run {VAMPIRE}: {error}"))
        })?;
        let mut text = String::from_utf8_lossy(&output.stdout).into_owned();
        text.push_str(&String::from_utf8_lossy(&output.stderr));
        text.truncate(
            text.char_indices()
                .map(|(at, _)| at)
                .take_while(|at| *at <= MAX_OUTPUT)
                .last()
                .unwrap_or(0),
        );
        Ok(text)
    }

    /// Files the verdict where a later reader finds it.
    ///
    /// # Errors
    ///
    /// Returns an error when the directory or the record cannot be written.
    async fn file(&self, verdict: &Verdict) -> Result<()> {
        let directory = self.workspace.join(VERDICT_DIR);
        tokio::fs::create_dir_all(&directory).await.map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!("failed to create {VERDICT_DIR}: {error}"))
        })?;
        let body = serde_json::to_string_pretty(&verdict.record()).map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!("failed to render the verdict: {error}"))
        })?;
        tokio::fs::write(
            directory.join(format!("{}.json", slug(&verdict.problem))),
            body + "\n",
        )
        .await
        .map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!("failed to write the verdict: {error}"))
        })
    }
}

#[async_trait]
impl Tool<()> for FindCounterexample {
    fn name(&self) -> &'static str {
        "find_counterexample"
    }

    fn description(&self) -> &'static str {
        "Searches for a finite model that satisfies a TPTP problem's axioms and falsifies its \
         conjecture — a counterexample. Also reports when the conjecture is provable instead, and \
         when the axioms contradict each other."
    }

    fn schema(&self) -> ToolSchema {
        ToolSchema::new(
            self.name(),
            self.description(),
            json!({
                "type": "object",
                "properties": {
                    "problem": {
                        "type": "string",
                        "description": "Workspace-relative path of the TPTP problem, such as \
                                        `code/refute/girth.p`. It holds the axioms as `fof(..., \
                                        axiom, ...)` and the statement being attacked as \
                                        `fof(..., conjecture, ...)`."
                    }
                },
                "required": ["problem"],
                "additionalProperties": false
            }),
        )
    }

    async fn call(&self, _state: &(), call: ToolCall) -> Result<ToolResult> {
        let requested = string_argument(&call, "problem")?;
        let path = paths::checked_workspace_path(&self.workspace, &requested)?;
        if path.extension().is_none_or(|extension| extension != "p") {
            return Err(tinyagents::TinyAgentsError::Validation(format!(
                "`{requested}` is not a `.p` file; write the axioms and the conjecture as a TPTP \
                 problem first"
            )));
        }
        if !path.is_file() {
            return Err(tinyagents::TinyAgentsError::Validation(format!(
                "`{requested}` does not exist in the workspace; write it before searching it"
            )));
        }
        let relative = paths::strip_workspace_prefix(&requested).to_string();
        let output = self.run(&path).await?;
        let verdict = parse(&relative, &output);
        self.file(&verdict).await?;
        Ok(ToolResult::text(call.id, self.name(), verdict.render()))
    }
}

#[cfg(test)]
#[path = "refute_test.rs"]
mod test;
