# Tasks

- [x] Record objective and completion criteria in goal.md (already present from prior context).
- [x] Pipeline re-verified 18 Sep 2025: brute.py + brute2.py at n=2,3,6 (all oracles OK, methods agree); solution.py self-test n=2..8 OK after fixing a path bug (out/extend_f.json); task12.py OK (Q(10) mod p = 468421536).
- [x] ccsum.py conjugacy-class engine run CCSUM_MAX=30 CCSUM_GATE=120: reaches n=30 fast but matches extend_f.json ONLY at n=2. Root cause PROVEN (test_classconst.py): cyclic-subgroup count S(lambda,k) is NOT constant on a conjugacy class, so the single-representative-per-class design is invalid. ccsum rows n>=3 are UNTRUSTED; written out/ccsum.json + out/ccsum_ab.json (n=2..30) with old captures backed up.
- [x] Wrote code/anbtable.py -> code/out/anbtable.txt (A, B, A//(n-1)!, B//(n-1)!, A%(n-1)!, B%(n-1)! for n=2..30 with per-row TRUST flag, plus trusted n=2..11 reference from extend_f.json). No closed form attempted (per instruction).
- [ ] (Later) Derive efficient method for Q(10^6) mod p; validate against oracle values. NOTE: the ccsum.py conjugacy-class engine does NOT provide valid A_n/B_n past n=11 — a correct method must sum S over all representatives per class, not one representative.
- [x] Run n=7 (both methods).  Method1 7.17s, method2 0.02s; exact agreement.
      Q(7)=47124948960, mod p = 124948631.
- [x] Run n=8: method 2 gave Q(8)=24768798220800, mod p = 798047424 (0.16s);
      method 1 skipped — measured n=7 speed predicts 8.7 min > 5 min budget
      (gate in brute.py confirmed: [gate] estimate too large -> skipped).
- [x] Record verified values and timings in memory.md.
- [x] Derive efficient method for Q(10^6) mod p.  **DONE**: closedform_derivation.md
      gives closed forms A_n, B_n; solution103.py (modular) + closedform_exact.py
      (exact) both ALL PASS.  **ANSWER: Q(10^6) mod p = 128553191**.

- [x] gaps.py: compute T(j,m) for n=2..9 by period formula (exact, no literal
      n!-power iteration). Verified translation invariance (all j) and found
      f_n(k)=T(1,1+k) is exactly arithmetic in k for n>=3. Oracle-checked n=2..5.
      A_n and B_n tables recorded in memory.md.
- [x] Ran brute.py and brute2.py for n=2..7; oracle OK (rank(2,1,3)=3, Q(2)=5,
      Q(3)=88, Q(6)=133103808); methods agree exactly on all n=2..7.
- [x] Wrote and ran explore.py (n=2..7): M_j and N(j,m) tables.  Pattern found:
      N(j,m)=f(m-j) translation-invariant; M_j = suffix sum of f.
- [x] extend_f.py: computed f_n(k) for n=2..11 by the period formula (0-based,
      row j=0), exact ints, saved to extend_f.json.  Every row is exactly
      arithmetic in k (2nd diff all zero).  New rows n=10, n=11 recorded.
- [x] verify_f_method2.py: independent cycle-type-decomposition recomputation of
      the n=10,11 rows; matches extend_f.json exactly (n=10 24.5s, n=11 319s).
- [x] verify_red.py: central reduction verified n=2..8; Q(10) mod p via
      extend_f.json chain reproduces 468421536.
- [x] closedform_derivation.md: closed forms A_n,B_n derived (sigma-measure
      decomposition + Campion-Loth Lemma 4.7 + three mu-moments); O(n) modular
      scheme.
- [x] closedform_exact.py: exact verification — ALL PASS (Lemma 4.7 per-class,
      mu-moments by orbit sum, closed-form rows == extend_f.json n=2..11,
      Q via verified reduction, Q(10)==468421536).
- [x] solution103.py: modular O(n) evaluator — ALL PASS (self-tests n=2..11,
      S direct/phi + exact/modular cross-checks, stability at 10^6).
      **ANSWER: Q(10^6) mod (10^9+7) = 128553191** (out/solution103_output.txt).