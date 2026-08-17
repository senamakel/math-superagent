# PE1006 — mechanical-word slope correction (numerically verified)

**Finding.** The literal steering-directive slope `F(n-1)/F(n)` is WRONG for
the mechanical-word construction: the words it produces contain the block
`11`, which never occurs in the Fibonacci word. The correct rational slope is
the continued-fraction convergent to `1/phi^2 = (3-sqrt5)/2`, namely

    a = fib(n) / fib(n+2)

(Mathlib's `Nat.fib`, so `fib 0 = 0, fib 1 = 1`; the slopes used in tests are
2/5, 3/8, 5/13, 8/21, 13/34, 21/55, ... — these are the convergents below
1/phi^2.)

**Intercepts.** The k+1 points are `x_m = frac(-m*a)`, `m = 0..k`
(equivalently `x_m = -m*a` mod 1). For each midpoint/intercept:

    digit_j(x_m) = floor(x_m + (j+1)*a) - floor(x_m + j*a),  j = 0..k-1.

(Arithmetic in ℚ / exact floor, no floating point.)

**Verified claim.** For k = 1..100 with any `n` satisfying `fib(n+2) > k`,
the set of the k+1 mechanical words equals the set of length-k contiguous
factors of the infinite Fibonacci word; and that factor set has cardinal
k+1. (k=40 earlier "failed" only because the brute prefix bound was too
short — with a longer prefix all k up to 100 match at the stated hypothesis.)

**Infinite word digit.** The 0-based digit at position t of the infinite
Fibonacci word (OEIS A003849, word 0100101001001...) is

    digit(t) = floor((t+2)*alpha) - floor((t+1)*alpha),
    alpha = 1/phi^2 = (3 - sqrt5)/2.

This is the characteristic/mechanical (Sturmian) word of slope 1/phi^2.

The positional indexing of the mechanical words differs from the factor
occurrence positions by a shift; what matters (and what Ψ sums over) is the
**set** identity, which holds exactly.

Verification programs: `/tmp/mech3.py` .. `/tmp/mech6.py` (slope search) and
`/tmp/bridge.py` (infinite-word digits & set equality).
