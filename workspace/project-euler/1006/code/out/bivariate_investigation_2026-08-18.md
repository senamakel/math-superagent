# Bounded bivariate floor-moment investigation

## Restatement and theory

For `S_0=0`, `S_1=01`, `S_n=S_{n-1}S_{n-2}`, let `F_k` be the distinct binary length-`k` factors and `N(w)` the decimal value of `w`. The target is `Psi(k)=sum_{w in F_k} N(w)^2` modulo `M=101001001`.

The adopted route represents factors by mechanical-word intercepts and telescopes their decimal values into affine floor expressions. The intended named theory is the universal Euclidean / floor-sum moment monoid: Euclidean quotient recursion can evaluate geometric first and second moments of one affine floor sequence in logarithmic time. The unresolved issue is the bivariate product over intercept and digit position: a one-sequence moment theorem does not automatically prove a uniform finite-dimensional closure for all intercept traces and concatenation boundaries.

## Required brute oracle

Command:

```text
python code/brute.py
```

Output included both worked examples exactly:

```text
psi(3)= 20302
psi(10) mod M= 10699667
```

It also emitted the bounded residue table for `k=1..20`; this is an oracle check only, not the full-size method.

## Existing diagnostic

Command:

```text
python code/g4_joint_diagnostic.py
```

Key output:

```text
oracle Psi(3) = 20302
oracle Psi(10) mod M = 10699667
existing O(k) evaluator vs mechanical k=1..150: PASS
block-window reproduction k=1..40: PASS
Psi(10^18): NOT COMPUTED; no validated fixed-dimensional collapse found.
```

The finite evaluator and mechanical formulation therefore agree on the tested range, but this is only an O(k) diagnostic.

## Corrected bounded counterexample oracle

The existing runner `code/refute/run_bivariate_diagonal_oracle.py` has a stale package import (`code` is not a Python package), so I ran its implementation directly:

```text
python code/refute/bivariate_diagonal_oracle.py
```

Exact output:

```text
(2, 3, (2, 3, 5), '010', '101', (3, 3, 5), (3, 5, 9))
```

Interpretation: at `k=2`, the words `010` and `101` have identical aggregate length-2 summary `(count,sum,sumsq)=(2,3,5)`. Appending the same symbol `0` produces `0100` and `1010`; their resulting summaries differ, `(3,3,5)` versus `(3,5,9)`. Thus count/first moment/second moment alone is not a sufficient concatenation boundary state. This refutes the currently adopted low-dimensional aggregate state, not every possible richer fixed-dimensional state.

The separate exact diagonal experiment was run with:

```text
python code/investigate_bivariate_diagonal.py
```

It produced `maxresidual=1` for each `k=1..20`; that particular local-data statistic is too weak to certify closure or nonclosure, so it is evidence of residual boundary data only, not an impossibility proof.

## Conclusion

No structurally justified value of `Psi(10^18)` was computed. The universal-Euclidean one-floor moment primitive is established in the workspace, but the missing joint intercept/boundary-collapse theorem remains unproved. Larger O(k) runs would not settle that gap and were not performed. The full-size answer is therefore honestly withheld.
