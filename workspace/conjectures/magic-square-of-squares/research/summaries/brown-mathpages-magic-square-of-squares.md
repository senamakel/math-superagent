# Brown, "Magic Square of Squares" (MathPages) — [[brown-mathpages-magic-square-of-squares.full]]

Web essay (Kevin Brown, MathPages) deriving algebra of 3×3 magic squares of squares. Not a refereed journal; treat the proposition as a self-contained argument, `asserted` here since unpublished.

## Content
Derives the standard structure: lines through centre are APs; centre × 3 = magic sum; with centre E, every magic square is parameterised by E, m, n (same grid as c,u,v). Then for a candidate square of squares, symmetric-pair products express e⁴ as a sum of two squares in four distinct ways — the roots of the four "other" squares being n, m, n+m, n−m. Consequence:
> **Proposition 1.** Any square whose elements satisfy the central sums (two diagonals, centre row, centre column) and whose central number is expressible as a sum of two squares in **no more than four** distinct ways will *not* satisfy the four outer row/column sums.

The proof: with 2e² a sum of two squares in only four ways (minimal to make the centre lines), the four pairs of opposite terms are forced, and exhaustive case analysis of their arrangement in the outer rows/columns shows none can sum to the magic constant.

## Implication (important for the run)
The argument only covers central numbers expressible as a sum of two squares in exactly/at most four ways. It does **not** rule out magic squares of squares whose central root has ≥3 distinct 4k+1 prime factors (which gives more than four partitions). Key corollary: **the root of the central number of any magic square of squares would have to be the product of more than two distinct primes of the form 4k+1.** This is a genuine structural restriction consistent with Bremner's 7-square witness (centre 425=5·17, two 4k+1 primes → exactly its four-way partitions, hence not a full square).

**Status:** the argument is a proof-by-exhaustive-cases on a web page, self-contained. Not verified here. It is a partial result for the "exactly four ways" subcase only.

```claim
id: brown-central-four-ways
statement: If a 3×3 array of distinct squares has equal sums on the four lines through the
  centre, and the central number is a sum of two squares in no more than four distinct ways,
  then the four outer rows and columns cannot all have the magic sum. Hence the root of the
  central number of any full magic square of squares must be the product of strictly more
  than two distinct 4k+1 primes.
hypotheses: distinct squares; central sum-of-two-squares count ≤ 4
holds-here: partial (only the ≤4-way case; the general case remains open)
status: asserted (self-contained web argument, not reproduced here)
bearing: gives a clean subcase theorem: any full MSS must have a central root with ≥3
  distinct 4k+1 prime factors (i.e. ≥5 four-way partitions); consistent with the 7-square
  witnesses whose centres have only two 4k+1 primes
anchor: research/sources/brown-mathpages-magic-square-of-squares.full.md
```
