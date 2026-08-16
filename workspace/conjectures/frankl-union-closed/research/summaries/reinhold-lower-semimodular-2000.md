# Frankl's Conjecture is True for Lower Semimodular Lattices

Jürgen Reinhold. _Graphs and Combinatorics_ 16 (2000), 115–116.
doi:10.1007/s003730050008
Note: only abstract obtainable (Springer paywall); full proof not captured.

<!-- source: https://doi.org/10.1007/s003730050008 -->

## What is confirmed (abstract level)

The paper proves: **every finite lower semimodular lattice `L` with `|L| ≥ 2`
contains a join-irreducible element `x` such that at most `|L|/2` elements
`y ∈ L` satisfy `y ≥ x`.** This is the strongest published result for a standard
lattice class (it generalises Abe–Nakano's modular case and is part of the chain
extended by Czédli–Schmidt).

`research/sources/reinhold-lower-semimodular-2000.full.md` holds only the
abstract + Springer metadata; the proof itself is not in this library. The proof
outline (via the Bruhn–Schaudt survey, which reproduces it) constructs an
injection from the principal filter `[a)` to its complement using a lower cover
`b` of `1 = a ∨ b` and the join-irreducible `a ≤ b`.

```claim
id: reinhold-lower-semimodular
answers: lattice-settled-classes
statement: Every finite lower semimodular lattice L with |L| ≥ 2 satisfies
  Frankl's conjecture: some join-irreducible x has |{y: y ≥ x}| ≤ |L|/2.
hypotheses: L finite lower semimodular lattice.
holds-here: true
status: asserted
bearing: strongest settled standard lattice class; proof not in this library
  (only the statement via abstract), so marked asserted not proved.
anchor: Reinhold, Graphs and Combinatorics 16 (2000) 115–116, abstract.
```
