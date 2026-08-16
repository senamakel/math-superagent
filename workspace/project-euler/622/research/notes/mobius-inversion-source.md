# Möbius inversion theorem — clean sourceable statement

Fills the sourcing gap for the Möbius-inversion rung (C(k), S(k) in
`research/notes/pe622-sequence-structure.md` and the proposed approach
`mobius-inversion-exponent-lattice`): the TCD notes only *define* the Möbius
function; no source in the library before this stated the inversion theorem
that inverts a divisor sum.

## Statement

**Möbius inversion theorem** (Stanford, crypto.stanford.edu/pbc/notes/
numbertheory/mobius.html — `research/sources/stanford-mobius-inversion.full.md`):

For arithmetic functions F, f over the positive integers,
```
   F(n) = sum_{d|n} f(d)  for all n >= 1
        iff
   f(n) = sum_{d|n} mu(n/d) F(d)  for all n >= 1
```
Equivalently `f(n) = sum_{d|n} mu(d) F(n/d)`, with mu the Möbius function
(defined by `sum_{d|m} mu(d) = [m = 1]`). Holds over any abelian group.

## Why it is the rung

The order-divisibility bijection (ord_m(2) | d  iff  m | 2^d - 1, Conrad
Thm 2.1) turns "m has exact order k" into a Möbius inversion over the divisors
d | k:

- C(k) = #{m : ord_m(2) = k} = sum_{d|k} mu(k/d)·(tau(2^d - 1) - 1)
- S(k) = sum of those m = sum_{d|k} mu(k/d)·(sigma(2^d - 1) - 1)

because the set {m : ord_m(2) | d} = {m : m | 2^d - 1} counts/sums to
tau(2^d - 1) - 1 / sigma(2^d - 1) - 1 (excluding m = 1, which has order 1 and
never has order k >= 2). This is the form `verify_answer.py` machine-checks for
k = 1..60.

## Claim

```claim
id: mobius-inversion-sourceable
statement: For arithmetic functions F, f over positive integers,
  F(n) = sum_{d|n} f(d) for all n  iff  f(n) = sum_{d|n} mu(n/d) F(d) for all n.
  Consequently, with C(k) = #{odd m > 1 : ord_m(2) = k} and
  S(k) = sum of those m,  C(k) = sum_{d|k} mu(k/d)(tau(2^d-1) - 1) and
  S(k) = sum_{d|k} mu(k/d)(sigma(2^d-1) - 1), valid for k >= 1.
hypotheses: f, F arithmetic; f multiplicative iff F multiplicative; the
  specific application needs ord_m(2) | d  iff  m | 2^d - 1 (gcd(2,m)=1, i.e.
  m odd — Conrad Thm 2.1).
holds-here: yes (m = n-1 is odd; order-divisibility bijection holds).
bearing: anchors the Möbius-inversion route (C/S over divisors of k) that
  machine-verifies the whole sequence tree and is proposed as the Lean
  Cited-axiom rung inverting over d | 60.
status: proved
anchor: Stanford pbc course notes, Möbius inversion (crypto.stanford.edu/
  pbc/notes/numbertheory/mobius.html); conjunction with Conrad Thm 2.1 for the
  specific application; multiplication over any abelian group.
```

## Notes

- The same inversion over the divisor lattice of the *exponent* k is the finitary
  instance of Rota's poset Möbius inversion; Mathlib's `Nat.sum_mul_moebius`
  realises the number-theoretic (divisor) form, so the Lean proof should use
  that rather than re-derive it.
- The finiteness that makes the inversion finite: ord_m(2) = k forces m | 2^k-1,
  so {m : ord_m(2) | k} is finite for each k.
