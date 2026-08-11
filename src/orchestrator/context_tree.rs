//! A bounded summary tree over the workspace's markdown.
//!
//! The run's standing context grows without limit and is re-sent on every
//! model call in nine roles, so the question is never *whether* to compress it
//! but how to compress it without losing what was compressed away. A flat
//! rewrite loses it: each pass drops what the previous pass judged less
//! important, nothing records what was dropped, and by the tenth pass the file
//! is confident about things no longer traceable to a source.
//!
//! So compression is a tree rather than a rewrite. Level 0 is the untouched
//! original — `research/<name>.full.md`, the complete converted document,
//! never edited. Level 1 is one digest per source, `research/<name>.md`,
//! linking down to its own full text. Level 2 folds up to [`FANOUT`] digests
//! into `research/folds/<topic>.md`, linking to each. The root is
//! `research/INDEX.md`, which folds the level below it. Every level is capped
//! at [`NODE_TOKENS`], and every node links to its children, so a reader who
//! needs the detail a fold left out walks down to it instead of being told it
//! never existed.
//!
//! This module holds no state and writes nothing. It reads the workspace,
//! works out which node is over budget or behind its children, and says so —
//! the fold itself is a judgement about meaning, so the research team writes
//! it. What is not left to judgement is whether a node is within budget and
//! whether it reflects its children; those are measured on disk, because an
//! instruction in a prompt asking for a few hundred words produced a 6.8 KB
//! file inside an hour.
//!
//! The structure is recovered from the links themselves rather than from a
//! sidecar manifest. A fold that has stopped linking a source has stopped
//! covering it, which is exactly the fact a manifest would hide.

use std::fmt::Write as _;
use std::fs;
use std::path::Path;
use std::time::SystemTime;

use super::folder_index::INDEX_FILE;

/// Children one fold node may cover.
pub(super) const FANOUT: usize = 10;

/// Tokens a fold node or a root may occupy.
///
/// A thousand tokens is what a role can afford to be handed on every one of
/// its model calls. It is a ceiling on each *node*, not on the tree: the tree
/// grows by adding levels, and the reader pays for one path down it rather
/// than for all of it.
pub(super) const NODE_TOKENS: u64 = 1_000;

/// Characters charged to one token, matching the harness estimator.
const CHARS_PER_TOKEN: u64 = 4;

/// Children that must have changed before a parent is refolded.
///
/// A refold costs a model call, and one new digest rarely changes what a fold
/// says. Refolding on every write would also starve acquisition outright: the
/// research team would spend every cycle restating a library it never got
/// round to extending.
const STALE_CHILDREN: usize = 3;

/// The folder every downloaded document is filed under.
const RESEARCH_DIR: &str = "research";

/// The folder holding intermediate fold nodes.
const FOLD_DIR: &str = "folds";

/// The run-wide standing brief, the one tree root outside `research/`.
const CONTEXT_FILE: &str = "context.md";

/// Suffix marking a level-0 original, which is never folded or rewritten.
const FULL_SUFFIX: &str = ".full.md";

/// One node of the tree as it currently exists on disk.
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
    /// The node costs more than its level may spend.
    OverBudget,
    /// The level has more children than one node may cover.
    Unfolded,
    /// Children have changed since the node was last written.
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

/// Estimated tokens held by a file, or zero when it cannot be read.
fn tokens(path: &Path) -> u64 {
    fs::metadata(path).map_or(0, |meta| meta.len() / CHARS_PER_TOKEN)
}

/// Last write time of a file, or `None` when it does not exist.
fn modified(path: &Path) -> Option<SystemTime> {
    fs::metadata(path).ok()?.modified().ok()
}

/// Markdown files directly inside `folder`, excluding indexes and originals.
///
/// Sorted, so a plan does not depend on directory order and a test can assert
/// one.
fn digests(folder: &Path) -> Vec<String> {
    let Ok(entries) = fs::read_dir(folder) else {
        return Vec::new();
    };
    let mut found: Vec<String> = entries
        .flatten()
        .filter(|entry| entry.file_type().is_ok_and(|kind| kind.is_file()))
        .map(|entry| entry.file_name().to_string_lossy().into_owned())
        .filter(|name| name.ends_with(".md") && !name.ends_with(FULL_SUFFIX) && name != INDEX_FILE)
        .collect();
    found.sort();
    found
}

/// Relative link targets a markdown file points at.
///
/// Deliberately forgiving about the surrounding syntax and strict about the
/// target: anything of the form `](target)` counts, and a target naming a file
/// that is not there counts as nothing. A fold claiming to cover a source it
/// has stopped linking is the case this exists to catch.
fn links(text: &str) -> Vec<String> {
    let mut found = Vec::new();
    for tail in text.split("](").skip(1) {
        let Some((target, _)) = tail.split_once(')') else {
            continue;
        };
        let target = target.split_whitespace().next().unwrap_or_default();
        if target.is_empty() || target.contains("://") {
            continue;
        }
        let target = target.trim_start_matches("./").to_string();
        if !found.contains(&target) {
            found.push(target);
        }
    }
    found
}

/// The children a node links, resolved against the folder holding it.
fn linked_children(workspace: &Path, node: &str) -> Vec<String> {
    let Some((folder, _)) = node.rsplit_once('/') else {
        return Vec::new();
    };
    let Ok(text) = fs::read_to_string(workspace.join(node)) else {
        return Vec::new();
    };
    links(&text)
        .into_iter()
        .map(|target| resolve(folder, &target))
        .filter(|target| workspace.join(target).is_file())
        .collect()
}

/// Resolves a link target against the folder holding the file that wrote it.
///
/// `..` is popped here rather than left to the filesystem, because a fold in
/// `research/folds/` naturally links its sources as `../paper.md` and a path
/// still carrying that segment matches nothing when compared against the
/// relative paths the rest of this module works in.
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

/// Children written since the parent was, as relative paths.
fn changed_since(workspace: &Path, parent: &str, children: &[String]) -> Vec<String> {
    let Some(sealed) = modified(&workspace.join(parent)) else {
        // A parent that does not exist yet is behind every child it should
        // cover, which is the strongest form of the same fault.
        return children.to_vec();
    };
    children
        .iter()
        .filter(|child| modified(&workspace.join(child)).is_some_and(|at| at > sealed))
        .cloned()
        .collect()
}

/// Works out what the tree needs, highest priority first.
///
/// Budget comes before structure and structure before freshness: a node over
/// budget is charging every model call in every role that reads it, an
/// unfolded level cannot be brought under budget without first being split,
/// and a node that is merely behind its children is still true as far as it
/// goes.
pub(super) fn plan(workspace: &Path) -> Vec<Task> {
    let research = workspace.join(RESEARCH_DIR);
    let leaves: Vec<String> = digests(&research)
        .into_iter()
        .map(|name| format!("{RESEARCH_DIR}/{name}"))
        .collect();
    let folds: Vec<String> = digests(&research.join(FOLD_DIR))
        .into_iter()
        .map(|name| format!("{RESEARCH_DIR}/{FOLD_DIR}/{name}"))
        .collect();
    let root = format!("{RESEARCH_DIR}/{INDEX_FILE}");

    // The root folds the level immediately below it, which is the fold nodes
    // once they exist and the digests themselves while the library is small
    // enough not to need them.
    let root_children = if folds.is_empty() {
        leaves.clone()
    } else {
        folds.clone()
    };

    let mut nodes = vec![
        Node {
            path: CONTEXT_FILE.to_string(),
            tokens: tokens(&workspace.join(CONTEXT_FILE)),
            children: vec![root.clone()],
        },
        Node {
            path: root.clone(),
            tokens: tokens(&workspace.join(&root)),
            children: root_children.clone(),
        },
    ];
    nodes.extend(folds.iter().map(|fold| Node {
        path: fold.clone(),
        tokens: tokens(&workspace.join(fold)),
        children: linked_children(workspace, fold),
    }));

    let mut tasks = Vec::new();
    for node in nodes.iter().filter(|node| node.tokens > NODE_TOKENS) {
        tasks.push(Task {
            node: node.clone(),
            fault: Fault::OverBudget,
        });
    }
    for node in nodes.iter().filter(|node| node.children.len() > FANOUT) {
        tasks.push(Task {
            node: node.clone(),
            fault: Fault::Unfolded,
        });
    }
    for node in &nodes {
        // A node with nothing under it is not stale, it is unstarted, and
        // asking for a fold of no children produces invention.
        if node.children.is_empty() {
            continue;
        }
        let changed = changed_since(workspace, &node.path, &node.children);
        if changed.len() >= STALE_CHILDREN || (!changed.is_empty() && node.tokens == 0) {
            tasks.push(Task {
                node: node.clone(),
                fault: Fault::Stale(changed),
            });
        }
    }
    tasks
}

/// Renders the highest-priority task as an instruction, if there is one.
///
/// One task per cycle. Handing over the whole plan invites a cycle that
/// rewrites every level at once, and a fold of a level that is itself about to
/// be rewritten is work thrown away.
pub(super) fn briefing(workspace: &Path) -> Option<String> {
    let task = plan(workspace).into_iter().next()?;
    let node = &task.node;
    let mut out = String::new();
    let _ = write!(
        out,
        "Before anything else, this cycle's job is the summary tree. Every node in it \
         is capped at {NODE_TOKENS} tokens and links to the files it covers, so \
         detail a fold leaves out stays reachable instead of being lost.\n\n"
    );
    match &task.fault {
        Fault::OverBudget => {
            let _ = write!(
                out,
                "`{}` is about {} tokens, over the {NODE_TOKENS}-token cap, and it is \
                 re-sent on every model call in every role that reads it. Rewrite it \
                 under the cap this cycle: merge findings that say the same thing, drop \
                 what later work has settled, and keep the statements and their \
                 consequences rather than the narrative. Whatever you cut, leave a \
                 markdown link to the file that still holds it — that is what makes the \
                 cut safe. Gather nothing new until it fits.",
                node.path, node.tokens,
            );
        }
        Fault::Unfolded => {
            let needed = node.children.len().div_ceil(FANOUT);
            let _ = write!(
                out,
                "`{}` now has {} files under it, more than the {FANOUT} one node may \
                 cover. Group them by subject into {needed} fold notes under \
                 `{RESEARCH_DIR}/{FOLD_DIR}/`, named for the subject they cover. Each \
                 fold says what its sources together establish, stays under \
                 {NODE_TOKENS} tokens, and links every source it covers. Then rewrite \
                 `{}` as a fold of the fold notes, linking each. The files are:\n{}",
                node.path,
                node.children.len(),
                node.path,
                list(&node.children),
            );
        }
        Fault::Stale(changed) => {
            let _ = write!(
                out,
                "`{}` has not been rewritten since {} of the files below it changed. \
                 Refold it so it says what they now establish, under {NODE_TOKENS} \
                 tokens, linking each file it covers. Changed:\n{}",
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
