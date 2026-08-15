<!-- source: https://arxiv.org/html/2312.13988 | converted from HTML; full text at research/sources/best-approximants-unifying-survey.full.md -->

# Dajani–Kraaikamp–Sanderson: best approximants unifying survey

Research survey (Math. Comp. 94, 2025) on a unifying theory for metrical results on
regular continued-fraction convergents and mediants, built on Ito's natural extension of
the Farey tent map. Relevant for context:

- Gives the standard characterisation of **best approximants**: `p/q` (in lowest terms)
  is a best approximant of `x` iff any other `d/e` with `|x - d/e| <= |x - p/q|` has
  `e > q`. Every best approximant is either a regular convergent or a mediant.
- Recovers Legendre's best-approximation property for convergents and a Legendre-type
  recognition theorem (a fraction within `1/(2 q^2)` is a convergent).
- "Best approximation of the second kind": `p/q` minimises `|q x - p|` over denominators
  `<= q`; these are exactly the convergents.

## Why it applies here

Confirms the exact identity between convergent denominators and best approximations of
the second kind, which is the formal mechanism connecting the record-low indices of
`(a n) mod m` to the continued fraction of `a/m`. This is survey-level confirmation of
Cornell Theorem 4.14, giving an independent authoritative source for the structural fact
the solution relies on.
