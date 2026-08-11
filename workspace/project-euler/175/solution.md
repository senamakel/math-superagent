# Solution to Project Euler 175

## Problem

Define `f(0) = 1`. For `n >= 1`, `f(n)` is the number of ways to write `n` as
a sum of powers of 2 in which no power of 2 occurs more than twice (each
`2^k` used 0, 1, or 2 times) — the "hyperbinary representations".

Worked examples (test oracle):
- `f(10) = 5` (the five listed decompositions).
- The smallest `n` with `f(n)/f(n-1) = 13/17` is `n = 241`, whose binary
  expansion `11110001` has SBE (runs, MSB first) `4,3,1`.

Target: SBE of the smallest `n` with `f(n)/f(n-1) = 123456789/987654321`.

## Governing theory

`f` counts hyperbinary representations, i.e. `f(n) = a(n+1)` where `a` is
Stern's diatomic sequence (OEIS A002487). Calkin & Wilf ("Recounting the
rationals", Amer. Math. Monthly 107 (2000) 360–363) prove:

    b(0) = 1,  b(2n+1) = b(n),  b(2n+2) = b(n) + b(n+1)

and that the ratios of consecutive terms enumerate each positive rational
exactly once (the Calkin–Wilf tree).

In the PE175 form (with `f(n)=b(n+1)`), the recurrences derived and verified
by `brute.py` are:

    f(2n)   = f(n) + f(n-1)
    f(2n+1) = f(n)
    f(2n-1) = f(n-1)

Let `r_n = f(n)/f(n-1)`. From these recurrences, with `n = 2m` or `n = 2m+1`:

    r_{2m}   = f(2m)/f(2m-1)      = (f(m)+f(m-1))/f(m-1)  = r_m + 1
    r_{2m+1} = f(2m+1)/f(2m)      = f(m)/(f(m)+f(m-1))    = r_m/(r_m+1)

with root `r_1 = f(1)/f(0) = 1/1`. This is exactly the Calkin–Wilf tree,
rooted at `1/1`. Appending a binary `0` bit applies `r -> r+1`; appending a
binary `1` bit applies `r -> r/(r+1)`. Since the Calkin–Wilf tree lists every
positive rational exactly once, each fraction `p/q` corresponds to a unique
integer `n`, whose binary representation is recovered by the Euclidean
inverse ("peel"):

    p > q : LSB 0, previous pair (p-q, q)
    p < q : LSB 1, previous pair (p, q-p)
    p == q: stop (n = 1)

The inverse cost is one step per output bit — O(|binary n|), never growing
with the value of `n` itself. This is the correct method: it walks the
rational-number tree, not the integer line.

## Matrix / run model (independent second route)

Represent the same recurrences with state vector `v = [f(m), f(m-1)]^T`,
root `v = [1,1]` (f(1)=1, f(0)=1). Appending a `0` bit multiplies by
`M0 = [[1,1],[0,1]]`; appending a `1` bit multiplies by `M1 = [[1,0],[1,1]]`.
Both are unipotent (`I +` nilpotent), so a whole run of `k` identical bits is
applied in O(1):

    M0^k: v -> [a + k*b, b]
    M1^k: v -> [a, k*a + b]

This lets an entire SBE run be consumed directly, which is the second,
independent derivation used to verify the final answer.

## Worked example reproduced (both methods)

`solution.py` peel(13,17): bits LSB-first `[1,0,0,0,1,1,1]` -> binary
`"1"+"1110001" = "11110001"`, SBE `[4,3,1]`. ✓
`verify_matrix.py`: binary `11110001` = root `1` + (3 ones, 3 zeros, 1 one);
`[1,1] --3·M1--> [1,4] --3·M0--> [13,4] --1·M1--> [13,17]`, ratio `13/17`. ✓

Both agree with the statement.

## Final answer

SBE `[1,13717420,8]`, binary `1` `+` `0×13717420` `+` `1×8`.

Peel check: `123456789 = 9·13717421`, `987654321 = 9·109739369`, reduced form
`13717421/109739369`. Reading the pairs: start `(13717421,109739369)`,
p>q so bit 0 and `(13717421-109739369, ...)` — the sequence of subtractions
produces exactly one initial `1` bit, then 13717420 zero bits, then 8 one bits,
then the root. SBE `= [1,13717420,8]`.

Matrix check: `apply_run([1,1],'0',13717420) = [13717421, 1]`;
`apply_run([1,1,'1',8)`... = `[13717421, 8·13717421+1] = [13717421, 109739369]`
ratio `13717421/109739369 = 123456789/987654321`. ✓

Reconstructed n: `n = 2^(13717420+8) + (2^8 - 1) = 2^13717428 + 255`,
bit length `13717429`, RLE `[1,13717420,8]`. ✓

## Answer

```
1,13717420,8
```
