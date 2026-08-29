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

/// Builds the HTTP client every request to the memory server goes through,
/// carrying this run's tenant key on all of them.
///
/// A default header rather than a per-call one, because the failure of getting
/// it wrong is silent in the direction that matters: a request that forgets the
/// key is answered `401` by a server that holds the run's whole memory, and one
/// call site out of eleven forgetting it would look like a store that
/// intermittently has nothing. There is one place to add a header and no place
/// to omit one.
///
/// # Errors
///
/// Returns an error when the key is empty or holds bytes a header cannot carry.
fn authenticated_client(api_key: &str) -> Result<reqwest::Client> {
    let api_key = api_key.trim();
    if api_key.is_empty() {
        return Err(tinyagents::TinyAgentsError::Validation(
            "COGNEE_API_KEY is empty: the memory server is shared and this run reaches it as its \
             own tenant, so an unset key is a `401` on every memory call rather than an \
             unauthenticated one. `scripts/memory-up --key <workspace-label>` prints it"
                .into(),
        ));
    }
    let mut value = reqwest::header::HeaderValue::from_str(api_key).map_err(|_| {
        tinyagents::TinyAgentsError::Validation(
            "COGNEE_API_KEY holds characters an HTTP header cannot carry".into(),
        )
    })?;
    // The key identifies the tenant whose memory this is. Marked sensitive so
    // that it stays out of the request logging `reqwest` and its middleware
    // emit, on the same rule the rest of this repository keeps for `.env`.
    value.set_sensitive(true);
    let mut headers = reqwest::header::HeaderMap::new();
    headers.insert("X-Api-Key", value);
    reqwest::Client::builder()
        .default_headers(headers)
        .build()
        .map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!("could not build the memory client: {error}"))
        })
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
