//! Runs the Docker-jailed registry-backed orchestrator.

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
    let answer = agent.run("orchestrator", task).await?;
    println!("{answer}");
    Ok(())
}
