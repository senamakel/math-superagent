# Librarian cycle 2026c — open request re-verified live; record unchanged; two candidates ruled out of scope

Cycle outcome: the open request `exact-current-published-c8b8` is answered again
from live primary listings (arXiv, MDPI Entropy, EJC, Springer), every anchor
re-confirmed on disk, and the two new-ish 2023–25 candidates found in the
recent window are **ruled out of scope** rather than downloaded — recorded here
so nobody fetches them later.

## 1. The published record, re-verified live (no movement)

Search window: 2024-06 → 2026 (two queries: journal-published constants; arXiv
2025–26 Frankl work). Established, with on-disk anchors:

- **Yu, "Dimension-Free Bounds for the Union-Closed Sets Conjecture", Entropy
  25(5):767 (2023), doi:10.3390/e25050767** (arXiv:2212.00658) — the strongest
  **published** constant, p_A ≥ 0.38234, certified ratio ≥ 1.00000889 at its
  optimizer. Full text on disk: `research/sources/yu-dimension-free-bounds-2023.full.md`.
- **Alweiss–Huang–Sellke, "Improved Lower Bound…", Electron. J. Combin.
  31(3):P3.35 (2024), doi:10.37236/12232** — the (3−√5)/2 ≈ 0.38197 iid-entropy
  barrier, peer-reviewed (submitted 2023-07-18, accepted 2024-07-01, published
  2024-09-20). On disk: `research/sources/alweiss-huang-sellke-barrier-2022.full.md`.
- **Cambie, arXiv:2212.12500**, c ≈ 0.3823455 (exact t̂_max =
  0.382345533366702…), **still a preprint** (latest revision v2, 2025-02-16).
  On disk: `research/sources/cambie-better-bounds-entropy-2022.full.md`.
- **Liu, arXiv:2306.08824**, ≈ 0.382709087918741 under numerically verified
  hypotheses — **still not a journal paper**; has appeared at the 58th Annual
  Conference on Information Sciences and Systems (IEEE CISS 2024). On disk:
  `research/sources/liu-conditionally-iid-coupling-2023.full.md`.
- **Colbert, "Chain Conditions and Optimal Elements…", Order 43:5 (2026),
  doi:10.1007/s11083-025-09717-w** — open access, published 2025-12-08; the
  journal version of the on-disk arXiv preprints. Its survey restates the same
  record and verification ranges (nothing moves). On disk:
  `research/sources/colbert-chain-conditions-order-2025.full.md` plus the two
  arXiv bodies.

Nothing in the window changes the ranking: published record Yu ≈ 0.38234;
conditional preprint record Liu ≈ 0.38271; the (3−√5)/2 value is the barrier
for the *iid-entropy method*, not for the conjecture (Sawin's dependent-coupling
route and its evaluations exceed it).

## 2. Two candidates ruled out of scope (do not re-fetch)

- **Zargar, "The union-closed sets conjecture for non-uniform distributions",
  arXiv:2305.19338** — proves weighted analogues for distributions with
  k_i ≥ 5, 1 ≤ m_i ≤ √k_i (Theorems 1.2–1.3). Frankl's UC is the uniform
  β = 0 / k = m boundary, which is **outside** the theorem's stated range, so
  the paper does **not** imply the conjecture. GOAL.md's rule: a generalisation
  is in scope only if it is easier AND implies a case of UC; neither holds
  here. Not downloaded.
- **Mallik, "New formulations of the union-closed sets conjecture", AMJC 1:5
  (2025?)** — three equivalent reformulations (matrix, graph, hypergraph), no
  new theorem. A reformulation is not a primary treatment of the mathematics
  involved unless it opens a proof; this one is kept only as a frontier lead.

## 3. Library completeness — phase-1 test still passes

- Minimal counterexample: |∪F| ≥ 13 (Vučković–Živković 2017), |F| ≥ 51
  (Roberts–Simpson 4q−1 with q ≥ 13) — claims `verified-n12-comp`,
  `verified-m-small`, `hu-theorem1-4m-minus-1`.
- Verified ranges: n ≤ 12 computer-assisted; |F| ≤ 50 (`bosnjak-markovic-11`,
  `faro-roberts-simpson-40`).
- Settled classes with hypotheses: singleton/2-set trivial; 3-set does not
  force UC (Ellis–Ivan–Leader); lattice classes (modular Abe–Nakano, lower
  semimodular Reinhold, planar/large semimodular Czédli–Schmidt, subgroup
  lattices Abdollahi–Woodroofe–Zaimi); graph classes (Bruhn–Charbit–Schaudt–
  Telle bipartite classes); Lean-4 formalised ideal/preorder classes
  (Hachimori–Kashiwabara, Ho's generalized Boppana).
- Known un-obtainable gap kept: Poonen JCTA 1992 full body is paywalled;
  content covered via errata + survey + Morris/Marić restatements
  (`research/sources/poonen-errata-union-closed-correction.full.md`,
  `poonen-papers-index.full.md`). Not re-requested (content already answered).
- The frontier's most-cited target (Knill math/9409215, cited by 5 of our
  sources) is already on disk: `research/sources/knill-graph-generated-1994.full.md`.

## Answer block (re-answers and closes the open request)

```claim
id: librarian-cycle-2026c-published-record-reverified
answers: exact-current-published-c8b8
statement: Live re-verification (2026 librarian cycle) of the open request: the
  PUBLISHED journal record for the union-closed constant remains Yu, Entropy
  25(5):767 (2023), doi:10.3390/e25050767, p_A >= 0.38234. The (3-sqrt5)/2
  iid-entropy bound is peer-reviewed as Alweiss-Huang-Sellke, EJC
  31(3):P3.35 (2024), doi:10.37236/12232. Cambie (arXiv:2212.12500,
  c ~ 0.3823455, t_hat_max = 0.382345533366702...; latest v2 2025-02-16) and
  Liu (arXiv:2306.08824, ~0.382709087918741 under numerically verified
  hypotheses; IEEE CISS 2024, not a journal) remain non-journal preprints.
  No source dated 2024-06 to 2026 moves the record; the conditional preprint
  record stays Liu ~0.38271. Colbert's journal survey (Order 43:5, 2026,
  open access) independently restates this same record and the verification
  ranges (n <= 12, |F| <= 50).
hypotheses: finite nonempty union-closed F != {emptyset}; constant is fraction of |F|.
holds-here: yes
status: asserted-by-source (live arXiv/MDPI/EJC/Springer listings re-checked this cycle; four full texts on disk)
bearing: pins the constant the run must beat (0.38234 published / 0.38271 conditional), the barrier's exact scope (iid-entropy method, not the conjecture), and the published/preprint split; closes REQUESTS row exact-current-published-c8b8.
anchor: research/sources/yu-dimension-free-bounds-2023.full.md; research/sources/alweiss-huang-sellke-barrier-2022.full.md; research/sources/liu-conditionally-iid-coupling-2023.full.md; research/sources/colbert-chain-conditions-order-2025.full.md
ceiling: a journal issue dated after 2025-12-08 publishing Cambie or Liu
  unconditionally; or a new unconditional record > 0.382709087918741.
```

## Out-of-scope decision block (so nobody re-fetches these)

```claim
id: zargar-nonuniform-excludes-uniform-case
statement: Zargar (arXiv:2305.19338) proves weighted UC analogues for
  distributions with k_i >= 5 and 1 <= m_i <= sqrt(k_i) (Theorems 1.2-1.3);
  Frankl's UC is the uniform (beta = 0, k = m) boundary, which is OUTSIDE the
  stated range, so the paper does not imply Frankl's conjecture. Per
  GOAL.md's generalisation rule it is out of scope. Mallik (AMJC 1:5, new
  reformulations only) is likewise not downloaded; both stay frontier leads.
hypotheses: n/a (scope decision)
holds-here: n/a
status: asserted-by-source (from the abstract and theorem statements)
bearing: stops future cycles downloading these two; the library stays at the
  primary treatments that actually bear on UC.
anchor: (none downloaded; source: arXiv:2305.19338 abstract, AMJC 10.63151/amjc.v1i.5)
ceiling: if either paper is found to imply a case of UC, re-open and download.
```

## Record: memory store attempt failed

The durable Cognee store of this cycle's summary was attempted and rejected by
the memory server ("cannot index right now … accepted and dropped rather than
stored"); the content survives here in this note and in the claims ledger.
A later run with a healthy memory server may re-store it; do not treat the
failed call as silent loss.