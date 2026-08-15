# Why the universal covering bound fails — kernel of the transfer matrix

## Setup

Right diagonal of a 2-then-odds prefix `q_1..q_n`: cells `(k, n-k)`, k=0..n-1.
Tail (the maximal `{0,2}` suffix region, run's convention `d[2:-1]`):
`k = 2..n-2`. A halved tail cell at depth k equals the XOR of a Pascal window of
the row-1 halved gap bits `h[j] = (g_j/2) mod 2` over ancestor columns `[n-k, n-1]`:

    halved(k, n-k) = XOR_{j : binom(k-1, j-(n-k)) odd} h[j]

Define the F2 matrix `Phi_n`, rows k=2..n-2, cols j=2..n-1:

    Phi_n[k][j] = [ C(k-1, j-(n-k)) mod 2 ]   (0 if j outside [n-k, n-1])

Then `wt(Phi_n h) = nu2(q_n)` = number of 2s in the {0,2} suffix.

## The kernel (structural, computed)

For every n = 2..20 (code/out/kernel_characterize.captured.txt):

    dim = n-2 columns, n-3 rows
    rank = n-3
    nullity = 1
    ker Phi_n = span(111..1)

**Reason it is the all-ones vector:** row k's dot product with all-ones is the
full Pascal row sum `Sigma_t C(k-1, t) = 2^(k-1) = 0 (mod 2)` for every k >= 2.
So `Phi_n * (all-ones) = 0`, i.e. every tail cell is 0 on the all-ones input.

## The universal claim is dead

`wt(Phi_n h) >= c * wt(h)` for ALL h, with a fixed c > 0, is false for every
c > 0: take h = all-ones, which sits in the kernel, giving `wt(Phi_n h) = 0`
while `wt(h) = n-2` grows linearly. Hence `min_{h != 0} wt(Phi_n h)/wt(h) = 0`
at every n.

The all-ones h is exactly the **consecutive-odds** sequence q=(2,3,5,7,9,...)
(all gaps = 2 ≡ 2 mod 4). This triangle is SUCCESSFUL (A_k(0) = 1 at every n;
cross-checked two independent code paths) yet nu2 = 0. So the transfer
`nu2 >= c·w` fails within the successful-class domain itself.

This confirms claim `g-supply-transfer-refuted` and decides the S1 fork to the
prime-specific case (b): the supply decomposition `nu2 >= c·w` is NOT a
universal combinatorial reduction.

## The real primes escape the kernel

Sieve to 1,000,000 (78,498 primes), n up to 3000:

    min nu2/w = 0.5152  (at n=53)
    nu2 = 0 never occurs on any real column

So the real prime halved-gap bit string is never in the kernel (never all-ones
on any window), consistent with nu2/w in [0.689, 0.867] on the earlier sparser
samples. The 0.5152 vs 0.689 difference is sample density: 0.689/0.867 was on
samples n in {50..3999}; the n≤3000 dense scan hits lower minima at small n.

## What this settles

- The prime-free, "provable half" of G-supply (the covering bound) does not
  exist as a universal statement. It is refuted, not weakened (Directive 54).
- Any supply-side lower bound must be prime-specific (case b): it rests on
  special structure of the prime halved-gap bit string, not on the F2 Rule-90
  geometry alone.
- The conditional theorem (HL/LOS ⟹ nu2 = n/2 + O(sqrt(n log n))) remains the
  honest deliverable; it applies the fold map to the prime bit string directly,
  NOT through the refuted universal transfer.

## Files

- code/refute/kernel_characterize.py (Gaussian elimination, exact F2)
- code/out/kernel_characterize.captured.txt (capture)
- code/refute/universal_transfer_matrix_run.py (exhaustive min-ratio scan)
- code/out/universal_transfer_matrix_RUN.captured.txt (capture)
