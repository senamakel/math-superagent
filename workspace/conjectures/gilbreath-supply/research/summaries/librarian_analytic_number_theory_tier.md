# Librarian: the analytic-number-theory (averaged-correlation) engine tier — added

Author: librarian. This run. Supplements `librarian_findings_supply.md` and
`librarian_coverage_pass.md`.

## What was missing and is now local

Directive 7 froze aimless search, but three open (proposed, not refuted)
approaches cited primary sources that were **absent from the library**, and their
engine papers are precisely nameable — a permitted gap. All three are the modern
analytic-number-theory machinery of averaged correlation decay for multiplicative
functions, which is the natural home of GOAL priority 1 (the averaged form of
SUPPLY). All three are now downloaded, indexed, and digested with claim blocks:

| Source | File | arXiv | Bearing |
| --- | --- | --- | --- |
| Matomäki–Radziwiłł, *Multiplicative functions in short intervals* | `sources/matomaki_radziwill_multiplicative_short_intervals.full.md` | 1501.04585 | Short-average cancellations of bounded multiplicative functions (μ, λ) — the value-domain engine of the `matomaki-radziwill-index-autocorrelation` approach. |
| Matomäki–Radziwiłł–Tao, *Fourier uniformity ... on average* | `sources/matomaki_radziwill_tao_fourier_uniformity_averaged.full.md` | 1812.01224 | Averaged form of Chowla at short intervals, `o(XH)` Fourier-uniformity for `H ≥ X^θ` — the quantified L²/autocorrelation engine the index-domain open step would invoke. |
| Green–Tao, *The Möbius function is strongly orthogonal to nilsequences* | `sources/green_tao_mobius_nilsequences.full.md` | 0807.1736 | Strong Möbius-nilsequence orthogonality (MN(s)) — the engine of the proposed `gowers-u2-nilsequence-uniformity` approach. |

## Honest bearing (what each does NOT do)

All three are **value-domain** statements for multiplicative functions (μ, λ)
indexed by integers. SUPPLY's object is the character `s_j = χ(q_j)` at **prime
indices**, and the fold's weight `wt(Φ_n h)`. The bridge each requires is the
**index-domain transfer** (via the Λ-weighting passage `Σ_j s_j ↔ Σ_n Λ(n)χ(n)`,
and the `g=0` adjacent-index case which is the parity barrier). None of these
sources proves SUPPLY, and none states a Walsh/subset-sum lower bound on
`wt(Φ_n h)` for the fixed prime string — so the open request
`walsh-spectral-subset-b904` remains genuinely open. What they add is the
confirmed existence and precise shape of the averaged-correlation-decay machinery
that the open averaged-form route would lean on.

## Four arXiv ID collisions caught and corrected

Guessing arXiv IDs resolved to wrong papers four times this run:
`1307.4385` (Banach thickness, math.FA), `1503.09121` (random-matrix thesis),
`1704.07746` (pdf and html: physics/Haldane). Each was verified against the
intended title, overwritten in place, or flagged as a pointer-only file (see
`sources/matomaki_radziwill_tao_averaged_chowla.full.md`). Correct IDs confirmed
via the published DOIs: `1501.04585` (MR short intervals), `1812.01224`
(MRT Fourier uniformity). Lesson stored in Cognee and in
`sources/DELETED_wrong_arxiv.md`: verify a fetched title before trusting a digest;
use the published DOI / exa_search to confirm arXiv IDs, not inference.
