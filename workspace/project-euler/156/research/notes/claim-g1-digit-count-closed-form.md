# Claim G1 — closed form for the digit-count function

The digit-count function fd(x) (occurrences of digit d in the decimal writings
of 1..x, equivalently of 0..x for d > 0) has an exact O(number of digits)
evaluation by summing per-position contributions.  This is the standard
place-value digit count.

```claim
id: G1-digit-count-closed-form
statement: >
  For n ≥ 0 with decimal digits x_k ... x_0 (x_k the digit in the k-th place
  from the right), fd(n) = Σ_k c_d(x_k), where with Y = floor(n/10^k)·10^(k-1):
  c_d(x_k) = Y when d>0 and x_k < d;
  c_d(x_k) = Y + (n mod 10^(k-1)) + 1 when d>0 and x_k = d;
  c_d(x_k) = Y + 10^(k-1) when d>0 and x_k > d.
  (d = 0 needs a separate adjustment for leading zeros, not needed here since
  PE156 only uses d in {1,...,9}.)  Cost is one pass over the digits: O(log n)
  time, O(log n) space, exact integer arithmetic.
hypotheses: >
  d in {1,...,9}; the formula counts d in 1..n, which equals the problem's
  f(n,d) counting d in 0..n because 0 contributes no occurrence of a nonzero
  digit.  The formula is the same identity in three forms across the library
  (paper Section 7 eq. (1); math.SE closed form f(d,n); GeeksforGeeks and
  LearnYard per-position/Digit-DP treatments).
holds-here: yes
status: >
  Sourced (three independent sources below); the run's tool_builder must still
  implement it and check it against code/brute.py on the statement's oracle
  points f(11,1)=4, f(12,1)=5, first solutions 0, 1, 199981, and s(1).
bearing: >
  Discharges gap G1 of research/backward/fixed-point-enumeration.md: the
  search can jump by evaluating f at chosen points instead of visiting
  numbers; combined with G2's bound [0, d·10^10] and G3's skip rules this
  gives an exact, fast solver.
anchor: >
  Khovanova & Marton, arXiv:2305.10357v2 Section 7 (eq. (1)) and AMM 132(8)
  2025 780-787 Section 7; math.stackexchange.com/questions/47477 answer by
  crasic (formula f(d,n)); geeksforgeeks.org/dsa/find-the-occurrences-of-y-in-the-range-of-x
  and learnyard.com (per-position/Digit-DP algorithms).
```