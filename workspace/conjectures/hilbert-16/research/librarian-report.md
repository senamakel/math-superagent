# Reference library report — Hilbert 16th, limit cycles

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
