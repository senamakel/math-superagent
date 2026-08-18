<!-- source: https://arxiv.org/pdf/0804.0657 | converted from PDF -->

arXiv:0804.0657v1  [math.MG]  4 Apr 2008THE DISCRETE SQUARE PEG PROBLEM

IGOR PAK⋆

Abstract. The square peg problem asks whether every Jordan curve in the plane
has four points which form a square. The problem has been resolved (positively)
for various classes of curves, but remains open in full generality. We present two
new direct proofs for the case of piecewise linear curves.

Introduction

The square peg problem is beautiful and deceptively simple. It asks whether every
Jordan curve C ⊂ R2 has four points which form a square. We call such squares
inscribed into C (see Figure 1).

PSfrag replacements C

Figure 1. Jordan curve C and an inscribed square.

The problem goes back to Toeplitz (1911), and over almost a century has been
repeatedly rediscovered and investigated, but never completely resolved. By now it
has been established for convex curves and curves with various regularity conditions,
including the case of piecewise linear curves. While there are several simple and
elegant proofs of the convex case, the piecewise linear case is usually obtained as a
consequence of results proved by rather technical topological and analytic arguments.
In fact, until to this paper, there was no direct elementary proof. Here we present
two such proofs in the piecewise linear case.

Main Theorem. Every simple polygon on a plane has an inscribed square.

As the reader will see, both proofs are direct and elementary, although perhaps not
to the extend one would call them “book proofs”. The proofs are strongly motivated

Date: April 3, 2008.
⋆School of Mathematics, University of Minnesota, Minneapolis, MN, 55455. Email: pak@umn.edu.
1

2 IGOR PAK

by the classical ideas in the ﬁeld (see Section 3). Here and there, we omit a number of
minor straightforward details, in particular the deformation construction at the end
of the second proof.
The rest of the paper is structured as follows. In the next two sections we present
the proofs of the main theorem. These proofs are completely separate and can be read
independently. In the last section we give an outline of the rich history of the problem
and the underlying ideas. The historical part is not meant to be comprehensive, but
we do include a number of pointers to surveys and recent references.

1. Proof via inscribed triangles

Let X = [x1 . . . xn] ∈ R2 be a simple polygon. We assume that X is generic in a sense
which will be clear later on. Further, we assume that the angles of X are obtuse,
i.e. lie between π/2 and 3π/2. Fix a clockwise orientation on X.
For an ordered pair (y, z) of points y, z ∈ X denote by u and v the other two
vertices of a square [zyuv] in the plane, with vertices on X in this order, as shown
in Figure 2. Parameterize X by the length and think of (y, z) as a point on a torus
T = X × X. Denote by U ⊂ T the subset of pairs (y, z) so that u ∈ X. Similarly,
denote by V ⊂ T the subset of pairs (y, z) so that v ∈ X. Our goal is to show that U
intersects V .

PSfrag replacements
 yy z
z
 uu
 v

v XX
 X ′

Figure 2. Square [zyuv] inscribed into X and a rotation X ′ of X around y.

First, observe that for a generic X the set of points Uy = {z : (y, z) ∈ U} is ﬁnite.
Indeed, these points z ∈ Uy lie in the intersection of the polygon X and a polygon X ′

obtained by a counterclockwise rotation of X around y by an angle π/2 (see Figure 2).
Therefore, if X does not have orthogonal edges there is only a ﬁnite number of points
in X ∩ X ′. Moreover, when y moves along X at a constant speed, these intersection
points z change piecewise linearly, which implies that U is also piecewise linear.
Let us show that U is a disjoint union of simple polygons. Observe that when y is
moved along X the intersection point z ∈ X ∩ X ′ cannot disappear except when a
vertex of X passes through an edge of X ′, or when a vertex of X ′ passes through an
edge of X. This implies that when y is moved along X the intersection points emerge
and disappear in pairs, and thus U is a union of polygons. Note that for a generic X,
at no time can a vertex pass through a vertex, which is equivalent to the condition
that no square with a diagonal (xi, xj) can have a point y ∈ X as its third vertex.

THE DISCRETE SQUARE PEG PROBLEM 3

To see that the polygons in U are simple and disjoint, observe that the only way
we can have an intersection if a vertex of X ′ changes direction at an edge in X, or,
similarly, if a vertex of X changes direction at an edge in X ′. This is possible only
when y and either z or u are vertices of X. Since X is chosen to be generic we can
assume this does not happen, i.e. that X does not have an inscribed right isosceles
triangle with an edge (xi, xj).

PSfrag replacements X

XXX X ′X ′X ′

Figure 3. Two disappearing points in X ∩X ′ and a converging family
of right isosceles triangles inscribed into X with angles < π/2.

A similar argument also implies that on a torus T , the set U separates points
(y, z) ∈ T with the corresponding vertex u inside of X, from those where u is outside.
By continuity, it suﬃces to show that the point u crosses the edge of X as the generic
point (y, z) crosses U. Consider a point (y, z) ∈ U such that the corresponding third
vertex of a square u lies in the relative interior of an edge e in X. Now ﬁx y and
change z. Since X is generic, point u will pass through the edge e, which implies the
claim.
We need a few more observations on the structure of U. First, observe that U does
not intersect the diagonal ∆ = {(y, y), y ∈ X}. Indeed, otherwise we would have a
sequence of inscribed right triangles (y, z, u) converging to the same point, which is
impossible since X does not have angles between π/2 and 3π/2 (see Figure 3). In
a diﬀerent direction, observe that for a generic y the number of points in Uy is odd.
This follows from the previous argument and the fact the number of intersections
of X and X ′ as even except at a ﬁnite number of points y.
Now, from above we can conclude that at least one of the polygons in U is not null
homotopic on the torus T , since otherwise for a generic point y the size of Uy is even.
Fix one such polygon and denote it by U ◦. Since U ◦ is simple, not null homotopic
and does not intersect the diagonal ∆, we conclude that U ◦ is homotopic to ∆ on Y .
Therefore, there exist a continuous family of inscribed right isosceles triangles (uyz)
such that when y goes around X so do z and u. Relabeling triangles (uyz) with (yzv)
we obtain a simple polygon V ◦ ⊂ V which is also homotopic to ∆ on T .
Suppose now that U ◦ and V ◦ do not intersect. Together with ∆ these curves sepa-
rate the torus T into three regions: region A between ∆ and U ◦, region B between U ◦

and V ◦, and region C between V ◦ and ∆ (see Figure 4). Consider the pairs (y, z) in
the regions A and C which lie close to ∆ (i.e. y and z lie close to each other on X).
Clearly, for such (y, z), either both corresponding points u and v lie inside X or
both u and v lie outside of X. Let A be the former and let C be the latter regions.
From above, for all (y, z) ∈ B we have u /∈ X and v ∈ X. In other words, when y is
ﬁxed and z is moved along X counterclockwise starting at y, of the points u and v
the ﬁrst to move outside of X is always u.

4 IGOR PAKPSfrag replacements
 A
 A
B

B

C
 C
 V ◦

U U ◦
 TT

∆ ∆

Figure 4. Set U on a torus T and the sequence of regions A, B, C ⊂ T .

Now, consider the smallest right equilateral triangle R inscribed into X (the ex-
istence was shown earlier). There are two ways to label it as shown in Figure 5.
For the ﬁrst labeling, if y is ﬁxed and z is moved as above, the ﬁrst time point u
lies on X is when z and u are vertices of R. By assumptions on region A ⊂ T , the
corresponding point v lies inside X. Similarly, for the second labeling, if y is ﬁxed
and z is moved as above, the ﬁrst time point v lies on X is when z and v are vertices
of R. By assumptions on regions A ⊂ T , the corresponding point u lies outside of X,
a contradiction.1PSfrag replacements
 y

y zz
 uu
 v

v XXX

R

Figure 5. The smallest inscribed right isosceles triangle and its two labelings.

Finally, suppose X is not generic. We can perturb the vertices of X to obtain a
continuous family of generic polygons converging to X and use the limit argument.
Since X is simple, the converging squares do not disappear and converge to a desired
inscribed square. Similarly, when X has angles < π/2 or > 3π/2, use the limit
argument by cutting the corners as shown in Figure 6.

Figure 6. A converging family of obtuse polygons.

1The ﬁgure is somewhat misleading as it gives the impression that for all y and z with |yz| smaller
than that in R, we must have (y, z) ∈ A. In fact, we can have all these pairs in C and the same
argument will work when A is substituted with C and the inside/outside properties are switched
accordingly. The point is, by continuity, all close (y, z) with a ﬁxed order on X determined by R,
must lie in the same region (either A or C).

THE DISCRETE SQUARE PEG PROBLEM 5

2. Proof by deformation

In this section, we prove the following extension of the main theorem: every generic
simple polygon has an odd number of inscribed squares. Now that we have the
relation, we can try to prove that it is invariant under certain elementary transitions.

Theorem 2.1. Every generic simple polygon has an odd number of inscribed squares.2

The main theorem now follows by a straightforward limit argument. Note also
that the theorem is false for all simple polygons; for example every right triangle
has exactly two inscribed squares. We begin the proof with the following simple
statement.

Lemma 2.2. Let ℓ1, ℓ2, ℓ3 and ℓ4 be four lines in R2 in general position. Then there
exists a unique square A = [a1a2a3a4] such that xi ∈ ℓi and A is oriented clockwise.
Moreover, the map (ℓ1, ℓ2, ℓ3, ℓ4) → (a1, a2, a3, a4) is continuously diﬀerentiable, where
deﬁned.3

Proof. Fix z1 ∈ ℓ1. Rotate ℓ4 around z1 by π/2, and denote by ℓ′
4 the resulting
line, and by z2 = ℓ2 ∩ ℓ′
4 the intersection point. Except when ℓ2⊥ℓ4, such z2 is
unique. Denote by z4 ∈ ℓ4 the inverse rotation of z2 around z1. We obtain the right
isosceles triangle ∆ = (z2z1z4) oriented clockwise in the plane. The fourth vertex z3
of a square is uniquely determined. Start moving z1 along ℓ1 and observe that the
locus of z3 is a line, which we denote by ℓ′
3. Since line ℓ3 is in general position with
respect to ℓ′
3, these two line intersect at a unique point x3, i.e. determines uniquely
the square [a1a2a3a4] as in the theorem. The second part follows from immediately
from the above construction. □

Sketch of proof of Theorem 2.1. We begin with the following restatement of the sec-
ond part of the lemma. Let X = [x1 . . . xn] be a generic simple polygon and let
{Xt, t ∈ [0, 1]} be its continuous piecewise linear deformation. Suppose A = [a1a2a3a4]
is an inscribed square with vertices ai at diﬀerent edges of X, and none at the vertices
of X, i.e. ai ̸= xj. Then, for suﬃciently small t, there exists a continuous deformation
{At} of inscribed squares, i.e. squares At inscribed into Xt. Moreover, for suﬃciently
small t, the vertices ai of At move monotonically along the edges of Xt.
Consider what can happen to inscribed squares At as t increases. First, we may
have some non-generic polygon Xs, where such square in non-unique or undeﬁned.
Note that the latter case is impossible, since by compactness we can always deﬁne a
limiting square As. If the piecewise linear deformation {Xt} is chosen generically, it
is linear at time s, and we can extend the deformation of At beyond As.
The second obstacle is more delicate and occurs when the vertex ai of square As is
at a vertex xj of Xs. Clearly, we can no longer deform As beyond this point. Denote
by e1 the edge of X which contains vertices ai of At for t < s. Clearly, e1 = (xj−1, xj)

2It takes some eﬀort to clarify what we mean by a generic (see the proof). For now, the reader
can read this as saying that the n-gons, viewed as points in R2n, are almost surely generic.
3To make this precise, think of lines ℓi as points in RP2.

6 IGOR PAK

or e1 = (xj, xj+1). Denote by e
′
1 the other edge adjacent to v. Denote by e2, e3 and e4
the other three edges of X containing vertices of At (see Figure 7).

PSfrag replacements
 At As Br

xj e1

e′
1e2

e3 e4

Figure 7. Inscribed squares At, As = Bs and Br, where t < s < r.
Here e2, e3 and e4 are ﬁxed, while e1 and e
′
1 move away from the squares.

Now consider a family {Bt} of squares inscribed into lines spanned by edges e
′
1, e2, e3
and e4. By construction, As = Bs. There are two possibilities: either the correspond-
ing vertex bi approaches xj from inside e
′
1 or from the outside, when t → s and t < s.
In the former case, we conclude that the number of inscribed squares decreases by 2
as t passes through s. In the latter case, one square appears and one disappears, so
the parity of the number of squares remains the same. In summary, the parity of the
number of squares inscribed into Xt with vertices at diﬀerent edges is invariant under
the deformation.
It remains to show that one can always deform the polygon X in such a way that
at no point in the deformation do there exist inscribed squares with more than one
vertex at the same edge, and such that the resulting polygon has an odd number of
inscribed squares.
Fix a triangulation T of X. Find a triangle ∆ in T with two edges the edges of X
and one edge a diagonal in X. Subdivide the edges of X into small edges, so that
neither of the new vertices is a vertex of an inscribed square. If the edge length is now
small enough, we can guarantee that no square with two vertices at the same edge
is inscribed into X. Now move the edges along two sides of the triangle ∆ toward
the diagonal as shown in Figure 8. Repeat the procedure. At the end we obtain a
polygon Z with edges close to an interval. Observe that Z has a unique inscribed
square (see Figure 8). This ﬁnishes the proof. □

PSfrag replacements
 X
 Z
∆

Figure 8. The ﬁrst step of the polygon deformation which preserves
the parity of the number of inscribed squares; the ﬁnal polygon Z.

THE DISCRETE SQUARE PEG PROBLEM 7

3. The history, the proof ideas and the final remarks

3.1. The square peg problem of inscribed squares has a long and interesting history.
It seems, every few years someone new falls in love with it and works very hard to
obtain a new variation on the problem. Unfortunately, as the results become stronger,
the solutions become more technically involved and several of them start to include
some gaps, still awaiting careful scrutiny.4 Interestingly, the impression one gets from
the literature is that that no direct elementary proof is even possible in the piecewise
linear case, as the problem is diﬃcult indeed, the existing techniques are inherently
non-discrete and, presumably, other people have tried.

3.2. We begin with the celebrated incorrect proof by Ogilvy [FO]. While the proof
was refuted by several readers within a few months after its publication, it is still
worth going over this proof and try ﬁnd the gaps (there are three major ones, even
if one assumes that the curve is piecewise linear or analytic). As reported in [KW],
Ogilvy later became disillusioned in the possibility of a positive resolution of the
problem.

3.3. The ﬁrst major result was proved by Emch, who established the square peg
problem for convex curves [E1]. Later, Emch writes in [E2] that Toeplitz and his
students discovered the result independently two years earlier, in 1911, but never
published the proof. We refer to [Gr¨u, p. 84] for further references to proofs in
the convex case). Emch starts by constructing a family of inscribed rhombi with a
diagonal parallel to a given line. By rotating the line and using uniqueness of such
rhombi he concludes that one can continuously rotate a rhombus into itself with two
diagonals interchanged. Then the intermediate value theorem implies that at some
point the rhombus has equal diagonals, thus giving a square.
In the largely forgotten followup paper [H], Hebbert studies the squares inscribed
into quadrilaterals, essentially proving Lemma 2.2. He stops short of applying his
observations to general simple polygons. Let us mention also that in the second proof
we use the fact that every non-convex polygon can be triangulated. This is a standard
result also due to Emch [E2].

3.4. An important breakthrough was made by Shnirelman in 1929, when he oﬀered
a solution for curves with piecewise continuous curvature. This paper was published
in an obscure Russian publication, but later an expanded version [Shn] was published
posthumously. Guggenheimer in [Gug] studied this proof, added and correct several
technical points, and concluded that for Shnirelman’s proof to work the curve needs to
have a bounded variation. Shnirelman noted that for a generic curve the parity of the
number of inscribed squares must be invariant as the curve is deformed. The proof
uses a local lemma on existence of inscribed square for closed curves, a non-linear
version of Hebbert’s observation (and, most likely, completely independent). For the
connectivity of curves with continuous curvature and bounded variation Shnirelman

4While we did ﬁnd some such rather unconvincing arguments, we refrain from commenting on
them and leave them to the experts.

8 IGOR PAK

and Guggenheimer use known advanced results in the ﬁeld. Finally, the fact that
every ellipse with unequal axis has a unique inscribed square is straightforward.
Our proof in Section 2 is modeled on the deformation idea of Shnirelman (we
were unaware of Hebbert’s paper). In the piecewise linear case we no longer have the
analytic diﬃculties, but we do get the unpleasant obstacle of having inscribed squares
with more than two vertices on the same edge. In fact, if not for the smooth case,
there is no intuitive reason behind Theorem 2.1.
Interestingly, we believe we know where Shnirelman got the idea of his proof. At
the time of his ﬁrst publication, Shnirelman was working with Lyusternik on the
conjecture of Poincar´e which states that every smooth convex surface has at least
three closed geodesics. This conjecture was made in the foundational paper [P], where
Poincar´e proves that at least one such closed geodesics exists (on analytic surfaces),
and this proof uses a similar deformation and parity argument.

3.5. In 1961, Jerrard rediscovered the square peg problem and proved it for analytic
curves. He was apparently motivated by the Kakutani’s theorem that every convex
body has a circumscribed cube. This result itself followed a series of earlier similar
results (see e.g. [Str]) and was later extended by Dyson, Floyd, and others.
Jerrard’s proof was a model of our proof in Section 1. He similarly considers a
curve U on a torus T , corresponding to inscribed right isosceles triangles. He then
uses a parity argument to conclude that U is not null homotopic, and a separate
argument to conclude that when moving along U the fourth vertex cannot stay on
the same side of the polygon. Our approach has several advantages due to the fact
that we can make them generic and thus avoid squares which have to be double
counted. Also, we use a straightforward ad hoc argument with the minimal inscribed
triangle, diﬀerent from that by Jerrard. Overall, most details are still diﬀerent due
to the diﬀerent nature of intersections of analytic and piecewise linear curves.

3.6. In recent years, further results on the square peg problem have appeared, most
notably [St] and [Gri], which both weakened the restrictions on the curves and ex-
tended the reach of the theorem (to certain space quadrilaterals in [St] and to rect-
angles in [Gri]). In fact, there is a long history of variations on the problem, which
goes back to [Kak]. Let us mention some of them.
First, there are several results on inscribed triangles and rhombi and rectangles
in general Jordan curves [Ni1, NW]. We refer to [Ni2] for the survey and further
references. Second, there are several results on cyclic quadrilaterals inscribed into
suﬃciently smooth curves [Ma1, Ma2, Ma3]. Note that in the piecewise linear case,
unless a quadrilateral Q ⊂ R2 is an isosceles trapezoid, one can always take a suﬃ-
ciently slim triangle X, such that no polygon similar to Q is inscribed into X. The
corresponding “isosceles trapezoid peg problem” is open for general piecewise linear
curves. We believe that our proof by deformation might be amenable to prove this
result, but not without a major change.
In a diﬀerent direction, an interesting “table theorem” in [Fenn] says that every
suﬃciently nice function f on a convex set U ⊂ R2 has an an inscribed square of given
size, deﬁned as four points in U which are vertices of a square and have equal value

THE DISCRETE SQUARE PEG PROBLEM 9

of f . If the graph of f is viewed as a two-dimensional hill, the inscribed square can be
interpreted as feet of a square table, thus the name. Note that when the curve C (in
the square peg problem) is a starred region, applying the table theorem to the cone
over C gives the desired square inscribed into C. We refer to [KK, Me1, Me2, Me3]
for more on the table theorem and other related results.
Finally, there is a large number of results extending the square peg problem to
higher dimensions, including curves (see e.g. [Wu]) and surfaces (see e.g. [HLM, Kra]).
These results are too numerous to be listed here. We refer to surveys [CFG, Sec-
tion B2] and [KW, Problem 11] for further references.

3.7. In conclusion, let us mention that although stated diﬀerently, the results for
many classes of curves are essentially equivalent. We already saw this phenomenon
in both proofs, where we applied what we called the limit argument. In each case,
we obtained one polygon as the limit of others and noted that the sizes of inscribed
squares do not converge to zero. Of course, this approach fails in general, e.g. a
rectiﬁable curve can be obtained as the limit of piecewise linear curves, but a priori
the inscribes squares can collapse into a point.
Nonetheless, one can use the limit argument in may cases that appear in the lit-
erature. It is easy to derive the square peg problem for analytic curves from that
of piecewise linear curves. Similarly, the piecewise linear curves can be obtained a a
limit of analytic curves and derive our main theorem from Jerrard’s paper. It would
be interesting to see how far the limit arguments take use from the piecewise linear
curves.

Acknowledgements. We are very grateful to Raman Sanyal for listening to the
ﬁrst several versions of these proofs, and to Ezra Miller for the encouragement. Spe-
cial thanks to Elizabeth Denne for the interesting discussions and several helpful
references. The author was partially supported by the NSF grant.

10 IGOR PAK

References

[CFG] H. T. Croft, K. J. Falconer and R. K. Guy, Unsolved problems in geometry, Springer, New
York, 1991.
[E1] A. Emch, Some properties of closed convex curves in a plane, Amer. J. Math. 35 (1913),
407–412.
[E2] A. Emch, On the Medians of a Closed Convex Polygon, Amer. J. Math. 37 (1915), 19–28.
[Fenn] R. Fenn, The table theorem, Bull. London Math. Soc. textbf2 (1970), 73–76.
[FO] O. Frink and C. S. Ogilvy, Advanced Problems and Solutions: 4325, Amer. Math. Monthly 57
(1950), no. 6, 423–424; See also 58 (1951), no. 2, 113–114.
[Gri] H. B. Griﬃths, The topology of square pegs in round holes, Proc. London Math. Soc. 62
(1991), 647–672.
[Gr¨u] B. Gr¨unbaum, Arrangements and spreads, AMS, Providence, RI, 1972.
[Gug] H. Guggenheimer, Finite sets on curves and surfaces, Israel J. Math. 3 (1965), 104–112.
[HLM] H. Hadwiger, D. G. Larman and P. Mani, Hyperrhombs inscribed to convex bodies, J.
Combin. Theory Ser. B 24 (1978), 290–293.
[H] C. M. Hebbert, The inscribed and circumscribed squares of a quadrilateral and their signif-
icance in kinematic geometry, Ann. of Math. 16 (1914/15), 38–42.
[Jer] R. P. Jerrard, Inscribed squares in plane curves, Trans. AMS 98 (1961), 234–241.
[Kak] S. Kakeya, On the inscribed rectangles of a closed curvex curve, Tˆohoku Math. J. 9 (1916),
163–166.
[KW] V. L. Klee and S. Wagon, Old and new unsolved problems in plane geometry and number
theory, MAA, Washington, DC, 1991.
[Kra] H. Kramer, Hyperparallelograms inscribed to convex bodies, Mathematica (Cluj) 22 (1980),
67–70.
[KK] E. H. and P. B. Kronheimer, The tripos problem, J. London Math. Soc. 24 (1981), 182–192.
[Ma1] V. V. Makeev, On quadrangles inscribed in a closed curve, Math. Notes 57 (1995), 91–93.
[Ma2] V. V. Makeev, On two unsolved geometric problems, J. Math. Sci. 119 (2004), 245–248.
[Ma3] V. V. Makeev, On quadrangles inscribed in a closed curve and the vertices of a curve,
J. Math. Sci. 131 (2005), 5395–5400.
[Me1] M. D. Meyerson, Convexity and the table theorem, Paciﬁc J. Math. 97 (1981), 167–169;
available at http://tinyurl.com/2jsj3l
[Me2] M. D. Meyerson, Balancing acts, Topology Proc. 6 (1981), 59–75.
[Me3] M. D. Meyerson, Remarks on Fenn’s “the table theorem” and Zaks’ “the chair theorem”,
Paciﬁc J. Math. 110 (1984), 167–169; available at http://tinyurl.com/2vv2ce
[Ni1] M. J. Nielsen, Rhombi inscribed in simple closed curves, Geom. Dedicata 54 (1995), 245–254.
[Ni2] M. J. Nielsen, Figures Inscribed in Curves, website http://tinyurl.com/2mwt6y
[NW] M. J. Nielsen and S. E. Wright, Rectangles inscribed in symmetric continua, Geom. Dedi-
cata 56 (1995), 285–297.
[P] H. Poincar´e, Sur les lignes g´eod´esiques des surfaces convexes, Trans. AMS 6 (1905), 237–274.
[Shn] L. G. Shnirelman, On certain geometrical properties of closed curves (in Russian), Uspehi
Matem. Nauk 10 (1944), 34–44; available at http://tinyurl.com/28gsy3
[St] W. Stromquist, Inscribed squares and square-like quadrilaterals in closed curves, Mathe-
matika 36 (1989), 187–197.
[Str] D. J. Struik, Diﬀerential geometry in the large, Bull. AMS 37 (1931), 49–62; available at
http://tinyurl.com/2p3zb4
[Wu] Y.-Q. Wu, Inscribing smooth knots with regular polygons, Bull. LMS 36 (2004), 176–180;
arXiv: math.GT/0610867.
