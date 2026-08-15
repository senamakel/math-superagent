# Ladder: the spike-propagation obstruction

The three existing ladders track the *accounting* (step law, recharge, block
erosion) and the *statistical* hypotheses (non-concentration, random analogue).
This ladder tracks the one mechanism the accounting does not: a single gap ≥ 6
in an otherwise regular background spawns a `{0,4}`-valued Pascal diamond that
advances one column per row to the left edge and kills the leading `1`. The
difficulties are named at that mechanism level, and the rungs climb from the
absorbed case (gap 4) through cancellation (two adjacent gaps 6) to the prime
arrangement. This is the concrete form of `intruder-ge-6`/`unbounded-gaps`
that the canonical ladders flagged but never isolated.

```ladder
goal: For A_0 = (2,3,5,7,11,13,...) the primes in order and A_{k+1}(i) = |A_k(i) − A_k(i+1)|, prove A_k(0) = 1 for every k ≥ 1 (Gilbreath's conjecture).
difficulties: infinite-horizon, intruder-ge-6, spike-propagation, gap-arrangement, non-concentration, regeneration-rate
status: open
```

What each difficulty names, exactly:

- `infinite-horizon` — the target quantifies over every row k ≥ 1; every finite
  computation is a fact about that depth only. Kept on in most rungs because the
  model classes collapse to a corner where it is trivially discharged.
- `intruder-ge-6` — at the block boundary, intruder value 4 absorbs (`|2−4|=2`),
  intruder ≥ 6 breaks (`|2−6|=4 ∉ {0,2}`). A class whose rows have maximum ≤ 4
  (by max-non-increase, `czz2011-ducci-2-lipschitz`) never sees this difficulty.
- `spike-propagation` — a single gap ≥ 6 in a constant `2`-background is a
  relative spike of value ≥ 4; it evolves as a `{0,4}`-valued Pascal (Rule 90)
  diamond that advances one column per row toward the left edge, and when its
  front reaches the second entry the leading 1 dies. Survival requires these
  diamonds to cancel.
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
  single gap (after the first) equals 4 instead of 2 — so A_1 = (1,2,2,...,2,4,2,2,...).
  Then A_k(0) = 1 for every k ≥ 1: the gap-4 spike is absorbed and the leading 1 never dies.
off: intruder-ge-6, spike-propagation, gap-arrangement, non-concentration, regeneration-rate
stance: settled
merge: This is the bottom. It is a direct corollary of `closure-0d-double-edge` (d=2):
  the relative spike has value 2, `|2−4|=2` stays in {0,2}, and the {0,2} block
  never dies (block lemma). Turning `intruder-ge-6` back on is the next step — the
  gap-6 spike, whose relative value 4 is exactly where {0,4} closure becomes fatal.
```

```rung
id: R-spike-6-survives
statement: Let A_0 be consecutive odds with a single gap equal to 6 (so A_1 has one
  6 in a sea of 2s). Then A_k(0) = 1 for every k ≥ 1.
off: gap-arrangement, non-concentration, regeneration-rate
stance: failed
reason: The relative spike is 4, and `{0,4}` is closed under absolute differencing
  (`closure-0d-double-edge`, d=4): the spike becomes a solid 4-valued Pascal diamond
  whose front advances one column per row to the left edge. When the front reaches
  the second entry the value there is 4, and `|1−4| = 3` kills the leading 1. A spike
  at gap position p kills the 1 after p rows (hand-checked: gap 6 at position 4 →
  row 4 second entry 4 → row 5 leading entry 3).
merge: Killed at a single gap — sharper than Colonna's delete-5 (which needs a whole
  gap-4 arrangement) and than Eppstein (which needs unbounded growth). The difficulty
  `spike-propagation` bites at ONE irregularity in the maximally stable background.
  The survival direction is interference: two diamonds can cancel (`|4−4|=0`), which
  is the next rung.
```

```rung
id: R-two-spikes-cancel
statement: Let A_0 be consecutive odds with exactly two gaps ≥ 6, at positions p < q.
  The leading 1 survives forever iff the Rule-90 (F2) fold of the two 4-diamonds
  never sends a 4 to the second entry; in particular adjacent positions (q = p+1)
  cancel completely, so such surviving pairs exist.
off: gap-arrangement, non-concentration, regeneration-rate
stance: open
merge: Attack this next. It is a finite two-parameter F2 computation: each spike
  contributes a shifted Pascal-mod-2 column, and the second entry is 4 iff the XOR
  of `C(p−1−d,d)` and `C(q−1−d,d)` (Lucas's theorem) is 1 at some depth d. The
  adjacent-pair cancellation is the seed of the proof. First move: prove the
  two-diamond XOR formula from `rule90-interior-xor` + `bcz-2023-left-edge-stabilization`,
  then characterize the surviving pairs (p,q). Turning `gap-arrangement` back on
  means allowing arbitrary finite sets of ≥6 gaps — that is R-finite-spikes.
```

```rung
id: R-finite-spikes
statement: Let A_0 be consecutive odds with a finite set S of gaps ≥ 6. The leading 1
  survives forever iff the Rule-90 XOR of the |S| diamonds never sends a 4 to the
  second entry; a nonempty S with survival exists.
off: gap-arrangement, non-concentration, regeneration-rate
stance: open
merge: This is R-two-spikes with an arbitrary finite spike set — the whole set must
  cancel on the left diagonal, which is the F2 fold of a finite sum of Sierpinski
  columns. It is a linear-algebra question over F2, not a probabilistic one. The
  merge back up is to replace "finitely many" by "bounded frequency", which is the
  deterministic non-concentration condition R-frequency-budget.
```

```rung
id: R-gaps-24
statement: Let A_0 = (2,3,x_1,x_2,...) with every x_i odd, x_1 − 3 = 2, and
  x_{i+1} − x_i ∈ {2,4} for all i (gaps after the first all 2 or 4). Then A_k(0) = 1
  for every k ≥ 1. Equivalently the canonical rung `R-carved-gap24` in recharge-ladder.md.
off: intruder-ge-6, spike-propagation, gap-arrangement, non-concentration
stance: open
merge: Here max non-increase (`czz2011-ducci-2-lipschitz`) gives every row maximum ≤ 4,
  so no intruder ≥ 6 and no killer diamond can ever form — `intruder-ge-6` and
  `spike-propagation` are switched off structurally, not by hypothesis. The rung keeps
  `regeneration-rate`: (2,4)-events must still keep arriving. Empirical support only
  (0 deaths among 48 measured sequences to depth 4000), not a proof. Turning
  `gap-arrangement` back on is the real climb: insert one ≥6 gap into the {2,4}
  stream and track its diamond (the R-spike-6 mechanism on a {2,4} background).
```

```rung
id: R-frequency-budget
statement: Let A_0 be 2-then-odds with gaps in {2,4} except that gaps ≥ 6 occur at
  most C times in any window of L consecutive gaps, for some explicit (C,L). Then
  A_k(0) = 1 for every k ≥ 1. This is a deterministic non-concentration condition:
  large gaps are tolerated if they are sparse enough that their 4-diamonds cancel
  before reaching the edge.
off: non-concentration
stance: open
merge: This is the bridge from the spike picture to the primes. The first move is to
  compute, for the R-two-spikes F2 fold, how large L must be for a given C so that
  the diamonds cancel — then check whether the prime gap sequence satisfies any such
  (C,L). Turning `non-concentration` back on means replacing the (C,L) hypothesis by
  a property the primes are known (or conjectured) to satisfy; that is the open step
  no held theorem covers.
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
  arrangement's 4-diamonds always cancel before the edge, with a rate fast enough to
  keep the recharge sum ahead.
```

---

## Summary

- **Bottom settled:** R-spike-4-absorbed — a gap-4 spike is absorbed because its
  relative value 2 stays in {0,2} (`closure-0d-double-edge` d=2).
- **Failed and kept:** R-spike-6-survives — a single gap-6 spike in the most stable
  background is fatal, by {0,4} closure (`closure-0d-double-edge` d=4) + Rule-90
  leftward propagation. This isolates the obstruction at ONE irregularity.
- **Next to attack:** R-two-spikes-cancel — the first open rung, a finite F2
  computation (two Pascal-mod-2 columns), with adjacent-pair cancellation as the
  proved seed.
- **Difficulty expected to bite:** `spike-propagation` first (it is what kills the
  single-spike rung); the deep one behind it is `regeneration-rate`, which no spike
  picture yet bounds.
