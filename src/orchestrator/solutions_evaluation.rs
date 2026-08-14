// Post-attempt evaluation: five arms asked at once, and how their answers fold.
//
// The loop used to ask its questions in a line — judge, then reflect, and
// inside the reflection a pattern drain, a literature rescue, and a
// line-of-attack search smuggled in as side effects. That made the reflection
// the place every other role was hidden, and it made a pass cost the sum of all
// of them.
//
// They are five nodes now, fanning out from the attempt and converging here.
// None of them reads another's output — each reads the same attempt — which is
// what makes them concurrent, and a pass costs the slowest arm rather than the
// sum.
//
// # What makes the fold safe
//
// Every arm is handed the same base state and returns a whole state, so the
// merge sees the base plus N near-copies of it and has to decide what each arm
// actually changed. Three rules, and between them they need no list of which
// arm owns which field — a list is exactly what would drift the first time an
// arm learned to write somewhere new:
//
// - **Counters fold by delta.** Each arm's value minus the base, all summed
//   onto the base. This is what makes a reset and an increment compose: the
//   reflection zeroes `unproductive` on a productive attempt (delta −3) while
//   the judge adds one for a restart (delta +1), and the result is 1 rather
//   than whichever arm was folded last.
// - **Lists fold by what was appended.** Everything past the base's length,
//   in arm order.
// - **Text and flags fold by difference.** An arm whose value differs from the
//   base is the arm that wrote it. Two arms differing on one field is a
//   collision the fold cannot resolve, and `no_two_arms_write_the_same_field`
//   is the test that says so rather than leaving it to be discovered live.
//
// The findings are the exception, and they were solved first: they are named
// slots, and `DiversifyFindings::absorb` skips empty ones, so arms writing
// disjoint slots merge in any order.
//
// Arms arrive in whatever order the engine finished them, so they are sorted by
// the tag each one stamps before anything is read. Nothing here should depend
// on that order — the rules above are order-independent — but "should" is not a
// property, and a sort is one line.

/// The field each evaluation arm stamps itself with.
///
/// Present so the fold can order the arms deterministically before reading
/// them, and so a trace names which arm produced which state. It is stripped
/// before the merged state goes back to the loop: the accumulator is what the
/// routing ladder reads, and a field that means "which arm am I" has no meaning
/// once the arms have merged.
pub(in crate::orchestrator) const ARM_FIELD: &str = "eval_arm";

/// Folds every evaluation arm's state onto the base the arms were handed.
pub(in crate::orchestrator) fn fold_evaluation(
    base: &serde_json::Value,
    arms: &[serde_json::Value],
) -> serde_json::Value {
    let Some(base_map) = base.as_object() else {
        return base.clone();
    };
    let mut sorted: Vec<&serde_json::Value> = arms.iter().collect();
    sorted.sort_by_key(|arm| {
        arm.get(ARM_FIELD)
            .and_then(serde_json::Value::as_str)
            .unwrap_or_default()
            .to_string()
    });

    let mut merged = base_map.clone();
    for (key, base_value) in base_map {
        if key == ARM_FIELD {
            continue;
        }
        let incoming: Vec<&serde_json::Value> =
            sorted.iter().filter_map(|arm| arm.get(key)).collect();
        if let Some(folded) = fold_field(base_value, &incoming) {
            merged.insert(key.clone(), folded);
        }
    }
    merged.remove(ARM_FIELD);
    serde_json::Value::Object(merged)
}

/// Folds one field, or leaves it alone when no arm touched it.
fn fold_field(
    base: &serde_json::Value,
    incoming: &[&serde_json::Value],
) -> Option<serde_json::Value> {
    match base {
        serde_json::Value::Number(_) => fold_counter(base, incoming),
        serde_json::Value::Array(base_items) => fold_list(base_items, incoming),
        serde_json::Value::Object(_) => fold_findings(base, incoming),
        _ => incoming
            .iter()
            .find(|value| **value != base)
            .map(|value| (*value).clone()),
    }
}

/// Sums each arm's change to a counter.
///
/// Signed intermediates, because a reset is a large negative delta and the sum
/// has to be able to represent it before it is clamped back into a count.
fn fold_counter(
    base: &serde_json::Value,
    incoming: &[&serde_json::Value],
) -> Option<serde_json::Value> {
    let start = base.as_i64()?;
    let mut total = start;
    for value in incoming {
        if let Some(value) = value.as_i64() {
            total += value - start;
        }
    }
    Some(serde_json::json!(total.max(0)))
}

/// Keeps everything each arm appended, in arm order.
fn fold_list(
    base_items: &[serde_json::Value],
    incoming: &[&serde_json::Value],
) -> Option<serde_json::Value> {
    let mut items = base_items.to_vec();
    for value in incoming {
        let Some(arm_items) = value.as_array() else {
            continue;
        };
        if arm_items.len() > base_items.len() {
            items.extend_from_slice(&arm_items[base_items.len()..]);
        }
    }
    Some(serde_json::Value::Array(items))
}

/// Absorbs every arm's filled slots, which is the one fold that was already
/// order-independent by construction.
fn fold_findings(
    base: &serde_json::Value,
    incoming: &[&serde_json::Value],
) -> Option<serde_json::Value> {
    let mut findings = DiversifyFindings::from_json(base);
    for value in incoming {
        findings.absorb(&DiversifyFindings::from_json(value));
    }
    Some(findings.to_json())
}

/// Establishes what the run already has, once, before the first attempt.
///
/// The curator is the role that reads a workspace for a living. Asking it here
/// means the first attempt is handed what the run has established rather than
/// having to go and find out, and it means the finding is written down once
/// instead of rediscovered by every role that follows.
pub(in crate::orchestrator) async fn curate_context(
    subagents: &AsyncSubagentManager,
    state: &SolutionState,
) -> String {
    delegate(
        subagents,
        "context_curator",
        format!(
            "Establish what this investigation already has, before it attempts anything. Read \
             the workspace: the goal, the research tree, the claim ledger, the code and its \
             captured output, and whatever an earlier run left behind. Report what is already \
             established and cited, what is asserted but unverified, what has been tried and \
             failed, and what the obvious next unresolved thing is. Be specific — name files, \
             claim ids, and numbers. If the workspace is empty, say so in one line rather than \
             describing the problem back.\n\nProblem:\n{}",
            state.problem
        ),
    )
    .await
}

/// Turns the merged findings into the briefing the next attempt reads.
///
/// Replaces `fresh_context` rather than accumulating onto it. Every arm here
/// runs on every pass, so what they produced last time has already been read by
/// the attempt this one is evaluating; carrying it forward would grow the
/// briefing without bound and bury this cycle's findings under every earlier
/// cycle's. `diversify_merge` does carry forward, and should: it runs once, on
/// a state that is about to be attempted again without a fresh evaluation.
pub(in crate::orchestrator) fn evaluation_merge(mut state: SolutionState) -> SolutionState {
    state.fresh_context = merge_context(&state.diversify.sections());
    state.diversify = DiversifyFindings::default();
    state
}
