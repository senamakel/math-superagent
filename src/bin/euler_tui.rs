//! A tabbed console for one run, one tab per team.
//!
//! The runtime prints a single interleaved stream: eleven roles, several
//! concurrent child runs each, one line per model call, tool call, and tool
//! result. That is the right shape for a trace and the wrong one for watching
//! — in one live run a background agent alone produced 232 of the first 400 lines,
//! so the solve's own progress scrolled past between two index refreshes.
//!
//! This splits the stream by role without changing it. Every byte still lands
//! in a log file exactly as the runtime emitted it, so `grep` and the existing
//! `trace.jsonl` tooling keep working; the tabs are a view, not a filter, and
//! nothing is dropped from the record because a tab was not open.
//!
//! This cannot start, stop, or restart a run. That is not a missing feature,
//! it is the point. When starting was part of the same command, opening a
//! second view started a second run on the same workspace — both writing the
//! same files and both making checkpoint commits over each other — which
//! happened three times in one evening, twice unnoticed for several minutes. A
//! viewer that cannot launch cannot do that, and quitting it, closing the
//! terminal, or opening a second one is guaranteed to leave the run alone.
//!
//! It *can* direct a run that already exists. Pressing `i` opens a line, and
//! what is typed there is appended to the run's directive queue with
//! [`math_agent::directives::enqueue`]; the run picks it up on its own
//! schedule and never waits for one. That narrows the rule above without
//! touching what the rule was written to prevent: a directive creates no
//! container, and a queue file with nothing in it is a run nobody directed
//! rather than a second run nobody noticed. Sending is refused under
//! `--replay`, where there is no live run to direct, and unavailable under
//! `--plain`, which exists for scripting.
//!
//! Runs are started with `./euler <number>` or `./conjecture <slug>`, which is
//! one command in one place, so "is something already running for this
//! problem" has one answer rather than one per terminal. The workspace is the
//! identity here, not the problem number: a Euler run lives at
//! `project-euler/<n>` and everything else is named with `--workspace`.

use std::collections::BTreeMap;
use std::io::{BufRead, BufReader, Write};
use std::path::Path;
use std::process::{Command, Stdio};
use std::sync::atomic::{AtomicBool, Ordering};
use std::sync::{Arc, Mutex};
use std::time::{Duration, Instant};

use crossterm::event::{self, Event, KeyCode, KeyEventKind, KeyModifiers};
use crossterm::terminal::{EnterAlternateScreen, LeaveAlternateScreen};
use crossterm::{execute, terminal};
use ratatui::Terminal;
use ratatui::backend::CrosstermBackend;
use ratatui::layout::{Constraint, Direction, Layout};
use ratatui::style::{Color, Modifier, Style};
use ratatui::text::{Line, Span};
use ratatui::widgets::{Block, Borders, Paragraph, Tabs};

/// Lines every tab shows, whichever role emitted them.
///
/// The loop's verdicts are the run's spine: an attempt boundary, a judge
/// score, a reflection verdict, and a team ending are what change the run's
/// state, and nobody should have to be on the right tab to see one.
const PINNED: [&str; 2] = ["solution loop:", "team "];

/// Lines worth counting in the status bar, each naming a failure the runtime
/// is built to survive, so the counts answer "is this run healthy" without
/// opening a tab.
const COUNTED: [(&str, &str); 6] = [
    ("err", "error: tool error"),
    ("trunc", "TRUNCATED"),
    ("retry", "model RETRY"),
    ("reroute", "PROVIDER FAILED"),
    ("timeout", "timed out after"),
    ("filed", "filed from the workspace root"),
];

/// Lines kept per tab. The log file holds everything regardless, so this
/// bounds memory rather than history.
const SCROLLBACK: usize = 20_000;

/// How long to wait for a key before repainting. Below what a hand registers,
/// so a keypress lands immediately; the previous implementation polled every
/// 200ms and every keystroke waited up to a fifth of a second.
const POLL: Duration = Duration::from_millis(15);

/// How often to repaint when no key was pressed, so a quiet tab still shows
/// new lines without spending a frame on every poll.
const REFRESH: Duration = Duration::from_millis(200);

/// One team's tab: its name and the lines filed under it.
#[derive(Debug, Default)]
struct Tab {
    lines: Vec<String>,
}

impl Tab {
    fn push(&mut self, line: &str) {
        if self.lines.len() >= SCROLLBACK {
            self.lines.drain(..SCROLLBACK / 4);
        }
        self.lines.push(line.to_string());
    }
}

/// The stream, split by role, with the counters and the last reported cost.
#[derive(Debug, Default)]
struct Runs {
    /// Ordered so the tab bar keeps a stable position per team; `all` is
    /// first because it is the one a reader falls back to.
    order: Vec<String>,
    tabs: BTreeMap<String, Tab>,
    counts: BTreeMap<&'static str, usize>,
    elapsed: String,
    cost: String,
    ended: bool,
}

impl Runs {
    fn new() -> Self {
        let mut runs = Self::default();
        runs.tab("all");
        runs
    }

    fn tab(&mut self, name: &str) -> &mut Tab {
        if !self.tabs.contains_key(name) {
            self.order.push(name.to_string());
            self.tabs.insert(name.to_string(), Tab::default());
        }
        self.tabs.entry(name.to_string()).or_default()
    }

    /// Files one raw line, opening a tab the first time a role speaks.
    fn add(&mut self, raw: &str) {
        let line = raw.trim_end_matches(['\n', '\r']);
        self.tab("all").push(line);
        for (name, needle) in COUNTED {
            if line.contains(needle) {
                *self.counts.entry(name).or_default() += 1;
            }
        }
        if let Some(cost) = line.rsplit_once('$')
            && cost.1.chars().all(|c| c.is_ascii_digit() || c == '.')
            && !cost.1.is_empty()
        {
            self.cost = format!("${}", cost.1);
        }
        let Some((elapsed, who, _)) = parse(line) else {
            // A build line, a panic, a bare traceback: unparsed, but it still
            // belongs somewhere a reader will actually look.
            return;
        };
        self.elapsed = elapsed;
        let role = who.split('/').next().unwrap_or(&who).to_string();
        self.tab(&role).push(line);
        if PINNED.iter().any(|pin| line.contains(pin)) {
            let others: Vec<String> = self
                .order
                .iter()
                .filter(|name| *name != "all" && **name != role)
                .cloned()
                .collect();
            for name in others {
                self.tab(&name).push(line);
            }
        }
    }
}

/// Splits `[MM:SS] role/agent-run-N  rest` into its three parts.
///
/// The timestamp is elapsed run time rather than wall clock, and is kept
/// verbatim: it is what the console and `trace.jsonl` agree on when something
/// has to be found in both.
fn parse(line: &str) -> Option<(String, String, String)> {
    let rest = line.strip_prefix('[')?;
    let (elapsed, rest) = rest.split_once(']')?;
    if !elapsed
        .chars()
        .all(|character| character.is_ascii_digit() || character == ':')
    {
        return None;
    }
    let rest = rest.trim_start();
    let (who, tail) = rest.split_once(char::is_whitespace)?;
    Some((
        elapsed.to_string(),
        who.to_string(),
        tail.trim().to_string(),
    ))
}

/// Names the container already running this workspace, if one is.
///
/// The run is the container, not this process. Asking Docker which container
/// has the workspace mounted is what makes a second client attach instead of
/// starting a second run.
fn running_for(workspace: &Path) -> Option<String> {
    let listed = Command::new("docker")
        .args(["ps", "--format", "{{.Names}}"])
        .output()
        .ok()?;
    let target = workspace.canonicalize().ok()?;
    for name in String::from_utf8_lossy(&listed.stdout).split_whitespace() {
        if !name.starts_with("riemann-agent-run") {
            continue;
        }
        let mounts = Command::new("docker")
            .args([
                "inspect",
                name,
                "--format",
                "{{range .Mounts}}{{.Source}}\n{{end}}",
            ])
            .output()
            .ok()?;
        if String::from_utf8_lossy(&mounts.stdout)
            .lines()
            .any(|mount| Path::new(mount.trim()) == target)
        {
            return Some(name.to_string());
        }
    }
    None
}

/// Follows the run's container, waiting for it to exist if it must.
///
/// `docker logs` replays a container from its start, so a client attaching an
/// hour in still gets the whole run and every tab is populated before its
/// first frame. That is why the log is rewritten rather than appended to:
/// re-attaching would otherwise stack a second copy of the same history.
fn follow(
    workspace: &Path,
    container: Option<String>,
    runs: &Arc<Mutex<Runs>>,
    log: &Path,
    echo: bool,
    stop: &AtomicBool,
) {
    let mut container = container;
    while container.is_none() && !stop.load(Ordering::Relaxed) {
        container = running_for(workspace);
        if container.is_none() {
            std::thread::sleep(Duration::from_secs(1));
        }
    }
    let Some(container) = container else { return };
    if let Ok(mut state) = runs.lock() {
        state.add(&format!("following {container}"));
    }
    let child = Command::new("docker")
        .args(["logs", "--follow", "--tail", "all", &container])
        .stdout(Stdio::piped())
        .stderr(Stdio::piped())
        .spawn();
    let Ok(mut child) = child else { return };
    // Both streams are read, and this is not a detail. The runtime's console
    // goes to the container's *stderr* — a live container had 643 lines there
    // and none on stdout — so a follower that reads only stdout attaches
    // successfully and then shows an empty screen forever, which is exactly
    // how this failed the first time. There is no safe way to merge two pipes
    // into one in `std` without `unsafe`, and the crate forbids it, so each
    // gets a reader and both feed the same sink.
    let file = Arc::new(Mutex::new(std::fs::File::create(log).ok()));
    let streams: Vec<Box<dyn std::io::Read + Send>> = [
        child
            .stdout
            .take()
            .map(|out| Box::new(out) as Box<dyn std::io::Read + Send>),
        child
            .stderr
            .take()
            .map(|err| Box::new(err) as Box<dyn std::io::Read + Send>),
    ]
    .into_iter()
    .flatten()
    .collect();
    let mut readers = Vec::new();
    for stream in streams {
        let runs = Arc::clone(runs);
        let file = Arc::clone(&file);
        readers.push(std::thread::spawn(move || {
            for line in BufReader::new(stream).lines().map_while(Result::ok) {
                if let Ok(mut state) = runs.lock() {
                    state.add(&line);
                }
                if let Ok(mut handle) = file.lock()
                    && let Some(handle) = handle.as_mut()
                {
                    let _ = writeln!(handle, "{line}");
                    let _ = handle.flush();
                }
                if echo {
                    println!("{line}");
                }
            }
        }));
    }
    for reader in readers {
        let _ = reader.join();
    }
    let _ = child.wait();
    if let Ok(mut state) = runs.lock() {
        state.ended = true;
    }
    let _ = child.kill();
}

include!("euler_tui/render.rs");
include!("euler_tui/cli.rs");

#[cfg(test)]
#[allow(clippy::expect_used)]
#[path = "euler_tui/euler_tui_test.rs"]
mod test;
