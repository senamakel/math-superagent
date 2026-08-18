//! Unit tests for the embedded `TinyAgents` runtime.

use super::{Message, ROUTER_CONTEXT_WINDOW, mock, router_model};
use tinyagents::harness::model::ModelRequest;

async fn capture_router_request(model_name: &str) -> super::Result<String> {
    use tokio::io::{AsyncReadExt as _, AsyncWriteExt as _};

    let listener = tokio::net::TcpListener::bind("127.0.0.1:0")
        .await
        .map_err(|error| {
            tinyagents::TinyAgentsError::Model(format!(
                "router test could not bind loopback: {error}"
            ))
        })?;
    let address = listener.local_addr().map_err(|error| {
        tinyagents::TinyAgentsError::Model(format!(
            "router test could not read its address: {error}"
        ))
    })?;
    let (sent, received) = tokio::sync::oneshot::channel();
    tokio::spawn(async move {
        let Ok((mut socket, _)) = listener.accept().await else {
            return;
        };
        let mut request = vec![0_u8; 8_192];
        let Ok(size) = socket.read(&mut request).await else {
            return;
        };
        request.truncate(size);
        let _ = sent.send(String::from_utf8_lossy(&request).into_owned());

        let body = r#"{"choices":[{"message":{"role":"assistant","content":"ok"},"finish_reason":"stop"}]}"#;
        let response = format!(
            "HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nContent-Length: {}\r\nConnection: close\r\n\r\n{body}",
            body.len()
        );
        let _ = socket.write_all(response.as_bytes()).await;
    });

    let model = router_model(
        "test-key".to_string(),
        &format!("http://{address}/v1"),
        model_name,
    );
    assert_eq!(
        model.profile().and_then(|profile| profile.max_input_tokens),
        Some(ROUTER_CONTEXT_WINDOW)
    );
    model
        .invoke(&(), ModelRequest::new(vec![Message::user("hello")]))
        .await?;

    received.await.map_err(|error| {
        tinyagents::TinyAgentsError::Model(format!("test server dropped request: {error}"))
    })
}

#[tokio::test]
async fn router_sends_authenticated_flash_and_reasoning_tiers() -> super::Result<()> {
    for model_name in ["flash", "reasoning"] {
        let request = capture_router_request(model_name).await?;
        let request = request.to_ascii_lowercase();
        assert!(
            request.contains("authorization: bearer test-key\r\n"),
            "router request omitted bearer authentication"
        );
        assert!(
            request.contains(&format!(r#""model":"{model_name}""#)),
            "router request omitted the `{model_name}` tier id"
        );
    }
    Ok(())
}

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
