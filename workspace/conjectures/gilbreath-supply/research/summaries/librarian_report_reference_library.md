# Librarian report — reference library state (this run)

Author: librarian. Date: this run. What is now available locally in
`research/sources/` (full texts, never edited) with `research/summaries/`
digests, all indexed and reachable via `search_documents`.

## What this run added

The library was already near-complete from the parent investigation. This run
verified integrity and closed the one genuine, nameable gap standing between the
library and the *open* (proposed, not refuted) approaches: the modern
analytic-number-theory machinery of **averaged correlation decay for
multiplicative functions**, which is the natural home of GOAL priority 1 (the
averaged form of SUPPLY). Three primary sources added:

| Source | File in `research/sources/` | Source URL | Summary | Claim |
| --- | --- | --- | --- | --- |
| Matomäki–Radziwiłł, *Multiplicative functions in short intervals* (Ann. Math. 183, 2016) | `matomaki_radziwill_multiplicative_short_intervals.full.md` | https://arxiv.org/html/1501.04585 | `summaries/matomaki_radziwill_multiplicative_short_intervals.md` | `mr-short-averages-of-multiplicative-functions-cancel` |
| Matomäki–Radziwiłł–Tao, *Fourier uniformity ... in short intervals on average* (Invent. Math. 220, 2020) | `matomaki_radziwill_tao_fourier_uniformity_averaged.full.md` | https://arxiv.org/pdf/1812.01224 | `summaries/matomaki_radziwill_tao_fourier_uniformity_averaged.md` | `mrt-fourier-uniformity-averaged-correlations-vanish` |
| Green–Tao, *The Möbius function is strongly orthogonal to nilsequences* (Ann. Math. 175, 2012) | `green_tao_mobius_nilsequences.full.md` | https://arxiv.org/pdf/0807.1736 | `summaries/green_tao_mobius_nilsequences.md` | `green-tao-mobius-orthogonal-to-nilsequences` |

These ground the engines of two open approaches:
- `matomaki-radziwill-index-autocorrelation` (proposed; averaged form, GOAL priority 1);
- `gowers-u2-nilsequence-uniformity` (proposed).

The third `mrt-fourier-uniformity` source is the quantified L²/autocorrelation
version the index-domain open step would invoke.

## Honest bearing — what they do NOT do

All three are **value-domain** statements for multiplicative functions (μ, λ)
indexed by integers. SUPPLY's object is the character `s_j = χ(q_j)` at **prime
indices**, and the fold weight `wt(Φ_n h)`. The gap each leaves is the
**index-domain transfer** (the Λ-weighting passage `Σ_j s_j ↔ Σ_n Λ(n)χ(n)`, and
the `g=0` adjacent-index case = the parity barrier). **No source here proves
SUPPLY or gives the Walsh/subset-sum bound on `wt(Φ_n h)`**, so the open request
`walsh-spectral-subset-b904` remains genuinely open. The finding note covering
this is `summaries/librarian_analytic_number_theory_tier.md`.

## Full canonical tier (verified present, all indexed)

- **Switch-density / prime-residue:** ABGS 2011 (`ash_beltis_gross_sinnott_prime_residues`),
  Lau 2024 (`lau_residue_patterns`), Lemke Oliver–Soundararajan 2016
  (`lemke_oliver_soundararajan_bias`), Granville–Martin (2 mirrors), Rubinstein–Sarnak.
- **Equal-residue (refutes doors 1–3):** Shiu 2000, Maynard 2016, BFTB 2015,
  Freiberg 2011.
- **The fold itself / Lucas:** Meštrović (Lucas survey, 2 formats), Bacher 2008,
  Hofer 2025, Allouche–Shallit (k-regular I & II), Rampersad–Wiebe 2023,
  Rowland, Szechtman, Odlyzko 1993 (the {0,2} object), Chase 2022 (random Gilbreath).
- **Coding theory engine (adopted `fold-second-moment-krawtchouk`):** MacWilliams
  1963, Guruswami LP notes, Essential Coding Theory (Guruswami–Rudra–Sudan),
  Ashikhmin–Barg–Litsyn, Friedlander 2024, Wikipedia Krawtchouk + MacWilliams.
- **Ergodic / CA engine (adopted `lucas-mixing-finite-transfer`):** Pivato–Yassawi
  (sofic randomization + affine-limit measures I & II), Takei, Pivato (entropy),
  Matusiak–Özaydın–Przebinda (Donoho–Stark), Tao uncertainty.
- **New analytic-NT tier (this run):** Matomäki–Radziwiłł, Matomäki–Radziwiłł–Tao,
  Green–Tao nilsequences.

## Integrity corrections made

- **Wrong-download quarantine:** `matomaki_radziwill_tao_averaged_chowla.full.md`
  was briefly a random-matrix-thesis (wrong arXiv 1503.09121). Now a pointer-only
  file telling the reader to use the correctly-named 1812.01224 source — its
  misleading digest is also replaced. **No wrong content entered the claims ledger.**
- **Four arXiv ID collisions caught** (1307.4385→Banach, 1503.09121→RMT,
  1704.07746 pdf+html→physics). Correct IDs confirmed via published DOIs:
  `1501.04585`, `1812.01224`, `0807.1736`. Verified each fetched title against the
  intended paper. Stored in Cognee and in `sources/DELETED_wrong_arxiv.md`.

## Verification bound / phase-1 (already established, unchanged by this run)

Per `research/ROOT.md`: oracle runs to n=8000 with convention pinned
(ν₂(4000)=1975); pointwise ceiling N=40000; three settled restricted classes
(uniform/rank, all-ones kernel, anti-dyadic balanced); the run-telescope identity
machine-verified to 2^14. This run added no new computation and made none of those
claims — it closed a library gap, which is the librarian's role.

## Report of unavailability

- The **finite-prefix / index-domain transfer** (from the ergodic CA and
  analytic-NT theorems to the single deterministic finite-string fold) appears
  in no source and is not in the library — it is the run's own open step.
- No arXiv source states the Walsh/subset-sum lower bound on `wt(Φ_n h)` for the
  fixed prime string (the `walsh-spectral-subset-b904` request) — a gap in
  theorems, not a gap in the library, so no further download closes it.
