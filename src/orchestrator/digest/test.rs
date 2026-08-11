use std::fmt::Write as _;

use super::{DIGEST_CHARS, digest, split_links};

/// A source already inside the budget is stored whole, with no notice about
/// truncation that did not happen.
#[test]
fn short_source_is_kept_whole() {
    let full = "# Note\n\nA short note.\n";
    assert_eq!(digest(full, "research/L0.0/note.full.md"), full);
}

/// The digest keeps the theorem statements, which is the part a paper is read
/// for, rather than the opening prose it happens to begin with.
#[test]
fn statements_survive_where_leading_prose_would_not() {
    let mut full = String::from("<!-- source: https://example.org/p | converted from PDF -->\n\n");
    full.push_str("# On the pass rule\n\n## 1. Introduction\n\n");
    // Enough motivation to bury the statements past any leading-characters cut.
    for index in 0..80 {
        let _ = write!(
            full,
            "The history of this subject is long and the literature is wide, and this paragraph \
             number {index} recounts a further part of it at some length for the reader.\n\n"
        );
    }
    full.push_str("## 4. The main result\n\n");
    full.push_str("**Theorem 4.1.** Every stopper has a canonical form.\n\n");
    full.push_str("*Proof.* Omitted for brevity in this test fixture.\n\n");
    full.push_str("Definition 4.2. A pseudonumber is an infinite stopper.\n\n");

    let digested = digest(&full, "research/L0.0/pass.full.md");
    assert!(digested.chars().count() < full.chars().count());
    assert!(digested.contains("Every stopper has a canonical form"));
    assert!(digested.contains("A pseudonumber is an infinite stopper"));
    // The outline says what is in the document without carrying its prose.
    assert!(digested.contains("- On the pass rule"));
    assert!(digested.contains("The main result"));
    // A proof is the argument for a statement already captured, and the
    // longest block on the page.
    assert!(!digested.contains("Omitted for brevity"));
    // Provenance survives, because a source whose origin is lost is unciteable.
    assert!(digested.contains("https://example.org/p"));
    assert!(digested.contains("research/L0.0/pass.full.md"));
}

/// Prose about theorems is not a theorem: the label has to open the block.
#[test]
fn prose_mentioning_a_label_is_not_a_statement() {
    let mut full = String::from("# Survey\n\n");
    full.push_str(&"Theorems of this kind are common in the literature. ".repeat(200));
    full.push('\n');
    let digested = digest(&full, "research/L0.0/survey.full.md");
    assert!(!digested.contains("## Statements it makes"));
}

/// A document with no structure to read digests to its leading characters,
/// because for that shape the leading characters are the document.
#[test]
fn unstructured_text_falls_back_to_leading_characters() {
    let full = "1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 ".repeat(200);
    let digested = digest(&full, "research/L0.0/terms.full.md");
    assert!(digested.contains("excerpt ends"));
    assert!(digested.contains("research/L0.0/terms.full.md"));
    assert!(digested.starts_with("> **Digest only"));
}

/// Whatever the shape of the source, the digest stays near its budget: it is
/// routed nowhere, but it is the file every reader of the library opens first.
#[test]
fn digest_stays_near_its_budget() {
    let mut full = String::from("# Paper\n\n");
    for index in 0..60 {
        let _ = write!(full, "## Section {index}\n\n");
        let _ = write!(
            full,
            "**Theorem {index}.** {}\n\n",
            "A long statement that runs on and on and on. ".repeat(40)
        );
    }
    let digested = digest(&full, "research/L0.0/paper.full.md");
    // Header, provenance, and the closing note sit outside the content budget.
    assert!(digested.chars().count() < DIGEST_CHARS * 2);
    assert!(digested.contains("further statements in the full text"));
}

/// The reference list the converter appends is the frontier's business, not
/// the digest's; repeating it here would spend the budget on URLs.
#[test]
fn the_link_list_is_split_off() {
    let full = "# Paper\n\nBody text.\n\n## Links\n\n[1]: https://example.org/a\n";
    let (body, links) = split_links(full);
    assert!(body.contains("Body text"));
    assert!(!body.contains("example.org"));
    assert!(links.contains("https://example.org/a"));
}

/// A document with no reference list splits into itself and nothing.
#[test]
fn a_document_without_links_splits_cleanly() {
    let (body, links) = split_links("# Paper\n\nBody text.\n");
    assert_eq!(body, "# Paper\n\nBody text.\n");
    assert!(links.is_empty());
}
