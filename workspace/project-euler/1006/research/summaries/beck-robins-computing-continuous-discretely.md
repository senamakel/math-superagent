# Beck & Robins — Computing the Continuous Discretely

Source: Matthias Beck and Sinai Robins, *Computing the Continuous Discretely:
Integer-Point Enumeration in Polyhedra*, 2nd ed., Springer 2015 (updated PDF
`ccdnew.pdf` from the author's site). Librarian-downloaded this cycle:
`research/sources/beck-robins-computing-continuous-discretely.full.md`
(521 KB). URL recorded in that file:
https://matthbeck.github.io/papers/ccdnew.pdf .

## Why it was added

The run's O(log) primitive for Psi(k) — the universal-Euclidean monoid of
directive 4, evaluated by a Euclidean/floor-sum recursion — previously rested
only on competitive-programming sources (OI-wiki 万能欧几里得, fhq cnblogs,
LOJ138, AtCoder `floor_sum`). This textbook is the academic anchor for the
underlying object: **counting integer lattice points under a line breaks into
floor sums**, and the floor-sum second moment is a Dedekind-sum / reciprocal
sum. It gives the surrounding theory (Ehrhart, Fourier–Dedekind, Dedekind
reciprocity) a citable literature footing.

## What it establishes (relevant to PE1006)

- The integer-point count under the graph y=f(x) is the floor-sum object; the
  interpolation between continuous and discrete volume is measured by
  **Dedekind sums** and their reciprocity laws. This is the same algebra the
  Euclidean recursion of `ueuclid` performs when it subtracts the integral part
  of a/c, b/c at each step.
- Fourier–Dedekind sums give exact (not asymptotic) enumeration of
  lattice points in rational polytopes — the exact-arithmetic ethos of the
  run's modular sum.
- Reciprocal / reciprocity laws for Dedekind-type sums are what justify the
  floor-sum reduction being O(log): each Euclidean step swaps the roles of the
  two arguments rather than shrinking the summation range by exhausting it.

## Relation to the problem

Not the solving method (PE1006's sum carries the geometric weight x^i with
x=10^{-1} mod M and arc-midpoint intercepts, which this book does not treat).
It anchors the *window* in which the run's weighted floor-sum monoid lives and
gives a literature citation for "sum of powers of a floor over a lattice,
evaluated by a Euclidean recursion, is a Dedekind-sum structure" — the
unweighted baseline behind `brown-floor-power-sums-dedekind-2026`. For the
weighted case the run still leans on the OI-wiki/fhq/LOJ138 anchors, but the
structural claim now has a textbook citation.
