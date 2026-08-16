# Exoo — Three Graphs and the Erdős–Gyárfás Conjecture

Source: Geoffrey Exoo, "Three Graphs and the Erdős-Gyárfás Conjecture",
arXiv:1403.5636 (22 Mar 2014). Full text abstract held at
`sources/exoo-three-graphs-G420-no-4-8-16.full.md` (PDF body not converted;
the abstract carries the load-bearing facts here).

## What it establishes

Three cubic graphs relevant to the Erdős–Gyárfás conjecture, each derived from
a famous symmetric graph:

1. **G420** — derived from the **Buckyball** (the 60-vertex C60 fullerene
   graph). A **3-connected cubic planar** graph with **no 4-, 8-, or 16-cycles**.
   This is a partial answer to Heckman–Krakovski's bound: they proved every
   3-connected cubic planar graph has a 2^m-cycle with m ≤ 7, and asked how far
   the bound could be lowered. G420 shows it cannot be lowered to m ≤ 3 or 4
   (i.e. a guaranteed {4,8,16}) even in this class: it avoids 4, 8, and 16
   simultaneously, so the 2-power cycle in such a graph must be at length ≥ 32.
2. A graph derived from the **Petersen graph** — appears to be the **smallest
   known cubic graph with no 2^m-cycle for m ≤ 4** (no 4, 8, 16).
3. A graph derived from the **Tutte–Coxeter graph** — appears to be the
   **smallest known cubic graph with no 2^m-cycle for m ≤ 5** (no 4, 8, 16, 32).

## Why it matters here

This is the cleanest primary-source pinning of the **short-2-power obstruction**:
within the very class Heckman–Krakovski settled (3-connected cubic planar), you
cannot hope for a uniform 4- or 8-cycle — G420 needs a 2-power cycle of length
≥ 32. So any structural forcing argument that claims "δ≥3 forces a C4 or C8" is
false *even in the cubic planar class*, and any argument that claims "girth ≥ 5
forces an 8-cycle" (e.g. the Gebendorfer preprint's abstract) must be checked
against these high-girth constructions.

It also agrees with and tightens the catalogue data already held
(`sources/exoo-cubic-no-4-8-16.full.md`): smallest known no-{4,8,16} = 78
vertices, no-{4,8,16,32} = 540 vertices. The Petersen- and Tutte–Coxeter-derived
examples here are the "appear to be smallest known" instances of those two
avoidances.

```claim
id: exoo-g420-no-4-8-16-cubic-planar
statement: There exists a 3-connected cubic planar graph (G420, derived from the Buckyball) with no cycle of length 4, 8, or 16; its 2-power cycle, if any, must have length ≥ 32. Heckman–Krakovski's m ≤ 7 cannot be lowered to m ≤ 4 even in the 3-connected cubic planar class.
hypotheses: 3-connected, cubic, planar
holds-here: yes — pins the obstruction within an already-settled class
status: sourced (Exoo arXiv:1403.5636)
bearing: refutes any 'short 2-power forcing' claim (C4/C8 guaranteed) even in cubic planar; check any girth-dichotomy proof (e.g. Gebendorfer) against it
anchor: research/sources/exoo-three-graphs-G420-no-4-8-16.full.md
contradicts: none — G420 lies inside Heckman–Krakovski's settled class (hk-cubic-planar) and still contains a 2^m-cycle with m ≥ 5; it refutes only the informal conjecture that the uniform bound could be lowered to m ≤ 4, which is not a held claim id. The distinction to record: this pinpoints the shortest-2-power obstruction inside an already-settled class
```
