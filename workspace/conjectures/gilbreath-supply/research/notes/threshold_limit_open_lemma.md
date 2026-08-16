# Open lemma for the threshold-limit proof: the hypergeometric parity-mode bound

**Author:** scholar (post-reconciliation). Tangible gap left by the third pass's
resolution of GOAL.md's head question.

## Context

GOAL.md's one computation ("does the min weight ratio at which linear supply
becomes typical tend to 0, or plateau near 1/8") is **resolved on disk** as
measured-not-proved (see `research/threads/supply-class-characterisation.md`
HEAD QUESTION RESOLVED; claims `threshold-mean-exact-parity-formula`,
`threshold-weight-sublinear-n055-measured`, 
`weight-threshold-tends-to-zero-sublinear-exponent`):
- exact-mean threshold ratio falls monotonically from n=14: 0.375@8 → 0.0028@2^18
  (no plateau; the pass-2 `0.125,0.125` was a 300-sample/coarse-grid artifact);
- combined sampled threshold (mean AND frac>=0.5) falls 0.375@8 → 0.020@4096;
- absolute threshold weight w(n) ~ n^0.55, LEADING to "linear supply typical
  once switch count exceeds ~n^0.55" — a sublinear demand, strictly weaker than
  positive mod-4 switch density.

The measured/verified content is exact-mean per n. What is NOT yet a proof is
the **limit** theta(n) → 0. That needs three pure-F2/hypergeometric lemmas
spelled out in `research/backward/supply-threshold-limit.md`:
`G-threshold-parity-control`, `G-threshold-asymptotic-zero`, `G-threshold-concentration`.

## The specific unproved bound

`G-threshold-parity-control` needs: for X ~ Hypergeometric(n, m, w),
```
|E[(-1)^X]| <= max_j P[X=j] = O(1/sqrt(1+Var X)),
```
by splitting the alternating sum at the mode into two monotone tails each
bounded by the mode atom, plus the standard log-concavity local bound on the
mode atom. This single lemma is the engine of both of the other two.

**This is NOT a missing source.** The on-disk library (O'Donnell, Guruswami–
MacWilliams) does not state it, but it is an elementary, self-provable result:
the hypergeometric distribution is log-concave (its probability mass function
has ratio `P[X=j+1]/P[X=j]` monotone), hence unimodal, and the standard local
limit bound `max_j P[X=j] = O(1/sqrt(Var X))` holds. The absolute constant C
in `max_j P[X=j] <= C/sqrt(1+Var X)` is the only thing to pin; a theorem_prover
or symbolic role can derive and fix it without any new download. The earlier
refuted pointwise bound `|E[(-1)^X]| <= (1-2theta)^m` must NOT be resurrected
(the `n=6,m=3,w=2` counterexample in `supply-threshold-limit.md`).

**Falsifier to check first:** verify numerically over all (n,m,w), n<=40 that
`|E[(-1)^X]| <= max_j P[X=j]` holds, and that the sharp corner (n=6,m=3,w=2,
|E|=0.2, max atom = P[X=1] = 3/5 = 0.6) satisfies it comfortably.

## What closing it would give

`G-threshold-asymptotic-zero`: group depths by popcount k; N_p = C(L,k) cells of
m=2^k, each parity |E[(-1)^X]| <= C/sqrt(1+theta(1-theta)2^k(1-2^k/n)); the
worst group k=L/2 contributes (n/sqrt(log n))/n^(1/4) = n^(3/4)/sqrt(log n) = o(n)
and the other groups are smaller, so the biased-cell sum is o(n) and
E[nu2/n] -> 1/2 for every fixed theta -> theta_mean(n)/n -> 0 (PROOF, not
inference). `G-threshold-concentration`: Var(nu2(n)) = o(n^2) via the second
moment over symmetric-difference sizes, giving the fraction criterion too —
the "typical" threshold itself -> 0. Both are elementary; no primes, no number
theory. This is the natural next attack if a role wants to convert the measured
tends-to-0 into a theorem.

```claim
id: threshold-limit-hinges-on-hypergeometric-mode-bound
statement: The proof that the linear-supply typical-weight threshold tends to 0
  (private claim: goal threshold-limit) reduces to exactly one elementary lemma:
  for X ~ Hypergeometric(n,m,w), |E[(-1)^X]| <= max_j P[X=j] = O(1/sqrt(1+Var X))
  (log-concavity/unimodality + local limit). The on-disk library does not state
  this bound; it is self-provable, not a missing source. The measure/verified
  content (threshold ratio falls exactly to 0.0028@2^18, absolute weight ~n^0.55)
  is not a proof of the limit; this lemma, with the popcount-group sum, is the
  missing proof.
hypotheses: X ~ Hypergeometric(n,m,w) (the w ones among n, m read positions of a
  fold cell); floored fold d in [2,n-1]; threshold fixed at c=0.40.
holds-here: yes (all checks are pure combinatorial; no prime input)
status: measured-not-proved (the threshold values are exact-verified; the limit
  and this lemma are open)
bearing: closing it promotes the third pass's measured tends-to-0 to a proof
  (G-threshold-asymptotic-zero + G-threshold-concentration), the strongest
  affirmative statement in the workspace; it still does not prove SUPPLY for the
  primes ('typical is not this string').
answer-note: request walsh-spectral-subset-b904 and the threshold-limit gap are
  NOT served by a new download; hand G-threshold-parity-control to a
  theorem-prover/symbolic role.
```
