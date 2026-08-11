//! Runs the Docker-jailed registry-backed orchestrator.
//!
//! Every run goes through the graph-backed solution loop: attempt, reflect on
//! what actually happened, and diversify when repeated attempts stop making
//! progress. There is deliberately no single-turn mode. A hard problem's first
//! approach is usually wrong, and the single-turn path differed only in
//! discarding that information.

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
    println!("{}", agent.solve(task).await?);
    Ok(())
}
