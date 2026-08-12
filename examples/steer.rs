//! Queues one directive for a run that is already going.
//!
//! Runs on the host, like `dump_prompts`: it appends a line to the workspace
//! the container has mounted, so it needs neither the container, nor a provider
//! key, nor anything opened into the sandbox. The run picks the directive up on
//! its own schedule and never waits for it, which is why this exits as soon as
//! the line is written rather than reporting what the run did with it — that
//! goes to `config/DIRECTIVES.md`.
//!
//! ```sh
//! cargo run --example steer -- workspace/project-euler/763 "check the n=14 bound"
//! ```
//!
//! Use `./steer` rather than this directly; it resolves the workspace and
//! refuses traversal first.

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut arguments = std::env::args().skip(1);
    let (Some(workspace), Some(text)) = (arguments.next(), arguments.next()) else {
        return Err("usage: steer <workspace-path> <directive>".into());
    };
    let path = std::path::Path::new(&workspace);
    if !path.is_dir() {
        return Err(format!("workspace `{workspace}` is not a directory").into());
    }
    let directive = math_agent::directives::enqueue(path, "steer", &text)?;
    println!(
        "queued directive {} for {workspace}\nthe run picks it up on its next director cycle; \
         what it did goes to config/DIRECTIVES.md",
        directive.id
    );
    Ok(())
}
