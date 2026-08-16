# "Regularity versus complexity in the binary representation of 3^n" (David E. Weirich)

Source: arXiv:0902.3257 (2009). Full text: `research/sources/weirich-2009-regularity-complexity-binary-3n.full.md`.

## What it establishes

Studies the grid of binary bits of `3^n` (row n = binary digits of `3^n`). Exhibits **diagonal stripes** in the
bits of `3^{2^n}` — the first of an infinite sequence of such structures — and explains them via a **2-adic
power series**: the apparent disorder in the bits of `3^n` carries hidden 2-adic regularity on the
subsequence `3^{2^n}`. General claim: base-p representation of `k^{p^n}` has analogous features.

Key structural facts: each column (mod `2^a`) has period `2^{a-2}` for `a ≥ 3`; local nestedness (later rows
resemble the initial condition in low-order bits); rows stabilize in low-order bits as n grows.

## Relevance to this run — the symbolic-invariant line

This is the **mirror image** of the run's live attack. The run looks for a transducer/carry statistic on the
`x ↦ 2x` carry that is preserved by `x ↦ 2x` and violated by the digit-`{0,1}` set S (in `Z_3`). This paper
shows the *dual* 2-adic structure: the binary digits of `3^n` (equivalently the bit pattern of `3^{2^n}`)
obey a 2-adic power-series regularity. It is evidence that digit sequences of powers of one base *do* carry
hidden algebraic regularity in the other base's arithmetic — the same phenomenon a symbolic invariant on the
`{2^n}` orbit would exploit. But it is about `3^n` in base 2, not `2^n` in base 3, and does not itself give the
Erdős obstruction.

The period-`2^{a-2}` column regularity is a concrete, quotable fact about how the bits of `3^n` control
low-order 2-adic digits — a candidate structural analogy for what a `2^n mod 3^k` column-period analysis
(`ord_{3^k}(2) = 2·3^{k-1}`) might feed a symbolic invariant.

## Status

Sourced; full text held. Background/structural analogy for the symbolic-invariant program, not a proof tool
by itself.

```claim
id: WEIRICH-3N-BINARY-2ADIC-REGULARITY
statement: The binary bits of 3^n carry hidden 2-adic regularity on the subsequence 3^{2^n} (diagonal stripes, explained by a 2-adic power series). Each column (mod 2^a) has period 2^(a-2) for a ≥ 3; rows stabilize in low-order bits as n grows. Base-p representation of k^{p^n} has analogous features.
hypotheses: 3^n written in base 2; subsequence n = 2^n.
holds-here: no
status: asserted
bearing: the mirror image of this run's attack — proves digit sequences of powers of one base carry hidden algebraic regularity in another base's arithmetic (the phenomenon a symbolic invariant on the {2^n} orbit would exploit) — but it is about 3^n in base 2, not 2^n in base 3, and does not itself give the Erdős obstruction. The period-2^(a-2) column regularity is a structural analogy, not a tool.
anchor: research/summaries/weirich-2009-regularity-complexity-binary-3n.md
```
