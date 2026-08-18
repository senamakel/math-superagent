<!-- source: https://www.mathnet.ru/php/getFT.phtml?jrnid=im&paperid=8352&what=fullteng&option_lang=eng | converted from PDF -->

Izvestiya: Mathematics 80:1 50–112 Izvestiya RAN : Ser. Mat. 80:1 55–118

DOI 10.1070/IM8352

Finiteness theorems for limit cycles:
a digest of the revised proof

Yu. S. Ilyashenko

Abstract. This is the ﬁrst paper in a series of two presenting a digest of
the proof of the ﬁniteness theorem for limit cycles of a planar polynomial
vector ﬁeld. At the same time we sketch the proof of the following two
theorems: an analogous result for analytic vector ﬁelds, and a description
of the asymptotics of the monodromy transformation for polycycles of such
ﬁelds.

Keywords: limit cycles, elementary polycycles, functional cochains, super-
exact asymptotic series.
 To the memory of Andrey Bolibruch,
an outstanding mathematician and a dear friend

Introduction: from diﬀerential equations to complex analysis

0.1. Finiteness theorems. The goal of this paper is to provide a survey of a sim-
pliﬁed and corrected proof of the following theorem.

Theorem 0.1. Any planar polynomial vector ﬁeld has only a ﬁnite number of limit
cycles.

The ﬁrst proof was given in [1]. An independent proof was obtained simultane-
ously by Ecalle [2].
This theorem is a particular case of a much stronger result.

Theorem 0.2. An analytic vector ﬁeld on a closed two-dimensional surface has
only ﬁnitely many limit cycles.

0.2. Non-accumulation theorems. Both of these theorems are corollaries of
the following result.

Theorem 0.3 (non-accumulation theorem). An elementary polycycle of an ana-
lytic vector ﬁeld on a two-dimensional surface has a neighbourhood free of limit
cycles.

The author was supported in part by the RFBR (grant no. 13-01-00969).
AMS 2010 Mathematics Subject Classiﬁcation. 37F75.

c⃝ 2016 Russian Academy of Sciences (DoM), London Mathematical Society, Turpion Ltd.

Finiteness theorems for limit cycles 51

We recall that a polycycle of a vector ﬁeld is a separatrix polygon with a ﬁnite
number of vertices, which are singular points of the vector ﬁeld, and a ﬁnite num-
ber of edges. The latter requirement holds automatically for analytic vector ﬁelds.
A polycycle is said to be elementary if all its singular points are elementary, that is,
the linearization of the vector ﬁeld at each of them has at least one non-zero eigen-
value. The ﬁniteness theorem follows from the non-accumulation theorem for an
arbitrary (not necessarily elementary) polycycle. The case of general polycycles
reduces to the case of elementary polycycles by the desingularization theorem for
singular points of planar analytic vector ﬁelds.
The monodromy transformation of a polycycle is deﬁned in the same way as
for an ordinary cycle, except that we use a half-open interval instead of an open
interval. It is convenient to regard monodromy transformations as germs of map-
pings (R+, 0) → (R+, 0).

Theorem 0.4 (identity theorem). Suppose that the monodromy transformation of
an elementary polycycle of an analytic vector ﬁeld on a two-dimensional surface
has countably many ﬁxed points. Then it is the identity.

In our terminology, countable sets do not include ﬁnite ones. The identity theo-
rem yields all previous theorems. It is this theorem that will be proved schematically
in what follows.

0.3. Asymptotics of the monodromy transformation. Our main result is
not exhausted by the purely negative assertion that limit cycles of an analytic vec-
tor ﬁeld never accumulate to a polycycle. It also contains positive information:
a description of the leading term of the correction (the diﬀerence from the iden-
tity) of the monodromy transformation for a polycycle of a planar analytic vector
ﬁeld. A robust form of this result is as follows. Let x ∈ (R+, 0) be the ‘natural’
chart on a half-transversal, and let ξ ∈ (R+, ∞) = − ln x be the ‘logarithmic’ chart
on (R+, ∞). We write [n] for the iterated power:

f [n] = f ◦ · · · ◦ f
︸ ︷︷ ︸
n times
 .

The symbol ≺ means ‘< in some neighbourhood of inﬁnity’.

Theorem 0.5 (asymptotics theorem). Consider a polycycle of a planar analytic
vector ﬁeld whose monodromy transformation ∆ diﬀers from the identity. Then
there are positive numbers µ < ν and a non-negative integer n such that in the
logarithmic chart

exp(− exp
[n] νξ) ≺ |∆(ξ) − ξ| ≺ exp(− exp
[n] µξ). (1)

Moreover, for all positive µ < ν and any non-negative integer n there is a polycycle
of an analytic vector ﬁeld whose monodromy transformation satisﬁes the inequali-
ties (1).

The second part of this theorem is rather simple. It is proved in § 1.1. The
identity theorem follows easily from the ﬁrst part, which is itself a corollary of the

52 Yu. S. Ilyashenko

additive decomposition theorem stated below and is proved schematically in § 1.8.4
modulo some auxiliary results.
If a monodromy transformation written in the logarithmic chart satisﬁes the
inequalities (1) with n > 0, then it has a ﬂat correction in the natural chart.
In the analytic case this correction may decrease as an arbitrarily high tower of
exponentials. The question is, whether this is possible in the polynomial case.

Problem 0.1. Can the monodromy transformation of a polycycle of a polynomial
vector ﬁeld have a non-zero ﬂat correction ?

The expected answer is ‘no’, but it is not at all clear how this might be proved.

0.4. Reduction to elementary polycycles. It was mentioned above that
the Bendixon–Seidenberg–Lefschetz–Dumortier desingularization theorem [3]–[5]
enables one to reduce the identity theorem for arbitrary polycycles to that for ele-
mentary ones. An elementary polycycle that admits a monodromy transformation
may have singular points of only two types: saddles and saddlenodes. The mon-
odromy transformation of such a polycycle is a composite of the so-called Dulac
maps (or correspondence maps) associated with these singular points. We recall
that the correspondence map for a hyperbolic sector of a saddle or a saddlenode
maps a cross-section to an incoming separatrix into a cross-section to an outgoing
separatrix along the orbits of the vector ﬁeld.
A smooth description of these maps was obtained by Dulac in his famous mem-
oir [6] of 1923. An analytic description was given only in the early 1980s. It is
presented in § 0.5 and § 0.6.

0.5. Correspondence maps for hyperbolic saddles and monodromy trans-
formations for hyperbolic polycycles. In this section we summarize the results
of [7].

0.5.1. Almost-regular germs. In the hyperbolic case, the correspondence maps
written in the logarithmic chart extend to special domains, which are similar to
half-planes and are called quadratic standard domains.

Deﬁnition 0.1. A quadratic standard domain is any domain of the form

ΩC = ϕC(C+ \ K), ϕC(ζ) = ζ + C(ζ + 1)
1/2, C > 0, K = {|ζ| ⩽ R}.

Here C+ is the right half-plane ξ ⩾ 0, where ζ = ξ + iη.

Deﬁnition 0.2. A Dulac exponential series is a formal series of the form

Σ = ν0ζ + c + ∑ Pj(ζ) exp νjζ,

where ν0 > 0, 0 > νj ↘ −∞, and the functions Pj are real polynomials. The
arrow ↘ means monotonically decreasing convergence.

Deﬁnition 0.3. A holomorphic map of a quadratic standard domain Ω in C is said
to be almost regular if it is real on R+ and can be expanded into an asymptotic real
Dulac exponential series in Ω. This expandability means that for every ν > 0 there
is a partial sum which approximates the map within the accuracy o(exp(−νξ)) in Ω.
The class of all almost regular germs at inﬁnity is denoted by R.

Finiteness theorems for limit cycles 53

Theorem 0.6. The correspondence map of a hyperbolic saddle, written in the log-
arithmic chart, extends to an almost-regular map of some quadratic domain.

0.5.2. The Phragm´en–Lindel¨of theorem for almost-regular germs. Almost-regular
germs cannot be analytically extended to a full neighbourhood of inﬁnity. Yet they
are completely determined by their asymptotic series at inﬁnity.

Theorem 0.7 (Phragm´en–Lindel¨of theorem for almost-regular germs). An almost-
regular germ that decreases on (R+, ∞) faster than any exponential is identically
zero.

It follows that two almost-regular germs with the same asymptotic Dulac series
coincide. Indeed, their diﬀerence decreases on (R+, ∞) faster than any exponential.

0.5.3. The identity theorem for hyperbolic polycycles.

Theorem 0.8. If the monodromy transformation of a hyperbolic polycycle has an
inﬁnite set of ﬁxed points, then it is the identity.

Proof. The monodromy transformation is a composite of almost regular germs. It
is easy to deduce from the deﬁnition that such a composite is also almost regular.
Suppose that it has a non-trivial Dulac series, that is, a series diﬀerent from the
identity. The terms of this series do not oscillate and have diﬀerent rates of decay.
Hence the corresponding germ has no ﬁxed points near inﬁnity.
Suppose now that the Dulac series of the monodromy transformation is equal
to the identity. Then the monodromy transformation is also the identity since it is
uniquely determined by its Dulac series. □

The proof of the general identity theorem follows the same lines. We establish
that the monodromy transformation has the properties of regularity and expandabil-
ity. Expandability means the existence of a so-called superexact asymptotic series
for the monodromy transformation. This series has non-oscillating terms. If it is
diﬀerent from the identity, then the monodromy transformation has no ﬁxed points
near inﬁnity. If it is equal to the identity, then the monodromy transformation is
also equal to the identity by the regularity property.
This description is only approximate. A precise description requires more details.
But this approximate description gives the main idea of the proof to follow. Theo-
rem 0.5 shows that a precise description of the monodromy transformation cannot
be so simple.

0.6. Correspondence maps for saddlenodes.

0.6.1. Formal normal forms for saddlenodes and their correspondence maps. The
germ of a holomorphic vector ﬁeld at an isolated degenerate elementary singular
point is formally orbitally equivalent to the germ

˙z = zk+1(1 + azk)
−1, ˙w = −w. (2)

Here k + 1 is the multiplicity of the singular point, and a is a constant which
is real if the original germ is real. For a formal normal form, the manifold z = 0 is
contracting (in other words, stable) and the manifold w = 0 is the centre manifold.
The correspondence map of an arbitrary semitransversal to the ﬁrst manifold onto

54 Yu. S. Ilyashenko

a semitransversal to the second (brieﬂy, the map TO the centre manifold) is denoted
by ∆st. It may easily be calculated:

∆st = C exp
(− 1
hk,a(z)
 ), where hk,a(z) = kzk

1 − akzk ln z , C = exp 1
k .

Factors of this form introduce exponentially small terms into the asymptotic
expression for the monodromy transformation.

0.6.2. Parabolic germs and normalizing cochains. The complexiﬁed germ of a real
holomorphic vector ﬁeld at an isolated degenerate elementary singular point always
has a one-dimensional holomorphic invariant manifold which is contracting after
a suitable time change. As a rule, such a germ has no holomorphic centre manifolds.
Corresponding to a contracting manifold is a monodromy transformation that has
the following form after a suitable scale change with a positive factor:

f : z ↦→ z − 2πizk+1 + · · · . (3)

This transformation is a so-called parabolic germ (a germ with linear part the iden-
tity in the natural chart). It is formally equivalent to a shift along the trajectories
of the vector ﬁeld v(z) = zk+1/(1 + azk) for the time (−2πi). Here k and a are the
same as in the formal orbital normal form of the germ. The corresponding normal-
izing formal series diverge as a rule, but they are asymptotic series for the so-called
normalizing cochains, whose deﬁnition will now be given. Before doing this, we note
that we are dealing with functional cochains and their germs. Functional cochains
in domains are objects occurring at the very ﬁrst steps of the construction of ˇCech
cohomology. Namely, they appear when a partition of the domain is given. The
cochain itself is a tuple of holomorphic functions (called components of the cochain)
that correspond bijectively to the domains of the partition in such a way that each
function is holomorphic in the corresponding domain. The germ of a functional
cochain at a point is the tuple of germs of its components at this point (which is
usually a boundary point for all domains of the partition). Further requirements
on the domain and the partition will be speciﬁed in each particular case.
The nice k-partition of a punctured disc centred at zero is deﬁned as the partition
of the disc into 2k equal sectors (with vertex at zero) one of which has a boundary
ray on the real axis.

Theorem 0.9 (on sectorial normalization [8], [9]). For an arbitrary parabolic
germ (3) (not necessarily a monodromy transformation ) one can ﬁnd a disc D
centred at zero and a tuple of holomorphic functions (called a normalizing cochain )
with the following properties.
1. The functions in the tuple are in one-to-one correspondence with the sectors
of the nice k-partition of the punctured disc D. Each function is deﬁned in the
corresponding sector.
2. Each function in the tuple extends biholomorphically to a sector Sj with the
same bisector and a large angle α ∈ (π/k, 2π/k). The radius of this sector depends
on α.
3. All functions in the tuple have a common asymptotic Taylor series at zero
with linear part the identity.

Finiteness theorems for limit cycles 55

4. On the intersections of the corresponding sectors, the functions in the tuple
diﬀer by o(exp(−c/zk)) for some c > 0.
5. Each function in the tuple conjugates the germ (3) in the sector Sj with the
shift along the trajectories of the vector ﬁeld v(z) for the time −2πi.
There is a unique normalizing cochain whose correction decreases more rapidly
than the correction of the germ (3), that is, a cochain of the form id + o(zk+1).

We recall that the correction of a function (or a cochain) is the diﬀerence between
this function (cochain) and the identity.

Deﬁnition 0.4. The set of all normalizing cochains described in the preceding
theorem and in its supplement below is denoted by N C (normalizing cochains).
The set of maps in the tuple that correspond to the sector adjacent from above
(resp. below) to (R+, 0) is denoted by N C u (u = upper) (resp. N C l (l = lower)).

Deﬁnition 0.5. The additive coboundary of a normalizing cochain is the set of
diﬀerences between its components deﬁned on the germs (at zero) of narrow sectors
containing the rays of the nice partition, where the minuend corresponds to the
domain on the left of the ray. The composition coboundary of a normalizing cochain
is the set of composition quotients between its components deﬁned on the same
sectors, in which the numerator corresponds to the domain on the left of the ray.
In what follows the coboundary (without an adjective) is understood as the additive
one.

The next result is also known: it is contained ‘between the lines’ in [8] and [9].
To state it, we introduce the following notation:

Π = {
ξ ⩾ a, |η| ⩽ π
2
 }
, Π
(ε)
∗ = Φ1−εΠ, Π
(0)
∗ = Π∗, (4)

Φ1−ε = ζ + (1 − ε)ζ −2, ε ∈ [0, 1)

(see Fig. 1). The domains Π(ε)
∗ are ordered by inclusion: Π(ε)
∗ ⊂ Π
(ε
′)
∗ when ε < ε
′.
The domain Π
(ε)
∗ is called the generalized ε-neighbourhood of the curvilinear half-
strip Π∗.
 Figure 1

56 Yu. S. Ilyashenko

Theorem 0.10. Every function in the tuple forming a normalizing cochain extends
holomorphically to a domain larger than the sector Sj . For the sector Su (resp. Sl)
adjacent from above (resp. below ) to the positive semi-axis in the nice k-partition,
this domain is of the form k−1Π
(ε)
∗ in the logarithmic chart ζ = − ln z.
The asymptotic Taylor series expansion for N C u can be extended to the same
domain. The same holds for Sl and N C l.

An analogous result holds for the remaining functions in the tuple. The map
corresponding to Su (resp. Sl) in the normalizing cochain is denoted by F u
norm
(resp. F l
norm).
The following notation will always be used in the logarithmic chart:

ζ = − ln z, ξ = Re ζ, x = Re z, ξ = − ln x, ζ = ξ + iη.

Now everything is ready for a description of the correspondence maps for saddle-
nodes.

0.6.3. Correspondence maps. We recall that the correspondence maps are deﬁned
in the ﬁrst paragraph of § 0.4.

Theorem 0.11 ([10], [11]). The correspondence map ∆ : (R+, 0) → (R+, 0) TO
a centre manifold of a degenerate elementary singular point of a real-analytic vector
ﬁeld is the restriction to (R+, 0) of either of the two composite maps

∆ = gu ◦ ∆st ◦ F u
norm = gl ◦ ∆st ◦ F l
norm,

where Fnorm is the normalizing map-cochain (see the theorem on sectorial normal-
ization ) for the corresponding monodromy transformation, F u
norm (resp. F l
norm) is
the map in the tuple Fnorm which is deﬁned on the sector Su (resp. Sl) adjacent
to the ray (R+, 0) from above (resp. below ), ∆st is the map deﬁned at the beginning
of this section, and the germs gu, gl are holomorphic at their ﬁxed point zero. The
multipliers (gu(0))
′ and (gl(0))
′ are positive.

Remark 0.1. It is important that the maps F u
norm, F l
norm mentioned in this theo-
rem, when written in the logarithmic chart, can be extended as described in The-
orem 0.10.

By deﬁnition, the maps described in Theorem 0.11 form the class TO. The inverse
maps form the class FROM.

0.7. Structure theorems for the monodromy transformations.

0.7.1. A preliminary structure theorem.

Theorem 0.12. The monodromy transformation of a polycycle is a ﬁnite compo-
sition of almost-regular maps and maps in the classes TO and FROM.

This composition is called a Dulac composition for the monodromy transforma-
tion. The identity theorem will be proved below for such compositions.

0.7.2. The composition characteristic.

Deﬁnition 0.6. An elementary polycycle is said to be balanced if the number of
maps FROM the centre manifold in its Dulac decomposition is equal to the number
of maps TO the centre manifold. Otherwise the cycle is said to be unbalanced.

Finiteness theorems for limit cycles 57

A useful tool for describing a Dulac composition

∆ = ∆N ◦ · · · ◦ ∆1 (5)

consisting of N factors is a function χ, which is called the characteristic function of
this composition and is deﬁned on [−N, 0] as follows. The function χ is continuous
and linear on every closed interval between two adjacent integers, and χ(0) = 0. If
the map ∆j in the composition corresponds to a hyperbolic singular point, then we
put χ(−j) = χ(−j + 1) and say that the map ∆j is located at the level l = χ(−j)
in the composition (5).
If ∆j is a map FROM the centre manifold, then

χ(−j) = χ(−j + 1) + 1.

If ∆j is a map TO the centre manifold, then

χ(−j) = χ(−j + 1) − 1.

In these cases we say that the map ∆j is located between the levels l = χ(−j) and
l − 1 = χ(−j) − 1 (resp. between the levels l = χ(−j) and l + 1 = χ(−j) + 1) in the
composition (5).
Clearly, a polycycle γ is balanced if and only if χ(0) = χ(−N ) = 0. The
characteristic of a balanced polycycle is uniquely determined up to an additive
constant and a ‘cyclic shift of the argument’, j → j + k (mod N ), both of which
depend on the choice of the semitransversal.

Example 0.1. Consider a composition (5) with N = 7, where

∆1, ∆3, ∆5 ∈ R, ∆2, ∆4 ∈ TO, ∆6, ∆7 ∈ FROM .

Then ∆1, ∆3, ∆5 are located at the levels 0, 1, 2 respectively, ∆2, ∆7 occur between
the levels 0 and 1 while ∆4, ∆6 occur between the levels 1 and 2.

Deﬁnition 0.7. A semitransversal to a balanced polycycle is said to be properly
chosen if the characteristic function of the Dulac decomposition of the correspond-
ing monodromy transformation is non-positive.

Remark 0.2. A proper choice of a semitransversal is always possible for a balanced
polycycle. It corresponds to a cyclic permutation of the factors in the Dulac decom-
position.

Lemma 0.1 (Dulac [6]). For a suitable choice of the semitransversal, the mon-
odromy transformation for an unbalanced polycycle is either ﬂat or vertical (that is,
the inverse of a ﬂat one).

The non-accumulation theorem is obvious for unbalanced polycycles. In what
follows we consider only balanced polycycles.

58 Yu. S. Ilyashenko

0.7.3. The class of a monodromy transformation.

Deﬁnition 0.8. The class of the Dulac decomposition of a monodromy transforma-
tion ∆ for a balanced polycycle is the oscillation of the corresponding characteristic
function χ∆: class of ∆ = − min χ∆

provided that the semitransversal is properly chosen, that is, χ∆ ⩽ 0.

The class of a composite is the major parameter of induction used throughout
the whole proof. It is denoted by n. When n = 0 the polycycle is hyperbolic, and the
ﬁniteness theorem for such polycycles is proved above. This is the induction base.
When n > 0 the proof is by induction on n. All of what follows is the induction
step from n − 1 to n.
Before going on, we discuss two approaches to the theory of functional cochains
and prove the simplest version of the Phragm´en–Lindel¨of theorem for them. This
theorem shows that a functional cochain is an entity rather than the tuple of its
components.

0.8. The cohomological approach and the classical approach. Cochains
of the class N C in Deﬁnition 0.4 are regarded as tuples of functions uniquely
attached to the domains of the corresponding nice partition. Normalizing cochains
appeared almost simultaneously in Voronin’s paper [8] and in Malgrange’s talk at
the Bourbaki seminar in 1981. Both works were devoted to the analytic classiﬁcation
of parabolic germs of maps (C, 0) → (C, 0). Two germs are equivalent if and only if
they can be transformed into one another by a germ of an analytic coordinate change
(C, 0) → (C, 0). The moduli of this classiﬁcation are, roughly speaking, composition
coboundaries of the normalizing cochains. In Voronin’s paper, coboundaries are
understood as in Deﬁnition 0.5: tuples of functions in the narrow sectors that con-
tain the rays of the corresponding nice partition. In Malgrange’s paper they are
treated as elements of some cohomology group and no ﬁxed partition is considered.
In our approach it is crucial to consider ﬁxed partitions. Normalizing cochains,
as well as other functional cochains introduced below, are entities. For example,
a cochain of class N C is completely determined by its component N C u. This follows
from the Phragm´en–Lindel¨of theorem stated later in this section. The statement
makes use of the logarithmic chart, and we now turn to its description.

0.9. Transition to the logarithmic chart. A semitransversal to an elementary
polycycle can always be chosen to lie on an analytic transversal (an open interval
transversal to the ﬁeld). A chart on the semitransversal which is equal to zero at
the vertex and is analytically extendible to the transversal is said to be natural.
Its logarithm with the minus sign is called the logarithmic chart. A natural chart
is denoted by x, and the corresponding logarithmic chart by ξ. The transition
function is ξ = − ln x. In the natural chart, the monodromy transformation of the
polycycle is the germ of a map (R+, 0) → (R+, 0), and in the logarithmic chart
it is the germ of a map (R+, ∞) → (R+, ∞). The notation z = x + iy, ζ = ξ + iη
is used upon extension to the complex domain. The transition to the logarithmic
chart is denoted by a tilde: if a function f represents a map in the natural chart,
then ̃f represents the same map in the logarithmic chart.

Finiteness theorems for limit cycles 59

Table 1 contains examples of maps that will be used repeatedly in what follows.

Table 1

A map in the natural chart The same map in the logarithmic chart

1 Power: z ↦→ Czν Aﬃne: ζ ↦→ νζ − ln C

2 Standard ﬂat: z ↦→ exp(−1/z) Exponential: ζ ↦→ exp ζ

3 A map deﬁned on a sector
with vertex 0 and expandable in
a convergent or asymptotic Tay-
lor series ̂f = z(1 + ∑∞
1 ajzj)
 A map deﬁned on a horizontal
half-strip and expandable in a conver-
gent or asymptotic Dulac (exponential)
series ̃f = ζ + ∑∞
1 bj exp(−jζ)

4 hk,a : z ↦→ kzk(1 − az−k ln z)
−1 ̃hk,a : ζ ↦→ kζ − ln k − ln(1 −
aζ exp(−kζ))

5 An almost regular map with
asymptotic Dulac series at zero
z ↦→ Czν + ∑ Pj(z)zνj , where
C > 0, ν > 0, 0 < νj ↗ ∞, and
the Pj are real polynomials
 An almost regular map with asymp-
totic Dulac exponential series at inﬁn-
ity ζ ↦→ νζ −ln C +∑ Qj(ζ)·exp(−µjζ)
where C > 0, ν > 0, 0 < µj ↗ ∞, and
the Qj are real polynomials

The most important example is a normalizing cochain written in the logarithmic
chart. Upon transition to the logarithmic chart it becomes a map cochain deﬁned
on the half-plane C+
a : ξ ⩾ a, where a depends on the cochain.
The nice k-partition of a punctured disc by sectors becomes the partition of C+
a
into half-strips by the rays η = πm/k, m ∈ Z. The set of all normalizing cochains
that are written in the logarithmic chart and correspond to this partition is denoted
by N Ck. The additive coboundary δF of a cochain F is the set of pairwise diﬀerences
of the components of the cochain deﬁned in half-strips with a common boundary
ray, where the minuend corresponds to the upper half-strip.
We denote the aﬃne map ζ ↦→ kζ − ln k by ak and put

N C0 = ⋃

k ak ◦ N Ck ◦ a
−1
k .

Deﬁnition 0.9. The standard partition Ξst is the partition of a domain in C by
the rays η = πj, j ∈ Z. The intersection of a strip η ∈ [π(j − 1), πj] with this
domain is denoted by Πj.

All cochains in the class N C0 correspond to the standard partition of the half-
plane C+
a (a depends on the cochain F ∈ N C0). The half-strips Π0 and Π1 adjacent
to (R+, ∞) are called the main half-strips. In what follows, the maps in normalizing
cochains corresponding to the main half-strip of the standard partition will be
extended to a curvilinear half-strip close to the right half-strip |η| ⩽ π/2. The
existence of such an extension follows from Theorem 0.10.
This implies that the cochains in N C0 possess the following properties.
1. Each cochain F ∈ N C0 corresponds to the standard partition of some right
half-plane C+
a , where a depends on F .

60 Yu. S. Ilyashenko

2. All maps in the cochain can be extended to the ε-neighbourhoods of the corre-
sponding half-strips for some ε > 0. The maps corresponding to the main half-strips
Π0 and Π1 of the standard partition can be extended holomorphically to the germ
at inﬁnity of the half-strip Π
(ε)
∗ for every ε > 0 (see (4)), and the correction of the
extended map is bounded above by a decreasing exponential.
3. The modules of corrections of all maps in the cochain (extended as in the
previous property ) are bounded above by a decreasing exponential exp(−µξ), where
µ > 0 is the same for all maps in F .
4. The additive coboundary δF is bounded above by an iterated exponential in
the ε-neighbourhoods of all rays of the partition:

|δF | < exp(−C exp ξ) (6)

for some C > 0.
5. The cochain F can be expanded in an asymptotic Dulac exponential series
in its domain, including the extended components mentioned in property 2. This
means that the partial sums of the series approximate the components of the cochain
uniformly on the domains described in property 2, within the accuracy exp(−ν exp ξ)
for every ν > 0.
In what follows we use these and only these properties of the cochains of class
N C0. The set of all cochains with these properties is denoted by N C. We can
now state the simplest version of the Phragm´en–Lindel¨of theorem for functional
cochains. As mentioned above, it shows that a functional cochain is an entity.

0.10. The Phragm´en–Lindel¨of theorem for cochains of class N C.

Theorem 0.13. A cochain of class N C that decreases on (R+, ∞) faster than any
exponential, is identically 0.

Note that a holomorphic function in an arbitrary horizontal half-strip |η| < a
may decrease on (R+, ∞) faster than any exponential and be diﬀerent from zero.
We start with classical versions of the Phragm´en–Lindel¨of theorem.

0.10.1. Classical Phragm´en–Lindel¨of theorems and their modiﬁcations.

Theorem 0.14. Let D be a simply connected domain on the Riemann sphere such
that the boundary of D contains the point ∞. Suppose that f is holomorphic on D
and bounded and continuous on the closure of D, which is taken in the topology
of C and does not contain ∞. Then

sup
D |f | = sup
∂D |f |.

This theorem is a variant of the maximum principle for holomorphic functions.

Theorem 0.15. Suppose that a holomorphic function f : C+ → C+ is bounded on
the union of the imaginary axis and the positive semi-axis and increases no faster
than an exponential of the modulus: there is a ν > 0 such that |f (ζ)| < exp ν|ζ|.
Then f is bounded and supC+ |f | = sup∂C+ |f |.

Finiteness theorems for limit cycles 61

Proof. We ﬁrst prove that f satisﬁes the maximum principle in each of the sec-
tors S1, S2, where S1 is the ﬁrst coordinate quadrant and S2 is the fourth. Consider
the sector S1 and a family of barrier functions gε that are holomorphic on S1 and
have modulus greater than exp c|ζ|
1+δ for some c > 0 and δ > 0. For example,

gε(ζ) = exp ε(βζ)
1+δ, β = e
iπ/4.

For every positive value of the parameter ε, the quotient f /gε is bounded on S1
and, by Theorem 0.14,
 sup
S1
 ∣
∣
∣
∣ f
gε
 ∣
∣
∣
∣ = sup
∂S1
 ∣
∣
∣
∣ f
gε
 ∣
∣
∣
∣.

Letting ε → 0, we obtain that f is bounded on S1. Similarly, f is bounded on S2
and, therefore, on C+. Using Theorem 0.14 again, we get Theorem 0.15. □

Corollary 0.1. If a holomorphic function f : C+ → C is bounded and decreases
on R+ faster than any exponential exp(−νξ), ν > 0, then f ≡ 0.

Proof. The function f exp λζ satisﬁes the hypotheses of Theorem 0.15 for every
λ > 0. Since | exp λζ| = 1 on ∂C+, it follows that

sup
C+ |f (ζ)| | exp λζ| ⩽ sup
∂C+ |f |.

Assume that there is a point ζ such that Re ζ > 0 and f (ζ)̸=0. Then f (ζ) exp λζ →∞
as λ → ∞, a contradiction. □

Remark 0.3. We include these proofs because they give a sample of the proofs to
follow.

The following result is easily derived from the previous ones. It will be used in
what follows.

Corollary 0.2. Let Ω be a subdomain in C containing the ray R+
a : ξ > a for
some a > 0. Suppose that there is a conformal map ψ : Ω → C+ sending the germ
of the ray (R+, ∞) to a curve (Γ, ∞) whose germ at inﬁnity lies in some sector
Sα := {| arg ζ| < α}, α ∈ (0, π/2). Let f : Ω → C be a holomorphic function
increasing no faster than exp ν|ψ| for some ν > 0. Suppose that f is bounded
on ∂Ω and on R+
a . Then f is bounded on Ω and

sup
Ω |f | = sup
∂Ω |f |.

If, moreover, f decreases on R+
a faster than exp(−λ Re ψ) for all λ > 0, then f ≡ 0.

We now pass to the proof of Theorem 0.13.

0.10.2. Trivialization of a cocycle. In this subsection we take the ﬁrst step in the
proof of Theorem 0.13. Namely, for every functional cochain of class N C we shall
ﬁnd a ‘small’ cochain with the same coboundary. It follows that the diﬀerence of
these two cochains is a holomorphic function.
Let Ω be a quadratic standard domain, Ξ
ε the standard partition of Ωε, and ∂Ξ
ε

its boundary.

62 Yu. S. Ilyashenko

Lemma 0.2. Let F be an ε-extendible cochain of the class N C deﬁned in an
ε-neighbourhood Ωε of some quadratic standard domain. Suppose that its cobound-
ary in an ε-neighbourhood of the boundary of the standard partition is bounded
above by an iterated exponential m = exp(−C exp ξ) (see (6)) such that

m0 = sup
Ωε m, ∫

∂Ξε m ds = I < ∞.

Then there is an ε-extendible functional cochain Φ deﬁned on Ω such that

δF = δΦ on ∂Ξ, max
Ω |Φ| ⩽ Cε−1(m0 + I),

where C is a constant independent of F .

Proof. Let Ξ and ∂Ξ
ε be the same as at the beginning of this subsection. We deﬁne
the cochain Φ by a Cauchy-type integral:

Φ(ζ) = 1
2πi
 ∫

∂Ξε δF (τ )
τ − ζ dτ.

By a well-known theorem of complex analysis (see, for example, [12]) we have
δF = δΦ, where the coboundaries δF and δΦ are calculated on each boundary
ray by letting the minuend (resp. subtrahend) correspond to the domain above
(resp. below) the ray. We now obtain upper bounds for F in Ω.
1) Suppose that dist(ζ, ∂Ξ
ε) ⩾ ε. Then |Φ(ζ)| ⩽ ε−1I.
2) Suppose that dist(ζ, ∂Ξ
ε) < ε and ζ belongs to a domain D of the partition Ξ.
Then the disc K with centre ζ and radius ε lies in the ε-neighbourhood of D. We
replace the integral over the chord of the disc in the formula for Φ by an integral
over the arc of K that has the same endpoints as the chord and is such that
the arc and the point ζ are separated by the chord. The integral over the arc is
bounded above by 2πm0/ε, and the integral over the remaining part of the contour
is bounded above by I/ε. □

The cochain Φ provided by this lemma is called the trivialization of the cocy-
cle δF .

0.10.3. The maximum modulus principle for functional cochains.

Lemma 0.3 (maximum modulus principle for the class N C). Under the hypotheses
of Lemma 0.2 suppose that the functional cochain F grows no faster than exp νξ
for some ν > 0 and is bounded on ∂Ω and R+. Then F is bounded on Ω and

sup
Ω |F | ⩽ sup
∂Ω |F | + 2Cε−1(m0 + I),

where ε, m0, I, C are the same as in the previous lemma.

Proof. Let Φ be the trivialization of δF provided by the previous lemma. Then
the diﬀerence F − Φ is a holomorphic function on Ω satisfying the hypotheses
of Corollary 0.2. Hence,

sup
Ω |F | ⩽ sup
Ω |F − Φ| + sup
Ω |Φ| ⩽ sup
∂Ω |F | + 2 sup
Ω |Φ|.

The bound for |Φ| in the previous lemma now yields the desired bound. □

Finiteness theorems for limit cycles 63

0.10.4. A preliminary estimate and completion of the proof of the Phragm´en–
Lindel¨of theorem for cochains of class N C.

Lemma 0.4 (a preliminary estimate for cochains of class N C). Let F be a cochain
of class N C that decreases on (R+, ∞) faster than any exponential. Then the
following inequality holds in the strip Π0 ∪ Π1:

|F (ζ)| ⩽ exp(−C exp ξ)

for some C > 0 independent of ζ.

The Phragm´en–Lindel¨of theorem for the class N C says that under the hypotheses
of Lemma 0.4 we have F ≡ 0. This can easily be derived from the lemma and this
will be done at the end of this subsection. In what follows we use a ‘universal
constant’ C that may take diﬀerent values in diﬀerent inequalities.

Proof of Lemma 0.4. We may assume without loss of generality that |F | ⩽ 1 on Ωε,
where Ω
ε is the ε-neighbourhood of a standard quadratic domain Ω. Indeed, by
property 3 in the deﬁnition of N C, all components Fj of F satisfy a uniform bound
|Fj| ⩽ C|ζ| on Ωε. Hence the cochain F exp(−ζ) is bounded on Ωε. Multiplying
this product by a suitable constant, we get a cochain F1 such that |F1| ⩽ 1 on Ω
ε.
In what follows we omit the subscript 1.
Let ψ : Ω → (C+, ∞) be a conformal map. For suﬃciently large a ∈ R+ we
deﬁne the domain Ωa = {ζ | Re ψ(ζ) ⩾ Re ψ(a)}.

Note that ψ is real on (R+, ∞), whence Re ψ(a) = ψ(a).
Consider a cochain Fλ,a def
= F exp λ(ψ(ζ) − ψ(a)).

It decreases on (R+, ∞) faster than any exponential (since F does) and ψ =
ζ(1 + o(1)). Hence the maximum principle for functional cochains is applicable
to it. We shall estimate the values of I and m0 for a large and λ properly depend-
ing on a. To do this, we estimate the coboundary of Fλ,a from above. We have

|δF | ⩽ m(ζ) = exp(−C exp ξ).

Hence, |δFλ,a(ζ)| ⩽ exp
(−C exp ξ + λ Re(ψ(ζ) − ψ(a))
).

Since Ω is a quadratic standard domain, the vertical line Re ζ = ξ crosses no
more than Cξ2 boundary lines of the standard partition. Hence,

I(a) ⩽ C ∫ ∞

a−ε ξ2 exp
(−C exp ξ + λ Re(ψ(ζ) − ψ(a))
) dξ.

We denote the integrand by m+. The integral I(a) is easily estimated if

m
′
+
m+ ⩽ −1 for ξ ⩾ a − ε, m
′
+ = dm+
dξ . (7)

64 Yu. S. Ilyashenko

In this case,

m+(ξ) ⩽ m+(a − ε) exp(a − ε − ξ), I(a) ⩽ Cm+(a − ε).

At the same time, m0 ⩽ m+(a − ε).

We have
 m+(a − ε) = (a − ε)
2 exp
(− exp(a − ε) + λ(ψ(a − ε) − ψ(a))
).

Note that the second term in the exponent is negative. Hence,

m+(a − ε) ⩽ (a − ε)
2 exp(− exp(a − ε)).

For suﬃciently large a the right-hand side is smaller than Cε for any prescribed
constant C. Hence, for a large,
 2ε−1(m0 + I) < 1.

Then, by the maximum modulus principle,

|Fλ,a(ζ)| < 2. (8)

We now turn to (7). We have

ln m+ = 2 ln ξ − exp ξ + λ Re(ψ(ζ) − ψ(a)).

Therefore,
 (ln m+)
′ = 2
ξ − exp ξ + λ(1 + o(1)).

For λ = 1
2 exp a

and a large enough, the inequality (7) holds. Hence the estimate (8) also holds.
We now want to estimate |F (ζ)| for a given ζ ∈ Π0 ∪ Π1. Take an a ∈ R such
that Re ψ(ζ) − ψ(a) = 1. Since ψ = ζ + C√ζ, we have |a − Re ζ| ⩽ c for some c
independent of ζ. By (8) we have

|F (ζ)| ⩽ 2 exp
(− 1
2 exp a
) ⩽ exp(−C1 exp ξ)

for some C1 > 0 independent of ζ. This proves Lemma 0.4. □

We now prove the Phragm´en–Lindel¨of theorem for the class N C. The estimates
obtained above remain valid if we replace F by F u or F l. By property 2 in § 0.9
these components are holomorphic in a strip wider than π. By property 3, they are
bounded above on Π1 ∪ Π0 by Cξ for some C > 0. At the same time, these func-
tions decrease on (R+, ∞) as exp(−C exp ξ). By the classical Phragm´en–Lindel¨of
theorem, F u ≡ F l ≡ 0. Using the same argument and induction on j, we establish
that the jth component of F is equal to zero. This completes the proof of the
Phragm´en–Lindel¨of theorem for cochains of class N C.
The Phragm´en–Lindel¨of theorem for the more tricky functional cochains is pre-
sented in § 2.
 Finiteness theorems for limit cycles 65

§ 1. Decomposition of monodromy transformations
into terms with incomparable rates of decay

This section is the central one. Here we prove the ﬁniteness theorem modulo
auxiliary results. These results are then schematically proved in the rest of the
paper.

1.1. A monodromy transformation with prescribed asymptotics. In this
subsection we prove the easier part of the asymptotic theorem. For any given num-
bers µ, 0 < µ < ν, and n ∈ Z
+ we shall construct a polycycle whose monodromy
transformation satisﬁes (1). The polycycle will have two hyperbolic (and even lin-
ear) saddles and 2n saddlenodes. The properly chosen transversal Γ will be located
on an edge connecting the two linear saddles. We put

Ad(f )g = f −1 ◦ g ◦ f Ag = Ad(exp)g, A−1g = Ad(ln)g.

The saddlenodes will be oriented in such a way that the monodromy transforma-
tion ∆ will take the following form in the logarithmic chart:

∆ = Ad(α)A
n(ξ + exp(−ξ)), µ < α < ν. (9)

We ﬁrst construct a polycycle with this monodromy transformation and then check
that it satisﬁes (1).
Consider 2n + 2 copies of the unit square [−1, 1]
2 with coordinates

(x0, y0), . . . , (xn, yn), (Xn, Yn), . . . , (X0, Y0)

and deﬁne vector ﬁelds on them by the formulae

v0 = (x0, −αy0), v1 = (x
2
1, −y1), . . . , vn = (x
2
n, −yn),

Vn = (X 2
n, Yn), . . . , V1 = (X 2
1 , Y1), V0 = (−X0, 1
α Y0
)

(see Fig. 2). We glue together parts of the boundaries of the squares and deﬁne the
polycycle as a glued union of the oriented closed intervals on the coordinate axes
ordered as follows: [1, 0] on Oyj, [0, 1] on Oxj, [−1, 0] on OXj, [0, 1] on OYj; the
order is Oy0, Ox0, . . . , Oyn, Oxn, OXn, OYn, . . . , OX0, OY0.

The gluing maps identify neighbourhoods of 0 on the following sides:

xj = 1 and yj+1 = 1, j = 0, . . . , n − 1,

xn = 1 and Xn = −1,

Yj = 1 and Xj−1 = −1, j = n, . . . , 1,

Y0 = 1 and y0 = 1.

The coordinates on these sides are yj, xj+1, yn, Yn, Xj, Yj−1 and X0, x0. We recall
that in the hyperbolic sector under consideration we have Xj ∈ [−1, 0]. The gluing

66 Yu. S. Ilyashenko

Figure 2

functions are

x1 = f0(y0) = y0, xj+1 = fj(yj) = e
−1yj, j = 1, . . . , n − 1,

Yn = fn(yn) = yn exp(−e
−1yn),

Yj−1 = Fj(Xj) = −eXj, j = n, . . . , 2,

Y0 = F1(X1) = −X1, x0 = F0(X0) = −X0.

The correspondence maps are of the form

y0 = x
α
0 , yj = e · e
−1/xj , j = 1, . . . , n,

|Xj| = − 1
ln(Yj · e−1) , j = n, . . . , 1, |X0| = Y 1/α
0 .

Together with the gluing maps we have

x1 = x
α
0 , xj+1 = e
−1/xj , j = 1, . . . , n − 1,

|Xn| = Ad(e
−1/x)(xn exp(−xn)),

|Xj−1| = − 1
ln |Xj| , j = n, . . . , 2, |X0| = |X1|
1/α.

Finiteness theorems for limit cycles 67

It follows that ∆ = Ad(f [n]
0 ◦ x
α)(x exp(−x)).

In the logarithmic chart this map takes the form (9).
It is easily proved by induction on n that

A
n(ξ + exp(−ξ)) = ξ + (1 + o(1))(exp(−ξ))(exp(− exp ξ)) · · · (exp(− exp
[n] ξ)).

Hence,

∆ = Ad(α)A
n(ξ + exp(−ξ)) = ξ + (α−1 + o(1))(exp(−αξ)) · · · exp(− exp
[n] αξ).

This map satisﬁes (1).
We have thus constructed a piecewise-analytic vector ﬁeld on a topological annu-
lus with prescribed asymptotics of the monodromy transformation.
We can now change the complex structure on this annulus in such a way that
the vector ﬁeld becomes real-analytic. This trick was ﬁrst used in [7].
This proves the second part of Theorem 0.5.

1.2. Dulac maps for saddlenodes revisited. Denote by H the set of germs
of maps (C+, ∞) → (C+, ∞) obtained from parabolic germs of holomorphic maps
(C, 0) → (C, 0) by passing to the logarithmic chart.
The set of almost-regular germs whose aﬃne principal part is the identity is
denoted by R0.
Finally, we write Aﬀ for the set of germs of aﬃne maps (C+, ∞) → (C+, ∞)
with real coeﬃcients and positive multiplier, and let MR (R for real mappings) be
the set of germs of maps whose restrictions to (R+, ∞) act as (R+, ∞) → R (below
such germs are referred to as real).
After minor calculations, Theorem 0.11 implies that

TO ⊂ (H ◦ exp ◦R0 ◦ N C ◦ Aﬀ) ∩ MR =: TO. (10)

Denote by FROM the class of germs at inﬁnity inverse to those in TO. These
two classes are the main ones considered in what follows.

1.3. The ﬁnal structure theorem. Let Gn be the group of all balanced com-
positions of maps in the families TO, FROM and R of class (depth) at most n.
We recall some notation and introduce some more. If A1, . . . , Am are subsets of
a group, then we write Gr(A1, . . . , Am) and Gr+(A1, . . . , Am) for the group and
semigroup (respectively) generated by them. The set of all products am ◦ · · · ◦ a1,
aj ∈ Aj, is denoted by Am ◦ · · · ◦ A1.
If A and B are subsets of some group, then Ad(A)B = Gr(Ad(a)b | a ∈ A, b ∈ B).
If B is a normal subgroup of the group G = Gr(A, B), then every element g ∈ G
can be represented in the form g = ab, where a ∈ A and b ∈ B. In this case we
write G = BA = AB. Let R, R0 and Aﬀ be the same classes as above. Then
R = Aﬀ ◦R0.
Consider a cluster of maps ̃∆ ∈ FROM ◦ R ◦ TO in the composition (5). By
the deﬁnition of level in § 0.7.2, the ﬂanking maps lie between the levels j − 1, j for
some j, and the other maps (belonging to R) are at the level j. We say that ̃∆ lies

68 Yu. S. Ilyashenko

between the levels j − 1 and j. We now rearrange the composition ̃∆ and redeﬁne
the notion of level in such a way that every factor, except for exp and ln, will have
a certain level.
We ﬁrst insert in the composition a product exp
[j−1] ◦ ln
[j−1] immediately before
and after each cluster ̃∆ ∈ FROM ◦ R ◦ TO that lies between the levels j − 1 and j.
When j ⩽ n − 1, the new cluster A
j−1 ̃∆ belongs to Gn−1. The group Gn diﬀers
from Gn−1 by clusters of the form A
n−1 ̃∆:

Gn = Gr(A
n−1(FROM ◦ R ◦ TO), Gn−1). (11)

Note that all factors on the right-hand side are real on the real axis. Hence their
composites are well deﬁned in some neighbourhood of (R+, ∞). We now decompose
the clusters FROM and TO into factors that in general are not real on the real
axis. As a compensation, every factor in the resulting composition will be located
at one level only, in a sense explained below.
The composition FROM ◦ R ◦ TO is of the form

FROM ◦ R ◦ TO = Aﬀ ◦N C−1 ◦ R0 ◦ A(H ◦ R ◦ H) ◦ R0 ◦ N C ◦ Aﬀ .

We want to separate the normalizing cochain in this composition from the factor
belonging to A(H ◦ R ◦ H). To do this, we need the following deﬁnitions.

Deﬁnition 1.1. Put A0 = Gr(f ∈ R0 ◦ N C | there is a ̃g ∈ H : Ãg ◦ f is real).

The class H is not contained in R since all germs in R are real on (R+, ∞), while
those in H need not be. This fact together with the preceding formula motivates
the following deﬁnition.

Deﬁnition 1.2. H 0 = Gr(Ad(Aﬀ)H, R0).

Therefore we get

FROM ◦ R ◦ TO ⊂ Aﬀ ◦A0 ◦ A(H 0 ◦ Aﬀ) ◦ A0 ◦ Aﬀ .

Denote by T the group of real translations. It is easy to see that

A(Aﬀ) ⊂ T ◦ R0, Ad(T )R0 = R0, Ad(T )N C = N C.

Hence we can get rid of the factor A(Aﬀ) in the formula above:

FROM ◦ R ◦ TO ⊂ Gr(R, A0, A(H 0)).

Moreover, A
n−1R ⊂ Gn−1. Therefore,

Gn ⊂ Gr(Gn−1, An−1A0, AnH 0) =: ̃Gn. (12)

We now extend the notion of level and say by deﬁnition that the factors in
A
n−1A0, A
nH 0 are located at the levels n − 1, n respectively. Note that ̃Gn−1 =
Gr(Gn−2, An−2A0, An−1H 0). There are clusters in A
n−1H 0 at level n − 1 in this

Finiteness theorems for limit cycles 69

group. But they are diﬀerent from the clusters in A
n−1A0 at level n − 1 that occur
in the group ̃Gn.
Note that the maps of classes FROM, TO, R are real on (R+, ∞). Hence their
composites are well deﬁned on (R+, ∞) and, therefore, in some neighbourhood
of (R+, ∞). On the contrary, the maps of classes A0, H 0 are not real on (R+, ∞).
Yet the following lemma holds.

Lemma 1.1. Every germ in ̃Gn is well deﬁned in some neighbourhood of (R+, ∞).

A proof is brieﬂy outlined in § 1.5.3.

All germs in Gn are real. This yields the following result.

Theorem 1.1 (ﬁnal structure theorem). We have

Gn ⊂ ̃Gn ∩ MR.

1.4. Strategy I. The strategy of the present proof of the ﬁniteness theorem is
diﬀerent from the original one. To describe the monodromy transformations of
class n, we must introduce functional cochains and standard domains of class n.
These classes depend on n, and the ﬁrst of them contains all normalizing cochains,
but is much wider. In the original proof [1] these classes were deﬁned immediately
after the statement of the ﬁnal structure theorem. Then some main properties of
these classes were stated without proof, and the ﬁniteness theorem was deduced
from these properties. The rest of the book [1] was devoted to the proof of these
properties.
The deﬁnitions of functional cochains and standard domains of class n were
given by induction on n and were rather long and involved. Given without suﬃcient
motivation, they formed a sort of barrier in front of the proofs of the main theorems.
The proof to come is organized in a diﬀerent way. First, we give a new and
simple deﬁnition of standard domains of class n. It is straightforward and uses
no induction. Second, we give an axiomatic description of functional cochains of
class n. It is much shorter than their explicit deﬁnition. Then we deduce the main
theorems from the axioms. After that we give an explicit deﬁnition of functional
cochains of class n, thus building a model for the given axioms. This is the same
deﬁnition as in the original proof, slightly modiﬁed. At this stage, it is well moti-
vated by the previous material. We also add brief motivations for the key details
of the deﬁnitions.
The rest of the proof is devoted to checking that the model constructed does
indeed satisfy the axioms. From now on, we ﬁx n > 0. All objects of class m deﬁned
below are considered for m ⩽ n. Various induction assumptions are assumed to
hold for m ⩽ n − 1. They are proved for m = n at the induction step from n − 1
to n.

1.5. Axiomatic description of functional cochains of class n. The descrip-
tion mentioned in the title makes use of some operations over functional cochains
that are deﬁned in the following subsection.

70 Yu. S. Ilyashenko

1.5.1. Functional cochains and map-cochains. Let Ω ⊂ C be an arbitrary domain,
and let Ξ be a locally ﬁnite partition of Ω into analytic polyhedra: each domain
of the partition is the closure of an open set given by ﬁnitely many inequalities of
the form ω < 0, where ω is a real-analytic function on a subdomain of R2. A tuple
F = {fj} of functions is called a functional cochain corresponding to the partition Ξ
if the functions in the tuple are in one-to-one correspondence with the domains of
the partition, and each function extends holomorphically to some neighbourhood
of its domain of the partition. The partition corresponding to a functional cochain F
is denoted by Ξ
F . The functions fj are called components of F .
The coboundary δF of a functional cochain F is deﬁned as the following tuple of
holomorphic functions on the boundary lines of the partition. Let L be a boundary
curve of the partition Ξ
F . In what follows we consider only those partitions whose
boundary curves admit a bijective projection onto (R+, ∞) along the vertical lines.
This endows these curves with an orientation inherited from (R+, ∞). Consider an
ordered pair of domains of the partition with a common boundary curve L such
that the ﬁrst domain lies to the left of this curve, and let f1, f2 be the ordered pair
of functions corresponding to these domains. Then f1 − f2 is the component of δF
deﬁned in some neighbourhood of L. The tuple of these components is called the
additive coboundary of the cochain.
Map-cochains are deﬁned similarly to functional cochains. We only require that
the functions fj map the corresponding domains of the partition biholomorphically
onto their images. The composition coboundary is deﬁned as the additive one, with
the diﬀerence of the components replaced by their composition quotient.

Example 1.1. Our main examples are normalizing cochains written in the loga-
rithmic chart. The role of Ω is played by the right half-plane C+
a : Re ζ > a > 0
for some a. The corrections of the composition coboundaries decrease like double
exponentials.

Functional cochains can be added, subtracted and multiplied. Compositions are
deﬁned for map-cochains.
Recall that the product of two partitions is the partition formed by the pairwise
intersections of their domains.
The sum of functional cochains F and G is a functional cochain denoted by F +G
and corresponding to the product of the partitions Ξ
F and Ξ
G. This means that
to the intersection U1 ∩ U2 of two domains of the partitions Ξ
F and Ξ
G there
corresponds the function f1 + g1, which is equal to the sum of the components of F
and G corresponding to U1 and U2 respectively. The diﬀerences and products of
functional cochains are deﬁned analogously. We note that the sums, diﬀerences and
products of functional cochains on the same domain Ω are always well deﬁned.
Let F be a functional cochain, and let id +G be a map-cochain such that G → 0
at inﬁnity. The composite F ◦ (id +G) is deﬁned componentwise like the sum.
It is not always well deﬁned. A suﬃcient condition for the composite to be well
deﬁned is the existence of a positive number ε such that all components of F
extend to the ε-neighbourhoods of the corresponding domains of the partition, and
the correction G of the cochain id +G is less than ε in modulus. In more detail,
let fj be a component of F , Dj the domain of fj, and gk a component of G with

Finiteness theorems for limit cycles 71

domain ̃Dk such that Dj ∩ ̃Dk =: D ̸= ∅. By deﬁnition, fj ◦ (id +gk) is the
component of F ◦ (id +G) deﬁned on D provided that the following holds: fj can
be extended holomorphically to some ε-neighbourhood Dε of D and |gk| < ε/2
on Dε. Then the composite fj ◦ (id +gk) can be extended to Dε/2.
In what follows all partitions will have a boundary line (R+, ∞).

1.5.2. Standard domains.

Deﬁnition 1.3. A standard domain is a domain which is symmetric with respect
to the real axis, lies in the right half-plane and admits a real conformal map onto
the right half-plane that has derivative of the form 1 + o(1) as ζ → ∞ and extends
for some δ > 0 to the δ-neighbourhood of the part of the domain outside a compact
set. Moreover, ξ → ∞ as ζ → ∞ in this domain.

Quadratic standard domains satisfy this deﬁnition, and the right half-plane
does not.

Deﬁnition 1.4. A standard domain of class m > 0 corresponding to the constants
ε > 0 and C > 0 is a domain of the form

Ωm,ε,C = Φm,ε(C+
C), (13)

where

Φm,ε : ζ ↦→ ζ(1 + (ln
[m−1] ζ)
−ε), C+
C = C+ \ KC, KC = {|ζ| ⩽ C}. (14)

Remark 1.1. For all m, ε one can ﬁnd a number C(m, ε) such that for every C >
C(m, ε) the domain Ωm,ε,C is standard in the sense of Deﬁnition 1.3, and the
map Φm,ε in the deﬁnition of this domain is conformal on C+ \ KC. We recall that
there is a conformal map C+ \ KC → C+ of the form ζ + o(1) at (C+, ∞).

Deﬁnition 1.5. The set Ωm of standard domains of class m > 0 is the set of
all domains Ωm,ε,C with C > C(m, ε), where the number C(m, ε) is so large that
Φm,ε is biholomorphic on Ωm,ε,C. The set Ω0 is the class of all quadratic standard
domains.

1.5.3. Extended groups Gn and functional cochains of class n. In what follows we
extend the group Gn to Gn. This is done by induction on m ⩽ n.
Base of induction: the groups G−1 and G−1 (as well as G0 and G0) coincide:
G−1 = Aﬀ, G0 = R.
Induction step: suppose that the groups Gm ⊃ Gm, m < n, have already
been constructed. The group Gn diﬀers from Gn−1 by the compositions in
A
n−1(FROM ◦ R ◦ TO). New functional cochains may (and do) occur at the
levels n − 1 and n. They are referred to as functional cochains of class n and
types 1 and 0 respectively, and the sets of them are denoted by FCn−1
1 and FCn
0
(the superscript is the level, the subscript is the type, and their sum is the class).
These functional cochains will be described axiomatically, again by induction on n.
When n = 0 they are just the aﬃne and almost regular maps respectively.
The following new set occurs at level n − 1 for n ⩾ 1:

J n−1 = Ad(Gn−1)A
n−1A0. (15)

72 Yu. S. Ilyashenko

In what follows, an estimate of a cochain is understood as a uniform estimate
for its components on some representative of the germ at inﬁnity of the domain of
this cochain.
A cochain F is said to be rapidly decreasing if it decreases exponentially fast on
its domain (always contained in the right half-plane):

|F (ζ)| ≺ exp(−εξ) for some ε > 0.

The set of such cochains in FCn−1
1 (resp. FCn
0 ) is denoted by FCn−1
1+ (resp. FCn
0+).
The new set occurring at level n for n ⩾ 1 is deﬁned in terms of the set FCn
0 :

H n = Gr(id +FCn
0+ ◦ exp
[n] ◦g | g ∈ Gn−1).

Here is the ﬁrst axiom concerning cochains of class n.

Inclusion axiom. The sets J n−1 and H n are well deﬁned. Moreover,

A
nH 0 ⊂ H n, (16)

J n−1 ⊂ Gr(id +FCn−1
1+ ◦ exp
[n−1] ◦ g | g ∈ Gn−2). (17)

The second assertion of this axiom will be repeated later as a part of another
axiom called the fourth shift lemma. Note that FCn
0 consists of functional cochains
deﬁned on standard domains Ω ∈ Ωn. The composites in FCn
0 ◦ exp
[n] are deﬁned
in very narrow neighbourhoods ln
[n] Ω of the ray (R+, ∞). We put

̃Gn = Gr(Gn−1, J n−1, H n), Gn = ̃Gn ∩ MR. (18)

The group operation in ̃Gn is composition. All germs of map-cochains in Gn
are deﬁned on germs at inﬁnity of neighbourhoods of the ray (R+, ∞). These
germs of domains depend on the germs of the corresponding map-cochains. Germs
in Gn−1 are holomorphic on their (narrow) domains. Germs in J n−1 and H n are
map-cochains in domains so narrow that the only jump line is (R+, ∞). Taking the
composites of the upper components of both entries and then the composites of
the lower ones, we obtain a new map-cochain with jump line (R+, ∞). The additive
decomposition theorem enables us to extend these composites to domains that can
be described explicitly. However, we do not need this description.
Let us give a brief sketch of the proof that the group ̃Gn is well deﬁned. At the
same time this will yield Lemma 1.1. Below we state the so-called shift lemmas,
which imply that ̃Gn = Gn−1 ◦ J n−1 ◦ H n.

We then prove that every element of this composition is well deﬁned in some neigh-
bourhood of (R+, ∞).
The ﬁrst assertion (16) of the inclusion axiom together with Theorem 1.1 implies
that Gn ⊂ Gn.
We will prove the identity theorem for elements of the group Gn. Arguing by
induction on n, we assume that the theorem has already been proved for Gn−1.
Hence for every g ∈ Gn−1 we have either g ≺ id, or g = id, or g ≻ id. Thus the
group Gn−1 is ordered by the following relation: g1 ≺ g2 if and only if g1 − g2 ≺ 0
or, equivalently, g1 ◦ g−1
2 ≺ id.

Finiteness theorems for limit cycles 73

1.5.4. Ordered groups and generalized multipliers. Let G be a group of germs
(R+, ∞) → (R+, ∞) that contains the map A
ngc for some c > 0, where gc(ξ) = cξ.
Suppose that G is ordered by the relation

g1 ≺ g2 if and only if g1 − g2 ≺ 0. (19)

Then the following map is well deﬁned:

λn : G → R, g ↦→ lim
(R+,∞) A
−ng(ξ)
ξ .

Indeed, λn(g) = sup{c | A
ngc ≺ g}.

The image λn(g) is called the (nth) generalized multiplier of g. For a ﬁxed n and
for the same group G as above, we put

λ−1
n (0) = G−
slow, λ−1
n (R+) = Grap, λ−1
n (∞) = G+
slow.

This notation is explained as follows. The corrections of the germs g ∈ Grap
decrease so rapidly that λn(g) ∈ R+, and those of the germs in G \ Grap decrease
so slowly that λn(g) = 0 or ∞. The superscript ‘+’ (resp. ‘−’) is used to refer to
inﬁnity (resp. zero).
By the induction hypothesis, the group Gk is ordered for every k ⩽ n − 1. It is
easy to see that A
k+1gc ∈ Gk. Indeed, A
2(gc) ∈ R0 and A
k−1R0 ⊂ Gk. Hence the
map λk+1 and the subsets Gk
slow, Gk
slow, Gk
rap are well deﬁned.

1.5.5. Motivation for the shift lemmas. Here we motivate the lemmas (axioms) to
follow. By (12), we conclude that the group ̃Gn may contain elements of the form

∆ = A
nF ◦ A
n−1G, F ∈ H 0, G ∈ A0.

The factors A
nF , A
n−1G are in the ‘wrong order’, preventing the future study
of the asymptotics of ∆. We would like to reverse this order and write, if possible,

∆ = A
n−1 ̃G ◦ A
n ̃F , ̃G ∈ A0, ̃F ∈ H 0.

However, this is impossible. We must extend A
n−1A0 and A
nH 0 to the classes
J n−1 and H n (deﬁned in § 1.5.3) for which there are classes of germs Φ ⊃ J n−1 −id,
Ψ ⊃ H n − id with the following properties. The classes Φ and Ψ are vector spaces
and, for all ϕ ∈ Φ and ψ ∈ Ψ,
• ϕ and ψ are deﬁned in some neighbourhoods of the ray (R+, ∞) depending
on ϕ, ψ;
• ϕ → 0, ψ → 0 at inﬁnity in their domains;
• the composites (id +ϕ)
−1, (id +ϕ) ◦ (id +ψ) and (id +ψ) ◦ (id +ϕ) are deﬁned
on the germ of some neighbourhood of (R+, ∞) and we have

(id +ϕ)
−1 = id − ̃ϕ, ̃ϕ ∈ Φ; (20)

ϕ ◦ (id +ψ) = ϕ + ̃ψ, ̃ψ ∈ Ψ; (21)

ψ ◦ (id +ϕ) = ̂ψ, ̂ψ ∈ Ψ. (22)

74 Yu. S. Ilyashenko

Note that (21), (22) and further equalities in this subsection hold on the inter-
section of some neighbourhood of the positive semi-axis with the upper half-plane.
These properties yield the following principle.

Shift–conjugacy principle. Under the assumptions above, for all ϕ ∈ Φ, ψ ∈ Ψ
there is an element ψ1 ∈ Ψ such that

(id +ψ) ◦ (id +ϕ) = (id +ϕ) ◦ (id +ψ1).

Proof. We start with the identity

(id +ψ) ◦ (id +ϕ) = (id +ϕ) ◦ Ad(id +ϕ) ◦ (id +ψ).

The following chain of equalities completes the proof:

Ad(id +ϕ) ◦ (id +ψ) = (id − ̃ϕ) ◦ (id +ψ) ◦ (id +ϕ)

= (id +ψ − ̃ϕ ◦ (id +ψ)) ◦ (id +ϕ) = (id − ̃ϕ − ̃ψ + ψ) ◦ (id +ϕ)

= (id − ̃ϕ) ◦ (id +ϕ) − ̂ψ ◦ (id +ϕ) = id +ψ1, ̃ϕ ∈ Φ, ̂ψ, ψ1 ∈ Ψ.

The ﬁrst equality follows from (20), the second is obvious, the third follows from (21),
the fourth holds because Ψ is a vector space, and the ﬁfth follows from (22). □

The relations (20)–(22) are models for the shift lemmas (axioms) to follow. These
lemmas (axioms) enable us to make similar permutations in the group ̃Gn and prove
the main results: the multiplicative and additive decomposition theorems.

1.5.6. Shift lemmas. The four shift lemmas stated below (as well as other assertions
in §§ 1.5.3–1.5.9) are regarded as axioms that hold for all functional cochains of the
classes FCm, m < n. The multiplicative and additive decomposition theorems
(stated below) follow from these axioms.
We emphasize once again that, by the induction hypothesis, all these lemmas
and theorems are assumed to be proved for 1 ⩽ m ⩽ n − 1 (where n is the positive
integer ﬁxed above). The same is assumed about Theorems MDTm and ADTm
stated below. The induction base is presented in § 1.5.10.
Equalities with plus in brackets mean that the equality holds with plus (and
then with no brackets) as well as without plus.

Lemma 1.2 (the ﬁrst shift lemma, axiom SL1n). a) FCn
0(+) ◦ exp
[n] ◦Gn−1
rap =
FCn
0(+) ◦ exp
[n];

b) FCn−1
1(+) ◦ exp
[n−1] ◦Gn−2
rap = FCn−1
1(+) ◦ exp
[n−1]. This equality holds on the inter-
section of the germ at inﬁnity of some neighbourhood of the positive semi-axis with
the upper half-plane (in what follows we brieﬂy say: on an upper half-neighbourhood
of the positive semi-axis ).

Convention. Suppose that n is ﬁxed as above, and 1 ⩽ m ⩽ n. Then FCm stands
for FCm
1 if m ⩽ n − 1, and FCn
0 if m = n.
Suppose that m ⩽ n, g ∈ Gm−1. Then we put

F m
(+)g = FCm
(+) ◦ exp
[m] ◦g.

Finiteness theorems for limit cycles 75

According to our convention, this means that

F m
(+)g = FCm
1(+) ◦ exp
[m] ◦g, m ⩽ n − 1; F n
(+)g = FCn
0(+) ◦ exp
[n] ◦g.

By the same convention, the axiom SL1n takes the following form.

Lemma 1.3 (SL1n). Suppose that m = n − 1 or m = n, g ∈ Gm−1
rap . Then

F m
(+)g = F m
(+) id.

This equality holds in an upper half-neighbourhood of the positive semi-axis.

The last requirement needs a comment. By deﬁnition, every element ϕ ∈ F m
g is
of the form ϕ = F1 ◦ exp
[m] ◦g, F1 ∈ FCm.

The lemma asserts that there is a cochain F ∈ FCm such that F = F1 ◦ A
−mg and
this equality holds in the intersection of some standard domain of class m with the
upper half-plane.
Before stating the next lemma, we give a deﬁnition.

Deﬁnition 1.6. a) For f and g belonging to Gk we write f ≺≺ g in Gk if and
only if f ◦ g−1 ∈ Gk−
slow;
b) (k, f ) ≺ (m, g) if and only if f ∈ Gk−1, g ∈ Gm−1 and either k < m, or k = m
and f ≺≺ g in Gm−1.

Lemma 1.4 (the second shift lemma, axiom SL2n). Let m = n − 1 or m = n.
Suppose that (k, f ) ≺ (m, g) and ϕ ∈ F k
f . Then

ϕ ◦ (id +F m
+g) ⊂ ϕ + F m
+g.

This equality holds in an upper half-neighbourhood of the positive semi-axis.

In more detail, for all elements

ϕ = F1 ◦ exp
[k] ◦ f, F1 ∈ FCk, f ∈ Gk−1,

ψ = F2 ◦ exp
[m] ◦ g, F2 ∈ FCm
+ , g ∈ Gm−1,

there is a cochain F ∈ FCm such that

F = F1 ◦ ρ − F1 ◦ (ρ + F2), ρ = exp
[k] ◦ f ◦ g−1 ◦ ln
[m]

and the equality for F holds in the intersection of some standard domain of class m
with the upper half-plane.

Lemma 1.5 (the third shift lemma, axiom SL3n). a) Let m = n − 1 or m = n.
Suppose that f ≻≻ g in Gm−1 or f ◦ g−1 ∈ Gm−1
rap . Then

F m
(+)f ◦ (id +F m
+g) ⊂ F m
(+)f .

This inclusion holds in an upper half-neighbourhood of the positive semi-axis (see
the comment after the statement of the lemma ).
b) (id +F m
+g)
−1 = id +F m
+g for an arbitrary g ∈ Gm−1.

76 Yu. S. Ilyashenko

In more detail, part a) means that for all elements

ϕ = F1 ◦ exp
[m] ◦ f, F1 ∈ FCm, f ∈ Gm−1,

ψ = F2 ◦ exp
[m] ◦ g, F2 ∈ FCm
+ , g ∈ Gm−1,

where f ≻≻ g in Gm−1, there is a cochain F ∈ FCm such that

F = F1 ◦ exp
[m] ◦ f ◦ (f −1 ◦ ln
[m] +F2 ◦ ρ), ρ = A
−m(g ◦ f −1)

and the equality for F holds on the intersection of some standard domain of class m
with the upper half-plane.

Lemma 1.6 (the fourth shift lemma, axiom SL4n). a) J n−1 ⊂ Gr(id +F n−1
1+ );
b) F n
0(+)g ◦ J n−1 ⊂ F n
0(+)g.
This inclusion holds in an upper half-neighbourhood of the positive semi-axis.

We comment on part b). For all elements

ϕ = F1 ◦ exp
[n] ◦g, F1 ∈ FCn, g ∈ Gn−1, j ∈ J [n−1],

there is a cochain F ∈ FCn
0 such that

F = F1 ◦ exp
[m] ◦g ◦ j ◦ g[−1] ◦ ln
[m]

and the equality for F holds on the intersection of some standard domain of class m
with the upper half-plane.
We omit the analogous comment on part a) in order to avoid repetition.

1.5.7. Weak reality and a lower bound.

Deﬁnition 1.7. A functional cochain is said to be weakly real if the boundary of
the corresponding partition contains the ray (R+, ∞), the domains of the partition
adjacent to R are symmetric to each other with respect to R, and

F u(¯ζ) = F l(ζ).

A composite

ϕ ∈ F k
f , ϕ = F ◦ exp
[k] ◦f, F ∈ FCk, f ∈ Gk−1, k ⩽ n,

is said to be weakly real if F is weakly real.

If we replace the cochain by a holomorphic function (that is, if we assume F u

and F l to be analytic extensions of each other), then the previous deﬁnition simply
means that the function F u ≡ F l is real on R.

Theorem 1.2 (lower bound theorem, LETn). Suppose that m = n − 1 or m = n,
F ∈ FCm, and F is weakly real. Then there is a ν > 0 such that

| Re F | ≻ exp(−νξ) on (R+, ∞).

Finiteness theorems for limit cycles 77

1.5.8. Phragm´en–Lindel¨of theorem for cochains, PLTn. Let S denote the symme-
try operator S : F → SF , SF (ζ) = F (¯ζ), and put IF = F − SF .

Theorem 1.3. Suppose that m = n − 1 or m = n, F ∈ FCm, and F decreases
on (R+, ∞) faster than any exponential:

|F (ξ)| ≺ exp(−νξ) on (R+, ∞) ∀ ν > 0.

Then F u ≡ 0, F l ≡ 0.
The theorem also holds for G = IF for any F ∈ FCm.

1.5.9. Upper bound of the coboundary.

Theorem 1.4. Suppose that 1 < m ⩽ n, F ∈ FCm. Then

|δF | ≺ exp(−νξ) on (R+, ∞) ∀ ν > 0.

Moreover, for any m and g, the space of germs at inﬁnity of the composites in F m
(+)g
is a vector space. By the deﬁnition of F m
(+)g, this is equivalent to saying that FCm is
a vector space.

1.5.10. Induction base: n = 0. The Poincar´e maps of hyperbolic polycycles that
occur at level 0 were described in § 0.3: these are almost-regular germs with non-zero
derivative of the aﬃne part. We recall that the group of such germs is denoted by R.
The subgroup of germs with aﬃne part the identity is denoted by R0. In particular,
G0 = R.
To check the axioms below, we introduce the following sets:

FC0
0 , FC−1
1 , G−1, G−1
rap, G−1±
slow , J −1, G−2.

The elements of FC0
0 are called zero-level cochains. We put

FC0
0 = R, FC−1
1 = ∅, G−1 = Aﬀ .

By deﬁnition of the ‘rap’ subgroup, G−1
rap is the group of all a ∈ Aﬀ for which the
a limit lim(R+,∞)(A
−na)
′, n = 0, exists. Hence,

G−1
rap = Aﬀ, G−1±
slow = ∅.

We must also introduce the relation (k, l) ≺ (m, g) for k ⩽ m ⩽ 0. Since G−1−
slow = ∅,
the relation f ≺≺ g makes no sense in G−1. Thus the relation above may only be
of the form (−1, id) ≺ (0, a), a ∈ Aﬀ .

We put J −1 = G−2 = ∅.
In the terms introduced above at the level n = 0, the shift lemmas and all the
other axioms become trivial. We omit the details.

1.6. The multiplicative and additive decomposition theorems.

Theorem 1.5 (multiplicative decomposition theorem, MDTn).
1
◦. For n > 0 we have Gn = Gn−1 ◦ J n−1 ◦ H n ∩ MR.

78 Yu. S. Ilyashenko

2
◦. Suppose that ∆ is a monodromy transformation of class n or, more generally,
∆ ∈ Gn. Then either ∆ ∈ Gn−1, or for some N ∈ N we have

∆ = g ◦
 N∏

j=1(id +ϕj), (23)

where
g ∈ Gn−1, ϕj ∈ F kj
+fj , n − 1 ⩽ kj ⩽ n, (kj, fj) ≺ (kj+1, fj+1). (24)

Theorem 1.6 (additive decomposition theorem, ADTn). Suppose that ∆ is a non-
identity monodromy transformation of class n or, more generally, ∆ ∈ Gn \ id.
Then the following expansion holds for some N ∈ N:

∆ = a +
 N∑

1 ϕj, a ∈ Aﬀ, ϕj ∈ F kj
+fj , 0 ⩽ kj ⩽ n, (kj, fj) ≺ (kj+1, fj+1),

(25)
where the equality (25) holds on the intersection of some neighbourhood of the
positive semi-axis with the upper half-plane. If a = id, then ϕ1 is weakly real.

Remark 1.2. 1) Theorem MDTn enables us to represent an arbitrary monodromy
transformation ∆ ∈ Gn of class n as a composite:

∆ ∈ Aﬀ ◦J 0 ◦ (H 1 ◦ J 1) ◦ · · · ◦ (H n−1 ◦ J n−1) ◦ H n.

This is done by induction over m < n. For Gn−1, Theorem MDTn−1 is assumed
to be proved. It yields that

Gn−1 = Gn−2 ◦ J n−2 ◦ H n−1 ∩ MR.

Then we argue by inverse induction over m.
The corrections of germs of the class H k ◦ J k decrease at inﬁnity no slower than
exp(− exp
[k] µξ) on (R+, ∞), where µ > 0 depends on the germ.
2) The assertion of Theorem ADTn on the weak reality of the terms in the
expansion of the real correction g − id enables us to get a lower bound for this
correction and prove that it is non-oscillating. This is done in the next subsection.

The additive decomposition theorem together with the lower bound theorem
yields Theorem 0.5.

1.7. Reduction of the ﬁniteness theorem to auxiliary results. Here we
prove the identity theorem for monodromy transformations of class n. We recall its
statement. Let Fix∞ be the set of germs of maps (R+, ∞) → (R+, ∞) with inﬁnite
set of ﬁxed points.

Theorem 1.7. Suppose that ∆ is a monodromy transformation of class n and
∆ ∈ Fix∞. Then ∆ = id. Moreover, the same assertion holds for all ∆ ∈ Gn.

Finiteness theorems for limit cycles 79

Proof. Suppose that ∆ ̸= id. Consider the decomposition (25) in Theorem ADTn.
Its aﬃne term a ∈ Aﬀ tends to plus inﬁnity because its derivative is positive. By
the induction hypothesis, all germs f ∈ Gm, m < n, tend to plus inﬁnity. We will
prove the same assertion for ∆ ∈ Gn. It suﬃces to check that all the terms in (25)
except for the aﬃne one tend to 0 on (R+, ∞). Indeed, in (25),

ϕj = Fj ◦ exp
[kj ] ◦fj, kj ⩽ n, Fj ∈ FCkj
+ , fj ∈ Gkj −1,

and Fj decreases exponentially on (R+, ∞). Hence in (25) we have ϕj → 0 on
(R+, ∞). Therefore ∆ is almost aﬃne:

∆ = a + o(1) on (R+, ∞).

This proves that every germ in Gn tends to inﬁnity on (R+, ∞). We now assume
that ∆ ̸= id and reach a contradiction.
Suppose ﬁrst that a ̸= id. In this case the correction ∆ − id does not vanish
on (R+, ∞) because a − id is bounded away from zero and all other terms tend to
zero on (R+, ∞).
Suppose now that a = id. Let ϕ be the ﬁrst non-zero term after id in the
decomposition (25). Write

ϕ = F ◦ exp
[k] ◦f, F ∈ FCk
+, f ∈ Gk−1.

By Theorem ADTn, F is weakly real. Hence, by Theorem LETk,

| Re F | ≻ exp(−νξ) on (R+, ∞)

for some ν > 0. Any other term ψ in the decomposition (25) of ∆ is of the form

ψ = G ◦ exp
[m] ◦g, G ∈ FCm
+ , g ∈ Gm−1 and (k, f ) ≺ (m, g).

The cochain G is rapidly decreasing by deﬁnition. Hence,

|G| ≺ exp(−εξ) on (R+, ∞)

for some ε > 0.
To compare the terms ϕ and ψ on (R+, ∞), it suﬃces to compare F and
ψ ◦ f −1 ◦ ln
[k] = G ◦ exp
[m−k] A
−kh, where h = g ◦ f −1.
We ﬁrst consider the case when k = m. By assumption, in this case h ∈ Gk−1+
slow .
It follows by deﬁnition that λk(h) = ∞, that is, the germ A
−kh grows faster than
any linear germ on (R+, ∞). Hence the germ G ◦ A
−kh decreases faster than any
exponential. Together with the lower bound for F , this implies that ϕ ≻ Cψ for
any C > 0.
We now consider the case when k < m. Then m − k ⩾ 1. The germ h grows as
a linear function. It is easy to prove that the composite A
−kh grows faster than C ln
for any C > 0. Then exp
[m−k] A
−kh grows faster than any power. Hence we again
have ϕ ≻ Cψ for any C > 0.
It follows that ∆ − id does not oscillate. Hence, in both cases, ∆ /∈ Fix∞,
a contradiction. □

80 Yu. S. Ilyashenko

Thus the ﬁniteness theorem is deduced from the additive decomposition theorem.
The latter will be deduced from axioms in the next subsection.
The same method gives a proof of the following proposition.

Proposition 1.1. The group Gn is ordered by the following relation: g1 ≺ g2 if
and only if g1 − g2 ≺ 0.

We now switch to the proof of the multiplicative and additive decomposition
theorems.

1.8. Proof of the multiplicative and additive decomposition theorems,
MDTn and ADTn. We deduce these theorems from the axioms. Except for the
weak reality of ϕ1, everything will be deduced from the shift lemmas.
The proofs are by induction on m ⩽ n. The induction base (m = 0) is trivial.
The induction step makes use of the assumption that both theorems hold for the
groups Gm, m < n.

1.8.1. The shift–conjugacy principle revisited. Here we prove conjugacy lemmas,
from which MDTn is deduced in the next two subsections. The general idea is that
a shift property entails the corresponding conjugacy property, as shown in the proof
of the following lemma.

Lemma 1.7 (conjugacy lemma 1n, CL1n). Suppose that

m ⩽ n, f, g ∈ Gm−1, ϕ ∈ F m
+f , ψ ∈ F m
+g, f ≺≺ g in Gm−1.

Then Ad(id +ϕ)(id +ψ) ∈ id +F m
+g.

Proof. By Lemma SL3m,

(id +ϕ)
−1 = (id + ̃ϕ), ̃ϕ ∈ F m
+f .

Then there are ̃ψ ∈ F m
g and ̂ψ ∈ F m
g such that the following chain of equalities
(explained below) holds:

(id + ̃ϕ) ◦ (id +ψ) ◦ (id +ϕ) = (id + ̃ϕ + ̃ψ) ◦ (id +ϕ) = id + ̃ψ ◦ (id +ϕ) = (id + ̂ψ).

The ﬁrst equality follows from Lemma SL2m, the third from Lemma SL3m. □

Lemma 1.8 (conjugacy lemma 2n, CL2n).

Ad(J n−1)H n = H n.

Proof. This lemma is proved using the same ideas as in the previous one, only we
refer to Lemma SL4n(b) instead of SL3n. □

Lemma 1.9 (conjugacy lemma 3n, CL3n).

Ad(Gn−1)H n = H n.

Proof. This lemma is proved using the same ideas as before and applying Theo-
rem ADTn−1 to the group Gn−1. □

Finiteness theorems for limit cycles 81

1.8.2. Proof of MDTn 1
◦.

Proof. It suﬃces to prove that

̃Gn = Gr(Gn−1, J n−1, H n) = Gn−1 ◦ J n−1 ◦ H n.

To do this, it suﬃces to establish that

Ad(Gn−1)J n−1 = J n−1, Ad(J n−1)H n = H n, Ad(Gn−1)H n = H n.

The ﬁrst equality is an immediate consequence of the deﬁnition of J n−1. The second
and third equalities follow from Lemmas CL2n and CL3n respectively. □

1.8.3. Proof of MDTn 2
◦. We must prove that if g ∈ Gn (and even if g ∈ ̃Gn),
then (23) and (24) hold.
It follows from MDTn 1◦ that

g = ̃g ◦ j ◦ h, ̃g ∈ Gn−1, j ∈ J n−1, h ∈ H n.

The frequent notation j for an element of J n−1 should not be confused with the
subscript j: which is intended is always clear from the context.
The germs j and h are products of generators of the groups J n−1 and H n:

j = ∏
(id + ̃ϕj), ̃ϕj ∈ F n−1
1+ efj , ̃fj ∈ Gn−2,

h = ∏
(id +ψj), ψj ∈ F n
0+gj , gj ∈ Gn−1.

We claim that all factors in the product j ◦ h can be properly ordered. Indeed,
we ﬁrst assume that there are two factors of the form

(id +ψ) ◦ (id +ϕ), ϕ ∈ F m
+f , ψ ∈ F m
+g, f ≺≺ g in Gm−1, n − 1 ⩽ m ⩽ n.
(26)
This is the wrong order (in the correct order the last factor should go ﬁrst). How-
ever, this product of two factors can be written in the form

(id +ϕ) Ad(id +ϕ)(id +ψ) = (id +ϕ) ◦ (id + ̃ψ), ̃ψ ∈ F m
+g.

This follows from Lemma CL1m for m = n − 1 or m = n. The two factors above
are in the correct order.
We now suppose that in (26) the relation f ≺≺ g in Gm−1 is replaced by f ◦g−1 =
h ∈ Gm−1
rap . Then the product of two factors will be replaced by a single one. This
is done using the ﬁrst and third shift lemmas. Namely,

ϕ ∈ F m
+h◦g = (F m
+h) ◦ g = F m
+ id ◦ g = F m
+g.

The second equality follows from Lemma SL1m. Now ϕ and ψ belong to F m
+g. Since
F m
+g is a vector space, we obtain from Lemma SL3m that

(id +ϕ) ◦ (id +ψ) = id + ̃ϕ, ̃ϕ ∈ F m
+g.

82 Yu. S. Ilyashenko

1.8.4. Proof of ADTn. Modulo the weak reality of the leading terms, Theorem ADTn
is an immediate consequence of MDTn 2◦. The proof is by double induction: on the
depth n of the composite ∆ (exterior induction) and the number N of factors in
the product (23) (interior induction). We shall prove (25) for an arbitrary ∆ ∈ Gn

(and even ∆ ∈ ̃Gn).
Exterior induction base: n = 0. The theorem is trivial in this case.
Exterior induction hypothesis: ADTn−1 holds. In other words, for all ̃g ∈ ̃Gn−1

we have

̃g = a+∑ ̃ϕj, a ∈ Aﬀ, ̃ϕj ∈ F kj
+ efj , 0 ⩽ kj ⩽ n−1, (kj, ̃fj) ≺ (kj+1, ̃fj+1).

Interior induction base: N = 0. In this case the product (23) consists of only
one factor and the theorem follows from the induction hypothesis above.
Interior induction step from N − 1 to N . Suppose that the product (23) consists
of N factors. Then, by the interior induction hypothesis, the product of the ﬁrst
N − 1 factors is written as a sum (25) with 0 ⩽ kj ⩽ n − 1 or 0 ⩽ kj ⩽ n. Consider
the ﬁrst case. The last factor is id +ϕN , where ϕN ∈ F m
+f and f ∈ Gm−1, m = n−1
or m = n. Consider the last case. Let ̃ϕj be the same as ϕj in (25), 0 ⩽ kj ⩽ n − 1,
ϕN ∈ F n
+f . Then ̃ϕ ◦ (id +ϕN ) = ̃ϕj + ψN , ψN ∈ F n
+f by the second shift lemma.
Hence,
(a + ∑ ̃ϕj) ◦ (id +ϕN ) = a + ∑ ̃ϕj + ψ, ̃ϕj ∈ F kj
+fj , ψ ∈ F n
+f ,

0 ⩽ kj ⩽ n − 1, (kj, fj) ≺ (kj+1, fj+1).

This proves Theorem ADTn in the case considered. Other cases are treated in
the same way with minor technical details added.
We now prove the weak reality of the term ϕ1 in (25) in the case when a = id
and ∆ ∈ Gn, that is, ∆ is real on (R+, ∞). The diﬀerence between ̃Gn and Gn is
crucial here.

1.8.5. A criterion for weak reality.

Lemma 1.10. Suppose that m = n − 1 or m = n. A cochain F of class FCm is
weakly real if and only if the imaginary part of at least one component F u or F l

decreases on (R+, ∞) faster than any function of the form exp(−νξ), ν > 0.

Proof. Suﬃciency. In what follows we only need the suﬃciency, so we omit the
proof of necessity. Suppose that | Im F u| ≺ exp(−νξ) on (R+, ∞) for every ν > 0.
Then the same holds for | Im F l| and | Re(F u − F l)| on (R+, ∞) because the
coboundary of F decreases faster than any exponential (see Theorem 1.4, included
in the list of axioms). Recall that we introduced a symmetry operator S : F → SF
by the formula SF (ζ) = F (¯ζ) and put IF = F − SF . A cochain F is weakly
real if and only if IF ≡ 0 on (R+, ∞). Consider the cochain IF = SF − F . It
decreases on (R+, ∞) faster than any exponential exp(−νξ). By the second part
of the Phragm´en–Lindel¨of theorem (see Theorem 1.3), SF − F ≡ 0 on (R+, ∞).
It follows that F is weakly real. □

1.8.6. Conclusion of the proof of the additive decomposition theorem. Suppose
that ∆ ∈ Gn and a = id in the decomposition (25). We must prove that the next

Finiteness theorems for limit cycles 83

term after a (to be denoted by ϕ) in this decomposition is weakly real. Write

ϕ = F ◦ exp
[k] ◦f

for some k ⩽ n, F ∈ FCk, f ∈ Gk−1. Any term ψ after ϕ in the decomposition (25)
is of the form

ψ = G ◦ exp
[m] ◦ ̃f , G ∈ FCm
+ , ̃f ∈ Gm−1, (k, f ) ≺ (m, ̃f ).

It decreases on (R+, ∞) faster than ϕ. This was shown in § 1.7. We can show in
the same way that the composite ψ ◦ f −1 ◦ ln
[k] decreases on (R+, ∞) faster than
any exponential.
On the other hand, the sum (25) is real on the real axis because ∆ ∈ Gn. Hence,

Im F = − ∑ Im ψj ◦ f −1 ◦ ln
[k] .

The right-hand side decreases on (R+, ∞) faster than any exponential. By the
criterion proved above, F (and hence ϕ) is weakly real.
This completes the proof of Theorem ADTn.

1.9. Strategy II: further proof of the ﬁniteness theorem. The ﬁrst part
of § 1 is over. The second part starts with a general preview of the remaining
elements of the proof. They are illustrated by the diagram shown in Fig. 3.

Figure 3

84 Yu. S. Ilyashenko

The blocks contain the names of the major auxiliary assertions and of the ﬁnite-
ness theorem itself. The arrows, as usual, stand for implications. Solid arrows show
implications that have already been proved. Dashed arrows show implications to
be proved. There are no arrows entering the lower left block. It is included in
the induction hypothesis. The induction step (proof of the properties of admissible
germs of class n + 1) relies upon all the previous results and is carried out in § 5.
It appears in the upper box.
The ﬁrst step is to build a model for the axioms above. This is done in the second
part of this section. At the same time we deﬁne the admissible germs mentioned
in the South-West box. Cochains of classes FCn
0 and FCn−1
1 are characterized by
two major properties: regularity and expandability. These properties correspond
to the two upper boxes in the South-East corner of the scheme. The Phragm´en–
Lindel¨of property relies only upon the regularity while the lower bound requires
both regularity and expandability. Proofs of the shift lemmas and the Phragm´en–
Lindel¨of theorem make use of some properties of admissible germs. The induction
hypothesis is that these properties hold for all admissible germs of class n. For this
reason, no arrow enters the South-West box.
To complete the induction step, we prove the required properties for admissible
germs of class n +1. This is done in § 5. The proof makes use of all previous results.
This is shown by the broad arrow on the top of Fig. 3.
The shift lemmas are proved in § 3 (regularity part) and § 4 (expandability part).
The Phragm´en–Lindel¨of theorem is proved in § 2.
We turn to the explicit deﬁnitions of cochains of class n, that is, to constructing
a model for the axioms above.

1.10. Admissible germs of diﬀeomorphisms.

Deﬁnition 1.8. Let Ω be a set of standard domains. The germ of a diﬀeomorphism
σR : (R+, ∞) → (R+, ∞) is said to be admissible of class Ω (or Ω-admissible) if the
following conditions hold.
1) The inverse germ ρ admits a biholomorphic extension to some standard
domain, and for every standard domain Ω ∈ Ω there is a standard domain ̃Ω ∈ Ω
such that ρ maps ̃Ω biholomorphically to Ω.
2) The derivative ρ′ is bounded on ̃Ω.
3) There is a µ > 0 such that Re ρ < µξ on ̃Ω.
4) For every ν > 0 we have exp Re ρ ≻ νξ on ̃Ω.

The extension of the germ σR to the domain ρ̃Ω is denoted by σ and is also called
an Ω-admissible germ. When speaking of an admissible (instead of Ω-admissible)
germ, we mean by deﬁnition that Ω is the set of all standard domains.

Example 1.2. The germs µζ, ζ µ for µ > 1, exp µζ for µ ∈ [0, 1) are admissible,
and the germ exp ζ is not (requirement 4 of Deﬁnition 1.8 does not hold).

1.11. Regular cochains. Two map-cochains or two functional cochains are said
to be equivalent if there is a standard domain on which they are deﬁned and coin-
cide. An equivalence class of map-cochains (or functional cochains) is called a germ
of a map-cochain (or of a functional cochain). By deﬁnition, representatives of
a germ are considered in standard domains.

Finiteness theorems for limit cycles 85

1.11.1. Regular partitions. We ﬁrst deﬁne regular partitions of standard domains.
Choose and ﬁx a subset Ω in the set of all standard domains.

Deﬁnition 1.9. Let Ξ be a partition of a standard domain Ω ∈ Ω. The image
of Ξ under the action of an admissible germ of a diﬀeomorphism σ of class Ω is
a partition σ∗Ξ of a standard domain ̃Ω ∈ Ω such that a representative of the germ
ρ = σ−1 is deﬁned and biholomorphic on ̃Ω and maps ̃Ω to Ω. The domains of the
partition σ∗Ξ are deﬁned by the equalities

(σ∗Ξ)j = σ(Ξj ∩ ρ̃Ω),

where Ξj are the domains of the partition Ξ. By deﬁnition, the domain (σ∗Ξ)j
corresponds to the domain Ξj.
 Figure 4

Example 1.3. Pictured in Fig. 4 are the images of the standard partition under
the action of the diﬀeomorphisms exp µζ, µ ∈ (0, 1); ζ µ, µ > 1; µζ, µ > 0. The
domains of the image partition are ordinary sectors in the ﬁrst case, ‘parabolic
sectors’ in the second, and horizontal half-strips in the third.

Consider an arbitrary domain Ω and a partition Σ of Ω. A boundary curve of
a domain of this partition is said to be exterior if it is contained in ∂Ω, and interior
otherwise. The union of all interior boundary curves of Σ is called the boundary
of Σ and is denoted by ∂Σ. We recall that Ξst stands for the standard partition
(see Deﬁnition 0.9).

Deﬁnition 1.10. Consider a tuple

σ = (σ1, . . . , σN ) (27)

of admissible germs. A regular partition of a standard domain Ω is deﬁned as
a product
 Ξ =
 N∏

1 σj∗Ξst. (28)

This partition is called a partition of type σ and numerical type N .

86 Yu. S. Ilyashenko

We recall that the product of partitions is deﬁned in § 1.5.1.
Along with ε-neighbourhoods of domains of the partition (28), it is convenient
to consider their generalized ε-neighbourhoods, which are deﬁned as follows.

Deﬁnition 1.11. Let (28) be a regular partition of type σ (see (27)) of a standard
domain Ω, and let ̃Ω be another standard domain such that for all σj ∈ σ we have
ρj ̃Ω ⊂ Ω, where ρj = σ−1
j . We denote the domains of the standard partition Ξst
of Ω by Ξj and consider a domain

U = ̃Ω
 N⋂

1 σj(Ξlj )

of the partition (28) of ̃Ω. Here the lj are chosen in such a way that U ̸= ∅.
Let A
ε stand for the ε-neighbourhood of a set A in C. Then the generalized
ε-neighbourhood U (ε) of the domain U is deﬁned as follows:

U (ε) = ̃Ωε N⋂

1 σj(Ξ
ε
lj ).

Deﬁnition 1.12. For every boundary curve of the partition (28), which is a com-
mon boundary of two domains of the partition, the generalized ε-neighbourhood is
deﬁned as the intersection of the generalized ε-neighbourhoods of these domains of
the partition. The union of all such neighbourhoods is denoted by ∂Ξ
(ε).

Deﬁnition 1.13. Every regular partition of type σ generates a family of func-
tional cochains deﬁned on the generalized ε-neighbourhoods of the boundary of the
partition. These cochains are called rigging cochains and are deﬁned as follows.
The function of the cochain given in a neighbourhood of a boundary curve L is
denoted by mσ,C,ε,L and is given by

mσ,C,ε,L = ∑ exp(−C exp Re ρj), ρj = σ−1
j , (29)

where the sum is taken over those j for which L is an interior boundary curve of the
partition σj∗Ξst. The cochain with components (29) is denoted by mσ,C,ε. A par-
tition endowed with the set of rigging cochains (that is, cochains of the form (29)
for all positive C, ε) is said to be rigged.

Remark 1.3. The ray (R+, ∞) is a boundary line of the partition σj∗Ξst for all j.
Hence a rigging cochain on this ray is equal to the sum (29) over all j = 1, . . . , N .

1.12. Regular cochains of type D. Here is the main deﬁnition of this section.
Its requirements are named, and their names follow their numbers. As always,
ξ = Re ζ, ζ ∈ C+.

Deﬁnition 1.14. An ε-extendible germ of a regular cochain of class Ω is a germ
with a representative (called a regular functional cochain) deﬁned in an ε-
neighbourhood of a standard domain Ω of class Ω (this domain depends on the
germ) with the following properties.
1) (Partition). The corresponding partition is a regular partition of type σ =
(σ1, . . . , σN ), the germs σj are admissible germs of class Ω, and the partition is
rigged (the last condition holds automatically).

Finiteness theorems for limit cycles 87

2) (Expandability). For small ε all functions forming the cochain extend holo-
morphically to generalized ε-neighbourhoods of the corresponding domains of the
partition.
3) (Growth). The modulus of the cochain is bounded above in Ω by the function
exp νξ for some ν ∈ R depending on the cochain. If ν can be chosen negative in
this bound, then the cochain is said to be rapidly decreasing. If the modulus of the
cochain is bounded above by the function C|ζ|
−5 for some C > 0, then the cochain
is said to be weakly decreasing.
4) (Coboundary). The functions forming the coboundary of the cochain admit
an analytic extension to the generalized ε-neighbourhoods of boundary curves of
the partition, and their modules are bounded above in these neighbourhoods by the
corresponding functions of the rigging cochain mσ,C,ε for some constants C > 0
and ε > 0 depending on the cochain.

The set of all regular functional cochains is denoted by FCreg, and the set
of all rapidly decreasing regular functional cochains by FC+
reg (FC for functional
cochains).

Deﬁnition 1.15. An ε-extendible germ of a regular map-cochain is a germ whose
correction is an ε-extendible germ of a rapidly decreasing regular functional cochain.
We similarly deﬁne an ε-extendible germ of a weakly regular map-cochain: here the
correction must decrease not rapidly, but weakly. The sets of all regular and weakly
regular map-cochains are denoted by MCreg and MCwr (MC for map-cochains,
wr for weakly regular).

Deﬁnition 1.16. Let D be an arbitrary set of germs of admissible diﬀeomor-
phisms. The germ of a functional cochain or map-cochain is said to be regular
of type D if the corresponding partition is of type σ = (σ1, . . . , σN ), where σj ∈ D.
The sets of such germs are denoted by FCreg(D), MCreg(D). The sets of germs of
rapidly or weakly decreasing functional cochains of class D and the set of weakly
regular map-cochains of class D are denoted by FC+
reg(D), FCwr(D), MCwr(D)
respectively.

1.13. Regular cochains in non-standard domains. Regular functional
cochains satisfy the Phragm´en–Lindel¨of theorem provided that they admit spe-
cial complex extensions called realizations. These extensions are deﬁned here and
in the next subsection.
Consider any connected domain ̂Ω lying in some standard domain Ω of class Ω
and containing (R+, ∞). Let ̂Ω(ε) be any increasing family of domains:

̂Ω(ε) ⊂ ̂Ω(ε
′) for ε < ε
′, ̂Ω(0) = ̂Ω.

Deﬁnition 1.17. A partition (28) of type (27) of the domain ̂Ω is the intersection
of the partition (28) of Ω with ̂Ω. More precisely, any domain W of this partition
is the intersection of some domain U of the partition (28) with ̂Ω. A generalized
ε-neighbourhood of W is the intersection

W (ε) = ̂Ω(ε) ∩ U (ε).

88 Yu. S. Ilyashenko

Generalized ε-neighbourhoods of the boundary curves of the partition are deﬁned
in the same way as above. Rigging cochains for the partition (28) of ̂Ω are deﬁned by
the formula (29) with the same summation rule.

After that, the set of regular cochains of type (27) is well deﬁned in every
domain ̂Ω described above. Only the expandability property should be modiﬁed:
generalized ε-neighbourhoods are understood in the sense of Deﬁnition 1.17.
An important example is given by realizations of regular cochains, which are
deﬁned in the next subsection.

1.14. Realizations. Before giving general deﬁnitions, we start with some exam-
ples.
Consider two cochains F, G ∈ N C. By deﬁnition, both correspond to the stan-
dard partition. We also consider aﬃne maps a : ζ ↦→ ν−1
1 ζ, b : ζ ↦→ ν−1
2 ζ, ν1 > ν2,
and cochains ̃F = Ad(a)F , ̃G = Ad(b)G corresponding to the partitions ν1∗Ξst,
ν2∗Ξst respectively. Their sum H = ̃F + ̃G is a cochain of type (a
−1, b−1) = (ν1, ν2),
where νj stands for the map ζ ↦→ νjζ. The coboundary δH is estimated by the
rigging cochain
 m = exp(−C exp ν−1
1 ξ) + exp(−C1 exp ν−1
2 ξ)

in a neighbourhood of the boundary of the partition Ξ = ν1∗Ξst · ν2∗Ξst. The ﬁrst
term in the expression for m dominates the second:

m ≺ exp(−C ′ exp ν−1
1 ζ)

for any C ′ > C. We now consider the cochain

H1 = Ad(a)F u + G on ν1Πmain.

The ﬁrst term is holomorphic on Ω(1) = ν1Πmain. Hence the cochain H1 corresponds
to the partition ν2∗Ξst of Ω(1). In a neighbourhood of the boundary of this partition
we have δH1(ζ) ≺ exp(−C1 exp ν−1
2 ξ).

The coboundary of H1 is estimated by a rigging cochain that decreases faster than
the rigging cochain estimating the coboundary of H.
The cochains H and H1 coincide on Ω(1) ∩ {η > 0}. In what follows, H1 is
called a 1-realization of H. The advantage of this realization is that its coboundary
is estimated by a rigging cochain that decreases faster than the rigging cochain
estimating the coboundary of H.
We now consider the sum

H1,1 = Ad(a)F u + Ad(b)Gl.

This sum is a holomorphic function on the domain Ω1,1 = ν−1
2 Π
+
main (and hence
has no coboundary at all). It is coincides with H1 on Ω1,1 ∩ {η < 0}.
The cochains H1 and H1,1 are examples of what will be called 1- and (1, 1)-
realizations of H. Realizations are used repeatedly, in particular, in the proof of
the Phragm´en–Lindel¨of theorem. We pass to general deﬁnitions.

Finiteness theorems for limit cycles 89

Deﬁnition 1.18. A class Ω of standard domains is said to be proper if the following
conditions hold.
1) For every C > 0 an arbitrary domain of class Ω contains a domain of the same
class whose distance to the boundary of the ﬁrst domain is no smaller than C.
2) The intersection of any two domains of class Ω contains a domain of the same
class.

Consider a proper class Ω of standard domains (see Deﬁnition 1.18) and a fam-
ily D of Ω-admissible germs.

Deﬁnition 1.19. The admissible germs σ1 and σ2 are said to be weakly equivalent,
σ1 w
∼ σ2, if their composition quotient σ−1
1 ◦σ2 has a bounded correction on (R+, ∞).

We put
 Πmain = Π∗ ∪ Π1, Π
+
main = Π∗ ∪ Π0, (30)

Π
(ε)
main = Π
(ε)
∗ ∪ Π
ε
1, Π
+(ε)
main = Π
(ε)
∗ ∪ Π
ε
0. (31)

Recall that Πε
j is the ε-neighbourhood of Πj, the notation Π∗ was deﬁned in (4),
and Π0, Π1 are the strips of the standard partition adjacent to (R+, ∞) from
above and below respectively.
Suppose that the class D has the following properties.
• Ordering. For any two distinct germs σ1, σ2 ∈ D the diﬀerence σ1 − σ2 does
not vanish on (R+, ∞). We introduce an order relation

σ1 ≻ σ2 ⇐⇒ σ1 − σ2 ≻ 0 ⇐⇒ σ1 − σ2 > 0 on (R+, ∞).

• Monotonicity.
1) If σ1 ≻ σ2 ∈ D and the germs σ1, σ2 are not weakly equivalent, then

(σ1Πmain ∩ Ω, ∞) ⊃ (σ2Πmain ∩ Ω, ∞). (32)

2) If the germs σ1, σ2 ∈ D are weakly equivalent, then they can be renumbered
in such a way that for all ε > δ > 0 we have

(σ1Π
(ε)
main ∩ Ω, ∞) ⊃ (σ2Π
(δ)
main ∩ Ω, ∞). (33)

Deﬁnition 1.20. Suppose that either σ1, σ2 are not weakly equivalent and
σ1 ≻ σ2, or they are weakly equivalent and (33) holds. Then we write σ1 ◃ σ2.

By symmetry with respect to the real axis it follows from (32), (33) that

(σ1Π
+
main ∩ Ω, ∞) ⊃ (σ2Π
+
main ∩ Ω, ∞), (34)

(σ1Π
+(ε)
main ∩ Ω, ∞) ⊃ (σ2Π
+(δ)
main ∩ Ω, ∞) (35)

for all ε, δ with 1 > ε > δ > 0.
Every ﬁnite subset σ of a class D possessing the properties of ordering and
monotonicity can be written in ordered form:

σ = (σ1, . . . , σN ), σ1 ◃ σ2 ◃ · · · ◃ σN . (36)

90 Yu. S. Ilyashenko

We now deﬁne domains of realizations of cochains of class (36) as well as their
generalized ε-neighbourhoods. Deﬁne the following domains of types (σ, k), (σ, k+)
and (σ, k, l) for 0 < k ⩽ N , 0 < l ⩽ N − k:

Ωσ,k = σkΠmain ∩ Ω, Ω+
σ,k = σkΠ
+
main ∩ Ω, Ωσ,k,l = Ωσ,k ∩ Ω+
σ,k+l. (37)

Generalized ε-neighbourhoods of these domains are deﬁned as

Ω(ε)
σ,k = σkΠ
(ε)
main ∩ Ωε, Ω+(ε)
σ,k = σkΠ
+(ε)
main ∩ Ωε, Ω(ε)
σ,k,l = Ω
(ε)
σ,k ∩ Ω+(ε)
σ,k+l, (38)

where Π
(ε)
main, Π+(ε)
main are the same as in (31).
Suppose that no two germs in (36) are weakly equivalent. Then the smaller j is,
the larger σj is (it grows at inﬁnity faster than all subsequent ones). The larger the
germ σj is, the larger the domain Ωσ,j is. If the weak equivalence of some germs
σj, σj+1 is admitted, then (33) holds. In both cases, if j < k, then for all ε > δ > 0
we have (Ω(δ)
σ,k, ∞) ⊂ (Ω(ε)
σ,j, ∞), (Ω+(δ)
σ,k , ∞) ⊂ (Ω+(ε)
σ,j , ∞). (39)

Moreover, if m > l, then
 (Ω(δ)
σ,k,m, ∞) ⊂ (Ω(ε)
σ,k,l, ∞). (40)

Note that the domains Ωσ,k and Ω+
σ,k are symmetrically placed with respect
to (R+, ∞).

Deﬁnition 1.21. Partitions of types (σ, k), (σ, k+), (σ, k, l) for tuples σ of the
form (36) are partitions of the form
 N∏

j=a σj∗Ξst (41)

of the domain Ω, where a = k + 1, k + 1, k + l + 1 and Ω = Ωσ,k, Ω+
σ,k, Ωσ,k,l
respectively.

By the monotonicity relations (39) and (40), partitions of type (σ, k) possess the
following key property: they coincide with partitions of type σ of the domain Ωσ,k.
Namely, for every j ⩽ k the partition of type σ has only one interior boundary line
that belongs to σj∂Ξst: this is (R+, ∞). Indeed, even when j = k the line σk(η = π)
is contained in the upper boundary of Ωσ,k. When j ̸= 0, 1 the lines σk(η = πj) are
disjoint from Ωσ,k.
The rigging cochains mσ and mσ,k corresponding to partitions of type σ or (σ, k)
of the domain Ωσ,k coincide everywhere except for a generalized ε-neighbourhood of
(R+, ∞). On (R+, ∞) we have

mσ =
 N∑

j=1 exp(−C exp ρj), mσ,k =
 N∑

j=k+1 exp(−C exp ρj). (42)

Finiteness theorems for limit cycles 91

By the ordering property of the germs σj in the tuple σ, the rigging cochain mσ
on (R+, ∞) is characterized by its ﬁrst term:

exp(−C exp ρ1) ≻ mσ|(R+,∞) ≻ exp(−C ′ exp ρ1) (43)

for some C ′ > C. Indeed, let σ1 be weakly equivalent to σj. Then σ−1
1 ◦ σj = id +Φ,
where Φ is bounded on (R+, ∞). Suppose that |Φ| < D on (R+, ∞). Then

exp(−C exp ρ1 ◦ ρ−1
j (ξ)) = exp(−C exp σ−1
1 ◦ σj(ξ)) = exp(−C exp(ξ + Φ(ξ)))

≻ exp(−(C exp(−D)) exp ξ)

and exp(−C exp ρ1) ≻ exp(−(C exp(−D)) exp ρj).

If σ1 is not weakly equivalent to σj and σ1 ≻ σj, then the same calculation yields
that exp(−C exp ρj) = o(1) exp(−C exp ρ1).

This proves (43).
The same argument yields the following bounds on (R+, ∞):

exp(−C exp ρk+1) ≻ mσ,k ≻ exp(−C ′ exp ρk+1). (44)

Hence the regular cochains corresponding to partitions of type (σ, k) on Ωσ,k,
have ‘smaller coboundaries’ and are ‘more holomorphic’ than the restrictions of
cochains of type σ on Ωσ,k.
This motivates the following deﬁnition based on Deﬁnition 1.17 in § 1.13.

Deﬁnition 1.22. Let σ be as in (36), 0 < k ⩽ N , 0 < l ⩽ N − k. A regular
cochain of type (σ, k) (resp. (σ, k+), (σ, k, l)) is a regular cochain that is deﬁned
on the corresponding domain (37) and corresponds to a partition of type (σ, k)
(resp. (σ, k+), (σ, k, l)).

Deﬁnition 1.23. Let F be a regular functional cochain on a standard domain Ω,
0 < k ⩽ N , 0 < l ⩽ N − k. A regular cochain F(k) (resp. F +
(k) or F(k,l)) is called
a k-realization (resp. k+- or (k, l)-realization) of F is the following conditions hold.
• It is of type (σ, k) (resp. (σ, k+) or (σ, k, l)).
• It coincides with F on the intersection of its domain with the upper half-plane:

F = F(k) on σkΠ1 ∩ Ω (45)

or, respectively, it coincides with F on the intersection of its domain with the lower
half-plane: F = F +
(k) on σkΠ0 ∩ Ω (46)

or, respectively, it coincides with F(k) on the intersection of its domain with the
lower half-plane: F(k,l) = F(k) on Ωσ,k,l ∩ {η < 0}. (47)

The cochain F is called its own 0-realization and is denoted by F(0): F = F(0).

92 Yu. S. Ilyashenko

Remark 1.4. (k, l)-realizations are deﬁned only for cochains of numerical type N > 1.

Deﬁnition 1.24. A regular cochain of type (36) is said to be
• weakly realizable if it has all k-realizations for 0 < k ⩽ N ;
• almost realizable if it has all k- and k+-realizations for 0 < k ⩽ N ;
• absolutely realizable if it has numerical type N > 1 and possesses all k-, k+-
and (k, l)-realizations, or if it has numerical type 1 and is almost realizable, or if
it is a holomorphic function.

To clarify the deﬁnitions that follow, we recall that Πmain = Π1 ∪ Π∗, Π
+
main =
Π0 ∪ Π∗, and the intersection of Ωσ,k (see (37)) with the upper half-plane is equal
to σkΠ1 ∩ Ω. Similarly, Ω+
σ,k ∩ {η < 0} = σkΠ0 ∩ Ω.

Example 1.4. Normalizing cochains are absolutely realizable. Indeed, they are
cochains of numerical type 1, whence their absolute realizability is equivalent to
almost realizability. The latter requires the existence of two realizations: F(1) of
type 1 and F +
(1) of type 1+. These realizations exist by the supplement to the
sectorial normalization theorem and are holomorphic functions:

F(1) = F u, F +
(1) = F l.

This example is in a sense the main one.
The need for realizations is motivated by the following argument (among others).
In order to satisfy the Phragm´en–Lindel¨of theorem, a regular cochain F must be
weakly realizable, that is, all k-realizations are needed. For the cochain SF to
satisfy the Phragm´en–Lindel¨of theorem, it must also be weakly realizable. But
we have (SF )k = S(F +
k ).

It follows that F must be almost realizable. Absolute realizability will be moti-
vated in the second part of this paper where we discuss the substitution of slowly
decreasing germs into functional cochains.

1.15. Standard domains, admissible germs and regular cochains of
class n. In this subsection we deﬁne the regularity properties required by cochains
of class n. Namely, we deﬁne regular cochains of class n and type 0 or 1. In the
next subsection we deﬁne the expandability properties and thus complete the con-
struction of the model for the axioms stated above.

1.15.1. Motivations: regularity. Below we deﬁne standard domains and admissible
germs of class n. The notion of a standard domain depends on n because of the
following requirement: for every germ inverse to an admissible germ of class n and
every domain of class n there must exist another domain of this class which is
mapped by this germ to the given domain. Thus the class of domains must be
adjusted to the class of germs.
Shift lemmas imply that the complexity of the structure of cochains occurring
at level m increases with m. Thus the class of admissible germs used in the deﬁ-
nition of cochains of class m must depend on m. A more careful analysis of these
lemmas gives rise to the sets Dn
0 and Dn−1
1 of admissible germs of class n, which
are deﬁned below.
 Finiteness theorems for limit cycles 93

1.15.2. Standard domains of class n. We recall that a standard domain Ωm,ε,C
of class m corresponding to the constants ε > 0 and C > 0 is deﬁned by the
formulae (13) and (14). The properties of these domains were discussed in § 1.5.2.

1.15.3. Admissible germs and regular cochains of class n. We shall deﬁne two sets
of Ωn-admissible and Ωn−1-admissible germs of class n and types 0 and 1 respec-
tively: Dn
0 and Dn−1
1 . Thus we encounter the following sets of regular cochains of
class n: FC n
0 reg = FCreg(Dn
0 ), FC n−1
1 reg = FCreg(Dn−1
1 ).

When m < n the deﬁnitions are the same with n replaced by m. The set of regular
cochains of class 1 and type 1 is especially simple. We describe it now.

Deﬁnition 1.25. Regular sectorial cochains are cochains of class FCreg(D0), where

D0 = {exp µζ | µ ∈ (0, 1)}.

The set of regular cochains of class 1 and type 0 is also simple. These cochains
are even said to be simple.

Deﬁnition 1.26. Regular simple cochains are cochains of class FCreg(D1), where

D1 = {νζ | ν ∈ R+}.

We now deﬁne the classes Dn
0 and Dn−1
1 .

Deﬁnition 1.27. The set of Ωn-admissible germs of class n and type 0 is deﬁned
as Dn
0 = {exp ◦A
1−ng | g ∈ Gn−1−
slow }.

Example 1.5. The set D0
1 is equivalent to D0 in the following sense: the set
FCreg(D1
0) of regular cochains of class 1 and type 1 coincides with the set of regular
sectorial cochains. This means that the same tuple of components corresponds
simultaneously to the slightly diﬀerent partitions of types D0
1 and D0 and satisﬁes
all the requirements of Deﬁnition 1.14 for both partitions.

The deﬁnition of Dn−1
1 is more involved. We ﬁrst write Dn−1
∗ for the set

Dn−1
∗ = Dn−1+
slow ∪ Dn−1
rap ,

Dn−1+
slow = {A
1−ng | g ∈ Gn−2+
slow }, Dn−1
rap = {A
1−ng | g ∈ Gn−2
rap }.

Let TO
0 be the set of those maps of class TO for which the aﬃne factor in the
decomposition (10) is the identity:

TO
0 = (H ◦ exp ◦R0 ◦ N C ∩ MR).

For every n ⩾ 3 we consider the set

L
n−1 = {A
1−ng | g ∈ Gn−1, g = Ad(f )A
n−2h,

h ∈ ln ◦TO
0, f ∈ Gn−2, λn−2(f ) = 0}.

Note that this formula makes no sense when n ⩽ 2. Indeed, if n ⩽ 2, then the set
{f ∈ Gn−2, λn−2(f ) = 0} is empty. When n ⩽ 3 we put L
n−1 = {id}.

94 Yu. S. Ilyashenko

Deﬁnition 1.28. The set of Ωn−1-admissible germs of class n and type 1 is
deﬁned as Dn−1
1 = Dn−1
0 ∪ Dn−1
∗ ◦ L
n−1.

Example 1.6. The set D0
1 is equivalent to D1 in the following sense: the set
FCreg(D0
1) of regular cochains of class 1 and type 1 coincides with the set of regular
simple cochains.

In order to consider the classes FCreg for D = Dn
0 or Dn−1
1 , we need the following
lemma.

Lemma 1.11. 1) The classes Dn
0 and Dn−1
1 consist of Ωn-admissible and Ωn−1-
admissible germs respectively.
2) Each of the classes Dn
0 , Dn−1
1 possesses the ordering and monotonicity prop-
erties introduced in § 1.14.

The sets Dm
0 , Dm−1
1 are deﬁned for every m > 0, m < n in the same way as the
sets Dn
0 , Dn−1
1 , with n replaced by m. Lemma 1.11 holds for the classes Dm
0 , Dm−1
1 .
This is proved by induction on m.
Indeed, when m = 1 the lemma is obvious. When 1 < m ⩽ n we include this
lemma in the induction hypothesis as a property of the germs of classes Dm
0 , Dm−1
1 ,
m ⩽ n. For the classes Dn+1
0 and Dn
1 , the lemma will be proved schematically in § 5.
This induction step (from n to n + 1) completes the proof of the lemma.
Lemma 1.11 enables us to deﬁne weakly realizable, almost realizable, and abso-
lutely realizable cochains of classes Dn
0 , Dn−1
1 .

Deﬁnition 1.29. Regular cochains of class n and type 0 or 1 are absolutely real-
izable cochains of the classes FCreg(Dn
0 ) and FCreg(Dn−1
1 ) respectively.

This completes the regularity part of the deﬁnition. The expandability part is
given in the next subsection.

1.16. Superexact asymptotic series. In §§ 1.10–1.15 we completed the ﬁrst
part of the construction of the model for the axioms: the regularity requirements
were described. In this subsection we complete the second part of the construction:
the expandability requirements are given.

1.16.1. A heuristic description of superexact asymptotic series. We use the acronym
STAR for superexact asymptotic series. This is an abbreviation of the Russian term
‘SverkhTochnye Asimptoticheskie Ryady’.
Theorem 0.5 implies that ordinary asymptotic series are insuﬃcient for the
unique determination of monodromy transformations. We need superexact asymp-
totic series, which are constructed using the following idea.
Consider germs of maps on (R+, ∞) written in the logarithmic chart. Suppose
we are investigating a set M1 of germs of maps (R+, ∞) → (R+, ∞). Each of these
germs can be expanded in an asymptotic series whose partial sums approximate
the germ within an arbitrary exponential accuracy, for example, in an exponential
Dulac series. Such series will be called ordinary series. However, it is desirable to
expand the germs studied in series whose terms have (not only simple exponential
but) double exponential order of smallness. At ﬁrst glance, this is impossible: an

Finiteness theorems for limit cycles 95

arbitrary remainder term of an ordinary series has a simple exponential order of
smallness and it seems meaningless to take into account terms that decrease as
double exponentials.
This diﬃculty can be overcome as follows. We introduce an intermediate class
of functions M0, whose elements are expanded in ordinary series and are uniquely
determined by them, that is, the zero series corresponds to the zero germ. For
example, M0 can be taken to be the set of almost-regular germs written in the
logarithmic chart. Then the germs of class M1 are expanded in series of decreasing
double exponentials, and the coeﬃcients of these series are no longer numbers but
functions in M0. The simplest example of a STAR is of the form

Σ = a0(ξ) +
 ∞∑

j=1 aj(ξ) exp(−νj exp ξ), aj ∈ M0, 0 < νj ↗ ∞. (48)

A series Σ is said to be asymptotic for a germ f if, for every ν > 0, the
series has a partial sum that approximates f on (R+, ∞) within the accuracy
o(exp(−ν exp ξ)). All information about the expansion of f in an ordinary series is
included in the free term of the superexact series: the ordinary series for f and a0
coincide.
We show by a simple example how to use superexact series to prove a simpliﬁed
version of the identity theorem. Assume in addition to the preceding that the
class M0 (resp. M1) contains the germs of the functions 0 and ξ, and that all
germs in this class can be expanded in exponential Dulac series (resp. STAR of
the form (48)) and are uniquely determined by these series. Then the following
theorem holds.

Theorem 1.8. f ∈ M1 ∩ Fix∞ ⇒ f = id.

Proof. The theorem is proved according to the same scheme as the identity theo-
rem 1.7. Suppose that the theorem is false: there is an f ∈ M1 ∩ Fix∞, f ̸= id. Let
(48) be the STAR for f . We ﬁrst assume that a0 ̸= id. Then the corresponding
exponential Dulac series ̂a0 − id is non-zero. Hence the germ of a0 − id is equal
to the leading term of its exponential Dulac series multiplied by 1 + o(1), where
o(1) → 0 on (R+, ∞). In particular, for some ν > 0 we have

|a0 − id | ≻ exp(−νξ).

Note that every term in the series (48) is small in comparison with the previous one.
Indeed, the coeﬃcients are almost regular germs, which can be estimated from above
by an increasing simple exponential and from below by a decreasing one. Since the
double exponential ‘beats’ the simple one, it follows from the expandability of f in
a STAR (48) that

|f − id | ⩾ |a0 − id | + (|a1| exp(−ν1 exp ξ)
)(1 + o(1)) ≻ exp(−νξ)(1 + o(1)).

Hence f − id ̸= 0 for large ξ and, therefore, f /∈ Fix∞, a contradiction.
We now assume that a0 = id, f ̸= id. Then the STAR (48) is diﬀerent from id;
otherwise we would have f = id since germs in M1 are uniquely determined by

96 Yu. S. Ilyashenko

their series. We obtain from the deﬁnition of expandability that

f − id = (a1 exp(−ν1 exp ξ)
)(1 + o(1)).

Arguing as in the preceding paragraph, we see that a1 ̸= 0 for large ξ. Two other
factors in the formula for f − id also do not vanish near inﬁnity. Hence f /∈ Fix∞,
a contradiction. □

Theorem 0.5 shows that the actual asymptotic series for monodromy transfor-
mations of class n must be even more complicated.
We now pass to the deﬁnition of superexact asymptotic series of class n.

1.16.2. Survey of deﬁnitions to follow. Cochains of class n can be decomposed in
STAR-n. The set of all STAR corresponding to FCn−1
1 (resp. FCn
0 ) is denoted
by E n−1
1 (resp. E n
0 ). All series and cochains in these sets have not only class n, but
also rank r ∈ Z
+ ranging from 0 to inﬁnity. The corresponding classes are denoted
by E n−1,r
1 , FCn−1,r
1 , E n,r
0 , FCn,r
0 :

E n−1
1 =
 ∞⋃

0 E n−1,r
0 , FCn−1
1 =
 ∞⋃

0 FCn−1,r
0 , (49)

E n
0 =
 ∞⋃

0 E n,r
0 , FCn
0 =
 ∞⋃

0 FCn,r
0 . (50)

The deﬁnition of these classes is by induction on n (exterior induction) and r
(interior induction). Base of the exterior induction is the deﬁnition of series and
cochains of classes m = 0 and m = 1. The step is made from n − 1 to n. The
exterior induction hypothesis is that all the sets E m
1 , FCm
1 are deﬁned for m < n − 1
and the sets E m
0 , FCm
0 are deﬁned for m < n.
For series and cochains of class n and type 1, the step of the interior induction is
done as follows. Suppose that the sets E n−1,r
1 , FCn−1,r
1 have already been deﬁned.
Using this, we deﬁne the sets E n−1,r+1
1 , FCn−1,r+1
1 and then the sets (49).
Having done this, we pass to the deﬁnition of series and cochains of class n and
type 0: E n,r
0 , FCn,r
0 . They are also deﬁned by induction on r, which results in (50).
In what follows all STAR are of the form

Σ = ∑ aj exp ej, (51)

where the ej and aj are called exponents and coeﬃcients respectively. The principal
coeﬃcients ν(ej), which are deﬁned below, tend to −∞. To deﬁne a new class of
series, we must deﬁne the class E of their exponents and the class K of coeﬃcients.
Subscripts and superscripts are added to the symbols E and K to indicate particular
classes, for example, Kn−1,r
1 .
Very roughly speaking, the induction on r for class n and type 1 goes as follows:
coeﬃcients in Kn−1,r
1 are deﬁned by the induction hypothesis;
cochains in FCn−1,r
1 are deﬁned using coeﬃcients in Kn−1,r
1 ;
coeﬃcients in Kn−1,r+1
1 are deﬁned using cochains in FCn−1,r
1 .
Similar constructions are carried out for class n and type 0.

Finiteness theorems for limit cycles 97

1.16.3. Base of exterior induction. When m = 0 the rank is not considered and the
type is 0. Superexact series of class 0 and type 0 are exponential Dulac series; they
form a set E 0. Functional cochains of class 0 are almost regular germs: FC0
0 = R.
We recall that series in E 0 are of the form (51), where

ej = µjζ, µj → −∞,

and the aj are real polynomials.
In what follows we describe in detail the step of exterior induction from m = 0
to m = 1. It includes an interior induction on r and helps us to follow the step
from n − 1 to n.
We ﬁrst deﬁne the set E 0
1 of series STAR-01 and the set FC0
1 . These sets are
independent of the rank. The series in E 0
1 are again exponential Dulac series. The
cochains of class FC0
1 are those regular simple cochains (see § 1.15.3) that can be
decomposed in asymptotic series STAR-01 in some quadratic standard domains.
We now deﬁne the set E 1
0 of series STAR-10 and the set FC1
0 . This time we use
the interior induction.
Base of the interior induction: r = 0, series of class E 1,0
0 = STAR-(1, 0)0 and
cochains of class FC1,0
0 .
As mentioned above, to deﬁne series of a certain class, we must deﬁne the class
of exponents and the class of coeﬃcients. While the set of exponents of any class to
follow does not depend on the rank, the set of coeﬃcients does.
The set E1 of exponents of series of class 1 and type 0 is the set of all partial sums
of exponential Dulac series with non-negative exponents not exceeding 1. Namely,

E1 = {
e | e = ∑ Pj(ζ) exp µjζ}
,

where the sum is ﬁnite, the Pj are real polynomials and the µj ∈ [0, 1]. Moreover,
if µj = 1, then Pj = const, but if µj = 0, then Pj ∈ (ζ 2), that is, the free term and
linear term of Pj vanish. The principal exponent of the term exp e is deﬁned as the
limit
 ν1(e) = lim
(R+,∞) e(ξ)
exp ξ .

This limit exists by the deﬁnition of E1.
A motivation for this deﬁnition is given in the next subsection.
The set K1,0
0 of coeﬃcients of STAR-(1, 0)0 is the set FC0
1 of all simple functional
cochains. Series Σ ∈ E 1,0
0 are of the form (51), where ej ∈ E1, aj ∈ K1,0
0 and
ν1(ej) → −∞.
We now deﬁne cochains of class FC1,0
0 . The deﬁnition consists of two parts,
regularity and expandability.

Deﬁnition 1.30. The cochains F of class FC1,0
0 are those regular sectorial cochains
deﬁned in § 1.15.3 (the regularity assumption) that can be decomposed in asymp-
totic series STAR-(1, 0)0, denoted by Σ. This means that for every ν > 0 the
composite F ◦ exp can be approximated by a partial sum of Σ within accuracy
exp(−ν exp ξ) on the germ at inﬁnity of the domain ln Ω for some standard domain Ω
of class 1 (the expandability assumption).

98 Yu. S. Ilyashenko

This completes our description of the base of the interior induction. We now
make the step of induction on r. Suppose that the set K1,r
0 has already been deﬁned.
Let E 1,r
0 be the set of all series (51) with ej ∈ E1, aj ∈ K1,r
0 and ν1(ej) → −∞.
The following deﬁnition works for all classes and ranks as soon as the set E m,r
l
is deﬁned for some (m, r, l): l = 0, 1, m = 0, . . . , n, r ∈ Z
+.

Deﬁnition 1.31. A functional cochain F is said to be expandable in its domain Ω
in a series STAR-(m, r)l, which is denoted by Σ, if for every ν > 0 there is a partial
sum ΣN of Σ that approximates F ◦ exp
[m] within accuracy o(| exp(−ν Re exp
[m])|)
on the domain ln
[m] Ω:

F ◦ exp
[m] = ΣN + R, R = o(| exp(−ν Re exp
[m])|) on ln
[m] Ω. (52)

Deﬁnition 1.32. A cochain of class FC1,r
0 is a regular functional cochain which
is expandable in a series STAR-(1, r)0 in some standard domain of class 1.

Thus, in the course of the interior induction step, starting with the set of coeﬃ-
cients K1,r
0 , we have deﬁned the series of class E 1,r
0 and the cochains of class FC1,r
0 .
We now deﬁne the set K1,r+1
0 and thus complete the interior induction step:

K1,r+1
0 = L
(K1,r
0 , FC1,r
0 ◦ exp ◦µζ | µ ∈ (0, 1)
).

Here L stands for the linear hull with real coeﬃcients.
Thus, using induction on r, we have deﬁned the series and cochains of classes E 1,r
0 ,
FC1,r
0 for all r ∈ Z
+. The equalities E 1
0 = ⋃∞
0 E 1,r
0 and FC1
0 = ⋃∞
0 E 1,r
0 complete
the deﬁnition of series and cochains of class n = 1.
The induction step from n = 0 to n = 1 is completed. The induction step from
n − 1 to n is done in a similar way starting with series and cochains of class n
and type 1. Before making this step, we consider some motivations.

1.16.4. Motivations: expandability. Let us motivate the deﬁnition of the set E1

of exponents of the series in E 1
0 . These are series for the compositions F ◦ exp,
F ∈ FC1
0 . By the axiom ‘fourth shift lemma’, for all F1 ∈ FC1
0 and j ∈ A0 there is
a cochain F ∈ FC1
0 such that
 F1 ◦ exp ◦j = F ◦ exp .

If Σ1 is a STAR for F1 ◦ exp, then Σ1 ◦ j is a STAR for F ◦ exp. We consider the
simplest case, when F1 = exp(−ζ), F1 ◦ exp = exp(− exp ζ). Suppose that j has
an asymptotic Dulac series Σ:

Σ = ζ + ΣPj(ζ) exp(−µjζ), 0 < µj ↗ ∞.

Suppose for simplicity (this is an example only) that Σ = ζ + P exp(−µζ), µ ∈
(1/l + 1, 1/l], l ∈ N. Then

exp ◦j = (exp ζ) exp(P exp(−µζ))

= (exp ζ)
(1 +
 l∑

k=1
 (P exp(−µζ))
k

k! + o(exp(−(1 + ε)ζ))
)

Finiteness theorems for limit cycles 99

for some ε > 0. Hence, exp ◦j = e + o(exp(−εζ)),

where e is a sum of quasipolynomials of the form exp ζ + ΣPj exp νjζ, 0 < νj < 1.
Finally,
exp(− exp ◦j) = exp
(e + o(exp(−εζ))
) = (1 + o(exp(−εζ))
) · exp e.

The ‘tail’ of the series exp ◦j is included in the ﬁrst factor. We say that it is
‘absorbed by the coeﬃcient’. The exponent e is an element of the set E1 deﬁned
above.
The motivation for the deﬁnitions below is also related to the axioms stated
at the beginning of this section. Namely, the set of asymptotic series for cochains
of the classes FCn
0 , FCn−1
1 that satisfy the four shift lemmas and the condition that
FC0
1 contains N C, must contain all series constructed below.

1.16.5. Step of induction from n−1 to n: deﬁnition of STAR-(n − 1)1 and cochains
of class FCn−1
1 . We ﬁx n > 1 as above and suppose that all STAR and functional
cochains of classes m < n have already been deﬁned. To make the induction step
for series and cochains of class n and type 1, we must deﬁne the set of exponents
En−1
1 and the set of coeﬃcients Kn−1
1 .
The set of exponents En−1
1 is by deﬁnition equal to En−1
0 . The latter, being
a set of exponents of class n − 1, is already deﬁned by the induction hypothesis.
We write En−1
1 ≡ En−1
0 =: En−1.

We also make the inductive assumption that the principal exponent

νn−1(e) = lim
(R+,∞) e
exp[n−1] ξ

is well deﬁned for all e ∈ En−1. Let us now deﬁne the sets E n−1,r
1 , FCn−1,r
1 by
induction on r.

1.16.6. Base of exterior induction on r. The base of induction consists in deﬁning
the set of coeﬃcients Kn−1,r
1 of STAR(n − 1, r)1 for r = 0. We recall that the
group Gm, m ⩽ n, is deﬁned in § 1.5.3.

Deﬁnition 1.33. Put

Kn−1,0
1 = L(FCn−2
1 ◦ exp
[n−2] ◦ g | g ∈ Gn−3),

where the set FCn−2
1 is already deﬁned by the ‘exterior’ induction hypothesis on n.
We recall that L( · ) stands for the linear hull over R.

1.16.7. Step of exterior induction on r.

Deﬁnition 1.34. Suppose that the set Kn−1,r
1 is already deﬁned. We deﬁne the
set E n−1,r
1 of all STAR-(n − 1, r)1 as the set of all formal series of the form

Σ = ∑ aj exp ej, ej ∈ En−1, aj ∈ Kn−1,r
1 , νn−1(ej) → −∞.

100 Yu. S. Ilyashenko

Deﬁnition 1.35. A functional cochain F is a cochain of class n − 1, rank r and
type 1 if it possesses the following properties of regularity and expandability.
Regularity: F is an absolutely realizable regular cochain of class FCreg(Dn−1
1 )
in the sense of Deﬁnition 1.16.
Expandability: the composite F ◦ exp
[n−1] = ϕ can be expanded in a STAR-
(n − 1, r)1. Moreover, for every realization F∗ (where ‘∗’ stands for (k), (k+),
(k, l)) of F , the composite F∗ ◦ exp
[n−1] = ϕ is expanded in the same asymptotic
series. Here F is considered in an appropriate standard domain of class n − 1,
and its realizations F∗ are considered in some generalized neighbourhoods of the
corresponding domains (see (38)). In other words, the cochain and its realizations
are expandable in STAR-(n − 1, r)1 on their domains in the sense of Deﬁnition 1.31.

We recall that the set of all functional cochains of class n − 1, rank r and type 1
is denoted by FCn−1,r
1 .
The following deﬁnition completes the induction step:

Kn−1,r+1
1 = L(Kn−1,r
1 , FCn−1,r
1 ◦ exp
[n−1] ◦ g | g ∈ Gn−2−
slow ).

Thus we have deﬁned the sets E n−1,r
1 , FCn−1,r
1 for every r > 0. Then the for-
mula (49) determines the sets E n−1
1 , FCn−1
1 .
Summarizing, we give the following deﬁnition.

Deﬁnition 1.36. Functional cochains of class n and type 1 are absolutely realiz-
able functional cochains of type Dn−1
1 that can be decomposed in a STAR-(n − 1)1
in the generalized ε-neighbourhoods of their domains, along with all of their realiza-
tions considered in the generalized ε-neighbourhoods of the corresponding domains,
in the sense of Deﬁnition 1.31.

This completes the deﬁnition of superexact asymptotic series and functional
cochains of class n and type 1: FCn−1
1 . We now pass to type 0.

1.16.8. Deﬁnition of STAR-(n)0 and cochains of the class FCn
0 . We can now deﬁne
the sets of series and cochains of class n and type 0, STAR-n0 and FC n
0 . To do
this, we ﬁrst deﬁne the set En of exponents of STAR-n0.

Deﬁnition 1.37. A partial sum ΣN of a STAR-(n − 1)1 is said to be weakly real
if ΣN = SΣN .

We recall that SΣN (ζ) = ΣN (¯ζ).

Deﬁnition 1.38. The set En of exponents of STAR-n0 is the set of all partial
sums of the series STAR-(n − 1)1 with the following properties.
1) The sum e ∈ En is weakly real and takes the form

e =
 N∑

1 aj exp ̃ej, ̃ej ∈ En−1,

where νn−1(̃ej) ⩾ 0 for all j.

Finiteness theorems for limit cycles 101

2) The real limit
 νn(e) = lim
(R+,∞) e
exp[n]

exists. It is called the principal exponent of the term with exponent e.
3) One can ﬁnd a number µ > 0 and a standard domain of class n on which

| Re e ◦ ln
[n] | < µξ, |e ◦ ln
[n] | < µ|ζ|.

4) Im e → 0 on (R+, ∞).
The map νn : En → R, e ↦→ νn(e), is called the nth principal exponent map.

We now deﬁne STAR and cochains of class n and type 0. They are characterized
by rank r ⩾ 0 and are deﬁned in the same way as the corresponding objects of
class n − 1 and type 1 with only one diﬀerence: standard domains of class n − 1
are replaced by standard domains of class n. The deﬁnition is by induction on r.
Namely, we deﬁne the set of coeﬃcients Kn,r
0 and the set of all STAR-(n, r)0, which
is denoted by E n,r
0 . It consists of formal series of the form

Σ = ∑ aj exp ej, ej ∈ En, aj ∈ Kn,r
0 , νn(ej) → −∞.

1.16.9. Base of interior induction: r = 0. Put

Kn,0
0 = L(FCn−1
1 ◦ exp
[n−1] ◦ Gn−2),

where FCn−1
1 is deﬁned in the previous subsection. Then the induction goes in
exactly the same way as in the previous case and results in the deﬁnitions of the
sets E n
0 and FCn
0 of series and cochains of class n and type 0. We pass to details.

1.16.10. Step of induction on r.

Deﬁnition 1.39. Suppose that the set Kn,r
0 is already deﬁned. We deﬁne the
set E n,r
0 of all STAR-(n, r)0 as the set of all formal series of the form

Σ = ∑ aj exp ej, ej ∈ En, aj ∈ Kn,r
0 , νn(ej) → −∞.

The expandability of a functional cochain in a STAR-(n, r)0 is deﬁned in the
same way as for STAR-(n−1, r)1 (see Deﬁnition 1.31), only with n−1 replaced by n.

Deﬁnition 1.40. A functional cochain F is called a cochain of class n, rank r
and type 0 if it possesses the following properties of regularity and expandability.
Regularity: F is an absolutely realizable regular cochain of class FCreg(Dn
0 ) in
the sense of Deﬁnition 1.16.
Expandability: the composite F ◦ exp
[n] = ϕ can be expanded in a STAR-(n, r)0
and the composites F∗ ◦ exp
[n] = ϕ are also expanded in the same asymptotic
series for all k-, k+- and (k, l)-realizations F∗ of F . Here F is considered in an
appropriate standard domain of class n and the realizations F∗ are considered in
some generalized neighbourhoods of the corresponding domains (see (38)).

102 Yu. S. Ilyashenko

We recall that the set of all functional cochains of class n, rank r and type 0 is
denoted by FCn,r
0 .
The following deﬁnition completes the induction step:

Kn,r+1
0 = L(Kn,r
0 , FCn,r
0 ◦ exp
[n] ◦ g | g ∈ Gn−1−
slow ).

Thus we have deﬁned the sets E n,r
0 and FCn,r
0 for every r > 0. Then the for-
mula (50) determines the sets E n
0 and FCn
0 .
Summarizing, we give the following deﬁnition.

Deﬁnition 1.41. Functional cochains of class n and type 0 are absolutely real-
izable functional cochains of type Dn
0 that are deﬁned in standard domains of
class n and can be expanded in a STAR-n0 in the generalized ε-neighbourhoods
of these domains, along with all of their realizations considered in the generalized
ε-neighbourhoods of the corresponding domains.

We stress that the expansion in STAR-n is bilateral: the composites F ◦ exp
[n]

are approximated by partial sums of the series in a full neighbourhood of the germ
of the positive semi-axis at inﬁnity.
Thus the construction of the model for the axioms above is completed. We must
prove that the axioms do indeed hold for this model. In §§ 3 and 4 of part II
of this paper we give a sketch of the proof of the shift lemmas. In § 2 below we
give a schematic proof of a general Phragm´en–Lindel¨of theorem for cochains, which
yields the Phragm´en–Lindel¨of theorem for cochains of class n.

§ 2. A general Phragm´en–Lindel¨of theorem for functional cochains

In this section we prove a general Phragm´en–Lindel¨of theorem for regular func-
tional cochains of class FCreg(D) provided that the class D of admissible germs
possesses certain properties listed below. The result in this form is new, although
it relies heavily on the arguments in [1]. Then we deduce the Phragm´en–Lindel¨of
theorem for regular cochains of class n from the general Phragm´en–Lindel¨of the-
orem. To do this, we must in particular verify that admissible germs of class n
have the properties required from the class D in the general Phragm´en–Lindel¨of
theorem. This will be done schematically in § 5 of part II of this paper.
Roughly, the Phragm´en–Lindel¨of theorem asserts that if a cochain of a certain
class decreases on (R+, ∞) faster than any exponential, then it is identically equal
to zero on (R+, ∞).

2.1. Regular sectorial and simple cochains. We recall that regular sectorial
and simple cochains were deﬁned in § 1.15.3.

Theorem 2.1 (Phragm´en–Lindel¨of theorem for sectorial cochains). Let F be
a weakly realizable regular sectorial cochain deﬁned in some standard domain which
lies in a quadratic one. Suppose that F decreases on the real axis faster than any
exponential. Then F u ≡ F l ≡ 0.
The theorem also holds for G = IF provided that F is almost realizable.

Finiteness theorems for limit cycles 103

The second statement follows from the ﬁrst. Indeed, if F is almost realizable,
then SF is almost (hence, weakly) realizable too: the symmetry permutes k- and
k+-realizations. Therefore, the ﬁrst part of the Phragm´en–Lindel¨of theorem may
be applied to IF .

2.1.1. A preliminary estimate.

Lemma 2.1 (the ﬁrst preliminary estimate for sectorial cochains). Let F be a sec-
torial cochain of type

(exp ◦ µ1, . . . , exp ◦ µN ), 1 > µ1 > · · · > µN > 0.

Suppose that it decreases on the real axis faster than any exponential. Then for
every sector Sα = {| arg ζ| < α < π/2} there is a number C (depending on α) such
that everywhere on Sα we have

|F (ζ)| < exp(−C|ζ|
µ), µ = µ
−1
1 . (53)

This lemma is proved in the same way as Lemma 0.4: trivialize the cocycle, use
the maximum modulus principle, and construct the cochain Fλ,a as in Lemma 0.4.
We omit the details.
If the cochain F is of numerical type 1, a reference to an appropriate version of
the Phragm´en–Lindel¨of theorem completes the proof.
But for numerical type beyond 1, a new idea is required: we shall use realizations.

2.1.2. Use of realizations. We shall prove the Phragm´en–Lindel¨of theorem for sec-
torial cochains by induction on the numerical type N . We will estimate from above
the realizations of the sectorial cochain one by one: the larger the number of the
realization, the stronger the estimate. The last realization is a holomorphic function
on its domain, and its rate of decay is so high that the classical Phragm´en–Lindel¨of
theorem forces this function to be identically zero. We now pass to more detail.
We again use a universal constant C that may take diﬀerent values in diﬀerent
inequalities.

Lemma 2.2 (the second preliminary estimate for sectorial cochains). Suppose that
a sectorial cochain of type

(exp µk+1, . . . , exp µN ), 1 > µk+1 > · · · > µN > 0, (54)

is deﬁned in the following sector Sµ, 1 > µ > µk+1:

Sµ = {
ζ | |ζ| > R, arg ζ ∈ (− π
2 µ, α(µ)
)},

where R is some positive number,

α(µ) =
 




πµ for µ < 1
2 ,

π
2 − δµ for µ ⩾ 1
2 ,

104 Yu. S. Ilyashenko

and δ is so small that the opening γ of the sector Sµ is larger than πµ. Suppose
that F decreases on (R+, ∞) in the following way:

|F | ≺ exp(−C|ζ|
1/µ).

Then |F | ≺ exp(−C|ζ|
1/µk+1) (55)

on every sector lying strictly inside Sµ.

This lemma is proved in the same way as the ﬁrst preliminary estimate for
sectorial cochains.
We now deduce the Phragm´en–Lindel¨of theorem for sectorial cochains from the
following estimate: for all k = 1, . . . , N ,

|F(k)| ≺ exp(−C|ζ|
1/µk ). (56)

This estimate is proved by induction on k.
Induction base: k = 1. In this case (56) follows from the ﬁrst preliminary
estimate for sectorial cochains.
Induction step: from k to k + 1. We suppose that (56) has already been proved
for k and prove it for k + 1. Note that the kth realization of F is deﬁned on
a domain Ω(σ,k) of the form

Ω(σ,k) = (exp µkζ)(Πmain) ∩ Ω,

where Πmain is deﬁned in (30). This domain contains the germ at inﬁnity of any
sector Sµ for µ < µk. Take an arbitrary µ ∈ (µk+1, µk). Apply Lemma 2.2 to the
realization F(k). This is a sectorial cochain of type (54) deﬁned in the sector Sµ.
The lemma yields (55) for F = F(k). At the same time, this is an estimate for
F(k+1) because F(k+1) = F(k) on (R+, ∞). This completes the induction step and
proves (56) for k + 1 and, therefore, for all k = 2, . . . , N .
The realization F(N ) is holomorphic on the domain Ω(σ,N ), which contains a sec-
tor with opening larger than πµN . Moreover,

|F(N )| ≺ exp(−C|ζ|
1/µN )

on (R+, ∞). By the classical Phragm´en–Lindel¨of theorem, F(N ) ≡ 0. This com-
pletes the proof of the Phragm´en–Lindel¨of theorem for sectorial cochains.
The Phragm´en–Lindel¨of theorem for simple cochains is proved in the same way.
We omit the details and pass to the general Phragm´en–Lindel¨of theorem.

2.2. Statement of the result, and special admissible germs.

2.2.1. The general Phragm´en–Lindel¨of theorem. Consider a proper class Ω of stan-
dard domains (see Deﬁnition 1.18). Let D be the class of special Ω-admissible germs
to be described below.

Theorem 2.2. Let F be a regular weakly realizable functional cochain of type

σ = (σ1, . . . , σN ), σj ∈ D, σj ≻ σj+1, (57)

Finiteness theorems for limit cycles 105

which is deﬁned on a standard domain of class Ω, grows no faster than exp νξ
for some ν > 0, and decreases on (R+, ∞) faster than any exponential exp(−νξ),
ν > 0. Then F u ≡ 0 and F l ≡ 0.

This statement becomes complete after describing the set D. We list the prop-
erties required of the germs in this set.

2.2.2. Generalized powers. For every germ σ ∈ D the limit

l(σ) = lim
(R+,∞) ξσ′

σ ∈ [1, ∞] (58)

exists.
The number l(σ) is called the generalized power of σ.
In particular, if l(σ) = l < ∞, then σ = ζ l+o(1).

Deﬁnition 2.1. A germ σ ∈ D is said to be almost power if l(σ) ∈ [1, ∞), and
almost linear if l(σ) = 1.

2.2.3. Generalized exponents. Let Πa be the germ at inﬁnity of the half-strip
| Im ζ| < a. We say that a certain relation holds on (Π
∀, ∞) if it holds on Πa
for every a (the symbol Π∀ means the germ at inﬁnity of any half-strip Πa).
a) For every σ ∈ D the limit

L(σ) = lim
(Π∀,∞) σ′

σ ∈ [0, 1] (59)

exists.
b) If L(σ) = 0, then arg σ′ → 0 on (Π∀, ∞). (60)

c) If L(σ) = 1, then
 ξ − ln σ ↘ ∞ on (R+, ∞). (61)

The number L(σ) is called the generalized exponent of σ.

Deﬁnition 2.2. A germ σ of class D is said to be fast if L(σ) = 1, sectorial
if L(σ) ∈ (0, 1), and slow otherwise.

2.2.4. Ordering and monotonicity. The germs in D are ordered by the relation ≻.
Moreover, the following monotonicity conditions hold (the ﬁrst two repeat (32), (33)
respectively).
a) Suppose that Ω ∈ Ω, σ1 ≻ σ2 ∈ D, and the germs σ1 and σ2 are not weakly
equivalent. Then (σ1Πmain ∩ Ω, ∞) ⊃ (σ2Πmain ∩ Ω, ∞). (62)

b) Let the germs σ1 and σ2 be weakly equivalent but not equal. Then σ1 and σ2
can be renumbered in such a way that for all ε and δ with 0 < δ < ε < 1 we have

(σ2Π
(δ)
main ∩ Ω, ∞) ⊂ (σ1Π
(ε)
main ∩ Ω, ∞). (63)

c) Suppose that Ω ∈ Ω, σ1 ≻ σ2 ∈ D and ρj = σ−1
j , j = 1, 2. Then

ρ2
ρ1 ≻ 1 + o(1). (64)

106 Yu. S. Ilyashenko

2.2.5. Strips of Warschawski type. Suppose that σ ∈ D, L(σ) = 1, ln σΠ = ̃Π.
Then ̃Π is a strip of Warschawski type. We will not describe the set of all strips of
Warschawski type. We require ̃Π to be an element of the following subset of this
set.
The germ (̃Π, ∞) is of the form

(̃Π, ∞) = {
(ξ, η) | η ∈ ( π
2 +γ(ξ), π
2 −γ(ξ)
), ξ ∈ (R+, ∞)
} and γ ↘ 0, γ′ ↗ 0.

(65)
The function γ in (65) is such that
∣
∣
∣
∣ ξγ′

γ
 ∣
∣
∣
∣ ≺ 2, γ′(ξ(1 + o(1))) = γ′(ξ)(1 + o(1)) on (R+, ∞). (66)

For every λ > 0 the strip

(̃Πλ, ∞) = {
(ξ, η) | η ∈ (− π
2 + γ(ξ), π
2 − λγ(ξ)
)} (67)

is contained in ln Ω for every standard domain Ω of class Ω and in Π∗:

(̃Πλ, ∞) ⊂ Π∗ ∩ ln Ω. (68)

2.2.6. Nice partitions. To state the next property, we need the following deﬁnitions.
Suppose that σ is an admissible germ and the partition σ∗Ξst is well deﬁned
in a standard domain Ω.

Deﬁnition 2.3. The partition σ∗Σst is said to be nice if the following conditions
hold.
• All boundary lines are the graphs of certain functions η = η(ξ).
• Every vertical segment Re ζ = ξ in Ω intersects at most ﬁnitely many boundary
lines. The sum of the secants of the slope angles of the partition curves at the
intersection points is called the total slope and is denoted by CΞ,Ω(ξ). We require
that CΞ,Ω < Cξ4. (69)

• If σ is not almost linear, then the real part of the germ ρ = σ−1 is non-
decreasing when moving away from the real axis along a vertical line:

Re ρ ≻ ρ ◦ Re . (70)

If σ is almost linear, then for every δ > 0 we have

Re ρ ≻ (1 − δ)ρ ◦ Re . (71)

Deﬁnition 2.4. A partition of type

σ = (σ1, . . . , σN ), σ1 ≻ · · · ≻ σN (72)

is said to be nice if the partitions σj∗Ξst are nice for j = 1, . . . , N .

Finiteness theorems for limit cycles 107

Here is another property of the germs in D.
For every standard domain Ω ∈ Ω and any ordered tuple (57) there is a smaller
domain ̃Ω ⊂ Ω, ̃Ω ∈ Ω, such that the partition (57) of ̃Ω is nice.
The hypothesis of Theorem 2.2 is that the class D possesses the properties listed
above.
In this subsection we ﬁx an arbitrary proper class Ω of standard domains and
a class D of Ω-admissible germs. We also assume in all assertions below (as well
as in Theorem 2.2) that D possesses all the properties listed in this subsection.
The germs σj in the tuple (72) are ordered by the relation ≻. Hence the tuple
begins with fast germs, continues with sectorial ones, and ends with slow ones. We
may assume without loss of generality that σ1 is fast. Otherwise we add a ‘ﬁctitious’
germ to the tuple (57). This procedure is explained at the end of § 2.3.1.

2.2.7. Proof of the Phragm´en–Lindel¨of theorem for cochains of class n. In order
to apply the general Phragm´en–Lindel¨of theorem to cochains of class n, we must
prove that families of admissible germs of class n satisfy the assumptions imposed
in § 2.2 on the class D. These proofs are carried out in § 5 in the form of a sequence
of lemmas corresponding to the properties listed above. Modulo these lemmas,
the Phragm´en–Lindel¨of theorem for functional cochains of class n follows from
Theorem 2.2. A proof of Theorem 2.2 is sketched in the remaining part of § 2.

2.3. Preliminary estimates and plan of the proof of the Phragm´en–
Lindel¨of theorem.

2.3.1. Preliminary estimates. Let F be a cochain as in the Phragm´en–Lindel¨of
theorem. The ﬁrst (resp. second) estimate in the following lemma will be applied
to F (resp. to the k-realizations F(k)).

Lemma 2.3. I. Consider a cochain F of type (57) deﬁned in a standard domain
Ω ∈ Ω and satisfying the hypotheses of the Phragm´en–Lindel¨of theorem. Suppose
that the germ σ1 in the tuple (57) is fast. Then on (R+, ∞) we have

|F (ξ)| ≺ exp(−C exp ρ1(ξ)) (73)

for some C > 0.
II. Consider a tuple (57) and a cochain Fk (not necessarily the realization F(k)
of F ) deﬁned for some ε > 0 in a domain

Ωσ,k = σkΠ
(ε)
main ∩ Ω, Ω ∈ Ω, (74)

of type σk = (σk+1, . . . , σN ).

Suppose that one of the following estimates holds on (R+, ∞):

|Fk(ξ)| ≺ exp(−C exp ρk) (75)

in the case when σk is fast;

|Fk(ξ)| ≺ exp(−C exp(1 − δ)ρk) (76)

108 Yu. S. Ilyashenko

in the case when σk is sectorial or slow. Then on (R+, ∞) we have

|Fk(ξ)| ≺ exp(−C exp ρk+1) (77)

in the case when σk+1 is fast;

|Fk(ξ)| ≺ exp(−C exp(1 − δ)ρk+1) (78)

for every δ > 0 in the case when σk+1 is sectorial or slow, with the following
exceptions. The lemma requires that
a ) σ1 is fast;
b) if σk is fast, then σk+1 is not slow;
c) if σk is sectorial, then σk+1 is not almost power.

These exceptions are not at all restrictive. We could omit them by introduc-
ing some ﬁctitious germs in (57). Namely, we put a ﬁctitious fast germ at the
ﬁrst place, a ﬁctitious sectorial germ between any successive fast and slow germs
in (72), and a ﬁctitious slow (but not almost power) germ between any successive
sectorial and almost power germs in (57). So we will apply Lemma 2.3 without any
exception.
The introduction of ﬁctitious germs can be explained as follows. Let F be
a cochain of type (57) without jumps (that is, with δF = 0) on those curves
σ1(η = πj) with j ̸= 0 that contain no arcs of curves in σj∂Ξst for j > 1. Suppose
that |δF | ≺ exp(−C exp ρ2(ξ)).

Then the cochain F is actually of type (σ2, . . . , σN ). The germ σ1 in the tuple (57)
for the cochain F may be regarded as ﬁctitious.
Suppose now that the germ σ1 in the tuple (57) is not fast. Then we can add
a germ σ0 = exp(ζ − √ζ) to the left of (57) as a ﬁctitious germ (in the sense of the
previous paragraph). The new tuple will begin with a ﬁctitious fast germ.
In this case, for a cochain F deﬁned on Ω, the realization F(1) will be deﬁned on
the domain σ0Πmain ∩ Ω and will be equal to the restriction of F to this domain.
Then the preliminary estimates say that F decreases not only exponentially
on (R+, ∞), but faster than exp(−C exp ρ0), ρ0 = σ−1
0 = ϕ(ζ) ◦ ln, where the
function ϕ(ζ) is inverse to (ζ − √ζ).
The role of the other ﬁctitious germs is described similarly.
Lemma 2.3 is a modiﬁed version of Lemma 4 in § 3.6 of [11]. It is a more
complicated analogue of Lemma 0.4. Its proof follows the same lines: we trivialize
the cocycle, apply the maximum modulus principle, construct the cochain Fλ,a
and estimate it from above. However, the proof is more technical because of the
presence of the admissible germs σj.

2.3.2. Sketch of the proof of the Phragm´en–Lindel¨of theorem based on the prelim-
inary estimates. Consider a cochain F of type (57) as in Theorem 2.2. Recall
that germs σ, ̃σ in D are weakly equivalent if the correction of their compo-
sition quotient σ−1 ◦ ˜σ is bounded on (R+, ∞). We divide the tuple (57) into
weak equivalence classes. Since the germs in (57) are ordered by the relation ≻,
germs in one class occur consecutively. Let σkj , j = 1, . . . , m, be the last germs

Finiteness theorems for limit cycles 109

in their weak equivalence classes. Then σk1 is weakly equivalent to σ1. We shall
prove the Phragm´en–Lindel¨of theorem by induction on j. By adding ﬁctitious
germs to the sequence (57), we may assume that the following conditions hold.
• The germ σ1 is fast.
• If σk is fast, then σk+1 is sectorial.
• If σk is sectorial, then σk+1 is not almost power.
• The last germ σN in (57) is linear: σN = µζ.
We comment on the last assumption. For every germ σ ∈ Dn−1
1 there is a linear
germ ˜σ such that σ ≻ ˜σ and σ is not weakly equivalent to ˜σ. Indeed, if σ ∈
Dn−1+
slow ◦ L
n−1, then σ′ → ∞ on (R+, ∞) and the desired requirement is obvious.
But if σ ∈ Dn−1
rap ◦ L
n−1, then the limit

lim
(R+,∞) σ′ = λ ∈ (0, ∞)

exists. To fulﬁll the requirement, it now suﬃces to take µ < λ.
We shall prove the relations (75), (76) for the realizations F(kj ) by induction
on j. These relations for F(km) yield the same relations for the realization F(N ),
which is a holomorphic function on its domain. Below we present special arguments
that enable us to apply the classical Phragm´en–Lindel¨of theorem and conclude that
F(N ) ≡ 0.
Let F be the same as in the Phragm´en–Lindel¨of theorem and, therefore, the
same as in Lemma 2.3.
Induction base: j = 0. In this case, F(k0) = F by deﬁnition. Applying the ﬁrst
part of Lemma 2.3 to F , we conclude that (73) holds for F . Since σ1 and σk1 are
weakly equivalent, the bound (73) also holds if we replace ρ1 by ρk1:

|F (ξ)| ≺ exp(−C ′ exp ρk1) (79)

for some C ′ > 0. Indeed,
σ−1
1 ◦ σk1 = ρ1 ◦ σk1 = id +O(1).

Hence σ−1
k1 ◦ σ1 = ρk1 ◦ ρ−1
1 = id +O(1). Then

exp ρk1 = exp(ρk1 ◦ ρ−1
1 ) ◦ ρ1 = exp(ρ1 + O(1)) ≺ C exp ρ1

for some C > 0. This yields (79).
Moreover, F(k1) = F on (R+, ∞). Hence F(k1) satisﬁes (79) on (R+, ∞). This
completes the justiﬁcation of the induction base.
Induction step: from j ⩾ 1 to j + 1.
Suppose that F(kj ) satisﬁes (75) or (76) depending on the properties of σkj , where
Fk, ρk are replaced by F(kj ) and ρkj . Then, by the second part of Lemma 2.3,

|F(kj )| ≺ exp(−C exp ρkj +1)

or |F(kj )| ≺ exp(−C exp(1 − δ)ρkj +1),

depending on whether σkj +1 is fast or not.

110 Yu. S. Ilyashenko

Note that σkj +1 is weakly equivalent to σkj+1. Hence, by the arguments used to
justify the induction base, the same inequalities hold if we replace ρkj +1 by ρkj+1.
The realizations F(kj ) and F(kj+1) coincide on (R+, ∞). Hence,

|F(kj+1)| ≺ exp(−C exp ρkj+1)

or |F(kj+1)| ≺ exp m(−C exp(1 − δ)ρkj+1),

depending on whether σkj+1 is fast or not. This completes the induction step.
As a result, we conclude that

|F(N )| ≺ exp(−C exp ρN ). (80)

The realization F(N ) is a holomorphic function on the domain

Ωσ,N = σN (Πmain ∩ ρN Ω).

By assumption, σN = µζ. Hence Ωσ,N is the curvilinear strip µ(Π1 ∪ Π∗). In
this strip F(N ) decreases faster than exp(−C exp µ
−1ξ). The function F(N )(µζ) is
holomorphic on a horizontal strip wider than π and decreases on (R+, ∞) faster
than exp(−C exp ξ). The classical Phragm´en–Lindel¨of theorem now implies that
F(N ) ≡ 0.
This completes the deduction of the general Phragm´en–Lindel¨of theorem from
Lemma 2.3.
Our proof of Lemma 2.1 uses the same arguments as the proof of Lemma 0.4.
Unfortunately, they provide a weaker version than needed: the so-called preparatory
estimates. To deduce the preliminary estimates from the preparatory ones, we need
serious technical eﬀorts. We omit the details here.

§ 3. Some notation

3.1. General notation. 1) z = x + iy is the standard coordinate on C, ζ = ξ + iη
is the logarithmic coordinate (ζ = − ln z);
2) C+ = {ζ : Re(ζ) > 0} is the right half-plane;
3) Ad(f )g = f −1 ◦ g ◦ f ;
4) Ag = Ad(exp)g;
5) f [k] = f ◦ f ◦ · · · ◦ f (k times).

3.2. Correspondence map for a saddlenode.

1. ∆st = C exp
(− 1
hk,a
 ), C = exp 1
k , hk,a(x) = kx
k

1 − akxk ln x
is the holonomy of the normal form of a saddlenode in the z-chart (see row 5 of the
table in § 0.9).
2. Fnorm is the normalizing sectorial cochain for a parabolic germ; ̃Fnorm is the
same cochain in the logarithmic chart.
3. Correspondence map TO a central manifold written in the z-chart: ∆ =
gl ◦ ∆st ◦ F l
norm = gu ◦ ∆st ◦ F u
norm, where the F u,l
norm are the components of the nor-
malizing cochain corresponding to the sectors Su,l, and the gu,l are parabolic germs.

Finiteness theorems for limit cycles 111

3.3. Sets of germs. 1. R is the set of almost regular germs written in the loga-
rithmic chart; R0 is the set of germs in R with aﬃne principal part the identity.
2. H is the set of parabolic germs of conformal maps at zero written in the
logarithmic chart (at ∞).
3. Aﬀ is the set of germs of aﬃne maps (C+, ∞) → (C+, ∞) with real coeﬃcients
and positive multiplier.
4. N Ck is the set of normalizing cochains of order k (that is, those corresponding
to strips of width π/k).
5. N C = ⋃
k a
k ◦ N Ck ◦ a
−1
k , where ak is the aﬃne map ζ ↦→ kζ − ln k.
6. MR is the set of germs whose restriction to (R+, ∞) is a map (R+, ∞) → R.
7. TO = (H ◦ exp ◦ R0 ◦ N C ◦ Aﬀ) ∩ MR is a class containing the holonomy TO
of a saddlenode TO the centre manifold (written in the logarithmic chart).
8. FROM is the set of germs inverse to the germs in TO.
9. H 0 = Gr(Ad(Aﬀ)H, R0).
10. A0 = Gr(f ∈ R0 ◦ N C | there is a ̃g ∈ H : Ãg ◦ f is real).
11. Gn is the set of all composites of maps in TO, FROM and R of depth n with
an equal number of maps in TO and FROM (the monodromy of any polycycle
of depth n is contained in Gn). It is easy to see that Gn = Gr(A
k(FROM ◦
R ◦ TO), R) | 1 ⩽ k ⩽ n − 1). By the ﬁnal structure theorem, Gn ⊂ Gr(Gn−1,
A
n−1A0, AnH 0) ∩ MR.
12. J n−1 = Ad(Gn−1)A
n−1A0.
13. H n = Gr(id +FCn
0+ ◦ exp
[n] ◦g | g ∈ Gn−1).
14. Gn = Gr(Gn−1, J n−1, H n) ∩ MR.
15. λk(g) = lim(R+,∞) A
−kg/ξ is the generalized multiplier of order k of the germ
g : (R+, ∞) → (R+, ∞).
16. If the group G and the number k are such that G is k-proper, then we deﬁne

λ−1
k (0) = G−
slow, λ−1
k (R+) = Grap, λ−1
k (∞) = G+
slow,

Gslow = G \ Grap = G−
slow ∪ G+
slow.

3.4. Functional cochains. 1. Φc(C+) is a quadratic standard domain, Φc(ζ) =
ζ + c
√1 + ζ.
2. Πj = {Im ζ ∈ π[j − 1, j]} is a strip of the standard partition Ξst of the right
half-plane C+.
3. FCn
0 , FCn−1
1 are the sets of cochains of class n, which are deﬁned axiomatically
in § 1.5. A model for this axiomatic deﬁnition is built in §§ 1.10–1.16.
4. FCn
0+, FCn−1
1+ : the subscript ‘+’ means that the cochain is rapidly decreasing,
that is, |F (ζ)| ≺ exp(−εξ) in some standard domain of class n (resp. n − 1).
Equalities with the sign (+) hold with plus as well as without plus.
5. FCm with 1 ⩽ m ⩽ n stands for FCm
1 if m ⩽ n − 1, and FCn
0 if m = n.
6. F m
(+)g = FCm
(+) ◦ exp
[m] ◦g.

Acknowledgements. It is my pleasure to thank the referee for a great job and
numerous fruitful comments aimed at making the paper more understandable. I am
also grateful to Ivan Shilin, Alexei Okunev and Stanislav Minkov who read the ﬁrst
draft of the text and eradicated many bugs. Alexei Okunev also compiled the list
of notation.

112 Yu. S. Ilyashenko

Bibliography

[1] Yu. S. Il’yashenko, Finiteness theorems for limit cycles, transl. from the Russian,
Transl. Math. Monogr., vol. 94, Amer. Math. Soc., Providence, RI 1991.
[2] J. ´Ecalle, Introduction aux fonctions analysables et preuve constructive de la
conjecture de Dulac, Actualites Math., Hermann, Paris 1992.
[3] I. Bendixson, “Sur les courbes d´eﬁnies par des ´equations diﬀ´erentielles”, Acta Math.
24:1 (1901), 1–88.
[4] F. Dumortier, Singularities of vector ﬁelds, Monograf. Mat., vol. 32, Instituto de
Matem´atica Pura e Aplicada, Rio de Janeiro 1978.
[5] A. Seidenberg, “Reduction of singularities of the diﬀerential equation A dy = B dx”,
Amer. J. Math. 90:1 (1968), 248–269.
[6] H. Dulac, “Sur les cycles limites”, Bull. Soc. Math. France 51 (1923), 45–188;
Russian transl., H. Dulac, On limit cycles, Nauka, Moscow 1980.
[7] Yu. S. Il’yashenko, “Limit cycles of polynomial vector ﬁelds with nondegenerate
singular points on the real plane”, Funktsional. Anal. i Prilozhen. 18:3 (1984),
32–42; English transl., Funct. Anal. Appl. 18:3 (1984), 199–209.
[8] S. M. Voronin, “Analytic classiﬁcation of germs of conformal mappings (C, 0) →
(C, 0) with identity linear part”, Funktsional. Anal. i Prilozhen. 15:1 (1981), 1–17;
English transl., Funct. Anal. Appl. 15:1 (1981), 1–13.
[9] Yu. S. Il’yashenko, “Dulac’s memoir ‘On limit cycles’ and related problems of the
local theory of diﬀerential equations”, Uspekhi Mat. Nauk 40:6(246) (1985), 41–78;
English transl., Russian Math. Surveys 40:6 (1985), 1–49.
[10] Yu. S. Il’yashenko, “Separatrix lunes of analytic vector ﬁelds of the plane”, Vestn.
Mosk. Univ. Ser. 1 Mat. Mekh., 1986, no. 4, 25–31; English transl., Mosc. Univ.
Math. Bull. 41:4 (1986), 28–35.
[11] Yu. S. Il’yashenko, “Finiteness theorems for limit cycles”, Uspekhi Mat. Nauk
45:2(272) (1990), 143–200; English transl., Russian Math. Surveys 45:2 (1990),
129–203.
[12] E. C. Titchmarsh, The theory of functions, 2nd ed., Oxford Univ. Press, Oxford
1939; Russian transl., Gostekhizdat, Moscow 1951; 2nd ed., Nauka, Moscow 1980.

Yulij S. Ilyashenko
National Research University ‘Higher
School of Economics’, Moscow
Cornell University, Ithaca, NY, USA
Moscow Independent University
E-mail: yulijs@mccme.ru
 Received 3/FEB/15
16/JUN/15
Edited by A. V. DOMRIN
