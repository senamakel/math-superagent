use super::{Candidate, MAX_ROWS, already_fetched, record, render, worth_offering};
use crate::orchestrator::documents::WorkspaceDocuments;
use crate::orchestrator::readable::LinkRecord;

use std::collections::BTreeMap;

fn workspace(name: &str) -> std::io::Result<std::path::PathBuf> {
    let path = std::env::temp_dir().join(format!("math-agent-frontier-{name}"));
    let _ = std::fs::remove_dir_all(&path);
    std::fs::create_dir_all(&path)?;
    path.canonicalize()
}

fn link(url: &str, label: &str, context: &str) -> LinkRecord {
    LinkRecord {
        url: url.to_string(),
        label: label.to_string(),
        context: context.to_string(),
    }
}

/// A source three of the library's papers cite is the standard reference for
/// the subject, and nothing else in the runtime is in a position to see that.
#[test]
fn in_degree_outranks_goal_overlap() {
    let mut ledger = BTreeMap::new();
    ledger.insert(
        "https://example.org/agreed".to_string(),
        Candidate {
            citers: 3,
            label: "Siegel, Coping with cycles".to_string(),
            context: "for the general theory we follow".to_string(),
            path: String::new(),
        },
    );
    ledger.insert(
        "https://example.org/wordy".to_string(),
        Candidate {
            citers: 1,
            label: "zugzwang stoppers partizan".to_string(),
            context: "zugzwang stoppers partizan loopy".to_string(),
            path: String::new(),
        },
    );
    let rendered = render(&ledger, "zugzwang stoppers partizan loopy games");
    let agreed = rendered.find("agreed").unwrap_or(usize::MAX);
    let wordy = rendered.find("wordy").unwrap_or(0);
    assert!(
        agreed < wordy,
        "three citers must outrank a single citer that merely shares vocabulary"
    );
}

/// A source already in the library is struck through and names its file, so a
/// reader of the table is pointed at what the run has rather than at a fetch.
#[test]
fn a_fetched_source_is_struck_through_and_named() {
    let mut ledger = BTreeMap::new();
    ledger.insert(
        "https://example.org/read".to_string(),
        Candidate {
            citers: 2,
            label: "already read".to_string(),
            context: String::new(),
            path: "research/L1.0/read.md".to_string(),
        },
    );
    let rendered = render(&ledger, "");
    assert!(rendered.contains("~~https://example.org/read~~"));
    assert!(rendered.contains("research/L1.0/read.md"));
}

/// The table is bounded. A long run's frontier reaches thousands of URLs and
/// rendering the tail would cost every reader of the file the whole page.
#[test]
fn the_table_is_bounded_and_says_what_it_left_out() {
    let ledger: BTreeMap<String, Candidate> = (0..MAX_ROWS + 15)
        .map(|index| {
            (
                format!("https://example.org/{index:03}"),
                Candidate {
                    citers: 1,
                    ..Candidate::default()
                },
            )
        })
        .collect();
    let rendered = render(&ledger, "");
    assert_eq!(rendered.matches("| 1 |").count(), MAX_ROWS);
    assert!(rendered.contains("15 further candidates not shown"));
}

/// A publisher links its own login and its social accounts from every article.
/// None of it is a lead and all of it outnumbers the references.
#[test]
fn publisher_furniture_is_not_a_lead() {
    assert!(worth_offering("https://arxiv.org/abs/1505.01907"));
    assert!(worth_offering("https://oeis.org/A000788"));
    assert!(!worth_offering("https://twitter.com/some_journal"));
    assert!(!worth_offering("https://www.facebook.com/journal"));
    assert!(!worth_offering(
        "https://publisher.example/login?next=/paper"
    ));
    assert!(!worth_offering("https://publisher.example/terms-of-use"));
    assert!(!worth_offering("mailto:editor@example.org"));
}

/// The download path's duplicate check: the same paper reached by two
/// spellings is one document, and the answer names where it already is.
#[tokio::test]
async fn a_fetched_url_is_recognised_through_its_tracking_parameters() -> std::io::Result<()> {
    let path = workspace("dedup")?;
    let Ok(documents) = WorkspaceDocuments::new(path) else {
        return Ok(());
    };
    assert!(
        already_fetched(&documents, "https://arxiv.org/abs/1505.01907")
            .await
            .is_none(),
        "an empty ledger has fetched nothing"
    );

    record(
        &documents,
        "https://arxiv.org/abs/1505.01907",
        "research/L1.0/pass_waiting.md",
        &[link(
            "https://arxiv.org/abs/1204.3222",
            "Morrison, Friedman, Landsberg",
            "a one-time pass changes the structure of the game",
        )],
        "combinatorial game theory with a pass move",
    )
    .await;

    assert_eq!(
        already_fetched(
            &documents,
            "https://arxiv.org/abs/1505.01907?utm_source=digest"
        )
        .await
        .as_deref(),
        Some("research/L1.0/pass_waiting.md"),
        "the canonical form is what the ledger is keyed on"
    );
    // What it cited is a lead, and has not been fetched.
    assert!(
        already_fetched(&documents, "https://arxiv.org/abs/1204.3222")
            .await
            .is_none()
    );
    Ok(())
}

/// Citations accumulate across downloads, which is the whole point: agreement
/// between independent sources is only visible once more than one has landed.
#[tokio::test]
async fn citations_accumulate_across_downloads() -> std::io::Result<()> {
    let path = workspace("accumulate")?;
    let Ok(documents) = WorkspaceDocuments::new(path) else {
        return Ok(());
    };
    let shared = link("https://example.org/standard", "the standard treatment", "");
    for (index, url) in ["https://example.org/one", "https://example.org/two"]
        .into_iter()
        .enumerate()
    {
        record(
            &documents,
            url,
            &format!("research/L1.0/source{index}.md"),
            &[shared.clone()],
            "",
        )
        .await;
    }
    let rendered = documents
        .read_runtime(super::FRONTIER_PATH)
        .await
        .unwrap_or_default();
    assert!(
        rendered.contains("| 2 | https://example.org/standard |"),
        "two independent sources cite it: {rendered}"
    );
    Ok(())
}
