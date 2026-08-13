//! Draws the solution loop to an image file.
//!
//! ```sh
//! cargo run --features graph-debug --bin graph-render -- solution-loop.png
//! ```
//!
//! Separate from `euler-tui` because the two watch different things: the viewer
//! shows one live run's traffic, and this shows the fixed shape that traffic
//! moves through. Nothing here reads a workspace or a container, so it is safe
//! to run while a solve is in progress.

fn main() -> std::process::ExitCode {
    let Some(path) = std::env::args().nth(1) else {
        eprintln!("usage: graph-render <output.png|.jpg|.jpeg>");
        return std::process::ExitCode::FAILURE;
    };
    match math_agent::render_solution_loop(&path) {
        Ok(()) => {
            println!("wrote {path}");
            std::process::ExitCode::SUCCESS
        }
        Err(error) => {
            eprintln!("{error}");
            std::process::ExitCode::FAILURE
        }
    }
}
