# Solution — Project Euler 493

## Problem
70 balls, 7 colours × 10 each. Draw 20 without replacement uniformly over all
C(70,20) subsets. Compute E[X], X = number of distinct colours present.

## Governing result

**Linearity of expectation (indicator method) + symmetry.** Write
X = Σ_{i=1}^{7} I_i, where I_i = 1 iff colour i appears in the draw.
Then E[X] = Σ_i P(I_i=1) = 7 · P(colour 1 appears), by symmetry.

This is the structural fact that makes the bound irrelevant: instead of any
enumeration over colour subsets or draws, we need a single probability.

## Why it applies / the reduction

A fixed colour is absent iff all 20 drawn balls come from the other 6 colours'
60 balls. Drawing is uniform over C(70,20) subsets, so

  P(absent) = C(60,20) / C(70,20).

Hence

  E[X] = 7 · (1 − C(60,20)/C(70,20)).

## Computation

Fully exact rational arithmetic:

    C(60,20) = 4,191,844,505,805,495
    C(70,20) = 161,884,603,662,657,880

    E = 7 · (1 − 4191844505805495 / 161884603662657880)
      = 763700091 / 112000148
      ≈ 6.818741802019762

Answer to 9 decimal places: **6.818741802**

## Complexity

O(1) arithmetic on ~10^17 integer magnitudes — the cost is constant, entirely
independent of n=20 or N=70. (Contrast: enumerating ball subsets would be
exponential; the closed form sidesteps the search space completely.)

## Verification (two independent routes + statistical check)

1. **solution.py** — the closed form above, exact Fractions.
2. **brute.py route (b)** — fully independent: enumerates the 2^7 = 128 colour
   subsets and, for each |S|=d, counts 20-ball draws whose colour set is
   *exactly* S via inclusion–exclusion
   `Σ_{j=0}^{d} (−1)^{d−j} C(d,j) C(10j,20)`, then
   `E = [Σ_d d·C(7,d)·(exact_count for d)] / C(70,20)`. This uses only colour
   subsets (128 of them), not ball subsets, so it is exact and fast.
   Both yield the identical fraction `763700091/112000148`.
3. **montecarlo.py** — 2,000,000 trials drawing 20 of 70 labelled balls and
   counting distinct colours: mean 6.8185885, standard error 0.000283, which is
   0.54 standard errors from the exact 6.8187418 — consistent.

Known answer cross-checked two independent exact ways plus a simulation.

## Saved files
- /workspace/code/brute.py — independent exact oracle (closed form + colour-subset inclusion-exclusion).
- /workspace/code/solution.py — efficient exact closed-form solution.
- /workspace/code/montecarlo.py — independent statistical verification.
- /workspace/GOAL.md, MEMORY.md — working records.
