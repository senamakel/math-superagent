# The 2D chessboard-pebbling characterization, and the ladder to 3D (PE763)

## Answer to the question, in one paragraph

In dimension 2 the reachable pebbling configurations (this run's 2D amoeba) are
exactly the positions whose played cells form a **polyominoid** — the set of
sites on-or-between two lattice paths with a common start and end — and each
such position is bijectively represented by its **voidance set** = its left and
lower boundary points (with the crossing/double-play subtlety that makes 2D
hard). In dimension n ≥ 3 (which includes this run's 3D PE763 process) the
structure *simplifies*: the same four-way bijection holds between reachable
positions, voidance sets, **folded polyominoids** (a polyominoid whose edges
are consistently labelled by the n coordinate directions), and pairs of
labelled k-vectors u,v — and, crucially, in n ≥ 3 **no cell is ever played
twice**, so a reachable position is completely determined by its voidance set
(= the left+lower boundary points of its folded polyominoid), and the
reachable-position count collapses onto the folded-polyominoid count. This is
the exact machinery the 3D D(N) can (and should) be built on.

---

## 1. What a reachable configuration is (structural characterization)

### 2D: polyominoids and voidance sets
**Definition (Eriksson, "Pebblings", EJC 2 (1995) #R7, §2).** A **polyominoid
set** in Z² = all points on or between two lattice paths with a common starting
point and common ending point. Call (x,y) a **left boundary point** if
(x−1,y) ∉ polyominoid and a **lower boundary point** if (x,y−1) ∉ polyominoid.

- **Observation 6.** Polyominoids correspond bijectively to *parallelogram
  polyominoes* (Delest–Viennot): translate the left path up one step, the lower
  path right one step, rejoin endpoints.
- **Proposition 8.** The points played in a pebbling game on Z² form a
  polyominoid.
- **Proposition 7.** Number of polyominoid sets whose two lattice paths each
  have length k (i.e. k+1 left+lower boundary points) is the **Catalan number**
  C_{k+1} = 1/(k+2)·C(2k+2, k+1).
- The **voidance set** of a (finite) game = all points that at some stage were
  pebble-points but end up empty. For a polyominoid of height h and width w the
  voidance set = the h left + w lower boundary points, cardinality w+h+1.
- **Prop 20 (the pivotal bijection).** There is a one-to-one-to-one
  correspondence between **reachable positions, shot counts and voidance
  sets.** So counting reachable positions = counting voidance sets.

**The 2D subtlety (why 2D is hardest — Eriksson Theorem 10).** In Z² a cell may
be played *twice*: it receives two pebbles (has both left and lower neighbours
in the polyominoid) and is later emptied (its right and upper neighbours are
left/lower boundary points); such a **crossing** is a singleton on its level,
and the second play replaces two old voidance points by one new one. Reachable
*positions* therefore correspond to folded polyominoids with an *arbitrary
subset of their crossings marked as voidance points*, with generating function
```
g(x) = (1 − 6x + 4x² + 4x³ + √(1−4x²)) / (2(1 − 6x + 8x² − 4x⁴))
     = 1 + 2x + 5x² + 14x³ + 43x⁴ + 140x⁵ + …
```
growth constant G ≈ 4.112. **This is the bounding object of the 2D reachable
sequence = OEIS A007902.** (Voidance sets alone have the different GF
h(x) = 1+2x+5x²+15x³+51x⁴+…, growth 4.147, matching CGMO's minimal-unavoidable
constant.)

### n ≥ 3: folded polyominoids — the 3D case (Eriksson Theorem 9)
For the n-dimensional game (a pebble at (x_1,…,x_n) → n pebbles one unit out
in each positive coordinate, all n targets empty), with n ≥ 3, the following
are in bijection:
1. **Reachable positions** with highest pebble on level k+1;
2. **Voidance sets** of cardinality k+1;
3. **Folded polyominoids** with boundary-path length k;
4. **Pairs of integer k-vectors u, v** with a total of k nonzero labels in
   {1,…,n} satisfying the three conditions (a)–(c) given there.

A **folded polyominoid** = a (2D) polyominoid whose edges are consistently
labelled by coordinate directions: in each square adjacent sides get different
labels and opposite sides the same label; it suffices to label the h+w left and
lower boundary edges (h+w labels over the 2k places of the two vectors u,v).

**Why n ≥ 3 is simpler (Eriksson Prop 24).** In higher Z^n every node is
covered by at least three nodes, so **no node is ever fired twice** and
every fired node has f(x)=1. Consequently the voidance set = exactly the
left+lower boundary points of the folded polyominoid, and *positions, voidance
sets and folded polyominoids all coincide* — there are no crossings to mark.
This is precisely the regime of this run's 3D PE763 process (3 children per
split, the n=3 pebbling game of Vaderlind/Eriksson). So the 3D reachable-
position count D(N) is a folded-polyominoid count with the additional
"reachable-position" constraints from the division process, exactly as g(x)
is a refined Catalan/voidance count in 2D.

Eriksson's Fig. 3 gives the raw count f(k,n) of folded polyominoes in Z^n of
circumference 2k (rows k=0..6, columns n=1..6), with column n=2 giving the
Catalan numbers and row k=2 the values n(3n−1)/2 — a table the research note
research/L2.0/pebbling_ejc_survey.md reproduces and indexes.

---

## 2. Generating function and how the 2D sequence is computed

There is **no elementary closed form**; the 2D sequence A007902 has:

1. **An exact structural recurrence** (CGMO; the OEIS entry's Maple program) via
   the auxiliary G(k,m) — the number of reachable configs with k pebbles whose
   top structure sits at level m:
   ```
   G(k, 0) = 2·G(k−1,0) + G(k,1) + δ(k,2)
   G(k, 1) = G(k−3,0) + 2·G(k−2,1) + G(k−1,2) + G(k−4,1)
   G(k, m) = G(k−m−2, m−1) + 2·G(k−m−1, m) + G(k−m, m+1),   m ≥ 2
   ```
   with a(n) = 1 for n=1, a(n)=G(n,0) for n ≥ 2. This reproduces the full 2D
   amoeba sequence (verified against the run's 2D BFS oracle: a(n+1) = D2D(n)).
   (Also writable as G(k,0) = 2^(k−2) + Σ_{l=1}^k 2^(k−l) G(l,1).)

2. **An exact contour-integral formula** (Zhen & Knessl, arXiv:1009.5731,
   Theorem 2.1 / Corollary 2.1): G(k) = 2^(k−2) +
   (1/2πi)∮_C (2^k − z^{−k})/(1−2z) V_1(z) dz, with V_1 and the q-series S(z)
   as given in that paper.

3. **Asymptotics** (Knessl 2008; Zhen–Knessl 2010; on the OEIS entry):
   a(n) ~ c·d^n with d = 2.3216421994942297… , c = 0.12268707342148599…
   (equivalently G(k) ~ c*·a^k, a = 1/z_* where z_* ≈ 0.430729593137930 is the
   unique root |z_*|<1/2 of S(z)=0). The constant is characterised by a
   continued-fraction / Jacobi-elliptic transcendental equation.

---

## 3. How the problem generalizes to higher dimensions (the 3D setup)

The n-dimensional game (Vaderlind, in Eriksson §2): board = first orthant of
Z^n, one pebble at origin, a move replaces a pebble by n pebbles one unit out
in each positive coordinate direction, all n targets empty, parent removed.
The 3D PE763 process is exactly this at n=3. The generalisation of the *2D*
machinery is:

- **Weight invariant.** Weight of a pebble at (x_1,…,x_n) is n^{-(x_1+…+x_n)};
  total weight 1 invariant. (In 2D this is 2^{-(i+j)}, giving CGMO's Lemma 1.)
- **Unavoidable sets / level trimming** (Props 4, 13): X unavoidability is
  decided by level trimming, with the "no 3-pebble point" criterion.
- **Reachable position ≡ voidance set ≡ folded polyominoid** (Theorem 9, n≥3),
  which is the counting object to set up for 3D.
- **Eriksson Prop 1.** In Z^n (n≥3) the origin plus its three neighbour points
  is unavoidable — the 3D analogue of the 2D L(1)∪L(2) fact.

The difference from 2D is decisive and in the 3D run's favour: no node is
played twice in n ≥ 3, so the crossing-marking combinatorics (the hard part of
the 2D GF g(x)) disappears, and the reachable-position count equals the folded-
polyominoid (voidance-set) count. This is the structural handle the run should
exploit for D(10000).

---

## Sources (all fetched and filed under /workspace/research)

- **H. Eriksson, "Pebblings", Electron. J. Combin. 2 (1995) #R7** — the primary
  structural source (polyominoids, crossings, folded polyominoids, Theorem 9).
  https://www.combinatorics.org/ojs/index.php/eljc/article/view/v2i1r7/pdf ;
  https://doi.org/10.37236/1201
  (full text: research/L0.0/pebbling_ejc_survey.full.md; digest:
  research/L2.0/pebbling_ejc_survey.md)
- **Chung, Graham, Morrison, Odlyzko, "Pebbling a chessboard", Amer. Math.
  Monthly 102 (1995) 113-123** — original; opening pages exactly transcribed
  in Dijkstra EWD 1200. DOI 10.2307/2975345; full scan (no text layer) at
  https://fanchung.ucsd.edu/mypaps/fanpap/150chess.pdf ; transcription:
  https://www.cs.utexas.edu/~EWD/transcriptions/EWD12xx/EWD1200.html
  (digest: research/L2.0/cgmo_opening_dijkstra.md;
  full: research/L0.0/cgmo_opening_dijkstra.full.md)
- **Q. Zhen & C. Knessl, "An Explicit Solution to the Chessboard Pebbling
  Problem", arXiv:1009.5731** — exact recurrence and contour formula for 2D.
  https://arxiv.org/pdf/1009.5731
  (full: research/L0.0/pebbling_knessl_pdf.full.md; digest: research/L2.0/pebbling_knessl_pdf.md)
- **C. Knessl, Math. Comput. Modelling 47 (2008) 127-139** — asymptotics,
  growth constant (via the OEIS entry / MaRDI DOI 10.1016/j.mcm.2007.02.010).
- **OEIS A007902** — the 2D reachable-position sequence and its recurrence.
  https://oeis.org/A007902

## Evidence grading
- **Sourced theorems:** polyominoid ⇄ voidance/position bijections (Eriksson
  Props 7, 8, 20), the 4-way folded-polyominoid bijection for n≥3 (Eriksson
  Thm 9), "no node fired twice in n≥3" (Eriksson Prop 24), the 2D GFs g,h
  (Eriksson Thm 10), the CGMO weight/level-trimming Lemmas 1-3 & Thm 1
  (transcribed verbatim), the Knessl exact recurrence/formula/constants.
  All directly quoted above with URLs.
- **Computed cross-checks** (this run, small N only): the G(k,m) recurrence
  reproduces the run's 2D BFS oracle D2D(0..14); reverse-merge reducibility to
  {origin} holds on every config the forward BFS reaches in d=2 and d=3; the 2D
  sequence matches A007902 via direct OEIS lookup.
- **Not otherwise verified / heuristic:** the *closed* walk from folded-
  polyominoid count to the specific numeric D(N) of PE763 is not made here; the
  run's own BFS data (D(N) up to N=14) remains the numeric source of truth.
