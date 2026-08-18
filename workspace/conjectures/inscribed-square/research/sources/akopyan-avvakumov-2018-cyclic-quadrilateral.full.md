<!-- source: https://arxiv.org/pdf/1712.10205 | converted from PDF -->

ANY CYCLIC QUADRILATERAL CAN BE INSCRIBED
IN ANY CLOSED CONVEX SMOOTH CURVE

ARSENIY AKOPYAN AND SERGEY AVVAKUMOV

Abstract. We prove that any cyclic quadrilateral can be inscribed in any closed convex C 1-curve.
The smoothness condition is not required if the quadrilateral is a rectangle.

1. Introduction

To inscribe a quadrilateral Q in a Jordan curve is to ﬁnd a non-degenerate scaling, rotation,
and translation which maps all of the vertices of Q to the curve.
Which quadrilaterals can be inscribed in any closed convex curve? Obviously, the quadrilateral
must be cyclic, that is inscribed in a circle. Such quadrilaterals are characterized by a remarkable
property that the sum of their opposite angles is π. It turns out that for C 1-curves this condition
is also suﬃcient.1

Theorem 1. Any cyclic quadrilateral can be inscribed in any closed convex C 1-curve.

The C 1-smoothness requirement is necessary in Theorem 1. For example, the kite with angles
π/2 and 2π/3 cannot be inscribed in the thin triangle with angles π/10, π/10, 4π/5 (Figure 1).
However, if Q is a rectangle the smoothness condition can be relaxed.

Theorem 2. Any rectangle can be inscribed in any closed convex curve.

Fig. 1.
In [8] V. Makeev conjectured that any cyclic quadrilateral can be inscribed in any Jordan curve.
He proved the conjecture for the case of star-shaped C 2-curves intersecting any circle at no more
than 4 points. Theorem 1 proves it for convex C 1-curves. The example above shows that the
conjecture fails without the smoothness assumption. This example can be generalized to any
cyclic quadrilateral except for trapezoids. So, I. Pak [14] conjectured that Makeev’s conjecture
still holds for cyclic trapezoids even without the smoothness assumption.
Makeev’s conjecture is a part of a substantial topic originating from the famous question in
geometry known as the Square Peg problem or Toeplitz’ conjecture: Does every Jordan curve
contain all the vertices of a square? In its general form the Square Peg problem is still open. In
the last hundred years it was positively solved, however, for a wide variety of classes of curves.
For instance, for convex curves and later for piecewise analytic curves by A. Emch [1, 2], for
C 2-curves by L. Schnirelman [17], for locally monotone curves by W. Stromquist [15], for curves
without special trapezoids, for curves inscribed in a certain annulus, and for centrally symmetric
curves [13]. There were also high-dimension extensions of these results [4, 5, 9, 6]. For more
details we refer the reader to the survey [11] by B. Matschke.
Similar to the Square Peg problem, there exists the Rectangular Peg conjecture stating that
every Jordan curve contains the vertices of a rectangle with the prescribed aspect ratio. A

1The results of this paper were independently obtained by B. Matschke, whose preprint [12] appeared just a
few days later. In addition it contains a stronger version of Theorem 2, which is proved not only for rectangles
but also for any cyclic trapezoids. 1arXiv:1712.10205v2  [math.MG]  4 Jun 2018
ANY CYCLIC QUADRILATERAL CAN BE INSCRIBED IN ANY CLOSED CONVEX SMOOTH CURVE 2

proof was claimed by H. Griﬃths [3], but an error was found later. For a discussion see [11,
Conjecture 8]. The speciﬁc case of aspect ratio √3 and “close to convex” curves was solved
B. Matschke [10]. Theorem 2 proves the Rectangular Peg conjecture for the case of convex
curves.
It is noteworthy that all of the proofs mentioned above use the topological obstruction theory.
Unfortunately, this approach fails in the more general cases. The proof of Theorem 1 and 2
is based on a “non-topological” observation ﬁrst made by R. Karasev, [7]. It allowed him, in
particular, to prove the inﬁnitesimal version of Theorem 1. R. Karasev noticed and proved that
during the rotation of any three out of four vertices of a quadrilateral Q along a curve γ the fourth
vertex travels along a path bounding the same signed area as the original curve γ. A similar idea
was recently independently discovered by T. Tao who used it to prove the Toeplitz’ conjecture
for new types of curves [16].

2. The case of strictly convex C ∞-curves.

In this section we prove the following theorem.

Theorem 3. Let Q be a cyclic quadrilateral and let γ be a closed strictly convex C ∞-curve. Then
for any ε > 0 there is a cyclic quadrilateral Qε which is ε-close to Q and can be inscribed in γ.

The proofs of Theorems 1 and 2 are obtained from Theorem 3 by “going to the limit” type
argument in the next section.
Until the end of the section let us ﬁx a closed strictly convex C ∞-curve γ.
For a quadrilateral Q its drawing is the image of Q under some non-degenerate scaling, rotation,
and translation. If the angle of the rotation is α we also call it an α-drawing.

Lemma 4. Pick a vertex of a quadrilateral Q. For any angle α there is a unique α-drawing of Q
with all of the remaining 3 vertices being on γ.

Proof. The existence of a drawing follows by a simple continuity argument similar to the argument
in the proof of the following Lemma 6. The drawing is unique because the vertices of two distinct
homothetic triangles cannot lie on a strictly convex curve. □

For a vertex d of a quadrilateral Q denote by d(α) the position of d in the α-drawing of Q with
the remaining 3 vertices being on γ.

Lemma 5. Let Q be a cyclic quadrilateral. Then for any ε > 0 there is a cyclic quadrilateral Qε
which is ε-close to Q and such that d(α) is a closed C ∞-curve for any vertex d of Qε.

Proof. Let U be the space of ordered triples of pairwise distinct points of γ. Consider the map
f : U → S1 × S1 which sends a triple (x, y, z) to the pair of angles (∠xyz, ∠yzx). Clearly, f
is C ∞.
Let abcd be the vertices of Q in the counterclockwise order. Then the curve d(α) corresponds
to the f -preimage of the pair of angles (∠abc, ∠bca). By Sard’s lemma the set of the critical
values of f has Lebesgue measure 0, i.e., the set of cyclic quadrilaterals Q such that d(α) is not a
C ∞-curve also has Lebesgue measure 0. Applying this argument to every vertex of Q we get the
statement of the lemma. □

Lemma 6. Let Q be a cyclic quadrilateral. Then there is a vertex d of Q such that the angle at d
is non-acute and d(α) contains a point either on γ or in the exterior of γ.

Proof. Let abcd be the vertices of Q in the counterclockwise order.
There are two adjacent vertices of Q with non-acute angles because Q is cyclic. Without the
loss of generality let us assume that the angles at c and d are non-acute. We may also assume
that γ is tangent to the lines y = 0 and y = 1.

ANY CYCLIC QUADRILATERAL CAN BE INSCRIBED IN ANY CLOSED CONVEX SMOOTH CURVE 3

For t ∈ (0, 1) denote by at and bt the leftmost and the rightmost, respectively, of the two
intersections of γ with y = t. Denote by ct and dt the points such that atbtctdt is a drawing of Q.
Note that ct and dt are above the line y = t, see Figure 2.
Consider the case when t is very close to 1. Then ∠dtatbt is greater than the angle between
atbt and the tangent to γ at at. Which places dt is in the exterior of γ. Likewise, ct is also in the
exterior of γ.
Consider now the opposite case of t being very close to 0. Then ∠dtatbt is less than the angle
between atbt and the tangent to γ at at. Also, the segment atdt is “short”, i.e., much shorter than
the intersection of the interior of γ with the line parallel to atdt and going through the common
point of γ and y = 0. Which means that dt is in the interior of γ. Likewise, ct is also in the
interior of γ.
Let us now continuously decrease t from 1 to 0. At some moment one of the vertices d or c is
going to intersect γ while another one is still in the exterior of γ, or on γ. Without the loss of
generality we may assume that the latter vertex is d. Then d(α) contains a point either on γ or
in the exterior of γ. □

y = 0

y = 1

ba
 cd
 ba
 cd
 Fig. 2.
 a

b
 c
 d
 d(α)

Fig. 3.

Proof of Theorem 3. Choose a cyclic quadrilateral Qε as in the statement of Lemma 5.
By Lemma 6, there is a vertex d of Qε with a non-acute angle and such that d(α) contains a
point either on γ or in the exterior of γ.
If d(α) intersects γ then we are done, so we may assume that d(α) and γ are disjoint.
By the Jordan curve theorem, d(α) lies in the exterior of γ. On the other hand, γ lies in the
interior of d(α). Indeed, as we revolve once along d(α), the diagonal bd of the corresponding
α-drawing of Qε must also complete a 2π rotation. This would be impossible if the interiors of γ
and d(α) were disjoint.
By the following lemma, the curve d(α) has no self-intersections in the exterior of γ, i.e., no
self-intersections at all.

Lemma 7. Let abcd and a′b′c′d be two distinct drawings of the same cyclic quadrilateral with a
non-acute ∠d. Suppose that d is outside of the convex hull of the points a,b,c,a′,b′,and c′. Then
six points a, b, c and a′, b′, c′ cannot be in strictly convex position.

It is left to note that the area of d(α) must then be greater than the area of γ which contradicts
to the following lemma proven in [7].

Lemma 8. Let Q be a cyclic quadrilateral and let d(α) be a C ∞-curve for some vertex d of Q.
Then the area of d(α) is equal to the area of γ.
 □

3. Proofs of Theorem 1 and Theorem 2.

Proof of Theorem 1. Let γ be a closed convex C 1-curve and let Q be a cyclic quadrilateral. Choose
a sequence γi of closed strictly convex C ∞-curves converging to γ pointwise. By Theorem 3, there

ANY CYCLIC QUADRILATERAL CAN BE INSCRIBED IN ANY CLOSED CONVEX SMOOTH CURVE 4

is a sequence Qi of cyclic quadrilaterals converging to Q and such that Qi can be inscribed in γi
for each i.
Let ai, bi, ci, di ∈ γi be the vertices of Qi in the counterclockwise order. By passing to the
subsequences, we may assume that the sequences ai, bi, ci, and di have limits, a, b, c, and d,
respectively.
The quadrilateral abcd is inscribed in γ and is obtained from Q by a composition of scaling,
rotation, and translation. It remains to prove that the scaling is non-degenerate.
Assume to the contrary that a = b = c = d. Then both aibi and bici converge to the tangent
to γ at a = b = c = d. I.e., ∠aibici converges to either 0 or π. On the other hand, ∠aibici must
converge to the corresponding angle of Q. Angles of Q are neither 0 nor π, which leads to a
contradiction. □

Proof of Theorem 2. Let γ be a closed convex curve and let Q be a rectangle. Let γi, Qi, ai, bi,
ci, di, a, b, c, and d be as in the proof of Theorem 1.
Again, it remains to prove that the rectangle abcd is non-degenerate. Assume to the contrary,
that a = b = c = d.
The vertices of Qi divide γi into 4 arcs which we denote in the counterclockwise order by Ai,
Bi, Ci, and Di, see Figure 4. The lengths of 3 out of 4 arcs converge to 0. Without the loss of
generality we assume that the lengths l(Ai) and l(Ci) of Ai and Ci, respectively, converge to 0.
Denote by LAi and LCi the tangents to Ai and Ci parallel to aibi, see Figure 4. The distance
between LAi and LCi is less than l(Ai) + l(Ci) + |bici|, i.e., it converges to 0. Which contradicts
to the fact that the curve γi lies between LAi and LCi for each i. □

LAi

LCi

ai bi

cidi
 Ai
 Bi

CiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCiCi

Di
 Fig. 4.

4. Proof of Lemma 7

Assume to the contrary of the statement of the lemma that the points a, b, c, a′, b′, and c′ lie
in strictly convex position.
Draw the lines containing the sides of the triangle abc, and denote the angular regions of the
plane formed by them as shown in Figure 5. At ﬁrst, let us note that the point a′ cannot belong
to the region Ca, because in that case a is covered by the triangle a′bc. Analogously, the points
b′ and c′ cannot belong to the regions Cb and Cc, respectively.
Denote by Ω the circumcircle of abcd and let ℓ be the tangent line to Ω at a. Together with the
lines ab and ac the line ℓ forms two additional angular regions denoted by C ′
b and C ′
c, respectively,
see Figure 5.
It is easy to see that the composition of a homothety and a rotation around d which sends a to
b and a′ to b′ also sends C ′
b to Cb. So, if a′ lies in C ′
b then b′ lies in Cb, which we already showed
to be impossible. Therefore a′ cannot lie in C ′
b. Analogously, a′ cannot lie in C ′
c.
We proved that a′ cannot lie in the union of Ca, C ′
b, and C ′
c, which means that a
′ and d lie on
the same side of the line ab. Similarly, a and d lie on the same side of the line a′b′. From the
latter fact we conclude that a′ lies in the exterior of the circle ω passing through d and tangent to
ab at a (Figure 6). To see this the reader might consider that a′b′ passes through a iﬀ a′ belongs
to ω.

ANY CYCLIC QUADRILATERAL CAN BE INSCRIBED IN ANY CLOSED CONVEX SMOOTH CURVE 5

We know that d lies outside of the convex hull of a, b, c, a′, b′, and c′ and that ∠cda =
∠c′da′ ≥ π/2, so ∠ada′ < π/2. Thus, without the loss of generality we may assume that the
counterclockwise rotation sending da to da
′ is at most π/2. Therefore, a′ lies in the angular
region formed by ∠cda.
This region is covered by the four grey zones in Figures 5, 6, 7, 8. Let us give a verbal description
of the zones and prove that a
′ cannot lie in them. This will conclude the proof of the lemma.

d a

b

ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
 ℓ

Ca

C ′
b

C ′
c

Cb

Cc
 Ω
 Fig. 5.
 d a

b

c
 a
′

b
′

c
′
 ω
 Ω

Fig. 6.

• The grey zone in Figure 5 is the halfplane bounded by ab and not containing d.
• The grey zone in Figure 6 is the interior of ω.

We have already proved that a′ cannot lie in the grey zones in Figures 5 and 6.

• The grey zone in Figure 7 is the intersection of the halfplane bounded by ab and containing
d, the exterior of ω, and the interior of Ω. Suppose that a′ is in that grey zone.
Denote by x the point of intersection of the line ab with the circle going through a,
a′, and d. Point x is inside of the segment ab. From the angular property of an iscribed
quadrilateral it follows that b′, a′, and x lie on the same line. So, the intersection point x
of ab and a′b′ lie inside of the segment ab and outside of the segment a′b′ which contradicts
to the convex position of a, b, a′, and b′.
• The grey zone in Figure 8 is the intersection of the halfplane bounded by ℓ and containing
c, the halfplane bounded by ac and not containing d, and the exterior of Ω. Suppose that
a′ is in that grey zone.
Denote by y the point of intersection of the line ac with the circle going through a, a′,
and d. Point y is outside of the segment ac. From the angular property of an iscribed
quadrilateral it follows that c′, a′, and y lie on the same line. So, the intersection point y
of ac and a′c′ lie outside of the segment ac and inside of the segment a′c′ which contradicts
to the convex position of a, c, a′, and c′.

Remark 9. Lemma 7 does not hold if the quadrilateral is not assumed to be cyclic (Figure 9) or
if the angle at d is allowed to be acute (Figure 10).

Acknowledgments. The ﬁrst author is supported by the European Research Council (ERC)
under the European Union’s Horizon 2020 research and innovation programme (grant agreement
No 716117).
The authors are grateful to Roman Karasev for useful discussions and ideas.

ANY CYCLIC QUADRILATERAL CAN BE INSCRIBED IN ANY CLOSED CONVEX SMOOTH CURVE 6

d a

b

a
′
b
′
 x

Ω
 ω

Fig. 7.
 d a

c a
′c
′ y
 Ω
 ℓ

Fig. 8.

Fig. 9. Fig. 10.

References

[1] A. Emch. Some Properties of Closed Convex Curves in a Plane. Amer. J. Math., 35(4):407–412, 1913.
[2] A. Emch. On Some Properties of the Medians of Closed Continuous Curves Formed by Analytic Arcs. Amer.
J. Math., 38(1):6–18, 1916.
[3] H. B. Griﬃths. The topology of square pegs in round holes. Proc. London Math. Soc. (3), 62(3):647–672,
1991.
[4] M. L. Gromov. Simplexes inscribed on a hypersurface. Mat. Zametki, 5:81–89, 1969.
[5] T. Hausel, E. Makai, and A. Sz˝ucs. Inscribing cubes and covering by rhombic dodecahedra via equivariant
topology. Mathematika, 47(1-2):371–397, 2000.
[6] R. N. Karasev. Inscribing a regular crosspolytope. arXiv preprint arXiv:0905.2671, 2009.
[7] R. N. Karasev. A note on Makeev’s conjectures. Journal of Mathematical Sciences, 212(5):521–526, Feb 2016.
[8] V. V. Makeev. Quadrangles inscribed in a closed curve. Mathematical Notes, 57(1):91–93, Jan 1995.
[9] V. V. Makeev. Universally inscribed and outscribed polytopes. Doctor of mathematics thesis. Saint-Petersburg
State University, 2003.
[10] B. Matschke. Equivariant topology methods in discrete geometry. PhD thesis, Freie Universit¨at Berlin, 2011.
[11] B. Matschke. A survey on the square peg problem. Notices of the American Mathematical Society, 61(4):346–
352, apr 2014.
[12] B. Matschke. Quadrilaterals inscribed in convex curves. arXiv preprint arXiv:1801.01945, 2018.
[13] M. J. Nielsen and S. E. Wright. Rectangles inscribed in symmetric continua. Geom. Dedicata, 56(3):285–297,
1995.
[14] I. Pak. The discrete square peg problem. arXiv preprint arXiv:0804.0657, 2008.
[15] W. Stromquist. Inscribed squares and square-like quadrilaterals in closed curves. Mathematika, 36(2):187–197
(1990), 1989.
[16] T. Tao. An integration approach to the toeplitz square peg problem. Forum of Mathematics, Sigma, 5, 2017.
[17] L. G. ˇSnirel’man. On certain geometrical properties of closed curves. Uspehi Matem. Nauk, 10:34–44, 1944.

Arseniy Akopyan
E-mail address: akopjan@gmail.com

Sergey Avvakumov
E-mail address: s.avvakumov@gmail.com

Institute of Science and Technology Austria (IST Austria), Am Campus 1, 3400 Klosterneuburg,
Austria
