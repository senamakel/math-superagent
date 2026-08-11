use super::{identifier, post, refresh};
use crate::orchestrator::documents::WorkspaceDocuments;

fn workspace(name: &str) -> std::io::Result<std::path::PathBuf> {
    let root = std::env::temp_dir().join(format!("math-agent-requests-{name}"));
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(root.join("research/L1.0"))?;
    root.canonicalize()
}

fn claim(root: &std::path::Path, name: &str, block: &str) -> std::io::Result<()> {
    std::fs::write(
        root.join(format!("research/L1.0/{name}.md")),
        format!("# {name}\n\n```claim\n{block}\n```\n"),
    )
}

/// The same gap stated twice is one row. Two roles reaching the same wall is a
/// signal worth seeing once, not a queue with the question in it twice.
#[test]
fn the_same_need_names_the_same_request() {
    let first = identifier("Whether the pass loop keeps the game a stopper");
    let second = identifier("whether the PASS loop keeps the game a stopper");
    assert_eq!(first, second);
    assert_ne!(first, identifier("Whether the recurrence has a closed form"));
    // The id reads as what it asks for, so a claim answering it is legible.
    assert!(first.starts_with("whether-pass-loop"), "{first}");
}

/// The reluctance, made mechanical: the common case is that the run already
/// knows this and has forgotten, and that should cost a lookup rather than a
/// download.
#[tokio::test]
async fn a_gap_the_library_already_answers_is_not_queued() -> std::io::Result<()> {
    let root = workspace("answered")?;
    let Ok(documents) = WorkspaceDocuments::new(root.clone()) else {
        return Ok(());
    };
    claim(
        &root,
        "stoppers",
        "id: skip-is-a-stopper\n\
         statement: A pass self-loop leaves the game a stopper, so the fixpoint terminates.\n\
         status: proved\n\
         holds-here: yes",
    )?;

    let reply = post(
        &documents,
        "whether the pass self-loop leaves the game a stopper",
        "it decides whether the fixpoint terminates",
        "a non-terminating fixpoint",
    )
    .await;
    assert!(reply.starts_with("not queued"), "{reply}");
    assert!(reply.contains("skip-is-a-stopper"));

    let rendered = documents
        .read_runtime(super::REQUESTS_PATH)
        .await
        .unwrap_or_default();
    assert!(
        !rendered.contains("pass self-loop"),
        "an answered gap leaves no open row: {rendered}"
    );
    Ok(())
}

/// A genuine gap is queued with the field that makes it a question rather than
/// a topic.
#[tokio::test]
async fn a_genuine_gap_is_queued_with_what_would_falsify_it() -> std::io::Result<()> {
    let root = workspace("queued")?;
    let Ok(documents) = WorkspaceDocuments::new(root) else {
        return Ok(());
    };
    let reply = post(
        &documents,
        "the exact statement of Trollope-Delange for weighted digit sums",
        "it turns the summatory count into an O(log n) evaluation",
        "a fluctuation term that is not 1-periodic",
    )
    .await;
    assert!(reply.starts_with("recorded as"), "{reply}");

    let rendered = documents
        .read_runtime(super::REQUESTS_PATH)
        .await
        .unwrap_or_default();
    assert!(rendered.contains("Trollope-Delange"));
    assert!(rendered.contains("not 1-periodic"));
    assert!(!rendered.contains("Nothing outstanding"));
    Ok(())
}

/// A request closes against a claim, so whether the gap was filled is read off
/// the library rather than asserted by whoever went looking.
#[tokio::test]
async fn a_claim_answering_a_request_closes_it() -> std::io::Result<()> {
    let root = workspace("closing")?;
    let Ok(documents) = WorkspaceDocuments::new(root.clone()) else {
        return Ok(());
    };
    let need = "a polylog evaluation of the summatory popcount";
    let reply = post(&documents, need, "it lets the DP run at n=10^5", "").await;
    assert!(reply.starts_with("recorded as"), "{reply}");
    let id = identifier(need);

    let rendered = documents
        .read_runtime(super::REQUESTS_PATH)
        .await
        .unwrap_or_default();
    assert!(!rendered.contains("## Answered"), "{rendered}");

    claim(
        &root,
        "a000788",
        &format!(
            "id: summatory-popcount\n\
             statement: A000788 gives the summatory popcount by an O(log n) recurrence.\n\
             status: proved\n\
             holds-here: yes\n\
             answers: {id}"
        ),
    )?;
    refresh(&documents).await;

    let rendered = documents
        .read_runtime(super::REQUESTS_PATH)
        .await
        .unwrap_or_default();
    assert!(rendered.contains("## Answered"), "{rendered}");
    assert!(rendered.contains(&id));
    assert!(rendered.contains("Nothing outstanding"));
    Ok(())
}
