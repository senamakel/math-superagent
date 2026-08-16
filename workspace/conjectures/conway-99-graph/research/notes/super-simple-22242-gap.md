# Super-simple 2-(22,4,2): the coclique-lift gap, named (directive 18)

The steering directive (18) names the object the coclique-lift line actually needs. This
note records the precise gap and the verified state of the two defects, and posts the one
acquisition request. The request tool filters it as "already bearing" against 8 on-disk
claims, but none of those claims states the super-simple existence spectrum — so the gap
is recorded here, where REQUESTS.md is populated from.

## The object (named)

Q2 asks for a 2-(22,4,2) design in which no three points lie in two blocks,
equivalently no two blocks meet in 3 points. That is a **super-simple 2-(22,4,2)**
design (b = 77, r = 14, every pair exactly twice, intersection numbers lambda_3 = 0).
Super-simple (v,4,2) designs are a studied family with published existence spectra
(Gronau, Mullin, and successors). Whether a super-simple 2-(22,4,2) exists is likely
already settled in the literature, in either direction, and either answer is decisive.

## Why super-simple is exactly what the graph needs

A tight 22-coclique C in any srg(99,14,1,2) forces {N(b) ∩ C : b outside} to be a
2-(22,4,2) design (claim `coclique-alpha22-forces-22242-design`, checked; b=77, r=14).
Each outside vertex b has a 4-block in C. If two outside vertices b, b' have blocks
sharing 3 points of C, then regardless of adjacency:
- if b ~ b', lambda=1 requires exactly 1 common neighbour — contra 3;
- if b ≁ b', mu=2 requires exactly 2 common neighbours — contra 3.
So 3 shared C-neighbours is a direct mu=2/lambda=1 violation. The graph lift needs
**no block-pair sharing 3 points**, i.e. a super-simple design. This is not optional — it
is forced by lambda=1, mu=2.

## Verified state (this session, from captures)

- **Q1 plain 2-(22,4,2) EXISTS** (HiGHS, 66.6s). The found design
  (`code/out/coclique_lift_design.txt`, captured `coclique_lift_q1.captured.txt`) is
  verified: 77 distinct blocks, every pair covered exactly twice, 0 repeated blocks — but
  it has **6 block-pairs sharing exactly 3 vertices** (6 direct mu=2 violations;
  `coclique_lift_check_design.captured.txt`). Unusable for a graph lift.
- **Q2 (super-simple) INCONCLUSIVE** (HiGHS, 482.5s timeout, status 13, no feasible
  point; `coclique_lift_q2.captured.txt`). The 1540 triple<=1 constraints (= super-simple)
  were added on top of Q1's 253 equality constraints; hit the 481s/482s time limit with
  no feasible point found. Not a nonexistence proof.
- `coclique_lift_q2b.captured.txt` is **EMPTY (0 bytes)** — a failed run (per GOAL.md,
  an empty capture is a failed run, not a missing one). `coclique_lift_q2_long.captured.txt`
  is also EMPTY. These should be deleted or filled.
- `coclique_lift_constructive.captured.txt` is 4000 random draws over 0.72s finding
  nothing — the steer is right that this is not evidence (AGENTS.md prohibits searching
  the answer space / sampling combines to nothing). Do not extend it. The MILP with a
  longer budget, or the literature, decides this.

## The definitive question

**Does a super-simple 2-(22,4,2) design exist?** (v=22, b=77, r=14, k=4, lambda=2,
lambda_3=0.)

- If **NO**: then alpha=22 is impossible in any srg(99,14,1,2) — a REAL constraint,
  pulling alpha below 22. The coclique-lift line is dead at the design level, and the next
  question is whether alpha=22 is forced at all or merely allowed.
- If **YES**: the design-level obstruction is absent; the only remaining obstruction is
  the full graph lift — the line continues.

This is a literature-settled question in the Gronau–Mullin super-simple family; the
in-library claims genuinely do not answer it.

```claim
id: super-simple-22242-gap
statement: A tight 22-coclique in any srg(99,14,1,2) forces the outside
  neighbourhoods {N(b) cap C} to be a 2-(22,4,2) design (b=77, r=14, checked), and the
  graph lift additionally requires NO two blocks to meet in 3 points (else a violating
  pair of outside vertices shares 3 common neighbours in C, contradicting lambda=1 if
  adjacent or mu=2 if not) — i.e. a SUPER-SIMPLE 2-(22,4,2). Verified: the Q1 HiGHS
  design exists but has 6 block-pairs sharing exactly 3 vertices (6 direct mu=2
  violations); Q2 (super-simple, 1540 triple<=1 constraints) timed out at 482s with no
  feasible point, INCONCLUSIVE. Whether a super-simple 2-(22,4,2) exists is a
  literature-settled (Gronau-Mullin) question not answered by any in-library claim:
  if it does NOT exist, alpha=22 is impossible in any srg(99,14,1,2) (a real constraint
  pulling alpha<22); if it DOES, the line continues to the full graph lift.
hypotheses: existence of srg(99,14,1,2) assumed; C a coclique of size exactly alpha=22
  (a nontrivial hypothesis); lambda=1, mu=2; the 2-(22,4,2) force is checked.
holds-here: yes for the reduction and the Q1/Q2 verified state (captures re-read this
  session); the super-simple existence itself is UNKNOWN (the gap).
status: checked for the force, the Q1 design's 6 violations, and the Q2 timeout; the
  existence of a super-simple 2-(22,4,2) is open (the gap).
bearing: names the exact finite object the coclique-lift line turns on; either published
  answer is decisive — nonexistence ⇒ alpha=22 impossible (real constraint), existence
  ⇒ line continues to the lift.
answers: (intended) the super-simple (v,4,2) existence-spectrum request
anchor: code/out/coclique_lift_q1.captured.txt, code/out/coclique_lift_check_design.captured.txt,
  code/out/coclique_lift_q2.captured.txt, code/out/coclique_lift_constructive.captured.txt,
  research/notes/lou-murin-alpha22-block-design.md
follows-from: coclique-alpha22-forces-22242-design, lou-murin-alpha22-block-design-reduction
```

## References to chase (if the librarian can serve the request)

Gronau, Mullin — "On super-simple 2-(v,4,lambda) designs" line; super-simple designs
with block size 4, lambda = 2 existence spectrum. Keys: "super-simple 2-(v,4,2)",
"super-simple designs existence spectrum". The v=22 row (b=77, r=14) is the target.
