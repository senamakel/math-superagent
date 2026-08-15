# Vector chromatic number and the Karger–Motwani–Sudan SDP (1994/1998)

**Subject:** The definition of the **vector chromatic number** `χ_v(G)` — the
SDP relaxation of `χ(G)` that the run's adopted `lovasz-theta-vector-chromatic`
approach uses as `χ_v(G) = ϑ(Ḡ)`. This note fixes what vector colouring is, and
the exact statement that `χ_v` is the Lovász theta of the complement.

## Source

- **Primary:** D. Karger, R. Motwani, M. Sudan, *Approximate graph coloring by
  semidefinite programming*, FOCS 1994, pp. 2–13; Journal version J. ACM **45**
  (1998) 246–265. DOI 10.1145/274787.274791.
  https://dl.acm.org/doi/10.1145/274787.274791
  Retrieved via `exa_search` (research paper); passage-level text confirms the
  vector-colouring SDP, its duality with the Lovász theta function, and the
  resulting colouring approximation bounds.

## What it establishes

**Definition (k-vector-colouring / vector chromatic number).** A graph G has a
**k-vector-colouring** when each vertex v is assigned a unit vector `u_v` in some
Euclidean space such that for every edge `{u,v}` the inner product
`⟨u_u, u_v⟩ ≤ −1/(k−1)`. The **vector chromatic number** `χ_v(G)` is the smallest
`k` for which such an assignment exists. A proper k-colouring is a k-vector-
colouring with the standard basis as vectors, so `χ_v(G) ≤ χ(G)`.

**Established relation to Lovász theta.** The primal of the KMS vector-colouring
SDP is dual to the Lovász theta SDP, and the optimum value is exactly
`χ_v(G) = ϑ(Ḡ)` (the Lovász number of the complement). This is the connection the
approach file cites as `χ_v = ϑ(Ḡ)`.

**Colouring approximation results (for context, not used directly).** KMS show a
randomized polynomial-time algorithm colours every 3-colourable graph on n
vertices with `min{O(Δ^{1/3} log^{1/2} Δ · log n), O(n^{1/4} log^{1/2} n)}` colours,
where Δ is the maximum degree; for general k-colourable graphs the exponent scales
with `1 − 3/(k+1)`. The duality value is used to colour; the run only needs the
*value* (as a lower bound on χ), not the rounding.

## Why this matters

The adopted `lovasz-theta-vector-chromatic` approach calls `χ_v(G) = ϑ(Ḡ)` the
"polynomial exact SDP lower bound" and needs it *sourced* — the approach file
explicitly flags "theta has its vertex-transitive eigenvalue formula (source
before use)". This note fixes the definition of χ_v and the 
`χ_v = ϑ(Ḡ)` identity from the primary KMS paper. The known limitations (from the
SDP-relaxation literature, e.g. "On semidefinite programming relaxations for graph
coloring"): there are graph families where the SDP value is `2+ε` while χ is large
— i.e., the relaxation can be much weaker than χ, which the run must keep in mind
as the value-caveat on its adopted direction.

## Notation trap (from parallel-source synthesis — important before implementing)

Two phrasings of the adjacent-vertex inner-product bound circulate in the
literature: `⟨x_u,x_v⟩ ≤ −1/k` and `⟨x_u,x_v⟩ ≤ −1/(k−1)`. The canonical KMS
definition — and the one that equals `ϑ(Ḡ)` — is **`−1/(k−1)`**. The `−1/k`
phrasing appears in a variant (the "strict" vector chromatic number `χ_sv`), and
some sources state the `χ_v = ϑ(Ḡ)` identity only for the strict variant. The run
must use `−1/(k−1)` when implementing ϑ(Ḡ). This is a notation trap, not a
mathematical discrepancy; the sandwich `ω ≤ ϑ(Ḡ) ≤ χ` is universal either way.

## Claim block

```claim
id: vector-chromatic-equals-theta-complement
statement: The vector chromatic number of G, defined by unit-vector assignments
  with ⟨u_u,u_v⟩ ≤ −1/(k−1) on edges, equals the Lovász theta number of the
  complement: χ_v(G) = ϑ(Ḡ). In particular ϑ(Ḡ) ≤ χ(G), so ϑ(Ḡ) > 4 is a
  certificate that G is not 4-colourable.
hypotheses: G a finite simple graph; ϑ the Lovász SDP value of the complement;
  the vector-colouring SDP and theta SDP are dual to one another.
holds-here: YES — applies to every finite unit-distance graph the run constructs;
  this is the adopted lower-bound certificate.
status: asserted-by-source (Karger–Motwani–Sudan 1994/1998 primary; corroborated
  by the "On semidefinite programming relaxations for graph coloring" and the
  "Graph coloring and semidefinite rank" (2024) surveys; not re-derived here).
bearing: makes the theta/vector-chromatic direction computable and certified:
  χ_v is exactly the SDP the run computes, and the sandwich theorem fixes its
  soundness.
anchor: research/sources/karger-motwani-sudan-vector-chromatic-1994.md
falsifies: a graph whose vector-chromatic number exceeds its chromatic number —
  impossible by the theorem; the recordable failure is χ_v ≤ 4 on every
  constructible UDG (relaxation strictly below the 5 threshold).
```

## Status

Recorded by the librarian as a primary source note. The identity
`χ_v = ϑ(Ḡ)` is asserted-by-source; *computing* the values on the run's graphs is
the adopted approach's next step, not this note.
