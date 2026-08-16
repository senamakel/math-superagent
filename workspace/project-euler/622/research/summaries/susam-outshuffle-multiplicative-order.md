# Susam, "From Out Shuffles to Multiplicative Order"

Source: https://susam.net/from-out-shuffles-to-multiplicative-order.html · full text: [[susam-outshuffle-multiplicative-order.full]]

## What it establishes

A self-contained derivation that the number of out-shuffles to restore an even
deck of size n equals the multiplicative order of 2 mod n−1. Structure:
1. Congruence relation — the out-shuffle position map.
2. Multiplicative order — Case n≥4, split by whether position i is coprime to
   n−1; Case n=2 handled separately.
3. Computing the multiplicative order — the CRT/order machinery.

The conclusion matches DGK Lemma 1: s(n) = ord_{n−1}(2).

## Consequences for this problem

A third independent confirmation of the reduction, with a from-scratch
derivation that does not rely on the group-structure paper. Useful as a
plain-language sanity reference and for the n=2 edge case (which the PE
statement's "positive even n" includes: s(2)=1 since a 2-card deck is unchanged
by an out-shuffle; ord_1(2) is ill-defined, so the reduction is meant for n≥4
or treated as n−1=1 edge).

## Does not settle

- The prime-power/lcm structure and the numerical answer. No new theorem
  beyond the reduction.

## Status

Proved. Hypotheses (out-shuffle, even n) hold here. Supports
`outshuffle-order-equals-ord`.
