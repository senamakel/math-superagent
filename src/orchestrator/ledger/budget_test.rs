use std::fmt::Write as _;

use super::{MAX_LISTED, REASON_CHARS, elided, listed};

/// A shorter list renders whole and reports nothing dropped.
#[test]
fn a_short_list_renders_whole() {
    let (rendered, dropped) = listed(["a", "b", "c"], 10, |out, item| {
        let _ = writeln!(out, "- {item}");
    });
    assert_eq!(rendered, "- a\n- b\n- c\n");
    assert_eq!(dropped, 0);
    assert!(elided(dropped, "somewhere").is_empty());
}

/// A longer list is cut at the bound and the remainder is counted, not lost.
///
/// Counting rather than silently cutting is the whole reason this helper
/// exists: a section rendered as though complete tells the reader the run holds
/// nothing more.
#[test]
fn a_long_list_reports_what_it_dropped() {
    let (rendered, dropped) = listed(0..10, 3, |out, item| {
        let _ = writeln!(out, "- {item}");
    });
    assert_eq!(rendered, "- 0\n- 1\n- 2\n");
    assert_eq!(dropped, 7);
    let note = elided(dropped, "research/approaches/");
    assert!(note.contains('7'), "the count reaches the reader: {note}");
    assert!(
        note.contains("research/approaches/"),
        "and so does where the rest is: {note}"
    );
}

/// The iterator is drained even past the bound, so the count is the real total.
///
/// An implementation that stopped early would report zero dropped for every
/// oversized list, which is the failure it is supposed to detect.
#[test]
fn the_count_is_the_whole_input() {
    let (_, dropped) = listed(0..1000, 5, |out, item| {
        let _ = write!(out, "{item}");
    });
    assert_eq!(dropped, 995);
}

/// A bound of zero renders nothing and attributes everything to the remainder.
#[test]
fn a_zero_bound_renders_nothing() {
    let (rendered, dropped) = listed(["a", "b"], 0, |out, item| {
        let _ = write!(out, "{item}");
    });
    assert!(rendered.is_empty());
    assert_eq!(dropped, 2);
}

/// The two bounds together hold a pathological section to a readable size.
///
/// This is the regression the module was written for: sixty closed approaches,
/// each carrying five kilobytes of refutation prose, rendered 86 KB into a
/// system prompt. Under the bounds the same input has to fit in what forty
/// rows of [`REASON_CHARS`] can hold, plus the scaffolding around them.
#[test]
fn a_pathological_section_stays_bounded() {
    let approaches: Vec<(String, String)> = (0..60)
        .map(|index| (format!("approach-{index}"), "refutation ".repeat(500)))
        .collect();
    let (rendered, dropped) = listed(&approaches, MAX_LISTED, |out, (slug, reason)| {
        let _ = writeln!(
            out,
            "- [[{slug}]]: {}",
            crate::orchestrator::text::truncate(reason, REASON_CHARS)
        );
    });
    let whole = rendered + &elided(dropped, "research/approaches/");
    assert_eq!(dropped, 20);
    // Forty rows, each at most REASON_CHARS of prose plus a wikilink and the
    // list punctuation. The slack covers the elision line.
    let ceiling = MAX_LISTED * (REASON_CHARS + 64) + 256;
    assert!(
        whole.chars().count() <= ceiling,
        "{} chars exceeds the {ceiling}-char ceiling",
        whole.chars().count()
    );
    assert!(
        whole.contains("approach-0"),
        "the rows that fit are still readable"
    );
}
