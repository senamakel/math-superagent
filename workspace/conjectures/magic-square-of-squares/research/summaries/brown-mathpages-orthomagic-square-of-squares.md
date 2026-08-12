# Brown, "Orthomagic Square of Squares" (MathPages) — [[brown-mathpages-orthomagic-square-of-squares.full]]

Web essay (Kevin Brown) proposing and analysing a route via "orthomagic" squares — arrays of squares where only the six row/column sums are equal (diagonals ignored).

## Content
- An OMSOS = 3×3 of distinct squares with the 3 row sums and 3 column sums equal.
- **Remarkably, most OMSOSs have a square common sum.** The smallest OMSOS has row/column sum 3249 = 57². Of the twelve smallest, nine have a square common sum.
- Since a fully-magic square of squares would have common sum 3E² (three times the central square), and **a square cannot equal 3 times a nonzero square**, every OMSOS with a square common sum is immediately ruled out as a candidate.
- The exceptional OMSOSs (common sum not a square) must be checked individually; the smallest non-square-sum OMSOS has common sum 5691 = 3·7·271 and all entries are squared primes.
- Suggests that if all OMSOSs had square sums (or were otherwise eliminable) the problem would be solved; but this is not established.

## Implication
The central observation — **a full MSS's magic sum would be 3e², and 3e² is never a square (for e>0)** because 3 is squarefree — is a genuinely useful structural fact. Any row/column-sum-equal array whose common sum is a perfect square cannot be a magic square of squares. This is a clean, exact check usable on generator output. But the OMSOS classification is incomplete, so this alone does not resolve the problem.

**Status:** informal web essay; the 3e²-never-square fact is elementary and exact; the OMSOS claims are asserted.

```claim
id: sum-never-thrice-square
statement: The magic sum of any 3×3 magic square of squares equals 3e² where e² is the central
  entry; since 3 is squarefree, 3e² is never a perfect square for e>0. Therefore any square
  array whose common line-sum is a perfect square cannot be a magic square of squares.
hypotheses: distinct positive squares
holds-here: yes
status: proved (elementary; magic sum = 3×centre)
bearing: an exact sieve fact; OMSOSs with square common sum are instantly excluded
anchor: research/sources/brown-mathpages-orthomagic-square-of-squares.full.md
```
