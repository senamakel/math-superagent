<!-- source: https://ddd.uab.cat/pub/artpub/2012/228095/Cau2012.pdf | converted from PDF -->

Hilbert’s Sixteenth Problem
for polynomial Li´enard equations

Magdalena Caubergh

Abstract. This article reports on the survey talk ‘Hilbert’s Sixteenth Prob-
lem for Li´enard equations,’ given by the author at the Oberwolfach Mini-
Workshop ‘Algebraic and Analytic Techniques for Polynomial Vector Fields.’
It is written in a way that it is accessible to a public with heterogeneous math-
ematical background as the one at the Mini-Workshop. The article reviews
recent developments and techniques used in the study of Hilbert’s 16th prob-
lem where the main focus is put on the subclass of polynomial vector ﬁelds
derived from the Li´enard equations.

Mathematics Subject Classiﬁcation (2000). Primary 34C07; Secondary 37G15,
34C20 .
Keywords. Planar vector ﬁelds, periodic orbits, compactiﬁcation, large ampli-
tude limit cycles, Li´enard equations.

1. Introduction

Polynomial Li´enard equations are planar diﬀerential equations associated to the
second order scalar diﬀerential equations

x
′′ + f (x) x
′ + g (x)= 0, (1.1)

where the functions f and g are polynomials of degree n and m respectively. They
occur as models or at least as simpliﬁcations of models in many domains of science.
Besides singularities, which are well-understood for (1.1) , isolated periodic
orbits or so-called limit cycles represent the asymptotic state of the other solutions
of (1.1), see Figure 1, which are subject of Hilbert’s 16th Problem and Smale’s
13th Problem. A formulation of these problems and their recent developments are
recalled in section 2. There were several attempts to solve Hilbert’s 16th Problem
and so far all of them failed. However the problem yet has a source of inspiration
for signiﬁcant progress in the geometric theory of planar vector ﬁelds, as well as
bifurcation theory, normal forms, foliations and some topics in algebraic geometry.

This is a preprint of: “Hilbert’s sixteenth problem for polynomial Li´enard equations”, Magdalena
Caubergh, Qual. Theory Dyn. Syst., vol. 11, 3–18, 2012.
DOI: [10.1007/s12346-012-0068-y]

2M. Caubergh

This survey aims at collecting important developments and techniques in the
study of Hilbert’s 16th Problem where the main focus is put on the subclass of
polynomial vector ﬁelds derived from the Li´enard equations (1.1) :

˙x = y, ˙y = − g (x) − f (x) y, (1.2)

or written in the coordinates (X, Y )= (x, y + F (x)) of the Li´enard plane:

˙X = Y − F (X) , ˙Y = − g (X)where F (X)= ∫ X

0 f (u) du. (1.3)

2. Hilbert’s Sixteenth Problem

2.1. Polynomial vector ﬁelds
Hilbert’s 16th Problem essentially asks for a uniform upper bound H (n)for the
maximum number of limit cycles of a planar polynomial vector ﬁeld

X n
(a,b) – x
′ =
 n∑

j=0
 j∑

i=0 aijx
iyj−i and y′ =
 n∑

j=0
 j∑

i=0 bijx
iyj−i} where aij ,bij  R,

uniformly in terms of the degree n. This problem is more than 100 years old and its
investigation has produced many papers contributing to the wide development of
the theory of Dynamical Systems. It is not known whether a uniform upper bound
only depending on the degree of the vector ﬁeld might exist, even not when the
degree is two. This part of Hilbert’s 16th Problem is generally called the uniform
ﬁniteness problem.
Even Dulac’s theorem to prove that for individual vector ﬁelds the number of
limit cycles is ﬁnite was far from trivial (see e.g. [18]); this problem is also referred
to as the individual ﬁniteness problem. In 1923 Dulac presented a proof for this
theorem. Later it was found that the proof contained a gap. This lack was ﬁrst
solved for quadratic systems by Bamon in 1985 and for arbitrary degree by Ecalle
and Ilyashenko independently in the 1990s.
Solution programmes for Hilbert’s 16th Problem mostly consist in its reduc-
tion to several subproblems, based on either considering local cyclicity problems
[26] or restricting the class of vector ﬁelds to a particular simpler class, see e.g.
[18] for an overview.
Using diﬀerent techniques (Abelian integrals, simultaneous bifurcations from
centers,. . . ), there are some lower estimates known for the Hilbert’s numbers, for
instance: H (2)  4 [9, 29, 33], H (3)  13 [23], H (4)  22 [2], H (5)  28 [30],
H (6)  35 [31], H (7)  50 [25], H (n)  kn2 ln n [7], and

H (n)  4(n +1)
2 (1.442695 ln (n +1) − 1/6) + n − 2/3[20].

Finally note that Hilbert’s 16th problem was also considered for vector ﬁelds
on phase spaces of arbitrary dimension  3 by Bobienski and Zoladek; in [1] they
illustrate that then the uniform ﬁniteness problem has a negative answer.

Hilbert’s 16th Problem for Li´enard equations 3

γ

Figure 1. Repelling limit cycle γ.

2.2. Li´enard equations

In the following we denote by H L (m, n) the maximum number of limit cycles of
(1.1), (1.2) or (1.3). Part of the 13th Problem that Smale put forward on his list
of challenging problems for the 21st century deals with Hilbert’s 16th Problem
restricted to the classical Li´enard equations, i.e. the case g (x)= x in (1.1) , (1.2)
or (1.3) , see [28]. Moreover Smale suggests that the maximal number of limit cycles
H L(1,n) for classical Li´enard equations grows at most by an algebraic law of type
nd where d is a universal constant.
The problem for classical Li´enard equations when the degree of f is equal to
2 or 3 is solved; the result in [24] shows that H L(1, 2) = 1 (i.e. the so-called Van
der Pol Equation has at most one limit cycle, see Figure 1) and very recently Li
and Llibre proved in their preprint [22] that H L (3, 1) = 1. Besides there is the
so-called Lins, de Melo and Pugh Conjecture, stating that the maximal number of
limit cycles is equal to l if g(x)= x and the degree of f is 2l or 2l +1.
Of course there is the counter-example to that conjecture, for limit cycles in
singular perturbations, due to Dumortier, Panazzolo and Roussarie (H L (1, 6)  4
see [15] and a recent generalization H L (1,n)  [ n
2 ] +2,  n  5 in [10]), but it does
not contradict the possibility for the growth of the number of limit cycles to be
linear. In [15] classical Li´enard equations are presented with degree of f equal to 2l
and having at least l + 1 limit cycles; hence one limit cycle more than conjectured
by Lins, de Melo and Pugh.
In fact, in [24], they prove that, under these assumptions, there are at most
l small amplitude limit cycles. Lloyd and Lynch considered the similar problem
for generalized Li´enard equations [21]. In most cases, they prove an upper bound
for the number of small amplitude limit cycles, that can bifurcate out of a single
non-degenerate singularity.
Later Coppel proved in [8] that H L(2, 1) = 1. In [12, 17] it is shown that
H L(3, 1) = 1 and in [13] it is shown that H L(2, 2) = 1. Up to now, as far as we
know, only these ﬁve cases have been completely investigated. From Dumortier and
Li we know that H L (2, 3)  5 [14]; furthermore from Yang, Han and Romanovski
we know that H L (m, 3)  [ 3m+14
4 ] for 3 Σ m Σ 8, see [32].

4M. Caubergh

Recently progress has been made towards proving the ﬁniteness part of
Hilbert’s 16th Problem for classical Li´enard equations. By the results from [4, 27]
the study of the ﬁniteness part of Smale’s 13th Problem is reduced to singular
perturbation problems; more precisely the following theorem is proven.

Theorem 2.1. The global number of limit cycles of (1.1) with g (x)= x is uniformly
bounded if f is restricted to some compact set of polynomials of degree exactly n
(see [27] for n even and [4] for n odd).

In section 4 we provide with some insight in the techniques underlying The-
orem 2.1. In (2.1) we have summarized the currently known results for the Hilbert
numbers for Li´enard equations (1.2) that we mentioned here above.

H L (m, n) 1 2 3 4 5 6 n 
1 0 1 1  4  5 [4, 27],[10]
2 1 1  5
3 1
m Φ [32]
 (2.1)

3. Local and global ﬁniteness problems

Hilbert’s 16th Problem is a global ﬁniteness problem in the sense that one aims
at bounding the number of limit cycles of X n
(a,b) in the plane R2 for all possible
values of the parameter (a, b) . In this section we brieﬂy explain how this global
problem can be ‘localized’. For this purpose we ﬁrst introduce the notions of limit
periodic set and cyclicity. Limit periodic sets are subsets consisting of singularities
and regular orbits, that can produce limit cycles by perturbation, and the cyclicity
is the maximal number of limit cycles that they can generate in a perturbation.
More precisely these notions are deﬁned as:

Deﬁnition 3.1. Let P 	 Rp be the parameter space with λ
0  P and let (Xλ)λ∈P
be a family of vector ﬁelds on a regular 2-dimensional surface S. Then,
1. a compact set Γ 	 S is a limit periodic set of (Xλ)λ for λ  λ
0 if and only if
there exists a sequence (λn)n∈N in P with λn  λ
0 for n 
 and such that
for all n  N, there exists a limit cycle γn of Xλn with γn  Γfor n 
 .
2. Let Γ be a limit periodic set of (Xλ)λ for λ  λ
0. Then we say that Γ has
ﬁnite cyclicity in the unfolding (Xλ)λ for λ  λ
0 if there exist N  N and
constants ε, δ > 0 such that for every parameter value λ with ∥
∥λ − λ
0∥
∥ <δ
the vector ﬁeld Xλ has at most N limit cycles γ with dH (γ, Γ) <ε. If Γ
has ﬁnite cyclicity in (Xλ)λ for λ  λ
0, then the cyclicity of Γ inside the
unfolding (Xλ)λ for λ  λ
0 is deﬁned as the positive integer

Cycl (
Xλ, (
Γ,λ
0)) = lim
λ→λ0 sup
γ→Γ –number of limit cycles γ of Xλ} . (3.1)

The distance dH is the Hausdorﬀ distance on the metric space of compact
sets, and the limits γn  Γand γ  Γ are considered in this metric space.

Hilbert’s 16th Problem for Li´enard equations 5

A major question is the so-called local ﬁniteness problem or local cyclicity
problem that exists in ﬁnding suﬃcient conditions under which the cyclicity is
ﬁnite, and in this case, to ﬁnd an explicit estimate for the cyclicity.
Limit periodic sets are the so-called organizing centers for limit cycles. There-
fore to detect limit cycles one looks ﬁrst for all limit periodic sets, for which there
exists in case there are only isolated singularities a structure thm analogous to the
Poincar´e-Bendixson Theorem for α-and ω-limit sets (see [26]). This theorem clas-
siﬁes the possible types of limit periodic sets Γ of (Xλ)λ for λ  λ
0 as a singular
point, a periodic orbit or a graphic of Xλ0. Recall that a graphic Γ of a vector
ﬁeld Xλ0 is the union of (not necessarily distinct) singular points p0,...,pm with
pm = p0, and regular orbits γ1,... ,γm−1 of Xλ0 , connecting these singular points,
in the sense that pi = α (γi)and pi+1 = ω (γi) , 1 Σ i Σ m − 1. In section 4.3 we
encounter the so-called ‘2-saddle cycle’ which is a simple example of a graphic, see
Figure 3 (Γ = Γ1 ﬀ Γ2 ﬀ– s+, s−} ).
By compactiﬁcation of the parameter space and the phase plane of X n
(a,b),the
family of polynomial vector ﬁelds extends to a compact analytic family, such that
Hilbert’s global ﬁniteness problem is reduced to several local cyclicity problems
(see Theorem 3.2 below and [27]).

3.1. Localization method
Compactifying phase plane as well as parameter space one can apply the so-called
localization method of Roussarie ([27]) which is based on the following theorem:

Theorem 3.2. Let K be a compact set in parameter space and let S be a compact
2-dimensional manifold, let Xλ be an analytic vector Þeld on S for each λ  K.
Then there exists a uniform upper bound for the number of limit cycles of Xλ in S
for λ  K if and only if for any λ
0  K any limit periodic set Γ of Xλ0 has Þnite
cyclicity inside the family Xλ for λ  λ
0, i.e.

Cycl (
Xλ, (
Γ,λ
0)) <
 .

In section 4, to prove Theorem 2.1, we apply the localization method of
Roussarie reducing the global Smale’s problem to several local cyclicity problems:
small, medium and large amplitude limit cycles and cyclicity problems for slow-
fast systems. This localization method requires an appropriate compactiﬁcation of
the phase plane, as well as the chosen space of Li´enard equations itself (see section
4.5).

3.2. Classical tools to study local cyclicity problems
Traditionally the study of limit cycles of planar vector ﬁelds (Xλ)λ near a limit
periodic set Γ for λ  λ
0, as the ones we consider, is replaced by the study of
isolated ﬁxed points s of associated 1-dimensional Poincar´e-maps (Pλ)λ ,

Pλ (s)= s for s near s0,

where s0 corresponds to Γ. Or equivalently, by the study of isolated zeroes s of
so-called displacement maps δλ = Pλ − Id or diﬀerence maps Δλ (e.g., see section

6M. Caubergh

4.3 and Figure 3). In such a way conﬁgurations of isolated zeroes of δλ (resp. Δλ)
correspond to conﬁgurations of limit cycles of Xλ. In particular the cyclicity in
(3.1) can be expressed in terms of zeroes of Δλ (or δλ):

Cycl (
Xλ, (
Γ,λ
0)) = lim
λ→λ0 sup
s→s0 –number of isolated zeroes s of Δλ} .

To control zeroes of these maps near s0 one can rely on classical theorems
as the Implicit Function theorem, Rolle’s Theorem, the Preparation Theorem, as
long as the map Δλ0 is of ﬁnite order at s0. In the other case some degeneracies
ﬁrst have to be removed. To that end, when Γ is approached by a period annulus,
one can analyze the division of the map in terms of Melnikov functions or the
Bautin ideal (see [26]). The Bautin ideal also serves to characterize the parameter
values for which the corresponding vector ﬁeld is of center type. Moreover an
upper bound of the cyclicity can be expressed in terms of this ideal. In [3] it
is proven that this Bautin ideal corresponds to the ideal generated by Lyapunov
quantities, which determine the order and stability of a weak focus; in [6] Lyapunov
quantities are determined for classical and generalized Li´enard equations using
Cherkas transformation, and a local division of the displacement map is given
in terms of the Lyapunov quantities. Furthermore in [6] a detailed study of the
bifurcation phenomenon of small amplitude limit cycles is provided and generic
Hopf-Takens bifurcations (degenerate or not) are precisely described.

4. Classical Li´enard equations of degree n

In the Li´enard plane the classical Li´enard equation (1.3) is written as the polyno-
mial vector ﬁeld Ln
a with

Ln
a  ˙x = y − F n
a (x) , ˙y = − x where F n
a (x)=
 n−1∑

i=1 aix
i + x
n. (4.1)

Besides the compactiﬁcation process, due to the fact that the ‘central sys-
tem’ is too degenerate to permit a study of its unfolding without a blow up,
the method includes a desingularization. In this way the boundary of the space
of Li´enard equations is made by Hamiltonian and singular perturbation prob-
lems. These boundary problems both exhibit diﬀerent phenomena. In this survey
we only include the Hamiltonian perturbation problems that can completely be
solved. The study of the cyclicity problem for classical Li´enard equations of odd
degree (i.e. n is odd) that do not belong to the boundary is easy and well-known
among specialists. In this case limit cycles stay at a uniform distance from inﬁnity
(see [27]). For classical Li´enard equations of even degree (i.e. n =2l is even) this
is no longer true and then the main problem consists in studying limit cycles that
come close to inﬁnity. These limit cycles are so-called large amplitude limit cycles
of which it is shown in [4] that there are at most l + 1 (see Deﬁnition 4.1).

Hilbert’s 16th Problem for Li´enard equations 7

4.1. Bounded Li´enard equations
By ‘bounded Li´enard equations’ of degree n we refer to a family of Li´enard equa-
tions (Ln
a)a , where a belongs to a compact set K in Rn−1.
Applying the Lyapunov-Poincar´e compactiﬁcation, that is a quasi-homogenous
version of the Poincar´e compactiﬁcation, the Li´enard system Ln
a extends to an
analytic vector ﬁeld on the sphere S
2 (see [11]). In this compactiﬁcation the non-
elementary singularities at inﬁnity are spread out over the equator of S
2 being all
of elementary type.

4.2. Local cyclicity problems for bounded Li´enard equations
Since the origin is the only singularity of Ln
a in R2, that is a weak focus or center,
limit periodic sets that lie entirely in the ﬁnite plane correspond to either the
singularity in the origin or a regular periodic orbit. Limit cycles bifurcating from
these limit periodic sets are called respectively small amplitude limit cycles and
medium amplitude limit cycles. These cyclicity problems are well understood and
result in ﬁnite cyclicity, because these limit cycle bifurcations can be studied by
isolated zeroes of analytic maps (displacement maps), see e.g. [6].
Since there are no other limit periodic sets in the ﬁnite plane the only bifur-
cation phenomenon of limit cycles that remains to be studied is the one of large
amplitude limit cycles, that is deﬁned here below. Let BR (0) denote the open ball
in R2 centered at (0, 0) and with radius R> 0:

BR (0) = {
(x, y)  R2 : x
2 + y2 <R} .

Deﬁnition 4.1. We say that a family (Xλ)λ of vector ﬁelds on the plane R2 has
exactly N large amplitude limit cycles for λ  λ
0 if and only if

1. there exist R> 0, a neighbourhood W of λ
0 such that for all λ  W the
vector ﬁeld Xλ has at most N limit cycles having a non-empty intersection
with R2 “ BR (0) ;
2. for all R> 0 and for every neighbourhood W of λ
0, there exists λ  W such
that Xλ0 has N limit cycles having a non-empty intersection with R2“BR (0) .

In sections 4.3 and 4.4 the proofs will be sketched of the facts that no large
amplitude limit cycles appear for the family of Li´enard equations of odd degree,
while there appear at most l +1 for Li´enard equations of even degree n =2l.

4.3. No large amplitude limit cycles in case n is odd
For n is odd one can construct a uniform domain of attraction by considering the
Lyapunov function V (x, y)= (
x
2 + y2) /2. Since the time derivative of V is given
by ˙V (x, y)= x ˙x + y ˙y = − xF n
a (x)= − x
n+1 (1 + o (1)) ,x  +
 .

Therefore given an arbitrary compact set K 	 Rn−1 there exists RK > 0 such that
for all a  K all orbits of Ln
a enter ¯BRK (0) after some ﬁnite time, and stay there
for all later times. As a consequence there are no large amplitude limit cycles.

8M. Caubergh

Γ1 s+s− Γ1 s+s− Γ1 s+s−
 Γ2

(a)(b)(c)

Figure 2. Classical Li´enard equation L2l
a extended to the
Poincar´e-Lyapunov disc of type (1, 2l). (a) Topological behavior
at
 . (b) No connection between s+ and s− in the ﬁnite plane. (c)
Connection Γ2 between s+ and s− in the ﬁnite plane, thus giving
rise to the unbounded 2-saddle cycle Γ = Γ1 ﬀ Γ2 ﬀ– s+, s−} .

4.4. At most l +1 large amplitude limit cycles in case n is even
For n =2l even, the inﬁnity is no longer repelling and we here sketch brieﬂy how
the analysis of large amplitude limit cycles proceeds.

1. Compactiﬁcation of phase space: take local coordinates (¯x, ¯y) near inﬁnity
given by x =¯x/s, y =¯y/s2l with s> 0and ¯x
2 +¯y2 =1. After a time-rescaling
(¯t = s2l−1t) the vector ﬁeld Ln
a extends analytically to a vector ﬁeld ¯Ln
a on the
Poincar´e-Lyapunov disc of type (1, 2l) . The phase portrait near the equator
of this disc (which corresponds to
 , or s = 0) is presented in Figure 1 (a).
There are four singularities at
 : two semi-hyperbolic saddle singularities
that we denote by s± in the upper half sphere and two elementary nodes (a
repelling and an attracting one) in the lower half-sphere. The semi-hyperbolic
singularities s± are connected by a regular orbit Γ1 at
 for all a  Rn−1. If
for a0 arbitrary but ﬁxed there is no connection in the ﬁnite plane between
s+ and s−, then there will be no large amplitude limit cycles bifurcating for
a  a0, see Figure 1 (b). If there does exist a connection Γ2 in the ﬁnite plane
between s+ and s−, and thus giving rise to an unbounded 2-saddle cycle Γ,
then large amplitude limit cycles can bifurcate from Γ for a  a0, see Figure
1 (c). In the following we assume that such Γ exists for a = a0, seeFigure3.
2. Let Σi be a transversal section with respect to Γi,i =1, 2. As is convenient in
the study of limit cycles near a 2-saddle cycle we deﬁne the so-called diﬀerence
map Δ as the diﬀerence between the transitions Δ1 and Δ2 from Σ1 to Σ2,
deﬁned by the ﬂow of ¯Ln
a in forward and backward time respectively:

Δ(w, a)=Δ2 (w, a) − Δ1 (w, a) , for w  0,

where w is a local regular parameter on Σ1, such that w = 0 corresponds
to Γ1 ﬁ Σ1. In this way isolated zeroes w of Δ (· ,a)for w Φ 0,w ﬂ=0and

Hilbert’s 16th Problem for Li´enard equations 9

Γ1
 s+s−
 Γ2

Δ1

Δ2

Σ1
 Σ2
 D+D−
 Γ1
 s+s−
 Γ2

Σ
−
1
 Σ
+
2

Σ
+
1

Σ
−
2
 R1

R2

(a)(b)

Figure 3. Diﬀerence map Δ near two-saddle cycle Γ. (a) Δ =
Δ2 − Δ1;(b) Δ1 = D+ ﬃ R1 and Δ1 = R2 ﬃ D−.

a  a0 correspond to large amplitude limit cycles of Xa near Γ. Taking
appropriate sections Σ
±
i with respect to Γi near s± the transition maps Δi :
Σ−
1  Σ+
2 ,i =1, 2 are written as the composition of a regular transition Ri
along Γi and a Dulac transition D± near the saddle point s±, seeFigure3
(b).
3. To facilitate the calculations near Γ1 one can use local coordinates (u, s)in
which ¯Ln
a reads as

ˆLn
a  { ˙u =1 − u2l − G (u, s, a)+ (2l)
−1 u2s4l−2,
˙s =(2l)
−1 s4l−1u,

where
 G (u, s, a)=
 2l−1∑

i=1 aiuis2l−i.

Clearly G (u, s, a)= G (− u, − s, a) ; hence ˆLn
a is invariant with respect to the
symmetry (u, s, t)  (− u, − s, − t) , seeFigure4 (a).
4. By this symmetry we can use the same normalizing coordinates (z, w)near
the semi-hyperbolic saddle points s±, transforming ˆLn
a into the equivalent
diﬀerential system

X norm
a  { ˙z = − z,
˙w = w4l−1 (
1+ αw4l−2)−1 ,

where α = α (a) depends polynomially on a. The Dulac map from –z =1} to
–w =1} near the saddle point (0, 0) of X norm
a can be explicitly written down
as
 D (w)= wα exp ( 1 − w4l+2

4l − 2
 ) , for w  0.

By the invariance of X norm
a with respect to the symmetry (z, w, t)  (z, − w, − t)
the Dulac map from –z =1} to –w = − 1} near the saddle point (0, 0) is given

10 M. Caubergh

D+
 D−
 s+
 s− s+ s−

z –z =1} –w = − 1}

–w =1}
 D(w)

D(w)

w

− w

(a)(b)

Figure 4. Dulac transitions D± near the saddle points s± using
the symmetry (a) (u, s, t)  (− u, − s, − t)resp. (b) (z, w, t) 
(z, − w, − t), that is present in the coordinates (u, s, t)near

resp. the normalizing coordinates (z, w, t).

by D (− w) , for w Σ 0, see Figures 3 and 4. By taking the corresponding sec-
tions Σ±
i in the (u, s) plane and using these normalizing coordinates as regular
parameter one can write

Δ2 (w, a)= R2 ﬃ D (w)and Δ1 (w, a)= D ﬃ R1 (w) .

For readability, in the notation of D and Ri,i =1, 2 we left out the depen-
dence on the parameter a. Clearly Δ is C∞ at w = 0 and its jet of inﬁnite
order at w = 0 is given by j∞ (Δ)0 (w)  R2 (0) , the so-called breaking coef-
ﬁcient.If R2 (0) ﬂ=0, then there is no connection between s+ and s− in the
ﬁnite plane for the considered parameter a  Rn−1, and hence there are no
large amplitude limit cycles for parameter values suﬃciently close to a.
5. Since there is no explicit expression known for the connection Γ2 in the ﬁnite
plane, there is almost no chance to perform an asymptotic analysis of R2.
Therefore, by taking the derivative and an algebraic manipulation, we replace
the study of zeroes of Δ (· ,a) to zeroes of Δ
1 (· ,a) in such a way that zeroes
of Δ
1 (· ,a) correspond to solutions of ∂Δ
∂w (· ,a)=0. By Rolle’s Theorem
the number of zeroes w Φ 0of Δ (· ,a) is bounded by 1 plus the number of
zeroes w Φ 0of Δ
1 (· ,a) , where the zeroes are counted with multiplicity. The

Hilbert’s 16th Problem for Li´enard equations 11

principal part of the so-called reduced diﬀerence map Δ
1 can be written as:

Δ
1 (w, a)= 1
− 4l +2
 ( 1 − ¯R1 (w, a)
w
 )−4l+2 + O (
w4l−3) ,w Φ 0, (4.2)

where R1 (w, a)= w ¯R1 (w, a) .
6. After some calculations one obtains the asymptotic expansion for ¯R1 :

¯R1 (w, a)=1 + a2l−1w (C0 + o (1)) ,w Φ 0, (4.3)

for some C0 > 0. Furthermore, if a0
2l−1−2i =0,  0 Σ i Σ k − 1, then there
exists Ck > 0 such that this asymptotic expansion reads as

¯R1 (w, a)= 1 + a2l−1−2kw2k+1 (Ck + o (1)) ,w Φ 0. (4.4)

7. Division-derivation algorithm: Assume that a0
2l−1−2i =0,  0 Σ i Σ k − 1for
0 Σ k Σ l − 1. Then combining (4.2) , (4.3) and (4.4) we obtain the map Δ
k+1

from Δ
1 after k derivations and divisions by non-zero functions for w> 0
with
 Δ
k+1 (
w, a0) = − a0
2l−1−2kCk + o (1) ,w Φ 0.

(a) If Ln
a0 has no center at (0, 0) , then there exists 0 Σ k Σ l − 1 such that
a0
2l−1−2i =0,  0 Σ i Σ k − 1and a0
2l−1−2k ﬂ=0. Then by continuity
Δ
k+1 has no zeroes bifurcating from w =0 for a suﬃciently close to a0.
By Rolle’s Theorem it then follows that there are at most k + 1 large
amplitude limit cycles for a  a0.
(b) If all a0
2l−1−2k =0, 1 Σ k Σ l, then j∞ (
Δ
1 (
· ,a0))

0 (w)  0. However
Δ
1 is not analytic at w =0, and therefore this fact does not imply
automatically that Δ
1 (
· ,a0)  0. However if all a0
2l−1−2k =0, 1 Σ k Σ l
then Ln
a0 satisﬁes a symmetry property implying that Ln
a0 has a center
at (0, 0) , and hence Δ
1 (
· ,a0)  0. Applying Taylor’s Theorem Δ
1 can
locally be written as:

Δ
1 (w, a)=
 l∑

k=1 a2l−2k−1Φk (w, a) ,

for C∞ functions Φk, 1 Σ k Σ l with

Φk (w, a)= Ckw2k (1 + o (1)) ,w Φ 0.

By the following rescaling of the parameter we can reduce this degen-
erate case to the regular case:

(b, ρ)=(b1,...,b2l−1,ρ)  a, where  1 Σ i Σ l :

a2i = b2i,a2i−1 = ρb2i−1 and
 l∑

i=1 b2
2i−1 =1.

12 M. Caubergh

In terms of the rescaled parameter (b, ρ)=(b1,... ,b2l−1,ρ)we then
have
 Δ
1 (w, a)= ρ
 l∑

k=1 b2l−2k−1Φk (w, a)= ρ ¯Δ
1 (w, b, ρ) .

For each b  Rn−1 ﬁxed with ∑l
i=1 b2
2i−1 =1, we can apply the division-
derivation algorithm to ¯Δ
1 and ﬁnd that there are at most l + 1 large
amplitude limit cycles that bifurcate from Γ for a  a0.

4.5. Putting a boundary on the space of Li´enard equations
Following the idea of Roussarie in [27] we put a boundary on the Li´enard family
(Ln
a )a∈R n−1 to end up with a compact family. More precisely we imbed (Ln
a )a∈R n−1
in the family (
Sn
a,ε) that is deﬁned as

Sn
a,ε  ˙x = y − F n
a (x) , ˙y = − εx for ε> 0.

Clearly Ln
a  Sn
a,1. Furthermore Sn
a,0 is a singular family of planar vector ﬁelds,
having the graph of y = F n
a (x) full of non-isolated singularities; the vector ﬁelds
of the family Sn
a,ε for ε> 0 small are called slow-fast Li´enard equations.
For later use let us introduce the natural projections on Rn= Rn−1× R by
π1 : Rn−1 × R  Rn−1 :(a, ε)  a and π2 : Rn−1 × R  R :(a, ε)  ε.
The family (
Sn
a,ε)

a∈R n−1,ε>0 is quasi-homogeneous; as a consequence for all
(a, ε)and (¯x, ¯y) ﬁxed, there exist 1-parameter groups of diﬀeomorphisms

–Tτ (¯x, ¯y): τ  R} and –Uτ (a, ε): τ  R}

such that Sn
Uτ (a,ε) is conjugate to τ n−1Sn
a,ε via Tτ , where

Tτ (¯x, ¯y)= (τ ¯x, τ n ¯y) and (4.5)

Uτ (a, ε)= (
τ n−1a1,τ n−2a2,...,τ an−1,τ 2n−2ε) for a =(a1,...,an−1) . (4.6)

The phase portraits of Sn
Uτ (b,δ) and Sn
b,δ thus are diﬀeomorphic via Tτ , and so
Sn
Uτ (b,δ) and Sn
b,δ have the same number of limit cycles in the plane.
Let · be the Euclidean norm on Rn−1, and deﬁne the unit disc and its
boundary respectively by

Δ  {a  Rn−1 :  aΣ 1} and ∂Δ  {
a  Rn−1 :  a =1} .

Then for any ε> 0 the family (
Sn
a,ε)

a∈Δ is equivalent to the bounded Li´enard
family (Ln
b )b∈Kε via τ (ε) , where

Kε  {
π1 (
Uτ (ε) (a, ε)
) :  aΣ 1} and τ (ε)  2n+2√
1/ε for ε> 0. (4.7)

In particular one has π2 (
Uτ (ε) (a, ε)
) = 1 and for ε Φ 0 the diameter of Kε tends to

 , see Figure 5. Indeed notice that the 1-parameter groups of smooth diﬀeomor-
phisms –Uτ (a, ε) ,τ > 0} for ﬁxed values (a, ε) can be deﬁned by the diﬀerential

Hilbert’s 16th Problem for Li´enard equations 13

0

a
0
 a(log τ (ε),a
0)

Rn−1 “ Kε
 ∂Δ∂Kε

Figure 5. Bounded versus unbounded Li´enard equations Ln
a .
Here a(· ,a0) denotes the ﬂow deﬁned by (4.8) with initial con-
dition a = a0; the time log(τ (ε)) is necessary to pass from ε
to 1. Since (4.8) describes a linear expansion the compact set
Kε  Rn−1 for ε Φ 0, see (4.7).

equations

d
dlog τ ai =(n − i) , for all 1 Σ i Σ n − 1and d
dlog τ ε =(2n − 2) (4.8)

in parameter space Rn. Furthermore the orbits of (4.6) are transverse to the hy-
perspace –ε =1} ; therefore and since the equations for the parameter variable
a  Rn−1 are independent from the one for ε> 0, we can study the evolution
of the disc Δ and its boundary ∂Δ in the projected space Rn−1 by π1 after time
log τ (ε) , which is strictly increasing to +
 when ε Φ 0(see Figure 5).
Therefore for any ﬁxed ε0 > 0 the family (
Sn
a,ε0 )

a∈Δ is equivalent to a
‘bounded Li´enard family’ (Ln
b )b∈Kε0 and the family (
Sn
a,ε)

a∈∂Δ,0≤ε<ε0 is equivalent
to its complement in the space of Li´enard equations (Ln
b )b∈R n−1 , i.e. (Ln
b )b∈R n−1\Kε0 ,
which is unbounded (see Figures 5 and 6).
It follows from the results in sections 4.3 and 4.4 that for any ﬁxed ε0 > 0
there exists an integer N (n, ε0) such that the number of limit cycles of the bounded
Li´enard family (Ln
b )b∈Kε0 is uniformly bounded by N (n, ε0) in the plane. Therefore
to complete Smale’s 13th Problem it suﬃces to solve the ﬁniteness problem for the
compact family of polynomial vector ﬁelds (
Sn
a,ε)

a∈∂Δ,0≤ε≤ε0 , where ε0 > 0can
be taken as small as necessary. Notice that for ε0 Φ 0 limit cycles of Sn
a,ε shrink
to the origin. As a consequence, using the compactness of ∂Δ and the localization
method of Roussarie, Smale’s 13th Problem is reduced to a singular ε-perturbation

14 M. Caubergh

–ε =0}
 –ε =1}

–ε = ε0}
 Kε1

R+ × Rn−1
 ε

Kε0

Δ

Figure 6. Compactiﬁcation of classical Li´enard equations –Ln
b :
b  Rn−1} . The constants εi > 0,i =0, 1 are assumed to be
ordered as ε0 <ε1. The bounded Li´enard family –Ln
b : b  Kε0}
is equivalent to –Sn
a,ε0 : a  Δ} and the unbounded Li´enard family
–Ln
b : b  Rn−1 “Kε0} is equivalent to –Sn
a,ε : a  ∂Δ, 0 Σ ε< ε0} .

problem: the cyclicity problem of the singular point (0, 0) of the singular vector
ﬁeld Sn
a0,0 inside the family (Sn
a0,ε)0≤ε≤ε0 for all a0  ∂Δ, where ε0 is suﬃciently
small (but independent of a0).

4.6. Conclusions and some generalizations
In sections 4.1,4.2,. . . ,4.5 we have sketched the proof of Theorem 2.1, i.e., how
Hilbert’s 16th Problem is solved for bounded classical Li´enard equations, and how
Smale’s 13th Problem is reduced to some cyclicity problems for slow-fast systems.
Besides this proof includes an independent proof of the Dulac Theorem for classical
Li´enard equations.
In [19] the Hilbert number for the bounded family of classical Li´enard equa-
tions of even degree n in case the origin is a focus, say H ∗
BL (1,n) , is estimated in
terms of diﬀerent parameters using the Growth-and-Zeroes Theorem provided by
Ilyashenko and Yakovenko and the result on large amplitude limit cycles from [4].
For a complete study of large amplitude limit cycles for the family of gen-
eralized Li´enard equations, i.e., (1.2) when g (x) ﬂ= x, the characterization of an
unbounded center is needed; this is detailed in [5] where complete results only are
obtained for certain subfamilies of generalized Li´enard equations.

Acknowledgment
The author would like to thank the organizers A. Gasull, J. Hartmann, J. Llibre
and S. Walcher for this invitation at the Oberwolfach Mini-Workshop where they

Hilbert’s 16th Problem for Li´enard equations 15

brought together a lot of interesting talks both on qualitative study of polyno-
mial vector ﬁelds as well as on algebraic and analytic geometry leaving time for
stimulating discussions on interesting and important open problems.

References

[1] M. Bobienski and H. Zoladek, A Counterexample to a multidimensional version of
the Weakened Hilbert’s 16th Problem. Moskow Mathematical Journal 7 (2007), 1–20.

[2] C.J. Christopher, Estimating Limit Cycles Bifurcations from Centers. in: Trends in
Mathematics: Diﬀerential Equations with Symbolic Computation, Birkh¨auser Verlag
Basel/Switzerland, pp.23–35, 2006.

[3] M. Caubergh and F. Dumortier, Hopf-Taken bifurcations and centres. Journal of Dif-
ferential Equations 202 (2004), 1–31.

[4] M. Caubergh and F. Dumortier, Hilbert’s 16th problem for classical Li´enard equations
of even degree. Journal of Diﬀerential Equations 244 (2008), 1359–1395.

[5] M. Caubergh, F. Dumortier and S. Luca, Cyclicity of unbounded semi-hyperbolic 2-
saddle cycles in polynomial Li´enard systems. Discrete and Continuous Dynamical
Systems 27 (2010), 963–980.

[6] M. Caubergh and J.P. Fran¸coise, Generalized Li´enard equations, cyclicity and Hopf-
Takens bifurcations. Qualitative Theory of Dynamical Systems 5(2004), 195–222.

[7] C.J. Christopher and N.G. Lloyd, Polynomial Systems: A Lower Bound for the Hilbert
Numbers. Proceedings: Mathematical and Physical Sciences 450 (1995), 219–224.

[8]W. A.Coppel, Some Quadratic Systems with at Most One Limit Cycle. Dynamics
Reported 2 (1988), Wiley, New York, 61–68.

[9] L. Chen and M. Wang, Relative position and number of limit cycles of a quadratic
diﬀerential system. (Chinese), Acta Mathematica Sinica 22(1979), 751–758.

[10] P. De Maesschalck and F. Dumortier, Classical Li´enard equations of degree n ≥ 6
can have [(n − 1) /2]+2 limit cycles. Journal of Diﬀerential Equations 250, 2162–2176.

[11] F. Dumortier and C. Herssens, Polynomial Li´enard Equations near Inﬁnity. Journal
of Diﬀerential Equations 153 (1999), 1–29.

[12] F. Dumortier and C. Li, On the uniqueness of limit cycles surrounding one or more
singularities for Li´enard equations. Nonlinearity 9 (1996), 1489–1500.

[13] F. Dumortier and C. Li, Quadratic Li´enard Equations with Quadratic Damping.
Journal of Diﬀerential Equations 139 (1997), 41–59.

[14] F. Dumortier and C. Li, Perturbation from an elliptic Hamiltonian of degree four:
(IV) Figure eight-loop. Journal of Diﬀerential Equations 188 (2003), 512–554.

[15] F. Dumortier, D. Panazzolo and R. Roussarie, More limit cycles than expected in
Li´enard equations. Proceedings of the American Mathematical Society 135 (2007),
1895–1904.

[16] F. Dumortier and R. Roussarie, Birth of canard cycles. Discrete and Continuous
Dynamical Systems S2 (2009) 723–781.

[17] F. Dumortier and C. Rousseau, Cubic Li´enard equations with linear damping. Non-
linearity 3 (1990), 1015–1039.

16 M. Caubergh

[18] Yu. S. Ilyashenko, Centennial history of Hilbert’s 16th Problem. Bulletin of the Amer-
ican Mathematical Society (N.S.) 39 (2002), 301–354.
[19] G. Kolutsky, An upper estimate for the number of limit cycles of even-degree Li´enard
equations in the focus case. Journal of Dynamical and Control Systems 17 (2011),
231–241.
[20] J. Li, H.S.Y. Chan and K.W. Chung, Some Lower Bounds for H(n) in Hilbert’s 16th
Problem. Qualitative Theory of Diﬀerential Equations 3 (2003), 345–360.
[21] N.G. Lloyd and S. Lynch, Small-amplitude limit cycles of certain Li´enard systems.
Proceedings of the Royal Society London A, 418 (1988), 199–208.
[22] C. Li and J. Llibre, Uniqueness of Limit Cycle for Li´enard Equations of Degree Four.
Preprint, 2011.
[23] C. Li, C. Liu and J. Yang, A cubic system with thirteen limit cycles. Journal of
Diﬀerential Equations 246 (2009), 3609-3619.
[24] A. Lins, W. de Melo and C.C. Pugh, On Li´enard’s equation. Lecture Notes in Math-
ematics 597 (1977), 335–357, Springer, Berlin.
[25] J. Li, M. Zhang and S. Li, Bifurcations of limit cycles in a Z2-equivariant planar
polynimial vector ﬁeld of degree 7. International Journal of Bifurcation and Chaos 16
(2006), 925–943.
[26] R. Roussarie, Bifurcations of Planar Vector Fields and Hilbert’s Sixteenth Problem.
Progress in Mathematics 164, Birkhauser-Verlag, Basel, 1998.
[27] R. Roussarie, Putting a boundary to the space of Li´enard Equations. Discrete and
Continuous Dynamical Systems 17 (2007), 441–448.
[28] S. Smale, Mathematical Problems for the Next Century. Mathematical Intelligencer
20 (1998), 7–15.
[29] Shi Songling, A concrete example of the existence of four limit cycles for plane qua-
dratic systems. Scientia Sinica 23 (1980), 154–158.
[30] Y. Wu, Y. Gao and M. Han, On the number and distributions of limit cycles in a
quintic planar vector ﬁeld. International Journal of Bifurcation and Chaos in Applied
Sciences and Engineering, 18 (2008), 1939–1955.
[31] S. Wang and P. Yu, Bifurcation of limit cycles in a quintic Hamiltonian system under
a sixth-order perturbation. Chaos, Solitons and Fractals 26(5) (2005), 1317–1335.
[32] J. Yang, M. Han and V.G. Romanovski, Limit cycle bifurcations of some Li´enard
systems. Journal of Mathematical Analysis and Applications, 336 (2010), 242–255.
[33] Zhang Zhi-fen, Ding Tong-ren, Huang Wen-zoa, Dong Zhen-xi. Qualitative Theory
of Diﬀerential Equations. American Mathematical Society, Providence, 1992.

Magdalena Caubergh
Departament de Matem`atiques
Facultat de Ci`encies(Ediﬁci C)
Universitat Aut`onoma de Barcelona
Campus Bellaterra
09381 Cerdanyola del Vall`es (Barcelona)
Spain
e-mail: leen@mat.uab.cat
