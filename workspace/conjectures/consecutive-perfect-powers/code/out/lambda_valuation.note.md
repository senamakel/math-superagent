# (1-zeta_p)-adic valuation of x - zeta_p — verified

Program: `code/cassels/lambda_valuation.py`. Output: `code/out/lambda_valuation.captured.txt`.

This program sat written and 0-byte-captured (never run); this run executed it
and it **OVERALL: PASS** on both checks.

Method: exact iterative division by `lambda = 1 - zeta_p` in `Z[zeta_p]` in the
basis `{1, zeta, ..., zeta^{p-2}}` (using `1+...+zeta^{p-1}=0`). Each division
step is re-multiplied and checked to round-trip, so the valuation is
self-verifying. All arithmetic exact integers.

Check 1 — **`v_lambda(x - zeta_p) = 1` iff `p | (x-1)`**: PASS over all odd
primes `p <= 61` and all `x` in `1..200` (0 failures). Exemplars:
`p=3,x=1 -> 1` (p|0), `p=3,x=2 -> 0` (p∤1), `p=3,x=4 -> 1` (p|3).

Check 2 — **exact integer `v_p(x^p - 1) = v_p(x-1) + [p | (x-1)]`**: PASS over
the same grid (0 failures). This is the corrected LTE form: the `+1` applies
exactly when `x ≡ 1 (mod p)`, and `p=3,x=2` correctly gives `v_3(7)=0`, not 1.

These are the same identities already recorded as claim
`cassels-valuation-lte-and-cyclotomic` (checked) in `code/out/cassels_valuation.note.md`;
this is an independent, self-round-trip-checking reproduction of the
`(1-zeta_p)`-adic half through concrete ring arithmetic rather than integer LTE.

```claim
id: lambda-valuation-x-zeta-iff-p-divides-x-minus-1
statement: In Z[zeta_p] with lambda = 1 - zeta_p (odd prime p), v_lambda(x - zeta_p)
  equals 1 iff p | (x-1), and equals 0 otherwise, for every integer x. Equivalently
  v_p(x^p - 1) = v_p(x - 1) + [p | (x-1)] exactly (LTE, corrected form).
hypotheses: p odd prime, x integer, exact (1-zeta)-adic-with-roundtrip-check in
  the {1,...,zeta^{p-2}} basis; verified over odd primes p <= 61 and x in 1..200.
holds-here: TRUE — the known solution (3,2,2,3) sits at x=3 where v_3(3^3-1)=2
  = v_3(2)+1=1+1; nothing here claims no solution, so (3,2,2,3) is not excluded.
status: checked (numerical, finite grid p<=61, x<=200; the ring arithmetic is
  exact and roundtrip-checked, but this is not a proof for all p, x)
bearing: pins the local behaviour used by the Cassels p|y / q|x divisibility:
  (x - zeta_p) is divisible by (1-zeta_p) exactly when the equation's
  factorisation x^p - 1 = prod (x - zeta_p^j) concentrates at the ramified prime.
anchor: code/out/lambda_valuation.captured.txt
```
