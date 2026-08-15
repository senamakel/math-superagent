# Ladder: the intruder-magnitude hierarchy

> Complements `recharge-ladder.md` (canonical block-length/recharge axis) and
> `gap-lipschitz-ladder.md` (the gap-jump axis). This ladder climbs a quantity
> neither of them isolates: the **boundary intruder value** `y_k = A_k(b_k+1)`,
> the first non-`{0,2}` entry past the block. The step law makes the whole
> conjecture a statement about the two-variable frontier state `(x_k, y_k)`,
> where `x_k = A_k(b_k) ∈ {0,2}` is the block's edge. The ladder's sharp fact:
> the pinned-intruder class survives *only* at `y ≡ 4`; admitting a single `6`
> already kills it, so the difficulty bites exactly at 6 and the climb to the
> primes is through the *frequency* of intruders ≥ 6, not their magnitude.

```ladder
goal: For A_0 = (2,3,5,7,11,13,...) the primes in order and A_{k+1}(i) = |A_k(i) − A_k(i+1)|, prove A_k(0) = 1 for every k ≥ 1 (Gilbreath's conjecture, Proth 1878 / Gilbreath 1958).
difficulties: infinite-horizon, intruder-ge-6, edge-intruder-coincidence, all-zero-block, prime-gap-arrangement, regeneration-rate
status: open
```

What each difficulty names, exactly:

- `infinite-horizon` — the conclusion quantifies over every row k ≥ 1 with no
  finite bound; a finite check is a fact about that depth only.
- `intruder-ge-6` — at an edge-2 read, intruder `y = 4` regenerates
  (`|2−4| = 2`), but intruder `y ≥ 6` forces erosion (`|2−6| = 4 ∉ {0,2}`).
  The sequence of intruder values `y_k ∈ {4,6,8,...}` is the unproved quantity.
- `edge-intruder-coincidence` — regeneration needs `x = 2` **and** `y = 4` in
  the same row. The interior can force edge-2 at least once per block lifetime
  (`edge-interior-invertibility-sharpened`) but not simultaneously with `y = 4`.
- `all-zero-block` — the block `(1, 0^n, y)` reads edge 0 for its entire life,
  so the drain law is frozen (`y` never falls) and the block dies in n rows.
  Whether this shape is reachable from a 2-then-odds start is the crux of the
  pinned-intruder rungs.
- `prime-gap-arrangement` — after each growth event the intruder is reset to a
  value drawn from the prime gaps: unbounded, irregular, no independence
  hypothesis. It is the *arrangement* of ≥ 6 intruders, not their size.
- `regeneration-rate` — growth events must arrive fast enough that
  `Σ_{i<k}(j_i+1) ≥ k−2` for all k (the recharge identity,
  `step-law-theorem-proved`); consumption is settled, this arrival rate is the
  whole open core.

---

```rung
id: R-frontier-drain-law
statement: For any nonnegative-integer absolute-difference array at a row with block length b_k ≥ 1, edge x_k = A_k(b_k) ∈ {0,2} and intruder y_k = A_k(b_k+1) ∈ {4,6,8,...}: b_{k+1} ≥ b_k ⟺ (x_k, y_k) = (2,4), otherwise b_{k+1} = b_k − 1 and the next frontier is x_{k+1} = |u − x_k| ∈ {0,2} (u = A_k(b_k−1) ∈ {0,2}) and y_{k+1} = |x_k − y_k| = y_k − 2·[x_k = 2]. During erosion y never increases: it is frozen at edge-0 reads and falls by exactly 2 at edge-2 reads.
off: infinite-horizon, intruder-ge-6, edge-intruder-coincidence, all-zero-block, prime-gap-arrangement, regeneration-rate
stance: settled
merge: This is the bottom: the one-row frontier mechanics, already owned as the step law (`step-law-theorem-proved`) plus `{0,2}` closure (`closure-0d-double-edge`) and the drain corollary recorded in the run's notes. Turn `edge-intruder-coincidence` back on by controlling the edge half alone: the next rung is the proved fact that a nonzero block cannot hide its edge.
```

```rung
id: R-nonzero-edge-availability
statement: Under pure erosion (no growth event fires), every NONZERO {0,2} block of length n shows edge value 2 at least once in its n erosion reads; the longest edge-0 run is ≤ n−1, sharp, achieved only by the halved patterns [1,0,...,0] and its mirror. The all-zero block is the sole exception: it reads edge 0 for all n reads.
off: infinite-horizon, intruder-ge-6, prime-gap-arrangement, regeneration-rate
stance: settled
merge: The block's own interior pattern cannot suppress the edge-2 that a growth event needs, but the all-zero block can. Turn `all-zero-block` back on: the next rung pins the intruder to 4 and asks whether the all-zero block is reachable at all. First move: if A_k = (1, 0^n, 4), backward-induct one row — A_{k−1}(1..n+1) must be constant v with |1−v| = 1, so v ∈ {0,2}.
```

```rung
id: R-intruder-4-always
statement: For a 2-then-odds triangle with g_1 = 2, if the block-boundary intruder value is 4 at every row where the leading block is nonempty and finite (y_k = A_k(b_k+1) = 4), then A_k(0) = 1 for all k — the leading block never dies. This is the same rung as `gap-lipschitz-ladder`'s `R-intruder-4-always` / `regeneration-ladder`'s `R6-intruder-4-regeneration`, restated in frontier coordinates.
off: intruder-ge-6, prime-gap-arrangement, regeneration-rate
stance: open
merge: This is the rung to attack next, and a complete candidate proof exists (hand argument, NOT yet oracle-checked — do not mark settled until a program confirms both branches). Assembly: (drain law + edge availability) a nonzero block shows edge 2 at least once per lifetime, and at any edge-2 read the pair is (2,4) by hypothesis, so growth fires; the block dies only if it is ALL-zero at some row. The candidate proof shows all-zero is unreachable: if A_k = (1, 0^n, 4, ...), then A_{k−1}(1..n+1) is constant v, and |1−v| = 1 forces v ∈ {0,2}. Branch v = 2: A_{k−1} = (1, 2^{n+1}, 6, ...) — full block length n+1, intruder 6, violating the intruder≡4 hypothesis. Branch v = 0: A_{k−1} = (1, 0^{n+1}, 4, ...), so the zero block extends back one position per row; inducting to row 1 forces A_1(1) = 0, contradicting g_1 = 2. First move: check this backward induction against the oracle by exhaustive search over small even-gap inputs for any row of shape (1, 0^n, 4, ...) with all prior intruders 4 — UNSAT confirms the lemma and settles the rung; a found row refutes it and the all-zero block is the obstruction.
```

```rung
id: R-intruder-le-6
statement: For a 2-then-odds triangle with g_1 = 2, if the block-boundary intruder value is at most 6 at every live row (y_k ∈ {4,6}), then A_k(0) = 1 for all k — the leading block never dies.
off: prime-gap-arrangement, regeneration-rate
stance: failed
killed-by: gaps (2,2,6,2,2,...) — A_0 = (2,3,5,7,13,15,17,19,...), A_1 = (1,2,2,6,2,2,...) with b_1 = 2 and intruder y_1 = 6; A_2 = (1,0,4,4,0,...) with b_2 = 1 and intruder y_2 = 4; A_3 = (1,4,0,4,...) with b_3 = 0 (A_3(1) = 4 ∉ {0,2}); A_4(0) = |1−4| = 3. Every observed intruder lies in {4,6}, yet the triangle dies at row 4.
reason: The single gap 6 injects a 4 into row 2 (|2−6| = 4). In a {0,2} background that 4 propagates one column left per row until it is the second entry (row 3) and then the leading entry (row 4). It is healed iff a 2 sits immediately to its left (|2−4| = 2); here the left neighbour is 0, so it is not healed. This is the same counterexample as `spike-propagation-ladder`'s `R-spike-6-fatal` and `gap-lipschitz-ladder`'s `R-single-gap-jump-4`, re-stated in intruder coordinates: intruders 6, 4, 4 die.
merge: The pinned-intruder class survives only at y ≡ 4; admitting a single 6 already kills it, and the same spike kills every fixed upper bound M ≥ 6 (intruders 6,4,4 are all ≤ M). So the magnitude hierarchy is closed here — the climb is NOT to larger fixed M. It is to a *frequency* restriction on intruders ≥ 6 (next rung): the question is how sparse the ≥ 6 intruders must be for the drain law to reach 4 and fire a growth event before the block exhausts.
```

```rung
id: R-intruder-frequency-budget
statement: Let A_0 be 2-then-odds with g_1 = 2, and suppose the block-boundary intruder value is ≥ 6 at most C times in any window of L consecutive live rows, for some explicit pair (C, L). Then A_k(0) = 1 for every k ≥ 1. This is the goal with `prime-gap-arrangement` switched off by an explicit sparsity hypothesis on the ≥ 6 intruders; the drain law (frozen at edge 0, −2 at edge 2) is what the budget must outlast.
off: prime-gap-arrangement
stance: open
merge: Restore the prime arrangement. First move: measure the intruder-≥6 frequency in the depth-1000 prime record — the run already records that after every genuine giant the intruder returns to 4 within ≤ 12 rows (`pattern-finder-no-loworder-plus-surplus`), which is exactly the shape a (C, L) budget needs. The seed is a pair (C, L) under which the drain provably reaches 4 at an edge-2 read before exhaustion; then check whether the prime intruder stream satisfies it. This is the deterministic non-concentration condition in frontier coordinates, and it is where the ladder is expected to stall.
```

```rung
id: R-full
statement: The full goal: for the primes in order, A_k(0) = 1 for every k ≥ 1 — equivalently A_k(1) ∈ {0,2} for every k ≥ 1, equivalently Σ_{i<k}(j_i+1) ≥ k−2 for all k.
off:
stance: open
merge: n/a — top of the ladder. Reaching it means the intruder-≥6 frequency budget has been proved for the prime arrangement with a rate fast enough to keep the recharge sum ahead; that is `regeneration-rate`, the single open core, now turned fully back on.
```

---

## Summary

- **Settled floor:** R-frontier-drain-law (`step-law-theorem-proved` + `closure-0d-double-edge`),
  R-nonzero-edge-availability (`edge-interior-invertibility-sharpened`). Both are
  one-row / one-block-lifetime facts already owned by the run, restated in the
  frontier coordinates this ladder is about.
- **Attack next:** R-intruder-4-always — the pinned-intruder-4 conditional. A
  complete candidate proof (backward induction: the all-zero block with intruder 4
  is unreachable) is stated in its `merge` and is one oracle check from settled;
  it is the same open rung the other ladders already flag.
- **Failed and kept:** R-intruder-le-6 — gaps (2,2,6,2,...) has intruders 6,4,4
  and dies at row 4, so the pinned-intruder class survives only at y ≡ 4. The
  counterexample is the established spike-6 death (`R-spike-6-fatal`), restated
  in intruder coordinates, and it kills every fixed upper bound M ≥ 6.
- **Difficulty expected to bite:** `intruder-ge-6` — a single intruder 6 at an
  edge-2 read forces erosion and its diamond reaches the second entry; `prime-gap-arrangement`
  is its input-side form (the primes have infinitely many gaps ≥ 6, hence
  infinitely many intruders ≥ 6), and `regeneration-rate` is the frequency
  statement that turns "sparse enough" into survival.
