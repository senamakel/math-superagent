# Weakened ladder: the scalar-energy axis (invariant search)

This ladder decomposes Gilbreath along the *invariant / Lyapunov-function* axis —
the deliverable GOAL.md names first ("a proved invariant of the absolute-difference
operator forcing `A_k(1) ∈ {0,2}`") and which the other ladders touch only through
the `excess-height-ladder`'s max non-increase. The object tracked here is the
**excess above the `{0,2}` floor**: with `t_k(i) = max(0, A_k(i) − 2)` (unhalved;
halved it is `max(0, h_k(i) − 1)`), the leading block is exactly the set where
`t_k(i) = 0`, and the conjecture is `t_k(1) = 0` for all k.

The load-bearing distinction this ladder adds over `excess-height-ladder`: **the
maximum** excess is provably non-increasing (settled there, `R-excess-max-nonincrease`),
but the **total** excess and the **adjacent-defect** energy are natural Lyapunov
candidates that *fail*. The failures below are new — the board's hunch (E-potential,
adversarial) is refuted in R2, not merely left open.

```ladder
goal: For A_0 = (2,3,5,7,11,13,...) the primes in order and A_{k+1}(i) = |A_k(i) − A_k(i+1)|, prove A_k(0) = 1 for every k ≥ 1 (Gilbreath's conjecture, Proth 1878 / Gilbreath 1958).
difficulties: infinite-horizon, total-energy-nonmonotone, cancellation-branch, regeneration-rate, non-concentration
status: open
```

What each difficulty names, exactly:

- `infinite-horizon` — the conclusion quantifies over every k ≥ 1; a finite check
  is a fact about that depth only.
- `total-energy-nonmonotone` — the natural scalar Lyapunov candidates are **not**
  non-increasing. Total excess mass `T_k = Σ_i max(0, A_k(i) − 2)` can jump up
  (R1), and the adjacent-defect energy `E_k = Σ_i max(0, |A_k(i) − A_k(i+1)| − 2)`
  can jump up (R2). Only the *maximum* is monotone. This is the specific obstruction
  to any "total mass decays to the floor" proof.
- `cancellation-branch` — `|a − b| = max(a,b) − min(a,b)` has a subtraction branch;
  linear and total-positivity potentials do not survive it (`fwd-diff-identity-refuted`),
  and it is the mechanism behind R1/R2: a spike pattern `(0,d,0,d,…)` merges its
  separated mass into a solid block and *increases* the energy instead of damping it.
- `regeneration-rate` — the `(2,4)`-event arrival rate is unproved; the recharge
  identity `Σ_{i<k}(j_i+1) ≥ k−2` for all k is the whole open core. A monotone
  energy gives consumption only, never recurrence.
- `non-concentration` — the deterministic prime gap sequence carries no independence
  / frequency hypothesis; every proved recurrence theorem is a random analogue
  (Chase 2024, CHT 2026) whose hypotheses are unchecked for the primes.

---

```rung
id: R-floor-absorbing-energy-zero
statement: If a row has A_k(i) ∈ {0,2} for all i ≥ 1 (equivalently total excess T_k = Σ_i max(0, A_k(i) − 2) = 0), then every later row has A_j(i) ∈ {0,2} for all i ≥ 1 and A_j(0) = 1 for all j > k. Zero total excess is an absorbing state: |1 − c| = 1 and a difference of two {0,2} entries is in {0,2}. Claim `closure-0d-double-edge` (proved).
off: infinite-horizon, total-energy-nonmonotone, cancellation-branch, regeneration-rate, non-concentration
stance: settled
merge: This is the bottom and it is settleable today (already settled: `closure-0d-double-edge`, and the corner-closure rung `R-corner-closure` in gap-lipschitz-ladder is the same shape). The zero state being absorbing means the whole difficulty is *reaching* it, which is what the energy rungs above test. First move up: ask whether the energy is a monotone Lyapunov function that forces approach to this state — that is R1.
```

```rung
id: R-excess-total-nonincrease
statement: For ANY nonnegative-integer absolute-difference array, the total excess T_k = Σ_i max(0, A_k(i) − 2) is non-increasing: T_{k+1} ≤ T_k. Equivalently in halved units, Σ_i max(0, h_k(i) − 1) is non-increasing.
off: infinite-horizon, regeneration-rate, non-concentration
stance: failed
killed-by: A = (4,0,4,0) → A' = (4,4,4): T(A) = 2+0+2+0 = 4 but T(A') = 2+2+2 = 6 > 4. In halved units (2,0,2,0) → (2,2,2): Σ max(0,h−1) = 1+0+1+0 = 2 → 1+1+1 = 3. The row is genuine: A is the child of parent (4,0,0,4,4) (|4−0|=4, |0−0|=0, |0−4|=4, |4−4|=0), whose own total excess is 6, so the sequence is 6 → 4 → 6.
reason: Two separated spikes of 4 merge into a run of 4s. The per-entry bound |a−b| ≤ max(a,b) gives only max(0,|a−b|−2) ≤ max(0,a−2) + max(0,b−2), and summing over children hits each parent entry twice, so the naive total bound is 2·T_k, not T_k — and the factor 2 is real, not slack: the spike pattern saturates it. The maximum is monotone (settled, `R-excess-max-nonincrease`); the total is not.
merge: Do not re-propose a plain total-mass potential. The surviving form must down-weight the interior relative to the boundary (so a spike merge deep in the row does not count), or factor out a power of two à la Chamberland's Ducci template. That is R3. Note the counterexample (a,a,c,c)-shape is exactly Chamberland's rigid borderline equality class (`ducci-max-factoring-potential-template`), so the fix is expected to be the max-factoring / weighting treatment, not a better inequality.
```

```rung
id: R-adjacent-defect-energy-nonincrease
statement: The adjacent-defect energy E_k = Σ_i max(0, |A_k(i) − A_k(i+1)| − 2) satisfies E_k = 0 ⟺ row k+1 is wholly {0,2}-valued, and is non-increasing: E_{k+1} ≤ E_k. (This is the adversarial board hunch, stated as a claim to test.)
off: infinite-horizon, regeneration-rate, non-concentration
stance: failed
killed-by: A = (0,0,8,8,16,16) → A' = (0,8,0,8,0): E(A) = 0+6+0+6+0 = 12 but E(A') = 6+6+6+6 = 24 > 12. A is a genuine row: it is the child of parent (0,0,0,8,0,16,0) (|0−0|=0, |0−0|=0, |0−8|=8, |8−0|=8, |0−16|=16, |16−0|=16). Writing d_i = |A_i − A_{i+1}|, E_k = Σ max(0, d_i − 1) (halved) and E_{k+1} = Σ max(0, |d_i − d_{i+1}| − 1), so the claim reduces to: every nonneg d satisfies Σ max(0, |d_i − d_{i+1}| − 1) ≤ Σ max(0, d_i − 1). Counterexample d = (0,4,0,4,0): LHS 12 > RHS 6.
reason: The "zero ⟺ next row all-{0,2}" half is true by definition and remains useful. The monotonicity half is false: the operator is a *sharpening* map, not a smoothing map — an alternating sequence of adjacent-difference magnitudes (0,4,0,4,0) sharpens into solid 4s (4,4,4,4), doubling the defect energy. This is the same cancellation-branch mechanism as R1, and it refutes the board's E-potential hunch.
merge: Do not re-propose E (or any fixed-window local energy built only from adjacent differences) as a Lyapunov function. The energy increases exactly on Chamberland-borderline (a,a,c,c)-type inputs, so the honest next candidate is a *weighted* defect with left-decaying weights, or a max-factored defect. That is R3. First move: check whether the refutation (0,0,8,8,16,16) is already excluded by some natural left-edge hypothesis; if it is reachable from a 2-then-odds top, the hunch is dead unconditionally.
```

```rung
id: R-weighted-excess-potential
statement: There exists a summable weight sequence (w_i)_{i≥1} with w_1 > 0, w_i ≥ 0, and a defect d_i = max(0, A_k(i) − 2) such that the weighted potential P_k = Σ_i w_i · d_i is non-increasing under the row operator: P_{k+1} ≤ P_k for every nonnegative-integer absolute-difference array. (The weights are the correction to R1: mass far from the left edge must count less, so a spike merge deep in the row cannot increase P.)
off: infinite-horizon, regeneration-rate, non-concentration
stance: open
merge: This is the rung to attack next. It is a finite, searchable question: for a truncated window of length L and entries in {0,2,4,…,2M}, the constraint P_{k+1} ≤ P_k for every row is a system of linear inequalities in the unknown weights w_1..w_L; feasibility is a linear program (or UNSAT in a solver). Settle by LP for small (L,M), then either exhibit a witness weight sequence (and Lean-prove the monotonicity) or prove no summable weights work (a genuine negative invariant result). Turning `regeneration-rate` back on is the next difficulty: a monotone P only accounts for consumption; to close the goal it must be shown that P_k *recharges* at (2,4)-events. First move: express the per-row drop ΔP_k = P_{k+1} − P_k as (consumption term) − (recharge term), so P becomes a potential for the proved recharge identity `b_k = b_1 + Σ_{i<k}(j_i+1) − (k−1)`.
```

```rung
id: R-full
statement: The full goal: for the primes in order, A_k(0) = 1 for every k ≥ 1 — equivalently A_k(1) ∈ {0,2} for every k ≥ 1, equivalently Σ_{i<k}(j_i+1) ≥ k−2 for all k.
off:
stance: open
merge: n/a — top of the ladder. Reached exactly when the weighted (or max-factored) potential is proved monotone *and* its recharge at (2,4)-events is proved fast enough to keep the left edge at zero excess; that recharge rate is the `regeneration-rate` difficulty, which no energy argument yet bounds.
```

---

## Summary

- **Settled (bottom):** R-floor-absorbing-energy-zero — zero total excess is absorbing
  (`closure-0d-double-edge`); the whole difficulty is reaching the zero state, never
  leaving it.
- **Failed and kept (new, verified by hand against valid parents):** R-excess-total-nonincrease
  (total excess `Σ max(0, A−2)` jumps 4→6 on `(4,0,4,0)→(4,4,4)`), and
  R-adjacent-defect-energy-nonincrease (the board's E-potential jumps 12→24 on
  `(0,0,8,8,16,16)→(0,8,0,8,0)`). Both fail on the same Chamberland-borderline
  spike-merge pattern; the operator sharpens rather than smooths.
- **Next to attack:** R-weighted-excess-potential — does a left-decaying weighted
  defect (or a max-factored defect) give a monotone invariant? This is a finite LP
  question the forward loop can settle today.
- **Difficulty expected to bite:** `total-energy-nonmonotone`, whose mechanism is
  `cancellation-branch` — the min branch of `|a−b|` merges separated excess mass and
  increases every natural scalar energy, so no *total-mass* Lyapunov function exists;
  only the *maximum* is provably monotone, and maximum-monotonicity is far too weak
  to force `A_k(1) ∈ {0,2}`.
