# Garcia-Fritz & Pasten, "Patterns on elliptic curves beyond Bremner's conjecture", arXiv:2605.14962 (2026)

[[garcia-fritz-pasten-patterns-elliptic-2026]]
Full text: `research/sources/garcia-fritz-pasten-patterns-elliptic-2026.html.full.md`
URL: https://arxiv.org/abs/2605.14962
Authors: Natalia Garcia-Fritz, Hector Pasten (PUC Chile). ANID Fondecyt 1251300 / 1230507.
Version: v1, 14 May 2026; dated 11 Aug 2026 in header.

## What it establishes

A "pattern principle" (Theorem 3.1) generalising Bremner's conjecture from
arithmetic progressions to arbitrary patterns in the image of a finite-rank
subgroup of an elliptic curve under maps to P¹:

> **Theorem 3.1 (pattern principle).** For each d there is a constant
> κ₁(d) > 1 depending only on d such that: if E/C is an elliptic curve,
> g: E→P¹ and F: P¹→P¹ non-constant morphisms of degree ≤ d with **g and
> F∘g having different sets of branch values**, and Γ ≤ E(C) a finite-rank
> subgroup, then any S ⊆ g(Γ) with F(S) ⊆ g(Γ) satisfies |S| ≤ κ₁(d)^(1+rank Γ).

Specialisations: Theorem 1.2/3.4 (Möbius recurrences — F ∈ PGL₂ of infinite
order, bounding recurrence orbits), Corollary 3.5 (additive shifts: if
S, S+a ⊆ g(Γ) then |S| ≤ κ₁(d)^(1+rank Γ)), Corollary 3.6 (multiplicative
shifts). The additive-shift case with g = x-coordinate and F(t)=t+a recovers
Bremner's conjecture: an AP of x-coordinates of points of Γ has length
≤ c(2)^(1+rank Γ) (Theorem 1.1, restating GFP IMRN 2021 + Uniform Mordell–Lang
of Gao–Ge–Kühne).

## Key structural point relevant to the magic-square-of-squares run

**The branching hypothesis is necessary, and the Lattès duplication map is the
example that fails it.** The paper (just after Theorem 3.1) states explicitly:

> "one could take g: E→P¹ as the x-coordinate map for a fixed Weierstrass
> equation and F the corresponding Lattès map for duplication on E. Then
> F(x(Γ)) = x([2](Γ)) ⊆ x(Γ)."

So the pattern principle *cannot* be applied with F = the x-duplication Lattès
map: g and F∘g then have the same branch values, the hypothesis fails, and
indeed no such uniform bound holds for that configuration.

## Resolution of the run's open request (`exact-reduction-magic-507c`)

The open request asked whether the Garcia-Fritz–Pasten AP-length bound applies
to the MSS configuration, whose AP is of x-coordinates of **doubled** points
x(2P) rather than the curve's own x(P). Two separate facts:

1. **The AP-of-doubled-points IS an AP of x-coordinates of points on the
   single curve E, in the finite-rank subgroup 2E(Q) ≤ E(Q).** By Mordell–Weil,
   2E(Q) has finite rank equal to rank E(Q). So Theorem 1.1 (Bremner's
   conjecture as proved) applies directly with Γ = 2E(Q): an AP of length n of
   x(2Q_i) has n ≤ c(2)^(1 + rank E(Q)). There is **no geometry mismatch** —
   the "doubling" is irrelevant because the doubled points are just rational
   points of E lying in a finite-rank subgroup. This is *not* the Lattès-map
   failure case (that failure concerns the *pattern principle's* use of F as
   the duplication map itself, not an AP of points in 2E(Q)).

2. **The genuine remaining obstruction is ineffectiveness, not geometry.**
   Theorem 1.1 gives no explicit c(2) (Rémond/Uniform-Mordell-Lang constants
   are ineffective). For non-existence one would need c(2)^(1+rank E(Q)) < 3,
   i.e. rank E(Q) < log(3)/log(c(2)) − 1; with c(2) unknown and certainly ≫ 1
   this is not decidable from the theorem. So `uniform-height-bound-elliptic-ap`
   survives on the doubled-point question but still dies on the ineffective
   constant — consistent with the request's caveat (the gap for "explicit
   constant" remains).

**Bottom line for the approach:** the doubled-point AP is an AP of x-coordinates
of points in 2E(Q) on one elliptic curve E, so Bremner's conjecture (Theorem
1.1) does apply — kill the "AP on E vs AP of doubled x-coordinates" mismatch.
The approach is not refuted on that ground; its surviving obstruction is the
ineffective constant.

```claim
id: patterns-bremner-2026-no-mismatch-for-2E-Q
statement: The magic-square-of-squares AP of doubled-point x-coordinates IS an AP
  of x-coordinates of points of the single curve E: y²=x(x²−c²) lying in the finite-rank
  subgroup 2E(Q) (rank equal to rank E(Q)); hence Garcia-Fritz–Pasten Theorem 1.1
  (Bremner's conjecture, proved) bounds its length by c(2)^(1+rank E(Q)). The Lattès/
  duplication-map failure of the branch hypothesis in their pattern principle concerns a
  different configuration (using the duplication map as the recurrence F), not an AP of
  points in 2E(Q).
hypotheses: Robertson reduction holds (AP of x(2Q_i) with Q_i∈E(Q)); 2E(Q) finite index in E(Q)
holds-here: yes (this dissolves the `exact-reduction-magic-507c` mismatch worry)
status: sourced (Garcia-Fritz–Pasten 2026, arXiv:2605.14962, Section 2.2 + remark after Thm 3.1)
bearing: unblocks the doubled-point applicability question for uniform-height-bound-elliptic-ap;
  the surviving obstruction to non-existence via Theorem 1.1 is the ineffectiveness of c(2), not geometry
anchor: research/summaries/garcia-fritz-pasten-patterns-elliptic-2026.html.md
```
