# Brown, `totientsum.py` — reference implementation of Algorithm 13

Source: https://arxiv.org/src/2506.07386v1/anc/totientsum.py — code at
`research/sources/brown-totientsum-ancillary.full.md`.

## What this source establishes

The author's own Python implementation of Algorithm 13 (the Θ̃(n^{2/3})-time,
Θ̃(n^{1/3})-space totient summatory algorithm of arXiv:2506.07386). It is the
ground truth against which any re-implementation can be diffed.

Key structure (matching the paper's Algorithm 13):

- `mobiussieve(limit)`: segmented Möbius sieve, yields μ(k) for k < limit.
- `totientsum(n)`:
  - `a = introot(int((n / log(log(n)))**2), 3)`; `b = n // a`; `nr = isqrt(n)`.
  - `Mover` array (indexed by y, 1..b) accumulates M(⌊n/y⌋) contributions;
    `Mblock` holds the batch of Mertens values from phase 2.
  - Phase 1: for x ≤ √n, accumulate X and fill `Mover` via the
    μ(x)·⌊v/y⌋ updates and the `1 − ⌊n/d⌋ + x·mert` corrections, processing
    Mertens batches of size b.
  - Phase 2: for √n < x ≤ a, save Mertens values at the χ-points
    (χ = ⌊n/s⌋), flush batches when full, and finish Z = mert·b(b+1)/2.
  - Phase 3: for y = b..1, compute M(⌊n/y⌋) from `Mover` via the Mertens
    recursion tail, accumulate Y = Σ y·M(⌊n/y⌋).
  - Return X + Y − Z.

The code was used to produce Table 1 of the paper, including the new
Φ(10^19) = 30396355092701331435065976498046398788, verified by running twice.

## Why it matters here

It is the independent reference implementation for the run's
`code/solution.py`: the run's solver should agree with `totientsum(n)` on
every n it can reach, and in particular must reproduce Φ(10^8) =
3039635516365908 (OEIS A064018 a(8)) and the statement's H(10^8) target.
**[correction 2026-08-14: the previous text said Φ(10^8)=303963552391; that
is wrong — it conflates Φ(10^6)=303963552392 with row 8. The correct value
a(8) = Φ(10^8) is 3039635516365908.]**

Note: the file was downloaded as `.py` and converted to Markdown; to execute
it, strip the Markdown code fence (the body is the original Python source).
