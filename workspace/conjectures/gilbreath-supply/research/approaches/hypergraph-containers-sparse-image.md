# Container method for the sparse-image set (Saxton–Thomason / BMS)

```approach
idea: Bound the "bad set" B(ε) = {h ∈ F₂^n : wt(Φ_n h) ≤ εn} with the hypergraph
container method, then show the prime h lies outside every container by a
provable uniformity fact. This replaces "is h complicated" by "h is outside an
explicitly structured, exponentially small union", and the containers — not a
complexity hypothesis — are the certificate.

mechanism: The bad set is the preimage of a Hamming ball: for each sparse image
vector y there are exactly 2² = 4 preimages (rank Φ_n = n−2, nullity 2), so
|B(ε)| = 4·Σ_{k≤εn} C(n−2,k) ≈ 4·2^{n·H(ε)}, exponentially small for ε < 1/2.
The container method (Saxton–Thomason, Balogh–Morris–Samotij) turns such a
supersaturation-structured set into a SMALL family of containers, each a
structured superset (typically "the vertex is ε-close to a kernel-like/alternating
configuration"). Here the hypergraph on the cube is given by the rows: vertex
h ∈ F₂^n, one edge per row d consisting of the affine hyperplane a_d = 1. B(ε)
is the set of vertices incident to ≤ εn edges of one sign. The candidate theorem:
containers for B(ε) are explicitly of the form "h is ε-close to a dyadic-
alternating (kernel-like) string", and the primes avoid all of them by a provable
input (one-point balance at all dyadic scales, plus non-2-automaticity). This is
a purely combinatorial engine; its output is a *certificate* that implies linear
fold weight without assuming the pair pattern (switch density).

falsifier: the containers may be trivial (all of F₂^n) or not characterizable, in
which case no arithmetic input can be plugged in; or the containers may be exactly
the five closed-door witnesses in disguise (re-opening a door, e.g. "h is not
alternating" is insufficient). Also the primes must be shown to avoid the
containers by a PROVABLE input, not a heuristic.

status: refuted
killed-by: >
  B(ε) is NOT a family of independent sets of any hypergraph on the cube, so the
  container theorem does not apply. The BMS/ST container theorem covers the
  INDEPENDENT SETS of an s-uniform hypergraph whose edges are evenly distributed
  (supersaturation/co-degree conditions). Here B(ε)={h∈F2^n : wt(Φ_n h) ≤ ε n}
  is the preimage of a Hamming ball under the surjective rank-(n-2) map Φ_n,
  |B(ε)|=4·Σ_{k≤εn}C(n-2,k) — a low-density-set condition, not "contains no edge
  of a fixed hypergraph". The route's proposed hypergraph (one edge per row d =
  the affine hyperplane a_d=1, vertex set F2^n) has B(ε) as the set of vertices
  incident to few edges of one sign, the COMPLEMENT of an independent-style
  condition. Second independent defect: the proposed container shape "h is
  ε-close to a dyadic-alternating (kernel-like) string" is FALSE as a
  description of B(ε): Thue-Morse has sublinear nu2, so h=Thue-Morse ∈ B(ε) for
  small ε, yet it is not close to the kernel (differs from both alternating
  strings on half the coordinates) — so every covering container family must
  contain Thue-Morse, and a characterization that excludes it is wrong. It also
  re-opens the closed family ("h not close to alternating" is a weak non-
  complexity input that cannot separate the primes from Thue-Morse, which also
  collapses).
precedent:
  - "Balogh, Morris, Samotij, Independent sets in hypergraphs, J. Amer. Math.
    Soc. 28 (2015) 669-709, DOI 10.1090/S0894-0347-2014-00816-X."
  - "Saxton, Thomason, Hypergraph containers, Invent. Math. (2015),
    arXiv:1204.6506 (the general container theorem)."
  - "Balogh-Morris-Samotij, The method of hypergraph containers, ICM 2018
    survey (arXiv:1506.08311)."
  - "Mousset-Nenadov-Steger, On the number of graphs without large cliques, DOI
    10.1137/130947878 (standard container template, K_ℓ-free graphs)."
  - "Campos-Samotij, Towards an optimal hypergraph container lemma, Combinatorica
    2026, DOI 10.1007/s00493-026-00214-1 (recent strengthening, HCL machinery)."
first-step: (a) set up the hypergraph H_n precisely (vertex F₂^n, one edge per
row d = the odd-parity affine hyperplane), compute average degree and co-degree
to check the supersaturation hypotheses numerically for n ≤ 16; (b) run the
container construction (or a SAT encoding of "enumerate the maximal independent
families of the complementary hypergraph") for n ≤ 16 and INSPECT the containers:
if they are visibly "dyadic-alternating-like", the route is live and the next step
is pricing the arithmetic input that proves the primes avoid them; if the
containers are trivial or already include the five door witnesses only, the route
is dead.
```
