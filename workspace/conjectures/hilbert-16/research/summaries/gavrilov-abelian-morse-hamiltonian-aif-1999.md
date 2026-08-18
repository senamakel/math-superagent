# Gavrilov, "Abelian integrals related to Morse polynomials and perturbations of plane Hamiltonian vector fields"

**Source**: Ann. Inst. Fourier (Grenoble) 49(2) (1999) 611–652, open access on
Numdam. Held full text: `research/sources/gavrilov-abelian-morse-hamiltonian-aif-1999.full.md`
(URL: http://www.numdam.org/article/AIF_1999__49_2_611_0.pdf).
Claim: `h16-gavrilov-abelian-morse-hamiltonian-aif-1999`.

## What it establishes

The primary treatment of the **Petrov (bounded) module** of Abelian integrals:

- **Theorem 1**: for `f ∈ K[x,y]` a *semiweighted-homogeneous* polynomial of
  weighted degree `d` and type `w = (wx, wy)`, the `K[t]`-module `P_f` of Abelian
  integrals is **free and finitely generated** by `μ = (d−wx)(d−wy)/(wx·wy)`
  polynomial one-forms, each defined by an explicit cohomology condition.
- **Theorem 2 + Corollary 2**: for semiweighted-homogeneous `f` with only Morse
  critical points, a real vanishing cycle `δ(t)` compatible with the real
  structure and satisfying condition `(*)` makes the `R[t]`-module `A_δ` free and
  finitely generated of rank equal to the rank of the (real-compatible) vector
  bundle `E_δ` — i.e., the module of Abelian integrals *along a fixed cycle
  class* is finitely generated over `R[t]`.
- **The conjecture**: for any `f` with isolated critical points and regular-at-
  infinity fibers, `P_f` is free of rank equal to the global Milnor number — the
  structural statement constraining how far the machinery extends beyond the
  semiweighted-homogeneous case.
- **§6 (the part this run needs)**: the Abelian integrals that arise in
  polynomial perturbations of **quadratic Hamiltonian vector fields with a
  center** — generic and reversible — with the explicit non-oscillation /
  Chebyshev-type results for the period annulus (the sharp `n−1`-type bound
  shape), built on the module/Milnor-bundle machinery and the argument-principle
  zero-count of Parts 2–4.

## Why it matters for this run

This is the origin of the "module freeness → sharp Chebyshev zero-count" pipeline
that the adopted approach (`abelian-picard-fuchs-argument-principle-sharp-count`)
re-runs: it gives the finite set of generating 1-forms (`μ` of them, explicitly
bounded) whose integrals span the Abelian integral module for the relevant
Hamiltonian classes, and it is the source cited by Novikov–Yakovenko as
"Proposition 1 (Gavrilov theorem)". It also fixes the condition `(*)`/real-
structure hypotheses a candidate family must satisfy (or explicitly fail) before
the rank-μ Chebyshev count applies — precisely the hypotheses a Lean statement of
the sharp count must carry. Section 6's quadratic-Hamiltonian-center case is the
natural first clean-room re-execution target (sympy over Q: generators,
Wronskians, CT-system sign checks).

**Boundary**: Theorem 1 needs semiweighted-homogeneity; the conjecture marks
exactly where generality stops being proved. Generic (non-swh) Hamiltonians need
the Picard–Fuchs system of Novikov–Yakovenko 2002 (held) instead, and the
degenerate / iterated-integral cases the Gavrilov–Iliev displacement-map work.