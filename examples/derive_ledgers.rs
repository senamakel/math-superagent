//! Prints the statement graph and the entailment closure a workspace implies.
//!
//! Both are derived from files a run wrote, so what they conclude can be
//! checked on the host against a real workspace rather than only against a
//! fixture — without a container, an API key, or spending anything.
//!
//! ```sh
//! cargo run --example derive_ledgers -- workspace/project-euler/351
//! ```

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let workspace = std::env::args()
        .nth(1)
        .unwrap_or_else(|| "workspace/template".to_string());
    let path = std::path::Path::new(&workspace);
    if !path.is_dir() {
        return Err(format!("workspace `{workspace}` is not a directory").into());
    }
    println!("{}", math_agent::ledger_report(path));
    Ok(())
}
