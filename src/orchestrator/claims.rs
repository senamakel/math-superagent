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

/// The derived table, filed with the library it describes.
pub(super) const CLAIMS_PATH: &str = "research/CLAIMS.md";

/// Opening fence of a claim block.
const FENCE: &str = "```claim";

/// Rows the rendered table carries.
///
/// `CLAIMS.md` is routed into system prompts, so every model call in every
/// role that reads it pays for each row. A library with more claims than this
/// has a compression problem the summary tree exists to solve, and the table
/// says so rather than growing without limit.
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
    fn parse(value: &str) -> Self {
        match value.trim().to_ascii_lowercase().as_str() {
            "yes" | "true" | "holds" => Self::Yes,
            "no" | "false" => Self::No,
            _ => Self::Unchecked,
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
    /// This run checked it numerically.
    Checked,
    /// The source states it without proof, or cites elsewhere.
    #[default]
    Asserted,
    /// Suggestive rather than established.
    Heuristic,
}

impl Status {
    fn parse(value: &str) -> Self {
        let lowered = value.trim().to_ascii_lowercase();
        if lowered.starts_with("proved") || lowered.starts_with("proven") {
            Self::Proved
        } else if lowered.starts_with("checked") || lowered.starts_with("numeric") {
            Self::Checked
        } else if lowered.starts_with("heuristic") || lowered.starts_with("conject") {
            Self::Heuristic
        } else {
            Self::Asserted
        }
    }

    fn label(self) -> &'static str {
        match self {
            Self::Proved => "proved",
            Self::Checked => "checked",
            Self::Asserted => "asserted",
            Self::Heuristic => "heuristic",
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

/// What one derivation found across the whole library.
#[derive(Debug, Default)]
pub(super) struct Ledger {
    claims: Vec<Claim>,
    malformed: Vec<Malformed>,
}

/// Reads every claim block in `text`, attributing each to `source`.
pub(super) fn parse(text: &str, source: &str) -> (Vec<Claim>, Vec<&'static str>) {
    let mut claims = Vec::new();
    let mut faults = Vec::new();
    let mut rest = text;
    while let Some(open) = rest.find(FENCE) {
        let after = &rest[open + FENCE.len()..];
        let Some(close) = after.find("```") else {
            faults.push("a claim block was never closed");
            break;
        };
        let block = &after[..close];
        rest = &after[close + 3..];
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

/// Reads one block's `key: value` lines.
///
/// A line with no key continues the previous value, so a statement may run to
/// several lines without being reformatted into one.
fn read_block(block: &str, source: &str) -> Claim {
    let mut claim = Claim {
        source: source.to_string(),
        ..Claim::default()
    };
    let mut current = String::new();
    for line in block.lines() {
        let trimmed = line.trim();
        if trimmed.is_empty() {
            continue;
        }
        match trimmed.split_once(':') {
            // A key is one word, so a colon inside a statement does not open a
            // new field. `S(n): the skip count` would otherwise become a field
            // named after the function it defines.
            Some((key, value)) if is_key(key) => {
                current = key.trim().to_ascii_lowercase().replace('_', "-");
                set(&mut claim, &current, value.trim());
            }
            _ => append(&mut claim, &current, trimmed),
        }
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
        "contradicts" => {
            claim.contradicts = value
                .split(|c: char| c == ',' || c.is_whitespace())
                .map(|id| id.trim_matches(['`', '[', ']']).to_string())
                .filter(|id| !id.is_empty())
                .collect();
        }
        "anchor" | "source" | "where" => claim.anchor = value.to_string(),
        _ => {}
    }
}

fn append(claim: &mut Claim, key: &str, line: &str) {
    let target = match key {
        "statement" => &mut claim.statement,
        "hypotheses" | "hypothesis" => &mut claim.hypotheses,
        "bearing" | "implies" => &mut claim.bearing,
        _ => return,
    };
    if !target.is_empty() {
        target.push(' ');
    }
    target.push_str(line);
}

/// Derives the ledger from every note under `research/`.
///
/// Full texts are skipped: they are the untouched original, nothing may edit
/// them, and reading megabytes of converted paper to find blocks that cannot
/// be there is the one way this walk could become expensive.
pub(super) fn collect(workspace: &Path) -> Ledger {
    let mut ledger = Ledger::default();
    let mut budget = MAX_FILES;
    walk(
        workspace,
        &workspace.join(super::documents::RESEARCH_DIR),
        MAX_DEPTH,
        &mut budget,
        &mut ledger,
    );
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
        ledger.malformed.extend(faults.into_iter().map(|reason| {
            Malformed {
                source: relative.clone(),
                reason,
            }
        }));
    }
}

impl Ledger {
    /// Renders the table routed into the roles that reason about the library.
    pub(super) fn render(&self) -> String {
        let mut out = String::from(
            "# Claims — what the library establishes, one row per claim\n\n\
             Derived from the `claim` blocks in the notes under `research/`, and rewritten \
             whenever one of those notes is written. Do not edit this file; the next write \
             re-derives it. To add a claim, put a fenced `claim` block in the note that \
             establishes it, with `id`, `statement`, `hypotheses`, `holds-here`, `status`, \
             `bearing`, and `anchor` lines.\n\n\
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
        self.append_unverified(&mut out);
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
        let mut rows = String::new();
        for claim in &self.claims {
            for target in &claim.contradicts {
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
            }
        }
        if rows.is_empty() {
            return;
        }
        out.push_str("\n## Contradictions\n\nResolve these before building on either side.\n\n");
        out.push_str(&rows);
    }

    /// Lists claims the run is leaning on without having verified them.
    fn append_unverified(&self, out: &mut String) {
        let mut rows = String::new();
        for claim in self
            .claims
            .iter()
            .filter(|claim| claim.holds == Holds::Yes && claim.status == Status::Asserted)
        {
            let _ = writeln!(
                rows,
                "- `{}` ({}) — asserted by the source, not proved there and not checked here",
                claim.id, claim.source
            );
        }
        if rows.is_empty() {
            return;
        }
        out.push_str(
            "\n## Load-bearing but unverified\n\nTaken to hold here on a source's word alone. \
             Verify by a second route, or say the result is unverified when reporting it.\n\n",
        );
        out.push_str(&rows);
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
        for fault in &self.malformed {
            let _ = writeln!(out, "- `{}`: {}", fault.source, fault.reason);
        }
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
        scored.sort_by(|left, right| {
            right
                .0
                .cmp(&left.0)
                .then(left.1.id.cmp(&right.1.id))
        });
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
    let _ = documents
        .write_runtime(CLAIMS_PATH, &ledger.render())
        .await;
    ledger
}

/// Whether a written path is a note the ledger is derived from.
pub(super) fn is_note(relative: &str) -> bool {
    relative.starts_with(&format!("{}/", super::documents::RESEARCH_DIR))
        && relative.ends_with(".md")
        && !relative.ends_with(super::documents::FULL_TEXT_SUFFIX)
        && !relative.ends_with(CLAIMS_PATH)
}

fn cell(text: &str) -> String {
    if text.trim().is_empty() {
        return "—".to_string();
    }
    text.replace('|', "\\|").replace('\n', " ")
}

fn truncate(text: &str, limit: usize) -> String {
    let text = text.trim();
    if text.chars().count() <= limit {
        return text.to_string();
    }
    let head: String = text.chars().take(limit).collect();
    let head = head
        .rsplit_once(char::is_whitespace)
        .map_or(head.as_str(), |(body, _)| body);
    format!("{}…", head.trim_end())
}

mod tool;

pub(super) use tool::ClaimsTool;

#[cfg(test)]
mod test;
