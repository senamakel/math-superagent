# OEIS A213014 — number of zeros following the initial 1 (counts of the leading {0,2} block's 0-run)

<!-- source: https://oeis.org/A213014 | full text: sources/oeis-A213014-zeros-before-first-term.full.md (small; summary holds the whole document) -->

## What it establishes

**Definition (M. F. Hasler, 2012):** A213014(n) = number of "0"s preceding the
first term > 1 in the n-th row of the Gilbreath array A036261/A036262.

Terms (first ~30): `0,1,0,0,0,0,0,0,6,5,4,3,2,1,0,0,1,0,0,2,1,0,0,0,3,2,1,0,...`

- Hasler's comment states the reduction plainly: **GC would be violated if the
  initial 1 were not always followed by some number (≥0) of 0s and then a 2 as
  the first term > 1.** This is exactly the run's `second-entry-4-kills`
  mechanism stated at the catalogue level: the first term past the zeros must
  be 2, else the leading 1 dies.
- Offset is 1,9 — so this counts zeros *following the initial 1* in rows of the
  array whose row 0 is the primes.
- Robert Israel's Maple and the PARI program both give independent
  recomputation of the sequence (catalogue-internal cross-check).
- Note the "6,5,4,3,2,1,0" and "3,2,1,0" descending runs: these are the
  **erosion progressions** — a stretch of 6 zeros shrinks one zero per row
  (block consumption in the zero-count, exactly the run's step law
  `b_{k+1} = b_k − 1` during erosion). The catalogue data directly exhibits
  the consumption mechanism at zero-count level.

## Bearing / status

**Catalogue source (status: catalogued).** A213014 is the zero-run part of the
leading `{0,2}` block. Together with A036277 (the position of the first term
> 2), it gives Hasler's catalogue reformulation of GC:

> **GC ⟺ A036277(n) > A213014(n) + 2 for all n > 0** (see A036277 comments).

This is the {0,2}-regime statement in pure sequence terms: the first non-{0,2}
value must occur strictly after the zeros-that-follow-the-1 plus 2 positions.
It corroborates the run's reduction and its observed erosion progressions.

```claim
id: oeis-A213014-zero-run-of-block
statement: A213014(n) counts the zeros following the initial 1 in row n of the Gilbreath array; Hasler: GC would be violated if the initial 1 were not always followed by ≥0 zeros and then a 2 as the first term > 1. The sequence shows descending runs 6,5,4,3,2,1,0 — the erosion progression, matching the run's step law b_{k+1}=b_k−1.
hypotheses: primes triangle; the standard Gilbreath array (row 0 = primes).
holds-here: yes — the zero-run of the leading {0,2} block, counted at catalogue level; the descending runs are erosion in action.
status: catalogued (Hasler 2012, OEIS); consistent with the run's proved step law and depth-1000 data.
bearing: an independent catalogue statement of the {0,2}+then-2 mechanism, and the zero-count side of the A036277/A213014 reformulation of GC.
anchor: research/sources/oeis-A213014-zeros-before-first-term.full.md
```