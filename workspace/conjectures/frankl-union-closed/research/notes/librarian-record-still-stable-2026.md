# Librarian live re-check — published record still stable (2026-02)

Re-verification of the open request `exact-current-published-c8b8` on this pass.
Method: live arXiv record of Cambie (2212.12500) via the library's own held copy
(`research/sources/cambie-better-bounds-entropy-2022.full.md`, whose first lines
carry the arXiv DOI 10.48550/2212.12500), a dedicated exa search for a Cambie
journal version of 2212.12500, and a fresh 2025–2026 search over new union-closed
constants. Yu and Liu publication status are carried from the prior live-verified
claim `published-record-current-verified` (verified 2025 via arXiv/IEEE records),
not re-checked on this pass.

## What this pass establishes

1. **Cambie (arXiv:2212.12500, c ≈ 0.3823455) remains a preprint.** The held
   arXiv record shows version v2 dated 2025-02-16 (which adds a 2-parameter
   verification in §3.4) and no journal-ref. A dedicated search for a journal
   version returned only the arXiv preprint and aggregator pages; the single
   phrase "later published in a journal" appears in an AI-generated aggregator
   summary (exa's own synthesis), is contradicted by the arXiv record itself,
   and is **not** evidence. No journal version found. The ceiling
   t̂_max = 0.3823455333667 that the run's uc-coupling work clamps to is a
   **preprint** ceiling, exactly as previously recorded.

2. **No new constant since the last audit.** The 2025–2026 live search surfaced
   only: Wakhare "Iterated entropy derivatives" (J. Approx. Theory 2025,
   already held); Ho "Generalization of Boppana's inequality" (arXiv:2601.19327,
   already held); Phan "Entropy approach for a generalization" (arXiv:2412.18622,
   already held); Hachimori–Kashiwabara "Ideal families Lean 4" (arXiv:2504.13454,
   already held); Colbert "Chain conditions" (Order, DOI 10.1007/s11083-025-09717-w,
   already held); and Samotij "Entropy Methods in Combinatorics" (SIAM 2026,
   **paywalled, not held** — a survey, and triage confirmed it does not state a
   new numerical constant for UC). None exceeds ≈ 0.38271 unconditionally.

3. **The record ordering stands**: Gilmer (0.01, arXiv:2211.09055) → iid
   refinements to (3−√5)/2 (AHS EJC 2024 published; Chase–Lovett, Sawin, Pebody
   arXiv) → Sawin dependent-coupling escape → Yu (Entropy 2023, ≈ 0.38234,
   **the published record**) and Cambie (preprint, exact t̂_max ≈ 0.3823455) →
   Liu (CISS 2024 conference only, ≈ 0.38271 conditional). Peer-reviewed state:
   AHS (3−√5)/2 and Yu ≈ 0.38234.

## Claim block

```claim
id: librarian-record-still-stable-2026
statement: As of this pass's live re-check, the published (journal) record for
  the union-closed constant is unchanged: Yu, Entropy 25(5):767 (2023),
  c ≈ 0.38234. Cambie (arXiv:2212.12500) remains an arXiv preprint (v2
  2025-02-16, no journal-ref found; a single aggregator phrase claiming journal
  publication is contradicted by the arXiv record and is not evidence). Liu
  (arXiv:2306.08824, c ≈ 0.38271 conditional) remains conference-only (IEEE
  CISS 2024), not a journal paper. No 2025–2026 source exceeds ≈ 0.38271
  unconditionally. Samotij's SIAM survey "Entropy Methods in Combinatorics"
  (2026) is paywalled and does not state a new constant in its triage.
hypotheses: F nonempty finite union-closed, F ≠ {∅}; constant is a fraction
  of |F|; publication status is per arXiv/IEEE/journal records.
holds-here: yes
status: asserted-by-source (live arXiv record held in library; dedicated
  journal-version search this pass; Yu/Liu status carried from the prior
  live-verified claim published-record-current-verified, 2025)
bearing: closes the open request exact-current-published-c8b8 again with a
  fresh 2026 check; prevents citing Cambie's 0.3823455 or Liu's 0.38271 as the
  published record, and marks the run's t̂_max ceiling as preprint.
anchor: research/notes/librarian-record-still-stable-2026.md
answers: exact-current-published-c8b8
falsifies: if Cambie (2212.12500) or Liu (2306.08824) gains a journal record, or
  a survey/new paper states an unconditionally better published constant, this
  ranking is stale and must be re-checked.
```

## What this pass did not re-verify

- Yu's journal record and Liu's CISS conference status were not re-fetched live;
  they are carried from `published-record-current-verified` (2025).
- Samotij's survey full text is paywalled; only the DOI landing page and
  triage abstracts were read. It is not in the library.

## Error made and corrected this pass

A download of Phan arXiv:2412.18622's abstract page was accepted before the
dedup check recognised the full body already held as
`phan-entropy-generalization-2024.full.md` (different filename → different
dedup key). The duplicate was overwritten with a pointer stub
(`research/sources/phan-entropy-generalization-frankl-2412.18622.full.md`)
directing readers to the canonical copy. Lesson: dedup by arXiv ID, not by
filename, before downloading; arXiv abstract-page downloads of a paper whose
full body is held should be refused.