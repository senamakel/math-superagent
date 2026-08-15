# Index — code/caseB

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `caseB_complete_closure.py` | Completes Case B of Catalan via the Nagell-Ljunggren theorem, exact for the slice. Points 1-2: states the slice (n=p odd prime >=3, X=c^2+1>=5, residual class X≡1 mod 4) and checks exactly that both N-L exceptions (4,7,20) and (5,3,11) are excluded (n=4 even; c^2=2 impossible; X=3,7 fail X≡1 mod 4). Point 3: independent exact oracle that T(c,p)=((c^2+1)^p-1)/c^2 is not a square for c even in [2,200000], odd primes p in [3,199] — 4.5e6 pairs, 0 squares, 7.78s via ProcessPoolExecutor (28 workers); wider on small-c than the prior verify_bundle box, settles nothing new. Point 4: direct exact enumeration of (X^n-1)/(X-1)=Y^2 for n in {2,3,4,5}, X in [2,10^6] — confirms both exceptions (7,20) and (3,11) and no other solution in odd indices n=3,5. Exact integer arithmetic (pow + math.isqrt), no floats. Correctness established: ALL CHECKS PASS (EXIT 0), captures in code/out/caseB_complete_closure.captured.txt; the reduction (claim exp2-caseB-reduction) and mod-8 classification (claim exp2-caseB-t-mod8-classification) are the proved in-workspace premises; Nagell-Ljunggren itself is asserted-classical (verified numerically). |
| `certify_lebesgue_caseB.py` | Certifies the Case-B reduction: x^p-y^2=1 (p odd prime) forces x=c^2+1, y=c·m, m^2=T(c,p)=Σ(c²+1)^i. Steps 1-5 machine-certified (parity, Z[i] factorisation, unit absorption, d=±1, c |
| `check_step4_bound.py` | _(undescribed)_ |
| `extend_square_check.py` | _(undescribed)_ |
| `probe_T_exact_mod8.py` | Primer for the Case-B mod-8 classification: computes T(c,p)=sum(c^2+1)^k exactly then mod 8 by (c mod 4, p mod 4) class. Ran to a clean capture (code/out/probe_T_exact_mod8.captured.txt) showing c odd => T=7 mod 8 for all sampled p; superseded by the proof-certificate programs prove_T_c_odd_nonsquare.py and prove_T_mod8_classification.py. |
| `probe_T_mod8.py` | _(undescribed)_ |
| `probe_step4_lemmas.py` | _(undescribed)_ |
| `prove_T_mod_lemmas.py` | _(undescribed)_ |
| `prove_mod_obstruction.py` | _(undescribed)_ |
| `residual_modulus_hunt.py` | Hunts for a fixed modulus M on which T(c,p)=sum(c^2+1)^k is NEVER a square mod M over the residual class (c even, p odd prime ==1 mod 8) of Case B. Establishes (and per-candidate verifies) that NO fixed M closes the class: for every M, c=2M and p=least prime==1 mod lcm(8,M) give T(2M,p) == p == 1 (mod M), a square; c^2==0 mod M collapses every term of the geometric sum. Also runs a sanity oracle (0 true squares for c even<=400, p in [17,300], p==1 mod 8 — consistent with Ljunggren). Exact integer arithmetic, no floats. Correct because the construction is unconditional (Dirichlet guarantees p) and confirmed by independent enumeration (method B) agreeing with method A on all 33 candidate moduli; output in code/out/residual_modulus_hunt.captured.txt (EXIT 0). |
| `time_sample.py` | _(undescribed)_ |
| `time_sample2.py` | _(undescribed)_ |
