//! Turning a paper or a research note into checked Lean.
//!
//! The solution loop formalises what its own statement graph ranks, which is
//! the right thing when a graph exists. Across `workspace/` most of the time it
//! does not: 33 of 45 workspaces hold no Lean at all, four of seventeen
//! conjecture workspaces have a `derived/LEMMAS.md`, and Conway-99 — which does
//! have a graph — carries 246 research files against 16 Lean ones. The library
//! trails the reading by roughly forty to one.
//!
//! Nothing in that gap is a decomposition problem. It is that a run has read a
//! paper, written down what the paper establishes, and never turned any of it
//! into something the kernel can check. So this walks the other way round: from
//! prose the run already has, or a paper named on the command line, to
//! statements, to files, to verdicts.
//!
//! # Why it is not the verification arm
//!
//! The arm asks "what does the most rest on", and needs a graph to answer.
//! This asks "what did this source claim", and needs only the source. They meet
//! at the kernel and nowhere else, which is why this takes no blueprint and
//! writes no attempt records: a mill run must work on a workspace that has
//! never had a decomposition, or it is inert exactly where the Lean is missing.
//!
//! # What lands
//!
//! Only what compiled. A candidate whose file the kernel rejects is reported
//! and dropped, because a `.lean` file that does not compile sitting in the
//! library is worse than an absent one — `derived/LEMMAS.md` re-derives from
//! the sources, and a failed file becomes a row that reads like work.
//!
//! A result taken *from the literature* rather than proved here is an `axiom`
//! under `namespace Cited`, and earns `conditional` rather than `formalised`.
//! That status is read off the verdict as everywhere else, never typed.

use std::fmt::Write as _;
use std::path::{Path, PathBuf};

use super::async_subagents::AsyncSubagentManager;

/// Where the mill writes, relative to the workspace.
///
/// The library rather than `code/lean/` directly, because these statements are
/// not one run's working files: they are what the run knows, stated so the
/// kernel agrees, and the next run should find them as a library rather than as
/// somebody's scratch.
pub(super) const LIB_DIR: &str = "code/lean/Lib";

/// Where the scribe may hunt for a Mathlib name.
///
/// A directory of its own so that hunting leaves nothing in the library. The
/// scribe holds no search tool — `#check` in a file is the only way it has to
/// find out whether a name exists — and on a live Casas-Alvero run 17 of 26
/// kernel verdicts were `test_*` probe files it had written into
/// `code/lean/Lib/`. Naming the place for them is cheaper than forbidding them,
/// because the need is real.
///
/// Swept at the end of a mill run: it is scratch by construction, and a probe
/// nobody deleted reads to the next run exactly like a statement.
pub(super) const PROBE_DIR: &str = "code/lean/probe";

/// How many candidates one mill run formalises by default.
///
/// The rate limit is the real bound — the scribe tier admits roughly 0.63
/// requests a second, so a hundred candidates with a repair loop each is a
/// long-running job rather than a quick one — and this keeps a default
/// invocation to something a person will wait for. `--budget` moves it.
pub(super) const DEFAULT_BUDGET: usize = 25;

/// Where a mill run reads its statements from.
#[derive(Clone, Debug, PartialEq, Eq)]
pub(super) enum Source {
    /// A file or directory already in the workspace.
    Workspace(PathBuf),
    /// A paper to fetch, by URL.
    Url(String),
    /// A paper to fetch, by arXiv id.
    Arxiv(String),
}

impl Source {
    /// Reads a source from the spelling a caller used.
    ///
    /// One parser, so `--from` and `--paper` are two words for the same
    /// argument rather than two code paths that will drift. An `arxiv:` prefix
    /// or a bare arXiv id is recognised before the URL check, because
    /// `arxiv.org/abs/2401.00001` and `2401.00001` should not reach the
    /// librarian as different requests.
    pub(super) fn parse(raw: &str) -> Option<Self> {
        let raw = raw.trim();
        if raw.is_empty() {
            return None;
        }
        if let Some(id) = raw.strip_prefix("arxiv:") {
            let id = id.trim();
            return (!id.is_empty()).then(|| Self::Arxiv(id.to_string()));
        }
        if is_arxiv_id(raw) {
            return Some(Self::Arxiv(raw.to_string()));
        }
        if raw.starts_with("http://") || raw.starts_with("https://") {
            return Some(Self::Url(raw.to_string()));
        }
        Some(Self::Workspace(PathBuf::from(raw)))
    }
}

/// Whether `raw` is a bare arXiv identifier, such as `2401.00001v2`.
fn is_arxiv_id(raw: &str) -> bool {
    let Some((head, tail)) = raw.split_once('.') else {
        return false;
    };
    if head.len() != 4 || !head.chars().all(|c| c.is_ascii_digit()) {
        return false;
    }
    let digits = tail.trim_end_matches(|c: char| c == 'v' || c.is_ascii_digit());
    let number = tail.trim_start_matches(|c: char| c.is_ascii_digit());
    digits.is_empty()
        && tail.chars().next().is_some_and(|c| c.is_ascii_digit())
        && (number.is_empty() || number.starts_with('v'))
}

/// One statement the mill will try to state and check.
#[derive(Clone, Debug, PartialEq, Eq)]
pub(super) struct Candidate {
    /// A Lean-safe name, which becomes the file name and the declaration's.
    pub(super) name: String,
    /// The statement in prose, as the source put it.
    pub(super) statement: String,
    /// Where it came from, carried through to the file as a comment.
    ///
    /// Not decoration. A `Cited` axiom whose provenance is lost is an
    /// unfalsifiable assumption in the library, and the difference between that
    /// and a citation is this string.
    pub(super) provenance: String,
    /// Whether the source *proves* this or merely states it.
    ///
    /// A statement the source proves is something this run may try to prove
    /// too. One it only asserts — a result quoted from elsewhere — becomes a
    /// `Cited` axiom, and must never come back as `formalised`.
    pub(super) cited: bool,
}

impl Candidate {
    /// The workspace-relative file this candidate is written into.
    pub(super) fn source_path(&self) -> String {
        format!("{LIB_DIR}/{}.lean", self.name)
    }

    /// The brief handed to the scribe.
    ///
    /// Everything the scribe needs and nothing else: it holds no workspace
    /// context by design, so what is not in here does not reach it. See
    /// `orchestrator::tiers` for why that role is small.
    pub(super) fn briefing(&self) -> String {
        let kind = if self.cited {
            "This is quoted from the literature and is NOT to be proved here. State it as an \
             `axiom` inside `namespace Cited`, with the citation above it as a comment. Do not \
             write a proof, and do not add a `#print axioms` line for it."
        } else {
            "The source proves this. State it as a `theorem` and prove it, with a `#print axioms` \
             line for the theorem."
        };
        format!(
            "Formalise one statement in Lean 4 against Mathlib.\n\n\
             Write it into `{}` and call `lean_check` on that file.\n\n\
             {kind}\n\n\
             Name the declaration `{}`.\n\n\
             Source: {}\n\n\
             Statement:\n{}",
            self.source_path(),
            self.name,
            self.provenance,
            self.statement
        )
    }
}

/// Folds a name into the Lean-safe, file-safe set.
///
/// The same fold `verify::source_for` uses, for the same reason: the mill has
/// to find the file again to read its verdict, and a name the model chose is a
/// name the model has to reproduce. Leading digits are prefixed rather than
/// dropped, because `2_adic_bound` is not a Lean identifier and silently
/// becoming `adic_bound` would collide with a different lemma.
pub(super) fn safe_name(raw: &str) -> Option<String> {
    let folded: String = raw
        .trim()
        .chars()
        .map(|character| {
            if character.is_ascii_alphanumeric() {
                character.to_ascii_lowercase()
            } else {
                '_'
            }
        })
        .collect();
    let folded = folded.trim_matches('_').to_string();
    if folded.is_empty() {
        return None;
    }
    if folded.starts_with(|c: char| c.is_ascii_digit()) {
        return Some(format!("lemma_{folded}"));
    }
    Some(folded)
}

/// Reads the candidates out of the extractor's reply.
///
/// The reply is one JSON array. Anything that is not an object with a usable
/// `name` and `statement` is skipped rather than failing the run: an extractor
/// that returns nine good rows and one malformed one should mill the nine.
///
/// Deduplicated by name, because two sections of one paper stating the same
/// lemma is ordinary and two candidates writing one file is not — the second
/// would overwrite the first and both would report success.
pub(super) fn parse_candidates(reply: &str) -> Vec<Candidate> {
    let Some(array) = extract_array(reply) else {
        return Vec::new();
    };
    let Ok(values) = serde_json::from_str::<Vec<serde_json::Value>>(&array) else {
        return Vec::new();
    };
    let mut seen: Vec<String> = Vec::new();
    let mut candidates = Vec::new();
    for value in values {
        let Some(statement) = value.get("statement").and_then(serde_json::Value::as_str) else {
            continue;
        };
        let statement = statement.trim();
        if statement.is_empty() {
            continue;
        }
        let Some(name) = value
            .get("name")
            .and_then(serde_json::Value::as_str)
            .and_then(safe_name)
        else {
            continue;
        };
        if seen.contains(&name) {
            continue;
        }
        seen.push(name.clone());
        candidates.push(Candidate {
            name,
            statement: statement.to_string(),
            provenance: value
                .get("source")
                .and_then(serde_json::Value::as_str)
                .unwrap_or("unattributed")
                .trim()
                .to_string(),
            cited: value
                .get("cited")
                .and_then(serde_json::Value::as_bool)
                .unwrap_or(false),
        });
    }
    candidates
}

/// The first top-level JSON array in `reply`.
///
/// Models fence their JSON, preface it, or both. Scanning for the brackets is
/// what makes the extractor's prompt a request rather than a contract the run
/// breaks on.
fn extract_array(reply: &str) -> Option<String> {
    let start = reply.find('[')?;
    let mut depth = 0usize;
    let mut in_string = false;
    let mut escaped = false;
    for (offset, character) in reply[start..].char_indices() {
        if in_string {
            match character {
                _ if escaped => escaped = false,
                '\\' => escaped = true,
                '"' => in_string = false,
                _ => {}
            }
            continue;
        }
        match character {
            '"' => in_string = true,
            '[' => depth += 1,
            ']' => {
                depth -= 1;
                if depth == 0 {
                    return Some(reply[start..=start + offset].to_string());
                }
            }
            _ => {}
        }
    }
    None
}

/// The prose a mill run reads, gathered from one workspace path.
///
/// A file is itself; a directory is every Markdown file directly inside it, in
/// name order so two runs over one directory read it the same way. Bounded, so
/// a directory of two hundred notes does not become one prompt.
pub(super) fn gather(
    workspace: &Path,
    relative: &Path,
    max_bytes: usize,
) -> (Vec<(String, String)>, usize) {
    let root = workspace.join(relative);
    let mut sources = Vec::new();
    if root.is_file() {
        if let Ok(text) = std::fs::read_to_string(&root) {
            sources.push((relative.display().to_string(), text));
        }
        return (sources, 0);
    }
    let Ok(entries) = std::fs::read_dir(&root) else {
        return (sources, 0);
    };
    let mut paths: Vec<PathBuf> = entries
        .filter_map(std::result::Result::ok)
        .map(|entry| entry.path())
        .filter(|path| path.extension().is_some_and(|ext| ext == "md"))
        .collect();
    paths.sort();
    let mut spent = 0usize;
    let mut unread = 0usize;
    for path in paths {
        let Ok(text) = std::fs::read_to_string(&path) else {
            unread += 1;
            continue;
        };
        // Counted rather than broken out of. A directory whose first file is
        // enormous and whose rest are small would otherwise report every one of
        // them as unread, when only the one did not fit.
        if spent + text.len() > max_bytes {
            unread += 1;
            continue;
        }
        spent += text.len();
        let label = path
            .strip_prefix(workspace)
            .unwrap_or(&path)
            .display()
            .to_string();
        sources.push((label, text));
    }
    (sources, unread)
}

/// What one mill run did.
#[derive(Clone, Debug, Default, PartialEq, Eq)]
pub(super) struct Report {
    /// Candidates whose file the kernel accepted outright.
    pub(super) landed: Vec<String>,
    /// Candidates whose file compiles and states something, with gaps.
    ///
    /// Kept rather than dropped, and reported apart from `landed` because the
    /// difference matters: these are statements, not results. A live run on
    /// Casas-Alvero produced this — a faithful statement of the conjecture over
    /// `ℂ` in Mathlib's own vocabulary, compiling, whose only defect was the
    /// `sorry` nobody on earth can currently remove. Deleting that was the
    /// mill throwing away its best output.
    pub(super) stated: Vec<String>,
    /// Candidates whose file the kernel rejected, and were therefore dropped.
    pub(super) rejected: Vec<String>,
    /// Candidates found but not attempted, because the budget ran out.
    pub(super) skipped: usize,
    /// Source files that did not fit the read bound and were never seen.
    ///
    /// Separate from `skipped`, because they are different failures with
    /// different fixes: a skipped candidate was read and not attempted, and an
    /// unread file might hold the best statement in the directory. A mill run
    /// that read half a directory and said only what it milled reads exactly
    /// like one that read all of it.
    pub(super) unread: usize,
}

impl Report {
    /// The run, rendered for a person reading a terminal.
    ///
    /// States what was left out. A mill run that milled 25 of 60 candidates and
    /// said only what landed reads as a complete pass over the source, which is
    /// the reporting failure this repository keeps writing controls against.
    pub(super) fn render(&self) -> String {
        let mut out = format!(
            "milled {} statement(s): {} verified, {} stated with gaps, {} rejected",
            self.landed.len() + self.stated.len() + self.rejected.len(),
            self.landed.len(),
            self.stated.len(),
            self.rejected.len()
        );
        if !self.landed.is_empty() {
            let _ = write!(out, "\n\nlanded in {LIB_DIR}/:");
            for name in &self.landed {
                let _ = write!(out, "\n  {name}.lean");
            }
        }
        if !self.stated.is_empty() {
            let _ = write!(
                out,
                "\n\nstated in {LIB_DIR}/, compiling, with gaps left as `sorry`. These are \
                 statements rather than results and back no claim — but a faithful statement of \
                 an open problem is what a decomposition starts from:"
            );
            for name in &self.stated {
                let _ = write!(out, "\n  {name}.lean");
            }
        }
        if !self.rejected.is_empty() {
            let _ = write!(
                out,
                "\n\ndropped and removed, because a file the kernel rejects is worse in the \
                 library than an absent one:"
            );
            for name in &self.rejected {
                let _ = write!(out, "\n  {name}");
            }
        }
        if self.unread > 0 {
            let _ = write!(
                out,
                "\n\n{} source file(s) were not read at all: the directory is larger than one \
                 prompt. Mill a narrower path to reach them.",
                self.unread
            );
        }
        if self.skipped > 0 {
            let _ = write!(
                out,
                "\n\n{} further candidate(s) were found and not attempted: the budget was spent. \
                 Raise it with --budget.",
                self.skipped
            );
        }
        out
    }
}

/// What the extractor is asked for.
///
/// JSON rather than prose, because the next step is a loop and not a reader.
/// The `cited` flag is the field that matters: it decides whether a statement
/// becomes a theorem this run must prove or an axiom it may only quote, and a
/// model that marks everything `false` produces a library of unprovable
/// obligations while one that marks everything `true` produces a library of
/// assumptions. The prompt therefore says what the distinction is rather than
/// naming the field and hoping.
fn extraction_brief(sources: &[(String, String)]) -> String {
    let mut brief = String::from(
        "Read the material below and list the mathematical statements in it that could be stated \
         in Lean 4 against Mathlib.\n\n\
         Answer with one JSON array and nothing else. Each element:\n\
         - `name`: a short identifier, lowercase words separated by underscores\n\
         - `statement`: the statement itself, self-contained, with every hypothesis it needs\n\
         - `source`: where it came from — the file, and the theorem number if there is one\n\
         - `cited`: `false` if the material *proves* it, `true` if the material merely quotes or \
           asserts it from somewhere else\n\n\
         `cited` is the field to get right. A statement the material proves is one this run may \
         prove too. One it only asserts becomes an axiom, and an axiom recorded as a theorem is a \
         false record.\n\n\
         Prefer statements that are self-contained and precisely stated. Skip anything whose \
         meaning depends on notation the material sets up and you cannot restate. An empty array \
         is a good answer when there is nothing crisp enough.\n",
    );
    for (label, text) in sources {
        let _ = write!(brief, "\n\n## {label}\n{text}");
    }
    brief
}

/// Runs one mill: source in, checked Lean out.
///
/// The steps are separate delegations on purpose. Extraction wants a model that
/// reads prose and holds a whole paper; formalisation wants one that writes Lean
/// quickly and cheaply, and gets a fresh child per statement so a candidate that
/// goes badly cannot spend the next one's turns. See `orchestrator::tiers`.
pub(super) async fn run(
    subagents: &AsyncSubagentManager,
    workspace: &Path,
    sources: Vec<(String, String)>,
    unread: usize,
    budget: usize,
) -> Report {
    let mut report = Report {
        unread,
        ..Report::default()
    };
    if sources.is_empty() {
        return report;
    }
    let Ok(reply) = subagents
        .run_to_completion("scholar", extraction_brief(&sources))
        .await
    else {
        return report;
    };
    let mut candidates = parse_candidates(&reply);
    if candidates.len() > budget {
        report.skipped = candidates.len() - budget;
        candidates.truncate(budget);
    }
    for candidate in candidates {
        // One child per statement, and its outcome is read off the kernel
        // rather than off what the child said about itself. A scribe reporting
        // success is a claim; the verdict on disk is the record.
        let _ = subagents
            .run_to_completion(super::lean::SCRIBE_ROLE, candidate.briefing())
            .await;
        let source = candidate.source_path();
        let verdict = super::lean::verdict(workspace, &source);
        if verdict.as_ref().is_some_and(super::lean::Verdict::verified) {
            report.landed.push(candidate.name);
            continue;
        }
        // Kept, but never counted as verified. See `Verdict::states_something`.
        if verdict
            .as_ref()
            .is_some_and(super::lean::Verdict::states_something)
        {
            report.stated.push(candidate.name);
            continue;
        }
        // Removed, not merely left unreported. The library is read by later
        // runs and re-derived into `derived/LEMMAS.md`, so a file the kernel
        // refused is worse sitting there than absent: it becomes a row that
        // reads like work. A live run made this concrete — the scribe uses
        // `#check` probes to find Mathlib names, and sixteen probe files
        // reached `code/lean/Lib/` on one pass of ten statements.
        //
        // A failure to remove is not a failure of the mill: the file is
        // already recorded as rejected, and the verdict beside it says why.
        let _ = std::fs::remove_file(workspace.join(&source));
        report.rejected.push(candidate.name);
    }
    // Scratch by construction; see `PROBE_DIR`. Swept whole rather than
    // per-file, and failures ignored, because a probe left behind is untidy
    // and a mill run that failed over one would be worse.
    let _ = std::fs::remove_dir_all(workspace.join(PROBE_DIR));
    report
}

#[cfg(test)]
#[path = "mill_test.rs"]
mod test;
