# Weakened ladder: from a computed record to Gilbreath's conjecture

The full goal is one statement — the second entry of every row of the
prime iterated-absolute-difference triangle lies in `{0,2}`. This ladder
switches off the named difficulties one at a time and climbs back up.
Every settled rung is a true statement the run has already established
(claim IDs cited); the open rungs are the targets the forward loop should
attack next. Expected bite: **regeneration rate**, via the fact that a
single-row boundary value never determines the jump size.

```ladder
goal: For every k >= 1, the first entry of the k-th iterated-absolute-difference row of the prime sequence is 1 — equivalently A_k(1) in {0,2} for all k >= 1.
difficulties: infinite horizon, uncontrolled far entries, intruder-4 timing, prime gap arrangement, regeneration rate
status: open
```

```rung
id: R1-finite-prime-record
statement: In the prime Gilbreath triangle below 1e9, A_k(0)=1 for every row 1 <= k <= 50,847,533: rows 1..247 computed exactly, rows 248..50,847,533 by the proved block lemma from the row-248 all-{0,2} block (claim block-lemma-verification-bound-1e9).
off: infinite horizon, uncontrolled far entries, intruder-4 timing, prime gap arrangement, regeneration rate
stance: settled
merge: Turn infinite horizon back on. The record is a computation plus one protection step, not a proof for all k. The next rung proves the all-k statement for the model situations where the tail is already closed; the mechanism is the one-line closure "a difference of two {0,2} entries is in {0,2}". First move: prove {0,2} is closed under absolute differencing and that (1,c,c,c,...) with c in {0,2} is a fixed shape.
```

```rung
id: R2-consecutive-odds-class
statement: For A_0 = (2, 3, 5, 7, 9, ...) (2 followed by the consecutive odd numbers), A_k(0)=1 for all k >= 1. Row 1 is (1,2,2,2,...), row 2 onward is the corner (1,0,0,...)-shape, and every later leading entry is 1.
off: infinite horizon, uncontrolled far entries, intruder-4 timing, prime gap arrangement, regeneration rate
stance: settled
merge: Turn uncontrolled far entries back on. Consecutive odds reaches the pure corner at row 2, so there is never an intruder past the block. The next rung (R4) is the exact law for a finite block with an arbitrary tail: one position lost per row unless the intruder pair is (2,4). First move: derive b_{k+1} = b_k - 1 for any intruder pair different from (2,4) by a finite case analysis.
```

```rung
id: R3-constant-02-tail-class
statement: If some row of any absolute-difference triangle equals (1, c, c, c, ...) with c in {0,2}, then every later row begins with 1. The all-equal {0,2} tail is a fixed shape under the operator (claim closure-0d-double-edge; the run's proved restricted class).
off: infinite horizon, uncontrolled far entries, intruder-4 timing, prime gap arrangement, regeneration rate
stance: settled
merge: Same reintroduction as R2. The all-equal tail is the degenerate zero-intruder case; the real object is a finite block followed by an intruder that is not forced to be 4. Next rung is R4's exact accounting, which makes the intruder pair the whole story.
```

```rung
id: R4-exact-accounting
statement: For any nonnegative-integer absolute-difference array with leading {0,2} block length b_k and intruder pair (x,y) = (A_k(b_k), A_k(b_k+1)): b_{k+1} >= b_k iff (x,y) = (2,4), else b_{k+1} = b_k - 1; and the recharge identity b_k = b_1 + sum_{events i<k}(j_i+1) - (k-1) holds. Gilbreath is thereby equivalent to sum_{events i<k}(j_i+1) >= k-2 for all k (claim step-law-theorem-proved).
off: prime gap arrangement, regeneration rate
stance: settled
merge: Turn regeneration rate back on. The identity is exact but the event arrival is unproved: the whole open content is whether sum (j_i+1) keeps pace with k-2. The attackable rung just above is R6 (pin the intruder to 4 and ask whether the interior regenerates). First move: express the jump j_i in terms of the continuation past the intruder, using the 1-Lipschitz landing-block characterization.
```

```rung
id: R5-interior-edge-invertibility
statement: Under pure erosion (no regeneration event fires), every nonzero {0,2} block of length n shows edge value 2 at least once in its n erosion reads; the longest run of edge-0 rows is at most n-1, sharp and achieved only by [2,0,...,0] and its mirror (claim edge-interior-invertibility-sharpened).
off: intruder-4 timing, prime gap arrangement, regeneration rate, uncontrolled far entries
stance: settled
merge: Turn intruder-4 timing back on. Edge-2 availability is necessary but an event also needs the intruder value 4, and the library already records that intruder=4 alone is not sufficient (36 erosion rows at depth 1000 have y=4 without regenerating). Next rung is R6, the conditional with y_k = 4 at every live row. First move: search small arrays for a triangle whose intruder is 4 at every live row yet dies — a falsification of R6 would locate the far-entry obstruction precisely.
```

```rung
id: R6-intruder-4-regeneration
statement: If a 2-then-odds absolute-difference triangle has intruder value 4 at every live row (y_k = A_k(b_k+1) = 4 whenever the leading block is interior, b_k+1 < row width), then A_k(0)=1 for all k — the leading block never dies. Pinning y_k=4 does NOT pin A_k(b_k+2), so the jump j_i is still determined by the continuation; this rung still faces the uncontrolled-far-entries difficulty.
off: intruder-4 timing, prime gap arrangement
stance: open
merge: Turn prime gap arrangement back on. R6 is a conditional that says nothing about whether the prime rows actually realize the intruder-4 condition with the needed frequency. Next rung is R7, which keeps the primes and asks only for infinitely-often (a strictly weaker conclusion than the goal's rate). First move: extract the (x,y) pairs and continuation lengths from the depth-1000 event data and measure whether y=4 recurs with positive frequency.
```

```rung
id: R7-primes-events-infinitely-often
statement: For the prime triangle, (2,4)-regeneration events occur infinitely often as k -> infinity. This is strictly weaker than the conjecture (occurrence, not rate) and is the natural first target with the prime gap arrangement switched back on; the random-gap analogue is settled by Chase 2024 / CHT 2026 but the prime arrangement has no such proof.
off: regeneration rate
stance: open
merge: Turn regeneration rate back on. Infinitely-often is necessary but not sufficient: the recharge surplus must never fall k-2 behind, so a rate statement (sum of (j_i+1) growing at least linearly in k) is required. Next rung is the goal itself. First move: model the event sequence as a renewal process and convert any inter-event gap bound into a recharge-surplus lower bound.
```

```rung
id: R8-goal
statement: For every k >= 1, A_k(1) in {0,2} for the prime triangle (equivalently A_k(0)=1) — Gilbreath's conjecture, all difficulties switched on.
off:
stance: open
merge: none — top of ladder.
```
