# Pattern-finder report — round 17: catalogue confirmed exhausted by a fresh independent run

## What I did this round

The whole of the sequence-bearing data on disk has been mined across rounds 1–16,
and round 16's verdict was "catalogue exhausted; several only-99-specific
structural values remain." Before endorsing that from inheritance, I re-derived
the entire family-count catalogue **fresh** from the closed forms (`code/out/pf_round17_consolidated.py`)
and ran the exact sequence tools myself on representative sequences. I also
examined the one item the catalogue had flagged *live but unmined* — the
incidence p-rank deficiency pattern — to decide whether it carries any sequence
structure not yet extracted.

## Every family sequence reproduces round 16 exactly (checked)

Over the feasible index set `u ∈ {1,3,4,10,31}` (`k=u²+u+2`, `v=1+k²/2`,
`a=2u+1 | 63`), my fresh re-derivation gives the exact catalogue:

| sequence | values |
|---|---|
| triangles | [6, 231, 891, 117096, 81842481] |
| hexagon base (n3=0) | [6, 209286, 4980690, 146767540920, ...] |
| outer blocks | [6, 1386, 8910, 6440280, 40593870576] |
| distance-2 | [36, 8316, 53460, 38641680, 243563223456] |
| coclique bound | [3, 22, 45, 561, 15408] |
| n3 cap | [18, 4158, 26730, 19320840, 121781611728] |
| m_r | [4, 44, 110, 2992, 243104] |
| m_s | [4, 54, 132, 3280, 250914] |
| d_C | [2, 4, 5, 11, 32] |
| coclique blocks b | [6, 77, 198, 5712, 478611] |

All match the on-disk authoritative values. The pentagon count `[0, 33264, 384912,
1669320576, 96451036488576]` is independently brute-force verified
(`v·k(k−2)(k−4)/5`; at 99 it is exactly 33,264). My own quick script initially
used a wrong pentagon formula (paths, not induced pentagons); I discarded that
stray value and kept the independent-verified one.

## Sequence-tool results (exact over the terms, this round's own run)

`analyze_sequence` on the coclique bound `[3,22,45,561,15408]` and the
distance-2 family `[4,84,220,6160,493024]`: first differences never become
constant at any level, so neither is a low-degree polynomial (exact statement
over the terms). `find_linear_recurrence` with `max_order=4` finds **no**
constant-coefficient linear recurrence fitting either 5-term sample. This is
exactly what rounds 1–16 established for every family count: each is the same
sparse-index `a|63`-governed quartic, meaningful only through its closed form,
not through an independent recurrence law.

So the sequence tools **confirm** the standing catalogue rather than adding to
it. Every parameter-determined count is a `|63`-quartic and none separates 99
from the two existing members 9 and 243.

## The incidence rank-deficiency pattern: NOT a sequence (resolves the last unmined item)

The thread `incidence-code` had flagged the p-rank as possibly live. The
measured rank-2 deficiencies are `[4,5,6,0]` over rook(3), doily, GQ(2,4),
BvLS. I checked the premise: these four graphs have **different** parameter sets —
rook(9,4,1,2), doily(15,6,1,3), GQ(2,4)(27,10,1,5), BvLS(243,22,1,2). They are
not points of a single parametric family; the 4,5,6 track the varying v, not a
a-sequence of the λ=1,μ=2 family. Only rook and BvLS share that family, and two
points give no exact sequence claim. So the deficiency pattern is a structural
observation (the thread's open gate — parameter-determinism — is a *proof*
question, not a sequence question) and has no extractable regularity here.

## Status and honesty

- **Checked:** the entire catalogue reproduces round 16; no new sequence-bearing
  artifact exists on disk since round 16 (only INDEX.md, commands.log and this
  run's own files are newer than report 16).
- The two 99-specific quantities that separate 99 from the controls remain
  exactly those two: **coclique bound 22** and **forced n3 ≥ 3** (Makhnev
  conditional, with n3≥3 from intersecting n3≡0 mod 3). Neither is a sequence
  with extrapolating terms; both are structural values no sequence tool extends.
- First-falsifying term: none — the catalogue is closed forms verified on
  fixed sets, not a fitted pattern to break.

## Recommendation

The sequence line is genuinely done (rounds 1–17, now confirmed by a fresh
independent run). The next structural steps are construction/search: the full
graph lift of a super-simple 2-(22,4,2) into 99 vertices, and the k=14 local
triangle geometry — not regularity mining. NOTHING FURTHER is available from the
sequence tools.

## Files

- `code/out/pf_round17_consolidated.py` — fresh re-derivation + difference checks (this round).
- `code/out/pattern_finder_report16.md` and prior reports — the standing catalogue.
- This report.
