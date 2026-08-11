# Pinsky, "The Inversion Statistic in Derangements and in other Permutations with a Prescribed Number of Fixed Points" (EJC 33(2), P2.36; DOI 10.37236/14250)

## What it establishes
For each n and k∈{0..n}, let P_n^(k) be uniform measure on perms of S_n with
exactly k fixed points. Gives an **exact finite-n formula** for the expected
number of inversions under P_n^(k), and for the per-pair inversion probability
P_n^(k)(σ_i^{-1}<σ_j^{-1}) for 1≤i<j≤n (i.e. i precedes j). Asymptotics: expected
inversions in a random derangement (k=0) is n(n−1)/4 + n/6 + 1/12 + o(1); for
k≥2 it is n(n−1)/4 − (k−1)n/6 − (k²−k−1)/12 + o(1); borderline k=1 gives +1/12
over uniform. k, i, j may depend on n. Proofs use the Chinese-restaurant
construction.

## Why it matters here (the open core)
Our reduced statistic needs A_n, B_n from f_n(k), the pair-inversion count
translation/affine in gap, whose coefficient sums run over cycle types but
depend only on a_1=#fixed points. Pinsky gives exactly the machinery for the
fixed-point-conditioned per-pair inversion probability, and this paper is the
exact finite-n (not just asymptotic) companion to the fixed-point-conditioned
part of [[pinsky_schickentanz_ewens_html]] (Prop 10a there). Together they give a
concrete summation route to A_n, B_n: average the per-gap inversion prob over
the fixed-point count distribution of a uniform permutation.

## Verdict
Directly relevant, mechanism/route — an exact finite-n per-gap inversion
probability conditioned on the fixed-point count, closing a gap between the
two already-proved mechanisms. It is NOT itself the closed form for A_n, B_n and
does not compute Q(10^6). Full text: L0 `pinsky_inversion_fixed_points.full.md`
(EJC page + abstract; PDF at combinatorics.org v33i2p36/pdf).
