#![allow(clippy::expect_used)]

use super::*;

/// The salt the pinned fixtures below were generated under.
const PINNED_SALT: &str = "pinned-fixture-salt-0123456789abcdef";

/// Digests produced by `scripts/compile-screen` itself.
///
/// This is the cross-language pin. The Python compiler writes the digests a run
/// is screened against and this Rust module computes the ones they are compared
/// to, so a divergence in normalisation silently stops the screen matching —
/// no error, no ledger entry, just a blocklist that never fires. Regenerate
/// with the snippet in the module documentation of `scripts/compile-screen` and
/// update here only when both sides were changed together and deliberately.
const PINNED: &[(&str, &[&str], &str)] = &[
    ("de Grey", &["de", "grey"], "6c5b64951e68b7f78c154859ab0dc1e8"),
    (
        "Mihăilescu",
        &["mihailescu"],
        "850e18fd04df47834ce574b98da7c482",
    ),
    (
        "Hadwiger-Nelson",
        &["hadwiger", "nelson"],
        "cf3a5678da20c45f614081acabe59f94",
    ),
    (
        "sensitivity conjecture",
        &["sensitivity", "conjecture"],
        "ddb73d32ca199ea513b7aed9adbea7af",
    ),
    ("Erdős", &["erdos"], "490cd84e2085b238daf07c186e3d4cab"),
    (
        "Métsankylä Ø ł",
        &["metsankyla", "o", "l"],
        "3aab963deeb004b2ad4cfa492796f190",
    ),
    (
        "1804.02385",
        &["1804", "02385"],
        "8867919690f1129942439532f57985c9",
    ),
];

#[test]
fn an_identifier_matches_inside_a_citation() {
    // The reason every non-alphanumeric character separates: a term compiled
    // from `1804.02385` has to be found in text that writes it
    // `arXiv:1804.02385`. Welding punctuation away instead of splitting on it
    // would produce `arxiv180402385` here and match nothing.
    let salt = "s";
    let needle = digest(salt, &tokenise("1804.02385"));
    assert!(
        digests_of(salt, "see arXiv:1804.02385 for the construction", 10).contains(&needle),
        "an arXiv identifier must match inside a citation"
    );
}

#[test]
fn normalisation_agrees_with_the_compiler_script() {
    for (source, expected_tokens, expected_digest) in PINNED {
        let tokens = tokenise(source);
        assert_eq!(
            tokens, *expected_tokens,
            "tokenising {source:?} diverged from scripts/compile-screen"
        );
        assert_eq!(
            digest(PINNED_SALT, &tokens),
            *expected_digest,
            "digest of {source:?} diverged from scripts/compile-screen"
        );
    }
}

#[test]
fn a_term_is_found_inside_surrounding_text() {
    let salt = "s";
    let needle = digest(salt, &tokenise("de Grey"));
    let haystack = digests_of(
        salt,
        "Aubrey D. N. J. de Grey, The chromatic number of the plane",
        10,
    );
    assert!(
        haystack.contains(&needle),
        "a two-token term must match inside a longer sentence"
    );
}

#[test]
fn case_and_diacritics_do_not_defeat_a_match() {
    let salt = "s";
    let needle = digest(salt, &tokenise("Mihăilescu"));
    for variant in ["MIHAILESCU, Preda", "mihăilescu proved it", "Mihailescu"] {
        assert!(
            digests_of(salt, variant, 4).contains(&needle),
            "{variant:?} should match the term `Mihăilescu`"
        );
    }
}

#[test]
fn punctuation_and_hyphens_do_not_defeat_a_match() {
    let salt = "s";
    let needle = digest(salt, &tokenise("Hadwiger Nelson"));
    for variant in [
        "the Hadwiger-Nelson problem",
        "Hadwiger–Nelson",
        "(Hadwiger, Nelson)",
    ] {
        assert!(
            digests_of(salt, variant, 4).contains(&needle),
            "{variant:?} should match the term `Hadwiger Nelson`"
        );
    }
}

#[test]
fn an_unrelated_sentence_matches_nothing() {
    let salt = "s";
    let blocked: Vec<String> = ["de Grey", "Mihăilescu", "sensitivity conjecture"]
        .iter()
        .map(|term| digest(salt, &tokenise(term)))
        .collect();
    let text = digests_of(
        salt,
        "We compute the chromatic number of a small unit-distance graph.",
        10,
    );
    for needle in &blocked {
        assert!(
            !text.contains(needle),
            "ordinary mathematical prose must not trip the blocklist"
        );
    }
}

#[test]
fn an_ngram_longer_than_the_text_is_not_searched() {
    // Guards the `width > tokens.len()` break: without it, `windows` panics on
    // a width past the slice length.
    let found = digests_of("s", "one two", 10);
    assert_eq!(
        found.len(),
        3,
        "two tokens yield exactly two unigrams and one bigram"
    );
}

#[test]
fn a_combining_mark_does_not_split_a_token() {
    // `Mihăilescu` written in decomposed form, as some PDF text layers emit it.
    // Combining marks are dropped rather than treated as separators; treating
    // them as separators cuts the name into `miha` and `ilescu` and the term
    // stops matching, silently.
    let decomposed = "Miha\u{0306}ilescu";
    assert_eq!(tokenise(decomposed), vec!["mihailescu".to_string()]);
    assert_eq!(tokenise("Mihăilescu"), tokenise(decomposed));
}

#[test]
fn empty_text_yields_no_digests() {
    assert!(digests_of("s", "   ...   ", 10).is_empty());
}
