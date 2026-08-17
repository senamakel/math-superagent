<!-- source: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/FCA46BEF322C4B8A02C2C47270177DF5/S0008414X00031758a.pdf/the-geometry-of-quadratic-differential-systems-with-a-weak-focus-of-third-order.pdf | converted from PDF -->

Canad. J. Math. Vol. 56 (2), 2004 pp. 310–343

The Geometry of
Quadratic Differential Systems
with a Weak Focus of Third Order

Jaume Llibre and Dana Schlomiuk

Abstract. In this article we determine the global geometry of the planar quadratic differential systems
with a weak focus of third order. This class plays a signiﬁcant role in the context of Hilbert’s 16-th
problem. Indeed, all examples of quadratic differential systems with at least four limit cycles, were
obtained by perturbing a system in this family. We use the algebro-geometric concepts of divisor
and zero-cycle to encode global properties of the systems and to give structure to this class. We give
a theorem of topological classiﬁcation of such systems in terms of integer-valued afﬁne invariants.
According to the possible values taken by them in this family we obtain a total of 18 topologically
distinct phase portraits. We show that inside the class of all quadratic systems with the topology of the
coefﬁcients, there exists a neighborhood of the family of quadratic systems with a weak focus of third
order and which may have graphics but no polycycle in the sense of [15] and no limit cycle, such that
any quadratic system in this neighborhood has at most four limit cycles.

1 Introduction, Brief Review of the Literature and
Informal Outline of Results

The complete characterization of the phase portraits for real planar quadratic vector
ﬁelds is not known, and attempting to classify these systems, which occur rather often
in applications, is quite a complex task. This family of systems depends on twelve
parameters, but due to the group action of real afﬁne transformations and positive
time rescaling, the class ultimately depends on ﬁve parameters. Bifurcation diagrams
were constructed for some algebraic and semialgebraic subsets of this class, see for
example [4, 5, 8, 10, 25, 33, 41, 39, 50, 54]. With the exception of some articles (for
example [50]) the classiﬁcations of systems were done in terms of local charts and
inequalities on the coefﬁcients of the systems written in these charts. This line of
work follows the program stated by Coppel in his nice short article which appeared
in 1966 (cf. [11]). Coppel thought that the phase portraits of quadratic systems could
be characterized by means of algebraic inequalities on the coefﬁcients. We now know
that algebraic inequalities would not be sufﬁcient; analytic as well as non-analytic
ones (cf. references [37] and [14, pp. 118–119]) need to be taken into consideration.
We would also want to see that classiﬁcations be done not in terms of coordinate
charts as in previous works but in more intrinsic terms, to reveal the geometry of the

Received by the editors October 12, 2001; revised March 13, 2003.
The ﬁrst author is partially supported by a MCYT grant number BFM 2002-04236-C02-02 and by a
CICYT grant number 2001SGR 003173, and the second is partially supported by NSERC and by Quebec
Education Ministry, and was also supported by a grant from the Ministerio de Educaci ´on y Cultura of
Spain.
AMS subject classiﬁcation: Primary: 34C40, 51F14; secondary: 14D05, 14D25.
c⃝Canadian Mathematical Society 2004.

310

https://doi.org/10.4153/CJM-2004-015-2 Published online by Cambridge University Press

Quadratic Differential Systems 311

systems. Since it is expected that quadratic differential systems will yield more than
two thousand phase portraits, tools for organizing this maze of phase portraits need
to be introduced.
The phase portraits are classiﬁed by using the topological equivalence [48]. Just
as homotopy groups could be used to distinguish topological spaces, we need to have
invariants to distinguish between phase portraits. A complete set of invariants was
given by Markus for C 1 systems on the plane (cf. [28], also [31]). He associated to
every C 1 system its separatrix conﬁguration and he showed that two C 1 systems are
topologically equivalent if and only if their corresponding separatrix conﬁgurations
are topologically equivalent. The separatrix conﬁguration is formed by all the sepa-
ratrices of the system, together with an orbit for each open connected component of
the complement in the plane of the union of all separatrices. Each of these compo-
nents is called a canonical region. The separatrix conﬁgurations could still be rather
complex, and criteria to distinguish them are needed.
Global concepts introduced in [34, 42] are used here for classifying the family of
quadratic differential systems we study. These geometric concepts are: zero-cycles of
the afﬁne or projective plane, real or complex, and divisors corresponding to the line
at inﬁnity. We associate to these, integer-valued global afﬁne invariants which help us
distinguish (and sometimes even identify) separatrix conﬁgurations. We apply these
ideas to the particular class QW3 of all quadratic systems with a weak focus of third
order. In the end we obtain phase portraits of this family and their classiﬁcation up
to topological equivalence. For a large part of the parameter space this classiﬁcation
is intrinsic, i.e., it is independent of the normal form for the systems considered since
it only depends on integer-valued afﬁne invariants which could be calculated, as we
indicate in Section 10, IV, for any presentation of the systems.
Since a weak focus may produce up to three limit cycles in a quadratic pertur-
bation of the system, the study of this class is of interest in itself in the context of
Hilbert’s 16-th problem. This problem asks for the maximum H(m) (the Hilbert
number) of the numbers of limit cycles which real polynomial vector ﬁelds deﬁned
by polynomials of maximum degree m could have [21]. The nature of the problem is
global in two ways: we are interested in the whole class of polynomial vector ﬁelds of
a maximum ﬁxed degree m and at the same time in the behavior on the whole plane
of phase curves of each individual member of this family. The problem is still un-
solved, even for the case m = 2. The most important result of a global nature is the
individual ﬁniteness theorem proved independently in the late 1980’s by Ecalle [17]
and Il’yashenko [22]. This theorem says that each ﬁxed polynomial vector ﬁeld has
a ﬁnite number of limit cycles. This result was stated as a theorem by Dulac [13] in
1923 but the proof Dulac gave was ﬂawed. If we consider the family of all quadratic
vector ﬁelds, it is not even proved that H(2) is a ﬁnite number. There is a program
under way (cf. [15]) to prove this. The program proposes to show that all the 121
graphics listed in [15], which intervene in the problem of proving the ﬁniteness of
H(2), have ﬁnite cyclicity (cf. [36]). Because in over one hundred years since Hilbert
stated the problem, no example was found where we can prove that more than four
limit cycles exist, it is not only conjectured that H(2) is ﬁnite but also that H(2) = 4.
All known examples of quadratic vector ﬁelds having at least four limit cycles were
obtained by perturbing a quadratic vector ﬁeld with a weak focus of third order, a

https://doi.org/10.4153/CJM-2004-015-2 Published online by Cambridge University Press

312 Jaume Llibre and Dana Schlomiuk

good motivation for understanding this family.
Assuming the proof of the ﬁniteness of H(2) were done, we would still know very
little about the geometry of the systems in this class or of the class itself. For this
reason along with a search for a proof of the ﬁniteness part it is necessary to advance
the knowledge on this class, and the present work is a step in this direction. For a
general framework of study of the class of all quadratic differential systems we refer
to the article of Roussarie and Schlomiuk [38].
The work is organized as follows. In Section 2 we describe the normal form for
the family of systems we consider. Although they are an essential tool for performing
calculations, it is necessary to break away from speciﬁc normal forms and as much as
possible, state results which are applicable to any speciﬁc presentation of the systems.
As we explain in later sections, for most phase portraits of the classiﬁcation, this is
possible.
For the study of real planar polynomial vector ﬁelds two compactiﬁcations are
used. In Section 3 we describe very brieﬂy the Poincar´e compactiﬁcation on the 2-
dimensional sphere. We also introduce two foliations with singularities on the real
and complex projective planes, associated to the real polynomial vector ﬁelds. Al-
though a different compactiﬁcation, the real foliation with singularities on the real
projective plane is closely related to the Poincar´e compactiﬁcation on the sphere. The
two polynomials deﬁning a real planar polynomial vector ﬁeld also deﬁne a complex
vector ﬁeld when the variables range over C. To this complex vector ﬁeld on C2 we
can associate a compactiﬁcation by passing to the foliation with singularities on the
complex projective plane CP2. This foliation turns out to be very important for the
study of the real vector ﬁeld.
In Section 4, intersection numbers are attached to the singularities of the complex
foliation with singularities associated to a real vector ﬁeld.
In Section 5, we introduce some concepts which encode globally the information
about singularities. They are zero-cycles of the plane and divisors (cf. [18]) on the line
at inﬁnity and they are applied in Section 6 to the speciﬁc study of the class QW3 of
quadratic systems with a weak focus of third order. Some singularities are composite
or multiple, arising from collision of neighboring points which are singularities in a
perturbation of the system. We use the zero-cycles on both the real and the complex
projective planes and divisors on the line at inﬁnity to encode the multiplicities of all
the singular points, ﬁnite or inﬁnite. We also need to encode globally the information
on the topology of the phase portrait around each one of the singularities. This is
done by using in Proposition 10 of Section 6, the zero-cycle DI encoding globally the
indices of singularities in the real projective plane of the compactiﬁed systems. The
types of these divisors and zero-cycles and their degrees (as deﬁned in Section 5) are
afﬁnely invariant.
In Section 7 we list the basic theorems from the literature, and in particular the
properties of quadratic systems or of QW3, which are used in Section 8. We thus
mention two important results: the nonexistence of a limit cycle surrounding a weak
focus of third order (cf. [24]) and a recently obtained result afﬁrming that if a quad-
ratic system has limit cycles around two foci, then around one of them we cannot
have more than just one limit cycle (cf. [52, 53]). The main result of Section 7 is
Theorem 12 about the bifurcation diagram for the class QW3. To facilitate future

https://doi.org/10.4153/CJM-2004-015-2 Published online by Cambridge University Press

Quadratic Differential Systems 313

studies, its proof is here made much more explicit. An important fact coming out of
this proof is that roughly speaking the knowledge of portraits of nongeneric systems,
the systems with center (they are integrable in the quadratic case), yields in fact this
bifurcation diagram. This is an improvement over [2], [3] and [5]. Firstly because
of the use here of the projective plane as the parameter space, which allowed us to
gather the pieces of the bifurcation diagram in just one picture, in view of a sym-
metry possessed by the systems a half-disc. In each one of the previously mentioned
articles these pieces appear separately drawn. Viewing the changes in the phase por-
traits as parameters vary facilitates understanding global properties of this class. The
integer-valued invariants as deﬁned by us in Section 7 pointed out to us the errors in
the previous literature. In particular they allowed us to correct statements in [5], [2]
and [3] as we indicate in Sections 9 and 10.
In Section 8 we introduce a global invariant denoted by I, which classiﬁes the
phase portraits obtained for the systems in the class QW3 up to topological equiva-
lence. Theorem 14 shows clearly that for a large part of the parameter space, call it
here A, these phase portraits are uniquely determined (up to topological equivalence)
by the values of an invariant, J, depending only on the values of the above divisors
and zero-cycles. In this region A the bifurcation diagram is shown to be part of a real
algebraic set. For any value in A we have a phase portrait which has no limit cycle
and no graphic (cf. [15]). In the complement B of A in the parameter space we have
limit cycles or graphics. In B, J takes only two values and it cannot distinguish all
the phase portraits. New concepts are thus needed and we introduce them, yielding
the afﬁne invariant I. It is in B that a connected bifurcation curve G, part analytic,
part algebraic, occurs on the diagram of Figure 3. On G the systems do not have limit
cycles. G is the only subset in the parameter space where graphics occur; more pre-
cisely, for all points in G the systems have a unique graphic (which in two of the three
possible cases is a polycycle (cf. [15])) with two singularities, both at inﬁnity and with
two path curves, one of them part of the line at inﬁnity. We prove the existence and
analyticity of the curve G, and numerical computations determine the position of its
non-algebraic part with as high accuracy as we wish.
The region with limit cycles, where three distinct phase portraits occur, is bounded
by the curve G and by a line (a = 0, i.e., the vertical line of the diagram in Figure 2,
also in Figure 3) on which we have symmetric systems with two centers.
There is a difference between deﬁning invariants and actually being able to com-
pute them for any given presentation of the systems. We indicate in Section 10 how
part of the integer-valued invariants deﬁned here relate to the algebraic invariants
which in turn can be computed for any given particular chart in which the systems
may be presented.

2 Quadratic Vector Fields With a Weak Focus of Third Order

A singular point p of a planar vector ﬁeld X in R2 is a linear center if the eigenvalues of
its linear part, DX(p), are imaginary numbers, i.e., ±βi with β ∈ R\{0}. We say that
p is a center of X if p is an isolated singularity such that there exists a neighborhood
U of p where all non-trivial orbits of X are periodic. It is known that a linear center p
is either a center, or a focus. In this last case p is called a weak focus. We recall that p is

https://doi.org/10.4153/CJM-2004-015-2 Published online by Cambridge University Press

314 Jaume Llibre and Dana Schlomiuk

a strong focus if the eigenvalues of its linear part are of the form α ± βi with αβ ̸= 0.
The next result is due to Shi [45, 46]. This lemma is better stated in [40] where
the rings involved are explicitly written, and where a sketch of the proof is also given.
For the sake of completeness we give below the statement of this lemma.

Lemma 1 Consider the polynomial system:

(1) ˙x = p(x, y) = −y + p2(x, y) + · · · + pm(x, y),

˙y = q(x, y) = x + q2(x, y) + · · · + qm(x, y),

where
 pi(x, y) =
 i∑

j=0 ai jxi− j y j, qi(x, y) =
 i∑

j=0 bi jxi− j y j.

Then there exists a formal power series F ∈ Q[a20, . . . , b0m][[x, y]],

F = 1
2 (x2 + y2) + F3(x, y) + F4(x, y) + · · · ,

and there exists polynomials V1, . . . , Vi, . . . ∈ Q[a20, . . . , b0m] such that

dF
dt = ∂F
∂x p + ∂F
∂ y q =
 ∞∑

i=1 Vi(x2 + y2)i+1.

The quantities Vi are not uniquely determined. For each i there is an inﬁnite
number of possibilities for a Vi. But according to a result also proven by Shi, all
such Vis are in the same coset modulo the ideal generated by V 1, . . . , Vi−1 in the
ring Q[a20, . . . , b0m]. From the work of Poincar´e [35] it follows that system (1) has
a center at the origin if and only if Vi = 0 for all i. By Hilbert’s basis theorem, the
ideal I = ⟨V1, . . . , Vi, . . .⟩ has a ﬁnite basis. It follows from the work of Bautin [6]
that for quadratic systems (m = 2) this ideal is determined by the values of V i with
i ≤ 3. The above result implies that V1 = V2 = V3 = 0 if and only if Vi = 0 for all i
and the origin is a center. We say that the origin of a quadratic system is
(i) a weak focus of ﬁrst order if V1 ̸= 0;
(ii) a weak focus of second order if V1 = 0 and V2 ̸= 0; and
(iii) a weak focus of third order if V1 = V2 = 0 and V3 ̸= 0.

A quadratic system with a focus or a center at the origin can always be written in
the form

(2) ˙x = ax − by + a20x2 + a11xy + a02 y2, ˙y = bx + ay + b20x2 + b11xy + b02 y2,

with b ̸= 0. Moreover, since the focus is weak we can assume that a = 0. We
remark that the change of variables for writing an arbitrary quadratic system with
a weak focus into the form (2) with a = 0 is continuous. Doing a rescaling of the
independent variable we can assume without loss of generality that b = 1.

https://doi.org/10.4153/CJM-2004-015-2 Published online by Cambridge University Press

Quadratic Differential Systems 315

Proposition 2 Any quadratic system with a weak focus at the origin can be written
into the normal form

(3) ˙x = −y + lx2 + rxy + ny2, ˙y = x + ax2 + bxy,

by a linear change of variables and a rescaling of the independent variable. Furthermore,
the transformation into this normal form depends continuously on the parameters.

Proof For the system (2) with a = 0 and b = 1, we perform the linear change of
variables

(4) x = X cos θ + Y sin θ y = −X sin θ + Y cos θ.

Then the quadratic system (2) becomes

˙X = −Y + a ′20X2 + a ′11XY + a ′02Y 2, ˙Y = X + b ′20X2 + b ′11XY + b ′02Y 2.

with

(5) b ′02 = b02 cos3 θ + (a02 + b11) cos2 θ sin θ + (a11 + b20) cos θ sin2 θ + a20 sin
3 θ.

We note that this cubic trigonometric polynomial cannot be identically zero. Indeed,
the case b20 = a20 = a02 + b11 = a11 + b20 = 0 produces the quadratic system

˙x = −y(1 − a11x − a02 y), ˙y = x(1 − a11x − a02 y);

and clearly this system has a center at the origin instead of a focus.
Since the cubic trigonometric polynomial (5) is not identically zero, it always has
a real solution θ0 depending continuously on the coefﬁcients. For instance, when
a20 ̸= 0 then the cubic (5) has always a real root in tan θ which goes to inﬁnity when
a20 tends to zero, and we can take θ0 = π/2 for a20 = 0. The process of associating to
any system (2) with a = 0, b = 1, the angle θ0 is continuous and the coefﬁcients a ′
i j
and b ′
i j are obtained from ai j and bi j by continuous operations, and doing the change
of variables (4) with θ = θ0, the proposition is proved.

Looking at the proof of this proposition and taking into account the remark made
just before the statement of the previous proposition, it follows that we can pass any
quadratic system with a weak focus to the normal form (3) in a continuous way.
Calculations of Li [23] yield that V1 = L1, V2 = L2 (mod V1), V3 = L3
(mod V1, V2) where
 L1 = r(l + n) − a(b + 2l),

L2 = ra(5a − r)[(l + n)2(n + b) − a2(b + 2l + n)],

L3 = ra2[2a2 + n(l + 2n)][(l + n)2(n + b) − a2(b + 2l + n)].

Using the above proposition and L1 = 0, L2 = 0, L3 ̸= 0 we obtain:

https://doi.org/10.4153/CJM-2004-015-2 Published online by Cambridge University Press

316 Jaume Llibre and Dana Schlomiuk

Corollary 3 A planar quadratic vector ﬁeld with a weak focus of third order may be
written in the following form where the weak focus is placed at the origin:

(6) ˙x = p(x, y) = −y + lx2 + 5axy + ny2, ˙y = q(x, y) = x + ax2 + (3l + 5n)xy,

with L3 = 5a3[2a2 + n(l + 2n)][3(l + n)2(l + 2n) − a2(5l + 6n)] ̸= 0.

Systems (6) depend on the parameter λ = (a, l, n) ∈ R3. We consider systems (6)
which are nonlinear, i.e., λ = (a, l, n) ̸= 0. In this case a system (6) can be rescaled,
therefore the parameter space needed is actually the real projective plane RP(2) and
not R3.

3 The Poincar´e Compactiﬁcation and the Complex (Real) Foliation
with Singularities on CP2 (RP2) Associated to a Real Planar
Polynomial Vector Field

A real planar polynomial vector ﬁeld ξ can be compactiﬁed on the sphere as follows:
Consider the x, y plane as being the plane Z = 1 in the space R3 with coordinates
X, Y , Z. The central projection of the vector ﬁeld ξ on the sphere of radius one
yields a diffeomorphic vector ﬁeld on the upper hemisphere and also another vector
ﬁeld on the lower hemisphere. There exists (for a proof cf. [19]) an analytic vec-
tor ﬁeld p(ξ) on the whole sphere such that its restriction on the upper hemisphere
has the same phase curves as the one constructed above from the polynomial vector
ﬁeld. The projection of the closed northern hemisphere H + of S2 on Z = 0 under
(X, Y, Z) → (X, Y ) is called the Poincar´e disc. A singular point q of p(ξ) is called an
inﬁnite (respectively ﬁnite) singular point if q ∈ S1 (respectively q ∈ S2 \ S1). By the
Poincar´e compactiﬁcation of a polynomial vector ﬁeld we mean the vector ﬁeld p(ξ)
restricted to the upper hemisphere completed with the equator.
Ideas in the remaining part of this section go back to Darboux’s work [12]. Let
p(x, y) and q(x, y) be polynomials with real coefﬁcients. For the vector ﬁeld

(7) p ∂
∂x + q ∂
∂ y ,

or equivalently for the differential system

(8) ˙x = p(x, y), ˙y = q(x, y),

we consider the associated differential 1-form ω1 = q(x, y)dx − p(x, y)dy, and the
differential equation

(9) ω1 = 0.

Clearly, equation (9) deﬁnes a foliation with singularities on C2. The afﬁne plane
C2 is compactiﬁed on the complex projective space CP2 = (C3 \ {0})/∼, where
(X, Y, Z) ∼ (X ′, Y ′, Z ′) if and only if (X, Y, Z) = λ(X ′, Y ′, Z ′) for some complex
λ ̸= 0. The equivalence class of (X, Y, Z) will be denoted by [X :Y : Z].

https://doi.org/10.4153/CJM-2004-015-2 Published online by Cambridge University Press

Quadratic Differential Systems 317

The foliation deﬁned by equation (9) on C2 can be extended to a singular foliation
on CP2 and the 1-form ω1 can be extended to a meromorphic 1-form ω on CP2

which yields an equation ω = 0, i.e.,

(10) A(X, Y, Z)dX + B(X, Y, Z)dY + C(X, Y, Z)dZ = 0,

whose coefﬁcients A, B, C are homogeneous polynomials and satisfy the relation:

(11) A(X, Y, Z)X + B(X, Y, Z)Y + C(X, Y, Z)Z = 0,

Indeed, consider the map i : C3\{Z = 0} → C2, given by i(X, Y, Z) = (X/Z, Y /Z) =
(x, y) and suppose that max{deg(p), deg(q)} = m > 0. Since x = X/Z and y =
Y /Z we have:
 dx = (ZdX − XdZ)/Z2, dy = (ZdY − Y dZ)/Z2,

the pull-back form i∗(ω1) has poles at Z = 0 and the equation (9) can be written as

i∗(ω1) = q(X/Z, Y /Z)(ZdX − XdZ)/Z2 − p(X/Z, Y /Z)(ZdY − Y dZ)/Z2 = 0.

Then the 1-form ω = Zm+2i∗(ω1) in C3 \ {Z ̸= 0} has homogeneous polynomial
coefﬁcients of degree m + 1, and for Z ̸= 0 the equations ω = 0 and i ∗(ω1) = 0 have
the same solutions. Therefore the differential equation ω = 0 can be written as (10)
where
 A(X, Y, Z) = ZQ(X, Y, Z) = Zm+1q(X/Z, Y /Z),

B(X, Y, Z) = −ZP(X, Y, Z) = −Zm+1 p(X/Z, Y /Z),(12)
 C(X, Y, Z) = Y P(X, Y, Z) − XQ(X, Y, Z).

Clearly A, B and C are homogeneous polynomials of degree m + 1 satisfying (11).
To study the foliation with singularities deﬁned by the differential equation (10)
subject to (11) with A, B, C satisfying the above conditions in the neighborhood of
the line Z = 0, we consider the two charts of CP2: (u, z) = (Y /X, Z/X), X ̸= 0, and
(v, w) = (X/Y, Z/Y ), Y ̸= 0, covering this line. We note that in the intersection of
the charts (x, y) = (X/Z, Y /Z) and (u, z) (respectively (v, w)) we have the change of
coordinates x = 1/z, y = u/z (respectively x = v/w, y = 1/w). Except for the point
[0 : 1 : 0], the foliation deﬁned by equations (10),(11) with A, B, C as in (12) yields, in
the neighborhood of the line Z = 0, the foliation deﬁned by the phase curves of the
vector ﬁeld associated with the system

(13) ˙u = uP(1, u, z) − Q(1, u, z) = C(1, u, z), ˙z = zP(1, u, z);

and except for the point [1 : 0 : 0] it yields, in the neighborhood of the line Z = 0,
the foliation deﬁned in this neighborhood by the integral curves of the vector ﬁeld
associated with the system

(14) ˙v = vQ(v, 1, w) − P(v, 1, w) = −C(v, 1, w), ˙w = wP(v, 1, w).

Similarly way we can associate a real foliation with singularities on RP2 to a real
planar polynomial vector ﬁeld.

https://doi.org/10.4153/CJM-2004-015-2 Published online by Cambridge University Press

318 Jaume Llibre and Dana Schlomiuk

4 Intersection Numbers

In this section we brieﬂy recall the notion of intersection number of two algebraic
curves at a point (cf. [18]).
The intersection number of two afﬁne algebraic curves C : f (x, y) = 0 and
C ′ : g(x, y) = 0 over C at a point in C2 is the number

Ia( f , g) = dimC Oa/( f , g),

where Oa is the local ring of the afﬁne complex plane A2(C) = C2 at a; i.e., Oa is the
ring of rational functions r(x, y)/s(x, y) which are deﬁned at a, i.e., s(a) ̸= 0.
In our case, since the polynomial differential systems are quadratic, the intersec-
tion numbers Ia(p, q) for p, q as in (2), at the singular points a in C2 can be computed
easily by using the axioms (cf. [18]). For two projective curves in CP2, F(X, Y, Z) = 0
and G(X, Y, Z) = 0, where F and G are homogeneous polynomials in the variables X,
Y and Z over C, assuming for instance Z ̸= 0, we deﬁne IW (F, G) = Iw( f , g) where
f = F(x, y, 1), g = G(x, y, 1) and w = (X/Z, Y /Z). It is known that IW (F, G) is
independent of the choice of a local chart, and of a projective change of variables, see
again [18].
Clearly the above concept of intersection multiplicity extends to that of intersec-
tion multiplicity of several curves at a point of the projective plane. In particular we
will be interested in the way the projective curves A = 0, B = 0 and C = 0 intersect
and hence in the values of

Ia(A, B, C) = dimC Oa/(A, B, C).

Here Oa is the local ring at a of the complex projective plane (for more information
see [18]) and (A, B, C) is the homogeneous ideal generated by these three polynomi-
als.
If a is a ﬁnite or inﬁnite singular point of system (6) and A, B and C are deﬁned as
in (12), then we have that Ia(P, Q), Ia(C, Z) and Ia(A, B, C) are invariant with respect
to afﬁne transformations ([34]) and

(15) Ia(A, B, C) =
 {Ia(P, Q) = Ia(p, q) if a is ﬁnite,
Ia(P, Q) + Ia(C, Z) if a is inﬁnite.

5 Zero-Cycles and Divisors

In this section we shall use the algebro-geometric notions of zero-cycle and divisor
for the purpose of classifying systems (6). We brieﬂy recall the deﬁnitions of these
notions.
Let V be an irreducible algebraic variety over a ﬁeld K. A cycle of dimension r or
r-cycle on V is a formal sum ∑

W nW W , where W is a subvariety of V of dimension r
which is not contained in the singular locus of V , nW ∈ Z, and only a ﬁnite number
of nW s are non-zero. The support of a cycle C is the set Supp(C) = {W |nW ̸= 0}. We
denote by Max(C) the maximum value of the coefﬁcients nW in C. For every m ≤

https://doi.org/10.4153/CJM-2004-015-2 Published online by Cambridge University Press

Quadratic Differential Systems 319

Max(C) let s(m) be the number of the coefﬁcients nW in C which are equal to m. We
call type of the cycle C the set of ordered couples ( s(m), m) where 1 ≤ m ≤ Max(C).
The degree of a cycle of C2, (respectively R2, CP2, RP2) is the sum of its coefﬁcients
nW . If J is a cycle we denote by deg( J), its degree.
An (n − 1)-cycle is called a divisor. These notions which occur frequently in al-
gebraic geometry [20], were used for classiﬁcation purposes of planar quadratic dif-
ferential systems by Pal and Schlomiuk [34, 42]. They are also helpful here as we
indicate below.
Using Section 3, we can associate to the differential system (6) a singular foliation
on CP2 described by the equation (10) satisfying (11), where

(16)
 A(X, Y, Z) = ZQ(X, Y, Z) = Z(XZ + aX2 + (3l + 5n)XY ),

B(X, Y, Z) = −ZP(X, Y, Z) = −Z(−Y Z + lX2 + 5aXY + nY 2),

C(X, Y, Z) = Y P(X, Y, Z) − XQ(X, Y, Z)

= −aX3 − (2l + 5n)X2Y − X2Z + 5aXY 2 − Y 2Z + nY 3.

We note that the straight line Z = 0 is always an algebraic invariant curve of this
foliation and that its singular points are the solutions of the system A(X, Y, Z) =
B(X, Y, Z) = C(X, Y, Z) = 0.
We consider a real polynomial differential system

(17) ˙x = f (x, y), ˙y = g(x, y),

with f and g relatively prime polynomials in C[x, y] with max( deg( f ), deg(g)) =
m. To this system we can associate several zero-cycles and divisors:
(i) Two zero-cycles which encode the information regarding the intersection num-
bers of the real projective curves F = 0 and G = 0 in CP2:

DK(F, G) = ∑

W ∈KP2 IW (F, G)W,

with K = C or K = R, where

F(X, Y, Z) = Zm f (X/Z, Y /Z), G(X, Y, Z) = Zmg(X/Z, Y /Z).

We note that when W ∈ RP2 the sum runs only on the real intersection points of
F = 0 and G = 0. Always IW (F, G) is computed over C.
(ii) Two divisors on the line at inﬁnity Z = 0 which encode the multiplicities of
the intersection points of F = 0 with G = 0 in KP2 which lie on Z = 0:

DK(F, G; Z) = ∑

W ∈{Z=0}∩KP2 IW (F, G)W.

(iii) Two zero-cycles which encode the information regarding the intersection
numbers of the afﬁne algebraic curves f = 0 and g = 0 in K 2:

DK( f , g) = DK(F, G) − DK(F, G; Z).

https://doi.org/10.4153/CJM-2004-015-2 Published online by Cambridge University Press

320 Jaume Llibre and Dana Schlomiuk

(iv) A divisor which encodes the multiplicities of complex (respectively real) sin-
gular points at inﬁnity which count how many complex real or complex singular
points at inﬁnity will bifurcate at inﬁnity in a complex (respectively real) perturba-
tion of the system:
 DC(C, Z) = ∑

W ∈{Z=0}∩KP2 IW (C, Z)W,

where C(X, Y, Z) = Y F(X, Y, Z) − XG(X, Y, Z) and Z does not divide C.
(v) A zero-cycle which encodes the information regarding the intersection num-
bers of all the real or complex singularities W of the foliation in CP2 (respectively
RP2) associated to a system (17):

DC = DC( f , g) + DC(F, G; Z) + DC(C, Z) = ∑

W ∈CP2 IW (A, B, C)W,

where Z does not divide C. In this last equality we have used (15).
The foliation with singularities in RP2 associated to the system (17) can be ob-
tained by identifying the diametrically opposite trajectories of the Poincar ´e compact-
iﬁcation of system (17) and disregarding the orientation on the orbits. Then we can
deﬁne for every isolated singular point W of the foliation in RP2 its topological in-
dex, i(W ), as the topological index of one of the two diametrically opposed singular
points of the Poincar´e compactiﬁcation of system (17) which after the identiﬁcation
give the point W . A singular point is called elementary if at least one of its eigenvalues
is not zero.
(vi) We introduce two new zero-cycles DI and DC I which will encode the topo-
logical indices of all the isolated singular points W of the foliation in RP2 associated
to system (17) as follows:

DI = ∑

W ∈RP2 i(W )W, DC I = ∑

W ∈CP2 j(W )W.

where i(W ) is as deﬁned above and j(W ) = i(W ) for points W in RP2 and it is zero
elsewhere in CP2.

6 Zero-Cycles and Divisors for Systems (6) and Their Bifurcation
Curves

We apply the notions of the preceding section to our family of real differential systems
(6). Our ﬁnal goal is to give a clear, geometrical classiﬁcation of this class.
For the real differential systems (6) with nonzero L3 we associate the families of
zero-cycles or divisors on Z = 0 introduced in Section 5 indexed by λ where λ =
[a : l : n] ∈ RP(2).

Remark 4 Although the expressions of the zero-cycles and divisors in the following
propositions depend on the speciﬁc canonical form (6), their degrees and their types
as deﬁned in the preceding section are afﬁne invariant.

https://doi.org/10.4153/CJM-2004-015-2 Published online by Cambridge University Press

Quadratic Differential Systems 321

Indeed, these degrees and types depend only on the coefﬁcients of these cycles
which are afﬁne invariant being intersection multiplicities. Furthermore, as we ex-
plain in our last section, these geometric invariants could be expressed in terms of
algebraic invariants which in turn can be computed for any given normal form of the
systems, other than (6), and the computation implemented on a computer.
To compute the cycles and obtain the bifurcation diagram, we ﬁrst introduce
some notations and perform some calculations. Not to repeat unnecessary com-
putations we ﬁrst note that the systems (6) have a symmetry. Indeed, a system (6)
corresponding to the parameter λ = (a, l, n) with a < 0 is topologically equiv-
alent to system (6) corresponding to the parameter λ ′ = (−a, l, n) through the
symmetry (x, y, t) → (−x, y, −t). Due to this, we only consider the parameters
[a : l : n] ∈ RP2 with a ≥ 0 and n ≥ 0. We can identify this subset of the pa-
rameter space with the quarter of the 2-dimensional sphere a2 + l2 + n2 = 1 of
R3 = {(a, l, n) : a, b, c ∈ R} having a ≥ 0 and n ≥ 0. We can view the bifurcation
diagram in the disc {(a, l) : a2 + l2 ≤ 1} via vertical projection. However to obtain
a better picture, we prefer to project this quarter of sphere on the plane n = 0 as
follows. To every point p on this quarter of sphere we associate the intersection point
p ′ of the plane n = 0 with the line joining p with the point (0, 0, −3/4). In this way
the parameter space of points [a : l : n] ∈ RP2, images of non-zero (a, l, n) in R3 with
a ≥ 0, n ≥ 0, can be identiﬁed with the half-disc D = {(a, l) : a2 + l2 ≤ 1 and
a ≥ 0}.
Dλ,C(P, Q; Z) involves the common roots of p2(x, y) and q2(x, y). We deﬁne

Ω = Resultant( p2(x, 1), q2(x, 1), x) = n[l(3l + 5n)2 − 3a2(5l + 8n)] = n ¯Ω.

We remark that for a weak focus of third order, it is not possible to have both n = 0
and ¯Ω = 0 as in this case we would also have L3 = 0 which yields a center at the
origin.
Both Dλ,C(p, q) and Dλ,C(P, Q; Z) involve the intersection points of P = 0 with
Q = 0. These are obtained by intersecting each of the lines X = 0 and Z + aX +
(3l+5n)Y = 0 with P = 0. In the ﬁrst case we obtain the points [0 : 0 : 1] and [0 : 1 : n].
In general, in the second case we obtain two points q3 and q4 which if ¯Ω ̸= 0 are given
by
 [3a(2l + 3n) + (3l + 5n)√3δ : 3a2 − l(3l + 5n) − a√
3δ : ¯Ω],

[3a(2l + 3n) − (3l + 5n)√
3δ : 3a2 − l(3l + 5n) + a√
3δ : ¯Ω],

where δ = 3a2 − l(l + 2n). They are real if δ ≥ 0, or complex if δ < 0 and, q3 = q4
if δ = 0. The real projective curve δ = 0 restricted to R2 has two branches which
we denote by δi, see Figure 1. If we denote by R(y) the resultant of p(x, y) and
q(x, y) with respect to x, we note that δ is a factor of the resultant of R(y) and R ′(y)
with respect to y. If ¯Ω = 0, then one of the singularities q3 and q4 is ﬁnite and the
other [3l + 5n : − a : 0] is inﬁnite. When ¯Ω = 0 and L3 ̸= 0 the ﬁnite singularity is
[6a2 − 3l2 − 5ln : −al : a(2l(3l + 5n) − 6a2)]. When it is on l + 2n = 0 the point [0 : 1 : n]
satisﬁes both Z + aX + (3l + 5n)Y = 0 and P = 0. In this case q2 coincides with one
of the two points q3, q4.

https://doi.org/10.4153/CJM-2004-015-2 Published online by Cambridge University Press

322 Jaume Llibre and Dana Schlomiuk

Viewed in the half disc D, the real algebraic curve ¯Ω = 0 restricted to D has three
parts which we denote by ¯Ωi, i = 1, 2, 3, and ¯Ω3 is described below; see Figure 1. The
line l + 2n = 0 cuts ¯Ω3, and determines on ¯Ω3 two open components ¯Ω31 and ¯Ω32,
as indicated in Figure 1. The curve ¯Ω = 0 determines on the straight line l + 2n = 0
viewed on D two segments ln1 and ln2, as indicated in Figure 1.
For the divisor Dλ,C(C; Z), we need the common points of C = 0 and Z = 0.
We denote by c(x) = C(x, 1, 0) = p2(x, 1) − xq2(x, 1), where p2 and q2 are the
degree 2 homogeneous parts of p, respectively q. Let ∆ be the discriminant of the
cubic polynomial c(x). We have:

∆ = 125a4 + a2(25l2 + 170ln + 262n2) + n(2l + 5n)3 = Resultant(c(x), c ′(x), x)/(4a).

It is only necessary to do the resultant with respect to x, because when a is not zero
the system (6) has no inﬁnite singular points [X :Y : Z] with Y = 0. This also implies
that all common points of C = 0 and Z = 0 must be of the form p = [r : 1 : 0]. We
remark that c(x) cannot have a triple root in our family, for this would imply that
c(x), c ′(x) and c ′ ′(x) have a common root, which yields a = 0, impossible in our
case. The real roots of c(x) denoted in increasing values by ri, give inﬁnite points
[ri : 1 : 0] denoted by pi.
The real algebraic curve n ¯Ωδ(l + 2n)∆ = 0 divides the part corresponding to the
half-disc D into 9 open connected components Ri, see Figure 1. In the following
discussion we omit from these components the points of D such that L3 = 0. We
denote by ∂Ri the boundary of Ri in D. The interior of ∂Ri ∩ {n = 0} with the
topology of the straight line n = 0 viewed in D is denoted by ni; consequently ni ⊂
∂Ri, see Figure 1. In this ﬁgure the curve ∆ = 0 is denoted simply by ∆.

Convention In order not to have two separate tables for real and complex divisors,
we make the convention to use the symbol pc (respectively qc) to specify that a com-
plex point p (respectively q) is not real. In this way the real divisors could be read
directly from the table of complex divisors.

Notation We denote by NC(S) the number of distinct complex singular points of
the complex foliation with singularities (10) with (16), associated to a real planar
quadratic system S. We denote by NR, f (S), NR,∞(S) the number of ﬁnite, respectively
inﬁnite, distinct real singular points of the system S, by DI f the ﬁnite part of the
zero-cycle DI.

Proposition 5 For all values of the parameter λ ∈ RP2, the divisors Dλ,C(P, Q; Z),
Dλ,C(C, Z) and the zero-cycles Dλ,C(p, q) and Dλ,C for systems (6) with L3 ̸= 0 are well
deﬁned and we have

(a) deg( Dλ,C(P, Q; Z)) ≤ 1. Moreover,

Dλ,C(P, Q; Z) =
 



0 if Ω(λ) ̸= 0,
[3l + 5n : − a : 0] if ¯Ω(λ) = 0,
[0 : 1 : 0] if n = 0.

https://doi.org/10.4153/CJM-2004-015-2 Published online by Cambridge University Press

Quadratic Differential Systems 323

Figure 1: Bifurcation curves.

https://doi.org/10.4153/CJM-2004-015-2 Published online by Cambridge University Press

324 Jaume Llibre and Dana Schlomiuk

Hence the bifurcation curve for this divisor is Ω(λ) = n ¯Ω(λ) = 0.
(b) The zero-cycles Dλ,C(p, q) for systems (6) with L3 ̸= 0 are given by:

Dλ,C(p, q) =
 




q1 + q2 + q3 + q4 if δ > 0 and l + 2n ̸= 0,
q1 + q2 + qc
3 + qc
4 if δ < 0 and l + 2n ̸= 0,
q1 + q2 + 2q3 if δ = 0,
q1 + 2q2 + q3 if l + 2n = 0,
q1 + qc
2 + qc
3 in n1 ∪ n8.

Thus the bifurcation curve for this zero-cycle is δ(l + 2n) = 0.
(c) The divisor Dλ,C(C, Z) for systems (6) with L3 ̸= 0 are given by:

Dλ,C(C, Z) =
 



p1 + p2 + p3 if ∆ > 0,
p1 + pc
2 + pc
3 if ∆ < 0,
2p1 + p2 if ∆ = 0.

Thus the bifurcation curve for this divisor is ∆ = 0.
(d) For λ ∈ RP2 the zero-cycle Dλ,C for a system (6) with L3 ̸= 0 is well deﬁned and
for points corresponding to D it is given below, listed according to decreasing values
for NC.

NC = 7 q1 + q2 + qc
3 + qc
4 + p1 + p2 + p3 if λ ∈ R1 ∪ R8 ∪ R9,

q1 + q2 + q3 + q4 + p1 + p2 + p3 if λ ∈ R2 ∪ · · · ∪ R7,

NC = 6 q1 + qc
3 + qc
4 + 2p1 + p2 + p3 if λ ∈ n1 ∪ n8,(q2 = p1),

q1 + q3 + q4 + 2p1 + p2 + p3 if λ ∈ n2 ∪ n3 ∪ n5 ∪ n7,(q2 = p1),

q1 + q2 + 2q3 + p1 + p2 + p3 if λ ∈ δ1 ∪ δ2,

q1 + q2 + q4 + p1 + 2p2 + p3 if λ ∈ ¯Ω1, (q3 = p2),

q1 + q2 + q3 + 2p1 + p2 + p3 if λ ∈ ¯Ω2, (q4 = p1),

q1 + q2 + q4 + p1 + p2 + 2p3 if λ ∈ ¯Ω31 ∪ ¯Ω32, (q3 = p3),

q1 + 2q2 + q3 + p1 + p2 + p3 if λ ∈ ln1 ∪ ln2,

q1 + q2 + qc
3 + qc
4 + 2p1 + p3 if λ ∈ ∆,

NC = 5 q1 + 2q3 + 2p1 + p2 + p3 if λ = [1 : ± √3 : 0], (q2 = p1),

q1 + 2q2 + p1 + p2 + 2p3 if λ ∈ [1 : − 2√
3 : √3], (q3 = p3).

Thus the bifurcation curve for this zero-cycle is the real curve ∆Ωδ(l + n) = 0.

Proof (a) and (b) of the proposition follow easily from the expression of qi for i =
1, . . . , 4, and the deﬁnition of intersection numbers. (c) follows from the fact that
c(x) is a cubic polynomial, which for a ̸= 0 cannot have a triple root and ∆ is the
discriminant of c(x). (d) sums up the results concerning multiplicities.

https://doi.org/10.4153/CJM-2004-015-2 Published online by Cambridge University Press

Quadratic Differential Systems 325

We note that in Proposition 5 if n = 0, we must have ¯Ω ̸= 0 since otherwise
L3 = 0. We denote by L the algebraic curve in RP2 formed by the points λ such that
L3 = 0.

Proposition 6 The real curve C = {λ ∈ RP2 : n ¯Ωδ(l + 2n)∆ = 0} is the saddle-
node bifurcation curve for the systems (6) with weak focus of third order at the origin
(see Figure 1). Furthermore, (a) on the curve n ¯Ω = 0 inﬁnite saddle-nodes arise from
the collision of one ﬁnite singularity with an inﬁnite one; (b) on the curve δ(l + 2n) = 0
ﬁnite saddle-nodes arise from the collision of two ﬁnite singularities; (c) on the curve
∆ = 0 inﬁnite saddle-nodes arise from the collision of two inﬁnite singularities.

Proof (a) By using the classiﬁcation of the planar singular points which have exactly
one zero eigenvalue, it follows easily that the singular point q3 when n ̸= 0 and
¯Ω = 0, or the singular point q2 when n = 0, is a saddle-node. From the deﬁnition
of the points qi’s, it is clear that the above two points are ﬁnite points on Ω ̸= 0 that
reach the inﬁnity on Ω = 0.
(b) Using the classiﬁcation of the planar singular points which have exactly one
zero eigenvalue (see for instance [1]), it follows easily that the singular point q3 when
δ = 0, or the singular point q2 when l + 2n = 0, is a saddle-node.
(c) The singular point p1 when ∆ = 0 is a saddle-node. From the deﬁnition
of the points pi’s, it is clear that the inﬁnite singular points p1 and p2 collide when
∆ = 0.

The only real singularities of the curve C in D \ L are the three points: {[1 : ±√3 : 0]} = {δ = 0} ∩ {n = 0} and [1 : − 2√
3 : √
3] = { ¯Ω = 0} ∩ {l + 2n = 0}. We
denote by Sing(C), the set formed by these three points.

Corollary 7 For the normal form (6) and points corresponding to D we have NC(λ)
equal to 7, 6 or 5 if and only if λ /∈ C, λ ∈ C \ Sing(C) or λ ∈ Sing(C), respectively.

The next result follows easily from Proposition 5.

Corollary 8 For systems S in the class of quadratic systems with a weak focus of third
order, NR, f (S) takes all the values from 1 to 4 and NR,∞(S) takes all the values from 1 to
3. For the normal form (6) and for points corresponding to D we have:

NR, f (λ) =
 




4 iff λ ∈ R2 ∪ · · · ∪ R7,
3 iff λ ∈ n2 ∪ n3 ∪ n5 ∪ n7 ∪ δ1 ∪ δ2 ∪ ¯Ω1
∪ ¯Ω2 ∪ ¯Ω31 ∪ ¯Ω32 ∪ ln1 ∪ ln2,
2 iff λ ∈ R1 ∪ R8 ∪ R9 ∪ ∆ ∪ Sing(L),
1 iff λ ∈ n1 ∪ n8;

and NR,∞(λ) is 1, 2 or 3 if and only if λ ∈ R9, λ ∈ ∆ or otherwise, respectively.

Proposition 9 All ﬁnite and inﬁnite singular points of a quadratic system with a weak
focus of third order are elementary.

https://doi.org/10.4153/CJM-2004-015-2 Published online by Cambridge University Press

326 Jaume Llibre and Dana Schlomiuk

Proof From the normal form (6) it is easy to check that the linear part of the ﬁ-
nite and inﬁnite singular points have either determinant different from zero, or trace
different from zero. So the proposition follows.

We recall that the local phase portraits of elementary singular points are well
known and consequently also their topological indices which could only be −1, 0
or 1, see for instance [1].

Proposition 10 For all values of the parameter λ ∈ RP2 the divisor DIλ for a system
(6) with L3 ̸= 0 is well deﬁned and for points corresponding to D it is equal to

NC = 7 1q1 − 1q2 + 0qc
3 + 0qc
4 + 1p1 − 1p2 + 1p3 if λ ∈ R1,

1q1 − 1q2 + 1q3 − 1q4 + 1p1 − 1p2 + 1p3 if λ ∈ R2,

1q1 − 1q2 − 1q3 − 1q4 + 1p1 + 1p2 + 1p3 if λ ∈ R3,

1q1 − 1q2 − 1q3 + 1q4 − 1p1 + 1p2 + 1p3 if λ ∈ R4,

1q1 + 1q2 − 1q3 − 1q4 − 1p1 + 1p2 + 1p3 if λ ∈ R5,

1q1 − 1q2 + 1q3 + 1q4 − 1p1 + 1p2 − 1p3 if λ ∈ R6,

1q1 + 1q2 + 1q3 − 1q4 − 1p1 + 1p2 − 1p3 if λ ∈ R7,

1q1 + 1q2 + 0qc
3 + 0qc
4 − 1p1 + 1p2 − 1p3 if λ ∈ R8,

1q1 + 1q2 + 0qc
3 + 0qc
4 − 1p1 + 0pc
2 + 0pc
3 if λ ∈ R9,

NC = 6 1q1 + 0qc
3 + 0qc
4 + 0p1 − 1p2 + 1p3 if λ ∈ n1, q2 = p1,

1q1 + 1q3 − 1q4 + 0p1 − 1p2 + 1p3 if λ ∈ n2 ∪ n7, q2 = p1,

1q1 − 1q3 − 1q4 + 0p1 + 1p2 + 1p3 if λ ∈ n3 ∪ n5, q2 = p1,

1q1 + 0qc
3 + 0qc
4 + 0p1 + 1p2 − 1p3 if λ ∈ n8, q2 = p1,

1q1 − 1q2 + 0q3 + 1p1 − 1p2 + 1p3 if λ ∈ δ1,

1q1 + 1q2 + 0q3 − 1p1 + 1p2 − 1p3 if λ ∈ δ2,

1q1 − 1q2 − 1q4 + 1p1 + 0p2 + 1p3 if λ ∈ ¯Ω1, q3 = p2,

1q1 − 1q2 − 1q3 + 0p1 + 1p2 + 1p3 if λ ∈ ¯Ω2, q4 = p1,

1q1 − 1q2 + 1q4 − 1p1 + 1p2 + 0p3 if λ ∈ ¯Ω31, q3 = p3,

1q1 + 1q2 − 1q4 − 1p1 + 1p2 + 0p3 if λ ∈ ¯Ω32, q3 = p3,

1q1 + 0q2 + 1q3 − 1p1 + 1p2 − 1p3 if λ ∈ ln1,

1q1 + 0q2 − 1q3 − 1p1 + 1p2 + 1p3 if λ ∈ ln2,

1q1 + 1q2 + 0qc
3 + 0qc
4 + 0p1 − 1p2 if λ ∈ ∆,

https://doi.org/10.4153/CJM-2004-015-2 Published online by Cambridge University Press

Quadratic Differential Systems 327

NC = 5 1q1 + 0q3 + 0p1 − 1p2 + 1p3 if λ ∈ [1 : ± √3 : 0], q2 = p1,

1q1 + 0q2 − 1p1 + 1p2 + 0p3 if λ ∈ [1 : − 2√
3 : √3], q3 = p3.

To have all real singularities displayed in the statement of the Proposition 10 we
included the saddle-nodes (real) points qi or pi, whose indices are zero and we wrote
0qi or 0pi along with 0qc
i or 0pc
i . Although the above values for DIλ are computed for
the canonical form (2), the types of these divisors are afﬁne invariants.
According to the Poincar´e-Hopf Theorem (see for instance [30]) the sum of the
indices of all singularities of the foliation in RP2 associated to system (6) is deg(DI) =
1. Then, the next result follows from Proposition 10.

Corollary 11 For systems S in the class of quadratic systems with a weak focus of third
order the values taken by the function deg(DI f )(S) are −2, −1, 0, 1 and 2. For the
normal form (6) and for points corresponding to D we have:

deg[(DI f )(λ)] =
 



−2 iff λ ∈ R3,
−1 iff λ ∈ n3 ∪ n5 ∪ ¯Ω1 ∪ ¯Ω2,
0 iff λ ∈ R1 ∪ R2 ∪ R4 ∪ R5 ∪ δ1 ∪ ln2,
1 iff λ ∈ n1 ∪ n2 ∪ n7 ∪ n8 ∪ ¯Ω31 ∪ ¯Ω32 ∪ Sing(L),
2 iff λ ∈ R6 ∪ R7 ∪ R8 ∪ R9 ∪ δ2 ∪ ln1 ∪∆ .

The deg[(DI f )(λ)] is a global topological index measuring the relative number of
ﬁnite saddles versus antisaddles in the ﬁnite plane.

7 The Bifurcation Diagram of the Systems With a Weak Focus of
Third Order

7.1 Basic Properties of Quadratic Systems and Speciﬁc Properties of
Systems in QW3

We list below results which play a role in the study of the global phase portraits of
real planar quadratic systems (6) having a weak focus of third order.
The following results hold for any quadratic system:
(i) A straight line either has at most two (ﬁnite) contact points with a quadratic
system (which include the singular points), or it is formed by trajectories of the sys-
tem; see Lemma 11.1 of [51]. We recall that by deﬁnition a contact point of a straight
line L is a point of L where the vector ﬁeld has the same direction as L, or it is zero.
(ii) If a straight line passing through two real ﬁnite singular points q1 and q2 of a
quadratic system is not formed by trajectories, then it is divided by these two singular
points in three segments ∞q1, q1q2 and q2∞ such that the trajectories cross ∞q1 and
q2∞ in one direction, and they cross q1q2 in the opposite direction; see Lemma 11.4
of [51].
(iii) The straight line connecting a real ﬁnite singular point and a pair of real
opposite inﬁnite singular points in the Poincar´e compactiﬁcation of a system (6) is

https://doi.org/10.4153/CJM-2004-015-2 Published online by Cambridge University Press

328 Jaume Llibre and Dana Schlomiuk

either formed by trajectories or is a straight line without (ﬁnite) contact points except
at that ﬁnite singular point; see Lemma 11.5 of [51].
(iv) If a quadratic system has a limit cycle, then it surrounds a unique singular
point, and this point is a focus; see [11].
(v) If in a quadratic system the separatrix of an inﬁnite saddle connects with
the separatrix of the diametrically opposite inﬁnite saddle, then this separatrix is an
invariant straight line; see [49].
(vi) If a quadratic system has a center, then it is integrable; i.e., there exists a
nonconstant analytic ﬁrst integral deﬁned in the whole real plane except perhaps on
some invariant algebraic curve; see [50], [27] and [39].
Finally we state here an important result on general quadratic systems obtained by
Zhang Pingguang [52], [53].
(vii) If there are limit cycles surrounding two foci of a quadratic system, then
around one of the foci there is at most one limit cycle.
The proof of this result is based on several lemmas as well as on previous articles.
The main tools used in this proof are: the transformation of the systems into Lienard
form and previous results in the literature on uniqueness of limit cycles in planar
vector ﬁelds. For this see the English version [53] of [52].
We shall also need the following speciﬁc result for quadratic systems having a weak
focus of third order at the origin:
(viii) There are no limit cycles of systems (6) surrounding the weak focus of third
order, see [24].
We shall now use these properties for the study of the class QW3.
From (iv) it follows that the limit cycles of a system (6) may only be around the
singular points (0, 0) and (0, 1/n) because they are the only possible foci of system
(6) for convenient values of the parameters. Therefore, from (viii), the limit cycles of
a system (6) can only be around the singular point (0, 1/n) in case they exist, and only
when this singular point is a focus. Now, from (vii), since by perturbing conveniently
a weak focus of third order it is possible to produce three limit cycles surrounding
the origin, it follows that for those systems (6) which have two foci, if they have limit
cycles around (0, 1/n), then they must have exactly one limit cycle.
Except for eliminating the possibility of existence of more than one limit cycle
surrounding a focus at (0, 1/n), the phase portraits of quadratic systems (6) were ob-
tained by Art´es in his 1984 Master’s Thesis [3], supervised by Llibre and published
by the Universitat Aut `onoma de Barcelona. At the time of the publication in 1984,
the result (vii) was not yet proved. Interest shown by some mathematicians in the
work [3] inspired the authors to write a new version and to publish it in a journal
(cf. [5]) in order to facilitate wider access, but again this was prior to the result (vii).
Furthermore the phase portraits in [5] are classiﬁed in terms of inequalities on the
coefﬁcients appearing in the normal form (6) and no concern was shown for ob-
taining intrinsic results. Here we checked the results and furthermore we introduced
integer-valued invariants. These led us to detect that two phase portraits which were
counted as distinct in [5] turned out to be topologically equivalent. As it is expected
that the class of quadratic systems will yield more than two thousand phase portraits,
global tools to distinguish or identify them are essential. Another aspect is the appli-
cability of results to any given situation irrespective of particular presentation of the

https://doi.org/10.4153/CJM-2004-015-2 Published online by Cambridge University Press

Quadratic Differential Systems 329

systems, a problem which we discuss in our last section.

7.2 Phase Portraits of QW3 and Basic Features of the Bifurcation Diagram

The basic ingredient for obtaining the phase portraits of QW3 is the knowledge we
have of the global phase portraits of the quadratic systems (6) with a center (cf. [39,
50]), which appear in our diagram on the components of the curve L or L3 = 0, i.e.,
the line L1 deﬁned by a = 0 (the diameter in Figure 2), the conic L2 (a parabola
in the afﬁne part n ̸= 0) deﬁned by 2a2 + n(l + 2n) = 0, and the singular cubic L3
deﬁned by 3(l + n)2(l + 2n) − a2(5l + 6n) = 0 with a nodal singularity at the point
[0 : − 1 : 1]. Perturbing these systems with center we obtain the phase portraits near
by. Then using these as well as further analysis based on knowledge of singularities
yields most of the results. A special discussion is needed for the region R8 and for
part of its border: ∆ = 0. We describe below the arguments needed to obtain the
phase portraits on R1 and on its boundary. Then, with the exception of the region
R8 and its partial boundary ∆ = 0, where more arguments will be needed, the phase
portraits in all the remaining regions could be obtained in a similar way.
We highlight below some of the arguments. Although we picture our diagram
on the half-disc D, we shall mark the points on D by their corresponding points
in RP2 given in homogeneous coordinates, since for us the important object is the
parameter space RP2. Thus, for instance, the point (a, l) of D will be denoted by
[a : l : √1 − a2 − l2].
The systems (6) are of two types: centers, which correspond to values of λ =
[a : l : n] for which L3 = 0; or weak foci, which correspond to values of λ for which
L3 ̸= 0.
The phase portraits of quadratic systems with centers are known (cf. [39, 50]). We
place these on the bifurcation curves of centers. These are the components of the
curve L or L3 = 0, i.e., the line L1 deﬁned by a = 0 (the diameter in Figure 2), the
conic L2 (a parabola in the afﬁne part n ̸= 0) deﬁned by 2a2 + n(l + 2n) = 0, and
the singular cubic L3 deﬁned by 3(l + n)2(l + 2n) − a2(5l + 6n) = 0 with a node at
[0 : − 1 : 1].
Systems (6) with a = 0 are given by

˙x = −y + lx2 + ny2, ˙y = x + (3l + 5n)xy.

These are the systems (4.10) in [39] with b = −l, d = −n and A = 3l + 5n =
−3b − 5d. So the line a = 0 is the line A + 3b + 5d = 0 which could be traced in
Figure 5 of [39] with afﬁne part (d ̸= 0) in Figure 2 of [39]. We place on our Figure 2,
and on L1 (a = 0) the corresponding phase portraits. We remark that the changes
in phase portraits on a = 0 are given by the changes in the invariant algebraic curves
which such systems have; namely, the straight line (3l + 5n)y + 1 = 0 and the conic
−l(2l + 5n)(l + 5n)x2 − 2(l + 3n) − 4l(l + 3n)y + ln(l + 5n)y2 = 0. In a similar way
we put on Figures 2 and 3 all the phase portraits having a center.
The phase portrait W1 on R1 follows easily from the phase portrait corresponding
to the ∂R1 ∩ {a = 0} which has a center. To obtain W1 we use the behavior of the
vector ﬁeld on the explicit expression of the straight invariant line connecting two
diametrically opposite inﬁnite saddles of the system with center.

https://doi.org/10.4153/CJM-2004-015-2 Published online by Cambridge University Press

330 Jaume Llibre and Dana Schlomiuk

Figure 2: Phase portraits.

https://doi.org/10.4153/CJM-2004-015-2 Published online by Cambridge University Press

Quadratic Differential Systems 331

Figure 3: Phase portraits.

https://doi.org/10.4153/CJM-2004-015-2 Published online by Cambridge University Press

332 Jaume Llibre and Dana Schlomiuk

The phase portrait W1 actually holds in the whole region R1. Indeed, we rule
out the two other global phase portraits which might occur, since they would imply
the existence, for some parameter point, of a straight invariant line connecting two
opposite points at inﬁnity, a fact which cannot occur in a system in QW3 according
to results in [49].
The phase portrait W14 in R9 follows easily from the phase portrait on the border
of R9 which is on a = 0, which has a center. Using arguments analogous to the ones
for W1 we see that W14 holds in the whole region.
The phase portrait W2 on n1 is obtained from the phase portrait W1 on R1 taking
into account that on n1 the saddle [0 : 1 : n] of W2 collides with an inﬁnite node of W2,
creating a saddle-node at inﬁnity.
The phase portrait W3 on δ1 follows from the phase portrait W1 on R1 knowing
that on δ1 there appears an additional singularity which is a ﬁnite saddle-node.
The phase portrait W4 at [1 : √3 : 0] can be obtained easily from the phase portraits
W2 on n1 and W3 on δ1. So we have described all the phase portraits on the region
R1 and its boundary points not on a = 0.
The detailed discussion for the regions R2, . . . , R7, will appear as a technical report
elsewhere.
We shall now describe the phase portraits in the region R8 and on ∆ = 0. Here
again we start by perturbing a system with center.
We start by using the curve L2 of centers. These centers are algebraically integrable
systems which in [39] are of Class I. This curve enables us to ﬁnd the phase portraits
corresponding to any λ sufﬁciently close to L2. For such λs we obtain two distinct
phase portraits, one for λ such that 2a2+n(l+2n) < 0 and another one for λ such that
2a2 +n(l+2n) > 0. These phase portraits are respectively W 11 and W12. For obtaining
them we use the behavior of the vector ﬁeld on the algebraic curve which bounds the
period annulus around the center of the phase portrait associated to L2 and look at
how the local separatrices behave with respect to this curve in the perturbations.
In the subregion of R8 where 2a2 + n(l + 2n) > 0 we have the curve Γ = 25a2 +
12(l + 2n)n = 0 (or simply Γ) on which the singular point (0, 1/n) = [0 : 1 : n] passes
from being a node to a focus. This curve Γ has endpoints [0 : − 2 : 1] and [0 : − 1 : 0]
and it is contained inside the part of R8 which is limited by L2 and ∆ = 0; it does not
intersect these last two curves except at its endpoints. We claim that on Γ and close
to it there is no topological change in the phase portrait but only a C ∞ change when
crossing Γ. Therefore the phase portrait in Γ and also close around it, is thus W 12.
Now we prove the claim. By Zhang Pingguang’s result [52, 53], crossing Γ from
a node to a focus there could appear at most one limit cycle surrounding the focus,
which must be semistable near the bifurcation curve due to the fact that the focus or
node is unstable and there is a stable separatrix coming from inﬁnity surrounding it
(see phase portrait W12). But if for a system X in QW3 such a semistable limit cycle
exists, then close to it there would be two limit cycles surrounding the focus, one
stable and the other unstable, (because the QW3 systems form a rotated family with
respect to the parameter a in an open neighborhood of Γ; see [51] for a deﬁnition
and properties), and this is in contradiction with Zhang Pingguang’s result. So the
claim is proved.
We now discuss the behavior of the systems on ∆ = 0, or simply ∆. In the region

https://doi.org/10.4153/CJM-2004-015-2 Published online by Cambridge University Press

Quadratic Differential Systems 333

R9 the phase portrait is W14, and in the region R8 near ∆ and close to [0 : 1 : 0] it is
W12. Then, moving just above ∆ from R8 to R9 on a small segment with l = constant
which intersects ∆, an inﬁnite saddle and an inﬁnite node of W 12 collide, and by
continuity we obtain on ∆ close to [0 : 1 : 0] the phase portrait W 13. If we continue
moving in the same direction, on the same segment, we get the phase portrait W 14
on R9.
The phase portraits in R8 close to the open segment γ on a = 0 having endpoints
[0 : − 5 : 2] and [0 : − 2 : 1] are again obtained from portraits with center, i.e., from
those on γ which have two centers. So, studying the behavior of the vector ﬁeld on
the branches of the hyperbola that limit the annular regions around the two centers,
we obtain the phase portrait W17 on the points of R8 which are sufﬁciently near to γ.

7.3 The Saddle to Saddle Connection Bifurcation Curve G3

We complete here the construction of the phase portraits in R8. Take a point q on
γ close to [0 : − 2 : 1] (actually q could be taken as close as we wish to this point).
For any point p of γ we consider an analytic arc σ p inside the region R8 connecting
p with q. On σp close to p we have the phase portrait W17 and close to q we have
W12. Therefore, in between, there must exist at least a bifurcation point. We now
show that on σp we have a bifurcation point for which the phase portrait has a saddle
to saddle connection. We ﬁrst note that in the whole of R8 we have the same kinds
of singularities, ﬁnite or inﬁnite. Furthermore, in the lower part of the x,y plane
the phase portraits have the same aspect: a canonical region bounded by a global
separatrix connecting an inﬁnite saddle, say S1 with an inﬁnite node say N1, by an
arc segment at inﬁnity and by a global separatrix with one end at the weak focus
and oriented towards an inﬁnite saddle, say S2. It is in the upper part that the phase
portraits could look different. At inﬁnity we have two more saddles: S ′
1 opposite
S1 having a local stable manifold W s
loc(S ′
1(λ)) and S ′
2 opposite S2 having an unstable
manifold W u
loc(S ′
2(λ)). Due to the analyticity of the systems in both x, y and in λ,
the local invariant manifolds have local equations depending analytically on x, y, λ,
(see [7], [29, p. 518 Appendice II] for proofs of the analyticity of the local invariant
manifolds which also work with parameters).1

By analytic continuation on solution curves, the local invariant manifolds are con-
tinued globally to W s( S ′
1(λ)) , W u( S ′
2(λ)) and have local equations F(x, y, λ) = 0,
G(x, y, λ) = 0 around any point (x0, y0, λ0), with F, G analytic in x, y, λ. Due to
the transversality of the ﬂow on x = 0 and due to the conﬁguration of the singulari-
ties at inﬁnity, both W s( S ′
1(λ)) , W u( S ′
2(λ)) cut the y-axis. Let y1(λ), y2(λ) be the
ﬁrst points where the two global invariant manifolds cut the y-axis. Due to the ana-
lytic version of the Implicit Function Theorem (IFT), applied respectively to the local
equations F(x, y, λ) = 0 and G(x, y, λ) = 0 of the two invariant manifolds around
the points ( 0, y1(λ)) , ( 0, y2(λ)) , the functions yi(λ) of λ are analytic. The hypoth-
esis of (IFT) is veriﬁed due to the analyticity of F and G and due to the transversality
of the ﬂow to x = 0. Hence the function f (λ) = y1(λ) − y2(λ) is analytic in λ
and deﬁned for all points in R8 belonging to a neighborhood Np of σp. In Np and

1We thank C. Rousseau for checking this and mentioning it to us.

https://doi.org/10.4153/CJM-2004-015-2 Published online by Cambridge University Press

334 Jaume Llibre and Dana Schlomiuk

close to Γ, f (λ) is positive (see phase portrait W 18) and close to a = 0 it is negative
(see W12). Hence by continuity, on σp there exists a point λ0 such that f (λ0) = 0,
which means that for λ0 we have a connection and the corresponding phase portrait
is W18. Let G3 be the set of all λ such that f (λ) = 0 when p runs over γ. Due to the
analyticity of f in λ, the set G3 is analytic.
Due to the analyticity of f (λ) on σp, there are only a ﬁnite number of solutions
of f (λ) = 0. It has been observed numerically that we actually have a unique such
solution which can be computed with as good an approximation as we wish. Varying
p in γ we get a continuous curve connecting the points [0 : −2 : 1] and a point ∆2 ∈ ∆
whose coordinates are given numerically as in [5]. At this point the phase portrait
is W18. Numerical computations show that the curve G3 has the qualitative shape
indicated in Figures 2 and 3.
We divide the curve ∆ into two arcs: ∆1, which is the open arc of ∆ having end-
points [0 : − 1 : 0] and the point ∆2, and the open arc ∆3 having endpoints ∆2 and
[0 : − 5 : 2].
Now we consider a sufﬁciently small open segment l = constant, having endpoints
on both sides of the curve ∆3. Thus at the endpoint inside R9 the phase portrait is
W14 and at the endpoint inside R8 and very near ∆3 the phase portrait is W17. Then
moving from W17 to W14 on this vertical segment we obtain that an inﬁnite saddle
and an inﬁnite node of W17 collide on ∆3 giving a saddle-node, and by continuity we
obtain the phase portrait W16 on ∆3. If we continue the motion the saddle-node at
inﬁnity disappears and we get the phase portrait W 14.
We note that the phase portraits W14, W16 and W17 have a limit cycle, due to the
instability of the strong focus and the behavior of the separatrix winding around the
strong focus and whose ω-limit set cannot thus be this strong focus. The uniqueness
of this limit cycle follows from previous arguments given at the beginning of this
section.
Let G = ∆1 ∪ ∆2 ∪ G3. G is the bifurcation curve which separates in D the phase
portraits having limit cycles from those without limit cycles. Then G = ∆1 ∪∆2 ∪G3.
We also denote G1 = ∆1 and G2 = ∆2.
From the above arguments, modulo uniqueness of the curve G3 which is observed
numerically, in 7.2 and 7.3 we have thus proved the following result.

Theorem 12 The bifurcation set of the class QW3 is formed by an algebraic set on
which we have bifurcations of saddle-node singularities and by an analytic set (G3) of
saddle-to-saddle connections. The bifurcation diagram of the class QW3, viewed in the
quarter of the disc D is as pictured in Figure 2 with its grey area enlarged in Figure 3, the
uniqueness and shape of the connection curve G3 being observed numerically.

8 Summing Up the Global Geometrical Properties of Quadratic
Systems with Third Order Foci: the Classiﬁcation Theorems

In a bifurcation diagram we may have topologically equivalent phase portraits be-
longing to distinct regions of the parameter space. In identifying two of the phase

https://doi.org/10.4153/CJM-2004-015-2 Published online by Cambridge University Press

Quadratic Differential Systems 335

portraits, counted as distinct in [5], we were helped by the integer-valued invariants
which we constructed. It is thus necessary to have a classiﬁcation in terms of simple
and, if possible integer-valued invariants. We give below such a classiﬁcation.
A crude grouping of the systems into classes according to their properties, was
given in terms of the values of NC in Corollary 7 of the preceding section. We shall
now split the three classes obtained into ﬁner ones by using the remaining three in-
variants: NR, f , deg(DI f ), NR,∞, the four invariants being ordered according to their
weight in the classiﬁcation problem. Knowledge of the ﬁrst invariants sometimes
determines the remaining ones and even implies, up to topological equivalence, a
unique phase portrait as indicated in the next theorem. Using these four invariants
we obtain a partition of the parameter space RP2.

Theorem 13 Consider the family QW3 of all quadratic systems with a weak focus of
third order. The values of the afﬁne invariant J(S) = ( NC, NR, f , deg(DI f ), NR,∞) (S)
given in the following diagram yield a partition of the family QW32 as follows:

NC(S) =
 




7 and NR, f (S) =
 




2 and deg( DI f (S)) =
 



0(W1),

2 and NR,∞(S) =
 {1(W14),
3,

4 and deg( DI f (S)) =
 



−2(W8),
0(W5),
2(W9),

6 and NR, f (S) =
 




1(W2),
2,

3 and deg( DI f (S)) =
 



−1(W3),
0(W7),
1(W6),
2(W10),
5(W4).

Furthermore, for each value of J(S) in this diagram with the exception of two cases:
(i) J(S) = (7, 2, 2, 3) which occurs in R8, and (ii) NC(S) = 6 and NR, f (S) = 2
which occurs on ∆, there corresponds a single phase portrait; i.e., if S and S ′ are such
that J(S) = J(S ′) and this common value does not satisfy (i) or (ii) above, S and S ′ are
topologically equivalent. This unique phase portrait has neither limit cycles nor graphics
(for the deﬁnition of a graphic see [15]), with the exception of the phase portrait W 14
corresponding to J(S) = (7, 2, 2, 1) which has a unique limit cycle. The phase portrait
W14 is the only one in the family QW3 having (two) complex singularities at inﬁnity in
addition to a real one.

2We point out that in the cases other than (i) and (ii), whenever just the ﬁrst component (or the ﬁrst
two components) of J(S) sufﬁce to yield a single phase portrait, we do not write the values of the remaining
invariants.

https://doi.org/10.4153/CJM-2004-015-2 Published online by Cambridge University Press

336 Jaume Llibre and Dana Schlomiuk

The above result follows from a careful analysis of the bifurcation diagram in Fig-
ures 2 and 3 of Section 9.

We now consider the cases (i) and (ii) left out in Theorem 13, i.e., the systems S
whose normal form (6) corresponds to λ ∈ R8 ∪ ∆. We deﬁne below some new
concepts.

Deﬁnition We consider the Poincar´e compactiﬁcation on the sphere. Let ¯H =
H ∪ S1 where H is the upper hemisphere and S1 is its equator. Let

DSep,∞ = ∑

W ∈S1 s(W )W, DSep, f = ∑

W ∈H s(W )W, DSep = ∑

W ∈ ¯H s(W )W

where s(W ) is the number of global nonequilibrium separatrices contained in H (or
in R2) which start or end at W . Let m∞ = maxW ∈S1 {s(W )} where s(W ) is deﬁned
as above.

There is a great difference between the divisor DSep,∞ on S1, the zero-cycles DSep, f
on R2, DSep on the semi-algebraic variety ¯H, and the previously deﬁned zero-cycles
or divisors. Indeed, DSep,∞, DSep, f , DSep depend on nontrivial global solutions which
are separatrices of the phase portrait. Clearly m∞ is a global integer-valued afﬁne
invariant.3

Remark 14 With the exception of two phase portraits: W 3 and W7, the type of the
zero-cycle DSep distinguishes the 18 phase portraits of quadratic systems having a
weak focus of third order. These two phase portraits are well distinguished by the
degree deg(DI f ) of the zero-cycle DI f . More precisely deg(DI f ) = 0 for W3 and
deg(DI f ) = −1 for W7.

It is not difﬁcult to prove that the only separatrices of polynomial vector ﬁelds on
the Poincar´e sphere are singular points, limit cycles and the boundary orbits of the
hyperbolic sectors of singularities; for more details see [26].
We denote by p ′
i the inﬁnite singular point diametrically opposed to the inﬁnite
singular point pi for the Poincar´e compactiﬁcation of a planar polynomial vector
ﬁeld.
We divide the open set R8 as follows: Ru
8 is the open subset of R8 whose boundary
is formed by the curves δ2 ∪ n8 ∪ L2; Rd
8 is the open subset of R8 whose boundary is
formed by the curves L2 ∪G; and Rdd
8 is the open subset deﬁned by R8 \( Ru
8 ∪cl(Rd
8)) ,
where as usual cl(A) denotes the closure of the set A.
We now deﬁne the full multi-integer-valued invariant which classiﬁes topologi-
cally all systems in QW3: I = ( NC, NR, f , deg(DI f ), NR,∞, deg(Dsep ), m∞) . Due to
Theorem 13, we only need to check the cases covered by (i) and (ii), left out in Theo-
rem 13. For Wi with i = 11, 12, 13, m∞ takes the values 1, 2, 3 respectively. For W16
and W17 we have Dsep = 7 but m∞ is 2 respectively 1. For W15 and W18, Dsep is 6 but
m∞ is 2, respectively 1. In short, we have obtained the following:

3For a good deﬁnition of a separatrix of a 2-dimensional ﬂow see, for instance, Newman [31].

https://doi.org/10.4153/CJM-2004-015-2 Published online by Cambridge University Press

Quadratic Differential Systems 337

Theorem 15 Let S and S ′ be quadratic systems having a weak focus of third order.
Then I(S) = I(S ′) if and only if S and S ′ are topologically equivalent.

We now sum up the global geometrical characteristics we have obtained for the
class QW3.

Theorem 16 The class QW3 is partitioned in the following three subclasses:

(I) Systems without a limit cycle and without graphics. We have a total of twelve such
phase portraits: Wi with i = 1, . . . , 12. The systems with Wi, i = 1, . . . , 10 are
classiﬁed by J(S) (see Theorem 13). J(S) = (7, 2, 2, 3) for W 11 and for W12 and
these phase portraits are distinguished by m∞. m∞ = 1 for W11 and m∞ = 2 for
W12.
(II) Systems with a limit cycle. These have no graphic and the limit cycle is unique.
These yield three phase portraits which are topologically classiﬁed by J(S). More
precisely we have: (II.1) J(S) = (7, 2, 2, 1) with phase portrait W 14;
(II.2) J(S) = (7, 2, 2, 3) with phase portrait W17; (II.3) J(S) = (6, 2, 2, 2) with
phase portrait W16 occurring as a bifurcation from (II.2) to (II.1), when two of the
three points at inﬁnity collide. (In Figure 3 the region where we have limit cycles is
delimited by the curves G and a = 0: λ ∈ R9 ∪ ∆3 ∪ Rdd
8 ).
(III) Systems with a graphic. These have no limit cycle and the graphic is unique, sur-
rounding a strong focus. We have exactly three phase portraits in this class. These
are: W18 with J(S) = (7, 2, 2, 3) and W13, W15, both with J(S) = (6, 2, 2, 2).
W13 is distinguished from W15 by m∞. For W13, m∞ = 3; for W15, m∞ = 2.

We note that if J(S) = (7, 2, 2, 3), S could be of any of the types (I), (II), (III).

9 Perturbations of Systems in the Class QW3

In this section we study the limit cycles which can bifurcate from a system in QW3
when we perturb it inside the class of all quadratic system with the topology of the
coefﬁcients.

Proposition 17 The following statement holds.

(a) At most one limit cycle could arise near the graphic, from a quadratic system corre-
sponding to a point on G1, in any perturbation of the system inside the class of all
quadratic systems. Furthermore, if this limit cycle exists, it is hyperbolic.

In addition there is numerical evidence for the following afﬁrmation:

(b) From the graphic corresponding to a quadratic system having its parameters on
the curve G2 ∪ G3, at most one limit cycle could arise near the graphic, in any
perturbation of the system inside the class of all quadratic systems. When this limit
cycle exists it is hyperbolic.

Proof We know explicitly the points of the algebraic curve G1. The graphics of the
systems associated to these parameters (see W13) are elementary (in the sense of [15]),

https://doi.org/10.4153/CJM-2004-015-2 Published online by Cambridge University Press

338 Jaume Llibre and Dana Schlomiuk

having two singular points, a saddle and a saddle-node, which satisfy the assumptions
of Theorem 1 of [15]. Therefore, the cyclicity of such a graphic is one, i.e., by a small
perturbation, at most one limit cycle could bifurcate near the graphic. If this limit
cycle exists it is hyperbolic (see again [15]). This proves statement (a).
The fact that G3 is analytic has been proved. But we could only determine its
position numerically. The graphic of a system W18 associated to a point of the analytic
curve G3, (see W18) is an elementary graphic having two saddles. Since the position
of G3 is only numerically determined, the assumptions in Theorem 1 of [15] are only
numerically veriﬁed for points on G3. The graphic of the system associated to the
point G2, (see W15) is elementary having two singular points, a saddle and a saddle-
node. The assumptions in Theorem 1 of [15] were numerically veriﬁed for the point
G2. So, we have (b).

Theorem 18 The following statements hold.

(a) Inside the class of all quadratic systems there exists a neighborhood U 1 of the systems
in QW3 which have neither a limit cycle nor a graphic, i.e., whose phase portrait is
Wi for some i = 1, . . . , 12 such that any quadratic system in U 1 has at most three
limit cycles.
(b) Inside the class of all quadratic systems there exists a neighborhood U 2 of the family
of systems in QW3 with phase portrait W13, such that any quadratic system in U2
has at most four limit cycles.

In addition there is numerical evidence for the following two afﬁrmations:

(c) Inside the class of all quadratic systems, there exists a neighborhood U 3 of the sys-
tems in QW3 with phase portraits Wi for i = 15, 18 such that any quadratic system
in U3 has at most four limit cycles.
(d) Inside the class of all quadratic systems, there exists a neighborhood U 4 of the sys-
tems in QW3 with phase portraits Wi for i = 14, 16, 17, such that any quadratic
system in U4 has at most four limit cycles.

Proof Consider a system corresponding to Wi for some i = 1, . . . , 10. This system
has a unique focus, the weak focus of third order and it has neither graphics, nor limit
cycles. For systems in a sufﬁciently small neighborhood of the system, their only limit
cycles are those produced by the weak focus and in view of Bautin’s theorem [6], there
could be at most three.
Consider now a system Wi for some i = 11, 12. This system has two foci, the weak
focus of third order and a strong focus, and it has neither graphics nor limit cycles.
For a sufﬁciently small perturbation within the quadratic family, the only limit cycles
which could be obtained are those produced by the weak focus. So, statement (a) is
proved.
A system with portrait W13 has two foci, the weak focus of third order and a strong
focus which is surrounded by a graphic. This system has no limit cycles. By Proposi-
tion 17(a), if the perturbation of W13 is sufﬁciently small within the quadratic family,
the only limit cycles which could be obtained are those produced by the weak focus

https://doi.org/10.4153/CJM-2004-015-2 Published online by Cambridge University Press

Quadratic Differential Systems 339

plus the unique one produced by the graphic. So, the perturbed system can have at
most four limit cycles. Hence, statement (b) is proved.
The point (c) is obtained by a similar argument used to show (b) but now since
the part (b) of Proposition 17(b) is numerical, we only have numerical evidence for
the statement (c).
A system with portrait Wi for i = 14, 16, 17 has two foci, (the weak focus of third
order and a strong focus which is surrounded by a unique limit cycle) and it has no
graphic. We have numerical evidence that this limit cycle is hyperbolic. Therefore, if
the perturbation of Wi is sufﬁciently small within the quadratic family, the only limit
cycles which could be obtained are those produced by the weak focus, and the one
which comes from the hyperbolic limit cycle. So, the perturbed system can have at
most four limit cycles. Hence, the statement (d) is obtained.

We remark that the statement (d) would be an analytical result if we knew that
the limit cycle of Wi for i = 14, 16, 17 is hyperbolic. In fact we only know, due
to Proposition 17(a), that the limit cycle of a system with W 14 is hyperbolic in a
neighborhood of the algebraic curve G1.

Deﬁnition As in [15] we call polycycle a graphic in the sense of [15] with a Poincar ´e
return map on a semitransversal section.
The next result follows easily from Theorem 18.

Corollary 19 Inside the class of all quadratic systems there exists a neighborhood of
the class of quadratic systems with a weak focus of third order and without any polycycle
or limit cycle such that any quadratic system in this neighborhood has at most 4 limit
cycles.

10 Concluding Comments

(I) We chose the class QW3 for two reasons: ﬁrst, because it seems to be next in line
to study after the family of systems with a center, systems studied in [50], [39] and
[33]. Second, this class plays a signiﬁcant role in Hilbert’s 16-th problem. Indeed, all
the quadratic systems which have been proven to have most limit cycles (at least four)
are obtained by perturbing systems in QW3. The ﬁrst known examples of quadratic
systems for which it was possible to show that they have at least four limit cycles
are the example of Shi Songling [44] and that of Chen and Wang [9]. Both these
examples are produced by perturbing systems S in the region of QW3 determined
by J(S) = (7, 2, 2, 1), i.e., in R9 of Figures 2 and 3. In the early 1980s it became
clear from the work [3] that there are two other distinct subsets of QW3 from which
two new types of phase portraits with at least four limit cycles could be obtained by
perturbations of systems in the class QW3. In this work we see these sets clearly on
Figures 2 and 3. These are the systems in Rdd
8 and on ∆3. The region where we have
limit cycles is bounded by the curve G and by points on a = 0 which correspond to
symmetric systems with two centers.
It is interesting to note that part of the boundary of the region in the parameter
space where we have limit cycles for QW3 is formed by systems with center and that it

https://doi.org/10.4153/CJM-2004-015-2 Published online by Cambridge University Press

340 Jaume Llibre and Dana Schlomiuk

is basically by perturbing systems with a center that the limit cycles are obtained. This
shows the close connection existing between the problem of the center and Hilbert’s
16-th problem. Among the systems with center located on a = 0 in Figures 2 and
3, the more degenerate ones lie, as expected, in the boundary of several regions Ri.
Naturally we expect that the study of their perturbations in the quadratic class will
be more complex. It is thus not surprising that the program outlined in [15] and
pursued in numerous articles has stopped short (so far) of proving the ﬁnite cyclicity
of graphics present in these more degenerate systems, such as for example the system
corresponding to the point λ = [0 : 1 : 0] in Figure 1.
(II) Zhang’s theorem (see point (vii) in Section 7.1) in [52, 53] was very help-
ful for proving more results here than in the previous studies [3, 2, 5], done before
this result was available. We also proved here the analyticity of the saddle-to-saddle
connection which was not proven in the above-mentioned works and gave the bi-
furcation diagram in just one picture representing the projective space, the adequate
parameter space for this classiﬁcation problem. The previous bifurcation diagrams
contained certain inaccuracies. Two phase portraits denoted by W 6 and W9, and
counted as distinct in [3], [5] are in fact topologically identical. The topological
equivalence of these phase portraits was only observed after we saw that these por-
traits were put into the same class by the ﬁrst components of the multi-integer-valued
invariant I(S). Two other phase portraits in the list in [5] turn out to be topologically
equivalent: W13 and W14. They are in fact distinct C ∞ phase portraits (we have a
node and a focus in one and two foci in the other) but topologically equivalent.
In [2] Andronova studied the class QW3 and constructed a bifurcation diagram
for this class. This was done in R3 by taking sections of the space obtained by making
l (denoted by k in [2]) constant for l = 0 or l ̸= 0. However her arguments on pages
122 and 124 of [2] where she deals with the more delicate cases, encountered by us in
the part of the half disc which we denoted by ∆ ∪ R8, are incomplete. She says4:

If the separatrices coalesce, then there must exist still another bifurcation curve, at
each point of which, a separatrix of a saddle (or of a saddle-node) goes from it to a
saddle. If the coalescence of separatrices does not occur, then on the curve ∆ = 0
for |a| > −l/(12√5) there could exist only the decomposition 36, . . . It is exactly
in this last case that we get the bifurcation diagram in Figure 22.

This paragraph contains an “if . . . if ” situation and she chooses one of the two cases
for the bifurcation diagram. We see numerically that actually it is the other situation
which occurs. Due to this, her description of the phase portraits on the bifurcation
curve where we only have two points at inﬁnity, (our curve ∆ in Figure 1), is correct
in only one part of this curve, as she says that the phase portraits on ∆ = 0 with
the exception of only one point, are all topologically equivalent. Actually on the
above mentioned curve we have three phase portraits. The phase portrait we denoted
here by W13 is missing from Andronova’s list. Although she notes the presence of a
bifurcation curve of connections in the area which in our Figure 3 is “inside” L2 but
not “inside” ∆, she does not observe that this curve may actually coincide with ∆ at

4This is an almost word for word translation of Andronova’s russian text by the authors.

https://doi.org/10.4153/CJM-2004-015-2 Published online by Cambridge University Press

Quadratic Differential Systems 341

some of the points. We see that this happens and so on the curve G we have three
phase portraits instead of just two.
(III) This work shows the importance of numerical work in such studies. It is
clear from her pictures that Andronova did not rely on numerical computations for
drawing the connection bifurcation and it is in part due to this that her work contains
the inaccuracy indicated above. The numerical computations performed in [5] which
could be made as accurate as we wish were very helpful is seeing more clearly what
actually occurs.
(IV) The invariants we used in this work are very simple and have a clear geomet-
ric meaning. In contrast to them, the algebraic invariants and comitants used in the
work of K. S. Sibirsky and his school (cf. [47]) are much more complicated. Those
invariants and comitants are deﬁned using tensors with their multi-index notation
and rather artiﬁcial-looking polynomial expressions deﬁned in terms of them. Clas-
siﬁcations are done using such polynomial expressions, see for example [32]. This
method is technically very complex, and the geometrical meaning is mostly missing.
The power of the method resides in its computational aspect: no matter how the sys-
tem may be presented, independent of particular chart and normal form, one can
compute the corresponding algebraic invariants and comitants and the computation
can be programmed on a computer.
Given the merits of both kinds of invariants it is thus natural to try to merge the
geometrical ones with the algebraic ones which are computationally very powerful.
Such a merger would yield easily accessible computations of the geometrical invari-
ants of systems for whatever normal form and would lend geometrical meaning to
the algebraic invariants.
This was done for the problem of classifying the quadratic differential systems
according to the topology of their phase curves in the neighborhood of the inﬁn-
ity [43]. This problem was ﬁrst studied in [32] using only algebraic invariants. In
[43], both geometric (integer-valued ones like here) and algebraic invariants were
used and the algebraic invariants were chosen to ﬁt better with the geometric ones.
A complete dictionary translating geometric into algebraic invariants is given. An
analogous work by Art´es, Llibre and Vulpe for the classiﬁcation of the quadratic dif-
ferential systems according to the topology of their phase curves in the neighborhood
of their ﬁnite singularities is almost completed. These works enable us to compute
most integer-valued invariants deﬁned in this article for systems given in whatever
normal form.

Acknowledgements We wish to thank Antonio Teruel for his help in drawing the
ﬁgures of this paper and Simon Guillotte for a larger scale version of Figure 1. Special
thanks are due to Robert Roussarie for his valuable suggestion concerning Proposi-
tion 17 and for the reference [16].

References

[1] A. A. Andronov, E. A. Leontoovich, I. I. Gordon and A. L. Maier, Qualitative theory of second-order
dynamic systems. John Wiley and Sons, New York, 1973.

https://doi.org/10.4153/CJM-2004-015-2 Published online by Cambridge University Press

342 Jaume Llibre and Dana Schlomiuk

[2] E. A. Andronova, Decomposition of the parameter space of a quadratic equation with a singular point
of center type and topological structure with limit cycles. Ph. D. Thesis, The Gorky Institute of Water
Transport Engineers, Gorky, Russia, 1988 (Russian).
[3] J. C. Art´es, Sistemes quadr`atics amb un focus feble de tercer ordre. Master’s Thesis, Universitat
Aut `onoma de Barcelona, 1984 (Catalan).
[4] J. C. Art´es and J. Llibre, Quadratic Hamiltonian vector ﬁelds. J. Differential Equations 107(1994),
80–95; 129(1996), 559–560.
[5] , Quadratic vector ﬁelds with a weak focus of third order. Publ. Mat. 41(1997), 7–39.
[6] N. N. Bautin, On the number of limit cycles which appear with the variation of coefﬁcients from an
equilibrium point of focus or center type. Transl. Amer. Math. Soc. 1(1962), 396–413.
[7] Ch. A. A. Briot et J. C. Bouquet, Recherches sur les fonctions d´eﬁnies par les ´equations diff´erentielles.
J. ´Ecole Polytechnique XXI(1856), 134–198.
[8] L. Cair ´o and J. Llibre, Phase portraits of planar semi-homogeneous systems I. Nonlinear Anal.
29(1997), 783–811.
[9] L. S. Chen and M. S. Wang, The relative position and number of limit cycles of the quadratic
differential systems. Acta Math. Sinica 22(1979), 751–758.
[10] B. Coll, A. Gasull and J. Llibre, Some theorems on the existence, uniqueness and non existence of limit
cycles for quadratic systems. J. Differential Equations 67 (1987), 372–399.
[11] W. A. Coppel, A survey of quadratic systems. J. Differential Equations 2(1966), 293–304.
[12] G. Darboux, M´emoire sur les ´equations diff´erentielles alg´ebriques du premier ordre et du premier
degr´e. (M´elanges) Bull. Sci. Math. (2) 2(1878), 60–96; 123–144; 151–200.
[13] H. Dulac, Sur les cycles limites. Bull. Soc. Math. France 51(1923), 45–188.
[14] F. Dumortier and P. Fiddelaers, Qualitative models for generic local 3-parameter bifurcations on the
plane. Trans. Amer. Math. Soc. 326(1991), 101–126.
[15] F. Dumortier, R. Roussarie and C. Rousseau, Hilbert’s 16-th problem for quadratic vector ﬁelds.
J. Differential Equations 110(1994), 66–133.
[16] , Elementary graphics of cyclicity 1 and 2. Nonlinearity 7(1994), 1001–1043.
[17] J. Ecalle, Introduction aux fonctions analysables et preuve constructive de la conjecture de Dulac.
Hermann, 1992.
[18] W. Fulton, Algebraic curves. An introduction to Algebraic Geometry. W. A. Benjamin, Inc., New York,
1969.
[19] E. A. Gonz´alez Velasco, Generic properties of polynomial vector ﬁelds at inﬁnity. Trans. Amer. Math.
Soc. 143(1969), 201–222.
[20] R. Hartshorne, Albegraic geometry. Graduate Texts in Math. 52, Springer, 1977.
[21] D. Hilbert, Mathematische Probleme. Lecture at the Second International Congress of
Mathematicians, Paris 1900; reprinted in Mathematical Developments Arising from Hilbert
Problems, (ed. F. E. Browder), Proc. Symp. Pure Math. 28, Amer. Math. Soc., Providence, RI, 1976,
1–34.
[22] Yu. Il’yashenko, Finiteness Theorems for Limit Cycles. Transl. Math. Monogr. 94, Amer. Math. Soc.,
1991.
[23] Chengzhi Li, Two problems of planar quadratic systems. Sci. Sinica 26(1983), 471–481.
[24] , Non-existence of limit cycles around a weak focus of order three for any quadratic system.
Chinese Ann. Math. Ser. B 7(1986), 174–190.
[25] Chengzhi Li, J. Llibre and Zhifen Zhang, Weak focus, limit cycles and bifurcations for bounded
quadratic systems. J. Differential Equations 115(1995), 193–223.
[26] Weigu Li, J. Llibre, M. Nicolau and Xiang Zhang, On the differentiability of ﬁrst integrals of two
dimensional ﬂows. Proc. Amer. Math. Soc. 130(2002), 2079–2088.
[27] V. A. Lunkevich and K. S. Sibirskii, Integrals of general quadratic differential systems in cases of a
center. Differential Equations 8(1982), 563–568.
[28] L. Markus, Global structure of ordinary differential equations in the plane. Trans. Amer. Math. Soc.
76(1954), 127–148.
[29] J. F. Mattei and R. Moussu, Holonomie et int`grales premi`eres. Ann. Sci. ´Ecole Norm. Sup. (4)
13(1980), 469–523.
[30] J. Milnor, Topology from the differential viewpoint. The University Press of Virginia, Charlottesville,
1972.
[31] D. A. Newman, Classiﬁcation of continuous ﬂows on 2-manifolds. Proc. Amer. Math. Soc. 48(1975),
73–81.
[32] I. Nikolaev and N. Vulpe, Topological classiﬁcation of quadratic systems at inﬁnity. J. London Math.
Soc. 55(1997), 473–488.
[33] J. Pal and D. Schlomiuk, Summing up the dynamics of quadratic Hamiltonian systems with a center.
Canad. J. Math. 49(1997), 583–599.

https://doi.org/10.4153/CJM-2004-015-2 Published online by Cambridge University Press

Quadratic Differential Systems 343

[34] , Intersection multiplicity and limit cycles in quadratic differential systems with a weak focus.
Preprint, September 1999, 40 pages.
[35] H. Poincar´e, M´emoire sur les courbes d´eﬁnies par les ´equations diff´erentielles. J. Math. Pures Appl. (4)
1(1885), 167–244; Oeuvres de Henri Poincar´e 1, Gauthier-Villars, Paris, 1951, 95–114.
[36] R. Roussarie, A note on ﬁnite cyclicity and Hilbert’s 16-th problem. Springer Lecture Notes in Math.
1331(1988), 161–168.
[37] , Smoothness property for bifurcation diagrams. Publ. Mat. 41(1997), 243–268.
[38] R. Roussarie and D. Schlomiuk, On the geometric structure of the class of planar quadratic
differential systems. Qualitative Theory Systems 3(2002), 93–122.
[39] D. Schlomiuk, Algebraic particular integrals, integrability and the problem of the center. Trans. Amer.
Math. Soc. 338(1993), 799–841.
[40] , Algebraic and Geometric Aspects of the Theory of Polynomial Vector Fields. In: Bifurcations
and Periodic Orbits of Vector Fields, (ed., D. Schlomiuk), 1993, 429–467.
[41] , Basic algebro-geometric concepts in the study of planar polynomial vector ﬁelds. Publ. Mat.
41(1997), 269–295.
[42] D. Schlomiuk and J. Pal, On the geometry in the neighborhood of Inﬁnity of Quadratic Differential
Systems with a Weak Focus. Qualitative Theory Systems 2(2001), 1–43.
[43] D. Schlomiuk and N. Vulpe, Geometry of quadratic differential systems in the neighborhood of the
inﬁnity. CRM-Report, CRM-2831, Universit´e de Montr´eal, December 2001, 41pp.
[44] Shi Songling, A concrete example of the existence of four limit cycles for planar quadratic systems. Sci.
Sinica 23(1980), 153–158.
[45] , A method of constructing cycles without contact around a weak focus. J. Differential
Equations 41(1981), 301–312.
[46] , On the structure of Poincar´e-Lyapunov constants for the weak focus of polynomial vector
ﬁelds. J. Differential Equations 52(1984), 52–57.
[47] K. S. Sibirsky, Introduction to the algebraic theory of invariants of differential equations. Nonlinear
Science: Theory and Applications. Manchester University Press, Manchester, 1988.
[48] J. Sotomayor, Lic¸´oes de equac¸´oes diferenciais ordin´arias. Projecto Euclides, IMPA, Rio de Janeiro,
1979.
[49] J. Sotomayor and R. Paterlini, Quadratic vector ﬁelds with ﬁnitely many periodic orbits. Springer
Lecture Notes in Math. 1007(1983), 753–766.
[50] N. I. Vulpe, Afﬁne-invariant conditions for the topological discrimination of quadratic systems with
center. Differential Equations 19(1983), 273–280.
[51] Ye Yanqian and Others, Theory of Limit Cycles. Transl. Math. Monogr. 66, Amer. Math. Soc., 1986.
[52] Zhang Pingguang, On the distribution and number of limit cycles for quadratic systems with two foci.
(chinese), Acta Math. Sinica 44(2001), 37–44.
[53] , On the distribution and number of limit cycles for quadratic systems with two foci.
Qualitative Theory Systems 3(2002), 1–28.
[54] H. ˙Zoła¸dek, Quadratic Systems with Center and Their Perturbations. J. Differential Equations
109(1994), 223–273.

Departament de Matem`atiques
Universitat Aut`onoma de Barcelona
08193 Bellaterra
Barcelona Spain
e-mail: jllibre@mat.uab.es
 D´epartement de Math´ematiques
et Statistique
Universit´e de Montr´eal
C.P. 6128, Succ. Centre-Ville
Montr´eal, Qu´ebec
H3C 3J7
email: dasch@dms.umontreal.ca

https://doi.org/10.4153/CJM-2004-015-2 Published online by Cambridge University Press
