# MathWorld — Out-Shuffle

Source: https://mathworld.wolfram.com/Out-Shuffle.html · full text: [[mathworld-out-shuffle.full]]

## What it establishes

Encyclopedic definition of the out-shuffle (top half in right hand, cards
interleaved alternately, bottom card stays on the bottom) and the key fact:
the numbers of out-shuffles needed to return a deck of n = 2,4,... to its
original order are 1,2,4,3,6,10,12,4,8,18,6,11,... (OEIS A002326), which is
**simply the multiplicative order of 2 mod (n−1)**. Example: 52 cards needs 8
(ord_51(2)=8).

Also: out-shuffling 2n cards n−2 times when n−1 is prime restores the deck.

## Consequences for this problem

Confirms s(n) = ord_{n−1}(2) for small n and the s(52)=8 example. The A002326
link ties back to the exact order sequence. Secondary confirmation.

## Does not settle

The enumeration over divisors of 2^60−1 and the answer.

## Status

Encyclopedic. Hypotheses hold. Supports `outshuffle-order-equals-ord`.
