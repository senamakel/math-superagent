# Circularly chainable continua that annularly inscribe squares (Morales-Fuentes–Villanueva-Segovia 2025)

**Source:** Ulises Morales-Fuentes, Cristina Villanueva-Segovia, Topology and its Applications 368 (2025), 109379. DOI: 10.1016/j.topol.2025.109379.

**Record:** `research/summaries/citations_w4408904160.md` (citation-graph entry with abstract; full text paywalled at Elsevier, download converted to 112 bytes of navigation HTML and was not usable).

## What it establishes (from the published abstract)

Let A denote the annulus {x ∈ R² : 1 ≤ ||x|| ≤ 1+√2}. Then:

1. **Main theorem:** If X is a circularly chainable continuum essentially embedded in A, then X contains the four vertices of a Euclidean square of side length at least √2.
2. **Annular inscription property:** A plane continuum X satisfies the annular inscription property in A if every essentially embedded image of X in A admits an inscribed square of side at least √2. Every circularly chainable, not chainable plane continuum satisfies this property in A.
3. **Genericity:** The annular inscription property in A is generic among continua that separate the plane.

## Why it matters here

- **Circularly chainable continua are genuinely wild objects** — they include the pseudo-circle, solenoids, and circle-like continua, which are hereditarily indecomposable, non-rectifiable, fractal-like continua. They are exactly the kind of object the minimal-counterexample analysis says must be a square-peg counterexample (non-rectifiable, non-locally-monotone, outside all curve-class positive theorems).
- **This is a positive result for a class of wild continua** — but with a crucial caveat: the continuum must be *essentially embedded in the annulus* (winding around the hole), and the conclusion is a square of side ≥ √2. The annulus geometry pins a positive scale, exactly as in Matschke's annulus theorem (Thm 1.3: continuous curve in the annulus, nontrivial in π₁, inscribes a square of side ≥ √2). This is the same nondegeneracy mechanism: homotopy class + annular geometry prevents shrinkout.
- **Genericity statement:** the property is generic among plane-separating continua — evidence that "most" wild continua (in the Baire-category sense) inscribe squares, consistent with Matschke's open-dense-class result for curves.
- **Boundary of the result:** it does NOT cover circularly chainable continua whose embeddings are not annular (e.g., embedding the pseudo-circle as a thin, non-annular set, where no positive scale is pinned). That is precisely the shrinkout scenario the minimal-counterexample analysis flags.

## Claims

```claim
id: morales-villanueva-2025-annular-square
statement: If X is a circularly chainable continuum essentially embedded in the annulus {1 ≤ ||x|| ≤ 1+√2}, then X contains the four vertices of a Euclidean square of side length at least √2. Every circularly chainable, not chainable plane continuum has the annular inscription property in this annulus; the property is generic among continua separating the plane.
status: asserted-by-source
evidence: Morales-Fuentes–Villanueva-Segovia 2025, Topology and its Applications 368, 109379 (published abstract via citation graph; full text paywalled)
holds-here: yes — a positive result for wild non-rectifiable continua (pseudo-circle, solenoids) when annular; pins side ≥ √2, preventing shrinkout; does not cover non-annular embeddings, the shrinkout scenario
falsifies: a circularly chainable continuum essentially embedded in the annulus with no inscribed square of side ≥ √2
```
