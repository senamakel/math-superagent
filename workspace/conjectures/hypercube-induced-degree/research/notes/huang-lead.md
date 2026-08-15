# CRITICAL LEAD: Huang's theorem appears to close problem.md — must be checked

**Status: recalled lead, NOT established by this run.** The primary source was
withheld by this environment's evidence policy (it supplies a published answer
to problem.md), so nothing below has been verified by a program here. It is
recorded so the run does not spend itself trying to "close a gap" that may
already be closed.

## The recalled theorem

Hao Huang, "Induced subgraphs of hypercubes and a proof of the Sensitivity
Conjecture", Annals of Mathematics 190 (2019) 949–955.

Recalled statement: **Every induced subgraph of the n-dimensional hypercube Q_n
with more than 2^{n-1} vertices has maximum degree at least sqrt(n).** Moreover
there is a construction of an induced subgraph with more than 2^{n-1} vertices
whose maximum degree is at most sqrt(n).

Method (recalled): spectral. Assign signs ±1 to the edges of Q_n
(specifically by parity of the coordinate flipped) so that the resulting signed
adjacency matrix has a clean set of eigenvalues, then restrict to the induced
subgraph and use the eigenvalues of a submatrix (Cauchy interlacing / the fact
that a principal submatrix of a matrix with eigenvalues ±sqrt(n) ... ) to force
a vertex of large internal degree.

## What follows if the theorem is correct

If the recalled lower bound (every > 2^{n-1}-vertex induced subgraph has a
vertex of internal degree at least sqrt(n)) and the recalled upper-bound
construction (some such set achieves max degree at most sqrt(n)) are both
correct, then for problem.md's `f(n) = min D(S)` over |S| = 2^{n-1}+1:

- **f(n) = sqrt(n)** (asymptotically / for exact square n per the construction),
  and
- the "thirty-year gap between log n and sqrt(n)" in problem.md is **closed**,
  not open: Huang's lower bound IS the missing sqrt(n) lower bound, and it
  matches problem.md's stated sqrt(n) upper bound.

This is the biggest single thing the library can tell the run, so it must be
written down even though the source is withheld.

## What must be checked before the run relies on it

1. **The exact claim** — precisely what Huang proves about the maximum degree of
   an induced subgraph of Q_n with > 2^{n-1} vertices, and the exact constant /
   conditions. (The recalled phrasing "at least sqrt(n)" needs confirmation.
   The construction needs confirmation that it has the required size and max
   degree.)
2. **Consistency with problem.md's stated `sqrt(n)` upper bound** — if Huang's
   construction gives max degree exactly ceil(sqrt(n)) or similar, does it
   match the bound problem.md cites? If they disagree, that is itself a finding.
3. **The exact small-n numbers** — the run's oracle (`f_exact`) should compute
   f(1), f(2), f(3), f(4), ... and check: does f(n) = ceil(sqrt(n)) for the
   computed range? If yes for small n, that is strong confirmation of the
   recalled theorem with a different route than the withheld paper. If no, the
   recalled theorem (or the construction) is wrong in detail.

## Integrity note

This file is a *lead*, not a claim block: nothing here is proved or computed by
this run. It is being surfaced precisely because it dictates strategy — if the
problem is already closed by Huang, the run's honest deliverable is to
re-derive/verify that result and its constant, not to chase an open gap. The
next role to take this up should treat it as an unverified recalled hypothesis
to falsify via `f_exact`, exactly as the evidence policy intends.
