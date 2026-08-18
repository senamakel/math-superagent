<!-- source: https://arxiv.org/pdf/2309.11974 | converted from PDF -->

arXiv:2309.11974v1  [math.NT]  21 Sep 2023
Real quadratic singular moduli and
p-adic families of modular forms

Paulina Fust, Judith Ludwig, Alice Pozzi, Mafalda Santos and Hanneke Wiersema

Abstract

The classical theory of elliptic curves with complex multiplication is a fundamental tool
for studying the arithmetic of abelian extensions of imaginary quadratic ﬁelds. While no
direct analogue is available for real quadratic ﬁelds, a (conjectural) theory of “real multi-
plication” was recently proposed by Darmon and Vonk, relying on p-adic methods, and in
particular on the new notion of rigid meromorphic cocycles. A rigid meromorphic cocy-
cle is a class in the ﬁrst cohomology of the group SL2(Z[1/p]) acting on the non-zero rigid
meromorphic functions on the Drinfeld p-adic upper half plane by Möbius transformation.
The values of rigid meromorphic cocycles at real quadratic points can be thought of as
analogues of singular moduli for real quadratic ﬁelds.
In this survey article, we will discuss aspects of the theory of complex multiplication
and compare them with conjectural analogues for real quadratic ﬁelds, with an emphasis
on the role played by families of modular forms in both settings.

1 Introduction

The goal of this article is to present recent developments in the theory of singular moduli for real
quadratic ﬁelds introduced in [DV21] in a parallel perspective to the classical theory of complex
multiplication. The theory of elliptic curves with complex multiplication has yielded some
spectacular arithmetic applications. Kronecker tackled the problem of constructing abelian
extensions of imaginary quadratic ﬁelds, known as the Kronecker Jugendtraum, via singular
moduli, i.e., values of modular functions at imaginary quadratic points of the complex upper
half plane H∞. While class ﬁeld theory provides a description of the Galois groups classifying
abelian extensions of arbitrary number ﬁelds, ﬁnding an explicit recipe for their generators is
more elusive beyond the CM setting.
Another problem for which in current approaches CM theory is an essential tool is the Birch
and Swinnerton-Dyer Conjecture. Given an elliptic curve E over a number ﬁeld K, the Birch
and Swinnerton-Dyer Conjecture (BSD) predicts an equality between the rank of its group of
K-rational points and the order of vanishing of its L-function L(E/K, s) at s = 1. The only known
approach to systematically producing global points is via the theory of Heegner points. The
works of Gross–Zagier [GZ85] and Kolyvagin [Kol89] settle many instances of BSD in rank 1
by exploiting properties of this supply of global points.
The construction of singular moduli and Heegner points share some common features.
They both arise from an appropriate evaluation process at CM points on the complex up-
per half plane. The corresponding values are deﬁned over abelian extensions of imaginary

1

quadratic ﬁelds K. We will refer to this type of construction as Heegner constructions. It is nat-
ural to ask if a similar approach can be implemented to construct collections of objects lying
in abelian extensions of other number ﬁelds.
Let K be a real quadratic ﬁeld. From a naive perspective, the idea of evaluating modular
functions at real quadratic points (or RM, by analogy with CM points) of H∞ already fails
because RM points lie on the real line. This suggests that an appropriate analogue of CM
theory should be sought by replacing the role played by the archimedean place with a ﬁnite
place that does not split in K. This is the point of view proposed by Darmon and Vonk in their
theory of singular moduli for real quadratic ﬁelds.
For a ﬁnite prime p, the Drinfeld p-adic upper half plane is the rigid analytic space Hp
whose Cp-valued points are P1(Cp) \ P1(Qp). It contains RM points over real quadratic ﬁelds K
in which p is ramiﬁed or inert. In analogy with CM theory, it would be natural to attempt to
deﬁne singular moduli as values of suitable modular functions at RM points in Hp, for some
action of a modular group Γ ⊂ GL2(Qp). Typically, one would expect this group to arise as the
elements of norm one in a Z [1/p]-order of a quaternion algebra B/Q which splits at p. On
the one hand, if the quaternion algebra is deﬁnite, the quotient Γ\Hp admits the structure of a
rigid analytic space. However, in that setting, B does not contain any real quadratic subalgebra.
Therefore one would not expect such quotients to appear in the framework of RM theory. On
the other hand, if B is indeﬁnite, it contains real quadratic subalgebras but the action of Γ
on Hp is not discrete, so that there are no suitable modular functions. Darmon and Vonk ﬁx
the indeﬁnite quaternion algebra B = M2(Qp), so that Γ = SL2(Z[1/p]) is the Ihara group, and
they deﬁne rigid meromorphic cocycles as classes in H 1(Γ, M×), where M is the ring of rigid
meromorphic functions on Hp. They show that these classes (or more precisely, the quasi-
parabolic classes, see §3.3) can be meaningfully evaluated at RM points. They then conjecture
that their RM values lie in composita of abelian extensions of real quadratic ﬁelds, making
them suitable candidates for an analogue of singular moduli in the real quadratic setting. The
theory of real quadratic singular moduli ﬁts into a program launched by Darmon in [Dar01]
attempting to deﬁne conjectural analogues of Heegner constructions for real quadratic ﬁelds
via p-adic methods. Most notably, the construction of a putative analogue of Heegner points,
known as Stark–Heegner points, has since seen many generalisations. While the theoretical
evidence on the rationality of these points is scarce, the computational results are extensive.
In the last 50 years, new aspects of the theory of complex multiplication have emerged,
in which automorphic methods are used substantially. An important theme is the study of
modular generating series constructed out of CM cycles on Shimura curves, pioneered by the
work of Gross and Zagier on the factorisation of diﬀerences of singular moduli [GZ85]. The
crucial idea of relating generating series to derivatives of real analytic families of Eisenstein
series culminated in the proof of many cases of the Birch and Swinnerton–Dyer Conjecture for
a modular elliptic curve in analytic rank 1 in [GZ86] (see Thm. 4.2.1). Although the algebraic-
ity properties of the analogues of the Heegner constructions in the real quadratic setting are
conjectural, one can package RM cycles on Hp into modular generating series. It is natural
to speculate that these generating series would be related to derivatives of p-adic families of
modular forms. This perspective has been explored by Darmon, Pozzi and Vonk in [DPV21]
and [DPV23].
In the archimedean setting, only real analytic Eisenstein series admit variations in families.
By contrast, the work of Hida, and its generalisation via the theory of eigenvarieties intro-

2

duced by Coleman–Mazur, show that p-adic families of automorphic forms abound. A useful
feature of the p-adic theory is that cusp forms vary in p-adic families. In addition, their cor-
responding Galois representations can be interpolated. This aspect has been leveraged into
breakthroughs in Iwasawa theory and the theory of p-adic L-functions, for example the proof
of the Iwasawa Main Conjecture over totally real ﬁelds by Mazur–Wiles, or the proof of the
Mazur–Tate–Teitelbaum Conjecture by Greenberg–Stevens.
In the context of modular generating series for RM values, the additional ﬂexibility of the
p-adic setting has been used by Darmon–Pozzi–Vonk to prove some instances of the expected
algebraicity results for the analogues of elliptic units for real quadratic ﬁelds (see Theorem
5.3.1). Their approach is somewhat indirect. On the one hand, derivatives of certain p-adic
families of modular forms are used to produce modular generating series for RM values. On
the other hand, the derivatives of cuspidal families are related to global cohomology classes
informing the arithmetic of abelian extensions of real quadratic ﬁelds. This strategy towards
the algebraicity of Heegner constructions in the RM setting suggests that the richer theory of
p-adic automorphic forms can sometimes make up for the lack of an a priori global description
of the corresponding RM objects.

Overview of the paper. This article is structured as follows. Section 2 contains a review
of some aspects of the classical theory of complex multiplication, with an emphasis on singu-
lar moduli, elliptic units and Heegner points. Section 3 focuses on the construction of their
conjectural analogues for real quadratic ﬁelds. For the reader’s convenience, we include some
background on the Drinfeld p-adic upper half plane as a rigid space and introduce the theory of
rigid meromorphic cocycles. Sections 4 and 5 are devoted to the interplay between derivatives
of families of modular forms and singular moduli, in the archimedean and non-archimedean
setting respectively. In particular, Section 4 treats Gross and Zagier’s work on the factorisation
of singular moduli and the BSD Conjecture in analytic rank 1 [GZ85] and [GZ86], while Sec-
tion 5 focuses on the articles [DPV21] and [DPV23]. Sections 2 and 3 are meant to be mostly
self-contained, while Sections 4 and 5 aim to be an overview of various arithmetic applications
to Heegner constructions in a uniﬁed framework.

Acknowledgements. We would like to thank the organisers of the WIN-Europe 4 confer-
ence for inviting us to contribute to these proceedings. We would like to thank Henri Darmon
and Jan Vonk for enlightening explanations of their work. We would also like to thank Sandra
Rozensztajn, Ana Caraiani and Catherine Hsu for helpful conversations during the prepara-
tion of this manuscript. We would like to thank Oğuz Gezmiş and the anonymous referees for
many helpful comments and suggestions.
P.F. was funded by the DFG Graduiertenkolleg 2553. J.L. acknowledges support from the
Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) through TRR 326 Ge-
ometry and Arithmetic of Uniformized Structures, project number 444845124. A.P. was funded
by the Leverhulme Trust (via the Leverhulme Prize of Ana Caraiani). M.S. was funded by
the Engineering and Physical Sciences Research Council [EP/L015234/1], the EPSRC Centre
for Doctoral Training in Geometry and Number Theory (The London School of Geometry and
Number Theory), Imperial College London, and by the Max-Planck-Institut für Mathematik.
H.W. acknowledges support from the Herchel Smith Postdoctoral Fellowship Fund, and the
Engineering and Physical Sciences Research Council (EPSRC) grant EP/W001683/1.

3

2 Heegner Constructions for imaginary quadratic ﬁelds

In this section, we will give a brief overview of results in the classical theory of elliptic curves
with complex multiplication, and its applications to the construction of arithmetic objects over
abelian extensions of imaginary quadratic ﬁelds. At the heart of these results lies the fact that
modular curves, quotients of the complex upper half plane by congruence subgroups, admit a
moduli interpretation which endows them with a rational structure. The moduli interpretation
of CM points can be used to determine their images under ﬁeld automorphisms, which allows
one to deduce that they deﬁne global points on modular curves.
We will begin by recalling some facts about the moduli interpretation of CM points on modular
curves and the Main Theorem of Complex Multiplication. We will then discuss in more detail
the Heegner constructions of singular moduli, elliptic units and Heegner points.

2.1 Modular curves and CM points

2.1.1 Elliptic curves with complex multiplication

Let E be a complex elliptic curve, which we view as a Riemann surface. It admits a uniformisa-
tion E(C) ≃ C/Λ, where Λ ⊂ C is its period lattice, well-deﬁned up to homothety; by rescaling,
the latter can be chosen of the form Λ = τZ + Z, for τ ∈ C with positive imaginary part. En-
domorphisms of E are given by endomorphisms of its universal covering C that preserve the
lattice Λ. Denote by RE the set of endomorphisms of E. For a generic τ in the upper half
plane, all endomorphisms of E are given by multiplication by an integer. Otherwise, there
exists α ∈ C \ Z, and integers a, b, c, d satisfying

cτ + d = α, aτ + b = ατ.

This forces K = Q(τ) to be an imaginary quadratic ﬁeld and α to be an algebraic integer in K.
As a result RE is isomorphic to an order O in K, for which the lattice Λ is a proper fractional
ideal. In this case we say that E has complex multiplication by O.

2.1.2 The Main Theorem of Complex Multiplication

Let H∞ be the Poincaré complex upper half plane, on which the group GL
+
2 (R) of invertible
real matrices with positive determinant acts by Möbius transformation.
For a positive integer N , consider the order

M0(N ) = {(
a b
c d
) ∈ M2(Z) : N | c}

in the ring of 2 × 2-matrices with integer coeﬃcients, and let Γ0(N ) be the group of matrices
of determinant 1 in M0(N ). The assigment τ ↦→ (τZ + Z, τZ + 1/N Z) identiﬁes the quotient
Γ0(N )\H∞ with the moduli space of pairs of lattices (Λ, Λ′) with

Λ ⊂ Λ′ such that Λ′/Λ ≃ Z/N Z,

deﬁned up to homothety.
 4

The moduli problem parametrising isomorphism classes of pairs of elliptic curves (E, E′)
with a cyclic degree N -isogeny E → E′ admits a coarse moduli space Y0(N ) over Q which we
refer to as the (open) modular curve of the level Γ0(N ). We let X0(N ) be its compactiﬁcation,
obtained by adding cusps.
There is a bijection

ιN : Γ0(N )\H∞ → Y0(N )(C), τ ↦→ (C/(τZ + Z), C/(τZ + 1/N Z))

which provides a uniformisation of Y0(N )(C) by the complex upper half plane.

We say that τ ∈ H∞ is imaginary quadratic of discriminant D if [τ, 1] is a solution to a
quadratic equation of the form AX2 + BXY + CY 2 = 0 for some coprime integers A, B, C and
D = B2 − 4AC < 0. For τ ∈ H∞ and N ∈ Z≥1 let

O(N )
τ := {(
a b
c d
) ∈ M0(N ) : aτ + b = cτ2 + dτ} .

The image of the inclusion O(N )
τ ֒→ C given by ( a b
c d ) ↦→ cτ + d is either isomorphic to Z or to an
order in the imaginary quadratic ﬁeld K = Q(τ). In the latter case, we say that τ is a CM point
on Y0(N ) and denote by [τ] its Γ0(N )-orbit, when the level Γ0(N ) is understood. For an order
O in an imaginary quadratic ﬁeld K of discriminant prime to N , we denote by HO
∞ the set of
points τ ∈ H∞ with O(N )
τ = O(1)
τ ∩ O(1)
N τ ≃ O.

Such points are in bijection with the pairs of elliptic curves (C/Λ, C/Λ′) whose correspond-
ing lattices (Λ, Λ′) are contained in K (up to homothety) and for which the set

{α ∈ K : αΛ ⊂ Λ, αΛ′ ⊂ Λ′} (1)

is equal to O. The set HO
∞ is preserved by the action of Γ0(N ) and the quotient Γ0(N )\HO
∞ is
ﬁnite. We let Γ0(N )\HCM
∞ be the union of Γ0(N )-orbits of points with complex multiplication by
O for some imaginary quadratic order O.

Denote by Cl(O) the class group of O. Given a proper fractional ideal a in O and a pair of
lattices (Λ, Λ′), condition (1) is stable under multiplication by a. As a result

a ∗ (C/Λ, C/Λ′) := (C/(a ∗ Λ), C/(a ∗ Λ′))

deﬁnes an action of the class group Cl(O) on Γ0(N )\HO
∞. For [τ] ∈ Γ0(N )\HO
∞, we write a ∗ τ for
a ∗ (C/(Z + τZ), C/(1/N Z + τZ)) by abuse of notation.

The Main Theorem of Complex Multiplication ensures that CM points on modular curves
are deﬁned over suitable ring class ﬁelds, and describes the Galois action on CM points. More
precisely, let O be an order in an imaginary quadratic ﬁeld K. The Artin reciprocity map yields
an isomorphism rec : Cl(O) → Gal(H/K)

where H is the ring class ﬁeld of O. The Main Theorem of Complex Multiplication can be
stated as follows.
 5

Theorem 2.1.1. Let O be an order of discriminant D in an imaginary quadratic ﬁeld K, and let H
be its corresponding ring class ﬁeld. Let N be a positive integer coprime to D.
For every point [τ] ∈ Γ0(N )\HO
∞, we have:

(i) ιN ([τ]) ∈ Y0(N )(H),

(ii) (Shimura reciprocity law): every a ∈ Cl(O) satisﬁes ιN (a ∗ [τ]) = rec(a)−1ιN ([τ]).

For a reference see [Cox89, Cor. 11.37]. In §2.2 we will explain how Theorem 2.1.1 can be
exploited towards the construction of global units and global points on elliptic curves over ring
class ﬁelds of imaginary quadratic ﬁelds.

2.2 Heegner Constructions

Theorem 2.1.1 endows the modular curve Y0(N ) with a systematic supply of global points.
Given a group scheme X/Q together with a Q-rational morphism Y0(N ) → X, one obtains a
collection of global points on X, satisfying similar properties to those of CM points on modular
curves. We refer to constructions of this ﬂavour as Heegner constructions.
In the following examples, Heegner constructions are obtained from an a priori holomor-
phic map Φ : Γ0(N )\H∞ → X(C)

of Riemann surfaces that is shown to arise from a Q-rational morphism of curves (an important
example being the modular parametrisation of an elliptic curve). As a consequence of Theorem
2.1.1, the following properties are satisﬁed:

(i) If [τ] ∈ Γ0(N )\HO
∞ then Φ([τ]) ∈ X(H);

(ii) The action of the class group Cl(O) is compatible with the Galois action on X(H) under a
Shimura reciprocity law.

Below we will give three examples of Heegner constructions. The following table sum-
marises how these examples ﬁt into this perspective.

X Φ

Singular Moduli aﬃne line A1/Q j -invariant
Elliptic Units multiplicative group Gm/Q modular unit
Heegner Points elliptic curve E/Q modular parametrisation

The setting of singular moduli is obtained by specialising Theorem 2.1.1 to the case of level
Γ0(1). Elliptic units are constructed from the evaluation of a modular unit at CM points.
Roughly speaking, Heegner points are obtained by projecting CM cycles on the Jacobian of
the modular curve onto its f -isotypic component for a newform f of weight 2.
Remark 1. The constructions presented in §3 will mimic the ones above by replacing H∞ with
the Drinfeld p-adic upper half plane Hp and imaginary quadratic with real quadratic points.
The Heegner constructions in the RM setting are obtained via techniques of rigid analytic ge-
ometry and are expected to satisfy similar properties to those of classical Heegner construc-
tions. However, there are signiﬁcant diﬀerences. The analogues of the map Φ described above
will only be deﬁned at real multiplication points. More crucially, the RM constructions are
purely local, and no analogues of the modular curve are available in that setting.
We will now proceed to describe the inputs of these constructions in some detail.

6

2.2.1 Singular moduli

Given a lattice Λ in C, the theory of elliptic curves over the complex numbers yields an identi-
ﬁcation between the complex torus C/Λ and the points of an elliptic curve with equation

Y 2 = 4X3 − g2(Λ)X − g3(Λ)

where the constants are deﬁned as

g2(Λ) = 60 ∑

ω∈Λ−{0}
 1
ω4 , g3(Λ) = 140 ∑

ω∈Λ−{0}
 1
ω6 .

For i = 2, 3, and τ in the upper half plane, the assignment gi (τ) := gi(Z + τZ) deﬁnes a modular
form of weight 2i and level SL2(Z). The complex functions

∆ := g3
2 − 27g2
3 , j := 1728 g3
2
∆
are the modular discriminant and the modular j -function respectively. The former is a nowhere
vanishing cusp form of weight 12. The latter is a holomorphic SL2(Z)-invariant function on
H∞. The map j : SL2(Z)\H∞ → A1(C) (2)

extends to an isomorphism of Riemann surfaces between the compactiﬁcations of SL2(Z)\H∞
and A1(C), respectively. The crucial property of the j -invariant is that it characterises elliptic
curves up to isomorphism over an algebraically closed ﬁeld, and captures the minimal ﬁeld of
deﬁnition of an elliptic curve. As a result, the coarse moduli space for elliptic curves Y0(1) can
be identiﬁed with the aﬃne line via (2). For N ≥ 1, the image of the morphism

Γ0(N )\H∞ → A2(C) , τ ↦→ (j (τ), j (N τ))

is cut out by a single equation given by ϕN ∈ Q[X, Y ], referred to as the N -th modular polyno-
mial ([DS05, Section 7.5]). The corresponding plane curve is birational to the modular curve
X0(N ).

Deﬁnition 1. Singular moduli are values of the j -function at points in SL2(Z)\HCM
∞ .

For N = 1, Theorem 2.1.1 directly translates into properties of singular moduli. The gen-
eral level case easily follows from the level 1 setting, together with properties of the modular
polynomials. An important application is the following corollary.

Corollary 1. Let D < 0 be a fundamental discriminant, let τ ∈ H∞ be a point of discriminant D and
denote K = Q(τ). Then the Hilbert class ﬁeld of K is K(j (τ)).

This result (and its analogues for non-fundamental discriminants) can be interpreted as
providing explicit generators for certain abelian extensions of imaginary quadratic ﬁelds. More
generally, Hilbert’s Twelfth Problem consists in ﬁnding explicit formulae for generators of all
abelian extensions of number ﬁelds. The motivating example is the Kronecker–Weber The-
orem. It states that all abelian extensions of Q can be obtained by adjoining roots of unity,
which can be viewed as values of the function z ↦→ e2πiz at rational arguments. However, for
an imaginary quadratic ﬁeld K, singular moduli do not suﬃce to generate the maximal abelian
extension, as one would also need to consider values of coordinates of torsion points of elliptic
curves with CM by orders in K (see [Sil94, Chp. II, Cor. 5.7]).

7

2.2.2 Elliptic units

Singular moduli give generators of certain abelian extensions of imaginary quadratic ﬁelds.
For arithmetic applications, it can be useful to construct generators with controlled integrality
properties, by replacing the j -function with suitable units on modular curves of higher level.
A modular unit u is a nowhere vanishing function on the open modular curve Y0(N ) extend-
ing meromorphically to the cusps. Examples of modular units can be constructed as products
of pullbacks of the modular discriminant via projection maps from Y0(N ) to the modular curve
of level 1. For a ﬁxed level N , let ΣN be the set of divisors of N and consider a degree zero
formal linear combination α = ∑d∈ΣN md[d]. Then the holomorphic function

uα(z) := ∏

d ∆(dz)md

is Γ0(N )-invariant because α has degree 0 and nowhere vanishing because ∆ is. The modu-
lar unit uα can be viewed as a morphism from the open modular curve of level Γ0(N ) to the
multiplicative group.

Deﬁnition 2. Given a divisor α as above, elliptic units are values of uα at points in Γ0(N )\HCM
∞ .

Theorem 2.1.1 implies that elliptic units are deﬁned over ring class ﬁelds of imaginary
quadratic ﬁelds. However, a careful study of the integrality of modular units (cfr. [KL81, Chp.
1, Lemma 1.1]) yields the following result.

Theorem 2.2.1. Let O be an order in an imaginary quadratic ﬁeld K, of discriminant prime to N .
Let uα be a modular unit of level Γ0(N ) and let τ ∈ Γ0(N )\HO
∞. Then

uα(τ) ∈ OH [1/N ]×,

where OH is the ring of integers of the ring class ﬁeld H.

Remark 2. In fact, the values uα(τ) for τ ∈ Γ0(N )\HO
∞ can be used to produce genuine units in
the ring class ﬁeld of O. More precisely, one can show that for every σ ∈ Gal(H/K), we have

(σ − 1)uα(τ) ∈ O×
H .

2.2.3 Heegner points

The construction of Heegner points on an elliptic curve E/Q relies crucially on the modularity
of the elliptic curve E. We brieﬂy recall this notion.
Let f = ∑n≥1 anqn be a newform of weight 2 and level Γ0(N ) for some N ≥ 1; suppose
that its Fourier coeﬃcients are integers. The Eichler–Shimura construction attaches to f an
elliptic curve, as we now recall. Let T2(Γ0(N )) be the Hecke algebra acting on cusp forms of
weight 2 and level Γ0(N ) over Z. Let If be the ideal given by the kernel of the ring morphism
T2(Γ0(N )) → Z sending the Hecke operator Tn to an. Let J0(N ) be the Jacobian of the modular
curve X0(N ) of level Γ0(N ). It is an abelian variety of dimension equal to the genus of X0(N ),
endowed with an action of T2(Γ0(N )). The quotient

Ef := J0(N )/If J0(N )

8

is the elliptic curve attached to f . The composition of the morphism X0(N ) → J0(N ) given by
P ↦→ (P) − (∞) with the projection J0(N ) → Ef yields a surjective Q-rational morphism

πEf : X0(N ) → Ef .

Deﬁnition 3. Given an elliptic curve E, we say that E admits a modular parametrisation if
there exists a surjective Q-rational morphism πE : X0(N ) → E. When this is the case, we say
that E is modular.

The work of Wiles [Wil95], Taylor–Wiles [TW95] on Fermat’s Last Theorem and its gener-
alisations by Breuil, Conrad, Diamond, and Taylor [BCDT01] culminated in a full proof of the
following theorem, formerly known as the Shimura–Taniyama Conjecture.

Theorem 2.2.2. Let E/Q be an elliptic curve. Then E is modular.

Remark 3. For an alternative formulation of modularity via L-functions see [DDT97].

Deﬁnition 4. Let E be a modular elliptic curve, and let πE : X0(N ) → E be its modular parametri-
sation. Heegner points on E are images of points in Γ0(N )\HCM
∞ under πE.

Theorem 2.1.1 implies that Heegner points are deﬁned over ring class ﬁelds of imaginary
quadratic ﬁelds. Their importance in relation to the Birch and Swinnerton–Dyer conjecture
will be discussed in §4.2.

3 Heegner constructions for real quadratic ﬁelds

Given the importance of singular moduli and more general Heegner constructions for algebraic
number theory, it is desirable to have an analogue for real quadratic ﬁelds. While no direct
analogue is available for real quadratic ﬁelds, a (conjectural) theory of “real multiplication”
relying on p-adic methods was recently proposed by Darmon and Vonk in [DV21]. In this
section we will present the theory of rigid meromorphic cocycles, which is the main new tool in
this approach. A rigid meromorphic cocycle is a class in the ﬁrst cohomology of the Ihara group
SL2(Z[1/p]) acting on the non-zero rigid meromorphic functions on the Drinfeld p-adic upper
half plane Hp. These rigid meromorphic cocycles can be evaluated at real quadratic points of
Hp. Conjecturally their values display striking similarities with the classical singular moduli.
In a similar vein, the theory of analytic theta cocycles, obtained by considering cocycles for
the Ihara group with values in analytic functions on Hp deﬁned up to scalars, can be used
to reinterpret constructions of Darmon–Dasgupta [DD06] and Darmon [Dar01] of conjectural
analogues of elliptic units and Heegner points for real quadratic ﬁelds.
Before introducing rigid meromorphic cocycles, we will review the relevant background on
the Drinfeld p-adic upper half plane.

3.1 Drinfeld p-adic upper half plane

In search for an analogue of singular moduli for real quadratic ﬁelds, the ﬁrst obstacle one runs
into is the absence of real quadratic points on the complex upper half plane. However, there
is a p-adic analogue of the complex upper half plane containing many real quadratic points,

9

the Drinfeld upper half plane, which we brieﬂy describe. The Drinfeld upper half plane Hp is a
rigid analytic space1, whose Cp-points are given by

Hp = P1(Cp) \ P1(Qp).

In the following we abuse notation and write Hp for the rigid space and as well as its Cp-
points. The space Hp has an admissible covering by an increasing sequence of open aﬃnoid
subdomains H≤n
p which are constructed by removing balls of decreasing radius around all Qp-
rational points. More explicitly, for each z ∈ P1(Cp) we ﬁx homogeneous coordinates z = [z0 : z1]
such that max{|z0|, |z1|} = 1. Then

H≤n
p = {[z0 : z1] ∈ P1(Cp) | ordp(x0z1 − x1z0) ≤ n ∀[x0 : x1] ∈ P1(Qp)}.

For example, when n = 0, the open aﬃnoid H≤0
p consists of the points [z0 : z1] ∈ P1(Cp) such
that ordp(x0z1 − x1z0) ≤ 0 for any [x0 : x1] ∈ P1(Qp). Hence H≤0
p is obtained from P1(Cp) by
removing balls of radius 1 around the Qp-rational points. The latter are precisely the points
that are mapped to the Fp-rational points under the projection map π : P1(Cp) → P1(Fp), so
that H≤0
p = P1(Cp) \ π−1(P1(Fp)).

For convenience let us include the following ad hoc description of the rigid analytic func-
tions on Hp, which the reader who is unfamiliar with rigid analytic geometry can take as a
deﬁnition.

Deﬁnition 5. • A rigid analytic function on H≤n
p is a limit with respect to uniform conver-
gence of rational functions on P1(Cp) with poles in P1(Cp) \ H≤n
p .

• A rigid analytic function on Hp is a function f : Hp → Cp, such that the restriction of f to
H≤n
p is a rigid analytic function for every n ≥ 0.

• A rigid meromorphic function on Hp is a ratio f = g
h of rigid analytic functions g and h with
h , 0.

We denote by A the set of rigid analytic functions on Hp and by M the set of rigid mero-
morphic functions.
The key structural properties of the rigid space Hp are that it is a smooth 1-dimensional
Stein space and that its algebra of rigid analytic functions A is a reﬂexive Fréchet space.
The group GL2(Qp) acts on Hp by Möbius transformations, i.e., for γ = ( a b
c d ) ∈ GL2(Qp) and
z ∈ Hp, the action of γ on z is given by
 γ · z = az + b
cz + d .

As the center of GL2(Qp) acts trivially, this also deﬁnes an action of PGL2(Qp).

1For an introduction to rigid analytic geometry see e.g. [Con08, Bos14].

10

Figure 1: The Bruhat–Tits tree of PGL2(Q2)

3.1.1 Bruhat–Tits tree for PGL2(Qp)

A useful tool for studying the Drinfeld upper half plane is the Bruhat–Tits tree T attached to
the group PGL2(Qp). We recall its construction.
We call two Zp-lattices Λ and Λ′ in Q2
p equivalent if they are homothetic. This deﬁnes
an equivalence relation on the set of all Zp-lattices in Q2
p. The set of vertices of the tree T is
deﬁned to be the set of equivalence classes of lattices:

V (T ) := {Λ ⊆ Q2
p Zp-lattice}/ ∼ .

By deﬁnition two vertices v, v′ ∈ V (T ) are connected by an edge in the graph T if there are
representatives v = [Λ] and v′ = [Λ′], such that pΛ ⊊ Λ′ ⊊ Λ. One can show that the graph
deﬁned by this is a homogeneous tree of degree p + 1. For example, Figure 1 shows a part of
the Bruhat–Tits tree for p = 2.
The group GL2(Qp) acts transitively on the set of all Zp-lattices in Q2
p, preserving the equiv-
alence classes. This induces a transitive action of GL2(Qp) and of PGL2(Qp) on T .

Example 1. The lattice Z2
p gives rise to a vertex called the standard vertex v0 = [Z2
p]. The adjacent
vertices of v0 are given by
(0 −1
1 0
 ) (
1 0
0 p
) v0 and (1 0
λ 1

) (
1 0
0 p
) v0 for λ ∈ Fp.

Moreover, if we consider the action of SL2(Z[1/p]) on T , the stabiliser of the standard vertex is
the group SL2(Z) and the stabiliser of the edge e0 from v0 to ( 1 0
0 p ) v0 is the congruence subgroup
Γ0(p).

There is the so-called reduction map

red : Hp → |T |

from the p-adic upper half plane to the geometric realisation of T . We refer to [DT08] for
details regarding its construction. Via this map, the tree T serves as a nice combinatorial tool
to study the Drinfeld upper half plane. Let us indicate a few features of the reduction map.
It is equivariant for the action of PGL2(Qp). Moreover we can recover the aﬃnoids H≤n
p in the
admissible covering described above as inverse images

H≤n
p = red−1(|T ≤n|),

11

where T ≤n is the subtree of T consisting of all vertices and edges which have distance ≤ n to
the standard vertex v0 = [Z2
p]. Finally, the reduction map allows us to view Hp as a tubular
neighbourhood of the Bruhat–Tits tree. For example, the inverse image of the edge e0 is the
annulus red
−1(e0) = {z ∈ Cp|1 < |z| < p}.

3.1.2 RM points on the Drinfeld p-adic upper half plane

We introduce some notation for real quadratic points on Hp which will later be used to deﬁne
the evaluation of rigid meromorphic cocycles.
Let τ ∈ Cp. We say that τ is a real quadratic point of discriminant D if [τ : 1] satisﬁes
the homogeneous quadratic equation AX2 + BXY + CY 2 = 0 with A, B, C ∈ Z coprime integers
satisfying D = B2 − 4AC > 0, with D not a square.
Then K = Q(τ) is a real quadratic extension of Q and the point [τ : 1] ∈ P1(Cp) lies in
Hp if and only if the prime p does not split in K. We refer to points arising in this way as
real multiplication points or RM points of Hp and denote the set of these points as HRM
p . For
τ ∈ HRM
p , deﬁne
 Oτ := {(
a b
c d
) ∈ M2(Z[1/p]) : aτ + b = cτ2 + dτ} .

Then Oτ is isomorphic to a Z[1/p] order in the real quadratic ﬁeld K = Q(τ) via the inclusion

Oτ ֒→ K, γ = (
a b
c d
) ↦→ cτ + d.

Let Γ := SL2(Z[1/p]) denote the Ihara group. Let O×
τ,1 denote the elements in O×
τ of reduced
norm one. The Dirichlet S-unit Theorem implies that the stabiliser

StabΓ(τ)   O×
τ,1   {±1} × ⟨γτ⟩

is up to torsion a free group of rank 1. It is generated by a fundamental unit γτ of norm
1, called the automorph of τ. Moreover the points of HRM
p are precisely those for which the
stabiliser in Γ has rank 1. This feature is crucial to the evaluation of the rigid meromorphic
cocycles deﬁned in the subsequent sections. We note that the action of Γ on HRM
p need not
preserve the discriminant, but it does preserve its prime-to-p part.

3.2 Group actions, curves and p-adic theta functions

We review the theory of p-adic theta functions arising in the context of p-adic uniformisation
of Shimura curves. While the construction of rigid cocycles does not ﬁt in this setting, the
cocycles arising in §3.3 are obtained via similar methods, after an appropriate degree shift in
cohomology.

Let Γ0 ⊂ SL2(Qp) be any subgroup. We say that Γ0 acts discretely on Hp if the orbit Γ0τ of
each element τ ∈ Hp intersects each of the aﬃnoids H≤n
p only in ﬁnitely many points.
Note that the groups SL2(Z), SL2(Z[1/p]) and SL2(Zp) all act non-discretely on Hp. To see
this recall that SL2(Z) is contained in the stabiliser of the standard vertex v0 of the Bruhat–Tits

12

tree and that any element τ ∈ H≤0
p is mapped to v0 via the reduction map. So the whole orbit
SL2(Z)τ is contained in H≤0
p = red−1(T ≤0) and the set SL2(Z)τ ∩ H≤0
p contains inﬁnitely many
elements.
The upper half plane Hp is of major signiﬁcance for arithmetic geometry as it can be used
to construct families of algebraic curves (so-called Mumford curves) which uniformise certain
Shimura curves p-adically. These curves arise as quotients of Hp by discrete group actions. We
refer to [DT08, §2.4] and references therein for details. Here we only mention the following
class of examples.

Example 2. Let B be the deﬁnite quaternion algebra Q[i, j ] ⊂ H inside the Hamilton quaternions
and let R = Z[i, j , i+j +k+1
2 ] be a maximal order. Choose an odd prime p at which B splits and
consider the group ΓB = (R[1/p])×
1 of units γ ∈ R[1/p]× of reduced norm 1. After choosing an
isomorphism (B⊗QQp)×   GL2(Qp) the group ΓB embeds into SL2(Qp) and acts discretely on Hp.
Let Γ′ ⊂ ΓB be a subgroup of ﬁnite index which has no ﬁxed points on Hp. Then the quotient
space XΓ′ = Γ′\Hp is a rigid analytic space which admits a model as a Shimura curve.

Note that a deﬁnite quaternion algebra does not admit an embedding of a real quadratic
ﬁeld. Essentially due to this fact the quotients XΓ′ are not so relevant for a theory of real
multiplication. As we will see below, a better setup for these purposes is to consider the in-
deﬁnite quaternion algebra B = M2(Q) and the (non-discrete) actions of groups like SL2(Z) and
SL2(Z[1/p]) on Hp.
Nevertheless we want to brieﬂy discuss one aspect from the theory of Mumford curves, the
construction of p-adic theta functions. These are important tools in the study of the Jacobian
of the compactiﬁcation of a Mumford curve. Key ideas of their construction can be modiﬁed to
construct interesting functions also in situations where a non-discrete group action is involved.
Assume that Γ0 ⊂ SL2(Qp) is a subgroup which acts discretely and without ﬁxed points on Hp.
The p-adic theta functions for Γ0 are meromorphic functions on Hp, which are invariant under
Γ0 up to multiplicative scalars and which can be constructed as follows.
For an element w ∈ P1(Cp), deﬁne the rational functions tw on P1(Cp) by

tw(z) =
 



z − w, if |w| ≤ 1,
z/w − 1, if |w| > 1,
1, if w = ∞.

Note that for two distinct elements w+, w− in Hp and γ ∈ Γ0 the quotient function

tw+ (γ z)
tw− (γ z)

has a simple zero at γ −1w+ and a simple pole at γ −1w−, as does the function tγ−1w+ (z)
tγ−1w− (z) . Therefore

they are equal up to a constant.
Now consider the degree zero divisor ∆ = w+ − w−. Then the product

f ∆(z) = ∏

γ ∈Γ0
 tγ w+(z)

tγ w−(z)

13

converges to a rigid meromorphic function on Hp. (For more details, see Section 2.2 in [DV21].)
By the observation above, the function f ∆ is Γ0-invariant up to multiplication by a constant in
Cp. Hence, it deﬁnes an element of (M×/C×
p )Γ0 = H 0(Γ0, M×/C×
p ). The function f ∆ is called the
p-adic theta function associated to the degree zero divisor ∆.

3.3 Rigid meromorphic cocycles

One way of looking at the j -function is as an SL2(Z)-invariant function on the complex up-
per half plane H∞, i.e., an element of H 0(SL2(Z), Hol(H∞)), where Hol(H∞) denotes the holo-
morphic functions on H∞. Now consider Γ := SL2(Z[1/p]) acting on Hp. In search for direct
analogues of j in the p-adic setting, one might ﬁrst naturally want to consider the groups
H 0(Γ, A) or H 0(Γ, M). However it follows essentially from the Weierstrass preparation theorem
that any Γ-invariant rigid analytic function must be constant (cf. [DV21, Lemma 1.9]), hence
H 0(Γ, A)   Cp   H 0(Γ, M) and so these groups do not contain interesting functions. Consider-
ing the corresponding cohomology groups in degree one on the other hand turns out to be a
successful strategy, even more so if one furthermore switches to the multiplicative theory. This
leads to the following deﬁnition:

Deﬁnition 6. • A rigid meromorphic (resp. analytic) cocycle is an element in H 1(Γ, M×) (resp.
in H 1(Γ, A×)).

• A rigid meromorphic (resp. analytic) theta cocycle is an element in H 1(Γ, M×/C×
p ) (resp. in
H 1(Γ, A×/C×
p )).

Let Γ∞ ⊂ Γ be the subgroup of upper triangular matrices. A rigid meromorphic cocycle
is called parabolic if its restriction to Γ∞ is trivial. It is called quasi-parabolic if its restriction
to Γ∞ lies in the image of H 1(Γ∞, C×
p ). The groups of such cohomology classes are denoted by
H 1
par(Γ, M×) and H 1
f (Γ, M×), respectively. One can show that any cohomology class in H 1
f (Γ, M×)
has a unique representative, whose values on Γ∞ consist of constant functions.

Remark 4. One reason for considering the multiplicative group M× as coeﬃcients rather than
the additive group M is the connection to the theory of modular symbols and so-called rigid
meromorphic period functions. More precisely, the subgroup H 1
par(Γ, M×) can be identiﬁed
with the group of Γ-invariant modular symbols MS Γ(M×) ([DV21, Section 1]). This connection
to modular symbols is useful for establishing structural results. It also allows one to produce
many interesting elements in H 1(Γ, M×). Contrary to this, the group H 1(Γ, M) contains no
parabolic elements ([DV21, Remark 1.8]).

In practice it is easier to write down examples of theta cocycles (we will give a few of these
below). Note that there is a natural map H 1(Γ, M×) → H 1(Γ, M×/C×
p ) and one would like to lift
theta cocycles to rigid meromorphic cocycles. Unfortunately this is in general not possible as
there is an obstruction to lifting. What is possible though is to lift the restriction of a theta
cocycle to the group SL2(Z) to an element in H 1(SL2(Z), M×), as H 2(SL2(Z), C×
p ) = 0. In some
situations this is good enough.
 14

3.3.1 Examples

Let us discuss some examples.

Example 3 (The trivial cocycle). Fix a base point ξ ∈ P1(Qp). For any γ ∈ Γ, deﬁne the rational
function Jtriv(γ )(z) := z − γ ξ
z − ξ .

Up to a scalar this function is uniquely determined as the rational function with divisor
(γ ξ) − (ξ). Then for two elements γ1, γ2 ∈ Γ, the function Jtriv(γ1γ2) is the function with divisor
(γ1γ2ξ) − (ξ) = (γ1γ2ξ) − (γ1ξ) + (γ1ξ) − (ξ). Hence up to a scalar, Jtriv(γ1γ2) is the same as
Jtriv(γ1)γ1Jtriv(γ2). So we obtain a rigid analytic theta cocycle Jtriv ∈ H 1(Γ, A×/C×
p ).

Example 4. (Theta cocycles attached to RM points). This example is inspired by a similar con-
struction in the theory of rational modular cocycles (see [DV21, Section 1.4]). As we have
observed above, Γ does not act discretely on Hp. However, it does act discretely on the product
Hp × H∞ of the Drinfeld upper half plane and the complex upper half plane H∞. We can use
this to construct examples of theta cocycles as follows.
For a tuple (r, s) ∈ P1(Q)2 and w real quadratic, let w′ be its algebraic conjugate. The
geodesic from r to s in H∞ cuts H∞ = H∞ ∪ R ∪ {∞} into two connected components, say "on
the right hand side" of the geodesic is the −-component H−
∞ and on the left hand side is the
+-component H+
∞ (see Figure 2). This allows us to deﬁne the following symbol

(r, s)(w, w′) :=
 



0, if w, w′ are in the same connected component
1, if w ∈ H+
∞, w′ ∈ H−
∞
−1, if w ∈ H−
∞, w′ ∈ H+
∞.
 (3)

We refer to it as the signed intersection number of the geodesics from r to s and from w to w′.
For example the intersection number of the geodesics in Figure 2 is −1.

r sw w′

−

+
 H∞

Figure 2: Intersection of geodesics

For an RM point τ ∈ HRM
p , deﬁne the function

Jτ : Γ → M×

γ ↦→ ∏

w∈Γτ tw(z)(γ ∞,∞)(w,w′ ),

where tw(z) is as in Section 3.2.
 15

As it turns out, the set of elements w ∈ Γτ such that (γ ∞, ∞)(w, w′) , 0 is a discrete subset
of Hp. One can show that the product converges, that indeed Jτ(γ ) deﬁnes a non-zero rigid
meromorphic function and that furthermore Jτ deﬁnes a class in H 1(Γ, M×/C×
p ).

Example 5 (The winding cocycle). Let us also mention here the so-called winding cocycle from
[DPV21, Section 2.3], which is an example of a rigid analytic theta cocycle. To deﬁne it choose
a base point ξ = (ξp, ξ∞) ∈ Hp × H∞, such that ξp ∈ H≤0
p and ξ∞ does not lie in any geodesic in
the Γ-orbit of [0, ∞]. Denote by Σ the Γ-orbit of the pair (0, ∞) in P1(Q)2 and deﬁne for every
γ ∈ Γ and z ∈ Hp
 J ξ
(0,∞)(γ )(z) := ∏

(r,s)∈Σ
 ( ξp − r

ξp − s · z − s
z − r
 )(r,s)(ξ∞,γ ξ∞) ,

using the usual conventions when some of the points are ∞ and where (r, s)(ξ∞, γ ξ∞) denotes
the signed intersection number as in (3). The function J ξ
(0,∞)(γ ) converges to a rigid analytic

function on Hp and γ ↦→ J ξ
(0,∞)(γ ) satisﬁes the cocycle condition up to scalars in C×
p (cf. [DPV21,

Proposition 2.5]). The corresponding class in H 1(Γ, A×/C×
p ) is independent of the choice of base
point [DPV21, Prop. 2.6] and is called the winding cocycle and we denote it by J(0,∞).

3.3.2 Hecke module structure of rigid meromorphic cocycles

On the space H 1(Γ, M×) of rigid meromorphic cocycles and on the space H 1(Γ, M×/C×
p ) of rigid
meromorphic theta cocycles one can deﬁne Hecke operators Tn for any n ≥ 1. This is done by
decomposing a relevant union of double cosets into cosets and following a recipe of Shimura.
We refer to [DPV21, §2.4] for details.

Deﬁnition 7. Given a quasi-parabolic rigid meromorphic cocycle J, its rigid meromorphic period
function is the value at S := ( 0 −1
1 0 ) ∈ Γ of the quasi-parabolic representative of J.

Let us deﬁne the abstract Hecke algebra as T := Z[Tn , n ≥ 1]. One can then prove the
following structural result.

Theorem 3.3.1 ([DV21, Theorem 1 and Remark 2]). The group H 1(Γ, M×) is of inﬁnite rank. Any
ﬁnite rank T-stable submodule of H 1
f (Γ, M×) is contained in H 1
f (Γ, A×).

Analytic theta cocycles behave diﬀerently. As Hecke modules, they are closely related to
modular forms. In [DV22], Darmon and Vonk prove a classiﬁcation result using ideas of
Stevens and Schneider–Teitelbaum. We brieﬂy review the key points (see also [DPV21, Sec-
tion 3.1]).

Consider the annulus U := {z ∈ Cp| 1 < |z| < p}. Its stabiliser in Γ is Γ0(p). Denote dlogf :=
f ′(z)
f (z) dz. The group homomorphism

A× → Cp, f ↦→ resU (dlogf ),

where resU denotes the p-adic annular residue along U , is Γ0(p)-equivariant and trivial on
constants. It can be shown that it takes values in Z. This induces a map on cohomology

δU := resU ◦dlog : H 1(Γ, A×/C×
p ) → H 1(Γ0(p), Z).

16

Theorem 3.3.2. [DV22, Section 3]. The map

δU ⊗ 1 : H 1(Γ, A×/C×
p ) ⊗ Q → H 1(Γ0(p), Z) ⊗ Q

is surjective and has a 1-dimensional kernel, generated by the analytic theta cocycle Jtriv.
The map δU admits a Hecke-equivariant section

ST
× : H 1(Γ0(p), Z) → H 1(Γ, A×/C×
p ).

The section ST
× above is called the multiplicative Schneider–Teitelbaum lift, and one can use
it to classify the analytic theta cocycles as follows.

Theorem 3.3.3. [DV22, Section 3]. The space H 1(Γ, A×/C×
p ) ⊗ Q is of dimension 2g + 2, where g is
the genus of the modular curve X0(p). The Hecke action factors through the faithful Hecke algebra of
modular forms M2(Γ0(p)).

3.4 Heegner constructions

The crucial motivation for the study of rigid meromorphic cocycles and analytic theta cocycles
is the construction of conjectural analogues of Heegner objects for real quadratic ﬁelds. In
analogy with the Heegner constructions, they can be viewed as images of maps

Φ : Γ\HRM
p → X(Cp)

for the group schemes X/Q appearing in §2.2.
The corresponding images are expected to be global. Note that however in the RM settings
these maps will be deﬁned exclusively at RM points in Hp via the evaluation of rigid meromor-
phic or theta cocycles, which we now describe.

3.4.1 Evaluation at RM points

We now deﬁne the evaluation of quasi-parabolic rigid meromorphic cocycles at RM points.
Recall that for τ ∈ HRM
p , γτ ∈ Γ denotes the automorph of τ as deﬁned in 3.1.2.

Deﬁnition 8. Let [J] ∈ H 1
f (Γ, M×) be a quasi-parabolic rigid meromorphic cocycle. Consider a

representative J ∈ [J] given by a map J : Γ → M× such that J(Γ∞) ⊂ C×
p and let τ ∈ HRM
p . Deﬁne
the evaluation of J at τ as J[τ] := J(γτ)(τ) ∈ Cp ∪ {∞}.

Remark 5. One can check that this is constant on Γ orbits.

Remark 6. Deﬁning the evaluation of a theta cocycle at an RM point is also possible but requires
some extra work involving the restriction to (a conjugate of) SL2(Z). We refer to Section 2.3
of [DV22] for the deﬁnition. When the theta cocycle lifts to a rigid meromorphic cocycle,
the values essentially agree. When the cocycle does not lift, the values are expected to be
transcendental in general, but are still of arithmetic interest as they are related to Gross–Stark
units (see Conj. 2) and Stark–Heegner points (see Conj. 3) below.

17

3.4.2 Singular moduli for real quadratic ﬁelds

Let τ ∈ HRM
p and write Hτ for the narrow ring class ﬁeld corresponding to Oτ. For a quasi-
parabolic rigid meromorphic cocycle J we let j be its associated period function (see Def. 7).
Then we deﬁne a ﬁeld Hj = HJ := Compositumj (τ)=∞(Hτ),

which is a ﬁnite extension of Q.

Deﬁnition 9. Let τ ∈ Γ\HRM
p . For a quasiparabolic meromorphic cocycle J, we say that J[τ] is
a real quadratic singular modulus.

The following conjecture, due to Darmon and Vonk, justiﬁes the analogy with the values of
the j -function at CM points.

Conjecture 1 ([DV21]). If J ∈ H 1
f (Γ, M×), then J[τ] is algebraic and lies in the compositum of HJ
and Hτ.

Note that the analogy with classical singular moduli is imperfect, because the choice of
cocycle J impacts the ﬁeld of deﬁnition of its value. A perhaps more appropriate analogy is
that these values should be thought of as multiplicative analogues of diﬀerences of singular
moduli, lying in composita of the corresponding ring class ﬁelds.

3.4.3 Elliptic units for real quadratic ﬁelds

Consider the unique (normalised) Eisenstein eigenform of weight 2 and level Γ0(p) with Fourier
expansion
 E(p)
2 = p − 1
12 + ∑

n≥1
 

 ∑

d|n,p∤d d

 qn.

For a choice of base point z0 ∈ H∞, the function computing path integrals of the diﬀerential
attached to the Eisenstein series
 γ ↦→ ∫ γ z0

z0
 1
2πi E(p)
2 (z)dz

for γ ∈ Γ0(p) takes integer values and transforms as a (non-parabolic) cocycle ϕDR ∈ H 1(Γ0(p), Z).
Its values can be described explicitly in terms of Dedekind sums (see [DD06, §2.5]).
The Schneider–Teitelbaum lift JDR := ST×(ϕDR)

of ϕDR to H 1(Γ, A×/C×
p ) is called the Dedekind–Rademacher theta cocycle.

Deﬁnition 10. Let τ ∈ Γ\HRM
p be a point of discriminant D prime to p. The value JDR[τ] is
called the real quadratic elliptic unit attached to τ.

Its values at RM points in Hp should be thought of as analogues of the elliptic units deﬁned
in §2, as the following conjecture suggests.
 18

Conjecture 2. [DD06, Conj. 2.14] Let τ ∈ Hp be a real quadratic point of discriminant D prime to
p and let Hτ be the narrow ring class ﬁeld of the order deﬁned by τ. Then the real quadratic elliptic
unit attached to τ satisﬁes JDR[τ] ∈ OHτ [1/p]×.

Note that unlike in the CM setting, these values are expected to be p-units rather than
genuine units in the Hilbert class ﬁeld. The analogy with the construction of elliptic units is
perhaps not obvious on the surface. However, the Eisenstein series E(p)
2 whose periods appear
in the deﬁnition above can be viewed as the logarithmic derivative of ∆(pz)/∆(z), a typical
example of the modular unit featuring in §2.2.2.

3.4.4 Stark–Heegner points

Let f be a newform of weight 2 and level Γ0(p), with Fourier coeﬃcients valued in Z. Consider
the diﬀerential form ωf = 2πif (z)dz, and let

ω+
f = ωf + ωf , and ω−
f = ωf − ωf .

be its real and imaginary part, respectively. Given z0 ∈ H∞, the maps ˜φf : Γ0(p) → R deﬁned by

γ ↦→ ∫ γ z0

z0 ω±
f ,

can be rescaled by suitable periods Ω±
f in such a way that the pair of cocycles ϕ±
f := 1/Ω±
f ˜ϕ±
f
take values in Z. The Schneider–Teitelbaum lifts of the cocycles deﬁned above

J ±
f := ST×(ϕ±
f )

are called the elliptic theta cocycles attached to f .
By the Eichler–Shimura construction reviewed in §2.2.3, a newform f ∈ S2(Γ0(p)) as above
corresponds to an elliptic curve E := Ef with multiplicative reduction at p. For such an elliptic
curve, Tate showed that its Cp-valued points can be uniformised as

ΨTate : C×
p /qZ
E ∼
−→ E(Cp)

for some parameter qE ∈ C×
p satisfying |qE| < 1.

Deﬁnition 11. Let τ ∈ Γ\HRM
p be a point of discriminant D prime to p. A Stark–Heegner point
for E attached to τ is P±
τ := ΨTate(J ±
f [τ]) ∈ E(Cp).

The following conjecture, originally formulated by Darmon in [Dar01] motivates the con-
jectural analogy between Stark–Heegner points and the classical Heegner points in CM theory.

Conjecture 3 ([Dar01],[DV22, Conjecture 3.18]). Let τ ∈ Γ\HRM
p be a point of discriminant D
prime to p. Denote Hτ the narrow ring class ﬁeld of the order Oτ attached to τ. Then

P±
τ ∈ E(Hτ).

19

In addition, the point P±
τ is expected to lie in the (±1)-part of E(Hτ) for the action of the
complex conjugation in the narrow Hilbert class ﬁeld of τ.

Remark 7. The above conjecture (and suitable generalisations) has been veriﬁed extensively,
see for example [DP06]. The theoretical evidence is much more fragmentary, and no general
approach is known at this stage. However, an important case was showed in the article [BD09]
for Stark–Heegner points deﬁned over genus ﬁelds of real quadratic ﬁelds by relating them to
Heegner points in this special setting.

4 Families of real analytic Eisenstein series and CM theory

In this section, we introduce the second main theme of this article, which is how modular
generating series constructed from Heegner objects appear in relation to derivatives of families
of modular forms. We will start by reviewing some archimedean examples; we will then move
to their p-adic counterparts in §5.
In the archimedean setting, derivatives of real analytic families of Eisenstein series ﬁt
prominently in the Kudla program. Roughly speaking, this vast program seeks to show that
certain formal q-expansions encoding special cycles on orthogonal Shimura varieties are mod-
ular. The most basic instances of these statements involve CM cycles on modular curves. The
works [GZ85], [GZ86] of Gross and Zagier were indispensable to the emergence of this pro-
gram. In §4.1, we will give an account of their work on the diﬀerences of singular moduli,
which will be close in spirit to the p-adic analogues discussed in §5. We will then give a brief
overview of the work of Gross and Zagier on the derivative of the L-function attached to an
elliptic curve [GZ86]. Finally in §4.3 we explain how the two articles can be interpreted under
a uniﬁed perspective, which will be translated in the p-adic setting in §5.

4.1 Gross–Zagier’s factorisation formula

We review the work of Gross and Zagier on the factorisation of diﬀerences of singular moduli,
the CM values of the j -function introduced in §2.2.1. Their landmark work unveiled new
phenomena in the theory of complex multiplication, initiating the study of the intersection
theory of CM cycles on modular curves via automorphic methods.
Let us introduce the main result. Let D1 and D2 be two negative relatively prime funda-
mental discriminants. Let D = D1D2 and let wi be the number of roots of unity in the quadratic
orders of discriminant Di. For τ ∈ H∞ denote by [τ] the equivalence class of τ under the action
of SL2(Z). The main theorem of complex multiplication implies that the product

J(D1, D2) = ∏

[τ1], discτ1=D1
[τ2], discτ2=D2
 (j (τ1) − j (τ2))
 4
w1w2

(or more precisely, its square for Di ≥ −4) is an integer. Gross and Zagier are motivated by the
deceptively simple question of determining its prime factorisation.
For primes ℓ with ( D1D2
ℓ ) , −1 deﬁne

ǫ(ℓ) =
 


( D1
ℓ ) if (ℓ, D1) = 1,
( D2
ℓ ) if (ℓ, D2) = 1.

20

Now if n = ∏i ℓai
i is such that ( D1D2
ℓi ) , −1 for all i, then we deﬁne ǫ(n) = ∏
i ǫ(ℓi)ai . Gross and
Zagier prove the following theorem.

Theorem 4.1.1. [GZ85, Thm 1.3]

J(D1, D2)2 = ± ∏

x,n,n′ ∈Z
n,n′>0,
x2+4nn′=D
 nǫ(n′ ). (4)

In loc. cit, the authors provide two alternative proofs of this result. The ﬁrst one is essen-
tially algebraic and relies on the moduli interpretation of CM points on the modular curve.
The second is purely analytic and makes use of automorphic techniques to obtain a formula
for J(D1, D2)2. While one can easily deduce the algebraicity of J(D1, D2) from the theory of com-
plex multiplication, no use of this fact is made in the analytic proof, where instead it can be
seen as a byproduct of the proof itself. In view of translating the Gross–Zagier approach to the
RM setting, the analytic strategy is of course more relevant, as a moduli interpretation of RM
points of the Drinfeld p-adic upper half plane is lacking.

We will brieﬂy outline some ideas behind the algebraic proof before focusing on the analytic
one. The general idea is rather natural: if a prime p divides J(D1, D2)2, there is a pair of elliptic
curves with CM by two orders OK1 and OK2 with isomorphic reductions over Fp. This forces the
endomorphism ring of the reduction to be a maximal order in the quaternion algebra ramiﬁed
at p and ∞.
The existence of embeddings of the orders OKi into an order in a quaternion algebra of
discriminant p is rather restrictive on the prime. Working out explicit conditions, one deter-
mines the primes contributing to the factorisation of J(D1, D2)2. A delicate calculation using
Deuring’s theory of endomorphisms of elliptic curves in ﬁnite characteristic is necessary to de-
termine the precise exponent in the factorisation formula.

The ﬁrst step of the analytic proof consists in producing a reformulation of (4) more suitable
to analytic manipulation. Let F = Q(√
D) and consider the diagram of quadratic extensions

Q

Q(
√
D1) Q(√
D2)

Q(
√
D1, √
D2)

F

where Q(√
D1, √D2) is an unramiﬁed extension of the real quadratic ﬁeld F. By Artin reci-
procity, the genus character cutting out this extension can be viewed as a quadratic character
of the narrow class group Cl+(OF) of F, which we denote by χ. An elementary calculation
shows that the explicit factorisation formula for J(D1, D2) is equivalent to

− log |J(D1, D2)|
2 = ∑

ν∈d−1
+ ,Trν=1
 ∑

n|(νd) χ(n) logNm(n), (5)

21

where d−1
+ denotes the totally positive elements in the inverse diﬀerent d−1 of OF. The right
hand side of (5) evokes formulae appearing in the work of Siegel on special values of Dedekind
ζ-functions for totally real ﬁelds [Sie69, §2]. For ν ∈ F, denote (ν1, ν2) its real embeddings. For
z = (z1, z2) ∈ H2
∞ and (ν, µ) in F2, we let

Nm(µz + ν) := (µ1z1 + ν1) · (µ2z2 + ν2).

The formulae appearing in loc. cit. arise as restrictions of Hilbert Eisenstein series of weight
(k, k), where k ≥ 2 is an even integer, and level SL2(OF), which are given by

EF,k(z) = ∑

a∈Cl(OF ) Nm(a)k ∑

(m,n)∈(a2)′ /O×
F
 Nm(mz + n)−k, for z ∈ H2
∞, (6)

along the diagonal embedding ∆ : H∞ → H2
∞. The diagonal restriction inherits modular prop-
erties from those of EF,k. It is an elliptic modular form of weight 2k and level 1. Siegel’s
formulae are obtained by expressing the resulting form, whose constant term in the Fourier
expansion encodes the Dedekind special value, in terms of a basis of the space of elliptic mod-
ular forms for small values of k.
The strategy of Gross and Zagier consists of mimicking Siegel’s approach in the degenerate
case in which k = 1. The series in (6) would not converge for k = 1. The problem can be obviated
by considering the family of real analytic Hilbert Eisenstein series of parallel weight one

EF,1,s(z) = ∑

a∈Cl(OF ) χ(a) Nm(a)1+2s ∑

(m,n)∈(a2)′ /O× Nm(mz + n)−k |Nm(mz + n)|
−s y
s (7)

for a complex variable s with Re(s) > 0. For ﬁxed values z ∈ H2
∞, this deﬁnes a holomorphic
function of s, and it can be extended meromorphically to all of C. The strategy for constructing
holomorphic weight 1 Eisenstein series, also known as Hecke’s trick, consists in taking the limit
of EF,1,s as s tends to 0. In this setting, Hecke’s trick fails at producing an interesting weight
one Hilbert Eisenstein series: an unexpected cancellation occurs when computing the corre-
sponding Fourier expansion. Gross–Zagier are drawn to consider instead the derivative E′
F,1,s
at s = 0. This is a real analytic weight 1 Hilbert modular form; it can be restricted along the
diagonal embedding ∆ to obtain a (non-holomorphic) elliptic modular form of weight 2, as in
[Sie69]. From this real analytic form ∆∗E′
F,1 one can extract a holomorphic one by applying a
projector onto the holomorphic subspace as in [Stu80]. The resulting modular form, denoted
by (∆∗E′
F,1)hol, is the object of the following theorem, summarising the calculations in [GZ85,
§7].

Theorem 4.1.2. The ﬁrst Fourier coeﬃcient a1 of the holomorphic modular form (∆∗E′
F,1)hol of
weight 2 and level SL2(Z) satisﬁes the equation

a1 · λ = log |J(D1, D2)|
2 + ∑

ν∈d−1
+ ,Trν=1
 ∑

n|(νd) χ(n) logNm(n),

for some λ ∈ C×.

Now as (∆∗E′
F,1)hol is of weight 2 and level SL2(Z), one abstractly knows that it is the zero
function, hence a1 = 0 and the equality (5) follows.

22

4.2 Gross–Zagier’s work on BSD in analytic rank 1

Beyond the factorisation of diﬀerences of singular moduli, the circle of ideas of [GZ85] yielded
some striking developments towards the Birch and Swinnerton-Dyer Conjecture.
Let E/Q be an elliptic curve. The L-function L(E, s) is deﬁned as a convergent inﬁnite prod-
uct for Re(s) > 3/2. If E is modular, that is L(f , s) = L(E, s) for a suitable modular form f , the
L-function L(E, s) admits analytic continuation to all of C and functional equation with centre
s = 1. The Birch and Swinnerton-Dyer Conjecture states that the algebraic rank, that is the
rank of the group E(Q), is equal to the analytic rank, the order of vanishing of L(E, s) at s = 1.
The main result in [GZ86] is the following.

Theorem 4.2.1. [GZ86, Thm. 7.3] Suppose that L(E, 1) = 0. There exists a point P ∈ E(Q) such that

L′(E, 1)   ΩE⟨P, P⟩

where ΩE is the real period of a regular diﬀerential on E, the pairing ⟨·, ·⟩ denotes the Néron-Tate
height pairing on E(Q) ⊗ R and the equality denoted by   is deﬁned up to scalars in Q×.

In particular, if the analytic rank is one, the rank of the Mordell–Weil group E(Q) is posi-
tive. This result was later complemented by Kolyvagin’s work bounding the algebraic rank in
analytic rank 0 and 1. The point P arises as a Heegner construction (see below). Combining
the results of Gross–Zagier and Kolyvagin, one can conclude that this Heegner construction
produces non-torsion points in E(Q) precisely when the algebraic (or analytic) rank is 1.
Let us discuss some ingredients of the proof. Let N be the conductor of E. The assumption
that E is modular implies that up to isogeny E is a direct factor of the Jacobian J0(N ) of the
modular curve of level X0(N ). Let D < 0 be a fundamental discriminant coprime to N , and let
K = Q(√
D). Let τ ∈ H∞ be an element with discriminant D deﬁning a CM point of the modular
curve of level Γ0(N ). Then the divisor cτ := (τ) − (∞) deﬁnes an H-rational point of J0(N ), where
H is the Hilbert class ﬁeld of K. By Shimura reciprocity, the divisor

cD = ∑

[τ] : disc(τ)=D cτ,

where the sum runs over a set of representatives of the Γ0(N )-orbits of points of discriminant D
in H∞, is K-rational. The point P appearing in the statement of Theorem 4.2.1 is constructed
as a suitable trace of the divisor cD.
The vector space J0(N )(H) ⊗ R is endowed with a canonical height pairing, which can be
described as a sum of local heights and is equivariant for the Hecke action.
The formal q-expansion GD(q) = ∑

n≥1⟨cD, TncD⟩qn (8)

is the q-expansion of a modular forms of weight 2 and level Γ0(N ). This formal series GD(q) is a
prototypical example of a modular generating series. It packages pairings of Hecke translates of
Heegner objects into a formal q-expansion. Its modularity follows from the fact that the Hecke
action on the Jacobian of the modular curve factors through the Hecke algebra of modular
forms of weight 2 and level Γ0(N ).
The proof of Theorem 4.2.1 hinges on providing an alternative construction of the f -isotypic
component of the series GD which can be related to L-values. For this, the key input is the

23

Rankin–Selberg method. It allows to reinterpret the derivative L′(f /K, s) at s = 1 as the f -
isotypic component of the holomorphic projection of the product of

• a weight 1 theta series θ1 attached to K and

• the derivative at s = 0 of a family of real analytic Eisenstein series E1,s of constant weight
1, parametrised by a complex variable s.

The comparison between the modular generating series GD and the holomorphic projection
of θ1 · E′ involves matching local contributions for both. In particular, it requires computing
local height pairings for the divisor cD at non-archimedean places via intersection theory, and
at archimedean places via Green functions.

4.3 Biquadratic extensions and modular generating series

While the arithmetic applications of [GZ85] and [GZ86] are on the surface fairly diﬀerent, the
strategies of proof ﬁt into a general framework. The diagram 4.1 can be viewed as a special
case of a diagram of quadratic ﬁeld extensions (or, more generally, of étale algebras of degree
2) of the form
 Q

K1 K2

L

F

where F is a real quadratic ﬁeld (or a split quadratic algebra over Q, that is F ≃ Q × Q) and
Ki = Q(√
Di) are imaginary, so that L is forced to be a CM extension of F.
For the imaginary quadratic ﬁelds K1 and K2, one can produce Heegner divisors cDi at-
tached to points of discriminant Di in the Jacobian of modular curves of suitable level. As in
(8), the global height pairings on the Hecke translates of cDi can be parlayed into a modular
generating series GD1,D2(q) = ∑n≥1⟨cD1, TncD2⟩qn. The setting of Gross–Zagier’s work on BSD in
analytic rank 1 corresponds to the degenerate case in which the imaginary quadratic ﬁelds are
equal, F is the split quadratic algebra over Q, and L = K1 × K1.
Obtaining an explicit characterisation of the Fourier coeﬃcients of GD1,D2 is an essential
step towards the desired arithmetic applications:

• In [GZ85], the quantity J(D1, D2) can be read oﬀ the archimedean contribution of the
height pairing ⟨cD1, cD2⟩ for the modular curve of level 1;

• In [GZ86], for a modular elliptic curve E corresponding to a newform f , the f -isotypic
component of GD1,D2 encodes the height of the Heegner point appearing in the statement
of 4.2.1.

The crucial idea in both [GZ85] and [GZ86] is to express the modular generating series
GD1,D2 in an alternative form by exploiting the derivative of a suitable family Gs of real an-
alytic Hilbert modular forms of constant parallel weight 1 for the quadratic Q-algebra F,
parametrised by the variable s ∈ C. In [GZ85], the role of Gs is the Eisenstein series EF,1,s.

24

In the degenerate setting of [GZ86], the role of Gs is played by the pair of elliptic modular
forms (E1,s, θ1) viewed as a pair of functions on two copies of H∞ invariant under the action of
a congruence subgroup of GL2(Q × Q).
The modular generating series GD1,D2 is then shown to be equal to the formal q-expansion
of (∆∗G′)hol, the elliptic (holomorphic) modular form obtained by:

i) computing the derivative G′ of Gs at s = 0. This yields a real analytic Hilbert modular form
of parallel weight 1;

ii) pulling back G′ under the diagonal embedding ∆ : H∞ → H2
∞. The resulting diagonal
restriction ∆∗G′ is a real analytic elliptic weight 2 modular form;

iii) applying a holomorphic projection to ∆∗G′.

The resulting holomorphic projection (∆∗G′)hol is ﬁnally shown to equal the modular generat-
ing series GD1,D2.
In §5 the structure of these proofs will be mimicked in the p-adic setting, by replacing CM
cycles with their real quadratic counterparts, and real analytic families with p-adic families of
modular forms.

Remark 8. In [GZ85], the modular generating series GD1,D2 does not appear explicitly. Because
the calculation is carried out for the modular curve of level 1, which has genus 0, such a gen-
erating series is identically zero. The calculation in the analytic proof of loc. cit. amounts to
determining the degree 1 coeﬃcient of the modular generating series as a sum of local contri-
butions, thereby leading to the desired factorisation formula.

Remark 9. Note that in [GZ86], the theta series θ1 appearing as the second component of the
family Gs should be thought of as constant in the variable s. This reﬂects the fact that in the
archimedean setting, only real analytic Eisenstein series admit variations in families. This
imposes some restrictions on the Heegner cycles for which the Gross–Zagier strategy can be
carried out. In general, one would expect the relevant Hilbert family Gs to deform a parallel
weight 1 Hilbert theta series attached to the CM extension L/F. However, these theta series
are usually cuspidal, and as such they do not admit archimedean deformations. By contrast,
in the p-adic setting, cusp forms can often be p-adically deformed. This will allow additional
ﬂexibility in the settings arising in §5.

5 p-adic families of modular forms and RM theory

As we have seen in the last section real analytic families of Eisenstein series play a vital role in
the works of Gross and Zagier on CM theory. In the p-adic setting there is a direct analogue, the
p-adic family of Eisenstein series and below we will review how it is used in RM theory. Before
we go into details we provide a bit of context for the much richer theory of p-adic families of
modular forms.

5.1 A brief overview of p-adic families of modular forms

The theory of p-adic families of modular forms (or more generally of automorphic forms) has
its origins in the 70s when Serre observed that the Hecke eigenvalues of Eisenstein series can

25

be p-adically interpolated and hence that Eisenstein series can be viewed as a p-adic family
parametrised by the weight. This simple yet striking observation combined with a general
interest in establishing congruences of modular forms motivated the search for a theory of
p-adic variations of modular forms.
A p-adic modular form (of level SL2(Z)) as deﬁned by Serre in [Ser73] is a power series f =
∑n≥0 anqn ∈ Qp[[q]] such that there is a sequence of classical modular forms f i = ∑n≥0 ai,nqn that
converges to f (uniformly in the coeﬃcients). There is an alternative geometric deﬁnition due
to Katz [Kat73], which involves the (rigid analytic versions of) modular curves and generalises
the classical deﬁnition of modular forms as sections of certain line bundles.
In a family of p-adic modular forms the weight is one of the crucial p-adically varying
parameters. In fact this parameter can be viewed to vary in the so-called weight space, which is
a rigid analytic space W whose Cp-points are given by

W (Cp) = Homcts(Z×
p , C×
p ) ,

the group of continuous C×
p -valued characters of Z×
p and which identiﬁes with a ﬁnite union of
open unit discs. The weight k ∈ Z of a classical modular form is viewed as a Qp-point of W by
identifying it with the character z ↦→ zk−1, a general p-adic modular form then comes with a
weight κ ∈ W (Cp).
For building a good geometric theory of families the space of p-adic modular forms turns
out to be too big, a problem that both Hida and Coleman managed to overcome using the Hecke
operator Up which acts on the space of p-adic modular forms. In a nutshell, Hida studies
the ordinary subspace, i.e., the subspace of the space of p-adic modular forms on which Up
acts invertibly. Coleman on the other hand works with certain subspaces of the space of p-
adic forms, the so called overconvergent p-adic modular forms. Overconvergence was already
studied by Katz and is an extra condition which decreases the size of these spaces (although
the result is still an inﬁnite-dimensional space). Now, on these spaces of overconvergent forms
the operator Up acts as a compact operator and the complement of the kernel of Up is well
behaved. Coleman managed to use this fact to build p-adic families of modular forms [Col97].
From a geometric point of view the theory for p-adic families of modular forms then cul-
minates in the construction of the so-called eigencurve by Coleman and Mazur ([CM98]). The
eigencurve is a rigid analytic curve C which lives over W and whose points correspond to over-
convergent p-adic modular Hecke eigenforms that are not in the kernel of the Up-operator. The
classical points, i.e., the points corresponding to classical modular forms, form a Zariski-dense
subset of C. The global geometry of the Coleman–Mazur eigencurve remains a fascinating and
challenging subject in current research (see [LTXZ23] for very recent progress on some of the
original questions of Coleman and Mazur).
Let us highlight one important feature of the theory of eigencurves, namely the connection
to the theory of Galois representations. To a classical modular eigenform f one can associate a
2-dimensional Galois representation ρf , which is characterised by identifying the Hecke eigen-
values with traces of Frobenius elements ([Del71], [DS05, Chapter 9]). As it turns out, one can
interpolate these Galois representations (or rather, their traces and determinants) on the eigen-
curve to a family of pseudorepresentations. Moreover the inﬁnitesimal neighbourhood of a
classical point on the eigencurve has an interpretation in terms of a (suitably reﬁned) Galois
deformation space. This allows the usage of tools like Galois cohomology in the study of the
local geometry of the eigencurve.
 26

Since the works of Serre, Katz, Coleman and Mazur, p-adic forms have been introduced
for other reductive groups G over a number ﬁeld F by diﬀerent techniques. In particular the
deﬁnition of overconvergent modular forms has been generalised to the setting of more general
Shimura varieties. Furthermore we have constructions of so-called eigenvarieties generalising
the Coleman–Mazur eigencurve. Let us emphasise (as this is relevant below) that we have a
good theory of p-adic families of Hilbert modular forms at hand.

5.2 A modular generating series for RM values

While a priori singular moduli for real quadratic ﬁelds do not enjoy the same algebraicity prop-
erties as their imaginary quadratic counterparts, they can be packaged into modular generating
series, which one can hope to relate to derivatives of modular forms in the p-adic setting. In
[DPV21], Darmon, Pozzi and Vonk imitate the strategy of [GZ85] outlined in §4.1 by replac-
ing the real analytic family of Hilbert Eisenstein series appearing in (7) with a p-adic family
parametrised by the weight, and relate it to a modular generating series for RM values of theta
cocycles. We will describe their result and compare it with the formalism presented in §4.3.

Let F be a real quadratic ﬁeld of discriminant D, let χ be an odd character of Cl+(OF), and
let p be a prime unramiﬁed in F. Given an odd integer k ∈ Z≥1, consider the parallel weight k
Hilbert Eisenstein series in the variable z = (z1, z2) in H2
∞ with Fourier expansion

E(p)
F,χ,k(z) = L(p)(F, χ, 1 − k) + 4 ∑

ν∈d−1
+
 ∑

n|(νd), p∤Nm(n) χ(n) Nm(n)k−1e2πiTr(ν·z) (9)

where Tr(ν · z) := ν1z1 + ν2z2 for the real embeddings ν1, ν2 of ν ∈ F and

L(p)(F, χ, s) = ∑

n, p∤Nm(n) χ(n)Nm(n)s.

These modular forms are obtained as p-stabilisations of Hilbert modular forms of level SL2(OF)
deﬁned similarly to (6) at primes above p in F. The p-stabilisation procedure allows their
Fourier coeﬃcients to interpolate into continuous functions of the variable k ∈ W , at the cost of
introducing p into the level. This can be veriﬁed directly for the Hecke coeﬃcients attached to
ν ∈ d−1
+ , and can be deduced for the constant term following Serre’s approach to the analyticity
of the Kubota–Leopoldt p-adic ζ-function. We denote the family as EF,χ,k, where the weight k
is thought of as a variable k ∈ W , as explained in §5.1.

Darmon, Pozzi and Vonk translate the steps outlined in §4.3 to the current setting. In
analogy to Gross–Zagier, who consider a family of constant weight 1, it is natural to analyse
the specialisation of the family EF,χ,k at k = 1, in view of applying a derivative. While the
Fourier expansion of (9) may not vanish at k = 1, there is no harm in ﬁrst considering the
pullback of the family EF,χ,k along the diagonal embedding ∆ : H∞ ֒→ H2
∞. For every classical

weight k, the diagonal restriction of the weight k-specialisation E(p)
F,χ,k gives a classical elliptic
modular form of weight 2k, and its Fourier coeﬃcients interpolate p-adically as functions of
k ∈ W . This yields a p-adic family of elliptic modular forms ∆∗EF,χ,k. Its behaviour at k = 1
depends on the splitting of p in F (see [DPV21, Thm. A]).

27

• When p splits in F, the specialisation of ∆∗EF,χ,k need not vanish. The coeﬃcients of
its Fourier expansion can be expressed in terms of intersection pairings of the geodesic
attached to real quadratic points of discriminant D on the modular curve of level Γ0(p)
and the path between (0, ∞) on the modular curve of level Γ0(p).

• When p is inert in F, the specialisation at k = 1 vanishes identically.

The split setting is rather classical in ﬂavour. In the inert setting, the vanishing happens for
similar reasons as in [GZ85], as the weight 1 specialisation of ∆∗EF,χ,k can itself be viewed as
the p-stabilisation of the diagonal restriction of an Eisenstein series of weight 1 and trivial
level, which must be identically 0. In the latter setting, it is tempting to consider the derivative
∆∗E′
F,χ,k of the above family at k = 1. Exploiting the vanishing of ∆∗EF,χ,k at k = 1, one can show
that this derivative is a p-adic (and, in fact, even overconvergent) modular form of weight 2
and trivial tame level [DPV21, Thm. 2.1]. Following the Gross–Zagier strategy, one wishes to
tweak the resulting p-adic modular form and produce a classical one. This can be achieved by
means of Hida’s ordinary projector, constructed by taking limits of suitable iterates of the Up
operator. We denote the resulting modular form by (∆∗E′
F,χ,k)ord. It turns out to be a modular
generating series for the RM values of the winding theta cocycle J(0,∞) at real quadratic points
of discriminant D.

Theorem 5.2.1. [DPV21, Thm. B] Suppose that p is inert in F. The ordinary projection of the
diagonal restriction of E′
F,χ,k is a classical modular form of weight 2 and level Γ0(p) with q-expansion

(∆∗E′
F,χ,k)ord = L′
p(F, χ, 0) + ∑

n≥1 qn ∑

[τ], discτ=D χ(cτ) logp
 (
NmQp2
Qp (TnJ(0,∞))[τ])

where the sum runs over SL2(Z)-classes of points of discriminant D, cτ denotes the fractional ideal
Z + τZ if τ − τ′ > 0 and √
D(Z + τZ) otherwise, and Qp2 is the unique unramiﬁed quadratic extension
of Qp.

Note that the points τ in the above sum belong to Hp precisely because p is inert in F.
Unlike in Thm. 4.1.2, the constructed modular form has no a priori reason to vanish since it
has level Γ0(p).

Remark 10. The modular form in Theorem 5.2.1 is in general non-zero. Its constant coeﬃcient
is the leading term of a p-adic L-function which can be expressed as the p-adic logarithm of a
certain global units, which will be the subject of Theorem 5.3.1.

Remark 11. The values J(0,∞)[τ] of the winding theta cocycle at RM points τ in Hp should
be thought of as multiplicative analogues of the diﬀerences of singular moduli j (τ1) − j (τ2)
appearing in Gross–Zagier [GZ85], where the pair (0, ∞) corresponds to the split quadratic
form Q(0,∞)(X, Y ) = XY . However, this setting is degenerate, because the solutions to Q(0,∞) lie
at the boundary of the p-adic upper half plane. In particular, the corresponding theta cocycle
is not expected to have algebraic values at real quadratic points in general. In the general
framework described in §4.3, this setting should correspond to the diagram of biquadratic Q-
algebras of the form
 28

Q

F Q × Q

F × F

F

where the leftmost and rightmost algebras in the middle row correspond to quadratic forms of
discriminant D and Q(0,∞), respectively. The analogy with the settings of Gross–Zagier [GZ85]
and [GZ86] is imperfect: in their work the archimedean place does not split in the quadratic
ﬁelds K1 and K2. By contrast, in the setting of [DPV21] the prime p splits in the algebra Q × Q.
This is related to the fact that the Eisenstein series appearing in [DPV21] is attached to an ar-
bitrary totally odd character of the class group Cl+(OF), while in [GZ85] only genus characters
are considered.

5.3 The values of the Dedekind–Rademacher theta cocycle

In the archimedean setting, we discussed how modular generating series for Heegner cycles
on the Jacobian of modular curves can be leveraged into arithmetic applications for the Heeg-
ner constructions discussed in §2. Particularly, the main result in [GZ85] towards the Birch
and Swinnerton-Dyer Conjecture is obtained by projecting a suitable modular generating se-
ries into the f -isotypic component for a newform f corresponding to an elliptic curve via the
Eichler–Shimura construction.
Similarly, we will now discuss an arithmetic application of the ideas appearing in §5.2 to
the algebraicity of the RM values of the Dedekind–Rademacher theta cocycle JDR deﬁned in
§3.4. The values of the Dedekind–Rademacher cocycle at real multiplication points should be
thought of as real quadratic analogues of the elliptic units, in light of Conjecture 2. The co-
cycle JDR is the Eisenstein class in the module of analytic theta cocycles H 1(Γ, A×/C×
p ), as its
deﬁnition involves the periods of the weight 2 Eisenstein series of level Γ0(p). Accordingly, the
main result of [DPV23] is obtained by projecting a suitable modular generating series similar
to the one appearing in Theorem 5.2.1 onto its Eisenstein subspace.
However, a signiﬁcant new element occurs in this setting that does not have an archime-
dean counterpart. The modular generating series in question is obtained by considering the
derivative of a p-adic family of cusp forms deforming over an appropriate weight space for
Hilbert modular forms for a real quadratic ﬁeld F. The coeﬃcients of its derivative are richer
than those of Eisenstein series and encode information about the arithmetic of the Hilbert class
ﬁeld of F.
The main result [DPV23] can be formulated as follows.

Theorem 5.3.1. Let D > 0 be a fundamental discriminant, and let p ∤ D be a prime number. Let
τ ∈ Hp be a point of discriminant D. Let F = Q(τ) and let H be the narrow Hilbert class ﬁeld of F.
The values of the Dedekind–Rademacher cocycle at τ satisfy

JDR[τ] = u12
τ modulo (pZ × roots of unity in Q×
p2)

for an element uτ ∈ OH [1/p]× ⊗ Q.
 29

Prior to this work, the equality of local norms

NmQ2
p
Qp (JDR(τ))   NmQ2
p
Qp (u12
τ ) (10)

up to p-powers and roots of unity in Qp2 was already known, as both sides of (10) had been
related to the derivative of a p-adic L-function (for a deﬁnition, see [DD06, §4]). More pre-
cisely, Thm. 4.1 in loc. cit. relates the derivative of this p-adic L-function to the norm of the RM
values of the Dedekind–Rademacher cocycle. On the other hand, the p-unit uτ is an example
of the Gross–Stark units, appearing in the conjectures of Stark and Gross about derivatives of
Artin L-functions and their p-adic analogues. In particular, the formula for the derivative of
the p-adic zeta function above and the norm of the p-unit uτ was proved by Darmon, Dasgupta
and Pollack in their work on the Gross–Stark Conjecture.
The main contribution of the reﬁnement of (10) in Theorem 5.3.1 is proving the algebraicity of
the RM values of the Dedekind–Rademacher cocycle itself, for which the equality up to local
norms would not suﬃce. This establishes cases of Conjecture 2, providing theoretical evidence
in favour of pursuing a theory of real multiplication via p-adic methods.

Remark 12. The unit uτ in the statement of Thm. 5.3.1 can be characterised more precisely.
It is trivial if F has a unit of negative norm, or equivalently, if the narrow class ﬁeld of H is
totally real. Otherwise, it is a non-trivial element in the subspace of OH [1/p]× ⊗ Q on which the
complex conjugation in H acts as −1. The recent breakthroughs of Dasgupta and Kakde on the
Brumer–Stark Conjecture imply that this unit in fact lies in OH [1/p]× ⊗ Z[1/2].

The crucial intuition behind the strategy in [DPV23] is that removing the norm in (10)
could be achieved by removing the norms in the modular generating series in Theorem 5.2.1
obtained from the derivative of the p-adic family of Eisenstein series. This approach requires
ﬁnding a suitable family of p-adic modular forms and exploiting its derivatives to produce the
desired modular generating series.
Fortunately, the setting allows a lot of ﬂexibility due to a lucky coincidence. The weight 1
Eisenstein series E(p)
F,χ,1 considered in (9) happens to be cuspidal when viewed as an overcon-
vergent p-adic Hilbert modular form. In fact, it is an example of a critical p-stabilisation of
a classical Eisenstein series (considered, for example by Bellaiche and Chenevier for elliptic
modular forms [BC06]). As such, it deﬁnes a point on the eigenvariety parametrising p-adic
families of Hilbert cusp forms for F. Unlike Eisenstein series, which only vary in parallel
weight, Hilbert families of cusp forms range over a larger weight space parametrising pairs of
weights (k1, k2).
Cuspidal variations of Hilbert modular forms are, in general, entirely inexplicit. However,
their attached Galois representations provide a useful tool to tackle a local description. In
particular, they can be exploited to entirely determine the Fourier expansion of the derivative
of a family Fk,2−k specialising to E(p)
F,χ,1 at k = 1, in the antiparallel direction of weights (k1, k2)
satisfying k1 +k2 = 2. The diagonal restriction of the derivative Fk,2−k with respect to k, denoted
by ∆∗F ′, is again an overconvergent p-adic modular form. Its ordinary projection (∆∗F ′)ord,
(up to an explicit correction term obtained from the diagonal restriction of explicit Eisenstein
series) yields the following theorem, which is the key stepping towards Thm. 5.3.1.

30

Theorem 5.3.2. [DPV23, Thm. C] There is a classical modular form of weight 2 and level Γ0(p) with
q-expansion logp(uτ) + ∑

n≥1 logp(TnJ(0,∞)[τ])qn,

for a unit uτ ∈ OH [1/p]× ⊗ Q.

From this result, the relation between the unit uτ and the RM values of the Dedekind-
Rademacher cocycle can easily be deduced by decomposing the winding cocycle J(0,∞) with
respect to an eigenbasis of the space of analytic theta cocycles, and in particular determining
its projection onto the Eisenstein eigenspace spanned by JDR.

Remark 13. The relevance of cuspidal deformations of the Eisenstein series E(p)
F,χ,1 towards Thm.
5.3.1 should not be surprising. A cuspidal variation of this Eisenstein series in the parallel
weight direction played a crucial role in the proof of the Gross–Stark Conjecture in [DDP11]
implying the equality (10). This ﬁts into a general theme relating congruences between cusp
forms and Eisenstein series to L-functions, initiated by Ribet in [Rib76] and often referred to
as Ribet’s method. Theorem 5.3.1 is a special case of a far more general result of Dasgupta and
Kakde [DK21], providing explicit p-adic formulae for units in abelian extensions of totally real
ﬁelds. Their result can be seen as the culmination of a program of Dasgupta and collaborators
settling Hilbert’s Twelfth problem for totally real ﬁelds via p-adic methods. Their approach
makes use of generalisations of Ribet’s method. However, unlike in [DPV23], the strategy is
applied to variations of Hilbert modular forms over ﬁnite group rings, rather than over a p-adic
weight space.

References

[BC06] J. Bellaïche and G. Chenevier. Lissité de la courbe de Hecke de GL2 aux points
Eisenstein critiques. J. Inst. Math. Jussieu, 5(2):333–349, 2006.

[BCDT01] Christophe Breuil, Brian Conrad, Fred Diamond, and Richard Taylor. On the modu-
larity of elliptic curves over Q: wild 3-adic exercises. J. Amer. Math. Soc., 14(4):843–
939, 2001.

[BD09] Massimo Bertolini and Henri Darmon. The rationality of Stark-Heegner points over
genus ﬁelds of real quadratic ﬁelds. Ann. Math. (2), 170(1):343–369, 2009.

[Bos14] Siegfried Bosch. Lectures on formal and rigid geometry, volume 2105 of Lect. Notes
Math. Cham: Springer, 2014.

[CM98] R. Coleman and B. Mazur. The eigencurve. In Galois representations in arithmetic
algebraic geometry. Proceedings of the symposium, Durham, UK, July 9–18, 1996, pages
1–113. Cambridge: Cambridge University Press, 1998.

[Col97] Robert F. Coleman. p-adic Banach spaces and families of modular forms. Invent.
Math., 127(3):417–479, 1997.
 31

[Con08] Brian Conrad. Several approaches to non-archimedean geometry. In p-adic geome-
try. Lectures from the 2007 10th Arizona winter school, Tucson, AZ, USA, March 10–14,
2007, pages 9–63. Providence, RI: American Mathematical Society (AMS), 2008.

[Cox89] David A. Cox. Primes of the form x2 + ny2. Fermat, class ﬁeld theory and complex
multiplication. New York etc.: John Wiley &| Sons, 1989.

[Dar01] Henri Darmon. Integration on Hp × H and arithmetic applications. Ann. Math. (2),
154(3):589–639, 2001.

[DD06] Henri Darmon and Samit Dasgupta. Elliptic units for real quadratic ﬁelds. Ann.
Math. (2), 163(1):301–346, 2006.

[DDP11] Samit Dasgupta, Henri Darmon, and Robert Pollack. Hilbert modular forms and
the Gross-Stark conjecture. Ann. of Math. (2), 174(1):439–484, 2011.

[DDT97] Henri Darmon, Fred Diamond, and Richard Taylor. Fermat’s last theorem. In El-
liptic curves, modular forms & Fermat’s last theorem (Hong Kong, 1993), pages 2–140.
Int. Press, Cambridge, MA, 1997.

[Del71] Pierre Deligne. Modular forms and ℓ-adic representations. Sémin. Bourbaki
1968/69, No. 355, Lect. Notes Math. 179, 139-172 (1971)., 1971.

[DK21] Samit Dasgupta and Mahesh Kakde. Brumer–Stark units and Hilbert’s 12th prob-
lem. arxiv.2103.02516, 2021.

[DP06] Henri Darmon and Robert Pollack. Eﬃcient calculation of Stark-Heegner points via
overconvergent modular symbols. Isr. J. Math., 153:319–354, 2006.

[DPV21] Henri Darmon, Alice Pozzi, and Jan Vonk. Diagonal restrictions of p-adic Eisenstein
families. Math. Ann., 379(1-2):503–548, 2021.

[DPV23] Henri Darmon, Alice Pozzi, and Jan Vonk. The values of the Dedekind–Rademacher
cocycle at real multiplication points. J. Eur. Math. Soc., 2023.

[DS05] Fred Diamond and Jerry Shurman. A ﬁrst course in modular forms, volume 228 of
Grad. Texts Math. Berlin: Springer, 2005.

[DT08] Samit Dasgupta and Jeremy Teitelbaum. The p-adic upper half plane. In p-adic
geometry, volume 45 of Univ. Lecture Ser., pages 65–121. Amer. Math. Soc., Provi-
dence, RI, 2008.

[DV21] Henri Darmon and Jan Vonk. Singular moduli for real quadratic ﬁelds: a rigid
analytic approach. Duke Math. J., 170(1):23–93, 2021.

[DV22] Henri Darmon and Jan Vonk. Real quadratic Borcherds products. Pure Appl. Math.
Q., 18(5):1803–1865, 2022.

[GZ85] Benedict H. Gross and Don B. Zagier. On singular moduli. J. Reine Angew. Math.,
355:191–220, 1985.
 32

[GZ86] Benedict Gross and Don Zagier. Heegner points and derivatives of l-series. Invent.
math, 84:225–320, 1986.

[Kat73] Nicholas M. Katz. p-adic properties of modular schemes and modular forms. Mod-
ular Functions of one Variable III, Proc. internat. Summer School, Univ. Antwerp
1972, Lect. Notes Math. 350, 69-190 (1973)., 1973.

[KL81] Daniel S. Kubert and S. Lang. Modular Units. Grundlehren der mathematischen
Wissenschaften. Springer Verlag, 1981.

[Kol89] V. A. Kolyvagin. Finiteness of E(Q) and X(E, Q) for a subclass of Weil curves. Math.
USSR, Izv., 32(3):523–541, 1989.

[LTXZ23] Ruochuan Liu, Nha Xuan Truong, Liang Xiao Xiao, and Bin Zhao. Slopes of modular
forms and geomtry of eigencurves. arxiv.2302.07697, 2023.

[Rib76] Kenneth A. Ribet. A modular construction of unramiﬁed p-extensions of Q(µp).
Invent. Math., 34(3):151–162, 1976.

[Ser73] Jean-Pierre Serre. Formes modulaires et fonctions zêta p-adiques. In Willem Kuijk
and Jean-Pierre Serre, editors, Modular Functions of One Variable III, pages 191–268,
Berlin, Heidelberg, 1973. Springer Berlin Heidelberg.

[Sie69] Carl Ludwig Siegel. Berechnung von Zetafunktionen an ganzzahligen Stellen.
Nachr. Akad. Wiss. Gött., II. Math.-Phys. Kl., 1969:87–102, 1969.

[Sil94] Joseph H. Silverman. Advanced topics in the arithmetic of elliptic curves, volume 151
of Graduate Texts in Mathematics. Springer-Verlag, New York, 1994.

[Stu80] Jacob Sturm. Projections of C∞-automorphic forms. Bull. Am. Math. Soc., New Ser.,
2:435–439, 1980.

[TW95] Richard Taylor and Andrew Wiles. Ring-theoretic properties of certain Hecke alge-
bras. Ann. Math. (2), 141(3):553–572, 1995.

[Wil95] Andrew Wiles. Modular elliptic curves and Fermat’s Last Theorem. Ann. Math. (2),
141(3):443–551, 1995.
 33
