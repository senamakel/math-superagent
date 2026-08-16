# Current record: published vs preprint — resolution

Answers request `exact-current-published-c8b8`.

## The question
What is the exact current PUBLISHED (not preprint) constant for the union-closed
sets conjecture, and have AHS / Cambie / Liu appeared in journals?

##Resolution (from exa_search on doi/arxiv records)

```claim
id: published-record-c
answers: exact-current-published-c8b8
statement: The best PUBLISHED lower bound for the union-closed sets conjecture
  is ≈ 0.38234, proved by Lei Yu, "Dimension-Free Bounds for the Union-Closed
  Sets Conjecture", Entropy 2023, 25(5). This is the computable form of
  Sawin's dependent-coupling method. The iid-entropy bound (3−√5)/2 ≈ 0.381966
  is the older, separately-published barrier (Alweiss–Huang–Sellke,
  Electron. J. Combin. 31(3):P3.35, 2024, doi:10.37236/12232).
hypotheses: F nonempty union-closed, F ≠ {∅}; constant is fraction of |F|.
holds-here: true
status: sourced
bearing: fixes the record the run must beat and the published/preprint split.
anchor: exa_search on arXiv:2212.00658 (Entropy 2023) and doi:10.37236/12232
```

```claim
id: preprint-status-c
statement: Cambie (arXiv:2212.12500, c≈0.3823455) and Liu (arXiv:2306.08824,
  c≈0.38271 under numerically-verified hypotheses) remain PREPRINTS as of
  search date; Liu has appeared at CISS 2024 (conference) but is not a journal
  paper. Yu's Entropy 2023 paper is the strongest peer-reviewed record.
hypotheses: none beyond the above.
holds-here: true
status: sourced
bearing: prevents the run from citing a preprint constant as the published record.
anchor: exa_search records arXiv:2212.12500 and arXiv:2306.08824 marked "Preprint"
```

## What this means for the run
- The single number to beat in print is **0.38234...** (Yu, Entropy 2023).
- (3−√5)/2 is the **iid-entropy barrier**, not the record: dependent couplings
  (Sawin → Yu/Cambie → Liu) escape it.
- Liu's 0.38271 is conditional on numerically-verified structural hypotheses and
  is not yet the published record; do not cite it as such.
