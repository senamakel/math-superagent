# Ross, "Empirical Structure of the Gilbreath Decay Constants" (Zenodo PDF)

<!-- source: https://zenodo.org/api/records/21326026/files/Empirical_Structure_of_the_Gilbreath_Decay_Constants.pdf/content | full text: sources/ross-gilbreath-decay-constants-pdf.full.md -->

The July 2026 note by Michael M. Ross (independent researcher) quantifying decay in the CHT
stationary continuous Gilbreath model: top row i.i.d. standard exponentials,
`a(i+1,j)=|a(i,j)−a(i,j+1)|`, `c_i := E a(i,j)`.

## What it establishes

- The `{0,2}`-regime framing stated explicitly (the "two mechanisms" distinction): parity
  alone forces every leading entry odd; getting it to 1 requires reaching and sustaining the
  closed `{0,2}` regime. This is exactly the run's reduction.
- Exact low-depth anchors: `c_i = (i+1)·E b(i,1)` after writing `a_r = s·b_r` on the standard
  simplex; each sign-cone gives a linear form, so `c_i` is a sum of rational polytope volumes.
  CHT's c_0..c_3 are reproduced; **new exact** `c_4 = 778959731701/1447295850000`, plus exact
  c_5, c_6 (digest truncated before their values; see full text).
- Empirical law `c_i ≈ C·λ^{s_2(i)}/i`, `s_2` = binary digit sum, λ ≈ 1.14–1.20; 1/i visible
  within digit-sum classes, dyadic sawtooth in pooled data; saturation at extreme digit sums.
- Finite-depth experiments: polynomial-vs-exponential phase transition for Unif[0,R(j)] data;
  full-row relaxation τ(G) ≈ G^{0.63–0.66}; spike of amplitude G survives ≈ G columns (decays
  ~1 unit per column).
- Open status: neither `c_i → 0` nor boundedness proved.

## Bearing on this run

The digit-sum law is the continuous analogue of the run's discrete mod-4/Pascal structure
(c_finite values track A000120). It quantifies the regeneration obstruction's averaged shadow.
All asymptotic statements are empirical by the author's own disclaimer; only the low-depth
values and identities are exact. Nothing here is a proof about primes.

## Source status

Zenodo record 21326026, version of 21326025; CC-BY-4.0; PDF 696 KB; author-flagged
empirical. Complements the run's held CHT full text (sources/chase-hunter-tao-2026-full-html.full.md).