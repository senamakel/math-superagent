# Step-1/2 artifact audit

Command executed from `/workspace`:

```sh
python code/brute.py
```

Output:

```text
F3= ['001', '010', '100', '101']
Psi(3)= 20302
Psi(10) mod M= 10699667
```

This exactly reproduces both worked examples in `problem.md`. The oracle is explicitly naive and bounded: it constructs successive Fibonacci words, accumulates all contiguous length-k factors until stabilization, and computes exact integer squares. Its worst-case behavior is exponential in the requested k because Fibonacci-word construction and factor storage grow exponentially in the stage index; it was run only at k=3 and k=10 and must not be used at full size.

Audit findings:

- `problem.md` exists and matches the requested definition, examples, modulus, and target.
- `GOAL.md` exists and restates the task faithfully.
- `CONTEXT.md` exists and records the governing Sturmian/mechanical-word theory and the unresolved joint-intercept aggregation gap.
- `code/brute.py` exists and is a suitable small-instance oracle.
- `code/out/brute_oracle_results.md` records the same anchor results plus bounded checks.
- No correction was required to these artifacts. In particular, no full-size brute force was attempted.
