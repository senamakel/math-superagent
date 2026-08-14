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
//! # And for every school, not for one
//!
//! There is no longer one set of thresholds. A school is a method policy and a
//! [`Thresholds`], several run at once, and each builds its own graph — so
//! there is one translation to prove per distinct set of numbers, and proving
//! it for the control school would leave every other school's ladder untested.
//! [`corpus`] therefore takes the thresholds it is sweeping and derives its
//! ranges from them: a school with a higher `max_attempts` gets a sweep that
//! reaches past it, rather than a fixed range that stops short and calls the
//! untested room agreement.
//!
//! The one thing it cannot check is whether the *shared* answer is right. Both
//! engines read the same numbers, so a wrong threshold is wrong in both and
//! agrees with itself. That is what `docs/solution-loop.md` and the routing
//! tests in `solutions_test.rs` are for; this file only proves the translation.

use serde_json::{Value, json};

use super::schools::{self, Thresholds};
use super::solutions::{Route, SolutionState};
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

/// The port the workflow's reflection ladder selects for `state`, under one
/// school's bounds.
pub(super) fn workflow_route(state: &Value, thresholds: &Thresholds) -> String {
    tinyflows::expr::evaluate(
        &json!(super::workflow::reflect_ladder(thresholds)),
        &scope_for(state),
    )
    .as_str()
    .unwrap_or("<null>")
    .to_string()
}

/// Every school whose translation has to be proved, named.
///
/// Read off [`schools::ALL`] rather than listed, so a school added there is a
/// school this gate covers. The slug travels with the numbers because a
/// divergence should say *whose* ladder disagreed, and two schools sharing a
/// set of numbers are both worth naming — the sweep is a few thousand pure
/// comparisons, so deduplicating them would save nothing and lose that.
pub(super) fn schools_under_test() -> Vec<(&'static str, Thresholds)> {
    schools::ALL
        .iter()
        .map(|school| (school.slug, school.thresholds))
        .collect()
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
/// Each range reaches one past the threshold that reads it, so every arm is
/// exercised from below, at, and above its boundary, which is where an
/// off-by-one lives. Derived from the thresholds under test rather than fixed:
/// a school that raises `stuck` to four and sweeps to three would never reach
/// its own diversify arm, and the sweep would report agreement about a decision
/// it never asked either engine to make.
///
/// For the control school this is the same corpus as before — every threshold
/// is two and the attempt ceiling is eight, so the ranges are `0..=3` and
/// `0..=9`, exactly the numbers that used to be written here.
pub(super) fn corpus(thresholds: &Thresholds) -> Vec<Case> {
    let mut cases = Vec::new();
    for attempts in 0..=thresholds.max_attempts + 1 {
        for solved in [false, true] {
            for blocked in 0..=thresholds.blocked + 1 {
                for unproductive in 0..=thresholds.stuck + 1 {
                    for computational in 0..=thresholds.computational + 1 {
                        for unverified in 0..=thresholds.unverified + 1 {
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
