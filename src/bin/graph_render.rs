//! Draws this crate's flows to image files.
//!
//! ```sh
//! cargo run --features graph-debug --bin graph-render -- diagrams/
//! cargo run --features graph-debug --bin graph-render -- solution-loop.png
//! ```
//!
//! A directory gets every flow, one `<name>.png` each; a path ending in an image
//! extension gets the solution loop alone. Both spellings exist because the two
//! questions are different — "show me the shape of everything" and "redraw the
//! one I am editing" — and the second is the one run in a loop while working.
//!
//! Separate from `euler-tui` because the two watch different things: the viewer
//! shows one live run's traffic, and this shows the fixed shape that traffic
//! moves through. Nothing here reads a workspace or a container, so it is safe
//! to run while a solve is in progress.

/// The extensions the renderer writes, and therefore what marks an argument as a
/// single file rather than a directory.
const IMAGE: [&str; 3] = ["png", "jpg", "jpeg"];

fn main() -> std::process::ExitCode {
    let Some(path) = std::env::args().nth(1) else {
        eprintln!("usage: graph-render <directory | output.png|.jpg|.jpeg>");
        return std::process::ExitCode::FAILURE;
    };
    // By extension rather than by asking the filesystem, so the two spellings
    // mean the same thing whether or not the target exists yet.
    let one_file = std::path::Path::new(&path)
        .extension()
        .and_then(std::ffi::OsStr::to_str)
        .is_some_and(|extension| IMAGE.contains(&extension.to_ascii_lowercase().as_str()));

    let written = if one_file {
        math_agent::render_solution_loop(&path).map(|()| vec![std::path::PathBuf::from(&path)])
    } else {
        math_agent::render_flows(&path)
    };

    match written {
        Ok(paths) => {
            for path in paths {
                println!("wrote {}", path.display());
            }
            std::process::ExitCode::SUCCESS
        }
        Err(error) => {
            eprintln!("{error}");
            std::process::ExitCode::FAILURE
        }
    }
}
