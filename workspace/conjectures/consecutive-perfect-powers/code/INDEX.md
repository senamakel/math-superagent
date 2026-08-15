# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `brute.py` | Bounded exact search oracle for consecutive perfect powers (returns (3,2,2,3)). |
| `cassels_reduction.py` / `cassels_valuation.py` / `cassels_reduction_crosscheck.py` | Cassels-style reductions and valuations for Catalan. |
| `classgroup.py`, `cond_driver.py`, `crossprime_sweep.py`, `exp2_crosscheck.py`, `exp2_explore.py`, `exp2_verify.py`, `hminus_full.py` | Various checks across the run (class groups, conditions, exponent-2, h-minus). |
| `exp2_even_proof.py` | Machine-verifies lemma exp2-a-even: x^2-y^q=1, x even, q odd prime, has no solution (3-step elementary proof, exact integer arithmetic; oracle over even x<=10^7, q<=30 finds none). |
| `lebesgueB/.md.md` | Lebesgue Case B Z[i] proof verification, unit kept explicit — `verify_z[i]_mirror.py`, all 13 checks PASS, output `code/out/lebesgueB_z[i].captured.txt`. |
| `pattern_bernoulli_check.py`, `pattern_crossprime_corr.py`, `pattern_dw_char.py`, `pattern_dw_extend.py`, `pattern_dw_structure.py`, `pattern_irregular83.py`, `pattern_irregularity.py`, `pattern_sequences.py` | Pattern-search probes over the conjectural structure (Bernoulli, cross-prime correlations, Wieferich character). |
| `prove_T_c_odd_nonsquare.py` | Proof certificate (exit 0, first run this turn) that T(c,p)=sum(c^2+1)^k ≡ 7 (mod 8) for c odd, any odd prime p≥3, so T(c,p) is never a square for c odd. Verified (a)-(f) on exact integers. DECISIVE: in Lebesgue Case B the reduction forces x odd hence c even, so this rung is vacuous there; no modulus <2000 rules out squares for even c. |
| `prove_T_mod8_classification.py` | Complete mod-8 classification of T(c,p): certifies the three residue formulas (c odd -> 7; c=0 mod 4 -> p; c=2 mod 4 -> 3p-2 mod 8), emits the (c mod 8, p mod 8) class table, and confirms over a box that eliminated classes contain no squares while only c even & p==1 mod 8 remains open (the residual gap for Ljunggren). |
| `rfixed23_proof.py`, `stick_index.py`, `stick_index_py.py`, `stick_index.sage`, `thue_unit_descent.py`, `verify_foundations.py` | Descent / Stickelberger-index / Thue unit descent / foundation verification. |
| `run_verify.sh` | Wrapper to run verification with a timeout and tee. |
| `scholar_verify_ramification.py` | Exact-algebra check that Conrad's ramification claim (p)=prod_{k=1}^{p-1}(1-zeta^k)=(1-zeta)^(p-1) holds for odd primes p, via Phi_p(1)=p and the exact product identity in Z[zeta_p]. |
| `verify_bundle.py` | Four-section exact-integer verification bundle for Catalan (x^p-y^q=1). S1: oracle solutions(N) extended to N=1e10,1e12 (returns exactly [(3,2,2,3)]). S2: Case-A descent subclaim r^q - 2^(mq-2)s^q = ±1 verified over q<=101, m<=10, r,s<=2000, only (3,1,1,1). S3: T(c,p)=((c^2+1)^p-1)/c^2 never a square over c<=1e5, odd primes p<=251, 0 squares. S4: recomputes h^-(Q(zeta_p)) for all 45 odd primes <200, finds exactly one cross-prime survivor (47,139), which fails both double-Wieferich congruences. Correctness established by: oracle reproducing known solution (3,2,2,3); exact isqrt/q-root (no floats); h^- values matching prior crossprime_sweep200 and OEIS A000927. Output at code/out/verify_bundle.captured.txt. Bounded verification only, not proofs. |
