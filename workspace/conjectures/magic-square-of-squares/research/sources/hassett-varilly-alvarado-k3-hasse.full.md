<!-- source: https://www.math.brown.edu/bhassett/papers/K3Hasse/K3Hasse10.pdf | converted from PDF -->

FAILURE OF THE HASSE PRINCIPLE ON GENERAL K3 SURFACES

BRENDAN HASSETT AND ANTHONY V ´ARILLY-ALVARADO

Abstract. We show that transcendental elements of the Brauer group of an algebraic
surface can obstruct the Hasse principle. We construct a general K3 surface X of degree 2
over Q, together with a two-torsion Brauer class α that is unramiﬁed at every ﬁnite prime,
but ramiﬁes at real points of X. Motivated by Hodge theory, the pair (X, α) is constructed
from a double cover of P2 × P2 ramiﬁed over a hypersurface of bi-degree (2, 2).

1. Introduction

Let X be a smooth projective geometrically integral variety over a number ﬁeld k. If X has
a kv-point for every place v of k (equivalently, if its set X(Ak) of adelic points is nonempty),
yet it does not have a k-point, then we say that X does not satisfy the Hasse principle.
Manin [Man71] showed that any subset S of the Brauer group Br(X) := H 2
´et(X, Gm) may
be used to construct an intermediate set

X(k) ⊆ X(Ak)
S ⊆ X(Ak)

that often explains failures of the Hasse principle, in the sense that X(Ak)
S may be empty,
even if X(Ak) is not. In this case, we say there is a Brauer-Manin obstruction to the Hasse
principle for X. See §4 for the deﬁnition of X(Ak)
S.
There is a ﬁltration of the Brauer group Br0(X) ⊆ Br1(X) ⊆ Br(X), where

Br0(X) := im (Br(k) → Br(X)) ,

Br1(X) := ker (Br(X) → Br(X)
) ,

and X = X ×k k for a ﬁxed algebraic closure k of k. Elements in Br0(X) are said to be
constant; class ﬁeld theory shows that if S ⊆ Br0(X), then X(Ak)
S = X(Ak), so these
elements cannot obstruct the Hasse principle. Elements in Br1(X) are called algebraic; the
remaining elements of the Brauer group are transcendental.
There is a large body of literature, spanning the last four decades, on algebraic Brauer
classes and algebraic Brauer-Manin obstructions to the Hasse principle and the related no-
tion of weak approximation (i.e., where sets S ⊆ Br1(X) suﬃce to explain failures of these
phenomena); see, for example [Man74, BSD75, CTCS80, CTSSD87, CTKS87, SD93, SD99,
KT04, Bri06, BBFL07, Cun07, Cor07, KT08, Log08, VA08, LvL09, EJ10a, EJ10b, Cor10,
EJ11a]. The systematic study of these obstructions beneﬁts in no small part from an iso-
morphism

(1) Br1(X)/ Br0(X) ∼
−→ H 1(k, Pic(X)
),

coming from the Hochschild-Serre spectral sequence.

2000 Mathematics Subject Classiﬁcation. Primary 11 G35; Secondary 14 G05, 14 F22.
This research was supported by National Science Foundation Grants 0554491, 0901645, and 1103659.
1

2 BRENDAN HASSETT AND ANTHONY V ´ARILLY-ALVARADO

Obstructions arising from transcendental elements, on the other hand, remain mysterious,
because it is diﬃcult to get a concrete handle on transcendental elements of the Brauer
group; there is no known analogue of (1) for the group Br(X)/ Br1(X).
If X is a curve, or a surface of negative Kodaira dimension, then Br (X) = 0, so the
Brauer group is entirely algebraic. On the other hand, in 1996 Harari constructed a 3-fold
with a transcendental Brauer-Manin obstruction to the Hasse principle [Har96]. This begs
the question: what about algebraic surfaces? Can transcendental Brauer classes obstruct
the Hasse principle on an algebraic surface? A natural place to study this question is the
class of K3 surfaces; they are arguably some of the simplest surfaces of nonnegative Kodaira
dimension in the Castelnuovo-Enriques-Manin classiﬁcation. The group Br(X)/ Br1(X) is
ﬁnite for a K3 surface [SZ08], but it can be nontrivial.
With arithmetic applications in mind, several authors over the last decade have con-
structed explicit transcendental elements on K3 surfaces [Wit04, SSD05, HS05, Ier10, Pre10,
ISZ11, SZ12]. Wittenberg, Ieronymou and Preu have used these elements to exhibit obstruc-
tions to weak approximation (i.e., density of X(k) in ∏
v X(kv) for the product of the v-adic
topologies). In all cases the K3 surfaces considered have elliptic ﬁbrations that play a vital
role in the construction of transcendental classes.
Inspired by Hodge-theoretic work of van Geemen and Voisin [vG05, Voi86], we recently
constructed a K3 surface with geometric Picard number 1 (and hence no elliptic ﬁbrations),
together with a transcendental Brauer class α obstructing weak approximation; see [HVAV11]
(joint with Varilly). The pair (X, α) was obtained from a cubic fourfold containing a plane.
At the time, we were unable to extend our work to obtain counterexamples to the Hasse
principle, in part because we were unable to control the invariants of α at real points of X—
ironically, this is precisely the reason we obtain a counterexample to weak approximation!
See Remarks 1.3 as well.
Taking advantage of some recent developments (see Remarks 1.3), our goal in this paper is
to rectify the above situation and show, once and for all, that transcendental Brauer classes
on algebraic surfaces can obstruct the Hasse principle.

Theorem 1.1. Let X be a K3 surface of degree 2 over a number ﬁeld k, with function ﬁeld
k(X), given as a sextic in the weighted projective space P(1, 1, 1, 3) = Proj k[x0, x1, x2, w] of
the form

(2) w2 = −1
2 · det
 

2A B C
B 2D E
C E 2F
 

 ,

where A, . . . , F ∈ k[x0, x1, x2] are homogeneous quadratic polynomials. Then the class A of
the quaternion algebra (B2 − 4AD, A) in Br(k(X)) extends to an element of Br(X).
When k = Q, there exist particular polynomials A, . . . , F ∈ Z[x0, x1, x2] such that X has
geometric Picard rank 1 and A gives rise to a transcendental Brauer-Manin obstruction to
the Hasse principle on X.

Remark 1.2. In [vG05, §9], Van Geemen showed that every Brauer class α of order 2 on a
polarized complex K3 surface (X, f ) of degree 2 with Pic(X) = Zf gives rise to (and must
arise from) one of three types of varieties:
• a smooth complete intersection of three quadrics in P5 (itself a K3 surface), or

FAILURE OF THE HASSE PRINCIPLE ON GENERAL K3 SURFACES 3

• a cubic fourfold containing a plane, or
• a double cover of P2 × P2 ramiﬁed along a hypersurface of bidegree (2, 2).

More precisely, the class α determines a sublattice Tα ⊆ TX of the transcendental lattice of
X which is a polarized Hodge structure, a twist of which is Hodge isometric to a primitive
sublattice of the middle cohomology of one the three types of varieties above. See §2 for
more details.
The Azumaya algebra A of Theorem 1.1 represents a class arising from a double cover of
P2 × P2 ramiﬁed along a hypersurface of bidegree (2, 2).

Remarks 1.3. We record a few remarks on the computational subtleties behind the second
part of Theorem 1.1:

(1) For computational purposes, we go in a direction “opposite” to van Geemen: starting
from one of the three types of varieties described in Remark 1.2, deﬁned over a number
ﬁeld k, we recover a K3 surface X over k of degree 2, together with a 2-torsion
Azumaya algebra A. Unfortunately, there is no guarantee that X has geometric
Picard number ρ = 1; in fact, it need not. We use a recent theorem of Elsenhans and
Jahnel [EJ11c] to certify that our example has ρ = 1.
(2) Curiously, one of the most delicate steps in the proof of Theorem 1.1 is determining
the primes of bad reduction of X. We have to factor an integer with 318 decimal
digits, whose smallest prime factor turns out to have 66 digits!
(3) We use some of our work on varieties parametrizing maximal isotropic subspaces of
families of quadrics admitting at worst isolated singularities to show that A can ram-
ify only at the real place, 2-adic places and primes of bad reduction for X [HVAV11,
§3]. These are thus the only places where the local invariants of A can be nontrivial.
(4) We rely on recent work of Colliot-Th´el`ene and Skorobogatov [CTS13] to control the
local invariants for the algebra A at odd primes of bad reduction.

Remark 1.4. The Azumaya algebra of Theorem 1.1 looks remarkably similar to the algebra
we used in [HVAV11] to exhibit counter-examples to weak approximation. This is not a
coincidence: compare Theorem 3.2 with [HVAV11, Theorem 5.1].

Outline of the paper. In §2 we explain the content of Remark 1.2 in detail, following
van Geemen [vG05]. The section is not logically necessary for the paper, but we include
it for completeness because it explains how to construct, in principle, Azumaya algebras
representing every two-torsion Brauer class on a general K3 surface of degree 2.
In §3, we explain how to explicitly construct, from a double cover of P2 × P2 ramiﬁed
along a hypersurface of bidegree (2, 2), a pair (X, α) where X is a K3 surface of degree
2 and α ∈ Br(X)[2] is an Azumaya algebra. We work mostly over a discrete valuation
ring (see Theorem 3.2). This ﬂexibility later aﬀords us control, when working over number
ﬁelds, of local invariants at places where α ramiﬁes; see Lemma 4.4. In §4, we give a
collection of suﬃcient conditions to control the evaluation maps of α over number ﬁelds,
specializing ultimately to the case k = Q. Notably, Proposition 4.1 (due to Colliot-Th´el`ene
and Skorobogatov) together with Lemma 4.2 show that the evaluation maps of α are constant
at non-2-adic ﬁnite places of bad reduction of X whenever the singular locus consists of r < 8
ordinary double points.

4 BRENDAN HASSETT AND ANTHONY V ´ARILLY-ALVARADO

We use this preparatory work to give an example in §5 of a surface witnessing the second
part of Theorem 1.1. In §6 we give details of how we found the example of §5, using a
computer.

Acknowledgments. We thank Olivier Wittenberg for helpful comments and correspon-
dence on transcendental Brauer classes on general K3 surfaces of degree 2 [Wit]. We also
thank the referee for their careful reading of the manuscript and suggesting valuable im-
provements. Our computations were carried out using Macaulay 2 [GS], Magma [BCP97] and
SAGE [S
+09]
 2. Lattices and Hodge theory

In this section, all varieties are deﬁned over C. Our goal here is to outline van Geemen’s
geometric constructions representing two-torsion Brauer classes on a K3 surface of degree
2 and Picard rank 1. Strictly speaking, this section is not logically necessary in the proof
of Theorem 1.1, and we use only one of the three constructions described. We include it,
however, so that readers not acquainted with these ideas get a clear sense of the geometric
motivation behind Theorem 1.1.
Let X be a complex K3 surface. Regarding its middle cohomology as a lattice with respect
to the intersection form, we can write [LP81, §1]

(3) H 2(X, Z) ≃ U 3 ⊕ E8(−1)
2 =: Λ

where
 U = ⟨e, f ⟩, with intersections e f
e 0 1
f 1 0
and E8 is the positive deﬁnite lattice arising from the corresponding root system, i.e., the
unique positive deﬁnite even unimodular lattice of rank eight. Let e and f denote the
generators of the ﬁrst summand U in (3), and h ∈ H 2(X, Z) a primitive vector with h · h =
2d > 0. The isomorphism (3) can be chosen so that

h ↦→ e + df.

Writing v = e − df , we have

h
⊥ ≃ Zv ⊕ Λ
′, where Λ
′ := U 2 ⊕ E8(−1)
2.

Let (X, h) be a polarized K3 surface of degree 2d, i.e., h · h = 2d; assume that Pic(X) is
generated by h. Since H 3(X, Z) = 0, the long exact sequence in cohomology associated to
the exponential sequence gives rise to the short exact sequence

0 → H 2(X, Z)/ ⟨h⟩ → H 2(X, OX) → Br X → 0.

Applying the snake lemma to the diagram obtained by multiplication by 2 on this exact
sequence, we see that two-torsion elements of the Brauer group of X may be interpreted as
elements α ∈ H 2(X, Z/2Z)/ ⟨h⟩ .
Under this identiﬁcation, we can express

α = n ¯f + ¯λα, n = 0, 1,

FAILURE OF THE HASSE PRINCIPLE ON GENERAL K3 SURFACES 5

where ¯f is the image of f and ¯λα is the image of some λα ∈ Λ
′. Using the non-degenerate
cup product on H 2(X, Z), let α⊥ be the kernel of the map h
⊥ → Z/2Z, x ↦→ x · (nf + λα).
We have α⊥ ⊂ h
⊥ ⊂ H 2(X, Z),
where the ﬁrst subgroup has index two when α ̸= 0.
Assume from now on that α ̸= 0. If n = 1 and λα = 0, then α⊥ = Z(2v) ⊕ Λ
′, a lattice
with discriminant group Z/8dZ, generated by v/2d. If λα ̸= 0, choose µ ∈ Λ
′ satisfying

(4) µ · λα ≡ 1 mod 2.

In this case α⊥ = Z(v + µ) + {λ′ ∈ Λ
′ : λ′ · λα ≡ 0 mod 2},
a lattice with discriminant group generated by (−v + 2dλα)/4d, which is therefore Z/8dZ.
If n = 0 then λα ̸= 0 and we can also choose µ ∈ Λ
′ satisfying (4). We have

α⊥ = Zv ⊕ {λ′ ∈ Λ
′ : λ′ · λα ≡ 0 mod 2},

a lattice with discriminant group (Z/2dZ) ⊕ (Z/2Z)
2, where the last two summands are
generated by λα/2 and µ.
General results on quadratic forms (see, for example, [Nik79]) make it possible to classify
even indeﬁnite quadratic forms with prescribed rank and discriminant group H, provided
the rank of the form is signiﬁcantly larger than the number of generators of H. In particular,
van Geemen [vG05, Proposition 9.2] classiﬁes isomorphism classes of lattices α⊥ arising from
this construction:
• if n = 0 there is a unique such lattice, up to isomorphism;
• if n = 1 and d is even then there is a unique such lattice up to isomorphism;
• if n = 1 and d is odd then there are two such lattices up to isomorphism, depending
on the parity of λα · λα/2.
He goes further when d = 1, oﬀering geometric constructions of varieties having primitive
Hodge structure isomorphic to α⊥. We elaborate on his description:

Case n = 0: Let W ⊂ P2 × P2 denote a smooth hypersurface of bidegree (2, 2) and Y →
P2 ×P2 the double cover branched along W . Let h1 and h2 denote the divisors on Y obtained
by pulling back the hyperplane classes from the factors. We have intersections:

h
2
1 h1h2 h
2
2
h
2
1 0 0 2
h1h2 0 2 0
h
2
2 2 0 0

The non-zero Hodge numbers of Y are:

h
00 = h
44 = 1, h
11 = h
33 = 2, h
13 = h
31 = 1, h
22 = 22.

Consider the weight-two Hodge structure
〈h
2
1, h1h2, h
2
2〉⊥ ⊂ H 4(Y )(1)

having underlying lattice M , with respect to the intersection form. The lattice M is even
indeﬁnite, and it has the same rank and discriminant group as α⊥. Thus

M ≃ α⊥.

6 BRENDAN HASSETT AND ANTHONY V ´ARILLY-ALVARADO

Case n = 1, λα · λα ≡ 0 (mod 4): In this case, there exists a primitive embedding

α⊥ ↪→ U 3 ⊕ E8(−1)
2,

unique up to automorphisms of the source and target. We can interpret the image as the
primitive cohomology of a polarized K3 surface (S, f ) with f · f = 8.

Case n = 1, λα · λα ≡ 2 (mod 4): Let Y be a cubic fourfold containing a plane P , with
hyperplane class h. We have the intersections:

h
2 P
h
2 3 1
P 1 3

The non-zero Hodge numbers of Y are

h
00 = h
44 = 1, h
11 = h
33 = 1, h
13 = h
31 = 1, h
22 = 21.

The weight-two Hodge structure 〈h
2, P 〉⊥ ⊂ H 4(Y )(1)

has underlying lattice isomorphic to α⊥.

The last two geometric constructions yield explicit unramiﬁed Azumaya algebras over
the degree two K3 surface. The connection between cubic fourfolds containing planes and
quaternion algebras over the K3 surface can be found in [HVAV11]; the other construction
goes back to Mukai [Muk84]: A degree eight K3 surface S is generally a complete intersection
of three quadrics in P5, and the discriminant curve of the corresponding net is a smooth plane
sextic. Let X be a degree-two K3 surface obtained as the double cover of P2 branched along
this sextic. The variety F parametrizing maximal isotropic subspaces of the quadrics cutting
out S admits a morphism (cf. [HVAV11, §3]) F → X, which is smooth with geometric ﬁbers
isomorphic to P3.
In this paper, we focus on the ﬁrst case, and use the resulting Azumaya algebra for
arithmetic purposes.
 3. Unramified conic bundles

Let k be an algebraically closed ﬁeld of characteristic ̸= 2, and let W be an irreducible
type (2, 2) divisor on P2 × P2, that is, hypersurface of bidegree (2, 2). The two projections
π1 : W → P2 and π2 : W → P2 deﬁne conic bundle structures on W . Let Y → P2 × P2 be the
double cover branched along W . Composing this map with the projections onto the factors
we obtain two quadric surface bundles qi : Y → P2. Note that the πi and qi need not be ﬂat
morphisms.
Let x0, x1, x2 and y0, y1, y2 denote homogeneous coordinates on the P2’s. The equation
for W may be expressed as a quadratic form in the yj’s with coeﬃcients quadratic in the
xj’s (or vice versa). The determinant of the associated symmetric 3 × 3 matrix of quadratic
forms gives the locus over which π1 (or π2) ramiﬁes. This determinant might be identically
zero. Otherwise, we obtain plane sextic curves C1 and C2 over which π1 and π2 (as well as
q1 and q2) are ramiﬁed. Let φi : Xi → P2 be a double cover of P2 branched over Ci; if Ci is
a smooth curve then Xi is a K3 surface of degree 2.

FAILURE OF THE HASSE PRINCIPLE ON GENERAL K3 SURFACES 7

If W has at worst isolated singularities then the geometric generic ﬁber of πi (and hence
of qi) is smooth. Indeed, if the geometric generic ﬁber of πi were singular then there would
exist a generically ´etale V → P2 such that V ×P2 W is singular over the generic point of V .
Here we are using the fact that the characteristic ̸= 2. Thus it follows that C1 and C2 are
curves.

Lemma 3.1. Retain the notation above and assume that C1 and C2 are curves. If Y (equiv-
alently, W ) is not smooth then neither C1 nor C2 is smooth. On the other hand, if W is
smooth then each πi is ﬂat and Ci is singular if πi has a geometric ﬁber of rank 1, i = 1, 2.

Proof. An easy application of the Jacobian criterion shows that Y is smooth if and only if
W is smooth. We use the latter scheme to prove the remaining claims of the lemma.
Let w ∈ W be a singular point, ci ∈ Ci its images under projection, (u0, u1) local coordi-
nates of the ﬁrst P2 centered at c1, and (v0, v1) local coordinates of the second P2 centered
at c2. The deﬁning equation of W takes the form

a(u0, u1)v2
0 + b(u0, u1)v0v1 + 2d(u0, u1)v2
1 + c(u0, u1)v0 + e(u0, u1)v1 = 0,

where the coeﬃcients are quadratic in u0 and u1, and c(0, 0) = e(0, 0) = 0. Note that
W would be singular if the coeﬃcients a(u0, u1), . . . , e(u0, u1) were all zero. The deﬁning
equation for C1 is therefore
 det
 

2a b c
b 2d e
c e 0



 = 0.

Expanding this out, we get bce − ae
2 − c2d = 0,
where each term vanishes to order ≥ 2 at c1 = (0, 0).
The last statement of the lemma is a consequence of [Bea77, Prop. 1.2]. □

Theorem 3.2. Let O denote a discrete valuation ring with residue ﬁeld F of characteris-
tic ̸= 2. Let W be a type (2, 2) divisor in P2 × P2 ﬂat over Spec O, and Y → P2 × P2 a
double cover simply branched along W. For i = 1, 2, let qi : Y → P2 denote the quadric
surface bundle obtained by projecting onto the i-th factor, and let Ci ⊂ P2 be its discriminant
divisor. Assume that for some j ∈ {1, 2}, Cj is ﬂat over O, and that (Cj)F is smooth.
Let rj : Fj → P2 be the relative variety of lines of qj. Then the Stein factorization

ri : Fj → Xj φj
−→ P2

consists of a smooth P1-bundle followed by a degree-two cover of P2, which is a K3 surface.

Proof. By Lemma 3.1, smoothness of (Cj)F implies smoothness of WF, and hence of YF. The
same lemma shows that the ﬁbers of (qj)F have at worst isolated singularities. On the other
hand, the morphism qj : Y → P2 is ﬂat, and thus Y is a regular scheme. Geometric ﬁbers of qj
over the generic point of Spec O with non-isolated singularities specialize to geometric ﬁbers
over the closed point with non-isolated singularities. Hence the ﬁbers of qj have isolated
singularities. The theorem now follows directly from [HVAV11, Proposition 3.3]: The Stein
factorization of the variety of maximal isotropic subspaces of a family of even-dimensional
quadric hypersurfaces with (at worst) isolated singularities is isomorphic to the discriminant
double cover of the base.

8 BRENDAN HASSETT AND ANTHONY V ´ARILLY-ALVARADO

Since the morphism Cj → P2 is ﬂat, smoothness of (Cj)F implies that Cj is regular. Hence
Xj is a K3 surface over Spec O. □

The smooth P1-bundle rj : Fj → Xj may be interpreted as a two-torsion element of Br(Xj).
Without loss of generality, assume in the hypotheses of Theorem 3.2 that (C1)F is smooth;
we omit the subscript j = 1 from here on in. We give an explicit quaternion algebra over
k(X ) representing the Brauer class of F → X . Express

P2 × P2 = Proj O[x0, x1, x2] ×O Proj O[y0, y1, y2]

so the equation for W takes the form

0 = A(x0, x1, x2)y2
0 + B(x0, x1, x2)y0y1 + C(x0, x1, x2)y0y2
+ D(x0, x1, x2)y2
1 + E(x0, x1, x2)y1y2 + F (x0, x1, x2)y2
2,
(5)

for some homogeneous quadratic polynomials A, . . . , F ∈ O[x0, x1, x2]. The coeﬃcients are
unique modulo multiplication by a common unit in O.
Consider the bigraded ring O[x0, x1, x2, y0, y1, y2, v] where

deg(xi) = (1, 0), deg(yi) = (0, 1), deg(v) = (1, 1),

and let R := ⊕

n∈Z O[x0, x1, x2, y0, y1, y2, v](n,n)

denote the graded subring generated by elements of bidegree (n, n) for some n. Then an
equation for Y ⊂ Proj R is

v2 = A(x0, x1, x2)y2
0 + B(x0, x1, x2)y0y1 + C(x0, x1, x2)y0y2
+ D(x0, x1, x2)y2
1 + E(x0, x1, x2)y1y2 + F (x0, x1, x2)y2
2.
(6)

The quadric surface bundle q : Y → P2 is ramiﬁed over the curve

(7) C : det
 




2A B C 0
B 2D E 0
C E 2F 0
0 0 0 −2





 = 0.

Thus, after rescaling, the K3 surface X is described by the hypersurface

(8) w2 = −1
2 · det(M )

in P(1, 1, 1, 3), where M ∈ Mat3(O[x0, x1, x2]) is the leading 3 × 3 principal minor of the
matrix in (7). The factor − 1
2 is dictated by the interpretation of the structure sheaf of X as
the discriminant algebra of our quadratic form in four variables (cf. [HVAV11, §3.1]).
The discussion in [HVAV11, §3.3] shows that the generic ﬁber of the map F → X is the
Severi-Brauer conic in Proj k(X )[Y0, Y1, Y2] given by

(9) AY 2
0 + BY0Y1 + CY0Y2 + DY 2
1 + EY1Y2 + F Y 2
2 = 0.

Essentially, given a smooth quadric surface whose discriminant double cover is split, each
component of the variety of lines on the surface is isomorphic to a smooth hyperplane section
of the surface. Let

MA := 4DF − E2, MD := 4AF − C 2, and MF := 4AD − B2.

FAILURE OF THE HASSE PRINCIPLE ON GENERAL K3 SURFACES 9

Completing squares in (9), and renormalizing, we obtain

Y 2
0 = − MF
4A2 Y 2
1 − det(M )
2A · MF Y 2
2 .

Hence, by [GS06, Corollary 5.4.8], the conic (9) corresponds to the Hilbert symbol

(10) (− MF
4A2 , − det(M )
2A · MF
 ) .

Write A for the class of this symbol in Br(k(X )); A is unaﬀected by multiplication by squares
in either entry of a representative symbol. Since − 1
2 det(M ) is a square in k(X )
×, we see
that
 (−MF , A · MF ) = (−MF , A)

is another representative of A (the equality uses the multiplicativity of the Hilbert symbol
and the relation (−MF , MF ) = 1 [Ser73, III, Proposition 2]). Here we have the usual abuse
of notation: the entries are not rational functions, though they are homogeneous polynomials
of even degree.
Depending on how we complete squares and renormalize (9), we may obtain several rep-
resentatives of A:
 (−MF , A), (−MD, A), (−MF , D),

(−MA, D), (−MD, F ), (−MA, F ).
(11)

Proposition 3.3. Let X be a K3 surface of degree 2 over a number ﬁeld k, given as a sextic
in the weighted projective space P(1, 1, 1, 3) = Proj k[x0, x1, x2, w] of the form

w2 = −1
2 ·
 

2A B C
B 2D E
C E 2F
 

 ,

where A, . . . , F ∈ k[x0, x1, x2] are homogeneous quadratic polynomials. Then the class A of
the quaternion algebra (B2 − 4AD, A) in Br(k(X)) extends to an element of Br(X).

Proof. Let O be the valuation ring at some ﬁnite place of k where X has good reduction. The
proposition follows directly from Theorem 3.2 and the subsequent discussion, keeping track
of what is happening over the generic point of Spec O. Indeed, deﬁne W and Y, respectively,
by (5) and (6). The resulting curve (C1)k is the branch curve of the double cover X → P2,
which is smooth because X is a K3 surface, by hypothesis. □

Remark 3.4. The assortment of quaternion algebras (11) representing the class A of Propo-
sition 3.3 is useful for the computation of the invariant map on the image of the evaluation
map evA : X(Ak) → ⊕
v Br(kv), (Pv) ↦→ (A(Pv)
). The industrious reader can check that
at every local point of X, either the ﬁrst, fourth or ﬁfth representative of A in our list is
well-deﬁned; we shall not use this observation directly.

10 BRENDAN HASSETT AND ANTHONY V ´ARILLY-ALVARADO

4. Local Invariants

Let X be a smooth projective geometrically integral variety over a number ﬁeld k. For
S ⊆ Br(X), let

X(Ak)
S :=
 {

(Pv) ∈ X(Ak) : ∑

v invv A(Pv) = 0 for all A ∈ S
}
 .

The inclusion X(k) ⊆ X(Ak)
S follows from class ﬁeld theory. See [Sko01, §5.2] for de-
tails. The local invariants invv A(Pv) can be nonzero only at a ﬁnite number of places: the
archimedean places of k, the places of bad reduction of X, and places where the class A is
ramiﬁed.
We begin this section by explaining how recent work of Colliot-Th´el`ene and Skoroboga-
tov [CTS13] shows that local invariants are constant at certain ﬁnite places v of bad reduction
for X where the singular locus satisﬁes a technical hypothesis. Specializing to the case where
X is a K3 surface over a number ﬁeld k as in Proposition 3.3, this technical hypothesis is sat-
isﬁed provided the singular locus at v consists of r < 8 ordinary double points (Lemma 4.2).
We then show that the class A of Proposition 3.3 can ramify only over inﬁnite places,
2-adic places, and places of bad reduction for X. Finally, in the special case k = Q, we give
suﬃcient conditions for local invariants of A to be trivial at 2-adic points and nontrivial at
real points.

4.1. Places of bad reduction with mild singularities. In this section we use the fol-
lowing notation: k is a ﬁnite extension of Qp with a ﬁxed algebraic closure k, O denotes
the ring of integers of k, and F denotes its residue ﬁeld. We let X be a smooth, proper,
geometrically integral variety over k and write π : X → Spec O for a ﬂat proper morphism
with X = X ×O k.
The following proposition is a straightforward reﬁnement of [CTS13, Proposition 2.4],
using ideas in the remark on the case of bad reduction in [CTS13, §2]. We include the
details here for the reader’s convenience.

Proposition 4.1. Let ℓ ̸= p be a prime. Assume that X is regular with geometrically
integral ﬁbers over Spec O, and that the smooth locus X sm
F of the closed ﬁber is geometrically
irreducible and has no connected unramiﬁed cyclic geometric coverings of degree ℓ. If X(k) ̸=
∅, then, for A ∈ Br(X){ℓ}, the image of the evaluation map evA : X(k) → Br(k) consists of
one element.

Proof. Let Z be the largest open subscheme of X that is smooth over Spec O; note that
Z ×O k = X. Write ZF for its closed ﬁber, and note that ZF = X sm
F . Let Z (1)
F denote the
set of closed integral subvarieties of ZF of codimension 1. In [Kat86, Prop. 1.7], Kato shows
there is a complex

Br(X)[ℓ
n] res
−→ H 1(k(ZF), Z/ℓ
nZ
) → ⊕

Y ∈Z (1)
F
 H 0(k(Y ), Z/ℓ
nZ(−1)
).

(In Kato’s notation, take q = −1, i = −2, n ↦→ ℓ
n, and X ↦→ Z.) We claim that for
A ∈ Br(X)[ℓ
n], the residue res(A) ∈ H 1(k(ZF), Z/ℓ
nZ
) lies in the subgroup H 1
´et(ZF, Z/ℓ
nZ
).
Indeed, the group H 1(k(ZF), Z/ℓ
nZ
) classiﬁes connected cyclic covers of ZF. By Kato’s
complex, the cover W → ZF corresponding to res(A) is unramiﬁed in codimension one, and

FAILURE OF THE HASSE PRINCIPLE ON GENERAL K3 SURFACES 11

hence, by the Zariski-Nagata purity theorem [SGA03, Expos´e X, Th´eor`eme 3.1], W → ZF
is unramiﬁed.
The long exact sequence of low degree terms associated to the spectral sequence

Ep,q
2 := H p(F, H q
´et(ZF, Z/ℓ
nZ
)) =⇒ H p+q
´et (ZF, Z/ℓ
nZ)

starts as follows:

(12) 0 → H 1(F, Z/ℓ
nZ
) → H 1
´et(ZF, Z/ℓ
nZ
) → H 1
´et(ZF, Z/ℓ
nZ
)

Since, by hypothesis, ZF has no connected unramiﬁed cyclic geometric coverings of degree
ℓ, we have H 1
´et(ZF, Z/ℓ
nZ
) = 0.
We claim there is an element α ∈ Br(k){ℓ} such that A − α has trivial residues along
any codimension one subvariety of Z. Such a residue depends only on the local ring at
the generic point of the subvariety, so it suﬃces to consider residues along codimension one
subvarieties of generic ﬁber X of Z → Spec O, as well as the residue along the generic point
of the special ﬁber ZF. Since A belongs to Br(X), it can have a nonzero residue only at the
generic point of the special ﬁber ZF. As above, this residue lies in H 1
´et(ZF, Z/ℓ
nZ
). On the
other hand, local class ﬁeld theory shows that the invariant map Br(k)[ℓ
n] → H 1(F, Z/ℓ
nZ
)

is an isomorphism. We pick α ∈ Br(k){ℓ} so that its invariant in H 1(F, Z/ℓ
nZ
) coincides
with the preimage of res(A) in H 1(F, Z/ℓ
nZ
) for the map in (12).
By Gabber’s purity theorem [Fuj02], it follows that A − α ∈ Br(Z){ℓ} ⊆ Br(X){ℓ}. A
valuation argument shows that X(k) = X (O) = Z(O); see [Sko96, proof of Lemma 1.1(b)].
Since Br(O) = 0, we conclude that the images of the evaluation maps evA and evα in Br(k)
coincide; the latter consists of one element. □

Lemma 4.2. Suppose that p ̸= 2. Let X be a K3 surface deﬁned over k, and let π : X →
Spec O be a ﬂat proper morphism from a regular scheme with X = X ×O k. Assume that
the singular locus of the closed ﬁber X0 := XF has r < 8 points, each of which is an ordinary
double point. Then the smooth locus U ⊂ X0 has no connected unramiﬁed cyclic covers of
prime degree ℓ ̸= p.

Proof. Consider an algebraically closed ﬁeld F of characteristic diﬀerent from ℓ. Let Y be a
separated integral scheme over F with Γ(Y, O ∗
Y ) = F ∗; this is the case if Y is proper, or a
dense open subset of a proper scheme with complement of codimension ≥ 2. Then degree
ℓ cyclic ´etale covers of Y are classiﬁed by H 1
´et(Y, µℓ) [Mil80, ch.III]. The Kummer exact
sequence [Mil80, p.125] implies that H 1
´et(Y, µℓ) = Pic(Y )[ℓ], the ℓ-torsion subgroup.
Combining the canonical homomorphism from the Picard group to the Weil class group
and the restriction homomorphism on class groups yields

Pic(X0) ⊂ Cl(X0) ≃ Cl(U ) ≃ Pic(U ).

The quotient Pic(U )/ Pic(X0) is two-torsion. Indeed, ordinary double points are ´etale locally
isomorphic to quadric cones, whose local class group equals Z/2Z (generated by the ruling).
Thus for each closed point x ∈ X0, the quotient Pic(Spec OX0,x \ {x})/ Pic(Spec OX0,x) is
annihilated by two [Lip69, §14]. If ℓ ̸= 2 then this computation shows that Pic(U )[ℓ] =
Pic(X0)[ℓ], whence degree ℓ cyclic ´etale covers of U extend to X0.
We claim that Pic(X0)[ℓ] = 0 for each prime ℓ ̸= p. To prove this, replace k by the ramiﬁed
quadratic extension k′ with ring of integers O′, so that X ′ = X ×O O′ is singular over the

12 BRENDAN HASSETT AND ANTHONY V ´ARILLY-ALVARADO

double points of X0. Concretely, given p a uniformizer of O, p′ = √p the corresponding
uniformizer of O′, and x ∈ X0 an ordinary double point, then the ´etale local equation of X

p = uv + w2

pulls back to (p′)
2 = uv + w2.

Let ˜X → X ′ denote the blow-up of the resulting singularities, with central ﬁber the union
of the proper transform of X0 and the exceptional divisors

˜X0 = S ∪ E1 ∪ · · · ∪ Er, Ej ≃ P1 × P1.

(At the cost of passing to an algebraic space, we could blow down E1, . . . , Er along one of
the rulings of P1 × P1.) Note that S is the K3 surface obtained by resolving the ordinary
double points of X0. The pull-back homomorphism

Pic(X0) → Pic(S)

is injective since we may regard U as an open subset of both X0 and S. However, Pic(S) has
no ℓ-torsion: the specialization homomorphism [Ful98, §20.3]

Pic(Xk) → Pic(S)

is injective and any torsion of its cokernel is annihilated by p [MP09, Prop. 3.6].
We now focus on the case ℓ = 2. Let F1, . . . , Fr denote the exceptional divisors of S → X0,
which satisfy F 2
1 = · · · = F 2
r = −2, FiFj = 0, i ̸= j,

because X0 has ordinary double points.
There may exist ´etale double covers of U that fail to extend to ´etale covers of X0. Given
an ´etale double cover V → U , let ϖ : T → S denote the normalization of S in the function
ﬁeld of V . Since T is normal, ϖ is a ﬂat morphism [Eis95, Ex. 18.17], ´etale away from
F1 ∪ · · · ∪ Fr. Moreover, by purity of the branch locus, ϖ is branched over some subset

{Fj1, . . . , Fjs} ⊂ {F1, . . . , Fr}.

Since the characteristic is odd, ϖ is simply branched over these curves. Consequently,∑s
i=1 Fji = 2D for some D ∈ Pic(S), hence 4D2 = −2s. Since D2 is even, we conclude that
s ≡ 0 (mod 4), i.e., s = 0 or 4. The case s = 0 is impossible, since this would mean that S
admits an ´etale cyclic cover with degree prime to the characteristic. The case s = 4 is also
impossible: By Riemann-Roch, we have

χ(OS(−D)) = 1

but h
2(OS(−D)) = h
0(OS(D)) = 0,

as any eﬀective divisor supported in the Fj (like 2D) is rigid. On the other hand, since a
divisor and its negative cannot both be eﬀective, we ﬁnd

h
0(OS(−2D)) = 0 which implies h
0(OS(−D)) = 0.

Therefore h
1(OS(−D)) = −1, which is a contradiction. □

FAILURE OF THE HASSE PRINCIPLE ON GENERAL K3 SURFACES 13

Remark 4.3. When r = 8, it is possible that a smooth resolution of X0 is a K3 surface with
a Nikulin involution, in which case the smooth locus U ⊂ X0 has a connected unramiﬁed
cyclic double cover [vGS07].

4.2. Places where A can ramify.

Lemma 4.4. Let X be a K3 surface over a number ﬁeld k as in Proposition 3.3. Let v be
a ﬁnite place of good reduction for X, and assume that v is not 2-adic. Then A does not
ramify at v. Consequently, invv A(P ) = 0 for all P ∈ X(kv).

Proof. We may assume without loss of generality that the coeﬃcients of A, . . . , F are integral.
Let Ov be the ring of integers of kv, and Fv its residue ﬁeld. Since X is smooth and proper
over k and has good reduction at v, there is a smooth proper morphism X → Spec Ov with
Xkv = X ×Ov kv. We will show that the class A ⊗ kv can be spread out to a class in Br(X ).
Since, by the valuative criterion of properness, we have X (Ov) = X(kv), it will follow that
A(P ) ∈ Br(Ov) = 0 for every point P ∈ X(kv), establishing all the claims of the proposition.
Deﬁne W and Y over Ov, respectively, by (5) and (6). The quadric surface bundle
(q1)F : YF → P2
F ramiﬁes over the discriminant curve of XFv → P2
Fv , which is smooth, be-
cause X has good reduction at v. By Theorem 3.2, there exists a smooth P1 bundle F → X ,
whose corresponding two-torsion class in Br(X ) is represented by the quaternion algebra
(B2 − 4AB, A), by the discussion following Theorem 3.2. Thus A ∈ Br(X ), as claimed. □

4.3. Real and 2-adic invariants. In this section we use the notation of Proposition 3.3,
specializing to the case k = Q. The following lemma gives a suﬃcient condition to guarantee
that the local invariants of A at real points of X are always non-trivial.

Lemma 4.5. Suppose that the quadratic forms A, B, C, D, E and F satisfy
(1) A, D and F are negative deﬁnite,
(2) B, C and E are positive deﬁnite.
Then, for any real point of X, we have

MA > 0, MD > 0 and MF > 0.

Proof. First, observe that we can write 1
2 det(M ) as

(13) A · MA − (C 2D + B2F − BCE).

Let P be a real point of X, so that 1
2 det(M ) ≤ 0 holds at P . Our hypotheses on A, . . . , F
imply that (C 2D + B2F − BCE)(P ) < 0.

Suppose ﬁrst that MA ≤ 0. Then at P we have

1
2 det(M ) = A︸︷︷︸
<0 · MA︸︷︷︸
≤0 −(C 2D + B2F − BCE︸ ︷︷ ︸
<0 ) > 0,

a contradiction. Hence MA > 0 at P . A similar argument shows the remaining two cases. □

Corollary 4.6. Suppose the hypotheses of Lemma 4.5 hold. Then the local invariant of A
at every real point of X is nontrivial.

14 BRENDAN HASSETT AND ANTHONY V ´ARILLY-ALVARADO

Proof. It suﬃces to show that, for any real point P of X, there is a quaternion algebra
representing A whose entries are both negative at P . Using the six representatives (11) of
A, together with Lemma 4.5, the result follows. □

Next, we write down a suﬃcient condition to guarantee that the local invariant map on
A is constant and trivial on 2-adic points. Write v2 : Q2 → Z ∪ {∞} for the standard 2-adic
valuation. Recall that a ∈ Q
×
2 is a square if and only if v2(a) is even and if a/2
v2(a) ≡ 1 mod 8.
Let P = [x0 : x1 : x2 : w] denote a 2-adic point of X. We may assume without loss of
generality that x0, x1 or x2 are elements of Z2, at least one of which is a 2-adic unit. Suppose
ﬁrst that x0 is a 2-adic unit, so that v2(x0) = 0. We use the representative (−MF , A) of A
to evaluate invariants at P . Write

A = A1x2
0 + A2x0x1 + A3x0x2 + A4x2
1 + A5x1x2 + A6x2
2,

and suppose that the coeﬃcients of A satisfy

A1 ≡ 1 mod 8, and v2(Ai) ≥ 3 for i = 2, . . . , 6.

Then, at P , we have A ≡ 1 mod 8 (since v2(x0) = 0) so A is a 2-adic square. It follows that
inv2 A(P ) = 0, provided that MF (P ) ̸= 0. To ensure this, we impose restrictions on the
coeﬃcients of the quadratic form

B = B1x2
0 + B2x0x1 + B3x0x2 + B4x4
1 + B5x1x2 + B6x2
2.

Suppose that v2(B1) = 0, and v2(Bi) ≥ 1 for i = 2, . . . , 6.
Then, since v2(x0) = 0, it follows that

v2(MF (P )) = v2(B(P )) = 0

and hence MF ̸= 0 at P .
To ensure that 2-adic invariants of A are trivial at points where v2(x1) = 0, we use the
representative (−MA, D) of A and constrain the coeﬃcients of D and E, respectively, in a
manner analogous to how we constrained the coeﬃcients of A and B. We proceed similarly
for 2-adic points with v2(x2) = 0, this time using the representative (−MD, F ) and we
constrain the coeﬃcients of C and F . We summarize our discussion in the following lemma.

Lemma 4.7. Write

A = A1x2
0 + A2x0x1 + A3x0x2 + A4x2
1 + A5x1x2 + A6x2
2,

B = B1x2
0 + B2x0x1 + B3x0x2 + B4x2
1 + B5x1x2 + B6x2
2,

C = C1x2
0 + C2x0x1 + C3x0x2 + C4x2
1 + C5x1x2 + C6x2
2,

D = D1x2
0 + D2x0x1 + D3x0x2 + D4x2
1 + D5x1x2 + D6x2
2,

E = E1x2
0 + E2x0x1 + E3x0x2 + E4x2
1 + E5x1x2 + E6x2
2,

F = F1x2
0 + F2x0x1 + F3x0x2 + F4x2
1 + F5x1x2 + F6x2
2.

Suppose that the coeﬃcients of these quadratic forms satisfy:
(1) A1 ≡ 1 mod 8, and v2(Ai) ≥ 3 for i ̸= 1.
(2) v2(B1) = 0, and v2(Bi) ≥ 1 for i ̸= 1.
(3) v2(C6) = 0, and v2(Ci) ≥ 1 for i ̸= 6.
(4) D4 ≡ 1 mod 8, and v2(Di) ≥ 3 for i ̸= 4.

FAILURE OF THE HASSE PRINCIPLE ON GENERAL K3 SURFACES 15

(5) v2(E4) = 0, and v2(Ei) ≥ 1 for i ̸= 4.
(6) F6 ≡ 1 mod 8, and v2(Fi) ≥ 3 for i ̸= 6.
Then, for every 2-adic point P of X, we have inv2 A(P ) = 0. □

5. An example

Consider the quadrics

A := −7x2
0 − 16x0x1 + 16x0x2 − 24x2
1 + 8x1x2 − 16x2
2
B := 3x2
0 + 2x0x2 + 2x2
1 − 4x1x2 + 4x2
2
C := 10x2
0 + 4x0x1 + 4x0x2 + 4x2
1 − 2x1x2 + x2
2
D := −16x2
0 + 8x0x1 − 23x2
1 + 8x1x2 − 40x2
2
E := 4x2
0 − 4x0x2 + 11x2
1 − 4x1x2 + 6x2
2
F := −40x2
0 + 32x0x1 − 40x2
1 − 8x1x2 − 23x2
2.

(14)

Let W ⊂ Proj Q[x0, x1, x2]×Proj Q[y0, y1, y2] be the type (2, 2) divisor given by the vanishing
of the bihomogeneous polynomial

A(x0, x1, x2)y2
0 + B(x0, x1, x2)y0y1 + C(x0, x1, x2)y0y2
+ D(x0, x1, x2)y2
1 + E(x0, x1, x2)y1y2 + F (x0, x1, x2)y2
2.
(15)

As in §3, the projections πi : W → P2 give conic bundle structures on W ramiﬁed over
plane sextics Ci, i = 1, 2. An equation for C1 is then given by f := − 1
2 det(M ) = 0, with M
as in (8). An equation for C2 can be found analogously. The Jacobian criterion shows that
both C1 and C2 are smooth; thus, for i = 1, 2, the double cover Xi → P2 ramiﬁed along Ci
is a K3 surface of degree 2.

5.1. Primes of bad reduction. The primes of bad reduction of X1 and C1 coincide. The
latter divide the generator m of the ideal obtained by saturating
〈f, ∂f
∂x0 , ∂f
∂x1 , ∂f
∂x2
 〉 ⊂ Z[x0, x1, x2]

by the irrelevant ideal and eliminating x0, x1 and x2. We obtain

m = 1115508232640214856843363784231663793779083264535962688555888430968
8933364438401787008291918987282105867611490800785997644322303281186
8922614222749465991103128446037422257623280138072129654879995620391
0907629715637695773281604080143775185215794393627484442538367517916
8651952191024387026109016400178074232186309443422761817391984342483
34511814400.

Standard factorization methods quickly reveal a few small prime power factors of m:

m = 2
8 · 5
2 · 7 · 89 · 173 · 257
2 · 263 · 650779
2 · m′.

The remaining factor m′ has 318 decimal digits. Factoring m′ with present day mathematical
and computational technology is a diﬃcult problem. However, the presence of the second

16 BRENDAN HASSETT AND ANTHONY V ´ARILLY-ALVARADO

K3 surface X2 supplies a backdoor solution: by Lemma 3.1, a prime of bad reduction for W
is a prime of bad reduction for both X1 and X2.
Another Groebner basis calculation shows that the primes of bad reduction of X2 divide

n := 18468445386704774116897512713438756322646374324269134481315634355660
59216198653927410468599212130905398491499555534045930594495263034981
50100881353352665095649631677613412079293044973446406764509694053112
10471631439070548340358668493117334582314574674926223315439909955021
6973495867514854209929544319382116616140800

Again, standard factorization methods give a few small prime power factors of n:

n = 2
11 · 5
2 · 7 · 89 · 173 · 263 · 461
2 · 6547
2 · n′,

where n′ has 290 decimal digits. Our observation says that we may reasonably expect that m′

and n′ have a large greatest common divisor (which is easily calculated using the Euclidean
algorithm). This is indeed the case:

gcd(m′, n′) := 809147864157687938441948148614369785987783654943839689121548451
788111145202992792430023470932052297439515068068797124401938255
799311490342451172887433057574480263654457987109316488649107.

Here a small miracle happens: gcd(m′, n′) is a prime number! This claim is rigorously veriﬁed
using elliptic curve primality proving algorithms [AM93], implemented in both SAGE and
magma. We are now in a position to complete the factorization of m, and hence compute the
primes of bad reduction for X1, which are:

2, 5, 7, 89, 173, 257, 263, 650779,
521219738678096220868573969913582546660848099260319499224599922739,

gcd(m′, n′).

We note that the penultimate prime in the list above occurs with multiplicity 2 in the
factorization of m. We will write q for this prime number in Table 1.

Remark 5.1. Our numerical experiments yield several “viable” pairs (X1, A) that could be
counter-examples to the Hasse principle explained by a transcendental Brauer-Manin ob-
struction arising from A, in the following sense: X1 has geometric Picard rank 1, and we
can control the real and 2-adic invariants of A (using Corollary 4.6 and Lemma 4.7). Out
of a dozen or so viable candidates that our initial search yielded, the example we present
is the only one we found for which gcd(m′, n′) is a prime number. One can obtain further
examples by computing 2-adic invariants by “brute force” instead of using Lemma 4.7.

5.2. Local points. By the Weil Conjectures, if p > 22 is a prime such that X1 has smooth
reduction (X1)p at p, then (X1)p has a smooth Fp-point, which can be lifted by Hensel’s
lemma to a smooth Qp-point. Thus, to show X1 is locally soluble, it suﬃces to verify that
X1 has local points at R (clear), and at Qp for primes p ≤ 19 and primes p > 19 where X1
has bad reduction. This is indeed the case: we substitute integers with small absolute value
for x0, x1, and x2, and check if − 1
2 det(M ) is a square in Qp. The results are recorded in
Table 1.
 FAILURE OF THE HASSE PRINCIPLE ON GENERAL K3 SURFACES 17

p x0 x1 x2 − 1
2 det(M )
2 0 0 −1 57872
3 −1 −1 1 1622952
5 −1 −1 −1 736256
7 −1 −1 0 256575
11 −1 −1 −1 736256
13 −1 −1 −1 736256
17 −1 −1 1 1622952
19 −1 −1 −1 736256
89 −1 0 −1 80019
173 −1 −1 0 256575
257 −1 −1 −1 736256
263 −1 −1 0 256575
650779 −1 −1 1 1622952
q −1 −1 −1 736256
gcd(m′, n′) −1 −1 −1 736256

Table 1. Verifying X1 has Qp-points at small p and primes of bad reduc-
tion. The numerical entries in the rightmost column are all squares in the
appropriate p-adic ﬁeld.

5.3. Picard Rank 1. In this section we show X1 has (geometric) Picard rank 1. This will
allow us to conclude that the obstruction to the Hasse principle arising from A is genuinely
transcendental. Until recently, the method to prove a K3 surface has odd Picard rank,
devised by van Luijk and reﬁned by Kloosterman, and Elsenhans and Jahnel [vL07, Klo07,
EJ11b], required point counting over extensions of the residue ﬁeld at two primes of good
reduction. A recent result of Elsenhans and Jahnel allows us to prove odd Picard rank using
information at two primes, but counting points over extensions of a single residue ﬁeld.

Theorem 5.2 ([EJ11c]). Let f : X → Spec Z be a proper, ﬂat morphism of schemes. Suppose
there is a rational prime p ̸= 2 such that the ﬁber Xp of f at p satisﬁes H 1(Xp, OXp) = 0.
Then the specialization homomorphism Pic(XQ) → Pic(XFp) has torsion-free cokernel.

We deduce the following generalization of [EJ11c, Example 1.6].

Proposition 5.3. Let X be a K3 surface of degree 2 over Q, given as a double cover π : X →
P2 ramiﬁed over a smooth plane sextic curve C. Let p and p′ denote two odd primes of good
reduction for X. Assume that there exists a line ℓ that is tritangent to the curve Cp, and
suppose further that Pic(X p) has rank 2 and is generated by the curves in π−1
p (ℓ). If there
are no tritangent lines to the curve Cp′, then Pic(X) has rank 1.

Proof. Since Pic(X) injects into Pic(X p), if Pic(X) has rank 2, then we claim the tritangent
line ℓ must lift to a tritangent line L in characteristic 0. To see this, note that by Theorem 5.2,
the components of the pullback of ℓ to X p lift to divisors C and C ′ on X such that C 2 =
C ′2 = −2 and C · h = C ′ · h = 1, where h is the pullback of the class of a line from P2. By
Riemann-Roch, either C or −C is eﬀective. Since C · h > 0, we conclude that C is eﬀective;

18 BRENDAN HASSETT AND ANTHONY V ´ARILLY-ALVARADO

likewise for C ′. The projection L of C or C ′ to P2 is a tritangent line in characteristic zero,
as claimed.
Degree considerations show that L cannot break upon reduction modulo p′. This contra-
dicts the assumption that the curve Cp′ has no tritangent lines. □

Remarks 5.4. Proposition 5.3 is computationally useful because:
(1) Checking the existence of a tritangent line modulo p′ is an easy Groebner basis
calculation; see [EJ08, Algorithm 8].
(2) Given a K3 surface of degree 2 over Q, we can quickly search for small primes p of
good reduction over which the branch curve Cp′ of the double cover Xp′ → P2
Fp′ has
a tritangent line.

Our particular surface X1 reduces modulo 3 to the (smooth) K3 surface

w2 = 2x2
1(x2
0 + 2x0x1 + 2x2
1)
2 + (2x0 + x2)(x5
0 + x4
0x1 + x3
0x1x2 + x2
0x3
1 + x2
0x2
1x2
+ +2x2
0x3
2 + x0x4
1 + 2x0x3
1x2 + x0x2
1x2
2 + x5
1 + 2x4
1x2 + 2x3
1x2
2 + 2x5
2).

From the expression on the right hand side, it is clear that 2x0 + x2 = 0 is a tritangent line to
the branch curve of the double cover. The components of the pullback of this line generate
a rank 2 sublattice of Pic ((X1)3). Let Nn := #X1(F3n); counting points we ﬁnd

N1 N2 N3 N4 N5 N6 N7 N8 N9 N10
7 79 703 6607 60427 532711 4792690 43068511 387466417 3486842479 .

This is enough information to determine the characteristic polynomial f of Frobenius on
H 2((X1)F3, Qℓ); see, for example [vL07] (the sign of the functional equation for f is negative—
a positive sign gives rise to roots of f of absolute value ̸= 3). Setting f3(t) = 3
−22f (3t), we
obtain a factorization into irreducible factors as follows:

f3(t) = 1
3(t − 1)(t + 1)(3t
20 + 3t
19 + 5t
18 + 5t
17 + 6t
16 + 2t
15 + 2t
14 − 3t
13 − 4t
12 − 8t
11

− 6t
10 − 8t
9 − 4t
8 − 3t
7 + 2t
6 + 2t
5 + 6t
4 + 5t
3 + 5t
2 + 3t + 3).

The number of roots of f3(t) that are roots of unity give an upper bound for Pic((X1)F3)
(see, e.g., [vL07, Corollary 2.3]). The roots of the degree 20 factor of f3(t) are not integral,
so they are not roots of unity. We conclude that rk Pic((X1)F3) = 2.
A computation shows that X1 has no line tritangent to the branch curve when we reduce
modulo p′ = 11 (see Remark 5.4(i)). Note that the surface is not smooth at p′ = 5, 7.
Applying Proposition 5.3, we obtain the following result.

Proposition 5.5. The surface X1 has geometric Picard rank 1. □

5.4. Local invariants. In this section we compute the local invariants of the algebra A for
our particular surface X1.

Proposition 5.6. Let p ≤ ∞ be a place of Q. For any P ∈ X1(Qp), we have

invp (A(P )
) =
 {
0, if Qp ̸= R,
1/2, if Qp = R.

FAILURE OF THE HASSE PRINCIPLE ON GENERAL K3 SURFACES 19

Proof. Whenever p ̸= 2 is a ﬁnite prime of good reduction for X1, we have invp (A(P )
) = 0
for all P , by Lemma 4.4.
At every odd prime of bad reduction of X1, the singular locus consists of r < 8 ordinary
double points: for most of these primes p the claim follows because the valuation at p of
the discriminant of X1 is one, by our work in §5.1, so the singular locus consists of a single
ordinary double point. For the remaining primes, a straightforward computer calculation
does the job.
Together with Proposition 4.1 and Lemma 4.2, this implies that invp (A(P )
) is indepen-
dent of P ; it thus suﬃces to evaluate these invariants at a single point P . We use the local
points listed in Table 1 to verify that all the local invariants vanish.
Finally, the quadrics (14) are readily seen to satisfy the hypotheses of Lemmas 4.5 and 4.7,
which establishes the claim for real and 2-adic points of X1, using Corollary 4.6. □

5.5. Proof of Theorem 1.1. The ﬁrst part of the Theorem is just Proposition 3.3. We
specialize now to the case k = Q.
Let A, . . . , F be as in (14), so that X is the surface X1 considered throughout this section.
The cohomology group H 1(Q, Pic(X)
) is trivial, because Pic(X) ∼= Z, with trivial Galois
action, by Proposition 5.5. By (1), we have Br1(X) = Br0(X). Hence, the class A ∈ Br(X)
is transcendental, if it is not constant.
We established in §5.2 that X(A) ̸= ∅. On the other hand, X(A)
A = ∅, by Proposition 5.6.
This shows that A is nonconstant, and that X(A)
Br = ∅. □

6. Computations

In the interest of transparency, we brieﬂy outline the computations that led to the ex-
ample witnessing the second part of Theorem 1.1. The basic idea is to construct “random”
K3 surfaces of the form (2), and perform a series of tests that guarantee the statement of
Theorem 1.1 holds. Any surface left over after Step 7 below is a witness to this theorem.

Step 1: Seed polynomials. Generate random homogeneous quadratic polynomials

A, B, C, D, E, and F ∈ Z[x0, x1, x2],

with coeﬃcients in a suitable range, subject to the constraints imposed by the hypotheses
of Lemma 4.7. We also require that the signs of x2
0, x2
1 and x2
2 are positive for B, C and E,
and negative for A, D and F , to improve the chances that the hypotheses of Lemma 4.5 are
satisﬁed. If these hypotheses are not satisﬁed, then start over.

Step 2: Smoothness. Compute f := − 1
2 det(M ), where M is the matrix in (8). This is
an equation for the curve C1. Use the Jacobian criterion to check smoothness of C1 over Q
and F3 (the latter will be needed to certify that the K3 surface X1 has Picard rank 1). If
either condition is not satisﬁed, then start over.

Step 3: Tritangent lines. Here we have the hypotheses of Proposition 5.3 in mind. Over
F3, use [EJ08, Algorithm 8] to test for the existence of a tritangent line to C1. Let

S := {p : 5 ≤ p ≤ 100 a prime of good reduction for C1}.

20 BRENDAN HASSETT AND ANTHONY V ´ARILLY-ALVARADO

Find p ∈ S, such that C1 over Fp has no tritangent line. If either test fails, then start over.

Step 4: Local points. For primes p ≤ 22 and p = ∞, test for Qp-points of X1/Q : w2 = f
by plugging in integers with small absolute value (typically 1 or 2) for x0, x1 and x2, and
determining whether f is a p-adic square. If this test fails, then it is plausible that X1 has
no local points (false negatives are certainly possible); start over.

Step 5: Point Counting. Use [EJ08, Algorithm 15] to determine X1(F3n) for n = 1, . . . , 10.
This algorithm counts Galois orbits of points, saving a factor of n when counting F3n-points.
Use [EJ08, Algorithms 21 and 23] to determine an upper bound ρup for the geometric Picard
number of the surface X1 over F3. If ρup > 2, then start over. Otherwise, Proposition 5.3
guarantees that X1 has geometric Picard number 1, by our work in Step 3.

Step 6: Primes of bad reduction. Proceeding as in the beginning of §5.1, compute the
integer m whose prime factors give the places of bad reduction of C1 (and hence those of
X1). Compute an equation for C2, as well as the analogous integer n giving its primes of
bad reduction. Typically, m and n will be very large. Proceed as in §5.1 to factorize them.
If the factorization is not feasible (e.g., the integer gcd(m′, n′) as in §5.1 not is prime), then
start over.

Step 7: Computations at places of bad reduction. At odd places of bad reduction,
check for local points, as in Step 4. Determine the (geometric) singular locus. If at any
prime in question the locus does not consist of r < 8 ordinary double points, then start over.
Use to the local points found to compute the (constant) value the invariants of A takes at
these places. If there is no Brauer-Manin obstruction, then start over.

References

[AM93] A. O. L. Atkin and F. Morain. Elliptic curves and primality proving. Math. Comp., 61(203):29–
68, 1993.
[BBFL07] M. J. Bright, N. Bruin, E. V. Flynn, and A. Logan. The Brauer-Manin obstruction and Sh[2].
LMS J. Comput. Math., 10:354–377 (electronic), 2007.
[BCP97] Wieb Bosma, John Cannon, and Catherine Playoust. The Magma algebra system. I. The user
language. J. Symbolic Comput., 24(3-4):235–265, 1997. Computational algebra and number the-
ory (London, 1993).
[Bea77] Arnaud Beauville. Vari´et´es de Prym et jacobiennes interm´ediaires. Ann. Sci. ´Ecole Norm. Sup.
(4), 10(3):309–391, 1977.
[Bri06] Martin Bright. Brauer groups of diagonal quartic surfaces. J. Symbolic Comput., 41(5):544–558,
2006.
[BSD75] B. J. Birch and H. P. F. Swinnerton-Dyer. The Hasse problem for rational surfaces. J. Reine
Angew. Math., 274/275:164–174, 1975. Collection of articles dedicated to Helmut Hasse on his
seventy-ﬁfth birthday, III.
[Cor07] Patrick Corn. The Brauer-Manin obstruction on del Pezzo surfaces of degree 2. Proc. Lond.
Math. Soc. (3), 95(3):735–777, 2007.
[Cor10] Patrick Corn. Tate-Shafarevich groups and K3 surfaces. Math. Comp., 79(269):563–581, 2010.
[CTCS80] Jean-Louis Colliot-Th´el`ene, Daniel Coray, and Jean-Jacques Sansuc. Descente et principe de
Hasse pour certaines vari´et´es rationnelles. J. Reine Angew. Math., 320:150–191, 1980.

FAILURE OF THE HASSE PRINCIPLE ON GENERAL K3 SURFACES 21

[CTKS87] Jean-Louis Colliot-Th´el`ene, Dimitri Kanevsky, and Jean-Jacques Sansuc. Arithm´etique des
surfaces cubiques diagonales. In Diophantine approximation and transcendence theory (Bonn,
1985), volume 1290 of Lecture Notes in Math., pages 1–108. Springer, Berlin, 1987.
[CTS] Jean-Louis Colliot-Th´el`ene and Alexei N. Skorobogatov. Sur le groupe de brauer transcendant.
arXiv:1106.6312.
[CTS13] Jean-Louis Colliot-Th´el`ene and Alexei N. Skorobogatov. Good reduction of the Brauer–Manin
obstruction. Trans. Amer. Math. Soc., 365(2):579–590, 2013.
[CTSSD87] Jean-Louis Colliot-Th´el`ene, Jean-Jacques Sansuc, and Peter Swinnerton-Dyer. Intersections of
two quadrics and Chˆatelet surfaces. II. J. Reine Angew. Math., 374:72–168, 1987.
[Cun07] Stephen Cunnane. Rational points on Enriques surfaces, 2007. Ph. D. thesis, Imperial College
London.
[Eis95] David Eisenbud. Commutative algebra, volume 150 of Graduate Texts in Mathematics. Springer-
Verlag, New York, 1995.
[EJ08] Andreas-Stephan Elsenhans and J¨org Jahnel. K3 surfaces of Picard rank one and degree two.
In Algorithmic number theory, volume 5011 of Lecture Notes in Comput. Sci., pages 212–225.
Springer, Berlin, 2008.
[EJ10a] Andreas-Stephan Elsenhans and J¨org Jahnel. Cubic surfaces with a Galois invariant double-six.
Cent. Eur. J. Math., 8(4):646–661, 2010.
[EJ10b] Andreas-Stephan Elsenhans and J¨org Jahnel. On the Brauer-Manin obstruction for cubic sur-
faces. J. Comb. Number Theory, 2(2):107–128, 2010.
[EJ11a] Andreas-Stephan Elsenhans and J¨org Jahnel. Cubic surfaces with a Galois invariant pair of
Steiner trihedra. Int. J. Number Theory, 7(4):947–970, 2011.
[EJ11b] Andreas-Stephan Elsenhans and J¨org Jahnel. On the computation of the Picard group for K3
surfaces. Math. Proc. Cambridge Philos. Soc., 151(2):263–270, 2011.
[EJ11c] Andreas-Stephan Elsenhans and J¨org Jahnel. The Picard group of a K3 surface and its reduction
modulo p. Algebra Number Theory, 5(8):1027–1040, 2011.
[Fuj02] Kazuhiro Fujiwara. A proof of the absolute purity conjecture (after Gabber). In Algebraic ge-
ometry 2000, Azumino (Hotaka), volume 36 of Adv. Stud. Pure Math., pages 153–183. Math.
Soc. Japan, Tokyo, 2002.
[Ful98] William Fulton. Intersection theory, volume 2 of Ergebnisse der Mathematik und ihrer Gren-
zgebiete. 3. Folge. A Series of Modern Surveys in Mathematics. Springer-Verlag, Berlin, second
edition, 1998.
[GS] Daniel R. Grayson and Michael E. Stillman. Macaulay2, a software system for research in alge-
braic geometry. Available at http://www.math.uiuc.edu/Macaulay2/.
[GS06] Philippe Gille and Tam´as Szamuely. Central simple algebras and Galois cohomology, volume 101
of Cambridge Studies in Advanced Mathematics. Cambridge University Press, Cambridge, 2006.
[Har96] David Harari. Obstructions de Manin transcendantes. In Number theory (Paris, 1993–1994),
volume 235 of London Math. Soc. Lecture Note Ser., pages 75–87. Cambridge Univ. Press,
Cambridge, 1996.
[HS05] David Harari and Alexei Skorobogatov. Non-abelian descent and the arithmetic of Enriques
surfaces. Int. Math. Res. Not., 52:3203–3228, 2005.
[HVAV11] Brendan Hassett, Anthony V´arilly-Alvarado, and Patrick Varilly. Transcendental obstructions
to weak approximation on general K3 surfaces. Adv. Math., 228(3):1377–1404, 2011.
[Ier10] Evis Ieronymou. Diagonal quartic surfaces and transcendental elements of the Brauer groups.
J. Inst. Math. Jussieu, 9(4):769–798, 2010.
[ISZ11] Evis Ieronymou, Alexei N. Skorobogatov, and Yuri G. Zarhin. On the brauer group of diagonal
quartic surfaces. J. London Math. Soc. (2), 83(3):659–672, 2011.
[Kat86] Kazuya Kato. A Hasse principle for two-dimensional global ﬁelds. J. Reine Angew. Math.,
366:142–183, 1986. With an appendix by Jean-Louis Colliot-Th´el`ene.
[Klo07] Remke Kloosterman. Elliptic K3 surfaces with geometric Mordell-Weil rank 15. Canad. Math.
Bull., 50(2):215–226, 2007.
[KT04] Andrew Kresch and Yuri Tschinkel. On the arithmetic of del Pezzo surfaces of degree 2. Proc.
London Math. Soc. (3), 89(3):545–569, 2004.

22 BRENDAN HASSETT AND ANTHONY V ´ARILLY-ALVARADO

[KT08] Andrew Kresch and Yuri Tschinkel. Eﬀectivity of Brauer-Manin obstructions. Adv. Math.,
218(1):1–27, 2008.
[Lip69] Joseph Lipman. Rational singularities, with applications to algebraic surfaces and unique fac-
torization. Inst. Hautes ´Etudes Sci. Publ. Math., (36):195–279, 1969.
[Log08] Adam Logan. The Brauer-Manin obstruction on del Pezzo surfaces of degree 2 branched along a
plane section of a Kummer surface. Math. Proc. Cambridge Philos. Soc., 144(3):603–622, 2008.
[LP81] Eduard Looijenga and Chris Peters. Torelli theorems for K¨ahler K3 surfaces. Compositio Math.,
42(2):145–186, 1980/81.
[LvL09] Adam Logan and Ronald van Luijk. Nontrivial elements of Sha explained through K3 surfaces.
Math. Comp., 78(265):441–483, 2009.
[Man71] Y. I. Manin. Le groupe de Brauer-Grothendieck en g´eom´etrie diophantienne. In Actes du Congr`es
International des Math´ematiciens (Nice, 1970), Tome 1, pages 401–411. Gauthier-Villars, Paris,
1971.
[Man74] Yu. I. Manin. Cubic forms: algebra, geometry, arithmetic. North-Holland Publishing Co., Ams-
terdam, 1974. Translated from Russian by M. Hazewinkel, North-Holland Mathematical Library,
Vol. 4.
[Mil80] James S. Milne. ´Etale cohomology, volume 33 of Princeton Mathematical Series. Princeton Uni-
versity Press, Princeton, N.J., 1980.
[MP09] Davesh Maulik and Bjorn Poonen. N´eron-Severi groups under specialization, 2009.
arXiv:0907.4781.
[Muk84] Shigeru Mukai. Symplectic structure of the moduli space of sheaves on an abelian or K3 surface.
Invent. Math., 77(1):101–116, 1984.
[Nik79] V. V. Nikulin. Integer symmetric bilinear forms and some of their geometric applications. Izv.
Akad. Nauk SSSR Ser. Mat., 43(1):111–177, 238, 1979.
[Pre10] Thomas Preu. Transcendental Brauer-Manin obstruction for a diagonal quartic surface, 2010.
Ph. D. thesis, Universit¨at Z¨urich.
[S
+09] W. A. Stein et al. Sage Mathematics Software (Version 4.2.1). The Sage Development Team,
2009. http://www.sagemath.org.
[SD93] Peter Swinnerton-Dyer. The Brauer group of cubic surfaces. Math. Proc. Cambridge Philos.
Soc., 113(3):449–460, 1993.
[SD99] Peter Swinnerton-Dyer. Brauer-Manin obstructions on some Del Pezzo surfaces. Math. Proc.
Cambridge Philos. Soc., 125(2):193–198, 1999.
[Ser73] J.-P. Serre. A course in arithmetic. Springer-Verlag, New York, 1973. Translated from the French,
Graduate Texts in Mathematics, No. 7.
[SGA03] Revˆetements ´etales et groupe fondamental (SGA 1). Documents Math´ematiques (Paris) [Math-
ematical Documents (Paris)], 3. Soci´et´e Math´ematique de France, Paris, 2003. S´eminaire de
g´eom´etrie alg´ebrique du Bois Marie 1960–61. [Algebraic Geometry Seminar of Bois Marie 1960-
61], Directed by A. Grothendieck, With two papers by M. Raynaud, Updated and annotated
reprint of the 1971 original [Lecture Notes in Math., 224, Springer, Berlin; MR0354651 (50
#7129)].
[Sko96] Alexei N. Skorobogatov. Descent on ﬁbrations over the projective line. Amer. J. Math.,
118(5):905–923, 1996.
[Sko01] Alexei Skorobogatov. Torsors and rational points, volume 144 of Cambridge Tracts in Mathe-
matics. Cambridge University Press, Cambridge, 2001.
[SSD05] Alexei Skorobogatov and Peter Swinnerton-Dyer. 2-descent on elliptic curves and rational points
on certain Kummer surfaces. Adv. Math., 198(2):448–483, 2005.
[SZ08] Alexei N. Skorobogatov and Yuri G. Zarhin. A ﬁniteness theorem for the Brauer group of abelian
varieties and K3 surfaces. J. Algebraic Geom., 17(3):481–502, 2008.
[SZ12] Alexei N. Skorobogatov and Yuri G. Zarhin. The Brauer group of Kummer surfaces and torsion
of elliptic curves. J. Reine Angew. Math., 666:115–140, 2012.
[VA08] Anthony V´arilly-Alvarado. Weak approximation on del Pezzo surfaces of degree 1. Adv. Math.,
219(6):2123–2145, 2008.

FAILURE OF THE HASSE PRINCIPLE ON GENERAL K3 SURFACES 23

[vG05] Bert van Geemen. Some remarks on Brauer groups of K3 surfaces. Adv. Math., 197(1):222–247,
2005.
[vGS07] Bert van Geemen and Alessandra Sarti. Nikulin involutions on K3 surfaces. Math. Z.,
255(4):731–753, 2007.
[vL07] Ronald van Luijk. K3 surfaces with Picard number one and inﬁnitely many rational points.
Algebra Number Theory, 1(1):1–15, 2007.
[Voi86] Claire Voisin. Th´eor`eme de Torelli pour les cubiques de P5. Invent. Math., 86(3):577–601, 1986.
[Wit] Olivier Wittenberg. Personal letter, April 27th, 2010.
[Wit04] Olivier Wittenberg. Transcendental Brauer-Manin obstruction on a pencil of elliptic curves. In
Arithmetic of higher-dimensional algebraic varieties (Palo Alto, CA, 2002), volume 226 of Progr.
Math., pages 259–267. Birkh¨auser Boston, Boston, MA, 2004.

Department of Mathematics, Rice University, Houston, TX 77005, USA
E-mail address: hassett@rice.edu
URL: http://www.math.rice.edu/~hassett

Department of Mathematics, Rice University, Houston, TX 77005, USA
E-mail address: varilly@rice.edu
URL: http://www.math.rice.edu/~av15
