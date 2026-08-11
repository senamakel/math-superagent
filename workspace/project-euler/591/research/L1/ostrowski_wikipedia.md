# Ostrowski numeration — Wikipedia (background/setup)

Source: https://en.wikipedia.org/wiki/Ostrowski_numeration (full text read).

## What it establishes

Two classical numeration systems built from the continued fraction of a fixed
irrational `α = [a_0; a_1, a_2, ...]`. Let `q_n` be the convergent denominators,
`q_n = a_n q_{n-1} + q_{n-2}`.

**Integer representation.** Every positive integer `N` is written *uniquely* as
`N = Σ_{k=1}^{n} b_k q_k` with integer coefficients `0 ≤ b_k ≤ a_k` and the
Markovian condition "if `b_k = a_k` then `b_{k-1} = 0`" (no consecutive full
digits).

**Real representation.** Every positive real `x` is written
`x = Σ_{n≥1} b_n β_n` with the same digit bounds and the same Markovian condition;
the base is `β_n = (-1)^{n+1} α_0···α_n` (Gauss-map iterates), satisfying
`β_n = a_n β_{n-1} + β_{n-2}`.

For `α =` golden ratio (all `a_k = 1`) this reduces to Zeckendorf's theorem:
`q_n` are Fibonacci numbers and the condition forbids consecutive 1s.

## Hypotheses / applicability

`α` irrational (guaranteed here: `α = {√d}`, d non-square). The article is
explicitly flagged as citation-light ("needs more citations"), so treat it as a
survey statement, not the primary authority.

## What it implies for this problem

It is **setup/background only**. It fixes the classical Ostrowski α-numeration of
integers and reals. Cabanillas (arXiv:1904.01874) builds a *variant* of exactly
this system that codes integers and reals of `[0,1)` by the same digit sequence —
that variant, with Props 9/10, is what this run actually uses for PE591. The
Wikipedia article contains **no** inhomogeneous best-approximation statement and
therefore does not, by itself, produce a candidate set or the answer.

## Does it contradict memory.md?

No. It agrees with the run's §2.1 description. Minor index-convention difference:
Wikipedia's integer form uses scale `q_k (k≥1)` with `b_1` bounded by `a_1`;
Berthe-Imbert and Cabanillas write `N = Σ b_k q_{k-1}`, `0 ≤ b_1 ≤ a_1 − 1`. Same
system, different shifting of indices.

## Verdict

Helps as context; does not settle anything. Nobody needs to re-read it.
