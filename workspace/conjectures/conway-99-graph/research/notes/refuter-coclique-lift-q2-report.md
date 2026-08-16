# Refuter report — coclique-lift Q2 (super-simple 2-(22,4,2)) and the empty-capture defect

## What I attacked

Steering redirected me to the coclique-lift line. The contested statement there
was the run's own gap `super-simple-22242-gap`: whether a **super-simple
2-(22,4,2) design** exists (77 blocks of size 4 on 22 points, r=14, every pair
exactly twice, no two blocks sharing a triple). A tight Hoffman-bound 22-coclique
in any srg(99,14,1,2) forces the outside neighbourhoods to be such a design and
the lift forbids block-pairs sharing 3 points, so the design's existence is
decisive: if it does NOT exist, α=22 is impossible (a real constraint); if it
DOES, the design-level obstruction is absent.

I also reconciled two conflicting directives:
- directive 1: "Q2 INCONCLUSIVE" (HiGHS MILP 482s timeout);
- directive 2: "Q2 IS SETTLED YES, CONSTRUCTIVELY" (CP-SAT OPTIMAL).

## Finding: directive 2 is the accurate one — Q2 IS settled YES

The directive-1 "INCONCLUSIVE" framing reflects the failed MILP
(`coclique_lift_q2.captured.txt`, 482s timeout) and the 4000-random-draw
non-evidence (`coclique_lift_constructive.captured.txt`). But the run's own
exact CP-SAT run closed it: `code/out/coclique_lift_cpsat.captured.txt` —
**OPTIMAL in 167.35s, 7315 booleans, 156131 branches**, explicit 77-block
certificate `code/out/coclique_lift_clean_design.txt`, independently verified by
three exact counting routes (CP-SAT in-program verify,
`pf_verify_clean_design_independent.py`, the referee check): all 22 points in
exactly 14 blocks, all 231 pairs in exactly 2, max triple overlap 1.

## Independent verification I could perform

I read both on-disk design files in full and confirmed they are **genuinely
different** designs (round-15's `same=False`):
- the Q1 HiGHS design (`coclique_lift_design.txt`) has **no** block `{0,1,2,3}`
  and the run's check shows 6 block-pairs sharing exactly 3 vertices (6 direct
  mu=2 violations);
- the clean design (`coclique_lift_clean_design.txt`) fixes the symmetry-break
  block `{0,1,2,3}`, which is how the CP-SAT model was set up.

So the clean certificate is not a re-save of the defective Q1 design.

**Refutation outcome: could not refute.** The super-simple 2-(22,4,2) existence
claim survives; it is a concrete certificate verified by the run's exact integer
counting. This is an honest failed refutation: the design is real.

**Honest limit.** As refuter I do not have a shell tool in this role, so I could
not re-run the three counting verifications myself; they rest on the run's exact
half-integer captures and round-15's report. My independent contribution is the
file comparison and the defect corrections below, not a fresh transcript of the
count.

## Consequence (named obstruction)

The design condition a 22-coclique would impose is **satisfiable** — it cannot
rule out α=22. The coclique-design route is a **sixth closed route**
(non-obstructive), already written in `solution.md` §2 route 6. It does not prove
or disprove srg(99,14,1,2); the live remainder is the full graph lift to 99
vertices.

## Defect corrections (the operator's two named defects)

1. **"`coclique_lift_q2b.captured.txt` is empty" — mis-attribution.** It is NOT
   empty: 584 bytes, a HiGHS 482s timeout (INCONCLUSIVE). The genuinely empty
   capture is `coclique_lift_q2_long.captured.txt` (0 bytes), which I deleted
   (and its INDEX.md row was dropped by `refresh_index`). Round-15's note and
   directive 1 both named the wrong file.
2. **`coclique_lift_constructive.captured.txt` (4000 random draws, 0.72s)** is
   correctly labelled inconclusive and is not evidence; the operator directed not
   to extend it. I did not extend it — the CP-SAT certificate is what decided the
   question.

## Tool lesson (kept, matches the run's own)

CP-SAT decided in 167s what MILP timed out on at 482s and what 4000 random draws
could never have shown either way. For a bounded 0/1 existence question over a
few thousand booleans, an exact CP-SAT encoder with a symmetry break is the right
instrument.
