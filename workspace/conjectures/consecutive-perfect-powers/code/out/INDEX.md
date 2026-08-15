# Index — code/out

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `README.md` | _(undescribed)_ |
| `_run_pillai.py` | _(undescribed)_ |
| `attempt2_verification.note.md` | _(undescribed)_ |
| `brute.captured.txt` | _(undescribed)_ |
| `caseB.captured.txt` | Captured output (EXIT 0) of code/caseB/certify_lebesgue_caseB.py: full PASS/FAIL trace for the Case-B reduction (steps 1-5 all PASS) and the step-6 numeric check that T(c,p) is not a square for c in [1,2000], odd prime p in [3,101] (50000 pairs, 0 squares, nearest gaps listed). Largest c reached 2000, ~0.28s for the box. |
| `caseB.note.md` | Result note for Code B (Lebesgue) certification: x^p-y^2=1 (p odd prime) reduction machine-certified (steps 1-5), T(c,p) non-square verified numerically (c<=2000, odd p<=101, 50000 pairs, 0 squares) and asserted by the classical Ljunggren theorem (not proved here). Claim block exp2-case-B-reduction, status reduction-proved + lemma verified-numeric/classical-asserted (NOT status:proved), follows the steering correction that the two-square bound fails for large p. |
| `caseB_complete_closure.captured.txt` | Captured output (EXIT 0, RESULT: ALL CHECKS PASS, TOTAL 8.49s) of code/caseB/caseB_complete_closure.py: slice stated (n=p odd prime>=3, X=c^2+1, residual X≡1 mod 4); both Nagell-Ljunggren exceptions excluded by exact assertions (n=4 even; c^2=2 impossible; X=3,7 fail X≡1 mod 4); exact oracle T(c,p) not square for c even in [2,200000], odd primes p in [3,199] (4.5e6 pairs, 0 squares, 7.78s parallel); direct enumeration of (X^n-1)/(X-1)=Y^2 for n in {2,3,4,5}, X in [2,10^6] finds exactly (4,7,20) and (5,3,11) and none else in odd indices 3,5. |
| `caseB_complete_closure.note.md` | Result note + claim block (id caseB-complete-closure-nagell-ljunggren) for the complete Case-B closure via Nagell-Ljunggren, exact for the slice. Lists proved-in-workspace (reduction, mod-8 classification, exception-exclusion verified here, oracle) vs asserted-classical (the Nagell-Ljunggren theorem itself, standard citation asserted not fetched; exceptions reproduced numerically). Status: Case B proved conditional on Ljunggren (asserted not re-proved). |
| `cassels_bracket_test.captured.txt` | _(undescribed)_ |
| `cassels_descent_probe.captured.txt` | _(undescribed)_ |
| `cassels_elementary.captured.txt` | Captured output (EXIT 0) of code/cassels/elementary_structure.py: all 7 sections PASS in 1.17s — gcd lemma (1,199,994 cases, 0 failures), Fermat equivalence (same range), reduced-system sweep Phi_p(a^q+1) never a perfect q-th power (202,886 (p,q,a) cases, 0 hits; max Phi 1201 bits), mirror sweep Phi_q(-(c^p-1)) never a perfect p-th power (46,480 cases, 0 non-degenerate), calibration at (3,2,2,3), gmpy2.iroot cross-check (258 samples). Exact integers only. |
| `cassels_elementary.note.md` | Result note for code/cassels/elementary_structure.py: the reduced-system structural fact (gcd(x-1,Phi_p(x))=gcd(x-1,p) in {1,p} forces x-1=a^q, Phi_p(x)=b^q in the p∤y branch — so the sweep is exactly the numerical spine of Cassels p\ |
| `cassels_valuation.captured.txt` | Captured output of running code/cassels_valuation.py: full PASS/FAIL trace for the Cassels valuation computation — Section A LTE identities (234 cases, exact-proved), Section B cyclotomic v_P factorisation/ramification with norm cross-check (36 rows), Section C coprimality off the ramified prime (623 pairs), Section D oracle. All PASS; total wall time ~0.1s. |
| `cassels_valuation.note.md` | Result note for code/cassels_valuation.py: status ledger (A LTE identities exact-proved; B cyclotomic v_P factorisation and ramification transfer numerically verified; C coprimality off the ramified prime verified, 623 pairs; D oracle), the lifted claim block cassels-valuation-lte-and-cyclotomic, and explicit statement that Cassels' full q |
| `certify_lebesgue_caseB.captured.txt` | Earlier capture (prior run) of the same Case-B certification program, EXIT 0. Superseded by code/out/caseB.captured.txt (same content, current naming). Kept because a program carrying a result is not deleted. |
| `certify_lebesgue_caseB.note.md` | Earlier result note (prior run) for the same Code B certification; carries claim id caseb-lebesgue-reduction-certified. Superseded by code/out/caseB.note.md which uses the task-mandated claim id exp2-case-B-reduction (steering-corrected: reduction-proved + lemma verified-numeric/classical-asserted, NOT status:proved). |
| `check_conditions_all_small.captured.txt` | _(undescribed)_ |
| `check_step4_bound.captured.txt` | _(undescribed)_ |
| `commands.log` | _(undescribed)_ |
| `cond.captured.txt` | _(undescribed)_ |
| `cond_note.md` | Record of what the exact-integer condition evaluator computed and verified: check_conditions(2,3) values (excluded-by-hypothesis), 0 double-Wieferich pairs at B=200/500, oracle solutions(10**8) exactly (3,2,2,3). Carries the checked claim block cond-evaluator-odd-prime-wieferich. |
| `cond_verify.captured.txt` | _(undescribed)_ |
| `correct_evenness.captured.txt` | _(undescribed)_ |
| `crossprime.captured.txt` | _(undescribed)_ |
| `crossprime.err` | _(undescribed)_ |
| `crossprime_sweep.captured.txt` | _(undescribed)_ |
| `crossprime_sweep.note.md` | Result note + claim block for the executed crossprime h^- divisibility sweep: the condition q |
| `crossprime_sweep200.captured.txt` | Captured output of code/crossprime_sweep.py at bound 200: exact-integer cross-prime h^-(Q(zeta_p)) divisibility matrix. h^- matches OEIS A000927 for all 45 odd primes <= 200; exactly one surviving pair (47,139). Combined with double-Wieferich, jointly eliminates every odd-prime exponent pair < 200. Run: 147.8s. |
| `crossprime_test.py` | _(undescribed)_ |
| `descent-subclaim-attacks.note.md` | Record of this run's executed attacks: the exponent-2 descent sub-claim r^q - 2^{mq-2} s^q = ±1 has no solution other than (3,1,1,1) over q≤29,m≤7,r,s≤300, and the full x^2-y^3=1 descent is reproduced (unique (3,2)). Verified-numerically, exact integer math; anchor and claim block. |
| `dw_pairs_1e4.captured.txt` | _(undescribed)_ |
| `elementary_rungs.captured.txt` | Captured output of code/elementary/elementary_rungs.py: R-trivial-bases proved (x=1 => y=0 excluded; y=1 => x^p=2 impossible), oracle solutions(1e8)=[(3,2,2,3)] all bases>=2; R-p-eq-q proved (factorisation) with 0 brute hits over primes<=19, x<3000; R-fixed-23 verified numerically to x=10^7 -> only (3,2) with y>0. EXIT 0. |
| `elementary_rungs.note.md` | Result note + claim blocks (r-trivial-bases, r-p-eq-q, r-fixed-23-verified-numerically) for the three elementary rungs; states hypotheses, holds-here (known solution not eliminated), status (proved / proved / verified-numerically), bearing, anchor. |
| `equivalence.captured.txt` | _(undescribed)_ |
| `equivalence_bounded.captured.txt` | _(undescribed)_ |
| `equivalence_bounded.note.md` | Result note + claim block (exp2-descent-lebesgue-equivalence-bounded, status checked) for the bounded bijection verification between the descent sub-claim r^q-2^{mq-2}s^q=+-1 and x^2-y^q=1. Records that verify_equivalence.py was non-terminating (Xb=2*S**q infinite x-loop -> 0-byte captures), the branch-corrected maps, and that the known solution sits in the -1 branch. Anchors equivalence_bounded/verify_direction_split/verify_subclaim_fresh captures. |
| `equivalence_fresh.captured.txt` | _(undescribed)_ |
| `equivalence_rerun.captured.txt` | _(undescribed)_ |
| `equivalence_run.txt` | _(undescribed)_ |
| `exp2.captured.txt` | Captured output of code/exp2_verify.py: the exponent-2 independent searches at N=1e6 and 1e7, with per-task verdicts and cross-checks against the oracle. |
| `exp2.md` | Note and claim block for the exponent-2 independent searches: task 1 agrees (unique (3,2,3)), task 2 agrees (none), task 3 reduction vacuous (only solution has prime exponents) — each at N=1e6 and 1e7, confirmed by two independent routes. |
| `exp2_crosscheck.captured.txt` | Captured output of running code/exp2_crosscheck.py (independent exact-integer route): Task 1 x^p - y^2 = 1, p odd, y<=1e7 -> no solution; Task 2 x^2 - y^q = 1, x<=1e8 -> exactly (3,2,3). AGREE with the exp2_verify.py route. ~200s. |
| `exp2_crosscheck.note.md` | Note + fenced claim (id exp2-independent-crosscheck) recording the independent exact-integer cross-check of the two exponent-2 cases via gmpy2.iroot + residue filter. Verdicts: task 1 x^p-y^2=1 (p odd) none for y<=1e7; task 2 x^2-y^q=1 (q odd) exactly (3,2,3) for x<=1e8. Captured output in exp2_crosscheck.captured.txt. |
| `exp2_descent_eprover.captured.txt` | _(undescribed)_ |
| `exp2_even_proof.captured.txt` | Captured output (EXIT 0) of code/exp2_even_proof.py: 3-part machine verification of lemma exp2-a-even (x^2-y^q=1, x even, q odd prime, no solution). Part (a) minimiser b^q-a^q at (1,2)=2^q-1, monotone, 2^q-1>=7>2, all OK for q in {3..31}; Part (b) gcd(x-1,x+1)=1 for even x<=2e6; Part (c) brute oracle even x<=1e7, q<=30 -> ZERO solutions, runtime 53.7s. Known solution (3,2,3) x odd excluded. Exact integer arithmetic. |
| `exp2_even_proof.note.md` | Result note + claim block (id exp2-a-even, status proved) for the even-x case of x^2-y^q=1: 3-step elementary proof (gcd, coprime-factor q-th-power split, b^q-a^q>=7>2 inequality), machine-verified parts listed, falsifier discipline (known solution x=3 odd excluded, not eliminated), cross-checks. |
| `exp2_explore.captured.txt` | _(undescribed)_ |
| `extend_square_check.captured.txt` | _(undescribed)_ |
| `geom_check.py` | _(undescribed)_ |
| `hminus_check.captured.txt` | _(undescribed)_ |
| `hminus_check.py` | Validates h^-(Q(zeta_p)) = 2p * prod_{odd chi} (-1/2 B_{1,chi}) for p in {3,5,7,11,13,23,31,37} via mpmath high-precision character-value evaluation, rounding to the known integer class numbers (1,1,1,1,1,3,9,37). Produced ALL MATCH: True. Resolves prior sympy-Float/.real AttributeError and the hanging symbolic-simplification route. |
| `hminus_check_fixed.captured.txt` | _(undescribed)_ |
| `hminus_consecutive_verify.md` | _(undescribed)_ |
| `hminus_exact.captured.txt` | Captured output of hminus_exact.py: high-precision mpmath verification of h^-(Q(zeta_p)) matching known values for p=3..43, ALL MATCH after primitive_root bug fix. |
| `hminus_exact.py` | High-precision mpmath verification of the relative class number formula h^-(Q(zeta_p)) = 2p*prod(-1/2 B_{1,chi}) against known values p=3..43. Written but NOT yet run (scholar has no execution tool); delegates to the computing role to close claim minus-class-number-formula. |
| `hminus_full.captured.txt` | _(undescribed)_ |
| `hminus_full100.captured.txt` | _(undescribed)_ |
| `hminus_full97.captured.txt` | _(undescribed)_ |
| `hminus_full_oracle.captured.txt` | _(undescribed)_ |
| `hminus_lib_check.captured.txt` | _(undescribed)_ |
| `hminus_pari.captured.txt` | Captured output of the PARI/GP bnfinit-ratio cross-check of h^-(Q(zeta_p)): 13 rows, h(K), h(K^+), h^-, all 13 matching the expected values (1^7,3,8,9,37,121,211); h(K^+)=1 throughout. |
| `hminus_pari.note.md` | Write-up of the independent PARI/GP bnfinit-ratio cross-check of h^-: normalisation, 13/13 matched table, commands, and status as a numeric cross-check not a proof. |
| `hminus_two_route_claim.md` | _(undescribed)_ |
| `hminus_verify_note.md` | Record that claim minus-class-number-formula was closed: h^-(Q(zeta_p)) verified on p=3..43 by two independent routes (exact sympy rational + mpmath), plus the primitive_root bug found/fixed at p=43. |
| `inventor_approach_checks.captured.txt` | Capture of code/out/inventor_approach_checks.py: Lucas identities U_p(x+1,x)=(x^p-1)/(x-1) and U_q(y-1,-y)=(y^q+1)/(y+1) hold for p,q in {3,5,7} (sympy). The reported "poly gcd(x-1,Phi_p)=x-1" is a BUG from un-reduced sp.expand((x^p-1)/(x-1)); corrected exact check gives poly gcd over QQ = 1 and Phi_p(1)=p. |
| `inventor_approach_checks.py` | _(undescribed)_ |
| `lambda_valuation.captured.txt` | Captured output of running code/cassels/lambda_valuation.py: OVERALL PASS. Check 1 (v_lambda(x-zeta_p)=1 iff p\ |
| `lambda_valuation.note.md` | Result note + claim block `lambda-valuation-x-zeta-iff-p-divides-x-minus-1` for the (1-zeta_p)-adic valuation verification; the program was 0-byte-captured before this run, now executed and PASS. |
| `lean_reduction.captured.txt` | _(undescribed)_ |
| `lebesgueA_v2.captured.txt` | _(undescribed)_ |
| `lebesgueA_v2.note.md` | _(undescribed)_ |
| `lebesgueB_z[i].captured.txt` | _(undescribed)_ |
| `lebesgueB_z[i].note.md` | _(undescribed)_ |
| `local_solvability_check.py` | _(undescribed)_ |
| `maillet_verify.py` | Exact-integer check that the Maillet determinant det(M_q) = ±q^((q-3)/2)·h_1(q) reproduces the catalogued relative class numbers h^-(Q(zeta_q)) for q=3..43 (OEIS A000927). Independent second route for the minus-class-number formula. NOT YET RUN. |
| `oeis_digest_check.py` | _(undescribed)_ |
| `oracle_1e10.captured.txt` | _(undescribed)_ |
| `oracle_state.txt` | _(undescribed)_ |
| `pattern_bernoulli_check.captured.txt` | _(undescribed)_ |
| `pattern_crossprime_corr.captured.txt` | _(undescribed)_ |
| `pattern_crossprime_corr.note.md` | _(undescribed)_ |
| `pattern_dw_char.captured.txt` | _(undescribed)_ |
| `pattern_dw_extend.captured.txt` | _(undescribed)_ |
| `pattern_dw_structure.captured.txt` | _(undescribed)_ |
| `pattern_finder_note.md` | _(undescribed)_ |
| `pattern_findings.note.md` | Pattern-recognition findings on the computed sequences: Kummer criterion verified exactly (p |
| `pattern_irregular83.captured.txt` | _(undescribed)_ |
| `pattern_irregular_conflict.captured.txt` | _(undescribed)_ |
| `pattern_irregular_correction.note.md` | Records the verified correction that the double-Wieferich primes 2903 and 911 are REGULAR (not irregular): exact arithmetic num(B_2386)%2903=1170 and num(B_60)%911=859 refute the earlier buggy modular-recurrence labels. Carries claim dw-pairs-all-regular-corrected. The 2903/911 irregularity was falsely asserted by pattern_dw_structure.py's OLD_bernoulli_even_modp recurrence and by the earlier copy of the dw-pairs-regular-minor-torsion-free claim. |
| `pattern_irregular_cross.captured.txt` | _(undescribed)_ |
| `pattern_irregular_decide.captured.txt` | _(undescribed)_ |
| `pattern_irregular_decide_v2.captured.txt` | _(undescribed)_ |
| `pattern_irregular_dw.captured.txt` | _(undescribed)_ |
| `pattern_irregular_dw2.captured.txt` | _(undescribed)_ |
| `pattern_irregular_locbug.captured.txt` | _(undescribed)_ |
| `pattern_irregular_pari.captured.txt` | _(undescribed)_ |
| `pattern_irregular_via3.captured.txt` | _(undescribed)_ |
| `pattern_irregularity.captured.txt` | _(undescribed)_ |
| `pattern_phi_residue.captured.txt` | _(undescribed)_ |
| `pattern_sequences.captured.txt` | _(undescribed)_ |
| `pillai_probe.py` | _(undescribed)_ |
| `pillai_tier_check.md` | Hand-verified arithmetic for the Pillai/Bennett related-equations tier: the three Pillai two-solution (3,2) equations, the five Bennett (N,c) exception equations, and the falsifier boundary showing c=1 (the run's known solution) is the multi-representation small-c case these at-most-one theorems exclude. Establishes holds-here=no for the Pillai tier. |
| `pillai_tier_check.py` | _(undescribed)_ |
| `primitive_div.captured.txt` | Captured output of code/primitive_div/verify_primitive_div.py: all 5 sections PASS (Lucas identities p,q in {3..13}; gcd lemma 2994 pairs 0 fail; primitive divisor for every odd prime p in {3..23}, no (p,x) failure; p=2 exception confirmed; condition-check scope). |
| `primitive_div.md` | Result note + claim block `prim-div-lucas-verified` for the primitive-divisor machinery verification: Lucas identities, gcd lemma, Zsigmondy primitive divisors per p, the p=2 exception, and the Cassels/Wieferich scope. |
| `primitive_div_crosscheck.captured.txt` | Captured output of code/primitive_div/crosscheck_order.py: direct multiplicative-order cross-check, 102 (p,x) all order(x mod r)=p PASS; mirror primitive divisor small exceptions listed. |
| `primitive_div_mirror.captured.txt` | _(undescribed)_ |
| `primitive_div_mirror.md` | _(undescribed)_ |
| `probe_T_exact_mod8.captured.txt` | _(undescribed)_ |
| `probe_T_mod8.captured.txt` | _(undescribed)_ |
| `probe_evenc_abs1.captured.txt` | _(undescribed)_ |
| `probe_evenness_correct.captured.txt` | _(undescribed)_ |
| `probe_step4_lemmas.captured.txt` | _(undescribed)_ |
| `prove_T_c_odd_nonsquare.captured.txt` | _(undescribed)_ |
| `prove_T_c_odd_nonsquare.note.md` | Result note for prove_T_c_odd_nonsquare.py: proves the c-odd mod-8 rung (status proved) but records it is VACUOUS for Case B because the certified reduction forces c even; documents the dead-end probe that no modulus <2000 rules out squares for even c. Carries claim caseb-codd-mod8-proved-but-vacuous. |
| `prove_T_mod8_classification.captured.txt` | _(undescribed)_ |
| `prove_T_mod8_classification.note.md` | _(undescribed)_ |
| `prove_T_mod8_residual_crosscheck.captured.txt` | _(undescribed)_ |
| `prove_T_mod8_residual_crosscheck.txt` | _(undescribed)_ |
| `prove_T_mod_lemmas.captured.txt` | _(undescribed)_ |
| `prove_mod_obstruction.captured.txt` | _(undescribed)_ |
| `r35_derive.captured.txt` | _(undescribed)_ |
| `r35_search.captured.txt` | _(undescribed)_ |
| `r35_verify_caseII.captured.txt` | _(undescribed)_ |
| `r35_verify_eisen5.captured.txt` | _(undescribed)_ |
| `r35_verify_structure.captured.txt` | _(undescribed)_ |
| `ramification_check.note.md` | Result note + claim block ramification-check-exact: three independent exact-arithmetic routes now verify the consequences of the load-bearing claim zeta-p-ring-of-integers-and-ramification (previously asserted): N(1-zeta_p)=p, (1-zeta)^(p-1)=p*u with u an integral unit (ideal equality (p)=P^(p-1)), Phi_p ≡ (X-1)^(p-1) mod p. Upgrades that claim's evidence tier to checked on the stated ranges (all odd primes <= 97 for integrality, <= 23 for unit norm). |
| `ramification_verified.note.md` | Note with fenced claim id ramify-p-eq-prime-checked: (1-zeta_p)^{p-1}=p*u unit, (p)=P^{p-1}, N(1-zeta)=p, verified for all odd primes p<=97 by two independent exact routes (verify_ram_fast.py and verify_ramification.py). Captured output at code/out/verify_ram_fast.captured.txt and code/out/verify_ramification.captured.txt. |
| `residual_modulus_hunt.captured.txt` | _(undescribed)_ |
| `residual_modulus_hunt.note.md` | _(undescribed)_ |
| `rfixed23.captured.txt` | _(undescribed)_ |
| `rfixed23_proof.captured.txt` | Captured output of code/rfixed23_proof.py: exact-integer reproduction of the x^2-y^3=1 descent — brute unique (3,2) to x=1e4, sympy parity facts, {c^3,2d^3} distribution, Thue c^3-2d^3=±1 swept to d=1e6 unique (1,1,-1), direct + oracle cross-checks. All PASS. |
| `rfixed23_proof.rerun.txt` | _(undescribed)_ |
| `roitman_confirm.py` | _(undescribed)_ |
| `run_maillet.sh` | _(undescribed)_ |
| `run_ram_fast.sh` | _(undescribed)_ |
| `run_ramification.sh` | _(undescribed)_ |
| `run_roitman.sh` | Records (as a note, not a runner) that the Roitman primitive-divisor claim is already corroborated by checked computation; the proposed re-check was withdrawn as redundant. Read this instead of re-running the Roitman mechanism. |
| `run_verify.sh` | _(undescribed)_ |
| `runge_check.py` | _(undescribed)_ |
| `scholar_hminus_crosscheck.py` | sympy-exact third route to the relative class number h^-(Q(zeta_p)) = 2p ∏ (-1/2 B_{1,chi}), cross-checking the already-verified values (1,1,1,1,1,3,9,37,211) against OEIS A000927 by prime index. |
| `scholar_ramification_check.captured.txt` | _(undescribed)_ |
| `scholar_ramification_check.note.md` | Records that the load-bearing ramification claim (Z[zeta_p]=O_K, (p)=(1-zeta_p)^(p-1)) is still asserted and proposes an exact 3-consequence check that was written but not run (no execution tool in this session). |
| `scholar_verify_loadbearing.py` | _(undescribed)_ |
| `step4_evenness_refuted.note.md` | _(undescribed)_ |
| `stick_index.captured.txt` | _(undescribed)_ |
| `stick_index_py.captured.txt` | _(undescribed)_ |
| `subclaim_run.txt` | _(undescribed)_ |
| `thue_attack.captured.txt` | _(undescribed)_ |
| `thue_completeness.captured.txt` | _(undescribed)_ |
| `thue_descend_fixed23.note.md` | _(undescribed)_ |
| `thue_descent_check.captured.txt` | Captured output of code/refute/thue_descent_check.py: the descent sub-claim r^q - 2^{mq-2} s^q = ±1 has no solution other than (q=3,m=1,r=s=1) over odd primes q≤13, m≤6, r,s≤200. Exact integer arithmetic; 0 counterexamples. |
| `thue_descent_full.captured.txt` | _(undescribed)_ |
| `thue_gp.captured.txt` | _(undescribed)_ |
| `thue_nf.captured.txt` | _(undescribed)_ |
| `thue_pair.captured.txt` | _(undescribed)_ |
| `thue_run2.captured.txt` | Captured output of code/refute/thue_run2.py: wider sweep of the same descent sub-claim over q≤29, m≤7, r,s≤300 — 0 solutions other than the known (q=3,m=1,r=s=1). Exact integer arithmetic. |
| `thue_sage.captured.txt` | _(undescribed)_ |
| `thue_unit_descent.captured.txt` | _(undescribed)_ |
| `thue_unit_descent.note.md` | _(undescribed)_ |
| `time_sample.captured.txt` | _(undescribed)_ |
| `time_sample2.captured.txt` | _(undescribed)_ |
| `verify_bundle.captured.txt` | Captured output of code/verify_bundle.py (EXIT 0, 431.7s): four-section exact-integer bundle. S1 oracle solutions(1e10)=solutions(1e12)=[(3,2,2,3)]; S2 descent subclaim q<=101,m<=10,r,s<=2000 only (3,1,1,1); S3 T(c,p) no square for c<=1e5,p<=251 (5.3e6 pairs, 0 squares); S4 cross-prime h^- survivor below 200 exactly (47,139), fails both double-Wieferich. |
| `verify_bundle.note.md` | Companion note to verify_bundle.captured.txt: the four sections stated with the extended ranges reached, each prior range named, the known-solution falsifier placement, and the claim block verify-bundle-2024-ext. |
| `verify_claims.captured.txt` | Captured output of verify_claims.py: LTE/valuation identity PASS (8646 cases), minus-class-number h^-(Q(zeta_p)) matches known values for p=3..43 via exact rational sympy, 1-z^a polynomial identity PASS. |
| `verify_claims.py` | Scholar verification program for the cheapest machine-tier claims: exact-integer LTE/valuation identity checks (v_p(x^p±1)=1+v_p(x±1) under the corrected p |
| `verify_direction_split.captured.txt` | _(undescribed)_ |
| `verify_foundations.captured.txt` | _(undescribed)_ |
| `verify_foundations.notes.md` | _(undescribed)_ |
| `verify_ram_fast.captured.txt` | _(undescribed)_ |
| `verify_ram_fast.py` | Exact integer/sympy verification that (1-zeta_p)^{p-1} = p*u with u in Z[zeta_p], i.e. (p)=(1-zeta_p)^{p-1}, for odd primes p<=97. Reduces (1-x)^{p-1} mod Phi_p by integer polynomial division, checks every remainder coefficient divisible by p (so u integral, N(u)=1 by norm multiplicativity), and checks Phi_p(1)=p. ALL PASS for all 24 odd primes <=97. Finite numeric check, not a proof. Established: matches lib.cyclo resultant route (verify_ramification.py) on overlap. |
| `verify_ramification.captured.txt` | _(undescribed)_ |
| `verify_ramification.note.md` | _(undescribed)_ |
| `verify_ramification.py` | Independent exact verification of ramification in Q(zeta_p) using lib.cyclo resultant field norms: N(1-zeta)=p, (1-zeta)^{p-1}=p*u with N(u)=+-1 and u integral, p/(1-z) integral. PASS for p in {3,5,7,11,13,17,19,23,29,31,37}. Confirms (p)=(1-zeta_p)^{p-1} via a different route than verify_ram_fast.py. Finite numeric check, not a proof. |
| `verify_subclaim.captured.txt` | _(undescribed)_ |
| `verify_subclaim.note.md` | _(undescribed)_ |
| `verify_subclaim_fresh.captured.txt` | _(undescribed)_ |
