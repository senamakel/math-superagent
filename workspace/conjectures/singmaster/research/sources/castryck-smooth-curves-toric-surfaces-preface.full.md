<!-- source: https://homes.esat.kuleuven.be/~wcastryc/preface.pdf | converted from PDF -->

vii

EXTENDED PREFACE TO:

Smooth curves in toric surfaces

(Les courbes lisses dans les surfaces toriques)

by Wouter CASTRYCK

Let k be an algebraically closed ﬁeld and let

f = ∑

(i,j)∈Z2 cijxiyj ∈ k[x±1, y±1]

be an irreducible bivariate Laurent polynomial, deﬁning a curve Uf inside the two-dimen-
sional torus T2 := (k∗)2 = A2 \ coordinate axes. This manuscript is devoted to con-
nections between the birational geometry of Uf and the combinatorics of the Newton
polygon ∆(f ) = conv{ (i, j) ∈ Z
2 | cij ̸= 0 } ⊆ R
2

(assumed to be two-dimensional) of f . The earliest such connection is surprisingly old,
dating back to 1893, when Baker observed [Bak93] that the geometric genus of Uf is
bounded by the number of lattice points (= Z2-valued points) in the interior of ∆(f ). In
the 1970s, after toric geometry had made its appearance, a more satisfactory proof was
given by Khovanskii [Kho77], who moreover showed that Baker’s bound is generically
met. Recently developed tools such as tropical geometry and Berkovich theory concep-
tualized this remarkable result further, although these topics will not be addressed here.
A well-known generically satisﬁed condition which is sufﬁcient for meeting Baker’s
bound [CDV06, Prop. 1] is that f is nondegenerate with respect to its Newton polygon,
meaning that for all faces τ ⊆ ∆(f ) of any dimension (i.e. vertices, edges and ∆(f ) itself),
the system of equations

fτ = x ∂fτ
∂x = y ∂fτ
∂y = 0 with fτ = ∑

(i,j)∈τ ∩Z2 cijxiyj

has no solutions in T2. For ∆ a lattice polygon (= the convex hull in R2 of ﬁnitely many
points in Z2) we say that f is ∆-nondegenerate if it is nondegenerate with respect to its
Newton polygon and ∆(f ) = ∆. In general, the condition of nondegeneracy is not strictly
needed for meeting Baker’s bound, which leads to the following slight and seemingly
bland relaxation:

Deﬁnition 1. Let ∆ be a two-dimensional lattice polygon and let f ∈ k[x±1, y±1] be irreducible.
We say that f is weakly ∆-nondegenerate if

• ∆(f ) ⊆ ∆ and for each edge τ ⊆ ∆ one has ∆(f ) ̸⊆ ∆ \ τ ,

• the genus of Uf equals the number of lattice points in the interior of ∆.

viii

Weak nondegeneracy is the assumption underlying most of the results presented in this
manuscript. Besides being (slightly) weaker than nondegeneracy and thereby leading to
stronger statements, the notion allows for more combinatorial freedom, in the sense that
a weakly ∆-nondegenerate Laurent polynomial might also be weakly ∆′-nondegenerate
for some other (potentially easier) lattice polygon ∆′, which has important proof-technical
advantages. This freedom does not apply to ∆(1), the convex hull of the lattice points in
the interior of ∆, which is ﬁxed and in fact turns out to play a more important role than
∆ itself.

Well-known examples. Familiar examples include the Weierstrass polynomials f = y2 −
h(x), where char k ̸= 2 and h(x) ∈ k[x] is squarefree of degree 2g + 1 for some integer
g ≥ 1: these are weakly ∆2g+1,2-nondegenerate. Other examples are the dehomogeniza-

(0, 0) (2g + 1, 0)

(0, 2)
 ∆2g+1,2
 (0, 0) (d, 0)

(0, d)
 dΣ
g interior lattice points

(d−1)(d−2)
2 interior lattice points

tions f ∈ k[x, y] with respect to z of the homogeneous degree d ≥ 1 forms F ∈ k[x, y, z]
that deﬁne a smooth curve in P2: such polynomials are weakly dΣ-nondegenerate. In
both cases the reader sees that Baker’s bound conﬁrms the well-known formula for the
genus.

Remark. More generally for a, b ∈ Z≥1 we use ∆a,b to denote conv{(0, 0), (a, 0), (0, b)}. If
gcd(a, b) = 1 then the corresponding curves are said to be Ca,b; this notion was intro-
duced by Miura in the context of coding theory [Miu93].

More examples. Other recurring examples are weakly dΥ-nondegenerate Laurent poly-
nomials and weakly □a,b-nondegenerate Laurent polynomials, where d, a, b ≥ 1, which

(−d, −d)
 (d, 0)

(0, d)

dΥ
 (0, 0) (a, 0)

(a, b)(0, b)
 □a,b

(−d, −d)

deﬁne curves of genus 3
2 d2 − 3
2 d + 1 and (a − 1)(b − 1), respectively.

For an irreducible (not necessarily smooth or complete) algebraic curve C/k and a
two-dimensional lattice polygon ∆, we say that C is weakly ∆-nondegenerate if it is
birationally equivalent to Uf for some weakly ∆-nondegenerate Laurent polynomial f ∈
k[x±1, y±1] — similarly we say that C is ∆-nondegenerate if f can moreover be taken
∆-nondegenerate.
The presented work groups together a number of research papers that are devoted to
connections between the birational geometry of such a weakly ∆-nondegenerate curve
 ix

C and the combinatorics of ∆. Their joint goal is to extend the geometry-combinatorics
dictionary that started with Baker’s formula for the genus, although we stress that sev-
eral entries remain to be added and/or enhanced by future researchers. For reasons of
coauthorship and efﬁciency I have left the papers in their original shape, even though
when put together the treatment is not entirely uniform: some statements assume non-
degeneracy rather than weak nondegeneracy, while others are presented subject to the
condition that the base ﬁeld k is of characteristic 0. One source for this non-uniformity is
that the material has matured over time, with some insights postdating the publication
of the earliest papers. Another cause is that several important references assume that
char k = 0 or even k = C, and unfortunately I was not able to sift each of these to the
bottom to verify the need for this (possibly often unneeded) assumption.
In view of these considerations, the goal of this preface is not only to give an overview
of the results obtained, but also to update the exposition: in the text below, all main re-
sults are stated under the weak nondegeneracy assumption, which is always sufﬁcient,
and certain characteristic zero statements have been reformulated in arbitrary character-
istic, along with some lines of explanation why this is allowed.

Remark on terminology. Unfortunately the non-uniformity also affects the terminology of
being weakly ∆-nondegenerate, for which a.o. in Chapters 5 and 11 the phrasing ∆-toric is
used.

Contents. Concretely, the following papers are included in this HDR thesis:

• Chapter 1: On nondegeneracy of curves, Algebra & Number Theory 3(3), pp. 255-281
(2009), written jointly with John Voight

• Chapter 2: Moving out the edges of a lattice polygon, Discrete and Computational
Geometry 47(3), pp. 496-518 (2012)

• Chapter 3: The lattice size of a lattice polygon, Journal of Combinatorial Theory, Series
A 136, pp. 64-95 (2015), written jointly with Filip Cools

• Chapter 4: A minimal set of generators for the canonical ideal of a non-degenerate curve,
Journal of the Australian Mathematical Society 98(3), pp. 311-323 (2015), written
jointly with Filip Cools

• Chapter 5: Linear pencils encoded in the Newton polygon, to appear in International
Mathematics Research Notices (2017), written jointly with Filip Cools

• Chapter 6: Computing graded Betti tables of toric surfaces, preprint, written jointly
with Filip Cools, Jeroen Demeyer and Alexander Lemmens

• Chapter 7: A lower bound for the gonality conjecture, preprint

• Chapter 8: On graded Betti tables of curves in toric surfaces, preprint, written jointly
with Filip Cools, Jeroen Demeyer and Alexander Lemmens

• Chapter 9: A combinatorial interpretation for Schreyer’s tetragonal invariants, Docu-
menta Mathematica 20, pp. 903-918 (2015), written jointly with Filip Cools

• Chapter 10: Intrinsicness of the Newton polygon for smooth curves on P1 ×P1, to appear
in Revista Matemática Complutense, written jointly with Filip Cools

• Chapter 11: Curves in characteristic 2 with non-trivial 2-torsion, Advances in Math-
ematics of Communications 8(4), pp. 479-495 (2014), written jointly with Marco
Streng and Damiano Testa

x

I have also made these chapters, as well as the current preface, available in electronic
form on http://math.univ-lille1.fr/~castryck/HDR/.

Acknowledgements. My Ph.D. thesis was on the development of a Kedlaya-style algorithm
for computing Hasse-Weil zeta functions of nondegenerate curves over ﬁnite ﬁelds of
small characteristic [CDV06], which is how I got acquainted with the world of smooth
curves in toric surfaces. I wish to thank my former supervisor Jan Denef for his enthu-
siastic introduction to this beautiful topic, and him and my collaborator Frederik Ver-
cauteren for their guidance over the ﬁrst hurdles. The direct provocation for the cur-
rently presented work was to gain a better understanding of to which curves exactly
our algorithm applies, a problem which I attacked together with John Voight. Later the
research diverged in the direction of linear systems on smooth curves in toric surfaces,
sparked by connections with tropical geometry [Bak08; CC12] and by recent work of
Kawaguchi [Kaw16]; here, most of the results were obtained in collaboration with Filip
Cools. I would like to thank John and Filip, and also my other coauthors Jeroen Demeyer,
Alexander Lemmens, Marco Streng and Damiano Testa for the fruitful collaboration. My
hope is that our work turns out useful for future algebraic geometers in verifying hy-
potheses and proving existence results, and as such contributes to Fulton’s qualiﬁcation
of toric geometry as a remarkably fertile testing ground for general theories [Ful93, Pref.].
Finally I would like to express my gratitude to my garant Raf Cluckers, for his stimulat-
ing and genuinely positive attitude, to Pierre Dèbes, Anne Moreau, Sam Payne, Josef
Schicho and Frank-Olaf Schreyer for willing to be part of the jury, and to my parents,
sister, brother in law, niece, and other family and friends, for their continuous support
and for the moments of much-welcomed relaxation.

1. Weakly nondegenerate curves as smooth curves in toric surfaces
(Chapters 4 and 5)

To every two-dimensional lattice polygon ∆ one can associate a projectively embedded
toric surface X∆ over k, obtained by taking the Zariski closure of the image of

ϕ∆ : T
2 ↪→ P#(∆∩Z2)−1 : (x, y) ↦→ (xiyj)(i,j)∈∆∩Z2.

If f ∈ k[x±1, y±1] is weakly ∆-nondegenerate then ϕ∆(Uf ) closes along with ϕ∆(T2) to
the smooth hyperplane section ∑

(i,j)∈∆∩Z2 cijXi,j = 0

of X∆, where Xi,j denotes the projective coordinate corresponding to the lattice point
(i, j). Thus, weakly ∆-nondegenerate Laurent polynomials f allow for an explicit smooth
complete model of Uf , which we denote by Cf .

Remark. Informally one can think of a weakly ∆-nondegenerate Laurent polynomial f
as deﬁning a smooth curve in T2, the singularities of whose planar completion are ‘no
worse’ than what ∆ prescribes and that therefore can be resolved using toric geometry.

When viewed as a divisor on X∆ the curve Cf is Cartier and very ample. From the
theory of toric varieties [CLS11; Ful93] it follows that Cf is linearly equivalent to a torus-
invariant divisor D, to which one can naturally associate a polygon PD ⊆ R2. It turns out
that this polygon is precisely ∆, modulo translation over an element of Z2 that depends
 xi

on the speciﬁc choice of D; this issue will be ignored from now on. Conversely consider
a smooth complete Cartier curve C on a toric surface X ⊇ T2, where to avoid certain
pathologies we assume that C is non-rational. Consider a torus-invariant divisor D ∼ C
and let PD ⊆ R2 be the associated polygon. Then this is automatically a two-dimensional
lattice polygon and C ∩T2 is deﬁned by a weakly PD-nondegenerate Laurent polynomial
f ∈ k[x±1, y±1].
In this sense weak nondegeneracy is a geometrically more pleasing notion than non-
degeneracy, which on top of smoothness requires that the curve intersects toric inﬁnity
X \ T2 transversally. For instance, while dΣ-nondegenerate Laurent polynomials merely

nondegenerate
but not nondegenerate
but not nondegenerate
 weakly nondegenerate but not nondegenerate
(allowed to pass through non-singular T
0’s,
tangency allowed to T
1’s)

correspond to smooth degree d curves in P2, dΣ-nondegeneracy moreover forces the
curve not to pass through the coordinate points and to be non-tangent to the coordi-
nate axes. On the other hand every weakly dΣ-nondegenerate curve (i.e. when consid-
ered modulo birational equivalence) is also dΣ-nondegenerate because using an auto-
morphism of P2 one can enforce appropriate intersection behaviour with the coordinate
axes. This trick does not always work: there exist two-dimensional lattice polygons ∆
along with weakly ∆-nondegenerate curves that are genuinely non-∆-nondegenerate.
An example is given in Chapter 5.

Remark on the non-Cartier case. Let C be a smooth complete non-rational curve on a toric
surface X ⊇ T2 which is not necessarily Cartier. Let D be a linearly equivalent torus-
invariant divisor. Then PD need not be a lattice polygon, which complicates matters
slightly. Nevertheless C is weakly nondegenerate, as one can show that C ∩ T2 is deﬁned
by a weakly conv(PD ∩ Z2)-nondegenerate Laurent polynomial.

Khovanskii’s proof of Baker’s formula for the genus g(Uf ) essentially amounts to an
application of the adjunction formula to the inclusion Cf ⊆ X∆, in combination with
a well-known combinatorial interpretation for the Riemann-Roch space associated to a
torus-invariant divisor D (the statement involves the polygon PD). In fact this yields
much ﬁner information than merely g(Uf ) = g(Cf ) = #(∆(1) ∩ Z2): it entails an explicit
canonical divisor K∆ on Cf that satisﬁes

H 0(Cf , K∆) = ⟨xiyj⟩(i,j)∈∆(1)∩Z2,

where x, y are viewed as functions on Cf through ϕ∆. This leads to the following classi-
ﬁcation based on dim ∆(1):

(i) Cf is rational if and only if ∆(1) = ∅.

xii

(ii) Cf is elliptic if and only if dim ∆(1) = 0.

(iii) Cf is hyperelliptic if and only if dim ∆(1) = 1.

(iv) If dim ∆(1) = 2 then the canonical embedding ‘factors’ through ϕ∆(1) and therefore
the canonical image Ccan
f is contained in the toric surface

X∆(1) ⊆ P#(∆(1)∩Z2)−1.

Even though these four claims are easy consequences of Khovanskii’s proof method,
as far as we know, prior to our articles the only explicit mention of the last two state-
ments can be found in Koelman’s (unpublished) Ph.D. thesis see [Koe91, Lem. 3.1.3 and
Lem. 3.2.9] and are therefore not well-known. We hope that our work helps to publicize
these interesting facts.
Chapters 4 and 5 contain a number of new accompanying facts, one of which is the
following geometric interpretation in case (iv) of ∆max, the maximal polygon with respect
to inclusion whose interior polygon equals ∆(1) — from a combinatorial perspective the
existence of such a maximum was observed by Koelman [Koe91, §2.2] and rediscovered
by Haase and Schicho [HS09] (see also the next section).

Lemma 2. If in case (iv) one considers a torus-invariant divisor on X∆(1) that is linearly equiv-
alent to Ccan
f , then its associated polygon equals ∆max.

Another contribution is an explicit minimal set of generators for the ideal I(Ccan
f ) of Ccan
f ,
again in case (iv). These are obtained by starting from a minimal set of generators for the
ideal of X∆(1), consisting of

(
g − 1
2
 ) − 2 vol(∆
(1)) quadrics and { 0 if ∆(1) ̸∼= Υ
1 if ∆(1) ∼= Υ cubics

(here ∼= denotes unimodular equivalence). Extending this to a minimal set of generators
for the canonical ideal of Cf can be done following a so-called rolling factors recipe. This
amounts to adding





 1 quartic if ∆(1) ∼= Σ,
g − 3 cubics if ∆(2) = ∅ but ∆(1) ̸∼= Σ,
#(∆(2) ∩ Z2) quadrics if ∆(2) ̸= ∅

(where ∆(2) abbreviates ∆(1)(1)). For instance in the last case the quadrics are

Qw = ∑

(i,j)∈∆∩Z2 cijXuij Xvij ∈ k[ Xi,j | (i, j) ∈ ∆(1) ∩ Z
2 ]

where w runs through ∆(2) ∩ Z2 and uij, vij are chosen such that (i, j) − w = (uij − w) +
(vij − w). For more details we refer to Chapter 4. We have implemented the resulting
algorithm in Magma [BCP97], allowing for a quick computation of a minimal set of gen-
erators for the canonical ideal of any concretely given weakly nondegenerate curve of
genus up to about 100. For general curves within this range this is currently an infeasible
task.
 xiii

2. The combinatorics of lattice polygons (Chapters 2, 3 and 5)

Even though there is always some toric geometric motivation in the background, sev-
eral parts of the presented chapters are purely combinatorial. Mostly these parts are
concerned with the question of how the operation ∆ ↦→ ∆(1) affects certain combinatorial
invariants, i.e. quantities that do not change when applying a unimodular transformation.
One example of such a combinatorial invariant is the number of lattice points on the
boundary, in which case the question amounts to relating #(∂∆∩Z2) to #(∂∆(1)∩Z2). An
answer was obtained through a beautiful application of Poonen and Rodrigues-Villegas’
12 theorem, by Haase and Schicho [HS09], from whom we have copied the superscript
notation (1). We omit a detailed statement. Indirectly their work also treats the number of
lattice points in the interior #(∆◦ ∩Z2) = #(∆(1) ∩Z2), which in view of Baker’s theorem
is called the genus. An important property of the genus is given by the following result:

Lemma 3. Up to unimodular equivalence the number of lattice polygons having a given genus
g ≥ 1 is ﬁnite.

See e.g. [LZ91]. An alternative proof can be found in Chapter 2.
For our needs, besides the genus the most important combinatorial invariant is the
lattice width, which is deﬁned as follows. For each primitive vector v = (a, b) ∈ Z2

deﬁne the width w(∆, v) to be the smallest integer d for which there exists an m ∈ Z such
that m ≤ aj − bi ≤ m + d for all (i, j) ∈ ∆, (1)

as illustrated below. This deﬁnition assumes that ∆ is a non-empty lattice polygon; one

...
 ∆ v

m
m + 1

m + d

lets w(∅, v) = −1. The lattice width lw(∆) is then deﬁned as minv w(∆, v). Alternatively,
if ∆ ̸= ∅ then lw(∆) is the minimal height d ∈ Z≥0 of a horizontal strip R × [0, d] in which
∆ can be mapped using a unimodular transformation. The question of relating lw(∆) to
lw(∆(1)) has the following surprisingly simple answer: if ∆ is two-dimensional then

lw(∆) = { lw(∆(1)) + 3 if ∆ ∼= dΣ for some d ≥ 2,
lw(∆(1)) + 2 if not. (2)

Note that this allows one to compute lw(∆) recursively; we have implemented this in
Magma.

Remark. This implies that lw(∆) = lw(∆max) whenever ∆(1) is two-dimensional, except
possibly if ∆max ∼= dΣ for some d ≥ 4.

A proof of the recursive formula (2) can be found in the paper [CC12], which is not
considered part of this thesis because independently a more complete result, discussing

xiv

the concrete primitive vectors v for which lw(∆) = w(∆, v), was obtained by Lubbes
and Schicho [LS11, Thm. 13]. Note that such vectors always arise in pairs ±v. One can
prove [DMN12] that the number of pairs realizing the lattice width is at most 4 as soon
as ∆ is two-dimensional. These and some accompanying properties are reported upon in
more detail in Chapter 5, which also includes a number of new facts and introduces the
following reﬁned quantity.

Deﬁnition 4. The multi-set of width invariants of a lattice polygon ∆ with non-empty interior
associated to a primitive v ∈ Z2 is deﬁned as

E(∆, v) = { −1 + #{ (i, j) ∈ ∆(1) ∩ Z
2 | aj − bi = m + ℓ } ∣
∣
∣ ℓ = 1, . . . , d − 1 } ,

where m, d ∈ Z are the values from (1). (Its cardinality is w(∆, v) − 1, counting multiplicities.)

Using a unimodular transformation if needed one can always assume that v = (1, 0)
and ∆ ⊆ R × [0, w(∆, v)]. In this setting the width invariants are given by the multi-set
{Ej}j=1,...,w(∆,v)−1, with Ej the number of lattice points minus one that are contained in
∆(1) at height j.

Example. Consider dΣ for some d ≥ 3. Then lw(dΣ) = d and there are three pairs of
primitive vectors realizing the lattice width, namely ±(1, 0), ±(0, 1), ±(1, −1). For each
of these vectors v the multi-set E(dΣ, v) of width invariants equals {−1, 0, 1, 2, . . . , d −
4, d − 3}. On the other hand one veriﬁes that w(dΣ, (1, 1)) = 2d and E(dΣ, (1, 1)) =

w(dΣ, (1, 0)) = d w(dΣ, (1, 1)) = 2d

{−14, 04, 14, 24, . . . , ⌊(d − 6)/2⌋4, ⌊(d − 4)/2⌋ϵ}, where the superscripts denote the multi-
plicities and ϵ = 1 or 3, depending on whether d is odd or even, respectively.

Note that the width invariants are elements of Z≥−1. In Chapter 5 it is shown that if v
realizes the lattice width and ∆ ̸∼= dΣ for any d ≥ 3, then the width invariants associated
to v are all non-negative.
Chapter 3 introduces the following generalization of the lattice width:

Deﬁnition 5. The lattice size lsX (∆) of a non-empty lattice polygon ∆ with respect to a given
set X ⊆ R2 having positive Jordan measure is deﬁned as the minimal d ∈ Z≥0 such that ∆ can
be mapped inside dX by means of a unimodular transformation.

For X = R × [0, 1] one recovers the lattice width. The chapter focuses entirely on X = Σ
and X = □ := □1,1. In order to state our main results relating lsX (∆) to lsX (∆(1)) it is
convenient to deﬁne lsΣ(∅) = −2 and ls□(∅) = −1.

Theorem 6. Let ∆ be a two-dimensional lattice polygon. Then lsΣ(∆) = lsΣ(∆(1)) + 3, except
in the following situations:
 xv

• ∆ ∼= conv{(0, 0), (a, 0), (b, 1), (0, 1)} where a = b = 1 or 2 ≤ a ≥ b ≥ 0, in which case
ls□(∆(1)) = −2 while
 lsΣ(∆) = { a + 1 if a = b
a if a > b.

• ∆ ∼= 2Σ in which case lsΣ(∆(1)) = −2 while lsΣ(∆) = 2.

• ∆ ∼= ∆4,2 in which case lsΣ(∆(1)) = 0 while lsΣ(∆) = 4.

• ∆ ∼= □a,b for a, b ≥ 2, in which case lsΣ(∆(1)) = a + b − 4 while lsΣ(∆) = a + b.

• There exist parallel edges τ ⊆ ∆ and τ ′ ⊆ ∆(1) whose supporting lines are at integral
distance 1 of each other, such that

#(τ ∩ Z2) − #(τ ′ ∩ Z2) ≥ 4,

in which case lsΣ(∆(1)) = #(τ ′ ∩ Z2) and lsΣ(∆) = #(τ ∩ Z2).

As in the case of the lattice width, this result can be converted into a recursive algorithm
for computing lsΣ(∆) in practice, which we have again implemented in Magma. From the

unimodular
transformation

ϕ

∆
 (Illustration of lsΣ(∆).)
 ϕ(∆)

dΣ

proof of the foregoing theorem one sees that Schicho’s algorithm for simplifying rational
surface parametrizations [Sch03a] works optimally.

Theorem 7. Let ∆ be a two-dimensional lattice polygon. Then ls□(∆) = ls□(∆(1)) + 2, except
in the following situations:

• ∆ ∼= conv{(0, 0), (a, 0), (b, 1), (0, 1)} where 2 ≤ a ≥ b ≥ 0, in which case ls□(∆(1)) =
−1 while ls□(∆) = a.

• ∆ ∼= 2Σ in which case ls□(∆(1)) = −1 while ls□(∆) = 2.

• ∆ ∼= 3Σ, ∆3,2, conv{(0, 0), (3, 0), (2, 1)(0, 2)} or conv{(0, 0), (3, 0), (1, 2), (0, 2)} in which
case ls□(∆(1)) = 0 while ls□(∆) = 3.

• ∆ ∼= ∆4,2 in which case ls□(∆(1)) = 0 while ls□(∆) = 4.

• There exist parallel edges τ ⊆ ∆ and τ ′ ⊆ ∆(1) whose supporting lines are at integral
distance 1 of each other, such that

#(τ ∩ Z2) − #(τ ′ ∩ Z2) ≥ 3,

in which case ls□(∆(1)) = #(τ ′ ∩ Z2) and ls□(∆) = #(τ ∩ Z2).

Again the resulting recursive method has been implemented in Magma. The proof of
the foregoing theorem has a remarkable byproduct: it turns out that the unimodular
transformation mapping ∆ inside ls□(∆) · □ can be chosen such that it also maps inside
R × [0, lw(∆)]. As a consequence:

xvi

Corollary 8. For each non-empty lattice polygon ∆ the set
{ (a, b) ∈ Z2
≥0 ∣
∣ a ≤ b and ∃∆′ ∼= ∆ with ∆′ ⊆ [0, a] × [0, b] }

has a minimum with respect to the product order on Z≥0 × Z≥0, namely (lw(∆), ls□(∆)).

We conclude by stressing that the map ∆ ↦→ ∆(1) is not surjective. In fact for a two-
dimensional lattice polygon Γ to be of the form ∆(1) for some larger lattice polygon ∆
is a rather restrictive property. The following criterion was proved by Haase and Schi-
cho [HS09]. Each edge τ ⊆ Γ lies on the boundary of a unique half-plane aτ X + bτ Y ≤ cτ
containing Γ, where aτ , bτ , cτ ∈ Z are chosen to satisfy gcd(aτ , bτ ) = 1. Consider the
polygon Γ(−1) = ⋂

τ (half-plane aτ X + bτ Y ≤ cτ + 1) ,

said to be obtained from Γ by moving out the edges. Then Γ = ∆(1) for some lattice
polygon ∆ if and only if Γ(−1) is a lattice polygon. If this is the case then one can simply
let ∆ = Γ(−1), and this is the maximal possible choice with respect to inclusion. In other
words if ∆ is a lattice polygon having a two-dimensional interior then ∆max = ∆(1)(−1).
For any lattice polygon ∆, a repeated application of ∆ ↦→ ∆(1) eventually leads to
a lattice polygon whose interior is at most one-dimensional. Such polygons have been
classiﬁed explicitly by Koelman [Koe91, §4]. Conversely, starting from these basic cases
one can algorithmically produce all lattice polygons up to a given genus by repeatedly
applying ∆ ↦→ ∆(−1), verifying Haase and Schicho’s criterion and making local tweaks
(clipping off vertices). The details can be found in Chapter 2, which comes along with
a Magma implementation by means of which we have produced a list containing ex-
actly one representative within each unimodular equivalence class of lattice polygons of
genus 1 ≤ g ≤ 30. This list is useful for testing hypotheses and detecting patterns; we
have mainly applied this to the study of syzygies of toric surfaces (and of smooth curves
therein) in Chapters 6 and 8. But there are also some purely combinatorial consequences
which seem interesting in their own right. For instance prior to our work the concrete
number of equivalence classes of lattice polygons of genus g ≥ 1 was unknown for g
as small as 3, even though asymptotically for g → ∞ it was shown to be O(exp(g1/3))
by Bárány [BT04]. Another consequence (albeit slightly indirect; see Chapter 2 for the
details) is:

Lemma 9. The minimal genus of a lattice 15-gon is 45.

This ﬁlls in the smallest open entry of a list whose study began with Arkinstall [Ark80].
Recently our data set was used to give tight bounds on the generalized Helly numbers of
Z2; see [Ave+15].

3. The number of moduli (Chapter 1)

The generic Laurent polynomial that is supported on a given two-dimensional lattice
polygon ∆ ⊆ R2 is ∆-nondegenerate, and weakly ∆-nondegenerate in particular. As a
consequence, if the man in the street would be asked to scribble down a random curve,
the outcome is likely to be weakly nondegenerate, and most curves that can be found in
the wild are indeed of this kind, including all hyperelliptic curves and smooth curves in
P2 as we have seen above, but also all trigonal curves, Ca,b curves, and several more well-
studied families. For a moment this might tempt one to conclude that the generic curve,
in the proper moduli-theoretic sense, is weakly non-degenerate. But a second thought
quickly reveals that this is far from true. Some obstructions are:
 xvii

• The moduli space Mg of curves of genus g is not unirational for g ≥ 22 [Far09].

• The gonality of a weakly ∆-nondegenerate genus g curve is bounded by lw(∆),
which is O(
√g) by [FTM74], while the general curve has gonality ⌊(g + 3)/2⌋ by
Brill-Noether theory. This was recently elaborated in detail by Smith [Smi15] who
proved that weakly nondegenerate curves cannot be Brill-Noether general from
g ≥ 7 onwards.

• The canonical ideal of a weakly nondegenerate curve contains (many) quadratic
binomials, i.e. quadrics of rank 3 or 4.

The latter obstruction seems best-suited for proving that a certain concretely given curve
C/k is not weakly nondegenerate.
In Chapter 1 we try to obtain a more precise understanding of which curves are
weakly nondegenerate. For curves of genus at most four, we prove:

Theorem 10. Every curve C/k of genus g ≤ 4 is weakly ∆-nondegenerate for exactly one choice
of ∆ among the lattice polygons listed below.

Σ ∆3,2 ∆5,2 ∆7,2

4Σ ∆9,2 ∆6,3 □3,3.

(The polygons referred to in the statement of Theorem 10.)

The theorem remains true upon replacement of ‘weakly ∆-nondegenerate’ by ‘∆-nonde-
generate’. Also, slightly modiﬁed versions hold over ﬁelds that are not necessarily alge-
braically closed. For instance over ﬁnite ﬁelds the theorem is true except when C is of
genus 4 and canonically embeds into an elliptic quadric in P3; see also [CV10].
The main result of Chapter 1 is a determination of the number of moduli of the family
of weakly nondegenerate curves, through a parameter count that builds on Haase and
Schicho’s aforementioned work [HS09] and a combinatorial description of the automor-
phism group of X∆ due to Bruns and Gubeladze [BG09]. For a two-dimensional lattice
polygon ∆, we denote by M∆ the Zariski closure of the locus inside Mg of all weakly
∆-nondegenerate curves; these spaces had already been introduced and studied by Koel-
man [Koe91, §2]. For each g ≥ 1 let

Mwnd
g = ⋃

∆ for which
♯(∆(1)∩Z2)=g
 M∆,

which in view of Lemma 3 is a ﬁnite union because unimodularly equivalent lattice poly-
gons give rise to the same curves. We show:

xviii

Theorem 11. One has 



 dim Mwnd
1 = 1,
dim Mwnd
2 = 3,
dim Mwnd
3 = 6,
dim Mwnd
7 = 16,
dim Mwnd
g = 2g + 1 if g ≥ 4 and g ̸= 7.

In particular from genus ﬁve on the generic curve is not weakly nondegenerate (let alone
nondegenerate). For g ≥ 4 a top-dimensional subvariety of Mwnd
g is given by the trigonal
locus Mtri
g , except when g = 7, where the trigonal curves are beaten by the trinodal plane
sextics. Recently Brodsky, Joswig, Morrison and Sturmfels used a similar approach to
obtain the same moduli count for tropical plane curves [Bro+15].

4. Gonality, Clifford index, and related invariants (Chapters 3 and 5)

This section adds a number of entries to the geometry-combinatorics dictionary for weak-
ly nondegenerate curves, related to linear systems. The main reference for the results
presented below is Chapter 5. The most important new entry is the gonality, which is
deﬁned as the minimal possible degree of a non-constant rational map to P1:

Theorem 12. Let ∆ be a two-dimensional lattice polygon and let f ∈ k[x±1, y±1] be a weakly ∆-
nondegenerate Laurent polynomial. Then the gonality of Uf equals lw(∆(1))+2, unless ∆(1) ∼= Υ
in which case it is lw(∆(1)) + 1.

This theorem arises as a consequence of a stronger result. Let f be a weakly ∆-nondegene-
rate Laurent polynomial and let v = (a, b) ∈ Z2 be a primitive vector. We deﬁne the com-
binatorial pencil gv on Cf associated to v as the trace of the linear system on X∆ swept
out by T2 → T1 : (x, y) ↦→ xayb. Notice that gv = g−v is of degree w(∆, v), in other words
it concerns a g1
w(∆,v).

Remark. In almost all cases gv equals the basepoint free pencil associated to the map
Uf → T1 : (x, y) ↦→ xayb. However when ∆(f ) ⊊ ∆, in certain cases this needs to be
extended by basepoints.

Our strengthening of Theorem 12 reads as follows:

Theorem 13. Let ∆ be a two-dimensional lattice polygon such that ∆(1) is not unimodularly
equivalent to any of the following:

∅, (d − 3)Σ (for some d ≥ 3), Υ, 2Υ, Γ
5
1, Γ
5
2, Γ
5
3.

If char k > 0 then we also exclude Γ12. Let f ∈ k[x±1, y±1] be a weakly ∆-nondegenerate Laurent
polynomial. Then every linear pencil on Cf which realizes the gonality is combinatorial.

One byproduct of the above theorem is that besides the gonality itself, one also knows the
number of gonality pencils by merely looking at the Newton polygon, except possibly
when ∆(1) ∼= Υ in which case Uf is always tetragonal but the number of gonality pencils
depends on the concrete choice of f (it is either 1 or 2), and except possibly when char k >
0 and ∆(1) ∼= Γ12 where the situation is not fully understood. If ∆(1) = ∅ then there is a
unique gonality pencil. In the other exceptional cases ∆(1) ∼= (d − 3)Σ, 2Υ, Γ5
i the number
of gonality pencils can be shown to be inﬁnite.
 xix

(0, −1)
 (1, 0)

(0, 1)

(−1, 0) Γ5
1
 (0, −1) (1, −1)

(0, 1)

(−1, 0) Γ5
2
 (1, −1)

(0, 1)

(−1, −1)
 Γ5
3

(Polygons excluded in the statement of Theorem 13, corresponding to curves of genus 5.)

(−1, 0)

(−1, 1)
 (0, 3)
 (3, −1)
(2, −1)

(1, 2)

Γ
12

(Polygon excluded by Theorem 13 in positive characteristic, corresponding to curves of genus 12.)

Our main proof ingredient is a result due to Serrano [Ser87] which given a curve C
inside some surface X, provides sufﬁcient conditions under which a morphism C → P1

can be extended to a morphism X → P1. We stress that this approach, and as a matter
of fact the entire statement of Theorem 13, is due to Kawaguchi [Kaw16], modulo two
relaxations:

• Kawaguchi made the technical assumption that Uf is not birationally equivalent to
a smooth plane curve of degree d ≥ 5. We got rid of this condition, essentially by
invoking the formula (2) at the proof step where this assumption was used.

• Both Kawaguchi and we proved these statements subject to char k = 0. However
one can obtain the same results in positive characteristic by using [Ser87, Rmk. 3.12],
which discusses sufﬁcient conditions for the extension of separable morphisms
from curves to rational surfaces, in combination with the fact that every morphism
Cf → P1 decomposes into a purely inseparable part and a separable part

Cf → CFrob
f → P1,

along with the observation that Frobenius preserves weak nondegeneracy. This ap-
proach does not work when ∆(1) ∼= Γ12, in which case one of the extra conditions
mentioned in [Ser87, Rmk. 3.12] is violated. Therefore Γ12 pops up as a new excep-
tion, although this may well be just a proof artefact (unlike the other exclusions,
which are really needed). More details will be included in the forthcoming version
of [CT].

In addition, our database of polygons having small genus allowed us to skip a large and
combinatorially tedious part of Kawaguchi’s proof.
Using the same techniques we can deduce an analogous result for near-gonal pencils,
by which we mean base-point free linear pencils of degree γ + 1, where γ is the gonality
of Uf :

Theorem 14. Let ∆ be a two-dimensional lattice polygon such that

lsΣ(∆
(1)) ≥ lw(∆
(1)) + 2

xx

and such that ∆(1) ̸∼= 2Υ, 3Υ, Γ7, Γ8. If char k > 0 then we also exclude Γ10. Let f ∈ k[x±1, y±1]
be a weakly ∆-nondegenerate Laurent polynomial. Then every near-gonal pencil on Cf is combi-
natorial.
 (0, −1)
 (2, 0)

(0, 1) (1, 1)

(−1, −1)
 Γ
7
 (0, −1)
 (3, 0)

(0, 1) (1, 1)

(−1, −1)
 Γ8

(Polygons excluded in the statement of Theorem 14, corresponding to curves of genus 7 and 8.)

(−2, 0)
 (0, 2)
 (2, −1)
(1, −1)

(1, 1)

Γ
10

(Polygon excluded by Theorem 14 in positive characteristic, corresponding to curves of genus 10.)

Again the exclusion of Γ10 might be a proof artefact; as explained in Chapter 5 the other
exclusions are necessary. Also, one can verify that the list of excluded polygons is a strict
extension of its counterpart from Theorem 13.
In principle it should be possible to obtain similar statements for basepoint free g1
γ+n’s
with n = 2, 3, . . ., but we expect the proof to become increasingly case-distinctive and the
number of excluded polygons to grow. Nevertheless for small n it might be worth the try,
in order to gain some feeling on how dim W 1
γ+n can grow with n, a question which has
sparked much interest in view of connections with Green’s canonical syzygy conjecture,
through Aprodu’s linear growth condition [Apr05].
Another entry to the dictionary is given by the scrollar invariants associated to a com-
binatorial pencil (e.g. any gonality pencil in the case of a polygon that is non-exceptional
for Theorem 13). The scrollar invariants associated to a linear pencil g1
d on a non-hyper-
elliptic genus g curve C/k are deﬁned as follows. View the g1
d as a 1-dimensional family
of effective divisors D on the canonical model Ccan
f ⊆ Pg−1 and let S ⊆ Pg−1 be the ruled
variety obtained by taking the union of all linear spans ⟨D⟩. A theorem by Eisenbud and
Harris [EH87, Thm. 2] states that S is a rational normal scroll. The scrollar invariants
associated to g1
d are deﬁned as the multi-set of invariants (= the degrees of the spanning
rational normal curves) of this scroll. If our g1
d is complete and basepoint free then the
⟨D⟩’s are planes of dimension d − 2, and S is of dimension d − 1. In this case the scrollar
invariants 0 ≤ e0 ≤ e1 ≤ . . . ≤ ed−1 satisfy ed−1 ≤ (2g − 2)/d.

Theorem 15. Let ∆ be a lattice polygon such that ∆(1) is two-dimensional. Let v ∈ Z2 be a
primitive vector and let f ∈ k[x±1, y±1] be a weakly ∆-nondegenerate Laurent polynomial. Then
the multi-set of scrollar invariants of Cf with respect to gv equals the multi-set of non-negative
width invariants of ∆ with respect to v.

The proof can be found in Chapter 5 and has the following corollary:

Corollary 16. The rank of the complete linear system spanned by gv equals the number of negative
width invariants (counting multiplicities) plus one. In particular gv is complete if and only if all
width invariants are non-negative.
 xxi

Example. Consider dΣ for some d ≥ 4 along with the primitive vector v = (1, 0). Recall
from Section 2 that E(dΣ, v) = {−1, 0, 1, 2, . . . , d − 3}. By Theorem 15 the scrollar invari-
ants associated to g(1,0) are {0, 1, 2, . . . , d − 3}. By Corollary 16 our g(1,0) is a subsystem
of a g2
d, hence it is not complete. But this just conﬁrms a well-known fact, because Cf is a
smooth projective degree d curve in P2 and g(1,0) is cut out by the pencil of lines through
a ﬁxed point of the plane. By varying the point one obtains the g2
d.

Example (Maroni invariants). Consider a lattice polygon ∆ with lw(∆) = 3 and ∆ ̸∼= 3Σ.
Then up to unimodular equivalence ∆(1) is of the form below, for certain integers 1 ≤
a ≥ b ≥ 0. Notice that weakly ∆-nondegenerate Laurent polynomials f ∈ k[x±1, y±1]

(a, 0)

(b, 1)(0, 1)

(0, 0)
 ∆(1)

give rise to trigonal curves Cf of genus g = #(∆(1) ∩ Z2) = a + b + 2. Then g(1,0) is a go-
nality pencil and the corresponding scrollar invariants are seen to be {a, b}; if a = 1 then
there may exist other combinatorial gonality pencils but the associated scrollar invariants
are the same. The numbers a and b are classical invariants called the Maroni invariants1

of Cf . Every trigonal curve arises as a weakly ∆-nondegenerate curve with ∆ a lattice
polygon of the above form. A fun fact is that the well-known bound a ≤ (2g − 2)/3 which
is usually proven through the Riemann-Roch theorem, can also be obtained in a purely
combinatorial way, using Haase and Schicho’s criterion for ∆(1) to be an interior polygon.

Another observation is that Theorem 13 can be combined with results of Coppens
and Martens [CM91] to obtain combinatorial interpretations for the Clifford index and
the Clifford dimension, which are deﬁned for curves of genus g ≥ 4 only: the Clifford
index is

min{ d − 2r | Cf carries a divisor D with |D| = gr
d and h0(Cf , D), h
0(Cf , K∆ − D) ≥ 2 }

which is a non-negative integer due to Clifford’s theorem. The Clifford dimension is the
smallest r for which the minimum is realized; this concept was introduced in [Eis+89].
Coppens and Martens assume char k = 0; we inherit this condition since it is not clear to
us how to circumvent it.

Theorem 17. Let ∆ be a two-dimensional lattice polygon and let f ∈ k[x±1, y±1] be a weakly
∆-nondegenerate Laurent polynomial. Assume that #(∆(1) ∩ Z2) ≥ 4 and char k = 0. Then:

• The Clifford index of Uf equals lw(∆(1)), unless ∆(1) ∼= (d − 3)Σ for some d ≥ 5, ∆(1) ∼=
Υ, or ∆(1) ∼= 2Υ, in which cases it is lw(∆(1)) − 1.

• The Clifford dimension of Uf equals 2 if ∆(1) ∼= (d − 3)Σ for some d ≥ 5, it equals 3 if
∆(1) ∼= 2Υ, and it is 1 in all other cases.

The possibility of combining Theorem 13 with [CM91] was already mentioned by Kawa-
guchi [Kaw16]. However we recall Kawaguchi’s assumption that Uf is not birationally
equivalent to a smooth plane curve of degree d ≥ 5, or in other words that the Clifford
dimension is different from 2. So by getting rid of this condition we end up with a more

1The existing literature is ambiguous at this point: sometimes one talks about a single Maroni invariant,
in which case one means either b or a − b.

xxii

complete and pleasing statement. The main ingredient taken from [CM91] is that there
always exist inﬁnitely many gonality pencils as soon as the Clifford dimension is at least
2. Because the number of combinatorial pencils is necessarily ﬁnite, through Theorem 13
this reduces one’s task to analyzing the exceptions ∆(1) ∼= ∅, (d − 3)Σ, Υ, 2Υ, Γ5
1, Γ5
2, Γ5
3.
For smooth plane curves, Coppens and Martens’ result is classical and holds in any char-
acteristic [Har86], allowing one to obtain the following corollary:

Corollary 18. Let ∆ be a lattice polygon with non-empty interior. Let f ∈ k[x±1, y±1] be weakly
∆-nondegenerate and assume that Uf is birationally equivalent to a smooth projective curve in
P2, say of degree d ≥ 3. Then ∆(1) ∼= (d − 3)Σ.

Therefore, in the case of smooth plane curves, one can view ∆(1) in some sense as a ge-
ometric invariant. We refer to this property as intrinsicness of the interior polygon and
will state a few more results of this kind in Section 8.

Remark. Stated more geometrically, this means that if a toric surface X contains a smooth
projective curve C that is abstractly isomorphic to a smooth plane projective curve, then
there exists a toric blow-down π : X → P2 such that π|C : C → P2 is an embedding.

∆(1) gonality Clifford ind. Clifford dim.
(d − 3)Σ (for some d ≥ 5) d − 1 d − 4 2
Υ 3 1 1
2Υ 6 3 3
everything else lw(∆) lw(∆
(1)) 1

(Overview in char. 0 of combinatorial interpretations for gonality, Clifford index, Clifford dimension.)

A consequence of Theorems 12 and 17 is that the gonality and (if char k = 0) the Clif-
ford index and dimension of Uf depend on ∆ only, rather than on the speciﬁc choice
of our weakly ∆-nondegenerate Laurent polynomial f ∈ k[x±1, y±1]. This is an a priori
non-trivial fact that can be rephrased as constancy among the smooth curves in linear
systems of curves on toric surfaces. The existing literature contains other results of this
type, which are usually stated in characteristic zero only. For instance recent work of
Lelli-Chiesa proves constancy of the gonality and the Clifford index for curves in cer-
tain linear systems on other types of rational surfaces [LC13]. An important theorem by
Green and Lazarsfeld states that constancy of the Clifford index holds in linear systems
on K3 surfaces [GL87], although here constancy of the gonality is not necessarily true.
In the next section we will state a constancy result for the entire canonical graded Betti
table (which subject to Green’s canonical syzygy conjecture is a vast generalization of the
Clifford index).
We end this section with a brief discussion (more details to be found in Chapter 3)
of two other invariants that we have put to a combinatorial analysis, albeit with less
conclusive results:

• The minimal degree s2(Uf ) of a possibly singular curve in P2 that is birationally
equivalent to Uf ; equivalently this asks for the minimal degree of a simple linear
system of rank 2.

• The minimum s1,1(Uf ) of
{ (a, b) ∈ Z2
≥0 ∣
∣ a ≤ b and ∃ C ⊆ P1 × P1 of bidegree (a, b) with C ≃ Uf } (3)
 xxiii

where ≃ denotes birational equivalence. The minimum is taken with respect to the
lexicographic order on Z≥0 × Z≥0 (but see the ‘open question’ at the end of this
section).

Unfortunately we can only provide upper bounds, and leave it as an unsolved problem
whether these statements are sharp. In particular we do not know whether the quantities
s2(Uf ) and s1,1(Uf ) are independent of the concrete choice of f ∈ k[x±1, y±1].

Theorem 19. Let ∆ be a two-dimensional lattice polygon and let f ∈ k[x±1, y±1] be a weakly
∆-nondegenerate Laurent polynomial. Then s2(Uf ) ≤ lsΣ(∆(1)) + 3. If ∆(1) ∼= dΥ for some
d ≥ 1 then the sharper bound s2(Uf ) ≤ lsΣ(∆(1)) + 2 applies.

Theorem 20. Let ∆ be a two-dimensional lattice polygon and let f ∈ k[x±1, y±1] be a weakly ∆-
nondegenerate Laurent polynomial. Then s1,1(Uf ) ≤ (lw(∆(1)) + 2, ls□(∆(1)) + 2). If ∆(1) ∼= Υ
then the sharper bound s1,1(Uf ) ≤ (3, 4) applies.

Remark that by Theorem 12 the ﬁrst components of the upper bounds stated in Theo-
rem 20 are equal to the gonality. Therefore this part of the statement is optimal and one
sees that the bounds necessarily hold with respect to the product order on Z≥0 × Z≥0.
In particular, if it is indeed true that Theorem 20 is always sharp, then the set (3) always
admits a minimum with respect to the product order. Please compare this to Corollary 8,
which can be viewed as a combinatorial analogue of this statement.

Open question. As an even wilder shot in the dark, we wonder whether it is true for every
algebraic curve C/k (i.e. not necessarily weakly nondegenerate) that the set of bidegrees
(a, b) with a ≤ b of curves in P1 × P1 that are birationally equivalent to C admits a mini-
mum with respect to the product order on Z≥0 × Z≥0.

5. Canonical graded Betti numbers (Chapters 6, 7 and 8)

Let ∆ be a lattice polygon with two-dimensional interior and let f ∈ k[x±1, y±1] be a
weakly ∆-nondegenerate Laurent polynomial. Recall from Section 1 that Cf ⊆ X∆ is
non-hyperelliptic and that its canonical model satisﬁes

Ccan
f ⊆ X∆(1) ⊆ Pg−1 = Proj S∆(1) (4)

where S∆(1) = k[ Xi,j | (i, j) ∈ ∆(1) ∩ Z2 ] and g = #(∆(1) ∩ Z2) denotes the genus of Cf .
In this section we report on a combinatorial analysis of the Betti numbers βij appearing
in a minimal free resolution of the homogeneous coordinate ring of Ccan
f as a graded
S∆(1)-module:

· · · → ⊕

q≥2 S∆(1)(−q)
β2,q → ⊕

q≥1 S∆(1)(−q)β1,q → ⊕

q≥0 S∆(1)(−q)
β0,q → S∆(1)⧸I(Ccan
f ) → 0.

These numbers are usually gathered in what is called the canonical graded Betti table
of Cf , by writing βp,p+q in the pth column and the qth row. Alternatively, and often
more conveniently, this entry equals the dimension of the Koszul cohomology space
Kp,q(Cf , K∆). The canonical graded Betti table is known to be of the form

0 1 2 3 . . . g − 4 g − 3 g − 2
0 1 0 0 0 . . . 0 0 0
1 0 a1 a2 a3 . . . ag−4 ag−3 0
2 0 ag−3 ag−4 ag−5 . . . a2 a1 0
3 0 0 0 0 . . . 0 0 1,
 (5)

xxiv

where omitted entries are understood to be zero. If one assumes Green’s canonical
syzygy conjecture [Gre84], the settlement of which is arguably the most important un-
solved problem concerning linear series on algebraic curves, then the canonical graded
Betti table is a vast generalization of the Clifford index. Indeed, Green’s conjecture pre-
dicts that the latter is equal to min{ ℓ | ag−ℓ ̸= 0 } − 2.

Remark. Assume that char k = 0. If X∆(1) carries an anticanonical pencil, or equivalently
if the polygon P−K associated to an anticanonical torus-invariant divisor −K on X∆(1)
contains at least two lattice points, then one can invoke a result of Lelli-Chiesa [LC13] to
settle Green’s conjecture for all weakly ∆-nondegenerate curves. This includes the cases
where X∆(1) is Gorenstein and weak Fano, which are discussed further down. The details
of these claims are explained in Chapter 8.

Remark. It is known that Green’s conjecture may fail over ﬁelds of very small positive
characteristic [Sch03b], but we do not know of any weakly nondegenerate counterexam-
ples.

Having a combinatorial description of the Clifford index at hand (at least if char k = 0,
see Theorem 17), it is a natural step to look for a similar description of the entire canonical
Betti table. At this moment this seems to be an infeasible task, both from a combinatorial
and a geometric perspective. In view of (4) we hope for an explicit relationship with the
graded Betti table of X∆(1), which is of the form

0 1 2 3 . . . g − 4 g − 3
0 1 0 0 0 . . . 0 0
1 0 b1 b2 b3 . . . bg−4 cg−3
2 0 cg−3 cg−4 cg−5 . . . c2 c1.
 (6)

Concretely, we distill the following three research questions, each of which we leave
unanswered in their general form, although we can offer several partial results:

(i) What would such an explicit relationship look like?

The inclusion (4) gives rise to an exact sequence

0 −→ bℓ −→ aℓ −→ cℓ µℓ,f
−→ cg−1−ℓ −→ ag−1−ℓ −→ bg−1−ℓ −→ 0 (7)

for each value of ℓ = 1, 2, . . . , g − 2. Here we abusingly write the dimensions of the
Koszul cohomology spaces, rather than the spaces themselves, and it is understood
that ag−2 = bg−2 = cg−2 = 0. The map µℓ,f is a morphism between two cohomol-
ogy spaces associated to X∆(1) that is induced by multiplication by f ; we refer to
Chapter 8 for the precise construction. This shows that aℓ = bℓ + cℓ − dim im µℓ,f ,
and the question reduces to a determination of the last term. Our main theorem is
that µℓ,f = 0 in the cases where X∆(1) is Gorenstein and weak Fano.

Theorem 21. Let ∆ be a lattice polygon with two-dimensional interior. Let f ∈ k[x±1, y±1]
be a weakly ∆-nondegenerate Laurent polynomial and let g = #(∆(1) ∩ Z2). Denote
by a1, a2, . . . , ag−3 the canonical graded Betti numbers of Cf as in (5), and similarly let
b1, c1, b2, c2, . . . , bg−3, cg−3 be the graded Betti numbers of X∆(1) as in (6). If X∆(1) is
Gorenstein and weak Fano then for all ℓ = 1, 2, . . . , g − 3 we have aℓ = bℓ + cℓ.

Being Gorenstein and weak Fano has an easy combinatorial interpretation: it means
that the convex hull of the primitive inward pointing normal vectors to the edges
 xxv

is a reﬂexive polygon (= a lattice polygon of genus one). An example is depicted
below. This is a rather strong condition, but we note that Theorem 21 applies to

∆(1)
 and take
convex hull

attach to origin

(Illustration of the Gorenstein weak Fano property from the combinatorial viewpoint.)

most of our introductory examples, including the cases where ∆ ∼= dΣ for some
d ≥ 4, where ∆ ∼= dΥ for some d ≥ 2, where ∆ ∼= □a,b for some a, b ≥ 3, and so
on. Moreover, experimentally we observe that µℓ,f = 0 much more frequently than
under the Gorenstein weak Fano assumption. Of course, an obvious reason could
be that cℓ = 0 or cg−1−ℓ = 0: by Theorem 24 below we perfectly understand when
this happens. But often µℓ,f = 0 for reasons we do not know.

Example. In this example we let k be (the algebraic closure of) the ﬁnite ﬁeld F10007;
this is mainly for computational efﬁciency, we expect the same analysis to apply
over C. The toric surface X∆(1) over k corresponding to the interior polygon ∆(1)

shown below is Gorenstein but not weak Fano. One computationally veriﬁes that

(−1, 0)

(−1, 1)
 (0, 3)
 (3, −1)
(2, −1)

(1, 3)

Γ
14

the corresponding graded Betti table is

0 1 2 3 4 5 6 7 8 9 10 11
0 1 0 0 0 0 0 0 0 0 0 0 0
1 0 59 363 1100 2013 2310 1525 343 24 0 0 0
2 0 0 0 0 0 7 112 574 561 265 66 7,

while the canonical graded Betti table of Cf for an aimlessly chosen2 Laurent poly-
nomial f ∈ F10007[x±1, y±1] that is weakly ∆max-nondegenerate when considered
over k was found to be

0 1 2 3 4 5 6 7 8 9 10 11 12
0 1 0 0 0 0 0 0 0 0 0 0 0 0
1 0 66 429 1365 2574 2884 1637 350 24 0 0 0 0
2 0 0 0 0 24 350 1637 2884 2574 1365 429 66 0
3 0 0 0 0 0 0 0 0 0 0 0 0 1.

2We equipped the lattice points on the boundary of ∆max with the prime coefﬁcients
2, 3, 5, 7, 11, 13, 17, 19, starting at the left-most vertex and proceeding counterclockwise. The coefﬁcients
corresponding to the interior lattice points were chosen 0 in view of Lemma 23 below.

xxvi
 (The computation started from our explicit minimal set of generators for the canon-
ical ideal; see Section 2.) Thus for ℓ = 6 the exact sequence (7) reads

0 −→ 1525 −→ 1637 −→ 112 µ6,f
−→ 7 −→ 350 −→ 343 −→ 0,

implying that µ6,f = 0, and similarly one sees that µ7,f = 0. We do not understand
why, as this is not explained by Theorem 21. In all other cases µℓ,f = 0 because
either cℓ = 0 or cg−1−ℓ = 0.

Example. The same computer experiment, when applied to the polygon Γ12 from
Section 4, respectively resulted in the graded Betti tables

0 1 2 3 4 5 6 7 8 9 10
0 1 0 0 0 0 0 0 0 0 0 0
1 0 45 231 550 693 399 69 0 0 0 0
2 0 0 0 0 69 399 693 550 231 45 0
3 0 0 0 0 0 0 0 0 0 0 1

and 0 1 2 3 4 5 6 7 8 9
0 1 0 0 0 0 0 0 0 0 0
1 0 39 186 414 504 295 69 0 0 0
2 0 0 0 0 1 105 189 136 45 6.

Here one sees that the exact sequence (7) for ℓ = 5 reads:

0 −→ 295 −→ 399 −→ 105 µ5,f
−→ 1 −→ 69 −→ 69 −→ 0.

So µ5,f is not trivial in this case, but rather surjective onto its one-dimensional
codomain. In fact, ∆(1) is the only interior polygon for which we have observed
deviating behavior with respect to the formula aℓ = bℓ + cℓ, although we expect
more exceptions to pop up beyond the range of polygons that we have computed
(if not then Green’s conjecture would be violated, as explained at the end of this
section).

(ii) Is it true at all that the canonical graded Betti table of Cf only depends on the
graded Betti table of X∆(1), rather than on the speciﬁc choice of f ?

In other words, do we have constancy in the sense discussed in Section 4? It is clear
from Theorem 21 that the answer is yes if X∆(1) is Gorenstein and weak Fano:

Corollary 22. Let ∆ be a lattice polygon with two-dimensional interior and let f ∈
k[x±1, y±1] be a weakly ∆-nondegenerate Laurent polynomial. If X∆(1) is Gorenstein and
weak Fano then the canonical graded Betti numbers of Cf do not depend on the speciﬁc
choice of f .

For example, this implies that the canonical graded Betti table of a smooth plane
projective degree d ≥ 4 curve depends on d only. For general lattice polygons ∆ we
can show that only the coefﬁcients that are supported on the boundary potentially
matter:

Lemma 23. Let ∆ be a two-dimensional lattice polygon and let f ∈ k[x±1, y±1] be a
weakly ∆-nondegenerate Laurent polynomial. Then the canonical graded Betti table of Cf
at most depends on the coefﬁcients of f that are supported on ∂∆ ∩ Z2.
 xxvii

See again Chapter 8 for a proof. As a modest new application of this, we obtain
constancy of the canonical graded Betti table for triangles whose only lattice points
on the boundary are its vertices. Indeed, using the action of T2 the three corre-
sponding coefﬁcients can always be set to 1.

Remark. If the answer to (ii) is no, then question (i) still makes sense by restricting
to sufﬁciently generic weakly ∆-nondegenerate Laurent polynomials f ∈ k[x±1, y±1].

(iii) What does the graded Betti table of X∆(1) look like?

In order to have a combinatorial description of the canonical graded Betti table of
Cf it does not sufﬁce to merely relate it to the graded Betti numbers of X∆(1): we
also need to describe these numbers in a combinatorial way. This is a difﬁcult ques-
tion in its own right, with several partial results available in the existing literature,
most notably in the Ph.D. thesis [Her06] of Hering (who in fact studied syzygies
of toric varieties of arbitrary dimension). Much of our recent research time was
devoted to complementing the existing statements, but the overall picture remains
far from complete. Because of the independent interest we studied graded Betti
numbers of arbitrary projectively embedded toric surfaces, i.e. not necessarily of the
form X∆(1). An overview of our ﬁndings can be found in the chart on the next page.
For an accompanying discussion and proofs we refer to Chapter 6, but let us high-
light two statements that can be viewed as analogues of Green’s canonical syzygy
conjecture. At the lower-left end of the graded Betti table we have:

Theorem 24 (Hering, Schenck, Lemmens). Let ∆ be a lattice polygon such that ∆(1) ̸=
∅. The number of leading zeroes on row q = 2 of the graded Betti table of the toric surface
X∆ over k, counting from column index p = 1, is given by #(∂∆ ∩ Z2) − 3.

(If ∆(1) = ∅ then the entire row q = 2 is trivial.) In characteristic zero the above the-
orem was proven by Hering [Her06], following an observation of Schenck [Sch04]
and building on work of Gallego–Purnaprajna [GP01]. Recently Lemmens [Lem]
gave a proof that works in arbitrary characteristic; he also provided an explicit for-
mula for the ﬁrst non-zero entry. At the upper-right end of the graded Betti table
we conjecture:

Conjecture 25. Let ∆ be a two-dimensional lattice polygon such that ∆ ̸∼= Σ, Υ. The
number of concluding zeroes on row q = 1 of the graded Betti table of the toric surface X∆
over k, counting backwards from column index p = #(∆ ∩ Z2) − 3, is given by lw(∆) − 1,
except if

∆ ∼= dΣ for some d ≥ 2 or ∆ ∼= Υd for some d ≥ 2 or ∆ ∼= 2Υ (8)

in which case it is given by lw(∆) − 2.

(−1, −1)
 (d, 0)

(0, d)
Υd

xxviii xxix

(If ∆ ∼= Σ, Υ then the entire row q = 1 is trivial.) We have the following evidence in
favour of this conjecture:

Theorem 26. Let ∆ be a two-dimensional lattice polygon such that ∆ ̸∼= Σ, Υ. The number
of concluding zeroes on row q = 1 of the graded Betti table of the toric surface X∆ over k is
at most the quantity predicted by Conjecture 25. Moreover:

• If char k = 0 and #(∆ ∩ Z2) ≤ 32 then equality holds.

• If char k = 0, ∆ = Γ(1) for a larger lattice polygon Γ, and Green’s canonical syzygy
conjecture holds for some weakly Γ-nondegenerate curve (e.g. if X∆ carries an anti-
canonical pencil [LC13]), then equality holds.
In particular, if char k = 0 and X∆ is Gorenstein and weak Fano then equality holds.

• If equality holds for a certain instance of ∆ not among (8), then it also holds for every
lattice polygon containing ∆ and having the same lattice width.
Using [CL] and (a) it follows that if char k = 0 and lw(∆) ≤ 6 then equality holds.

For proofs we refer to Chapter 6, although let us note that the ﬁrst claim was ob-
tained using an explicit determination of the relevant entries in the graded Betti
table of X∆, for all two-dimesional lattice polygons ∆ containing at most 32 lattice
points, using our database from Chapter 2. For reasons of efﬁciency the computa-
tion was carried out in ﬁnite characteristic, leading to the stated result through a
semi-continuity argument.

Remark. The underlying algorithm can be used to gather all sorts of related data.
It explicitly computes the Koszul cohomology of X∆, using duality, the action of
T2 and some of the features stated in the chart on the previous page to reduce the
time and memory requirements. It was implemented in SageMath and for instance
allowed us to explicitly determine the graded Betti numbers of the Veronese surface
X6Σ = ν6(P2) in characteristic 40 009; we expect this to match with characteristic
zero. Up to ν5(P2) these data were recently gathered by Greco and Martino [GM16].

We end this section with two applications. Recall that Green’s conjecture helped us in
settling special instances of Conjecture 25. But there is also an implication in the opposite
direction: the instances of Conjecture 25 that were established through explicit computa-
tion in turn imply new cases of Green’s conjecture.

Theorem 27. Let char k = 0, let X/k be a toric surface, and let C ⊆ X be a non-hyperelliptic
smooth projective curve of genus 4 ≤ g ≤ 32. Then Green’s canonical syzygy conjecture is true
for C.

Omitting exceptional cases, the proof uses that

ag−lw(∆(1))−1 = bg−lw(∆(1))−1

as soon as cg−lw(∆(1))−1 = 0, (9)

which is immediate from the exact sequence (4). From Theorem 24 we know that (9) holds
if and only if #(∂∆(1)∩Z2) ≥ lw(∆(1))+2. Using our database of lattice polygons we com-
putationally veriﬁed that this last inequality is true whenever #(∆(1) ∩ Z2) ≤ 32, except
if ∆(1) ∼= Υ. The result then follows from Theorem 26, which says that bg−lw(∆(1))−1 = 0,
and our combinatorial interpretation for the Clifford index stated in Theorem 17, which

xxx

says that Green’s conjecture amounts to ag−lw(∆(1))−1 = 0. We refer to Chapter 8 for ad-
ditional details.

Remark. In higher genus there exist more counterexamples to #(∂∆(1) ∩ Z2) ≥ lw(∆(1)) +
2, with ∆ = conv{(4, 0), (10, 4), (0, 10)} being the smallest instance that we have found,
corresponding to g = 36. Here #(∂∆(1) ∩ Z2) = 9 and lw(∆(1)) = 8, and as a consequence
c27 ̸= 0. In this case Green’s canonical syzygy conjecture amounts to a27 = 0, but unlike
the foregoing cases it is insufﬁcient to verify that b27 = 0. In fact, if the sum formula
a27 = b27 + c27 from Theorem 21 would be true here (which we do not think it is), then
this would show that a27 ̸= 0 and hence that weakly ∆-nondegenerate curves are coun-
terexamples to Green’s conjecture!

A second application is concerned with the gonality conjecture due to Green and
Lazarsfeld [GL86], which was recently proven by Ein and Lazarsfeld [EL15].

Theorem 28 (Gonality conjecture, proven by Ein–Lazarsfeld). Let char k = 0 and let C/k
be a smooth projective curve of gonality γ ≥ 2. Let L be a globally generated divisor on C of
sufﬁciently large degree, and assume that C ⊆ Prk|L| is embedded using the linear system |L|.
Then the number of non-zero entries on row q = 1 of the graded Betti table of the homogeneous
coordinate ring of C equals h0(C, L) − γ − 1.

Concretely Ein and Lazarsfeld showed that deg L ≥ g3 is sufﬁcient, a bound which was
recently improved to deg L ≥ 4g − 3 by Rathmann [Rat]. It is expected that this is not
yet optimal, although Green and Lazarsfeld already noted that one needs at least deg L ≥
2g + γ − 1. In a ﬁrst draft of [FK] Farkas and Kemeny speculated that the latter bound
might always be sufﬁcient. However we show:

Theorem 29. For each γ ≥ 3 there exists a curve C/k of genus g = γ(γ − 1)/2 along with a very
ample divisor L of degree 2g + γ − 1 such that the number of non-zero entries on row q = 1 of
the graded Betti table of the homogeneous coordinate ring of the correspondingly embedded curve
is at least h0(C, L) − γ.

The curve C we construct is weakly Υγ−1-nondegenerate, and its exceptional behaviour
is tightly connected with the fact that Υγ−1 is exceptional for Conjecture 25. We refer to
Chapter 7 for the details.

6. Scrollar ruling degrees (Chapters 9 and 10)

As in the previous section we consider a lattice polygon ∆ with two-dimensional inte-
rior along with a weakly ∆-nondegenerate Laurent polynomial f ∈ k[x±1, y±1]. Write
g = #(∆(1) ∩ Z2) and let γ ≥ 3 denote the lattice width lw(∆). Assume that the latter
equals the gonality of Cf , or in other words that there exists at least one combinatorial
gonality pencil gv.

Remark. In view of the material from Chapter 5 this means that we exclude ∆ ∼= 2Υ
and ∆ ∼= dΣ for any d ≥ 4. However, in the last case one can circumvent this by not-
ing that a weakly dΣ-nondegenerate curve is also weakly conv{(1, 0), (d, 0), (0, d), (0, 1)}-
nondegenerate: simply replace f by f (x + x0, y + y0) for some (x0, y0) ∈ Uf . This does
not affect the interior polygon, in terms of which all results below are stated.

For convenience we assume that v = (1, 0) and that ∆ ⊆ R × [0, γ]; in particular gv =
|ﬁber of (x, y) ↦→ x|. This can always be achieved by means of a unimodular transforma-
tion. It is not hard to see that the rational normal scroll S ⊆ Pg−1 swept out by gv equals
 xxxi

∆(1)
 ∆j = γ
j = γ − 1

j = 0
j = 1
j = 2

...

the (γ − 1)-dimensional toric variety associated to the polytope that one obtains from
∆(1) by ‘forgetting’ that horizontal lines are coplanar, which amounts to omitting certain
deﬁning equations; we refer to Chapter 5 for more details. In fact this observation is the
central ingredient in the proof of Theorem 15, which in our case states that the scrollar
invariants are given by the width invariants

Ej := i
(+)(j) − i
(−)(j)

for j = 1, . . . , γ − 1, where

i
(−)(j) = min{i ∈ Z | (i, j) ∈ ∆(1)} and i
(+)(j) = max{i ∈ Z | (i, j) ∈ ∆(1)}.

For our current purposes an important conclusion is that the series of inclusions (4) ex-
tends to Ccan
f ⊆ X∆(1) ⊆ S ⊆ Pg−1.
Recall that in Chapter 4 we provided a recipe for obtaining a minimal set of generators
of the canonical ideal of Cf . In this section we report on a similar method for determin-
ing a minimal set of deﬁning equations for our canonical curve relative to the scroll S. This
concept was introduced and made precise by Schreyer [Sch86]. Informally spoken, the
goal is to realize Ccan
f as the scheme-theoretic intersection of as few divisors on S as possi-
ble. Modulo linear equivalence these divisors can be expressed as linear combinations of
the hyperplane section class H and the ruling class R, which generate the Picard group.
The coefﬁcient of H matches with our intuitive notion of degree and therefore has little
added value. But the coefﬁcient of R can give interesting new discrete information.

Example. In the trigonal case Ccan
f is a divisor itself. It concerns a ‘cubic’, as it is contained
in the class 3H − (g − 4)R.

Subtlety. If one of the rational normal curves spanning S is of degree 0 (i.e. is a point)
then the Picard group may not be freely generated by H and R [Fer01]. To give a rather
degenerated example, consider ∆(1) = Σ: here the scroll is just P2 where R = H, and we
recover that Ccan
f ∈ 3H + R = 4R is a plane quartic. To avoid non-unique expansions and
various other theoretical issues one should actually work with the strict transforms of
Ccan
f and X∆(1) under the natural birational morphism j : S′ → S induced by increasing
the degrees of the spanning rational normal curves by some ﬁxed positive amount, but
we will ignore this technicality here.

From γ ≥ 4 on it turns out that our curve is minimally cut out by (γ2 − 3γ)/2 ‘quadrics’,
i.e. divisors whose classes are of the form

2H − b1R, 2H − b2R, 2H − b3R, . . . , 2H − b(γ2−3γ)/2R

xxxii

for integers bi that sum up to (γ − 3)(g − γ − 1) and which turn out to be independent
of the chosen divisors, up to order. See [BH15; Sch86] for more details. We call these
numbers the scrollar ruling degrees3 with respect to gv.
We ﬁrst concentrate on the case γ = 4, which is particularly interesting. Assume that
gv has scrollar invariants 0 ≤ a ≤ b ≤ c, so that S ⊆ Pg−1 is the toric threefold associated
to the polytope ∆a,b,c depicted below. Note that we can view it as a completion of afﬁne

(b, 1, 0)(0, 1, 0)

(0, 0, 0)

(0, 0, 1) (a, 0, 1)
 (c, 0, 0)
 ∆a,b,c

space A3 rather than just the torus T3. Inside S our curve Ccan
f arises as a complete
intersection of two divisors Y, Z whose respective classes are 2H − b1R and 2H − b2R
with b1 + b2 = g − 5, where we can assume that b1 ≥ b2. It can be shown that b2 ≥ −1,
where equality occurs if and only if Cf is isomorphic to a smooth plane quintic [Sch86,
§6], i.e. if and only if ∆(1) ∼= 2Σ.
In terms of deﬁning equations this means that Y ∩ A3 is deﬁned by a polynomial
fY ∈ k[x, y, z] which is supported on the horizontally shrunk version of 2∆a,b,c shown
below (and that this is no longer true if we shrink it further). The analogous claim applies

(0, 0, 0)
 (2 b − b1, 2 , 0)
 (2 c − b1, 0, 2)

(2 a − b1, 0, 0)

(0, 2 , 0)

(0, 0, 2)
 to the polynomial fZ ∈ k[x, y, z] associated to Z. Since Z corresponds to the bigger
polytope it moves in a family: one is free to replace fZ by fZ + gfY for some g ∈ k[x] of
degree at most b1 − b2. On the other hand if b1 > b2 then Y is immovable. In fact Schreyer
proved that the invariants b1, b2 are independent of the chosen g1
4 and that the same is
true for the surface Y as soon as b1 > b2. The main result of Chapter 9 is:

Theorem 30. Let ∆ be a two-dimensional lattice polygon, let f ∈ k[x±1, y±1] be weakly ∆-
nondegenerate, and assume that Cf is tetragonal. Then the scrollar ruling degrees {b1, b2} of Cf
are given by { #(∂∆
(1) ∩ Z2) − 4 , #(∆(2) ∩ Z
2) − 1 } .

Moreover if #(∂∆(1) ∩ Z2) − 4 > #(∆(2) ∩ Z2) − 1 then the surface Y is given by X∆(1).

The last equality is almost always satisﬁed, with all counterexamples to be found in
Chapter 9.

Example. Let f ∈ k[x±1, y±1] be a weakly ∆4,7-nondegenerate Laurent polynomial. This is
a C4,7 curve, which by Baker’s bound is of genus 9, and by Theorem 13 carries a unique
g1
4. According to Theorem 15 the corresponding scrollar invariants are 0, 2, 4 and the
above theorem says that b1 = 4 and b2 = 0. The surface Y , whose corresponding poly-
tope is depicted above, is the toric surface X
∆(1)
4,7, which on A3 is cut out by fY = y2 − z.

3In Chapter 10 we have called these invariants the ‘ﬁrst scrollar Betti numbers’, but since these numbers
do not appear as dimensions of cohomology spaces, this terminology was up for improvement.
 xxxiii

(0, 2 , 0)

(0, 0, 1)
 (4 , 0, 0)(0, 0, 0) Next in Chapter 10 we work towards a combinatorial interpretation for the scrollar
ruling degrees of a weakly nondegenerate curve of gonality γ ≥ 5. For this we assume
that ∆ and v satisfy two technical conditions P1(v) and P2(v), which are explained in
more detail below. Essentially these conditions impose on ∆(1) a certain combinatorial
compatibility between its ‘left-hand side’ and its ‘right-hand side’, i.e. between the num-
bers i(−)(j) and the numbers i(+)(j).
In a ﬁrst phase we look for divisors that cut out our toric surface X∆(1). Recall that S
was obtained from X∆(1) by forgetting that horizontal lines are coplanar, so the idea is to
rivet these lines gradually back together. Concretely for each pair j1, j2 ∈ {1, 2, . . . , γ − 1}
such that j2 − j1 ≥ 2 we deﬁne a toric (γ − 2)-fold Dj1,j2 ⊆ S which reminds the scroll of
the fact that the pair of lines at heights j1, j2 and the pair of lines at heights j1 + r, j2 − r
have the same ‘mean’:
 j1

j1 + r
mean j2 − r

j2

Here r ∈ {1, 2, . . . , (j2 − j1)/2} should be chosen carefully, which is where the condition
P1(v) shows up. Concretely, for each r we deﬁne

ϵ
(−)
j1,j2,r =
 {
0 if i(−)(j1 + r) + i(−)(j2 − r) ≤ i(−)(j1) + i(−)(j2)
1 if i(−)(j1 + r) + i(−)(j2 − r) > i(−)(j1) + i(−)(j2)

= max{0, (i
(−)(j1 + r) + i(−)(j2 − r)) − (i
(−)(j1) + i
(−)(j2))}

and
 ϵ
(+)
j1,j2,r =
 {
0 if i(+)(j1 + r) + i(+)(j2 − r) ≥ i(+)(j1) + i(+)(j2)
1 if i(+)(j1 + r) + i(+)(j2 − r) < i(+)(j1) + i(+)(j2)

= max{0, (i
(+)(j1) + i
(+)(j2)) − (i(+)(j1 + r) + i
(+)(j2 − r))}.

Condition P1(v) imposes that

• either we can ﬁnd an r for which ϵ
(−)
j1,j2,r = ϵ
(+)
j1,j2,r = 0, in which case we deﬁne
ϵj1,j2 = 0,

• or there is no r for which ϵ
(−)
j1,j2,r = 0 but there is an r for which ϵ
(+)
j1,j2,r = 0, in which
case we deﬁne ϵj1,j2 = 1,

• or, similarly, there is no r for which ϵ
(+)
j1,j2,r = 0 but there is an r for which ϵ
(−)
j1,j2,r = 0,
in which case we deﬁne ϵj1,j2 = 1,

xxxiv

• or there is no r for which ϵ
(−)
j1,j2,r = 0 and neither there is an r for which ϵ
(+)
j1,j2,r = 0,
in which case we deﬁne ϵj1,j2 = 2.

This should be true for all (γ − 2)(γ − 3)/2 pairs j1, j2. We refer to Chapter 10 for further
details on the construction of Dj1,j2, for some clarifying examples, and eventually for a
proof of the following statement:

Theorem 31. Inheriting the notation from above and assuming that condition P1(v) is satisﬁed,
one has that the (γ − 2)(γ − 3)/2 divisors Dj1,j2 ⊆ S together cut out X∆(1). Moreover

Dj1,j2 ∈ 2H − Bj1,j2R for all j1, j2, where Bj1,j2 = Ej1 + Ej2 − ϵj1,j2,

and the Bj1,j2’s sum up to (γ − 4)g − (γ2 − 3γ) + #(∂∆(1) ∩ Z2).

The next step is to add divisors that slice this further down to Ccan
f . Recall from
Section 2 that the canonical ideal of Cf ⊆ Pg−1 is spanned by the ideal of X∆(1) and the
quadrics Qw = ∑

(i,j)∈∆∩Z2 cijXuij Xvij , w ∈ ∆(2) ∩ Z2,

where uij, vij should be chosen such that (i, j) − w = (uij − w) + (vij − w). Typically
the choice of uij and vij is not unique. Condition P2(v) amounts to the existence for each
horizontal line L of horizontal lines M1 and M2 such that it is possible to choose uij ∈ M1
and vij ∈ M2 for all w ∈ L. If this is indeed possible then we obtain our requested divisors
by grouping together all Qw’s that correspond to lattice points on the same horizontal line
L. More precisely we deﬁne for each j = 2, 3, . . . , γ − 2 a divisor

Dj := S ∩ { Qw | w ∈ ∆(2) ∩ Z2 lies at height j }.

We refer to Chapter 10 for explanation why this indeed results in a subscheme of codi-
mension one (in contrast with what happens if one does not choose the uij’s and vij’s in
a consistent way), and for a proof of the following statement:

Theorem 32. Inheriting the notation from above and assuming that condition P2(v) is satisﬁed,
one has that the γ − 3 divisors Dj ⊆ S together with X∆(1) ⊆ S cut out Ccan
f . Moreover

Dj ∈ 2H − BjR for all j, where Bj = −1 + #{ i ∈ Z | (i, j) ∈ ∆(2) ∩ Z
2 },

and the Bj’s sum up to #(∆(2) ∩ Z2) − (γ − 3).

Notice that the multi-set of Bj’s equals the multi-set of width invariants E(∆(1), v). Fi-
nally, by combining both results and noticing that

(γ − 2)(γ − 3)/2 + (γ − 3) = (γ2 − 3γ)/2,

we arrive at our desired interpretation of the scrollar ruling degrees:

Corollary 33. Inheriting the notation from above and assuming that conditions P1(v) and P2(v)
are satisﬁed, one has that the scrollar ruling degrees of Cf with respect to gv are given by

{Bj}j∈{2,...,γ−2} ∪ {Bj1,j2}j1,j2∈{1,...,γ−1}
j2−j1≥2 .

These scrollar Betti numbers indeed add up to (γ − 3)(g − γ − 1), as announced.
 xxxv

Remark. The conditions P1(v) and P2(v) are milder than one might fear at a ﬁrst glance.
In fact condition P1(v) is void for γ = 5 and γ = 6 and we believe that the same is true
for P2(v), although we could not prove this. The smallest pair ∆, v violating P2(v) that
we managed to ﬁnd corresponds to curves of genus 46 and gonality 10; see Chapter 10.

7. Arithmetic features (Chapter 11)

Consider a ﬁeld k that is not necessarily algebraically closed. Let ∆ be a two-dimensional
lattice polygon and let f ∈ k[x±1, y±1] be a Laurent polynomial that is weakly ∆-non-
degenerate when considered over kalg.cl.. Then Cf ⊆ X∆ is a smooth projective curve that
is deﬁned over k. In this section we wish to illustrate that besides geometric information,
our polygon ∆ potentially also contains some arithmetic data, even though we do not
expect the existence of a large one-to-one arithmetic-combinatorics dictionary as in the
geometric case.
A ﬁrst arithmetic feature is that if an edge τ ⊆ ∆ has integral length one then the
corresponding torus-invariant divisor Dτ ⊆ X∆ contains a k-rational point of Cf . The
reason is that the intersection locus of Cf with Dτ is locally given by a linear equation
with coefﬁcients in k. Thus if there are many such edges then this yields meaningful
lower bounds on #Cf (k). This was used by Kresch, Wetherell and Zieve to prove the
following fact:

Theorem 34 (Kresch, Wetherell, Zieve [KWZ02]). For every integer g ≥ 0 and every prime
power q deﬁne Nq(g) := maxC #C(Fq), where C ranges over all smooth projective curves of
genus g over Fq. Then limg→∞ Nq(g) = ∞. More precisely lim inf g→∞ Nq(g)/g1/3 > 0.

This statement is no longer the best available: in 2004 the same authors, in cooperation
with Elkies, Howe and Poonen [Elk+04], managed to replace the denominator g1/3 by g,
which is optimal in view of the Hasse-Weil bound. Unfortunately this relies on other tech-
niques, but nevertheless Theorem 34 remains a beautiful application of smooth curves in
toric surfaces.

Remark. More generally the presence of an edge τ ⊆ ∆ of integeral length r ensures the
existence of a k-rational divisor of degree r. Using a classiﬁcation due to Fisher [Fis08],
we used this in Chapter 1 to prove that a genus one curve C/k is k-birationally equiva-
lent to a weakly nondegenerate curve if and only if it has a k-rational divisor of degree at
most 3.

A second arithmetic feature is that the k-rational gonality of Cf , by which we mean
the minimal degree of a k-rational map Cf → P1, equals its geometric gonality, except
possibly if ∆ ∼= 2Υ or if ∆ ∼= dΣ for some d ≥ 2. This is a trivial consequence of Theo-
rem 13, because combinatorial pencils are clearly k-rational. In particular Cf is hyperel-
liptic if and only if it is geometrically hyperelliptic.

Remark. By letting k = C((t)), through specialization of divisors this gives (very) prudent
support in the case of planar graphs in favour of a conjecture by Baker [Bak08, Conj. 3.14],
saying that the gonality of a graph equals the gonality of its metrization.

If ∆ ∼= 2Υ then the k-rational gonality equals the geometric gonality (namely 3) except
if Cf canonically embeds into an elliptic quadric in P3 in which case it equals 4; the
occurrence of this event may depend on the speciﬁc choice of f . If ∆ ∼= dΣ for some
d ≥ 2 then the k-rational gonality equals the geometric gonality (namely d − 1) except if
#Cf (k) = ∅ in which case it equals d; again this may depend on the speciﬁc choice of f .

xxxvi

Chapter 11 is devoted to yet another arithmetic phenomenon, which has a geomet-
ric intake. One can verify that the canonical divisor K∆ on Cf that one obtains from
adjunction theory (see Section 1) equals
∑

τ (−⟨ντ , pτ ⟩ − 1)(Dτ ∩ Cf ), (10)

where:

• the sum runs through all edges τ ⊆ ∆,

• Dτ denotes the torus-invariant divisor on X∆ associated to τ ,

• ντ ∈ Z2 is the primitive inward pointing normal vector to τ ,

• pτ is any point on τ ∩ Z2.

Here ⟨·, ·⟩ denotes the standard inner product on R2. It is the divisor of the differential

dx

xy ∂f
∂y ,

unless ∂f /∂y = 0, which happens if x is not a separating variable, in which case4 one
should exchange the role of x and y. Similarly one veriﬁes that the set
{

xiyj dx

xy ∂f
∂g
 }

(i,j)∈∆(1)∩Z2 (11)

is a basis of holomorphic differentials. We refer to [CDV06] for more details.
One observes that if all ⟨ντ , pτ ⟩’s are odd then all coefﬁcients in (10) are even, so that
we obtain a theta characteristic Θgeom by halving them. Note that Θgeom is k-rational. If
not all inner products are odd then it might be possible to achieve this by translating ∆
over some (i, j) ∈ Z2, amounting to multiplying f by the monomial xiyj. If this is indeed
possible then ∆ is called canonically even. If it is moreover possible to do this in such a
way that (0, 0) becomes contained in ∆, then ∆ is called effectively canonically even be-
cause the resulting theta characteristic is effective. (Note that then (0, 0) is automatically
contained in ∆(1), otherwise one of the inner products would be zero, hence even.)

Remark. If translation over a vector v ∈ Z2 makes all ⟨ντ , pτ ⟩’s odd, then so does translat-
ing over v + w for any w ∈ (2Z)2.

Examples. All triangles ∆a,b where gcd(a, b, 2) = 1 are canonically even. If moreover
a, b ≥ 2 then they are effectively canonically even. This covers all smooth plane curves
of odd degree and all Ca,b curves. Also all triangles ∆2,2g+2 where g ≥ 3 is odd are
effectively canonically even; this corresponds to hyperelliptic curves of odd genus. The
polygon Ω depicted below is an example of a lattice polygon which is canonically even
but not effectively canonically even.

Now assume char k = 2. Then Cf automatically carries another k-rational theta char-
acteristic Θarith, which was introduced by Mumford [Mum71]. It is simply deﬁned as
Θarith := (div dx)/2, where we note that dx indeed has even orders of vanishing because

4This event is extremely unlikely but it can happen. Example: f = y2 + x2 + x + 1 in characteristic 2.
 xxxvii

(1, 0)
 (3, 1)

(0, 3)
 Ω

only even terms remain when differentiating a Laurent series in characteristic two.5 A
theorem by Stöhr and Voloch [SV87] says that h0(Cf , Θarith) = g − r, where g is the genus
of Cf and r is the rank of the Cartier operator acting on the space of holomorphic differ-
entials. It is well-known that r = g if and only if Cf is an ordinary curve. This implies:

Lemma 35. Let ∆ be a two-dimensional effectively canonically even lattice polygon and let k be
a ﬁeld of characteristic 2. Let f ∈ k[x±1, y±1] be a weakly ∆-nondegenerate Laurent polynomial.
If Cf is ordinary then Jac(Cf ) carries a non-trivial k-rational 2-torsion point.

Indeed, if Cf is ordinary then h0(Cf , Θarith) = 0 and therefore Θarith is not linearly equiv-
alent to an effective divisor, in particular not to Θgeom. Then the divisor Θarith − Θgeom
maps to a non-trivial k-rational 2-torsion point on the Jacobian.
Alternatively, we obtain Lemma 35 as a corollary to the following stronger result,
which is proven in Chapter 11 by explicit computation, using the basis (11).

Theorem 36. Let ∆ be a two-dimensional canonically even lattice polygon and let k be a ﬁeld of
characteristic 2. Let f = ∑

(i,j)∈∆∩Z2 cijx
iyj ∈ k[x±1, y±1]

be a weakly ∆-nondegenerate Laurent polynomial. Let P be the set of vectors (i, j) ∈ ∆ ∩ Z2 such
that translating over (−i, −j) makes all ⟨ντ , pτ ⟩’s odd. Let ρ = #P .

• If ci,j ̸= 0 for at least one (i, j) ∈ P then Θarith and Θgeom are not linearly equivalent, and
therefore Jac(Cf ) carries a non-trivial k-rational 2-torsion point.

• If ci,j = 0 for all (i, j) ∈ P then the rank of the Cartier operator is at most g − ρ.

In particular if ∆ is effectively canonically even, then ρ > 0 and

Cf ordinary ⇒ ci,j ̸= 0 for some (i, j) ∈ P ⇒ Jac(Cf )(k)[2] ̸= 0.

As a consequence, in characteristic two, a sufﬁciently generic Laurent polynomial that
is supported on an effectively canonically even lattice polygon deﬁnes a curve with a
non-trivial k-rational two-torsion point on its Jacobian. This observation was ﬁrst made
by Cais, Ellenberg and Zureick-Brown in the case of smooth plane curves of odd de-
gree [CEZB13]. In the case of ∆a,b with gcd(a, b) = 1 this explains why Denef and Ver-
cauteren [DV06] had to tolerate a factor 2 in #Jac(C)(k) when trying to generate crypto-
graphically secure Ca,b curves C over ﬁnite ﬁelds of characteristic two.
We actually conjecture that under the assumptions of the theorem the rank of the
Cartier operator is at least g−ρ, where equality holds if and only if ci,j = 0 for all (i, j) ∈ P .
Chapter 11 contains proofs of this conjecture for ∆ ∼= ∆2g+2,2 with g odd (hyperelliptic
curves of odd genus), for ∆ ∼= dΣ with d odd (smooth plane curves of odd degree), and
also for ∆ ∼= Ω. In the latter case ρ = 0, so this converts into the following fact:

5If x is not a separating variable then dx = 0, in which case we again exchange the role of x and y.

xxxviii

Lemma 37. Let k be a ﬁeld of characteristic 2 and let f ∈ k[x±1, y±1] be weakly Ω-nondegenerate.
Then Cf is ordinary.

8. Intrinsicness (Chapters 5, 9 and 10)

In this section we reinstall the assumption that k is an algebraically closed ﬁeld. Let ∆ be
a two-dimensional lattice polygon and let f ∈ k[x±1, y±1] be a weakly ∆-nondegenerate
Laurent polynomial. Given the long list of geometric invariants that can be told from the
combinatorics of ∆, one can wonder to what extent it is possible to recover the polygon
itself from the abstract birational geometry of Uf (or of Cf ). The best one can hope for
is to ﬁnd back ∆ up to unimodular equivalence, because unimodular transformations
correspond to automorphisms of T2. Another relaxation is that (usually) one can only
expect to recover ∆(1), rather than all of ∆. For example, recall from the ﬁrst remark
in Section 6 that every weakly dΣ-nondegenerate Laurent polynomial is also weakly ∆-
nondegenerate, where ∆ is obtained from dΣ by clipping off the point (0, 0). More gen-
erally, pruning a vertex off a two-dimensional lattice polygon ∆ without affecting its in-
terior boils down to forcing the curve through a certain non-singular point of X∆, which
is usually not an intrinsic property. One is naturally led to the following deﬁnition.

Deﬁnition 38. Let ∆ be a two-dimensional lattice polygon and let C/k be a weakly ∆-nondegenerate
curve. We say that ∆(1) is intrinsic to C if for all two-dimensional lattice polygons ∆′ for which
C is weakly ∆′-nondegenerate it holds that ∆(1) ∼= ∆′(1). We say that ∆(1) is intrinsic if it is
intrinsic to every weakly ∆-nondegenerate curve.

A few ﬁrst cases in which ∆(1) is intrinsic are:

• ∆(1) = ∅, which occurs if and only if Cf is rational,

• dim ∆(1) = 0, which holds if and only if Cf is elliptic,

• dim ∆(1) = 1, which holds if and only if Cf is hyperelliptic of genus #(∆(1) ∩ Z2),

• ∆(1) ∼= (d − 3)Σ for some d ≥ 3, which by Corollary 18 occurs if and only if Cf is
birationally equivalent to a smooth projective plane curve of degree d.

From Theorem 17 we see that if char k = 0 then also ∆(1) ∼= 2Υ is intrinsic, because this
occurs if and only if Cf is of Clifford index 3. Most likely this result is also true in positive
characteristic.
As with many statements in this manuscript, the case where ∆(1) ∼= Υ turns out
to be an exception. Indeed, recall from Theorem 10 that every genus 4 curve is either
weakly □3,3-nondegenerate or weakly ∆6,3-nondegenerate. The respective interiors of
these polygons are □1,1 and ∆2,1, while Υ is equivalent to neither of both. Since both
cases occur, this turns all three interior genus 4 polygons □1,1, ∆2,1, Υ into exceptions.

More counterexamples. Our polygon Υ belongs to a larger family of counterexamples. Let
g ≥ 4 satisfy g ≡ 0 mod 4, and consider the lattice polygons Γg and Γ′
g depicted below,
which are non-equivalent. We note that Γ4 ∼= Υ. If char k = 0 or char k > g/2 + 1
then the polynomials f = 1 − x2y4 − x g
2 +2y2 and f ′ = (y4 − 1)x g
2 +1 + 4y2 are weakly
∆g-nondegenerate and weakly ∆′
g-nondegenerate, respectively. Here ∆g and ∆′
g are as

depicted above and satisfy ∆(1)
g = Γg and ∆
′(1)
g = Γ′
g. Since the rational maps

Uf → Uf ′ : (x, y) ↦→ (x, 1 − xy2

x g
4 +1y
 )
 xxxix

(1, 1) (g/4, 1)
 (g/2 + 1, 2)

(2, 3) (g/4 + 1, 3)

Γg∆g (1, 2)
 (g/2, 1)

(g/2, 3)(g/4 + 1, 3)

(g/4 + 1, 1)

Γ
′
g ∆′
g

Uf ′ → Uf : (x, y) ↦→
 (

x, 2y

x g
4 +1(1 + y2)
 )

are inverses of each other, we conclude that Cf and Cf ′ are isomorphic. Therefore Γg is
not intrinsic to Cf , and neither is Γ′
g.

In spite of these exceptions we believe that ‘most’ interior lattice polygons are intrinsic,
but making this statement precise (let along proving this) seems to be a hard task. Using
Theorem 15 and Theorem 30 we can settle some additional cases, though:

• #(∆(1) ∩ Z2) ≥ 5 and ∆(2) = ∅, which holds if and only if Cf is trigonal of genus
g ≥ 5, or isomorphic to a smooth plane quintic,

• lw(∆(1)) = 2 and #(∂∆(1) ∩ Z2) ≥ #(∆(2) ∩ Z2) + 5, which holds if and only if Cf
is tetragonal and b1 ≥ b2 + 2.

In both cases, the bare line of accompanying text does not sufﬁce to conclude intrinsic-
ness: more details and reﬁned statements can be found in Chapter 9. Let us remark that
in both situations X∆(1) can be easily recovered from the canonical model Ccan
f ⊆ Pg−1.
Indeed, in the former case it arises as the intersection of all quadrics containing Ccan
f .
In the latter case it is the unique surface containing Ccan
f that is linearly equivalent to
2H − b1R, when viewed as a divisor inside the scroll spanned by a g1
4. Our most subtle
intrinsicness result, which strongly relies on Corollary 33, is:

Theorem 39. Let a, b ≥ 1 be integers that are not both equal to 1. Then the interior polygon □a,b
is intrinsic. More precisely let ∆ be a two-dimensional lattice polygon, let f ∈ k[x±1, y±1] be a
weakly ∆-nondegenerate Laurent polynomial, and assume that Uf is birationally equivalent to a
smooth projective curve in P1 × P1 of bidegree (a + 2, b + 2). Then ∆(1) ∼= □a,b.

A proof can be found in Chapter 10.

Remark. One can also target weaker intrinsicness questions, by only distinguishing be-
tween polygons that belong to some given family:

• A weakly ∆a,b-nondegenerate curve cannot be weakly ∆a′,b′-nondegenerate for dis-
tinct pairs of coprime positive integers {a, b} and {a′, b′}. This is immediate from
our combinatorial interpretations for the genus

#(∆(1)
a,b ∩ Z
2) = (a − 1)(b − 1)/2

and the gonality lw(∆
(1)
a,b) + 2 = lw(∆a,b) = min{a, b}.

In other words a Ca,b curve cannot be Ca′,b′.

• A similar reasoning involving the scrollar invariants shows that if a smooth non-
hyperelliptic curve C/k of genus g ≥ 2 can be embedded in the nth Hirzebruch
surface Hn for some n ≥ 0, then this value of n is unique and can therefore be
considered an invariant of C. We refer to Chapter 5 for an elaboration of the details.

xl

References

[Apr05] M. Aprodu. “Remarks on syzygies of d-gonal curves”. In: Math. Res. Lett.
12.2-3 (2005), pp. 387–400.

[Ark80] J. R. Arkinstall. “Minimal requirements for Minkowski’s theorem in the plane.
I”. In: Bull. Austral. Math. Soc. 22.2 (1980), pp. 259–274, 275–283.

[Ave+15] G. Averkov et al. “Tight bounds on discrete quantitative Helly numbers”. In:
Preprint (2015).

[Bak08] M. Baker. “Specialization of linear systems from curves to graphs”. In: Alge-
bra Number Theory 2.6 (2008). With an appendix by B. Conrad, pp. 613–653.

[Bak93] H. Baker. “Examples of applications of Newton’s polygon to the theory of
singular points of algebraic functions”. In: Trans. Cambridge Phil. Soc. 15 (1893),
pp. 403–450.

[BCP97] W. Bosma, J. Cannon, and C. Playoust. “The Magma algebra system. I. The
user language”. In: J. Symbolic Comput. 24.3-4 (1997). Computational algebra
and number theory (London, 1993), pp. 235–265.

[BG09] W. Bruns and J. Gubeladze. Polytopes, rings, and K-theory. Springer Mono-
graphs in Mathematics. Springer, Dordrecht, 2009, pp. xiv+461.

[BH15] C. Bopp and M. Hoff. “Resolutions of general canonical curves on rational
normal scrolls”. In: Arch. Math. (Basel) 105.3 (2015), pp. 239–249.

[Bro+15] S. Brodsky et al. “Moduli of tropical plane curves”. In: Res. Math. Sci. 2 (2015),
Art. 4, 31.

[BT04] I. Bárány and N. Tokushige. “The minimum area of convex lattice n-gons”.
In: Combinatorica 24.2 (2004), pp. 171–185.

[CC12] W. Castryck and F. Cools. “Newton polygons and curve gonalities”. In: J.
Algebraic Combin. 35.3 (2012), pp. 345–366.

[CDV06] W. Castryck, J. Denef, and F. Vercauteren. “Computing zeta functions of non-
degenerate curves”. In: IMRP Int. Math. Res. Pap. (2006), Art. ID 72017, 57.

[CEZB13] B. Cais, J. Ellenberg, and D. Zureick-Brown. “Random Dieudonné modules,
random p-divisible groups, and random curves over ﬁnite ﬁelds”. In: J. Inst.
Math. Jussieu 12.3 (2013), pp. 651–676.

[CL] F. Cools and A. Lemmens. Minimal polygons with ﬁxed lattice width. Preprint:
https://arxiv.org/abs/1702.01131.

[CLS11] D. Cox, J. Little, and H. Schenck. Toric varieties. Vol. 124. Graduate Stud-
ies in Mathematics. American Mathematical Society, Providence, RI, 2011,
pp. xxiv+841.

[CM91] M. Coppens and G. Martens. “Secant spaces and Clifford’s theorem”. In:
Compositio Math. 78.2 (1991), pp. 193–212.

[CT] W. Castryck and J. Tuitman. Point counting on curves using a gonality preserving
lift. Preprint: https://arxiv.org/abs/1605.02162.

[CV10] W. Castryck and J. Voight. “Nondegenerate curves of low genus over small ﬁ-
nite ﬁelds”. In: Arithmetic, geometry, cryptography and coding theory 2009. Vol. 521.
Contemp. Math. Amer. Math. Soc., Providence, RI, 2010, pp. 21–28.

[DMN12] J. Draisma, T. McAllister, and B. Nill. “Lattice-width directions and Minkowski’s
3d-theorem”. In: SIAM J. Discrete Math. 26.3 (2012), pp. 1104–1107.
 xli

[DV06] J. Denef and F. Vercauteren. “Counting points on Cab curves using Monsky-
Washnitzer cohomology”. In: Finite Fields Appl. 12.1 (2006), pp. 78–102.

[EH87] D. Eisenbud and J. Harris. “On varieties of minimal degree (a centennial ac-
count)”. In: Algebraic geometry, Bowdoin, 1985 (Brunswick, Maine, 1985). Vol. 46.
Proc. Sympos. Pure Math. Amer. Math. Soc., Providence, RI, 1987, pp. 3–13.

[Eis+89] D. Eisenbud et al. “The Clifford dimension of a projective curve”. In: Compo-
sitio Math. 72.2 (1989), pp. 173–204.

[EL15] L. Ein and R. Lazarsfeld. “The gonality conjecture on syzygies of algebraic
curves of large degree”. In: Publ. Math. Inst. Hautes Études Sci. 122 (2015),
pp. 301–313. ISSN: 0073-8301.

[Elk+04] N. Elkies et al. “Curves of every genus with many points. II. Asymptotically
good families”. In: Duke Math. J. 122.2 (2004), pp. 399–422.

[Far09] G. Farkas. “Birational aspects of the geometry of Mg”. In: Surveys in differ-
ential geometry. Vol. XIV. Geometry of Riemann surfaces and their moduli spaces.
Vol. 14. Surv. Differ. Geom. Int. Press, Somerville, MA, 2009, pp. 57–110.

[Fer01] R. Ferraro. “Weil divisors on rational normal scrolls”. In: Geometric and combi-
natorial aspects of commutative algebra (Messina, 1999). Vol. 217. Lecture Notes
in Pure and Appl. Math. Dekker, New York, 2001, pp. 183–197.

[Fis08] T. Fisher. “The invariants of a genus one curve”. In: Proc. Lond. Math. Soc. (3)
97.3 (2008), pp. 753–782.

[FK] G. Farkas and M. Kemeny. Linear syzygies on curves with prescribed gonality.
Preprint: https://arxiv.org/abs/1610.04424.

[FTM74] L. Fejes Tóth and E. Makai Jr. “On the thinnest non-separable lattice of convex
plates”. In: Stud. Sci. Math. Hungar. 9 (1974), pp. 191–193.

[Ful93] W. Fulton. Introduction to toric varieties. Vol. 131. Annals of Mathematics Stud-
ies. Princeton University Press, Princeton, NJ, 1993, pp. xii+157.

[GL86] M. Green and R. Lazarsfeld. “On the projective normality of complete linear
series on an algebraic curve”. In: Invent. Math. 83.1 (1986), pp. 73–90.

[GL87] M. Green and R. Lazarsfeld. “Special divisors on curves on a K3 surface”. In:
Invent. Math. 89.2 (1987), pp. 357–370.

[GM16] O. Greco and I. Martino. “Syzygies of the Veronese modules”. In: Comm. Al-
gebra 44.9 (2016), pp. 3890–3906.

[GP01] F. Gallego and B. Purnaprajna. “Some results on rational surfaces and Fano
varieties”. In: J. Reine Angew. Math. 538 (2001), pp. 25–55.

[Gre84] M. Green. “Koszul cohomology and the geometry of projective varieties”. In:
J. Differential Geom. 19.1 (1984), pp. 125–171.

[Har86] R. Hartshorne. “Generalized divisors on Gorenstein curves and a theorem of
Noether”. In: J. Math. Kyoto Univ. 26.3 (1986), pp. 375–386.

[Her06] M. Hering. “Syzygies of toric varieties”. PhD thesis. University of Michigan,
2006.

[HS09] C. Haase and J. Schicho. “Lattice polygons and the number 2i + 7”. In: Amer.
Math. Monthly 116.2 (2009), pp. 151–165.

[Kaw16] R. Kawaguchi. “The gonality and the Clifford index of curves on a toric sur-
face”. In: J. Algebra 449 (2016), pp. 660–686.

xlii

[Kho77] A. G. Khovanskii. “Newton polyhedra, and toroidal varieties”. In: Funkcional.
Anal. i Priložen. 11.4 (1977), pp. 56–64, 96.

[Koe91] R.-J. Koelman. “The number of moduli of families of curves on toric sur-
faces”. PhD thesis. Katholieke Universiteit Nijmegen, 1991.

[KWZ02] A. Kresch, J. Wetherell, and M. Zieve. “Curves of every genus with many
points. I. Abelian and toric families”. In: J. Algebra 250.1 (2002), pp. 353–370.

[LC13] M. Lelli-Chiesa. “Green’s conjecture for curves on rational surfaces with an
anticanonical pencil”. In: Math. Z. 275.3-4 (2013), pp. 899–910.

[Lem] A. Lemmens. On the n-th row of the graded Betti table of an n-dimensional toric
variety. Preprint: https://arxiv.org/abs/1701.01393.

[LS11] N. Lubbes and J. Schicho. “Lattice polygons and families of curves on rational
surfaces”. In: J. Algebraic Combin. 34.2 (2011), pp. 213–236.

[LZ91] Jeffrey C. Lagarias and Günter M. Ziegler. “Bounds for lattice polytopes con-
taining a ﬁxed number of interior points in a sublattice”. In: Canad. J. Math.
43.5 (1991), pp. 1022–1035.

[Miu93] S. Miura. “Algebraic geometric codes on certain plane curves”. In: Electron-
ics and Communications in Japan (Part III: Fundamental Electronic Science) 76.12
(1993), pp. 1–13.

[Mum71] D. Mumford. “Theta characteristics of an algebraic curve”. In: Ann. Sci. École
Norm. Sup. (4) 4 (1971), pp. 181–192.

[Rat] J. Rathmann. An effective bound for the gonality conjecture. Preprint: https :
//arxiv.org/abs/1604.06072.

[Sch03a] J. Schicho. “Simpliﬁcation of surface parametrizations—a lattice polygon ap-
proach”. In: J. Symbolic Comput. 36.3-4 (2003). International Symposium on
Symbolic and Algebraic Computation (ISSAC’2002) (Lille), pp. 535–554.

[Sch03b] F.-O. Schreyer. “Some topics in computational algebraic geometry”. In: Ad-
vances in algebra and geometry (Hyderabad, 2001). Hindustan Book Agency,
New Delhi, 2003, pp. 263–278.

[Sch04] H. Schenck. “Lattice polygons and Green’s theorem”. In: Proc. Amer. Math.
Soc. 132.12 (2004), pp. 3509–3512.

[Sch86] F.-O. Schreyer. “Syzygies of canonical curves and special linear series”. In:
Math. Ann. 275.1 (1986), pp. 105–137.

[Ser87] F. Serrano. “Extension of morphisms deﬁned on a divisor”. In: Math. Ann.
277.3 (1987), pp. 395–413.

[Smi15] G. Smith. “Brill-Noether theory of curves on toric surfaces”. In: J. Pure Appl.
Algebra 219.7 (2015), pp. 2629–2636.

[SV87] K.-O. Stöhr and J. Voloch. “A formula for the Cartier operator on plane alge-
braic curves”. In: J. Reine Angew. Math. 377 (1987), pp. 49–64.
