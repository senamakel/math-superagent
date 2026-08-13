/// Query parameters that carry no meaning and cost tokens.
const TRACKING_PARAMS: [&str; 9] = [
    "utm_source",
    "utm_medium",
    "utm_campaign",
    "utm_term",
    "utm_content",
    "fbclid",
    "gclid",
    "mc_cid",
    "ref_src",
];

/// Collects links so each distinct URL is written once.
///
/// A reference page can carry the same long URL a dozen times, and an inline
/// `[text](https://…)` pays for the whole thing at every occurrence. Numbering
/// them and listing each once at the end costs a couple of characters per use
/// instead, which on a real page is the difference between a readable document
/// and one that fills the context with navigation targets.
#[derive(Debug, Default)]
pub(super) struct LinkTable {
    urls: Vec<String>,
    /// Where each distinct URL was first cited, and under what anchor text.
    ///
    /// Only the first occurrence is kept. A page that links the same reference
    /// a dozen times cites it once for a reason and eleven times from a
    /// navigation bar, and the first is the one that came with prose.
    first: Vec<(String, usize)>,
}

impl LinkTable {
    /// Returns the one-based reference number for `url`, adding it if new.
    fn reference(&mut self, url: &str) -> usize {
        let cleaned = clean_url(url);
        if let Some(position) = self.urls.iter().position(|existing| *existing == cleaned) {
            return position + 1;
        }
        self.urls.push(cleaned);
        self.first.push((String::new(), 0));
        self.urls.len()
    }

    /// Records the anchor text and position of a URL's first citation.
    fn cited(&mut self, reference: usize, label: &str, at: usize) {
        if let Some(entry) = self.first.get_mut(reference.saturating_sub(1))
            && entry.1 == 0
        {
            *entry = (label.to_string(), at);
        }
    }

    /// Builds one record per distinct URL, reading context out of `rendered`.
    ///
    /// `rendered` must be the buffer the offsets were taken against — the
    /// conversion output before it is trimmed and its blank lines collapsed —
    /// or the windows land in the wrong place.
    fn records(&self, rendered: &str) -> Vec<LinkRecord> {
        self.urls
            .iter()
            .zip(&self.first)
            .map(|(url, (label, at))| LinkRecord {
                url: url.clone(),
                label: label.clone(),
                context: window(rendered, *at),
            })
            .collect()
    }

    /// Renders the reference list appended below the document.
    fn render(&self) -> String {
        if self.urls.is_empty() {
            return String::new();
        }
        let mut out = String::from("\n\n## Links\n\n");
        for (index, url) in self.urls.iter().enumerate() {
            let _ = writeln!(out, "[{}]: {url}", index + 1);
        }
        out
    }
}

/// Characters of prose kept either side of a citation.
const CONTEXT_BEFORE: usize = 140;

/// Characters of prose kept after a citation.
const CONTEXT_AFTER: usize = 160;

/// Reads a one-line window of prose around byte offset `at`.
///
/// Collapsed to a single line because the window is destined for a table row.
/// An empty result is normal and means the citation carried no prose — a
/// navigation link, or a bare URL on a line of its own.
fn window(text: &str, at: usize) -> String {
    if at == 0 || at > text.len() {
        return String::new();
    }
    let start = floor_boundary(text, at.saturating_sub(CONTEXT_BEFORE));
    let end = ceil_boundary(text, (at + CONTEXT_AFTER).min(text.len()));
    let mut out = collapse_spaces(&text[start..end].replace('\n', " "));
    // Both ends are cut mid-word by construction, so drop the partial words
    // rather than presenting them as text the source wrote.
    if start > 0
        && let Some((_, rest)) = out.split_once(' ')
    {
        out = rest.to_string();
    }
    if end < text.len()
        && let Some((body, _)) = out.rsplit_once(' ')
    {
        out = body.to_string();
    }
    out.trim().to_string()
}

/// Markers introducing a citation in text that has no anchors.
///
/// A converted PDF is the case that matters: a mathematical paper's reference
/// list is where the primary literature on its subject is named, and it names
/// it as arXiv identifiers and DOIs far more often than as URLs. Reading them
/// is the difference between a library that grows by search and one that grows
/// by following what its own sources cite.
const BARE_MARKERS: [&str; 4] = ["http://", "https://", "arxiv:", "doi:"];

/// Extracts citations from text with no markup to read them from.
fn bare_links(text: &str) -> Vec<LinkRecord> {
    let lowered = text.to_ascii_lowercase();
    let mut records: Vec<LinkRecord> = Vec::new();
    let mut cursor = 0;
    while cursor < lowered.len() {
        let Some((at, marker)) = BARE_MARKERS
            .iter()
            .filter_map(|marker| {
                lowered[cursor..]
                    .find(marker)
                    .map(|at| (cursor + at, *marker))
            })
            .min_by_key(|(at, _)| *at)
        else {
            break;
        };
        let rest = &text[at + marker.len()..];
        let body: String = rest
            .chars()
            .take_while(|c| !c.is_whitespace() && !matches!(c, '<' | '>' | '"' | '\\' | '|'))
            .collect();
        let body = body.trim_end_matches(['.', ',', ';', ':', ')', ']', '}', '\'']);
        cursor = at + marker.len() + body.len().max(1);
        if body.is_empty() {
            continue;
        }
        let url = match marker {
            "arxiv:" => format!("https://arxiv.org/abs/{body}"),
            "doi:" => format!("https://doi.org/{body}"),
            _ => format!("{marker}{body}"),
        };
        let url = clean_url(&url);
        if records.iter().any(|record| record.url == url) {
            continue;
        }
        records.push(LinkRecord {
            label: String::new(),
            context: window(text, at),
            url,
        });
    }
    records
}

fn floor_boundary(text: &str, mut index: usize) -> usize {
    while index > 0 && !text.is_char_boundary(index) {
        index -= 1;
    }
    index
}

fn ceil_boundary(text: &str, mut index: usize) -> usize {
    while index < text.len() && !text.is_char_boundary(index) {
        index += 1;
    }
    index
}

/// Rewrites an arXiv abstract URL to the PDF that abstract describes.
///
/// An arXiv `/abs/` page is metadata: title, authors, subject classes, and the
/// site's navigation. It fetches cleanly and converts to perfectly readable
/// Markdown, so nothing downstream can tell it apart from a paper — and it
/// contains no mathematics at all. One live run held nine sources ingested this
/// way, among them the Chase-Hunter-Tao paper proving the random-model analogue
/// of the conjecture it was working on, and correctly concluded from each that
/// there was no usable result in it. Reading `/pdf/` instead costs one
/// substitution and is the difference between a library of abstracts and a
/// library of papers; the PDF text layer is already extracted by [`super::readable`].
fn prefer_arxiv_pdf(url: &str) -> String {
    let Some(rest) = url
        .strip_prefix("https://arxiv.org/abs/")
        .or_else(|| url.strip_prefix("http://arxiv.org/abs/"))
        .or_else(|| url.strip_prefix("https://www.arxiv.org/abs/"))
    else {
        return url.to_string();
    };
    if rest.is_empty() {
        return url.to_string();
    }
    format!("https://arxiv.org/pdf/{rest}")
}

/// Removes tracking parameters and a redundant trailing slash from a URL.
pub(super) fn clean_url(url: &str) -> String {
    let rewritten = prefer_arxiv_pdf(url);
    let url = rewritten.as_str();
    let (base, query) = match url.split_once('?') {
        Some((base, query)) => (base, Some(query)),
        None => (url, None),
    };
    let (query, fragment) = match query {
        Some(query) => match query.split_once('#') {
            Some((query, fragment)) => (Some(query), Some(fragment)),
            None => (Some(query), None),
        },
        None => (None, None),
    };
    let kept: Vec<&str> = query
        .map(|query| {
            query
                .split('&')
                .filter(|pair| {
                    let key = pair.split('=').next().unwrap_or(pair);
                    !TRACKING_PARAMS.contains(&key) && !pair.is_empty()
                })
                .collect()
        })
        .unwrap_or_default();
    let mut out = base.to_string();
    if !kept.is_empty() {
        out.push('?');
        out.push_str(&kept.join("&"));
    }
    if let Some(fragment) = fragment
        && !fragment.is_empty()
    {
        out.push('#');
        out.push_str(fragment);
    }
    out
}
