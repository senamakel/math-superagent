# Brown (MathPages), "Orthomagic Square of Squares", kmath427

[[brown-mathpages-orthomagic-square-of-squares]]

Considers arrangements of nine distinct squares satisfying the **six orthogonal sums** (rows
and columns) only — an "orthomagic square of squares" (OMSOS) — as an intermediate toward the
full diagonal conditions.

## Established claims

- **Common-sum-is-a-square phenomenon.** Most small OMSOS's have a square common sum. Since a
  full MSS must have common sum `3E²` (3× the central square), and a square can't be 3× a
  square, **every OMSOS with a square common sum is instantly excluded** from being fully magic.
- Of the twelve smallest OMSOS's, nine have square common sum (excluded); the other three are
  ruled out individually. Among 91 primitive OMSOS's with common sum < 30000, 56 have square
  sum (excluded) and the remaining 35 non-square cases are **none of the form 3k²**, so none
  can be a full MSS.
- The square-sum OMSOS's form infinite 1-parameter families (one containing `1²`, another
  containing `2²`, …); there are infinite 4-parameter families via Euler's four-square product
  / quaternionic rotation matrices: rows and columns are orthogonal triads, common sum = square
  of the magnitude.

## Implications for this run
- The orthomagic framing is a **different intermediate object** from the run's `(c,u,v)`
  parametrisation (which fixes centre-line sums). The useful fact here is negative: "most
  near-solutions die by the square-sum constraint, and the non-square exceptions are never
  `3k²`" — a heuristic that near the small end, nothing reaches full magic.
- The "common sum square ⇒ excluded" reasoning is the same modular/3-factor argument as
  Morgenstern Thm 4/Zimmermann; no new impossibility content for large entries.

## Does not help
- The exact OMSOS characterisation is open even on this page; it does not provide a reduction
  to the full problem, and the 4-parameter families apply to the orthomagic-with-square-sum
  world rather than to the MSS.
