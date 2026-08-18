# Panazzolo–Rousseau 2017 — topological classification of limit periodic sets

Full text: [[arxiv-1702.04965-panazzolo-rousseau-limit-periodic.full]]
(arXiv:1702.04965; published in Qualitative Theory of Dynamical Systems, 2020).

## What the source establishes (held full text, verbatim)

**Definition 1.1 (limit periodic set)** — the definition this run's frame uses: Γ ⊂ ℝ²
is a limit periodic set for a polynomial family (X_λ) at parameter λ₀ if there are
λ_n → λ₀ and topological circles γ_n (limit cycles of X_{λ_n}) with γ_n → Γ̂ in the
Hausdorff topology of 𝕊² (Bendixson compactification). First introduced by
Françoise–Pugh.

**Proposition 1.2 (Poincaré–Bendixson consequence):** Γ̂ is one of (i) a singular
point; (ii) a periodic orbit; (iii) a polycycle (cyclic ordered collection of
singular points and integral arcs); (iv) a degenerate limit cycle (contains
non-isolated singularities).

**Theorem 1.3 (main result):** every limit periodic set Γ of a polynomial planar
family is homeomorphic (via φ: 𝕊²→𝕊²) to a compact connected semialgebraic set of
dimension 0 or 1; conversely, every non-empty closed semialgebraic Γ ⊂ ℝ² of
dimension 0 or 1 with connected compactification is realizable as a limit periodic
set of some polynomial family.

**Prior state it corrects:** Panazzolo–Roussarie's first characterization needed the
first jet of the singular points non-vanishing; this paper removes that and proves
the converse, improving the first author's earlier examples (limit periodic sets not
in the Poincaré–Bendixson list — i.e. the (iv) degenerate case is real).

## What it lets this run conclude

- The **Roussarie reduction's object is well-defined and complete**: limit cycles can
  only accumulate on the four Poincaré–Bendixson types, and the DRR 121-graphic
  program is exactly the case-by-case analysis of those limit periodic sets for
  quadratic fields (the source itself says the DRR program "is divided in 121
  case-by-case analysis based on the limit periodic sets" — a verbatim primary-source
  anchor for the 121 count).
- **The converse matters for uniformity:** since every semialgebraic compact
  connected 0- or 1-dimensional set is realizable as a limit periodic set, a
  uniformity argument cannot restrict the topology of accumulation sets to a smaller
  class; finite cyclicity must be proved for the actual DRR graphics, not for a
  topologically smaller list.
- The degenerate case (iv) is real: the earlier examples show limit periodic sets
  topologically outside the PB list exist; the DRR degenerate graphics (DF*, DH*,
  DI*) are the quadratic instances.

```claim
id: h16-panazzolo-rousseau-limit-periodic-topology
statement: Panazzolo–Rousseau (arXiv:1702.04965, published QTDS 2020): (Definition 1.1) a limit periodic set of a polynomial planar family is the Hausdorff limit of limit cycles; (Proposition 1.2) every limit periodic set is a singular point, periodic orbit, polycycle, or degenerate limit cycle (non-isolated singularities); (Theorem 1.3) every limit periodic set is homeomorphic to a compact connected semialgebraic set of dimension 0 or 1, and conversely every such semialgebraic set is realizable. This makes the Roussarie/DRR reduction's object (finite cyclicity of all limit periodic sets) well-defined and shows the degenerate case is real.
hypotheses: polynomial planar families (X_λ), λ in a real algebraic parameter manifold; Bendixson compactification to S^2; Hausdorff topology on compact sets.
holds-here: yes — this is the frame's foundation: the DRR 121-graphic program is the case-by-case analysis of the limit periodic sets of the quadratic family (source's own words).
status: asserted
evidence: full text held at research/sources/arxiv-1702.04965-panazzolo-rousseau-limit-periodic.full.md; Definition 1.1, Proposition 1.2, Theorem 1.3 verbatim at lines 28-70.
falsifier: a limit periodic set not homeomorphic to a compact connected semialgebraic 0/1-dimensional set, or a semialgebraic set not realizable — both contradicted by Theorem 1.3 as stated.
sources: https://arxiv.org/abs/1702.04965
anchor: research/sources/arxiv-1702.04965-panazzolo-rousseau-limit-periodic.full.md
follows-from:
answers:
```
