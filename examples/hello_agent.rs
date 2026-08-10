//! Runs the OpenRouter-backed hello-world agent.
//!
//! ```sh
//! cargo run --example hello_agent -- "your task"
//! ```

use rust_template::HelloAgent;

#[tokio::main]
async fn main() -> rust_template::agent::Result<()> {
    let task = std::env::args().skip(1).collect::<Vec<_>>().join(" ");
    let task = if task.is_empty() {
        "Say hello, use add_numbers to calculate 20 + 22, then ask a sub-agent for one fun fact \
         about the number 42."
            .to_string()
    } else {
        task
    };

    let agent = HelloAgent::from_env()?;
    let answer = agent.run("hello-world", task).await?;
    println!("{answer}");
    Ok(())
}
