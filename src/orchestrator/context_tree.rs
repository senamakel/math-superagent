//! A bounded summary tree over the workspace's markdown.
//!
//! The run's standing context grows without limit and is re-sent on every
//! model call in nine roles, so the question is never *whether* to compress it
//! but how to compress it without losing what was compressed away. A flat
//! rewrite loses it: each pass drops what the previous pass judged less
//! important, nothing records what was dropped, and by the tenth pass the file
//! is confident about things no longer traceable to a source.
//!
//! So compression is a tree rather than a rewrite, laid out on disk:
//!
//! ```text
//! research/            reflections/
//! ├── INDEX.md         ├── INDEX.md      the root — what it all now means
//! ├── L0/              ├── L0/           originals, never edited
//! ├── L1/              ├── L1/           one note per original
//! └── L2/              └── L2/           one note per ten notes below
//! ```
//!
//! `L0` is the untouched original: the complete converted document, or the
//! reflection the loop wrote. Every level above it holds one note per
//! [`FANOUT`] notes below, each capped at [`NODE_TOKENS`], and a new level
//! appears only when the level under it outgrows one node. `INDEX.md` is the
//! root, and the only file a reader is expected to open first.
//!
//! Every node links to the notes beneath it with Obsidian wikilinks, so the
//! workspace opens as a vault and a fold is safe to write: what it leaves out
//! is one link down, not gone. That is the whole point of the shape — a claim
//! nobody can trace to a source is worth less than no claim.
//!
//! This module holds no state and writes nothing. It reads the workspace,
//! works out which node is over budget, unfolded, or behind its children, and
//! says so — the fold itself is a judgement about meaning, so an agent writes
//! it. What is not left to judgement is whether a node is within budget and
//! whether it reflects what is under it; those are measured on disk, because
//! an instruction asking for a few hundred words produced a 6.8 KB file inside
//! an hour.
//!
//! Structure is recovered from the links themselves rather than from a sidecar
//! manifest. A fold that has stopped linking a note has stopped covering it,
//! which is exactly the fact a manifest would hide.

use std::fmt::Write as _;
use std::fs;
use std::path::Path;
use std::time::SystemTime;

use super::folder_index::INDEX_FILE;

/// Notes one fold node may cover.
pub(super) const FANOUT: usize = 10;

/// Tokens any node above `L0` may occupy.
///
/// A thousand tokens is what a role can afford to be handed on every one of
/// its model calls. It caps each *node*, not the tree: the tree grows by
/// adding levels, and a reader pays for one path down it rather than all of
/// it.
pub(super) const NODE_TOKENS: u64 = 1_000;

/// Characters charged to one token, matching the harness estimator.
const CHARS_PER_TOKEN: u64 = 4;

/// Notes that must have changed before a parent is refolded.
///
/// A refold costs a model call, and one new note rarely changes what a fold
/// says. Refolding on every write would also starve acquisition outright: the
/// research team would spend every cycle restating a library it never got
/// round to extending.
const STALE_CHILDREN: usize = 3;

/// Folders carrying a tree, each with its own `INDEX.md` root.
const ROOTS: [&str; 2] = ["research", "reflections"];

/// The run-wide standing brief, a root in its own right.
const CONTEXT_FILE: &str = "context.md";

/// Deepest level the planner will look for.
///
/// Ten levels at a fan-out of ten is more notes than a run can produce, so the
/// bound exists only to keep the scan finite.
const MAX_LEVEL: usize = 10;

/// One node of the tree as it currently stands on disk.
#[derive(Clone, Debug, PartialEq, Eq)]
pub(super) struct Node {
    /// Path relative to the workspace root.
    pub(super) path: String,
    /// Estimated tokens the node currently occupies.
    pub(super) tokens: u64,
    /// Paths this node is responsible for covering.
    pub(super) children: Vec<String>,
}

/// What is wrong with a node, in the order the tree wants it fixed.
#[derive(Clone, Debug, PartialEq, Eq)]
pub(super) enum Fault {
    /// The node costs more than a node may spend.
    OverBudget,
    /// More notes sit at this level than one node may cover.
    Unfolded(String),
    /// Notes have changed since the node was last written.
    Stale(Vec<String>),
}

/// A node and the one thing wrong with it.
#[derive(Clone, Debug, PartialEq, Eq)]
pub(super) struct Task {
    /// The node needing work.
    pub(super) node: Node,
    /// Why it needs work.
    pub(super) fault: Fault,
}

/// The folder holding one level of a tree.
fn level_dir(root: &str, level: usize) -> String {
    format!("{root}/L{level}")
}

/// Estimated tokens held by a file, or zero when it cannot be read.
fn tokens(workspace: &Path, relative: &str) -> u64 {
    fs::metadata(workspace.join(relative)).map_or(0, |meta| meta.len() / CHARS_PER_TOKEN)
}

/// Last write time of a file, or `None` when it does not exist.
fn modified(workspace: &Path, relative: &str) -> Option<SystemTime> {
    fs::metadata(workspace.join(relative)).ok()?.modified().ok()
}

/// Markdown notes directly inside a workspace-relative folder, sorted.
///
/// The index is not one of them: it is the root of the tree, never a note in
/// a level of it.
fn notes(workspace: &Path, folder: &str) -> Vec<String> {
    let Ok(entries) = fs::read_dir(workspace.join(folder)) else {
        return Vec::new();
    };
    let mut found: Vec<String> = entries
        .flatten()
        .filter(|entry| entry.file_type().is_ok_and(|kind| kind.is_file()))
        .map(|entry| entry.file_name().to_string_lossy().into_owned())
        .filter(|name| {
            Path::new(name)
                .extension()
                .is_some_and(|extension| extension.eq_ignore_ascii_case("md"))
                && name != INDEX_FILE
        })
        .map(|name| format!("{folder}/{name}"))
        .collect();
    found.sort();
    found
}

/// Link targets a note points at, as written.
///
/// Both spellings count. Obsidian wikilinks are what the vault is built from,
/// and a plain markdown link is what a model reaches for when it forgets; a
/// planner that recognised only one of them would report a fold as covering
/// nothing on the strength of its punctuation.
fn links(text: &str) -> Vec<String> {
    let mut found = Vec::new();
    let mut push = |target: &str| {
        let target = target.trim().trim_start_matches("./");
        if !target.is_empty() && !target.contains("://") && !found.iter().any(|seen| seen == target)
        {
            found.push(target.to_string());
        }
    };
    for tail in text.split("[[").skip(1) {
        if let Some((target, _)) = tail.split_once("]]") {
            // `[[note|shown as this]]` and `[[note#heading]]` both name `note`.
            let target = target.split(['|', '#']).next().unwrap_or_default();
            push(target);
        }
    }
    for tail in text.split("](").skip(1) {
        if let Some((target, _)) = tail.split_once(')') {
            push(target.split_whitespace().next().unwrap_or_default());
        }
    }
    found
}

/// Resolves a link target against the folder holding the file that wrote it.
///
/// `..` is popped here rather than left to the filesystem, because a fold in
/// `research/L2/` naturally links a note as `../L1/paper.md`, and a path still
/// carrying that segment matches nothing against the relative paths the rest
/// of this module works in.
fn resolve(folder: &str, target: &str) -> String {
    let mut parts: Vec<&str> = folder.split('/').filter(|part| !part.is_empty()).collect();
    for part in target.split('/') {
        match part {
            "" | "." => {}
            ".." => {
                parts.pop();
            }
            part => parts.push(part),
        }
    }
    parts.join("/")
}

/// The notes a node links, resolved against the folder holding it.
///
/// A wikilink carries a bare note name and Obsidian resolves it anywhere in
/// the vault, so a target that does not exist beside the node is searched for
/// among `candidates` before being discarded.
fn linked_children(workspace: &Path, node: &str, candidates: &[String]) -> Vec<String> {
    let folder = node.rsplit_once('/').map_or("", |(folder, _)| folder);
    let Ok(text) = fs::read_to_string(workspace.join(node)) else {
        return Vec::new();
    };
    let mut found = Vec::new();
    for target in links(&text) {
        let beside = resolve(folder, &target);
        let resolved = if workspace.join(&beside).is_file() {
            Some(beside)
        } else {
            let name = target.rsplit('/').next().unwrap_or(&target);
            let name = if name.ends_with(".md") {
                name.to_string()
            } else {
                format!("{name}.md")
            };
            candidates
                .iter()
                .find(|candidate| candidate.ends_with(&format!("/{name}")))
                .cloned()
        };
        if let Some(resolved) = resolved
            && !found.contains(&resolved)
        {
            found.push(resolved);
        }
    }
    found
}

/// Notes written since the parent was.
fn changed_since(workspace: &Path, parent: &str, children: &[String]) -> Vec<String> {
    let Some(sealed) = modified(workspace, parent) else {
        // A parent that does not exist yet is behind every note it should
        // cover, which is the strongest form of the same fault.
        return children.to_vec();
    };
    children
        .iter()
        .filter(|child| modified(workspace, child).is_some_and(|at| at > sealed))
        .cloned()
        .collect()
}

/// The levels of one tree, shallowest first, with the notes at each.
///
/// A flat folder counts as `L1`. Every workspace started flat and several are
/// running now; a planner that saw only `L1/` would report a library of
/// thirteen sources as empty and quietly stop maintaining it.
fn levels(workspace: &Path, root: &str) -> Vec<(usize, Vec<String>)> {
    let mut found = Vec::new();
    let flat = notes(workspace, root);
    if !flat.is_empty() {
        found.push((1, flat));
    }
    for level in 0..=MAX_LEVEL {
        let at = notes(workspace, &level_dir(root, level));
        if at.is_empty() {
            continue;
        }
        match found.iter_mut().find(|(existing, _)| *existing == level) {
            Some((_, notes)) => notes.extend(at),
            None => found.push((level, at)),
        }
    }
    found.sort_by_key(|(level, _)| *level);
    found
}

/// Works out what the trees need, highest priority first.
///
/// Budget comes before structure and structure before freshness: a node over
/// budget charges every model call in every role that reads it, an outgrown
/// level cannot be brought under budget without first being split, and a node
/// merely behind its children is still true as far as it goes.
pub(super) fn plan(workspace: &Path) -> Vec<Task> {
    let mut over_budget = Vec::new();
    let mut unfolded = Vec::new();
    let mut stale = Vec::new();

    let context = Node {
        path: CONTEXT_FILE.to_string(),
        tokens: tokens(workspace, CONTEXT_FILE),
        children: ROOTS
            .iter()
            .map(|root| format!("{root}/{INDEX_FILE}"))
            .filter(|index| workspace.join(index).is_file())
            .collect(),
    };
    let mut nodes = vec![context];

    for root in ROOTS {
        let levels = levels(workspace, root);
        let Some((top, top_notes)) = levels.last() else {
            continue;
        };
        // The index folds the highest level present; everything below is
        // reached through it.
        nodes.push(Node {
            path: format!("{root}/{INDEX_FILE}"),
            tokens: tokens(workspace, &format!("{root}/{INDEX_FILE}")),
            children: top_notes.clone(),
        });
        if top_notes.len() > FANOUT {
            unfolded.push(Task {
                node: Node {
                    path: level_dir(root, *top),
                    tokens: 0,
                    children: top_notes.clone(),
                },
                fault: Fault::Unfolded(level_dir(root, top + 1)),
            });
        }
        // `L0` holds originals: never rewritten, never folded, exempt from the
        // cap that every level above it is held to.
        for (level, at) in levels.iter().filter(|(level, _)| *level > 0) {
            let below = levels
                .iter()
                .filter(|(under, _)| under < level)
                .next_back()
                .map(|(_, notes)| notes.clone())
                .unwrap_or_default();
            for note in at {
                nodes.push(Node {
                    path: note.clone(),
                    tokens: tokens(workspace, note),
                    children: linked_children(workspace, note, &below),
                });
            }
        }
    }

    for node in &nodes {
        if node.tokens > NODE_TOKENS {
            over_budget.push(Task {
                node: node.clone(),
                fault: Fault::OverBudget,
            });
        }
        if node.children.is_empty() {
            // Nothing under it: unstarted rather than stale, and asking for a
            // fold of no notes produces invention.
            continue;
        }
        let changed = changed_since(workspace, &node.path, &node.children);
        if changed.len() >= STALE_CHILDREN || (!changed.is_empty() && node.tokens == 0) {
            stale.push(Task {
                node: node.clone(),
                fault: Fault::Stale(changed),
            });
        }
    }

    over_budget.extend(unfolded);
    over_budget.extend(stale);
    over_budget
}

/// Renders the highest-priority task as an instruction, if there is one.
///
/// One task per cycle. Handing over the whole plan invites a cycle that
/// rewrites every level at once, and folding a level that is itself about to
/// be rewritten is work thrown away.
pub(super) fn briefing(workspace: &Path) -> Option<String> {
    let task = plan(workspace).into_iter().next()?;
    let node = &task.node;
    let mut out = String::from(
        "Before anything else, this cycle's job is the summary tree. `L0/` holds \
         originals and is never edited; each level above it holds one note per ten \
         notes below, capped at ",
    );
    let _ = write!(
        out,
        "{NODE_TOKENS} tokens, and `INDEX.md` is the root. Link what a note covers \
         with Obsidian wikilinks — `[[note-name]]` — so what a fold leaves out stays \
         one step away instead of being lost.\n\n"
    );
    match &task.fault {
        Fault::OverBudget => {
            let _ = write!(
                out,
                "`{}` is about {} tokens, over the {NODE_TOKENS}-token cap, and is \
                 re-sent on every model call in every role that reads it. Rewrite it \
                 under the cap this cycle: merge notes that say the same thing, drop \
                 what later work has settled, and keep the statements and their \
                 consequences rather than the narrative. Whatever you cut, leave a \
                 wikilink to the note that still holds it — that is what makes the cut \
                 safe. Gather nothing new until it fits.",
                node.path, node.tokens,
            );
        }
        Fault::Unfolded(next) => {
            let needed = node.children.len().div_ceil(FANOUT);
            let _ = write!(
                out,
                "`{}` now holds {} notes, more than the {FANOUT} one node may cover. \
                 Group them by subject into {needed} fold notes under `{next}/`, named \
                 for the subject each covers. Every fold says what its notes together \
                 establish, stays under {NODE_TOKENS} tokens, and wikilinks each note \
                 it covers. Then rewrite the index above them as a fold of those, \
                 linking each. The notes are:\n{}",
                node.path,
                node.children.len(),
                list(&node.children),
            );
        }
        Fault::Stale(changed) => {
            let _ = write!(
                out,
                "`{}` has not been rewritten since {} of the notes below it changed. \
                 Refold it so it says what they now establish, under {NODE_TOKENS} \
                 tokens, wikilinking each note it covers. Changed:\n{}",
                node.path,
                changed.len(),
                list(changed),
            );
        }
    }
    Some(out)
}

/// Renders paths as a markdown list.
fn list(paths: &[String]) -> String {
    paths
        .iter()
        .map(|path| format!("- `{path}`"))
        .collect::<Vec<_>>()
        .join("\n")
}

#[cfg(test)]
mod test;
