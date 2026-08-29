/// How one recall's budget is split across the three durable stores.
///
/// The brain takes half and the other two share the rest, because the brain
/// holds what survived checking and a session transcript is worth less per row
/// than a finding. Every store gets at least one, so a small `limit` narrows
/// each store rather than silencing two of them — a recall that quietly stopped
/// reading the library below some limit would be a gap nobody could see.
pub(super) fn store_budgets(limit: u64) -> [u64; 3] {
    let brain = (limit / 2).max(1);
    let rest = limit.saturating_sub(brain);
    let library = (rest / 2).max(1);
    let session = rest.saturating_sub(library).max(1);
    [brain, library, session]
}

/// What one durable store is called in a recall the model reads.
fn store_heading(store: &str) -> &str {
    match store {
        "store:brain" => "What this project has established",
        "store:library" => "From this project's library",
        "store:session" => "From earlier agent sessions",
        other => other,
    }
}

/// Builds the HTTP client every request to the memory server goes through,
/// carrying this deployment's key and this run's actor on all of them.
///
/// Default headers rather than per-call ones, because the failure of getting
/// either wrong is silent in the direction that matters: a request that forgets
/// the key is answered `401` by a server holding the run's whole memory, and
/// one call site out of nine forgetting it would look like a store that
/// intermittently has nothing. There is one place to add a header and no place
/// to omit one.
///
/// The actor is the project rather than a role, and that is deliberate. It is
/// recorded on every event as `caller`, so it is what a later audit reads to
/// say which run wrote something; a per-role actor would make the memory's
/// provenance depend on which specialist happened to hold the tool.
///
/// # Errors
///
/// Returns an error when the key is empty or holds bytes a header cannot carry.
fn authenticated_client(api_key: &str, project: &str) -> Result<reqwest::Client> {
    let api_key = api_key.trim();
    if api_key.is_empty() {
        return Err(tinyagents::TinyAgentsError::Validation(
            "CORTEX_API_KEY is empty: an unset key is a `401` on every memory call rather than an \
             unauthenticated one. `scripts/memory-up --key <workspace-label>` prints it"
                .into(),
        ));
    }
    let mut key = reqwest::header::HeaderValue::from_str(&format!("Bearer {api_key}")).map_err(
        |_| {
            tinyagents::TinyAgentsError::Validation(
                "CORTEX_API_KEY holds characters an HTTP header cannot carry".into(),
            )
        },
    )?;
    // Marked sensitive so that it stays out of the request logging `reqwest`
    // and its middleware emit, on the same rule the rest of this repository
    // keeps for `.env`.
    key.set_sensitive(true);
    // Bounded at the server's own 64-character segment cap. A workspace label
    // long enough to overflow it would otherwise be rejected on every call.
    let actor = format!("agent:{}", truncate_chars(project, 57));
    let actor = reqwest::header::HeaderValue::from_str(&actor).map_err(|_| {
        tinyagents::TinyAgentsError::Validation(
            "MATH_AGENT_WORKSPACE_LABEL holds characters an HTTP header cannot carry".into(),
        )
    })?;
    let mut headers = reqwest::header::HeaderMap::new();
    headers.insert(reqwest::header::AUTHORIZATION, key);
    headers.insert("X-Cortex-Actor", actor);
    reqwest::Client::builder()
        .default_headers(headers)
        .build()
        .map_err(|error| {
            tinyagents::TinyAgentsError::Tool(format!("could not build the memory client: {error}"))
        })
}

/// Reads `/v1/admin/ready` as a verdict on whether a write now would be
/// recallable later.
///
/// Two things are refusals and they are not the same one. `ready: false` is the
/// server saying a check it needs is failing, and the checks are named so the
/// refusal can quote them. `degraded: true` is the server saying it is storing
/// vectors from a **mock** provider — which it does silently, and which it pins
/// to the data directory so that the damage outlives the outage that caused it.
///
/// A report this runtime cannot read is not a refusal, on the same rule the
/// Cognee path keeps: silence about a field means the server did not claim
/// anything was wrong, and refusing on an unfamiliar shape would stop a memory
/// that works.
fn readiness(report: &Value) -> Readiness {
    if report.get("ready").and_then(Value::as_bool) == Some(false) {
        let failing = report
            .get("checks")
            .and_then(Value::as_object)
            .into_iter()
            .flatten()
            .filter(|(_, check)| check.get("ok").and_then(Value::as_bool) == Some(false))
            .map(|(name, check)| {
                format!(
                    "{name} ({})",
                    check
                        .get("detail")
                        .and_then(Value::as_str)
                        .unwrap_or("no detail given")
                )
            })
            .collect::<Vec<_>>();
        let failing = if failing.is_empty() {
            "it named no failing check".to_string()
        } else {
            failing.join(", ")
        };
        return Readiness::Refusing(format!(
            "the server reports it is not ready: {}",
            truncate_chars(&failing, 300)
        ));
    }
    if report.get("degraded").and_then(Value::as_bool) == Some(true) {
        let provider = report
            .get("embedding_provider")
            .and_then(Value::as_str)
            .unwrap_or("an unnamed provider");
        return Readiness::Refusing(format!(
            "it is running degraded on embedding provider `{provider}`, so what it stores now is \
             pinned to vectors that mean nothing and will not be found by any later recall"
        ));
    }
    Readiness::Ready
}

/// Checks that a write actually reached the barrier it asked for.
///
/// The barrier is the whole reason a durable write blocks, so a `200` that
/// names fewer stages than were asked for is the one answer this must not read
/// as success — it is the server saying it holds bytes it has not indexed,
/// which is the failure Cognee reported 363 times across two workspaces.
///
/// A response that names no stages at all is accepted. `stages_completed` is
/// the server's own reporting rather than a contract this runtime can hold it
/// to, and refusing on its absence would fail every write against a build that
/// simply stopped sending it.
///
/// # Errors
///
/// Returns an error when the stage list is present and does not contain the
/// barrier.
fn reached_barrier(response: &Value, barrier: &str) -> Result<()> {
    let Some(stages) = response.get("stages_completed").and_then(Value::as_array) else {
        return Ok(());
    };
    let reached = stages
        .iter()
        .filter_map(Value::as_str)
        .collect::<Vec<_>>();
    if reached.contains(&barrier) {
        return Ok(());
    }
    Err(tinyagents::TinyAgentsError::Tool(format!(
        "the memory server stored the document but did not reach `{barrier}`: it completed \
         {}. The document is held and not yet recallable",
        if reached.is_empty() {
            "no stage at all".to_string()
        } else {
            reached.join(", ")
        }
    )))
}

/// The singular a `per_layer_limits` key is spelled with.
///
/// The `include` list is plural and the budget map is singular, which is the
/// server's spelling rather than a choice available here; getting it wrong
/// costs the bound silently, since an unrecognised budget key is ignored and
/// the layer comes back at the server's own default.
fn singular(layer: &str) -> &str {
    match layer {
        "events" => "event",
        "episodes" => "episode",
        "facts" => "fact",
        "beliefs" => "belief",
        other => other,
    }
}

/// Renders a stratified pack as the answer to the question that was asked.
///
/// Only the layers the lookup asked for are rendered, and they are rendered in
/// the order [`layers`] names them, so a passage recall reads as passages and a
/// connection recall reads as what the memory concluded. Returning the whole
/// pack would put five layers of scaffolding in the prompt for a question about
/// one — the mistake `render_result` was written to undo on the Cognee side,
/// where a live recall arrived at over twice the tokens of the passage inside
/// it.
///
/// Returns `None` when every layer asked for is empty, so the caller can say
/// "nothing recorded" in its own words.
fn render_pack(pack: &Value, lookup: Lookup) -> Option<String> {
    let mut sections: Vec<String> = Vec::new();
    for layer in layers(lookup) {
        let entries = pack
            .pointer(&format!("/layers/{layer}"))
            .and_then(Value::as_array)
            .map(Vec::as_slice)
            .unwrap_or_default();
        if entries.is_empty() {
            continue;
        }
        let rendered = entries
            .iter()
            .enumerate()
            .map(|(index, entry)| format!("{}. {}", index + 1, render_entry(entry)))
            .collect::<Vec<_>>()
            .join("\n\n");
        sections.push(format!("### {}\n\n{rendered}", heading(layer)));
    }
    (!sections.is_empty()).then(|| sections.join("\n\n"))
}

/// What one layer is called in a recall the model reads.
fn heading(layer: &str) -> &str {
    match layer {
        "events" => "What was recorded",
        "episodes" => "Sessions these came from",
        "facts" => "Facts the memory extracted",
        "beliefs" => "What the memory currently holds",
        "understanding" => "Concepts the memory has synthesised",
        other => other,
    }
}

/// Renders one layer entry as the text it carries, named by where it came from.
///
/// Each layer has its own shape and they share no single text field: an event
/// carries `content.text`, an episode a `summary`, a concept a `name` and a
/// `summary` with a stance and a confidence behind it. The fields are tried in
/// that order and the whole entry is pretty-printed when none of them is
/// present — because a shape this runtime does not recognise is one where
/// guessing which field mattered would lose the answer, and a verbose result
/// beats a silently emptied one.
fn render_entry(entry: &Value) -> String {
    let text = entry
        .pointer("/content/text")
        .and_then(Value::as_str)
        .or_else(|| entry.get("statement").and_then(Value::as_str))
        .or_else(|| entry.get("summary").and_then(Value::as_str))
        .filter(|text| !text.trim().is_empty());
    let Some(text) = text else {
        return truncate_chars(
            &serde_json::to_string_pretty(entry).unwrap_or_else(|_| entry.to_string()),
            PASSAGE_CLIP,
        );
    };
    let body = truncate_chars(text, PASSAGE_CLIP);
    let rendered = match entry.get("name").and_then(Value::as_str) {
        Some(name) => format!("**{name}** — {body}"),
        None => body,
    };
    let mut provenance: Vec<String> = Vec::new();
    if let Some(scope) = entry.get("scope").and_then(Value::as_str) {
        provenance.push(format!("from {scope}"));
    }
    // A concept states how well it is held as well as what it says, and a run
    // reading "supported, 0.7" acts differently from one reading "contested,
    // 0.3". Dropping it would render a hedge as a fact.
    if let Some(stance) = entry.get("stance").and_then(Value::as_str) {
        match entry.get("confidence").and_then(Value::as_f64) {
            Some(confidence) => provenance.push(format!("{stance}, confidence {confidence:.2}")),
            None => provenance.push(stance.to_string()),
        }
    }
    if provenance.is_empty() {
        rendered
    } else {
        format!("{rendered}\n\n({})", provenance.join("; "))
    }
}

fn cortex_transport_error(error: &reqwest::Error) -> tinyagents::TinyAgentsError {
    tinyagents::TinyAgentsError::Tool(format!("CortexDB request failed: {error}"))
}

/// Renders a refusal in the server's own words, naming its error code.
///
/// `CortexDB` answers a refusal with `{error_code, message, retriable}`, and the
/// code is the half worth surfacing: `POLICY_DENIED` and `RATE_LIMITED` want
/// different things from the caller, and a run told only "403" cannot tell
/// them apart.
async fn cortex_response_error(
    operation: &str,
    response: reqwest::Response,
) -> tinyagents::TinyAgentsError {
    let status = response.status();
    let body = response
        .text()
        .await
        .unwrap_or_else(|_| "unreadable response".into());
    let detail = serde_json::from_str::<Value>(&body)
        .ok()
        .and_then(|parsed| {
            let code = parsed.get("error_code").and_then(Value::as_str)?;
            let message = parsed
                .get("message")
                .and_then(Value::as_str)
                .unwrap_or("no message given");
            Some(format!("{code}: {message}"))
        })
        .unwrap_or_else(|| truncate_chars(&body, 2_000));
    tinyagents::TinyAgentsError::Tool(format!("CortexDB {operation} returned {status}: {detail}"))
}
