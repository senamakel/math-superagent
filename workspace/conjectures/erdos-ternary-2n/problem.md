# The Erdős ternary conjecture on powers of two

## Statement

Write `2^n` in base 3:

```
2^n = sum_{i=0}^{k} a_i 3^i ,   a_i in {0, 1, 2}
```

**Conjecture (Erdős, 1979).** For every integer `n > 8`, the base-3
representation of `2^n` contains at least one digit `2`.

Equivalently: `2^n` is never a sum of *distinct* powers of 3 once `n > 8`.

The mathematical consensus is that the conjecture is **true**. The deliverable
is a proof, a disproof, or a genuine partial result stated exactly. A search is
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

## The directed route for this run: 3-adic dynamics and a symbolic invariant

This run is asked to attack the problem as a **dynamical system on the 3-adic
integers `Z_3`**, and to look for a *symbolic invariant* rather than a larger
computation. Concretely, the three things the run is asked to try, in order:

1. **The modular sieve, as an instrument.** The multiplicative order of `2`
   modulo `3^k` is `2·3^(k-1)` for `k ≥ 1`. So `2^n mod 3^k` depends only on
   `n mod 2·3^(k-1)`; the set `S_k` of residues mod `3^k` whose `k` low ternary
   digits all lie in `{0,1}` has exactly `2^k` elements; and the admissible `n`
   are `A_k = { n mod 2·3^(k-1) : 2^n mod 3^k ∈ S_k }`. Compute `|A_k|` as a
   function of `k`. This is a sieve on residue classes, not a search over `n` —
   each discarded class removes an entire arithmetic progression at once.

2. **Read the sieve as a 3-adic orbit.** `n ↦ 2^n` extends to the closure of
   the orbit of `1` under multiplication by `2` in `Z_3^×`; digit-avoidance is
   membership in the Cantor-like closed set `S ⊂ Z_3` of 3-adic integers whose
   digits lie in `{0,1}`, of Hausdorff dimension `log2/log3 < 1`. The question
   is whether the orbit closure meets `S` in more than the three known points.
   Say precisely what a dimension or measure statement about `S` does **and does
   not** give about which integers lie in it.

3. **The symbolic invariant.** Search for an invariant — a congruence, a
   weight function, a carry/transducer statistic on the base-2 → base-3
   conversion, an automaton-theoretic obstruction — that is preserved by
   `x ↦ 2x` on `Z_3` and that `S` violates. Encode candidate invariants as
   SMT constraints (Z3) over the digit variables `a_i ∈ {0,1}` together with
   the modular constraints on `2^n`, and let the solver refute or exhibit
   solutions for bounded digit length. **An SMT run is evidence for a bounded
   instance and never a proof of the general statement**; report the bound.

## The obstruction this route must beat, stated up front

`|S_k|/3^k = (2/3)^k → 0`, but `A_k` is indexed by `n mod 2·3^(k-1)`, which
grows like `3^k` too. The naive count gives `|A_k| ≈ 2·3^(k-1)·(2/3)^k`, which
does **not** tend to zero — it tends to a constant multiple of `2^k/3`. So the
naive heuristic predicts `A_k` *grows*.

A previous run of this workspace reported having proved `|A_k| = 2^(k-1)` for
all `k` and having computed `A_k` to `k = 26`. **That work is not in this
workspace any more and is recorded here as an unverified lead, not as a fact.**
If it is right, no finite `k` closes the sieve, and step 1 above can never by
itself produce a proof — it is an instrument for steps 2 and 3, and the run
must say how those beat it. Re-establishing `|A_k| = 2^(k-1)` is worth doing
once, cheaply, with its own proof; it is not the deliverable.

State this obstruction in `research/ROOT.md` before proposing an approach, and
say how the approach beats it.

## Leads — verify each before relying on it

Not established facts in this workspace. Each needs a primary source and its
own claim block with an explicit status.

- **Narkiewicz (1980)** — the standard reference bounding the number of
  `n ≤ x` with `2^n` digit-`2`-free. Usually quoted as `O(x^c)` with explicit
  `c < 1`. Find the exact statement, the constant, and the method.
- **Dimitrov–Howe** — reported to show any counterexample has no digit 2 and at
  least some explicit number of digits `1`. Find the exact statement and what it
  leaves open.
- **Verified ranges** — reported numerical bounds vary between sources and
  must be treated as unverified until reproduced here or attributed to a
  primary source. Report the bound this run actually reproduces separately
  from the bound the literature claims.
- **Hausdorff dimension of digit-restricted sets in `Z_3`**, and what is known
  about intersections of such sets with orbit closures of `×2` — this is where
  the ×2 ×3 literature (Furstenberg, and the Hausdorff-dimension results on
  `×2`-invariant sets) touches the problem.
- **Automatic sequences and finite automata** — the digit-avoidance condition
  is recognised by a finite automaton in base 3, and `2^n` is not
  3-automatic; whether any decidability machinery (Cobham, Büchi arithmetic,
  Walnut) applies is worth one honest look and a recorded answer either way.
