//! Matching text against a blocklist nobody in the container can read.
//!
//! A calibration run is given a conjecture that has already been solved and
//! told it is open. That only measures anything if the published solution
//! cannot be reached, so the run's way onto the web is screened against a list
//! of the names, titles and identifiers that carry the answer.
//!
//! The list cannot be shipped in plaintext. The compiled policy is mounted into
//! the agent container so this code can use it, and `execute_command` runs
//! Python as the same user, so any file the runtime can read the run can read
//! too. A plaintext blocklist would hand the run exactly the names it is meant
//! to withhold — the file would *be* the leak.
//!
//! So a term arrives as a salted digest of its normalised token n-gram, and
//! matching hashes the candidate text the same way and intersects. `de Grey` is
//! found inside `Aubrey D. N. J. de Grey` because both normalise to the bigram
//! `de grey`; `Mihăilescu` is found inside `MIHAILESCU` because normalisation
//! folds case and diacritics. Neither string appears anywhere in the container.
//!
//! What this deliberately does not do is defend against an adversary. A run
//! that set out to defeat the screen could learn that one exists. The threat
//! model is accidental ingestion by a run that is trying to do mathematics, and
//! against that the digest is enough: it removes the file as a source of the
//! very strings it withholds.
//!
//! # This must agree with `scripts/compile-screen`
//!
//! The digests compared against here are produced by that script, in Python.
//! If the two normalisations diverge, nothing fails loudly — the screen simply
//! stops matching, which is the worst failure shape available in this module.
//! So the rules are kept deliberately small and identical on both sides, and
//! [`test`] pins a set of digests computed by the script itself.

use std::collections::HashSet;

use sha2::{Digest as _, Sha256};

/// Latin letters that Unicode canonical decomposition does **not** take apart.
///
/// The script normalises with NFKD and drops the combining marks, which folds
/// `ă`, `ü`, `é` and most of what appears in a mathematician's name. A handful
/// of letters have no decomposition — the stroked and slashed ones — and would
/// survive on one side and not the other. They are listed explicitly here and
/// in the script's `EXPLICIT_FOLD`, and the two lists must stay equal.
const EXPLICIT_FOLD: &[(char, char)] = &[
    ('ø', 'o'),
    ('œ', 'o'),
    ('ł', 'l'),
    ('đ', 'd'),
    ('ð', 'd'),
    ('ħ', 'h'),
    ('ı', 'i'),
    ('ŧ', 't'),
    ('æ', 'a'),
    ('ß', 's'),
    ('þ', 't'),
];

/// Splits text into the normalised tokens the digests are computed over.
///
/// **Every non-alphanumeric character separates.** That is the whole rule, and
/// it is chosen over a list of separators because the alternatives silently
/// lose matches in two directions at once. Mathematics writes a two-name result
/// with an en dash — `Hadwiger–Nelson`, `Erdős–Gyárfás` — so a rule that splits
/// only on the ASCII hyphen collapses the pair into one token and the term
/// never matches a real paper. And an identifier arrives as `arXiv:1804.02385`,
/// so a rule that *drops* punctuation inside a token welds it into
/// `arxiv180402385`, which matches nothing either. Splitting on everything
/// makes both work: the term and the text tokenise the same way, and a
/// multi-token term is found as an n-gram.
///
/// Case is folded, and precomposed Latin letters are folded by
/// [`EXPLICIT_FOLD`] and [`fold_precomposed`], so `Mihăilescu` and
/// `MIHAILESCU` agree. Combining marks are not alphanumeric, so they separate
/// and then vanish, which completes the folding for decomposed text.
///
/// This must stay in exact agreement with `normalise` in
/// `scripts/compile-screen`.
pub(super) fn tokenise(text: &str) -> Vec<String> {
    let folded: String = text
        .chars()
        .flat_map(char::to_lowercase)
        .map(fold_precomposed)
        // Combining marks are DROPPED, not treated as separators. Text that
        // arrives decomposed — some PDF text layers do — writes `ă` as `a`
        // plus a combining breve, and the breve is not alphanumeric, so
        // splitting on it would cut `mihailescu` into `miha` and `ilescu`.
        .filter(|character| !is_combining(*character))
        .collect();
    folded
        .split(|character: char| !character.is_alphanumeric())
        .filter(|token| !token.is_empty())
        .map(ToOwned::to_owned)
        .collect()
}

/// Whether a character is a Unicode combining mark.
///
/// The four blocks that carry Latin diacritics. This is not a complete
/// combining-mark table and does not need to be: the script's NFKD pass is
/// what produces marks in the compiled terms, and it produces them only for
/// letters in the ranges [`fold_precomposed`] covers.
fn is_combining(character: char) -> bool {
    matches!(
        character as u32,
        0x0300..=0x036F | 0x1AB0..=0x1AFF | 0x1DC0..=0x1DFF | 0x20D0..=0x20FF
    )
}

/// Contiguous ranges of precomposed Latin letters, and the base each folds to.
///
/// At module scope because an item declared *after* a statement inside a
/// function reads as though it were scoped to the code above it, and it is not.
const RANGES: &[(char, char, char)] = &[
    ('à', 'å', 'a'),
    ('è', 'ë', 'e'),
    ('ì', 'ï', 'i'),
    ('ò', 'ö', 'o'),
    ('ù', 'ü', 'u'),
    ('ā', 'ą', 'a'),
    ('ć', 'č', 'c'),
    ('ď', 'ď', 'd'),
    ('ē', 'ě', 'e'),
    ('ĝ', 'ģ', 'g'),
    ('ĥ', 'ĥ', 'h'),
    ('ĩ', 'į', 'i'),
    ('ĵ', 'ĵ', 'j'),
    ('ķ', 'ķ', 'k'),
    ('ĺ', 'ľ', 'l'),
    ('ń', 'ň', 'n'),
    ('ō', 'ő', 'o'),
    ('ŕ', 'ř', 'r'),
    ('ś', 'š', 's'),
    ('ţ', 'ť', 't'),
    ('ũ', 'ų', 'u'),
    ('ŵ', 'ŵ', 'w'),
    ('ŷ', 'ÿ', 'y'),
    ('ź', 'ž', 'z'),
    ('ñ', 'ñ', 'n'),
    ('ç', 'ç', 'c'),
    ('ý', 'ý', 'y'),
];

/// Folds one precomposed Latin letter to its base.
///
/// Covers Latin-1 Supplement and Latin Extended-A, which is the range every
/// name in a calibration blocklist has lived in so far. A letter outside it is
/// left alone and its term still matches on its other tokens.
fn fold_precomposed(character: char) -> char {
    if let Some((_, folded)) = EXPLICIT_FOLD.iter().find(|(from, _)| *from == character) {
        return *folded;
    }
    RANGES
        .iter()
        .find_map(|(low, high, base)| {
            (*low <= character && character <= *high).then_some(*base)
        })
        .unwrap_or(character)
}

/// The salted digest of one normalised n-gram.
///
/// Truncated to 32 hex characters, matching `scripts/compile-screen`. The full
/// digest is not needed: this is not a signature, and nothing depends on
/// collision resistance beyond a blocklist entry firing spuriously — a false
/// positive the ledger records and an operator can read.
pub(super) fn digest(salt: &str, ngram: &[String]) -> String {
    let mut hasher = Sha256::new();
    hasher.update(salt.as_bytes());
    hasher.update([0u8]);
    hasher.update(ngram.join(" ").as_bytes());
    hasher.finalize().iter().take(16).fold(
        String::with_capacity(32),
        |mut accumulated, byte| {
            use std::fmt::Write as _;
            let _ = write!(accumulated, "{byte:02x}");
            accumulated
        },
    )
}

/// Every digest reachable from `text`, over n-grams up to `max_ngram` tokens.
///
/// Returned as a set so a caller can intersect against a whole blocklist in one
/// pass rather than testing each term against the text separately. Cost is
/// `max_ngram` times the token count: against the 24,000-character bound on a
/// screened result and a ten-token limit, a few tens of thousands of hashes,
/// which is not measurable beside the network call that produced the text.
pub(super) fn digests_of(salt: &str, text: &str, max_ngram: usize) -> HashSet<String> {
    let tokens = tokenise(text);
    let mut found = HashSet::new();
    for width in 1..=max_ngram.max(1) {
        if width > tokens.len() {
            break;
        }
        for window in tokens.windows(width) {
            found.insert(digest(salt, window));
        }
    }
    found
}

#[cfg(test)]
#[path = "terms_test.rs"]
mod test;
