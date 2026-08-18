<!-- source: https://arxiv.org/pdf/2001.06515 | converted from PDF -->

arXiv:2001.06515v2  [math.AG]  22 Feb 2021
Tschirnhaus transformations after Hilbert

Jesse Wolfson
∗

February 24, 2021

Abstract

In this paper, we use enumerative geometry to simplify the formula for the roots of
the general one-variable polynomial of degree n, for all n. More precisely, let RD(n)
denote the minimum d for which there exists a formula for the roots of the general
degree n polynomial using only algebraic functions of d or fewer variables. In 1927,
Hilbert sketched how the 27 lines on a cubic surface could be used to construct a 4-
variable formula for the general degree 9 polynomial (implying RD(9) ≤ 4). In this
paper, we turn Hilbert’s sketch into a general method. We show this method produces
best-to-date upper bounds on RD(n) for all n, improving earlier results of Hamilton,
Sylvester, Segre and Brauer.

1 Introduction

The goal of this paper is to use enumerative geometry to produce simplest-to-date formulas
for the roots of the general one-variable polynomial of degree n, for all n. Consider the
problem of ﬁnding the roots of a polynomial

zn + a1zn−1 + · · · + an = 0

in terms of the coeﬃcients a1, . . . , an. A priori, the assignment

(a1, . . . , an) ↦→ {z | zn + a1zn−1 + · · · + an = 0}

is an algebraic function of n (complex) variables, and it is natural to ask whether there
exists a formula using only algebraic functions of d or fewer variables. Call the minimum
such d the resolvent degree and denote this by RD(n) (see Section 4 for a precise deﬁnition,
and [FW19] for a detailed treatment). At present, no nontrivial lower bounds for RD(n) are
known. The best general upper bounds in the literature are due to Brauer [Br75], who uses
methods dating to Tschirnhaus [Ts1683] to prove that RD(n) ≤ n − r for n ≥ (r − 1)! + 1.
As Brauer remarks, his bounds are not optimal for small r.1

In this paper we take a diﬀerent approach to bounding RD(n), inspired by a geometric
argument of Hilbert. In [Hi27], Hilbert sketches how the 27 lines on a cubic surface can be
used to produce a 4-variable formula for the general degree 9 polynomial, i.e. RD(9) ≤ 4.

∗Supported in part by NSF Grant DMS-1811846.
1Brauer’s ﬁrst improvement over prior bounds occurs for r = 7.

1

We turn Hilbert’s sketch into a general method, whereby lines on cubic surfaces are replaced
by r-planes on degree d hypersurfaces in Pm for appropriate choices of r, d and m. This
deﬁnes an explicit increasing function F : N // N (Deﬁnition 5.4) for which we prove the
following:

Theorem 1.1. Let F : N // N be the function deﬁned in Deﬁnition 5.4.

1. For all r and all n ≥ F(r), RD(n) ≤ n − r.

2. For all r, n = F(r) is the least value for which we know RD(n) ≤ n − r to hold.2 In
particular, the initial values are given by

r 1 2 3 4 5 6 7
F(r) 2 3 4 5 9 41 121

3. Writing B(r) = (r − 1)! + 1 for Brauer’s bound, then

lim
r→∞ B(r)/ F(r) = ∞.

The ﬁrst statement appears as Theorem 5.6 below, while the last two appear as Theorem 5.8.

Remark 1.2.

1. The construction of F, the proof that F(5) = 9 and that this implies RD(9) ≤ 4
marks the ﬁrst rigorous construction of the 4-variable formula for the general degree
9 sketched by Hilbert in [Hi27].3

2. The ﬁrst improvement over prior bounds occurs at F(6) = 41. Previously, Sylvester
proved [Sy1887, p. 485] that for n ≥ 44, RD(n) ≤ n − 6.

Besides the general interest in obtaining simpler formulas for polynomials, we hope this
paper spurs work on two questions. For the ﬁrst, we quote Dixmier [Di93, p. 90]4:

“Every reduction of RD(n) would be serious progress. In particular, it is time
to know if RD(6) = 1 or RD(6) = 2.” (Dixmier, 1993)

While the present methods cannot touch Hilbert’s Sextic Conjecture (RD(6) = 2), they do
contribute to Dixmier’s call to lower the possible values of RD(n). They also contribute to
a problem ﬁrst posed (as far as we are aware) by Segre [Se51, III.5]:

Problem 1.3. Understand the large n behavior of RD(n).

As a clearer understanding of Segre’s problem comes into view, we look forward to seeing
the present bounds lowered in turn.

2i.e. n = F(r) is the least value for which RD(n) ≤ n − r is currently proven to hold in any of the
literature of which we are aware. Note that G. Chebotarev [Ch54] claimed to have extended an argument
of Wiman [Wi27] to conclude RD(n) ≤ n − 6 for n ≥ 21. His proof has gaps similar to those observed by
Dixmier [Di93] in the arguments of Hilbert and Wiman, namely he takes for granted that certain forms are
generic, when they are not.
3Rigorous 4-variable formulas have been previously constructed by Segre [Se45] and Dixmier [Di93].
4n.b. Dixmier writes “s(n)” for our RD(n).
 2

Remarks on the Proof. Given a polynomial

p(z) = zn + a1zn−1 + · · · + an =
 n∏

i=1(z − zi),

a Tschirnhaus transformation is a “change of variables”

y =
 n−1∑

j=0 bjzj.

This gives a new polynomial

q(y) = ∏

i (y −
 n−1∑

j=0 bjzj
i ) = yn + c1yn−1 + · · · + cn,

and we can ask for Tschirnhaus transformations which normalize the resulting polynomial
so that, e.g. c1 = · · · = ck = 0. (1.1)

The space of all (b0, . . . , bn−1) such that the conditions (1.1) are satisﬁed forms an aﬃne
cone, and the projectivization gives a complete intersection

T n
1···k ⊂ Pn−1;

when the superscript n is clear from context, we suppress it and write T1···k. If we can
ﬁnd a point of T1···k over a convenient extension of C(a1, . . . , an), e.g. one deﬁned using
only algebraic functions of at most d variables, then we can write a formula for the general
degree n polynomial using only functions of at most d variables and the algebraic function

(ck+1, . . . , cn) ↦→ {y | yn + ck+1yn−k−1 + · · · + cn = 0},

This, together with a ﬁnal rational change of coordinates, gives an upper bound

RD(n) ≤ max{d, n − k − 1}.

In [Hi27], Hilbert sketched how to use the 27 lines on a smooth cubic surface to ﬁnd points on
T1234 for n = 9: Here, T1 ⊂ P8 is a hyperplane, and thus T12 is a quadric 6-fold in T1 ∼= P7.
Over a solvable extension L/C(a1, . . . , a9), every smooth quadric contains a 3-plane P in P7.
The intersection of this 3-plane P with T123 is a cubic surface, and this gives a map from
Spec(L) to the moduli of cubic surfaces. Since every smooth cubic surface has 27 lines, and
the moduli space of cubic surfaces is 4-dimensional, the algebraic function which assigns a
line to a cubic surface is a function of at most 4-variables. Given a line on our cubic surface
P ∩ T123, we can then intersect it with T1234 to get a quartic polynomial in one variable, and
by adjoining radicals, we can ﬁnd a point on T1234(L′), where L′/C(a1, . . . , a9) is deﬁned
using algebraic functions of at most d = 4 variables.
As Dixmier observed [Di93, S8], the argument above is incomplete. In particular, Hilbert
takes for granted that the family of cubic surfaces P ∩ T123 is suﬃciently generic. Letting

3

H3,3 denote the parameter space of cubic surfaces and M3,3 the (coarse) moduli space of
smooth cubic surfaces, Hilbert essentially assumes that the above map

Spec(L) // H3,3

lands in the locus where the rational map

H3,3 99K M3,3

is well-deﬁned.5 The principal geometric contribution of this paper is to show that for
all n, the family of “Tschirnhaus hypersurfaces” needed for Hilbert’s argument (and its
generalization to arbitrary degrees) is generically smooth; see Theorem 2.12.
Beyond this, we need two fundamental post-Hilbert advances to convert Hilbert’s sketch
into a general method. The ﬁrst is Merkurjev and Suslin’s theorem on Severi-Brauer vari-
eties [MS83, Theorem 16.1], which allows us to trivialize the Severi-Brauer varieties which
arise in Hilbert’s argument by adjoining radicals.6 The second is a theorem of Hochster–
Laksov [HL87] which allowed Waldron [Wa08, Theorem 1.6] (see also [St17, Theorem 1.2])
to show that every degree d hypersurface in PN contains an r-plane when an appropriate di-
mension count is non-negative. Given these, we can generalize Hilbert’s sketch to explicitly
construct the function F and obtain the bounds on RD(n) stated above.

Outline of the Paper. In Section 2 we introduce the Tschirnhaus complete intersections
and study their geometry. In Section 3, we recall the geometric perspective on Tschirnhaus
transformations, and connect this to the Tschirnhaus complete intersections. In Section 4,
we develop the necessary results about the resolvent degree of a dominant map needed to
implement Hilbert’s idea for general degrees n. This extends the treatment of resolvent
degree of generically ﬁnite dominant maps in [FW19]. In Section 5, we prove the upper
bounds for RD(n) and compare them to Brauer’s. In Appendix A, we give explicit values
for the function F(r) discussed above. In Appendix B, we review the history of the search
for simple formulas for the general degree n polynomial and the summarize the major prior
work to date.

Conventions Throughout the paper, by a variety over a ﬁeld K or over Z, we mean a
reduced, separated, not-necessarily irreducible K or Z-scheme. For maps of varieties X //Z
and Y // Z, we will use the notation Y |X to denote the ﬁber product X ×Z Y .

Acknowledgements. First, I thank Benson Farb, who was closely involved with the ideas
that led to this paper, but who declined to be listed as a coauthor. Next, my sincere thanks
to Sebastian Hensel who translated Hilbert’s 1927 paper into English at Benson’s and my
request. This paper takes place in the context of ongoing joint work with Benson Farb and
Mark Kisin, and their inﬂuence permeates the perspective here. I thank Curt McMullen
for helpful conversations and for extensive helpful comments and suggestions on a draft.
I thank Aaron Landesman and Igor Dolgachev for helpful comments on a draft. I thank

5n.b. Hilbert actually assumes that the generic member of the family P ∩ T123 admits a “pentahedral
form”, but one can weaken this as above without any loss in the argument.
6Neither Hilbert nor Dixmier comment on this gap in Hilbert’s argument.

4

Jordan Ellenberg, Vlad Matei, Madhav Nori, Zinovy Reichstein, Daniil Rudenko and David
Smyth for helpful conversations. Last, I thank the referee for many helpful comments.

2 Tschirnhaus Complete Intersections

Given a polynomial
 p(z) = zn + a1zn−1 + · · · + an = ∏
(z − xi),

a Tschirnhaus transformation is a “change of variables”

y =
 n−1∑

j=0 bjxj.

This gives a new polynomial

q(z) = zn + c1zn−1 + · · · + cn = ∏

i (z − yi).

We are interested in Tschirnhaus transformations such that q(z) is “better normalized”
than p(z), e.g. in the sense that for some i,
∑

j yi
j = 0,

or more generally such that ∑

j yi1
j = · · · = ∑

j yik
j = 0

for some i1, . . . , ik. In this section, we study the collection of all b = (b0, . . . , bn−1) such
that the above normalizations hold. These are aﬃne varieties which we denote ̃T n
i1···ik , and
we refer to their projectivizations T n
i1···ik as Tschirnhaus complete intersections.
In this section, we introduce the varieties T n
i1···ik as objects of interest in their own right,
i.e. via explicit equations. We relate them to classical examples of interest, and study their
geometry. In Section 3, we review the classical subject of Tschirnhaus transformations for
algebraic functions, and we identify the varieties T n
i1···ik considered here with the spaces of
“normalized changes of variables” described above.

Tschirnhaus Complete Intersections via Explicit Equations

Fix n ≥ 0. In this section, we work over Z unless otherwise speciﬁed, so that, e.g. An :=
Spec(Z[a1, . . . , an]). For ease of reading, we adopt the following notation.

Notation 2.1. Denote

a := (a1, . . . , an) ∈ An. |κ| := ∑i ki
b := [b0 : · · · : bn−1] ∈ Pn−1 ||κ|| := ∑i i · ki
κ := (k0, . . . , kn−1) ∈ Nn bκ := ∏i bki
i

5

For |κ| = i, recall the multinomial coeﬃcients
( i
κ
) := ( i
k0, . . . , kn−1
) := i!
k0! · · · kn−1! .

We also introduce two variants of the above.

Notation 2.2.
 ′b := [b1 : · · · : bn−1] ∈ Pn−2

′κ := (k1, . . . , kn−1) ∈ Nn−1

′b
′ := [b1 : · · · : bn−2] ∈ Pn−3

′κ
′ := (k1, . . . , kn−2) ∈ Nn−2

Mutatis mutandis, we will also write |′κ|, ||′κ′||, ( i
′κ
), etc. Note that the meaning of || − ||
depends on whether the ﬁrst coordinate is the zeroth coordinate or the ﬁrst coordinate.
Our notation indicates that any tuple without a ′ preceding its label starts with a zeroth
coordinate, while any tuple with a ′ preceding its label starts with a ﬁrst coordinate.

We now inductively deﬁne polynomials in the ai by

p0 := n, (2.1)

while, for 0 < k ≤ n
 pk := kak +
 k−1∑

i=1 ak−ipi, (2.2)

and for k > n
 pk := −
 k−1∑

i=k−n ak−ipi. (2.3)

Remark 2.3. To interpret the polynomials pi, let σi denote the ith elementary symmetric
polynomial in formal variables x1, . . . , xn. If we write ai = (−1)iσi, then Newton’s Identities
give
 pi =
 n∑

j=1 xi
j.

Deﬁnition 2.4. For i, n ≥ 1, let the T n
i ⊂ An
a ×Pn−1
b be the variety deﬁned by the vanishing
of the polynomial ∑

κ s.t. |κ|=i
 ( i
κ

)p||κ||bκ. (2.4)

Note that this polynomial is homogeneous of degree i in the b-coordinates. Projecting onto
the ﬁrst factor gives a family of degree i hypersurfaces in Pn−1

T n
i // An
a

We refer to this family as the nth Tschirnhaus hypersurface of degree i. When the superscript
n is clear from context, we will suppress it for ease of reading.

6

Deﬁnition 2.5. Fix n ≥ 1. For 1 ≤ i1 < . . . < ik, deﬁne the nth Tschirnhaus complete
intersection T n
i1···ik (of multi-degree i1 · · · ik) to be the variety deﬁned by the vanishing of
the polynomials (2.4) for i = i1, . . . , ik. Equivalently, deﬁne

T n
i1···ik := T n
i1 ×An
a ×Pn−1
b · · · ×An
a ×Pn−1
b T n
ik // An
a.

Deﬁne the nth reduced Tschirnhaus complete intersection T n′
i1···ik (of multi-degree i1 · · · ik)
by T n′
i1···ik := T n
i1···ik ∩ {b0 = 0} ⊂ An
a × Pn−1
b .

Example 2.6. The hyperplane T1(a) ⊂ Pn−1
b is given by the equation

nb0 +
 n−1∑

i=1 pibi = 0

Over Z[1/n], we have an isomorphism

An
a × Pn−2 ∼= // T1

(a, [b1 : · · · : bn−1]) ↦→ (a, [− 1
n
 n−1∑

i=1 pibi : b1 : · · · : bn−1]).

Likewise, the hyperplane T ′
1(a) ⊂ Pn−2
b is given by the equation

n−1∑

i=1 pibi = 0

Over each locus {pi ̸= 0} ⊂ An
a for 1 ≤ i < n, we have an isomorphism

An
a × Pn−3 ∼= // T1

(a, [b1 : · · · : bˆi : · · · : bn−2]) ↦→ (a, [b1 : · · · : bi−1 : −1
pi
 ∑

j̸=i pjbj : bi+1 : · · · bn−2]).

As a warm-up to Theorem 2.12 below, we prove the following.

Lemma 2.7. The families of quadrics T12 // An
a and T ′
12 // An
a are generically smooth.

Remark 2.8. The statement of the lemma for T12 (and most likely for T ′
12) is classical, and
follows from the fact that the discriminant of the quadratic form deﬁning T12(a) is equal
to 1
n times the discriminant of the polynomial xn + a1xn−1 + · · · + an (see, e.g. [Sy1887, p.
468-469]). We give a diﬀerent proof in order to warm-up for Theorem 2.12.

Proof of Lemma 2.7. The quadric T12(a) ⊂ Pn−2
b is given, in coordinates [b1 : · · · : bn−1] by
the equation
 − 1
n
 ( 1
n
 n−1∑

i=1 pibi
)2
 + ∑

1≤i<j≤n−1 pi+jbibj +
 n−1∑

i=1 p2ib2
i = 0.

7

We now specialize to the radical pencil xn + a = 0, i.e. a = (0, . . . , 0, a). Then T12(a) :=
T12(0, . . . , a) is given by the equation




 −2na (∑ n−1
2
i=1 bibn−i
) = 0 n odd

−na (
b2
n
2 + 2 ∑ n
2 −1
i=1 bibn−i) = 0 n even (2.5)

The partial derivatives of the deﬁning polynomial of T12(a) are given by

∂bj T12(a) = −2nabn−j.

We see that these vanish simultaneously if and only if bj = 0 for all j, i.e. T12(a) is smooth
over Z[1/2n] so long as a ̸= 0 (and thus T12 // An
a is generically smooth).
We now prove T ′
12 // An
a is generically smooth. Using (2.2), the hyperplane T ′
1(a) is
given by (n − 1)abn−1 = 0.

Over Z[1/(n − 1)], and a ̸= 0, we can therefore use the coordinates

[b1 : · · · : bn−2]

on T ′
1(a). In these coordinates, and abusing notation by writing the same symbol for a
hypersurface and its deﬁning polynomial, we have

T ′
12(a) =
 



 −2(n − 1)a (∑ n
2 −1
i=1 bibn−1−i) n even

−(n − 1)a(b2
n−1
2 + (∑ n
2 −1
i=1 bibn−1−i) n odd

The partial derivatives of T ′
12(a) are given by

∂bj T ′
12(a) = −2(n − 1)abn−1−j .

We see that these vanish simultaneously if and only if bj = 0 for all j, i.e. T ′
12(a) is smooth
over Z[1/2(n − 1)] so long as a ̸= 0 (and thus T ′
12 // An
a is generically smooth).

Tschirnhaus hypersurfaces as spaces of maps. In Section 3, we explain the origin
of the Tschirnhaus complete intersections in the classical study of formulas for the general
degree n polynomial (beginning with [Ts1683]). For the moment, we just observe that
several varieties of classical interest are closely related to T n
i for small i, n.
Let x := (x1, . . . , xn) be coordinates on aﬃne n-space, denoted An
x. Let σi(x) denote
the ith elementary symmetric function on the xi, and consider the map

q : An
x // An
a
x ↦→ (−σ1(x), . . . , (−1)
nσn(x)).

By Newton’s Theorem, this map realizes An
a as the quotient of An
x by the permutation action
of the symmetric group Sn on An
x. As remarked above, Newton’s Identities imply that

pi(q(x)) =
 n∑

j=1 xi
j.

8

Let ˜b := (b0, . . . , bn−1) viewed as aﬃne coordinates on An
˜b. The relative aﬃne cone on the
pullback Ti|An
x // An
x is given by

̃Ti|An
x :=
 


(x, ˜b) ∈ An
x × An
˜b | ∑ ∑

κ s.t. |κ|=i
 ( i
κ
) 

 n∑

j=1 x||κ||
j
 

 ˜bκ = 0




 .

Consider the map
 ev : An
x × An
˜b // An
x

(x, ˜b) ↦→ (

n−1∑

j=0 bjxj
1, . . . ,
 n−1∑

j=0 bjxj
n).

Lemma 2.9. In the notation above,

̃Ti|An
x = ev−1({x ∈ An
x | ∑

j xi
j = 0.}).

Proof. We prove this by explicit computation. For i ≥ 0, write

pi(x) :=
 n∑

ℓ=1 xi
ℓ.

In particular, p0(x1, . . . , xn) = n. Let ev(x, ˜b)ℓ := ∑n−1
j=0 bjxj
ℓ. By the Multinomial Theo-
rem,
 pi(ev(x, ˜b)) = ∑

ℓ ev(x, ˜b)
i
ℓ = ∑

ℓ
 


n−1∑

j=0 bjxj
ℓ



i

= ∑

ℓ
 

 ∑

κ s.t. |κ|=i
 ( i
κ

)bκx||κ||
ℓ
 



= ∑

κ s.t.|κ|=i
 ( i
κ
)p||κ||b
κ (2.6)

where, in the ﬁnal line, we use Newton’s Identities to identify the power sums with the
polynomials p||κ|| in the ai deﬁned in Equations 2.1-2.3.
Setting the form (2.6) to 0, we obtain the hypersurface ̃T n
i as claimed.

Example 2.10. Let S ⊂ P4 be the Clebsch diagonal surface, i.e. the complete intersection

S := {[x1 : · · · : x5] ∈ P4 |
 5∑

i=1 xi =
 5∑

i=1 x3
i = 0}.

Let ̃S ⊂ A5
x be the aﬃne cone over S. Then

̃T 5
13|A5
x = ev−1( ̃S).

9

As observed by Klein [Kl1884, Part II, Ch. 2], ̃T 5
13|A5
x can be understood as a space of
S5-equivariant maps of A5
x // ̃S.

Example 2.11. Let F ⊂ P6 be the symmetric Fano sextic 3-fold as in [Be12], i.e. the
complete intersection

F := {[x1 : · · · : x7] ∈ P6 |
 7∑

i=1 xi =
 7∑

i=1 x2
i =
 7∑

i=1 x3
i = 0}.

Let ̃F ⊂ A7
x be the aﬃne cone over F . Then

̃T 7
123|A7
x = ev−1( ̃F ).

Though not remarked upon in [Be12], the symmetric Fano sextic arises as the “root space”
of the normal form for the general degree 7 polynomial considered by Hilbert in his 13th
problem [Hi1900]: z7 + az3 + bz2 + cz + 1 = 0.

. The variety ̃T 7
123|A7
x can be understood as a space of S7-equivariant maps of A7
x // ̃F ,
equivalently of ways of converting the general degree 7 polynomial into Hilbert’s normal
form.

Geometry of Tschirnhaus Complete Intersections

We can now state our main geometric theorem.

Theorem 2.12. Let p be a prime. Let i = pr + 1 < n for some prime power pr with r > 0.

1. If p ∤ n, the family of Tschirnhaus complete intersections

T12i // An
a

is generically smooth (i.e. there is a Zariski open U ⊂ An
a such that for all a ∈ U ,
T12i(a) is a smooth complete intersection).

2. If p | n, the family of reduced Tschirnhaus complete intersections

T ′
12i // An
a

is generically smooth.

Deferring the proof for a moment, let K be a ﬁeld of characteristic 0, now and throughout
this paper.
We now record a special case of Kleiman’s Bertini Theorem [Kl74]; for ease of reading,
we include the proof below.
 10

Proposition 2.13 (Bertini for isotropics). Let K be algebraically closed. Let X be a
K-variety. Let Q ⊂ Pn
X be a smooth family of quadrics over X. For k ≤ ⌊ n−1
2 ⌋, let
Gr(k, Q) // X denote the relative Grassmannian of k-dimensional isotropic subspaces in
Q, and let L // Gr(k, Q) denote the tautological bundle. Let Y ⊂ Pn
X be a smooth family of
varieties over X such that the family Q×Pn
X Y //X is smooth over some dense open V ⊂ X.
Then there exists a dense open U ⊂ Gr(k, Q)|V such that the family L|U ×Pn
X Y |V // X is
smooth.

Combining Theorem 2.12, Lemma 2.7 and Proposition 2.13, we obtain the following.

Corollary 2.14. Let Gr(T12) //An
a denote the relative Grassmannian of maximal isotropics
in the family of quadrics T12 // An
a, and let L // Gr(T12) denote the tautological bundle
(with similar notation for the analogous objects for T ′
12). Let p be a prime and let i = pr + 1
for some r > 0.

1. If p ∤ n, there exists a dense open V ⊂ Gr(T12) such that

L|V ×An
a ×Pn−1
b T12i // An
a

is smooth (i.e. for the generic polynomial, the intersection of T12i(a) with a maximal
isotropic in T12(a) is smooth).

2. If p | n, there exists a dense open V ⊂ Gr(T ′
12) such that

L|V ×An
a ×Pn−2
′b T ′
12i // An
a

is smooth.

Proof. Note that to prove the existence of an open dense V , it suﬃces to restrict all of the
varieties over Z above to a geometric generic point Spec(K) // Spec(Z). The result now
follows immediately from Theorem 2.12, Lemma 2.7 and Proposition 2.13.

Remark 2.15. Corollary 2.14 (for the case p = 2, i = 3, n = 9) ﬁlls the gap in Hilbert’s
argument remarked upon by Dixmier [Di93, S8].

Proof of Proposition 2.13. We recall Kleiman’s proof [Kl74]. Consider the canonical map

pr2 : L // Q

(coming from the construction of L as an incidence variety L ⊂ Gr(k, Q) ×X Q). Observe
that this map is smooth: indeed, the relative group scheme O(Q) acts transitively over X
on both L and Q (i.e. it acts transitively on ﬁbers over X) and the map L // Q is an
O(Q)-equivariant ﬁber bundle, with ﬁber at v ∈ Q given by StabO(Q)(v)/ StabO(Q)(L, v),
(n.b. the stabilizer of an isotropic point v is a maximal parabolic, and the stabilizer of the
ﬂag v ∈ L is a sub-parabolic).
Let V ⊂ X be a dense open such that Q ×Pn
X Y // X is smooth over V . Shrinking
V as necessary, we can assume without loss of generality that V is a smooth variety over

11

K (note that we are using characteristic 0 here), and thus (Q ×Pn
X Y )|V is also a smooth
K-variety. Now consider the ﬁber product

(L ×Pn
X Y )|V f //

g   
 (Q ×Pn
X Y )|V

ι
  
L|V pr2 //

π   
 Q|V

Gr(k, Q)|V

The map f is smooth because pr2 is smooth. Because (Q ×Pn
X Y )|V is a smooth K-variety,
the K-variety (L ×Pn
X Y )|V is smooth. We therefore have a dominant map of smooth K-
varieties q = π ◦ g : (L ×Pn
X Y )|V // Gr(k, Q)|V .

By generic smoothness (e.g. [Ha77, Corollary III.10.7]), there exists a nonempty open
subset U ⊂ Gr(k, Q)|V such that q : (L|U ×Pn
X Y |V ) // U is smooth, and thus the composite
(L|U ×Pn
X Y |V ) // U // V is smooth as well.

We now prove Theorem 2.12.

Proof of Theorem 2.12. We prove the two cases separately, via parallel arguments. As in
the proof of Lemma 2.7, if it will not cause confusion, we will abuse notation by writing the
same symbol to denote a complete intersection and its deﬁning polynomials.
Case 1: p ∤ n. The complete intersection T12i(a) is smooth if and only if the 3 × n matrix



 ∂b1T1(a) · · · ∂bn−1 T1(a)
∂b1T2(a) · · · ∂bn−1 T2(a)
∂b1Ti(a) · · · ∂bn−1 Ti(a)
 



has full rank for all b ∈ T12i(a). Choosing coordinates on T1, we can equivalently check
whether the 2 × (n − 1) matrix given by the partials of T12 and T1i has rank 2 for all
b ∈ T12i(a). To show generic smoothness, it suﬃces to ﬁnd a single a for which this
holds. Further, because the matrix above is deﬁned over Z, to show it is nonsingular in
characteristic 0, it suﬃces to ﬁnd a prime p for which its reduction mod p is nonsingular.
We specialize to the locus of radical polynomials, i.e. those of the form

p(x) = xn + a

i.e. a = (0, . . . , 0, a). It suﬃces to show there exists a such that T12i(a) := T12i(0, . . . , a) is
smooth. Note that, restricting to xn + a, the hyperplane T1(a) is given by

nb0 = 0.

We can therefore use the coordinates
 [b1 : · · · : bn−1]

12

on T1(a) as above. As in (2.5), the form T12(a) is given in these coordinates by

T12(a) =
 



 −2na (∑ n−1
2
i=1 bibn−i
) n odd

−na (
b2
n
2 + 2 ∑ n
2 −1
i=1 bibn−i) n even

and the partial derivatives are given by

∂bj T12(a) = −2nabn−j.

Similarly, using Notation 2.2, the form T1i(a) is given by

T1i(a) = n ·
 

 i−1∑

ℓ=1(−1)
ℓaℓ
 

 ∑

′κ s.t.|′κ|=i,||′κ||=ℓn
 ( i
′κ

)′b
′κ






The partial derivatives of T1i(a) are given by

∂bj T1i(a) = in ·
 

 i−1∑

ℓ=1(−1)
ℓa
ℓ
 

 ∑

′κ s.t. |′κ|=i−1,||′κ||+j=ℓn
 (i − 1
′κ
 )′b′κ




 .

Deﬁne
 Tj,12(a) := abn−j

Tj,1i(a) :=
 i−1∑

ℓ=1(−1)
ℓaℓ
 

 ∑

′κ s.t. |′κ|=i−1,||′κ||+j=ℓn
 (i − 1
′κ
 )′b′κ

 .

Then, in characteristic 0, the matrix
( ∂b1 T12(a) · · · ∂bn−1 T12(a)
∂b1T1i(a) · · · ∂bn−1 T1i(a)
 )

is singular if and only if the matrix
( T1,12(a) · · · Tn−1,12(a)
T1,1i(a) · · · Tn−1,1i(a)
 )

is singular. Because this matrix is deﬁned over Z[a], to show that it is generically nonsingular
in characteristic 0, we can reduce mod p and ﬁnd some a ∈ Fp for which it is nonsingular.
Let Tj,12(a) and Tj,1i(a) denote the reduction of the above forms mod p.
Recall that Legendre’s formula implies that a prime p divides all the multinomial coef-
ﬁcients {
( ℓ
k1,...,km) | kj < ℓ for all j} if and only if ℓ = pr. Therefore, reducing the forms
Tj,1i(a) mod p, and using i − 1 = pr, Legendre’s formula implies that .

Tj,1i(a) =
 i−1∑

ℓ=1(−1)
ℓaℓ
 

 ∑

1≤ν≤n−1,prν+j=ℓn bpr
ν
 

 (2.7)

13

(n.b. as we remark just below, only one term in the above sum is nonzero). Now, because p ∤
n, pr ∈ (Z/nZ)×. Therefore, multiplication by p−r determines a permutation of {1, . . . , n −
1} = Z/nZ − {0}, which we denote by

ν(j) := p−r · j ∈ Z/nZ − {0} = {1, . . . , n − 1}.

In this notation, we have
 Tj,12(a) = ab−j

Tj,1i(a) = (−a) pr ν(−j)+j
n b
pr

ν(−j)

where ±j and ν(±j) denote the corresponding elements of {1, . . . , n − 1}. Now, multipli-
cation by p−r on Z/nZ − {0} generates a cyclic group, and so a partition of {1, . . . , n − 1}
into m orbits Oα of size sα. Let jα denote the least element of the orbit Oα. For ease of
notation, denote
 ǫα(t) := prνt(jα) + n − νt−1(jα)
n .

Reorder the columns of the matrix we are considering so that it is of the form

M := ( M1 · · · Mm ) (2.8)

where each Mα denotes the 2 × sα matrix

Mα :=
 ( abjα abν(jα) · · · abνsα−1(jα)
(−a)ǫα(1)b
pr

ν(jα) (−a)ǫα(2)bpr

ν2(jα) · · · (−a)ǫα(sα)bpr
jα
 )
 .

Note that, by construction, for each j, all monomials containing bj appear in precisely one
Mα.
Now the matrix (2.8) is singular at b ∈ Pn−2 and a ∈ Fp if and only if its two rows are
linearly dependent. Equivalently, there exists λ ∈ F
×
p such that for all α and 0 ≤ t ≤ sα − 1

abνt(jα) = λ(−a)
ǫα(t+1)b
pr

νt+1(jα). (2.9)

Restrict to a ∈ F
×
p . Then, by induction on t, we obtain that for all j ∈ Oα

bj = (−λ)
∑sα
t=1 p(t−1)r (−a)
∑sα
t=1 p(t−1)r(ǫα(t)−1)bpsαr
j .

Therefore, for any bj ̸= 0 for j ∈ Oα (and such a j and α must exist since b ∈ Pn−2), we
have
 b
psαr−1
j = (−λ)
− ∑sα
t=1 p(t−1)r (−a)
− ∑sα
t=1 p(t−1)r(ǫα(t)−1)

=: cα(a)

But, if j = νt(jα), then by Equation (2.9),

cα(a) = bpsαr−1
j = (−λ(−a)
ǫα(t+1)−1)
psαr−1cα(a)
pr .

14

Expanding the deﬁnition of cα(a) in terms of λ and a, we obtain

(−λ)
− ∑sα
t=1 p(t−1)r (−a)
− ∑sα
t=1 p(t−1)r(ǫα(t)−1)

= (−λ)
psαr−1−∑sα
t=1 ptr (−a)
(psαr−1)(ǫα(t+1)−1)−∑sα
t=1 ptr(ǫα(t)−1)

= (−λ)
− ∑sα
t=1 p(t−1)r (−a)
(psαr−1)(ǫα(t+1)−1)−∑sα
t=1 ptr(ǫα(t)−1).

Therefore, for all 0 ≤ t ≤ sα

1 = (−a)
(psαr−1)(ǫα(t+1)−1)−∑sα
t=1 p(t−1)r(pr−1)(ǫα(t)−1)

In particular, a2(psαr−1)(ǫα(t+1)−1)−∑sα
t=1 p(t−1)r(pr−1)(ǫα(t)−1) = 1. (2.10)

But, sα, ǫα(t), p, r ∈ N are ﬁxed once and for all by our choice of p and n. In particular,
there exists N ∈ N such that

N > max
α |2(psαr − 1)(ǫα(t + 1) − 1) −
 sα∑

t=1 p(t−1)r(pr − 1)(ǫα(t) − 1)|.

But, then for any primitive N th root of unity a ∈ Fp, Equation 2.10 is never satisﬁed.
Therefore, the matrix M (a) = (M1(a) · · · Mm(a)) of (2.8) has full rank for all ′b ∈ Pn−2 as
claimed.

Case 2: p | n. This case is similar. We specialize to the pencil xn + ax = 0, i.e. a =
(0, . . . , 0, a, 0). It suﬃces to show there exists a such that T ′
12i(a) := T ′
12i(0, . . . , a, 0) is
smooth.
As noted in the proof of Lemma 2.7, over Z[1/(n − 1)], and a ̸= 0, we can use the
coordinates [b1 : · · · : bn−2]

on T ′
1(a). We follow Notation 2.2. In these coordinates and this notation, the partial
derivatives of T ′
12(a) are given by

∂bj T12(a) = −2(n − 1)abn−1−j

(as noted in the proof of Lemma 2.7). Similarly, we have

T ′
1i(a) =(n − 1) ·
 

 i−1∑

ℓ=1(−a)
ℓ ∑

′κ′ s.t. |′κ′|=i,||′κ′||=ℓ(n−1)
 ( i
′κ′
) ′b
′(′κ′)




∂bj T ′
1i(a) =i(n − 1) ·
 

 i−1∑

ℓ=1(−a)
ℓ ∑

′κ′ s.t. |′κ′|=i−1,||′κ′||+j=ℓ(n−1)
 (i − 1
′κ′
 ) ′b′(′κ′)




Deﬁne
 T ′
j,12(a) := abn−1−j

T ′
j,1i(a) :=
 i−1∑

ℓ=1(−a)
ℓ ∑

′κ′ s.t. |′κ′|=i−1,||′κ′||+j=ℓ(n−1)
 (i − 1
′κ′
 ) ′b
′(′κ′)

15

Just as in Case 1, the matrix
( ∂b1 T12(a) · · · ∂bn−2 T12(a)
∂b1T1i(a) · · · ∂bn−2 T1i(a)
 )

is everywhere nonsingular in characteristic 0 for some a if and only if the matrix
( T ′
1,12(a) · · · T ′
n−2,12(a)
T ′
1,1i(a) · · · T ′
n−2,1i(a)
 )

is everywhere nonsingular for some a. We now reduce this matrix mod p. Because i = pr +1,
the mod p reduction of T ′
j,1i(a) is given by

T ′
j,1i(a) =
 i−1∑

ℓ=1(−a)
ℓ ∑

′κ′ s.t. |′κ′|=i−1,||′κ′||+j=ℓ(n−1)
 (i − 1
′κ′
 ) ′b′(′κ′)

In particular, because i − 1 = pr, and pr ∈ (Z/(n − 1)Z)×, the same arguments as above
allow us to deﬁne a permutation ν ⟲ {1, . . . , n − 2} = (Z/(n − 1)Z) − {0} by

ν(j) = p−rj ∈ (Z/(n − 1)Z) − {0} = {1, . . . , n − 2}.

Using ν, we have
 T ′
j,1i(a) = (−a)
 pr ν(j)+j
n−1 b
pr

ν(j).

Mutatis mutandis, we now complete the argument by the same reasoning as for Case 1.

Remark 2.16. A similar argument shows that the Tschirnhaus hypersurface Ti // An
a
itself is generically smooth for i = pr + 1 and r ≥ 0. More generally, we see no reason not
to expect this, as well as Theorem 2.12, to hold without restriction on i < n. In principle,
this comes down to checking whether an appropriate discriminant identically vanishes on
Ti (resp. T12i), i.e. checking a polynomial condition on the form deﬁning Ti. However, this
discriminant is a polynomial of degree (n − 1)(d − 1)n−1 in the coeﬃcients of the form, and
the number of terms in this polynomial grows so quickly as to make direct computation
impossible except for very small d and n.

3 Algebraic Functions and Tschirnhaus Transformations

In this section, we recall the theory of Tschirnhaus transformations of algebraic functions
and relate this to the Tschirnhaus complete intersections studied above.
Let X be an irreducible K-variety. We write K(X) for the rational functions on X.
More generally, for a (not necessarily reducible) K-variety Y with irreducible components
{Yi}, let K(Y ) := ∏
i K(Yi).
Recall that an algebraic function Φ on X is a ﬁnite rational correspondence X 99K1:n A1,
i.e. Φ is given by a span EΦ z //

π   
 A1

X
 16

where π is a dominant, quasi-ﬁnite map and z is a regular function. We say Φ is irreducible
if EΦ is an irreducible K-variety and z is a primitive element of the ﬁnite ﬁeld extension
K(EΦ)/K(X). As a bridge to the classical literature, we will also denote K(EΦ) as K(X)(Φ)
to emphasize that K(EΦ) is obtained from the ﬁeld K(X) by adjoining the values of Φ.
Let Mon(Φ) denote the monodromy group of Φ, equivalently the Galois group of the
normal closure of K(X)(Φ)/K(X). Let

mΦ(z) := zn + a1zn−1 + . . . + an

denote the minimal polynomial of z, where the ai ∈ K(X) (i.e. mΦ(z) is the monic generator
of the ideal of K(X)[z] corresponding to the extension K(X)(Φ)). A classical perspective
describes Φ as the assignment

x ↦→ {z ∈ ¯K | mΦ(x)(z) = zn + a1(x)zn−1 + . . . + an(x) = 0}. (3.1)

For any ﬁeld extension K(X) ֒→ L, write

L(Φ) := L ⊗K(X) K(X)(Φ).

Note that since {1, z, . . . , zn−1} is a basis for K(X)(Φ) over K(X), it is also a basis for
L(Φ) over L. Given this, for each w ∈ L(Φ), there exist unique b0, . . . , bn−1 ∈ L such that

w =
 n−1∑

i=0 bizi.

Moreover, ˜b = (b0, . . . , bn−1) ∈ Ln determines an L-linear transformation

T˜b : L(Φ) // L(Φ)

given by (extending L-linearly) the assignment T˜b(zj) := wj for each 0 ≤ j ≤ n − 1. Note
that T˜b is an automorphism if and only if w is a primitive element of the extension L(Φ)/L.

Deﬁnition 3.1. Let X be an irreducible K-variety. Let Φ be an irreducible algebraic
function on X with primitive element z ∈ K(X)(Φ). A Tschirnhaus transformation T of Φ
is a K(X)-linear automorphism
T : K(X)(Φ) // K(X)(Φ).

of the form
 zj ↦→ wj =
 (n−1∑

i=0 bizi)j

for b0, . . . , bn−1 ∈ K(X). We say the transformation is rational over X if b0, . . . , bn−1 ∈
K(X). More generally, we say it is rational over L/K(X) if all bi ∈ L.

Picking an integral model Y // X for K(X)(˜b)/K(X), (i.e. a map of K-varieties
Y // X and an isomorphism K(Y ) ∼= K(X)(˜b) as extensions of K(X)), we denote by T (Φ)
the algebraic function on Y determined by the primitive element w ∈ K(Y )(Φ).

17

Now let Φ be an algebraic function as above, and T a Tschirnhaus transformation of Φ.
Let w = T (z), and let the minimal polynomial of multiplication by w on K(X)(Φ) be given
by mT (Φ)(w) := wn + c1wn−1 + . . . cn

where ci ∈ L = K(Y ). The algebraic function T (Φ) on Y is given by the assignment

y ↦→ {z ∈ K(X) | mT (Φ)(y)(z) = zn + c1(y)zn−1 + . . . + cn(y) = 0}.

Recall that An
X := X ×Spec(K) An
K , viewed as a variety over X.

Lemma 3.2. Let X be irreducible, and let Φ be an irreducible, generically n-valued algebraic
function on X. Then there is an open subvariety

TΦ ⊂ An
X,

such that for all ﬁnite extensions L/K(X), TΦ(L) is the set of Tschirnhaus transformations
of Φ which are rational over L. In particular, the map

TΦ  • //
 !!❈❈❈❈❈❈❈❈ An
X

  
X

is smooth. Equivalently the parameter space of Tschirnhaus transformations TΦ // X is
smooth over X.

Proof. We begin by constructing the variety TΦ. Denote the set of K(X)-rational Tschirn-
haus transformations of Φ by TΦ(K(X)). We will show that this embeds as an explicit
Zariski open subset of K(X)n = An
X(K(X)), and that its complement is deﬁned over
K(X); we thus conclude that TΦ(K(X)) is the set of geometric generic points of a variety
TΦ ⊂ An
X.
Let z ∈ K(X)(Φ) be the primitive element determined by Φ. Given ˜b ∈ K(X)n, we
have a K(X)-linear endomorphism

T˜b : K(X)(Φ) // K(X)(Φ)

given by
 zj ↦→
 (n−1∑

i=0 bizi)j
 .

Moreover, the assignment ˜b ↦→ T˜b deﬁnes a Gal(K(X)/K(X))-equivariant map

T : An(K(X)) // End
K(X)(K(X)(Φ)) ∼= An2(K(X)).

By deﬁnition, TΦ(K(X)) is in bijection with the set

{˜b ∈ K(X)n | T˜b ∈ AutK(X)(K(X)(Φ))}

18

i.e. TΦ(K(X)) = T −1(AutK(X)(K(X)(Φ))).

Since AutK(X)(K(X)(Φ)) is the pullback to K(X) of an open subvariety of An2
Z (i.e. the

locus {det ̸= 0})) and T is deﬁned over K(X), we conclude that TΦ(K(X)) ⊂ An(K(X)
is Zariski open and deﬁned over K(X) as claimed. The remaining claims follow by direct
inspection.

Corollary 3.3. Let Φ be an irreducible n-valued algebraic function on X such that K(X)(Φ)/K(X)
has no intermediate subﬁelds. Let An
X be given coordinates (b0, . . . , bn−1) as above, and let
A1
X,0 ⊂ An
X denote the b0-axis. Then
TΦ = An
X − A1
X,0.

Proof. Because K(X)(Φ)/K(X) has no intermediate subﬁelds, y ∈ K(X)(Φ) is a primitive
element if and only if y /∈ K(X), i.e. if and only if y is of the form y = ∑n−1
i=0 bizi with
bi ̸= 0 for some i > 0.

Example 3.4. Let X = An
a, viewed as the parameter space for monic, degree n polynomials
(parametrized by their coeﬃcients a := (a1, . . . , an)). Let Pn be the general degree n
polynomial, i.e. mPn(z) = zn + a1zn−1 + . . . + an.

Then the degree n extension K(An
a)(Pn)/K(An
a) has no intermediate subﬁelds, because it
corresponds to the maximal subgroup Sn−1 ⊂ Sn = Mon(Pn). In particular, the space of
Tschirnhaus transformations of the general degree n polynomial is given by

TPn = An
X − A1
X,0
:= An
˜b × An
a − A1
b0 × An
a
= (An
˜b − A1
b0) × An
a.

Now let Φ be an irreducible algebraic function on X, and let T be a Tschirnhaus trans-
formation of Φ as above, with minimal polynomial

mT (Φ)(y) := yn + c1yn−1 + . . . cn

Observe that the assignment x ↦→ (c1(x), . . . , cn(x))

determines a rational map X 99K An

which ﬁts into a pullback square EΦ //❴❴❴

π   
 EPn

  
X //❴❴❴ An

19

In particular, the Tschirnhaus transformation T transforms Φ into a function of d =
dim(Image(X 99K An)) variables.
We now study loci of interest in the space of Tschirnhaus transformations. The basic
observation (essentially going back to Tschirnhaus [Ts1683]) is as follows. First, the col-
lection of n-valued algebraic functions on X is given by An
X, where a = (a1, . . . , an) ∈ An
X
corresponds to the function Φa of (3.1), i.e. the function

x ↦→ {z ∈ ¯K | mΦa(x)(z) = zn + a1(x)zn−1 + . . . + an(x) = 0}.

Next, the assignment (Φa, ˜b) ↦→ T˜b(Φa) determines an “evaluation” map

An
X,a × An
X,˜b ev // An
X,a

(a, ˜b) ↦→ T˜b(a)

(where we write (−)a and (−)˜b to distinguish the diﬀerent roles of the a and ˜b coordinates).
The coordinates of T˜b(a) can be computed explicitly as follows. By deﬁnition, ˜b ∈ An
X
corresponds to the assignment
 z ↦→
 n−1∑

i=0 bizi = y

for z a value of Φa. Passing to a Galois closure of K(X)(Φ), the transformation T maps
the roots zi of mΦ to yi given by
 yi =
 n−1∑

j=0 bjzj
i .

In particular, the polynomial mT (Φ) is given by

mT (Φ)(y) =
 n∏

i=1(y − yi).

i.e. the coordinates of TΦ are obtained (up to sign) by expanding the elementary symmetric
polynomials in the yi as polynomials in b with coeﬃcients given by polynomials in the
coordinates a. In particular, the jth coeﬃcient is a homogeneous polynomial of total degree
j in the coordinates ˜b.
As a result, every Zariski closed subvariety Z ⊂ An
X,a determines a Zariski closed sub-
variety ev−1(Z) ⊂ An
X,a × An
X,˜b,

Specializing to a particular algebraic function Φ, and its space of Tschirnhaus transforma-
tions TΦ ⊂ An
X,˜b, we obtain a Zariski closed subvariety (concretely TΦ ∩ ev−1(Z)), which,
by abuse of notation, we denote again by

ev−1(Z) ⊂ TΦ.

By construction, this subvariety parametrizes Tschirnhaus transformations of Φ such that
T (Φ) (or more precisely, the coeﬃcients of its minimal polynomial) lie in Z ⊂ An
X,a.

20

We can now make contact with the Tschirnhaus complete intersections introduced in
Section 2. For 1 ≤ i1 < . . . < ik, deﬁne

Zi1···ik := {a ∈ An
a | pi1(a) = · · · = pik (a) = 0}

where the pis are as in Section 2.

Deﬁnition 3.5. Let n > 0. For 1 ≤ i1 < . . . < ik, deﬁne the aﬃne Tschirnhaus complete
intersection ˜Ti1···ik (Pn) to be

˜Ti1···ik (Pn) := ev−1(Zi1···ij ) ⊂ TPn ⊂ (An
˜b − A1
b0=0) × An
a.

Projecting onto An
a gives the family ˜Ti1···ik (Pn) // An
a.
Similarly, deﬁne the Tschirnhaus complete intersection

Ti1···ik (Pn) ⊂ (Pn−1
b − {[1 : 0 : · · · : 0]}) × An
a

to be the (ﬁberwise) projectivization of the family ˜Ti1···ik (Pn) // An
a.
Deﬁne the reduced aﬃne Tschirnhaus complete intersection by

˜T ′
i1···ik (Pn) := Ti1···ik ∩ {b0 = 0}.

Similarly, deﬁne the reduced Tschirnhaus complete intersection

T ′
i1···ik (Pn) ⊂ Pn−2
′b × An
a

to be the (ﬁberwise) projectivization of the family ˜T ′
i1···ik // An
a.

Lemma 2.9 can now be equivalently restated as follows.

Lemma 3.6. For all n and all 1 ≤ i1 ≤ · · · ≤ ik, we have

Ti1···ik (Pn) = T n
i1···ik

as subvarieties of An
a × Pn−1
b , where the right hand side denotes the Tschirnhaus complete
intersection of Deﬁnition 2.5.
Similarly, we have
 T ′
i1···ik (Pn) = T n′
i1···ik

as subvarieties of An
a × Pn−2
′b .

4 The Resolvent Degree of a Dominant Map

Recall the following (see [Br75, AS76, FW19]).

21

Deﬁnition 4.1 (Resolvent degree). Let Y // X be a generically ﬁnite dominant map
of K-varieties. Its resolvent degree RD(Y // X) is the minimum d for which there exists a
dense Zariski open U ⊂ X and a tower of generically ﬁnite dominant maps

Er // · · · // E1 // E0 = U

such that Er // U factors through a dominant map Er // Y and such that for each i ≥ 0,
there exists a pullback diagram Ei //

  
 ˜Zi

  
Ei−1 // Zi

where ˜Zi // Zi is a generically ﬁnite dominant map with dim(Zi) ≤ d.

Example 4.2. Consider the space An
a of monic degree n-polynomials. This has a canonical
n-sheeted branched cover EPn // An
a where EPn is the space of monic degree n polynomials
with a choice of root, and the map forgets the root. By deﬁnition

RD(n) := RD(EPn // An
a).

We now extend the notion of resolvent degree to general dominant maps. We adopt the
following convention to avoid pathologies.

Convention 4.3. By a dominant map, we mean a map Y // X that is both dominant,
and is such that every irreducible component of Y maps dominantly onto some irreducible
component of X.

Deﬁnition 4.4 (Rational multi-section). Let Y π // X be a dominant map of K-
varieties. A rational multi-section is a subvariety U ⊂ Y such that the restriction π|U :
U // X is a generically ﬁnite dominant map.

Lemma 4.5. Every dominant map Y // X admits a dense set of rational multi-sections,
i.e. the closure of their union is all of Y .

Proof. First assume that X is irreducible. Let K(X) be an algebraic closure of the rational
functions of X. Then every point of Y (K(X)) is a germ of a rational multi-section, and, by
Hilbert’s Nullstellensatz, the closure of the union of all of these contains the generic ﬁber
of Y // X; in particular it is dense. For the general case, the argument above exhibits a
dense set of rational multi-sections over each irreducible component. Their union gives a
dense set of rational multi-sections of Y // X.

It will be useful to extend the deﬁnition of resolvent degree from generically ﬁnite dom-
inant rational maps to all dominant rational maps.

Deﬁnition 4.6 (Resolvent degree of a dominant map). Let Y π // X be a dominant
map of K-varieties. The resolvent degree of the dominant map, RD(Y // X) is deﬁned to
be the minimum d for which there exists a dense set of rational multi-sections {Uα ⊂ Y }
with RD(Uα // X) ≤ d for all α.
 22

We will need a few basic facts about the resolvent degree of a dominant map.

Lemma 4.7. Let Y // X be a dominant map of K-varieties.

1. RD(Y // X) ≤ dim(X).

2. Let Z // X be any dominant map of K-varieties. Then

RD(Y ×X Z // Z) ≤ RD(Y // X).

3. If Y // X is birationally equivalent to W // Z, then

RD(Y // X) = RD(W // Z).

4. If X = ⋃ Xi is a union of irreducible components, write {Yi,j} for the set of irreducible
components of Y which dominate Xi. Then

RD(Y // X) = max
i,j {RD(Yi,j // Xi)}.

Proof. These follow immediately from the deﬁnition and the analogous properties for resol-
vent degree of generically ﬁnite dominant maps (cf. [FW19, Lemmas 2.5, 2.6]).

Lemma 4.8. Let Y // X be a surjective map (on geometric points). Let Z // X be any
map. Then RD(Y |Z // Z) ≤ dim(X).

Proof. Let W ⊂ X be the Zariski closure of the image of Z // X. By construction, the
map Z // W is dominant. The surjectivity of Y // X implies that the restriction

Y |W // W

is dominant. Therefore, by Lemma 4.7,

RD(Y |Z // Z) ≤ RD(Y |W // W )

≤ dim(W )

≤ dim(X).

Lemma 4.9. Let Y // X be a generically ﬁnite dominant map. Then Deﬁnition 4.6
specializes to Deﬁnition 4.1 for Y // X, i.e. they give equivalent notions of resolvent
degree.

Proof. By Lemma 4.7 4 and [FW19, Lemma 2.6], it suﬃces to prove this when Y is irre-
ducible. In this case, any rational multi-section U ⊂ Y of Y // X must be dense in Y . In
particular, it must be birational to Y . From the birational invariance of RD for generically
ﬁnite dominant maps, we conclude that RD(U // X) = RD(Y // X) (as generically ﬁnite
dominant maps). The lemma follows.
 23

Lemma 4.10. Let Z π1 // Y π2 // X be a pair of dominant maps of K-varieties. Then

RD(Z // X) ≥ RD(Y // X)

and
 RD(Z // X) ≤ max{RD(Z // Y ), RD(Y // X)}.

with equality when either Z // Y or Y // X is generically ﬁnite.

Proof. For the ﬁrst inequality, let {Uα ⊂ Z} be a dense set of rational multi-sections of
Z // X with RD(Uα // X) ≤ d for all α. Then, shrinking each Uα as necessary (e.g.
restricting to the preimage in U of an aﬃne open in Y ), its (scheme theoretic) image
Vα := Image(Uα // Y ) is a subscheme of Y , and thus a rational multi-section of Y // X.
Since Z // Y is dominant, that {Uα ⊂ Z} is dense implies that {Vα ⊂ Y } is dense. By
[FW19, Lemma 2.7], we conclude that RD(Uα // X) ≥ RD(Vα // X). Minimizing over all
{Uα ⊂ Z}, we conclude that
 RD(Z // X) ≥ RD(Y // X).

For the second inequality, let {Uα ⊂ Z} be a dense set of rational multi-sections for Z // Y
and {Vβ ⊂ Y } a dense set of rational multi-sections for Y // X. Then

{Wα,β := Uα ×Y Vβ ⊂ Z}

is a dense set of rational multi-sections for Z // X. By [FW19, Lemmas 2.5, 2.7],

RD(Wα,β // X) ≤ max{RD(Uα // Y ), RD(Vβ // X)}.

Minimizing over all such collections {Uα}, {Vβ }, we conclude

RD(Z // X) ≤ max{RD(Z // Y ), RD(Y // X)}.

To show the equalities when dim(Y ) = dim(X) or dim(Z) = dim(Y ), it suﬃces, by Lemma
4.7(4), to prove the case when X and Y are irreducible. Under this assumption, if dim(X) =
dim(Y ) or if dim(Z) = dim(Y ), then any rational multi-section U for Z // Y is a rational
multi-section for Z // X and vice versa. In particular,

RD(U // Y ) ≤ RD(U // X)

and taking the minimum over dense subsets of such, we see that RD(Z //Y ) ≤ RD(Z //X).
The equality RD(Z // X) = max{RD(Z // Y ), RD(Y // X)}

follows from what we have shown above.

Special cases of the following are implicit in [Se45, Br45, Br75].

24

Proposition 4.11. Let Y // X be a dominant map of K-varieties. Let S // X be a
map such that the generic ﬁber is a Severi-Brauer variety over K(X), and let K(X) be an
algebraic closure of K(X). Suppose that there exists an embedding over X

Y ֒→ S

such that the closure of the geometric generic ﬁber Y |K(X) in S|K(X) ∼= Pn
K(X) has degree
d. Then RD(Y // X) ≤ RD(d) < d.

Proof. By the Merkurjev-Suslin theorem [MS83, Theorem 16.1], using that K is a ﬁeld
of characteristic 0, there exists a solvable extension L./K(X) such that S|Spec(L) ∼= Pn
L.
Because we are in characteristic 0, the extension L/K(X) is separable, so picking a primitive
element z and writing L ∼= K(X)(z), we can, by clearing denominators in the minimal
polynomial for z over K(X) and using that the discriminant of this minimal polynomial is
not identically 0, realize L as K(E) for E ⊂ A1
X a locally closed subvariety such that the
projection E // X is solvable and ´etale. Shrinking E as needed, we can extend the above
isomorphism S|Spec(L) ∼= Pn
L to an isomorphism S|E ∼= Pn
E. We conclude that the embedding
Y ֒→ S pulls back to an embedding
 Y |E ֒→ S|E ∼= Pn
E

whose closure is a degree d subvariety. Points of Y |E are thus of degree at most d over K(E)
(and the generic point is of degree d). Therefore, by [FW19, Lemma 2.9], Y |E admits a
dense set of rational multi-sections {Uα ⊂ Y |E} with RD(Uα //E) ≤ RD(d). The images of
these rational multi-sections in Y , {Vα ⊂ Y } are thus a dense set of rational multi-sections,
and by [FW19, Lemma 2.6], we have

RD(Vα // X) ≤ RD(Uα // E // X)

= max{RD(Uα // E), RD(E // X)}

≤ max{RD(d), 1} = RD(d) < d.

Now let X be a variety, and let An
X,a be the parameter space for n-valued algebraic
functions on X as in Section 3. Observe that the action of Gm on algebraic functions by
rescaling their values corresponds to a weighted action Gm ⟲ An
X,a where

λ · (a1, . . . , an) = (λa1, . . . , λnan).

Moreover, if Z ⊂ An
X,a is weighted homogeneous with respect to this action, then ev−1(Z) ⊂
TΦ is homogeneous (with respect to the diagonal action of Gm on An
X,b).

Lemma 4.12. Let X be an irreducible K-variety. Let Φ be an algebraic function on X.
Let Z ⊂ An
X,a be a Zariski closed subvariety which is weighted homogeneous (relative to the
above action). Let U ⊂ ev−1(Z) ⊂ TΦ

be any rational multi-section for ev−1(Z) // X. Then

RD(Φ) ≤ max{RD(U // X), dim(Z) − 1}.

25

Proof. The multi-section U // ev−1(Z) determines a Tschirnhaus transformation T of Φ|U
which is rational over K(U ). By the observations above, we have a pullback square

(EΦ)|U //❴❴❴

  
 (EPn)|Z

  
U //❴❴❴❴❴❴ Z

Since Z is weighted homogeneous, we can projectivize (EPn)Z // Z to obtain a pullback
square (EΦ)|U //❴❴❴

  
 P(EPn)|P(Z)

  
U //❴❴❴❴❴❴ P(Z)

where P(Z) ⊂ P(An
a) and P(An
a) now denotes the weighted projective space. The result now
follows by applying Lemmas 4.7 and 4.10.

5 Hilbert’s Formula for the Degree 9 and New General Up-
per Bounds

We now apply the results of the previous sections to complete and extend Hilbert’s argu-
ment from [Hi27]. We work throughout this section over an algebraically closed ﬁeld K of
characteristic 0.
Let Hd,N denote the parameter space of degree d hypersurfaces in PN , i.e. Hd,N ∼=
P(
N+d
d )−1. Let Md,N denote the coarse moduli space of smooth hypersurfaces, i.e

Md,N = (Hd,N − Σ)/ PGLN +1

where Σ denotes the locus of singular hypersurfaces. Let Hr
d,N denote the space of such
hypersurfaces with a choice of r-plane on them, i.e. Hr
d,N is the incidence variety

Hr
d,N := {(X, L) ∈ Hd,N × Gr(r + 1, N + 1) | L ⊂ X}.

Similarly to above, let Mr
d,N denote the moduli of smooth degree d hypersurfaces equipped
with an incident r-plane, i.e.
 M
r
d,N = (Hr
d,N − ˜Σ)/ PGLN +1,

where ˜Σ ⊂ Hr
d,N denotes the locus where the hypersurface is singular.
We will need the following theorem of Waldron [Wa08, Theorem 1.6] (see also [St17,
Theorem 1.2]).

Theorem 5.1 (Waldron). Let d ≥ 3. The map

Hr
d,N // Hd,N

is surjective for r, N such that

(r + 1)(N − r) − (d + r
r
 ) ≥ 0.

26

Motivated by this theorem, we introduce the following notation:

Notation 5.2. Given (d, k) ∈ N≥3 × N, deﬁne

ψ(d, k)0 = k.

For 0 ≤ i < d − 2, deﬁne

ψ(d, k)i+1 = ⌈ψ(d, k)i + (ψ(d, k)i + d − i
ψ(d, k)i
 )/(ψ(d, k)i + 1)⌉.

Finally, deﬁne
 ψ(d, k)d−1 = 2ψ(d, k)d−2 + 1.

By Waldron’s Theorem, for all 0 ≤ i < d − 2, the map

Hψ(d,k)i
d−i,ψ(d,k)i+1 // Hd−i,ψ(d,k)i+1

is surjective. Similarly, by the classical theory of quadratic forms, the locus of smooth
quadrics is contained in the image of the map

Hψ(d,k)d−2
2,ψ(d,k)d−1 // H2,ψ(d,k)d−1

In words, the integers ψ(d, k)i are deﬁned so that every smooth quadric in a Pψ(d,k)d−1
contains a ψ(d, k)d−2 plane, every cubic hypersurface in this ψ(d, k)d−2 plane contains a
ψ(d, k)d−3 plane, every quartic in this ψ(d, k)d−3 plane contains a ψ(d, k)d−4 plane, and on
down until we arrive at a ψ(d, k)1 plane such that every degree d hypersurface inside it
contains a k-plane.

Lemma 5.3. For all d ≥ 2 and all k ≥ 1,

dim(M3,ψ(d,k)d−2 ) ≥ max{dim(Hd−i,ψ(d,k)i+1 )}
d−3
i=0

and
 dim(M3,ψ(d,k)d−2 ) + d + k + 1 ≥ ψ(d, k)d−1 + 2.

Proof. For each i,
 dim(Hd−i,ψ(d,k)i+1) = (d − i + ψ(d, k)i+1
d − i
 ) − 1

From the deﬁnition of the ψ(d, k)is, we conclude for all i that

dim(Hd−i,ψ(d,k)i+1) ≥ dim(Hd−i+1,ψ(d,k)i)

and thus
 dim(H4,ψ(d,k)d−3 ) = max{dim(Hd−i,ψ(d,k)i+1 )}
d−4
i=0 .

27

Similarly,
 dim(M3,ψ(d,k)d−2 ) = max{0, (3 + ψ(d, k)d−2
3
 ) − (ψ(d, k)d−2 + 1)
2}.

From the deﬁnition, this is a maximum of a ceiling function of a monotone increasing
degree 6 polynomial in ψ(d, k)d−3, all of whose derivatives are monotone increasing in the
domain ψ(d, k)d−3 ≥ 1, while dim(H4,ψ(d,k)d−3) is a monotone increasing quartic, all of
whose derivatives are monotone increasing in the same domain. Therefore, the inequality

dim(M3,ψ(d,k)d−2 ) ≥ dim(H4,ψ(d,k)d−3 )

for all (d, k) follows from the equality for (d, k) = (3, 1) and direct inspection of the higher
derivatives of the sextic and quartic polynomials in the interval ψ(d, k)d−3 ≥ 1 (for which
both left and right hand side equal 4; note that the inequality is vacuously true for (d, k) =
(2, 1)).
Finally, from the deﬁnition,

ψ(d, k)d−1 + 2 = 2ψ(d, k)d−2 + 3.

By the same reasoning as above, the inequality

dim(M3,ψ(d,k)d−2 ) + d + k + 1 ≥ ψ(d, k)d−1 + 2

for all (d, k) ∈ N≥2 × N>0 follows from the inequality for (d, k) = (2, 1) (in which case the
left hand side is 8 and the right hand side is 4).

The lemma implies that for d ≥ 3, dim(M3,ψ(d,k)d−2) gives a coarse upper bound on the
resolvent degree of the surjective maps

M
ψ(d,k)d−3
3,ψ(d,k)d−2 // M3,ψ(d,k)d−2

Hψ(d,k)i
d−i,ψ(d,k)i+1 // Hd−i,ψ(d,k)i+1.

This motivates the following deﬁnition.

Deﬁnition 5.4. Given (d, k) ∈ N≥2 × N>0, deﬁne

Φ(d, k) := max{ (d + k)!
d! + 1, dim(M3,ψ(d,k)d−2 ) + d + k + 1}

For r ∈ N≥4, deﬁne
 F(r) := 2⌊ 1
2 · ( min
d+k+1=r Φ(d, k)
)⌋ + 1. (5.1)

For r ≤ 3, deﬁne F(r) = r + 1.

Lemma 5.5. For all r ∈ N, F(r + 1) > F(r), i.e. F is monotone increasing.

Proof. The maximum of two monotone increasing functions is monotone increasing, as is
any linear combination with positive integer coeﬃcients of the integer part of a monotone
increasing function.
 28

We can now state our ﬁrst main theorem.

Theorem 5.6. Let F : N //N be the monotone increasing function (5.1). For all n ≥ F(r),

RD(n) ≤ n − r.

Example 5.7. Observe that

F(5) = Φ(3, 1) = max{ 4!
3! + 1, dim(M3,3) + 5}

= max{5, 9} = 9.

The theorem thus asserts that for n ≥ 9, RD(n) ≤ n − 5, as ﬁrst stated by Hilbert.

We can compare the upper bounds of Theorem 5.6 to Brauer’s bounds as follows. Both
the previous theorem and Brauer’s theorem prove the existence, for each r, of an explicit
cut-oﬀ (for n) after which RD(n) ≤ n − r. More precisely, deﬁne

B(r) := (r − 1)! + 1.

Brauer proved [Br75, Theorem 1] that for n ≥ B(r),

RD(n) ≤ n − r.

The cut-oﬀ functions B(r) and F(r) are related as follows.

Theorem 5.8. Let B(r) and F(r) be as above. There exists a monotone increasing function
ϕ : N // N, such that ϕ(2) = 5, and such that for r ≥ ϕ(d),

B(r)/ F(r) ≥ d!

In particular, F(r) ≤ B(r) for all r and

lim
r→∞ B(r)/ F(r) = ∞.

Remark 5.9.

1. As remarked above, Brauer’s bound B(r) gives the best prior general bound once
r ≥ 7; in this range, Theorem 5.8 shows that F is the best current bound. For r = 6,
Sylvester [Sy1887] proved that the bound n = 44 is suﬃcient, while for r = 5, Segre
and Dixmier proved that n = 9 suﬃces. In Appendix A, we give explicit computations
of F(r) for r up to 15 (at which point F(r) is approximately 3.6 billion). In particular,
we see that F(5) = 9 recovers the Hilbert-Wiman-Segre-Dixmier bound, and F(6) = 41
improves Sylvester.

2. We do not expect that the upper bounds of Theorem 5.6 are themselves sharp for
two reasons: ﬁrst, we expect that further optimizations to the present method should
be possible; and second, we have not made contact in this paper with the methods
introduced by Sylvester and Hammond [Sy1887, SH1887, SH1888] in their study of
Hamilton’s work [Ha1836].

It remains to prove Theorems 5.6 and 5.8.

29

5.1 Proof of Theorem 5.6

Our proof follows the strategy outlined by Hilbert [Hi27]. We recall a classical lemma on
quadrics.

Lemma 5.10. Let K be a ﬁeld of characteristic 0, let K ⊂ K be an algebraic closure, and
let K 2-solv ⊂ K denote the quadratic closure of K. For any smooth quadric Q over K, with
maximal isotropic Grassmannian Gr(Q), the inclusion

Gr(Q)(K 2-solv) ⊂ Gr(Q)(K)

is Zariski dense. Moreover, for any x ∈ Gr(Q)(K 2-solv), the associated Severi-Brauer vari-
ety over K 2-solv is trivial.

Proof. The proof is classical, and goes back at least to work of Sylvester. Recall that
by completing the squares, every nonsingular, deﬁnite quadratic form Q over K admits a
K-rational change of coordinates to one of the form

Q′(x1, . . . , xn) = a1x2
1 + · · · + anx2
n (5.2)

for ai ∈ K ×. For example, see [Fo36] for explicit formulas for the ai in terms of minors of
the matrix associated to the quadratic form (n.b. Fort states the results for real deﬁnite
forms, but the method holds over any base ﬁeld).
Let L = K(
√a1, . . . , √an) ⊂ K 2-solv. The L-rational change of coordinates

xi =: yi
√ai

converts the above quadratic form (5.2) to

Q′′(y1, . . . , yn) = y2
1 + · · · + y2
n.

Finally, let L′ = L(
√−1) ⊂ K 2-solv. Then the quadratic form Q′′ vanishes identically on
the linear subspace Λ deﬁned by
 y2i−1 = √
−1y2i

for i = 1, . . . , ⌊ n
2 ⌋. Counting the dimension, Λ is a maximal isotropic, i.e.

Λ ∈ Gr(Q)(L′) ⊂ Gr(Q)(K 2-solv).

Using that Gr(Q) is a homogeneous space for the algebraic group O(Q), and that K (and
thus L′) is an inﬁnite ﬁeld, we conclude that the O(Q)(L′) orbit of Λ is dense in Gr(Q)( ¯K)
as claimed. Finally, because Λ has an L′ point (e.g. for n even [y1 : · · · : yn] = [
√−1 : 1 :
· · · : √−1 : 1], with the analogous formula if n is odd), the Severi-Brauer variety associated
to Λ over L′ splits completely. We conclude the same for every point in the O(Q)(L′) orbit
of Λ.

Corollary 5.11. Let X be a variety over a ﬁeld K of characteristic 0. For any generically
smooth family of quadrics Q // X, the solvable multi-sections of Gr(Q) // X are Zariski
dense in Gr(Q)( ¯K(X)).
 30

Proof of Theorem 5.6. Because F is a monotone increasing function (by Lemma 5.5), if
n ≥ F(r), then n − 1 ≥ F(r − 1). We can therefore induct on r.
For n ≤ 4, solutions in radicals imply RD(n) = 1. That RD(n) ≤ n − 4 for n ≥ 5 follows
from Bring [Br1786] and Hamilton [Ha1836]. We reprove this Bring-Hamilton bound as the
base of our induction, in order to show the uniform general method; simple modiﬁcations
of the below can be used to rederive the bound F(r) for r ≤ 3.
For n ≥ 5 we have a generically smooth family of quadrics T12 // An
a (by Lemma 2.7)
of dimension at least 2. By Lemma 5.10, there exists a solvable branched cover

U1 // An
a

with a map over An
a to the relative Grassmannian of maximal isotropics Gr(T12), i.e. there
exists a linear embedding L : U1 × P⌊ n−3
2 ⌋ // T12|U .

Because n ≥ 5, the dimension of the linear subspaces is at least 1. We can therefore intersect
with T3|U1 to get a rational map
 U1 99K A3

u ↦→ L(u) ∩ T3.

Adjoining the solution of this family of cubics, we get a solvable branched cover

U2 // U1

and a map U2 // T123. By Lemma 4.12, we conclude that

RD(n) ≤ max{RD(U2 // An
a), dim(An−3
a1=a2=a3=0) − 1}

= max{1, n − 4} = n − 4.

For the induction step, let r ≥ 5 and assume that we have shown that for all s < r,
n ≥ F(s) implies that RD(n) ≤ n − s. Let n ≥ F(r). Note that if mind+k+1=r Φ(d, k) is
odd, then the deﬁnition of F implies that

F(r) = min
d+k+1=r Φ(d, k).

Conversely, if mind+k+1=r Φ(d, k) is even, then

F(r) = min
d+k+1=r Φ(d, k) + 1.

Consequently, if n is odd, then
 n ≥ min
d+k+1=r Φ(d, k),

while if n is even
 n ≥ min
d+k+1=r Φ(d, k) + 1.

31

Let (d, k) be such that Φ(d, k) = min
d′+k′+1=r Φ(d
′, k′).

If n is odd (and thus n ≥ Φ(d, k)), we will explicitly construct a rational multi-section

U // T1···d+k

for T1···d+k // An
a with

RD(U // An
a) ≤ max{RD( (d + k)!
d! ), dim(M3,ψ(d,k)d−2 )}.

If n is even (and thus n ≥ Φ(d, k) + 1), mutatis mutandis the same argument will produce
a rational multi-section U // T ′
1···d+k

with RD(U // An
a) ≤ max{RD( (d+k)!
d! ), dim(M3,ψ(d,k)d−2 )}.

Case 1: n odd. Let U1 = An
a. By Lemma 2.7, the family T12 // An
a is generically smooth.
By Corollary 2.14, there exists a dense open V ⊂ Gr(T12), such that

L|V ×Pn
An
a T123 // An
a

is smooth (i.e. for the generic polynomial, the intersection of T123(a) with a generic maximal
isotropic in T12(a) is smooth).
By Corollary 5.11, RD(V // An
a) = 1

More precisely, there exists a multi-section U2 ⊂ V such that U2 // U1 is a solvable cover
of its image, and such that
 L|U2 ∼= P
 n−3
2
U2 .

Now, by Lemma 5.3 and our assumption on n,

n ≥ Φ(d, k) ≥ ψ(d, k)d−1 + 2

= 2ψ(d, k)d−2 + 3.

Therefore,
 n − 3
2 ≥ ψ(d, k)d−2

If n−3
2 = ψ(d, k)d−2, then we obtain a map

U2 // M3,ψ(d,k)d−2
x ↦→ L|x ×Pn−2 T123|x.

If n−3
2 > ψ(d, k)d−2, by the Bertini Theorem for isotropics (Proposition 2.13), there exists
a dense open V ′ ⊂ Gr(ψ(d, k)d−2, L|U2)

32

such that the family of cubic hypersurfaces in Pψ(d,k)d−2 given by

V ′ ×L|U2 (T123 ×Pn−2
U1 L|U2) // U2

is generically smooth. Because rational points are dense in Grassmannians, perhaps after
shrinking U2, we obtain a section U2 // V ′. As above, we again obtain a map

U2 ∩T123 // M3,ψ(d,k)d−2 .

Note that, from the construction above, RD(U2 // U1) = 1.
By Waldron’s Theorem (Theorem 5.1) and the deﬁnition of the numbers ψ(d, k)i, the
map M
ψ(d,k)d−3
3,ψ(d,k)d−2 // M3,ψ(d,k)d−2

is surjective. Therefore, the map
 M
ψ(d,k)d−3
3,ψ(d,k)d−2|U2 // U2

is surjective, and by Lemma 4.8,

RD(M
ψ(d,k)d−3
3,ψ(d,k)d−2 |U2 // U2) ≤ dim(M3,ψ(d,k)d−2 ).

Let U ′ ⊂ M
ψ(d,k)d−3
3,ψ(d,k)d−2 |U2 be any rational multi-section such that

RD(U ′ // U2) = RD(M
ψ(d,k)d−3
3,ψ(d,k)d−2 |U2 // U2).

Let ¯L // M
ψ(d,k)d−3
3,ψ(d,k)d−2 denote the tautological ψ(d, k)d−3-plane bundle. By the Merkurjev-
Suslin Theorem [MS83, Theorem 16.1], there exists a solvable ´etale map U3 // U ′ such
that ¯L|U3 ∼= Pψ(d,k)d−3
U3 .

By Lemma 4.10 and the construction above,

RD(U3 // U2) = max{RD(U ′ // U2), 1} ≤ dim(M3,ψ(d,k)d−2 ).

Further, intersecting with the Tschirnhaus hypersurface T4, we obtain a map

U3 ∩T4 // H4,ψ(d,k)d−3
x ↦→ (T123|x ×U3 ¯L|U3) ×Pn−1
U3 T4|U3.

By induction, we now construct, for each 4 ≤ i ≤ d, a quasi-ﬁnite dominant map

Ui // Ui−1

such that

1. RD(Ui // Ui−1) ≤ dim(Hi,ψ(d,k)d−i+1 ),

33

2. we have a commuting diagram

Ui //

  
 Hψ(d,k)d−i
i,ψ(d,k)d−i+1

  
Ui−1 ∩Ti // Hi,ψ(d,k)d−i+1

with a trivialization L|Ui ∼= Pψ(d,k)d−i
Ui ,

where L // Hψ(d,k)d−i
i,ψ(d,k)d−i+1 denotes the tautological ψ(d, k)d−i-plane bundle;

3. and the assignment
 x ↦→ (T1···i|x ×Ui Li,ψ(d,k)d−i+1|Ui) ×Pn−1
Ui Ti+1|x

deﬁnes a map
 Ui ∩Ti+1 // Hi+1,ψ(d,k)d−i.

The construction proceeds along the same lines as the construction of U3 above. Given Ui−1
with the map
 Ui−1 ∩Ti // Hi,ψ(d,k)d−i+1,

by the deﬁnition of the ψ(d, k)j s and Waldron’s Theorem (Theorem 5.1), the map

Hψ(d,k)d−i
i,ψ(d,k)d−i+1 // Hi,ψ(d,k)d−i+1

is surjective. Therefore, the map

Hψ(d,k)d−i
i,ψ(d,k)d−i+1|Ui−1 // Ui−1

is surjective, and by Lemma 4.8,

RD(Hψ(d,k)d−i
i,ψ(d,k)d−i+1|Ui−1 // Ui−1) ≤ dim(Hi,ψ(d,k)d−i+1).

Let U ′ ⊂ Hψ(d,k)d−i
i,ψ(d,k)d−i+1|Ui−1 be any rational multi-section such that

RD(U ′ // Ui−1) = RD(Hψ(d,k)d−i
i,ψ(d,k)d−i+1|Ui−1 // Ui−1).

Let L // Hψ(d,k)d−i
i,ψ(d,k)d−i+1 denote the tautological ψ(d, k)d−i-plane bundle. By the Merkurjev-
Suslin Theorem [MS83, Theorem 16.1], there exists a solvable ´etale map Ui // U ′ such
that L|Ui ∼= Pψ(d,k)d−i
Ui .

By Lemma 4.10 and the construction above,

RD(Ui // Ui−1) = max{RD(U ′ // Ui−1), 1} ≤ dim(Hi,ψ(d,k)d−i+1).

34

Finally, to complete the induction step, we observe that, by intersecting with the Tschirn-
haus hypersurface Ti+1, we obtain a map

Ui ∩Ti+1 // Hi+1,ψ(d,k)d−i
x ↦→ (T1···i|x ×Ui L|Ui) ×Pn−1
Ui Ti+1|Ui.

This completes the induction step. We have thus constructed a tower of maps

Ud // · · · // U4 // U3 // U2 // U1 = An
a.

Further, from the inductive construction and Lemmas 4.10 and 5.3, we have

RD(Ud // An
a) ≤ dim(M3,ψ(d,k)d−2).

Now let L // Hd,ψ(d,k)1 denote the tautological k-plane bundle (n.b. k = ψ(d, k)0). Then,
by construction, we have an isomorphism

L|Ud ∼= Pk
Ud.

For i1 < . . . < ik, and N , let Hi1···ik,N

denote the parameter space of complete intersections of degree (i1, . . . , ik). Let

I // Hi1···ik,N

denote the tautological family of complete intersections. By Proposition 4.11,

RD(I // Hi1···ik,N ) ≤ RD(i1 · · · ik).

By our inductive construction, we have a map

Ud ∩T(d+1)···(d+k) // H(d+1)···(d+k),k
x ↦→ (T1···d|x ×Ud L|Ud) ×Pn−1
Ud T(d+1)···(d+k)|Ud.

Because, I // H(d+1)···(d+k),k is surjective, by Lemma 4.8,

RD(I|Ud // Ud) ≤ RD( (d + k)!
d! ).

Let Ud+1 ⊂ I|Ud be a rational multi-section of I|Ud // Ud such that

RD(Ud+1 // Ud) ≤ RD( (d + k)!
d! ).

Then, by construction, Ud+1 carries a canonical map

Ud+1 // T1···(d+k)

35

making it a rational multi-section of the Tschirnhaus complete intersection. Further, by
the above construction and Lemma 4.10,

RD(Ud+1 // An
a) ≤ max{RD( (d + k)!
d! ), dim(M3,ψ(d,k)d−2 )}.

By assumption, n ≥ F(r) = Φ(d, k) ≥ (d+k)!
d! + 1. Lemma 5.5 thus implies that (d+k)!
d! ≥
F(r − 1). Therefore, by the inductive hypothesis,

RD( (d + k)!
d! ) ≤ (d + k)!
d! − (r − 1).

Moreover, from the deﬁnition of Φ(d, k), n ≥ Φ(d, k) implies that n ≥ dim(M3,ψ(d,k)d−2 )+r.
By Lemma 4.12, we therefore conclude that

RD(n) ≤ max{RD(Ud+1 // An
a), dim(ev(T1···(d+k))) − 1}

≤ max{ (d + k)!
d! − (r − 1), dim(M3,ψ(d,k)d−2 ), n − r.}

= n − r.

Case 2: n even. Let U1 = An
a. By Lemma 2.7, the family T ′
12 //An
a is generically smooth.

By Corollary 2.14, there exists a dense open V ⊂ Gr(T ′
12), such that

L|V ×Pn
An
a T ′
123 // An
a

is smooth (i.e. for the generic polynomial, the intersection of T ′
123(a) with a generic maximal
isotropic in T ′
12(a) is smooth).
By Corollary 5.11, RD(V // An
a) = 1

More precisely, there exists a multi-section U2 ⊂ V such that U2 // U1 is a solvable cover
of its image, and such that L|U2 ∼= P
 n
2 −2
U2 .

Now, by Lemma 5.3 and our assumption on n

n − 1 ≥ Φ(d, k) ≥ ψ(d, k)d−1 + 2

= 2ψ(d, k)d−2 + 3.

Therefore,
 n
2 − 2 ≥ ψ(d, k)d−2

If n
2 − 2 = ψ(d, k)d−2, then we obtain a map

U2 // M3,ψ(d,k)d−2
x ↦→ L|x ×Pn−2 T ′
123|x.

36

If n
2 − 2 > ψ(d, k)d−2, by the Bertini Theorem for isotropics (Proposition 2.13), there exists
a dense open V ′ ⊂ Gr(ψ(d, k)d−2, L|U2)

such that the family of cubic hypersurfaces in Pψ(d,k)d−2 given by

V ′ ×L|U2 (T ′
123 ×Pn−2
U1 L|U2) // U2

is generically smooth. Because rational points are dense in Grassmannians, perhaps after
shrinking U2, we obtain a section U2 // V ′. As above, we again obtain a map

U2 ∩T ′
123 // M3,ψ(d,k)d−2 .

Note that, from the construction above, RD(U2 // U1) = 1. The remainder of the proof
now proceeds exactly as in the case of n odd.

5.2 Proof of Theorem 5.8

Proof of Theorem 5.8. We deduce the theorem from the following:

Claim 1. There exists a monotone increasing function ρ : N // N such that

1. for k ≥ ρ(d),
 (d + k)!
d! + 1 = Φ(d, k)

≤ Φ(d − 1, k + 1)

(i.e. both conditions hold for k ≥ ρ(d));

2. for all k < ρ(d), either Φ(d, k) > Φ(d − 1, k + 1).

or (d + k)!
d! + 1 ̸= Φ(d, k)

(i.e. ρ(d) is the least integer such that both conditions hold).

Granting the claim, let ϕ(d) := ρ(d + 1) + d + 2. From Deﬁnition 5.4, we see that
ρ(3) = 2, and thus ϕ(2) = 6. However, F(5) = 9 while B(5) = 25, so we can modify ϕ by
setting ϕ(2) := 5 as claimed. Moreover, for r ≥ ϕ(d), we have

k := (r − 1) − (d + 1)

≥ ϕ(d) − (d + 2)

≥ ρ(d + 1)

As a result,
 F(r) = (r − 1)!
(d + 1)! + 1

37

and therefore,
 B(r)/ F(r) = (r − 1)! + 1
(r − 1)!/(d + 1)! + 1
≥ d!

We now prove Claim 1 by asymptotic estimates; more precisely, we show that for each d,
dim(M3,ψ(d,k)d−2) grows polynomially in k, while (d+k)!
d! grows superexponentially. Precise
formulas for the function ρ require a more detailed analysis.
Continuing to follow Notation 5.2, we claim the following:

Claim 2. Fix d. Then as a function of k,

O((d + k)!) ≥ max{O(dim(M3,ψ(d,k)d−2 )), O(dim(M3,ψ(d−1,k+1)d−3 ))}),

where O(f ) denotes the asymptotic growth of a function f .

Granting the claim, we see that for k >> d,

Φ(d, k) = (d + k)!
d! < (d + k)!
(d − 1)! = Φ(d − 1, k + 1).

Note that by deﬁnition,

Φ(d, k) = max{ (d + k)!
d! + 1, dim(M3,ψ(d,k)d−2 ) + d + k + 1}

Therefore Claim 1 follows from Claim 2. To prove Claim 2, recall Stirling’s formula (cf.
[Ro55]) √
2πmm+ 1
2 e 1
12m+1 −m ≤ m! ≤ √2πmm+ 1
2 e 1
12m −m

This implies that
 O(ln((d + k)!)) = O((d + k + 1
2 ) ln(d + k)).

It suﬃces to prove that

max{O(dim(M3,ψ(d,k)d−2 )), O(dim(M3,ψ(d−1,k+1)d−3 ))} = O(kαd)

for some αd, as then

max{O(ln(dim(M3,ψ(d,k)d−2 ))), O(ln(dim(M3,ψ(d−1,k+1)d−3 )))} = O(αd · ln(k))

≤ O((d + k + 1
2 ) ln(d + k))

= O(ln(d + k)!).

Recall that ψ(d, k)0 = k and for i > 0,

ψ(d, k)i = ⌈ψ(d, k)i−1 + (ψ(d, k)i−1 + d − (i − 1)
ψ(d, k)i−1
 )/(ψ(d, k)i−1 + 1)⌉.

38

Therefore
 ψ(d, k)i ∼ (d − i + 1 + ψ(d, k)i−1) · · · (ψ(d, k)i−1 + 2)
(d − i + 1)! ∼ (ψ(d, k)i−1)
d−i.

Because ψ(d, k)1 ∼ kd−1, by induction, we obtain

dim(Hd−i,ψ(d,k)i+1) = (d − i + ψ(d, k)i+1
ψ(d, k)i+1
 ) − 1

∼ ψ(d, k)
d−i
i+1

∼ k(d−i) (d−1)!
(d−i−2)! .

Similarly,

dim(M3,ψ(d,k)d−2 ) ∼ k3(d−1)!.

By the same argument,

dim(M3,ψ(d−1,k+1)d−3 ) ∼ (k + 1)
3(d−2)! ∼ k3(d−2)!,

and, thus, as functions of k,

O((d + k)!) ≥ max{O(dim(M3,ψ(d,k)d−2 )), O(dim(M3,ψ(d−1,k+1)d−3 ))}

as claimed.
 39

A Explicit Bounds

Table 1: Upper Bounds on RD(n)
r F(r) Best Prior Bound B′(r) Source of B′(r) B′(r)/ F(r) (d, k)
2 3 3 Babylonians 1
3 4 4 Ferrari 1
4 5 5 Bring [Br1786] 1 (2,1)
5 9 9 Segre [Se45] 1 (3,1)
6 41 44 Sylvester [Sy1887] 1.07 (3,2)
7 121 721 Brauer [Br75] 5.95 (3,3)
8 841 5041 ” 5.99 (3,4)
9 6721 40321 ” 5.99 (3,5)
10 60481 362881 ” 5.99 (3,6)
11 604801 3628801 ” 5.99 (3,7)
12 6652801 39916801 ” 5.99 (3,8)
13 78485043 12! + 1 ” 6.10 (4,8)
14 320082459 13!+1 ” 19.45 (4,9)
15 3632428801 14!+1 ” 24 (4,10)

Table 2: In the rightmost column above, k is the dimension of the linear subspace on the
degree d hypersurface that we use to construct the necessary Tschirnhaus transformation,
e.g. for r = 5, (d, k) = (3, 1) and we are using a line on a cubic surface `a la Hilbert to prove
F(5) = 9.

B Historical Background.

“The theory has been a plant of slow growth.”
(Sylvester and Hammond, 18877)

Tschirnhaus [Ts1683] introduced his transformationto show that RD(n) ≤ n − 3, improving
upon the linear change of variables used by the Babylonians to set the ﬁrst coeﬃcient of
the general polynomial to 0. A century later, Bring [Br1786] improved this for n = 5 to
show that RD(5) = 1. Hamilton [Ha1836] was the ﬁrst to show that

lim
n // ∞ n − RD(n) = ∞.

More precisely, he showed the existence a monotone increasing function H : N // N, such
that n − RD(n) ≥ r for n ≥ H(r).8 Hamilton computed the initial values of H (for r ≤ 7).
Five decades later, Sylvester [Sy1887] extended Hamilton’s computations to give:

r 4 5 6 7 8 9
H(r) 5 11 47 923 409, 619 83, 763, 206, 255

7[SH1887, p. 286]
8The numbers H(r) are listed as the “Hamilton numbers” in the Online Encyclopedia of Integer Sequences.

40

Sylvester then sharpened Hamilton’s bounds slightly (see [Sy1887, p. 485])9, and Sylvester
and Hammond [SH1887], [SH1888] gave a generating function for H.
Preceding Sylvester (and apparently unbeknownst to him at the time of [SH1887]), Klein
[Kl1871] initiated a new approach to solving polynomials, linking it with group theory,
representation theory, projective geometry, classical invariant theory, and the theory of
elliptic and automorphic functions. Fundamental to Klein’s vision was the goal of reducing a
given algebraic function to a simplest possible “normal form”, with the ideal being a normal
form given by the action of the monodromy group of the function on a projective space of
minimal dimension.10 For n = 5, 6, 7, this program allowed Klein [Kl1884, Kl1887, Kl1905]
to reproduce the Bring/Hamilton bounds of RD(n) ≤ n − 4 with substantial simpliﬁcations
in both the algebra of the formulas and the geometry of the normal forms involved. Klein
also popularized the problem of ﬁnding simplest solutions of polynomials [Kl1908, Second
Part, Ch. II], was the ﬁrst, or among the ﬁrst, to explicitly consider the problem of lower
bounds for RD [Kl1894, Kl1905], and worked, over a 50 year span, to anchor this problem
ﬁrmly within the central mathematical concerns of his time (see also [Kl1888, Kl1879], and
more generally [Kl22, Fr26]).
In his 1900 address at the Universal Exposition in Paris, Hilbert [Hi1900, Problem 13]
explicitly posed the problem of the non-existence of 2-variable formulas for the general
degree 7 polynomial. Hilbert’s address cements two decisive shifts for the problem: ﬁrst,
he explicitly called attention to the question of lower bounds on resolvent degree, made
conjectures as to lower bounds, and advocated for this as the fundamental problem. Second,
Hilbert built upon Enriques’ 1897 ICM address [En1897] by generalizing the problem to
encompass formulas using analytic functions and even continuous ones; he then proved by a
dimension count that the general three variable analytic function does not admit a formula
in analytic functions of two or fewer variables. Hilbert returned to this problem at the
end of his career in [Hi27], where he explicitly conjectured that RD(6) = 2, RD(7) = 3,
RD(8) = 4, and then sketched a beautiful geometric idea to lower RD(9) to at most 4.
Shortly after, Wiman [Wi27] sketched another approach to showing RD(n) ≤ n − 5 for
n ≥ 9. As Dixmier observed [Di93], there are gaps in both Hilbert and Wiman’s proofs due
to their assuming certain forms are suﬃciently generic.
Progress on the general problem of bounding RD(n) stalled after Hilbert. N. Chebotarev
highlighted this and related questions in his 1932 ICM address [Ch32], and in several papers
in the 1930s and 1940s [Ch31a, Ch31b, Ch34, Ch43]. However, by the mid-20th century,
much of the 19th century work appears to have been forgotten. Segre [Se45], building
on Hilbert, provided the ﬁrst rigorous proof that RD(n) ≤ n − 5 for n ≥ 9, and proved
that for n ≥ 157, RD(n) ≤ n − 6 (n.b. Hamilton proved this for n ≥ 47, while Sylvester
proved it for n ≥ 44). G. Chebotarev (N.’s son) worked to extend Wiman’s methods to
show RD(n) ≤ n − 6 for n ≥ 21 [Ch54], but his proof is incomplete.11 Segre (loc. cit.)
conjectured that in the limit lim
n // ∞ n − RD(n) = ∞.

9Writing S(r) for Sylvester’s sharpening, the initial values are S(4) = 5, S(5) = 10, S(6) = 44, S(7) = 905.
10As Wiman proved, this program cannot produce a solution in RD(n) variables for the general degree n
polynomial once n is at least 8.
11As remarked above, Chebotarev’s argument has the same gap that Dixmier [Di93] observed in Hilbert
and Wiman, namely certain non-generic forms are assumed to be generic.

41

(i.e. precisely what Hamilton had showed over a century earlier). Brauer [Br45] and Segre
each reproved this statement, but without giving eﬀective bounds `a la Hamilton (see also
[Se51]).
In 1957, Arnold (then 19 years old) published a theorem which he described as a “com-
plete solution of the 13th problem of Hilbert” [Ar57]. A strengthening of Arnold’s the-
orem, published soon after by Kolmogorov [Ko57], states that for any continuous map
f : [0, 1]n // R, there exist continuous functions gj, ϕij : [0, 1] // R such that

f (t1, . . . , tn) =
 2n−1∑

j=1 gj(
 k∑

i=1 ϕij(ti))

To apply this to Hilbert’s problem, one must interpret Hilbert as having asked for an
obstruction to expressing a single-valued branch of the general degree 7 polynomial as a
composition of (single-valued) continuous functions of two or fewer variables. Following
Arnold and Kolmogorov, work on the problem in all of its forms largely collapsed, this
despite Arnold’s eﬀorts over a four decade span [Ar70a, Ar70b, Ar70c, AS76, Ar99] to call
attention to and solve Hilbert’s (still open!) thirteenth problem.12

In 1971, Khovanskii [Kh70] showed that if one prohibited the use of division in a formula
(i.e. one only allowed “entire” algebraic functions), then the quintic was not solvable in
1-variable functions.13 Khovanskii emphasized that, more than anything else, this result
shows the importance of division.14

In 1975, Brauer [Br75] gave the ﬁrst rigorous deﬁnition of resolvent degree in the lit-
erature (followed soon after by Arnold and Shimura [AS76]). Brauer then proved that for
n ≥ (r − 1)! + 1, RD(n) ≤ n − r. This improves Sylvester and Hamilton’s bounds for r ≥ 7,
and for such r provides the best upper bound, of which we are aware, prior to this paper.
While not stricly on RD(n), McMullen’s work on iterative algorithms [Mc88] and his
iterative solution of the quintic with Doyle [DM89] represent one of the major outgrowths
of Arnold’s eﬀorts to obstruct solutions of polynomials. More recently, Buhler-Reichstein’s
formalization of the Kronecker-Klein resolvent problem [BR97, BR99], and the broader
theory of essential dimension that this given rise to, provides the closest contemporary
body of work (see e.g. [Re10], [Me17], [FKW19a]).
The interested reader can ﬁnd other discussions of the history of the problem in Sylvester
and Hammond [SH1887], in Klein [Kl26], or more recently in the surveys by Dixmier [Di93]
and Vitushkin [Vi04]. For a contemporary treatment of resolvent degree and its relation to
classical problems see also [FW19, FKW19b].

References

[Ab95] S. Abhyankar, Hilbert’s thirteenth problem, Alev, J. (ed.) et al., Alg`ebre non commu-
tative, groupes quantiques et invariants. Septi`eme contact Franco-Belge, Reims, France,
June 26–30, 1995. Soci´et´e Math´ematique de France. S´emin. Congr. 2 (1995), pp. 1–11.

12See also [Ar00, Problems 1972-27, 1976-34, 1979-10, 1980-10, 1985-18]
13A late paper of Abhyankar [Ab95], apparently unaware of Khovanskii’s result, proves the analogous
theorem for the sextic.
14Lin has also extensively investigated what one can say for the general degree n polynomial if one rules
out division and possibly imposes further restrictions, see the papers [Li73, Li76, Li96].

42

[Ar57] V. Arnold, On continuous functions of three variables, Dokl. Akad. Nauk SSSR vol. 114
(1957), pp. 679–681.

[Ar70a] V. Arnold, On some topological invariants of algebraic functions, Trans. Moscow Math.
Soc. vol. 21 (1970), pp. 30–52.

[Ar70b] V. Arnold, Cohomology classes of algebraic functions invariant under Tschirnhausen
transformations, Funct. Anal. Appl. vol. 4 (1970), pp. 74–75.

[Ar70c] V. Arnold, Topological invariants of algebraic functions, II, Funct. Anal. Appl. vol. 4
(1970), pp. 91–98.

[Ar99] V. Arnold, From Hilbert’s superposition problem to dynamical systems. The Arnoldfest.
Proceedings of a conference in honour of V. I. Arnold for his 60th birthday, Toronto,
Canada, June 15-21, 1997, AMS, Fields Inst. Commun. vol. 24 (1999), pp. 1–18.

[Ar00] V. Arnold, Arnold’s Problems, Springer, 2000.

[AS76] V. Arnold and G. Shimura, Superpositions of algebraic functions, Proc. Symposia in Pure
Math. vol. 28 (1976), AMS, Providence, pp. 45–46.

[Be12] A. Beauville, Non-rationality of the symmetric sextic Fano threefold, Geometry and arith-
metic, 57–60, EMS Series of Congress Reports, Eur. Math. Soc., Z¨urich, 2012.

[Br45] R. Brauer, A note on systems of homogeneous algebraic equations, Bull. AMS, vol. 51
(1945), 749–755.

[Br75] R. Brauer, On the resolvent problem, Ann. Mat. Pura Appl. (4) 102 (1975), pp. 45–55.

[Br1786] E. Bring, Meletemata quædam Mathematica circa Transformationem Æquationum Al-
gebraicarum (“Some Selected Mathematics on the Transformation of Algebraic Equa-
tions”), Lund, 1786.

[BR97] J. Buhler and Z. Reichstein, On the essential dimension of a ﬁnite group, Compositio
Math. vol. 106 (1997), pp. 159–179.

[BR99] J. Buhler and Z. Reichstein, On Tschirnhaus transformations, Topics in number theory
(University Park, PA, 1997), 127–142, Math. Appl., 467, Kluwer Acad. Publ., Dordrecht.

[Ch31a] N. Chebotarev, ¨Uber ein algebraisches Problem von Herrn Hilbert. I, Math. Ann. vol.
104 (1931), pp. 459–471.

[Ch31b] N. Chebotarev, ¨Uber ein algebraisches Problem von Herrn Hilbert. II, Math. Ann. vol.
105 (1931), pp. 240–255.

[Ch32] N. Chebotarev, Die Probleme der modernen Galoisschen Theorie, Proceedings of the
International Congress of Mathematicians, 1932.

[Ch34] N. Chebotarev, ¨Uber das Klein-Hilbertsche Resolventenproblem, Bull. Soc. Phys.-Math.
Kazan, III. Ser. 6 (1934), pp. 5–22.

[Ch43] N. Chebotarev, The problem of resolvents and critical manifolds, Izvestia Akad. Nauk
SSSR vol. (1943), pp. 123—146.

[Ch54] G. Chebotarev, On the problem of resolvents, Uchenye Zapiski Kazanskogo Universiteta
vol. 114 (1954) Book 2, pp. 189–193.
43

[Di93] J. Dixmier, Histoire de 13e probl`eme de Hilbert, Cahiers du s´eminaire d’histoire des
math´ematiques, 2e s´erie, tome 3 (1993), pp. 85–94.

[DM89] P. Doyle and C. McMullen, Solving the quintic by iteration, Acta Math. vol. 163 (1989),
pp. 151–180.

[En1897] F. Enriques, Sur les probl`emes qui se rapportent `a la r´esolution des ´equations alg´ebriques
renfermant plusieurs inconnues, Proceedings of the International Congress of Mathemati-
cians, 1897.

[FKW19a] B. Farb, M. Kisin and J. Wolfson, Essential dimension of congruence covers,
arXiv:1901.09013.

[FKW19b] B. Farb, M. Kisin and J. Wolfson, Modular functions and resolvent problems (with an
appendix by N. Harman), arXiv:1912.12536.

[FW19] B. Farb and J. Wolfson, Resolvent degree, Hilbert’s 13th problem and Geometry,
L’Enseignement Math´ematique vol. 65 (2019), no. 3–4, pp. 303–376.

[Fo36] T. Fort, Formulas for Reducing a Quadratic Form to a Sum of Squares, American Math-
ematical Monthly, vol. 43 (1936), no. 8, pp. 477–481.

[Fr26] R. Fricke, Lehrbuch der Algebra, vol. 2, Viewig und Sohn, Braunschweig, 1926.

[Ha1836] W. Hamilton, Inquiry into the validity of a method recently proposed by George B.
Jerrard, esq., for transforming and resolving equations of elevated degrees, Report of the
Sixth Meeting of the British Association for the Advancement of Science (1836), Bristol,
295-–348.

[Ha77] R. Hartshorne, Algebraic Geometry, GTM 52, Springer-Verlag, New York, NY, 1977,
xvi+496 pp.

[Hi1900] D. Hilbert, Mathematical Problems, from Proceedings of the 1900 ICM, English transla-
tion reprinted in Bull. AMS, Vol. 37, No. 4 (2000), pp. 407–436.

[Hi27] D. Hilbert, ¨Uber die Gleichung neunten Grades, Math. Ann. vol. 97 (1927), no. 1, 243–
250. English translation: On the equation of ninth degree, translation by S. Hensel, 2017,
available at https://www.mathematik.uni-muenchen.de/ hensel/papers/hilbert2.pdf.

[HL87] M. Hochster and D. Laksov, The linear syzygies of generic forms, Comm. Algebra vol. 15
(1987), no. 1-2, pp. 227–239.

[Kh70] A. Khovanskii, The representability of algebroidal functions by superpositions of analytic
functions and algebroidal functions of one variable, Funct. Anal. Appl. vol. 4 (1970), pp.
152–156; translation from Funkts. Anal. Prilozh. vol. 4 (1970), No. 2, pp. 74–79.

[Kl74] S. Kleiman, The transversality of a general translate, Compositio Math. vol. 28 (1974),
no. 3, pp. 287–297.

[Kl1871] F. Klein, Ueber eine geometrische Repr¨asentation der Resolventen algebraischer Gle-
ichungen, Math. Ann. vol. 4, 1871, pp. 346-358.

[Kl1879] F. Klein, Ueber die Auﬂ¨osung gewisser Gleichungen vom siebenten und achten Grade,
Math. Ann. vol. 15, 1879, pp. 252–282.

44

[Kl1884] F. Klein, Vorlesungen ¨uber das Ikosaeder und die Auﬂ¨osung der Gleichungen vom f¨unften
Grade, Teubner, Leipzig, 1884. English translation: Lectures on the icosahedron and
solution of equations of the ﬁfth degree, translated by G. G. Morrice, 2nd and rev.
edition, New York, Dover Publications, 1956.

[Kl1887] F. Klein, Zur Theorie der allgemeinen Gleichungen sechsten und siebenten Grades, Math.
Ann. vol. 28 (1887), pp. 499–532.

[Kl1888] F. Klein, Sur la resolution, par les fonctions hyperelliptiques de l’equation du vingt-
septieme degre, de laquelle depend la determination des vingt-sept droites d’une surface
cubique, Journal de Math´ematiques pures et appliqu´ees (4) vol. 4 (1888), pp. 169–176.

[Kl1894] F. Klein, Lectures on Mathematics, MacMillan and Co., 1894.

[Kl1905] F. Klein, ¨Uber die Auﬂ¨osung der allgemeinen Gleichungen f¨unften und sechsten Grades,
Journal f¨ur die reine und angewandte Mathematik vol. 129 (1905), pp.150–174. English
translation: About the solution of the general equations of ﬁfth and sixth degree, trans-
lation by A. Sutherland, 2019, arXiv:1911.02358.

[Kl1908] F. Klein, Elementarmathematik vom h¨oheren Standpunkte ans. Teil I: Arithmetik, Al-
gebra, Analysis. Teubner. (1908). English translation: Elementary Mathematics from
a Higher Standpoint, vol. 1: Arithmetic, Algebra, Analysis, translated from the 3rd
German ed. by E. R. Hedrick and C. A. Noble, New York, Dover Publications (1953).

[Kl22] F. Klein, Gesammelte Mathematische Abhandlungen, vol. 2, pp. 255–504, 1922.

[Kl26] F. Klein, History of the development of mathematics in the 19th century, Springer, 1926.

[Ko57] A. Kolmogorov, On the representation of continuous functions of many variables by
superposition of continuous functions of one variable and addition, Dokl. Akad. Nauk
SSSR vol. 114 (1957), no. 5, pp. 953–956.

[Li73] V. Lin, On superpositions of algebraic functions, Funct. Anal. Appl. vol. 6 (1973), pp.
240–241; translation from Funkts. Anal. Prilozh. vol. 6 (1972), No. 3, pp. 77–78.

[Li76] V. Lin, Superpositions of algebraic functions. Funct. Anal. Appl. vol. 10 (1976), pp.
32–38; translation from Funkts. Anal. Prilozh. vol. 10 (1976), No. 1, pp. 37–45.

[Li96] V. Lin, Around the 13th Hilbert problem for algebraic functions. Teicher, Mina (ed.),
Proceedings of the Hirzebruch 65 conference on algebraic geometry, Bar-Ilan University,
Ramat Gan, Israel, May 2-7, 1993. Bar-Ilan University, Isr. Math. Conf. Proc. 9 (1996),
pp. 307–327.

[Mc88] C. McMullen, Braiding of the attractor and the failure of iterative algorithms, Invent.
Math. vol. 91 (1988), pp. 259–272.

[Me17] A. Merkurjev, Essential dimension, Bull. AMS vol 54 (2017), no. 4, pp. 635–661.

[MS83] A. Merkurjev and A. Suslin, K-Cohomology of Severi-Brauer Varieties and the Norm
Residue Homomorphism, Math. USSR Izv. vol. 21 (1983), no. 2, pp. 307–340.

[Re10] Z. Reichstein, Essential dimension, Proceedings of the International Congress of Mathe-
maticians, Hyderabad, India, 2010.

[Ro55] H. Robbins, A Remark on Stirling’s Formula, The American Mathematical Monthly, vol.
62 (1955) no. 1: pp. 26-29.
 45

[Se45] B. Segre, The Algebraic Equations of Degrees 5, 9, 157, ..., and the Arithmetic Upon an
Algebraic Variety, Ann. of Math. (2), vol. 46 (1945), pp. 287–301.

[Se51] B. Segre, Arithmetical Questions on Algebraic Varieties, University of London, Athlone
Press, London, 1951.

[St17] J. Starr, Veronese varieties contained in hypersurfaces, arXiv:1703.03294.

[Sy1887] J. Sylvester, On the so-called Tschirnhausen transformation, J. Reine Angew. Math. vol.
100 (1887), pp. 465–486.

[SH1887] J. Sylvester and J. Hammond, On Hamilton’s Numbers, Phil. Trans. R. Soc. London A
vol. 178 (1887), pp. 285–312.

[SH1888] J. Sylvester and J. Hammond, On Hamilton’s Numbers II, Phil. Trans. R. Soc. London
A vol. 179 (1888), pp. 65–71.

[Ts1683] E. von Tschirnhaus, Methodus auferendi omnes terminos intermedios ex data aeqvatione
(Method of eliminating all intermediate terms from a given equation), Acta Eruditorum
(1683), pp. 204–207.

[Vi04] A. Vitushkin, On Hilbert’s thirteenth problem and related questions, Russian Math.
Surveys vol. 59 (2004) no. 1, pp. 11–25.

[Wa08] A. Waldron, Fano Varieties of Low-Degree Smooth Hypersurfaces and Unirationality,
Bachelor thesis, Harvard University, Cambridge, Massachusetts, 2008.

[Wi27] A. Wiman, ¨Uber die Anwendung der Tschirnhausen-Transformation auf die Reduktion
algebraischer Gleichungen, Nova acta regiae societatis scientiarum Uppsaliensis, vol. 16
(1927), pp. 3–8.

Dept. of Mathematics, University of California, Irvine
E-mail: wolfson@uci.edu
 46
