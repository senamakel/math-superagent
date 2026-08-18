# Matschke 2009 — On the Square Peg Problem and some Relatives

**Source:** Benjamin Matschke, "On the Square Peg Problem and some Relatives," arXiv:1001.0186 (2009). Full text at [[research/sources/matschke2009-square-peg-relatives.full.md]].

## What it establishes

Proves the Square Peg Problem for the **largest known class of curves at the time**, an explicit **open and dense** neighborhood of Stromquist's locally monotone curves in the C⁰ topology:

- **Theorem 1.4:** The Square Peg Problem holds for all curves in an explicit open and dense neighborhood of Stromquist's locally monotone curves in the space of injective maps S¹ → R² with the C⁰ topology. Interpreted: *any generic Jordan curve inscribes a square.*
- **Corollary 2.10 / 2.12:** if there is ε ∈ (0,1) such that γ inscribes no (or generically an even number of) *special trapezoid of size ε*, then γ has an inscribed square; this class is an open and dense neighborhood of Stromquist's class.
- **Theorem 1.3 / 2.3 / 2.4 (quantitative continuous-curve results):** curves in annuli (e.g., A = {1 ≤ ||x|| ≤ 1+√2}, or the square annulus [−3,3]²\(−1,1)², or a triangle-annulus) that are homotopically nontrivial inscribe a square of side length at least √2 (or 2√3−3). These are genuine *continuous*-curve results with explicit lower bounds — the bound rules out shrinkout by construction.
- **Theorem 2.8/2.9 (mod-2 intersection formulation):** the square-peg question reduces to a mod-2 intersection number i(S, P₄(ω)) in the configuration space; if γ does not inscribe a square then this number is well-defined and equals 1; conversely, if P₄(ω) ∩ S = ∅ then γ has an inscribed square.
- **Rectangular Peg (Theorem 1.5):** C∞ curves with angular convexity at most 60° inscribe a rectangle of aspect ratio √3.
- **Higher dimensions:** the regular-octahedron-on-metric-2-spheres problem has a "topological counter-example" (a test map with boundary condition exists), blocking the straightforward higher-dimensional analogue.
- Presents the modern Shnirelman argument (bordism form) for smooth curves, and the configuration-space parameterization of polygons on a curve (Section 2).

## Why it matters here

- This is the **technical engine** behind the survey's Theorem 4 and the open-dense class. The special-trapezoid criterion (Corollary 2.10) is the cleanest structural statement for a run to formalize: it is a *finite-scale* condition (no special trapezoid of size ε) that forces an inscribed square — no limiting argument needed.
- The annulus theorems are the natural **oracle test targets**: they are existence statements for continuous curves with explicit side-length lower bounds, so an exact checker can verify the side length is not degenerate.
- The mod-2 intersection formulation (Theorem 2.8) is the parity claim at the heart of the Mobius-band method, in its most explicit form.

## Claims

```claim
id: matschke2009-open-dense-class
statement: There is an explicit open and dense neighborhood of Stromquist's locally monotone curves in the C⁰ topology on injective maps S¹ → R² such that every curve in it inscribes a square.
status: asserted-by-source
evidence: Matschke, arXiv:1001.0186, Theorem 1.4
holds-here: yes — the largest-class result; strictly generalizes locally monotone
falsifies: a curve in the open-dense class with no inscribed square; or a published correction
```

```claim
id: matschke2009-special-trapezoid-criterion
statement: If a Jordan curve γ inscribes no special trapezoid of size ε (0 < ε < 1), or generically an even number, then γ inscribes a square.
status: asserted-by-source
evidence: Matschke, arXiv:1001.0186, Corollary 2.10
holds-here: yes — the finite-scale structural criterion; candidate for Lean formalization (it has no limiting step)
falsifies: a Jordan curve with no special trapezoid of size ε and no inscribed square
```

```claim
id: matschke2009-special-trapezoid-criterion-formalisation
statement: The abstract logical schema of Matschke's special-trapezoid criterion is encoded in Lean: for a Jordan curve γ, rational ε with 0 < ε < 1, and special-trapezoid count either zero or an even natural number, InscribesSquare γ follows.
status: conditional
evidence: Kernel check passed; the implication is stated as Cited.special_trapezoid_criterion, relying on Matschke Corollary 2.10/2.12 as a cited axiom.
formalisation: code/lean/matschke2009_special_trapezoid_criterion-4ca30655.lean
holds-here: yes as an abstract schema; geometric definitions remain unformalized.
falsifies: A mismatch between the abstract predicates/count convention and Corollary 2.10/2.12, or a counterexample to the cited theorem.
```

```claim
id: matschke2009-annulus-quantitative
statement: A continuous closed curve in the annulus {1 ≤ ||x|| ≤ 1+√2} that is homotopically nontrivial inscribes a square of side length at least √2.
status: asserted-by-source
evidence: Matschke, arXiv:1001.0186, Theorem 1.3 (also in the 2014 survey as Theorem 5)
holds-here: yes — quantitative continuous-curve result; ideal oracle/verification target (nondegenerate by construction)
falsifies: a continuous curve in the annulus, nontrivial in π1, with no square of side ≥ √2
```

```claim
id: matschke2009-mod2-intersection
statement: If γ does not inscribe a square, then the mod-2 intersection number i(S, P₄(ω)) is well-defined and equals 1, for any path ω representing a generator of π1((S¹)²\Δ(S¹)²) ≅ Z.
status: asserted-by-source
evidence: Matschke, arXiv:1001.0186, Theorem 2.8
holds-here: yes — the explicit parity statement at the core of the Mobius-band method
falsifies: a square-free Jordan curve for which the intersection number is 0 or ill-defined
```

```claim
id: griffiths1991-rectangle-proof-error
statement: Griffiths 1991's proof of the Rectangular Peg Problem contains an error in the calculation of intersection numbers/orientations; the standard configuration-space/test-map scheme fails for rectangles because the test map exists (generically zero oriented rectangles).
status: asserted-by-source
evidence: Matschke 2009 §1, §4; error per Matschke's thesis [26, Chap. III.7]
holds-here: yes — Ruled out: do not re-attempt the Griffiths route; the orientation-counting obstruction is documented
falsifies: a published correction showing Griffiths's calculation was sound
```


