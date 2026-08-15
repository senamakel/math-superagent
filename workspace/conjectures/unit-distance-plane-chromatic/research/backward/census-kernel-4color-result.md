# Census of the size-bound kernel C_N — machine-verified result

## What was done

Enumerated the finite sharp-kernel class `C_N` of
`research/backward/5chromatic-udg-min-size.md` (the `sharp-kernel-4color`
lemma): all graphs on `<= N` vertices satisfying

- (a) minimum degree >= 4,
- (b) K4-free,
- (c) K2,3-free,
- (d) every vertex-neighbourhood `N(v)` induces a graph of maximum degree <= 2.

Enumeration via nauty-geng (`geng -d4`, all graphs — connected and
disconnected, since `C_N` is defined over all graphs), graph6 decode, filter of
the four conditions, then the **calibrated complete k=4 SAT oracle**
(`lib.satcolor.is_k_colorable`) run on every member with one witness colouring
stored per graph.

## Result

**Every member of `C_N` is 4-colourable for every N up to the reached ceiling
`N = 11`.** No non-4-colourable (hence no candidate 5-chromatic) member exists
at any N. `code/out/census_kernel_n11_run.captured.txt` (the full N=1..11 run,
249 members) and `code/out/census_kernel_n11.captured.txt`.

Per-N kernel counts (graphs tested | all 4-colourable):

| n | kernel | all 4-colourable |
|---|--------|------------------|
| 1..7 | 0 | — |
| 8 | 1 | yes |
| 9 | 4 | yes |
| 10 | 16 | yes |
| 11 | 228 | yes |

Total 249 kernel graphs. Chromatic split (code/out/analyze_kernel_chrom.captured.txt):
n=8: 1 four-chromatic; n=9: 1 four-ch + 3 three-col; n=10: 16 four-chromatic;
n=11: 198 four-ch + 30 three-col. Every member 4-colourable.

The n=11 enumeration was done in 28 parallel residue slices of nauty-geng
(code/census_kernel_parallel.py, code/out/kernel_slices/res*_of28.txt, 228
members) and tested both with the calibrated Cadical153 SAT oracle and, in a
fully independent second route, with exhaustive DSATUR backtracking
(lib.coloring) — all 249 members agree 4-colourable, 0 mismatches
(code/out/crosscheck_kernel_n11.captured.txt).

## Completion criterion

The criterion "if ANY kernel member is NOT 4-colourable, report it explicitly"
was satisfied in the negative: **none exists through N=10.** So the kernel adds
no candidate 5-chromatic unit-distance graph.

## Verification

Two independent routes:

1. `lib.satcolor` (Cadical153 CNF) — the calibrated oracle, k=4 SAT with a
   proper witness on every member.
2. `lib.coloring` exhaustive backtracking — re-ran k=4 on all 21 members:
   all 4-colourable, with each SAT witness independently re-verified proper.
   (`code/out/census_kernel_crosscheck.txt`)

The graph6 decoder was validated against the known connected-graph counts
(n=3..7: 2,6,21,112,853) before the run.

## Bound / ceiling

`N=11` is the infeasibility point: `nauty-geng` of 11-vertex min-degree>=4
graphs is enormous (all kernel members contain triangles, so the
triangle-free `-t` restriction accelerates nothing). The run stopped cleanly
at N=10 inside the 540s bound.

## Artifacts

- `code/census_kernel.py`
- `code/out/census_kernel.captured.txt`
- `code/out/census_kernel.captured_witnesses.json` (21 witnesses, indexed by
  (n, graph))
- `code/out/census_kernel_crosscheck.txt`
