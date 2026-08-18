# van Heijst 2014 — The algebraic square peg problem (Master's thesis, Aalto)

**Source:** Wouter van Heijst, "The algebraic square peg problem," Master's thesis in mathematics, Aalto University, March 2014. arXiv:1403.5979 [math.AG]. Full text: `research/sources/vanheijst-2014-algebraic-square-peg.full.md`.

**Status: verified against full text on disk. Thesis (not peer-reviewed journal), but contains the results referenced in the Notices of the AMS April 2014, p. 349 (Matschke's survey).**

## What it establishes

**Theorem 4.8 (main result).** An algebraic plane curve of degree m (defined by the vanishing of a polynomial in two variables) inscribes at most **(m⁴ − 5m² + 4m)/4** isolated squares.

The proof casts the set of inscribed squares as a variety: parametrize a complex square by its center (a,b) and offset (c,d) — corners (a,b)+(c,d), (a,b)+(−d,c), (a,b)+(−c,−d), (a,b)+(d,−c) — evaluate the defining polynomial f at the four corners to get the "corner ideal," apply **Bernshtein's Theorem** (mixed volume of Newton polytopes) with a clever choice of generators to get the bound, which beats Bézout's naive bound.

- Section 5: experimental evidence (computer algebra) that the bound is **sharp for generic complex algebraic plane curves**.
- Section 6: real algebraic plane curves of degrees 3–8 inscribing various numbers of squares; **a real algebraic curve homeomorphic to the real line conjectured to inscribe an even number of squares** (one of three conjectures in Section 7).
- Context: Eggleston's example — the conjecture fails for regular polygons with > 4 vertices (a convex curve inscribing no regular n-gon, n ≥ 5); Nielsen: every Jordan curve inscribes a triangle; Vaughan: every Jordan curve inscribes a rectangle (no aspect-ratio control).

## Why it matters for this run

The algebraic/counting angle is a genuinely distinct attack surface from the topological Mobius-band parity argument: instead of proving existence by parity, it bounds the *number* of squares on a curve from a polynomial equation. The sharpness-for-generic-complex-curves evidence and the real-curve parity conjectures connect back to the odd-count mechanism (Emch/Jerrard/Stromquist) but for algebraic curves the parity may be even (conjecture) — a possible *counterpoint* to the parity-obstruction intuition.

## Claim blocks

```claim
id: vanheijst2014-algebraic-counting-bound
statement: An algebraic plane curve of degree m inscribes at most (m⁴ − 5m² + 4m)/4 isolated squares.
hypotheses: plane curve defined by polynomial f of degree m (complex or real); counting isolated inscribed squares.
holds-here: algebraic curves — a counting/upper-bound result, not the continuous Jordan-curve existence question.
evidence: full text verified (arXiv:1403.5979); Bernshtein's theorem, mixed volume.
status: theorem (Master's thesis; main result also announced in Matschke's Notices survey p. 349)
falsifies: an algebraic plane curve of degree m with more than (m⁴−5m²+4m)/4 isolated inscribed squares.
```

```claim
id: vanheijst2014-regular-polygon-counterexample
statement: The conjecture does not hold if squares are replaced by regular polygons with more than four vertices: Eggleston gave a convex curve inscribing no regular polygon with more than four vertices.
hypotheses: convex curve; regular n-gon, n ≥ 5.
holds-here: marks the boundary of "inscribed regular polygon" results — squares are special.
evidence: van Heijst 2014 (citing Eggleston).
status: sourced claim (secondary; primary Eggleston not in library)
falsifies: a convex curve inscribing every regular n-gon for n ≥ 5.
```

## Relation to existing library

- New angle: **algebraic counting** — the library previously covered topological (Möbius-band parity, Vrećica–Živaljević cyclohedra), analytic (Tao integrals), symplectic (Greene–Lobb, Hugelmeyer, Asano–Ike), and discrete (Pettersson–Tverberg–Östergård) approaches. This adds algebraic-geometric counting with an explicit upper bound that is *verifiable by exact computation* — relevant to the run's oracle (GOAL.md criterion: exact verification, never floating-point).
- Complements the CDM odd-count result (odd number for a C¹-dense family of smooth curves; ellipse exactly one): for *algebraic* curves the count can be bounded above exactly, and the real-line case may be even.
