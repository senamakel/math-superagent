# A364972 — bases where the zero-count never equals the index (d=0 companion)

**Source:** https://oeis.org/A364972 (OEIS entry; b-file at https://oeis.org/A364972/b364972.txt, full text on disk: `research/sources/oeis-A364972-zeros-bases.full.md`). Authors Marton & Khovanova, Aug 14 2023; links to arXiv:2305.10357 and to the supporting code (colab / github gregory-marton/vhs).

**Definition.** Bases b ≥ 2 in which the number of zeros needed to write out the numbers from 1 through k never equals k for any k. I.e. bases where **no fixed point exists for the digit 0**: there is no k with f_0(k, b) = k.

**Terms (first 62, from the b-file).** 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 17, 18, 19, 20, 21, 22, 23, 25, 27, 30, 32, 35, 37, 38, 39, 40, 41, 43, 45, 48, 49, 53, 54, 57, 58, 59, 63, 65, 67, 68, 69, 71, 72, 73, 74, 75, 76, 77, 79, 80, 83, 85, 88, 89, 90, 93, 94, 95, 96, 98, 100. (So base 10 ∈ A364972: the d=0 equality f_0(k,10)=k has no solution — consistent with Khovanova–Marton Theorem 8.1, on disk: a=(0) is not well-defined in base 10.)

**Example given.** 11 and 13 are *not* in the sequence: for k = 3152738985031, exactly that many zeros are needed to write 1..k in base 11 (and similarly 3950024143546664 for base 13).

## What it establishes for this run

- **Closes the last named object in the open request `identify-sticker-numbers-eeda`**: A364972 is the bases-without-zero-fixed-point companion to A226238 (largest d=1 fixed point) inside the same Khovanova–Marton paper. The request is already answered by `G2-solution-bound` (the paper, Prop 9.1, and the d·10^10 bound); having A364972 on disk completes the request's named-sequence inventory.
- **Zero-digit boundary**: PE156 only asks d ∈ {1..9}. d=0 has no solutions in base 10 (A364972 says 10 is a term; Theorem 8.1 of the paper proves it). So the problem's restriction to nonzero digits is not a convenience — the d=0 equation genuinely has no solution, which is why s(d) is only defined for d=1..9. This matches the problem note "for every digit d ≠ 0, 0 is the first solution".

## Does not settle

- Nothing about d ∈ {1..9} fixed points, which are governed by Prop 9.1 (x ≤ d·10^10) and the per-digit OEIS sequences A014778/A101639–A101641/A130427–A130431. This entry is a boundary fact, not a search bound.

## Hypothesis note for the claims ledger

The claim `oeis-per-digit-counts` (A130432 = per-digit counts [84,14,36,48,5,72,49,344,9]) and this entry's "10 ∈ A364972" agree with the Khovanova–Marton Table 2/Theorem 8.1 read from `research/sources/archive-labeling-*` on disk. No new claim block is added here: A364972 is catalogue context, and the mathematical content it reflects (d=0 unsolvable in base 10) is already the paper's Theorem 8.1.