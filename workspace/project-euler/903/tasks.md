# Tasks

- [x] Record objective and completion criteria in goal.md (already present from prior context).
- [x] Read problem statement (problem.html) and confirm worked examples: rank(2,1,3)=3, Q(2)=5, Q(3)=88, Q(6)=133103808, Q(10) mod p = 468421536.
- [ ] Write /workspace/brute.py — method 1: literal double sum, for every pi compute pi^i for i=1..n! and sum rank(pi^i); lex-order rank dict; reproduce rank(2,1,3)=3.
- [ ] Write /workspace/brute2.py — method 2: Q(n) = sum_pi (n!/ord(pi)) * sum_{tau in <pi>} rank(tau) over distinct powers.
- [ ] Run both for n=2,3,4,5,6; check Q(2)=5, Q(3)=88, Q(6)=133103808; methods agree.
- [x] Run n=7 (both methods).  Method1 7.17s, method2 0.02s; exact agreement.
      Q(7)=47124948960, mod p = 124948631.
- [x] Run n=8: method 2 gave Q(8)=24768798220800, mod p = 798047424 (0.16s);
      method 1 skipped — measured n=7 speed predicts 8.7 min > 5 min budget
      (gate in brute.py confirmed: [gate] estimate too large -> skipped).
- [x] Record verified values and timings in memory.md.
- [ ] (Later) Derive efficient method for Q(10^6) mod p; validate against oracle values.

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