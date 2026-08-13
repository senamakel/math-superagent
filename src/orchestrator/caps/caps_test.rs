//! Tests that the bundle as a whole keeps its boundaries.
#![allow(clippy::expect_used)]

/// `Capabilities::shell` is optional and this crate leaves it unset, so a
/// `shell` node fails with a capability error rather than silently doing
/// nothing. This asserts the decision is still the decision: a later change
/// that supplies a shell runner has to come here and say why.
#[test]
fn no_shell_runner_is_supplied() {
    // Nothing in this crate constructs a `ShellRunner`. Asserted by grep rather
    // than by type, because the point is the absence.
    let sources = [
        include_str!("mod.rs"),
        include_str!("execution.rs"),
        include_str!("state.rs"),
        include_str!("tools.rs"),
    ];
    for source in sources {
        assert!(
            !source.contains("impl ShellRunner"),
            "a ShellRunner appeared; see execution.rs for why there is none"
        );
    }
}
