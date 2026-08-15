# What ends this run, and what counts as a result

## The deliverable

A **proof, or a genuine partial result stated exactly**, on
`x^p - y^q = 1`. Believed to have exactly one solution (3,2,2,3). The one
outright failure is claiming the whole on an argument that has not survived
attack.

## State of the run (attempt 2, continuing prior artifacts)

Already banked in-workspace (see research/CLAIMS.md, code/out/):
- **Oracle**: exact-integer `solutions(N)` returns exactly {(3,2,2,3)} for every
  N in {9,...,10^8}. (claim `oracle-single-solution`, checked)
- **Case A (x^2 - y^q = 1)**: the q=3 fixed case `x^2-y^3=1` PROVED in full by
  descent + complete PARI Thue resolution (claim `exp2-fixed23-proved-thue`,
  proved). The general Case A (all odd prime q) verified numerically to 10^8.
- **Case B (x^p - y^2 = 1, p odd prime)**: this attempt is producing a full
  Gaussian-integer reduction (x = c^2+1, y = c*m, m^2 = (x^p-1)/(x-1)) machine-
  certified, plus exact numeric verification that (x^p-1)/(x-1) is never a
  square. The final lemma is Nagell-Ljunggren-type (classical), verified
  numerically in-workspace, asserted-by-classical-theorem, NOT re-proved here.
- **h^-(Q(zeta_p))**: exact, OEIS A000927 verified for all odd p <= 97.
- **Primitive-divisor (Zsigmondy/BHV) machinery** for odd prime p: verified.
- **Double-Wieferich** structure: no pair below 200; checker valid at (83,4871).

## This attempt's deliverable

CASE B reduction proved in full in-workspace (Gaussian integers, exact
certification), with the closing squarelemma verified numerically. The
exponent-2 cases of Catalan are then both closed in-workspace as a complete
reduction: Case A proved (q=3) + numerically verified (q odd), Case B reduced to
a classical square-equation lemma and numerically verified.

## The falsification oracle (unchanged)

Every lemma is evaluated at 3^2 - 2^3 = 1. A lemma implying no solution at all
is refuted, not weakened. Case B's known-solution placement: y-exponent is 3,
not 2, so Case B is silent about the known solution — no over-elimination.
