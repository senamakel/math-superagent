//! Writes every agent's assembled system prompt to a file, for inspection.
//!
//! The prompts are the most consequential text in the runtime and were the
//! least reviewable part of it: assembled at startup from a built-in policy,
//! a role prompt, and whichever workspace files that role is entitled to, then
//! visible only in a provider trace after a run had already started. This
//! renders the same assembly on the host, without a container, an API key, or
//! spending anything.
//!
//! ```sh
//! cargo run --example dump_prompts -- workspace/template
//! cargo run --example dump_prompts -- workspace/conjectures/gilbreath
//! cargo run --example dump_prompts -- workspace/template --stdout | less
//! ```
//!
//! The report goes to `reports/prompts/<workspace>.md`, which is gitignored.
//! It is a rendering of state that already exists — the same argument that
//! keeps `derived/` out of a source directory — and it is large: a live
//! workspace assembles to half a megabyte across twenty-four roles, so
//! committing one would put a diff nobody can review into every batch.
//!
//! Naming the file after the workspace rather than the clock is deliberate.
//! The question this answers is *what does this workspace cost right now*, so
//! a second run on the same workspace should replace the first rather than
//! leave two files a reader has to date-check. Comparing two points in time is
//! what `git stash` and a second path are for.
//!
//! `--stdout` prints instead, for piping into a pager or a diff.

use std::path::{Path, PathBuf};

/// Where a report goes when it is not being piped.
const REPORTS_DIR: &str = "reports/prompts";

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut workspace: Option<String> = None;
    let mut to_stdout = false;
    for argument in std::env::args().skip(1) {
        match argument.as_str() {
            "--stdout" => to_stdout = true,
            other if other.starts_with("--") => {
                return Err(format!("unknown option `{other}`; the only one is `--stdout`").into());
            }
            other => workspace = Some(other.to_string()),
        }
    }
    let workspace = workspace.unwrap_or_else(|| "workspace/template".to_string());
    let path = Path::new(&workspace);
    if !path.is_dir() {
        return Err(format!("workspace `{workspace}` is not a directory").into());
    }

    let report = math_agent::prompt_report(path)?;
    if to_stdout {
        println!("{report}");
        return Ok(());
    }

    let destination = report_path(path);
    if let Some(parent) = destination.parent() {
        std::fs::create_dir_all(parent)?;
    }
    std::fs::write(&destination, &report)?;
    println!("{}", destination.display());
    // The closing line of the report carries the total and the count, which is
    // the one number somebody runs this to see. Printing it here saves opening
    // the file to answer *did that get better*.
    if let Some(summary) = report.lines().rev().find(|line| line.starts_with("_~")) {
        println!("{}", summary.trim_matches('_'));
    }
    Ok(())
}

/// The report path for `workspace`, named after the workspace it describes.
///
/// `workspace/conjectures/gilbreath` becomes
/// `reports/prompts/conjectures-gilbreath.md`. The leading `workspace/` is
/// dropped because every one of these has it, and the separators are flattened
/// so the reports sit in one directory a reader can list.
///
/// A path outside `workspace/` — a scratch copy, a fixture — keeps enough of
/// its own shape to stay distinguishable, which matters because the alternative
/// is two different trees writing the same file.
fn report_path(workspace: &Path) -> PathBuf {
    let slug: String = workspace
        .components()
        .map(|component| component.as_os_str().to_string_lossy().into_owned())
        .filter(|part| !part.is_empty() && part != "." && part != "workspace")
        .collect::<Vec<_>>()
        .join("-");
    let slug = slug
        .chars()
        .map(|character| {
            if character.is_ascii_alphanumeric() || character == '-' || character == '_' {
                character
            } else {
                '-'
            }
        })
        .collect::<String>();
    let slug = slug.trim_matches('-').to_string();
    Path::new(REPORTS_DIR).join(format!(
        "{}.md",
        if slug.is_empty() {
            "workspace".to_string()
        } else {
            slug
        }
    ))
}
