# The Erdős ternary conjecture on powers of two

## Statement

Write `2^n` in base 3:

```
2^n = sum_{i=0}^{k} a_i 3^i ,   a_i in {0, 1, 2}
```

**Conjecture (Erdős, 1979).** For every integer `n > 8`, the base-3
representation of `2^n` contains at least one digit `2`.

Equivalently: `2^n` is never a sum of *distinct* powers of 3 once `n > 8`.

The conjecture is believed **true**. The objective here is a proof or a
genuine partial result toward one — not a counterexample hunt. A search is
only an instrument for testing a proposed obstruction, never the deliverable.

## The witness set — three exceptions, and they are the whole difficulty

```
n = 0:  2^0 = 1     = 1_3
n = 2:  2^2 = 4     = 11_3
n = 8:  2^8 = 256   = 100111_3
```

These are the reason the conjecture reads `n > 8`, and they are the
falsification oracle for every argument attempted here.

> **Any claimed obstruction must be checked against `n = 0, 2, 8`.** An
> argument that forces a digit `2` for all `n` above some point must not also
> force one at `n = 8`. An argument phrased modulo `3^k` that excludes `n = 8`
> is false, and the check that catches it is three lines long.

This is the specific way a proof of this conjecture goes wrong: a modular
argument that looks like it forbids digit-avoidance in general, but which is
really forbidding it everywhere including where it demonstrably happens.

## Why it is hard, stated honestly

The digits of `2^n` in base 3 behave empirically like independent uniform
draws from `{0,1,2}`. Under that heuristic the chance all of them avoid `2` is
about `(2/3)^k` with `k ≈ n·log2/log3 ≈ 0.63n`, which is summable — so
heuristically only finitely many `n` work, and the three known ones are all of
them.

**That heuristic is not a proof and must never be recorded as one.** It
asserts the absence of a conspiracy without exhibiting any mechanism that
prevents one. Every serious attempt on this problem dies at the same place:
density statements about *all* integers whose ternary expansion avoids `2` say
nothing about the *specific thin sequence* `2^n`, and bridging that gap is the
open problem. An argument that proves "the density of digit-avoiding integers
tends to 0" has proved something true and irrelevant. Record the distinction
in every claim.

This is a small instance of the interaction between base-2 and base-3
structure — the same tension behind **Furstenberg's ×2 ×3 problem** — which is
why no elementary argument is expected to settle it.

## The structure the attack rests on

The multiplicative order of `2` modulo `3^k` is `2·3^(k-1)` for `k ≥ 1`. So:

- `2^n mod 3^k` depends only on `n mod 2·3^(k-1)`;
- the set `S_k` of residues mod `3^k` whose `k` low ternary digits all lie in
  `{0,1}` has exactly `2^k` elements out of `3^k`;
- the admissible `n` are those in `A_k = { n mod 2·3^(k-1) : 2^n mod 3^k ∈ S_k }`.

`A_k` shrinks as `k` grows, and `A_{k+1}` refines `A_k`. **Computing `|A_k|`
as a function of `k` is the first experiment, and it is a sieve on residue
classes, not a search over `n`.** Each surviving class rules out an entire
arithmetic progression of `n` at once.

If `|A_k|` reaches zero for some finite `k` after removing the classes
containing `n = 0, 2, 8`, the conjecture is **proved** for all `n` outside
those classes — that is the shape of a complete proof, and establishing
whether `|A_k| → 0` or stabilises is the central question.

Note the asymmetry that makes this hard: `|S_k|/3^k = (2/3)^k → 0`, but `A_k`
is indexed by `n mod 2·3^(k-1)`, which grows like `3^k` too. The naive count
gives `|A_k| ≈ 2·3^(k-1)·(2/3)^k`, which does **not** tend to zero — it tends
to a constant multiple of `2^k/3`. So the naive heuristic predicts `A_k`
*grows*, and any proof must find structure the counting argument misses.
State this obstruction in `research/ROOT.md` before proposing an approach, and
say how the approach beats it.

## Leads — verify each before relying on it

Not established facts in this workspace. Each needs a primary source and its
own claim block with an explicit status.

- **Narkiewicz (1980)** — the standard reference bounding the number of
  `n ≤ x` with `2^n` digit-`2`-free. Usually quoted as `O(x^c)` with explicit
  `c < 1`. Find the exact statement, the constant, and the method.
- **Verified ranges** — reported numerical bounds vary between sources and
  must be treated as unverified until reproduced here or attributed to a
  primary source. Report the bound this run actually reproduces separately
  from the bound the literature claims.
- **Digit-omission problems generally** — the family "the base-`b` expansion of
  `a^n` omits a fixed digit"; `(a,b) = (2,3)` is the famous case.
- **Automatic sequences and finite automata** — the digit-avoidance condition
  is recognised by a finite automaton in base 3, and `2^n` is not
  3-automatic; whether any decidability machinery (Cobham, Büchi arithmetic)
  applies is worth one honest look and a recorded answer either way.
