# Guy, Unsolved Problems in Number Theory §A10 — "Gilbreath's Conjecture" (CRC MathWorld mirror)

<!-- source: https://sanweb.lib.msu.edu/crcmath/math/math/g/g167.htm (CRC Concise Encyclopedia of Mathematics mirror of the Guy A10 entry); full text: sources/crc-mirror-guy-A10-gilbreath.full.md (small; summary holds the whole document) -->

## What it establishes

This is the **canonical problem-collection entry** — the CRC MathWorld mirror of
R. K. Guy's *Unsolved Problems in Number Theory* 2nd ed. (1994), §A10
(pp. 25–26), which MathWorld, Caldwell, A089582, A036262 and the Muney 2026
paper all cite as the standard reference for the conjecture's statement.

- **Statement (Guy's notation):** Let the difference of successive primes be
  `d_n = p_{n+1} − p_n`, and iterate
  `d_n^k = |d_{n+1}^{k−1} − d_n^{k−1}|` for k > 1.
  "N. L. Gilbreath claimed that d_1^k = 1 for all k" (Guy 1994).
- **Verification bounds (as of the 1994 edition):** verified for `k < 63,419`
  and all primes up to `π(10^13)`.
- This is a *statement-tier* source: it fixes the canonical statement, the A10
  numbering, and the two classic verification bounds. No theorem content beyond
  that — it is the record of the problem's status.

## Bearing / status

**Encyclopedic/problem-collection tier (status: catalogued/asserted).** The
library now holds the canonical A10 reference (via this CRC mirror, which
faithfully reproduces the Guy entry) alongside Odlyzko 1993, Killgrove–Ralston
1959, MathWorld, Caldwell, and the OEIS catalogue. Any citation of "Guy A10"
for the statement now has a local anchor.

```claim
id: guy-A10-canonical-statement
statement: Guy, Unsolved Problems in Number Theory 2nd ed. (1994) §A10, "Gilbreath's Conjecture": with d_n = p_{n+1} − p_n and d_n^k = |d_{n+1}^{k−1} − d_n^{k−1}|, Gilbreath claimed d_1^k = 1 for all k; verified for k < 63,419 and primes up to π(10^13) as of the 2nd edition.
hypotheses: the standard prime-difference iteration.
holds-here: yes — canonical statement, matched by all other library sources.
status: catalogued (CRC MathWorld mirror of the Guy entry, 1999 fetch of the 1994 book text)
bearing: fixes the canonical reference for the problem statement; corroborates the two classic verification bounds.
anchor: research/sources/crc-mirror-guy-A10-gilbreath.full.md
```