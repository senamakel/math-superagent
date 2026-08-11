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
//! Placement is enforced here, in the write path, for the same reason
//! [`super::documents::research_path`] enforces `research/`: a prompt asking
//! for tidiness holds only until a model is busy. What cannot be enforced here
//! is a shell redirect — `python solve.py > out.txt` writes through the
//! filesystem, not through a tool — so the organizer still sweeps. This makes
//! the sweep small instead of making it the only defence.

/// Folders that already say what they hold, left exactly as addressed.
///
/// Each is a place the runtime or an agent files things deliberately, so a
/// path naming one has already made this decision.
const SETTLED: [&str; 7] = [
    "research",
    "reflections",
    "toolkits",
    "code",
    "raw",
    "prompts",
    "notes",
];

/// The folder every program and its output belongs to.
pub(super) const CODE_DIR: &str = "code";

/// Data a program produced, kept apart from the programs themselves.
///
/// A folder holding `solve.py` beside `solve.out.txt`, `fdtable.json`, and
/// nine more captures is the root's problem moved one level down. The split
/// costs nothing to maintain — it is decided by extension — and it means the
/// listing of `code/` answers "what can I run" rather than "what has been
/// run".
pub(super) const OUTPUT_DIR: &str = "code/out";

/// Extensions that make a file a program.
const PROGRAM: [&str; 10] = [
    "py", "sh", "bash", "c", "cpp", "rs", "js", "ts", "sql", "ipynb",
];

/// Files allowed at the workspace root, by exact name.
///
/// The run's prose, its configuration, and the problem statement it was given.
const ROOT_FILES: [&str; 6] = [
    "AGENTS.md",
    "README.md",
    "INDEX.md",
    "config.toml",
    "problem.html",
    "problem.url",
];

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
    if let Some((folder, _)) = trimmed.split_once('/') {
        // Anything under a folder has already been placed, whether by an agent
        // that knows where it goes or by a rule like `research_path`.
        let _ = folder;
        return trimmed.to_string();
    }
    if ROOT_FILES.contains(&trimmed) || ROOT_EXTENSIONS.contains(&extension(trimmed).as_str()) {
        return trimmed.to_string();
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
         programs, and `{OUTPUT_DIR}/` what they produce)"
    )
}

/// Whether a folder is one the layout already accounts for.
pub(super) fn settled(folder: &str) -> bool {
    SETTLED.contains(&folder)
}

#[cfg(test)]
mod test;
