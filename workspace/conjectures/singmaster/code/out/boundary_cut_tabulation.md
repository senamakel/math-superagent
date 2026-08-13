# Boundary-cut tabulation — witnesses and Fibonacci family, eps = 1/2

**Status: checked (computed this run, exact integer arithmetic for every rep).**

Program: `code/boundary/boundary_cut_table.py`
Capture: `code/out/boundary_cut_tabulation.captured.txt` (EXIT_CODE=0)
Secondary capture (family-boundary-forever): `code/out/boundary_family_always_boundary.captured.txt` (EXIT_CODE=0)

## Statement

Under the run's fixed convention (N(a) counts both mirrors plus the trivial
pair C(a,1)=C(a,a-1)), and the MRSTT boundary cut with eps = 1/2:

    boundary  :  k < exp((log n)^(2/3+eps)) = exp((log n)^(7/6))   (log = natural)
    interior  :  exp((log n)^(7/6)) <= k <= n/2

Every known nontrivial occurrence of the witness set AND of the infinite
Fibonacci family lies in the **MRSTT-open boundary**. Of 27 known nontrivial
left-half reps: **27 BOUNDARY, 0 interior**.

## Witness set (from `code/out/witnesses.json`, each rep verified C(n,k)==a)

| a | reps (n,k) | class |
|---|---|---|
| 120 | (10,3),(16,2) | BOTH BOUNDARY |
| 210 | (10,4),(21,2) | BOTH BOUNDARY |
| 1540 | (22,3),(56,2) | BOTH BOUNDARY |
| 3003 | (14,6),(15,5),(78,2) | ALL BOUNDARY |
| 7140 | (36,3),(120,2) | BOTH BOUNDARY |
| 11628 | (19,5),(153,2) | BOTH BOUNDARY |
| 24310 | (17,8),(221,2) | BOTH BOUNDARY |

## Fibonacci family j=1..6 (C(n+1,m+1)=C(n,m+2), n=F_{2j+2}F_{2j+3}-1, m=F_{2j}F_{2j+3}-1)

Each member contributes two nontrivial left-half reps, both BOUNDARY:

| j | n1 | k1 | n2 | k2 | class |
|---|---|---|---|---|---|
| 1 | 15 | 5 | 14 | 6 | BOUNDARY (a=3003) |
| 2 | 104 | 39 | 103 | 40 | BOUNDARY |
| 3 | 714 | 272 | 713 | 273 | BOUNDARY |
| 4 | 4895 | 1869 | 4894 | 1870 | BOUNDARY |
| 5 | 33552 | 12815 | 33551 | 12816 | BOUNDARY |
| 6 | 229970 | 87840 | 229969 | 87841 | BOUNDARY |

## Structural fact: the family stays boundary forever for eps >= 1/3 (exactly), leaves the boundary for eps < 1/3

k/n -> F_{2j}/F_{2j+2} -> 1/phi^2 ≈ 0.3820 is constant (in the left half).
The cut exponent comparison: boundary iff k < exp((log n)^(2/3+eps)), i.e.
log k < (log n)^(2/3+eps).  Along the family log n ~ c·j and log k ~ c·j, so
the asymptotic verdict is set by comparing the growth exponents:
(log n)^(2/3+eps) vs log n, i.e. (2/3+eps) vs 1:

    eps > 1/3 : cut grows faster than n, cut/n -> +inf, family boundary forever
    eps = 1/3 : cut ~ n, boundary threshold is borderline constant
    eps < 1/3 : cut/n -> 0, family eventually leaves the boundary (becomes interior)

Verified numerically (code/out/boundary_eps_dependence.captured.txt): at
eps=0.5 all j boundary; at eps=0.2 the members are NOT boundary (interior)
from j=6 onward (log cut < log n); at eps=0.1 same.  Under the eps=1/2 value
the task's cut specifies, every family member j=1..12 is exactly boundary
(24/24, code/out/boundary_family_always_boundary.captured.txt), confirming
BACKWARD.md's revised G-boundary-collision-a-finite: for eps >= 1/3 the
infinite Fibonacci family contributes a bounded (<= 2) number of boundary
left-half reps per a forever — consistent with (not a proof of) a uniform C.

**Consequence for G-boundary-uniform-count:** because the family is inside the
object being counted for every eps >= 1/3, any argument proving C must cover
the family, not set it aside as interior.  The two reps per a of the family
are consistent with the witness lower bound C >= 3 (3003 has (78,2),(15,5),
(14,6)).

## What this pins

- The witness set has at most 3 boundary reps for a single a (3003: (78,2),
  (15,5), (14,6)), so the lower bound C >= 3 for G-boundary-uniform-count is
  consistent and not contradicted.
- The MRSTT interior theorem does not cover ANY known high-multiplicity
  occurrence; the entire observed multiplicity concentrates in the small-m
  boundary, the exact open gap.

## Evidence class

Computed, exact: every rep is verified with `math.comb(n,k) == a` before
tabulation; no search is performed (occurrences are the known/catalogued
ones). The cut is real-arithmetic on natural logs (floating point), matching
MRSTT's eps=1/2 n-form classifier. The asymptotic boundary-forever is exact
(log algebra); the j=1..12 scan is the numerical check.

**Caveat / uniformity:** this is a per-occurrence classification on the known
set, NOT a proof of the bound C for all a. It pins C >= 3 from 3003 and shows
the whole known catalogue (including the infinite family) is boundary; it does
not bound the number of boundary reps for arbitrary large a. That is exactly
the open gap G-boundary-uniform-count, which this computation does not close.
