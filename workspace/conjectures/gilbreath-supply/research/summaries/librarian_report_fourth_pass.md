# Librarian report — reference library (this pass)

What is now available locally in `research/sources/` (full texts, never
edited), with digests in `research/summaries/`, all indexed and reachable via
`search_documents`.

## What this pass changed

The reference library was already **mature and fully digested** for every live
line of attack (52 full texts, 70+ digests before this pass). I verified the
maturity rather than bulk-adding. One genuine gap existed and I closed it:

### Added: Tao, *Higher Order Fourier Analysis* (AMS GSM 142)

| Field | Value |
| --- | --- |
| File | `research/sources/tao_higher_order_fourier_analysis.full.md` |
| Digest | `research/summaries/tao_higher_order_fourier_analysis.md` |
| Source URL | https://terrytao.wordpress.com/wp-content/uploads/2012/12/gsm-142-tao7-higher-book-05june2012.pdf (author's preliminary version, published by AMS) |
| Original publisher | AMS, Graduate Studies in Mathematics vol. 142 (2012), ISBN 978-0-8218-8986-2 |

**Why it was the one missing canonical reference.** The reopened question
(GOAL priority 2) is framed in the vocabulary of **correlation order `K`**:
a functional of the fold sensitive to `1 < K ≲ n/2`. That is precisely the
subject of higher-order Fourier analysis — Gowers uniformity norms `U^s`,
their inverse theory (nilsequences over finite fields and the integers), and
the equidistribution of polynomial phases. Tao's book is the canonical
reference for that vocabulary, and it was **cited twice by the library's own
Gowers-norm sources** (Byszewski–Konieczny–Müllner and Konieczny both cite
it) without being held. It is now held and indexed.

**Honest bearing (not a key).** The book supplies the structure: under the
inverse conjecture, an order-`K`-blind functional on a bounded input means
orthogonality to `K`-step nilsequences. Door 3 (Thue–Morse) is a fully
Gowers-uniform input that nevertheless collapses (`ν₂` sublinear) — so
correlation-order control of `h` alone cannot be the weaker arithmetic input
that forces `wt(Φ_n h) ≥ c·n`. The book sharpens what a `1 < K` control input
must look like but does **not** transfer to the fixed finite-string fold on the
prime gap-parity string, and closes no open request.

## Inventory (now)

- **53 full texts** in `research/sources/`, each with its source URL on line 1
  (`<!-- source: … -->`), all indexed and search-reachable.
- **72+ digests** in `research/summaries/`, carrying claim blocks that feed
  `research/CLAIMS.md` (re-derived on this write).

Tiers covered and current:
1. **Parity barrier / mod-4 switch side:** Ash–Beltis–Gross–Sinnott 2011; Lau
   2024; Lemke Oliver–Soundararajan 2016 (+ sawtooth paper); Los 2018; Wu 2019;
   Granville–Martin *Prime Number Races*; Rubinstein–Sarnak *Chebyshev's Bias*;
   Montgomery–Soundararajan *Beyond pair correlation*.
2. **Equal-residue side / door-3 refutation:** Shiu 2000 (expository full text);
   Maynard 2016; Banks–Freiberg–Turnage-Butterbaugh; Freiberg 2010.
3. **The fold Φ (Rule-90 / Pascal-mod-2 / Lucas-submask):** Meštrović; Hofer;
   Bacher; Allouche–Shallit k-regular I & II; Rampersad–Wiebe; Steinhaus
   triangles; Rowland; Szechtman.
4. **Walsh / Krawtchouk / MacWilliams / Delsarte:** O'Donnell; Guruswami–Rudra–
   Sudan *Essential Coding Theory*; MacWilliams 1963; Friedlander; Wikipedia
   Krawtchouk & MacWilliams; Donoho–Stark; Meshulam; Tao's uncertainty notes.
5. **Higher-order / Gowers / automatic (the reopened K>1 territory):** Tao
   *Higher Order Fourier Analysis* (**this pass**); BKM 2020; Konieczny 2019
   (1611.09985); Konieczny–Müllner; Müllner.
6. **Ergodic / Lucas-mixing / Rule-90 limit measures:** Pivato–Yassawi I & II;
   Pivato (LCA entropy, sofic); Takei.
7. **Direct prior work on the exact object:** Odlyzko 1993; Chase 2022;
   Encyclopedia of Mathematics *Gilbreath conjecture*; Lacasa et al. 2018
   (forbidden gap-blocks mod 6, unconditional).
8. **Value-domain analytic number theory:** Matomäki–Radziwiłł; MRTF; Green–Tao
   (nilsequences); Mauduit–Rivat; Green *Three topics*.

## Indexing integrity

Verified by `search_documents`: the new Tao source returns on the
Gowers-uniformity / inverse-conjecture query, alongside O'Donnell, Green–Tao,
MRTF and the coding-theory texts. All sources resolve from search.

## What is genuinely unobtainable or absent (so nobody retries it)

- **A Walsh/subset-sum lower bound on `wt(Φ_n h)` for the fixed prime string**
  (open request `walsh-spectral-subset-b904`) is a gap in **theorems, not in
  the library** — no published result states it. Nothing to download; it is a
  theorem to be found.
- **The finite-prefix / index-domain transfer** (from the ergodic-CA and
  value-domain analytic-NT theorems to the single deterministic finite-string
  fold) appears in no source — it is the run's own open step (thread
  `finite-prefix-transfer`).
- Recorded dead downloads, kept so nobody repeats them: the real Shiu-2000 full
  text (Wiley cookie wall; the freely-available expository full text stands in
  for it), the wrong-identity Konieczny arXiv paper, and the wrong
  Matomäki–Radziwiłł–Tao arXiv ID.
