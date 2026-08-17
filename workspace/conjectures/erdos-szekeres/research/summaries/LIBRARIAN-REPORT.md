# Librarian report — local reference library for the Erdős–Szekeres run

What is available locally in `research/sources/` (full primary texts) and
`research/summaries/` (digests), with source URLs. Everything below is on disk;
nothing cited is a guess.

## Canonical reference tier (the foundational statement, history, names)

| Source | File | URL |
|---|---|---|
| Erdős–Szekeres 1935, "A combinatorial problem in geometry", Compositio Math. 2:463–470 | `sources/erdos-szekeres - A combinatorial problem in geometry - Compositio 1935 full.full.md` | https://www.numdam.org/article/CM_1935__2__463_0.pdf |
| Erdős–Szekeres 1961, "On some extremum problems in elementary geometry", Ann. Univ. Sci. Budapest 3–4:53–62 | `sources/erdos-szekeres-1961-on-some-extremum-problems-elementary-geometry-renyi.pdf.full.md` | https://renyi.hu/~p_erdos/1960-09.pdf |
| Morris & Soltan, ES problem survey, BAMS 37(4) 437–458 | `sources/morris-soltan - The Erdos-Szekeres problem on points in convex position - survey BAMS 2000.full.md` | https://www.ams.org/journals/bull/2000-37-04/S0273-0979-00-00877-6/ |
| Wikipedia happy-ending / ES-theorem, MathWorld, erdosproblems 107, OEIS A000051 | `sources/wikipedia-happy-ending-problem.full.md`, `wikipedia-erdos-szekeres-theorem.full.md`, `mathworld-happy-end-problem.full.md` + OEIS summaries | Wikipedia/MathWorld/erdosproblems.com/107 |

## Upper bounds (each exact form, source-backed)

| Bound | Source file | URL |
|---|---|---|
| ES(n) ≤ C(2n-4,n-2)+1 (cups-caps 1935) | `erdos-szekeres - ... 1935` | numdam |
| g(n) ≤ C(2n-4,n-2) (Chung–Graham 1998, first improvement) | `chung-graham-Forced-convex-n-gons-in-the-plane-1998.full.md` | DOI 10.1007/PL00009353 |
| C(2n-4,n-2)+7-2n (Kleitman–Pachter 1998) | `kleitman-pachter-Finding-convex-sets-among-points-in-the-plane-1998.full.md` | DOI 10.1007/PL00009358 |
| ES(n) ≤ C(2n-5,n-3)+2 (Tóth–Valtr 1998) | `toth-valtr-ES-theorem-upper-bounds-and-related-results.full.md` | arXiv (via Tóth index) |
| limsup ≤ C(2n-5,n-2)·7/8 (Norin–Yuditsky 2016) | `norin-yuditsky - Erdos-Szekeres without induction - DCG 2016 full.full.md` | arXiv:1509.03332 |
| ES(n) ≤ 2^{n + 6n^{2/3}log n} (Suk 2017, JAMS) | `suk-erdos-szekeres-convex-polygon-problem-arxiv1604.08657.full.md` | arXiv:1604.08657 |
| ES(n) ≤ 2^{n+O(√(n log n))} (Holmsen–Mojarrad–Pach–Tardos) | `holmsen-mojarrad-pach-tardos - Two extensions of the Erdos-Szekeres problem.full.md` | arXiv:1710.11415 |

## Lower bound & exact values

- ES(n) ≥ 2^{n-2}+1 construction (primary, 1961) — above.
- Duque–Fabila-Monroy–Hidalgo-Toscano, small integer realization O(n² log³ n): `duque-... - correct full.full.md`, arXiv:1602.03075.
- Peters–Szekeres 2006, ES(6)=17 computer proof: `peters-szekeres ... ANZIAM full.full.md`, DOI 10.1017/S144618110000300X.
- Marić 2017 formal verification of n=6: `maric - Fast Formal Proof ES ... JAR 2017.full.md`.
- ES(3..6)=3,5,9,17 recorded in claims `es-exact-values`.

## Order types / SAT / oriented matroids (the computational arm's foundations)

- Aichholzer–Aurenhammer–Krasser, order-type database ≤10: `aichholzer-... 2002`.
- Felsner–Weil 2001 signotopes: `felsner-weil-sweeps-arrangements-signotopes-2001.full.md` (author PDF).
- Bergold–Felsner–Scheucher extension theorem: `bergold-...-extension-theorem-signotopes.full.md`, arXiv:2303.04079.
- Knuth CC systems + Wikipedia CC-system: `knuth-axioms-and-hulls.full.md`, `wikipedia-cc-system.full.md`.
- Balko–Valtr SAT attack (ENDM 2015 open full text): `balko-valtr-A-SAT-attack-on-ES-ENDM2015.full.md`, https://eurocomb2015.w.uib.no/files/2015/08/endm1938.pdf.
- Scheucher SAT higher-dim ES: `scheucher - A SAT Attack ... full.full.md`, arXiv:2105.08406.
- Subercaseaux et al., empty-hexagon Lean: `subercaseaux-et-al - Formal Verification ... ITP 2024`.
- Heule–Scheucher empty hexagon 30: `heule-scheucher - Happy Ending ... 2024`, arXiv:2403.00737.
- SMQH 2025 (no realizable 4-fold 32-pt no-7-gon): `subercaseaux-mackey-qian-heule - Automated Symmetric ... HTML.full.md`, arXiv:2506.00224.
- PointSAT 2026 (h(6,7)=24; 32-pt no-7-gon, no realizable found): `krapivin-przybocki-heule ... PointSAT HTML.full.md`, arXiv:2607.02958.
- Dumitru 2025, 33-point ES(7): `dumitru-notes-on-33-point-esz-arxiv2512.24061.full.md`, arXiv:2512.24061.
- Koshelev–Koshka SAT/ASP linear subreduction: `koshelev-koshka-SAT-ASP-esz-linear-subreduction-arxiv2604.20120.html.full.md`, arXiv:2604.20120.

## Restricted classes / structural partial results

- Baek–Balko 2025 split k-gons, decomposable: `baek-balko - ... SoCG 2025 correct.full.md`, DOI 10.4230/LIPIcs.SoCG.2025.13.
- Baek ETV / P(n,4,n) first new case: `ETV-on-the-Erdos-Tuza-Valtr-Conjecture.full.md`, arXiv:2206.04260.
- Károlyi–Tóth 2012 forbidden subconfigurations: `karolyi-toth-2012-...springer.full.md`, DOI 10.1007/s00454-012-9424-6.
- Moshkovitz–Shapira integer-partition proof: `moshkovitz-shapira - ... arxiv1206.4001.full.md`.
- Damásdi et al. saturation: `damasdi-... SoCG 2024 full.full.md`, arXiv:2312.01223.
- Pór–Valtr partitioned: `por-valtr - The Partitioned Version ... DCG 2002.full.md`.
- Bárány–Valtr positive-fraction: `barany-valtr-A-positive-fraction-ES-theorem.full.md`.
- Fox–Pach–Sudakov–Suk monotone paths: `fox-pach-sudakov-suk ... PLMS 2012.full.md`, arXiv:1105.2097.
- Jain et al. k-convex sets: `balko-bhore-martinez-sandoval-valtr - ... IWOCA2019` (abstract only).

## **This cycle's addition: Horton 1983 closed**

`research/sources/horton-1983-sets-with-no-empty-convex-7-gons.pdf.full.md` — the
**primary full text** of J. D. Horton, "Sets with No Empty Convex 7-Gons", Canad.
Math. Bull. 26(4) (1983) 482–484, from the Cambridge PDF
(https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0E7C17D71D9FA4A08B265441FBEB32D7/S0008439500065176a.pdf/sets-with-no-empty-convex-7-gons.pdf).

This closes a genuine frontier gap (cited by 4 held sources; previously only
secondary restatements). It establishes: for every k a 2^k-point set
S_k={(i,d(i))}, d(i)=Σ a_j c^{j-1}, c=2^k+1, has no **empty** convex 7-gon, so the
empty-convex-n-gon number g(n) does not exist for n≥7 (g(5)=10 Harborth, g(6)
open). Claims `horton-no-empty-7gon` and `horton-s-k-construction` (both proved)
are in the claims ledger. This is the empty-side analogue of the ES 1961
construction and must remain distinct from the convex-position ES(n) conjecture.

## Newly registered gaps (documented-but-not-held)

- **Erdős–Tuza–Valtr 1996, "Ramsey-remainder", EJC 17(6):519–532** (DOI
  10.1006/eujc.1996.0045) — canonical primary of the ETV enumeration conjecture.
  Paywalled; the run's ETV arm reads Baek (held) which states the equivalence and
  proves P(n,4,n). Not a live block.
- **Károlyi–Solymosi 2005, ES theorem with forbidden order types**, JCTA
  113:455–465 — ancestor of held Károlyi–Tóth 2012. ScienceDirect 403 (confirmed);
  restated in the held 2012 paper.

## Indexing & recall

- Full texts are indexed via `index_document`; the Horton full text is searchable.
- Durable findings stored in Cognee (`remember_memory`): library inventory and the
  Horton acquisition + two claims.
- `research/LIBRARY_LEDGER.md` updated with this cycle's acquisitions and gaps.
- The three requests (`balko-valtr-attack-baa4`, `open-access-full-1e6e`,
  `full-text-faithful-b96b`) are answered by `answers:` claim blocks on disk but
  still render open in `derived/REQUESTS.md` — a re-derivation-state issue, not a
  library gap.

## File hygiene note

The MIS-DOWNLOAD stubs (guessed arXiv IDs that resolved to wrong papers) remain
flagged and must never be cited; each carries a pointer to the correct held copy.
No guessed identifiers were used this cycle — every URL came from a search result
or a held source's own link.
