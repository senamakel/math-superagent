# Reduction attack execution note

The requested attack was encoded in `code/refute/attack_reduction_counterexample.py`.
It includes:

- a direct integer moment oracle for the 0-indexed sums;
- exhaustive small parameter checks of `ue0`, including `n=0` and `n=1`;
- exact mechanical-word comparison through `k=80` under four Fibonacci
  approximants;
- a deliberate decimal-exponent mutant search for the smallest witness.

No program-run facility was available in this session, so this note records the
artifact but does not claim its output. Existing captured artifacts independently
record `ue0` checks and small-k indexing checks; the unresolved issue is the
intercept aggregation wiring, not the monoid's composition law.
