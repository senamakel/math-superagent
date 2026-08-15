<!-- source: https://pi.math.cornell.edu/~gautam/ContinuedFractions.pdf | converted from PDF; full text at research/sources/cornell-continued-fractions-best-approx.full.md -->

# Cornell notes: Continued fractions and best approximations

Standard encyclopedic treatment of simple (regular) continued fractions and their role in
rational approximation. Key load-bearing statements for this problem:

- Every rational has a finite simple CF expansion; convergents `p_n/q_n` defined by
  `p_n = a_n p_{n-1} + p_{n-2}`, `q_n = a_n q_{n-1} + q_{n-2}` (`p_0=a_0, p_1=a_1 a_0+1;
  q_0=1, q_1=a_1`), with `[a_0; a_1, ..., a_n] = p_n/q_n`.
- **Theorem 4.9 (best approximation):** `p_m/q_m` is the best approximation to `x` among
  all rationals with denominator `<= q_m`.
- **Theorem 4.14:** the convergents of `x` are precisely all best approximations of the
  second kind to `x`. (A fraction `p/q` is a best approximation of the second kind if
  `|q x - p| < |q' x - p'|` for every `q' <= q`, `p/q != p'/q'`.)
- **Theorem 4.15:** the closest lattice points to the line `y = alpha x` are in one-one
  correspondence with the convergents of `alpha`.

## Why it applies here

The Eulercoins are record lows of `c_n = (a n) mod m`. Equivalently, a record low at index
`n` means `a n mod m` is smaller than `a k mod m` for all `k < n`. Writing `a n - m
floor(a n / m) = c_n`, a record low corresponds to a best approximation of the second
kind of `a/m` (the index `n` is a convergent denominator structure). The continued
fraction / Euclidean structure of `a/m` therefore governs *which* indices produce record
lows and guarantees the number of record lows is small (bounded by the CF length, i.e.
O(log m)), not O(m). This is why scanning up to `m ~ 4.5e15` is the wrong method: the
Eulercoins form a short sequence whose indices obey the recurrence in
`record-low-recurrence.md`.
