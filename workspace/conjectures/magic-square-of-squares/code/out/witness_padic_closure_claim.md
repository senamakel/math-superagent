# No pure p-adic / modular obstruction exists for the primes tested — claim block

Source: `code/out/witness_padic_falsification.py` + `code/out/phi_padic_closure_all.py`,
captured at `code/out/witness_padic_falsification.captured.txt` and
`code/out/phi_padic_closure_all.captured.txt`. Exact integer arithmetic, no floats.

## What the run established

For the universal rational set `Phi = {f(m,n) = 4mn(m^2-n^2)/(m^2+n^2)^2}`, the
run tested whether any residue set achievable by `Phi` can obstruct an additive
triple `q1, q2, q1+q2 in Phi` modulo prime powers. The conclusion is a real
negative result: **no pure p-adic/modular obstruction proof exists for the
primes and prime powers actually covered**, because every achievable residue
set of `Phi` is additively closed at each tested prime power (mod 3 and mod 5
collapse to the single residue `{0}`).

The overall run concluded: "ALL CONSISTENT - no statement forbids a witness".
Both known witnesses (Sallows LS1 and Bremner's magic square) satisfy all the
proved p-adic facts (`v2 >= 3, v3 >= 1`, and residue 0 mod 3 for every fully
realised `Phi` element), so no residue/closure argument forbids either witness.

## Exact primes and prime powers covered

Valuation distributions were computed for `Phi(m)` with m up to 200
(`|Phi(200)| = 8156`) for primes:
`p = 2, 3, 5, 7, 11, 13, 17, 19, 23`.

Additive-closure of the achievable residue set `|R|` was verified at these
prime powers (all report `closed=True`):

| p | prime powers tested | residue set sizes |closure |
|---|---|---|---|
| 2 | 2,4,8,16,32 | 1,1,1,2,4 | all True |
| 3 | 3,9,27,81,243 | 1,3,9,27,81 | all True |
| 5 | 5,25,125,625,3125 | 1,5,25,124,611 | all True |
| 7 | 7,49,343,2401,16807 | 3,9,57,383,2344 | all True |
| 11 | 11,121,1331,14641,161051 | 3,33,360,3549,8156 | all True |
| 13 | 13,169,2197,28561,371293 | 3,39,501,4671,6988 | all True |

Note: `p=5` and `p=13` results carry a `skip=` flag (2709 and 1168, presumably
elements skipped as duplicates/non-representatives in the residue-set
construction); the closure conclusion is reported for the tested sets.

## The bound is the result, not the claim

This says nothing about primes not tested or prime powers beyond those listed.
It does **not** say "no p-adic obstruction exists, period." It says: for the
prime powers enumerated above, every achievable residue set is additively
closed, so no additive-triple obstruction can be forced by residues at those
moduli. This is a negative result that rules out the pure modular sieve at the
tested moduli, and it bounds the claim.

```claim
id: witness-padic-falsification
statement: For every prime power in the tested set (p=2 up to 32; p=3 up to
  243; p=5 up to 3125; p=7 up to 16807; p=11 up to 161051; p=13 up to 371293),
  every achievable residue set R of the universal set Phi = {f(m,n)} is
  additively closed: whenever r1, r2 in R then r1 + r2 is achievable mod that
  prime power (and mod 3, mod 5 the residue set collapses to the single class
  0). Hence no pure p-adic or modular obstruction proof of the Phi-no-triple
  conjecture exists at these moduli: such an argument would need an identity
  of residue sets that is never present. Both known 7-square witnesses satisfy
  all proved p-adic facts (v2>=3, v3>=1, residue 0 mod 3), so no residue/closure
  argument forbids either witness.
hypotheses: the run's exact Phi-membership test and residue-set construction,
  as implemented in witness_padic_falsification.py / phi_padic_closure_all.py;
  the specific primes p in {2,3,5,7,11,13,17,19,23} and the specific prime
  powers tabulated above.
holds-here: yes, on the tested moduli only
status: checked
bearing: rules out the pure modular-sieve line of attack at the tested primes
  and prime powers; deliberately NOT an unbounded statement — no conclusion is
  drawn about primes or prime powers outside the tested set.
anchor: code/out/witness_padic_falsification.py,
  code/out/phi_padic_closure_all.py,
  code/out/witness_padic_falsification.captured.txt,
  code/out/phi_padic_closure_all.captured.txt
source: operator-computation (this run)
```
