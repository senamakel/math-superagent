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

fn fnv1a(bytes: &[u8]) -> u64 {
    bytes.iter().fold(0xcbf2_9ce4_8422_2325, |hash, byte| {
        (hash ^ u64::from(*byte)).wrapping_mul(0x0000_0100_0000_01b3)
    })
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
