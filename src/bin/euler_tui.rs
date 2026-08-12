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

/// Chooses the style for one line, by what the line reports.
///
/// Colour is doing one job: making the shape of a run readable while it
/// scrolls, so an eye lands on the events that change what happens next.
/// Faults are red because they are the reason to look; the loop's verdicts are
/// yellow and bold because they are the run changing state; a started tool
/// call is cyan and a finished one green, so the gap between them — where a
/// ten-minute command sits — is a colour nothing has answered yet. Model calls
/// are dimmed: they are the bulk of the stream and rarely the thing sought.
fn style_for(line: &str) -> Style {
    if PINNED.iter().any(|pin| line.contains(pin)) {
        return Style::default()
            .fg(Color::Yellow)
            .add_modifier(Modifier::BOLD);
    }
    if line.contains("error") {
        return Style::default().fg(Color::Red);
    }
    if [
        "TRUNCATED",
        "model RETRY",
        "PROVIDER FAILED",
        "workspace root",
    ]
    .iter()
    .any(|word| line.contains(word))
    {
        return Style::default().fg(Color::Magenta);
    }
    if line.contains("spawned:") || line.contains("run started") {
        return Style::default().fg(Color::Blue);
    }
    if line.contains("tool  done") {
        return Style::default().fg(Color::Green);
    }
    if line.contains("tool  call") {
        return Style::default().fg(Color::Cyan);
    }
    if line.contains("model") {
        return Style::default().add_modifier(Modifier::DIM);
    }
    Style::default()
}

/// What the view is currently showing.
#[derive(Debug, Default)]
struct View {
    tab: usize,
    /// Lines back from the live end; zero follows the tail.
    offset: usize,
    /// What is being typed, when the reader is composing a directive.
    ///
    /// `None` is the normal state, and it is what makes every other key mean
    /// what it always meant: with a composing buffer open, `q` is a letter
    /// rather than a way out, so the two states have to be distinguishable
    /// rather than inferred from whether the buffer is empty.
    composing: Option<String>,
    /// What the last send did, shown until the next one.
    sent: Option<String>,
    /// Directives sent from this viewer.
    count: usize,
}

/// Paints one frame.
fn render(frame: &mut ratatui::Frame<'_>, runs: &Runs, view: &View, waiting: &str) {
    let areas = Layout::default()
        .direction(Direction::Vertical)
        .constraints([
            Constraint::Length(1),
            Constraint::Min(1),
            Constraint::Length(1),
        ])
        .split(frame.area());

    let titles: Vec<Line<'_>> = runs
        .order
        .iter()
        .enumerate()
        .map(|(index, name)| Line::from(format!("{}:{name}", index + 1)))
        .collect();
    frame.render_widget(
        Tabs::new(titles)
            .select(view.tab)
            .style(Style::default().fg(Color::Cyan).add_modifier(Modifier::DIM))
            .highlight_style(
                Style::default()
                    .fg(Color::Cyan)
                    .add_modifier(Modifier::BOLD | Modifier::REVERSED),
            )
            .divider(" "),
        areas[0],
    );

    let empty = Tab::default();
    let tab = runs
        .order
        .get(view.tab)
        .and_then(|name| runs.tabs.get(name))
        .unwrap_or(&empty);
    let height = usize::from(areas[1].height);
    let end = tab.lines.len().saturating_sub(view.offset);
    let start = end.saturating_sub(height);
    let body: Vec<Line<'_>> = tab.lines[start..end]
        .iter()
        .map(|line| Line::styled(line.clone(), style_for(line)))
        .collect();
    frame.render_widget(
        Paragraph::new(body).block(Block::default().borders(Borders::NONE)),
        areas[1],
    );

    render_status(frame, runs, view, waiting, areas[2]);
}

/// Paints the bottom row: the run's health, or the line being typed.
///
/// Split out of [`render`] when composing was added. The row now has two
/// states rather than one, and they share nothing but their position.
fn render_status(
    frame: &mut ratatui::Frame<'_>,
    runs: &Runs,
    view: &View,
    waiting: &str,
    area: ratatui::layout::Rect,
) {
    // Composing takes the whole row. The alternative is a separate input line
    // that appears and disappears, which moves the body under the reader's
    // eyes at the moment they have started typing.
    if let Some(typed) = &view.composing {
        frame.render_widget(
            Paragraph::new(Line::from(Span::styled(
                format!(" direct the run> {typed}▏  [enter send · esc cancel] "),
                Style::default()
                    .fg(Color::Yellow)
                    .add_modifier(Modifier::REVERSED),
            ))),
            area,
        );
        return;
    }

    let faults: Vec<String> = COUNTED
        .iter()
        .filter_map(|(name, _)| {
            runs.counts
                .get(name)
                .filter(|count| **count > 0)
                .map(|count| format!("{name}={count}"))
        })
        .collect();
    let state = if runs.ended {
        "ended"
    } else if runs.elapsed.is_empty() {
        // The container has not spoken yet. Say so, and count in wall clock,
        // or a silent build reads as a program that never started.
        "starting"
    } else {
        "running"
    };
    let clock = if runs.elapsed.is_empty() {
        waiting
    } else {
        &runs.elapsed
    };
    let live = if view.offset == 0 {
        "LIVE".to_string()
    } else {
        format!("-{}", view.offset)
    };
    let sent = view
        .sent
        .as_ref()
        .map_or_else(String::new, |sent| format!(" {sent} "));
    let status = format!(
        " {clock} {state} {live} {} {}{sent} \
         [tab/shift-tab team · arrows scroll · g live · i direct · q detach] ",
        runs.cost,
        faults.join(" ")
    );
    let bar = if faults.is_empty() {
        Style::default().fg(Color::Cyan)
    } else {
        Style::default().fg(Color::Red)
    };
    frame.render_widget(
        Paragraph::new(Line::from(Span::styled(
            status,
            bar.add_modifier(Modifier::REVERSED),
        ))),
        area,
    );
}

/// Applies one keypress while a directive is being composed.
///
/// Split out because composing swallows the whole keyboard: `q` is a letter
/// here and `1` is a digit, so leaving this inline in the navigation match
/// would mean every future binding had to remember to check the mode first.
///
/// `directable` is `None` in replay, where there is no run to direct. The
/// refusal is here rather than at the `i` binding so the reason can be said in
/// the status bar at the moment someone tries, rather than the key doing
/// nothing and reading as a broken viewer.
fn compose_key(view: &mut View, key: KeyCode, directable: Option<&Path>) {
    let Some(typed) = view.composing.as_mut() else {
        return;
    };
    match key {
        KeyCode::Esc => {
            view.composing = None;
        }
        KeyCode::Backspace => {
            typed.pop();
        }
        KeyCode::Char(character) => typed.push(character),
        KeyCode::Enter => {
            let text = typed.clone();
            view.composing = None;
            let Some(workspace) = directable else {
                view.sent = Some("replay: no run to direct".to_string());
                return;
            };
            match math_agent::directives::enqueue(workspace, "euler-tui", &text) {
                Ok(directive) => {
                    view.count += 1;
                    // The count, not just the last one, because a directive is
                    // picked up asynchronously: an operator who sent three and
                    // sees "sent" cannot tell whether the third one landed.
                    view.sent = Some(format!("sent #{} ({})", directive.id, view.count));
                }
                Err(error) => view.sent = Some(format!("not sent: {error}")),
            }
        }
        _ => {}
    }
}

/// Runs the view until the reader asks to leave. Quitting never stops the run.
///
/// `directable` carries the workspace a directive may be queued in, and is
/// `None` in replay. Nothing else in this function can reach the run.
fn watch(
    runs: &Arc<Mutex<Runs>>,
    started: Instant,
    directable: Option<&Path>,
) -> std::io::Result<()> {
    terminal::enable_raw_mode()?;
    let mut out = std::io::stdout();
    execute!(out, EnterAlternateScreen)?;
    let mut terminal = Terminal::new(CrosstermBackend::new(out))?;
    let mut view = View::default();
    // `None` until the first frame, so the view paints immediately rather than
    // waiting a refresh interval to show anything.
    let mut painted: Option<Instant> = None;
    let outcome = loop {
        let elapsed = started.elapsed().as_secs();
        let waiting = format!("{:02}:{:02}", elapsed / 60, elapsed % 60);
        if painted.is_none_or(|at| at.elapsed() >= REFRESH) {
            if let Ok(state) = runs.lock() {
                view.tab = view.tab.min(state.order.len().saturating_sub(1));
                terminal.draw(|frame| render(frame, &state, &view, &waiting))?;
            }
            painted = Some(Instant::now());
        }
        if !event::poll(POLL)? {
            continue;
        }
        // Every event waiting is consumed before the next repaint, so a held
        // arrow scrolls by its whole run rather than one line per frame.
        let mut page = 1;
        if let Ok(state) = runs.lock() {
            page = state.order.len();
        }
        let _ = page;
        let mut leave = false;
        while event::poll(Duration::ZERO)? || !leave {
            let Event::Key(key) = event::read()? else {
                break;
            };
            if key.kind != KeyEventKind::Press {
                break;
            }
            let tabs = runs.lock().map_or(1, |state| state.order.len()).max(1);
            // Composing first, and it consumes everything. Falling through to
            // the navigation keys would make `q` in the middle of a sentence
            // detach the viewer and lose what had been typed.
            if view.composing.is_some() {
                compose_key(&mut view, key.code, directable);
                painted = None;
                if !event::poll(Duration::ZERO)? {
                    break;
                }
                continue;
            }
            match key.code {
                KeyCode::Char('i') => {
                    view.composing = Some(String::new());
                    view.sent = None;
                }
                KeyCode::Char('q') | KeyCode::Esc => {
                    leave = true;
                    break;
                }
                KeyCode::Char('c') if key.modifiers.contains(KeyModifiers::CONTROL) => {
                    leave = true;
                    break;
                }
                KeyCode::Tab | KeyCode::Right | KeyCode::Char('n') => {
                    view.tab = (view.tab + 1) % tabs;
                    view.offset = 0;
                }
                KeyCode::BackTab | KeyCode::Left | KeyCode::Char('p') => {
                    view.tab = (view.tab + tabs - 1) % tabs;
                    view.offset = 0;
                }
                KeyCode::Up => view.offset += 1,
                KeyCode::Down => view.offset = view.offset.saturating_sub(1),
                KeyCode::PageUp => view.offset += 20,
                KeyCode::PageDown => view.offset = view.offset.saturating_sub(20),
                KeyCode::Char('g') | KeyCode::End => view.offset = 0,
                KeyCode::Char(digit) if digit.is_ascii_digit() && digit != '0' => {
                    let wanted = usize::from(
                        u8::try_from(u32::from(digit) - u32::from('0')).unwrap_or(1) - 1,
                    );
                    if wanted < tabs {
                        view.tab = wanted;
                        view.offset = 0;
                    }
                }
                _ => {}
            }
            painted = None;
            if !event::poll(Duration::ZERO)? {
                break;
            }
        }
        if leave {
            break Ok(());
        }
    };
    terminal::disable_raw_mode()?;
    execute!(terminal.backend_mut(), LeaveAlternateScreen)?;
    terminal.show_cursor()?;
    outcome
}

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

#[cfg(test)]
#[allow(clippy::expect_used)]
mod test {
    use super::{View, compose_key};
    use crossterm::event::KeyCode;

    fn typing(view: &mut View, text: &str, workspace: Option<&std::path::Path>) {
        for character in text.chars() {
            compose_key(view, KeyCode::Char(character), workspace);
        }
    }

    fn workspace(name: &str) -> std::io::Result<std::path::PathBuf> {
        let root = std::env::temp_dir().join(format!("math-agent-tui-{name}"));
        let _ = std::fs::remove_dir_all(&root);
        std::fs::create_dir_all(root.join("config"))?;
        root.canonicalize()
    }

    /// The viewer may direct a run that exists. It still cannot start one, and
    /// what it writes is a line in a file rather than anything that spawns.
    #[test]
    fn a_typed_directive_reaches_the_queue() -> std::io::Result<()> {
        let root = workspace("send")?;
        let mut view = View {
            composing: Some(String::new()),
            ..View::default()
        };
        typing(&mut view, "check the n=14 bound", Some(&root));
        compose_key(&mut view, KeyCode::Enter, Some(&root));

        assert_eq!(view.composing, None, "sending closes the line");
        assert_eq!(view.count, 1);
        let queued = std::fs::read_to_string(root.join(math_agent::directives::QUEUE))?;
        assert!(queued.contains("check the n=14 bound"), "{queued}");
        assert!(view.sent.is_some_and(|sent| sent.contains("sent #1")));
        Ok(())
    }

    /// Replay is a record of a run that has already finished. A directive
    /// queued against it would sit unread until somebody started a run on the
    /// same workspace, and then arrive as an instruction from an hour ago.
    #[test]
    fn replay_refuses_to_send_and_says_why() -> std::io::Result<()> {
        let root = workspace("replay")?;
        let mut view = View {
            composing: Some(String::new()),
            ..View::default()
        };
        typing(&mut view, "stop enumerating", None);
        compose_key(&mut view, KeyCode::Enter, None);

        assert_eq!(view.count, 0);
        assert!(!root.join(math_agent::directives::QUEUE).exists());
        assert!(
            view.sent.is_some_and(|sent| sent.contains("replay")),
            "the refusal has to say why, or the key reads as broken"
        );
        Ok(())
    }

    /// Composing swallows the keyboard. Without that, `q` in the middle of a
    /// sentence detaches the viewer and loses what was typed.
    #[test]
    fn composing_treats_navigation_keys_as_text() -> std::io::Result<()> {
        let root = workspace("swallow")?;
        let mut view = View {
            composing: Some(String::new()),
            ..View::default()
        };
        typing(&mut view, "q1g and prove it", Some(&root));
        assert_eq!(view.composing.as_deref(), Some("q1g and prove it"));
        assert_eq!(view.tab, 0, "a digit while composing is not a tab jump");
        assert_eq!(view.offset, 0);
        Ok(())
    }

    /// Escape abandons the line without queueing anything.
    #[test]
    fn escape_cancels_without_sending() -> std::io::Result<()> {
        let root = workspace("cancel")?;
        let mut view = View {
            composing: Some(String::new()),
            ..View::default()
        };
        typing(&mut view, "never mind", Some(&root));
        compose_key(&mut view, KeyCode::Esc, Some(&root));

        assert_eq!(view.composing, None);
        assert_eq!(view.count, 0);
        assert!(!root.join(math_agent::directives::QUEUE).exists());
        Ok(())
    }

    /// An empty directive is refused by the queue, and the viewer says so
    /// rather than reporting a send that did not happen.
    #[test]
    fn an_empty_line_is_reported_as_not_sent() -> std::io::Result<()> {
        let root = workspace("empty")?;
        let mut view = View {
            composing: Some(String::new()),
            ..View::default()
        };
        compose_key(&mut view, KeyCode::Enter, Some(&root));

        assert_eq!(view.count, 0);
        assert!(view.sent.is_some_and(|sent| sent.contains("not sent")));
        Ok(())
    }

    /// Backspace edits rather than cancelling: a typo in a long directive
    /// should not cost the whole sentence.
    #[test]
    fn backspace_edits_the_line() {
        let mut view = View {
            composing: Some(String::new()),
            ..View::default()
        };
        typing(&mut view, "sieve", None);
        compose_key(&mut view, KeyCode::Backspace, None);
        assert_eq!(view.composing.as_deref(), Some("siev"));
    }
}
