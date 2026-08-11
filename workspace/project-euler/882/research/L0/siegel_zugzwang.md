# Siegel, "Coping with cycles" — excerpt summary

> Summary — read this first; full text at `research/L0/siegel_zugzwang.full.md`.

<!-- source: https://library.slmath.org/books/Book56/files/12siegel.pdf | converted from PDF -->

Aaron N. Siegel, "Coping with cycles", *Games of No Chance 3*, MSRI Publ. 56
(2009), 91–123. A primary survey of **partizan loopy combinatorial games**
(Conway/Bach/Norton theory), including **Li's zugzwang games**:

- **Stoppers**: loop games that always terminate in isolation; canonical-form and
  comparison theorems (Conway). The no-skip bit game is a stopper.
- **Sides** `s & t`: a loopy game's behaviour reduces to its onside/offside
  stoppers (Swivel Chair Theorem); pass-move loops are `on = fpass|}`, `off = {|pass}`,
  `over = f0|passg`, `dud = fpass|passg`.
- **Zugzwang games** (Li 1976) = games where moving is disadvantageous; **Li's
  Theorem**: a loopy game is a zugzwang game iff it equals `x & y` for dyadic
  rationals `x ≤ y`. Weak zugzwang games add `on/off/z±over/z±under` sides.
- **Pseudonumbers** = infinite stoppers generalising surreals; `bZ = ω:off`.

Relevance: our skip is exactly the `pass` loop of this theory, and One's forced
1-bit consumption is zugzwang — warrant for the (A,B) stopper/loopy model, but
not a formula for the budgeted skip count S(n). See `research/L1/siegel_zugzwang.md`.
