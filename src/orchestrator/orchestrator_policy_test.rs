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
    for role in ["reducer", "judge", "director"] {
        assert!(
            REASONING_ROLES.contains(&role),
            "{role} judges and should be on the reasoning model"
        );
    }
    for role in ["inventor", "reflection", "weakener", "orchestrator"] {
        assert!(
            MAX_REASONING_ROLES.contains(&role),
            "{role}'s judgement keeps improving with depth and should be on the deepest ladder"
        );
    }
}

/// No role is on two tiers at once.
///
/// Without this the answer would come from the order of two lines in
/// `tier_for` rather than from a decision anybody made, and the losing list
/// would keep reading as though it applied.
#[test]
fn the_two_reasoning_tiers_are_disjoint() {
    for role in MAX_REASONING_ROLES {
        assert!(
            !REASONING_ROLES.contains(&role),
            "{role} is on both reasoning tiers"
        );
    }
}

/// The deepest tier stays small, because every role added to it costs more per
/// call than the same role one tier down and nothing fails to say so.
#[test]
fn the_deepest_tier_stays_small() {
    assert!(
        MAX_REASONING_ROLES.len() <= 5,
        "the max-reasoning tier has stopped being the exception"
    );
    for role in ["goals", "context_curator", "scholar", "research", "coder"] {
        assert!(
            !MAX_REASONING_ROLES.contains(&role),
            "{role} is frequent or bulk work and must not be on the deepest ladder"
        );
    }
}

/// Every role on the deepest ladder must be one the runtime actually builds.
///
/// `orchestrator` is the exception and is checked by name: it is the top-level
/// harness rather than a delegate, so it is absent from the subagent registry
/// while still resolving its model through the tiers like any other role.
#[test]
fn every_max_reasoning_role_is_a_registered_agent() -> agent::Result<()> {
    let registry = default_registry(true)?;
    for role in MAX_REASONING_ROLES {
        assert!(
            role == "orchestrator" || registry.get(role).is_some(),
            "{role} is on the deepest ladder but is not registered"
        );
    }
    Ok(())
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

