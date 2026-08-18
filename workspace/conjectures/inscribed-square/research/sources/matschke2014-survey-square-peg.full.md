<!-- source: https://pure.mpg.de/rest/items/item_3120610/component/file_3120611/content | converted from PDF -->

A Survey on the
Square Peg Problem

Benjamin Matschke

T

his is a short survey article on a 103-
year-old and still open problem in plane
geometry, the Square Peg Problem. It
is also known as the Inscribed Square
Problem and it is due to Otto Toeplitz.

Conjecture 1 (Square Peg Problem, [39]). Every
continuous simple closed curve in the plane γ : S 1 →
R 2 contains four points that are the vertices of a
square.
 Figure 1. Example for Conjecture 1.

A continuous simple closed curve in the plane
is also called a Jordan curve, and it is the same as
an injective map from the unit circle into the plane
or, equivalently, a topological embedding S 1 ↩ R 2.
In its full generality Toeplitz’s problem is still
open. So far it has been solved aﬃrmatively
for curves that are “smooth enough” by various
authors for varying smoothness conditions; see
the next section. All of these proofs are based on
the fact that smooth curves inscribe generically an
odd number of squares, which can be measured
in several topological ways. However, so far none
of these methods can be made to work for the
general continuous case.
One may think that the general case of the Square
Peg Problem can be reduced to the case of smooth
curves by approximating a given continuous curve

Benjamin Matschke is a researcher at Max Planck Institute
for Mathematics, Bonn. His email address is matschke@
mpim-bonn.mpg.de.

The author was supported by Deutsche Telekom Stiftung,
NSF Grant DMS-0635607, an EPDI-fellowship, and MPIM
Bonn.

DOI: http://dx.doi.org/10.1090/noti1100
 Figure 2. We do not require the square to lie fully
inside γγγ; otherwise there are counterexamples.

γ by a sequence of smooth curves γn: Any γn
inscribes a square Qn, and by compactness there
is a converging subsequence (Qnk )k whose limit is
an inscribed square for the given curve γ. However,
this limit square is possibly degenerate to a point,
and so far there is no argument known that can
deal with this problem.
Suppose we could show that any smooth (or
equivalently any piecewise linear) curve γ that
contains in its interior a ball of radius r inscribes
a square of side length at least √
2r (or at least εr
for some constant ε > 0). Then the approximation
argument would imply that any continuous curve
has the same property. However, it seems that we
need more geometric than merely topological ideas
to show the existence of large inscribed squares.
Other surveys are due to Klee and Wagon [21,
Problem 11], Nielsen [30], Denne [4], Karasev [18,
2.6, 4.6], and Pak [32, I.3, I.4]. Jason Cantarella’s
homepage oﬀers some animations. A Java applet
and an extended version of this article are available
on my homepage.
In order to raise awareness, let me put 100
euros on each of the Conjectures 1, 8, and 13. That
is, you may earn 300 euros in total.
I want to thank the referees for many very useful
comments.

History of the Square Peg Problem
The Square Peg Problem ﬁrst appeared in the
literature in the conference report [39] in 1911.
Toeplitz gave a talk whose second part had the
title “On some problems in topology”. The report
on that second part is rather short:

346 Notices of the AMS Volume 61, Number 4

b) Ueber einige Aufgaben der Analysis situs.
[. . .]
b) Der Vortragende erzählt von zwei Aufgaben
der Analysis Situs, zu denen er gelangt ist,
und dann von der folgenden dritten, deren
Lösung ihm nur für konvexe Kurven gelungen
ist: Auf jeder einfach geschlossenen stetigen
Kurve in der Ebene gibt es vier Punkte,
welche ein Quadrat bilden. Diskussion: Die
Herren Fueter, Speiser, Laemmel, Stäckel,
Grossmann.

Here is an English translation:

b) On some problems in topology. [. . .]
b) The speaker talks about two problems in
topology that he obtained, and then about
the following third one, whose solution he
managed to ﬁnd only for convex curves:
On every simple closed continuous curve in
the plane there are four points that form a
square. Discussions: Messrs. Fueter, Speiser,
Laemmel, Stäckel, Grossmann.

It seems that Toeplitz never published a proof.
In 1913 Arnold Emch [6] presented a proof for
“smooth enough” convex curves. Two years later
Emch [7] published a further proof that requires a
weaker smoothness condition. However, he did not
note that the special case of smooth convex curves
already implies by a limit argument that all convex
curves inscribe squares. In a third paper from 1916,
Emch [8] proved the Square Peg Problem for curves
that are piecewise analytic with only ﬁnitely many
inﬂection points and other singularities where the
left- and right-side tangents at the ﬁnitely many
nonsmooth points exist.
Emch states in his second paper [7] that he
was not aware of Toeplitz’s and his students’
work and that the problem was suggested to him
by Kempner. From 1906 to 1913 Toeplitz was a
postdoc in Göttingen. Aubrey J. Kempner was an
English mathematician who ﬁnished his Ph.D. with
Edmund Landau in Göttingen in 1911. Afterwards
he went to the University of Illinois in Urbana-
Champaign and stayed there until 1925 according
to http://www.maa.org/history/presidents/
kempner.html (another biography of Kempner
can be found at http://www.findagrave.com/
cgi-bin/fg.cgi?page=gr&GRid=13165695,
which claims diﬀerent dates). Emch joined
the faculty of the same university in 1911.
I will let the reader decide whether this is enough
information on how all these parts ﬁt together and
who considered the Square Peg Problem ﬁrst. It is
usually attributed to Toeplitz.
In 1929 Schnirelman proved the Square Peg
Problem for a class of curves that is slightly
larger than C 2. An extended version [37] which
also corrects some minor errors was published
 posthumously in 1944. Guggenheimer [12] states
that the extended version still contains errors,
which he claims to correct. However, in my point
of view, Schnirelman’s proof is correct except for
some minor errors. His main idea is a bordism
argument; below we give some details. Since the
transversality machinery was not invented at this
time, Schnirelman’s proof contains many computa-
tions in explicit coordinates. Guggenheimer’s main
lemma, on the other hand, admits counterexam-
ples; he was not aware that squares can vanish
pairwise when one deforms the curve.
Other proofs are due to Hebbert [14] when γ is
a quadrilateral, Zindler [43] and Christensen [3]
for convex curves, Jerrard [16] for analytic curves,
Nielsen–Wright [31] for curves that are symmetric
across a line or about a point, Stromquist [38] for
locally monotone curves, Vre´cica–Živaljevi´c [40] for
Stromquist’s class of curves, Pak [32] for piecewise
linear curves, Sagols–Marín [35], [36] for similar
discretizations, Cantarella–Denne–McCleary [2] for
curves with bounded total curvature without cusps
and for C 1-curves, Makeev [23] for star-shaped
C 2-curves that intersect every circle in at most
4 points (more generally he proved the Circular
Quad Peg Problem 9 for such curves, see below),
Matschke [26] for a technical open and dense class
of curves and for continuous curves in certain
bounded domains. In the next section we shall
review some of these special cases in more detail.
Pettersson, Tverberg, and Östergård [33] have
the latest result, which uses a computer: They
showed that any Jordan curve in the 12 × 12 square
grid inscribes a square whose size is at least 1/√
2
times the size of the largest axis-parallel square
that ﬁts into the interior of the curve.

Special Cases
Let us discuss some of the above-mentioned proofs
in more detail.

Emch’s Proof

Let γ : S 1 ↩ R 2 be the given piecewise analytic
curve. Fixing a line τ, Emch considers all secants
of γ that are parallel to τ and calls the set of all
midpoints of these secants the set of medians Mτ .
Under some genericity assumptions he proves that
for two orthogonal lines τ and τ ⊥, Mτ intersects
Mτ ⊥ in an odd number of points. Nowadays
one could write this down homologically. These
intersections correspond to inscribed rhombi,
where the two intersecting secants are the two
diagonals of the rhombus.
Now he rotates τ continuously by 90 degrees
and argues that Mτ ∩ Mτ ⊥ moves continuously,
where at ﬁnitely many times two intersection points
can merge and disappear or two new intersection

April 2014 Notices of the AMS 347

points can appear. When τ is rotated by 90 degrees,
the one-dimensional family of intersection points
closes up to a possibly degenerate union of circle
components.
Since Mτ ∩ Mτ ⊥ is odd, Emch argues that an
odd number of these components must be Z /4Z -
invariant, meaning that if R1R2R3R4 is a rhombus
in such a component, then R2R3R4R1 must also be
in the same component. By the mean value theorem,
when moving from R1R2R3R4 to R2R3R4R1 along
a component of inscribed rhombi, at some point
the diagonals must have equal length. That is, we
obtain an inscribed square. This argument also
implies that the number of inscribed squares is
(generically) odd for Emch’s class of curves.

Schnirelman’s Proof

Schnirelman solved the Square Peg Problem for a
slightly larger class than C 2 using an early bordism
argument that yields a very conceptual proof. His
idea was that the set of inscribed squares can
be described as a preimage, for example, in the
following way: Let γ : S 1 ↩ R 2 be the given curve.
The space (S 1)4 parameterizes quadrilaterals that
are inscribed in γ. We construct a so-called test-map,

(1) fγ : (S 1)4 → R 6,

which sends a 4-tuple (x1, x2, x3, x4) of points
on the circle to the mutual distances between
γ(x1), . . . , γ(x4) ∈ R 2. Let V be the 2-dimensional
linear subspace of R 6 that corresponds to the
points where all four edges are of equal length
and the two diagonals are of equal length. The pre-
image f −1
γ (V ) is parameterizing the set of inscribed
squares, plus a few “degenerate components”. The
degenerated components consist of points where
x1 = x2 = x3 = x4—these are the degenerate
squares—and more generally of 4-tuples where
x1 = x3 and x2 = x4.
Now Schnirelman argues as follows: An ellipse
inscribes exactly one square up to symmetry. Now
deform the ellipse (via some smooth isotopy) into
the given curve along other curves γt , t ∈ [0, 1]. By
smoothness these inscribed squares do not come
close to the degenerate quadrilaterals during the
deformation; that is, they do not shrink to a point.
Thus the nondegenerate part of all preimages
f −1
γt (V ) forms a 1-manifold that connects the
solution sets for γ and the ellipse, and since 1-
manifolds always have an even number of boundary
points, the parities of the number of inscribed
squares on γ and on the ellipse coincide.
Thus, any smooth curve inscribes generically
an odd number of squares. Here we have swept
technical arguments concerning transversality
under the rug, which we hope is appreciated by
the reader.
 fellipse

R 6 ⊃ V

fγ

(S 1)4

(S 1)4

[0, 1] × (S 1)
4

Figure 3. The bordism between the solution sets
for γγγ and the ellipse. To simplify the ﬁgure we
already modded out the symmetry group of the
square and omitted the degenerate components.

Figure 4. Example of a piece of a locally
monotone curve. Note that Figure 1 is not locally
monotone because of the spiral.

For general curves, it is diﬃcult to separate
the degenerate quadrilaterals in f −1(V ) from the
squares we are interested in. This is the basic
reason why the Square Peg Problem could not be
solved completely with the current methods.

Stromquist’s Criterion

Stromquist’s class of curves for which he proved
the Square Peg Problem is very beautiful, and it
is the second strongest one: A curve γ : S 1 ↩ R 2

is called locally monotone if every point x ∈ S 1

admits a neighborhood U and a linear functional
ℓ : R 2 → R such that ℓ ◦ γ|U is strictly monotone.

Theorem 2 (Stromquist). Any locally monotone
embedding γ : S 1 ↩ R 2 inscribes a square.

In his proof Stromquist also considers the set
of inscribed rhombi ﬁrst.

Fenn’s Table Theorem

A beautiful proof for convex curves is due to
Fenn [9]. It follows as an immediate corollary from
his table theorem.

Theorem 3 (Fenn). Let f : R 2 → R ≥0 be a non-
negative function that is zero outside a compact
convex disc D and let a > 0 be an arbitrary real
number. Then there exists a square in the plane
with side length a and whose center point belongs
to D such that f takes the same value on the vertices
of the square.

As the reader might guess, Fenn’s proof basically
uses a mod-2 argument showing that the number
of such tables is generically odd.
The table theorem implies the Square Peg
Problem for convex curves γ by constructing a

348 Notices of the AMS Volume 61, Number 4

ε γ a
 a
 a

b γ(4)γ(1)
 γ(3)γ(2)
 a > b

1 2 3 4

Figure 5. A special trapezoid of size εεε.

height function f : R 2 → R ≥0 whose level sets
f −1(x) are similar to γ for all x > 0.
Zaks [42] found an analogous “chair theorem”,
where instead of a square table he considers
triangular chairs with a ﬁxed direction. Kronheimer–
Kronheimer [22] found conditions on ∂D such
that the table/chair can be chosen such that all
four/three vertices lie in D: namely, ∂D should not
inscribe a square/triangle of a smaller size. More
table theorems are due to Meyerson [28].

An Open and Dense Criterion

In [26] the Square Peg Problem was proved for the
so far weakest smoothness condition.

Theorem 4. Let γ : S 1 ↩ R 2 be a Jordan curve.
Assume that there is 0 < ε < 2π such that γ con-
tains no (or generically an even number of) special
trapezoids of size ε. Then γ inscribes a square.

Here an inscribed special trapezoid is a 4-tuple
of pairwise distinct points x1, . . . , x4 ∈ S 1 lying
clockwise on S 1 such that the points Pi := γ(xi)
satisfy

||P1 − P2|| = ||P2 − P3|| = ||P3 − P4|| > ||P4 − P1||

and ||P1 − P3|| = ||P2 − P4||.

The size of this special trapezoid is deﬁned as the
length of the clockwise arc in S 1 from x1 to x4.
The set of curves without inscribed special
trapezoids of a ﬁxed size ε is open and dense
in the space of embeddings S 1 ↩ X with respect
to the compact-open topology. This theorem is
basically the exact criterion that one obtains by
applying equivariant obstruction theory to the
test-map (1). Vre´cica and Živaljevi´c [40] are the
ﬁrst to apply obstruction theory to the Square Peg
Problem, and they proved it for Stromquist’s class
of locally monotone curves.

An Explicit Open Criterion

All previous criteria on curves for which the Square
Peg Problem was proved are deﬁned by local
smoothness conditions. The following criterion
from [26] is a global one which yields an open set
of not necessarily injective curves in C 0(S 1, R 2)
with respect to the C 0-topology or, equivalently,
the compact-open topology.
 Figure 6. Example for Theorem 5.

Theorem 5. Let A denote the annulus {x ∈ R 2 | 1 ≤
||x|| ≤ 1 + √
2}. Suppose that γ : S 1 → A is a
continuous closed curve in A that is nonzero in
π1(A) = Z . Then γ inscribes a square of side length
at least √2.

It is open whether the outer radius 1 + √
2 of A
can be increased by some small ε > 0.
The proof idea is very simple: If the annulus A
is thin enough, then the set of squares with all
vertices in A splits into two connected components:
big squares and small squares. A generic curve
that represents a generator of π1(A) inscribes an
odd number of big squares (and an even number
of small squares).

Related Problems

The Number of Inscribed Squares

Popvassilev [34] constructed for any n ≥ 1 a
smooth convex curve that has exactly n inscribed
squares, every square being counted exactly once
and not with multiplicity. All but one of the n
squares in his construction are nongeneric. They
will disappear immediately after deforming the
curve by a suitable C ∞-isotopy.
In [26] this author gave the parity of the number
of squares on generic smooth immersed curves in
the plane, which depends not only on the isotopy
type of the immersion but also on the intersection
angles.
Van Heijst proves in his upcoming master’s
thesis [15] that any real algebraic curve in R 2 of
degree d inscribes either at most (d4 − 5d2 + 4d)/4
or inﬁnitely many squares. For this he makes
use of Bernstein’s theorem, which states that the
number of common zeros in (C ∗)k of k generic
Laurent polynomials in k variables with prescribed
Newton polytopes equals the mixed volume of
these polytopes.

Inscribed Triangles

It is not hard to show that any smooth embedding
γ : S 1 → R 2 inscribes arbitrary triangles, even if
we prescribe where one of the vertices has to sit.
Moreover, the set of all such inscribed triangles
determines a homology class α ∈ H1(P3, Z ) = Z ,
where P3 is the set of 3-tuples of points on γ
that lie counterclockwise on the curve. The class

April 2014 Notices of the AMS 349

Figure 7. The image of fff , a self-intersecting
Möbius strip with boundary γγγ.

α turns out to be a generator, as one sees from
inspecting the situation for the circle.
For continuous curves Nielsen [29] proved the
following version of the result:

Theorem 6 (Nielsen). Let T be an arbitrary triangle
and γ : S 1 -→ R 2 an embedded circle. Then there
are inﬁnitely many triangles inscribed in γ which
are similar to T , and if one ﬁxes a vertex of smallest
angle in T , then the set of the corresponding vertices
on γ is dense in γ.

Inscribed Rectangles

Instead of squares one may ask whether any
embedded circle in the plane inscribes a rectangle.
If one does not prescribe the aspect ratio, then the
answer is aﬃrmative.

Theorem 7 (Vaughan). Any continuous embedding
γ : S 1 ↩ R 2 inscribes a rectangle.

Vaughan’s proof, which appeared in Meyer-
son [28], is very beautiful: Z 2 := Z /2Z acts on the
torus (S 1)
2 by permuting the coordinates, and the
quotient space (S 1)
2/Z 2 is a Möbius strip. The
proof of Theorem 7 uses the fact that the map
f : (S 1)
2/Z 2 → R 2 × R ≥0 given by

f (x, y) = (
(γ(x) + γ(y))/2, ||γ(x) − γ(y)||)

must have a double point; otherwise it would
extend to an embedding of R P 2 into R 3 by gluing
to that Möbius strip the disc I × {0}, where I ⊂ R 2

is the interior of γ. The double point corresponds
to two secants of γ having the same length and
the same midpoint. Hence this forms an inscribed
rectangle.
If we furthermore prescribe the aspect ratio of
the rectangle, then the problem is wide open, even
for smooth or piecewise linear curves.

Conjecture 8 (Rectangular Peg Problem). Every C ∞

embedding γ : S 1 → R 2 contains four points that
are the vertices of a rectangle with a prescribed
aspect ratio r > 0.

This conjecture is highly interesting, since the
standard topological approach does not yield a
proof : The equivariant homology class of the
solution set, a Z -valued smooth isotopy invariant
 of the curve, turns out to be zero. For example, an
ellipse inscribes a positive and a negative rectangle.
Stronger topological tools fail as well. It seems
again that more geometric ideas are needed.
Equivalently we could state Conjecture 8 for
all piecewise linear curves. Proofs exist only for
the case r = 1, which is the smooth Square Peg
Problem, for arbitrary r in case the curve is close
to an ellipse, see Makeev [23] and Conjecture 9
below; and for r = √
3 in case the curve is close to
convex, see [26].
A proof for the Rectangular Peg Problem was
claimed by Griﬃths [10], but it contains errors
regarding the orientations. Essentially, he calcu-
lated that the number of inscribed rectangles of
the given aspect ratio counted with appropriate
signs and modulo symmetry is 2. However, zero is
correct.

Other Inscribed Quadrilaterals

It is natural to ask what other quadrilaterals can
be inscribed into closed curves in the plane. Since
the unit circle is a curve, those quadrilaterals must
be circular; that is, they must have a circumcircle.
Depending on the class of curves that we look
at, the following two conjectures seem reasonable.

Conjecture 9 (Circular Quad Peg Problem). Let Q
be a circular quadrilateral. Then any C ∞ embed-
ding γ : S 1 → R 2 admits an orientation-preserving
similarity transformation that maps the vertices of
Q into γ.

Makeev [23] proved a ﬁrst instance of this
conjecture, namely, for the case of star-shaped
C 2-curves that intersect every circle in at most 4
points.
Furthermore, Karasev [20] proved that, for any
smooth curve and a given Q = ABCD, either this
conjecture holds or one can ﬁnd two inscribed
triangles similar to ABC such that the two corre-
sponding fourth vertices D coincide (but D may
not lie on γ). The proof idea is a beautiful geometric
volume argument. It should be stressed that most
open problems discussed here are geometric prob-
lems rather than topological ones: We understand
the basic algebraic topology here quite well but not
the restrictions on the topology that the geometry
dictates. New geometric ideas such as Karasev’s
are needed.

Conjecture 10 (Trapezoidal Peg Problem). Let T
be an isosceles trapezoid. Then any piecewise-linear
embedding γ : S 1 → R 2 inscribes a quadrilateral
similar to T .

The reason for restricting the latter conjecture
to isosceles trapezoids, that is, trapezoids with
circumcircle, is that all other circular quadrilaterals
cannot be inscribed into very thin triangles. This
was observed by Pak [32].

350 Notices of the AMS Volume 61, Number 4

Other Inscribed Polygons

For any n-gon P with n ≥ 5 it is easy to ﬁnd many
curves that do not inscribe P . If we do not require
all vertices to lie on γ, then Makeev has some
results for circular pentagons; see [25].
Alternatively, we can relax the angle conditions;
that is, we require only that the edge ratios are
the same as the ones in a given polygon P . Then
as for the triangles above, one can show that the
set of such n-gons represents the generator of
H1(Pn; Z ) = Z , where Pn is the set of n-tuples
of points on γ that lie counterclockwise on the
curve; see Meyerson [27], Wu [41], Makeev [25], and
Vre´cica–Živaljevi´c [40].

Higher Dimensions

In higher dimensions one may ask whether any
(n − 1)-sphere that is smoothly embedded in R n

inscribes an n-cube in the sense that all vertices
of the cube lie on the sphere. However, most
smooth embeddings S n−1 ↩ R n do not inscribe
an n-cube for n ≥ 3, in the sense that these
embeddings form an open and dense subset
of all smooth embeddings in the compact-open
topology, a heuristic reason being that the number
of equations to fulﬁll is larger than the degrees of
freedom. An explicit example is the boundaries of
very thin simplices, as was noted by Kakutani [17]
for n = 3. Hausel–Makai–Sz˝ucs [13] proved that
the boundary of any centrally symmetric convex
body in R 3 inscribes a 3-cube.
If we do not want to require further symmetry
on the embedding S n−1 ↩ R n, then crosspolytopes
are more suitable higher analogs of squares: The
regular n-dimensional crosspolytope is the convex
hull of {±ei} where ei are the standard basis
vectors in R n.

Theorem 11 (Makeev, Karasev). Let n be an odd
prime power. Then every smooth embedding Γ :
S n−1 → R n contains the vertices of a regular n-
dimensional crosspolytope.

The n = 3 case was posed as Problem 11.5 in Klee
and Wagon [21]. This was answered aﬃrmatively
by Makeev [24]. Karasev [19] generalized the proof
to arbitrary odd prime powers. Akopyan and
Karasev [1] proved the same theorem for n = 3
in case Γ is the boundary of a simple polytope by
a careful and nontrivial limit argument from the
smooth case.
Gromov [11] proved a similar theorem for
inscribed simplices.

Theorem 12 (Gromov). Any compact set S ⊂ R d

with C 1-boundary and nonzero Euler characteristic
inscribes an arbitrary given simplex up to similarity
on its boundary ∂S.
 Figure 8. Intuition behind Conjecture 13: Think
of a square table for which we want to ﬁnd a
spot on Earth such that all four table legs are at
the same height.

Let us ﬁnish with the following table problem
on the sphere.

Conjecture 13 (Table problem on S 2). Suppose
x1, . . . , x4 ∈ S 2 ⊂ R 3 are the vertices of a square
that is inscribed in the standard 2-sphere, and let
h : S 2 → R be a smooth function. Then there exists
a rotation ρ ∈ SO(3) such that h(ρ(x1)) = · · · =
h(ρ(x4)).

So far this result has been proven only when
x1, . . . , x4 lie on a great circle (see Dyson [5]), since
this is the only case in which the generic number
of solutions is odd. The critical points of h can be
thought of as the spots on which you can put an
inﬁnitesimally small table.

References
1. Arseniy Akopyan and Roman N. Karasev, Inscribing
a regular octahedron into polytopes, Discrete Math.
313 (2013), no. 1, 122–128.
2. Jason Cantarella, Elizabeth Denne, and John Mc-
Cleary, Transversality in conﬁguration spaces and the
Square Peg Problem, in preparation.
3. Carl Marius Christensen, A square inscribed in a
convex ﬁgure (in Danish), Matematisk Tidsskrift B 1950
(1950), 22–26.
4. Elizabeth Denne, Inscribed squares: Denne speaks,
http://quomodocumque.wordpress.com/2007/08/
31/inscribed-squares-denne-speaks, 2007, Guest
post on Jordan S. Ellenberg’s blog Quomodocumque.
5. Freeman J. Dyson, Continuous functions deﬁned on
spheres, Ann. Math. 54 (1951), no. 2, 534–536.
6. Arnold Emch, Some properties of closed convex
curves in a plane, Amer. J. Math. 35 (1913), 407–412.
7. , On the medians of a closed convex polygon,
Amer. J. Math. 37 (1915), 19–28.
8. , On some properties of the medians of closed
continuous curves formed by analytic arcs, Amer. J.
Math. 38 (1916), no. 1, 6–18.
9. Roger Fenn, The table theorem, Bull. London Math.
Soc. 2 (1970), 73–76.
10. H. Brian Grifﬁths, The topology of square pegs in
round holes, Proc. London Math. Soc. 62 (1990), no. 3,
647–672.
11. Mikhail L. Gromov, Simplexes inscribed on a hyper-
surface (Russian), Matematicheskie Zametki 5 (1969),
81–89.
12. Heinrich W. Guggenheimer, Finite sets on curves and
surfaces, Israel J. Math. 3 (1965), 104–112.
13. Tamás Hausel, Endre Makai Jr., and András Sz˝ucs,
Inscribing cubes and covering by rhombic dodecahedra

April 2014 Notices of the AMS 351

via equivariant topology, Mathematika 47 (2002), no. 1-
2, 371–397.
14. Clarence M. Hebbert, The inscribed and circum-
scribed squares of a quadrilateral and their signiﬁcance
in kinematic geometry, Ann. of Math. (2) 16 (1914/15),
no. 1-4, 38–42.
15. Wouter van Heijst, master’s thesis, in preparation.
16. Richard P. Jerrard, Inscribed squares in plane curves,
Trans. Amer. Math. Soc. 98 (1961), 234–241.
17. Shizuo Kakutani, A proof that there exists a circum-
scribing cube around any bounded closed convex set
in R3, Ann. Math. 43 (1942), no. 4, 739–741.
18. Roman N. Karasev, Topological methods in combi-
natorial geometry, Russian Math. Surveys 63 (2008),
no. 6, 1031–1078.
19. , Inscribing a regular crosspolytope, http://
arxiv.org/abs/0905.2671, 2009.
20. Roman N. Karasev and Aleksei Yu. Volovikov,
A note on Makeev’s conjectures, http://arxiv.
org/abs/1002.4070, 2010.
21. Victor Klee and Stan Wagon, Old and New Unsolved
Problems in Plane Geometry and Number Theory, Dol-
ciani Mathematical Expositions, Math. Assoc. America,
1996.
22. Erwin H. Kronheimer and Peter B. Kronheimer, The
tripos problem, J. London Math. Soc. (2) 24 (1981), no. 1,
182–192.
23. Vladimir V. Makeev, On quadrangles inscribed in a
closed curve, Math. Notes 57 (1995), no. 1-2, 91–93.
24. , Universally inscribed and outscribed polytopes,
Ph.D. thesis, Saint-Petersburg State University, 2003.
25. , On quadrangles inscribed in a closed curve and
the vertices of the curve, J. Math. Sci. 131 (2005), no. 1,
5395–5400.
26. Benjamin Matschke, Equivariant topology methods in
discrete geometry, Ph.D. thesis, Freie Universität Berlin,
2011.
27. Mark D. Meyerson, Equilateral triangles and con-
tinuous curves, Polska Akademia Nauk. Fundamenta
Mathematicae 110 (1980), no. 1, 1–9.
28. , Balancing acts, Topology Proc. 6 (1981), no. 1,
59–75.
29. Mark J. Nielsen, Triangles inscribed in simple closed
curves, Geometriae Dedicata 43 (1992), 291–297.
30. , Web page on Figures Inscribed in Curves,
http://www.webpages.uidaho.edu/~markn/squares/,
2000.
31. Mark J. Nielsen and Stephen E. Wright, Rectangles
inscribed in symmetric continua, Geom. Dedicata 56
(1995), no. 3, 285–297.
32. Igor Pak, Lectures on Discrete and Polyhedral
Geometry, http://math.ucla.edu/~pak/book.htm,
2010.
33. Ville H. Pettersson, Helge Tverberg, and Patric R. J.
Östergård, A note on Toeplitz’ square problem,
submitted, 2013.
34. Strashimir G. Popvassilev, On the number of in-
scribed squares of a simple closed curve in the plane,
http://arxiv.org/abs/0810.4806, 2008.
35. Feliú Sagols and Raúl Marín, The inscribed square
conjecture in the digital plane, Combinatorial Image
Analysis, Lecture Notes in Comput. Sci., vol. 5852,
Springer, 2009, pp. 411–424.
36. , Two discrete versions of the inscribed square
conjecture and some related problems, Theoret.
Comput. Sci. 412 (2011), no. 15, 1301–1312.
 37. Lev G. Schnirelman, On some geometric proper-
ties of closed curves (in Russian), Usp. Mat. Nauk
10 (1944), 34–44. Available at http://ega-math.
narod.ru/Nquant/Square.djv. Posthumous repro-
duction and extension of the author’s original article
in Sbornik Rabot Matematiˇceskogo Razdela Sekcii
Estestvennyh i Toˇcnyh Nauk Komakademii, Moscow,
1929.
38. Walter R. Stromquist, Inscribed squares and square-
like quadrilaterals in closed curves, Mathematika 36
(1989), 187–197.
39. Otto Toeplitz, Ueber einige Aufgaben der Analysis
situs, Verhandlungen der Schweizerischen Natur-
forschenden Gesellschaft in Solothurn 4 (1911),
197.
40. Siniša Vre´cica and Rade T. Živaljevi´c, Fulton–
MacPherson compactiﬁcation, cyclohedra, and the
polygonal pegs problem, Israel J. Math. 184 (2011),
no. 1, 221–249.
41. Ying-Qing Wu, Inscribing smooth knots with regular
polygons, Bull. London Math. Soc. 36 (2004), no. 2, 176–
180.
42. Joseph Zaks, The chair theorem, Proceedings of the
Second Louisiana Conference on Combinatorics, Graph
Theory and Computing (Baton Rouge, La.), Louisiana
State Univ., 1971, pp. 557–562.
43. Konrad Zindler, Über konvexe Gebilde, Monatshefte
für Mathematik und Physik 31 (1921), 25–56.

352 Notices of the AMS Volume 61, Number 4
