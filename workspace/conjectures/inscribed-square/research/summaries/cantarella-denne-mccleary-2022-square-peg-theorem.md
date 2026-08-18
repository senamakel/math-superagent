# Cantarella–Denne–McCleary 2022 — Configuration spaces, multijet transversality, and the square-peg problem

**Source:** Jason Cantarella, Elizabeth Denne, John McCleary, "Configuration spaces, multijet transversality, and the square-peg problem," Illinois Journal of Mathematics 66(2), 2022. DOI: 10.1215/00192082-10120454. Full text on disk is the arXiv preprint arXiv:1402.6174 (2014) at [[research/sources/cantarella-denne-mccleary-2022-square-peg-theorem.full.md]]; the paper's own authors' note states the preprint "will not be published in this form, but instead has been split into three separate papers." The published IJM paper is the version of record.

## Status of problem.md's "unconfirmed claim"

**RESOLVED — problem.md's flagged claim does not exist in the literature.** problem.md said "Cantarella–Denne–McCleary (2020 preprint) claims a proof of the full conjecture for every continuous Jordan curve." The actual paper proves **no such thing**:

> "there is a C¹-dense family of smooth embedded circles in the plane where each simple closed curve has an odd number of inscribed squares"

That is the paper's actual result — odd-number-of-squares for a *dense family of smooth curves* — plus analogous odd-count results for inscribed square-like quadrilaterals in Rⁿ and regular simplices in higher dimensions. It is a *genericity* theorem, not a full-conjecture proof, and it does not touch general continuous Jordan curves. The peer-reviewed version (Illinois J. Math., 2022) says the same. **The "unconfirmed full proof" hypothesis is closed: no such proof was published, and the paper that was published proves a strictly weaker, genericity-type statement.**

## What it establishes

- **Transversality lifting property (main theorem):** given a submanifold M ⊂ R^k, the configuration space C_n[M] can be made transverse to any submanifold Z ⊂ C_n[R^k] (boundary-disjoint case) by an arbitrarily C¹-small variation of M, via the multijet transversality theorem.
- **Square-peg application:** a C¹-dense family of smooth embedded circles in the plane each has an **odd number** of inscribed squares. Higher-dimensional analogues: dense families of embedded (n−1)-spheres in Rⁿ with inscribed regular n-simplices.
- **Key structural ingredients:** the square-like-quadrilateral submanifold Slq ⊂ C₄[Rᵏ] is orientable, with ∂Slq ⊂ ∂C₄[Rᵏ]; the cyclic-relabeling Z/4Z action is smooth and free; the Cayley–Menger theorem characterizes constructible simplex distance ratios; boundary-disjointness is what prevents the degenerate configurations from spoiling the intersection count.

## Why it matters here

- The method is the same configuration-space / parity family as Shnirelman–Stromquist, but recast in multijet transversality. It shows *generic* smooth curves have odd counts; it does **not** address curves that are not smooth, and it does **not** prove the full conjecture.
- The odd-count claim is a stronger structural statement than mere existence for the dense family — useful as an exact-arithmetic oracle check target (e.g., an ellipse has exactly 1 inscribed square, per the paper's Proposition 26; parallel chords of an ellipse meet midpoints on a diameter, Lemma 27).

## Claims

```claim
id: cdm2022-genericity-odd-squares
statement: There is a C¹-dense family of smooth embedded circles in the plane such that each curve in the family has an odd number of inscribed squares. (Peer-reviewed: Illinois J. Math. 2022.)
status: asserted-by-source
evidence: Cantarella–Denne–McCleary 2022 (published IJM); arXiv:1402.6174
holds-here: yes — the exact statement that resolves problem.md's "unconfirmed full proof" claim; the claim as problem.md framed it (full conjecture for all continuous curves) is NOT in this paper
falsifies: a published source showing CDM proved the full conjecture, or a counterexample curve in the dense family with an even number of inscribed squares
```

```claim
id: cdm2022-no-full-conjecture-proof
statement: No paper by Cantarella, Denne and McCleary proves the Square Peg Problem for every continuous Jordan curve; their published result is a genericity/odd-count statement for dense families of smooth curves.
status: sourced
evidence: authors' note in arXiv:1402.6174 (paper split into three), published abstract in Illinois J. Math. 66(2) 2022 (DOI 10.1215/00192082-10120454)
holds-here: closes problem.md's open item — treat the "2020 full proof" claim as not existing; the conjecture remains open
falsifies: location of a CDM paper proving the full conjecture for all continuous curves
```

```claim
id: cdm2022-ellipse-single-square
statement: A planar ellipse x²/a² + y²/b² = 1 with a² ≠ b² has a transverse intersection C⁰₄[γ] ⋔ Slq representing a single square.
status: asserted-by-source
evidence: CDM 2022 Proposition 26
holds-here: oracle test case — exact checker should find exactly one inscribed square on a non-circular ellipse
falsifies: an exact computation finding more than one inscribed square on a non-circular ellipse
```
