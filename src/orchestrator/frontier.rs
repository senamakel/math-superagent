//! The citation frontier: sources this run's own sources point at.
//!
//! The converter has always parsed every anchor on a downloaded page into a
//! reference table, and has always then thrown the result away — rendering a
//! `## Links` list at the foot of the document and keeping nothing. That is a
//! citation graph discarded at the moment of maximum information.
//!
//! It is worth keeping because it answers a question search cannot. A search
//! ranks pages by what the wider web thinks of them; a citation says what *the
//! sources this run already trusts* thought was worth pointing at, and it says
//! so in a sentence that explains why. A URL cited by three of the library's
//! sources is the standard reference for the subject, and no amount of
//! rephrasing a query surfaces that fact.
//!
//! So the frontier is ranked mechanically and costs no model call: in-degree
//! first, then how well the citing sentences overlap the run's goal. The
//! librarian reads the top of the table and decides; nothing here decides for
//! it, because whether a source is worth a download is a judgement and this
//! module measures rather than judges.
//!
//! It doubles as the fetch ledger. Every download records its own canonical
//! URL, so a source already in the library is struck through rather than
//! offered again — one live workspace holds two separate notes derived from
//! the same arXiv abstract, fetched twice because nothing remembered the
//! first.

use std::collections::BTreeMap;
use std::fmt::Write as _;

use serde_json::{Value, json};

use super::documents::WorkspaceDocuments;
use super::readable::LinkRecord;

/// Where the frontier's machine-readable form lives.
///
/// Under `config/` with the run's other plumbing, and hidden from the listing
/// for the same reason the document index is: it is bookkeeping, and the file
/// an agent is meant to read is the rendered table beside the library.
const LEDGER_PATH: &str = "config/.frontier.json";

/// The rendered table, filed with the library it describes.
pub(super) const FRONTIER_PATH: &str = "research/FRONTIER.md";

/// Rows the rendered table carries.
///
/// A bound, not a budget. The frontier of a long run reaches thousands of
/// URLs, almost all of them a publisher's navigation; the top of the ranking
/// is the part anybody reads, and rendering the tail would cost every reader
/// of this file the whole page.
const MAX_ROWS: usize = 40;

/// Citations kept per source document.
///
/// A reference page can carry hundreds of anchors. Keeping every one would let
/// a single navigation-heavy download drown the citations of ten papers.
const MAX_PER_SOURCE: usize = 60;

/// Characters a stored citing sentence is held to.
const MAX_CONTEXT: usize = 200;

/// Hosts whose links are navigation rather than citation.
///
/// A publisher's page links its own login, its subject index, and its social
/// accounts from every article. None of it is a lead, all of it outnumbers the
/// references, and the run has no use for any of it.
const IGNORED_HOSTS: [&str; 14] = [
    "facebook.com",
    "twitter.com",
    "x.com",
    "linkedin.com",
    "reddit.com",
    "youtube.com",
    "instagram.com",
    "t.co",
    "creativecommons.org",
    "schema.org",
    "w3.org",
    "adobe.com",
    "apple.com",
    "google.com",
];

/// Path fragments that mark a publisher's plumbing rather than a document.
const IGNORED_FRAGMENTS: [&str; 10] = [
    "/login",
    "/signin",
    "/register",
    "/subscribe",
    "/cart",
    "/privacy",
    "/terms",
    "/cookie",
    "/rss",
    "/feed",
];

/// One candidate source, as the ledger holds it.
#[derive(Clone, Debug, Default)]
struct Candidate {
    /// How many distinct library sources cite it.
    citers: usize,
    /// The anchor text it was first called by.
    label: String,
    /// The sentence explaining why it was cited.
    context: String,
    /// Where the run filed it, empty until it has been downloaded.
    ///
    /// Carried so a refused second download can name the file that already
    /// holds the source, rather than telling an agent only that it may not
    /// have what it asked for.
    path: String,
}

impl Candidate {
    /// Whether the run has already downloaded this source.
    fn fetched(&self) -> bool {
        !self.path.is_empty()
    }
}

/// Records what a freshly downloaded source cites, and re-renders the table.
///
/// Best effort throughout: the frontier is a convenience built on top of a
/// download that has already succeeded, and losing a row must never turn a
/// stored document into a failed tool call.
pub(super) async fn record(
    documents: &WorkspaceDocuments,
    source_url: &str,
    stored_path: &str,
    links: &[LinkRecord],
    goal: &str,
) {
    let mut ledger = load(documents).await;
    // The source itself is now in the library, so it leaves the frontier
    // whether or not anything had cited it.
    ledger
        .entry(super::readable::clean_url(source_url))
        .or_default()
        .path = stored_path.to_string();
    for link in links.iter().filter(|link| worth_offering(&link.url)).take(
        // Bounded per download rather than globally, so one link-heavy page
        // cannot crowd out the references of every paper beside it.
        MAX_PER_SOURCE,
    ) {
        let entry = ledger.entry(link.url.clone()).or_default();
        entry.citers += 1;
        if entry.label.is_empty() {
            entry.label = truncate(&link.label, 90);
        }
        if entry.context.is_empty() {
            entry.context = truncate(&link.context, MAX_CONTEXT);
        }
    }
    store(documents, &ledger).await;
    let rendered = render(&ledger, goal);
    let _ = documents.write_runtime(FRONTIER_PATH, &rendered).await;
}

/// Returns where the run already filed `url`, if it has downloaded it.
///
/// The check is on the canonical form, so the same paper reached by two
/// spellings — with and without a tracking parameter, say — is recognised as
/// one document. One live workspace holds two notes derived from the same
/// arXiv abstract for want of exactly this check.
pub(super) async fn already_fetched(documents: &WorkspaceDocuments, url: &str) -> Option<String> {
    load(documents)
        .await
        .get(&super::readable::clean_url(url))
        .map(|candidate| candidate.path.clone())
        .filter(|path| !path.is_empty())
}

/// Whether a URL is a lead rather than a publisher's furniture.
fn worth_offering(url: &str) -> bool {
    let lowered = url.to_ascii_lowercase();
    if !lowered.starts_with("http") {
        return false;
    }
    let host = lowered
        .split_once("//")
        .map_or("", |(_, rest)| rest.split('/').next().unwrap_or(""));
    if IGNORED_HOSTS
        .iter()
        .any(|ignored| host == *ignored || host.ends_with(&format!(".{ignored}")))
    {
        return false;
    }
    !IGNORED_FRAGMENTS
        .iter()
        .any(|fragment| lowered.contains(fragment))
}

/// Renders the table an agent reads.
fn render(ledger: &BTreeMap<String, Candidate>, goal: &str) -> String {
    let terms = terms(goal);
    let mut ranked: Vec<(&String, &Candidate, usize)> = ledger
        .iter()
        .filter(|(_, candidate)| candidate.citers > 0)
        .map(|(url, candidate)| {
            let overlap = overlap(&terms, &format!("{} {}", candidate.label, candidate.context));
            (url, candidate, overlap)
        })
        .collect();
    // Unfetched before fetched, then in-degree, then goal overlap. A source
    // three of the library's papers cite outranks one that merely uses the
    // run's vocabulary, because agreement between independent sources is the
    // stronger signal and the cheaper one to trust.
    ranked.sort_by(|left, right| {
        left.1
            .fetched
            .cmp(&right.1.fetched)
            .then(right.1.citers.cmp(&left.1.citers))
            .then(right.2.cmp(&left.2))
            .then(left.0.cmp(right.0))
    });

    let mut out = String::from(
        "# Frontier — what this library's own sources cite\n\n\
         Derived from the citations inside every document this run has downloaded, and rewritten \
         on each download. Nothing here has been judged: a row is a lead, not a recommendation.\n\n\
         Ranked by how many of the library's sources cite it, then by how closely the citing \
         sentence matches the goal. A **cited by** count above one means independent sources \
         agree it is the reference for the subject, which is worth more than any single search \
         ranking. A ~~struck-through~~ row is already in the library — do not download it again.\n\n\
         | Cited by | Source | Called | Why it was cited |\n| --- | --- | --- | --- |\n",
    );
    if ranked.is_empty() {
        out.push_str("| — | _(nothing cited yet)_ | | |\n");
        return out;
    }
    let shown = ranked.len().min(MAX_ROWS);
    for (url, candidate, _) in ranked.iter().take(MAX_ROWS) {
        let name = if candidate.fetched {
            format!("~~{url}~~")
        } else {
            (*url).clone()
        };
        let _ = writeln!(
            out,
            "| {} | {name} | {} | {} |",
            candidate.citers,
            cell(&candidate.label),
            cell(&candidate.context)
        );
    }
    if ranked.len() > shown {
        let _ = writeln!(
            out,
            "\n_{} further candidates not shown; they are cited once each._",
            ranked.len() - shown
        );
    }
    out
}

/// Escapes the characters that would break a Markdown table row.
fn cell(text: &str) -> String {
    if text.trim().is_empty() {
        return "—".to_string();
    }
    text.replace('|', "\\|").replace('\n', " ")
}

/// Splits a goal into the words worth matching a citation against.
fn terms(goal: &str) -> Vec<String> {
    goal.split(|c: char| !c.is_alphanumeric())
        .map(str::to_ascii_lowercase)
        // Short words are the ones every document shares, so matching on them
        // ranks by prose style rather than by subject.
        .filter(|word| word.len() > 4)
        .collect()
}

/// Counts how many goal terms a citation's prose carries.
fn overlap(terms: &[String], text: &str) -> usize {
    let lowered = text.to_ascii_lowercase();
    terms
        .iter()
        .filter(|term| lowered.contains(term.as_str()))
        .count()
}

fn truncate(text: &str, limit: usize) -> String {
    let text = text.trim();
    if text.chars().count() <= limit {
        return text.to_string();
    }
    let head: String = text.chars().take(limit).collect();
    let head = head
        .rsplit_once(char::is_whitespace)
        .map_or(head.as_str(), |(body, _)| body);
    format!("{}…", head.trim_end())
}

/// Reads the ledger, treating any failure as an empty frontier.
///
/// A corrupt or missing ledger costs the run its accumulated leads and nothing
/// else, where returning an error here would fail the download that was trying
/// to add to it.
async fn load(documents: &WorkspaceDocuments) -> BTreeMap<String, Candidate> {
    let Ok(raw) = documents.read_runtime(LEDGER_PATH).await else {
        return BTreeMap::new();
    };
    let Ok(Value::Object(entries)) = serde_json::from_str::<Value>(&raw) else {
        return BTreeMap::new();
    };
    entries
        .into_iter()
        .map(|(url, value)| {
            let candidate = Candidate {
                citers: value
                    .get("citers")
                    .and_then(Value::as_u64)
                    .and_then(|count| usize::try_from(count).ok())
                    .unwrap_or_default(),
                label: string(&value, "label"),
                context: string(&value, "context"),
                fetched: value
                    .get("fetched")
                    .and_then(Value::as_bool)
                    .unwrap_or_default(),
            };
            (url, candidate)
        })
        .collect()
}

fn string(value: &Value, key: &str) -> String {
    value
        .get(key)
        .and_then(Value::as_str)
        .unwrap_or_default()
        .to_string()
}

async fn store(documents: &WorkspaceDocuments, ledger: &BTreeMap<String, Candidate>) {
    let entries: serde_json::Map<String, Value> = ledger
        .iter()
        .map(|(url, candidate)| {
            (
                url.clone(),
                json!({
                    "citers": candidate.citers,
                    "label": candidate.label,
                    "context": candidate.context,
                    "fetched": candidate.fetched,
                }),
            )
        })
        .collect();
    let Ok(serialised) = serde_json::to_string(&Value::Object(entries)) else {
        return;
    };
    let _ = documents.write_runtime(LEDGER_PATH, &serialised).await;
}

#[cfg(test)]
mod test;
