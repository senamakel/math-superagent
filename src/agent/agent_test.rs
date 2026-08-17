//! Unit tests for the embedded `TinyAgents` runtime.

use super::{
    Message, is_openrouter_base_url, is_surplus_base_url, mock, openrouter_client,
    openrouter_model_name,
};
use tinyagents::harness::model::{ChatModel as _, ModelRequest};

#[tokio::test]
async fn openrouter_requests_identify_opencompany() -> super::Result<()> {
    use tokio::io::{AsyncReadExt as _, AsyncWriteExt as _};

    let listener = tokio::net::TcpListener::bind("127.0.0.1:0")
        .await
        .map_err(|error| {
            tinyagents::TinyAgentsError::Model(format!(
                "attribution test could not bind loopback: {error}"
            ))
        })?;
    let address = listener.local_addr().map_err(|error| {
        tinyagents::TinyAgentsError::Model(format!(
            "attribution test could not read its address: {error}"
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

    let model = openrouter_client("test-key")
        .with_base_url(format!("http://{address}/v1"))
        .with_model("test-model");
    model
        .invoke(&(), ModelRequest::new(vec![Message::user("hello")]))
        .await?;

    let request = received.await.map_err(|error| {
        tinyagents::TinyAgentsError::Model(format!("test server dropped request: {error}"))
    })?;
    let request = request.to_ascii_lowercase();
    assert!(
        request.contains("http-referer: https://opencompany.tinyhumans.ai/\r\n"),
        "request omitted the OpenCompany URL: {request}"
    );
    assert!(
        request.contains("x-openrouter-title: opencompany\r\n"),
        "request omitted the OpenCompany title: {request}"
    );
    assert!(
        request.contains("x-openrouter-categories: personal-agent\r\n"),
        "request omitted the OpenCompany category: {request}"
    );
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

#[test]
fn only_the_openrouter_endpoint_enables_its_routing_dialect() {
    assert!(is_openrouter_base_url("https://openrouter.ai/api/v1"));
    assert!(is_openrouter_base_url("https://openrouter.ai/api/v1/"));
    assert!(!is_openrouter_base_url(
        "https://api.surplusintelligence.ai/v1"
    ));
}

#[test]
fn the_default_endpoint_and_fallback_model_use_each_providers_dialect() {
    assert!(is_surplus_base_url(
        "https://api.surplusintelligence.ai/v1/"
    ));
    assert_eq!(
        openrouter_model_name("deepseek-v4-flash-0731"),
        "deepseek/deepseek-v4-flash-0731"
    );
    assert_eq!(
        openrouter_model_name("anthropic/claude-sonnet-4.6"),
        "anthropic/claude-sonnet-4.6"
    );
}
