<!-- source: https://zenn.dev/yatyou/articles/47831bf5576657?locale=en | converted from HTML; full text at research/sources/floor-sum-zenn-full-derivation.full.md -->

# floor_sum in O(log max(a,m)): full recursive derivation

A complete, self-contained derivation of the AtCoder Library `floor_sum` recursion —
`f(n, m, a, b) = sum_{i=0}^{n-1} floor((a·i + b) / m)` — in O(log max(a, m)) steps.
This is the standard tool for summing the terms of `c_i = A·i mod M` over a range,
which is the designed **independent verification route** for the Project Euler 700
record-low (Eulercoin) sum.

## What it establishes (the recursion, with proof)

Reduce `a`, `b` modulo `m` first: write `a = d_a·m + r_a`, `b = d_b·m + r_b` with
`0 <= r_a, r_b < m`. Then

    f(n, m, a, b) = n(n-1)/2 · d_a  +  n · d_b  +  f(n, m, r_a, r_b)

Now set `k = floor((r_a(n-1) + r_b)/m)` (so the reduced summands take only values
`0..k`). **Change of order of summation:** count how many indices `j` have
`floor((r_a j + r_b)/m) = i`; the boundary is `(m·i - r_b)/r_a <= j`, giving

    f(n, m, r_a, r_b) = k·n  -  sum_{i=1}^{k} ceil((m·i - r_b)/r_a)

Using `floor(x) = -ceil(-x)` and reindexing `i -> k - i` this becomes

    f(n, m, r_a, r_b) = k·n  +  f(k, r_a, m, -m·k + r_b)

which **swaps `m` and `r_a`**, so the recursion is Euclidean and runs in
`O(log max(a, m))`. Base case: when `r_a = 0`, `f(n, m, 0, r_b) = n·d_b`.

## Why it applies here and what it reduces the work to

- `c_i = A·i mod M = A·i - M·floor(A·i/M)`, so any block-sum
  `sum c_i = A·sum_i i - M·floor_sum(n, M, A, 0)`. The floor-sum term is computed in
  `O(log A + log M)`, independent of the block length.
- The independent verification of the Eulercoin total `V = 1517926517777556`
  (102 coins) can sum each gap between consecutive Eulercoin indices this way and
  add the coin values — a genuinely different code path from the
  `record-low-recurrence` (record-low-recurrence.md) that produced the answer.
- Because it is a different derivation, agreement between the two at full size
  constitutes an independent check (rule: verify by a second route).

## Status

The recursion and change-of-order proof are reproduced in full here and are standard
(the AtCoder Library `floor_sum` uses exactly this). This strengthens the library's
`eu700-floor-sum-tool` claim from "asserted" toward "checked" by giving the primary
derivation on disk. The full-size re-derivation of V by this route remains to be
executed by the solver.

```claim
id: eu700-floor-sum-recursion-proof
statement: f(n,m,a,b) = sum_{i=0}^{n-1} floor((a i + b)/m) satisfies, after reducing a,b mod m (a = d_a m + r_a, b = d_b m + r_b, 0 <= r_a,r_b < m), f(n,m,a,b) = n(n-1)/2 d_a + n d_b + f(n,m,r_a,r_b); and with k = floor((r_a(n-1)+r_b)/m), f(n,m,r_a,r_b) = k n + f(k, r_a, m, -m k + r_b), base case r_a = 0 giving f = n d_b. The recursion swaps m and r_a, so it runs in O(log max(a,m)) (Euclidean).
hypotheses: m >= 1, n >= 0, a, b integers; r_a, r_b the non-negative residues.
holds-here: true. m = 4503599627370517, a = 1504170715041707, n can be up to ~4.5e15, all within O(log m).
status: checked as an O(log) summation tool — the recursion was run at full size in code/out/check_floor_sum.txt (floor_sum(M,M,A,0) matches (A-1)(M-1)/2; residue-sum identity M*(M-1)/2; matches direct sum on 4 small cases). code/out/check_floor_sum.txt Route A also reproduced V = 1517926517777556 at full size via value-only Euclidean descent (a distinct code path, though sharing the recurrence's quotient-descent structure). floor_sum was not itself used to re-sum the Eulercoin windows window-by-window; the derivation-independent full check remains the brute forward scan + small-modulus full scans.
bearing: floor_sum is a validated O(log) summation tool available for range sums of c_i = A i mod M; it and Route A give extra (code-path) confidence but are not a mathematically distinct derivation of V.
anchor: research/summaries/floor-sum-zenn-full-derivation.md
```
