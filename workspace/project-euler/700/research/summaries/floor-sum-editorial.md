<!-- source: https://atcoder.jp/contests/practice2/editorial/579 | converted from HTML; full text at research/sources/floor-sum-editorial.md -->

# Floor sum: the O(log m) Euclidean recursion

Defines `f(n, m, a, b) = sum_{i=0}^{n-1} floor((a i + b)/m)`. After reducing `a, b mod m`
(so `1 <= a < m`, `0 <= b < m`), the key identity is

    y = floor((a n + b)/m),  z = (a n + b) mod m
    f(n, m, a, b) = f(y, a, m, z)

The proof counts, for each level `x`, how many `i` have `floor((a i + b)/m) >= x`, then
applies `y = (a n + b - z)/m`. The recursion swaps `(a, m) -> (a, (a n+b) mod m)`, which
shrinks like the Euclidean algorithm, so it runs in `O(log a + log m)` steps. This is the
standard implementation in the AtCoder Library (`floor_sum`).

## Why it applies here

The Eulercoin recurrence produces the record-low values directly, which is the primary
method. Floor sum is an **independent route** for verification: the sum over a block of
`c_i = a i - m floor(a i / m)` can be written in terms of `floor_sum`, and the record-low
windows between consecutive Eulercoin indices each contribute `floor_sum`-shaped sums.
Because it is a different derivation path, it can be used to cross-check the recurrence
answer at full size.

```claim
id: eu700-floor-sum-tool
statement: The sum of a range of terms c_i = a*i - m*floor(a*i/m) reduces to floor_sum(n,m,a,b) = sum floor((a i + b)/m), which is computable in O(log a + log m) by the Euclidean recursion f(n,m,a,b) = f(floor((a n + b)/m), a, m, (a n + b) mod m) after reducing a,b mod m.
hypotheses: m >= 1; n >= 0; a, b integers; a reduced so 1 <= a < m, 0 <= b < m.
holds-here: true. m = 4503599627370517, a = 1504170715041707.
status: asserted by AtCoder editorial (yosupo) and AtCoder Library reference; O(log m) recursion standard.
bearing: Independent verification route for the record-low sum; also the tool that dominates the range-summation picture of the problem.
anchor: research/summaries/floor-sum-editorial.md
```
