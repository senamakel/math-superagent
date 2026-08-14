//! The compiled blocklist a calibration run is screened against.
//!
//! Loaded once at startup from the path in `MATH_AGENT_SCREEN`, which
//! `compose.eval.yaml` mounts read-only at `/etc/riemann/screen.json`. The file
//! is produced by `scripts/compile-screen` from the plaintext terms under
//! `evals/`, which never leave the host.
//!
//! # Absent means off, malformed means stop
//!
//! An unset `MATH_AGENT_SCREEN` yields no policy and nothing is screened, so an
//! ordinary run against an open conjecture is untouched by any of this.
//!
//! A *named* policy that cannot be read or parsed is a hard startup failure.
//! The alternative — carry on unscreened — is the one outcome that must not
//! happen, because it produces a calibration run that looks normal, spends
//! hours and provider credit, and measures nothing at all, with the only
//! evidence a line in a log nobody reads. Failing to start is loud and cheap.

use std::collections::HashSet;
use std::path::{Path, PathBuf};

use serde_json::Value;

use crate::agent::{Result, TinyAgentsError};

/// Environment variable naming the compiled policy.
pub(crate) const SCREEN_PATH_ENV: &str = "MATH_AGENT_SCREEN";

/// The compiled policy this run was pointed at, if any.
///
/// The whole of the environment read, kept to one function because the crate
/// forbids `unsafe` and mutating the process environment is the only way a test
/// could exercise it. Everything downstream takes a path, so everything
/// downstream is testable.
///
/// An empty value is treated as unset, so `MATH_AGENT_SCREEN=` in a compose
/// file — which is how an unset variable arrives through Docker's `${VAR:-}`
/// idiom — means "no screen" rather than "a policy at the empty path".
pub(crate) fn configured_path() -> Option<PathBuf> {
    let raw = std::env::var_os(SCREEN_PATH_ENV)?;
    let path = PathBuf::from(raw);
    (!path.as_os_str().is_empty()).then_some(path)
}

/// What the screen decided about one piece of text.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub(crate) enum Verdict {
    /// Nothing matched; the text passes untouched.
    Allow,
    /// A `[block]` term matched. The text is withheld.
    Deny,
    /// A `[flag]` term matched. Not withheld on its own — the adjudicator
    /// decides, and its failure is a denial.
    Adjudicate,
}

/// The compiled blocklist, and the settings that go with it.
#[derive(Clone, Debug)]
pub(crate) struct ScreenPolicy {
    /// Which calibration problem this policy belongs to. Carried only so the
    /// ledger and the trace can say which run they describe; it is the
    /// de-named slug the run already knows.
    pub(crate) slug: String,
    salt: String,
    max_ngram: usize,
    block: HashSet<String>,
    flag: HashSet<String>,
    deny_hosts: HashSet<String>,
    /// Whether the semantic second stage runs at all.
    pub(crate) adjudicator_enabled: bool,
    /// How long one adjudication may take before it is treated as a denial.
    pub(crate) adjudicator_timeout_seconds: u64,
    /// How much text is handed to the adjudicator.
    pub(crate) adjudicator_max_chars: usize,
}

impl ScreenPolicy {
    /// Reads and validates a compiled policy from `path`.
    ///
    /// # Errors
    ///
    /// Returns an error when the file cannot be read or does not carry the
    /// fields `scripts/compile-screen` emits.
    pub(crate) fn load(path: &Path) -> Result<Self> {
        let text = std::fs::read_to_string(path).map_err(|error| {
            TinyAgentsError::Validation(format!(
                "the screen policy at `{}` could not be read: {error}. \
                 {SCREEN_PATH_ENV} is set, so this run is a calibration run and must not \
                 continue unscreened",
                path.display()
            ))
        })?;
        let document: Value = serde_json::from_str(&text).map_err(|error| {
            TinyAgentsError::Validation(format!(
                "the screen policy at `{}` is not valid JSON: {error}",
                path.display()
            ))
        })?;

        let salt = document
            .get("salt")
            .and_then(Value::as_str)
            .filter(|salt| salt.len() >= 16)
            .ok_or_else(|| {
                TinyAgentsError::Validation(format!(
                    "the screen policy at `{}` has no `salt` of at least 16 characters; \
                     an unsalted blocklist is reversible by dictionary",
                    path.display()
                ))
            })?
            .to_string();

        let slug = document
            .get("slug")
            .and_then(Value::as_str)
            .unwrap_or("unnamed")
            .to_string();

        let max_ngram = document
            .get("max_ngram")
            .and_then(Value::as_u64)
            .filter(|width| *width >= 1)
            .ok_or_else(|| {
                TinyAgentsError::Validation(format!(
                    "the screen policy at `{}` has no positive `max_ngram`",
                    path.display()
                ))
            })?;

        let adjudicator = document.get("adjudicator");
        let policy = Self {
            slug,
            salt,
            max_ngram: usize::try_from(max_ngram).unwrap_or(usize::MAX),
            block: digest_set(&document, "block"),
            flag: digest_set(&document, "flag"),
            deny_hosts: digest_set(&document, "deny_hosts"),
            adjudicator_enabled: adjudicator
                .and_then(|section| section.get("enabled"))
                .and_then(Value::as_bool)
                .unwrap_or(true),
            adjudicator_timeout_seconds: adjudicator
                .and_then(|section| section.get("timeout_seconds"))
                .and_then(Value::as_u64)
                .unwrap_or(45),
            adjudicator_max_chars: adjudicator
                .and_then(|section| section.get("max_chars"))
                .and_then(Value::as_u64)
                .and_then(|chars| usize::try_from(chars).ok())
                .unwrap_or(24_000),
        };

        if policy.block.is_empty() {
            return Err(TinyAgentsError::Validation(format!(
                "the screen policy at `{}` has an empty `block` list; a policy that withholds \
                 nothing is almost certainly a compilation mistake, and it would produce a \
                 calibration run that measures nothing",
                path.display()
            )));
        }
        Ok(policy)
    }

    /// Screens a piece of text against the blocklist.
    ///
    /// [`Verdict::Deny`] wins over [`Verdict::Adjudicate`] — a `[block]` term
    /// is a decision, not an escalation — so the block set is tested first.
    pub(crate) fn screen_text(&self, text: &str) -> Verdict {
        let found = super::terms::digests_of(&self.salt, text, self.max_ngram);
        if !self.block.is_disjoint(&found) {
            return Verdict::Deny;
        }
        if !self.flag.is_disjoint(&found) {
            return Verdict::Adjudicate;
        }
        Verdict::Allow
    }

    /// Whether a URL names a host the policy withholds.
    ///
    /// The proxy is what actually enforces the host denylist, and it holds the
    /// plaintext. This copy exists so a denied URL can be refused *before* the
    /// request is made, which produces a ledger entry naming the tool and the
    /// argument instead of a proxy failure arriving later as an opaque network
    /// error.
    ///
    /// Subdomains are covered: `arxiv.org` in the denylist withholds
    /// `export.arxiv.org`, because the suffix's own tokens are a sub-n-gram of
    /// the host's.
    pub(crate) fn denies_host(&self, url: &str) -> bool {
        let Some(host) = host_of(url) else {
            return false;
        };
        let found = super::terms::digests_of(&self.salt, &host, self.max_ngram);
        !self.deny_hosts.is_disjoint(&found)
    }
}

/// Reads one array of hex digests out of the compiled policy.
///
/// A missing or malformed section yields an empty set rather than an error.
/// `block` being empty is checked separately and *is* an error; `flag` and
/// `deny_hosts` are genuinely optional, and a problem may legitimately have
/// neither.
fn digest_set(document: &Value, field: &str) -> HashSet<String> {
    document
        .get(field)
        .and_then(Value::as_array)
        .map(|entries| {
            entries
                .iter()
                .filter_map(Value::as_str)
                .map(str::to_ascii_lowercase)
                .collect()
        })
        .unwrap_or_default()
}

/// The host component of a URL, without scheme, credentials, port or path.
///
/// Written out rather than pulled from a URL parser because the input here is
/// a model-supplied string that may not be a valid URL at all, and the right
/// answer for "not a URL" is "no host" rather than an error.
fn host_of(url: &str) -> Option<String> {
    let after_scheme = url
        .split_once("://")
        .map_or(url, |(_, remainder)| remainder);
    let authority = after_scheme
        .split(['/', '?', '#'])
        .next()
        .filter(|authority| !authority.is_empty())?;
    let host = authority
        .rsplit_once('@')
        .map_or(authority, |(_, host)| host)
        .split(':')
        .next()?;
    (!host.is_empty()).then(|| host.to_ascii_lowercase())
}

#[cfg(test)]
impl ScreenPolicy {
    /// Builds a policy directly from plaintext terms, for tests.
    ///
    /// The production path only ever loads digests, because the plaintext must
    /// not be inside the container. A test is on the host and needs to say what
    /// it is blocking in order to be readable, so it compiles the terms here
    /// through the same [`super::terms`] functions the loader compares against.
    pub(crate) fn for_test(block: &[&str], flag: &[&str], deny_hosts: &[&str]) -> Self {
        let salt = "test-salt-0123456789abcdef";
        let compile = |terms: &[&str]| {
            terms
                .iter()
                .map(|term| super::terms::digest(salt, &super::terms::tokenise(term)))
                .collect()
        };
        Self {
            slug: "test-problem".to_string(),
            salt: salt.to_string(),
            max_ngram: 10,
            block: compile(block),
            flag: compile(flag),
            deny_hosts: compile(deny_hosts),
            adjudicator_enabled: true,
            adjudicator_timeout_seconds: 5,
            adjudicator_max_chars: 24_000,
        }
    }
}

#[cfg(test)]
#[path = "policy_test.rs"]
mod test;
