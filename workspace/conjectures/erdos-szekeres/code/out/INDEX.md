# Index — code/out

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `README.md` | _(undescribed)_ |
| `RUN_notes.txt` | _(undescribed)_ |
| `_arr_bound.py` | _(undescribed)_ |
| `_cmd_ang.txt` | _(undescribed)_ |
| `_grid.py` | _(undescribed)_ |
| `_pad_tmp.py` | _(undescribed)_ |
| `_probe_index.py` | _(undescribed)_ |
| `_repro.py` | _(undescribed)_ |
| `_run_ang.py` | _(undescribed)_ |
| `_run_ang.sh` | _(undescribed)_ |
| `_run_noncov.py` | _(undescribed)_ |
| `_run_pattern_attack.py` | _(undescribed)_ |
| `_sweep.py` | _(undescribed)_ |
| `_time.py` | _(undescribed)_ |
| `_wedge_explore.py` | _(undescribed)_ |
| `_wedge_gauge.py` | _(undescribed)_ |
| `_wedge_pair_gauge.py` | _(undescribed)_ |
| `_wedge_ref.txt` | _(undescribed)_ |
| `_wedge_scratch.py` | _(undescribed)_ |
| `_witness_exact_check.py` | _(undescribed)_ |
| `allowable_encoder.captured.txt` | Old captured output of allowable_encoder.py (superseded by allseq_adjudicate.captured.txt): shows the pre-fix encoder's contradictory 'replay ok: False' alongside '120/120 adjacent', the old depth S2..S5 failing to match block index, and the old B test truncated at 5 disagreements (all 3-subsets, always convex — an early-break artifact, not a real signal). |
| `allowable_encoder.captured2.txt` | Identical duplicate of allowable_encoder.captured.txt (same content, second capture filename as referenced in the adjudication task). Kept for provenance; the authoritative adjudication capture is allseq_adjudicate.captured.txt. |
| `allowable_encoder.py` | First allowable-sequence encoder (superseded by allseq_adjudicate.py). Has a known replay bug: merged consecutive simultaneous blocks into one reversed run (wrong for disjoint parallel pairs) and dropped the initial permutation in the B-test extremes (permsS[1:]), plus early-break truncation at 5 disagreements. Kept on disk for the record of the failure; do not build on its replay. |
| `allseq_adjudicate.captured.txt` | Captured stdout of allseq_adjudicate.py: TEST 1 (circular-sequence axioms PASS n=4..7), TEST 2 (reversal depth constant n-1, depth==block-index FAIL), TEST 3 (contiguous-block convexity FAIL n=4 0/1, n=5 88/163, n=6 62096/64839), TEST 3b (extreme-in-projection criterion PASS n=5 163/163, n=6 64839/64839). Adjudication record for the allowable-sequence approach refutation. |
| `allseq_adjudicate.py` | Adjudicates the allowable-sequence approach. Reconstructs the exact Goodman-Pollack circular sequence of a point set by directed-line sweep (exact Fraction cross products), computes per-point reversal depth over one half-period, and tests (a) depth==block-index on es_construct n=4..7, (b) the contiguous-block convexity characterization vs the exact oracle es_geom.in_convex_position over all |
| `allseq_axiom_adjudication.captured.txt` | _(undescribed)_ |
| `allseq_axiom_adjudication.py` | Resolves the [A] axiom inconsistency in allowable_encoder.py: reproduces and pins the contradiction (old replay's run-merging of tied multi-event groups corrupts the permutation -> spurious non-adjacent-swap reports) while the corrected per-pair replay proves the Goodman-Pollack axioms hold on es_construct at n=4..7. Capture: allseq_axiom_adjudication.captured.txt. |
| `allseq_debug.py` | Debug harness that isolated the restricted-permutation replay bug: compared sequence-derived (first-or-last) extreme points per subset against an independent direct min/max-projection check on the failing subset [1,2,3,4] at n=6. Confirmed points 1 and 3 are direct extremes but were missed by the sequence replay (initial permutation at angle 0+ had been dropped: permsS[1:] bug), and that merged-run group reversal was wrong for disjoint parallel pairs. |
| `block_tight_sum.py` | _(undescribed)_ |
| `block_tightness.py` | _(undescribed)_ |
| `block_tightness_claim.md` | _(undescribed)_ |
| `block_tightness_n8.py` | _(undescribed)_ |
| `brute_existing.captured.txt` | _(undescribed)_ |
| `brute_oracle.captured.txt` | _(undescribed)_ |
| `cell_premise_audit.py` | _(undescribed)_ |
| `check_esz_construction.py` | _(undescribed)_ |
| `checker_vs_construction_resolution.md` | Steering-directive resolution: the convex-position checker (lib/es_geom) is CORRECT (verified on hand-known sets); the ES lower-bound constructions in this workspace are all DEFECTIVE and must be rebuilt before any structural argument cites them. Grounding for claims es-construction-broken-integer/-rational and es-construction-defective-checker-correct. |
| `commands.log` | _(undescribed)_ |
| `convex_spectrum.captured.txt` | _(undescribed)_ |
| `convex_spectrum.py` | Exact full convex-subset spectrum (convex k-subsets for k=3..n-1) of the verified es_construct ES construction at n=5,6,7, via the exact lib/es_geom oracle. Produces code/out/convex_spectrum.captured.txt. |
| `convex_spectrum_finding.md` | Records the pattern-finder finding on the convex-subset spectrum of es_construct: exact table, sequence-tool verdicts (k=4 row 38,1119,23220,422186 is an OEIS miss not low-degree polynomial), and unimodality/peak-at-n-2 conjecture. |
| `convex_spectrum_n8_k4.captured.txt` | _(undescribed)_ |
| `convex_spectrum_n8_k4.py` | Extends the convex-4-subset row of es_construct to n=8 (N=64, C(64,4)=635k exact convex tests), giving the 4th term 422186 used for the sequence-tool analysis. |
| `cupcap_claim.md` | _(undescribed)_ |
| `cupcap_oeis.py` | Verifies the cups/caps threshold f(k,k)=C(2k-4,k-2)+1 matches OEIS A323230 closed form C(2(n-1),n-1)+1 and the Pascal DP recurrence F(k,l)=F(k,l-1)+F(k-1,l). |
| `cupcap_tightness.py` | _(undescribed)_ |
| `cupcap_verify.txt` | _(undescribed)_ |
| `demo_cap_bug.py` | _(undescribed)_ |
| `es61_staircase_probe.py` | _(undescribed)_ |
| `evenodd_cutfamily.captured.txt` | Captured provenance run of evenodd_cutfamily.py (command + EXIT: 0, 23.5s wall, 28 workers, exact integer/Fraction arithmetic via verified lib.es_geom and lib.es_construct). Answers the directive-17 part-2 question: the even/odd split at n=7 is not a half-plane (k=1: 0), not a double-wedge side-intersection (k=2: 0, control reproduces record), but IS a triple side-intersection (minimum k=3, both halves, DP-exact over all k, brute k=3 scan and direct frozenset verification agree). Counting cut independently confirms no single line + tie-break realizes either half. Positive result — the cut family 'intersections of k>=3 sides' realizes even/odd at minimum k=3. |
| `evenodd_cutfamily.py` | Decides which side-intersection cut family realizes the even/odd block bipartition of es_construct at n=7. Reuses the validated ordered_pair_sides enumerator (592→992 sides), reduces k-side intersections to an exact minimum set-cover DP (min k=3, witnesses), runs explicit k=1,2,3 brute corroboration incl. steering counts (560 triples, 1 size-16 intersection each), plus an independent counting-cut check (no line+tie-break realizes either half). Captured EXIT 0: code/out/evenodd_cutfamily.captured.txt. Scoped to es_construct(7) only. |
| `evenodd_cutfamily_RESULT.md` | _(undescribed)_ |
| `evenodd_cutfamily_result.md` | Result write-up for evenodd_cutfamily.captured.txt: the even/odd block bipartition of es_construct at n=7 is realized by an intersection of exactly 3 open half-plane sides (min k over all k>=1), with the exact-reduction method (set-cover DP over the 16-bit complement universe), the verifying numbers (k=1 False, k=2 0/120 control, min k=3 both halves, exhaustive k=3 witness + direct frozenset verification, counting-cut independent check 0 hits), scope, and the close-reason text for the writing role. Written because the memory server was down (remember_memory/note_scratch both refused); to be stored to durable memory once it recovers. |
| `factorization_staircase_n7.captured.txt` | Clean EXIT-0 capture of factorization_staircase_n7.py (safe idiom): verifies at n=7 that the staircase placement of es_construct's blocks reproduces the arc placement's factorization and identical g (incl. middle-block g={0:1,1:10,3:46,4:41}), total 39648, 15 patterns. |
| `factorization_staircase_n7.py` | Confirms the per-block goodness-factorization survival extends to n=7: exact enumeration of all C(32,6) (n-1)-subsets under the staircase placement of es_construct's blocks vs the arc placement. Verifies factorization True on both and g values IDENTICAL (incl. middle-block g_2=g_3={0:1,1:10,3:46,4:41}), total 39648, 15 patterns. Capture: code/out/factorization_staircase_n7.captured.txt (EXIT 0). |
| `factorization_survival.captured.txt` | Clean EXIT-0 capture of factorization_survival.py (safe idiom): the deciding-scope test at n=6 — same es_construct blocks re-placed as arc / staircase / scrambled-y; factorization True with identical g for arc+staircase (802), False for scrambled-y (1464, 30 patterns, mismatches). Backs the scope-survival claim. |
| `factorization_survival.py` | Deciding-scope test for the per-block goodness factorization: keeps es_construct's blocks but re-places them (arc / staircase / scrambled) at n=6 and checks whether #(n-1)-convex-subset per block pattern factorizes as prod g_i(c_i). Result: factorization survives arc+staircase (identical g, 802) and breaks on scrambled-y (1464, mismatches). Its EXIT-0 capture is code/out/factorization_survival.captured.txt. |
| `goodness_T1_closedform.py` | _(undescribed)_ |
| `goodness_closedform.py` | _(undescribed)_ |
| `goodness_definitive.py` | _(undescribed)_ |
| `goodness_direct.py` | _(undescribed)_ |
| `goodness_direct2.py` | _(undescribed)_ |
| `goodness_existscheck.py` | _(undescribed)_ |
| `goodness_factorization.py` | _(undescribed)_ |
| `goodness_factorization_scope_claim.md` | Claim note for the per-block goodness factorization of es_construct's (n-1)-convex subsets, with its survival scope: exact n=4..7, holds on ES-consistent (convex-corridor/staircase) placements with identical g, FAILS on corridor-breaking placements. Answers the steer's deciding question; records OEIS misses for [1,10,46,41] and [4,38,802,39648]. |
| `goodness_middle_n8.py` | _(undescribed)_ |
| `goodness_middle_n9.py` | _(undescribed)_ |
| `goodness_middle_n9b.py` | _(undescribed)_ |
| `goodness_n8_sample.py` | _(undescribed)_ |
| `goodness_recovered.captured.txt` | Clean EXIT-0 capture of goodness_recovered.py under the safe idiom: the recovered per-block goodness g_i(c) for es_construct n=4..7 ([1,10,46,41] middle-block values at n=7), with all-patterns-factorized=True at every n. This is the provenance-anchored factorization data the scope-survival claim is measured against. |
| `goodness_recovered.py` | Formally verifies the block-pattern count factorization for (n-1)-convex subsets of es_construct: recovers per-block goodness g_i(c) from single-bump patterns and checks prod_i g_i(c_i)==exact count for every pattern at n=4..7 (all-patterns-factorized=True). The source of the recorded g-values (n=7 middle-block g_2=g_3={0:1,1:10,3:46,4:41}). |
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
| `gsplit_phase2.captured.txt` | _(undescribed)_ |
| `gsplit_seq.py` | _(undescribed)_ |
| `gsplit_state.md` | G-split question state. Status SUPERSEDED (steer 10): captured run was a shell error and pair-line counts (57/241/993, 6/4/2/0) are wrong in both directions; re-derive via rotating-line (task gsplit-enumeration-recheck). |
| `horton_verify.py` | Verifies the Horton (1983) empty-side construction S_k collects no empty convex 7-gon and is in general position, over exact integer determinants; reproduces claim horton-no-empty-7gon (needs coder to run). |
| `horton_verify_HANDOFF.md` | Scholar-to-coder handoff: exact command and expected result for running code/out/horton_verify.py to verify the newly-digested Horton 1983 primary. |
| `layer_conjecture_A.captured.txt` | Captured stdout + exit code of layer_conjecture_A.py: Conjecture A confirmed (PASS) at n=5,6,7. Established by exact Fraction coordinate matching against es_geom.convex_hull; no floating point. |
| `layer_conjecture_A.py` | Checks Conjecture A at n=5,6,7 against the verified es_construct.es_set_blocks: exact-Fraction block matching of convex_hull vertices, verifying (a) n-1 hull vertices, (b) exactly one per block, (c) hull block order 0..n-2. Output and exit code in layer_conjecture_A.captured.txt. Verdict: PASS at all three n. |
| `layer_extremality.captured.txt` | _(undescribed)_ |
| `layer_extremality.py` | Peels the onion layers of the verified es_construct ES construction with the exact es_geom oracle and checks Conjecture C (layer extremality): every layer is maximally convex under the no-convex-n-gon ceiling (layers of size >= n-1 contain n-1 convex points, smaller layers are fully convex). Established at n=5,6,7 (PASS); captured in layer_extremality.captured.txt. |
| `layer_extremality_claim.md` | _(undescribed)_ |
| `layer_extremality_indep.captured.txt` | _(undescribed)_ |
| `layer_extremality_indep.py` | Independent cross-check of the layer-extremality result (Conjecture C): re-peels the es_construct onion layers with a from-scratch gift-wrapping (Jarvis) hull and from-scratch orientation determinant instead of es_geom, confirming every layer is maximally convex at n=5,6,7 (PASS). Captured in layer_extremality_indep.captured.txt; verifies layer_extremality.py by a second algorithm. |
| `layer_profile_conjecture.md` | Claim Conjecture A about the ES construction's outer onion layer (one point per block, n-1 hull vertices, block-index order), with the machine check to run and its falsifier. |
| `maxconvex_structure.captured.txt` | _(undescribed)_ |
| `maxconvex_structure.py` | Exact full enumeration of maximal (n-1)-convex subsets of the verified es_construct ES set at n=5,6,7: counts (38/802/39648), full block-index-pattern distribution, and the transversal-conjecture verdict (FAIL) with witnesses. Uses lib/es_construct.es_set_blocks + lib/es_geom.in_convex_position (exact Fraction arithmetic). n=7 checks all C(32,6)=906192 subsets in ~125 s. |
| `maxconvex_structure_verify.captured.txt` | _(undescribed)_ |
| `maxconvex_structure_verify.py` | Second route validating maxconvex_structure: re-checks the recorded FAIL witnesses as convex via the 4-point criterion (independent of the hull test) and checks the companion structural fact that every full transversal (one point from each of the n-1 blocks) is in convex position, count == prod( |
| `maxconvex_structure_xcheck.captured.txt` | _(undescribed)_ |
| `maxconvex_structure_xcheck.py` | Independent re-enumeration of the pattern distribution using the 4-point criterion instead of the hull test; proves the per-pattern counts and totals (38/802/39648) are not an artifact of the convexity test implementation. n=7 re-run takes ~334 s. |
| `merge_geometry_probe.py` | _(undescribed)_ |
| `nnc_from_captured.py` | Derives the non-convex-4-subset counts NNC(N)=C(N,4)-convex4 of es_construct from already-captured convex-4 rows and evaluates the covering-ratio test NNC*C(N-4,n-4)>=C(N,n) at N=2^{n-2}; the first-step quantity of queued task con4-supersat-nnc-count. |
| `nnc_from_captured_claim.md` | _(undescribed)_ |
| `nonconvex4_cover.py` | _(undescribed)_ |
| `pat_corner_full_check.py` | Exhaustive exact verifier of the corner-block-pair characterization of the six FULL block patterns of es_construct (EXIT 0, n=5..7, all C(N,n-1) subsets). |
| `pat_sgc_check.py` | Cross-check of split-gon spectrum cup/cap numbers against chains_by_rightmost and es_geom; established that whole-set max cup and max cap are both n-1 (so max union=2n-4 is trivial). |
| `pattern_bijection_check.py` | Exact verification of the explicit bijection between realized (n-1)-convex block patterns of es_construct and unordered block pairs {L,R}; exhaustive n=4..7, sampled n=8. The formula/answer comes from here. |
| `pattern_bijection_claim.md` | Claim note for the explicit bijection: realized (n-1)-convex block patterns of es_construct = C(B,2) profiles c_L=L+1, c_R=B-R indexed by unordered block pairs; conjecture, exact n=4..7. |
| `pattern_blocks.py` | Per-block cup/cap bounds of the ES construction, es_construct, at n=6: all exact block invariants verified (cup<=n-i, cap<=i+2). |
| `pattern_class_count.py` | _(undescribed)_ |
| `pattern_class_n8_direct.py` | _(undescribed)_ |
| `pattern_class_n8_sample.py` | _(undescribed)_ |
| `pattern_class_triangular_claim.md` | Records the new finding that the number of distinct realized block-pattern classes among the (n-1)-convex subsets of es_construct(n) equals C(n-1,2) (triangular numbers), exact n=4..7, n=8 sampled; distinct from the six-FULL-pattern result. |
| `pattern_complete_n8.py` | Completeness check at n=8: proves (by explicit non-convex witness) that all 868 non-six block-count patterns are non-FULL, leaving only the six. |
| `pattern_corner_pairs_claim.md` | New exact regularity unifying the realized-pattern bijection and the six-FULL-pattern family on the verified es_construct: the six FULL (all-convex) block patterns are exactly the realized patterns whose pinning pair {L,R} lies wholly in the corner-block set CO={0,1,n-3,n-2} (C(4,2)=6 pairs). Verified exhaustively n=5..7. Conjecture; also records the 2n-4 split-gon max-union false lead. |
| `pattern_count_factorization.py` | _(undescribed)_ |
| `pattern_counts_extract.py` | _(undescribed)_ |
| `pattern_factor.py` | Computes, per block-count pattern of (n-1)-subsets of verified es_construct(n), the exact convex count and ratio, for n=5,6,7. Establishes exactly six FULL patterns (every realization convex). |
| `pattern_factor_n8.py` | Exhaustive out-of-sample test of the six FULL block-count patterns at n=8 (es_construct): all six reconfirmed all-convex (largest 1,012,500 realizations), five controls fail. |
| `pattern_factor_n9.py` | Randomized (60k samples each) supportive test of the six FULL block-count patterns at n=9; no refutation found. |
| `pattern_family_claim.md` | Claim note for the six-FULL-block-pattern family of (n-1)-convex subsets of es_construct, with evidence (exhaustive n=5..8, sampled n=9), the failed rule-characterization, bearer status, and anchor files. |
| `pattern_finder_report.md` | Consolidated pattern-finder report: resolves the checker-vs-construction disambiguation (es_construct.es_set is a CORRECT ES lower bound, n=4..7, two independent hull algorithms), catalogues the square ES threshold as A000051 and the cups/caps f(k,k) as A323230, and records the even/odd block-split structural finding (each half 2^{n-3}, (n-1)-avoiding). |
| `pattern_finder_report2.md` | This round's pattern findings: transversal-convexity conjecture (exact n=4..9), the gsplit count sequence [6,4,2,0], the uncatalogued distinct-convex counts, and block-tightness identity. |
| `pattern_finder_report3.md` | Round-3 pattern-finder report: mechanical confirmation (margin analysis + placement-breaking control) that transversal-convexity is a structural consequence of the convex-arc design (adjudication a), plus exact sequence-tool record over the run's computed integers and housekeeping per directive 13. |
| `pattern_finder_report4.md` | _(undescribed)_ |
| `pattern_finder_report5.md` | Round-5 pattern-finder report: upgrades the triangular realized-pattern-class count to an explicit verified bijection with unordered block pairs. |
| `pattern_finder_report6.md` | This round's pattern-finder report: the new exact convex-subset spectrum of es_construct (k=4 row 38,1119,23220,422186 is a real OEIS miss and not low-degree polynomial), the peak-at-k=n-2 unimodality conjecture, and re-confirmation of the established template sequences. Describes the template only; does not bound ES(n). |
| `pattern_finder_report7.md` | _(undescribed)_ |
| `pattern_finder_report8.md` | _(undescribed)_ |
| `pattern_finder_report9.md` | Pattern-finder round 9: re-survey confirms no new sequence since round 8; the only newer artifact is an ES oracle self-check reproduction. Verdict NOTHING FURTHER — inventory of all sequence-bearing data unchanged, cross-family comparison impossible (second family not realized on disk). |
| `pattern_finder_round2.md` | Pattern-finder round-2 report: the full-transversal count of es_construct equals A001142 (every transversal convex, verified to n=9); the distinct-convex sequence [4,38,802,39648] is not in OEIS and shows no closed form; reversal-symmetry of pattern counts; gsplit/onion counts are non-regularities. |
| `pattern_hm_n8.py` | Refutes the last unproven non-six pattern (0,0,3,1,1,2,0) as FULL at n=8 with sampled witness [14,9,19,32,52,62,57], completing the six-pattern exactness. |
| `pattern_layers.py` | Convex-layer peeling and whole-set cup/cap spectra of es_construct.es_set at n=4..7. |
| `pattern_probe.py` | Extracts the run's exact oracle sequences: circle convexity, cups/caps f(k,k), ES(n) conjecture values, and es_set(n) cup/cap/largestConvex spectra. |
| `pattern_reversal.py` | Exact checker of the reversal-symmetry and full-transversal=A001142 regularities of the maximal (n-1)-convex subsets of es_construct (pattern counts symmetric under block-index reversal; (1..1) diagonal count = prod C(n-2,i)). Confirms both at n=5,6. |
| `pattern_rule_n7.py` | Tests and refutes the naive 'interior blocks take <=1' characterization of FULL block patterns at n=7 (72 counterexamples). Records that the exact rule is the 6-pattern family. |
| `radial_probe.py` | _(undescribed)_ |
| `radon_rank_check.py` | Exact check that in rank-3 (planar) affine geometry every 4-subset of a general-position set is a circuit — refutes the radon-circuit-no-radon-4set approach's premise that circuit membership distinguishes convexity. |
| `run_transversal_adjudicate.py` | _(undescribed)_ |
| `seq_extract.py` | Extracts exact integer sequences from es_construct: distinct (n-1)-convex-subset counts, full-transversal counts (=A001142), and gsplit valid-split counts, n=4..7. |
| `spacing_probe.py` | _(undescribed)_ |
| `split_gon_spectrum.py` | _(undescribed)_ |
| `split_probe.py` | _(undescribed)_ |
| `staircase_probe.py` | _(undescribed)_ |
| `step1_checker_selfcheck.py` | _(undescribed)_ |
| `transversal_adjudicate.py` | Adjudicate whether transversal-convexity of es_construct is a structural consequence (tiny clusters on a strictly convex arc) or placement-specific, by re-realizing the ES block structure with varied cluster scale and arc geometry under exact arithmetic. |
| `transversal_adjudicate_margin.py` | Margin analysis measuring cluster diameters vs the convex-arc corridor (slope-drop x spacing), showing >8 orders of magnitude scale separation that forces every full transversal onto a strictly convex chain (supports verdict that transversal-convexity is a structural consequence of the design). |
| `transversal_adjudication.captured.txt` | _(undescribed)_ |
| `transversal_adjudication.py` | Adjudicates whether 'every full transversal of es_construct is convex' is a structural consequence (tiny clusters on a strictly convex arc) vs a discovery about extremal sets. Parts A-E: (A) reproduce largest_convex_subset(es_set(5..6))=4,5 and point counts 8/16; (B) enumerate all full transversals, all convex (9 at n=5, 96 at n=6); (C) hull is one point per block in block order (n-1 vertices); (D) arbitrary within-cluster perturbations keep all transversals convex; (E) generic circle clusters (sizes 1,3,3,1) contain a convex 5-gon (largest 6) yet all 9 transversals convex. Uses only verified lib.es_construct/es_geom. Verified: EXIT 0 in code/out/transversal_adjudication.captured.txt; verdict in code/out/transversal_adjudication_verdict.md. |
| `transversal_adjudication_verdict.md` | Verdict of the transversal-convexity adjudication: the lemma 'clusters near distinct convex-position centers on a strictly convex arc => every full transversal convex' is VERIFIED as a structural consequence of es_construct's design (Parts C+D), NOT a discovery; Part E shows the forward direction fails (generic circle clusters have convex transversals without being n-avoiding), so it does NOT characterize n-avoiding sets and has no bearing on the ES upper bound. |
| `transversal_all_convex.py` | _(undescribed)_ |
| `transversal_breaking.py` | Placement-breaking control for the transversal-convexity adjudication: keeps identical es_construct blocks but replaces convex-arc centers with scrambled/random y, showing transversal-convexity and n-avoidance both fail off the arc (verdict a, structural consequence). |
| `transversal_convex_n8.py` | Exact out-of-sample test of the es_construct transversal-convexity finding at n=8: all 162,000 full transversals convex (zero non-convex), via lib/es_geom Fraction arithmetic. |
| `transversal_convex_n9.captured.txt` | Captured output of transversal_convex_n9.py: all 26,471,025 transversals of es_construct at n=9 convex (zero non-convex), EXIT 0. Input to the adjudicated claim es-construct-transversal-convexity. |
| `transversal_convex_n9.py` | Exact (integer-scaled coordinates) out-of-sample test of transversal-convexity at n=9: all 26,470,125 full transversals convex (zero non-convex). Confirms the conjecture extends far beyond the n=5..7 data. |
| `transversal_convexity_claim.md` | Adjudicated claim for es_construct transversal-convexity (directive 13): records that every full transversal is convex (verified n=4..9), adjudged a structural consequence of the template's cup/cap-free design + Conjecture A, NOT a discovery about extremal sets in general; names the open characterization question. |
| `transversal_geom_probe.py` | Shows es_construct blocks are minuscule clusters (~1e-5 wide) around centers ~1000 apart on a strictly convex arc — the structural basis for transversal-convexity. |
| `triple_inter.captured.txt` | Captured output of triple_inter_capture.py (EXIT: 0). |
| `triple_inter_capture.py` | Provenance capture script: fresh exhaustive k=3 triple-intersection check for the even/odd block bipartition of es_construct at n=7. Reuses validated ordered_pair_sides (imported from gsplit_enum_definitive); enumerates ALL C(16,3)=560 triples per superset family with exact set intersections (no DP, no sampling); reproduces the k=1/k=2 controls; exit 0 only if all gates assert. Output: code/out/triple_inter.captured.txt |
| `verify_block_tightness_brute.py` | _(undescribed)_ |
| `verify_cupcap_brute.py` | _(undescribed)_ |
| `verify_es_construct.py` | Verifies es_construct.es_set is a correct ES lower bound (N=2^{n-2}, general position, largest convex subset = n-1) at n=4..7, using the es_geom oracle. |
| `verify_es_construct_indep.py` | Independent verification of es_construct.es_set using gift-wrapping (Jarvis) hull from scratch, cross-checking largest convex subset and general position at n=4..6. Confirms the main verify script by a separate algorithm. |
| `wedge_cell_enum_corrected.captured.txt` | _(undescribed)_ |
| `wedge_cell_enum_corrected.py` | _(undescribed)_ |
| `wedge_enum_full_captured.txt` | _(undescribed)_ |
| `wedge_evenodd_alln.captured.txt` | Capture of wedge_evenodd_alln.py (EXIT 0): even/odd block split realization per cut family: n=5,6 double-wedge yes / line no; n=7 neither family; all three (n-1)-avoiding. |
| `wedge_evenodd_alln.py` | Extends the directive-16 framing answer to n=5,6,7: tests whether the even/odd block bipartition of es_construct is realized by a single open half-plane side and by a double-wedge side-pair intersection at each n. Exact arithmetic. Result: n=5,6 -> NOT a line, IS a double wedge; n=7 -> neither. |
| `wedge_evenodd_check.captured.txt` | Capture of wedge_evenodd_check.py (EXIT 0): at n=7 the even/odd block split of es_construct is 6-avoiding (largest convex subset 5 on both halves) yet is NOT among the 2454 size-16 double-wedge (side-pair intersection) bipartitions. |
| `wedge_evenodd_check.py` | Answers the directive-16 framing question at n=7: is the even/odd block bipartition of es_construct realized as an intersection of two open half-plane sides (double wedge)? Recomputes the 2454 size-16 intersections from scratch, tests membership of the even/odd bipartition, and independently re-verifies both halves 6-avoiding by largest_convex_subset (2^16 each, exact). Result: NO (but both halves are 6-avoiding). |
| `wedge_sidepair.captured.txt` | _(undescribed)_ |
| `wedge_sidepair.captured2.txt` | Completed capture of wedge_split_v2.py (EXIT 0, 156.7s on 28 workers): the directive-16 double-wedge side-pair enumeration on es_construct(7). Positive control PASS; 491,536 side pairs -> 13,030 size-16 pairs -> 2,454 distinct bipartitions -> 27 valid splits (both halves 6-avoiding), vs 0 for single open half-planes at n=7. Witness split realized as proper wedge at apex (2400,2725). |
| `wedge_sidepair_adjudication.md` | Adjudicated record of the wedge-split-n7-arbiter task: 27 valid double-wedge (side-pair intersection) splits at n=7 vs 0 single-line splits; even/odd block split is double-wedge-realizable at n=5,6 but not at n=7, though (n-1)-avoiding at all three. Scoped to the es_construct template; captures cited. Written because the memory server was down and the task ledger is director-owned. |
| `wedge_split.py` | _(undescribed)_ |
| `wedge_split_enum.py` | _(undescribed)_ |
| `wedge_split_v2.py` | _(undescribed)_ |
| `wedge_witness_ang.py` | _(undescribed)_ |
| `wedge_witness_convex.py` | _(undescribed)_ |
| `which_construction_is_verified.py` | _(undescribed)_ |
| `whole_cap_only.py` | _(undescribed)_ |
| `whole_cupcap.py` | _(undescribed)_ |
| `whole_cupcap_extend.py` | _(undescribed)_ |
| `whole_cupcap_fast.py` | _(undescribed)_ |
| `whole_cupcap_probe.py` | _(undescribed)_ |
