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