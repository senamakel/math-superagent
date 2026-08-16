# Librarian report — the SUPPLY reference set, current state

Author: librarian (this pass). This is a verification-and-maintenance pass on an
already mature library. No new source was needed and none was fetched: the
search freeze (directive 30) is in force, the library already covers every live
line, and the one open request (`walsh-spectral-subset-b904`) is a gap in
theorems, not in literature.

## What I verified (the core librarian duty this run)

1. **The reference set is complete for the live territory.** Every one of the
   tiers below is represented by full text(s) in `research/sources/`, each with
   its source URL recorded on line 1 (`<!-- source: … -->`), and a digest in
   `research/summaries/` carrying its claim blocks.

2. **The index reaches the sources.** I ran `search_documents` across every tier;
   all resolve. This addresses the one failure mode this run has hit before
   (sources on disk but not indexed, so `search_documents` could not reach them).

3. **One indexing gap found and closed this pass.** `wu_nonuniform_residues_prime_sequences.full.md`
   (Wu 2019, arXiv:1908.07095 — length-k consecutive-prime residue-pattern
   frequencies open at every order k≥2, the K>1 parity-barrier companion) was
   on disk but **not** in the search index. I indexed it
   (`index_document`); it now resolves. Its digest `summaries/wu_nonuniform_residues_prime_sequences.md`
   already carried claim blocks. No other source I probed was missing from the
   index.

## The tiers on disk (all indexed, all digest-carrying)

| Tier | What it covers | Representative sources |
| --- | --- | --- |
| Parity barrier / switch density | the mod-4 consecutive-pair problem SUPPLY reduces to | Ash–Beltis–Gross–Sinnott 2011 (`ash_beltis_gross_sinnott_prime_residues`), Lau 2024 (`lau_residue_patterns`), Lemke Oliver–Soundararajan 2016 (`lemke_oliver_soundararajan_bias` + sawtooth), Wu 2019 (`wu_nonuniform_residues_prime_sequences`, **indexed this pass**), Granville–Martin, Rubinstein–Sarnak |
| Equal-residue side / door-3 refutation | long constant runs, the wrong direction | Shiu 2000 expository (`shiu_strings_expository`), Maynard 2016, Banks–Freiberg–Turnage-Butterbaugh 2015, Freiberg 2010 |
| The fold Φ (Rule-90 / Pascal-mod-2 / Lucas-submask) | Lucas' theorem, the submask-XOR reading, k-regularity | Meštrović, Hofer, Bacher, Allouche–Shallit I & II, Rampersad–Wiebe, Steinhaus triangles, Rowland, Szechtman, Yoshida |
| Walsh / Krawtchouk / MacWilliams / Delsarte | weight-distribution and analysis-of-Boolean machinery | O'Donnell, Guruswami–Rudra–Sudan, MacWilliams 1963, Friedlander, Meshulam, Donoho–Stark, Tao's uncertainty notes |
| Higher order (K>1) | Gowers norms, inverse theory, automatic sequences | Tao *Higher Order Fourier Analysis*, BKM 2020, Konieczny (two), Konieczny–Müllner, Müllner–Spiegelhofer |
| Ergodic / Rule-90 limit measures | Lucas-mixing / randomization | Pivato–Yassawi I & II, Pivato (LCA entropy + sofic), Takei |
| Direct prior work on the object | the absolute-difference triangle, {0,2} reduction | Odlyzko 1993, Chase 2022, Encyclopedia of Mathematics *Gilbreath conjecture*, Lacasa et al. 2018 |
| Value-domain analytic NT | multiplicative functions, nilsequences, digit sums | Matomäki–Radziwiłł, MRTF, Green–Tao, Mauduit–Rivat, Green |

## What is genuinely unobtainable / absent (so nobody retries it)

- **A Walsh/subset-sum lower bound on `wt(Φ_n h)` for the fixed prime string** — request
  `walsh-spectral-subset-b904`. This is a `theorem to be found`, not a source: no
  published result states it. Nothing to download.
- **The finite-prefix / index-domain transfer** (from the ergodic-CA and
  value-domain analytic-NT theorems to the single deterministic finite-string
  fold `wt(Φ_n h)`) — the run's own open step (thread `finite-prefix-transfer`);
  in no source.
- **Recorded dead downloads** (kept so nobody repeats them): real Shiu-2000 PDF
  (Wiley cookie wall; the expository full text stands in), wrong-identity
  Matomäki–Radziwiłł–Tao arXiv ID (`matomaki_radziwill_tao_averaged_chowla` is a
  pointer only), and a wrong-identity Yoshida arXiv ID (`DELETED_wrong_arxiv_yoshida.md`).

## The search freeze

Search and download are gated by directive 30 until the N=160000 Ratio B
discriminator has a capture or an unaffordable-runtime note is accepted.
`code/out/ratio_b_extension.txt` records N=160000 was **not** run (projected
~22 min, over budget), so the note leg of the release condition exists on disk
but the freeze is recorded as still in force. Consistent with that, this pass
fetched **nothing** — the library was verified complete without it.

## Bottom line

The reference set needs no further gathering for any live line of attack. The
two open gaps are both theorems-to-be-found or in-house computations, not
literature, and both are already stated precisely in `research/REQUESTS.md` and
`research/ROOT.md`. The one mechanical action this pass took — indexing the Wu
source that was on disk but unreachable by search — made the index agree with
the folder.
