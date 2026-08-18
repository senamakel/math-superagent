<!-- source: https://arxiv.org/pdf/1912.12536 | converted from PDF -->

arXiv:1912.12536v1  [math.AG]  28 Dec 2019
MODULAR FUNCTIONS AND RESOLVENT PROBLEMS

BENSON FARB, MARK KISIN AND JESSE WOLFSON

WITH AN APPENDIX BY NATE HARMAN

Abstract. The link between modular functions and algebraic functions was
a driving force behind the 19th century study of both. Examples include the
solutions by Hermite and Klein of the quintic via elliptic modular functions and
the general sextic via level 2 hyperelliptic functions. This paper aims to apply
modern arithmetic techniques to the circle of “resolvent problems” formulated
and pursued by Klein, Hilbert and others. As one example, we prove that
the essential dimension at p = 2 for the symmetric groups Sn is equal to the
essential dimension at 2 of certain Sn-coverings deﬁned using moduli spaces of
principally polarized abelian varieties. Our proofs use the deformation theory
of abelian varieties in characteristic p, speciﬁcally Serre-Tate theory, as well
as a family of remarkable mod 2 symplectic Sn-representations constructed by
Jordan. As shown in an appendix by Nate Harman, the properties we need
for such representations exist only in the p = 2 case.
In the second half of this paper we introduce the notion of E-versality as a
kind of generalization of Kummer theory, and we prove that many congruence
covers are E-versal. We use these E-versality result to deduce the equivalence
of Hilbert’s 13th Problem (and related conjectures) with problems about con-
gruence covers.
 Contents

1. Introduction 2
2. Moduli of Abelian varieties 5
2.1. Extension classes 5
2.2. Monodromy on the ordinary locus 6
2.3. Essential dimension 8
3. Modular symplectic representations of ﬁnite groups 10
3.1. General Finite Groups 10
3.2. The Groups Sn and An 11
3.3. Finite groups of Lie type 13
4. Classical Problems and Congruence Covers 13
4.1. Accessory Irrationalities and E-Versality 14
4.2. E-Versal Congruence Covers 17
Appendix A. On quadratic representations of Sn 24
A.1. Statement of Results 24
A.2. Proofs of Main Theorems 26
A.3. Modiﬁcations for An 30
References 31

The authors are partially supported by NSF grants DMS-1811772 and Jump Trading Mathlab
Research Fund (BF), DMS-1601054 (MK) and DMS-1811846 (JW).

1

2 BENSON FARB, MARK KISIN AND JESSE WOLFSON

1. Introduction

The link between modular functions and algebraic functions was a driving force
behind the 19th century development of both. Examples include the solutions by
Hermite and Klein of the quintic via elliptic modular functions, degree 7 and 8
equations with Galois group PSL2(F7) via the level the level 7 modular curve, the
general sextic via level 2 hyperelliptic functions, the 27 lines on smooth cubic sur-
faces via level 3, dimension 2 abelian functions, and the 28 bitangents on a smooth
quartic via level 2, dimension 3 abelian functions.1 With the Nazi destruction of
the G¨ottingen research community this connection was largely abandoned, and the
study of algebraic functions and resolvent problems, as pioneered by Klein, Hilbert
and others, fell into relative obscurity. The purpose of this paper to reconsider the
link between modular functions and classical resolvent problems. We do this from
a modern viewpoint, using arithmetic techniques.

Essential dimension at p of modular functions. To ﬁx ideas we work over
C. Recall that an algebraic function is a ﬁnite correspondence X 99K
1:n P1; that is, a
rational function f : ˜X 99K P1 on some (ﬁnite, possibly branched) cover ˜X → X. 2

A fundamental example is the general degree n polynomial, equivalently the cover

M0,n → M0,n/Sn,

where M0,n denotes the moduli space of n distinct marked points in P1. When X
is a locally symmetric variety f is called a modular function. A basic example is
the cover Ag,N → Ag where Ag is the (coarse) moduli space of principally polarized
g-dimensional abelian varieties and Ag,N is the moduli of pairs (A, B) with A ∈ Ag
and B a symplectic basis for H1(A; Z/N Z).
The relationship between modular functions and the solutions of the general de-
gree n polynomial motivated Klein [Kl1884,Kl1888], Kronecker [Kr1861] and others
to ask about the intrinsic complexity of these algebraic functions, as measured by
the number of variables to which they can be reduced after a rational change of
variables. In modern terms (as deﬁned by Buhler-Reichstein, see e.g. [Rei10]), the
essential dimension ed( ˜X/X) ≤ dim(X) of an algebraic function is the smallest
d ≥ 1 so that ˜X → X is the birational pullback of a cover ˜Y → Y of d-dimensional
varieties.
One can also allow, in addition to rational changes of coordinates, the adjunction
of radicals or other algebraic functions. This is done by specifying a class E of covers
under which ˜X → X can be pulled back before taking ed of the resulting cover.
This gives the essential dimension ed( ˜X/X; E) relative to the class E of “accesory
irrationalities”. For example, if one ﬁxes a prime p and pulls back by covers of
degree prime to p, one obtains the notion of essential dimension at p, denoted
ed( ˜X/X; p) (see e.g. [RY00]). The idea of accessory irrationality was central to the
approaches of Klein and Hilbert to solving equations. We axiomatize this notion in
Deﬁnition 4.1.3 below and explore its consequences in Section 4.
The general degree n polynomial is universal for covers with Galois group Sn,
even allowing prime-to-p accessory irrationalities; that is, for all p ≥ 2 and for

1See e.g. [Kl1879, Kl1884, Kl1888, Bu1890, Bu1891, Bu1893, KF1892, FK12, Fri26], as well as
[Kle22a, Kle22b].
2When the functions are understood, we denote an algebraic function simply by the cover
˜X → X.
 MODULAR FUNCTIONS AND RESOLVENT PROBLEMS 3

ed(Sn; p) deﬁned as the maximum of ed( ˜X/X; p) for all Sn-covers ˜X → X, we
have: ed(M0,n/M0,n; p) = ed(Sn; p).
With the many examples relating the general degree n polynomial to modular
functions, it is natural to ask if the same “maximal complexity property” holds for
modular functions. Our ﬁrst result states that for p = 2 this is indeed the case. To
explain this, for a subgroup G ⊂ Sp2g(Z/N Z) set Ag,G := Ag,N /G.

Theorem 1. Let n ≥ 2, g = ⌈ n
2 ⌉ − 1, and let N ≥ 3 be odd. There exists an
embedding Sn ⊂ Sp2g(F2) ⊂ Sp2g(Z/2N Z) such that

ed(Ag,2N /Ag,Sn ; 2) = ⌊n/2⌋ = ed(Sn; 2).

We remark that what we actually prove is the ﬁrst equality. The second equality
then follows from a result of Meyer-Reichstein [MR09, Corollary 4.2]. In particular,
one sees from their result that ed(Sn; p) takes its maximal value for p = 2, so this
case is, in some sense, the most interesting.
One ingredient in the proof of Theorem 1 comes from the link between binary
forms and hyperelliptic functions; speciﬁcally, Jordan proved that the monodromy
of the 2-torsion points on the universal hyperelliptic Jacobian gives a mod 2 sym-
plectic Sn-representation. These remarkable representations were rediscovered and
studied by Dickson [Dic08] in 1908. We deduce Theorem 1 by applying the following
general result to these representations.

Theorem 2. Let G be a ﬁnite group, and G → Sp2g(Fp) a representation. If
U ⊂ Sp2g is the unipotent of a Siegel parabolic then

ed(Ag,pN /Ag,G; p) ≥ dimFp G ∩ U (Fp)

Theorem 2 is of most interest for those G which admit a symplectic representation
with dimFp G ∩ U (Fp) = ed(G; p), where ed(G; p) is the essential dimension at p of
a versal branched cover with group G (see Deﬁnition 4.1.6 below). For G = Sn, a
result of Harman (Theorems A.1 and A.2) says that this is possible only for p = 2,
and only using the particular mod 2 symplectic representation of Jordan/Dickson!
We also show that for G the Fq-points of a split semisimple group of classical type,
there is a symplectic representation of G for which the lower bound in Theorem 2 is
either equal or nearly equal to the maximal rank of an elementary abelian p-group
in G. The only near-misses occur for odd orthogonal groups. Note however, that
this rank is in general less than ed(G; p).

E-versal modular functions. Kummer theory gives that for each d ≥ 2 the cover
P1 → P1/(Z/dZ) has the following universal property: any Z/dZ cover ˜X → X
is pulled back from it. It follows that ed( ˜X/X; p) = 1 for any such ˜X → X.
Klein’s Normalformsatz states that, while the icosahedral cover P1 → P1/A5 is not
universal in the above sense (indeed ed(M0,5 → M0,5/A5) = 2), there exists a
Z/2Z accessory irrationality ˜Y → ˜X
↓ ↓
Y → X

such that ˜Y → Y is a pullback of P1 → P1/A5. This nonabelian version of Kum-
mer’s theorem is a kind of classiﬁcation of actions of A5 on all varieties. We say
in this case that P1 → P1/A5 is E-versal with respect to any collection E of covers

4 BENSON FARB, MARK KISIN AND JESSE WOLFSON

containing Z/2Z covers. Note that this cover is modular; indeed it is equivariantly
birational to the cover H2/Γ2(5) → H2/SL2(Z), where H2 is the hyperbolic plane
and Γ2(5) is the level 5 congruence subgroup of SL2(Z); here we are using the
natural isomorphism PSL2(F5) ∼= A5.
In §4 we axiomatize the idea of E-versality and we give a number of examples
(most classically known) of congruence covers that are E-versal for various groups
G. One sample result on E-versality is the following (see §4.2 for terminology). For
Γ < SL2(R) × SL2(R) a lattice, let MΓ : (H2 × H2)/Γ; these are complex-algebraic
varieties called Hilbert modular surfaces.

Proposition 3. For E any class of accessory irrationalities containing all quadratic
and cubic covers and composites thereof, the Hilbert modular surface

M ̃
SL2(Z[ 1+√5
2 ],3) → MSL2(Z[ 1+√5
2 ])

is E-versal for A6, where ̃
SL2(Z[ 1+√5
2 ], 3) denotes the kernel of the map

SL2(Z[ 1 + √
5
2 ]) → PGL2(F9) ∼= A6.

In particular, Hilbert’s Sextic Conjecture is equivalent to the statement that the
resolvent degree of this cover equals 2.

The connection between these E-versality results with the ﬁrst part of this paper
is that E-versal G-covers always maximize ed( ˜X/X; E) over all G-covers ˜X → X.
In §4 we apply such E-versality results to exhibit further the close relationship
between modular functions and roots of polynomials. Speciﬁcally, Hilbert’s 13th
Problem, and his Sextic and Octic Conjectures (see §4 for their exact statements)
are phrased in terms of the resolvent degree of the degree 6, 7 and 8 polynomials.
The resolvent degree RD( ˜X/X) is the smallest d such that ˜X → X is covered by a
composite of covers, each of essential dimension ≤ d (see e.g. [AS76,Bra75,FW18]).
Applying various E-versality results, we deduce in §4 the equivalence of each of
Hilbert’s conjectures with a conjecture about the resolvent degree of a speciﬁc
modular cover. Similarly, we show that such a modular reformulation is possible
not only for general polynomials of low degree, but also for each of the algebraic
functions considered by Klein and his school [Kl1871, Kl1888, Kle26, Fri26].

Methods. The proof of Theorem 2 uses a reﬁnement of the results of [FKW19],
which is explained in §1. In loc. cit, we used Serre-Tate theory to give lower bounds
on the essential at p for the coverings Ag,pN → Ag,N , when restricted to (some)
subvarieties Z ⊂ Ag,N . Here we drop the assumption that Z is a subvariety and
allow certain maps Z → Ag,N (cf. Proposition 2.3.5). In particular, we can apply
the resulting estimate to Z = Ag,G for G a subgroup of Sp2g(Fp), which yields the
lower bound for ed(Ag,pN /Ag,G; p) in Theorem 2.
One may compare the bounds given by Theorem 2 to those obtained in [FKW19,
§4] for certain ﬁnite simple groups of Lie type. The bound in the case of odd
orthogonal groups in loc. cit is weaker than the one given here because of the
restriction on the signature of Hermitian symmetric domains associated to odd
orthogonal groups. On the other hand the coverings we consider here correspond
to rather more exotic congruence subgroups than those of loc. cit.

MODULAR FUNCTIONS AND RESOLVENT PROBLEMS 5

Acknowledgements. The authors would like to thank Robert Guralnick for point-
ing out a mistake in an earlier version of this paper. We also thank Igor Dolgachev,
Bert van Geemen, Bruce Hunt, Aaron Landesman, Zinovy Reichstein and Ron
Solomon for helpful correspondence.

2. Moduli of Abelian varieties

2.1. Extension classes.

2.1.1. Fix a prime p, and let V be a complete discrete valuation ring of charac-
teristic 0, with perfect residue ﬁeld k of characteristic p, and a uniformizer π ∈ V.
Let A = V [[x1, . . . , xn]] be a power series ring over V. We denote by mA ⊂ A the
maximal ideal, and ¯mA = mA/πA. and set ˜X = Spec A, and X = Spec A[1/p]. We
will denote by k[ǫ] = k[X]/X 2 the dual numbers over k.
Recall [FKW19, 3.1.2] that there is a commutative diagram

A
×/(A
×)
p ∼ //

  
 Ext
1
˜X (Z/pZ, µp)

  
A[1/p]×/(A[1/p]×)
p ∼ // Ext
1
X (Z/pZ, µp)

where the terms on the right are extensions as Z/pZ-sheaves. The vertical maps
are injective, and the extensions in the image of the map on the right are called
syntomic. There is also a map [FKW19, 3.1.5]

θA : Ext
1
˜X (Z/pZ, µp) ∼
−→ A
×/(A
×)
p → ¯mA/ ¯m2
A.

which sends a class represented by a function f ∈ 1 + mA to f − 1.

Lemma 2.1.2. Let U ⊂ Ext
1
˜X (Z/pZ, µp) be an Fp-subspace of dimension ≤ n.
Suppose that for every map h : A → k[ǫ] the image of U under the induced map

(2.1.2.1) Ext
1
˜X (Z/pZ, µp) → Ext
1
Spec k[ǫ](Z/pZ, µp)

is nontrivial. Then the map

(2.1.2.2) θA : U ⊗Fp k → ¯mA/ ¯m2
A
is an isomorphism; in particular dimFp U = n.

Proof. Since the image of U under 2.1.2.1 is nontrivial, the composite

θA : U ⊗Fp k → ¯mA/ ¯m2
A → ǫ · k

is nontrivial for every h. This implies that 2.1.2.2 is surjective, and since dimFp U ≤
n it is injective, and dimFp U = n. □

2.1.3. We call a subspace U ⊂ Ext
1
˜X (Z/pZ, µp) satisfying the conditions of
Lemma 2.1.2 nondegenerate, and we ﬁx such a subspace. Now assume that V
contains a primitive pth root of unity, and ﬁx a geometric point ¯x of X. Then

Ext
1
X (Z/pZ, µp) ∼
−→ H 1(X, µp) = H 1
´et(X, µp) = Hom(π1(X, ¯x), µp).

If U ′ ⊂ U is a subspace, denote by X(U ′) → X the ﬁnite ´etale cover corresponding
to U ′. That is, X(U ′) is the cover corresponding to the intersection of all the
elements of Hom(π1(X, ¯x), µp) that are images of elements of U ′. We let ˜X ′ =
Spec A(U ′) denote the normalization of ˜X in X(U ′).

6 BENSON FARB, MARK KISIN AND JESSE WOLFSON

Lemma 2.1.4. For any U ′ ⊂ U the ring A(U ′) is a power series ring over V.
Further,

(2.1.4.1) dimk Im( ¯mA/ ¯m2
A → ¯mA(U ′)/m2
A(U ′)) = dimFp (U /U ′).

Proof. Let f1, . . . , fr ∈ A
× be elements with 1 − fi ∈ mA, and such that the
images of f1, . . . , fr in Ext
1
˜X (Z/pZ, µp) form an Fp-basis for U ′. By deﬁnition,
X(U ′) = Spec A[1/p]( p√
f1, . . . , p√
fr). To prove the ﬁrst claim, it suﬃces to show
that
 A( p√
f1, . . . , p√
fr) = A[z1, . . . , zr]/(zp
i − fi)

is a power series ring over V. Since U is nondegenerate, the images of f1, . . . , fr
are k-linearly independent in mA/m2
A. Hence, after a change of coordinates, we can
assume that A ∼
−→ V [[x1, . . . , xn]] with xi = fi − 1 for i = 1, . . . r. Then we have

A[z1, . . . , zr]/(zp
i − fi) ∼
−→ V [[z1 − 1, . . . , zr − 1, xr+1, . . . , xn]].

This also shows 2.1.4.1, as both sides are equal to n − r. □

2.2. Monodromy on the ordinary locus.

2.2.1. Fix an integer g ≥ 1, a prime p ≥ 2, and a positive integer N ≥ 2 coprime
to p. Consider the ring Z[ζN ][1/N ], where ζN is a primitive N th root of 1. Denote
by Ag,N the Z[ζN ][1/N ]-scheme which is the coarse moduli space of principally
polarized abelian schemes A of dimension g equipped with a basis of A[N ] that is
symplectic with respect to the Weil pairing deﬁned by ζN . When N ≥ 3, this is a
ﬁne moduli space which is smooth over Z[ζN ][1/N ]. For a Z[ζN ][1/N ]-algebra B,
denote by Ag,N/B the base change of Ag,N to B. If no confusion is likely to result,
we sometimes denote this base change simply by Ag,N .
From now on, unless stated otherwise, we assume that N ≥ 3 and we let A →
Ag,N be the universal abelian scheme. The p-torsion subgroup A[p] ⊂ A is a ﬁnite
ﬂat group scheme over Ag,N which is ´etale over Z[ζN ][1/N p]. Let x ∈ Ag,N be a
point with residue ﬁeld κ(x) of characteristic p, and Ax the corresponding abelian
variety over κ(x).
The set of points x such that Ax is ordinary is an open subscheme A
ord
g,N ⊂
Ag,N ⊗ Fp. We denote by ̂A
ord
g,N the formal completion of Ag,N along A
ord
g,N . We
denote by A
ord,an
g,N the “generic ﬁbre” of ̂A
ord
g,N as a p-adic analytic space.3

Denote by k an algebraically closed perfect ﬁeld of characteristic p, and let
K/W [1/p] be a ﬁnite extension with ring of integers OK and uniformizer π. Assume
that K is equipped with a choice of primitive N th root of 1, ζN ∈ K, so that we
may consider all the objects introduced above over OK. Let ¯K/K be an algebraic
closure.

Proposition 2.2.2. Fix a geometric point x ∈ ̂A
ord,an
g,N ( ¯K) and denote by ¯x ∈ A
ord
g,N
its reduction.The covering Ag,pN → Ag,N corresponds to a surjective representation

(2.2.2.1) π1(Ag,N , x) → Sp2g(Fp).

3The reader may think of any version of the theory of p-adic analytic spaces they prefer (Tate,
Raynaud, Berkovich, or H¨uber’s adic spaces), as this will have no bearing on our arguments.

MODULAR FUNCTIONS AND RESOLVENT PROBLEMS 7

(1) There exists a Siegel parabolic P ⊂ Sp2g /Fp with unipotent radical U, such
that 2.2.2.1 induces a surjective representation

(2.2.2.2) π1( ̂A
ord,an
g,N , x) → P (Fp).

(2) Let A = ̂OAg,N ,¯x be the completion of the local ring at ¯x. Then (2.2.2.1)
induces a surjective representation

(2.2.2.3) π1(Spec A[1/p], x) → U (Fp).

Proof. The ﬁrst claim is well known. Indeed, the existence of the Weil pairing on
A[p] implies that Ag,pN corresponds to a symplectic representation. A comparison
with the topological fundamental group shows that the image of the geometric
fundamental group π1(Ag,N ⊗K ¯K, x) is Sp2g(Fp), so the representation is surjective.
Now recall, that a Siegel parabolic is the stabilizer of a maximal isotropic subspace
in the underlying vector space of a symplectic representation. Equivalently it is a
parabolic with abelian unipotent radical. All such parabolics are conjugate. Over
̂A
ord
g,N the ﬁnite ﬂat group scheme A[p] is an extension

(2.2.2.4) 0 → A[p]m → A[p] → A[p]
´et → 0

of an ´etale by a multiplicative group scheme, where ´etale locally A[p]
´et ∼
−→ (Z/pZ)
g

and A[p]m ∼
−→ µg
p. The Weil pairing induces a map of group schemes

A[p] × A[p] → µp.

which identiﬁes A[p] with its Cartier dual, and induces an isomorphism A[p]m with
the Cartier dual of A[p]
´et. In particular, this shows that A[p]m
x ⊂ A[p]x corresponds
to a maximal isotropic subspace under the Weil pairing. This deﬁnes a Siegel
parabolic such that (2.2.2.1) maps π1( ̂A
ord,an
g,N , x) into P (Fp). By [FC90, Prop. 7.2]
the image of the composite

π1( ̂A
ord,an
g,N , x) → P (Fp) → (P/U )(Fp)

is surjective. Hence it suﬃces to prove (2).
For this, we adopt the notation of 2.1 applied with A as in (2). Since we are
assuming k is algebraically closed, over A, the group schemes A[p]
´et and A[p]m are
isomorphic to (Z/pZ)
g and µg
p respectively. In particular, the map (2.2.2.3) factors
through U (Fp). Let U ⊂ Ext
1
X (Z/pZ, µp) be the span of the g2 syntomic extension
classes deﬁning the extension (2.2.2.4). Note that U (Fp) is an elementary abelian
p-group of rank n = dimFp U = dim Ag = (
g+1
2 )
. Any Fp-linear map s : U (Fp) → Fp
induces a representation

π1(Spec A[1/p], x) → µp( ¯K) ∼
−→ Fp

(choosing pth root of unity), and hence a class in

c(s) ∈ Ext
1
X (Z/pZ, µp) ∼
−→ H 1(X, Fp).

The subspace U is the span of all the classes c(s). This shows dim U ≤ n, with
equality only if (2.2.2.3) is surjective. However, by [FKW19, 3.2.2], one sees that
U satisﬁes the conditions of Lemma 2.1.2, so that dim U = n, which completes
the proof of the lemma. □

Corollary 2.2.3. With the notation above, HomFp(U (Fp), Fp) is naturally identi-
ﬁed with a nondegenerate subspace U ⊂ Ext
1
X (Z/pZ, µp).

8 BENSON FARB, MARK KISIN AND JESSE WOLFSON

Proof. The proof of the Proposition 2.2.2 shows that there is a natural map

HomFp(U (Fp), Fp) → Ext
1
X (Z/pZ, µp)

whose image U is a nondegenerate subspace of dimension n = dimFp U. □

2.3. Essential dimension.

2.3.1. We refer the reader to [FKW19, §2] for the deﬁnitions and facts we will need
about essential dimension and essential dimension at p. We remind the reader that
for K a ﬁeld and Y → X a ﬁnite ´etale map of ﬁnite type K-schemes, ed(Y /X; p)
denotes the essential dimension at p of Y ¯K → X ¯K, where ¯K is an algebraic closure
of K.

2.3.2. We continue to use the notation introduced above. In particular A =
̂OAg,N ,¯x denotes the complete local ring which is a power series ring over OK in
n = (
g+1
2 ) variables.

Lemma 2.3.3. Let g : A → B and f : C → B be maps of power series rings over
OK, with f a ﬂat map. Suppose there exists a ﬁnite ´etale covering Y ′ → Spec C[1/p]
and an isomorphism of ´etale coverings ε : f ∗Y ′ ∼
−→ g∗A[p] over Spec B[1/p]. Then

Im( ¯mA/ ¯m2
A → ¯mB/ ¯m2
B) ⊂ Im( ¯mC / ¯m2
C → ¯mB/ ¯m2
B).

In particular, dimk ¯mC / ¯m2
C ≥ dimk Im( ¯mA/ ¯m2
A → ¯mB/ ¯m2
B).

Proof. By [FKW19, 2.1.8], we may assume that Y ′ is an extension of a constant
´etale group scheme by a constant multiplicative group scheme, and that ε is an
isomorphism of extensions. By [FKW19, 3.1.4, 3.1.5], the extension Y ′ is syntomic,
and we may assume that the isomorphism f ∗Y ′ ∼
−→ g∗A[p] extends to an iso-
morphism of ﬁnite ﬂat group schemes (which automatically respects the extension
structure) over Spec B.
Now let h : B → k[ǫ] be any map which vanishes on the image of ¯mC/ ¯m2
C, so that
h induces the constant map C → k. Then h∗f ∗Y ′ ∼
−→ h∗g∗A[p] is a split extension
over Spec k[ǫ]. It follows from [FKW19, 3.2.2] that h ◦ g(mA) = 0, which proves the
inclusion in the lemma. □

2.3.4. We introduce the following notation. For a map f : X → Y of smooth
k-schemes, we let
 r(f ) = max
x∈X(k) dimk Im( ¯mf (x)/ ¯m2
f (x) → ¯mx/ ¯m2
x)

For f a map of smooth OK-schemes, set r(f ) = r(f ⊗ k). Note that r(f ) does not
change if we restrict f to a dense open subset in X.

Proposition 2.3.5. Let Z be a smooth, connected OK-scheme, and let Z →
Ag,N/OK be a map of OK-schemes such that the image of the special ﬁber, Zk,
meets the ordinary locus A
ord
g,N ⊂ Ag,N/k. Then

ed(A[p]|ZK /ZK; p) ≥ r(f )

Proof. The proof of this is almost the same as that of Theorem [FKW19, 3.2.6].
The only diﬀerence is that we use Lemma 2.3.3 instead of Lemma 3.2.4 of loc. cit
at the end of the proof. □

MODULAR FUNCTIONS AND RESOLVENT PROBLEMS 9

Example 2.3.6. Let Hg denote the moduli of hyperelliptic curves of genus g. Let
Hg[n] be the moduli of pairs (C, B) where C is a hyperelliptic genus g curve and B
is a symplectic basis for H1(C; Z/nZ). Let τ : Hg/OK → Ag/OK denote the Torelli
map. By [Lan19, Theorem 1.2], τ is an embedding only when the characteristic
of k is prime to 2; when k is of characteristic 2, r(τ ) = g + 1. Because of this,
[FKW19, Theorem 3.2.6] does not give a lower bound on ed(Hg[2]/Hg; 2). Using
Proposition 2.3.5 above instead, as well as the argument of [FKW19, Corollary
3.2.7], we obtain ed(Hg[2]/Hg; 2) ≥ g + 1.

Remark 2.3.7. More generally, Proposition 2.3.5 gives an arithmetic tool for ob-
taining lower bounds on the essential dimension at p, analogous to the “ﬁxed point
method” (cf. [Rei10]). As forthcoming work of Brosnan-Fakhrudin-Reichstein
[BFR] demonstrates, the ﬁxed point method applied to the toroidal boundary
recovers the bounds of Theorem 1 and similar bounds for non-compact locally
symmetric varieties (including those not of Hodge type); it also allows one to use
toroidal boundary components other than those corresponding to Siegel parabolics.
However, as remarked in [FKW19], we are not aware of methods besides Proposi-
tion 2.3.5 that apply to unramiﬁed nonabelian covers of compact varieties.

2.3.8. Proposition 2.2.2 implies that the monodromy group of Ag,pN → Ag,N can
be identiﬁed with Sp2g(Fp). Fix such an identiﬁcation. Let G be a subgroup of
Sp2g(Fp) ⊂ Sp2g(Z/pN Z). Denote by Ag,G → Ag,N the ﬁnite, normal, covering
corresponding to G.

Theorem 2.3.9. Let p be a prime, and let N ≥ 3 be prime to p. G ⊂ Sp2g(Fp) ⊂
Sp2g(Z/pN Z). Then

ed(A[p]|Ag,G /Ag,G; p) ≥ max
U dimFp U ∩ G,

where the maximum on the right hand side is over all unipotent radicals of Siegel
parabolics in Sp2g(Fp).

Proof. Let U0 ⊂ Sp2g(Fp) be an abelian unipotent subgroup such that dimFp U0 ∩G
achieves the maximum. Let U ⊂ Sp2g /Fp be the abelian unipotent subgroup deﬁned
in Proposition 2.2.2. Because all Siegel parabolics are conjugate in Sp2g(Fp), there
exists a conjugate of G, denoted G
′ ⊂ Sp2g(Fp), such that

dimFp U (Fp) ∩ G
′ = dimFp U0 ∩ G.

Because conjugate subgroups give isomorphic covers, and because ed(−; p) is a
birational invariant,

ed(A[p]|Ag,N,G /Ag,N,G; p) = ed(A[p]|Ag,N,G′ /Ag,N,G′; p).

It therefore suﬃces to prove the theorem under the assumption that U0 = U (Fp).
For this, it suﬃces to consider the case G = U (Fp) ∩ G. In the following we slightly
abuse notation and write U for U (Fp).
Let x ∈ Ag,N (k) be a point in the ordinary locus. By (2) of Proposition 2.2.2,
there exists y ∈ Ag,pN (k) and x
′ ∈ Ag,N,U (k) with y mapping to x
′ and x, such
that the natural map
 A := ̂OAg,N ,x → ̂OAg,N,U ,x′

10 BENSON FARB, MARK KISIN AND JESSE WOLFSON

is an isomorphism, and such that, if B = ̂OAg,pN ,y, then

Spec B[1/p] → Spec A[1/p]

is a U -covering.
Let U = HomFp (U, Fp), and U ′
G = HomFp (U/(U ∩ G), Fp). By Corollary 2.2.3,
U is identiﬁed with a nondegenerate subspace of Ext
1
X (Z/pZ, µp) where X =
Spec A[1/p]. Now let A
′ = ̂OAg,N,U ∩G,¯x′′, where x
′′ denotes the image of y in
Ag,N,U∩G. Since Ag,N,U∩G is normal, using the notation of 2.1.3, we have A
′ =
A(U ′
G). Hence, by Lemma 2.1.4, we have

dimk Im( ¯mA/ ¯m2
A → ¯mA′/m2
A′) = dimFp U ∩ G,

and A
′ is a power series ring over OK.
Since x was any point in the ordinary locus, this shows that r(f ) ≥ dimFp U ∩ G,
where f : Ag,N,U∩G → Ag,N , and that Ag,N,U∩G is smooth over OK, over the
ordinary locus of Ag,N . Combining this with Proposition 2.3.5 proves the theorem.
□

3. Modular symplectic representations of finite groups

3.1. General Finite Groups. Let p be prime, G a ﬁnite group and V a faithful,
ﬁnite-dimensional G-representation over Fp. The pairing

ev : V ⊗ V ∨ → Fp

extends to a G-invariant symplectic form on V ⊕ V ∨. We refer to the associated
representation G → Sp(V ⊕ V ∨)
as the diagonal (symplectic) representation associated to V .

Lemma 3.1.1. Let H ⊂ G be an elementary abelian p-subgroup, such that H maps
to the unipotent radical of a maximal parabolic in GL(V ). Then there exists a Siegel
parabolic of P ⊂ Sp(V ⊕ V ∨) with unipotent radical U such that, under the diagonal
representation associated to V ,
 H ⊂ U ∩ G.

Proof. Any maximal parabolic in GL(V ) is the stabilizer P (W ) of a subspace W ⊂
V. Let U (W ) denote the unipotent radical of P (W ). Let W ⊥ ⊂ V ∨ denote the dual
subspace. Then W ⊕ W ⊥ is a Lagrangian subspace of V ⊕ V ∨, and

GL(V ) ∩ StabSp(V ⊕V ∨)(W ⊕ W ⊥) = StabGL(V )(W ) = P (W ).

Hence GL(V ) ∩ U (W ⊕ W ⊥) = U (W ),
where U (W ⊕ W ⊥) is the unipotent radical of StabSp(V ⊕V ∨)(W ⊕ W ⊥), the Siegel
parabolic corresponding to W ⊕ W ⊥. In particular H ⊂ U (W ) ⊂ U (W ⊕ W ⊥), the
Siegel parabolic corresponding to W ⊕ W ⊥. □

3.1.2. Let sp(G) := max
U⊂GL(V ) dimFp U ∩ G

where the maximum is taken over all faithful representations G of V, and unipo-
tents U of maximal parabolics in GL(V ). Proposition 3.1.1 and Theorem 2.3.9
immediately imply the following.

MODULAR FUNCTIONS AND RESOLVENT PROBLEMS 11

Corollary 3.1.3. For some g, there exists a congruence cover Ag,p → Ag,G with

ed(Ag,p/Ag,G; p) ≥ sp(G).

Remark 3.1.4. While Corollary 3.1.3 implies that ed(G; p) ≥ sp(G), this is not
hard to show directly, e.g. by [BR97, Lemma 4.1]. In fact, let

rp(G) := max
H⊂G dimFp H

where the maximum is taken over all elementary abelian p-groups H ⊂ G. Then
ed(G; p) ≥ rp(G) ≥ sp(G). The novelty of Corollary 3.1.3 is that a) this lower bound
can be realized by an explicit congruence cover; and b) the congruence cover, and
thus the lower bound, comes from modular representation theory at the relevant
prime, rather than from ordinary representation theory in characteristic 0 (as in
e.g. [BR97] or the theorem of Karpenko-Merkurjev [KM08]).
The corollary is most interesting in those cases where sp(G) is large. In the
remainder of this section we give examples where sp(G) is equal to, or at least very
close to rp(G). These consist of the case of alternating groups when p = 2, and the
case where G is the Fq-points of a split semisimple group of classical type.

3.2. The Groups Sn and An. We now specialize to the symmetric groups Sn and
the alternating groups An.

3.2.1. We would like to apply Corollary 3.1.3 to the case of symmetric and alternat-
ing groups. Meyer-Reichstein [MR09, Corollary 4.2] proved that ed(Sn; p) = rp(Sn)
and similarly for An for all n and p. However, in Appendix A, Harman shows that
for p > 2, sp(Sn) < rp(Sn) and similarly for An. The purpose of this section is to
show - see Proposition 3.2.2 below - that one has s2(Sn) = r2(Sn) for all n, and
s2(An) = r2(An) (resp. s2(An) = r2(An) − 1) for n = 2, 3 (resp. 0, 1) modulo 4.
This uses a remarkable mod 2 symplectic representation of Sn, discovered by Dick-
son. Harmon’s results imply that for n ≥ 5, this is the only mod 2 representations
for which the unipotent of a maximal parabolic meets Sn in a maximal elementary
abelian 2-group.
Recall the “permutation irrep” V of Sn over Fp.4 For p ∤ n this is the analogue
over Fp of the standard permutation irrep in characteristic 0, i.e. the invariant
hyperplane
 V = {(a1, . . . , an) ∈ Fn
p | ∑ ai = 0}

For p | n the diagonal line ∆ := {(a, . . . , a)} ⊂ Fn
p is an invariant subspace of the
invariant hyperplane, and

V = {(a1, . . . , an) ∈ Fn
p | ∑ ai = 0}/∆.

Dickson [Dic08] showed that over F2, the permutation irrep of Sn is a symplectic
representation. Let
 dn := ⌈ n
2 ⌉ − 1,

so that Dickson’s representation gives a “Dickson embedding” Sn ⊂ Sp2dn (F2).

4The results of Dickson [Dic08] and Wagner [Wag76, Wag77] show that the permutation irrep
is a minimal-dimensional faithful irrep for n > 8 and p = 2, or for n > 6 and p odd.

12 BENSON FARB, MARK KISIN AND JESSE WOLFSON

Proposition 3.2.2. Let N ≥ 3 be odd. For all n ≥ 2, consider the Dickson
embedding Sn ⊂ Sp2dn(F2) ⊂ Sp2dn(Z/2N Z). There exists a Siegel parabolic with
unipotent radical U such that

dimF2 U ∩ Sn = ⌊ n
2 ⌋,

dimF2 U ∩ An = ⌊ n
2 ⌋ − 1.

By Theorem 2.3.9, for all n ≥ 1:

ed(Adn,2N /Adn,Sn ; 2) = ⌊ n
2 ⌋ = ed(Sn; 2),

ed(Adn,2N /Adn,An ; 2) = ⌊ n
2 ⌋ − 1,

i.e.
 ed(Adn,2N /Adn,An; 2) = { ed(An; 2) − 1 n = 0, 1 mod 4
ed(An; 2) n = 2, 3 mod 4

Proof. Let V denote the permutation irrep of n over F2, as in [Dic08], i.e.

V = H/∆ = {(x1, . . . , x2⌈ n
2 ⌉) ∈ F2⌈ n
2 ⌉
2 | ∑

i xi = 0}/{(x, . . . , x) ∈ F2}

A convenient basis for V is given by the cosets in H of

ei := [(0, . . . , 1, . . . , 0
︸ ︷︷ ︸
1 in the ith place

, 0, 1)]

for i = 1, . . . , 2dn. With respect to this basis the action of S2dn ⊂ Sn is the standard
permutation action of S2dn on F2dn
2 . Dickson [Dic08, p. 124] proved that the Sn
action on F2dn
2 preserves the symplectic form ∑1≤i̸=j≤dn xiyj. We now change basis
for ease of studying a Lagrangian. Let

ωi := e2i−1 + e2i

ω∨
i = ∑2i−1
j=0 ej.

A straightforward computation shows that the planes W = ⟨{ωi}n
i=1⟩ and W ⊥ =
⟨{ω∨
i }n
i=1⟩ are dual Lagrangians written with dual Lagrangian bases.
Now ﬁx W and let P := Stab(W ) be the corresponding Siegel parabolic with
unipotent U . From the Lagrangian basis for W , we see that

(3.2.2.1) F⌊ n
2 ⌋
2 = ⟨(12), (34), . . . , (2⌊ n
2 ⌋ − 1 2⌊ n
2 ⌋)⟩ ⊂ U ∩ Sn

But this is a maximal elementary abelian 2-group in Sn, so (3.2.2.1) is an equality.
Thus
 U ∩ An = ⟨(12)(34), . . . , (12)(2⌊ n
2 ⌋ − 1 2⌊ n
2 ⌋)⟩ = F⌊ n
2 ⌋−1
2

as claimed. □

MODULAR FUNCTIONS AND RESOLVENT PROBLEMS 13

3.3. Finite groups of Lie type.

Proposition 3.3.1. Let q = pr, and G = H(Fq), where H is one of the semisim-
ple Lie groups SLm, SO2m+1, Sp2m with m ≥ 2 or SO2m, with m ≥ 4. Let ρ :
H → GL(V ) be the standard representation of H over Fq. Then there exists a par-
abolic P (W ) ⊂ GL(V ) with unipotent radical U, such that dimFq W = ⌊ dim V
2 ⌋, and
r′
p(G) := dimFq G ∩ U satisﬁes:

• If G = SLm(Fq), then r′
p(G) = ⌊ m2
4 ⌋.
• If G = Sp2m(Fq) then r′
p(G) = m(m+1)
2 .
• If G = SO2m(Fq) then r′
p(G) = m(m−1)
2 .
• If G = SO2m+1(Fq) then r′
p(G) = m(m−1)
2 .
We have r · r′
p(G) = rp(G) in all cases except if G = SO2m+1, in which case
rp(G)/r = m(m+1)
2 if q is even and rp(G)/r = m(m−1)
2 + 1 (resp. 5, resp. 3) if q is
odd and m ≥ 4, (resp. m = 3, resp. m = 2).

Proof. We use the standard representations of the root systems of each of the groups
H. In each case, we will recall the weights appearing in V, specify the subspace
W ⊂ V, and describe a subgroup UG ⊂ H as a sum of root spaces. In each case
if r is a root appearing in UG and w, w′ are weights appearing in W and V /W
respectively, then r + w does not appear in V, and r + w′ does not appear in V /W.
This implies that UG ⊂ H ∩ U.
If G = SLm(Fq), then the weights of V are e1, . . . , em, and W = ⟨e1, . . . , e⌊ m
2 ⌋⟩.
The roots appearing in UG are ei − ej with i ≤ ⌊ m
2 ⌋ < j.
If G = Sp2m(Fq), then the weights of V are ±e1, . . . , ±em, and W = ⟨e1, . . . , em⟩.
The roots appearing in UG are ei + ej and 2ei for 1 ≤ i < j ≤ m.
If G = SO2m(Fq), then the weights of V are ±e1, . . . , ±em, and W = ⟨e1, . . . , em⟩.
The roots appearing in UG are ei + ej for 1 ≤ i < j ≤ m.
If G = SO2m+1(Fq), then the weights of V are ±e1, . . . , ±em, 0 and W =
⟨e1, . . . , em⟩. The roots appearing in UG are ei + ej for 1 ≤ i < j ≤ m.
The maximal elementary abelian p-subgroups of H(Fq) for each group H ap-
pearing above are computed in [Bar79]. In particular, for G equal to one of
SLm(Fq), Sp2m(Fq), SO2m(Fq), one sees that UG is already a maximal elementary
abelian p-subgroup, so that UG = H ∩U and r·r′
p(G) = rp(G). For G = SO2m+1(Fq)
the claims about rp(G) also follows from loc. cit, and it remains only to prove that
UG = H ∩ U in this case.
To see this, consider v = ∑r arr ∈ Lie (H ∩ U ) where r is a positive root of H
and ar is a scalar. Now V is a cyclic highest weight module for Lie H. Using this
and that v annihilates ej ∈ W, one gets ar = 0 if r = ei − ej. Similarly, since v
annihilates −ej ∈ V /W, ar = 0 for r = ej. Thus v ∈ UG. □

Remark 3.3.2. Note that when q is even, one has SO2m+1(Fq) ≃ Sp2m(Fq), so
that sp(G) = rp(G) in this case.

4. Classical Problems and Congruence Covers

Beginning with the work of Hermite on the quintic [He1858], the use of modu-
lar functions to solve algebraic equations is a major theme of 19th century work,
including Klein’s icosahedral solution of the quintic [Kl1884], the Klein-Burkhardt
formula for the 27 lines on a cubic surface [Kl1888, Bu1890, Bu1891, Bu1893], the

14 BENSON FARB, MARK KISIN AND JESSE WOLFSON

Klein-Gordan solution of equations with Galois group the simple group PSL(2, 7)
[Kl1879, Go1882], and the Klein-Fricke solution of the sextic [Kle05, Fri26]. Under-
lying this work is the fact that problems of algebraic functions are often equivalent
to problems of modular functions and congruence covers.
Our goal in this section is to record the classical equivalences, and add to them
using recent advances in uniformization. We begin by axiomatizing the notion of
accessory irrationality, and recalling the general context in which to take up Klein’s
call to “fathom the nature and signiﬁcance of the necessary accessory irrationalities”
[Kl1884, p. 174]. We then recall the general setup of congruence covers of locally
symmetric varieties in order to state the precise equivalences.
While many of the results of this section are implicit in the classical literature, as
far as we can tell, with the exception of Klein’s Normalformsatz [Kl1884], that var-
ious classical problems are in fact equivalent has gone unremarked in the literature
until quite recently [FW18].

4.1. Accessory Irrationalities and E-Versality. For the rest of the paper we
ﬁx an algebraically closed ﬁeld K of characteristic 0.

4.1.1. By a branched cover Y → X, we mean a dominant, ﬁnite map of normal
K-schemes of ﬁnite type. Branched covers form a category: a map (Y ′ → X ′) →
(Y → X) is a commutative diagram

Y ′ //

  
 Y

  
X ′ // X.

If f : X ′ → X is a map of normal K-schemes of ﬁnite type, denote by f ∗Y the
normalization of Y ×X X ′. If X is connected then Y → X corresponds to a ﬁnite
set SY with an action of π1(U ) for some dense open U ⊂ X, where π1(U ) denotes
the ´etale fundamental group of U. We denote by Mon(Y /X) the image of π1(U ) in
Aut(SY ).

4.1.2. We now introduce the notion of a class of accessory irrationalities (cf. Klein
[Kl1884, Kl1893], see also Chebotarev [Che32]).

Deﬁnition 4.1.3 (Accesory irrationalities). A class of accessory irrationalities
is a full subcategory E of the category of branched covers. If E(X) ⊂ E denotes the
subcategory consisting of branched covers ˜X → X, then we require that E(X) is
stable under isomorphisms, and satisﬁes the following conditions.

(1) For any X, the identity X → X is in E(X).
(2) For any map f : X ′ → X of normal K-schemes of ﬁnite type, f ∗ induces a
functor f ∗ : E(X) → E(X ′).
(3) E(X ∐ X ′) = E(X) × E(X ′).
(4) E(X) is closed under products: If E, E′ ∈ E(X), then E ×X E′ ∈ E(X).
(5) If U ⊂ X is dense open, then the map E(X) → E(U ) induced by restriction
is an equivalence of categories.
(6) If E → X ′ → X are branched covers and if E → X is in E(X) then E → X ′

is in E(X ′).

MODULAR FUNCTIONS AND RESOLVENT PROBLEMS 15

Axiom (2) implies that E is a category ﬁbered over the category of normal K-
schemes. Note that Axiom (3) implies that it is enough to specify E(X) for X
connected.

Deﬁnition 4.1.4. Fix a class E of accessory irrationalities. The essential dimension
of a cover ˜X → X, with respect to E is:

ed( ˜X/X; E) := min
(E→X)∈E ed(E ×X ˜X/E).

Example 4.1.5. Some of the core classical examples of E are as follows (for sim-
plicity we specify E(X) only for X connected):
(1) For E(X) = {id : X → X}, the quantity ed( ˜X/X; E) is just the essential
dimension ed( ˜X/X).
(2) Let p be a prime and let E(X) be the subcategory of branched covers of X
whose degree is coprime to p. Then ed( ˜X/X; E) is the essential dimension
at p. We emphasize that, although it leads to the same notion of essential
dimension at p, we do not insist that E is connected, as this version of the
deﬁnition does not satisfy Axiom (3) of Deﬁnition 4.1.3.
(3) Let E(X) be the set of covers E → X with Mon(E/X) abelian. Then
ed( ˜X/X; E) is the abelian resolvent degree. Likewise, we can consider the
class of accessory irrationalities with nilpotent (resp. solvable) monodromy,
to obtain the nilpotent (resp. solvable) resolvent degree (see [Kl1893,Che32,
Che43]).
(4) Let G be a ﬁnite simple group, and let E(X) consist of all E → X such
that for each connected component E′ of E, the branched cover E′ → X is
Galois and a composition series for Gal(E′/X) has no factor isomorphic to
G. We write ed( ˜X/X; G) for ed( ˜X/X; E).

Deﬁnition 4.1.6 (E-versality). Let E be a class of accessory irrationalities. A
Galois branched cover ˜X → X with group G is E-versal if for any other Galois
G-cover ˜Y → Y , and any Zariski open U ⊂ X, there exists
(1) an accessory irrationality E → Y in E(Y ),
(2) a nontrivial rational map f : E → U , and
(3) an isomorphism f ∗ ˜X|U ∼= ˜Y |E.

Remark 4.1.7. If E is the trivial class of accessory irrationalities, i.e. E(X) only
contains the identity, then E-versal is just “versal” in the usual sense of the term
(see e.g. [GMS03, Section 1.5]).
If E ′ ⊂ E are classes of accessory irrationalities, then E ′-versality for a G-cover
implies E-versality. In particular a cover which is versal is E-versal for any class E.

Example 4.1.8.
(1) Hilbert’s Theorem 90 implies that for a ﬁnite group G, and every faithful
linear action G ⟲ An, the map An → An/G is versal (see [DR15]).
(2) The Merkujev-Suslin Theorem [MS83, Theorem 16.1] implies that for every
faithful, projective-linear action G ⟲ Pn, the map Pn → Pn/G is solvably
versal, i.e. E-versal for the class E of solvable branched covers.5

Lemma 4.1.9. Let G be a ﬁnite group, let E be a class of accessory irrationalities,
and let ˜X → X be an E-versal G-cover.

5Mutatis mutandis, this follows by the same reasoning as in [DR15].

16 BENSON FARB, MARK KISIN AND JESSE WOLFSON

(1) Let ˜X → ˜Z be a G-equivariant dominant rational map. Then ˜Z → ˜Z/G is
an E-versal G-cover.
(2) Let H ⊂ G be any subgroup. Then ˜X → ˜X/H is an E-versal H-cover.

Proof. The ﬁrst statement follows immediately from the deﬁnition. For the second,
let ˜Y → Y be a Galois H-cover. Then

˜Y ×H G → Y

is a Galois G-cover which is H-equivariantly isomorphic to ˜Y × G/H → Y . By
E-versality, for any Zariski open U ⊂ X, there exists an accessory irrationality

E → Y

in E, and a rational map f : E → U

with an isomorphism of G-covers

f ∗ ˜X ∼= ( ˜Y ×H G)|E.

By the Galois correspondence for covers, the H-equviariant isomorphism above
implies that E → U factors through a map

˜f : E → ( ˜X/H)|U

We conclude that ˜f ∗ ˜X ∼= ˜Y |E and that ˜X → ˜X/H is E-versal for H as claimed. □

Remark 4.1.10. Example 4.1.8(1) and Lemma 4.1.9(1) immediately imply that
for each n ≥ 4, the cover M0,n → M0,n/Sn is versal for the group Sn.

4.1.11. We can also consider the resolvent degree of a cover ˜X → X, which is
somewhat diﬀerent from, but related to the idea of the general notion of essential
dimension deﬁned above. To explain this, write E• → X for a tower of branched
covers E = Er → · · · → E0 = X. The resolvent degree of ˜X → X is deﬁned as

RD( ˜X/X) = min
E•→X max {
ed(E ×X ˜X/E), {ed(Ei/Ei−1)}r
i=1}

where E• → X runs over all sequences of covers.
When Mon( ˜X/X) is simple, it follows from [FW18, Cor. 2.18] that the deﬁnition
of RD( ˜X/X) does not change if we consider only E• → X such that the compo-
sition π1(E) → π1(X) → Mon( ˜X/X) is surjective and ed(Ei/Ei−1) < dim(X). In
particular

(4.1.11.1) min
E•→X ed(E ×X ˜X/E) ≤ RD( ˜X/X)

where E• → X runs over sequences of covers satisfying these conditions. On the
other hand, in every known example, the current best upper bound for RD(−) can
be exhibited using such a sequence E• → X which in addition satisﬁes ed(E ×X
˜X/E) ≥ ed(Ei+1/Ei), for i = 1, . . . , r.
Hilbert [Hi1900, Hil27] made three conjectures on the resolvent degree of the
general degree n polynomial; equivalently on

RD(n) := RD(M0,n/(M0,n/Sn)) = RD(M0,n/(M0,n/An)).

MODULAR FUNCTIONS AND RESOLVENT PROBLEMS 17

Conjecture 4 (Hilbert). The following equalities hold:

Sextic Conjecture: RD(6) = 2.
13th Problem: RD(7) = 3.
Octic Conjecture: RD(8) = RD(9) = 4.

The upper bounds in Conjecture 4 are known; the ﬁrst two are due to Hamilton,
the last to Hilbert.
Our interest in E-versality comes from the following lemma, which is proven
mutatis mutandis by the same argument as in the proof of [FW18, Proposition 3.7].

Lemma 4.1.12. Let E be a class of accessory irrationalities and let ˜X → X be an
E-versal G-cover. For any Galois branched cover ˜Y → Y with monodromy G,

ed( ˜Y /Y ; E) ≤ ed( ˜X/X; E).

In particular, for any other E-versal G-cover ˜X ′ → X ′,

ed( ˜X ′/X ′; E) = ed( ˜X/X; E).

Further, if E is any of the classes of Example 4.1.5 and if G is simple, then

RD( ˜Y /Y ) ≤ RD( ˜X/X) and RD( ˜X ′/X ′) = RD( ˜X/X).

Lemma 4.1.12 makes precise the classical discovery that E-versal G-covers pro-
vide “normal forms” to which every other G-cover or can be reduced. Notably, for
many groups G of classical interest, congruence covers are E-versal for a natural
choice of E.

Remark 4.1.13. While the notion of versality has been studied intensively for
several decades, many of the most interesting normal forms, beginning with Klein’s
Normalformsatz, rely on the notion of solvable versality, which is substantially more
ﬂexible. For example, a versal G-variety of minimal dimension must be unirational.
On the other hand, there are no rational A6 curves (by Klein’s classiﬁcation of
ﬁnite M¨obius groups), and the level 3 Hilbert modular surface of discriminant
5, which is solvably versal for A6 and conjectured by Hilbert to be of minimal
dimension among such varieties, has arithmetic genus equal to 5 (see the discussion
in the proof of Propositon 4.2.5 below). A better understanding of the geometric
implications of solvable versality (and related notions) could shed signiﬁcant light
on the underpinnings of Hilbert’s conjectures.

4.2. E-Versal Congruence Covers. We can now record the E-versal congruence
covers that we know. Klein’s Normalformsatz provides the paradigmatic example
for what follows.

4.2.1. Let G be a group-scheme of ﬁnite type over Z whose generic ﬁber, which
we also denote by G, is a connected semisimple group. A subgroup Γ ⊂ G(Z) is
called a congruence subgroup if it contains

G(Z, n) := ker(G(Z) → G(Z/n))

for some positive integer n.
We assume that the quotient X of G(R) by its maximal compact subgroup is
a Hermitian symmetric domain. Then for any congruence subgroup Γ, a theorem

18 BENSON FARB, MARK KISIN AND JESSE WOLFSON

of Baily-Borel asserts that MΓ := X/Γ is a complex, quasiprojective variety. For
Γ′ ⊂ Γ congruence subgroups there is a natural map covering map MΓ′ → MΓ.
For L a totally real number ﬁeld, one can apply the above to ResL/QG, instead
of G. In this case we have G(OL) ∼
−→ ResL/QG(Z) and when we write G(OL)
we mean that we are working the Hermitian symmetric domain and congruence
subgroups associated with the group ResL/QG. Similarly, we write G(OL, n) for
ResL/QG(Z, n). If L = Q(
√
d) is real quadratic, denote by G(OL, √
d) the kernel of

ResL/QG(Z) = G(OL) → G(OL/√
d).

If L is quadratic imaginary and a, b are non-negative integers, one can consider
the unitary group U(a, b) of signature a, b deﬁned by L. This is the subgroup scheme
of ResOL/ZGLn, where n = a + b, which ﬁxes the standard Hermitian (with respect
to conjugation on K) form of signature (a, b). One also has the corresponding
projective unitary group PU(a, b).
In fact for the rest of this section we take L = Q(ω), where ω is a primitive
cube root of 1, and we will only need groups of signature n − 1, 1. We denote by
PU(n − 1, 1)(Z, √
−3) the kernel of the composite

PU(n − 1, 1)(Z) → ResOL/Z PGLn(Z) = PGLn(OL) → PGLn(F3).

Theorem 4.2.2 (Klein’s Normalformsatz, [Kl1884]). Let E be any class of
accessory irrationalities containing all quadratic branched covers. Then the level 5
cover of the modular curve
 MSL(Z,5) → MSL2(Z).

is an E-versal A5-cover. In particular, for any branched cover ˜X → X with mon-
odromy A5, ed( ˜X/X; E) = RD( ˜X/X) = 1.

This is in contrast to Klein’s theorem that ed(A5) = 2. We can add another
example for A5, which was studied in detail by Hirzebruch [Hir76], and was likely
known to Kronecker, Klein and Hilbert.

Proposition 4.2.3. The level 2 cover of the Hilbert modular surface

MSL2(Z[ 1+√5
2 ],2) → MSL2(Z[ 1+√5
2 ])
is versal for A5.

Proof. By [Hir76], there is an A5-equivariant birational equivalence

M0,5 ≃ MSL2(Z[ 1+√
5
2 ],2).

There is an A5-equvariant dominant map

A5 → M0,5,

where the source is the permutation representation and the map is the quotient
by the diagonal action of Aut(A1). By Hilbert’s Theorem 90, A5 is versal. The
proposition now follows from Lemma 4.1.9. □

Similar to, but less well-known than, Klein’s normalformsatz is the following (see
[Kl1879, Go1882], [Hir77, p. 318-319] and [Fri26, Vol. II, Part 2, Chapters 1-2]).
Denote by PSL(2, 7) the image of SL2(F7) → PGL2(F7); this is a simple group.

Proposition 4.2.4 (Normal forms for PSL(2, 7)).

MODULAR FUNCTIONS AND RESOLVENT PROBLEMS 19

(1) Let PGL+
2 (Z[√7]) ⊂ PGL2(Z[√7]) denote the subgroup of elements which
lift to an element of GL2(Z[√7]) with totally positive determinant. The
cover M PGL2(Z[√
7],√
7) → M PGL
+
2 (Z[√
7])
of Hilbert modular surfaces is versal for the simple group PSL(2, 7).
(2) Let E be any class of accessory irrationalities containing all S4-covers. Let
̃SL2(Z, 7) denote the kernel of the surjection SL2(Z) → PSL(2, 7). Then
the level 7 modular curve

M ̃SL2(Z,7) → MSL2(Z)

is an E-versal PSL(2, 7)-cover. In particular, for any branched cover ˜X →
X with monodromy PSL(2, 7),

ed( ˜X/X; E) = RD( ˜X/X) = 1.

Proof. We remark that Z[√
7]× = {±ǫn} where ǫ = 8+3√
7 is the fundamental unit.
Hence PGL2(Z[√7], √
7) ⊂ PGL+
2 (Z[√7]), and in particular, the latter group is a
congruence subgroup.
Consider the modular curve M ̃SL2(Z,7). This has genus 3, and so the action of

PSL(2, 7) on 1-forms gives a linear action of PSL(2, 7) on A3, and an equivariant
dominant rational map A3 → P2. Lemma 4.1.9 then implies that P2 is versal
for PSL(2, 7). As noted on [Hir77, p. 318-319], there is a PSL(2, 7)-equivariant
birational isomorphism P2 ∼= M PGL2(Z[√
7],√
7).

This proves the ﬁrst statement of the proposition.
The second statement follows from [Kl1879, Go1882]. In modern language, it
suﬃces to construct an accessory irrationality E → P2/PSL(2, 7) and a PSL(2, 7)-
equivariant dominant rational map

P2|E → M ̃SL2(Z,7).

For this, the canonical embedding of the modular curve M ̃SL2(Z,7) gives a PSL(2, 7)-
equivariant map M ̃SL2(Z,7) → P2.

As Klein discovered, the image of this map is a quartic curve, the so-called “Klein
quartic”. Fixing any PSL(2, 7)-invariant pairing on P2, there is a rational map

P2 → M0,4/S4.

which sends a point x ∈ P2 to the intersection of the dual line Lx with the Klein
quartic. Let E = M0,4|P2.
Then there is a PSL(2, 7)-equivariant dominant map

P2|E → M ̃SL2(Z,7)
as claimed. □

We can add the following result to the above.

Proposition 4.2.5 (Normal forms for the sextic).

20 BENSON FARB, MARK KISIN AND JESSE WOLFSON

(1) The congruence cover
 A2,2 → A2

and the Picard modular 3-fold

MPU(3,1)(Z,√
−3) → MPU(3,1)(Z)

are versal for A6.
6

(2) For E any class of accessory irrationalities containing all quadratic covers
and composites thereof, the congruence cover

A2,3/F×
3 → A2,A6

and the Picard modular 3-fold

MPU(3,1)(Z,2) → MPU(3,1)(Z,A6)

are E-versal for A6.
(3) For E any class of accessory irrationalities containing all quadratic and
cubic covers and composites thereof, the Hilbert modular surface

M ̃
SL2(Z[ 1+√5
2 ],3) → MSL2(Z[ 1+√5
2 ])

is E-versal for A6, where ̃
SL2(Z[ 1+√5
2 ], 3) denotes the kernel of the map
SL2(Z[ 1+√5
2 ]) → PGL2(F9) = A6.
In particular (cf. Remark 4.1.10 and Lemma 4.1.12) Hilbert’s Sextic Conjecture
is equivalent to the statement that the resolvent degree of any (and thus each) of
the above covers is dim(MSL2(Z[ 1+√
5
2 ])) = 2.

Let PSp(4, 3) denote the image of Sp4(F3) → PSp4(F3); this is a simple group.
To prove the proposition, we make use of the following lemma.

Lemma 4.2.6. Let PSp(4, 3) act linearly on P3 and let G ⊂ PSp(4, 3) be any
subgroup. Let E be any class of accessory irrationalities containing all composites
of quadratic covers. Then P3 is an E-versal G-variety.

Proof. There is (see e.g. [ABL+19]) an Sp4(F3)-equivariant dominant rational map

A4 → P3.

Lemma 4.1.9 then implies that P3 is versal for Sp4(F3) As observed in the proof
of [FW18, Theorem 4.3], this implies that P3 is E-versal for PSp(4, 3) and thus, by
Lemma 4.1.9 for any G ⊂ PSp(4, 3) as well. □

Proof of Proposition 4.2.5. For versality, as in the proof of Proposition 4.2.3, it
suﬃces to prove that there are A6-equivariant birational isomorphisms

(4.2.6.1) M0,6 ∼= A2,2 ∼= MPU(3,1)(Z,√
−3)

where M0,6 is the moduli of 6 distinct points in P1. The ﬁrst isomorphism of
(4.2.6.1) is the classical period map which sends 6 points in P1 to the Jacobian of

6Recall that there are exceptional isomorphisms Sp4(F2) ∼= O+
4 (F3) ∼= S6.

MODULAR FUNCTIONS AND RESOLVENT PROBLEMS 21

the hyperelliptic curve branched at those points. For the second, consider the Segre
cubic threefold X3 in P5 given by

X3 := {[x0 : · · · : x5] ∈ P5 :
 5∑

i=0 xi = 0 =
 5∑

i=0 x
3
i }.

The permutation action of S6 on P5 leaves invariant X3, permuting its 10 nodes.
Kondo [Kon13] proved that X3 is isomorphic to the Satake-Bailey-Borel compact-
iﬁcation of the Picard modular 3-fold MPU(3,1)(Z,√
−3). One can check that the
birational map MPU(3,1)(Z,√
−3) → X3 is S6-equivariant (cf. e.g. [SBT97, p. 6,
Lemma 2.1]).
Hunt proves in [Hun96, Theorem 3.3.11] that the dual variety to X3 is the so-
called Igusa quartic I4, which is the moduli space of 6 points on a conic in P2. The
two varieties X3 and I4 are S6-equivariantly birational. The Igusa quartic I4 is the
Satake compactiﬁcation of A2,2. The second birational isomorphism in (4.2.6.1) is
the composition of these.
Now let E be any class of accessory irrationalities containing all quadratic covers
and composites thereof. As explained in Hunt [Hun96, Chapter 5.3], there is a 6 : 1
(in particular, dominant) PSp(4, 3)-equivariant rational map

P3 → B

where the action of PSp(4, 3) on P3 is linear and where B denotes the “Burkhardt
quartic”. There is also a PSp(4, 3)-equivariant birational isomorphism

B ∼= A2,3/F×
3 .

Lemma 4.2.6 implies that A2,3/F×
3 is E-versal for G = A6 ⊂ PSp(4, 3).
Thus A2,3/F×
3 is E-versal for any subgroup of PSp(4, 3), in particular A6. Finally,
Hunt [Hun96, Theorem 5.6.1] proved that B is PSp(4, 3)-equivariantly biregularly
isomorphic to the Baily-Borel compactiﬁcation of MPU(3,1)(Z,2).
For the last statement, let E be any class of accessory irrationalities containing
all composites of quadratic and cubic covers. By [vdG88, Chapter VIII, Theorem
2.6], there exists an A6-equivariant birational isomorphism

MSL2(Z[ 1+√
5
2 ],3) ∼= V1,2,4 ⊂ P5

where V1,2,4 is the common vanishing locus of the 1st, 2nd and 4th elementary
symmetric polynomials and A6 acts on P5 via the permutation representation. As
above, it suﬃces to construct an accessory irrationality E → A6/A6 in E and an
equivariant dominant rational map

A6|E → V1,2,4.

This follows from the classical theory of Tschirnhaus transformations (see e.g. [Wol]
for a contemporary treatment). Recall that a Tschirnhaus transformation Tb, for
some b := (b0, . . . , b5) ∈ A6, is the assignment which sends a root z of the generic
sextic to 5∑

i=0 bizi.

This deﬁnes an S6-equivariant rational map

Tb : A6 → A6

22 BENSON FARB, MARK KISIN AND JESSE WOLFSON

Letting b vary, we have an A6
b parameter space of Tschirnhaus tranformations for
each sextic, which we view as a trivial bundle

π1 : A6 × A6
b → A6.

We also have an evaluation map

ev : A6 × A6
b → A6

By direct computation (see e.g. [Wol, Deﬁnition 3.5 and Lemma 3.6]), ev−1( ̃V1,2,4),
i.e. the preimage under the map ev of the aﬃne cone over V1,2,4, is the intersection
of a (trivial) family of hyperplanes ̃T1, a cone over a generically smooth quadric ̃T2
(for smoothness, see e.g. [Wol, Lemma 2.6]), and a quartic cone ̃T4. By the classical
theory of quadrics (e.g. [Wol, Lemma 5.10]), there exists a ﬁnite, generically ´etale
map E0 → A6/A6

with monodromy a 2-group such that the quadric cone ̃T2|E0 contains a (trivial)
family L → E0 of 2-planes over E0. The intersection

L ×E0 ̃T4

is thus the aﬃne cone over a family of 4 distinct points in P1. There thus exists an
S4-cover E → E0

and a section σ : E → ev−1( ̃V1,2,4)|E. The map

ev ◦ σ : A6|E → V1,2,4

gives the dominant map we seek. By construction E → A6/A6 is in the class E,
and thus V1,2,4 is indeed E-versal. □

Proposition 4.2.7 (Normal forms for the 27 lines).

(1) The congruence cover

MPU(4,1)(Z,√
−3) → MPU(4,1)(Z)

is versal for O+
5 (F3) ∼= W (E6). 7

(2) For E any class of accessory irrationalities containing all quadratic covers
and composites thereof, the congruence cover

A2,3/F×
3 → A2

and the Picard modular 3-fold

MPU(3,1)(Z,2) → MPU(3,1)(Z)

are E-versal for the simple group PSp(4, 3) ∼= W (E6)
+ (the normal index
2-subgroup of W (E6)).

In particular, [FW18, Conjecture 1.8] implies and is implied by the resolvent
degree of any (and thus each) of the above covers equaling dim(A2) = 3.

7Recall that there is an exceptional isomorphism of O+
5 (F3) with the Weyl group of E6.

MODULAR FUNCTIONS AND RESOLVENT PROBLEMS 23

Proof. By Allcock-Carlson-Toledo [ACT02], there exists an O+
5 (F3) ∼= W (E6)-
equivariant birational isomorphism

H3,3(27) ≃ MPU(4,1)(Z,√
−3)

from the moduli H3,3(27) of smooth cubic surfaces with a full marking of the
intersection of their 27 lines to the Picard modular 4-fold.
By [DR14, Lemma 6.1] H3,3(27) is versal for W (E6). By Lemma 4.1.9, both
varieties are therefore versal for any subgroup of W (E6).
The remaining statements follow from the proof of Proposition 4.2.5 above. Con-
cretely, there we showed that A2,3/F×
3 was E-versal for any subgroup of PSp(4, 3),
in particular for PSp(4, 3) itself. Together with the PSp(4, 3)-equivariant birational
isomorphism A2,3/F×
3 ≃ MPU(3,1)(Z,2)
recalled in the proof of Proposition 4.2.5, this implies the result. □

Proposition 4.2.8 (Normal forms for the septic, the octic, and 28 bitan-
gents). Let G ⊂ Sp6(F2) be any subgroup. Then the cover

A3,2 → A3,G

is versal for G. In particular (cf. Remark 4.1.10 and Lemma 4.1.12) :

(1) Hilbert’s 13th Problem is equivalent to

RD(A3,2/A3,A7) = 3.

(2) Hilbert’s Octic Conjecture [Hil27, p. 248] is equivalent to

RD(A3,2/A3,A8) = 4.

(3) [FW18, Problem 5.5(2)], which asks for the resolvent degree of ﬁnding a
bitangent on a planar quartic, is equivalent to asking for RD(A3,2 → A3).

Proof. This follows as in the proof of [FW18, Proposition 5.7], which in turn
draws on [DO88] and ideas of Coble. As explained there, there exists an Sp6(F2)-
equivariant dominant rational map

A7 → H4,2(28) ≃ M3[2]

where H4,2(28) denotes the moduli of smooth planar quartics with a marking of
their 28 bitangents, and M3[2] denotes the moduli of genus 3 curves with full
level 2 structure. The period mapping gives an Sp6(F2)-equivariantly birational
isomorphism M3[2] ≃ A3,2,

and thus A3,2 is a versal G-variety for any G ⊂ Sp6(F2) as claimed. □

4.2.9. By Klein [Kl1887], the action A7 ⟲ P3 is solvably versal. As a result,
Hilbert’s 13th problem is equivalent to the assertion that the cover P3 → P3/A7 is
a normal form of minimal dimension.

Question 4.2.10. Is there a congruence cover XΓ′ → XΓ with Galois group A7 and
dim XΓ = 3 which is also E-versal for one of the classes of accessory irrationalities
considered in Example 4.1.5?

24 BENSON FARB, MARK KISIN AND JESSE WOLFSON

Finding such a congruence cover would give the transcendental part of Klein’s 3-
variable solution of the degree 7, as in [Kl1884, Chapter 5.9]. Note that Prokhorov’s
classiﬁcation [Pro12, Theorem 1.5] of ﬁnite simple groups acting birationally on
rationally connected 3-folds gives strong constraints on any possible congruence
cover.

Question 4.2.11. Is there a congruence cover XΓ′ → XΓ with Galois group A8 and
dim XΓ = 4 which is also E-versal for one of the classes of accessory irrationalities
considered in Example 4.1.5?

4.2.12. As Propositions 4.2.5 and 4.2.8 show, for g = 2, 3 the Sp2g(F2)-variety Ag,2
is G-versal for any subgroup G ⊂ Sp2g(F2). Hence for n = 6, 7, 8 the resolvent degree
of the cover Adn,2 → Adn,An is equal to RD(n), as deﬁned in the introduction.
Interestingly, Hilbert’s conjectured value for resolvent degree, and the value of the
essential dimension at 2 for these covers, almost agree :

n 6 7 8 9
Hilbert: RD(n) 2 3 4 4
ed(An; 2) 2 2 4 4

Note that in these cases the value of ed(Adn,2 → Adn,An; 2) = ed(An; 2) is already
given by Proposition 3.2.2, except when n = 8 and g = 3, in which case Proposi-
tion 3.2.2 gives the lower bound 3. The actual value ed(A3,2 → A3,A8 ; 2) = 4 follows
from versality (e.g. from Lemma 4.1.12 applied to the modular cover A4,2 → A4,A8
arising from the diagonal representation of A8 = SL4(F2); the ed at 2 of this cover
follows from Corollary 3.1.3).

Appendix A. On quadratic representations of Sn

By Nate Harman

A.1. Statement of Results. Recall that any linear representation of a p-group G
over a ﬁeld k of characteristic p contains a non-zero invariant vector, in particular
this implies that the only irreducible representation of G over k is the trivial repre-
sentation. This does not mean that all representations are trivial though, there are
non-split extensions of trivial representations and understanding their structure is
a central part of modular representation theory.
In a non-semisimple setting, one basic invariant of a representation is its Lowey
length. For representations of p-groups in characteristic p it can be deﬁned as
follows: Start with a representation V and then quotient it by its space of invariants
to obtain a new representation V ′ = V /V G, then repeat this process until the
quotient is zero. The Lowey length is the number of steps this takes.
In the above work Farb, Kisin, and Wolfson analyze certain special represen-
tations of symmetric groups in characteristic 2, the so-called Dickson embeddings.
Typically denoted D(n−1,1) in the representation theory literature, these representa-
tions have the following key property: Let n = 2m or 2m + 1, these representations
have Lowey length 2 when restricted to the rank m (which is the maximum possible)
elementary abelian 2-subgroup Hn generated by (1, 2), (3, 4), . . . , and (2m−1, 2m).
This motivates the following deﬁnition: We say that an irreducible representation
of a Sn in characteristic p is quadratic with respect to a maximal rank elementary
abelian p-subgroup H if it has Lowey length 2 upon restriction to H. The purpose
of this note is to prove ﬁrst that this is only a characteristic 2 phenomenon, and

MODULAR FUNCTIONS AND RESOLVENT PROBLEMS 25

second that these representations D(n−1,1) are the only representations which are
quadratic with respect to some maximal rank elementary abelian p-subgroup for n
suﬃciently large (n ≥ 9).

In characteristic p > 2, the maximal rank elementary abelian p-subgroups in Sn
are just those generated by a maximal collection of disjoint p-cycles. Our ﬁrst main
theorem tells us that there are no quadratic representations in characteristic p > 2,
and in fact we can detect the failure to be quadratic here by restricting to a single
p-cycle.

Theorem A.1. Any irreducible representation of Sn with n ≥ p in characteristic
p > 2 which is not a character has Lowey length at least 3 upon restriction to the
copy of Cp generated by (1, 2, . . . , p), and therefore is not quadratic with respect to
any maximal rank elementary abelian p-subgroup.

Note that in any characteristic p > 2 the characters of Sn are just the trivial
and sign representations.

In characteristic 2 things are a bit more complicated. While the subgroup Hn
of Sn is a maximal rank elementary 2-subgroup, it is no longer the unique such
subgroup up to conjugation. Recall that in S4 there is the Klein four subgroup
K = {e, (12)(34), (13)(24), (14)(23)}, which is a copy of C2
2 not conjugate to H4.
We can construct other maximal rank elementary 2-subgroups of Sn by taking
products

K × K × · · · × K
︸ ︷︷ ︸
m times ×Hn−4m ⊂ S4 × S4 × · · · × S4︸ ︷︷ ︸
m times
 ×Sn−4m ⊂ Sn

and up to conjugacy though these are all the maximal rank elementary abelian
2-subgroups inside Sn.
S8 has a special irreducible representation D(5,3) of dimension 8 which upon
restriction A8 decomposes as a direct sum D(5,3)+ ⊕ D(5,3)− of two representations
of dimension 4. These representations realize the “exceptional” isomorphism A8 ∼=
GL4(F2), or rather they realize two diﬀerent isomorphisms diﬀering by either by
conjugating A8 by a transposition in S8 or by the inverse-transpose automorphism
of GL4(F2). Under this isomorphism the subgroup K × K ⊂ A8 gets identiﬁed with
the subgroup of matrices of the form






1 0 a b
0 1 c d
0 0 1 0
0 0 0 1






which is manifestly quadratic. Our second main theorem will be to show that there
are no other quadratic representations other than the Dickson embedding once n
is at least 9.

Theorem A.2. Suppose V is a non-trivial irreducible representation of Sn with
n ≥ 9 over a ﬁeld of characteristic 2 which is quadratic with respect to a maximal
rank elementary abelian 2-subgroup H. Then V ∼= D(n−1,1), and H is conjugate to
Hn.

26 BENSON FARB, MARK KISIN AND JESSE WOLFSON

A.2. Proofs of Main Theorems. We will be assuming a familiarity with the
modular representation theory of symmetric groups. A standard reference for this
material the book [Jam78] of James, which we will be adopting the notation from
and referring to for all the basic results we need. The irreducible representations
of Sn in characteristic p are denoted by Dλ, for p-regular partitions λ of n. These
arise as quotients of the corresponding Specht modules Sλ, which are well behaved
reductions of the ordinary irreducible representations in characteristic zero.

A.2.1. Proof of Theorem A.1. First we will reduce the problem to just looking at
representations of Sp. For that we have the following lemma:

Lemma A.2.1.

(1) Every irreducible representation V of Sn with n ≥ p in characteristic p > 3
which is not a character has a composition factor when restricted to Sp
which is not a character.
(2) Every irreducible representation V of Sn with n ≥ 4 in characteristic 3
which is not a character has a composition factor when restricted to S4
which is not a character.

Proof: For part (a) suppose V only has composition factors which are characters
when restricted to Sp. If we restrict this to the alternating group Ap all the com-
position factors must be trivial, as Ap only has the trivial character. If we further
restrict to Ap−1 the whole action must be trivial because representations of Ap−1
are semisimple in characteristic p. However if the action of Ap−1 is trivial on V
then so is the action of the entire normal subgroup generated by Ap−1 inside Sn,
which we know is all of An if n > 3. So V must be the trivial as a representation
of An, and is therefore a character of Sn.
For part (b), let’s again suppose V only has composition factors that are char-
acters when restricted to S4, which implies it only has trivial composition factors
when restricted to A4. If we further restrict to the Klein four subgroup K the whole
action must be trivial because representations of K are semisimple in characteristic
p ̸= 2. As before we see V must be trivial for the normal subgroup of Sn generated
by K, which we know is all of An for n > 4. Therefore V is a character. □

Remark: The modiﬁcation for characteristic 3 is necessary because in character-
istic 3 the only irreducible representations of S3 are the trivial and sign represen-
tations. Theorem A.1 holds vacuously in this case.

It is now enough to prove Theorem A.1 for Sp in characteristic p > 3, and for S4
in characteristic 3. Let’s ﬁrst focus on the case where p > 3. If λ is a p-core, then
Nakayama’s conjecture (which is actually a theorem, see [Jam78] Theorem 21.11)
tells us Dλ = Sλ is projective, and hence remains projective when restricted to
Cp and therefore has Lowey length p. This leaves those irreducible representations
corresponding to hook partitions λ = (p − k, 1k).
In the simplest case where λ = (p − 1, 1) then Dλ is the (p − 2)-dimensional
quotient of the standard (p − 1)-dimensional representation S(p−1,1) by its one
dimensional space of invariants, and one can easily verify this forms a single (p − 2)-
dimensional indecomposable representation of Cp. Peel explicitly computed the
decomposition matrices for Sp in characteristic p (see [Jam78] Theorem 24.1), and
it follows from his calculation that the remaining irreducible representations Dλ

MODULAR FUNCTIONS AND RESOLVENT PROBLEMS 27

with λ = (p − k, 1k) for 1 < k ≤ p − 2 are just exterior powers ΛkD(p−1,1) of this
(p − 2)-dimensional representation.
Since k < p we know that ΛkD(p−1,1) is a direct summand of (D(p−1,1))
⊗k,
which as a representation of Cp is just the unique (p − 2)-dimensional indecompos-
able representation tensored with itself k times. Tensor product decompositions for
representations of cyclic groups are known explicitly ([Gre62] Theorem 3), and in
particular it is known that a tensor product of two odd dimensional indecomposable
representations of Cp always decomposes as a direct sum of odd dimensional inde-
composable representations. So we see (D(p−1,1))
⊗k and ΛkD(p−1,1) = D(p−k,1
k)

only have odd length indecomposable factors when restricted to Cp. If it had Lowey
length 1 when restricted to Cp that means the action is trivial, which implies the
action of Ap must also be trivial as Ap is simple, but that would imply the original
representation of Sn was a character.
In the characteristic 3 case there are only two irreducible representations of
S4, they are the standard 3-dimensional representation S(3,1) = D(3,1) and its
sign twisted version S(2,1,1) = D(2,1,1). These are 3-core partitions so again by
Nakayama’s conjecture they are both projective and therefore remain projective
when restricted to C3 and have Lowey length 3. □

A.2.2. Proof of Theorem A.2. The overall structure of the proof will be to succes-
sively rule diﬀerent classes of representations and maximal rank elementary abelian
2-subgroups through a sequence of lemmas. The ﬁrst such lemma will let us rule
out those irreducible representations Dλ where λ is a 2-regular partition with at
least 3 parts.

Lemma A.2.2. If λ is a 2-regular partition with at least 3 parts, then the irreducible
representation Dλ of Sn contains a projective summand when restricted to S6.

Proof: Note that any 2-regular partition λ with at least 3 parts can be writ-
ten as (3, 2, 1) + µ = (µ1 + 3, µ2 + 2, µ3 + 1, µ4, . . . , µℓ) for some partition µ =
(µ1, µ2, . . . , µℓ). James and Peel [PJ79] constructed explicit Specht ﬁltrations for
Ind
Sn
S6×Sn−6(S(3,2,1) ⊗ Sµ), which have Sλ as the top ﬁltered quotient. In particular
this implies Ind
Sn
S6×Sn−6(S(3,2,1) ⊗ Sµ) has Dλ as a quotient. However by Frobenius
reciprocity we know that

HomSn(Ind
Sn
S6×Sn−6(S(3,2,1)⊗Sµ), Dλ) ∼= HomS6×Sn−6(S(3,2,1)⊗Sµ, ResSn
S6×Sn−6(Dλ)).

So since the left hand side is nonzero, the right hand side is as well.
Now if we look at S(3,2,1) ⊗ Sµ as a representation of S6 it is just a direct
sum of dim(Sµ) copies of S(3,2,1), which we know is irreducible and projective by
Nakayama’s conjecture. In particular the image under any nonzero homomorphism
is also just a direct sum of copies of S(3,2,1), so Dλ must contain at least one copy
of S(3,2,1) as a direct summand. □

Corollary A.3. If λ is a 2-regular partition with at least 3 parts, then Dλ is not
quadratic with respect to any maximal rank elementary abelian 2-subgroup of Sn.

Proof: After conjugating we may assume that our maximal rank elementary
abelian subgroup intersects S6 in an elementary abelian 2-group of rank at least 2.
The previous lemma says any such irreducible representation must contain projec-
tive summand when restricted to S6, and then this summand remains projective

28 BENSON FARB, MARK KISIN AND JESSE WOLFSON

upon restriction to the intersection of S6 with our maximal rank elementary 2-
subgroup. Projective representations of C2
2 have Lowey length 3, so the Lowey
length for the entire maximal rank elementary abelian 2-subgroup of Sn must be
at least that big. □

This reduces the problem to understanding what happens for two-part partitions
λ = (a, b). These representations are much better understood then the general case.
For one thing, the branching rules for restriction are completely known in this case,
although we’ll just need the following simpliﬁed version:

Lemma A.3.1. (See [Kle98] Theorem 3.6, following [She99]) If (a, b) is a two-part
partition of n with a− b > 1 then D(a−1,b) appears as a subquotient with multiplicity
one inside the restriction of D(a,b) to Sn−1, and the other composition factors are
all of the form D(a−1+r,b−r) with r > 0.

Recall that we deﬁned H2k ⊂ S2k to be the elementary abelian 2-subgroup of S2k
generated by the odd position adjacent transpositions (2i − 1, 2i) for 1 ≤ i ≤ k, we
will also consider H2k as a subgroup of Sn for n > 2k via the standard inclusions of
S2k into Sn. The next lemma will be to settle for us exactly which representations
are have Lowey length 2 when restricted to the standard maximal rank elementary
abelian subgroup Hn.

Lemma A.3.2. D(n−k,k) contains a projective summand when restricted to H2k.

Proof: We know from the branching rules (Lemma A.3.1) that D(n−k,k) contains
a copy of D(k+1,k) as a subquotient when restricted to S2k+1, so it is enough to
verify it for D(k+1,k). Moreover H2k ⊂ S2k so really this calculation is taking place
inside M (2k) := Res
S2k+1
S2k D(k+1,k).
These representations D(k+1,k) and M (2k) are well studied. Benson proved
D(k+1,k) is a reduction modulo 2 of the so-called basic spin representation of S2k+1
in characteristic zero ([Ben88] Theorem 5.1). Nagai and Uno ([Uno02] Theorem 2,
or see [Oku08] Proposition 3.1 for an account in English), gave explicit matrix pre-
sentations for M (2k) and showed that they have the following recursive structure:

Res
S2m
S2i×S2m−2iM (2m) ∼= M (2i) ⊗ M (2m − 2i)

In particular since M (2) can easily be seen to be the regular representation of
S2 = H2, it follows by induction that M (2k) is projective (and just a single copy
of the regular representation) for H2k. □

Corollary A.4. The only nontrivial irreducible representation of Sn which is qua-
dratic with respect to Hn is D(n−1,1).

Proof: Corollary A.3 tells us that if λ has at least 3 parts, Dλ has Lowey length
at least 3 when restricted to Hn. Then Lemma A.3.2 tells us that D(n−k,k) has
Lowey length at least k + 1 as a Hn representation and is therefore not quadratic
for k > 1. □

To ﬁnish the proof of Theorem A.2 we need to show that for n at least 9 that
there are no representations which are quadratic with respect to to any of these
other maximal rank elementary abelian 2-subgroups K m × Hn−4k with m ≥ 1.
Lemma A.3 rules out Dλ for λ of length at least 3, so again we will just need to
address the case when λ is a length 2 partition.

MODULAR FUNCTIONS AND RESOLVENT PROBLEMS 29

We do this through a series of lemmas ruling out diﬀerent cases, but ﬁrst will state
the following well-known fact from the modular representation theory of symmetric
groups:

Lemma A.4.1. ([Jam78] Theorem 9.3) If λ is a partition of n, then Sλ restricted
to Sn−1 admits a ﬁltration

0 = M0 ⊂ M1 ⊂ · · · ⊂ MN ∼= Sλ

such that the successive quotients Mi/Mi−1 are isomorphic to Specht modules Sµ,
and Sµ appears if and only if µ is obtained from λ by removing a single box, in
which case it appears with multiplicity one.

Lemma A.4.2. D(n−1,1), for n ≥ 5, contains a projective summand when re-
stricted to K, and is therefore not quadratic with respect to any group containing
K.

Proof: It suﬃces to prove it for D(4,1) as every D(n−1,1) for n > 5 contains it as
a composition factor upon restriction to S5 by Lemma A.3.1. This representation
D(4,1) is just the 4 dimensional subspace of F5
2 where the sum of the coordinates is
zero. If we restrict this representation to S4 this can be identiﬁed with the standard
4-dimensional permutation representation via the map (a, b, c, d) → (a, b, c, d, −a −
b − c − d). The restriction of the standard action of S4 on a 4-element set to K is
simply transitive, so this representation is just a copy of the regular representation.
□

Lemma A.4.3. D(n−2,2) for n ≥ 7 and D(n−3,3) for n ≥ 9 each contain a projective
summand when restricted to K, and are therefore not quadratic with respect to any
group containing K.

Proof: It suﬃces to prove it for D(5,2) and D(6,3) as every D(n−2,2) for n > 7
contains D(5,2) as a composition factor upon restriction to S7, and similarly every
D(n−2,2) for n > 7 contains D(6,3) as a composition factor upon restriction to S9
by Lemma A.3.1.
For S7 and S9 the decomposition matrices are known explicitly and we have
that D(5,2) = S(5,2) and D(6,3) = S(6,3) (see the appendix of [Jam78]). For Specht
modules the branching rules are given by Lemma A.4.1 and S(5,2) and S(6,3) both
contain S(4,1) as a subquotient upon restriction to S5. The result then follows from
the previous lemma. □

Lemma A.4.4. D(n−k,k) for k ≥ 4 and n ≥ 2k + 1 is not quadratic when restricted
to K m × Hn−4m for any m ≥ 1.

Proof: We know by Lemma A.3.2 these are projective upon restriction to H2k, and
are therefore projective when restricted to the intersection of H2k with K m×Hn−4m.
This intersection has rank at least 2 since k ≥ 4, and therefore projective objects
have Lowey length at least 3. □

This completes the proof of Theorem A.2. □

30 BENSON FARB, MARK KISIN AND JESSE WOLFSON

A.3. Modiﬁcations for An. We will now brieﬂy describe what changes if we work
with alternating groups instead of symmetric groups, but we will omit some of the
details of the calculations. First a quick summary of the modular representation
theory of alternating groups in terms of the theory for symmetric groups:
Upon restriction from Sn to An, the irreducible representations Dλ either remain
irreducible, or split as a direct sums Dλ ∼= Dλ+ ⊕ Dλ− of two irreducible non-
isomorphic representations of the same dimension; all irreducible representations
of An are uniquely obtained this way. We’ll note that in characteristic p > 2 this
is a standard application of Cliﬀord theory, but in characteristic 2 it is a diﬃcult
theorem of Benson ([Ben88] Theorem 1.1). Moreover it is known exactly which Dλ

split this way, but we won’t go into the combinatorics here.
When p > 2 the maximum rank abelian p-groups in Sn all lie in An, and the proof
of Theorem A.1 goes through without modiﬁcation to give the following theorem.

Theorem A.1’. Any non-trivial irreducible representation of An with n ≥ p in
characteristic p > 2 has Lowey length at least 3 upon restriction to the copy of
Cp generated by (1, 2, . . . , p), and is therefore not quadratic with respect to any
maximal rank elementary abelian p-subgroup.

When p = 2, the diﬀerence is more dramatic. It is no longer true that every
maximum rank abelian 2-subgroup of Sn lies in An, in particular Hn is not a
subgroup of An. Let ˜Hn denote the intersection of Hn and An, this has rank one
less than Hn. The maximal rank elementary abelian 2-subgroups of An are as
follows:
If n = 4b or 4b + 1 then up to conjugacy the only maximal rank elementary
abelian 2-subgroup inside An is K b, and it is of rank 2b. If n = 4b + 2 or 4b + 3
then all maximal rank elementary abelian 2-subgroups in Sn still have maximal
rank when intersected with An, and up to conjugacy the maximal rank elementary
abelian 2-subgroups inside An are of the form:

K × K × · · · × K
︸ ︷︷ ︸
m times × ˜Hn−4m ⊂ A4 × A4 × · · · × A4︸ ︷︷ ︸
m times
 ×An−4m ⊂ An

and these have rank 2b − 1.
The appropriate modiﬁcation to Theorem A.2 for alternating groups is the fol-
lowing:

Theorem A.2’. Suppose V is a non-trivial irreducible representation of An with
n ≥ 9 over a ﬁeld of characteristic 2 which is quadratic with respect to a maximal
rank elementary abelian 2-subgroup H. Then n ≡ 2 or 3 modulo 4, V ∼= D(n−1,1),
and H is conjugate to ˜Hn.

The proof of Theorem A.2 mostly goes through in this case. Some additional care
is needed to handle the representations Dλ+ and Dλ− which are not restrictions
of irreducible representations of Sn, however one simplifying observation is that
since Dλ+ and Dλ− just diﬀer by conjugation by a transposition, they are actually
isomorphic to one another upon restriction to a maximal rank elementary abelian
2-subgroup. We will omit the remaining details though.

MODULAR FUNCTIONS AND RESOLVENT PROBLEMS 31

References

[ABL+19] Rachel Abbot, John Bray, Steve Linton, Simon Nickerson, Simon Norton, Richard
Parker, Ibrahim Suleiman, Jonathan Tripp, Peter Walsh, and Robert Wilson, Atlas of
ﬁnite group representations, v.3, http://brauer.maths.qmul.ac.uk/Atlas/v3/, 2019.
[ACT02] Daniel Allcock, James Carlson, and Domingo Toledo, The Complex Hyperbolic Geom-
etry of the Moduli Space of Cubic Surfaces, J. Alg. Geo. 11 (2002), 659–754.
[AS76] Vladimir Arnold and Goro Shimura, Superpositions of algebraic functions, Proc. Sym-
posia in Pure Math. 28 (1976), 45–46.
[Bar79] Michael J. J. Barry, Large abelian subgroups of Chevalley groups, J. Austral. Math.
Soc. Ser. A 27 (1979), no. 1, 59–87.
[Ben88] Dave Benson, Spin modules for symmetric groups, Journal of the London Mathematical
Society 38 (1988), no. 2, 250-262.
[Bra75] Richard Brauer, On the resolvent problem, Ann. Mat. Pura Appl. 102 (1975), 45–55.
[BFR] Patrick Brosnan, Najmudden Fakrhuddin, and Zinovy Reichstein, Fixed points in
toroidal compactiﬁcations of Shimura varieties and essential dimension of congruence
covers, In preparation.
[BR97] J. Buhler and Z. Reichstein, On the essential dimension of a ﬁnite group, Compositio
Math. 106 (1997), no. 2, 159–179.
[BR99] , On Tschirnhaus transformations, Topics in number theory (University Park,
PA, 1997) 467 (1999), no. 2, 127–142.
[Bu1890] Heinrich Burkhardt, Grundz¨uge einer allgemeinen Systematik der hyperelliptischen
Functionen I. Ordnung, Math. Ann. 35 (1890), 198-296.
[Bu1891] , Untersuchungen aus dem Gebiete der hyperelliptischen Modulfunctionen.
Zweiter Teil., Math. Ann. 38 (1891), 161-224.
[Bu1893] , Untersuchungen aus dem Gebiete der hyperelliptischen Modulfunctionen. III.,
Math. Ann. 41 (1893), 313-343.
[Che32] N.G. Chebotarev, Die Probleme der modernen Galoisschen Theorie, Proceedings of
the ICM (1932).
[Che43] , The problem of resolvents and critical manifolds, Izvestia Akad. Nauk SSSR
7 (1943), 123–146.
[Dic08] L.E. Dickson, Representations of the General Symmetric Group as Linear Groups in
Finite and Inﬁnite Fields, Trans. AMS 9 (1908), no. 2, 121–148.
[DO88] Igor Dolgachev and David Ortland, Point Sets in Projective Spaces and Theta Func-
tions, 1988.
[DR15] Alexander Duncan and Zinovy Reichstein, Versality of algebraic group actions and
rational points on twisted varieties, J. Alg. Geom. 24 (2015), 499–530.
[DR14] , Pseudo-reﬂection groups and essential dimension, J. Lond. Math. Soc. 90
(2014), no. 3, 879–902.
[DR15] , Versality of algebraic group actions and rational points on twisted varieties,
J. Algebraic Geom. 24 (2015), no. 3, 499–530.
[FC90] Gerd Faltings and Ching-Li Chai, Degeneration of abelian varieties, Ergebnisse der
Mathematik und ihrer Grenzgebiete (3) [Results in Mathematics and Related Areas
(3)], vol. 22, Springer-Verlag, Berlin, 1990. With an appendix by David Mumford.
[FKW19] Benson Farb, Mark Kisin, and Jesse Wolfson, Essential dimension of congruence cov-
ers, arXiv:1901.09013 (2019).
[FW18] Benson Farb and Jesse Wolfson, Resolvent degree, Hilbert’s 13th Problem and Geom-
etry, arXiv:1803.04063 (2018).
[Fri26] Robert Fricke, Lehrbuch der Algebra, Vol. 2, Viewig und Sohn, Braunschweig, 1926.
[FK12] Robert Fricke and Felix Klein, Vorlesungen ¨uber die Theorie der automorphen Func-
tionen, Vol. 1,2, Teubner, Berlin, 1912.
[GMS03] Skip Garibaldi, Alexander Merkurjev, and J.P. Serre, Cohomological invariants in Ga-
lois cohomology, University Lecture Series, vol. 28, American Mathematical Society,
Providence, RI, 2003.
[vdG88] Gerard van der Geer, Hilbert Modular Surfaces, Springer-Verlag, 1988.
[Go1882] Paul Gordan, Ueber Gleichungen siebenten Grades mit einer Gruppe von 168 Substi-
tutionen, Math. Ann. 20 (1882), 515-530.

32 BENSON FARB, MARK KISIN AND JESSE WOLFSON

[Gre62] J.A. Green, The modular representation algebra of a ﬁnite group, Illinois Journal of
Mathematics 6 (1962), no. 4, 607-619.
[Gro00] L.C. Grove, Classical groups and Geometric Algebra, Graduate Studies in Math.,
vol. 39, AMS, 2000.
[He1858] C. Hermite, Sur la r´esolution de l’equation du cinqui`eme degr´e, Comptes rendus de
l’Acad´emie des Sciences 46 (1858), 508–515.
[Hi1900] David Hilbert, Mathematical Problems, Proceedings of the 1900 ICM, English transla-
tion reprinted in Bull. AMS 37 (2000), no. 4, 407–436.
[Hil27] , ¨Uber die Gleichung neunten Grades, Math. Ann. 97 (1927), no. 1, 243–250.
[Hir76] Friedrich Hirzebruch, Hilbert’s Modular Group of the Field Q(
√5) and the Cubic Di-
agonal Surface of Clebsch and Klein, Russ. Math. Surv. 31 (1976), no. 5, 153-166.
[Hir77] , The Ring of Hilbert Modular Forms for Real Quadratic Fields of Small Dis-
criminant, Modular functions of one variable, VI (Proc. Second Internat. Conf., Univ.
Bonn, Bonn, 1976) Lecture Notes in Math., 627 (1977), 287-323.
[Hun96] Bruce Hunt, The geometry of some special arithmetic quotients, Springer Lect. Notes
in Math., vol. 1637, 1996.
[KM08] Nikita A. Karpenko and Alexander S. Merkurjev, Essential dimension of ﬁnite p-
groups, Invent. Math. 172 (2008), no. 3, 491–508.
[Kl1871] Felix Klein, Ueber eine geometrische Repr¨asentation der Resolventen algebraischer
Gleichungen, Math. Ann. 4 (1871), 346-358.
[Kl1879] , Ueber die Auﬂ¨osung gewisser Gleichungen vom siebenten und achten Grade,
Math. Ann. 15 (1879), 252-282.
[Kl1884] , Vorlesungen ¨uber das Ikosaeder und die Auﬂ¨osung der Gleichungen vom fnften
Grade (Lectures on the Icosahedron and the Solution of the Equation of the Fifth
Degree), Leipzig, T¨ubner, 1884.
[Kl1887] , Zur Theorie der allgemeinen Gleichungen sechsten und siebenten Grades,
Math. Ann. 28 (1887), 499-532.
[Kl1888] , Sur la resolution, par les fonctions hyperelliptiques de l’equation du vingt-
septieme degre, de laquelle depend la determination des vingt-sept droites d’une surface
cubique, Journal de Math´ematiques pures et appliqu´ees 4 (1888), 169-176.
[Kl1893] , Lectures on Mathematics, MacMillan and Co., 1894.
[Kle05] , ¨Uber die Auﬂ¨osung der allgemeinen Gleichungen f¨unften und sechsten Grades,
Journal f¨ur die reine und angewandte Mathematik 129 (1905), 150-174.
[Kle26] , Vorlesungen uber die Entwicklung der Mathematik im 19. Jahrhundert,
Springer, Berlin, 1926.
[Kle22a] , Gesammelte Mathematische Abhandlungen, Vol. 2, Berlin, 1922.
[Kle22b] , Gesammelte Mathematische Abhandlungen, Vol. 3, Berlin, 1922.
[KF1892] Felix Klein and Robert Fricke, Vorlesungen ¨uber die Theorie der elliptischen Modul-
funktionen, Vol. 1,2, Teubner, Leipzig, 1892.
[Kle98] A.S. Kleshchev, Branching rules for symmetric groups and applications, in Algebraic
Groups and their Representations (R.W. Carter and J. Saxl eds.), Springer, Dordrecht,
1998, pp. 103-130.
[Kon13] Shigeyuki Kondo, The Segre cubic and Borcherds products, Arithmetic and geometry
of K3 surfaces and Calabi-Yau threefolds 67 (2013), 549–565.
[Kr1861] Leopold Kronecker, Ueber die Gleichungen f¨unften Grades, Journal f¨ur die reine und
angewandte Mathematik 59 (1861), 306–310.
[Jam78] G.D. James, The Representation Theory of Symmetric Groups, Lecture Notes in Math-
ematics, vol. 682, Springer, 1978.
[Lan19] Aaron Landesman, The Torelli map restricted to the hyperelliptic locus,
arXiv:1911.02084 (2019).
[Mer17] Alexander Merkurjev, Essential dimension, Bull. AMS 54 (2017), no. 4, 635–661.
[MS83] Alexander Merkurjev and Andrei Suslin, K-Cohomology of Severi-Brauer Varieties
and the Norm Residue Homomorphism, Math. USSR Izv. 21 (1983), no. 2, 307–340.
[MR09] A. Meyer and Z. Reichstein, The essential dimension of the normalizer of a maximal
torus in the projective linear group, Algebra & Number Theory 3 (2009), no. 4, 467–
487.
[Oku08] Tetsuro Okuyama, On a certain simple module and cohomology of the symmetric group
over GF (2), Kyoto University Department Bulletin 1581 (2008), no. 58-63.

MODULAR FUNCTIONS AND RESOLVENT PROBLEMS 33

[PJ79] M.H. Peel and G.D. James, Specht series for skew representations of symmetric groups,
Journal of Algebra 56 (1979), no. 2, 343-364.
[Pro12] Yuri Prokhorov, Simple ﬁnite subgroups of the Cremona group of rank 3, J. Algebraic
Geom. 21 (2012), no. 3, 563-600.
[Rei10] Zinovy Reichstein, Essential Dimension, Proceedings of the International Congress of
Mathematicians, 2010.
[RY00] Zinovy Reichstein and Boris Youssin, Essential dimensions of algebraic groups and a
resolution theorem for G-varieties, Canad. J. Math. 52 (2000), no. 5, 1018–1056. With
an appendix by J´anos Koll´ar and Endre Szab´o.
[SBT97] Nick Shepherd-Barron and Richard Taylor, Mod 2 and Mod 5 Icosahedral Representa-
tions, J. Amer. Math. Soc. 10 (1997), no. 2, 283–298.
[She99] Jagat Sheth, Branching rules for two row partitions and applications to the inductive
systems for symmetric groups, Communications in Algebra 27 (1999), no. 9, 3303-3316.
[Shi64] Goro Shimura, On purely transcendental ﬁelds of automorphic functions of several
variables, Osaka Jour. Math. 1 (1964), 1–14.
[Tay92] D.E. Taylor, Geometry of the Classical Groups, Sigma Series in Pure Math., vol. 9,
Helderberg Verlag Berlin, 1992.
[Uno02] K. Uno, The rank variety of a simple module of a symmetric group, RIMS Kokyuroku
1251 (2002), 8-15.
[Wag76] A Wagner, The Faithful Linear Representation of Least Degree of Sn and An over a
Field of Characteristic 2, Math. Z. 151 (1976), 127–137.
[Wag77] , The Faithful Linear Representation of Least Degree of Sn and An over a Field
of Odd Characteristic, Math. Z. 154 (1977), 103–114.
[Wol] Jesse Wolfson, Tschirnhaus transformations after Hilbert, Preprint available at
https://jpwolfson.com/articles-and-pre-prints/.

Department of Mathematics, University of Chicago
E-mail address: farb@math.uchicago.edu

Department of Mathematics, Harvard
E-mail address: kisin@math.harvard.edu

Department of Mathematics, University of California-Irvine
E-mail address: wolfson@uci.edu

Department of Mathematics, University of Chicago
E-mail address: nateharman1234@gmail.com
