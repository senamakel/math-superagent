//! Writes the statement graph, the entailment closure, and what every derived
//! ledger costs a prompt.
//!
//! All of it is derived from files a run wrote, so what it concludes can be
//! checked on the host against a real workspace rather than only against a
//! fixture — without a container, an API key, or spending anything.
//!
//! ```sh
//! cargo run --example derive_ledgers -- workspace/conjectures/gilbreath
//! cargo run --example derive_ledgers -- workspace/project-euler/351 --stdout
//! ```
//!
//! The report goes to `reports/<project>/ledgers.md`, beside that project's
//! `prompts/` folder, and `/reports/` is gitignored. It stays one file where
//! the prompts are split per agent: this is a single argument — the graph, what
//! it entails, and what carrying it costs — and splitting it would separate the
//! cost table from the ledgers it prices. `--stdout` prints instead.

mod common;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let options = common::options("workspace/template")?;
    let path = std::path::Path::new(&options.workspace);
    if !path.is_dir() {
        return Err(format!("workspace `{}` is not a directory", options.workspace).into());
    }

    let report = math_agent::ledger_report(path);
    if options.to_stdout {
        println!("{report}");
        return Ok(());
    }

    let destination = common::project_dir(path)?.join("ledgers.md");
    common::write(&destination, &report)?;
    println!("{}", destination.display());
    // The two verdict lines at the top and the cost total at the bottom, which
    // between them are why somebody runs this: whether the argument closes, and
    // what carrying it costs every prompt that does.
    for line in report.lines() {
        if line.starts_with("statement graph:")
            || line.starts_with("entailment:")
            || line.starts_with("| **total**")
        {
            println!("{line}");
        }
    }
    Ok(())
}
