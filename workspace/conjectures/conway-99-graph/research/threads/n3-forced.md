# Thread: is n_3 ≥ 1 forced for a putative srg(99,14,1,2)?

```thread
id: thread-n3-forced
question: Is n_3 >= 1 forced for a putative srg(99,14,1,2)? n_3 = number of
  unordered pairs of triangles joined by exactly 2 edges (equivalently, pairs
  of triangles sharing an edge without sharing the third triangle edge).
status: open
rests-on: makhnev1988-condstar-theorems (sourced, primary Russian full text),
  reimbayev-hexagon-bound-n3-pivot,
  code/out/hexagon_identity_verified.captured.txt,
  code/out/makhnev-1988-condition-captured.txt,
  code/out/check_makhnev_n3_counts.captured.txt,
  code/out/check_srg33_12_1_6.captured.txt
blocked-by:
next: n_3 >= 1 at 99 is RE-DERIVED (claim makhnev99-shorter-proof-integrality,
  note research/notes/makhnev-99-shorter-proof.md). REMAINING TARGET (directive
  12, task `kill-n3-ge1-case`) is a FINITE SAT/CP-SAT question, not an informal
  push: can a disjoint triangle pair joined by exactly 2 edges (ABC, DEF, edges
  A-D and B-E) extend AT ALL in a graph that is locally 7K2 with mu=2? Encode
  the bounded local ball — lambda=1 (each edge in a unique triangle), mu=2 (two
  common neighbours per non-adjacent pair), neighbourhood = perfect matching —
  and ask SAT/CP-SAT whether it extends. ENCODER GATE: the same encoder must
  FIND the join-3 and join-1 triangle-pair configurations that BvLS actually contains (join histogram {3:8910}, {1:240570}, code/out/n3_four_graphs.captured.txt) and find rook(3) outright at (9,4,1,2) before any UNSAT is believed. This is the kill-n3-ge1-case question, now ANSWERED (directive 14): the seed extends locally — NO local obstruction (2 satisfying assignments under the sound upper-bound criterion, code/out/n3_seed_consistency_ub.captured.txt, claim n3-seed-locally-consistent-radius1). The earlier CONTRADICTION was a soundness bug in code/lib/localprop.py, not an obstruction. NEXT (directive 16): CONSOLIDATE FIRST — write solution.md (task `write-solution-md`) before any further radius work; the radius-2 CP-SAT setup is STOPPED (sat_solver agent-run-81 FAILED at 213:44 having written nothing). AFTER solution.md exists, return to the radius question by bounded enumeration on ONE more shell, NOT CP-SAT (task `radius-one-more-shell-enumeration`), and record the enumeration ceiling as the infeasibility boundary — the radius attempted, the search space, the worker count, the wall clock at abandonment, and how far it got. A radius-R local obstruction is NOT a global nonexistence proof.
  NOTE: rook(3) and bvls_graph() both have n_3=0, and no known mu=2 lambda=1
  SRG has n_3>=1, so they CANNOT refute an n_3>=1 argument. The mu>=4
  Bondarenko-Radchenko graphs (81,20,1,6),(729,112,1,20) do witness n_3>=1
  but are mu!=2 and cannot gate a mu=2-specific argument. The control is
  therefore the hand-built 2-edge-joined disjoint triangle pair inside a
  locally-7K2 mu=2 neighbourhood (weaker than a real graph) — see the
  Controls section.
```

## Why this is the phase-4 target

Makhnev 1988 Thm 2 (primary Russian full text, open access mathnet.ru, now in
`research/sources/makhnev-1988-lambda1-russian-fulltext.full.md`) proves:

> There is no srg(99,14,1,2) or srg(115,18,1,3) satisfying condition (*),

where (*) = "any pair of triangles joined by at least two edges is joined by
exactly three edges" — which is exactly `n_3 = 0`. So the contrapositive reads:

> **If a srg(99,14,1,2) exists, then n_3 ≥ 1.**

A forcing argument for n_3 ≥ 1 would therefore settle nonexistence **given**
Makhnev; a construction with n_3 = 0 would refute the conditional. This is the
single sharpest lever the run has.

**Status of the conditional:** `sourced` (primary Russian full text READ,
`research/sources/makhnev-1988-lambda1-russian-fulltext.full.md`; claim
`makhnev1988-condstar-theorems`). Makhnev's *proof* is not independently
reproduced here, but the mechanism is named from the text: lemmas 8-9 build an
srg(33,12,1,6) subgraph Delta_0 satisfying (*), which Thm 1 kills (mu=6>3).
The contrapositive — any putative (99,14,1,2) has n_3 >= 1 — is a CONSTRAINT,
not a nonexistence proof: ruling the problem out still needs the n_3>=1 case
killed. Quote it as sourced, never as computed.

## The controls, checked

Both existing members have n_3 = 0 and exist:

- rook(3) = srg(9,4,1,2): 6 triangles, 0 pairs joined by exactly 2 edges.
- BvLS = srg(243,22,1,2): 891 triangles, 8910 pairs joined by exactly 3 edges,
  0 by exactly 2.

So n_3 = 0 is realizable inside the family. **For an argument forcing n_3 ≥ 1,
rook(3) and bvls_graph() are NOT witnesses against it — both have n_3=0, so they
cannot refute an n_3≥1 argument.** That is the amendment to the earlier
admissibility rule: this line needs a DIFFERENT control (a known lambda=1 SRG
with n_3 >= 1; see task `n3-positive-control`). **Control status, corrected (directive 11).** n_3 ≥ 1 IS witnessed in the λ=1
family: Brouwer–Haemers srg(81,20,1,6) and Games srg(729,112,1,20) exist (claim
`bondarenko-radchenko-lambda1-gk`) and have μ≥4, so Thm 1's contrapositive
forces n_3≥1 on them. They are μ≠2, so they cannot gate the μ=2/locally-7K2
kill argument. The only known μ=2 λ=1 SRGs are rook(3) and bvls_graph(), both
n_3=0, so no known μ=2 graph witnesses n_3≥1. The doily (15,6,1,3)=GQ(2,2) and
the GQ(2,4) point graph (27,10,1,5) are to be built and n_3-checked (predicted
0; task `n3-positive-control`) — four exact numbers, no literature. The kill
argument's control is therefore the hand-built 2-edge-joined disjoint triangle
pair inside a locally-7K2 μ=2 neighbourhood (weaker than a real graph).

Source of the measured values: `code/out/hexagon_identity_verified.captured.txt`
(triangle-pair join-2 enumeration, exact integers) and
`code/out/makhnev-1988-condition-captured.txt` (condition (*) holds on both
controls).

## What n_3 counts, precisely

n_3 = #{ unordered pairs {T, T′} of triangles with |E(T) ∩ E(T′)| = 1 } — two
triangles sharing exactly one edge (joined by exactly 2 edges). In the
triangle graph Γ_Δ of Makhnev/Reimbayev, (*) = "no such pair", i.e. every pair
of triangles meeting in ≥2 edges meets in exactly 3 edges (shares a whole
triangle).

## Candidate attack lines (none endorsed yet)

0. **Primary target (directive): what does n_3 >= 1 force?** Take a disjoint
   triangle pair joined by exactly 2 edges in a graph that is locally 7K2 with
   mu=2, and push the local configuration to a contradiction or a construction.
   The controls caveat above applies.

1. **Local count around a vertex.** Each vertex is in 7 triangles; count the
   triangles meeting a fixed triangle's neighbourhood, and ask whether the
   parameter arithmetic (99,14,1,2) forces some pair of triangles to share an
   edge. Test any identity at 9 and 243 first (both have n_3=0).
2. **A second counting identity in n_3.** Reimbayev's order-6 subgraph counts
   are determined by (n,k)+n_3; if any induced-subgraph count has a second
   closed form not involving n_3, equating the two gives a relation that may
   force n_3 at 99.
3. **Makhnev's own mechanism inverted.** Thm 2 builds an srg(33,12,1,6) from a
   triangle's closure under (*); attacking the *converse* (exhibiting the
   obstruction that must appear if n_3 ≥ 1) is the same route read backwards.

## Falsifiers

- Forcing n_3 = 0 at 99 (the opposite conclusion) settles nonexistence given
  Makhnev Thm 2.
- A construction of srg(99,14,1,2) with n_3 = 0 refutes the conditional.
- Makhnev's Thm 2 being mis-stated (the primary text says otherwise — re-check
  before either conclusion is drawn).
