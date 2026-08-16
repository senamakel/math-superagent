//! Claim-level retrieval over the reference library.
//!
//! The unit of the research folder is a *file*, and a file is the wrong thing
//! to retrieve. An agent about to compute something does not need "Siegel
//! 2009"; it needs the sentence *a loopy game is a zugzwang game iff it equals
//! `x & y` for dyadic `x <= y`*, together with whether those hypotheses hold
//! here, whether the source proves it or merely asserts it, and where in the
//! text to check. Reading a note to recover one of those costs a note; reading
//! six notes to find which one carries it costs six.
//!
//! So a note may carry `claim` blocks, and this module derives one table from
//! all of them. The table is derived rather than written for the same reason
//! `INDEX.md` is: whether the ledger agrees with the notes is not a judgement,
//! and a hand-maintained ledger drifts silently from the files it claims to
//! summarise. What *is* a judgement — what a source establishes, and whether
//! its hypotheses hold for this problem — stays with the scholar who writes
//! the block.
//!
//! Two things fall out of this for free, and both were previously asked for in
//! a prompt and never mechanically checked. A claim that names another claim
//! it contradicts produces a contradiction the run can see; the scholar prompt
//! calls finding one "the most valuable thing you can find" and nothing
//! detected it. And a claim marked as holding here while its status is only
//! *asserted* is a load-bearing belief nobody has verified, which is exactly
//! the thing the method policy says to distinguish and exactly the thing a
//! long run forgets it did.

use std::collections::BTreeSet;
use std::fmt::Write as _;
use std::path::Path;

use super::ledger::budget;
use super::text::truncate;

/// The derived table, filed with the library it describes.
pub(super) const CLAIMS_PATH: &str = "derived/CLAIMS.md";

/// Where the claim blocks themselves live.
///
/// Unlike every other ledger this one has no directory of its own: a claim is a
/// fenced block inside whatever note established it, so a section that has been
/// cut points at the library rather than at one folder. `search_claims` is the
/// better route and the section blurbs say so; this is the answer to *where do
/// I look* for a reader who is not an agent.
const NOTES_ROOT: &str = "research/";

/// Rows the rendered table carries.
///
/// `CLAIMS.md` is routed into system prompts, so every model call in every
/// role that reads it pays for each row. A library with more claims than this
/// must rely on Cognee recall rather than growing this current-run table.
const MAX_ROWS: usize = 60;

/// Characters one rendered statement is held to.
const STATEMENT_CHARS: usize = 220;

/// Files one derivation may read.
const MAX_FILES: usize = 400;

/// Directory depth the walk descends.
const MAX_DEPTH: usize = 4;

/// Claims one search returns.
const MAX_RESULTS: usize = 8;

/// Whether the claim's hypotheses hold for the problem this run is solving.
///
/// The distinction the field exists for: a true theorem whose hypotheses fail
/// here is worse than no theorem, because it looks like progress.
/// Whether `text` opens with `word` as a whole word rather than as a fragment.
///
/// `starts_with` alone would read `notation` as `no`, which is the one way a
/// prefix match can invent an answer nobody gave.
fn starts_with_word(text: &str, word: &str) -> bool {
    text.strip_prefix(word)
        .is_some_and(|rest| rest.chars().next().is_none_or(|next| !next.is_alphanumeric()))
}

#[derive(Clone, Copy, Debug, Default, PartialEq, Eq)]
pub(super) enum Holds {
    /// The hypotheses were checked against this problem and hold.
    Yes,
    /// The hypotheses were checked and do not hold.
    No,
    /// Nobody has checked.
    #[default]
    Unchecked,
}

impl Holds {
    /// Reads the field, tolerating the reason written after the answer.
    ///
    /// This required the whole value to be exactly `yes`, `no`, or `unchecked`
    /// while [`Status::parse`] beside it matched on a prefix, and the
    /// inconsistency cost a live run its own best finding. PE620 established
    /// that its oracle model was wrong — `g(16,5,5,6) = 0` against a stated
    /// `9` — and wrote `holds-here: false — contradicts the worked oracle
    /// value 9.` The trailing clause is exactly what a role is asked for
    /// everywhere else in this workspace, and it turned a refutation the run
    /// had *checked* into `**unchecked**` in the ledger every planning role
    /// reads. Silently downgrading a negative result is the worst direction for
    /// this to fail in: a claim that does not hold is the one thing the ledger
    /// exists to stop the run building on.
    ///
    /// Prefix-matching rather than exact, for the same reason `Status` does:
    /// what follows the answer is prose, and an unrecognised value still falls
    /// through to `Unchecked`, so a hedge is never read as a decision.
    fn parse(value: &str) -> Self {
        let lowered = value.trim().to_ascii_lowercase();
        // `no` before `not checked`: the shorter word is a prefix of nothing
        // else here, but the order is what makes that safe to keep true.
        if ["yes", "true", "holds"]
            .iter()
            .any(|answer| starts_with_word(&lowered, answer))
        {
            Self::Yes
        } else if ["no", "false", "fails"]
            .iter()
            .any(|answer| starts_with_word(&lowered, answer))
        {
            Self::No
        } else {
            Self::Unchecked
        }
    }

    fn label(self) -> &'static str {
        match self {
            Self::Yes => "yes",
            Self::No => "no",
            Self::Unchecked => "**unchecked**",
        }
    }
}

/// What kind of evidence stands behind the claim.
///
/// The method policy requires a proof, a numerical check, a heuristic, and a
/// sourced assertion to be told apart. Making it a field is what lets the
/// ledger point at a belief the run is leaning on without evidence.
#[derive(Clone, Copy, Debug, Default, PartialEq, Eq)]
pub(super) enum Status {
    /// The source proves it.
    Proved,
    /// The Lean kernel checked it, in this run, in this workspace.
    ///
    /// A separate variant from [`Status::Proved`] rather than a stronger
    /// reading of it, and the distinction is the same one `Checked` already
    /// draws. `Proved` is a statement about a *source*: somebody else's paper
    /// contains the argument, and the run is relying on their word that it is
    /// sound. This is a statement about an artifact on disk in this workspace,
    /// which is a different kind of thing to be wrong about and a different
    /// kind of thing to check.
    ///
    /// It is the only status the ledger does not take on trust. Every other
    /// one is a word a model typed into a note; this one is dropped to
    /// `Asserted` unless [`super::lean::verdict`] finds a passing kernel
    /// verdict for the file the claim names. That is the point of it — until
    /// this existed, a formalisation and a sentence claiming a formalisation
    /// were the same row.
    Formalised,
    /// This run checked it numerically.
    Checked,
    /// The source states it without proof, or cites elsewhere.
    #[default]
    Asserted,
    /// Suggestive rather than established.
    Heuristic,
    /// Read out of a catalogue: a term list, a table, a b-file.
    ///
    /// This is not a weaker `Asserted`, it is a different thing, and Project
    /// Euler 241 is why it needs its own name. That run's answer —
    /// 482,316,491,800,641,154 — came from `sum_answer.py`, twenty lines
    /// summing a hardcoded copy of OEIS A159907's b-file, whose definition is
    /// the problem's own condition restated. Its actual derivation,
    /// `solution.py`, was wrong: 5 of the 9 terms below 10^8. Nothing on disk
    /// distinguished the two files, so a correct number sat beside a broken
    /// proof and the run had no way to notice.
    ///
    /// A catalogue is a legitimate and often excellent source — `oeis_lookup`
    /// is the first thing the librarian is told to reach for, and rightly. The
    /// failure is not consulting one, it is letting a lookup *stand in for* the
    /// derivation without saying so. Marked, it is a cross-check that confirms
    /// a result; unmarked, it is a substitute for one.
    Catalogued,
}

impl Status {
    fn parse(value: &str) -> Self {
        let lowered = value.trim().to_ascii_lowercase();
        if lowered.starts_with("formal")
            || lowered.starts_with("lean")
            || lowered.starts_with("kernel")
        {
            // Tested before `proved`, because "formally proved" is the phrase a
            // role reaches for. Read in the other order it lands on the weaker,
            // unchecked status — silently, and in the direction that loses the
            // check. Spelled several ways for the reason `Catalogued` is: a
            // role writing `lean` or `kernel` means exactly this, and falling
            // through to `asserted` would make a kernel-checked lemma
            // indistinguishable from a sentence.
            Self::Formalised
        } else if lowered.starts_with("proved") || lowered.starts_with("proven") {
            Self::Proved
        } else if lowered.starts_with("checked")
            || lowered.starts_with("numeric")
            || lowered.starts_with("measured")
        {
            // `measured` for the same reason `formal` is spelled several ways.
            // A run told to label a computation "measured, not proved" writes
            // exactly that, and the phrase used to fall through to `asserted` —
            // filing a result verified by three agreeing oracles under "not
            // checked here". `Checked` is what it means: this run computed it.
            Self::Checked
        } else if lowered.starts_with("heuristic") || lowered.starts_with("conject") {
            Self::Heuristic
        } else if lowered.starts_with("catalogue")
            || lowered.starts_with("cataloged")
            || lowered.starts_with("catalog")
            || lowered.starts_with("looked up")
            || lowered.starts_with("lookup")
            || lowered.starts_with("b-file")
            || lowered.starts_with("bfile")
            || lowered.starts_with("table")
        {
            // Spelled several ways on purpose. A role that writes `looked up`
            // or `b-file` means exactly this and should not silently fall
            // through to `asserted`, where it would be indistinguishable from
            // a theorem somebody stated without proof.
            Self::Catalogued
        } else {
            Self::Asserted
        }
    }

    pub(super) fn label(self) -> &'static str {
        match self {
            Self::Proved => "proved",
            Self::Formalised => "formalised",
            Self::Checked => "checked",
            Self::Asserted => "asserted",
            Self::Heuristic => "heuristic",
            Self::Catalogued => "catalogued",
        }
    }
}

/// One statement the library establishes, with its provenance and standing.
#[derive(Clone, Debug, Default)]
pub(super) struct Claim {
    /// Stable name, so other claims and other notes can refer to it.
    pub(super) id: String,
    /// What is being claimed.
    pub(super) statement: String,
    /// What the claim requires to be true.
    pub(super) hypotheses: String,
    /// Whether those hypotheses hold for this problem.
    pub(super) holds: Holds,
    /// What kind of evidence stands behind it.
    pub(super) status: Status,
    /// What it lets this run compute, bound, or rule out.
    pub(super) bearing: String,
    /// Claim ids this one contradicts.
    pub(super) contradicts: Vec<String>,
    /// The claims this one is a consequence of.
    ///
    /// The entailment edge, and the only field in the block that lets one
    /// claim carry another's standing. A claim written `follows-from: a, b`
    /// asserts that `a` and `b` together give it — so if both are established,
    /// this one is established too, and nobody has to prove it again.
    ///
    /// Deliberately not `implies`, which this block already spells and which
    /// means something looser: `bearing`/`implies` is prose about what the
    /// claim is *for*. This is a machine-readable edge between ids, and
    /// [`super::closure`] is what reads it.
    pub(super) follows_from: Vec<String>,
    /// Request ids this claim answers.
    ///
    /// How a stated gap closes. The note that fills it says so, so whether a
    /// request was met is read off the library rather than asserted by
    /// whoever went looking.
    pub(super) answers: Vec<String>,
    /// The TPTP problem whose refutation verdict backs a counterexample claim.
    ///
    /// Optional, unlike [`Claim::formalisation`], because most claims are not
    /// about a counterexample. When it *is* present it is checked the same way:
    /// a claim that names a refutation the engine did not produce is recorded
    /// as asserted, with the reason. A counterexample is the most consequential
    /// thing a run can get wrong in this direction — it does not merely fail to
    /// establish the goal, it says the goal is false.
    pub(super) refutation: String,
    /// The `.lean` file whose kernel verdict backs a formalised claim.
    ///
    /// Empty for every other status. It is a separate field rather than a
    /// convention on `anchor` because it is the only field in this struct that
    /// is *checked* against the workspace rather than recorded from the note:
    /// `anchor` says where in a paper to look, and nothing can tell whether it
    /// is true, while this names a file that either has a passing verdict or
    /// does not.
    pub(super) formalisation: String,
    /// Where in the source text to check it.
    pub(super) anchor: String,
    /// The note the block was found in.
    pub(super) source: String,
}

/// A claim block that could not be read, and why.
#[derive(Clone, Debug)]
struct Malformed {
    source: String,
    reason: &'static str,
}

/// A claim that called itself formalised and was not, and why.
///
/// Kept separate from [`Malformed`], which is about a block that could not be
/// *read*. This one read perfectly well and said something the workspace does
/// not support, which is a different accusation and asks for different work:
/// one wants the note fixed, the other wants the proof finished.
#[derive(Clone, Debug)]
struct Unbacked {
    id: String,
    source: String,
    objection: String,
}

/// What one derivation found across the whole library.
#[derive(Debug, Default)]
pub(super) struct Ledger {
    claims: Vec<Claim>,
    malformed: Vec<Malformed>,
    unbacked: Vec<Unbacked>,
}

/// The library's block format: a fenced block of `key: value` lines.
///
/// Borrowed rather than invented, in the same spirit as the patch envelope:
/// it is the front-matter shape a model has seen a thousand times, inside a
/// code fence so it survives every Markdown renderer and stays visibly
/// separate from the prose around it. Both the claim ledger and the thread
/// table read it, so an agent learns one format for the whole library.
///
/// Returns the body of each block opened by `` ```<fence> ``, and whether any
/// block was left unclosed.
pub(super) fn fenced<'a>(text: &'a str, fence: &str) -> (Vec<&'a str>, bool) {
    let opener = format!("```{fence}");
    let mut blocks = Vec::new();
    let mut rest = text;
    let mut unclosed = false;
    while let Some(open) = rest.find(&opener) {
        let after = &rest[open + opener.len()..];
        let Some(close) = after.find("```") else {
            unclosed = true;
            break;
        };
        blocks.push(&after[..close]);
        rest = &after[close + 3..];
    }
    (blocks, unclosed)
}

/// Reads one block's fields, in order.
///
/// A line with no key continues the previous value, so a statement may run to
/// several lines without being reformatted into one. Keys are lowercased and
/// underscores folded to hyphens, because a model asked for `holds-here`
/// writes `holds_here` about as often.
///
/// An indented line is always a continuation, whatever it contains. Naming a
/// curve mid-statement is ordinary mathematical prose — `E: y² = x(x² − c²)`
/// reads as a field called `e` on the word alone, and because [`set`] discards
/// a key it does not recognise, every line after it was discarded too. One live
/// claim lost its arithmetic-progression condition and its `2E(Q)` criterion
/// that way while still rendering as `proved`, which is the worst shape
/// available: the evidence is gone and the standing that rested on it is not.
pub(super) fn fields(block: &str) -> Vec<(String, String)> {
    let base = base_indent(block);
    let mut out: Vec<(String, String)> = Vec::new();
    for line in block.lines() {
        let trimmed = line.trim();
        if trimmed.is_empty() {
            continue;
        }
        let opens = indent(line) <= base;
        match trimmed.split_once(':') {
            // A key is one word, so a colon inside a statement does not open a
            // new field. `S(n): the skip count` would otherwise become a field
            // named after the function it defines.
            Some((key, value)) if opens && is_key(key) => out.push((
                key.trim().to_ascii_lowercase().replace('_', "-"),
                value.trim().to_string(),
            )),
            _ => {
                if let Some((_, value)) = out.last_mut() {
                    if !value.is_empty() {
                        value.push(' ');
                    }
                    value.push_str(trimmed);
                }
            }
        }
    }
    out
}

/// The column a block's field names start at.
///
/// Taken from the recognised keys rather than assumed to be zero, so a block
/// written with every line indented still parses. A block with no recognised
/// key falls back to the left margin, which is how one read before.
fn base_indent(block: &str) -> usize {
    block
        .lines()
        .filter(|line| {
            line.trim()
                .split_once(':')
                .is_some_and(|(key, _)| is_key(key) && is_known(key))
        })
        .map(indent)
        .min()
        .unwrap_or(0)
}

/// How far a line is indented, counting a tab as one column.
fn indent(line: &str) -> usize {
    line.len() - line.trim_start().len()
}

/// Whether a key names a field [`set`] acts on.
fn is_known(key: &str) -> bool {
    matches!(
        key.trim().to_ascii_lowercase().replace('_', "-").as_str(),
        "id" | "statement"
            | "hypotheses"
            | "hypothesis"
            | "holds-here"
            | "holds"
            | "status"
            | "evidence"
            | "bearing"
            | "implies"
            | "follows-from"
            | "derives-from"
            | "contradicts"
            | "answers"
            | "closes"
            | "formalisation"
            | "formalization"
            | "lean"
            | "refutation"
            | "counterexample"
            | "anchor"
            | "source"
            | "where"
    )
}

/// Splits a comma- or whitespace-separated list of identifiers.
///
/// Two rules beyond the split, and a live run wrote the sentence that needed
/// both. Asked for what its skeleton rests on, `reducer` answered
/// `rests-on: none (research/CLAIMS.md is empty; no claim in the ledger covers
/// this)` — which is a true, useful answer to the question and not a list. The
/// split turned it into eleven identifiers, and the statement graph dutifully
/// reported that the goal rested on `is`, on `the`, and on `covers`, none of
/// which exist. Eleven false faults are worse than none, because the report
/// that finds a genuine misspelling is the same report.
///
/// So: a field that opens by saying there is nothing lists nothing, whatever
/// follows; and a token that is not shaped like an identifier is dropped rather
/// than reported as missing. Both are deliberately narrow. A misspelled id is
/// still id-shaped and still reported, which is the case worth keeping.
pub(super) fn identifiers(value: &str) -> Vec<String> {
    // A parenthetical is a comment on the list, never a member of it, and the
    // words inside one are as id-shaped as anything else.
    let value = value.split('(').next().unwrap_or(value);
    let mut parts = value
        .split(|c: char| c == ',' || c.is_whitespace())
        .map(|id| id.trim_matches(['`', '[', ']']))
        .filter(|id| !id.is_empty());
    let Some(first) = parts.next() else {
        return Vec::new();
    };
    if matches!(
        first.trim_end_matches([':', '.', ';']).to_lowercase().as_str(),
        "none" | "no" | "nothing" | "n/a" | "na" | "tbd" | "-" | "—"
    ) {
        return Vec::new();
    }
    std::iter::once(first)
        .chain(parts)
        .filter(|id| is_identifier(id))
        .map(str::to_string)
        .collect()
}

/// Splits a list whose entries are not identifiers — URLs and citations.
///
/// The lenient split, kept for the fields that hold them. A URL is not
/// id-shaped and must not be filtered out for failing to be.
pub(super) fn references(value: &str) -> Vec<String> {
    value
        .split(|c: char| c == ',' || c.is_whitespace())
        .map(|id| id.trim_matches(['`', '[', ']']).to_string())
        .filter(|id| !id.is_empty())
        .collect()
}

/// Whether a token could be an identifier somebody wrote in a block.
///
/// Shape only. Whether it names anything is the derived ledger's question, and
/// answering it here would silence the misspelling report that is the reason
/// dangling edges are collected at all.
fn is_identifier(token: &str) -> bool {
    token.starts_with(|c: char| c.is_ascii_alphanumeric())
        && token
            .chars()
            .all(|c| c.is_ascii_alphanumeric() || matches!(c, '-' | '_' | '/' | '.'))
}

/// Reads every claim block in `text`, attributing each to `source`.
pub(super) fn parse(text: &str, source: &str) -> (Vec<Claim>, Vec<&'static str>) {
    let mut claims = Vec::new();
    let mut faults = Vec::new();
    let (blocks, unclosed) = fenced(text, "claim");
    if unclosed {
        faults.push("a claim block was never closed");
    }
    for block in blocks {
        let claim = read_block(block, source);
        if claim.id.is_empty() {
            faults.push("a claim block has no `id`, so nothing can refer to it");
        } else if claim.statement.is_empty() {
            faults.push("a claim block has no `statement`, so it claims nothing");
        } else {
            claims.push(claim);
        }
    }
    (claims, faults)
}

/// Reads one block's fields into a claim.
fn read_block(block: &str, source: &str) -> Claim {
    let mut claim = Claim {
        source: source.to_string(),
        ..Claim::default()
    };
    for (key, value) in fields(block) {
        set(&mut claim, &key, &value);
    }
    claim
}

/// Whether a colon-prefixed word is a field name rather than prose.
fn is_key(key: &str) -> bool {
    let key = key.trim();
    !key.is_empty()
        && key.len() <= 20
        && key
            .chars()
            .all(|c| c.is_ascii_alphabetic() || c == '-' || c == '_')
}

fn set(claim: &mut Claim, key: &str, value: &str) {
    match key {
        "id" => claim.id = value.trim().replace(['`', ' '], "-"),
        "statement" => claim.statement = value.to_string(),
        "hypotheses" | "hypothesis" => claim.hypotheses = value.to_string(),
        "holds-here" | "holds" => claim.holds = Holds::parse(value),
        "status" | "evidence" => claim.status = Status::parse(value),
        "bearing" | "implies" => claim.bearing = value.to_string(),
        "follows-from" | "derives-from" => claim.follows_from = identifiers(value),
        "contradicts" => claim.contradicts = identifiers(value),
        "answers" | "closes" => claim.answers = identifiers(value),
        "formalisation" | "formalization" | "lean" => {
            claim.formalisation = value.trim().replace(['`', ' '], "");
        }
        "refutation" | "counterexample" => {
            claim.refutation = value.trim().replace(['`', ' '], "");
        }
        "anchor" | "source" | "where" => claim.anchor = value.to_string(),
        _ => {}
    }
}

/// Derives the ledger from every note under `research/`.
///
/// Full texts are skipped: they are the untouched original, nothing may edit
/// them, and reading megabytes of converted paper to find blocks that cannot
/// be there is the one way this walk could become expensive.
/// `code/out/` is walked beside `research/`, and the asymmetry it removes is
/// the point. A claim could previously originate only in a note about a
/// *source*, so the run ledgered what it had read and forgot what it had
/// computed. Project Euler 597 sat at `proved=0` for a fourteen-check stretch
/// while holding `p(4,400) = 521/1020` — the value its problem statement
/// supplies, reproduced to all ten digits — and 38 exact points cross-validated
/// by two independent enumerators and Monte Carlo. Its own strongest evidence
/// was invisible to every role that reads the ledger, including the judge that
/// scored it 1/5.
///
/// The `Checked` status already meant "this run checked it numerically" and had
/// no way in. Now a program's output folder may carry `claim` blocks in a
/// Markdown note beside the data, on the same terms as any research note.
pub(super) fn collect(workspace: &Path) -> Ledger {
    let mut ledger = Ledger::default();
    let mut budget = MAX_FILES;
    for root in [
        workspace.join(super::documents::RESEARCH_DIR),
        workspace.join(super::layout::OUTPUT_DIR),
    ] {
        walk(workspace, &root, MAX_DEPTH, &mut budget, &mut ledger);
    }
    ledger.check_formalisations(workspace);
    ledger.claims.sort_by(|left, right| left.id.cmp(&right.id));
    ledger
}

fn walk(root: &Path, directory: &Path, depth: usize, budget: &mut usize, ledger: &mut Ledger) {
    if depth == 0 || *budget == 0 {
        return;
    }
    let Ok(entries) = std::fs::read_dir(directory) else {
        return;
    };
    let mut paths: Vec<std::path::PathBuf> = entries.flatten().map(|entry| entry.path()).collect();
    paths.sort();
    for path in paths {
        if *budget == 0 {
            return;
        }
        if path.is_dir() {
            walk(root, &path, depth - 1, budget, ledger);
            continue;
        }
        let name = path.file_name().unwrap_or_default().to_string_lossy();
        if !name.ends_with(".md")
            || name.ends_with(super::documents::FULL_TEXT_SUFFIX)
            || name == super::folder_index::INDEX_FILE
        {
            continue;
        }
        *budget -= 1;
        let Ok(text) = std::fs::read_to_string(&path) else {
            continue;
        };
        let relative = path
            .strip_prefix(root)
            .unwrap_or(&path)
            .to_string_lossy()
            .into_owned();
        let (claims, faults) = parse(&text, &relative);
        ledger.claims.extend(claims);
        ledger
            .malformed
            .extend(faults.into_iter().map(|reason| Malformed {
                source: relative.clone(),
                reason,
            }));
    }
}

impl Ledger {
    /// Drops every formalised claim the kernel does not actually back.
    ///
    /// This is the one place the ledger disbelieves a note, and it is worth
    /// being clear about why the check lives here rather than in the tool. The
    /// tool records what Lean said about a *file*; the claim is written later,
    /// in a different note, by a role that may name any file it likes. Nothing
    /// joins the two until the ledger is derived, so this is the join — and it
    /// runs on every derivation, so a claim whose Lean file is later edited
    /// into a `sorry` loses its standing on the next write rather than keeping
    /// a verdict it has outgrown.
    ///
    /// A failed check downgrades to [`Status::Asserted`] rather than dropping
    /// the claim. The statement may well be true and the run may well need it;
    /// what it has lost is the right to be called checked, and a claim that
    /// vanished would take its `bearing` and its hypotheses with it.
    fn check_formalisations(&mut self, workspace: &Path) {
        self.check_refutations(workspace);
        for claim in &mut self.claims {
            if claim.status != Status::Formalised {
                continue;
            }
            let objection = if claim.formalisation.is_empty() {
                Some(
                    "the claim names no `formalisation:` file, so there is nothing to check it \
                     against"
                        .to_string(),
                )
            } else {
                match super::lean::verdict(workspace, &claim.formalisation) {
                    None => Some(format!(
                        "no `lean_check` verdict exists for `{}`; run the kernel over it",
                        claim.formalisation
                    )),
                    Some(verdict) => verdict.objection(),
                }
            };
            if let Some(objection) = objection {
                claim.status = Status::Asserted;
                self.unbacked.push(Unbacked {
                    id: claim.id.clone(),
                    source: claim.source.clone(),
                    objection,
                });
            }
        }
    }

    /// Drops the standing of a claim naming a refutation the engine did not make.
    ///
    /// The same join the formalisation check performs, one engine over: the
    /// tool records what the model builder found about a *problem*, the claim
    /// is written later by a role that may name any problem it likes, and
    /// nothing connects the two until the ledger is derived.
    ///
    /// The asymmetry with formalisation is deliberate. A `formalisation:` line
    /// is *required* by `Status::Formalised`, because that status means nothing
    /// else; a `refutation:` line is optional, because a counterexample can
    /// perfectly well be established by hand and checked by a program. What is
    /// checked is only the claim that cites the engine — and citing it falsely
    /// is the worst case available here, since a refutation does not merely
    /// fail to establish the goal, it asserts the goal is false.
    fn check_refutations(&mut self, workspace: &Path) {
        for claim in &mut self.claims {
            if claim.refutation.is_empty() {
                continue;
            }
            let objection = match super::refute::verdict(workspace, &claim.refutation) {
                None => Some(format!(
                    "no `find_counterexample` verdict exists for `{}`",
                    claim.refutation
                )),
                Some(found) if !found.refuted() => Some(format!(
                    "`{}` was not refuted; the engine reported `{}`",
                    claim.refutation, found.status
                )),
                Some(_) => None,
            };
            if let Some(objection) = objection {
                claim.status = Status::Asserted;
                self.unbacked.push(Unbacked {
                    id: claim.id.clone(),
                    source: claim.source.clone(),
                    objection,
                });
            }
        }
    }

    /// How many claims this run established itself, by proof or by computation.
    ///
    /// A formalised claim counts, and by this point it has survived
    /// [`Ledger::check_formalisations`] — so unlike every other status here,
    /// the count is of something the runtime verified rather than of something
    /// a note asserted.
    pub(super) fn established(&self) -> usize {
        self.count(|status| {
            matches!(
                status,
                Status::Proved | Status::Formalised | Status::Checked
            )
        })
    }

    /// How many claims rest on a source's word alone.
    pub(super) fn asserted(&self) -> usize {
        self.count(|status| status == Status::Asserted)
    }

    /// How many claims were read out of a catalogue rather than derived.
    pub(super) fn catalogued(&self) -> usize {
        self.count(|status| status == Status::Catalogued)
    }

    fn count(&self, wanted: impl Fn(Status) -> bool) -> usize {
        self.claims
            .iter()
            .filter(|claim| wanted(claim.status))
            .count()
    }

    /// Renders the table routed into the roles that reason about the library.
    pub(super) fn render(&self) -> String {
        let mut out = String::from(
            "# Claims — what the library establishes, one row per claim\n\n\
             Derived from the `claim` blocks in the notes under `research/` and `code/out/`, and \
             rewritten whenever one of those notes is written. Do not edit this file; the next \
             write re-derives it. To add a claim, put a fenced `claim` block in the note that \
             establishes it, with `id`, `statement`, `hypotheses`, `holds-here`, `status`, \
             `bearing`, and `anchor` lines. A result this run *computed* belongs here as much as \
             one it read: write the note beside the output in `code/out/` and mark it \
             `status: checked`.\n\n\
             `status: formalised` is the one status this file does not take on trust. It means \
             the Lean kernel checked it *here*, so it needs a `formalisation:` line naming the \
             `.lean` file and a passing `lean_check` verdict for that file; without one the row \
             is recorded as `asserted` and listed below with the reason. Everything else on this \
             page is a word somebody typed.\n\n\
             `holds-here` is whether the hypotheses hold for *this* problem: a true theorem whose \
             hypotheses fail here is worse than no theorem, because it looks like progress.\n\n",
        );
        if self.claims.is_empty() {
            out.push_str("_No claims recorded yet._\n");
            self.append_faults(&mut out);
            return out;
        }
        out.push_str("| Claim | Statement | Holds here | Evidence | Note |\n| --- | --- | --- | --- | --- |\n");
        for claim in self.claims.iter().take(MAX_ROWS) {
            let _ = writeln!(
                out,
                "| `{}` | {} | {} | {} | `{}` |",
                claim.id,
                cell(&truncate(&claim.statement, STATEMENT_CHARS)),
                claim.holds.label(),
                claim.status.label(),
                claim.source
            );
        }
        if self.claims.len() > MAX_ROWS {
            let _ = writeln!(
                out,
                "\n_{} further claims not shown. A library with this many distinct claims is \
                 asking to be folded: seal what is settled so the table is the run's live \
                 beliefs rather than its whole history._",
                self.claims.len() - MAX_ROWS
            );
        }
        self.append_contradictions(&mut out);
        self.append_unbacked(&mut out);
        self.append_unverified(&mut out);
        self.append_catalogued(&mut out);
        self.append_faults(&mut out);
        out
    }

    /// Lists the claims that name another claim they contradict.
    ///
    /// The scholar prompt calls a source contradicting a standing belief the
    /// most valuable thing it can find, and until this existed nothing
    /// mechanically noticed one. A contradiction naming a claim that is not in
    /// the ledger is reported too: a belief nobody can locate is not resolved
    /// by leaving it unmentioned.
    fn append_contradictions(&self, out: &mut String) {
        let known: BTreeSet<&str> = self.claims.iter().map(|claim| claim.id.as_str()).collect();
        let pairs = self
            .claims
            .iter()
            .flat_map(|claim| claim.contradicts.iter().map(move |target| (claim, target)));
        let (rows, dropped) = budget::listed(pairs, budget::MAX_LISTED, |rows, (claim, target)| {
            let note = if known.contains(target.as_str()) {
                String::new()
            } else {
                " — _no claim of that id is on disk; either it was never written down or the \
                 id is misspelled_"
                    .to_string()
            };
            let _ = writeln!(
                rows,
                "- `{}` ({}) contradicts `{target}`{note}",
                claim.id, claim.source
            );
        });
        if rows.is_empty() {
            return;
        }
        out.push_str("\n## Contradictions\n\nResolve these before building on either side.\n\n");
        out.push_str(&rows);
        out.push_str(&budget::elided(dropped, NOTES_ROOT));
    }

    /// Lists claims that called themselves formalised and were downgraded.
    ///
    /// Reported rather than silently corrected, and placed above *Load-bearing
    /// but unverified* because it is the more specific accusation: those rows
    /// are claims nobody said were checked, and these are claims somebody said
    /// were checked and the kernel does not agree. A downgrade that showed up
    /// only as a changed word in the table would be indistinguishable from the
    /// role having written `asserted` in the first place, which is exactly the
    /// confusion this status exists to end.
    fn append_unbacked(&self, out: &mut String) {
        if self.unbacked.is_empty() {
            return;
        }
        out.push_str(
            "\n## Called formalised, not backed by the kernel\n\nEach of these was written as a \
             formalised claim and has been recorded as `asserted` instead, because no passing \
             `lean_check` verdict on disk supports it. Nothing here says the statement is false; \
             it says the workspace does not yet contain a proof of it. Run `lean_check` over the \
             file, fix what it reports, and the status returns on the next derivation.\n\n",
        );
        let (rows, dropped) = budget::listed(&self.unbacked, budget::MAX_LISTED, |rows, row| {
            let _ = writeln!(
                rows,
                "- `{}` ({}) — {}",
                row.id,
                row.source,
                truncate(&row.objection, budget::REASON_CHARS)
            );
        });
        out.push_str(&rows);
        out.push_str(&budget::elided(dropped, NOTES_ROOT));
    }

    /// Lists claims the run is leaning on without having verified them.
    fn append_unverified(&self, out: &mut String) {
        let unverified = self
            .claims
            .iter()
            .filter(|claim| claim.holds == Holds::Yes && claim.status == Status::Asserted);
        let (rows, dropped) = budget::listed(unverified, budget::MAX_LISTED, |rows, claim| {
            let _ = writeln!(
                rows,
                "- `{}` ({}) — asserted by the source, not proved there and not checked here",
                claim.id, claim.source
            );
        });
        if rows.is_empty() {
            return;
        }
        out.push_str(
            "\n## Load-bearing but unverified\n\nTaken to hold here on a source's word alone. \
             Verify by a second route, or say the result is unverified when reporting it. Search \
             the whole ledger with `search_claims`.\n\n",
        );
        out.push_str(&rows);
        out.push_str(&budget::elided(dropped, NOTES_ROOT));
    }

    /// Lists what the run read out of a catalogue rather than derived.
    ///
    /// Separate from *Load-bearing but unverified* because the two ask for
    /// different work. An asserted claim wants a second source or a proof; a
    /// catalogued one wants a program that reproduces the terms without reading
    /// the catalogue. Collapsing them loses that, and the distinction is the
    /// whole lesson of a run that reported a correct sum it had not computed.
    fn append_catalogued(&self, out: &mut String) {
        let catalogued = self
            .claims
            .iter()
            .filter(|claim| claim.status == Status::Catalogued);
        let (rows, dropped) = budget::listed(catalogued, budget::MAX_LISTED, |rows, claim| {
            let _ = writeln!(
                rows,
                "- `{}` ({}) — read from a catalogue; no derivation here reproduces it",
                claim.id, claim.source
            );
        });
        if rows.is_empty() {
            return;
        }
        out.push_str(
            "\n## Taken from a catalogue\n\nThese are lookups, not derivations. A catalogue is \
             good evidence that a result is right and no evidence at all about why, so one of \
             these may confirm a final answer and may never be the reason for it. Reproduce the \
             terms with a program that does not read the catalogue, then say so; until then, \
             report the result as looked up.\n\n",
        );
        out.push_str(&rows);
        out.push_str(&budget::elided(dropped, NOTES_ROOT));
    }

    /// Reports blocks that could not be read, rather than dropping them.
    ///
    /// A claim silently discarded for a missing `id` is worse than a visible
    /// gap: the note reads as though it recorded something, and nothing
    /// downstream can tell that it did not.
    fn append_faults(&self, out: &mut String) {
        if self.malformed.is_empty() {
            return;
        }
        out.push_str("\n## Blocks that could not be read\n\n");
        let (rows, dropped) = budget::listed(&self.malformed, budget::MAX_LISTED, |rows, fault| {
            let _ = writeln!(
                rows,
                "- `{}`: {}",
                fault.source,
                truncate(fault.reason, budget::REASON_CHARS)
            );
        });
        out.push_str(&rows);
        out.push_str(&budget::elided(dropped, NOTES_ROOT));
    }

    /// The request ids the library's claims say they answer.
    pub(super) fn answered(&self) -> std::collections::BTreeSet<String> {
        self.claims
            .iter()
            .flat_map(|claim| claim.answers.iter().cloned())
            .collect()
    }

    /// The ids of every claim on disk.
    ///
    /// Used to check that a thread rests on something the library actually
    /// establishes, rather than on a belief nobody wrote down.
    pub(super) fn ids(&self) -> std::collections::BTreeSet<String> {
        self.claims.iter().map(|claim| claim.id.clone()).collect()
    }

    /// Every claim on disk, for a reader that needs the whole graph.
    pub(super) fn all(&self) -> &[Claim] {
        &self.claims
    }

    /// Returns the claims matching `query`, best first.
    ///
    /// Ranked on term overlap across the statement, its hypotheses, and what
    /// it bears on, so a query naming an object finds the claims about that
    /// object rather than the notes that happen to mention it.
    pub(super) fn search(&self, query: &str) -> Vec<&Claim> {
        let terms: Vec<String> = query
            .split(|c: char| !c.is_alphanumeric())
            .filter(|word| word.len() > 2)
            .map(str::to_ascii_lowercase)
            .collect();
        let mut scored: Vec<(usize, &Claim)> = self
            .claims
            .iter()
            .map(|claim| {
                let haystack = format!(
                    "{} {} {} {} {}",
                    claim.id, claim.statement, claim.hypotheses, claim.bearing, claim.source
                )
                .to_ascii_lowercase();
                let score = terms
                    .iter()
                    .filter(|term| haystack.contains(term.as_str()))
                    .count();
                (score, claim)
            })
            .filter(|(score, _)| *score > 0)
            .collect();
        scored.sort_by(|left, right| right.0.cmp(&left.0).then(left.1.id.cmp(&right.1.id)));
        scored
            .into_iter()
            .take(MAX_RESULTS)
            .map(|(_, claim)| claim)
            .collect()
    }
}

/// Renders one claim in full, for a search result.
///
/// Everything a reader needs to decide whether to use it, and where to check
/// it, without opening the note.
pub(super) fn detail(claim: &Claim) -> String {
    let mut out = format!("### `{}`\n\n{}\n\n", claim.id, claim.statement);
    if !claim.hypotheses.is_empty() {
        let _ = writeln!(out, "- Hypotheses: {}", claim.hypotheses);
    }
    let _ = writeln!(
        out,
        "- Holds here: {} · Evidence: {}",
        claim.holds.label(),
        claim.status.label()
    );
    if !claim.bearing.is_empty() {
        let _ = writeln!(out, "- Bearing: {}", claim.bearing);
    }
    let _ = writeln!(out, "- Note: `{}`", claim.source);
    if !claim.anchor.is_empty() {
        let _ = writeln!(out, "- Check it at: {}", claim.anchor);
    }
    out
}

/// Whether a path names a Markdown file, however it is cased.
pub(super) fn is_markdown(relative: &str) -> bool {
    std::path::Path::new(relative)
        .extension()
        .is_some_and(|extension| extension.eq_ignore_ascii_case("md"))
}

/// Characters of statement one indexed claim keeps.
///
/// Wider than every other ledger's headline, and that asymmetry is the finding
/// rather than an inconsistency. An approach's index line exists to stop it
/// being re-proposed, and the id does most of that work — the refutation behind
/// it is elaboration. A claim's *statement* is not elaboration: it is the thing
/// a role has to read to know it does not need to prove it again. Indexing it
/// at a hundred and ten characters would leave a list of ids nobody can use.
const INDEXED_STATEMENT: usize = 240;

/// One line per claim: its id, its standing, and its statement.
pub(super) fn index(workspace: &Path) -> String {
    let ledger = collect(workspace);
    let rows: Vec<(String, String, String)> = ledger
        .claims
        .iter()
        .map(|claim| {
            (
                claim.id.clone(),
                format!("{}, {}", claim.status.label(), claim.holds.label()),
                claim.statement.clone(),
            )
        })
        .collect();
    super::ledger::index::render(
        "claims",
        "Claims",
        "What the library establishes, with how well and whether the hypotheses hold here. A \
         statement on this list does not need proving again — read it before you set out to \
         establish something.",
        rows.iter().map(|(id, status, headline)| super::ledger::index::Row {
            id,
            status,
            headline,
        }),
        INDEXED_STATEMENT,
    )
}

/// Re-derives the ledger from disk and rewrites [`CLAIMS_PATH`].
///
/// Called from the write path rather than left to a tool, for the same reason
/// placement is: a prompt asking an agent to keep a derived file current holds
/// only until a model is busy, and a ledger that disagrees with the notes is
/// worse than no ledger — the next reader trusts the row instead of opening
/// the note. Writing is best effort; a failed refresh must not fail the write
/// that succeeded.
pub(super) async fn refresh(documents: &super::documents::WorkspaceDocuments) -> Ledger {
    let ledger = collect(documents.root());
    let _ = documents.write_runtime(CLAIMS_PATH, &ledger.render()).await;
    // Described here at write time, because a derived file
    // nobody wrote by hand has no author to ask what it is for, and an index
    // row reading `_(undescribed)_` for the life of a run is worse than none.
    super::folder_index::record_description(
        documents,
        CLAIMS_PATH,
        "Derived: every claim block in the notes, one row each, with whether its hypotheses hold \
         here and what evidence stands behind it. Rewritten on every research write; do not edit.",
    )
    .await;
    ledger
}

/// Whether a written path is a note the ledger is derived from.
///
/// The trigger has to match what [`collect`] walks, or a claim enters the
/// library and the table does not show it until something unrelated is written.
/// That is worse than not collecting it at all: the note is on disk, the run
/// believes it recorded a result, and the ledger every other role reads
/// disagrees without saying so.
pub(super) fn is_note(relative: &str) -> bool {
    let research = format!("{}/", super::documents::RESEARCH_DIR);
    let computed = format!("{}/", super::layout::OUTPUT_DIR);
    (relative.starts_with(&research) || relative.starts_with(&computed))
        && is_markdown(relative)
        && !relative.ends_with(super::documents::FULL_TEXT_SUFFIX)
        && !relative.ends_with(CLAIMS_PATH)
        && !relative.ends_with("/INDEX.md")
        && !relative.ends_with("/ROOT.md")
}

fn cell(text: &str) -> String {
    if text.trim().is_empty() {
        return "—".to_string();
    }
    text.replace('|', "\\|").replace('\n', " ")
}

mod tool;

pub(super) use tool::ClaimsTool;

#[cfg(test)]
#[path = "claims_test.rs"]
mod test;
