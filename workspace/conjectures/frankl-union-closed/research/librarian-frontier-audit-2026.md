# Librarian frontier audit — 2026-02

Confirming the library is complete and the record stable before pausing.

## What this audit did

- Read `research/ROOT.md` (phase-1 deliverable: minimal-counterexample structure,
  verification bound, settled classes — meets the GOAL.md phase-1 bar).
- Read the one open request (`exact-current-published-c8b8`) and checked it
  against the claim store: answered by `published-status-current`,
  `ahs-published-ejc`, `preprint-status-c`, `liu-conditionally-iid`, `daswu-record-0-3823455`.
- Read the frontier's top rows and confirmed each is already on disk
  (Knill math/9409215 → `knill-graph-generated-1994`; Bruhn–Schaudt survey → on
  disk; Gowers polymath → `polymath-frankl-union-closed`; entropy DOIs → all on
  disk; Wikipedia → on disk).
- Ran fresh `exa_search` over 2025–2026 to check for any new constant or new n=13
  settlement, and over the Vučković–Živković twelve-element case.

## Findings

1. **The record is stable.** Published record = Yu, Entropy 25(5):767 (2023),
   c ≈ 0.38234 (arXiv:2212.00658). The (3−√5)/2 barrier is peer-reviewed
   (Alweiss–Huang–Sellke, EJC 31(3):P3.35, 2024, doi:10.37236/12232). Cambie
   (arXiv:2212.12500, c≈0.3823455) and Liu (arXiv:2306.08824, c≈0.38271,
   conditional) remain preprints; Liu at IEEE CISS 2024 only. No 2025–2026 source
   exceeds ≈0.38271 unconditionally. Matches the library's existing claims — no
   correction needed.

2. **Verification bound consistent.** The Pulaj–Raymond–Theis survey's union of
   "n ≤ 12 AND m ≤ 50, with (m,n)=(51,13) open" is NOT a contradiction of the
   library. The Vučković–Živković 2017 primary source settles ground-set n ≤ 12
   (so any counterexample has ≥ 13 elements); with the Roberts–Simpson 4m−1 bound
   this is consistent with the m=51, n=13 open case. ROOT.md's "|∪F| ≥ 13, |F| ≥ 51"
   is correct.

3. **No genuinely new source surfaced.** The 2025–2026 search returned only
   works already in the library (Das–Wu, Lu–Raz, Wakhare, Colbert).

## Conclusion

The library is finished per the operator directive; the frontier's top rows and
the only open request are covered. Pausing source gathering: any further addition
happens against a genuinely new gap stated in the requests ledger.
