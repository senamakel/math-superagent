# I^1_6b four-second-type Dulac toy

## Source/formula availability

The held Roussarie--Rousseau source states that some I^1_6b blown-up limit
periodic sets require four second-type Dulac maps and a two-equation system in
`(r1,rho1,r2,rho2)`, with `r_i rho_i = nu_i` (source:
`research/sources/rousseau-roussarie-center-graphics-nilpotent.full.md`, lines
60--75). Its Theorem 2.3 gives the second-type normal-form shape, including the
compensator `omega(z,0)=-log(z)` (lines 221--249), but the exact I^1_6b passage
coefficients are not available in a directly machine-readable form here.

## Toy and method

`code/i6b_second_type_toy.py` models four passages by exact expressions in
`t=-log(v)`, parameters `c,d`, and `L=log(t)`. It forms two residuals `F,G`,
the derivation--division Jacobian `J=F_c G_d-F_d G_c`, and the Wronskians of
`F,G,J` after `c=d=0`. This is the generalized Rolle/derivation--division
route, while the ECT test asks for nonzero Wronskians.

## Result

The capture `code/out/i6b_second_type_toy.captured.txt` reports
`W3 = 0` identically, including the exact boundary specialization `L=0`.
Thus this deliberately naive three-function ECT package fails. This supports
the warning that iterated-log composition cannot be treated as an automatic
finite-rank ECT family. It does **not** refute finite cyclicity of I^1_6b:
the toy is not the source's exact transition system, and no theorem transfers
its zero Wronskian to the quadratic graphic.

Three tests: (1) smooth test: the toy retains explicit logarithmic analytic
structure, but does not prove the needed quasianalytic control; (2) lower-bound
test: irrelevant to this local zero-count toy; (3) slow-fast test: `t` is the
blow-up/slow-divergence scale, but no singular perturbation bound is claimed.
