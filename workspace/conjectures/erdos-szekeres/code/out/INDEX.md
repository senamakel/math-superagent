# Index — code/out

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `README.md` | _(undescribed)_ |
| `RUN_notes.txt` | _(undescribed)_ |
| `block_tight_sum.py` | _(undescribed)_ |
| `block_tightness.py` | _(undescribed)_ |
| `block_tightness_claim.md` | _(undescribed)_ |
| `block_tightness_n8.py` | _(undescribed)_ |
| `check_esz_construction.py` | _(undescribed)_ |
| `checker_vs_construction_resolution.md` | Steering-directive resolution: the convex-position checker (lib/es_geom) is CORRECT (verified on hand-known sets); the ES lower-bound constructions in this workspace are all DEFECTIVE and must be rebuilt before any structural argument cites them. Grounding for claims es-construction-broken-integer/-rational and es-construction-defective-checker-correct. |
| `commands.log` | _(undescribed)_ |
| `cupcap_claim.md` | _(undescribed)_ |
| `cupcap_oeis.py` | Verifies the cups/caps threshold f(k,k)=C(2k-4,k-2)+1 matches OEIS A323230 closed form C(2(n-1),n-1)+1 and the Pascal DP recurrence F(k,l)=F(k,l-1)+F(k-1,l). |
| `cupcap_tightness.py` | _(undescribed)_ |
| `cupcap_verify.txt` | _(undescribed)_ |
| `es61_staircase_probe.py` | _(undescribed)_ |
| `gsplit_consistent.py` | Tests G-split-consistent on the correct es_construct construction: even/odd block halves each have size 2^{n-3} and are (n-1)-avoiding at n=5,6,7. |
| `gsplit_exhaustive.captured.txt` | _(undescribed)_ |
| `gsplit_exhaustive.py` | Exhaustive all-lines split test for steering item 3: for each of C(N,2) pair-lines through points of the es_construct construction, plus all perturbations assigning on-line points, check whether any side of exactly 2^{n-3} points has (n-1)-avoiding complement at n=4..7. NEEDS TO BE RUN — no captured output yet. |
| `gsplit_exhaustive_claim.md` | Claim note (status: checked) recording the captured result of running gsplit_exhaustive.py against the verified es_construct ES construction: n=5 gives 4 valid straight-line splits into two 2^{n-3} (n-1)-avoiding halves, n=6 gives 2, n=7 gives 0 over 993 line-bipartitions — so the G-split pattern fails on this template at n=7. Full stdout with command and exit code is in gsplit_exhaustive.captured.txt. |
| `gsplit_line.py` | Confirms binomial identity sum_{i even} C(m,i)=2^{m-1} and tests strict line-separability of even/odd block halves (found NOT strictly separable in this radial placement). |
| `gsplit_state.md` | Steering item 3 state: the even/odd block split is a dead guess (not line-separable, captured), the exhaustive all-lines split test exists but is NOT yet run — question genuinely open on the verified construction; what an empty result would and would not rule out. |
| `layer_profile_conjecture.md` | Claim Conjecture A about the ES construction's outer onion layer (one point per block, n-1 hull vertices, block-index order), with the machine check to run and its falsifier. |
| `layer_conjecture_A.py` | Checks Conjecture A at n=5,6,7 against the verified es_construct.es_set_blocks: exact-Fraction block matching of convex_hull vertices, verifying (a) n-1 hull vertices, (b) exactly one per block, (c) hull block order 0..n-2. Output and exit code in layer_conjecture_A.captured.txt. Verdict: PASS at all three n. |
| `layer_conjecture_A.captured.txt` | Captured stdout + exit code of layer_conjecture_A.py: Conjecture A confirmed (PASS) at n=5,6,7. Established by exact Fraction coordinate matching against es_geom.convex_hull; no floating point. |
| `merge_geometry_probe.py` | _(undescribed)_ |
| `pattern_blocks.py` | Per-block cup/cap bounds of the ES construction, es_construct, at n=6: all exact block invariants verified (cup<=n-i, cap<=i+2). |
| `pattern_finder_report.md` | Consolidated pattern-finder report: resolves the checker-vs-construction disambiguation (es_construct.es_set is a CORRECT ES lower bound, n=4..7, two independent hull algorithms), catalogues the square ES threshold as A000051 and the cups/caps f(k,k) as A323230, and records the even/odd block-split structural finding (each half 2^{n-3}, (n-1)-avoiding). |
| `pattern_layers.py` | Convex-layer peeling and whole-set cup/cap spectra of es_construct.es_set at n=4..7. |
| `pattern_probe.py` | Extracts the run's exact oracle sequences: circle convexity, cups/caps f(k,k), ES(n) conjecture values, and es_set(n) cup/cap/largestConvex spectra. |
| `radial_probe.py` | _(undescribed)_ |
| `spacing_probe.py` | _(undescribed)_ |
| `staircase_probe.py` | _(undescribed)_ |
| `step1_checker_selfcheck.py` | _(undescribed)_ |
| `verify_es_construct.py` | Verifies es_construct.es_set is a correct ES lower bound (N=2^{n-2}, general position, largest convex subset = n-1) at n=4..7, using the es_geom oracle. |
| `verify_es_construct_indep.py` | Independent verification of es_construct.es_set using gift-wrapping (Jarvis) hull from scratch, cross-checking largest convex subset and general position at n=4..6. Confirms the main verify script by a separate algorithm. |
| `which_construction_is_verified.py` | _(undescribed)_ |
| `whole_cupcap.py` | _(undescribed)_ |
