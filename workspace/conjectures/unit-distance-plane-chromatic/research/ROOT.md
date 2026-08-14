# ROOT — the subject's foundation, as this run's library now establishes it

**Subject:** the Hadwiger–Nelson problem — the chromatic number χ of the
unit-distance graph of the plane, known to satisfy 4 ≤ χ ≤ 7, open for decades.
Lower bound 4 (Moser spindle); upper bound 7 (hexagonal tiling). Neither has
moved in decades.
Wait — evidence policy note: this run's own objective is the problem in
problem.md. Statement and bounds are inputs to be **verified in this workspace**,
not quoted from the library. ROOT records the *technique and structural*
knowledge the library now holds.

## What the library now establishes (each claim sourced; see CLAIMS.md)

1. **The finite-subgraph reduction (de Bruijn–Erdős 1951, proved).**
   χ(G_plane) ≥ k iff some finite subgraph is not (k−1)-colourable. The entire
   lower-bound search operates on finite unit-distance graphs; nothing infinite
   needs reasoning about. This is the single most load-bearing structural fact.
2. **Density constraint (Spencer–Szemerédi–Trotter, O(n^{4/3})).** A unit-
   distance graph on n points has O(n^{4/3}) edges. Unit-distance graphs cannot
   be randomly dense; a graph forcing high chromatic number must be *rigid*,
   with highly coincidental unit distances, which happens only for point sets
   with algebraic structure.
3. **Rigidity–structure tie (Pach–Raz–Solymosi).** Near-extremal unit-distance
   point sets decompose into a large subset plus bipartite rigidity subgraphs.
   Rigidity is the source of density; the growth conditions delimit how the
   rigidity must accumulate.
4. **Lattice criterion (Chilakamarri).** A finite graph is a plane unit-distance
   graph **iff** it is faithfully √2-recurring in Z². Algebraic lattices are thus
   a complete search class: lattice-restricted constructions can already force
   5 colours in a unit-distance analogue (χ(Z²,r,√2) ≥ 5).
5. **Construction engines (Alexeev–Mixon–Parshall; Raigorodskii survey).** The
   standard machinery for building rigid/dense unit-distance graphs is Minkowski
   sums, spindles (rotating a copy about a shared vertex), and algebraic point
   sets (Gaussian/Eisenstein lattices). Spindles are the canonical lower-bound
   gadget; tilings the canonical upper-bound colouring.
6. **Boundary with measurable variant (Raigorodskii survey; Székely).** The
   measurable-chromatic-number problem is a strictly larger lower bound and is
   NOT the target; any result proved under a measurability hypothesis belongs to
   the variant and must be recorded as such.

## Structure of a minimal counterexample (what the run now knows to seek)

A minimal non-4-colourable unit-distance graph — if one exists — has to be:

- **rigid** (algebraically determined coordinates), because random/sparse point
  sets are 4-colourable; density O(n^{4/3}) cannot be bought;
- **accumulated**: the obstruction is not a local gadget but rigidity forced
  across the whole configuration (per the problem statement and the
  near-extremal structure theory);
- **constructible by algebraic engines**: Minkowski sums and spindles of
  algebraic point sets (Gaussian / Eisenstein / cyclotomic lattices) are the
  known-generative machinery;
- **verifiable exactly**: every edge at distance exactly 1 and colouring
  decided by a complete method, with the coordinate field Q(sqrt(d))-type
  extensions and exact symbolic edge checks.

## Current verification bound (phase-1 starting datum)

7 vertices: the Moser/7-vertex spindle is 4-chromatic (4-colourable, not
3-colourable) — the low end. There is no 5-chromatic unit-distance graph known
to this library on any number of vertices; the minimum size of a 5-chromatic
unit-distance graph is part of the run's own search space. **N starts at 7** for
the size-lower-bound skeleton: the run must establish, mechanically, which N
admit only 4-colourable unit-distance graphs. Note: the known published
lower-bound constructions (the 1581-vertex graph, later reduced) are screened by
the evidence policy as the problem's answer-tier material; the run derives its
own constructions and verification.

Main caution from the density side: a random or greedy point set is
4-colourable; the search must be over *constructions* (Minkowski sums, spindles,
lattices), never over random points.

## Settled restricted classes (with their hypotheses)

| Restricted class | What is settled | Hypothesis | Source |
| --- | --- | --- | --- |
| Finite unit-distance graphs, any bipartite/planar-in-the-abstract case | de Bruijn–Erdős: χ(G_plane) = sup over finite subgraphs | ordinary infinite graph, choice principle | de Bruijn–Erdős 1951 |
| Point sets with u(P) ≥ n^{4/3} h(n) | must contain near-extremal bipartite rigidity blocks | h(n)→inf | Pach–Raz–Solymosi Thm 6 |
| Lattice-restricted graphs (Z²,r,√2) | χ ≥ 5 for all integer r ≥ 1 | lattice graph edges at distance in an interval | Chilakamarri 1996 |
| Graphs on ≤ 9 vertices | unit-distance iff F-free for the Globus–Parshall F | F the 74 minimal forbidden subgraphs | Alexeev–Mixon–Parshall |
| Measurable colourings of the plane | strictly larger lower bounds known (NOT the target) | measurability of colour classes | Raigorodskii survey; Székely |

## Where this library stands relative to phase 1's exit test

Phase-1 exit criterion as given: ROOT.md states the structure of a minimal
counterexample, the current verification bound, and at least three settled
restricted classes with hypotheses. All three are now present. Subsequent
library growth happens only against a stated gap in REQUESTS.md.

## Open gaps (recorded in REQUESTS.md)

- The largest N for which it is *published* that every unit-distance graph on
  ≤ N vertices is 4-colourable — the verification-bound datum — is not yet on
  disk from a primary source; the evidence policy screens the answer-tier
  construction papers, so this may be derivable only by the run's own verifier.
- Full texts of the survey-level sources (Raigorodskii, Woodall, Chilakamarri)
  could not be downloaded (network-blocked); their summaries are on disk from
  read_sources. The work proceeds on the technique tier already present.