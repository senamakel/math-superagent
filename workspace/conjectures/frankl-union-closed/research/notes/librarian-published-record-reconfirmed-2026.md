# Published record reconfirmed — closes request `exact-current-published-c8b8`

Librarian re-check, searching for a published record that has moved past the
library's Sep-2024 audit. Answer: none found. The published/preprint split in
`published-record-c`, `published-status-current`, `preprint-status-c`,
`ahs-published-ejc` and `ahs-published-note` stands.

## What was re-searched and what it established

- Searched Exa (research-paper category) for union-closed lower-bound constants
  published 2024-06 onward. No journal result exceeds ≈0.38234.
- **Yu, "Dimension-Free Bounds…", Entropy 25(5):767 (2023), arXiv:2212.00658**
  remains the strongest *published* constant ≈0.38234. (Full text on disk:
  `research/sources/yu-dimension-free-bounds-2023.full.md`.)
- **Alweiss–Huang–Sellke, "Improved Lower Bound…", Electron. J. Combin.
  31(3):P3.35 (2024), doi:10.37236/12232**: (3−√5)/2 barrier, peer-reviewed —
  the strongest *published iid-entropy* bound. (Full text on disk:
  `research/sources/alweiss-huang-sellke-barrier-2022.full.md`; the EJC record
  itself returned by search: Submitted 2023-07-18, Accepted 2024-07-01,
  Published 2024-09-20.)
- **Liu, "Improving the lower bound via conditionally IID coupling"**, ≈0.38271,
  is confirmed still **not** a journal paper: Hachimori–Kashiwabara
  (arXiv:2504.13454, Lean-formalised ideal-family case) cite it as "58th Annual
  Conference on Information Sciences and Systems (CISS), IEEE, 2024". This
  independently re-confirms the library's existing record that Liu is a
  conference contribution. (Liu full text on disk.)
- **Colbert, "Chain Conditions and Optimal Elements…", Order (2025),
  doi:10.1007/s11083-025-09717-w** (already in the library) surveys the
  post-2022 landscape with the same constants; it restates Bošnjak–Marković's
  `|UF| ≤ 11` and Roberts–Simpson's `|F| ≥ 4q−1`, giving `|F| ≥ 47` from the
  older `q ≥ 12`. The library's ROOT uses **51** via the `q ≥ 13` refinement
  (Vučković–Živković n≤12 case). These are the same bound at two refinement
  levels, not a contradiction.

## Answer block (closes the request)

```claim
id: librarian-published-record-reconfirmed
answers: exact-current-published-c8b8
statement: As of this re-check, the peer-reviewed record for the union-closed
  constant is Yu (Entropy 2023) ≈0.38234; the (3−√5)/2 barrier is separately
  peer-reviewed (AHS, EJC 31(3):P3.35, 2024); Cambie (arXiv:2212.12500) and Liu
  (arXiv:2306.08824, CISS 2024) remain preprints/conference, so the ≈0.38271
  constant is not a published record. No source found moves the record past
  0.38271 unconditionally.
hypotheses: finite nonempty union-closed F ≠ {∅}; constant is fraction of |F|.
holds-here: yes
status: asserted-by-source (live arXiv/journal listings + on-disk full texts)
bearing: confirms the constants the run must beat and the published/preprint
  split; prevents citing Liu's conditional 0.38271 as the record.
anchor: research/sources/yu-dimension-free-bounds-2023.full.md;
  research/sources/alweiss-huang-sellke-barrier-2022.full.md;
  research/sources/liu-conditionally-iid-coupling-2023.full.md;
  research/sources/colbert-chain-conditions-2412.full.md
ceiling: publication-status claim only; a journal issue dated after 2024-09-20
  that publishes Liu/Cambie would supersede this.
```

Note: `answers:` field connects to the requests ledger. `ceiling` states the
falsifier explicitly so a later run knows exactly what would overturn it.
