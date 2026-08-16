# Pattern-finder: the δ≥3 2-connected count sequence is OEIS A006289

## The data (from commands.log, the legitimate corrected G-heart rerun)

The count of **2-connected graphs with minimum degree ≥ 3** on n vertices,
n = 4..8, computed by the corrected ear-decomposition generator with exact
canonical dedup and oracle-verified (a 4/8/16-cycle exists in every one):

```
n=4: 1, n=5: 3, n=6: 19, n=7: 149, n=8: 2581
```

The full corrected n=8 table from commands.log (generation 20.6s, wall 28.3s):

```
n | #2conn | #delta>=3 | #with_2power | verdict
3 | 1  | 0    | 0    | VERIFIED
4 | 3  | 1    | 1    | VERIFIED
5 | 10 | 3    | 3    | VERIFIED
6 | 56 | 19   | 19   | VERIFIED
7 | 468| 149  | 149  | VERIFIED
8 | 7123| 2581| 2581 | VERIFIED
```

The `#2conn` column matches OEIS A002218 (1,3,10,56,468,7123). The
`#delta>=3` column was independently cross-checked by an nx.simple_cycles
detector agreeing 2581/2581 at n=8.

## The finding

`oeis_lookup([1,3,19,149,2581])` returns exactly **A006289**, "Number of
series-reduced 2-connected graphs with n nodes". A series-reduced 2-connected
graph is precisely a 2-connected graph with no degree-2 vertices, i.e. minimum
degree ≥ 3 — the exact class the run's G-heart lemma is about. So:

- The generator's δ≥3 2-connected class matches the catalogue class exactly
  (verified-numerically against A006289, n ≤ 8).
- The next term is A006289's n=9 entry: **84151**.

## Sequence tools

- `analyze_sequence([1,3,19,149,2581])`: not a low-degree polynomial;
  differences 2,16,130,2432 then 14,114,2302; residues all odd (period 1 mod 2);
  leading ratios 3.0, 6.33, 7.84, 17.3 (super-exponential growth, consistent
  with the catalogue).
- `find_linear_recurrence` (orders 1..8): **no** constant-coefficient linear
  recurrence fits. Neither count sequence (A002218, A006289) has an elementary
  closed form in the catalogue; none is extracted here.

## What it means for the run

1. **Validation**: the G-heart verification now runs over exactly the
   catalogue's δ≥3 2-connected class, independent confirmation of generation
   completeness and dedup exactness.
2. **Verification bound / ceiling**: n=8 verified (2581 graphs, all have a
   4/8/16-cycle). Pushing to n=9 would check 84151 graphs, which the current
   hash+V F2 generator could not finish in two timeout attempts (150s and 590s
   both killed). That is a practical ceiling of the generator, not a
   mathematical one — a faster enumerator (e.g. graph6 canonical labels from a
   library, or generative-grammar counting) would settle n=9.
3. No polynomial/LRS structure to exploit in the counts themselves.

## Conjecture / status

- Claim: the count of 2-connected δ≥3 graphs on n vertices equals A006289(n)
  for n=4..8. Verified-numerically (exact catalogue match, n ≤ 8).
- G-heart lemma verified-numerically for the whole class through n=8 (every
  δ≥3 2-connected graph on ≤ 8 vertices has a 4/8/16-cycle), with an
  independent 4/8-cycle detector agreement at n=8.
- NOT asserted beyond n=8; n=9 would falsify the verification bound if a
  δ≥3 graph there lacked a 4/8/16-cycle, but that is uncomputed.
