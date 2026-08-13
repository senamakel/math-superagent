# alternating-sum-telescope-invariant

```approach
idea: An exact Abel/telescoping identity for the signed alternating sum of a Gilbreath row, which shows the linear part of the absolute-difference operator collapses to a boundary term and leaves only the nonlinear min-correction. Hunt for a weighted version of this functional that is a monotone (or conserved) invariant forcing A_k(1) in {0,2}.
mechanism: Write |a-b| = a + b - 2*min(a,b). For a row a_0..a_W with next row b_i = |a_i - a_{i+1}| (i=0..W-1), sum the signed functional sigma(a) = sum_{i=0}^{W-1} (-1)^i b_i. The linear part telescopes exactly: sum (-1)^i (a_i + a_{i+1}) = a_0 - (-1)^W a_W. Hence
  sigma(next row) = a_0 - (-1)^W a_W - 2 * sum_{i=0}^{W-1} (-1)^i min(a_i, a_{i+1}).
The linear "sum" term (a+b) is annihilated by the alternating-sum kernel, so the signed alternating sum of the next row is (boundary) - 2*(alternating sum of the pairwise minima). In the even interior (i >= 1) each min(a_i, a_{i+1}) is even, so the min-correction is divisible by 4 — this recovers the known mod-4 linearization as a corollary, but the identity is EXACT, not just a congruence (the refuted mod-4 approach was the congruence ceiling; this keeps the full integer equality). The program is to find weights w_i such that the weighted functional Phi(a) = sum (-1)^i w_i a_i makes the boundary term vanish or sign-definite and the min-correction sign-definite, i.e. Phi(next row) <= Phi(row), a genuine monotone potential of the operator. A monotone Phi whose minimal value is attained exactly on the safe shape (halved {0,1} block, i.e. original {0,2}) would force A_k(1) in {0,2}.
status: proposed
first-step: (a) Verify the exact identity on the three smallest real rows (problem.md's A_1..A_3) against the oracle before building anything — per the run's own lesson, an unverified identity is worthless. (b) Symbolically search (sympy) for a small-support weight vector w = (w_0,...,w_m) making Phi monotone: Phi(T(row)) <= Phi(row) over all {0,2}-valued blocks with an adversarial even completion, and check whether the resulting Phi is minimized at the {0,2} shape. Report the first w found or the exhaustive refutation of weight vectors up to a stated length/coefficient bound.
```

## Why this is not on disk

- Not `mod4-pascal-invariant` (refuted): that took |a-b| = a+b-2min to a congruence and hit the mod-8 lift ceiling. This keeps the EXACT integer identity and uses a different functional (signed alternating sum), whose linear part telescopes — a structural fact the congruence route never exposed.
- Not `total-variation-oscillation-potential` (refuted): that potential counted runs/oscillation and was refuted at (0,0,1,1). This is a weighted alternating-sum functional derived from the exact min-decomposition, and its monotonicity is *to be tested*, not assumed.
- Not a path-sum or subset-sum enumeration: it is a single scalar functional identity, no exponential branching.

## What would falsify it

If no small-support weight vector makes Phi monotone (or every monotone Phi is minimized away from the {0,2} shape), the invariant does not exist at this order; that is a clean, recorded negative result. The identity itself is provable and will be checked against the oracle before use.

## Side

General-class side: the identity holds for ANY row of nonnegative integers, so an invariant found here is an invariant of the operator itself, not of the primes.
