# Librarian report — local reference set for the Erdős–Szekeres conjecture

This report confirms the state of the local reference library and lists what is
available on disk with source URLs. The library is **phase-1 complete** (ROOT.md
meets GOAL.md criterion 1): every canonical source, every published upper bound
in its exact form, the lower-bound construction with its realizability, the exact
values, the SAT/order-type/chirotope foundations, and the restricted-class
results are all held as full primary texts or faithful digests. Nothing in this
report is recalled from memory; every file named is on disk.

## Canonical reference tier (the statement, history, names)

| Source | File | URL |
|---|---|---|
| Erdős–Szekeres 1935, "A combinatorial problem in geometry", Compositio Math. 2:463–470 | `sources/erdos-szekeres - A combinatorial problem in geometry - Compositio 1935 full.full.md` | https://www.numdam.org/article/CM_1935__2__463_0.pdf |
| Erdős–Szekeres 1961 (lower-bound construction), "On some extremum problems in elementary geometry", Ann. Univ. Sci. Budapest 3–4:53–62 | `sources/erdos-szekeres-1961-on-some-extremum-problems-elementary-geometry-renyi.pdf.full.md` | https://renyi.hu/~p_erdos/1960-09.pdf |
| Morris & Soltan, ES survey, BAMS 37(4) 437–458 | `sources/morris-soltan - The Erdos-Szekeres problem on points in convex position - survey BAMS 2000.full.md` | https://www.ams.org/journals/bull/2000-37-04/S0273-0979-00-00877-6/ |
| Wikipedia happy-ending / ES-theorem, MathWorld, erdosproblems 107, OEIS A000051 | `sources/wikipedia-happy-ending-problem.full.md`, `wikipedia-erdos-szekeres-theorem.full.md`, `mathworld-happy-end-problem.full.md`, `summaries/oeis_a000051.md` | Wikipedia / MathWorld / erdosproblems.com/107 / oeis.org/A000051 |

The encyclopedic record (erdosproblems 107) confirms the problem is **open with
zero claimed proofs** as of Apr 2026, with Erdős $500 / Graham $1000. Claim
`erdosproblems-107-open`.

## Upper bounds (each exact form, source-backed)

| Bound | Source file | URL |
|---|---|---|
| ES(n) ≤ C(2n-4,n-2)+1 (cups-caps 1935) | `sources/erdos-szekeres - ... 1935` | numdam (above) |
| g(n) ≤ C(2n-4,n-2) (Chung–Graham 1998) | `sources/chung-graham-Forced-convex-n-gons-in-the-plane-1998.full.md` | DOI 10.1007/PL00009353 |
| C(2n-4,n-2)+7-2n (Kleitman–Pachter 1998) | `sources/kleitman-pachter-Finding-convex-sets-among-points-in-the-plane-1998.full.md` | DOI 10.1007/PL00009358 |
| ES(n) ≤ C(2n-5,n-3)+2 (Tóth–Valtr) | `sources/toth-valtr-ES-theorem-upper-bounds-and-related-results.full.md` | arXiv via Tóth index |
| limsup ≤ (7/8)·C(2n-5,n-2) (Norin–Yuditsky 2016) | `sources/norin-yuditsky - ... DCG 2016 full.full.md` | arXiv:1509.03332 |
| ES(n) ≤ 2^{n+6n^{2/3}log n} (Suk, JAMS 2017) | `sources/suk-erdos-szekeres-convex-polygon-problem-arxiv1604.08657.full.md` | arXiv:1604.08657 |
| ES(n) ≤ 2^{n+O(√(n log n))} (Holmsen–Mojarrad–Pach–Tardos) | `sources/holmsen-mojarrad-pach-tardos - Two extensions of the Erdos-Szekeres problem.full.md` | arXiv:1710.11415 |

The two asymptotic bounds (Suk, HMPT) are of the form 2^{n+o(n)} and cannot
settle the exact conjecture; they are recorded as context, not as tools
(`research/ROOT.md` §1.4–1.5).

## Lower bound & exact values

- ES(n) ≥ 2^{n-2}+1 construction (primary 1961), concrete statement in
  `summaries/erdos-szekeres-1961-construction-concrete.md` (claim
  `es1961-construction-held`, answers `full-text-faithful-b96b`).
- Duque–Fabila-Monroy–Hidalgo-Toscano: realizable on integer grid O(n² log³ n),
  `sources/duque-... - correct full.full.md`, arXiv:1602.03075.
- Peters–Szekeres 2006, ES(6)=17 computer proof, `sources/peters-szekeres-17-point-esz-ANZIAM-2006.full.md`, DOI 10.1017/S144618110000300X.
- Marić 2017 formal verification of n=6, `sources/maric - ... full.md`.
- ES(3..6)=3,5,9,17 in claims `es-exact-values`.

## Order types / SAT / oriented matroids (the computational arm's foundations)

- Aichholzer–Aurenhammer–Krasser order-type database ≤ 10: `sources/aichholzer-... 2002 full.full.md`.
- Felsner–Weil 2001 signotopes: `sources/felsner-weil-sweeps-arrangements-signotopes-2001.full.md` (author PDF).
- Bergold–Felsner–Scheucher extension theorem: `sources/bergold-...-extension-theorem-signotopes.full.md`, arXiv:2303.04079.
- Knuth CC systems + Wikipedia CC-system: `sources/knuth-axioms-and-hulls.full.md`, `sources/wikipedia-cc-system.full.md`.
- Balko–Valtr SAT attack (open ENDM 2015 full text): `sources/balko-valtr-A-SAT-attack-on-ES-ENDM2015.full.md`, https://eurocomb2015.w.uib.no/files/2015/08/endm1938.pdf — refutes the strengthened Peters–Szekeres conjecture over ALL abstract colorings (all counterexamples non-pseudolinear, hence NOT counterexamples to the geometric conjecture); verifies the ES-equivalent Conjecture 3.1 over pseudolinear colorings. Claims `balko-valtr-refutes-PS`, `balko-valtr-pseudolinear-verifies`.
- Scheucher SAT higher-dim ES: `sources/scheucher - A SAT Attack ... full.full.md`, arXiv:2105.08406.
- Subercaseaux et al. empty-hexagon Lean: `sources/subercaseaux-et-al - Formal Verification of the Empty Hexagon Number - ITP 2024 full.full.md`.
- Heule–Scheucher h(6)=30: `sources/heule-scheucher - Happy Ending ... 2024 full.full.md`, arXiv:2403.00737.
- SMQH 2025 (no realizable 4-fold 32-pt no-7-gon): `sources/subercaseaux-mackey-qian-heule - Automated Symmetric Constructions - HTML.full.md`, arXiv:2506.00224.
- PointSAT 2026 (h(6,7)=24; 200k abstract 32-pt no-7-gon candidates, none realizable): `sources/krapivin-przybocki-heule - Toward Satisfiability Modulo Realizability - PointSAT HTML.full.md`, arXiv:2607.02958.
- Dumitru 2025 (33-point ES(7) notes): `sources/dumitru-notes-on-33-point-esz-arxiv2512.24061.full.md`, arXiv:2512.24061.
- Koshelev–Koshka SAT/ASP linear subreduction: `sources/koshelev-koshka-SAT-ASP-esz-linear-subreduction-arxiv2604.20120-html.full.md`, arXiv:2604.20120.

## Restricted classes / structural partial results

- Baek–Balko 2025 split k-gons, decomposable: `sources/baek-balko - The Erdos-Szekeres Conjecture Revisited - SoCG 2025 correct.full.md`, DOI 10.4230/LIPIcs.SoCG.2025.13.
- Baek ETV / P(n,4,n): `sources/ETV-on-the-Erdos-Tuza-Valtr-Conjecture.full.md`, arXiv:2206.04260.
- Károlyi–Tóth 2012 forbidden subconfigurations: `sources/karolyi-toth-2012-...springer.full.md`, DOI 10.1007/s00454-012-9424-6.
- Moshkovitz–Shapira integer-partition proof: `sources/moshkovitz-shapira - ... arxiv1206.4001.full.md`.
- Damásdi et al. saturation: `sources/damasdi-... SoCG 2024 full.full.md`, arXiv:2312.01223.
- Pór–Valtr partitioned version: `sources/por-valtr - The Partitioned Version of the Erdos-Szekeres Theorem - DCG 2002.full.md`.
- Bárány–Valtr positive-fraction: `sources/barany-valtr-A-positive-fraction-ES-theorem.full.md`.
- Fox–Pach–Sudakov–Suk monotone paths: `sources/fox-pach-sudakov-suk - ... PLMS 2012.full.md`, arXiv:1105.2097.
- Horton 1983 (empty convex 7-gons, adjacent): `sources/horton-1983-sets-with-no-empty-convex-7-gons.pdf.full.md`.

## Formalisation arm

- Mathlib `erdos_szekeres` is the **monotone-subsequence** result, NOT the planar
  convex-position statement (claim `mathlib-esz-is-monotone-subsequence`). The
  planar statement is not in Mathlib — GOAL 5 must write it from scratch.
- LeanPool ErdősTuzaValtr `CapCup.lean`, kernel-checked caps-and-cups dichotomy
  (claim `leanpool-capcup-ordinal-dichotomy`).

## Gaps — fully audited this cycle

Re-checked the head of the citation frontier and the requests ledger. The
library is complete against the problem; the only known gaps are documented and
**unobtainable in open access**, not missed acquisitions:

- **Baek–Balko JCTA 2026** (DOI 10.1016/j.jcta.2026.106195) journal version —
  the held SoCG 2025 says "proof of Theorem 8 is omitted" (deferred to JCTA
  2026). ScienceDirect 403-confirmed; **no arXiv preprint** exists as of this
  cycle (Baek's arXiv: 2206.04260 ETV held, 2411.19826 Gerver-sofa unrelated).
  Claim `baek-balko-decomposable` stays **asserted-by-source**.
- **SMQH inner-12 configurations** — claimed by SMQH to be the six
  non-realizable configurations shared by all 310M 4-fold-symmetric 32-pt
  no-7-gon solutions, but never published and absent from the public repo
  (claim `smqh-inner12-never-published`). Cannot be recovered without re-running
  the ~1 CPU-year SAT enumeration.
- **Erdős–Tuza–Valtr 1996 "Ramsey-remainder"** primary — paywalled; faithfully
  restated in held Baek and Balko–Valtr. Do not re-search.
- **Károlyi–Solymosi 2005** — not author-hosted; restated in held Károlyi–Tóth 2012.

## Contamination note (do not cite)

Several MIS-DOWNLOAD stubs remain flagged (guessed arXiv IDs that resolved to
wrong papers). Each carries a pointer to the correct held copy. The correct
content is always in the auto-generated canonical `<name>.full.md` sibling.
Never cite the stub files; the library ledger records which are contaminated.

## Indexing & recall

Full texts are indexed via `index_document` (searchable). Durable findings are
stored in Cognee: library inventory, current bounds, exact values, Peters–
Szekeres encoding cost, SMQH/PointSAT frontier results. `research/LIBRARY_LEDGER.md`
is the authoritative on-disk inventory.

## Standing steering

The library is **phase-1 complete**; further acquisition resumes only against a
stated gap in `derived/REQUESTS.md`, and none of the three remaining gaps is
open-access obtainable. The next librarian cycle's only actionable item is to
re-check for a Baek–Balko JCTA 2026 arXiv post or an SMQH inner-12 data release.
