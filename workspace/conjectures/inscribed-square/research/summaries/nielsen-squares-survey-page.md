# Figures Inscribed in Curves — A short tour of an old problem (Nielsen, University of Idaho)

**Source:** Mark J. Nielsen (University of Idaho), "Figures Inscribed in Curves: A short tour of an old problem" — an informal survey webpage, archived 2024.  
**URL:** https://web.archive.org/web/2024/https://www.webpages.uidaho.edu/~markn/squares/  
**Full text:** `research/sources/nielsen-squares-survey-page.full.md`

## What it establishes (informal survey, not a primary source)

This is an encyclopedic-style introduction by a researcher (Mark Nielsen, co-author of the Nielsen–Wright symmetric-continua rectangle theorem) to the inscribed squares problem. It fixes the statement in accessible terms and documents the "range of ignorance":

- **Statement:** does every simple closed curve have an inscribed square? (Vertices on the curve; no requirement on the square's interior or on vertex order.)
- **Two extreme possibilities neither ruled out:** (1) every closed and bounded set separating the plane into more than one piece contains the four vertices of a square; (2) most simple closed curves (in a Baire-category sense) do NOT have inscribed squares. The fact that even the extremal possibility (2) is not ruled out shows how little is known about the general case.
- **Stromquist's theorem (the best result):** if the simple closed curve J is "nice enough" — for each point P on the curve there is a coordinate system in which some piece of the curve containing P is the graph y = f(x) of a continuous function — then J has an inscribed square. This is the graph-theoretic formulation of local monotonicity, matching the primary abstract.
- **Prior results:** all polygons, differentiable curves, and convex curves inscribe squares.
- Includes links to six theorems (theorem A etc.) illustrating different approaches and symmetry-based variants.

## Why it matters here

- This is the "problem-collection page" tier of the library: it fixes the statement, the two extreme possibilities (useful for calibrating what a minimal counterexample must look like — under possibility 2, most curves lack squares; under possibility 1, even continua separating the plane suffice), and confirms the graph-theoretic reading of Stromquist's local monotonicity.
- **The graph formulation is the version the Lean formalization should use:** a curve is locally monotone iff every point has a neighborhood that is the graph of a continuous function in some coordinate system. This is equivalent to the linear-functional definition and is easier to state formally.
- The page is informal (a professor's course-adjacent page), so nothing here is load-bearing by itself; its value is the canonical statement and the enumeration of the field's ignorance.

## Claims

```claim
id: nielsen-survey-stromquist-graph-formulation
statement: Stromquist's theorem: if a simple closed curve J is such that for each point P on it there is a coordinate system in which some piece of the curve containing P is the graph y = f(x) of a continuous function, then J has an inscribed square.
status: asserted-by-source
evidence: Nielsen survey page (archived 2024), citing Stromquist 1989, Mathematika 36, 187–197; corroborated by the Cambridge abstract of Stromquist 1989 (weaker condition satisfied by convex, polygonal, piecewise C¹ curves)
holds-here: yes — the graph formulation of local monotonicity; this is the version to use in the Lean statement of Stromquist's theorem
falsifies: a published example of a curve locally representable as continuous-function graphs with no inscribed square
```

```claim
id: nielsen-survey-range-of-ignorance
statement: Neither of the two extreme possibilities is ruled out: (1) every closed bounded set separating the plane contains a square's vertices; (2) most (Baire-generic) simple closed curves have no inscribed square. The problem has resisted all approaches since 1911.
status: asserted-by-source
evidence: Nielsen survey page (archived 2024); consistent with Matschke 2014 survey (open status) and GL 2026 (only a positive-measure rectangle result for general curves)
holds-here: yes — calibrates the minimal-counterexample structure: the field cannot even rule out that a counterexample is Baire-generic
falsifies: a proof that all plane-separating closed sets contain square vertices, or a proof that Baire-generic curves lack squares (either would be a major result in itself)
```
