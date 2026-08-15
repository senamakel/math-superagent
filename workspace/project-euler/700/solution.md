# Solution — Project Euler 700 (Eulercoin)

## Problem
For n = 1, 2, 3, … define
    A = 1504170715041707,  M = 4503599627370517,
    c_n = (A · n) mod M  (least nonnegative residue).
An **Eulercoin** is a term strictly smaller than every previously found
Eulercoin — the running-minimum (record-low) subsequence of (c_n).
Task: sum all Eulercoins.

Worked example: c_1 = A, c_3 = (3A) mod M = 8912517754604, first-two sum =
1513083232796311.

## Governing structural fact
Because gcd(A,M) = 1 (checked: 1), the map n ↦ c_n is a bijection of the
residues 0..M-1 (it is multiplication by a unit mod M). Hence the sequence
(c_n) is a permutation of 0..M-1, and the record lows are a finite strictly
decreasing list ending at the value 0 (achieved exactly at n = M). The
running-minimum sequence is therefore finite.

**Record-low index recurrence (sourced: smsxgz/brob26 method).** If
n_1, n_2, … are the indices of successive record lows, then with
n_1 = 1, n_2 = 3 (the statement's two coins), the next index satisfies

    n_{k+2} = ceil( c_{n_k} / c_{n_{k+1}} ) · n_{k+1} − n_k

and the new coin value is c_{n_{k+2}} = (A · n_{k+2}) mod M.

This is the Euclidean/continued-fraction descent of the rotation: each coin
value strictly decreases, and the ratio c_{n_k}/c_{n_{k+1}} is the
continued-fraction quotient, so the number of coins is O(log M) — 
continued-fraction/Euclidean complexity — **not** O(M). This is the structural
fact that makes the search space unnecessary to visit: a forward scan must go
to n ≈ M ≈ 4.5×10^15, while the recurrence reaches the answer in ~100 steps.

## Method
1. **Oracle (brute force, small).** Forward compute c_n for n up to a few
   million, recording running minima. Reproduces the worked example
   (a_1, a_3, first-two sum 1513083232796311) and the first ~13 coins.
2. **Verify recurrence.** code/verify_recurrence.py checks the recurrence
   against the brute scan on three small pairs run to full termination
   (7,17 → 4 coins sum 12; 3,23 → sum 4; 5,13 → sum 8) and on the real pair
   to n = 10^6 (12 coins, exact match), and reproduces the statement's example.
   All checks PASS.
3. **Full run.** code/solution.py iterates the recurrence in exact Python ints
   from n_1=1, n_2=3 until the coin value reaches 0, sums all coin values.

## Result
- Number of Eulercoins: **102**
- Sum V = **1517926517777556**

## Verification (second independent route)
- code/brute.py reproduces the worked example and the first ~13 coins; its
  running sum at 5M terms (1517925664753868) is already ≈ V with only large-n
  coins remaining, and the recurrence's first 12 coins match the brute prefix
  minima exactly.
- code/check_floor_sum.py re-derives the coin values/sum by an independent
  route (see its output) and asserts equality with V.
- First-two-coin sum matches the statement's 1513083232796311 (asserted inside
  solution.py).
