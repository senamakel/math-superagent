# Goal

## Problem (Project Euler 493, "70 coloured balls")

70 coloured balls are placed in an urn, 10 for each of the seven rainbow colours.

**Question:** What is the expected number of distinct colours among 20 randomly
picked balls (sampled without replacement, uniformly over all C(70,20) subsets)?

**Answer format:** nine digits after the decimal point (a.bcdefghij).

## Symbols

- N = 70 total balls.
- m = 7 rainbow colours.
- k = 10 balls per colour (so m·k = 70).
- n = 20 balls drawn.
- X = number of distinct colours appearing among the n drawn balls (a random
  variable taking integer values 1..7).
- E[X] = expected value to compute.

## Worked examples in the statement

The statement gives no numeric worked example — it is itself the single
question. Our test oracle is therefore an independent exact brute-force
computation of E[X] (see brute.py), which we check against the closed-form
solution (see solution.py).

## Completion criteria

1. brute.py: naive but obviously-correct exact computation of E[X] for this
   input, run to completion.
2. solution.py: efficient exact-rational closed-form computation of E[X],
   agreeing with brute.py exactly.
3. Final answer reported to 9 decimal places.
4. Verified by a second independent route.
