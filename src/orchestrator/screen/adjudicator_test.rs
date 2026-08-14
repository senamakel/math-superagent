use super::*;

#[test]
fn a_one_word_reply_is_read() {
    assert_eq!(parse("ALLOW"), Some(Ruling::Allow));
    assert_eq!(parse("DENY"), Some(Ruling::Deny));
    assert_eq!(parse("allow"), Some(Ruling::Allow));
    assert_eq!(parse(" deny\n"), Some(Ruling::Deny));
}

#[test]
fn the_last_word_is_the_conclusion() {
    // A model that reasons before answering names both words. The conclusion is
    // the one it ends on, so reading the first would inverts the ruling exactly
    // when the model was being careful.
    assert_eq!(
        parse("This could be ALLOW, but it states the result, so DENY"),
        Some(Ruling::Deny)
    );
    assert_eq!(
        parse("At first this looks like DENY, but on reflection ALLOW"),
        Some(Ruling::Allow)
    );
}

#[test]
fn a_reply_with_neither_word_is_not_a_ruling() {
    // The caller fails closed on `None`, which is the whole point: an
    // adjudicator that did not answer must not be read as having allowed.
    assert_eq!(parse(""), None);
    assert_eq!(parse("I am not sure about this one."), None);
}

#[test]
fn deny_is_matched_inside_a_longer_word_only_as_written() {
    // `DENY` inside `DENYING` still reads as a denial, which is the safe
    // direction. Recorded as a deliberate property rather than an accident.
    assert_eq!(parse("DENYING this source"), Some(Ruling::Deny));
}
