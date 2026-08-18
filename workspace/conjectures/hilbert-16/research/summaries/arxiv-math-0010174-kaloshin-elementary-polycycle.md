# Kaloshin 2000/2003 — estimate for cyclicity of an elementary polycycle

Full text: [[arxiv-math-0010174-kaloshin-elementary-polycycle.full]]
(arXiv:math/0010174, lecture notes) and [[primary-kaloshin-elementary-polycycles.html.full]].
Published: V. A. Kaloshin, "The Existential Hilbert 16-th problem and an estimate for
cyclicity of elementary polycycles", Invent. Math. 151 (2003) 451–512.

## What the source establishes (held full text, verbatim)

**E(k) ≤ 2^{25k²}** (equation (1.5), held full text line 149). This is the first
explicit general estimate for cyclicity of an elementary polycycle in a generic
k-parameter family: the bifurcation number B(k) — maximal cyclicity of a nontrivial
polycycle occurring in a generic k-parameter family — is finite and bounded by the
double-exponential-type shape in k.

**Context it supplies (definitions that the run's frame uses):**
- The **Hilbert–Arnold Problem (HAP)**: prove that in a generic finite-parameter family
  of vector fields on S² with compact base B, the number of limit cycles is uniformly
  bounded. Solved under the elementary-singularities assumption (line 99: "any generic
  finite parameter family ... with only elementary singularities has a uniform upper
  bound for the number of limit cycles").
- The **Global Finiteness Conjecture (GFC)** [Roussarie]: for any family of line fields
  on S² with compact parameter base, the number of limit cycles is uniformly bounded.
  This is the exact conjecture Roussarie's reduction to finite cyclicity serves, and it
  is what H(2)<∞ would discharge for the quadratic family.
- The **individual finiteness theorem** (IFT, Ilyashenko–Écalle) is the pointwise pillar;
  the HAP/GFC is the uniform pillar. Kaloshin's own route is an independent proof of the
  Ilyashenko–Yakovenko finiteness theorem for elementary polycycles.

**What it does NOT cover:** nonelementary polycycles. The source explicitly says
extending (1.5) to generic nonelementary polycycles needs a Desingularization Theorem
for families of generic C^∞ vector fields (Denkowska–Roussarie, Trifonov approaches),
and that singular perturbation (curves of equilibria after blow-up) is the phenomenon
that appears. This is exactly the DRR degenerate-graphics obstruction.

## What it lets this run conclude

- The elementary-polycycle restricted class (ROOT.md row 1) is anchored with the exact
  constant 2^{25k²}, verified verbatim in the held full text. The `E(k)≤2^(25 k^2)`
  ROOT.md citation is CORRECT.
- It is the precedent for the run's `compensator-pfaffian-mourtada-moussu-synthesis`
  and `pfaffian-chain-return-map` approaches: the diagnostic is to prove a uniform
  Pfaffian-chain representation of the displacement including all parameter-dependent
  exponents and passages; without it, no bound for an open graphic.
- It confirms the separation drawn in ROOT.md and in `h16-drr-121-graphics`: elementary
  = settled (Mourtada, IY, Kaloshin, Kaleda–Shchurov); nilpotent/degenerate = the open
  content.

```claim
id: h16-kaloshin-elementary-polycycle-bound
statement: In a generic k-parameter family of C^infty planar (or S^2) vector fields, the cyclicity E(k) of an elementary polycycle is at most 2^{25k^2} (Kaloshin, equation (1.5)). More precisely the bifurcation number B(k), the maximal cyclicity of a nontrivial polycycle in a generic k-parameter family, satisfies this bound; the Hilbert–Arnold problem is solved for generic families with only elementary singularities.
hypotheses: generic k-parameter family; all singular points elementary (nonzero eigenvalues); polycycle (compact invariant graph of the singular foliation).
holds-here: yes — restricted class; the open DRR graphics are non-elementary so this does not close them.
status: asserted
evidence: held full text verbatim (research/sources/primary-kaloshin-elementary-polycycles.html.full.md line 149: "E(k) ≤ 2^{25k²}"); lecture notes arXiv:math/0010174.
falsifier: a counterexample elementary polycycle in a generic k-parameter family with cyclicity exceeding 2^{25k²}, or a correction to the paper.
sources: https://arxiv.org/abs/math/0010174 ; https://doi.org/10.1007/s00222-002-0244-9
anchor: research/sources/primary-kaloshin-elementary-polycycles.html.full.md
follows-from:
answers:
```
