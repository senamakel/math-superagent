//! The demand side of research: who needs what, and whether they got it.
//!
//! Gathering in this runtime is deliberately reluctant — a download costs a
//! digest, an index row, and a share of every later reader's attention — so
//! the question that matters is when it is *worth* it. Until now that was
//! inferred: a `STUCK` verdict from the loop, a gap named in `ROOT.md`, or an
//! attempt count crossing a threshold. All three are guesses about demand
//! rather than statements of it, and none of them can be closed, so nothing
//! could say whether a search that ran actually answered the thing that
//! prompted it.
//!
//! A request states it instead: what is needed, what the asker would do with
//! it, and what would falsify the belief they are working from. That last
//! field is the one that makes a request worth reading — a gap phrased as
//! "anything on partizan games" is a search; a gap phrased as "whether the
//! pass loop keeps the game a stopper, because if it does not the DP does not
//! terminate" is a question a source can answer or fail to.
//!
//! Two things follow. A request is checked against the claim ledger *before*
//! it is queued, so the common case — the run already knows this and has
//! forgotten — costs a lookup rather than a download; that is the reluctance
//! made mechanical rather than asked for. And a request closes against a
//! claim: the note that answers it carries `answers: <id>`, so "was the gap
//! filled" is read off the library rather than asserted by whoever went
//! looking.

use std::collections::BTreeMap;
use std::fmt::Write as _;

use serde_json::{Value, json};

use super::claims::Ledger;
use super::documents::WorkspaceDocuments;

/// Where the queue's machine-readable form lives.
const LEDGER_PATH: &str = "config/.requests.json";

/// The rendered table, filed with the library it drives.
pub(super) const REQUESTS_PATH: &str = "research/REQUESTS.md";

/// Requests the rendered table carries.
const MAX_ROWS: usize = 30;

/// Characters one stored field is held to.
const MAX_FIELD: usize = 300;

/// Claim-ledger term overlap at which a request is answered from disk instead
/// of being queued.
///
/// Two terms rather than one: a single shared word is how every claim in a
/// library about one subject matches every request about it, and answering a
/// genuine gap with an unrelated claim is worse than not answering it — the
/// asker stops looking.
const ANSWERED_FROM_DISK: usize = 2;

/// One stated gap.
#[derive(Clone, Debug, Default)]
struct Request {
    /// What is needed.
    need: String,
    /// What the asker would do with it.
    why: String,
    /// What would show the asker's current belief is wrong.
    falsifies: String,
}

/// Posts a request, unless the library already answers it.
///
/// Returns the sentence the tool reports. A request answered from disk is not
/// queued: the run has it, and adding a row saying so would send somebody
/// looking for what is already in front of them.
pub(super) async fn post(
    documents: &WorkspaceDocuments,
    need: &str,
    why: &str,
    falsifies: &str,
) -> String {
    let ledger = super::claims::collect(documents.root());
    let found = ledger.search(need);
    let strong: Vec<_> = found
        .into_iter()
        .filter(|claim| overlap(need, claim) >= ANSWERED_FROM_DISK)
        .collect();
    if !strong.is_empty() {
        let detail = strong
            .iter()
            .map(|claim| super::claims::detail(claim))
            .collect::<Vec<_>>()
            .join("\n");
        return format!(
            "not queued — the library already carries {} claim(s) bearing on this. Read these \
             before asking anyone to go looking; if they genuinely do not answer the gap, say so \
             in `need` more precisely and ask again.\n\n{detail}",
            strong.len()
        );
    }

    let mut queue = load(documents).await;
    let id = identifier(need);
    queue.insert(
        id.clone(),
        Request {
            need: truncate(need, MAX_FIELD),
            why: truncate(why, MAX_FIELD),
            falsifies: truncate(falsifies, MAX_FIELD),
        },
    );
    store(documents, &queue).await;
    refresh(documents).await;
    format!(
        "recorded as `{id}` in {REQUESTS_PATH}. It closes when a note carries a claim block with \
         `answers: {id}` — so whoever fills it writes down what was established, and the gap is \
         read off the library rather than declared filled."
    )
}

/// Re-derives the queue's rendered form.
///
/// Which requests are answered is read from the claim ledger, so a request
/// stays open until something on disk actually establishes an answer.
pub(super) async fn refresh(documents: &WorkspaceDocuments) {
    let queue = load(documents).await;
    let ledger = super::claims::collect(documents.root());
    let _ = documents
        .write_runtime(REQUESTS_PATH, &render(&queue, &ledger))
        .await;
}

/// How many of a request's distinctive words a claim carries.
fn overlap(need: &str, claim: &super::claims::Claim) -> usize {
    let haystack = format!("{} {} {}", claim.id, claim.statement, claim.bearing).to_ascii_lowercase();
    need.split(|c: char| !c.is_alphanumeric())
        .filter(|word| word.len() > 4)
        .map(str::to_ascii_lowercase)
        .collect::<std::collections::BTreeSet<_>>()
        .iter()
        .filter(|term| haystack.contains(term.as_str()))
        .count()
}

/// Names a request after what it asks for.
///
/// Derived from the text rather than from a counter or a clock, so the same
/// gap stated twice is one row. Two roles reaching the same wall is a signal
/// worth seeing once, not a queue with the same question in it twice.
fn identifier(need: &str) -> String {
    let mut hash: u64 = 0xcbf2_9ce4_8422_2325;
    for byte in need
        .to_ascii_lowercase()
        .bytes()
        .filter(|byte| !byte.is_ascii_whitespace())
    {
        hash ^= u64::from(byte);
        hash = hash.wrapping_mul(0x0000_0100_0000_01b3);
    }
    let slug: String = need
        .split(|c: char| !c.is_alphanumeric())
        .filter(|word| word.len() > 3)
        .take(3)
        .map(str::to_ascii_lowercase)
        .collect::<Vec<_>>()
        .join("-");
    if slug.is_empty() {
        format!("req-{hash:08x}")
    } else {
        format!("{slug}-{:04x}", hash & 0xffff)
    }
}

fn render(queue: &BTreeMap<String, Request>, ledger: &Ledger) -> String {
    let answered = ledger.answered();
    let mut out = String::from(
        "# Requests — what the run is short of\n\n\
         Posted with `request_research` and rewritten whenever one is posted or a note is \
         written. Do not edit this file; the next write re-derives it.\n\n\
         A request closes when a note carries a claim block with `answers: <id>`. That is \
         deliberate: whoever fills a gap has to write down what was established, so \"was the gap \
         filled\" is read off the library rather than asserted by whoever went looking. An open \
         request with a precise **falsifies** column is the best query this run can hand a \
         search — better than anything available from the problem statement alone.\n\n",
    );
    let mut open: Vec<(&String, &Request)> = queue
        .iter()
        .filter(|(id, _)| !answered.contains(id.as_str()))
        .collect();
    open.sort_by_key(|(id, _)| (*id).clone());
    if open.is_empty() {
        out.push_str("_Nothing outstanding._\n");
    } else {
        out.push_str(
            "| Request | Needed | What it would settle | What would falsify the current belief |\n\
             | --- | --- | --- | --- |\n",
        );
        for (id, request) in open.iter().take(MAX_ROWS) {
            let _ = writeln!(
                out,
                "| `{id}` | {} | {} | {} |",
                cell(&request.need),
                cell(&request.why),
                cell(&request.falsifies)
            );
        }
        if open.len() > MAX_ROWS {
            let _ = writeln!(
                out,
                "\n_{} further open requests not shown._",
                open.len() - MAX_ROWS
            );
        }
    }

    let closed: Vec<&String> = queue
        .keys()
        .filter(|id| answered.contains(id.as_str()))
        .collect();
    if !closed.is_empty() {
        out.push_str("\n## Answered\n\nKept, so the same gap is not re-opened.\n\n");
        for id in closed {
            let _ = writeln!(
                out,
                "- `{id}` — {}",
                queue.get(id).map(|request| request.need.as_str()).unwrap_or_default()
            );
        }
    }
    out
}

fn cell(text: &str) -> String {
    if text.trim().is_empty() {
        return "—".to_string();
    }
    text.replace('|', "\\|").replace('\n', " ")
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

async fn load(documents: &WorkspaceDocuments) -> BTreeMap<String, Request> {
    let Ok(raw) = documents.read_runtime(LEDGER_PATH).await else {
        return BTreeMap::new();
    };
    let Ok(Value::Object(entries)) = serde_json::from_str::<Value>(&raw) else {
        return BTreeMap::new();
    };
    entries
        .into_iter()
        .map(|(id, value)| {
            let request = Request {
                need: string(&value, "need"),
                why: string(&value, "why"),
                falsifies: string(&value, "falsifies"),
            };
            (id, request)
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

async fn store(documents: &WorkspaceDocuments, queue: &BTreeMap<String, Request>) {
    let entries: serde_json::Map<String, Value> = queue
        .iter()
        .map(|(id, request)| {
            (
                id.clone(),
                json!({
                    "need": request.need,
                    "why": request.why,
                    "falsifies": request.falsifies,
                }),
            )
        })
        .collect();
    let Ok(serialised) = serde_json::to_string(&Value::Object(entries)) else {
        return;
    };
    let _ = documents.write_runtime(LEDGER_PATH, &serialised).await;
}

mod tool;

pub(super) use tool::RequestTool;

#[cfg(test)]
mod test;
