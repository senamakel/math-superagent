/// Headroom between a wait's own expiry and the deadline around it.
///
/// The wait must be the thing that ends, because it ends by *returning* — with
/// the child's state as it stands. A deadline that fired first would replace
/// that with an error, which is the failure this exists to prevent.
const AWAIT_GRACE_SECONDS: u64 = 60;

fn run_id_schema(max_wait_seconds: Option<u64>) -> Value {
    match max_wait_seconds {
        Some(maximum) => json!({
            "type": "object",
            "properties": {
                "run_id": { "type": "string" },
                "wait_seconds": { "type": "integer", "minimum": 0, "maximum": maximum }
            },
            "required": ["run_id"],
            "additionalProperties": false
        }),
        None => json!({
            "type": "object",
            "properties": { "run_id": { "type": "string" } },
            "required": ["run_id"],
            "additionalProperties": false
        }),
    }
}

/// Shortens a spawn prompt for the operator-facing console line.
fn preview_input(input: &str) -> String {
    const PREVIEW_CHARS: usize = 160;
    let collapsed = input.split_whitespace().collect::<Vec<_>>().join(" ");
    if collapsed.chars().count() <= PREVIEW_CHARS {
        return collapsed;
    }
    let kept = collapsed.chars().take(PREVIEW_CHARS).collect::<String>();
    format!("{kept}...")
}

fn required_string(arguments: &Value, name: &str) -> Result<String> {
    arguments
        .get(name)
        .and_then(Value::as_str)
        .filter(|value| !value.trim().is_empty())
        .map(ToOwned::to_owned)
        .ok_or_else(|| {
            tinyagents::TinyAgentsError::Validation(format!("{name} must be a non-empty string"))
        })
}
