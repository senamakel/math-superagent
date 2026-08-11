# Working memory

## Problem

S = sum over non-square d in [2,99] of |I_d(BQA_d(pi, 10^13))|.

BQA_d(x,n) = argmin over (a,b), |a|<=n, |b|<=n of |x-(a+b*sqrt(d))|.
I_d(a+b sqrt(d)) = a.

For fixed b, best a = round(pi - b*sqrt(d)), error = ||b sqrt(d) - pi||_Z.

## Worked examples (test oracle)
1. BQA_2(pi,10)        = 6 - 2 sqrt2        a=6,b=-2
2. BQA_5(pi,100)       = 26 sqrt5 - 55      a=-55,b=26
3. BQA_7(pi,10^6)      = 560323 - 211781 sqrt7  a=560323,b=-211781
4. I_2(BQA_2(pi,10^13))= -6188084046055     a=-6188084046055,b=4375636191520

## Verified (Task 1)
brute.py reproduces examples 1,2,3 exactly (see run output in scratchpad).
solution_bothsides.py reproduces ALL FOUR examples (1-3 plus the d=2 n=1e13 oracle).

## Additional exact laws (verified on corrected both-sign data, n=1e13)
- |I_d| == |nint(b_d sqrt(d) - pi)| for all 90 d (90/90).
- m^2 scaling: |I_{m^2 d0}| == |I_{d0}| iff m | b_{d0} (36/36 pairs); when equal,
  b_{m^2 d0} == b_{d0}/m (18/18).

## Established results
- Cabanillas Prop 9/10 (arXiv:1904.01874) candidate set for record b's of
  ||b alpha - beta||_Z, alpha={sqrt d}, beta={pi}, verified EXACTLY against
  brute force on d in {2,3,5,7,11}, N in {200,1000,5000} AND at full method
  scale n=10^6 for ALL 90 non-square d (both signs of b):
  b_d = Cabanillas candidate with minimum distance; a = nint(pi - b sqrt(d)).
  (toolkits/verify_cabanillas_exact.py, toolkits/validate_all_d.py,
   toolkits/validate_bothsides.py)
- d=2 oracle verified exactly: a+b.sqrt(2)-pi = -4.2930117e-15; b=4375636191520
  is NOT a sqrt(2) semiconvergent denominator (toolkits/verify_oracle_d2.py).
- uniform exact relation at n=10^4 (90 d's): |I_d| = nint(b_d*sqrt(d) - pi)
  = nint(b_d*sqrt(d)) - 3  (toolkits/analyze_Id_b.py). NOTE: |I_d| != round(sqrt(d)*b)
  (check_rel.py claims were false).
- record-b sequences (probe_records.py, N=2e6) show NO simple linear recurrence,
  no polynomial growth; all are Cabanillas candidates, NOT semiconvergents in general.
- **ALL 90 non-square d validated**: at n=10^6, Cabanillas-candidate b_d equals
  brute-force argmin for every d in [2,99] (toolkits/validate_all_d.py, 47s,
  zero mismatches). This is the uniform cross-check of the method across all d.

## Failed approaches
- "records are semiconvergents of sqrt(d)" hypothesis: FALSE (d=2 oracle b not a
  semiconvergent; most records aren't).
- check_rel.py |I|=round(sqrt(d)*b): FALSE.

## Open questions (all resolved)
- CONFIRMED (all closed): b_d at n=10^13 via Cabanillas candidates reproduces
  d=2 oracle (b=4375636191520, a=-6188084046055).
- **CRITICAL correction**: b may be NEGATIVE. solution.py searched only b>=0 and
  got S=498809825393729, which is WRONG. Corrected both-sign solver
  /workspace/solution_bothsides.py reproduces examples 1-4 (d=2,n=10 has b=-2;
  d=7,n=1e6 has b=-211781) and matches brute force on all 90 d at n=1e6
  (toolkits/validate_bothsides.py). **S (corrected) = 526007984625966**,
  written to /workspace/results_full_bothsides.txt. Positive-only was strictly
  worse on 45 d (negative-b winners), never better.
