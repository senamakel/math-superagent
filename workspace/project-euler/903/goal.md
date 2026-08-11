# Goal

Compute Q(10^6) mod (10^9+7), where

Q(n) = sum over all permutations pi of {1..n} of [ sum_{i=1}^{n!} rank(pi^i) ],
rank = 1-based position in lexicographically sorted list of all n! permutations,
pi^i = i-th iterate of pi (order-preserving power, pi^1 = pi, pi^0 = identity).

## Worked examples (test oracle)
- rank(2,1,3) = 3.
- Q(2) = 5
- Q(3) = 88
- Q(6) = 133103808
- Q(10) ≡ 468421536 (mod 10^9+7)

## Completion criteria
1. brute.py reproduces all of: Q(2)=5, Q(3)=88, Q(6)=133103808 (mod p) and lex example rank(2,1,3)=3.  (CURRENT SUBTASK — in progress)
2. brute2.py (independent method: Q(n) = sum_pi (n!/ord(pi)) * sum_{tau in <pi>} rank(tau)) agrees with brute.py for n=2..6.
3. solution.py (efficient, exact mod-p arithmetic) agrees with brute.py on every case brute can reach.
4. solution.py reproduces Q(10) ≡ 468421536 mod p (secondary example).
5. solution.py computes Q(10^6) mod p.
6. Answer verified by a second, independent route or stated as unverified.

## Status
- [x] Objective recorded (above).
- [ ] Sub-task: brute.py + brute2.py written, run for n=2..7 (+ n=8 if feasible), values checked.
- [ ] Sub-task: efficient solution.py agreeing with brute force.
- [x] gaps.py: T(j,m) computed for n=2..9 with period formula; shown
      translation-invariant in j and exactly arithmetic in the gap k.
      (memory.md has tables. This is a structural lead for the n=10^6 method.)
- [x] verify_red.py: central reduction Q(n) = (n!)^2 + A_n*S + (B_n/2)*T with
      S=Sigma m*m! (=n!-1), T=Sigma m(m-1)*m!, A=f[0], B=f[1]-f[0], verified
      EXACT big-int match against Q(2..8). ALL PASS.  Problem reduced to
      finding A_n and B_n (memory.md).