# de Bruijn–Erdős theorem (1951): chromatic number of infinite graphs

**Subject:** The reduction that makes the whole infinite problem a finite-object
lower-bound question. Task input to `problem.md`; here sourced.

## Source
- **Original paper:** N.G. de Bruijn, P. Erdős, *A Colour Problem for Infinite
  Graphs and a Problem in the Theory of Relations*, Indagationes Mathematicae
  (Proceedings) **54** (1951), 371–373. DOI: 10.1016/S1385-7258(51)50053-7.
  Obtained as a search/synthesis summary, not as verbatim full text (network
  boundary blocks direct publisher fetch).
- Supporting treatments surfaced by search: P. Komjáth, *The chromatic number
  of infinite graphs — A survey*, Discrete Mathematics (2010), DOI
  10.1016/j.disc.2010.11.004; R. Diestel, *Graph Theory* (Springer), chapter
  on infinite graphs; Erné (1997) *Prime Ideal Theorems and systems of finite
  character*, and the thesis *Topology and Infinite Graphs* (Lowery 2009)
  which gives four compactness proofs.

## What it establishes
Let `G` be any (finite or infinite) simple graph. Then

    chi(G) = sup { chi(H) : H a finite subgraph of G }.

Equivalently: if every finite subgraph of `G` is `k`-colourable then `G` itself
is `k`-colourable.

Two direction:
- `chi(G) >= sup`: trivial, a `k`-colouring of `G` restricts to subgraphs.
- `chi(G) <= sup`: compactness. If every finite subgraph is `k`-colourable then
  a global `k`-colouring exists. Classical proofs use Tychonoff's theorem on a
  product of finite discrete colour spaces, Rado's selection lemma, Zorn's
  lemma / ultrafilters, or the Boolean Prime Ideal Theorem (BPIT).

## Axiom-of-choice / compactness hypothesis
- Sources agree the theorem holds in ZF for the *finite chromatic values*
  (no full AC needed); the extension step is a compactness principle. Lowery
  gives four proofs, all compactness-based; Erné shows the n-colouring theorem
  follows from the Intersection Lemma / Finite Cutset Lemma which in ZF are
  equivalent to the Boolean Prime Ideal Theorem. So the honest statement: the
  finite-to-infinite extension needs a choice/compactness principle (BPIT),
  which is weaker than AC and valid in ZFC.
- For the plane graph, vertices = all of R^2, edges = pairs at distance 1, the
  theorem applies directly: `chi(plane graph) >= k` iff some **finite**
  subgraph has `chi >= k`. `chi >= 5` is exactly the existence of a finite
  unit-distance graph not `4`-colourable.

## Claim block
```claim
id: debruijn-erdos-1951
statement: For any graph G, chi(G) = sup { chi(H) : H finite subgraph of G }.
hypotheses: G any simple graph; the finite-to-infinite step uses a compactness
  / BPIT / choice principle (valid in ZFC; not needed for the sup direction).
holds-here: YES — applies verbatim to the plane unit-distance graph, so
  chi(plane) >= 5 iff some finite unit-distance graph is not 4-colourable.
status: asserted-by-source (1951 paper; textbook treatments).
bearing: turns the whole infinite upper/lower bounds into finite-object
  questions; the run's lower-bound target is a finite not-4-colourable
  unit-distance graph.
anchor: research/sources/debruijn-erdos-1951-chromatic-reduction.md
falsifies: a compactness-free counterexample (finite subgraphs k-colourable but
  graph not) — none known; theorem is classical and correct.
```
