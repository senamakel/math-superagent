# PE591 Run Verification Report

Commands run in order from /workspace. No existing files modified.

## (1) `python3 brute.py` — verbatim output
```
BQA_2(pi,10) = (6, -2, 0.029980221664016593)
BQA_5(pi,100) = (-55, 26, 0.0038252385952581847)
BQA_7(pi,10^6) = (560323, -211781, 1.2236465742887503e-06)
```
Matches statement examples:
- BQA_2(pi,10) = 6 - 2*sqrt(2):  (a,b)=(6,-2)       PASS
- BQA_5(pi,100) = 26*sqrt(5)-55:  (a,b)=(-55,26)    PASS
- BQA_7(pi,10^6) = 560323-211781 sqrt(7): (a,b)=(560323,-211781) PASS

## (2) `python3 solution_bothsides.py` — worked-example lines (verbatim)
```
  d=2: pos b=5 err=0.0705248; neg b=-2 err=0.0299802
d=2 n=10: (a=6, b=-2) |a|=6
  d=5: pos b=26 err=0.00382524; neg b=-29 err=0.012436
d=5 n=100: (a=-55, b=26) |a|=55
  d=7: pos b=302307 err=1.3496e-6; neg b=-211781 err=1.22365e-6
d=7 n=1000000: (a=560323, b=-211781) |a|=560323
  d=2: pos b=4375636191520 err=4.17055e-15; neg b=-4447114215301 err=4.42435e-14
d=2 n=10000000000000: (a=-6188084046055, b=4375636191520) |a|=6188084046055
```
d=2 n=10^13 gives a=-6188084046055  ->  matches oracle example 4.  PASS.

Final line:
```
S = 526007984625966
```

## (3) Independent re-sum of |a| column from results_full_bothsides.txt
Python one-liner with exact ints, skipped the trailing "S ..." marker:
- 90 data rows (all non-square d in [2,99]); last line is `S 526007984625966` (ignored).
- d=2 row present: (2, 4375636191520, -6188084046055, 6188084046055) — matches oracle.
- independent_recomputed_S = 526007984625966
- matches_expected = True

## Verdict
PASS — S = 526007984625966, independently re-derived from the results file,
equal to the solver's accumulator and to the expected value.
