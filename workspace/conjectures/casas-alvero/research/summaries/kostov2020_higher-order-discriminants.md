# Kostov 2020 — A property of discriminants

<!-- source: https://arxiv.org/pdf/1701.02912 -->
V. P. Kostov, "A property of discriminants" (arXiv:1701.02912). Full text: [[kostov2020_higher-order-discriminants.full]] (small; also see [[kostov2020_highorder-discriminants.full]] for the companion "Higher-order discriminants").

## What it establishes

For the family `P = x^n + a_1 x^{n-1} + … + a_n` of monic complex polynomials, let `R = Res(P, P', x) ∈ ℂ[a]` be the discriminant (`a = (a_1,…,a_n)`). Regard `R` as a polynomial in the single variable `a_k` and take its discriminant (resultant with `∂R/∂a_k`):

```claim
id: kostov-discriminant-factorization
statement: Res_{a_k}(R, ∂R/∂a_k) = c_k · (a_n)^{d(n,k)} · M_k^2 · T_k^3, where c_k ∈ ℚ^*, d(n,k) = min(1,n−k) + max(0,n−k−2), and M_k, T_k ∈ ℂ[a^k] (a^k = all a_j except a_k) have integer coefficients. The sets {M_k=0} and {T_k=0} are the projections (to the a^k-coordinate space) of the closures of the strata of the discriminant variety {R=0} on which P has respectively two double roots or a triple root. Explicit: with P_k := P − xP'/(n−k) for 1≤k≤n−1 and P_n := P', one has T_k = Res(P_k, P_k', x) for k≠n−1 and T_{n−1} = Res(P_{n−1}, P_{n-1}', x)/a_n.
hypotheses: P monic degree n over ℂ; R = Res(P,P',x); a_k the k-th coefficient variable.
holds-here: yes (this is the exact discriminant-factorisation structure of the i=1 slice, the simplest CA slice)
status: proved
bearing: Gives the exact stratified decomposition of the discriminant locus (two-double-root vs triple-root strata) for the degree family. In the CA scheme the i=1 resultant R_1 = Res(f,f') is a first coordinate of the CA ideal, so this describes the boundary of the lowest slice; not itself a CA step but the exact structure of where f shares a root with only f'.
anchor: research/sources/kostov2020_higher-order-discriminants.full.md (Thm 1)
contradicts: none
follows-from: none
answers: none
```

Note the `M_k^2` (two double roots) and `T_k^3` (triple root) square/cube powers: these are the correct multiplicity stranding weights on the discriminant-variety strata, the same multiplicity bookkeeping the run's u-resultant/exponent certificate uses for the full CA ideal.

## Relationship to the run

This is a supporting commutative-algebra/exact-factorisation result about the discriminant slice `R_1 = Res(f,f')`. It is relevant background for §(1) of the u-resultant approach (resultants over the coefficient ring) but is not itself a CA constraint. The companion paper ([[kostov2020_highorder-discriminants]]) treats the higher-order discriminants `Res(f^{(i)},f^{(j)})` more directly in the direction of the CA resultants.
