/// Returns the byte offset just past the matching closing tag.
fn find_close(html: &str, from: usize, name: &str) -> Option<usize> {
    let needle = format!("</{name}");
    html[from..]
        .to_ascii_lowercase()
        .find(&needle)
        .map(|offset| from + offset)
}

/// Reads a tag attribute's value.
fn attribute(tag: &str, name: &str) -> Option<String> {
    let lowered = tag.to_ascii_lowercase();
    let position = lowered.find(&format!("{name}="))?;
    let rest = &tag[position + name.len() + 1..];
    let mut characters = rest.chars();
    match characters.next()? {
        quote @ ('"' | '\'') => rest[1..].find(quote).map(|end| rest[1..=end].to_string()),
        _ => Some(
            rest.split(|c: char| c.is_whitespace() || c == '>')
                .next()
                .unwrap_or("")
                .to_string(),
        ),
    }
}

fn flush_text(out: &mut String, pending: &mut String, in_pre: bool) {
    if pending.is_empty() {
        return;
    }
    let decoded = decode_entities(pending);
    if in_pre {
        out.push_str(&decoded);
    } else {
        let collapsed = collapse_spaces(&decoded);
        if !collapsed.is_empty() {
            if needs_space(out, &collapsed) {
                out.push(' ');
            }
            out.push_str(&collapsed);
        }
    }
    pending.clear();
}

fn needs_space(out: &str, next: &str) -> bool {
    match out.chars().last() {
        None | Some('\n' | ' ' | '[' | '`' | '*' | '#' | '\u{0}') => false,
        Some(_) => !next.starts_with([',', '.', ';', ':', ')', ']', '!', '?']),
    }
}

fn collapse_spaces(text: &str) -> String {
    let mut out = String::with_capacity(text.len());
    let mut in_space = false;
    for character in text.chars() {
        if character.is_whitespace() {
            in_space = true;
        } else {
            if in_space && !out.is_empty() {
                out.push(' ');
            }
            in_space = false;
            out.push(character);
        }
    }
    if in_space && !out.is_empty() {
        out.push(' ');
    }
    out
}

fn ensure_blank_line(out: &mut String) {
    trim_trailing_spaces(out);
    if out.is_empty() {
        return;
    }
    while !out.ends_with("\n\n") {
        out.push('\n');
        if out.len() > 2 && out.ends_with("\n\n") {
            break;
        }
        if out.ends_with("\n\n") {
            break;
        }
        if out.chars().rev().take_while(|c| *c == '\n').count() >= 2 {
            break;
        }
    }
}

fn trim_trailing_spaces(out: &mut String) {
    while out.ends_with(' ') || out.ends_with('\t') {
        out.pop();
    }
}

fn collapse_blank_lines(text: &str) -> String {
    let mut out = String::with_capacity(text.len());
    let mut blanks = 0;
    for line in text.lines() {
        let trimmed = line.trim_end();
        if trimmed.is_empty() {
            blanks += 1;
            if blanks > 1 {
                continue;
            }
        } else {
            blanks = 0;
        }
        out.push_str(trimmed);
        out.push('\n');
    }
    out.trim().to_string()
}

/// Bytes searched for an entity's closing `;`.
///
/// An entity is short — the longest this decodes is `&hellip;` at eight bytes,
/// and a numeric one like `&#x2264;` is the same — so a bare ampersand must not
/// send the scan to the end of the document looking for a semicolon that
/// belongs to something else.
const MAX_ENTITY_BYTES: usize = 12;

/// The longest prefix of `text` within `limit` bytes that ends on a character
/// boundary.
///
/// Slicing to a byte index is what a bounded scan wants and what Rust will not
/// give you: `&text[..12]` panics when the twelfth byte is in the middle of a
/// character. That is not a rare input here. A live download aborted on
/// ordinary prose with `end byte index 12 is not a char boundary; it is inside
/// '–'`, and because the conversion runs on a tokio worker the panic surfaced
/// as a failed tool call with no reason attached to it.
///
/// Backing up to the boundary loses nothing the caller wanted. Every entity
/// this decodes is ASCII, so a multi-byte character inside the window is proof
/// that the window holds no entity — the shortened prefix cannot hide a `;`
/// that a correct scan would have found.
fn bounded_prefix(text: &str, limit: usize) -> &str {
    if text.len() <= limit {
        return text;
    }
    let mut end = limit;
    while end > 0 && !text.is_char_boundary(end) {
        end -= 1;
    }
    &text[..end]
}

/// Decodes the HTML entities that appear in mathematical prose.
fn decode_entities(text: &str) -> String {
    if !text.contains('&') {
        return text.to_string();
    }
    let mut out = String::with_capacity(text.len());
    let mut rest = text;
    while let Some(start) = rest.find('&') {
        out.push_str(&rest[..start]);
        let tail = &rest[start..];
        let Some(end) = bounded_prefix(tail, MAX_ENTITY_BYTES).find(';') else {
            out.push('&');
            rest = &tail[1..];
            continue;
        };
        let entity = &tail[1..end];
        let decoded = match entity {
            "amp" => Some("&".to_string()),
            "lt" => Some("<".to_string()),
            "gt" => Some(">".to_string()),
            "quot" => Some("\"".to_string()),
            "apos" | "#39" => Some("'".to_string()),
            "nbsp" | "#160" => Some(" ".to_string()),
            "mdash" => Some("—".to_string()),
            "ndash" => Some("–".to_string()),
            "hellip" => Some("…".to_string()),
            "times" => Some("×".to_string()),
            "minus" => Some("−".to_string()),
            "le" => Some("≤".to_string()),
            "ge" => Some("≥".to_string()),
            other => other
                .strip_prefix('#')
                .and_then(|digits| {
                    digits.strip_prefix('x').map_or_else(
                        || digits.parse::<u32>().ok(),
                        |hex| u32::from_str_radix(hex, 16).ok(),
                    )
                })
                .and_then(char::from_u32)
                .map(|c| c.to_string()),
        };
        if let Some(value) = decoded {
            out.push_str(&value);
            rest = &tail[end + 1..];
        } else {
            out.push('&');
            rest = &tail[1..];
        }
    }
    out.push_str(rest);
    out
}
