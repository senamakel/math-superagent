/// Extracts a PDF's text layer.
///
/// The extractor is run inside `catch_unwind` because it panics on malformed
/// input, and a panic here would take down work that has nothing to do with
/// this document.
fn pdf_to_text(bytes: &[u8]) -> crate::agent::Result<String> {
    let owned = bytes.to_vec();
    let extracted = std::panic::catch_unwind(move || pdf_extract::extract_text_from_mem(&owned));
    match extracted {
        Ok(Ok(text)) => Ok(text),
        Ok(Err(error)) => Err(tinyagents::TinyAgentsError::Validation(format!(
            "this PDF could not be parsed: {error}. Try the publisher's HTML version, or an \
             abstract or preprint page instead."
        ))),
        Err(_) => Err(tinyagents::TinyAgentsError::Validation(
            "this PDF is malformed enough to crash the text extractor. Use a different source or \
             format."
                .into(),
        )),
    }
}

/// Elements whose entire contents are dropped.
const DROPPED: [&str; 8] = [
    "script", "style", "noscript", "nav", "header", "footer", "aside", "form",
];

/// Converts HTML to Markdown, preserving TeX delimiters and code verbatim.
fn html_to_markdown(html: &str, table: &mut LinkTable) -> String {
    let mut out = String::with_capacity(html.len() / 2);
    let mut chars = html.char_indices().peekable();
    let mut list_stack: Vec<Option<usize>> = Vec::new();
    let mut in_pre = false;
    let mut pending_text = String::new();
    // While inside an anchor, text is buffered here instead of being written
    // out, because the reference number is only emitted once the label is
    // known at the closing tag.
    let mut link_target: Option<String> = None;
    let mut link_text = String::new();

    while let Some((index, character)) = chars.next() {
        if character != '<' {
            pending_text.push(character);
            continue;
        }
        // Flush the text accumulated before this tag into whichever buffer is
        // currently collecting.
        if link_target.is_some() {
            flush_text(&mut link_text, &mut pending_text, in_pre);
        } else {
            flush_text(&mut out, &mut pending_text, in_pre);
        }

        let Some(close) = html[index..].find('>') else {
            break;
        };
        let raw = &html[index + 1..index + close];
        // Advance past the tag body.
        while let Some(&(next, _)) = chars.peek() {
            if next >= index + close {
                chars.next();
                break;
            }
            chars.next();
        }

        if raw.starts_with('!') {
            continue;
        }
        let closing = raw.starts_with('/');
        let name = raw
            .trim_start_matches('/')
            .split(|c: char| c.is_whitespace() || c == '/')
            .next()
            .unwrap_or("")
            .to_ascii_lowercase();

        if DROPPED.contains(&name.as_str()) {
            if !closing && let Some(end) = find_close(html, index, &name) {
                while let Some(&(next, _)) = chars.peek() {
                    if next >= end {
                        break;
                    }
                    chars.next();
                }
            }
            continue;
        }

        apply_tag(
            &mut TagContext {
                out: &mut out,
                list_stack: &mut list_stack,
                in_pre: &mut in_pre,
                link_target: &mut link_target,
                link_text: &mut link_text,
                table,
            },
            &name,
            closing,
            raw,
        );
    }
    if link_target.is_some() {
        // An anchor that never closed: keep its text rather than losing it.
        flush_text(&mut link_text, &mut pending_text, in_pre);
        out.push_str(link_text.trim());
    } else {
        flush_text(&mut out, &mut pending_text, in_pre);
    }
    out
}

/// The mutable state a tag handler acts on.
struct TagContext<'a> {
    out: &'a mut String,
    list_stack: &'a mut Vec<Option<usize>>,
    in_pre: &'a mut bool,
    link_target: &'a mut Option<String>,
    link_text: &'a mut String,
    table: &'a mut LinkTable,
}

/// Emits the Markdown for one opening or closing tag.
fn apply_tag(ctx: &mut TagContext<'_>, name: &str, closing: bool, raw: &str) {
    let out = &mut *ctx.out;
    match (name, closing) {
        ("br", _) => out.push('\n'),
        ("hr", _) => out.push_str("\n\n---\n\n"),
        ("p" | "div" | "section" | "article" | "tr" | "blockquote" | "table", _)
        | ("h1" | "h2" | "h3" | "h4" | "h5" | "h6", true) => ensure_blank_line(out),
        ("h1" | "h2" | "h3" | "h4" | "h5" | "h6", false) => {
            ensure_blank_line(out);
            let level = name[1..].parse::<usize>().unwrap_or(1);
            let _ = write!(out, "{} ", "#".repeat(level.clamp(1, 6)));
        }

        ("ul", false) => {
            ensure_blank_line(out);
            ctx.list_stack.push(None);
        }
        ("ol", false) => {
            ensure_blank_line(out);
            ctx.list_stack.push(Some(1));
        }
        ("ul" | "ol", true) => {
            ctx.list_stack.pop();
            ensure_blank_line(out);
        }
        ("li", false) => {
            trim_trailing_spaces(out);
            if !out.ends_with('\n') {
                out.push('\n');
            }
            let depth = ctx.list_stack.len().saturating_sub(1);
            out.push_str(&"  ".repeat(depth));
            match ctx.list_stack.last_mut() {
                Some(Some(counter)) => {
                    let _ = write!(out, "{counter}. ");
                    *counter += 1;
                }
                _ => out.push_str("- "),
            }
        }
        ("pre", false) => {
            ensure_blank_line(out);
            out.push_str("```\n");
            *ctx.in_pre = true;
        }
        ("pre", true) => {
            *ctx.in_pre = false;
            if !out.ends_with('\n') {
                out.push('\n');
            }
            out.push_str("```\n\n");
        }
        ("code", _) if !*ctx.in_pre => out.push('`'),
        ("strong" | "b", _) => out.push_str("**"),
        ("em" | "i", _) => out.push('*'),
        ("td" | "th", true) => out.push_str(" | "),

        ("img", false) => {
            if let Some(alt) = attribute(raw, "alt")
                && !alt.trim().is_empty()
            {
                let _ = write!(out, "[image: {}]", decode_entities(&alt));
            }
        }
        ("a", false) => {
            if let Some(href) = attribute(raw, "href")
                && !href.starts_with('#')
                && !href.starts_with("javascript:")
            {
                *ctx.link_target = Some(href);
                ctx.link_text.clear();
            }
        }
        ("a", true) => {
            if let Some(href) = ctx.link_target.take() {
                let label = ctx.link_text.trim().to_string();
                let reference = ctx.table.reference(&href);
                if needs_space(out, "[") {
                    out.push(' ');
                }
                ctx.table.cited(reference, &label, out.len());
                if label.is_empty() {
                    let _ = write!(out, "[{reference}]");
                } else {
                    let _ = write!(out, "[{label}][{reference}]");
                }
                ctx.link_text.clear();
            }
        }
        _ => {}
    }
}
