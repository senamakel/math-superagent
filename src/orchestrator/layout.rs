//! Where a new file belongs, decided by the runtime rather than by the agent.
//!
//! A long run produces a lot of files, and left alone every one of them lands
//! at the workspace root. One live run reached thirty-one Python programs,
//! four JSON tables, and a scatter of `.out.txt` captures beside the six
//! Markdown files that actually say what the run is doing — so the listing
//! every agent reads before deciding anything was mostly noise, and the two
//! files carrying the derivation were buried in it.
//!
//! The root is therefore an allowlist, not a default. It holds the run's
//! prose — what the problem is, what is believed, what has been derived — and
//! nothing else. Programs and the data they produce go to `code/`, which
//! carries its own `AGENTS.md` and `INDEX.md` so the rules for working there
//! travel with the folder.
//!
//! Inside `code/` there is a second level this module deliberately does not
//! decide. Where a program belongs among the questions a run is attacking is a
//! judgement about the mathematics, and a rule that guessed at it would file
//! by extension — which is how a folder ends up sorted by a fact nobody cares
//! about. So a caller that names a folder is trusted, the default sink stays
//! `code/`, and whether that sink has grown into a pile is measured after the
//! fact by [`super::code_layout`].
//!
//! Placement is enforced here, in the write path, for the same reason
//! [`super::documents::research_path`] enforces `research/`: a prompt asking
//! for tidiness holds only until a model is busy. What cannot be enforced here
//! is a shell redirect — `python solve.py > out.txt` writes through the
//! filesystem, not through a tool — so later readers still sweep. This makes
//! the sweep small instead of making it the only defence.

/// The folder holding the run's plumbing rather than its work.
pub(super) const CONFIG_DIR: &str = "config";

/// The folder every program and its output belongs to.
pub(super) const CODE_DIR: &str = "code";

/// The folder holding what other programs import.
///
/// Named `lib` rather than `toolkits` because the name is what decides how it
/// gets used. A folder called `toolkits` reads as somewhere to put tools, and
/// that is exactly what a live run did with it: thirteen one-off scripts with
/// their data pasted into the source, and not one import anywhere in the
/// workspace. `lib` reads as things other files import, which is the only
/// thing that belongs here.
///
/// `/workspace/code` is on `PYTHONPATH` (see the `Dockerfile`), so a module
/// here is `from lib.<module> import <name>` from any working directory and
/// any invocation. That is deliberate: before it, importing worked only when a
/// program happened to be run as `python code/<name>.py`, and three separate
/// `sys.path.insert` dialects appear in the committed workspaces where agents
/// discovered that the hard way. An agent burned once inlines the routine
/// instead, which is how a folder ends up holding seven copies of one
/// function.
pub(super) const LIB_DIR: &str = "code/lib";

/// Data a program produced, kept apart from the programs themselves.
///
/// A folder holding `solve.py` beside `solve.out.txt`, `fdtable.json`, and
/// nine more captures is the root's problem moved one level down. The split
/// costs nothing to maintain — it is decided by extension — and it means the
/// listing of `code/` answers "what can I run" rather than "what has been
/// run".
pub(super) const OUTPUT_DIR: &str = "code/out";

/// Extensions that make a file a program.
///
/// `lean` is here for the same reason `py` is, and its absence was a real
/// misreading: a `.lean` file is source a role wrote, and without it every
/// statement in `code/lean/` counted as something a program *produced*. So a
/// workspace holding nothing but stated lemmas answered yes to
/// [`has_results`] — reporting results it did not have — and the judge's output
/// scan collected the Lean library as though it were output data.
const PROGRAM: [&str; 11] = [
    "py", "sh", "bash", "c", "cpp", "rs", "js", "ts", "sql", "ipynb", "lean",
];

/// How deep under `code/` to look for a result, and how many entries to read.
const RESULT_DEPTH: usize = 3;
const RESULT_SCAN: usize = 500;

/// Whether any program in this workspace has produced something.
///
/// A *result* is a file under `code/` that a program wrote: not a program, and
/// not a note. Both exclusions are load-bearing. `code/` is seeded from
/// `workspace/template`, so it holds `AGENTS.md` and `INDEX.md` from the first
/// second of every run, and `code/out/` holds a `README.md`; a check for
/// "results exist" that counts those answers yes on an empty run forever.
///
/// This exists because the check it replaces asked whether the *folder* existed.
/// `RESULT_FOLDERS` lists `code/out` and `code`, and the template has always
/// created `code/`, so the "a workspace with no results at all reads as
/// unchanged" guard in `results_unchanged` could never fire on a real
/// workspace — it was answering a question nobody was asking. PE620 is what
/// that cost: its `pattern_finder` was the run's largest consumer at 34 model
/// calls and 35.4% of spend, waking on every churn of `code/`, walking the
/// tree, and concluding each time that there was nothing to analyse — a
/// conclusion the run had already written down itself, in
/// `code/out/oracle-model-broken.md`, saying its sequence tools "were therefore
/// not run: there are no program-produced terms to feed them".
pub(super) fn has_results(workspace: &std::path::Path) -> bool {
    fn walk(folder: &std::path::Path, depth: usize, budget: &mut usize) -> bool {
        if depth == 0 || *budget == 0 {
            return false;
        }
        let Ok(entries) = std::fs::read_dir(folder) else {
            return false;
        };
        for entry in entries.flatten() {
            if *budget == 0 {
                return false;
            }
            *budget -= 1;
            let name = entry.file_name();
            let name = name.to_string_lossy();
            if name.starts_with('.') || name == "__pycache__" {
                continue;
            }
            let path = entry.path();
            if path.is_dir() {
                if walk(&path, depth - 1, budget) {
                    return true;
                }
            } else if !is_authored(&name) {
                return true;
            }
        }
        false
    }
    let mut budget = RESULT_SCAN;
    walk(&workspace.join(CODE_DIR), RESULT_DEPTH, &mut budget)
}

/// Whether a file under `code/` was written by a person rather than a program.
pub(super) fn is_authored(name: &str) -> bool {
    let found = extension(name);
    found == "md" || PROGRAM.iter().any(|program| found == *program)
}

/// Files allowed at the workspace root, by exact name.
///
/// The run's prose and the problem statement it was given. Configuration, the
/// trace, the document index, and the source URL are plumbing rather than
/// work, so they live under `config/` — nothing in them is worth a line in the
/// listing every agent reads before deciding what to do next.
const ROOT_FILES: [&str; 4] = ["AGENTS.md", "README.md", "INDEX.md", "problem.md"];

/// Extensions allowed at the workspace root.
///
/// Markdown only. Every derivation, belief, and plan the run writes is
/// Markdown, and keeping the root to it is what makes a directory listing read
/// as an account of the work rather than a build directory.
const ROOT_EXTENSIONS: [&str; 1] = ["md"];

/// Returns the extension of a file name, lowercased.
fn extension(name: &str) -> String {
    std::path::Path::new(name)
        .extension()
        .map(|extension| extension.to_string_lossy().to_lowercase())
        .unwrap_or_default()
}

/// Returns where `relative` belongs, which is usually where it was asked for.
///
/// Only a path at the workspace root can move, and only when the root does not
/// admit it. A path already naming a folder is trusted: an agent that said
/// where something goes has made a decision this module has no better
/// information than.
pub(super) fn placed(relative: &str) -> String {
    let trimmed = relative
        .trim()
        .trim_start_matches("/workspace/")
        .trim_start_matches("./")
        .trim_start_matches('/');
    if trimmed.is_empty() {
        return trimmed.to_string();
    }
    if trimmed.contains('/') {
        // Anything under a folder has already been placed, whether by an agent
        // that knows where it goes or by a rule like `research_path`. Naming a
        // folder is a decision, and this module has no better information than
        // the caller that made it.
        return trimmed.to_string();
    }
    if ROOT_FILES.contains(&trimmed) || ROOT_EXTENSIONS.contains(&extension(trimmed).as_str()) {
        return trimmed.to_string();
    }
    if trimmed == "config.toml"
        || trimmed == "problem.url"
        || trimmed == "problem.html"
        || trimmed == "trace.jsonl"
    {
        // Plumbing the runtime itself writes or reads. It has a home, and the
        // root listing is not it.
        return format!("{CONFIG_DIR}/{trimmed}");
    }
    if PROGRAM.contains(&extension(trimmed).as_str()) {
        return format!("{CODE_DIR}/{trimmed}");
    }
    format!("{OUTPUT_DIR}/{trimmed}")
}

/// Explains a placement to the agent that asked for the other one.
///
/// Returned in the tool result rather than swallowed, because a model that is
/// not told where its file went writes the next one to the same wrong place
/// and then cannot read either back.
pub(super) fn note(requested: &str, placed: &str) -> String {
    if requested == placed {
        return String::new();
    }
    format!(
        " (filed at {placed}; the workspace root holds the run's Markdown, `{CODE_DIR}/` the \
         programs, and `{OUTPUT_DIR}/` what they produce. `{CODE_DIR}/` is a package tree, not a \
         drawer: what another program imports belongs in `{LIB_DIR}/<subject>.py` and is reached \
         as `from lib.<subject> import <name>`, and a program exploring one question belongs in \
         `{CODE_DIR}/<question>/` beside the others attacking it. Name the folder yourself and \
         this file goes there instead)"
    )
}

/// Files the sweep never touches, whatever their extension.
///
/// A dotfile at the root is machinery — the checkpoint history, the pip
/// prefix, a bytecode cache — and none of it is the run's work to file.
fn swept(name: &str) -> bool {
    !name.starts_with('.') && placed(name) != name
}

/// Moves root-level files the layout does not admit into the folders it does.
///
/// [`placed`] enforces the layout in the write path, which covers every file
/// that arrives through a tool. It cannot cover a shell redirect or a heredoc:
/// `cat > solve.py <<'EOF'` and `python solve.py > out.txt` write through the
/// filesystem, and the tool sees only a command and an exit code. Left to a
/// prompt, that hole reopens the problem the layout exists to close — one live
/// workspace accumulated six programs at its root in nineteen minutes, written
/// entirely through the shell while another agent was running.
///
/// So the sweep runs where the files appear, immediately after the command
/// that could have made them. Three rules keep it safe to run that often:
///
/// - a destination that already exists is left alone, because a file carrying
///   a result must never be overwritten by one that happens to share its name;
/// - a failure to move anything is silent, because the command itself
///   succeeded and a tidying step must not turn that into an error;
/// - every move is named in the result, for the reason [`note`] exists — an
///   agent not told where its file went runs `python solve.py` again and
///   cannot find it.
pub(super) async fn sweep(workspace: &std::path::Path) -> Swept {
    let Ok(mut entries) = tokio::fs::read_dir(workspace).await else {
        return Swept::default();
    };
    let mut swept_files = Swept::default();
    while let Ok(Some(entry)) = entries.next_entry().await {
        if !entry.file_type().await.is_ok_and(|kind| kind.is_file()) {
            continue;
        }
        let name = entry.file_name().to_string_lossy().to_string();
        if !swept(&name) {
            continue;
        }
        let destination = placed(&name);
        let target = workspace.join(&destination);
        if target.exists() {
            // A file carrying a result must never be overwritten by one that
            // shares its name — but silence here is its own failure. The stray
            // stays at the root for the rest of the run, the two files drift,
            // and nothing says which is current. A live run reached exactly
            // this: `brute.py` at the root and a different `code/brute.py`
            // beside it, four minutes apart. So the collision is reported and
            // the caller decides.
            swept_files.blocked.push((name, destination));
            continue;
        }
        let Some(parent) = target.parent() else {
            continue;
        };
        if tokio::fs::create_dir_all(parent).await.is_err() {
            continue;
        }
        if tokio::fs::rename(entry.path(), &target).await.is_ok() {
            swept_files.moved.push((name, destination));
        }
    }
    swept_files
}

/// What one sweep did, and what it refused to do.
#[derive(Default)]
pub(super) struct Swept {
    /// Files filed away, as `(was, is)`.
    moved: Vec<(String, String)>,
    /// Strays left in place because their destination was taken.
    blocked: Vec<(String, String)>,
}

/// Renders a list of `(from, to)` pairs for a tool result.
fn listed(pairs: &[(String, String)]) -> String {
    pairs
        .iter()
        .map(|(from, to)| format!("{from} -> {to}"))
        .collect::<Vec<_>>()
        .join(", ")
}

/// Reports what the sweep moved, in the result of the command that ran.
pub(super) fn swept_note(swept: &Swept) -> String {
    use std::fmt::Write as _;
    let mut note = String::new();
    if !swept.moved.is_empty() {
        let _ = write!(
            note,
            "\n\nfiled from the workspace root: {}. The root holds the run's Markdown, \
             `{CODE_DIR}/` the programs, and `{OUTPUT_DIR}/` what they produce — write there \
             directly, or run these by their new path.",
            listed(&swept.moved)
        );
    }
    if !swept.blocked.is_empty() {
        let _ = write!(
            note,
            "\n\nleft at the workspace root because the filed name is taken: {}. Nothing here \
             is overwritten, so two files now share a name and only one is filed. Decide which \
             is current: fold the change into the filed copy, or move the stray to a new name \
             under `{CODE_DIR}/` and delete it from the root.",
            listed(&swept.blocked)
        );
    }
    note
}

#[cfg(test)]
#[path = "layout_test.rs"]
mod test;
