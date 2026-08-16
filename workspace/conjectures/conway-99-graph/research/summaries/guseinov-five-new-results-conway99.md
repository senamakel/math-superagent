# Guseinov — Five New Results on Conway's 99-Graph Problem

Source URL: https://doi.org/10.6084/m9.figshare.23732622.v1
(Figshare preprint; version 1 2023-07-22, latest version 5 2025-04-12)

## What it is
A self-published preprint (NOT peer-reviewed; 0 citations). The five results
are stated as claims obtained 2022–2023 by the author. **None has been
independently verified by the oracle in this workspace.** Treat the five as
leads whose plausibility phase 4 should test, not as established facts.

## Five claims (var., G a putative Conway 99-graph = srg(99,14,1,2))
1. G is not a subgraph of any srg(243,22,1,2) [BvLS graph].
2. G cannot be obtained by a generalisation of the Berlekamp–van Lint–Seidel
   construction.
3. G is Cartesian-indecomposable.
4. G contains no Hamming graph H(4,3).
5. The independence number of G is at least 10.

## Which are checkable by the oracle, and how
- **(5) alpha(G) >= 10** is the most concrete and directly checkable claim
  against a partial/constructive search and against the family's upper bounds.
  An independence number lower bound of 10 is a *structural* restriction that
  does NOT follow from srg parameters alone (alpha for such graphs is not
  pinned). If a lower bound of 10 is sound, it combines with any upper bound
  to constrain the graph. **Unverified; candidate for oracle.**
- **(1) not a subgraph of BvLS(243)** requires the BvLS graph built from the
  ternary Golay code (already an oracle control) and a subgraph-isomorphism
  check — expensive but bounded; a lead.
- **(4) no H(4,3)** is a forbidden-induced-subgraph claim, also checkable
  in principle but H(4,3) has 81 vertices, so containment is a 81-vertex
  structure inside 99; a lead.
- (2) and (3) are structural-construction claims, harder to reduce to the
  oracle directly.

## Assessment
Status: asserted-by-author, unpublished, unverified. Relevant to the run
mainly because claim (5) and claim (1) are stated in a form the oracle could
test, and because they suggest the recent research direction. Not a source of
"known result" facts — do not cite as established until verified.

Also note the paper's own framing reinforces the run's picture: existence
remains open as of its latest version (2025-04).
