//! An embeddable, vendored `TinyAgents` harness.
//!
//! The vendored `TinyAgents` runtime provides model and tool orchestration
//! without the full application's memory, channels, or Web3 domains.
//! [`HelloAgent`] supplies a minimal OpenRouter-backed loop with arithmetic,
//! echo, Exa search, and sub-agent delegation tools. Loop events are exported
//! to Langfuse on a best-effort basis.
//!
//! # Layout
//!
//! - `src/error/` holds the crate-wide [`Error`] enum and the [`Result`] alias
//!   returned by every fallible public function.
//! - Each feature area lives in its own module directory with a `mod.rs`
//!   module root, an optional `types.rs`, and a `test.rs` holding its unit
//!   tests.
//! - Every public item is re-exported from here, so downstream users have a
//!   single predictable surface.
//! - `agent` exposes the `TinyAgents` harness facade.
//! - [`HelloAgent`] exposes the runnable hello-world agent.
//!
//! # Example
//!
//! ```
//! use rust_template::{greet, Error};
//!
//! assert_eq!(greet("Ferris")?, "Hello, Ferris!");
//! assert_eq!(greet("   ").unwrap_err(), Error::EmptyName);
//! # Ok::<(), rust_template::Error>(())
//! ```
//!
pub mod agent;
mod error;
mod greeting;
mod hello_agent;

pub use error::{Error, Result};
pub use greeting::greet;
pub use hello_agent::HelloAgent;
