use std::sync::Arc;

use super::{Kind, PATH, QUEUE, collect, post, render};

/// A post round-trips through the queue.
#[test]
fn a_post_round_trips() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    post(
        workspace.path(),
        "adversarial",
        Kind::DeadEnd,
        "the generating-function route is dead: it needs f to be D-finite and it is not",
        &["claim-4".to_string()],
    )
    .expect("the post must be written");
    let posts = collect(workspace.path());
    assert_eq!(posts.len(), 1, "one post was written");
    assert_eq!(posts[0].from, "adversarial");
    assert_eq!(posts[0].kind, Kind::DeadEnd);
    assert_eq!(posts[0].refers, vec!["claim-4".to_string()]);
    assert!(posts[0].body.contains("D-finite"));
}

/// An empty body is refused rather than filed as a blank row.
#[test]
fn an_empty_post_is_refused() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    assert!(
        post(workspace.path(), "chisel", Kind::Lesson, "   ", &[]).is_err(),
        "a blank body must not reach the board"
    );
}

/// An unrecognised kind becomes a hunch rather than being lost.
#[test]
fn an_unknown_kind_claims_the_least() {
    assert_eq!(Kind::parse("proof"), Kind::Hunch);
    assert_eq!(Kind::parse("DEAD-END"), Kind::DeadEnd);
    assert_eq!(Kind::parse("lesson"), Kind::Lesson);
}

/// A line that will not parse costs only itself.
#[test]
fn an_unreadable_line_is_skipped() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    post(workspace.path(), "chisel", Kind::Lesson, "a real post", &[])
        .expect("the post must be written");
    let path = workspace.path().join(QUEUE);
    let mut raw = std::fs::read_to_string(&path).expect("the queue must be readable");
    raw.push_str("{ this is not json\n");
    std::fs::write(&path, raw).expect("the queue must be writable");
    assert_eq!(
        collect(workspace.path()).len(),
        1,
        "one torn line must not cost the board every other post"
    );
}

/// Concurrent posters interleave whole lines and never halves of one.
///
/// This is the property that lets several schools share the board with no lock,
/// so it is asserted rather than assumed. Each post carries its own index, and
/// every index must come back exactly once.
#[tokio::test]
async fn concurrent_posts_do_not_interleave() {
    let workspace = Arc::new(tempfile::tempdir().expect("a temporary workspace"));
    let mut tasks = Vec::new();
    for index in 0..32u32 {
        let workspace = Arc::clone(&workspace);
        tasks.push(tokio::task::spawn_blocking(move || {
            post(
                workspace.path(),
                "school",
                Kind::Hunch,
                &format!("post number {index}"),
                &[],
            )
            .expect("every concurrent post must be written");
        }));
    }
    for task in tasks {
        task.await.expect("a posting task must not panic");
    }
    let posts = collect(workspace.path());
    assert_eq!(posts.len(), 32, "every concurrent post must survive");
    let mut seen: Vec<String> = posts.into_iter().map(|post| post.body).collect();
    seen.sort();
    seen.dedup();
    assert_eq!(seen.len(), 32, "no post may be lost or duplicated");
}

/// The rendered board says plainly that a post is not a claim.
///
/// The whole boundary this module defends is that a hunch cannot become a
/// finding by being read, and the rendered header is where a reading role is
/// told so.
#[test]
fn the_render_says_a_post_is_not_a_claim() {
    let workspace = tempfile::tempdir().expect("a temporary workspace");
    post(
        workspace.path(),
        "rising-sea",
        Kind::Hunch,
        "the sheaf-theoretic setting may cover this",
        &[],
    )
    .expect("the post must be written");
    let rendered = render(&collect(workspace.path()));
    assert!(rendered.contains("asserted, not established"));
    assert!(rendered.contains("rising-sea"));
    assert!(rendered.contains("hunch"));
    assert!(
        PATH.starts_with("teams/"),
        "the board belongs in the shared teams tree"
    );
}

/// An empty board renders rather than failing.
#[test]
fn an_empty_board_renders() {
    let rendered = render(&[]);
    assert!(rendered.contains("Nothing posted yet"));
}
