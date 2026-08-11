# Working memory

## Problem

We need S = sum over non-square d in [2,99] of |I_d(BQA_d(pi, 10^13))|.

BQA_d(x,n) = argmin over (a,b), |a|<=n, |b|<=n of |x - (a + b*sqrt(d))|.
I_d(a+b sqrt(d)) = a.

For fixed b, best a = round(pi - b*sqrt(d)). Error for that b is
||b*sqrt(d) - pi||_Z = distance of b*sqrt(d) to nearest integer (distance to pi+Z).

Box: |a|<=n => b*sqrt(d) must stay near pi + integer within box. Since best
accuracy comes from tiny errors far inside, the active b range is roughly
0 <= b <= n/sqrt(d) (interior, |a| clamped only far away where error is large).

Both signs of b matter (approximation to +pi and to -pi essentially).

## Worked examples (test oracle)
1. BQA_2(pi,10)        = 6 - 2 sqrt2        a=6,    |a|=6
2. BQA_5(pi,100)       = 26 sqrt5 - 55      a=-55,  |a|=55
3. BQA_7(pi,10^6)      = 560323 - 211781 sqrt7  a=560323, |a|=560323
4. I_2(BQA_2(pi,10^13))= -6188084046055     a=-6188084046055, |a|=6188084046055
   (so b=4375636191520, and |a|,|b|<1e13)

## Established results
(none yet)

## Failed approaches
(none yet)

## Open questions
- Exact structure of record-holder b's for ||b sqrt(d) - pi||.
- Efficient method for n=10^13.

## Plan
1. brute.py reproduces examples 1,2,3 (feasible). 
2. Discover record pattern for all d at small n.
3. Find scalable method (CF-based), verify vs brute at reachable sizes.
4. Reproduce example 4 (d=2, n=10^13) with real method.
5. Sum over all d, verify by independent route.
