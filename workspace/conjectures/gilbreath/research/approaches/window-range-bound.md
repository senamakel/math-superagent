# window-range-bound

```approach
idea: A proved cell-wise bound A_k(i) <= range(max - min) of the k consecutive gap entries feeding cell (k,i). Used to bound the intruder y_k, which by the proved drain law converts directly into an event-rate lower bound under a stated gap-range hypothesis.
mechanism: Let g_m = A_1(m) (the even gap p_{m+1}-p_m, m >= 1). For k >= 2, A_k(i) is the (k-1)-fold iterated absolute difference of the gap sequence starting at g_i, so it depends only on g_i..g_{i+k-1} (k gaps). Induction on the operator: A_k(i) and A_k(i+1) both lie in [0, R] where R = range(g_i..g_{i+k-1}), so A_{k+1}(i) = |A_k(i)-A_k(i+1)| <= R. This proves, for k >= 2: A_k(i) <= max_{0<=j<k} g_{i+j} - min_{0<=j<k} g_{i+j}. (Base k=2 is the exact equality A_2(i)=|g_i-g_{i+1}|; A_1(i)=g_i itself.) The load-bearing consequence is on the intruder: y_k = A_k(b_k+1) <= range of the k consecutive gaps in its influence window. By the PROVED drain law (y_{k+1} = y_k - 2*[x_k=2] during erosion), the intruder is monotone non-increasing and reaches 4 after at most (R-4)/2 rows with edge x_k=2. Combined with a lower bound on the edge-2 frequency p (equivalently an upper bound on the max 0-run in the edge, a non-concentration condition), this yields a regeneration event at least once every ~(R(k)-4)/(2p) rows: a lower bound on the (2,4)-event rate. That is exactly the open content (consumption is settled; this is the recharge side).
status: proposed
first-step: Verify the range bound numerically on the oracle rows (code/out/witnesses.json, depth 600/33860 primes, and blocks_depth1000.json where available): for a sample of cells (k,i) with k>=2, check A_k(i) <= range(g_i..g_{i+k-1}) with zero violations, and specifically verify y_k <= range(window) on the 161 live rows. Then compute the empirical range R(k) of the prime-gap windows feeding each intruder and compare against the measured intruder values (which are <= 14 despite max normalized gap 89), to see how much slack the bound leaves for a conditional event-rate theorem.
```

## Why this is not on disk

- Not `total-variation-oscillation-potential` (refuted): that was a run-count-of-oscillation lemma r(T(x)) <= r(x), machine-refuted at (0,0,1,1). This is a *per-cell upper bound by the feeding window's range*, which is provably TRUE (no monotonicity assumption), not a claimed global potential.
- Not `ducci-potential-max-decrease` (proposed): that hunts a numeric windowed max that *decreases*. This is a fixed, provable inequality that bounds the intruder and feeds the already-proved drain law.
- Not a prime-distribution theorem: the only number-theoretic input is a hypothesis on the *range* of k consecutive prime gaps (much weaker than Cramer, and empirically tiny: intruders <= 14 while a single gap can be 178). It is a general-operator bound plus a stated gap-statistics hypothesis, not a claim about primes per se.

## What would falsify it

The bound itself is elementary and should survive. The *application* (event-rate lower bound) would be falsified if the empirical range R(k) of the intruder-feeding windows is not small relative to the inter-event gap required by the recharge identity — i.e. if R(k) grows faster than the jump sizes allow. That is measured in the first step.

## Side

General-class side for the bound; prime side only through the (stated, mild) gap-range hypothesis.
