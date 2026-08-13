# window-range-bound

```approach
idea: A proved cell-wise bound A_k(i) <= range(max - min) of the k consecutive gap entries feeding cell (k,i). Used to bound the intruder y_k, which by the proved drain law converts directly into an event-rate lower bound under a stated gap-range hypothesis.
mechanism: Let g_m = A_1(m) (the even gap p_{m+1}-p_m, m >= 1). For k >= 2, A_k(i) is the (k-1)-fold iterated absolute difference of the gap sequence starting at g_i, so it depends only on g_i..g_{i+k-1} (k gaps). Induction on the operator: A_k(i) and A_k(i+1) both lie in [0, R] where R = range(g_i..g_{i+k-1}), so A_{k+1}(i) = |A_k(i)-A_k(i+1)| <= R. This proves, for k >= 2: A_k(i) <= max_{0<=j<k} g_{i+j} - min_{0<=j<k} g_{i+j}. (Base k=2 is the exact equality A_2(i)=|g_i-g_{i+1}|; A_1(i)=g_i itself.) The load-bearing consequence is on the intruder: y_k = A_k(b_k+1) <= range of the k consecutive gaps in its influence window. By the PROVED drain law (y_{k+1} = y_k - 2*[x_k=2] during erosion), the intruder is monotone non-increasing and reaches 4 after at most (R-4)/2 rows with edge x_k=2. Combined with a lower bound on the edge-2 frequency p (equivalently an upper bound on the max 0-run in the edge, a non-concentration condition), this yields a regeneration event at least once every ~(R(k)-4)/(2p) rows: a lower bound on the (2,4)-event rate. That is exactly the open content (consumption is settled; this is the recharge side).
status: adopted
precedent: |
  > The range bound is elementary — induction on |a−b| ≤ max − min over any
  > feeding window — and does not depend on primality. The edge-invertibility
  > lemma (`edge-interior-invertibility-sharpened`, proved this run) gives the
  > edge-2 frequency lower bound ≥ 1/b_k per block-life. The drain law
  > (`step-law-theorem-proved`, proved this run) makes the intruder monotone
  > non-increasing. These three proved components together yield a conditional
  > theorem: under a stated bound R on the intruder-feeding window's range and
  > a minimum block length b_min, the worst-case inter-event gap is
  > ≤ (R−4)/2 + b_min rows, giving a lower bound on the (2,4)-event rate. This
  > is the missing r in the subadditive-growth framework's r·J > 1 criterion.
  > Empirically the intruder never exceeds 14 despite max single gap 89, so the
  > slack is enormous.
  > 
  > No source refutes or pre-empts this: the range inequality is too elementary
  > to have been studied on its own, and no prior work couples it to the drain
  > law + edge-invertibility to produce an event-rate bound. The CHT inverse
  > theorem operates at the obstruction level (ruling out long zero-blocks and
  > long shallow {0,d}-blocks), not at the per-cell inequality level; Eppstein's
  > anti-Gilbreath construction kills gap-bound-only proofs but does not touch a
  > conditional theorem whose hypothesis includes a range bound on the intruder
  > window specifically.
first-step: |
  **(a) Range-bound verification (tool_builder).** From the oracle rows
  (witnesses.json, depth 600, and blocks_depth1000.json), compute for every
  live row k=2..161: the k consecutive gaps feeding the intruder position
  b_k+1, their range R(k) = max − min, and verify A_k(b_k+1) = y_k ≤ R(k).
  Also spot-check 100 random interior cells (k,i) against their feeding
  window's range. Report violations (expect zero — the inequality is provable
  by induction).  Compute the maximum R(k) over all live rows and compare
  against the observed max intruder (14).

  **(b) Conditional event-rate theorem statement (theorem_prover).** State the
  theorem precisely: "Let A be a Gilbreath array from a 2-then-odds initial
  sequence. Let b_k be the leading {0,2} block length at row k, with
  b_1 = 2. Let R(k) bound the range of the k consecutive gaps feeding the
  intruder at row k. Assume (i) b_k ≥ b_min ≥ 1 for all k up to the current
  row, and (ii) the intruder y_k ≤ R(k). Then the worst-case number of rows
  between successive (2,4)-events is at most (R(k)−4)/2 + b_min, where the
  first term is the max erosion rows to drain the intruder from R(k) to 4
  (drain law, edge-2 at least once per b_min rows by edge-invertibility) and
  the second term is the worst-case edge-0 stall at intruder=4 before the
  edge flips to 2."  The edge-invertibility lemma gives edge-2 at least once
  per b_k rows; with b_k ≥ b_min, this is at least once per b_min rows. When
  the edge is 2 and the intruder is 4, the (2,4)-event fires (step law).

  **(c) Empirical slack measurement (tool_builder).** For each of the 60
  regeneration events in the live regime: extract the actual inter-event gap,
  the intruder value at the start of the erosion run, and the block length
  b_k. Compare the actual gap against the worst-case bound (y_0−4)/2 + b_k.
  Report the maximum ratio (actual/bound) and the median — this measures how
  much slack the bound leaves, and whether it is tight enough to feed a
  renewal argument.  Output to `code/out/range_bound_slack.{captured.txt,json}`.

  **(d) Thread integration.** This approach supplies the event-rate lower
  bound r that the subadditive-growth framework (`subadditive-growth-ergodic-
  block-length`) needs.  Do not create a separate thread; instead amend the
  subadditive-growth thread's first-step to import this bound, once (c)
  quantifies the slack.
```

## Why this is not on disk

- Not `total-variation-oscillation-potential` (refuted): that was a run-count-of-oscillation lemma r(T(x)) <= r(x), machine-refuted at (0,0,1,1). This is a *per-cell upper bound by the feeding window's range*, which is provably TRUE (no monotonicity assumption), not a claimed global potential.
- Not `ducci-potential-max-decrease` (proposed): that hunts a numeric windowed max that *decreases*. This is a fixed, provable inequality that bounds the intruder and feeds the already-proved drain law.
- Not a prime-distribution theorem: the only number-theoretic input is a hypothesis on the *range* of k consecutive prime gaps (much weaker than Cramer, and empirically tiny: intruders <= 14 while a single gap can be 178). It is a general-operator bound plus a stated gap-statistics hypothesis, not a claim about primes per se.

## What would falsify it

The bound itself is elementary and should survive. The *application* (event-rate lower bound) would be falsified if the empirical range R(k) of the intruder-feeding windows is not small relative to the inter-event gap required by the recharge identity — i.e. if R(k) grows faster than the jump sizes allow. That is measured in the first step.

## Side

General-class side for the bound; prime side only through the (stated, mild) gap-range hypothesis.
