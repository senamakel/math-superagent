# Wikipedia — Faro shuffle

Source: https://en.wikipedia.org/wiki/Faro_shuffle · full text: [[wikipedia-faro-shuffle.full]]

## What it establishes

Definitions and context, not new theorems:
- The faro (weave/dovetail) shuffle: deck split into two equal halves,
  interleaved perfectly.
- **Out-shuffle**: top and bottom cards stay in place. **In-shuffle**: top
  card moves to second position.
- Group-theoretic aspects: the out-shuffles on n cards form a cyclic group of
  order equal to the multiplicative order of 2 mod n−1; the faro shuffle is a
  distance-doubling permutation 2i mod (n−1).

## Consequences for this problem

Confirms the identification of the statement's "riffle shuffle" (top and
bottom card preserved) with the out-shuffle, i.e. s(n) = ord_{n−1}(2). It is a
reference/secondary confirmation of the reduction, not an independent primary
source.

## Does not settle

Nothing beyond the reduction; no combinatorics of the enumeration.

## Status

Encyclopedic (asserted, with the proof sketched via the standard result).
Hypotheses hold. Supports `outshuffle-order-equals-ord`.
