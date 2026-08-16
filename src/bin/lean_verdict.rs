//! Runs the Lean kernel over one workspace file and prints the verdict.
//!
//! ```sh
//! lean-verdict /workspace code/lean/link_a.lean
//! lean-verdict /workspace code/lean/link_a.lean --json
//! ```
//!
//! This exists so a `.lean` file can be checked from outside a run. Lean and a
//! prebuilt Mathlib are in the runtime image and nowhere else, so before this
//! binary the only way to learn whether a formalisation compiled was to start
//! an agent and ask it — which made the 78 `.lean` files past runs produced
//! unscoreable, and made iterating on one cost a model call.
//!
//! It is a second caller of `math_agent::check_lean_file`, not a second
//! implementation of it. Writing the verdict logic again in shell would be a
//! second answer to *what counts as verified*, and the whole value of the
//! kernel check is that there is exactly one.
//!
//! **This binary never writes a verdict, and that is a control rather than a
//! default.** `code/out/lean/` is what `research/CLAIMS.md` consults before it
//! will record a claim as formalised, and the only thing that may write there is
//! the `lean_check` tool.
//!
//! It was briefly given a `--file-verdict` flag, and a live run found the hole
//! within thirteen minutes: this binary ships in the runtime image, so
//! `execute_command` can call it, and a role that could pass that flag could
//! file its own evidence without going through the tool that grants it. The
//! flag was speculative — no caller needed it — and every env-var gate that
//! might have guarded it is settable from the same shell. Removing the
//! capability is the only version of this that is not a prompt instruction.
//!
//! A role reaching this from the shell is fine and is not new: `execute_command`
//! could always run `lean` directly. What it gets is a verdict it can read and
//! cannot file, which is exactly the arrangement `lean_prover.md` describes.
//!
//! What Lean printed is included under the verdict, because the verdict alone
//! cannot be acted on: it says a file did not compile, and the error text says
//! which goal is left after which tactic. `--json` prints the record instead,
//! for a caller that is counting rather than reading.
//!
//! The exit code is the verdict: `0` verified, `1` failed, `2` conditional —
//! proved, but resting on axioms cited from the literature. Three codes rather
//! than two because a caller looping over a tree has to be able to separate
//! them without parsing prose, and rounding conditional to either neighbour
//! loses the distinction the status exists for.

use std::path::PathBuf;
use std::process::ExitCode;
use std::time::Duration;

use math_agent::LeanOutcome;

/// How long one file gets. Generous next to a tool call's ceiling, because a
/// Mathlib-importing file elaborates for tens of seconds before it says
/// anything and a replay over a whole tree should not report a slow file as a
/// broken one.
const TIMEOUT: Duration = Duration::from_mins(10);

/// What the command line asked for.
struct Args {
    /// The workspace root every path is resolved against.
    workspace: PathBuf,
    /// The workspace-relative `.lean` file to check.
    file: String,
    /// Print the JSON record rather than the prose report.
    json: bool,
}

/// Reads the command line, or explains itself.
fn parse() -> Option<Args> {
    let mut positional: Vec<String> = Vec::new();
    let mut json = false;
    for argument in std::env::args().skip(1) {
        match argument.as_str() {
            "--json" => json = true,
            "-h" | "--help" => return None,
            other if other.starts_with('-') => {
                eprintln!("unknown flag: {other}");
                return None;
            }
            other => positional.push(other.to_string()),
        }
    }
    let [workspace, file] = positional.as_slice() else {
        return None;
    };
    Some(Args {
        workspace: PathBuf::from(workspace),
        file: file.clone(),
        json,
    })
}

fn main() -> ExitCode {
    let Some(args) = parse() else {
        eprintln!(
            "usage: lean-verdict <workspace> <file.lean> [--json]\n\
             \n\
             Runs the Lean kernel over one workspace-relative .lean file and reports\n\
             what it found. It never writes a verdict; only the lean_check tool does.\n\
             \n\
               --json  print the JSON record instead of the prose report\n\
             \n\
             exit: 0 verified, 1 failed, 2 conditional (proved given cited axioms)"
        );
        return ExitCode::FAILURE;
    };

    let runtime = match tokio::runtime::Builder::new_current_thread()
        .enable_all()
        .build()
    {
        Ok(runtime) => runtime,
        Err(error) => {
            eprintln!("failed to start the runtime: {error}");
            return ExitCode::FAILURE;
        }
    };

    let checked = runtime.block_on(math_agent::check_lean_file(
        &args.workspace,
        &args.file,
        TIMEOUT,
        // Never. See the header: this binary is in the runtime image, so a flag
        // that let it file evidence would be a flag `execute_command` could pass.
        false,
    ));

    let (verdict, output) = match checked {
        Ok(checked) => checked,
        Err(error) => {
            eprintln!("{error}");
            return ExitCode::FAILURE;
        }
    };

    if args.json {
        println!("{}", verdict.to_json());
    } else {
        print!("{}", verdict.to_report());
        // Lean's own output, and not only when the check failed. A file that
        // compiled can still have printed a warning worth reading, and a caller
        // that has to pass a flag to see why something broke will read the
        // verdict and guess instead.
        if !output.trim().is_empty() {
            println!("\nlean output:\n{output}");
        }
    }

    match verdict.verdict() {
        LeanOutcome::Verified => ExitCode::SUCCESS,
        LeanOutcome::Conditional => ExitCode::from(2),
        LeanOutcome::Failed => ExitCode::FAILURE,
    }
}
