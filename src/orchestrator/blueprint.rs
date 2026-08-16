//! The statement graph: what rests on what, and what can be picked up now.
//!
//! `research/BACKWARD.md` lists decompositions and `research/CLAIMS.md` lists
//! established statements, and between them they hold every edge this file
//! draws. What neither holds is the *graph*. A skeleton names the gaps it needs
//! and the claims it rests on; a gap is discharged by a claim or by another
//! skeleton proving it outright. Those are dependency edges, and read one file
//! at a time they are invisible — which costs the run three specific things.
//!
//! The first is what Massot's blueprint bought the Polynomial Freiman–Ruzsa
//! formalisation: a node whose dependencies are all settled can be worked on
//! by somebody who has not read the rest of the argument. Roughly twenty-five
//! contributors formalised PFR in three weeks that way, with the author writing
//! about five per cent of the Lean, and the thing that made it divisible was a
//! DAG with a status on every node rather than a document to be read in order.
//! This runtime has the same shape available to it — the detached sub-agents
//! are already concurrent — and no way to say which lemma is safe to hand one.
//!
//! The second is circularity. Nothing here notices when skeleton `A` needs a
//! lemma that skeleton `B` proves from `A`. Read as two files it looks like two
//! reductions; followed as edges it is a cycle, and a cycle proves nothing at
//! all. A flat ledger cannot detect this in principle, because the fault is not
//! in any one row.
//!
//! The third is the difference between *blocked* and *ready*, which is what a
//! planning role most needs and the open-gap list flattens. Every open gap
//! looks equally attackable there. Here a gap resting on a lemma nobody has
//! proved is separated from one resting on nothing, and the second is where the
//! next attempt should go.
//!
//! Derived, like every other ledger: no role writes this file, and no new role
//! was added to produce it. It is the graph that was already implied by the
//! skeletons on disk, computed rather than restated.

use std::collections::{BTreeMap, BTreeSet};
use std::fmt::Write as _;
use std::path::Path;

use super::backward::{GapStance, Skeletons, Stance};
use super::claims::{Ledger, Status};
use super::ledger::budget;
use super::text::truncate;

/// The derived graph, filed with the ledgers it is computed from.
pub(super) const BLUEPRINT_PATH: &str = "derived/BLUEPRINT.md";

/// Nodes one section lists before it is summarised.
const MAX_ROWS: usize = 40;

/// Verification targets one briefing names.
///
/// Three rather than forty, and the difference in kind is the point. The ready
/// list is a menu a planning role chooses from; this is a queue something acts
/// on, one entry per pass. A queue nobody can get to the end of is a list, and
/// the ranking below is what makes the first three the right three.
const MAX_TARGETS: usize = 3;

/// Characters one rendered statement is held to.
const FIELD_CHARS: usize = 140;

/// Where one node of the argument stands.
///
/// Ordered weakest-last so a node's standing is the minimum over its
/// dependencies, which is the whole arithmetic of a blueprint: a proposition is
/// only as established as the least established thing it rests on.
#[derive(Clone, Copy, Debug, Default, PartialEq, Eq, PartialOrd, Ord)]
pub(super) enum Standing {
    /// The Lean kernel checked it in this workspace.
    Verified,
    /// Established without a kernel check — proved in a source, or numerically
    /// checked here, or discharged by a claim of that strength.
    Established,
    /// Open, and every dependency is settled. Somebody can start on this today
    /// without reading the rest of the argument.
    Ready,
    /// Open, and something it rests on is not settled yet.
    #[default]
    Blocked,
    /// False, or resting on something false.
    Refuted,
    /// Its skeleton was spent or broken, so proving it buys the run nothing.
    Abandoned,
}

impl Standing {
    fn label(self) -> &'static str {
        match self {
            Self::Verified => "**verified**",
            Self::Established => "established",
            Self::Ready => "**ready**",
            Self::Blocked => "blocked",
            Self::Refuted => "refuted",
            Self::Abandoned => "abandoned",
        }
    }

    /// Whether a dependent may treat this node as done.
    ///
    /// `Refuted` is deliberately not settled in the permissive direction: a
    /// node resting on a refuted lemma is not ready, it is broken, and the
    /// propagation below is what turns the second into the first.
    fn is_settled(self) -> bool {
        matches!(self, Self::Verified | Self::Established)
    }
}

/// What kind of thing a node is, which decides where a reader goes to work it.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
enum Kind {
    /// A skeleton's goal — the proposition that decomposition proves.
    Goal,
    /// A lemma one skeleton needs.
    Lemma,
    /// A statement the claim ledger carries.
    Claim,
}

impl Kind {
    fn label(self) -> &'static str {
        match self {
            Self::Goal => "goal",
            Self::Lemma => "lemma",
            Self::Claim => "claim",
        }
    }
}

/// One proposition in the argument, with what it rests on.
#[derive(Clone, Debug)]
struct Node {
    /// The key other nodes name it by.
    id: String,
    kind: Kind,
    /// The mathematics, for a reader deciding whether to pick it up.
    statement: String,
    /// The file to open to work on it.
    home: String,
    /// The ids this node needs settled.
    needs: Vec<String>,
    /// Where it stands, before propagation.
    standing: Standing,
}

/// One node worth handing to the kernel, and why it is worth it.
///
/// Ranked rather than listed, because a runtime that formalised everything
/// would formalise nothing: Mathlib elaboration is the most expensive thing
/// this image can run, and the budget buys a handful of checks per run. Which
/// handful is therefore the whole decision, and [`Blueprint::targets`] makes it
/// from the graph instead of from whichever statement a role found interesting.
#[derive(Clone, Debug, PartialEq, Eq)]
pub(super) struct Target {
    /// The node key, which is also how its Lean source is named.
    pub(super) id: String,
    /// The mathematics to state in Lean.
    pub(super) statement: String,
    /// The file the statement is written down in today.
    pub(super) home: String,
    /// How many nodes rest directly on this one.
    pub(super) load: usize,
    /// Whether the run is already building on it.
    ///
    /// The distinction Scholze's criterion turns on. A node the run treats as
    /// settled is being used as a black box, so a mistake in it is invisible
    /// until something above it fails — and nothing above it will fail, because
    /// everything above it is being built on the same belief. An open node is a
    /// different job: it has to be *proved* before it can be checked, and the
    /// kernel is an expensive way to discover that nobody has proved it yet.
    pub(super) established: bool,
}

/// The whole statement graph, with the faults found building it.
#[derive(Debug, Default)]
pub(super) struct Blueprint {
    nodes: BTreeMap<String, Node>,
    /// Dependency ids naming nothing on disk.
    dangling: Vec<(String, String)>,
    /// Cycles, each rendered as the ids in the order they close.
    cycles: Vec<Vec<String>>,
}

/// The key a gap is addressed by across skeletons.
///
/// Qualified by its skeleton rather than bare, because two decompositions may
/// each call a lemma `main-bound` and mean different statements. The gap id
/// alone is still resolvable — [`Blueprint::resolve_edges`] falls back to it —
/// so a skeleton may name a sibling's lemma without knowing which file it
/// lives in.
fn gap_key(skeleton: &str, gap: &str) -> String {
    format!("{skeleton}/{gap}")
}

/// Reads a claim's status as a standing.
fn claim_standing(status: Status) -> Standing {
    match status {
        Status::Formalised => Standing::Verified,
        Status::Proved | Status::Checked => Standing::Established,
        // Asserted, heuristic and catalogued are all reasons to believe rather
        // than establishments, and a blueprint that treated them as settled
        // would report a proof complete when its foundation is a sentence.
        // `Blocked` rather than a status of its own: what a reader needs to
        // know is that something still has to happen here.
        Status::Asserted | Status::Heuristic | Status::Catalogued => Standing::Blocked,
    }
}

/// Every id anything on disk could legitimately be named by.
///
/// Built before any node is, because the edges point in both directions
/// through the file order: a skeleton's gap may be proved by a skeleton later
/// in the directory, and a gap may be discharged by a claim in a note nobody
/// has walked yet. Filtering edges against a set assembled as the nodes are
/// built would make an edge's survival depend on alphabetical order.
fn addressable(skeletons: &Skeletons, ledger: &Ledger) -> BTreeSet<String> {
    let mut known: BTreeSet<String> = ledger.ids();
    for skeleton in skeletons.all() {
        known.insert(skeleton.slug.clone());
        for gap in &skeleton.gaps {
            known.insert(gap.id.clone());
            known.insert(gap_key(&skeleton.slug, &gap.id));
        }
    }
    known
}

/// Builds the graph from the skeletons, the claim library, and what it entails.
///
/// The closure is a third input rather than something read from statuses,
/// because a claim the library *entails* is as good to build on as one somebody
/// proved and its block says otherwise. A graph that read only written statuses
/// would leave a lemma blocked behind a claim the run already holds, and then
/// offer the run its own theorem back as work.
pub(super) fn build(
    skeletons: &Skeletons,
    ledger: &Ledger,
    closure: &super::closure::Closure,
) -> Blueprint {
    let mut blueprint = Blueprint::default();
    let known = addressable(skeletons, ledger);
    // A gap whose id is a skeleton's slug is a lemma that skeleton proves.
    // That edge is what makes this a graph rather than a two-level tree, and
    // it is the only kind that can close a cycle — so it is drawn from the
    // slugs rather than from whatever a role happened to write.
    let slugs: BTreeSet<String> = skeletons
        .all()
        .iter()
        .map(|skeleton| skeleton.slug.clone())
        .collect();
    for claim in ledger.all() {
        if claim.id.is_empty() {
            continue;
        }
        blueprint.nodes.insert(
            claim.id.clone(),
            Node {
                id: claim.id.clone(),
                kind: Kind::Claim,
                statement: claim.statement.clone(),
                home: claim.source.clone(),
                needs: Vec::new(),
                // The stronger of the two readings, never the entailed one
                // outright. A claim the library derives is settled whatever
                // word its own block carries, and dropping the block's word
                // would discard the free upgrade before it reached a planning
                // role — but entailment is an upgrade, and an upgrade that can
                // *lower* a standing is a bug. A `formalised` claim that the
                // library also entails was read as merely established, which
                // sends the kernel back to re-check a lemma it has already
                // accepted and costs the run its scarcest budget on a settled
                // question. `Standing` is ordered strongest-first, so the
                // minimum is the join.
                standing: {
                    let stated = claim_standing(claim.status);
                    if closure.is_covered(&claim.id) {
                        stated.min(Standing::Established)
                    } else {
                        stated
                    }
                },
            },
        );
    }
    for skeleton in skeletons.all() {
        let home = format!("research/backward/{}.md", skeleton.slug);
        let mut needs: Vec<String> = skeleton.rests_on.clone();
        for gap in &skeleton.gaps {
            let key = gap_key(&skeleton.slug, &gap.id);
            needs.push(key.clone());
            let standing = match gap.stance {
                GapStance::Discharged => Standing::Established,
                GapStance::Refuted => Standing::Refuted,
                GapStance::Open if skeleton.stance.is_closed() => Standing::Abandoned,
                GapStance::Open => Standing::Blocked,
            };
            // A gap closed by a claim inherits that claim's standing rather than
            // a flat `established`, which is the join that makes a kernel check
            // reach the goal it was written for. Without it, formalising a
            // lemma would leave the proposition above it looking exactly as it
            // did before.
            let mut node = Node {
                id: key.clone(),
                kind: Kind::Lemma,
                statement: gap.lemma.clone(),
                home: home.clone(),
                needs: Vec::new(),
                standing,
            };
            // A gap is closed by a claim, and it is also closed by another
            // skeleton proving it outright — which is the edge that makes this
            // a graph rather than a two-level tree, and the only one that can
            // close a cycle. `discharged-by` may also name a note path, so
            // both sources are filtered against what is addressable rather
            // than reported as missing.
            for source in super::claims::identifiers(&gap.discharged_by) {
                if source != key && known.contains(&source) {
                    node.needs.push(source);
                }
            }
            if slugs.contains(&gap.id) && gap.id != skeleton.slug {
                node.needs.push(gap.id.clone());
            }
            blueprint.nodes.insert(key, node);
        }
        let standing = match skeleton.stance {
            Stance::Discharged => Standing::Established,
            Stance::Broken => Standing::Refuted,
            Stance::Spent => Standing::Abandoned,
            Stance::Sketched | Stance::Live => Standing::Blocked,
        };
        blueprint.nodes.insert(
            skeleton.slug.clone(),
            Node {
                id: skeleton.slug.clone(),
                kind: Kind::Goal,
                statement: skeleton.goal.clone(),
                home,
                needs,
                standing,
            },
        );
    }
    blueprint.resolve_edges();
    blueprint.find_cycles();
    blueprint.propagate();
    blueprint
}

impl Blueprint {
    /// Rewrites every dependency to a key the graph holds, recording the rest.
    ///
    /// A gap may be named by its qualified key, by its bare id, or by the slug
    /// of the skeleton that proves it, and all three are things a role writes.
    /// Resolving them here rather than at each read means the cycle search and
    /// the propagation below both walk one kind of edge.
    fn resolve_edges(&mut self) {
        let bare: BTreeMap<String, String> = self
            .nodes
            .keys()
            .filter_map(|key| {
                key.split_once('/')
                    .map(|(_, gap)| (gap.to_string(), key.clone()))
            })
            .collect();
        let known: BTreeSet<String> = self.nodes.keys().cloned().collect();
        let mut dangling = Vec::new();
        for node in self.nodes.values_mut() {
            let mut resolved = Vec::new();
            for need in std::mem::take(&mut node.needs) {
                if known.contains(&need) {
                    resolved.push(need);
                } else if let Some(key) = bare.get(&need) {
                    resolved.push(key.clone());
                } else {
                    dangling.push((node.id.clone(), need));
                }
            }
            resolved.sort();
            resolved.dedup();
            // A node may not depend on itself. This is a one-node cycle and the
            // search below would find it, but reporting it as a cycle tells a
            // reader less than dropping it does: it is nearly always a gap
            // whose id repeats its skeleton's slug.
            resolved.retain(|need| need != &node.id);
            node.needs = resolved;
        }
        self.dangling = dangling;
    }

    /// Finds every dependency cycle, by depth-first search over the edges.
    ///
    /// Reported rather than repaired. Which of the edges in a cycle is the
    /// wrong one is a mathematical question — one of the two reductions is
    /// unsound, or one is stating a lemma it should be assuming — and a
    /// runtime that guessed would delete the record of the real fault.
    fn find_cycles(&mut self) {
        let mut done: BTreeSet<String> = BTreeSet::new();
        let mut cycles = Vec::new();
        for start in self.nodes.keys() {
            if done.contains(start) {
                continue;
            }
            let mut stack = vec![(start.clone(), 0usize)];
            let mut on_path: Vec<String> = vec![start.clone()];
            while let Some((id, index)) = stack.pop() {
                let needs = self.nodes.get(&id).map(|node| node.needs.clone());
                let Some(needs) = needs else { continue };
                if index >= needs.len() {
                    done.insert(id.clone());
                    on_path.pop();
                    continue;
                }
                stack.push((id.clone(), index + 1));
                let next = needs[index].clone();
                if let Some(at) = on_path.iter().position(|seen| seen == &next) {
                    let mut cycle = on_path[at..].to_vec();
                    cycle.push(next);
                    cycles.push(cycle);
                } else if !done.contains(&next) {
                    on_path.push(next.clone());
                    stack.push((next, 0));
                }
            }
        }
        // A cycle is found once per entry point into it, so the same loop
        // arrives several times under different rotations. Normalising to the
        // sorted id set is what makes the report say "one cycle" when there is
        // one.
        let mut seen = BTreeSet::new();
        cycles.retain(|cycle| {
            let key: BTreeSet<&String> = cycle.iter().collect();
            seen.insert(key.into_iter().cloned().collect::<Vec<_>>())
        });
        self.cycles = cycles;
    }

    /// Settles every node against what it rests on, to a fixed point.
    ///
    /// Two directions, and both matter. A blocked node whose dependencies are
    /// all settled becomes `Ready`, which is the section a planning role reads.
    /// A node resting on something refuted or abandoned takes that standing
    /// itself, which is how a broken lemma reaches the goal above it rather
    /// than sitting in one file while the goal still reads as live.
    ///
    /// Iterated rather than computed in topological order, because the graph is
    /// not guaranteed acyclic — detecting that it is not is half of what this
    /// file is for. The bound is the node count: each pass either changes
    /// something or is the last one.
    fn propagate(&mut self) {
        let count = self.nodes.len();
        for _ in 0..=count {
            let mut changed = false;
            let snapshot: BTreeMap<String, Standing> = self
                .nodes
                .iter()
                .map(|(id, node)| (id.clone(), node.standing))
                .collect();
            for node in self.nodes.values_mut() {
                if node.standing.is_settled() {
                    continue;
                }
                let mut standing = if node.standing == Standing::Blocked {
                    Standing::Ready
                } else {
                    node.standing
                };
                for need in &node.needs {
                    let Some(dependency) = snapshot.get(need) else {
                        continue;
                    };
                    standing = match dependency {
                        Standing::Refuted => Standing::Refuted,
                        Standing::Abandoned if standing != Standing::Refuted => Standing::Abandoned,
                        Standing::Blocked | Standing::Ready if standing == Standing::Ready => {
                            Standing::Blocked
                        }
                        _ => standing,
                    };
                }
                if standing != node.standing {
                    node.standing = standing;
                    changed = true;
                }
            }
            if !changed {
                break;
            }
        }
    }

    /// The nodes anybody could start on right now.
    ///
    /// The reason this file exists. Ordered by kind so a lemma comes before the
    /// goal it feeds, which is the order somebody picking work up wants.
    fn ready(&self) -> Vec<&Node> {
        let mut ready: Vec<&Node> = self
            .nodes
            .values()
            .filter(|node| node.standing == Standing::Ready && node.kind != Kind::Claim)
            .collect();
        ready.sort_by_key(|node| (node.kind == Kind::Goal, node.id.clone()));
        ready
    }

    /// How many nodes rest directly on `id`.
    ///
    /// Direct rather than transitive, and that is the reading of the criterion
    /// rather than an approximation of it. What makes an unchecked lemma
    /// dangerous is being *used as a black box* — cited by name, its proof not
    /// re-read — and a node is used as a black box by its immediate dependants.
    /// A transitive count would rank a leaf under a long chain above a lemma
    /// six separate arguments cite, which inverts the thing being measured.
    fn load(&self, id: &str) -> usize {
        self.nodes
            .values()
            .filter(|node| node.needs.iter().any(|need| need == id))
            .count()
    }

    /// The nodes a kernel check would buy the most, best first.
    ///
    /// Scholze states the criterion and is his own evidence for it: a proof
    /// used as a black box is one whose mistake stays uncaught, and his
    /// weight-monodromy argument "passed judgment of top mathematicians, but
    /// then it turned out to contain a fatal mistake". Perelman prices the
    /// absence of the check at five years and three independent teams.
    ///
    /// Three keys, in this order, and the order was settled by running the
    /// wrong one against a live workspace:
    ///
    /// 1. **Load, descending.** How much of the argument a mistake takes with
    ///    it. This is the criterion, so it is the first key.
    /// 2. **Established before ready.** Within one load, the node the run is
    ///    already building on is the one whose mistake is compounding now; an
    ///    open one has to be proved before a kernel can check it at all.
    /// 3. **Id.** So two equal targets order the same way on every derivation,
    ///    which is what lets a caller treat the list as a queue.
    ///
    /// The first two were the other way round to begin with, on the reading
    /// that "already building on it" *is* the black-box condition. Against the
    /// `hypercube-induced-degree` workspace that ordering put ten load-0 nodes
    /// at the head of the queue, alphabetically, and the kernel's first job
    /// would have been a note recording that a transcription in the library is
    /// wrong. A node nothing rests on is used as a black box by nothing, so it
    /// cannot outrank one three arguments cite: being established is what makes
    /// a load dangerous, not a substitute for having one.
    ///
    /// A goal node carries load 0 — nothing rests on the top of a DAG — and is
    /// deliberately not special-cased. It is `Blocked` while any lemma under it
    /// is open, so it is not a candidate until the argument beneath it is
    /// settled, which is exactly when it should be the target and when the
    /// queue above it has drained anyway.
    ///
    /// `Verified` is absent because the kernel has already spoken. `Blocked`,
    /// `Refuted` and `Abandoned` are absent for the same reason in three
    /// different keys: there is nothing here a check could establish. A blocked
    /// node cannot be proved before the thing under it is, a refuted one is
    /// false, and an abandoned one buys the run nothing when proved.
    pub(super) fn targets(&self) -> Vec<Target> {
        let mut targets: Vec<Target> = self
            .nodes
            .values()
            .filter(|node| matches!(node.standing, Standing::Established | Standing::Ready))
            .map(|node| Target {
                id: node.id.clone(),
                statement: node.statement.clone(),
                home: node.home.clone(),
                load: self.load(&node.id),
                established: node.standing == Standing::Established,
            })
            .collect();
        targets.sort_by(|left, right| {
            right
                .load
                .cmp(&left.load)
                .then(right.established.cmp(&left.established))
                .then(left.id.cmp(&right.id))
        });
        targets
    }

    /// How many nodes stand at each level, for the judge's evidence briefing.
    ///
    /// Returned as a tuple rather than a map because the caller wants exactly
    /// these three: what the kernel has, what can be started, and how much of
    /// the argument is waiting on something else.
    pub(super) fn counts(&self) -> (usize, usize, usize) {
        let count = |wanted: Standing| {
            self.nodes
                .values()
                .filter(|node| node.standing == wanted)
                .count()
        };
        (
            count(Standing::Verified),
            self.ready().len(),
            count(Standing::Blocked),
        )
    }

    /// Whether the graph contains a circular argument.
    pub(super) fn is_circular(&self) -> bool {
        !self.cycles.is_empty()
    }

    /// The ready nodes, rendered for the next attempt's prompt.
    ///
    /// Empty when nothing is ready, which is the honest answer: a run whose
    /// every open lemma rests on another open lemma has a decomposition
    /// problem, and a briefing that named an arbitrary blocked node instead
    /// would hide it.
    pub(super) fn briefing(&self) -> String {
        let ready = self.ready();
        if ready.is_empty() && self.cycles.is_empty() {
            return String::new();
        }
        let mut out = String::new();
        if !self.cycles.is_empty() {
            out.push_str(
                "The statement graph is circular, so at least one reduction is proving something \
                 from itself. Fix this before attacking any lemma in the loop:\n",
            );
            for cycle in self.cycles.iter().take(MAX_ROWS) {
                let _ = writeln!(out, "- {}", cycle.join(" → "));
            }
        }
        if !ready.is_empty() {
            out.push_str(
                "\nReady to work on now — every lemma these rest on is already settled, so any one \
                 of them can be attacked without reading the rest of the argument:\n",
            );
            for node in ready.iter().take(MAX_ROWS) {
                let _ = writeln!(
                    out,
                    "- `{}` ({}, in {}): {}",
                    node.id,
                    node.kind.label(),
                    node.home,
                    truncate(&node.statement, FIELD_CHARS)
                );
            }
        }
        out
    }

    /// Renders the derived file.
    pub(super) fn render(&self) -> String {
        let mut out = String::from(
            "# Blueprint — the statement graph\n\n\
             Derived from `research/backward/` and the claim library, and rewritten whenever \
             either moves. Do not edit this file; the next write re-derives it.\n\n\
             `research/BACKWARD.md` lists the decompositions and `research/CLAIMS.md` lists what \
             is established. This file is the graph between them: which proposition rests on \
             which, what that makes each one's standing, and — the section to read first — which \
             lemmas can be picked up right now without reading the rest of the argument.\n\n\
             A node is **ready** when everything it rests on is settled. A node is **blocked** \
             when something it rests on is not. That distinction is the whole point: the open-gap \
             list in `BACKWARD.md` makes every unproved lemma look equally attackable, and most \
             of them are not.\n\n",
        );
        if self.nodes.is_empty() {
            out.push_str(
                "_Nothing to graph yet. Write a skeleton under `research/backward/` and this file \
                 fills in._\n",
            );
            return out;
        }
        self.append_cycles(&mut out);
        self.append_ready(&mut out);
        self.append_targets(&mut out);
        self.append_table(&mut out);
        self.append_dangling(&mut out);
        out
    }

    /// Reports circular reasoning, above everything else.
    ///
    /// First in the file because it invalidates what is below it. A cycle means
    /// some node's standing was computed from itself, so the ready list and the
    /// table are both describing an argument that does not close.
    fn append_cycles(&self, out: &mut String) {
        if self.cycles.is_empty() {
            return;
        }
        out.push_str(
            "## Circular — read this first\n\nEach line below is a chain of dependencies that \
             returns to where it started, which proves nothing. One of the reductions in the loop \
             is stating a lemma it should be assuming, or is unsound. Nothing else in this file \
             can be trusted while a cycle stands.\n\n",
        );
        let (rows, dropped) = budget::listed(&self.cycles, MAX_ROWS, |rows, cycle| {
            let _ = writeln!(rows, "- {}", cycle.join(" → "));
        });
        out.push_str(&rows);
        out.push_str(&budget::elided(dropped, super::backward::BACKWARD_DIR));
        out.push('\n');
    }

    /// Whether any lemma is waiting on something unsettled.
    ///
    /// Separates the two ways the ready list comes back empty. A goal blocked
    /// while every lemma under it is discharged is not the same problem as a
    /// decomposition whose leaves all rest on each other, and the advice for
    /// the two is opposite.
    fn blocked_lemmas(&self) -> bool {
        self.nodes
            .values()
            .any(|node| node.kind == Kind::Lemma && node.standing == Standing::Blocked)
    }

    /// Lists what can be started immediately.
    fn append_ready(&self, out: &mut String) {
        let ready = self.ready();
        if ready.is_empty() {
            out.push_str("## Ready to work on\n\n");
            // Two very different states, and a live run reached the second one
            // inside ninety minutes while the file told it the first. PE 351
            // discharged all three of its lemmas and left only the goal open,
            // waiting on claims nobody had verified — and the empty-list note
            // said the run had a decomposition problem, which was both wrong
            // and the opposite of what to do next. An empty list is honest; a
            // diagnosis attached to it has to be earned.
            out.push_str(if self.blocked_lemmas() {
                "_Nothing is ready: every open lemma rests on another open lemma. That is a \
                 decomposition problem rather than a proving one — the run needs a reduction \
                 whose leaves are attackable, not another attempt at a blocked node._\n\n"
            } else {
                "_Nothing is ready, and no lemma is blocked either: every proposition the \
                 decomposition names is settled, and what remains open is the goal itself. \
                 Check what it rests on — a goal still blocked when its lemmas are all \
                 discharged is resting on something nobody verified, or on an inference the \
                 skeleton never wrote down._\n\n"
            });
            return;
        }
        out.push_str(
            "## Ready to work on\n\nEverything these rest on is settled, so each can be attacked \
             on its own, by a role that has not read the rest of the argument. This is the list \
             to schedule from.\n\n",
        );
        let (rows, dropped) = budget::listed(&ready, MAX_ROWS, |rows, node| {
            let _ = writeln!(
                rows,
                "- `{}` ({}) — {}\n  - open `{}`",
                node.id,
                node.kind.label(),
                cell(&truncate(&node.statement, FIELD_CHARS)),
                node.home
            );
        });
        out.push_str(&rows);
        out.push_str(&budget::elided(dropped, super::backward::BACKWARD_DIR));
        out.push('\n');
    }

    /// Lists what the kernel should be handed next.
    ///
    /// Written into the derived file rather than into [`Self::briefing`], which
    /// is what reaches the next attempt. The attempt's job is the mathematics;
    /// the verification arm reads this queue and acts on it, and an attempt
    /// told to formalise as well would spend a solving budget on a job already
    /// scheduled. What the attempt is told is the *standing*, which is where a
    /// passed check shows up.
    fn append_targets(&self, out: &mut String) {
        let targets = self.targets();
        if targets.is_empty() {
            return;
        }
        out.push_str(
            "## Verify these first\n\nRanked by how much of the argument rests on each, and within \
             one load by whether the run is already building on it. An unchecked lemma three other \
             nodes cite is used as a black box, so a mistake in it stays uncaught and everything \
             above it inherits it — where a node nothing rests on is used by nothing, whatever its \
             standing. This is the queue the verification arm works, one entry per pass.\n\n",
        );
        let listed: Vec<&Target> = targets.iter().take(MAX_TARGETS).collect();
        let (rows, dropped) = budget::listed(&listed, MAX_TARGETS, |rows, target| {
            let _ = writeln!(
                rows,
                "- `{}` — {} node(s) rest on it, {} — {}",
                target.id,
                target.load,
                if target.established {
                    "and the run is already building on it"
                } else {
                    "and it is open, so it has to be proved before it can be checked"
                },
                cell(&truncate(&target.statement, FIELD_CHARS))
            );
        });
        out.push_str(&rows);
        out.push_str(&budget::elided(dropped, BLUEPRINT_PATH));
        if targets.len() > MAX_TARGETS {
            let _ = writeln!(
                out,
                "\n_{} further candidate(s) below these, in the table._",
                targets.len() - MAX_TARGETS
            );
        }
        out.push('\n');
    }

    /// The whole graph, one row per node.
    fn append_table(&self, out: &mut String) {
        out.push_str(
            "## Every node\n\n| Node | Kind | Standing | Rests on | Statement |\n\
             | --- | --- | --- | --- | --- |\n",
        );
        for node in self.nodes.values().take(MAX_ROWS) {
            let rests = if node.needs.is_empty() {
                "—".to_string()
            } else {
                node.needs
                    .iter()
                    .map(|need| format!("`{need}`"))
                    .collect::<Vec<_>>()
                    .join(", ")
            };
            let _ = writeln!(
                out,
                "| `{}` | {} | {} | {} | {} |",
                node.id,
                node.kind.label(),
                node.standing.label(),
                cell(&rests),
                cell(&truncate(&node.statement, FIELD_CHARS))
            );
        }
        if self.nodes.len() > MAX_ROWS {
            let _ = writeln!(
                out,
                "\n_{} further nodes not shown._",
                self.nodes.len() - MAX_ROWS
            );
        }
    }

    /// Lists dependencies naming nothing that exists.
    fn append_dangling(&self, out: &mut String) {
        if self.dangling.is_empty() {
            return;
        }
        out.push_str(
            "\n## Resting on nothing that exists\n\nEach edge below names a lemma or claim no \
             file on disk carries. Either the id is misspelled, or the run is taking something as \
             given that nobody wrote down.\n\n",
        );
        let (rows, dropped) = budget::listed(&self.dangling, MAX_ROWS, |rows, (node, need)| {
            let _ = writeln!(rows, "- `{node}` rests on `{need}`, which does not exist");
        });
        out.push_str(&rows);
        out.push_str(&budget::elided(dropped, super::backward::BACKWARD_DIR));
    }
}

/// Re-derives the graph and rewrites [`BLUEPRINT_PATH`].
///
/// Best effort, like every other derived ledger: a failed refresh must not fail
/// the write that succeeded.
pub(super) async fn refresh(documents: &super::documents::WorkspaceDocuments) {
    let blueprint = collect(documents.root());
    let _ = documents
        .write_runtime(BLUEPRINT_PATH, &blueprint.render())
        .await;
    super::folder_index::record_description(
        documents,
        BLUEPRINT_PATH,
        "Derived: the statement graph — what rests on what, which lemmas are ready to be picked \
         up now, and whether the argument is circular. Rewritten on every skeleton and note \
         write; do not edit.",
    )
    .await;
}

/// Builds the graph from what is on disk.
pub(super) fn collect(workspace: &Path) -> Blueprint {
    let ledger = super::claims::collect(workspace);
    let closure = super::closure::build(&ledger);
    build(&super::backward::collect(workspace), &ledger, &closure)
}

fn cell(text: &str) -> String {
    if text.trim().is_empty() {
        return "—".to_string();
    }
    text.replace('|', "\\|").replace('\n', " ")
}

#[cfg(test)]
#[path = "blueprint_test.rs"]
mod test;
