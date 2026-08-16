# Index — code/out

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `README.md` | _(undescribed)_ |
| `badprimes_criterion_n4_n20.md` | Computation record for the bad-prime work: n=4 minor-criterion verification (lcm J_T = 1575 -> {3,5,7}, two routes) and degree-20 certified-bad frontier (18 certified primes, 20 smallest non-certified candidates, candidates < 100), plus the sympy sequential-subs bug fix and SNF-minor identity notes. Canonical claim blocks are in research/notes/badprimes-criterion-n4-n20.md. |
| `badprimes_n20_frontier.captured.txt` | Capture of certified_bad_frontier_n20.py: 18 certified-bad primes for degree 20 (p |
| `badprimes_n4.captured.txt` | Capture of verify_badprimes_n4.py: all 64 tuples T, lcm J_T = 1575 = 3^2·5^2·7, prime divisors exactly {3,5,7} (two routes), sufficient binomial criterion {3,5} subset. ALL CHECKS PASSED, exit 0. |
| `badprimes_n5.captured.txt` | Capture of code/badprimes_criterion/verify_badprimes_n5.py (rank-over-F_p route, degree 5): all 625 tuples T in {1..5}^4 × 170 primes (all <1000 plus 3541, 8009) = 106,250 exact rank computations over 28 workers. Independently re-run on 2026-08-16: 384.1 s internal wall (384.4 s external), rank drops (<120) occur exactly at the published bad primes {2,3,7,11,131,193,599,3541,8009} with identical witness counts/min ranks/first witnesses as the original 386.9 s run; all 161 primes <1000 outside the list full-rank on every tuple; spot check p=3547 full rank. ALL CHECKS PASSED, exit 0. |
| `badprimes_n5_semantic.captured.txt` | Capture of code/badprimes_criterion/semantic_n5_smallprimes.py (independent semantic route, degree 5): exhaustive enumeration of all p^5 monic degree-5 polynomials over F_p for p in {2,3,5,7,11,13} (552,551 polys, 28 workers, 85.4 s) through the canonical oracle lib.casas_alvero.is_ca_hasse / is_pure_power. Counterexamples exist iff p in {2,3,7,11} (counts 2,12,0,42,110,0), matching the published list and the rank route; p=2 witness x^5+x printed. ALL CHECKS PASSED, exit 0. |
| `badprimes_sn.captured.txt` | Capture of the S_n-scheme bad-prime verification over GF(p): ALL CHECKS PASSED, exit 0. Hasse formulation: n=3 bad {2}, n=4 bad {3,5,7} over all 17 primes p<60, matching Castryck et al. 2012 Thm 4 / De Jong–Draisma; bounded F_p enumeration via is_ca_hasse agrees (counts n=3 {2:2,3:0,5:0,7:0}, n=4 {2:0,3:6,5:20,7:42}). Documents the ordinary-vs-Hasse divergence (ordinary scheme marks p=2 bad for n=4 via vacuous zero derivatives). |
| `binomial_calibration.captured.txt` | Capture of code/n5/binomial_calibration.py (exit 0, ALL CHECKS PASSED): binomial-criterion calibration vs true bad-prime lists at n=3,4,5. n=3: certified {2} of {2} (1.000). n=4: certified {3,5} of {3,5,7}, gap {7} (2/3). n=5: certified {2,3} of {2,3,7,11,131,193,599,3541,8009}, gap 7 primes (2/9 = 0.222). Negative controls: 10 good primes per degree all divide no C(n,i)-1. Byte-identical to program stdout (diff-checked). |
| `brute_worked_examples.md` | _(undescribed)_ |
| `brute_worked_examples.txt` | _(undescribed)_ |
| `capture_satisfier.md` | Captures the fresh enumeration of Hasse-CA satisfier counts over F_p and the derived multiplier m=sat/p sequences (p=2 n=3..16, p=3 n=3..9), the m=p law and its breaks, from scripts that had been written but never run. |
| `commands.log` | _(undescribed)_ |
| `count_n4_hasse.py` | _(undescribed)_ |
| `crosscheck_p2_n17n18.py` | Proposed independent sympy-oracle cross-check of the n=17,18 p=2 multipliers; TIMED OUT (sympy product-enumeration route too slow at 2^17/2^18). Kept as a record that the sympy route is infeasible here and the values rest on the bit-parallel checker + rule-11 match over all n=3..16. |
| `crosscheck_p2_prior.py` | Cross-check of the bit-parallel F2 Hasse-CA checker (extend_p2_multiplier.py) against the run's 14 already-recorded p=2 multipliers for n=3..16. Result: ALL MATCH, including the 457 spike at n=15 and m=1 at 4,8,16. This is the oracle/rule-11 verification that makes the n=17..20 extension trustworthy. |
| `elimination_n3.captured.txt` | _(undescribed)_ |
| `extend_p2_multiplier.py` | Exact bit-parallel F2 Hasse-CA satisfier/counterexample counter: extends the p=2 multiplier m(n,2)=sat/2 from the run's n<=16 to n=20. Verified against lib.casas_alvero on all 2^n polys for n=3,4,5 and reproduces every recorded multiplier n=3..16 (incl. 457 spike at n=15, m=1 at 4,8,16). Output: m(n,2)=1 iff n a power of 2 across n=2..20, and n=17..20 multipliers 2,2,8,2 (new). Also files: crosscheck_p2_prior.py (oracle check n=3..16), crosscheck_p2_n17n18.py (sympy route, timed out). |
| `feasibility_boundary.captured.txt` | Capture of code/n5/feasibility_boundary.py: Casas-Alvero minor-criterion feasibility boundary for n=3..8 — exact parameters d, C, D, tuples and route feasibility (SNF n<=4, rank-only n=5, neither n>=6). All parameter values independently recomputed by direct formulas, matching. Exit 0. |
| `ghosh_break.captured.txt` | Capture of the char-p break verification (code/ghosh_charp/verify_break.py): 1313 checks, all PASS — f(n,j,n)=1/-n divisibility, unit death at p |
| `multiplier_seq_p23.py` | _(undescribed)_ |
| `multiplier_table.py` | _(undescribed)_ |
| `open_degree_coverage.captured.txt` | _(undescribed)_ |
| `oracle_guard.captured.txt` | Capture of the canonical oracle guard suite (code/lib/casas_alvero.py main()): guards 1-4 (32 pure powers (x-a)^n over QQ n=1..8; 24 random monics deg 2..7 must fail; 4 char-p witnesses x^{p+1}-x^p must be counterexamples; x^n over GF(p) pure power) plus NEW guard 5 — char-0 agreement is_ca==is_ca_hasse on 64+8 polynomials over QQ. 72 checks, ALL GUARDS PASSED, exit 0. Non-vacuity of guard 5 confirmed separately: over GF(2), x^4+x^2 has is_ca=True but is_ca_hasse=False (the ordinary/Hasse divergence that guard 5 exists to exclude in char 0). |
| `oracle_guard.rerun.txt` | _(undescribed)_ |
| `ordinary-vs-hasse-charp-witness.captured.txt` | Capture of code/hasse_charp/recheck_xpp1_xp_hasse.py: Hasse recheck of the "f(X^p) without constant term also works since all derivatives vanish" clause of claim charp-witness-xpp1-xp. Guards (x-1)^3 CA, x^3-x not CA over QQ, x^{p+1}-x^p Hasse-CA p=2,3,5 pass. (A) x^{p+1}-x^p: is_ca and is_ca_hasse True, pure power False for p=2,3,5,7. (B1) x^{mp} m=1..3: all Hasse derivatives vanish only for (2,1),(2,2),(3,1),(3,3),(5,1),(7,1); H_2(x^6)=x^4 over F_2. (B2) x^p+x^{2p}: is_ca True vacuously, is_ca_hasse False, first failing index p. (B2b) Hasse-CA iff c_1 ≡ 0 mod p. |
| `ordinary-vs-hasse-charp-witness.md` | Verdict note for the Hasse recheck, with claim block id charp-witness-xpp1-xp-hasse-recheck (status checked): the "all derivatives vanish" clause is ordinary-only; monomials x^{mp} are Hasse-CA only via the shared factor x (pure powers anyway); x^p+x^{2p} fails Hasse-CA at i=p. Two independent exact routes agree (56/56). |
| `parameter` | _(undescribed)_ |
| `probe_extend.py` | _(undescribed)_ |
| `probe_n4_structure.py` | _(undescribed)_ |
| `probe_n5p3.py` | _(undescribed)_ |
| `refute_char2.md` | Records the engine-refuted char-2 counterexample x^3+x^2 (negative control proving the TPTP encoding of the CA hypothesis is faithful) and what it does/doesn't establish. |
| `refute_deg4_char3.md` | Refutation note: degree-4 char-3 counterexample x^4+x, confirming p=3 is a bad prime for n=4 and locating the char-p break of the run's two-roots centroid argument (f''' vanishes mod 3). |
| `refute_deg4_char5.md` | Refutation note: degree-4 char-5 counterexample x^4-x^2 (Hasse formulation, 3 distinct roots, not a pure power), recording that p=5 is a bad prime for n=4 and corroborating the run's J_T criterion (5 |
| `refute_deg4_char7.captured.txt` | _(undescribed)_ |
| `refute_deg4_char7.md` | Claim note for the degree-4 char-7 refutation: the counterexample f=x^4+x^3+4x over F_7, hand-checked tables, and the claim block deg4-char7-refuted. |
| `refute_deg5_char2.md` | Refutation note with checked claim block: CA degree 5 over F_2 false via f=x^5+x^4=x^4(x+1); first n=5 refutation in the refute set, independent semantic corroboration that p=2 is bad for n=5. |
| `refute_deg6_char2.md` | Refutation note: CA in degree 6 over F_2 is false (Hasse), witness x^6+x^2; fresh-(n,p) char-p negative control corroborating the root-difference approach's break; engine- and hand-verified. |
| `refute_deg6_char5.md` | _(undescribed)_ |
| `satisfier_table.py` | _(undescribed)_ |
| `test_n5_law.py` | _(undescribed)_ |
| `test_n5_law_small.py` | _(undescribed)_ |
| `verify_charp_agreement.py` | _(undescribed)_ |
