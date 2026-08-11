# Tasks

- [x] Record objective and completion criteria in goal.md (already present from prior context).
- [x] Read problem statement (problem.html) and confirm worked examples: rank(2,1,3)=3, Q(2)=5, Q(3)=88, Q(6)=133103808, Q(10) mod p = 468421536.
- [ ] Write /workspace/brute.py — method 1: literal double sum, for every pi compute pi^i for i=1..n! and sum rank(pi^i); lex-order rank dict; reproduce rank(2,1,3)=3.
- [ ] Write /workspace/brute2.py — method 2: Q(n) = sum_pi (n!/ord(pi)) * sum_{tau in <pi>} rank(tau) over distinct powers.
- [ ] Run both for n=2,3,4,5,6; check Q(2)=5, Q(3)=88, Q(6)=133103808; methods agree.
- [ ] Run n=7 (both methods).  Report timing.
- [ ] Run n=8: method 2 always; method 1 only if estimated to finish within ~5 min.
- [ ] Record verified values and timings in memory.md.
- [ ] (Later) Derive efficient method for Q(10^6) mod p; validate against oracle values.