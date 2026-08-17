# Published-record status — re-verified (live arXiv/IEEE check)

Source URLs for the verification (fetched live via exa_search, not from memory):
- Cambie, arXiv:2212.12500 — https://arxiv.org/html/2212.12500v2 (updated 2025-02-16)
- Liu, arXiv:2306.08824 — https://doi.org/10.1109/ciss59072.2024.10480167
- Yu, Entropy 25(5):767 — https://doi.org/10.3390/e25050767
- Alweiss–Huang–Sellke, EJC 31(3):P3.35 — https://doi.org/10.37236/12232

Answers the open request `exact-current-published-c8b8`: the current PUBLISHED
(journal) record for the constant c in "some element in ≥ c·|F| sets" for
finite union-closed families remains **Yu, Entropy 2023, ≈ 0.38234**. Re-checked
live, nothing has superseded it.

Status of each candidate (verified, not recalled):
- **Cambie (2212.12500, c ≈ 0.3823455)**: still an arXiv PREPRINT. Updated
  2025-02-16 to v2, which adds a 2-parameter (2D) verification in §3.4 but does
  not move it to a journal. The frontier's ceiling t̂_max = 0.3823455334 comes
  from this paper and is what the uc-coupling scorer clamps to.
- **Liu (2306.08824, c ≈ 0.38271, conditionally-IID)**: appeared at the 58th
  IEEE Information Sciences and Systems Conference (CISS 2024, Princeton,
  March 2024), conference proceedings DOI 10.1109/ciss59072.2024.10480167 —
  NOT a journal. The 0.38271 value remains conditional on numerically-verified
  structural hypotheses and unpublished in a journal. One search result labels
  it "journal version" but the DOI is the IEEE conference record; treat as
  conference, not journal.
- **Yu (2212.00658, c ≈ 0.38234)**: published, Entropy 2023, the peer-reviewed
  record.
- **Alweiss–Huang–Sellke (2211.11731, (3−√5)/2)**: peer-reviewed, EJC 31(3)
  P3.35, 2024. This is the iid-entropy bound; established BEFORE Yu's 0.38234.

Order of events that must not be compressed: Gilmer (0.01) → five refinements to
(3−√5)/2 (Nov 2022) → Sawin dependent-coupling shows the iid barrier is escapable
→ Yu (0.38234) and Cambie (0.3823455) make the dependent-coupling improvement
explicit → Liu (0.38271, conditional). The peer-reviewed record is Yu, and the
strongest conditional/unpublished is Liu.

## Claim block

```claim
id: published-record-current-verified
statement: The current PUBLISHED (journal) record for the union-closed constant
  is Yu (Entropy 2023), c ≈ 0.38234. Cambie (2212.12500, c≈0.3823455) remains an
  arXiv preprint (v2 2025-02-16); Liu (2306.08824, c≈0.38271) appeared only at
  the IEEE CISS 2024 conference, not a journal, and its value is conditional on
  numerically-verified hypotheses.
hypotheses: F nonempty finite union-closed, F ≠ {∅}; constant is a fraction of |F|.
holds-here: yes
status: asserted-by-source (live arXiv/IEEE records via exa_search, 2025)
bearing: Confirms and keeps fresh the open request `exact-current-published-c8b8`.
  Prevents citing Liu's conditional 0.38271 or Cambie's 0.3823455 as the
  published record. The run's ceiling (t̂_max ≈ 0.3823455, from Cambie) is a
  preprint ceiling, not a published one.
answers: exact-current-published-c8b8
anchor: research/summaries/published-record-current-verified-2025.md
falsifies: If Cambie or Liu is found published in a journal since this check, or
  if Liu's 0.38271 was retracted, the ranking above is stale.
```
