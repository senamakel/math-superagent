# verify.py — independent second route, grand total

`code/verify.py` is the independent second route for PE156. Its digit-count
evaluators are two most-significant digit-position enumerations that share no
code with the primary counter `code/lib/digits.py` (least-significant
place-value peeling): a closed-form block-enumeration with prefix counts
(`f_prefix_blocks`) and a textbook memoized `(pos, tight)` digit-DP
(`f_digit_dp`). The fixed points are found by a jump iterator whose two rules
are re-derived from monotonicity alone (R1: f=c>n ⇒ (n,c) empty, resume at c;
R2: gap grows ≤ D-1 per step, coast ceil((n-c)/(D-1))). Search bound
n < d·10^10 is Khovanova–Marton Prop. 9.1 (d·b^b), sanity-probed by
f(d·10^10, d) > d·10^10.

Output: `code/out/verify-output.txt` (captured 2026 run, wall time 4.31 s).

```claim
id: PE156-grand-total-verified
statement: >
  Sum_{d=1..9} s(d) = 21295121502550, where s(d) is the sum of all n with
  f(n,d) = n (each n counted once per digit it satisfies; f(n,d) counts
  occurrences of digit d in the decimal writings of 0..n).  Per-digit:
  s(1)=22786974071 (matches the problem statement), s(2)=73737982962,
  s(3)=372647999625, s(4)=741999999540, s(5)=100000000000, s(6)=2434703999430,
  s(7)=1876917059570, s(8)=15312327487352, s(9)=360000000000.
hypotheses: >
  decimal base; d in 1..9; n counted once per satisfying digit; solutions
  bounded by n < d*10^10 (Khovanova–Marton Prop. 9.1, proven in source).
holds-here: yes
status: checked (computed by code/verify.py, 2026)
bearing: >
  This is the answer to Project Euler 156.  Independently verified by three
  structurally different evaluators — the two new digit-DP routes of
  verify.py and the primary place-value counter f_place_value from
  code/lib/digits.py — each driving the jump iterator to full size and
  producing identical per-digit solution lists and sums.  Agreement with the
  naive oracle (code/brute.py): both evaluators equal f_naive for all
  n <= 20000, d = 1..9, and the d=1 jump run over 0..300000 equals the
  brute-force scan exactly (458 probes vs 300001 scanned).  Oracle points
  reproduced: f(11,1)=4, f(12,1)=5, f(22,2)=6, statement table f(n,1)
  n=0..12, first fixed points 0, 1, 199981, s(1)=22786974071.  Per-digit
  solution counts equal the sourced counts [84,14,36,48,5,72,49,344,9]
  (OEIS A130432, a completeness flag).  d=1's 84 terms start with the OEIS
  A014778 %S block and end at the sourced last term 1111111110.
anchor: code/verify.py; output code/out/verify-output.txt; bound source
  research/notes/claim-g2-solution-bound.md
```
