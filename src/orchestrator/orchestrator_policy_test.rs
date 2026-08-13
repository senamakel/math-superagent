#[test]
fn every_role_with_memory_can_query_the_graph_and_not_only_the_chunks() -> agent::Result<()> {
    // A knowledge graph used only through `recall_memory` is a search box with
    // extra infrastructure: chunk search returns the passages nearest a phrase,
    // which is what the vector store already did. `relate_memory` returns the
    // edges, so a connection the run established across two sources and never
    // stated in one place is retrievable. A role that has one and not the other
    // cannot ask the question the graph exists to answer.
    let registry = default_registry(true)?;
    for role in [
        "research",
        "librarian",
        "scholar",
        "inventor",
        "reducer",
        "reflection",
        "pattern_finder",
    ] {
        let Some(agent) = registry.get(role) else {
            continue;
        };
        let has = |tool: &str| agent.tools.iter().any(|held| held == tool);
        if !has("recall_memory") {
            continue;
        }
        assert!(
            has("relate_memory"),
            "{role} can recall chunks but cannot query the graph"
        );
        assert!(
            has("remember_memory"),
            "{role} can read memory but never write it"
        );
    }
    Ok(())
}

/// The stronger model goes to the roles whose output is a judgement nothing
/// mechanical can check, and only while they stay cheap.
///
/// Asserted rather than left to the constant's own comment, because the
/// expensive mistake here is silent: adding a role to the list costs money on
/// every run and nothing fails to say so.
#[test]
fn the_reasoning_model_reaches_the_judgement_roles() {
    for role in ["inventor", "reducer", "judge", "reflection", "director"] {
        assert!(
            REASONING_ROLES.contains(&role),
            "{role} judges and should be on the reasoning model"
        );
    }
}

/// The roles kept off it, each for a reason the constant records: the curator
/// is a run's measured top consumer and runs on a schedule, the library roles
/// read whole documents, and the rest execute or drive rather than judge.
#[test]
fn the_reasoning_model_is_kept_from_the_expensive_and_the_mechanical() {
    for role in [
        "context_curator",
        "scholar",
        "research",
        "librarian",
        "pattern_finder",
        "tool_builder",
        "coder",
        "goals",
        "orchestrator",
    ] {
        assert!(
            !REASONING_ROLES.contains(&role),
            "{role} would put the expensive model on frequent or bulk work"
        );
    }
}

/// Every role on the reasoning model must be one the runtime actually
/// registers, or the list is quietly describing a role that does not exist.
#[test]
fn every_reasoning_role_is_a_registered_agent() -> agent::Result<()> {
    let registry = default_registry(true)?;
    for role in REASONING_ROLES {
        assert!(
            registry.get(role).is_some(),
            "{role} is on the reasoning model but is not registered"
        );
    }
    Ok(())
}

/// The inventor's bench must name a registered agent too, for the same reason:
/// a spawn at a name nothing answers to is a failure the run only finds live.
#[test]
fn the_inventors_bench_is_a_registered_agent() -> agent::Result<()> {
    let registry = default_registry(true)?;
    for role in INVENTION_BENCH {
        assert!(
            registry.get(role).is_some(),
            "the inventor may delegate to {role}, which is not registered"
        );
    }
    // Bounded at one level: the bench holds a role that cannot itself delegate.
    assert_eq!(INVENTION_BENCH.len(), 1);
    assert!(!SPECIALISTS.contains(&"goals"));
    Ok(())
}

/// The engine switch is opt-in, and an unrecognised value selects the proven
/// path rather than failing: an operator who mistypes the variable should get
/// the state graph, not a stopped run.
#[test]
fn the_workflow_engine_is_opt_in_and_fails_safe() {
    for (value, expected) in [
        (None, false),
        (Some(""), false),
        (Some("graph"), false),
        // A typo is the case that matters. It must not be read as consent.
        (Some("wrokflow"), false),
        (Some("workflow"), true),
        (Some("  Workflow  "), true),
        (Some("WORKFLOW"), true),
    ] {
        assert_eq!(
            super::selects_workflow_engine(value),
            expected,
            "MATH_AGENT_ENGINE={value:?}"
        );
    }
}
