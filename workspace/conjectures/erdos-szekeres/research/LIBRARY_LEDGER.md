# Library ledger — what is held and what is not

The genuine primary sources are in `research/sources/*.full.md` (or canonical variants)
with readable digests in `research/summaries/*.md`. This inventory records which file
holds which result, and flags the contamination this run introduced and corrected.

## READ THIS FIRST — filename collision due to guessed arXiv identifiers

I twice downloaded a *wrong paper* under a descriptive name because I guessed an arXiv
identifier, then downloaded the *correct* paper to the same path (overwriting) or to a
sibling path. The files below marked MIS-DOWNLOAD hold the wrong paper and must not be
cited. The correct content is held in the file named on each stub.

Because the runtime auto-named some downloads with the canonical filename, the correct
content lives under BOTH a descriptive name I chose and an auto-generated
`<canonical>.full.md` sibling. To avoid double-counting, treat the auto-generated
canonical file as the authoritative full text where a duplicate exists, and the
descriptive-name stub as a pointer.

## Verified genuine sources (correct content)

- **Erdős–Szekeres 1935**, *A combinatorial problem in geometry*, Compositio Math. 2 (1935) 463–470.
  - `sources/erdos-szekeres - A combinatorial problem in geometry - Compositio 1935 full.full.md`; digest `summaries/erdos-szekeres - ... full.md`. Numdam PDF.
  - Proves ES(n) finite two ways (Ramsey; and cups-and-caps giving ES(n) ≤ C(2n-4,n-2)+1 = 4^{n-o(n)}), conjectures ES(n)=2^{n-2}+1; N(3)=3, N(4)=5, E. Makai proved N0(5)=9.
- **Morris–Soltan 2000**, survey, BAMS 37 (2000) 437–458. `sources/morris-soltan - ... full.full.md`; digest `summaries/morris-soltan - ... survey BAMS 2000.md` (indexed). Canonical survey; includes the ES lower-bound construction and the cups/caps lemma f(k,l)=C(k+l-4,k-2)+1.
- **Suk 2017** (arXiv:1604.08657; JAMS 30 (2017) 1047–1053). Authoritative full text: `sources/suk-erdos-szekeres-convex-polygon-problem-arxiv1604.08657.full.md`; digest `summaries/suk-...-arxiv1604.08657.md` and `summaries/suk - ... JAMS 2017.md` (indexed). THEOREM 1.1: ES(n) ≤ 2^{n+6n^{2/3}log n}, i.e. ES(n)=2^{n+o(n)} — breakthrough to right base.
- **Holmsen–Mojarrad–Pach–Tardos 2017**, *Two extensions of the Erdős–Szekeres problem*, arXiv:1710.11415 (JEMS 22 (2020) 3981–3995). `sources/holmsen-mojarrad-pach-tardos - Two extensions ... .full.md`; digest `summaries/holmsen-... .md` (indexed). Strengthens Suk's error term.
- **Szekeres–Peters 2006**, *Computer solution to the 17-point Erdős–Szekeres problem*, ANZIAM J. 48(2) (2006) 151–164, DOI:10.1017/S144618110000300X. Authoritative full text: `sources/peters-szekeres-17-point-esz-ANZIAM-2006.full.md`; digest `summaries/peters-szekeres-17-point-esz-ANZIAM-2006.md` (indexed). Computer proof ES(6)=17 (convex 6-subset among 17 points), signature functions, ~1500 CPU-hours, three independent implementations.
- **Heule–Scheucher 2024**, *Happy Ending: An Empty Hexagon in Every Set of 30 Points*, arXiv:2403.00737. `sources/heule-scheucher - ... 2024 full.full.md`; digest `summaries/heule-scheucher - ... full.md` (indexed). h(6)=30; repro ES(6)=17 in 8.53s via SAT. The model SAT+partitioning (cube-and-conquer) for any ES(7)-type attack.
- **Scheucher**, *A SAT attack on higher dimensional Erdős–Szekeres numbers*, arXiv:2105.08406 (CGT 2022). `sources/scheucher - A SAT Attack ... full.full.md`; digest `summaries/scheucher - ... full.md` (indexed). SAT via acyclic chirotopes: g(3)(7)=13, g(4)(8)≤13, g(5)(9)≤13. The oriented-matroid SAT model.
- **Aichholzer–Aurenhammer–Krasser 2002**, *Enumerating order types for small point sets with applications*, Order 19 (2002) 265–281. `sources/aichholzer-... 2002 full.full.md`; digest `summaries/aichholzer-... full.md` (indexed). Order-type database: all order types up to 11 points (14,309,547 for 10; ~2.3 billion for 11).
- **Baek–Balko 2025**, *The Erdős–Szekeres Conjecture Revisited*, SoCG 2025, DOI:10.4230/LIPIcs.SoCG.2025.13. Authoritative: `sources/baek-balko - The Erdos-Szekeres Conjecture Revisited - SoCG 2025 correct.full.md`; digest `summaries/baek-balko - ... correct.md` (indexed). ES_split(k)=2^{k-2}+1 tight; ES holds for decomposable sets; blow-up constructions.
- **Norin–Yuditsky 2016**, *Erdős–Szekeres without induction*, DCG 55(4) (2016) 963–971, arXiv:1509.03332. `sources/norin-yuditsky - ... full.full.md`; digest `summaries/norin-yuditsky - ... full.md` (indexed). limsup ES(n)/C(2n-5,n-2) ≤ 7/8 (beats Vlachos 29/32). Tóth–Valtr-style potential functions.
- **Damásdi–Dong–Scheucher–Zeng 2024**, *Saturation results around the Erdős–Szekeres problem*, SoCG 2024, arXiv:2312.01223. `sources/damasdi-... full.full.md`; digest `summaries/damasdi-... full.md` (indexed). sat_g(n) ≤ (7/8)·2^{n-2}; proves ES61 construction is n-gon-saturated.
- **Subercaseaux et al. 2024**, *Formal Verification of the Empty Hexagon Number*, ITP 2024, arXiv:2403.17370. `sources/subercaseaux-et-al - ... full.full.md`; digest `summaries/subercaseaux-... full.md` (indexed). Lean formalisation of the SAT encoding; h(6)≤30. Model for this run's Lean goal.
- **Duque–Fabila-Monroy–Hidalgo-Toscano**, *Point Sets with Small Integer Coordinates and with Small Convex Polygons*, arXiv:1602.03075; DCG (2017) DOI:10.1007/s00454-017-9931-6. Authoritative: `sources/duque-... - correct full.full.md`; digest `summaries/duque-... - correct full.md` (indexed). Realizes the ES 1961 construction (n=2^{t-2} points, no convex polygon with > t-1 vertices) on an integer grid of size O(n^2 log^3 n). ESSENTIAL for building the lower-bound construction with exact integer coordinates.
- **Chung–Graham 1998**, *Forced convex n-gons in the plane*, DCG 19(3) (1998) 367–371, DOI:10.1007/PL00009353. `sources/chung-graham-Forced-convex-n-gons-in-the-plane-1998.full.md`; digest `summaries/chung-graham-Forced-convex-n-gons-in-the-plane-1998.md` (indexed). The FIRST improvement to the ES upper bound in 60 years: $g(n) \le \binom{2n-4}{n-2}$ for $n\ge4$ (removes the +1). Introduces the A/B left-right-endpoint directed-cycle + slope-monotonicity method, the seed of the Kleitman–Pachter and Tóth–Valtr refinements. Closes the historical gap between ES 1935 and Tóth–Valtr.
- **Kleitman–Pachter 1998**, *Finding convex sets among points in the plane*, DCG 19(3) (1998) 405–410, DOI:10.1007/PL00009358. `sources/kleitman-pachter-Finding-convex-sets-among-points-in-the-plane-1998.full.md`; digest `summaries/kleitman-pachter-Finding-convex-sets-among-points-in-the-plane-1998.md` (indexed). $g(n) \le \binom{2n-4}{n-2}+7-2n$ via vertical-configuration recurrences and the defective extreme-point device. Second 1998 improvement; completes the historical chain to Tóth–Valtr.

## This cycle's additions (Horton 1983 primary; documented gaps)

- **Horton 1983**, *Sets with No Empty Convex 7-Gons*, Canad. Math. Bull. 26(4) (1983) 482–484. `sources/horton-1983-sets-with-no-empty-convex-7-gons.pdf.full.md` (Cambridge PDF; URL in leading comment); digest `summaries/horton-1983-sets-with-no-empty-convex-7-gons.pdf.md`. Constructs a 2^k-point set S_k={(i,d(i))}, d(i)=Σ a_j c^{j-1}, c=2^k+1, with no empty convex 7-gon; hence the empty-convex-n-gon number g(n) does not exist for n≥7 (g(3)=3, g(4)=5, g(5)=10 Harborth, g(6) open). Claims `horton-no-empty-7gon` (proved), `horton-s-k-construction` (proved). This is the empty-side analogue of the ES 1961 construction — keep strictly separate from the convex-position ES(n) conjecture.
- **Documented-but-not-held** (alternate or none held; recorded per convention):
  - Erdős–Tuza–Valtr 1996, "Ramsey-remainder", EJC 17(6):519–532 (DOI 10.1006/eujc.1996.0045) — canonical primary of the ETV enumeration conjecture. Paywalled; the run's ETV arm reads Baek (arXiv:2206.04260, held) which states the equivalence (Thm 1.5) and proves P(n,4,n). Not a live block.
  - Károlyi–Solymosi 2005, "Erdős–Szekeres theorem with forbidden order types", JCTA 113:455–465 (DOI 10.1016/j.jcta.2005.04.006) — ancestor of held Károlyi–Tóth 2012. ScienceDirect 403 confirmed. Restated in the held 2012 paper. **Author-page check (this cycle):** Solymosi's UBC on-line list (https://personal.math.ubc.ca/~solymosi/publications/publications.html, `sources/solymosi-publications-page.full.md`) lists the paper "to appear" but attaches no hosted PDF; confirmed not author-hosted.

### Later-cycle re-verification (audit; two author-page negatives recorded)

- **Erdős–Tuza–Valtr 1996 "Ramsey-remainder"** — refined: Pavel Valtr's Charles University homepage (https://kam.mff.cuni.cz/~valtr/, contact-only) hosts no PDFs; SZTAKI holds metadata only. Re-confirmed unobtainable in open access. Its content is faithfully restated in held Baek (arXiv:2206.04260) and Balko–Valtr. Do not re-search.
- **Károlyi–Solymosi 2005/6** — refined: re-confirmed not author-hosted (above). Its F_T(n)>2^{n−2} / f_T(N)=Θ(log N) results are restated in the held Károlyi–Tóth 2012 full text. Do not re-search.
- Cycle record: `summaries/LIBRARIAN-THIS-CYCLE-audit-confirmed-unobtainable.md`.

## Previous cycle additions (Lean formalisation & signotope foundations)

- **Mathlib `erdos_szekeres`** (Wiedijk 100-Theorems #73, monotone-subsequence). `sources/mathlib-erdos-szekeres-monotone-subsequence-full.md`; digest `summaries/mathlib-erdos-szekeres-monotone-subsequence.md` (indexed). URL https://leanprover-community.github.io/mathlib_docs/wiedijk_100_theorems/ascending_descending_sequences.html. Confirms the Mathlib name collision: `erdos_szekeres` there is the monotone-subsequence theorem, NOT the convex-polygon ES(n)=2^{n−2}+1. The planar convex-position statement is NOT in Mathlib — GOAL 5 must write it from scratch. Claim `mathlib-esz-is-monotone-subsequence` (checked).
- **LeanPool ErdosTuzaValtr `CapCup.lean`** (Jineon Baek 2026). `sources/leanpool-erdostuzavaltr-capcup.lean.full.md`; digest `summaries/leanpool-erdostuzavaltr-capcup.md` (indexed). URL https://raw.githubusercontent.com/Vilin97/lean-pool/main/LeanPool/ErdosTuzaValtr/Main/CapCup.lean. Kernel-checked Lean 4 caps-and-cups dichotomy |S|>C(a+b,a)→(a+2)-cap or (b+2)-cup; the ordered/ETV flavour, NOT the planar lemma. Formalisation model for the cups-and-caps arm. Claim `leanpool-capcup-ordinal-dichotomy` (checked).
- **Bergold, Felsner, Scheucher 2023**, *An extension theorem for signotopes*, SoCG 2023, arXiv:2303.04079. `sources/bergold-felsner-scheucher-extension-theorem-signotopes.full.md`; digest `summaries/bergold-felsner-scheucher-extension-theorem-signotopes.md` (indexed). URL https://arxiv.org/abs/2303.04079. States precisely the rank-3 signotope ↔ pseudoline-arrangement correspondence (Felsner–Weil) that underpins the run's orientation-variable SAT encoders; realizability of a rank-3 signotope is ∃ℝ-complete. Claim `signotope-rank3-pseudoline-correspondence` (checked).

### Blocked this cycle (record; not a gap — alternate source held in each case)

- Felsner–Weil 2001 "Sweeps, arrangements and signotopes" (Discrete Appl. Math., DOI 10.1016/S0166-218X(00)00232-8): Refubium host (https://refubium.fu-berlin.de/handle/fub188/17838) errored both on the handle page and the bitstream PDF; journal version paywalled. The correspondence it proves is restated faithfully in Bergold–Felsner–Scheucher (held). Do not re-fetch unless a precise statement is needed.
- Bergold–Felsner–Scheucher via escholarship DOI 10.5070/c65465668: 403 Forbidden; arXiv:2303.04079 (held) is the same content. DROPS LIPIcs PDF https://drops.dagstuhl.de/storage/00lipics/lipics-vol258-socg2023/LIPIcs.SoCG.2023.17/LIPIcs.SoCG.2023.17.pdf is the proceedings version if ever needed.

## Documented-but-not-held (no clean open-access full text located this run)

- **Balko–Valtr**, *A SAT attack on the Erdős–Szekeres conjecture*, ENDM 49 (2015) 425–431 (DOI:10.1016/j.endm.2015.06.060) and EJC 66 (2017) 13–23 (DOI:10.1016/j.ejc.2017.06.010). **UPDATE: the open-access EuroComb ENDM full text IS now held** at `sources/balko-valtr-A-SAT-attack-on-ES-ENDM2015.full.md` (https://eurocomb2015.w.uib.no/files/2015/08/endm1938.pdf), which refutes the strengthened Peters–Szekeres conjecture and verifies the ES-equivalent Conjecture 3.1 over pseudolinear colorings. The EJC 66 (2017) journal version remains paywalled but is the same content. Requests `balko-valtr-attack-baa4` and `open-access-full-1e6e` closed. (THIS "not held" note is superseded by LIBRARY-STATUS; kept for record.)

## Contaminated files — DO NOT CITE

- `sources/suk - On the Erdos-Szekeres ... JAMS 2017.full.md` — MIS-DOWNLOAD stub (was RDF paper arXiv 1606.08657). Correct: arXiv 1604.08657.
- `sources/peters-szekeres - Computer solution to the 17-point Erdos-Szekeres problem.full.md` — MIS-DOWNLOAD stub (was Drell-Yan paper arXiv 0707.3042). Correct: ANZIAM PDF.
- `sources/baek-balko - ... SoCG 2025.full.md` — MIS-DOWNLOAD stub (was superfluid-helium paper arXiv 2505.24374). Correct: LIPIcs page.
- `sources/duque-... - Point sets ... 2017 full.full.md` — MIS-DOWNLOAD stub (was microfilament paper arXiv 1708.02181). Correct: arXiv 1602.03075.
- `sources/balko-valtr - ... EJC 2017 full.full.md` — MIS-DOWNLOAD stub (was Segal-Bargmann probability paper arXiv 1601.03182); Balko–Valtr has no arXiv located.
- Correspondingly named `summaries/*` stubs are likewise marked. The Scheucher BFT-replication file was overwritten with correct content.

## LESSON (also stored in memory)
Never guess an arXiv identifier. Download only URLs seen in search results, in
`research/FRONTIER.md`, or inside an already-held source; verify every downloaded digest
matches its intended paper before filing; flag bad files as MIS-DOWNLOAD stubs.
