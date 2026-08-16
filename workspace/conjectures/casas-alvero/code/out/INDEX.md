# Index — code/out

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `README.md` | Folder README for code/out: states that this folder holds what a program computed (captures), while code/ holds what a person wrote; captures should be written beside a markdown note with a fenced claim block status:checked when the output settles something. |
| `analyze_p2_shapes.py` | Test the set-bit hypothesis for F2 Hasse-CA counterexamples: for popcount-2 n (n=2^b+2^c), the counterexamples are conjectured exactly x^a(x+1)^(n-a) with a in the set-bit powers {2^b,2^c}; generalize and test whether all counterexamples have that form. |
| `analyze_p2_shapes_small.py` | Shape analysis of F2 Hasse-CA counterexamples for small n where single-threaded enumeration is fast (n<=14 popcount classes, n=15 allowed); counts two-term counterexamples per n and the a-values to test the set-bit prediction. |
| `badprimes_criterion_n4_n20.md` | Note on the bad-prime-minors criterion verified at n=4 and the n=20 certified-bad frontier from the sufficient binomial criterion. |
| `badprimes_n20_frontier.captured.txt` | Degree-20 certified-bad frontier by the sufficient binomial criterion p |
| `badprimes_n4.captured.txt` | Exact computation of the bad-prime-minors criterion at n=4: J_T = gcd of all 15×15 minors (SNF), lcm over all 64 tuples {1..4}^3 = 1575 = 3²·5²·7, prime divisors exactly the known degree-4 bad primes {3,5,7}. ALL CHECKS PASSED. |
| `badprimes_n5.captured.txt` | n=5 bad-prime verification by rank-over-F_p (rank_{F_p}(M_T)<120): 625 tuples × 170 primes = 106,250 ranks; rank drops occur exactly at the published degree-5 bad-prime list {2,3,7,11,131,193,599,3541,8009}. ALL CHECKS PASSED. |
| `badprimes_n5_semantic.captured.txt` | Literal-definition semantic check: p bad for degree 5 iff a counterexample exists over F_p; on primes {2,3,5,7,11,13} holds exactly at {2,3,7,11}, agreeing with the published list. |
| `badprimes_sn.captured.txt` | S_n-scheme radical-equality route under the HASSE formulation reproduces published bad-prime lists exactly: n=3 → {2}, n=4 → {3,5,7}, over all 17 primes p<60, plus bounded F_p enumeration via lib.casas_alvero.is_ca_hasse. ALL CHECKS PASSED. |
| `binomial_calibration.captured.txt` | Calibration of the sufficient binomial bad-prime criterion against true lists: n=3 certifies {2} (ratio 1.0); n=4 {3,5} of {3,5,7}; n=5 {2,3} of the 9 true bad primes (22%); negative control: never falsely condemns a good prime (30 checks). ALL CHECKS PASSED. |
| `brute_worked_examples.md` | Records the naive brute-force oracle (code/brute.py) reproducing the worked examples and char-p set; output of the rule-9 cross-check. |
| `brute_worked_examples.txt` | Raw output of the naive brute-force worked-example checks against the canonical oracle. |
| `capture_satisfier.md` | Note capturing the Hasse-CA satisfier/counterexample count data used to test the satisfier law. |
| `charp_break.captured.txt` | Capture of code/rootdiff/verify_charp_break.py: exact GF(p) verification of the char-p break table for x^{p+1}-x^p (H_1=x^p, H_i=0 for 2..p-1, H_p=x-1; 2-root coloring {0,1} survives, neither root alone suffices), for p=2,3,5,7,11,13. Header names program, oracle (lib.casas_alvero.is_ca_hasse/is_pure_power), range. ALL CHECKS PASSED (42 passed, 0 failed), exit 0. |
| `check_popcount_hypothesis.py` | Verify the popcount hypothesis over the run's recorded p=2 multiplier data, then identify which fresh n (beyond 20) would test it: m(n,2)=sat(n,2)/2 depends only on popcount(n) (popcount 1→1, 2→2, 3→8, 4→457, 5→?). |
| `commands.log` | The runtime's own event log — verbatim replay of prior tool calls; not a normal file. Operators read it outside the run; the tools refuse it. |
| `confirm_twoterm_lib.py` | Independent confirmation of the two-term subset-sum law for F2 Hasse-CA using lib.casas_alvero.is_ca_hasse/is_pure_power (a different implementation from the bit-parallel is_ca_f2): x^a+x^n is an F2 Hasse-CA counterexample iff a is a proper nonempty subset-sum of n's set bits. |
| `consolidate_popcount.py` | Consolidated p=2 multiplier m(n,2)=sat/2 data (recorded n=3..20 plus fresh locally-computed n=21..24); tests whether m depends only on popcount(n). |
| `consolidate_support_law.py` | Consolidates the F2 Hasse-CA support-structure law: support-2 = 2^pc-2 across 19 degrees, pc=3 full rigidity, pc=4 small-support rigidity with variable large supports. |
| `count_n4_hasse.py` | Count over F_p the monic degree-n Hasse-CA satisfiers and counterexamples for n=3 and n=4 (enumerating p^n, classified with lib.casas_alvero.is_ca_hasse/is_counterexample); supports badprimes_sn. |
| `crosscheck_p2_n17n18.py` | Independent cross-check of n=17, n=18 p=2 multiplier values using the canonical sympy oracle directly (the slow route) — a second, different route to the same value (rule-9/11). |
| `crosscheck_p2_prior.py` | Cross-check the bit-parallel F2 Hasse-CA checker against already-recorded p=2 multiplier data for n=3..16: [2,1,2,2,8,1,2,2,8,2,8,8,457,1]. |
| `descent_check.captured.txt` | Capture of code/scholar/descent_check.py verifying the Graf-von-Bothmer coefficient-descent char-p mechanism: d=p^k has full descent (d choose i)≡0 mod p for all 1<=i<=d-1 so X_d(Fbar_p) empty; pivot (d choose d-1)=d must vanish for descent to start; witness degree d=p+1 has pivot (p+1 choose p)=p+1 NOT ≡0 mod p so descent stalls and x^(p+1)-x^p survives. Degrees {3,6,4,5,12,20,24,28} over primes p<30: full descent only at prime powers (3,4,5); pivot vanishes at prime divisors; degree 20 pivot==0 at {2,5} but NOT a prime power so descent does not settle it (matches degree-20 open). ALL CHECKS PASSED, verified by independent Lucas/prime-divisor enumeration. |
| `elimination_n3.captured.txt` | Elimination/Gröbner verification of CA at degree n=3 (smallest nontrivial degree). |
| `extend_p2_further.py` | Extends the F2 Hasse-CA multiplier sequence m(n,2)=sat/2 to fresh n (25,26,27) testing the popcount conjecture; parallel exact bit-arithmetic oracle. |
| `extend_p2_multiplier.py` | Fast exact p=2 Hasse-CA satisfier count for monic degree-n polys over F2 via bit-parallel Lucas Hasse derivatives and bit-polynomial Euclid (no floats, no sympy). |
| `extend_p2_popcount.py` | Parallel exact F2 Hasse-CA satisfier count extending the multiplier sequence m(n,2)=sat/2 to test the popcount conjecture. |
| `fam_vs_mono.py` | _(undescribed)_ |
| `family_exhaustive.py` | _(undescribed)_ |
| `feasibility_boundary.captured.txt` | Maps the feasibility boundary of the bad-prime-minors criterion: SNF feasible at n=4 (19×15 matrices, 64 tuples, ms), SNF-infeasible at n=5 (single 195×120 SNF >90 s cap) but rank-only feasible; n=6 rank-infeasible (C=1365, D=2751, ~185 core-s/rank, full sweep ~2.2e5 core-hours); n=7,8 neither. ALL CHECKS PASSED. |
| `ghosh_break.captured.txt` | 1313 exact checks (over QQ and GF(p)) verifying the named char-p break in the Ghosh proof (the leading coefficient -n of F(n,n,n) used as a unit in eq 4.18, which must fail at char p |
| `list_p2_counterexamples.py` | List the actual Hasse-CA monic polynomials over F2 (pure powers and counterexamples) for small n to find the structural form behind m(n,2). |
| `multiplier_seq_p23.py` | Compute the multiplier m=sat/p as a sequence in n for fixed p=2 and p=3, over a range large enough for sequence tools (m=1 at good primes, m>1 at bad). |
| `multiplier_table.py` | For a fixed degree n, tabulate the multiplier m=sat/p over several bad primes to characterize when m==p (law) vs the exceptions (n=7 bad for many small primes). |
| `open_degree_coverage.captured.txt` | Corrected open-degree coverage comparison (scenario/verify_open_degrees.py, pred==published): the old pub!=cov falsely flagged 89 degrees; genuine mismatches under the corrected comparison are {96,98}. Negative controls 16/20/28 assert the corrected semantics. ALL CHECKS PASSED. |
| `oracle_guard.captured.txt` | Full guard suite of the canonical oracle (code/lib/casas_alvero.py): (x-a)^n n=1..8 over QQ, random deg-5 fails, char-p witnesses are counterexamples, x^n over GF(p) pure power, char-0 is_ca==is_ca_hasse agreement — ALL GUARDS PASSED. |
| `oracle_guard.rerun.txt` | Re-run of the guard suite against the surviving canonical oracle after the one-canonical-oracle consolidation; confirms code/lib/casas_alvero.py is the passing oracle, comprehensiveness and the char-p handling. |
| `ordinary-vs-hasse-charp-witness.captured.txt` | Capture of code/hasse_charp/recheck_xpp1_xp_hasse.py: Hasse recheck of the "f(X^p) without constant term also works since all derivatives vanish" clause of claim charp-witness-xpp1-xp. Guards pass; x^{p+1}-x^p is_ca and is_ca_hasse True, pure power False for p=2,3,5,7; monomials x^{mp} Hasse-CA only via shared factor x; x^p+x^{2p} fails Hasse-CA at i=p. |
| `ordinary-vs-hasse-charp-witness.md` | Verdict note for the Hasse recheck, with claim block charp-witness-xpp1-xp-hasse-recheck (checked): the "all derivatives vanish" clause is ordinary-only; monomials x^{mp} are Hasse-CA only via the shared factor x (pure powers anyway); x^p+x^{2p} fails Hasse-CA at i=p. Two independent exact routes agree (56/56). |
| `parallel_p2_counts.py` | Parallel F2 Hasse-CA counterexample count (popcount study), splitting the [0,2^n) space across 28 CPUs, each counting satisfiers and counterexamples then summing. Exact bit-arithmetic. |
| `parameter` | _(undescribed)_ |
| `pc2_all_twoterm.py` | _(undescribed)_ |
| `pc3_nonfamily.py` | _(undescribed)_ |
| `pc3_nonfamily_print.py` | _(undescribed)_ |
| `pc_regularity.py` | _(undescribed)_ |
| `probe_extend.py` | Test the refined satisfier law (T) ce=sat-p (the p pure powers always satisfy), (C) sat is a multiple of p; good prime → m=1, bad prime → m=p except n=5,p=3 gives m=5=n; probe n=7,8,9 for more exceptions. |
| `probe_n4_structure.py` | Verify the satisfier law at corner cases and probe the STRUCTURE of the extra satisfiers at a bad prime: sat(n,p)=p if p good (CA holds), =p² if p bad (conjectured). |
| `probe_n5p3.py` | Probe the full structure of Hasse-CA satisfiers at n=5,p=3 (bad), where the count 15 breaks the naive p² law; lists every satisfier and marks pure powers. |
| `refute_char2.md` | Records the engine-refuted char-2 counterexample x^3+x^2 (negative control proving the TPTP encoding of the CA hypothesis is faithful) and what it does/doesn't establish. |
| `refute_deg4_char3.md` | Refutation note: degree-4 char-3 counterexample x^4+x, confirming p=3 is a bad prime for n=4 and locating the char-p break of the run's two-roots centroid argument (f''' vanishes mod 3). |
| `refute_deg4_char5.md` | Refutation note: degree-4 char-5 counterexample x^4-x^2 (Hasse formulation, 3 distinct roots, not a pure power), recording that p=5 is a bad prime for n=4 and corroborating the run's J_T criterion. |
| `refute_deg4_char7.captured.txt` | Capture of the degree-4 char-7 refutation checks (f=x^4+x^3+4x over F_7). |
| `refute_deg4_char7.md` | Claim note for the degree-4 char-7 refutation: the counterexample f=x^4+x^3+4x over F_7, hand-checked tables, and the claim block deg4-char7-refuted. |
| `refute_deg5_char2.md` | Refutation note with checked claim block: CA degree 5 over F_2 false via f=x^5+x^4=x^4(x+1); first n=5 refutation in the refute set, independent semantic corroboration that p=2 is bad for n=5. |
| `refute_deg6_char2.md` | Refutation note: CA in degree 6 over F_2 is false (Hasse), witness x^6+x^2; fresh-(n,p) char-p negative control corroborating the root-difference approach's break; engine- and hand-verified. |
| `refute_deg6_char5.md` | Refutation note: CA in degree 6 over F_5 is false (Hasse), witness x^6-x^5=x^5(x-1). |
| `refute_deg7_char2.md` | Refutation note for CA in degree 7 over F_2: witness x^7+x^3, hand-verified Hasse derivatives and engine confirmation, alignment with the published degree-7 bad-prime list and binomial criterion; claim deg7-char2-refuted. |
| `rootdiff_identity.captured.txt` | _(undescribed)_ |
| `rootdiff_identity_corrected.captured.txt` | _(undescribed)_ |
| `rootdiff_identity_deleted.md` | Documents that code/out/rootdiff_identity.captured.txt was deleted (was a zero-byte failed redirection) and must not be re-created by re-running code/rootdiff/verify_rootdiff_identity.py: the identity is settled by proof (directive 10 option 2, research/notes/root-difference-identity-verified.md) and a re-run cannot terminate (n=5,i=2 symbolic resultant exceeds 550 s, measured). Points to the real live verification, code/out/charp_break.captured.txt. |
| `satisfier_table.py` | Gather the Hasse-CA counterexample count over F_p for degrees n=3..6 across small primes to characterize when the p(p-1) law holds. |
| `shapes_n15_n23.py` | Shape comparison of F2 Hasse-CA counterexamples at n=15 and n=23 (both popcount 4): m=457 vs 466; finds the counterexample shape accounting for the 9 extra at n=23 (by monomial-support size and two-term a-values). |
| `shapes_n28.py` | Verifies pc=3 support-size profile rigidity at n=28 (m=8, {2:6,4:5,6:3}), highest feasible pc=3 degree. |
| `shapes_pc2_pc3.py` | Support-size profiles of F2 Hasse-CA counterexamples at pc=2 and pc=3 degrees (n=5,6,7,9,10,11,13): pc=3 profile {2:6,4:5,6:3} rigid. |
| `shapes_pc3_extend.py` | Extends the pc=3 support-size profile rigidity check to n=19,21,22,25,26 (all {2:6,4:5,6:3}). |
| `shapes_pc4_compare.py` | _(undescribed)_ |
| `shapes_pc4_parallel.py` | Parallel support-size profile of F2 Hasse-CA counterexamples at pc=4 degrees n=15,23,27 (support-2=14, support-4=106 constant; large support varies). |
| `test_n5_law.py` | Test the satisfier law at degree n=5: sat=p if p good, =p² if bad; ce=0 good, =p(p-1) bad; bad primes {2,3,7,…}, good {5,13,…}; checks p=2,3,7 (bad) and 5,13 (good). |
| `test_n5_law_small.py` | Test the satisfier law at degree n=5 for small primes only (p in {2,3,5,7}, max 7^5=16807), keeping it fast. |
| `test_twoterm_subset_sum.py` | Test the two-term subset-sum law for F2 Hasse-CA counterexamples: for n with set-bits B, x^a+x^n is a counterexample iff a is a proper nonempty subset-sum of B's bits. |
| `two_term_family_lib.py` | _(undescribed)_ |
| `two_term_rule.py` | _(undescribed)_ |
| `verify_charp_agreement.py` | Independent verification of char-p oracle agreement between the canonical sympy oracle (code/lib/casas_alvero.py) and the naive Euclid/radical oracle (code/brute.py) on the char-p counterexample family and pure powers. |
| `verify_n23_popcount.py` | Independently verify the n=23 p=2 Hasse-CA multiplier (m=466) using sympy's canonical oracle on masked random subsets, confirming parallel_p2_counts.py. |
| `verify_twomonomial_pc4.py` | Verifies the two-monomial submask law (x^a+x^n is F2 Hasse-CA ce iff a proper submask of n) at pc=4 degrees n=15,23,27: 14 submasks == 14 actual ce each, confirming the support-2 = 2^pc-2 rigidity. |
