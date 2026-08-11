//! Runs the Docker-jailed registry-backed orchestrator.
//!
//! Two modes. The default gives the orchestrator one turn and trusts it to
//! delegate well, which suits a problem whose approach is clear. Setting
//! `MATH_AGENT_SOLVE_LOOP=on` instead runs the graph-backed solution loop,
//! which attempts, reflects on what happened, and diversifies when repeated
//! attempts stop making progress. Use the loop when the first approach is
//! likely to be wrong, which is the usual case for a hard problem.

use math_agent::OrchestratorAgent;

#[tokio::main]
async fn main() -> math_agent::agent::Result<()> {
    let task = std::env::args().skip(1).collect::<Vec<_>>().join(" ");
    let task = if task.is_empty() {
        "Ask research for one current source about Rust agents, then ask tool_builder to create \
         and run a tiny shell tool that prints hello from /workspace."
            .to_string()
    } else {
        task
    };

    let agent = OrchestratorAgent::from_env()?;
    let answer = if solution_loop_enabled() {
        agent.solve(task).await?
    } else {
        agent.run("orchestrator", task).await?
    };
    println!("{answer}");
    Ok(())
}

/// Returns whether the graph-backed solution loop should drive this run.
fn solution_loop_enabled() -> bool {
    matches!(
        std::env::var("MATH_AGENT_SOLVE_LOOP")
            .unwrap_or_default()
            .trim()
            .to_ascii_lowercase()
            .as_str(),
        "on" | "1" | "true" | "yes" | "enabled"
    )
}
