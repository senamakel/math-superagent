# Goal

_Replace this with the objective for this problem. `./euler` fetches the
official statement into `problem.md`; this file is what the run is measured
against._

The answer is one number. The run is finished when that number is computed
**and** something says why it is right.

## What counts as finished

- The number, agreeing between an obviously-correct oracle and a fast method,
  on every case the oracle can still reach.
- The identity, recurrence or bound the fast method rests on, stated in
  `code/lean/Lib/` and checked — not the answer restated as itself.
- Every catalogue lookup reproduced by a program that does not read the
  catalogue.

## What does not count

- Agreement between two programs that share a wrong assumption.
- A number whose derivation exists only as a comment.
- `theorem answer : N = N := by rfl`, which the runtime refuses by name.
