//! Unit tests for document conversion and URL compression.

use super::{Format, LinkTable, clean_url, decode_entities, detect, html_to_markdown, to_markdown};

fn render(html: &str) -> String {
    let mut table = LinkTable::default();
    html_to_markdown(html, &mut table)
}

#[test]
fn magic_bytes_beat_a_mislabelled_content_type() {
    // Servers mislabel routinely; a PDF served as text/html is still a PDF.
    assert_eq!(detect(b"%PDF-1.7\nstuff", Some("text/html")), Format::Pdf);
    assert_eq!(
        detect(b"<!DOCTYPE html><p>x", Some("text/plain")),
        Format::Html
    );
    assert_eq!(detect(b"plain words", Some("text/plain")), Format::Text);
    assert_eq!(
        detect(&[0xff, 0xd8, 0xff, 0xe0, 0x00], Some("image/jpeg")),
        Format::Binary
    );
}

#[test]
fn headings_paragraphs_and_lists_become_markdown() {
    let markdown = render("<h2>Method</h2><p>First.</p><ul><li>one</li><li>two</li></ul>");
    assert!(markdown.contains("## Method"));
    assert!(markdown.contains("First."));
    assert!(markdown.contains("- one"));
    assert!(markdown.contains("- two"));
}

#[test]
fn ordered_lists_are_numbered() {
    let markdown = render("<ol><li>alpha</li><li>beta</li></ol>");
    assert!(markdown.contains("1. alpha"));
    assert!(markdown.contains("2. beta"));
}

#[test]
fn scripts_styles_and_navigation_are_dropped_entirely() {
    let markdown = render(
        "<nav>Home About</nav><script>var x = 1;</script><style>p{color:red}</style><p>Real.</p>",
    );
    assert!(markdown.contains("Real."));
    assert!(!markdown.contains("var x"));
    assert!(!markdown.contains("color:red"));
    assert!(!markdown.contains("About"));
}

#[test]
fn tex_delimiters_survive_conversion() {
    // The whole reason this converter is hand-written: a general-purpose one
    // escapes the backslashes and destroys the mathematics.
    let markdown = render(r"<p>Consider \(x^2 - Dy^2 = 1\) for \(D \le 1000\).</p>");
    assert!(markdown.contains(r"\(x^2 - Dy^2 = 1\)"));
    assert!(markdown.contains(r"\(D \le 1000\)"));
}

#[test]
fn entities_are_decoded_including_numeric_and_hex() {
    assert_eq!(decode_entities("a &amp; b"), "a & b");
    assert_eq!(decode_entities("&lt;tag&gt;"), "<tag>");
    assert_eq!(decode_entities("&#65;&#x42;"), "AB");
    assert_eq!(decode_entities("x &le; y"), "x ≤ y");
    // A bare ampersand is left alone rather than eating following text.
    assert_eq!(decode_entities("Tom & Jerry"), "Tom & Jerry");
}

#[test]
fn repeated_links_are_numbered_once_not_repeated_inline() {
    let long = "https://example.org/a/very/long/path/that/costs/many/tokens";
    let html = format!("<p><a href=\"{long}\">first</a> and <a href=\"{long}\">second</a></p>");
    let mut table = LinkTable::default();
    let markdown = html_to_markdown(&html, &mut table);
    assert!(markdown.contains("first][1]"));
    // Same URL reuses reference 1 rather than repeating the whole URL.
    assert!(markdown.contains("second][1]"));
    assert!(!markdown.contains(long));
    assert!(table.render().contains(&format!("[1]: {long}")));
}

#[test]
fn distinct_links_get_distinct_references() {
    let mut table = LinkTable::default();
    let markdown = html_to_markdown(
        "<a href=\"https://a.test/x\">a</a><a href=\"https://b.test/y\">b</a>",
        &mut table,
    );
    assert!(markdown.contains("a][1]"));
    assert!(markdown.contains("b][2]"));
}

#[test]
fn tracking_parameters_are_stripped_from_urls() {
    assert_eq!(
        clean_url("https://x.test/p?utm_source=news&id=7&fbclid=abc"),
        "https://x.test/p?id=7"
    );
    // A URL with only tracking loses its query entirely.
    assert_eq!(
        clean_url("https://x.test/p?utm_medium=email"),
        "https://x.test/p"
    );
    // Meaningful queries and fragments survive.
    assert_eq!(
        clean_url("https://x.test/p?q=1#frag"),
        "https://x.test/p?q=1#frag"
    );
    assert_eq!(clean_url("https://x.test/plain"), "https://x.test/plain");
}

#[test]
fn conversion_records_its_source_and_format() {
    let markdown = to_markdown(
        b"<p>Hello</p>",
        Some("text/html"),
        "https://x.test/a?utm_term=z",
    )
    .expect("html converts");
    assert!(markdown.contains("converted from HTML"));
    // The recorded source is compressed too.
    assert!(markdown.contains("source: https://x.test/a "));
    assert!(markdown.contains("Hello"));
}

#[test]
fn binary_content_explains_what_to_do_instead() {
    let error = to_markdown(&[0x00, 0x01, 0xff, 0xfe], Some("application/zip"), "u")
        .expect_err("binary cannot convert");
    let message = error.to_string();
    assert!(message.contains("binary"));
    // The message reaches a model that must choose another source, so it has
    // to say so rather than just failing.
    assert!(message.contains("different source") || message.contains("HTML or PDF"));
}

#[test]
fn empty_documents_are_reported_rather_than_returned_blank() {
    let error = to_markdown(b"<html><head></head><body></body></html>", None, "u")
        .expect_err("an empty page is not usable");
    assert!(error.to_string().contains("no extractable text"));
}

#[test]
fn a_real_project_euler_statement_converts_without_losing_mathematics() {
    // Project Euler delimits maths with `$…$` and uses `<br>` for the line
    // breaks that separate worked examples. Both must survive: the examples
    // are the run's test oracle.
    let html = "<p>Define $f(0)=1$ and $f(n)$ to be the number of ways to write $n$ as a sum of \
                powers of $2$ where no power occurs more than twice.</p>\n\n<p>\nFor example, \
                $f(10)=5$ since there are five different ways to express $10$:<br>$10 = 8+2 = \
                8+1+1 = 4+4+2$</p><p>We shall call the string $4,3,1$ the <dfn>Shortened Binary \
                Expansion</dfn> of $241$.</p>";
    let markdown = render(html);

    assert!(markdown.contains("$f(0)=1$"));
    assert!(markdown.contains("$f(10)=5$"));
    assert!(markdown.contains("$10 = 8+2 = 8+1+1 = 4+4+2$"));
    // The <br> before the worked example must become a real line break.
    assert!(markdown.contains(":\n$10 = 8+2"));
    // Inline semantic tags are unwrapped, not dropped with their text.
    assert!(markdown.contains("Shortened Binary Expansion"));
    assert!(!markdown.contains("<dfn>"));
    assert!(!markdown.contains("<p>"));
}
