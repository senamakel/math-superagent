//! Moves each named workspace's rendered ledgers from `research/` into
//! `derived/`.
//!
//! A run migrates its own workspace at startup, so this is for the workspaces
//! nobody has started since `derived/` existed. Leaving one is not a loud
//! failure: the prompts route `derived/CLAIMS.md`, `load_workspace_files` skips
//! a path that is not there, and the role is quietly told less than it should
//! be. Running this is cheaper than noticing that.
//!
//! Takes any number of workspace paths and reports every move, workspace by
//! workspace. It never overwrites, so running it twice is safe and the second
//! run moves nothing.
//!
//! ```sh
//! cargo run --example migrate_derived -- workspace/project-euler/351
//! cargo run --example migrate_derived -- workspace/conjectures/*
//! ```

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let workspaces: Vec<String> = std::env::args().skip(1).collect();
    if workspaces.is_empty() {
        return Err("usage: migrate_derived <workspace>...".into());
    }
    let mut total = 0_usize;
    for workspace in &workspaces {
        let path = std::path::Path::new(workspace);
        if !path.is_dir() {
            return Err(format!("workspace `{workspace}` is not a directory").into());
        }
        let moved = math_agent::migrate_derived(path);
        total += moved.len();
        if moved.is_empty() {
            println!("{workspace}: nothing to move");
            continue;
        }
        println!("{workspace}: moved {}", moved.len());
        for entry in moved {
            println!("  {entry}");
        }
    }
    println!(
        "\n{total} file(s) moved across {} workspace(s)",
        workspaces.len()
    );
    Ok(())
}
