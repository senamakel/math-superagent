# Pattern-finder report — round 15: the clean (super-simple) 2-(22,4,2) exists — the coclique-lift gap is closed

## What changed since round 14

Rounds 13–14 and the steering narrative (`super-simple-22242-gap.md`,
`scholar-digest-pass-6.md`) all report the super-simple 2-(22,4,2) Q2 question
as **INCONCLUSIVE** (HiGHS MILP timeout at 482s, Q1 design defective with 6
block-pairs sharing 3 vertices, random draws finding nothing). But on disk
there is a newer artifact the narrative never integrated: the CP-SAT run
`code/out/coclique_lift_clean_design.txt` / `coclique_lift_cpsat.captured.txt`
(19:11) that found a **clean design**, timestamped before
`pattern_finder_report14.md` (19:18) and `super-simple-22242-gap.md` (19:19)
— both of which still call Q2 INCONCLUSIVE. The run was sitting on the answer
to its own named decisive gap.

## Finding — a super-simple 2-(22,4,2) design EXISTS (verified, three routes)

`coclique_lift_clean_design.txt` is a genuine **super-simple 2-(22,4,2)**
design: 77 distinct 4-blocks on {0..21}, every point in exactly 14 blocks,
every pair in exactly 2 blocks, and **no two blocks share a triple** (max
triple overlap = 1; all 308 covered triples distinct). Equivalently it is a
`2-(22,4,2)` with intersection number `lambda_3 = 0` — exactly the
`mu=2`/`lambda=1`-clean family member the graph lift needs.

Verified by **three independent routes of exact integer counting** (no floats):

| route | file | result |
|---|---|---|
| CP-SAT in-program verify | `coclique_lift_cpsat.py` | OPTIMAL (167s), deg14, pairs2, clean |
| my independent direct count | `code/out/pf_verify_clean_design_independent.py` | 2-(22,4,2) True, SUPER-SIMPLE True |
| existing referee check | `code/out/refute_check_clean_design.py` | clean: SUPER-SIMPLE True, 0 block-pairs sharing >=3 |

The clean file is **not** byte-identical to the Q1 design (which genuinely has
6 block-pairs sharing 3 vertices and is super-simple-FALSE): `same = False`.

## Closing the run's named decisive gap

`super-simple-22242-gap.md` set the criterion: **if NO super-simple 2-(22,4,2)
exists, alpha=22 is impossible in any srg(99,14,1,2)** (a real constraint
pulling alpha<22); **if YES, the design-level obstruction is absent and the
line continues to the full graph lift.** Per that exact criterion, the finding
resolves the gap:

- The design-level obstruction is **ABSENT**. alpha=22 is not pulled below 22
  at the design level.
- The existence of a super-simple 2-(22,4,2) is consistent with a tight
  22-coclique's neighbourhood-family in a putative srg(99,14,1,2); the
  coclique-lift line's remaining obstruction is the **full graph lift** (the
  interlocking of ~77 outside vertices), not the design.

This is **exact and constructive** — an explicit 77-block certificate on disk,
re-verified by direct counting here. It is NOT a proof that srg(99,14,1,2)
exists; it removes the run's named decisive design-level blocker and redirects
the coclique-lift effort to where it actually stands.

## On the sequence catalogue (re-affirmed: still no new algebraic sequence)

No new length-bearing integer sequence arrived with the clean design — it is a
finite 77-block object, not a sequence. The standing catalogue of 14 rounds
(parameter-determined counts = `a=2u+1|63` quartics, none separating 99) is
unchanged. The one genuinely new, exact, run-changing fact is the super-simple
existence certificate above.

## Status notes

- This is a **checked / constructive** finding (explicit certificate + three
  exact counting verifications), not a conjecture.
- First-falsifying term: none — it is a concrete object on disk, not a fitted
  pattern. The only way it is not "the answer to Q2" is if the design's
  super-simplicity were mis-verified; it is verified three independent ways.
- The three routes agree exactly.

## Recommendation / hand-off

The steering directive's coclique-lift line no longer hangs on the design. The
next question the numbers pose is whether a *cleaned* 2-(22,4,2) (this one, or
any super-simple one) can be **lifted to a full graph** on 22+77=99 vertices
— a finite construction/consistency question beyond the design level, most
naturally for the sat_solver / a global consistency engine, not the sequence
tools. This round closes the design-level branch and names the true next step.

## Files

- `code/out/coclique_lift_clean_design.txt` — the super-simple certificate (77 blocks).
- `code/out/coclique_lift_cpsat.captured.txt` — CP-SAT run that found it (OPTIMAL, 167s).
- `code/out/pf_verify_clean_design_independent.py` — my third-route verification (this round).
- `code/out/refute_check_clean_design.py` — running referee check.
- `research/notes/super-simple-22242-gap.md` — the gap, now closed by this finding.
- This report.
