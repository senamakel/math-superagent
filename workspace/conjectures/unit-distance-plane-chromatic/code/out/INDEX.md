# Index — code/out

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `README.md` | _(undescribed)_ |
| `analyze_4critical_cores.captured.txt` | _(undescribed)_ |
| `analyze_cores_nauty.captured.txt` | _(undescribed)_ |
| `analyze_cores_small.captured.txt` | _(undescribed)_ |
| `analyze_kernel_chrom.captured.txt` | _(undescribed)_ |
| `brute_calibration.txt` | _(undescribed)_ |
| `calibrate_moser.captured.txt` | Captured output of the gating calibration: exact Moser spindle coordinates, all 11 certified unit edges, 4-colouring witness, k=3 UNSAT, verdict chi=4 PASSED. |
| `census-kernel-n11-result.md` | Records the run's strongest verified partial result: every unit-distance graph on <= 11 vertices is 4-colourable, via the sharp-critical-degree + sharp-nbhd-local + C_11 census, each machine-checked. Corrects the older N=10 bound. |
| `census_kernel.captured.txt` | Captured output of the sharp-kernel census: per-N kernel counts and the verdict that every member of C_N is 4-colourable through N=10 (n=8:1, n=9:4, n=10:16, total 21, all 4-colourable, zero failures). |
| `census_kernel.captured_witnesses.json` | One proper 4-colouring witness stored per kernel member, indexed by (n, graph). |
| `census_kernel_crosscheck.txt` | Superseded partial cross-check: lib.coloring backtracking at k=4 on n=8,9 only (5 members), all 4-colourable, not 3-colourable where noted. Superseded by crosscheck_kernel_coloring.captured.txt (all 21). |
| `census_kernel_n11.captured.txt` | Captured output of the sharp-kernel census extended to N=11 (nauty-geng -c -d4 -k): n=11 adds 228 kernel members, all 4-colourable, extending the verified bound from N=10 to N=11 (249 total: n=8:1, n=9:4, n=10:16, n=11:228). |
| `census_kernel_n11.captured_witnesses.json` | One proper 4-colouring witness per sharp-kernel member through n=11 (n=8:1, n=9:4, n=10:16, n=11:228, total 249). |
| `census_kernel_n11_run.captured.txt` | _(undescribed)_ |
| `census_kernel_n11_test.captured.txt` | Quick small-case smoke test of the geng -k/-c prune (n<=11) confirming the streaming decode path. |
| `census_kernel_n11attempt.captured.txt` | Earlier unpruned n=11 attempt (geng -d4 only, 187M graphs) that timed out at n=11 — superseded by the -k/-c-pruned run in census_kernel_n11.captured.txt. |
| `census_kernel_streamcheck.txt` | Superseded streaming check of the sharp-kernel census through N=10 (matches census_kernel.captured.txt: n=8:1, n=9:4, n=10:16). |
| `census_kernel_streamcheck_witnesses.json` | Witness colourings from the streaming through-N=10 check (matches census_kernel.captured_witnesses.json). |
| `check_alon_tarsi_direction.md` | _(undescribed)_ |
| `check_moser_containment.captured.txt` | _(undescribed)_ |
| `commands.log` | _(undescribed)_ |
| `crosscheck_kernel_coloring.captured.txt` | Full independent second-route cross-check of the sharp-kernel census: all 21 kernel members (n=8:1, n=9:4, n=10:16) re-tested for 4-colourability with lib.coloring.chromatic_colorable (exhaustive DSATUR backtracking, a different complete method than the SAT oracle), plus independent verification of every recorded SAT witness. Result: all 21 agree 4-colourable, no mismatches. |
| `crosscheck_kernel_n11.captured.txt` | Independent second-route cross-check of the n=11 sharp-kernel census: all 249 kernel members (incl. all 228 at n=11) re-tested 4-colourable by exhaustive DSATUR backtracking, all SAT witnesses verified, 249/249 AGREE, zero mismatches. Also re-confirms the 21 at n<=10. |
| `crosscheck_triangle_sum.captured.txt` | Independent second-route confirmation via the library SAT oracle: T+T = 6 vertices, 9 unit edges, chi=3. PASSED, agrees with verify_sources.captured.txt. |
| `diag_mycielski.captured.txt` | _(undescribed)_ |
| `enum_core_graphs.captured.txt` | _(undescribed)_ |
| `explore_spindle.captured.txt` | _(undescribed)_ |
| `forced_pair.captured.txt` | Complete forced-pair SAT test: Moser spindle (7v,11e) and Moser+Moser (26v,69e) have NO pair with |
| `fractional-chromatic-values.md` | Records the computed fractional chromatic numbers of the run's calibration graphs (C5=5/2, diamond=3, Moser=7/2, Moser+Moser=7/2), the exact rational dual witness for Moser, and the reconciliation of the stale "never computed" claim in REQUESTS/approaches; claim blocks chi-f-moser-values and chi-f-moser-exact-argument. |
| `hoffman_bounds.captured.txt` | Hoffman spectral chi-lower-bound on the constructible family, exact-coordinate graphs. Calibrated on C5 (=sqrt5) and Moser (exact char-poly eigenvalues match float eig). Values: Moser 2.712, Moser+Moser 2.864, diamond 2.640, triangular disk R=3 2.995. Nothing clears 4, so the spectral relaxation cannot certify chi>=5 on these graphs (negative datum for the adopted theta route). |
| `kernel_slice_0.log` | Per-residue completion log for residue 0 of the mod-28 N=11 kernel census: 'processed <N> graphs, <k> kernel members, <t>s'. The 28 slice logs together partition nauty-geng 11 -d4 (sum = 187,095,840 full graph count) and sum to 228 kernel members; normal termination of every slice shows complete enumeration with no timeout. |
| `kernel_slice_1.log` | _(undescribed)_ |
| `kernel_slice_10.log` | _(undescribed)_ |
| `kernel_slice_11.log` | _(undescribed)_ |
| `kernel_slice_12.log` | _(undescribed)_ |
| `kernel_slice_13.log` | _(undescribed)_ |
| `kernel_slice_14.log` | _(undescribed)_ |
| `kernel_slice_15.log` | _(undescribed)_ |
| `kernel_slice_16.log` | _(undescribed)_ |
| `kernel_slice_17.log` | _(undescribed)_ |
| `kernel_slice_18.log` | _(undescribed)_ |
| `kernel_slice_19.log` | _(undescribed)_ |
| `kernel_slice_2.log` | _(undescribed)_ |
| `kernel_slice_20.log` | _(undescribed)_ |
| `kernel_slice_21.log` | _(undescribed)_ |
| `kernel_slice_22.log` | _(undescribed)_ |
| `kernel_slice_23.log` | _(undescribed)_ |
| `kernel_slice_24.log` | _(undescribed)_ |
| `kernel_slice_25.log` | _(undescribed)_ |
| `kernel_slice_26.log` | _(undescribed)_ |
| `kernel_slice_27.log` | _(undescribed)_ |
| `kernel_slice_3.log` | _(undescribed)_ |
| `kernel_slice_4.log` | _(undescribed)_ |
| `kernel_slice_5.log` | _(undescribed)_ |
| `kernel_slice_6.log` | _(undescribed)_ |
| `kernel_slice_7.log` | _(undescribed)_ |
| `kernel_slice_8.log` | _(undescribed)_ |
| `kernel_slice_9.log` | _(undescribed)_ |
| `n11_census_verify.md` | Tool-builder's adversarial verdict on the N=11 size-bound census claims: confirms the 28 slice logs sum to exactly 187,095,840 graphs (matching full nauty-geng 11 -d4) and 228 kernel members, confirms both SAT (Cadical) and independent DSATUR (lib.coloring) routes report all 228 4-colourable with 0 fails (plus an independent re-check of kernel conditions and proper witnesses), confirms N=11 is the largest verified N and that no N=12 artifact exists. No heavy re-enumeration performed. |
| `refute_kernel.captured.txt` | _(undescribed)_ |
| `refute_kernel_independent.captured.txt` | _(undescribed)_ |
| `refute_kernel_verify.captured.txt` | _(undescribed)_ |
| `refute_kernel_verify.md` | _(undescribed)_ |
| `sat_calibration.captured.txt` | _(undescribed)_ |
| `sat_count_check.captured.txt` | _(undescribed)_ |
| `scholar_verify_claims.captured.txt` | Captured output of scholar_verify_claims.py after fixing the `six`-set bug: minkowski-sum identity on 2000 exact Q(sqrt3) pairs, Eisenstein units over [-12,12]^2, SAT 4-SAT/3-UNSAT on Moser spindle — ALL PASSED. |
| `scholar_verify_library.captured.txt` | Captured output of scholar_verify_library.py (Eisenstein six units N==1, Minkowski-sum identity on all pairs, K_k critical min-degree): ALL CHECKED, no floats. |
| `sharp_nbhd_cert.captured.txt` | Exact symbolic certificate (no floats) for the sharp-nbhd-local lemma: K4-free (Groebner unit ideal), K2,3-free (resultant elimination, at most two real roots), and neighbourhood max-degree <= 2 ( |
| `torus_margin.captured.txt` | Captured output of code/lib/torus_margin.py: exactly re-derives the A2 hexagonal-tiling 7-colouring margin (same-colour centre factor sqrt21·L, valid window 1/(sqrt21-2) < L < 1/2), machine-verifies chi(F(A2,L))=7 in-window (6-col UNSAT / 7-col SAT, quotient = K7), and sweeps 30 rational-slope sublattices of A2 at k=6: 24 six-colourable, 6 needing 7. Periodic-6 search not closed (census only). |
| `verdict_mycielski_core.captured.txt` | _(undescribed)_ |
| `verify_5critical_conclusion.txt` | Captured output of the 5-critical-conclusion verification: PASSED over all 173 graphs with chi>=5 on <=6 vertices; every one reduces to a k-critical subgraph with delta>=k-1, and the 5-critical subgraph always has delta>=4 (all 172 reduce to a 5-vertex 5-critical subgraph). |
| `verify_calibration_independent.captured.txt` | _(undescribed)_ |
| `verify_critical_brute3.txt` | Captured output of the independent brute-force re-check: brute_chrom agrees with critoracle.chrom over all graphs up to 5 vertices (0 mismatches), and the 5-critical conclusion passes (1 five-chromatic graph on <=5 vertices, 0 failures). PASSED. |
| `verify_critical_min_degree.txt` | Captured FAILED output of the first (superseded) sharp-critical-degree verification using lib.coloring — spuriously reported thousands of violations that are actually a lib.coloring soundness bug. Retained as the record that exposed the bug; the real result is in verify_critical_min_degree2.txt (PASSED). |
| `verify_critical_min_degree2.txt` | Captured output of the sharp-critical-degree verification with the correct SAT oracle: PASSED over all 33,866 graphs on <=6 vertices (90 vertex-critical, 0 min-degree<chi-1 violations, 0 critical-subgraph failures), plus 0 critoracle-vs-satcolor oracle mismatches. |
| `verify_mycielski_k23_notes.md` | Working note (task deliverable) recording that M^k(C5) for k>=2 is not unit-distance realizable as a direct consequence of the K2,3-freeness lemma, independent of any colouring oracle. States the two premises (certified K2,3-free lemma from sharp_nbhd_cert + explicit K2,3 on vertices 0,2 sharing {1,6,12} in M^2), the exact counts table for M^0..M^4, and the robustness check across construction variants. Working note generated by code/verify_mycielski_k23_udg.py and its siblings. |
| `verify_sources.captured.txt` | Captured output verifying the six Eisenstein unit vectors have |
