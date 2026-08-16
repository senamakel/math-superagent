# Librarian library report — reference set for Frankl's union-closed sets conjecture

Session focus: fix the flagged download disease (abstract-page `*.full.md` files),
verify the previously-doubted Yu/Liu optimization sources, and confirm the library
now carries full bodies for every load-bearing primary source.

## The flagged gap, resolved

The lesson claimed `yu-dimension-free-bounds-2023.full.md` and
`liu-conditionally-iid-coupling-2023.full.md` were 6–7KB abstract boilerplate and
that the Yu/Liu optimization formulation was never on disk. **That gap is now
closed and verified.** Both files are full arXiv HTML bodies:

- `research/sources/yu-dimension-free-bounds-2023.full.md` — 46,508 bytes, 376
  lines. Carries Proposition 1 (the cardinality-restricted
  `Γ̂(t) = sup_α inf_{symmetric P_pq} g(P_pq,α)/𝔼h(p)`), the numerical record
  `p_A ≥ 0.38234` at `α=0.035, t=0.38234` with optimizer
  `P_pq=(1−β)Q_{a,a}+βQ_{a,1}`, `a≈0.3300622`, `β≈0.1560676`, `Γ̂≥1.00000889`,
  and Cambie's sharper `0.382345533366702 ≤ t̂_max ≤ 0.382345533366703`.
- `research/sources/liu-conditionally-iid-coupling-2023.full.md` — 67,398 bytes,
  562 lines. Carries Theorem 12 (the 9-dimensional conditionally-IID reduction
  over `(a₁,a₂,q,b₀..b₅)`) and Theorem 13 (value `≈0.382709087918741`, conditional
  on numerically-verified hypotheses).

## Re-fetched to full bodies this pass

Previously abstract-page boilerplate (arxiv.org/pdf/… files ~5–6KB, no proof
body); re-fetched from `arxiv.org/html/<id>`:

| Source | arXiv | Full body (bytes / lines) |
| --- | --- | --- |
| Gilmer | 2211.09055v2 | 33,901 / body with Lemma 1, Theorems 1–2, Conjecture 1 |
| Alweiss–Huang–Sellke | 2211.11731v4 | 37,774 / body with Claim 3, φ*=1/φ, Theorems 1–2 |
| Cambie | 2212.12500v2 | 66,018 / full proof incl. §3.4, the exact 0.382345533366703 |
| Karpas | 1708.01434v1 | 39,409 / large-family |F|≥(1/2−c)2^n, upper-shadow theorems |
| Hu | 1706.06167 | 25,647 / Theorem 1 |A|≥4m−1, Theorem 2 (ε-UC) |
| Ellis–Ivan–Leader | 2201.11484 | 17,975 / Theorem 1 frequency (1+o(1))log₂k/(2k) |
| Maßberg | 1508.05718 | 14,599 / separating families |
| Falgas-Ravry | 1101.2589 | 44,759 / minimal weight 2n |
| Vaughan | math/0208012 | 66,009 / families implying Frankl |
| Marić–Živković–Vučković | 1209.5628 | 44,635 / FC-families |
| Cambie progress survey | 2306.12351 | 31,933 / winter 2022–23 overview |

Chase–Lovett, Pebody, and Boppana full bodies already existed as
`*.html.full.md` (verified: Chase–Lovett carries Theorem 1.3 ψ-optimality,
Boppana carries the full h(x²)≥φ·xh(x) calculus proof). Sawin and Li(u) were
already full.

## Remaining abstract-only, and why that is acceptable

- **Springer paywall lattice papers** (Reinhold lower-semimodular 2000,
  Abe–Nakano modular 1998): the exact theorem statement is in the abstract; the
  proof is behind a paywall we cannot fetch. The result is also confirmed in the
  Bruhn–Schaudt survey full body.
- **Pulaj "Characterizing 3-sets" (Experimental Math 2021)**: paywalled journal
  article; carried as a bibliographic record that points to the three free
  algorithmic sources that ARE full on disk (Morris FC-families, Pulaj cutting
  planes, Pulaj–Wood local configurations).

## Newly recorded finding

With Vučković–Živković's `m ≥ 13` (ground-set of a minimal counterexample),
Hu's Theorem 1 (`|A| ≥ 4m−1`) yields **|F| ≥ 4·13−1 = 51** member sets for a
minimal counterexample — correcting the older `|F| ≥ 47` (which used
Bošnjak–Marković's `m ≥ 12`). Root note `research/ROOT.md` and claim
`verified-m-small` still say 47; the sourced value is 51. Recorded in Cognee.

## What is now available locally

Full bodies (research/sources/*.full.md) and digests (research/summaries/*.md)
covering, with source URLs embedded in each file:

1. **Entropy line (full proofs)**: Gilmer, AHS, Chase–Lovett, Sawin, Pebody,
   Boppana, Yu, Cambie, Liu, Ho (generalized Boppana, Lean), Wakhare,
   Phan, Cambie survey. The whole 2022–23 breakthrough chain is on disk.
2. **Pre-entropy combinatorial line**: Bruhn–Schaudt survey (full 105 KB),
   Balla–Bollobás–Eccles, Balla min-density, Knill, Morris FC-families, Pulaj
   (cutting planes, wood, 3-sets), Eccles, Maßberg, Falgas-Ravry, Vaughan.
3. **Verification**: Bošnjak–Marković (n≤11), Vučković–Živković (n≤12),
   Roberts–Simpson (4q−1, |F|≥47/51), Hu.
4. **Lattice classes**: Poonen (errata), Abe–Nakano, Reinhold, Czédli–Schmidt,
   Joshi–Waphare, Abdollahi–Woodroofe–Zaimi, Bouchard.
5. **Graph formulation**: Bruhn–Charbit–Schaudt–Telle, Nived, Knill,
   Bruhn–Schaudt random bipartite.
6. **Generalizations / structural**: Colbert, Bouchard (generalized UC),
   Carvalho–Machiavelo (supratopologies), Das–Wu (frequent elements),
   Yuster, Lozin–Zamaraev.
7. **Encyclopedic**: Wikipedia entry, West's open-problems page, polymath page.

Every file records its source URL in its first lines. The search index
(`search_documents`) reaches the full texts. The claims ledger (`search_claims`)
holds the extracted claims with hypotheses, holds-here, and evidence class.

## Not obtainable

- Springer proof bodies for Reinhold (2000) and Abe–Nakano (1998) lower/
  modular semimodular lattice papers (paywall). Statements secured;
  proofs available only in the survey's restatement.
- Pulaj 3-sets (Experimental Math) full proof body (paywall); the algorithmic
  content is in the three free companion sources already on disk.
