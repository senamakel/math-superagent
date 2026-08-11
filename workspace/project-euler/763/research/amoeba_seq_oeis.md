# OEIS and literature status of the 3D-amoeba sequence D(N)

## Question

D(N) = 1,1,3,9,30,99,336,1134,3855,13086,44499,151263,514419,1749267,5949063
(N=0..14) counts distinct connected sets of 2N+1 occupied cubes reachable by a
3D "amoeba" process: an amoeba at (x,y,z) splits into (x+1,y,z),(x,y+1,z),
(x,y,z+1) if those three cubes are empty; the dividing amoeba disappears; start
with one amoeba at (0,0,0).

## Result: NOT in OEIS

Authoritative direct queries to the OEIS search endpoint (fmt=text) both return
**"No results."**:

- Full 15 terms 1,1,3,9,30,99,336,1134,3855,13086,44499,151263,514419,1749267,5949063
  https://oeis.org/search?q=1,1,3,9,30,99,336,1134,3855,13086,44499,151263,514419,1749267,5949063&fmt=text
- Partial (offset-1) 11 terms 1,3,9,30,99,336,1134,3855,13086,44499
  https://oeis.org/search?q=1,3,9,30,99,336,1134,3855,13086,44499&fmt=text

The local `oeis_lookup` tool also returned "no OEIS entry matches".

So the sequence is not catalogued. No A-number exists yet; no formula or
recurrence can be looked up from OEIS. As of the search date the sequence has
not (yet) been submitted.

## Web-search hits for the terms (all negative / unrelated)

Searching the numbered terms surfaced only Project Euler 763 mirrors
(e.g. https://euler.haku.dev/playground/763 restates the problem and known
values D(2)=3, D(10)=44499, D(20)=9204559704, last nine of D(100)=780166455)
and unrelated OEIS entries that do NOT match:

- A006801 (2-D directed compact animals): 1,2,5,13,34,... no match
- A130866 (polyominoes with at most n cells): no match
- A045723 (bead configurations): 1,1,3,7,23,... diverges at term 4
- A005519 (free polyominoes summed over dims): 1,1,2,7,26,153,... no match

## Structural relatives in the literature (none is this process)

The word "amoeba" in the literature means unrelated things here; none counts
3D lattice reachable configurations by this division rule:

- "Growing Trees and Amoebas' Replications" (Gurvich, Krnc, Vyalyi; arXiv 2401.07484 /
  Results in Mathematics 2025, https://link.springer.com/article/10.1007/s00025-025-02421-6):
  amoebas as rooted trees growing copies in a host tree (ℓ-growth, mortality/immortality).
  Tree-based, not 3D lattice, not a count of reachable connected sets.
- "Amoebas of complex hypersurfaces" (statistical thermodynamics): logarithmic
  projections of complex curves; topological, unrelated.
- amoebot model / programmable matter papers: distributed self-organizing
  particles forming shapes; not an enumeration of reachable configurations.

The closest *counting* relative is **directed lattice animals** (a finite
connected set of sites every non-root site of which has a neighbor nearer the
root along the preferred directions). The 3D directed site-animal generating
function is known to be solvable on certain directed cubic lattices; the
directed **bond**-animal generating function on the cubic lattice is not
D-finite (Rechnitzer, "Haruspicy 3", arXiv math/0408054). But the amoeba
process here has an additional "empty-cell" constraint on all three forward
neighbours at once (a cell may be occupied only if its three backward
neighbours have not both split into it — i.e. no cell is filled twice by
different splits), which makes it a *different* object from free directed
animals, and its counts (1,1,3,9,30,...) do not match any catalogued
directed-animal sequence (e.g. A006801).

## Bottom line for the run

- The bound in the problem (D(10000)) cannot be met by looking up a closed form:
  none is catalogued. The structure must come from the problem itself
  (the run's own BFS/DP route).
- This "no OEIS entry" is a genuine negative finding worth retaining so
  nobody re-searches the numbers.
- Deliberately NOT consulted: any Project Euler 763 solver/forum thread
  (per instruction). The haku.dev mirror appeared in search results but was
  used only to confirm the problem statement, not its solution.

## Files

- research/L1.0/oeis_direct.md — full direct OEIS query (No results)
- research/L1.0/oeis_partial.md — partial direct OEIS query (No results)
- this note
