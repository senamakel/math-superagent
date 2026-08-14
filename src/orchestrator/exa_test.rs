use serde_json::json;

use super::{
    apply_common, extracted_leads, failed, render, render_all, result_leads, results_of, synthesis,
};
use crate::agent::ToolCall;

fn call(arguments: serde_json::Value) -> ToolCall {
    ToolCall {
        id: "call-1".into(),
        name: "tool".into(),
        invalid: None,
        arguments,
    }
}

fn page() -> serde_json::Value {
    json!({
        "url": "https://arxiv.org/abs/2401.01234",
        "title": "Cycles of length a power of two",
        "author": "A. Author",
        "publishedDate": "2024-01-02",
        "summary": "Settles the conjecture for graphs of girth at least five.",
        "highlights": ["every cubic graph contains such a cycle", "the bound is tight"],
        "extras": { "links": ["https://example.org/survey", "https://example.org/original"] }
    })
}

/// A result is rendered with what lets a source be weighed rather than merely
/// cited: who wrote it and when, not only what it is called.
#[test]
fn a_result_carries_its_provenance_and_why_it_matched() {
    let rendered = render(0, &page());
    assert!(rendered.starts_with("1. Cycles of length a power of two"));
    assert!(rendered.contains("https://arxiv.org/abs/2401.01234"));
    assert!(rendered.contains("A. Author · 2024-01-02"));
    assert!(rendered.contains("Settles the conjecture"));
    assert!(rendered.contains("Why it matched: every cubic graph"));
    // Highlights are joined rather than concatenated, so two passages do not
    // read as one sentence.
    assert!(rendered.contains(" … "));
}

/// A result missing everything optional still renders, rather than producing a
/// row of empty separators.
#[test]
fn a_bare_result_renders_without_dangling_separators() {
    let rendered = render(0, &json!({ "url": "https://example.org/x" }));
    assert!(rendered.contains("Untitled"));
    assert!(!rendered.contains(" · "));
    assert!(!rendered.contains("Why it matched"));
}

/// Every result becomes a lead saying why it is one, because a frontier row
/// outlives the turn and a search result does not.
#[test]
fn results_become_leads_that_say_where_they_came_from() {
    let leads = result_leads(&[page()], "resembles https://seed");
    assert_eq!(leads.len(), 1);
    assert_eq!(leads[0].url, "https://arxiv.org/abs/2401.01234");
    assert_eq!(leads[0].label, "Cycles of length a power of two");
    assert_eq!(leads[0].context, "resembles https://seed");
}

/// The same page returned twice is one lead.
#[test]
fn a_repeated_result_is_one_lead() {
    assert_eq!(result_leads(&[page(), page()], "x").len(), 1);
}

/// What a triaged page linked to survives the decision not to download it —
/// which is most of what the page was worth when the verdict was no.
#[test]
fn links_from_a_triaged_page_become_leads() {
    let leads = extracted_leads(&[page()]);
    let urls: Vec<&str> = leads.iter().map(|lead| lead.url.as_str()).collect();
    assert_eq!(urls, ["https://example.org/survey", "https://example.org/original"]);
    assert!(leads[0].context.contains("linked from Cycles of length a power of two"));
}

/// A page that links to itself contributes nothing, and neither does one with
/// no links at all.
#[test]
fn self_links_and_linkless_pages_contribute_nothing() {
    let selfish = json!({
        "url": "https://example.org/a",
        "extras": { "links": ["https://example.org/a", ""] }
    });
    assert!(extracted_leads(&[selfish]).is_empty());
    assert!(extracted_leads(&[json!({ "url": "https://example.org/b" })]).is_empty());
}

/// Unreachable pages are named, because a triage over twenty URLs that quietly
/// returns eleven reads as eleven candidates rather than nine open questions.
#[test]
fn unreachable_pages_are_reported() {
    let reply = json!({
        "results": [page()],
        "statuses": [
            { "id": "https://arxiv.org/abs/2401.01234", "status": "success" },
            { "id": "https://paywalled.example/paper", "status": "error" }
        ]
    });
    let message = failed(&reply);
    assert!(message.contains("1 could not be reached"));
    assert!(message.contains("https://paywalled.example/paper"));
    // A wholly successful batch says nothing rather than saying "0 failed".
    assert!(failed(&json!({ "statuses": [{ "id": "a", "status": "success" }] })).is_empty());
}

/// The synthesis is read from whichever field this revision of the endpoint
/// used, because a reply carrying prose the runtime cannot find is
/// indistinguishable from one carrying none.
#[test]
fn the_synthesis_is_found_wherever_the_endpoint_puts_it() {
    assert_eq!(synthesis(&json!({ "output": { "content": "an answer" } })), "an answer");
    assert_eq!(synthesis(&json!({ "answer": "an answer" })), "an answer");
    assert_eq!(synthesis(&json!({ "content": "an answer" })), "an answer");
    // Whitespace-only prose is no prose, so the next candidate is tried.
    assert_eq!(synthesis(&json!({ "answer": "   ", "content": "real" })), "real");
    assert!(synthesis(&json!({ "results": [] })).is_empty());
}

/// The filters every endpoint here shares are spelled once, so a filter cannot
/// silently do nothing on one of the three.
#[test]
fn shared_filters_are_applied_in_exas_spelling() {
    let mut body = json!({ "query": "x" });
    apply_common(
        &mut body,
        &call(json!({
            "include_domains": ["arxiv.org", " ams.org "],
            "exclude_domains": ["wikipedia.org"],
            "start_published_date": "2000-01-01",
            "end_published_date": "2020-01-01"
        })),
    );
    assert_eq!(body["includeDomains"], json!(["arxiv.org", "ams.org"]));
    assert_eq!(body["excludeDomains"], json!(["wikipedia.org"]));
    assert_eq!(body["startPublishedDate"], "2000-01-01");
    assert_eq!(body["endPublishedDate"], "2020-01-01");
}

/// An absent or empty filter is left off the request rather than sent as an
/// empty list, which Exa reads as "match nothing".
#[test]
fn empty_filters_are_omitted_entirely() {
    let mut body = json!({ "query": "x" });
    apply_common(
        &mut body,
        &call(json!({ "include_domains": [], "start_published_date": "  " })),
    );
    assert!(body.get("includeDomains").is_none());
    assert!(body.get("startPublishedDate").is_none());
}

/// A reply with no results array is empty rather than an error, so a caller
/// says "nothing found" in its own words.
#[test]
fn a_reply_without_results_is_empty() {
    assert!(results_of(&json!({})).is_empty());
    assert!(render_all(&[]).is_empty());
}
