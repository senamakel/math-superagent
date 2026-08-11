# Inventor proposal: count 3D reachable configs by their voidance sets

## The structural fact (the lever)

The 3D PE763 amoeba is exactly Eriksson/Vaderlind's **n=3 pebbling game**
(a cell splits into its three forward neighbours iff all three are empty)
— sourced claim, EJC 2 (1995) #R7, verified rule-for-rule.  For n>=3 the
reachable-position enumeration collapses onto a bijection (Thm 9):

> reachable positions  <->  voidance sets  <->  folded polyominoids

and **no cell is ever produced twice** (Prop 24).  So *counting reachable
configurations = counting voidance sets*, and the voidance set of an
N-division configuration has **N cells** (one per division: every division
empties its parent cell).

## Why the current enumerators cap out and what breaks that

The run's BFS enumerates actual occupied-cell sets; the frontier grows ×3.4
per division and the 2 GiB container caps it at N=14 (~5.9M states).  My job
is a method whose cost does not grow with the frontier.  The voidance-set
count is that method **if** there is a DP that counts voidance sets directly
without listing them — the 3D analogue of the 2D `G(k,m)` two-index DP that
counts A007902 without enumerating.

## New structural observation (hand-verified, to be machine-confirmed)

Poring over the run's own config dumps (`data/level_N.txt`, N=2..12) and the
explicit N=3,4 configs:

1. **Every reachable config's max level M holds exactly 3 cells** — every
   level histogram ends in `3` ("0 2 3", "0 2 2 3", "0 1 5 3", ...).  This is
   exactly what Eriksson Prop 24 (no node played twice) predicts: the deepest
   cells form a single complete child-triangle.
2. Those 3 top cells are the **complete forward-child triangle of one empty
   parent at level M-1** — they can only have been produced by a single
   division of that parent.
3. **Consequence: the reverse collapse (merge the unique top cap into its
   parent) is DETERMINISTIC.**  Repeating reaches {origin} in exactly N steps.
   This gives a one-to-one correspondence between reachable N-configs and
   their (ordered) collapse sequences — i.e. between configs and **full
   ternary trees of divisions**, which is the voidance-set bijection.

This is the reduction the problem statement's bound (N=10000) is designed to
force: instead of trusting BFS, *build a counting DP on the voidance set
(collapse tree) structure*.  The 2D crossword is the same bijection; the 3D
version is *simpler* because no cell is played twice (2D needs
crossing-marking, 3D does not — Eriksson).

## The precise testable proposal

**CLAIM A (reverse cap-collapse is canonical).** For every reachable config S
at N>=1 divisions:
- A1: S has exactly 3 cells on its max level M;
- A2: those 3 top cells = {p+e1,p+e2,p+e3} for a unique empty p at level M-1;
- A3: iterated cap-merge reaches {origin} deterministically in N steps.

**CLAIM B (forward recurrence).** Let conf(N) = reachable N-configs and
f(C) = #{cells p in C : none of p+e1,p+e2,p+e3 lies in C} (dividable cells).
Then
        D(N+1) = Σ_{C∈conf(N)} f(C)      (N = 0,1,2,...)
because the map (dividable p, C) → child config is injective (CLAIM A3).

**CLAIM C (the 3D G(k,m)-analogue DP).** Since configs <-> voidance sets, and
a voidance set is characterized by the *height profile* (how deep each
division's parent sits — i.e. the level multiset of the N collapse-merge of
parents = the histogram of voidance-cell levels), count voidance sets by a
two-index DP H(k, m) = #voidance sets of size... (see below).  D(N) = sum over
profiles.  This is the object to implement; it is the announced open seam, not
yet derived.

## Small-N checks (the falsifiers)

The tool_builder should run `python3 code/inventor/check_recurrence.py`
(forward BFS N<=7) and confirm:
- CLAIM A1 bad-count == 0 (every max level has exactly 3 cells);
- CLAIM A2 bad-count == 0 (unique cap parent);
- CLAIM A3 bad-count == 0 (deterministic collapse to origin, N steps);
- CLAIM B: Σ conf(N) f(C) == D(N+1) for every N in range.

If any of these fails, the reverse structure is NOT canonical and the
collapse-tree bijection is wrong.  This is a cheap, decisive check against
the run's own verified D(0..14).

## Why this beats the alternatives
- **vs BFS / exact enumeration**: cost independent of the frontier (which is
  what caps at N=14).  The recurrence sums over configurations, so it still
  needs a way to count without enumerating — CLAIM C is that way.
- **vs holonomic / linear-recurrence fitting** (already dead): D(N) has no
  small-order holonomic or constant-coefficient recurrence (proven dead), so
  no closed-form fit will ever validate against D(20)/D(100).  A structural
  transfer DP is the only route consistent with the 2D precedent (A007902
  also has only a two-index DP, no closed form).
- **vs naive directed-animal count** (C1, dead): reachability is far stricter
  than origin-connectivity; the voidance/top-cap constraint is precisely the
  difference and is what a correct DP must encode.

## Honest status of each piece
- **Sourced**: Eriksson n=3 game identity, Thm 9 (configs=voidance sets=folded
  polyominoids), Prop 24 (no double play).  These are on the source's word;
  the run's own reverse-merge check corroborates on all BFS-reachable d=3
  configs it reaches.
- **Hand-verified observation (not yet machine-confirmed)**: every histogram
  ends in "3", the unique-cap collapse.  To be confirmed by
  `check_recurrence.py` before trusting.
- **Speculative**: the exact two-index DP that makes CLAIM C summable without
  enumerating configs.  I name the object (voidance-set / folded-polyominoid
  height-profile DP) but have not derived its transfer rule.  This is the
  announced seam; its falsifier is that it must reproduce D(14) then
  D(20)=9204559704 and D(100) mod 10^9 = 780166455.
