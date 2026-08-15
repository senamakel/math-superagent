# Verdict: N=11 size-bound census claims vs. captured artifacts

Reviewer: tool-builder (adversarial). No heavy re-enumeration performed — this
verdict checks the recorded artifacts for existence, completeness, internal
consistency, and agreement with the claims in
`code/out/census-kernel-n11-result.md`.

## (1) Do the captured outputs / logs exist and show complete enumeration?

**YES — all 28 slices present, no timeout, sum = 228 kernel members.**

- `code/out/kernel_slice_0..27.log` — 28 files, each with a normal-termination
  line `RES=r/28: processed <N> graphs, <k> kernel members, <t>s`. None shows a
  timeout/kill/killed marker (grep for error/timeout/OOM across all four
  captured files and the logs found none).
- The 28 per-residue member dumps exist: `code/out/kernel_slices/res0..27_of28.txt`
  (28 files). The 6 slices logged as `kernel=0` (res 11,13,15,17,19,23) have
  **empty** res files — exactly consistent with zero members found.
- **Graph-count completeness:** the 28 slice counts sum to **187,095,840**,
  which matches *exactly* the full `nauty-geng 11 -d4 | wc -l` total recorded
  twice in `commands.log` (187,095,840). The residue classes mod 28 partition
  the search space, so no graph is missed.
- **Kernel-member count:** slice kernel counts sum to **228**, matching the
  recorded n=11 count. (The note's "~185M graphs" is a shallow approximation of
  the true 187,095,840 — a cosmetic rounding, not a substantive gap.)

## (2) Does the crosscheck re-verify all 228 as 4-colourable by the independent DSATUR route with 0 fails?

**YES.** Two artifacts record the independent route, plus my own re-check:

- `code/out/census_kernel_n11_test.captured.txt`: `unique kernel members: 228`,
  `all 228 members 4-colourable: True`, `failures: 0`, and
  `independent backtracking cross-check (lib.coloring): backtracking all-4col
  universal: True (0 fails)`.
- `code/out/crosscheck_kernel_n11.captured.txt`: exhaustively lists all 249
  kernel members (n=8:1, n=9:4, n=10:16, n=11:228) and for each shows
  `bt4col=True` (lib.coloring exhaustive DSATUR backtracking) **and**
  `satWitnessChecks=True` (Cadical153, witness proper). Footer: "TOTAL kernel
  members re-verified: 249, Members both oracles agree 4-colourable: 249, No
  mismatches."
- **My independent re-verification** (O(edges) per graph, reads `res*_of28.txt`
  and `census_kernel_n11.captured_witnesses.json`): 228 distinct canonical
  members, all on 11 vertices, all satisfying all four kernel conditions
  (min-deg>=4, K4-free, K23-free, nbhd-maxdeg<=2) with 0 violations, all 228
  stored SAT witnesses **proper** 4-colourings, and JSON edge sets == res-file
  edge sets. So the recorded artifacts are internally consistent.

Note the two *enumeration* routes agree too, which strengthens completeness:
the single-process `--maxn 11` run (`census_kernel.captured.txt` / n11 run)
used `nauty-geng 11 -c -d4 -k` (connected, K4-free-pruned, 6 249 149 graphs),
while the 28-slice run used full `nauty-geng 11 -d4` (187 095 840, connected
and not). Both produced **228** kernel members and identical n=8,9,10 counts
(1,4,16), which match the earlier N=10 census exactly.

## (3) Largest N, and any N=12 artifact?

- **Largest N for which the census shows every unit-distance graph 4-colourable: N = 11.**
  Per-N kernel counts recorded and reproduced across artifacts:
  n<=7:0, n=8:1, n=9:4, n=10:16, n=11:228; total 249; **zero** non-4-colourable
  members (failures=0 in every captured file).
- **There is NO artifact attempting N=12.** Search of `code/out`, `code/`, and
  the command log found no `geng 12`, no n=12 census output, no N=12 run. The
  only `kernel_slice_12.log` is slice index 12 of the mod-28 N=11 split, not an
  N=12 run. The result note itself states N=12 was not attempted ("N=12 is a
  scaling question (~100M+ more graphs), not a claimed result"). So **N=11 is
  the claimed and verified ceiling; N=12 is unclaimed and unattempted**, and
  no recorded claim asserts N=12.

## Claim status

- `sharp-nbhd-local`: **supported** — `code/out/sharp_nbhd_cert.captured.txt`
  shows all three geometric conditions certified symbolically over exact
  symbolic fields ("OVERALL: ALL CERTIFICATES PASS"; Groebner unit ideal for
  K4-freeness, resultant/quadratic-root-count for K23, exact cosine identity
  +-60° for the neighbourhood-degree bound). This is a symbolic certificate,
  reviewed as such, not a floating-point number.
- `sharp-kernel-4color-n11`: **supported** by the complete 28-slice
  enumeration (graph-count exact match = 187 095 840) and both the Cadical and
  DSATUR 4-colourability routes reporting 0 failures; my independent member-level
  check reproduces all kernel conditions and proper witnesses.
- `size-bound-udg-4color-n11`: **supported to the extent the three steps are
  sound** — it is an assembled deduction (5-critical $\Rightarrow\delta\ge4$;
  + sharp-nbhd-local; + sharp-kernel-4color-n11). The computational steps are
  machine-verified; the graph-theoretic/geometric lemmas are certified
  symbolically. No gap found between the recorded claims and the actual
  captured outputs, apart from the cosmetic "~185M" vs 187 095 840 and the
  note's correct explicit statement that N=12 was not attempted.

Verdict: **claims stand**; N=11 is the verified ceiling, N=12 unattempted.
