/// Reads the shared `limit` argument, clamped to what a prompt can afford.
fn limit_argument(call: &ToolCall) -> u64 {
    call.arguments
        .get("limit")
        .and_then(Value::as_u64)
        .unwrap_or(DEFAULT_LIMIT)
        .clamp(1, MAX_LIMIT)
}

/// The schema fragment both recall tools use for `limit`.
///
/// Written once because the two are the same control over the same budget, and
/// a cap that differed between them would be a cap somebody had to look up.
fn limit_property() -> Value {
    json!({
        "type": "integer",
        "minimum": 1,
        "maximum": MAX_LIMIT,
        "default": DEFAULT_LIMIT,
        "description": "How many results to return. Raise it when surveying what the run knows \
                        about a subject; leave it alone when checking one specific thing."
    })
}

fn string_argument(call: &ToolCall, name: &str) -> Result<String> {
    call.arguments
        .get(name)
        .and_then(Value::as_str)
        .filter(|value| !value.trim().is_empty())
        .map(ToOwned::to_owned)
        .ok_or_else(|| {
            tinyagents::TinyAgentsError::Validation(format!("{name} must be a non-empty string"))
        })
}

fn point_id(text: &str) -> u64 {
    fnv1a(text.as_bytes())
}

/// Names the uploaded source for the extension its bytes actually carry.
///
/// The workspace path always ends `.md` — the runtime stores the *conversion*
/// under that name — so passing it through would upload a PDF called `.md` and
/// invite Cognee to read it as text. The extension is taken from the content
/// type when it names one, and from the bytes when it does not.
fn source_file_name(path: &str, content_type: Option<&str>) -> String {
    let stem = slug(path.strip_suffix(".md").unwrap_or(path));
    format!("source-{stem}.{}", source_extension(content_type))
}

/// The file extension matching a declared content type.
fn source_extension(content_type: Option<&str>) -> &'static str {
    match content_type.map(|value| value.split(';').next().unwrap_or(value).trim()) {
        Some("application/pdf") => "pdf",
        Some("text/html" | "application/xhtml+xml") => "html",
        Some("text/markdown") => "md",
        _ => "txt",
    }
}

/// The MIME type to upload one source under.
///
/// Magic bytes beat the declared type, on the same evidence the download path
/// records: servers mislabel routinely, and a PDF served as `text/html` is
/// still a PDF. Getting this wrong costs the extraction — Cognee would chunk
/// the binary as text — so the cheap check is worth making twice.
fn source_mime(bytes: &[u8], content_type: Option<&str>) -> String {
    if bytes.starts_with(b"%PDF-") {
        return "application/pdf".to_string();
    }
    match content_type.map(|value| value.split(';').next().unwrap_or(value).trim()) {
        Some(declared) if !declared.is_empty() => declared.to_string(),
        _ => "application/octet-stream".to_string(),
    }
}

fn slug(value: &str) -> String {
    let slug = value
        .chars()
        .map(|character| {
            if character.is_ascii_alphanumeric() {
                character.to_ascii_lowercase()
            } else {
                '_'
            }
        })
        .collect::<String>();
    let slug = slug.trim_matches('_');
    if slug.is_empty() {
        "default".into()
    } else {
        slug.to_string()
    }
}

/// The node set this project's completed agent sessions are written under.
fn session_node_set(project: &str) -> String {
    format!("{SESSION_NODE_SET_PREFIX}{project}")
}

/// The node set this project's provisional notes are written under.
fn scratch_node_set(project: &str) -> String {
    format!("{SCRATCH_NODE_SET_PREFIX}{project}")
}

/// The node set this project's downloaded sources are written under.
fn library_node_set(project: &str) -> String {
    format!("{LIBRARY_NODE_SET_PREFIX}{project}")
}

/// The node sets durable recall may read: the shared brain, plus this
/// project's completed sessions and its library.
///
/// This is the scoping that the server actually applies, so it is the one the
/// separation between the three stores now rests on — see
/// [`VectorStore::search_in`]. Every writer builds its `node_set` through the
/// helpers above and this reader consumes the same ones, because a writer and
/// a reader spelling the same scope apart is a leak nothing would report: the
/// documents would simply be filed where recall never looks.
///
/// The scratch is deliberately absent, for the reason [`visible_datasets`]
/// records: provisional arithmetic returned by durable recall is how a run
/// comes to believe something nobody checked. [`VectorStore::recall_scratch`]
/// is the only way in, and it names [`scratch_node_set`] alone.
fn durable_node_sets(project: &str) -> Vec<String> {
    vec![
        BRAIN_NODE_SET.to_string(),
        session_node_set(project),
        library_node_set(project),
    ]
}

/// Picks the datasets one run may read: the shared brain, plus this project's
/// own session memory and library, and nothing else.
///
/// An allowlist rather than a denylist, and that is the correction of a
/// measured leak. The rule used to be "everything except another project's
/// sessions and any scratch", which passes anything a name does not classify —
/// so a live server carrying `project_euler_903_L0`, thirty-six sources an
/// earlier build had ingested, was searched by every run on the box. For a
/// Project Euler problem that is another problem's literature arriving
/// unasked, and at worst its answer. A dataset this runtime does not recognise
/// belongs to another project or an older build, and neither is this run's.
///
/// A session dataset belongs to this project when it *is* this project's
/// dataset, or when it is one of the per-run datasets an older build created
/// underneath it — `<project>__s<nanos>-<pid>`. Matching those too is what lets
/// a run reach the session memory of every earlier run on the same problem
/// instead of only its own, and it recovers the datasets already stranded by
/// the old naming.
///
/// The `__` in the prefix test is load-bearing: without it, project `euler_18`
/// would read `euler_185`'s memory.
///
/// No scratch dataset is ever visible here, not even this project's own. The
/// scratch holds arithmetic that has not survived anything yet, and durable
/// recall returning it would restate the mistake `role_context` was built to
/// avoid: provisional work read as evidence of progress. `recall_scratch` is
/// the only way in, and only the roles doing provisional work hold it.
fn visible_datasets(datasets: &Value, current_session: &str, library: &str) -> Vec<String> {
    let owned_session = format!("{current_session}__");
    datasets
        .as_array()
        .into_iter()
        .flatten()
        .filter_map(|dataset| dataset.get("name").and_then(Value::as_str))
        .filter(|name| {
            *name == BRAIN_DATASET
                || *name == library
                || *name == current_session
                || name.starts_with(&owned_session)
        })
        .map(ToOwned::to_owned)
        .collect()
}

/// Reads Cognee's `/health/detailed` report as a verdict on whether a document
/// posted now would survive.
///
/// The report names each component it depends on and gives each a status; this
/// takes the first one that is not `healthy` and hands its own words back, so
/// the refusal a tool returns says *what* is broken rather than that something
/// is. All six components the server reports — its relational store, its vector
/// store, the graph, file storage, the model endpoint and the embedding service
/// — are on the path an ingest takes, so none of them is one to pass over: the
/// pipeline that dropped 193 findings was stopped by the model endpoint, and a
/// dead file store would drop them just as quietly.
///
/// A report this runtime cannot read is not a refusal. Silence about a
/// component means the server did not claim it was broken, and a runtime that
/// refused writes on an unfamiliar shape would stop a memory that works.
fn indexing_health(report: &Value) -> IngestHealth {
    let Some(components) = report.get("components").and_then(Value::as_object) else {
        return IngestHealth::Ready;
    };
    for (name, component) in components {
        let status = component.get("status").and_then(Value::as_str).unwrap_or("");
        if status.is_empty() || status == "healthy" {
            continue;
        }
        let detail = component
            .get("details")
            .and_then(Value::as_str)
            .unwrap_or("no detail given");
        return IngestHealth::Refusing(format!(
            "{name} is {status} ({})",
            truncate_chars(detail, 300)
        ));
    }
    IngestHealth::Ready
}

fn fnv1a(bytes: &[u8]) -> u64 {
    bytes.iter().fold(0xcbf2_9ce4_8422_2325, |hash, byte| {
        (hash ^ u64::from(*byte)).wrapping_mul(0x0000_0100_0000_01b3)
    })
}

/// Renders both Cognee's plain chunk results and richer result objects.
///
/// A result object carries the passage twice — once as `text` and again as
/// `raw.value` — beside a dozen fields the reader cannot use: `score: null`,
/// `metadata: {}`, `structured: null`, the dataset's UUID. Pretty-printing the
/// object put all of that in the prompt, so a live recall arrived as
/// `{ "dataset_id": null, "kind": "chunk", … }` with the passage escaped inside
/// it, at something over twice the tokens of the passage itself — and the
/// 4,000-character clip then fell inside the scaffolding rather than at the end
/// of the text. The passage is what was asked for, so the passage is what is
/// returned, with the source named when the server gives one.
///
/// Anything without a usable `text` still renders whole. A shape this runtime
/// does not recognise is one where guessing which field mattered would lose the
/// answer, and a verbose result beats a silently emptied one.
fn render_result(value: &Value) -> String {
    if let Value::String(text) = value {
        return text.clone();
    }
    let text = value
        .get("text")
        .and_then(Value::as_str)
        .filter(|text| !text.trim().is_empty());
    match text {
        None => serde_json::to_string_pretty(value).unwrap_or_else(|_| value.to_string()),
        Some(text) => match value.get("dataset_name").and_then(Value::as_str) {
            None => text.to_string(),
            Some(dataset) => format!("{text}\n\n(from {dataset})"),
        },
    }
}

fn cognee_transport_error(error: &reqwest::Error) -> tinyagents::TinyAgentsError {
    tinyagents::TinyAgentsError::Tool(format!("Cognee request failed: {error}"))
}

async fn cognee_response_error(
    operation: &str,
    response: reqwest::Response,
) -> tinyagents::TinyAgentsError {
    let status = response.status();
    let body = response
        .text()
        .await
        .unwrap_or_else(|_| "unreadable response".into());
    tinyagents::TinyAgentsError::Tool(format!(
        "Cognee {operation} returned {status}: {}",
        truncate_chars(&body, 2_000)
    ))
}

fn truncate_chars(text: &str, limit: usize) -> String {
    let mut chars = text.chars();
    let kept = chars.by_ref().take(limit).collect::<String>();
    if chars.next().is_some() {
        format!("{kept}…")
    } else {
        kept
    }
}
