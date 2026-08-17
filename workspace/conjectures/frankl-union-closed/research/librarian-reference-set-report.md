# Librarian report — local reference set for Frankl's union-closed sets conjecture

Cycle date: this run. Role: librarian.

## Summary

The local reference library is **complete, indexed, searchable, and provenance-tagged**.
This pass did not download new material — the operator directive `stop-adding-sources`
is in force, and the prior librarian report (`librarian-library-report.md`) plus
CONTEXT.md confirm the library meets the phase-1 test (`research/ROOT.md` states the
minimal-counterexample structure, the verification bound, and settled classes, each tied
to a primary source). This pass re-verified soundness rather than re-gathering.

## What is available locally

Full primary texts: **`research/sources/`** (62 files); short digests:
**`research/summaries/`** (≈120 files). Every downloaded file records its **source URL
in its first lines** (verified below). Search reaches the full texts via
`search_documents` (verified: querying "union-closed sets conjecture best constant
0.38234 Yu entropy" returns Gilmer, AHS, Cambie, Liu, Yu full bodies).

### Canonical / encyclopedia tier (the phase-1 "first download" tier, present)

- **Survey**: Bruhn & Schaudt, "The journey of the union-closed sets conjecture"
  — `bruhn-schaudt-journey-survey-2013-body.full.md`
  (https://arxiv.org/html/1309.3297v2) + official Ulm PDF + abstract variants.
- **Open-problems encyclopedia entry**: D. West, "Union-Closed Sets Conjecture (1979)"
  — `west-open-problems-union-closed.full.md`
  (http://dwest.web.illinois.edu/openp/unionclos.html).
- **Encyclopedic**: Wikipedia entry — `wikipedia-union-closed-sets-conjecture.full.md`;
  Polymath11 page — `polymath-frankl-union-closed.full.md`.
- **Sequence catalogue**: OEIS A102896 (FC-family count) + dozens of sequence records.

### The entropy era — full proofs (the live frontier, 2022–23)

Gilmer (2211.09055), Alweiss–Huang–Sellke (2211.11731, the (3−√5)/2 barrier),
Chase–Lovett (2211.11689, approximate UC & ψ-optimality), Sawin (2211.11504,
dependent-coupling escape), Pebody (2211.13139), Boppana (2301.09664, the
h(x²)≥φxh(x) calculus proof), **Yu** (2212.00658, published record ≈0.38234, Γ̂(t)
formulation and certified optimizer a≈0.3300622, β≈0.1560676), **Cambie** (2212.12500,
the exact 0.382345533366703), **Liu** (2306.08824, 9-dim conditionally-IID coupling,
≈0.38271 conditional), Ho (2601.19327, generalized Boppana in Lean), Wakhare, Phan,
Cambie survey (2306.12351). Each carries the exact theorem statement and proof body.

### Pre-entropy combinatorial line

Bruhn–Schaudt survey (full 105 KB), Balla–Bollobás–Eccles, Balla min-density, Knill,
Morris FC-families, Pulaj (cutting planes, local configurations, 3-sets), Eccles,
Maßberg, Falgas-Ravry, Vaughan, Reimer, Markovic–Bozin, Nagel, Das–Wu.

### Verification / bounds

Bošnjak–Marković (n≤11, EJC 2008), **Vučković–Živković (n=12, computer-assisted)**,
Roberts–Simpson (|F|≥4n−1 → |F|≥51 for a minimal counterexample when n≥13), Hu
(1706.06167), Karpas (1708.01434, |F|≥2^(n−1) → UC), Spence (2026 auditing claimed
proofs), Marić–Živković–Vučković FC-families (1207.3604).

### Lattice classes (Poonen lattice formulation)

Poonen (1992 origin — full text **not obtainable**, see gaps; represented by his own
errata + survey restatement), Abe–Nakano (modular), Reinhold (lower semimodular),
Czédli–Schmidt (planar/large semimodular), Joshi–Waphare (2019), Abdollahi–Woodroofe–Zaimi
(subgroup lattices), Bouchard (2025), Brown (semigroup/Möbius algebra).

### Graph formulation

Bruhn–Charbit–Schaudt–Telle (2015), Nived (2024), Knill, Bruhn–Schaudt random bipartite.

### Generalizations / modern structural

Colbert (chain conditions, Order 2026 open access), Carvalho–Machiavelo (normalized /
supratopologies), Hachimori–Kashiwabara (Lean averaging), Lozin–Zamaraev (Horn functions),
Yuster (almost-k-union-closed), Bhasin (cubical complements), Hu–Shi–Zhou (2025).

## Provenance audit (this pass)

- **60 of 62** source files carry a `<!-- source: <URL> | converted from … -->`
  first-line tag (verified by grep across `research/sources/`).
- The two nontagged files are intentional, both correctly annotated:
  - `phan-entropy-generalization-frankl-2412.18622.full.md` — a **duplicate stub**
    pointing to the canonical `phan-entropy-generalization-2024.full.md`.
  - `eccles-stability-probe.full.md` — a labeled **throwaway** marking a wrong
    download (misdirected probe), with the correct Eccles paper held as
    `eccles-stability-result-2015-*.full.md`. Do not cite the probe.
- `pulaj-characterizing-3-sets-2021.full.md` carries its source inline (DOI
  10.1080/10586458.2021.1927254) plus links to the three free algorithmic companions.
- Spot checks confirmed load-bearing bodies are full, not abstracts: Gilmer
  (33,901 B), Yu (46,508 B, carries Γ̂(t) and the optimizer),
  Vučković–Živković (25,902 B, from the IPSI PDF), Cambie (66,018 B), AHS (37,774 B).

## The one open request — answered by the existing library

`exact-current-published-c8b8` (the published-vs-preprint record split) is settled
and re-verified this cycle per CONTEXT.md directive 15: Yu ≈0.38234 published
(Entropy 25(5):767, 2023); AHS (3−√5)/2 published (EJC 31(3):P3.35, 2024); Cambie
≈0.3823455 and Liu ≈0.38271 remain preprints (Liu at IEEE CISS 2024 only). No
number changed, and the supporting full texts are already on disk — nothing to fetch.

## Not obtainable (recorded, not re-attempted)

- **Poonen, "Union-closed families", JCTA 59:253–268 (1992)** — the origin of the
  lattice formulation and FRONTIER's most-cited work. Paywalled (ScienceDirect 403),
  not on the author's own site, no arXiv version, ar5iv 404. Content represented by
  `poonen-errata-union-closed-correction.full.md` (author's corrections) + survey
  restatement of all formulations + Morris/Marić restatements. Gap in
  `research/notes/poonen-1992-gap-reconfirmed.md`.
- Springer proof bodies for Reinhold (2000) and Abe–Nakano (1998) lattice papers
  (paywall; statements secured, proofs restated in the survey).
- Pulaj "Characterizing 3-sets" full proof body (paywall; algorithmic content in the
  three free companions on disk).

## Recommendation

Phase 1 (build the library) is **finished**. ROOT.md meets the stated test, the
frontier is pinned and reproduced, and every angle CONTEXT.md lists as covered is
covered by a full primary text with an embedded URL. Further gathering should occur
only against a stated gap in `research/REQUESTS.md`; the active work is the
abundance-profile front and the Lean formalisation of the g(n,m) envelope, which the
library fully supports.
