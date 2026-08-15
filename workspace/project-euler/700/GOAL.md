# Goal — Project Euler 700 "Eulercoin"

Statute: let

    A = 1504170715041707        (the multiplier)
    M = 4503599627370517        (the modulus, ~4.5e15)

Define the integer sequence (n = 1, 2, 3, …)

    a_n = (A · n)  mod  M

i.e. a_n is the least non-negative residue of A·n modulo M. Because
gcd(A, M) = 1, the map n ↦ a_n is a permutation of the residues {0, …, M−1}.

An **Eulercoin** is an element a_n that is strictly smaller than every
previously found Eulercoin — the running-prefix-minimum (record-low) sequence,
taken in order of occurrence n = 1, 2, 3, …

**Objective / completion criterion:** compute the **sum of all Eulercoins**
(it is finite, since the residues hit the record lows a finite number of times,
ending at 0).

## Worked examples (the test oracle — must all be reproduced by any method)

- a_1 = 1504170715041707 — the first term, and it is the first Eulercoin
  (A < M so no reduction: a_1 = A).
- a_2 = 2·A = 3008341430083414 — still < M, and greater than a_1, so NOT a coin.
- a_3 = (3·A − M) = 8912517754604 — less than a_1, so the second Eulercoin.
- Sum of the first 2 Eulercoins = 1504170715041707 + 8912517754604
  = **1513083232796311**.

## Verified (by code/brute.py, forward scan)

The brute oracle reproduces all four of the above exactly: first coin at n=1
value 1504170715041707, second at n=3 value 8912517754604, sum
1513083232796311. Forward scan of the first 50 terms finds just these two
coins (no further record low before n=50).
