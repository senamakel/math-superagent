# Scholar — third-pass library audit

This pass confirms the on-disk library is exhausted and the third-pass
computation is sound. No new source digest was needed; the value added is an
independent hand-verification of the live threshold column, a memory
persistence attempt, and a statement of what still lacks a source.

## What the library already establishes (not re-derived)

The third pass's live computation is captured twice and cross-checked:
`code/out/threshold_limit_exact.txt` and
`code/out/threshold_exact_mean_independent.txt` (independent code path,
digit-for-digit to n=16384), plus the exponent fit
`code/out/threshold_exponent_fit_pass3.txt` and claim
`weight-threshold-tends-to-zero-sublinear-exponent`.

The exact-mean closed form is
`mean_n(w) = (1/n) Σ_{d=2}^{n−1} P_d(w)` with
`P_d(w) = (C(n,w) − [z^w](1−z)^k(1+z)^{n−k}) / (2C(n,w))`, `k = 2^popcount(d)`.

## Independent hand-check (oracle verification, small case)

I recomputed the n=8, w=1 cell by hand rather than trusting the capture, to
confirm the formula's *logic* independently of the code:

- Cells d ∈ [2,7] with popcount/depth-size k = 2^popcount(d):
  d=2,4 → pc 1, k=2 (two cells); d=3,5,6 → pc 2, k=4 (three cells);
  d=7 → pc 3, k=8 (one cell).
- `[z^1](1−z)^k(1+z)^{8−k} = (8−k) − k = 8 − 2k`.
- `P_d(1) = (8 − [z^1]) / (2·8)`: k=2 → (8−4)/16 = 1/4; k=4 → 8/16 = 1/2;
  k=8 → 16/16 = 1.
- `Σ P_d = 2·(1/4) + 3·(1/2) + 1 = 3.0`; `mean = 3/8 = 0.375`. ✓ matches the
  capture's 0.375 and the exhaustive `linear_supply_by_weight.txt` (8→3).

So the exact-mean half is reproduced by hand arithmetic, independent of the
program — this is the ordinal check the claim's per-n `w*` values stand on.

## Threshold-balance sanity: why the exponent is not a settled 1/2

I also checked the *mechanism* of the threshold by hand at n=4096 (w*=77,
alpha=0.0188): the balance `Σ_d (1−2α)^{k_d} ≈ 0.2·n` reproduces mean ≈ 0.40.
The dominant cells are those with popcount well below L/2 (low hit-count),
so the threshold weight genuinely outpaces `√n` at finite n — this is why `1/2`
is rejected by the data (librarian's rising `w/√n` column) and why the claim
correctly calls the exponent *fitted* (0.55678±0.00225), not a closed form.
I do **not** override the measured result; it is sound.

## Sources that do not help (already recorded; kept for the record)

- `debruijn_cyclespace_eigenvectors` — abstract-only; De Bruijn Laplacian
  eigenvectors have no bearing on Φ_n's image weight.
- `ashikhmin_barg_litsyn_polynomial_method`, `friedlander_macwilliams_krawtchouk`
  — abstract-only; use Wikipedia Krawtchouk/MacWilliams + Guruswami fulltexts.
- `granville_martin_prime_number_races` — duplicate of `prime_races`.
- `matomaki_radziwill(_tao)`, `green_tao_mobius_nilsequences` — value-domain
  multiplicative machinery; indexing transfer absent.
- `encyclopedia_gilbreath`, `chase_random_gilbreath`, `odlyzko_gilbreath` —
  out of scope (Gilbreath not the goal).
- `hoi_annotated_bibliography_*` — bibliography index, no theorem family.

## What the run still lacks (unchanged)

1. The finite-prefix → actual-Hamming-weight transfer (absent from all
   sources; the largest missing tool).
2. The unconditional second-moment bound `E[S(n)²] = O(n)` for the prime
   string `h` (`walsh-spectral-subset-b904` stays open).
3. A proof (not fit) of the threshold-weight limit / an asymptotic for the
   exponent — the open lemma `threshold-limit-hinges-on-hypergeometric-mode-bound`.

## Memory

`recall_memory` returns 404 (Cognee read broken this run). I attempted to
persist the load-bearing third-pass finding so a later run can reach it; the
write-side result is below.
