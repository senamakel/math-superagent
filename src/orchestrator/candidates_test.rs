#![allow(clippy::expect_used)]

use super::super::vcs::{ATTEMPTS_DIR, Git, TRUNK};
use super::{SLOTS, checkout_of, role_for, slots};

#[test]
fn every_slot_has_its_own_role_and_its_own_directory() {
    let ids = slots();
    assert_eq!(ids.len(), SLOTS);

    let roles: std::collections::BTreeSet<String> = ids.iter().map(|id| role_for(id)).collect();
    assert_eq!(roles.len(), SLOTS, "two slots share a role name: {roles:?}");

    let root = std::path::Path::new("/workspace");
    let dirs: std::collections::BTreeSet<std::path::PathBuf> =
        ids.iter().map(|id| checkout_of(root, id)).collect();
    assert_eq!(dirs.len(), SLOTS, "two slots share a checkout: {dirs:?}");
    for dir in &dirs {
        assert!(
            dir.starts_with(root.join(ATTEMPTS_DIR)),
            "a checkout escaped the attempts directory: {dir:?}"
        );
    }
}

#[test]
fn slot_ids_sort_as_they_read() {
    // Zero-padded, so `list_attempts` and the ledger agree on the order a
    // reader sees. `10` sorting before `2` is the kind of thing that makes a
    // list look wrong for no reason anybody can name.
    let ids = slots();
    let mut sorted = ids.clone();
    sorted.sort();
    assert_eq!(ids, sorted);
    assert_eq!(ids.first().map(String::as_str), Some("01"));
}

/// Two candidates writing the same path must not collide.
///
/// This is the property the whole design rests on: each slot is a linked
/// worktree, so `code/solution.py` resolves to a different file for each of
/// them, and committing one leaves the others and the trunk untouched.
#[tokio::test]
async fn two_candidates_write_the_same_path_without_colliding() {
    let root = std::env::temp_dir().join("candidates-isolation");
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(root.join("code")).expect("created");
    std::fs::write(root.join("code").join("solution.py"), "print('trunk')\n").expect("written");

    let git = Git::history(&root);
    git.initialise().await.expect("history");
    git.stage_all().await.expect("staged");
    git.commit("seed").await.expect("committed");

    let ids = slots();
    let first = ids.first().expect("a first slot");
    let second = ids.get(1).expect("a second slot");
    for (id, body) in [(first, "print('one')\n"), (second, "print('two')\n")] {
        let checkout = checkout_of(&root, id);
        git.worktree_add(&checkout, &format!("attempt/{id}"), TRUNK)
            .await
            .expect("branched");
        std::fs::write(checkout.join("code").join("solution.py"), body).expect("written");
        let candidate = Git::worktree(&root, &checkout);
        candidate.stage_all().await.expect("staged");
        candidate
            .commit(&format!("candidate {id}"))
            .await
            .expect("committed");
    }

    // Each kept its own bytes.
    assert_eq!(
        std::fs::read_to_string(checkout_of(&root, first).join("code/solution.py")).expect("read"),
        "print('one')\n"
    );
    assert_eq!(
        std::fs::read_to_string(checkout_of(&root, second).join("code/solution.py")).expect("read"),
        "print('two')\n"
    );
    // And the trunk kept its own.
    assert_eq!(
        std::fs::read_to_string(root.join("code/solution.py")).expect("read"),
        "print('trunk')\n",
        "a candidate's write reached the trunk"
    );

    // The two branches disagree, which is the point: the archivist has a real
    // choice to make and both options are on disk.
    let one = git
        .diff(TRUNK, &format!("attempt/{first}"), None)
        .await
        .expect("diff");
    assert!(one.contains("print('one')"), "{one}");
    assert!(!one.contains("print('two')"), "candidate two leaked in: {one}");
}

/// A candidate's own ledgers and notes fork with its files.
#[tokio::test]
async fn a_candidates_notes_stay_in_its_own_checkout() {
    let root = std::env::temp_dir().join("candidates-ledgers");
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(root.join("research")).expect("created");
    std::fs::write(root.join("GOAL.md"), "the goal\n").expect("written");

    let git = Git::history(&root);
    git.initialise().await.expect("history");
    git.stage_all().await.expect("staged");
    git.commit("seed").await.expect("committed");

    let id = slots().first().cloned().expect("a slot");
    let checkout = checkout_of(&root, &id);
    git.worktree_add(&checkout, &format!("attempt/{id}"), TRUNK)
        .await
        .expect("branched");

    std::fs::create_dir_all(checkout.join("research")).expect("created");
    std::fs::write(
        checkout.join("research").join("note.md"),
        "what I found\n",
    )
    .expect("written");

    assert!(
        !root.join("research").join("note.md").exists(),
        "a candidate's note appeared in the trunk's research tree"
    );
}


/// Reusing a slot must not destroy a candidate nobody recorded.
///
/// The first version of `prepare` deleted the branch outright, justified by the
/// round's ledger entry making the work reviewable. Nothing enforces that entry:
/// a live run reached three finished branches with the attempts ledger still
/// unrendered, because the planner timed out before recording anything. A second
/// round would have thrown all three away.
#[tokio::test]
async fn reusing_a_slot_keeps_a_branch_that_carries_work() {
    let root = std::env::temp_dir().join("candidates-slot-reuse");
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(root.join("code")).expect("created");
    std::fs::write(root.join("code").join("solution.py"), "print('trunk')\n").expect("written");

    let git = Git::history(&root);
    git.initialise().await.expect("history");
    git.stage_all().await.expect("staged");
    git.commit("seed").await.expect("committed");

    let id = slots().first().cloned().expect("a slot");
    let branch = format!("attempt/{id}");
    let checkout = checkout_of(&root, &id);

    // Round one: the candidate commits something and is never recorded.
    git.worktree_add(&checkout, &branch, TRUNK)
        .await
        .expect("branched");
    std::fs::write(checkout.join("code").join("solution.py"), "print('round one')\n")
        .expect("written");
    let candidate = Git::worktree(&root, &checkout);
    candidate.stage_all().await.expect("staged");
    candidate.commit("round one").await.expect("committed");
    let kept = git.head_of(&branch).await.expect("a head");

    // Round two reuses the slot.
    git.worktree_remove(&checkout).await.expect("removed");
    assert!(git.commits_ahead(TRUNK, &branch).await > 0);
    git.rename_branch(&branch, &format!("{branch}-{kept}"))
        .await
        .expect("moved aside");
    git.worktree_add(&checkout, &branch, TRUNK)
        .await
        .expect("rebranched");

    // Round one's work is still reachable, under its own head.
    let archived = format!("{branch}-{kept}");
    assert_eq!(git.head_of(&archived).await.as_deref(), Some(kept.as_str()));
    assert_eq!(
        git.subject_of(&archived).await.as_deref(),
        Some("round one"),
        "a slot reused before its candidate was recorded lost the work"
    );
    // And the fresh slot starts from the trunk, not from round one.
    assert_eq!(
        std::fs::read_to_string(checkout.join("code/solution.py")).expect("read"),
        "print('trunk')\n"
    );
}

/// A branch with nothing on it is deleted rather than archived, so reusing a
/// slot repeatedly does not accumulate empty refs.
#[tokio::test]
async fn reusing_an_untouched_slot_leaves_no_ref_behind() {
    let root = std::env::temp_dir().join("candidates-slot-empty");
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(&root).expect("created");
    std::fs::write(root.join("GOAL.md"), "goal\n").expect("written");

    let git = Git::history(&root);
    git.initialise().await.expect("history");
    git.stage_all().await.expect("staged");
    git.commit("seed").await.expect("committed");

    let id = slots().first().cloned().expect("a slot");
    let branch = format!("attempt/{id}");
    git.worktree_add(&checkout_of(&root, &id), &branch, TRUNK)
        .await
        .expect("branched");

    assert_eq!(git.commits_ahead(TRUNK, &branch).await, 0);
}
