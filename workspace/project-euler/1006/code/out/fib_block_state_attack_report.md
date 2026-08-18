# Refutation report: fixed-dimensional Fibonacci-block/joint-intercept collapse

## Theory and target

The governing object is the Fibonacci/Sturmian word, with length-k factors
represented by rolling base-10 windows. A proposed fixed-dimensional collapse
would need a finite summary state that is closed under Fibonacci-block
concatenation and retains enough information to account for windows crossing a
block boundary. The existing `directive9_transfer.py` summary is
`(count, sum(V), sum(V^2))`; its composition is componentwise addition.

The standard relevant principle is finite-state/monoid closure: if a summary is
an adequate compositional state, equal states must have equal effects under all
continuations. I attacked that necessary condition, rather than enumerating
answers up to a large bound.

## Hand-smallest counterexample

At window length `k=1`, the strings `01` and `10` have the same summary

`(count, sum, sumsq) = (2, 1, 1)`.

Appending `0` distinguishes them:

- `010`: `(3, 1, 1)`;
- `100`: `(3, 11, 101)`.

Therefore `(count,sum,sumsq)` is not a sufficient closed state. The reason is
exactly the omitted boundary/suffix information: rolling decimal updates are
not additive across concatenation.

This does **not** refute every conceivable fixed-dimensional state encoding;
it refutes the plausible existing summary and the claim that its componentwise
composition supplies the needed Fibonacci renormalisation. Any successful
fixed-dimensional proposal must explicitly encode boundary action, and prove
that this enriched action closes uniformly in `k`.

## Executed oracle

The oracle is `code/refute/fib_block_state_counterexample.py`. Its exact recorded
output is `code/out/fib_block_state_counterexample.txt`. It searched all binary
strings through length 15 (exponential oracle only; `oracle_bound=15`) and found
the first collision at `(k,n)=(1,2)`, namely the witness above. It also checked
Fibonacci-prefix block splits for `k=1..7`; for `k>=2`, naive additive block
composition undercounts by `k-1` cross-boundary windows.

The bounded Fibonacci checks are evidence, not a proof about all blocks. The
length-2 collision is an exact minimal counterexample to the proposed summary
closure, checked directly by decimal window arithmetic.

## Verdict

**refuted (for the existing summary/composition claim).** The current
fixed-dimensional collapse thesis remains unestablished in its stronger form:
the attack found no counterexample to an as-yet-unspecified enriched state, but
it demonstrated that the state currently implemented cannot be that state.
Consequently no exact value of `Psi(10^18)` follows from this route.
