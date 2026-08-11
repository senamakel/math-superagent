# Goal

## Objective
Solve Project Euler 591 (https://projecteuler.net/minimal=591), statement saved at
/workspace/problem.html.

## Restatement with symbols
- d : a non-square positive integer.
- quadratic integer for basis sqrt(d): a + b*sqrt(d), with a,b integers.
- BQA_d(x, n) : the quadratic integer closest to the real x among those with
  |a| <= n and |b| <= n. "Closest" = minimizes |a + b*sqrt(d) - x|.
- I_d(a + b*sqrt(d)) = a  (the integral part, i.e. the coefficient a).

Let x = pi, n = 10^13.

## Worked examples (test oracle)
1. BQA_2(pi, 10)     = 6 - 2*sqrt(2)        -> a=6,  b=-2, |a|=6
2. BQA_5(pi, 100)    = 26*sqrt(5) - 55      -> a=-55, b=26, |a|=55
3. BQA_7(pi, 10^6)   = 560323 - 211781*sqrt(7) -> a=560323, b=-211781, |a|=560323
4. I_2(BQA_2(pi,10^13)) = -6188084046055    -> a=-6188084046055, b=4375636191520
   (matches the top inequality's lower bound a,b exactly)

## Completion criteria
- brute.py reproduces all four examples above.
- solution.py agrees with brute.py on every case brute.py can reach, and
  reproduces the examples.
- solution.py computes sum_{d non-square, 1<=d<100} |I_d(BQA_d(pi,10^13))|.
- Answer verified by a second independent route.
