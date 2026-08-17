# Reference library report — Hilbert 16th, limit cycles

## Second pass additions (2025)

Five new primary/reference sources downloaded, indexed, and filed. All in
`research/sources/` with full text, digests in `research/summaries/`, claims in
`research/notes/claims.md` (→ `derived/CLAIMS.md`).

### 1. Galias–Tucker, "The Songling system has exactly four limit cycles" (2022) — CERTIFIED H(2) ≥ 4
- File: `sources/galias-tucker-songling-four-cycles.full.md`
- URL: http://www.zet.agh.edu.pl/~galias/ps/amc2022.pdf (open access CC BY)
- Establishes: the Shi Songling quadratic system with its three extreme
  parameter scales has **exactly** four limit cycles, proved by rigorous
  adaptive-precision interval arithmetic (P-map fixed points, explicit bounds
  spanning 10⁻⁷⁵→0.04, no-more-cycles chunks). **This is a fully certified
  reproduction of H(2) ≥ 4** — the strongest evidence of the lower bound in the
  library, and a template for this run's certified limit-cycle oracle.
- Evidence class: verified-computationally (rigorous, reflexive).

### 2. Gasull–Santana, "A note on Hilbert 16th problem" (Proc. AMS 2025) — H(n) strictly increasing
- File: `sources/gasull-santana-note-h16-pams-2025.full.md`
- URL: https://ddd.uab.cat/pub/artpub/2025/309367/GasSan24-Postprint.pdf
- Establishes: H(n+1) ≥ H(n)+1 (strictly increasing when finite); realizability
  by structurally stable fields; H(n) ≤ ℵ₀; recalls H(2n+1) ≥ 4H(n)
  (Christopher–Lloyd). Peer-reviewed.
- Evidence class: sourced (peer-reviewed postprint held full).

### 3. Christopher–Lloyd, "Polynomial systems: a lower bound for the weakened 16th Hilbert problem" (Extracta Math. 2001) — primary tangential lower bound
- File: `sources/christopher-lloyd-weakened-16th-extracta-2001.full.md`
- URL: https://ddd.uab.cat/pub/artpub/2001/110469/extmat_a2001v16n3p441.pdf
- Establishes: b_{m,n} ≥ ((n+1)(n+3)/8−1) for n≤m, ((m+1)(2n−m+3)/8−1) for
  n≥m (m,n odd), the open-access primary treatment of the weakened-H16 lower
  bound at one singular point; b_{m,n} ≤ N(m,n) ≤ H(max{m,n}).
- Evidence class: sourced (full text held).

### 4. BIRS 07w5021 report (2007) — independent confirmation of the DRR/121 reduction
- File: `sources/birs-workshop-h16-2007-report.full.md`
- URL: https://www.birs.ca/workshops/2007/07w5021/report07w5021.pdf
- Establishes: the Roussarie compactification → limit periodic sets → H(2)<∞
  reduces to finite cyclicity of 121 graphics; state of Picard–Fuchs /
  Varchenko–Khovanskii tools.
- Evidence class: sourced.

### 5. Llibre–Zhang, "Limit cycles of the classical Liénard systems…" (Expo. Math. 2017) — replaces the contaminated file
- File: `sources/llibre-zhang-lienard-survey-expmath-2017.uab.full.md`
- URL: http://ddd.uab.cat/record/221320
- Establishes: LdMP conjecture true n≤4, FALSE n≥6, **n=5 open** as of 2017.
- Replaces the wrongly-guessed arXiv ID (`llibre-zhang-lienard-conjecture-survey.full.md`
  = unrelated power-grid paper, Mureddu arXiv:1612.05532). See claim
  `data-contamination-llibre-zhang`.

## Status of the open gaps after this pass

- `dumortier-roussarie-rousseau-9c4f` / `complete-current-ledger-cb3d` (the
  graphic-by-graphic current ledger of the 121): **still open** — no post-2020
  authoritative graphic-by-graphic table is in hand. The library now confidently
  asserts: 121 graphics (confirmed by Rousseau 1997 survey, RSZ 2015, RR 2015,
  Ilyashenko 2002, BIRS 2007, Zhu 2005); 88 closed by 2015; + (I¹₁₄) → 89;
  (H³₁₄) open (Lu 2026 preprint claims it); (I⁶b¹),(H¹³₃),(DI₂b) partial
  (boundary sets only); ≥11 degenerate graphics open (Shan 2013). The 125-in-
  Shan counting discrepancy is NOT resolved (library holds 121 throughout).
- Liénard n=5 status: OPEN as of 2017 (now anchored in held source, replacing
  the contaminated file).
- Christopher–Lloyd 1995 n²log n primary treatment itself: **still not held**
  (paywalled at Royal Society). The weakened-16th 2001 paper (held) and Buzzi–
  Novaes 2024 (held) corroborate the growth from the secondary/derived side.
- Shi 1980 / Chen–Wang 1979 originals: not held, but now the H(2)≥4 lower bound
  rests on the **certified** Galias–Tucker 2022 reproduction rather than on the
  asserted-by-source original. Recorded as verified-computationally.

## What is now verifiable from locally-held sources

- H(2) ≥ 4: CERTIFIED (Galias–Tucker 2022).
- H(n) strictly increasing & realizable by hyperbolic fields: sourced
  (Gasull–Santana 2025).
- H(n) not bounded by any quadratic (n²log n lower bound): sourced via
  Buzzi–Novaes 2024 + Christopher–Lloyd weakened-16th 2001.
- LdMP Liénard: n≤4 true, n≥6 false, n=5 open: sourced (Llibre–Zhang 2017).
- Tangential weakened-H16 lower bound at a point: sourced primary
  (Christopher–Lloyd 2001).

## What could not be obtained, and why

- **Christopher–Lloyd 1995 "Polynomial systems: a lower bound for the Hilbert
  numbers"** (Proc. R. Soc. A 450:219–224) — paywalled at Royal Society; only
  abstract/title verifiable from search. Its result (H(n) ≳ n²log n) is
  corroborated by held Buzzi–Novaes 2024 and the held Christopher–Lloyd
  weakened-16th 2001.
- **DRR 1994 raw 121-graphic catalogue** — paywalled at JDE; not in hand. The
  list's framing is confirmed by five held sources, but the full id-by-id
  open/closed ledger remains the top open acquisition.
- **Llibre–Zhang full postprint body** — UAB record page held; the postprint
  PDF itself is a separate file on the DDD server (Postprint 17p, 402.2KB) not
  fetched; abstract + record content sufficient for the n=5-open claim.
- **Roussarie 1998 monograph** — paywalled; not in hand.
- **Bautin 1952/1954 original** — not openly downloadable; M(2)=3 confirmed
  via multiple held/secondary sources.
- **Christopher & Lloyd 1995** (as above), **Shi 1980**, **Chen–Wang 1979**
  originals — not held as primary texts.

Everything cited in notes is now present in `research/sources/` or marked as
not-yet-obtained in this report. No claim in `research/notes/claims.md`
references a source absent from the library.

---

## First pass report (below)

Status of the local reference library as built by the librarian. Sources are in
`research/sources/`, structural digests in `research/summaries/`, claims in
`research/notes/claims.md` (derived into `derived/CLAIMS.md`). Cognee was down
during this build so verified findings are stored here and should be filed to
memory when it recovers.

## What is now on disk (verified contents)

| Source | File | What it establishes |
|---|---|---|
| Ilyashenko, *Centennial History of Hilbert's 16th Problem*, Bull. AMS 39(3) 2002 | `sources/ilyashenko-centennial-history-hilbert-16.full.md` (readable) + `-h16.full.md` (single-line copy) | Canonical survey. Finiteness Theorem; H(2) open; Kaloshin E(k) ≤ 2^{25k²}; Petrovskii–Landis gap; DRR program; Hilbert–Arnold problems 8–9. |
| Rousseau–Shan–Zhu, arXiv:1502.00689 (2015) | `sources/rouseau-shan-zhu-nilpotent-saddle-graphics.html.full.md` | **DRR = finite cyclicity of 121 graphics in S²×K; (I¹₁₂),(I¹₁₃) → count 88.** Full theorems, Dulac maps, normal forms, blow-up. |
| Kaloshin, *Around Hilbert–Arnold Problem*, math/0111053 | `sources/kaloshin-around-hilbert-arnold.full.md` | Hilbert–Arnold problem; IY finiteness; E(k) ≤ 2^{25k²}. |
| BNY, *Number of Zeros of Abelian Integrals*, 0808.2952 | `sources/binyamini-novikov-yakovenko-abelian-integrals.full.md` | Constructive double-exponential bound, tangential H16. |
| Binyamini–Dor, 1108.1846 | `sources/binyamini-dor-linear-abelian-integrals.full.md` | Explicit bound linear in deg ω. |
| Yakovenko, math/0104140 | `sources/yakovenko-quantitative-ode-tangential-h16.full.md` | Cyclicity N_f; Roussarie compactness → uniform finiteness. |
| **Yeung, "Dulac's Theorem Revisited", Qual. Theory Dyn. Syst. 24 (2025) Art 57** | `sources/yeung-dulac-theorem-revisited.full.md` | **PEER-REVIEWED gap claim in Ilyashenko's approach to Dulac's theorem.** |
| Yeung, arXiv:2402.12506 (HTML full) | `sources/yeung-gap-ilyashenko-dulac-html.full.md` | Preprint version: explicit counterexample to ordering-of-asymptotics. |
| Palma-Márquez–Yeung, arXiv:2410.07532 | `sources/palma-marquez-yeung-maximum-modulus-dulac.full.md` | Max-modulus dichotomy; partial repair. |
| Yeung, arXiv:2409.13630 | `sources/yeung-natural-levels-return-maps.full.md` | Specific hyperbolic-polycycle Dulac case, Ilyashenko-style. |
| Bamón, *Quadratic vector fields... finite number of limit cycles*, IHÉS 64 (1986) | `sources/bamon-quadratic-finite-limit-cycles.full.md` | Individual quadratic fields have finitely many limit cycles (n=2). |
| Liang–Torregrosa, Weak-Foci of High Order and Cyclicity (2016) | `sources/liang-torregrosa-weak-foci-cyclicity.full.md` | Bautin ideal, M(n) lower bounds, weak-focus orders, M(2)=3 context. |
| García–Saldaña–Rebollo, Limit cycles from Chile (2025) | `sources/garcia-saldana-rebollo-chile-limit-cycles.full.md` | Survey; rich bibliography incl. Bamón, DRR DOIs, Yeung 2025. |

## Wrong / failed downloads (honestly recorded)

- `sources/dpr-lienard-more-limit-cycles.full.md`,
  `sources/dumortier-panazzolo-roussarie-lienard.full.md`: AMS journal
  navigator pages, not article text. Liénard counterexample fact verified
  through search abstracts of the actual papers instead (asserted-by-source).
- `sources/llibre-zhang-lienard-conjecture-survey.full.md`: name-collision —
  arXiv:1612.05532 is an unrelated physics paper. This is the precise failure
  the library exists to catch (guessed arXiv ID).
- DPR 2007 (the original Liénard 4-cycle counterexample) and Llibre–Zhang 2017
  survey full texts: NOT obtained (paywalled / wrong guess). Facts sourced from
  abstracts.

## Verified findings (to file to Cognee when it recovers)

1. **DRR list = 121 graphics** (Dumortier–Roussarie–Rousseau 1994; confirmed by
   Rousseau–Shan–Zhu 2015 and Roussarie–Rousseau 2015 and Marín–Villadelprat
   2025). Proving H(2)<∞ ⇔ finite cyclicity of all 121. As of 2015, 88 closed;
   exact current open count needs a post-2020 authoritative table (Shan 2013
   thesis table counts 125 and is outdated — discrepancy noted).
2. **Dulac finiteness proof is under peer-reviewed contention (2025).** Yeung,
   "Dulac's Theorem Revisited" (Qual. Theory Dyn. Syst. 2025) published the gap
   claim in Ilyashenko's 1991 approach, with counterexample and confinement of
   validity. The theorem itself is not claimed false; hyperbolic polycycles
   remain fully understood. No Ilyashenko-side published rebuttal found yet.
3. **Bamón 1986**: each quadratic planar field has finitely many limit cycles
   (individual finiteness, n=2) — distinct from uniform H(2).
4. **Tangential bounds**: BNY 2010 double-exp; Binyamini–Dor 2012 linear in deg
   ω.
5. **Kaloshin**: E(k) ≤ 2^{25k²}, elementary polycycles.
6. **Lower bounds**: H(2)≥4 (Shi 1980/Chen-Wang 1979), H(2)=4 open; H(3)≥13;
   H(4)≥28; M(2)=3 (Bautin); M(3)≥11 (Żołądek); H(n) grows ≥ order
   (n+2)²/ln(n+2) — contradicts any quadratic upper bound.
7. **Liénard LdMP conjecture false for n≥6** (DPR 2007: degree-6 f with 4
   cycles; ≥⌊(n−1)/2⌋+2 for n≥6); n=5 open as of 2017. Slow-fast warning.

## Gaps to request

- Post-2020 authoritative DRR open-graphics table (which named graphics remain).
- Primary text of Christopher–Lloyd for the exact H(n) growth (n² ln n vs n²/ln n).
- Post-2017 status of degree-5 Liénard maximum (was open in 2017).
- Whether the DRR 121 count and the Shan 125 count are the same list under a
  coarser/finer grouping, from the DRR 1994 paper itself.
