# Librarian cycle 2026b — two 2024–25 primary sources added, one parser defect fixed

Cycle outcome: the record is unchanged (re-verified live), the library stayed
closed per operator directive, but two genuinely new primary sources were found
in the recent window (2024-06 → now) that no audit had surfaced, plus one
library-mechanism defect was found and fixed.

## Added (both from live arXiv searches, both previously absent)

1. **Demontis, "The union-closed set conjecture is true", arXiv:2405.03731**
   (6 May 2024). A claimed FULL proof of Frankl's conjecture.
   `research/sources/demontis-union-closed-set-conjecture-is-true-2024.full.md`,
   summary + claim `demontis-claimed-uc-proof-unaudited`.
   **Reception: zero.** 0 citations; no critique or endorsement found; the same
   text was "accepted" by OPAST's Curr Res Stat Math in 26 days (1 May → 27 May
   2024), a venue with no peer-review record. The workspace's claimed-proof
   audit (Spence, on two OTHER claimed proofs) does not cover Demontis.
   Filed explicitly as **claimed / unaudited — DO NOT cite as established**;
   nothing in it is used anywhere in this library.
   Red flags for a future auditor: the proof is elementary and self-contained
   (~9 pages, no entropy machinery, does not engage the 0.38234 literature at
   all); the final line is `|F| = 2|A_i| − 1 − |D| ≤ 2|A_i| − 2|D_i| = 2|F_i|`,
   whose hypothesis-matching with Theorems 4–5 is the natural first check.

2. **Hachimori–Kashiwabara, "Average-Rare Order Ideals in Functional
   Preorders", arXiv:2511.19833** (25 Nov 2025; follow-up to on-disk
   2504.13454). Proves (Lean 4 formalised, repo
   `github.com/kashiwabarakenji/avg-rare`) that the order-ideal family of any
   functional preorder induced by f: V→V is **average-rare** (NDS ≤ 0) — a new
   machine-checked settled class for Frankl's conjecture (dual form). Covers
   rooted-forest posets. Average-rarity fails for general preorders
   (Example 2.7, NDS = 1 > 0) though UC still holds there — a useful boundary.
   Conjecture 6.1 (rooted-set representations with each element root of at most
   one rooted set ⟹ average-rare) is their open next step.
   Claim `hak-functional-preorders-average-rare` filed.

## Parser defect found and fixed

**Claim blocks fenced ` ```yaml ` silently never reach the claims ledger.**
The parser only accepts ` ```claim ` fences. Verifying the two new claims in
`read_ledger` surfaced that my ` ```yaml ` blocks were not indexed; the same
fence was found on `research/summaries/published-record-current-verified-2025.md`
(only other occurrence in research/) and fixed. Lesson stored durably:
always fence claim blocks ` ```claim `. Search for stray `^```yaml` before
closing a cycle.

## Not obtainable (re-confirmed)

- **Poonen 1992 full text**: ScienceDirect PDF 403-paywalled (the audit's
  prediction held). The paper's content stays covered by 8 indexed claims via
  the survey, the errata, and Morris/Marić restatements; the citation graph was
  walkable (62 citations, 25 new leads into the frontier), but no free copy
  surfaced. Kept as a known gap, not re-requested (the request machinery
  correctly judged the content already answered).

## Library state after this cycle

- ROOT.md still meets the phase-1 exit test (minimal counterexample |∪F|≥13,
  |F|≥51; verification n≤12 / |F|≤50; settled classes incl. the two new Lean-4
  classes; record Yu 0.38234 published, Cambie/Liu preprints).
- No claim in this library cites Demontis as established.
- The single open request `exact-current-published-c8b8` remains answered and
  unchanged by live re-verification.