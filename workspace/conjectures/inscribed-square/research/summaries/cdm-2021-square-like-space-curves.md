# CDM 2021 — Square-like quadrilaterals inscribed in embedded space curves

**Source:** Jason Cantarella, Elizabeth Denne, John McCleary, "Square-like quadrilaterals inscribed in embedded space curves," arXiv:2103.13848 [math.DG], 25 Mar 2021. Full text: `research/sources/cdm-2021-square-like-space-curves.full.md`.

## What it establishes

A generalization of the square-peg problem to embedded curves in Rⁿ: does every embedding γ : S¹ ↪ Rⁿ contain an inscribed **square-like quadrilateral** — four points forming a planar quadrilateral with equal sides and equal diagonals (the planar case reduces exactly to an inscribed square)?

**The main regularity class: FTCWC — finite total curvature without cusps.**

- **Theorem 11.** If γ : S¹ ↪ Rⁿ is an embedding in FTCWC, then γ has an inscribed square-like quadrilateral.
- **Corollary 12.** Every C²-smooth embedding S¹ ↪ Rⁿ has an inscribed square-like quadrilateral.

**The mechanism — this is the paper's real contribution to this run's core question:**

- **Lemma 6.** Any square-like quadrilateral pqrs has total curvature κ(σ_pqrs) ≥ π, with equality iff pqrs is a planar square. (σ_pqrs is the closed curve formed by the four edges.)
- **Lemma 8.** Any square-like quadrilateral inscribed in an FTC curve γ has side length ≥ π-d(γ) — where d(γ) is a positive constant measuring how much the total curvature of γ falls short of the "square-like" threshold along short arcs. **This is a genuine side-length lower bound, an explicit anti-shrinkout scale certificate.**
- **Lemma 9.** If γ is embedded and in FTCWC, then π-d(γ) > 0 — the lower bound is strictly positive for the whole class.
- **Proposition 10 (stability).** If γᵢ → γ uniformly in position, arclength, and total curvature, and π-d(γ) > 0, then liminf π-d(γᵢ) > 0 — the scale certificate survives approximation.
- **Proposition 5.** Any FTC curve is approximable in position, arclength, and total curvature by smooth FTC curves.

**Theorem 3** (citing Theorem 35 of the CDM configuration-spaces paper): a C^∞-open neighborhood of any smooth embedding contains, for all m, a C^m-dense set of smooth embeddings each with an odd finite set of inscribed square-like quadrilaterals.

## Why it matters for this run

1. **The anti-shrinkout mechanism, stated as an explicit bound.** Lemma 8's side-length lower bound π-d(γ) is exactly the kind of scale certificate ROOT.md says any honest extension of the rectifiable theorem must supply (like Matschke's √2 in the annulus, Rifford's C·max(g−f), the Legendrian-lift scale). Here the certificate comes from **total curvature**: the class FTCWC is defined so that short arcs have small curvature, which rules out small squares directly. This is a *different* regularity handle than local monotonicity, rectifiability, or Legendrian lifts — curvature-based rather than metric/contact-based.
2. **The authors state the obstruction explicitly.** The introduction (p.2) says: "The problem is clear: The sequence of square-like quadrilaterals on the approximating curves may have sidelengths approaching zero. If one could construct a general lower bound on these sidelengths in terms of the global geometry of the curves... this possibility could be ruled out. We do not know of any explicit example of a family of curves where all the inscribed square-like quadrilaterals have sidelengths converging to zero, so this approach may yet be possible. However, this line of attack has been more or less obvious from the start, and nobody has managed to construct such an argument in the past century." — a source-backed statement that shrinkout is real, unexemplified, and the century-old blocker.
3. **Where it does not reach.** FTCWC is a strict regularity class (bounded total curvature, no cusps). A nowhere-differentiable Jordan curve has infinite total curvature and is outside it. So it does not touch the general conjecture — but it is a *fourth named anti-shrinkout device* in the library, and it shows the obstruction is attacked from several independent directions.
4. **The space-curve generalization.** The same school (CDM) as the configuration-spaces/odd-count paper already in the library; the two papers share Theorem 35 (dense family of C∞ embeddings each with an odd finite set of inscribed square-like quadrilaterals). It confirms the configuration-space method extends to Rⁿ square-like quadrilaterals, while the planar square problem remains open.

## Claim blocks

```claim
id: cdm2021-square-like-space-curves-FTCWC
statement: Every embedding γ : S¹ ↪ Rⁿ of finite total curvature without cusps (FTCWC) has an inscribed square-like quadrilateral (four points forming equal-side equal-diagonal planar quadrilateral); in particular every C²-smooth embedded circle in Rⁿ does.
hypotheses: γ : S¹ ↪ Rⁿ embedding, FTCWC (finite total curvature, no cusps).
holds-here: yes — a positive result for a named regularity class, strictly inside the open frontier; the planar square case is the n=2 instance.
evidence: full text verified (arXiv:2103.13848, Theorems 11, Corollary 12).
status: theorem (arXiv preprint; peer-review status not confirmed by this library)
falsifies: an FTCWC embedding without an inscribed square-like quadrilateral; or a published error in the total-curvature argument.
```

```claim
id: cdm2021-curvature-scale-certificate
statement: In an FTCWC embedding γ, every inscribed square-like quadrilateral has side length ≥ π−d(γ) > 0, where d(γ) is a total-curvature-derived positive constant; the bound is stable under approximation in position/arclength/total curvature.
hypotheses: γ embedded FTCWC.
holds-here: yes — the fourth named anti-shrinkout scale certificate in the library (after Stromquist's µ, Matschke's √2, Rifford's C·max(g−f), the Legendrian-lift scale); curvature-based rather than metric/contact-based.
evidence: full text verified (arXiv:2103.13848, Lemmas 6–9, Proposition 10).
status: theorem (arXiv preprint)
falsifies: an FTCWC curve with an inscribed square-like quadrilateral of side < π−d(γ); or a published error in Lemma 8's derivation.
```

```claim
id: cdm2021-shrinkout-unexemplified-source-statement
statement: CDM 2021 state (p.2) that no explicit example is known of a family of curves whose inscribed square-like quadrilaterals all have sidelengths converging to zero, and that no one has constructed a general lower-bound argument in the past century; their FTCWC result rules out small squares using local (curvature) rather than global data.
hypotheses: none — a source statement about the state of the shrinkout obstruction.
holds-here: yes — the library's strongest source-backed statement that shrinkout is real, unexemplified, and the century-old blocker; any claimed counterexample or full proof must be read against it.
evidence: full text verified (arXiv:2103.13848, introduction p.2, verbatim).
status: sourced claim (authors' own statement about the literature)
falsifies: a published explicit example of a family of curves where all inscribed square-like quadrilaterals shrink to points; or a general side-length lower bound for arbitrary C⁰ curves.
```

```claim
id: cdm2021-FTCWC-does-not-cover-wild-curves
statement: The FTCWC class (finite total curvature without cusps) is a strict regularity class; nowhere-differentiable Jordan curves have infinite total curvature and lie outside it, so this result does not touch the general Toeplitz conjecture.
hypotheses: none — a scope statement.
holds-here: yes — prevents over-claiming the CDM 2021 result as progress on the open case.
evidence: class definition and total-curvature finiteness in the full text; standard fact that wild curves have unbounded variation of the tangent.
status: derived observation (from verified source)
falsifies: an FTCWC definition that includes nowhere-differentiable curves.
```
