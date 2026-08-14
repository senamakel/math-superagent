use serde_json::json;

use super::{Direction, abstract_text, doi, leads, note, openalex_id, row, unresolved};

fn seed() -> serde_json::Value {
    json!({
        "id": "https://openalex.org/W2741809807",
        "doi": "https://doi.org/10.1017/S0305004100034095",
        "display_name": "On the Erdős–Gyárfás conjecture",
        "publication_year": 1997,
        "cited_by_count": 142,
        "type": "article",
        "authorships": [
            { "author": { "display_name": "P. Erdős" } },
            { "author": { "display_name": "A. Gyárfás" } }
        ],
        "primary_location": { "source": { "display_name": "Combinatorica" } },
        "abstract_inverted_index": {
            "Every": [0], "graph": [1, 6], "with": [2], "minimum": [3],
            "degree": [4], "three": [5], "contains": [7], "a": [8], "cycle": [9]
        }
    })
}

fn cited() -> serde_json::Value {
    json!({
        "id": "https://openalex.org/W3",
        "doi": "https://doi.org/10.1000/later",
        "display_name": "A cycle of length a power of two",
        "publication_year": 2012,
        "cited_by_count": 7,
        "authorships": [{ "author": { "display_name": "R. Solver" } }],
        "primary_location": { "source": { "display_name": "JCTB" } }
    })
}

/// The four spellings a reference list actually carries all reach the same
/// work, because the alternative is the model converting between them by
/// guessing.
#[test]
fn identifiers_are_recognised_in_the_forms_sources_carry_them() {
    assert_eq!(openalex_id("W2741809807").as_deref(), Some("W2741809807"));
    assert_eq!(
        openalex_id("https://openalex.org/W2741809807").as_deref(),
        Some("W2741809807")
    );
    assert_eq!(doi("10.1017/S0305004100034095").as_deref(), Some("10.1017/S0305004100034095"));
    assert_eq!(
        doi("https://doi.org/10.1017/S0305004100034095").as_deref(),
        Some("10.1017/S0305004100034095")
    );
    // arXiv is what a mathematics run has in hand, in both the modern and the
    // pre-2007 spelling.
    assert_eq!(doi("2401.01234").as_deref(), Some("10.48550/arXiv.2401.01234"));
    assert_eq!(
        doi("arXiv:2401.01234v2").as_deref(),
        Some("10.48550/arXiv.2401.01234v2")
    );
    assert_eq!(
        doi("math/0211159").as_deref(),
        Some("10.48550/arXiv.math/0211159")
    );
}

/// A title is not an identifier, and must not be mistaken for one — otherwise a
/// search path silently becomes a direct fetch of something that does not exist.
#[test]
fn a_title_is_not_read_as_an_identifier() {
    assert!(openalex_id("On the Erdős–Gyárfás conjecture").is_none());
    assert!(doi("On the Erdős–Gyárfás conjecture").is_none());
    // A bare word starting with W is a word.
    assert!(openalex_id("Weyl").is_none());
}

/// The inverted index is a storage decision, not a redaction: sorting recovers
/// the abstract exactly, and the abstract is the only field saying what the
/// paper does.
#[test]
fn the_abstract_is_reconstructed_in_order() {
    assert_eq!(
        abstract_text(&seed()),
        "Every graph with minimum degree three graph contains a cycle"
    );
}

/// A record without one reads as absent rather than as an empty section.
#[test]
fn a_missing_abstract_is_empty() {
    assert!(abstract_text(&json!({ "display_name": "x" })).is_empty());
}

/// The note carries what a reader needs to choose without downloading: who,
/// when, where, and how heavily cited.
#[test]
fn the_note_carries_both_directions_with_provenance() {
    let sections = vec![
        (Direction::References, vec![cited()]),
        (Direction::Citations, Vec::new()),
    ];
    let body = note(&seed(), &sections);
    assert!(body.contains("On the Erdős–Gyárfás conjecture"));
    assert!(body.contains("P. Erdős, A. Gyárfás"));
    // Provenance, so a lead stays citable.
    assert!(body.contains("https://doi.org/10.1017/S0305004100034095"));
    assert!(body.contains("A cycle of length a power of two"));
    assert!(body.contains("References — what it is built on"));
    // An empty direction says which kind of emptiness it is rather than
    // rendering a headed blank.
    assert!(body.contains("nobody has built on this"));
    // It is a lookup, not a reading.
    assert!(body.contains("none of them is evidence"));
}

/// A pipe in a title must not break the table it is rendered into.
#[test]
fn a_pipe_in_a_title_is_escaped() {
    let awkward = json!({
        "display_name": "Bounds on |E(G)| for cubic graphs",
        "publication_year": 2001,
        "cited_by_count": 3,
        "doi": "https://doi.org/10.1000/pipe"
    });
    let rendered = row(&awkward);
    assert!(rendered.contains("\\|E(G)\\|"), "{rendered}");
    // Five columns and no more, which is what the escape is protecting.
    assert_eq!(rendered.matches(" | ").count(), 4, "{rendered}");
}

/// Every work found becomes a lead saying which way it was found and how
/// heavily it is cited — the field the frontier's own in-degree ranking cannot
/// see.
#[test]
fn works_become_leads_that_say_why() {
    let sections = vec![(Direction::Citations, vec![cited()])];
    let records = leads("On the Erdős–Gyárfás conjecture", &sections);
    assert_eq!(records.len(), 1);
    assert_eq!(records[0].url, "https://doi.org/10.1000/later");
    assert!(records[0].context.contains("cites On the Erdős–Gyárfás conjecture"));
    assert!(records[0].context.contains("cited 7 times"));
    assert!(records[0].context.contains("2012"));
}

/// A work reached in both directions is one lead, not two rows saying different
/// things about the same paper.
#[test]
fn a_work_found_twice_is_one_lead() {
    let sections = vec![
        (Direction::References, vec![cited()]),
        (Direction::Citations, vec![cited()]),
    ];
    assert_eq!(leads("seed", &sections).len(), 1);
}

/// An identifier that resolves to nothing says so in words a model can act on,
/// and names the case a live run actually hit.
///
/// The failure this replaced was a raw 404 with the whole query string in it.
/// `math/0211159` is the real example: `OpenAlex` indexes pre-2007 arXiv
/// preprints without a DOI, so the identifier arXiv would mint resolves to
/// nothing at all.
#[test]
fn an_identifier_that_resolves_to_nothing_says_what_to_try_instead() {
    let message = unresolved("math/0211159", "the DOI `10.48550/arXiv.math/0211159`").to_string();
    assert!(message.contains("math/0211159"), "{message}");
    assert!(message.contains("Pre-2007 arXiv"), "{message}");
    // It names the next move rather than only the failure.
    assert!(message.contains("DOI, or the exact title"), "{message}");
    // And warns about the one fallback this module refuses to make silently.
    assert!(message.contains("can return a different one"), "{message}");
}

/// A record with no DOI still yields a usable lead rather than an empty URL
/// that the frontier would rank and nobody could open.
#[test]
fn a_work_without_a_doi_falls_back_to_its_record() {
    let sections = vec![(
        Direction::References,
        vec![json!({
            "id": "https://openalex.org/W9",
            "display_name": "An unindexed preprint",
            "publication_year": 1968,
            "cited_by_count": 0
        })],
    )];
    let records = leads("seed", &sections);
    assert_eq!(records.len(), 1);
    assert_eq!(records[0].url, "https://openalex.org/W9");
}
