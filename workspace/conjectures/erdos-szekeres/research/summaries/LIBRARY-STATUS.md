# Reference library status — Erdős–Szekeres run

Librarian report, current state of `research/sources/`. Every verified source has
its URL recorded inside the file. Full texts are never edited; summaries are in
`research/summaries/` and are the scholar's to maintain.

## Latest librarian cycle — completed the Dumitru ES(7) summary (library-gap close)

This cycle verified the two newest arXiv entries in the library are genuine (Dumitru
2512.24061, Koshelev–Koshka 2604.20120 — confirmed against live search; neither is an
invented citation), confirmed all 7 MIS-DOWNLOAD quarantine files have genuine `correct`
siblings, and **closed a library gap**: the Dumitru "Notes on the 33-point Erdős–Szekeres
problem" summary was an unfinished `digest only` template with no claim blocks, despite
being the most recent direct ES(7) attack in the library. I read the full source and wrote
`research/summaries/dumitru-notes-on-33-point-esz-arxiv2512.24061.md` with a claim block
(`dumitru-es7`): ES(7)=33 is STILL OPEN as of Dec 2025; the encoding (triple-orientation +
14-pattern 4-set criterion + convex-layer anchoring, 578,336 vars / 16,670,808 clauses)
proves UNSAT only for anchored subfamilies, not the full 33-point case; the reduced-5-point
relaxation's soundness (relaxed UNSAT ⟹ stronger UNSAT) is the key logical takeaway. The
run's `es-nogon-k7-rung` must treat 32 as the record and 33+ as a would-be refutation
needing independent re-verification. The three standing requests (balko-valtr-attack-baa4,
open-access-full-1e6e, full-text-faithful-b96b) remain answered by held full texts.

## Prior cycle — two adjacent-problem closes + one dead-end close

This cycle: (1) acquired the Balko–Bhore–Martinez-Sandoval–Valtr "k-convex point sets"
(mis-downloaded to an unrelated hep-th paper, then correctly identified; only the abstract
is held — full text paywalled; it is an ADJACENT relaxation of convex position, NOT a
restricted class, so it is context only, filed with a drift-guard claim `balko-bhore-kconvex-abstract`);
(2) closed the standing SMQH inner-12 "gap" as a DEAD END — the six non-realizable inner-12
configurations were never published as data and the automatic-symmetries repo tree (held)
has no 32-point/inner-12 files, so the claim rests on the paper's assertion alone
(`research/summaries/LIBRARIAN-closed-SMQH-inner12-dead-end.md`);
(3) verified the three long-standing requests (balko-valtr-attack-baa4, open-access-full-1e6e,
full-text-faithful-b96b) are all answered by primary full texts on disk with `answers:` claim
blocks — no later run should re-open them; ROOT.md §7 rows 2–3 listing them open are stale.

## Prior cycle — forbidden-order-type restricted class now held in full

Previously the library's most-documented-not-held gap is now closed with **primary
full texts**. Both fill GOAL 1's "restricted classes" arm and the order-type
structural apparatus the run works over:

| Source | File | URL | What it establishes |
|---|---|---|---|
| Károlyi & Tóth, "Erdős–Szekeres Theorem for Point Sets with Forbidden Subconfigurations", DCG 48 (2012) 441–452 | `karolyi-toth-2012-ES-forbidden-subconfigurations-springer.full.md` (+ summary) | https://link.springer.com/article/10.1007/s00454-012-9424-6 | **The fifth restricted class, now primary.** F_𝒯(n) machinery; twin construction T_n (|T_n|=2^n, no 2^n+1 convex pts); separation property ⇒ F_𝒮(2n+1)>2^n (Lemma 3); explicit 𝒜 (triangle+3 near-edge pts) and 𝒫 (pentagon+center) with F_𝒜,F_𝒫(n)>2^{n/2−1} (Thm 1); Erdős–Hajnal property for ℱ_k, 𝒢_{k;l,m} (Thm 4,5); triangular-hull trichotomy Thm 8 (linear ℰ_k / quadratic-to-poly ℱ_k / exponential otherwise). Claims `karolyi-toth-forbidden-exponential-T1`, `karolyi-toth-triangular-trichotomy-T8`, `karolyi-toth-twin-construction`. |
| Goaoc & Welzl, "Convex Hulls of Random Order Types", arXiv:2003.08456 (JACM 2022) | `goaoc-welzl-Convex-Hulls-of-Random-Order-Types-ar5iv.full.md` (+ summary) | https://arxiv.org/abs/2003.08456 (ar5iv full text) | **Order-type forbidden-pattern counting survey.** Average hull of a uniform random simple planar order type is 4+o(1) extreme points (labeled 4−8/(n²−n+2), var<3); sample-concentration of random point sets; Theorem 1.4 (proportion 1−O(1/n) of size-n order types contain a triangle enclosing a convex k-chain — a 'relative of ES'); symmetry-group classification (cyclic Z_k affine / finite subgroups of SO(3) projective) for isomorph rejection. Surveys the Károlyi–Solymosi/Tóth program in §1.3.5. Claims `goaoc-welzl-average-hull-4`, `goaoc-welzl-forbidden-pattern-chain`. |

Both indexed (search_documents reachable), stored in Cognee. The `geza-toth-publications-index.full.md`
beacon is also held for author copies of ES-adjacent papers; its item-[66] link is stale/404.

**Resolved this cycle:** the Károlyi–Tóth 2012 "Blocked" status below is obsolete —
the primary full text is now held. The Károlyi–Solymosi JCTA 2005 companion remains
ScienceDirect-403 (paywalled); its non-explicit F_𝒯(n)>2^{n−2} result is the ancestor
of Károlyi–Tóth Thm 1 and is restated in the now-held 2012 paper.

## Prior cycle — the ETV reformulation & its integer-partition backbone

Two genuinely thin structural angles were covered this cycle: the Erdős–Tuza–Valtr
conjecture (the strengthened form equivalent to the ES conjecture, referenced
throughout the library as "Conjecture 3.1" but never held as its own source), and
the integer-partition machinery that is its exact counting backbone.

| Source | File | URL | What it establishes |
|---|---|---|---|
| Baek, "On the Erdős-Tuza-Valtr Conjecture" (2022) | `ETV-on-the-Erdos-Tuza-Valtr-Conjecture.full.md` (+ summary) | https://arxiv.org/pdf/2206.04260v2 | **ETV conjecture, primary**. N(n,a,b)=Σ_{i=n-b}^{a-2}C(n-2,i); P(n,n,n)=ES and ETV ⟺ ES (Thm 1.5). Proves the FIRST new case since 1935: P(n,4,n), i.e. (n-1 choose 2)+2 points contain a 4-cap or an n-gon. Gives the α-statistic/(α,β)-plane structural machine for a-cap,b-cup-free near-extremal sets. Claims `etv-equivalent-to-es`, `baek-ETV-n4n`, `etv-alpha-statistic-injective`, `baek-interweaved-laced-cups`. A fifth restricted class for ROOT §5. |
| Moshkovitz & Shapira, "Ramsey Theory, Integer Partitions and a New Proof of the Erdős–Szekeres Theorem" (2012, Adv. Math. 2014) | `moshkovitz-shapira - Ramsey theory integer partitions new proof of ES - arxiv1206.4001.full.md` (+ summary) | https://arxiv.org/pdf/1206.4001 | **Exact counting backbone of cups-caps.** N3(q,n)=P_{q-1}(n)+1 (P_d = # d-dim partitions); N3(2,n)=(2n choose n)+1; the EST cups-caps bound g(n,n)≤(2n-4 choose n-2)+1 follows by a Seidenberg-style down-set injectivity. This down-set→partition injectivity is the exact source of Baek's α-statistic and of the run's structural bound |S|≤(a+b-4 choose a-2). Claims `ms-n3q-partition-count`, `ms-esz-downset-injectivity`. |

Both are indexed (search_documents reachable) and their verified findings stored
in Cognee. The stale `/abs/` landing-page capture `on-the-erdos-tuza-valtr-conjecture-arxiv2206.04260.full.md`
was overwritten with a pointer to the proper PDF copy.

### Blocked this cycle (record, not gaps)

**RESOLVED this cycle — the primary full text is now held** at
`sources/karolyi-toth-2012-ES-forbidden-subconfigurations-springer.full.md`
via the Springer article page. The 2005 JCTA companion (Károlyi–Solymosi) is still
ScienceDirect-403; its non-explicit F_𝒯(n)>2^{n−2} result is restated in the held 2012
paper.

## Previous cycle — Lean-formalisation & signotope foundations

Three genuinely thin angles of the library were covered that cycle: the Lean
arm (GOAL 5), the signotope/oriented-matroid backbone of the SAT encoders, and
the Mathlib name ambiguity problem.md flagged but the library had not pinned.

| Source | File | URL | What it establishes |
|---|---|---|---|
| Mathlib `erdos_szekeres` (Wiedijk 100-Theorems #73) | `mathlib-erdos-szekeres-monotone-subsequence-full.md` (+ summary) | https://leanprover-community.github.io/mathlib_docs/wiedijk_100_theorems/ascending_descending_sequences.html | **Mathlib name collision, verified.** The theorem named `erdos_szekeres` in Mathlib is the MONOTONE-SUBSEQUENCE result ((r−1)(s−1)+1), NOT the convex-polygon ES(n)=2^{n−2}+1 this run targets. The planar convex-position statement is NOT in Mathlib and must be written from scratch (GOAL 5). Claim `mathlib-esz-is-monotone-subsequence`. |
| LeanPool ErdosTuzaValtr CapCup.lean | `leanpool-erdostuzavaltr-capcup.lean.full.md` (+ summary) | https://raw.githubusercontent.com/Vilin97/lean-pool/main/LeanPool/ErdosTuzaValtr/Main/CapCup.lean | **Lean 4 cups-and-caps dichotomy, kernel-checked**: \|S\| > C(a+b,a) forces an (a+2)-cap or (b+2)-cup (diagonal induction). This is the ordered-set/ETV flavour, NOT the planar convex-polygon lemma — a name-hygiene and formalisation model for GOAL 5. Claim `leanpool-capcup-ordinal-dichotomy`. |
| Bergold, Felsner, Scheucher 2023, "An extension theorem for signotopes", SoCG 2023 | `bergold-felsner-scheucher-extension-theorem-signotopes.full.md` (+ summary) | https://arxiv.org/abs/2303.04079 | **Rank-3 signotope ↔ pseudoline-arrangement correspondence (Felsner–Weil), stated precisely** — the combinatorial backbone of the run's entire orientation-variable SAT arm. Realizability of a rank-3 signotope is ∃ℝ-complete; a point set is a STRETCHABLE signotope. Claim `signotope-rank3-pseudoline-correspondence`. |

All three are indexed (search_documents reachable) and their verified findings
stored in Cognee (`remember_memory`).

### Blocked this cycle (record, not gaps — alternate sources already held)

- **Felsner–Weil 2001 "Sweeps, arrangements and signotopes"** (Discrete Appl. Math.), the canonical citation for the rank-3 signotope corrrespondence: the FU-Berlin/Refubium host (both `/handle/` and the bitstream PDF) returned connection errors this run, and DOI 10.1016/S0166-218X(00)00232-8 is paywalled. **Not a gap**: the correspondence it proves is restated faithfully in Bergold–Felsner–Scheucher (held, indexed). Do not re-fetch unless a specific statement is needed; record the refubium handle https://refubium.fu-berlin.de/handle/fub188/17838 as the place it would come from.
- **Bergold–Felsner–Scheucher via escholarship DOI 10.5070/c65465668**: 403 Forbidden. arXiv:2303.04079 (held) is the same content; the DROPS LIPIcs PDF (https://drops.dagstuhl.de/storage/00lipics/lipics-vol258-socg2023/...) is the proceedings version if ever needed.

## Background: prior canonical tier (unchanged, still held)

The library's core was already strong before this cycle: ES 1935 & 1961 primary
texts, Morris–Soltan survey, Suk / HMPT / Tóth–Valtr / Norin–Yuditsky upper
bounds, Peters–Szekeres n=6 SAT proof, Marić formal verification, exact values
ES(3..6), Aichholzer order-type database, Balko–Valtr SAT attack, SMQH
(4-fold-symmetric 32-pt no-7-gon), PointSAT (h(6,7)=24), Heule–Scheucher empty
hexagon, Baek–Balko split k-gons, Damásdi saturation, Pór–Valtr partitioned,
Bárány–Valtr positive-fraction, Duque et al. small-integer realization, the SMQH
primary encoder code, and the encyclopedic tier (Wikipedia/MathWorld/
erdosproblems/OEIS). Details in the full prior table below and the individual
summaries.

## Gaps (recorded in REQUESTS.md)

0. **Explicit inner-12 configurations of SMQH.** (Standing open gap — see prior status below.)

| Source | File | URL | What it establishes |
|---|---|---|---|
| Subercaseaux, Mackey, Qian, Heule 2025, "Automated Symmetric Constructions in Discrete Geometry" | `subercaseaux-mackey-qian-heule - Automated Symmetric Constructions - HTML.full.md` (+ 2025.full.md abstract) | https://arxiv.org/abs/2506.00224; code https://github.com/bsubercaseaux/automatic-symmetries | **No realizable 4-fold-symmetric 32-pt no-7-gon set** (claims `smqh-no-realizable-4fold-32-no7gon`, `smqh-dynamic-ordering-axioms`). Full SAT enumeration (~1 CPU-yr, 310,187,713 solutions) shows all share one of 6 non-realizable inner-12 configs. Symmetry-compatible SAT encoding (dynamic ordering, ≈(4/3)n⁴ orientation clauses) + Localizer realizability solver + convex-layer/quadrant symmetry breaking. |
| Krapivin, Przybocki, Heule 2026, "Toward Satisfiability Modulo Realizability" (PointSAT) | `krapivin-przybocki-heule - Toward Satisfiability Modulo Realizability - PointSAT HTML.full.md` | https://arxiv.org/abs/2607.02958; code https://github.com/andrewkrapivin/PointSAT | **h(6,7)=24** (largest set with no 6-hole or 7-gon is 23) — claim `kph-h67-24`. **32-pt no-7-gon search: 200,000 abstract candidates, zero realizable** (claim `kph-32-no7gon-no-realizable-found`) — evidence, not disproof, of ES(7)=33. SAT+Localizer with diversity / nearby-feedback / flippability heuristics (claim `kph-flippability-method`). |

## Canonical reference tier (verified, in library)

| Source | File | URL | What it establishes |
|---|---|---|---|
| Erdős–Szekeres **1961**, "On some extremum problems in elementary geometry", Ann. Univ. Sci. Budapest. Eötvös Sect. Math. 3-4 (1960/61) 53–62 | `erdos-szekeres-1961-on-some-extremum-problems-elementary-geometry-renyi.pdf.full.md` | https://renyi.hu/~p_erdos/1960-09.pdf | **PRIMARY lower-bound construction**: explicit 2^{n-2}-point set with no convex n-gon (S = ⋃_{k=1}^{n-1} S_k, |S_k|=C(n-2,k-1), positive-slope blocks with strict negative-slope bands between, so any convex polygon has ≤ n-1 vertices). The canonical obstruction. **Closes request `full-text-faithful-b96b`.** Concrete summary: `summaries/erdos-szekeres-1961-construction-concrete.md`. |
| Erdős–Szekeres 1935, "A combinatorial problem in geometry", Compositio Math. 2 (1935) 463–470 | `erdos-szekeres - A combinatorial problem in geometry - Compositio 1935 full.full.md` | https://www.numdam.org/article/CM_1935__2__463_0.pdf | Original finiteness theorem, Ramsey proof, cups–caps proof; Esther Klein's 5-points→convex-4 proof; states ES(3)=3, ES(4)=5, Makai's ES(5)=9; CONJECTURE ES(n)=2^{n-2}+1. |
| Erdős–Szekeres problem survey, Morris & Soltan, BAMS 37(4) (2000) 437–458 | `morris-soltan - The Erdos-Szekeres problem on points in convex position - survey BAMS 2000.full.md` | https://www.ams.org/journals/bull/2000-37-04/S0273-0979-00-00877-6/ | Comprehensive survey: f(k,l) cups-caps = C(k+l-4,k-2)+1 tight (Thm 2.5); lower bound N(n) ≥ 2^{n-2}+1 (Thm 2.6, cites ES 1961); Tóth–Valtr bound N(n) ≤ C(2n-5,n-3)+2 (Thm 2.4); ES(5)=9 (Thm 2.7); higher-dim and convex-body generalizations. Has the recursive X_0..X_{n-2} lower-bound construction description. |
| Erdős–Szekeres conjecture, encyclopedic tier | `wikipedia-happy-ending-problem.full.md`, `wikipedia-erdos-szekeres-theorem.full.md`, `mathworld-happy-end-problem.full.md`, `erdosproblems-107-happy-ending-entry.md`, `toth-valtr-note-erdos-szekeres-DIMACS-TR97-31.md` | Wikipedia/MathWorld/erdosproblems.com/107 + DIMACS TR 97-31 | Fixes statement, history (Klein 1931 f(4)=5, Makai f(5)=9), prizes ($500 proof/$100 disproof, $1000 Graham), OEIS A000051 sequence; flags the name ambiguity: the "Erdős–Szekeres theorem" wiki page is the monotone-subsequence result, NOT this conjecture. Tóth–Valtr primary: g(n) ≤ C(2n-5,n-2)+2. |
| Suk 2016/17, "On the Erdős–Szekeres convex polygon problem", JAMS 30(4) (2017) 1047–1053 | `suk-erdos-szekeres-convex-polygon-problem-arxiv1604.08657.full.md` | https://arxiv.org/abs/1604.08657 (JAMS DOI 10.1090/jams/869) | Breakthrough: ES(n) ≤ 2^{n + 6 n^{2/3} log n} for large n, i.e. ES(n)=2^{n+o(n)}. Uses positive-fraction ES theorem (Bárány–Valtr / Pór–Valtr), dense subsets, cup/cap supports. |
| Holmsen–Mojarrad–Pach–Tardos, "Two extensions of the Erdős–Szekeres problem" | `holmsen-mojarrad-pach-tardos - Two extensions of the Erdos-Szekeres problem.full.md` | https://arxiv.org/abs/1710.11415 (JEMS 22 (2020) 3981–3995) | Improves Suk's error term to ES(n) ∈ 2^{n+O(√(n log n))}; generalizes to pseudoline convexity and convex bodies. |
| Peters–Szekeres 2006, "Computer solution to the 17-point Erdős–Szekeres problem", ANZIAM J. 48(2) 151–164 | `peters-szekeres - Computer solution to the 17-point ES problem - ANZIAM full.full.md` | https://doi.org/10.1017/S144618110000300X | Computes n0(6)=16, i.e. ES(6)=17. Full signature-function encoding, 8 convexity relations, algorithm, cost (~3000 GHz-hours). |

## Order types / computational geometry (verified, in library)

| Source | File | URL | What it establishes |
|---|---|---|---|
| Aichholzer, Aurenhammer, Krasser 2002, "Enumerating Order Types for Small Point Sets with Applications", Order 19 (2002) 265–281 | `aichholzer-aurenhammer-krasser - Enumerating order types for small point sets with applications 2002 full.full.md` | https://link.springer.com/article/10.1023/A:1021231927255 | Complete order-type database for n ≤ 10, with realizing point sets in small integer grids. The standard enumeration source for order types. |
| Heule & Scheucher 2024, "Happy Ending: An Empty Hexagon in Every Set of 30 Points" | `heule-scheucher - Happy Ending An Empty Hexagon in Every Set of 30 Points - 2024 full.full.md` | https://arxiv.org/abs/2403.00737 | SAT proof of empty-hexagon number h(6)=30; the model encoding reference for k-hole SAT. |
| Scheucher 2024, "A SAT attack on higher dimensional Erdős–Szekeres numbers and the Empty Hexagon Theorem" | `scheucher - A SAT Attack on Erdos-Szekeres Numbers in Rd and the Empty Hexagon Theorem full.full.md` | https://arxiv.org/abs/2105.08406 | SAT model based on acyclic chirotopes (oriented matroids); g^(3)(7)=13 etc. This is the orientation-variable SAT formulation the run should mirror. |
| Subercaseaux et al. 2024, "Formal Verification of the Empty Hexagon Number", ITP 2024 | `subercaseaux-et-al - Formal Verification of the Empty Hexagon Number - ITP 2024 full.full.md` | https://arxiv.org/abs/2403.17370 | Lean formalization of the empty-hexagon SAT proof and the ES g(6)≤17 encoding; directly relevant to this run's Lean goal and to comparing encodings with Marić. |
| Norin & Yuditsky 2016, "Erdős–Szekeres without induction", DCG 55(4) | `norin-yuditsky - Erdos-Szekeres without induction - DCG 2016 full.full.md` | https://arxiv.org/abs/1509.03332 | Improves limsup of ES(n)/C(2n-5,n-2) to ≤ 7/8; best binomial-form asymptotics. |
| Damásdi, Dong, Scheucher, Zeng 2024, "Saturation results around the Erdős–Szekeres problem", SoCG 2024 | `damasdi-dong-scheucher-zeng - Saturation results around the Erdos-Szekeres problem - SoCG 2024 full.full.md` | https://arxiv.org/abs/2312.01223 | Constructs (7/8)·2^{n-2} saturated sets; proves the ES construction is saturated. Relevant to structural constraints on extremal sets. |
| Baek & Balko 2025, "The Erdős–Szekeres Conjecture Revisited", SoCG 2025 | `baek-balko - The Erdos-Szekeres Conjecture Revisited - SoCG 2025 correct.full.md` | https://doi.org/10.4230/LIPIcs.SoCG.2025.13 | Proves a relaxed "split k-gon" tight threshold 2^{k-2}+1; ES holds for decomposable sets; new 2^{k-2}-point constructions. |
| Dumitru 2025, "Notes on the 33-point Erdős–Szekeres problem" | `dumitru-notes-on-33-point-esz-arxiv2512.24061.full.md` | https://arxiv.org/abs/2512.24061 | Directly targets ES(7)=33. SAT encoding via triple-orientation variables, 4-set convexity criterion, convex-layer anchoring; reports UNSAT certificates for anchored subfamilies and heavy-tailed runtime. The run's live frontier for ES(7). |
| Duque, Fabila-Monroy, Hidalgo-Toscano 2017, "Point Sets with Small Integer Coordinates and with Small Convex Polygons" | `duque-fabila-monroy-hidalgo-toscano - ES construction small integer coordinates - correct full.full.md` | https://arxiv.org/abs/1602.03075 | Realizes the Erdős–Szekeres 1961 lower-bound construction (2^{n-2} points with no convex n-gon) in an integer grid of size O(n² log³ n). This is the exact-coordinate realization GOAL.md needs for n=5,6,7. Partially fills gap `full-text-faithful-b96b`. |
| Balko & Valtr 2015, "A SAT attack on the Erdős–Szekeres conjecture", ENDM 49 (EuroComb 2015) 425–431 | `balko-valtr-A-SAT-attack-on-ES-ENDM2015.full.md` | https://eurocomb2015.w.uib.no/files/2015/08/endm1938.pdf | **Open-access full text** of the SAT attack. Refutes the strengthened Peters–Szekeres conjecture: cES(7)>32, cES(8)>64 over ALL red-blue colorings of K^3_N (all non-pseudolinear / unrealizable, so NOT counterexamples to the geometric conjecture); verifies the ES-equivalent Conjecture 3.1 over pseudolinear colorings (a=4,u=k=7:16; a=4,u=k=8:22). Closes request `balko-valtr-attack-baa4` and `open-access-full-1e6e`. |
| Goodman, Pollack, Sturmfels 1990, "Upper bounds for configurations and polytopes in R^d", DCG | `goodman-pollack-sturmfels - Upper bounds for configurations and polytopes in Rd.full.md` | https://dl.acm.org/doi/10.1007/BF02187696 | Order-type abstraction. ≤ n^{d(d+1)n} realizable order types of simple n-point sets in R^d (≤ n^{6n} in the plane = 32^{192} at n=32). Quantifies why order-type enumeration can never settle ES(7); the mandatory route is SAT over orientation variables. |
| Fox, Pach, Sudakov, Suk 2012, "Erdős–Szekeres-type theorems for monotone paths and convex bodies", PLMS | `fox-pach-sudakov-suk - ES-type theorems for monotone paths and convex bodies - PLMS 2012.full.md` | https://arxiv.org/abs/1105.2097 | The ordered-3-uniform-hypergraph reformulation: ES(n) ≤ C(2n-4,n-2)+1 is exactly N_3(2,n)=C(2n-4,n-2)+1 (monotone-path Ramsey value). This is the theoretical backbone of the orientation-variable SAT encoding. |
| Pór & Valtr 2002, "The Partitioned Version of the ES Theorem", DCG 28 | `por-valtr - The Partitioned Version of the Erdos-Szekeres Theorem - DCG 2002.full.md` | https://link.springer.com/article/10.1007/s00454-002-2894-1 | Any general-position set is almost a bounded union of convex k-clusterings (bounded exception + ≤ c clusterings). Structural constraint on what an extremal 2^{n-2}-point n-gon-free set must look like; strengthens Bárány–Valtr positive-fraction. |

## Interpreting the MIS-DOWNLOAD files

Three files in `sources/` were created earlier by *guessed* arXiv identifiers and
resolved to the wrong paper. Each now carries a `# MIS-DOWNLOAD — DO NOT CITE`
header pointing to the correct copy. They are record, not library:

- `suk - On the Erdos-Szekeres convex polygon problem - JAMS 2017.full.md` (731 B) → correct copy is `suk-erdos-szekeres-convex-polygon-problem-arxiv1604.08657.full.md`
- `peters-szekeres - Computer solution to the 17-point Erdos-Szekeres problem.full.md` (890 B) → correct copy is `peters-szekeres - Computer solution to the 17-point ES problem - ANZIAM full.full.md`
- `baek-balko - The Erdos-Szekeres Conjecture Revisited - SoCG 2025.full.md` (731 B) → correct copy is `... SoCG 2025 correct.full.md`

(The JSTOR and first-Cambridge attempts that were blocked are superseded by the
correct AMS/Cambridge copies above.)

## Gaps (recorded in REQUESTS.md)

0. **Explicit inner-12 configurations of SMQH.** Subercaseaux et al. (arXiv:2506.00224)
   state all 310,187,713 4-fold-symmetric 32-point no-7-gon SAT solutions share one of 6
   non-realizable inner-12 configurations. The paper gives neither coordinates nor orientation
   tables; the GitHub repo (`bsubercaseaux/automatic-symmetries`) may carry them. Extracted, they
   would be a concrete forbidden local structure (an exact restricted class) for 32-point no-7-gon
   sets, and the raw material for a proof of WHY each of the 6 is unrealizable. A genuine open gap:
   the existing claim `smqh-no-realizable-4fold-32-no7gon` records the existence of the 6 but not
   their structure.
1. ~~`full-text-faithful-b96b`~~ — **FILLED.** Full text of Erdős–Szekeres 1961 "On
   some extremum problems in elementary geometry" downloaded from the Erdős archive
   (renyi.hu/~p_erdos/1960-09.pdf) and filed at
   `erdos-szekeres-1961-on-some-extremum-problems-elementary-geometry-renyi.pdf.full.md`;
   construction stated concretely in `summaries/erdos-szekeres-1961-construction-concrete.md`
   with a claim block carrying `answers: full-text-faithful-b96b`. The construction
   can now be built from the primary treatment itself (backed by Duque et al.'s
   small-integer-grid realization for coordinates at n=5,6,7).
2. ~~`balko-valtr-attack-baa4`~~ / ~~`open-access-full-1e6e`~~ — **FILLED.** The open-access EuroComb full text of Balko & Valtr "A SAT attack on the Erdős–Szekeres conjecture" (ENDM 49 (2015) 425–431) is filed at
   `balko-valtr-A-SAT-attack-on-ES-ENDM2015.full.md`
   (https://eurocomb2015.w.uib.no/files/2015/08/endm1938.pdf), with the claim block
   `balko-valtr-refutes-PS` carrying the `answers:` lines for both requests. It refutes
   the STRENGTHENED Peters–Szekeres conjecture (cES(7)>32, cES(8)>64) over ALL red-blue
   colorings of the ordered complete 3-uniform hypergraph on 2^{k-2}+1 vertices — all
   counterexamples non-pseudolinear, hence NOT counterexamples to the geometric ES
   conjecture; orientation-variable SAT encoding and the pseudolinear verification of the
   ES-equivalent Conjecture 3.1 are all in the full text. (The EJC 66 (2017) journal
   version remains paywalled, but the arXiv-equivalent ENDM full text is the primary
   content and is held.)

## Durable findings stored in Cognee

- Peters–Szekeres signature-function encoding, convexity relations, algorithm and
  ~3000 GHz-hour cost (source: ANZIAM paper).
- Current upper bounds (Tóth–Valtr C(2n-5,n-2)+2; Suk 2^{n+o(n)}; HMPT 2^{n+O(√(n log n))}),
  lower bound 2^{n-2}+1, and exact values ES(3..6).
- SMQH 2025: no realizable 4-fold-symmetric 32-pt no-7-gon set (all 310M SAT solutions share 6
  non-realizable inner-12 configs); symmetry-compatible SAT encoding.
- PointSAT 2026: h(6,7)=24 (adjacent 6-hole result, NOT ES(7)); 32-pt no-7-gon search found
  200,000 abstract candidates, none realizable — evidence, not disproof, of ES(7)=33.

## Drift guard (adjacent problems, held for context only, NOT progress on ES(7))

- h(6,7)=24 (PointSAT): an exact value on the simultaneous 6-hole/7-gon avoidance variant. Not ES(7).
- h(6)=30 (Heule–Scheucher): empty-hexagon number. Adjacent.
- Tightly-packed / density-restricted / diameter-restricted convex-position bounds (Valtr, Bukh–Dong,
  Dumitrescu–Tóth): polynomial-growth regimes in restricted settings. Adjacent; do not mistake for
  the unrestricted exponential conjecture.
- ES in higher dimensions (Scheucher, Furukawa) and k-hole numbers: context only.
