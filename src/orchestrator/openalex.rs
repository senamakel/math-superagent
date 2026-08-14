//! Walking the citation graph out from a paper the run already holds.
//!
//! Search and this answer different questions, and the difference is the whole
//! argument for adding it. A query asks *what is this called*, and every hit it
//! returns was ranked by what the wider web thinks of a page. A citation asks
//! *what did this author consider load-bearing*, and the answer was written by
//! somebody who had read the subject. No rewording of a query recovers the
//! second, which is why a run that only searches keeps meeting the same six
//! famous papers and never the survey that all six cite.
//!
//! [`super::frontier`] already makes this argument and already acts on it, for
//! the links a downloaded page happens to carry. That is the same idea reaching
//! only as far as the anchors in one HTML document — so a PDF, which is most of
//! the mathematics worth reading, contributes nothing at all, and an abstract
//! page contributes its publisher's navigation. This module asks a bibliographic
//! index the question directly, and gets back what a text converter cannot see:
//! the works this one cites, the works that cite it, and the title, year, venue
//! and citation count of each.
//!
//! Both directions are worth having and they are not the same lead. What a paper
//! cites is its foundation — the definitions and theorems the run has to hold
//! before the paper means anything — and is a fixed set that will never grow.
//! What cites *it* is the frontier in the ordinary sense: who took this further,
//! who found the error in it, who applied it to the adjacent problem. A run
//! stuck on a 1974 bound wants the second and usually asks for the first.
//!
//! Nothing here decides what is worth reading. Every work found is filed into
//! [`super::frontier`] as a lead with its citation count and the direction it
//! was found in, and the librarian reads the ranked table and chooses — the
//! same division of labour the frontier module records, for the same reason:
//! whether a source is worth a download is a judgement, and this module
//! measures.
//!
//! # Why `OpenAlex`
//!
//! It answers both directions with no key, which matters more than it sounds.
//! A key is a thing that expires, is absent in a test, and turns a source
//! adapter into a configuration question; `oeis_lookup` needs none either, and
//! the two together are the run's only lookups that cannot fail for a reason
//! nobody can see. It also indexes preprints, so an arXiv identifier — which is
//! what a mathematics run actually has in hand — resolves without a detour
//! through a publisher.

use std::fmt::Write as _;
use std::sync::Arc;

use async_trait::async_trait;
use serde_json::{Value, json};

use super::documents::WorkspaceDocuments;
use super::readable::LinkRecord;
use super::text::truncate;
use crate::agent::{Result, Tool, ToolCall, ToolResult, ToolSchema};

/// The index every lookup here goes to.
const API: &str = "https://api.openalex.org/works";

/// The address `OpenAlex` asks callers to identify themselves with.
///
/// It buys the "polite pool", which is a faster and more reliably available
/// tier of the same free service. It is deliberately a project address rather
/// than anything belonging to whoever is running this: a run must not put a
/// person's mail in a query string, and a shared address is what the pool is
/// for.
const MAILTO: &str = "riemann-agent@example.invalid";

/// Fields asked for on every work.
///
/// Asked for explicitly because the default record carries per-year citation
/// breakdowns, topic scores, and funder metadata, and a fifty-work reply of
/// those is megabytes of JSON to reach fifty titles. Everything named here ends
/// up in the filed note or the frontier row.
const SELECT: &str = "id,doi,display_name,publication_year,cited_by_count,authorships,\
                      primary_location,type";

/// Fields asked for on the seed work alone.
///
/// The abstract and the reference count are worth the bytes once and not fifty
/// times over.
const SEED_SELECT: &str = "id,doi,display_name,publication_year,cited_by_count,authorships,\
                           primary_location,type,abstract_inverted_index,referenced_works_count";

/// Works one direction may return.
///
/// The cap is on the reply rather than on the frontier, which does its own
/// ranking across every source it holds. Fifty is where a heavily cited paper
/// stops naming its successors and starts naming its field.
const MAX_WORKS: u64 = 50;

/// Works one direction returns when the caller says nothing.
const DEFAULT_WORKS: u64 = 25;

/// Characters kept from a reconstructed abstract.
const MAX_ABSTRACT: usize = 2_400;

/// Authors named before a work is credited to the first of them.
const MAX_AUTHORS: usize = 6;

/// Walks the citation graph out from one work.
#[derive(Debug)]
pub(crate) struct CitationGraphTool {
    documents: WorkspaceDocuments,
}

impl CitationGraphTool {
    /// Builds the tool set this module contributes.
    pub(in crate::orchestrator) fn all(documents: &WorkspaceDocuments) -> Vec<Arc<dyn Tool<()>>> {
        vec![Arc::new(Self {
            documents: documents.clone(),
        })]
    }

    /// Fetches one `OpenAlex` URL and parses the reply.
    async fn get(&self, url: &reqwest::Url) -> Result<Value> {
        let body = self.documents.fetch_text(url.as_str()).await?;
        serde_json::from_str(&body).map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!("the OpenAlex reply could not be read: {error}"))
        })
    }

    /// Resolves what the caller named to one work record.
    ///
    /// A caller has whatever the source it is reading gave it — a DOI from a
    /// reference list, an arXiv number from a preprint, a title from a search
    /// result — and requiring one spelling would mean the model converting
    /// between them by guessing, which is how a run files the wrong paper under
    /// the name it wanted. So all four are accepted and the conversion happens
    /// here, where it is a rule rather than a recollection.
    async fn resolve(&self, work: &str) -> Result<Value> {
        let work = work.trim();
        if let Some(id) = openalex_id(work) {
            return self
                .get(&direct(&format!("{API}/{id}"), SEED_SELECT)?)
                .await
                .map_err(|_| unresolved(work, "that OpenAlex id"));
        }
        if let Some(doi) = doi(work) {
            return self
                .get(&direct(&format!("{API}/doi:{doi}"), SEED_SELECT)?)
                .await
                .map_err(|_| unresolved(work, &format!("the DOI `{doi}`")));
        }
        // A title is a search, and a search can be wrong — so unlike the three
        // identifier paths this one returns something the caller has to check,
        // and the filed note names what was matched for exactly that reason.
        let url = query(&[
            ("search", work),
            ("per-page", "1"),
            ("select", SEED_SELECT),
        ])?;
        let found = self.get(&url).await?;
        found
            .get("results")
            .and_then(Value::as_array)
            .and_then(|results| results.first())
            .cloned()
            .ok_or_else(|| {
                tinyagents::TinyAgentsError::Tool(format!(
                    "OpenAlex has no work matching `{work}`. If that was a title, try the DOI or \
                     the arXiv identifier instead — a title match is the one lookup here that can \
                     silently return the wrong paper, so it fails rather than guessing"
                ))
            })
    }

    /// Returns the works on one side of the seed.
    ///
    /// `cited_by` is `OpenAlex`'s name for "works this one cites" and `cites` for
    /// "works that cite this one", which read backwards and are the single
    /// easiest thing to get wrong here; they are written once, here, and the
    /// caller asks in the direction a reader would name.
    async fn neighbours(&self, id: &str, direction: Direction, limit: u64) -> Result<Vec<Value>> {
        let filter = match direction {
            Direction::References => format!("cited_by:{id}"),
            Direction::Citations => format!("cites:{id}"),
        };
        let limit = limit.to_string();
        let url = query(&[
            ("filter", filter.as_str()),
            ("per-page", limit.as_str()),
            // Most cited first in both directions. A reference list has no
            // useful order of its own — OpenAlex returns it in whatever order
            // it holds — and for citations this is the difference between the
            // survey everyone reads and the twelfth paper to mention the result
            // in passing.
            ("sort", "cited_by_count:desc"),
            ("select", SELECT),
        ])?;
        Ok(self
            .get(&url)
            .await?
            .get("results")
            .and_then(Value::as_array)
            .cloned()
            .unwrap_or_default())
    }
}

/// Which way along the graph one request looks.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
enum Direction {
    /// What the seed cites: the foundation it was built on.
    References,
    /// What cites the seed: who took it further, applied it, or corrected it.
    Citations,
}

impl Direction {
    /// How the filed note and the frontier row name this direction.
    const fn heading(self) -> &'static str {
        match self {
            Self::References => "References — what it is built on",
            Self::Citations => "Cited by — who took it further",
        }
    }

    /// The sentence stored beside a lead, saying why it is a lead.
    fn context(self, seed: &str) -> String {
        match self {
            Self::References => format!("cited by {seed}"),
            Self::Citations => format!("cites {seed}"),
        }
    }
}

/// Builds a URL onto the works endpoint with the polite-pool address attached.
fn query(params: &[(&str, &str)]) -> Result<reqwest::Url> {
    let mut all = params.to_vec();
    all.push(("mailto", MAILTO));
    reqwest::Url::parse_with_params(API, all).map_err(|error| {
        tinyagents::TinyAgentsError::Tool(format!("could not build the OpenAlex query: {error}"))
    })
}

/// Builds a URL onto one work's own record.
fn direct(base: &str, select: &str) -> Result<reqwest::Url> {
    reqwest::Url::parse_with_params(base, [("select", select), ("mailto", MAILTO)]).map_err(
        |error| {
            tinyagents::TinyAgentsError::Tool(format!("could not build the OpenAlex query: {error}"))
        },
    )
}

/// Says an identifier did not resolve, and refuses to guess past it.
///
/// The failure this replaces was a raw `404 Not Found` with a hundred-character
/// query string in it, which tells a model nothing it can act on. A live smoke
/// test hit it on `math/0211159`: `OpenAlex` holds pre-2007 arXiv preprints with
/// no DOI at all, so the identifier arXiv itself would mint resolves to nothing.
///
/// It deliberately does **not** fall back to searching the identifier as a
/// title. That was tried against the live index and returned a *different*
/// paper — "Notes on Perelman's papers" for Perelman's paper — which is the one
/// failure this whole module is written against: a lookup that quietly hands
/// back the wrong work is worse than one that fails, because the run files it
/// under the name it wanted.
fn unresolved(work: &str, what: &str) -> tinyagents::TinyAgentsError {
    tinyagents::TinyAgentsError::Tool(format!(
        "OpenAlex has no work under {what}, so `{work}` could not be resolved. Pre-2007 arXiv \
         identifiers are the common case: OpenAlex indexes those preprints without a DOI, so \
         there is nothing to look up by. Try the published version's DOI, or the exact title — \
         and check the title match names the paper you meant, because a title search can return \
         a different one"
    ))
}

/// Reads an `OpenAlex` work identifier out of what the caller named.
fn openalex_id(work: &str) -> Option<String> {
    let candidate = work
        .trim()
        .trim_start_matches("https://openalex.org/")
        .trim_start_matches("http://openalex.org/")
        .trim_start_matches("https://api.openalex.org/works/");
    let rest = candidate.strip_prefix('W').or_else(|| candidate.strip_prefix('w'))?;
    (!rest.is_empty() && rest.chars().all(|character| character.is_ascii_digit()))
        .then(|| format!("W{rest}"))
}

/// Reads a DOI out of what the caller named, converting an arXiv number to one.
///
/// arXiv registers a DOI for every preprint under a fixed prefix, so an
/// identifier a mathematics run actually has in hand resolves without the model
/// being asked to know that.
fn doi(work: &str) -> Option<String> {
    let candidate = work
        .trim()
        .trim_start_matches("https://doi.org/")
        .trim_start_matches("http://doi.org/")
        .trim_start_matches("doi:");
    if candidate.starts_with("10.") && candidate.contains('/') {
        return Some(candidate.to_string());
    }
    let arxiv = candidate
        .trim_start_matches("https://arxiv.org/abs/")
        .trim_start_matches("http://arxiv.org/abs/")
        .trim_start_matches("arXiv:")
        .trim_start_matches("arxiv:");
    // `2401.01234`, `2401.01234v2`, and the old `math/0211159` all appear in
    // reference lists, and all three are the same kind of thing.
    let looks_like_arxiv = arxiv
        .split_once('.')
        .is_some_and(|(head, _)| head.len() == 4 && head.chars().all(|c| c.is_ascii_digit()))
        || arxiv
            .split_once('/')
            .is_some_and(|(head, tail)| {
                head.chars().all(|c| c.is_ascii_alphabetic())
                    && tail.len() == 7
                    && tail.chars().all(|c| c.is_ascii_digit())
            });
    looks_like_arxiv.then(|| format!("10.48550/arXiv.{arxiv}"))
}

/// The work's canonical landing page.
///
/// The DOI when it has one, because that is the address a reference list will
/// carry and the one [`super::frontier`] can recognise as already fetched. The
/// `OpenAlex` record otherwise, which at least names the work.
fn landing(work: &Value) -> String {
    if let Some(doi) = work.get("doi").and_then(Value::as_str)
        && !doi.is_empty()
    {
        return doi.to_string();
    }
    work.get("id")
        .and_then(Value::as_str)
        .unwrap_or_default()
        .to_string()
}

fn title(work: &Value) -> String {
    work.get("display_name")
        .and_then(Value::as_str)
        .filter(|value| !value.trim().is_empty())
        .unwrap_or("(untitled)")
        .to_string()
}

/// Credits a work the way a citation would.
fn authors(work: &Value) -> String {
    let names: Vec<&str> = work
        .get("authorships")
        .and_then(Value::as_array)
        .into_iter()
        .flatten()
        .filter_map(|authorship| {
            authorship
                .get("author")
                .and_then(|author| author.get("display_name"))
                .and_then(Value::as_str)
        })
        .collect();
    match names.len() {
        0 => "(unattributed)".to_string(),
        count if count > MAX_AUTHORS => format!("{} et al.", names[0]),
        _ => names.join(", "),
    }
}

/// Where the work appeared, when the record says.
fn venue(work: &Value) -> String {
    work.get("primary_location")
        .and_then(|location| location.get("source"))
        .and_then(|source| source.get("display_name"))
        .and_then(Value::as_str)
        .unwrap_or("")
        .to_string()
}

fn year(work: &Value) -> String {
    work.get("publication_year")
        .and_then(Value::as_i64)
        .map_or_else(|| "n.d.".to_string(), |value| value.to_string())
}

fn citations(work: &Value) -> i64 {
    work.get("cited_by_count").and_then(Value::as_i64).unwrap_or(0)
}

/// Rebuilds an abstract from `OpenAlex`'s inverted index.
///
/// The index is a map from each word to the positions it occupies, which is a
/// storage decision rather than a redaction: every word is present and the
/// original is recovered exactly by sorting. Worth doing, because the abstract
/// is the only part of the record that says what the paper *does*, and the
/// alternative is a run downloading a paper to find out whether it is relevant.
fn abstract_text(work: &Value) -> String {
    let Some(index) = work.get("abstract_inverted_index").and_then(Value::as_object) else {
        return String::new();
    };
    let mut placed: Vec<(u64, &str)> = index
        .iter()
        .flat_map(|(word, positions)| {
            positions
                .as_array()
                .into_iter()
                .flatten()
                .filter_map(Value::as_u64)
                .map(move |position| (position, word.as_str()))
        })
        .collect();
    placed.sort_unstable();
    let words: Vec<&str> = placed.into_iter().map(|(_, word)| word).collect();
    truncate(&words.join(" "), MAX_ABSTRACT)
}

/// Renders one work as a table row.
fn row(work: &Value) -> String {
    let venue = venue(work);
    format!(
        "| {} | {} | {} | {} | {} |",
        title(work).replace('|', "\\|"),
        authors(work).replace('|', "\\|"),
        year(work),
        citations(work),
        if venue.is_empty() {
            landing(work)
        } else {
            format!("{} — {}", venue.replace('|', "\\|"), landing(work))
        }
    )
}

/// Renders the note filed under `research/`.
fn note(seed: &Value, sections: &[(Direction, Vec<Value>)]) -> String {
    let mut out = format!("# Citation graph — {}\n\n", title(seed));
    let _ = writeln!(out, "<!-- source: {} -->\n", landing(seed));
    let _ = writeln!(
        out,
        "**{}** ({}). {}. Cited {} times.\n",
        authors(seed),
        year(seed),
        if venue(seed).is_empty() {
            "unpublished or preprint".to_string()
        } else {
            venue(seed)
        },
        citations(seed)
    );
    let summary = abstract_text(seed);
    if !summary.is_empty() {
        let _ = writeln!(out, "## Abstract\n\n{summary}\n");
    }
    for (direction, works) in sections {
        let _ = writeln!(out, "## {}\n", direction.heading());
        if works.is_empty() {
            let _ = writeln!(
                out,
                "OpenAlex holds none. For references that usually means the record is \
                 incomplete rather than that the paper cites nothing; for citations it is a \
                 real signal that nobody has built on this.\n"
            );
            continue;
        }
        let _ = writeln!(out, "| Work | Authors | Year | Cited | Where |");
        let _ = writeln!(out, "| --- | --- | --- | --- | --- |");
        for work in works {
            let _ = writeln!(out, "{}", row(work));
        }
        out.push('\n');
    }
    out.push_str(
        "\n> Filed by a citation-graph lookup, not read. Every work above is a lead and none \
         of them is evidence: the row says a paper exists and how often it is cited, which is \
         not what it establishes. Download the ones that bear on this problem and have the \
         scholar say what they actually prove.\n",
    );
    out
}

/// Turns the works found into leads for the frontier.
fn leads(seed: &str, sections: &[(Direction, Vec<Value>)]) -> Vec<LinkRecord> {
    let mut out: Vec<LinkRecord> = Vec::new();
    for (direction, works) in sections {
        for work in works {
            let url = landing(work);
            if url.is_empty() || out.iter().any(|record| record.url == url) {
                continue;
            }
            out.push(LinkRecord {
                url,
                label: title(work),
                // The citation count rides along in the context sentence
                // because that is the field the frontier's own ranking cannot
                // see — it ranks by in-degree within *this* library, and a work
                // the library has met once may still be the standard reference
                // for the whole subject.
                context: format!(
                    "{} ({}, cited {} times)",
                    direction.context(seed),
                    year(work),
                    citations(work)
                ),
            });
        }
    }
    out
}

#[async_trait]
impl Tool<()> for CitationGraphTool {
    fn name(&self) -> &'static str {
        "citation_graph"
    }

    fn description(&self) -> &'static str {
        "Walks the citation graph out from one paper: what it cites, and what cites it. Give it a \
         DOI, an arXiv identifier, an OpenAlex id, or a title. This answers what a search cannot — \
         a query returns what a subject is called, a citation says what somebody who had read the \
         subject thought was load-bearing — so use it on every source worth holding. What a paper \
         cites is the foundation you need before it means anything; what cites it is who took it \
         further, applied it, or found the error. Every work found is filed as a lead in the \
         frontier with its citation count."
    }

    fn schema(&self) -> ToolSchema {
        ToolSchema::new(
            self.name(),
            self.description(),
            json!({
                "type": "object",
                "properties": {
                    "work": {
                        "type": "string",
                        "description": "The paper to walk out from: a DOI (10.1017/…), an arXiv \
                                        identifier (2401.01234 or math/0211159), an OpenAlex id \
                                        (W2741809807), or an exact title. Prefer an identifier — \
                                        a title match can return the wrong paper."
                    },
                    "direction": {
                        "type": "string",
                        "enum": ["references", "citations", "both"],
                        "description": "`references` for what it is built on, `citations` for who \
                                        took it further, `both` by default. Ask for citations \
                                        when the run is stuck on an old result; ask for \
                                        references when it lacks the definitions."
                    },
                    "limit": {
                        "type": "integer",
                        "minimum": 1,
                        "maximum": MAX_WORKS,
                        "description": "Works per direction. Defaults to 25."
                    }
                },
                "required": ["work"],
                "additionalProperties": false
            }),
        )
    }

    async fn call(&self, _state: &(), call: ToolCall) -> Result<ToolResult> {
        self.schema().validate_call(&call)?;
        let work = call
            .arguments
            .get("work")
            .and_then(Value::as_str)
            .map(str::trim)
            .filter(|value| !value.is_empty())
            .ok_or_else(|| {
                tinyagents::TinyAgentsError::Validation(
                    "work must be a DOI, arXiv identifier, OpenAlex id, or title".into(),
                )
            })?;
        let limit = call
            .arguments
            .get("limit")
            .and_then(Value::as_u64)
            .unwrap_or(DEFAULT_WORKS)
            .clamp(1, MAX_WORKS);
        let directions = match call.arguments.get("direction").and_then(Value::as_str) {
            Some("references") => vec![Direction::References],
            Some("citations") => vec![Direction::Citations],
            _ => vec![Direction::References, Direction::Citations],
        };

        let seed = self.resolve(work).await?;
        let id = openalex_id(seed.get("id").and_then(Value::as_str).unwrap_or_default())
            .ok_or_else(|| {
                tinyagents::TinyAgentsError::Tool(
                    "the OpenAlex record carried no identifier to walk from".into(),
                )
            })?;

        let mut sections: Vec<(Direction, Vec<Value>)> = Vec::new();
        for direction in directions {
            sections.push((direction, self.neighbours(&id, direction, limit).await?));
        }

        let found: usize = sections.iter().map(|(_, works)| works.len()).sum();
        let seed_title = title(&seed);
        let path = super::documents::research_path(
            self.documents.root(),
            &format!("citations_{}.md", slug(&id)),
        );
        // Filed rather than only reported, on the argument `oeis_lookup`
        // records: a bibliography quoted into a tool result and nowhere else is
        // a set of citations nobody can check later.
        let stored = self
            .documents
            .write_runtime(&path, &note(&seed, &sections))
            .await
            .is_ok();
        super::frontier::record(
            &self.documents,
            &landing(&seed),
            if stored { &path } else { "" },
            &leads(&seed_title, &sections),
            &self.documents.goal().await,
        )
        .await;

        Ok(ToolResult::text(
            call.id,
            self.name(),
            format!(
                "`{work}` resolved to **{seed_title}** ({}, cited {} times). {found} connected \
                 work{} added to {}, ranked there against everything else this library cites.{} \
                 None of them has been read — the row says a paper exists, not what it \
                 establishes, so download the ones that bear on the problem.",
                year(&seed),
                citations(&seed),
                if found == 1 { "" } else { "s" },
                super::frontier::FRONTIER_PATH,
                if stored {
                    format!(" The bibliography with abstracts is at `{path}`.")
                } else {
                    String::new()
                }
            ),
        ))
    }
}

/// Reduces an identifier to something safe to put in a filename.
fn slug(value: &str) -> String {
    let slug: String = value
        .chars()
        .map(|character| {
            if character.is_ascii_alphanumeric() {
                character.to_ascii_lowercase()
            } else {
                '_'
            }
        })
        .collect();
    let trimmed = slug.trim_matches('_');
    if trimmed.is_empty() {
        "work".into()
    } else {
        trimmed.to_string()
    }
}

#[cfg(test)]
#[path = "openalex_test.rs"]
mod test;
