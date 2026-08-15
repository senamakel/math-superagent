# Lovász theta function and the Sandwich Theorem (Knuth 1994)

**Subject:** The exact-arithmetic, polynomial-time lower-bound machinery the run's
adopted `lovasz-theta-vector-chromatic` approach rests on. This note fixes the
definition of ϑ and the exact sandwich inequality `ω(G) ≤ ϑ(Ḡ) ≤ χ(G)` that makes
`ϑ(Ḡ) > 4` a machine-verifiable certificate of non-4-colourability.

## Source

- **Primary:** Donald E. Knuth, *The Sandwich Theorem*, The Electronic Journal of
  Combinatorics **1** (1994), #A1. DOI 10.37236/1193.
  https://doi.org/10.37236/1193
  Retrieved via `exa_search` (research paper) — abstract + references; the SDP
  formulation of ϑ and the sandwich inequality are confirmed against the returned
  text and two corroborating sources below.

## What it establishes

**Definition (Lovász number ϑ).** For a graph G with Laplacian/sphere relaxations,
ϑ(G) is best given for this run in its SDP form: ϑ(G) is the maximum of
`sum_{i,j} X_ij` over PSD symmetric matrices `X ⪰ 0` with `tr X = 1` and
`X_ij = 0` whenever `{i,j}` is an edge of G (the "orthonormal-representation" SDP
of Lovász 1979). Equivalently ϑ(G) can be defined by orthonormal representations
of Ḡ.

**Sandwich Theorem (clique-coclique-sandwich).** For every graph G,

```
ω(G)  ≤  ϑ(Ḡ)  ≤  χ(G)
```

where ω is the clique number, χ the chromatic number, and ϑ(Ḡ) the Lovász number
of the complement.

**Computational tractability.** ϑ can be computed in polynomial time (to arbitrary
precision) via semidefinite programming — Grötschel–Lovász–Schrijver. ω and χ are
NP-complete to compute exactly; ϑ sits between them and is easy. This is exactly
what the run needs: `ϑ(Ḡ) > 4` would certify `χ(G) ≥ 5` at polynomial cost where
complete SAT (exponential) cannot reach.

**The KMS links.** The vector chromatic number `χ_v(G) = ϑ(Ḡ)` (Karger–Motwani–
Sudan; see `karger-motwani-sudan-vector-chromatic-1994.md`) is the SDP relaxation
of χ whose primal is the vector-colouring program — this is the same ϑ(Ḡ) in the
sandwich. Corroborated by Coja-Oghlan's "The Lovász Number of Random Graphs"
(2005), which states `α(G) ≤ ϑ(G) ≤ χ(Ḡ)` and notes `θ(G) = ϑ(Ḡ)` gives
`ω(G) ≤ θ(G) ≤ χ(G)`, and by the 2026 "Algebraic bounds on the chromatic number"
review, which restates the Sandwich Theorem verbatim and notes `ω(G) ≤ ϑ(Ḡ) ≤ χ(G)`
with ϑ(Ḡ) polynomial-time computable.

## Why this matters (the run's adopted direction)

`problem.md`'s lower-bound form is "exhibit a finite unit-distance graph not
4-colourable." Complete SAT on that graph is exponential. The call-to-arms on the
board (adversarial, converging decision) adopted `ϑ(Ḡ)` as the *other* lower-bound
oracle: computing ϑ(Ḡ) of the run's constructions is a polynomial exact SDP, and
any value strictly above 4 is a proof that the graph is not 4-colourable — hence
χ(plane) ≥ 5 by de Bruijn–Erdős. The sandwich theorem is the theorem that makes
that inference sound. It is technique, not answer: it certifies non-colourability
without handing over any concrete 5-chromatic construction.

## The value caveat, stated honestly

The sandwich only guarantees `ϑ(Ḡ) ≥ ω(G)`, and no plane unit-distance graph
contains K4 (three unit edges from one vertex lie on a unit circle, pair distances
≤ √3 < ... ), so ω(G) ≤ 3 for every plane UDG and the relaxation gives no bound
above 3 for free. Whether any constructible UDG reaches `ϑ(Ḡ) > 4` is the run's
own computation to make (REQUESTS row 7); this source only fixes the theorem that
*both* directions of the inequality are sound.

## Claim block

```claim
id: lovasz-sandwich-theta
statement: For every graph G, ω(G) ≤ ϑ(Ḡ) ≤ χ(G), where ϑ is the Lovász number
  (computable in polynomial time via SDP), ω the clique number, χ the chromatic
  number. In particular ϑ(Ḡ) > 4 in any finite graph that is not 4-colourable,
  and ϑ(Ḡ) ranges in [3, χ] for the run's plane unit-distance constructions
  (ω ≤ 3 because K4 does not embed at unit distance in the plane).
hypotheses: G a finite simple graph; ϑ the Lovász SDP value of the complement.
holds-here: YES — applies verbatim to every finite unit-distance graph the run
  constructs; it is the lower-bound oracle of the adopted lovasz-theta approach.
status: asserted-by-source (Knuth 1994, primary exposition; corroborated by
  Coja-Oghlan 2005 and the 2026 algebraic-bounds review; not re-derived here).
bearing: the soundness of ϑ(Ḡ) > 4 as a machine-certificate of χ ≥ 5 — the
  run's polynomial exact replacement for exponential SAT on large constructions.
anchor: research/sources/lovasz-theta-sandwich-knuth-1994.md
falsifies: a graph with ϑ(Ḡ) > 4 that is nonetheless 4-colourable — impossible
  by the theorem, so a correct ϑ implementation has no such case; the real,
  recordable failure is every constructed graph staying ϑ(Ḡ) ≤ 4 (relaxation gap).
```

## Status

Recorded by the librarian as a primary source note. The claim is
`asserted-by-source`, not machine-checked here (computing ϑ(Ḡ) exactly IS the
run's next step per the adopted approach — this source is the theorem it rests
on, not the computation itself).
