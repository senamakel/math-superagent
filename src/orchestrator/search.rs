//! Scored program search: the `FunSearch` loop, with the verifier put out of the
//! searcher's reach.
//!
//! The runtime could already write a program, run it, and read what it printed.
//! What it had no version of is *search over programs* — propose, score,
//! keep the good ones, propose again from those — which is how `FunSearch`
//! improved the cap-set lower bound past twenty years of work and how
//! `AlphaEvolve` matched or beat the literature on 20 of 67 problems. The move
//! that makes it worth having is not the loop; it is what the loop produces.
//! `FunSearch`'s own statement of it: "we do not just discover the set of 512
//! eight-dimensional vectors in itself, but a program that generates it …
//! Through inspecting the code, we obtain a degree of understanding of what
//! this set is." A number is an answer; a program is an explanation, which is
//! this repository's stated standard for what a result has to be.
//!
//! Three of `FunSearch`'s four ingredients are bookkeeping and therefore live
//! here in Rust rather than in a prompt: the skeleton with exactly one evolved
//! function, best-shot prompting, and the island population. A model asked to
//! remember which programs scored best, and to sample them in the right order,
//! is a model spending its turn on arithmetic something else can do exactly.
//! The fourth — asynchronous scaling — the runtime already has.
//!
//! # The verifier is an adversarial boundary
//!
//! This is the part that is not a convenience. Tao, Georgiev, Gómez-Serrano and
//! Wagner found that `AlphaEvolve` is "extremely good at locating exploits in the
//! verification code", in one case satisfying a minimum-distance constraint by
//! placing points nearly on top of one another; they rewrote their verifiers in
//! exact arithmetic with conservative bounds, and warn that "blindly trusting
//! the AE values can be risky as they may be a consequence of verifier exploits
//! rather than any true progress."
//!
//! An autonomous agent occupies that row by default, because the search and the
//! verifier are written by the same process. So the split is a *tool boundary*
//! rather than an instruction: the `searcher` role holds no file-write tool at
//! all. It cannot edit [`SCORER`], it cannot edit the skeleton, and the only
//! way a candidate reaches disk is [`SubmitCandidate`], which writes it and
//! scores it in one call. A program that was never executed cannot be recorded,
//! and a scorer the searcher dislikes cannot be adjusted.
//!
//! # Cheap rejection, counted
//!
//! `FunSearch` discards what does not run: "Programs that were incorrect (that
//! did not execute within the imposed time and memory limits, or produced
//! invalid outputs) are discarded." That cuts against this runtime, which
//! reflects on failures and writes a lesson from each — correctly, for an
//! attempt that costs an hour, and ruinously for a search whose whole method is
//! to be wrong thousands of times cheaply.
//!
//! Both survive here by separating the two meanings of "silent". A rejected
//! candidate costs no reflection, no lesson, and no reasoning turn — the tool
//! says it was discarded and why in one line. But it is *recorded*, so the
//! ledger can say how many candidates the search spent to buy its best score.
//! A search that has run four hundred candidates without improving is a finding
//! nobody obtains from a leaderboard that shows only the winners.

use std::collections::BTreeMap;
use std::fmt::Write as _;
use std::path::{Path, PathBuf};
use std::time::Duration;

use async_trait::async_trait;
use serde_json::json;

use super::string_argument;
use crate::agent::{Result, Tool, ToolCall, ToolResult, ToolSchema};

/// Root of the search tree, one subdirectory per search.
pub(super) const SEARCH_DIR: &str = "code/search";

/// The verifier, written once by a role that is not the searcher.
///
/// Named by a constant rather than by convention because two separate things
/// depend on the name agreeing: the runner invokes it, and the searcher's write
/// boundary is defined as everything that is *not* it.
pub(super) const SCORER: &str = "score.py";

/// Where a proposed program is written, and the only path the searcher reaches.
pub(super) const CANDIDATE_DIR: &str = "candidates";

/// The append-only record of every candidate ever scored.
pub(super) const LEDGER: &str = "scores.jsonl";

/// The derived leaderboard, filed beside the programs it ranks.
pub(super) const BOARD: &str = "SEARCH.md";

/// How many islands the population is split across.
///
/// `FunSearch`'s third ingredient: "we maintain a large pool of diverse programs
/// by using an island-based evolutionary method that encourages exploration and
/// avoids local optima." Four rather than the paper's ten because this runtime
/// samples a frontier model at a few hundred candidates per run, not Codey at
/// 10⁶ — ten islands at this scale is ten populations of two, which is not a
/// population.
const ISLANDS: usize = 4;

/// How many previous programs a best-shot brief carries.
///
/// Two, as in the paper. This is a *prompt cost*: every candidate in the brief
/// is re-sent on the model call that proposes the next one, so a large k buys
/// context at the price of the samples that context was supposed to fund.
const BEST_SHOT: usize = 2;

/// Candidates an island may record without improving before it is reseeded.
///
/// `FunSearch` resets the worst islands on a wall-clock cadence. A cadence is the
/// wrong instrument here, because this runtime's searches are bounded by a run
/// budget rather than by hours — so the trigger is staleness, which is what the
/// cadence was a proxy for. A reseeded island restarts from the best program in
/// the whole population, which is the paper's rule and the reason a reset
/// explores rather than forgets.
const ISLAND_STALE: usize = 12;

/// How long one scoring run may take.
///
/// Deliberately far below the shell tool's ceiling. A scorer is a verifier, not
/// an experiment: it reads one candidate and returns a number. One that needs
/// ten minutes is one the search cannot afford to call a thousand times, and
/// discovering that at candidate four hundred is worse than discovering it at
/// candidate one.
const SCORE_TIMEOUT: Duration = Duration::from_mins(1);

/// Address space one scoring run may claim, in bytes.
///
/// The container's own cap is 8 GiB and is the wrong instrument for this: it
/// kills the *run*, so a single candidate that allocates without bound ends an
/// investigation and leaves an OOM to be found in `docker events` rather than a
/// rejected candidate on the board. This is deliberately far below it, so the
/// scorer dies and the search carries on.
///
/// Two gibibytes rather than one because the image bakes in `numpy`, `sympy`
/// and `scipy`, and importing them reserves address space well beyond what they
/// touch — `ulimit -v` bounds the reservation, not the resident set, so a tight
/// value would reject honest scorers at `import numpy`. A verifier reads one
/// candidate and returns a number; one needing more than this is one the search
/// cannot afford thousands of calls to.
const SCORER_MEMORY: usize = 2 * 1024 * 1024 * 1024;

/// How much of a scorer's output is kept.
const MAX_SCORE_OUTPUT: usize = 8 * 1024;

/// The line a scorer prints to report a candidate's value.
const SCORE_MARK: &str = "SCORE:";

/// The line a scorer prints to reject a candidate.
const INVALID_MARK: &str = "INVALID:";

/// What became of one proposed program.
#[derive(Clone, Debug, PartialEq)]
pub(super) enum Outcome {
    /// The scorer accepted it, at this value.
    ///
    /// The value is kept as the scorer printed it *and* as a number. The string
    /// is what the board shows, because a scorer following the exact-arithmetic
    /// rule prints `355/113` or a forty-digit integer, and rendering that
    /// through an `f64` is the precision loss the rule exists to prevent. The
    /// number is only ever used to order candidates.
    Scored { shown: String, value: f64 },
    /// The scorer rejected it, or it did not run.
    Invalid(String),
}

impl Outcome {
    /// The value, for ordering; `None` when there is nothing to order.
    fn value(&self) -> Option<f64> {
        match self {
            Self::Scored { value, .. } => Some(*value),
            Self::Invalid(_) => None,
        }
    }
}

/// One program the search has evaluated.
#[derive(Clone, Debug)]
pub(super) struct Candidate {
    /// Stable identifier, and the stem of the file holding the program.
    pub(super) id: String,
    /// Which island proposed it.
    pub(super) island: usize,
    /// What the scorer made of it.
    pub(super) outcome: Outcome,
}

/// Every candidate one search has recorded, in the order it recorded them.
///
/// Order is load-bearing rather than incidental: staleness is "how many
/// candidates has this island recorded since its last improvement", which is a
/// question about sequence. A `BTreeMap` keyed by score would answer the
/// leaderboard question and lose that one.
#[derive(Clone, Debug, Default)]
pub(super) struct Population {
    pub(super) candidates: Vec<Candidate>,
}

impl Population {
    /// Reads the ledger for one search.
    ///
    /// A line that cannot be parsed is skipped rather than failing the load. The
    /// ledger is append-only and written by a tool that may be killed by the run
    /// cap mid-write, so a torn final line is an ordinary event — and losing the
    /// whole population to it would discard hours of scoring for one truncated
    /// record.
    pub(super) fn load(workspace: &Path, slug: &str) -> Self {
        let path = workspace.join(SEARCH_DIR).join(slug).join(LEDGER);
        let Ok(text) = std::fs::read_to_string(path) else {
            return Self::default();
        };
        let candidates = text
            .lines()
            .filter_map(|line| serde_json::from_str::<serde_json::Value>(line).ok())
            .filter_map(|row| read_row(&row))
            .collect();
        Self { candidates }
    }

    /// The best-scoring candidate overall, if any scored.
    pub(super) fn best(&self) -> Option<&Candidate> {
        self.scored().max_by(|left, right| compare(left, right))
    }

    /// Every candidate the scorer accepted.
    fn scored(&self) -> impl Iterator<Item = &Candidate> {
        self.candidates
            .iter()
            .filter(|candidate| candidate.outcome.value().is_some())
    }

    /// How many candidates have been discarded.
    pub(super) fn discarded(&self) -> usize {
        self.candidates.len() - self.scored().count()
    }

    /// Which island the next proposal is *expected* to land on.
    ///
    /// Round-robin rather than random, because this crate cannot use
    /// `Math::random`-style nondeterminism in anything a test has to pin down —
    /// and round-robin gives every island the same number of proposals, which
    /// is what the island model wants anyway.
    ///
    /// Advisory, and only advisory. What a candidate's island actually *is* is
    /// `index % ISLANDS` for the index [`reserve`] claimed, because that index
    /// is decided by the kernel and this count is not: a torn ledger line or a
    /// concurrent submission makes the two disagree. The brief reports this so
    /// a proposal knows roughly which island it is writing for; the ledger
    /// records the other. Deriving the recorded island from here is the bug
    /// [`reserve`] exists to prevent, one field over.
    pub(super) fn next_island(&self) -> usize {
        self.candidates.len() % ISLANDS
    }

    /// Candidates on one island, oldest first.
    fn island(&self, island: usize) -> impl Iterator<Item = &Candidate> {
        self.candidates
            .iter()
            .filter(move |candidate| candidate.island == island)
    }

    /// Whether an island has gone [`ISLAND_STALE`] candidates without a gain.
    fn stale(&self, island: usize) -> bool {
        let mut best: Option<f64> = None;
        let mut since = 0_usize;
        for candidate in self.island(island) {
            match candidate.outcome.value() {
                Some(value) if best.is_none_or(|top| value > top) => {
                    best = Some(value);
                    since = 0;
                }
                _ => since += 1,
            }
        }
        since >= ISLAND_STALE
    }

    /// The programs one proposal is shown, worst first.
    ///
    /// Worst-to-best is `FunSearch`'s order and not an arbitrary one: the last
    /// thing in the prompt is the thing the model is most likely to build on,
    /// so the ordering makes "improve on this" the default reading without a
    /// sentence asking for it.
    ///
    /// A stale island is shown the whole population's best instead of its own,
    /// which is the reset: it keeps the island's next proposal from being the
    /// thirteenth variation on a local optimum, without deleting anything the
    /// ledger recorded.
    pub(super) fn best_shot(&self, island: usize) -> Vec<&Candidate> {
        let mut pool: Vec<&Candidate> = if self.stale(island) {
            self.scored().collect()
        } else {
            self.island(island)
                .filter(|candidate| candidate.outcome.value().is_some())
                .collect()
        };
        pool.sort_by(|left, right| compare(left, right));
        pool.into_iter().rev().take(BEST_SHOT).rev().collect()
    }

    /// Renders the leaderboard filed beside the programs.
    pub(super) fn render(&self, slug: &str) -> String {
        let mut out = format!(
            "# Search — {slug}\n\nDerived from `{LEDGER}`; do not edit, the next candidate \
             re-derives it. Every row is a program in `{CANDIDATE_DIR}/` that was executed \
             against `{SCORER}` — a candidate that was not executed is not here, because \
             nothing can record one.\n\n"
        );
        if self.candidates.is_empty() {
            let _ = writeln!(
                out,
                "_Nothing scored yet. Write `{SCORER}` first: it takes a candidate module path \
                 on argv, and prints one `{SCORE_MARK} <value>` line or one `{INVALID_MARK} \
                 <reason>` line. Use exact arithmetic — a search finds the slack in a verifier \
                 before it finds the mathematics._"
            );
            return out;
        }
        let _ = writeln!(
            out,
            "{} candidates scored, {} discarded.\n",
            self.scored().count(),
            self.discarded()
        );
        out.push_str("| Candidate | Island | Score |\n| --- | --- | --- |\n");
        let mut ranked: Vec<&Candidate> = self.scored().collect();
        ranked.sort_by(|left, right| compare(right, left));
        let (rows, dropped) = super::ledger::budget::listed(ranked, MAX_ROWS, |out, candidate| {
            let Outcome::Scored { shown, .. } = &candidate.outcome else {
                return;
            };
            let _ = writeln!(
                out,
                "| `{CANDIDATE_DIR}/{}.py` | {} | `{shown}` |",
                candidate.id, candidate.island
            );
        });
        out.push_str(&rows);
        out.push_str(&super::ledger::budget::elided(dropped, LEDGER));
        self.append_rejections(&mut out);
        out
    }

    /// Summarises why candidates were discarded, without listing every one.
    ///
    /// The counts rather than the rows, because the rows are the bulk and the
    /// distribution is the finding: a search whose rejections are all "did not
    /// finish in time" has a scorer too slow to search with, and one whose
    /// rejections are all the same constraint has found the constraint that
    /// actually binds. Neither is visible from a leaderboard of winners.
    fn append_rejections(&self, out: &mut String) {
        let mut reasons: BTreeMap<&str, usize> = BTreeMap::new();
        for candidate in &self.candidates {
            if let Outcome::Invalid(reason) = &candidate.outcome {
                *reasons.entry(reason.as_str()).or_default() += 1;
            }
        }
        if reasons.is_empty() {
            return;
        }
        out.push_str("\n## Why candidates were discarded\n\n");
        let mut rows: Vec<(&&str, &usize)> = reasons.iter().collect();
        rows.sort_by(|left, right| right.1.cmp(left.1));
        // Bounded on both axes, because bounding the rows alone still admits
        // forty six-kilobyte reasons — which is the same unbounded file by
        // another route, and the shape `APPROACHES.md` reached 86 KB through.
        let (listed, dropped) =
            super::ledger::budget::listed(rows, MAX_ROWS, |out, (reason, count)| {
                let mut reason = (*reason).to_string();
                // `nth(n)` is the byte offset of the character *after* the
                // first `n`, which is exactly where to cut to keep `n` of
                // them; `None` means there were fewer, so keep all. Truncating
                // to the last offset that fits instead drops a character, and
                // on a multi-byte boundary `truncate` would panic.
                let cut = reason
                    .char_indices()
                    .nth(super::ledger::budget::REASON_CHARS)
                    .map_or(reason.len(), |(at, _)| at);
                reason.truncate(cut);
                let _ = writeln!(out, "- {count}× {reason}");
            });
        out.push_str(&listed);
        out.push_str(&super::ledger::budget::elided(dropped, LEDGER));
    }
}

/// Rows one rendering shows.
const MAX_ROWS: usize = 20;

/// Orders two candidates by score, worst first.
///
/// Unscored candidates sort below everything. `total_cmp` rather than
/// `partial_cmp` so the ordering is total: a `NaN` that survived the finiteness
/// check would otherwise make the sort's result depend on the input order.
fn compare(left: &Candidate, right: &Candidate) -> std::cmp::Ordering {
    let key = |candidate: &Candidate| candidate.outcome.value().unwrap_or(f64::NEG_INFINITY);
    key(left).total_cmp(&key(right))
}

/// Reads one ledger row.
fn read_row(row: &serde_json::Value) -> Option<Candidate> {
    let id = row.get("id")?.as_str()?.to_string();
    let island = usize::try_from(row.get("island")?.as_u64()?).ok()?;
    let outcome = match row.get("score").and_then(serde_json::Value::as_str) {
        Some(shown) => Outcome::Scored {
            value: shown.parse::<f64>().ok().or_else(|| ratio(shown))?,
            shown: shown.to_string(),
        },
        None => Outcome::Invalid(
            row.get("reason")
                .and_then(serde_json::Value::as_str)
                .unwrap_or("discarded")
                .to_string(),
        ),
    };
    Some(Candidate {
        id,
        island,
        outcome,
    })
}

/// Reads `a/b` as a number, for a scorer following the exact-arithmetic rule.
///
/// A verifier told to avoid floating point prints a fraction, and a search that
/// could not order `355/113` would silently treat every exact score as
/// unscored — discarding precisely the candidates the rule was meant to
/// protect.
fn ratio(text: &str) -> Option<f64> {
    let (numerator, denominator) = text.split_once('/')?;
    let numerator = numerator.trim().parse::<f64>().ok()?;
    let denominator = denominator.trim().parse::<f64>().ok()?;
    if denominator == 0.0 {
        return None;
    }
    Some(numerator / denominator)
}

/// Reads a scorer's output into an outcome.
///
/// The last `SCORE:` line wins, so a scorer that prints progress before its
/// verdict is not misread. An output carrying neither marker is a rejection
/// rather than a zero: a scorer that printed nothing recognisable has not
/// approved anything, and defaulting to a number would enter an unverified
/// candidate onto the board.
pub(super) fn parse_outcome(output: &str) -> Outcome {
    let mut invalid = None;
    let mut scored = None;
    for line in output.lines() {
        let line = line.trim();
        if let Some(rest) = line.strip_prefix(SCORE_MARK) {
            scored = Some(rest.trim().to_string());
        } else if let Some(rest) = line.strip_prefix(INVALID_MARK) {
            invalid = Some(rest.trim().to_string());
        }
    }
    // A scorer that printed both has rejected the candidate and then reported a
    // number for it, which is a contradiction in the verifier rather than a
    // result. Taking the rejection is the safe reading: the cost is one
    // discarded candidate out of thousands, where the cost of the other reading
    // is an unverified program on the board.
    if let Some(reason) = invalid {
        return Outcome::Invalid(format!("rejected by the scorer: {reason}"));
    }
    match scored {
        Some(shown) => {
            let value = shown.parse::<f64>().ok().or_else(|| ratio(&shown));
            match value {
                Some(value) if value.is_finite() => Outcome::Scored { shown, value },
                // An infinite or unparseable score is how a verifier exploit
                // most often surfaces: a candidate that divides by the
                // constraint it was supposed to satisfy scores `inf` and tops
                // the board forever.
                _ => Outcome::Invalid(format!("scorer printed an unusable value: {shown}")),
            }
        }
        None => match tail(output) {
            Some(said) => Outcome::Invalid(format!(
                "scorer printed no `{SCORE_MARK}` line, so nothing was verified; it said: {said}"
            )),
            None => Outcome::Invalid(format!(
                "scorer printed no `{SCORE_MARK}` line and produced no output at all, so nothing \
                 was verified"
            )),
        },
    }
}

/// Characters of the scorer's own output carried back on an unparseable run.
///
/// Small on purpose. This is not the artifact channel: it is the one line that
/// says *why* nothing was scored, and a rejection has to stay cheap.
const TAIL_CHARS: usize = 240;

/// The informative end of a scorer's output, whitespace collapsed to one line.
///
/// The *tail* rather than the head because the two things that land here are a
/// Python traceback, whose last line names the exception, and a `usage:` exit,
/// which is the whole output. A head would show the traceback's frames and cut
/// off before the reason.
///
/// This exists because of a live run. A Frankl scorer declared
/// `usage: python score.py alpha a1 a2 b1 b2` while the harness calls
/// `python3 score.py candidates/c0000.py`, so every candidate exited on the
/// usage line. The searcher was told only that nothing was verified — a verdict
/// it cannot act on and cannot distinguish from a bug in its own program — and
/// wrote seven candidates against a contract the harness never speaks. One line
/// of the scorer's own output names the fault immediately.
fn tail(output: &str) -> Option<String> {
    let collapsed = output.split_whitespace().collect::<Vec<_>>().join(" ");
    if collapsed.is_empty() {
        return None;
    }
    let from = collapsed
        .char_indices()
        .rev()
        .nth(TAIL_CHARS.saturating_sub(1))
        .map_or(0, |(at, _)| at);
    let mut shown = collapsed[from..].to_string();
    if from > 0 {
        shown.insert(0, '…');
    }
    Some(shown)
}

/// Candidates one search may record before it is refused.
///
/// A runaway guard rather than a budget — the run budget is what actually ends
/// a search — in the spirit of `ledger::registry::MAX_DEFINED`. It also bounds
/// the scan in [`reserve`], which would otherwise have no termination condition
/// if every name were somehow taken.
const MAX_CANDIDATES: usize = 5_000;

/// Claims the next free candidate id by creating its file.
///
/// The id used to be `format!("c{:04}", population.candidates.len())`, derived
/// from the number of ledger rows that *parsed*, and that is wrong in two ways
/// that both destroy work silently.
///
/// A torn final line is an ordinary event here — [`Population::load`] skips one
/// by design, because the ledger is appended to by a tool the run cap can kill
/// mid-write. But skipping it also lowers the count, so the next candidate
/// takes an id that is already on disk and **overwrites the program that holds
/// it**, while both rows stay in the ledger pointing at one file.
///
/// And two searchers submitting at once both read the same length, both write
/// `c0007.py`, and one program is gone. That is not hypothetical: sharing one
/// population across concurrent searchers is the whole point of running more
/// than one.
///
/// `create_new(true)` moves the decision to the kernel, which is the only place
/// it can be made correctly: the first caller whose `open` succeeds owns that
/// index, and every other caller moves on. The scan starts from the population
/// count because that is a good guess, never because it is trusted.
///
/// # Errors
///
/// Returns an error when no free id exists below [`MAX_CANDIDATES`], or when
/// the candidate file cannot be created for a reason other than already
/// existing.
fn reserve(parent: &Path, from: usize) -> Result<(usize, String)> {
    for index in from..MAX_CANDIDATES {
        let id = format!("c{index:04}");
        match std::fs::OpenOptions::new()
            .write(true)
            .create_new(true)
            .open(parent.join(format!("{id}.py")))
        {
            Ok(_) => return Ok((index, id)),
            // Taken by another submission; try the next index.
            Err(error) if error.kind() == std::io::ErrorKind::AlreadyExists => {}
            Err(error) => {
                return Err(tinyagents::TinyAgentsError::Tool(format!(
                    "failed to create the candidate: {error}"
                )));
            }
        }
    }
    Err(tinyagents::TinyAgentsError::Validation(format!(
        "this search has already recorded {MAX_CANDIDATES} candidates; start another search \
         rather than growing this one"
    )))
}

/// Whether a name is safe to use as a search's directory.
///
/// Checked rather than passed to [`paths::checked_workspace_path`] alone,
/// because a slug is a single directory name and traversal is not the only way
/// to misuse one: a slug containing a separator would scatter one search's
/// programs across a tree the board cannot then find.
fn checked_slug(slug: &str) -> Result<String> {
    let slug = slug.trim();
    let sane = !slug.is_empty()
        && slug.len() <= 64
        && slug
            .chars()
            .all(|c| c.is_ascii_alphanumeric() || c == '-' || c == '_');
    if !sane {
        return Err(tinyagents::TinyAgentsError::Validation(format!(
            "`{slug}` is not a search name: use letters, digits, `-` and `_`, up to 64 characters"
        )));
    }
    Ok(slug.to_string())
}

/// Reads a file under a search's directory, or an empty string.
fn read(root: &Path, name: &str) -> String {
    std::fs::read_to_string(root.join(name)).unwrap_or_default()
}

/// The brief one proposal is written against.
///
/// A separate tool rather than context routed into the prompt, because it
/// changes on every candidate: the whole point of best-shot prompting is that
/// the sample reflects what has just been scored, and a system prompt is
/// assembled once per run. It is also why the sample is assembled here rather
/// than left to the searcher to reconstruct — a model asked to remember which
/// of four hundred programs scored best, and to order them worst-to-best, is
/// spending its turn on bookkeeping that cannot be got wrong in Rust.
#[derive(Debug)]
pub(super) struct SearchBrief {
    workspace: PathBuf,
}

impl SearchBrief {
    pub(super) fn new(workspace: PathBuf) -> Self {
        Self { workspace }
    }
}

#[async_trait]
impl Tool<()> for SearchBrief {
    fn name(&self) -> &'static str {
        "search_brief"
    }

    fn description(&self) -> &'static str {
        "Returns what to write next for a scored program search: the problem, the scorer that \
         will judge it, and the best programs found so far, worst first."
    }

    fn schema(&self) -> ToolSchema {
        ToolSchema::new(
            self.name(),
            self.description(),
            json!({
                "type": "object",
                "properties": {
                    "slug": {
                        "type": "string",
                        "description": "Name of the search, a directory under code/search."
                    }
                },
                "required": ["slug"],
                "additionalProperties": false
            }),
        )
    }

    async fn call(&self, _state: &(), call: ToolCall) -> Result<ToolResult> {
        let slug = checked_slug(&string_argument(&call, "slug")?)?;
        let root = self.workspace.join(SEARCH_DIR).join(&slug);
        let scorer = read(&root, SCORER);
        if scorer.trim().is_empty() {
            return Err(tinyagents::TinyAgentsError::Validation(format!(
                "`{SEARCH_DIR}/{slug}/{SCORER}` does not exist, so nothing can score a candidate. \
                 It is not yours to write: ask for it, then search against it"
            )));
        }
        let population = Population::load(&self.workspace, &slug);
        let island = population.next_island();
        let mut out = format!(
            "search: {slug}\nisland: {island}\nscored so far: {}\ndiscarded so far: {}\n\n\
             ## The problem\n\n{}\n\n## The scorer that will judge your program \
             (`{SCORER}` — you cannot edit it)\n\n```python\n{scorer}\n```\n",
            population.scored().count(),
            population.discarded(),
            read(&root, "PROBLEM.md").trim(),
        );
        let sample = population.best_shot(island);
        if sample.is_empty() {
            out.push_str(
                "\n## Previous programs\n\nNone yet. Write the simplest thing that scores at \
                 all — a first candidate exists to prove the scorer runs, not to be good.\n",
            );
            return Ok(ToolResult::text(call.id, self.name(), out));
        }
        out.push_str("\n## Previous programs, worst first — improve on the last one\n");
        for candidate in sample {
            let shown = match &candidate.outcome {
                Outcome::Scored { shown, .. } => shown.as_str(),
                Outcome::Invalid(_) => continue,
            };
            let program = read(&root.join(CANDIDATE_DIR), &format!("{}.py", candidate.id));
            let _ = write!(
                out,
                "\n### `{}` — score `{shown}`\n\n```python\n{}\n```\n",
                candidate.id,
                program.trim()
            );
        }
        Ok(ToolResult::text(call.id, self.name(), out))
    }
}

/// Writes one proposed program, scores it, and records what happened.
///
/// One call rather than three, and that is the control. Separate `write`,
/// `run`, and `record` steps would let a candidate be recorded without having
/// been executed — which is the failure this repository keeps finding in other
/// forms, an answer no program produced. Here it cannot be expressed: the only
/// path onto the board runs the scorer first.
#[derive(Debug)]
pub(super) struct SubmitCandidate {
    workspace: PathBuf,
}

impl SubmitCandidate {
    pub(super) fn new(workspace: PathBuf) -> Self {
        Self { workspace }
    }

    /// Runs the scorer over one written candidate.
    ///
    /// A timeout is a rejection rather than an error, because that is what it
    /// means to a search: this candidate is too slow to be worth having, and
    /// the next one should be cheaper. Treating it as a tool failure would end
    /// the searcher's turn on the most ordinary event in the loop.
    ///
    /// Memory is bounded for the same reason and by a harder mechanism. The
    /// timeout bounds how long a candidate may take and bounded nothing about
    /// how much it may allocate, so a construction that builds a list of every
    /// subset was answered by the *container's* cap — which kills the run, not
    /// the candidate, and leaves an OOM to be diagnosed from
    /// `docker events`. [`SCORER_MEMORY`] is well below that cap so the
    /// scorer dies first and the search continues, and it is enforced by
    /// `setrlimit` in the child rather than by polling its RSS, so the
    /// allocation fails at the point it is made instead of being noticed a
    /// tick later.
    async fn score(&self, root: &Path, relative: &str) -> Outcome {
        let mut command = tokio::process::Command::new("sh");
        let run = command
            .arg("-c")
            // `ulimit` rather than a `pre_exec` hook calling `setrlimit`,
            // because `pre_exec` is `unsafe` and this crate forbids `unsafe`.
            // The shell reaches the same kernel limit without a new dependency
            // and without the one construct the crate does not allow.
            //
            // Both interpolated values are constants or derived from an
            // integer — `SCORER` is a `const` and `relative` is
            // `candidates/c0007.py` built from a reserved index — so there is
            // nothing here a candidate could steer. Neither is ever the
            // model's text.
            .arg(format!(
                "ulimit -v {}; exec python3 {SCORER} {relative}",
                SCORER_MEMORY / 1024
            ))
            .current_dir(root)
            .kill_on_drop(true)
            .stdout(std::process::Stdio::piped())
            .stderr(std::process::Stdio::piped())
            .output();
        let Ok(finished) = tokio::time::timeout(SCORE_TIMEOUT, run).await else {
            return Outcome::Invalid(format!(
                "did not finish within {} seconds",
                SCORE_TIMEOUT.as_secs()
            ));
        };
        let Ok(output) = finished else {
            return Outcome::Invalid("the scorer could not be executed".to_string());
        };
        let mut text = String::from_utf8_lossy(&output.stdout).into_owned();
        text.push_str(&String::from_utf8_lossy(&output.stderr));
        text.truncate(
            text.char_indices()
                .map(|(at, _)| at)
                .take_while(|at| *at <= MAX_SCORE_OUTPUT)
                .last()
                .unwrap_or(0),
        );
        parse_outcome(&text)
    }
}

#[async_trait]
impl Tool<()> for SubmitCandidate {
    fn name(&self) -> &'static str {
        "submit_candidate"
    }

    fn description(&self) -> &'static str {
        "Writes one candidate program, runs the search's scorer over it, and records the result. \
         Writing and scoring are one step: a candidate that was not executed cannot be recorded."
    }

    fn schema(&self) -> ToolSchema {
        ToolSchema::new(
            self.name(),
            self.description(),
            json!({
                "type": "object",
                "properties": {
                    "slug": {
                        "type": "string",
                        "description": "Name of the search, a directory under code/search."
                    },
                    "program": {
                        "type": "string",
                        "description": "The complete candidate module. It must define whatever \
                                        the scorer imports from it and nothing else needs to be \
                                        true of it."
                    }
                },
                "required": ["slug", "program"],
                "additionalProperties": false
            }),
        )
    }

    async fn call(&self, _state: &(), call: ToolCall) -> Result<ToolResult> {
        let slug = checked_slug(&string_argument(&call, "slug")?)?;
        let program = string_argument(&call, "program")?;
        let root = self.workspace.join(SEARCH_DIR).join(&slug);
        if !root.join(SCORER).is_file() {
            return Err(tinyagents::TinyAgentsError::Validation(format!(
                "`{SEARCH_DIR}/{slug}/{SCORER}` does not exist, so there is nothing to score \
                 against"
            )));
        }
        let mut population = Population::load(&self.workspace, &slug);
        let parent = root.join(CANDIDATE_DIR);
        tokio::fs::create_dir_all(&parent).await.map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!("failed to create {CANDIDATE_DIR}: {error}"))
        })?;
        // Derived rather than supplied, so a proposal cannot overwrite an
        // earlier one — by collision or by choosing to.
        let (index, id) = reserve(&parent, population.candidates.len())?;
        let island = index % ISLANDS;
        let relative = format!("{CANDIDATE_DIR}/{id}.py");
        let path = root.join(&relative);
        tokio::fs::write(&path, &program).await.map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!("failed to write the candidate: {error}"))
        })?;

        let outcome = self.score(&root, &relative).await;
        let row = match &outcome {
            Outcome::Scored { shown, .. } => {
                json!({ "id": id, "island": island, "score": shown })
            }
            Outcome::Invalid(reason) => {
                json!({ "id": id, "island": island, "reason": reason })
            }
        };
        append(&root, &row).await?;
        population.candidates.push(Candidate {
            id: id.clone(),
            island,
            outcome: outcome.clone(),
        });
        let _ = tokio::fs::write(root.join(BOARD), population.render(&slug)).await;

        let verdict = match &outcome {
            Outcome::Scored { shown, .. } => {
                let best = population
                    .best()
                    .filter(|best| best.id != id)
                    .and_then(|best| match &best.outcome {
                        Outcome::Scored { shown, .. } => Some(shown.clone()),
                        Outcome::Invalid(_) => None,
                    });
                match best {
                    Some(best) => format!("scored {shown}; the best so far is {best}"),
                    None => format!("scored {shown}, which is the best so far"),
                }
            }
            // Deliberately one line and no advice. A rejected candidate is the
            // ordinary case in a search and must cost as close to nothing as
            // possible; a paragraph of guidance here would be re-read on every
            // one of them.
            Outcome::Invalid(reason) => format!("discarded: {reason}"),
        };
        Ok(ToolResult::text(
            call.id,
            self.name(),
            format!("{relative} {verdict}"),
        ))
    }
}

/// Appends one row to a search's ledger.
///
/// # Errors
///
/// Returns an error when the ledger cannot be written — which, unlike a failed
/// score, must not be swallowed: a candidate that ran and was not recorded is
/// spent budget the next proposal cannot see.
async fn append(root: &Path, row: &serde_json::Value) -> Result<()> {
    use tokio::io::AsyncWriteExt as _;
    tokio::fs::create_dir_all(root).await.map_err(|error| {
        tinyagents::TinyAgentsError::Tool(format!("failed to create the search directory: {error}"))
    })?;
    let mut file = tokio::fs::OpenOptions::new()
        .create(true)
        .append(true)
        .open(root.join(LEDGER))
        .await
        .map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!("failed to open the score ledger: {error}"))
        })?;
    file.write_all(format!("{row}\n").as_bytes())
        .await
        .map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!("failed to record the score: {error}"))
        })
}

#[cfg(test)]
#[path = "search_test.rs"]
mod test;
