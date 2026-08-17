//! Lemmas: the run's Lean tree, read as a library rather than as a folder of
//! source files.
//!
//! Every other ledger here is derived from prose somebody typed. This one is
//! derived from Lean, and that is the whole reason it exists. A research
//! library is mostly statements — this object is defined so, this theorem holds
//! under these hypotheses, this follows from that — and prose is a bad
//! container for them on both counts that matter to a run. It is *loose*: the
//! hypotheses of a summarised theorem are the thing that goes missing, and
//! `research/CLAIMS.md` already carries a `holds-here` column because a true
//! theorem whose hypotheses fail here is worse than no theorem. And it is
//! *large*: one workspace's `research/` tree is 202 markdown files and 2.8 MB,
//! every paragraph of which is tokens a role pays for and cannot verify.
//!
//! A Lean declaration has neither problem. Its hypotheses are in the type, so
//! they cannot be dropped in the retelling; and a signature is a line where a
//! summary is a page. So the run writes the mathematics as Lean under
//! `code/lean/`, and this module renders the signatures back out as an index —
//! what the library knows, one line each, with what the kernel said about it.
//!
//! **What the status here means, and what it does not.** The status is read off
//! the filed `lean_check` verdict for the file a declaration lives in, so it is
//! a fact about a whole file and not about one theorem in it. That is coarse
//! and deliberately so: Lean reports a compile failure per file, and a
//! declaration that elaborated inside a file that did not compile is not
//! something this run should be leaning on. `unchecked` means no verdict exists
//! — the file was written and the kernel was never run over it, which is the
//! state worth making visible, because a `.lean` file nobody checked reads
//! exactly like one that passed.
//!
//! **Why the whole `code/lean/` tree and not just `Lib/`.** The prompt asks the
//! role to put settled work under `code/lean/Lib/` and keep probes beside it,
//! and that convention is worth having. It is not worth *enforcing here* by
//! hiding everything else: a verified lemma in a file called `probe_gcd.lean`
//! is still a verified lemma, and an index that omitted it would send the next
//! role to prove it again. The tree is walked whole and the path is rendered,
//! so a reader can see which half of the convention a declaration is on.

use std::fmt::Write as _;
use std::path::Path;

use super::ledger::budget;
use super::text::truncate;

/// The folder the Lean tree lives under.
pub(super) const LEAN_DIR: &str = "code/lean";

/// The derived index, filed with the library it describes.
pub(super) const LEMMAS_PATH: &str = "derived/LEMMAS.md";

/// Declarations one table lists.
///
/// Larger than the other ledgers' bounds because a row here is a signature
/// rather than a paragraph, so the same number of rows costs a fraction of the
/// tokens — and because the failure this file prevents is a role re-proving
/// something, which gets more likely the more the run has proved.
const MAX_ROWS: usize = 80;

/// Characters one rendered signature is held to.
const SIGNATURE_CHARS: usize = 180;

/// Characters one rendered provenance line is held to.
const SOURCE_CHARS: usize = 90;

/// The declaration keywords this module recognises.
///
/// `example` is deliberately absent: it is anonymous, so it cannot be cited,
/// referred to, or re-used, and indexing one would put a row in the table that
/// a reader has no way to act on.
const KEYWORDS: [&str; 8] = [
    "theorem",
    "lemma",
    "def",
    "abbrev",
    "axiom",
    "structure",
    "inductive",
    "instance",
];

/// Modifiers that may precede a declaration keyword.
const MODIFIERS: [&str; 6] = [
    "private",
    "protected",
    "noncomputable",
    "partial",
    "unsafe",
    "scoped",
];

/// Where a declaration's file stands with the kernel.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub(super) enum Standing {
    /// The kernel checked the file, resting on Lean's own axioms alone.
    Verified,
    /// The kernel checked the file *given* results cited from the literature.
    Conditional,
    /// The file has a verdict and it does not pass.
    Failed,
    /// No verdict exists: the kernel was never run over this file.
    Unchecked,
}

impl Standing {
    fn label(self) -> &'static str {
        match self {
            Self::Verified => "verified",
            Self::Conditional => "conditional",
            Self::Failed => "failed",
            Self::Unchecked => "unchecked",
        }
    }
}

/// One Lean declaration, as a reader of the index needs it.
#[derive(Clone, Debug)]
pub(super) struct Declaration {
    /// The fully qualified name, namespace included.
    pub(super) name: String,
    /// `theorem`, `def`, `axiom`, and so on.
    pub(super) kind: String,
    /// Everything between the name and the proof: binders and the statement.
    pub(super) signature: String,
    /// The workspace-relative file it is in.
    pub(super) file: String,
    /// The `src:` line from its docstring, when it has one.
    pub(super) source: String,
    /// Where its file stands with the kernel.
    pub(super) standing: Standing,
}

/// Every declaration in the workspace's Lean tree.
#[derive(Debug, Default)]
pub(super) struct Lemmas {
    declarations: Vec<Declaration>,
    /// Files under [`LEAN_DIR`] that no `lean_check` verdict covers.
    unchecked_files: Vec<String>,
}

/// Walks `code/lean/` and reads every declaration out of it.
pub(super) fn collect(workspace: &Path) -> Lemmas {
    let mut lemmas = Lemmas::default();
    let root = workspace.join(LEAN_DIR);
    let mut sources: Vec<std::path::PathBuf> = Vec::new();
    walk(&root, &mut sources);
    sources.sort();
    for path in sources {
        let Ok(text) = std::fs::read_to_string(&path) else {
            continue;
        };
        let Some(relative) = path
            .strip_prefix(workspace)
            .ok()
            .and_then(|relative| relative.to_str())
        else {
            continue;
        };
        let relative = relative.replace('\\', "/");
        let standing = match super::lean::verdict(workspace, &relative) {
            None => {
                lemmas.unchecked_files.push(relative.clone());
                Standing::Unchecked
            }
            Some(verdict) => match verdict.outcome() {
                super::lean::Outcome::Verified => Standing::Verified,
                super::lean::Outcome::Conditional => Standing::Conditional,
                super::lean::Outcome::Failed => Standing::Failed,
            },
        };
        for mut declaration in declarations(&text) {
            declaration.file.clone_from(&relative);
            declaration.standing = standing;
            lemmas.declarations.push(declaration);
        }
    }
    lemmas
}

/// Collects every `.lean` file below `root`, depth first.
fn walk(root: &Path, found: &mut Vec<std::path::PathBuf>) {
    let Ok(entries) = std::fs::read_dir(root) else {
        return;
    };
    for entry in entries.flatten() {
        let path = entry.path();
        // Hidden folders are the checkpoint history and the build tree, and
        // neither holds a declaration a reader would cite.
        if path
            .file_name()
            .and_then(std::ffi::OsStr::to_str)
            .is_some_and(|name| name.starts_with('.'))
        {
            continue;
        }
        if path.is_dir() {
            walk(&path, found);
        } else if path.extension().is_some_and(|extension| extension == "lean") {
            found.push(path);
        }
    }
}

/// Reads the declarations out of one Lean source.
///
/// A header-level parse, and it is worth being exact about what that means,
/// because the alternative reads better on paper. Lean can be asked what a file
/// declares — but only by elaborating it, which is a Mathlib import and tens of
/// seconds per file, against an index that has to be re-derived every time a
/// verdict is filed. So this reads the text.
///
/// It therefore fails in both directions and only one of them is acceptable. It
/// **misses** a declaration whose keyword is not at the start of a line, or
/// whose name is written in a way this does not expect; the row is then absent
/// from the index, and absent is what the index already means for a file nobody
/// has written yet. It must never **invent** one, or report a name that is not
/// in the file, because a role reading a signature it cannot then `exact?`
/// against is worse off than one reading nothing. Every rule below is on the
/// conservative side of that line.
fn declarations(text: &str) -> Vec<Declaration> {
    let mut found = Vec::new();
    let mut namespaces: Vec<String> = Vec::new();
    let mut docstring = String::new();
    let mut in_docstring = false;
    for line in text.lines() {
        let trimmed = line.trim();

        // A docstring is carried to the declaration it precedes, which is where
        // the provenance lives: `/-- src: arXiv:2307.05997 §4 Cor 8 -/` is one
        // line of Lean standing in for the paragraph of prose a summary would
        // have been.
        if in_docstring {
            if let Some(source) = source_line(trimmed) {
                docstring = source;
            }
            if trimmed.ends_with("-/") {
                in_docstring = false;
            }
            continue;
        }
        if trimmed.starts_with("/--") {
            if let Some(source) = source_line(trimmed) {
                docstring = source;
            }
            in_docstring = !trimmed.ends_with("-/");
            continue;
        }

        if let Some(rest) = trimmed.strip_prefix("namespace ") {
            if let Some(name) = rest.split_whitespace().next() {
                namespaces.push(name.to_string());
            }
            continue;
        }
        if trimmed == "end" || trimmed.starts_with("end ") {
            namespaces.pop();
            continue;
        }

        let Some((kind, rest)) = keyword(trimmed) else {
            // Only a blank line clears a pending docstring. A comment or an
            // attribute between the docstring and its declaration is ordinary
            // Lean, and dropping the provenance on one would lose exactly the
            // line this whole convention exists to carry.
            if trimmed.is_empty() {
                docstring.clear();
            }
            continue;
        };
        let Some((name, signature)) = split_name(rest) else {
            continue;
        };
        let qualified = if namespaces.is_empty() {
            name
        } else {
            format!("{}.{name}", namespaces.join("."))
        };
        found.push(Declaration {
            name: qualified,
            kind: kind.to_string(),
            signature,
            file: String::new(),
            source: std::mem::take(&mut docstring),
            standing: Standing::Unchecked,
        });
    }
    found
}

/// The `src:` provenance out of a docstring line, if it carries one.
fn source_line(line: &str) -> Option<String> {
    let start = line.to_ascii_lowercase().find("src:")?;
    let rest = line[start + "src:".len()..]
        .trim_end_matches("-/")
        .trim()
        .to_string();
    (!rest.is_empty()).then_some(rest)
}

/// Splits a line into its declaration keyword and what follows, skipping any
/// modifiers in front of it.
///
/// Only at the start of a line, and that is the conservative choice: `def` also
/// appears inside `Nat.rec`-style prose, inside strings, and inside a `where`
/// block indented under something else, and indexing those would put names in
/// the table that no `exact?` will resolve.
fn keyword(line: &str) -> Option<(&'static str, &str)> {
    let mut rest = line;
    // Attributes precede the modifiers: `@[simp] theorem foo`.
    if rest.starts_with("@[")
        && let Some(close) = rest.find(']')
    {
        rest = rest[close + 1..].trim_start();
    }
    loop {
        let stripped = MODIFIERS.iter().find_map(|modifier| {
            rest.strip_prefix(modifier)
                .filter(|after| after.starts_with(' '))
        });
        match stripped {
            Some(after) => rest = after.trim_start(),
            None => break,
        }
    }
    KEYWORDS.iter().find_map(|keyword| {
        rest.strip_prefix(keyword)
            .filter(|after| after.starts_with(' ') || after.starts_with('\n'))
            .map(|after| (*keyword, after.trim_start()))
    })
}

/// Splits `foo (n : Nat) : n = n := by rfl` into its name and its signature.
fn split_name(rest: &str) -> Option<(String, String)> {
    let name: String = rest
        .chars()
        .take_while(|character| {
            character.is_alphanumeric() || "_'.!?«»".contains(*character) || *character == '_'
        })
        .collect();
    if name.is_empty() {
        return None;
    }
    let signature = rest[name.len()..]
        .split(":=")
        .next()
        .unwrap_or_default()
        .split_whitespace()
        .collect::<Vec<_>>()
        .join(" ");
    Some((name, signature))
}

impl Lemmas {
    /// How many declarations the kernel has checked, on either footing.
    pub(super) fn checked(&self) -> usize {
        self.declarations
            .iter()
            .filter(|declaration| {
                matches!(
                    declaration.standing,
                    Standing::Verified | Standing::Conditional
                )
            })
            .count()
    }

    /// Renders the index routed into the roles that reason about the library.
    ///
    /// Verified declarations first, then conditional, then everything else —
    /// so the bound, when it bites, drops the rows a reader can least act on
    /// rather than whichever ones happened to sort last.
    pub(super) fn render(&self) -> String {
        let mut out = String::from(
            "# Lemmas — what the run has stated in Lean, one row per declaration\n\n\
             Derived by walking `code/lean/`. Do not edit this file; the next `lean_check` \
             re-derives it. This is the library's *statements*: a Lean signature carries its \
             hypotheses in its type, so unlike a prose summary it cannot quietly lose one, and \
             it costs a line where a summary costs a page.\n\n\
             **Read this before proving anything.** A declaration on this list with a `verified` \
             standing has been checked by the kernel in this workspace and does not need proving \
             again — `exact?` against it, or import the file. Search here before you search \
             Mathlib, and search Mathlib before you prove.\n\n\
             The standing is a fact about the *file*, not about the one declaration: Lean fails a \
             file, not a theorem. `verified` is the kernel resting on its own three axioms; \
             `conditional` is the kernel resting additionally on results cited from the \
             literature under `namespace Cited`, so the implication is proved and the hypothesis \
             is somebody's paper; `unchecked` means the file exists and the kernel was never run \
             over it, which reads exactly like a passing file and is not one.\n\n",
        );
        if self.declarations.is_empty() {
            out.push_str("_Nothing stated in Lean yet._\n");
            return out;
        }

        let mut ordered: Vec<&Declaration> = self.declarations.iter().collect();
        ordered.sort_by_key(|declaration| {
            (
                match declaration.standing {
                    Standing::Verified => 0,
                    Standing::Conditional => 1,
                    Standing::Unchecked => 2,
                    Standing::Failed => 3,
                },
                declaration.file.clone(),
                declaration.name.clone(),
            )
        });

        out.push_str(
            "| Declaration | Kind | Standing | Statement | Source | File |\n\
             | --- | --- | --- | --- | --- | --- |\n",
        );
        let (body, dropped) = budget::listed(ordered, MAX_ROWS, |body, declaration| {
            let _ = writeln!(
                body,
                "| `{}` | {} | {} | {} | {} | `{}` |",
                declaration.name,
                declaration.kind,
                declaration.standing.label(),
                cell(&truncate(&declaration.signature, SIGNATURE_CHARS)),
                cell(&truncate(&declaration.source, SOURCE_CHARS)),
                declaration.file
            );
        });
        out.push_str(&body);
        out.push_str(&budget::elided(dropped, LEAN_DIR));

        let _ = write!(
            out,
            "\n{} declarations, {} of them in a file the kernel has checked.\n",
            self.declarations.len(),
            self.checked()
        );

        if !self.unchecked_files.is_empty() {
            out.push_str(
                "\n## Never checked\n\nThese files are in the tree and no `lean_check` verdict \
                 exists for them. Nothing on this page from one of them is evidence of \
                 anything.\n\n",
            );
            let (listed, more) =
                budget::listed(&self.unchecked_files, budget::MAX_LISTED, |body, file| {
                    let _ = writeln!(body, "- `{file}`");
                });
            out.push_str(&listed);
            out.push_str(&budget::elided(more, LEAN_DIR));
        }
        out
    }
}

/// Re-derives the index from disk and rewrites [`LEMMAS_PATH`].
///
/// Triggered by a `lean_check`, and that is the right trigger rather than a
/// convenient one. Half of every row here — the standing — *is* a verdict, so
/// re-deriving when a `.lean` file is written would produce a table that says
/// `unchecked` about work the kernel had just accepted. Writing is best effort,
/// as every other refresh is: a failed derivation must not fail the check that
/// succeeded.
pub(super) async fn refresh(documents: &super::documents::WorkspaceDocuments) {
    let lemmas = collect(documents.root());
    let _ = documents
        .write_runtime(LEMMAS_PATH, &lemmas.render())
        .await;
    super::folder_index::record_description(
        documents,
        LEMMAS_PATH,
        "Derived: every Lean declaration in `code/lean/`, one row each, with what the kernel said \
         about the file it is in. Rewritten on every `lean_check`; do not edit.",
    )
    .await;
}

fn cell(text: &str) -> String {
    if text.trim().is_empty() {
        return "—".to_string();
    }
    text.replace('|', "\\|").replace('\n', " ")
}

#[cfg(test)]
#[path = "lemmas_test.rs"]
mod test;

/// The declarations in `source` whose statement is `X = X`.
///
/// A tautology is the one wrong statement a kernel check cannot object to, and
/// it is the wrong statement a Lean-first mandate invites. Live evidence: a run
/// told the answer was not accepted until a `.lean` file with a passing verdict
/// carried it produced, under a docstring reading *the answer stated directly
/// as an equality of naturals*,
///
/// ```text
/// theorem pe622_answer_nat : 3010983666182123972 = 3010983666182123972 := by rfl
/// ```
///
/// It compiles, carries no `sorry`, needs no axiom beyond Lean's own, and says
/// nothing whatever about Project Euler 622 — so every check in `lean.rs` would
/// have passed it as `verified`, the strongest status this runtime has, and the
/// claim ledger would have carried the answer on it.
///
/// The test is deliberately the narrowest one that catches it: the two sides of
/// the top-level `=` are *textually identical*. That is never informative and is
/// always safe to refuse. It is not a general triviality check and cannot be —
/// `2 + 2 = 4 := by rfl` is a real fact and must keep passing, which it does,
/// because its sides differ. What this cannot catch is a statement that is
/// merely *beside the point*, and nothing mechanical can; that is what
/// `lean_prover.md` asks the role to say in prose and what `holds-here` is for.
/// Whether a declaration's proposition is literally `True`.
///
/// `True` is inhabited by definition, so asserting it says nothing whatever —
/// the same category of never-informative-and-always-safe-to-refuse as the
/// identical-sides check below, and caught for the same reason.
///
/// It is the shape a model reaches for when it has been asked to state
/// something it cannot express. Ten statements milled out of Conway-99's
/// summaries produced six of exactly `axiom <name> : True`, each with a
/// docstring above it describing the theorem it was standing in for. Without
/// this they fail for an incidental reason — the verdict finds no declarations
/// to report — and nothing tells the caller the file was empty rather than
/// wrong.
///
/// Deliberately textual and narrow. A statement that merely *reduces* to `True`
/// is not caught and cannot be; this refuses the one spelling that is always a
/// placeholder.
fn is_vacuous(signature: &str) -> bool {
    let Some((_, proposition)) = signature.rsplit_once(':') else {
        return false;
    };
    proposition.trim() == "True"
}

pub(super) fn tautologies(source: &str) -> Vec<String> {
    let mut found = Vec::new();
    for declaration in declarations(source) {
        // An `axiom` asserts, so it is judged like a theorem here even though
        // it carries no proof. A file whose whole content is
        // `axiom foo : True` is the mill's commonest bad output and states
        // nothing at all — see `is_vacuous`.
        if !matches!(
            declaration.kind.as_str(),
            "theorem" | "lemma" | "axiom"
        ) {
            continue;
        }
        if is_vacuous(&declaration.signature) {
            found.push(declaration.name);
            continue;
        }
        // Only a theorem or lemma makes an equational claim. A `def` of the
        // form `x = x` is a definition of a proposition, not an assertion.
        if declaration.kind == "axiom" {
            continue;
        }
        // Everything after the last top-level `:` is the proposition. Binders
        // may contain `:` too, so the *last* one is taken, which is right for
        // the shape this catches and gives up harmlessly on anything ornate.
        let Some((_, proposition)) = declaration.signature.rsplit_once(':') else {
            continue;
        };
        let Some((left, right)) = proposition.split_once('=') else {
            continue;
        };
        // `≠`, `≤`, `≥` and `:=` all contain or neighbour `=`; a split that
        // caught one of those would report a real statement as a tautology,
        // which is the only way this check could do harm.
        if left.ends_with(['≠', '≤', '≥', '<', '>', '!', ':'])
            || right.starts_with('=')
            || left.trim().is_empty()
        {
            continue;
        }
        if left.trim() == right.trim() && !left.trim().is_empty() {
            found.push(declaration.name);
        }
    }
    found
}
