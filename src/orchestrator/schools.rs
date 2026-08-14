//! The schools: two or three mathematicians working the same problem at once.
//!
//! The runtime attacked a problem exactly one way, and it did not choose to.
//! `research/mathematicians/12-cross-cutting.md` sets eleven mathematicians
//! against each other and states the rule this module exists to apply: *where
//! all eleven agree, the runtime has a requirement; where they split, the
//! runtime has a setting it did not know it had chosen.*
//!
//! It had chosen two. Every control on this branch is one side of Split 1 —
//! `weakener` lowers the target, `refuter` attacks the statement, `searcher`
//! hits a score function, `reducer` finds sufficient lemmas — and
//! `src/prompts/method_policy.md` opens by requiring computation before prose,
//! which is one side of Split 4. Neither was argued for. The cross-cutting file
//! is blunt about how the first happened: the rising sea *"is unaffordable
//! under `MAX_ATTEMPTS = 8` and `STUCK_THRESHOLD = 2`"*, so **the thresholds
//! decided the methodology and no document said so**.
//!
//! A school is that setting made explicit, and it is deliberately only four
//! things: a method-policy overlay, per-role prompt overlays, a bench, and
//! [`Thresholds`]. It is not a second loop, a second graph or a second set of
//! roles — those are shared, because the point is several mathematicians in one
//! workspace rather than several runtimes in one container.
//!
//! # The control comes first
//!
//! [`CHISEL`] is today's runtime under a name: its overlay is empty, its
//! thresholds are the existing constants, and [`selected`] returns it alone
//! unless somebody asks for more. That is not timidity, it is what makes the
//! rest measurable — a new school is only ever evidence if the old one is
//! running beside it on the same problem, and a change that altered the control
//! while adding the alternatives could not be read at all.

use super::solutions::{
    BLOCKED_THRESHOLD, COMPUTATIONAL_THRESHOLD, MAX_ATTEMPTS, MAX_RESTARTS, REDUCTION_INTERVAL,
    STUCK_THRESHOLD, UNVERIFIED_THRESHOLD,
};

/// The environment variable naming which schools run.
///
/// Comma-separated slugs. Under the rule every other override in this runtime
/// follows, a missing, empty or unrecognised value keeps the default rather
/// than silently removing it — see [`selected`].
const SELECTION_VAR: &str = "MATH_AGENT_SCHOOLS";

/// Every counter the routing ladder and the loop's terminal condition read.
///
/// Gathered into one value because there are now more than one set of them and
/// **two** places that must agree on each: [`super::solutions::route`], which is
/// the executable specification of the routing policy, and the jq the workflow
/// engine actually runs, which [`super::workflow`] generates. A second list
/// would be a second answer to a question about when a run stops, and
/// `orchestrator::parity` exists precisely to prove there is only one — it now
/// proves it for every school rather than for one.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub(in crate::orchestrator) struct Thresholds {
    /// Attempts allowed before the loop reports what it has.
    pub(in crate::orchestrator) max_attempts: usize,
    /// Consecutive unproductive attempts before diversifying rather than retrying.
    pub(in crate::orchestrator) stuck: usize,
    /// Consecutive attempts lost to the provider before the loop stops trying.
    pub(in crate::orchestrator) blocked: usize,
    /// Consecutive attempts whose only gain was a larger instance.
    pub(in crate::orchestrator) computational: usize,
    /// Consecutive single-route answers before the loop reports what it has.
    pub(in crate::orchestrator) unverified: usize,
    /// Restarts the judge may force in one run.
    pub(in crate::orchestrator) max_restarts: usize,
    /// Completed cycles between one decomposition of the goal and the next.
    pub(in crate::orchestrator) reduction_interval: usize,
}

impl Thresholds {
    /// The numbers the runtime has always used.
    ///
    /// Read off the constants rather than repeated here, so the evidence that
    /// justifies each one — every threshold in
    /// [`super::solutions`] carries the live run that set it — stays attached to
    /// the number instead of drifting from a copy.
    pub(in crate::orchestrator) const fn chisel() -> Self {
        Self {
            max_attempts: MAX_ATTEMPTS,
            stuck: STUCK_THRESHOLD,
            blocked: BLOCKED_THRESHOLD,
            computational: COMPUTATIONAL_THRESHOLD,
            unverified: UNVERIFIED_THRESHOLD,
            max_restarts: MAX_RESTARTS,
            reduction_interval: REDUCTION_INTERVAL,
        }
    }

    /// A longer leash, for a school whose method does not show progress every
    /// attempt.
    ///
    /// Raising a threshold is declined in `docs/methods-proposals.md` — *"it
    /// spends more budget on the same measurement"* — and that decline stands
    /// for the single loop it was written about. It does not reach here. The
    /// rising sea is not the same measurement run longer: it is a method whose
    /// whole shape is that the goal does not move while the theory around it
    /// does, which the unproductive counter cannot tell apart from being stuck.
    /// The cross-cutting file names that exact confusion as the reason the
    /// method was never affordable.
    ///
    /// It is still bounded, and by the same wall clock as everything else. What
    /// changes is which of the two stops it: attempts rather than a premature
    /// diversify away from the only method it has.
    const fn patient() -> Self {
        Self {
            stuck: STUCK_THRESHOLD + 2,
            computational: COMPUTATIONAL_THRESHOLD + 1,
            ..Self::chisel()
        }
    }
}

/// One mathematician's way of working.
#[derive(Clone, Copy, Debug)]
pub(in crate::orchestrator) struct School {
    /// The name it is addressed and traced by. Also its workspace subtree.
    pub(in crate::orchestrator) slug: &'static str,
    /// One line saying what this school is a bet on, for the run's report.
    pub(in crate::orchestrator) stance: &'static str,
    /// What it may spend and when it changes course.
    pub(in crate::orchestrator) thresholds: Thresholds,
    /// Added to the shared method policy, never replacing it.
    ///
    /// The shared policy carries the rules that are requirements rather than
    /// settings — never invent a citation, verify independently, declare the
    /// complexity you actually have — and the cross-cutting file's *"where all
    /// eleven agree"* section is what makes them requirements. A school that
    /// could replace them would be a school that could switch them off.
    pub(in crate::orchestrator) policy: &'static str,
}

impl School {
    /// The role name this school addresses `role` by.
    ///
    /// Each school registers its own copy of every role, because a role's
    /// prompt is where the school actually lives. Qualifying the name is how
    /// one [`super::AsyncSubagentManager`] — and so one concurrency semaphore,
    /// one trace and one budget pool — serves all of them.
    pub(in crate::orchestrator) fn role(&self, role: &str) -> String {
        format!("{role}@{}", self.slug)
    }
}

/// Today's runtime, named.
///
/// The empty policy is the load-bearing part: it makes this school's assembled
/// prompts byte-identical to the ones the runtime sent before schools existed,
/// which `schools_test` asserts rather than assumes.
const CHISEL: School = School {
    slug: "chisel",
    stance: "attack the problem where it stands, and compute before reasoning about it",
    thresholds: Thresholds::chisel(),
    policy: "",
};

/// Grothendieck and Scholze: change the ground rather than the target.
const RISING_SEA: School = School {
    slug: "rising-sea",
    stance: "enlarge the setting until the problem dissolves, and keep the goal fixed",
    thresholds: Thresholds::patient(),
    policy: include_str!("../prompts/schools/rising-sea.md"),
};

/// Erdős, Gowers and Zeilberger: break it before believing it.
const ADVERSARIAL: School = School {
    slug: "adversarial",
    stance: "try to refute the statement before attempting it, and price what is not proved",
    thresholds: Thresholds::chisel(),
    policy: include_str!("../prompts/schools/adversarial.md"),
};

/// Every school this runtime knows how to run.
pub(in crate::orchestrator) const ALL: [School; 3] = [CHISEL, RISING_SEA, ADVERSARIAL];

/// The schools this run will use.
///
/// Reads [`SELECTION_VAR`]. An unset, empty, or wholly unrecognised value keeps
/// [`CHISEL`] alone — the same rule [`crate::agent::budget`] applies to every
/// other override, so a typo cannot silently reconfigure a run's methodology.
/// Unrecognised names among recognised ones are dropped rather than failing the
/// run, and duplicates collapse, so the order the caller wrote is preserved
/// without it being able to run one school twice.
pub(in crate::orchestrator) fn selected() -> Vec<School> {
    let Ok(raw) = std::env::var(SELECTION_VAR) else {
        return vec![CHISEL];
    };
    let mut chosen: Vec<School> = Vec::new();
    for name in raw.split(',') {
        let name = name.trim();
        if name.is_empty() || chosen.iter().any(|school| school.slug == name) {
            continue;
        }
        if let Some(school) = ALL.iter().find(|school| school.slug == name) {
            chosen.push(*school);
        }
    }
    if chosen.is_empty() {
        return vec![CHISEL];
    }
    chosen
}

#[cfg(test)]
#[path = "schools_test.rs"]
mod test;
