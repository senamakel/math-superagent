# Librarian audit — dangling full-text references fixed (cycle 2)

Two provenance defects found and fixed this cycle. Both were the same class:
an OEIS/primary page whose full text had been filed as a *summary*, leaving
the summary's `research/sources/...full.md` reference dangling.

## 1. dudeney-torn-number.full.md now in sources/

`research/summaries/dudeney-torn-number-solution.md` referenced
`research/sources/dudeney-torn-number.full.md` (the problem statement) but no
such file existed — the raw problem page had been misclassified as a *summary*
(`research/summaries/dudeney-torn-number.md`) and carried the full converted
HTML there.

**Fix.** Full text now at `research/sources/dudeney-torn-number.full.md`
(source https://bookofproofs.github.io/.../the-torn-number.html), indexed for
search_documents. The summary was rewritten to a concise note pointing at both
the problem and solution pages. The reference in
`dudeney-torn-number-solution.md` now resolves.

## 2. oeis-A238237-torn-numbers.full.md now in sources/

`research/summaries/oeis-A238237-torn-numbers.md` was stored as a raw HTML
"digest" of the OEIS A238237 record page and told readers "the complete text is
at `research/sources/oeis-A238237-torn-numbers.full.md`; open that only when
this file does not answer the question" — but that full-text file had never
been created. A238237 (two-block equal-halves torn numbers) is a genuine
canonical-sequence record in the two-block theory tier, so it belongs in
`sources/`.

**Fix.** Full record at `research/sources/oeis-A238237-torn-numbers.full.md`
(source https://oeis.org/A238237), indexed. Summary rewritten as a concise note
(definition, three Schott subsequences, relation to A102766/A006886/Javaheri/
Kodrnja, bearing on PE 719).

## Audit of remaining references

Every other `research/sources/<file>` referenced from summaries exists: all
OEIS records (A104113, A038206 b-file, A006886), the two-block theory full
texts (Iannucci, Black, Dudeney x2, Javaheri, Hamilton), Butler–Graham–Stong
(both abstract and body), nrich, Smarandache, and the DE/contribution notes.
The `oeis_a110113_full.md` leftover is a deliberate pointer note (the earlier
misfile), already recorded in the cycle-1 audit.

## State

The reference library is complete for this problem and internally consistent:
every source named in a note or claim has a real file under
`research/sources/` or is a documented intentional exclusion (MathWorld,
Oxman–Stupel payable, S.P-numbers/SSPDS/junction name-collisions). The final
answer T(10^12)=128088830547982 stands verified by three independent routes
(solution.py recursion, A038206 b-file sum of squares, meet-in-the-middle).
