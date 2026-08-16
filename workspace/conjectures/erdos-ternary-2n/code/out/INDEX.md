# Index — code/out

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `README.md` | _(undescribed)_ |
| `class_injectivity.captured.txt` | _(undescribed)_ |
| `class_injectivity.py` | _(undescribed)_ |
| `class_set_search.captured.txt` | _(undescribed)_ |
| `class_set_search.py` | _(undescribed)_ |
| `class_sets.captured.txt` | _(undescribed)_ |
| `class_sets.py` | _(undescribed)_ |
| `commands.log` | _(undescribed)_ |
| `cross_modulus_corrected.captured.txt` | Captured stdout of cross_modulus_corrected.py: verifies digit_free oracle (0,2,8 True, 5 False), pure class count = 2^(k-1) for k=1..9, Dr(q)=F_q coverage 100% for all ten q, and corrected mixed == pure == 2^(k-1)*T for every (q,k) — zero KILLs, so the old q=19,k=3,4 kills were artifacts of the s=0 proxy. |
| `cross_modulus_corrected.py` | Corrected mixed-modulus sieve: replaces the old s=0 proxy condition with the true mod-q consistency (∃ digit-2-free high part s with 2^r ≡ L_r + 3^k s mod q). Proves+verifies Dr(q)=F_q for every q coprime to 3, making (b') vacuous, and shows the old q=19,k=3,4 "kills" were artifacts of the s=0 over-constraint. |
| `cross_modulus_coverage_general.captured.txt` | _(undescribed)_ |
| `cross_modulus_coverage_general.py` | _(undescribed)_ |
| `cross_modulus_sieve.captured.txt` | Captured stdout of cross_modulus_sieve.py (the OLD s=0-proxy sieve): shows q=19,k=3,4 producing mixed < 2^(k-1) (the KILL flags) with killed classes r≡6 mod 18 and r≡24,42 mod 54 — these are superseded by the corrected mixed-modulus sieve, which shows them to be artifacts of the s=0 over-constraint. |
| `cross_modulus_sieve.py` | Mixed-modulus sieve: tests whether adding a mod-q constraint (2^r mod q in D, the sub-sum set of 3^0..3^(k-1) mod q) over a full period [0, ord_M(2)) kills survivor residue classes of the pure 3-adic sieve. Exact modular arithmetic, 2^r never built; verifies |
| `cvc5_invariant.smt2` | Independent cvc5 (QF_LIA) SMT-LIB check of the gate (n=0,2,8 reachable) and the witness refutations; agrees with z3 and returns unsat for the vacuous bare digit-free n>8 query. |
| `dh_determinacy_criterion_claim.md` | _(undescribed)_ |
| `dh_gate_independent.captured.txt` | Captured stdout of the buggy dh_gate_independent.py: M1/M2 PASS verdicts correct, then spurious MISMATCH rows from the wrong canon==i determinacy test — the bug dh_gate_independent2.py diagnoses and corrects. |
| `dh_gate_independent.py` | First independent re-derivation of the DH n=3 worked examples (naive enumeration of 2-powers/3-powers mod M1=5440, M2=2796160): correctly reproduces M1 extraneous (via indeterminate 2^6) and M2 clean — the two PASS verdicts, established two ways and NOT re-verified by dh_gate_independent2.py. Its determinacy spot-check is BUGGY: it tests canon_of_val==i (smallest exponent) instead of the definition (only exponent), printing spurious MISMATCHes on (5440,2,6..8), (2796160,2,7..9), (81,2,0..2), (512,2,9), (512,3,0..1). Superseded for the criterion check by dh_gate_independent2.py; kept because the M1/M2 verdicts it produced stand. |
| `dh_gate_independent2.captured.txt` | Captured stdout of dh_gate_independent2.py (EXIT_CODE=0): ALL PASS — criterion (a) i < v_p(M) equals direct definitional determinacy (b) for every (M,p,i) on all 8 moduli; 2^14 == 2^6 mod 5440 confirms 2^6 indeterminate while old canon==i test wrongly said True; table shows i=0..5 determinate, i>=6 indeterminate for M=5440. |
| `dh_gate_independent2.py` | CORRECTED determinacy spot-check for the DH n=3 cross-modulus classifier. Fixes the bug in dh_gate_independent.py (which tested determinacy as canon_of_val==i, i.e. "first exponent", not "only exponent"): recomputes determinacy from first principles — (a) criterion i < v_p(M) vs (b) direct definitional test (no b != i in 0..B, B = v_p + ord_{M/p^v}(p) + 5, with p^b == p^i mod M) — over p in {2,3}, i in 0..v_p+4, for M in {5440, 2796160, 81, 81, 46080=2^10*3^2*5, 27, 2592=2^5*3^4, 512}. Also proves the recurrence explicitly: 2^14 == 2^6 (mod 5440) so 2^6 is genuinely indeterminate while the OLD test wrongly returned True, and prints the determinate 0..5 / indeterminate 6..9 table for (5440,2). Exact integer arithmetic only (pow, sympy n_order, gcd); does NOT touch the M1/M2 PASS verdicts and does NOT reuse erdos.dh_classifier logic. Verified: ALL (a)==(b) agreed on all 8 moduli, both p, all i — capture in dh_gate_independent2.captured.txt. |
| `direct_verify_mod3j.captured.txt` | _(undescribed)_ |
| `direct_verify_mod3j.py` | _(undescribed)_ |
| `direct_verify_mod3j2.captured.txt` | _(undescribed)_ |
| `direct_verify_mod3j2.py` | _(undescribed)_ |
| `dr_surjectivity.captured.txt` | Captured stdout of dr_surjectivity.py (EXIT_CODE=0, 4.93s): oracle witnesses reproduced (digit_free 0,2,8 True; 2^5=1012_3 False); Dr(q)=F_q theorem printed and verified by construction for all 199 moduli (q in [5,300] with 3∤q plus 257,641,1021) for every residue; corrected mixed sieve pure==mixed==2^(k-1) on 90 (q,k) pairs (q in {5,7,11,13,17,19,29,41,193,257}, k 1..9, lcm cap 3e5); conclusion: H1 of CROSS-MODULUS-BEATS-SIEVE-HYPOTHESES REFUTED, |
| `dr_surjectivity_claim.md` | Claim note beside the dr_surjectivity capture: DR-SURJECTIVITY-ALL-Q (proved: Dr(q)=F_q for every q coprime to 3, via S_t=sum_{j<t}3^(j*ord_q(3)) ≡ t; verified by construction on 199 moduli × all residues) and CROSS-MODULUS-H1-REFUTED (verified-numerically: corrected mixed sieve never kills a survivor class, mixed==pure==2^(k-1) on all 90 (q,k) pairs; H1 of CROSS-MODULUS-BEATS-SIEVE-HYPOTHESES refuted as a counting mechanism). |
| `erdos2adic.captured.txt` | _(undescribed)_ |
| `oracle_mixed_kill.captured.txt` | _(undescribed)_ |
| `oracle_mixed_kill.py` | Independent brute-force oracle for the mixed-modulus sieve: verifies the two KILL cases (q=19,k=3 and q=19,k=4) by materialising 2^r as a big integer and checking both the low-k-ternary-digit condition and the mod-q sub-sum condition directly. Confirms the sieve's reported murdered survivor classes r≡6 mod 18, and r≡24, r≡42 mod 54. |
| `oracle_verify.captured.txt` | Captured stdout of run_oracle_verify.py (ALL PASS): the witness table, sieve_count vs 2^(k-1) k=1..26, and finite_check over [1,1000]={2,8}. The run's own oracle verification, cross-validated by direct and lift counts. |
| `oracle_verify_claim.md` | Claim block ORACLE-VERIFIED-THIS-WORKSPACE: this-workspace reproduction that digit_free(0,2,8)=True, sieve_count(k)==2^(k-1) for k=1..26 (direct and lift agree), finite_check[1,1000]={2,8}; resolves the |
| `pattern_branch.captured.txt` | _(undescribed)_ |
| `pattern_branch.py` | Probes survivor branch structure: which of the 3 lifts is excluded (digit 2), shown asymptotically uniform with no 2-adic pattern (k<=14). |
| `pattern_c0c2.captured.txt` | Executed output of pattern_c0c2.py at N=30000 (this run): #c0odd=14824, #c2odd=15073, first divergence n=1, max gap 264 — refutes the #{c0 odd}==#{c2 odd} count equality. |
| `pattern_c0c2.py` | Incremental base-3 digit-counter program that tests whether #{n<=N:c0(n) odd}==#{n<=N:c2(n) odd}; output in pattern_c0c2.captured.txt (refutes equality). Independently re-verified this run by checking the proved invariants c1-even and c0==c2+L mod 2 over n=1..30000 (0 violations), confirming the counter is correct. |
| `pattern_carry.captured.txt` | _(undescribed)_ |
| `pattern_carry.py` | _(undescribed)_ |
| `pattern_count_below_half_check.py` | _(undescribed)_ |
| `pattern_count_below_half_direct.captured.txt` | _(undescribed)_ |
| `pattern_count_below_half_direct.py` | Independent direct-residue-sieve recompute of C_k = #{survivors below half the period}, confirming the survivor-lifting values and that C_k never equals 2^(k-2) for k<=12 (negative closure). |
| `pattern_digitarg.captured.txt` | _(undescribed)_ |
| `pattern_digitarg.py` | _(undescribed)_ |
| `pattern_extend.captured.txt` | _(undescribed)_ |
| `pattern_extend.py` | _(undescribed)_ |
| `pattern_extend2.captured.txt` | _(undescribed)_ |
| `pattern_extend2.py` | _(undescribed)_ |
| `pattern_fresh.captured.txt` | _(undescribed)_ |
| `pattern_fresh.py` | _(undescribed)_ |
| `pattern_fresh5.captured.txt` | _(undescribed)_ |
| `pattern_fresh5.py` | _(undescribed)_ |
| `pattern_invproof.captured.txt` | _(undescribed)_ |
| `pattern_invproof.py` | Verifies the two load-bearing numeric claims of the S ∩ S^{-1} = {1} proof: inverse of 1+3^m has digit 2 at position m (m=1..11), and general y≡1 mod 3 cases give digit_m(inverse)=2. |
| `pattern_invset.captured.txt` | _(undescribed)_ |
| `pattern_invset.py` | Value-domain enumeration: among all 2^(k-1) units of S (digit-{0,1} set) mod 3^k, only x=1 has inverse in S. k=2..12. |
| `pattern_max.captured.txt` | _(undescribed)_ |
| `pattern_max.py` | _(undescribed)_ |
| `pattern_parity.captured.txt` | _(undescribed)_ |
| `pattern_parity.py` | _(undescribed)_ |
| `pattern_refl.captured.txt` | _(undescribed)_ |
| `pattern_refl.py` | _(undescribed)_ |
| `pattern_refl2.captured.txt` | _(undescribed)_ |
| `pattern_refl2.py` | Verifies A_k contains no reflection pair {r, P−r} except {0,0}, exact modular survivor lift to k=26, plus independent value-domain check via 2^r and 2^-r both digit-free only at r=0. |
| `pattern_residues.captured.txt` | _(undescribed)_ |
| `pattern_residues.py` | _(undescribed)_ |
| `pattern_residues3.captured.txt` | _(undescribed)_ |
| `pattern_residues3.py` | _(undescribed)_ |
| `pattern_residues4.captured.txt` | _(undescribed)_ |
| `pattern_residues4.py` | _(undescribed)_ |
| `pattern_residues5.captured.txt` | _(undescribed)_ |
| `pattern_residues5.py` | Probes survivor-exponent residue classes mod 3^j and 2*3^j against the digit-{0,1} value set, to test maximal-spread and characterization hypotheses; feeds regularity_findings_5.md |
| `pattern_residues6.captured.txt` | _(undescribed)_ |
| `pattern_residues6.py` | _(undescribed)_ |
| `pattern_residues7.captured.txt` | _(undescribed)_ |
| `pattern_residues7.py` | _(undescribed)_ |
| `pattern_survival.captured.txt` | _(undescribed)_ |
| `pattern_survival.py` | Computes the survival-depth sequence f(n)=least LSB base-3 digit position of 2^n that is a 2 (sieve survival depth); n=0,2,8 digit-free give inf. Varies over both parities; the odd-included version is dominated by trivial f(odd)=0. |
| `pattern_survival_corollaries.captured.txt` | _(undescribed)_ |
| `pattern_survival_corollaries.py` | Verifies two corollaries of the survival-depth membership restatement: (A) g(m)>=k depends only on m mod 3^(k-1), fresh second window zero mismatches; (B) |
| `pattern_survival_even.captured.txt` | _(undescribed)_ |
| `pattern_survival_even.py` | Computes g(m)=f(2m), the survival depth restricted to even exponents (odd n trivially have f=0). Produces the raw g(m) sequence that was run through analyze_sequence/find_linear_recurrence/oeis_lookup (no structure) in regularity_findings_5.md. |
| `pattern_survival_membership.captured.txt` | _(undescribed)_ |
| `pattern_survival_membership.py` | First (buggy) check of the membership restatement g(m)>=k <=> m mod 3^(k-1) in B_k. Superseded by pattern_survival_membership2.py which corrected two bugs (digit-free m, n/m off-by-bound); kept to document the earlier attempt, not used for the result. |
| `pattern_survival_membership2.captured.txt` | _(undescribed)_ |
| `pattern_survival_membership2.py` | Corrected verification that g(m)>=k <=> m mod 3^(k-1) in B_k (halved survivor set, |
| `prove_mod3j_count.captured.txt` | _(undescribed)_ |
| `prove_mod3j_count.py` | _(undescribed)_ |
| `regularity_findings.md` | Pattern-finder pass over the run's computed digit-count and survivor-residue data: the two proved exact regularities (c1(n) even for all n>=1 [claim c1-even-parity, discharging G-cong(i)]; |
| `regularity_findings_2.md` | Second pattern-finder pass: survivor-exponent residue structure (fill all even classes mod 2^m), digit-count parity facts (c1 even proved, c0==c2 refuted), and the refuted max=period-12 guess. The exact structural negatives the symbolic-invariant route must work around. |
| `regularity_findings_3.md` | Third pattern pass: refutes the #{c0 odd}==#{c2 odd} count coincidence (211=211 at N=400 is a crossing, not a law — differs by N=200), establishes the exact modular identity c0==c2+L(n) mod 2, and closes the survivor branch-excluded-child probe as uniform/patternless. |
| `regularity_findings_3_claim.md` | Claim block c0c2-count-parity-not-equal: statement + hypotheses + two-program verification that the c0/c2 odd-count equality does not hold in general. |
| `regularity_findings_4.md` | Pattern-finder fourth pass: carry-count sequence c(n) on the ×2 base-3 transducer — negative linear/polynomial/OEIS structure, and the proved equivalence c(n)=0 ⟺ digit_free(2^n) (a reformulation of the digit-2-free predicate). |
| `regularity_findings_5.md` | _(undescribed)_ |
| `regularity_findings_6.md` | Sixth pattern-finder pass: proves |
| `regularity_findings_7.md` | Pattern-finder 7th pass: proves S ∩ S^{-1} = {1} in Z_3 (only {0,1}-digit 3-adic unit whose inverse is also {0,1}-digit is 1), and the resulting anti-orbit fact that survivor-exponent set A_k contains no reflection pair {r, period−r} except {0,0} for k=2..26. This is the newly-proved partial result. |
| `run_dh_verify.sh` | _(undescribed)_ |
| `run_oracle_verify.py` | Verification driver for the Erdős oracle. Prints witness table (digit_free on 0,2,8 free and 1,3,5 containing 2), sieve_count(k) vs 2^(k-1) for k=1..26 cross-checked against direct_count and lift_count for k<=11, and finite_check(1,1000). |
| `spencer_verify.captured.txt` | Executed capture of spencer_verify.py, EXIT_CODE=0, ALL PASS: Lemma 6.1 27-word exhaustion, Lemma 9.1 (no 1+3^s a power of 2 for s in [2,40]), reduced cofactors core(101_3)=5 and core(21_3)=7 preserved under 3-scaling, canonical packet 2101_3=64 -> 256=100111_3 digit-free -> *4 = 1101221_3 (has 2), witnesses digit_free(1,4,256)=True / digit_free(2,8,32)=False. |
| `spencer_verify.py` | Machine-executed check of the Spencer 2026 carry-packet preprint's arithmetic (was never run before this run: its docstring said no shell existed). Confirms the lemmas' arithmetic; does NOT repair the missing induction that makes Theorem 12.1 unsound (claim SPENCER-CARRY-PACKET-UNSOUND). BUG FIXED on first execution: probe originally tested core(10101_3=91) against the 7-cofactor, which the source attaches to 21_3=7. |
| `spencer_verify_claim.md` | Hand-verification note for the Spencer 2026 carry-packet preprint: confirms its arithmetic (Lemma 6.1 list, Lemma 9.1, reduced cofactors, canonical packet 2101_3=64->256) and documents why the proof is still unsound (missing induction in Thm 12.1). This is where claim SPENCER-CARRY-PACKET-UNSOUND, status checked, is recorded. |
| `validate_invariant_models.captured.txt` | _(undescribed)_ |
| `validate_invariant_models.py` | Validates by direct integer arithmetic each model the solver returned: confirms n=0 refutes C1/C2 (Polarity=1), and n=8 digits reconstruct 256=100111_3, so the models really falsify the stated candidates. |
| `verify_2adic_family.captured.txt` | _(undescribed)_ |
| `verify_2adic_family.py` | _(undescribed)_ |
| `verify_c0c2.py` | Cross-check of the incremental base-3 counter against direct 2**n digit counting (match at N=200). |
| `verify_c0c2_400.py` | Re-verifies the 211=211 at N=400 and shows the counts already differ at N=200; confirms incremental==direct at 400. |
| `verify_dh_n3.captured.txt` | _(undescribed)_ |
| `verify_dh_n3.py` | Verifies the two worked n=3 examples of Dimitrov-Howe (M1=5440 has extraneous solutions via indeterminate 2^6; M2=2^7*5*17*257 is clean with all determinate summands), reproducing Definition 2.2, Notation 2.3 and Lemma 3.1. Hand-verified this run; ready for the harness to execute and capture for machine confirmation. |
| `verify_dh_n3_examples.py` | SUPERSEDED by verify_dh_n3.py. Early, partially-buggy draft of the DH n=3 enumeration (had a broken factorization line). Do not run; use verify_dh_n3.py. |
| `verify_dh_n3_lemma.py` | SUPERSEDED by verify_dh_n3.py (its Lemma 3.1 cross-order hypothesis checks are incorporated there). Do not run; use verify_dh_n3.py. |
| `verify_spencer_carry.py` | _(undescribed)_ |
| `witness_invariants.py` | Independent hand/machine check (no Z3) of the three witnesses 0,2,8 and the candidate invariants (Polarity, digit counts, carry) used as the oracle the SMT encoding must agree with. |
| `z3_invariant.captured.txt` | _(undescribed)_ |
| `z3_invariant.cvc5.captured.txt` | _(undescribed)_ |
| `z3_invariant.py` | Z3 (QF_LIA, digit bound L=40) test of candidate symbolic invariants (G-invariant skeleton) for the Erdős conjecture: gate passes finding witnesses 0,2,8; C1 and C2 (weighted Polarity) are refuted at witness n=0; bare digit-free n>8 is vacuously UNSAT (no digit-free n>8 in range, by exact oracle). established: gate finds 0,2,8; C2 refuted by model n=0; encoding is not over-constrained. |
