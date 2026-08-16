# Lucas' theorem: generalizations, extensions and applications (1878–2014) — Romeo Meštrović

Source: https://arxiv.org/pdf/1409.3820 (arXiv:1409.3820); full text also at
`research/sources/lucas-theorem-survey-mestrovic.full.md` and
`research/sources/lucas-survey-fulltext.full.md` → [[lucas-survey-fulltext.full]]

## What it establishes

A survey of Lucas' theorem and its descendants. The `p = 2` case governs this problem:

Let `n = Σ n_i 2^i` and `m = Σ m_i 2^i` be binary expansions. Then
`C(n,m) ≡ ∏_i C(n_i, m_i) (mod 2)`, so `C(n,m) mod 2 = 1` **iff every binary digit of
`m` is ≤ the corresponding digit of `n` — i.e. iff `m` is a binary submask of `n`**
(equivalently `m ∧ (¬n) = 0`).

This is precisely the fact the fold matrix uses: `Φ_n[d][j] = C(d, j−(n−1−d)) mod 2`
is the indicator of the down-set `M_d`. Also treats the double-Lucas property,
prime-power generalizations (Wolstenholme), and generalized-binomial analogues.

## Bearing on this problem

Fixes the definitional foundation of `Φ_n` and `M_d`. No number theory is needed
beyond this; the problem explicitly forbids using facts about primes.

## Claim blocks

```claim
id: lucas-submask
statement: C(n,m) mod 2 = 1 iff m is a binary submask of n (every binary digit of m
  is ≤ the corresponding digit of n); equivalently m ∧ (¬n) = 0.
hypotheses: n, m nonnegative integers, m ≤ n
holds-here: yes
status: proved (classical Lucas' theorem, p = 2)
bearing: definitional basis for the fold rows M_d = {o : o submask of d}; must not be
  re-derived.
anchor: research/sources/lucas-theorem-survey-mestrovic.full.md
```

## What it does not settle

Does not address the symmetric-difference multiset, the collapse, or which sets occur.
