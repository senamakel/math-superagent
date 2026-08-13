# The Erdős ternary conjecture on powers of two

## Statement

Write `2^n` in base 3:

```
2^n = sum_{i=0}^{k} a_i 3^i ,   a_i in {0, 1, 2}
```

**Conjecture (Erdős, 1979).** For every integer `n > 8`, the base-3
representation of `2^n` contains at least one digit `2`.

Equivalently: `2^n` is never a sum of distinct powers of 3 once `n > 8`.

## The known exceptions, in full

There are exactly three, and they are the reason the conjecture starts at
`n > 8`:

```
n = 0:  2^0 = 1      = 1_3
n = 2:  2^2 = 4      = 11_3
n = 8:  2^8 = 256    = 100111_3
```

`n = 8` is the largest known. Every one of these must be reproduced by any
program before that program is trusted for anything — they are the witness
set. A search that reports "no n with only digits 0 and 1" and does not
find `n = 0, 2, 8` is broken, not conclusive.

## What is at stake

This is not an isolated curiosity. It is a small, concrete instance of the
question of how the base-2 and base-3 structures of an integer interact, the
same tension behind **Furstenberg's ×2 ×3 problem** and the `3x+1`
literature. The digits of `2^n` in base 3 are expected to behave like
independent uniform draws from `{0,1,2}`, which would make the probability
that none is a `2` about `(2/3)^k` with `k ~ n log2/log3` — summable, so
heuristically only finitely many `n` work and the search space is expected to
be empty above 8. A heuristic is not a proof, and this one explains why the
conjecture is believed and why it is hard: it asserts the absence of a
conspiracy, and there is no known mechanism forcing one not to happen.

## What is already known — verify each before relying on it

These are leads, **not established facts in this workspace**. Every one needs
checking against a primary source before it is cited, and each should become a
claim block with its own status.

- **Narkiewicz (1980)** is the standard reference for a nontrivial upper bound
  on the count of `n <= x` whose ternary expansion of `2^n` omits the digit 2.
  The bound is subexponential in the natural parameter and is usually quoted as
  `O(x^c)` for an explicit `c < 1`. Find the exact statement and constant.
- **Numerical verification** has been pushed far — reported ranges vary and
  should be treated as unverified until reproduced or sourced. State the bound
  this run actually reproduces, separately from the bound the literature
  claims.
- **Related digit-omission problems.** The general family "the base-`b`
  expansion of `a^n` omits a fixed digit" has partial results; the case
  `(a,b) = (2,3)` is the famous one.
- **Connection to `3`-adic and equidistribution methods.** The condition is a
  constraint modulo `3^k` for growing `k`, which is what makes a sieve
  possible: `2^n mod 3^k` is periodic with period `2 * 3^(k-1)`, and the
  digits-in-{0,1} condition cuts the residues down sharply.

## The structure worth exploiting

The multiplicative order of `2` modulo `3^k` is `2 * 3^(k-1)` for `k >= 1`.
So `2^n mod 3^k` depends only on `n mod 2*3^(k-1)`, and the set of admissible
residues — those whose low `k` ternary digits avoid `2` — can be computed
exactly and intersected as `k` grows. This gives a **sieve** rather than a
brute-force search: instead of testing every `n`, test residue classes and
discard whole classes at once. The number of surviving classes as a function
of `k` is itself the quantity Narkiewicz-type bounds control, and computing it
is the natural first experiment.

Brute force over `n` alone is the wrong instrument past small ranges: `2^n`
has about `0.63 n` ternary digits, so testing `n` up to `10^6` means arithmetic
on numbers with hundreds of thousands of digits.
