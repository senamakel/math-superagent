# The 4-vertex-condition counting identity for srg(v,k,1,2) — a structural lead

<!-- Claims c7, c8 from the Brouwer–Ihringer–Kantor survey (arXiv:2107.00076),
read at research/sources/brouwer-ihringer-kantor-4vertex-condition.full.md,
Prop 2.1 (lines 76-88). -->

## The deduction, and its strengthening from the source

**Sims' criterion (Prop 2.1):** an SRG(v,k,λ,µ) satisfies the 4-vertex condition
with parameters (α,β) iff the number of edges in Γ(x)∩Γ(y) is α when x~y and
β when x≁y, and then

```
k(C(λ,2) − α) = β(v − k − 1)
```

(The equality counts 4-cliques-minus-an-edge.)

For the family srg(v,k,1,2): λ=1, C(1,2)=0, so −kα = β(v−k−1) forces
**α=β=0**. Hence the common-neighbour set of any pair is independent — the two
common neighbours of a nonadjacent pair are nonadjacent.

**The source strengthens this from conditional to unconditional.** The survey
immediately adds: "The same holds for a graph Γ with λ ≤ 1" (i.e. every λ≤1
SRG satisfies the 4-vertex condition, with α=(λ choose 2), β=0). For our family
that means **the 4-vertex condition holds automatically and the mu=2 common
neighbours of any nonadjacent pair are always nonadjacent** — this is a sourced
structural theorem about the geometry, not merely a conditional on the 4-vertex
condition.

Consequence for the geometry of srg(99,14,1,2): through a nonadjacent pair
x,y, the unique 4-cycle uses two common neighbours that are themselves a
NONEDGE. In the triangle (partial-Steiner-triple-system) geometry: the two
points common to the "lines" through a noncollinear pair form a noncollinear
pair. This is a clean, checkable constraint on the local structure — and it is
NOT spectral, so it survives the GOAL.md v=9/v=243 negative-control test.

## Verification pending (oracle)

A verification script is staged at code/out/check_c7_4vertex.py for
tool_builder/coder: it checks that every nonadjacent pair in rook(3) (9,4,1,2)
and in BvLS (243,22,1,2) has an independent (nonadjacent) pair of common
neighbours. If both pass, c7 is confirmed compatible with the two existing
graphs — as it must be, since the source asserts it as a theorem for λ≤1. If
either fails, the source theorem contradicts a real graph and something is
wrong (very unlikely; would indicate misreading).

## What this gives the run

A sourced, non-spectral structural fact:

```claim
id: c7-4vertex-mu2-common-neighbour-nonadjacent
statement: In any srg(v,k,1,2) (in particular a hypothetical srg(99,14,1,2)),
  the two common neighbours of any nonadjacent pair are nonadjacent to each
  other. This follows from Sims' criterion: lambda=1 forces alpha=beta=0 in
  the 4-vertex condition, and the Brouwer-Ihringer-Kantor survey states the
  4-vertex condition holds for every lambda<=1 SRG with alpha=(lambda choose 2),
  beta=0.
hypotheses: srg(v,k,1,2); Sims' criterion and the lambda<=1 statement in the
  survey (Prop 2.1 and the sentence following it).
holds-here: yes for (99,14,1,2). The lone nonadjacent-case content is mu=2:
  the two common neighbours form a nonedge.
status: sourced (survey Prop 2.1 + the lambda<=1 sentence). Arithmetic
  (lambda=1 -> C(1,2)=0 -> alpha=beta=0) verified by hand from the sourced
  formula. Oracle confirmation on rook(3) and BvLS pending at
  code/out/check_c7_4vertex.py.
bearing: a non-spectral structural constraint on the triangle geometry; a
  candidate load-bearing fact for the derived-design / partial-line-space
  attack surface. It does NOT by itself rule out 99 (it holds for 9 and 243),
  so it is a constraint to build on, not a nonexistence proof.
anchor: research/sources/brouwer-ihringer-kantor-4vertex-condition.full.md
```

## What would settle its value for 99
Whether the mu=2 common-neighbour-independence, combined with the 7K₂ local
structure and replication 7 of the partial-Steiner-triple-system, forces
something at 99 that 9 and 243 escape. That is a phase-3/4 structural question,
not a library one.

## What would refute c7 as a 99-lead (and what would not)

Both control graphs (rook(3)=9 and BvLS=243) satisfy c7: every nonadjacent
pair has a nonadjacent pair of common neighbours (checked in
code/out/c7_4vertex.captured.txt). **By itself that constrains nothing about
99** — it is a fact every member of the family shares, so it cannot split 99
off from 9 and 243, and confirming it on both controls is only the
admissibility test, not progress.

c7 becomes load-bearing for 99 only through a *combined* forcing argument:
someone must show that the mu=2-common-neighbour-independence, joined with
the 7 disjoint K₂ per-neighbourhood structure and replication 7 of the
partial-Steiner triple system, yields a local configuration at 99 that 9 and
243 do not have. The concrete refutation of such an argument is demonstrated
by construction on the controls:

  - **What would refute a c7-based 99 argument:** exhibit the argument's
    claimed forced configuration actually occurring in BvLS(243) (or
    rook(9)). Since BvLS is a real srg(243,22,1,2) and shares c7 with 99,
    any configuration the argument claims is 99-forcing that also occurs in
    243 proves the argument wrong — exactly the GOAL.md 9/243 admissibility
    rule. The smallest such case is the Rook example: c7 + the 7K₂ structure
    must hold in rook(3) and BvLS (it does), so an argument must name the
    *additional* 99-only ingredient.
  - In concrete terms: find the smallest substructure (function
    `lib.hexagons`/local-enumeration) whose forced occurrence at 99
    contradicts a count or local subgraph that BvLS already realises. That
    would refute the 99 claim while leaving c7 a true but inert theorem.

Until such an argument is written, c7 is a **lead, not a result**: correct,
sourced, compatible with the controls, and entirely silent about whether the
99 graph exists.
