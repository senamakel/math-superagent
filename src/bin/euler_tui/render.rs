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
