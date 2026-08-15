# Note — exact-integer evaluator of necessary divisibility conditions

Program: `code/cond_driver.py`, importing `code/lib/cond.py` and
`code/scholar_oracle/oracle.py`. Output captured to `code/out/cond.captured.txt`;
independent calibration checks in `code/out/cond_verify.captured.txt`.

All arithmetic is exact-integer (`pow(base, exp, mod)` for modular
exponentiation). No floats anywhere.

## What was computed

**(a) `check_conditions(2,3)` at the known solution `3^2 - 2^3 = 1`:**

| field | value |
| --- | --- |
| is_odd_prime_pair | False (p=2 is even) |
| vp_y (Cassels p\|y) | False — excluded-by-hypothesis |
| vq_x (Cassels q\|x) | False — excluded-by-hypothesis |
| wieferich_1 (q^(p-1) mod p^2) | False — excluded-by-hypothesis |
| wieferich_2 (p^(q-1) mod q^2) | False — excluded-by-hypothesis |

Because `is_odd_prime_pair=False` (p=2 is even), all four conditions are
**excluded-by-hypothesis**, NOT rejections of the known solution. The
conditions only speak about pairs of odd primes; `(2,3)` lies outside their
domain. Cross-check with concrete `x=3, y=2`: with a concrete solution the
Cassels divisibilities genuinely hold there (`q=3 | x=3`, `p=2 | y=2`), so the
known solution satisfies the Cassels content and is not contradicted — only the
odd-prime gate is closed.

**(b) `double_wieferich_pairs(B)`** — odd-prime pairs `p<q`, `p,q<=B`, with
both `q^(p-1)==1 mod p^2` and `p^(q-1)==1 mod q^2`:

- `B=200`: **0** pairs
- `B=500`: **0** pairs

Consistent with the known minimal double-Wieferich pair being `(83, 4871)`
> 500. Verified that the enumerator is not silently broken: the known pair
`(83,4871)` IS detected up to `B=5000` and is the only one there. For a genuine
double-Wieferich odd-prime pair, `check_conditions(83,4871)` returns
`is_odd_prime_pair=True, wieferich_1=True, wieferich_2=True` (calibration
against a real instance of the hypothesis).

**(c) Oracle sanity:** `solutions(10**8) == [(3,2,2,3)]` exactly.
`3^2 - 2^3 = 1` is the only consecutive-perfect-power solution with both sides
`<= 10^8`. (`solutions` enumerates the set of perfect powers as exact integers
and checks consecutive pairs; no floats.)

## Interpretation

The double-Wieferich conditions are necessary for an odd-prime solution
(skeleton `conditional-non-wieferich`: solution -> Cassels p|y,q|x -> double
Wieferich congruences; contrapositive is the conditional theorem). This run
provides the direct, runnable evaluator of that hypothesis. It does not prove
the lemmas; it evaluates the stated congruences exactly. No odd-prime pair up
to 500 satisfies them (apart from the check confirming `(83,4871)` at 5000),
so the condition is far from vacuous and the known solution is correctly
outside it.

```claim
id: cond-evaluator-odd-prime-wieferich
statement: >
  check_conditions(2,3) at the known solution 3^2-2^3=1 reports
  is_odd_prime_pair=False (p=2 even), so the Cassels and double-Wieferich
  conditions are excluded-by-hypothesis and do not reject the known
  solution; with concrete x=3,y=2 the Cassels divisibilities q|x (q=3|3)
  and p|y (p=2|2) genuinely hold. double_wieferich_pairs finds zero
  odd-prime pairs (p<q) with both q^(p-1)==1 mod p^2 and p^(q-1)==1 mod q^2
  for B=200 and B=500, consistent with the known minimal pair (83,4871)>500;
  the enumerator is verified to detect (83,4871) at B=5000 and the
  check_conditions Wieferich flags are True there. The oracle
  solutions(10**8) is exactly [(3,2,2,3)].
hypotheses: >
  p,q exponents of a hypothetical solution; the Wieferich congruences are
  stated only for odd-prime (p,q). Exact integer arithmetic; the search
  evidence (zero pairs <=500, only (83,4871) <=5000) is computational, not
  a proof for all pairs.
holds-here: yes
status: checked
bearing: >
  Provides the direct runnable evaluator of the necessary double-Wieferich
  condition on an odd-prime solution (the hypothesis of the
  conditional-non-wieferich theorem) and confirms the known solution is
  excluded only by the odd-prime hypothesis, not violated. Zero pairs up to
  500 does not imply the theorem is vacuous; the gap remains the descent
  over double-Wieferich pairs such as (83,4871).
anchor: code/out/cond.captured.txt, code/out/cond_verify.captured.txt
```
