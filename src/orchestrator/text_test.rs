use super::truncate;

#[test]
fn text_shorter_than_the_limit_is_returned_unchanged() {
    assert_eq!(truncate("a short claim", 40), "a short claim");
}

#[test]
fn text_at_exactly_the_limit_gains_no_ellipsis() {
    assert_eq!(truncate("abcde", 5), "abcde");
}

#[test]
fn surrounding_whitespace_is_removed_before_the_budget_is_spent() {
    assert_eq!(truncate("  \n a short claim \n ", 40), "a short claim");
}

#[test]
fn a_long_run_is_cut_at_the_last_word_boundary() {
    let cut = truncate("the quick brown fox jumps over the lazy dog", 20);
    assert_eq!(cut, "the quick brown fox…");
}

#[test]
fn a_run_with_no_whitespace_keeps_the_character_bound() {
    // Nothing to cut back to, so the character limit is what applies. The
    // `oeis` copy of this routine did this for *every* input, which is how the
    // drift was visible.
    let cut = truncate("https://example.invalid/aaaaaaaaaaaaaaaaaaaaaaaa", 20);
    assert_eq!(cut.chars().count(), 21, "20 characters and the ellipsis");
    assert!(cut.ends_with('…'));
}

#[test]
fn multi_byte_characters_are_counted_rather_than_sliced() {
    // A byte-indexed implementation would panic here rather than shorten.
    let cut = truncate("λαμβδα καππα μυ νυ ξι", 12);
    assert!(cut.ends_with('…'));
    assert!(cut.chars().count() <= 13);
}
