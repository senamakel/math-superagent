# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | _(undescribed)_ |
| `_append_board.py` | _(undescribed)_ |
| `_check_nmin.py` | _(undescribed)_ |
| `_cleanup.py` | _(undescribed)_ |
| `_drive_indep.py` | _(undescribed)_ |
| `_drive_main.py` | _(undescribed)_ |
| `_exec_oeis.py` | _(undescribed)_ |
| `_exec_shell.py` | _(undescribed)_ |
| `_noop.py` | _(undescribed)_ |
| `_placeholder.py` | _(undescribed)_ |
| `_robot.txt` | _(undescribed)_ |
| `_runner_placeholder.py` | _(undescribed)_ |
| `analyze_cores_small.py` | Classifies 4-critical cores of 4-chromatic sharp-kernel members and reports core vertex/edge-count distributions per n; the dominant 7v/11e core form is the Moser spindle. |
| `analyze_kernel_chrom.py` | Chromatic-number split of all sharp-kernel census members (n=8..11): reports per-n counts of 4-chromatic vs 3-colourable, the exact chromatic number of each member via the complete SAT oracle, and confirms the Moser spindle is NOT a kernel member (min-degree 3, K4-free) — the kernel is a sound superset of 5-critical UDGs. |
| `analyze_nonmoser_cores.py` | _(undescribed)_ |
| `bench_census_filter.py` | _(undescribed)_ |
| `brute.py` | Naive exact-arithmetic oracle for the unit-distance problem. Defines the field Q(sqrt3,sqrt11) with exact (rational) arithmetic, unit_graph(points) which certifies edges by squared distance exactly 1, and a complete backtracking k-colouring test with witness. Calibrated: reproduces the 7-point two-lozenges graph from problem.md with exactly 11 edges, chi=4, not 3-colourable — all in exact arithmetic, matching the worked example. |
| `calibrate_moser.py` | Gating calibration driver. Builds the Moser spindle via `moser_spindle()`, certifies all 11 edges exactly, reports the 4-colouring witness and k=3 UNSAT. Output: code/out/calibrate_moser.captured.txt. Result: chi=4 PASSED. |
| `calibrate_torus_7col.py` | _(undescribed)_ |
| `calibrate_torus_margin.py` | _(undescribed)_ |
| `census_kernel.py` | Census of the sharp-kernel C_N: enumerate all connected graphs on <=N vertices with min-deg>=4, K4-free, K2,3-free, nbhd-maxdeg<=2 via nauty-geng, and test each with the calibrated complete k=4 SAT oracle. Extended to pass geng flags -c (connected) and -k (K4-free, a required kernel condition) which prune the n=11 enumeration from 187M graphs to 6.2M, allowing the census to reach N=11 (228 kernel members, all 4-colourable) within the timeout. Result: every member of C_N is 4-colourable through N=11 (249 graphs total: n=8:1, n=9:4, n=10:16, n=11:228). Witness colourings written to code/out/census_kernel_n11.captured_witnesses.json. Independently cross-checked by crosscheck_kernel_n11.py. |
| `census_kernel_parallel.py` | _(undescribed)_ |
| `census_n11_test.py` | _(undescribed)_ |
| `check_alon_tarsi_direction.py` | _(undescribed)_ |
| `check_h2_three_circles.py` | _(undescribed)_ |
| `check_moser_containment.py` | Tests whether 4-chromatic sharp-kernel members contain the Moser spindle as a subgraph vs as an induced subgraph (exact permutation search). Finding: Moser is present as a subgraph in 118/198 n=11 four-chromatic members but never as an induced subgraph (kernel's min-degree>=4 excludes induced copies). |
| `check_moser_k4.py` | Verifies the Moser spindle contains no K4 subgraph (degrees 4,3,3,3,3,3,3) — correcting a claim in the pattern note; the min-degree>=4 kernel condition, not K4-freeness, is what excludes induced Moser copies. |
| `check_ns_edge_poly.py` | Exact sympy check that the Nullstellensatz colouring edge polynomial S_e=(x_u^4-x_v^4)/(x_u-x_v) vanishes iff the two 4th-roots-of-unity colours are distinct — the load-bearing identity of the nullstellensatz-colouring-certificate approach. |
| `confirm_moser_critical.py` | Confirms the Moser spindle (7v, 11e) is edge-critical: every single-edge removal is 3-colourable, so chi drops from 4 to 3. Used to establish that the dominant 7v/11e 4-critical core in the kernel census is exactly the Moser spindle. |
| `correct_torus_sweep.py` | _(undescribed)_ |
| `crosscheck_kernel_coloring.py` | Independent second-route re-verification of the sharp-kernel census 4-colourability result. Reads all 21 kernel members (n=8:1, n=9:4, n=10:16) and their SAT witnesses from code/out/census_kernel.captured_witnesses.json, and re-tests each with the DIFFERENT complete method lib.coloring.chromatic_colorable (exhaustive DSATUR backtracking with symmetry breaking) instead of the SAT oracle. For each member confirms (a) chromatic_colorable finds a proper 4-colouring and (b) the recorded SAT witness independently checks via verify_coloring. Result: all 21 agree 4-colourable (no mismatches). Output: code/out/crosscheck_kernel_coloring.captured.txt. This supersedes the older partial code/out/census_kernel_crosscheck.txt which only covered n=8,9 (5 members). |
| `crosscheck_kernel_n11.py` | Independent second-route re-verification of the sharp-kernel census extended to n=11. Reads all 249 kernel members (n=8:1, n=9:4, n=10:16, n=11:228) and their SAT witnesses from code/out/census_kernel_n11.captured_witnesses.json, re-tests each with the DIFFERENT complete method lib.coloring.chromatic_colorable (exhaustive DSATUR backtracking) and independently verifies each SAT witness. Result: all 249 agree 4-colourable, zero mismatches. Output: code/out/crosscheck_kernel_n11.captured.txt. This extends crosscheck_kernel_coloring.py (which covered n<=10) to the new n=11 members. |
| `crosscheck_triangle_sum.py` | Independent cross-check of the triangle-sum result: rebuilds the T+T point set in exact Q(sqrt3) rational arithmetic, counts n=6 distinct vertices and m=9 unit edges, and computes chi via the library complete SAT oracle (lib.satcolor). Confirms chi=3, agreeing with verify_sources.py by a second, distinct route. Output: code/out/crosscheck_triangle_sum.captured.txt. |
| `diag_mycielski.py` | Independent correct textbook Mycielski construction: mycielski(edges) with cross edges u_i v_j/u_j v_i plus apex star (4 |
| `edge_counts.py` | Parses the n=11 kernel member edge lists from analyze_kernel_chrom.captured.txt and tabulates the edge-count distribution (22:15, 23:112, 24:62, 25:9); confirms 198 lines == 198 four-chromatic n=11 members. |
| `enum_core_graphs.py` | Bounded oracle enumerating all 7-vertex 11-edge graphs to test (the wrong) edge-critical predicate; superseded — the Moser is edge-critical under the correct predicate (removal 3-colourable), and no 7v/11e graph is edge-critical in the buggy sense. Kept as the record that this check was done. |
| `explore_spindle.py` | Scratch exploration that first fixed the Moser spindle construction (two rhombi sharing vertex O rotated so far tips Q,Q' are at distance 1) and verified 11 unit edges and chi=4. Superseded by calibrate_moser.py but kept as the derivation record. Output: code/out/explore_spindle.captured.txt. |
| `forced_pair.py` | Forced-pair attack: for a graph, add each non-edge pair and test k-colourability; UNSAT => forced monochromatic. Stages: Moser spindle (4-col, none), diamond k=3 (tips forced equal, sqdist 3>=1/4, confirmed), H+H Minkowski sum (26v/69e, 4-colourable, none). Uses exact Q(sqrt3,sqrt11) via lib.unitfield and SAT via lib.satcolor. |
| `frac_chro_calib.py` | Fractional chromatic number chi_f of the exact calibration graphs (C5, diamond, Moser spindle) via the LP over the independent-set polytope (scipy highs), exact for these tiny graphs. Grounds the fractional-chromatic-lp-lower-bound approach; the run has never computed chi_f before. Written but NOT yet executed — the computation is filed as a REQUIRE query for tool_builder. |
| `frac_chro_verify_rational.py` | _(undescribed)_ |
| `frac_mosm_alpha.py` | _(undescribed)_ |
| `frac_mosm_lp.py` | chi_f(Moser+Moser) via dual fractional-colouring LP with MWIS cutting-plane separation (returns 7/2). |
| `frac_mosm_mwis.py` | _(undescribed)_ |
| `frac_mosm_primal.py` | _(undescribed)_ |
| `hoffman_bounds.py` | Hoffman spectral lower bound 1 - lambda_max/lambda_min on chi for the run's constructible exact-coordinate unit-distance graphs (Moser 7v/11e, Moser+Moser 26v/69e, diamond 4v/5e, triangular disk R=3 37pts). Edges built exactly from lib.unitfield; the bound is the cheap spectral relaxation from the adopted lovasz-theta/vector-chromatic approach. Calibrated: C5 gives sqrt5 (2.23606798), and Moser's float eigenvalues match the exact characteristic-polynomial eigenvalues. Result: max Hoffman=2.995 (triangular disk), nothing clears 4, so the spectral route cannot certify chi>=5 on this family. Output: code/out/hoffman_bounds.captured.txt. |
| `moser_chromatic_dc.py` | _(undescribed)_ |
| `moser_chromatic_dc2.py` | _(undescribed)_ |
| `moser_chromatic_extend.py` | _(undescribed)_ |
| `moser_chromatic_poly.py` | _(undescribed)_ |
| `moser_chromatic_poly_fit.py` | _(undescribed)_ |
| `mycielski_sequence2.py` | Re-derives the Mycielski-iterate recurrences (V: 5,11,23; E: 5,20,71) from the explicit construction rather than formula, and re-verifies that Mycielski^2(C5) (23v/71e/chi5) fails K2,3-freeness — confirming it is not a sharp-kernel counterexample and the N=11 size bound stands. Context: Mycielski graphs are not unit-distance graphs, so this is dead-end documentation, not a construction lead. |
| `pattern_core_isomoser.py` | Complete scan of the 198 n=11 four-chromatic kernel members: exactly 67 have a minimal 4-critical core that is 7-vertex/11-edge and isomorphic to the Moser spindle (permutation-correct). |
| `pattern_decode_core.py` | _(undescribed)_ |
| `pattern_full_moser_scan.py` | Full n=11 scan: 67/198 four-chromatic kernel members have a Moser-isomorphic minimal 4-critical core (reconfirms pattern_core_isomoser on all data). |
| `pattern_moser_chromatic_final.py` | Verifies the Moser spindle chromatic polynomial P_M(k)=k(k-1)(k-2)^2(k-3)(k^2-3k+4) against exact proper-colouring counts on the certified edge list from lib.unitfield, fitted at k=0..7 and checked out-of-sample at all k=1..14. Reconciles two stale deletion-contraction outputs (dc.txt, dc2.txt) that do NOT match the exact counts. |
| `pattern_moser_subgraph.py` | Permutation-correct Moser-as-subgraph check on sampled Moser-cored members: 8/8 contain the Moser as a non-induced subgraph. |
| `pattern_reconcile_moser.py` | Reconciles the earlier containMoser=0 bug: confirms Moser never appears as an induced subgraph of a kernel member (extra edges always present). |
| `pattern_verify_mycielski2.py` | Independent sympy second route proving Mycielski vertex/edge closed forms (V_k=3*2^k-1, E_k=(1-6*2^k+7*3^k)/2) from the construction recurrences; output pattern_verify_mycielski2.captured.txt ALL CHECKS PASS. |
| `refute_kernel_independent.py` | _(undescribed)_ |
| `refute_mycielski_kernel.py` | _(undescribed)_ |
| `run_check_ns_edge_poly.sh` | _(undescribed)_ |
| `run_frac_chro.py` | Runs the fractional-chromatic-number calibration computation on the exact calibration graphs. |
| `run_frac_chro.sh` | Runs the independent chi_f check (lib/frac_chro_verify.py) and the never-executed code/frac_chro_calib.py, capturing both to code/out/ with EXIT_CODE. |
| `run_refute_kernel.py` | _(undescribed)_ |
| `run_refute_kernel_independent.py` | _(undescribed)_ |
| `run_scholar_verify_frac.sh` | _(undescribed)_ |
| `run_scholar_verify_n11.py` | _(undescribed)_ |
| `run_scholar_verify_n11.sh` | _(undescribed)_ |
| `run_verify_frac.py` | _(undescribed)_ |
| `run_verify_frac_indep.py` | _(undescribed)_ |
| `run_verify_polytope_equalization.sh` | _(undescribed)_ |
| `sat_calibration.py` | Second, independent route to the Moser spindle calibration: CNF k-colourability encoding solved with real SAT solvers (PySAT Cadical153 and Minisat22), with exact reconstruction cross-check of the edge list and a pure-integer witness validator. Reproduces k=4 SAT with witness and k=3 UNSAT that brute.py's exhaustive route already established. |
| `sat_count_check.py` | Strengthened cross-check: compares the exact number of proper k-colourings of the 7-vertex Moser spindle obtained two independent ways — brute-force enumeration (oracle) vs SAT-based model enumeration via Cadical153 — agreeing exactly for every k (0,0,0,384,5040). No floats. |
| `scholar_check_edge_bounds.py` | Exact-rational re-derivation of the k=5 edge-count ladder coefficients (Dirac 1957, Gallai 1963, Krivelevich 1997, Kostochka-Yancey 2014) used in the size-bound direction. Written this session but NOT executed (no exec tool in the scholar environment); the coefficients were hand-verified by rational simplification instead. An executor with a shell should run it to produce captured output. |
| `scholar_frac_chro_calib.py` | Exact rational fractional-chromatic-number chi_f(G) calibration over the independent-set LP dual (fractional clique), via vertex enumeration over Fractions; computes chi_f(C5), chi_f(diamond), chi_f(Moser spindle). This is the OPEN REQUESTS computation for the fractional-chromatic-lp-lower-bound approach; run with `timeout 540 python3 code/scholar_frac_chro_calib.py |
| `scholar_run_verify.py` | _(undescribed)_ |
| `scholar_run_verify_capture.py` | Exact-arithmetic verification of four library claims (Minkowski-sum unit-distance condition, Eisenstein lattice units, k-critical min-degree sharpness, Minkowski-sum-of-segments as a unit-distance example). All Fraction/int exact arithmetic, no floats. Writes a JSON verdict meant to be captured to code/out/. This is the scholar's cheap-verification step so claims resting on a directly-checkable identity are not left at 'asserted'. |
| `scholar_verify_claims.py` | Scholar's independent verification of the library's load-bearing computational claims (minkowski-sum-unit-distance-condition, einstein-lattice-unit-distance, sat-k-colourability-encoding) in exact Q(sqrt3) arithmetic, upgrading them from `asserted` to `checked`. |
| `scholar_verify_frac.py` | Exact-rational verification of fractional chromatic numbers (C5=5/2, diamond=3, Moser=7/2) via dual-fractional-clique vertex scan over Q; upgrades the asserted chi_f claims to checked. |
| `scholar_verify_library.py` | Scholar's cheap exact verification of library algebraic claims (Eisenstein unit vectors/norm, Minkowski sum distance identity). Written but NOT run (no execution tool on scholar role); needs a tool_builder run to produce captured output that upgrades those claims from asserted to checked. |
| `scholar_verify_mycielski_transition.py` | Independent check of the Mycielski edge-count transition; settles the 3e+v vs 4e+v contradiction in the library notes. |
| `scholar_verify_n11.py` | _(undescribed)_ |
| `scholar_verify_newsource.py` | Scholar verification of the newest library material: Mycielski edge/vertex transition vs OEIS, recurrences A083329/A122695, K2,3-in-M^2(C5), and the REQUESTS-open Hoffman eigenvalue bound on the Moser spindle. |
| `scholar_verify_oeis_mycielski.py` | Cross-checks the OEIS-catalogued Mycielski vertex/edge sequences (A083329, A122695) against the run's verified textbook Mycielski construction, so the catalogue is not taken on faith. |
| `scratch_torus_explore.py` | _(undescribed)_ |
| `scratch_verify_a2_margin.py` | Sympy verification of the hand-derived A2 hexagonal 7-colouring margin: same-colour centre distance sqrt(21)*L, valid window 1/(sqrt21-2) < L < 1/2, min separation (sqrt21-2)/2 ~ 1.291. Corrects the record's sqrt(7)*L (lattice-norm units, missing sqrt3 centre-spacing factor). Hand-derived; tool_builder must run it before anything rests on it. |
| `sharp_nbhd_cert.py` | Exact symbolic certificate (sympy, no floats) for the sharp-neighbourhood lemma sharp-nbhd-local from research/backward/5chromatic-udg-min-size.md, the geometry of the whole size-bound skeleton. Verifies: (i) K4-freeness — Groebner basis [1] (unit ideal) proves |
| `tmp_census_capture.py` | _(undescribed)_ |
| `tmp_diag_sweep.py` | _(undescribed)_ |
| `torus_minsep_calib.py` | _(undescribed)_ |
| `verdict_mycielski_core.py` | Final verdict witness on the Mycielski kernel refutation claim: confirms Mycielski^2(C5) is 5-critical (every G-v 4-colourable), resolves the explicit K2,3 subgraph (vertices 0,2, common nbhd [1,6,12]), and reports the four sharp-kernel conditions. Result: fails K2,3-free, so not a counterexample. Correctness established by exact chromatic SAT oracle and the explicit K2,3. |
| `verify_5critical_conclusion.py` | Focused verifier of the load-bearing conclusion: every 5-chromatic graph (on <=6 vertices) contains a 5-critical subgraph with min degree >= 4. Exhaustive over the 173 graphs with chi>=5 up to 6 vertices via lib.critoracle. PASSED (no failures); all 172 reduce to a 5-vertex 5-critical subgraph with delta>=4. Output: code/out/verify_5critical_conclusion.txt. |
| `verify_calibration_independent.py` | Independent cross-check of the calibration written without reusing construction/colouring library logic: numeric+symbolic edge rebuild, independent differently-ordered exhaustive 3/4-colour search. Confirms 11 edges and chi=4 by a second route. Output: code/out/verify_calibration_independent.captured.txt. |
| `verify_chord_poly.py` | Symbolic (sympy) verification that the unit-circle chord/edge condition |
| `verify_critical_brute3.py` | Third, genuinely independent oracle for the sharp-critical-degree check: pure-Python product-enumeration proper-colouring search with NO symmetry breaking and NO SAT. Confirms brute_chrom equals critoracle.chrom on every graph up to 5 vertices (0 mismatches) and re-confirms the 5-critical conclusion (1 five-chromatic graph on <=5 vertices, 0 failures). PASSED. Output: code/out/verify_critical_brute3.txt. |
| `verify_critical_min_degree.py` | First (superseded) verifier of the sharp-critical-degree lemma, which used lib.coloring and FAILED spuriously, exposing a soundness bug in lib.coloring.chromatic_colorable (inconsistent symmetry break makes its not-colourable answers unreliable). Kept as the record of that discovery; superseded by verify_critical_min_degree2.py with the correct SAT oracle. Output: code/out/verify_critical_min_degree.txt (the FAILED run). |
| `verify_critical_min_degree2.py` | Verifier for the sharp-critical-degree lemma using lib.critoracle: complete enumeration over all 33,866 graphs on <=6 vertices, checking (1) every graph contains a vertex-critical same-chi subgraph by greedy deletion and (2) every vertex-critical graph has min degree >= chi-1. Cross-checks critoracle against lib.satcolor. PASSED. Output: code/out/verify_critical_min_degree2.txt. |
| `verify_dominant_core.py` | Canonicalizes the Moser spindle edge list and matches it to the dominant 7-vertex/11-edge 4-critical core form found in the sharp-kernel census — confirms the common core IS the Moser spindle. |
| `verify_k4check_bug.py` | Verifies the K4-check false positive in analyze_kernel_chrom.py's diagnostic loop vs the correct adjacency-required K4 check in census_kernel.check_kernel. Confirms on the Moser spindle: diagnostic prints 'Moser contains K4: True' (false positive, pairs (0,3)/(0,6) non-adjacent), independent 4-subset ground truth finds 0 real K4s, and census_kernel's K4 branch does not fire. Established the size-bound (<=11 vertices 4-colourable) is unaffected. |
| `verify_mycielski_both_variants.py` | Shows the K2,3 obstruction is robust to the choice of textbook Mycielski construction. Both the canonical no-mirror variant (3 |
| `verify_mycielski_k23_indep.py` | Independent cross-check (different adjacency-list build) that M^k(C5) k>=2 contains a K2,3, showing vertex 0 and 2 share 4 common neighbours {1,6,12,17} in M^2. Confirms the K2,3-freeness obstruction is the graph structure, not an artifact of one builder; M^k is K2,3-free iff k<=1. Output: code/out/verify_mycielski_k23_indep.captured.txt. |
| `verify_mycielski_k23_udg.py` | Shows M^k(C5) for k>=2 is NOT unit-distance realizable as a direct consequence of the K2,3-freeness lemma (no colouring oracle). Constructs M^0..M^4 with the correct textbook no-mirror Mycielskian (3 |
| `verify_polytope_equalization.py` | Independent verification of the load-bearing equalization counterexample of the projection-distance-equalization approach: 24-cell pair equalizing to one planar length under a rank-2 projection (shows projection is not a homothety), and the 24-cell vertex count. |
| `verify_projection_equalize.py` | Sympy machine check of the load-bearing equalization counterexample (24-cell diff vectors (0,2,0,0) and (0,-1,1,0) both project to squared norm 4 under rows a=(0,1,3,0), b=(0,0,0,1)). Written but NOT yet executed with captured output. |
| `verify_sources.py` | Cheap exact verification of three load-bearing sourced claims: (A) the six Eisenstein unit vectors have |
| `verify_torus_both.py` | _(undescribed)_ |
| `verify_tptp_false_positive.py` | Independent re-verification (not yet run — no exec tool here) of the kernel-4color TPTP false-positive: decodes the 8-vertex model, checks the four C_8 kernel conditions and exhaustively counts proper 3-/4-colourings. |
