# Weakened ladder: the excess-height (floor/excess) axis

The run's board already adopted `excess-height-renormalization` as a *reformulation*,
but no ladder has written it down as rungs, and the load-bearing identity has no
claim block yet. This file does both. The coordinate change: for every row k and
every position i ≥ 1, `A_k(i)` is even, so halve it — `h_k(i) = A_k(i)/2` — and
take the *excess over the floor*, `t_k(i) = max(0, h_k(i) − 1)`.

Then the floor `t_k(i) = 0` is exactly `h_k(i) ∈ {0,1}`, i.e. `A_k(i) ∈ {0,2}`
— the `{0,2}` block. The whole conjecture is `t_k(1) = 0` for every k ≥ 1
(`A_k(1) ∈ {0,2} ⟺ A_{k+1}(0) = 1`, proved, `gilbreath-reduces-to-second-in-02`).
The sharp fact this axis exposes: **wherever both parents are off the floor, the
excess field evolves by the *same* absolute-difference operator, minus one and
floored at 0.** The `−1` is the consumption term; the floor is the absorbing
regime; and the fatal value is excess 2 (= unhalved 6 = the spike-6 death).

```ladder
goal: For A_0 = (2,3,5,7,11,13,...) the primes in order and A_{k+1}(i) = |A_k(i) − A_k(i+1)|, prove A_k(0) = 1 for every k ≥ 1 (Gilbreath's conjecture, Proth 1878 / Gilbreath 1958).
difficulties: infinite-horizon, floor-regeneration, excess-noncontraction, floor-crossing, prime-gap-arrangement
status: open
```

What each difficulty names, exactly:

- `infinite-horizon` — the target quantifies over every row k ≥ 1 with no finite
  bound; a finite check is a fact about that depth only.
- `floor-regeneration` — the open core in these coordinates: `t_k(1)` must stay 0
  forever, i.e. the floor (`{0,2}` block) must be re-supplied at position 1 exactly
  as fast as it erodes. This is `regeneration-rate` restated: the excess field must
  never reach column 1.
- `excess-noncontraction` — the excess operator `f(a,b) = max(0, |a−b| − 1)` is NOT
  a contraction; a positive excess blob can persist and slide toward the left edge
  rather than decay. The maximum excess is non-increasing (`czz2011-ducci-2-lipschitz`)
  but nothing forces it to 0. Excess 2 is exactly the fatal spike (unhalved 6).
- `floor-crossing` — the excess identity holds only where *both* parents are off the
  floor (`t ≥ 1`). At the interface between floor and excess (one parent on the
  floor, one off) the two fields couple nonlinearly and the excess is not determined
  by the excess field alone. This is `intruder-coincidence` in these coordinates:
  survival is exactly the coupled floor/excess dynamics at the boundary.
- `prime-gap-arrangement` — the excess field is a deterministic function of the
  prime gap word: unbounded, irregular, no independence hypothesis.

---

```rung
id: R-excess-step-identity
statement: For any nonnegative-integer absolute-difference array, with halved entries h_k(i) = A_k(i)/2 (i ≥ 1) and excess t_k(i) = max(0, h_k(i) − 1): if both parents are off the floor, t_k(i) ≥ 1 and t_k(i+1) ≥ 1, then t_{k+1}(i) = max(0, |t_k(i) − t_k(i+1)| − 1). In words: where the excess field is nonzero, it evolves by the same absolute-difference operator, minus one and floored at 0 — the −1 being the one-position-per-row consumption. Proof in one line: off the floor h = 1 + t, so h_{k+1}(i) = |h_k(i) − h_k(i+1)| = |t_k(i) − t_k(i+1)| and t_{k+1}(i) = max(0, h_{k+1}(i) − 1). The hypothesis "both off the floor" is sharp: h = (0,2) has t = (0,1); the child is h′ = |0−2| = 2, i.e. t′ = 1, while the off-floor formula would give max(0, |0−1| − 1) = 0 — so the identity fails (reads 0 instead of 1) the moment a parent is on the floor.
off: infinite-horizon, floor-regeneration, excess-noncontraction, floor-crossing, prime-gap-arrangement
stance: open
merge: This is the bottom and it is settleable today: formalise the identity in Lean (or file it as a proved claim after the one-line algebra + the (0,2) boundary check). Turning `floor-crossing` back on is the first move up — the next rung is the floor half alone (erosion), where the interface is not needed because only floor entries are considered.
```

```rung
id: R-excess-floor-erosion
statement: If row k has t_k(1..n) = 0 (a floor of length n, i.e. A_k(1..n) ⊆ {0,2}), then t_{k+d}(1) = 0 for d = 0..n and the floor shortens by exactly one position per row: t_{k+d}(1..n−d) = 0. The floor protects exactly n+1 rows; protection constant is 1. This is the block lemma in excess coordinates, and it does not claim the floor is ever re-supplied.
off: floor-regeneration, excess-noncontraction, floor-crossing, prime-gap-arrangement
stance: settled
merge: This is `odlyzko-block-lemma-exact` (proved) restated: consumption is exactly one floor position per row. The −1 in R-excess-step-identity is precisely this erosion. Turning `floor-regeneration` back on is the whole game; the first move up is to make the interface event — the only thing that can grow the floor — exact, which is the step law in these coordinates.
```

```rung
id: R-excess-step-law
statement: For any nonnegative-integer absolute-difference array with floor length b_k ≥ 1, boundary floor bit p_k = h_k(b_k) ∈ {0,1} and boundary excess q_k = t_k(b_k+1): the floor grows, b_{k+1} ≥ b_k, iff (p_k, q_k) = (1, 1) — i.e. unhalved edge 2 and unhalved intruder 4 — and otherwise b_{k+1} = b_k − 1. The recharge identity b_k = b_1 + Σ_{events i<k}(j_i+1) − (k−1) is the same accounting. This is `step-law-theorem-proved` translated into the floor/excess coordinates, and it says the ONLY floor-growth mechanism is the interface state (p,q) = (1,1).
off: floor-regeneration, excess-noncontraction, prime-gap-arrangement
stance: settled
merge: This is one transition, not a rate. It leaves open whether (p,q) = (1,1) recurs — and at which q. The next rung controls the excess side by the only monotone quantity that survives non-contraction: the maximum.
```

```rung
id: R-excess-max-nonincrease
statement: For any nonnegative-integer absolute-difference array, the maximum excess M_k = max_{i≥1} t_k(i) is non-increasing: M_{k+1} ≤ M_k. Proof (all entries, floor included): for nonnegative a,b, WLOG a ≥ b, one has t_child = max(0, a−b−1) ≤ max(0, a−1) = max(t_parent of a, t_parent of b) — if a−b−1 ≤ 0 it is 0; if a−b−1 > 0 then a−1 > b ≥ 0 and a−b−1 ≤ a−1. So every child excess is at most the larger parent excess, and M is monotone. This is the excess-coordinate form of Ducci max non-increase (`czz2011-ducci-2-lipschitz`, "iterates have non-increasing maximum M"), and it is the ONLY monotone quantity that survives `excess-noncontraction` — the operator does not contract, but it cannot raise the ceiling.
off: floor-crossing, floor-regeneration, prime-gap-arrangement
stance: settled
merge: Max non-increase is far short of decay: it keeps excess 2 blobs from growing but does not remove them. The next rung tests the first fixed ceiling above the floor and finds it false — the ladder bites exactly at excess 2.
```

```rung
id: R-excess-height-2-class
statement: For a 2-then-odds triangle with g_1 = 2, if every row has all interior excesses ≤ 2 (equivalently every row entry ∈ {0,2,4,6}), then A_k(0) = 1 for all k.
off: excess-noncontraction, prime-gap-arrangement
stance: failed
killed-by: gaps (2,2,6,2,2,...) — A_0 = (2,3,5,7,13,15,17,19,...), A_1 = (1,2,2,6,2,2,...), A_2 = (1,0,4,4,0,...), A_3 = (1,4,0,4,...), A_4 = (3,4,4,...). In excess coordinates h_1 = (1,1,3,1,1), t_1 = (0,0,2,0,0) (max 2), h_2 = (0,2,2,0), t_2 = (0,1,1,0), h_3 = (2,0,2), t_3 = (1,0,1) — the excess reaches position 1, i.e. A_3(1) = 4 ∉ {0,2}, and A_4(0) = 3. Every interior excess is ≤ 2 throughout, yet the triangle dies at row 4.
reason: Excess 2 is the unhalved value 6, the single-gap spike whose relative value 4 is exactly where `{0,d}` closure (d ≥ 4) becomes fatal: the excess blob slides one column left per row and reaches position 1. This is the same counterexample as `R-spike-6-fatal` and `R-intruder-le-6`, re-derived in excess coordinates. Max non-increase holds (2 → 2 → 1 → 1) but does not save the leading 1.
merge: The fixed-ceiling hierarchy is closed here: any ceiling ≥ 2 admits the spike-6 death, so the climb is NOT to a larger fixed bound on the excess. It is to the ceiling 1 — the next rung — where the only nonzero excess is 1 and the interface state (p,q) = (1,1) is forced to be the sole growth move.
```

```rung
id: R-excess-height-1-class
statement: For a 2-then-odds triangle with g_1 = 2, if every row has all interior excesses ≤ 1 (equivalently every row entry ∈ {0,2,4}), then A_k(0) = 1 for all k. The natural generator is the gaps-⊆{2,4} class (R-carved-gap24), whose row 1 is {2,4}-valued and which keeps the ceiling at 4 by max non-increase; the rung in excess coordinates is the class of all arrays whose floor/excess field stays {0,1}-valued.
off: excess-noncontraction, prime-gap-arrangement
stance: open
merge: This is the rung to attack next after the bottom identity, and it is the same open rung as `recharge-ladder`'s `R-carved-gap24` / `spike-propagation-ladder`'s `R-gaps-24` — empirical support only (0 deaths among 48 measured {2,4} sequences to depth 4000, `event-rate-sweep`), not a proof. In these coordinates the claim is crisp: with excess ≤ 1, the only off-floor value is 1, so the boundary state is either (p,q) = (1,1) — growth — or (0,1)/(1,0) — erosion — and the open content is that the (1,1) state recurs before the floor exhausts. First move: prove (or machine-refute) that a {0,1}-valued excess field with floor length b_k ≥ 1 always exhibits the interface state (1,1) within its b_k-row lifetime; that one lemma settles the rung.
```

```rung
id: R-excess-frequency-budget
statement: Let A_0 be 2-then-odds with g_1 = 2, and suppose the interior excess is ≥ 2 (unhalved intruder ≥ 6) at most C times in any window of L consecutive live rows, for some explicit pair (C,L). Then A_k(0) = 1 for every k ≥ 1. This is the goal with `prime-gap-arrangement` switched off by an explicit sparsity hypothesis on the fatal excess-2 blobs; max non-increase bounds each blob's height and the drain/interface law is what the budget must outlast.
off: prime-gap-arrangement
stance: open
merge: Restore the prime arrangement. First move: measure the excess-≥2 frequency in the depth-1000 prime record — the run already records that after every genuine giant the intruder returns to 4 within ≤ 12 rows (`pattern-finder-no-loworder-plus-surplus`), which is the shape a (C,L) budget needs. The seed is the pair (C,L) under which the interface provably hits (1,1) before the floor exhausts; then check whether the prime excess stream satisfies it. This is the deterministic non-concentration condition in excess coordinates, and it is where the ladder is expected to stall.
```

```rung
id: R-excess-full
statement: The full goal: for the primes in order, A_k(0) = 1 for every k ≥ 1 — equivalently t_k(1) = 0 for every k ≥ 1, equivalently Σ_{events i<k}(j_i+1) ≥ k−2 for all k.
off:
stance: open
merge: n/a — top of the ladder. Reaching it means the excess-≥2 frequency budget has been proved for the prime arrangement with a rate fast enough to keep the floor from ever reaching position 1; that is `floor-regeneration`, the single open core, now turned fully back on.
```

---

## Summary

- **Bottom, settle today:** R-excess-step-identity — the one-line off-floor identity
  `t_{k+1} = max(0, |t_k(i) − t_k(i+1)| − 1)`, sharp at the floor (the (0,2) check).
  Not yet a claim block; formalising/filing it is a one-attempt job.
- **Settled (re-derived in excess coordinates):** R-excess-floor-erosion
  (`odlyzko-block-lemma-exact`), R-excess-step-law (`step-law-theorem-proved`),
  R-excess-max-nonincrease (`czz2011-ducci-2-lipschitz`). The first open rung below
  them is not a new obstacle; it is the known ceiling-1 class.
- **Failed and kept:** R-excess-height-2-class — the single-gap-6 counterexample
  dies at row 4 with all excesses ≤ 2 throughout, so any fixed ceiling ≥ 2 fails.
  The ladder bites exactly at excess 2 (unhalved 6), the sharp form of the
  intruder-≥6 obstruction.
- **Attack next:** R-excess-step-identity (settle today), then R-excess-height-1-class
  (= R-carved-gap24): prove or machine-refute that a {0,1}-valued excess field with
  floor length b_k ≥ 1 always shows the interface state (1,1) within its b_k-row
  lifetime. That single lemma would settle the ceiling-1 class.
- **Difficulty expected to bite:** `floor-crossing` — the coupled floor/excess
  interface where the excess identity stops being valid and where the (edge 2,
  intruder 4) coincidence lives. Behind it, `floor-regeneration` is the same open
  core every other ladder locates; the excess coordinates do not remove it, they
  make its threshold (excess 1 vs 2) and its monotone quantity (the non-increasing
  max) explicit.
