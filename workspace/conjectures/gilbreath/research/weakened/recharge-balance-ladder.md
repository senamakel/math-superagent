# recharge-balance-ladder

The goal stated in recharge coordinates. By the proved step law and recharge
identity (claim `step-law-theorem-proved`), `b_k = b_1 + Σ_{i<k}(j_i+1) − (k−1)`
for ANY absolute-difference array, where `b_k` is the leading `{0,2}` block
length and `j_i` is the jump of the i-th `(2,4)`-event. For the prime shape
`b_1 = 2`, `b_k ≥ 1 ⟺ A_k(1) ∈ {0,2} ⟺ A_{k+1}(0) = 1`, so Gilbreath's
conjecture is *exactly* the budget inequality below. The whole climb is about
turning the two quantitative difficulties (gap, jump) and the one qualitative
one (determinism) back on one at a time.

```ladder
goal: In the prime Gilbreath triangle (A_0 = primes in order, A_{k+1}(i) = |A_k(i) − A_k(i+1)|), prove Σ_{i<k} (j_i + 1) ≥ k − 2 for every k ≥ 1, where j_i is the jump b_{k+1} − b_k of the i-th (2,4)-regeneration event (edge 2, intruder 4) and the sum runs over events at rows < k. This is exactly Gilbreath's conjecture, because the proved recharge identity b_k = 2 + Σ_{i<k}(j_i+1) − (k−1) makes b_k ≥ 1 (i.e. A_k(1) ∈ {0,2}) equivalent to the inequality, and A_k(1) ∈ {0,2} ⟺ A_{k+1}(0) = 1.
difficulties: infinite-horizon, unbounded-event-gap, zero-jump-stalls, prime-determinism
status: open
```

The four difficulties, named as specific obstructions:

- `infinite-horizon` — the quantifier "for every k ≥ 1" over the infinite
  triangle; a finite check bounds nothing that happens later.
- `unbounded-event-gap` — the row gap `τ_{i+1} − τ_i` between consecutive
  `(2,4)`-events has no known constant bound (measured max 64 among the
  genuine giants at 1e9, but no unconditional bound exists). Every row between
  events is pure linear consumption `−(k−1)` with no recharge.
- `zero-jump-stalls` — an event may have jump `j_i = 0` (`b_{k+1} = b_k`), so it
  contributes only `j_i + 1 = 1` to the budget — exactly one row, unable to
  repay a preceding multi-row gap. Measured: 17 of 60 events at depth 1000 are
  stalls.
- `prime-determinism` — the event stream is a fixed function of the prime gaps,
  with no independence/renewal law to draw a lower bound from. This is the
  ABGS 2011 §9 mod-4 switch-frequency openness (`abgs-2011-s9-mod4-switch-limit-open`)
  in disguise: no unconditional linear lower bound on the switch bit exists.

```rung
id: R-recharge-finite-window
statement: In the prime Gilbreath triangle below 2·10^7 (sieve, W = 1,270,607 primes, exact integer rows), the recharge budget Σ_{i<k}(j_i+1) ≥ k − 2 holds for every k = 2..1000, with total recharge Σ(j_i+1) = 1,270,603 against total consumption 998 (margin 1,269,605). This is the finite-prefix form of the goal in recharge coordinates.
off: infinite-horizon
stance: settled
merge: Restore the ∀k quantifier. The finite fact (claim surplus-renewal-structure-1000; step-law-and-recharge-identity verified 0 failures to depth 800) gives no bound on future event gaps or jumps — a sampled budget is not a law. First move: replace the sampled inequality by a uniform sufficient condition, which is the next rung.
```

```rung
id: R-balance-telescope
statement: For ANY absolute-difference array with b_1 = 2, if (2,4)-events occur at rows τ_1 < τ_2 < … infinitely often, with τ_1 ≤ 2 and each event's jump covering the erosion until the next event (j_i + 1 ≥ τ_{i+1} − τ_i for all i), then Σ_{i<k}(j_i+1) ≥ k − 2 for all k, hence A_k(0) = 1 for all k. Proof by telescoping: for the last event τ_m before k, Σ_{i≤m}(j_i+1) ≥ Σ_{i<m}(τ_{i+1}−τ_i) + (k − τ_m) = k − τ_1 ≥ k − 2.
off: unbounded-event-gap, zero-jump-stalls, prime-determinism
stance: open
merge: This is a one-line corollary of claim step-law-theorem-proved (the recharge identity plus telescoping) — settle it first, it is the bottom of the quantitative half. Then turn zero-jump-stalls back on: the primes violate the hypothesis (17 stalls j=0 cannot cover a following gap > 1), so the next rung is the same budget with jumps allowed to be 0.
```

```rung
id: R-stall-rate-insufficiency
statement: For ANY absolute-difference array with b_1 = 2, if (2,4)-events occur with bounded row gap τ_{i+1} − τ_i ≤ G for some fixed G, then A_k(0) = 1 for all k — i.e. a positive lower bound on event *frequency* alone (jumps arbitrary, stalls allowed) forces survival.
off: unbounded-event-gap, prime-determinism
stance: open
merge: This is the rung expected to bite on zero-jump-stalls. The arithmetic is already against it: a stall contributes exactly 1, so with gaps ≤ G and all jumps 0 one gets Σ(j_i+1) = #{events < k} ≈ k/G < k − 2 for G ≥ 2, forcing b_k → 0. The first move is to exhibit (or prove existence of) one array with gap ≤ G ≥ 2 and bounded jumps that dies; the arithmetic shows any all-stall array with gap ≥ 2 dies, so the refutation reduces to exhibiting a single all-stall array. The finding this rung isolates either way: event frequency is NOT the conjecture — the recharge magnitude (jump sizes paying back more than one row each on average) is.
```

```rung
id: R-window-balance
statement: For ANY absolute-difference array with b_1 = 2, if there is a constant C such that every window between consecutive (2,4)-events is paid back by the preceding jump on average — Σ_{i in window} (j_i+1) ≥ (τ_end − τ_start) for every window — then Σ_{i<k}(j_i+1) ≥ k − 2 for all k, hence A_k(0) = 1 for all k. (The cumulative form of R-balance-telescope that tolerates stalls, since a window with one stall and one large jump can still balance.)
off: unbounded-event-gap, prime-determinism
stance: open
merge: This is the real target: turn zero-jump-stalls back on but keep it satisfied in aggregate rather than event-by-event. It is a theorem about ANY array (determinism still off), provable by telescoping over windows. Once settled, the entire remaining content is showing the prime sequence realizes such a window-balance condition — which is exactly the open supply side. Turn prime-determinism back on next.
```

The top of the ladder, with `unbounded-event-gap`, `zero-jump-stalls`, and
`prime-determinism` all back on, is the goal itself: the deterministic prime
event stream keeps the budget `Σ(j_i+1) ≥ k−2` for all k. That is the named
open content (G-supply `ν₂ ≥ c·n`, reduced to the ABGS-open mod-4 switch
frequency).
