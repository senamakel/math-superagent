# Lovász number of vertex-transitive and regular graphs: eigenvalue formula

**Subject:** The source the adopted `lovasz-theta-vector-chromatic` approach
explicitly asks for ("theta has its vertex-transitive eigenvalue formula — source
before use"). For vertex-transitive (hence regular) graphs, ϑ is governed by the
eigenvalues, which is exactly the "closed-form exact computation" the run's
synthesis wants on its Eisenstein-lattice (triangular lattice) constructions.

## Source

- Galtman, *Spectral Characterizations of the Lovász Number and the Delsarte
  Number of a Graph*, J. Combin. Optim. (2000). DOI 10.1023/a:1026587926110.
  Retrieved via `exa_search` (research paper).
- Corroborating (SPECTRA of vertex-transitive graphs): Petersdorf–Sachs theorem
  and the convention `λ = k − 2α` for simple eigenvalues of k-regular
  vertex-transitive graphs (as restated in "Simple eigenvalues of cubic
  vertex-transitive graphs", Canad. J. Math. 2023).

## What it establishes

**Theta as a spectral SDP over weighted Laplacians.** Galtman shows that for the
complement, `ϑ(Ḡ)` can be written as
`1 + max over admissible weights W of 1/λ_max(L_W)` where `L_W` is a weighted
Laplacian (Fan Chung's). This turns ϑ into an eigenvalue-optimisation problem.

**Vertex-transitive case (why it matters here).** For vertex-transitive graphs,
symmetry collapses the weight optimisation: the optimal weight is constant /
symmetry-preserving, and ϑ is given by a closed eigenvalue expression depending
only on the spectrum. For the run this is the exact computational reward: the
triangular-lattice graph (Eisenstein integers Z[ω]) is vertex-transitive, so
ϑ(Ḡ) is an exact function of its adjacency eigenvalues, computable over the
cyclotomic field with DFT sums — no interior-point SDP needed.

**The general situation.** For graphs that are only regular (not vertex-
transitive), or 1-walk-regular / in homogeneous coherent configurations, the
plain eigenvalue formula does not in general reduce to `ϑ = 1 − λ_max/λ_min`;
that clean identity is specific to the strongly-regular / vertex-transitive /
association-scheme setting. The run must not assume the naive formula on an
arbitrary Minkowski sum; compute the SDP value directly there.

## Claim block

```claim
id: vertex-transitive-theta-eigenvalue
statement: For a vertex-transitive graph, the Lovász number ϑ(Ḡ) admits a closed
  spectral expression (optimise over symmetry-preserving weights in the weighted-
  Laplacian characterisation), computable exactly from the graph's eigenvalues;
  the simple formula ϑ ≈ 1 − λ_max/λ_min is specific to the strongly-regular /
  vertex-transitive / association-scheme setting and must not be assumed for
  arbitrary (e.g. Minkowski-sum) unit-distance graphs.
hypotheses: G vertex-transitive (hence regular); the weighted-Laplacian
  characterisation of ϑ (Galtman 2000).
holds-here: YES for the run's triangular-lattice / Eisenstein-integer
  constructions (vertex-transitive ⇒ exact spectral ϑ over the cyclotomic field);
  NOT for arbitrary Minkowski sums (compute the SDP value directly there).
status: asserted-by-source (Galtman 2000 primary; Petersdorf–Sachs for the
  spectral convention; not re-derived here).
bearing: fixes whether the adopted approach's "closed-form exact computation" is
  legitimate — it is, on vertex-transitive constructions, and not on general sums.
anchor: research/sources/vertex-transitive-lovasz-theta-formula.md
falsifies: a vertex-transitive graph whose ϑ differs from its spectral formula —
  would contradict Galtman; the run's safeguard is to never assume the naive
  formula off the vertex-transitive / association-scheme class.
```

## Status

Recorded by the librarian as a primary source note. `asserted-by-source`, not
machine-checked here; applying it to an Eisenstein-lattice disk/torus is the run's
own exact computation.
