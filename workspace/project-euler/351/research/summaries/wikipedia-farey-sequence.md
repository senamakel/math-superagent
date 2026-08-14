# Wikipedia — Farey sequence

Source: https://en.wikipedia.org/wiki/Farey_sequence — full text at
`research/sources/wikipedia-farey-sequence.full.md`
[[wikipedia-farey-sequence.full]]

## What this source establishes

The Farey sequence F_n of order n is the ascending sequence of completely
reduced fractions between 0 and 1 with denominators ≤ n. Its length
|F_n| = 1 + Σ_{k=1..n} φ(k) = 1 + Φ(n) — the same summatory totient as the
orchard's per-sector visible count (A002088 comment: a(n) is the number of
rationals p/q in (0,1] with denominators q ≤ n). Properties: neighbouring
terms satisfy bc − ad = 1; the Farey sequence relates to Ford circles, the
Riemann hypothesis, and the totient sum.

## Hypotheses

n ≥ 1 integer. Holds here.

## What it lets this run do

- A different combinatorial face of Φ(n) (Farey length), corroborating the
  structural role of Φ in counting reduced pairs/fractions; context, not
  load-bearing for the computation.

## What it does not settle

- No summatory values at 10⁸; no algorithm.

## Claims

```claim
id: farey-length-totient
statement: |F_n| = 1 + Φ(n): the Farey sequence of order n has length
1 + Σ_{k=1..n} φ(k).
hypotheses: n ≥ 1 integer.
holds-here: yes (context; consistent with A002088's reduced-fraction count).
status: sourced (Wikipedia Farey sequence).
bearing: corroborates the interpretation of Φ as counting reduced fractions.
anchor: research/summaries/wikipedia-farey-sequence.md
```
