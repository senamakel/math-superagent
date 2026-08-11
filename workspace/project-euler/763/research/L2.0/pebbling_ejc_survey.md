# Pebblings — Eriksson, Electron. J. Combin. 2 (1995) #R7

<!-- source: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v2i1r7/pdf/ -->
<!-- DOI: https://doi.org/10.37236/1201 ; PDF: https://www.combinatorics.org/ojs/index.php/eljc/article/view/v2i1r7/pdf -->

**The pivotal structural source for this run: it characterises reachable
pebbling configurations in every dimension, and gives the exact object (the
folded polyominoid) that the 3D PE763 amoeba configs should be counted by.**

Strengthens and generalises Chung–Graham–Morrison–Odlyzko's chessboard
pebbling. Two-dimensional result first, then the n-dimensional generalisation.

## The n-dimensional pebbling game (Vaderlind's version, §2)

Board = integer grid points of the first orthant in Z^n. Start with one pebble
at the origin. A *legal move* replaces a pebble at (x_1,…,x_n) by n pebbles,
one unit out along each positive coordinate direction. The **weight** of a
pebble at coordinates (x_1,…,x_n) is `n^{-(x_1+…+x_n)}`; total weight is
invariant under a move.

**Proposition 1.** The four-point set in Z^n (n ≥ 3) consisting of the origin
and its three neighbour points is *unavoidable* (every game position carries a
pebble in it). Proved by emptying that unit cube's four points and forcing
pebbles onward.

**Fact 3 / Prop 4 (level trimming).** The *level* of an orthant point is the
sum of its coordinates. There is an order-independent *level-trimming*
procedure: at each level perform the moves needed to strip all pebbles from a
point in X, or all-but-one from a point not in X. A set X is unavoidable iff
level trimming can go on forever without running out of pebbles; equivalently
(Prop 4) no point ever accumulates ≥ 3 pebbles when trimming levels 1..n−k.

## Voids, shot counts, and the key bijection (Proposition 20)

The **voidance set** of a (finite) game = all points in Z^n that were at some
stage pebble-points but end up empty.

- **Fact 5 / Prop 20.** A reachable game *position* is completely specified by
  its voidance set; more sharply there is a *one-to-one-to-one correspondence*
  between **reachable positions, shot counts** (records of how many times each
  node was fired) **and voidance sets**.
- This is the structural heart: instead of counting arrangements, count
  voidance sets (or shot counts), which are far more tractable objects.

## The 2D characterisation: polyominoids (§2, Props 7–8)

The points played in a 2D pebbling game form a **polyominoid set**: all points
on or between two lattice paths with a common start and common end point.
The corresponding voidance set = the set of **left and lower boundary points**
of those two paths (a left boundary point (x,y) has (x−1,y) ∉ polyominoid; a
lower boundary point has (x,y−1) ∉ polyominoid). A polyominoid with height h
and width w has h left + w lower boundary points, voidance set size = w+h+1.

- **Observation 6.** Polyominoids correspond bijectively to *parallelogram
  polyominoes* (Delest–Viennot): translate the left path up one step, the
  lower path right one step, rejoin the endpoints.
- **Proposition 7.** Number of polyominoid sets whose lattice paths each have
  length k (i.e. with k+1 left+lower boundary points) is the **Catalan number**
  C_{k+1} = 1/(k+2)·C(2k+2, k+1). (Continuous-Catalan, the classical
  non-crossing-lattice-path count in the parallelogram-polyomino world.)

**Theorem 10 (2D, folded polyominoids + crossings).** For pebbling in Z^2,
reachable positions with the highest pebble on level k+1 correspond bijectively
to **folded polyominoids** with boundary-path length k, with *any subset of the
CROSSINGS* marked as voidance points. (A *crossing* is a point played twice: it
must receive 2 pebbles, i.e. have both left and lower neighbours in the
polyominoid, and be emptied — a singleton on its level; the second play
replaces two old voidance points by one new one.)
- The g.f. g(x) for these *positions* has series 1+2x+5x²+14x³+43x⁴+140x⁵+⋯
  and asymptotic g_k ~ C·G^k, G ≈ 4.112.
- The g.f. h(x) for *voidance sets* of cardinality k+1 has series
  1+2x+5x²+15x³+51x⁴+187x⁵+⋯, growth H ≈ 4.147 — identical to CGMO's
  minimal-unavoidable growth constant (Prop 21: a minimal unavoidable set = a
  voidance set plus one extra point that makes level trimming infinite).

NOTE (important): Eriksson's g,k are stratified by the *highest-pebble level*
and count *positions* (including stopped ones with empty cells); they are NOT
the OEIS A007902 sequence (which this run calls D2D), though both are 2D
reachable-configuration counts. A007902/growth 2.3216 counts *configurations
with exactly k pebbles*; Eriksson's g has growth 4.112. The polynomial closed
forms for g,h are OCR-mangled in the full-text conversion (constant terms do
not check out), so only the series heads and growth constants are trusted
here; the run's own 2D oracle values are concrete and verified.

## The 3D (and higher) characterisation: folded polyominoids (Theorem 9)

For pebbling in Z^n with n ≥ 3, the following four objects correspond
bijectively to each other:

1. **Reachable positions** whose highest pebble is on level k+1;
2. **Voidance sets** of cardinality k+1;
3. **Folded polyominoids** with boundary-path length k;
4. **Pairs of integer k-vectors u, v**, with a total of k nonzero elements
   (labels) in {1,…,n}, satisfying the three conditions
   (a) if |u…r| + |v…r| = r then u_{r+1} ≤ v_{r+1},
   (b) |u…r| + |v…r| ≥ r for all 1 ≤ r ≤ k,
   (c) if the same label occurs in u_i and v_j then |u…i| + |v…j| ≥ max(i,j).

A **folded polyominoid** in Z^n is defined by a *consistent labelling* of the
edges of an (ordinary 2D) polyominoid with coordinate directions: for each
square, adjacent sides have different labels, opposite sides the same label.
It suffices to label the h+w edges on the left and lower boundary (h+w labels
distributed over the 2k places of the two k-vectors u and v).

(Full proof of the bijection is a corollary of Prop 27; in n ≥ 3 no node is
played twice — Prop 24 (f(x)=1 for every fired node, the support has
∧-completion) — so the voidance set = all left+lower boundary points of the
folded polyominoid, cardinality k+1.)

Eriksson's Figure 3 tabulates f(k,n) = number of folded polyominoes in Z^n
with circumference 2k, rows k=0..6, columns n=1..6:

```
           n=1  n=2  n=3   n=4    n=5     n=6
k=0         1    1    1     1     1       1
k=1         1    2    3     4     5       6
k=2         1    5   12    22    35      51
k=3         1   14   57   148   305     546
k=4         1   42  300  1126  3045    6756
k=5         1  132 1680  9220 32985   91236
k=6         1  429 9900 79972 368665 1228575
```

Column n=1 is identically 1 (1D has no reachable positions, per Prop 4 note).
Column n=2 gives **Catalan numbers C_{k+1}** (1,1,5,14,42,132,429) — matching
Prop 7. Row k=2 equals `n(3n−1)/2` (1,5,12,22,35,51 for n=1..6); each row k is
a degree-k polynomial in n. This is the directly relevant object for the 3D
PE763 amoeba: its configs should be an n=3 column-like counting problem of
folded polyominoids, though the PE763 *reachable-position* count (which allows
the level-histogram constraints of the division process) is a refinement of
the raw folded-polyominoid count, exactly as g(x) refines the Catalan count in
2D.

## Why the 2D game is the subtle one

Eriksson stresses that the *position* characterisation is **harder in the
plane** than in higher dimensions, because in higher Z^n every node is covered
by ≥ 3 nodes so no node is ever fired twice (Prop 24), whereas in 2D a node may
be played twice (a crossing). This is why the 2D reachable-position GF g(x)
involves the marked-crossing combinatorics and a different growth constant
(4.112) than the voidance counts (4.147). For n ≥ 3 the two coincide (folded
polyominoid = voidance set), which is the simplification the 3D PE763 count can
exploit.

## Sources
- Eriksson, "Pebblings", Electron. J. Combin. 2 (1995) #R7.
  https://www.combinatorics.org/ojs/index.php/eljc/article/view/v2i1r7/pdf
- DOI: https://doi.org/10.37236/1201
- Underlying: Delest & Viennot (parallelogram polyominoes / Catalan);
  Gessel & Viennot (lattice-path determinants).
