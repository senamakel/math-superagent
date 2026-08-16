# Librarian: analytic-number-theory tier now local (averaged-correlation engines)

The reference library is complete for the live lines. This run verified the
existing 40+ source tier and closed the one genuine gap: three primary sources
cited by the *open* (proposed) approaches were absent, and are now local,
indexed, and digested with claim blocks:

- **Matomäki–Radziwiłł, Multiplicative functions in short intervals** (Ann.
  Math. 183 (2016); arXiv:1501.04585) — short-average cancellations of μ/λ.
  Engine of `matomaki-radziwill-index-autocorrelation` (averaged form).
  Claim `mr-short-averages-of-multiplicative-functions-cancel`.
- **Matomäki–Radziwiłł–Tao, Fourier uniformity ... on average** (Invent. Math.
  220 (2020); arXiv:1812.01224) — averaged Chowla at short intervals,
  ∫|Σ λ(n)e(−αn)| dx = o(XH) for H ≥ X^θ. Claim
  `mrt-fourier-uniformity-averaged-correlations-vanish`.
- **Green–Tao, Möbius strongly orthogonal to nilsequences** (Ann. Math. 175
  (2012); arXiv:0807.1736) — |(1/N)Σ μ(n)F(g(n)Γ)| ≪ log^{−A}N, MN(s).
  Engine of `gowers-u2-nilsequence-uniformity`. Claim
  `green-tao-mobius-orthogonal-to-nilsequences`.

**Banker's honesty:** all three are value-domain statements for μ/λ over
integers. SUPPLY is a prime-INDEX character and a finite fold weight; the
index-domain transfer (Λ-weighting bridge; the g=0 adjacent-index case = the
parity barrier) is STILL the open step and is not in any of them. None closes
`walsh-spectral-subset-b904`. But if the averaged form (GOAL priority 1) is
attacked through MRT-type correlation decay, the exact theorem shapes you would
cite are now on disk, read to be checked against the run's numeric index-domain
autocorrelations.

Four arXiv-ID collisions caught and corrected (wrong papers for 1307.4385,
1503.09121, 1704.07746); a pointer-only quarantine file marks the mislabeled
`matomaki_radziwill_tao_averaged_chowla.*`. No wrong content entered the claims
ledger. Full map: `research/summaries/librarian_report_reference_library.md`.
