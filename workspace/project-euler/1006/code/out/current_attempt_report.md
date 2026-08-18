# Current attempt report

The unresolved G4 theorem is a fixed-dimensional O(log k) aggregation of all k+1 rotation intercepts for the weighted second moment Psi(k).

## Executed evidence

`python code/g4_joint_diagnostic.py` reproduced:

- Psi(3) = 20302
- Psi(10) mod 101001001 = 10699667
- existing O(k) evaluator agrees with the mechanical evaluator for k=1..150
- doubled Fibonacci-window checks pass for k=1..40

These are checks of the established finite formulas, not a full-size solution.

## Counterexample to the current proposed summary

`python code/refute/fib_block_state_counterexample.py` finds:

- 01 and 10 both have summary (count,sum V,sum V^2)=(2,1,1)
- appending 0 yields 010 with (3,1,1), but 100 with (3,11,101)

Thus componentwise additive summaries omit essential prefix/suffix boundary information. For k>=2, split Fibonacci blocks miss k-1 cross-boundary windows.

## Lean artifact

`code/lean/G4Statement.lean` explicitly states the desired fixed-dimensional theorem and was checked with `lean_check`. The theorem has an intentional `sorry`, so the checker reports a sorry warning; this records the exact open proposition rather than a proof.

## Status

No honest value of Psi(10^18) has been computed. The missing joint-intercept/block-collapse theorem is not settled by larger O(k) runs; scaling would only extend an already-known method and would not answer the structural question.
