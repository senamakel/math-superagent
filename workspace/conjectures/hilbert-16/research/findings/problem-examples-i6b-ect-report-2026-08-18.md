# Worked examples and I^1_6b ECT gate (2026-08-18)

## Executed evidence

`python code/problem_examples_and_i6b_report.py` completed successfully; capture:
`code/out/problem_examples_and_i6b_report.captured.txt`.

The exact radial oracle reproduced every worked example encoded in `problem.md`: `A=1-u` gives 1, the linear centre gives 0, the expanding linear focus gives 0, `A=(1-u)(2-u)` gives 2, and `A=(1-u)^2(2-u)` gives 1 (the double root is not a sign-changing/hyperbolic cycle under this oracle). It used exact SymPy arithmetic and no floating point. This is an oracle consistency check, not a general limit-cycle theorem.

## I^1_6b investigation

The adopted theory is the slow-divergence/ECT strategy: derive Dulac/transition contributions, place the displacement in a finite Chebyshev/ECT function space, then apply a zero theorem. The exact gate tested the inference that separately ECT passage contributions remain ECT after addition. Representatives `(1,x)` and `(-1,-x)` each have Wronskian `1`, but their sum is `(0,0)` with Wronskian `0`. The parameter family `(a,a x)` has Wronskian `a^2`, collapsing at `a=0`.

This is an exact algebraic/logical obstruction, not a counterexample to the actual quadratic dynamics. Prior source audit records that RR's full I^1_6b non-boundary strata require four second-type Dulac maps and a coupled two-equation problem; the held result only handles the boundary limit-periodic set. Huzak's slow-divergence theorem is for DF2a, a different graphic, and GMV's ECT theorem requires verified separated-Hamiltonian/balance hypotheses not supplied for full I^1_6b.

## Exact blocker

No precise finite example for the actual I^1_6b family is available in the artifacts. To proceed one would need: (1) the exact RR-coordinate four second-type maps, (2) a parameter-uniform analytic/quasianalytic remainder class stable under composition, and (3) a stratum-by-stratum zero theorem including vanishing slow-divergence coefficients and the identically-zero stratum. Therefore no full-graphic finite-cyclicity claim is made.

The smooth test also remains decisive: formal asymptotic terms without controlled analytic/quasianalytic remainders do not bound zeros. The lower-bound and slow-fast tests cannot be applied to a bound that has not been derived.
