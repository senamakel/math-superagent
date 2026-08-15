# Intruder drain — the regeneration-side gap, split honestly

This file refines the **single live atomic gap** of `regeneration-sufficiency.md`
(`REG-intruder-drains`) into two lemmas with a real inference between them. It
does **not** restate Route B's supply side (`route-b-supply-consolidated.md`):
that file records that everything below the supply line is discharged and the one
remaining proposition is `ν₂ ≥ c·n` (named open,
`abgs-2011-s9-mod4-switch-limit-open`). This file attacks the *other* live gap —
the block/event picture — and separates what is genuinely a new lemma from what
is the supply side again under a different name.

## The honest structure

`REG-intruder-drains` bundles two different things:

1. **an input bound** — how large can the intruder be at the start of an erosion
   run? This is about the landing block of a `(2,4)`-event and is *not* obviously
   the supply side. Call it `REG-intruder-sharp-bound`.
2. **an XOR density** — does the erosion produce enough edge-2 flips to drain that
   intruder to 4 before the block dies? This is the Rule-90 edge diagonal weight,
   and — as the regeneration thread already recorded — it is the *same open
   content* as Route B's supply side in right-diagonal coordinates. Call it
   `REG-edge-flip-density`, and cross-reference rather than pretend it is new.

The inference ties the flip requirement to the actual intruder `y₀` (not to an
absolute `M`), which is what makes the reduction sound: a block with a small
intruder needs few flips, and short blocks with small intruders are not
over-demanded.

```skeleton
goal: Gilbreath's conjecture for the primes — A_k(0) = 1 for every k ≥ 1.
implies: |
  Step 0 (reduction, DISCHARGED). A_k(0)=1 ∀k ⟺ A_k(1)∈{0,2} ∀k
  (gilbreath-reduces-to-second-in-02). With b_k the leading {0,2} block length,
  A_k(1)∈{0,2} ⟺ b_k ≥ 1, so the goal is "b_k ≥ 1 for every k".

  Step 1 (exact dynamics, DISCHARGED). step-law-theorem-proved: b_{k+1} ≥ b_k
  ⟺ (edge x_k, intruder y_k) = (2,4), else b_{k+1} = b_k − 1. On an erosion run
  the drain law y_{k+1} = y_k − 2·[x_k = 2] holds (a proved corollary of the
  step law), so y is non-increasing along the run, y = 4 is absorbing under
  erosion, and the number of edge-2 flips needed to descend from y₀ to 4 is
  exactly (y₀−4)/2 (y₀ is even and ≡ 0 or 2 mod 4 by the parity wave).
  odlyzko-block-lemma-exact supplies the erosion rate 1: a block of length n is
  read at depths 0..n−1, exactly while b ≥ 1.

  Step 2 (y=4 regenerates, DISCHARGED). REG-4-forces (composition of
  step-law-theorem-proved + edge-interior-invertibility-sharpened): a nonzero
  block with b_k ≥ 1 and y_k = 4 fires a (2,4)-event within its remaining
  erosion life, before b reaches 0. The all-zero block is the sole exception
  (its edge is 0 forever).

  Step 3 (the only failure mode left). By Steps 1–2 the only way any b_k can
  reach 0 is an erosion run that ends (block exhausted) *before* its intruder
  has descended to 4. Rule that out with the two gaps:

    REG-intruder-sharp-bound (OPEN): every erosion run starts with y₀ ≤ M for
    a fixed absolute M. This bounds the needed flip count by (M−4)/2.

    REG-edge-flip-density (OPEN, = supply side): for every prime erosion run
    with block length n and initial intruder y₀, the number of edge-2 reads over
    the run's n erosion rows is ≥ (y₀−4)/2.

  COMBINE: given an erosion run, REG-intruder-sharp-bound gives y₀ ≤ M, hence a
  needed flip count (y₀−4)/2 ≤ (M−4)/2. REG-edge-flip-density guarantees the run
  produces at least (y₀−4)/2 flips. Since the n reads happen exactly while b ≥ 1
  (Step 1), the intruder reaches 4 with b ≥ 1 and a nonzero block. Step 2 then
  fires a (2,4)-event. Hence no erosion run dies: b_k ≥ 1 for all k, and Step 0
  gives A_k(0) = 1 for all k — Gilbreath's conjecture.

  Honesty note: REG-edge-flip-density is NOT an independent third front. It is
  the (2,4)-event-arrival statement in block coordinates, which the regeneration
  thread already identifies with Route B's supply bound ν₂(q_n) ≥ c·n
  (SC-supply-nu2-linear, the named open problem abgs-2011-s9-mod4-switch-limit-open).
  The genuine new content of this file is the intruder bound (REG-intruder-sharp-bound);
  closing that plus the supply side closes GC. If REG-intruder-sharp-bound turns
  out to need the supply side too, then the block picture collapses to Route B
  with no loss, which is itself a useful negative result.
status: live
rests-on: gilbreath-reduces-to-second-in-02, step-law-theorem-proved, odlyzko-block-lemma-exact, edge-interior-invertibility-sharpened, rule90-interior-xor, closure-0d-double-edge
killed-by: (none — refines the live gap REG-intruder-drains of regeneration-sufficiency.md; the predecessor event-rate-sufficiency.md is broken by the refuted g-balance-per-event-refuted rung, which this file does not use)
```

```gap
id: REG-drain-law
lemma: |
  On an erosion run (rows with b_{k+1} = b_k − 1), the intruder evolves by the
  drain law y_{k+1} = y_k − 2·[x_k = 2]: it drops by 2 exactly on the rows where
  the edge x_k = A_k(b_k) is 2, and is unchanged when the edge is 0. Consequently
  y is non-increasing along the run, y = 4 is absorbing under erosion (it stays 4
  until the edge is 2, at which point (2,4) fires and the run ends), and the
  number of edge-2 flips needed to descend from y₀ to 4 is exactly (y₀−4)/2.
status: discharged
discharged-by: step-law-theorem-proved (the drain law is a proved corollary of the step law; research/notes/step_law_proved.md)
next: none — restating this as open re-opens a proved corollary.
```

```gap
id: REG-intruder-sharp-bound
lemma: |
  In the prime Gilbreath triangle there is an absolute constant M such that every
  erosion run (maximal stretch of rows with b_{k+1} = b_k − 1) starts with an
  intruder y₀ = A_k(b_k+1) ≤ M. The run's depth-1000 data supports M = 14
  (intruders observed in {4,6,8,10,12,14}, all ≡ 0 or 2 mod 4, max 14); any
  fixed M suffices for the inference, bounding the needed flip count by (M−4)/2.
status: open
next: |
  This is the genuinely separable new lemma (the sharp form of the input-side half
  that the broken event-rate-sufficiency.md called G-intruder). Two first moves:

  tool_builder (cheap, decisive): extract every erosion run from
  code/out/blocks_depth1000.json (the 26 runs) and the 6e8/1e9 giant records
  (code/out/pattern_finder_6e8_giants.captured.txt,
  code/out/pattern_finder_1e9_giants.captured.txt). Report for each run the
  initial intruder y₀, the run length d, and the initial block length b. Check
  (i) y₀ ≤ 14 and y₀ ≡ 0 or 2 (mod 4) with zero violations (the empirical form,
  tested to the data's depth); (ii) after a genuine giant the intruder returns to
  4 within ≤ 12 rows (pattern-finder-no-loworder-plus-surplus reports this;
  promoting it from "checked" to "theorem" is one way this gap closes).

  theorem_prover: the intruder after a (2,4)-event with jump j is the first entry
  past the landing block, i.e. the first adjacent halved pair differing by ≥ 2 in
  the generating 1-Lipschitz stretch (the giant-jump characterization,
  code/out/giant_stretches.md). Prove y₀ ≤ C·(maximum gap over the generating
  stretch) from that characterization plus row-maximum-non-increasing
  (czz2011-ducci-2-lipschitz), then bound the local maximum gap. If the local gap
  bound cannot be made absolute, this lemma is the same open content as Route B's
  supply side and must be stated as a hypothesis, not a theorem.
```

```gap
id: REG-edge-flip-density
lemma: |
  For every erosion run of the prime Gilbreath triangle with block length n and
  initial intruder y₀, the number of edge-2 reads over the run's n erosion rows
  is at least (y₀−4)/2. Equivalently, in the halved Rule-90 interior, the number
  of 1s on the edge diagonal of the block pattern is at least the intruder's
  required drain count.
status: open
next: |
  STATUS FIRST — this is the same open content as Route B's supply side, not an
  independent gap. The regeneration thread records it plainly: a lower bound on
  the edge-2 flip count / a proof the intruder drains in time is exactly the
  (2,4)-event-arrival statement in block coordinates, i.e. SC-supply-nu2-linear
  (ν₂(q_n) ≥ c·n, named open, abgs-2011-s9-mod4-switch-limit-open). Do not attack
  it as a third front; route the work through research/backward/route-b-supply-consolidated.md.

  It is prime-specific, NOT universal: edge-interior-invertibility-sharpened
  proves the edge map is unitriangular (invertible), so the edge sequence is a
  bijection of the block pattern and some nonzero patterns have edge weight
  exactly 1 — no universal lower bound beyond 1 exists (the same reason
  g-supply-transfer-universal-refuted is refuted).

  tool_builder (falsification anchor, cheap): for each of the 26 depth-1000
  erosion runs, compute the halved block at run start, simulate its full erosion
  by the Rule-90 edge rule (rule90-interior-xor), and report (n, y₀, flip count,
  flip count vs (y₀−4)/2). Check flip count ≥ (y₀−4)/2 with zero violations —
  this is REG-intruder-drains itself, re-derived as a sanity anchor. Record the
  observed flip/n density; if it clusters near 1/2 (random-block behaviour) the
  lemma is true with huge margin and the target is the random analogue.

  theorem_prover (the honest first theorem is the random analogue): for a block of
  n i.i.d. Bernoulli(1/2) halved bits, the edge-2 flip count over its erosion is
  n/2 + O(√(n log n)) with high probability (an Azuma/variance bound over the
  Rule-90 edge diagonal, using rule90-interior-xor). Then state the deterministic
  non-concentration hypothesis on the prime block patterns that lifts the random
  bound — this is exactly the mod-4 switch density of the supply side. Do not
  claim a universal bound: it is false.
```
