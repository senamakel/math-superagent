# Koolen, Cao, Yang — "Recent progress on graphs with fixed smallest eigenvalue" (arXiv:2011.11935)

<!-- source: https://arxiv.org/pdf/2011.11935 | converted from PDF -->

**Full text:** `research/sources/koolen-cao-yang-smallest-eigenvalue-survey.full.md`

## What it is
A 2021 survey of the classification programme for graphs with a fixed smallest
eigenvalue, concentrating on two parts:
(i) **Hoffman graphs** — basic theory and applications to graphs with fixed
    smallest eigenvalue and large minimal valency;
(ii) **distance-regular and co-edge-regular graphs** with fixed smallest
    eigenvalue, and characterizations of families of distance-regular graphs.
Also discusses signed graphs with fixed smallest eigenvalue at the end.

## Statements it makes (most relevant to this run)
- **Theorem 2.1 (cf. Cameron–Goethals–Seidel–Shult lineage):** if a connected
  graph has smallest eigenvalue ≥ −2 it is a generalized line graph (and
  conversely, line graphs have smallest eigenvalue ≥ −2). This is the −2
  classification that gates the −4 programme's contrast.
- **Hoﬀman-graph framework (Prop 3.9, Lemma 3.12, Theorems 3.17-3.20):**
  line-graph-style characterizations via {h₂,h₃,h₅}-line Hoﬀman graphs; a graph
  of order n is a line graph iff its edge-set can be partitioned into cliques
  meeting in at most one vertex (the Beineke/Krausz-type criterion).
- **Lemma 3.7:** smallest eigenvalues of induced subgraphs are ≥ that of the
  supergraph (monotonicity under taking induced subgraphs) — the elementary but
  load-bearing fact for interlacing/precrowding arguments.
- **Theorem 2.4 / Theorem 2.6 / Theorem 2.7:** structural thresholds for
  smallest eigenvalues near supremum values (α₁ ≈ −2.4812, etc.) — this is
  where the "no finite forbidden-subgraph basis beyond λ* ≈ 2.0198" boundary
  (cf. Birkhoff–Jiang–Polyanskii, used in the run's −4 approach note) is
  contextualized: −4 with λ=4 > λ* lies past the finite-basis threshold.

## Bearing on (99,14,1,2)
- The survey confirms the −2 theory is complete (generalized line graphs) while
  the −3 / −4 theory is not — matching the `least-eigenvalue-minus-4-structure`
  approach's "speculative: high" flag and why the −4 gate is not a settled
  finite classification the way −2 is.
- **Neumaier's geometric dichotomy** (a primitive SRG with smallest eigenvalue
  −m is geometric — Latin-square or Steiner family — provided
  (m+1)(a+1)−k > (c−1)(m+1)/2) has HYPOTHESIS FAILING at (99,14,1,2):
  m=4, a=λ=1, c=2, k=14 gives 5·2−14 = −4, not > 2.5 = 1·5/2. So the geometric
  classification does not fire at 99. This was in the approach note; the survey
  is the named source for it.
- The survey is a **map, not a weapon**: it confirms which doors at −4 are open
  (geometric-SRG classification lineage van Dam / Koolen–Yang / Spence) and
  which are shut (finite forbidden-subgraph basis; Neumaier geometric
  dichotomy). No theorem in it itself excludes (99,14,1,2).

## Why it matters here
It is the named survey for the `least-eigenvalue-minus-4-structure` approach's
dichotomy (first-step request #2). The library now holds it, so the approach's
precedent tier is complete on its two primary references (GKP tables + this
survey). No claim to record beyond the approach note; the −4 geometric-SRG
classification gap remains a live request if the approach is pursued.
