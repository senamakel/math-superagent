# Weakened ladder: the regeneration ladder

The full target reduces (proved, Lean-formalised) to one sentence: **the second
entry of every row lies in {0,2}**, because `2` is the only even prime so every
row has shape `(odd, even, even, ...)` and `|1 − e| = 1` exactly when `e ∈ {0,2}`.

Five named difficulties make that hard. A rung is the goal with a subset of
them switched off; `off` lists exactly which. Bottom rungs that the run has
already established are `settled` — the ladder's floor is the run's own partial
results, reframed as weakened targets. The first `open` rung is where the climb
starts.

**The five difficulties.**

- `infinite-horizon` — the target quantifies over every row k ≥ 1 with no
  finite bound; any finite check is a fact about that depth only.
- `regeneration-rate` — the single open core. A {0,2} block erodes at exactly
  one position per row (settled); the conjecture is exactly that (2,4)-events
  keep arriving fast enough that `Σ_{i<k}(j_i+1) ≥ k−2` forever. Consumption is
  settled, regeneration is not.
- `unbounded-gap-arrangement` — the input is the primes: gaps are unbounded and
  it is their *arrangement* (where the 2s, 4s and large gaps sit), not their
  magnitude, that drives the event stream; gap-magnitude upper bounds provably
  cannot force a block-length lower bound.
- `non-concentration-hypothesis` — every existing regeneration theorem (Chase
  2024, CHT 2026) needs an independence / non-concentration hypothesis on the
  gap sequence; that hypothesis is unverified for the deterministic primes.
- `intruder-coincidence` — regeneration needs edge = 2 **and** intruder = 4 in
  the same row; the interior can only force the edge half, so the joint event
  is uncontrolled.

```ladder
goal: For A_0 = (2,3,5,7,11,13,...) the primes in order and A_{k+1}(i) = |A_k(i) − A_k(i+1)|, prove A_k(0) = 1 for every k ≥ 1 (Gilbreath's conjecture, Proth 1878 / Gilbreath 1958)
difficulties: infinite-horizon, regeneration-rate, unbounded-gap-arrangement, non-concentration-hypothesis, intruder-coincidence
status: open
```

## Rungs, bottom to top

```rung
id: R-finite-depth
statement: For the prime sequence, A_k(0) = 1 for every 1 ≤ k ≤ D. This run checks D = 1000 exactly (sieve 2e7, 1,270,607 primes, first_bad = None); the sourced record is D with G = 635 to π(10^13) (Odlyzko 1993), and Plouffe/Colonna extend to 10^14–1.5·10^15. Finite-depth survival is the goal with the for-all-k quantifier cut off.
off: infinite-horizon
stance: settled
merge: Restore the for-all-k quantifier. The first move is to find a row-to-row invariant that forces the *parity* of A_k(0) for every k — that is the next rung, and its settled status is the floor the climb stands on.
```

```rung
id: R-parity-reduction
statement: For ANY sequence beginning (2, 3, odd, odd, ...) — equivalently any A_1 = (1, even, even, ...) — every row A_k has shape (odd, even, even, ...): A_k(0) is odd for all k, and A_{k+1}(0) = 1 ⟺ A_k(1) ∈ {0,2}. So the whole conjecture is equivalent to "A_k(1) ∈ {0,2} for all k ≥ 1". The weakened target actually settled here is the parity half (leading entry odd forever); the ⟺ is the bridge that turns "odd" into the exact target.
off: regeneration-rate, unbounded-gap-arrangement, non-concentration-hypothesis, intruder-coincidence
stance: settled
merge: Restore magnitude content — distinguish {0,2} from {4,6,...}. First move: prove that a leading {0,2} block is self-propagating (the block lemma), which is how the {0,2} regime is carried forward in time.
```

```rung
id: R-block-erosion
statement: If row k has A_k(1..n) ⊆ {0,2} (a leading {0,2} block of length n), then A_{k+d}(0) = 1 for d = 0..n and A_{k+d}(1..n−d) ⊆ {0,2}: the block protects exactly n+1 rows and erodes at exactly one position per row. Protection constant is 1, not n/2 (the n/2 figure is refuted). This is the whole *consumption* half of the regeneration-rate difficulty, with regeneration not claimed.
off: regeneration-rate, unbounded-gap-arrangement, non-concentration-hypothesis, intruder-coincidence
stance: settled
merge: Restore the *recharge* half of regeneration-rate. First move: prove the step law — b_{k+1} ≥ b_k ⟺ the intruder pair is (2,4), else b_{k+1} = b_k − 1 — which turns "the block erodes" into an exact accounting of when it grows.
```

```rung
id: R-step-law-recharge
statement: For ANY absolute-difference array on nonnegative integers with block length b_k, edge x = A_k(b_k), intruder y = A_k(b_k+1): b_{k+1} ≥ b_k ⟺ (x,y) = (2,4), else b_{k+1} = b_k − 1; hence the recharge identity b_k = b_1 + Σ_{events i<k}(j_i+1) − (k−1). For the prime shape (b_1 = 2) the conjecture is exactly Σ_{events i<k}(j_i+1) ≥ k−2 for all k. A (2,4)-event is the ONLY growth mechanism. This settles the accounting; it does not settle that events keep coming.
off: unbounded-gap-arrangement, non-concentration-hypothesis, intruder-coincidence
stance: settled
merge: Restore the *intruder* half of the event condition. First move: prove the interior cannot hide the edge — that a {0,2} block cannot keep its edge at 0 for its whole erosion life — which removes the fear that a bad interior pattern suppresses regeneration.
```

```rung
id: R-edge-interior
statement: For a leading {0,2} block of halved length n under pure erosion (no (2,4)-event fires), the edge reads 2 at least once in its n erosion reads; the longest edge-0 run is ≤ n−1, sharp, achieved only by the halved patterns [1,0,...,0] and its mirror. The halved edge map is F2-linear and unitriangular, hence invertible: e = 0 ⟺ h = 0. The block's own interior pattern cannot keep the edge at 0 for the block's whole life.
off: intruder-coincidence, unbounded-gap-arrangement, non-concentration-hypothesis
stance: settled
merge: Restore the intruder-4 coincidence. The edge must be 2 *when the intruder is 4*; this lemma controls only the edge half. First move: attack a deterministic class where the intruder is controlled — gaps frozen in {2,4} with the first even gap 2 (next rung), where the intruder dynamics are simple enough to track exactly.
```

```rung
id: R-bounded-gap-4
statement: For every 2-then-odds sequence with all gaps (after the first) ≤ 4, the leading 1 persists forever — the deterministic bounded-gap class at g = 4.
off: unbounded-gap-arrangement
stance: failed
killed-by: Colonna's delete-5 example (2,3,7,11,13,17,...): all gaps after the first are ≤ 4, yet the second entry of row 2 is 4, so the leading 1 dies at row 3. So the bounded-gap class dies at g = 4; Eppstein's construction kills every fixed g.
merge: Killed by Colonna's delete-5 example (2,3,7,11,13,17,...): gaps ≤ 4 yet the second entry of row 2 is 4, so the leading 1 dies at row 3. Eppstein's anti-Gilbreath construction kills every fixed g, so `unbounded-gap-arrangement` bites exactly at g = 4. The surviving route is NOT a wider bounded-gap class but a *frequency/concentration* restriction tolerating rare large gaps (R-carved-gap24 is the narrow-support version, R-random-analogue the independence version).
```

```rung
id: R-carved-gap24
statement: Let A_0 = (2,3,x_1,x_2,...) with every x_i odd, x_1 − 3 = 2, and x_{i+1} − x_i ∈ {2,4} for all i ≥ 1 (gaps after the first all equal 2 or 4). Then A_k(0) = 1 for every k ≥ 1. This is the goal with unbounded, irregularly arranged gaps switched off. It strictly generalises the proved consecutive-odds case (all gaps 2), and it is NOT killed by Eppstein's anti-Gilbreath construction (needs unbounded gap bound) or Colonna's deletion counterexamples (those have a 6 or a missing first-2). Empirical support only: 0 deaths among 48 measured sequences to depth 4000 (event-rate sweep, {2,4} support + first gap 2) — not a proof.
off: unbounded-gap-arrangement, non-concentration-hypothesis
stance: open
merge: Restore unbounded/irregular gaps. First move: understand how a single gap 6 (or 8, ...) inserted into a {2,4} sequence perturbs the (2,4)-event stream, then seek a frequency bound (at most C gaps ≥ 6 per window of length L) under which survival provably persists — that bound is the seed of a deterministic non-concentration condition for the primes.
```

```rung
id: R-random-analogue
statement: (Chase 2024, Math. Ann. 388:2611–2625, arXiv:2005.00530, Thm 1) For f increasing with 2 ≤ f(n), f(M) ≤ (1/100) log log M / log log log M, the random sequence a_1 = 2, a_2 = 3, a_{n+1} = a_n + 2u_n with u_n i.i.d. uniform on {0,...,f(n)−1} is almost surely eventually Gilbreath. This is the goal for a random input with independence granted by fiat — the non-concentration difficulty switched off at the hypothesis level.
off: non-concentration-hypothesis
stance: settled
merge: De-randomise. First move: replace i.i.d. uniformity with a deterministic frequency condition on the prime gap arrangement (the same seed as R-carved-gap24's merge), keeping the growth bound f(n) ≤ (1/100) log log n / log log log n — this is the step from the random analogue to a theorem the primes could actually satisfy.
```

```rung
id: R-full
statement: The full goal: for the primes in order, A_k(0) = 1 for every k ≥ 1, equivalently A_k(1) ∈ {0,2} for every k ≥ 1, equivalently Σ_{events i<k}(j_i+1) ≥ k−2 for all k.
off:
stance: open
merge: n/a — top of the ladder. The ladder is exhausted exactly when this rung is settled; reaching it means the unbounded-gap-arrangement difficulty (the step R-carved-gap24 → primes) has been turned back on and survived.
```
