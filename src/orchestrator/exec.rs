//! The shell tool the code-writing roles run their programs through, and the
//! gate that decides whether a declared method is tractable enough to run.
//!
//! Lifted out of `mod.rs`, which had grown to hold the registry, the prompt
//! assembly, the path checks, and this. What belongs together here is one
//! thing: everything that decides what a run is allowed to execute, and what it
//! is told about how the execution went.

use std::path::PathBuf;
use std::time::Duration;

use async_trait::async_trait;
use serde_json::json;

use super::capture::Capture;
use super::{layout, string_argument};
use crate::agent::{Result, Tool, ToolCall, ToolResult, ToolSchema};

/// How much of one stream's output reaches the model.
///
/// This is a *memory* bound as well as a context bound, which is the point.
/// It used to be neither: the drains read each pipe to its end into an
/// unbounded `Vec` and this limit was applied afterwards, so a program printing
/// in a loop was charged against the container's memory in full and only then
/// shortened. The container has a hard `mem_limit`, and an OOM kill is the
/// worst failure shape available here — the kernel stops the process, nothing
/// reaches the console, and everything in flight is lost. Raising the limit
/// treated the symptom; the middle of the stream is now dropped as it arrives.
pub(super) const MAX_COMMAND_OUTPUT_BYTES: usize = 64 * 1024;

/// Where every command's output is written, so that running a program leaves
/// something behind.
///
/// What a command printed used to reach the model and nothing else. A live run
/// executed `phi_padic_closure_all.py` in 126 ms for 1,766 bytes of output and
/// `benchmark.py` for 463 more, read both, and left `code/out/` untouched —
/// five babysitting passes watched `code files` climb 36 → 44 while `captured
/// output` sat at 17. Two directives asked the run to redirect its own output
/// and neither changed the behaviour, which is the repository's own maxim
/// arriving on schedule: a prompt instruction is not a control.
///
/// It matters because the attempt ends at a cap. `DEFAULT_RUN_MINUTES` stops
/// the agent thirty minutes in and takes its context with it, so output that
/// existed only in that context is destroyed — the program ran, the number was
/// computed, and the next attempt has no way to know it. Writing here costs one
/// append per command and makes the evidence outlive the attempt that produced
/// it.
const COMMAND_LOG: &str = "code/out/commands.log";

/// How much of one command's output the log keeps.
///
/// Smaller than [`MAX_COMMAND_OUTPUT_BYTES`] on purpose: the model gets the
/// full rendering, and the log is the record that has to stay readable and
/// committable. A program worth more than this should write its own file.
const COMMAND_LOG_ENTRY_BYTES: usize = 8 * 1024;

/// How large the log is allowed to get before its oldest entries are dropped.
///
/// Workspace contents are committed, so an append-only file with no ceiling
/// becomes the thing this repository already refuses to keep. Trimming happens
/// at an entry boundary and from the front, because the most recent run is the
/// one the next attempt needs.
const COMMAND_LOG_MAX_BYTES: usize = 512 * 1024;

/// Separates entries in [`COMMAND_LOG`], and is where a trim cuts.
const COMMAND_LOG_MARK: &str = "\n=== command ===\n";

/// How long the pipe drains are given to finish after the child is killed.
///
/// Killing the child closes the pipes it holds, and that is what ends the
/// reads — but only when the child is the last process holding them. A command
/// that forks leaves descendants with the same write ends inherited, and a read
/// waiting on those never returns. The process group is signalled for exactly
/// that reason, and this bound is the second line: whatever survives being
/// signalled, the tool still answers rather than hanging past its own ceiling
/// on a pipe nobody will close.
const DRAIN_GRACE: Duration = Duration::from_secs(5);

/// Awaits one drain, giving up on it rather than waiting for it.
///
/// A drain that times out or whose task died leaves an empty capture, so the
/// tool still reports the command's status. The alternative is holding the tool
/// open on a descendant that survived the signal, which is the failure
/// [`DRAIN_GRACE`] exists to bound.
async fn drained(task: tokio::task::JoinHandle<Capture>) -> Capture {
    tokio::time::timeout(DRAIN_GRACE, task)
        .await
        .ok()
        .and_then(std::result::Result::ok)
        .unwrap_or_else(|| Capture::bounded(MAX_COMMAND_OUTPUT_BYTES))
}

/// Reads a pipe to its end, keeping a bounded window of what it carried.
async fn drain<R: tokio::io::AsyncRead + Unpin>(pipe: &mut Option<R>) -> Capture {
    use tokio::io::AsyncReadExt;
    let mut capture = Capture::bounded(MAX_COMMAND_OUTPUT_BYTES);
    let Some(pipe) = pipe.as_mut() else {
        return capture;
    };
    // Read into a fixed scratch buffer and fold each chunk into the window.
    // The stream is still consumed in full — a program that keeps printing
    // keeps running rather than blocking on a pipe nobody is emptying — but
    // only the two ends are retained.
    let mut buffer = vec![0_u8; 32 * 1024];
    while let Ok(read) = pipe.read(&mut buffer).await {
        if read == 0 {
            break;
        }
        capture.push(&buffer[..read]);
    }
    capture
}

#[derive(Debug)]
pub(super) struct ExecuteCommand {
    workspace: PathBuf,
    timeout: Duration,
}

/// What a command printed, and how it ended.
///
/// `status` is `None` when the command hit the ceiling and was killed, which
/// is why this exists instead of `std::process::Output`: that type cannot
/// represent a process with output but no exit status.
#[derive(Debug)]
struct CommandOutput {
    stdout: Capture,
    stderr: Capture,
    status: Option<std::process::ExitStatus>,
}

impl ExecuteCommand {
    pub(super) fn new(workspace: PathBuf, timeout: Duration) -> Self {
        Self { workspace, timeout }
    }

    /// Runs one command, keeping what it printed even if it has to be killed.
    ///
    /// `Command::output()` inside a `timeout` discards everything on expiry:
    /// the future is dropped mid-read, so a program that printed nine minutes
    /// of progress and then hit the ceiling returned the agent nothing but
    /// `command timed out`. Two such commands cost one live run twenty of its
    /// first forty-four minutes and taught it nothing either time — it could
    /// not tell a program that was nearly done from one that had not got past
    /// its first loop, so it had no basis for choosing a smaller bound.
    ///
    /// So the pipes are drained by their own tasks, and whatever arrived before
    /// the ceiling is returned with the timeout reported as the exit status
    /// rather than as an error. A timeout is evidence about the method, and
    /// evidence belongs in the result.
    ///
    /// The child is started in its own process group and the *group* is
    /// signalled. Killing the child alone was enough only while the child was
    /// the last process holding the pipes: `sh -lc "python x.py"` execs, so
    /// there is nothing else, but a pipeline, a background `&`, or anything
    /// using `multiprocessing` leaves descendants with the write ends
    /// inherited. Those keep the reads alive after the shell is gone, so the
    /// drains never finish and the tool hangs well past its own ceiling — and
    /// in a container with a `pids_limit`, the orphans go on consuming the
    /// run's budget for the rest of it.
    async fn run(&self, command: &str) -> Result<CommandOutput> {
        let mut process = tokio::process::Command::new("/bin/sh");
        let mut child = process
            .arg("-lc")
            .arg(command)
            // Its own group, so the whole tree can be signalled at once.
            .process_group(0)
            .current_dir(&self.workspace)
            .kill_on_drop(true)
            .stdout(std::process::Stdio::piped())
            .stderr(std::process::Stdio::piped())
            .spawn()
            .map_err(|error| {
                tinyagents::TinyAgentsError::Tool(format!("failed to execute command: {error}"))
            })?;
        let group = child.id();
        let mut out = child.stdout.take();
        let mut err = child.stderr.take();
        let reading_out = tokio::spawn(async move { drain(&mut out).await });
        let reading_err = tokio::spawn(async move { drain(&mut err).await });
        let finished = tokio::time::timeout(self.timeout, child.wait()).await;
        if finished.is_err() {
            let _ = child.kill().await;
            kill_group(group).await;
        }
        // Bounded so a descendant that survived the signal — one that changed
        // its own process group, or is stuck in uninterruptible I/O — cannot
        // hold the tool open indefinitely. What was read by then is the result.
        let stdout = drained(reading_out).await;
        let stderr = drained(reading_err).await;
        let status = match finished {
            Ok(Ok(status)) => Some(status),
            Ok(Err(error)) => {
                return Err(tinyagents::TinyAgentsError::Tool(format!(
                    "failed to execute command: {error}"
                )));
            }
            Err(_) => None,
        };
        Ok(CommandOutput {
            stdout,
            stderr,
            status,
        })
    }

    /// Appends one command and what it printed to [`COMMAND_LOG`].
    ///
    /// Best-effort on purpose. The command has already run and its result is
    /// the thing the caller asked for, so a workspace that cannot be written
    /// costs the record rather than the result.
    async fn record(&self, command: &str, status: &str, stdout: &str, stderr: &str) {
        let entry = format!(
            "{COMMAND_LOG_MARK}$ {command}\nexit: {status}\nstdout:\n{}\nstderr:\n{}\n",
            clipped(stdout),
            clipped(stderr)
        );
        let path = self.workspace.join(COMMAND_LOG);
        let Some(parent) = path.parent() else {
            return;
        };
        if tokio::fs::create_dir_all(parent).await.is_err() {
            return;
        }
        let existing = tokio::fs::read_to_string(&path).await.unwrap_or_default();
        let _ = tokio::fs::write(&path, trimmed(existing + &entry)).await;
    }
}

/// Signals every process in a timed-out command's group.
///
/// Spawned as `kill` rather than called through `libc`, because the crate
/// forbids `unsafe` and a process-group signal has no safe binding in `std`.
/// The cost is one short-lived process on a path that only runs when a command
/// has already burned its whole ceiling; the alternative is a `libc` dependency
/// whose only use is an `unsafe` block this crate does not permit.
///
/// Best effort throughout. The child has already been killed on its own by the
/// caller, so a failure here leaves orphans rather than a live command, and
/// turning that into a tool error would replace a usable partial result with
/// nothing.
async fn kill_group(group: Option<u32>) {
    let Some(group) = group else {
        return;
    };
    let _ = tokio::process::Command::new("kill")
        .arg("-KILL")
        .arg("--")
        .arg(format!("-{group}"))
        .stdout(std::process::Stdio::null())
        .stderr(std::process::Stdio::null())
        .status()
        .await;
}

#[async_trait]
impl Tool<()> for ExecuteCommand {
    fn name(&self) -> &'static str {
        "execute_command"
    }

    fn description(&self) -> &'static str {
        "Runs one shell command in /workspace inside the jailed container."
    }

    fn schema(&self) -> ToolSchema {
        ToolSchema::new(
            self.name(),
            self.description(),
            json!({
                "type": "object",
                "properties": {
                    "command": { "type": "string", "description": "Shell command to run from /workspace." },
                    "complexity": {
                        "type": "string",
                        "description": "Time and space complexity, both polynomial or better \
                                        unless this is a bounded oracle."
                    },
                    "complexity_class": {
                        "type": "string",
                        "enum": [
                            "constant", "logarithmic", "linear", "quasilinear", "polynomial",
                            "exponential", "factorial"
                        ],
                        "description": "Worst of the command's time and space complexity \
                                        classes. Declare it honestly: `exponential` and \
                                        `factorial` are allowed only for a brute-force oracle \
                                        and only with `oracle_bound` set."
                    },
                    "oracle_bound": {
                        "type": "string",
                        "description": "Required when the class is exponential or factorial: \
                                        the concrete input bound that keeps this run small, \
                                        such as `n <= 7`. A brute-force oracle validating the \
                                        real method on small instances is legitimate; the real \
                                        method itself must still be polynomial or better."
                    }
                },
                "required": ["command", "complexity", "complexity_class"],
                "additionalProperties": false
            }),
        )
    }

    async fn call(&self, _state: &(), call: ToolCall) -> Result<ToolResult> {
        let command = string_argument(&call, "command")?;
        let complexity = string_argument(&call, "complexity")?;
        let complexity_class = string_argument(&call, "complexity_class")?;
        let oracle_bound = string_argument(&call, "oracle_bound").ok();
        validate_complexity(&complexity, &complexity_class, oracle_bound.as_deref())?;
        let output = self.run(&command).await?;
        let stdout = output.stdout.render();
        let stderr = output.stderr.render();
        let status = match output.status {
            Some(status) => status
                .code()
                .map_or_else(|| "signal".to_string(), |code| code.to_string()),
            None => format!(
                "timed out after {} seconds, killed. The output above is what it had printed by \
                 then — read it for how far the computation got, and run a smaller instance \
                 rather than the same one again",
                self.timeout.as_secs()
            ),
        };
        self.record(&command, &status, &stdout, &stderr).await;
        // File anything the command wrote through the shell. `layout::placed`
        // covers the write path; a heredoc and a redirect go round it, and
        // that is how a root fills up during a run.
        let swept = layout::swept_note(&layout::sweep(&self.workspace).await);
        Ok(ToolResult::text(
            call.id,
            self.name(),
            format!("exit: {status}\nstdout:\n{stdout}\nstderr:\n{stderr}{swept}"),
        ))
    }
}

/// Shortens one stream for [`COMMAND_LOG`], keeping the end.
///
/// The tail is what a program's conclusion is in, which is the same reason
/// [`TAIL_BUDGET`] is the larger share of what reaches the model.
fn clipped(text: &str) -> String {
    if text.len() <= COMMAND_LOG_ENTRY_BYTES {
        return text.to_string();
    }
    let cut = text
        .char_indices()
        .map(|(at, _)| at)
        .find(|at| text.len() - at <= COMMAND_LOG_ENTRY_BYTES)
        .unwrap_or(text.len());
    format!("[earlier output dropped]\n{}", &text[cut..])
}

/// Drops whole entries from the front of the log until it fits.
///
/// Cutting at [`COMMAND_LOG_MARK`] rather than at a byte offset keeps every
/// entry that survives readable, and keeps the file valid UTF-8 whatever a
/// program printed.
fn trimmed(log: String) -> String {
    if log.len() <= COMMAND_LOG_MAX_BYTES {
        return log;
    }
    let over = log.len() - COMMAND_LOG_MAX_BYTES;
    match log.match_indices(COMMAND_LOG_MARK).find(|(at, _)| *at >= over) {
        Some((at, _)) => log[at..].to_string(),
        // One entry larger than the whole ceiling: keep it and let the next
        // append trim, rather than returning a fragment cut mid-character.
        None => log,
    }
}

/// Rejects an intractable method while allowing a deliberately bounded oracle.
///
/// The gate used to refuse every declared exponential cost, and the schema
/// offered no honest way to say so. That produced the opposite of what it was
/// for. A tool-builder that truthfully declared a naive minimax as exponential
/// was refused and could not write the oracle the method policy requires as its
/// first step; another, running a genuinely factorial search over all `n!`
/// permutations twice nested, wrote `polynomial (O((n!)²))` in the free-text
/// field and sailed through, because the forbidden list looked for `o(n!` and
/// the parenthesis did not match. The gate punished accuracy and was defeated
/// by punctuation.
///
/// So exponential and factorial are declarable, and legitimate only with a
/// concrete `oracle_bound` — brute force validating the real method on small
/// instances, which the method policy has always called for. What stays
/// prohibited is the thing that was meant to be: an intractable *method*,
/// unbounded. A declaration whose class and prose disagree is refused, because
/// that mismatch is how the old gate was evaded.
///
/// # Errors
///
/// Returns a validation error when the class is not one the schema offers, when
/// an intractable class carries no `oracle_bound`, when the declared prose and
/// the declared class disagree, or when the prose names an unbounded search
/// strategy rather than a cost.
pub(super) fn validate_complexity(
    complexity: &str,
    complexity_class: &str,
    oracle_bound: Option<&str>,
) -> Result<()> {
    let intractable = matches!(complexity_class, "exponential" | "factorial");
    if !intractable
        && !matches!(
            complexity_class,
            "constant" | "logarithmic" | "linear" | "quasilinear" | "polynomial"
        )
    {
        return Err(tinyagents::TinyAgentsError::Validation(
            "complexity class must be polynomial or better".into(),
        ));
    }
    let normalized = complexity.to_ascii_lowercase().replace(' ', "");
    let forbidden = [
        "exponential",
        "factorial",
        "o(2^",
        "o(2**",
        "n!",
        "2^n",
        "2**n",
    ];
    let claims_intractable = forbidden.iter().any(|term| normalized.contains(term));
    // A bounded oracle is legitimate however it searches, and says so with
    // `oracle_bound`. Only an unbounded search reaches the refusal.
    let bounded = oracle_bound
        .map(str::trim)
        .is_some_and(|bound| !bound.is_empty());
    if intractable {
        if !bounded {
            return Err(tinyagents::TinyAgentsError::Validation(
                "an exponential or factorial command is allowed only as a brute-force oracle: \
                 set oracle_bound to the concrete input bound that keeps this run small, such \
                 as `n <= 7`. The real method must still be polynomial or better"
                    .into(),
            ));
        }
        return Ok(());
    }
    if claims_intractable {
        return Err(tinyagents::TinyAgentsError::Validation(
            "the stated complexity is exponential or factorial but the class says otherwise: \
             declare complexity_class as exponential or factorial and set oracle_bound if this \
             is a bounded oracle, or choose a polynomial formulation"
                .into(),
        ));
    }
    if !bounded
        && SEARCH_METHODS
            .iter()
            .any(|method| normalized.contains(method))
    {
        return Err(tinyagents::TinyAgentsError::Validation(
            "this names a search strategy rather than a cost, and a search over candidate \
             solutions is what the method policy prohibits. If it is the bounded oracle of rule \
             8, set oracle_bound to the input bound that keeps it small. If it is the real \
             method, state what a solution *is* and hand the search to an engine: delegate to \
             sat_solver, which encodes a finite decision or optimisation problem for CP-SAT, \
             SAT, or MILP. Otherwise give the actual complexity of a polynomial formulation"
                .into(),
        ));
    }
    Ok(())
}

/// Search strategies over candidate solutions, matched in the declared prose.
///
/// The gate asked for a cost and never checked it was one. A live run on
/// Project Euler 185 — sixteen digits, so ten quadrillion candidates, and the
/// one problem in the archive where CP-SAT is the canonical method — declared
/// `complexity: "backtracking with pruning"` against `complexity_class:
/// "polynomial"` and was allowed through. That string names a method and
/// states no bound at all, so neither the class check nor the notation check
/// had anything to catch: the forbidden list looks for `2^n` and `n!`, and
/// prose that mentions no quantity contains neither.
///
/// This is the third form of the same evasion the rest of this function
/// documents, and it is caught the same way: mechanically, at the point of
/// execution, rather than by asking a prompt to be believed. The role that
/// exists for exactly this is `sat_solver`, and the refusal names it, because
/// a gate that blocks the wrong method without pointing at the right one costs
/// the run a turn to rediscover.
///
/// The list is deliberately four unambiguous terms. `enumerate` is not among
/// them: "enumerate the divisors of n" is an honest description of an
/// `O(√n)` method, and a gate that refused it would punish accuracy, which is
/// the failure this function was rewritten once already to stop doing. Each
/// term here essentially never describes a polynomial method that is not a
/// bounded oracle — and a bounded oracle declares `oracle_bound` and never
/// reaches this check.
const SEARCH_METHODS: [&str; 5] = [
    "backtrack",
    "bruteforce",
    "brute-force",
    "branchandbound",
    "exhaustive",
];

#[cfg(test)]
#[path = "exec_test.rs"]
mod test;
