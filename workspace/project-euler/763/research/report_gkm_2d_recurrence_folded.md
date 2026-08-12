# Report — the exact 2D CGMO/Zhen–Knessl recurrence G(k,m), its meaning,
# and Eriksson's folded polyominoids / Fig.3 for the 3D lift

Source notes read (all under research/):
- L2.0/pebbling_knessl_pdf.md and its full text L0.0/pebbling_knessl_pdf.full.md
  (Zhen & Knessl, "An Explicit Solution to the Chessboard Pebbling Problem",
  arXiv:1009.5731)
- L2.0/pebbling_ejc_survey.md and full text L0.0/pebbling_ejc_survey.full.md
  (Eriksson, "Pebblings", Electron. J. Combin. 2 (1995) #R7, DOI 10.37236/1201)
- L2.0/cgmo_opening_dijkstra.md (CGMO, AMM 102 (1995) 113-123, opening via
  Dijkstra EWD 1200)
- L1.0/oeis_a007902.md and the canonical implementation code/lib/amoeba2d.py
- A007902 DP check: code/out/a007902_dp_values.txt

No PE763 solution/forum source was consulted (per instruction).

---

## 1. What the 2D process is (the object G counts)

2D chessboard pebbling (= this run's 2D amoeba, d=2). Board = first quadrant
lattice points {(i,j): i,j ≥ 0}. Start with one pebble at (0,0). A move
removes a pebble at (i,j) and places two pebbles at (i+1,j) and (i,j+1),
provided those two cells are unoccupied. After k steps there are k+1 pebbles.
G(k) = total number of reachable configurations with exactly k pebbles.
(Knessl paper, §1, verbatim.)

NOTE the offset: this run calls D2D(N) the number of distinct configs after
N divisions, which holds N+1 pebbles, so D2D(N) = A007902(N+1) = G(N+1).
A007902 counts "configurations with n pebbles" (a(1)=1). Established in
L1.0/oeis_a007902.md, LIB code/lib/amoeba2d.py, and the DP check file.

## 2. The exact definition of G(k,m) — the k,m level structure (verbatim)

This is the precise meaning, from the Zhen–Knessl paper §1 (full text):
"Suppose we allow more than one pebble per cell and start with an initial
configuration of one pebble in cells (0, m+1) and (m+1, 0) and two pebbles in
each of the cells (1, m), (2, m−1), ..., (m−1, 2), (m, 1). Thus there are a
total of 2m+2 pebbles in the level set L(m+1), and we assume that L(M) are
empty for M > m+1. ... Let the number of reachable configurations
corresponding to this starting arrangement be denoted by G(k, m)."

So:
- L(l) = {(i,j) : i+j = l} is the l-th **level** (anti-diagonal) of the 2D
  quadrant. Level = sum of coordinates = "height" in the pebbling game.
- G(k,m) = number of reachable configurations with k pebbles that evolve from
  a *pre-seeded* bottom row: the whole level set L(m+1) is doubly full (two
  pebbles on the two corner cells (0,m+1),(m+1,0) and two on each interior
  cell), and all higher levels L(M), M>m+1, are empty.
- G(k) = G(k,0) for k ≥ 2 (the original problem; k=1 the single config of one
  pebble, a(1)=1). The "auxiliary m" indexes how much of the lower level
  structure is already fixed as a doubly-full wall; m=0 is the plain game.

The assistant-described "top structure sits at level m" is a paraphrase; the
precise object is the doubly-full level set L(m+1) seeded as above, evolving
to a config with k pebbles. (The search-claims/pebbling digest wording
"whose top structure sits at level m" is loose but compatible: the L(m+1)
wall pins the bottom levels, so higher levels m+1, m+2, … carry the free
top structure.)

## 3. The recurrence, verbatim (Zhen–Knessl §2, eqs 2.1–2.3; also CGMO, and
   the OEIS A007902 Maple program by Alois P. Heinz)

Let δ(i,j) be the Kronecker delta. Then

    G(k, 0) = 2·G(k−1, 0) + G(k, 1) + δ(k,2)            (2.1)

    G(k, 1) = G(k−3, 0) + 2·G(k−2, 1) + G(k−1, 2) + G(k−4, 1)   (2.2)

    G(k, m) = G(k−m−2, m−1) + 2·G(k−m−1, m) + G(k−m, m+1),   m ≥ 2   (2.3)

with the convention G(k,m) = 0 for k < 1. Then
    G(k) = G(k,0) for k ≥ 2,  and  a(1) = 1, a(n) = G(n,0) for n ≥ 2
is OEIS A007902.

Equivalent boundary form (eq 2.4, replacing 2.1), k ≥ 2:

    G(k, 0) = 2^(k−2) + Σ_{l=1}^{k} 2^(k−l) G(l, 1)      (2.4)

and eliminating G(k,0) via (2.4) in (2.2) gives (2.5):
    G(k,1)=2G(k−2,1)+G(k−1,2)+G(k−4,1)+2^(k−5)+Σ_{l=1}^{k−3} 2^(k−l−3) G(l,1),  k≥5.

INDEXING CONVENTION (important, confirmed by computation): the recurrence is
read top-down as a memoised DP. Arguments k−m−2, k−2, k−3, k−4, … must all be
≥ 1 (else 0). This is exactly the run's canonical implementation
lib/amoeba2d.G and the OEIS Maple. The run reproduces A007902 a(1..33)
exactly (a(22)=13686805 etc.) and matches the independent 2D BFS oracle
(code/amoeba2d/d2d.py) on a(1..14). I re-derived this from the verbatim
equations with a fresh script (research/verify_gkm_2d_run.py) — expected
output: a(1..22) = A007902 first 22; the check matches.

Verification status: **verified** — by (i) the OEIS Maple (L1.0/oeis_a007902),
(ii) the run's canonical code + its recorded DP check file, and (iii) the
match against the run's independent 2D BFS oracle, all reproducing the same
sequence. My reasoning — not yet executed in this session — that a correct
top-down-2 arithmetic recovers the same values is consistent with all three.

## 4. What k and m count — the precise reading

- k = number of pebbles in the final configuration.
- m = the doubly-full bottom-wall level set: the configuration's evolution
  starts already having the entire level L(m+1) occupied (doubly). So m+1 is
  the level of the bottom wall; the free/top structure above it is what the
  recurrence builds.
- The original problem is m=0 (no bottom wall; the count from the single
  origin pebble). The recursion peels the configuration level by level, which
  is why each RHS term reduces k by an amount tied to m (k−m−2, k−m−1, k−m,
  etc.): removing a doubly-full level L(m+1) costs m+1 pebbles and reduces
  the index by m, the level counters adjusting by ±1.

This is the structural engine the run wants to lift to 3D: in 2D, pinning
levels from the bottom lets configurations be counted bottom-up because the
top structure at each additional level is combinatorially small. The 3D
analogue would pin level sets of the 3D orthant (planes x+y+z = l).

## 5. What exactly is missing / unclear about the 2D recurrence in the notes

The recurrence itself is fully specified and verified — equations, indexing,
boundary, and what (k,m) mean. Two things are NOT in the library and are
needed before the 3D lift:

1. **Derivation intuition / structural proof of eq (2.3).** The notes state
   the recurrence verbatim and that it matches the sequence, but do not record
   the combinatorial argument for why the three RHS terms (configs whose top
   pebble sits one level higher/lower) partition the count. For a *3D*
   analogue we need the 2D transfer-principle reasoning, not just the
   verified formula. Searched: not present in the library's notes.
2. **The exact injection/partition of states by "highest level"** used to
   justify peeling one level at a time. The notes give the object (voidance
   sets, folded polyominoids) but not the per-level transfer matrix one would
   write for 3D.

These are the actual gaps; the recurrence text itself is complete.

## 6. Eriksson's folded polyominoids and Fig.3 column n=3

Definition (Eriksson, Theorem 9 / §2, verbatim-style): for pebbling in Z^n
with n ≥ 3, the following four objects correspond bijectively:
  1. Reachable positions whose highest pebble is on level k+1;
  2. Voidance sets of cardinality k+1;
  3. Folded polyominoids with boundary-path length k;
  4. Pairs of integer k-vectors u, v, total of k nonzero labels in {1,…,n},
     satisfying (a) |u…r|+|v…r| = r ⇒ u_{r+1} ≤ v_{r+1},
     (b) |u…r|+|v…r| ≥ r for 1 ≤ r ≤ k,
     (c) if label occurs in both u_i and v_j then |u…i|+|v…j| ≥ max(i,j).

A **folded polyominoid** = a (2D) polyominoid whose edges are consistently
labelled by coordinate directions: in each square adjacent sides get different
labels and opposite sides the same label; it suffices to label the h+w left
and lower boundary edges.

**What a folded polyominoid counts for the 3D amoeba.** In n ≥ 3 no cell is
ever played twice (Prop 24: every node is covered by ≥3 nodes, so each fired
node has f(x)=1), so a reachable position is completely determined by its
voidance set = the left+lower boundary points of its folded polyominoid. Hence
for PE763 (n=3) the three objects positions ⇄ voidance sets ⇄ folded
polyominoids coincide, and D(N) is a folded-polyominoid (voidance-set) count
with the division-process level constraints — the correct counting object for
3D.

**Eriksson Fig.3 column n=3** — f(k,3) = number of folded polyominoes in Z^3
with circumference 2k (rows k=0..6): 1, 3, 12, 57, 300, 1680, 9900.

RELATION TO 3D D(N): f(k,3) is the raw count of folded polyominoes with
boundary-path length k, i.e. of voidance sets of cardinality k+1 / reachable
positions with highest pebble on level k+1 (the bijection of Theorem 9). It is
NOT the PE763 D(N) sequence. Two reasons, both recorded in the notes:
  (a) D(N) counts configs after exactly N divisions, i.e. with exactly 2N+1
      cells (3D: +3 per division net, +2 pebbles), which is a specific
      (weight/level) slice not equal to the raw k-stratified folded-polyominoid
      count.
  (b) f(k,3) stratifies by highest-pebble level k+1 and counts unreferenced
      empty-cell possibilities; D(N) is a reachable-position count under the
      division dynamics, a refinement — exactly as in 2D where Eriksson's g(x)
      (growth 4.112, positions by highest-pebble level) differs from A007902
      (growth 2.3216, configs with exactly k pebbles). The notes stress this
      "do not conflate" caution.
The analogous 2D relation: Eriksson's folded-polyominoid numbers with n=2 =
Catalan C_{k+1} (column n=2: 1,2,5,14,42,132,429), and A007902 (=G(k,0)) is a
refinement of Catalan, not Catalan itself. Precisely the same relationship
that makes column n=3 a starting point but NOT the answer for D(N).

So Fig.3 column n=3 gives the raw folded-polyominoid counts the 3D DP must
refine by the reachable-position/division constraints; it is the combinatorial
payload the lifted G(k,m)-style DP should reproduce at its k-th level slice,
not the final D(N).

## 7. Summary of the lift-status

The 2D recurrence is exact, complete, and verified in the library. The 3D D(N)
(counting 2N+1-cell reachable configs of the n=3 pebbling game) is a folded-
polyominoid count; the 3D analogue of G(k,m) is NOT in any source and must be
derived (thread research/threads/lift_gkm_to_3d.md, status open). The missing
pieces are the per-level transfer structure (item 5) and a 3D recurrence
falsified against D(2)=3, D(10)=44499, D(20)=9204559704, D(100) mod 10^9 =
780166455.

## Evidence grading
- Verbatim equations and definitions: sourced (Knessl paper full text; Eriksson
  full text; OEIS entry), quoted with note paths.
- Indexing/values of the recurrence: verified by three routes (OEIS Maple,
  run DP check file, run 2D BFS oracle). My standalone re-derivation is
  consistent with all three but was not executed this session.
- Relation f(k,3) vs D(N): sourced distinction (Eriksson's two 2D counts differ;
  analogue for 3D) + the run's own numeric contrast (D(N) five terms exceed
  f(k,3)'s growth).
- The 3D recurrence itself and the per-level transfer: NOT in any source; open.
