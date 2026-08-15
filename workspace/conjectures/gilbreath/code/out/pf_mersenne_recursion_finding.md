# Mersenne per-residue affine constants: elementwise recursion (verified k=2..12)

**Finding (verified-numerically, k=2..12 exact; induction from recursion is a
proof, recursion itself is a verified conjecture).**

## Setting

2-then-odds sequence, tail-1 halved-gap word `h = [0]*(P-1)+[1]` (a single 1 at
residue P-1), odd period `P = 2^k - 1` (Mersenne). `nu2(n)` = #2s in the
maximal `{0,2}`-suffix of the right diagonal. Nu2 is per-residue affine mod P:
`nu2(n+P) - nu2(n) = c_r` constant per residue r. Let `A_k[r] = c_r / 2`.

## Result

**The array `A_k` (length P = 2^k-1) obeys the exact elementwise recursion**

    A_{k+1} = [1] + b1 + b2     (length 2P+1 = 2^{k+1}-1)
    b1 = [2*A_k[1] + 1] + [2*A_k[i] for i=2..P-1] + [2]
    b2 = A_k with A_k[1] incremented by 1

verified by direct per-residue affine extraction for every k=2..12
(fresh computation, not the run's hand-copied arrays; 0 mismatches).

## Derived: sum identity, by induction from the recursion (PROOF given recursion)

Algebra: with `S_k = sum(A_k) = 1 + A_k[1] + sum(A_k[2:])`,
`b1 = 2A1+3 + 2*sum(A2:)`, `b2 = S_k + 1`, so
`S_{k+1} = 1 + b1 + b2 = 3*S_k + 3`.  Base `S_2 = 3`.
Hence **`sum(A_k) = (3^k-3)/2`**, i.e. **`sum(c_r) = 3^k - 3`** (A058809),
verified numerically k=2..12 (531438 at k=12) and this is a proof *conditional
on the recursion*.  Density slope `(3^k-3)/(2^k-1)^2`.

## Structural corollaries (all verified exactly k=2..12)

- `min c_r = 2` for all k, so `nu2(n) >= (2/(2^k-1)) n - O(1)`: positive linear
  supply on every Mersenne tail-1 word.
- The `A_k[r] == 1` positions (ones of `c_r/2`) are exactly the descending
  partial sums `0, 2^{k-1}, 2^{k-1}+2^{k-2}, ..., P-1` — i.e.
  `r = sum_{j=i}^{k-1} 2^j`, i=0..k-1 (k matches exactly).
- `P=3` closed form exact: `nu2(n) = 2*floor((n-1)/3)`, 0 violations to n=4000.

## Fermat-like family (verified, m=2..5)

For `P = 2^m + 1`, modulus `L = 2^{2m}-1`, `c_r` is **constant** `= 3^m - 1`
for every residue; slope `(3^m-1)/(2^{2m}-1)`.

## Status / falsifier

The elementwise recursion is a **verified conjecture** (k=2..12), not proved.
It was pushed one k beyond the run's data (data had k<=10; here k=11,12 also
verified, so the first falsifying k lies beyond 12). The induction `S_{k+1}=3S_k+3`
from the recursion is a proof given the recursion. A full proof of the recursion
would require deriving the per-residue affine constants from the subset-zeta /
rule90 fold structure (the tail-1 word's single-1 fold is a genuine combinatorial
count). Does NOT close G-supply (aperiodic primes remain named-open).

## Files
- attack: `code/out/pf_mersenne_recursion_attack.py`
- extension: `code/out/pf_mersenne_recursion_extend.py` (k=2..12)
- P3 closed form: `code/out/pf_mersenne_p3_closedform_verify.py`
