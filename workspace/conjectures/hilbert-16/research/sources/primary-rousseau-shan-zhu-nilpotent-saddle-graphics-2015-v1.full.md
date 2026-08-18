<!-- source: https://arxiv.org/pdf/1502.00689v1 | converted from PDF -->

Finite cyclicity of some graphics through a nilpotent
point of saddle type inside quadratic systems
∗

Christiane Rousseau
a, Chunhua Shan
b and Huaiping Zhu
c

a Department of Mathematics and Statistics and CRM,
University of Montreal, Montreal, Canada H3C 3J7
bDepartment of Mathematical and Statistical Sciences,
University of Alberta, Edmonton, Canada T6G 2G1
c Department of Mathematics and Statistics and LAMPS,
York University, Toronto, Canada, M3J 1P3

Abstract. In this paper we show the ﬁnite cyclicity of the two graphics (I 1
12) and (I 1
13) through a
triple nilpotent point of saddle type inside quadratic vector ﬁelds. These results contribute to the
program launched in 1994 by Dumortier, Roussarie and Rousseau (DRR program) to show the
existence of a uniform upper bound for the number of limit cycles for planar quadratic vector
ﬁelds.

Key words. Nilpotent saddle; Graphics; Cyclicity; DDR program; Poincar´e ﬁrst return map;
Finiteness part of Hilbert’s 16th problem.

1 Introduction

Hilbert’s 16th problem, second part, asks for the maximum number of limit cycles, called
H(n), as well as the relative positions of limit cycles of a polynomial vector ﬁeld P (x, y) ∂
∂x +
Q(x, y) ∂
∂y as a function of n = max(deg(P ), deg(Q)). It is still unknown whether H(n) is
ﬁnite. The DRR program started in 1994 by Dumortier, Roussarie and Rousseau ([1]) produces
a procedure to prove that H(2) < ∞. The underlying idea is a compactness argument. Indeed,
polynomial vector ﬁelds can be extended to the Poincar´e sphere S
2 by adding points at inﬁnity
in all directions. The number of limit cycles of a vector ﬁeld depends only on its equivalence
class under afﬁne transformations and time rescalings. Also, limit cycles in quadratic vector
ﬁelds necessarily surround a unique singular point with nondegenerate linear part, and linear
vector ﬁelds can have no limit cycles. Hence, it is possible to compactify the space of equiva-
lence classes of quadratic vector ﬁelds with a nondegenerate singular point of anti-saddle type:
this yields a compact parameter space K. Limit cycles in the compact set S
2 ×K accumulate on

∗This research was supported by NSERC of Canada
 1arXiv:1502.00689v1  [math.CA]  3 Feb 2015
(a) (I 1
12) (b) (I 1
13)

Figure 1: Graphics for which we prove ﬁnite cyclicity

graphics, which are unions of trajectories and singular points for a given value of the parame-
ters. The DRR program reduces the proof that H(2) < ∞ to the proof that each graphic Γ ⊂ S
2

surrounding a nondegenerate singular point of anti-saddle type and occurring for a parameter
value A0 ∈ K has ﬁnite cyclicity in S
2 × K, i.e. can produce only a ﬁnite number of limit
cycles in a neighborhood U of Γ for parameter values A in a neighborhood V of A0. Achieving
the DRR program requires proving the ﬁnite cyclicity of 121 graphics in S
2 × K. This program
has stimulated the development of highly sophisticated methods to treat problems of increasing
complexity. The graphics can be grouped in large classes and the strategy is to treat one class
at a time. In this paper, we prove that the two graphics through a nilpotent point of saddle type,
(I 1
12) and (I 1
13), that do not surround a center, have ﬁnite cyclicity. Therefore the results from
this paper will bring the number of graphics of the program for which ﬁnite cyclicity is proved
to 88.

In practice, in this paper we address the following questions:

(1) We ﬁrst show that a generic graphic through a nilpotent saddle of multiplicity 3 has ﬁnite
multiplicity in the case where one connection is ﬁxed. The case of codimension 3 was
already treated in [7] and it sufﬁces to treat the case a = − 1
2 corresponding to b = 0 in
the DRS normal form ([3]).

(2) In quadratic systems, we show that the genericity condition is met for (I 1
12). This amounts
to show that the integral of the divergence along the invariant parabola is nonzero. Note
that the same computation shows the ﬁnite cyclicity of (I 2
9b) when the codimension of the
point is 3 (corresponding to ϵ2 ̸= 0 in [3]).

(3) We show that a generic graphic through a nilpotent saddle of multiplicity 3 and a saddle-
node with central transition has ﬁnite multiplicity in the case where one connection is
ﬁxed. As an application, this yields the ﬁnite cyclicity of the graphic (I 1
13) inside quadratic
systems.
 2

2 Preliminaries

2.1 Normal form for the unfolding of a nilpotent triple point of saddle
type

We consider graphics through one singular point, which is a triple nilpotent point of saddle type.
A germ of vector ﬁeld in the neighborhood of such a point has the form

˙x = y
˙y = x3 + bxy + ηx
2y + yO(x3) + O(y2). (2.1)

The unfolding of such points has been studied by Dumortier, Roussarie and Sotomayor, [3],
including a normal form for the unfolding of the family. A different normal form has been
used in [7] for studying the ﬁnite cyclicity of generic graphics through such singular points,
which is particularly suitable for applications in quadratic vector ﬁelds, where there is always
an invariant line through a nilpotent point of multiplicity 3.

Indeed, a germ of C ∞ vector ﬁeld in the neighborhood of a nilpotent point of multiplicity 3
of saddle type can be brought by an analytic change of coordinates to the form

˙x = y + ax2,
˙y = y(x + ηx
2 + o(x2) + O(y)), (2.2)

with a < 0 (see Figure 2).
 Figure 2: A nilpotent saddle

A generic unfolding depending on a multi-parameter λ = (µ1, µ2, µ3, µ) in a neighborhood
of the origin has the form

˙x = y + a(λ)x2 + µ2,
˙y = µ1 + µ3y + x4h1(x, λ) + y(x + ηx
2 + x3h2(x, λ)) + y2Q(x, y, λ), (2.3)

where h1(x, λ) = O(|λ|). Moreover, h1, h2, Q are C ∞ functions, and Q can be chosen of
arbitrarily high order in λ.
 3

2.2 Finite cyclicity of a graphic

Deﬁnition 2.1. A graphic Γ of a vector ﬁeld X0 , i.e. a union of trajectories and singular points,
has ﬁnite cyclicity inside a family Xλ if there exists N ∈ N, ϵ > 0 and δ > 0 such that any
vector ﬁeld Xλ with |λ| < δ has at most N periodic solutions at a Hausdorff distance less than
ϵ from Γ. The minimum value N is the cyclicity of the graphic.

When studying the ﬁnite cyclicity of a graphic Γ, we need to ﬁnd a uniform bound for the
number of periodic solutions that can appear from it, for all values of the multi-parameter in a
small neighborhood W of the origin. Typically, we need to ﬁnd a uniform bound for the number
of ﬁxed points of the Poincar´e return map or, equivalently, for the number of zeros of some
displacement map between two transversal sections to the graphic. With graphics containing
a nilpotent singular point there is no way to make a uniform treatment for all λ ∈ W , and we
cover W by an inﬁnite number of sectors with conic structure, one around each direction in
parameter space. On each sector, we give a uniform bound for the ﬁnite cyclicity. Since the set
of directions in parameter space is compact, we extract a ﬁnite subcovering: the maximum of
the cyclicities on each sector of the covering is the cyclicity of the graphic Γ. The method for
doing this is the blow-up of the family, which was ﬁrst introduced by Roussarie.

2.3 Blow-up of the family

Let us make the change of parameters

(µ1, µ2, µ3) = (ν3µ1, ν2µ2, νµ3). (2.4)

We take a neighborhood of the origin in parameter-space of the form S
2 × [0, ν0) × U , where U
is a neighborhood of 0 in µ-space, M = (µ1, µ2, µ3) ∈ S
2 and ν ∈ [0, ν0).

Note that S
2 is compact. Hence, to give an argument of ﬁnite cyclicity for the graphic Γ,
it sufﬁces to ﬁnd a neighborhood of each M = (µ1, µ2, µ3) ∈ S
2 inside S
2, a corresponding
ν0 > 0 and a corresponding U on which we can give a bound for the number of limit cycles. In
our study, we will consider special values a0 of a. It is important to note that a(λ) depends on
λ, and hence that a − a0 is a parameter in itself.

The way to handle this program is to do a blow-up of the family, a technique developed
by Roussarie. For this, we introduce the weighted blow-up of the singular point (0, 0, 0) of
the three-dimensional family of vector ﬁelds obtained by adding the equation ˙ν = 0 to the
2-dimensional system (2.3). The blow-up transformation is given by

(x, y, ν) = (rx, r2y, rρ), (2.5)

with r > 0 and (x, y, ρ) ∈ S
2. After dividing by r the transformed vector ﬁeld, we get a
family of C ∞ vector ﬁelds X A, depending on the parameters A = (a − a0, M , µ). The foliation
{ν = rρ = Const} is invariant under the ﬂow. The leaves {rρ = ν} with ν > 0 are regular
two-dimensional manifolds, while the critical locus {rρ = 0} is stratiﬁed and contains the two
strata (see Figure 3):
 4

• S
1 × R
+ is the blow-up of X0 (for λ = 0);

• Dµ = {x2 + y2 + ρ2 = 1 | ρ ≥ 0}.

2.4 Limit periodic sets in the blow-up family

The strategy for studying the ﬁnite cyclicity of Γ is the following. We study the singular points
of X on r = ρ = 0. For a ̸= 1
2, there will be four distinct singular points (occuring in two
pairs) corresponding to y = 0 (for P1 and P2) and y = 1−2a
2 (for P3 and P4): see Figure 3. Their
eigenvalues appear in Table 2.4.

P
 4P P3
 P21

Figure 3: The stratiﬁed set {rρ = 0} in the blow-up.

r ρ y
P1 −a a −(1 − 2a)
P2 a −a (1 − 2a)
P3 1/2 −1/2 −(1 − 2a)
P4 −1/2 1/2 (1 − 2a)

Table 1: The eigenvalues at Pi (i = 1, 2, 3, 4)

In this paper we study the ﬁnite cyclicity of a graphic Γ joining P3 and P4. We consider a
particular value A0 = (a0, M 0). Here is the strategy for ﬁnding an upper bound for the number
of limit cycles that appear for A in a neighborhood of A0. We determine the phase portrait
of the family rescaling (2.6) on Dµ: this allows determining limit periodic sets Γ, which are
formed by the union of Γ with a ﬁnite number of trajectories and singular points on Dµ joining
P4 and P3, so that their orientation will be compatible with that of Γ. The limit periodic sets to
be studied appear in Table 2. They are continuous families of limit periodic sets. We use the
convention to label the different types: Sxhhia, Sxhhib, etc, starting from the top. For instance,
Sxhh1a corresponds to the boundary upper limit periodic set, Sxhh1b corresponds to any of the
intermediate limit periodic set, and Sxhh1c corresponds to the lower periodic set through the
saddle point. They come from studying the phase portrait of the family rescaling

˙x = y + ax2 + µ2,
˙y = µ1 + µ3y + xy, (2.6)

5

obtained by putting ρ = 1 and r = 0. It then sufﬁces to show that each limit periodic set has
ﬁnite cyclicity, i.e. to show the existence of an upper bound for the number of periodic solutions
of X A for A in a small neighborhood of A0.

Sxhh1 Sxhh2 Sxhh3

Sxhh4 Sxhh5 Sxhh6

Sxhh7 Sxhh8

Sxhh9 Sxhh10

Table 2: Convex limit periodic sets of hh-type for a graphic with a nilpotent saddle

2.5 Proving the ﬁnite cyclicity of a limit periodic set

The following argument will be used for proving the ﬁnite cyclicity of a limit periodic set: limit
cycles correspond to ﬁxed points of a Poincar´e return map deﬁned on a section or, equivalently,
to zeroes of a displacement map between two sections. The sections are 2-dimensional but,
because of the invariant foliation, the problem can be reduced to a 1-dimensional problem and
the conclusion follows by a derivation-division argument.

To compute the displacement map, we decompose the related transition maps between sec-
tions into compositions of Dulac maps in the neighborhood of the singular points and regular
C k transitions elsewhere.
 6

2.6 Dulac maps

The Dulac maps have been computed in [7]. There are two types of Dulac transitions. The ﬁrst
type of transition map goes from a section {r = r0} to a section {ρ = ρ0}, or the other way
around. This type of transition typically behaves as an afﬁne map which is a very strong con-
traction or dilatation. The study of the number of zeroes of a displacement map involving only
Dulac maps of the ﬁrst type is reduced to the study of the number of zeroes of a 1-dimensional
map.

The second type of Dulac map is concerned with a transition from a section {y = y0} to,
either a section {r = r0}, or a section {ρ = ρ0}. Here we only need the ﬁrst type of Dulac map.
We recall the precise results here.

2.6.1 First type of Dulac map

We consider a Dulac map Di from a section Πi = {ρ = ρ0} to a section Σi = {r = r0} in the
neighborhood of a singular point Pi (potentially following the ﬂow backwards). We decide to
choose (ν, ˜yi) as coordinates on the sections Πi and Σi, where ˜yi is a normalizing coordinate for
the blow-up system in the neighborhood of Pi. The normal form near Pi is given by

˙r = r,
˙ρ = −ρ,
˙˜yi = G(r, ρ, ˜yi),
 (2.7)

where
 G(r, ρ, ˜yi) =
 



˜yi(−σ + ϕi(ν)), σ0 /∈ Q,
˜yi(−σ + ϕi(ν) + fi(rp ˜yi)) + ηi(ν)ρp, σ0 = p ∈ N,
˜yi(−σ + ϕi(ν) + fi(rp ˜yq
i )), σ0 = p
q , q > 1 (2.8)

where
 σ =
 {
2(1 − 2a) = 2(1 − 2a0) + α, i = 3, 4,

2a−1
a = 2a0−1
a0 + α, i = 1, 2.

Deﬁnition 2.2. The compensator ω is a univeral unfolding of the function − log x, namely

ω(x, α) =
 { x−α−1
α , α ̸= 0,
− log x, α = 0. (2.9)

The form of the Dulac map was ﬁrst studied in [7]. The following form is a reﬁnement from
[6].

Theorem 2.3. We consider the Dulac map from the section {ρ = ρ0} to the section {r = r0},
both parametrized by (˜yi, ν). Let ν0 = r0ρ0 and

¯σi = σ − ϕi(ν) = σ0 + αi. (2.10)

The ˜yi-component of the transition map Di has the following expression:

7

1. If σ0 ̸∈ Q :
 Di(˜yi, ν) = ( ν
ν0
 )¯σ ˜yi. (2.11)

2. If σ0 = p
q ∈ Q with (p, q) = 1:

Di(˜yi, ν) = ηi(ν)ρp
0( ν
ν0
 )¯σω( ν
ν0 , αi) + ( ν
ν0
 )¯σ(˜yi + φi(˜yi, ν, )
), (2.12)

where

• φi = O (νp+qαiωq+1 ( ν
ν0 , αi) | ln ν|
) and for any integer l ≥ 2, φµ,σ is of class Cl−2

in (˜yi, ν1/l, ν1/lω ( ν
ν0 , αi) , ν, µ, σ);

• ηi is as in (2.8). In particular, ηi ≡ 0 when σ0 ̸∈ N.

Remark 2.4. It follows from the form of φ as a function of class Cl−2 on the generalized mono-
mials ˜yi, ν1/l and ν1/lω ( ν
ν0 , αi) that all its derivatives with respect to ˜yi of small order are

O(νβ) for some β > 0. We say that φ has property J.

2.7 Dulac map near a hyperbolic or semi-hyperbolic point

When considering limit periodic sets, we will have additional singular points on them, and their
associated Dulac maps. These can be explicitly calculated when the system is in C k normal
form. We recall very brieﬂy the form of these Dulac maps.

Theorem 2.5. We consider a polynomial normal form for a family depending on a multi-
parameter A, in the neighborhood of a hyperbolic saddle point with eigenvalues λ1(A) >
0, −λ2(A) < 0. The hyperbolicity ratio is deﬁned as the quotient τ = λ2(A)
λ1(A) . If the system near
the saddle has the following C k normal form for A close to A0 :

˙x = λ1(A)x,
˙y = −λ2(A)y(1 + Q(x, y)), (2.13)

with
 Q(x, y) =
 {
0, τ (A0) /∈ Q+,
∑K
i=1 ci(A)(xpyq)
i, τ (A0) = p
q ,

then the Dulac map from {y = Y0} to {x = X0} is of the form

DA(x) = Y0X −τ (A)
0 xτ (A)(1 + φ(x, A)),

where φ has the property I of Mourtada given in Deﬁnition 2.6 below. Note that φ ≡ 0, when
τ (A0) /∈ Q.

In the particular case τ (A0) = 1, we need the more reﬁned form

DA(x) = Y0X −τ (A)
0 (x + αxω(x, α) + φ(x, A))

where ω is the compensator deﬁned in (2.9), τ = 1 − α, and φ has the property I of Mourtada,
with φ(x, A) = O(x1+δ) for some δ > 0.
 8

Deﬁnition 2.6. A function φ(y, A) has the property (I) of Mourtada if φ is C K for some K on
(0, y0) × W , where W is a neighborhood of A0 in A-space, and if there exists some neighbor-
hood W ′ of the origin in A-space such that for all 0 ≤ j ≤ K,

lim
y→0 yi ∂jφ
∂yj (y, λ) = 0,

uniformly for λ ∈ W ′.

Theorem 2.7. [2] We consider a polynomial normal form for a family depending on a multi-
parameter A in the neighborhood of a saddle-node with eigenvalues 0, −λ < 0, for A = A0. If
the system has the following normal form near the saddle-node

˙x = (x2 + η(A))(1 + C(A)x2) = F (x),
˙y = −λy, (2.14)

with η(A0) = 0, then

1. Case of central transition: for η > 0, the Dulac map from {x = −X0} to {x = X0} is
linear of the form DA(y) = ϵ(A)y, with ϵ(A) > 0 exponentially small in √η;

2. Case of stable-center transition: the Dulac map DA(x) from {y = Y0} to {x = X0} is
ﬂat in x, as well as all its partial derivatives in x and in the parameters.

3 Finite cyclicity of convex graphics through a nilpotent sad-
dle of multiplicity 3

It was shown in [7] that a graphic through a nilpotent saddle of codimension 3 has ﬁnite cyclicity
as soon as the ﬁrst return map along the graphic has a derivative different from 1. This excludes
the value a0 = − 1
2 in (2.3). This hypothesis was only used in studying the ﬁnite cyclicity of the
limit periodic sets in Sxhh1 and Sxhh5. We now consider the case a0 = − 1
2. We show that all
limit periodic sets in Sxhh1 have ﬁnite cyclicity. Under the additional hypothesis that the line
on the blow-up sphere is a ﬁxed connection, we also show that all limit periodic sets in Sxhh1
have ﬁnite cyclicity.

Theorem 3.1. We consider a convex graphic through a nilpotent saddle of multiplicity 3 with
a0 = − 1
2 and such that the derivative of the ﬁrst return map γ∗ = P ′(0) ̸= 1. Then all limit
periodic sets in Sxhh1 have ﬁnite cyclicity.

Proof. Without loss of generality we can suppose that the limit periodic set Γ joins P3 and
P4 (see Figure 3). Note that the ﬁnite cyclicity of the upper boundary graphic of Sxhh1 was
proved in [7]. Therefore, we only need to prove that the intermediate graphics Sxhh1b and the
lower boundary graphic of Sxhh1c have ﬁnite cyclicity. The only place where the hypothesis
a0 ̸= − 1
2 was used in [7] is when the hyperbolicity ratio τ (M 0) (i.e. the quotient of minus
the negative eigenvalue to the positive one) is equal to 1 at the saddle point of (2.6). Since

9

D3D4
 34
 34
 R

T

Figure 4: Transition map for the hh-graphics of saddle type

the divergence of (2.6) is identically equal to ¯µ3 for a0 = − 1
2, we need only consider the case
A0 = (− 1
2, µ1, µ2, 0, 0).

Let Γ be any intermediate or lower boundary graphic of Sxhh1. To study its cyclicity, we
take coordinates (r, ρ, yi) in the neighborhood of Pi, i = 3, 4, where r = x (resp. −x) for P3
(resp. P4) and yi = y − 1−2a
2 (hence yi = 0 at Pi). A C k-change of coordinates to normal form
in the neighborhood of Pi can be taken of the form ˜yi = yi + fi(r, ρ, yi). Let us take sections
Σi = {r = r0} and Πi = {ρ = ρ0} as shown in Fig. 4 in the normal form coordinates (r, ρ, ˜yi)
in the neighborhood of the singular point Pi (i = 3, 4). We will study the displacement map
L : Π4 −→ Σ3 deﬁned by L = R−1 ◦ D4 − D3 ◦ T, (3.1)

where R : Σ3 −→ Σ4 and T : Π4 −→ Π3 are the transition maps along the regular orbits in the
normal form coordinates, and Di : Πi −→ Σi are the Dulac maps. We will study the maximum
number of small roots of L = 0.

We decide to choose (ν, ˜yi) as coordinates on the sections Πi and Σi. The maps R and T
are two-dimensional but, since they preserve the ν-coordinate, we will cheat a little and identify
them with their second component which depends on ν, and which we denote Rν and Tν. We
denote by Lν the corresponding second component of L in (3.1). For ν ∈ [0, ν0), Rν and Tν are
regular C k-diffeomorphisms. Let Sν = R−1
ν . The Dulac maps Di near P4 (following the ﬂow
backwards) and near P3 are calculated in Theorem 2.3, with σ0 = 4.

Let α34 = σ3 − σ4 = νO(1).

The map Lν has the form

Lν(˜y) = m0(ν, λ) + ( ν
ν0
 )σ3 [
T ′
ν(0) − S′
ν(0) ( ν
ν0
 )−α34 + O(ν)

]
 ˜y4 + ( ν
ν0
 )σ3 o(˜y4). (3.2)

10

It is clear that an intermediate graphic has cyclicity 1 as soon as T ′
ν(0)−S′
ν(0)νσ4−σ3 is bounded
away from 0 for A in a neighborhood of A0 = (− 1
2, M 0, 0). This is precisely the case when
T ′
ν(0) is close to 1. Indeed, we know that S′
ν(0) ̸= 1. Also,

( ν
ν0
 )−α34 = e−α34 log(ν/ν0) = 1 + O(ν1−δ)

for some small δ, since α34 = O(ν). Hence, it sufﬁces to show that T ′
0(0) = 1 when A0 =
(− 1
2, µ1, µ2, 0, 0). We show the stronger property that T0 ≡ id for such an A0. For this purpose,
we use that the system (2.6) is Hamiltonian for a = − 1
2 and µ3 = 0: the trajectories are level
curves H(x, y) = C of the Hamiltonian

H(x, y) = 1
2 y2 − 1
2x2y + µ2y − µ1x.

Hence, we must explain the link between the constant C and the corresponding normalizing co-
ordinates ˜y3 (resp. ˜y4) on Π3 (resp. Π4). For this, we must not forget that the family rescaling has
been obtained by putting ρ = 1 after the blow-up. For r = 0, the system in (ρ, y)-coordinates
is given by
 ˙ρ = ∓ρ(y − 1
2 + µ2ρ
2),

˙y = ±2y ∓ 2y2 ∓ 2µ2yρ
2 + µ1ρ3, (3.3)

where the sign + (resp. −) comes from putting x = +1 (resp x = −1). The function ρ−5 is an
integrating factor of (3.3), which yields ﬁrst integrals

H ± = y2

2ρ4 − y
2ρ4 + µ2 y
ρ2 ∓ µ1 1
ρ .

We need to localize at P3 and P4 by letting z = y − 1. Then

H ± = z2

2ρ4 + z
2ρ4 + µ2 z + 1
ρ2 ∓ µ1 1
ρ ,

which means that the trajectories are given by

Z = z2

2 + z
2 + µ2(z + 1)ρ2 ∓ µ1ρ3 = C±ρ4,

The change of coordinate z ↦→ Z is invertible for small z and is precisely the normalizing
coordinate. Then it is easy to see that on sections Π3 and Π4 with common equation {ρ = ρ0}
we have ˜y3 = C+ρ4
0 and ˜y4 = C−ρ
4
0, and also that C+ = C = C− for a given trajectory. Hence
T0 ≡ id, which means that T ′ is close to 1 for A close to A0 in the neighborhood of the limit
periodic set.

We now only need to consider the lower graphic Sxhh1c for A0 = (− 1
2, µ1, µ2, 0, 0). Let
τ (M ) = 1 − α be the hyperbolicity ratio at the saddle point of (2.6).

11

Using Theorem 2.5, the regular transition near the hyberbolic saddle in suitable normal form
coordinates has the form

Vν(˜y) = m0(A) + m1(A)αω(˜y, α)˜y + m2(A)˜y + O (˜y2 ω(˜y, α)
) ,

with m0(A0) = m1(A0) = m2(A0) − 1 = 0, which yields that the transition map Tν has the
form
 Tν(˜y3) = n0(A) + n1(A)α˜y3ω(˜y3, α)(1 + φ1(˜y3, α))

+ n2(A)˜y3(1 + φ2(˜y3, α)) + O (˜y2 ω(˜y, α)) , (3.4)

with n0(A0) = n1(A0) = n2(A0) − 1 = 0, where the functions φj have the property (I) of
Mourtada (see Deﬁnition 2.6).

This yields that Lν(˜y3) has the form

Lν(˜y3) = ˜n0(A, ν) + n1(A, ν) ( ν
ν0
 )σ3 α˜y3ω(˜y3, α)(1 + ψ1(˜y3, ν))

+ ( ν
ν0
 )σ3 [
n2(Aν) − S′
ν(0) ( ν
ν0
 )α34 + O(ν)
] ˜y3(1 + ψ2(˜y3, ν)),
 (3.5)

where ˜n0(A0, 0) = α(A0, 0) = 0. Let ˜n2(A, ν) = n2(Aν) − S′
ν(0) ( ν
ν0
 )α34 + O(ν), then we
have ˜n2(A0, 0) ̸= 0. ψ1, ψ2 are ﬁnite sums of products of functions with property (I) or (J).

By Rolle’s theorem, the number of zeroes of Lν is at most 1 plus the number of zeroes of

N1,ν(˜y3) = ( ν
ν0
 )−σ3 dL
d˜y3 (˜y3). Considering that the derivative of ω(˜y3, α) is 1 + αω(˜y3, α), we
have
 N1,ν(˜y3) = n1(A, ν)[(1 − α)ω(˜y3, α) − 1](1 + ξ1(˜y3, ν)) + ˜n2(A, ν)(1 + ξ2(˜y3, ν)),

where ξ1, ξ2 are ﬁnite sums of functions with property (I) and (J). The number of zeroes of
N1,ν(˜y3) is the same as the number of zeroes of

N2,ν(˜y3) = N1,ν(˜y3)
[(1 − α)ω(˜y3, α) − 1](1 + ξ1(˜y3, ν)).

By Rolle’s theorem again, this number is at most 1 plus the number of zeroes of N3,ν(˜y3) =
dN2,ν
d˜y3 (˜y3), given by

N3,ν(˜y3) = −˜n2(A, ν) (1 − α)˜y−1−α
3
[(1 − α)ω(˜y3, α) − 1]2 (1 + χ2(˜y3, ν)) ̸= 0,

with χ2 a sum of functions with property (I) and (J), since it is standard that xnω(x, α) is small
for positive n and small (x, α).

Theorem 3.2. We consider a convex graphic through a nilpotent saddle of multiplicity 3 with
a0 = − 1
2 passing through the points P3 and P4 of the blow-up, and such that the derivative of
the ﬁrst return map γ∗ = P ′(0) ̸= 1. We also suppose that there is a ﬁxed connection on the
blow-up sphere along a line joining P1 and P2 (corresponding to µ1 = 0 in (2.3). Then all limit
periodic sets in Sxhh5 have ﬁnite cyclicity.
 12

Proof. The proof is very similar to that of Theorem 3.1. When µ3 ̸= 0, then the product of
the hyperbolicity ratios τ1τ2 at the two saddle points is different from 1, and the ﬁnite cyclicity
was proven in [7]. When µ3 = 0, then the family rescaling (2.6) is integrable, both because
it is symmetric and Hamiltonian. Hence, for the intermediate limit periodic sets, the transition
map Tν is close to the identity. As for the lower periodic set through the two saddle points, the
transition map Tν has the same form as in (3.4) with τ = τ1τ2 = 1 − α.

Remark 3.3. We conjecture that the hypothesis that µ1 = 0 in Theorem 3.2 can be dropped,
but we have not been able to prove it.

Corollary 3.4. We consider a convex graphic through a nilpotent saddle of multiplicity 3 with
a0 = − 1
2 passing through the points P3 and P4 of the blow-up, and such that the derivative of
the ﬁrst return map γ∗ = P ′(0) ̸= 1. We also suppose that there is a ﬁxed connection on the
blow-up sphere along a line joining P1 and P2. Then the graphic has ﬁnite cyclicity.

Proof. All limit periodic sets except Sxhh1 and SXhh5 were proved in [7] to have ﬁnite cyclic-
ity for any a0 negative. And we have proved the ﬁnite cyclicity of SXhh1 and Sxhh5 in Theo-
rems 3.1 and 3.2.

4 Applications to quadratic systems

4.1 Quadratic systems with a nilpotent singular point at inﬁnity

Proposition 4.1. A quadratic system with a triple singular point of saddle or elliptic type at
inﬁnity and a ﬁnite singular point of focus or center type can be brought to the form

{ ˙x = δx − y + Bx2

˙y = x + γy + xy. (4.1)

The value of “a” in the corresponding normal form (2.3) is a = 1 − B. Moreover

1. When B > 1, the singular point is a nilpotent saddle.

2. For B ̸= 0, 1
2, the system has an invariant parabola

y = (B − 1
2)x2 + (2 − 1
B )δx − B + (1 − 2B)δ2

2B2 (4.2)

if γB − (1 − 2B)δ = 0. (4.3)

3. The nilpotent saddle point is of codimension 4 when B = 3
2 (corresponding to a = − 1
2).

4. The integrability condition is γ = δ = 0.

13

Proof. We can suppose that the nilpotent singular point at inﬁnity is located on the y-axis, the
other singular point at inﬁnity on the x-axis and the focus or center at the origin. Then the
system can be brought to the form
{ ˙x = δ10x + δ01y + δ20x2 + δ11xy
˙y = γ10x + γ01y + γ11xy + γ02y2. (4.4)

For the ﬁnite singular point to be a focus or center, we should have δ10γ01 − δ01γ10 > 0.

Localizing the system (4.4) at the singular point at inﬁnity on y-axis by v = x
y , z = 1
y , we
have { ˙v = (δ11 − γ02)v + δ01z + (δ20 − γ11)v2 + (δ10 − γ01)vz − γ10v2z
˙z = z(−γ02 − γ01z − γ11v − γ10vz) (4.5)

The singular point (0, 0) of system (4.5) is nilpotent, if δ11 = γ02 = 0. It is triple if γ11(δ20 −
γ11) ̸= 0. By a rescaling and still using the original coordinates (x, y), we obtain the system
(4.1).

By a transformation tangent to (v, z) ↦→ (−V, z) and a time rescaling, we can bring system
(4.5) into the C ∞-equivalent form




 ˙V = Z
˙Z = (B − 1)V 3 − γ(B − 1)2V 4 + O(V 5)

+Z[
(3 − 2B)V − γ(B − 1)(B2 − 2B + 4)V 2 + O(V 3)] + Z 2O(|(V, Z)|
3). (4.6)

Then η = −γ(B − 1)
2(5B2 − 4B + 11) in (2.1) does not vanish when γ ̸= 0 and B > 1. Also
b = 3 − 2B vanishes for B = 3
2.

4.2 Finite cyclicity of graphics with a nilpotent point of saddle-type inside
quadratic systems
 Figure 5: The graphic (I 1
12).

Theorem 4.2. The graphic (I 1
12) (Figure 5) has ﬁnite cyclicity inside quadratic systems.

14

Proof. The graphic (I 1
12) is an hh-type graphic with a nilpotent saddle of multiplicity 3 at inﬁnity
and an invariant parabola as shown in Fig 5.

By Theorem 3.4, to prove the ﬁnite cyclicity of (I 1
12), we only need to check that the ﬁrst
return map P of the system (4.1) along the invariant parabola (4.2) under condition (4.3) satisﬁes
γ∗ = P ′(0) ̸= 1 when γ ̸= 0. Along the invariant parabola (4.2), we have

P ′(0) = exp (∫ ∞

−∞ div dt
)

= lim
x0→∞ exp
 (∫ x0

−x0
 (1 + 2B)x + (1−B)δ
B
1
2x2 + (1−B)δ
B x + (1−2B)δ2+B
2B2 dx
)

= lim
x0→∞
 [( −B2x2
0 + 2δB(B − 1)x0 + δ2(2B − 1) − B
−B2x2
0 − 2δB(B − 1)x0 + δ2(2B − 1) − B
 )1+2B

exp
 (
4δB1/2(1 − B)(1 − Bδ2)
−1/2 arctan −Bx + (B − 1)δ
√
B(1 − Bδ2)
 ) ∣
∣
∣x0

−x0
]

= exp (
4πδB1/2(1 − B)(1 − Bδ2)
−1/2) ̸= 1,

when δ ̸= 0 and B ̸= 1. (Note that 1 − Bδ2 > 0 is the condition that the system has no singular
point on the invariant parabola.)
 Figure 6: The graphic (I 1
13).

Theorem 4.3. The graphic (I 1
13) (see Figure 6) has ﬁnite cyclicity inside quadratic systems.

Proof. This graphic is a convex graphic through a nilpotent saddle of multiplicity 3, and with a
central transition through a saddle-node. In quadratic systems, such a graphic occurs when the
nilpotent point is at inﬁnity. Then µ1 = 0 in the unfolding, because the equator is invariant. This
limits the number and complexity of the limit periodic sets to be considered. Without loss of
generality, we can suppose that the saddle-node is attracting. The proof is an easy adjustement
of that of Corollary 3.4. Indeed, by Theorem 2.7, the central transition through a saddle-node
in normal form coordinates is linear with exponentially small coefﬁcient ϵ(A) in the parameter
unfolding the saddle-node.

Because of the restriction to quadratic systems (hence µ1 = 0) we need only consider the
limit periodic sets occurring in Sxhh1-Sxhh8 of Table 2, and the connection along the invariant

15

line is always ﬁxed. The upper and intermediate graphics all have cyclicity one: indeed, the ﬁrst
return map has a derivative much smaller than one because of the passage near the saddle-node
by Theorem 2.7.

Hence, we need only consider the lower limit periodic sets. The cyclicity is one for Sxhh2c.
Indeed, the global Poincar´e return map has a derivative less than 1, since the Dulac map near
the attracting saddle-node on the blow-up sphere is ﬂat (Theorem 2.7, case 2), and hence has
a very small derivative. The same is true for Sxhh8c because the transition is ﬁxed between
the saddle and the saddle-node on the blow-up sphere. Indeed, since the stable-center transition
near the saddle-node is ﬂat, then the composition of three maps on the blow-up sphere (the
passage near the saddle (given in Theorem 2.5) with the regular transition between the saddle
and the saddle-node and the stable-center transition near the saddle-node is ﬂat.

We group the rest of the limit periodic sets into classes and give sketchy arguments, since
these are quite classical.

Sxhh1, Sxhh4, Sxhh5 and Sxhh6. The argument is similar to the ﬁnite cyclicity of a graphic
with a saddle-node with center transition and a hyperbolic saddle. The cyclicity is 1 if the
hyperbolicity ratio τ at the saddle for Sxhh1 (resp. the product τ of the hyperbolicity ratios at
the two saddle points for Sxhh4 and Sxhh6) is greater than one since the Poincar´e return map
has a derivative less than 1.

When τ ≤ 1, we consider the displacement map Lν : Σ4 −→ Σ (see Figure 7(a)), deﬁned
by Lν = R3,ν ◦ D3,ν ◦ Tν ◦ D−1
4,ν − D−1
ν ◦ R−1
4,ν. It has been shown in [4] that it is possible to
choose normalizing coordinates on Π, such that R4,ν is an afﬁne map. Hence, D−1
ν ◦ R−1
4,ν is
an afﬁne map, whose second derivative is identically zero. If τ < 1, then we directly see that
L′′
ν(˜y4) ̸= 0, since Tν(˜y4) = ϵ0 + C ˜yτ
4 + O(˜y4), with C ̸= 0. If τ = 1, which occurs for µ3 = 0,
then we can use exactly the same sections and arguments as in Theorem 3.1 since the family
rescaling is integrable in this case.

Sxhh3. The argument is similar to the ﬁnite cyclicity of a graphic with two saddle-nodes, one
with center transition (the one on the blow-up sphere) and one with center-unstable transition.
It involves using the Khovanskii method. Indeed, let Σ
′ and Π
′ be two sections in normal form
coordinates at the entrance and exit of the saddle-node on the blow-up sphere (see Figure 7(b)),
where Σ′ is parameterized by z and Π′ by w. We replace considering the displacement map
from Π
′ to Σ
′ by considering the equivalent system of two equations
{
z = Sν(w),
z = D′−1
ν (w), (4.7)

where Sν follows the ﬂow forwards:

Sν = T4,ν ◦ D−1
4,ν ◦ R4,ν ◦ Dν ◦ R3,ν ◦ D3,ν ◦ T3,ν. (4.8)

The Taylor expansion of Sν has the form Sν(w) = ϵ0(A) + ϵ1(A)w(1 + h(w, A)), where
h(w, A) = O(w) is bounded and has property (J). Also ϵ1(A) > 0, when the saddle-node
has disappeared, a necessary condition for the existence of limit cycles. Now, D−1
ν is the Dulac
map following the ﬂow backwards near the saddle-node. The function z = D−1
ν (w) is solution
of the Pfaff equation FA(w)dz − zdw = 0, where FA(w) = (w2 + η(A))(1 + C(A)w) and

16

D3D4
 34
 34
 R

 D
 T 3T 4

(a) Intermediate graphic D3D4 34
 34
 R

 D
 T 3T 4
 4 R3

D&& &

(b) Sxhh3D3D4 34
 34
 R

 D
 T 3T 4
 4 R3

D&&

&
&&
 &&
 R

D&&
 (c) Sxhh7

Figure 7: The sections for (I 1
13).

FA(w) ∂
∂w + z ∂
∂z is the normal form of the vector ﬁeld in the neighborhood of the saddle-node.
Hence, we replace the system (4.7) by the system
{
z = Sν(w),
Ω = FA(w)dz − zdw = 0, (4.9)

Between two solutions of the system (4.9), there exists on z = Sν(w) a contact point of Ω with
z = Sν(w). Hence, the number of solutions is at most one plus the number of solutions of
{
z = Sν(w),
z − S′
ν(w)FA(w) = 0, (4.10)

which yields the 1-dimensional equation VA(w) = Sν(w) − S′
ν(w)FA(w) = 0. This equation
has at most one small solution. Indeed,

V ′
A(w) = ϵ1(A) [1 + O(w) + O(η)] ̸= 0,

for small w and A sufﬁciently close to A0.

Sxhh7. We only need to adapt the argument done for Sxhh3. We consider the sections in
Figure 7(c). Since the connection between the saddle and the saddle-node is ﬁxed on the blow-
up sphere, this suggests taking for the displacement map, the map from Π′ to Σ
′′, parametrized
respectively by z and w. As before, we consider the equivalent system of two equations
{
z = Sν(w),
z = Uν(w), (4.11)

where Sν is given by (4.8) and Uν = D′′−1
ν ◦ T −1
ν ◦ D′−1
ν . Let τ (A) be the hyperbolicity ratio at
the saddle point. We have

v = Tν ◦ D′′
ν (z) = c(A)zτ (A)(1 + φ1(z, A)), (4.12)

17

where c(A) > 0 and φ1 has property (I). As before, the function v = D′−1
ν (w) is solution of the
Pfaff equation FA(w)dv −vdw = 0, where FA(w) = (w2 +η)(1+C(A)w) and FA(w) ∂
∂w +v ∂
∂v
is the normal form of the vector ﬁeld in the neighborhood of the saddle-node. Then, replacing
(4.12) in the Pfaff equation yields

τ (A)FA(w)dz − z(1 + φ2(z, A))dw = 0,

where φ2(z, A) has property (I).

The rest of the proof is as for Sxhh3.

References

[1] F. Dumortier, R. Roussarie and C. Rousseau, Hilbert’s 16th problem for quadratic vector
ﬁelds, J. Differential Equations 110 (1994), no. 1, 86–133.

[2] F. Dumortier, R. Roussarie and C. Rousseau, Elementary graphics of cyclicity 1 and 2,
Nonlinearity 7 (1994), no. 1, 1001–1043.

[3] F. Dumortier, R. Roussarie and S. Sotomayor, Generic 3-parameter families of vector
ﬁelds in the plane, unfoldings of saddle, focus and elliptic singularities with nilpotent
linear parts. Springer Lecture Notes in Mathematics 1480, 1–164 (1991).

[4] A. Guzman and C. Rousseau, Genericity conditionsfor ﬁnite cyclicity of elementary graph-
ics, J. Differential Equations 155 (1999), 44–72.

[5] A. G. Khovanskii, Fewnomials, Translations of Mathematical Mongraphs, 88, American
Mathematical Society, 1991.

[6] R. Roussarie and C. Rousseau, Finite cyclicity of some center graphics through a nilpotent
point inside quadratic systems, preprint, 2014.

[7] H. Zhu and C. Rousseau, Finite cyclicity of graphics with a nilpotent singularity of saddle
or elliptic type, J. Differential Equations 178 (2002), 325–436.

18
