<!-- source: https://ti.inf.ethz.ch/ew/Lehre/CG13/lecture/cg-2012.pdf | converted from PDF -->

Computational Geometry
Lecture Notes1 HS 2012

Bernd Gärtner <gaertner@inf.ethz.ch>
Michael Hoﬀmann <hoffmann@inf.ethz.ch>

Tuesday 15th January, 2013

1Some parts are based on material provided by Gabriel Nivasch and Emo Welzl. We also thank
Tobias Christ, Anna Gundert, and May Szedlák for pointing out errors in preceding versions.

Contents

1 Fundamentals 7
1.1 Models of Computation . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
1.2 Basic Geometric Objects . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8

2 Polygons 11
2.1 Classes of Polygons . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
2.2 Polygon Triangulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
2.3 The Art Gallery Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . 19

3 Convex Hull 23
3.1 Convexity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
3.2 Planar Convex Hull . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
3.3 Trivial algorithms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
3.4 Jarvis’ Wrap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
3.5 Graham Scan (Successive Local Repair) . . . . . . . . . . . . . . . . . . . 31
3.6 Lower Bound . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
3.7 Chan’s Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33

4 Line Sweep 37
4.1 Interval Intersections . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
4.2 Segment Intersections . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
4.3 Improvements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
4.4 Algebraic degree of geometric primitives . . . . . . . . . . . . . . . . . . . 42
4.5 Red-Blue Intersections . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45

5 Plane Graphs and the DCEL 51
5.1 The Euler Formula . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
5.2 The Doubly-Connected Edge List . . . . . . . . . . . . . . . . . . . . . . . 53
5.2.1 Manipulating a DCEL . . . . . . . . . . . . . . . . . . . . . . . . . 54
5.2.2 Graphs with Unbounded Edges . . . . . . . . . . . . . . . . . . . . 57
5.2.3 Remarks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58

3

Contents CG 2012

6 Delaunay Triangulations 61
6.1 The Empty Circle Property . . . . . . . . . . . . . . . . . . . . . . . . . . 64
6.2 The Lawson Flip algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . 66
6.3 Termination of the Lawson Flip Algorithm: The Lifting Map . . . . . . . 67
6.4 Correctness of the Lawson Flip Algorithm . . . . . . . . . . . . . . . . . . 68
6.5 The Delaunay Graph . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70
6.6 Every Delaunay Triangulation Maximizes the Smallest Angle . . . . . . . 72
6.7 Constrained Triangulations . . . . . . . . . . . . . . . . . . . . . . . . . . 75

7 Delaunay Triangulation: Incremental Construction 79
7.1 Incremental construction . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79
7.2 The History Graph . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82
7.3 The structural change . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83

8 The Conﬁguration Space Framework 85
8.1 The Delaunay triangulation — an abstract view . . . . . . . . . . . . . . . 85
8.2 Conﬁguration Spaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86
8.3 Expected structural change . . . . . . . . . . . . . . . . . . . . . . . . . . 87
8.4 Bounding location costs by conﬂict counting . . . . . . . . . . . . . . . . . 89
8.5 Expected number of conﬂicts . . . . . . . . . . . . . . . . . . . . . . . . . 90

9 Trapezoidal Maps 95
9.1 The Trapezoidal Map . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95
9.2 Applications of trapezoidal maps . . . . . . . . . . . . . . . . . . . . . . . 96
9.3 Incremental Construction of the Trapezoidal Map . . . . . . . . . . . . . . 96
9.4 Using trapezoidal maps for point location . . . . . . . . . . . . . . . . . . 98
9.5 Analysis of the incremental construction . . . . . . . . . . . . . . . . . . . 99
9.5.1 Deﬁning The Right Conﬁgurations . . . . . . . . . . . . . . . . . . 99
9.5.2 Update Cost . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
9.5.3 The History Graph . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
9.5.4 Cost of the Find step . . . . . . . . . . . . . . . . . . . . . . . . . . 104
9.5.5 Applying the General Bounds . . . . . . . . . . . . . . . . . . . . . 104
9.6 Analysis of the point location . . . . . . . . . . . . . . . . . . . . . . . . . 106
9.7 The trapezoidal map of a simple polygon . . . . . . . . . . . . . . . . . . 108

10 Voronoi Diagrams 115
10.1 Post Oﬃce Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
10.2 Voronoi Diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116
10.3 Duality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119
10.4 Lifting Map . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120
10.5 Point location in a Voronoi Diagram . . . . . . . . . . . . . . . . . . . . . 121
10.5.1 Kirkpatrick’s Hierarchy . . . . . . . . . . . . . . . . . . . . . . . . 122

4

CG 2012 Contents

11 Linear Programming 129
11.1 Linear Separability of Point Sets . . . . . . . . . . . . . . . . . . . . . . . 129
11.2 Linear Programming . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130
11.3 Minimum-area Enclosing Annulus . . . . . . . . . . . . . . . . . . . . . . 133
11.4 Solving a Linear Program . . . . . . . . . . . . . . . . . . . . . . . . . . . 135

12 A randomized Algorithm for Linear Programming 137
12.1 Helly’s Theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 138
12.2 Convexity, once more . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139
12.3 The Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 140
12.4 Runtime Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141
12.4.1 Violation Tests . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142
12.4.2 Basis Computations . . . . . . . . . . . . . . . . . . . . . . . . . . 143
12.4.3 The Overall Bound . . . . . . . . . . . . . . . . . . . . . . . . . . . 143

13 Line Arrangements 145
13.1 Arrangements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 146
13.2 Construction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 147
13.3 Zone Theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 147
13.4 The Power of Duality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 149
13.5 Sorting all Angular Sequences. . . . . . . . . . . . . . . . . . . . . . . . . 150
13.6 Segment Endpoint Visibility Graphs . . . . . . . . . . . . . . . . . . . . . 151
13.7 Ham Sandwich Theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . 153
13.8 3-Sum . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 155
13.9 3-Sum hardness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 156

14 Davenport-Schinzel Sequences 161
14.1 Davenport-Schinzel Sequences . . . . . . . . . . . . . . . . . . . . . . . . . 162

15 Epsilon Nets 167
15.1 Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 167
15.2 Range spaces and ε-nets. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 168
15.2.1 Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 168
15.2.2 No point in a large range. . . . . . . . . . . . . . . . . . . . . . . . 169
15.2.3 Smallest enclosing balls. . . . . . . . . . . . . . . . . . . . . . . . . 170
15.3 Either almost all is needed or a constant suﬃces. . . . . . . . . . . . . . . 170
15.4 What makes the diﬀerence: VC-dimension . . . . . . . . . . . . . . . . . . 171
15.4.1 The size of projections for ﬁnite VC-dimension. . . . . . . . . . . . 172
15.5 VC-dimension of Geometric Range Spaces . . . . . . . . . . . . . . . . . . 174
15.5.1 Halfspaces. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 174
15.5.2 Balls. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 175
15.6 Small ε-Nets, an Easy Warm-up Version . . . . . . . . . . . . . . . . . . . 176
15.6.1 Smallest enclosing balls, again . . . . . . . . . . . . . . . . . . . . 177

5

Contents CG 2012

15.7 Even Smaller ε-Nets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 178

6

Chapter 1

Fundamentals

1.1 Models of Computation

Real RAM Model. A memory cell stores a real number. Any single arithmetic operation
or comparison can be computed in constant time. In addition, sometimes also roots,
logarithms, other analytic functions, indirect addressing (integral), or ﬂoor and ceiling
are used.
This is a quite powerful (and somewhat unrealistic) model of computation, as a single
real number in principle can encode an arbitrary amount of information. Therefore we
have to ensure that we do not abuse the power of this model.

Algebraic Computation Trees (Ben-Or [1]). A computation is regarded as a binary tree.

≤ 0

a − b
 b − ca − c

≤ 0 ≤ 0

a c b c The leaves contain the (possible) results of the compu-
tation. Every node v with one child has an operation of the
form +, −, ∗, /, √
, . . . associated to it. The operands of
this operation are constant input values, or among the
ancestors of v in the tree. Every node v with two children has associated to it a
branching of the form > 0, ⩾ 0, or = 0. The branch
is with respect to the result of v’s parent node. If the
expression yields true, the computation continues with
the left child of v; otherwise, it continues with the right
child of v.

If every branch is based on a linear function in the input values, we face a linear
computation tree. Analogously one can deﬁne, say, quadratic computation trees. The
term decision tree is used if all of the results are either true or false.

7

Chapter 1. Fundamentals CG 2012

The complexity of a computation or decision tree is the maximum number of vertices
along any root-to-leaf path. It is well known that Ω(n log n) comparisons are required
to sort n numbers. But also for some problems that appear easier than sorting at ﬁrst
glance, the same lower bound holds. Consider, for instance, the following problem.

Element Uniqueness

Input: {x1, . . . , xn} ⊂ R, n ∈ N.

Output: Is xi = xj, for some i, j ∈ {1, . . . , n} with i ̸= j?

Ben-Or [1] has shown that any algebraic decision tree to solve Element Uniqueness
for n elements has complexity Ω(n log n).

1.2 Basic Geometric Objects

We will mostly be concerned with the d-dimensional Euclidean space R
d, for small
d ∈ N; typically, d = 2 or d = 3. The basic objects of interest in R
d are the following.

Points. A point p, typically described by its d Cartesian
coordinates p = (x1, . . . , xd). p = (−4, 0)
q = (2, −2)
 r = (7, 1)

Directions. A vector v ∈ Sd−1 (the (d − 1)-dimensional
unit sphere), typically described by its d Cartesian coor-

dinates v = (x1, . . . , xd), with ||v|| = √∑d
i=1 xi2 = 1.

Lines. A line is a one-dimensional aﬃne subspace. It can
be described by two distinct points p and q as the set of
all points r that satisfy r = p + λ(q − p), for some λ ∈ R.
 p
 q

While any pair of distinct points deﬁnes a unique line, a line in R
2 contains inﬁnitely
many points and so it may happen that a collection of three or more points lie on a line.
Such a collection of points is termed collinear 1.
Rays. If we remove a single point from a line and take
the closure of one of the connected components, then we
obtain a ray. It can be described by two distinct points p
and q as the set of all points r that satisfy r = p+λ(q−p),
for some λ ⩾ 0. The orientation of a ray is the direction
(q − p)/∥q − p∥. p
 q

1Not colinear, which refers to a notion in the theory of coalgebras.

8

CG 2012 1.2. Basic Geometric Objects

Line segment. A line segment is the intersection of two
collinear rays of opposite orientation. It can be described
by two points p and q as the set of all points r that satisfy
r = p + λ(q − p), for some λ ∈ [0, 1]. We will denote
the line segment through p and q by pq. Depending
on the context we may allow or disallow degenerate line
segments consisting of a single point only (p = q in the
above equation).
 p
 q

Hyperplanes. A hyperplane H is a (d−1)-dimensional aﬃne subspace. It can be described
algebraically by d + 1 coeﬃcients λ1, . . . , λd+1 ∈ R, where ∥(λ1, . . . , λd+1)∥ = 1, as the
set of all points (x1, . . . , xd) that satisfy the linear equation H : ∑d
i=1 λixi = λd+1.
If the above equation is converted into an inequality, we obtain the algebraic descrip-
tion of a halfspace (in R
2: halfplane).

Spheres and balls. A sphere is the set of all points that are equidistant to a ﬁxed point.
It can be described by a point c (center) and a number ρ ∈ R (radius) as the set of all
points p that satisfy ||p − c|| = ρ. The ball of radius ρ around p consists of all points p
that satisfy ||p − c|| ⩽ ρ.

References

[1] Michael Ben-Or, Lower bounds for algebraic computation trees. In Proc.
15th Annu. ACM Sympos. Theory Comput., pp. 80–86, 1983, URL
http://dx.doi.org/10.1145/800061.808735.

9

Chapter 2

Polygons

Although we can think of a line ℓ ⊂ R
2 as an inﬁnite point set that consists of all points
in R
2 that are on ℓ, there still exists a ﬁnite description for ℓ. Such a description is,
for instance, provided by the three coeﬃcients a, b, c ∈ R of an equation of the form
ax + by = c, with (a, b) ̸= (0, 0). Actually this holds true for all of the fundamental
geometric objects that were mentioned in the previous section: Each of them has constant
description complexity (or, informally, just size), that is, it can be described by a
constant1 number of parameters.
In this course we will typically deal with objects that are not of constant size. Often
these are formed by merely aggregating constant-size objects, for instance, points to
form a ﬁnite set of points. But sometimes we also demand additional structure that
goes beyond aggregation only. Probably the most fundamental geometric objects of this
type are what we call polygons. You probably learned this term in school, but what
is a polygon precisely? Consider the examples shown in Figure 2.1. Are all of these
polygons? If not, where would you draw the line?

(a) (b) (c) (d) (e) (f)

Figure 2.1: What is a polygon?

2.1 Classes of Polygons

Obviously, there is not the right answer to such a question and certainly there are
diﬀerent types of polygons. Often the term polygon is used somewhat sloppily in place

1Unless speciﬁed diﬀerently, we will always assume that the dimension is (a small) constant. In a
high-dimensional space Rd, one has to account for a description complexity of Θ(d).

11

Chapter 2. Polygons CG 2012

of what we call a simple polygon, deﬁned below.

Deﬁnition 2.1 A simple polygon is a compact region P ⊂ R
2 that is bounded by a simple
closed curve γ : [0, 1] → R
2 that consists of a ﬁnite number of line segments. A
curve is a continuous map γ : [0, 1] → R
2. A curve γ is closed, if γ(0) = γ(1) and it
is simple if it is injective on [0, 1), that is, the curve does not intersect itself.

Out of the examples shown above only Polygon 2.1a is simple. For each of the remaining
polygons it is impossible to combine the bounding segments into a simple closed curve.
The term compact for subsets of R
d means bounded and closed. A subset of P ⊂ R
d

is bounded, if it is contained in the ball of radius r around the origin, for some ﬁnite
r > 0. Being closed means that the boundary is considered to be part of the polygon.
In order to formally deﬁne these terms, let us brieﬂy review a few basic notions from
topology.
The standard topology of R
d is deﬁned in terms of the Euclidean metric. A point
p ∈ R
d is interior to a set P ⊆ R
d, if there exists an ε-ball Bε(p) = {x ∈ R
d : ||x−p|| < ε}
around p, for some ε > 0, that is completely contained in P. A set is open, if all of its
points are interior; and it is closed, if its complement is open.

Exercise 2.2 Determine for each of the following sets whether they are open or closed
in R
2. a) B1(0) b) {(1, 0)} c) R
2 d) R
2 \Z
2 e) R
2 \Q2 f ) {(x, y) : x ∈ R, y ⩾ 0}

Exercise 2.3 Show that the union of countably many open sets in R
d is open. Show
that the union of a ﬁnite number of closed sets in R
d is closed. (These are two of
the axioms that deﬁne a topology. So the statements are needed to assert that the
metric topology is a topology, indeed.) What follows for intersections of open and
closed sets? Finally, show that the union of countably many closed sets in R
d is
not necessarily closed.

The boundary ∂P of a set P ⊂ R
d consists of all points that are neither interior to P
nor to its complement R
d \ P. By deﬁnition, for every p ∈ ∂P every ball Bε(p) contains
both points from P and from R
d \ P. Sometimes one wants to consider a set P ⊂ R
d open
although it is not. In that case one can resort to the interior P◦ of P that is formed by
the subset of points interior to P. Similarly, the closure P of P is deﬁned by P = P ∪ ∂P.
Lower-dimensional objects, such as line segments in R
2 or triangles in R
3, do not
possess any interior point (because the ε-balls needed around any such point are full-
dimensional). Whenever we want to talk about the interior of a lower-dimensional object,
we use the qualiﬁer relative and consider it relative to the smallest aﬃne subspace that
contains the object.
For instance, the smallest aﬃne subspace that contains a line segment is a line and
so the relative interior of a line segment in R
2 consists of all points except the endpoints,
just like for an interval in R
1. Similarly, for a triangle in R
3 the smallest aﬃne subspace
that contains it is a plane. Hence its relative interior is just the interior of the triangle,
considered as a two-dimensional object.
 12

CG 2012 2.1. Classes of Polygons

Exercise 2.4 Show that for any P ⊂ R
d the interior P◦ is open. (Why is there some-
thing to show to begin with?) Show that for any P ⊂ R
d the closure P is closed.

When describing a simple polygon P it is suﬃcient to describe only its boundary
∂P. As ∂P by deﬁnition is a simple closed curve γ that consists of ﬁnitely many line
segments, we can eﬃciently describe it as a sequence p1, . . . , pn of points, such that γ
is formed by the line segments p1p2, p2p3, . . . , pn−1pn, pnp1. These points are referred
to as the vertices of the polygon, and the segments connecting them are referred as the
edges of the polygon.
Knowing the boundary, it is easy to tell apart the (bounded) interior from the (un-
bounded) exterior. This is asserted even for much more general curves by the well-known
Jordan-Curve Theorem.

Theorem 2.5 (Jordan 1887) Any simple closed curve γ : [0, 1] → R
2 divides the plane
into exactly two connected components whose common boundary is formed by γ.

In full generality, the proof of the deceptively obvious claim is surprisingly diﬃcult. We
will not prove it here, the interested reader can ﬁnd a proof, for instance, in the book
of Mohar and Thomassen [11]. There exist diﬀerent generalizations of the theorem and
there also has been some debate about to which degree the original proof of Jordan is
actually correct. For simple polygons the situation is easier, though. The essential idea
can be worked out algorithmically, which we leave as an exercise.

Exercise 2.6 Describe an algorithm to decide whether a point lies inside or outside
of a simple polygon. More precisely, given a simple polygon P ⊂ R
2 as a list of its
vertices (v1, v2, . . . , vn) in counterclockwise order and a query point q ∈ R
2, decide
whether q is inside P, on the boundary of P, or outside. The runtime of your
algorithm should be O(n).

There are good reasons to ask for the boundary of a polygon to form a simple curve:
For instance, in the example depicted in Figure 2.1b there are several regions for which it
is completely unclear whether they should belong to the interior or to the exterior of the
polygon. A similar problem arises for the interior regions in Figure 2.1f. But there are
more general classes of polygons that some of the remaining examples fall into. We will
discuss two such classes here. The ﬁrst comprises polygons like the one from Figure 2.1d.

Deﬁnition 2.7 A region P ⊂ R
2 is a simple polygon with holes if it can be described as
P = F \ ⋃
H∈H H
◦, where H is a ﬁnite collection of pairwise disjoint simple polygons
(called holes) and F is a simple polygon for which F◦ ⊃ ⋃
H∈H H.

The way this deﬁnition heavily depends on the notion of simple polygons makes it
straightforward to derive a similar trichotomy as the Jordan Curve Theorem provides
for simple polygons, that is, every point in the plane is either inside, or on the boundary,
or outside of P (exactly one of these three).

13

Chapter 2. Polygons CG 2012

The second class describes polygons that are “almost-simple” in the sense that they
are arbitrarily close to a simple polygon. In many algorithmic scenarios such polygons
can be treated very similarly to simple polygons.

Deﬁnition 2.8 A weakly simple polygon is a bounded region P ⊂ R
2 such that

1. P is connected, ∂P is connected, and P is simply-connected;

2. ∂P consists of a ﬁnite number of line segments, no two of which intersect
except at a common endpoint; and

3. there exists a k ∈ N such that for every ε > 0 there exists a simple polygon Qε
on at most k vertices for which the symmetric diﬀerence (Qε ∪ P) \ (Qε ∩ P)
has area less than ε.

It remains to deﬁne the terms connected and simply-connected. A set P ⊆ R
d is
connected 2 if for every pair p, q ∈ P there is a curve within P that connects p and
q. A set P ⊆ R
d is simply-connected if it is connected and if for every simple closed
curve γ : [0, 1] → P the bounded region enclosed by γ (well-deﬁned by Theorem 2.5)
is completely contained in P. For instance, the simple polygon with one hole depicted
in Figure 2.2a is not simply-connected, because the red curve around the hole encloses
points that do not belong to the polygon. The polygon P shown in Figure 2.2b is not
simple but weakly simple; the simple polygon shown in orange provides a pretty good
approximation that can be made arbitrarily close (but soon would be indistinguishable
from P).
 (a) (b)

Figure 2.2: Weakly simple or not?

Exercise 2.9 Which of the shapes depicted in Figure 2.1 are weakly simple polygons?

Exercise 2.10 Show that the class of weakly simple polygons would change if we de-
manded a weakly simple polygon to be closed. Would it change the deﬁnition if we
asked for a weakly simple polygon to be open?

2In general, a topological space is connected if it cannot be described as a disjoint union of open subsets.
The property deﬁned here is called path-connected. But as for Rd both notions are equivalent, we stick
to the more intuitive and geometric one.
 14

CG 2012 2.2. Polygon Triangulation

Exercise 2.11 Show that in Deﬁnition 2.8 the condition that the closure is simply-
connected is necessary in the following sense: If dropped then there exist two “weakly
simple” polygons that have the same boundary but diﬀerent interior.

2.2 Polygon Triangulation

From a topological point of view, a simple polygon is nothing but a disk and so it is a very
elementary object. But geometrically a simple polygon can be—as if mocking the label
we attached to it—a pretty complicated shape, see Figure 2.3 for an example. While
there is an easy and compact one-dimensional representation in terms of the boundary,
as a sequence of vertices/points, it is often desirable to work with a more structured
representation of the whole two-dimensional shape.

Figure 2.3: A simple (?) polygon.

For instance, it is not straightforward to compute the area of a general simple polygon.
In order to do so, one usually describes the polygon in terms of simpler geometric objects,
for which computing the area is easy. Good candidates for such shapes are triangles,
rectangles, and trapezoids. Indeed, it is not hard to show that every simple polygon
admits a “nice” partition into triangles, which we call a triangulation.

Deﬁnition 2.12 A triangulation of a simple polygon P is a collection T of triangles, such
that

(1) P = ⋃
T ∈T T ;

(2) the vertices of all triangles in T are also vertices of P; and

(3) for every distinct pair T , U ∈ T, the intersection T ∩ U is either a common
vertex, or a common edge, or empty.

If we are given a triangulation of a simple polygon P it is easy to compute the area of P
by simply summing up the area of all triangles from T. Triangulations are an incredibly
useful tool in planar geometry, and one reason for their importance is that every simple
polygon admits one.

Theorem 2.13 Every simple polygon has a triangulation.

15

Chapter 2. Polygons CG 2012

Proof. Let P be a simple polygon on n vertices. We prove the statement by induction on
n. For n = 3 we face a triangle P that is a triangulation by itself. For n > 3 consider the
lexicographically smallest vertex v of P, that is, among all vertices of P with a smallest x-
coordinate the one with smallest y-coordinate. Denote the neighbors of v (next vertices)
along ∂P by u and w. Consider the line segment uw. We distinguish two cases.
Case 1: except for its endpoints u and w, the segment uw lies completely in P◦.
Then uw splits P into two smaller polygons, the triangle uvw and a simple polygon P ′

on n − 1 vertices (Figure 2.4a). By the inductive hypothesis, P ′ has a triangulation that
together with T yields a triangulation of P.

v

u
 w
(a) Case 1.
 v

u
 w

p

(b) Case 2.

Figure 2.4: Cases in the proof of Theorem 2.13.

Case 2: the relative interior of uw does not lie completely in P◦ (Figure 2.4b). By
choice of v, the polygon P is contained in the closed halfplane to the right of the vertical
line through v. Therefore, as the segments uv and vw are part of a simple closed curve
deﬁning ∂P, every point suﬃciently close to v and between the rays vu and vw must be
in P◦.
On the other hand, since uw ̸⊂ P◦, there is some point from ∂P in the interior of
the triangle T = uvw (by the choice of v the points u, v, w are not collinear and so T is
a triangle, indeed) or on the line segment uw. In particular, as ∂P is composed of line
segments, there is a vertex of P in T ◦ or on uw (otherwise, a line segment would have
to intersect the line segment uw twice, which is impossible). Let p denote a leftmost
such vertex. Then the open line segment vp is contained in T ◦ and, thus, it splits P into
two polygons P1 and P2 on less than n vertices each (in one of them, u does not appear
as a vertex, whereas w does not appear as a vertex in the other). By the inductive
hypothesis, both P1 and P2 have triangulations and their union yields a triangulation of
P. 
The conﬁguration from Case 1 above is called an ear : Three consecutive vertices u, v, w
of a simple polygon P such that the relative interior of uw lies in P◦. In fact, we could
have skipped the analysis for Case 2 by referring to the following theorem.

Theorem 2.14 (Meisters [9, 10]) Every simple polygon that is not a triangle has two
non-overlapping ears, that is, two ears A and B such that A◦ ∩ B
◦ = ∅.

16

CG 2012 2.2. Polygon Triangulation

But knowing Theorem 2.13 we can obtain Theorem 2.14 as a direct consequence of the
following

Theorem 2.15 Every triangulation of a simple polygon on n ⩾ 4 vertices contains at
least two (triangles that are) ears.

Exercise 2.16 Prove Theorem 2.15.

Exercise 2.17 Let P be a simple polygon with vertices v1, v2, . . . , vn (in counterclock-
wise order), where vi has coordinates (xi, yi). Show that the area of P is

1
2
 n∑

i=1 xi+1yi − xiyi+1,

where (xn+1, yn+1) = (x1, y1).

The number of edges and triangles in a triangulation of a simple polygon are completely
determined by the number of vertices, as the following simple lemma shows.

Lemma 2.18 Every triangulation of a simple polygon on n ⩾ 3 vertices consists of
n − 2 triangles and 2n − 3 edges.

Proof. Proof by induction on n. The statement is true for n = 3. For n > 3 consider
a simple polygon P on n vertices and an arbitrary triangulation T of P. Any edge uv in
T that is not an edge of P (and there must be such an edge because P is not a triangle)
partitions P into two polygons P1 and P2 with n1 and n2 vertices, respectively. Since
n1, n2 < n we conclude by the inductive hypothesis that T partitions P1 into n1 − 2
triangles and P2 into n2 − 2 triangles, using 2n1 − 3 and 2n2 − 3 edges, respectively.
All vertices of P appear in exactly one of P1 or P2, except for u and v, which appear in
both. Therefore n1 +n2 = n+2 and so the number of triangles in T is (n1 −2)+(n2−2) =
(n1 + n2) − 4 = n + 2 − 4 = n − 2. Similarly, all edges of T appear in exactly one of P1
or P2, except for the edge uv, which appears in both. Therefore the number of edges in
T is (2n1 − 3) + (2n2 − 3) − 1 = 2(n1 + n2) − 7 = 2(n + 2) − 7 = 2n − 3. 
The universal presence of triangulations is something particular about the plane: The
natural generalization of Theorem 2.13 to dimension three and higher does not hold.
What is this generalization, anyway?

Tetrahedralizations in R
3. A simple polygon is a planar object that is a topological disk
that is locally bounded by patches of lines. The corresponding term in R
3 is a polyhedron,
and although we will not formally deﬁne it here yet, a literal translation of the previous
sentence yields an object that topologically is a ball and is locally bounded by patches
of planes. A triangle in R
2 corresponds to a tetrahedron in R
3 and a tetrahedralization
is a nice partition into tetrahedra, where “nice” means that the union of the tetrahedra
covers the object, the vertices of the tetrahedra are vertices of the polyhedron, and any

17

Chapter 2. Polygons CG 2012

two distinct tetrahedra intersect in either a common triangular face, or a common edge,
or a common vertex, or not at all.3

Unfortunately, there are polyhedra in R
3 that do not admit a tetrahedralization. The
following construction is due to Schönhardt [12]. It is based on a triangular prism, that
is, two congruent triangles placed in parallel planes where the corresponding sides of both
triangles are connected by a rectangle (Figure 2.5a). Then one triangle is twisted/rotated
slightly within its plane. As a consequence, the rectangular faces are not plane anymore,
but they obtain an inward dent along their diagonal in direction of the rotation (Fig-
ure 2.5b). The other (former) diagonals of the rectangular faces—labeled ab ′, bc ′, and

(a)
 a
 b

c

a ′ c ′

b ′

(b)

Figure 2.5: The Schönhardt polyhedron cannot be subdivided into tetrahedra without
adding new vertices.

ca ′ in Figure 2.5b—are now epigonals, that is, they lie in the exterior of the polyhe-
dron. Since these epigonals are the only edges between vertices that are not part of
the polyhedron, there is no way to add edges to form a tetrahedron for a subdivision.
Clearly the polyhedron is not a tetrahedron by itself, and so we conclude that it does
not admit a subdivision into tetrahedra without adding new vertices. If adding new
vertices—so-called Steiner vertices—is allowed, then there is no problem to construct a
tetrahedralization, and this holds true in general.

Algorithms. Knowing that a triangulation exists is nice, but it is much better to know
that it can also be constructed eﬃciently.

Exercise 2.19 Convert Theorem 2.13 into an O(n
2) time algorithm to construct a
triangulation for a given simple polygon on n vertices.

The runtime achieved by the straightforward application of Theorem 2.13 is not optimal.
We will revisit this question at several times during this course and discuss improved
algorithms for the problem of triangulating a simple polygon.

3These “nice” subdivisions can be deﬁned in an abstract combinatorial setting, where they are called
simplicial complices.
 18

CG 2012 2.3. The Art Gallery Problem

The best (in terms of worst-case runtime) algorithm known due to Chazelle [4] com-
putes a triangulation in linear time. But this algorithm is very complicated and we will
not discuss it here. There is also a somewhat simpler randomized algorithm to compute
a triangulation in expected linear time [2], which we will not discuss in detail, either.
Instead you will later see a much simpler algorithm with a pretty-close-to linear runtime
bound. The question of whether there exists a simple (which is not really a well-deﬁned
term, of course, except that Chazelle’s Algorithm does not qualify) deterministic linear
time algorithm to triangulate a simple polygon remains open [7].

Polygons with holes. It is interesting to note that the complexity of the problem changes
to Θ(n log n), if the polygon may contain holes [3]. This means that there is an algorithm
to construct a triangulation for a given simple polygon with holes on a total of n vertices
(counting both the vertices on the outer boundary and those of holes) in O(n log n)
time. But there is also a lower bound of Ω(n log n) operations that holds in all models
of computation in which there exists the corresponding lower bound for comparison-
based sorting. This diﬀerence in complexity is a very common pattern: There are many
problems that are (sometimes much) harder for simple polygons with holes than for
simple polygons. So maybe the term “simple” has some justiﬁcation, after all. . .

Genaral triangle covers. What if we drop the “niceness” conditions required for triangu-
lations and just want to describe a given simple polygon as a union of triangles? It
turns out this is a rather drastic change and, for instance, it is unlikely that we can
eﬃciently ﬁnd an optimal/minimal description of this type: Christ has shown [5] that it
is NP-hard to decide whether for a simple polygon P on n vertices and a positive integer
k, there exists a set of at most k triangles whose union is P. In fact, the problem is not
even known to be in NP, because it is not clear whether the coordinates of solutions can
always be encoded compactly.

2.3 The Art Gallery Problem

In 1973 Victor Klee posed the following question: “How many guards are necessary, and
how many are suﬃcient to patrol the paintings and works of art in an art gallery with n
walls?” From a geometric point of view, we may think of an “art gallery with n walls” as
a simple polygon bounded by n edges, that is, a simple polygon P with n vertices. And
a guard can be modeled as a point where we imagine the guard to stand and observe
everything that is in sight. In sight, ﬁnally, refers to the walls of the gallery (edges of
the polygon) that are opaque and, thus, prevent a guard to see what is behind. In other
words, a guard (point) g can watch over every point p ∈ P, for which the line segment
gp lies completely in P◦, see Figure 2.6.
It is not hard to see that ⌊n/3⌋ guards are necessary in general.

19

Chapter 2. Polygons CG 2012

g

Figure 2.6: The region that a guard g can observe.

Exercise 2.20 Describe a family (Pn)n⩾3 of simple polygons such that Pn has n vertices
and at least ⌊n/3⌋ guards are needed to guard it.

What is more surprising: ⌊n/3⌋ guards are always suﬃcient as well. Chvátal [6] was
the ﬁrst to prove that, but then Fisk [8] gave a much simpler proof using—you may
have guessed it—triangulations. Fisk’s proof was considered so beautiful that it was
included into “Proofs from THE BOOK” [1], a collection inspired by Paul Erdős’ belief
in “a place where God keeps aesthetically perfect proofs”. The proof is based on the
following lemma.

Lemma 2.21 Every triangulation of a simple polygon is 3-colorable. That is, each
vertex can be assigned one of three colors in such a way that adjacent vertices
receive diﬀerent colors.

Proof. Induction on n. For n = 3 the statement is obvious. For n > 3, by Theorem 2.15
the triangulation contains an ear uvw. Cutting oﬀ the ear creates a triangulation of a
polygon on n − 1 vertices, which by the inductive hypothesis admits a 3-coloring. Now
whichever two colors the vertices u and w receive in this coloring, there remains a third
color to be used for v. 
Theorem 2.22 (Fisk [8]) Every simple polygon on n vertices can be guarded using at
most ⌊n/3⌋ guards.

Proof. Consider a triangulation of the polygon and a 3-coloring of the vertices as ensured
by Lemma 2.21. Take the smallest color class, which clearly consists of at most ⌊n/3⌋
vertices, and put a guard at each vertex. As every point of the polygon is contained in
at least one triangle and every triangle has exactly one vertex in the guarding set, the
whole polygon is guarded. 
Questions

1. What is a simple polygon/a simple polygon with holes Explain the deﬁnitions
and provide some examples of members and non-members of the respective classes.

20

CG 2012 2.3. The Art Gallery Problem

Figure 2.7: A triangulation of a simple polygon on 17 vertices and a 3-coloring of it.
The vertices shown solid orange form the smallest color class and guard
the polygon using ⌊17/3⌋ = 5 guards.

For a given polygon you should be able to tell which of these classes it belongs to
or does not belong to and argue why this is the case.

2. What is a closed/open/bounded/connected/simply-connected set in R
d? What
is the interior/closure of a point set? Explain the deﬁnitions and provide some
illustrative examples. For a given set you should be able to argue which of the
properties mentioned it possesses.

3. What is a triangulation of a simple polygon? Does it always exist? Explain
the deﬁnition and provide some illustrative examples. Present the proof of Theo-
rem 2.13 in detail.

4. How about higher dimensional generalizations? Can every polyhedron in R
3

be nicely subdivided into tetrahedra? Explain Schönhardt’s construction.

5. How many points are needed to guard a simple polygon? Present the proofs of
Theorem 2.15, Lemma 2.21, and Theorem 2.22 in detail.

References

[1] Martin Aigner and Günter M. Ziegler, Proofs from THE BOOK. Springer-Verlag,
Berlin, 3rd edn., 2003.

[2] Nancy M. Amato, Michael T. Goodrich, and Edgar A. Ramos, A randomized algo-
rithm for triangulating a simple polygon in linear time. Discrete Comput. Geom.,
26, 2, (2001), 245–265, URL http://dx.doi.org/10.1007/s00454-001-0027-x.

[3] Takao Asano, Tetsuo Asano, and Ron Y. Pinter, Polygon triangulation:
eﬃciency and minimality. J. Algorithms, 7, 2, (1986), 221–231, URL
http://dx.doi.org/10.1016/0196-6774(86)90005-2.

[4] Bernard Chazelle, Triangulating a simple polygon in linear time. Discrete Comput.
Geom., 6, 5, (1991), 485–524, URL http://dx.doi.org/10.1007/BF02574703.

21

Chapter 2. Polygons CG 2012

[5] Tobias Christ, Beyond triangulation: covering polygons with triangles. In
Proc. 12th Algorithms and Data Struct. Sympos., vol. 6844 of Lec-
ture Notes Comput. Sci., pp. 231–242, Springer-Verlag, 2011, URL
http://dx.doi.org/10.1007/978-3-642-22300-6_20.

[6] Václav Chvátal, A combinatorial theorem in plane geome-
try. J. Combin. Theory Ser. B, 18, 1, (1975), 39–41, URL
http://dx.doi.org/10.1016/0095-8956(75)90061-1.

[7] Erik D. Demaine, Joseph S. B. Mitchell, and Joseph O’Rourke, The Open Problems
Project, Problem #10. http://cs.smith.edu/~orourke/TOPP/P10.html.

[8] Steve Fisk, A short proof of Chvátal’s watchman theorem. J. Combin. Theory Ser.
B, 24, 3, (1978), 374, URL http://dx.doi.org/10.1016/0095-8956(78)90059-X.

[9] Gary H. Meisters, Polygons have ears. Amer. Math. Monthly, 82, 6, (1975), 648–
651, URL http://www.jstor.org/stable/2319703.

[10] Gary H. Meisters, Principal vertices, exposed points, and ears. Amer. Math.
Monthly, 87, 4, (1980), 284–285, URL http://www.jstor.org/stable/2321563.

[11] Bojan Mohar and Carsten Thomassen, Graphs on surfaces. Johns Hopkins Uni-
versity Press, Baltimore, 2001.

[12] Erich Schönhardt, Über die Zerlegung von Dreieckspolyedern in Tetraeder. Math.
Ann., 98, (1928), 309–312, URL http://dx.doi.org/10.1007/BF01451597.

22

Chapter 3

Convex Hull

There exists an incredible variety of point sets and polygons. Among them, some have
certain properties that make them “nicer” than others in some respect. For instance,
look at the two polygons shown below.

(a) A convex polygon. (b) A non-convex polygon.

Figure 3.1: Examples of polygons: Which do you like better?

As it is hard to argue about aesthetics, let us take a more algorithmic stance. When
designing algorithms, the polygon shown on the left appears much easier to deal with
than the visually and geometrically more complex polygon shown on the right. One
particular property that makes the left polygon nice is that one can walk between any
two vertices along a straight line without ever leaving the polygon. In fact, this statement
holds true not only for vertices but for any two points within the polygon. A polygon
or, more generally, a set with this property is called convex.

Deﬁnition 3.1 A set P ⊆ R
d is convex if and only if pq ⊆ P, for any p, q ∈ P.

An alternative, equivalent way to phrase convexity would be to demand that for every
line ℓ ⊂ R
d the intersection ℓ ∩ P be connected. The polygon shown in Figure 3.1b is
not convex because there are some pairs of points for which the connecting line segment
is not completely contained within the polygon.
Indeed there are many problems that are comparatively easy to solve for convex sets
but very hard in general. We will encounter some particular instances of this phenomenon

23

Chapter 3. Convex Hull CG 2012

later in the course. However, not all polygons are convex and a discrete set of points is
never convex, unless it consists of at most one point only. In such a case it is useful to
make a given set P convex, that is, approximate P with or, rather, encompass P within
a convex set H ⊇ P. Ideally, H diﬀers from P as little as possible, that is, we want H to
be a smallest convex set enclosing P.
At this point let us step back for a second and ask ourselves whether this wish makes
sense at all: Does such a set H (always) exist? Fortunately, we are on the safe side
because the whole space R
d is certainly convex. It is less obvious, but we will see below
that H is actually unique. Therefore it is legitimate to refer to H as the smallest convex
set enclosing P or—shortly—the convex hull of P.

3.1 Convexity

Consider P ⊂ R
d. The following terminology should be familiar from linear algebra
courses.

Linear hull.

lin(P) := {
q ∣
∣
∣ q = ∑ λipi ∧ ∀ i : pi ∈ P, λi ∈ R} ,

the set of all linear combinations of P (smallest linear subspace containing P). For
instance, if P = {p} ⊂ R
2 \ {0} then lin(P) is the line through p and the origin.

Aﬃne hull.

aﬀ(P) := {q ∣
∣
∣ q = ∑ λipi ∧ ∑ λi = 1 ∧ ∀ i : pi ∈ P, λi ∈ R} ,

the set of all aﬃne combinations of P (smallest aﬃne subspace containing P). For
instance, if P = {p, q} ⊂ R
2 and p ̸= q then aﬀ(P) is the line through p and q.

Convex hull.

Proposition 3.2 A set P ⊆ R
d is convex if and only if ∑n
i=1 λipi ∈ P, for all n ∈ N,
p1, . . . , pn ∈ P, and λ1, . . . , λn ⩾ 0 with ∑n
i=1 λi = 1.

Proof. “⇐”: obvious with n = 2.
“⇒”: Induction on n. For n = 1 the statement is trivial. For n ⩾ 2, let pi ∈ P
and λi ⩾ 0, for 1 ⩽ i ⩽ n, and assume ∑n
i=1 λi = 1. We may suppose that λi > 0,
for all i. (Simply omit those points whose coeﬃcient is zero.) We need to show that∑n
i=1 λipi ∈ P.
Deﬁne λ = ∑n−1
i=1 λi and for 1 ⩽ i ⩽ n − 1 set µi = λi/λ. Observe that µi ⩾ 0
and ∑n−1
i=1 µi = 1. By the inductive hypothesis, q := ∑n−1
i=1 µipi ∈ P, and thus by
convexity of P also λq + (1 − λ)pn ∈ P. We conclude by noting that λq + (1 − λ)pn =
λ ∑n−1
i=1 µipi + λnpn = ∑n
i=1 λipi. 
24

CG 2012 3.1. Convexity

Observation 3.3 For any family (Pi)i∈I of convex sets the intersection ⋂
i∈I Pi is con-
vex.

Deﬁnition 3.4 The convex hull conv(P) of a set P ⊂ R
d is the intersection of all convex
supersets of P.

By Observation 3.3, the convex hull is convex, indeed. The following proposition provides
an algebraic description of the convex hull, similar as given above for the linear and aﬃne
hull.

Proposition 3.5 For any P ⊆ R
d we have

conv(P) =
 { n∑

i=1 λipi
 ∣
∣
∣
∣
∣ n ∈ N ∧
 n∑

i=1 λi = 1 ∧ ∀i ∈ {1, . . . , n} : λi ⩾ 0 ∧ pi ∈ P
 }
 .

The elements of the set on the right hand side are referred to as convex combinations
of P.
Proof. “⊇”: Consider a convex set C ⊇ P. By Proposition 3.2 (only-if direction) the
right hand side is contained in C. As C was arbitrary, the claim follows.
“⊆”: Denote the set on the right hand side by R. We show that R forms a convex set.
Let p = ∑n
i=1 λipi and q = ∑n
i=1 µipi be two convex combinations. (We may suppose
that both p and q are expressed over the same pi by possibly adding some terms with
a coeﬃcient of zero.)
Then for λ ∈ [0, 1] we have λp + (1 − λ)q = ∑n
i=1(λλi + (1 − λ)µi)pi ∈ R, as
λλi︸︷︷︸
⩾0 + (1 − λ)
︸ ︷︷ ︸
⩾0 µi︸︷︷︸
⩾0 ⩾ 0, for all 1 ⩽ i ⩽ n, and ∑n
i=1(λλi + (1 − λ)µi) = λ + (1 − λ) = 1. 
Deﬁnition 3.6 The convex hull of a ﬁnite point set P ⊂ R
d forms a convex polytope.
Each p ∈ P for which p /∈ conv(P \ {p}) is called a vertex of conv(P). A vertex of
conv(P) is also called an extremal point of P. A convex polytope in R
2 is called a
convex polygon. A convex polytope in R
3 is called a convex polyhedron.

Essentially, the following proposition shows that the term vertex above is well deﬁned.

Proposition 3.7 A convex polytope in R
d is the convex hull of its vertices.

Proof. Let P = {p1, . . . , pn}, n ∈ N, such that without loss of generality p1, . . . , pk
are the vertices of P := conv(P). We prove by induction on n that conv(p1, . . . , pn) ⊆
conv(p1, . . . , pk). For n = k the statement is trivial.
For n > k, pn is not a vertex of P and hence pn can be expressed as a convex
combination pn = ∑n−1
i=1 λipi. Thus for any x ∈ P we can write x = ∑n
i=1 µipi =
∑n−1
i=1 µipi + µn ∑n−1
i=1 λipi = ∑n−1
i=1 (µi + µnλi)pi. As ∑n−1
i=1 (µi + µnλi) = 1, we conclude
inductively that x ∈ conv(p1, . . . , pn−1) ⊆ conv(p1, . . . , pk). 
25

Chapter 3. Convex Hull CG 2012

Theorem 3.8 (Carathéodory [3]) For any P ⊂ R
d and q ∈ conv(P) there exist k ⩽ d + 1
points p1, . . . , pk ∈ P such that q ∈ conv(p1, . . . , pk).

Exercise 3.9 Prove Theorem 3.8.

Theorem 3.10 (Separation Theorem) Any two compact convex sets C, D ⊂ R
d with C ∩
D = ∅ can be separated strictly by a hyperplane, that is, there exists a hyperplane
h such that C and D lie in the opposite open halfspaces bounded by h.

Proof. Consider the distance function d : C × D → R with (c, d) ↦→ ||c − d||. Since
C × D is compact and d is continuous and strictly bounded from below by 0, d attains
its minimum at some point (c0, d0) ∈ C × D with d(c0, d0) > 0. Let h be the hyperplane
perpendicular to the line segment c0d0 and passing through the midpoint of c0 and d0.

c0 d0

C Dh c ′

If there was a point, say, c ′ in C ∩ h, then by
convexity of C the whole line segment coc ′ lies in
C and some point along this segment is closer to
d0 than is c0, in contradiction to the choice of c0.
The ﬁgure shown to the right depicts the situation
in R
2. If, say, C has points on both sides of h, then
by convexity of C it has also a point on h, but we
just saw that there is no such point. Therefore, C
and D must lie in diﬀerent open halfspaces bounded
by h. 
Actually, the statement above holds for arbitrary (not necessarily compact) convex sets,
but the separation is not necessarily strict (the hyperplane may have to intersect the sets)
and the proof is a bit more involved (cf. [7], but also check the errata on Matoušek’s
webpage).

Exercise 3.11 Show that the Separation Theorem does not hold in general, if not both
of the sets are convex.

Exercise 3.12 Prove or disprove:

(a) The convex hull of a compact subset of R
d is compact.

(b) The convex hull of a closed subset of R
d is closed.

Altogether we obtain various equivalent deﬁnitions for the convex hull, summarized
in the following theorem.

Theorem 3.13 For a compact set P ⊂ R
d we can characterize conv(P) equivalently as
one of

(a) the smallest (w. r. t. set inclusion) convex subset of R
d that contains P;

(b) the set of all convex combinations of points from P;

26

CG 2012 3.2. Planar Convex Hull

(c) the set of all convex combinations formed by d + 1 or fewer points from P;

(d) the intersection of all convex supersets of P;

(e) the intersection of all closed halfspaces containing P.

Exercise 3.14 Prove Theorem 3.13.

3.2 Planar Convex Hull

Although we know by now what is the convex hull of point set, it is not yet clear how
to construct it algorithmically. As a ﬁrst step, we have to ﬁnd a suitable representation
for convex hulls. In this section we focus on the problem in R
2, where the convex hull
of a ﬁnite point set forms a convex polygon. A convex polygon is easy to represent,
for instance, as a sequence of its vertices in counterclockwise orientation. In higher
dimensions ﬁnding a suitable representation for convex polytopes is a much more delicate
task.

Problem 3.15 (Convex hull)

Input: P = {p1, . . . , pn} ⊂ R
2, n ∈ N.

Output: Sequence (q1, . . . , qh), 1 ⩽ h ⩽ n, of the vertices of conv(P) (ordered counter-
clockwise).

q1
 q2 q3
 q4

q5

q6
q7
 (a) Input.
 q1
 q2 q3
 q4

q5

q6
q7
 (b) Output.

Figure 3.2: Convex Hull of a set of points in R
2.

Another possible algorithmic formulation of the problem is to ignore the structure of the
convex hull and just consider it as a point set.

Problem 3.16 (Extremal points)

Input: P = {p1, . . . , pn} ⊂ R
2, n ∈ N.

Output: Set Q ⊆ P of the vertices of conv(P).

27

Chapter 3. Convex Hull CG 2012

Degeneracies. A couple of further clariﬁcations regarding the above problem deﬁnitions
are in order.
First of all, for eﬃciency reasons an input is usually speciﬁed as a sequence of points.
Do we insist that this sequence forms a set or are duplications of points allowed?
What if three points are collinear? Are all of them considered extremal? According
to our deﬁnition from above, they are not and that is what we will stick to. But note
that there may be cases where one wants to include all such points, nevertheless.
By the Separation Theorem, every extremal point p can be separated from the convex
hull of the remaining points by a halfplane. If we take such a halfplane and shift its
deﬁning line such that it passes through p, then all points from P other than p should lie
in the resulting open halfplane. In R
2 it turns out convenient to work with the following
“directed” reformulation.

Proposition 3.17 A point p ∈ P = {p1, . . . , pn} ⊂ R
2 is extremal for P ⇐⇒ there is a
directed line g through p such that P \ {p} is to the left of g.
 c r
The interior angle at a vertex v of a polygon P is the angle
between the two edges of P incident to v whose corresponding
angular domain lies in P◦. If this angle is smaller than π, the
vertex is called convex ; if the angle is larger than π, the vertex is
called reﬂex. For instance, the vertex c in the polygon depicted
to the right is a convex vertex, whereas the vertex labeled r is
a reﬂex vertex.

Exercise 3.18
A simple polygon S ⊂ R
2 is star-shaped if and only if there
exists a point c ∈ S, such that for every point p ∈ S the
line segment cp is contained in S. A simple polygon with
exactly three convex vertices is called a pseudotriangle (see
the example shown on the right).

In the following we consider subsets of R
2. Prove or disprove:

a) Every convex vertex of a simple polygon lies on its convex hull.

b) Every star-shaped set is convex.

c) Every convex set is star-shaped.

d) The intersection of two convex sets is convex.

e) The union of two convex sets is convex.

f ) The intersection of two star-shaped sets is star-shaped.

g) The intersection of a convex set with a star-shaped set is star-shaped.

28

CG 2012 3.3. Trivial algorithms

h) Every triangle is a pseudotriangle.

i) Every pseudotriangle is star-shaped.

3.3 Trivial algorithms

One can compute the extremal points using Carathéodory’s Theorem as follows: Test
for every point p ∈ P whether there are q, r, s ∈ P \ {p} such that p is inside the triangle
with vertices q, r, and s. Runtime O(n
4).
Another option, inspired by the Separation Theorem: test for every pair (p, q) ∈ P2

whether all points from P \ {p, q} are to the left of the directed line through p and q (or
on the line segment pq). Runtime O(n
3).

Exercise 3.19 Let P = (p0, . . . , pn−1) be a sequence of n points in R
2. Someone claims
that you can check by means of the following algorithm whether or not P describes
the boundary of a convex polygon in counterclockwise order:

bool is_convex(p0, . . . , pn−1) {
for i = 0, . . . , n − 1:
if (pi, p(i+1) mod n, p(i+2) mod n) form a rightturn:
return false;
return true;
}

Disprove the claim and describe a correct algorithm to solve the problem.

Exercise 3.20 Let P ⊂ R
2 be a convex polygon, given as an array p[0]. . .p[n-1] of its
n vertices in counterclockwise order.

a) Describe an O(log(n)) time algorithm to determine whether a point q lies
inside, outside or on the boundary of P.

b) Describe an O(log(n)) time algorithm to ﬁnd a (right) tangent to P from a
query point q located outside P. That is, ﬁnd a vertex p[i], such that P is
contained in the closed halfplane to the left of the oriented line qp[i].

3.4 Jarvis’ Wrap

We are now ready to describe a ﬁrst simple algorithm to construct the convex hull. It
works as follows:

Find a point p1 that is a vertex of conv(P) (e.g., the one with smallest x-
coordinate). “Wrap” P starting from p1, i.e., always ﬁnd the next vertex
of conv(P) as the one that is rightmost with respect to the direction given
by the previous two vertices.
 29

Chapter 3. Convex Hull CG 2012

Besides comparing x-coordinates, the only geometric primitive needed is an orienta-
tion test: Denote by rightturn(p, q, r), for three points p, q, r ∈ R
2, the predicate that
is true if and only if r is (strictly) to the right of the oriented line pq.

q[0]=p start
 q next

q[1]
 q[2]

Code for Jarvis’ Wrap.

p[0..N) contains a sequence of N points.
p_start point with smallest x-coordinate.
q_next some other point in p[0..N).

int h = 0;
Point_2 q_now = p_start;
do {
q[h] = q_now;
h = h + 1;

for (int i = 0; i < N; i = i + 1)
if (rightturn_2(q_now, q_next, p[i]))
q_next = p[i];

q_now = q_next;
q_next = p_start;
} while (q_now != p_start);

q[0,h) describes a convex polygon bounding the convex hull of p[0..N).

Analysis. For every output point the above algorithm spends n rightturn tests, which is
⇒ O(nh) in total.

Theorem 3.21 [6] Jarvis’ Wrap computes the convex hull of n points in R
2 using
O(nh) rightturn tests, where h is the number of hull vertices.

In the worst case we have h = n, that is, O(n
2) rightturn tests. Jarvis’ Wrap has a
remarkable property that is called output sensitivity: the runtime depends not only on
the size of the input but also on the size of the output. For a huge point set it constructs

30

CG 2012 3.5. Graham Scan (Successive Local Repair)

the convex hull in optimal linear time, if the convex hull consists of a constant number of
vertices only. Unfortunately the worst case performance of Jarvis’ Wrap is suboptimal,
as we will see soon.

Degeneracies. The algorithm may have to cope with various degeneracies. Several points have smallest x-coordinate ⇒ lexicographic order:

(px, py) < (qx, qy) ⇐⇒ px < qx ∨ px = qx ∧ py < qy . Three or more points collinear ⇒ choose the point that is farthest among those
that are rightmost.

Predicates. Besides the lexicographic comparison mentioned above, the Jarvis’ Wrap
(and most other 2D convex hull algorithms for that matter) need one more geomet-
ric predicate: the rightturn or—more generally—orientation test. The computation
amounts to evaluating a polynomial of degree two, see the exercise below. We therefore
say that the orientation test has algebraic degree two. In contrast, the lexicographic
comparison has degree one only. The algebraic degree not only has a direct impact on
the eﬃciency of a geometric algorithm (lower degree ↔ less multiplications), but also an
indirect one because high degree predicates may create large intermediate results, which
may lead to overﬂows and are much more costly to compute with exactly.

Exercise 3.22 Prove that for three points (px, py), (qx, qy), (rx, ry) ∈ R
2, the sign of
the determinant
∣
∣
∣
∣
∣
∣
 1 px py
1 qx qy
1 rx ry
 ∣
∣
∣
∣
∣
∣

determines if r lies to the right, to the left or on the directed line through p and q.

3.5 Graham Scan (Successive Local Repair)

There exist many algorithms that exhibit a better worst-case runtime than Jarvis’ Wrap.
Here we discuss only one of them: a particularly elegant and easy-to-implement variant
of the so-called Graham Scan [5]. This algorithm is referred to as Successive Local
Repair because it starts with some polygon enclosing all points and then step-by-step
repairs the deﬁciencies of this polygon, by removing non-convex vertices. It goes as
follows:
Sort points lexicographically and remove duplicates: (p1, . . . , pn).

31

Chapter 3. Convex Hull CG 2012

p9
 p4
 p1
 p3
 p2
 p5

p8

p7 p6

p9 p4 p1 p3 p2 p5 p8 p7 p6 p7 p8 p5 p2 p3 p1 p4 p9

As long as there is a (consecutive) triple (p, q, r) such that r is to the right of or on the
directed line −→pq, remove q from the sequence.

Code for Graham Scan.

p[0..N) lexicographically sorted sequence of pairwise distinct points, N ⩾ 2.

q[0] = p[0];
int h = 0;
// Lower convex hull (left to right):
for (int i = 1; i < N; i = i + 1) {
while (h>0 && !leftturn_2(q[h-1], q[h], p[i]))
h = h - 1;
h = h + 1;
q[h] = p[i];
}

// Upper convex hull (right to left):
for (int i = N-2; i >= 0; i = i - 1) {
while (!leftturn_2(q[h-1], q[h], p[i]))
h = h - 1;
h = h + 1;
q[h] = p[i];
}

q[0,h) describes a convex polygon bounding the convex hull of p[0..N).

Analysis.

Theorem 3.23 The convex hull of a set P ⊂ R
2 of n points can be computed using
O(n log n) geometric operations.

Proof.

1. Sorting and removal of duplicate points: O(n log n).

32

CG 2012 3.6. Lower Bound

2. At the beginning we have a sequence of 2n − 1 points; at the end the sequence
consists of h points. Observe that for every positive orientation test, one point is
discarded from the sequence for good. Therefore, we have exactly 2n − h − 1 such
shortcuts/positive orientation tests. In addition there are at most 2n − 2 negative
tests (#iterations of the outer for loops). Altogether we have at most 4n − h − 3
orientation tests.

In total the algorithm uses O(n log n) geometric operations. Note that the number of
orientation tests is linear only, but O(n log n) lexicographic comparisons are needed. 
3.6 Lower Bound

It is not hard to see that the runtime of Graham Scan is asymptotically optimal in the
worst-case.

Theorem 3.24 Ω(n log n) geometric operations are needed to construct the convex hull
of n points in R
2 (in the algebraic computation tree model).

Proof. Reduction from sorting (for which it is known that Ω(n log n) comparisons
are needed in the algebraic computation tree model). Given n real numbers x1, . . . , xn,
construct a set P = {pi | 1 ⩽ i ⩽ n} of n points in R
2 by setting pi = (xi, x
2
i). This
construction can be regarded as embedding the numbers into R
2 along the x-axis and
then projecting the resulting points vertically onto the unit parabola. The order in which
the points appear along the lower convex hull of P corresponds to the sorted order of
the xi. Therefore, if we could construct the convex hull in o(n log n) time, we could also
sort in o(n log n) time. 
Clearly this reduction does not work for the Extremal Points problem. But us-
ing a reduction from Element Uniqueness (see Section 1.1) instead, one can show that
Ω(n log n) is also a lower bound for the number of operations needed to compute the set
of extremal points only. This was ﬁrst shown by Avis [1] for linear computation trees,
then by Yao [8] for quadratic computation trees, and ﬁnally by Ben-Or [2] for general
algebraic computation trees.

3.7 Chan’s Algorithm

Given matching upper and lower bounds we may be tempted to consider the algorithmic
complexity of the planar convex hull problem settled. However, this is not really the
case: Recall that the lower bound is a worst case bound. For instance, the Jarvis’ Wrap
runs in O(nh) time an thus beats the Ω(n log n) bound in case that h = o(log n). The
question remains whether one can achieve both output dependence and optimal worst
case performance at the same time. Indeed, Chan [4] presented an algorithm to achieve
this runtime by cleverly combining the “best of” Jarvis’ Wrap and Graham Scan. Let us

33

Chapter 3. Convex Hull CG 2012

look at this algorithm in detail. The algorithm consists of two steps that are executed
one after another.

Divide. Input: a set P ⊂ R
2 of n points and a number H ∈ {1, . . . , n}.

1. Divide P into k = ⌈n/H⌉ sets P1, . . . , Pk with |Pi| ⩽ H.

2. Construct conv(Pi) for all i, 1 ⩽ i ⩽ k.

Analysis. Step 1 takes O(n) time. Step 2 can be handled using Graham Scan in
O(H log H) time for any single Pi, that is, O(n log H) time in total.

Conquer. Output: H vertices of conv(P), or the message that conv(P) has less than H
vertices.

1. Find the lexicographically smallest point in conv(Pi) for all i, 1 ⩽ i ⩽ k.

2. Starting from the lexicographically smallest point of P ﬁnd the ﬁrst H points of
conv(P) oriented counterclockwise (simultaneous Jarvis’ Wrap on the sequences
conv(Pi)).

Determine in every wrap step the point qi of tan-
gency from the current point of conv(P) to conv(Pi),
for all 1 ⩽ i ⩽ k. We have seen in Exercise 3.20 how
to compute qi in O(log |conv(Pi)|) = O(log H) time.
Among the k candidates q1, . . . , qk we ﬁnd the next
vertex of conv(P) in O(k) time.
Analysis. Step 1 takes O(n) time. Step 2 con-
sists of at most H wrap steps. Each wrap step needs
O(k log H + k) = O(k log H) time, which amounts to
O(Hk log H) = O(n log H) time for Step 2 in total.
Remark. Using a more clever search strategy instead of many tangency searches one
can handle the conquer phase in O(n) time, see Exercise 3.25 below. However, this is
irrelevant as far as the asymptotic runtime is concerned, given that already the divide
step takes O(n log H) time.

Exercise 3.25 Consider k convex polygons P1, . . . Pk, for some constant k ∈ N, where
each polygon is given as a list of its vertices in counterclockwise orientation. Show
how to construct the convex hull of P1 ∪ . . . ∪ Pk in O(n) time, where n = ∑k
i=1 ni
and ni is the number of vertices of Pi, for 1 ⩽ i ⩽ k.

34

CG 2012 3.7. Chan’s Algorithm

Searching for h. While the runtime bound for H = h is exactly what we were heading for,
it looks like in order to actually run the algorithm we would have to know h, which—
in general—we do not. Fortunately we can circumvent this problem rather easily, by
applying what is called a doubly exponential search. It works as follows.
Call the algorithm from above iteratively with parameter H = min{22t, n}, for t =
0, . . ., until the conquer step ﬁnds all extremal points of P (i.e., the wrap returns to its
starting point).
Analysis: Let 22
s be the last parameter for which the algorithm is called. Since the
previous call with H = 22s−1 did not ﬁnd all extremal points, we know that 22s−1 < h,
that is, 2s−1 < log h, where h is the number of extremal points of P. The total runtime
is therefore at most

s∑

i=0 cn log 22
i = cn
 s∑

i=0 2i = cn(2s+1 − 1) < 4cn log h = O(n log h),

for some constant c ∈ R. In summary, we obtain the following theorem.

Theorem 3.26 The convex hull of a set P ⊂ R
2 of n points can be computed using
O(n log h) geometric operations, where h is the number of convex hull vertices.

Questions

6. How is convexity deﬁned? What is the convex hull of a set in R
d? Give at
least three possible deﬁnitions.

7. What does it mean to compute the convex hull of a set of points in R
2? Discuss
input and expected output and possible degeneracies.

8. How can the convex hull of a set of n points in R
2 be computed eﬃciently?
Describe and analyze (incl. proofs) Jarvis’ Wrap, Successive Local Repair, and
Chan’s Algorithm.

9. Is there a linear time algorithm to compute the convex hull of n points in R
2?
Prove the lower bound and deﬁne/explain the model in which it holds.

10. Which geometric primitive operations are used to compute the convex hull of
n points in R
2? Explain the two predicates and how to compute them.

References

[1] David Avis, Comments on a lower bound for convex hull de-
termination. Inform. Process. Lett., 11, 3, (1980), 126, URL
http://dx.doi.org/10.1016/0020-0190(80)90125-8.

35

Chapter 3. Convex Hull CG 2012

[2] Michael Ben-Or, Lower bounds for algebraic computation trees. In Proc.
15th Annu. ACM Sympos. Theory Comput., pp. 80–86, 1983, URL
http://dx.doi.org/10.1145/800061.808735.

[3] C. Carathéodory, Über den Variabilitätsbereich der Fourierschen Konstanten von pos-
itiven harmonischen Funktionen. Rendiconto del Circolo Matematico di Palermo,
32, (1911), 193–217.

[4] Timothy M. Chan, Optimal output-sensitive convex hull algorithms in two and
three dimensions. Discrete Comput. Geom., 16, 4, (1996), 361–368, URL
http://dx.doi.org/10.1007/BF02712873.

[5] Ronald L. Graham, An eﬃcient algorithm for determining the convex hull
of a ﬁnite planar set. Inform. Process. Lett., 1, 4, (1972), 132–133, URL
http://dx.doi.org/10.1016/0020-0190(72)90045-2.

[6] Ray A. Jarvis, On the identiﬁcation of the convex hull of a ﬁnite set
of points in the plane. Inform. Process. Lett., 2, 1, (1973), 18–21, URL
http://dx.doi.org/10.1016/0020-0190(73)90020-3.

[7] Jiří Matoušek, Lectures on discrete geometry. Springer-Verlag, New York, NY, 2002.

[8] Andrew C. Yao, A lower bound to ﬁnding convex hulls. J. ACM, 28, 4, (1981),
780–787, URL http://dx.doi.org/10.1145/322276.322289.

36

Chapter 4

Line Sweep

In this chapter we will discuss a simple and widely applicable paradigm to design ge-
ometric algorithms: the so-called Line-Sweep (or Plane-Sweep) technique. It can be
used to solve a variety of diﬀerent problems, some examples are listed below. The ﬁrst
part may come as a reminder to many of you, because you should have heard something
about line-sweep in one of the basic CS courses already. However, we will soon proceed
and encounter a couple of additional twists that were most likely not covered there.
Consider the following geometric problems.

Problem 4.1 Given a sequence P = (p1, . . . , pn) of points
in R
2, does P describe the boundary of a simple polygon? ?

Problem 4.2 (Polygon Intersection) Given two simple poly-
gons P and Q in R
2 as a (counterclockwise) sequence of
their vertices, is P ∩ Q = ∅?
 ?

Problem 4.3 (Segment Intersection Test) Given a set of n
closed line segments in R
2, do any two of them intersect? ?

Remark: In principle it is clear what is meant by “two segments intersect”. But there
are a few special cases that one may have to consider carefully. For instance, does it count
if an endpoint lies on another segment? What if two segments share an endpoint? What
about overlapping segments and segments of length zero? In general, let us count all
these as intersections. However, sometimes we may want to exclude some of these cases.
For instance, in a simple polygon test, we do not want to consider the shared endpoint
between two consecutive edges of the boundary as an intersection.

Problem 4.4 (Segment Intersections) Given a set of n closed
line segments in R
2, compute all pairs of segments that
intersect.
 ⇒

37

Chapter 4. Line Sweep CG 2012

Problem 4.5 (Segment Arrangement) Given a set of n closed
line segments in R
2, construct the arrangement induced
by S, that is, the subdivision of R
2 induced by S.
 ⇒

Problem 4.6 (Map Overlay) Given two sets S and T of n and
m, respectively, pairwise interior disjoint line segments in
R
2, construct the arrangement induced by S ∪ T .
 ⇒

In the following we will use Problem 4.4 as our ﬂagship example.

Trivial Algorithm. Test all the (n
2) pairs of segments from S in O(n
2) time and O(n) space.
For Problem 4.4 this is worst-case optimal because there may by Ω(n
2) intersecting pairs.
But in case that the number of intersecting pairs is, say, linear in n there is still hope
to obtain a subquadratic algorithm. Given that there is a lower bound of Ω(n log n) for
Element Uniqueness (Given x1, . . . , xn ∈ R, is there an i ̸= j such that xi = xj?) in the
algebraic computation tree model, all we can hope for is an output-sensitive runtime of
the form O(n log n + k), where k denotes the number of intersecting pairs (output size).

4.1 Interval Intersections

As a warmup let us consider the corresponding problem in R
1.

Problem 4.7 Given a set I of n intervals [ℓi, ri] ⊂ R, 1 ⩽ i ⩽ n. Compute all pairs of
intervals from I that intersect.

Theorem 4.8 Problem 4.7 can be solved in O(n log n + k) time and O(n) space, where
k is the number of intersecting pairs from (I
2
)
.

Proof. First observe that two real intervals intersect if and only if one contains the right
endpoint of the other.
Sort the set {(ℓi, 0) | 1 ⩽ i ⩽ n} ∪ {(ri, 1) | 1 ⩽ i ⩽ n} in increasing lexicographic order
and denote the resulting sequence by P. Store along with each point from P its origin
(i). Walk through P from start to end while maintaining a list L of intervals that contain
the current point p ∈ P.
Whenever p = (ℓi, 0), 1 ⩽ i ⩽ n, insert i into L. Whenever p = (ri, 1), 1 ⩽ i ⩽ n,
remove i from L and then report for all j ∈ L the pair {i, j} as intersecting. 
4.2 Segment Intersections

How can we transfer the (optimal) algorithm for the corresponding problem in R
1 to the
plane? In R
1 we moved a point from left to right and at any point resolved the situation
locally around this point. More precisely, at any point during the algorithm, we knew all

38

CG 2012 4.2. Segment Intersections

intersections that are to the left of the current (moving) point. A point can be regarded
a hyperplane in R
1, and the corresponding object in R
2 is a line.

General idea. Move a line ℓ (so-called sweep line) from left to right over the plane, such
that at any point during this process all intersections to the left of ℓ have been reported.

Sweep line status. The list of intervals containing the current point corresponds to a list L
of segments (sorted by y-coordinate) that intersect the current sweep line ℓ. This list L is
called sweep line status (SLS). Considering the situation locally around L, it is obvious
that only segments that are adjacent in L can intersect each other. This observation
allows to reduce the overall number of intersection tests, as we will see. In order to
allow for eﬃcient insertion and removal of segments, the SLS is usually implemented as
a balanced binary search tree.

Event points. The order of segments in SLS can change at certain points only: whenever
the sweep line moves over a segment endpoint or a point of intersection of two segments
from S. Such a point is referred to as an event point (EP) of the sweep. Therefore we
can reduce the conceptually continuous process of moving the sweep line over the plane
to a discrete process that moves the line from EP to EP. This discretization allows for
an eﬃcient computation.
At any EP several events can happen simultaneously: several segments can start
and/or end and at the same point a couple of other segments can intersect. In fact
the sweep line does not even make a diﬀerence between any two event points that have
the same x-coordinate. To properly resolve the order of processing, EPs are considered
in lexicographic order and wherever several events happen at a single point, these are
considered simultaneously as a single EP. In this light, the sweep line is actually not a
line but an inﬁnitesimal step function (see Figure 4.1).

Event point schedule. In contrast to the one-dimensional situation, in the plane not all
EP are known in advance because the points of intersection are discovered during the
algorithm only. In order to be able to determine the next EP at any time, we use a
priority queue data structure, the so-called event point schedule (EPS).
Along with every EP p store a list end(p) of all segments that end at p, a list begin(p)
of all segments that begin at p, and a list int(p) of all segments in SLS that intersect at
p a segment that is adjacent to it in SLS.
Along with every segment we store pointers to all its appearances in an int(·) list of
some EP. As a segment appears in such a list only if it intersects one of its neighbors
there, every segment needs to store at most two such pointers.

39

Chapter 4. Line Sweep CG 2012

p

1

2

4

5
 6

7
2

3

5

(a) Before.
 p

1

2

3

4

5
 6

7
2

3

5

(b) After.

Figure 4.1: Handling an event point p. Ending segments are shown red (dashed),
starting segments green (dotted), and passing segments blue (solid).

Invariants. The following conditions can be shown to hold before and after any event
point is handled. (We will not formally prove this here.) In particular, the last condition
at the end of the sweep implies the correctness of the algorithm.

1. L is the sequence of segments from S that intersect ℓ, ordered by y-coordinate of
their point of intersection.

2. E contains all endpoints of segments from S and all points where two segments that
are adjacent in L intersect to the right of ℓ.

3. All pairs from (
S
2) that intersect to the left of ℓ have been reported.

Event point handling. An EP p is processed as follows.

1. If end(p) ∪ int(p) = ∅, localize p in L.

2. Report all pairs of segments from end(p) ∪ begin(p) ∪ int(p) as intersecting.

3. Remove all segments in end(p) from L.

4. Reverse the subsequence in L that is formed by the segments from int(p).

5. Insert segments from begin(p) into L, sorted by slope.

6. Test the topmost and bottommost segment in L from begin(p) ∪ int(p) for intersec-
tion with its successor and predecessor, respectively, and update EP if necessary.

40

CG 2012 4.2. Segment Intersections

Updating EPS. Insert an EP p corresponding to an intersection of two segments s and
t. Without loss of generality let s be above t at the current position of ℓ.

1. If p does not yet appear in E, insert it.

2. If s is contained in an int(·) list of some other EP q, where it intersects a segment
t ′ from above: Remove both s and t ′ from the int(·) list of q and possibly remove
q from E (if end(q) ∪ begin(q) ∪ int(q) = ∅). Proceed analogously in case that t
is contained in an int(·) list of some other EP, where it intersects a segment from
below.

3. Insert s and t into int(p).

Sweep.

1. Insert all segment endpoints into begin(·)/end(·) list of a corresponding EP in E.

2. As long as E ̸= ∅, handle the ﬁrst EP and then remove it from E.

Runtime analysis. Initialization: O(n log n). Processing of an EP p:

O(#intersecting pairs + |end(p)| log n + |int(p)| + |begin(p)| log n + log n).

In total: O(k+n log n+k log n) = O((n+k) log n), where k is the number of intersecting
pairs in S.

Space analysis. Clearly |S| ⩽ n. At begin we have |E| ⩽ 2n and |S| = 0. Furthermore the
number of additional EPs corresponding to points of intersection is always bounded by
2|S|. Thus the space needed is O(n).

Theorem 4.9 Problem 4.4 and Problem 4.5 can be solved in O((n + k) log n) time and
O(n) space. 
Theorem 4.10 Problem 4.1, Problem 4.2 and Problem 4.3 can be solved in O(n log n)
time and O(n) space. 
Exercise 4.11 Flesh out the details of the sweep line algorithm for Problem 4.2 that is
referred to in Theorem 4.10. What if you have to construct the intersection rather
than just to decide whether or not it is empty?

Exercise 4.12 You are given n axis–parallel rectangles in R
2 with their bottom sides
lying on the x–axis. Construct their union in O(n log n) time.

41

Chapter 4. Line Sweep CG 2012

4.3 Improvements

The basic ingredients of the line sweep algorithm go back to work by Bentley and
Ottmann [2] from 1979. The particular formulation discussed here, which takes all
possible degeneracies into account, is due to Mehlhorn and Näher [9].
Theorem 4.10 is obviously optimal for Problem 4.3, because this is just the 2-
dimensional generalization of Element Uniqueness (see Section 1.1). One might sus-
pect there is also a similar lower bound of Ω(n log n) for Problem 4.1 and Problem 4.2.
However, this is not the case: Both can be solved in O(n) time, albeit using a very
complicated algorithm of Chazelle [4] (the famous triangulation algorithm).
Similarly, it is not clear why O(n log n+k) time should not be possible in Theorem 4.9.
Indeed this was a prominent open problem in the 1980’s that has been solved in several
steps by Chazelle and Edelsbrunner in 1988. The journal version of their paper [5]
consists of 54 pages and the space usage is suboptimal O(n + k).
Clarkson and Shor [6] and independently Mulmuley [10, 11] described randomized
algorithms with expected runtime O(n log n + k) using O(n) and O(n + k), respectively,
space.
An optimal deterministic algorithm, with runtime O(n log n + k) and using O(n)
space, is known since 1995 only due to Balaban [1].

4.4 Algebraic degree of geometric primitives

We already have encountered diﬀerent notions of complexity during this course: We can
analyze the time complexity and the space complexity of algorithms and both usually
depend on the size of the input. In addition we have seen examples of output-sensitive
algorithms, whose complexity also depends on the size of the output. In this section,
we will discuss a diﬀerent kind of complexity that is the algebraic complexity of the
underlying geometric primitives. In this way, we try to shed a bit of light into the
bottom layer of geometric algorithms that is often swept under the rug because it consists
of constant time operations only. But it would be a mistake to disregard this layer
completely, because in most—if not every—real world application it plays a crucial role
and the value of the constants involved can make a big diﬀerence.
In all geometric algorithms there are some fundamental geometric predicates and/or
constructions on the bottom level. Both are operations on geometric objects, the diﬀer-
ence is only in the result: The result of a construction is a geometric object (for instance,
the point common to two non-parallel lines), whereas the result of a predicate is Boolean
(true or false).
Geometric predicates and constructions in turn are based on fundamental arithmetic
operations. For instance, we formulated planar convex hull algorithms in terms of an
orientation predicate—given three points p, q, r ∈ R
2, is r strictly to the right of the ori-
ented line pr— which can be implemented using multiplication and addition/subtraction
of coordinates/numbers. When using limited precision arithmetic, it is important to keep

42

CG 2012 4.4. Algebraic degree of geometric primitives

an eye on the size of the expressions that occur during an evaluation of such a predicate.
In Exercise 3.22 we have seen that the orientation predicate can be computed by
evaluating a polynomial of degree two in the input coordinates and, therefore, we say
that

Proposition 4.13 The rightturn/orientation predicate for three points in R
2 has alge-
braic degree two.

The degree of a predicate depends on the algebraic expression used to evaluate it. Any
such expression is intimately tied to the representation of the geometric objects used.
Where not stated otherwise, we assume that geometric objects are represented as de-
scribed in Section 1.2. So in the proposition above we assume that points are repre-
sented using Cartesian coordinates. The situation might be diﬀerent, if, say, a polar
representation is used instead.
But even once a representation is agreed upon, there is no obvious correspondence
to an algebraic expression that describes a given predicate. There are many diﬀerent
ways to form polynomials over the components of any representation, but it is desirable
to keep the degree of the expression as small as possible. Therefore we deﬁne the (al-
gebraic) degree of a geometric predicate or construction as the minimum degree of a
polynomial that deﬁnes it. So there still is something to be shown in order to complete
Proposition 4.13.

Exercise 4.14 Show that there is no polynomial of degree at most one that describes
the orientation test in R
2.
Hint: Let p = (0, 0), q = (x, 0), and r = (0, y) and show that there is no linear
function in x and y that distinguishes the region where pqr form a rightturn from
its complement.

The degree of a predicate corresponds to the size of numbers that arise during its
evaluation. If all input coordinates are k-bit integers then the numbers that occur during
an evaluation of a degree d predicate on these coordinates are of size about1 dk. If the
number type used for the computation can represent all such numbers, the predicate
can be evaluated exactly and thus always correctly. For instance, when using a standard
IEEE double precision ﬂoating point implementation which has a mantissa length of 53
bit then the above orientation predicate can be evaluated exactly if the input coordinates
are integers between 0 and 225, say.
Let us now get back to the line segment intersection problem. It needs a few new
geometric primitives: most prominently, constructing the intersection point of two line
segments.

1It is only about dk because not only multiplications play a role but also additions. As a rule of thumb,
a multiplication may double the bitsize, while an addition may increase it by one.

43

Chapter 4. Line Sweep CG 2012

Two segments. Given two line segments s = λa + (1 − λ)b, λ ∈ [0, 1] and t = µc + (1 −
µ)d, µ ∈ [0, 1], it is a simple exercise in linear algebra to compute s ∩ t. Note that s ∩ t
is either empty or a single point or a line segment.
For a = (ax, ay), b = (bx, by), c = (cx, cy), and d = (dx, dy) we obtain two linear
equations in two variables λ and µ.

λax + (1 − λ)bx = µcx + (1 − µ)dx
λay + (1 − λ)by = µcy + (1 − µ)dy

Rearranging terms yields

λ(ax − bx) + µ(dx − cx) = dx − bx
λ(ay − by) + µ(dy − cy) = dy − by

Assuming that the lines underlying s and t have distinct slopes (that is, they are neither
identical nor parallel) we have

D = ∣
∣
∣
∣ ax − bx dx − cx
ay − by dy − cy
 ∣
∣
∣
∣ =
 ∣
∣
∣
∣
∣
∣
∣
∣
 ax ay 1 0
bx by 1 0
cx cy 0 1
dx dy 0 1
 ∣
∣
∣
∣
∣
∣
∣
∣
 ̸= 0

and using Cramer’s rule

λ = 1
D
 ∣
∣
∣
∣ dx − bx dx − cx
dy − by dy − cy
 ∣
∣
∣
∣ and µ = 1
D
 ∣
∣
∣
∣ ax − bx dx − bx
ay − by dy − by
 ∣
∣
∣
∣ .

To test if s and t intersect, we can—after having sorted out the degenerate case in
which both segments have the same slope—compute λ and µ and then check whether
λ, µ ∈ [0, 1].
Observe that both λ and D result from multiplying two diﬀerences of input coor-
dinates. Computing the x-coordinate of the point of intersection via bx + λ(ax − bx)
uses another multiplication. Overall this computation yields a fraction whose numerator
is a polynomial of degree three in the input coordinates and whose denominator is a
polynomial of degree two in the input coordinates.
In order to maintain the sorted order of event points in the EPS, we need to compare
event points lexicographically. In case that both are intersection points, this amounts
to comparing two fractions of the type discussed above. In order to formulate such a
comparison as a polynomial, we have to cross-multiply the denominators, and so obtain
a polynomial of degree 3 + 2 = 5. It can be shown (but we will not do it here) that this
bound is tight and so we conclude that

Proposition 4.15 The algebraic degree of the predicate that compares two intersection
points of line segments lexicographically is ﬁve.

44

CG 2012 4.5. Red-Blue Intersections

Therefore the coordinate range in which this predicate can be evaluated exactly using
IEEE double precision numbers shrinks down to integers between 0 and about 210 =
1 ′024.

Exercise 4.16 What is the algebraic degree of the predicate checking whether two line
segments intersect? (Above we were interested in the actual intersection point,
but now we consider the predicate that merely answers the question whether two
segments intersect or not by yes or no).

Exercise 4.17 What is the algebraic degree of the InCircle predicate? More precisely,
you are given three points p, q, r in the plane that deﬁne a circle C and a fourth
point s. You want to know if s is inside C or not. What is the degree of the
polynomial(s) you need to evaluate to answer this question?

4.5 Red-Blue Intersections

Although the Bentley-Ottmann sweep appears to be rather simple, its implementation
is not straightforward. For once, the original formulation did not take care of possible
degeneracies—as we did in the preceding section. But also the algebraic degree of the
predicates used is comparatively high. In particular, comparing two points of intersection
lexicographically is a predicate of degree ﬁve, that is, in order to compute it, we need to
evaluate a polynomial of degree ﬁve. When evaluating such a predicate with plain ﬂoating
point arithmetic, one easily gets incorrect results due to limited precision roundoﬀ errors.
Such failures frequently render the whole computation useless. The line sweep algorithm
is problematic in this respect, as a failure to detect one single point of intersection often
implies that no other intersection of the involved segments to the right is found.
In general, predicates of degree four are needed to construct the arrangement of line
segments because one needs to determine the orientation of a triangle formed by three
segments. This is basically an orientation test where two points are segment endpoints
and the third point is an intersection point of segments. Given that the coordinates of
the latter are fractions, whose numerator is a degree three polynomial and the common
denominator is a degree two polynomial, we obtain a degree four polynomial overall.
Motivated by the Map overlay application we consider here a restricted case. In the
red-blue intersection problem, the input consists of two sets R (red) and B (blue) of
segments such that the segments in each set are interior-disjoint, that is, for any pair of
distinct segments their relative interior is disjoint. In this case there are no triangles of
intersecting segments, and it turns out that predicates of degree two suﬃce to construct
the arrangement. This is optimal because already the intersection test for two segments
is a predicate of degree two.

Predicates of degree two. Restricting to degree two predicates has certain consequences.
While it is possible to determine the position of a segment endpoint relative to a(nother)

45

Chapter 4. Line Sweep CG 2012

segment using an orientation test, one cannot, for example, compare a segment endpoint
with a point of intersection lexicographically. Even computing the coordinates for a
point of intersection is not possible. Therefore the output of intersection points is done
implicitly, as “intersection of s and t”.
Graphically speaking we can deform any segment—keeping its endpoints ﬁxed—as
long as it remains monotone and it does not reach or cross any segment endpoint (it
did not touch before). With help of degree two predicates there is no way to tell the
diﬀerence.

Witnesses. Using such transformations the processing of intersection points is deferred as
long as possible (lazy computation). The last possible point w(s, t) where an intersection
between two segments s and t has to be processed we call the witness of the intersection.
The witness w(s, t) is the lexicographically smallest segment endpoint that is located
within the closed wedge formed by the two intersecting segments s and t to the right
of the point of intersection (Figure 4.2). Note that each such wedge contains at least
two segment endpoints, namely the right endpoints of the two intersecting segments.
Therefore for any pair of intersecting segments its witness is well-deﬁned.

s
 t
 w

Figure 4.2: The witness w(s, t) of an intersection s ∩ t.

As a consequence, only the segment endpoints are EPs and the EPS can be determined
by lexicographic sorting during initialization. On the other hand, the SLS structure gets
more complicated because its order of segments does not necessarily reﬂect the order in
which the segments intersect the sweep line.

Invariants. The invariants of the algorithm have to take the relaxed notion of order into
account. Denote the sweep line by ℓ.

1. L is the sequence of segments from S intersecting ℓ; s appears before t in L =⇒ s
intersects ℓ above t or s intersects t and the witness of this intersection is to the
right of ℓ.

2. All intersections of segments from S whose witness is to the left of ℓ have been
reported.

SLS Data Structure. The SLS structure consist of three levels. We use the fact that
segments of the same color do not interact, except by sharing endpoints possibly.

46

CG 2012 4.5. Red-Blue Intersections

1. Collect adjacent segments of the same color in bundles, stored as balanced search
trees. For each bundle store pointers to the topmost and bottommost segment.
(As the segments within one bundle are interior-disjoint, their order remains static
and thus correct under possible deformations due to lazy computation.)

2. All bundles are stored in a doubly linked list, sorted by y-coordinate.

3. All red bundles are stored in a balanced search tree (bundle tree).

List

Bundle
Tree

Figure 4.3: Graphical representation of the SLS data structure.

The search tree structure should support insert, delete, split and merge in (amortized)
logarithmic time each. For instance, splay trees [12] meet these requirements. (If you
have never heard about splay trees so far, you do not need to know for our purposes
here. Just treat them as a black box. However, you should take a note and read about
splay trees still. They are a fascinating data structure.)

EP handling. An EP p is processed as follows.

1. Localize p in bundle tree → ⩽ 2 bundles containing p (all red bundles in between
must end at p). For the localization we use the pointers to the topmost and
bottommost segment within a bundle.

2. Localize p in ⩽ 2 red bundles found and split them at p. (If p is above the topmost
or below the bottommost segment of the bundle, there is no split.) All red bundles
are now either above, ending, or below with respect to p.

3. Localize p within the blue bundles by linear search.

4. Localize p in the ⩽ 2 blue bundles found and split them at p. (If p is above the
topmost or below the bottommost segment of the bundle, there is no split.) All
bundles are now either above, ending, or below with respect to p.

47

Chapter 4. Line Sweep CG 2012

5. Run through the list of bundles around p. More precisely, start from one of the
bundles containing p found in Step 1 and walk up in the doubly linked list of
bundles until two successive bundles (hence of opposite color) are both above p.
Similarly, walk down in the doubly linked list of bundles, until two successive
bundles are both below p. Handle all adjacent pairs of bundles (A, B) that are in
wrong order and report all pairs of segments as intersecting. (Exchange A and B
in the bundle list and merge them with their new neighbors.)

6. Report all pairs from begin(p) × end(p) as intersecting.

7. Remove ending bundles and insert starting segments, sorted by slope and bundled
by color and possibly merge with the closest bundle above or below.

Remark: As both the red and the blue segments are interior-disjoint, at every EP there
can be at most one segment that passes through the EP. Should this happen, for the
purpose of EP processing split this segment into two, one ending and one starting at this
EP. But make sure to not report an intersection between the two parts!

Analysis. Sorting the EPS: O(n log n) time. Every EP generates a constant number of
tree searches and splits of O(log n) each. Every exchange in Step 5 generates at least
one intersection. New bundles are created only by inserting a new segment or by one
of the constant number of splits at an EP. Therefore O(n) bundles are created in total.
The total number of merge operations is O(n), as every merge kills one bundle and O(n)
bundles are created overall. The linear search in steps 3 and 5 can be charged either to
the ending bundle or—for continuing bundles—to the subsequent merge operation. In
summary, we have a runtime of O(n log n + k) and space usage is linear obviously.

Theorem 4.18 For two sets R and B, each consisting of interior-disjoint line segments
in R
2, one can ﬁnd all intersecting pairs of segments in O(n log n + k) time and
linear space, using predicates of maximum degree two. Here n = |R| + |B| and k is
the number of intersecting pairs.

Remarks. The ﬁrst optimal algorithm for the red-blue intersection problem was pub-
lished in 1988 by Harry Mairson and Jorge Stolﬁ [7]. In 1994 Timothy Chan [3] described
a trapezoidal-sweep algorithm that uses predicates of degree three only. The approach
discussed above is due to Andrea Mantler and Jack Snoeyink [8] from 2000.

Exercise 4.19 Let S be a set of n segments each of which is either horizontal or
vertical. Describe an O(n log n) time and O(n) space algorithm that counts the
number of pairs in (
S
2) that intersect.
 48

CG 2012 4.5. Red-Blue Intersections

Questions

11. How can one test whether a polygon on n vertices is simple? Describe an
O(n log n) time algorithm.

12. How can one test whether two simple polygons on altogether n vertices inter-
sect? Describe an O(n log n) time algorithm.

13. How does the line sweep algorithm work that ﬁnds all k intersecting pairs
among n line segments in R
2? Describe the algorithm, using O((n + k) log n)
time and O(n) space. In particular, explain the data structures used, how event
points are handled, and how to cope with degeneracies.

14. Given two line segments s and t in R
2 whose endpoints have integer coordi-
nates in [0, 2b); suppose s and t intersect in a single point q, what can you
say about the coordinates of q? Give a good (tight up to small additive number
of bits) upper bound on the size of these coordinates. (No need to prove tightness,
that is, give an example which achieves the bound.)

15. What is the degree of a predicate and why is it an important parameter? What
is the degree of the orientation test and the incircle test in R
2? Explain the
term and give two reasons for its relevance. Provide tight upper bounds for the
two predicates mentioned. (No need to prove tightness.)

16. What is the map overlay problem and how can it be solved optimally using
degree two predicates only? Give the problem deﬁnition and explain the term
“interior-disjoint”. Explain the bundle-sweep algorithm, in particular, the data
structures used, how an event point is processed, and the concept of witnesses.

References

[1] Ivan J. Balaban, An optimal algorithm for ﬁnding segment intersections. In
Proc. 11th Annu. ACM Sympos. Comput. Geom., pp. 211–219, 1995, URL
http://dx.doi.org/10.1145/220279.220302.

[2] Jon L. Bentley and Thomas A. Ottmann, Algorithms for reporting and counting
geometric intersections. IEEE Trans. Comput., C-28, 9, (1979), 643–647, URL
http://dx.doi.org/10.1109/TC.1979.1675432.

[3] Timothy M. Chan, A simple trapezoid sweep algorithm for reporting red/blue seg-
ment intersections. In Proc. 6th Canad. Conf. Comput. Geom., pp. 263–268, 1994,
URL https://cs.uwaterloo.ca/~tmchan/red_blue.ps.gz.

[4] Bernard Chazelle, Triangulating a simple polygon in linear time. Discrete Comput.
Geom., 6, 5, (1991), 485–524, URL http://dx.doi.org/10.1007/BF02574703.

49

Chapter 4. Line Sweep CG 2012

[5] Bernard Chazelle and H. Edelsbrunner, An optimal algorithm for inter-
secting line segments in the plane. J. ACM, 39, 1, (1992), 1–54, URL
http://dx.doi.org/10.1145/147508.147511.

[6] Kenneth L. Clarkson and Peter W. Shor, Applications of random sampling in
computational geometry, II. Discrete Comput. Geom., 4, (1989), 387–421, URL
http://dx.doi.org/10.1007/BF02187740.

[7] Harry G. Mairson and Jorge Stolﬁ, Reporting and counting intersections between
two sets of line segments. In R. A. Earnshaw, ed., Theoretical Foundations of
Computer Graphics and CAD, vol. 40 of NATO ASI Series F, pp. 307–325,
Springer-Verlag, Berlin, Germany, 1988.

[8] Andrea Mantler and Jack Snoeyink, Intersecting red and blue line seg-
ments in optimal time and precision. In J. Akiyama, M. Kano, and
M. Urabe, eds., Proc. Japan Conf. Discrete Comput. Geom., vol. 2098
of Lecture Notes Comput. Sci., pp. 244–251, Springer Verlag, 2001, URL
http://dx.doi.org/10.1007/3-540-47738-1_23.

[9] Kurt Mehlhorn and Stefan Näher, Implementation of a sweep line algorithm for
the straight line segment intersection problem. Report MPI-I-94-160, Max-Planck-
Institut Inform., Saarbrücken, Germany, 1994.

[10] Ketan Mulmuley, A Fast Planar Partition Algorithm, I. J. Symbolic Comput., 10,
3-4, (1990), 253–280, URL http://dx.doi.org/10.1016/S0747-7171(08)80064-8.

[11] Ketan Mulmuley, A fast planar partition algorithm, II. J. ACM, 38, (1991), 74–103,
URL http://dx.doi.org/10.1145/102782.102785.

[12] Daniel D. Sleator and Robert E. Tarjan, Self-adjusting binary search trees. J. ACM,
32, 3, (1985), 652–686, URL http://dx.doi.org/10.1145/3828.3835.

50

Chapter 5

Plane Graphs and the DCEL

So far we have been talking about geometric structures such as triangulations of polygons
and arrangements of line segments without paying much attention to how to represent
these structures. This will change now. As all of these structures can be regarded as
plane graphs, we start by reviewing a bit of terminology from (planar) graph theory. We
assume that this is—at least somewhat—familiar ground for you. If you would like to
see more details and examples, please refer to any standard textbook on graph theory,
such as Bondy and Murty [2], Diestel [3], or West [10].
A (simple undirected) graph is a pair G = (V, E) where V is a ﬁnite set of vertices
and E is the set of edges, E ⊆ (
V
2 ) := {{u, v} | u, v ∈ V, u ̸= v}. For brevity, one often
writes uv rather than {u, v} to denote an edge. The two vertices deﬁning an edge are
adjacent to each other and they are incident to the edge.
For a vertex v ∈ V, denote by NG(v) the neighborhood of v in G, that is, the
set of vertices from G that are adjacent to v. Similarly, for a set W ⊂ V of vertices
deﬁne NG(W) := ⋃
w∈W NG(w). The degree degG(v) of a vertex v ∈ V is the size of
its neighborhood, that is, the number of edges from E incident to v. The subscript is
often omitted when it is clear to which graph it refers to. As every edge is incident to
exactly two vertices, we have the following simple but useful relationship, often called
handshaking-lemma: ∑
v∈V deg(v) = 2|E|.
A walk in a graph G is a sequence W = (v1, . . . , vk), k ∈ N, of vertices such that vi
and vi+1 are adjacent in G, for all 1 ⩽ i < k. A path is a walk whose vertices are pairwise
distinct. A cycle is a walk whose vertices are pairwise distinct, except for v1 = vk. A
graph is connected, if there is a path between any pair of vertices. If a graph is not
connected, it is disconnected. A disconnected graph can be decomposed into maximal
connected subgraphs, its (connected) components.
A tree is a connected graph that does not have any cycle. It is not hard to show that
trees on n vertices are exactly the graphs on n vertices that have n − 1 edges.
In geometry we are typically concerned with graphs that are embedded on some
surface, here R
2. An embedding or drawing is just a “nice” mapping of a graph G into
the plane. More formally, each vertex v is mapped to a distinct point φ(v) ∈ R
2 (that
is, φ : V → R
2 is injective) and each edge uv is mapped to an arc—a simple Jordan

51

Chapter 5. Plane Graphs and the DCEL CG 2012

curve—φ(uv) ⊂ R
2 from φ(u) to φ(v) such that no vertex is mapped to the relative
interior of φ(uv).
A graph is planar if it admits a crossing-free drawing, that is, a drawing in which
no two arcs intersect except at common endpoints. For example, K4 (the complete graph
on four vertices) is planar, as demonstrated by the drawing shown in Figure 5.1a.

(a) Crossing-free drawing. (b) Straight-line drawing.

Figure 5.1: Embeddings of K4 into the plane.

If a graph is planar, then by Fáry-Wagner’s Theorem [4, 8] there also exists a straight-
line drawing, that is, a drawing in which all arcs are line segments. In order to obtain
such a drawing for K4, we have to put one vertex inside the convex hull of the other
three, see Figure 5.1b.
Sometimes we refer to graphs not as abstract graphs but in a concrete embedding.
If this embedding is a crossing-free embedding into the plane, the embedded graph is
referred to as a plane graph. Note the distinction between “planar” and “plane”: The
former refers to an abstract graph and expresses the possibility of a crossing-free drawing,
whereas the latter refers to a geometric object that is a concrete crossing-free drawing of
a graph in the plane.
A plane straight-line graph (PSLG) is a crossing-free straight-line drawing of a graph
in the plane. Both graphs in Figure 5.1 are plane, but only the one shown on the right
is also a plane straight-line graph.

5.1 The Euler Formula

If we remove all vertices (points) and edges (arcs) of a plane graph G from R
2, then what
remains is a ﬁnite collection of open sets. These sets are referred to as the faces of G.
For instance, both plane graphs in Figure 5.1 have 4 vertices, 6 edges and 4 faces (one
of which is unbounded). In general, if |V| is the number of vertices of a connected plane
graph, |E| its number of edges and |F| the number of faces, then the Euler Formula states
that
 |V| − |E| + |F| = 2.

In the example, we get 4 − 6 + 4 = 2.
If you do not insist on being too formal, the proof is simple and works by induction
on the number of edges. If we ﬁx the number of vertices, the base case occurs for |V| − 1

52

CG 2012 5.2. The Doubly-Connected Edge List

edges where the plane graph is a tree. Then we have |F| = 1 and the formula holds.
A graph with more edges always contains a cycle and therefore at least one bounded
face. Choose one edge from a bounded face and remove it. The resulting graph is still
connected and has one edge less but also one face less since the edge removal merges
the bounded face with another one. Consequently, since the Euler Formula holds for the
smaller graph by induction, it also holds for the larger graph.
The Euler Formula can be used to prove the following important fact about planar
graphs.

Lemma 5.1 Any planar graph on n ⩾ 3 vertices has at most 3n − 6 edges and at most
2n − 4 faces.

This lemma shows that the overall complexity—the sum of the number of vertices, edges,
and faces—of a planar graph is linear in n. A planar graph with a maximal number
(3n − 6) of edges is called maximal planar.

Exercise 5.2 Prove Lemma 5.1 using the Euler formula.

Exercise 5.3 Prove that every planar graph has a vertex of degree at most 5.

Exercise 5.4 Show that K5 (the complete graph on ﬁve vertices) is not planar.

5.2 The Doubly-Connected Edge List

Many algorithms in computational geometry work with plane graphs. The doubly-
connected edge list (DCEL) is a data structure to represent a plane graph in such a way
that it is easy to traverse and to manipulate. In order to avoid unnecessary complications,
let us discuss only connected graphs here that contain at least two vertices. It is not hard
to extend the data structure to cover all plane graphs. For simplicity we also assume
that we deal with a straight-line embedding and so the geometry of edges is deﬁned by
the mapping of their endpoints already. For more general embeddings, the geometric
description of edges has to be stored in addition.
The main building block of a DCEL is a list of halfedges. Every actual edge is
represented by two halfedges going in opposite direction, and these are called twins, see
Figure 5.2. Along the boundary of each face, halfedges are oriented counterclockwise.
A DCEL stores a list of halfedges, a list of vertices, and a list of faces. These lists are
unordered but interconnected by various pointers. A vertex v stores a pointer halfedge(v)
to an arbitrary halfedge originating from v. Every vertex also knows its coordinates, that
is, the point point(v) it is mapped to in the represented embedding. A face f stores a
pointer halfedge(f) to an arbitrary halfedge within the face. A halfedge h stores ﬁve
pointers: a pointer target(h) to its target vertex,

53

Chapter 5. Plane Graphs and the DCEL CG 2012

h

next(h)

prev(h)
 twin(h)

target(h)

face(h)

Figure 5.2: A halfedge in a DCEL. a pointer face(h) to the incident face, a pointer twin(h) to its twin halfedge, a pointer next(h) to the halfedge following h along the boundary of face(h), and a pointer prev(h) to the halfedge preceding h along the boundary of face(h).

A constant amount of information is stored for every vertex, (half-)edge, and face of the
graph. Therefore the whole DCEL needs storage proportional to |V| + |E| + |F|, which is
O(n) for a plane graph with n vertices by Lemma 5.1.
This information is suﬃcient for most tasks. For example, traversing all edges around
a face f can be done as follows:

s ← halfedge(f)
h ← s
do something with h
h ← next(h)
while h ̸= s

Exercise 5.5 Give pseudocode to traverse all edges incident to a given vertex v of a
DCEL.

Exercise 5.6 Why is the previous halfedge prev(·) stored explicitly and the source ver-
tex of a halfedge is not?

5.2.1 Manipulating a DCEL

In many geometric algorithms, plane graphs appear not just as static objects but rather
they evolve over the course of the algorithm. Therefore the data structure used to
represent the graph must allow for eﬃcient update operations to change it.

54

CG 2012 5.2. The Doubly-Connected Edge List

First of all, we need to be able to generate new vertices, edges, and faces, to be added
to the corresponding list within the DCEL and—symmetrically—the ability to delete an
existing entity. Then it should be easy to add a new vertex v to the graph within some
face f. As we maintain a connected graph, we better link the new vertex to somewhere,
say, to an existing vertex u. For such a connection to be possible, we require that the
open line segment uv lies completely in f.
Of course, two halfedges are to be added connecting u and v. But where exactly?
Given that from a vertex and from a face only some arbitrary halfedge is directly accessi-
ble, it turns out convenient to use a halfedge in the interface. Let h denote the halfedge
incident to f for which target(h) = u. Our operation becomes then (see also Figure 5.3)

add-vertex-at(v, h)
Precondition: the open line segment point(v)point(u), where u := target(h),
lies completely in f := face(h).
Postcondition: a new vertex v has been inserted into f, connected by an edge
to u.
 u
 v

h f

. . .
 . . .

(a) before
 u
 v

h
 f

h1

h2

. . .
 . . .

(b) after

Figure 5.3: Add a new vertex connected to an existing vertex u.

and it can be realized by manipulating a constant number of pointers as follows.

add-vertex-at(v, h) {
h1 ← a new halfedge
h2 ← a new halfedge
halfedge(v) ← h2
twin(h1) ← h2
twin(h2) ← h1
target(h1) ← v
target(h2) ← u
face(h1) ← f
face(h2) ← f
next(h1) ← h2
next(h2) ← next(h)
prev(h1) ← h
 55

Chapter 5. Plane Graphs and the DCEL CG 2012

prev(h2) ← h1
next(h) ← h1
prev(next(h2)) ← h2
}

Similarly, it should be possible to add an edge between two existing vertices u and v,
provided the open line segment uv lies completely within a face f of the graph, see
Figure 5.4. Since such an edge insertion splits f into two faces, the operation is called
split-face. Again we use the halfedge h that is incident to f and for which target(h) = u.

u
 v

fh
 (a) before
 u
 v

f1

h f2

h1 h2

(b) after

Figure 5.4: Split a face by an edge uv.

Our operation becomes then

split-face(h, v)
Precondition: v is incident to f := face(h) but not adjacent to u := target(h).
The open line segment point(v)point(u) lies completely in f.
Postcondition: f has been split by a new edge uv.

The implementation is slightly more complicated compared to add-vertex-at above, be-
cause the face f is destroyed and so we have to update the face information of all incident
halfedges. In particular, this is not a constant time operation, but its time complexity
is proportional to the size of f.

split-face(h, v) {
f1 ← a new face
f2 ← a new face
h1 ← a new halfedge
h2 ← a new halfedge
halfedge(f1) ← h1
halfedge(f2) ← h2
twin(h1) ← h2
twin(h2) ← h1
target(h1) ← v
 56

CG 2012 5.2. The Doubly-Connected Edge List

target(h2) ← u
next(h2) ← next(h)
prev(next(h2)) ← h2
prev(h1) ← h
next(h) ← h1
i ← h2
loop
face(i) ← f2
if target(i) = v break the loop
i ← next(i)
endloop
next(h1) ← next(i)
prev(next(h1)) ← h1
next(i) ← h2
prev(h2) ← i
i ← h1
do face(i) ← f1
i ← next(i)
until target(i) = u
delete the face f
}

In a similar fashion one can realize the inverse operation join-face(h) that removes the
edge (represented by the halfedge) h, thereby joining the faces face(h) and face(twin(h)).
It is easy to see that every connected plane graph on at least two vertices can be
constructed using the operations add-vertex-at and split-face, starting from an embedding
of K2 (two vertices connected by an edge).

Exercise 5.7 Give pseudocode for the operation join-face(h). Also specify precondi-
tions, if needed.

Exercise 5.8 Give pseudocode for the operation split-edge(h), that splits the edge (rep-
resented by the halfedge) h into two by a new vertex w, see Figure 5.5.

5.2.2 Graphs with Unbounded Edges

In some cases it is convenient to consider plane graphs, in which some edges are not
mapped to a line segment but to an unbounded curve, such as a ray. This setting is not
really much diﬀerent from the one we studied before, except that one vertex is placed
“at inﬁnity”. One way to think of it is in terms of stereographic projection: Imagine
R
2 being the x/y-plane in R
3 and place a unit sphere S such that its southpole touches
the origin. We obtain a bijective continuous mapping between R
2 and S \ {n}, where n

57

Chapter 5. Plane Graphs and the DCEL CG 2012

u
 v

h
f2
 f1

(a) before
 u
 v

w

h2
 h1
k1
 k2
f2
 f1

(b) after

Figure 5.5: Split an edge by a new vertex.

is the northpole of S, as follows: A point p ∈ R
2 is mapped to the point p ′ that is the
intersection of the line through p and n with S, see Figure 5.6. The further away a point

n

p
 p ′

(a) Three-dimensional view.
 n

p
 p ′
 q

q ′

0
(b) Cross-section view.

Figure 5.6: Stereographic projection.

in R
2 is from the origin, the closer its image on S gets to n. But there is no way to reach
n except in the limit. Therefore, we can imagine drawing the graph on S instead of in
R
2 and putting the “inﬁnite vertex” at n.
All this is just for the sake of a proper geometric interpretation. As far as a DCEL
representation of such a graph is concerned, there is no need to consider spheres or, in
fact, anything beyond what we have discussed before. The only diﬀerence to the case
with all ﬁnite edges is that there is this special inﬁnite vertex, which does not have any
point/coordinates associated to it. But other than that, the inﬁnite vertex is treated
in exactly the same way as the ﬁnite vertices: it has in– and outgoing halfedges along
which the unbounded faces can be traversed (Figure 5.7).

5.2.3 Remarks

It is actually not so easy to point exactly to where the DCEL data structure originates
from. Often Muller and Preparata [7] are credited, but while they use the term DCEL,

58

CG 2012 5.2. The Doubly-Connected Edge List

∞

Figure 5.7: A DCEL with unbounded edges. Usually, we will not show the inﬁnite
vertex and draw all edges as straight-line segments. This yields a geo-
metric drawing, like the one within the gray box.

the data structure they describe is diﬀerent from what we discussed above and from what
people usually consider a DCEL nowadays. Overall, there is a large number of variants
of this data structure, which appear under the names winged edge data structure [1],
halfedge data structure [9], or quad-edge data structure [5]. Kettner [6] provides a
comparison of all these and some additional references.

Questions

17. What are planar/plane graphs and straight-line embeddings? Give the deﬁni-
tions and explain the diﬀerence between planar and plane.

18. How many edges can a planar graph have? What is the average vertex degree
in a planar graph? Explain Euler’s formula and derive your answers from it (see
Exercise 5.2 and 5.3).

19. How can plane graphs be represented on a computer? Explain the DCEL data
structure and how to work with it.

References

[1] Bruce G. Baumgart, A polyhedron representation for computer vision. In Proc.
AFIPS Natl. Comput. Conf., vol. 44, pp. 589–596, AFIPS Press, Alrington, Va.,
1975, URL http://dx.doi.org/10.1145/1499949.1500071.

59

Chapter 5. Plane Graphs and the DCEL CG 2012

[2] John Adrian Bondy and U. S. R. Murty, Graph Theory, vol. 244 of
Graduate texts in Mathematics. Springer-Verlag, New York, 2008, URL
http://dx.doi.org/10.1007/978-1-84628-970-5.

[3] Reinhard Diestel, Graph Theory. Springer-Verlag, Heidelberg, 4th edn., 2010.

[4] István Fáry, On straight lines representation of planar graphs. Acta Sci. Math.
Szeged, 11, (1948), 229–233.

[5] Leonidas J. Guibas and J. Stolﬁ, Primitives for the manipulation of general subdivi-
sions and the computation of Voronoi diagrams. ACM Trans. Graph., 4, 2, (1985),
74–123, URL http://dx.doi.org/10.1145/282918.282923.

[6] Lutz Kettner, Software design in computational geometry and contour-edge
based polyhedron visualization. Ph.D. thesis, ETH Zürich, Zürich, Switzerland,
1999, URL http://dx.doi.org/10.3929/ethz-a-003861002.

[7] David E. Muller and Franco P. Preparata, Finding the intersection of
two convex polyhedra. Theoret. Comput. Sci., 7, (1978), 217–236, URL
http://dx.doi.org/10.1016/0304-3975(78)90051-8.

[8] Klaus Wagner, Bemerkungen zum Vierfarbenproblem. Jahresbericht der
Deutschen Mathematiker-Vereinigung, 46, (1936), 26–32.

[9] Kevin Weiler, Edge-based data structures for solid modeling in a curved sur-
face environment. IEEE Comput. Graph. Appl., 5, 1, (1985), 21–40, URL
http://dx.doi.org/10.1109/MCG.1985.276271.

[10] Douglas B. West, An Introduction to Graph Theory. Prentice Hall, Upper Saddle
River, NJ, 2nd edn., 2001.
 60

Chapter 6

Delaunay Triangulations

In Chapter 2 we have discussed triangulations of simple polygons. A triangulation nicely
partitions a polygon into triangles, which allows, for instance, to easily compute the
area or a guarding of the polygon. Another typical application scenario is to use a
triangulation T for interpolation: Suppose a function f is deﬁned on the vertices of the
polygon P, and we want to extend it “reasonably” and continuously to P◦. Then for a
point p ∈ P◦ ﬁnd a triangle t of T that contains p. As p can be written as a convex
combination ∑3
i=1 λivi of the vertices v1, v2, v3 of t, we just use the same coeﬃcients to
obtain an interpolation f(p) := ∑3
i=1 λif(vi) of the function values.
If triangulations are a useful tool when working with polygons, they might also turn
out useful to deal with other geometric objects, for instance, point sets. But what could
be a triangulation of a point set? Polygons have a clearly deﬁned interior, which naturally
lends itself to be covered by smaller polygons such as triangles. A point set does not have
an interior, except . . . Here the notion of convex hull comes handy, because it allows us
to treat a point set as a convex polygon. Actually, not really a convex polygon, because
points in the interior of the convex hull should not be ignored completely. But one way to
think of a point set is as a convex polygon—its convex hull—possibly with some holes—
which are points—in its interior. A triangulation should then partition the convex hull
while respecting the points in the interior, as shown in the example in Figure 6.1b.

(a) Simple polygon triangulation. (b) Point set triangulation. (c) Not a triangulation.

Figure 6.1: Examples of (non-)triangulations.

In contrast, the example depicted in Figure 6.1c nicely subdivides the convex hull

61

Chapter 6. Delaunay Triangulations CG 2012

but should not be regarded a triangulation: Two points in the interior are not respected
but simply swallowed by a large triangle.
This interpretation directly leads to the following adaption of Deﬁnition 2.12.

Deﬁnition 6.1 A triangulation of a ﬁnite point set P ⊂ R
2 is a collection T of triangles,
such that

(1) conv(P) = ⋃
T ∈T T ;

(2) the vertices of all triangles in T are points from P;

(3) if p ∈ t, for any p ∈ P and t ∈ T, then p is a vertex of t; and

(4) for every distinct pair T , U ∈ T, the intersection T ∩ U is either a common
vertex, or a common edge, or empty.

Note that due to (4) we could also combine (2) and (3) to read “the vertices of the
triangles in T are exactly the points from P”.
Just as for polygons, triangulations are universally available for point sets, meaning
that (almost) every point set admits at least one.

Proposition 6.2 Every set P ⊆ R
2 of n ⩾ 3 points has a triangulation, unless all points
in P are collinear.

Proof. In order to construct a triangulation for P, consider the lexicographically sorted
sequence p1, . . . , pn of points in P. Let m be minimal such that p1, . . . , pm are not
collinear. We triangulate p1, . . . , pm by connecting pm to all of p1, . . . , pm−1 (which are
on a common line), see Figure 6.2a.

(a) Getting started. (b) Adding a point.

Figure 6.2: Constructing the scan triangulation of P.

Then we add pm+1, . . . , pn. When adding pi, for i > m, we connect pi with all
vertices of Ci−1 := conv({p1, . . . , pi−1}) that it “sees”, that is, every vertex v of Ci−1 for
which piv∩Ci−1 = {v}. In particular, among these vertices are the two points of tangency
from pi to Ci−1, which shows that we always add triangles (Figure 6.2b) whose union
after each step covers Ci. 
The triangulation that is constructed in Proposition 6.2 is called a scan triangulation.
Such a triangulation (Figure 6.3a (left) shows a larger example) is usually “ugly”, though,

62

CG 2012

since it tends to have many long and skinny triangles. This is not just an aesthetic deﬁcit.
Having long and skinny triangles means that the vertices of a triangle tend to be spread
out far from each other. You can probably imagine that such a behavior is undesirable,
for instance, in the context of interpolation. In contrast, the Delaunay triangulation
of the same point set (Figure 6.3b) looks much nicer, and we will discuss in the next
section how to get this triangulation.

(a) Scan triangulation. (b) Delaunay triangulation.

Figure 6.3: Two triangulations of the same set of 50 points.

Exercise 6.3 Describe an O(n log n) time algorithm to construct a scan triangulation
for a set of n points in R
2.

On another note, if you look closely into the SLR-algorithm to compute planar convex
hull that was discussed in Chapter 3, then you will realize that we also could have used
this algorithm in the proof of Proposition 6.2. Whenever a point is discarded during
SLR, a triangle is added to the polygon that eventually becomes the convex hull.
In view of the preceding chapter, we may regard a triangulation as a plane graph:
the vertices are the points in P and there is an edge between two points p ̸= q, if and
only if there is a triangle with vertices p and q. Therefore we can use Euler’s formula to
determine the number of edges in a triangulation.

Lemma 6.4 Any triangulation of a set P ⊂ R
2 of n points has exactly 3n−h−3 edges,
where h is the number of vertices on conv(P).

Proof. Consider a triangulation T of P and denote by E the set of edges and by F the
set of faces of T . We count the number of edge-face incidences in two ways. Denote
I = {(e, f) ∈ E × F : e ⊂ ∂f}.
 63

Chapter 6. Delaunay Triangulations CG 2012

On the one hand, every edge is incident to exactly two faces and therefore |I| = 2|E|.
On the other hand, every bounded face of T is a triangle and the unbounded face has h
edges on its boundary. Therefore, |I| = 3(|F| − 1) + h.
Together we obtain 3|F| = 2|E| − h + 3. Using Euler’s formula (3n − 3|E| + 3|F| = 6)
we conclude that 3n − |E| − h + 3 = 6 and so |E| = 3n − h − 3. 
In graph theory, the term “triangulation” is sometimes used as a synonym for “maxi-
mal planar”. But geometric triangulations are diﬀerent, they are maximal planar in the
sense that no straight-line edge can be added without sacriﬁcing planarity.

Corollary 6.5 A triangulation of a set P ⊂ R
2 of n points is maximal planar, if and
only if conv(P) is a triangle.

Proof. Combine Lemma 5.1 and Lemma 6.4. 
Exercise 6.6 Find for every n ⩾ 3 a simple polygon P with n vertices such that P has
exactly one triangulation. P should be in general position, meaning that no three
vertices are collinear.

Exercise 6.7 Show that every set of n ⩾ 5 points in general position (no three points
are collinear) has at least two diﬀerent triangulations.
Hint: Show ﬁrst that every set of ﬁve points in general position contains a convex
4-hole, that is, a subset of four points that span a convex quadrilateral that does
not contain the ﬁfth point.

6.1 The Empty Circle Property

We will now move on to study the ominous and supposedly nice Delaunay triangulations
mentioned above. They are deﬁned in terms of an empty circumcircle property for
triangles. The circumcircle of a triangle is the unique circle passing through the three
vertices of the triangle, see Figure 6.4.

Figure 6.4: Circumcircle of a triangle.

Deﬁnition 6.8 A triangulation of a ﬁnite point set P ⊂ R
2 is called a Delaunay triangu-
lation, if the circumcircle of every triangle is empty, that is, there is no point from
P in its interior.
 64

CG 2012 6.1. The Empty Circle Property

Consider the example depicted in Figure 6.5. It shows a Delaunay triangulation of a
set of six points: The circumcircles of all ﬁve triangles are empty (we also say that the
triangles satisfy the empty circle property). The dashed circle is not empty, but that is
ﬁne, since it is not a circumcircle of any triangle.

Figure 6.5: All triangles satisfy the empty circle property.

It is instructive to look at the case of four points in convex position. Obviously, there
are two possible triangulations, but in general, only one of them will be Delaunay, see
Figure 6.6a and 6.6b. If the four points are on a common circle, though, this circle is
empty; at the same time it is the circumcircle of all possible triangles; therefore, both
triangulations of the point set are Delaunay, see Figure 6.6c.

(a) Delaunay triangulation. (b) Non-Delaunay triangulation. (c) Two Delaunay triangulations.

Figure 6.6: Triangulations of four points in convex position.

Proposition 6.9 Given a set P ⊂ R
2 of four points that are in convex position but not
cocircular. Then P has exactly one Delaunay triangulation.

Proof. Consider a convex polygon P = pqrs. There are two triangulation of P: a
triangulation T1 using the edge pr and a triangulation T2 using the edge qs.
Consider the family C1 of circles through pr, which contains the circumcircles C1 =
pqr and C ′
1 = rsp of the triangles in T1. By assumption s is not on C1. If s is outside of

65

Chapter 6. Delaunay Triangulations CG 2012

C1, then q is outside of C ′
1: Consider the process of continuously moving from C1 to C ′
1
in C1 (Figure 6.7a); the point q is “left behind” immediately when going beyond C1 and
only the ﬁnal circle C ′
1 “grabs” the point s.

p

q r
 s

C1
 C ′
1

(a) Going from C1 to C′
1 in C1.
 p

q r
 s

C1

C2

(b) Going from C1 to C2 in C2.

Figure 6.7: Circumcircles and containment for triangulations of four points.

Similarly, consider the family C2 of circles through pq, which contains the circumcir-
cles C1 = pqr and C2 = spq, the latter belonging to a triangle in T2. As s is outside of
C1, it follows that r is inside C2: Consider the process of continuously moving from C1
to C2 in C2 (Figure 6.7b); the point r is on C1 and remains within the circle all the way
up to C2. This shows that T1 is Delaunay, whereas T2 is not.
The case that s is located inside C1 is symmetric: just cyclically shift the roles of
pqrs to qrsp. 
6.2 The Lawson Flip algorithm

It is not clear yet that every point set actually has a Delaunay triangulation (given that
not all points are on a common line). In this and the next two sections, we will prove
that this is the case. The proof is algorithmic. Here is the Lawson ﬂip algorithm for a
set P of n points.

1. Compute some triangulation of P (for example, the scan triangulation).

2. While there exists a subtriangulation of four points in convex position that is not
Delaunay (like in Figure 6.6b), replace this subtriangulation by the other triangu-
lation of the four points (Figure 6.6a).

We call the replacement operation in the second step a (Lawson) ﬂip.

Theorem 6.10 Let P ⊆ R
2 be a set of n points, equipped with some triangulation T.
The Lawson ﬂip algorithm terminates after at most (n
2) = O(n
2) ﬂips, and the
resulting triangulation D is a Delaunay triangulation of P.

66

CG 2012 6.3. Termination of the Lawson Flip Algorithm: The Lifting Map

We will prove Theorem 6.10 in two steps: First we show that the program described
above always terminates and, therefore, is an algorithm, indeed (Section 6.3). Then we
show that the algorithm does what it claims to do, namely the result is a Delaunay
triangulation (Section 6.4).

6.3 Termination of the Lawson Flip Algorithm: The Lifting Map

In order to prove Theorem 6.10, we invoke the (parabolic) lifting map. This is the
following: given a point p = (x, y) ∈ R
2, its lifting ℓ(p) is the point

ℓ(p) = (x, y, x
2 + y
2) ∈ R
3.

Geometrically, ℓ “lifts” the point vertically up until it lies on the unit paraboloid

{(x, y, z) | z = x
2 + y
2} ⊆ R
3,

see Figure 6.8a.

(a) The lifting map. (b) Points on/inside/outside a circle are lifted to
points on/below/above a plane.

Figure 6.8: The lifting map: circles map to planes.

The following important property of the lifting map is illustrated in Figure 6.8b.

Lemma 6.11 Let C ⊆ R
2 be a circle of positive radius. The “lifted circle” ℓ(C) = {ℓ(p) |
p ∈ C} is contained in a unique plane hC ⊆ R
3. Moreover, a point p ∈ R
2 is strictly
inside (outside, respectively) of C if and only if the lifted point ℓ(p) is strictly below
(above, respectively) hC.

Exercise 6.12 Prove Lemma 6.11.

Using the lifting map, we can now prove Theorem 6.10. Let us ﬁx the point set P for
this and the next section. First, we need to argue that the algorithm indeed terminates
(if you think about it a little, this is not obvious). So let us interpret a ﬂip operation in

67

Chapter 6. Delaunay Triangulations CG 2012

the lifted picture. The ﬂip involves four points in convex position in R
2, and their lifted
images form a tetrahedron in R
3 (think about why this tetrahedron cannot be “ﬂat”).
The tetrahedron is made up of four triangles; when you look at it from the top, you
see two of the triangles, and when you look from the bottom, you see the other two. In
fact, what you see from the top and the bottom are the lifted images of the two possible
triangulations of the four-point set in R
2 that is involved in the ﬂip.
Here is the crucial fact that follows from Lemma 6.11: The two top triangles come
from the non-Delaunay triangulation before the ﬂip, see Figure 6.9a. The reason is that
both top triangles have the respective fourth point below them, meaning that in R
2,
the circumcircles of these triangles contain the respective fourth point—the empty circle
property is violated. In contrast, the bottom two triangles come from the Delaunay
triangulation of the four points: they both have the respective fourth point above them,
meaning that in R
2, the circumcircles of the triangles do not contain the respective fourth
point, see Figure 6.9b.

(a) Before the ﬂip: the top two triangles of
the tetrahedron and the corresponding non-
Delaunay triangulation in the plane.
 (b) After the ﬂip: the bottom two triangles of the
tetrahedron and the corresponding Delaunay
triangulation in the plane.

Figure 6.9: Lawson ﬂip: the height of the surface of lifted triangles decreases.

In the lifted picture, a Lawson ﬂip can therefore be interpreted as an operation that
replaces the top two triangles of a tetrahedron by the bottom two ones. If we consider
the lifted image of the current triangulation, we therefore have a surface in R
3 whose
pointwise height can only decrease through Lawson ﬂips. In particular, once an edge
has been ﬂipped, this edge will be strictly above the resulting surface and can therefore
never be ﬂipped a second time. Since n points can span at most (n
2) edges, the bound
on the number of ﬂips follows.

6.4 Correctness of the Lawson Flip Algorithm

It remains to show that the triangulation of P that we get upon termination of the
Lawson ﬂip algorithm is indeed a Delaunay triangulation. Here is a ﬁrst observation
telling us that the triangulation is “locally Delaunay”.

68

CG 2012 6.4. Correctness of the Lawson Flip Algorithm

Observation 6.13 Let ∆, ∆ ′ be two adjacent triangles in the triangulation D that results
from the Lawson ﬂip algorithm. Then the circumcircle of ∆ does not have any
vertex of ∆ ′ in its interior, and vice versa.

If the two triangles together form a convex quadrilateral, this follows from the fact
that the Lawson ﬂip algorithm did not ﬂip the common edge of ∆ and ∆ ′. If the four
vertices are not in convex position, this is basic geometry: given a triangle ∆, its cir-
cumcircle C can only contains points of C \ ∆ that form a convex quadrilateral with the
vertices of ∆.
Now we show that the triangulation is also “globally Delaunay”.

Proposition 6.14 The triangulation D that results from the Lawson ﬂip algorithm is
a Delaunay triangulation.

Proof. Suppose for contradiction that there is some triangle ∆ ∈ D and some point
p ∈ P strictly inside the circumcircle C of ∆. Among all such pairs (∆, p), we choose one
for which we the distance of p to ∆ is minimal. Note that this distance is positive since
D is a triangulation of P. The situation is as depicted in Figure 6.10a.

q
 ∆

p

(a) A point p inside the cir-
cumcircle C of a triangle ∆.
 q
 ∆

p

q ∆ ′
 e

(b) The edge e of ∆ closest to p
and the second triangle ∆′

incident to e.
 ∆

p

q
 ∆ ′
 e
C ′ C

(c) The circumcircle C′ of ∆′ also
contains p, and p is closer to
∆′ than to ∆.

Figure 6.10: Correctness of the Lawson ﬂip algorithm.

Now consider the edge e of ∆ that is facing p. There must be another triangle ∆ ′ in
D that is incident to the edge e. By the local Delaunay property of D, the third vertex q
of ∆ ′ is on or outside of C, see Figure 6.10b. But then the circumcircle C ′ of ∆ ′ contains
the whole portion of C on p’s side of e, hence it also contains p; moreover, p is closer to
∆ ′ than to ∆ (Figure 6.10c). But this is a contradiction to our choice of ∆ and p. Hence
there was no (∆, p), and D is a Delaunay triangulation. 
Exercise 6.15 The Euclidean minimum spanning tree (EMST) of a ﬁnite point set
P ⊂ R
2 is a spanning tree for which the sum of the edge lengths is minimum
(among all spanning trees of P). Show:
 69

Chapter 6. Delaunay Triangulations CG 2012

a) Every EMST of P is a plane graph.

b) Every EMST of P contains a closest pair, i.e., an edge between two points
p, q ∈ P that have minimum distance to each other among all point pairs in (
P
2)
.

c) Every Delaunay Triangulation of P contains an EMST of P.

6.5 The Delaunay Graph

Despite the fact that a point set may have more than one Delaunay triangulation, there
are certain edges that are present in every Delaunay triangulation, for instance, the edges
of the convex hull.

Deﬁnition 6.16 The Delaunay graph of P ⊆ R
2 consists of all line segments pq, for
p, q ∈ P, that are contained in every Delaunay triangulation of P.

The following characterizes the edges of the Delaunay graph.

Lemma 6.17 The segment pq, for p, q ∈ P, is in the Delaunay graph of P if and only
if there exists a circle through p and q that has p and q on its boundary and all
other points of P are strictly outside.

Proof. “⇒”: Let pq be an edge in the Delaunay graph of P, and let D be a Delaunay
triangulation of P. Then there exists a triangle ∆ = pqr in D, whose circumcircle C does
not contain any point from P in its interior.
If there is a point s on ∂C such that rs intersects pq, then let ∆ ′ = pqt denote the
other (̸= ∆) triangle in D that is incident to pq (Figure 6.11a). Flipping the edge pq
to rt yields another Delaunay triangulation of P that does not contain the edge pq, in
contradiction to pq being an edge in the Delaunay graph of P. Therefore, there is no
such point s.
 p

q

r
 sC
 ∆
 t

∆ ′

(a) Another point s ∈ ∂C.
 p

q

r
C
 ∆
 C ′

(b) Moving C away from s.

Figure 6.11: Characterization of edges in the Delaunay graph (I).

70

CG 2012 6.5. The Delaunay Graph

Otherwise we can slightly change the circle C by moving away from r while keeping
p and q ﬁx. As P is a ﬁnite point set, we can do such a modiﬁcation without catching
another point from P with the circle. In this way we obtain a circle C ′ through p and q
such that all other points from P are strictly outside C ′ (Figure 6.12b).
“⇐”: Let D be a Delaunay triangulation of P. If pq is not an edge of D, there must
be another edge of D that crosses pq (otherwise, we could add pq to D and still have a
planar graph, a contradiction to D being a triangulation of P). Let rs denote the ﬁrst
edge of D that intersects the directed line segment pq.
Consider the triangle ∆ of D that is incident to rs on the side that faces p (given
that rs intersects pq this is a well deﬁned direction). By the choice of rs neither of the
other two edges of ∆ intersects pq, and p /∈ ∆
◦ because ∆ is part of a triangulation of P.
The only remaining option is that p is a vertex of ∆ = prs. As ∆ is part of a Delaunay
triangulation, its circumcircle C∆ is empty (i.e., C∆◦ ∩ P = ∅).
Consider now a circle C through p and q, which exists by assumption. Fixing p and q,
expand C towards r to eventually obtain the circle C ′ through p, q, and r (Figure 6.12a).
Recall that r and s are on diﬀerent sides of the line through p and q. Therefore, s lies
strictly outside of C ′. Next ﬁx p and r and expand C ′ towards s to eventually obtain the
circle C∆ through p, r, and s (Figure 6.12b). Recall that s and q are on the same side
of the line through p and r. Therefore, q ∈ C∆, which is in contradiction to C∆ being
empty. It follows that there is no Delaunay triangulation of P that does not contain the
edge pq. 
p

q

r
 s

C ′ C
 ∆

(a) Expanding C towards r.
 p

q

r
 s
C ′
 C∆
 ∆

(b) Expanding C′ towards s.

Figure 6.12: Characterization of edges in the Delaunay graph (II).

The Delaunay graph is useful to prove uniqueness of the Delaunay triangulation in
case of general position.

Corollary 6.18 Let P ⊂ R
2 be a ﬁnite set of points in general position, that is, no four
points of P are cocircular. Then P has a unique Delaunay triangulation. 
71

Chapter 6. Delaunay Triangulations CG 2012

6.6 Every Delaunay Triangulation Maximizes the Smallest Angle

Why are we actually interested in Delaunay triangulations? After all, having empty
circumcircles is not a goal in itself. But it turns out that Delaunay triangulations satisfy
a number of interesting properties. Here we show just one of them.
Recall that when we compared a scan triangulation with a Delaunay triangulation of
the same point set in Figure 6.3, we claimed that the scan triangulation is “ugly” because
it contains many long and skinny triangles. The triangles of the Delaunay triangulation,
at least in this example, look much nicer, that is, much closer to an equilateral triangle.
One way to quantify this “niceness” is to look at the angles that appear in a triangulation:
If all angles are large, then all triangles are reasonably close to an equilateral triangle.
Indeed, we will show that Delaunay triangulations maximize the smallest angle among
all triangulations of a given point set. Note that this does not imply that there are no
long and skinny triangles in a Delaunay triangulation. But if there is a long and skinny
triangle in a Delaunay triangulation, then there is an at least as long and skinny triangle
in every triangulation of the point set.
Given a triangulation T of P, consider the lexicographically sorted sequence A(T) =
(α1, α2, . . . , α3m) of interior angles, where m is the number of triangles (we have already
remarked earlier that m is a function of P only and does not depend on T). Being sorted
lexicographically means that α1 ⩽ α2 ⩽ · · · ⩽ α3m. Let T, T ′ be two triangulations of P.
We say that A(T) < A(T ′) if there exists some i for which αi < α ′
i and αj = α ′
j, for all
j < i.

Theorem 6.19 Let P ⊆ R
2 be a ﬁnite set of points in general position (not all collinear
and no four cocircular). Let D∗ be the unique Delaunay triangulation of P, and let
T be any triangulation of P. Then A(T) ⩽ A(D∗).

In particular, D∗ maximizes the smallest angle among all triangulations of P.

α1
α4

α2α1
α3
α2

α4 α3

p

q
 r
 s

(a) Four cocircular points and the
induced eight angles.
 α1
α4
α2α1
α3
α2
 α4 α3

(b) The situation before a ﬂip.

Figure 6.13: Angle-optimality of Delaunay triangulations.

72

CG 2012 6.6. Every Delaunay Triangulation Maximizes the Smallest Angle

Proof. We know that T can be transformed into D∗ through the Lawson ﬂip algorithm,
and we are done if we can show that each such ﬂip lexicographically increases the sorted
angle sequence. A ﬂip replaces six interior angles by six other interior angles, and we
will actually show that the smallest of the six angles strictly increases under the ﬂip.
This implies that the whole angle sequence increases lexicographically.
Let us ﬁrst look at the situation of four cocircular points, see Figure 6.13a. In this
situation, the inscribed angle theorem (a generalization of Thales’ Theorem, stated
below as Theorem 6.20) tells us that the eight depicted angles come in four equal pairs.
For instance, the angles labeled α1 at s and r are angles on the same side of the chord
pq of the circle.
In Figure 6.13b, we have the situation in which we perform a Lawson ﬂip (replacing
the solid with the dashed diagonal). By the symbol α (α, respectively) we denote an
angle strictly smaller (larger, respectively) than α. Here are the six angles before the
ﬂip:
 α1 + α2, α3, α4, α1, α2, α3 + α4.

After the ﬂip, we have

α1, α2, α3, α4, α1 + α4, α2 + α3.

Now, for every angle after the ﬂip there is at least one smaller angle before the ﬂip:

α1 > α1,
α2 > α2,
α3 > α3,
α4 > α4,
α1 + α4 > α4,
α2 + α3 > α3.

It follows that the smallest angle strictly increases. 
Theorem 6.20 (Inscribed Angle Theorem) Let C be a circle with center c and positive
radius and p, q ∈ C. Then the angle\prq mod π = 1
2\pcq is the same, for all r ∈ C.

Proof. Without loss of generality we may assume that c is located to the left of or on
the oriented line pq.
 73

Chapter 6. Delaunay Triangulations CG 2012

p
 q

r
 s
 t

C
 2θ
 θ

θ
 π − θ

c
 π + θ

Figure 6.14: The Inscribed Angle Theorem with θ :=\prq.

Consider ﬁrst the case that the triangle ∆ = pqr
contains c. Then ∆ can be partitioned into three trian-
gles: pcr, qcr, and cpq. All three triangles are isosce-
les, because two sides of each form the radius of C. De-
note α =\prc, β =\crq, γ =\cpq, and δ =\pcq
(see the ﬁgure shown to the right). The angles we are
interested in are θ =\prq = α + β and δ, for which
we have to show that δ = 2θ.
Indeed, the angle sum in ∆ is π = 2(α + β + γ)
and the angle sum in the triangle cpq is π = δ + 2γ.
Combining both yields δ = 2(α + β) = 2θ.
 p
 q

r
 C

δ

α
 c

β
 β

α γ γ

Next suppose that pqcr are in convex position and
r is to the left of or on the oriented line pq. Without
loss of generality let r be to the left of or on the oriented
line qc. (The case that r lies to the right of or on the
oriented line pc is symmetric.) Deﬁne α, β, γ, δ as
above and observe that θ = α − β. Again have to show
that δ = 2θ.
The angle sum in the triangle cpq is π = δ + 2γ
and the angle sum in the triangle rpq is π = (α − β) +
α + γ + (γ − β) = 2(α + γ − β). Combining both yields
δ = π − 2γ = 2(α − β) = 2θ. p
 q

r
 C

δ
c

α

α β
 γ
γ
 β

74

CG 2012 6.7. Constrained Triangulations

It remains to consider the case that r is to the right of the
oriented line pq.
Consider the point r ′ that is antipodal to r on C, and the
quadrilateral Q = prqr ′. We are interested in the angle φ of
Q at r. By Thales’ Theorem the inner angles of Q at p and q
are both π/2. Hence the angle sum of Q is 2π = θ + φ + 2π/2
and so φ = π − θ.
 p q

r
 C

c

θ
 φ

π
2
 r ′
 π
2 
What happens in the case where the Delaunay triangulation is not unique? The
following still holds.

Theorem 6.21 Let P ⊆ R
2 be a ﬁnite set of points, not all on a line. Every Delaunay
triangulation D of P maximizes the smallest angle among all triangulations T of P.

Proof. Let D be some Delaunay triangulation of P. We inﬁnitesimally perturb the points
in P such that no four are on a common circle anymore. Then the Delaunay triangulation
becomes unique (Corollary 6.18). Starting from D, we keep applying Lawson ﬂips until
we reach the unique Delaunay triangulation D∗ of the perturbed point set. Now we
examine this sequence of ﬂips on the original unperturbed point set. All these ﬂips must
involve four cocircular points (only in the cocircular case, an inﬁnitesimal perturbation
can change “good” edges into “bad” edges that still need to be ﬂipped). But as Figure 6.13
(a) easily implies, such a “degenerate” ﬂip does not change the smallest of the six involved
angles. It follows that D and D∗ have the same smallest angle, and since D∗ maximizes
the smallest angle among all triangulations T (Theorem 6.19), so does D. 
6.7 Constrained Triangulations

Sometimes one would like to have a Delaunay triangulation, but certain edges are already
prescribed, for example, a Delaunay triangulation of a simple polygon. Of course, one
cannot expect to be able to get a proper Delaunay triangulation where all triangles satisfy
the empty circle property. But it is possible to obtain some triangulation that comes as
close as possible to a proper Delaunay triangulation, given that we are forced to include
the edges in E. Such a triangulation is called a constrained Delaunay triangulation, a
formal deﬁnition of which follows.
Let P ⊆ R
2 be a ﬁnite point set and G = (P, E) a geometric graph with vertex set
P (we consider the edges e ∈ E as line segments). A triangulation T of P respects G if
it contains all segments e ∈ E. A triangulation T of P that respects G is said to be a
constrained Delaunay triangulation of P with respect to G if the following holds for
every triangle ∆ of T:
 75

Chapter 6. Delaunay Triangulations CG 2012

The circumcircle of ∆ contains only points q ∈ P in its interior that are not
visible from the interior of ∆. A point q ∈ P is visible from the interior of
∆ if there exists a point p in the interior of ∆ such that the line segment pq
does not intersect any segment e ∈ E. We can thus imagine the line segments
of E as “blocking the view”.

For illustration, consider the simple polygon and its constrained Delaunay triangula-
tion shown in Figure 6.15. The circumcircle of the shaded triangle ∆ contains a whole
other triangle in its interior. But these points cannot be seen from ∆
◦, because all
possible connecting line segments intersect the blocking polygon edge e of ∆.

∆ e

Figure 6.15: Constrained Delaunay triangulation of a simple polygon.

Theorem 6.22 For every ﬁnite point set P and every plane graph G = (P, E), there
exists a constrained Delaunay triangulation of P with respect to G.

Exercise 6.23 Prove Theorem 6.22. Also describe a polynomial algorithm to construct
such a triangulation.

Questions

20. What is a triangulation? Provide the deﬁnition and prove a basic property: every
triangulation with the same set of vertices and the same outer face has the same
number of triangles.

21. What is a triangulation of a point set? Give a precise deﬁnition.

76

CG 2012 6.7. Constrained Triangulations

22. Does every point set (not all points on a common line) have a triangulation?
You may, for example, argue with the scan triangulation.

23. What is a Delaunay triangulation of a set of points? Give a precise deﬁnition.

24. What is the Delaunay graph of a point set? Give a precise deﬁnition and a
characterization.

25. How can you prove that every set of points (not all on a common line) has a
Delaunay triangulation? You can for example sketch the Lawson ﬂip algorithm
and the Lifting Map, and use these to show the existence.

26. When is the Delaunay triangulation of a point set unique? Show that general
position is a suﬃcient condition. Is it also necessary?

27. What can you say about the “quality” of a Delaunay triangulation? Prove
that every Delaunay triangulation maximizes the smallest interior angle in the
triangulation, among the set of all triangulations of the same point set.

77

Chapter 7

Delaunay Triangulation: Incremental
Construction

In the last lecture, we have learned about the Lawson ﬂip algorithm that computes a
Delaunay triangulation of a given n-point set P ⊆ R
2 with O(n
2) Lawson ﬂips. One can
actually implement this algorithm to run in O(n
2) time, and there are point sets where
it may take Ω(n
2) ﬂips.
In this lecture, we will discuss a diﬀerent algorithm. The ﬁnal goal is to show that
this algorithm can be implemented to run in O(n log n) time; this lecture, however, is
concerned only with the correctness of the algorithm. Throughout the lecture we assume
that P is in general position (no 3 points on a line, no 4 points on a common circle), so
that the Delaunay triangulation is unique (Corollary 6.18). There are techniques to deal
with non-general position, but we don’t discuss them here.

7.1 Incremental construction

The idea is to build the Delaunay triangulation of P by inserting one point after another.
We always maintain the Delaunay triangulation of the point set R inserted so far, and
when the next point s comes along, we simply update the triangulation to the Delaunay
triangulation of R ∪ {s}. Let DT(R) denote the Delaunay triangulation of R ⊆ P.
To avoid special cases, we enhance the point set P with three artiﬁcial points “far
out”. The convex hull of the resulting point set is a triangle; later, we can simply remove
the extra points and their incident edges to obtain DT(P). The incremental algorithm
starts oﬀ with the Delaunay triangulation of the three artiﬁcial points which consists
of one big triangle enclosing all other points. (In our ﬁgures, we suppress the far-away
points, since they are merely a technicality.)
Now assume that we have already built DT(R), and we next insert s ∈ P \ R. Here is
the outline of the update step.

1. Find the triangle ∆ = ∆(p, q, r) of DT(R) that contains s, and replace it with the
three triangles resulting from connecting s with all three vertices p, q, r; see Figure

79

Chapter 7. Delaunay Triangulation: Incremental Construction CG 2012

s

∆

Figure 7.1: Inserting s into DT(R): Step 1

7.1. We now have a triangulation T of R ∪ {s}.

2. Perform Lawson ﬂips on T until DT(R ∪ {s}) is obtained; see Figure 7.2

s

∆
 s

∆

s

∆
 s

∆

Figure 7.2: Inserting s into DT(R): Step 2

How to organize the Lawson ﬂips. The Lawson ﬂips can be organized quite systematically,
since we always know the candidates for “bad” edges that may still have to be ﬂipped.
Initially (after step 1), only the three edges of ∆ can be bad, since these are the only
edges for which an incident triangle has changed (by inserting s in Step 1). Each of
the three new edges is good, since the 4 vertices of its two incident triangles are not in
convex position.
Now we have the following invariant (part (a) certainly holds in the ﬁrst ﬂip):

80

CG 2012 7.1. Incremental construction

(a) In every ﬂip, the convex quadrilateral Q in which the ﬂip happens has exactly two
edges incident to s, and the ﬂip generates a new edge incident to s.

(b) Only the two edges of Q that are not incident to s can become bad through the
ﬂip.

We will prove part (b) in the next lemma. The invariant then follows since (b) entails
(a) in the next ﬂip. This means that we can maintain a queue of potentially bad edges
that we process in turn. A good edge will simply be removed from the queue, and a bad
edge will be ﬂipped and replaced according to (b) with two new edges in the queue. In
this way, we never ﬂip edges incident to s; the next lemma proves that this is correct
and at the same time establishes part (b) of the invariant.

Lemma 7.1 Every edge incident to s that is created during the update is an edge of
the Delaunay graph of R ∪ {s} and thus an edge that will be in DT(R ∪ {s}). It easily
follows that edges incident to s will never become bad during the update step.1

Proof. Let us consider one of the ﬁrst three new edges, sp, say. Since the triangle
∆ has a circumcircle C strictly containing only s (∆ is in DT(R)), we can shrink that
circumcircle to a circle C ′ through s and p with no interior points, see Figure 7.3 (a).
This proves that sp is in the Delaunay graph. If st is an edge created by a ﬂip, a similar
argument works. The ﬂip destroys exactly one triangle ∆ of DT(R). Its circumcircle C
contains s only, and shrinking it yields an empty circle C ′ through s and t. Thus, st is
in the Delaunay graph also in this case. 
C

C'
 r

p

q s ∆

(a) New edge sp incident
to s created in Step 1
 C

s

C' ∆

t

(b) New edge st incident
to s created in Step 2

Figure 7.3: Newly created edges incident to s are in the Delaunay graph

1If such an edge was bad, it could be ﬂipped, but then it would be “gone forever” according to the
lifting map interpretation from the previous lecture.

81

Chapter 7. Delaunay Triangulation: Incremental Construction CG 2012

s

∆
 s

∆

s s s

Figure 7.4: The history graph: one triangle gets replaced by three triangles

7.2 The History Graph

What can we say about the performance of the incremental construction? Not much yet.
First of all, we did not specify how we ﬁnd the triangle ∆ of DT(R) that contains the
point s to be inserted. Doing this in the obvious way (checking all triangles) is not good,
since already the ﬁnd steps would then amount to O(n
2) work throughout the whole
algorithm. Here is a smarter method, based on the history graph.

Deﬁnition 7.2 Given R ⊆ P (regarded as a sequence that reﬂects the insertion order),
the history graph of R is a directed acyclic graph whose vertices are all triangles
that have ever been created during the incremental construction of DT(R). There
is a directed edge from ∆ to ∆ ′ whenever ∆ has been destroyed during an insertion
step, ∆ ′ has been created during the same insertion step, and ∆ overlaps with ∆ ′

in its interior.

It follows that the history graph contains triangles of outdegrees 3, 2 and 0. The ones of
outdegree 0 are clearly the triangles of DT(R).
The triangles of outdegree 3 are the ones that have been destroyed during Step 1 of
an insertion. For each such triangle ∆, its three outneighbors are the three new triangles
that have replaced it, see Figure 7.4.
The triangles of outdegree 2 are the ones that have been destroyed during Step 2 of
an insertion. For each such triangle ∆, its two outneighbors are the two new triangles
created during the ﬂip that has destroyed ∆, see Figure 7.5.
The history graph can be built during the incremental construction at asymptotically
no extra cost; but it may need extra space since it keeps all triangles ever created. Given
the history graph, we can search for the triangle ∆ of DT(R) that contains s, as follows.
We start from the big triangle spanned by the three far-away points; this one certainly

82

CG 2012 7.3. The structural change

s
 s

s s

Figure 7.5: The history graph: two triangles get replaced by two triangles

contains s. Then we follow a directed path in the history graph. If the current triangle
still has outneighbors, we ﬁnd the unique outneighbor containing s and continue the
search with this neighbor. If the current triangle has no outneighbors anymore, it is in
DT(R) and contains s—we are done.

Types of triangles in the history graph. After each insertion of a point s, several triangles are
created and added to the history graph. It is important to note that these triangles come
in two types: Some of them are valid Delaunay triangles of R∪{s}, and they survive to the
next stage of the incremental construction. Other triangles are immediately destroyed
by subsequent Lawson ﬂips, because they are not Delaunay triangles of R ∪ {s}. These
“ephemeral" triangles will give us some headache (though not much) in the algorithm’s
analysis in the next chapter.
Note that, whenever a Lawson ﬂip is performed, of the two triangles destroyed one
of them is always a “valid" triangle from a previous iteration, and the other one is an
“ephemeral" triangle that was created at this iteration. The ephemeral triangle is always
the one that has s, the newly inserted point, as a vertex.

7.3 The structural change

Concerning the actual update (Steps 1 and 2), we can make the following

Observation 7.3 Given DT(R) and the triangle ∆ of DT(R) that contains s, we can
build DT(R ∪ {s}) in time proportional to the degree of s in DT(R ∪ {s}), which is the
number of triangles of DT(R ∪ {s}) containing s.

Indeed, since every ﬂip generates exactly one new triangle incident to s, the number
of ﬂips is the degree of s minus three. Step 1 of the update takes constant time, and

83

Chapter 7. Delaunay Triangulation: Incremental Construction CG 2012

since also every ﬂip can be implemented in constant time, the observation follows.
In the next lecture, we will show that a clever insertion order guarantees that the
search paths traversed in the history graph are short, and that the structural change (the
number of new triangles) is small. This will then give us the O(n log n) algorithm.

Exercise 7.4 For a sequence of n pairwise distinct numbers y1, . . . , yn consider the se-
quence of pairs (min{y1, . . . , yi}, max{y1, . . . , yi})i=0,1,...,n (min ∅ := +∞, max ∅ := −∞).
How often do these pairs change in expectation if the sequence is permuted ran-
domly, each permutation appearing with the same probability? Determine the ex-
pected value.

Questions

28. Describe the algorithm for the incremental construction of DT(P): how do we
ﬁnd the triangle containing the point s to be inserted into DT(R)? How do we
transform DT(R) into DT(R ∪ {s})? How many steps does the latter transformation
take, in terms of DT(R ∪ {s})?

29. What are the two types of triangles that the history graph contains?

84

Chapter 8

The Conﬁguration Space Framework

In Section 7.1, we have discussed the incremental construction of the Delaunay trian-
gulation of a ﬁnite point set. In this lecture, we want to analyze the runtime of this
algorithm if the insertion order is chosen uniformly at random among all insertion or-
ders. We will do the analysis not directly for the problem of constructing the Delaunay
triangulation but in a somewhat more abstract framework, with the goal of reusing the
analysis for other problems.
Throughout this lecture, we again assume general position: no three points on a line,
no four on a circle.

8.1 The Delaunay triangulation — an abstract view

The incremental construction constructs and destroys triangles. In this section, we want
to take a closer look at these triangles, and we want to understand exactly when a triangle
is “there”.

Lemma 8.1 Given three points p, q, r ∈ R, the triangle ∆(p, q, r) with vertices p, q, r
is a triangle of DT(R) if and only if the circumcircle of ∆(p, q, r) is empty of points
from R.

Proof. The “only if” direction follows from the deﬁnition of a Delaunay triangulation
(Deﬁnition 6.8). The “if” direction is a consequence of general position and Lemma 6.17:
if the circumcircle C of ∆(p, q, r) is empty of points from R, then all the three edges
pq, qr, pr are easily seen to be in the Delaunay graph of R. C being empty also implies
that the triangle ∆(p, q, r) is empty, and hence it forms a triangle of DT(R). 
Next we develop a somewhat more abstract view of DT(R).

Deﬁnition 8.2

(i) For all p, q, r ∈ P, the triangle ∆ = ∆(p, q, r) is called a conﬁguration. The
points p, q and r are called the deﬁning elements of ∆.

85

Chapter 8. The Conﬁguration Space Framework CG 2012

(ii) A conﬁguration ∆ is in conﬂict with a point s ∈ P if s is strictly inside the
circumcircle of ∆. In this case, the pair (∆, s) is called a conﬂict.

(iii) A conﬁguration ∆ is called active w.r.t. R ⊆ P if (a) the deﬁning elements of
∆ are in R, and (b) if ∆ is not in conﬂict with any element of R.

According to this deﬁnition and Lemma 8.1, DT(R) consists of exactly the conﬁgu-
rations that are active w.r.t. R. Moreover, if we consider DT(R) and DT(R ∪ {s}) as sets
of conﬁgurations, we can exactly say how these two sets diﬀer.
There are the conﬁgurations in DT(R) that are not in conﬂict with s. These conﬁg-
urations are still in DT(R ∪ {s}). The conﬁgurations of DT(R) that are in conﬂict with
s will be removed when going from R to R ∪ {s}. Finally, DT(R ∪ {s}) contains some new
conﬁgurations, all of which must have s in their deﬁning set. According to Lemma 8.1,
it cannot happen that we get a new conﬁguration without s in its deﬁning set, as such
a conﬁguration would have been present in DT(R) already.

8.2 Conﬁguration Spaces

Here is the abstract framework that generalizes the previous conﬁguration view of the
Delaunay triangulation.

Deﬁnition 8.3 Let X (the ground set) and Π (the set of conﬁgurations) be ﬁnite sets.
Furthermore, let

D : Π → 2X

be a function that assigns to every conﬁguration ∆ a set of deﬁning elements D(∆).
We assume that only a constant number of conﬁgurations have the same deﬁning
elements. Let

K : Π → 2X

be a function that assigns to every conﬁguration ∆ a set of elements in conﬂict with
∆ (the “killer” elements). We stipulate that D(∆) ∩ K(∆) = ∅ for all ∆ ∈ Π.
Then the quadruple S = (X, Π, D, K) is called a conﬁguration space. The number

d = d(S) := max
∆∈Π |D(∆)|

is called the dimension of S.
Given R ⊆ X, a conﬁguration ∆ is called active w.r.t. R if

D(∆) ⊆ R and K(∆) ∩ R = ∅,

i.e. if all deﬁning elements are in R but no element of R is in conﬂict with ∆. The
set of active conﬁgurations w.r.t. R is denoted by TS(R), where we drop the subscript
if the conﬁguration space is clear from the context.

86

CG 2012 8.3. Expected structural change

In case of the Delaunay triangulation, we set X = P (the input point set). Π consists
of all triangles ∆ = ∆(p, q, r) spanned by three points p, q, r ∈ X ∪ {a, b, c}, where a, b, c
are the three artiﬁcial far-away points. We set D(∆) := {p, q, r}∩X. The set K(∆) consists
of all points strictly inside the circumcircle of ∆. The resulting conﬁguration space has
dimension 3, and the technical condition that only a constant number of conﬁgurations
share the deﬁning set is satisﬁed as well. In fact, every set of three points deﬁnes a
unique conﬁguration (triangle) in this case. A set of two points or one point deﬁnes
three triangles (we have to add one or two artiﬁcial points which can be done in three
ways). The empty set deﬁnes one triangle, the initial triangle consisting of just the three
artiﬁcial points.
Furthermore, in the setting of the Delaunay triangulation, a conﬁguration is active
w.r.t. R if it is in DT(R ∪ {a, b, c}), i.e. we have T(R) = DT(R ∪ {a, b, c}).

8.3 Expected structural change

Let us ﬁx a conﬁguration space S = (X, Π, D, K) for the remainder of this lecture. We
can also interpret the incremental construction in S. Given R ⊆ X and s ∈ X \ R, we
want to update T(R) to T(R ∪ {s}). What is the number of new conﬁgurations that arise
during this step? For the case of Delaunay triangulations, this is the relevant question
when we want to bound the number of Lawson ﬂips during one update step, since this
number is exactly the number of new conﬁgurations minus three.
Here is the general picture.

Deﬁnition 8.4 For Q ⊆ X and s ∈ Q, deg(s, Q) is deﬁned as the number of conﬁgura-
tions of T(Q) that have s in their deﬁning set.

With this, we can say that the number of new conﬁgurations in going from T(R) to
T(R∪{s}) is precisely deg(s, R∪{s}), since the new conﬁgurations are by deﬁnition exactly
the ones that have s in their deﬁning set.
Now the random insertion order comes in for the ﬁrst time: what is

E(deg(s, R ∪ {s})),

averaged over all insertion orders? In such a random insertion order, R is a random r-
element subset of X (when we are about to insert the (r+1)-st element), and s is a random
element of X \ R. Let Tr be the “random variable” for the set of active conﬁgurations
after r insertion steps.
It seems hard to average over all R, but there is a trick: we make a movie of the
randomized incremental construction, and then we watch the movie backwards. What
we see is elements of X being deleted one after another, again in random order. This is
due to the fact that the reverse of a random order is also random. At the point where the
(r + 1)-st element is being deleted, it is going to be a random element s of the currently

87

Chapter 8. The Conﬁguration Space Framework CG 2012

present (r + 1)-element subset Q. For ﬁxed Q, the expected degree of s is simply the
average degree of an element in Q which is

1
r + 1
 ∑

s∈Q deg(s, Q) ⩽ d
r + 1|T(Q)|,

since the sum counts every conﬁguration of T(Q) at most d times. Since Q is a random
(r + 1)-element subset, we get

E(deg(s, R ∪ {s})) ⩽ d
r + 1 tr+1,

where tr+1 is deﬁned as the expected number of active conﬁgurations w.r.t. a random
(r + 1)-element set.
Here is a more formal derivation that does not use the backwards movie view. It
exploits the bijection

(R, s) ↦→ (R ∪ {s}
︸ ︷︷ ︸
Q , s)

between pairs (R, s) with |R| = r and s /∈ R and pairs (Q, s) with |Q| = r + 1 and s ∈ Q.
Let n = |X|.

E(deg(s, R ∪ {s})) = 1
(n
r) ∑

R⊆X,|R|=r
 1
n − r
 ∑

s∈X\R deg(s, R ∪ {s})

= 1
(n
r) ∑

Q⊆X,|Q|=r+1
 1
n − r
 ∑

s∈Q deg(s, Q)

= 1
( n
r+1) ∑

Q⊆X,|Q|=r+1
 ( n
r+1)

(n
r) 1
n − r
 ∑

s∈Q deg(s, Q)

= 1
( n
r+1) ∑

Q⊆X,|Q|=r+1
 1
r + 1
 ∑

s∈Q deg(s, Q)

⩽ 1
( n
r+1) ∑

Q⊆X,|Q|=r+1
 d
r + 1 |T(Q)|

= d
r + 1 tr+1.

Thus, the expected number of new conﬁgurations in going from Tr to Tr+1 is bounded
by
 d
r + 1 tr+1,
 88

CG 2012 8.4. Bounding location costs by conﬂict counting

where tr+1 is the expected size of Tr+1.
What do we get for Delaunay triangulations? We have d = 3 and tr+1 ⩽ 2(r + 4) − 4
(the maximum number of triangles in a triangulation of r + 4 points). Hence,

E(deg(s, R ∪ {s})) ⩽ 6r + 12
r + 1 ≈ 6.

This means that on average, ≈ 3 Lawson ﬂips are done to update DTr (the Delaunay
triangulation after r insertion steps) to DTr+1. Over the whole algorithm, the expected
update cost is thus O(n).

8.4 Bounding location costs by conﬂict counting

Before we can even update DTr to DTr+1 during the incremental construction of the
Delaunay triangulation, we need to locate the new point s in DTr, meaning that we need
to ﬁnd the triangle that contains s. We have done this with the history graph: During
the insertion of s we “visit" a sequence of triangles from the history graph, each of which
contains s and was created at some previous iteration k < r.
However, some of these visited triangles are “ephemeral" triangles (recall the discus-
sion at the end of Section 7.2), and they present a problem to the generic analysis we
want to perform. Therefore, we will do a charging scheme, so that all triangles charged
are valid Delaunay triangles.
The charging scheme is as follows: If the visited triangle ∆ is a valid Delaunay triangle
(from some previous iteration), then we simply charge the visit of ∆ during the insertion
of s to the triangle-point pair (∆, s).
If, on the other hand, ∆ is an “ephemeral" triangle, then ∆ was destroyed, together
with some neighbor ∆ ′, by a Lawson ﬂip into another pair ∆ ′′, ∆ ′′′. Note that this
neighbor ∆ ′ was a valid triangle. Thus, in this case we charge the visit of ∆ during the
insertion of s to the pair (∆ ′, s). Observe that s is contained in the circumcircle of ∆ ′,
so s is in conﬂict with ∆ ′.
This way, we have charged each visit to a triangle in the history graph to a triangle-
point pair of the form (∆, s), such that ∆ is in conﬂict with s. Furthermore, it is easy to
see that no such pair gets charged more than once.
We deﬁne the notion of a conﬂict in general:

Deﬁnition 8.5 A conﬂict is a conﬁguration-element pair (∆, s) where ∆ ∈ Tr for some
r and s ∈ K(∆).

Thus, the running time of the Delaunay algorithm is proportional to the number of
conﬂicts. We now proceed to derive a bound on the expected number of conﬂicts in the
generic conﬁguration-space framework.
 89

Chapter 8. The Conﬁguration Space Framework CG 2012

8.5 Expected number of conﬂicts

Since every conﬁguration involved in a conﬂict has been created in some step r (we
include step 0), the total number of conﬂicts is

n∑

r=0
 ∑

∆∈Tr\Tr−1 |K(∆)|,

where T−1 := ∅. T0 consists of constantly many conﬁgurations only (namely those where
the set of deﬁning elements is the empty set), each of which is in conﬂict with at most
all elements; moreover, no conﬂict is created in step n. Hence,

n∑

r=0
 ∑

∆∈Tr\Tr−1 |K(∆)| = O(n) +
 n−1∑

r=1
 ∑

∆∈Tr\Tr−1 |K(∆)|,

and we will bound the latter quantity. Let

K(r) := ∑

∆∈Tr\Tr−1 |K(∆)|, r = 1, . . . , n − 1.

and k(r) := E(K(r)) the expected number of conﬂicts created in step r.

Bounding k(r). We know that Tr arises from a random r-element set R. Fixing R, the
backwards movie view tells us that Tr−1 arises from Tr by deleting a random element s
of R. Thus,

k(r) = 1
(n
r) ∑

R⊆X,|R|=r
 1
r
 ∑

s∈R
 ∑

∆∈T(R)\T(R\{s}) |K(∆)|

= 1
(n
r) ∑

R⊆X,|R|=r
 1
r
 ∑

s∈R
 ∑

∆∈T(R),s∈D(∆) |K(∆)|

⩽ 1
(n
r) ∑

R⊆X,|R|=r
 d
r
 ∑

∆∈T(R) |K(∆)|,

since in the sum over s ∈ R, every conﬁguration is counted at most d times. Since we
can rewrite
∑

∆∈T(R) |K(∆)| = ∑

y∈X\R |{∆ ∈ T(R) : y ∈ K(∆)}|,

we thus have

k(r) ⩽ 1
(
n
r) ∑

R⊆X,|R|=r
 d
r
 ∑

y∈X\R |{∆ ∈ T(R) : y ∈ K(∆)}|.

To estimate this further, here is a simple but crucial

90

CG 2012 8.5. Expected number of conﬂicts

Lemma 8.6 The conﬁgurations in T(R) that are not in conﬂict with y are the conﬁg-
urations in T(R ∪ {y}) that do not have y in their deﬁning set; in formulas:

|T(R)| − |{∆ ∈ T(R) : y ∈ K(∆)}| = |T(R ∪ {y})| − deg(y, R ∪ {y}).

The proof is a direct consequence of the deﬁnitions: every conﬁguration in T(R) not in
conﬂict with y is by deﬁnition still present in T(R ∪ {y}) and still does not have y in
its deﬁning set. And a conﬁguration in T(R ∪ {y}) with y not in its deﬁning set is by
deﬁnition already present in T(R) and already there not in conﬂict with y.

The lemma implies that

k(r) ⩽ k1(r) − k2(r) + k3(r),

where

k1(r) = 1
(n
r) ∑

R⊆X,|R|=r
 d
r
 ∑

y∈X\R |T(R)|,

k2(r) = 1
(n
r) ∑

R⊆X,|R|=r
 d
r
 ∑

y∈X\R |T(R ∪ {y})|,

k3(r) = 1
(n
r) ∑

R⊆X,|R|=r
 d
r
 ∑

y∈X\R deg(y, R ∪ {y}).

Estimating k1(r). This is really simple.

k1(r) = 1
(
n
r) ∑

R⊆X,|R|=r
 d
r
 ∑

y∈X\R |T(R)|

= 1
(
n
r) ∑

R⊆X,|R|=r
 d
r (n − r)|T(R)|

= d
r (n − r)tr.
 91

Chapter 8. The Conﬁguration Space Framework CG 2012

Estimating k2(r). For this, we need to employ our earlier (R, y) ↦→ (R ∪ {y}, y) bijection
again.

k2(r) = 1
(
n
r) ∑

R⊆X,|R|=r
 d
r
 ∑

y∈X\R |T(R ∪ {y})|

= 1
(
n
r) ∑

Q⊆X,|Q|=r+1
 d
r
 ∑

y∈Q |T(Q)|

= 1
( n
r+1) ∑

Q⊆X,|Q|=r+1
 ( n
r+1)

(
n
r) d
r (r + 1)|T(Q)|

= 1
( n
r+1) ∑

Q⊆X,|Q|=r+1
 d
r (n − r)|T(Q)|

= d
r (n − r)tr+1

= d
r + 1 (n − (r + 1))tr+1 + dn
r(r + 1)tr+1

= k1(r + 1) + dn
r(r + 1) tr+1.

Estimating k3(r). This is similar to k2(r) and in addition uses a fact that we have em-
ployed before: ∑
y∈Q deg(y, Q) ⩽ d|T(Q)|.

k3(r) = 1
(
n
r) ∑

R⊆X,|R|=r
 d
r
 ∑

y∈X\R deg(y, R ∪ {y})

= 1
(
n
r) ∑

Q⊆X,|Q|=r+1
 d
r
 ∑

y∈Q deg(y, Q)

⩽ 1
(
n
r) ∑

Q⊆X,|Q|=r+1
 d
2

r |T(Q)|

= 1
( n
r+1) ∑

Q⊆X,|Q|=r+1
 ( n
r+1)

(
n
r) d
2

r |T(Q)|

= 1
( n
r+1) ∑

Q⊆X,|Q|=r+1
 n − r
r + 1 · d
2

r |T(Q)|

= d
2

r(r + 1) (n − r)tr+1

= d
2n
r(r + 1) tr+1 − d
2

r + 1 tr+1.
 92

CG 2012 8.5. Expected number of conﬂicts

Summing up. Let us recapitulate: the overall expected number of conﬂicts is O(n) plus

n−1∑

r=1 k(r) =
 n−1∑

r=1(k1(r) − k2(r) + k3(r)).

Using our previous estimates, k1(2), . . . , k1(n − 1) are canceled by the ﬁrst terms of
k2(1), . . . , k2(n − 2). The second term of k2(r) can be combined with the ﬁrst term of
k3(r), so that we get

n−1∑

r=1(k1(r) − k2(r) + k3(r)) ⩽ k1(1) − k1(n)
︸ ︷︷ ︸
=0 +n
 n−1∑

r=1
 d(d − 1)
r(r + 1) tr+1 −
 n−1∑

r=1
 d
2

r + 1 tr+1

⩽ d(n − 1)t1 + d(d − 1)n
 n−1∑

r=1
 tr+1
r(r + 1)

= O
 (

d
2n
 n∑

r=1
 tr
r2
 )
 .

The Delaunay case. We have argued that the expected number of conﬂicts asymptotically
bounds the expected total location cost over all insertion steps. The previous equation
tells us that this cost is proportional to O(n) plus

O
 (

9n
 n∑

r=1
 2(r + 4) − 4
r2
 )
 = O
 (
n
 n∑

r=1
 1
r
 )
 = O(n log n).

Here,
 n∑

r=1
 1
r =: Hn

is the n-th Harmonic Number which is known to be approximately ln n.
By going through the abstract framework of conﬁguration spaces, we have thus ana-
lyzed the randomized incremental construction of the Delaunay triangulation of n points.
According to Section 8.3, the expected update cost itself is only O(n). The steps dom-
inating the runtime are the location steps via the history graph. According to Section
8.5, all history graph searches (whose number is proportional to the number of conﬂicts)
can be performed in expected time O(n log n), and this then also bounds the space
requirements of the algorithm.

Exercise 8.7 Design and analyze a sorting algorithm based on randomized incremen-
tal construction in conﬁguration spaces. The input is a set S of numbers, and the
output should be the sorted sequence (in increasing order).

93

Chapter 8. The Conﬁguration Space Framework CG 2012

a) Deﬁne an appropriate conﬁguration space for the problem! In particular, the
set of active conﬁgurations w.r.t. S should represent the desired sorted se-
quence.

b) Provide an eﬃcient implementation of the incremental construction algo-
rithm. “Eﬃcient” means that the runtime of the algorithm is asymptotically
dominated by the number of conﬂicts.

c) What is the expected number of conﬂicts (and thus the asymptotic runtime of
your sorting algorithm) for a set S of n numbers?

Questions

30. What is a conﬁguration space? Give a precise deﬁnition! What is an active
conﬁguration?

31. How do we get a conﬁguration space from the problem of computing the De-
launay triangulation of a ﬁnite point set?

32. How many new active conﬁgurations do we get on average when inserting the
r-th element? Provide an answer for conﬁguration spaces in general, and for the
special case of the Delaunay triangulation.

33. What is a conﬂict? Provide an answer for conﬁguration spaces in general, and
for the special case of the Delaunay triangulation.

34. Explain why counting the expected number of conﬂicts asymptotically bounds
the cost for the history searches during the randomized incremental construc-
tion of the Delaunay triangulation!

94

Chapter 9

Trapezoidal Maps

In this section, we will see another application of randomized incremental construction
in the abstract conﬁguration space framework. At the same time, this will give us an
eﬃcient algorithm for solving the general problem of point location, as well as a faster
algorithm for computing all intersections between a given set of line segments.

9.1 The Trapezoidal Map

To start with, let us introduce the concept of a trapezoidal map.
We are given a set S = {s1, . . . , sn} of line segments in the plane (not necessarily
disjoint). We make several general position assumptions.
We assume that no two segment endpoints and intersection points have the same
x-coordinate. As an exception, we do allow several segments to share an endpoint. We
also assume that no line segment is vertical, that any two line segments intersect in at
most one point (which is a common endpoint, or a proper crossing), and that no three
line segments have a common point. Finally, we assume that si ⊆ [0, 1]2 for all i (which
can be achieved by scaling the coordinates of the segments accordingly).

Deﬁnition 9.1 The trapezoidal map of S is the partition of [0, 1]2 into vertices, edges,
and faces (called trapezoids), obtained as follows. Every segment endpoint and point
of intersection between segments gets connected by two vertical extensions with the
next feature below and above, where a feature is either another line segment or an
edge of the bounding box [0, 1]2.

Figure 9.1 gives an example.
(The general-position assumptions are made only for convenience and simplicity of
the presentation. The various degeneracies can be handled without too much trouble,
though we will not get into the details.)
The trapezoids of the trapezoidal map are “true” trapezoids (quadrangles with two
parallel vertical sides), and triangles (which may be considered as degenerate trapezoids).

95

Chapter 9. Trapezoidal Maps CG 2012

Figure 9.1: The trapezoidal map of ﬁve line segments (depicted in bold)

9.2 Applications of trapezoidal maps

In this chapter we will see two applications of trapezoidal maps (there are others):

1. Point location: Given a set of n segments in the plane, we want to preprocess them
in order to answer point-location queries: given a point p, return the cell (connected
component of the complement of the segments) that contains p (see Figure 9.2).
This is a more powerful alternative to Kirkpatrick’s algorithm that handles only
triangulations, and which is treated in Section 10.5. The preprocessing constructs
the trapezoidal map of the segments (Figure 9.3) in expected time O(n log n + K),
where K is the number of intersections between the input segments; the query time
will be O(log n) in expectation.

2. Line segment intersection: Given a set of n segments, we will report all segment
intersections in expected time O(n log n + K). This is a faster alternative to the
line-sweep algorithm we saw in Section 4.2, which takes time O((n + K) log n).

9.3 Incremental Construction of the Trapezoidal Map

We can construct the trapezoidal map by inserting the segments one by one, in random
order, always maintaining the trapezoidal map of the segments inserted so far. In order
to perform manipulations eﬃciently, we can represent the current trapezoidal map as a
doubly-connected edge list (see Section 5.2), for example.

96

CG 2012 9.3. Incremental Construction of the Trapezoidal Map

1
 2

3
 4

5

Figure 9.2: The general point location problem deﬁned by a set of (possibly intersect-
ing) line segments. In this example, the segments partition the plane into
5 cells.

Suppose that we have already inserted segments s1, . . . , sr−1, and that the resulting
trapezoidal map Tr−1 looks like in Figure 9.1. Now we insert segment sr (see Figure 9.4).
Here are the four steps that we need to do in order to construct Tr.

1. Find the trapezoid 0 of Tr−1 that contains the left endpoint of sr.

2. Trace sr through Tr−1 until the trapezoid containing the right endpoint of sr is
found. To get from the current trapezoid to the next one, traverse the boundary
of until the edge is found through which sr leaves .

3. Split the trapezoids intersected by sr. A trapezoid may get replaced by two new trapezoids (if sr intersects two vertical extensions of ); three new trapezoids (if sr intersects one vertical extension of ); four new trapezoids (if sr intersects no vertical extension of ).

4. Merge trapezoids by removing parts of vertical extensions that do not belong to Tr
anymore.

Figure 9.5 illustrates the Trace and Split steps. s6 intersects 5 trapezoids, and they
are being split into 3, 3, 4, 3, and 3 trapezoids, respectively.

97

Chapter 9. Trapezoidal Maps CG 2012

1
 2

3
 4

5

Figure 9.3: The trapezoidal map is a reﬁnement of the partition of the plane into
cells. For example, cell 3 is a union of ﬁve trapezoids.

The Merge step is shown in Figure 9.6. In the example, there are two vertical edges
that need to be removed (indicated with a cross) because they come from vertical exten-
sions that are cut oﬀ by the new segment. In both cases, the two trapezoids to the left
and right of the removed edge are being merged into one trapezoid (drawn shaded).

9.4 Using trapezoidal maps for point location

Recall that in the point location problem we want to preprocess a given set S of seg-
ments in order to answer subsequent point-location queries: S partitions the plane into
connected cells and we want to know, given a query point q, to which cell q belongs,
see Figure 9.2.

Note that the trapezoidal map of S is a reﬁnement of the partition of the plane into
cells, in the sense that a cell might be partitioned into several trapezoids, but every
trapezoid belongs to a single cell, see Figure 9.3. Thus, once the trapezoidal map of S is
constructed, we can easily “glue together" trapezoids that touch along their vertical sides,
obtaining the original cells. Then we can answer point-location queries using the same
routine that performs the Find step (whose implementation will be described below).

98

CG 2012 9.5. Analysis of the incremental construction

Figure 9.4: A new segment (dashed) is to be inserted

9.5 Analysis of the incremental construction

In order to analyze the runtime of the incremental construction, we insert the segments
in random order, and we employ the conﬁguration space framework. We also implement
the Find step in such a way that the analysis boils down to conﬂict counting, just as for
the Delaunay triangulation.

9.5.1 Deﬁning The Right Conﬁgurations

Recall that a conﬁguration space is a quadruple S = (X, Π, D, K), where X is the ground
set, Π is the set of conﬁgurations, D is a mapping that assigns to each conﬁguration its
deﬁning elements (“generators”), and K is a mapping that assigns to each conﬁguration
its conﬂict elements (“killers”).
It seems natural to choose X = S, the set of segments, and to deﬁne Π as the set
of all possible trapezoids that could appear in the trapezoidal map of some subset of
segments. Indeed, this satisﬁes one important property of conﬁguration spaces: for each
conﬁguration, the number of generators is constant.

Lemma 9.2 For every trapezoid in the trapezoidal map of R ⊆ S, there exists a set
D ⊆ R of at most four segments, such that is in the trapezoidal map of D.

Proof. By our general position assumption, each non-vertical side of is a subset of a
unique segment in R, and each vertical side of is induced by a unique (left or right)
endpoint, or by the intersection of two unique segments. In the latter case, one of these

99

Chapter 9. Trapezoidal Maps CG 2012

Figure 9.5: The Trace and Split steps

segments also contributes a non-vertical side, and in the former case, we attribute the
endpoint to the “topmost” segment with that (left or right) endpoint. It follows that
there is a set of at most four segments whose trapezoidal map already contains . 
But there is a problem with this deﬁnition of conﬁgurations. Recall that we can apply
the general conﬁguration space analysis only if

(i) the cost of updating Tr−1 to Tr is proportional to the structural change, the
number of conﬁgurations in Tr \ Tr−1; and

(ii) the expected cost of all Find operations during the randomized incremental con-
struction is proportional to the expected number of conﬂicts. (This is the “conﬂict
counting” part.)

Here we see that already (i) fails. During the Trace step, we traverse the boundary of
each trapezoid intersected by sr in order to ﬁnd the next trapezoid. Even if sr intersects
only a small number of trapezoids (so that the structural change is small), the traversals
may take very long. This is due to the fact that a trapezoid can be incident to a large
number of edges. Consider the trapezoid labeled in Figure 9.7. It has many incident
vertical extensions from above. Tracing a segment through such a trapezoid takes time
that we cannot charge to the structural change.
To deal with this, we slightly adapt our notion of conﬁguration.

Deﬁnition 9.3 Let Π be the set of all trapezoids together with at most one incident
vertical edge (“trapezoids with tail”) that appear in the trapezoidal map of some

100

CG 2012 9.5. Analysis of the incremental construction

Figure 9.6: The Merge steps

Figure 9.7: Trapezoids may have arbitrarily large complexity

subset of X = S, see Figure 9.8. A trapezoid without any incident vertical edge is
also considered a trapezoid with tail.

As it turns out, we still have constantly many generators.

Lemma 9.4 For every trapezoid with tail in the trapezoidal map of R ⊆ S, there
exists a set D ⊆ R of at most six segments, such that is in the trapezoidal map
of D.

Proof. We already know from Lemma 9.2 that the trapezoid without tail has at most
4 generators. And since the tail is induced by a unique segment endpoint or by the
intersection of a unique pair of segments, the claim follows. 
Here is the complete speciﬁcation of our conﬁguration space S = (X, Π, D, K).

101

Chapter 9. Trapezoidal Maps CG 2012

Figure 9.8: A trapezoid with tail is a trapezoid together with at most one vertical edge
attached to its upper or its lower segment.

Deﬁnition 9.5 Let X = S be the set of segments, and Π the set of all trapezoids with
tail. For each trapezoid with tail , D( ) is the set of at most 6 generators. K( )
is the set of all segments that intersect in the interior of the trapezoid, or cut oﬀ
some part of the tail, or replace the topmost generator of the left or right side, see
Figure 9.9.

Then S = (X, Π, D, K) is a conﬁguration space of dimension at most 6, by Lemma 9.4.
The only additional property that we need to check is that D( ) ∩ K( ) = ∅ for all
trapezoids with tail, but this is clear since no generator of properly intersects the
trapezoid of or cuts oﬀ part of its tail.

Figure 9.9: A trapezoid with tail is in conﬂict with a segment s (dashed) if s
intersects in the interior of the trapezoid (left), or cuts oﬀ part of the
tail (middle), or is a new topmost segment generating a vertical side.

9.5.2 Update Cost

Now we can argue that the update cost can be bounded by the structural change. We
employ the same trick as for Delaunay triangulations. We prove that the update cost
is in each step r − 1 → r proportional to the number of conﬁgurations that are being
destroyed. Over the whole algorithm, we cannot destroy more conﬁgurations than we
create, so the bound that we get is also a bound in terms of the overall structural change.

102

CG 2012 9.5. Analysis of the incremental construction

Lemma 9.6 In updating Tr−1 to Tr, the steps Trace, Split, and Merge can be performed
in time proportional to the number of trapezoids with tail in Tr−1 \ Tr.

Proof. By deﬁnition, the complexity (number of edges) of a trapezoid is proportional
to the number of trapezoids with tail that share this trapezoid. This means, the cost of
traversing the trapezoid can be charged to the trapezoids with tail containing it, and all
of them will be destroyed (this includes the trapezoids with tail that just change their
left or right generator; in the conﬁguration space, this is also a destruction). This takes
care of the Trace step. The Split and Merge steps can be done within the same asymptotic
time bounds since they can be performed by traversing the boundaries of all intersected
trapezoids a constant number of times each. For eﬃciently doing the manipulations on
the trapezoidal map, we can for example represent it using a doubly-connected edge list. 
We can now employ the general conﬁguration space analysis to bound the expected
structural change throughout the randomized incremental construction; as previously
shown, this asymptotically bounds the expected cost of the Trace, Split, and Merge steps
throughout the algorithm. Let us recall the general bound.

Theorem 9.7 Let S = (X, Π, D, K) be a conﬁguration space of ﬁxed dimension with
|X| = n. The expected number of conﬁgurations that are created throughout the
algorithm is bounded by

O
 ( n∑

r=1
 tr
r
 )
 ,

where tr is the expected size of Tr, the expected number of active conﬁgurations
after r insertion steps.

9.5.3 The History Graph

Here is how we realize the Find step (as well as the point-location queries for our point-
location application). It is a straightforward history graph approach as for Delaunay
triangulations. Every trapezoid that we ever create is a node in the history graph;
whenever a trapezoid is destroyed, we add outgoing edges to its (at most four) successor
trapezoids. Note that trapezoids are destroyed during the steps Split and Merge. In the
latter step, every destroyed trapezoid has only one successor trapezoid, namely the one
it is merged into. It follows that we can prune the nodes of the “ephemeral” trapezoids
that exist only between the Split and Merge steps. What we get is a history graph of
degree at most 4, such that every non-leaf node corresponds to a trapezoid in Tr−1 \ Tr,
for some r.
 103

Chapter 9. Trapezoidal Maps CG 2012

9.5.4 Cost of the Find step

We can use the history graph for point location during the Find step. Given a segment
endpoint p, we start from the bounding box (the unique trapezoid with no generators)
that is certain to contain p. Since for every trapezoid in the history graph, its area is
covered by the at most four successor trapezoids, we can simply traverse the history
graph along directed edges until we reach a leaf that contains p. This leaf corresponds to
the trapezoid of the current trapezoidal map containing p. By the outdegree-4-property,
the cost of the traversal is proportional to the length of the path that we traverse.
Here is the crucial observation that allows us to reduce the analysis of the Find step
to “conﬂict counting”. Note that this is is precisely what we also did for Delaunay
triangulations, except that there, we had to deal explicitly with “ephemeral” triangles.
Recall Deﬁnition 8.5, according to which a conﬂict is a pair ( , s) where is a
trapezoid with tail, contained in some intermediate trapezoidal map, and s ∈ K( ).

Lemma 9.8 During a run of the incremental construction algorithm for the trape-
zoidal map, the total number of history graph nodes traversed during all Find steps
is bounded by the number of conﬂicts during the run.

Proof. Whenever we traverse a node (during insertion of segment sr, say), the node
corresponds to a trapezoid (which we also consider as a trapezoid with tail) in some
set Ts, s < r, such that p ∈ , where p is the left endpoint of the segment sr. We can
therefore uniquely identify this edge with the conﬂict ( , sr). The statement follows. 
Now we can use the conﬁguration space analysis that precisely bounds the expected
number of conﬂicts, and therefore the expected cost of the Find steps over the whole
algorithm. Let us recapitulate the bound.

Theorem 9.9 Let S = (X, Π, D, K) be a conﬁguration space of ﬁxed dimension d with
|X| = n. The expected number of conﬂicts during randomized incremental construc-
tion of Tn is bounded by

O
 (

n
 n∑

r=1
 tr
r2
 )
 ,

where tr is as before the expected size of Tr.

9.5.5 Applying the General Bounds

Let us now apply Theorem 9.7 and Theorem 9.9 to our concrete situation of trapezoidal
maps. What we obviously need to determine for that is the quantity tr, the expected
number of active conﬁgurations after r insertion steps.
Recall that the conﬁgurations are the trapezoids with tail that exist at this point.
The ﬁrst step is easy.
 104

CG 2012 9.5. Analysis of the incremental construction

Observation 9.10 In every trapezoidal map, the number of trapezoids with tail is pro-
portional to the number vertices.

Proof. Every trapezoid with tail that actually has a tail can be charged to the vertex of
the trapezoidal map on the “trapezoid side” of the tail. No vertex can be charged twice
in this way. The trapezoids with no tail are exactly the faces of the trapezoidal map,
and since the trapezoidal map is a planar graph, their number is also proportional to the
number vertices. 
Using this observation, we have therefore reduced the problem of computing tr to the
problem of computing the expected number of vertices in Tr. To count the latter, we
note that every segment endpoint and every segment intersection generates 3 vertices:
one at the point itself, and two where the vertical extensions hit another feature. Here,
we are sweeping the 4 bounding box vertices under the rug.

Observation 9.11 In every trapezoidal map of r segments, the number of vertices is

6r + 3k,

where k is the number of pairwise intersections between the r segments.

So far, we have not used the fact that we have a random insertion order, but this
comes next.

Lemma 9.12 Let K be the total number of pairwise intersections between segments
in S, and let kr be the random variable for the expected number of pairwise in-
tersections between the ﬁrst r segments inserted during randomized incremental
construction. Then

kr = K
 (
n−2
r−2)

(n
r) = K r(r − 1)
n(n − 1).

Proof. Let us consider the intersection point of two ﬁxed segments s and s ′. This
intersection point appears in Tr if and only both s and s ′ are among the ﬁrst r segments.
There are (
n
r) ways of choosing the set of r segments (and all choices have the same prob-
ability); since the number of r-element sets containing s and s ′ is (
n−2
r−2)
, the probability
for the intersection point to appear is
(
n−2
r−2)

(
n
r) = r(r − 1)
n(n − 1).

Summing this up over all K intersection points, and using linearity of expectation, the
statement follows. 
From Observation 9.10, Observation 9.11 and Lemma 9.12, we obtain the following

105

Chapter 9. Trapezoidal Maps CG 2012

Corollary 9.13 The expected number tr of active conﬁgurations after r insertion steps
is
 tr = O (
r + K r(r − 1)
n2
 ) .

Plugging this into Theorem 9.7 and Theorem 9.9, we obtain the following ﬁnal

Theorem 9.14 Let S be a set of n segments in the plane, with a total of K pairwise
intersections. The randomized incremental construction computes the trapezoidal
map of S in time

O(n log n + K).

Proof. We already know that the expected update cost (subsuming steps Trace, Split, and
Merge) is proportional to the expected overall structural change, which by Theorem 9.7
is
 O
 ( n∑

r=1
 tr
r
 )
 = O(n) + O
 ( K
n2
 n∑

r=1 r

)
 = O(n + K).

We further know that the expected point location cost (subsuming step Find) is pro-
portional to the overall expected number of conﬂicts which by Theorem 9.9 is

O
 (

n
 n∑

r=1
 tr
r2
 )
 = O(n log n) + O
 ( K
n
 n∑

r=1 1
)
 = O(n log n + K). 
9.6 Analysis of the point location

Finally, we return to the application of trapezoidal maps for point location. We make
precise what we mean by saying that “point-location queries are handled in O(log n)
expected time", and we prove our claim.

Lemma 9.15 Let S = {s1, . . . , sn} be any set of n segments. Then there exists a con-
stant c > 0 such that, with high probability (meaning, with probability tending to
1 as n → ∞), the history graph produced by the random incremental construction
answers every possible point-location query in time at most c log n.

Note that our only randomness assumption is over the random permutation of S
chosen at the beginning of the incremental construction. We do not make any randomness
assumption on the given set of segments.
The proof of Lemma 9.15 is by a typical application of Chernoﬀ’s bound followed by
the union bound.
Recall (or please meet) Chernoﬀ’s bound:

106

CG 2012 9.6. Analysis of the point location

Lemma 9.16 Let X1, X2, . . . , Xn be independent 0/1 random variables, and let X =
X1 + · · · + Xn. Let pi = Pr[Xi = 1], and let µ = E[X] = p1 + · · · + pn. Then,

Pr[X < (1 − δ)µ] < ( e−δ

(1 − δ)1−δ
 )µ for every 0 < δ < 1;

Pr[X > (1 + δ)µ] < ( eδ

(1 + δ)1+δ
 )µ for every δ > 0.

The important thing to note is that e−δ/(1 −δ)1−δ as well as eδ/(1 +δ)1+δ are strictly
less than 1 for every ﬁxed δ > 0, and decrease with increasing δ.
Now back to the proof of Lemma 9.15:
Proof. First note that, even though there are inﬁnitely many possible query points, there
is only a ﬁnite number of combinatorially distinct possible queries: If two query points
lie together in every trapezoid (either both inside or both outside), among all possible
trapezoids deﬁned by segments of S, then there is no diﬀerence in querying one point
versus querying the other, as far as the algorithm is concerned. Since there are O(n
4)
possible trapezoids (recall that each trapezoid is deﬁned by at most four segments), there
are only O(n
4) queries we have to consider.
Fix a query point q. We will show that there exists a large enough constant c > 0,
such that only with probability at most O(n
−5) does the query on q take more than
c log n steps.
Let s1, s2, . . . , sn be the random order of the segments chosen by the algorithm, and
for 1 ⩽ r ⩽ n let Tr be the trapezoidal map generated by the ﬁrst r segments. Note
that for every r, the point q belongs to exactly one trapezoid of Tr. The question is how
many times the trapezoid containing q changes during the insertion of the segments,
since these are exactly the trapezoids of the history graph that will be visited when we
do a point-location query on q.
For 1 ⩽ r ⩽ n, let Ar be the event that the trapezoid containing q changes from
Tr−1 to Tr. What is the probability of Ar? As in Section 8.3, we “run the movie
backwards": To obtain Tr−1 from Tr, we delete a random segment from among s1, . . . , sr;
the probability that the trapezoid containing q in Tr is destroyed is at most 4/r, since
this trapezoid is deﬁned by at most four segments. Thus, Pr[Ar] ⩽ 4/r, independently
of every other As, s ̸= r.
For each r let Xr be a random variable equal to 1 if Ar occurs, and equal to 0 otherwise.
We are interested in the quantity X = X1 + · · · + Xr. Then µ = E[X] = ∑n
r=1 Pr[Ar] =
4 ln n + O(1). Applying Chernoﬀ’s bound with δ = 2 (it is just a matter of choosing δ
large enough), we get

Pr[X > (1 + δ)µ] < 0.273µ = O(0.2734 ln n) = O(n
−5.19),

so we can take our c to be anything larger than 4(1 + δ) = 12.
Thus, for every ﬁxed query q, the probability of a “bad event" (a permutation that
results in a long query time) is O(n
−5). Since there are only O(n
4) possible choices for

107

Chapter 9. Trapezoidal Maps CG 2012

q, by the union bound the probability of some q having a bad event is O(1/n), which
tends to zero with n. 
9.7 The trapezoidal map of a simple polygon

An important special case of the trapezoidal map is obtained when the input segments
form a simple polygon; seee Figure 9.10. In this case, we are mostly interested in the
part of the trapezoidal map inside the polygon, since that parts allows us to obtain a
triangulation of the polygon in linear time.

Figure 9.10: The trapezoidal map inside a simple polygon

To get a triangulation, we ﬁrst go through all trapezoids; we know that each trapezoid
must have one polygon vertex on its left and one on its right boundary (due to general
position, there is actually exactly one vertex on each of these two boundaries). Whenever
the segment connecting these two vertices is not an edge of the polygon, we have a
diagonal, and we insert this diagonal. Once we have done this for all trapezoids, it is
easily seen that we have obtained a subdivision of the polygon into x-monotone polygons,
each of which can be triangualated in linear time; see Exercise 9.24. This immediately
allows us to improve over the statement of Exercise 2.19.

Corollary 9.17 A simple polygon with n vertices can be triangulated in expected time
O(n log n).

Proof. By Theorem 9.14, the trapezoidal decomposition induced by the segments
of a simple polygon can be combuted in expected time O(n log n), since there are no
intersections between the segments. Using the above linear-time triangulation algorithm
from the trapezoidal map, the result follows. 
108

CG 2012 9.7. The trapezoidal map of a simple polygon

The goal of this section is to further improve this bound and show the following
result.

Theorem 9.18 Let S = {s1, s2, . . . , sn} be the set of edges of an n-vertex simple polygon,
in counterclockwise order around the polygon. The trapezoidal map induced by S
(and thus also a triangulation of S) can be computed in exptected time O(n log∗ n).

Informally speaking, the function log∗ n is the number of times we have to iterate the
operation of taking (binary) logarithms, before we get from n down to 1. Formally, we
deﬁne

log(h)(n) = { n, if h = 0
log(h−1)(log n), otherwise

as the h-times iterated logarithm, and for n ⩾ 1 we set

log∗ n = max{h : log(h) n ⩾ 1}.

For example, we have

log∗(265536) = 5,

meaning that for all practical purposes, log∗ n ⩽ 5; a bound of O(n log∗ n) is therefore
very close to a linear bound.

History ﬂattening. Recall that the bottleneck in the randomized incremental construction
is the Find step. Using the special structure we have (the segments form a simple polygon
in this order), we can speed up this step. Suppose that at some point during incremental
construction, we have built the trapezoidal map of a subset of r segments, along with
the history graph. We now ﬂatten the history by removing all trapezoids that are not in
Tr, the current trapezoidal map. To allow for point location also in the future, we need
an “entry point” into the ﬂattened history, for every segment not inserted so far (the old
entry point for all segments was the bounding unit square [0, 1]2).

Lemma 9.19 Let S be the set of edges of an n-vertex simple polygon, in counterclock-
wise order around the polygon. For R ⊆ S, let T(R) be the trapezoidal map induced
by R. In time proportional to n plus the number of conﬂicts between trapezoids in
T(R) and segments in S \ R, we can ﬁnd for all segment s ∈ S a trapezoid of T(R)
that contains an endpoint of s.

Proof. In a trivial manner (and in time O(n)), we do this for the ﬁrst segment s1 and
its ﬁrst endpoint p1. Knowing the trapezoid i containing pi, the ﬁrst endpoint of si,
we trace the segment si through T(R) until pi+1, its other endpoint and ﬁrst endpoint
of si+1 is found, along with the trapezoid i+1 containing it. This is precisely what we
also did in the Trace Step 2 of the incremental construction in Section 9.3.

109

Chapter 9. Trapezoidal Maps CG 2012

By Lemma 9.6 (pretending that we are about to insert si), the cost of tracing si
through T(R) is proportional to the size of T(R) \ T(R ∪ {si}), equivalently, the number
of conﬂicts between trapezoids in T(R) and si. The statement follows by adding up the
costs for all i. 
This is exactly where the special structure of our segments forming a polygon helps.
After locating pi, we can locate the next endpoint pi+1 in time proportional to the
structural change that the insertion of si would cause. We completely avoid the traversal
of old history trapezoids that would be necessary for an eﬃcient location of pi+1 from
scratch.
Next we show what Lemma 9.19 gives us in expectation.

Lemma 9.20 Let S be the set of edges of an n-vertex simple polygon, in counterclock-
wise order around the polygon, and let Tr be the trapezoidal map obtained after
inserting r segments in random order. In expected time O(n), we can ﬁnd for each
segment s not inserted so far a trapezoid of Tr containing an endpoint of s.

Proof. According to Lemma 9.19, the expected time is bounded by O(n + ℓ(r)), where

ℓ(r) = 1
(
n
r) ∑

R⊆S,|R|=r
 ∑

y∈S\R |{ ∈ T(R) : y ∈ K( )}|.

This looks very similar to the bound on the quantity k(r) that we have derived in
Section 8.5 to count the expected number of conﬂicts in general conﬁguration spaces:

k(r) ⩽ 1
(
n
r) ∑

R⊆S,|R|=r
 d
r
 ∑

y∈S\R |{∆ ∈ T(R) : y ∈ K(∆)}|.

Indeed, the diﬀerence is only an additional factor of d
r in the latter. For k(r), we have
then computed the bound

k(r) ⩽ k1(r) − k2(r) + k3(r) ⩽ d
r (n − r)tr − d
r (n − r)tr+1 + d
2

r(r + 1) (n − r)tr+1, (9.21)

where tr is the expected size of Tr. Hence, to get a bound for ℓ(r), we simply have to
cancel d
r from all terms to obtain

ℓ(r) ⩽ (n − r)tr − (n − r)tr+1 + d
r + 1 (n − r)tr+1 = O(n),

since tr ⩽ tr+1 = O(r) in the case of nonintersecting line segments. 
110

CG 2012 9.7. The trapezoidal map of a simple polygon

The faster algorithm. We proceed as in the regular randomized incremental construction,
except that we frequently and at well-chosen points ﬂatten the history. Let us deﬁne

N(h) = ⌈ n
log(h) n
⌉ , 0 ⩽ h ⩽ log∗ n.

We have N(0) = 1, N(log∗ n) ⩽ n and N(log∗ n + 1) > n. We insert the segments in
random order, but proceed in log∗ n + 1 rounds. In round h = 1, . . . , log∗ n + 1, we do
the following.

(i) Flatten the history graph by ﬁnding for each segment s not inserted so far a trape-
zoid of the current trapezoidal map containing an endpoint of s.

(ii) Insert the segments N(h − 1) up to N(h) − 1 in the random order, as usual, but
starting from the ﬂat history established in (i).

In the last round, we have N(h) − 1 ⩾ n, so we stop with segment n in the random
order.
From Lemma 9.20, we know that the expected cost of step (i) over all rounds is
bounded by O(n log∗ n) which is our desired overall bound. It remains to prove that
the same bound also deals with step (ii). We do not have to worry about the overall
expected cost of performing the structural changes in the trapezoidal map: this will be
bounded by O(n), using tr = O(r) and Theorem 9.7. It remains to analyze the Find step,
and this is where the history ﬂattening leads to a speedup. Adapting Lemma 9.8 and its
proof accordingly, we obtain the following.

Lemma 9.22 During round h of the fast incremental construction algorithm for the
trapezoidal map, the total number of history graph nodes traversed during all Find
steps is bounded by N(h)−N(h−1)1, plus the number of conﬂicts between trapezoids
that are created during round h, and segments inserted during round h.

Proof. The history in round h only contains trapezoids that are active at some point in
round h. On the one hand, we have the “root nodes” present immediately after ﬂattening
the history, on the other hand the trapezoids that are created during the round. The
term N(h) − N(h − 1) accounts for the traversals of the root nodes during round h. As in
the proof of Lemma 9.8, the traversals of other history graph nodes can be charged to the
number of conﬂicts between trapezoids that are created during round h and segments
inserted during round h. 
To count the expected number of conﬂicts involving trapezoids created in round h, we
go back to the general conﬁguration space framework once more. With kh(r) being the
expected number of conﬂicts created in step r, restricted to the ones involving segments
inserted in round h, we need to bound

κ(h) =
 N(h)−1∑

r=N(h−1) kh(r).

1this amounts to O(n) throughout the algorithm and can therefore be neglected

111

Chapter 9. Trapezoidal Maps CG 2012

As in (9.21), we get

kh(r) ⩽ d
r (N(h) − r)tr − d
r (N(h) − r)tr+1 + d
2

r(r + 1)(N(h) − r)tr+1,

where we have replaced n with N(h), due to the fact that we do not need to consider
segments in later rounds. Then tr = O(r) yields

κ(h) ⩽ O
 

N(h)
 N(h)−1∑

r=N(h−1)
 1
r
 



= O (
N(h) log N(h)
N(h − 1)
)

= O
 (
N(h) log log(h−1) n
log(h) n
 )

= O (
N(h) log(h) n
) = O(n).

It follows that step (ii) of the fast algorithm also requires expected linear time per
round, and Theorem 9.18 follows.

Exercise 9.23 a) You are given a set of n pairwise disjoint line segments. Find an
algorithm to answer vertical ray shooting queries in O(log n) time. That is,
preprocess the data such that given a query point q you can report in O(log n)
time which segment is the ﬁrst above q (or if there are none). Analyze the
running time and the space consumption of the preprocessing.

b) What happens if we allow intersections of the line segments? Explain in a
few words how you have to adapt your solution and how the time and space
complexity would change.

Exercise 9.24 Show that an n-vertex x-monotone polygon can be triangulated in time
O(n). (As usual a polygon is given as a list of its vertices in counterclockwise order.
A polygon P is called x-monotone if for all vertical lines ℓ, the intersection ℓ ∩ P
has at most one component.)

Questions

35. What is the deﬁnition of a trapezoidal map?

36. How does the random incremental construction of a trapezoidal map proceed?
What are the main steps to be executed at each iteration?

37. How can trapezoidal maps be used for the point location problem?

112

CG 2012 9.7. The trapezoidal map of a simple polygon

38. What is the conﬁguration space framework? Recall Section 8.3.

39. What is a naive way of deﬁning a conﬁguration in the case of trapezoids, and
why does it fail?

40. What is a more successful way of deﬁning a conﬁguration? Why do things
work in this case?

41. What is the history graph, and how is it used to answer point location queries?

42. What is the performance of the random incremental construction of the trape-
zoidal map when used for the point-location problem? Be precise!

43. What probabilistic techniques are used in proving this performance bound?

44. How can you speed up the randomized incremental construction in the case
where the input segments from a simple polygon? Sketch the necessary changes
to the algorithm, and how they aﬀect the analysis.

113

Chapter 10

Voronoi Diagrams

10.1 Post Oﬃce Problem

Suppose there are n post oﬃces p1, . . . pn in a city. Someone who is located at a position
q within the city would like to know which post oﬃce is closest to him. Modeling the
city as a planar region, we think of p1, . . . pn and q as points in the plane. Denote the
set of post oﬃces by P = {p1, . . . pn}.

Figure 10.1: Closest post oﬃces for various query points.

While the locations of post oﬃces are known and do not change so frequently, we do
not know in advance for which—possibly many—query locations the closest post oﬃce
is to be found. Therefore, our long term goal is to come up with a data structure on
top of P that allows to answer any possible query eﬃciently. The basic idea is to apply
a so-called locus approach: we partition the query space into regions on which is the
answer is the same. In our case, this amounts to partition the plane into regions such
that for all points within a region the same point from P is closest (among all points
from P).
As a warmup, consider the problem for two post oﬃces pi, pj ∈ P. For which query
locations is the answer pi rather than pj? This region is bounded by the bisector of pi
and pj, that is, the set of points which have the same distance to both points.

115

Chapter 10. Voronoi Diagrams CG 2012

Proposition 10.1 For any two distinct points in R
d the bisector is a hyperplane, that
is, in R
2 it is a line.

Proof. Let p = (p1, . . . , pd) and q = (q1, . . . , qd) be two points in R
d. The bisector of
p and q consists of those points x = (x1, . . . , xd) for which

||p − x|| = ||q − x|| ⇐⇒ ||p − x||
2 = ||q − x||2 ⇐⇒ ||p||
2 − ||q||2 = 2(p − q)⊤x .

As p and q are distinct, this is the equation of a hyperplane. 
pi
 pj

H(pi, pj)

Figure 10.2: The bisector of two points.

Denote by H(pi, pj) the closed halfspace bounded by the bisector of pi and pj that
contains pi. In R
2, H(pi, pj) is a halfplane; see Figure 10.2.

Exercise 10.2

a) What is the bisector of a line ℓ and a point p ∈ R
2 \ ℓ, that is, the set of all
points x ∈ R
2 with ||x − p|| = ||x − ℓ|| (= minq∈ℓ ||x − q||)?

b) For two points p ̸= q ∈ R
2, what is the region that contains all points whose
distance to p is exactly twice their distance to q?

10.2 Voronoi Diagram

In the following we work with a set P = {p1, . . . , pn} of points in R
2.

Deﬁnition 10.3 (Voronoi cell) For pi ∈ P denote the Voronoi cell VP(i) of pi by

VP(i) := {q ∈ R
2 ∣
∣ ||q − pi|| ⩽ ||q − p|| for all p ∈ P} .

Proposition 10.4

VP(i) = ⋂

j̸=i H(pi, pj) .
 116

CG 2012 10.2. Voronoi Diagram

Proof. For j ̸= i we have ||q − pi|| ⩽ ||q − pj|| ⇐⇒ q ∈ H(pi, pj). 
Corollary 10.5 VP(i) is non-empty and convex.

Proof. According to Proposition 10.4, VP(i) is the intersection of a ﬁnite number of
halfplanes and hence convex. VP(i) ̸= ∅ because pi ∈ VP(i). 
Observe that every point of the plane lies in some Voronoi cell but no point lies in the
interior of two Voronoi cells. Therefore these cells form a subdivision of the plane. See
Figure 10.3 for an example.

Deﬁnition 10.6 (Voronoi Diagram) The Voronoi Diagram VD(P) of a set P = {p1, . . . , pn}
of points in R
2 is the subdivision of the plane induced by the Voronoi cells VP(i),
for i = 1, . . . , n.
Denote by VV(P) the set of vertices, by VE(P) the set of edges, and by VR(P) the
set of regions (faces) of VD(P).

Figure 10.3: Example: The Voronoi diagram of a point set.

Lemma 10.7 For every vertex v ∈ VV(P) the following statements hold.

a) v is the common intersection of at least three edges from VE(P);

b) v is incident to at least three regions from VR(P);

c) v is the center of a circle C(v) through at least three points from P such that

d) C(v)◦ ∩ P = ∅.

Proof. Consider a vertex v ∈ VV(P). As all Voronoi cells are convex, k ⩾ 3 of them
must be incident to v. This proves Part a) and b).

117

Chapter 10. Voronoi Diagrams CG 2012

v

e2
 ek−1

eke1
 VP(k)

VP(1)

VP(2)
 . . .

Without loss of generality let these cells be VP(i), for
1 ⩽ i ⩽ k. Denote by ei, 1 ⩽ i ⩽ k, the edge incident to v
that bounds VP(i) and VP((i mod k) + 1).
For any i = 1, . . . , k we have v ∈ ei ⇒ ||v − pi|| = ||v −
p(i mod k)+1||. In other words, p1, p2, . . . , pk are cocircular,
which proves Part c).
Part d): Suppose there exists a point pℓ ∈ C(v)◦. Then
the vertex v is closer to pℓ than it is to any of p1, . . . , pk,
in contradiction to the fact that v is contained in all of
VP(1), . . . , VP(k). 
Corollary 10.8 If P is in general position (no four points from P are cocircular), then
for every vertex v ∈ VV(P) the following statements hold.

a) v is the common intersection of exactly three edges from VE(P);

b) v is incident to exactly three regions from VR(P);

c) v is the center of a circle C(v) through exactly three points from P such that

d) C(v)◦ ∩ P = ∅. 
Lemma 10.9 There is an unbounded Voronoi edge bounding VP(i) and VP(j) ⇐⇒
pipj ∩ P = {pi, pj} and pipj ⊆ ∂conv(P), where the latter denotes the boundary of the
convex hull of P.

Proof.
 pi pj

ρ
 H

r0

r

bi,j
 C
 D

Denote by bi,j the bisector of pi and pj, and let C
denote the family of circles centered at some point
on bi,j and passing through pi (and pj). There is
an unbounded Voronoi edge bounding VP(i) and
VP(j) ⇐⇒ there is a ray ρ ⊂ bi,j such that
||r − pk|| > ||r − pi|| (= ||r − pj||), for every r ∈ ρ
and every pk ∈ P with k /∈ {i, j}. Equivalently,
there is a ray ρ ⊂ bi,j such that for every point
r ∈ ρ the circle C ∈ C centered at r does not
contain any point from P in its interior.
The latter statement implies that the open
halfplane H, whose bounding line passes through
pi and pj and such that H contains the inﬁnite
part of ρ, contains no point from P in its interior.
Therefore, pipj appears on ∂conv(P) and pipj does not contain any pk ∈ P, for k ̸= i, j.
Conversely, suppose that pipj appears on ∂conv(P) and pipj ∩ P = {pi, pj}. Then
some halfplane H whose bounding line passes through pi and pj contains no point from

118

CG 2012 10.3. Duality

P in its interior. In particular, the existence of H together with pipj ∩P = {pi, pj} implies
that there is some circle C ∈ C such that C ∩ P = {pi, pj}. Denote by r0 the center of
C and let ρ denote the ray starting from r0 along bi,j such that the inﬁnite part of ρ is
contained in H. Consider any circle D ∈ C centered at a point r ∈ ρ and observe that
D \ H ⊆ C \ H. As neither H nor C contain any point from P in their respective interior,
neither does D. This holds for every D, and we have seen above that this statement is
equivalent to the existence of an unbounded Voronoi edge bounding VP(i) and VP(j). 
10.3 Duality

A straight-line dual of a plane graph G is a graph G ′ deﬁned as follows: Choose a point
for each face of G and connect any two such points by a straight edge, if the corresponding
faces share an edge of G. Observe that this notion depends on the embedding; that
is why the straight-line dual is deﬁned for a plane graph rather than for an abstract
graph. In general, G ′ may have edge crossings, which may also depend on the choice of
representative points within the faces. However, for Voronoi diagrams is a particularly
natural choice of representative points such that G ′ is plane: the points from P.

Theorem 10.10 (Delaunay [2]) The straight-line dual of VD(P) for a set P ⊂ R
2 of n ⩾ 3
points in general position (no three points from P are collinear and no four points
from P are cocircular) is a triangulation: the unique Delaunay triangulation of P.

Proof. By Lemma 10.9, the convex hull edges appear in the straight-line dual T of
VD(P) and they correspond exactly to the unbounded edges of VD(P). All remaining
edges of VD(P) are bounded, that is, both endpoints are Voronoi vertices. Consider some
v ∈ VV(P). According to Corollary 10.8(b), v is incident to exactly three Voronoi regions,
which, therefore, form a triangle △(v) in T . By Corollary 10.8(d), the circumcircle of
△(v) does not contain any point from P in its interior. Hence △(v) appears in the
(unique by Corollary 6.18) Delaunay triangulation of P.
Conversely, for any triangle pipjpk in the Delaunay triangulation of P, by the empty
circle property the circumcenter c of pipjpk has pi, pj, and pk as its closest points from
P. Therefore, c ∈ VV(P) and—as above—the triangle pipjpk appears in T . 
It is not hard to generalize Theorem 10.10 to general point sets. In this case, a
Voronoi vertex of degree k is mapped to a convex polygon with k cocircular vertices.
Any triangulation of such a polygon yields a Delaunay triangulation of the point set.

Corollary 10.11 |VE(P)| ⩽ 3n − 6 and |VV(P)| ⩽ 2n − 5.

Proof. Every edge in VE(P) corresponds to an edge in the dual Delaunay triangulation.
The latter is a plane graph on n vertices and thus has at most 3n − 6 edges and at most
2n − 4 faces by Lemma 5.1. Only the bounded faces correspond to a vertex in VD(P). 
119

Chapter 10. Voronoi Diagrams CG 2012

Figure 10.4: The Voronoi diagram of a point set and its dual Delaunay triangulation.

Corollary 10.12 For a set P ⊂ R
2 of n points, the Voronoi diagram of P can be con-
structed in expected O(n log n) time and space.

Proof. We have seen that a Delaunay triangulation T for P can be obtained using
randomized incremental construction in the given time and space bounds. As T is a
plane graph, its number of vertices, edges, and faces all are linear in n. Therefore, the
straight-line dual of T —which by Theorem 10.10 is the desired Voronoi diagram—can
be computed in O(n) additional time and space. 
Exercise 10.13 Consider the Delaunay triangulation T for a set P ⊂ R
2 of n ⩾ 3
points in general position. Prove or disprove:

a) Every edge of T intersects its dual Voronoi edge.

b) Every vertex of VD(P) is contained in its dual Delaunay triangle.

10.4 Lifting Map

Recall the lifting map that we used in Section 6.3 to prove that the Lawson Flip Algorithm
terminates. Denote by U : z = x
2 + y
2 the unit paraboloid in R
3. The lifting map
ℓ : R
2 → U with ℓ : p = (px, py) ↦→ (px, py, px2 + py2) is the projection of the x/y-plane
onto U in direction of the z-axis.
For p ∈ R
2 let Hp denote the plane of tangency to U in ℓ(p). Denote by hp : R
2 → Hp
the projection of the x/y-plane onto Hp in direction of the z-axis (see Figure 10.5).

Lemma 10.14 ||ℓ(q) − hp(q)|| = ||p − q||
2, for any points p, q ∈ R
2.

120

CG 2012 10.5. Point location in a Voronoi Diagram

p

U
 ℓ(p)

q

ℓ(q)

hp(q)
 Hp

Figure 10.5: Lifting map interpretation of the Voronoi diagram in a two-dimensional
projection.

Exercise 10.15 Prove Lemma 10.14. Hint: First determine the equation of the tangent
plane Hp to U in ℓ(p).

Theorem 10.16 For p = (px, py) ∈ R
2 denote by Hp the plane of tangency to the unit
paraboloid U = {(x, y, z) : z = x
2 + y
2} ⊂ R
3 in ℓ(p) = (px, py, px2 + py2). Let H(P) :=⋂
p∈P H+
p the intersection of all halfspaces above the planes Hp, for p ∈ P. Then the
vertical projection of ∂H(P) onto the x/y-plane forms the Voronoi Diagram of P
(the faces of ∂H(P) correspond to Voronoi regions, the edges to Voronoi edges, and
the vertices to Voronoi vertices).

Proof. For any point q ∈ R
2, the vertical line through q intersects every plane Hp,
p ∈ P. By Lemma 10.14 the topmost plane intersected belongs to the point from P that
is closest to q. 
10.5 Point location in a Voronoi Diagram

One last bit is still missing in order to solve the post oﬃce problem optimally.

Theorem 10.17 Given a triangulation T for a set P ⊂ R
2 of n points, one can build in
O(n) time an O(n) size data structure that allows for any query point q ∈ conv(P)
to ﬁnd in O(log n) time a triangle from T containing q.

The data structure we will employ is known as Kirkpatrick’s hierarchy. But before
discussing it in detail, let us put things together in terms of the post oﬃce problem.

Corollary 10.18 (Nearest Neighbor Search) Given a set P ⊂ R
2 of n points, one can build
in expected O(n log n) time an O(n) size data structure that allows for any query

121

Chapter 10. Voronoi Diagrams CG 2012

point q ∈ conv(P) to ﬁnd in O(log n) time a nearest neighbor of q among the points
from P.

Proof. First construct the Voronoi Diagram V of P in expected O(n log n) time. It has
exactly n convex faces. Every unbounded face can be cut by the convex hull boundary
into a bounded and an unbounded part. As we are concerned with query points within
conv(P) only, we can restrict our attention to the bounded parts.1 Any convex polygon
can easily be triangulated in time linear in its number of edges (= number of vertices).
As V has at most 3n − 6 edges and every edge appears in exactly two faces, V can
be triangulated in O(n) time overall. Label each of the resulting triangles with the
point from p, whose Voronoi region contains it, and apply the data structure from
Theorem 10.17. 
10.5.1 Kirkpatrick’s Hierarchy

We will now the develop the data structure for point location in a triangulation, as
described in Theorem 10.17. The main idea is to construct a hierarchy T0,. . . ,Th of
triangulations, such that T0 = T , the vertices of Ti are a subset of the vertices of Ti−1, for i = 1, . . . , h, and Th comprises a single triangle only.

Search. For a query point x the triangle from T containing x can be found as follows.

Search(x ∈ R
2)

1. For i = h, h − 1, . . . , 0: Find a triangle ti from Ti that contains x.

2. return t0.

This search is eﬃcient under the following conditions.

(C1) Every triangle from Ti intersects only few (⩽ c) triangles from Ti−1. (These will
then be connected via the data structure.)

(C2) h is small (⩽ d log n).

Proposition 10.19 The search procedure described above needs ⩽ 3cd log n = O(log n)
orientation tests.

Proof. For every Ti, 0 ⩽ i < h, at most c triangles are tested as to whether or not they
contain x. Using three orientation tests one can determine whether or not a triangle
contains a given point. 
1We even know how to decide in O(log n) time whether or not a given point lies within conv(P), see
Exercise 3.20.
 122

CG 2012 10.5. Point location in a Voronoi Diagram

Thinning. Removing a vertex v and all its incident edges from a triangulation creates a
non-triangulated hole that forms a star-shaped polygon since all points are visible from
v (the star-point).

Lemma 10.20 A star-shaped polygon, given as a sequence of n ⩾ 3 vertices and a
star-point, can be triangulated in O(n) time.

Proof. For n = 3 there is nothing to do. For n > 3, consider a star-shaped polygon
P = (p0, . . . , pn−1) and a star-point s of P. Consider some convex vertex pi of P, that is,\pi+1pipi−1 ⩽ π, all indices taken mod n. (Every simple polygon on n ⩾ 3 vertices has
at least three convex vertices, on the convex hull.)
As P is star-shaped, the quadrilateral Q = pi−1pipi+1s is completely contained in P.
Therefore, if\pi−1spi+1 ⩽ π and hence Q is convex (Figure 10.6a), then we can add
pi−1pi+1 as a diagonal. In this way one triangle is cut oﬀ from P, leaving a star-shaped
polygon P ′ (with respect to s) on n−1 vertices. The polygon P ′ can then be triangulated
recursively. If, on the other hand,\pi−1spi+1 > π (Figure 10.6b), we cannot safely add

s

pi

pi+1 pi−1

(a)\pi−1spi+1 ⩽ π.
 s
 pi

pi+1 pi−1

(b)\pi−1spi+1 > π.

Figure 10.6: The quadrilateral pi−1pipi+1s is contained in P.

the edge pi−1pi+1 because it might intersect other edges of P or even lie outside of P.
But we claim that in this case there exists another convex vertex pj of P, for which\pj−1spj+1 ⩽ π and therefore we can add the edge pj−1pj+1 instead.
In fact, it is enough to choose pj to be some convex vertex of P that is not a neighbor
of pi: As ∑n−1
k=0\pk−1spk = 2π and\pi−1spi +\pispi+1 =\pi−1spi+1 > π, we have\pj−1spj +\pjspj+1 =\pj−1spj+1 < π.
It remains to show that such a vertex pj exists. P has at least three convex vertices.
One of them is pi. If the only other two convex vertices are pi−1 and pi+1, then we make
the whole argument with pi−1 instead of pi and ﬁnd j = i + 1. Note that pi−1 and pi+1
are not neighbors because P is not a triangle.
As for the linear time bound, we simply scan the sequence of vertices as in Graham’s
Scan. For every triple pi−1pipi+1 of successive vertices it is tested (in constant time)
whether pi−1pipi+1s forms a convex quadrilateral. If so, then the edge pi−1pi+1 is added,
eﬀectively removing pi from further consideration. Therefore, pi can be charged for the
(potential, if there are enough vertices left) additional test of the new triple pxpi−1pi+1
formed with the predecessor px of pi−1 in the current sequence. As shown for Graham’s

123

Chapter 10. Voronoi Diagrams CG 2012

Scan in Theorem 3.23, this results in a linear time algorithm overall.2 
As a side remark, the kernel of a simple polygon, that is, the set of all star-points,
can be constructed in linear time as well. We will get back to this question later in the
course. . .
Our working plan is to obtain Ti from Ti−1 by removing several independent (pairwise
non-adjacent) vertices and re-triangulating. These vertices should

a) have small degree (otherwise the degree within the hierarchy gets too large, that
is, we need to test too many triangles on the next level) and

b) be many (otherwise the height h of the hierarchy gets too large).

The following lemma asserts the existence of a suﬃciently large set of independent
small-degree vertices in every triangulation.

Lemma 10.21 In every triangulation of n points in R
2 there exists an independent
set of at least ⌈n/18⌉ vertices of maximum degree 8. Moreover, such a set can be
found in O(n) time.

Proof. Let T = (V, E) denote the graph of the triangulation, which we consider as an
abstract graph in the following. We may suppose that T is maximally planar, that is, all
faces are triangles. (Otherwise triangulate the exterior face arbitrarily. An independent
set in the resulting graph is also independent in T .) For n = 3 the statement is true. Let
n ⩾ 4.
By the Euler formula we have |E| = 3n − 6, that is,
∑

v∈V degT (v) = 2|E| = 6n − 12 < 6n.

Let W ⊆ V denote the set of vertices of degree at most 8. Claim: |W| > n/2. Suppose
|W| ⩽ n/2. As every vertex has degree at least three, we have
∑

v∈V degT (v) = ∑

v∈W degT (v) + ∑

v∈V\W degT (v) ⩾ 3|W| + 9|V \ W|

= 3|W| + 9(n − |W|) = 9n − 6|W| ⩾ 9n − 3n = 6n,

in contradiction to the above.
Construct an independent set U in T as follows (greedily): As long as W ̸= ∅, add an
arbitrary vertex v ∈ W to U and remove v and all its neighbors from W.
Obviously U is independent and all vertices in U have degree at most 8. At each
selection step at most 9 vertices are removed from W. Therefore |U| ⩾ ⌈(n/2)/9⌉ =
⌈n/18⌉. 
Proof. (of Theorem 10.17)
Construct the hierarchy T0, . . . Th with T0 = T as follows. Obtain Ti from Ti−1 by removing

2Recall that the O(n log n) time bound for Graham’s Scan was caused by the initial sorting only.

124

CG 2012 10.5. Point location in a Voronoi Diagram

an independent set U as in Lemma 10.21 and re-triangulating the resulting holes. By
Lemma 10.20 and Lemma 10.21 every step is linear in the number |Ti| of vertices in Ti.
The total cost for building the data structure is thus

h∑

i=0 α|Ti| ⩽
 h∑

i=0 αn(17/18)i < αn
 ∞∑

i=0(17/18)i = 18αn ∈ O(n),

for some constant α. Similarly the space consumption is linear.
The number of levels amounts to h = log18/17 n < 12.2 log n. Thus by Proposi-
tion 10.19 the search needs at most 3 · 8 · log18/17 n < 292 log n orientation tests. 
Improvements. As the name suggests, the hierarchical approach discussed above is due
to David Kirkpatrick [5]. The constant 292 that appears in the search time is somewhat
large. There has been a whole line of research trying to improve it using diﬀerent
techniques. Sarnak and Tarjan [6]: 4 log n. Edelsbrunner, Guibas, and Stolﬁ [3]: 3 log n. Goodrich, Orletsky, and Ramaiyer [4]: 2 log n. Adamy and Seidel [1]: 1 log n + 2√log n + O( 4√log n).

Exercise 10.22 Let {p1, p2, . . . , pn} be a set of points in the plane, which we call obsta-
cles. Imagine there is a disk of radius r centered at the origin which can be moved
around the obstacles but is not allowed to intersect them (touching the boundary is
ok). Is it possible to move the disk out of these obstacles? See the example depicted
in Figure 10.7 below.
More formally, the question is whether there is a (continuous) path γ : [0, 1] −→
R
2 with γ(0) = (0, 0) and ∥γ(1)∥ ⩾ max{∥p1∥, . . . , ∥pn∥}, such that at any time t ∈
[0, 1] and ∥γ(t) − pi∥ ⩾ r, for any 1 ⩽ i ⩽ n. Describe an algorithm to decide
this question and to construct such a path—if one exists—given arbitrary points
{p1, p2, . . . , pn} and a radius r > 0. Argue why your algorithm is correct and analyze
its running time.

Exercise 10.23 This exercise is about an application from Computational Biology:
You are given a set of disks P = {a1, .., an} in R
2, all with the same radius ra > 0.
Each of these disks represents an atom of a protein. A water molecule is represented
by a disc with radius rw > ra. A water molecule cannot intersect the interior of
any protein atom, but it can be tangent to one. We say that an atom ai ∈ P is
accessible if there exists a placement of a water molecule such that it is tangent to
ai and does not intersect the interior of any other atom in P. Given P, ﬁnd an
O(n log n) time algorithm which determines all atoms of P that are inaccessible.

125

Chapter 10. Voronoi Diagrams CG 2012

r

(0, 0)
 pi

Figure 10.7: Motion planning: Illustration for Exercise 10.22.

Exercise 10.24 Let P ⊂ R
2 be a set of n points. Describe a data structure to ﬁnd in
O(log n) time a point in P that is furthest from a given query point q among all
points in P.

Exercise 10.25 Show that the bounds given in Theorem 10.17 are optimal in the al-
gebraic computation tree model.

Questions

45. What is the Voronoi diagram of a set of points in R
2? Give a precise deﬁnition
and explain/prove the basic properties: convexity of cells, why is it a subdivision
of the plane?, Lemma 10.7, Lemma 10.9.

46. What is the correspondence between the Voronoi diagram and the Delaunay
triangulation for a set of points in R
2? Prove duality (Theorem 10.10) and
explain where general position is needed.

47. How to construct the Voronoi diagram of a set of points in R
2? Describe an
O(n log n) time algorithm, for instance, via Delaunay triangulation.

48. How can the Voronoi diagram be interpreted in context of the lifting map?
Describe the transformation and prove its properties to obtain a formulation of the
Voronoi diagram as an intersection of halfspaces one dimension higher.

49. What is the Post-Oﬃce Problem and how can it be solved optimally? De-
scribe the problem and a solution using linear space, O(n log n) preprocessing, and
O(log n) query time.
 126

CG 2012 10.5. Point location in a Voronoi Diagram

50. How does Kirkpatrick’s hierarchical data structure for planar point location
work exactly? Describe how to build it and how the search works, and prove the
runtime bounds. In particular, you should be able to state and prove Lemma 10.20,
Lemma 10.21, and Theorem 10.17.

References

[1] Udo Adamy and Raimund Seidel, On the exaxt worst case query com-
plexity of planar point location. J. Algorithms, 37, (2000), 189–217, URL
http://dx.doi.org/10.1006/jagm.2000.1101.

[2] Boris Delaunay, Sur la sphère vide. A la memoire de Georges Voronoi. Izv. Akad.
Nauk SSSR, Otdelenie Matematicheskih i Estestvennyh Nauk, 7, (1934), 793–800.

[3] Herbert Edelsbrunner, Leonidas J. Guibas, and Jorge Stolﬁ, Optimal point loca-
tion in a monotone subdivision. SIAM J. Comput., 15, 2, (1986), 317–340, URL
http://dx.doi.org/10.1137/0215023.

[4] Michael T. Goodrich, Mark W. Orletsky, and Kumar Ramaiyer, Methods
for achieving fast query times in point location data structures. In Proc.
8th ACM-SIAM Sympos. Discrete Algorithms, pp. 757–766, 1997, URL
http://doi.acm.org/10.1145/314161.314438.

[5] David G. Kirkpatrick, Optimal search in planar subdivisions. SIAM J. Comput., 12,
1, (1983), 28–35, URL http://dx.doi.org/10.1137/0212002.

[6] Neil Sarnak and Robert E. Tarjan, Planar point location using per-
sistent search trees. Commun. ACM, 29, 7, (1986), 669–679, URL
http://dx.doi.org/10.1145/6138.6151.

127

Chapter 11

Linear Programming

This lecture is about a special type of optimization problems, namely linear programs.
We start with a geometric problem that can directly be formulated as a linear program.

11.1 Linear Separability of Point Sets

Let P ⊆ R
d and Q ⊆ R
d be two ﬁnite point sets in d-dimensional space. We want to
know whether there exists a hyperplane that separates P from Q (we allow non-strict
separation, i.e. some points are allowed to be on the hyperplane). Figure 11.1 illustrates
the 2-dimensional case.

Figure 11.1: Left: there is a separating hyperplane; Right: there is no separating
hyperplane

How can we formalize this problem? A hyperplane is a set of the form

h = {x ∈ R
d : h1x1 + h2x2 + · · · + hdxd = h0},

where hi ∈ R, i = 0, . . . , d. For example, a line in the plane has an equation of the form
ax + by = c.
 129

Chapter 11. Linear Programming CG 2012

The vector η(h) = (h1, h2, . . . , hd) ∈ R
d is called the normal vector of h. It is
orthogonal to the hyperplane and usually visualized as in Figure 11.2(a).

h: ax + by = c

η (h) = (a,b)

(a) The normal vector of a hyperplane
 h: ax + by = c

η (h) = (a,b)

h

h
 +

−

(b) The two halfspaces of a hyperplane

Figure 11.2: The concepts of hyperplane, normal vector, and halfspace

Every hyperplane h deﬁnes two closed halfspaces

h+ = {x ∈ R
d : h1x1 + h2x2 + · · · + hdxd ⩽ h0},
h− = {x ∈ R
d : h1x1 + h2x2 + · · · + hdxd ⩾ h0}.

Each of the two halfpsaces is the region of space “on one side” of h (including h itself).
The normal vector η(h) points into h−, see Figure 11.2(b). Now we can formally deﬁne
linear separability.

Deﬁnition 11.1 Two point sets P ⊆ R
d and Q ⊆ R
d are called linearly separable if
there exists a hyperplane h such that P ⊆ h+ and Q ⊆ h−. In formulas, if there
exist real numbers h0, h1, . . . , hd such that

h1p1 + h2p2 + · · · + hdpd ⩽ h0, p ∈ P,
h1q1 + h2q2 + · · · + hdqd ⩾ h0, q ∈ Q.

As we see from Figure 11.1, such h0, h1, . . . , hd may or may not exist. How can we
ﬁnd out?

11.2 Linear Programming

The problem of testing for linear separability of point sets is a special case of the general
linear programming problem.

Deﬁnition 11.2 Given n, d ∈ N and real numbers

bi , i = 1, . . . , n,
cj , j = 1, . . . , d,
aij , i = 1, . . . , n, j = 1, . . . , d,
 130

CG 2012 11.2. Linear Programming

the linear program deﬁned by these numbers is the problem of ﬁnding real numbers
x1, x2, . . . , xd such that

(i) ∑d
j=1 aijxj ⩽ bi, i = 1, . . . , n, and

(ii) ∑d
j=1 cjxj is as large as possible subject to (i).

Let us get a geometric intuition: each of the n constraints in (i) requires x =
(x1, x2, . . . , xd) ∈ R
d to be in the positive halfspace of some hyperplane. The intersection
of all these halfspaces is the feasible region of the linear program. If it is empty, there
is no solution—the linear program is called infeasible.
Otherwise—and now (ii) enters the picture—we are looking for a feasible solution x
(a point inside the feasible region) that maximizes ∑d
j=1 cjxj. For every possible value γ
of this sum, the feasible solutions for which the sum attains this value are contained in
the hyperplane

{x ∈ R
d :
 d∑

j=1 cjxj = γ}

with normal vector c = (c1, . . . , cd). Increasing γ means to shift the hyperplane into
direction c. The highest γ is thus obtained from the hyperplane that is most extreme in
direction c among all hyperplanes that intersect the feasible region, see Figure 11.3.

γ = 10

c
 γ

γ

γ

γ
 = 20

= 30

= 40

= 50

Figure 11.3: A linear program: ﬁnding the feasible solution in the intersection of ﬁve
positive halfspaces that is most extreme in direction c (has highest value
γ = ∑d
j=1 cjxj)

In Figure 11.3, we do have an optimal solution (a feasible solution x of highest value
∑d
j=1 cjxj), but in general, there might be feasible solutions of arbitrarily high γ-value.
In this case, the linear program is called unbounded, see Figure 11.4.

131

Chapter 11. Linear Programming CG 2012

γ = 10

c
 γ

γ

γ

γ
 = 20

= 30

= 40

= 50

Figure 11.4: An unbounded linear program

It can be shown that infeasibility and unboundedness are the only obstacles for the
existence of an optimal solution. If the linear program is feasible and bounded, there
exists an optimal solution.

This is not entirely trivial, though. To appreciate the statement, consider the problem
of ﬁnding a point (x, y) that (i) satisﬁes y ⩾ ex and (ii) has smallest value of y among all
(x, y) that satisfy (i). This is not a linear program, but in the above sense it is feasible
(there are (x, y) that satisfy (i)) and bounded (y is bounded below from 0 over the set of
feasible solutions). Still, there is no optimal solution, since values of y arbitrarily close
to 0 can be attained but not 0 itself.

Even if a linear program has an optimal solution, it is in general not unique. For
example, if you rotate c in Figure 11.3 such that it becomes orthogonal to the top-right
edge of the feasible region, then every point of this edge is an optimal solution. Why
is this called a linear program? Because all constraints are linear inequalities, and the
objective function is a linear function. There is also a reason why it is called a linear
program, but we won’t get into this here (see [3] for more background).

Using vector and matrix notation, a linear program can succinctly be written as
follows.
 132

CG 2012 11.3. Minimum-area Enclosing Annulus

(LP) maximize cT x
subject to Ax ⩽ b

Here, c, x ∈ R
d, b ∈ R
n, A ∈ R
n×d, and ·T denotes the transpose operation. The in-
equality “⩽” is interpreted componentwise. The vector x represents the variables, c
is called the objective function vector, b the right-hand side, and A the constraint
matrix.

To solve a linear programs means to either report that the problem is infeasible or
unbounded, or to compute an optimal solution x
∗. If we can solve linear programs, we
can also decide linear separability of point sets. For this, we check whether the linear
program
maximize 0
subject to h1p1 + h2p2 + · · · + hdpd − h0 ⩽ 0, p ∈ P,
h1q1 + h2q2 + · · · + hdqd − h0 ⩾ 0, q ∈ Q.

in the d + 1 variables h0, h1, h2, . . . , hd and objective function vector c = 0 is feasible or
not. The fact that some inequalities are of the form “⩾” is no problem, of course, since
we can multiply an inequality by −1 to turn “⩾” into “⩽”.

11.3 Minimum-area Enclosing Annulus

Here is another geometric problem that we can write as a linear program, although this is
less obvious. Given a point set P ⊆ R
2, ﬁnd a minimum-area annulus (region between
two concentric circles) that contains P; see Figure 11.5 for an illustration.
The optimal annulus can be used to test whether the point set P is (approximately)
on a common circle which is the case if the annulus has zero (or small) area.
Let us write this as an optimization problem in the variables c = (c1, c2) ∈ R
2 (the
center) and r, R ∈ R (the small and the large radius).

minimize π(R2 − r
2)
subject to r
2 ⩽ ∥p − c∥2 ⩽ R2, p ∈ P.

This neither has a linear objective function nor are the constraints linear inequalities.
But a variable substitution will take care of this. We deﬁne new variables

u := r
2 − ∥c∥2, (11.3)
v := R2 − ∥c∥2. (11.4)

Omitting the factor π in the objective function does not aﬀect the optimal solution (only
its value), hence we can equivalently work with the objective function v − u = R2 − r
2.
The constraint r
2 ⩽ ∥p − c∥2 is equivalent to r
2 ⩽ ∥p∥2 − 2pT c + ∥c∥2, or

u + 2pT c ⩽ ∥p∥2.
 133

Chapter 11. Linear Programming CG 2012

R

r

c

Figure 11.5: A minimum-area annulus containing P

In the same way, ∥p − c∥ ⩽ R turns out to be equivalent to

v + 2pT c ⩾ ∥p∥2.

This means, we now have a linear program in the variables u, v, c1, c2:

maximize u − v
subject to u + 2pT c ⩽ ∥p∥2, p ∈ P
v + 2pT c ⩾ ∥p∥2, p ∈ P.

From optimal values for u, v and c, we can also reconstruct r
2 and R2 via (11.3) and (11.4).
It cannot happen that r
2 obtained in this way is negative: since we have r
2 ⩽ ∥p − c∥2

for all p, we could still increase u (and hence r
2 to at least 0), which is a contradicition
to u − v being maximal.

Exercise 11.5 a) Prove that the problem of ﬁnding a largest disk inside a convex
polygon can be formulated as a linear program! What is the number of variables
in your linear program?

b) Prove that the problem of testing whether a simple polygon is starshaped can be
formulated as a linear program.

Exercise 11.6 Given a simple polygon P as a list of vertices along its boundary. De-
scribe a linear time algorithm to decide whether P is star-shaped and—if so—to
construct the so-called kernel of P, that is, the set of all star-points.

134

CG 2012 11.4. Solving a Linear Program

11.4 Solving a Linear Program

Linear programming was ﬁrst studied in the 1930’s -1950’s, and some of its original
applications were of a military nature. In the 1950’s, Dantzig invented the simplex
method for solving linear programs, a method that is fast in practice but is not known
to come with any theoretical guarantees [1].
The computational complexity of solving linear programs was unresolved until 1979
when Leonid Khachiyan discovered a polynomial-time algorithm known as the ellipsoid
method [2]. This result even made it into the New York times.
From a computational geometry point of view, linear programs with a ﬁxed number
of variables are of particular interest (see our two applications above, with d and 4
variables, respectively, where d may be 2 or 3 in some relavant cases). As was ﬁrst shown
by Megiddo, such linear programs can be solved in time O(n), where n is the number of
constraints [4]. In the next lecture, we will describe a much simpler randomized O(n)
algorithm due to Seidel [5].

Questions

51. What is a linear program? Give a precise deﬁnition! How can you visualize
a linear program? What does it mean that the linear program is infeasible /
unbounded?

52. Show an application of linear programming! Describe a geometric problem that
can be formulated as a linear program, and give that formulation!

References

[1] G. B. Dantzig, Linear Programming and Extensions, Princeton University Press,
Princeton, NJ, 1963.

[2] L. G. Khachiyan, Polynomial algorithms in linear programming, U.S.S.R. Comput.
Math. and Math. Phys 20 (1980), 53–72.

[3] J. Matoušek and B. Gärtner, Understanding and Using Linear Programming, Uni-
versitext, Springer-Verlag, 2007.

[4] N. Megiddo, Linear programming in linear time when the dimension is ﬁxed, J. ACM
31 (1984), 114–127.

[5] R. Seidel, Small-dimensional linear programming and convex hulls made easy, Dis-
crete Comput. Geom. 6 (1991), 423–434.

135

Chapter 12

A randomized Algorithm for Linear
Programming

Let us recall the setup from last lecture: we have a linear program of the form

(LP) maximize cT x
subject to Ax ⩽ b, (12.1)

where c, x ∈ R
d (there are d variables), b ∈ R
n (there are n constraints), and A ∈ R
n×d.
The scenario that we are interested in here is that d is a (small) constant, while n tends
to inﬁnity.
The goal of this lecture is to present a randomized algorithm (due to Seidel [2]) for
solving a linear program whose expected runtime is O(n). The constant behind the
big-O will depend exponentially on d, meaning that this algorithm is practical only for
small values of d.
To prepare the ground, let us ﬁrst get rid of the unboundedness issue. We add to our
linear program a set of 2d constraints

−M ⩽ xi ⩽ M, i = 1, 2, . . . d, (12.2)

where M is a symbolic constant assumed to be larger than any real number that it is
compared with. Formally, this can be done by computing with rational functions in M
(quotients of polynomials of degree d in the “variable “M), rather than real numbers.
The original problem is bounded if and only if the solution of the new (and bounded)
problem does not depend on M. This is called the big-M method.
Now let H, |H| = n, denote the set of original constraints. For h ∈ H, we write the
corresponding constraint as ahx ⩽ bh.

Deﬁnition 12.3 For Q, R ⊆ H, Q∩R = ∅, let x
∗(Q, R) denote the lexicographically largest
optimal solution of the linear program

LP(Q,R) maximize cT x
subject to ahx ⩽ bh, h ∈ Q
ahx = bh, h ∈ R
−M ⩽ xi ⩽ M, i = 1, 2, . . . , d.

137

Chapter 12. A randomized Algorithm for Linear Programming CG 2012

If this linear program has no feasible solution, we set x
∗(Q, R) = ∞.

What does this mean? We delete some of the original constraints (the ones not in
Q ∪R, and we require some of the constraints to hold with equality (the ones in R). Since
every linear equation ahx = bh can be simulated by two linear inequalities ahx ⩽ bh
and ahx ⩾ bh, this again assumes the form of a linear program. By the big-M method,
this linear program is bounded, but it may be infeasible. If it is feasible, there may
be several optimal solutions, but choosing the lexicographically largest one leads to a
unique solution x
∗(Q, R).
Our algorithm will compute x
∗(H, ∅), the lexicographically largest optimal solution
of (12.1) subject to the additional bounding-box constraint (12.2). We also assume that
x
∗(H, ∅) ̸= ∞, meaning that (12.1) is feasible. At the expense of solving an auxiliary
problem with one extra variable, this may be assumed w.l.o.g. (Exercise).

Exercise 12.4 Suppose that you have an algorithm A for solving feasible linear pro-
grams of the form

(LP) maximize cT x
subject to Ax ⩽ b,

where feasible means that there exists ˜x ∈ R
d such that A˜x ⩽ b. Extend algorithm
A such that it can deal with arbitrary (not necessarily feasible) linear programs of
the above form.

12.1 Helly’s Theorem

A crucial ingredient of the algorithm’s analysis is that the optimal solution x
∗(H, ∅) is
already determined by a constant number (at most d) of constraints. More generally,
the following holds.

Lemma 12.5 Let Q, R ⊆ H, Q ∩ R = ∅, such that the constraints in R are independent.
This means that the set {x ∈ R
d : ahx = bh, h ∈ R} has dimension d − |R|.
If x
∗(Q, R) ̸= ∞, then there exists S ⊆ Q, |S| ⩽ d − |R| such that

x
∗(S, R) = x
∗(Q, R).

The proof uses Helly’s Theorem, a classic result in convexity theory.

Theorem 12.6 (Helly’s Theorem [1]) Let C1, . . . Cn be n ⩾ d + 1 convex subsets of R
d.
If any d + 1 of the sets have a nonempty common intersection, then the common
intersection of all n sets is nonempty.

Even in R
1, this is not entirely obvious. There it says that for every set of intervals
with pairwise nonempty overlap there is one point contained in all the intervals. We will
not prove Helly’s Theorem here but just use it to prove Lemma 12.5.

138

CG 2012 12.2. Convexity, once more

Proof. (Lemma 12.5) The statement is trivial for |Q| ⩽ d − |R|, so assume |Q| > d − |R|.
Let
 L(R) := {x ∈ R
d : ahx = bh, h ∈ R}

and
 B := {x ∈ R
d : −M ⩽ xi ⩽ M, i = 1, . . . , d}.

For a vector x = (x1, . . . , xd), we deﬁne x0 = cT x, and we write x > x′ if (x0, x1, . . . , xd)
is lexicographically larger than (x′
0, x′
1, . . . , x′
d).
Let x
∗ = x
∗(Q, R) and consider the |Q| + 1 sets

Ch = {x ∈ R
d : ahx ⩽ bh} ∩ B ∩ L(R), h ∈ Q

and
 C0 = {x ∈ R
d : x > x
∗} ∩ B ∩ L(R).

The ﬁrst observation (that may require a little thinking in case of C0) is that all these
sets are convex. The second observation is that their common intersection is empty.
Indeed, any point in the common intersection would be a feasible solution ˜x of LP(Q, R)
with ˜x > x
∗ = x
∗(Q, R), a contradiction to x
∗(Q, R) being the lexicographically largest
optimal solution of LP(Q, R). The third observation is that since L(R) has dimension
d − |R|, we can after an aﬃne transformation assume that all our |Q| + 1 convex sets are
actually convex subsets of R
d−|R|.
Then, applying Helly’s Theorem yields a subset of d − |R| + 1 constraints with an
empty common intersection. Since all the Ch do have x
∗(Q, R) in common, this set of
constraints must contain C0. This means, there is S ⊆ Q, |S| = d − |R| such that

x ∈ Ch ∀h ∈ S ⇒ x /∈ C0.

In particular, x
∗(S, R) ∈ Ch for all h ∈ S, and so it follows that x
∗(S, R) ⩽ x
∗ = x
∗(Q, R).
But since S ⊆ Q, we also have x
∗(S, R) ⩾ x
∗(Q, R), and x
∗(S, R) = x
∗(Q, R) follows. 
12.2 Convexity, once more

We need a second property of linear programs on top of Lemma 12.5; it is also a conse-
quence of convexity of the constraints, but a much simpler one.

Lemma 12.7 Let Q, R ⊆ H, Q ∩ R ̸= ∅ and x
∗(Q, R) ̸= ∞. Let h ∈ Q. If

ahx
∗(Q \ {h}, R) > bh,

then
 x
∗(Q, R) = x
∗(Q \ {h}, R ∪ {h}).
 139

Chapter 12. A randomized Algorithm for Linear Programming CG 2012

Before we prove this, let us get an intuition. The vector x
∗(Q \ {h}, R) is the optimal
solution of LP(Q \ {h}, R). And the inequality ahx
∗(Q \ {h}, R) > bh means that the
constraint h is violated by this solution. The implication of the lemma is that at the
optimal solution of LP(Q, R), the constraint h must be satisﬁed with equality in which
case this optimal solution is at the same time the optimal solution of the more restricted
problem LP(Q \ {h}, R ∪ {h}).
Proof. Let us suppose for a contradition that

ahx
∗(Q, R) < bh

and consider the line segment s that connects x
∗(Q, R) with x
∗(Q \ {h}, R). By the
previous strict inequality, we can make a small step (starting from x
∗(Q, R)) along this
line segment without violating the constraint h (Figure 12.1). And since both x
∗(Q, R)
as well as x
∗(Q \ {h}, R) satisfy all other constraints in (Q \ {h}, R), convexity of the
constraints implies that this small step takes us to a feasible solution of LP(Q, R) again.
But this solution is lexicographically larger than x
∗(Q, R), since we move towards the
lexicographically larger vector x
∗(Q \ {h}, R); this is a contradiction. 
x (Q\{h}, R)

x (Q, R)*
 *
s
 h

Figure 12.1: Proof of Lemma 12.7

12.3 The Algorithm

The algorithm reduces the computation of x
∗(H, ∅) to the computation of x
∗(Q, R) for
various sets Q, R, where R is an independent set of constraints. Suppose you want to
compute x
∗(Q, R) (assuming that x
∗(Q, R) ̸= ∞). If Q = ∅, this is “easy”, since we have
a constant-size problem, deﬁned by R with |R| ⩽ d and 2d bounding-box constraints
−M ⩽ xi ⩽ M.
 140

CG 2012 12.4. Runtime Analysis

Otherwise, we choose h ∈ Q and recursively compute x
∗(Q \ {h}, R) ̸= ∞. We then
check whether constraint h is violated by this solution. If not, we are done, since then
x
∗(Q \ {h}, R) = x
∗(Q, R) (Think about why!). But if h is violated, we can use Lemma
12.7 to conclude that x
∗(Q, R) = x
∗(Q \ {h}, R ∪ {h}), and we recursively compute the
latter solution. Here is the complete pseudocode.

LP(Q, R):
IF Q = ∅ THEN
RETURN x
∗(∅, R)
ELSE
choose h ∈ Q uniformly at random
x
∗ := LP(Q \ {h}, R)
IF ahx
∗ ⩽ bh THEN
RETURN x
∗

ELSE
RETURN LP(Q \ {h}, R ∪ {h})
END
END

To solve the original problem, we call this algorithm with LP(H, ∅). It is clear that
the algorithm terminates since the ﬁrst argument Q becomes smaller in every recursive
call. It is also true (Exercise) that every set R that comes up during this algorithm is
indeed an independent set of constraints and in particular has at most d elements. The
correctness of the algorithm then follows from Lemma 12.7.

Exercise 12.8 Prove that all sets R of constraints that arise during a call to algorithm
LP(H, ∅) are independent, meaning that the set

{x ∈ R
d : ahx = bh, h ∈ R}

of points that satisfy all constraints in R with equality has dimension d − |R|.

12.4 Runtime Analysis

Now we get to the analysis of algorithm LP, and this will also reveal why the random
choice is important.
We will analyze the algorithm in terms of the expected number of violation tests
ahx
∗ ⩽ bh, and in terms of the expected number of basis computations x
∗(∅, R) that
it performs. This is a good measure, since these are the dominating operations of the
algorithm. Moreover, both violation test and basis computation are “cheap” operations
in the sense that they can be performed in time f(d) for some f.

141

Chapter 12. A randomized Algorithm for Linear Programming CG 2012

More speciﬁcally, a violation test can be performed in time O(d); the time needed
for a basis computation is less clear, since it amounts to solving a small linear program
itself. Let us suppose that it is done by brute-force enumeration of all vertices of the
bounded polyhedron deﬁned by the at most 3d (in)equalities

ahx = bh, h ∈ R

and
 −M ⩽ xi ⩽ M, i = 1, . . . , d.

12.4.1 Violation Tests

Lemma 12.9 Let T (n, j) be the maximum expected number of violation tests performed
in a call to LP(Q, R) with |Q| = n and |R| = d − j. For all j = 0, . . . , d,

T (0, j) = 0

T (n, j) ⩽ T (n − 1, j) + 1 + j
nT (n − 1, j − 1), n > 0.

Note that in case of j = 0, we may get a negative argument on the right-hand side, but
due to the factor 0/n, this does not matter.
Proof. If |Q| = ∅, there is no violation test. Otherwise, we recursively call LP(Q \ {h}, R)
for some h which requires at most T (n − 1, j) violation tests in expectation. Then there
is one violation test within the call to LP(Q, R) itself, and depending on the outcome, we
perform a second recursive call LP(Q \ {h}, R ∪ {h}) which requires an expected number
of at most T (n − 1, j − 1) violation tests. The crucial fact is that the probability of
performing a second recursive call is at most j/n.
To see this, ﬁx some S ⊆ Q, |S| ⩽ d − |R| = j such that x
∗(Q, R) = x
∗(S, R). Such a
set S exists by Lemma 12.5. This means, we can remove from Q all constraints except
the ones in S, without changing the solution.
If h ̸∈ S, we thus have

x
∗(Q, R) = x
∗(Q \ {h}, R),

meaning that we have already found x
∗(Q, R) after the ﬁrst recursive call; in particular,
we will then have ahx
∗ ⩽ bh, and there is no second recursive call. Only if h ∈ S (and
this happens with probability |S|/n ⩽ j/n), there can be a second recursive call. 
The following can easily be veriﬁed by induction.

Theorem 12.10

T (n, j) ⩽
 j∑

i=0
 1
i! j!n.

Since ∑j
i=0 1
i! ⩽ ∑∞
i=0 1
i! = e, we have T (n, j) = O(j!n). If d ⩾ j is constant, this is O(n).

142

CG 2012 12.4. Runtime Analysis

12.4.2 Basis Computations

To count the basis computations, we proceed as in Lemma 12.9, except that the “1” now
moves to a diﬀerent place.

Lemma 12.11 Let B(n, j) be the maximum expected number of basis computations
performed in a call to LP(Q, R) with |Q| = n and |R| = d − j. For all j = 0, . . . , d,

B(0, j) = 1

B(n, j) ⩽ B(n − 1, j) + j
nB(n − 1, j − 1), n > 0.

Interestingly, B(n, j) turns out to be much smaller than T (n, j) which is good since a
basic computation is much more expensive than a violation test. Here is the bound that
we get.

Theorem 12.12

B(n, j) ⩽ (1 + Hn)j = O(logj n),

where Hn is the n-th Harmonic number.

Proof. This is also a simple induction, but let’s do this one since it is not entirely
obvious. The statement holds for n = 0 with the convention that H0 = 0. It also holds
for j = 0, since Lemma 12.11 implies B(n, 0) = 1 for all n. For n, j > 0, we inductively
obtain

B(n, j) ⩽ (1 + Hn−1)j + j
n(1 + Hn−1)j−1

⩽
 j∑

k=0
 ( j
k
)
(1 + Hn−1)j−k( 1
n)k

= (1 + Hn−1 + 1
n)j = (1 + Hn)j.

The second inequality uses the fact that the terms (1 + Hn−1)j and j
n(1 + Hn−1)j−1 are
the ﬁrst two terms of the sum in the second line. 
12.4.3 The Overall Bound

Putting together Theorems 12.10 and 12.12 (for j = d, corresponding to the case R = ∅),
we obtain the following

Theorem 12.13 A linear program with n constraints in d variables (d a constant) can
be solved in time O(n).
 143

Chapter 12. A randomized Algorithm for Linear Programming CG 2012

Questions

53. What is Helly’s Theorem? Give a precise statement and outline the application
of the theorem for linear programming (Lemma 12.5).

54. Outline an algorithm for solving linear programs! Sketch the main steps of
the algorithm and the correctness proof! Also explain how one may achieve the
preconditions of feasibility and boundedness.

55. Sketch the analysis of the algorithm! Explain on an intuitive level how ran-
domization helps, and how the recurrence relations for the expected number of
violation tests and basis computations are derived. What is the expected runtime
of the algorithm?

References

[1] H. Edelsbrunner, Algorithms in Combinatorial Geometry, volume 10 of EATCS
Monographs on Theoretical Computer Science, Springer-Verlag, Heidelberg, West
Germany, 1987.

[2] R. Seidel, Small-dimensional linear programming and convex hulls made easy, Dis-
crete Comput. Geom. 6 (1991), 423–434.

144

Chapter 13

Line Arrangements

During the course of this lecture we encountered several situations where it was conve-
nient to assume that a point set is “in general position”. In the plane, general position
usually amounts to no three points being collinear and/or no four of them being cocir-
cular. This raises an algorithmic question: How can we test for n given points whether
or not three of them are collinear? Obviously, we can test all triples in O(n
3) time. Can
we do better? In order to answer this question, we will take a detour through the dual
plane.
Observe that points and hyperplanes in R
d are very similar objects, given that both
can be described using d coordinates/parameters. It is thus tempting to match these
parameters to each other and so create a mapping between points and hyperplanes. In
R
2 hyperplanes are lines and the standard projective duality transform maps a point
p = (px, py) to the line p∗ : y = pxx − py and a non-vertical line g : y = mx + b to the
point g∗ = (m, −b).

Proposition 13.1 The standard projective duality transform is incidence preserving: p ∈ g ⇐⇒ g∗ ∈ p∗ and order preserving: p is above g ⇐⇒ g∗ is above p∗.

Exercise 13.2 Prove Proposition 13.1.

Exercise 13.3 Describe the image of the following point sets under this mapping

a) a halfplane

b) k ⩾ 3 collinear points

c) a line segment

d) the boundary points of the upper convex hull of a ﬁnite point set.

145

Chapter 13. Line Arrangements CG 2012

Another way to think of duality is in terms of the parabola P : y = 1
2 x
2. For a point
p on P, the dual line p∗ is the tangent to P at p. For a point p not on P, consider the
vertical projection p ′ of p onto P: the slopes of p∗ and p ′∗ are the same, just p∗ is shifted
by the diﬀerence in y-coordinates.
 p
p
∗
 q

q
∗

ℓ∗
 ℓ

Figure 13.1: Point ↔ line duality with respect to the parabola y = 1
2x
2.

The question of whether or not three points in the primal plane are collinear trans-
forms to whether or not three lines in the dual plane meet in a point. This question in
turn we will answer with the help of line arrangements, as deﬁned below.

13.1 Arrangements

The subdivision of the plane induced by a ﬁnite set L of lines is called the arrangement
A(L). Observe that all cells of the subdivision are intersections of halfplanes and thus
convex. A line arrangement is simple if no two lines are parallel and no three lines meet
in a point. Although lines are unbounded, we can regard a line arrangement a bounded
object by (conceptually) putting a suﬃciently large box around that contains all vertices.
Such a box can be constructed in O(n log n) time for n lines.

Exercise 13.4 How?

Moreover, we can view a line arrangement as a planar graph by adding an additional
vertex at “inﬁnity”, that is incident to all rays which leave this bounding box. For
algorithmic purposes, we will mostly think of an arrangement as being represented by a
doubly connected edge list (DCEL), cf. Section 5.2.

Theorem 13.5 A simple arrangement A(L) of n lines in R
2 has (
n
2) vertices, n
2 edges,
and (n
2) + n + 1 faces/cells.

Proof. Since all lines intersect and all intersection points are pairwise distinct, there are(n
2) vertices.
 146

CG 2012 13.2. Construction

The number of edges we count using induction on n. For n = 1 we have 12 = 1 edge.
By adding one line to an arrangement of n − 1 lines we split n − 1 existing edges into
two and introduce n new edges along the newly inserted line. Thus, there are in total
(n − 1)2 + 2n − 1 = n
2 − 2n + 1 + 2n − 1 = n
2 edges.
The number f of faces can now be obtained from Euler’s formula v − e + f = 2, where
v and e denote the number of vertices and edges, respectively. However, in order to
apply Euler’s formula we need to consider A(L) as a planar graph and take the symbolic
“inﬁnite” vertex into account. Therefore,

f = 2 − ((n
2
) + 1) + n
2 = 1 + 1
2 (2n
2 − n(n − 1)) = 1 + 1
2 (n
2 + n) = 1 + (
n
2
) + n . 
The complexity of an arrangement is simply the total number of vertices, edges, and faces
(in general, cells of any dimension).

Exercise 13.6 Consider a set of lines in the plane with no three intersecting in a
common point. Form a graph G whose vertices are the intersection points of the
lines and such that two vertices are adjacent if and only if they appear consecutively
along one of the lines. Prove that χ(G) ⩽ 3, where χ(G) denotes the chromatic
number of the graph G. In other words, show how to color the vertices of G using
at most three colors such that no two adjacent vertices have the same color.

13.2 Construction

As the complexity of a line arrangement is quadratic, there is no need to look for a sub-
quadratic algorithm to construct it. We will simply construct it incrementally, inserting
the lines one by one. Let ℓ1, . . . , ℓn be the order of insertion.
At Step i of the construction, locate ℓi in the leftmost cell of A({ℓ1, . . . , ℓi−1}) it
intersects. (The halfedges leaving the inﬁnite vertex are ordered by slope.) This takes
O(i) time. Then traverse the boundary of the face F found until the halfedge h is found
where ℓi leaves F (see Figure 13.2 for illustration). Insert a new vertex at this point,
splitting F and h and continue in the same way with the face on the other side of h.
The insertion of a new vertex involves splitting two halfedges and thus is a constant
time operation. But what is the time needed for the traversal? The complexity of
A({ℓ1, . . . , ℓi−1}) is Θ(i2), but we will see that the region traversed by a single line has
linear complexity only.

13.3 Zone Theorem

For a line ℓ and an arrangement A(L), the zone ZA(L)(ℓ) of ℓ in A(L) is the set of cells
from A(L) whose closure intersects ℓ.
 147

Chapter 13. Line Arrangements CG 2012

ℓ

Figure 13.2: Incremental construction: Insertion of a line ℓ. (Only part of the ar-
rangement is shown in order to increase readability.)

Theorem 13.7 Given an arrangement A(L) of n lines in R
2 and a line ℓ (not neces-
sarily from L), the total number of edges in all cells of the zone ZA(L)(ℓ) is at most
6n.

Proof. Without loss of generality suppose that ℓ is horizontal and that none of the lines
from L is horizontal. (The ﬁrst condition can be addressed by rotating the plane and
the second by deciding that the left vertex of a horizontal edge is higher than the right
vertex.)
For each cell of ZA(L)(ℓ) split its boundary at its topmost
vertex and at its bottommost vertex and orient all edges from
bottom to top. Those edges that have the cell to their right are
called left-bounding for the cell and those edges that have the
cell to their left are called right-bounding. For instance, for the
cell depicted to the right all left-bounding edges are shown blue
and bold.
We will show that there are at most 3n left-bounding edges in ZA(L)(ℓ) by induction
on n. By symmetry, the same bound holds also for the number of right-bounding edges
in ZA(L)(ℓ).
For n = 1, there is at most one (exactly one, unless ℓ is parallel to and lies below the
only line in L) left-bounding edge in ZA(L)(ℓ) and 1 ⩽ 3n = 3. Assume the statement is
true for n − 1.
If no line from L intersects ℓ, then all lines in L ∪ {ℓ} are parallel and there are at
most 2 < 3n left-bounding edges in ZA(L)(ℓ). Else consider the rightmost line r from
L intersecting ℓ and the arrangement A(L \ {r}). By the induction hypothesis there are
at most 3n − 3 left-bounding edges in ZA(L\{r})(ℓ). Adding r back adds at most three
new left-bounding edges: At most two edges (call them ℓ0 and ℓ1) of the rightmost cell
of ZA(L\{r})(ℓ) are intersected by r and thereby split in two. Both of these two edges

148

CG 2012 13.4. The Power of Duality

ℓ
 r

ℓ0
 ℓ1

Figure 13.3: At most three new left-bounding edges
are created by adding r to A(L \ {r}).

may be left-bounding and thereby increase the number of left-bounding edges by at most
two. In any case, r itself contributes exactly one more left-bounding edge to that cell.
The line r cannot contribute a left-bounding edge to any cell other than the rightmost:
to the left of r, the edges induced by r form right-bounding edges only and to the right
of r all other cells touched by r (if any) are shielded away from ℓ by one of ℓ0 or ℓ1.
Therefore, the total number of left-bounding edges in ZA(L)(ℓ) is bounded from above
by 3 + 3n − 3 = 3n. 
Corollary 13.8 The arrangement of n lines in R
2 can be constructed in optimal O(n
2)
time and space.

Proof. Use the incremental construction described above. In Step i, for 1 ⩽ i ⩽ n,
we do a linear search among i − 1 elements to ﬁnd the starting face and then traverse
(part of) the zone of the line ℓi in the arrangement A({ℓ1, . . . , ℓi−1}). By Theorem 13.7
the complexity of this zone and hence the time complexity of Step i altogether is O(i).
Overall we obtain ∑n
i=1 ci = O(n
2) time (and space), for some constant c > 0, which is
optimal by Theorem 13.5. 
The corresponding bounds for hyperplane arrangements in R
d are Θ(n
d) for the com-
plexity of a simple arrangement and O(n
d−1) for the complexity of a zone of a hyperplane.

Exercise 13.9 For an arrangement A of a set of n lines in R
2, let F := ⋃
C is cell of A C
denote the union of the closure of all bounded cells. Show that the complexity
(number of vertices and edges of the arrangement lying on the boundary) of F is
O(n).

13.4 The Power of Duality

The real beauty and power of line arrangements becomes apparent in context of projective
point ↔ line duality. The following problems all can be solved in O(n
2) time and space

149

Chapter 13. Line Arrangements CG 2012

by constructing the dual arrangement.

General position test. Given n points in R
2, are any three of them collinear? (Dual: do
three lines meet in a point?)

Minimum area triangle. Given n points in R
2, what is the minimum area triangle spanned
by any three of them? For any vertex ℓ∗ of the dual arrangement (primal: line ℓ through
two points p and q) ﬁnd the closest point vertically above/below ℓ∗ through which an
input line passes (primal: closest line below/above and parallel to ℓ that passes through
an input point). In this way one can ﬁnd O(n
2) candidate triangles by constructing the
arrangement of the n dual lines
1 The smallest among those candidates can be determined
by a straightforward minimum selection (comparing the area of the corresponding trian-
gles). Observe that vertical distance is not what determines the area of the corresponding
triangle but orthogonal distance. However, the points that minimize these measures for
any ﬁxed line are the same. . .

Exercise 13.10 A set P of n points in the plane is said to be in ε-general position for
ε > 0 if no three points of the form

p + (x1, y1), q + (x2, y2), r + (x3, y3)

are collinear, where p, q, r ∈ P and |xi|, |yi| < ε, for i ∈ {1, 2, 3}. In words: P remains
in general position under changing point coordinates by less than ε each.
Give an algorithm with runtime O(n
2) for checking whether a given point set P
is in ε-general position.

13.5 Sorting all Angular Sequences.

Theorem 13.11 Consider a set P of n points in the plane. For a point q ∈ P let cP(q)
denote the circular sequence of points from S \ {q} ordered counterclockwise around
q (in order as they would be encountered by a ray sweeping around q). All cP(q),
q ∈ P, collectively can be obtained in O(n
2) time.

Proof. Assume without loss of generality that no two points in P have the same x-
coordinate (else rotate the plane inﬁnitesimally). Consider the projective dual P∗ of P.
An angular sweep around a point q ∈ P in the primal plane corresponds to a traversal
of the line q
∗ from left to right in the dual plane. (A collection of lines through a single
point q corresponds to a collection of points on a single line q
∗ and slope corresponds
to x-coordinate.) Clearly, the sequence of intersection points along all lines in P∗ can

1For instance, maintain over the incremental construction for each vertex a vertically closest line. The
number of vertices to be updated during insertion of a line ℓ corresponds to the complexity of the zone of
ℓ in the arrangement constructed so far. Therefore maintaining this information comes at no extra cost
asymptotically.
 150

CG 2012 13.6. Segment Endpoint Visibility Graphs

be obtained by constructing the arrangement in O(n
2) time. In the primal plane, any
such sequence corresponds to an order of the remaining points according to the slope of
the connecting line; to construct the circular sequence of points as they are encountered
around q, we have to split the sequence obtained from the dual into those points that
are to the left of q and those that are to the right of q; concatenating both yields the
desired sequence. 
Exercise 13.12 (Eppstein [1]) Describe an O(n
2) time algorithm that given a set P of n
points in the plane ﬁnds a subset of ﬁve points that form a strictly convex empty
pentagon (or reports that there is none if that is the case). Empty means that the
convex pentagon may not contain any other points of P.
Hint: Start with a point p ∈ P that is extremal in one direction and try to ﬁnd
out whether there is a solution P ′ containing p. For this, consider the star-shaped
polygon that visits all points in radial order, as seen from p.
Remark: It was shown by Harborth [5] that every set of ten or more points in
general position contains a subset of ﬁve points that form a strictly convex empty
pentagon.

13.6 Segment Endpoint Visibility Graphs

A fundamental problem in motion planning is to ﬁnd a short(est) path between two
given positions in some domain, subject to certain constraints. As an example, suppose
we are given two points p, q ∈ R
2 and a set S ⊂ R
2 of obstacles. What is the shortest
path between p and q that avoids S?

Observation 13.13 The shortest path (if it exists) between two points that does not
cross a ﬁnite set of ﬁnite polygonal obstacles is a polygonal path whose interior
vertices are obstacle vertices.

One of the simplest type of obstacle conceivable is a line segment. In general the
plane may be disconnected with respect to the obstacles, for instance, if they form a
closed curve. However, if we restrict the obstacles to pairwise disjoint line segments then
there is always a free path between any two given points. Apart from start and goal
position, by the above observation we may restrict our attention concerning shortest
paths to straight line edges connecting obstacle vertices, in this case, segment endpoints.

Deﬁnition 13.14 Consider a set S of n disjoint line segments in R
2. The segment
endpoint visibility graph V(S) is a geometric straight line graph deﬁned on the segment
endpoints. Two segment endpoints p and q are connected in V(S) if and only if the line segment pq is in S or pq ∩ s ⊆ {p, q} for every segment s ∈ S.

151

Chapter 13. Line Arrangements CG 2012

Figure 13.4: A set of disjoint line segments and their endpoint visibility graph.

If all segments are on the convex hull, the visibility graph is complete. If they form
parallel chords of a convex polygon, the visibility graph consists of copies of K4, glued
together along opposite edges and the total number of edges is linear only.
These graphs also appear in the context of the following question: Given a set of
disjoint line segments, is it possible to connect them to form (the boundary of) a simple
polygon? Is it easy to see that this is not possible in general: Just take three parallel
chords of a convex polygon (Figure 13.5a). However, if we do not insist that the segments
appear on the boundary, but allow them to be diagonals or epigonals, then it is always
possible [7, 6]. In other words, the segment endpoint visibility graph of disjoint line
segments is Hamiltonian, unless all segments are collinear. It is actually essential to
allow epigonals and not only diagonals [9, 4] (Figure 13.5b).

(a) (b)

Figure 13.5: Sets of disjoint line segments that do not allow certain polygons.

Constructing V(S) for a given set S of disjoint segments in a brute force way takes
O(n
3) time. (Take all pairs of endpoints and check all other segments for obstruction.)

Theorem 13.15 (Welzl [10]) The segment endpoint visibility graph of n disjoint line
segments can be constructed in worst case optimal O(n
2) time.

Proof. For simplicity we assume general position, that is, no three endpoints are collinear
and no two have the same x-coordinate. It is no problem to handle such degeneracies
explicitly.
We have seen above how all sorted angular sequences can be obtained from the dual
line arrangement in O(n
2) time. Topologically sweep the arrangement from left to right
(corresponds to changing the slope of the primal rays from −∞ to +∞) while maintaining
for each segment endpoint p the segment s(p) it currently “sees” (if any). Initialize by

152

CG 2012 13.7. Ham Sandwich Theorem

brute force in O(n
2) time (direction vertically downwards). Each intersection of two lines
corresponds to two segment endpoints “seeing” each other along the primal line whose
dual is the point of intersection. In order to process an intersection, we only need that
all preceding (located to the left) intersections of the two lines involved have already
been processed. This order corresponds to a topological sort of the arrangement graph
where all edges are directed from left to right. (Clearly, this graph is acyclic, that is, it
does not contain a directed cycle.) A topological sort can be obtained, for instance, via
(reversed) post order DFS in time linear in the size of the graph (number of vertices and
edges), which in our case here is O(n
2).
When processing an intersection, there are four cases. Let p and q be the two points
involved such that p is to the left of q.

1. The two points belong to the same input segment → output the edge pq, no change
otherwise.

2. q is obscured from p by s(p) → no change.

3. q is endpoint of s(p) → output pq and update s(p) to s(q).

4. Otherwise q is endpoint of a segment t that now obscures s(p) → output pq and
update s(p) to t.

Thus any intersection can be processed in constant time and the overall runtime of this
algorithm is quadratic. 
13.7 Ham Sandwich Theorem

Suppose two thieves have stolen a necklace that contains rubies and diamonds. Now it
is time to distribute the prey. Both, of course, should get the same number of rubies
and the same number of diamonds. On the other hand, it would be a pity to completely
disintegrate the beautiful necklace. Hence they want to use as few cuts as possible to
achieve a fair gem distribution.
To phrase the problem in a geometric (and somewhat more general) setting: Given
two ﬁnite sets R and D of points, construct a line that bisects both sets, that is, in either
halfplane deﬁned by the line there are about half of the points from R and about half of
the points from D. To solve this problem, we will make use of the concept of levels in
arrangements.

Deﬁnition 13.16 Consider an arrangement A(L) induced by a set L of n non-vertical
lines in the plane. We say that a point p is on the k-level in A(L) if and only p lies
on some line from L and there are at most k − 1 lines below and at most n − k lines
above p. The 1-level and the n-level are also referred to as lower and upper envelope,
respectively.
 153

Chapter 13. Line Arrangements CG 2012

Figure 13.6: The 3-level of an arrangement.

Another way to look at the k-level is to consider the lines to be real functions; then the
lower envelope is the pointwise minimum of those functions, and the k-level is deﬁned
by taking pointwise the k
th-smallest function value.

Theorem 13.17 Let R, D ⊂ R
2 be ﬁnite sets of points. Then there exists a line that
bisects both R and D. That is, in either open halfplane deﬁned by ℓ there are no
more than |R|/2 points from R and no more than |D|/2 points from D.

Proof. Without loss of generality suppose that both |R| and |D| are odd. (If, say, |R| is
even, simply remove an arbitrary point from R. Any bisector for the resulting set is also
a bisector for R.) We may also suppose that no two points from R ∪ D have the same
x-coordinate. (Otherwise, rotate the plane inﬁnitesimally.)
Let R∗ and D∗ denote the set of lines dual to the points from R and D, respectively.
Consider the arrangement A(R∗). The median level of A(R∗) deﬁnes the bisecting lines
for R. As |R| = |R∗| is odd, both the leftmost and the rightmost segment of this level
are deﬁned by the same line ℓr from R∗, the one with median slope. Similarly there is a
corresponding line ℓd in A(D∗).
Since no two points from R ∪ D have the same x-coordinate, no two lines from R∗ ∪ D∗

have the same slope, and thus ℓr and ℓd intersect. Consequently, being piecewise linear
continuous functions, the median level of A(R∗) and the median level of A(D∗) intersect
(see Figure 13.7 for an example). Any point that lies on both median levels corresponds
to a primal line that bisects both point sets simultaneously. 
How can the thieves use Theorem 13.17? If they are smart, they drape the necklace
along some convex curve, say, a circle. Then by Theorem 13.17 there exists a line that
simultaneously bisects the set of diamonds and the set of rubies. As any line intersects
the circle at most twice, the necklace is cut at most twice. It is easy to turn the proof
given above into an O(n
2) algorithm to construct a line that simultaneously bisects both
sets.
You can also think of the two point sets as a discrete distribution of a ham sandwich
that is to be cut fairly, that is, in such a way that both parts have the same amount of
ham and the same amount of bread. That is where the name “ham sandwich cut” comes

154

CG 2012 13.8. 3-Sum

Figure 13.7: An arrangement of 3 green lines (solid) and 3 blue lines (dashed) and
their median levels (marked bold on the right hand side).

from. The theorem also holds in R
d, saying that any d ﬁnite point sets (or ﬁnite Borel
measures, if you want) can simultaneously be bisected by a hyperplane. This implies
that the thieves can fairly distribute a necklace consisting of d types of gems using at
most d cuts.
Algorithmically the problem gets harder in higher dimension. But in the plane, a
ham sandwich cut can be found in linear time using a sophisticated prune and search
algorithm by Lo, Matoušek and Steiger [8].

Exercise 13.18 The goal of this exercise is to develop a data structure for halfspace
range counting.

a) Given a set P ⊂ R
2 of n points in general position, show that it is possible to
partition this set by two lines such that each region contains at most ⌈ n
4 ⌉ points.

b) Design a data structure of size O(n), which can be constructed in time O(n log n)
and allows you, for any halfspace h, to output the number of points |P ∩ h| of P
contained in this halfspace h in time O(n
α), for some 0 < α < 1.

Exercise 13.19 Prove or disprove the following statement: Given three ﬁnite sets
A, B, C of points in the plane, there is always a circle or a line that bisects A, B and
C simultaneously (that is, no more than half of the points of each set are inside or
outside the circle or on either side of the line, respectively).

13.8 3-Sum

The 3-Sum problem is the following: Given a set S of n integers, does there exist a
three-tuple
2 of elements from S that sum up to zero? By testing all three-tuples this

2That is, an element of S may be chosen twice or even three times, although the latter makes sense for
the number 0 only. :-)
 155

Chapter 13. Line Arrangements CG 2012

can obviously be solved in O(n
3) time. If the tuples to be tested are picked a bit more
cleverly, we obtain an O(n
2) algorithm.
Let (s1, . . . , sn) be the sequence of elements from S in increasing order. Then we test
the tuples as follows.

For i = 1, . . . , n {
j = i, k = n.
While k ⩾ j {
If si + sj + sk = 0 then exit with triple si, sj, sk.
If si + sj + sk > 0 then k = k − 1 else j = j + 1.
}
}

The runtime is clearly quadratic (initial sorting can be done in O(n log n) time).
Regarding the correctness observe that the following is an invariant that holds at the
start of every iteration of the inner loop: si + sx + sk < 0, for all i ⩽ x < j, and
si + sj + sx > 0, for all k < x ⩽ n.
Interestingly, this is essentially the best algorithm known for 3-Sum. It is widely
believed that the problem cannot be solved in sub-quadratic time, but so far this has
been proved in some very restricted models of computation only, such as the linear
decision tree model [2].

13.9 3-Sum hardness

There is a whole class of problems that are equivalent to 3-Sum up to sub-quadratic time
reductions [3]; such problems are referred to as 3-Sum-hard.

Deﬁnition 13.20 A problem P is 3-Sum-hard if and only if every instance of 3-Sum
of size n can be solved using a constant number of instances of P—each of O(n)
size—and o(n
2) additional time.

For instance, it is not hard to show that the following variation of 3-Sum—let us
denote it by 3-Sum◦—is 3-Sum hard: Given a set S of n integers, does there exist a
three-element subset of S whose elements sum up to zero?
As another example, consider the Problem GeomBase: Given n points on the three
horizontal lines y = 0, y = 1, and y = 2, is there a non-horizontal line that contains at
least three of them?
3-Sum can be reduced to GeomBase as follows. For an instance S = {s1, . . . , sn} of
3-Sum, create an instance P of GeomBase in which for each si there are three points in
P: (si, 0), (−si/2, 1), and (si, 2). If there are any three collinear points in P, there must
be one from each of the lines y = 0, y = 1, and y = 2. So suppose that p = (si, 0),
q = (−sj/2, 1), and r = (sk, 2) are collinear. The inverse slope of the line through p
and q is −sj/2−si
1−0 = −sj/2 − si and the inverse slope of the line through q and r is

156

CG 2012 13.9. 3-Sum hardness

sk+sj/2
2−1 = sk + sj/2. The three points are collinear if and only if the two slopes are equal,
that is, −sj/2 − si = sk + sj/2 ⇐⇒ si + sj + sk = 0.
A very similar problem is General Position, in which one is given n arbitrary points
and has to decide whether any three are collinear. For an instance S of 3-Sum◦, create
an instance P of General Position by projecting the numbers si onto the curve y = x
3,
that is, P = {(a, a3) | a ∈ S}.
Suppose three of the points, say, (a, a3), (b, b3), and (c, c3) are collinear. This is the
case if and only if the slopes of the lines through each pair of them are equal. (Observe
that a, b, and c are pairwise distinct.)

(b3 − a3)/(b − a) = (c3 − b3)/(c − b) ⇐⇒
b2 + a2 + ab = c2 + b2 + bc ⇐⇒
b = (c2 − a2)/(a − c) ⇐⇒
b = −(a + c) ⇐⇒
a + b + c = 0 .

Minimum Area Triangle is a strict generalization of General Position and, therefore, also
3-Sum-hard.
In Segment Splitting/Separation, we are given a set of n line segments and have to
decide whether there exists a line that does not intersect any of the segments but splits
them into two non-empty subsets. To show that this problem is 3-Sum-hard, we can
use essentially the same reduction as for GeomBase, where we interpret the points along
the three lines y = 0, y = 1, and y = 2 as suﬃciently small “holes”. The parts of the
lines that remain after punching these holes form the input segments for the Splitting
problem. Horizontal splits can be prevented by putting constant size gadgets somewhere
beyond the last holes, see the ﬁgure below. The set of input segments for the segment

splitting problem requires sorting the points along each of the three horizontal lines,
which can be done in O(n log n) = o(n
2) time. It remains to specify what “suﬃciently
small” means for the size of those holes. As all input numbers are integers, it is not
hard to see that punching a hole of (x − 1/4, x + 1/4) around each input point x is small
enough.
In Segment Visibility, we are given a set S of n horizontal line segments and two
segments s1, s2 ∈ S. The question is: Are there two points, p1 ∈ s1 and p2 ∈ s2 which
can see each other, that is, the open line segment p1p2 does not intersect any segment
from S? The reduction from 3-Sum is the same as for Segment Splitting, just put s1
above and s2 below the segments along the three lines.

157

Chapter 13. Line Arrangements CG 2012

In Motion Planning, we are given a robot (line segment), some environment (modeled
as a set of disjoint line segments), and a source and a target position. The question is:
Can the robot move (by translation and rotation) from the source to the target position,
without ever intersecting the “walls” of the environment?
To show that Motion Planning is 3-Sum-hard, employ the reduction for Segment
Splitting from above. The three “punched” lines form the doorway between two rooms,
each modeled by a constant number of segments that cannot be split, similar to the
boundary gadgets above. The source position is in one room, the target position in the
other, and to get from source to target the robot has to pass through a sequence of three
collinear holes in the door (suppose the doorway is suﬃciently small compared to the
length of the robot).

Exercise 13.21 The 3-Sum’ problem is deﬁned as follows: given three sets S1, S2, S3
of n integers each, are there a1 ∈ S1, a2 ∈ S2, a3 ∈ S3 such that a1 + a2 + a3 = 0?
Prove that the 3-Sum’ problem and the 3-Sum problem as deﬁned in the lecture
(S1 = S2 = S3) are equivalent, more precisely, that they are reducible to each other
in subquadratic time.

Questions

56. How can one construct an arrangement of lines in R
2? Describe the incremen-
tal algorithm and prove that its time complexity is quadratic in the number of lines
(incl. statement and proof of the Zone Theorem).

57. How can one test whether there are three collinear points in a set of n given
points in R
2? Describe an O(n
2) time algorithm.

58. How can one compute the minimum area triangle spanned by three out of n
given points in R
2? Describe an O(n
2) time algorithm.

59. What is a ham-sandwich cut? Does it always exist? How to compute it?
State and prove the theorem about the existence of a ham-sandwich cut in R
2 and
describe an O(n
2) algorithm to compute it.

60. What is the endpoint visibility graph for a set of disjoint line segments in the
plane and how can it be constructed? Give the deﬁnition and explain the relation
to shortest paths. Describe the O(n
2) algorithm by Welzl, including full proofs of
Theorem 13.11 and Theorem 13.15.

61. Is there a subquadratic algorithm for General Position? Explain the term
3-Sum hard and its implications and give the reduction from 3-Sum to General
Position.

62. Which problems are known to be 3-Sum-hard? List at least three problems
(other than 3-Sum) and brieﬂy sketch the corresponding reductions.

158

CG 2012 13.9. 3-Sum hardness

References

[1] David Eppstein, Happy endings for ﬂip graphs. J. Comput. Geom., 1, 1, (2010),
3–28, URL http://jocg.org/index.php/jocg/article/view/21.

[2] Jeﬀ Erickson, Lower bounds for linear satisﬁability prob-
lems. Chicago J. Theoret. Comput. Sci., 1999, 8, URL
http://cjtcs.cs.uchicago.edu/articles/1999/8/contents.html.

[3] Anka Gajentaan and Mark H. Overmars, On a class of O(n
2) problems in com-
putational geometry. Comput. Geom. Theory Appl., 5, (1995), 165–185, URL
http://dx.doi.org/10.1016/0925-7721(95)00022-2.

[4] Branko Grünbaum, Hamiltonian polygons and polyhedra. Geombinatorics, 3, 3,
(1994), 83–89.

[5] Heiko Harborth, Konvexe Fünfecke in ebenen Punktmengen. Elem. Math., 33,
(1979), 116–118, URL http://dx.doi.org/10.5169/seals-32945.

[6] Michael Hoﬀmann, On the existence of paths and cycles. Ph.D. thesis, ETH
Zürich, 2005, URL http://dx.doi.org/10.3929/ethz-a-004945082.

[7] Michael Hoﬀmann and Csaba D. Tóth, Segment endpoint visibility graphs
are Hamiltonian. Comput. Geom. Theory Appl., 26, 1, (2003), 47–68, URL
http://dx.doi.org/10.1016/S0925-7721(02)00172-4.

[8] Chi-Yuan Lo, Jiří Matoušek, and William L. Steiger, Algorithms for
ham-sandwich cuts. Discrete Comput. Geom., 11, (1994), 433–452, URL
http://dx.doi.org/10.1007/BF02574017.

[9] Masatsugu Urabe and Mamoru Watanabe, On a counterexample to a conjec-
ture of Mirzaian. Comput. Geom. Theory Appl., 2, 1, (1992), 51–53, URL
http://dx.doi.org/10.1016/0925-7721(92)90020-S.

[10] Emo Welzl, Constructing the visibility graph for n line segments
in O(n
2) time. Inform. Process. Lett., 20, (1985), 167–171, URL
http://dx.doi.org/10.1016/0020-0190(85)90044-4.

159

Chapter 14

Davenport-Schinzel Sequences

The complexity of a simple arrangement of n lines in R
2 is Θ(n
2) and so every algorithm
that uses such an arrangement explicitly needs Ω(n
2) time. However, there are many
scenarios in which we do not need the whole arrangement but only some part of it. For
instance, to construct a ham-sandwich cut for two sets of points in R
2 one needs the
median levels of the two corresponding line arrangements only. As mentioned in the
previous section, the relevant information about these levels can actually be obtained in
linear time. Similarly, in a motion planning problem where the lines are considered as
obstacles we are only interested in the cell of the arrangement we are located in. There
is no way to ever reach any other cell, anyway.
This chapter is concerned with analyzing the complexity—that is, the number of
vertices and edges—of a single cell in an arrangement of n curves in R
2. In case of a
line arrangement this is mildly interesting only: Every cell is convex and any line can
appear at most once along the cell boundary. On the other hand, it is easy to construct
an example in which there is a cell C such that every line appears on the boundary ∂C.
But when we consider arrangement of line segments rather than lines, the situation
changes in a surprising way. Certainly a single segment can appear several times along
the boundary of a cell, see the example in Figure 14.1. Make a guess: What is the
maximal complexity of a cell in an arrangement of n line segments in R
2?

Figure 14.1: A single cell in an arrangement of line segments.

161

Chapter 14. Davenport-Schinzel Sequences CG 2012

You will ﬁnd out the correct answer soon, although we will not prove it here. But
my guess would be that it is rather unlikely that your guess is correct, unless, of course,
you knew the answer already. :-)
For a start we will focus on one particular cell of any arrangement that is very easy to
describe: the lower envelope or, intuitively, everything that can be seen vertically from
below. To analyze the complexity of lower envelopes we use a combinatorial descrip-
tion using strings with forbidden subsequences, so-called Davenport-Schinzel sequences.
These sequences are of independent interest, as they appear in a number of combinatorial
problems [2] and in the analysis of data structures [7]. The techniques used apply not
only to lower envelopes but also to arbitrary cells of arrangements.

14.1 Davenport-Schinzel Sequences

Deﬁnition 14.1 A (n, s)-Davenport-Schinzel sequence is a sequence over an alphabet A of
size n in which no two consecutive characters are the same and there is no alternating subsequence of the form . . . a . . . b . . . a . . . b . . . of s + 2
characters, for any a, b ∈ A.

Let λs(n) be the length of a longest (n, s)-Davenport-Schinzel sequence.

For example, abcbacb is a (3, 4)-DS sequence but not a (3, 3)-DS sequence because it
contains the subsequence bcbcb.
Let F = {f1, . . . , fn} be a collection of real-valued continuous functions deﬁned on
a common interval I ⊂ R. The lower envelope LF of F is deﬁned as the pointwise
minimum of the functions fi, 1 ⩽ i ⩽ n, over I. Suppose that any pair fi, fj, 1 ⩽ i <
j ⩽ n, intersects in at most s points. Then I can be decomposed into a ﬁnite sequence
I1, . . . , Iℓ of (maximal connected) pieces on each of which a single function from F deﬁnes
LF. Deﬁne the sequence φ(F) = (φ1, . . . , φℓ), where fφi is the function from F which
deﬁnes LF on Ii.

Observation 14.2 φ(F) is an (n, s)-Davenport-Schinzel sequence.

In the case of line segments the above statement does not hold because a set of line
segments is in general not deﬁned on a common real interval.

Proposition 14.3 Let F be a collection of n real-valued continuous functions each of
which is deﬁned on some real interval. If any two functions from F intersect in at
most s points then φ(F) is an (n, s + 2)-Davenport-Schinzel sequence.

Proof. Let I denote the union of all intervals on which one of the functions from F is
deﬁned. Consider any function f ∈ F deﬁned on [a, b] ⊆ I = [c, d]. Extend f on I by
extending it using almost vertical rays pointing upward, from a use a ray of suﬃciently

162

CG 2012 14.1. Davenport-Schinzel Sequences

small slope, from b use a ray of suﬃciently large slope. For all functions use the same
slope on these two extensions such that no extensions in the same direction intersect.
By suﬃciently small/large we mean that for any extension ray there is no function
endpoint nor an intersection point of two functions in the open angular wedge bounded
by the extension ray and the vertical ray starting from the same source. (There may be
such points on the vertical ray, but not in the open wedge between the two rays.)
Denote the resulting collection of functions totally deﬁned on I by F ′. If the rays are
suﬃciently close to vertical then φ(F ′) = φ(F).

For any f ∈ F ′ a single extension ray can create at most one additional intersection
with any g ∈ F ′. (Let [af, bf] and [ag, bg] be the intervals on which the function f and
g, respectively, was deﬁned originally. Consider the ray r extending f from af to the left.
If af ∈ [ag, bg] then r may create a new intersection with g, if af > bg then r creates a
new intersection with the right extension of g from bg, and if af < ag then r does not
create any new intersection with g.)
On the other hand, for any pair s, t of segments, neither the left extension of the
leftmost segment endpoint nor the right extension of the rightmost segment endpoint
can introduce an additional intersection. Therefore, any pair of segments in F ′ intersects
at most s + 2 times and the claim follows. 
Next we will give an upper bound on the length of Davenport-Schinzel sequences for
small s.

Lemma 14.4 λ1(n) = n, λ2(n) = 2n − 1, and λ3(n) ⩽ 2n(1 + log n).

Proof. λ1(n) = n is obvious. λ2(n) = 2n − 1 is given as an exercise. We prove
λ3(n) ⩽ 2n(1 + log n) = O(n log n).
For n = 1 it is λ3(1) = 1 ⩽ 2. For n > 1 consider any (n, 3)-DS sequence σ of length
λ3(n). Let a be a character that appears least frequently in σ. Clearly a appears at
most λ3(n)/n times in σ. Delete all appearances of a from σ to obtain a sequence σ ′ on
n − 1 symbols. But σ ′ is not necessarily a DS sequence because there may be consecutive
appearances of a character b in σ ′, in case that σ = . . . bab . . ..
Claim: There are at most two pairs of consecutive appearances of the same char-
acter in σ ′. Indeed, such a pair can be created around the ﬁrst and last appearance

163

Chapter 14. Davenport-Schinzel Sequences CG 2012

of a in σ only. If any intermediate appearance of a creates a pair bb in σ ′ then
σ = . . . a . . . bab . . . a . . ., in contradiction to σ being an (n, 3)-DS sequence.
Therefore, one can remove at most two characters from σ ′ to obtain a (n − 1, 3)-DS
sequence ˜σ. As the length of ˜σ is bounded by λ3(n − 1), we obtain λ3(n) ⩽ λ3(n − 1) +
λ3(n)/n + 2. Reformulating yields

λ3(n)
n︸ ︷︷ ︸
=: f(n)
 ⩽ λ3(n − 1)
n − 1︸ ︷︷ ︸
=f(n−1)
 + 2
n − 1 ⩽ 1︸︷︷︸
=f(1) +2
 n−1∑

i=1
 1
i = 1 + 2Hn−1

and together with 2Hn−1 < 1 + 2 log n we obtain λ3(n) ⩽ 2n(1 + log n). 
Bounds for higher-order Davenport-Schinzel sequences. As we have seen, λ1(n) (no aba)
and λ2(n) (no abab) are both linear in n. It turns out that for s ⩾ 3, λs(n) is slightly
superlinear in n (taking s ﬁxed). The bounds are known almost exactly, and they involve
the inverse Ackermann function α(n), a function that grows extremely slowly.
To deﬁne the inverse Ackermann function, we ﬁrst deﬁne a hierarchy of functions
α1(n), α2(n), α3(n), . . . where, for every ﬁxed k, αk(n) grows much more slowly than
αk−1(n):
We ﬁrst let α1(n) = ⌈n/2⌉. Then, for each k ⩾ 2, we deﬁne αk(n) to be the number
of times we must apply αk−1, starting from n, until we get a result not larger than 1. In
other words, αk(n) is deﬁned recursively by:

αk(n) =
 {
0, if n ⩽ 1;
1 + αk(αk−1(n)), otherwise.

Thus, α2(n) = ⌈log2 n⌉, and α3(n) = log∗ n.
Now ﬁx n, and consider the sequence α1(n), α2(n), α3(n), . . .. For every ﬁxed n, this
sequence decreases rapidly until it settles at 3. We deﬁne α(n) (the inverse Ackermann
function) as the function that, given n, returns the smallest k such that αk(n) is at most
3:
 α(n) = min {k | αk(n) ⩽ 3}.

We leave as an exercise to show that for every ﬁxed k we have αk(n) = o(αk−1(n))
and α(n) = o(αk(n)).
Coming back to the bounds for Davenport-Schinzel sequences, for λ3(n) (no ababa)
it is known that λ3(n) = Θ(nα(n)) [4]. In fact it is known that λ3(n) = 2nα(n) ±
O(n
√α(n)) [5, 6]. For λ4(n) (no ababab) we have λ4(n) = Θ(n · 2α(n)) [3].
For higher-order sequences the known upper and lower bounds are almost tight, and
they are of the form λs(n) = n · 2poly(α(n)), where the degree of the polynomial in the
exponent is roughly s/2 [3, 6].
 164

CG 2012 14.1. Davenport-Schinzel Sequences

Realizing DS sequences as lower envelopes. There exists a construction of a set of n seg-
ments in the plane whose lower-envelope sequence has length Ω(nα(n)). (In fact, the
lower-envelope sequence has length nα(n) − O(n), with a leading coeﬃcient of 1; it is
an open problem to get a leading coeﬃcient of 2, or prove that this is not possible.)
It is an open problem to construct a set of n parabolic arcs in the plane whose
lower-envelope sequence has length Ω(n · 2α(n)).

Generalizations of DS sequences. Also generalizations of Davenport-Schinzel sequences
have been studied, for instance, where arbitrary subsequences (not necessarily an al-
ternating pattern) are forbidden. For a word σ and n ∈ N deﬁne Ex(σ, n) to be the
maximum length of a word over A = {1, . . . , n}∗ that does not contain a subsequence of
the form σ. For example, Ex(ababa, n) = λ3(n). If σ consists of two letters only, say a
and b, then Ex(σ, n) is super-linear if and only if σ contains ababa as a subsequence [1].
This highlights that the alternating forbidden pattern is of particular interest.

Exercise 14.5 Prove that λ2(n) = 2n − 1.

Exercise 14.6 Prove that λs(n) is ﬁnite for all s and n.

Exercise 14.7 Show that every (n, s)-Davenport-Schinzel sequence can be realized as
the lower envelope of n continuous functions from R to R, every pair of which
intersect at most s times.

Exercise 14.8 Show that every Davenport-Schinzel sequence of order two can be real-
ized as a lower envelope of n parabolas.

It is a direct consequence of the symmetry in the deﬁnition that the property of being
a Davenport-Schinzel sequence is invariant under permutations of the alphabet. For
instance, σ = bcacba is a (3, 3)-DS sequence over A = {a, b, c}. Hence the permutation
π = (ab) induces a (3, 3)-DS sequence π(σ) = acbcab and similarly π ′ = (cba) induces
another (3, 3)-DS sequence π ′(σ) = abcbac.
When counting the number of Davenport-Schinzel sequences of a certain type we
want to count essentially distinct sequences only. Therefore we call two sequences over
a common alphabet A equivalent if and only if one can be obtained from the other
by a permutation of A. Then two sequences are distinct if and only if they are not
equivalent. A typical way to select a representative from each equivalence class is to
order the alphabet and demand that the ﬁrst appearance of a symbol in the sequence
follows that order. For example, ordering A = {a, b, c} alphabetically demands that the
ﬁrst occurrence of a precedes the ﬁrst occurrence of b, which in turn precedes the ﬁrst
occurrence of c.

Exercise 14.9 Let P be a convex polygon with n + 1 vertices. Find a bijection between
the triangulations of P and the set of pairwise distinct (n, 2)-Davenport-Schinzel
sequences of maximum length (2n − 1). It follows that the number of distinct

165

Chapter 14. Davenport-Schinzel Sequences CG 2012

maximum (n, 2)-Davenport-Schinzel sequences is exactly Cn−1 = 1
n (2n−2
n−1 ), which is
the (n − 1)-st Catalan number.

Questions

63. What is an (n, s) Davenport-Schinzel sequence and how does it relate to the
lower envelope of real-valued continuous functions? Give the precise deﬁnition
and some examples. Explain the relationship to lower envelopes and how to apply
the machinery to partial functions like line segments.

64. What is the value of λ1(n) and λ2(n)?

65. What is the asymptotic value of λ3(n), λ4(n), and λs(n) for larger s?

66. What is the combinatorial complexity of the lower envelope of a set of n
lines/parabolas/line segments?

References

[1] Radek Adamec, Martin Klazar, and Pavel Valtr, Generalized Davenport-Schinzel
sequences with linear upper bound. Discrete Math., 108, (1992), 219–229, URL
http://dx.doi.org/10.1016/0012-365X(92)90677-8.

[2] Pankaj K. Agarwal and Micha Sharir, Davenport-Schinzel sequences and their
geometric applications. Cambridge University Press, New York, NY, 1995.

[3] Pankaj K. Agarwal, Micha Sharir, and Peter W. Shor, Sharp upper and lower bounds
on the length of general Davenport-Schinzel sequences. J. Combin. Theory Ser. A,
52, 2, (1989), 228–274, URL http://dx.doi.org/10.1016/0097-3165(89)90032-0.

[4] Sergiu Hart and Micha Sharir, Nonlinearity of Davenport-Schinzel sequences and
of generalized path compression schemes. Combinatorica, 6, (1986), 151–177, URL
http://dx.doi.org/10.1007/BF02579170.

[5] Martin Klazar, On the maximum lengths of Davenport-Schinzel sequences. In R. Gra-
ham et al., ed., Contemporary Trends in Discrete Mathematics, vol. 49 of DI-
MACS Series in Discrete Mathematics and Theoretical Computer Science, pp.
169–178, Amer. Math. Soc., Providence, RI, 1999.

[6] Gabriel Nivasch, Improved bounds and new techniques for Davenport-Schinzel se-
quences and their generalizations. In Proc. 20th ACM-SIAM Sympos. Discrete
Algorithms, pp. 1–10, 2009, URL http://doi.acm.org/10.1145/1496770.1496771.

[7] Seth Pettie, Splay trees, Davenport-Schinzel sequences, and the deque conjecture. In
Proc. 19th ACM-SIAM Sympos. Discrete Algorithms, pp. 1115–1124, 2008, URL
http://doi.acm.org/10.1145/1347082.1347204.

166

Chapter 15

Epsilon Nets

15.1 Motivation

Here is our scenario for this chapter. We are given a set A of points in R
d and a family
R of ranges r ⊆ R
d, for example the set of all balls, halfspaces, or convex sets in R
d.
A is huge and probably not even known completely; similarly, R may not be accessible
explicitly (in the examples above, it is an uncountable set). Still, we want to learn
something about A and R.
The situation is familiar, deﬁnitely, if we don’t insist on the geometric setting. For
example, let A be the set of consumers living in Switzerland, and let ˜r be the subset
of consumers who frequently eat a certain food product, say Lindt chocolate. We have
similar subsets for other food products, and together, they form the family of ranges R.
If we want to learn something about ˜r, e.g. the ratio |˜r|
|A| (the fraction of consumers
frequently eating Lindt chocolate), then we typically sample a subset S of A and see
what portion of S lies in ˜r. We want to believe that

|˜r ∩ S|
|S| approximates |˜r|
|A| ,

and statistics tells us to what extent this is justiﬁed. In fact, consumer surveys are based
on this approach: in our example, S is a sample of consumers who are being asked about
their chocolate preferences. After this, the quantity |˜r ∩ S|/|S| is known and used to
predict the “popularity” |˜r|/|A| of Lindt chocolate among Swiss consumers.
In this chapter, we consider a diﬀerent kind of approximation. Suppose that we
are interested in the most popular food products in Switzerland, the ones which are
frequently eaten by more than an ε-fraction of all consumers, for some ﬁxed 0 ⩽ ε ⩽ 1.
The goal is to ﬁnd a small subset N of consumers that “represent” all popular products.
Formally, we want to ﬁnd a set N ⊆ A such that

for all r: |r|
|A| > ε ⇒ r ∩ N ̸= ∅.

167

Chapter 15. Epsilon Nets CG 2012

Such a subset is called an epsilon net. Obviously, N = A is an epsilon net for all ε, but
as already mentioned above, the point here is to have a small set N.
Epsilon nets are very useful in many contexts that we won’t discuss here. But al-
ready in the food consumption example above, it is clear that a small representative
set of consumers is a good thing to have; for example if you quickly need a statement
about a particular popular food product, you know that you will ﬁnd somebody in your
representative set who knows the product.
The material of this chapter is classic and goes back to Haussler and Welzl [1].

15.2 Range spaces and ε-nets.

Here is the formal framework. Let X be a (possibly inﬁnite) set and R ⊆ 2X. The pair
(X, R) is called a range space 1, with X its points and the elements of R its ranges.

Deﬁnition 15.1 Let (X, R) be a range space. Given A ⊆ X, ﬁnite, and ε ∈ R, 0 ⩽ ε ⩽ 1,
a subset N of A is called an ε-net of A (w.r.t. R) if

for all r ∈ R: |r ∩ A| > ε|A| ⇒ r ∩ N ̸= ∅ .

This deﬁnition is easy to write down, but it is not so easy to grasp, and this is why we
will go through a couple of examples below. Note that we have a slightly more general
setup here, compared to the motivating Section 15.1 where we had X = A.

15.2.1 Examples

Typical examples of range spaces in our geometric context are (R, H1) with H1 := {(−∞, a] | a ∈ R} ∪ {[a, ∞) | a ∈ R} (half-inﬁnite intervals),
and (R, I) with I := {[a, b]∥ a, b ∈ R, a ⩽ b} (intervals),

and higher-dimensional counter-parts (R
d, Hd) with Hd the closed halfspaces in R
d bounded by hyperplanes, (R
d, Bd) with Bd the closed balls in R
d, (R
d, Sd) with Sd the d-dimensional simplices in R
d, and (R
d, Cd) with Cd the convex sets in R
d.

1In order to avoid confusion: A range space is nothing else but a set system, sometimes also called
hypergraph. It is the context, where we think of X as points and R as ranges in some geometric ambient
space, that suggests the name at hand.
 168

CG 2012 15.2. Range spaces and ε-nets.

ε-Nets w.r.t. (R, H1) are particularly simple to obtain. For A ⊆ R, N := {min A, max A}
is an ε-net for every ε—it is even a 0-net. That is, there are ε-nets of size 2, independent
from |A| and ε.
The situation gets slightly more interesting for the range space (R, I) with intervals.
Given ε and A with elements
 a1 < a2 < · · · < an ,

we observe that an ε-net must contain at least one element from any contiguous sequence
{ai, ai+1, . . . , ai+k−1} of k > εn (i.e. k ⩾ ⌊εn⌋ + 1) elements in A. In fact, this is a
necessary and suﬃcient condition for ε-nets w.r.t. intervals. Hence,

{a⌊εn⌋+1, a2⌊εn⌋+2, . . .}

is an ε-net of size
2 ⌊ n
⌊εn⌋+1⌋ ⩽ ⌈ 1
ε⌉ − 1. So while the size of the net depends now on ε,
it is still independent of |A|.

15.2.2 No point in a large range.

Let us start with a simple exercise, showing that large ranges are easy to “catch”. Assume
that |r ∩ A| > ε|A| for some ﬁxed r and ε, 0 ⩽ ε ⩽ 1.
Now consider the set S obtained by drawing s elements uniformly at random from A
(with replacement). We write
 S ∼ As,

indicating that S is chosen uniformly at random from the set As of s-element sequences
over A.
What is the probability that S ∼ As fails to intersect with r, i.e. S ∩ r = ∅? For
p := |r∩A|
|A| (note p > ε) we get3

prob(S ∩ r = ∅) = (1 − p)s < (1 − ε)s ⩽ e−εs .

That is, if s = 1
ε then this probability is at most e−1 ≈ 0.368, and if we choose s = λ 1
ε,
then this probability decreases exponentially with λ: It is at most e−λ.
For example, if |A| = 10000 and |r ∩ A| > 100 (r contains more than 1% of the points
in A), then a sample of 300 points is disjoint from r with probability at most e−3 ≈ 0.05.

2The number L of elements in the set is the largest ℓ such that ℓ(⌊εn⌋ + 1) ⩽ n, hence L = ⌊ n
⌊εn⌋+1 ⌋.

Since ⌊εn⌋ + 1 > εn, we have n
⌊εn⌋+1 < 1
ε , and so L < 1
ε , i.e. L ⩽ ⌈ 1
ε ⌉ − 1.
3We make use of the inequality 1 + x ⩽ e
x for all x ∈ R.

169

Chapter 15. Epsilon Nets CG 2012

15.2.3 Smallest enclosing balls.

Here is a potential use of this for a geometric problem. Suppose A is a set of n points
in R
d, and we want to compute the smallest enclosing ball of A. In fact, we are willing
to accept some mistake, in that, for some given ε, we want a small ball that contains all
but at most εn points from A. So let’s choose a sample S of λ 1
ε points drawn uniformly
(with replacement) from A and compute the smallest enclosing ball B of S. Now let
r := R
d \ B, the complement of B in R
d, play the role of the range in the analysis above.
Obviously r ∩ S = ∅, so it is unlikely that |r ∩ A| > ε|A|, since—if so—the probability of
S ∩ r = ∅ was at most e−λ.

It is important to understand that this was complete nonsense!

For the probabilistic analysis above we have to ﬁrst choose r and then draw the
sample—and not, as done in the smallest ball example, ﬁrst draw the sample and then
choose r based on the sample. That cannot possibly work, since we could always choose
r simply as the complement R
d \ S—then clearly r ∩ S = ∅ and |r ∩ A| > ε|A|, unless
|S| ⩾ (1 − ε)|A|.
While you hopefully agree on this, you might ﬁnd the counterargument with r = R
d\S
somewhat artiﬁcial, e.g. complements of balls cannot be that selective in ‘extracting’
points from A. It is exactly the purpose of this chapter to understand to what extent
this advocated intuition is justiﬁed or not.

15.3 Either almost all is needed or a constant suﬃces.

Let us reveal the spectrum of possibilities right away, although its proof will have to
await some preparatory steps.

Theorem 15.2 Let (X, R) be an inﬁnite range space. Then one of the following two
statements holds.

(1) For every n ∈ N there is a set An ⊆ X with |An| = n such that for every ε,
0 ⩽ ε ⩽ 1, an ε-net must have size at least (1 − ε)n.

(2) There is a constant δ depending on (X, R), such that for every ﬁnite A ⊆ X
and every ε, 0 < ε ⩽ 1, there is an ε-net of A w.r.t. R of size at most 8δ
ε log2 4δ
ε
(independent of the size of A).

That is, either we have always ε-nets of size independent of |A|, or we have to do the
trivial thing, namely choosing all but εn points for an ε-net. Obviously, the range spaces
(R, H1) and (R, I) fall into category (2) of the theorem.
For an example for (1), consider (R
2, C2). For any n ∈ N, let An be a set of n points
in convex position. For every N ⊆ An there is a range r ∈ C2, namely the convex hull
of An \ N, such that An ∩ r = An \ N (hence, r ∩ N = ∅); see Figure 15.1. Therefore,

170

CG 2012 15.4. What makes the diﬀerence: VC-dimension

N ⊆ An cannot be an ε-net of An w.r.t. C2 if |An \ N| = n − |N| > εn. Consequently, an
ε-net must contain at least n − εn = (1 − ε)n points.4

r N

Figure 15.1: If R consists of all convex sets in the plane, then only trivial epsilon nets
exist: for every subset N (black points) of a set An in convex position,
the range r = conv(An \ N) fails to intersect N.

So what distinguishes (R
2, C2) from (R, H1) and (R, I)? And which of the two cases
applies to the many other range spaces we have listed above? Will all of this eventually
tell us something about our attempt of computing a small ball covering all but at most
εn out of n given points? This and more should be clear by the end of this chapter.

15.4 What makes the diﬀerence: VC-dimension

Given a range space (X, R) and A ⊆ X, we let

R∣
∣
A := {r ∩ A | r ∈ R} ,

the projection of R to A. Even if R is inﬁnite, R∣
∣
A is always of size at most 2n if A
is an n-element set. The signiﬁcance of projections in our context becomes clear if we
rewrite Deﬁnition 15.1 in terms of projections: N ⊆ A is an ε-net if

for all r ∈ R∣
∣
A : |r| > ε|A| ⇒ r ∩ N ̸= ∅.

All of a sudden, the conditions for an ε-net have become discrete, and they only depend
on the ﬁnite range space (A, R∣
∣
A ).

4If we were satisﬁed with any abstract example for category (1), we could have taken (X, 2X) for any
inﬁnite set X.
 171

Chapter 15. Epsilon Nets CG 2012

Note that, for A a set of n points in convex position in the plane, C2∣
∣A = 2A; we
get every subset of A by an intersection with a convex set (this is also the message of
Figure 15.1). That is |C2∣
∣
A | = 2n, the highest possible value.
For A a set of n points in R, we can easily see that5 |I∣
∣
A | = (
n+1
2 ) + 1 = O(n
2). A
similar argument shows that |H1∣
∣
A | = 2n. Now comes the crucial deﬁnition.

Deﬁnition 15.3 Given a range space (X, R), a subset A of X is shattered by R if R∣
∣
A =
2A. The VC-dimension6 of (X, R), VCdim(X, R), is the cardinality (possibly inﬁnite)
of the largest subset of X that is shattered by R. If no set is shattered (i.e. not even
the empty set which means that R is empty), we set the VC-dimension to −1.

We had just convinced ourselves that (R
2, C2) has arbitrarily large sets that can be
shattered. Therefore, VCdim(R
2, C2) = ∞.
Consider now (R, I). Two points A = {a, b} can be shattered, since for each of the
4 subsets, ∅, {a}, {b}, and {a, b}, of A, there is an interval that generates that subset by
intersection with A. However, for A = {a, b, c} with a < b < c there is no interval that
contains a and c but not b. Hence, VCdim(R, I) = 2.

Exercise 15.4 What is VCdim(R, H1)?

Exercise 15.5 Prove that if VCdim(X, R) = ∞, then we are in case (1) of Theo-
rem 15.2, meaning that only trivial epsilon nets always exist.

15.4.1 The size of projections for ﬁnite VC-dimension.

Here is the (for our purposes) most important consequence of ﬁnite VC dimension: there
are only polynomially many ranges in every projection.

Lemma 15.6 (Sauer’s Lemma) If (X, R) is a range space of ﬁnite VC-dimension at most
δ, then
 |R∣
∣
A | ⩽ Φδ(n) :=
 δ∑

i=0
 (
n
i
 )

for all A ⊆ X with |A| = n.

5Given A as a1 < a2 · · · < an we can choose another n + 1 points bi, 0 ⩽ i ⩽ n, such that

b0 < a1 < b1 < a2 < b2 < · · · bn−1 < an < bn .

Each nonempty intersection of A with an interval can be uniquely written as A ∩ [bi, bj] for 0 ⩽ i < j ⩽ n.
This gives (
n+1
2 ) plus one for the empty set.
6‘VC’ in honor of the Russian statisticians V. N. Vapnik and A. Ya. Chervonenkis, who discovered the
crucial role of this parameter in the late sixties.
 172

CG 2012 15.4. What makes the diﬀerence: VC-dimension

Proof. First let us observe that Φ : N0 ∪ {−1} × N0 → N0 is deﬁned by the recurrence7

Φδ(n) =
 



 0 δ = −1,
1 n = 0 and δ ⩾ 0, and
Φδ(n − 1) + Φδ−1(n − 1) otherwise.

Second, we note that the VC-dimension cannot increase by passing from (X, R) to a
projection (A, R), R := R∣
∣A . Hence, it suﬃces to consider the ﬁnite range space (A, R)—
which is of VC-dimension at most δ—and show |R| ⩽ Φδ(n) (since Φ is monotone in
δ). Now we proceed to a proof by induction of this inequality. If A = ∅ or R = ∅ the
statement is trivial. Otherwise, we consider the two ‘derived’ range spaces for some ﬁxed
x ∈ A: (A \ {x}, R − x), with R − x := {r \ {x} | r ∈ R}

(note R − x = R∣
∣
∣A \ {x} ) and

(A \ {x}, R(x)), with R(x) := {r ∈ R | x ̸∈ r, r ∪ {x} ∈ R}.

Observe that the ranges in R(x) are exactly those ranges in R − x that have two preimages
under the map R ∋ r ↦→ r \ {x} ∈ R − x ,

all other ranges have a unique preimage. Consequently,

|R| = |R − x| + |R(x)| .

We have |R−x| ⩽ Φδ(n−1). If A ′ ⊆ A\{x} is shattered by R(x), then A ′ ∪{x} is shattered
by R. Hence, (A \ {x}, R(x)) has VC-dimension at most δ − 1 and |R(x)| ⩽ Φδ−1(n − 1).
Summing up, it follows that

|R| ⩽ Φδ(n − 1) + Φδ−1(n − 1) = Φδ(n)

which yields the assertion of the lemma. 
In order to see that the bound given in the lemma is tight, consider the range space

(X,
 δ⋃

i=0
 (X
i
 )
) .

Obviously, a set of more than δ elements cannot be shattered (hence, the VC-dimension is
at most δ), and for any ﬁnite A ⊆ X, the projection of the ranges to A is ⋃δ
i=0 (
A
δ)—with
cardinality Φδ(|A|).

7We recall that the binomial coeﬃcients (
n
k) (with k, n ∈ N0) satisfy the recurrence (
n
k) = 0 if n < k,
(
n
0) = 1, and (
n
k) = (
n−1
k ) + (
n−1
k−1)
.
 173

Chapter 15. Epsilon Nets CG 2012

We note that a rough, but for our purposes good enough estimate for Φ is given by8

Φδ(n) ⩽ n
δ for δ ⩾ 2.

We have seen now that the maximum possible size of projections either grows expo-
nentially (2n in case of inﬁnite VC-dimension) or it is bounded by a polynomial n
δ in
case of ﬁnite VC-dimension δ). The latter is the key to the existence of small ε-nets.
Before shedding light on this, let us better understand when the VC-dimension is ﬁnite.

15.5 VC-dimension of Geometric Range Spaces

15.5.1 Halfspaces.

Let us investigate the VC-dimension of (R
2, H2). It is easily seen that three points in the
plane can be shattered by halfplanes, as long a they do not lie on a common line. Hence,
the VC-dimension is at least 3. Now consider 4 points. If three of them lie on a common
line, there is no way to separate the middle point on this line from the other two by a
halfplane. So let us assume that no three points lie on a line. Either three of them are
vertices of a triangle that contains the fourth point—then we cannot possibly separate
the fourth point from the remaining three points by a halfplane. Or the four points are
vertices of a convex quadrilateral—then there is no way of separating the endpoints from
a diagonal from the other two points. Consequently, four points cannot be shattered,
and VCdim(R
2, H2) = 3 is established.
The above argument gets tedious in higher dimensions, if it works in a rigorous way
at all. Fortunately, we can employ a classic.9

Lemma 15.7 (Radon’s Theorem) Let d ∈ N. Every set A of n ⩾ d + 2 points in R
d can
be partitioned as A = A1 .
∪ A2 such that conv(A1) ∩ conv(A2) ̸= ∅.

Proof. For n ⩾ d + 2, n points {p1, p2, . . . , pn} in R
d are aﬃnely dependent, which—by
deﬁnition—means that there are real coeﬃcients λi, i ∈ {1, 2, . . . , n}, not all 0, with

n∑

i=1 λi = 0 and
 n∑

i=1 λipi = 0 .

Now let I1 := {i | λi > 0} and I2 := {i | λi ⩽ 0}, which both have to be non-empty. We have∑

i∈I1 λi = − ∑

i∈I2 λi, and we let λ denote this value (which has to be positive). Now

p := 1
λ
 ∑

i∈I1 λipi = − 1
λ
 ∑

i∈I2 λipi

8A better estimate, at least for δ ⩾ 3, is given by Φδ(n) < ( e n
δ )d for all n, d ∈ N, d ⩽ n.
9Radon’s Theorem forms a classical triumvirate with Carathéodory’s Theorem 3.8 and Helly’s Theo-
rem 12.6.
 174

CG 2012 15.5. VC-dimension of Geometric Range Spaces

denotes a point that lies in the convex hulls of A1 := {pi | i ∈ I1} and A2 := {pi | i ∈ I2},
respectively. Therefore, A1 and A2 provide a partition as required in the lemma. 
We get, as an easy implication, that a set A of at least d + 2 points in R
d cannot be
shattered by halfspaces. Indeed, let A1 .
∪ A2 be a partition as guaranteed by Randon’s
Lemma. Now every halfspace containing A1 must contain at least one point of A2, hence
h ∩ A = A1 is impossible for a halfspace h and thus A is not shattered by Hd. Moreover,
it is easily seen that the vertex set of a d-dimensional simplex (there are d + 1 vertices)
can be shattered by halfspaces (each subset of the vertices forms a face of the simplex
and can thus be separated from the rest by a hyperplane). We summarize that

VCdim(R
d, Hd) = d + 1 .

Let us now consider the range space (R
d, ˇHd), where ˇHd denotes the set of all closed
halfspaces below non-vertical hyperplanes10–we call these lower halfspaces. Since ˇHd ⊆
Hd, the VC-dimension of (R
d, ˇHd) is at most d + 1, but, in fact, it not too diﬃcult to
show
 VCdim(R
d, ˇHd) = d . (15.8)

(Check this claim at least for d = 2.) This range space is a geometric example where the
bound of Sauer’s Lemma is attained. Indeed, for any set A of n points in R
d in general
position11, it can be shown that
 | ˇHd∣
∣
A | = Φd(n) .

15.5.2 Balls.

It is easy to convince oneself that the VC-dimension of disks in the plane is 3: Three
points not on a line can be shattered and four points cannot. Obviously not, if one of the
points is in the convex hull of the other, and for four vertices of a convex quadrilateral,
it is not possible for both diagonals to be separated from the endpoints of the respective
other diagonal by a circle (if you try to draw a picture of this, you see that you get two
circles that intersect four times, which we know is not be the case).
A more rigorous argument which works in all dimensions is looming with the help of
(15.8), if we employ the following transformation called lifting map that we have already
encountered for d = 2 in Section 6.3:

R
d −→ R
d+1

(x1, x2, . . . , xd) = p ↦→ ℓ(p) = (x1, x2, . . . , xd, x12 + x22 + · · · + xd2)

10A hyperplane is called non-vertical if it can be speciﬁed by a linear equation ∑d
i=1 λixi = λd+1 with
λd ̸= 0; see also Section 1.2
11No i + 2 on a common i-ﬂat for i ∈ {1, 2, . . . , d − 1}; in particular, no d + 1 points on a common
hyperplane.
 175

Chapter 15. Epsilon Nets CG 2012

(For a geometric interpretation, this is a vertical projection of R
d to the unit paraboloid
xd+1 = x12 + x22 + · · · + xd2 in R
d+1.) The remarkable property of this transformation
is that it maps balls in R
d to halfspaces in R
d+1 in the following sense.
Consider a ball Bd(c, ρ) (c = (c1, c2, . . . , cd) ∈ R
d the center, and ρ ∈ R
+ the radius).
A point p = (x1, x2, . . . , xd) lies in this ball iﬀ

d∑

i=1(xi − ci)2 ⩽ ρ2 ⇔
 d∑

i=1(xi2 − 2xici + ci2) ⩽ ρ2

⇔
 ( d∑

i=1(−2ci)xi
)
 + (x12 + x22 + · · · + xd2) ⩽ ρ2 −
 d∑

i=1 ci2 ;

this equivalently means that ℓ(p) lies below the non-vertical hyperplane (in R
d+1)

h = h(c, ρ) = {x ∈ R
d+1 |
 d+1∑

i=1 hixi = hd+2} with

(h1, h2, . . . , hd, hd+1, hd+2) =
 (
(−2c1), (−2c2), . . . , (−2cd), 1, ρ2 −
 d∑

i=1 ci2)
 .

It follows that a set A ⊆ R
d is shattered by Bd (the set of closed balls in Rd) iﬀ
ℓ(A) := {ℓ(p) | p ∈ A} is shattered by ˇHd+1. Assuming (15.8), this readily yields

VCdim(R
d, Bd) = d + 1 .

The lifting map we have employed here is a special case of a more general paradigm
called linearization which maps non-linear conditions to linear conditions in higher
dimensions.
We have clariﬁed the VC-dimension for all examples of range spaces that we have
listed in Section 15.2.1, except for the one involving simplices. Before we elaborate on
this, let us prove a ﬁrst bound on the size of ε-nets when the VC-dimension is ﬁnite.

15.6 Small ε-Nets, an Easy Warm-up Version

Theorem 15.9 Let n, d ∈ N, d ⩾ 2, ε ∈ R
+. Let (X, R) be a range space of VC-
dimension d. If A ⊆ X with |A| = n, then there exists an ε-net N of A w.r.t. R with
|N| ⩽ ⌈ d ln n
ε ⌉.

Proof. We restrict our attention to the ﬁnite projected range space (A, R), R := R∣
∣
A ,
for which we know |R| ⩽ Φd(n) ⩽ n
d. It suﬃces to show that there is a set N ⊆ A with
|N| ⩽ d ln n
ε which contains an element from each r ∈ Rε := {r ∈ R | |r| > εn}.

176

CG 2012 15.6. Small ε-Nets, an Easy Warm-up Version

Suppose, for some s ∈ N (to be determined), we let N ∼ As. For each r ∈ Rε, we
know that prob(r ∩ N = ∅) < (1 − ε)s ⩽ e−εs. Therefore,

prob(N is not ε-net of A) = prob(∃r ∈ Rε : r ∩ N = ∅)

= prob( ⋁

r∈Rε(r ∩ N = ∅))

⩽ ∑

r∈Rε prob(r ∩ N = ∅) < |Rε|e−εs ⩽ n
de−εs .

It follows that if s is chosen so that n
de−εs ⩽ 1, then prob(N is not ε-net of A) < 1 and
there remains a positive probability for the event that N is an ε-net of A. Now

n
de−εs ⩽ 1 ⇔ n
d ⩽ eεs ⇔ d ln n ⩽ εs.

That is, for s = ⌈ d ln n
ε ⌉, the probability of obtaining an ε-net is positive, and therefore
an ε-net of that size has to exist.12 
If we are willing to invest a little more in the size of the random sample N, then the
probability of being an ε-net grows dramatically. More speciﬁcally, for s = ⌈ d ln n+λ
ε ⌉, we
have n
de−εs ⩽ n
de−d ln n−λ = e−λ ,

and, therefore, a sample of that size is an ε-net with probability at least 1 − e−λ.
We realize that we need d ln n
ε sample size to compensate for the (at most) n
d subsets
of A which we have to hit—it suﬃces to ensure positive success probability. The extra
λ
ε allows us to boost the success probability.
Also note that if A were shattered by R, then R = 2A and |R| = 2n. Using this bound
instead of n
d in the proof above would require us to choose s to be roughly n ln 2
ε , a
useless estimate which even exceeds n unless ε is large (at least ln 2 ≈ 0.69).

15.6.1 Smallest enclosing balls, again

It is time to rehabilitate ourselves a bit concerning the suggested procedure for computing
a small ball containing all but at most ε|A| points from an n-point set A ⊆ R
d.
Let (R
d, Bdcompl) be the range space whose ranges consist of all complements of closed
balls in R
d. This has the same VC-dimension d + 1 as (R
d, Bd). Indeed, if A ∩ r = A ′ for
a ball r, then A ∩ (R
d \ r) = A \ A ′, so A is shattered by Bd if and only if A is shattered
by Bdcompl.
Hence, if we choose a sample N of size s = ⌈ (d+1) ln n+λ
ε ⌉ then, with probability
at least 1 − e−λ this is an ε-net for A w.r.t. Bdcompl. Let us quickly recall what this

12This line of argument “If an experiment produces a certain object with positive probability, then it has
to exist”, as trivial as it is, admittedly needs some time to digest. It is called The Probabilistic Method,
and was used and developed to an amazing extent by the famous Hungarian mathematician Paul Erdős
starting in the thirties.
 177

Chapter 15. Epsilon Nets CG 2012

means: whenever the complement of some ball B has empty intersection with N, then
this complement contains at most an ε|A| points of A. As a consequence, the smallest
ball enclosing N has at most ε|A| points of A outside, with probability at least 1 − e−λ.

15.7 Even Smaller ε-Nets

We still need to prove part 2 of Theorem 15.2, the existence of ε-nets whose size is
independent of A. For this, we employ the same strategy as in the previous section, i.e.
we sample elements from A uniformly at random, with replacement; a reﬁned analysis
will show that—compared to the bound of Theorem 15.9—much less elements suﬃce.
Here is the main technical lemma.

Lemma 15.10 Let (X, R) be a range space of VC-dimension δ ⩾ 2, and let A ⊆ X be
ﬁnite. If x ∼ Am for m ⩾ 8/ε, then for the set Nx of elements occurring in x, we
have prob(Nx is not an ε-net for A w.r.t. R) ⩽ 2Φδ(2m)2− εm
2 .

Before we prove this, let us derive the bound of Theorem 15.2 from it. We want that

2Φδ(2m)2− εm
2 < 1,

since then we know that an ε-net of size m exists. We have

2Φδ(2m)2− εm
2 < 1
⇐ 2(2m)δ < 2 εm
2

⇔ 1 + δ log2(2m) < εm
2
⇐ 2δ log2 m < εm
2

⇔ 4δ
ε < m
log2 m.

In the second to last implication, we have used δ, m ⩾ 2. Now we claim that the latter
inequality is satisﬁed for m = 2 4δ
ε log2 4δ
ε . To see this, we need that m
log2 m > α for
m = 2α log2 α and α = 4δ
ε . We compute

m
log2 m = 2α log2 α
log2(2α log2 α) = 2α log2 α
1 + log2 α + log2 log2 α = α 2 log2 α
1 + log2 α + log2 log2 α ⩾ α

as long as
 log2 α ⩾ 1 + log2 log2 α ⇔ log2 α ⩾ log2 2 log2 α ⇔ α ⩾ 2 log2 α,

which holds as long as α ⩾ 2, and this is satisﬁed for α = 4δ
ε .

178

CG 2012 15.7. Even Smaller ε-Nets

Proof. (Lemma 15.10) By going to the projection (A, (
∣
∣R A), we may assume that X = A,
so we have a ﬁnite range space over n elements (see also Section 15.4). Fix ε ∈ R
+. For
t ∈ N, a range r ∈ R and x ∈ At (a t-vector of elements from A), we deﬁne

count(r, x) = |{i ∈ [t] : xi ∈ r}|.

Now we consider two events over A2m. The ﬁrst one is the bad event of not getting
an ε-net when we choose m elements at random from A (plus another m elements that
don’t matter). Recall that Rε = {r ∈ R : |r| > εn}.

Q := {xy ∈ A2m | ∃r ∈ Rε : count(r, x) = 0}

Thus prob(Q) = prob(Nx is not ε-net) which is exactly what we want to bound.
The second auxiliary event looks somewhat weird.

J := {xy ∈ A2m | x ∈ Am, y ∈ Am, ∃r ∈ Rε : count(r, x) = 0 and count(r, y) ⩾ εm
2 }.

This event satisﬁes J ⊆ Q and contains pairs of sequences x and y with somewhat
contradicting properties for some r. While x fails to contain any element from r, y has
many elements from r.

Claim 1. prob(J) ⩽ prob(Q) < 2prob(J).

The ﬁrst inequality is a consequence of J ⊆ Q. To prove the second inequality, we
show that prob(J)
prob(Q) = prob(J ∩ Q)
prob(Q) = prob(J | Q) ⩾ 1
2.

So suppose that xy ∈ Q, with “witness” r, meaning that r ∈ Rε and count(r, x) = 0.
We show that xy ∈ J with probability at least 1/2, for every ﬁxed such x and y chosen
randomly from Am. This entails the claim.
The random variable count(r, y) is a sum of m independent Bernoulli experiments
with success probability p := |r|/n > ε (thus expectation p and variance p(1 − p)).
Using linearity of expectation and variance (the latter requires independence of the ex-
periments), we get

E(count(r, y)) = pm,
Var(count(r, y)) = p(1 − p)m.

Now we use Chebyshew’s inequality13 to bound the probability of the “bad” event that

13prob(|X − E(X)| ⩾ kVar(X)) ⩽ 1
k2Var(X)
 179

Chapter 15. Epsilon Nets CG 2012

count(r, y) < εm
2 . We have

prob (
count(r, y) < εm
2
 )

⩽ prob (
count(r, y) < pm
2
 )

⩽ prob (
|count(r, y) − E(count(r, y))| > pm
2
 )

= prob (
|count(r, y) − E(count(r, y))| > 1
2(1 − p) Var(count(r, y)))

⩽ 4(1 − p)2

p(1 − p)m = 4(1 − p)
pm ⩽ 4
pm < 4
εm ⩽ 1
2 ,

since m ⩾ 8
ε . Hence
 prob (count(r, y) ⩾ εm
2
 ) ⩾ 1
2 ,

and the claim is proved.
Now the weird event J reveals its signiﬁcance: we can nicely bound its probability.
The idea is this: We enumerate A as A = {a1, a2, . . . , an} and let the type of z ∈ At be
the n-sequence
 type(z) = (count(a1, z), count(a2, z), . . . , count(an, z)).

For example, the type of z = (1, 2, 4, 2, 2, 4) w.r.t. A = {1, 2, 3, 4} is type(z) = (1, 3, 0, 2).
Now ﬁx an arbitrary type τ. We will bound the conditional probability prob(xy ∈ J |
xy has type τ), and the value that we get is independent of τ. It follows that the same
value also bounds prob(J).

Claim 2. prob(xy ∈ J | xy has type τ) ⩽ 2Φδ(2m)2−εm/2.

To analyze the probability in question, we need to sample z = xy uniformly at random
from all sequences of type τ. This can be done as follows: take an arbitrary sequence z ′

of type τ, and then apply a random permutation π ∈ S2m to obtain z = π(z ′), meaning
that zi = z ′
π(i) for all i.

Why does this work? First of all, π preserves the type, and it is easy to see that all
sequences z of type τ can be obtained in this way. Now we simply count the number of
permutations that map z ′ to a ﬁxed z and see that this number only depends on the τ,
so it is the same for all z. Indeed, for every element ai ∈ A, there are τi! many ways of
mapping the ai’s in z ′ to the ai’s in z. The number of permutations that map z ′ to z is
therefore given by n∏

i=1 τi!.

180

CG 2012 15.7. Even Smaller ε-Nets

By these considerations,

prob(xy ∈ J | xy has type τ) = prob(π(z ′) ∈ J)}.

To estimate this, we let S be the set of distinct elements in z ′ (this is also a function
of the type τ). Since (X, R) has VC-dimension δ, we know from Lemma 15.6 that
|R∣
∣
S | ⩽ Φδ(2m), so at most that many diﬀerent subsets T of S can be obtained by
intersections with ranges r ∈ R, and in particular with ranges r ∈ Rε.
Now we look at some ﬁxed such T , consider a permutation π and write π(z ′) = xy.
We call T a witness for π if no element of x is in T , but at least εm/2 elements of y are
in T . According to this deﬁnition,

π(z ′) ∈ J ⇔ π has some witness T ⊆ S.

By the union bound,

prob(xy ∈ J | xy has type τ) = prob(π(z ′) ∈ J) ⩽ ∑

T prob(T is a witness for π).

Suppose that z ′ contains ℓ ⩾ εm/2 occurences of elements of T (for smaller ℓ, T
cannot be a witness). The probability of T being a witness for a random permutation is
then (m
ℓ )

(2m
ℓ ) = m(m − 1) · · · m(m − ℓ + 1)
2m(2m − 1) · · · (2m − l + 1) ⩽ 2−ℓ ⩽ 2− εm
2 ,

since among all the (2m
ℓ ) equally likely ways in which π distributes the ℓ occurences in
z, exactly the (m
ℓ ) equally likely ways of putting them into y are good.14 Summing up
over all at most Φδ(2m) sets T , we get

prob(xy ∈ J | xy has type τ) ⩽ Φδ(2m)2− εm
2 ,

for all τ.
The proof is ﬁnished by combining the two claims:

prob(Nx is not ε-net) = prob(Q) ⩽ 2prob(J) ⩽ 2Φδ(2m)2− εm
2 . 
Questions

67. What is a range space? Give a deﬁnition and a few examples.

68. What is an epsilon net? Provide a formal deﬁnition, and explain in words what
it means.

14This argument can be made more formal by explicitly counting the permutations that map {1, 2, . . . , ℓ}
to the set {1, 2, . . . , m}. We leave this to the reader.

181

Chapter 15. Epsilon Nets CG 2012

69. What is the VC dimension of a range space Give a deﬁnition, and compute the
VC dimension of a few example range spaces.

70. Which range spaces always have small epsilon nets (and how small), and
which ones don’t? Explain Theorem 15.2.

71. How can you compute small epsilon nets? Explain the general idea, and give
the analysis behind the weaker bound of Theorem 15.9.

72. How can you compute smaller epsilon nets? Sketch the main steps of the proof
of the stronger bound of Theorem 15.2.

References

[1] D. Haussler and Emo Welzl, Epsilon-nets and simplex range queries. Discrete Com-
put. Geom., 2, (1987), 127–151.
 182
