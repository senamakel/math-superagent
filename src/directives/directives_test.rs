#![allow(clippy::expect_used)]

use super::{CURSOR, Directive, LEDGER, QUEUE, drain, enqueue, pending, record};
use crate::Error;

fn workspace(name: &str) -> std::io::Result<std::path::PathBuf> {
    let root = std::env::temp_dir().join(format!("math-agent-directives-{name}"));
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(root.join("config"))?;
    root.canonicalize()
}

/// The whole point of the channel: what the operator typed is what the run
/// gets back, unchanged.
#[test]
fn a_queued_directive_comes_back_whole() -> std::io::Result<()> {
    let root = workspace("roundtrip")?;
    let sent = enqueue(
        &root,
        "euler-tui",
        "  check the n=14 bound against a sieve  ",
    )
    .expect("a non-empty directive queues");
    assert_eq!(sent.id, 1);
    assert_eq!(sent.from, "euler-tui");
    assert_eq!(sent.text, "check the n=14 bound against a sieve");

    let waiting = pending(&root).expect("the queue reads back");
    assert_eq!(waiting, vec![sent]);
    Ok(())
}

/// Delivery is decided by the cursor, so a drained directive must not come
/// back on the next cycle — a standing team reads this every twenty seconds,
/// and a directive redelivered forever is a directive acted on forever.
#[test]
fn draining_consumes_each_directive_once() -> std::io::Result<()> {
    let root = workspace("once")?;
    enqueue(&root, "steer", "first").expect("first queues");
    enqueue(&root, "steer", "second").expect("second queues");

    let taken: Vec<String> = drain(&root)
        .expect("the queue drains")
        .into_iter()
        .map(|directive| directive.text)
        .collect();
    assert_eq!(taken, vec!["first".to_string(), "second".to_string()]);
    assert!(drain(&root).expect("a drained queue drains").is_empty());
    assert!(pending(&root).expect("nothing is pending").is_empty());

    // A directive arriving after the drain is still delivered, and keeps its
    // position in the file as its identifier.
    enqueue(&root, "steer", "third").expect("third queues");
    let third = pending(&root).expect("the third is pending");
    assert_eq!(third.len(), 1);
    assert_eq!(third[0].id, 3);
    Ok(())
}

/// A host append can interleave with the checkpoint commit that runs over the
/// workspace, so a torn line has to be stepped over rather than stopping the
/// channel. The line is still counted, which is what keeps an identifier equal
/// to a line number.
#[test]
fn a_torn_line_is_skipped_and_still_counted() -> std::io::Result<()> {
    let root = workspace("torn")?;
    enqueue(&root, "steer", "before").expect("the first queues");
    // A half-written line, as an interrupted append would leave.
    std::fs::write(
        root.join(QUEUE),
        format!(
            "{}{{\"at\":1,\"from\":\"steer\",\"te\n",
            std::fs::read_to_string(root.join(QUEUE))?
        ),
    )?;
    enqueue(&root, "steer", "after").expect("the third queues");

    let waiting = pending(&root).expect("the queue reads past the torn line");
    let texts: Vec<&str> = waiting.iter().map(|one| one.text.as_str()).collect();
    assert_eq!(texts, vec!["before", "after"]);
    // Third line, not second: the unreadable one kept its place.
    assert_eq!(waiting[1].id, 3);

    // And the cursor steps past the torn line rather than stalling on it.
    drain(&root).expect("the queue drains");
    assert!(pending(&root).expect("nothing is pending").is_empty());
    Ok(())
}

/// An unreadable cursor redelivers rather than dropping. A directive delivered
/// twice is visible to the operator; one dropped is not.
#[test]
fn an_unreadable_cursor_redelivers() -> std::io::Result<()> {
    let root = workspace("cursor")?;
    enqueue(&root, "steer", "only").expect("it queues");
    drain(&root).expect("it drains");
    std::fs::write(root.join(CURSOR), "not a number\n")?;
    assert_eq!(pending(&root).expect("the queue reads").len(), 1);
    Ok(())
}

/// The text is the untrusted input at this layer, so it is what gets checked.
#[test]
fn empty_and_oversized_directives_are_refused() -> std::io::Result<()> {
    let root = workspace("refused")?;
    assert_eq!(enqueue(&root, "steer", "   "), Err(Error::DirectiveEmpty));
    let long = "x".repeat(super::MAX_TEXT + 1);
    assert_eq!(
        enqueue(&root, "steer", &long),
        Err(Error::DirectiveTooLong {
            limit: super::MAX_TEXT,
            actual: super::MAX_TEXT + 1,
        })
    );
    // Neither wrote anything, so a refused send cannot leave a partial line
    // for the run to trip over.
    assert!(!root.join(QUEUE).exists());
    Ok(())
}

/// A directive holding newlines stays one line in the queue, because the file
/// format is one object per line and the reader counts lines.
#[test]
fn a_multiline_directive_stays_one_line() -> std::io::Result<()> {
    let root = workspace("multiline")?;
    enqueue(&root, "steer", "first thought\nsecond thought").expect("it queues");
    let raw = std::fs::read_to_string(root.join(QUEUE))?;
    assert_eq!(raw.lines().count(), 1);
    let waiting = pending(&root).expect("the queue reads");
    assert_eq!(waiting[0].text, "first thought\nsecond thought");
    Ok(())
}

/// An unnamed sender is recorded as unknown rather than as an empty column, so
/// the ledger never has a blank where a name goes.
#[test]
fn an_unnamed_sender_is_recorded_as_unknown() -> std::io::Result<()> {
    let root = workspace("unnamed")?;
    let sent = enqueue(&root, "  ", "direction").expect("it queues");
    assert_eq!(sent.from, "unknown");
    Ok(())
}

/// The receipt is what tells an operator the difference between "not picked up
/// yet" and "silently dropped", which is the one thing a channel that never
/// blocks cannot otherwise say.
#[test]
fn the_ledger_records_what_became_of_a_directive() -> std::io::Result<()> {
    let root = workspace("ledger")?;
    let directive = Directive {
        id: 1,
        at: 0,
        from: "euler-tui".to_string(),
        text: "check the n=14 bound".to_string(),
    };
    record(
        &root,
        &directive,
        "Rewrote TASKS.md to lead with the sieve check.",
    )
    .expect("the ledger writes");
    record(
        &root,
        &Directive { id: 2, ..directive },
        "No change: the run had already dropped that approach.",
    )
    .expect("the ledger appends");

    let ledger = std::fs::read_to_string(root.join(LEDGER))?;
    assert_eq!(ledger.matches("# Directives").count(), 1);
    assert!(ledger.contains("## 1 — from euler-tui"));
    assert!(ledger.contains("## 2 — from euler-tui"));
    assert!(ledger.contains("Rewrote TASKS.md"));
    Ok(())
}

/// A cursor left behind by an earlier run still exposes what arrived since.
///
/// A live run sat with a cursor of 37 against a 44-line queue for an hour and
/// drained nothing, so the operator's seven directives never reached it. This
/// pins the arithmetic that was suspected first, so the next investigation
/// starts past it rather than at it.
#[test]
fn a_stale_cursor_leaves_later_directives_pending() -> std::io::Result<()> {
    let root = workspace("stale-cursor")?;
    for index in 1..=44 {
        enqueue(&root, "steer", &format!("directive {index}")).expect("the queue accepts");
    }
    std::fs::write(root.join(CURSOR), "37\n")?;
    let waiting = pending(&root).expect("a readable queue");
    assert_eq!(waiting.len(), 7, "ids 38..=44 are still waiting");
    assert_eq!(waiting[0].id, 38);
    assert_eq!(waiting[6].id, 44);
    Ok(())
}
