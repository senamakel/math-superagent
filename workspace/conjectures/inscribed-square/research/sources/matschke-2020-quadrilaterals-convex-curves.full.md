<!-- source: https://arxiv.org/pdf/1801.01945 | converted from PDF -->

Quadrilaterals inscribed in convex curves

Benjamin Matschke

Boston University

matschke@bu.edu

December 3, 2020

Abstract

We classify the set of quadrilaterals that can be inscribed in convex Jordan curves, in the
continuous as well as in the smooth case.
1 This answers a question of Makeev in the special case
of convex curves. The diﬃculty of this problem comes from the fact that standard topological
arguments to prove the existence of solutions do not apply here due to the lack of suﬃcient
symmetry. Instead, the proof makes use of an area argument of Karasev and Tao, which we
furthermore simplify and elaborate on. The continuous case requires an additional analysis of the
singular points, and a small miracle, which then extends to show that the problems of inscribing
isosceles trapezoids in smooth curves and in piecewise C 1 curves are equivalent.

1 Introduction

A Jordan curve is a simple closed curve in the plane, i.e. an injective continuous map γ : S1 → R 2.
In 1911, Toeplitz [36] announced to have proved that any convex Jordan curve contains the four
vertices of a square – a so-called inscribed square – and he asked whether the same property holds
for arbitrary Jordan curves. This became the famous Inscribed Square Problem, also known as the
Square Peg Problem or as Toeplitz’ Conjecture. So far it has been answered in the aﬃrmative only in
special cases [7, 13, 8, 9, 39, 33, 3, 15, 34, 27, 19, 37, 28, 31, 32, 2, 21, 22, 29, 14, 35].
More generally, we say that a Jordan curve γ inscribes a quadrilateral Q if there is an orientation-
preserving similarity transformation that sends all four vertices of Q into the image of γ. Thus Toeplitz
proved that convex Jordan curves inscribe squares.
It is natural to ask whether they inscribe more general quadrilaterals as well. This is methodology-
wise a highly interesting question for the following reason: Almost all approaches up to today (with
few exceptions, Tao [35]; and for more general circular quadrilaterals see also Karasev [17], and for
rectangles of aspect ratio √3 see [22]) prove the existence of inscribed squares via more or less directly
proving topologically that the number of inscribed squares is odd when counted with appropriate
multiplicities, and thus never zero. Any other quadrilateral turns out to be inscribed an even number
of times (or zero times when counted with appropriate signs) due to their smaller symmetry group,
and thus the topological approach does not extend to quadrilaterals that are not squares.
A circular quadrilateral is a quadrilateral that has a circumcircle. An isosceles trapezoid is a
trapezoid that has a circumcircle. Let Q , Q , Q , Q⃝ denote the sets of squares, rectangles,
isosceles trapezoids and circular quadrilaterals, respectively. Clearly, Q ⊂ Q ⊂ Q ⊂ Q⃝.
If J is a class of Jordan curves and Q a set of quadrilaterals, we say that J inscribes Q if any
curve γ ∈ J inscribes each quadrilateral Q ∈ Q.

1The author was kindly notiﬁed by Arseniy Akopyan and Sergey Avvakumov about their recent article [1], which
has considerable overlap with the present one. As they had already submitted their preprint, it was too late to merge
them. Certainly, their results have full priority; in particular Theorem 1.5 appeared already in their work as well as (as
a corollary) the ﬁrst part of Theorem 1.4 in the special case of rectangles.

1arXiv:1801.01945v3  [math.MG]  1 Dec 2020
Let J k denote k-times continuously diﬀerentiable Jordan curves that are regular if k ≥ 1. Ma-
keev [19] asked: Does J 0 inscribe Q⃝? One restricts to Q⃝ clearly because the only quadrilaterals
that are inscribable in circles are circular. Quite likely Makeev meant J 1 instead of J 0 (compare
with Makeev [20]), as it turns out that for example the only quadrilaterals that can be inscribed in
arbitrarily thin triangles are isosceles trapezoids, as observed by Pak [28, Ex. 5.16]. In any case one
arrives at two natural questions.

Question 1.1 (Continuous case). Does J 0 inscribe Q ?

Question 1.2 (Smooth case). Does J 1 inscribes Q⃝?

Makeev [19] managed to answer Question 1.2 in the aﬃrmative in the special case of star-shaped
C 2-curves that intersect every circle at most 4 times, see also Makeev [20] for a version of that. To
underline the diﬃculty of both questions, the author [23] had put e100 on the weaker problem of
whether or not J ∞ inscribes Q .

Remark 1.3 (Updates). This prize was recently earned by Greene and Lobb [11], and moreover
they just announced in [10] a positive answer for Question 1.2. Their proofs are based on symplectic
topology, in particular using the minimum Maslov number of Lagrangian tori in C 2 for the general case.
In combination with Theorem 5.2 this allows us to also provide partial positive answers to Questions 1.1
and 1.2 for the class J 1
pw of piecewise C 1 Jordan curves without cusps; see Corollaries 5.4 and 5.5.

In the current paper, we answer both questions in the aﬃrmative in the case of convex curves.

Theorem 1.4 (Continuous case). The class J 0
conv of (continuous) convex Jordan curves inscribes the
set Q of isosceles trapezoids. Moreover, Q is the largest possible such set of quadrilaterals.

Theorem 1.5 (Smooth case). The class J 1
conv of diﬀerentiable convex Jordan curves inscribes the set
Q⃝ of circular quadrilaterals. Moreover, Q⃝ is the largest possible such set of quadrilaterals.

A common generalization. The above two theorems state the inscribability of Q⃝ in J 1
conv, and
of Q in J 0
conv. Additionally we know that for each quadrilateral not in Q there is a curve in J 0

that does not inscribe it. Nonetheless, we may ask for natural suﬃcient criteria for when a circular
quadrilateral can be inscribed into a (continuous) convex Jordan curve. One positive answer is given
in the following Theorem 1.6.

Figure 1: Q and its angles. Figure 2: Example for Theorem 1.6.

Consider a circular quadrilateral Q. We may and do assume that it is convex and positively oriented
by relabeling its vertices in positively oriented fashion P1, P2, P3, P4. Both pairs of opposite edges
of Q determine signed angles λ = ∡(
−−−→
P1P2, −−−→
P4P3) and µ = ∡(−−−→
P4P1, −−−→
P3P2), with the convention that
λ, µ ∈ (−π, π), compare with Figure 1. Note that λ and µ are zero, respectively, if and only if the
corresponding pairs of opposite edges are parallel. And if α, β, ζ, and δ denote the inner angles of Q,
then λ = α + δ − π = π − β − ζ and µ = ζ + δ − π = π − α − β.

The following is a natural common extension of Theorems 1.4 and 1.5 for certain continuous convex
Jordan curves and circular quadrilaterals, see Figure 2.

2

Theorem 1.6 (Common generalization). Let Q be a circular quadrilateral with signed angles λ and
µ as above. Suppose γ is a (continuous) convex Jordan curve all whose inner angles have size larger
than min(|λ|, |µ|). Then γ inscribes Q.

The condition on the inner angles of γ is only non-trivial at singular points of γ, since |λ|, |µ| < π.
In particular the angle condition is empty if γ is C 1, and Theorem 1.5 follows as a corollary.
As another special case, notice that if Q is an isosceles trapezoid, then min(|λ|, |µ|) = 0, which
makes the angle condition again trivially fulﬁlled, and Theorem 1.4 follows as a second corollary.

Related questions. There is a beautiful zoo of related theorems and open problems. For example
the reader may wonder about inscribed triangles in continuous curves (there are many, see Nielsen [25]),
or about inscribed pentagons (generically not possible, as the degree of freedom is one less then the
number of equations). We refer to various accounts on the history of inscribing and circumscribing
problems, see Klee and Wagon [18, Problem 11], Nielsen [26], Denne [5], Karasev [16, 2.6, 4.6], Pak [28,
I.3, I.4], M. [23].

Basic ideas and outline. In the smooth case, we follow Karasev [17]. Given Q = P1P2P3P4, ﬁrst
one considers the set of inscribed triangles similar to P1P2P3. For generic curves γ, this set forms a
one-dimensional manifold that winds around γ exactly once, i.e. each of the three vertices circumscribe
the interior of γ once, see Section 2. Karasev’s area argument then yields that the traced fourth vertex
will circumscribe a region with the same signed area (see Corollary 3.8). We will argue that if γ does
not inscribe Q, then this trace can be assumed to lie in the exterior of γ, going around γ exactly once,
and being injective, which yields a contradiction to the area argument. The major new step here is to
prove the injectivity of the trace, which is done in Section 4.
In the continuous case, two new problems arise: Genericity of γ and the corresponding approxi-
mation argument are harder to establish, which is a technical problem. Furthermore, there is a new
conceptual diﬃculty, namely that the inscribed triangles may become degenerate in a natural way,
and at these singular points the traced fourth vertex may swap the sides of γ without giving rise
to a proper inscribed quadrilateral. In many similar situations one would need to give up or ﬁnd
another approach (e.g. Toeplitz’ inscribed square problem). In our setting it turns out that after a
more detailed analysis of these degenerate side changes in Section 5 we can actually use them to our
advantage. With inscribing problems it is often the case that the more complicated curves become,
the more objects are inscribed, but to prove the existence of just a single one of them becomes harder
(e.g. in the above two questions). In our setting it seems to be quite the opposite. We can even ﬁnd a
lower bound for the number of inscribed Q’s, which can be tight even if the number of inscribed Q’s
is large, see Theorem 5.1.
Furthermore, the latter analysis can be used to show that inscribing Q into J ∞ is equally diﬃcult
as inscribing them into the class J 1
pw of piecewise C 1 Jordan curves, see Section 5.3.

Notation. We say that two polygons P1P2 . . . Pn and Q1Q2 . . . Qn in R 2 are similar to each other if
there is an orientation-preserving similarity transformation σ (a composition of translations, rotations
and scalings) such Qi = σ(Pi) (i = 1, . . . , n).
Throughout the paper, ‘smooth’ means C ∞. We usually identify a parametrized curve γ : S1 → R 2

with its image γ(S1) in order to simplify terminology. We may and do assume that γ goes in the positive
sense around its interior. Saying that γ is C 1 or C ∞ for us also includes that γ needs to be regular.
We call a convex polygon P1P2 . . . Pn positively oriented if P1, . . . , Pn lie counter-clockwise around
the boundary of the polygon.
Circular quadrilaterals may be self-intersecting (or “skew”), in which case we can simply relabel
the vertices in counter-clockwise order around the boundary of their convex hull, which makes the
quadrilateral convex. Inscribing either of them are equivalent tasks. That is, it is enough to deal with
positively oriented (and thus convex) circular quadrilaterals only.

3

2 Inscribing the ﬁrst three points

Let us start with the easier smooth case. Let Q = P1P2P3P4 be a circular quadrilateral with inner
angles α, β, γ, δ. For the sake of this paper we may assume that it is convex and positively oriented.
Furthermore we can cyclically permute the vertex labels to assure that ζ and δ are at least π/2, as Q
is circular. This assumption will be crucial in Section 4.

Figure 3: The trace γ4 of the fourth vertex
for a curve γ (exact drawing). Note that this
exemplary curve is not convex.
 Figure 4: Projection of ZT ⊂ (S1)
3 to the ﬁrst
two coordinates for the curve from Figure 3
(exact drawing).

Suppose γ : S1 → R 2 is positively oriented C 1 convex Jordan curve. We may deform γ slightly
(with respect to the C 1-metric) such that it becomes strictly convex and smooth. If we can show that
we can inscribe Q into the deformed smooth strictly convex curve, the same follows for the original
γ by a limit argument, using γ is C 1: To any approximating smooth strictly convex curve we ﬁnd
an inscribed Q. Making the approximation better in better (in the C 1-metric) yields a sequence of
quadrilaterals, which by compactness has a convergent subsequence, whose limit cannot degenerate to
a point as γ is C 1.
To any triangle T = P1P2P3 we can consider the set ZT of all triangles T ′ inscribed in γ that are
similar to T , see Figure 4 for the (non-convex) curve in Figure 3. This set has been studied topologically
several times, also for more general polygons, see e.g. Meyerson [24], Wu [38], Makeev [20], and Vre´cica–
ˇZivaljevi´c [37].
We consider ZT as a subset of the conﬁguration space (S1)
3 \ ∆ (∆ always denotes a thin diagonal
in this paper) which parametrizes all inscribed triangles in γ. As ZT can be deﬁned via two equations,
it can be written as a preimage ZT = f −1(0) for some map f : (S1)3 → R 2. Hence generically we
expect that ZT is a one-dimensional proper submanifold. The genericity can be achieved in various
ways. We choose to deform γ slightly with respect to the C 1-metric using ‘local bumps’, keeping it
strictly convex, where the amplitude of each bump depends on its own bounded real parameter. Using
the transversality theorem (see e.g. Guillemin and Pollack [12, p. 68]) this makes γ generic for any
choice of amplitude vector outside a zero-set. This method has the technical advantage that we did
not deform the test-map, the curve itself becomes generic. By an approximation argument as above,
we thus may assume that γ is not only smooth and strictly convex but also generic.
We claim that in case γ is convex, ZT is topologically a circle; and even more is true: For each
angle α ∈ S1 = Z /2π there is exactly one triangle parametrized by ZT whose ﬁrst edge has angle
α with the x-axis. If there were more than one, these would be at least two inscribed triangles T1
and T2 that diﬀer by a translation and a dilatation. However then their six vertices cannot lie in
strictly convex position. That for each α a corresponding inscribed triangle exists can be easily seen
using an intermediate value theorem argument. Or one computes directly the homology class that ZT
represents, e.g. via a bordism argument deforming γ to a simpler curve such as a circle.
Now for each such inscribed triangle T ′ = P ′
1P ′
2P ′
3 we construct the fourth vertex P ′
4 that makes
P ′
1P ′
2P ′
3P ′
4 similar to the given Q. The trace of these points P ′
4 is itself a closed curve γ4 in the
plane, although not necessarily simple, compare with Figure 3 for a non-convex curve γ. Now, each

4

intersection point of γ4 with γ correspond to an inscribed quadrilateral P ′
1P ′
2P ′
3P ′
4 similar to the given Q.
So assume that γ4 ∩ γ = ∅. Then γ4 stays inside of γ or it stays outside. We can restrict to the latter
case by the following argument: If we move a horizontal line parallelly from the bottom of γ to the
top, and at each time we call the intersection points P ′′
1 and P ′′
2 , and if we construct corresponding
points P ′′
3 and P ′′
4 to make Q
′′ = P ′′
1 P ′′
2 P ′′
3 P ′′
4 similar to Q, then one of P ′′
3 or P ′′
4 will intersect γ at
last (if they do it simultaneously then we already are done with inscribing Q). If P ′′
3 comes last, then
at that time, T ′′ = P ′′
1 P ′′
2 P ′′
3 lies in ZT and has P ′′
4 outside of γ, which is the case we want to be in.
If P ′′
4 comes last, we simply relabel 1 ↔ 2, 3 ↔ 4, and reﬂect the plane and the orientation of γ in
order to arrive a positively oriented situation, and we arrived in the case, where the trace γ4 of P ′
4
stays outside of γ. The following lemma summarizes this.

Lemma 2.1. It is enough to prove Theorem 1.5 for generic smooth strictly convex Jordan curves γ,
and positively oriented circular quadrilaterals Q with δ ≥ π/2 and whose trace γ4 of P ′
4 lies outside
of γ.

For each T ′ ∈ ZT , consider the intersection of the line segment between P ′
2 and P ′
4 with γ. As γ is
convex, there is exactly one such intersection point X, except for P ′
2 itself, and it moves continuously
with T ′ ∈ ZT . We may consider this as a map P ′
4 ↦→ X. Along ZT , P ′
2 winds once around γ (possibly
not in a monotone way), so does X, and thus the trace γ4 of the fourth vertex P ′
4 winds exactly once
around γ as well.

3 On Karasev’s and Tao’s conserved integrals of motion

Karasev [17] proved that γ4 circumscribes a region of signed area equal to the area of the interior of γ.
Here, the signed area can be deﬁned as one of the three equivalent integrals from Remark 3.6. As a
corollary he obtained the following theorem.

Theorem 3.1 (Karasev). Any smooth Jordan curve γ either inscribes a given circular quadrilateral
Q = P1P2P3P4, or it inscribes two copies of the triangle P1P2P3 such that the two corresponding fourth
vertices coincide.

His arguments behind this theorem are indeed the main ingredient for our proof of Theorem 1.5.
Tao [35] used a similar area argument in order to prove a new special case of Toeplitz’ inscribed
square problem, where the standard topological approach fails.

Theorem 3.2 (Tao). Let f, g : [0, 1] → R 2 be two (1 − ε)-Lipschitz functions whose graphs only
intersect at x = 0, 1. Then the curve formed by the two graphs inscribes a square.

And indeed his proof immediately generalizes to inscribed isosceles trapezoids, although one needs
to assume a suitable smaller Lipschitz constant that depends on the angles of the trapezoid.
Whilst Karasev could use the fact that the four curves γ1, γ2, γ3, γ4 parametrizing the vertices of
the quadrilateral in motion are closed, in Tao’s situation they were not closed (at least in his application
the path started and ended at quadrilaterals that were degenerate to a point).
The two lemmas in this section simplify and extend Karasev’s and Tao’s conserved integrals of
motion. They work for arbitrary paths of circular quadrilaterals similar to the given one, which do
not need to end where they started. One hope is that the lemmas could be used in the future to help
ﬁnding a proof of Makeev’s conjecture that J 1 inscribes Q⃝, for example by cutting the given curve
into suitable pieces and applying the lemma to suitable 4-tuples of these pieces.

An aﬃne dependence of points P1, . . . , Pn in some R -vector space is a non-zero vector (λ1, . . . , λn) ∈
R n such that ∑

i λi ( Pi
1 ) = 0, where ( Pi
1 ) denotes the projectivization of Pi. Any four points in the
plane are aﬃnely dependent.
 5

Lemma 3.3 (Area argument, complex version). Suppose Q = P1P2P3P4 is a circular quadrilateral.
Let (λ1, . . . , λ4) be an aﬃne dependence of P1, . . . , P4. Let γ1, . . . , γ4 : [t0, t1] → C be four piecewise
C 1-curves such that for each t ∈ [t0, t1], the quadrilateral γ1(t)γ2(t)γ3(t)γ4(t) is similar to Q. Then

4∑

i=1 λi
 ∫ t1

t0 γi(t) dγi(t) = 0. (1)

Proof of Lemma 3.3. We proceed as in Karasev [17]. Let O be the midpoint of Q and pi = Pi−O ∈ C ×.
Let ρ(t) ∈ C × denote the rotation-dilatation that sends Q to a translate of γ1(t)γ2(t)γ3(t)γ4(t), and
let o(T ) denote the midpoint of γ1(t)γ2(t)γ3(t)γ4(t). Then clearly, γi(t) = o(t) + ρ(t)pi. Thus,

γi(t)dγi(t) = o(t)do(t) + piρ(t)do(t) + pio(t)dρ(t) + |pi|2ρ(t)dρ(t). (2)

If r denotes the circumradius of Q, then
∑

i λi = 0, ∑

i λipi = 0, ∑

i λipi = 0 = 0, ∑

i λi|pi|
2 = r2 · 0 = 0.

Thus, summing (2) over i = 1, . . . , 4 with coeﬃcients λi yields

4∑

i=1 λiγi(t) dγi(t) = 0. (3)

Integrating this 1-form over t ∈ [t0, t1] yields (1).

In light of (3), this seems to be in some sense the most natural formulation of the area argument.
The simplicity of the proof underlines that. One possible caveat is that this talks about complex
1-forms, so let us also discuss a version for real forms.
The 1-forms zd¯z and ydx on C = R 2 (with z = x + iy) are up to the factor 2i cohomologous (see
below). Therefore, Lemma 1 can be rewritten in terms of ydx as follows.

Lemma 3.4 (Area argument, real version). In the setting of Lemma 3.3, let ρt = (γ2(t) − γ1(t))/(P2 −
P1) ∈ C × be the rotation-dilatation that sends Q to a translated copy of γ1(t)γ2(t)γ3(t)γ4(t). Let q be

the quadratic form with matrix representation 1
4 ( 1 1
1 −1 )t (∑4
i=1 λiPiP t
i ) ( 1 1
1 −1 ). Then

4∑

i=1 λi
 ∫

γi y dx = q(ρt1) − q(ρt0). (4)

Remark 3.5. 1.) The ‘potential’ q in (4) is a quadratic form on R 2 of signature (+, −). Its two
eigenvalues have opposite sign as the trace of q is zero: To show this, we may translate Q to have
its center at the origin, which keeps q invariant. Let r be the radius of Q’s circumcircle. Then
Tr ∑
i λiPiP t
i = ∑
i λi|Pi|2 = r2 ∑
i λi = 0. As ( 1 1
1 −1 ) is √2 times an orthogonal matrix, the trace of
q is zero as well.
2.) Furthermore, the eigenvectors of q are exactly the directions vλ, vµ of the angular bisectors of λ
and µ. Perhaps this has an elementary proof, but the author chose the brute-force algebraic way: First
one may assume that vλ, vµ are the standard basis vectors. Then the coordinates of P1, . . . , P4 satisfy
a system of polynomial equations, giving rise to an ideal I. The statement about the eigenvectors of q
is equivalent to say that vλ, vµ are isotropic vectors with respect to the quadratic form ∑

i λiPiP t
i ,
which translates into a polynomial equation in the coordinates of P1, . . . , P4. This polynomial is shown
to lie in the ideal I using a Gr¨obner basis of I, which was computed using SageMath [6], which in turn
uses Singular [4] for that task.
3.) Up to a scalar factor, the previous two points 1.) and 2.) uniquely describe q geometrically.

6

Proof of Lemma 3.4. Writing z = x + iy, we can expand and then collect terms

zdz = xdx + ydy + iydx − ixdy = 2iydx + 1
2 d(x2 − 2ixy + y2), (5)

which shows that zdz and 2iydx diﬀer only by a coboundary. Summing up over all i with coeﬃcients
λi and on using (1) we obtain

4∑

i=1 λi
 ∫

γi y dx = i
4
 4∑

i=1 λi(|γi(t1)|2 − 2iγi(t1)xγi(t1)y − |γi(t0)|
2 + 2iγi(t0)xγi(t0)y).

Using ∑

i λi|γi(t)|
2 = 0 we can manipulate the right hand side further,

4∑

i=1 λi
 ∫

γi y dx = 1
4
 4∑

i=1 λi(⟨1 , γi(t1)⟩
2 − ⟨1 , γi(t0)⟩2), (6)

where 1 = ( 1
1 ). We substitute γi(t) = o(t) + ρ(t)pi and use the aﬃne dependence to get rid of the o(t)
summands and obtain ∑
i λi⟨1 , γi(t)⟩
2 = ∑

i λi⟨1 , ρ(t)pi⟩2 = ∑

i λi1 tM pip
t
iM t1 , where M = ( a −b
b a )

is the matrix representing the rotation-dilatation given by multiplication by ρ(t) = a + ib. In the latter
we can replace pi by Pi, as again via the aﬃne dependence we see that the sum does not change.
Finally we write M t1 = ( a+b
a−b ) = ( 1 1
1 −1 ) ρ(t). This turns (6) into the claimed (4).

Remark 3.6. If γ : [t0, t1] → C parametrizes a closed curve, then the signed area of the region
circumscribed by γ (counted with multiplicity) is given by Green’s integrals A = ∫
γ x dy = − ∫

γ y dx.

With this in mind, integrating (5) proves ∫ t1
t0 γ dγ = −2iA.

Remark 3.7. Taking as integrand γdγ instead of ydx has the advantage that the right hand side
of (1) is simply 0 instead of the non-vanishing right hand side of (4), coming from the potential q. On
the other hand, ydx may have the advantage to be easier accessible geometrically, as it is immediately
connected to areas.

Corollary 3.8. In the setting of Lemma 3.3, suppose that the γi are closed curves. If γ1, γ2 and γ3
circumscribe regions of signed area A, then so does γ4.

Proof. Let λ be an aﬃne dependence of P1, . . . , P4. Since any three vertices of a circular quadrilateral
are aﬃnely independent, λ has no zero component.
If we put Ai = − ∫
γi y dx, then either of Lemma 3.3 and Lemma 3.4 implies ∑

i λiAi = 0 since the
curves are closed. As A1 = A2 = A3 = A, ∑ λi = 0, and λi ̸= 0 for all i, A4 needs to be equal to A as
well.

4 Injectivity of the fourth vertex’ trace

In this section we ﬁnish the proof of Theorem 1.5. In light of Lemma 2.1 and Corollary 3.8, it remains
prove the following proposition. Its proof relies heavily on the quadrilateral being cyclic.

Proposition 4.1. Let γ be a strictly convex smooth Jordan curve. Let P1P2P3P4 and Q1Q2Q3Q4 be
two similar convex circular quadrilaterals with P4 = Q4, such that the triangles P1P2P3 and Q1Q2Q3
lie counter-clockwise on γ, and such that P4 = Q4 lies outside of γ, and such that the inner angle at
P4 is at least π/2. Then P1P2P3P4 = Q1Q2Q3Q4.

It reminds of math competition type problems. Indeed, it could be reformulated without mention-
ing γ at all, just assuming that P1, P2, P3, Q1, Q2, Q3 are in convex position but P4 = Q4 lies outside
their convex hull.
Before proving this proposition we need a lemma about circular quadrilaterals. Any two distinct
points A, B in the plane determine a directed line −−→
AB. We say that a point X lies to the right of −−→
AB
if it lies in the closed half-space bounded by the line AB that lies on our right hand side when we look
from A to B.
 7

Lemma 4.2. Let P1P2P3P4 be a convex circular quadrilateral. For 1 ≤ i < j ≤ 3 let ρij denote the
rotation-dilatation about P4 that sends Pi to Pj. Then

a) ρ13(−−−→
P1P2) = −−−→
P2P3.

b) ρ12(−−−→
P1P3) = −−−→
P2P3.

c) ρ23(−−−→
P1P2) = −−−→
P1P3.

Proof. Let {i, j, k} = {1, 2, 3}. Then ρij(PkPi) = PkPj follows from combining ρ(Pi) = Pj and
∡PiP4Pj = ∡PiPkPj mod π. This proves the lemma up to the orientation issue. Now, all lines in the
lemma are oriented in such a way that they have P4 on their left as P1P2P3P4 is positively oriented,
and all ρij ﬁx P4 and preserve the orientation of the plane, therefore they also respect the orientations
of the lines.

Figure 5: Possible regions for γPiPj . Figure 6: Case 3, Q1 ∈ γP3P1 .

Lemma 4.3. In the situation of Proposition 4.1 the following equivalences hold.

a) Q1 lies to the right of −−−→
P1P2 if and only if Q3 lies to the right of −−−→
P2P3.

b) Q1 lies to the right of −−−→
P1P3 if and only if Q2 lies to the right of −−−→
P2P3.

c) Q2 lies to the right of −−−→
P1P2 if and only if Q3 lies to the right of −−−→
P1P3.

Proof. Q1Q2Q3Q4 is obtained from P1P2P3P4 via a rotation-dilatation about P4, and any two rotation-
dilatations about P4 commute. Thus ρij(Qi) = Qj. Therefore the lemma follows from the previous
one using that rotation-dilatations preserve the orientation of R 2.

Proof of Proposition 4.1. For two distinct points A, B on γ, let γAB denote the closed curve segment
on γ from A to B in counter-clockwise direction. Then we get two decompositions

γ = γP1P2 ∪ γP2P3 ∪ γP3P1 = γQ1Q2 ∪ γQ2Q3 ∪ γQ3Q1 .

Note that each point X ∈ γPiPj (i ̸= j) lies to the right of −−→
PiPj, see Figure 5.

Case 1. Q1 ∈ γP1P2 : Then Q1 lies to the right of −−−→
P1P2, and thus by the lemma, Q3 lies to the right
of −−−→
P2P3, whence Q3 ∈ γP2P3.
On the other hand, Q1 lies to the right of −−−→
P1P3, and thus by the lemma, Q2 lies to the right
of −−−→
P2P3. Hence Q2 ∈ γP2P3 and thus Q2 lies to the left of −−−→
P1P2, whence by the lemma, Q3 lies to the
left of −−−→
P1P3. Both restrictions on Q3 only allow Q3 = P3 and P1P2P3P4 = Q1Q2Q3Q4 follows.
From now on we may assume Q1 ̸∈ γP1P2 , and by symmetry (P ↔ Q and 1 ↔ 3),

Q1 ̸∈ γP1P2, P1 ̸∈ γQ1Q2 , Q3 ̸∈ γP2P3, P3 ̸∈ γQ2Q3 .

8

Case 2. Q1 ∈ γP2P3: Then Q1 lies to the left of −−−→
P1P3, hence by the lemma, Q2 lies to the left of −−−→
P2P3,
and thus Q2 ∈ γP2P3 . As P3 ̸∈ γQ2Q3, together with Q2 also Q3 needs to lie in γP2P3 . Therefore, Q3
lies to the right of −−−→
P2P3, and hence by the lemma, Q1 lies to the right of −−−→
P1P2, whence Q1 ∈ γP1P2,
which was already treated in the previous case.

Case 3. Q1 ∈ γP3P1: We may assume Q1 ̸= P1, otherwise the claim of the proposition follows. As
this case is the only remaining one, by symmetry we may assume

Q1 ∈ γP3P1, P1 ∈ γQ3Q1, Q3 ∈ γP3P1, P3 ∈ γQ3Q1.

This means not only that Q1 and Q3 lie on γP3P1, but also their order is determined: In counter-
clockwise order we see on γP3P1 the points P3, Q1, Q3, P1. (We allow that some of the points may
coincide.) As furthermore both triangles P1P2P3 and Q1Q2Q3 lie counter-clockwise on γ, this deter-
mines the cyclic order, in which all six of these points lie on γ, namely: P1, P2, P3, Q1, Q2, Q3 (up to
cyclic permutation, and possibly Q1 = P3 and/or P1 = Q3). This means (from P4’th point of view,
see Figure 6) that the two cones spanned by the angles ∠P1P4P3 and ∠Q1Q4Q3 with common apex
P4 = Q4 may at most have some boundary in common. As the size of both angles was assumed to be
at least π/2, it follows that P4 = Q4 lies in the convex hull of {P1, P3, Q1, Q3} ⊂ γ, and thus not in
the exterior of the convex curve γ, a contradiction!

Remark 4.4. Without the angle restriction ∡P1P4P3 ≥ π/2 one can indeed easily ﬁnd two similar
convex circular quadrilaterals P1P2P3P4 and Q1Q2Q3Q4 with P4 = Q4, such that P1P2P3Q1Q2Q3 is
a convex hexagon not containing P4 = Q4.

5 Singular curves

Let γ be a convex Jordan curve. At each point P ∈ γ we consider the inner angle 0 < αP ≤ π deﬁned
by αP = sup ∡AP B, the supremum ranging over all points A, B ∈ γ \{P }. Due to convexity, P is
a regular point of γ if and only if αP = π, otherwise it is a singular point of γ. We say that αP is
attained, if this supremum is attained, i.e. if in a neighborhood of P , γ looks like two straight line
segments meeting at an angle αP .
The complementary angle at P is αc
P = π − αP . As the total curvature of γ is 2π, the sum of the
complementary angles at all the singular points of γ is at most 2π. This implies that there are at most
countably many singular points, and for any ε > 0 there are at most ﬁnitely many singular points with
αc
P ≥ ε, or equivalently, with αP ≤ π − ε.
Let Q be a given circular quadrilateral with signed angles λ and µ between their opposite edge
pairs, as above Theorem 1.6. Then there are only ﬁnitely many singular points S of γ with inner angle
αS ≤ max(|λ|, |µ|), let us call these the crucial singular points, and we call αS a crucial angle.
They are crucial indeed, as they make the usual approximation argument break for two reasons.

1. If we smoothen γ at a crucial singular point S then this will introduce a tiny inscribed Q close
to S (unless αS = max(|λ|, |µ|), in which case a case distinction is needed). In the limit, there
will be a sequence of such inscribed Q’s that converges to the quadrilateral that is degenerate
to SSSS.

2. When we trace inscribed triangles T ′ similar to T = P1P2P3, then they may also run into a
crucial singular point S and come out again in a diﬀerent fashion, which is a priori not a serious
problem. The problem is that the trace γ4 of the fourth vertex can change sides of γ, namely
exactly when T ′ is degenerate to SSS. Here, the area argument that worked for smooth curves
would break, as the degenerate quadrilateral at S does not count as an inscribed Q.

If there is no crucial singular point, we can indeed simply approximate γ by a smooth convex curve,
reducing the problem to Theorem 1.5, and the limit argument works.
Let S1, . . . , Sn, be the crucial singular points, and αSi their inner angles.

9

5.1 Reduction to a generic setting

Let Q = P1P2P3P4 be a circular quadrilateral with δ ≥ π/2, and let γ be a convex Jordan curve. The
inner angles of T = P1P2P3 are denoted by α2, β, ζ2. Reducing to a generic setting is cumbersome for
the above mentioned reasons. We have to make sure that the approximation keeps the essential features
of the curve such that we can easily study the neighborhoods of crucial singular points, and that the
limit argument works (i.e. that ﬁnding a solution for each approximation yields a non-degenerate
solution for the given curve). Depending on the taste of the reader, we oﬀer two diﬀerent ways both
leading to a useful generic approximation of γ, either a piecewise smooth one, or a piecewise linear
one. The author usually prefers smooth settings, however here the discrete one might indeed be less
technical.

5.1.1 Piecewise smooth approximation

We proceed in three steps.

1. In case some αSi ∈ {|λ|, |µ|}, there are two possibilities:

(a) If αSi is attained (i.e. the supremum in the deﬁnition of αSi is attained) then a neighborhood
of S looks like two line segments meeting at an angle αSi. In that neighborhood, inﬁnitely
many copies of Q’s are inscribed.

(b) If αSi is not attained, then we can deform the curve locally around Si making the inner
angle slightly smaller and such that this smaller angle is attained.

Now, no inner angle is equal to |λ| or |µ|.

2. We deform the curve such that it stays convex and is smooth away from the crucial singular
points, and such that the crucial inner angles αSi are attained and do not belong to belong to
{α2, β, ζ2}:

(a) If αSi is crucial, we replace a neighborhood of γ around Si by two line segments that meet
at some crucial angle close to αSi and not in {α2, β, ζ2}.

(b) If αSi is non-crucial, we replace a neighborhood of γ around Si by a smooth arc.

(c) The remainder of γ is deformed slightly in the C 1-sense to make γ convex and smooth away
from the crucial angles.

This makes us easily understand the set ZT of inscribed triangles similar to T in the vicinity of
singular points Si (i.e. those triangles with all three vertices in a small neighborhood of Si that
are similar to T ): There ZT is a union of smooth paths, with gaps exactly where T ′ becomes
degenerate to SiSiSi. One could extend ZT at these points continuously.

3. The test-map f : (S1)
3 \ ∆ → R 2 from Section 2 that measured ZT = f −1(0) may not be
transversal to 0. To solve this, we could add local bumps to γ as in Section 2 (which is possible).
Instead, let us simply deform f directly, as follows. Around ∆, f is already transversal to 0
by the previous step. So we deform f only away from a neighborhood around ∆ by a suitable
ε-homotopy. This makes its preimage ZT into a 1-manifold, which is topologically a circle
punctured at possibly some of the points SiSiSi.

Generic setting. To summarize, we are now in the situation, where γ is a convex Jordan curve with
at most ﬁnitely many singular points, all of which are crucial, all of whose angles αSi are attained
and not among {α2, β, ζ2, |λ|, |µ|}. And with the deformed test-map, ZT = f −1(0) is a proper 1-
dimensional sub-manifold of (S1)
3 \ ∆, which parametrizes inscribed triangles that are up to some
small error similar to T , and this error vanishes for small triangles.

10

5.1.2 Piecewise linear approximation

In case some αSi ∈ {|λ|, |µ|}, there are two possibilities:

1. If the supremum αSi is attained then a neighborhood of S looks like two line segments meeting
at an angle αSi . In that neighborhood, inﬁnitely many Q’s are inscribed.

2. If the supremum αSi is not attained, in what follows we will make sure to approximate this angle
only from below (which can be done in general precisely because αSi is not attained).

We construct a piecewise linear curve γP L approximating γ (in the C 0 sense) with the following
properties: It will be convex and piecewise linear. Each inner angle of γP L that approximates a crucial
inner angle of γ needs to be crucial as well. All other angles of γP L must be non-crucial. No inner
angle of γP L is allowed to be in {α2, β, ζ2, |λ|, |µ|}. So far this is actually not diﬃcult to do.
Additionally we want that the set ZT of inscribed triangles similar to T is a piecewise smooth
1-manifold (in a generic way). Here we use an algebraic trick. If we pick a 3-tuple (e1, e2, e3) of edges
in γP L and consider the triangles T ′ = P ′
1P ′
2P ′
3 ∈ ZT that have their i’th vertex on ei (i = 1, 2, 3),
then we see that they form a polytope: We let P ′
1 and P ′
2 move freely on the lines extending e1 and e2,
and see that the condition that P ′
3 lies on the line extending e3 is a linear equation. Furthermore,
the restriction that Pi lies on ei yields two linear inequalities (for each i = 1, 2, 3). So all we need to
ensure is that these linear equations and inequalities are generic. This can be achieved by choosing
the vertices of γP L in such a way that all its real coordinates are algebraically independent over the
extension ﬁeld Q (cos α2, cos β, cos ζ2, cos λ, cos µ). This is the promised algebraic trick. We included
the cosines such that none of the inner angles of γP L is in {α2, β, ζ2, |λ|, |µ|}.
Thus in what follows we may work with γP L in place of γ.

5.2 Inscribed triangles in the neighborhood of singular points

Assume we are in the generic setting from above. To simplify notation, we write Pi instead of P ′
i .
Let S be a singular point of γ with inner angle αS = ε (crucial or not), and let U be a suﬃciently
small neighborhood of SSS ∈ (S1)3. ZT may visit U up to three times, once for each inner angle of T
that is larger than ε. To be precise, for each such inner angle, ZT ∩ U has two components, namely one
where the triangles run into the corner, and one where they come out of it. In what follows, imagine
that we connect these two ends with a one-dimensional family of imaginary inﬁnitesimal triangles at
S: The component of ZT ﬁrst runs into the corner S, becomes inﬁnitesimally small, then it rotates on
that spot counter-clockwise by the angle ε, and ﬁnally it comes along ZT out of the corner again, see
Figure 7. All this can be made technically precise when working in the blowing-up of (S1)3 along ∆
(or in the Fulton–MacPherson compactiﬁcation of (S1)
3 \ ∆).
Now let us see what happens with P4 in each of the three cases, compare with Figure 7.

1.) This case occurs if and only if α2 > ε. In the beginning, P4 lies outside of γ. At the end, P4 lies
outside if and only if λ < ε.

2.) This case occurs if and only if β > ε. In the beginning, P4 lies outside of γ if and only if λ < −ε.
At the end, P4 lies outside if and only if µ < −ε. If λ < −ε or µ < −ε (which implies β > ε), P4
will change sides of γ.

3.) This case occurs if and only if ζ2 > ε. In the beginning, P4 lies outside of γ if and only if µ < ε.
At the end, P4 lies outside.

This yields simple criteria for when P4 changes sides of γ when ZT passes a singular point S with
inner angle αS = ε.

1. P4 will change sides of γ during motion 1.) at S if and only if λ > ε, as then α2 > ε is
automatically fulﬁlled.
 11

Figure 7: The three ways the curve ZT of inscribed triangles similar to T can possibly
move into a singular point, rotate the inﬁnitesimal triangle by ε, and come out again.

2. P4 will change sides of γ during motion 2.) at S if and only if λ < −ε or µ < −ε, as in this case
β > ε is automatically fulﬁlled and both λ, µ < −ε cannot happen as λ + µ = 2δ − π ≥ 0.

3. P4 will change sides of γ during motion 3.) at S if and only if µ > ε, as then ζ2 > ε is
automatically fulﬁlled.

With this analysis we are ready to make use of these degeneracies. We start with the proof of the
general main theorem.

Proof of Theorem 1.6. In Section 5.1 we argued what kind of genericity we can assume about γ; as
we may approximate non-generic curves by generic ones and use a limit argument. Further we could
assume that there is at least one crucial singular points as otherwise the proof for smooth curves can
be used. We will only consider the case |λ| ≥ |µ|; since the case |λ| ≤ |µ| works analogously as the
above criteria are essentially symmetric in λ ↔ µ.
We will argue now how P4 changes sides of γ when ZT passes (a degenerate triangle at) a singular
point S. By the above criteria, whenever ZT passes a non-crucial singular point S, P4 stays outside
or stays inside.
More can happen at a crucial singular point S. Here, αS < |λ|. The assertion of the theorem
implies |µ| < αS. As λ + µ = 2δ − π ≥ 0, this can happen only if λ > 0. Thus, |µ| < αS < λ. Via
the criteria above, we see that during the potential motions of type 2.) or 3.) at S, P4 stays outside.
However there is a motion of type 1.) at S, and during that motion P4 changes from the outside of γ
to the inside.
These are all possibilities in which P4 can change sides of γ via a degenerate inscribed Q. Thus, if
n is the number of crucial singular points S of γ, then P4 needs to go at least n times back from the
inside of γ to the outside, and each time it yields a non-degenerate inscribed Q.

In fact, the proof can be easily made quantitative, which yields the following extension.

12

Theorem 5.1 (Quantitative extension of Theorem 1.6). Let Q be a circular quadrilateral with signed
angles λ and µ as above. Suppose γ is a (continuous) convex Jordan curve all whose inner angles have
size larger than min(|λ|, |µ|). Let n be the number of crucial singular points S, i.e. those with inner
angle aS ≤ max(|λ|, |µ|). Then γ inscribes at least max(n, 1) diﬀerent copies of Q.

Proof. We follow the proof of Theorem 1.6. Between any successive two of the n times that γ4 crosses
γ via a degenerate inscribed Q, γ4 needs to go back outside producing a non-degenerate inscribed Q.
These events are separated from each other, use for example that using the discrete approximations
the angle of −−−→
P1P2 with the x-axis is increasing (by how far depends only on the geometry of the original
curve as well as on the C 1-distance of the original curve to its piecewise linear approximation). Thus,
in the limit we obtain n diﬀerent non-degenerate inscribed Q’s for the given curve γ.

Given Q, the number n of crucial singular points can bounded from above using the inequality
n(π − max(|λ|, |µ|)) ≤ ∑

S crucial αc
S ≤ 2π, which seems to bound the strength of Theorem 5.1.
On the other hand, Theorem 5.1 can be tight for arbitrary large n: Isosceles trapezoids have (after
possibly relabeling the vertices) angles µ = 0 and 0 ≤ λ < π, and all such values for λ are possible.
Now, a regular n-gon has n inner angles of size α(n) = π − 2π/n. For an isosceles trapezoid Q with
λ > α(n), there are exactly n ways to inscribe it in the regular n-gon, which matches the lower bound
given in Theorem 5.1.

5.3 Inscribing isosceles trapezoids in non-convex curves

Akopyan asked (private communication) whether the implication Theorem 1.5 ⇒ Theorem 1.4 proved
in Section 5 works in the non-convex case as well.
To ﬁnd a positive answer, let us restrict to the class J 1
pw of piecewise C 1 Jordan curves without
cusps. By this we mean curves γ : S1 → R 2 that are C 1-regular along ﬁnitely many closed intervals
that cover S1, and such that at the singular points of γ there are no cusps (i.e. no inner or outer angles
of size 0).

Theorem 5.2. J 1
pw inscribes Q if and only if J ∞ inscribes Q .

One would conjecture that J 1
pw can be replaced by J 0, but this is completely out of reach, as this
would contain Toeplitz’ inscribed square problem as a special case.

Figure 8: Projection of Z ∗
T to (S1)
2. When
bouncing oﬀ from ∆, it cannot go ‘backwards’. Figure 9: Singular point S with inner or outer
angle equal to λ can become crucial or not.

Proof of Theorem 5.2. We only need to prove the if-part. Let Q ∈ Q , and we may assume λ ≥ 0,
µ = 0, δ ≥ π/2, and that Q is positively oriented. Let γ ∈ J 1
pw. By assumption, any smooth
approximation of γ will inscribe of copy of Q.
We extend the notion of the inner and outer angles in the obvious way to the non-convex setting:
Let αP ∈ (0, 2π) denote the inner angle at P ∈ γ (which shows towards the interior of γ), and
α◦
P = 2π − αP the corresponding outer angle. We call an (inner or outer) angle crucial if it measures
at most λ.
If γ has no crucial inner and outer angles, then we can use the standard limit argument to show that
γ inscribes a copy of Q: We approximate γ suitably by a sequence of smooth Jordan curves (γ(n))n,

13

such that the sizes of their inscribed copies of Q are uniformly bounded away from zero. The latter is
possible precisely because γ has no crucial inner and outer angles. By assumption, each γ(n) has an
inscribed copy Q(n) of Q, and by compactness, some subsequence converges to an inscribed copy of Q
in γ, which is non-degenerate due to the uniform lower bound on the sizes of Q(n).
We now come to the the case when γ has a crucial inner or outer angle. This is the non-trivial case
as smoothening a crucial angle will (usually) introduce a tiny inscribed copy of Q, which would vanish
in a limit argument into the corner. First, we assume that γ is as generic as needed with respect
to the C 1-topology. As in the convex setting, we construct ZT and extend it with ‘inﬁnitesimal’
triangles at the singular points (as if the corners were inﬁnitesimally smoothened) to make it into a
closed 1-manifold, sitting naturally in the blowing-up of (S1)
3 \ ∆ along ∆. It still represents the same
homology class in H1((S1)
3; Z ), as is seen e.g. via a cobordism argument by deforming γ into a strictly
convex curve. However, ZT may have several connected components. One can show that exactly
one of these components represents the same homology class as ∆, i.e. it traces inscribed triangles
each of whose vertices wind around γ once, and all the other components are null-homologous; see
Karasev [17] for a formal proof. Let Z 0
T denote the former component of ZT , and Z k
T (1 ≤ k ≤ k0) the
null-homologous ones.
As for convex curves the triangles T ′ = P1P2P3 traced by ZT may run into singular points S ∈ γ
and come out again, but now this is possible in two diﬀerent ways, namely when one of the inner angles
of T is smaller than either the inner angle αS (as before), or the outer angle αo
S (the new case). Both
cases are symmetric to each other, and in both settings we can use the analysis of Figure 7, except
that they diﬀer in up to two ways:

1. The sides of the interior and the exterior of γ are interchanged.

2. The direction of movement may be the opposite, i.e. for ε = αo
S, the arrows in Figure 7 may
show the other way. This also depends on the orientation of ZT .

In fact one can show that if we give ZT one of the two possible preimage orientations, then that
direction of movement will be opposite to Figure 7 exactly at outer angles; however we will only need
a weaker statement (see the claim below). As before, for each T ′ we denote by P4 = P4(T ′) the forth
vertex that makes P1P2P3P4 similar to Q. For now we impose an additional genericity assumption
on γ that none of its singular inner or outer angle is of size exactly λ (this will be justiﬁed in the last
paragraph). Then by the analysis of Section 5.2, during the passage of ZT through a singular vertex,
P4 will change sides with respect to γ if and only if this is a motion of type 1 at a crucial inner or
outer angle. Conversely, at each such angle, exactly one motion of type 1 occurs (and possibly others
of type 2 and 3).
Now consider one crucial inner or outer angle at some S ∈ γ, and let Z S
T be the component of ZT
that passes SSS in a motion of type 1. We claim: Z S
T can be oriented in such a way that each time
Z S
T passes in that orientation some crucial (inner or outer) angle in a motion of type 1, the fourth
vertex P4 moves from the outside to the inside of γ. As these are the only times where Z S
T passes a
degenerate quadrilateral at which P4 changes sides with respect to γ, and since P4 also has to move
equally often from the inside of γ to the outside, this claim proves the existence of an inscribed copy
of Q.
To prove the claim, consider the projection π12 : ZT → (S1)2 given by the position of the ﬁrst two
vertices P1, P2 of the parametrized T ′, see Figure 8. Let Z ∗
T := π12(Z S
T ), which is a closed path that
may only touch the diagonal of (S1)
2 without stepping over it.

Case 1: Z S
T = Z 0
T . Then Z ∗
T is homologous to the diagonal ∆ ⊂ (S1)2, and we give Z ∗
T the orientation
that corresponds to the standard orientation of ∆ (i.e. with tangent vectors (1, 1)), and Z 0
T the one that
corresponds to it via π12. Note that Z ∗
T does not self-intersect (except for possibly staying steady at
some points SS on the diagonal for some time) because T ′ is determined by its edge P1P2. Therefore,
whenever Z ∗
T touches ∆, it cannot ‘go back’ (see the question mark in Figure 8) as otherwise it would
have to self-intersect by a Jordan curve theorem type argument. We observe that at crucial inner

14

angles the direction of motion when Z 0
T passes SSS is as in Figure 7, and at crucial outer angles it is
the opposite. This proves the claim in Case 1.

Case 2: Z S
T = Z k
T , 1 ≤ k ≤ k0. Note that π12(Z 0
T ) cuts (S1)2 \ ∆ into at least two connected
components, and Z ∗
T must lies in one of them. Thus, if U ⊂ (S1)2 is a small neighborhood of ∆, Z ∗
T
intersects with only one of the two connected components of U \ ∆. In other words, the only singular
angles that Z S
T traverses are either all inner or all outer. Moreover, by an analog “no backwards”
argument as in Case 1, we see that the motions of passing a singular angle are always in the same
direction as in Figure 7 or always in the opposite direction (depending on the orientation of Z S
T ). The
claim follows.
It still remains to discuss how γ can be assumed to be generic. This works as with convex curves
(Section 5.1), but one crucial additional technical problem appears for singular points S with αS or
αo
S equal to λ, see Figure 9. If λ = αS is an inner angle, we call the interior of γ the λ-side and the
exterior the λ
o-side; else λ = αo
S is an outer angle and we swap these two notions. In a suitably small
neighborhood U ⊂ S1 of S, the triangles T ′ such that P2, P1, S, P3 lie in this order on γ (or reversed)
can be parametrized continuously: Near S, for each P2 there is exactly one such triangle, where for
example P1 can be obtained by intersecting γ|U with its own rotation about P2 by the angle β. (That
this intersection point exists follows from α2 > λ, and its uniqueness uses that γ is composed of closed
C 1-pieces and a mean value theorem type argument.) Now consider the trace of P4 when T ′ approaches
the degenerate triangle at S. If P4 stays in the λ-side of γ, we call S crucial. If P4 stays in the λo-side
of γ, we call S non-crucial. Otherwise P4 intersects γ on T ′’s way towards S and we are done. Now,
in the generic approximation of γ that we construct, say γP L, we choose the inner/outer angle at S
to be strictly smaller or strictly larger than λ depending on whether S is crucial or not. This keeps
the trace of P4 on the correct sides in the approximations, which avoids solutions that in the limit
degenerate to S.

Two steps in the proof can be considered ‘lucky’: 1.) We were able to use 2-dimensional arguments
of Jordan curve theorem type to show that P4 can change sides of γ only in one direction at points
where ZT degenerates. The author is not aware of any other proofs in this area where technical
diﬃculties for non-smooth curves arise in such a lopsided way that the theorem becomes trivially
provable. 2.) The inner or outer angles of size exactly λ, at which the notion of whether P4 changes
sides of γ during motions of type 1 may not be well-deﬁned, can be deformed without negatively
aﬀecting the limit argument, as for the sake of ZT such angles are still generic.

Remark 5.3 (Analogue of Theorem 1.6). Theorem 5.2 holds as well for circular quadrilaterals Q if
we restrict to curves whose inner and outer angles are larger than min(|λ|, |µ|); the proof is the same.

Finally we can combine Theorem 5.2 with the recent result of Greene–Lobb [10] that J ∞ in-
scribes Q⃝, and we obtain another positive partial answer for Question 1.1:

Corollary 5.4 (Assuming [10]). J 1
pw inscribes Q .

More generally, using Remark 5.3 in place of Theorem 5.2, we obtain:

Corollary 5.5 (Assuming [10]). Any circular quadrilateral Q, with signed angles λ and µ as above,
can be inscribed into any γ ∈ J 1
pw whose inner and outer angles are all larger than min(|λ|, |µ|).

The lower bound min(|λ|, |µ|) is best possible, as can be seen by taking as γ the union of two
congruent circular arcs that meet at their endpoints in a given angle.

Acknowledgement. I wish to thank Arseniy Akopyan, Sergey Avvakumov, Roman Karasev and
Sebastian Matschke for valuable correspondence. In particular one of Akopyan’s questions led to
Section 5.3. The plane geometry software Cinderella [30] was a useful visualization tool when ﬁnding
Proposition 4.1 and its proof. Moreover, I thank the anonymous referee for valuable comments. This
research was supported by the Initiative d’excellence de l’Universit´e de Bordeaux (IdEx) and by Simons
Foundation grant #550023 at Boston University.
 15

References

[1] Arseniy Akopyan and Sergey Avvakumov. Any cyclic quadrilateral can be inscribed in any closed convex
smooth curve. arXiv:1712.10205, 2017.
[2] Jason Cantarella, Elizabeth Denne, and John McCleary. Transversality in Conﬁguration Spaces and the
“Square-Peg” Problem. arXiv:1402.6174, 2014.
[3] Carl Marius Christensen. A square inscribed in a convex ﬁgure (in Danish). Matematisk Tidsskrift B,
1950:22–26, 1950.
[4] Wolfram Decker, Gert-Martin Greuel, Gerhard Pﬁster, and Hans Sch¨onemann. Singular 4-1-0 — A
computer algebra system for polynomial computations. https://www.singular.uni-kl.de, 2016.
[5] Elizabeth Denne. Inscribed squares: Denne speaks. http://quomodocumque.wordpress.com/2007/08/31/-
inscribed-squares-denne-speaks/, 2007. Guest post on Jordan S. Ellenberg’s blog Quomodocumque.
[6] The Sage Developers. SageMath (Version 8.0), 2017. http://www.sagemath.org.
[7] Arnold Emch. Some properties of closed convex curves in a plane. Amer. J. Math, 35:407–412, 1913.
[8] Arnold Emch. On the medians of a closed convex polygon. Amer. J. Math, 37:19–28, 1915.
[9] Arnold Emch. On some properties of the medians of closed continuous curves formed by analytic arcs.
Amer. J. Math., 38(1):6–18, 1916.
[10] Joshua E. Greene and Andrew Lobb. Cyclic quadrilaterals and smooth Jordan curves. arXiv:2011.05216,
2020.
[11] Joshua E. Greene and Andrew Lobb. The Rectangular Peg Problem. arXiv:2005.09193, 2020.
[12] Victor Guillemin and Alan Pollack. Diﬀerential topology. Prentice Hall, 1974.
[13] Clarence M. Hebbert. The inscribed and circumscribed squares of a quadrilateral and their signiﬁcance
in kinematic geometry. Ann. of Math. (2), 16(1-4):38–42, 1914/15.
[14] Wouter van Heijst, 2014. Master thesis, in preparation.
[15] Richard P. Jerrard. Inscribed squares in plane curves. Trans. Amer. Math. Soc., 98:234–241, 1961.
[16] Roman N. Karasev. Topological methods in combinatorial geometry. Russian Math. Surveys, 63(6):1031–
1078, 2008.
[17] Roman N. Karasev. A note on Makeev’s conjectures. J. Math. Sci., 212(5):521–526, 2016.
[18] Victor Klee and Stan Wagon. Old and new unsolved problems in plane geometry and number theory.
Dolciani Mathematical Expositions. The Math. Ass. America, 1996.
[19] Vladimir V. Makeev. On quadrangles inscribed in a closed curve. Math. Notes, 57(1-2):91–93, 1995.
[20] Vladimir V. Makeev. On quadrangles inscribed in a closed curve and the vertices of the curve. J. Math.
Sci., 131(1):5395–5400, 2005.
[21] Benjamin Matschke. On the Square Peg Problem and some relatives. arXiv:1001.0186, 2009.
[22] Benjamin Matschke. Equivariant topology methods in discrete geometry. PhD thesis, Freie Universit¨at
Berlin, 2011.
[23] Benjamin Matschke. A survey on the square peg problem. Notices Amer. Math. Soc., 61(4):346–352,
2014.
[24] Mark D. Meyerson. Equilateral triangles and continuous curves. Polska Akademia Nauk. Fundamenta
Mathematicae, 110(1):1–9, 1980.
[25] Mark J. Nielsen. Triangles inscribed in simple closed curves. Geometriae Dedicata, 43:291–297, 1992.
[26] Mark J. Nielsen. Web page on Figures Inscribed in Curves. http://www.webpages.uidaho.edu/∼markn/-
squares/, 2000.
[27] Mark J. Nielsen and Stephen E. Wright. Rectangles inscribed in symmetric continua. Geom. Dedicata,
56(3):285–297, 1995.
[28] Igor Pak. Lectures on Discrete and Polyhedral Geometry. http://www.math.ucla.edu/∼pak/book.htm,
2010.
[29] Ville H. Pettersson, Helge A. Tverberg, and Patric R. J. ¨Osterg˚ard. A note on Toeplitz’ conjecture.
Discrete Comput. Geom., 51(3):722–728, 2014.
[30] J¨urgen Richter-Gebert and Ulrich H. Kortenkamp. The Cinderella.2 Manual. Springer-Verlag, 2012.
[31] Feli´u Sagols and Ra´ul Mar´ın. The inscribed square conjecture in the digital plane. In Combinatorial image
analysis, volume 5852 of Lecture Notes in Comput. Sci., pages 411–424. Springer, 2009.
[32] Feli´u Sagols and Ra´ul Mar´ın. Two discrete versions of the inscribed square conjecture and some related
problems. Theoret. Comput. Sci., 412(15):1301–1312, 2011.
[33] Lev G. Schnirelman. On some geometric properties of closed curves. (in Russian) Usp. Mat. Nauk,
10:34–44, 1944. Available at http://ega-math.narod.ru/Nquant/Square.djv. Posthumous reproduction and
extension of the author’s original article in Sbornik Rabot Matematiˇceskogo Razdela Sekcii Estestvennyh i

16

Toˇcnyh Nauk Komakademii, Moscow, 1929.
[34] Walter R. Stromquist. Inscribed squares and square-like quadrilaterals in closed curves. Mathematika,
36:187–197, 1989.
[35] Terence Tao. An integration approach to the Toeplitz square peg problem. Forum Math. Sigma, 5:e30,
63 pp, 2017.
[36] Otto Toeplitz. Ueber einige Aufgaben der Analysis situs. Verhandlungen der Schweizerischen Natur-
forschenden Gesellschaft in Solothurn, 4:197, 1911.
[37] Siniˇsa Vre´cica and Rade T. ˇZivaljevi´c. Fulton–MacPherson compactiﬁcation, cyclohedra, and the polyg-
onal pegs problem. Israel J. Math., 184(1):221–249, 2011.
[38] Ying-Qing Wu. Inscribing smooth knots with regular polygons. Bull. London Math. Soc., 36(2):176–180,
2004.
[39] Konrad Zindler. ¨Uber konvexe Gebilde. Monatshefte f¨ur Mathematik und Physik, 31:25–56, 1921.

17
