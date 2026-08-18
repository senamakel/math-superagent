# I^1_6b slow-divergence/ECT attack

## Theory and target
An extended complete Chebyshev (ECT) system of three functions requires the initial Wronskians, in particular the 3x3 Wronskian, to be nonzero throughout the claimed interval. The adopted route would need to derive such a property for the actual four second-type Dulac passages and the resulting displacement/slow-divergence functions. Existing GMV criteria require their hypotheses (analytic Abelian-integral representation and balance conditions); those are not established for the full I^1_6b graphic.

## Computation
`code/refute/i6b_ect_bounded_search.py` was executed with exact SymPy arithmetic. It tested affine second-type passage surrogates
`D_i = a_i c + b_i d + g_i t + e_i L`, formed `F=D1+D2+D3 D4`, `G=D1 D4-D2 D3`, and the derivation--division Jacobian `J=F_c G_d-F_d G_c`. After specializing `c=d=0`, it checked the exact 3-function Wronskian in `t`.

Range: coefficient tuple `(a,b,g,e)` in `[-2,2]^4`, but the scan stopped at the first five failures; the first tuple already failed, so exactly 1 tuple was tested: `(-2,-2,-2,-2)`. The capture is `code/out/i6b_ect_bounded_search.captured.txt`. The earlier exact toy captures additionally show `W3=0` for a four-passage iterated-log surrogate and exact rank loss at a vanishing parameter `a=0`.

## Verdict
**Bounded failed search against the shortcut, not a refutation of I^1_6b finiteness.** The tested surrogate contains exact Wronskian rank-loss, so “each passage has a suitable Chebyshev property, therefore their composed/summed four-passage family is ECT” is invalid without extra independence and nonvanishing-stratum hypotheses. No actual quadratic vector field, Dulac map, slow-divergence integral, or published I^1_6b normal-form coefficient was encoded; therefore this cannot be promoted to `refuted` for the graphic.

`search-frame`: symbolic affine surrogate space with coefficient box `[-2,2]^4`; this lies outside no published exhaustive regime for the actual I^1_6b graphic, because it is not that dynamical family. The smallest obstruction found is algebraic rank loss, before testing non-uniformity.

## Self-critique
The result would be wrong as a claim about I^1_6b if the surrogate identities were silently identified with the actual Dulac passages. They were not: the report explicitly separates the logical obstruction from the dynamics. The search also did not test the actual slow-divergence strata or uniform parameter estimates. Thus the honest status is bounded/undecided for the adopted route, with the ECT shortcut specifically falsified in the toy class.
