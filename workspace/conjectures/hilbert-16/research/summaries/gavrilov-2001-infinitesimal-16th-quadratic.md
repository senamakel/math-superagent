# Gavrilov, "The infinitesimal 16th Hilbert problem in the quadratic case" (2001)

<!-- source: https://www.math.univ-toulouse.fr/~gavrilov/publications/31.pdf | converted from PDF; full text at research/sources/gavrilov-2001-infinitesimal-16th-quadratic.full.md -->

## What it establishes

**Theorem 1** (main): Let `H(x,y)` be a real cubic polynomial with four distinct
critical values (in a complex domain), and let `X_H = H_y ∂/∂x − H_x ∂/∂y` be
the corresponding quadratic Hamiltonian vector field. Then there is a
neighborhood `U` of `X_H` in the space of all quadratic plane vector fields
such that any `X ∈ U` has **at most two limit cycles**.

This is the **infinitesimal (weakened) Hilbert 16th problem in the quadratic
case**: the exact bound `Z(3,2) = 2` for Abelian integrals of a cubic
Hamiltonian with four distinct critical values, established via:

- Milnor-fibration/Dynkin-diagram structure of the cubic (Lemmas 1–6, §2);
- the bifurcation set `B_reg` of zeros of the Abelian integral
  `d²/dh² I_{αβγ}(h)` in a complex domain — five smooth codimension-one
  manifolds `l₂, l₃, l₄, l_∞, Δ` (Theorem 3.1, §3);
- upper bounds: the maximum number of zeros of `d²/dh² I_{αβγ}` in
  `D = C \ [1/6, ∞)` is **two** if `X_H` has one saddle and one center, and
  **four** otherwise (Theorem 4.1); exactly one zero in `U` (Theorem 4.2);
- the geometry of the centroid curve (Theorem 5.1, 5.2) used to conclude the
  main theorem (§6).

## What it implies for this run

- It is the canonical primary source for the run's sharp-Abelian goals
  (`abelian-picard-fuchs-argument-principle-sharp-count` approach and the
  `h16-sharp-abelian-named-family-G-*` claims): it demonstrates, in the
  quadratic/cubic case, the full route — Picard–Fuchs/Gauss–Manin structure,
  complex-domain argument-principle counting, exact bound `Z(3,2)=2`.
- It is the quadratic-case predecessor of BNY 2010 (`On the number of zeros of
  Abelian integrals`, held): BNY gives the general constructive
  double-exponential bound; Gavrilov gives the exact quadratic-case count
  under the four-distinct-critical-values hypothesis.
- The theorem is a **local-in-parameter-space** bound (neighborhood `U` of
  `X_H`), NOT a uniform bound over the whole quadratic family — consistent
  with problem.md's caution that pointwise/local finiteness is not H(2) < ∞.
  Its method (complex-domain zero counting of the Abelian integral's second
  derivative) is the template the run's sharp-count approach adapts.

## Evidence class

`asserted-by-source` — the author's own primary full text (Springer Inventiones
math. 143 (2001) 449–497, DOI 10.1007/s002220000112), held in full.

## Hypotheses to state beside any use

- `H` real cubic with **four distinct critical values** (real or complex);
- neighborhood `U` in the space of **quadratic** fields;
- bound is **at most two** limit cycles per field in `U`.

## Anchors

- Full text: `research/sources/gavrilov-2001-infinitesimal-16th-quadratic.full.md`
- Abstract + Theorem 1 (lines ~1–30); Theorem 3.1 (§3); Theorems 4.1–4.2 (§4);
  centroid curve (§5); proof of Theorem 1 (§6).
