# Sinisalo 2003 — on the minimal cycle lengths of the Collatz sequences

<!-- src: M. K. Sinisalo, "On the minimal cycle lengths of the Collatz sequences", preprint, Dept. Math. Sci., Univ. of Oulu, June 2003. Full text: research/sources/sinisalo-2003-minimal-cycle-length.full.md -->

## What the source establishes

The cycle-length bound as a rational-approximation problem, solved via Farey sequences.

**Lemma 1** (the bridge): if a non-trivial cycle of C (n→3n+1 odd, n→n/2 even) has length m = k+n (k odd-steps, n even-steps) and all its members exceed R, then

    ln3/ln2 < n/k ≤ ln(3+1/R)/ln2 .

**Theorem 1**: if the Collatz conjecture is verified up to R, and n/k is the rational with the least possible denominator k in (ln3/ln2, ln(3+1/R)/ln2], then the least possible non-trivial cycle length is n+k.

**Theorem 2**: any non-trivial cycle has length ≥ 1,027,712,276 (at R = 204×2^50 ≈ 2.29×10^17): the 20th convergent 630,138,897/397,573,379 of ln3/ln2 is the first satisfying the interval.

**Note 1**: with the (3x+1)/2 convention the cycle length is the numerator alone, ≥ 630,138,897.

**The table** (rational upper approximations of ln3/ln2, their cycle lengths, and the R needed): convergent 24 gives 217,976,794,617/137,528,045,312 → length 355,504,839,929 at R ≈ 5.10126×10^22; rows continue up to convergent 30 → length 1,114,548,031,663,007 at R ≈ 1.08×10^29. Intermediate rows include length 2,302,268,119,908 at R ≈ 3.80765×10^23 ≈ 2^77.8.

## Relation to the library — a discrepancy to settle, not to paper over

- The number 355,504,839,929 in Barina's line 253 (`barina-cycle-length-355b`) is exactly the convergent-24 row of this table (217,976,794,617 + 137,528,045,312).
- **But** Sinisalo's table attributes that length to R ≈ 5.1×10^22 ≈ 2^75.5, while Barina claims it at the 2^71 ≈ 2.36×10^21 verification limit. Barina's paper confirms the number and the 2^71 anchor, citing the Eliahou-type formula ([12]). Sinisalo's Lemma-1 interval for R = 2^71 has width ≈ 2.0×10^-22; whether convergent 24 is the least denominator inside it, and whether the Eliahou-formula computation (301994a + 17087915b + 85137581c) agrees, is a concrete check for the oracle. The two sources are not obviously consistent, and this run should settle it rather than inherit the number.
- Angeltveit 2026 independently claims: verifying to 2^77 gives length ≥ 2,302,268,119,908 — the Sinisalo-table row at R ≈ 3.8×10^23 ≈ 2^77.8. Same pattern: the claimed R for the convergent is ~2^77.8, marginally above 2^77. Flag for the same oracle check.

## Claims

```claim
id: sinisalo-theorem1
statement: If the Collatz conjecture is verified up to R > 1 and n/k is the rational with least possible denominator k satisfying ln3/ln2 < n/k ≤ ln(3+1/R)/ln2, then the least possible non-trivial cycle length is n+k (Sinisalo 2003, Theorem 1).
hypotheses: verification to R; C-map convention (3x+1 and x/2 both count)
holds-here: yes — the theorem is the explicit form of the cycle-length arm of the Diophantine lever
status: proved in source (preprint; elementary, Farey-sequence proof)
bearing: the exact statement the verification record plugs into; makes barina-cycle-length-355b checkable
anchor: research/summaries/sinisalo-2003-minimal-cycle-length.md
```

```claim
id: sinisalo-1027712276
statement: Any non-trivial cycle of the Collatz map has length at least 1,027,712,276, using R = 204×2^50 ≈ 2.29×10^17 (20th convergent 630,138,897/397,573,379 of ln3/ln2) (Sinisalo 2003, Theorem 2).
hypotheses: verification to 204×2^50 (long superseded)
holds-here: number is history; the method is current
status: proved in source (preprint)
bearing: historical landmark on the cycle-length ladder; superseded by barina-cycle-length-355b at 2^71
anchor: research/summaries/sinisalo-2003-minimal-cycle-length.md
```

```claim
id: sinisalo-convergent-table
statement: The cycle-length ladder by convergent of ln3/ln2: convergent 24 → 355,504,839,929 at R≈5.10126×10^22; 26 → 13,982,847,799,782 at R≈2.7×10^25; 28 → 29,912,458,879,543 at R≈3×10^26; 30 → 1,114,548,031,663,007 at R≈1.08×10^29; intermediate rows include 2,302,268,119,908 at R≈3.80765×10^23 (Sinisalo 2003, table).
hypotheses: R = 1/(2^(n/k) − 3) the bound whose verification forces that cycle length
holds-here: yes — this is the table the verification arm climbs
status: proved in source (computed table)
bearing: cross-check target for barina-cycle-length-355b and angeltveit's 2^77 claim; see the R-discrepancy above
anchor: research/summaries/sinisalo-2003-minimal-cycle-length.md
```
