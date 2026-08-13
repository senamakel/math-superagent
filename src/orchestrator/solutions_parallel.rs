// Graph-level fan-out: the diversify arms as concurrent nodes.
//
// Diversifying runs three independent lines of work — fetch and read the
// literature, look for structure in what the run has already computed, and
// invent a different line of attack. They do not read each other, which is
// what makes them concurrent.
//
// They used to be concurrent *inside* one node, joined with `tokio::join!`.
// That worked and was invisible: the graph saw one node that took a long
// time, so the fan-out could not be drawn, could not be bounded by graph
// policy, and a checkpoint could only ever land before or after the whole
// group. Now each arm is a node. `diversify` fans out to all three with one
// [`Command`], each runs in its own activation, and `diversify_merge` is a
// waiting-edge barrier that fires once all three have arrived.
//
// # Why the update type changed
//
// Concurrency is what forced [`LoopUpdate`]. With whole-state updates, three
// arms finishing in the same superstep each hand back a whole
// [`SolutionState`], and the runtime has three candidate next states and no
// principled way to choose — that is exactly the
// [`GraphError::InvalidConcurrentUpdate`](crate::agent::flow::GraphError) the
// runtime raises rather than silently picking one.
//
// So a node now says either "here is the whole state" — true of every node on
// the sequential path, which nothing else is running beside — or "here is what
// my arm found", which names the slot it writes. Two arms can be merged in
// either order and give the same state, because they never touch the same
// slot. `diversify_merge` is where the slots become prose again.

/// The arms `diversify` fans out to, and the barrier they converge on.
///
/// Named here rather than at the call sites so the fan-out, the barrier
/// registration, and the rendered picture cannot name different sets.
pub(super) const DIVERSIFY_ARMS: [&str; 3] = [
    "diversify_library",
    "diversify_patterns",
    "diversify_invention",
];

/// Where the arms converge.
pub(super) const DIVERSIFY_MERGE: &str = "diversify_merge";

/// One slot a diversify arm writes.
///
/// Two slots per arm in two cases, because those arms are sequential pairs
/// internally: the scholar reads what the librarian just downloaded, and the
/// inventor's choice follows the grounding it was checked against. Running
/// either pair as two graph nodes would express an ordering the graph would
/// then have to be told about; running it as one node with two slots says the
/// same thing without an edge.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub(super) enum Slot {
    /// What the librarian gathered.
    Library,
    /// What the scholar made of it.
    Digest,
    /// What the pattern arm found in the numbers already computed.
    Patterns,
    /// What the literature says about the invented candidates.
    Grounding,
    /// The line of attack the inventor settled on.
    Chosen,
}

/// One arm's contribution to a diversify.
#[derive(Clone, Debug)]
pub(super) struct Finding {
    /// Which slot this fills.
    pub(super) slot: Slot,
    /// What the arm reported.
    pub(super) text: String,
}

impl Finding {
    /// Builds a finding for `slot`.
    pub(super) fn new(slot: Slot, text: impl Into<String>) -> Self {
        Self {
            slot,
            text: text.into(),
        }
    }
}

/// Everything the arms have reported for the diversify in progress.
///
/// Cleared by `diversify_merge` once folded into `fresh_context`, so a later
/// diversify never inherits an earlier one's findings.
#[derive(Clone, Debug, Default)]
pub(super) struct DiversifyFindings {
    library: String,
    digest: String,
    patterns: String,
    grounding: String,
    chosen: String,
}

impl DiversifyFindings {
    /// Files one arm's report.
    fn set(&mut self, finding: Finding) {
        let slot = match finding.slot {
            Slot::Library => &mut self.library,
            Slot::Digest => &mut self.digest,
            Slot::Patterns => &mut self.patterns,
            Slot::Grounding => &mut self.grounding,
            Slot::Chosen => &mut self.chosen,
        };
        *slot = finding.text;
    }

    /// The findings as the labelled sections `merge_context` expects, in the
    /// order a reader wants them: what was gathered, what it means, what the
    /// numbers show, and what to do next.
    pub(super) fn sections(&self) -> [(&'static str, &str); 5] {
        [
            ("Reference material", self.library.as_str()),
            ("What the sources establish", self.digest.as_str()),
            ("Structural observations", self.patterns.as_str()),
            (
                "What the literature says about the candidates",
                self.grounding.as_str(),
            ),
            ("Line of attack chosen", self.chosen.as_str()),
        ]
    }
}

/// What a node hands back to the loop.
///
/// See the module documentation: the two variants exist because a node on the
/// sequential path owns the whole state, and an arm running beside two others
/// owns only its own slot.
#[derive(Clone, Debug)]
pub(super) enum LoopUpdate {
    /// The whole next state, from a node nothing is running beside.
    ///
    /// Boxed because [`SolutionState`] is much the larger variant, and an
    /// unboxed enum costs every arm's small update the size of a whole state.
    Whole(Box<SolutionState>),
    /// One arm's findings, merged by slot.
    Findings(Vec<Finding>),
}

impl LoopUpdate {
    /// Wraps a whole state.
    pub(super) fn whole(state: SolutionState) -> Self {
        Self::Whole(Box::new(state))
    }

    /// Wraps one arm's findings as a node result.
    pub(super) fn findings(findings: Vec<Finding>) -> NodeResult<Self> {
        NodeResult::Update(Self::Findings(findings))
    }
}

/// Folds one node's update into the run's state.
///
/// Total and order-independent for the concurrent case, which is the property
/// the fan-out rests on: findings are written to disjoint slots, so merging
/// two arms in either order gives the same state, and the runtime is free to
/// commit them as they arrive.
pub(super) fn reduce(mut state: SolutionState, update: LoopUpdate) -> GraphResult<SolutionState> {
    match update {
        LoopUpdate::Whole(next) => Ok(*next),
        LoopUpdate::Findings(findings) => {
            for finding in findings {
                state.diversify.set(finding);
            }
            Ok(state)
        }
    }
}

/// Fans out to every arm at once.
///
/// A plain edge cannot express this — the builder holds one static successor
/// per node — so the fan-out is a [`Command`], and the builder is told the
/// destination set separately with `with_unconditional_fanout`. Declaring it
/// as *unconditional* is what lets the barrier downstream reason about which
/// predecessors are really coming: a node that chose between arms would leave
/// the merge waiting on one that never runs.
pub(super) fn fan_out_to_arms() -> NodeResult<LoopUpdate> {
    NodeResult::Command(Command::goto(DIVERSIFY_ARMS))
}
