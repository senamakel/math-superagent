# Ladder: the spike-propagation obstruction

> Complements `research/weakened/gap-lipschitz-ladder.md`, which tracks the same
> obstruction at the input (gap-jump) level. That ladder names the killer value:
> a gap-jump `|g_i − g_{i+1}| = 4` injects a `4` into row 2, and the `4` is healed
> iff a `2` sits immediately to its left. This ladder isolates the *healing* half:
> which input patterns place that `2` next to the injected `4`, and whether the
> `{0,d}`-diamond picture (`closure-0d-double-edge`, d ≥ 4) gives a clean shield law.
> Rung `R-spike-6-fatal` below is the same counterexample as
> `gap-lipschitz-ladder`'s `R-single-gap-jump-4` (gaps `(2,2,6,2,...)`, dead at row
> 4), re-derived independently as a cross-check.

The three accounting/statistical ladders track the step law, the recharge, and
the random analogues. This ladder tracks the one mechanism the accounting does
not: a single gap ≥ 6 in an otherwise constant-2 background is a relative spike
of value `d = gap − 2 ≥ 4`, and `{0,d}` is closed under absolute differencing
(`closure-0d-double-edge`, d ≥ 4), so the spike becomes a solid `{0,d}`-valued
Pascal (Rule 90) diamond advancing one column per row toward the left edge. When
its front reaches the second entry, `|1 − d| ≥ 3` kills the leading 1. The clean
single-gap dichotomy — a lone gap 4 absorbs, a lone gap ≥ 6 kills — is stated and
hand-derived below; the *shield* question (does a gap 4 left of a gap 6 heal the
diamond before it reaches the edge) is the open rung.

```ladder
goal: For A_0 = (2,3,5,7,11,13,...) the primes in order and A_{k+1}(i) = |A_k(i) − A_k(i+1)|, prove A_k(0) = 1 for every k ≥ 1 (Gilbreath's conjecture).
difficulties: infinite-horizon, intruder-ge-6, spike-propagation, gap-arrangement, non-concentration, regeneration-rate
status: open
```

What each difficulty names, exactly:

- `infinite-horizon` — the target quantifies over every row k ≥ 1; every finite
  computation is a fact about that depth only. Kept on in the model rungs because
  the model collapses to a fixed `{0,2}` shape where it is trivially discharged.
- `intruder-ge-6` — at the block boundary, intruder value 4 absorbs (`|2−4|=2`),
  intruder ≥ 6 breaks (`|2−6|=4 ∉ {0,2}`). A class whose rows have maximum ≤ 4
  (by max non-increase, `czz2011-ducci-2-lipschitz`) never sees this difficulty.
- `spike-propagation` — a single gap ≥ 6 in a constant `2`-background is a
  relative spike of value d = gap − 2 ≥ 4; it evolves as a `{0,d}`-valued Pascal
  (Rule 90) diamond advancing one column per row toward the left edge, and when
  its front reaches the second entry the leading 1 dies.
- `gap-arrangement` — the deterministic, unbounded, irregular positions of gaps
  ≥ 6 in the primes. It is the *arrangement*, not the magnitude: magnitude upper
  bounds provably cannot force survival (`gap-bounds-cannot-force-block-growth`,
  Eppstein's anti-Gilbreath construction).
- `non-concentration` — no independence / 2-separated hypothesis holds for the
  primes; every proved regeneration theorem is a random analogue (Chase 2024,
  CHT 2026) whose hypotheses are unchecked here.
- `regeneration-rate` — the recharge identity `Σ_{i<k}(j_i+1) ≥ k−2` for all k;
  consumption is settled, this arrival rate is the whole open core.

---

```rung
id: R-spike-4-absorbed
statement: Let A_0 = (2,3,5,7,9,...) be the consecutive odd numbers except that a
  single gap g_p (p ≥ 3) equals 4 instead of 2, so A_1 = (1,2,...,2,4,2,2,...) with
  the first even gap still 2. Then A_k(0) = 1 for every k ≥ 1: the gap-4 spike is
  absorbed and the leading 1 never dies.
off: intruder-ge-6, spike-propagation, gap-arrangement, non-concentration, regeneration-rate
stance: settled
merge: This is the bottom, and it is subsumed by `gap-lipschitz-ladder`'s
  `R-lipschitz-corner` (a single 4 in a sea of 2s is a 1-Lipschitz gap sequence, so
  row 2 is the all-{0,2} corner). Direct proof in three lines: the relative spike has
  value 2, and {0,2} is closed under absolute differencing (`closure-0d-double-edge`
  d=2), so every row beyond row 1 is {0,2}-valued, A_k(1) ∈ {0,2} for all k, and
  A_{k+1}(0) = |1 − A_k(1)| = 1. Turning `intruder-ge-6` back on is the next step:
  the gap-6 spike, whose relative value 4 is exactly where {0,4} closure becomes fatal.
```

```rung
id: R-spike-6-fatal
statement: Let A_0 be consecutive odds except that a single gap g_p (p ≥ 2) equals
  6 (or any even value ≥ 6), so A_1 = (1,2,...,2,6,2,2,...). Then A_k(0) = 1 for
  every k ≥ 1.
off: gap-arrangement, non-concentration, regeneration-rate
stance: failed
reason: FALSE, and the failure is the whole obstruction in miniature. The relative
  spike has value d = gap − 2 ≥ 4, and {0,d} is closed under absolute differencing
  (`closure-0d-double-edge`, d ≥ 4): the spike becomes a solid {0,d}-valued Pascal
  diamond whose front advances one column per row. Hand-checked for the sharpest
  case, gaps (2,2,6,2,2,...): A_1 = (1,2,2,6,2,...) gives A_2 = (1,0,4,4,...),
  A_3 = (1,4,0,4,...), A_4 = (3,4,4,...) — leading entry 3 at row 4. This is the
  same counterexample as `gap-lipschitz-ladder`'s `R-single-gap-jump-4`, re-derived
  independently. Sharper than Colonna's delete-5 (which needs g_1 = 4) and Eppstein
  (which needs unbounded growth): ONE gap ≥ 6 in the maximally stable background is
  fatal.
merge: Killed at a single irregularity, so the deterministic "small gaps + one
  exception" class is closed here: a lone late gap 4 survives (R-spike-4-absorbed),
  a lone gap ≥ 6 dies. The dichotomy at the single-gap level is exact. The survival
  direction is *shielding*: can a gap 4 placed left of a gap 6 heal the injected 4
  before it reaches the edge? That is the next rung, and it is the honest open
  content.
```

```rung
id: R-leftmost-decides
statement: Let A_0 be 2-then-odds with the first even gap g_1 = 2 and every gap in
  {2,4,6}, with finitely many 6s. Then the leading 1 survives forever if and only if
  the leftmost non-2 gap is a 4. ("Leftmost non-2 gap is 6" is fatal by the
  R-spike-6 argument with nothing to its left to interfere; "leftmost non-2 gap is 4"
  heals every 6 to its right, because the 4 creates a 2 next to each injected 4.)
off: gap-arrangement, non-concentration, regeneration-rate
stance: open
merge: Attack this next. The forward direction is the R-spike-6 argument unchanged
  (a leftmost 6 has only 2s to its left, so row 2 has 0s to the left of the killer
  4 and it propagates to the edge). The reverse direction is hand-supported but not
  proved. Hand check of the shield, gaps (2,2,4,6,2,...) — a 4 at gap position 3, a
  6 at position 4: A_1 = (1,2,2,4,6,2,...) gives
  A_2 = (1,0,2,2,4,0,...), A_3 = (1,2,0,2,4,0,...), A_4 = (1,2,2,2,4,0,...),
  A_5 = (1,0,0,2,4,...), A_6 = (1,0,2,2,...), A_7 = (1,2,0,...), A_8 = (1,2,...),
  A_9 = (1,...) — the injected 4 is pinned at a fixed column with a 2 immediately to
  its left (|4−6| = 2 supplies the first such 2, |2−4| = 2 sustains it), so it never
  reaches the second entry. The forward loop should (i) machine-check survival for
  all small position pairs (p_4, p_6) and all finite 6-sets in gaps ⊆ {2,4,6}, and
  (ii) prove the shield lemma: a {0,2} "2" immediately left of a {0,d} diamond keeps
  column 1 in {0,2}. Turning `gap-arrangement` back on means arbitrary finite sets of
  ≥6 gaps, which is R-finite-spikes.
```

```rung
id: R-finite-spikes
statement: Let A_0 be consecutive odds with a finite set S of gaps ≥ 6. The leading 1
  survives forever iff the Rule-90 evolution of the spikes keeps the second entry in
  {0,2}; a nonempty S with survival exists (any S whose leftmost non-2 gap is a 4, by
  R-leftmost-decides).
off: gap-arrangement, non-concentration, regeneration-rate
stance: open
merge: This is R-leftmost-decides with an arbitrary finite spike set — the whole set
  must be absorbed before it reaches the edge, which mixes {0,2} and {0,d} diamonds
  nonlinearly (|2−4| = 2, not XOR over F2). The merge back up is to replace "finitely
  many" by "bounded frequency", which is the deterministic non-concentration condition
  R-frequency-budget.
```

```rung
id: R-gaps-24
statement: Let A_0 = (2,3,x_1,x_2,...) with every x_i odd, x_1 − 3 = 2, and
  x_{i+1} − x_i ∈ {2,4} for all i (gaps after the first all 2 or 4). Then A_k(0) = 1
  for every k ≥ 1. Equivalent to the canonical rung `R-carved-gap24` in recharge-ladder.md,
  and subsumed by `gap-lipschitz-ladder`'s settled `R-lipschitz-corner`.
off: intruder-ge-6, spike-propagation, gap-arrangement, non-concentration
stance: open
merge: Here max non-increase (`czz2011-ducci-2-lipschitz`) gives every row maximum ≤ 4,
  so no intruder ≥ 6 and no killer diamond can form — `intruder-ge-6` and
  `spike-propagation` are off structurally, not by hypothesis. This is exactly the
  "no 6s" limit of R-leftmost-decides. The rung keeps `regeneration-rate`: (2,4)-events
  must still keep arriving. Empirical support only (0 deaths among 48 measured
  sequences to depth 4000), not a proof. Turning `gap-arrangement` back on is the real
  climb: insert one ≥6 gap into the {2,4} stream and track whether a left 4 shields it
  (the R-leftmost-decides question on a {2,4} background).
```

```rung
id: R-frequency-budget
statement: Let A_0 be 2-then-odds with gaps in {2,4} except that gaps ≥ 6 occur at
  most C times in any window of L consecutive gaps, for some explicit (C,L). Then
  A_k(0) = 1 for every k ≥ 1. This is a deterministic non-concentration condition:
  large gaps are tolerated if they are sparse enough that their diamonds are shielded
  before reaching the edge.
off: non-concentration
stance: open
merge: This is the bridge from the spike picture to the primes. The first move is to
  compute, from R-leftmost-decides, how large L must be for a given C so that every
  ≥6 gap has a 4 shield to its left — then check whether the prime gap sequence
  satisfies any such (C,L). Turning `non-concentration` back on means replacing the
  (C,L) hypothesis by a property the primes are known (or conjectured) to satisfy;
  that is the open step no held theorem covers.
```

```rung
id: R-random-analogue
statement: (Chase 2024, Math. Ann. 388:2611–2625, Thm 1) For f increasing with
  2 ≤ f(n), f(M) ≤ (1/100) log log M / log log log M, the random sequence
  a_1 = 2, a_2 = 3, a_{n+1} = a_n + 2u_n (u_n i.i.d. uniform on {0,...,f(n)−1}) is
  almost surely eventually Gilbreath.
off: non-concentration
stance: settled
merge: The goal for a random input with independence granted by fiat — the
  `non-concentration` difficulty switched off at the hypothesis level. The merge back
  up is de-randomisation: replace i.i.d. uniformity with the deterministic frequency
  condition of R-frequency-budget, keeping the sublinear growth bound. That step is
  the prime case itself.
```

```rung
id: R-full
statement: The full goal: for the primes in order, A_k(0) = 1 for every k ≥ 1 —
  equivalently A_k(1) ∈ {0,2} for every k ≥ 1, equivalently Σ_{i<k}(j_i+1) ≥ k−2
  for all k.
off:
stance: open
merge: n/a — top of the ladder. Reaching it means every difficulty is back on and
  survived; the spike-propagation picture says that means proving the prime gap
  arrangement's ≥6-diamonds are always shielded by gap-4 diamonds before the edge,
  with a rate fast enough to keep the recharge sum ahead.
```

---

## Summary

- **Bottom settled:** R-spike-4-absorbed — a single late gap-4 spike is absorbed
  because its relative value 2 stays in {0,2} (`closure-0d-double-edge` d=2). Proved
  in three lines; subsumed by `gap-lipschitz-ladder`'s settled `R-lipschitz-corner`.
- **Failed and kept:** R-spike-6-fatal — a single late gap ≥ 6 in the most stable
  background is fatal, by {0,d} closure (d ≥ 4) + Rule-90 leftward propagation. The
  single-gap dichotomy (gap 4 absorbs, gap ≥ 6 kills) is exact; this is the same
  counterexample as `R-single-gap-jump-4`, re-derived independently.
- **Next to attack:** R-leftmost-decides — the first open rung: does a gap 4 left of
  a gap 6 shield it? The "leftmost 6 kills" direction is proved; "leftmost 4 heals"
  is hand-supported in one worked example and needs a machine check + a shield lemma.
- **Difficulty expected to bite:** `gap-arrangement` first — concretely whether a 4
  shield left of a 6 always holds, which is what the primes must exploit. The deep
  difficulty behind it is `regeneration-rate`, which no spike picture yet bounds.
