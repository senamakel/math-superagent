//! What `code/` has become, measured rather than asked about.
//!
//! [`super::layout`] decides where a new program goes, and it has exactly one
//! answer: `code/`. That is right for the first ten files and wrong for the
//! fiftieth. A live run reached forty-six Python programs sitting as siblings
//! in one folder, and the cost was not untidiness — it was arithmetic. `H(n)`
//! was defined seven times in that folder, `lex_ranks` six, `power` five: the
//! same routine typed out again by an agent that could not see it already
//! existed, each copy free to be the one with the bug, and the run's own
//! `toolkits/` folder holding two helpers nobody imported.
//!
//! Another workspace made the failure plainer still. It wrote *thirteen*
//! helpers and imported none of them, because what it filed under `toolkits/`
//! were one-off scripts with their data pasted into the source. Asking for
//! reuse in a prompt had produced a second flat pile.
//!
//! So reuse is measured here, in the same spirit as
//! [`super::context_tree::plan`]: walk `code/`, work out the one thing most
//! wrong with its shape, and say so. This module writes nothing — which
//! functions belong together is a judgement about the mathematics, so an agent
//! makes it — but whether a routine has been typed out three times is not a
//! judgement, so it is counted.
//!
//! The faults are ordered by what they cost. A routine defined in three
//! programs is the expensive one: the copies drift, and a check that passes
//! against one copy says nothing about the other two. A folder of fifty
//! siblings is next, because it is what makes the copying invisible. A folder
//! with no index is last, since it is only illegible rather than wrong.

use std::collections::BTreeMap;
use std::fmt::Write as _;
use std::fs;
use std::path::Path;

use super::folder_index::INDEX_FILE;
use super::layout::{CODE_DIR, LIB_DIR, OUTPUT_DIR};

/// Programs that must define a symbol before it is worth promoting.
///
/// Two copies of a routine is often one program and the oracle it is checked
/// against, which is the arrangement `code/AGENTS.md` explicitly asks for. The
/// third copy is the one nobody meant to write.
const DUPLICATES: usize = 3;

/// Programs allowed directly in `code/` before it wants grouping.
///
/// Matched to [`super::context_tree::FANOUT`] and for the same reason: ten
/// entries is a listing a reader takes in at a glance, and the eleventh is
/// where it starts being scanned instead.
const LOOSE: usize = 10;

/// How deep the walk goes below `code/`.
///
/// Two levels — a topic folder and a package inside it — is the shape this
/// module is asking for. A tree deeper than that is not what went wrong.
const MAX_DEPTH: usize = 4;

/// Names too common to mean two programs share a routine.
///
/// Every script has an entry point, and a test is named for what it tests.
const IGNORED: [&str; 2] = ["main", "run"];

/// What is wrong with the shape of `code/`, in the order it wants it fixed.
#[derive(Clone, Debug, PartialEq, Eq)]
pub(super) enum Fault {
    /// One routine has been written out in several programs.
    Duplicated {
        /// The function or class defined more than once.
        symbol: String,
        /// The programs defining it, workspace-relative.
        files: Vec<String>,
        /// Whether `code/lib/` already holds a definition of it.
        shelved: bool,
    },
    /// `code/` holds more loose programs than a listing can carry.
    Loose {
        /// The programs sitting directly in `code/`.
        files: Vec<String>,
    },
    /// A folder of programs says nothing about what any of them is for.
    Unindexed {
        /// The folder, workspace-relative.
        folder: String,
        /// How many programs it holds.
        programs: usize,
    },
}

/// One thing wrong with `code/`.
#[derive(Clone, Debug, PartialEq, Eq)]
pub(super) struct Task {
    /// Why the folder needs work.
    pub(super) fault: Fault,
}

/// Reads the top-level functions and classes a Python source defines.
///
/// Column zero only, so a method on a class and a closure inside a function
/// are not counted: what this module is looking for is a routine another
/// program could have imported, and neither of those is importable on its own.
fn symbols(source: &str) -> Vec<String> {
    let mut found: Vec<String> = Vec::new();
    for line in source.lines() {
        let rest = line
            .strip_prefix("def ")
            .or_else(|| line.strip_prefix("class "))
            .or_else(|| line.strip_prefix("async def "));
        let Some(rest) = rest else { continue };
        let name: String = rest
            .chars()
            .take_while(|character| character.is_alphanumeric() || *character == '_')
            .collect();
        if name.is_empty()
            || name.starts_with('_')
            || name.starts_with("test_")
            || IGNORED.contains(&name.as_str())
            || found.contains(&name)
        {
            continue;
        }
        found.push(name);
    }
    found
}

/// Every Python program under `code/`, workspace-relative and sorted.
///
/// `code/out/` is excluded because what a program produced is not a program,
/// and bytecode caches because they are not source.
fn programs(workspace: &Path) -> Vec<String> {
    let mut found = Vec::new();
    walk(workspace, CODE_DIR, 0, &mut found);
    found.sort();
    found
}

/// Collects Python sources below `relative`, depth-first.
fn walk(workspace: &Path, relative: &str, depth: usize, found: &mut Vec<String>) {
    if depth > MAX_DEPTH || relative == OUTPUT_DIR {
        return;
    }
    let Ok(entries) = fs::read_dir(workspace.join(relative)) else {
        return;
    };
    for entry in entries.flatten() {
        let name = entry.file_name().to_string_lossy().to_string();
        if name.starts_with('.') || name == "__pycache__" {
            continue;
        }
        let path = format!("{relative}/{name}");
        if entry.path().is_dir() {
            walk(workspace, &path, depth + 1, found);
        } else if name.to_lowercase().ends_with(".py") {
            found.push(path);
        }
    }
}

/// The folder holding a workspace-relative path.
fn folder_of(path: &str) -> String {
    path.rsplit_once('/')
        .map_or_else(String::new, |(folder, _)| folder.to_string())
}

/// Works out what `code/` needs, most expensive fault first.
pub(super) fn plan(workspace: &Path) -> Vec<Task> {
    let programs = programs(workspace);
    let mut defined: BTreeMap<String, Vec<String>> = BTreeMap::new();
    for path in &programs {
        let Ok(source) = fs::read_to_string(workspace.join(path)) else {
            continue;
        };
        for symbol in symbols(&source) {
            defined.entry(symbol).or_default().push(path.clone());
        }
    }

    let mut duplicated: Vec<Task> = defined
        .into_iter()
        .filter(|(_, files)| files.len() >= DUPLICATES)
        .map(|(symbol, files)| Task {
            fault: Fault::Duplicated {
                shelved: files.iter().any(|file| file.starts_with(LIB_DIR)),
                symbol,
                files,
            },
        })
        .collect();
    // Most copied first: it is the routine the run is most likely to be
    // holding two disagreeing versions of.
    duplicated.sort_by_key(|task| match &task.fault {
        Fault::Duplicated { symbol, files, .. } => (usize::MAX - files.len(), symbol.clone()),
        _ => (usize::MAX, String::new()),
    });

    let loose: Vec<String> = programs
        .iter()
        .filter(|path| folder_of(path) == CODE_DIR)
        .cloned()
        .collect();
    if loose.len() > LOOSE {
        duplicated.push(Task {
            fault: Fault::Loose { files: loose },
        });
    }

    let mut counts: BTreeMap<String, usize> = BTreeMap::new();
    for path in &programs {
        *counts.entry(folder_of(path)).or_default() += 1;
    }
    for (folder, count) in counts {
        if !workspace.join(&folder).join(INDEX_FILE).is_file() {
            duplicated.push(Task {
                fault: Fault::Unindexed {
                    folder,
                    programs: count,
                },
            });
        }
    }

    duplicated
}

/// Renders the highest-priority fault as an instruction, if there is one.
///
/// One per cycle, for the same reason [`super::context_tree::briefing`] hands
/// over one: a cycle asked to fix everything about a folder rewrites all of
/// it, and a reorganisation carried out while the run is still deciding what
/// it is doing is work thrown away.
pub(super) fn briefing(workspace: &Path) -> Option<String> {
    let task = plan(workspace).into_iter().next()?;
    let mut out = String::new();
    let _ = write!(
        out,
        "This cycle's job is the shape of `{CODE_DIR}/`. Programs are Python and \
         `/workspace/{CODE_DIR}` is on `PYTHONPATH`, so every folder in it is importable by \
         name from anywhere: a helper at `{LIB_DIR}/perms.py` is `from lib.perms import \
         lex_ranks`, and a program at `{CODE_DIR}/chains/probe.py` is `from chains.probe import \
         probe`. `{LIB_DIR}/` holds what other programs import — one subject per module, its \
         functions named for what they compute. Everything else is grouped by the question it \
         attacks, one folder per question, each with its own `{INDEX_FILE}`, and what those \
         programs produced under `{OUTPUT_DIR}/`. Move and rename to that shape; never delete a \
         program carrying a result, and never change what one computes.\n\n"
    );
    match &task.fault {
        Fault::Duplicated {
            symbol,
            files,
            shelved,
        } => {
            let _ = write!(
                out,
                "`{symbol}` is defined in {} separate programs: {}. ",
                files.len(),
                files.join(", "),
            );
            if *shelved {
                let _ = write!(
                    out,
                    "One of those is `{LIB_DIR}/`, so the shelf already has it and the other \
                     copies are the run ignoring its own library. Leave the shelved definition \
                     alone and rewrite each other program to import it.",
                );
            } else {
                let _ = write!(
                    out,
                    "Copies drift, and a check that passes against one says nothing about the \
                     others. Move the definition into the `{LIB_DIR}/` module for its subject, \
                     import it everywhere it was copied, and describe it with `describe_file` so \
                     `{LIB_DIR}/{INDEX_FILE}` records its signature, what it returns, and what \
                     established it correct. If the copies have genuinely diverged, say so in \
                     the index rather than picking one — a silently chosen definition is worse \
                     than two admitted ones.",
                );
            }
        }
        Fault::Loose { files } => {
            let _ = write!(
                out,
                "`{CODE_DIR}/` holds {} programs directly, past the {LOOSE} a listing can \
                 carry: {}. Group them by the question each attacks — the folder names come \
                 from the mathematics, not from when a file was written — and give every new \
                 folder an `{INDEX_FILE}` through `refresh_index` and `describe_file`. Anything \
                 another program would import belongs in `{LIB_DIR}/` instead.",
                files.len(),
                files.join(", "),
            );
        }
        Fault::Unindexed { folder, programs } => {
            let _ = write!(
                out,
                "`{folder}/` holds {programs} programs and no `{INDEX_FILE}`, so nothing there \
                 says which is the oracle, which carries a result, and which was superseded. \
                 Run `refresh_index` on it and describe every row: what the program computes, \
                 and what established it is correct.",
            );
        }
    }
    Some(out)
}

#[cfg(test)]
mod test;
