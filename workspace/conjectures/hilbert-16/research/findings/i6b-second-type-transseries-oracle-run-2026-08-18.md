# Bounded iterated-log transseries oracle run

## Method

The named theory is truncated Hahn-style transseries algebra plus the generalized derivation–division/Wronskian test. A finite support in monomials `z^a t^b log(t)^c loglog(t)^d` is propagated through four fixed second-type passage expressions. This is a symbolic stress test, not a theorem and not the exact I^1_6b return map.

## Executed guard and ceiling

Command:
`python code/naive_examples_oracle.py > /tmp/naive.txt; python code/i6b_second_type_transseries_oracle.py > /tmp/trans.txt; ...`

The capture is `code/out/i6b_second_type_transseries_oracle.captured.txt`. The naive guard reproduces every worked example in `problem.md`: counts `1,0,0,2,1`, all checks true. Arithmetic is exact (`Fraction` and SymPy); no floating point.

Exact ceiling: four fixed passages; monomial exponents are retained only for `z<=3`, `t<=3`, `log(t)<=2`, `loglog(t)<=1`. The projected Wronskian is computed symbolically in `t`, with `L=log(t)` and `LL=loglog(t)` treated as formal independent symbols. Cost is polynomial in the retained support; this is not a search over candidate dynamics.

## Output and interpretation

The run produced nonzero projected third Wronskian
`W3=-(108*L - 26*LL + 697)*(2*L**2 + L*LL + 3*L + 2*LL)/22050`.
Therefore this bounded fixed toy did **not** find a counterexample to finite ECT closure. This negative result is only within the stated support and chosen coefficients. It does not establish ECT closure, finite cyclicity, or anything about the exact I^1_6b graphic.

The earlier toy capture `code/out/i6b_second_type_toy.captured.txt` did find an algebraic Wronskian degeneracy, but that was a deliberately different toy/boundary specialization. The present run is the requested iterated-log composition attempt and does not reproduce that degeneracy.

Missing for a meaningful attack: machine-readable exact four Dulac maps, their parameter domain, and a certified transseries remainder/ordering. No theorem is claimed; no counterexample to finite ECT closure was found at this ceiling.