//! Runs the Docker-jailed registry-backed orchestrator.
//!
//! Every run goes through the graph-backed solution loop: attempt, reflect on
//! what actually happened, and diversify when repeated attempts stop making
//! progress. There is deliberately no single-turn mode. A hard problem's first
//! approach is usually wrong, and the single-turn path differed only in
//! discarding that information.
//!
//! `--mill <source>` runs the formalisation mill instead of the solution loop:
//! it reads prose the workspace already holds, or a paper named on the command
//! line, and turns what it can into Lean the kernel has accepted. A second mode
//! rather than a second binary, because the image ships one entrypoint and the
//! mill needs the same provider setup, the same workspace mount, and the same
//! registered roles the loop does.

use math_agent::OrchestratorAgent;

#[tokio::main]
async fn main() -> math_agent::agent::Result<()> {
    let arguments = std::env::args().skip(1).collect::<Vec<_>>();
    if let Some(index) = arguments.iter().position(|argument| argument == "--mill") {
        return mill(&arguments, index).await;
    }

    let task = arguments.join(" ");
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

/// Runs one pass of the formalisation mill.
async fn mill(arguments: &[String], index: usize) -> math_agent::agent::Result<()> {
    let Some(source) = arguments.get(index + 1) else {
        return Err(math_agent::agent::TinyAgentsError::Validation(
            "usage: --mill <path|url|arxiv-id> [--budget <n>]".to_string(),
        ));
    };
    let budget = arguments
        .iter()
        .position(|argument| argument == "--budget")
        .and_then(|at| arguments.get(at + 1))
        .and_then(|value| value.parse::<usize>().ok());

    let agent = OrchestratorAgent::from_env()?;
    println!("{}", agent.mill(source, budget).await?);
    Ok(())
}
