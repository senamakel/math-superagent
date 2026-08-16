# Summary — Arithmetical subword complexity of automatic sequences (Konieczny–Müllner)

Source: arXiv:2309.03180, *Arithmetical subword complexity of automatic
sequences*, Jakub Konieczny, Clemens Müllner (2023). Full text:
`research/sources/konieczny_mullner_arithmetical_subword_complexity.full.md`.

## What it establishes

**Theorem 2.1 (the decomposition, sharpened).** Every complex-valued `k`-automatic
sequence `a` admits

```
a = a_str + a_uni
```

with:

- `a_uni` **Gowers uniform**: for each `s ≥ 1`, `‖a_uni‖_{U^{s+1}[N]} = O(N^{−c(s)})` for
  some `c(s) > 0`;
- `a_str` **structured**: there is a `K` (a power of `k`), a periodic sequence
  `a_per` with period coprime to `k`, a forward-synchronising and a backward-
  synchronising `K`-automatic sequence, and a map `F` such that
  `a_str(n) = F(a_per(n), a_fs(n), a_bs(n))`.

It also classifies automatic sequences of **maximal arithmetical subword
complexity** (the ones in which every word appears along an arithmetic
progression): an automatic `a` has max arithmetical subword complexity iff there
is an arithmetic progression on which `a` takes every value (Corollary 1.4), and
it gives an asymptotic formula for the arithmetical subword complexity of any
automatic sequence.

## Why it matters for SUPPLY / the reopened question

This is the refined "structured + Gowers-uniform" dichotomy for automatic
sequences that the reopened question must navigate. The key structural
consequence: **every automatic sequence decomposes into a part any finite-order
correlation sees (the structured part) and a part no finite-order correlation
sees (the fully-Gowers-uniform part).** For the fold on automatic inputs, the
sublinear-`ν₂` collapsed inputs fall in the "structure invisible to finite
correlations" side — i.e. a collapse witness can be exactly as Gowers-uniform as
the primes are observed to be, so correlation-order functionals cannot be the
discriminator.

This also matters to the *arithmetic* side: it gives a precise sense in which an
arithmetic input weaker than switch density cannot be a correlation statement
about `h`, because the automatic collapse witnesses make all such correlations
vanish.

```claim
id: km-arithmetical-subword-structure
statement: Every complex-valued k-automatic sequence a admits a = a_str + a_uni where a_uni is Gowers uniform of all orders and a_str = F(a_per, a_fs, a_bs) is built from a periodic (period coprime to k) plus forward/backward synchronising automatic parts. Automatic sequences with maximal arithmetical subword complexity are classified (Cor 1.4).
hypotheses: a is k-automatic, finite alphabet; F a finite map on the product of the parts' value sets.
holds-here: Refines the automatic dichotomy the fold and door-3 live in. Reinforces that finite-order-correlation functionals of h cannot separate primes from a fully-Gowers-uniform collapse witness.
status: sourced (Konieczny–Müllner 2023)
bearing: The automatic structured/uniform dichotomy is the sharpest framing of why correlation-order control of h cannot be the needed weaker input.
anchor: research/sources/konieczny_mullner_arithmetical_subword_complexity.full.md
```

## Caveats

Infinite-sequence asymptotic statements; no quantitative transfer to a single
finite prefix `h[0..n−1]` and its fold weight is supplied.
