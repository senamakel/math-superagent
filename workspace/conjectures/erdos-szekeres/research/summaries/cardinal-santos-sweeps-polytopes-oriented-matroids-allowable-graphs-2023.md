# Cardinal & Santos, "Sweeps, Polytopes, Oriented Matroids, and Allowable Graphs of Permutations" (Combinatorica 2023)

<!-- source: https://link.springer.com/article/10.1007/s00493-023-00062-3 | full text at research/sources/cardinal-santos-sweeps-polytopes-oriented-matroids-allowable-graphs-2023.full.md -->

**Publication.** Jean Cardinal and Francisco Santos, *Combinatorica* 44 (2024) 63–123 (open access, published online Oct 2023). DOI 10.1007/s00493-023-00062-3.

## What it establishes

A **sweep** of a point configuration is any ordered partition induced by a linear functional (the order in which the points are hit by a sweeping line/hyperplane orthogonal to a direction). For planar configurations the family of all sweeps is the **allowable sequence of permutations** of Goodman and Pollack. This paper lifts the theory to higher dimension via two generalizations:

1. **Sweep polytopes.** The poset of sweeps of a configuration is realized as the face poset of a *sweep polytope* — a projection of the permutahedron. Sweeps are in bijection with faces of the sweep polytope.
2. **Sweep oriented matroids** — strong maps of the braid oriented matroid. Allowable sequences are exactly the sweep oriented matroids of rank 2, and many of their properties (sweep acycloids, cellular strings, monotone paths) extend to higher rank. They relate to modular hyperplanes and Dilworth truncations.
3. **Allowable graphs of permutations.** Symmetric sets of permutations connected by allowable sequences, forming acycloids; gives characterizations (da Silva, Handa's) for which allowable graphs arise from sweep oriented matroids.

## Relevance to this problem

- This is a **framework / vocabulary** source, not a bound on ES(n). It confirms that the 2D allowable (circular) sequence the run computes is the rank-2 sweep-OM case, and that the rotating-direction sweep generating it is the standard object. It does **not** carry the ES upper bound or the exact `2^{n-2}+1` constant.
- The monotone-path/shadow-vertex material (vertices extreme in directions `w + λu` along a projection) is the higher-dimensional analogue of the pointwise extreme-in-projection criterion; it broadly reinforces the EPS (extreme-in-projection = hull vertex) view the allowable-sequence thread uses, but does **not** state the 2D hull-vertex characterization in the clean `Prop 3.17` form — that is held in the Gärtner course notes.
- Because the conjecture is an *exact* constant question and this paper is asymptotic/generalizational, the run should treat it as context: the sweep-polytope viewpoint is a candidate reformulation vocabulary, not an immediate tool. Record as framework only.

**Not load-bearing for this run.** It generalizes rather than specializes to the exact `ES(n)=2^{n-2}+1`. Use it if a sweep/allowable-graph reformulation of extremal sets is pursued; do not treat its results as bearing on the exact conjecture.
