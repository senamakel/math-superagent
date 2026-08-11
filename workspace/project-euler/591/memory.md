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

## Established results
(none yet)

## Failed approaches
(none yet)

## Open questions
- Structure of record b's for ||b sqrt(d) - pi||_Z (Task 2 probing).
- Exact scalable method for n=10^13.
