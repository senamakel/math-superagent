# Assmus, "On 2-ranks of Steiner triple systems" (EJC 1995) — summary

**Source**: E. F. Assmus Jr., *The Electronic Journal of Combinatorics* 2 (1995) #R9,
doi 10.37236/1203. Full text held:
`research/sources/assmus-2ranks-sts-fulltext.full.md` (OCR, single-line — best read
via the digest in `research/notes/assmus-sts-2rank-acquisition.md` rather than the
garbled line).

## What it establishes (precise statements)

1. **Carrier code / existence–uniqueness (main theorem).** To every Steiner triple
   system one associates a binary code — the "carrier" — which depends **only on the
   order of the system and its 2-rank**. When the STS has 2-rank < number of points
   (a *deficient* system), the carrier organises all information needed to construct
   *directly* every STS of the given order and 2-rank, from STSs of a specified
   smaller order. The carriers are a two-parameter family of binary codes related to
   the Hamming codes.
2. **Quadruple systems.** An analogous existence–uniqueness theorem holds for
   Steiner quadruple systems; there the binary code (the analogue of the carrier) is
   the dual of a code obtained from a first-order Reed–Muller code repeated a
   specified number of times.
3. **Consequences.** All triple systems are "derived" provided those of full 2-rank
   are; and resolvable quadruple systems on u and on v points give a resolvable
   quadruple system on uv points.

## What this means for the 2-rank (the operative consequence for this run)

The theorem makes **rank_2(N)** a genuine structural invariant of an STS's line set:
it is *not* fixed by order/parameters alone, because deficient systems (2-rank < v)
coexist with full-rank systems of the same order. Classical minimum: the
Doyen–Hubaut–Vandensavel lower bound, 2-rank ≥ 2^n − 1 − n for STS(2^n − 1), with
equality iff the projective PG(n−1,2) design.

## Bearing on srg(99,14,1,2)

The 99-graph's triangle geometry is a **partial** STS (231 lines, 7 per point, λ=1),
so Assmus's full-STS carrier theorem does not apply verbatim; but the *principle*
carries: the incidence 2-rank of the (99×231) triangle-incidence matrix N is not
parameter-determined. **Checked** on the two negative controls:
rank_2(N) = 5 (defect 4) for rook(3)=srg(9,4,1,2) but **243 (full, defect 0)** for
BvLS=srg(243,22,1,2) — the two controls give different 2-ranks, so the invariant is
live and can in principle separate 99 from 243 (`code/out/incidence_p_rank.captured.txt`).
A putative 99-graph's rank_2(N) would be a 99-specific obstruction to seek, with no
spectral analogue.

## What it does not settle
- It does not itself give the 99 value of rank_2 (a computation, not a citation).
- It concerns *complete* STSs; the partial-STS transfer is the run's own extension.

The canonical claim block for this result is `assmus-sts-2rank-grounded`, held in
`research/notes/assmus-sts-2rank-acquisition.md` (rendered in CLAIMS.md).

[[assmus-2ranks-sts-fulltext.full]]
