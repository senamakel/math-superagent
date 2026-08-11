use serde_json::json;

use super::{cross_references, note};

fn entry() -> serde_json::Value {
    json!({
        "number": 788,
        "name": "Total number of 1's in binary expansions of 0, ..., n.",
        "data": "0,1,2,4,5,7,9,12,13,15",
        "formula": [
            "a(2n) = a(n) + a(n-1) + n.",
            "G.f.: (1/(1-x)) * Sum_{k>=0} x^(2^k)/(1-x^(2^(k+1)))."
        ],
        "xref": ["Cf. A000120, A059015.", "See also A083652."],
        "comment": ["Partial sums of A000120."]
    })
}

/// The note carries what the run came for: the terms that matched and the
/// closed form, filed where it can be cited rather than only reported.
#[test]
fn an_entry_is_filed_with_its_terms_and_formulas() {
    let (id, body) = note(&entry());
    assert_eq!(id, "A000788");
    assert!(body.contains("Total number of 1's"));
    assert!(body.contains("0,1,2,4,5,7,9,12,13,15"));
    assert!(body.contains("a(2n) = a(n) + a(n-1) + n."));
    // Provenance, so the formula stays citable.
    assert!(body.contains("https://oeis.org/A000788"));
    // It is a download, not a reading: the digest says what to replace it with.
    assert!(body.contains("Replace this with what it establishes"));
}

/// The `Cf.` line is the encyclopedia's own citation graph, and the sequences
/// on it describe the same structure differently — exactly what the frontier
/// is for.
#[test]
fn cross_references_become_leads() {
    let records = cross_references(&entry(), "A000788");
    let urls: Vec<&str> = records.iter().map(|record| record.url.as_str()).collect();
    assert!(urls.contains(&"https://oeis.org/A000120"), "{urls:?}");
    assert!(urls.contains(&"https://oeis.org/A059015"), "{urls:?}");
    assert!(urls.contains(&"https://oeis.org/A083652"), "{urls:?}");
    // A sequence does not cite itself.
    assert!(!urls.contains(&"https://oeis.org/A000788"));
    // Each lead says where it came from, so the frontier row is legible.
    assert!(
        records
            .iter()
            .all(|record| record.context.contains("A000788"))
    );
}

/// A sequence with no cross-references yields no leads rather than noise.
#[test]
fn an_entry_without_cross_references_yields_nothing() {
    let bare = json!({ "number": 1, "name": "x", "data": "1,2,3" });
    assert!(cross_references(&bare, "A000001").is_empty());
}

/// A missing field is absent from the note rather than rendered as an empty
/// heading, so a thin entry reads as thin.
#[test]
fn absent_sections_are_omitted() {
    let bare = json!({ "number": 4, "name": "The zero sequence.", "data": "0,0,0,0" });
    let (_, body) = note(&bare);
    assert!(!body.contains("## Formula"));
    assert!(!body.contains("## Cross-references"));
    assert!(body.contains("0,0,0,0"));
}
