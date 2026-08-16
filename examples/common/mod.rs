//! Shared plumbing for the host-side report examples.
//!
//! `dump_prompts` and `derive_ledgers` both render state a workspace already
//! holds, both produce more than anybody wants on a terminal, and both had the
//! same tail: parse a workspace path, decide whether to print or write, and put
//! the file somewhere Git will not pick it up. Two copies of that would drift,
//! and the one that drifts is the one that writes to a path outside `/reports/`
//! and gets committed.
//!
//! Lives in a subdirectory because Cargo builds `examples/*.rs` and
//! `examples/*/main.rs` as example targets and nothing else, so
//! `examples/common/mod.rs` is shared code rather than a third example with no
//! `main`.

use std::path::{Path, PathBuf};

/// Where a report goes when it is not being piped.
///
/// Ignored by Git, and the `.gitignore` entry carries the argument: these are
/// renderings of state already in history, regenerable by rerunning the command
/// beside them, and large enough that committing one would put a diff nobody
/// can review into every batch.
const REPORTS_ROOT: &str = "reports";

/// What the caller was asked to do.
pub(crate) struct Options {
    /// The workspace to report on.
    pub(crate) workspace: String,
    /// Print the report instead of writing it, for piping into a pager.
    pub(crate) to_stdout: bool,
}

/// Reads the arguments both report examples take.
///
/// One positional workspace, defaulting to `default_workspace`, and `--stdout`.
/// An unknown option is an error rather than being ignored: a typo'd flag that
/// silently does nothing leaves the caller believing they piped a report they
/// actually wrote to a file, or the reverse.
///
/// # Errors
///
/// Returns a message when an unrecognised option is given.
pub(crate) fn options(default_workspace: &str) -> Result<Options, String> {
    let mut workspace: Option<String> = None;
    let mut to_stdout = false;
    for argument in std::env::args().skip(1) {
        match argument.as_str() {
            "--stdout" => to_stdout = true,
            other if other.starts_with("--") => {
                return Err(format!(
                    "unknown option `{other}`; the only one is `--stdout`"
                ));
            }
            other => workspace = Some(other.to_string()),
        }
    }
    Ok(Options {
        workspace: workspace.unwrap_or_else(|| default_workspace.to_string()),
        to_stdout,
    })
}

/// The report folder for `workspace`, one per project.
///
/// `workspace/conjectures/gilbreath` becomes `reports/conjectures/gilbreath/`,
/// mirroring the tree it describes so a reader who knows where a workspace
/// lives knows where its reports do. A path outside `workspace/` — a scratch
/// copy, a fixture — is flattened into one folder name that keeps enough of its
/// own shape to stay distinguishable, because the alternative is two different
/// trees writing over each other's report.
///
/// # Errors
///
/// Returns an error when the folder cannot be created.
pub(crate) fn project_dir(workspace: &Path) -> std::io::Result<PathBuf> {
    let parts: Vec<String> = workspace
        .components()
        .map(|component| component.as_os_str().to_string_lossy().into_owned())
        .filter(|part| !part.is_empty() && part != "." && part != "workspace")
        .map(|part| clean(&part))
        .filter(|part| !part.is_empty())
        .collect();
    let directory = if workspace.is_absolute() {
        // One folder rather than a mirror of the whole filesystem: an absolute
        // path's leading components say where the machine keeps things, not
        // which project this is.
        Path::new(REPORTS_ROOT).join(join_or_default(&parts))
    } else {
        parts
            .iter()
            .fold(PathBuf::from(REPORTS_ROOT), |path, part| path.join(part))
    };
    let directory = if directory == Path::new(REPORTS_ROOT) {
        directory.join("workspace")
    } else {
        directory
    };
    std::fs::create_dir_all(&directory)?;
    Ok(directory)
}

/// Writes one report file, creating its parent.
///
/// # Errors
///
/// Returns an error when the directory cannot be created or the file written.
pub(crate) fn write(path: &Path, report: &str) -> std::io::Result<()> {
    if let Some(parent) = path.parent() {
        std::fs::create_dir_all(parent)?;
    }
    std::fs::write(path, report)
}

/// Replaces anything that is not safe in a path component.
fn clean(part: &str) -> String {
    part.chars()
        .map(|character| {
            if character.is_ascii_alphanumeric() || character == '-' || character == '_' {
                character
            } else {
                '-'
            }
        })
        .collect::<String>()
        .trim_matches('-')
        .to_string()
}

/// Joins parts into one folder name, or names the fallback.
fn join_or_default(parts: &[String]) -> String {
    if parts.is_empty() {
        "workspace".to_string()
    } else {
        parts.join("-")
    }
}
