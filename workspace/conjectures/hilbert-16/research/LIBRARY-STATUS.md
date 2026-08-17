# Reference library status (librarian report)

Built: first pass + second librarian pass. All full texts in `research/sources/`, digests in `research/summaries/`. Source URL recorded inside each document. Cognee memory server was down during these sessions; durable findings are recorded here and in `research/notes/claims.md` until the memory store accepts them.

## Canonical reference tier now in the library (full text)

1. **Yu. Ilyashenko, "Centennial History of Hilbert's 16th Problem", Bull. AMS 39 (2002)**
   - `research/sources/ilyashenko-centennial-history-hilbert-16.full.md`
   - (duplicate short copy: `ilyashenko-centennial-history-h16.full.md`)
   - URL: https://www.ams.org/journals/bull/2002-39-03/S0273-0979-02-00946-1/S0273-0979-02-00946-1.pdf
   - Establishes: Dulac 1923 claimed finiteness, gap found by Ilyashenko 1981-85; Petrovskii–Landis
     claimed H(2)=3, disproved by Novikov–Ilyashenko; quadratic fields with 4 limit cycles [CW],[Shi];
     Finiteness Theorem (E92, I91): polynomial planar field has finitely many limit cycles, and same
     for analytic fields on the 2-sphere; the 121-graphics DRR program (Section 5.2) with ~80 settled by 2002;
     papers [DRR],[DMR],[GR],[RSZ],[DIR] cited as the settlements so far.

2. **C. Rousseau, C. Shan, H. Zhu, "Finite cyclicity of some graphics through a nilpotent point of saddle
   type inside quadratic systems", arXiv:1502.00689 (2015)**
   - `research/sources/rouseau-shan-zhu-nilpotent-saddle-graphics.html.full.md`
   - URL: https://arxiv.org/html/1502.00689v1
   - Establishes: DRR program = prove finite cyclicity of the 121 graphics in S^2 × K; proves (I^1_12),
     (I^1_13) through triple nilpotent saddle; "will bring the number of graphics of the program for which
     finite cyclicity is proved to 88."

3. **G. Binyamini, D. Novikov, S. Yakovenko, "On the Number of Zeros of Abelian Integrals: A Constructive
   Solution of the Infinitesimal Hilbert Sixteenth Problem", Inv. Math. 181 (2010)**
   - `research/sources/binyamini-novikov-yakovenko-abelian-integrals.html.full.md`
   - URL: https://arxiv.org/html/0808.2952v3
   - Establishes: tangential (infinitesimal) H16 solved constructively; bound double exponential in the degree.

4. **V. Kaloshin, "Around Hilbert–Arnold Problem", AIM 2001-24 lecture notes**
   - `research/sources/kaloshin-around-hilbert-arnold.html.full.md`
   - URL: https://arxiv.org/html/math/0111053v1
   - Establishes: weak local Hilbert–Arnold problem; independent proof of Ilyashenko–Yakovenko finiteness;
     a-stratification; Grigoriev–Yakovenko applications.

5. **S. Yakovenko, "Quantitative theory of ordinary differential equations and tangential Hilbert 16th
   problem", arXiv:math/0104140 lecture notes**
   - `research/sources/yakovenko-quantitative-ode.html.full.md`
   - URL: https://arxiv.org/html/math/0104140v3
   - Establishes: surveys zeros of analytic functions defined by ODEs; tangential H16; Petrov elliptic case;
     Gavrilov–Horozov–Iliev bound (at most 2 roots for cubic Hamiltonian with 4 critical values + quadratic form).

6. **M. Yeung, "On the monograph 'Finiteness Theorems for limit cycles' and a special case of alternant
   cycles", arXiv:2402.12506 (2024)**
   - `research/sources/yeung-ilyashenko-finiteness-gap.full.md`
   - URL: https://arxiv.org/html/2402.12506
   - Establishes: a claimed gap in Ilyashenko's proof of Dulac's theorem for non-hyperbolic polycycles:
     the argument that the asymptotics are non-oscillatory is insufficient, with an explicit counterexample.
     Hyperbolic polycycle case stands unquestioned. Confirms only hyperbolic case undisputed.

7. **C. Buzzi, D. Novaes, "A note on a recent attempt to solve the second part of Hilbert's 16th Problem",
   arXiv:2411.09594 (2024)**
   - `research/sources/buzzi-novaes-claim-h16.full.md`
   - URL: https://arxiv.org/pdf/2411.09594
   - Establishes: a proposed solution H(n)=2(n−1)(4(n−1)−2) (Entropy 2024, "information geometry") is
     false: it is quadratic in n and contradicts the established asymptotic lower bound H(n) ~ n² log n.

8. **D. Marín, J. Villadelprat, "The cyclicity of hyperbolic hemicycles", arXiv:2501.16924 (2025)**
   - `research/sources/marin-villadelprat-cyclicity-hyperbolic-hemicycles.full.md`
   - URL: https://arxiv.org/html/2501.16924
   - Establishes: finite cyclicity of a hyperbolic hemicycle in quadratic systems — cyclicity exactly 2
     for a hemicycle in the integrable class QR3 (at least 2 when a0=−1); simultaneous cyclicity 3 for the
     pair of hemicycles in parameter regions K1∖{a0=−1} (resp. 2 in K2); existence of alien limit cycles
     with a new intrinsic definition. Notes Mourtada's unpublished proof of finite cyclicity of any
     hyperbolic polycycle is attributed by some authors ([27], cited in [18, Thm 0]).

8b. **R. Roussarie, C. Rousseau, "Finite cyclicity of some center graphics through a nilpotent point
     inside quadratic systems", Trudy Moskovskogo Mat. Obshch. 76(2):205–248 (2015), arXiv:1506.07104**
   - `research/sources/rousseau-roussarie-center-graphics-nilpotent.full.md`
   - URL: https://arxiv.org/html/1506.07104
   - Establishes: DRR program = prove finite cyclicity of the 121 graphics; introduces blow-up to a
     singular 3D foliation and the Bautin trick (division of the displacement map in a center ideal) to
     prove finite cyclicity of the graphic (I^1_14) and of the boundary limit periodic sets in the
     graphics (I^1_6b), (H^3_13), (DI_2b) through a triple nilpotent point at infinity of saddle, elliptic
     or degenerate type surrounding a center — all except one boundary set.


## Added in second pass (2025, fills documented gaps)

9. **Z. Galias, W. Tucker, "The Songling system has exactly four limit cycles",
   Appl. Math. Comput. 415 (2022) 126691**
   - `research/sources/galias-tucker-songling-four-cycles.full.md`
   - URL: http://www.zet.agh.edu.pl/~galias/ps/amc2022.pdf (open access, CC BY)
   - Establishes: the Songling quadratic system (Shi's 1980 H(2)≥4 example),
     with the three extreme parameter scales, has **exactly** four limit cycles,
     proved by rigorous adaptive-precision interval arithmetic (P-map fixed
     points, explicit positional bounds 10⁻⁷⁵ … 0.04, absence-of-cycle chunks).
     This is a **certified** reproduction of the H(2)≥4 lower bound — exactly
     the oracle shape this run's GOAL.md asks for. Model for the certified
     limit-cycle-counter.

10. **A. Gasull, P. Santana, "A note on Hilbert 16th problem", Proc. AMS
    153(2):669–677 (2025)**, postprint
    - `research/sources/gasull-santana-note-h16-pams-2025.full.md`
    - URL: https://ddd.uab.cat/pub/artpub/2025/309367/GasSan24-Postprint.pdf
    - Establishes: H(n+1) ≥ H(n) + 1 (strictly increasing when finite); H(n)
      realizable by structurally stable fields with only hyperbolic limit
      cycles; H(n) ≤ ℵ₀. Peer-reviewed Proc. AMS 2025. Also recalls the
      Christopher–Lloyd recurrence H(2n+1) ≥ 4H(n).

11. **C. Christopher, N. G. Lloyd, "Polynomial systems: a lower bound for the
    weakened 16th Hilbert problem", Extracta Math. 16(3):441–447 (2001)**, open access
    - `research/sources/christopher-lloyd-weakened-16th-extracta-2001.full.md`
    - URL: https://ddd.uab.cat/pub/artpub/2001/110469/extmat_a2001v16n3p441.pdf
    - Establishes: the primary, open-access statement of the weakened-H16 lower
      bound at one singular point: b_{m,n} ≥ ((n+1)(n+3)/8 − 1) if n ≤ m, else
      ((m+1)(2n−m+3)/8 − 1), for m,n odd; growth of order n².

12. **BIRS 07w5021 workshop report, "Mathematical developments around
    Hilbert's 16th problem" (2007)**
    - `research/sources/birs-workshop-h16-2007-report.full.md`
    - URL: https://www.birs.ca/workshops/2007/07w5021/report07w5021.pdf
    - Establishes: independently confirms the Roussarie compactification →
      121-graphics reduction for H(2)<∞; state-of-tools (Picard–Fuchs,
      Varchenko–Khovanskii) circa 2007.

13. **J. Llibre, X. Zhang, "Limit cycles of the classical Liénard differential
    systems: a survey on the Lins Neto, de Melo and Pugh's conjecture",
    Expo. Math. 35(3):286–299 (2017)**, UAB postprint record
    - `research/sources/llibre-zhang-lienard-survey-expmath-2017.uab.full.md`
    - URL: http://ddd.uab.cat/record/221320
    - **REPLACES the contaminated file** `llibre-zhang-lienard-conjecture-survey.full.md`
      (which was an unrelated power-grid paper, Mureddu arXiv:1612.05532).
      Establishes the correct Liénard-survey anchor: LdMP conjecture true for
      n ≤ 4, FALSE for n ≥ 6, **n=5 OPEN** as of 2017.

## Landing pages (abstract/navigation only, full text not yet obtained)

9. `binyamini-novikov-yakovenko-abelian-integrals.full.md` — arXiv abs page (original file; real text is #3)
10. `kaloshin-around-hilbert-arnold.full.md` — arXiv abs page (original; real text is #4)
11. `yakovenko-quantitative-ode-tangential-h16.full.md` — arXiv abs page (original; real text is #5)
12. `rouseau-shan-zhu-nilpotent-saddle-graphics.full.md` — arXiv abs page (original; real text is #2)
13. `dumortier-roussarie-rousseau-1994-121-graphics.full.md` — UHasselt record page for the DRR 1994 JDE
    paper (title/abstract/DOI 10.1006/jdeq.1994.1061); full text paywalled (JDE).

## Additional research-area sources found by concurrent work in sources/

- `dpr-lienard-more-limit-cycles.full.md` — Dumortier, Panazzolo, Roussarie, "More limit cycles than
  expected in Liénard equations" (Proc. AMS 135 (2007)) — the slow-fast Liénard construction.
- `dumortier-panazzolo-roussarie-lienard.full.md` — same or closely related paper.
- `liang-torregrosa-weak-foci-cyclicity.full.md` — Liang, Torregrosa, cyclicity of weak foci.
- `llibre-zhang-lienard-conjecture-survey.full.md` — survey of the Liénard conjecture.
- `binyamini-dor-linear-abelian-integrals.full.md` — Binyamini, Dor, linear (vs doubly exponential) bound.

## What could not be obtained, and why

- **Dumortier–Roussarie–Rousseau 1994, "Hilbert's 16th problem for quadratic vector fields",
  J. Differential Equations 110:86–133** — the 121-graphics list itself. Paywalled at Academic Press /
  ScienceDirect; UHasselt server holds only the metadata record, no open PDF. The list's content is
  reproduced in the RSZ 2015 paper and the Rousseau survey (Univ. Montréal), which we hold. Recorded as
  request: obtain the graphic-by-graphic list 1..121 with their labels.
- **Roussarie, "Bifurcations of Planar Vector Fields and Hilbert's Sixteenth Problem", Progr. Math. 164,
  Birkhäuser 1998** — the monograph carrying the reduction machinery. Paywalled; no open PDF found.
- **Christopher & Lloyd 1995 lower bound (n² log n)** — paywalled at Royal Society (403); abstract and
  the exact statement (H(n) grows at least as fast as n² log n, and the Han–Li refinement
  liminf H(n)/((n+2)² log(n+2)) ≥ 1/(2 log 2)) are recorded from search results; full text not obtained.
- **Bautin 1952/1954 original** — Russian original + AMS Transl.; not openly downloadable; its result
  (M(2)=3) is confirmed via multiple secondary sources (Cima–Gasull–Mañosas, Gaiko) recorded in searches.
- **Shi Songling 1979-80 / Chen–Wang H(2)≥4 original** — recorded via Ilyashenko's survey [CW],[Shi] and
  secondary sources; primary texts not obtained.

## Status facts established (with exact hypotheses where known)

- H(2) < ∞: OPEN. Equivalent (DRR) to finite cyclicity of each of the 121 graphics.
- Settled count: ~80 by 2002 (Ilyashenko survey); 85 by 2013 (Shan thesis: 125 graphics in a variant
  counting); 88 by 2015 (RSZ: "will bring the number ... to 88"; the two new graphics (I^1_12),(I^1_13));
  contemporaneously Roussarie–Rousseau 2015 closed (I^1_14) and the boundary sets of (I^1_6b),(H^3_13),
  (DI_2b) (all but one boundary set). Post-2015 closures known from search results: DF_{2a} (Huzak 2018),
  and the Marín–Villadelprat hyperbolic-hemicycle result (2025). No consolidated post-2020 count with a
  graphic-by-graphic ledger is in hand.

- Individual finiteness (Dulac's problem): Écalle 1992 + Ilyashenko 1991; Ilyashenko's proof has a claimed
  gap for non-hyperbolic polycycles (Yeung 2024); hyperbolic case undisputed.
- Tangential H16: solved constructively, double-exponential bound (BNY 2010).
- Lower bound H(n) ≳ n² log n (Christopher–Lloyd 1995); H(2)≥4 (Shi; Chen–Wang); H(3)≥13 (Li–Liu–Yang,
  Li–Liu); M(2)=3 (Bautin).
- A 2024 proposed closed form H(n)=2(n−1)(4(n−1)−2) is refuted (Buzzi–Novaes) as it contradicts n² log n.

## Scholar corrections and durable findings (memory server down; recorded here)

1. **Roussarie–Rousseau 2015 — scope correction.** The librarian's entry implied (I¹₁₄), (I¹₆b), (H³₁₃), (DI₂b) were all fully closed. Reading the full text (Theorem 1.1, 1.2, §1): only **(I¹₁₄) has FULL finite cyclicity** proved (Theorem 1.2). For (I¹₆b), (H³₁₃), (DI₂b) only the *boundary limit periodic set* has finite cyclicity (Theorem 1.1); the full finite cyclicity of these three graphics remains OPEN within quadratic systems. This is the single most important status correction.

2. **The 88 count precedes (I¹₁₄).** RSZ 2015 (reads "will bring the number ... to 88" for (I¹₁₂),(I¹₁₃)); RR 2015 then closes (I¹₁₄) as the next one. So the settled count after these two papers is **89 of 121** (88 + I¹₁₄), with I¹₆b, H³₁₃, DI₂b only partially (boundary) done.

3. **Lower-bound asymptotic confirmed & the inversion corrected.** Buzzi–Novaes (2024) full text confirms: H(n) grows at least like (n+2)²log(n+2)/(2 log 2) (Han–Li refinement of Christopher–Lloyd); so H(n) is **NOT bounded above by any quadratic polynomial**. The claims.md prose had this inverted; it is corrected below. A claimed closed form H(n)=2(n−1)(4(n−1)−2) (Entropy 2024) is refuted as quadratic — contradicts the n²log n lower bound — and its alternative "limit cycle" definition (counting singularities of |R| for a Fisher-information curvature) is neither necessary nor sufficient (Buzzi–Novaes give explicit polynomial systems).

4. **Dulac theorem: proof, not theorem, is the contested part.** Yeung 2024 (arXiv:2402.12506, now peer-reviewed 2025 as "Dulac's Theorem Revisited") locates the gap in Ilyashenko's *ordering-of-asymptotics* step for non-hyperbolic (semi-hyperbolic) polycycles, with an explicit counterexample: k₂'k₁−k₁'k₂ ∉ K₁,₁. The hyperbolic case stands unquestioned (Yeung himself: "up to date the only result that has not been questioned"). Écalle's route and the theorem itself are not claimed false.

## Requests still open (see derived/REQUESTS.md)

- `dumortier-roussarie-rousseau-9c4f`: graphic-by-graphic current status of the 121: which exactly remain
  open now, and the paper that settled each recently-closed one. The library now establishes ~88 settled by
  2015 and identifies the post-2015 closures found (DF_{2a}, hemicycles), but no source in hand gives the
  complete ledger with the paper closing each graphic. This is the single most valuable next acquisition.
  **2026 status: CLOSED as a literature question.** No consolidated post-2020 ledger exists in print
  (Rousseau has produced no status survey since 2015; DRR 1994's only complete 121-id list is paywalled
  with metadata only). The best primary per-class ledger is Shan 2013 Table 1.1 (125 graphics; 11
  degenerate open; only (I6a) elementary non-hyperbolic open). The run's inventory is therefore a
  triangulation of RSZ 2015 + RR 2015 + Shan 2013 + closure papers, recorded in `research/drr-list.md`
  (claims `drr-ledger-no-consolidated-post2020`, `drr-shan-2013-table11-ledger`).

## Added in the 2026 librarian pass

14. **C. Shan, "Theory and applications of high codimension bifurcations", PhD thesis, York University
    (2013)** — `research/sources/shan-phd-thesis-2013.full.md` (held)
    — Table 1.1 is the only primary per-class DRR progress ledger: 125 graphics in the standard family,
    11 degenerate open (only DF1a,DF2a done), only (I6a) elementary non-hyperbolic open, 4 RH-graphic
    families proved in the thesis. OCR'd column totals unreliable (claims
    `drr-ledger-no-consolidated-post2020`, `drr-shan-2013-table11-ledger`).

15. **D. Marín, "Fake saddles and their transition maps", EJQTDE 2026 no.5, doi:10.14232/ejqtde.2026.1.5**
    — `research/sources/marin-fake-saddles-transition-maps.full.md` (held; was already in library, summary
    read this pass) — uniform-in-µ transition-map expansion for a fake saddle; corrects
    Coll–Gasull–Prohens 2025; certifies zero cyclicity at a centre. Confirms DMRT 2015 (paywalled) proved
    cyclicity ≤ 2. Anchors the degenerate-graphics thread (`fake-saddle-transition-maps`).

## What could not be obtained, and why (2026 additions)

- **De Maesschalck–Rebollo-Perdomo–Torregrosa 2015, "Cyclicity of a fake saddle inside the quadratic
  vector fields", JDE 258:588–620** — paywalled; the JDE DOI download returned only a "Redirecting" stub
  (`research/sources/demaesschalck-rebollo-torregrosa-fake-saddle-2014.full.md`, 110 bytes). Its cyclicity
  ≤ 2 result is anchored instead via the held Marín 2026 paper and the UAB/MaRDI abstract records.
- **"Limit cycles near hyperbolas in quadratic systems" (JDE 2008, DI2a strip of hyperbolas)** — 403
  Forbidden on ScienceDirect; no open PDF located this cycle.
- **Zhu 2005, "From pp-graphics to the finiteness part of H16 for quadratic systems"** — scanned PDF with
  no text layer; not downloadable. Its content is represented in the held Zhu–Rousseau 2004 paper.
- **DRR 1994 original full text** — re-confirmed paywalled (UHasselt metadata only, MathSciNet MR1275749).
