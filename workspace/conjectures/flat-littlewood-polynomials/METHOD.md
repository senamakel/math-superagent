Solve by classical analysis on the unit circle — moments, autocorrelations and
extremal problems for trigonometric polynomials — with an exact-arithmetic
oracle underneath every number. The `L^2` bound is free and is a floor, not a
result; the content is a constant-factor gain over it, and that gain has to come
from a quantity sensitive to the coefficients lying in the two-point set
`{-1,+1}` rather than on the whole circle.

The oracle for this problem is a **certified** supremum-norm evaluator — the
maximum of `|P(e^{it})|^2` located by isolating the real roots of its derivative
in exact arithmetic, never by sampling a grid — together with an exact integer
`L^4` norm computed from aperiodic autocorrelations, and an exhaustive minimiser
`m(n)` over sign patterns modulo negation and reversal for as large an `n` as
the compute policy reaches.

Use symbolic_math (sympy/PARI) for the exact root isolation and the moment
identities, sat_solver or CP-SAT for the finite question "is there a sign pattern
of length n with `||P||_4^4 <= B`", and coder for the search over sign patterns.
Every asymptotic claim is checked against the exact table before it is believed.

Kahane's unimodular ultraflat theorem is the standing falsifier: a lemma whose
proof never uses that the coefficients are `±1` rather than unimodular is wrong,
because Kahane's construction contradicts it. State, for every lemma, where the
discreteness enters.
