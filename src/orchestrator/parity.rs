//! Proving the two engines decide a run the same way.
//!
//! The migration's one silent failure mode. The routing policy is the most
//! evidence-laden code in this crate — every threshold names the live run that
//! produced it — and it currently works. Re-expressing it as jq trades a
//! known-good component for an unverified one, and a ladder reading `>` where
//! the Rust reads `>=` changes when a run diversifies without failing anything.
//! A live run would not show it. A diff does.
//!
//! So both engines are replayed over the same states and their decisions
//! compared. Deterministic, free, and no provider involved: the routing policy
//! is a pure function of the counters on both sides, which is what makes the
//! comparison possible at all.
//!
//! # Exhaustive, not sampled
//!
//! The corpus is every combination of the counters over a range that reaches
//! past every threshold, rather than a handful of hand-picked cases. There are
//! only six inputs and each one matters within a small range, so the whole
//! decision space is a few thousand states — cheap enough that sampling would
//! buy nothing and could miss exactly the off-by-one this exists to catch.
//!
//! The one thing it cannot check is whether the *shared* answer is right. Both
//! engines read the same constants, so a wrong threshold is wrong in both and
//! agrees with itself. That is what `docs/solution-loop.md` and the routing
//! tests in `solutions_test.rs` are for; this file only proves the translation.

use serde_json::{Value, json};

use super::solutions::{Judged, Route, SolutionState};
use super::workflow::LOOP_NODE;

/// The scope a `switch` node's expression is resolved against.
///
/// The ladder addresses `nodes.<loop>.state`, which is where the `loop` node
/// publishes its accumulator, so the comparison has to present a state the same
/// way the engine would.
fn scope_for(state: &Value) -> Value {
    // Both ladders read `.item.json` — the step output they immediately
    // follow — so the comparison presents a state the way the engine does. The
    // accumulator is also supplied, because a ladder that regressed to reading
    // it would then still be *comparable* rather than resolving to null and
    // looking like agreement.
    json!({
        "item": { "json": state },
        "nodes": { LOOP_NODE: { "state": state } },
    })
}

/// The port the workflow's reflection ladder selects for `state`.
pub(super) fn workflow_route(state: &Value) -> String {
    tinyflows::expr::evaluate(&json!(super::workflow::reflect_ladder()), &scope_for(state))
        .as_str()
        .unwrap_or("<null>")
        .to_string()
}

/// The port the workflow's judge ladder selects, given a verdict.
pub(super) fn workflow_judged(state: &Value, verdict: &str) -> String {
    // The judge's verdict rides on the same state the counters do, which is
    // what `to_accumulator` produces. Building this scope by hand is what let a
    // mismatch between the ladder and the graph survive once, so
    // `the_ladders_read_fields_a_step_actually_emits` checks the spelling.
    let mut with_verdict = state.clone();
    if let Some(map) = with_verdict.as_object_mut() {
        map.insert("judged".into(), json!(verdict));
    }
    let scope = scope_for(&with_verdict);
    tinyflows::expr::evaluate(&json!(super::workflow::judge_ladder()), &scope)
        .as_str()
        .unwrap_or("<null>")
        .to_string()
}

/// The port name the state graph's [`Route`] corresponds to.
///
/// Written out rather than derived from `Display`, so the two vocabularies are
/// mapped in one visible place. `Route::Reported` renders as "reported
/// unverified" for a human and as `reported` for a port, and a mapping that
/// quietly relied on `Display` would break the day that wording improved.
pub(super) fn route_port(route: Route) -> &'static str {
    match route {
        Route::Solved => "solved",
        Route::Reported => "reported",
        Route::Retry => "retry",
        Route::Diversify => "diversify",
        Route::Blocked => "blocked",
    }
}

/// The port name the state graph's [`Judged`] corresponds to.
pub(super) fn judged_port(judged: Judged) -> &'static str {
    match judged {
        Judged::Reflect => "reflect",
        Judged::Restart => "restart",
    }
}

/// One state, in both engines' vocabularies.
///
/// Built from the counters the ladder reads. Anything else on
/// [`SolutionState`] is untouched by routing, so leaving it at its default
/// keeps the corpus about the decision rather than about the struct.
pub(super) struct Case {
    /// What the state graph routes on.
    pub(super) state: SolutionState,
    /// What the workflow routes on.
    pub(super) json: Value,
}

impl Case {
    /// Builds the same case for both engines.
    pub(super) fn new(
        attempts: usize,
        solved: bool,
        blocked: usize,
        unproductive: usize,
        computational: usize,
        unverified: usize,
        restarts: usize,
    ) -> Self {
        let mut state = SolutionState::new("a problem");
        state.attempts = attempts;
        state.solved = solved;
        state.blocked = blocked;
        state.unproductive = unproductive;
        state.computational = computational;
        state.unverified = unverified;
        state.restarts = restarts;
        Self {
            json: json!({
                "attempts": attempts,
                "solved": solved,
                "blocked": blocked,
                "unproductive": unproductive,
                "computational": computational,
                "unverified": unverified,
                "restarts": restarts,
            }),
            state,
        }
    }

    /// A one-line description, so a divergence names the state that caused it
    /// rather than leaving it to be reconstructed.
    pub(super) fn describe(&self) -> String {
        format!(
            "attempts={} solved={} blocked={} unproductive={} computational={} unverified={} \
             restarts={}",
            self.state.attempts,
            self.state.solved,
            self.state.blocked,
            self.state.unproductive,
            self.state.computational,
            self.state.unverified,
            self.state.restarts,
        )
    }
}

/// Every combination of the counters the routing policy reads.
///
/// The ranges reach past every threshold — the largest is `MAX_ATTEMPTS` at
/// eight — so each arm is exercised from below, at, and above its boundary,
/// which is where an off-by-one lives.
pub(super) fn corpus() -> Vec<Case> {
    let mut cases = Vec::new();
    for attempts in 0..=9 {
        for solved in [false, true] {
            for blocked in 0..=3 {
                for unproductive in 0..=3 {
                    for computational in 0..=3 {
                        for unverified in 0..=3 {
                            cases.push(Case::new(
                                attempts,
                                solved,
                                blocked,
                                unproductive,
                                computational,
                                unverified,
                                0,
                            ));
                        }
                    }
                }
            }
        }
    }
    cases
}

#[path = "parity_test.rs"]
mod test;
