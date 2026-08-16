<!-- source: https://doi.org/10.5281/zenodo.9036 | converted from HTML -->

# On an unsolved question about the Smarandache Square-Partial-Digital Subsequence

Author: Felice Russo (2014, Zenodo v1). Journal article.

## What this source is

A field report (computer-search based) on the **Smarandache Square-Partial-Digital
Subsequence (SSPDS)**: the sequence of square integers n = k^2 that admit a
partition of their decimal digits into two or more contiguous blocks, **each of
which is itself a perfect square**. Example terms: 49, 144, 169, 361, 441, 1225,
1369, ... (root k: 7, 12, 13, 19, 21, 35, 37, ...) — this root subsequence is
OEIS A048653.

Key rules stated by the source:
- the blocks must be squares (1 considered a square);
- blocks equal to **0 are excluded** (0 not treated as a square), so e.g.
  256036 is rejected because its valid partition 256|0|36 contains a 0 block;
- reports W. L. (Widmer) conjectures and a computer search resolving one
  unsolved question; poses new open questions about palindromic and prime
  members.

## Why it is in the library, and how it differs from PE 719

This is an **adjacent-but-distinct** class that a search for PE 719's general
S-number can collide with, because both are "squares whose digit string splits
into contiguous blocks". The condition is *different*:

- **PE 719 / OEIS A104113 / A038206** (the object of this run): the blocks sum
  to the square root r. n = r^2, blocks v_1..v_k (k >= 1), sum = r.
  Example: 8281 = 91^2 with 8+2+81 = 91.
- **SSPDS / A048653** (this source): each block is itself a perfect square.
  No condition on the root or a block-sum. Example: 49 = 7^2 = 4|9 where 4 and 9
  are squares.

The two conditions usually fail for the same n; the classes overlap only
coincidentally (e.g. 441 = 21^2 = 4|4|1: blocks 4,4,1 sum to 9 != 21, and are
squares — so 441 is SSPDS but not an S-number). This source therefore does NOT
bear on T(10^12); it is recorded so a later run does not mistake the two.

This is a field report, not a primary theorem paper; treat its unverified
conjectures as leads only.
