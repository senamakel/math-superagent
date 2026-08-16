<!-- source: https://arxiv.org/pdf/2512.24061 | converted from PDF -->

Notes on the 33-point Erdős–Szekeres problem

Dumitru Bogdan ∗

December, 2025

Abstract

The determination of ES(7) is the first open case of the planar Erdős–Szekeres problem,
where the general conjecture predicts ES(7) = 33. We present a SAT encoding for the 33-
point case based on triple-orientation variables and a 4-set convexity criterion for excluding
convex 7-gons, together with convex-layer anchoring constraints. The framework yields UN-
SAT certificates for a collection of anchored subfamilies. We also report pronounced runtime
variability across configurations, including heavy-tailed behavior that currently dominates
the computational effort and motivates further encoding refinements.

Keywords: Erdős–Szekeres problem, SAT solving, discrete geometry, convex layers, order
types, automated reasoning.

1 Introduction

In their seminal 1935 paper, Erdős and Szekeres investigated the smallest integer ES(k) such
that any set of ES(k) points in the plane in general position (no three collinear) contains k
points in convex position [1]. They conjectured the exact formula

ES(k) = 2k−2 + 1 (k ≥ 3).

This formula is verified for k ≤ 6. Moreover, the classical Erdős–Szekeres construction gives
the matching lower bound ES(k) ≥ 2k−2 + 1 [1]. The case k = 7 remains open: it is not
known whether every set of 33 points in general position contains a convex 7-gon, i.e., whether
ES(7) = 33.
Upper bounds for ES(k) have been refined substantially; for instance Suk proved ES(k) ≤
2k+o(k) [2], and Holmsen–Mojarrad–Pach–Tardos improved this to ES(k) ≤ 2k+O(√k log k) [3].
Computational approaches have also played an important role. Szekeres and Peters gave a
computer-assisted proof that ES(6) = 17 [4], and SAT-based approaches have been explored in
related settings (e.g. [5, 6]). Recent years have seen renewed SAT activity on Erdős–Szekeres-
type problems: Scheucher developed SAT models for higher-dimensional Erdős–Szekeres param-
eters and related questions, verifying UNSAT results via proof certificates [8], and Heule and
Scheucher established the exact empty hexagon number h(6) = 30 using a compact SAT en-
coding together with large-scale search and proof production [9]. While empty-hole problems
and higher-dimensional variants differ from the classical (non-empty) planar ES(7) case, these
works illustrate the current reach of SAT-based methods and motivate further exploration of
encodings tailored to the 33-point problem.
In this work we investigate the n = 33 case computationally by encoding geometric con-
sistency and the exclusion of convex 7-gons as a Boolean satisfiability problem. Our encoding
is built around orientation variables on triples and an exact reduction of convex position to
constraints on 4-point subsets. To reduce symmetry and support systematic experimentation,

∗Faculty of Computer Science, University of Bucharest, bogdan.dumitru@fmi.unibuc.ro

1arXiv:2512.24061v1  [math.CO]  30 Dec 2025
we additionally impose convex-layer (hull-template) anchoring constraints and, for some hard
templates, a simple sub-cubing parameter that further fixes the relative alignment of consecutive
layers. Using this framework we obtain UNSAT certificates for a growing collection of anchored
subfamilies, and we report a pronounced runtime imbalance across configurations, with some
subproblems taking weeks on commodity hardware.
The paper is organized as follows: Section 2 introduces the triple-orientation variables and a
family of 5-point CC-style implications (after Knuth). Section 3 states the 4-set criterion for con-
vex position and shows how it yields a compact “no convex 7-set” constraint. Section 4 describes
convex-layer anchoring templates and a simple sub-cubing parameter. Sections 5–6 summarize
instance sizes and representative computational results. Section 7 discusses bottlenecks and
outlines future work.

2 Preliminaries: triple orientations and CC-style constraints

2.1 Orientation variables

Let [n] = {0, 1, . . . , n − 1} be labels for points. In a realizable point set in general position,
every ordered triple (a, b, c) has a well-defined orientation (clockwise vs. counterclockwise). We
represent this with a sign predicate
 χ(a, b, c) ∈ {+, −},

alternating under swapping arguments.

Definition 1 (3-cup / 3-cap (convention)). Fix a convention: χ(a, b, c) = + corresponds to a
3-cup and χ(a, b, c) = − corresponds to a 3-cap (or vice versa). The convention is arbitrary
but must be used consistently.

We introduce one Boolean variable for each unordered triple {i, j, k} with i < j < k:

xijk ∈ {0, 1}.

For any ordered triple (a, b, c), let (i, j, k) be the sorted triple and define a signed literal

ℓ(a, b, c) ∈ {±xijk}

depending on whether (a, b, c) is an even or odd permutation of (i, j, k). This compactly enforces
antisymmetry at the literal level.

2.2 A 5-point implication (CC axiom 5)

To restrict assignments toward realizable order types, one can enforce axioms of oriented ma-
troids / chirotopes. We use a family of 5-point implications in the spirit of Knuth’s CC axioms [7].
In one common form, for distinct points p1, . . . , p5:

χ(p1, p2, p3) = χ(p1, p2, p4) = χ(p1, p2, p5) = χ(p1, p3, p4) = χ(p1, p4, p5) = + =⇒ χ(p1, p3, p5) = +.

Translated to CNF, this becomes a clause of the form

¬A1 ∨ ¬A2 ∨ ¬A3 ∨ ¬A4 ∨ ¬A5 ∨ C,

where each Ai and C are signed literals of triple-orientation variables.

Reduced generation. In the implementation documented here, we generate a reduced subset
of these 5-point clauses (motivated by symmetry and redundancy). This is a relaxation used for
performance.
 2

Interpretation of solver outcomes. Omitting clauses can only enlarge the set of admissible
Boolean assignments. Consequently, an UNSAT result for the relaxed instance remains a valid
certificate for any stronger formulation that includes the omitted clauses. Throughout this paper
we report only UNSAT outcomes.

3 A 4-set criterion for convex position

A direct encoding of “no convex 7-gon” tends to quantify over all 7-subsets and many cyclic
orderings, creating a large clause blowup at (n, k) = (33, 7). We instead use an exact reduction
to 4-point subsets.

Proposition 1 (4-set criterion for convex position). Let S be a finite set of points in the plane
in general position. Then S is in convex position if and only if every 4-point subset of S is in
convex position.

Proof sketch. If S is in convex position, then every subset of S is also in convex position, so
every 4-point subset is convex.
Conversely, assume S is not in convex position. Then some point p ∈ S is not a vertex of
the convex hull of S, hence p lies strictly inside the convex polygon P = conv(V ), where V ⊆ S
is the set of hull vertices. Triangulate P by fixing a hull vertex v0 ∈ V and drawing diagonals
from v0 to all non-adjacent hull vertices; this partitions P into triangles whose vertices lie in V .
Since p lies inside P , it lies inside one of these triangles, say △abc with a, b, c ∈ V ⊆ S. Then
the 4-set {a, b, c, p} is not in convex position (one point lies inside the triangle formed by the
other three), contradicting the assumption that every 4-point subset of S is convex.

4 Encoding 4-point types and excluding convex 7-sets

4.1 Four cyclic triple orientations

Fix a 4-set {a, b, c, d} together with an ordering (a, b, c, d). Consider the cyclic triples

(a, b, c), (b, c, d), (c, d, a), (d, a, b).

Each triple has an orientation literal, hence the 4-set induces a length-4 sign pattern in {+, −}4.
Not all 24 = 16 patterns occur for 4 points in general position; exactly 14 do. In our current
implementation, we introduce 14 selector variables per 4-set, one per realizable pattern, and
constrain them to be mutually covering.

4.2 Selector variables and CNF

Formally, for each 4-set Q and each realizable pattern index p ∈ {1, . . . , 14} we introduce a
variable tQ,p; we suppress the Q subscript when discussing a fixed 4-set.
For each 4-set we introduce 14 selector variables t1, . . . , t14. Each selector is constrained to
be equivalent to a conjunction of four literals (the cyclic triple orientations), using the standard
reification template t ↔ (L1 ∧ L2 ∧ L3 ∧ L4),

encoded as 5 clauses. We also enforce that at least one selector holds. Thus each 4-set contributes
14 × 5 + 1 = 71 clauses.

Remark 1 (Convex vs. non-convex patterns). In the generator version used here, 6 realizable
patterns are treated as convex:

+ + ++, − − −−, + + −−, − − ++, − + +−, + − −+,

and the remaining 8 realizable patterns are treated as non-convex.

3

4.3 No convex 7-set clauses

For each 7-set K, Proposition 1 implies that K is in convex position if and only if all its 4-subsets
are convex. Therefore, to exclude convex 7-sets it suffices to enforce that every 7-set contains
at least one non-convex 4-subset. In our encoding, for each 7-set K we add one clause
⋁

Q∈(K
4 )
 ⋁

p∈N tQ,p,

where N indexes the non-convex patterns for a 4-set Q. This clause has length 35 × 8 = 280.

5 Convex layers (hull templates) and a simple sub-cubing pa-
rameter

To reduce symmetry and to explore structured subfamilies, we add convex layer constraints
(also called convex-layer decompositions) that enforce a nested sequence of convex layers with
prescribed sizes.

5.1 Convex-layer (hull template) anchoring

Fix n and a vector of layer sizes

h = (h0, h1, . . . , hr−1), hi ≥ 3, H :=
 r−1∑

i=0 hi ≤ n.

We interpret points 0, . . . , h0 − 1 as the vertices of an outer convex h0-gon in cyclic order,
points h0, . . . , h0 + h1 − 1 as the next layer, and so on. Remaining n − H points are treated as
unconstrained interior points.
We then add unit clauses enforcing:

• Within-layer convexity: every triple of vertices within a layer (in the chosen cyclic
order) has fixed orientation.

• Nesting: each deeper-layer point lies on the interior side of each oriented edge of an outer
layer (encoded by fixed orientations of suitable triples).

5.2 A simple sub-cubing parameter (anchoring consecutive layers)

For some hard convex-layer templates we further add a small family of unit clauses controlled
by a vector w = (w0, w1, . . . , wr−1),

where each wi is interpreted as an offset within layer i (with w0 = 0 by convention). This
parameter is used as a manual sub-cubing mechanism: different choices of w produce independent
subinstances.

Geometric meaning. Let Li denote layer i and let si = ∑
j<i hj be its starting index, so
Li = {si, . . . , si + hi − 1}. For each i ≥ 1 we fix an anchor vertex a = si−1 in the previous layer
Li−1, and we select two vertices of the current layer:

b = si, c = si + wi.

We then add unit constraints on orientation literals that force all points of index > si (i.e.,
all remaining vertices of Li and all deeper layers / leftover points) to lie inside the wedge at a

4

bounded by the rays ab and ac. Equivalently, from the viewpoint of a, the pair (b, c) is forced
to behave like two extremal (supporting) vertices of the inner layer, fixing part of the relative
“rotation” between Li−1 and Li. When wi = 0 (so c = b), this extra anchoring at layer i is
omitted.

Role in computation. The w constraints are not intended as a balanced or exhaustive split-
ting strategy; rather, they provide a small, geometry-informed way to partition some highly
symmetric templates into subinstances that can behave very differently in runtime.

6 Instance size for (n, k) = (33, 7)

6.1 Variable counts

Triple variables. There are (33
3 ) = 5456 unordered triples, hence 5456 base orientation vari-
ables.

4-set selectors. There are (33
4 ) = 40920 4-sets and 14 selectors per 4-set, contributing 40920×
14 = 572,880 variables.

Total. Thus the base instance has

5456 + 572,880 = 578,336

Boolean variables.

6.2 Clause counts

The dominant clause blocks are:

• Reduced 5-point constraints: for n = 33 this block contributes 9,493,440 clauses in
the recorded generator version.

• 4-set consistency: 71
(33
4 ) = 2,905,320 clauses.

• No convex 7-set constraints (via 4-sets): (33
7 ) = 4,272,048 clauses, each of length
280.

Therefore the base CNF (before hull constraints) has

9,493,440 + 2,905,320 + 4,272,048 = 16,670,808

clauses. Hull constraints add only unit clauses (hundreds to a few thousands), so they do not
change CNF size materially, though they can strongly affect runtime.

7 Results and observations

This section summarizes a set of observed UNSAT runtimes for (n, k) = (33, 7) under convex-
layer templates and (optionally) the w sub-cubing parameter. Times are single-thread wall-clock
runtimes and should be interpreted qualitatively.
All CNF instances were generated using Python scripts (PySAT [10]) and solved using
Kissat [11] (single-thread runs).

Remark 2 (Runtime variability). Even within closely related convex-layer families, runtimes
vary widely. For example, within the 56 template we observe sub-cubes ranging from 2.50 × 103 s
to 2.28×106 s, and within 4-dominated templates from 8.76×104 s to 2.10×106 s. This motivates
both encoding refinements (to reduce clause/literal volume and strengthen propagation) and
stronger geometric anchoring for the hardest symmetric configurations.

5

Layer sizes h (sum H) sub-cube parameter w observed time (s)

6, 6, 6, 3, 6, 6 (H = 33) (not recorded) ≈ 1.73 × 105

311 (H = 33) (not recorded) ≈ 6.05 × 105

3, 3, 4, 3, 3, 6, 6, 5 (H = 33) [0, 1, 1, 1, 1, 1, 4, 4] 2.26 × 105

56 (H = 30) (baseline run) 2.59 × 105

56 (H = 30) [0, 4, 4, 4, 4, 4] 2.50 × 103

56 (H = 30) [0, 1, 1, 1, 1, 1] 1.60 × 104

56 (H = 30) [0, 1, 1, 1, 0, 0] 2.28 × 106

48 (H = 32) [0, 3, 3, 3, 3, 3, 3, 3] 8.76 × 104

48 (H = 32) [0, 1, 2, 3, 1, 2, 3, 1] 3.19 × 105

4, 3, 4, 4, 4, 4, 4, 4 (H = 31) [0, 1, 3, 2, 1, 2, 1, 1] 2.10 × 106

4, 3, 3, 5, 4, 6, 3, 4 (H = 32) [0, 2, 2, 4, 1, 1, 1, 1] 3.15 × 103

3, 5, 3, 5, 3, 3, 5, 5 (H = 32) [0, 1, 2, 1, 2, 1, 1, 4] 3.59 × 104

3, 4, 3, 4, 4, 3, 4, 4, 3 (H = 32) [0, 1, 2, 1, 2, 1, 1, 3, 2] 9.06 × 105

Table 1: Selected UNSAT runtimes for (n, k) = (33, 7) under convex-layer templates and the w
parameter (single-thread wall-clock seconds).

Reproducibility. The SAT instance generator and scripts used to produce the results reported
in this paper are publicly available.1 The repository contains the implementation correspond-
ing to the encoding described here, together with configurations for the reported convex-layer
templates.

8 Discussion and future work

The encoding presented here makes it feasible to generate and solve large SAT instances arising
from the (33, 7) case, at least for many structured subfamilies obtained by convex-layer an-
choring. The main practical challenge is that solver time varies widely across nearby anchored
families.

Future work

We list two encoding directions that appear promising and will be tested experimentally in a
future revision.

1. Reduce the granularity of the 4-set encoding. The current implementation distin-
guishes all realizable 4-point types using multiple selector variables per 4-set. However,
the 7-set exclusion constraints ultimately depend only on the coarse distinction “convex
vs. non-convex” for each 4-set. It may therefore be possible to replace the detailed 4-type
bookkeeping by a coarser representation that captures only what is needed for the 7-set
constraints, reducing auxiliary variables and 4-set clauses.

2. Shorten the 7-set constraints using the coarser 4-set information. At present,
each 7-set clause is a long disjunction expanded over many pattern-specific literals. If a
coarser convex/non-convex indicator is available per 4-set, the corresponding 7-set con-
straints can be expressed with substantially shorter clauses. Besides reducing memory
pressure, shorter clauses typically strengthen propagation because a 7-set becomes con-
strained once many of its 4-subsets are forced convex.

1https://github.com/bogdan27182/esc-paper
 6

A second (orthogonal) direction is stronger geometric anchoring on the outer convex layer to
reduce symmetry while preserving completeness of the intended case split; this will be explored
experimentally.

9 Conclusion

We presented a SAT encoding for the planar Erdős–Szekeres problem at (n, k) = (33, 7) using
triple-orientation variables, a reduced CC-style 5-point constraint family, and an exact 4-set
criterion (Proposition 1) to exclude convex 7-sets. The encoding supports additional convex-
layer anchoring constraints and yields UNSAT certificates for several anchored families. Further
progress appears to depend on both encoding refinements and stronger geometric anchoring for
the hardest symmetric configurations.

References

[1] P. Erdős and G. Szekeres. A combinatorial problem in geometry. Compositio Mathematica,
2:463–470, 1935.

[2] A. Suk. On the Erdős–Szekeres convex polygon problem. J. Amer. Math. Soc., 30(4):1047–
1053, 2017. (Preprint: arXiv:1604.08657.)

[3] A. Holmsen, H. N. Mojarrad, J. Pach, and G. Tardos. Two extensions of the Erdős–Szekeres
problem. J. Eur. Math. Soc., 22(12):3997–4010, 2020.

[4] G. Szekeres and L. Peters. Computer solution to the 17-point Erdős–Szekeres problem. The
ANZIAM Journal, 48(2):151–164, 2006.

[5] M. Balko and P. Valtr. A SAT attack on the Erdős–Szekeres conjecture. In Proc. 33rd
International Symposium on Computational Geometry (SoCG 2017). Schloss Dagstuhl–
Leibniz-Zentrum für Informatik, 2017.

[6] F. Marić. A fast formal proof of the Erdős–Szekeres theorem for polygons with at most 6
vertices. Journal of Automated Reasoning, 58(4):539–550, 2017.

[7] D. E. Knuth. Axioms and Hulls. Springer, 1992.

[8] M. Scheucher. A SAT Attack on Erdős–Szekeres Numbers in Rd and the Empty
Hexagon Theorem. Computing in Geometry and Topology, 2(1), 2:1–2:13, 2023.
doi:10.57717/cgt.v2i1.12.

[9] M. J. H. Heule and M. Scheucher. Happy Ending: An Empty Hexagon in Every Set of 30
Points. arXiv preprint arXiv:2403.00737, 2024.

[10] A. Ignatiev, A. Morgado, and J. Marques-Silva. PySAT: A Python toolkit for prototyping
with SAT oracles. In Proc. SAT 2018, LNCS 10929, pages 428–437. Springer, 2018.

[11] A. Biere, M. Fleury, L. Heisinger, and C. Sinz. CaDiCaL, Kissat, Paracooba, Plingeling
and Treengeling entering the SAT Competition 2020. Proceedings of SAT Competition 2020,
2020.
 7
