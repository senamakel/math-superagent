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
