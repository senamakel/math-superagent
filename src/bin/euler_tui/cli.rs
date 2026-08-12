/// What the client should do: watch a live run, or read a finished one's log.
///
/// A mode rather than a pair of booleans, because they were never independent
/// — `--replay --attach` has no meaning, and a struct of flags invites the
/// caller to ask about a combination that cannot happen.
#[derive(Debug, Clone, Copy, PartialEq, Eq, Default)]
enum Mode {
    /// Follow the container running this workspace.
    #[default]
    Attach,
    /// Read the existing log; touch nothing.
    Replay,
}

/// The parsed command line.
///
/// The workspace is the identity, not the problem number. A Euler problem is
/// named by its number and lives at `project-euler/<n>`, but a run against an
/// open conjecture lives anywhere under `workspace/`, and a viewer that can
/// only spell one of those cannot watch the other.
#[derive(Debug)]
struct Options {
    /// Path relative to `workspace/`.
    workspace: String,
    /// What to call it on screen and in an error.
    label: String,
    mode: Mode,
    plain: bool,
}

fn usage() -> String {
    "usage: ./euler-tui [--replay] [--plain] <problem>\n\
     \x20      ./euler-tui [--replay] [--plain] --workspace <relative/path>\n\
     \n\
     Watches a run; it never starts one. Start a run with `./euler <problem>`\n\
     or `./conjecture <slug>`.\n\
     \n\
       --replay  open the tabs on the existing log instead of a live container\n\
       --plain   no tabs; stream to stdout, as when scripting"
        .to_string()
}

fn options() -> Result<Options, String> {
    let mut workspace: Option<String> = None;
    let mut label = String::new();
    let mut mode = Mode::default();
    let mut plain = false;
    let mut expecting_workspace = false;
    for argument in std::env::args().skip(1) {
        if expecting_workspace {
            expecting_workspace = false;
            if argument.contains("..") || argument.starts_with('/') {
                return Err("workspace must be a relative path without traversal".to_string());
            }
            label.clone_from(&argument);
            workspace = Some(argument);
            continue;
        }
        match argument.as_str() {
            // Accepted and ignored: it was the only mode long enough that a
            // hand still types it, and refusing a flag that asks for what
            // already happens would be pedantry.
            "--attach" => mode = Mode::Attach,
            "--plain" => plain = true,
            "--replay" => mode = Mode::Replay,
            "--workspace" => expecting_workspace = true,
            "-h" | "--help" => return Err(usage()),
            _ if workspace.is_none() => {
                let problem = argument
                    .parse::<u32>()
                    .map_err(|_| "problem number must be a positive integer".to_string())?;
                if problem == 0 {
                    return Err("problem number must be a positive integer".to_string());
                }
                label = format!("problem {problem}");
                workspace = Some(format!("project-euler/{problem}"));
            }
            _ => {
                return Err(format!(
                    "unexpected argument `{argument}`. This watches a run; start one with \
                     `./euler <problem>`"
                ));
            }
        }
    }
    if expecting_workspace {
        return Err("--workspace needs a path".to_string());
    }
    let workspace = workspace.ok_or_else(usage)?;
    Ok(Options {
        workspace,
        label,
        mode,
        plain,
    })
}

fn main() -> std::process::ExitCode {
    let options = match options() {
        Ok(options) => options,
        Err(message) => {
            eprintln!("{message}");
            return std::process::ExitCode::from(2);
        }
    };
    let root = match std::env::current_dir() {
        Ok(directory) => directory,
        Err(error) => {
            eprintln!("cannot read the working directory: {error}");
            return std::process::ExitCode::FAILURE;
        }
    };
    let workspace = root.join("workspace").join(&options.workspace);
    let log = workspace.join("config").join("console.log");
    let _ = std::fs::create_dir_all(workspace.join("config"));

    let runs = Arc::new(Mutex::new(Runs::new()));
    let tabs = !options.plain && std::io::IsTerminal::is_terminal(&std::io::stdout());
    let started = Instant::now();

    if options.mode == Mode::Replay {
        let Ok(text) = std::fs::read_to_string(&log) else {
            eprintln!("no log at {}", log.display());
            return std::process::ExitCode::FAILURE;
        };
        if let Ok(mut state) = runs.lock() {
            for line in text.lines() {
                state.add(line);
                if !tabs {
                    println!("{line}");
                }
            }
            state.ended = true;
        }
        // Replay has no run to direct: the log is a record of one that has
        // already finished, and a directive queued against it would sit
        // unread until somebody started a run on the same workspace and then
        // arrive as instruction from an hour ago.
        if tabs && let Err(error) = watch(&runs, started, None) {
            eprintln!("{error}");
            return std::process::ExitCode::FAILURE;
        }
        return std::process::ExitCode::SUCCESS;
    }

    let Some(container) = running_for(&workspace) else {
        eprintln!(
            "nothing is running for {label}.\n\
             Start it, then run this again to watch it, or add --replay to read\n\
             the last run's log at {log}.",
            label = options.label,
            log = log.display()
        );
        return std::process::ExitCode::FAILURE;
    };
    if let Ok(mut state) = runs.lock() {
        state.add(&format!("watching {container}, running {}", options.label));
    }

    let stop = Arc::new(AtomicBool::new(false));
    let reader = {
        let (runs, stop) = (Arc::clone(&runs), Arc::clone(&stop));
        let (workspace, log) = (workspace.clone(), log.clone());
        std::thread::spawn(move || follow(&workspace, Some(container), &runs, &log, !tabs, &stop))
    };

    if tabs {
        if let Err(error) = watch(&runs, started, Some(&workspace)) {
            eprintln!("{error}");
            return std::process::ExitCode::FAILURE;
        }
        // Nothing about the run is stopped on the way out. It is a detached
        // container and outlives every client, which is the point of attaching
        // rather than owning.
        stop.store(true, Ordering::Relaxed);
        eprintln!(
            "detached — the run continues. Re-attach with the same command, or `tail -f {}`",
            log.display()
        );
    } else {
        let _ = reader.join();
    }
    std::process::ExitCode::SUCCESS
}
