# Pomerance, "The multiplicative order mod n, on average" (Dartmouth lecture)

Source: https://math.dartmouth.edu/~carlp/ordertalk.pdf · full text: [[pomerance-multiplicative-order-lecture.full]]

## What it establishes

l(n) = l_2(n) = multiplicative order of 2 in (Z/nZ)^×.

- The number of perfect shuffles to return a deck of 2n cards (bottom card
  staying on the bottom, i.e. the out-shuffle) to its initial order is
  l(2n − 1). Proof by numbering cards 0..2n−1, 0 the bottom card; one perfect
  shuffle sends position i to 2i mod 2n−1. This is an independent, explicit
  restatement of DGK Lemma 1.
- Checked values: l(51)=8, l(53)=52, l(49)=21 — so the "54-card deck needs 52
  shuffles" and "50-card deck needs 21 shuffles" facts.
- Basic fact attributed to Gauss and Carmichael: l_a(n) | λ(n), where λ
  (Carmichael) satisfies λ([m,n]) = [λ(m),λ(n)] and λ(p^α)=φ(p^α) for odd p,
  α=1,2; λ(2)=1, λ(4)=2, λ(2^α)=2^{α−2} for α≥3.

## Consequences for this problem

Confirms s(n) = ord_{n−1}(2) and the worked example s(52)=8, s(86)=8 (l(85)).
The λ bound gives ord_{p^a}(2) | φ(p^a) and hence the "divides 60 → m|2^60−1"
finiteness. The statistical part (average order, Arnold's turbulence heuristic)
is context only — irrelevant to an exact computation.

## Does not settle

- The lcm combination (Chappelon) and the exact prime-power orders (Packard).
- The numerical answer.

## Status

Proved in the lecture (the shuffle connection). Hypotheses hold here. Supports
`outshuffle-order-equals-ord` as a second independent source.
