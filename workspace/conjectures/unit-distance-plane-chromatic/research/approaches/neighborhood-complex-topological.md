# Approach: Lovász neighborhood complex as a topological 5-chromaticity certificate

```approach
idea: Lovász's neighborhood-complex theorem χ(G) ≥ conn(N(G)) + 3, used as a
  *topological* certificate of non-4-colourability: a unit-distance graph whose
  neighborhood complex N(G) is 2-connected (conn ≥ 2) is provably not 4-colourable.
  conn(N(G)) is computed exactly from the homology/1-skeleton of a finite
  simplicial complex, entirely in integer/F2 arithmetic — no colouring search at all.
mechanism: The run has already established the local structure that makes this
  natural: every vertex neighbourhood N(v) of a unit-distance graph is a disjoint
  union of paths and 6-cycles (chord-1 ⇔ central angle 60°), so the neighborhood
  complex — whose simplices are exactly the subsets of vertices sharing a common
  neighbour — is a finite simplicial complex built from this constrained data.
  Lovász's theorem (the same theorem that settles Kneser's conjecture) says a
  graph cannot be k-colourable unless its neighborhood complex is at most
  (k−3)-connected, i.e. χ ≥ conn(N(G)) + 3. Hence conn(N(G)) ≥ 2 forces χ ≥ 5.
  This is a *necessary condition* and therefore both (a) a machine-checkable
  certificate for a candidate graph and (b) a cheap pre-filter: compute conn(N(G))
  by reduced homology over F2 plus a π₁ computation from the 1-skeleton, and only
  graphs with conn ≥ 2 need the full SAT oracle. It also gives a diagnostic the
  run currently lacks: every 4-chromatic construction must have conn(N(G)) ≤ 1,
  so the Moser spindle and Moser+Moser establish the baseline and calibrate the
  topological oracle against the SAT oracle.
status: refuted
killed-by: N(G) is high-dimensional — one (deg(v)−1)-simplex per vertex, so the
  "tiny chain complex" cost is wrong; certifying conn ≥ 2 needs hard
  simple-connectivity (F₂ homology does not suffice); value is capped (the
  3-colourable triangular lattice forces conn ≤ 0). No regime beats the run's
  complete SAT oracle.
first-step: build N(G) for the Moser spindle and Moser+Moser from their exact
  coordinate fields, compute reduced homology H̃_i(N(G); F2) and the fundamental
  group of the 1-skeleton, confirm conn ≤ 1 for these χ=4 graphs (calibration
  against the SAT oracle), then wire conn(N(G)) in as a pre-filter ahead of the
  forced-pair/SAT harness for every new construction.
falsifies: a graph with conn(N(G)) ≥ 2 that is 4-colourable — impossible if
  Lovász's theorem and the connectivity computation are both correct, so the
  genuine failure mode is the reverse: every construction stays conn ≤ 1. That is
  a real, precise negative result (it bounds how "topologically 5-chromatic" the
  constructible family is), and it costs nothing like a SAT run to find.
cost: polynomial in the number of faces — the neighborhood complex of an n-vertex
  graph has at most n vertices and (by the run's K_{2,3}-free lemma) maximal faces
  of size ≤ 2, so its chain complex is tiny and F2-homology is linear in faces.
  BUT genuine connectivity needs π₁ of the 1-skeleton's cells, and in higher
  dimensions homotopy/homotopy-group triviality is hard even for small complexes
  (Kozlov: determining homotopy triviality is "an extremely hard problem even in
  low dimensions").
precedent:
  - Lovász 1978 "Kneser's conjecture, chromatic number and homotopy" — exact statement confirmed
  - https://doi.org/10.1090/s1079-6762-03-00112-4 (Babson–Kozlov survey: chi(G) >= k+3 when N(G) k-connected)
  - https://doi.org/10.48550/arxiv.math/0505563 (Kozlov survey: exact convention, k >= -1, connectivity/homotopy-triviality hardness caveat)
  - https://doi.org/10.4007/annals.2007.165.965 (Babson–Kozlov, Lovász conjecture / Hom(C odd,G))
  - https://www.sciencedirect.com/science/article/pii/S0097316504000883 (box/neighborhood complexes, Lovász bound)
```

## Verification status on the theorem and the convention

This is the approach whose stated **convention had to be pinned down**, and I
confirm it against the literature:

- **Exact statement (Lovász 1978).** For any graph G, if the neighborhood
  complex N(G) is `k`-connected for some `k ≥ −1`, then `χ(G) ≥ k + 3`. Equivalently
  `χ(G) ≥ conn(N(G)) + 3`. Confirmed by Babson–Kozlov (EJC 2003 survey,
  arXiv.math/0505563, and the Annals 2007 Lovász-conjecture paper where it is
  restated as "if Hom(K2,H) is k-connected, k ≥ −1, then χ(H) ≥ k+3").
- **The +3 and the k ≥ −1 convention are exactly as the approach file had them.**
  The Kneser sanity check pins it: KG(5,2) = Petersen graph has χ = 3, and its
  N(G) is a wedge of circles (conn = 0), giving 0+3 = 3 ✓. The `conn(N(G)) ≥ 2
  ⇒ χ ≥ 5` certificate claim is therefore correct.
- **Homotopy-equivalence note.** N(G) ≅ Hom(K2, G) in the same simple homotopy
  type (confirmed), so the connectivity one computes can be framed either way.
- **The neighbourhood-structure premise holds here.** The run's claim (each UDG
  vertex-neighbourhood is a disjoint union of paths and 6-cycles, chord-1 ⇔ 60°)
  is the `einstein-lattice-unit-distance` / sharp-nbhd structure already in the
  library. N(G)'s maximal faces are the common-neighbour sets, which by the
  K_{2,3}-free lemma have size ≤ 2.

## Value risk — the connectivity barrier is real and must be stated

Two honest problems, and I flagged both:

1. **The certificate step is π₁, not just F₂ homology.** `conn(N(G)) ≥ 2` means
   N(G) is simply connected *and* H₁ = H₂ = 0 (and reduced H̃₀ = 0). F₂ homology
   alone does not certify simple-connectivity. Kozlov explicitly notes that
   establishing homotopy triviality is hard even in low dimensions. So for the
   graphs where F₂-homology *suggests* conn ≥ 2 — the only ones that would matter
   here — the π₁ step is genuinely hard, not a polynomial add-on. On 4-chromatic
   constructions the calibration value (conn ≤ 1) is easy; the approach only gets
   expensive exactly where it would become interesting. The "cheap pre-filter"
   framing is right only as a *negative* filter (rules out conn ≥ 2 cheaply);
   it is not a cheap way to *certify* conn ≥ 2.
2. **Value.** Whether any plane UDG has conn(N(G)) ≥ 2 is unknown to me; the
   published-value question is censored at this run's evidence boundary. As a
   topological lower bound for the plane, the measurable/stronger-variant results
   historically use *different* invariants, and for the unrestricted finite-graph
   problem the neighborhood-complex connectivity of sparse rigid graphs tends to
   stay low (they have small common neighbourhoods, so N(G) is a low-dimensional
   complex with little reason to be highly connected).

**Verdict: grounded** (standard theorem, correctness confirmed, convention pinned,
and conn(N(G)) is a genuinely new cheap exact invariant that partitions the
construction family and can *rule out* candidates at polynomial cost) **with a
stated caveat**: the positive-certificate direction (conn ≥ 2) is a hard
homotopy-triviality problem, not a polynomial step, and the run should treat it
as a cheap negative filter first and only pursue the π₁ direction if a candidate
survives F₂-homology screening — which is unlikely for the rigid sparse graphs
this run constructs.

## What would refute it (killed-by)

A graph with conn(N(G)) ≥ 2 that is 4-colourable — impossible if both Lovász's
theorem and the connectivity computation are correct. The real, and likely,
failure is value-shaped: every construction has conn(N(G)) ≤ 1 (usually 0 or −1),
so the certificate never fires. That is a precise negative result: it bounds how
"topologically 5-chromatic" the constructible family is, costs a polynomial
computation to establish, and would retire the topological route as a 5-certifier
(while keeping it as a cheap pre-filter that feeds candidates to SAT).

## Killed-by (converging decision)

Three problems, any one of which retires it; together decisive.

1. **The cost estimate is wrong.** N(G) has one (deg(v)−1)-simplex per vertex, and a
   unit-distance vertex can have large degree (six on the triangular lattice, more on
   dense constructions); N(G) is therefore high-dimensional with up to Σ_v 2^{deg(v)}
   faces, not a "tiny" complex with maximal faces of size ≤ 2. That claim confused
   "N(v) is triangle-free as an induced graph" (true: chord 1 ⇒ 60°, no three circle
   points are pairwise unit) with "|N(v)| ≤ 2" (false). K_{2,3}-freeness bounds common
   neighbours of *two* vertices, not the size of one neighbourhood.
2. **The certifying step is hard exactly where it would matter.** conn ≥ 2 means simple
   connectivity of a high-dimensional complex (π₁ + H₁ = H₂ = 0); Kozlov notes homotopy
   triviality is hard even in low dimensions, and F₂ homology alone certifies nothing.
3. **Value is capped.** The most symmetric high-degree family — the triangular lattice —
   is 3-colourable, so Lovász's own theorem forces conn(N(G)) ≤ 0 there; sparse rigid
   constructions have little reason to be more connected. No regime beats the complete
   SAT oracle the run already owns and trusts.
