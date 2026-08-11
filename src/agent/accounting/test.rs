//! Unit tests for per-call cost accounting.
#![allow(clippy::expect_used)]

use serde_json::json;

use super::accounting_from;
use crate::agent::trace::ModelAccounting;

#[test]
fn reads_provider_model_tokens_and_cost_from_a_response_body() {
    // The shape OpenRouter returns: cost and the cached-token breakdown are
    // always present, so neither has to be requested or derived.
    let raw = json!({
        "provider": "DeepInfra",
        "model": "deepseek/deepseek-v4-flash-0731",
        "usage": {
            "prompt_tokens": 7296,
            "completion_tokens": 2343,
            "total_tokens": 9639,
            "cost": 0.000_423_15,
            "prompt_tokens_details": { "cached_tokens": 5632 },
            "completion_tokens_details": { "reasoning_tokens": 1900 }
        }
    });

    let accounting = accounting_from("tool_builder", &raw);

    assert_eq!(accounting.provider.as_deref(), Some("DeepInfra"));
    assert_eq!(
        accounting.model.as_deref(),
        Some("deepseek/deepseek-v4-flash-0731")
    );
    assert_eq!(accounting.input_tokens, 7296);
    assert_eq!(accounting.cached_tokens, 5632);
    assert_eq!(accounting.output_tokens, 2343);
    assert_eq!(accounting.reasoning_tokens, 1900);
    assert!((accounting.usd - 0.000_423_15).abs() < f64::EPSILON);
    assert_eq!(accounting.micro_usd(), 423);
}

#[test]
fn a_body_missing_the_accounting_fields_reports_zero_rather_than_guessing() {
    // Not every provider reports a price. Recording nothing is honest;
    // inferring one from a local price table would be fiction the moment a
    // price changed.
    let accounting = accounting_from("research", &json!({ "id": "gen-1" }));

    assert_eq!(accounting.agent, "research");
    assert_eq!(accounting.provider, None);
    assert_eq!(accounting.model, None);
    assert_eq!(accounting.input_tokens, 0);
    assert_eq!(accounting.micro_usd(), 0);
}

#[test]
fn a_nonsense_cost_does_not_become_a_credit() {
    for usd in [-1.0, f64::NAN, f64::INFINITY] {
        let accounting = ModelAccounting {
            usd,
            ..ModelAccounting::default()
        };
        assert_eq!(accounting.micro_usd(), 0, "{usd}");
    }
}
