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
| `gsplit_enum_definitive.captured.txt` | Phase-1 rotating-line validation (N=8..16 exact N(N-1), 0 missing/0 extra) — but NO command+exit line, so steer 10 requires re-capture under the safe command; Phase-2 n=5,6,7 counts are superseded until then. |
| `gsplit_enum_definitive.py` | Correct rotating directed-line (ordered-pair) enumeration `ordered_pair_sides` + 2^N disjoint-hulls oracle. Phase-1 validated (N(N-1), 0 missing/0 extra). REUSE this enumerator for the steer-10 rotating-line replacement; re-capture Phase 2 with the safe command. |
| `gsplit_enum_definitive_claim.md` | Phase-1 enumeration validity stands (checked); Phase-2 n=5,6,7 split counts SUPERSEDED (steer 10) pending a fresh rotating-line run. |
| `gsplit_enum_recheck.py` | _(undescribed)_ |
| `gsplit_enum_validate.captured.txt` | _(undescribed)_ |
| `gsplit_enum_validate.py` | _(undescribed)_ |
| `gsplit_exhaustive.captured.txt` | SUPERSEDED (steer 10): shell error (`${PIPESTATUS[0]}` under /bin/sh), script never re-ran. |
| `gsplit_exhaustive.py` | Pair-line enumerator — WRONG in both directions (steer 10: 50/222/946 with 33-40 false positives on es_construct). Replace `candidate_bipartitions` with the rotating-line enumerator from `gsplit_enum_definitive.py`. |
| `gsplit_exhaustive_claim.md` | SUPERSEDED (steer 10): 6/4/2/0 and 57/241/993 came from the wrong pair-line enumerator; claim marked superseded pending rotating-line re-run. |
| `gsplit_line.py` | Confirms binomial identity sum_{i even} C(m,i)=2^{m-1} and tests strict line-separability of even/odd block halves (found NOT strictly separable in this radial placement). |
| `gsplit_oracle_bruteforce.py` | _(undescribed)_ |
| `gsplit_state.md` | G-split question state. Status SUPERSEDED (steer 10): captured run was a shell error and pair-line counts (57/241/993, 6/4/2/0) are wrong in both directions; re-derive via rotating-line (task gsplit-enumeration-recheck). |
| `layer_conjecture_A.captured.txt` | Captured stdout + exit code of layer_conjecture_A.py: Conjecture A confirmed (PASS) at n=5,6,7. Established by exact Fraction coordinate matching against es_geom.convex_hull; no floating point. |
| `layer_conjecture_A.py` | Checks Conjecture A at n=5,6,7 against the verified es_construct.es_set_blocks: exact-Fraction block matching of convex_hull vertices, verifying (a) n-1 hull vertices, (b) exactly one per block, (c) hull block order 0..n-2. Output and exit code in layer_conjecture_A.captured.txt. Verdict: PASS at all three n. |
| `layer_extremality.captured.txt` | _(undescribed)_ |
| `layer_extremality.py` | Peels the onion layers of the verified es_construct ES construction with the exact es_geom oracle and checks Conjecture C (layer extremality): every layer is maximally convex under the no-convex-n-gon ceiling (layers of size >= n-1 contain n-1 convex points, smaller layers are fully convex). Established at n=5,6,7 (PASS); captured in layer_extremality.captured.txt. |
| `layer_extremality_claim.md` | _(undescribed)_ |
| `layer_extremality_indep.captured.txt` | _(undescribed)_ |
| `layer_extremality_indep.py` | Independent cross-check of the layer-extremality result (Conjecture C): re-peels the es_construct onion layers with a from-scratch gift-wrapping (Jarvis) hull and from-scratch orientation determinant instead of es_geom, confirming every layer is maximally convex at n=5,6,7 (PASS). Captured in layer_extremality_indep.captured.txt; verifies layer_extremality.py by a second algorithm. |
| `layer_profile_conjecture.md` | Claim Conjecture A about the ES construction's outer onion layer (one point per block, n-1 hull vertices, block-index order), with the machine check to run and its falsifier. |
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
