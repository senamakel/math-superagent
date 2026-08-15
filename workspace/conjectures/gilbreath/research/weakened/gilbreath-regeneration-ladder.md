# Ladder: the regeneration difficulty in Gilbreath's conjecture

> Superseded by `research/weakened/recharge-ladder.md` (canonical ladder for this
> run; difficulty names `infinite-horizon`, `regeneration-rate`,
> `unbounded-gap-arrangement`, `non-concentration-hypothesis`,
> `intruder-coincidence`). Kept for the failed rung R-bounded-gap-4, which the
> canonical ladder also carries.

```ladder
goal: For every k >= 1 the first entry of A_k is 1, where A_0 = primes and A_{k+1}(i) = |A_k(i) - A_k(i+1)|.
difficulties: unbounded-n, regeneration-rate, intruder-ge-6, non-concentration, unbounded-gaps
status: open
```

What each difficulty names, exactly:

- `unbounded-n` — the row is infinite and the depth is infinite; no finite window of
  row entries decides anything, and every finite-width run has a boundary artifact.
- `regeneration-rate` — the (2,4)-event arrival rate is unproved. GC is exactly
  `sum over events i<k of (j_i + 1) >= k - 2` for all k (step-law-theorem-proved,
  recharge identity); nobody has shown events keep arriving fast enough. This is the
  whole open content.
- `intruder-ge-6` — at the block boundary, an intruder value y >= 6 forces erosion
  even when the edge is 2 (|2-6| = 4 not in {0,2}); only intruder 4 regenerates.
  The sequence of boundary intruder values (4 vs >= 6) is the unproved quantity.
- `non-concentration` — the primes carry no independence / 2-separated hypothesis;
  every proved "regeneration recurs" theorem is a random analogue (Chase 2024, CHT
  2026) whose hypotheses are unchecked for the primes.
- `unbounded-gaps` — the deterministic class "2 then odds with all gaps <= g" is
  false for every g >= 4 (Colonna delete-5: gaps <= 4, second entry 4 at row 2;
  Eppstein for arbitrary unbounded monotone bounds). Only g = 2 (consecutive odds)
  survives.

---

```rung
id: R-base-02-row
statement: If a row is (1, c_1, ..., c_n) with every c_i in {0,2}, then every later
  row of the finite triangle has leading entry 1 (and the {0,2} block persists).
off: regeneration-rate, intruder-ge-6, unbounded-n, unbounded-gaps
stance: settled
merge: This is the bottom. To climb, allow entries > 2 past the block; the first
  move is the block lemma, which says exactly how many rows the block protects
  (R-erosion).
```

```rung
id: R-erosion-block-lemma
statement: If a row begins 1 followed by a leading {0,2} block of length n, then the
  next n rows begin with 1 — protection constant 1, one row per block entry.
off: regeneration-rate, intruder-ge-6, unbounded-n
stance: settled
merge: Erosion alone cannot be enough: the block is consumed at rate exactly 1 and
  nothing replaces the position lost from the left. Turning regeneration-rate back
  on is the whole game; the first move is the step law, which says what the block
  boundary must look like for the block to grow rather than shrink.
```

```rung
id: R-step-law
statement: With b_k the leading {0,2} block length and (x,y) = (row[b_k], row[b_k+1])
  the boundary pair, b_{k+1} >= b_k iff (x,y) = (2,4), else b_{k+1} = b_k - 1; and
  the recharge identity b_k = b_1 + sum over events i<k of (j_i + 1) - (k-1) holds.
off: regeneration-rate, unbounded-n
stance: settled
merge: This is one transition, not a rate. The rung leaves open whether (2,4)-events
  recur infinitely often; the next move is to pin the interior half of that question
  (R-edge-invertibility) and then the boundary half (R-intruder-4).
```

```rung
id: R-edge-invertibility
statement: Under erosion-only dynamics, every nonzero {0,2} block shows edge value 2
  at least once during its n erosion reads; the longest edge-0 run is <= n-1, sharp.
off: regeneration-rate, intruder-ge-6
stance: settled
merge: This says the block's own interior pattern cannot suppress the edge-2 that a
  (2,4)-event needs. It does NOT say the intruder is 4 when the edge reads 2 —
  turning intruder-ge-6 back on is the step that actually bites (R-intruder-4).
```

```rung
id: R-consecutive-odds
statement: If A_0 = (2, 3, 5, 7, 9, 11, ...) — consecutive odds after 2, i.e. every
  gap equal to 2 — then A_1 = (1, 2, 2, 2, ...) and the leading 1 persists forever.
off: regeneration-rate, intruder-ge-6, unbounded-gaps
stance: settled
merge: The block is self-sustaining because the row is all-2 after position 1. The
  first move back up is to let the gaps vary: gaps <= 3 is the same rung (even gaps
  <= 3 means gap 2), and gaps <= 4 is R-bounded-gap-4, which fails.
```

```rung
id: R-bounded-gap-4
statement: For every 2-then-odds sequence with all gaps (after the first) <= 4, the
  leading 1 persists forever.
off: unbounded-gaps
stance: failed
killed-by: Colonna's delete-5 example (2,3,7,11,13,17,...): gaps ≤ 4 yet the second entry of row 2 is 4, so the leading 1 dies at row 3.
merge: Colonna's delete-5 example (2,3,7,11,13,17,...) has gaps <= 4 and second entry
  4 at row 2, killing it. So the deterministic bounded-gap class dies at g = 4, and
  Eppstein's construction kills every fixed g. The difficulty `unbounded-gaps` bites
  exactly at 4; the surviving route is a further restriction (2-separated
  non-concentration, or the primes' specific arrangement), which is R-random-analogue
  and the prime case itself.
```

```rung
id: R-intruder-4
statement: For any 2-then-odds input (all gaps after the first even) whose Gilbreath
  triangle has every block-boundary intruder value equal to 4, the leading 1 persists
  forever.
off: intruder-ge-6
stance: open
merge: This is the rung to attack next. It should fall out of the already-proved
  step law + edge-map invertibility: whenever the edge reads 2 the boundary pair is
  (2,4) by hypothesis, so regeneration fires; the edge cannot stay 0 for a whole
  block lifetime by R-edge-invertibility, so the block never dies. Turning
  intruder-ge-6 back on is the real difficulty: handle the case y = 6 (or larger) at
  an edge-2 read, where |2-6| = 4 forces erosion. That is where the ladder is
  expected to bite.
```

```rung
id: R-random-analogue
statement: If the top row's gaps (normalized) are independent nonnegative integers
  with sublinear growth and no 2-separated concentration, then almost surely the left
  diagonal is eventually {0,1}-valued (hence GC holds a.s.).
off: non-concentration
stance: settled
merge: Proved for the random model (Chase 2024 Thm 1; CHT 2026 Thm 1.3), but the
  hypotheses are unchecked for the primes. The merge move is to drop independence and
  ask which deterministic 2-separation / non-concentration property of the prime gap
  sequence is enough; that is exactly the open prime case and it is not covered by
  any held theorem.
```

---

## Summary

- **Bottom settled:** R-base-02-row, R-erosion-block-lemma, R-step-law,
  R-edge-invertibility, R-consecutive-odds. These are all already proved in the
  library (`odlyzko-block-lemma-exact`, `step-law-theorem-proved`,
  `edge-interior-invertibility-sharpened`, the restricted-class results).
- **Failed and kept:** R-bounded-gap-4 (Colonna delete-5) — the deterministic
  bounded-gap class dies at g = 4.
- **Next to attack:** R-intruder-4 — the conditional theorem that an
  all-intruder-4 triangle regenerates forever. It is assembled from two proved
  pieces and is the last rung before the difficulty that bites.
- **Difficulty expected to bite:** `intruder-ge-6` — specifically the value 6
  appearing at an edge-2 boundary, which forces erosion. It is the concrete form
  of the unproved `regeneration-rate`.
