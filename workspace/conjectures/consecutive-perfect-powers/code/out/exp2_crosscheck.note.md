# Independent exact-integer cross-check of the two exponent-2 cases

Program: `code/exp2_crosscheck.py`; captured output: `code/out/exp2_crosscheck.captured.txt`.

## What was checked and how

This is an **independent** verification of the elementary (exponent-2) cases of
Catalan's equation `x^p - y^q = 1`, deliberately on a different code path from
the existing oracle (`code/scholar_oracle/oracle.py`), which enumerates the set
of perfect powers, and from `lib.perfectpow` / `lib.cond`.

The independent path here:
- **root extraction** uses `gmpy2.iroot` (exact integer arbitrary-precision),
  not the integer-Newton `iroot` in `lib.perfectpow`;
- each task **loops the unbounded coordinate on one side** and tests the other
  side for being an exact `k`-th power via `gmpy2.iroot`;
- a **pure-residue modular prefilter** prunes non-powers cheaply. A genuine
  `q`-th power reduces to a `q`-th power residue mod every modulus, so the
  filter (AND of two residue tests, moduli `r_i` prime with `r_i ≡ 1 (mod q)`)
  never rejects a true solution — it only skips values that cannot be powers.
  It is an optimisation only; correctness does not depend on it.

Exact integer arithmetic throughout: no floats, no `math.pow`, no logarithms.

## Results

### Task 1 — `x^p - y^2 = 1`, p odd prime
Iterate `y in [2, 10^7]`; `m = y^2 + 1` must equal `x^p`.

```
solutions (x, p, y): []
count: 0
verdict: AGREE (none found)
runtime: 20.938s
```

### Task 2 — `x^2 - y^q = 1`, q odd prime
Iterate `x in [2, 10^8]`; `m = x^2 - 1` must equal `y^q`.

```
solutions (x, y, q): [(3, 2, 3)]
count: 1
verdict: AGREE (exactly (3,2,3))
runtime: 179.712s
```

Totals: `M = 10^7` for the `x^p - y^2` case, `M = 10^8` for the `x^2 - y^q`
case, combined wall time ~200 s (bounded `timeout 540`).

## Independent-verification status

Same verdicts as the prior independent search `code/exp2_verify.py` (Newton
root path) and the oracle at these boxes. This is a **third** independent route
(`gmpy2.iroot` + residue filter) confirming:
- `x^p - y^2 = 1` (p odd) has **no** solution for `y <= 10^7`;
- `x^2 - y^q = 1` (q odd) has **exactly** `(x,y,q) = (3,2,3)` for `x <= 10^8`.

These are numerical finite-box facts, not proofs.

```claim
id: exp2-independent-crosscheck
statement: For the two exponent-2 cases of x^p - y^q = 1 with the other exponent an odd prime:
  (a) x^p - y^2 = 1 has no solutions for 2 <= y <= 10^7 (p odd prime);
  (b) x^2 - y^q = 1 has exactly the single solution (x,y,q) = (3,2,3) for 2 <= x <= 10^8 (q odd prime).
hypotheses: x,y >= 2; p odd prime in (a), q odd prime in (b); exact integer arithmetic.
holds-here: true (this is exactly the finite box under study).
status: checked
bearing: independent confirmation (gmpy2.iroot + residue filter, a third code path) of the two exponent-2 cases out to the stated M. Numerical finite box, NOT a proof.
anchor: code/out/exp2_crosscheck.captured.txt
```
