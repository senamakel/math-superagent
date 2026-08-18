# Muciño-Raymundo & Rebollo-Perdomo, "Abelian integrals for polynomials with trivial global monodromy on C²" (arXiv:2508.15925)

- **src**: https://arxiv.org/abs/2508.15925
  Full HTML: https://arxiv.org/html/2508.15925v1
- **Full texts held**:
  - `research/sources/mucino-rebollo-abelian-trivial-monodromy-2025.full.md` (abstract page)
  - `research/sources/mucino-rebollo-abelian-trivial-monodromy-html.full.md` (full HTML, 2117 lines)
- **Authors**: Jesús Muciño-Raymundo, Salomón Rebollo-Perdomo (2025, preprint).
- Summary file digest replaced 2025 by the librarian; this is the working summary.

## What the paper does

For a **primitive** polynomial H in C² with **trivial global monodromy** (deg H =
m+1), and a polynomial 1-form ω of degree ≤ n, it studies the Abelian integrals
I(c) = ∮_{γ(c)} ω along cycles γ(c) of the generic fiber {H = c}. The structural
trick: with trivial monodromy the integral along any fixed cycle class is a
**polynomial function of c** (not multivalued), so bounding its zeros becomes
bounding the real zeros of an explicit polynomial — a degree bound and a
fundamental-theorem-of-algebra count replace the Picard-Fuchs / complex-analysis
machinery.

## Concrete results (as read in the full text)

For the Neumann-Norbury normal forms (primitive type (0,2), deg H = m+1):

- **Theorem 23**: the unique Abelian integral is a polynomial with at most
  ⌊(n+1)m/2⌋ isolated zeros.
- **Section 5.4 (three-cycle example)**: with an explicit H, the integrals along
  the three cycle classes satisfy
  - Z(I₁(c)) ≤ 3n−2,  Z(I₂(c)) ≤ 3n−2,  Z(I₃(c)) ≤ n−1,
  and (non-conservative ω) N_BC(H)(ω) ≤ 2(3n−2) + (n−1).
  - Worked example, degree n=3, gives N = 15 (6+7+2 zeros, all distinct).
  - **Remark 9**: an infinite family β_l (l∈Z) of homology cycles is exhibited,
    each producing its own pair of limit cycles of the perturbed (complex)
    Hamiltonian system dH + εϑ₀ = 0 — i.e. infinitely many *complex* limit
    cycles across different homology classes. This is a complex-algebraic
    phenomenon (different cycles), NOT a real planar counterexample to H16.2;
    it underscores that the count must be per-cycle-class or on the real ovals.

## Relevance to this run / adopted approach

- Directly feeds `abelian-picard-fuchs-argument-principle-sharp-count`: a 2025
  primary source showing that trivial-monodromy structure converts Abelian
  integrals into explicit polynomials with clean zero bounds — the structural
  opposite of the general double-exponential BNY bound (h16-bny-abelian-bound).
- The zero-bounds are explicit in the degrees (m, n) and algebraically
  checkable, so a clean-room sympy + argument-principle re-check can graduate
  the pipeline (same promise as Yang 2025, held).
- Caveat for the run: the "infinite limit cycles" of Remark 9 must NOT be
  misread as conflicting with H16.2 — it is about infeasibly many complex
  homology classes, each contributing finitely many cycles around a single oval
  set. The real-oval restriction is where finiteness of the *planar field*
  problem lives.

## Status

- Preprint (arXiv, unrefereed as of acquisition).
- Claims recorded as **asserted-by-source**; the explicit polynomial identities
  (e.g. the ϑ₀ example's exact I₁,I₂,I₃) are machine-checkable but not yet
  re-executed in this run.
