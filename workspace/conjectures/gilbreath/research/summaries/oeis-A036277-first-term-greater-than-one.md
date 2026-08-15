# OEIS A036277 — position of first term > 2 in the n-th Gilbreath row

<!-- source: https://oeis.org/A036277 | NO separate .full.md companion (OEIS record is short; this summary IS the complete captured page). Do not search for sources/oeis-A036277-*.full.md — it does not exist. -->

## What it establishes

**Definition (Sloane; extended by David W. Wilson):** A036277(n) = position of
the first term > 2 in row n of the Gilbreath array A036262. Offset 0.

Terms (first ~50): `2,4,9,15,15,26,25,24,23,26,60,99,98,99,98,175,177,177,177,177,292,291,290,741,875,874,873,874,873,872,871,870,869,868,867,2181,...`

Key facts:

- **`a(n) = A000232(n) + 1`** (R. J. Mathar) — so this is the block-length
  sequence the run already uses (`block_profile(k) = A000232(k) − 1`), shifted:
  the position of the first value outside `{0,2}`.
- **Hasler's reformulation, stated in the entry itself:**
  > "Gilbreath's conjecture is equivalent to: A036277(n) > A213014(n) + 2 for
  > all n > 0." (See A036262 for proof.)
  This is the catalogue's complete GC ⟺ statement in terms of the two
  sequences this run now holds: the position of the first >2 value and the
  zero-run following the leading 1.
- The example makes the row-0-vs-row-1 indexing explicit (Hasler's caveat
  about A036261 vs A036262 conventions).
- **Erosion at catalogue level**: notice the runs `...,12,11,10,9,8,7,6,5,4,3,2,1,0,...`
  and `25,24,23,26` — when a fresh `{0,2}` block is long, the first >2
  position advances; within a block the position recedes by 1 per row
  (consumption) until a regeneration resets it (e.g. 99→98→99, 873→872→871→872).

## Bearing / status

**Catalogue source (status: catalogued).** Together with A213014 this is the
OEIS's own statement that GC ⟺ (first non-{0,2} value appears strictly after
the leading-1-following zeros plus 2). The `A036277 = A000232 + 1` identity
links it directly to the run's block-profile quantity.

```claim
id: oeis-A036277-first-term-position
statement: A036277(n) is the position of the first term > 2 in row n of the Gilbreath array, equals A000232(n)+1; Hasler: GC ⟺ A036277(n) > A213014(n) + 2 for all n > 0. The row-to-row movement of A036277 shows the same consumption/regeneration alternation the run computes (block recedes 1 per row during erosion, jumps forward on regeneration).
hypotheses: primes triangle; Gilbreath array A036262.
holds-here: yes — the position-of-first->2 quantity is the leading {0,2} block length plus 2 in catalogue terms.
status: catalogued (Sloane/Wilson/Mathar/Hasler); consistent with this run's block_profile = A000232 − 1 and the depth-1000 block record.
bearing: the other half of Hasler's GC ⟺ reformulation; independent catalogue corroboration of erosion/regen alternation.
anchor: research/summaries/oeis-A036277-first-term-greater-than-one.md (small catalogue record; the summary file is the complete captured page — no .full.md companion exists)
```