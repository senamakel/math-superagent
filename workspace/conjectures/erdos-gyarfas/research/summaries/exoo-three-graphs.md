# Exoo — Three Graphs and the Erdős–Gyárfás Conjecture (full paper)

Source: https://arxiv.org/pdf/1403.5636 (arXiv:1403.5636v1, 22 Mar 2014)
Full text: `research/sources/exoo-three-graphs-pdf.full.md`
(Note: the earlier `exoo-three-graphs.full.md` was only the arXiv abstract page; this is the real paper.)

## What it establishes

1. **f(2) = 10** (smallest cubic with no 4-cycles; three cubic graphs of order 10 lack C4,
   including the Petersen graph; none smaller).
2. **f(3) = 24** (Markström, all four 24-vertex C4,C8-free cubics listed; one of them is
   built from K4 by replacing three vertices by H7 and the fourth by a K3).
3. **f(4) ∈ [54, 78]**: lower bound 54 is unpublished Markström; upper bound by G78,
   the cubic graph on 78 vertices with no 4-, 8-, or 16-cycles, built from the Petersen
   graph via G12 (replace one vertex by a triangle) then replacing 11 of the 12 vertices
   by H7 (a 7-vertex graph with three degree-2 attachment vertices u,v,w and no 2^m-cycles).
   G78 is 3-connected cubic (order 78).
4. **f(5) ≤ 450**: G450 from the girth-8 Tutte–Coxeter graph (30 vertices) replacing each
   vertex by H15 (two H7 glued with one extra vertex; no 2^m-cycles; attachments at
   distance 3,3,5) with the u-vertex on the chord edges to kill 32-cycles. Cubic, order 450.
5. **G420**: the 3-connected cubic **planar** graph of order 420 with no 4-, 8- or 16-cycles,
   from the buckyball C60 with each vertex replaced by H7. This shows Heckman–Krakovski's
   suggested "bound m ≤ 4 for planar cubic" is false; the m in their theorem must be ≥ 5.

## Implication / reconciliation with the live catalog

The live Exoo CYCLES catalog (isu.indstate.edu/ge/COMBIN/CYCLES, fetched this run) gives
the *current* smallest known values:
- smallest trivalent with no 4,6,10 cycles (N4610)
- trivalent order 32 with no 4,8,32 cycles (N4832)
- smallest trivalent with no 4 or 8 cycles = G24a (order 24; 3 others exist)
- smallest with no 4 or 6 cycles (N46)
- smallest with no 4,6,8 cycles (N468)
- **smallest known with no 4,8,16 cycles: 78 vertices**
- **smallest known with no 4,8,16,32 cycles: 540 vertices** (this is the newer figure;
  Exoo's 2014 paper says f(5) ≤ 450 for m≤5 = {4,8,16,32}). The 540 record is the
  current best-known, superseding the 450 construction as a "smallest known" claim.

So CONTEXT.md's "f(5)≤450" is the 2014 paper's construction bound; the catalog's 540 is
the newer smallest-known. Both sourced; the honest statement is "smallest known with no
C4,C8,C16,C32 is 540 vertices; Exoo 2014 constructs one on 450 vertices".

```claim
id: EG-exoo-f4-f5-bounds
statement: The smallest cubic graph with no 2^m-cycle for all m≤4 (i.e. no C4,C8,C16) has order between 54 and 78: lower bound 54 (unpublished Markström), upper bound 78 (Exoo G78). The smallest cubic with none for m≤5 (no C4,C8,C16,C32) is at most 540 vertices per Exoo's live catalog (2014 construction: 450).
hypotheses: cubic graphs avoiding all cycles of lengths 4,8,16 (resp. also 32).
holds-here: yes — these bound the run's counterexample-search frontier.
status: proved upper bounds by explicit construction (Exoo arXiv:1403.5636); lower bound 54 unpublished (Markström); 540 is smallest-known-not-proved.
bearing: Any claim "every C4,C8-free cubic graph has a C16" is FALSE at n=78; the C16-forcing picture is only at n=24. A cubic counterexample to EG must be C4,C8,C16,C32-free and hence have order ≥ 540 (known smallest), and ≥ 55 by the unpublished 54 bound.
anchor: research/sources/exoo-three-graphs-pdf.full.md
```