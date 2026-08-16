# Thread: does a super-simple 2-(22,4,2) design exist, and does it decide the coclique-lift line?

```thread
id: thread-coclique-lift
question: Does a SUPER-SIMPLE 2-(22,4,2) design exist — 22 points, 77 blocks of
  size 4, every pair covered exactly twice (lambda=2), replication r=14, and no
  two blocks meeting in exactly 3 points (intersection number lambda_3 = 0)?
  And does the answer decide whether alpha=22 is possible in a putative
  srg(99,14,1,2)?
status: closed
rests-on: coclique-alpha22-forces-22242-design (checked),
  super-simple-22242-gap (the object, named), lou-murin-alpha22-block-design-reduction
blocked-by:
next: CLOSED by directive 20 — settled YES constructively, not by literature.
  CP-SAT OPTIMAL in 167.35s (7315 bools, 156131 branches), explicit 77-block
  certificate in code/out/coclique_lift_clean_design.txt, independently verified
  (degrees all 14, 231 pairs covered exactly twice, max triple overlap 1) —
  code/out/coclique_lift_cpsat.captured.txt. A super-simple 2-(22,4,2) design
  EXISTS, so the design condition is satisfiable and cannot rule out alpha=22.
  The line is closed as NON-OBSTRUCTIVE (sixth closed route, solution.md §2),
  not as a refutation of the graph. Note: research/notes/coclique-lift-supersimple-exists.md,
  claim super-simple-22242-exists. No librarian acquisition needed — construction
  beats citation.
```

## Why this line was live (now closed)

A tight 22-coclique C in any srg(99,14,1,2) forces the outside-neighbourhood
sets {N(b) ∩ C} to be a 2-(22,4,2) design (b=77, r=14), checked, claim
`coclique-alpha22-forces-22242-design`. The graph lift additionally forbids any
two blocks meeting in 3 points (else two outside vertices share 3 common
neighbours in C, violating lambda=1 if adjacent or mu=2 if not). That extra
condition is exactly super-simplicity — the object is a super-simple 2-(22,4,2)
design, not merely a 2-(22,4,2) design. See research/notes/super-simple-22242-gap.md.

## Verified state (re-read from captures, directive 19)

- Q1 plain 2-(22,4,2) **EXISTS**: `coclique_lift_q1.captured.txt` — HiGHS 66.56s,
  77 blocks, every point degree 14, every pair covered exactly twice.
- The Q1 design is **not usable**: `coclique_lift_check_design.captured.txt` —
  6 block-pairs sharing exactly 3 vertices (6 direct mu=2 violations).
- Q2 super-simple **INCONCLUSIVE**: `coclique_lift_q2.captured.txt` — 482.53s
  timeout, no feasible point. Not a nonexistence proof.
- `coclique_lift_q2_long.captured.txt` is 0 bytes (a failed run, per GOAL.md).
  (Note: the directive named `coclique_lift_q2b.captured.txt`, which is now
  filled — 584 bytes, the 481.79s timeout — so the empty file on disk is
  `coclique_lift_q2_long.captured.txt`.)
- `coclique_lift_constructive.captured.txt` = 4000 random draws in 0.72s,
  finding nothing. Honest label, but sampling over this space is not evidence
  (AGENTS.md). Do not extend.

## The two branches

- **Super-simple 2-(22,4,2) does NOT exist** (from the Gronau-Mullin spectrum):
  alpha=22 is impossible in any srg(99,14,1,2). This is a real constraint pulling
  the independence number below its Hoffman bound. Next question: is alpha=22
  forced at all, or merely allowed (so the constraint is vacuous)?
- **Super-simple 2-(22,4,2) DOES exist**: the design-level obstruction is absent;
  the only remaining obstruction is the full graph lift (finite, harder).
