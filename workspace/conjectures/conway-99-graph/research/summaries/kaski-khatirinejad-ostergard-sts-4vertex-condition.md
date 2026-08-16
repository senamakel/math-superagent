# Kaski–Khatirinejad–Östergård 2011, "Steiner triple systems satisfying the 4-vertex condition"

**Source:** https://doi.org/10.1007/s10623-011-9520-2 — Designs, Codes and
Cryptography 59 (2011) 31-38. Paywalled (Springer); **only the abstract and
reference list were obtained**. The complete proof is not in the library.

## What it establishes (from the abstract)

> Higman asked which block graphs of Steiner triple systems of order $v$ satisfy
> the 4-vertex condition and left the cases $v = 9, 13, 25$ unsettled. We give a
> complete answer…: the affine plane of order 3 and the binary projective spaces
> are the only such systems. The major part of the proof is to show that no
> block graph of an STS(25) satisfies the 4-vertex condition.

So: **the block graph of a complete Steiner triple system satisfies the
4-vertex condition iff the STS is AG(2,3) (order 9) or PG(m,2) (binary
projective, order $2^m-1$).** This settles Higman's 1971 question completely,
closing $v=13$ and $v=25$ in the negative.

## Relevance to the Conway 99-graph run

- The **block graph** of an STS(v) is the **line graph** of the STS: its
  vertices are the blocks, adjacency = disjoint blocks (intersection graph /
  line graph of the block design). For an STS(v) the block graph is
  `srg(v(v-1)/6, 3(v-3)/2, (v+3)/2, 9)` — e.g. STS(15) → srg(35,16,8,8),
  STS(21) → srg(70,27,9,11), generic λ=(v+3)/2, μ=9.
- That parameter family (λ=(v+3)/2, μ=9, μ = k(v−3)/(v−1)… ) is **disjoint
  from the λ=1, μ=2 family** this run targets. So KKO's *complete* answer does
  not decide anything about srg(99,14,1,2) directly.
- The **relevant transfer** is the underlying theorem it shares with this run's
  `c7`/4-vertex-condition threads: an srg satisfies the (Sims) 4-vertex
  condition iff its local intersection numbers are pair-type-constant (α for
  adjacent, β for nonadjacent pairs). For a **λ=1, μ=2** srg this pins
  α = C(λ,2) = 0, β = C(μ−1,1) = 1 for the neighbourhood counts; the run's
  claim `c7-4vertex-mu2-common-neighbour-nonadjacent` is the same machinery.
- The Conway 99-graph's triangle geometry is a **partial** Steiner triple
  system (231 lines of size 3, 7 per point), *not* a complete STS (1617 lines).
  The line/intersection-graph ℓ-graph of a partial STS is not the block graph
  of KKO, so KKO's classification cannot be pushed onto the partial geometry —
  which is precisely the "genuine-STS realization at 99 is not decided by it"
  caveat already recorded for Behbahani–Lam–Östergård 2012 in
  `research/notes/triangle-geometry-4vertex-enumeration.md`.

## Status in this library

- `sourced` (abstract-level). The classification statement is verified as
  quoted from the source abstract; the proof is unread (paywalled).
- **Reference URLs:** DOI https://doi.org/10.1007/s10623-011-9520-2 ;
  abstract captured from the Springer landing page at download time.

## Do not re-fetch

The full text is a Springer subscription article with no open-access copy
found in the archive searches; the abstract is the max obtainable here. The
result it establishes (which complete STSs have 4-vertex-condition block
graphs) is recorded; re-attempt only against a stated reason it would change
this run's decision.
