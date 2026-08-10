//! Unit tests for the embedded `TinyAgents` runtime.

use super::{Message, mock};

#[tokio::test]
async fn mock_harness_runs_without_application_domains() -> super::Result<()> {
    let harness = mock("Hello from the slim agent.");
    let run = harness
        .invoke_default(&(), vec![Message::user("Say hello.")])
        .await?;

    assert_eq!(run.text().as_deref(), Some("Hello from the slim agent."));
    assert_eq!(run.model_calls, 1);
    Ok(())
}
