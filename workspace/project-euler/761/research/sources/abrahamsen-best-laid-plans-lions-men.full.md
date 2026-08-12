<!-- source: http://dagstuhl.sunsite.rwth-aachen.de/volltexte/2017/7205/pdf/LIPIcs-SoCG-2017-6.pdf | converted from PDF -->

Best Laid Plans of Lions and Men

Mikkel Abrahamsen
∗1, Jacob Holm
2, Eva Rotenberg
3, and
Christian Wulﬀ-Nilsen4

1 Department of Computer Science, University of Copenhagen, Copenhagen,
Denmark
miab@di.ku.dk
2 Department of Computer Science, University of Copenhagen, Copenhagen,
Denmark
jaho@di.ku.dk
3 Department of Computer Science, University of Copenhagen, Copenhagen,
Denmark
roden@di.ku.dk
4 Department of Computer Science, University of Copenhagen, Copenhagen,
Denmark
koolooz@di.ku.dk

Abstract

We answer the following question dating back to J. E. Littlewood (1885–1977): Can two lions
catch a man in a bounded area with rectiﬁable lakes? The lions and the man are all assumed
to be points moving with at most unit speed. That the lakes are rectiﬁable means that their
boundaries are ﬁnitely long. This requirement is to avoid pathological examples where the man
survives forever because any path to the lions is inﬁnitely long. We show that the answer to
the question is not always “yes” by giving an example of a region R in the plane where the
man has a strategy to survive forever. R is a polygonal region with holes and the exterior and
interior boundaries are pairwise disjoint, simple polygons. Our construction is the ﬁrst truly
two-dimensional example where the man can survive.
Next, we consider the following game played on the entire plane instead of a bounded area:
There is any ﬁnite number of unit speed lions and one fast man who can run with speed 1 + ε
for some value ε > 0. Can the man always survive? We answer the question in the aﬃrmative
for any constant ε > 0.

1998 ACM Subject Classiﬁcation I.3.5 Computational Geometry and Object Modeling

Keywords and phrases Lion and man game, Pursuit evasion game, Winning strategy

Digital Object Identiﬁer 10.4230/LIPIcs.SoCG.2017.6

1 Introduction

‘A lion and a man in a closed circular arena have equal maximum speeds. What tactics should
the lion employ to be sure of his meal?’
1 These words (including the footnote) introduce the
now famous lion and man problem, invented by R. Rado in the late thirties, in Littlewood’s
Miscellany [15]. It was for a long time believed that in order to avoid the lion, it was optimal
for the man to run on the boundary of the arena. A simple argument then shows that the

∗ Research partly supported by Mikkel Thorup’s Advanced Grant from the Danish Council for Independent
Research under the Sapere Aude research career programme.
1 The curve of pursuit (L running always straight at M ) takes inﬁnite time, so the wording has its point.

© Mikkel Abrahamsen, Jacob Holm, Eva Rotenberg, and Christian Wulﬀ-Nilsen;
licensed under Creative Commons License CC-BY
33rd International Symposium on Computational Geometry (SoCG 2017).
Editors: Boris Aronov and Matthew J. Katz; Article No. 6; pp. 6:1–6:16
Leibniz International Proceedings in Informatics
Schloss Dagstuhl – Leibniz-Zentrum für Informatik, Dagstuhl Publishing, Germany

6:2 Best Laid Plans of Lions and Men

lion could always catch the man by staying on the radius OM deﬁned by the man while
approaching him as much as possible. However, A.S. Besicovitch proved in 1952 that the man
has a very simple strategy (following which he will approach but not reach the boundary)
that enables him to avoid capture forever no matter what the lion does. See [15] for details.

Throughout this paper, all men, lions, and other animals are assumed to be points. One
can prove that two lions are enough to catch the man in a circular arena, and Croft [8]
proves that in general a necessary and suﬃcient number of birds to catch a ﬂy inside an
n-dimensional spherical cage is just n (again, we assume that the ﬂy and the birds have
equal maximum speeds).

A well-known related discrete game is the cop and robber game: Let G be a ﬁnite connected
undirected graph. Two players called cop C and robber R play a game on G according to
the following rules: First C and then R occupy some vertex of G. After that they move
alternately along edges of G. The cop C wins if at some point in time C and R are on the
same vertex. If the robber R can prevent this situation forever, then R wins. The robber
has a winning strategy on many graphs including all cycles of length at least 4. Therefore,
the cop player C can be given a better chance by allowing him, say, k cops C1, . . . , Ck. At
every turn C moves any non-empty subset of {C1, . . . , Ck}. Now, the cop-number of G is
the minimal number of cops needed for C to win. Aigner and Fromme [2] observes that the
cop-number of the dodecahedron graph is at least 3, since if there are only 2 cops, the robber
can always move to a vertex not occupied by a cop and not in the neighbourhood of any.
Furthermore, they prove that the cop-number of any planar graph is at most 3. Thus, the
cop-number of the dodecahedron is exactly 3.

Returning to the lion and man game, Bollobás [6] writes that the following open problem
was already mentioned by J.E. Littlewood (1885–1977): Can two lions catch a man in a
bounded (planar) area with rectiﬁable lakes? An informal deﬁnition of a rectiﬁable curve
is that it has ﬁnite length. We require that the boundaries of the lakes and the exterior
boundary are all rectiﬁable curves to avoid pathological examples where the man survives
forever because any path to the lions is inﬁnite. Bollobás mentions the same problem in a
comment in his edition of Littlewood’s Miscellany [15] and in [7]. The problem is also stated
by Fokkink et al. [11]. Berarducci and Intrigila [4] prove that the man can survive forever
(for some initial positions of the man and lions) if the area is a planar embedding of the
dodecahedron graph where each edge is a curve with the same length, say length 1. The
proof is essentially the same as the proof by Aigner and Fromme [2] that the cop-number of
the dodecahedron is at least 3: When the man is standing at a vertex, there will always be a
neighbouring vertex with distance more than 1 to the nearest lion. It is thus safe for the
man to run to that vertex. This, however, is a one-dimensional example. Berarducci and
Intrigila raise the question whether it is possible to replace the one-dimensional edges by
two-dimensional thin lines.

We present a truly two-dimensional region R in the plane where two lions are not enough
to ever catch the man. We say that R is truly two-dimensional since R is a polygonal region
with holes and the exterior and interior boundaries are all pairwise disjoint, simple polygons
– in particular, they are clearly rectiﬁable. We were likewise inspired by the dodecahedron in
the construction of our example. We explain the construction in Section 2.

Rado and Rado [16] and Janković [13] consider the problem where there are many lions
and one man, but where the game is played in the entire unbounded plane. They prove
that the lions can catch the man if and only if the man starts in the interior of the convex
hull of the lions. Inspired by that problem, we ask the following question: What if the lions
have maximum speed 1 and the man has maximum speed 1 + ε for some ε > 0? We prove

M. Abrahamsen, J. Holm, E. Rotenberg, and C. Wulﬀ-Nilsen 6:3

that for any constant ε and any ﬁnite number of lions, such a fast man can survive forever
provided that he does not start at the same point as one of the lions. We explain a strategy
in Section 3.
Other variants of the game with a faster man have been studied previously. Flynn [9, 10]
and Lewin [14] study the problem where there is one lion and one fast man in a circular
arena. The lion tries to get as close to the man as possible and the man tries to keep the
distance as large as possible. Variants of the cop and robber game where the robber is faster
than the cops have also been studied. See for instance [3, 12].

1.1 Deﬁnitions

We follow the conventions of Bollobás et al. [5]. Let R ⊆ R2 be a region in the plane on
which the lion and man game is to be played, and assume that the lion starts at point l0
and the man at point m0. We deﬁne a man path as a function m : [0, ∞) −→ R satisfying
m(0) = m0 and the Lipschitz condition ∥m(s) − m(t)∥ ≤ V · |s − t|, where V is the speed of
the man. In our case, we either have V = 1 or, in the case of a fast man, V = 1 + ε for some
small constant ε > 0. Note that it follows from the Lipschitz condition that any man path is
continuous. A lion path l is deﬁned similarly, but the lions we consider always run with at
most unit speed. Let L be the set of all lion paths and M be the set of all man paths. Then
a strategy for the man is a function M : L −→ M such that if l, l′ ∈ L agree on [0, t], then
M (l) and M (l′) also agree on [0, t]. This last condition is a formal way to describe that the
man’s position M (l)(t), when he follows strategy M , depends only on the position of the
lion at points in time before and including time t, i.e., he is not allowed to act based on the
lion’s future movements. (By the continuity of any man path, the man’s position at time t
is in fact determined by the lion’s position at all times strictly before time t.) A strategy
M for the man is winning if for any l ∈ L and any t ∈ [0, ∞), it holds that M (l)(t) ̸= l(t).
Similarly, a strategy for the lion L : M −→ L is winning if for any m ∈ M, it holds that
L(m)(t) = m(t) for some t ∈ [0, ∞). These deﬁnitions are extended to games with more than
one lion in the natural way.
It might seem unfair that the lion is not allowed to react on the man’s movements when
we evaluate whether a strategy M for the man is winning. However, we can give the lion full
information about M and allow it to choose its path l depending on M prior to the start of
the game. If M is a winning strategy, the man can also survive the lion running along l.
We call a man strategy M locally ﬁnite if it satisﬁes the following property: if l and l′ are
any two lion paths that agree on [0, t] for some t then the corresponding man paths M (l) and
M (l′) agree on [0, t + δ] for some δ > 0 (we allow that δ depends on l|[0,t]). Thus, informally,
the man commits to doing something for some positive amount of time dependent only on
the situation so far. Bollobás et al. [5] prove that if the man has a locally ﬁnite winning
strategy, then the lion does not have any winning strategy. The argument easily extends
to games with multiple lions. At ﬁrst sight, it might sound absurd to even consider the
possibility that the lion has a winning strategy when the man also does. However, it does
not follow from the deﬁnition that the existence of a winning strategy for the man implies
that the lion does not also have a winning strategy. See the paper by Bollobás et al. [5] for a
detailed discussion of this (including descriptions of natural variants of the lion and man
game where both players have winning strategies). In each of the problems we describe, the
winning strategy of the man is locally ﬁnite, so it follows that the lions do not have winning
strategies. In fact, the strategies we describe satisfy the much stronger condition that they
are equitemporal, i.e., there is a constant ∆ > 0 such that the man at any point in time i · ∆,
for i = 0, 1, . . ., decides where he wants to run until time (i + 1) · ∆.
 S o C G 2 0 1 7

6:4 Best Laid Plans of Lions and Men

2 The Man Surviving Two Lions in a Bounded Area

In this section, we present a polygonal region R in the plane with 11 lakes. See [1] for an
illustration of such a region. The exterior and interior boundaries of R are all pairwise
disjoint simple polygons, and a man can survive forever in R against two lions provided that
the lions are initially at a suﬃcient distance.
Consider a planar embedding D of the dodecahedron where each edge is a polygonal
curve. We can obtain that all edges have the same length by prolonging some edges using a
zig-zag pattern. This embedding corresponds to an area with 11 lakes and inﬁnitely thin
paths between the lakes, and as observed by Berarducci and Intrigila [4], the man can survive
forever against two lions on such an embedding by deciding at each vertex which neighbouring
vertex to visit next. First, we explain why it is not straight-forward to obtain the region R
from D, or, at least, why some natural initial attemps will not work.
We want to “thicken” each edge of D such that the boundaries of the lakes become
disjoint, thus obtaining a truly two-dimensional region D′ containing D as a subset. However,
doing so, the point in D′ corresponding to a vertex of D does not necessarily lie on the
shortest path between its neighbours. We thus cannot simply employ the strategy from D,
roughly speaking, because the man must plan in advance which turn to take in the upcoming
vertex. Thus, before he reaches the region Rv corresponding to a given vertex, he should
already know which neighbouring vertex he will visit afterwards. Then, he can choose a path
through Rv that makes the concatenated path shortest possible.
In order to carry out this idea, we ﬁrst need to describe a winning strategy of the man
on the dodecahedron graph with the special property that he does not make his decisions
at the vertices. Let G be a planar embedding of the dodecahedron where all edges have
length 4. The distance between two points in G is the length of a shortest path between
the points. Let the quarters denote the points on the edges of G at distance 1 to the closest
vertex. Consider a quarter x on the edge ab of G. For a point p ∈ G, p ̸= x, let da(x, p) be
the length of a shortest simple path in G from x to p that initially follows the edge {a, b} in
direction towards a. Let db(x, p) be deﬁned similarly.
When the man is at a quarter x with distance 1 to the vertex a and 3 to the vertex b, we
let dnear denote the distance from x to the closest lion with respect to da, and let dfar denote
the distance from x to the closest lion with respect to db. To avoid confusion, we write them
as dnear(t) and dfar(t) when x is the position of the man at the time t.
We will now show that if the lions are suﬃciently far away in the initial situation, there
exists a winning strategy for the man where he only takes stock of the situations in the
quarters. That is, when he reaches a quarter, he must plan for the next 2 units of time where
to run to, and then he has reached a quarter again, and so on.

▶ Invariant 1. In the scenario described above:
1. The man is standing on a quarter.
2. min{dnear, dfar} ≥ 1.
3. At least one of the two following statements is true:
dnear ≥ 3
dfar ≥ 7

▶ Lemma 2. If Invariant 1 is satisﬁed initially, the man has a winning strategy by which he
runs from quarter to quarter at unit speed so that Invariant 1 is true at any quarter. The
strategy maintains Invariant 1 Point 2 at all times, that is, that the closest lion is always at
least at distance 1.

M. Abrahamsen, J. Holm, E. Rotenberg, and C. Wulﬀ-Nilsen 6:5

Figure 1 A situation from the proof of
Lemma 2. Imagine that all edges have length
4. The lion lnear is in the red part.
 Figure 2 The embedding D of the dodeca-
hedron. All edges have lengths 1 or 3.

Proof. Let x denote the position of the man at the time t, and assume the invariant holds.
We prove that he can run to another quarter x′ without getting caught such that the invariant
again holds when he reaches x′.
The proof goes by inspecting cases. Let ab be the edge containing x and suppose a be
the nearest vertex to x and b the furthest.
Case 1: dfar(t) ≥ 7. Let y denote the other quarter on the same edge as x. We claim that
the man can run to y without violating the invariant. We must thus argue that the invariants
are satisﬁed at time t+2 for a man situated at y. First, note that he will not encounter any lion
while running towards y because dfar(t) > 4. Note also that dfar(t + 2) ≥ 1, since dnear(t) ≥ 1
and the worst case is that the lion follows the man. Furthermore, dnear(t + 2) ≥ 7 − 4 = 3,
since dfar(t) ≥ 7 and the worst case is that the man and lion have run towards each other.
Thus, the invariant holds at the time t + 2.
Case 2: dfar < 7, and thus dnear(t) ≥ 3. In this case, we exploit the fact that dfar is so
small that we can bound dfar(t + 2) from below. Let lfar denote the lion at distance dfar from
x, and let lnear denote the other lion. Consider the two other quarters at distance 1 from a,
call them q1 and q2. Assume without loss of generality that q1 is furthest from lnear. The
situation is sketched in Figure 1. We now argue that the man can choose to run towards
q1 without getting eaten, and while maintaining the invariant. Let b′ denote the vertex at
distance 3 to q1. Note that db′(q1, lfar(t)) ≥ 11 and thus, db′(q1, lfar(t + 2)) ≥ 9.
In Figure 1, the points that are both ≥ 3 from x, and (weakly) closer to q2 than to q1, are
marked with red, and hence by our choice of q1, lnear must be in the subset marked with red
at time t. As is easily seen by inspection, db′ (q1, lnear(t)) ≥ 9, and thus db′ (q1, lnear(t+2)) ≥ 7.
But then, dfar(t + 2) ≥ min{9, 7} = 7, and Invariant 1.1 and 3 are maintained.
To see that Invariant 1.2 is still maintained, note that da(q1, lnear(t)) ≥ 3 and therefore
da(q1, lnear(t + 2)) ≥ 1. Similarly, since db(x, lfar(t)) ≥ 1, we have da(q1, lfar(t)) ≥ 3 so that
da(q1, lfar(t + 2)) ≥ 1. Thus, lnear(t + 2) ≥ 1, and we are done. ◀

Our ﬁrst goal is to ﬁnd an embedding G of the dodecahedron in the plane with the
properties described below, which will make it easier for us to construct the region R.
 S o C G 2 0 1 7

6:6 Best Laid Plans of Lions and Men

Figure 3 Regardless of angles between
a, b, c, we can introduce bends to make the
three edges meet at v in angles of size 3π
2 and
at the same time extend the lengths suitably.
 Figure 4 The shortest paths in the circle Dv
between any two of a, b, c, that avoid crossing the
polygonal curves Pvf , Pvg, Pvh all have length 1/8.

▶ Lemma 3. There exists a planar embedding G of the dodecahedron such that
all edges have length 4,
all edges consist of line segments with lengths being multiples of 1
8 ,
any pair of line segments from diﬀerent edges that meet at a vertex each have length 1/4
and form an angle of size 2π
3 , and
for any vertex v, the circle Dv centered at v with radius 1/16 only intersects the three
edges incident to v.

After proving this lemma, we derive from G a truly two-dimensional area R in the plane
where the man can survive against two lions. Lemma 2 gives a winning strategy for the man
in G where he runs from quarter to quarter. The paths along which he runs in R will be
exactly the same as in G except for inside the circles Dv.
We ﬁrst need the following elementary geometric observations:

▶ Observation 4. There exists a planar embedding D of the dodecahedron such that all edges
have length 1 or 3. D furthermore has the property that the circle of radius 1
4 centered at
any vertex v only intersects the three edges incident to v. (See Figure 2.)

▶ Lemma 5. For any three points a, b, c on a circle C, there exist a equilateral triangle
with corners a
′, b
′, c
′ on C where {a, b, c} and {a
′, b
′, c
′} are disjoint and such that, when
considering the points a, b, c, a
′, b
′, c
′ all together, a is a neighbour of a
′, and b is a neighbour
of b
′, and c is a neighbour of c′.

Proof. See Figure 3. The points a, b, c divide C into three arcs. Clearly, we can choose an
equilateral triangle with corners on C disjoint from {a, b, c} so that not all three corners of
the triangle are on the same arc. It is now easy to label the corners of the triangle with
a
′, b
′, c
′ to satisfy the lemma. ◀

We are now ready to prove that a planar embedding G of the dodecahedron exists as
stated in Lemma 3.

Proof of Lemma 3. Start with the embedding D shown in Figure 2, where all edges have
length 1 or 3. Consider a vertex v and the circle Cv of radius r = 1
4 centered at v. Assume the
three edges incident to v enter Cv in the points a, b, c, and let ua, ub, uc be the neighbouring

M. Abrahamsen, J. Holm, E. Rotenberg, and C. Wulﬀ-Nilsen 6:7

Figure 5 The edge euv of G is red and is one of the edges bounding the face f , which is above
euv. The polygonal curve Quv, which is on the boundary of the lake Lf , is blue.

vertices of v such that a is a point on the edge {ua, v}, b is a point on {ub, v}, and c is a
point on {uc, v}. We now delete the segments va, vb, and vc, and therefore need to reconnect
a, b, and c to v. We explain how to reconnect a to v; b and c are handled analogously.
We ﬁnd points a
′, b
′, c
′ on Cv as described in Lemma 5. See Figure 3. We ﬁrst connect
a
′ to v. We now need to connect a to a
′ using some bends. A bend is two segments xy
and yz, each of length r/2 = 1/8, such that x and z are on Cv and y is in the interior of
Cv. If the edge {ua, v} had length 3 in D, we make two bends that together connect a and
a
′. We thus increase the length of the edge {ua, v} by 1/2 in each end and the resulting
edge has length 4. If the edge {ua, v} had length 1 in D, we connect a and a′ by 6 bends,
corresponding to extending the length of the edge by 3. The result is a planar embedding G
of the dodecahedron with the properties stated in the lemma. ◀

We now describe how to make the region R. We want each quarter of G to be a point in
R and we want all pairs of quarters to have the same distances in G and R. It will then follow
from Lemma 2 that the man has a winning strategy by running from quarter to quarter in
R. We make one lake Lf corresponding to each face f of G. Here, we also consider the outer
boundary of R to be the boundary of an unbounded lake corresponding to the exterior face
of G. The shortest paths in R will be polygonal paths with corners at convex corners of the
lakes. Outside the circles Dv, the paths along which the man will run are exactly the paths
in G. Inside a circle Dv, we need to take special care to ensure that the man can always run
along an optimal path.
We now explain the construction of the lakes Lf corresponding to faces f of G. Consider
a vertex v of G and the faces f, g, h on which v is a vertex. We ﬁrst describe how the
boundaries of Lf , Lg, Lh look in the circle Dv of radius 1/16 centered at v. See Figure 4.
Let a, b, c be the points where the edges incident to v enter Dv. Suppose that the arc on Dv
from a to b is in the face f , the arc from b to c is in g, and the arc from c to a is in h. We
now create three polygonal curves Pvf , Pvg, Pvh inside Dv so that the shortest path between
any two of a, b, c contained in Dv and not crossing any of Pvf , Pvg, Pvh has length 1/8. The
curve Pvf starts at a point rvf on Dv and ends at a point svf on Dv, and the endpoints
rvf , svf are inside f , and similarly for the faces g, h. These properties are easy to obtain by
a construction as shown in Figure 4. The curves Pvf , Pvg, Pvh will be part of the boundary
of the lakes Lf , Lg, Lh, respectively.
 S o C G 2 0 1 7

6:8 Best Laid Plans of Lions and Men

We now explain how to construct the rest of the boundary of each lake Lf . Consider a
face f of G and assume that the vertices on f are uvxyz in that order on f . The curves
Puf , Pvf , Pxf , Pyf , Pzf appear on the boundary of Lf in that order. In the following, we
describe how to connect the end suf of Puf with the start rvf of Pvf – the other curves are
connected in a completely analogous way. See Figure 5. Let euv be the edge of G between
u and v, thus, euv is a polygonal curve. Let a corner of euv be a common point of two
neighbouring segments of euv. We make a polygonal curve Quv corresponding to euv. Quv
starts at suf and ends at rvf so that it connects Puf and Pvf . Quv stays near euv inside f
and touches euv at the corners of euv which are convex corners of f . To summarize, Quv has
the following properties:
1. Quv starts at suf and ends at rvf ,
2. Quv is completely contained in f ,
3. Quv is, except for the endpoints suf , rvf , outside the circles Du and Dv,
4. Quv and Qu′v′ are completely disjoint for any ordered pair (u
′v′) ̸= (u, v) so that {u
′, v′}
is an edge of G, and
5. Quv touches euv at a point p if and only if p is a corner of euv which is a convex corner
of f .

Observe that Qvu (note: not Quv!) touches euv at the corners which are concave corners
of f , since those are convex corners of the neighbouring face on the other side of euv.

▶ Theorem 6. There exists a polygonal region R in the plane with holes where the exterior
and interior boundaries are all pairwise disjoint and such that the man has a winning strategy
against two lions.

Proof. R is the region that we get by removing from R2 the interior of each of the lakes Lf .
Thus, the boundary of each lake is included in R, so that R is a closed set. R is also bounded
because we remove the interior of the unbounded lake corresponding to the exterior face of G.
Note that any point on an edge euv of G which is outside the circles Du and Dv is a point
in R. Since the quarters of euv are outside the circles Du and Dv, it follows that they are
also points in R. Furthermore, our construction ensures that the distance in R between any
two quarters is the same as in G. Let G′ be the points in R which are on some shortest path
between two quarters in R. Thus, G′ are the points that the man can possibly visit when
running along shortest paths in R from quarter to quarter.
Let l1 and l2 be two lions in R. We deﬁne projections l′
1 and l′
2 of the lions l1 and l2 to
be the closest points in G′ (with respect to distances in R). We now deﬁne l′′
1 and l′′
2 to be
projections of l′
1 and l′
2 in G in the following way. Outside the circles Dv, G and G′ coincide,
and here we simply deﬁne l′′
i := l′
i. Suppose now that l′
i is inside a circle Dv for some vertex
v of G. See Figure 6. Suppose that the three edges incident to v enter Dv at the points a, b, c.
The projection l′
i is a point on one of the shortest paths between a pair of the points a, b, c.
Recall that these shortest paths all have length 1/8. Assume without loss of generality that
l′
i is on the path from a to c. Let d be the distance from a to l′
i in R, so that 0 ≤ d ≤ 1/8. If
d = 1/16, we deﬁne l′′
i := v. Otherwise, if d < 1/16, we let l′′
i be the point on the segment
av in G with distance d to a, i.e., l′′
i ∈ av so that ∥al′′
i ∥ = d. Similarly, if d > 1/16, we let l′′
i
be the point on bv with distance 1/8 − d to b.
We now prove that l′′
i moves with at most unit speed in G. It will then follow from
Lemma 2 that the man has a winning strategy.
G′ subdivides R into some regions R′
1, . . . , R′
k, which are the connected components of
R \ G′. Let Ri = R′
i be the closure of R′
i. Now, R = ⋃k
i=1 Ri. Inside each circle Dv, there is
a triangular region bounded by three segments from G′. All other regions are bounded by

M. Abrahamsen, J. Holm, E. Rotenberg, and C. Wulﬀ-Nilsen 6:9

Figure 6 The projection of the lion’s position li onto the point l′
i of G′ (left), and the projection
of l′
i onto the point l′′
i of G (right). The dashed lines illustrate G′, and the solid lines illustrate G. In
the left ﬁgure, l′
i is the closest point on G′ to li. In the right ﬁgure, the length of the segment cl′′
i
equals the length of the dashed path from c to l′
i.

a polygonal curve C ⊂ ∂Lf on the boundary of some lake Lf and a concave chain H ⊂ G′.
Call such a region normal. If the lion li is in a normal region Rj with boundary ∂Rj = C ∪ H
as described before, the projection l′
i is on H. It then follows from the concavity of H that l′
i,
and thus also l′′
i , moves continuously and with at most unit speed.
However, when li is inside a triangular region in Dv, the projection l′
i might jump from
one segment of the triangle to another. Suppose that the three edges incident to v enter Dv
at the points a, b, c as in Figure 6. Let a′ be the point where the shortest paths from a to b
and c separate and deﬁne b
′ and c′ similarly. Thus, the points a
′b′c
′ are the corners of the
triangular region. Suppose that l′
i jumps from a
′b′ to a
′c
′. Then, the distance from li to
a
′b′ and a′c
′ is the same and the distance from a to l′
i before and after the jump is at most
1/16, since otherwise, li would be closer to the segment b′c
′ than to a
′b′ and a
′c
′. It follows
that l′
i jumps from one point to another which have the same projection l′′
i . Thus, l′′
i moves
continuously and with at most unit speed.
The man now employs the strategy from Lemma 2 in the following way. He imagines
that he is playing in the dodecahedron G against the lions l′′
1 and l′′
2 . Assume therefore that
Invariant 1 holds initially. The strategy tells the man to which neighbouring quarter to run.
That quarter also exists in G′, and has the same distance, so the man runs to that quarter in
G′. Since l′′
1 and l′′
2 run with at most unit speed, the man can escape them forever. When
the man is outside the circles Dv, it is a necessary condition for the lions to catch the man
that l′′
1 or l′′
2 coincide with the man, so we conclude that they cannot catch him outside the
circles. When the man is inside a circle Dv, we know from Lemma 2 that l′′
1 and l′′
2 are at
least 1 away from the man. Therefore, l1 and l2 must be outside Dv, and hence they cannot
catch him in that case either. Thus, the man survives forever in R. ◀

3 The Fast Man Surviving any Number of Lions in the Plane

Finally, we consider the case where the man is just slightly faster than the lions in the
unbounded plane without obstacles. In this case, the man is able to escape arbitrarily many
lions. The full proofs of some of the claims below can be found in [1].

▶ Theorem 7. In the plane R2, for any ε > 0, a man able to run at speed 1 + ε has a locally
ﬁnite strategy to escape the convex hull of any number n ∈ N of unit-speed lions, provided
 S o C G 2 0 1 7

6:10 Best Laid Plans of Lions and Men

that the man does not start at the same point as a lion. Thus, the man has a locally ﬁnite
winning strategy.

In fact, we prove that the man is able to keep some minimum distance dε,n to any lion, where
dε,n only depends on ε, n, and the initial distances to the lions. Thus, if the n lions and man
were disks with radius < 1
2 dε,n, the man is still able to escape.
We proceed by induction on the number n of lions. We deﬁne strategies Mj for the man
to keep distance cj to the ﬁrst j lions. The j’th strategy yields a curve consisting of line
segments all of the same length.
Inductively, the man can keep a safety distance cn−1 to the n − 1 ﬁrst lions by running
at speed 1 + εn−1, where ε1 < ε2 < . . . < εn < ε. The bends of the curve deﬁned by strategy
Mn−1 are milestones that he runs towards when avoiding n lions. If the n’th lion ℓn is in the
way, the man makes an avoidance move, keeping a much smaller safety distance cn to ℓn and
running slightly faster at speed εn (see Figure 9). Intuitively, when performing avoidance
moves, the man runs counter-clockwise around a ﬁxed-diameter circle centered at the lion.
After a limited number of avoidance moves, the man can make an escape move, where he
simply runs towards the milestone deﬁned by the strategy Mn−1.
By choosing cn suﬃciently small, we can make sure that the detour caused by the n’th
lion is so small that it can only annoy the man once for each of the segments of the strategy
Mn−1, and thus that he is ensured to have distance at least ci−1/2 to the position deﬁned
by Mn−1 and hence not in danger of the (n − 1)’st lions.

▶ Theorem 8. A man able to run at speed 1 + ε for any ε > 0 has a locally ﬁnite strategy to
escape the convex hull of any number n ∈ N of unit-speed lions, provided that the man does
not start at the same point as a lion. Thus, the man has a locally ﬁnite winning strategy.

Proof. We assume without loss of generality that ε < 1. Let l1, . . . , ln be n arbitrary lion
paths and let the man start at position m0 such that m0 ̸= li(0) for all i. We show that the
man has a strategy Mn with the following properties:
1. The man is always running at speed 1 + εn, where εn := (1 − 2−n) · ε.
2. The path deﬁned by Mn(l1, . . . , ln) is a polygonal path with corners m0m1 . . . and each
segment mimi+1 has the same length ∆n · (1 + εn). Thus, the time it takes the man to
run from mi to mi+1 is ∆n.
3. Let ti := i · ∆n be the time where the man leaves mi in order to run to mi+1. The point
mi+1 can be determined from the positions of the lions at time ti.
4. There exists a safety distance cn > 0 such that for any i = 1, . . ., any t ∈ [ti, ti+1], and
any point x ∈ mimi+1, it holds that dist(x, {l1(t), . . . , ln(t)}) ≥ cn.
5. There is a corner mi = Mn(ti) such that for all t ≥ ti,

Mn(l1, . . . , ln)(t) /∈ CH{l1(t), . . . , ln(t)}.

Clearly, it follows from the properties that Mn is a winning strategy for the man fulﬁlling
the requirements in the theorem. We prove the statement by induction on n. If there is only
one lion, the man will run on the same ray all the time with constant speed 1 + ε1 = 1 + ε/2.
The man chooses the direction of the ray to be m0 − l1(0). This strategy obviously satisﬁes
the stated properties. Assume now that a strategy Mn−1 with the stated properties exists
for n − 1 ≥ 1 lions and consider a situation with n lions running along paths l1, . . . , ln.
Assume without loss of generality that the lions are numbered according to their (increas-
ing) distance to the man at time 0, i.e., ∥m0l1(0)∥ ≤ ∥m0l2(0)∥ ≤ · · · ≤ ∥m0ln(0)∥. For any
i ∈ {1, . . . , n}, let Mi be shorthand for Mi(l1, . . . , li) and m shorthand for Mn.

M. Abrahamsen, J. Holm, E. Rotenberg, and C. Wulﬀ-Nilsen 6:11

At any time t, let the succeeding corner on the strategy Mn−1 be

g(t) := Mn−1(⌊t/∆n−1 + 1⌋ · ∆n−1).

By property 3, the man can always compute the point g(t).
We ﬁrst describe the intuition behind the man’s strategy without specifying all details,
and later give a precise description. In the situation with n lions, the man attempts to run
according to the strategy for the n − 1 ﬁrst lions, i.e., the strategy Mn−1. Thus, at any time
t, the man’s goal is to run towards the point g(t). However, the lion ln might prevent him
from doing so. Compared to the case with n − 1 lions, the man has increased his speed by
1 + εn − (1 + εn−1) = 2
−nε, so he has time to take detours while still following the strategy
Mn−1 approximately.
Assume that we have deﬁned the man’s strategy up to time t. If he is close to the n’th
lion, i.e., the distance ∥m(t)ln(t)∥ is close to r, for some small constant r > 0 to be speciﬁed
later, he runs counterclockwise around the lion, maintaining approximately distance r to
the lion. He does so until he gets to a point where running directly towards g(t) will not
decrease his distance to the lion. He then escapes from the lion, running directly towards
g(t). Doing so, he can be sure that the lion cannot disturb him anymore until he reaches g(t)
or g(t) has changed.
We choose r so small that when the man is running around the lion, we are in one of the
following cases:
The lion is so close to g(t) that the man is within the safety distance cn−1 from g(t), and
thus in no danger of the lions l1, . . . , ln−1.
After running around the lion in a period of time no longer than 12πr/εn, the man
escapes by running directly towards g(t) without decreasing the distance to the lion. By
choosing r suﬃciently small, we can therefore limit the duration, and hence the length,
of the detour that the lion can force the man to run, so that the man is ensured to be
within the safety distance from the lions l1, . . . , ln−1 during the detour.

We now describe the details that make this idea work. We deﬁne

r := min { ∆n−1εn(εn − εn−1)
2 + 2εn + 18π(1 + εn) , εncn−1
4 + 4εn + 24π(1 + εn)
 } ,

ρ := 2r/εn,

θ := arccos 1
1 + εn ,

ϕ ∈ (0, π/2] so that tan θ = ρ sin ϕ
ρ cos ϕ − 2r , and

∆n > 0 so that 2 arcsin (1 + εn)∆n
2(r − ∆n) + ∆n
ρ ≤ ϕ, ∆n < r
3 + εn , and ∆n−1/∆n ∈ N.

We note that ϕ can be chosen since the function x ↦−→ ρ sin x
ρ cos x−2r is 0 for x = 0 and tends

to +∞ as ρ cos x decreases to 2r. As for ∆n, the function x ↦−→ 2 arcsin (1+εn)x
2(r−x) + x
ρ is 0 for
x = 0 and increases continuously, and hence ∆n can be chosen.
Deﬁne a point in time t to be a time of choice if t has the form ti := i∆n for i ∈ N0. At
any time of choice ti, the man chooses the point m(ti+1) at distance (1 + εn)∆n from his
current position m(ti) by the following strategy (see Figures 7–9):
A. Suppose ﬁrst that ∥m(ti)ln(ti)∥ ≥ r + ∆n(1 + εn). Then the man chooses the direction
directly towards g(ti). In the exceptional case that m(ti) = g(ti), he chooses an arbitrary
direction.
 S o C G 2 0 1 7

6:12 Best Laid Plans of Lions and Men

ln(ti)

m(ti) g(ti)m(ti+1)
 Figure 7 A free move. The
circles with centers m(ti) and
ln(tn) have radii (1+εn)∆n and
r, respectively.

ln(ti)

m(ti)

g(ti)
 b

W 0

W 1
 Figure 8 An escape move.
The man runs to b.

ln(ti)

m(ti)

g(ti)

q
 Figure 9 An avoidance
move. The man runs to q.

B. Suppose now that ∥m(ti)ln(ti)∥ < r+∆n(1+εn) and consider the case m(ti) ̸= g(ti). Let b
be the point at distance (1+εn)∆n from m(ti) in the direction towards g(ti). If there exist
two parallel lines W0 and W1 such that m(ti) ∈ W0, b ∈ W1, dist(ln(ti), W0) ≥ r − ∆n,
and dist(ln(ti), W1) ≥ dist(ln(ti), W0) + ∆n, then the man runs to b.
C. In the remaining cases, the circles C(m(ti), ∆n(1 + εn)) and C(ln(ti), r) intersect at two
points p and q such that the arc on C(ln(ti), r) from p counterclockwise to q is in the
interior of C(m(ti), ∆n(1 + εn)). The man then runs towards the point q.

A move deﬁned by case A, B, or C is called a free move, an escape move, or an avoidance
move, respectively. Let move i be the move that the man does during the interval [ti, ti+1).

▶ Claim 9. At any time of choice ti, it holds that

∥m(ti)ln(ti)∥ ≥ r − ∆n

and if the preceding move was an avoidance move, it also holds that

∥m(ti)ln(ti)∥ ≤ r + ∆n.

Furthermore, at an arbitrary point in time t ∈ [ti−1, ti] and any point m
′ ∈ m([ti−1, ti]) it
holds that

0 < r − (3 + εn)∆n ≤ ∥m′ln(t)∥

and if move i − 1 is an avoidance move then additionally

∥m
′ln(t)∥ ≤ r + (3 + εn)∆n.

Proof. (Sketch) The proof is by induction on i. The induction step for the ﬁrst inequality
follows easily from the speed of the man and the speed of the lion ln and (in case of an escape
or avoidance move) from considering the distance ∥m(ti)ln(ti−1)∥. For the second inequality,
note that ∥m(ti)ln(ti−1)∥ = r. The third inequality follows by considering the combined
speed of the man and the lion ln and by observing that ∥m(ti−1)ln(ti−1)∥ ≥ r −∆n. A similar
argument using the inequality ∥m(ti−1)ln(ti−1)∥ ≤ r + ∆n shows the fourth inequality. ◀

M. Abrahamsen, J. Holm, E. Rotenberg, and C. Wulﬀ-Nilsen 6:13

ln(ti)

w 0

g

W 0
 w 4 W 4

Figure 10 The distance between two consecutive of the parallel lines W0, . . . , W4 is at least ∆n,
which proves that the man runs from m(ti) = w0 to w4 unless g moves in the meantime.

▶ Claim 10. An avoidance move is succeeded by an avoidance move or an escape move.
When the man does an escape move, he will not do an avoidance move before he reaches g(t)
or g(t) moves.

Proof. Consider move i. We know from Claim 9 that if move i − 1 was an avoidance move,
then ∥m(ti)ln(ti)∥ ≤ r + ∆n < r + (1 + εn)∆n, so move i cannot be a free move.
For the second part of the statement, assume that move i is an escape move. Let
g := g(ti). Let w0, . . . , wk be a sequence of points on the ray from m(ti) with direction
to g such that w0 = m(ti), ∥w0wj∥ = j(1 + εn)∆n, and k is minimum such that either
g ∈ wk−1wk or g(t′) ̸= g for some t′ ∈ [ti+k−1, ti+k]. See Figure 10. Let W0 and W1 be the
parallel lines deﬁned in case B for move i. We deﬁne lines Wj for j ≥ 2 to be parallel to
W0 and passing through wj. We claim that for any j ∈ {0, . . . , k − 1}, the man moves from
wj to wj+1 during move i + j using either an escape move or a free move. We prove this
by induction on j. It holds for j = 0 by assumption, so assume it holds that m(ti+j) = wj
and that move i + j − 1 was an escape move or a free move. Since the distance between
consecutive lines Wj and Wj+1 is at least ∆n, it follows that dist(ln(ti), Wj) ≥ r + (j − 1)∆n
and hence that dist(ln(ti+j), Wj) ≥ r − ∆n. Now, if ∥m(ti+j)ln(ti+j)∥ < r + ∆n(1 + εn),
then the lines Wj and Wj+1 are a witness that move i + j is an escape move so that the man
moves to wj+1. Otherwise, move i + j is a free move, in which case the man moves to wj+1.
Finally, since g(t) moves or the man reaches g during move i + k, the statement holds. ◀

Deﬁne ρ′ := ρ + r + (3 + εn)∆n and τ := 6πr/εn.

▶ Claim 11. If move i is an avoidance move, one of the following events occurs before τ
time has passed: (i) g(t) moves, (ii) ∥m(t)g(t)∥ < ρ
′, or (iii) the man makes an escape move.

Proof Sketch. If the ﬁrst two events do not occur, it follows from Claim 10 that the man
keeps doing avoidance moves during this time. Let ξ(t) resp. η(t) denote the angle of the
vector −−−−−−→
ln(t)m(t) resp. −−−−−−→
ln(t)g(ti). A key observation is that if the diﬀerence in these angles
is small, the man makes an escape move since then the lion and the goal g are roughly on
opposite sides of the man. Showing that this diﬀerence eventually becomes small involves
showing that η increases by at least 2π more than ξ after τ time so that at some point in
time t ∈ [ti, ti + τ ], vectors −−−−−−→
ln(t)m(t) and −−−−−−→
ln(t)g(ti) have the same orientation. By Claim 9,
 S o C G 2 0 1 7

6:14 Best Laid Plans of Lions and Men

the lion ln never gets closer than ρ to g(ti) which implies that the change in η is small in
any time interval [tj, tj+1]. Since the man keeps a minimum distance to the lion, it similarly
follows that the change in ξ is small in [tj, tj+1]. Picking j to be the maximum such that
tj ≤ t gives t − tj ≤ ∆n which implies that the diﬀerence in the two angles is small at time
tj at which point the man makes an escape move. Since tj ≤ t + τ , the lemma follows. ◀

For i ∈ N0, deﬁne the canonical interval Ii as Ii := [i∆n−1, (i + 1)∆n−1), i.e., Ii is
the interval of time where the man would run from the i’th to the (i + 1)’st corner on the
polygonal line deﬁned by the strategy Mn−1. We say that Ii ends at time t = (i + 1)∆n−1.
Note that if t ∈ Ii, then g(t) = Mn−1((i + 1)∆n−1) and g(t) moves when Ii ends.
As a consequence of Claim 10 and Claim 11, we get the following.

▶ Claim 12. If t ∈ Ii and ∥m(t)g(t)∥ ≤ ρ′, then for every t′ > t, t
′ ∈ Ii, we have

∥m(t
′)g(t)∥ ≤ ρ′ + (1 + εn)τ.

▶ Claim 13. For any i ∈ N0 and at any time during the canonical interval Ii, the man is
at distance at most ρ′ + 2(1 + εn)τ away from the segment Mn−1(Ii) and when Ii ends, the
man is within distance ρ′ + (1 + εn)τ from the endpoint Mn−1((i + 1)∆n−1) of the segment.

Proof. We prove the claim by induction on i. To easily handle the base-case, we introduce
an auxiliary canonical interval I−1 = [−∆n−1, 0) and assume that the lions and the man are
standing at their initial positions during all of I−1. The statement clearly holds for i = −1.
Assume inductively that the statement holds for Ii−1 and consider the interval Ii. Let
g := Mn−1((i + 1)∆n−1). The additional distance that the man runs during Ii when his
speed is 1 + εn as compared to the speed 1 + εn−1 is ∆n−1(εn − εn−1). It follows from the
deﬁnition of r that

∆n−1(εn − εn−1) ≥ ρ + 2r + 3(1 + εn)τ > ρ
′ + 3(1 + εn)τ.

By the induction hypothesis, the man is within a distance of ρ′ + (1 + εn)τ from
Mn−1(i∆n−1) at time i∆n−1. Thus, his distance to g at the beginning of interval Ii is at
most ∆n−1(1 + εn−1) + ρ
′ + (1 + εn)τ , where ∆n−1(1 + εn−1) is the length of the interval
Mn−1(Ii). If the man does not do any avoidance moves during Ii, he runs straight to g, so it
follows that he reaches g at time (i + 1)∆n−1 − 2τ at the latest. Therefore, the statement is
clearly true in this case.
Otherwise, let t ∈ Ii be the ﬁrst time of choice at which he does an avoidance move
during Ii. If he is at distance at most ρ
′ from g at time t, the statement follows from
Claim 12. Therefore, assume that the distance is more than ρ′. Then, we must have that
t < (i + 1)∆n−1 − 2τ , since, if t was larger, he would already have reached g by the above
discussion. Hence, Claim 11 gives that at some time t
′ ≤ t + τ , either
1. the man gets within a distance of ρ′ from g, or
2. he does an escape move.

We ﬁrst prove that in the interval [t, t
′], the distance from the man to the segment
Mn−1(Ii) is at most ρ′ + 2(1 + εn)τ . To this end, note that his distance to the segment at
time t is at most ρ′ + (1 + εn)τ . Thus, since t′ ≤ t + τ , his distance at time t
′ can be at most
ρ
′ + 2(1 + εn)τ .
It remains to be proven that the man stays within distance ρ′ + 2(1 + εn)τ from Mn−1(Ii)
after time t
′ and that he is at distance at most ρ′ + (1 + εn)τ from g at time (i + 1)∆n−1. If
we are in case 1, the statement follows from Claim 12, so assume case 2.

M. Abrahamsen, J. Holm, E. Rotenberg, and C. Wulﬀ-Nilsen 6:15

By Claim 10, the man will not do an avoidance move again after time t
′ until he reaches
g or Ii ends. While he is running directly towards g, his distance to the segment Mn−1(Ii)
is decreasing, so it follows that the distance is always at most ρ
′ + 2(1 + εn)τ , as claimed.
Since he was doing avoidance moves in a period of length at most τ before the escape move
at time t′, he can completely compensate for the delay caused by the avoidance moves in the
same amount of time by running directly towards g. The total delay is therefore at most 2τ .
Since he would reach g at time (i + 1)∆n−1 − 2τ at the latest if he did not do any avoidance
moves, it follows that he reaches g at time (i + 1)∆n−1 or earlier. The statement then follows
from Claim 12. ◀

We are now ready to ﬁnish our proof of Theorem 8. Claim 13 implies that during interval
Ii for any i, the distance from the man to any of the lions l1, . . . , ln−1 is at most

ρ
′ + 2(1 + εn)τ < ρ + 2r + 2(1 + εn)τ ≤ cn−1/2.

Thus, these lions will not catch the man. By Claim 9, the distance to ln is always at least
r − (3 + εn)∆n. Therefore, we now deﬁne cn := min{cn−1/2, r − (3 + εn)∆n}, and it holds
that in the time interval I := [i∆n, (i + 1)∆n], the distance from any point on the segment
m(I) to any lion is at least cn.
Claim 13 implies that at any time t and for any i ∈ {2, . . . , n}, the distance ∥Mi−1(t)Mi(t)∥
is bounded by some constant. It follows that ∥M1(t)Mn(t)∥ ≤ dn for some constant dn > 0.
Since M1(t) traverses a ray with constant speed 1 + ε/2 > 1, the man eventually escapes
the convex hull of the lions and that the distance diverges to ∞ as t → ∞. This proves the
theorem. ◀

References

1 M. Abrahamsen, J. Holm, E. Rotenberg, and C. Wulﬀ-Nilsen. Best laid plans of lions and
men. CoRR, abs/1703.03687, 2017. URL: https://arxiv.org/abs/1703.03687.
2 Martin Aigner and Michael Fromme. A game of cops and robbers. Discrete Applied Math-
ematics, 8(1):1–12, 1984.
3 Noga Alon and Abbas Mehrabian. Chasing a fast robber on planar graphs and random
graphs. Journal of Graph Theory, 78(2):81–96, 2015.
4 Alessandro Berarducci and Benedetto Intrigila. On the cop number of a graph. Advances
in Applied Mathematics, 14(4):389–403, 1993.
5 B. Bollobás, I. Leader, and M. Walters. Lion and man – can both win? Israel Journal of
Mathematics, 189(1):267–286, 2012.
6 Béla Bollobás. The Art of Mathematics: Coﬀee Time in Memphis. Cambridge University
Press, 2006.
7 Béla Bollobás. The lion and the christian, and other pursuit and evasion games. In Dierk
Schleicher and Malte Lackmann, editors, An Invitation to Mathematics: From Competitions
to Research, pages 181–193. Springer-Verlag Berlin Heidelberg, 2011.
8 Hallard T. Croft. “Lion and man”: A postscript. Journal of the London Mathematical
Society, 39:385–390, 1964.
9 James Flynn. Lion and man: The boundary constraint. SIAM Journal on Control, 11:397–
411, 1973.
10 James Flynn. Lion and man: The general case. SIAM Journal on Control, 12:581–597,
1974.
11 Robbert Fokkink, Leonhard Geupel, and Kensaku Kikuta. Open problems on search games.
In Steve Alpern, Robbert Fokkink, Leszek Antoni Gąsieniec, Roy Lindelauf, and V. S.
 S o C G 2 0 1 7

6:16 Best Laid Plans of Lions and Men

Subrahmanian, editors, Search Theory: A Game Theoretic Perspective, chapter 5, pages
181–193. Springer-Verlag New York, 2013.
12 Fedor V. Fomin, Petr A. Golovach, Jan Kratochvíl, Nicolas Nisse, and Karol Suchan. Pur-
suing a fast robber on a graph. Theoretical Computer Science, 411:1167–1181, 2010.
13 Vladimir Janković. About a man and lions. Matematički Vesnik, 2:359–361, 1978.
14 J. Lewin. The lion and man problem revisited. Journal of Optimization Theory and
Applications, 49(3):411–430, 1986.
15 John Edensor Littlewood. Littlewood’s miscellany: edited by Béla Bollobás. Cambridge
University Press, 1986.
16 Peter A. Rado and Richard Rado. More about lions and other animals. Mathematical
Sprectrum, 7(3):89–93, 1974/75.
