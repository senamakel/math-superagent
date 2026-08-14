use super::*;

#[test]
fn a_blocked_term_denies_and_beats_a_flag() {
    let policy = ScreenPolicy::for_test(&["de Grey"], &["chromatic number"], &[]);
    assert_eq!(
        policy.screen_text("a paper by Aubrey de Grey on the chromatic number"),
        Verdict::Deny,
        "a [block] match is a decision, so it must win over a [flag] match in the same text"
    );
}

#[test]
fn a_flagged_term_escalates_rather_than_denying() {
    let policy = ScreenPolicy::for_test(&["de Grey"], &["chromatic number"], &[]);
    assert_eq!(
        policy.screen_text("we bound the chromatic number of this graph"),
        Verdict::Adjudicate
    );
}

#[test]
fn ordinary_prose_passes() {
    let policy = ScreenPolicy::for_test(&["de Grey"], &["chromatic number"], &[]);
    assert_eq!(
        policy.screen_text("we verify each edge has length exactly one"),
        Verdict::Allow
    );
}

#[test]
fn a_denied_host_covers_its_subdomains() {
    let policy = ScreenPolicy::for_test(&["x"], &[], &["arxiv.org"]);
    for url in [
        "https://arxiv.org/abs/1804.02385",
        "http://export.arxiv.org/api/query",
        "https://arxiv.org:443/pdf/1907.00847",
        "https://user@arxiv.org/abs/1",
    ] {
        assert!(policy.denies_host(url), "{url} should be denied");
    }
}

#[test]
fn a_lookalike_host_is_not_denied() {
    let policy = ScreenPolicy::for_test(&["x"], &[], &["arxiv.org"]);
    for url in [
        "https://notarxiv.org/paper",
        "https://arxiv.example.com/abs/1",
        "https://oeis.org/A001597",
    ] {
        assert!(!policy.denies_host(url), "{url} should not be denied");
    }
}

#[test]
fn a_bare_hostname_is_denied_too() {
    // A tool argument spelled without a scheme still names the host, and the
    // safe reading of `arxiv.org` is the one that withholds it.
    let policy = ScreenPolicy::for_test(&["x"], &[], &["arxiv.org"]);
    assert!(policy.denies_host("arxiv.org"));
    assert!(policy.denies_host("arxiv.org/abs/1804.02385"));
}

#[test]
fn text_that_is_not_a_url_denies_nothing() {
    // The input here is a model-supplied string that may not be a URL at all,
    // and the right answer for "not a URL" is "no host" rather than an error.
    let policy = ScreenPolicy::for_test(&["x"], &[], &["arxiv.org"]);
    for text in ["", "not a url", "   ", "/abs/1804.02385"] {
        assert!(!policy.denies_host(text), "{text:?} names no denied host");
    }
}

/// Writes a compiled-policy fixture under a name unique to this test.
fn write_policy(name: &str, body: &str) -> std::path::PathBuf {
    let root = std::env::temp_dir().join(format!("math-agent-screen-{name}"));
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(&root).expect("the fixture directory must be creatable");
    let path = root.join("screen.json");
    std::fs::write(&path, body).expect("the fixture policy must be writable");
    path
}

#[test]
fn a_well_formed_policy_loads() {
    let path = write_policy(
        "well-formed",
        r#"{"slug":"p","salt":"0123456789abcdef0","max_ngram":4,
            "block":["aa"],"flag":[],"deny_hosts":[],
            "adjudicator":{"enabled":false,"timeout_seconds":7,"max_chars":11}}"#,
    );
    let policy = ScreenPolicy::load(&path).expect("a well-formed policy must load");
    assert_eq!(policy.slug, "p");
    assert!(!policy.adjudicator_enabled);
    assert_eq!(policy.adjudicator_timeout_seconds, 7);
    assert_eq!(policy.adjudicator_max_chars, 11);
}

#[test]
fn a_missing_policy_file_is_an_error_not_a_silent_pass() {
    // The whole point: a named-but-broken policy must stop the run. Degrading
    // to no screening produces a calibration run that looks normal, spends
    // hours of provider credit, and measures nothing.
    let error = ScreenPolicy::load(std::path::Path::new("/nonexistent/screen.json"))
        .expect_err("a missing policy must not load");
    assert!(
        error.to_string().contains("must not continue unscreened"),
        "the error must say why it is fatal, got: {error}"
    );
}

#[test]
fn a_policy_that_is_not_json_is_an_error() {
    let path = write_policy("not-json", "not json at all");
    assert!(ScreenPolicy::load(&path).is_err());
}

#[test]
fn a_policy_with_a_short_salt_is_an_error() {
    let path = write_policy(
        "short-salt",
        r#"{"slug":"p","salt":"short","max_ngram":4,"block":["aa"]}"#,
    );
    let error = ScreenPolicy::load(&path).expect_err("a short salt must not load");
    assert!(error.to_string().contains("salt"));
}

#[test]
fn a_policy_with_no_blocked_terms_is_an_error() {
    // An empty block list is almost always a compilation mistake, and it would
    // produce a run that is screened in name only.
    let path = write_policy(
        "empty-block",
        r#"{"slug":"p","salt":"0123456789abcdef0","max_ngram":4,"block":[]}"#,
    );
    let error = ScreenPolicy::load(&path).expect_err("an empty blocklist must not load");
    assert!(error.to_string().contains("empty `block` list"));
}

#[test]
fn a_policy_with_no_ngram_width_is_an_error() {
    let path = write_policy(
        "no-ngram",
        r#"{"slug":"p","salt":"0123456789abcdef0","block":["aa"]}"#,
    );
    assert!(ScreenPolicy::load(&path).is_err());
}
