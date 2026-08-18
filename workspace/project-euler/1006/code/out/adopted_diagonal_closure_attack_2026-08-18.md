# Adopted bivariate floor-moment diagonal closure: smallest-case attack

## Verdict

**Refuted in the adopted form.** The proposed state `(count, sum, sumsq)` is not
closed under continuation/concatenation. This is a counterexample to that
fixed-dimensional closure, not to every conceivable richer fixed-dimensional
state. The missing information is boundary/suffix context (equivalently the
joint intercept/diagonal data).

The governing principle is finite-state/monoid closure: equal states must have
equal effects under every continuation. The oracle searches only small binary
words and is explicitly exponential (`oracle_bound=15`); it is not used at full
size.

## Commands and exact outputs

Executed from `/workspace`:

```text
python code/brute.py
python code/refute/run_bivariate_diagonal_oracle.py
python code/refute/run_fib_block_state_counterexample.py
python code/g4_joint_diagnostic.py
```

The naive oracle reproduced the statement anchors:

```text
psi(3)= 20302
psi(10) mod M= 10699667
```

The direct bivariate-diagonal oracle returned:

```text
(1, 2, (2, 1, 1), '01', '10', (3, 1, 1), (3, 11, 101))
```

Thus at `k=1`, `01` and `10` both have summary `(2,1,1)`, but appending the
same `0` gives `010` with `(3,1,1)` and `100` with `(3,11,101)`. This is the
smallest possible witness: length 1 cannot contain two distinct words with a
continuation while length 2 is the first collision found.

The corrected block-state oracle returned:

```text
smallest local summary collision: (2, 3, (2, 11, 101), '010', '101', (3, 11, 101), (3, 21, 201))
```

This is the requested corrected `k=2` witness. Directly:

- `010` has length-2 windows `01,10`, values `1,2`, hence `(2,3,5)`, if
  interpreting the displayed source's `summary` as ordinary binary integers;
- `101` has windows `10,01`, values `2,1`, hence the same summary, while
  appending `0` gives `0100` versus `1010`, whose length-2 window summaries
  differ. The program's exact returned tuples are authoritative for its
  implemented convention: `(2,11,101)` → `(3,11,101)` versus `(3,21,201)`.

For an unambiguous check against the actually executed implementation, the
source computes `int(w[i:i+k])` (base-10 parsing of a binary-looking substring),
so the printed values use that exact convention; the collision property is
still valid: equal three moments before continuation, unequal afterward.

The independent G4 diagnostic output was:

```text
oracle Psi(3) = 20302
oracle Psi(10) mod M = 10699667
existing O(k) evaluator vs mechanical k=1..150: PASS
block-window reproduction k=1..40: PASS
additive summary composition k=1..40: PASS
boundary state requirement: each concatenation split has k-1 crossing windows;
their values depend on suffix/prefix digits, so the tested 3-number summary
does not determine the Fibonacci-block concatenation correction.
Psi(10^18): NOT COMPUTED; no validated fixed-dimensional collapse found.
```

(The diagnostic also printed short-sample order-one recurrence hits for selected
coordinates; those are not a common recurrence proof and do not rescue the
closure.)

## Conclusion and limits

The attack mechanically breaks the adopted three-moment diagonal summary at
smallest cases, including the corrected `k=2` witness. Existing O(k) evaluators
remain mutually checked on the recorded ranges, but no validated fixed-
dimension
joint-intercept/Fibonacci-block closure follows. Therefore no exact
`Psi(10^18)` value is reported. A richer boundary-state proposal would be a new
claim and is not refuted by this finite witness alone.
