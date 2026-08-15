# Beltrán–Ivanisvili–Madrid, "On sharp isoperimetric inequalities on the hypercube" (arXiv:2303.06738)

Source URL: https://arxiv.org/abs/2303.06738
Authors: David Beltrán, Paata Ivanisvili, José Madrid. 2023.

## What this source establishes

A sharp isoperimetric inequality for all A ⊆ {0,1}^n under uniform measure µ:
with h_A(x) = number of neighbours of x outside A (zero outside A), and the
two-sided boundary w_A, the paper proves lower bounds on E[h_A^β] in terms of
µ(A) for β ∈ [1/2,1], sharp (equality for subcubes).

Concrete sharp result: for β = 0.53,

    E[h_A^0.53] ≥ 8·µ(A)·(1−µ(A))·(1 − (2√2/3)µ(A) + (√2/3) − 1/4)

and for µ(A) ≥ 1/2, E[h_A^0.53] ≥ 2µ(A)(1−µ(A))·(something). It refines the
Kahn–Park partitioning results and yields Talagrand-type inequalities.

## Why it is here

This is the modern sharpest edge/isoperimetric inequality on the cube, and it
still bounds **E[h_A^β]** — an *average over vertices* of an outer boundary
count. Even at its sharpest it is an expectation, so it cannot by itself bound
max internal degree. For |S| = 2^{n-1}+1 (µ = 1/2 + 1/2^n) it gives a lower
bound on average outer boundary but says nothing about a single vertex's
internal degree. This is direct, recent evidence for problem.md's obstruction.

## Claim block

```claim
id: beltran-ivanisvili-madrid-sharp-avg-boundary
statement: For all A ⊆ {0,1}^n, E[h_A^β] has a sharp lower bound in terms of
  µ(A) for β ≥ 1/2 (e.g. β=0.53 case), minimised by subcubes; the bound is on
  an average vertex outer-boundary quantity.
hypotheses: uniform measure; h_A(x) = outer neighbours.
holds-here: holds but is of the wrong type — average outer boundary, not max
  internal degree. At µ = 1/2+1/2^n it lower-bounds mean outer degree, from
  which no lower bound on max internal degree D(S) follows.
status: asserted-by-source.
bearing: strongest known cube isoperimetric inequality is still an average; the
  sqrt(n) target (if the run's own oracle suggests it) cannot come from an
  average bound, consistent with problem.md.
anchor: beltran-ivanisvili-madrid-2023
```
