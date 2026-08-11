//! Prints every agent's assembled system prompt for inspection.
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
//! ```

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let workspace = std::env::args()
        .nth(1)
        .unwrap_or_else(|| "workspace/template".to_string());
    let path = std::path::Path::new(&workspace);
    if !path.is_dir() {
        return Err(format!("workspace `{workspace}` is not a directory").into());
    }
    println!("{}", math_agent::prompt_report(path)?);
    Ok(())
}
