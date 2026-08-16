# Approach: resolvability / 1-factorization of the triangle geometry (a spread of the partial Steiner triple system)

```approach
idea: Attack the triangle geometry (partial STS(99): 99 points, 231 lines of
  size 3, 7 lines per point) through its RESOLVABILITY structure — whether the
  231 triangles can be partitioned into 7 spreads (parallel classes), each a
  partition of the 99 points into 33 disjoint triangles, and what a single
  spread forces on the rest via the lambda=1, mu=2 collinearity graph.
mechanism: A spread (or "parallel class") is a set of 33 pairwise disjoint
  triangles covering all 99 points. Each vertex lies on exactly 7 triangles,
  so a full factorization into 7 spreads is exactly a 1-factorization of the
  triangle hypergraph — the triangle analogue of a Kirkman triple system
  (KTS), but for a partial STS. The mu=2 condition then couples spreads: any
  two points in different triangles of one spread have exactly 2 common
  neighbours, and a counting/design argument (the classical KTS / resolvable
  STS machinery, Moore graph / Bruck–Ryser style congruences, or the
  factorization-number congruences of resolvable designs) constrains whether
  7 parallel classes can close up. This is NOT the g-reduce line (which fixed
  one vertex and split triangles by distance); it is a global partition
  question whose named object is the RESOLVABLE partial Steiner triple system,
  with the doily GQ(2,2) = srg(15,6,1,3) and its spreads as the small model.
  The 99-specific number is 33 triangles per spread = 99/3, with 7 spreads;
  rook(9) would have spreads of size 3 (= 9/3) with 2 spreads (k/2 = 2), and
  BvLS(243) spreads of size 81 with 11 spreads — so a parity/congruence on the
  spread number or block count per spread can separate the three.
status: grounded
speculative: medium-high — the existence of even ONE spread in a putative
  99-graph is itself open, and the factorization is not known to exist; but
  that is the lever: either a spread is forced (then its structure is usable)
  or it is impossible (then nonexistence), and the question is finite-local.
precedent:
  - Ray-Chaudhuri & Wilson, "Solution of Kirkman's schoolgirl problem", Proc.
    Sympos. Pure Math. XIX (1968): a KTS (resolvable STS) exists iff v === 3
    (mod 6). NAMED EXISTENCE THEOREM for resolvability of FULL STS. CAUTION:
    this governs full Steiner triple systems (every point pair on a block); the
    triangle geometry of an srg(99,14,1,2) is a PARTIAL STS (replication 7, only
    adjacent point pairs joined by a triangle-line), so the theorem does not
    directly apply. v=99 == 3 (mod 6) is consistent but the hypothesis (full
    STS) fails here.
  - Stinson, "On partial parallel classes in partial Steiner triple systems",
    Discrete Math. 344 (2021), DOI 10.1016/j.disc.2020.112279 : the exact
    framework — partial parallel classes (PPC) in PARTIAL STS, with bounds on
    the maximum PPC size. This is the right named object for the 99 triangle
    geometry and supplies the counting vocabulary (a spread = a parallel class
    of 33 disjoint blocks; border beta(rho,v)). No result here is specialized to
    v=99, but it confirms the geometry is a legitimate resolvable-PSTS question.
  - Colbourn, Magliveras, Mathon (Math. Comp. 1992), DOI 10.1090/S0025-5718-1992-1106962-5 :
    the computational method the approach's first-step proposes — build a
    block-nonintersection graph (vertices = blocks/triangles, edges = disjoint
    blocks) and read off parallel classes as cliques. For STS(27) they find
    248 transitive KTS. Confirms the clique-in-nonintersection-graph method is
    standard and computable on exactly this object shape (99 points -> 231
    nonintersection graph vertices).
  - Buratti & Pasotti, "Heffter Spaces" (arXiv:2401.03940) : resolvable partial
    linear spaces whose parallel classes are Heffter systems; collinearity graph
    of a resolvable PLS is regular of degree = sum of block sizes. A live modern
    construction framework for resolvable partial linear spaces, though not
    specialized to mu=2 collinearity.
verdict: The reformulation is GROUNDED as a genuine, named class — resolvability
  of a partial STS and its parallel classes is a real theory (Stinson PPC;
  KTS; block-nonintersection cliques). The 99-specific numbers (7 spreads of 33
  triangles each = 231) are a legitimate finite-local question. BUT the
  literature gives NO answer and NO positive bound special to (99,14,1,2):
  the KTS existence theorem does not apply because the geometry is PARTIAL not
  full; Stinson's bounds are asymptotic/general and do not pin mu=2; and whether
  even ONE spread exists in a putative (99,14,1,2) is open. So the approach is
  not refuted, but it is also not supported toward a conclusion — it is a
  computation this run must do (count spreads in rook(3)=spreads of 3
  triangles, bvls(243)=spreads of 81, and see whether the mu=2 coupling permits
  7 spreads of 33 at 99). No dead end is known; the parity/congruence lever on
  the spread number is unstated in the literature and is the novel part.
first-step: (1) Build the spread-finder in code/lib: enumerate maximal sets of
  pairwise disjoint triangles; run it on rook(3) (spreads of 3 triangles) and
  bvls(243) (spreads of 81) to see whether spreads exist there and how many.
  (2) Count, in a putative (99,14,1,2), how many spreads must pass through a
  fixed triangle or a fixed edge using only lambda=1/mu=2 arithmetic, and
  check the congruences the resolvable-STS theory imposes on 33-block classes.
```

## Why this differs from the closed g-reduce line

g-reduce fixed a *vertex* and partitioned triangles by distance from it (through
/ cross / outer). This line partitions triangles by *disjointness* into parallel
classes, a global 1-factorization of the hypergraph, which is the object KTS
theory names. The mu=2 coupling across a spread is a different set of equations
from the vertex-derived design, and the small model is the doily (which has
spreads) rather than the rook's graph.
