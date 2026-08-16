/// Describes a freshly downloaded source from what it already carries.
///
/// The first heading is the document's own title far more often than not, and
/// the URL is its provenance. Together they answer "what is this and where did
/// it come from", which is the whole job of an index row until somebody has
/// actually read the thing.
fn provisional_description(content: &str, url: &str) -> String {
    let title = content
        .lines()
        .map(str::trim)
        .find(|line| line.starts_with('#'))
        .map(|line| line.trim_start_matches('#').trim())
        .filter(|title| !title.is_empty())
        .unwrap_or("downloaded source");
    let title: String = title.chars().take(120).collect();
    format!("{title} — from {url}; not yet read, excerpt pending a scholar summary")
}

/// Returns whether a stored document should be rendered to Markdown on read.
///
/// Keyed on the extension, plus the PDF magic bytes for a file saved without
/// one. Deliberately narrow: content sniffing every read would eventually
/// mangle a Markdown note that happens to quote some HTML.
fn needs_conversion(relative: &str, bytes: &[u8]) -> bool {
    if bytes.starts_with(b"%PDF-") {
        return true;
    }
    let lowered = relative.to_ascii_lowercase();
    [".html", ".htm", ".xhtml", ".pdf"]
        .iter()
        .any(|extension| lowered.ends_with(extension))
}

/// Recursively lists `directory`, appending one formatted line per entry.
fn walk<'a>(
    root: &'a std::path::Path,
    directory: &'a std::path::Path,
    depth: usize,
    lines: &'a mut Vec<String>,
    truncated: &'a mut bool,
) -> std::pin::Pin<Box<dyn Future<Output = Result<()>> + Send + 'a>> {
    Box::pin(async move {
        if depth == 0 || *truncated {
            return Ok(());
        }
        // An unreadable directory is skipped rather than failing the whole
        // listing: one bad permission should not hide the rest of the tree.
        let Ok(mut entries) = tokio::fs::read_dir(directory).await else {
            return Ok(());
        };
        while let Ok(Some(entry)) = entries.next_entry().await {
            if lines.len() >= MAX_LISTING_ENTRIES {
                *truncated = true;
                return Ok(());
            }
            let name = entry.file_name().to_string_lossy().into_owned();
            if HIDDEN_ENTRIES.contains(&name.as_str()) {
                continue;
            }
            let path = entry.path();
            let Ok(relative) = path.strip_prefix(root) else {
                continue;
            };
            let shown = relative.to_string_lossy();
            let Ok(metadata) = entry.metadata().await else {
                continue;
            };
            if metadata.is_dir() {
                lines.push(format!("  {shown}/"));
                walk(root, &path, depth - 1, lines, truncated).await?;
            } else {
                lines.push(format!("  {shown} ({} bytes)", metadata.len()));
            }
        }
        Ok(())
    })
}

/// Files a downloaded document under the research folder.
///
/// A path already inside the folder is left alone; anything else is moved into
/// it, and a leading `/workspace` or `./` is trimmed first so the common
/// spellings do not produce `research/workspace/...`.
pub(super) fn research_path(_workspace: &std::path::Path, requested: &str) -> String {
    let trimmed = requested
        .trim()
        .trim_start_matches("/workspace/")
        .trim_start_matches("./")
        .trim_start_matches('/');
    let inside = trimmed
        .strip_prefix(&format!("{RESEARCH_DIR}/"))
        .unwrap_or(if trimmed == RESEARCH_DIR { "" } else { trimmed });
    if inside.is_empty() {
        return format!("{DIGEST_DIR}/document.md");
    }
    let name = inside.rsplit('/').next().unwrap_or(inside);
    // A caller naming the full text is naming the wrong half of the pair. The
    // digest is what a download produces at level 1; strip the marker rather
    // than filing `x.full.md` there and giving its companion the name
    // `x.full.full.md`, which is what a live run produced.
    let name = match name.strip_suffix(FULL_TEXT_SUFFIX) {
        Some(stem) => format!("{stem}.md"),
        None => name.to_string(),
    };
    format!("{DIGEST_DIR}/{name}")
}

/// Renames a stored document to `.md`, because that is what it now contains.
///
/// Everything filed under `research/` has been through `to_markdown`, so a
/// stored file called `paper.pdf` is a lie: it holds Markdown. The wrong
/// extension misleads every later reader — an agent deciding whether it can
/// read a file, a human opening the workspace, and any tool that dispatches on
/// suffix. The original bytes keep their true extension under `raw/`, which is
/// where a genuine PDF still lives.
pub(super) fn markdown_path(relative: &str) -> String {
    // No extension at all: give it the one it has earned.
    let Some((stem, extension)) = relative.rsplit_once('.') else {
        return format!("{relative}.md");
    };
    // A dot in a directory name is not an extension, and neither is a version
    // number in `zeta.2.1` — only rewrite when the tail looks like a suffix.
    if stem.is_empty()
        || extension.contains('/')
        || extension.is_empty()
        || !extension.chars().all(|c| c.is_ascii_alphanumeric())
    {
        return format!("{relative}.md");
    }
    if extension.eq_ignore_ascii_case("md") {
        return relative.to_string();
    }
    format!("{stem}.md")
}

/// Returns where a converted document's original bytes are archived.
///
/// Mirrors the research layout under [`RAW_DIR`] so the two stay in
/// correspondence: `research/papers/pell.md` archives to `raw/papers/pell.md`.
pub(super) fn raw_path(research_relative: &str) -> String {
    let tail = research_relative
        .strip_prefix(&format!("{RESEARCH_DIR}/"))
        .unwrap_or(research_relative);
    format!("{RAW_DIR}/{tail}")
}

/// Returns where a document's complete converted text is filed.
///
/// One level below its summary. The original is what the whole tree is
/// anchored to and the one thing in it nobody may rewrite, so it lives in its
/// own folder rather than beside a note an agent is expected to replace.
pub(super) fn full_text_path(_workspace: &std::path::Path, summary_relative: &str) -> String {
    let stem = summary_relative
        .strip_suffix(".md")
        .unwrap_or(summary_relative);
    let name = stem.rsplit('/').next().unwrap_or(stem);
    // A caller may address the download at the level holding originals, in
    // which case the name already carries the marker. Appending a second
    // produced `x.full.full.md`, and seven of them landed in one live
    // workspace before this stripped the marker it already had.
    let name = name.strip_suffix(".full").unwrap_or(name);
    format!("{SOURCE_DIR}/{name}{FULL_TEXT_SUFFIX}")
}

/// Renders the heading for a listing root.
fn display_root(relative: &str) -> String {
    if relative == "." || relative.is_empty() {
        "/workspace".to_string()
    } else {
        format!("/workspace/{}", relative.trim_start_matches('/'))
    }
}

#[derive(Clone, Copy, Debug)]
enum DocumentToolKind {
    Download,
    Read,
    Write,
    Edit,
    Index,
    Search,
    List,
}

impl DocumentToolKind {
    const ALL: [Self; 7] = [
        Self::Download,
        Self::Read,
        Self::Write,
        Self::Edit,
        Self::Index,
        Self::Search,
        Self::List,
    ];
}

/// Entries never worth showing an agent: its own bookkeeping, installed
/// packages, and the console and event logs.
///
/// `start.log` is the console stream, and it is the same failure as
/// `trace.jsonl` wearing a different name. The launchers redirect a detached
/// run's output into it, so it holds every model call, tool call and tool
/// result the run has already produced, and it grows for as long as the run
/// does. A live `context_curator` read 37,609 bytes of one straight into a
/// model call. Hiding the trace and leaving this beside it hid the file the
/// policy names and not the one an agent actually reaches for.
///
/// `derived/` is the newest and the only one that is *not* runtime bookkeeping.
/// It holds the nine rendered ledgers, which are the run's own reasoning and are
/// committed and read by people. They are hidden from the file tools anyway,
/// because a rendered ledger is the expensive way in: `read_ledger` bounds what
/// it returns and filters by id, status or query, and `read_document` on the
/// same file returns all of it. Leaving both doors open left the cheap one
/// optional, and `CLAIMS.md` was measured at 7,488 tokens against a question
/// about one row. The refusal below names the tool to use instead.
const HIDDEN_ENTRIES: [&str; 9] = [
    ".workspace-history",
    DERIVED_DIR,
    ".python-packages",
    "__pycache__",
    ".document-index.json",
    ".frontier.json",
    "trace.jsonl",
    "start.log",
    RAW_DIR,
];

/// Largest number of entries one listing returns.
const MAX_LISTING_ENTRIES: usize = 400;

/// Rejects a path that names one of the runtime's own hidden entries.
///
/// Hiding these from `list_workspace` was never enough, because an agent can
/// name a path the listing did not offer it. A reflection run did exactly
/// that: it read `/workspace/trace.jsonl` — 1,124,798 bytes of the run's own
/// event log — straight into its context, producing a single 339,652-token
/// model call, pushing the run past the 300,000-token compression trigger and
/// collapsing the prompt-cache hit rate from 71% to 26% in one turn.
///
/// The content is the worst possible thing to feed back in. The trace is a
/// verbatim record of every prompt and tool result the run has already seen,
/// so re-reading it tells the agent nothing new while costing more than any
/// real document could. Worse, the reader is the judge: reflection consuming a
/// replay of the attempt it is meant to assess is not evidence, it is an echo.
///
/// Enforced here rather than by asking the model to avoid the file, because a
/// prompt instruction is not a control — and the workspace policy previously
/// told agents to read this very file.
/// Names the ledger a path *used* to be, when it names one.
///
/// The nine rendered ledgers moved from `research/` to `derived/`, and a role
/// that learnt the old path — from a note on disk, from a summary it wrote last
/// week, from its own memory — asks for it and gets "No such file or
/// directory". That is true and useless: a live librarian hit exactly this on
/// `research/FRONTIER.md` minutes after the move. A path that was somewhere
/// must say where it went, or the run pays a turn to rediscover it.
pub(super) fn moved_ledger(relative: &str) -> Option<String> {
    let rest = relative
        .trim_start_matches("/workspace/")
        .trim_start_matches("./")
        .strip_prefix("research/")?;
    if !super::ledger::is_derived_file(rest) {
        return None;
    }
    let name = rest.strip_suffix(".md")?;
    Some(format!(
        "`research/{name}.md` moved to `{DERIVED_DIR}/{name}.md`, which is derived and not read \
         as a file. Read it with `read_ledger`, which bounds what it returns and can select by \
         `id`, `status` or `query`; `list_ledgers` names them all."
    ))
}

fn ensure_visible(relative: &str) -> Result<()> {
    let hidden = std::path::Path::new(relative)
        .components()
        .filter_map(|component| component.as_os_str().to_str())
        .find(|name| HIDDEN_ENTRIES.contains(name));
    let Some(hidden) = hidden else {
        return Ok(());
    };
    // A refusal that does not name the way forward costs the turn twice: once
    // to be refused and once to guess. `docs/ledgers.md` already requires this
    // of the *write* guard, and the read guard is held to the same standard.
    if hidden == DERIVED_DIR {
        return Err(tinyagents::TinyAgentsError::Validation(format!(
            "`{relative}` is a derived ledger, rendered by this runtime from the notes a run \
             writes. Read it with `read_ledger`, which returns it bounded and can select by \
             `id`, `status` or `query` — `list_ledgers` names them all. Reading the file whole \
             costs several thousand tokens to answer a question about one row."
        )));
    }
    Err(tinyagents::TinyAgentsError::Validation(format!(
        "`{hidden}` is runtime bookkeeping, not a workspace document; it is \
         already in your context or irrelevant to the problem"
    )))
}
