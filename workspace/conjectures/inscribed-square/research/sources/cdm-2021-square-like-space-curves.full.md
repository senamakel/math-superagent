<!-- source: https://arxiv.org/pdf/2103.13848 | converted from PDF -->

SQUARE-LIKE QUADRILATERALS INSCRIBED IN EMBEDDED SPACE CURVES

JASON CANTARELLA, ELIZABETH DENNE, AND JOHN MCCLEARY

ABSTRACT. The square-peg problem asks if every Jordan curve in the plane has four points which
are the vertices of a square. The problem is open for continuous Jordan curves, but it has been
resolved for various regularity classes of curves between continuous and C 1-smooth Jordan curves.
Here, in a generalization of the square-peg problem, we consider embedded curves in space, and ask
if they have inscribed quadrilaterals with equal sides and equal diagonals. We call these quadrilat-
erals “square-like”. We give a regularity class (ﬁnite total curvature without cusps) in which we can
prove that every embedded curve has an inscribed square-like quadrilateral. The key idea is to use
local data to show that short enough arcs have small curvature, thus ruling out small squares. This
allows us to successfully use a limiting argument on approximating curves.

1. INTRODUCTION

Take an embedding γ : S1 ↪→ Rn of a circle in Rn. An inscribed polygon is a polygon whose
vertices lie on the curve. Note that when n = 2, the sides of the polygon do not have to lie in the
interior of the planar curve. There is a series of problems which ask what kind of quadrilaterals
can be inscribed in such curves
1. A classic example of such a problem is the old, yet still open,
question due to O. Toeplitz [38]. He asked whether a square can be inscribed in a Jordan curve (a
continuous, simple, closed curve in the plane). If we think of the Jordan curve as the “round hole”,
this conjecture has affectionately been nick-named the square-peg problem by mathematicians.
There have been many attempts to resolve the square-peg problem, and a brief overview of the
history of the problem can be found in Appendix A, as well as a number of survey articles (see for
instance [17, 23, 27]).
If we think of a square as being a quadrilateral that has equal sides and equal diagonals, then
we have a property of quadrilaterals that holds in any dimension. We say such a quadrilateral is
square-like (see Deﬁnition 2). In this paper, we look at a generalization of the square-peg problem:

Conjecture 1. There is a square-like quadrilateral inscribed in any embedding of S1 in Rn.

Date: March 26, 2021.
2020 Mathematics Subject Classiﬁcation. Primary 53A04, Secondary 55R80, 57Q65, 58A20, 51M04.
Key words and phrases. Square-peg problem, square-like quadrilaterals, embedded space curves, ﬁnite total curva-
ture.
1Including recent results on ﬁnding inscribed rectangles and cyclic quadrilaterals; see for instance [1, 2, 21, 10, 14,
15, 24, 33, 34]. 1arXiv:2103.13848v1  [math.DG]  25 Mar 2021
2 JASON CANTARELLA, ELIZABETH DENNE, AND JOHN MCCLEARY

FIGURE 1. On the left, we see a square-like quadrilateral inscribed in a space
curve. The four equal sides are marked in red, while the diagonals are unmarked.
The shape forms a special tetrahedron. On the right, we see a square-like quadri-
lateral inscribed in a plane curve. This shows that a planar square-like quadrilateral
is indeed a square.

Two examples of inscribed square-like quadrilaterals are shown in Figure 1. Just as with the
square-peg problem, we expect Conjecture 1 to be proved for various regularity classes of curves.
Indeed, in [3], we proved that there is a dense family of C∞-smoothly embedded S1 in Rn,
each of which has an odd number of inscribed square-like quadrilaterals. (This result and the
Whitney C∞ topology used are reviewed in Section 2.) Going back to the square-peg problem,
there are a number of solutions which required a mild-regularity hypothesis, for example those of
W. Stromquist [35], B. Matschke [22] and T. Tao [37]. These hypotheses require the curve to be
planar, and the regularity of the embedding lies somewhere between continuous and C1-smooth.
In this paper, we ﬁnd a regularity condition of a similar ﬂavor that allow us to resolve Conjecture 1,
but our regularity condition (discussed below) holds in any dimension.
The key idea in this paper is to look at a limiting argument. That is, take any curve which
is a limit of a sequence of C∞-smooth curves with inscribed square-like quadrilaterals. Can we
show that the limiting curve also has an inscribed square-like quadrilateral? The problem is clear:
The sequence of square-like quadrilaterals on the approximating curves may have sidelengths ap-
proaching zero. If one could construct a general lower bound on these sidelengths in terms of the
global geometry of the curves with the inscribed square-like quadrilaterals, this possibility could
be ruled out. We do not know of any explicit example of a family of curves where all the inscribed
square-like quadrilaterals have sidelengths converging to zero, so this approach may yet be pos-
sible. However, this line of attack has been more or less obvious from the start, and nobody has
managed to construct such an argument in the past century.
Our considerably more modest goal in this paper is to rule out small square-like quadrilaterals
using local, rather than global, data about the limit curve, and in this way to extend our results to
the class of curves of ﬁnite total curvature without cusps (FTCWC). In Section 3, we review the
deﬁnition of what it means for a curve to be of ﬁnite total curvature, and explore what it means for a
sequences of curves to converge uniformly in position, arclength and total curvature (Deﬁnition 4).
As well as allowing us to resolve Conjecture 1, the appeal of this choice of regularity class is largely
that the class of curves of ﬁnite total curvature is a well-understood space (cf. [36]).

SQUARE-LIKE QUADRILATERALS INSCRIBED IN EMBEDDED SPACE CURVES 3

Our argument is completed in three parts in Section 4. First, we show that each embedded curve
γ in FTCWC has no inscribed square-like quadrilaterals with side length smaller than a positive
constant, denoted by π-d(γ). Next, we show that if there is a sequence of curves γi converging
to γ in position, arclength and total curvature, and π-d(γ) > 0, then π-d(γi) > 0 too. Finally,
we take any FTCWC embedding γ of S1 in Rn. We approximate γ by a sequence of smooth
FTC embeddings γi of S1 in Rn, each of which has an odd number of square-like quadrilaterals.
The ﬁrst two steps then imply that the corresponding sequence of square-like quadrilaterals has a
convergent subsequence with limit a square-like quadrilateral with sidelength at least π-d(γ). This
give us our main result in Theorem 11: Any embedding of S1 in Rn that is in FTCWC has an
inscribed square-like quadrilateral.
One immediate consequence of Theorem 11 is that we resolve the square-peg problem for (pla-
nar) Jordan curves which are in FTCWC. How does this regularity class compare to the other
solutions of the square-peg problem? Stromquist [35] and Matschke [22, 23] give local conditions
for planar curves that are weaker than ours. However, unlike our results, they do not discuss em-
beddings of circles in Rn for n > 2. Tao [37] gives a different regularity condition. His condition
is for Jordan curves which are the union of two Lipschitz graphs that agree at the endpoints, and
whose Lipschitz constants are strictly less than one. Such curves might be thought of intuitively as
“vertically star-like”. Tao’s class of curves and the class of FTCWC curves intersect one another,
but neither class of curves fully contains the other.

2. TOPOLOGY AND SQUARE-LIKE QUADRILATERALS

We use compactiﬁed conﬁguration spaces and multijet transversality in [3] to prove that there is
a dense family of smoothly embedded circles in Rn, each of which has an odd number of inscribed
square-like quadrilaterals.

Deﬁnition 2. A square-like quadrilateral in Rn is a quadrilateral pqrs with equal sides (|pq| =
|qr| = |rs| = |sp|) and equal diagonals (|pr| = |qs|). The set of all square-like quadrilaterals in
Rn is denoted by Slq.

The structure of Slq is discussed in detail in [3]. We observe that when n = 2, a square-like
quadrilateral is a square. When n ≥ 3, a square-like quadrilateral is a tetrahedron, and is also
known as a tetragonal disphenoid
2. In [3], we prove the following.

Theorem 3 (See Theorem 35 [3]). Take any smooth embedding of a curve γ : S1 ↪→ Rn. Then there
is a C∞-open neighborhood of γ in C∞(S1, Rn), in which there is, for all m, a Cm-dense set of
smooth embeddings γ′ : Sl ↪→ Rn, each of which has an odd, ﬁnite set of inscribed square-like
quadrilaterals

In order to fully appreciate Theorem 3, we recall the topology of the spaces we are working in.
In general, for manifolds M and N , the space C∞(M, N ) has the Whitney C∞-topology (see for
instance [13]). The sets of the form
 N m(f ; (U, φ), (V, ψ), δ)

2By deﬁnition, a tetragonal disphenoid is a tetrahedron with four congruent isosceles triangle faces.

4 JASON CANTARELLA, ELIZABETH DENNE, AND JOHN MCCLEARY

give a subbasis for the Whitney Cm-topology on Cm(M, N ) (where m is ﬁnite). This subbasis is
the subset of functions g : M → N that are smooth, and for coordinate charts φ : (U ′ ⊂ M ) →
(U ⊂ Rm) and ψ : (V ′ ⊂ N ) → (V ⊂ Rk) and K ⊂ U compact with g(φ(K)) ⊂ V ′, then, for
all s ≤ r, and all x ∈ φ(K),

∥Ds(ψgφ
−1)(x) − Ds(ψf φ
−1)(x)∥ < δ.

Here, DsF for a function F : (U ⊂ Rm) → (V ⊂ Rk) is the k-tuple of the sth homogeneous parts
of the Taylor series representations of the projections of F . Finally, the subspace C∞(M, N ) has
the Whitney C∞-topology by taking the union of all subbases for all m ≥ 0.

3. FINITE TOTAL CURVATURE CURVES

We recall some standard facts about curves of ﬁnite total curvature (see for instance [36, 40]).
The total curvature of a curve is the supremum of the total turning angles of all polygons inscribed
in the curve. If this supremum is ﬁnite, we say the curve has ﬁnite total curvature or is in FTC.
Curves in FTC have a number of desirable properties. They are always rectiﬁable, and so can
be parametrized by arclength. They are almost everywhere differentiable, and a curve in FTC
has one-sided tangent vectors at every point. In fact, these tangents differ only at countably many
corner points. There is a Radon measure κ on every γ in FTC whose mass on any open subarc of
γ is the total curvature (in the above sense) of the subarc. This measure has a countable number of
atoms at corners of the curve γ. The mass of each atom is the turning angle between these vectors.
If this turning angle is π, we say the corner is a cusp.
Since FTC curves have a second derivative (at least weakly) it is natural to want to approximate
them “in C2” by smooth curves. Unfortunately, this is not quite possible. Note that the tangent
indicatrix to an FTC curve has gaps at the corners of the curve, while the tangent indicatrix of a
smooth curve forms a continuous curve on Sn−1. Thus the tangent vectors to a sequence of smooth
curves approximating an FTC curve can’t converge to tangents of the FTC curve near a corner of
the FTC curve. However, we can come very close to a C2 approximation in the following sense:

Deﬁnition 4. Suppose γ : R → Rn is a curve in FTC. Let Len(γ, a, b) be the length of the arc of
γ between γ(a) and γ(b) and κ(γ, a, b) be the total curvature of this arc. We say that a sequence of
ﬁnite total curvature curves γi : R → Rn approximate γ uniformly in position, arclength, and total
curvature if there are parametrizations of the γi so that for each ϵ > 0 there exists an N so that for
all i > N , we have the following:
(1) For any a, |γi(a) − γ(a)| < ϵ.
(2) For any [a, b], |Len(γi, a, b) − Len(γ, a, b)| < ϵ.
(3) For any [a, b], |κ(γi, a, b) − κ(γ, a, b)| < ϵ.

Proposition 5. Any FTC curve γ may be approximated uniformly in position, arclength, and total
curvature by smooth FTC curves γi.

Proof. This is an assembly of standard results about FTC curves. If we inscribe polygons with
vertices equally spaced by arclength in γ, and parametrize them compatibly (so that the vertices
have the same parameter values on γ and on each polygon), the polygons converge uniformly in

SQUARE-LIKE QUADRILATERALS INSCRIBED IN EMBEDDED SPACE CURVES 5

position and total curvature (cf. Lemma 4.2 of [20]) and are all ﬁnite-total curvature curves (since
their total curvatures are bounded by that of γ).
To see that they converge uniformly in arclength, ﬁx an arc (a, b) of γ, and observe that the
corresponding arcs of the γi have bounded total curvature, and converge to the arc of γ in Fr´echet
distance because they converge in position. Then use Theorem 5.1 of [40] (see also [5]) which
states that for any rectiﬁable curves K, L,

| Len(K) − Len(L)| ≤ δ(K, L)(π max{TC(K), TC(L)} + 2)

where δ(K, L) is the Fr´echet distance between K and L. Note that this theorem is not obvious: it
says that the standard examples of curves which converge in Fr´echet distance but not in arclength,
such as a stairstep curve converging to the diagonal of a square, must all have unbounded total
curvature.
To ﬁnish the proof, smooth each polygon by rounding off corners– the smooth curves have the
same total curvature as the polygons (and are hence FTC) and are close to the original polygons in
position, arclength, and total curvature, as required. □

4. CURVATURE π IS REQUIRED TO HAVE AN INSCRIBED SQUARE-LIKE QUADRILATERAL

The deﬁnition of total curvature means that the total curvature of any curve γ, is at least as large
as the total curvature of any polygonal curve inscribed in γ. We can apply this to curves which
have an inscribed square-like quadrilateral pqrs.
Notice that if a square-like quadrilateral pqrs is inscribed in an arc of γ, the total curvature of
the arc γpqrs must be at least as large as the total curvature (or total turning angle) of the inscribed
open square-like quadrilateral pqrs. Here, by open square-like quadrilateral (polygon), we mean
the open arc σpqrs (or pqrs without side sp). We compute the the total curvature of the open
square-like quadrilateral σpqrs by computing the turning angle at vertices q and r. When pqrs is
a planar square, we see the open square has total turning angle π. We now prove that the turning
angle is at least π if pqrs is an open square-like quadrilateral.

Lemma 6. Any square-like quadrilateral pqrs has the property that the open square-like quadri-
lateral σpqrs has total curvature κ(σpqrs) ≥ π, with equality if and only if pqrs is a planar square.

Proof. Consider the square-like quadrilateral found in Figure 2 where pqrs has equal sides pq, qr,
rs, and sq and equal diagonals pr and qs. We may assume without loss of generality that the sides
have length 1. We construct the midpoint t of qs. Since △pqs is isosceles, we can conclude that
∠ptq is right and that ∠qpt = ∠spt = θ. We then have pt = cos θ and qt = sin θ. Further, since
qs = pr, we have pr = 2 sin θ.
Since pq = rq, ps = rs, and qs is a common side, we have △rqs ∼= △pqs. Thus ∠qrs =
∠qps = 2θ and, after joining r to t, we ﬁnd rt = cos θ as above. So by the triangle inequality (on
△ptr) we have pt + tr ≥ pr, or 2 cos θ ≥ 2 sin θ.
This means that θ ≤ π/4, and θ = π/4 if and only if t is on the line pr. In this case pqrs is planar
(and hence it is a square). Now, at vertices q and r, the turning angle of pqrs is π − 2θ. Thus the
total turning angle of the open square-like quadrilateral σpqrs is 2π − 4θ ≥ π, as desired. □

6 JASON CANTARELLA, ELIZABETH DENNE, AND JOHN MCCLEARY

p

q
 s
 r

cos θ

sin θ

t θ

FIGURE 2. The open arc σpqrs of the square-like quadrilateral pqrs shown has
total curvature given by 2π − 4θ. We observe, however, that pt has length cos θ
and qt has length sin θ, while 2qt = qs = pr is less than 2pt. Thus cos θ ≥ sin θ
and θ ≤ π/4.

4.1. On a ﬁnite-total curvature curve without cusps, short enough arcs have small curvature.
In this section we will restrict our attention to curves with ﬁnite total curvature, but without cusps.
We say such a curve is in FTCWC. Recall that a cusp is a point on a curve with turning angle π.
What is our goal? We will take an embedded curve in FTCWC, and a sequence of smooth FTC
embedded curves γi converging to γ. We will prove that there exists a constant c > 0 so that no
square-like quadrilateral inscribed in γi has sidelength less than c.

Deﬁnition 7. We deﬁne the π-distance of an FTC curve γ, denoted π-d(γ). The value ℓ is an
admissible distance bound if every open subarc (a, b) of γ with |γ(a) − γ(b)| < ℓ has κ(γ, a, b) <
π. Then π-d(γ) = sup
ℓ is admissible ℓ = inf
ℓ is inadmissible ℓ.

Note that if ℓ is inadmissible, then there is some subarc (a, b) with |γ(a) − γ(b)| < ℓ, but
κ(γ, a, b) ≥ π. The point of π-d(γ) is that it provides a lower bound on the side length of a
square-like quadrilateral inscribed in γ.

Lemma 8. Any square-like quadrilateral inscribed in an FTC curve γ has sidelength greater than
or equal to π-d(γ).

Proof. Let pqrs be an inscribed square-like quadrilateral in γ, and consider the open polygon
σpqrs which has end-to-end distance |γ(p) − γ(s)|. By Lemma 6, the square-like quadrilateral is
an inscribed open polygon with total curvature at least π. Thus κ(γ, p, s) ≥ π. This means that
|γ(p) − γ(s)| is an inadmissible distance bound, and hence it is at least π-d(γ), as desired. □

We now want to show that an embedded curve in FTCWC is the limit of a sequence of smooth
curves with inscribed square-like quadrilaterals with side lengths uniformly bounded above zero.
We proceed in two steps: ﬁrst we will show that γ itself has π-d bounded above, then that π-d
behaves nicely under the sort of convergence of curves we introduced above in Deﬁnition 4.

Lemma 9. If γ is an embedded curve in FTCWC, then π-d(γ) > 0.

SQUARE-LIKE QUADRILATERALS INSCRIBED IN EMBEDDED SPACE CURVES 7

Proof. Suppose not. Since π-d(γ) = 0, there is a sequence of inadmissible ℓi → 0. So there
exists a collection of open subarcs Ai of γ whose endpoints ai, bi have |γ(ai) − γ(bi)| → 0, while
κ(γ, ai, bi) ≥ π. Passing to a subsequence where ai → a and bi → b, we see that γ(a) = γ(b),
and hence a = b because γ is embedded.
Now as the Ai approach {a}, their total curvature κ(Ai) ≥ π. Since γ is compact, we may
pass to a subsequence of Ai that are nested and converge to a point p. Since κ is an outer-regular
measure, this means that κ(p) ≥ π. Since κ(p) is a turning angle, it is always ≤ π. Thus κ(p) = π
and p is a cusp point, contradicting our assumption that γ was in FTCWC. □

Since π-d is deﬁned by lengths, distances, and curvatures, we can expect it to behave nicely as
we take limits in the sense of Deﬁnition 4.

Proposition 10. If γi → γ uniformly in position, arclength, and total curvature in the sense of
Deﬁnition 4, and π-d(γ) > 0, then lim inf i→∞ π-d(γi) > 0.

Proof. Suppose not. For any ϵ > 0, there must be inﬁnitely many γi with π-d(γi) < ϵ. Each γi
contains a subarc (ai, bi) with |γi(ai) − γi(bi)| < ϵ, but κ(γi, ai, bi) ≥ π. By compactness, we can
assume that we have passed to a subsequence where ai → a and bi → b.
Now by convergence in position, |γ(a) − γ(b)| ≤ ϵ. Let us expand the open arc (a, b) of γ
slightly to an open subarc (a′, b′) with |γ(a′) − γ(b′)| ≤ 3ϵ, say, and again pass to a subsequence
where (ai, bi) ⊂ (a′, b′) for all i. Now for any δ > 0, by convergence in total curvature, for large
enough i we have ∣
∣κ(γ, a′, b
′) − κ(γi, a
′, b
′)∣
∣ < δ
so κ(γ, a′, b
′) > κ(γi, a
′, b
′) − δ ≥ κ(γi, ai, bi) − δ ≥ π − δ.
where κ(γi, a′, b′) ≥ κ(γi, ai, bi) because (ai, bi) ⊂ (a′, b′). Since δ was arbitrary, this proves that
κ(γ, a′, b′) ≥ π.
However, this means that 3ϵ > |γ(a′) − γ(b′)| is an inadmissible distance bound for γ, and
hence that π-d(γ) < 3ϵ. Since ϵ was arbitrary, this proves that π-d(γ) = 0, providing the required
contradiction. □

We are ready to construct an inscribed square-like quadrilateral on any FTCWC curve. We have
done all the hard work above; it remains only to assemble the component pieces.

Theorem 11. Let γ : S1 ↪→ Rn be an embedding of S1 in Rn. If γ is in FTCWC, then γ has an
inscribed square-like quadrilateral.

Proof. First, we may approximate γ by a sequence of smooth FTC curves γi with convergence in
position, arclength, and total curvature by Proposition 5. Note that since γi are smooth, they are
automatically in FTCWC. By making a C2-small perturbation of each γi, we may assume by
Theorem 3 that each γi contains at least one inscribed square-like quadrilateral3. Since our pertur-
bations were C2-small, the sequence of curves γi still enjoys ﬁnite total curvature and converges to
γ in position, arclength, and total curvature.

3Theorem 3 says there is a C ∞-open neighborhood of each γi in which there is, for all m (in particular m = 2), a
C m-dense set of embeddings, each with an odd number of square-like quadrilaterals.

8 JASON CANTARELLA, ELIZABETH DENNE, AND JOHN MCCLEARY

By Lemma 9 and Proposition 10, there is a constant c > 0 so that we may pass to a subsequence
of γi, each of which has π-d(γi) > c. By Lemma 8 the inscribed square-like quadrilateral on each
γi has sidelength at least c. This is the crucial point in the proof: by bounding the sidelengths of
these square-like quadrilaterals from below, we have ensured that they do not shrink away as we
approach the limiting curve γ.
From here, the argument is standard. We may assume that the inscribed square-like quadrilat-
erals in the γi lie in a compact subset of Slq, and hence that they have a convergent subsequence.
The limit of this subsequence is a square-like quadrilateral inscribed in the limit curve γ. □

Since C2 smooth curves are in FTCWC, we immediately ﬁnd:

Corollary 12. Let γ : S1 ↪→ Rn be an embedding of S1 in Rn. If γ is C2-smooth, then γ has an
inscribed square-like quadrilateral.

Since square-like quadrilaterals are squares in the plane, then we have also shown that all em-
beddings of the circle in the plane which are in FTCWC or which are C2-smooth have an inscribed
square.
Note that we have lost something here. Our proof assumed that the limiting curves γi had an odd
number of square-like quadrilaterals. It is entirely possible that multiple square-like quadrilaterals
coincide on the limiting curve γ, so the count of inscribed square-like quadrilaterals may no longer
be odd. Indeed there are explicit examples [29, 31, 39] which show that for any n, there are curves
with n inscribed squares.
Also note that there exist smooth curves that are not FTC; these do not have corners but have
spirals where curvature diverges. For these curves, Theorem 3 still holds, but we can not con-
clude from Theorem 11 that there is at least one square-like quadrilateral. (The spirals prevent the
arguments of Proposition 10 from holding.)
Finally, we still do not know if Conjecture 1 holds for continuous embeddings of circles in Rn.
We have the intuition that if the square-peg problem holds true for continuous Jordan curves, then
Conjecture 1 will hold true for continuous embeddings as well. Proving either conjecture needs
new techniques which have yet to be developed.

ACKNOWLEDGEMENTS

The authors would like to ﬁrst thank Gerry Dunn who introduced us to the problem. We would
also like to thank the people who have discussed the problem with us over the years: Jordan Ellen-
berg, Richard Jerrard, Rob Kusner, Benjamin Matschke, Igor Pak, Strashimir Popvassiliev, John
M. Sullivan, Cliff Taubes, and Gunter Ziegler.

REFERENCES

[1] Arseniy Akopyan and Sergey Avvakumov. Any cyclic quadrilateral can be inscribed in any closed convex smooth
curve. Forum Math. Sigma, 6:Paper No. e7, 9, 2018.
[2] Jai Aslam, Shujian Chen, Florian Frick, Sam Saloff-Coste, Linus Setiabrata, and Hugh Thomas. Splitting loops
and necklaces: variants of the square peg problem. Forum Math. Sigma, 8:Paper No. e5, 16, 2020.
[3] Jason Cantarella, Elizabeth Denne, and John McCleary. Conﬁguration Spaces, Multijet Transversality, and the
Square-Peg Problem, Preprint 2021.
[4] C. M. Christensen. A square inscribed in a convex ﬁgure. Mat. Tidsskr. B, 1950:22–26, 1950.

SQUARE-LIKE QUADRILATERALS INSCRIBED IN EMBEDDED SPACE CURVES 9

[5] David Cohen-Steiner and Herbert Edelsbrunner. Inequalities for the curvature of curves and surfaces. Found. Com-
put. Math., 7(4):391–404, 2007.
[6] Arnold Emch. Some Properties of Closed Convex Curves in a Plane. Amer. J. Math., 35(4):407–412, 1913.
[7] Arnold Emch. On the Medians of a Closed Convex Polygon. Amer. J. Math., 37(1):19–28, 1915.
[8] Arnold Emch. On Some Properties of the Medians of Closed Continuous Curves Formed by Analytic Arcs. Amer.
J. Math., 38(1):6–18, 1916.
[9] Orrin Frink and C. S. Ogilvy. Advanced Problems and Solutions: Solutions: 4325. Amer. Math. Monthly,
57(6):423–424, 1950.
[10] Joshua Evan Greene and Andrew Lobb. Cyclic quadrilaterals and smooth Jordan curves, 2020.
[11] H. Brian Grifﬁths. The topology of square pegs in round holes. Proc. London Math. Soc. (3), 62(3):647–672, 1991.
[12] H. Guggenheimer. Finite sets on curves and surfaces. Israel J. Math., 3:104–112, 1965.
[13] Morris W. Hirsch. Differential topology, volume 33 of Graduate Texts in Mathematics. Springer-Verlag, New York,
1994. Corrected reprint of the 1976 original.
[14] Cole Hugelmeyer. Every smooth Jordan curve has an inscribed rectangle with aspect ratio equal to √
3, 2018.
[15] Cole Hugelmeyer. Inscribed rectangles in a smooth Jordan curve attain at least one third of all aspect ratios, 2019.
[16] R P Jerrard. Inscribed squares in plane curves. Trans. Amer. Math. Soc., 98:234–241, 1961.
[17] R. N. Karas¨ev. Topological methods in combinatorial geometry. Uspekhi Mat. Nauk, 63(6(384)):39–90, 2008.
[18] Elizabeth Kelley. A Combinatorial Approach to the Inscribed Square Problem. https://www-users.math.
umn.edu/˜kell1642/kelley_thesis.pdf, 2015. Honors Thesis, Harvey Mudd College. Accessed: Feb
22, 2021.
[19] Victor Klee and Stan Wagon. Old and new unsolved problems in plane geometry and number theory. The Dolciani
Mathematical Expositions, 11. Mathematical Association of America, 1991.
[20] J. Li and T. J. Peters. Isotopic convergence theorem. J. Knot Theory Ramiﬁcations, 22(3):1350012, 18, 2013.
[21] V V Makeev. On quadrangles inscribed in a closed curve and the vertices of the curve. Zap. Nauchn. Sem. S.-
Peterburg. Otdel. Mat. Inst. Steklov. (POMI), 299(Geom. i Topol. 8):241–251, 331, 2003.
[22] Benjamin Matschke. Equivariant topology methods in discrete geometry. PhD thesis, Freie Universit¨at, 2011.
[23] Benjamin Matschke. A survey on the square peg problem. Notices Amer. Math. Soc., 61(4):346–352, 2014.
[24] Benjamin Matschke. Quadrilaterals inscribed in convex curves, 2020.
[25] Mark J. Nielsen and S. E. Wright. Rectangles inscribed in symmetric continua. Geom. Dedicata, 56(3):285–297,
1995.
[26] Igor Pak. The discrete square peg problem, 2008.
[27] Igor Pak. Lectures on Discrete and Polyhedral Geometry. Free online text. 2010.
[28] Ville H. Pettersson, Helge A. Tverberg, and Patric R. J. ¨Osterg˚ard. A note on Toeplitz’ conjecture. Discrete Comput.
Geom., 51(3):722–728, 2014.
[29] Strashimir G. Popvassilev. On the number of inscribed squares of a simple closed curve in the plane. arXiv.org,
0810:4806, October 2008.
[30] Feli´u Sagols and Ra´ul Mar´ın. The inscribed square conjecture in the digital plane. In Combinatorial image analysis,
volume 5852 of Lecture Notes in Comput. Sci., pages 411–424. Springer, Berlin, 2009.
[31] Feli´u Sagols and Ra´ul Mar´ın. Two discrete versions of the inscribed square conjecture and some related problems.
Theoret. Comput. Sci., 412(15):1301–1312, 2011.
[32] L. G Schnirel’man. On certain geometrical properties of closed curves. (russian). Uspehi Matem. Nauk, 10:34–44,
1944.
[33] Richard Evan Schwartz. Rectangle Coincidences and Sweepouts, 2018.
[34] Richard Evan Schwartz. A Trichotomy for Rectangles Inscribed in Jordan Loops, 2019.
[35] Walter Stromquist. Inscribed squares and square-like quadrilaterals in closed curves. Mathematika, 36(2):187–197
(1990), 1989.
[36] John M. Sullivan. Curves of ﬁnite total curvature. In Discrete differential geometry, volume 38 of Oberwolfach
Semin., pages 137–161. Birkh¨auser, Basel, 2008.
[37] Terence Tao. An integration approach to the Toeplitz square peg problem. Forum Math. Sigma, 5:Paper No. e30,
63, 2017.

10 JASON CANTARELLA, ELIZABETH DENNE, AND JOHN MCCLEARY

[38] Otto Toeplitz. Ueber einige aufgaben der analysis situs. Verhandlugen Der Schwizerischen Naturafoschenden
Gesellshaft in Solothurn, 4:197, 1922.
[39] Wouter van Heijst. The algebraic square peg problem, 2014.
[40] A. C. M. van Rooij. The total curvature of curves. Duke Math. J., 32:313–324, 1965.
[41] Konrad Von Zindler. ¨Uber konvexe Gebilde. Monatsh. Math. Phys., 31(1):25–56, 1921.

APPENDIX A. A BRIEF HISTORY OF THE SQUARE-PEG PROBLEM

Let us recall the square-peg problem, originally due to O. Toeplitz [38].

Conjecture 13. Let γ : S1 ↪→ R2 be a Jordan curve (a continuous, simple, closed curve in plane).
Then γ(S1) has an inscribed square.

While Conjecture 13 is still open, here have been many attempts made to solve it. The interested
reader can ﬁnd a number of surveys of the history of these attempts, for example [17, 23, 27]. This
Appendix gives an overview of this history. We note that the majority of the existing solutions to
Conjecture 13 require that the Jordan curve be sufﬁciently regular.
In 1913, A. Emch [6, 7, 8], then K. Von Zindler [41] in 1921, and C.M. Christensen [4] in 1950,
all proved the square-peg problem for convex closed curves.
In 1929, L.G. Schnirel’man [32] (published in 1944), and then H. Guggenheimer [12] in 1965,
both proved the square-peg problem for curves of continuous curvature of bounded variation (a
class slightly larger than C2-smooth).
In 1961, R. Jerrard [16] showed that all analytic curves must have an odd or inﬁnitely many in-
scribed squares. Earlier, O. Frink, C.S. Ogilvy [9] in 1950 proved the square-peg problem assuming
some kind of smoothness (though this was not stated explicitly).
In 1989, W. Stromquist [35] proved the square-peg problem for C1-smooth curves, as well as
ones that are locally monotone4. The latter class includes curves that are convex, or are polygonal,
or piecewise C1-smooth without cusps, or even certain curves which are nowhere differentiable.
In 1990, H.B. Grifﬁths [11] proved the square-peg problem for C2-smooth (or higher); though
this paper appears to contain serious errors (see [3, 22]).
In 1991, V. Klee and S. Wagon [19] proved the square-peg problem or curves which star-like or
symmetric around a point z (speciﬁcally, where every line through z meets the curve in exactly two
points). A little later, in 1995, M.J. Nielsen and S.E. Wright [25] proved the square-peg problem
for curves which are centrally symmetric though a point, or symmetric through reﬂection across a
line. More recently in 2015, E. Kelley (a student of Francis Su) wrote an honors thesis [18] where
she explicitly showed that a square is inscribed in the Koch snowﬂake curve (a centrally symmetric
curve).
In 2008, I. Pak [26] proved the square-peg problem for generic piecewise linear curves (with an
elementary proof).
In 2011, B. Matschke [22, 23] proved the square-peg problem for curves which do not contain
small trapezoids of a certain type. It turns out that such curves form an open and dense subset of the
space of embeddings S1 ↪→ R2 with respect to the compact-open topology. Matschke also gives
one of the few known global conditions on curves guaranteeing the existence of squares. Here, the

4Locally monotone means that if every point p of the curve has a neighborhood U (p) and a direction n(p) such that
no chord of the curve is contained in U (p) and parallel to n(p).

SQUARE-LIKE QUADRILATERALS INSCRIBED IN EMBEDDED SPACE CURVES 11

curves must be contained in an annulus with a certain ratio between the outer and inner radii, and
which have a nontrivial winding number around the center of the annulus. In particular, this global
condition does not require that the continuous curves are injective.
In 2014 (revised 2021), J. Cantarella, E. Denne, and J. McCleary [3] proved that an open dense
set (with respect to the Whitney C∞ topology) of C∞-smooth embeddings of S1 in Rn have an
odd number of squares.
In 2017, T. Tao [37] proved the square-peg problem for curves which are the union of two
Lipschitz graphs that agree at the endpoints, and whose Lipschitz constants are strictly less than
one. Such curves might be thought of intuitively as “vertically star-like”.
Finally, this paper shows that the square-peg problem is proved for curves which are of ﬁnite
total curvature and without cusps.
There are other closely related versions of the square-peg problem. For example, there are two
slightly different discrete versions of the square-peg problem. The ﬁrst, described by F. Sagols and
R. Mar´ın [30, 28] in 2009, is where the vertices of polygonal Jordan curves are assumed to lie on a
planar integer lattice grid (Z × R) ∪ (R × Z). They then examine what kind of lattice curves have
inscribed squares with integer coordinates. In 2014, V.H. Pettersson et al. [31] looked at curves
where both vertices and edges lie on the planar integer lattice. They used computational methods
to show that for n ≤ 13, the side length of the largest square with edges on an n × n grid is at least
1/
√2 times the side length of the largest axis-aligned square contained in the curve.
There are also a number of results which count the number of squares. While several results
[3, 16] show that we expect there to be generically an odd number of squares, we can not expect
this in general. Indeed there are smooth convex curves (Popvassiliev [29]) and piecewise linear
curves (Sagols and Mar´ın [31]) which have exactly n inscribed squares for any n. In addition,
W. van Heijst [39] proved that any real algebraic curve of degree n in R2 inscribes either inﬁnitely
many squares or at most n4−5m2+4m/4 squares.

MATHEMATICS DEPARTMENT, UNIVERSITY OF GEORGIA, ATHENS GA 30602
Email address: jason.cantarella@uga.edu

MATHEMATICS DEPARTMENT, WASHINGTON & LEE UNIVERSITY, LEXINGTON VA 24450
Email address: dennee@wlu.edu

MATHEMATICS & STATISTICS DEPARTMENT, VASSAR COLLEGE, POUGHKEEPSIE NY 12604
Email address: mccleary@vassar.edu
