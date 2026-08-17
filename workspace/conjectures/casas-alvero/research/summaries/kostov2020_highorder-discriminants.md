# Kostov, "On higher-order discriminants" (2020)

Source: arXiv:1702.08216, published *Bull. Sci. Math.* (2020) (article 102842; the journal version is behind Elsevier). Full text (the arXiv preprint): `research/sources/kostov2020_highorder-discriminants.full.md`. Note: the earlier download `kostov2020_higher-order-discriminants.full.md` is actually the *different* 2017 paper "A property of discriminants" (arXiv:1701.02912) — see its own summary.

## What it establishes

For the monic generic family P := xⁿ + a₁xⁿ⁻¹ + ⋯ + aₙ, n ≥ 4, define the **higher-order discriminants**
```
D̃_m := Res(P, P^(m)),   m = 2, …, n−2,
```
and their projections in the coefficient-subspaces a^≤k := (a₁,…,a_{k−1},a_{k+1},…,aₙ).

**Main identity (Theorem; = Prop 1 + the paper's central equation).** For each m and each coefficient index k,
```
Res( D̃_m, ∂D̃_m/∂a_k, a_k )  =  A_{m,k} · B_{m,k} · C_{m,k}²
```
where, writing P^(m) = Σ_{j=0}^{n−m} c_j a_j x^{n−m−j} and P_{m,k} := c_k P − x^m P^(m):
- for 1 ≤ k ≤ n−m:  A_{m,k} = aₙ^{n−m−k},  B_{m,k} = Res(P_{m,k}, P′_{m,k});
- for n−m+1 ≤ k ≤ n:  A_{m,k} = a_{n−m}^{n−k},  B_{m,k} = Res(P^(m), P^(m+1)).

The equation **C_{m,k} = 0 is the projection** into the a^≤k-space of the closure of the parameter set where **P and P^(m) have two distinct roots in common**. The polynomials B_{m,k}, C_{m,k} ∈ ℂ[a^≤k] are **irreducible**. The whole statement generalises with P^(m) replaced by any P* = Σ b_j a_j x^{n−m−j} with 0 ≠ b_i ≠ b_j ≠ 0 (i≠j).

**Structural facts about the discriminants (Prop 1):** each D̃_m is irreducible; it is quasi-homogeneous of quasi-homogeneous weight n(n−m) (weight(a_j)=j); it is degree n in each a_j (j ≤ n−m) and degree n−m in each a_j (j > n−m); it contains certain unique monomials M_j, N_s isolating powers of single coefficients (relevant to the run's "pure power monomials" analysis of the CA resultants). Props 9, 18, 20–22 and Lemmas 8–12, 19 give detailed divisibility, irreducibility and quasi-homogeneous-weight data. Prop 18: m = n−2 forces s_{m,k}=1, r_{m,k}=2.

## Bearing on this problem

- This is **exactly the resultant family the run's scheme method uses**: the run's R_i = Res(f, H_i(f)) are (up to the Hasse-vs-ordinary unit 1/i!) the same higher-order discriminants D̃_m = Res(P, P^(m)). Kostov gives an *independent structural analysis* of these resultants over ℂ[a]: irreducibility, quasi-homogeneity (the weighted scaling x↦λx, a_j↦λ^j a_j is precisely the run's weight scheme), and — most valuably for CA — the meaning of **C_{m,k}=0 as "P and P^(m) share two distinct roots"**. A CA counterexample is precisely a polynomial where *every* pair (P, P^(m)) shares at least one root; if any pair shares two distinct roots then the projection witnesses the more degenerate stratum. This dovetails with the root-difference / shared-root-multiplicity thread.
- Cautio n: Kostov works over ℂ with the **ordinary** derivative P^(m) = c_j a_j (no Hasse unit), so his discriminants are the ordinary-derivative resultants; in char 0 these coincide with the Hasse formulation up to units, but his analysis is char-0 (ℂ[a]) only — no char-p content, so it does *not* speak to the run's char-p bad-prime break.
- Status: **sourced/asserted** — I read the abstract, Prop 1 and the main identity and the labelled lemmas; the full proofs and the fine divisibility data are taken from the paper without independent verification here.

```claim
id: kostov-higher-order-discriminant-two-shared-roots
statement: For the monic generic family P = x^n + a_1 x^{n-1} + ... + a_n over C, the higher-order discriminant D~_m = Res(P, P^(m)) is irreducible and quasi-homogeneous of weight n(n-m) (weight(a_j)=j), and Res(D~_m, partial D~_m/partial a_k, a_k) = A_{m,k} B_{m,k} C_{m,k}^2 where C_{m,k}=0 is the projection to the coefficient subspace a^{<=k} of the closure of the parameter set where P and P^(m) share TWO distinct roots; B and C are irreducible of degree 2 and 3 in this factorisation.
hypotheses: char 0 (C[a]); n >= 4; m in {2,...,n-2}; ordinary derivative P^(m) (coincides with the Hasse resultants R_i = Res(f,H_i f) of the run up to the unit 1/i! in char 0)
holds-here: yes
status: asserted
bearing: The run's R_i = Res(f, H_i f) are the same higher-order-discriminant family; C_{m,k}=0 meaning 'two distinct shared roots' is exactly the shared-root-multiplicity structure the root-difference / coincidence thread targets. Quasi-homogeneity weight(a_j)=j is the run's weighted scaling. Char-0 only (C[a]); does not speak to the char-p bad-prime break.
anchor: research/summaries/kostov2020_highorder-discriminants.md
answers: shared-root-multiplicity
```
