# Library status: what is available locally and where

Cycle summary for the librarian role. All paths are under `/workspace/`.

> **Cycle update (librarian, 2026 — chronology corrections, Ramaré primary source, BKP corrupt-file fix).** This cycle:
> (1) **Ramaré, "On Šnirel'man's Constant" (Ann. Scuola Norm. Sup. Pisa 1995) FULL TEXT** — `research/sources/ramare-on-snirelman-constant-1995-hal-pdf.full.md` from the HAL PDF (hal-02871110v1/file/Article.pdf). This is the primary source for "every even integer is a sum of at most 6 primes" (Schnirelman's constant ≤ 6), which ROOT.md §2.5 cites but previously had no source on disk. **Caveat:** the scan has no text layer — the OCR is garbled — so the theorem statement is corroborated via Tao arXiv:1201.6656 and Deshouillers–Granville–Narkiewicz–Pomerance 1993 rather than read from the scan. The HAL landing page is `research/sources/ramare-on-snirelman-constant-1995-hal.full.md` (metadata only).
> (2) **BKP corrupt-file fixed.** The file `brudern-kaczorowski-perelli-explicit-formulae-averages-goldbach-representations-TAMS-2019.full.md` contains the WRONG paper (Saha's withdrawn arXiv:1802.10562). The true paper — Brüdern–Kaczorowski–Perelli, "Explicit formulae for averages of Goldbach representations", TAMS 372 (2019) 6981–6999 — is **arXiv:1712.00737**, now on disk at `research/sources/bkp-explicit-formulae-averages-goldbach-representations-arxiv-1712.00737.html.full.md` (full text, theorem statement readable in §1) plus the abstract page `...-arxiv-1712.00737.full.md`. The corrupt file is still on disk under its old name; INDEX.md flags it CORRUPT. The theorem: for N ≥ 4, k > 0, G_k(N) = N²/Γ(k+3) − 2A_k(N) + B_k(N) + (lower-order explicit terms), where A_k, B_k are sums over nontrivial zeros of ζ; unconditional, for all k > 0, improving Languasco–Zaccagnini (k > 1) and Goldston–Yang (k = 1 under RH).
> (3) **Exceptional-set chronology corrected** in `research/notes/claims-exceptional-set-and-circle-method.md` (claim `exceptional-set-chronology`) and applied to ROOT.md §4.2: the chain now reads M–V 1975 → Chen–Pan 1980 (Δ>0.01) → Chen 1983 → Chen–Liu 1989 (δ=0.05) → Li 1999 (δ=0.079, E<X^0.921) → Li 2000 (E<X^0.914) → Lu 2010 (E<X^0.879, δ=0.121, best published) → Pintz 2018 preprint (0.72) → Zhao 2025 preprint (0.7). **The "0.079 vs 0.086" discrepancy previously flagged is resolved: they are two different Li papers** (1999 δ=0.079 per Pintz; 2000 exponent 0.914 ⟹ δ=0.086, which is what Kumchev–Tolev/Zhao cite). Also the OpenAlex row "J Chen 1980 (III)" is mislabeled — the (III) paper is Chen–Liu, Chinese Quart. J. Math. 4 (1989) 1–15.
> (4) **Mikawa 1992** "On the exceptional set in Goldbach's problem" (Tsukuba J. Math. 16(2) 513–543) — full text NOT obtained (J-Stage bot-wall); the statement (E(N,H) ≪_A H log^{-A} N for N^{7/48+ε} < H < N) is corroborated by the Languasco 1995 thesis excerpt and recorded in a stub at `research/sources/mikawa-...-full.md` marked NOT A FULL TEXT.
> (5) Memory server was down throughout this cycle (health check timeout on every remember_memory call); findings are recorded in workspace notes instead and should be pushed to Cognee once the memory service recovers.

> **Cycle update (librarian, 2026 — primary sources for verification record and parity survey).** This cycle added:
> (1) **Friedlander–Iwaniec, "Exceptional zeros, sieve parity, Goldbach" (Essential Number Theory 1(1) 13–39, 2022) FULL TEXT** — `research/sources/friedlander-iwaniec-exceptional-zeros-sieve-parity-goldbach-ent-2022-msp.full.md`, from the MSP PDF. This is the dedicated survey of Obstruction A (the parity barrier) and its connection to exceptional zeros of L-functions; the previous on-disk copies were abstract-only pages, and INDEX.md had a ghost row for a non-existent `-fulltext` file (now removed).
> (2) **Oliveira e Silva–Herzog–Pardi, "Empirical verification of the even Goldbach conjecture and computation of prime gaps up to 4·10^18" (Math. Comp. 83(288) 2033–2060, 2014) FULL TEXT** — `research/sources/oliveira-e-silva-herzog-pardi-empirical-verification-even-goldbach-mirror.full.md`, from a mirror at denisevellachemla.eu (AMS page itself 429-rate-limited). This is the primary source for the 4×10^18 verification record, previously held only as the author's project page. Contains the verification-history table (Sinisalo 1993 → Richstein 2001 → OeS–Herzog–Pardi 2012) and the statement "confirmed to be true for all even numbers not larger than 4·10^18".
> (3) **Goldston–Suriajaya, "Note on the Goldbach conjecture and Landau–Siegel zeros" (arXiv:2104.09407)** and **Friedlander–Goldston–Iwaniec–Suriajaya, "Note on a note of Goldston and Suriajaya" (arXiv:2105.09038)** — the weak-HL-Goldbach → no-Siegel-zeros conditional results that ROOT.md §4.6 rests on; previously only secondary sources. Both full texts now on disk.
> (4) Confirmed unobtainable: **Montgomery–Vaughan 1975 machine-readable text** — exhausted matwbn (textless scan), IMPAN CC-BY route (502), bibliotekanauki.pl article+PDF (textless scan), eudml/pldml (textless scan), Scribd (login-wall). The paper exists only as textless scans; the request is now a bibliographic dead end with the statement well-corroborated by Pintz 2018 + Bhowmik–Halupczok + Li 2000 (all on disk).
> Not obtained: Chen 1973 Scientia Sinica original (paywalled at SciEngine; Scribd copy is a login-walled fragment); AMS journal PDFs (rate-limited).

> **Audit (research specialist, 2026).** `research/audit/audit-binary-goldbach-literature-2026.md`
> is an independent audit of the binary Goldbach literature status: verification
> record (4×10^18 confirmed; Daniel 9×10^18, Gosar 6×10^18, GoldbachGPU 10^12
> are unverified, not records), Chen thresholds (BJS exp(exp 32.7) published
> IJNT 2025; solo-Bordignon Bull. AMS exp(36); Runbo Li 1.9728 published Math.
> Reports 2026), exceptional-set exponent (Lu 2010 best published 0.879; Pintz
> 0.72 and Zhao 0.7 preprints; M–V 1975 δ "explicitly calculable but not
> computed"), ternary (Helfgott, does not imply binary), restricted classes
> (Grimmelt–Teräväinen 2025 two-Chen-prime). Corrections applied to
> `research/ROOT.md` and the claims notes; uncertainties recorded in the audit's
> §7.

> **Cycle update (librarian, cycle 2026 — small-gaps, Liouville analogue, restricted classes).** This cycle added 13 full texts and closed two standing gaps:
> (1) **Hongze Li 2000** "The exceptional set of Goldbach numbers (II)", Acta Arith. 92 (2000) 71–88, full text from ICM matwbn aa92/aa9217.pdf — E(x) = O(x^0.914), closing the published-exponent chain Li 1999 (0.921) → Li 2000 (0.914) → Lu 2010 (0.879);
> (2) **Salmensuu 2022** "Goldbach with summands in APs" — the previously-paywalled restricted-class result now on disk via arXiv:2106.00778;
> (3) the **small-gaps-inside-Goldbach** thread: Tsuda (Monatsh. Math. 2025, Ξ ≤ 0.8201), Akeno (arXiv:2508.02769, Ξ ≤ 0.76542; bounded error 2×10^9 via Maynard–Tao), Akeno (arXiv:2606.29559, level of distribution 1/6 for Goldbach primes);
> (4) the **Liouville analogue** thread: Mangerel (arXiv:2404.12117, IMRN 2024 — |L_λ(N)| < N−1 unconditionally), Mangerel (arXiv:2412.17199, GRH-conditional sign-pattern result);
> (5) **Bhowmik–Grimmelt** survey (arXiv:2607.27282, to appear Analysis Mathematica) — exceptional-set survey with a new explicit major-arc formula and a sparse-HL-implies-no-exceptional-zero observation;
> (6) the **average-order/RH-equivalence** thread: Goldston–Suriajaya (arXiv:2110.14250, unconditional Fujii formula), Brüdern–Kaczorowski–Perelli (arXiv:1712.00737, explicit Cesàro–Riesz formula; TAMS 372 (2019) 6981–6999). **CORRECTION (scholar, this pass): the arXiv ID 1802.10562 recorded earlier is wrong — that record is Shubham Saha's withdrawn "Splitting of integer polynomials over fields of prime order", which is what sits in the misnamed file `brudern-kaczorowski-perelli-...TAMS-2019.full.md`. The true BKP paper is at `bkp-explicit-formulae-averages-goldbach-representations-arxiv-1712.00737.full.md` (arXiv:1712.00737), digested with claim `bkp-cesaro-riesz-explicit-formula`.**
> (7) **Matomäki 2008** short-interval exceptional set (Monatsh. Math. 155, 167–189) — **CORRECTION: the file is misnamed `peneva-...`; the article is by Kaisa Matomäki, not Peneva** — and **Cumberbatch 2024** digitally-restricted-sets result (arXiv:2402.07921).
> Not obtained: Montgomery–Vaughan 1975 machine-readable full text (only textless scan exists), Chen 1973 original (paywalled).

## Canonical tier (statement, notation, history)
> (1) the post-2020 record line — Runbo Li 2024 (Chen-count constant 1.9728,
> arXiv:2405.05727v4 + v1 for the 1.253 earlier constant), Lichtman 2023
> (level of distribution 66/107, Goldbach upper bound 3.3907·Π_a(a)),
> Chirre–Hagen 2025 (RH-conditional Goldbach number in (x, x+123·log²x]);
> (2) full text of Friedlander–Iwaniec, "Exceptional zeros, sieve parity,
> Goldbach" (Essential Number Theory 1(1) 13–39, 2022) — the parity survey,
> previously abstract-only; (3) corrected the Chen-count record chain (v1
> proves 1.253, not 1.733); (4) new bibliographic gaps: Lu 2010 and Salmensuu
> 2022 are paywalled with no free full text. All claims recorded in
> `research/notes/claims-post2020-state-of-the-art.md`.

## Canonical tier (statement, notation, history)

| Source | Location |
|--------|----------|
| Encyclopedia of Mathematics, "Goldbach problem" | `research/sources/goldbach-problem-encyclopedia-of-math.full.md` |
| Wikipedia, "Goldbach's conjecture" | `research/sources/goldbach-conjecture-wikipedia.full.md` |
| MathWorld, "Goldbach Conjecture" | `research/sources/goldbach-conjecture-mathworld.full.md` |
| MacTutor, Goldbach biography | `research/sources/goldbach-biography-mactutor.full.md` |
| Wikipedia, "Landau's problems" (Goldbach = Landau's 1st) | `research/sources/landaus-problems-wikipedia.full.md` |

## Primary papers (full text on disk)

- **Hardy–Littlewood 1923**, Partitio Numerorum III (Acta Math. 44, 1–70), full scan OCR'd:
  `research/sources/hardy-littlewood-partitio-numerorum-iii-1923-tsinghua-pdf.full.md`
- **Helfgott 2013**, "The ternary Goldbach conjecture is true":
  `research/sources/helfgott-ternary-goldbach-conjecture-is-true-arxiv-1312.7748.full.md`
- **Helfgott 2012/2013**, Major arcs / Minor arcs:
  `research/sources/helfgott-major-arcs-goldbach-problem-arxiv-1305.2897.full.md`,
  `research/sources/helfgott-minor-arcs-goldbach-problem-arxiv-1205.5252.full.md`
- **Helfgott–Platt 2013**, numerical verification to 8.875×10^30:
  `research/sources/helfgott-platt-numerical-verification-ternary-goldbach-8.875e30-arxiv-1305.3062.full.md`
- **Tao 2012**, every odd n > 1 is sum of ≤ 5 primes:
  `research/sources/tao-every-odd-integer-sum-of-at-most-five-primes-arxiv-1201.6656.full.md`
- **Yamada 2015**, explicit Chen: n > exp(exp 36):
  `research/sources/yamada-explicit-chens-theorem-arxiv-1511.03409.full.md`
- **Bordignon–Johnston–Starichkova 2022/24**, explicit Chen + linear sieve: n > exp(exp 32.7):
  `research/sources/bordignon-johnston-starichkova-explicit-chen-linear-sieve-arxiv-2207.09452.full.md`
- **Pintz 2018 II**, exceptional set, E(X) < X^0.72:
  `research/sources/pintz-explicit-formula-additive-theory-primes-II-exceptional-set-goldbach-arxiv-1804.09084.full.md`
  (and v2, same content)
- **Zhao 2025**, exceptional set E(X) = O(X^{7/10}) (preprint):
  `research/sources/zhao-exceptional-set-goldbach-linnik-constant-arxiv-2511.05631v2-pdf.full.md`
- **Friedlander–Iwaniec 2023**, fiftieth anniversary of Chen's theorem:
  `research/sources/friedlander-iwaniec-fiftieth-anniversary-chen-goldbach-theorem-arxiv-2303.06122.full.md`
- **Matomäki–Merikoski 2021**, Siegel zeros, twin primes, Goldbach:
  `research/sources/matomaki-merikoski-siegel-zeros-twin-primes-goldbach-short-intervals-arxiv-2112.11412.full.md`
- **Grimmelt–Teräväinen 2022**, exceptional set with almost twin primes:
  `research/sources/grimmelt-teravainen-exceptional-set-goldbach-almost-twin-primes-arxiv-2207.08805.full.md`
- **Grimmelt–Teräväinen 2025**, exceptional set with two Chen primes:
  `research/sources/grimmelt-teravainen-exceptional-set-goldbach-two-chen-primes-arxiv-2508.16400.full.md`
- **Hongze Li 2000**, exceptional set of Goldbach numbers (II), E(x) = O(x^0.914):
  `research/sources/li-hongze-exceptional-set-goldbach-numbers-II-acta-arith-92-2000.full.md`
- **Tsuda 2025**, small gaps between Goldbach primes, Ξ ≤ 0.8201:
  `research/sources/tsuda-small-gaps-primes-satisfy-goldbach-equation-monatshefte-2024.full.md`
- **Akeno 2025**, small gaps between Goldbach primes, Ξ ≤ 0.76542:
  `research/sources/akeno-small-gaps-goldbach-primes-arxiv-2508.02769.full.md`
- **Akeno 2026**, level of distribution 1/6 for Goldbach primes:
  `research/sources/akeno-level-of-distribution-goldbach-primes-arxiv-2606.29559.full.md`
- **Mangerel 2024**, Liouville Goldbach-type convolution, |L_λ(N)| < N−1 (IMRN; arXiv:2404.12117):
  `research/sources/mangerel-goldbach-type-problem-liouville-function-arxiv-2404.12117.full.md`
- **Mangerel 2024**, Shusterman sign-patterns under GRH (arXiv:2412.17199):
  `research/sources/mangerel-shusterman-goldbach-sign-patterns-liouville-arxiv-2412.17199.full.md`
- **Salmensuu 2022**, Goldbach with summands in APs (Q. J. Math.; arXiv:2106.00778):
  `research/sources/salmensuu-goldbach-summands-arithmetic-progressions-arxiv-2106.00778.full.md`
- **Cumberbatch 2024**, digitally restricted sets, exceptional set (arXiv:2402.07921):
  `research/sources/cumberbatch-digitally-restricted-sets-goldbach-exceptional-set-arxiv-2402.07921.full.md`
- **Matomäki 2008** [CORRECTED from "Peneva 2008" — file misnamed], exceptional set in short intervals (Monatsh. Math. 155, 167–189):
  `research/sources/peneva-exceptional-set-goldbach-short-intervals-monatshefte-2008.full.md`
- **Goldston–Suriajaya 2023**, unconditional Fujii average formula (arXiv:2110.14250):
  `research/sources/goldston-suriajaya-average-goldbach-representation-formula-fujii-arxiv-2110.14250.full.md`
- **Brüdern–Kaczorowski–Perelli 2019**, explicit Cesàro–Riesz formula (TAMS 372, 6981–6999; arXiv:1712.00737) — **true text is at `bkp-explicit-formulae-averages-goldbach-representations-arxiv-1712.00737.full.md`**; the file named `brudern-kaczorowski-perelli-...TAMS-2019.full.md` is a misnamed download of Saha's withdrawn note (arXiv:1802.10562) and must not be cited:
  `research/sources/bkp-explicit-formulae-averages-goldbach-representations-arxiv-1712.00737.full.md`
- **Bhowmik–Grimmelt**, exceptional-set survey with explicit major arcs (arXiv:2607.27282, to appear Anal. Math.):
  `research/sources/pintz-exceptional-set-goldbach-problem-survey-explicit-major-arcs-arxiv-2607.27282.full.md` (note: filename says Pintz, actual authors are Bhowmik & Grimmelt)
- **Meng 2007**, mean value theorem on the binary Goldbach problem (Monatsh. Math.):
  `research/sources/meng-mean-value-theorem-binary-goldbach-monatshefte-2007.full.md`
- **Platt 2012**, Computing π(x) analytically — π(10^24) unconditionally (arXiv:1203.5712):
  `research/sources/platt-computing-pi-x-analytically-arxiv-1203.5712.full.md`
- **Friedlander–Goldston 1995**, singular series averages / Goldbach in short intervals: abstract-only (Project Euclid paywall stub, no text; not persisted)
- **Johnston–Trudgian 2026**, Linnik–Goldbach, K = 6 under GRH:
  `research/sources/johnston-trudgian-update-linnik-goldbach-romanov-problems-arxiv-2605.17825.full.md`
- **Granville 2007**, refinements of Goldbach / RH equivalence:
  `research/sources/granville-refinements-goldbach-conjecture-GRH-2007.full.md`
- **Yee 2018**, computational history of primes and Riemann zeros:
  `research/sources/yee-computational-history-prime-numbers-riemann-zeros-arxiv-1810.05244.full.md`

## Surveys on disk

- **Kumchev–Tolev 2004**, "An invitation to additive prime number theory":
  `research/sources/kumchev-tolev-invitation-to-additive-prime-number-theory-arxiv-math0412220.full.md`
- **Bhowmik–Halupczok 2020**, "Asymptotics of Goldbach representations" (full text via arXiv:2010.01308):
  `research/sources/bhowmik-halupczok-asymptotics-goldbach-representations-arxiv-2010.01308.full.md`
- **Friedlander–Iwaniec 2022**, "Exceptional zeros, sieve parity, Goldbach" (ENT 1, 13–39): abstract page only
  `research/sources/friedlander-iwaniec-exceptional-zeros-sieve-parity-goldbach-ent-2022.full.md`

## Computational verification

- Oliveira e Silva's project page (the 4×10^18 verification, method, history, contributors):
  `research/sources/oliveira-e-silva-goldbach-verification-page-sweet-ua-pt.full.md`
- The AMS journal PDF is rate-limited (HTTP 429); the author's page + MathSciDoc/BibTeX entries carry the claim.

## Abstract-only / metadata pages (statements corroborated by ≥ 2 on-disk secondary sources)

- Montgomery–Vaughan 1975 (EUDML/PLDML metadata + scan link; textless scan, DOI 502):
  `research/sources/montgomery-vaughan-exceptional-set-goldbach-1975-eudml.full.md`, `-pldml.full.md`
- Chen 1973 original (SciEngine DOI; paywalled): `research/sources/zhang-contribution-jingrun-chen-number-theory-2023.full.md` (anniversary paper) corroborates
- Lu 2010 (J. Number Theory; abstract page): `research/sources/lu-exceptional-set-goldbach-number-jnt-2010.full.md`
- Hongze Li 2000 (Acta Arith 92, abstract; EUDML): `research/sources/...` via search; claim cites it

## Ledgers and deliverables

- **Claims ledger (37 claims, live)**: `derived/CLAIMS.md`; sources `research/notes/claims-verification-and-chen.md` and `research/notes/claims-exceptional-set-and-circle-method.md`
- **Frontier (citation graph)**: `derived/FRONTIER.md` — 41+ leads ranked by citation weight; top: Montgomery–Vaughan scan (4), then Helfgott-major-arcs, computational history, snap-2014 ternary survey, Bauer–Wang AP exceptional set, Li 2000/2010.
- **Requests (open gaps)**: `derived/REQUESTS.md` — full-text-montgomery-6b42, freely-downloadable-copy-17eb (Chen 1973), machine-readable-text-29b2.
- **Phase-1 deliverable**: `research/ROOT.md` — minimal-counterexample structure, verification bound 4×10^18, three settled restricted classes with exact hypotheses, two obstructions stated exactly, failed-approaches table.

## Not obtained (and why)

- Montgomery–Vaughan 1975 full text: only textless scan exists at matwbn (the direct PDF and the webarchive copy both parse with no text layer); DOI route 502. Gap recorded; statement corroborated by Pintz 2018 (on disk) and Bhowmik–Halupczok (on disk). **The value of M–V's δ is not stated in the paper itself** — it is effectively computable but not explicit; the chronology of explicit δ values starts with Chen–Liu 1989 (0.05).
- Chen 1973 original: paywalled at SciEngine; statement corroborated by Zhang 2023 + Yamada 2015 (both on disk). The 1966 Kexue Tongbao announcement is 2 pages (385–386); no free scan found this cycle.
- Oliveira e Silva–Herzog–Pardi journal PDF: AMS rate limit (429); author's page on disk.
- Friedlander–Iwaniec ENT 2022 full text: MSP abstract page only; the arXiv 2303.06122 companion is on disk.
- The 2024/2025 unrefereed "verification beyond 4×10^18" claims (Daniel et al. 9×10^18, Gosar et al. 6×10^18, GoldbachGPU) are NOT treated as established — the refereed record stands at 4×10^18.
- Zhao 2025 E(X)=O(X^0.7) is an unrefereed preprint; marked asserted-by-source, not established.
- Lu 2010 (J. Number Theory 130, 2359–2392, E(X) < X^0.879): paywalled, no arXiv; the best *published* exceptional-set exponent rests on abstract + corroboration from Pintz 2018 and Bhowmik–Halupczok (both on disk).
- The Zenodo "Polynomial correlations of the Liouville function" preprints by Deligiannis (2026, arXiv:2512.01739 / 2010.07924) are single-author, unrefereed, self-described as needing independent verification; NOT library sources — noted as leads only.