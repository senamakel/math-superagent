# Backward skeleton — no non-trivial Collatz cycle (sub-claim (b))

The goal this file is a proof skeleton of is **sub-claim (b): there is no
non-trivial cycle of the Collatz map** — equivalently, the only periodic orbit
on the positive integers is the trivial cycle $1\to4\to2\to1$. This is one of
the two halves of the conjecture (the other, ruling out divergent orbits, is
sub-claim (a); the two are independent and this skeleton does not touch (a)).

The run is committed to the Diophantine lever (GOAL.md), and the literature
already proves the upper arm of that lever — the irrationality measure of
$\log 3/\log 2$ — and the bridge from a cycle to a near-integer relation
between powers of $2$ and $3$. What no source establishes is the matching
*lower* arm: a lower bound on the cycle's minimum element that grows fast
enough to collide with the Diophantine upper bound. The skeleton names that
missing lower bound as the single open gap, and the inference that combines it
with what is already proved.

```skeleton
goal: There is no non-trivial cycle of the Collatz map T (n/2 if n even, (3n+1)/2 if n odd) on the positive integers; the only periodic orbit is 1 -> 4 -> 2 -> 1.
implies: A non-trivial m-cycle is governed on two sides by the single ratio (K+L)/K (K odd members, L even). The cycle identity forces the upper bound (K+L)/K < delta + (3 log 2 / K) * sum_i T(n_i) (Hercher Theorem 16, claim hercher-m92). The effective irrationality measure mu < 8.616 of delta = log 3/log 2 forces the lower bound |delta - (K+L)/K| > c_0 / K^mu (claim zudilin-mu-8616). The cycle is excluded once the lower bound exceeds the upper, i.e. once c_0 / K^mu > (3 log 2 / K) * sum_i T(n_i). The missing piece is a lower bound on sum_i T(n_i) (or on x_min) growing as a positive power of K with exponent > 1/(mu-1) ~ 0.1313, so the two arms collide for all K. G-cycle-diophantine-bridge and G-irrationality-measure are discharged by the literature; G-min-element-lower is the single open gap.
killed-by: 
rests-on: hercher-m92, hercher-K-1p375e11, zudilin-mu-8616, lagarias-W2, crandall-finite-cycles
status: sketched
```

## Gaps

```gap
id: G-cycle-diophantine-bridge
lemma: Every non-trivial m-cycle of the accelerated map T with K odd members, L even members, and minimum element x_min satisfies the two-sided bound delta < (K+L)/K < delta + (3 log 2 / K) * sum_{i=1}^{m} T(n_i), where delta = log 3/log 2, n_i are the local minima, and T(n_i) = sum_{t=0}^{k_i-1} 1/C^t(n_i) with k_i the run of odd steps after n_i. Equivalently the rational (K+L)/K is a rational approximation to delta with error < (3 log 2 / K) * sum_i T(n_i), and sum_i T(n_i) is exponentially small in x_min.
status: discharged
discharged-by: hercher-m92 (Hercher 2022, Theorem 16 + Corollary 17; the identity 2^{K+L} = prod_{n in Omega_o} (3 + 1/n) is proved in the source, and the AM-GM rewrite giving the upper bound is the proof of Theorem 16). The same bridge appears as Simons-de Weger's Lemma 1 (Crandall 1978) and the convergent-forcing inequality 0 < (K+L) log 2 - K log 3 < 1/x_min + 1/x_1.
thread:
next:
```

```gap
id: G-irrationality-measure
lemma: The effective irrationality measure of delta = log 3/log 2 is mu < 8.616: there exists an effective constant c_0 > 0 such that for all integers p, q >= 1, |delta - p/q| > c_0 / q^mu. Applied to p = K+L, q = K, this gives |delta - (K+L)/K| > c_0 / K^mu.
status: discharged
discharged-by: zudilin-mu-8616 (Zudilin 2004, Theorem 3, after Rhin: mu(gamma) < 8.616 for every nonzero gamma in Q log 2 + Q log 3, and delta = log 3/log 2 is such an element). The constant c_0 is effective in the source (Rhin-type linear forms); the weaker mu <= 11.1017577 of zudilin-mu-1110 is also available as a fallback.
thread:
next:
```

```gap
id: G-min-element-lower
lemma: For every non-trivial m-cycle, the quantity S := sum_{i=1}^{m} T(n_i) (the Hercher sum of reciprocal-orbit terms over the local minima) satisfies a lower bound growing as a positive power of K — concretely, S > C * K^alpha for explicit constants C > 0 and alpha > 1/(mu - 1) with mu = 8.616, i.e. alpha > 1/7.616 ~ 0.1313 — so that the Diophantine lower bound c_0 / K^mu exceeds the bridge upper bound (3 log 2 / K) * S for all sufficiently large K. (Equivalently: a lower bound on x_min, or on K itself, that makes the two arms collide.) The bound must hold for *every* non-trivial cycle, not almost every; it is the worst-case statement the parity-independence obstruction blocks.
status: open
discharged-by:
thread:
thread: DONE — first deliverable: `code/out/collision_table.txt` (from `code/no-cycle-diophantine/collision_table.py`), the side-by-side table for m = 92..200. It pairs Hercher's exact K lower bound H(m) (published Corollary 24 Table 1, source line per row) with the Diophantine threshold log10(3·log2) − log10(c_0) + 8.616·log10(m). Finding: the deficit (threshold at c_0=1 minus log10 H(m)) grows strictly with m, min −2.6519 at m=92, max +1.4734 at m=200; at c_0=1 the threshold overtakes Hercher's K-bound from m ≥ 135. Claims `hercher-table-K-bounds-m-92-200` and `collision-deficit-grows-with-m` are on file (checked, numerical).
next: Fix mu = 8.616 and the effective c_0 from Zudilin's construction (read off the polynomial choice in Section 3.4 of the source). Note the table's H(m) bounds K, not x_min — a genuine x_min lower bound is what G-min-element-lower needs, and Hercher's K-bound does not imply x_min ≥ H(m). Derive, symbolically in sympy, the exact collision inequality c_0 / K^mu > (3 log 2 / K) * S as a threshold K_*(S), with the true c_0 inserted (c_0 < 1 shifts every threshold down by log10(c_0), moving the crossing to larger m). Then build an exact checker (tool_builder) that, for each m in a finite range and each admissible run-pattern (k_1,...,k_m), computes the minimum-element lower bound the existing Hercher/Simons-de Weger machinery already gives (Corollary 24's table is the template), and tests whether the smallest surviving K already exceeds K_*.
```

## What this skeleton does not claim

- It does **not** address sub-claim (a), divergent orbits. A divergent orbit is
  not a cycle, so neither the cycle identity nor the irrationality measure
  applies to it. Closing sub-claim (b) alone does not prove the conjecture; it
  leaves (a) open. This is stated plainly so the run does not report a
  cycle-exclusion result as the full conjecture.
- It does **not** claim the irrationality measure can be improved. $\mu < 8.616$
  is taken from the literature as a fixed constant (claim `zudilin-mu-8616`);
  improving $\mu$ is a separate problem in linear forms in logarithms and is
  not this run's to do. A smaller $\mu$ would lower the threshold in
  `G-min-element-lower` (the exponent $1/(\mu-1)$ shrinks as $\mu$ shrinks,
  making the collision easier), so the gap is monotone in $\mu$ — but the gap
  is open at the current best $\mu$, and that is what the skeleton records.
- The finite exclusions already on file (`hercher-m92`: $m \le 91$;
  `lagarias-W2`: period $< 10^{10}$; `hercher-K-1p375e11`: $K > 1.375\times
  10^{11}$ given the verification bound) are the *checked initial segment* of
  this argument. They are not subsumed by the skeleton; they are the evidence
  that the two arms do collide for small $m$, and the skeleton is the
  statement that they collide for all $m$.

## Why this decomposition and not another

The two natural decompositions of sub-claim (b) are (1) "no cycle of bounded
length" — finite, settled computationally up to $m=91$ and period $10^{10}$ —
and (2) "no cycle of any length" — the tail. A decomposition into (1) is
already discharged by `hercher-m92` and `lagarias-W2` and needs no skeleton;
the open case is the tail, and the only known lever for the tail is the
Diophantine one. So the skeleton is built around the Diophantine collision,
and its single open gap is the lower arm that no source provides. A
decomposition that instead tried to extend the finite exclusion by larger
computation would be an approach (a route), not a decomposition — and it would
hit the verification-bound ceiling that `barina-2075-2p60` already sits at.
