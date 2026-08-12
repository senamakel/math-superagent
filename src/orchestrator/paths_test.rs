//! Unit tests for the workspace path boundary.
#![allow(clippy::expect_used)]

use super::{checked_workspace_path, strip_workspace_prefix};

#[test]
fn workspace_paths_reject_absolute_and_parent_traversal() {
    let workspace = std::path::Path::new("/workspace");
    assert!(checked_workspace_path(workspace, "tools/check.sh").is_ok());
    assert!(checked_workspace_path(workspace, "/etc/passwd").is_err());
    assert!(checked_workspace_path(workspace, "../outside").is_err());
    assert!(checked_workspace_path(workspace, "").is_err());
    assert!(checked_workspace_path(workspace, "tools/../../outside").is_err());
}

#[test]
fn workspace_paths_accept_the_mount_point_spelling_agents_are_given() {
    // Every prompt names files as `/workspace/solution.md`; that must resolve
    // to the same file as the relative spelling, not fail as traversal.
    let workspace = std::path::Path::new("/workspace");
    assert_eq!(
        checked_workspace_path(workspace, "/workspace/solution.md").ok(),
        checked_workspace_path(workspace, "solution.md").ok()
    );
    assert_eq!(
        checked_workspace_path(workspace, "/workspace/tools/check.sh").ok(),
        checked_workspace_path(workspace, "tools/check.sh").ok()
    );
}

#[test]
fn workspace_prefix_stripping_does_not_open_up_sibling_directories() {
    let workspace = std::path::Path::new("/workspace");
    assert!(checked_workspace_path(workspace, "/workspace-other/secret").is_err());
    assert!(checked_workspace_path(workspace, "/workspaces/secret").is_err());
    assert!(checked_workspace_path(workspace, "/workspace/../etc/passwd").is_err());
    assert!(checked_workspace_path(workspace, "/workspace").is_err());
}

#[test]
fn the_relative_mount_point_spelling_is_stripped_too() {
    // A live run failed three consecutive `refresh_index` calls on `workspace`,
    // `workspace/toolkits`, and `workspace/research`, none of which the model
    // could tell apart from the folder genuinely being absent.
    assert_eq!(strip_workspace_prefix("workspace/research"), "research");
    assert_eq!(strip_workspace_prefix("workspace"), "");
    assert_eq!(strip_workspace_prefix("/workspace/code/lib"), "code/lib");
    assert_eq!(strip_workspace_prefix("  code/lib.py  "), "code/lib.py");
}

#[test]
fn a_sibling_of_the_mount_point_keeps_its_absolute_form() {
    // Only an exact component match is stripped, so the caller still refuses
    // these as absolute rather than reading them as relative.
    assert_eq!(
        strip_workspace_prefix("/workspace-other/secret"),
        "/workspace-other/secret"
    );
    assert_eq!(
        strip_workspace_prefix("workspaces/secret"),
        "workspaces/secret"
    );
}
