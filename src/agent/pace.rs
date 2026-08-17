//! A departure schedule for a provider account with a published rate limit.
//!
//! Mistral's measured ceiling on the Leanstral tier is 0.63 requests per
//! second — the token allowance, 5M per minute, is slack by comparison at that
//! rate, so requests per second is the bound worth enforcing. Above it the
//! account returns 429, and the retry ladder then absorbs the rejection as
//! minutes of backoff across every waiting run at once, which is the same
//! failure the orchestrator's subagent pool documents for unbounded fan-out.
//!
//! This is a next-slot scheduler rather than a token bucket, and the
//! difference is the point. A bucket that has been idle holds a full burst,
//! so the first six candidate slots to want the model depart together and are
//! rejected together — precisely the case being prevented. Handing out one
//! monotonically increasing departure instant spaces them instead.
//!
//! The limit belongs to the API key, not to any one caller, so this wraps the
//! *tier*: the model is built once and cloned into every school, candidate and
//! sub-agent, which makes one wrapper enough to pace the whole process.

use std::sync::Arc;
use std::time::Duration;

use async_trait::async_trait;
use tinyagents::harness::model::{
    ChatModel, ModelProfile, ModelRequest, ModelResponse, ModelStream,
};
use tokio::sync::{Mutex, Semaphore};
use tokio::time::Instant;

use crate::agent::Result;

/// Requests per second allowed against the scribe tier.
///
/// The account's published figure. Kept as the default rather than shaded
/// downwards because the retry ladder is still behind it: this is the floor
/// that stops a burst, not the only thing standing between a run and a 429.
const DEFAULT_SCRIBE_RPS: f64 = 0.63;

/// Requests allowed in flight at once against the scribe tier.
///
/// One, because at 0.63 requests per second a second concurrent call has
/// nothing to do but wait for a departure slot it could have waited for
/// outside the connection.
const DEFAULT_SCRIBE_CONCURRENCY: usize = 1;

/// Spaces requests to a provider that publishes a rate limit.
///
/// Two independent bounds: how many calls may be in flight, and how closely
/// their departures may be spaced. A call acquires a permit, waits for its
/// slot, and only then reaches the wrapped model.
pub struct PacedModel<S: Send + Sync> {
    inner: Arc<dyn ChatModel<S>>,
    slots: Arc<Semaphore>,
    /// The earliest instant the next request may depart.
    next: Arc<Mutex<Instant>>,
    interval: Duration,
}

impl<S: Send + Sync> std::fmt::Debug for PacedModel<S> {
    fn fmt(&self, formatter: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        formatter
            .debug_struct("PacedModel")
            .field("interval", &self.interval)
            .field("permits", &self.slots.available_permits())
            .finish_non_exhaustive()
    }
}

impl<S: Send + Sync> PacedModel<S> {
    /// Wraps `inner` at `rps` requests per second, `concurrency` in flight.
    ///
    /// A non-positive or non-finite `rps` is treated as unpaced rather than as
    /// an error: the wrapper is a bound, and a malformed bound should not stop
    /// a run that would otherwise work.
    #[must_use]
    pub fn new(inner: Arc<dyn ChatModel<S>>, rps: f64, concurrency: usize) -> Self {
        let interval = if rps.is_finite() && rps > 0.0 {
            Duration::from_secs_f64(1.0 / rps)
        } else {
            Duration::ZERO
        };
        Self {
            inner,
            slots: Arc::new(Semaphore::new(concurrency.max(1))),
            next: Arc::new(Mutex::new(Instant::now())),
            interval,
        }
    }

    /// Wraps `inner` with the scribe tier's bounds, environment first.
    ///
    /// `MATH_AGENT_SCRIBE_RPS` and `MATH_AGENT_SCRIBE_CONCURRENCY` override
    /// them. An unset, empty, unparsable, or non-positive value keeps the
    /// default, so a malformed override never removes the bound.
    #[must_use]
    pub fn scribe_from_env(inner: Arc<dyn ChatModel<S>>) -> Self {
        let rps = std::env::var("MATH_AGENT_SCRIBE_RPS")
            .ok()
            .and_then(|value| value.trim().parse::<f64>().ok())
            .filter(|value| value.is_finite() && *value > 0.0)
            .unwrap_or(DEFAULT_SCRIBE_RPS);
        let concurrency = std::env::var("MATH_AGENT_SCRIBE_CONCURRENCY")
            .ok()
            .and_then(|value| value.trim().parse::<usize>().ok())
            .filter(|value| *value > 0)
            .unwrap_or(DEFAULT_SCRIBE_CONCURRENCY);
        Self::new(inner, rps, concurrency)
    }

    /// Waits until this request's departure slot, and claims the one after it.
    ///
    /// The lock is held only long enough to read and advance the schedule; the
    /// sleep happens after it is released, so waiting calls queue on the
    /// schedule rather than on each other.
    async fn depart(&self) {
        if self.interval.is_zero() {
            return;
        }
        let departure = {
            let mut next = self.next.lock().await;
            let departure = (*next).max(Instant::now());
            *next = departure + self.interval;
            departure
        };
        tokio::time::sleep_until(departure).await;
    }
}

#[async_trait]
impl<S: Send + Sync + 'static> ChatModel<S> for PacedModel<S> {
    fn profile(&self) -> Option<&ModelProfile> {
        self.inner.profile()
    }

    async fn invoke(&self, state: &S, request: ModelRequest) -> Result<ModelResponse> {
        let _permit = self.slots.acquire().await;
        self.depart().await;
        self.inner.invoke(state, request).await
    }

    async fn stream(&self, state: &S, request: ModelRequest) -> Result<ModelStream> {
        let _permit = self.slots.acquire().await;
        self.depart().await;
        self.inner.stream(state, request).await
    }
}

#[cfg(test)]
#[path = "pace_test.rs"]
mod test;
