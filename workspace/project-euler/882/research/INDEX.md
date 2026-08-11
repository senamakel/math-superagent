# Index — research

The library reduces the bit-deletion game to a counting game over the totals
(A = n#ones, B = n#zeros). Summary tree: `L1/` = one note per source, `folds/`
= one note per subject. Each fold links the notes it covers, so what it leaves
out stays one wikilink away.

## Folds (start here)
- [[folds/game-core]] — CGT framework: each number is the partisan game
  `{G(a-1,b)|G(a,b-1)}` = the integer `a-b`; the board's no-skip value is `A-B`;
  Sprague–Grundy does not apply. → the game reduces to (A,B). Covers
  [[L1/cgt]] [[L1/disjsum]] [[L1/surreal]] [[L1/partisan]] [[L1/normalplay]].
- [[folds/passes]] — the Zero-skip as zugzwang escape + loopy self-loop
  resolved as a DP fixpoint; the game is a stopper so a finite S(n) exists.
  Covers [[L1/pass_waiting]] [[L1/zugzwang]] [[L1/loopy]].
- [[folds/counting-arithmetic]] — polylog evaluation of A(n), B(n): the tools
  for the n=10^5 scale, from Trollope–Delange / weighted-moment theory and the
  A000788/A059015/A083652 recurrences. Covers [[L1/bitcount]] [[L1/zerocount]]
  [[L1/a083652]] [[L1/trollopedelange]] [[L1/weightedmom]]
  [[L1/verify_trollopedelange]].
- [[folds/deadends]] — examined, no yield: S(n) is not in OEIS; a generic
  strategy article is irrelevant. Covers [[L1/strategy]] [[L1/weightedsearch]].
- [[L1/misfiled]] — four arXiv downloads saved in L0/ that are unrelated to the
  problem (compression, KOTO, COHERENT, medical segmentation); accidental,
  dead. No L1 summary, no fold. See the note; do not re-open the L0 files.

## Notes by source (full text in L0/, summaries at the L1 link)
| Note | Purpose |
| --- | --- |
| [[L1/cgt]] | CGT position form / disjunctive sums; board decomposes. |
| [[L1/disjsum]] | Core: G(a,b)=a−b, board → the two totals A,B. |
| [[L1/surreal]] | Why a−b is exact; skips outside short games ⇒ A−B ≠ S(n). |
| [[L1/partisan]] | S−G inapplicable (disjoint move sets); minimax over (A,B). |
| [[L1/normalplay]] | unable-to-move loses; A−B>0 ⇒ One wins without skips. |
| [[L1/pass_waiting]] | Larsson–Nowakowski–Santos 2015 arXiv:1505.01907 primary pass theory. |
| [[L1/zugzwang]] | skip = "passing, if allowed, would be best". |
| [[L1/loopy]] | skip self-loop → DP fixpoint; stopper ⇒ finite S(n). |
| [[L1/bitcount]] | A000788: summatory 1-bits, O(log n) recurrences → A(n). |
| [[L1/zerocount]] | A059015: summatory 0-bits → B(n). |
| [[L1/a083652]] | A083652: summatory bit-length, exact O(1) closed form; third leg total = ones+zeros. |
| [[L1/trollopedelange]] | Girgensohn 2011 #A54: explicit Delange closed forms (1-periodic fluctuation). |
| [[L1/weightedmom]] | Larcher & Pillichshammer 2005: k·-weighted moments admit same closed forms. |
| [[L1/verify_trollopedelange]] | numeric checks to run before quoting Girgensohn. |
| [[L1/strategy]] | dead end. |
| [[L1/weightedsearch]] | dead end: S(n) ∉ OEIS. |

Caveat: the counting model is a *surrogate* — deleting a leading 1 can also
drop 0-bits (e.g. "100"→0). Real-vs-counting S(n) equality is checked
empirically by brute.py vs counting.py.
