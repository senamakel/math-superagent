<!-- source: https://drops.dagstuhl.de/storage/00lipics/lipics-vol332-socg2025/LIPIcs.SoCG.2025.13/LIPIcs.SoCG.2025.13.pdf | converted from PDF -->

The Erdős–Szekeres Conjecture Revisited

Jineon Baek
Department of Mathematics, University of Michigan, Ann Arbor, MI, USA

Martin Balko
Department of Applied Mathematics, Faculty of Mathematics and Physics,
Charles University, Prague, Czech Republic

Abstract

The famous and still open Erdős–Szekeres Conjecture from 1935 states that every set of at least
2
k−2 + 1 points in the plane with no three being collinear contains k points in convex position, that
is, k points that are vertices of a convex polygon. In this paper, we revisit this conjecture and show
several new related results.
First, we prove a relaxed version of the Erdős–Szekeres Conjecture by showing that every set of
at least 2
k−2 + 1 points in the plane with no three being collinear contains a split k-gon, a relaxation
of k-tuple of points in convex position. Moreover, we show that this is tight, showing that the value
2k−2 + 1 from the Erdős–Szekeres Conjecture is exactly the right threshold for split k-gons.
We obtain an analogous relaxation in a much more general setting of ordered 3-uniform hy-
pergraphs where we also show that, perhaps surprisingly, a corresponding generalization of the
Erdős–Szekeres Conjecture is not true. Finally, we prove the Erdős–Szekeres Conjecture for so-called
decomposable sets and provide new constructions of sets of 2k−2 points without k points in convex
position, generalizing all previously known constructions of such point sets and allowing us to
computationally tackle the Erdős–Szekeres Conjecture for large values of k.

2012 ACM Subject Classification Theory of computation → Randomness, geometry and discrete
structures; Theory of computation → Computational geometry; Mathematics of computing →
Combinatorics

Keywords and phrases convex position, Erdős–Szekeres theorem, point set

Digital Object Identifier 10.4230/LIPIcs.SoCG.2025.13

Funding Jineon Baek: acknowledges support from the Korea Foundation for Advanced Studies
during the completion of this research.
Martin Balko: supported by grant no. 23-04949X of the Czech Science Foundation (GAČR) and by
the Center for Foundations of Modern Computer Science (Charles Univ. project UNCE 24/SCI/008).

1 Introduction

A finite set of points on a plane is in general position if there are no three points on a single
line and in convex position if they form the vertices of a convex polygon. We consider finite
point sets in general position where no two points have the same x- or y-coordinate.
Motivated by a problem posed by Esther Klein, Erdős and Szekeres [7] showed that for
any positive integer k there is a minimum integer ES(k) such that any set of ES(k) points in
the plane in general position contains k points in convex position. This famous result, called
the Erdős–Szekeres Theorem, was a starting point of both discrete geometry and Ramsey
theory and was obtained as one of the first applications of Ramsey’s Theorem, which was
independently discovered by Erdős and Szekeres [7] in the same paper. Ramsey’s Theorem,
however, yields a poor bound on the minimum size ES(k) of a planar point set in general
position that guarantees the existence of k points in convex position. Thus, Erdős and
Szekeres [7] also provided an alternative proof that yields a much better estimate on ES(k).
This alternative argument uses more geometry and is based on so-called caps and cups.

© Jineon Baek and Martin Balko;
licensed under Creative Commons License CC-BY 4.0
41st International Symposium on Computational Geometry (SoCG 2025).
Editors: Oswin Aichholzer and Haitao Wang; Article No. 13; pp. 13:1–13:15
Leibniz International Proceedings in Informatics
Schloss Dagstuhl – Leibniz-Zentrum für Informatik, Dagstuhl Publishing, Germany

13:2 The Erdős–Szekeres Conjecture Revisited

For a positive integer a, we say that a points in the plane form an a-cap if they lie on a
graph of a concave function. Similarly, for u ∈ N, a set of u points in the plane forms a u-cup
if its points lie on a graph of a convex function. Using this notion, Erdős and Szekeres [7]
proved the following result known as the Erdős–Szekeres Cap-Cup Theorem.

▶ Theorem 1 (The Erdős–Szekeres Cap-Cup Theorem [7]). For all integers a, u ≥ 2, every set
of at least (a+u−4
a−2 ) + 1 points in the plane in general position contains an a-cap or a u-cup.
Moreover, this is tight. That is, for all integers a, u ≥ 2, there are sets of (a+u−4
a−2 ) points
in the plane in general position with neither an a-cap nor a u-cup.

Since points of an a-cap and a u-cup are in convex position, Theorem 1 gives

ES(k) ≤ (2k − 4
k − 2
 ) + 1 (1)

for any integer k ≥ 2. In fact, observe that every set of k points in convex position is a union
of an a-cap and a u-cup that share common endpoints and satisfy a + u = k + 2.
The bound (1) gives roughly ES(k) ≤ 4k. Erdős–Szekeres believed that this could be
significantly improved and posed the following conjecture.

▶ Conjecture 2 (The Erdős–Szekeres Conjecture [7]). For every integer k ≥ 2, we have

ES(k) = 2
k−2 + 1.

When posed in 1935, the conjecture was known to be true only for k ≤ 4. Later, it was
proved for k = 5, and Peters and Szekeres [19] proved it also for k = 6 in 2006 using a
computer-assisted approach. In the 1960s, Erdős and Szekeres [8] showed ES(k) ≥ 2
k−2 + 1
for any integer k ≥ 2, further supporting the conjecture. Despite many efforts, this conjecture
is still open for k ≥ 7, and Erdős himself offered $500 reward for its solution. For many
decades, the bound (1) was the best known, but then several smaller-order improvements
appeared [5, 14, 16, 18, 21, 22]. In 2017, Suk [20] made a breakthrough on this conjecture
by proving ES(k) ∈ 2k+O(k2/3 log k) and his bound was then slightly improved by Holmsen,

Mojarrad, Pach, and Tardos [13] to ES(k) ∈ 2
k+O(
√k log k). Although these bounds are fairly
close to 2k−2 + 1, there is still a gap between the known lower and upper bounds, and this
famous conjecture thus remains open.

2 Our results

In this paper, we introduce a natural relaxed variant of the Erdős–Szekeres Conjecture for
which the number 2
k−2 + 1 is exactly the right threshold. To our knowledge, this is the first
version of this famous conjecture where the conjectured value 2
k−2 + 1 appears as the right
threshold. We discuss abstract combinatorial extensions of this result and connections to the
original Erdős–Szekeres Conjecture, some of which indicate that this conjecture might be
false. We also prove the Erdős–Szekeres Conjecture restricted to special point sets, and we
provide new examples of 2
k−2 point sets with no k points in convex position.

2.1 Split polygons

For a positive integer N , let P be a set of N points in the plane in general position. For a
positive integer k, a split k-gon in P is a set of points from P that is formed by an a-cap and
a u-cup that share the rightmost point and that satisfy a + u = k + 2; see Figure 1. Note
that a split k-gon can contain k or k + 1 points and that if the a-cap and the u-cup share
also the leftmost point, then the points of the split k-gon are in convex position.

J. Baek and M. Balko 13:3

(a)(b)(c)(d)
 Figure 1 (a–d) Examples of split 7-gons. Note that the split 7-gons in (a) and (d) have only 7
points while the remaining split 5-gons contain 8 points.

We consider a variant of the Erdős–Szekeres Theorem for split polygons. More specifically,
for a positive integer k, let ESsplit(k) be the minimum positive integer N such that every
finite set of at least N points in the plane in general position contains a split k-gon. Since
ESsplit(k) ≤ ES(k), we have ESsplit(k) ≤ 2
(1+o(1))k by the result of Suk [20].
As our first main result, we prove that the numbers ESsplit(k) attain exactly the value
2
k−2 + 1 from the Erdős–Szekeres Conjecture.

▶ Theorem 3. For every integer k ≥ 2, we have ESsplit(k) = 2
k−2 + 1.

In fact, we can prove a stronger statement in the setting corresponding to a refinement
of the Erdős–Szekeres Conjecture as introduced by Erdős, Tuza, and Valtr [9]. In their
refinement, one tries to find k-tuples of points in convex position in point sets that do not
contain a-caps and u-cups of prescribed sizes a and u.
We state this formally in our setting. For integers a, u, k ≥ 2, let ESsplit(a, u, k) be the
minimum positive integer N such that every finite set of at least N points in the plane in
general position contains an a-cap, a u-cup, or a split k-gon. We are mostly interested in
the cases max{a, u} ≤ k ≤ a + u − 2 as otherwise at least one parameter from a, u, k is
unnecessary. Therefore, we define

T = {(a, u, k) : a, u ≥ 2 and max{a, u} ≤ k ≤ a + u − 2}.

For any triple (a, u, k) ∈ T , we can then determine the numbers ESsplit(a, u, k) exactly.

▶ Theorem 4. For every (a, u, k) ∈ T , we have

ESsplit(a, u, k) = 1 +
 u∑

i=k−a+2
 (k − 2
i − 2
 ).

Note that ESsplit(k) = ESsplit(k, k, k). Thus, Theorem 3 follows from Theorem 4 by
setting a = u = k as then

ESsplit(k) = 1 +
 k∑

i=2
 (k − 2
i − 2
 ) = 2
k−2 + 1.

Also, observe that Theorem 1 is a special case of Theorem 4 for k = a + u − 2.
We also remark that if ES(a, u, k) is the minimum positive integer N such that every
finite set of at least N points in the plane in general position contains an a-cap, a u-cup, or
k points in convex position, then it is conjectured that

ES(a, u, k) = 1 +
 u∑

i=k−a+2
 (k − 2
i − 2
 ) (2)

for all (a, u, k) ∈ T . However, this equality is known to be true only in the trivial case
k ≥ a + u − 3 and Baek [1] proved it when a or u equals 4. Surprisingly, Erdős, Tuza, and
Valtr [9] showed that the Erdős–Szekeres conjecture is equivalent to (2).
 S o C G 2 0 2 5

13:4 The Erdős–Szekeres Conjecture Revisited

2.2 Abstract split polygons

The proof of the upper bound in Theorem 4 is based on techniques used by Moshkovitz and
Shapira [17] when estimating ordered Ramsey numbers of so-called monotone paths. It turns
out that the proof can be generalized to this abstract combinatorial setting. To state this
extension, we need to introduce some definitions.
For a positive integer N , let K3
N be the ordered complete 3-uniform hypergraph with the
vertex set [N ] = {1, . . . , N } ordered by the standard ordering < of the positive integers. A
2-coloring of K3
N is a function χ that assigns either a red or blue color to each hyperedge of
K3
N . A monotone path P 3
n is an ordered 3-uniform hypergraph on n ≥ 2 vertices where the
hyperedges are formed by triples of vertices that are consecutive in the vertex ordering of P 3
n.
Let P = {p1, . . . , pN } be a set of points in the plane in general position with x(p1) <
· · · < x(pN ) where x(pi) is the x-coordinate of a point pi. The 2-coloring induced by P is a
2-coloring χP of K3
N that colors a hyperedge {i, j, k} with i < j < k red if the points pi, pj, pk
form a 3-cap and blue if pi, pj, pk form a 3-cup. Observe that, for each n, red monotone
paths on n vertices in χP correspond to n-caps in P and that blue monotone paths on n
vertices in χP correspond to n-cups in P .
In 2014, Moshkovitz and Shapira [17] proved the following result, whose first part vastly
generalizes the first part of the Erdős–Szekeres Cap-Cup Theorem (Theorem 1) as it deals
with all 2-colorings of K3
N and not only with those induced by a point set of size N .

▶ Theorem 5 ([7, 11, 17]). For all integers a, u ≥ 2 and N ≥ (a+u−4
a−2 ) + 1, every 2-coloring
of K3
N contains either a red copy of P 3
a or a blue copy of P 3
u.
Moreover, this is tight. That is, there are 2-colorings of K3
N with N = (a+u−4
a−2 ) that do
not contains red copy of P 3
a nor a blue copy of P 3
u.

In other words, Theorem 5 states that the ordered Ramsey number [3, 6] of P 3
a and P 3
u
equals (a+u−4
a−2 ) + 1. We extend this result similarly as Theorem 4 extends Theorem 1.
We start by generalizing split polygons. Let χ be a 2-coloring of K3
N with colors red and
blue. For k ∈ N, an abstract split k-gon in χ is an ordered subhypergraph of K3
N that is
formed by a red monotone path P 3
a and a blue monotone path P 3
u that share the rightmost
vertex and that satisfy a + u = k + 2. Observe that an abstract split k-gon can have at most
k + 1 vertices. Also, note that, for every abstract split k-gon C in a coloring χP induced by a
point set P , the two monochromatic monotone paths in C can share only their endpoint pair
and that abstract split k-gons in χP are in one-to-one correspondence with split k-gons in P .
Generalizing the definition of ESsplit(a, u, k), we let Csplit(a, u, k) be the minimum
positive integer N such that every 2-coloring of K3
N with colors red and blue contains a red
copy of P 3
a, a blue copy of P 3
u, or an abstract split k-gon. Observe that considering the
2-colorings induced by P gives, for every (a, u, k) ∈ T ,

ESsplit(a, u, k) ≤ Csplit(a, u, k). (3)

As our next result, we fully determine the numbers Csplit(a, u, k) by showing that
ESsplit(a, u, k) = Csplit(a, u, k) for every (a, u, k) ∈ T .

▶ Theorem 6. For every (a, u, k) ∈ T , we have

Csplit(a, u, k) = 1 +
 u∑

i=k−a+2
 (k − 2
i − 2
 ).

Similarly as before, note that Theorem 5 is a special case of Theorem 6 for k = a + u − 2.

J. Baek and M. Balko 13:5

2.3 Finding polygons that are not split

The only difference between the setting in the Erdős–Szekeres Conjecture and the setting
in Theorem 3 is that in the latter one, we allow the leftmost endpoints of the a-cap and
the u-cup to be different. Enforcing these two endpoints to meet without increasing the
size of the considered point sets would resolve the Erdős–Szekeres Conjecture. However, the
combinatorial structure used to prove Theorem 3 does not seem strong enough to ensure
this. Moreover, we will show that this strengthening is not true in the abstract combinatorial
setting from Subsection 2.2.
First, we generalize the concept of convex position. For a positive integer N , let χ be a
2-coloring of K3
N . For a positive integer k, a weak k-gon in χ is an ordered subhypergraph
of K3
N that is formed by a red monotone path P 3
a and a blue monotone path P 3
u that share
both their end-vertices and satisfy a + u = k + 2. That is, a weak k-gon is a particular case
of an abstract split k-gon. Note that the red and the blue monotone path can share other
vertices, not only their two end-vertices. If we exclude this possibility and allow the two
paths to share only their end-vertices, then we call such ordered subhypergraph a strong
k-gon in χ. If χP is a 2-coloring induced by a point set P , then every weak k-gon is a strong
k-gon in χP and corresponds to a set of k points from P that are in convex position.
Let Cweak(k) be the minimum N ∈ N such that every 2-coloring of K3
N contains a weak
k-gon. An analogous number for strong k-gons is denoted by Cstrong(k). Clearly,

Cstrong(k) ≥ Cweak(k) ≥ Csplit(k, k, k) = 2
k−2 + 1,

where the equality follows from Theorem 6. Moreover, if Cweak(k) ≤ 2k−2 + 1, then the
Erdős–Szekeres Conjecture is true.
We do not have Cstrong(k) ≤ 2k−2 + 1 as Balko and Valtr [4] proved Cstrong(7) > 33
with SAT solvers, disproving a conjecture of Peters and Szekeres [19]. Our SAT-solver-based
proofs show that this is also the case for weak k-gons.

▶ Theorem 7. We have Cweak(7) > 33.

Thus, there is no hope for extending the Erdős–Szekeres Conjecture to the abstract setting
with weak k-gons. This also suggests that the Erdős–Szekeres Conjecture might be false and
that one might look for counterexamples. A natural candidate for a counterexample is a
subset of the point sets that were used by Erdős–Szekeres to prove the tightness in Theorem 1
for a-caps and u-cups since such a set used by Erdős–Szekeres [7] contains a subset of 2
k−2

points with no k points in convex position.
However, we prove that it is impossible to find a counterexample to Erdős–Szekeres
Conjecture by restricting ourselves to these sets. In fact, we show this for a larger class
of so-called decomposable sets (see Section 4 for their definition). These sets include, for
example, the point sets with no long caps nor cups used by Erdős–Szekeres [7] as well as the
Horton sets defined by Valtr [23].

▶ Theorem 8. Let a, u, k be positive integers satisfying a, u ≤ k. Then, every decomposable
set of more than ∑u
i=k−a+2 (k−2
i−2) points contains an a-cap, a u-cup, or k points in convex
position.

In particular, since every non-empty subset of a decomposable set is decomposable,
we obtain, by choosing a = u = k, that every subset of more than 2k−2 points from a
decomposable set contains k points in convex position. Therefore, if we restrict ourselves
to decomposable sets, the Erdős–Szekeres Conjecture is true. The proof of Theorem 8 is
omitted.
 S o C G 2 0 2 5

13:6 The Erdős–Szekeres Conjecture Revisited

Finally, when exploring the validity of the Erdős–Szekeres Conjecture, we discovered new
constructions of sets of 2k−2 points in general position with no k points in convex position.
As our last main result, we introduce a “blow-up” method that generalizes all previously
known constructions of such point sets; see Section 4 for their brief description. Our new
method is captured by Lemma 14 in Section 6. We show that all previously known examples
follow rather easily from this lemma and that it also gives new examples of such point sets.

We also tried to computationally tackle the Erdős–Szekeres conjecture for large k using
a non-linear optimization solver based on a genetic algorithm and this new construction.
However, despite finding numerous new examples of 2
k−2 points without k points in convex
position even for k = 20, our experiments never produced such points sets with more than
2k−2 points; see Section 6 for more details.

3 Open problems

We showed that the variant of the Erdős–Szekeres Conjecture is true for split k-gons, even in
an abstract combinatorial setting, while the original Erdős–Szekeres Conjecture does not
admit such an abstract strengthening; these results are summarized in Table 1. Each cell
corresponds to a variant statement of the Erdős–Szekeres Conjecture.

Table 1 Variants of the Erdős–Szekeres Conjecture and their status.

Point sets Ordered hypergraphs
Split k-gons True (Theorem 6) True (Theorem 3)
Weak k-gons Open (Erdős–Szekeres [7]) False (Theorem 7)

It also follows from Theorem 7 that any proof of the Erdős–Szekeres Conjecture has to use
some assumptions on the 2-colorings. Natural candidates for such 2-colorings are so-called sig-
notopes that appear under many different names in the literature (see [2, 10], for example). For
N ∈ N, a 2-coloring χ of K3
N is a signotope if for every 4-tuple a < b < c < d of vertices of K3
N
there is at most one change of color in the sequence (χ(a, b, c), χ(a, b, d), χ(a, c, d), χ(b, c, d)).

Signotopes on K3
N are in one-to-one correspondence with pseudoline arrangements de-
termined by N points [10] and thus offer a natural and frequently used combinatorial
generalization of point sets. Moreover, if we have χ(a, b, c) = χ(b, c, d) for some vertices
a < b < c < d in a signotope χ, then χ(a, b, c) = χ(a, b, d) = χ(a, c, d) = χ(b, c, d). It follows
that any weak k-gon in χ is also a strong k-gon in χ.

In our computer experiments, we were not able to find a signotope on at least 1 +
∑u
i=k−a+2 (k−2
i−2) vertices that would contain neither a red copy of P 3
a, nor a blue copy of P 3
u,
nor a weak k-gon. Thus, it is still possible that the Erdős–Szekeres Conjecture is true even if
we do not restrict ourselves to 2-colorings induced by point sets but we consider all signotopes.
Such a generalization is equivalent to a conjecture of Goodman and Pollack [12].

Another natural open problem is to obtain better bounds on Cweak(k) and Cstrong(k).
We know that both numbers can be larger than 2k−2 + 1, but the strongest upper bound
that we are aware of follows from Theorem 5 for a = u = k and gives

Cweak(k) ≤ Cstrong(k) ≤ (
2k − 4
k − 2
 ) + 1.

J. Baek and M. Balko 13:7

4 Preliminaries and notation

In this section, we introduce some useful notation and definitions and briefly describe all
known constructions of sets of 2
k−2 that avoid subsets of k points in convex position. Some
of these constructions are used later in our proofs.
For a point p in the plane, we use x(p) and y(p) to denote the x- and y-coordinate of
p, respectively. Let A and B be two sets of points in the plane in general position. We
write x(A) < x(B) (or y(A) < y(B)) if A is to the left (or below, respectively) of B, that is,
x(a) < x(b) (y(a) < y(b), respectively) for every a ∈ A and b ∈ B. We say that A is deep
below B if y(A) < y(B) and all points from B lie above every line determined by two points
from A and all points from A lie below every line determined by two points from B.
For integers a, u ≥ 2, we now describe the sets of (a+u−4
a−2 ) points without a-caps and
u-cups that were used by Erdős and Szekeres [7] to prove the tight lower bound in Theorem 1.
We denote these sets by P (a, u) and we construct them by induction on a + u. If a = 2 or
u = 2, then we let P (a, u) be a set of one point. For a, u ≥ 3, we let P (a, u) be the point
set that is obtained by adding a translated copy of P (a, u − 1) to P (a − 1, u) that is to the
left of P (a − 1, u) and deep below P (a − 1, u). It is then easy to show that P (a, u) does not
contain a-cap nor a u-cup [7, 15].
A set P is decomposable if either |P | = 1 or if |P | ≥ 2 and P can be partitioned into two
decomposable sets A and B such that A is deep below B. Note that the sets P (a, u) are
decomposable and that every non-empty subset of a decomposable set is decomposable.
Let a, u, and k be integers satisfying (a, u, k) ∈ T . We use S(a, u, k) to denote the sum
∑u
i=k−a+2 (k−2
i−2). For a, u, k ∈ N with a, u ≤ k, we also define S(a, u, k) = 0 if a = 1 or u = 1.
These cases agree with the formula ∑u
i=k−a+2 (k−2
i−2) as the sum is then empty.
We now describe all known constructions of S(a, u, k) points in general position without
a-caps, u-cups, or k points in general position. Let Q be an arbitrary set of a + u − k − 1
points qk−a+2, . . . , qu in the plane in general position sorted by increasing y-coordinate. Let
P be the point set obtained by replacing each qi with a set Qi of (k−2
i−1) points without
(k − i + 2)-cap and i-cup in a sufficiently small neighborhood of qi such that Qi is deep
below Qi+1 for every i ∈ {k − a + 2, . . . , u − 1}. Then, it can be shown that P does not
contain a-cap, u-cup, nor k points in convex position [8, 9]. We call the resulting point
set Valtr’s construction as it was described to us by Valtr [24]. To our knowledge, it is not
described in the literature. If, in addition, Q is a (a + u − k − 1)-cup and each Qj is the set
P (k + 1 − j, j + 1), then we call the set P the Erdős–Szekeres construction and we denote it
by P (a, u, k). For a = u = k, this is the point set constructed by Erdős and Szekeres [8] to
prove ES(k) ≥ 2
k−2 + 1.

5 Proofs of Theorems 4 and 6

Here, we prove Theorems 4 and 6 by determining the values ESsplit(a, u, k) and Csplit(a, u, k)
for every (a, u, k) ∈ T . It follows from (3) that in order to prove both these results, it suffices
to prove the upper bound Csplit(a, u, k) ≤ 1 + ∑u
i=k−a+2 (k−2
i−2) from Theorem 6 and the
lower bound ESsplit(a, u, k) ≥ 1 + ∑u
i=k−a+2 (k−2
i−2) from Theorem 4.

5.1 Upper bound from Theorem 6

Let m and n be positive integers. We use ⪯ to denote the partial ordering on [m]×[n] satisfying
(x1, y1) ⪯ (x2, y2) if and only if x1 ≤ x2 and y1 ≤ y2 for all (x1, y1), (x2, y2) ∈ [m] × [n]. A
subset D of [m] × [n] is a down-set if y ∈ D implies x ∈ D for every x ⪯ y; see Figure 2.
 S o C G 2 0 2 5

13:8 The Erdős–Szekeres Conjecture Revisited

There is a one-to-one correspondence between down-sets in [m] × [n] and m × n line par-
titions with entries from {0, 1, . . . , n} which are sequences (a1, . . . , am) of numbers satisfying
n ≥ a1 ≥ a2 ≥ · · · ≥ am ≥ 0; see [17]. It is well-known and easy to see that the number of
such line partitions (and thus also the number of down-sets in [m] × [n]) is (m+n
m ).

Figure 2 An example of a down-set in [10] × [10] with the bounding box 9 × 8.

Given a non-empty down-set D in [m] × [n], we say that D has the bounding box r × s if
r is the maximum integer such that ar > 0 and a1 = s. We say that the empty down-set has
the bounding box 0 × 0.

▶ Lemma 9. For (a, u, k) ∈ T , the number of down-sets in [a − 2] × [u − 2] with the bounding
box r × s where r + s ≤ k − 1 is

u∑

i=k−a+2
 (
k − 2
i − 2
 ).

The proof of Lemma 9 is omitted. We now prove the upper bound on Csplit(a, u, k).

▶ Lemma 10. For every (a, u, k) ∈ T , we have

Csplit(a, u, k) ≤ 1 +
 u∑

i=k−a+2
 (k − 2
i − 2
 )
.

Proof. For a positive integer N , let χ be a 2-coloring of K3
N with colors red and blue such
that there is neither a red copy of P 3
a, a blue copy of P 3
u, nor an abstract split k-gon. We
show that N ≤ ∑u
i=k−a+2 (k−2
i−2).
For vertices u and v of K3
N with u < v, we let D(u, v) = (nr − 1, nb − 1) where nr (nb,
respectively) is the maximum number of vertices of a red (blue, respectively) monotone path
ending with u and v. By the choice of χ, we have D(u, v) ∈ [a − 2] × [u − 2]. Next, we define

D(v) = {x ∈ [a − 2] × [u − 2] : x ⪯ D(u, v) for some u < v}.

By definition, D(v) is a down-set in [a − 2] × [u − 2]. Moreover, since there is no abstract
split k-gon in χ, D(v) has the bounding box r × s where r + s ≤ k − 1.
Consider the mapping v ↦→ D(v). We show that this mapping is injective. Suppose
for contradiction that D(u) = D(v) for some vertices u < v. By definition, we have
D(u, v) ∈ D(v). Since D(u) = D(v), we obtain D(u, v) ∈ D(u) and thus, by the definition
of D(u), there is a vertex t such that t < u and D(u, v) ⪯ D(t, u). However, if χ(t, u, v) is
red, the longest red monotone path ending at u, v is longer than the longest red monotone
path ending at t, u. An analogous claim holds for blue monotone paths if χ(t, u, v) is blue.
In either case, we cannot have D(u, v) ⪯ D(t, u) and we obtain a contradiction.

J. Baek and M. Balko 13:9

Thus, N is at most as large as the number of down-sets in [a−2]×[u−2] with the bounding
box r × s where r + s ≤ k − 1. By Lemma 9, this number equals ∑u
i=k−a+2 (k−2
i−2). ◀

By combining Lemma 10 with (3), we obtain the upper bounds from Theorems 4 and 6.

5.2 Lower bound from Theorem 4

Now, we prove the lower bounds. First, we provide a general construction of 2-colorings that
avoid long monochromatic monotone paths and abstract split k-gons, obtaining the lower
bound Csplit(a, u, k) ≥ 1 + ∑u
i=k−a+2 (k−2
i−2) from Theorem 6. Then, we show that a special
case of this construction can be realized by points in the plane, obtaining a tight lower bound
ESsplit(a, u, k) ≥ 1 + ∑u
i=k−a+2 (k−2
i−2) from Theorem 4.

▶ Lemma 11. For every (a, u, k) ∈ T , we have

Csplit(a, u, k) ≥ 1 +
 u∑

i=k−a+2
 (k − 2
i − 2
 )
.

Proof. We use E := D(a, u) to denote the set of all down-sets in [a − 2] × [u − 2]. In this
proof, we let D := D(a, u, k) be the set of all down-sets in [a − 2] × [u − 2] with the bounding
box r × s where r + s ≤ k − 1 and we set N = |D|. Note that D ⊆ E. We know, by Lemma 9,
that N = ∑u
i=k−a+2 (k−2
i−2). The set E is partially ordered by inclusion ⊆. We let ≤E be an
arbitrary linear extension on E that extends ⊆ on E.
For two down-sets A, B ∈ E with A <E B, choose an arbitrary element δ(A, B) of B \ A.
This is possible, as the fact that ≤E extends ⊆ implies that the set B \ A is non-empty if
A <E B. For i ∈ {1, 2}, we let δ(A, B)i be the ith coordinate of δ(A, B).
We let K3
|E| be the ordered complete 3-uniform hypergraph with the vertex set E ordered
by ≤. We now define the following 2-coloring χa,u = χa,u(δ, ≤E ) of K3
|E|, which is used later
in the paper. The color χa,u(A, B, C) of an edge {A, B, C} of K3
|E| with A < B < C is red if
δ(A, B)1 < δ(B, C)1 and blue otherwise. Note that δ(A, B) ∈ B and δ(B, C) /∈ B and thus
δ(A, B) ̸= δ(B, C). Also, if χa,u(A, B, C) is blue, then δ(A, B)2 < δ(B, C)2 as we cannot
have δ(B, C) ⪯ δ(A, B), because otherwise the fact that B is a down-set in [a − 2] × [u − 2]
together with δ(A, B) ∈ B implies δ(B, C) ∈ B, which is impossible as δ(B, C) ∈ C \ B. Let
χ = χ(δ, ≤E ) be the coloring χa,u restricted to the copy of K3
N in K3
|E| induced by D.
It remains to show that χ contains neither a red copy of P 3
a, a blue copy of P 3
u, nor
an abstract split k-gon as then we have Csplit(a, u, k) ≥ N + 1. To do so, we first prove
by induction on ℓ ≥ 2 that any monochromatic copy of P 3
ℓ in χ with last two vertices
B < C satisfies δ(B, C)1 ≥ ℓ − 1 if all its hyperedges are red in χ and δ(B, C)2 ≥ ℓ − 1
if they are blue. If ℓ = 2, then the claim is trivially true as (1, 1) ⪯ δ(B, C). Thus,
consider ℓ ≥ 3. Let A < B < C be the last three vertices of the monochromatic copy of
Pℓ in χ. If all the hyperedges are red, then the induction hypothesis and the definition
of χ give δ(B, C)1 > δ(A, B)1 ≥ ℓ − 2. Similarly, if the hyperedges are blue, we obtain
δ(B, C)2 > δ(A, B)2 ≥ ℓ − 2. Since all down-sets from D are contained in [a − 2] × [u − 2],
it follows that there is no red copy of P 3
a nor a blue copy of P 3
u in χ. Since every down-set
from D has the bounding box r × s where r + s ≤ k − 1, we also see that there is no abstract
split k-gon in χ. Thus, we have Csplit(a, u, k) ≥ N + 1. ◀

We now prove ESsplit(a, u, k) ≥ N + 1. This can be shown directly using the Erdős–
Szekeres construction P (a, u, k) from Section 4. We prove this claim by showing that a
special case of the construction from the proof of Lemma 11 corresponds to χP (a,u,k).
 S o C G 2 0 2 5

13:10 The Erdős–Szekeres Conjecture Revisited

▶ Lemma 12. For every (a, u, k) ∈ T , we have

ESsplit(a, u, k) ≥ 1 +
 u∑

i=k−a+2
 (k − 2
i − 2
 )
.

The proof of Lemma 12 is omitted. Finally, we remark that using the Erdős–Szekeres
construction in the proof of the tight lower bound on ESsplit(a, u, k) is important. For
example, in the case a = u = k, some of the sets P of 2k−2 points constructed in Section 4
do not have k points in convex position but contain split (2k − 4)-gons.

6 Avoiding k points in convex position

Here, we introduce new constructions of sets of 2k−2 points in general position with no k
points in convex position, generalizing all previously known constructions of such point sets.
For integers a, u, k ≥ 2, let P ′(a, u) be an arbitrary set of (a+u−4
a−2 ) points in general
position in the plane with no a-cap and no u-cup. If (a, u, k) ∈ T , let P ′(a, u, k) and
P (a, u, k) be sets of ∑u
i=k−a+2 (k−2
i−2) points in general position in the plane with no a-cap,
no u-cup, and no k points in convex position where P (a, u, k) is the point configuration given
by the Erdos-Szekeres construction and P ′(a, u, k) is an arbitrary such point configuration.
Both sets are described in Section 4.
We let S be a set of points p1, . . . , pN sorted by increasing x-coordinates. We use the
term factor for an integer k that is used as a parameter that corresponds to the forbidden
size of a subset in convex position of an enlarged point set obtained from S. For integers i
and j with 1 ≤ i < j ≤ N , we let si,j be the maximum number of points from S that are in
convex position and have pi and pj as their leftmost and rightmost points, respectively.
We now define a blow-up operation that is the core of our construction and will help us
obtain large sets with few points in convex position; see Figure 3 for an illustration.

▶ Definition 13 ((X, Y )-blow-up of S). Let X = (x1, . . . , xN ) and Y = (y1, . . . , yN ) be
sequences of non-negative integers. For a factor k ∈ N0, an (X, Y )-blow-up bX,Y,k(S) of
S with respect to k is a point set obtained from S by replacing each point pi of S with
i ∈ {2, 3, . . . , N − 1} with an affine image Cpi of P ′(yi + 2, xi + 2) that is rotated clockwise by
π/2, is almost vertical and lies in a small neighborhood of pi. The point p1 is replaced with
an affine image Cp1 of P ′(k, x1 + 2, k), where this copy is rotated clockwise by π/2, is almost
vertical and lies in a small neighborhood of p1. Similarly, the point pN is analogously replaced
with an affine image CpN of P ′(yN +2, k, k). We choose the neighborhoods small enough so that
they are disjoint for different sets Cpi and for all triples i1, i2, i3 with 1 ≤ i1 < i2 < i3 ≤ N ,
the triple (pi1, pi2 , pi3 ) has the same orientation as each triple (qi1, qi2 , qi3 ) where qij ∈ Cpij .
Also, Cpi is almost vertical, meaning that for every pj ∈ S with j ̸= i any line determined by
two points of Cpi has all points of Cpj on the same side as the vertical line containing pi.
We call the sets Cpi clusters.

For each pi, every a-cap in the pre-image of Cpi corresponds to a left convex chain of
size a in Cpi and every u-cup in the pre-image of Cpi corresponds to a right convex chain of
size u in Cpi. We note that the constructions could be stated without the rotation by π/2,
but this version will be more natural in later constructions. In the following result, we state
how (X, Y )-blows-ups of arbitrary point sets affect the size of the largest subset in convex
position in the resulting point sets and also describe how large these point sets are.

J. Baek and M. Balko 13:11

SX, Y, kp1p2p3p4p5bX,Y,k(S)Cp1Cp2Cp3Cp4Cp5xiyiau
 Figure 3 An illustration of an (X, Y )-blow-up of a point set S and its subset in convex position.

▶ Lemma 14 (General blow-up construction). For k, N ∈ N, and a set S of N points in
the plane in general position, let X = (x1, . . . , xN ) and Y = (y1, . . . , yN ) be sequences of
non-negative integers satisfying
(a) xi + yi ≤ k − 1 for every i ∈ [N ] and
(b) xi + yj ≤ k − 1 − si,j for all i, j ∈ [N ] with i < j.
Then, the (X, Y )-blow-up bX,Y,k(S) of S does not contain k points in convex position and

|bX,Y,k(S)| =
 x1∑

l=0
 (
k − 2
l
 ) +
 N −1∑

i=2
 (xi + yi
xi
 ) +
 yN∑

l=0
 (
k − 2
l
 ).

The proof of Lemma 14 is omitted. Observe that it follows from the second condition
that the factor k is larger than the size of the largest convex subset of S as the numbers xi
and yi must be non-negative.

6.1 All known constructions

We now show that for each set S and factor k = |S| + 1 there are sequences X and Y such
that |bX,Y,k(S)| = 2k−2 with no k points in convex position. It will follow that all known
constructions of sets of 2
k−2 points in general position with no k points in convex position are
a special case of an (X, Y )-blow-up. We recall that all such known constructions fall within
Valtr’s construction. Now, let S be an arbitrary set of N ≤ k − 1 points in general position.
We set xi = i − 1, and yi = k − i − 1 for every i ∈ [N ]. Then, clearly, xi + yi = k − 2 ≤ k − 1
and xi, yi ≥ 0 for every i ∈ [N ] as |S| = N ≤ k − 1. We have xi + yj ≤ k − 1 − si,j for all
i, j ∈ [N ] with i < j, as si,j ≤ j −i+1 and (i−1)+(k −j −1) = k −1−(j −i+1) ≤ k −1−si,j.
Thus, all assumptions in Lemma 14 are met, and bX,Y,k(S) does not contain k points in
convex position. If N = k − 1, then we also get

|bX,Y,k(S)| =
 0∑

l=0
 (
k − 2
l
 ) +
 N −1∑

i=2
 (xi + yi
xi
 ) +
 0∑

l=0
 (
k − 2
l
 )

= 1 +
 k−2∑

i=2
 (k − 2
i − 1
 ) + 1 = 2
k−2

and bX,Y,k(S) corresponds to Valtr’s construction rotated by π/2.
 S o C G 2 0 2 5

13:12 The Erdős–Szekeres Conjecture Revisited

6.2 New construction

The previous choices of X and Y are not the only ones that work, we describe another choice
of an (X, Y )-blow-up to obtain a set of 2k−2 points with no k-tuple in convex position for
any k ≥ 3. This time, the sequence X will not be increasing, and we allow k < |S|.
We now proceed with the construction. For each point pi, each subset of S in convex
position with pi as its rightmost point (leftmost point) is called a left-gon at pi (right-gon at
pi, respectively). For a threshold L ∈ {0, 1, . . . , N }, we call points pi with i ∈ [L] left and
points pj with j ∈ [N ] \ [L] right. For each left (right, respectively) point pi, we define si as
the maximum size of left-gon at pi (right-gon at pi, respectively). Note that if L ∈ [N − 1]
there are exactly two points pi of S with si = 1, namely, the leftmost and the rightmost point
of S. For every positive integer j, let vj,L(S) be the number of points pi of S with si = j.
If xi = x and yi = k − 1 − x − si for every i ∈ [L] and xi = k − 1 − x − si and yi = x for
each i ∈ [N ] \ [L], then we call the set bX,Y,k(S) an x-blow-up of S with respect to threshold
L and factor k and denote it by bx,k,L(S). We now show that the size of the x-blow-up of S
can be expressed in terms of the numbers vj,L(S).

▶ Corollary 15. For a set S of N points in the plane in general position, let x be a non-
negative integer and choose m = k − 2x for some threshold L ∈ [N − 1] and factor k ≥ 1. If
S does not contain m points in convex position, then the x-blow-up bx,k,L(S) of S does not
contain k points in convex position and

|bx,k,L(S)| = 2
 x∑

l=0
 (k − 2
l
 ) +
 k−2x−1∑

j=2 vj,L(S) · (k − j − 1
x
 ).

The proof of Corollary 15 is omitted. It follows from Corollary 15 that in order to produce
large x-blow-ups without k points in convex position, point sets S with suitable values vj,L(S)
for some threshold L are useful. We now provide a simple formula for the values vj,N (P ) in
the Erdős–Szekeres construction P = P (k, k, k) where all points are labeled as left.

▶ Lemma 16. For every integer k ≥ 2, if we set the threshold L = 2k−2, then, for
P = P (k, k, k), we have

vj,L(P ) =
 




1, for j = 1,

2j−2, for j ∈ {2, . . . , k − 1},

0, otherwise.

The proof of Lemma 16 is omitted. Analogously, we get the same values vj,0(P ) if all
points of P (k, k, k) are labeled as right, that is, if we set L = 0.
We now construct a point set M with |M | = 2m−2 and without m points in convex
position that has larger x-blow-ups than P = P (m, m, m).

▶ Definition 17 (Point set M ). We construct the following set M that contains 2m − 2 points
ℓ1, . . . , ℓm−1, , r1, . . . , rm−1 in the plane in general position. We let ℓ1 = (−m, 0), r1 = (m, ε),
ℓ2 = (−m + 1, 1), and r2 = (m − 1, 1 + ε) for some small ε > 0. We now specify the placement
of the remaining points ℓ3, . . . , ℓm−1 and r3, . . . , rm−1 inductively; see Figure 4. Assume that
we have placed points ℓ1, . . . , ℓi and r1, . . . , ri for some i ≥ 2. We now let ℓi+1 be a point
above the lines ℓi−1ℓi and ri−1ri to the right of ℓi−1 and to the left of the line x = 0 and we
let ri+1 be a point above the lines ℓi−1ℓi and ri−1ri to the left of ri and to the right of the
line x = 0 so that y(ri+1) > y(ℓi+1).

J. Baek and M. Balko 13:13

We let P ′ be a point set obtained by replacing each point ℓi with i ∈ [m − 1] with a copy
of the set P (m − i + 1, i) that lies in a sufficiently small neighborhood of ℓi. We denote this
copy as Cℓi. Note that Cℓ1 = ∅. We then let P ′′ be a point set obtained by replacing each
point ri with i ∈ [m − 1] with a copy of the set P (m − i, i + 1) that lies in a sufficiently small
neighborhood of ri. We use Cri to denote this copy and note that Crm−1 = ∅. Note that the
point sets P ′ and P ′′ then form affine copies of the point set P (m − 1, m − 1, m − 1). Let
M = P ′ ∪ P ′′ and note that |M | = 2
m−2.

P (m, 1) = ∅P (m − 1 , 2)P (m − 1 , 2)r1r2P (m − 1 , 2)P (m − 2 , 3)ℓ1r1ℓ2r2r5P (m − 5 , 6) = ∅ℓ5P (m − 4 , 5)r4P (m − 4 , 5)ℓ4P (m − 3 , 4)P (m − 3 , 4)r3P (m − 2 , 3)ℓ3
 Figure 4 Example of the construction of the point set M for m = 6.

Now, if we set the threshold L = 2
m−3, then the left points of M are the points from P ′,
and the right points of M are the points of P ′′. We also obtain the following formulas.

▶ Lemma 18. For every integer m ≥ 3, the set M does not contain m points in convex
position and, for the threshold L = 2
m−3, satisfies

vj,L(M ) =
 



2, for j = 1,

2
j−1, for j ∈ {2, . . . , m − 2},

0, otherwise.
 (4)

The proof of Lemma 18 is omitted. We now prove that suitable x-blow-ups of M produce
new sets of 2
k−2 points in the plane in general position that do not contain k points in convex
position, obtaining a new construction of such point sets.

▶ Theorem 19. For each positive integer x and k ≥ 2x + 3, let m = k − 2x. The x-blow-up
bx,k,L(M ) of the point set M with respect to the threshold L = 2m−3 does not contain k
points in convex position and |bx,k,L(M )| = 2
k−2.

Proof. By applying the x-blow-up from Corollary 15 with parameters x, k, and L = 2m−3

to M , we obtain a set bx,k,L(M ) of

|bx,k,L(M )| =
 x∑

l=0
 (k − 2
l
 ) +
 k−2x−2∑

j=2 2
j−1 · (
k − j − 1
x
 ) +
 k−2∑

l=k−x−2
 (k − 2
l
 )

points in the plane in general position that contains no k points in convex position.
To show that |bx,k,L(M )| equals 2k−2 it suffices to prove that

k−x−3∑

l=x+1
 (k − 2
l
 ) =
 k−2x−2∑

j=2 2j−1 · (k − j − 1
x
 )
 S o C G 2 0 2 5

13:14 The Erdős–Szekeres Conjecture Revisited

if k ≥ 2x + 3, as then |bx,k,L(S)| = 2k−2 follows by the binomial theorem. This equality is
true because both sides count the number of subsets of [k − 2] of size at least x + 1 and at
most k − x − 3. This is trivial for the left-hand side. To prove the right-hand side, let F
be the set of subsets of [k − 2] of size at least x + 1 and at most k − x − 3. For F ∈ F, we
let j be the minimum element from [k − 2] such that either F or its complement contains
exactly x + 1 elements in {j − 1, . . . , k − 2}. Note that such j is uniquely determined for
each F ∈ F and that j ∈ {2, . . . , k − 2x − 2}. On the other hand, we can uniquely determine
set F from F by selecting j − 1, deciding whether F or its complement has exactly x + 1
elements in {j − 1, . . . , k − 2} and then select the remaining x of them from {j, . . . , k − 2} to
F (or to its complement, respectively) and, finally, select an arbitrary subset of [j − 2] to F
(or its complement, respectively). ◀

6.3 Computational experiments

Since there are other possible choices for X and Y , one might wonder whether some of
them yield constructions of more than 2
k−2 points without k points in convex position. We
implemented a simple program in Matlab based on a non-linear optimization solver to find
as large (X, Y )-blow-up of a given point set as possible. Given a set of N points in the plane
in general position and a factor k, this solver tries to find a solution (x1, . . . , xN , y1, . . . , yN )
that satisfies the linear constraints from Lemma 14 and that has as large value of the function

x1∑

l=0
 (k − 2
l
 ) +
 N −1∑

i=2
 (
xi + yi
xi
 ) +
 yN∑

l=0
 (k − 2
l
 )

as possible. Since the objective function is not linear, we used a solver based on a genetic
algorithm that does not guarantee finding a true optimum solution. We tried various point
sets on the input, including subsets of P (a, u) and random point sets. Using this program,
we obtained many examples of 2k−2 points for various choices of S and k up to 20. Even
though there is some freedom in choosing X and Y , the size of the (X, Y )-blow-up never
exceeded 2
k−2. So the Erdős–Szekeres conjecture remains open.

References

1 J. Baek. On the Erdős-Tuza-Valtr conjecture. European J. Combin., 124:Paper No. 104085,
15, 2025. doi:10.1016/j.ejc.2024.104085.
2 M. Balko. Ramsey numbers and monotone colorings. J. Combin. Theory Ser. A, 163:34–58,
2019. doi:10.1016/j.jcta.2018.11.013.
3 M. Balko, J. Cibulka, K. Král, and J. Kynčl. Ramsey numbers of ordered graphs. Electron. J.
Combin., 27(1), 2020. doi:10.37236/7816.
4 M. Balko and P. Valtr. A SAT attack on the Erdős–Szekeres conjecture. European Journal of
Combinatorics, 66:13–23, 2017. doi:10.1016/j.ejc.2017.06.010.
5 F. R. K. Chung and R. L. Graham. Forced convex n-gons in the plane. Discrete Comput.
Geom., 19(3):367–371, 1998. doi:10.1007/PL00009353.
6 D. Conlon, J. Fox, C. Lee, and B. Sudakov. Ordered Ramsey numbers. J. Combin. Theory
Ser. B, 122:353–383, 2017. doi:10.1016/J.JCTB.2016.06.007.
7 P. Erdős and G. Szekeres. A combinatorial problem in geometry. Compos. Math., 2:463–470,
1935.
8 P. Erdős and G. Szekeres. On some extremum problems in elementary geometry. Ann. Univ.
Sci. Budapest. Eötvös Sect. Math., 3–4:53–62, 1960–61.
9 P. Erdős, Z. Tuza, and P. Valtr. Ramsey-remainder. European J. Combin., 17(6):519–532,
1996. doi:10.1006/EUJC.1996.0045.

J. Baek and M. Balko 13:15

10 S. Felsner and H. Weil. Sweeps, arrangements and signotopes. Discrete Appl. Math., 109(1–
2):67–94, 2001. doi:10.1016/S0166-218X(00)00232-8.
11 J. Fox, J. Pach, B. Sudakov, and A. Suk. Erdős–Szekeres-type theorems for monotone paths
and convex bodies. Proc. London Math. Soc., 105(5):953–982, 2012.
12 J. E. Goodman and R. Pollack. A combinatorial perspective on some problems in geometry.
In Proceedings of the Twelfth Southeastern Conference on Combinatorics, Graph Theory and
Computing, Vol. I, volume 32 of Congressus Numerantium, pages 383–394, 1981.
13 A. F. Holmsen, H. N. Mojarrad, J. Pach, and G. Tardos. Two extensions of the Erdős–
Szekeres problem. Journal of the European Mathematical Society, 22:3981–3995, 2020. doi:
10.4171/JEMS/1000.
14 D. Kleitman and L. Pachter. Finding convex sets among points in the plane. Discrete Comput.
Geom., 19(3):405–410, 1998. doi:10.1007/PL00009358.
15 J. Matoušek. Lectures on discrete geometry, volume 212 of Graduate Texts in Mathematics.
Springer-Verlag, New York, 2002.
16 H. N. Mojarrad and G. Vlachos. An improved upper bound for the Erdős-Szekeres conjecture.
Discrete Comput. Geom., 56(1):165–180, 2016. doi:10.1007/S00454-016-9791-5.
17 G. Moshkovitz and A. Shapira. Ramsey theory, integer partitions and a new proof of the
Erdős-Szekeres theorem. Adv. Math., 262:1107–1129, 2014.
18 S. Norin and Y. Yuditsky. Erdős-Szekeres without induction. Discrete Comput. Geom.,
55(4):963–971, 2016. doi:10.1007/S00454-016-9778-2.
19 L. Peters and G. Szekeres. Computer solution to the 17-point Erdős–Szekeres problem.
ANZIAM J., 48(2):151–164, 2006.
20 A. Suk. On the Erdős-Szekeres convex polygon problem. J. Amer. Math. Soc., 30(4):1047–1053,
2017.
21 G. Tóth and P. Valtr. Note on the Erdős–Szekeres theorem. Discrete Comput. Geom.,
19(3):457–459, 1998.
22 G. Tóth and P. Valtr. The Erdős–Szekeres theorem: upper bounds and related results. In
Combinatorial and computational geometry, volume 52 of Math. Sci. Res. Inst. Publ., pages
557–568, Cambridge, 2005. Cambridge University Press.
23 P. Valtr. Convex independent sets and 7-holes in restricted planar point sets. Discrete &
Computational Geometry, 7(2):135–152, 1992. doi:10.1007/BF02187831.
24 P. Valtr. Private communication, 2024.
 S o C G 2 0 2 5
