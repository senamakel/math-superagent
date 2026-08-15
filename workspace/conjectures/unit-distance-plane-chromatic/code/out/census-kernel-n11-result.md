# Size-bound result through N=11 — machine-verified

This note records the run's strongest verified partial result as a `checked`
claim, correcting the older records (CONTEXT.md, `census-kernel-4color-result.md`)
which bound the size-result at N=10. The verified artifacts reach **N=11**.

## The theorem established

**Every unit-distance graph in R^2 on at most 11 vertices is 4-colourable.**
Equivalently, every 5-chromatic unit-distance graph has at least 12 vertices
(so any finite witness for chi(R^2) >= 5 needs >= 12 vertices).

## Why it is true — the three-step deduction, all machine-verified

Let H be a minimal counterexample: a 5-chromatic unit-distance graph on
<= 11 vertices with fewest vertices. Then H is 5-critical.

1. **`sharp-critical-degree`** (checked): H contains / is a 5-critical subgraph
   with minimum degree >= 4. A 5-critical graph is connected.
2. **`sharp-nbhd-local`** (certified symbolically): as a unit-distance graph,
   H is K4-free, K2,3-free, and every vertex-neighbourhood induces a graph of
   maximum degree <= 2.
3. Hence H is a member of the kernel `C_11` = { graphs on <= 11 vertices :
   min degree >= 4, K4-free, K2,3-free, neighbourhood max-degree <= 2 }.
   **`sharp-kernel-4color` through N=11** (checked): every member of `C_11` is
   4-colourable. Contradiction with chi(H)=5.

## The census (sharp-kernel-4color, N=11) — completeness and verification

- Enumeration: `nauty-geng 11 -d4 res/mod` for all 28 residues mod 28,
  streaming on all 28 CPUs (`code/out/kernel_slice_0..27.log`). Each slice
  processed 5.8–7.5M graphs (~185M total), all 28 residues completed (none
  timed out). The 28 residue classes partition the min-degree>=4 graphs on 11
  vertices exactly, so the scan is complete.
- Filter: `check_kernel` applies conditions (a)–(d) (min-deg>=4, K4-free,
  K2,3-free, nbhd max-deg <= 2). Per-slice kernel counts sum to **228** unique
  members.
- Colourability: every one of the 228 members is 4-colourable by **two
  independent routes** — Cadical153 CNF (`lib.satcolor`, the calibrated oracle,
  with a proper witness) — confirmed by
  `code/out/census_kernel_n11_test.captured.txt` where `lib.coloring` exhaustive
  backtracking independently re-checks all 228 as 4-colourable (0 fails). n=8,9,10
  counts (1, 4, 16) in the same n11 run agree exactly with the earlier
  `census_kernel.captured.txt`, validating the decoder/filter pipeline.

Per-N kernel counts (n=1..7: 0; n=8: 1; n=9: 4; n=10: 16; n=11: 228), all
4-colourable, zero failures.

## Bound / ceiling

N=11 is the largest **completed** enumeration. N=12 was not attempted in
these artifacts; the note `census-kernel-4color-result.md` (which says the
infeasibility point is N=11) predates the parallel 28-slice run and is
superseded by it. Pushing to N=12 is a scaling question (~100M+ more graphs),
not a claimed result.

## Claim blocks

```claim
id: sharp-nbhd-local
statement: >
  In any unit-distance graph in R^2: (i) no four vertices are pairwise at unit
  distance (K4-free); (ii) two distinct vertices share at most two common
  neighbours (K2,3-free); (iii) two neighbours of a vertex are adjacent iff the
  angle between them is exactly 60 degrees, so every vertex-neighbourhood
  induces a graph of maximum degree <= 2 (disjoint union of paths and 6-cycles).
hypotheses: finite point set in the Euclidean plane, edges iff distance exactly 1.
holds-here: YES — the geometric kernel condition that makes the finite
  enumeration tiny and sound.
status: checked (exact symbolic certificate, no floats:
  code/out/sharp_nbhd_cert.captured.txt, ALL CERTIFICATES PASS: Groebner unit
  ideal for (i), resultant elimination + at-most-two-real-roots for (ii),
  exact trig identity |x-y|^2 = 2 - 2 cos(delta) = 1 iff delta = +-60deg for (iii))
bearing: together with sharp-critical-degree it places any 5-critical
  unit-distance graph inside the finite kernel C_N.
anchor: code/out/sharp_nbhd_cert.captured.txt (+ research/backward/5chromatic-udg-min-size.md gap)
falsifies: a unit-distance graph with a K4, a K2,3, or a vertex whose
  neighbourhood has degree >= 3 — none exists by the certificate; a legend
  check is the Moser spindle (neighbourhoods are paths/fragments).
```

```claim
id: sharp-kernel-4color-n11
statement: >
  Every graph on at most 11 vertices with minimum degree >= 4, K4-free,
  K2,3-free, and every vertex-neighbourhood of maximum degree <= 2 is
  4-colourable. (The sharp-kernel-4color lemma, verified through N = 11.)
hypotheses: finite simple graphs on <= 11 vertices satisfying the four kernel
  conditions; k=4 colourability decided by a complete oracle.
holds-here: YES — C_11 is exactly the class a 5-critical unit-distance graph
  must lie in (by sharp-critical-degree + sharp-nbhd-local), so this is the
  finite check that carries the size bound.
status: checked (exhaustive enumeration over all 28 residue classes of
  min-degree>=4 11-vertex graphs — complete; 228 kernel members; all
  4-colourable by Cadical SAT with proper witnesses AND independent
  lib.coloring backtracking: 0 fails)
bearing: the finite check that closes the size-bound skeleton through N=11.
anchor: code/out/census_kernel_n11_run.captured.txt,
  code/out/census_kernel_n11_test.captured.txt, code/out/kernel_slice_*.log
falsifies: a member of C_11 that is not 4-colourable — none found; the scan
  was exhaustive over all 28 residues.
```

```claim
id: size-bound-udg-4color-n11
statement: >
  Every unit-distance graph in R^2 on at most 11 vertices is 4-colourable;
  every 5-chromatic unit-distance graph has at least 12 vertices.
hypotheses: finite unit-distance graphs (points in R^2, edges iff |x-y|=1).
holds-here: YES — this is the GOAL.md-reachable size-bound deliverable, at its
  best verified extent (N=11).
status: checked (a proof assembled from three machine-checked steps: the
  critical-degree lemma, the sharp-nbhd-local geometric kernel, and the
  C_11 census, each verified in code/out/)
bearing: the strongest partial result the run has established; a concrete lower
  bound on the size of any 5-chromatic witness (so any chi>=5 witness needs
  >= 12 vertices).
anchor: code/out/census_kernel_n11_run.captured.txt,
  code/out/sharp_nbhd_cert.captured.txt, research/backward/5chromatic-udg-min-size.md
follows-from: sharp-critical-degree, sharp-nbhd-local, sharp-kernel-4color-n11
falsifies: a 5-chromatic unit-distance graph on <= 11 vertices (none by the
  three verified steps); or a flaw in any of the three steps.
```
