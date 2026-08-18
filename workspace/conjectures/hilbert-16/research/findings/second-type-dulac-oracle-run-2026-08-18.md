# Second-type Dulac / oracle run (2026-08-18)

## Theory and scope

The naive oracle uses the radial normal form `x'=A(r²)x-B(r²)y`, `y'=B(r²)x+A(r²)y`; polar reduction gives `r'=rA(r²)`, so isolated radial cycles are controlled exactly by positive odd-multiplicity roots of `A`. This is only a small oracle, not a solver for H16.2.

The open-graphic investigation uses the generalized derivation–division/Rolle strategy: a two-equation displacement system can be reduced by Jacobians, but an ECT/Wronskian assertion requires nonvanishing Wronskians over the full domain. Second-type Dulac passages at nilpotent/semihyperbolic endpoints may contain compensators and iterated logarithms; therefore ordinary finite power-log closure cannot be assumed. The exact I^1_6b coefficients are not available in machine-readable form, so the executable is explicitly a toy and cannot establish or refute the graphic.

## Executed artifacts and exact outputs

Command:
`python code/naive_examples_oracle.py && python code/i6b_second_type_toy.py && python code/lu_analytic_remainder_probe.py`

Fresh captures:
- `code/out/naive_examples_oracle.captured.txt`
- `code/out/i6b_second_type_toy.captured.txt`
- `code/out/lu_analytic_remainder_probe.captured.txt`

The naive oracle output is exactly:

```text
cubic A=1-u: got=1, expected=1, check=True
linear centre A=0: got=0, expected=0, check=True
linear expanding focus A=1: got=0, expected=0, check=True
two cycles A=(1-u)(2-u): got=2, expected=2, check=True
semi-stable A=(1-u)^2(2-u): got=1, expected=1, check=True
ALL WORKED EXAMPLES PASS
```

The I^1_6b toy computes exact rational expressions and reports `W1=t*(35-36*t)/210`, `W2=-17*t**2/1260`, and `W3=0`, both with symbolic `L=log(t)` retained and at `L=0`. Thus the naive three-function ECT package fails mechanically. This is evidence against the shortcut only; it is not evidence that I^1_6b has infinite cyclicity.

The Lu remainder probe checks vanishing orders 1 through 10 for `R=z^k(1+z)` and then the exact counterprobe `R=z²(1-z²)`, whose roots are `{-1,0,1}`. It therefore refutes the inference “analytic and nonzero remainder implies unique local zero.” It does not test Lu's actual five-parameter displacement remainder.

## Counterexample attack and status

The attempted failure modes were: repeated roots/boundary roots in the radial oracle, the Wronskian degeneracy in the toy, and multiple zeros of an analytic remainder. The oracle's worked cases pass; the toy finds the intended Wronskian obstruction; the remainder probe finds the stronger-inference counterexample. No claim about the actual open graphic is proved. The missing load-bearing lemma remains an exact, parameter-uniform second-type endpoint Dulac expansion for the selected graphic, with a remainder class strong enough for zero counting and an analyticity/quasianalyticity step (smooth test). Slow-fast and lower-bound tests are not applicable to this local toy, and no global bound is claimed.
