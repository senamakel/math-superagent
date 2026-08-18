# G4 joint-collapse diagnostic (2026-08-18)

## Scope and theory

The object is `Psi(k)`, the sum of squared decimal values of the `k+1`
distinct length-`k` factors of the Fibonacci/Sturmian word. The proposed
structural route is a fixed-dimensional Fibonacci-block transducer: Fibonacci
blocks satisfy `Q[n+1] = Q[n] Q[n-1]`, while decimal windows obey the exact
rolling update. Such a route would need a bounded boundary state encoding all
cross-boundary windows; the existing `(count, sum, sumsq)` summary only adds
already-computed windows and does not encode that boundary information.

The diagnostic is bounded. The naive oracle is exponential and is used only
for the statement examples. The remaining checks are linear in tested finite
Fibonacci prefixes. No full-size enumeration or `10^18` run was attempted.

## Executed command

```sh
python code/g4_joint_diagnostic.py
```

Captured verbatim in `code/out/g4_joint_diagnostic.captured.txt`.

## Exact output

```text
oracle Psi(3) = 20302
oracle Psi(10) mod M = 10699667
existing O(k) evaluator vs mechanical k=1..150: PASS
block-window reproduction k=1..40: PASS
additive summary composition k=1..40: PASS
level recurrence sum, k=1, levels=4..11: orders=[1]
level recurrence sum, k=2, levels=4..11: orders=[1]
level recurrence sum, k=3, levels=4..11: orders=[1]
level recurrence sum, k=5, levels=4..11: orders=[1]
level recurrence sum, k=8, levels=4..11: orders=[1]
level recurrence sum, k=13, levels=4..11: orders=[1]
level recurrence sum, k=21, levels=4..11: orders=[1]
level recurrence sum, k=34, levels=4..11: orders=[1]
level recurrence sumsq, k=1, levels=4..11: orders=[1]
level recurrence sumsq, k=2, levels=4..11: orders=[1]
level recurrence sumsq, k=3, levels=4..11: orders=[1]
level recurrence sumsq, k=5, levels=4..11: orders=[1]
level recurrence sumsq, k=8, levels=4..11: orders=[1]
level recurrence sumsq, k=13, levels=4..11: orders=[1]
level recurrence sumsq, k=21, levels=4..11: orders=[1]
level recurrence sumsq, k=34, levels=4..11: orders=[1]
boundary state requirement: each concatenation split has k-1 crossing windows;
their values depend on suffix/prefix digits, so the tested 3-number summary
does not determine the Fibonacci-block concatenation correction.
Psi(10^18): NOT COMPUTED; no validated fixed-dimensional collapse found.
```

## Interpretation

The first two lines reproduce the problem's examples exactly. The existing
O(k) window evaluator agrees with the independent mechanical evaluator through
`k=150`; the doubled-block window construction agrees through `k=40`.
Componentwise summary composition passes as an arithmetic identity, but that is
not the sought closure theorem: it presupposes both child summaries have already
been computed and supplies no rule for computing Fibonacci-block summaries from
predecessor-block summaries.

The small constant-coefficient recurrence probe is deliberately only a
falsification test. It found order-one recurrences on the short, level-indexed
samples for the selected `k`; this does **not** imply a common recurrence in
`k`, nor a fixed-dimensional state recurrence for the required arbitrary
boundary interval. It therefore neither establishes nor refutes the desired
joint collapse.

The decisive unresolved condition remains the boundary correction: a split has
`k-1` crossing windows whose values depend on suffix/prefix digit contexts. No
mechanically validated constant-size state representing those contexts was found.
Accordingly, no honest value of `Psi(10^18) mod 101001001` is reported.
