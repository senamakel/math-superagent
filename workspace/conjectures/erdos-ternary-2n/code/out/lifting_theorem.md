# Theorem: `|A_k| = 2^(k-1)` for every `k`, so the 3-adic sieve never closes

This upgrades `ternary-sieve-count-doubles` from a fact verified to `k = 26`
into a proof for all `k`. Proved by the operator; every step is checked
numerically below, and the argument is short enough to formalise.

## Setup

For `k >= 1` let

```
A_k = { r mod 2*3^(k-1)  :  the low k ternary digits of 2^r mod 3^k lie in {0,1} }
```

This is well defined because the multiplicative order of `2` modulo `3^k` is
exactly `2*3^(k-1)`, so `2^r mod 3^k` depends only on `r mod 2*3^(k-1)`.

`|A_1| = 1`: modulo 3 the powers of 2 are `1, 2`, and only `2^0 = 1` avoids the
digit 2, so `A_1 = {0}`.

## Lemma 1 — the step element

For `k >= 2`,

```
2^(2*3^(k-2)) = 1 + c_k * 3^(k-1)   (mod 3^k),   with 3 not dividing c_k
```

*Proof.* `2` has order `2*3^(k-1)` in `(Z/3^k)*`, so `g = 2^(2*3^(k-2))` has
order `(2*3^(k-1)) / gcd(2*3^(k-1), 2*3^(k-2)) = 3`. The elements of order
dividing 3 in `(Z/3^k)*` are exactly those congruent to `1` mod `3^(k-1)`, and
`g != 1` since its order is 3. Writing `g = 1 + c_k 3^(k-1)`, `c_k` is
therefore nonzero mod 3. ∎

Computed: `c_k = 1` for every `k = 2..15`.

## Lemma 2 — the three lifts share their low digits

A residue `r mod 2*3^(k-2)` has exactly three preimages modulo `2*3^(k-1)`,
namely `r + j*2*3^(k-2)` for `j = 0,1,2`. All three give the **same** value
modulo `3^(k-1)`, because `2*3^(k-2)` is the order of `2` modulo `3^(k-1)`.

So the three lifts of `r` have **identical low `k-1` ternary digits**, and can
differ only in the `k`-th digit — the coefficient of `3^(k-1)`.

## Lemma 3 — the top digits are a permutation of `{0,1,2}`

Let `v = 2^r mod 3^k` and let `d` be its coefficient of `3^(k-1)`. By Lemma 1,

```
2^(r + j*2*3^(k-2)) = v * (1 + c_k 3^(k-1))^j = v * (1 + j c_k 3^(k-1))   (mod 3^k)
                    = v + v j c_k 3^(k-1)                                 (mod 3^k)
```

using `3^(2(k-1)) = 0 mod 3^k` for `k >= 2`. So the `k`-th digit of the `j`-th
lift is

```
d + v j c_k   (mod 3)
```

Now `v` is a power of 2, so `3` does not divide `v`; and `3` does not divide
`c_k` by Lemma 1. Hence `j -> d + v c_k j` is an affine bijection of `Z/3`, and
as `j` runs over `{0,1,2}` the top digit runs over all of `{0,1,2}` exactly
once. ∎

## Theorem

For every `k >= 1`, `|A_k| = 2^(k-1)`.

*Proof.* Induction. `|A_1| = 1 = 2^0`. Let `r in A_{k-1}`, so the low `k-1`
digits of `2^r` avoid 2. By Lemma 2 all three lifts of `r` keep exactly those
low `k-1` digits, so each lift lies in `A_k` if and only if its `k`-th digit is
not 2. By Lemma 3 the three top digits are `0, 1, 2` in some order, so exactly
one lift is killed and exactly **two survive**. Every element of `A_k` reduces
to an element of `A_{k-1}`, so this accounts for all of `A_k`, giving
`|A_k| = 2|A_{k-1}|`. ∎

## What follows

```
|A_k| / (2*3^(k-1)) = (1/2)(2/3)^(k-1)  ->  0     (the density vanishes)
|A_k| = 2^(k-1)                         ->  infinity  (the count diverges)
```

A modular sieve closes only if `A_k` becomes empty at some finite `k`. It never
does — it doubles at every level, unconditionally.

> **No obstruction modulo any power of 3 can prove the Erdős ternary
> conjecture.** Whatever rules out `n > 8` is invisible at every finite 3-adic
> precision.

This is a proof about the *method*, not about the conjecture, and it says the
approach in `METHOD.md` cannot succeed on its own. That is worth more than a
larger `k`: it redirects the run. The surviving routes are the ones that see
something a congruence cannot — Dimitrov–Howe's digit-count constraint
(`DH-1`: any exception has a digit 2 or at least 26 digits equal to 1) and
Lagarias-type density bounds on the orbit itself.

## Verification

- Lemma 1 checked for `k = 2..15`: `c_k = 1`, never divisible by 3.
- Lemmas 2 and 3 checked for `k = 3..13`, 200 random `r` per `k`: the low
  `k-1` digits agreed across all three lifts every time, and the three top
  digits were a permutation of `{0,1,2}` every time. **Zero violations.**
- The count `|A_k| = 2^(k-1)` was independently confirmed by direct sieving to
  `k = 26` (`code/out/sieve_lift.captured.txt`).
- Witnesses: `0, 2, 8` appear in `A_k` at every level, as they must.

```claim
id: ternary-lifting-theorem
statement: Let A_k be the residues r mod 2*3^(k-1) whose low k ternary digits
  of 2^r mod 3^k lie in {0,1}. Then |A_k| = 2^(k-1) for every k >= 1. Proof:
  2^(2*3^(k-2)) has order 3 mod 3^k, hence equals 1 + c*3^(k-1) with 3 not
  dividing c; the three lifts of a residue agree modulo 3^(k-1) so share their
  low k-1 digits; and their k-th digits are d + v*j*c mod 3 for j = 0,1,2,
  which is an affine bijection of Z/3 since 3 divides neither v (a power of 2)
  nor c. So exactly one of the three lifts has top digit 2 and exactly two
  survive, giving |A_k| = 2|A_{k-1}| with |A_1| = 1. Consequently the sieve
  set never empties and no congruence modulo a power of 3 can prove the Erdos
  ternary conjecture at any finite precision.
hypotheses: k >= 1; the order of 2 mod 3^k is 2*3^(k-1)
holds-here: yes, proved unconditionally; every lemma also checked numerically
status: proved
bearing: closes the purely modular route as a proof strategy, unconditionally
  rather than up to a computed bound. Supersedes ternary-sieve-count-doubles,
  which asserted the same count only for k <= 22. Redirects the run to methods
  that see past congruences, namely the Dimitrov-Howe digit-count constraint
  and Lagarias-type density bounds on the orbit
anchor: code/out/lifting_theorem.md; code/out/sieve_lift.captured.txt;
  code/out/sieve_structure.captured.txt
contradicts: none
source: operator-computation
```
