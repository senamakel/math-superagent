//! An embeddable, vendored `TinyAgents` harness.
//!
//! This crate is a template. It ships the layout, lint configuration, error
//! handling, testing, and documentation conventions described in `AGENTS.md`.
//! The vendored `TinyAgents` runtime provides model and tool orchestration
//! without the full application's memory, channels, or Web3 domains.
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
//! Replace the `greeting` module with the first real feature area, keep the
//! conventions, and update this documentation to describe the new crate.

pub mod agent;
mod error;
mod greeting;

pub use error::{Error, Result};
pub use greeting::greet;
