# Librarian report — reopened pass, additions and state

Author: librarian. Date: this run (reopened second pass).

## What this pass added

**One new canonical source**: Ryan O'Donnell, *Analysis of Boolean Functions* (CUP 2014; arXiv May 2021 revision).

- Full text: `research/sources/odonnell_analysis_boolean_functions.full.md` (980 KB Markdown, indexed and searchable)
- Source URL (in the file, line 1): `http://www.cs.cmu.edu/~odonnell/papers/Analysis-of-Boolean-Functions-by-Ryan-ODonnell.pdf`
- Summary: `research/summaries/odonnell_analysis_boolean_functions.md` (indexed)
- Claim block filed: `odonnell-boolean-fourier-degree-k-toolkit` (see `research/CLAIMS.md`)

**Why it was the gap.** The reopened pass (GOAL priority 2) asks for *a functional of the fold, sensitive to correlation order K with 1 < K ≲ n/2, controllable by an arithmetic input strictly weaker than pointwise mod-4 switch density*. The library already had the **algebraic** Fourier/coding tier (Krawtchouk, MacWilliams, Delsarte, Walsh) and the **K>1 arithmetic** tier (Lacasa's unconditional mod-6 forbidden blocks; Wu's length-k pattern barrier). It lacked the **analytic Boolean-function** tier that governs degree-K Fourier weight, higher-order influence, and hypercontractivity — exactly the vocabulary in which "a functional of the fold of order K" is expressed (each fold cell being an XOR over submasks, i.e. degree = popcount(d)). O'Donnell fills that.

## Library state (verified this pass)

- **53 full texts** in `research/sources/`, each with source URL on line 1; all search-reachable via `search_documents`.
- **73 digests** in `research/summaries/`, carrying claim blocks that feed `research/CLAIMS.md`.
- Every adopted live line and every facet of the reopened K>1 question has a local primary/sourced reference:
  - Parity barrier: Ash–Beltis–Gross–Sinnott, Lemke Oliver–Soundararajan, Lau, Granville–Martin, Rubinstein–Sarnak
  - Equal-residue side (door 3 refutation, proved): Shiu (expository full text), Maynard, BFTB, Freiberg
  - The fold Φ: Pascal-mod-2 / Rule-90 / Lucas-submask (Meštrović, Hofer, Bacher, Allouche–Shallit I & II, Rampersad–Wiebe, Steinhaus, Rowland, Szechtman)
  - Walsh/Krawtchouk/MacWilliams/Delsarte: coding-theory book + dedicated sources
  - **Analytic Boolean-function tier (NEW): O'Donnell — higher-order influence, hypercontractivity, low-degree concentration**
  - K>1 on prime gaps: Lacasa (unconditional forbidden blocks), Wu (length-k barrier)
  - Ergodic / Rule-90 limiting measures: Pivato–Yassawi, Pivato, Takei
  - Direct prior work on the object: Odlyzko 1993, Chase 2022; encyclopedic tier
  - Uncertainty (Walsh-side): Meshulam, Tao

## Open gaps (unchanged, and not source gaps)

- The **only** open research request, `walsh-spectral-subset-b904`, is a *theorem* (a Walsh/subset-sum lower bound on `wt(Φ_n h) ≥ c·n` for inputs not "complicated" in the five refuted senses), not a source. No published result states it. O'Donnell adds the standard analytic toolkit for *building* such a bound (Fourier weight by degree, higher-order influence, hypercontractivity) but does not itself state it. The arithmetic input on the prime parity string (K>1, strictly weaker than switch density) remains genuinely open — the Lacasa positive transfer is dead (parity projection, `notes/lacasa_parity_projection_transfer.md`, proved), and Wu shows the length-k non-constant side is conjectural.
- Shiu-2000 primary (Wiley cookie wall) is intentionally not re-fetched; the freely available expository full text (`sources/shiu_strings_expository.full.md`) states and proves the quantitative theorem, so the door-3 refutation is sourced.

## Nothing further to gather

No source scarcer than the run's needs exists for the order-K question. The surviving gap is a theorem to be found, not literature to be downloaded. Further gathering happens only against a stated gap in `research/REQUESTS.md` (terminus directive).
