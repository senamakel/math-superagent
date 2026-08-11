//! A bounded summary tree over the workspace's markdown.
//!
//! The run's standing context grows without limit and is re-sent on every
//! model call in nine roles, so the question is never *whether* to compress it
//! but how to compress it without losing what was compressed away. A flat
//! rewrite loses it: each pass drops what the previous pass judged less
//! important, nothing records what was dropped, and by the tenth pass the file
//! is confident about things no longer traceable to a source.
//!
//! So compression is a tree, and the tree is laid out on disk as sealed
//! batches:
//!
//! ```text
//! research/
//! ├── ROOT.md          what the whole library now establishes
//! ├── INDEX.md         what each file is — maintained by the index tools
//! ├── L0.0/            the first ten originals, sealed
//! ├── L0.1/            the next ten, still filling
//! ├── L1.0/            one note per sealed L0 batch: L0.0.md, L0.1.md, …
//! └── L2.0/            one note per sealed L1 batch, once L1.0 fills
//! ```
//!
//! A *batch* is the unit of compression. Leaves accumulate in the open batch
//! at level 0; when it reaches [`FANOUT`] it seals, and sealing means one note
//! summarising it appears one level up, named for the batch it covers. That
//! note then accumulates in the open batch at level 1, and the same rule
//! applies again. The tree grows a level only when a level has genuinely
//! outgrown a single node, and every node above `L0` is capped at
//! [`NODE_TOKENS`].
//!
//! Batching rather than one flat folder per level is what makes a fold
//! *stable*. A flat level is re-summarised every time anything is added to it,
//! so the same sources are re-read and re-compressed indefinitely and the
//! summary drifts. A sealed batch is summarised once and never revisited, so
//! the work is done once and the note stays true to what it covers.
//!
//! `ROOT.md` is the top, and it is deliberately not `INDEX.md`. The index says
//! what each file *is* and is derived from the directory by the index tools;
//! the root says what the library *means* and is written by an agent. Holding
//! both in one file put a tool and an agent in contention over it, and cost
//! this workspace three separate rounds of lost descriptions — a refresh
//! overwriting a synthesis, then a synthesis overwriting rows, then rows
//! rewritten in a spelling the refresh could not match.
//!
//! Every node links what it covers with Obsidian wikilinks, so the workspace
//! opens as a vault and a fold is safe to write: what it leaves out is one
//! link down, not gone. This module writes nothing. It reads the workspace,
//! works out which batch needs sealing and which node is over budget or behind
//! what it covers, and says so — the fold itself is a judgement about meaning,
//! so an agent writes it.

use std::fmt::Write as _;
use std::fs;
use std::path::Path;
use std::time::SystemTime;

use super::folder_index::INDEX_FILE;

/// Notes one batch may hold before it seals.
pub(super) const FANOUT: usize = 10;

/// Tokens any node above level 0 may occupy.
///
/// A thousand tokens is what a role can afford to be handed on every one of
/// its model calls. It caps each *node*, not the tree: the tree grows by
/// adding levels, and a reader pays for one path down it rather than all of
/// it.
pub(super) const NODE_TOKENS: u64 = 1_000;

/// Characters charged to one token, matching the harness estimator.
const CHARS_PER_TOKEN: u64 = 4;

/// Notes that must have changed before a parent is rewritten.
const STALE_CHILDREN: usize = 3;

/// Folders carrying a tree, each with its own root.
const ROOTS: [&str; 2] = ["research", "reflections"];

/// The top of a tree.
pub(super) const ROOT_FILE: &str = "ROOT.md";

/// The run-wide standing brief, a root in its own right.
const CONTEXT_FILE: &str = "CONTEXT.md";

/// Deepest level the planner will look for.
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

/// What is wrong with the tree, in the order it wants it fixed.
#[derive(Clone, Debug, PartialEq, Eq)]
pub(super) enum Fault {
    /// The node costs more than a node may spend.
    OverBudget,
    /// A batch is full and has no note summarising it one level up.
    Unsealed {
        /// Where the summarising note belongs.
        summary: String,
    },
    /// A seal does not link back to everything it compressed.
    Unlinked {
        /// The batch the seal covers.
        batch: String,
        /// Notes in that batch the seal does not link.
        missing: Vec<String>,
    },
    /// What the node covers has changed since it was written.
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

/// Reads a batch folder name as its level and batch number.
///
/// A bare `L1` counts as `L1.0`. Every workspace was laid out that way before
/// batches existed, and a planner that saw only the dotted form would report a
/// library of twenty sources as empty.
pub(super) fn batch_of(name: &str) -> Option<(usize, usize)> {
    let rest = name.strip_prefix('L')?;
    match rest.split_once('.') {
        Some((level, batch)) => Some((level.parse().ok()?, batch.parse().ok()?)),
        None => Some((rest.parse().ok()?, 0)),
    }
}

/// The folder holding one batch.
pub(super) fn batch_dir(level: usize, batch: usize) -> String {
    format!("L{level}.{batch}")
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
                && name != ROOT_FILE
        })
        .map(|name| format!("{folder}/{name}"))
        .collect();
    found.sort();
    found
}

/// Every batch folder of one tree, as `(level, batch, folder)`, sorted.
fn batches(workspace: &Path, root: &str) -> Vec<(usize, usize, String)> {
    let Ok(entries) = fs::read_dir(workspace.join(root)) else {
        return Vec::new();
    };
    let mut found: Vec<(usize, usize, String)> = entries
        .flatten()
        .filter(|entry| entry.file_type().is_ok_and(|kind| kind.is_dir()))
        .filter_map(|entry| {
            let name = entry.file_name().to_string_lossy().into_owned();
            let (level, batch) = batch_of(&name)?;
            (level <= MAX_LEVEL).then(|| (level, batch, format!("{root}/{name}")))
        })
        .collect();
    found.sort();
    found
}

/// The batch new notes should join at `level`.
///
/// The open batch is the highest-numbered one still under [`FANOUT`]; when the
/// highest is full, the next one opens. This is what a writer needs in order
/// to file something without knowing the tree's history.
pub(super) fn open_batch(workspace: &Path, root: &str, level: usize) -> usize {
    let mut highest: Option<(usize, bool)> = None;
    for (batch_level, batch, folder) in batches(workspace, root) {
        if batch_level != level {
            continue;
        }
        let full = notes(workspace, &folder).len() >= FANOUT;
        if highest.is_none_or(|(seen, _)| batch > seen) {
            highest = Some((batch, full));
        }
    }
    match highest {
        Some((batch, true)) => batch + 1,
        Some((batch, false)) => batch,
        None => 0,
    }
}

/// Link targets a note points at, as written.
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
            push(target.split(['|', '#']).next().unwrap_or_default());
        }
    }
    for tail in text.split("](").skip(1) {
        if let Some((target, _)) = tail.split_once(')') {
            push(target.split_whitespace().next().unwrap_or_default());
        }
    }
    found
}

/// Notes written since the parent was.
fn changed_since(workspace: &Path, parent: &str, children: &[String]) -> Vec<String> {
    let Some(sealed) = modified(workspace, parent) else {
        // A parent that does not exist yet is behind everything it covers,
        // which is the strongest form of the same fault.
        return children.to_vec();
    };
    children
        .iter()
        .filter(|child| modified(workspace, child).is_some_and(|at| at > sealed))
        .cloned()
        .collect()
}

/// Adds the sealing work one tree needs, and its folds to `nodes`.
///
/// Split out of [`plan`] because the batch walk and the node walk are two
/// separate passes over different things, and reading either meant reading
/// both.
fn seal_tasks(
    workspace: &Path,
    root: &str,
    batches: &[(usize, usize, String)],
    nodes: &mut Vec<Node>,
    unsealed: &mut Vec<Task>,
    unlinked: &mut Vec<Task>,
) {
    for (level, batch, folder) in batches {
        let held = notes(workspace, folder);
        // Level 0 holds originals: never rewritten, never folded, exempt
        // from the cap every level above it is held to.
        if *level > 0 {
            nodes.extend(held.iter().map(|note| Node {
                path: note.clone(),
                tokens: tokens(workspace, note),
                children: linked(workspace, note),
            }));
        }
        if held.len() < FANOUT {
            continue;
        }
        // A full batch is sealed by one note, one level up, named for it.
        let summary = format!(
            "{root}/{}/{}.md",
            batch_dir(level + 1, open_batch(workspace, root, level + 1)),
            batch_dir(*level, *batch)
        );
        if !workspace.join(&summary).is_file() {
            unsealed.push(Task {
                node: Node {
                    path: folder.clone(),
                    tokens: 0,
                    children: held,
                },
                fault: Fault::Unsealed { summary },
            });
            continue;
        }
        // A seal that does not link what it compressed has not compressed
        // it — it has replaced it. The link is the whole reason a fold is
        // safe to write, so it is checked rather than requested.
        let covered = linked(workspace, &summary);
        let missing: Vec<String> = held
            .iter()
            .filter(|note| !covered.contains(note))
            .cloned()
            .collect();
        if !missing.is_empty() {
            unlinked.push(Task {
                node: Node {
                    path: summary,
                    tokens: 0,
                    children: held,
                },
                fault: Fault::Unlinked {
                    batch: folder.clone(),
                    missing,
                },
            });
        }
    }
}

/// Works out what the trees need, highest priority first.
///
/// Budget first, then sealing, then freshness: a node over budget charges
/// every model call in every role that reads it; an unsealed batch is work the
/// tree is waiting on before it can compress at all; and a node merely behind
/// what it covers is still true as far as it goes.
pub(super) fn plan(workspace: &Path) -> Vec<Task> {
    let mut over_budget = Vec::new();
    let mut unsealed = Vec::new();
    let mut unlinked = Vec::new();
    let mut stale = Vec::new();

    let mut nodes = vec![Node {
        path: CONTEXT_FILE.to_string(),
        tokens: tokens(workspace, CONTEXT_FILE),
        children: ROOTS
            .iter()
            .map(|root| format!("{root}/{ROOT_FILE}"))
            .filter(|root| workspace.join(root).is_file())
            .collect(),
    }];

    for root in ROOTS {
        let batches = batches(workspace, root);
        if batches.is_empty() {
            continue;
        }
        let top = batches
            .iter()
            .map(|(level, _, _)| *level)
            .max()
            .unwrap_or_default();
        let top_notes: Vec<String> = batches
            .iter()
            .filter(|(level, _, _)| *level == top)
            .flat_map(|(_, _, folder)| notes(workspace, folder))
            .collect();

        // The root folds the highest level present; everything below it is
        // reached through it.
        nodes.push(Node {
            path: format!("{root}/{ROOT_FILE}"),
            tokens: tokens(workspace, &format!("{root}/{ROOT_FILE}")),
            children: top_notes,
        });

        seal_tasks(
            workspace,
            root,
            &batches,
            &mut nodes,
            &mut unsealed,
            &mut unlinked,
        );
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

    over_budget.extend(unsealed);
    over_budget.extend(unlinked);
    over_budget.extend(stale);
    over_budget
}

/// The notes a fold links, resolved against the tree holding it.
///
/// A wikilink carries a bare note name and Obsidian resolves it anywhere in
/// the vault, so the whole tree is searched rather than only the folder beside
/// the fold.
fn linked(workspace: &Path, node: &str) -> Vec<String> {
    let Some((root, _)) = node.split_once('/') else {
        return Vec::new();
    };
    let Ok(text) = fs::read_to_string(workspace.join(node)) else {
        return Vec::new();
    };
    let candidates: Vec<String> = batches(workspace, root)
        .iter()
        .flat_map(|(_, _, folder)| notes(workspace, folder))
        .collect();
    let mut found = Vec::new();
    for target in links(&text) {
        let name = target.rsplit('/').next().unwrap_or(&target);
        let name = match Path::new(name).extension() {
            Some(extension) if extension.eq_ignore_ascii_case("md") => name.to_string(),
            _ => format!("{name}.md"),
        };
        if let Some(hit) = candidates
            .iter()
            .find(|candidate| candidate.ends_with(&format!("/{name}")))
            && !found.contains(hit)
        {
            found.push(hit.clone());
        }
    }
    found
}

/// Renders the highest-priority task as an instruction, if there is one.
///
/// One task per cycle. Handing over the whole plan invites a cycle that
/// rewrites every level at once, and folding a level that is itself about to
/// be rewritten is work thrown away.
pub(super) fn briefing(workspace: &Path) -> Option<String> {
    let task = plan(workspace).into_iter().next()?;
    let node = &task.node;
    let mut out = String::new();
    let _ = write!(
        out,
        "Before anything else, this cycle's job is the summary tree. Originals sit in \
         `L0.<n>/` and are never edited. A batch holds at most {FANOUT} notes; when it \
         fills, one note a level up seals it — named for the batch it covers — and that \
         note is never revisited. Every node above level 0 is capped at {NODE_TOKENS} \
         tokens and wikilinks what it covers, `[[note-name]]`, so what a fold leaves out \
         stays one step away. `ROOT.md` is the top of the tree; `INDEX.md` beside it is \
         the file table, maintained by describe_file and refresh_index, and is not yours \
         to write.\n\n"
    );
    match &task.fault {
        Fault::OverBudget => {
            let _ = write!(
                out,
                "`{}` is about {} tokens, over the {NODE_TOKENS}-token cap, and is \
                 re-sent on every model call in every role that reads it. Rewrite it \
                 under the cap this cycle: merge what says the same thing, drop what \
                 later work has settled, and keep the statements and their consequences \
                 rather than the narrative. Whatever you cut, leave a wikilink to the \
                 note that still holds it. Gather nothing new until it fits.",
                node.path, node.tokens,
            );
        }
        Fault::Unsealed { summary } => {
            let _ = write!(
                out,
                "`{}` is full at {} notes and is waiting to be sealed. Write `{summary}`: \
                 one note saying what those {} together establish, under {NODE_TOKENS} \
                 tokens, wikilinking each. Seal it once and do not revisit it — a batch \
                 summarised repeatedly drifts from what it covers. Then bring `ROOT.md` \
                 up to date with what the tree now says. The batch holds:\n{}",
                node.path,
                node.children.len(),
                node.children.len(),
                list(&node.children),
            );
        }
        Fault::Unlinked { batch, missing } => {
            let _ = write!(
                out,
                "`{}` seals `{batch}` but does not link {} of the {} notes it compressed. \
                 A seal that drops a link has not compressed that note, it has replaced \
                 it: nothing points at the detail any more, and a claim nobody can trace \
                 to a source is worth less than no claim. Add a wikilink for each, and \
                 say in one clause what each contributes — a bare link list is a \
                 directory, not a fold. Missing:\n{}",
                node.path,
                missing.len(),
                node.children.len(),
                list(missing),
            );
        }
        Fault::Stale(changed) => {
            let _ = write!(
                out,
                "`{}` has not been rewritten since {} of the notes below it changed. \
                 Rewrite it so it says what they now establish, under {NODE_TOKENS} \
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
