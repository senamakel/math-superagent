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
const PROGRAM: [&str; 10] = [
    "py", "sh", "bash", "c", "cpp", "rs", "js", "ts", "sql", "ipynb",
];

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

#[cfg(test)]
mod test;
