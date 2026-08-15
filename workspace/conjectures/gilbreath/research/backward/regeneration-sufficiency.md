# Proof skeleton: the regeneration side, corrected

This supersedes `event-rate-sufficiency.md`, whose closing rung (`G-balance`,
the per-event bound `j ≥ d`) is **refuted** at depth 1000
(`g-balance-per-event-refuted`: transition 26 has `j=1 < d=2`; also `j=0` stalls
after `d=2` and `j=1` after `d=4`). The weak aggregate form of that rung is the
conjecture restated, not a reduction, so the three lemmas in that file do not
combine to give the goal. This file keeps the two lemmas that *were* doing real
work (the intruder and the edge), factors the edge behaviour out entirely with a
proved claim, and leaves exactly one open gap — the intruder's descent to 4.

```skeleton
goal: Gilbreath's conjecture for the primes — A_k(0) = 1 for every k ≥ 1.
implies: |
  Step 1 (reduction). By gilbreath-reduces-to-second-in-02 (DISCHARGED):
  A_k(0)=1 ∀k ⟺ A_k(1) ∈ {0,2} ∀k. With b_k the length of the leading {0,2}
  block (positions 1..b_k), A_k(1) ∈ {0,2} ⟺ b_k ≥ 1, so the goal is
  "b_k ≥ 1 for every k".

  Step 2 (exact dynamics). By step-law-theorem-proved (DISCHARGED):
  b_{k+1} ≥ b_k ⟺ (edge x_k, intruder y_k) = (2,4); otherwise b_{k+1} = b_k − 1.
  On erosion the drain law y_{k+1} = y_k − 2·[x_k = 2] holds, so the intruder
  y is non-increasing along an erosion run and y = 4 is absorbing under erosion
  (y stays 4 exactly until the edge is 2, and then (2,4) fires).

  Step 3 (edge behaviour is pinned). REG-4-forces (DISCHARGED, composition of
  step-law-theorem-proved + edge-interior-invertibility-sharpened): if at some
  row b_k ≥ 1, the leading block is not identically 0, and y_k = 4, then a
  (2,4)-event fires within the block's remaining erosion life — before b hits 0.
  Reason: while no event fires the edge stays 0 (else it would fire) and y stays
  4 (absorbing); the halved edge evolves by Rule 90 and a nonzero block shows
  edge value 2 at least once in its remaining reads (invertibility); at that
  read (x,y) = (2,4) and the step law fires. The all-zero block is the sole
  exception (its edge is 0 forever).

  Step 4 (the only thing left). Since Step 3 rules out death at y = 4 against a
  nonzero block, the only way any b_k can reach 0 is that an erosion run ends
  (block exhausted) before its intruder has descended to 4. So the one open
  gap, REG-intruder-drains, closes the goal:

  REG-intruder-drains (OPEN): in the prime triangle, every erosion run reaches
  a row with intruder y = 4 while the block is still nonzero and b ≥ 1. Then
  Step 3 regenerates at that row, no erosion run dies, b_k ≥ 1 for all k, and
  by Step 1 A_k(0) = 1 for all k — Gilbreath's conjecture.

status: live
rests-on: gilbreath-reduces-to-second-in-02, step-law-theorem-proved, edge-interior-invertibility-sharpened, rule90-interior-xor, closure-0d-double-edge
killed-by: (none — this is the corrected regeneration-side decomposition; the predecessor event-rate-sufficiency is broken by the refuted g-balance-per-event-refuted rung)
```

```gap
id: REG-4-forces
lemma: |
  (Composed lemma, discharged.) If a Gilbreath row has leading {0,2} block
  length b ≥ 1, the block A_k(1..b) is not identically 0, and the intruder
  y_k = A_k(b+1) equals 4, then the step-law regeneration event (x,y) = (2,4)
  fires within the block's remaining erosion life — i.e. before b reaches 0.
  The all-zero block is the unique block for which y = 4 does not force
  regeneration (its edge is 0 at every read, so it dies).
status: discharged
discharged-by: step-law-theorem-proved + edge-interior-invertibility-sharpened (composition)
next: |
  The three ingredients are individually proved: the step law makes (2,4) the
  only regeneration and gives the absorbing drain; the drain law makes y = 4
  persist while the edge is 0; invertibility (unitriangular edge map) makes a
  nonzero halved block show a 1 — hence the edge a 2 — at least once in its
  remaining reads, latest at the length-1 read. Optional hardening, not a gap:
  a theorem_prover formalises the composition in Lean over the existing
  code/lean/descent_lemma.lean and code/lean/gilbreath_reduction.lean
  primitives, reporting #print axioms and zero sorry.
```

```gap
id: REG-intruder-drains
lemma: |
  In the prime Gilbreath triangle, every erosion run (maximal stretch of rows
  with b_{k+1} = b_k − 1) reaches a row with intruder y = 4 while the leading
  block is still nonzero (b ≥ 1), before the block is exhausted (b = 0).
  Equivalently, via the drain law y ← y − 2·[x = 2]: the edge takes value 2 at
  least ⌈(y₀ − 4)/2⌉ times within each erosion run, where y₀ is the intruder at
  the run's start — so the intruder descends to 4 in time.
status: open
next: |
  First move (tool_builder, cheap and decisive): extract every erosion run from
  code/out/blocks_depth1000.json (the 26 runs of the depth-1000 record) and the
  6e8/1e9 giant records (code/out/pattern_finder_6e8_giants.captured.txt,
  code/out/pattern_finder_1e9_giants.captured.txt). For each run report
  (initial intruder y₀, final intruder y_f, edge-2 flip count, run length d,
  initial block length b). Two checks: (i) the drain-law identity
  "flip count = (y₀ − y_f)/2" must hold with zero violations (sanity); (ii) the
  target "y_f = 4 with b ≥ 1 and nonzero block in every run" — this is exactly
  REG-intruder-drains, tested to the data's depth. If y₀ ≤ 14 throughout (as
  the depth-1000 intruder stats show), the gap is a claim about at most 5
  edge-2 flips per run.

  Second move (theorem_prover): the edge-2 flip count is the number of 1s on
  the Rule-90 edge diagonal of the halved block; only "≥ 1" is proved today
  (invertibility). A lower bound on the flip count / a proof that the intruder
  drains in time is the same open content as Route B's supply side — the
  recharge identity in right-diagonal coordinates is exactly the
  (2,4)-event-arrival statement (lemma54-rederivation-safe), already reduced to
  the mod-4 switch density w(n) ≥ c'·n, which abgs-2011-s9-mod4-switch-limit-open
  identifies as a named open problem. Proving the precise correspondence turns
  this gap into the run's conditional theorem (Granville Lemma 5.4 + Theorem 5.5)
  rather than a new standalone conjecture.
```
