# Hoffman eigenvalue bound on the chromatic number

**Primary source:** A.J. Hoffman 1970. Statement confirmed / restated by
Abiad–Bosma–van Veluw, "Hoffman colorings of graphs" (arXiv:2407.02544) and by
Abiad–Meeus (arXiv:2512.13187, cited in the companion file), plus the
Elphick–Wocjan survey "Unified Spectral Bounds on the Chromatic Number"
(https://doaj.org/article/faa28d31c2c142359f5f1259e6a47ac2), which attributes
the bound to Hoffman 1970.

**How obtained:** server-side retrieval layer (direct publisher access blocked
at the network boundary). Not re-derived computationally here.

## Exact statement

For any finite simple graph G with at least one edge, let
`lambda_max >= ... >= lambda_min` be the (real) adjacency-matrix eigenvalues.
Then

    chi(G) >= 1 - lambda_max / lambda_min.

Holds for **general** (not necessarily regular) graphs with at least one edge.
The right-hand side is a lower bound on the chromatic number; when it exceeds 4
the graph is not 4-colourable.

## Why it matters here

This is the **cheap polynomial warm-up / filter** of the run's **adopted**
`lovasz-theta-vector-chromatic` approach: before running an SDP for `ϑ(Ḡ)`,
the Hoffman bound on the Moser spindle, Moser+Moser, and any candidate
unit-distance graph gives a one-line spectral certificate. If some constructible
UDG has `1 - lambda_max/lambda_min > 4`, that is an exact, coordinate-free
certificate that `chi >= 5` — polynomial, where SAT cannot scale. The run has
not yet computed this value on any of its graphs (REQUESTS row OPEN: "maximum
of theta(Gbar) over constructible UDGs" includes the Hoffman warm-up).

## Claim block

```claim
id: hoffman-eigenvalue-bound
statement: For any finite simple graph G with at least one edge and adjacency
  eigenvalues lambda_max >= ... >= lambda_min, chi(G) >= 1 - lambda_max/lambda_min.
hypotheses: G finite simple with at least one edge; real adjacency eigenvalues.
holds-here: yes — every plane unit-distance graph the run constructs is finite
  simple with edges; the bound applies verbatim and is the polynomial warm-up of
  the adopted lovasz-theta approach.
status: asserted-by-source (Hoffman 1970, as restated by Abiad–Bosma–van Veluw
  arXiv:2407.02544 and Elphick–Wocjan); not machine-checked here.
bearing: cheap exact spectral lower bound on chi for constructed unit-distance
  graphs — the warm-up/filter of the adopted lovasz-theta-vector-chromatic
  approach; > 4 would certify chi >= 5 polynomially.
anchor: research/sources/hoffman-eigenvalue-bound.md
falsifies: nothing — a classical universal bound; its usefulness here depends on
  whether some constructible UDG actually attains RHS > 4, which is a
  computation, not a source question.
```
