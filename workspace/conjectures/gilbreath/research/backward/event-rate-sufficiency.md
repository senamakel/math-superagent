# Proof skeleton: Gilbreath's conjecture for the primes

```skeleton
goal: Gilbreath's conjecture — for the iterated absolute-difference triangle of the primes, A_k(0) = 1 for all k ≥ 1.
implies: |
  By the reduction lemma (DISCHARGED, gilbreath-reduces-to-second-in-02),
  A_k(0)=1 ∀k ⟺ A_k(1) ∈ {0,2} ∀k. Let b_k be the length of the leading
  {0,2} block in row k (positions 1..b_k). Then A_k(1) ∈ {0,2} ⟺ b_k ≥ 1.
  By the step-law theorem (DISCHARGED, step-law-theorem-proved):
  b_{k+1} ≥ b_k ⟺ (edge x_k, intruder y_k) = (2,4); otherwise b_{k+1} = b_k − 1.
  The recharge identity gives b_k = 2 + Σ_{events i<k} (j_i+1) − (k−1).
  Hence b_k ≥ 1 ⟺ Σ_{events i<k} (j_i+1) ≥ k − 2. The entire conjecture
  reduces to this inequality for all k.

  The three gaps below together close this inequality:
  G-edges — the edge flips from 0 to 2 frequently enough that erosion runs
  are bounded.
  G-intruder — after a regeneration, the new intruder is bounded by a
  function of the jump size, so the intruder drains to 4 before the block
  erodes away.
  G-balance — the jump at each regeneration is at least the number of
  erosion rows since the previous event. (This makes the surplus S_k
  monotone non-decreasing after the first event, closing the inequality.)

  Together: G-intruder bounds the starting intruder of each erosion run,
  the drain law (proved) brings it to 4, G-edges ensures the edge hits 2
  while y=4 (triggering regeneration) before the block dies, and G-balance
  ensures the surplus never falls to zero.

status: broken
rests-on: gilbreath-reduces-to-second-in-02, step-law-theorem-proved, odlyzko-block-lemma-exact, closure-0d-double-edge, rule90-interior-xor
killed-by: its closing rung G-balance (per-event j ≥ d) is REFUTED at depth 1000 — claim g-balance-per-event-refuted (transition 26: j=1 < d=2; j=0 stalls after d=2; j=1 after d=4). The surviving weak form Σj_i ≥ total erosion is the conjecture restated, so the three lemmas do not recombine into the goal. Superseded by regeneration-sufficiency.md, which drops G-balance and composes the edge factor out of a proved claim (edge-interior-invertibility-sharpened).
```

```gap
id: G-edges
lemma: |
  For the prime Gilbreath triangle, during any erosion run (rows where
  b_{k+1} = b_k − 1) with intruder y = 4, the edge x_k cannot remain 0
  for more than L consecutive rows, where L is an absolute constant
  (independent of k and b_k). That is, within at most L rows of the
  first row where y = 4, the edge must equal 2, triggering a (2,4)-
  regeneration event.

  The edge x_k = A_k(b_k) is the last entry of the {0,2} block. Its
  halved value h_k = x_k/2 evolves under the XOR rule (proved,
  rule90-interior-xor): h_k = XOR_{j: (d & j) = j} h_init[p+j] where
  d is the descent depth from the start of the erosion run and p is the
  initial edge position. So the question reduces to: for the halved bit
  pattern of the leading {0,2} block of the prime Gilbreath triangle,
  the XOR over windows of the form {j: (d & j) = j} cannot be 0 for
  more than L consecutive depths d.
status: open
next: |
  Compute the exact halved bit pattern of the block at the start of each
  of the 26 erosion runs in the depth-1000 data (code/out/blocks_depth1000.json).
  For each run, track h_k = x_k/2 (0 or 1) across the erosion rows. Measure
  the maximum consecutive run of h_k = 0 when y = 4. If the maximum over all
  26 runs is, say, ≤ 6, then L = 6 is established for depth 1000 and the
  gap becomes: prove L is an absolute constant (theory) or bound it by the
  XOR structure. A tool_builder task: code/gap_analysis/edge_flip_runs.py.
```

```gap
id: G-intruder
lemma: |
  After a (2,4)-regeneration event with jump j (so b grows by j), the new
  intruder y_{k+1} = A_{k+1}(b_{k+1}+1) satisfies y_{k+1} ≤ C · g where
  g is the maximum prime gap in the vicinity of position b_{k+1}, and C is
  a small absolute constant (C ≤ 2).

  This bounds how many erosion rows are needed to drain y to 4 (via the
  proved drain law: y decreases by 2 when the edge is 2, stays constant
  when edge is 0). If the intruder at the start of an erosion run is at
  most M, then at most M/2 − 2 edge-flips-to-2 are needed to reach y=4,
  and G-edges bounds how many rows each such flip takes.
status: open
next: |
  Audited against the depth-1000 data: for each of the 60 regeneration
  events, record the new intruder y_{k+1} and the jump j. Compute the
  empirical bound y/j. If y/j ≤ 2 for all 60 events, this is a
  numerically-supported conjecture. A tool_builder task:
  code/gap_analysis/intruder_after_regen.py. The theoretical step:
  prove that A_{k+1}(b_{k+1}+1) is the absolute difference of two entries
  from row k whose positions are near b_{k+1}, hence |difference| ≤
  max difference of consecutive entries in that region.
```

```gap
id: G-balance
lemma: |
  At every (2,4)-regeneration event, the jump j (amount by which b_{k+1}
  exceeds b_k) satisfies j ≥ d, where d is the number of erosion rows
  (b decreases) since the previous (2,4)-event. Equivalently: the
  recharge surplus S_k = b_k + k − 3 is monotone non-decreasing, which
  is already true from the step law (S_{k+1} − S_k = b_{k+1} − b_k + 1 ≥ 0
  since b_{k+1} ≥ b_k − 1). But the stronger statement j ≥ d means
  that S_k − k is monotone non-decreasing, which would close the
  conjecture (since S_1 − 1 = 1 ≥ −2 and S_k − k never decreases).

  Weaker form: prove that Σ_{events i ≤ n} j_i ≥ k_n − k_1 − n + 1,
  i.e., total jump mass exceeds total erosion between first and last event.
  This is equivalent to b_{k_n+1} ≥ b_{k_1}, i.e., the block does not
  shrink over the long term. Verified to depth 1000 (b_1000 ≈ 1.27e6 ≫ b_1 = 2).
status: refuted
next: |
  REFUTED by g-balance-per-event-refuted: on the prime rows to depth 1000,
  transition 26 (871->872) has jump j=1 against d=2 erosion rows since the
  previous event; j=0 stalls occur after d=2 and j=1 after d=4. The per-event
  bound does not hold. Its weak aggregate form (Σj_i ≥ total erosion) is the
  recharge identity restated — not a reduction. See regeneration-sufficiency.md
  for the corrected decomposition that does not need this rung.
```