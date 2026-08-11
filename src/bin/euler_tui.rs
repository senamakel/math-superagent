//! A tabbed console for one Project Euler run, one tab per team.
//!
//! The runtime prints a single interleaved stream: eleven roles, several
//! concurrent child runs each, one line per model call, tool call, and tool
//! result. That is the right shape for a trace and the wrong one for watching
//! — in one live run the organizer alone produced 232 of the first 400 lines,
//! so the solve's own progress scrolled past between two index refreshes.
//!
//! This splits the stream by role without changing it. Every byte still lands
//! in a log file exactly as the runtime emitted it, so `grep` and the existing
//! `trace.jsonl` tooling keep working; the tabs are a view, not a filter, and
//! nothing is dropped from the record because a tab was not open.
//!
//! The run is a detached container and this is a client of it. `euler-tui`
//! asks Docker which container has the workspace mounted and follows that one,
//! starting a run only when none is going. Before that, every invocation
//! started its own: opening a second view put two runs on one workspace, both
//! writing the same files and both making checkpoint commits over each other,
//! which a live pair did for four minutes before it was noticed. Quitting the
//! view, closing the terminal, or opening a second one cannot touch the run.

use std::collections::BTreeMap;
use std::io::{BufRead, BufReader, Write};
use std::path::{Path, PathBuf};
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
    Some((elapsed.to_string(), who.to_string(), tail.trim().to_string()))
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

/// Starts the run so it outlives this process, and every later client.
///
/// Its own session, and its output to a file rather than a pipe, so nothing
/// about the run depends on this process still existing. The build and the
/// statement fetch happen before any container does, so that output has no
/// `docker logs` to be recovered from and is kept here instead — it is also
/// the only place a failed build says why.
fn start_detached(root: &Path, problem: u32, research: bool, extra: &[String], log: &Path) {
    let Ok(handle) = std::fs::OpenOptions::new().create(true).append(true).open(log) else {
        return;
    };
    let Ok(errors) = handle.try_clone() else {
        return;
    };
    let mut command = Command::new(root.join("euler"));
    if !research {
        command.arg("--no-research");
    }
    command.arg(problem.to_string());
    command.args(extra);
    let _ = command
        .current_dir(root)
        .stdout(Stdio::from(handle))
        .stderr(Stdio::from(errors))
        .stdin(Stdio::null())
        .spawn();
}

/// Follows the run's container, waiting for it to exist if it must.
///
/// `docker logs` replays a container from its start, so a client attaching an
/// hour in still gets the whole run and every tab is populated before its
/// first frame. That is why the log is rewritten rather than appended to:
/// re-attaching would otherwise stack a second copy of the same history.
fn follow(
    workspace: PathBuf,
    mut container: Option<String>,
    runs: Arc<Mutex<Runs>>,
    log: PathBuf,
    echo: bool,
    stop: Arc<AtomicBool>,
) {
    while container.is_none() && !stop.load(Ordering::Relaxed) {
        container = running_for(&workspace);
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
    let Some(output) = child.stdout.take() else {
        return;
    };
    let mut file = std::fs::File::create(&log).ok();
    for line in BufReader::new(output).lines().map_while(Result::ok) {
        if let Ok(mut state) = runs.lock() {
            state.add(&line);
        }
        if let Some(file) = file.as_mut() {
            let _ = writeln!(file, "{line}");
            let _ = file.flush();
        }
        if echo {
            println!("{line}");
        }
        if stop.load(Ordering::Relaxed) {
            break;
        }
    }
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
    if ["TRUNCATED", "model RETRY", "PROVIDER FAILED", "workspace root"]
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
    let status = format!(
        " {clock} {state} {live} {} {}  [tab/shift-tab team · arrows scroll · g live · q detach] ",
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
        areas[2],
    );
}

/// Runs the view until the reader asks to leave. Quitting never stops the run.
fn watch(runs: &Arc<Mutex<Runs>>, started: Instant) -> std::io::Result<()> {
    terminal::enable_raw_mode()?;
    let mut out = std::io::stdout();
    execute!(out, EnterAlternateScreen)?;
    let mut terminal = Terminal::new(CrosstermBackend::new(out))?;
    let mut view = View::default();
    let mut painted = Instant::now() - REFRESH;
    let outcome = loop {
        let elapsed = started.elapsed().as_secs();
        let waiting = format!("{:02}:{:02}", elapsed / 60, elapsed % 60);
        if painted.elapsed() >= REFRESH {
            if let Ok(state) = runs.lock() {
                view.tab = view.tab.min(state.order.len().saturating_sub(1));
                terminal.draw(|frame| render(frame, &state, &view, &waiting))?;
            }
            painted = Instant::now();
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
            let tabs = runs.lock().map(|state| state.order.len()).unwrap_or(1).max(1);
            match key.code {
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
            painted = Instant::now() - REFRESH;
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

/// The parsed command line.
#[derive(Debug)]
struct Options {
    problem: u32,
    research: bool,
    attach: bool,
    plain: bool,
    replay: bool,
    extra: Vec<String>,
}

fn usage() -> String {
    "usage: ./euler-tui [--attach] [--replay] [--plain] [--no-research] <problem> [instructions…]\n\
     \n\
       --attach       only attach to a run already going; do not start one\n\
       --replay       open the tabs on the existing log, starting nothing\n\
       --plain        no tabs; stream to stdout, as when scripting\n\
       --no-research  withhold web search, so the run tests reasoning"
        .to_string()
}

fn options() -> Result<Options, String> {
    let mut problem = None;
    let mut research = true;
    let (mut attach, mut plain, mut replay) = (false, false, false);
    let mut extra = Vec::new();
    for argument in std::env::args().skip(1) {
        match argument.as_str() {
            "--attach" => attach = true,
            "--plain" => plain = true,
            "--replay" => replay = true,
            "--no-research" => research = false,
            "--research" => research = true,
            "-h" | "--help" => return Err(usage()),
            _ if problem.is_none() => {
                problem = Some(
                    argument
                        .parse::<u32>()
                        .map_err(|_| "problem number must be a positive integer".to_string())?,
                );
            }
            _ => extra.push(argument),
        }
    }
    let problem = problem.ok_or_else(usage)?;
    if problem == 0 {
        return Err("problem number must be a positive integer".to_string());
    }
    Ok(Options {
        problem,
        research,
        attach,
        plain,
        replay,
        extra,
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
    let workspace = root
        .join("workspace")
        .join("project-euler")
        .join(options.problem.to_string());
    let log = workspace.join("config").join("console.log");
    let _ = std::fs::create_dir_all(workspace.join("config"));

    let runs = Arc::new(Mutex::new(Runs::new()));
    let tabs = !options.plain && std::io::IsTerminal::is_terminal(&std::io::stdout());
    let started = Instant::now();

    if options.replay {
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
        if tabs && let Err(error) = watch(&runs, started) {
            eprintln!("{error}");
            return std::process::ExitCode::FAILURE;
        }
        return std::process::ExitCode::SUCCESS;
    }

    let container = running_for(&workspace);
    match (&container, options.attach) {
        (Some(name), _) => {
            if let Ok(mut state) = runs.lock() {
                state.add(&format!(
                    "attaching to {name}, already running problem {}",
                    options.problem
                ));
            }
        }
        (None, true) => {
            eprintln!(
                "nothing is running for problem {}; drop --attach to start it",
                options.problem
            );
            return std::process::ExitCode::FAILURE;
        }
        (None, false) => {
            let continuing = workspace.join("code").is_dir();
            if let Ok(mut state) = runs.lock() {
                state.add(&format!(
                    "{} problem {}: building the image, fetching the statement, starting the \
                     container. This part is silent and slow on a cold build; the first [00:00] \
                     line below is the run itself.",
                    if continuing { "continuing" } else { "starting" },
                    options.problem
                ));
            }
            start_detached(
                &root,
                options.problem,
                options.research,
                &options.extra,
                &workspace.join("config").join("start.log"),
            );
        }
    }

    let stop = Arc::new(AtomicBool::new(false));
    let reader = {
        let (runs, stop) = (Arc::clone(&runs), Arc::clone(&stop));
        let (workspace, log) = (workspace.clone(), log.clone());
        std::thread::spawn(move || follow(workspace, container, runs, log, !tabs, stop))
    };

    if tabs {
        if let Err(error) = watch(&runs, started) {
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
