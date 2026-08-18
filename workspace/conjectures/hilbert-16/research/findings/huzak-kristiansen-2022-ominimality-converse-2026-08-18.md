# Huzak–Kristiansen 2022 full text held; o-minimality converse strengthens the parametric route

## Status: VERIFIED-AS-SOURCE (full text held), asserted-by-source (theorem itself)

Held this cycle (librarian):
- `research/sources/huzak-kristiansen-regularized-piecewise-unbounded.arxiv.full.md` (abstract page, 39.8 kB)
- `research/sources/huzak-kristiansen-regularized-piecewise-unbounded-html.full.md` (full HTML text, arXiv:2109.07759v2, 13 Oct 2022, 740 kB → 106 kB md)
- digest: `research/summaries/huzak-kristiansen-regularized-piecewise-unbounded-html.md`

## What it establishes (Theorem 1.1, verbatim from held full text)

There exists a quadratic vector-field `Z₊(·,λ)` and a linear vector-field `Z₋(·,λ)`,
depending smoothly on a parameter λ ∈ ℝ, such that in a compact domain U:

> For every k ∈ ℕ there exist (a) ε_k > 0, (b) a regularization function φ_k : ℝ → ℝ,
> (c) a continuous λ_c^k : [0,ε_k[ → ℝ, such that the regularized field
> Z(z) = Z₊(z,λ_c^k(ε))·φ_k(y·ε⁻¹) + Z₋(z,λ_c^k(ε))·(1−φ_k(y·ε⁻¹))
> has at least k limit cycles contained in U for all ε ∈ ]0, ε_k[.

Journal version: "The number of limit cycles for regularized piecewise polynomial systems
is unbounded", J. Differential Equations (2022), DOI 10.1016/j.jde.2022.09.028
(arXiv:2109.07759). The switching manifold is Σ = {y = 0}; the singular limit is a PWS
two-fold bifurcation of type VI₃ (visible-invisible).

## Why this matters for THIS problem (three uses)

1. **Smooth test (problem.md test 1) made sharp.** The paper is the modern, *proved*
   counterpart of Dulac's error: a smooth family (C^∞ regularization) with an unbounded
   number of limit cycles, exactly because the regularization family is NOT o-minimal.
   The authors state verbatim: "It is known that boundedness of limit cycles is closely
   related to the notion of o-minimality in function spaces... Our smoothings are taken
   from a family that does not have this o-minimality property. From this viewpoint it
   is not surprising that we find that the number of limit cycles is unbounded."
   → Any argument for H(2) < ∞ must locate the step that fails for these regularized
   systems; the step is the o-minimality/quasianalyticity of the parameterized family.

2. **Strengthens the `parametric-ominimality-nonhyperbolic-graphics` approach.**
   That approach (research/approaches/parametric-ominimality-nonhyperbolic-graphics.md,
   proposed) wants finite cyclicity of the open non-hyperbolic DRR graphics from
   definability in a fixed o-minimal structure (Kaiser–Rolin–Speissegger ℝ_Q expansion).
   Huzak–Kristiansen supply the *converse direction*: non-o-minimal smoothing ⇒
   unbounded cycles. Together with Speissegger's uniform-finiteness principle (held),
   this brackets the open question: H(2) < ∞ should hold iff the full parametric return
   map of each open graphic is definable in an o-minimal structure. This is a genuine
   sharpening of the approach's mechanism, sourced from a 2022 JDE paper.

3. **Boundary sanity check for any claimed uniform bound.** The unboundedness is for
   regularized *piecewise* polynomial systems, so it does NOT falsify H(2) < ∞ for
   smooth polynomial fields; but it shows the boundary between bounded/unbounded runs
   exactly along o-minimality, which is where the smooth test bites.

## What would falsify this reading

- A source showing H(2) < ∞ for smooth polynomial fields while the return maps of the
  open graphics are provably NOT definable in any o-minimal structure — that would
  disconnect o-minimality from uniform boundedness. None known.
- A correction/withdrawal of Huzak–Kristiansen Theorem 1.1. None known (JDE-refereed).

## Provenance

- Downloaded by librarian 2026-08-18 from https://arxiv.org/abs/2109.07759 and
  https://arxiv.org/html/2109.07759 (both reachable, full text held).
- Memory service (Cognee) was down during this cycle; this finding is the durable
  workspace record. Should be mirrored to Cognee when the service recovers.
