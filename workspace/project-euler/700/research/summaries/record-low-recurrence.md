<!-- source: https://smsxgz.github.io/post/math/an_elegant_result/ | full text at research/sources/smsxgz-elegant-result-eulercoin-recurrence.full.md; based on method of brob26 (Project Euler 700 thread) -->

# Record-low index recurrence for modular linear sequences

The Eulercoins of Project Euler 700 are the **record lows (prefix minima)** of
`c_n = A n mod M`, where `A = 1504170715041707`, `M = 4503599627370517`.

Since `gcd(A, M) = 1`, the sequence `c_n` (`n >= 1`) is a permutation of
`{1, 2, ..., M-1, 0}` before it repeats (it is a bijection on the residues; 0 occurs at
`n = M`). A term is an Eulercoin iff it is strictly smaller than every earlier term.

Let `n_1 = 1` (first term, value `A`, is the first Eulercoin). For `k >= 1`, define
`n_{k+1} = min{ n : n > n_k, c_n < c_{n_k} }`, i.e. the index of the next Eulercoin.

**Theorem (recurrence).** If `c_{n_{k+1}} > 0`, then

    n_{k+2} = ceil( c_{n_k} / c_{n_{k+1}} ) * n_{k+1} - n_k.

**Proof sketch (smsxgz, after brob26).** Set `alpha = ceil(c_{n_k}/c_{n_{k+1}})`. Then
`A(alpha n_{k+1} - n_k) ≡ alpha c_{n_{k+1}} - c_{n_k} (mod M)`, and
`0 <= alpha c_{n_{k+1}} - c_{n_k} < c_{n_{k+1}}`, so `c_{alpha n_{k+1} - n_k} <
c_{n_{k+1}}`, forcing `n_{k+2} <= alpha n_{k+1} - n_k`. A second argument shows equality.
See the source for the full proof.

## Why it applies and what it reduces the work to

The recurrence gives successive Eulercoin indices/values directly. It is essentially the
Euclidean/continued-fraction descent of `M/A`: each step's `ceil(c_{n_k}/c_{n_{k+1}})`
shrinks the residual, so the number of Eulercoins is `O(log M)`, not `O(M)`. Scanning
`n = 1 .. M` (M ~ 4.5e15) is impossible; the recurrence terminates in a handful of
Euclidean-like steps.

## Worked example check (exact arithmetic)

- `c_1 = A = 1504170715041707` (first Eulercoin, index 1).
- Second Eulercoin = `8912517754604` (given).
- Sum of first two = `1504170715041707 + 8912517754604 = 1513083232796311` — matches the
  statement exactly.

```claim
id: eu700-record-low-recurrence
statement: For the sequence c_n = A*n mod M (gcd(A,M)=1), letting n_1 = 1 and n_{k+1} = min{n > n_k : c_n < c_{n_k}}, the record-low indices satisfy n_{k+2} = ceil(c_{n_k}/c_{n_{k+1}})*n_{k+1} - n_k whenever c_{n_{k+1}} > 0. Hence the Eulercoins of Project Euler 700 can be generated in O(log M) steps rather than scanning to M ~ 4.5e15.
hypotheses: A, M positive integers with A < M and gcd(A,M)=1; residues taken in [0, M); c_{n_{k+1}} > 0 at each applied step.
holds-here: true. A = 1504170715041707 and M = 4503599627370517, gcd = 1, A < M.
status: checked — sourced (smsxgz blog, method of brob26); verified by this run's code/verify_recurrence.py: gcd(A,M)=1, recurrence matches full brute-force scan on small moduli (A=7/M=17, A=3/M=23, A=5/M=13) and on the real pair through n=10^6, reproduces a_1=1504170715041707, a_3=8912517754604, first-two sum 1513083232796311; code/solution.py runs it to termination, giving 102 Eulercoins and sum V=1517926517777556 (see code/out/verify_recurrence.txt, code/out/solution.txt).
bearing: This is the structural fact that makes the problem solveable in O(log M): enumerate record-low indices/values, sum the values.
anchor: research/summaries/record-low-recurrence.md
```
