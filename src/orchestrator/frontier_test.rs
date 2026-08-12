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
            std::slice::from_ref(&shared),
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

#[test]
fn the_scholarly_tooling_toolbar_is_not_a_citation() {
    // The failure this closes, taken verbatim from a live Erdős–Gyárfás
    // frontier whose top seventeen rows were all of this kind, tied at six
    // citers, above every actual paper. They accumulate citers faster than any
    // reference can because they appear on *every* arXiv abstract page — and
    // the librarian is told to work that file before searching.
    for url in [
        "https://info.arxiv.org/about",
        "https://info.arxiv.org/help/mathjax.html",
        "https://arxiv.org/search/advanced",
        "https://core.ac.uk/services/recommender",
        "https://www.connectedpapers.com/about",
        "http://gotit.pub/faq",
        "https://alphaxiv.org/",
        "https://dagshub.com/",
        "https://huggingface.co/docs/hub/spaces",
        "https://replicate.com/docs/arxiv/about",
        "https://sciencecast.org/welcome",
        "https://txyz.ai",
        "https://influencemap.cmlab.dev/",
        "https://www.litmaps.co/",
        "http://arxiv.org/licenses/nonexclusive-distrib/1.0/",
    ] {
        assert!(!super::worth_offering(url), "{url} is site furniture");
    }
}

#[test]
fn a_paper_on_a_host_that_also_serves_furniture_is_still_offered() {
    // The filters must not ban a host outright where it serves both. CORE
    // hosts papers at `/download/` and its recommender pitch at `/services/`;
    // arXiv hosts papers at `/abs/` and its search form at `/search/advanced`.
    for url in [
        "https://arxiv.org/abs/2410.22842",
        "https://core.ac.uk/download/pdf/12345.pdf",
        "https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Gy%C3%A1rf%C3%A1s_conjecture",
        "https://bibliotekanauki.pl/articles/30148697.pdf",
        "https://www.combinatorics.org/ojs/index.php/eljc/article/view/v11i1r62",
        "https://ui.adsabs.harvard.edu/abs/2004math......1049M",
    ] {
        assert!(super::worth_offering(url), "{url} is a real lead");
    }
}

#[test]
fn a_host_with_no_dot_is_not_on_the_public_internet() {
    // A container name on the page's own network, reachable only from where
    // that page was rendered. A live library had 64 candidates on
    // `backend:8080` — the House of Graphs internal API, a fifth of the whole
    // frontier — and not one was fetchable from the run.
    assert!(!super::worth_offering("http://backend:8080/api/graph_invariants/51419/1"));
    assert!(!super::worth_offering("http://localhost:3000/graphs"));
    assert!(super::worth_offering("https://houseofgraphs.org/graphs/51419"));
}

#[test]
fn a_reference_work_indexing_itself_is_not_a_citation() {
    // Taken from a live Project Euler 241 frontier: 69 Wikipedia rows and 30
    // OEIS rows out of 151, seventeen of them explaining themselves only as
    // "cross-referenced from A159907". An OEIS page lists every related
    // sequence and a Wikipedia article links hundreds; both are indexes, and an
    // index is exhaustive by design rather than selective.
    assert!(super::indexes_itself(
        "https://oeis.org/A159907",
        "https://oeis.org/A000203"
    ));
    assert!(super::indexes_itself(
        "https://en.wikipedia.org/wiki/Perfect_number",
        "https://en.wikipedia.org/wiki/Semiperfect_number"
    ));
    // Across language editions it is still the same work.
    assert!(super::indexes_itself(
        "https://en.wikipedia.org/wiki/Perfect_number",
        "https://de.wikipedia.org/wiki/Vollkommene_Zahl"
    ));
}

#[test]
fn a_reference_work_pointing_outward_is_kept() {
    // Outbound is the valuable half. A Wikipedia article's reference list is
    // papers and DOIs, which is exactly what the run cannot reach on its own.
    assert!(!super::indexes_itself(
        "https://en.wikipedia.org/wiki/Perfect_number",
        "https://arxiv.org/abs/2010.15802"
    ));
    assert!(!super::indexes_itself(
        "https://oeis.org/A159907",
        "https://doi.org/10.1007/BF01305234"
    ));
}

#[test]
fn a_paper_citing_a_paper_on_the_same_host_survives() {
    // The rule is not "same host is never a citation". An arXiv paper citing
    // another arXiv paper is the ordinary case and the frontier's whole point.
    assert!(!super::indexes_itself(
        "https://arxiv.org/abs/1508.07912",
        "https://arxiv.org/abs/2010.15802"
    ));
    assert!(!super::indexes_itself(
        "https://www.renyi.hu/~p_erdos/1988-06.pdf",
        "https://www.renyi.hu/~p_erdos/1975-05.pdf"
    ));
}
