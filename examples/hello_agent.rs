//! Runs the provider-backed hello-world agent.
//!
//! ```sh
//! cargo run --example hello_agent -- "your task"
//! ```

use math_agent::HelloAgent;

#[tokio::main]
async fn main() -> math_agent::agent::Result<()> {
    let task = std::env::args().skip(1).collect::<Vec<_>>().join(" ");
    let task = if task.is_empty() {
        "Say hello, use add_numbers to calculate 20 + 22, ask a sub-agent why 42 is culturally \
         recognizable, and use Exa to find one current source about TinyAgents."
            .to_string()
    } else {
        task
    };

    let agent = HelloAgent::from_env()?;
    let answer = agent.run("hello-world", task).await?;
    println!("{answer}");
    Ok(())
}
