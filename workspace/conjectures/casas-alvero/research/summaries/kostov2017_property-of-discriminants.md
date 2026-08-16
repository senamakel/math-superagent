# Kostov, "A property of discriminants" (2017)

Source: arXiv:1701.02912 (full text). Full text: `research/sources/kostov2017_property-discriminants.full.md`. (There is also a stale duplicate of the abstract page at `research/sources/kostov2020_higher-order-discriminants.full.md`, whose `.md` summary misnamed the paper — the *actual* 2020 higher-order discriminants paper is `research/sources/kostov2020_highorder-discriminants.full.md`.)

## What it establishes

For P := xⁿ + a₁xⁿ⁻¹ + ⋯ + aₙ over ℂ[a], let R := Res(P, P′, x) be the discriminant, viewed as a polynomial in each coefficient a_k. The paper studies the **discriminant-of-the-discriminant**
```
D̃_k := Res( R, ∂R/∂a_k, a_k ).
```

**Main result:** D̃_k factors as
```
D̃_k = c_k · (aₙ)^{d(n,k)} · M_k² · T_k³,   c_k ∈ ℚ*,  d(n,k) = min(1,n−k) + max(0,n−k−2),
```
with M_k, T_k ∈ ℂ[a^≤k] (integer coefficients). Geometrically, {M_k = 0} (resp. {T_k = 0}) is the projection to the a^≤k-space of the closure of the locus where **P has two double roots** (resp. **a triple root**).

Construction: P_k := P − x P′/(n−k) for 1 ≤ k ≤ n−1, P_n := P′; then T_k = mRes(P_k, P′_k, x) for k ≠ n−1, and T_{n−1} = mRes(P_{n−1}, P′_{n−1}, x)/aₙ.

## Bearing on this problem

- Analyses how the **discriminant hypersurface {Res(P,P′) = 0}** stratifies and how its "discriminant in one coefficient" factorises into the double-root and triple-root strata. This is adjacent — not identical — to the run's CA resultants Res(P, P^(m)) (which are the *higher-order* discriminants treated in the 2020 paper). Its value here is the demonstrated mechanism: **resultant-in-a-coefficient factorises into products detecting the distinct common-root multiplicities**, the same kind of factor analysis the run performs on the R_i to separate "shares one root" from "shares two" (relevant to the multiplicity/shared-root structure of a CA counterexample).
- Char-0 (ℂ[a]) only; no char-p content. Status: **sourced/asserted** (abstract + statement read; constants and factorisations on the paper's word).
