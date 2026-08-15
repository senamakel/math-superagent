<!-- source: https://math.mit.edu/classes/18.095/2024IAP/L5N.pdf | converted from PDF; full text at research/sources/mit-continued-fraction-notes.full.md -->

# MIT notes: Continued fractions (18.095)

Concise lecture notes on regular continued fractions and Diophantine approximation.
Load-bearing statements:

- A CF expansion of `R` terminates iff `R` is rational (Theorem 1); it is eventually
  periodic iff `R` is a quadratic irrational (Theorem 2).
- **Theorem 4:** if `|R - p/q| <= 1/(2 q^2)`, then `p/q` is one of the convergents of
  `R`. This is the Legendre-type recognition theorem: a good enough rational
  approximation is forced to be a convergent.
- Convergents are the best rational approximations of their denominator size.

## Why it applies here

The record-low indices of `(a n) mod m` are tied to the best-approximation / convergent
structure of `a/m`. Theorem 4's converse characterises which denominators `n` are
"convergents", and the record lows of the modular sequence occur exactly at those
convergents' denominators (up to the small-end behaviour). The number of Eulercoins is
controlled by the Euclidean-algorithm length of `(a, m)`, so it is O(log m), which is the
structural reason a recurrence over the record-low indices is efficient rather than a
scan over `m`.
