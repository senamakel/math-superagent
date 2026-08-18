<!-- source: https://arxiv.org/pdf/2204.13202 | converted from PDF -->

arXiv:2204.13202v1  [math.GR]  27 Apr 2022
HILBERT’S 13TH PROBLEM FOR ALGEBRAIC GROUPS

ZINOVY REICHSTEIN

Abstract. The algebraic form of Hilbert’s 13th Problem asks for the resolvent degree
rd(n) of the general polynomial f (x) = x
n+a1x
n−1+. . .+an of degree n, where a1, . . . , an
are independent variables. The resolvent degree is the minimal integer d such that every
root of f (x) can be obtained in a ﬁnite number of steps, starting with C(a1, . . . , an)
and adjoining algebraic functions in ⩽ d variables at each step. Recently Farb and
Wolfson deﬁned the resolvent degree rdk(G) of any ﬁnite group G and any base ﬁeld k
of characteristic 0. In this setting rd(n) = rdC(Sn), where Sn denotes the symmetric
group. In this paper we deﬁne rdk(G) for every algebraic group G over an arbitrary ﬁeld
k, investigate the dependency of this quantity on k and show that rdk(G) ⩽ 5 for any
ﬁeld k and any connected group G. The question of whether rdk(G) can be bigger than
1 for any ﬁeld k and any algebraic group G over k (not necessarily connected) remains
open.
 1. Introduction

The algebraic forms of Hilbert’s 13th Problem asks for the resolvent degree rd(n), which
is the smallest integer d such that a root of the general polynomial

f (x) = x
n + a1x
n−1 + . . . + an

can be expressed as a composition of algebraic functions of d variables with complex
coeﬃcients. It is known that rd(n) = 1 when n ⩽ 5, and that 1 ⩽ rd(n) ⩽ n − α(n).
where α(n) is an unbounded but very slow growing function of n. Classical upper bounds
of this form have been recently sharpened by Wolfson [45], Sutherland [39] and Heberle-
Sutherland [22]. On the other hand, it is not known whether or not rd(n) > 1 for any
n ⩾ 6. For a brief informal introduction to Hilbert’s 13th Problem, see [28, Section 1].
For a more detailed discussion, see [14, 16].
Farb and Wolfson [16] deﬁned the resolvent degree rdk(G) for every ﬁnite group G over
an arbitrary base ﬁeld k of characteristic 0. In this setting rd(n) = rdC(Sn), and it is not
known whether or not rdk(G) can ever be > 1.
In this paper we extend their deﬁnition of rdk(G) to an arbitrary algebraic group G
(not necesarily ﬁnite, aﬃne or smooth) deﬁned over an arbitrary ﬁeld k. Our deﬁnition
proceeds in three steps. First we deﬁne the level of a ﬁnite ﬁeld extension (Deﬁnition 4.1),
then the resolvent degree of a functor (Deﬁnition 7.3), then the resolvent degree of a
algebraic group (Deﬁnition 10.1). Out ﬁrst main result is the following.

2020 Mathematics Subject Classiﬁcation. 20G10, 20G15.
Key words and phrases. Resolvent degree, Hilbert’s 13th Problem, algebraic group, torsor.
Zinovy Reichstein was partially supported by National Sciences and Engineering Research Council of
Canada Discovery grant 253424-2017. 1

2 ZINOVY REICHSTEIN

Theorem 1.1. Let G be a connected algebraic group over a ﬁeld k. Then
(a) rdk(G) ⩽ 5.
(b) Moreover, if G has no simple components of type E8, then rdk(G) ⩽ 1.

Note that Theorem 1.1 was announced (in a weaker form and without proof) in Section
8 of my survey [28]. We will also investigate the dependence of rdk(G) on the base ﬁeld
k. Our main results in this direction are Theorems 1.2 and 1.3 below.

Theorem 1.2. Let G be an algebraic group deﬁned over k. Then rdk(G) = rdk′(Gk′) for
any ﬁeld extension k′/k.

The case where k′ is algebraic over k is fairly straightforward (see Proposition 8.3(b));
the main point here is that the extension k′/k can be arbitrary. In particular, if G is
deﬁned over Z, when Theorem 1.2 tells us that rdk′(Gk′) = rdk(Gk) for any two ﬁelds k
and k′ of the same characteristic. In arbitrary characteristic, we prove the following.

Theorem 1.3. Let G be a smooth aﬃne group scheme over Z. Denote the connected
component of G by G0. Assume that G0 is split reductive and G/G0 is ﬁnite over Z. Let
k be a ﬁeld of characteristic 0. Then rdk(Gk) ⩾ rdk(Gk0) for any other ﬁeld k0.

We will deduce Theorem 1.3 from a more general result, Proposition 13.1, which com-
pares the resolvent degrees of the general and the special ﬁbers of a group scheme over a
discrete valuation ring. Note that both Theorems 1.2 and 1.3 apply in the classical case,
where G is an abstract ﬁnite group viewed as a group scheme over Z, in particular to
G = Sn.
A key role in our proof of Theorem 1.1(b) will be played by a theorem of Tits, which
asserts that if G is a simple group over k of any type other than E8 and T → Spec(K) is
a G-torsor, then T can be “split by radicals”, i.e., T splits over some radical extension of
K; see Section 16. Tits asked whether or not the same is true for simple groups of type
E8. Using the arguments in Section 16, one readily sees that a positive answer to this
question would imply the following.

Conjecture 1.4. rdk(G) ⩽ 1 for any connected algebraic group G over any ﬁeld k.

Theorem 1.1(a) (or more precisely, Proposition 16.1(a)), may thus be viewed as a partial
answer to Tits’ question. Note that it is not known whether or not rdk(G) can be > 1 for
any ﬁeld k and any algebraic group G deﬁned over k (not necessarily connected).
The remainder of this paper is structured as follows. Sections 2 and 3 are devoted to
preliminary material on essential dimension of ﬁnite-dimensional algebras and ﬁeld exten-
sions. In Section 4 deﬁnes the level of a ﬁnite ﬁeld extension and explores its elementary
properties. Section 5 studies how the level changes under specialization. Section 6 in-
troduces the level d closure of a ﬁeld. The resolvent degree of a functor is introduced
in Section 7. This notion parallels the notion of essential dimension of a functor, due to
Merkurjev, Berhuy and Favi [1] but the type of functor we allow is more restrictive. Much
of the work towards proving Theorems 1.1 - 1.3 is, in fact, done in the general setting
of functors in Sections 8 and 9. Section 10 introduces the notion of resolvent degree of
an algebraic group. In Section 11 we study the resolvent degree of inﬁnitesimal groups
and abelian varieties. The proof of Theorem 1.2 is completed in Section 12, the proof of

HILBERT’S 13TH PROBLEM FOR ALGEBRAIC GROUPS 3

Theorem 1.3 in Section 13, and the proof of Theorem 1.1 in Sections 14 - 16. In the last
section we show that Conjecture 1.4 follows from a positive answer to a long-standing
open question of Serre (Question 17.1).
The main focus of this paper is on the aspects of the subject which have not been pre-
viously investigated: resolvent degree of connected groups and dependence of resolvent
degree on the base ﬁeld. However, many of the preliminary results overlap with exist-
ing literature and some have classical roots. In particular, Section 4 overlaps with [16,
Section 2], Section 10 with [16, Section 3]. Section 6 elaborates on the short note of
Arnold and Shimura [6, pp, 45-46]; there is also some overlap between Section 14 and [45,
Section 4]. I have tried to indicate these connections throughout the paper. I have also
included independent characteristic-free proofs for most background results, with the goal
of making the exposition largely self-contained. The arguments in this paper are mostly
algebraic and valuation-theoretic, with only a few exceptions (e.g., in Section 14). I have
not included references to classical literature; an interested reader can ﬁnd them in [16].

2. Preliminaries on finite-dimensional algebras

Let K be a ﬁeld and A be ﬁnite-dimensional K-algebra. We will say that A descends
to a subﬁeld K0 of K if there exists a K0-algebra A0 such that A ≃K A0 ⊗K0 K. Here ≃K
stands for isomorphism of algebras over K. We will sometimes say that A/K descends to
A0/K0.

Lemma 2.1. Let k ⊂ K be a ﬁeld extension, A a ﬁnite-dimensional K-algebra, and S a
ﬁnite subset of A. Then A/K descends to A0/K0 such that K0 is ﬁnitely generated over
k, A0 is a K0-subalgebra of A, and S ⊂ A0.

Proof. Choose a K-vector space basis b1, . . . , bn in A. Write bi · bj =
 n∑

h=1 ch
ijbh for every i,

j = 1, . . . , n and s =
 n∑

h=1 αh
s bh for every s ∈ S. Let

K0 = k(ch
ij, αh
s | i, j, h = 1, . . . , n and s ∈ S)

and L0 be the K0-subsalgebra of A generated by b1, . . . , bn. Then one readily sees that
K0 is ﬁnitely generated over k, the natural map A0 ⊗K0 K → A is an isomorphism over
K, and S ⊂ A0. □

Deﬁnition 2.2. Let K be a ﬁeld containing k and A be a ﬁnite-dimensional K-algebra.
The essential dimension edk(A/K) is the minimal value of trdegk(K0), where the minimum
is taken over all intermediate ﬁelds k ⊂ K0 ⊂ K such that L/K descends to K0.

Lemma 2.3. Let K be a ﬁeld containing k and A a ﬁnite-dimensional K-algebra. Then
edk(A) < ∞. Moreover, A/K descends to some A0/K0 such that K0 is ﬁnitely generated
over k and edk(A) = edk(A0) = trdegk(K0).

Proof. Descend A/K to A1/K1 so that d = trdegk(K1) is the smallest possible, i.e.,
d = edk(A). Note that a priori d is a non-negative integer or ∞. By Lemma 2.1, A1/K1
further descends to A0/K0, where k ⊂ K0 ⊂ K1 and K0 is ﬁnitely generated over k. By

4 ZINOVY REICHSTEIN

the minimality of d, edk(A) = edk(A1) = edk(A0) = trdegk(K0) = d. Moreover, since K0
is ﬁnitely generated over k, d < ∞. □

Lemma 2.4. Let k ⊂ k′ ⊂ K be ﬁelds and A be a ﬁnite-dimensional K-algebra. Then
(a) edk′(A) ⩽ edk(A).
(b) If k′ is algebraic over k, then edk′(A) = edk(A).
(c) There exists an intermediate ﬁeld k ⊂ l0 ⊂ k′ such that l0 is ﬁnitely generated over
k and edl(A) = edk′(A) for any l0 ⊂ l ⊂ k′.

Proof. (a) Suppose A descends to a subﬁeld K0 ⊂ K containing k such that trdegk(K0)
as small as possible, i.e., trdegk(K0) = edk(A). Then A also descends to k′K0, where the
compositum is taken in K. Now edk′(A) ⩽ trdegk′(k′K0) ⩽ trdegk(K0) = edk(A).
(b) In view of part (a), it suﬃces to show that edk(A) ⩽ edk′(A). Indeed, A descends to
some intermediate ﬁeld k′ ⊂ K ′
0 ⊂ K such that trdegk′(K ′
0) = edk′(A). If k′ is algebraic
over k, then edk(A) ⩽ trdegk(K ′
0) = trdegk′(K0) = edk′(A).
(c) By Lemma 2.3, A/K descends to some A0/K0 such that k′ ⊂ K0 ⊂ K, edk′(A) =
edk′(A0) = trdegk′(K0) and K0 is is generated by ﬁnitely many elements over k′, say
K0 = k′(a1, . . . , am).
Let x1, . . . , xm be independent variables over k′. For each subset I = {i1, . . . , ir} ⊂
{1, 2, . . . , m}, such that the elements ai1, . . . , air are algebraically dependent over k′,
choose a polynomial 0 ̸= pI(xi1, . . . , xir ) ∈ k′[xi1, . . . , xir ] such that pI(ai1, . . . , air ) = 0.
Now choose an intermediate ﬁeld k ⊂ l0 ⊂ k′ such that l0 is generated by the coeﬃcients
of the polynomials pI for every such I. With this choice of l0, any subset of {a1, . . . , am}
which is algebraically dependent over k′ remains algebraically dependent in l0. In other
words, trdegl0(K0) = trdegk′(K0) and thus

(1) edl0(A) ⩽ trdegl0(K0) = trdegk′(L0) = edk′(A).

By part (a), edl0(A) ⩾ edl(A) ⩾ edk′(A) for any intermediate ﬁeld l0 ⊂ l ⊂ k′. Now (1)
tells us that both of these inequalities are, in fact, equalities, as desired. □

3. Preliminaries on field extensions

We will be particularly interested in the case where the ﬁnite-dimensional K-algebra
A is itself a ﬁeld. In this case we will usually use the letter L in place of A and write
edk(L/K) in place of edk(A).

Lemma 3.1. Let k ⊂ K ⊂ L be ﬁeld extensions such that [L : K] < ∞.
(a) If K sep is the separable closure of K in L, then edk(K sep/K) ⩽ edk(L/K) and
edk(L/K sep) ⩽ edk(L/K).
(b) If L is separable over K, and L
norm is the normal closure of L, then edk(L/K) =
edk(L
norm/K).
(c) Suppose K ⊂ E ⊂ L is an intermediate extension. If E is separable over K, then
edk(E/K) ⩽ edk(L/K).

Proof. (a) Suppose L/K descends to L0/K0. Denote the separable closure of K0 in L0 by
(K0)sep. Then K sep/K descends to K sep
0 /K0, L/K sep descends to L0/(K0)sep and part (a)
follows.
 HILBERT’S 13TH PROBLEM FOR ALGEBRAIC GROUPS 5

(b) is proved in [7, Lemma 2.3].
(c) In view of part (a), it suﬃces to show that edk(E/K) ⩽ edk(K sep/K). In other
words, we may replace L by K sep and thus assume without loss of generality that L
is separable over K. By (b), we may further replace L by its normal closure over K
and thus assume that L is Galois over K. Then E = L
H , where H is a subgroup of
G = Gal(L/K). By [7, Lemma 2.2], L/K descends to some L0/K0, where k ⊂ K0 ⊂ K,
trdegk(K0) = edk(L/K), and L0 is a G-invariant subﬁeld of L. Then E/K descends to
L
H
0 /K0. This tells us that edk(E/K) ⩽ trdegk(K0) = edk(L/K), as desired. □

We will say that a ﬁeld extension L/K is simple if [L : K] < ∞ and L is generated
by one element over K. In other words, L ≃ K[x]/(f (x)), where f (x) ∈ K[x] is an
irreducible polynomial over K. By the Primitive Element Theorem, every ﬁnite separable
extension is simple.

Lemma 3.2. Suppose a ﬁnite ﬁeld extension L/K descends to L0/K0. Then L/K is
simple if and only if L0/K0 is simple.

Proof. One direction is obvious: if L0 = K0(a) is simple, then L = K(a) is also simple.
To prove the converse, assume that L/K is simple and set n = [L : K] = [L0 : K0]. If
K0 is a ﬁnite ﬁeld, then so is L0. In this case L0/K0 is separable and hence, simple. Thus
we may assume that K0 is inﬁnite. It suﬃces to show that L0 contains an element of
degree n over K0. View L0 as the set of K0-points of the n-dimensional aﬃne space An,
and L as the set of K-points of An. Let X ⊂ An be the subscheme of An determined by
the condition that for x ∈ An
K0, 1, x, . . . , x
n−1 are linearly dependent. Here multiplication
in An
K0 comes from identifying An(K0) with L0. It is easy to see that X is a closed
subscheme of An (given by the vanishing of a single n × n determinant) deﬁned over K0.
Then X(K0) is the set of elements of L0 of degree ⩽ n − 1 over K0 and X(K) is the set
of elements of L of degree ⩽ n − 1 over K. We know that L/K is simple; hence, X ⊊ An.
That is, U = An \ X is a non-empty Zariski open subscheme of An deﬁned over K0. Since
K0 is an inﬁnite ﬁeld, we conclude that U(K0) ̸= ∅. In other words, L0/K0 is simple, as
claimed. □

Lemma 3.3. Let k ⊂ K ⊂ L be ﬁelds such that L/K is simple. Assume K ′/K is another
ﬁeld extension (not necessarily ﬁnite), and L
′ = K ′L be a compositum of K ′ and L over
K. Then edk(L
′/K ′) ⩽ edk(L/K).

Note that Lemma 3.3 is immediate from the deﬁnition of edk(L/L) in the case, where
L
′ ≃ L ⊗K K ′ or equivalently, [L
′ : K ′] = [L : K]. The only (slight) complication arises
from the fact that [L
′ : K ′] may be smaller than [L : K].

Proof. Set n = [L : K] and d = edk(L/K). Then L/K descends to some intermediate
ﬁeld k ⊂ K0 ⊂ K such that trdegk(K0) = d. That is, there exists a ﬁeld extension L0/K0
such that L ≃K L0 ⊗K0 K, where ≃K0 denotes an isomorphism of ﬁelds over K0.
By Lemma 3.2, L0/K0 is simple. That is, L0 ≃K0 K0[x]/(f (x)), where f (x) ∈ K0[x]
is a polynomial of degree n, irreducible over K0. Then L ≃K K[x]/(f (x)). Now let
f (x) = f1(x) . . . fr(x) be an irreducible decomposition of f (x) over K ′. A compositum L
′

of L and K ′ is isomorphic to K ′[x]/(fi(x)) for some i, say, L
′ ≃K ′ K ′[x]/(f1(x)). Denote
the degree of f1(x) by n1 = [L
′ : K ′] and the roots of f1 in the algebraic closure of K by

6 ZINOVY REICHSTEIN

α1, . . . , αn1. Since each αi is a root of f (x) ∈ K0[x], each αi algebraic over K0. Hence,
the coeﬃcients of f1(x), being elementary symmetric polynomials in α1, . . . , αn1, are also
algebraic over K0. This shows that f1(x) ∈ K alg
0 [x], where K alg
0 is the algebraic closure of
K0 in K. In other words, L
′/K ′ descends to K alg
0 . Consequently,

edk(L
′/K ′) ⩽ trdegk(K alg
0 ) = trdegk(K0) = d = edk(L/K),

as desired. □

Lemma 3.4. Let k ⊂ K ⊂ L be ﬁelds such that [L : K] < ∞. Then there exist
intermediate extensions K = K (0) ⊂ K (1) ⊂ . . . ⊂ K (r) = L such that K (i)/K (i−1) is
simple and edk(K (i)/K (i−1)) ⩽ edk(L/K) for every i = 1, . . . , r.

Proof. Set d = edk(L/K). By deﬁnition, L/K descends to L0/K0, where k ⊂ K0 ⊂ K and
trdegk(K0) = d. Let α1, . . . , αr be generators for L0 over K0 and set K (i)
0 = K0(α1, . . . , αi)
and K (i) = K(α1, . . . , αi). We obtain the following diagram, where

K = K (0)   • // K (1)   • // . . .   • // K (r) = L

K0 = K (0)
0   • // K (1)
0   • // . . .   • // K (r)
0 = L0

By our construction, the extension K (i)/K (i−1) is simple for each i = 1, . . . r. Moreover,

edk(K (i)/K i−1) ⩽ trdegk(K (i−1)
0 ) = d

because K (i)/K (i−1) descends to K (i)
0 /K (i−1)
0 for each i. □

4. The level of a finite field extension

We now deﬁne the level of a ﬁeld extension, following Dixmier [14, Section 2].

Deﬁnition 4.1. Let k be a base ﬁeld, K be a ﬁeld containing k, and L/K be a ﬁeld
extension of ﬁnite degree. I will say that L/K is of level ⩽ d if there exists a diagram of
ﬁeld extensions

(2) Km

L
 ⑧⑧⑧⑧⑧⑧⑧⑧ .

K2

K1

K0

✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯ K

HILBERT’S 13TH PROBLEM FOR ALGEBRAIC GROUPS 7

such that [Ki : Ki−1] < ∞ and edk(Ki/Ki−1) ⩽ d for every i = 1, . . . , m. The level of
L/K is the smallest such d; I will denote it by levk(L/K).

Remarks 4.2. (1) The same notion was introduced by Brauer [2] (in characteristic 0)
under the name of resolvent degree. In this paper we will reserve the term “resolvent
degree” for the resolvent degree of an object of a functor; see Deﬁnition 7.3. If L/K is
a ﬁnite separable extension, then we may view L/K as an object of the functor of ´etale
algebras, and the two notions coincide; see Example 7.5.
(2) (cf. [16, Lemma 2.5.3]) If k ⊂ K ⊂ L
′ ⊂ L and [L : K] < ∞, then levk(L
′/K) ⩽
levk(L/K). Indeed, any tower (2) showing that levk(L/K) ⩽ d also shows that levk(L
′/K) ⩽
d. (3) (cf. [16, Lemma 2.5.1]) Taking m = 1 and K1 = L in (2), we see that levk(L/K) ⩽
edk(L/K).
(iv) We may assume without loss of generality that each extension Ki/Ki−1 in the
tower (2) is simple. Indeed, by Lemma 3.4, we may replace Ki/Ki−1 by a sequence of
simple extensions without increasing the essential dimension.
(5) Deﬁnition 4.1 formalizes the classical notion of composition of algebraic functions.
If K is a ﬁeld of rational functions on some algebraic variety X deﬁned over k, then
it is natural to think of K1 as being generated by algebraic (multi-valued) functions on
X in ⩽ edk(K1/K) variables, and Ki as being generated by compositions of i algebraic
functions on X in ⩽ levk(L/K) variables.
(6) No examples where levk(L/K) > 1 are known.

Lemma 4.3. Assume that k ⊂ k′ ⊂ K ⊂ L are ﬁelds and [L : K] < ∞. Then
(a) (cf. [16, Lemma 2.5.2]) levk(L/K) ⩾ levk′(L/K).
(b) Moreover, equality holds if k′ is algebraic over k.
(c) Furthermore, there always exists an intermediate ﬁeld k ⊂ l0 ⊂ k′ such that l0 is
ﬁnitely generated over k and levl(L/K) = levk′(L/K) for every ﬁeld l between l0 and k′.

Proof. Choose a tower K = K0 ⊂ K1 ⊂ . . . ⊂ Km, as in Deﬁnition 4.1 and apply parts
(a), (b) and (c) of Lemma 2.4, respectively, to each intermediate extension Ki/Ki−1. In
part (c), let li/k be a ﬁnitely generated ﬁeld extension obtained by applying Lemma 2.4(c)
to Ki/Ki−1. Now set l0 to be the compositum of l1, . . . , lm in k′ over k. □

Lemma 4.4. Assume that k ⊂ K ⊂ L are ﬁelds and [L : K] < ∞ and let K ⊂ K ′ be
another ﬁeld extension (not necessarily ﬁnite). Then levk(K ′L/K ′) ⩽ levk(L/K). Here
K ′L denotes an arbitrary compositum of K ′ and L over K.

Proof. Set d = levk(L/K) and choose a tower K = K0 ⊂ K1 ⊂ . . . ⊂ Km as in Deﬁni-
tion 4.1. By Remark 4.2(4) we may assume that each intermediate extension Ki/Ki−1 is
simple. Now consider the tower

K ′ = K ′
0 ⊂ K ′
1 ⊂ . . . ⊂ K ′
m,

Here K ′
m = K ′Km is some compositum of K ′ and Km, and for i = 0, . . . , m−1, K ′
i = K ′Ki
is the compositum of K ′ and Ki in K ′
m. Since K ⊂ L ⊂ Km, K ′L embeds into K ′Km over
K. Since Ki/Ki−1 is simple, Lemma 3.3 tells us that edk(K ′
i/K ′
i−1) ⩽ d. We conclude
that levk(K ′L/K ′) ⩽ d. □

8 ZINOVY REICHSTEIN

Lemma 4.5. Assume that k ⊂ K ⊂ L are ﬁelds and [L : K] < ∞. Then levk(L/K) = 0
if and only if L embeds in a compositum kK over k. In particular, if k is algebraically
closed, then levk(L/K) = 0 if and only if L = K.

Proof. The second assertion is an immediate consequence of the ﬁrst.
To prove the ﬁrst assertion, suppose L ⊂ kK. In other words, L/K is generated
by elements α1, . . . , αm ∈ L which are algebraic over k. Consider the tower of simple
extensions k = k0 ⊂ k1 ⊂ . . . ⊂ km,

where ki = k(α1, . . . , αs). Since trdegk(ki) = 0, we have edk(ki/ki−1) = 0 for every
i = 1, . . . , m. Now consider the tower

K = k0K ⊂ k1K ⊂ . . . ⊂ kmK = L.

By Lemma 4.4, edk(kiK/ki−1K) ⩽ edk(ki/ki−1) = 0. Thus levk(L/K) = 0.
Conversely, suppose levk(L/K) = 0. Then there exists a tower (2) of ﬁeld extensions
such that L ⊂ Km (over K) and edk(Ki/Ki−1) = 0 for each i. Consequently, Ki is
generated over Ki−1 by elements that are algebraic over k. This implies that Km embeds
in kK over K, and hence, so does L. □

Recall that a ﬁnite ﬁeld extension L/K is called radical if there exists a tower (2) such
that Ki = Ki−1(λ), where λni ∈ K for some ni ⩾ 1, i = 1, . . . , m.

Lemma 4.6. Let K be a ﬁeld containing k and L/K be a ﬁnite ﬁeld extension. Assume
that L/K is (a) solvable, (b) radical, (c) purely inseparable. Then levk(L/K) ⩽ 1.

Proof. By deﬁnition L/K is solvable if there exists a tower K = K0 ⊂ K1 ⊂ . . . ⊂ Km,
as in (2), such that L embeds into Km over K and Ki is of the form Ki−1(λi) for each
i = 1, . . . , m, where λi is a root of a polynomial of the form
(i) x
ni − ai or (ii) x
ni − x − ai for some positive integer ni and ai ∈ Ki−1,
Note that (i) covers the case, where λi is a root of unity (ai = 1), and (ii) is only needed
when ni = char(k) > 0. In both cases Ki = k(λ)Ki−1 and thus

edk(Ki/Ki−1) ⩽ edk(k(λ)/k(a)) ⩽ 1.

Here the ﬁrst inequality follows from Lemma 3.3. The second inequality is obvious, since
trdegk(k(a)) ⩽ 1. Thus levk(L/K) ⩽ 1. This proves (a).
(b) is proved by the same argument, except that case (ii) does not occur.
(c) follows from (b) because every purely inseparable extension is radical. □

Lemma 4.7. (cf. [16, Lemma 2.7]) Let K be a ﬁeld containing k and L/K and M/L be
ﬁeld extensions of ﬁnite degree. If levk(L/K) ⩽ d and levk(M/L) ⩽ d, then

levk(M/K) ⩽ d.

Proof. Choose a tower K = K0 ⊂ K1 ⊂ . . . ⊂ Km for L/K as in (2), and a similar tower
L = L0 ⊂ L1 ⊂ . . . ⊂ Ln for M/L. That is, L embeds into Km over K, M embeds into Ln
over L, edk(Ki/Ki−1) ⩽ d and edk(Lj/Lj−1) ⩽ d for every i = 1, . . . , m and j = 1, . . . , n.
By Remark 4.2(4) we may assume that all intermediate extensions Ki/Ki−1 and Lj/Lj−1

HILBERT’S 13TH PROBLEM FOR ALGEBRAIC GROUPS 9

are simple. Let K be an algebraic closure of K. Fix embeddings Km ֒→ K and Ln ֒→ K
and consider the tower of simple extensions

K0 ⊂ K1 ⊂ . . . ⊂ Km = KmL0 ⊂ KmL1 ⊂ . . . ⊂ KmLn,

where KmLi is the compositum of Km and Li in K. Clearly, M ⊂ Ln ⊂ KmLn. Thus it
suﬃces to show that
(i) edk(Ki/Ki−1) ⩽ d for every i = 1, . . . , m and
(ii) edk(KmLj/KmLj−1) ⩽ d for every j = 1, . . . , n.
(i) follows from our choice of the tower K0 ⊂ K1 ⊂ . . . ⊂ Km. On the other hand,
by Lemma 3.3, edk(KmLj/KmLj−1) ⩽ edk(Lj/Lj−1), and by our choice of the tower
L0 ⊂ L1 . . . ⊂ Ln, edk(Lj/Lj−1) ⩽ d for every j = 1, . . . , n. This proves (ii). □

Lemma 4.8. (cf. [16, Lemma 2.11]) Let k ⊂ K ⊂ L be ﬁelds. Assume that the ﬁeld
extension L/K is ﬁnite and separable. Denote the normal closure of L over K by L
norm.
Then levk(L/K) = levk(L
norm/K).

Proof. By Remark 4.2(2), levk(L/K) ⩽ levk(L
norm/K). We will thus focus on proving
the opposite inequality.
Set d = lev(L/K). By the Primitive Element Theorem, L
norm ≃K K[x]/f (x) for some
irreducible polynomial f (x) ∈ K[x]. Then f (x) splits into a product of linear factors over
L
norm. Denote its roots in L
norm by α1, . . . , αn. Set Li = K(α1, . . . , αi); in particular,
L0 = K. We claim that levk(Li/Li−1) ⩽ d for each i = 1, . . . , n. If we can prove this
claim, then applying Lemma 4.7 recursively, we obtain the desired inequality

levk(L
norm/K) = levk(Ln/K) ⩽ d = levk(L/K).

It thus remains to prove the claim. Since Li is a composite of Li−1 and K(αi) ≃K L for
each i, Lemma 4.4 tells us that

levk(Li/Li−1) = lev(Li−1K(αi)/Li−1) ⩽ levk(K(αi)/K) = levk(L/K) = d,

as claimed. □

Proposition 4.9. (cf. [16, Lemma 2.12]) Let k ⊂ K ⊂ L be ﬁelds, where [L : K] < ∞.
Assume that levk(L/K) ⩽ d. Then the tower

K = K0 ⊂ . . . ⊂ Km
of ﬁeld extensions in Deﬁnition 4.1 can be chosen to have the following additional prop-
erties.
(a) Each ﬁeld extension Ki/Ki+1 is simple and either separable or purely inseparable.
(b) If Ki/Ki−1 is separable, then it is Galois.
(c) If Ki/Ki−1 is Galois, then Gal(Ki/Ki−1) is a ﬁnite simple group.

Proof. We will start with a tower K = K0 ⊂ K1 ⊂ . . . ⊂ Km of Deﬁnition 4.1. By
Remark 4.2(4), we may assume that each intermediate extension Ki/Ki−1 is simple. We
will now modify this tower in three steps (a), (b) and (c), so that it acquires properties
(a), (b), and (c) from the statement of the proposition, respectively. At each stage m
may increase and the ﬁelds Ki may change, but every Ki/Ki−1 will remain simple, the
largest ﬁeld Km will either get larger or stay the same (and in particular, it will continue

10 ZINOVY REICHSTEIN

to contain L), and the maximal value of edk(Ki/Ki−1) will not increase (so that it will
remains ⩽ d).
(a) Let K sep
i−1 be the separable closure of Ki−1 in Ki. If Ki/Ki−1 is neither separable nor
purely inseparable, i.e., Ki−1 ⊊ K sep
i−1 ⊊ Ki, we insert K sep
i−1 between Ki−1 and Ki. Note
that Ki/K sep
i−1 is simple because Ki/Ki−1 is, and K sep
i−1/Ki−1 is simple by the Primitive
Element Theorem. Now relabel K0, K1, . . . to absorb the newly inserted ﬁelds. By our
construction each Ki/Ki−1 is simple and either separable or purely inseparable. The
maximal value of edk(Ki/Ki−1) does not increase by Lemma 3.1(a).
(b) If K1/K0 is purely inseparable, do nothing. If K1/K0 is separable, replace K1 by
its normal closure K norm
1 and Ki by K norm
1 Ki for each i ⩾ 2. All newly created extensions
K norm
1 /K0 and K norm
1 Ki/K norm
1 Ki−1 (i ⩾ 2), remain simple and either separable or purely
inseparable. Moreover, for every i ⩾ 2, edk(K norm
1 /K0) = edk(K1/K0) by Lemma 3.1(b)
and edk(K norm
1 Ki/K norm
1 Ki−1) ⩽ edk(Ki/Ki−1) by Lemma 3.3.
Now relabel K0, K1, . . . and do the same for the extension K2/K1. That is, if K2/K1
is purely inseparable, then do nothing. If K2/K1 is separable, replace K2 by its normal
closure K norm
2 , and Ki by K norm
2 Ki for every i ⩾ 3. Proceed recursively: do the same thing
for the extension K3/K2, then (after suitably modifying K3, . . . , Km) for the extension
K4/K3, etc. When all of these modiﬁcations are completed, the resulting tower K =
K0 ⊂ K1 ⊂ . . . ⊂ Km will have properties (a) and (b).
(c) If Ki/Ki−1 is purely inseparable, do nothing. If it is Galois and G = Gal(Ki/Ki−1)
is simple, again do nothing. If not - say if G has a proper normal subgroup N - insert
K N
i between Ki−1 and Ki. By Lemma 3.1(c), edk(Ki/K N
i ) and edk(K N
i /Ki−1) are both
⩽ edk(Ki/Ki−1). Thus the maximal value of edk(Ki/Ki−1) does not increase. Proceeding
recursively, we arrive at a tower of ﬁeld extensions satisfying (a), (b) and (c). □

5. Extensions of valued fields

Throughout this section we will assume that
(1) k ⊂ K ⊂ L are ﬁelds and [L : K] < ∞,
(2) K and L are complete relative to a discrete valuation ν : L
∗ → Z.
(3) We will denote the residue ﬁelds of k, K and L by kν, Kν and Lν, respectively.
Note that we do not require k to be complete. Our goal is to compare levk(L/K) to
levkν (Lν/Kν). Our main result is as follows.

Proposition 5.1. In addition to notational convention (1) - (3), assume that the residue
ﬁeld Kν is perfect. Then levkν (Lν/Kν) ⩽ max{levk(L/K), 1}.

Our proof of Proposition 5.1 will rely on the following lemma comparing the essential
dimensions of L/K and Lν/Kν.

Lemma 5.2. In addition to notational conventions (1), (2), (3), assume that L/K is a
Galois extension, H = Gal(L/K) is a non-abelian ﬁnite simple group and Lν is separable
over Kν. Then edkν (Lν/Kν) ⩽ edk(L/K).

Proof of Lemma 5.2. First note that since K is complete, ν is the unique valuation of L
lying over ν| K ∗; see [32, Theorem II.3.1(ii)]. Thus ν remains invariant under the action
of H, and this action descends to Lν.

HILBERT’S 13TH PROBLEM FOR ALGEBRAIC GROUPS 11

Let Kun/K be the largest unramiﬁed subextension of L/K. Then I = Gal(L/Kun)
is the inertia subgroup of H = Gal(L/K), i.e., the kernel of the H-action on Lν. In
particular, I is normal in H, and Lν/Kν is an (H/I)-Galois extension; see [32, Corollary
III.5.1]. Since H is simple, there are only two possibilities: either

(i) I = G and Kun = K, i.e., L/K is totally ramiﬁed, or

(ii) I = 1 and Kun = L, i.e., L/K is unramiﬁed.

Let us consider these possibilities separately. Case (i) is straightforward. Here Lν = Kν,
so that edkν (Lν/Kν) = 0 and hence, edkν (Lν/Kν) ⩽ edk(L/K), as desired.
In case (ii), Lν/Kν is an H-Galois extension. Let d = edk(L/K). By deﬁnition, L/K
descends to L0/K0, where k ⊂ K0 ⊂ K and trdegk(K0) = d. By [7, Lemma 2.2] we
may assume that L0 is invariant under H. Recall that L = L0 ⊗K0 K. Since H acts
faithfully on L and trivially on K, it acts faithfully on L0. The valuation ν restricts to
an H-invariant discrete valuation on L0, and the H-action on L0 descends to an H-action
on the residue ﬁeld (L0)ν. Note however that a priori L0 and K0 may not be complete,
and L0/K0 may be ramiﬁed.
We claim that H acts faithfully of (L0)ν. Let us assume for a moment that this claim has
been established. Then Lν/Kν descends to (L0)ν/(K0)ν, where (K0)ν denotes the residue
ﬁeld of K0. Indeed, the image of the natural map (L0)ν ⊗(K0)ν Kν → Lν is surjective
by the Galois correspondence, and hence, is an isomorphism, because [(L0)ν : (K0)ν] =
|H| = [Lν : Kν]. We thus conclude, that

edkν (Lν/Kν) ⩽ trdegkν (K0)ν ⩽ trdegk(K0) = d,

as desired. Here the second inequality follows from [5, lemma 2.1], which is a special case
of Abhyankar’s Lemma.
It remains to prove the claim. For each d ⩾ 0, let L
⩾d
0 = {a ∈ L
∗ | ν(a) ⩾ d} ∪ {0}. In
particular, L
⩾0
0 is the valuation ring of ν in L0, L
⩾1
0 is the maximal ideal, and L
⩾0
0 /L
⩾1
0 is,
by deﬁnition, the residue ﬁeld (L0)ν. Let Id be the kernel of the H-action on L
⩾0
0 /L
⩾d+1
0 .
Then I0 ⊃ I1 ⊃ I2 ⊃ . . . is a decreasing sequence of normal subgroups of H. Since H
is simple, each Id is either all of H or 1. Our goal is to show that I0 = 1. Assume the
contrary: I0 = H. Consider two cases.

Case 1: char((L0)ν) = 0. In this case I0 = H is a cyclic group; see [32, Corollary IV.2.2]
or [5, Lemma 2.2(a)]. This contradicts our assumption that H is non-abelian.

Case 2: char((L0)ν) = p > 0. In this case I0 = H is of the form P ⋉ C, where P is
a p-group and C is a cyclic group of order prime to p; see [32, Corollary IV.2.4]. Once
again, this contradicts our assumption that H is simple and non-abelian. This completes
the proof of the claim and thus of Lemma 5.2. □

Proof of Proposition 5.1. Let d = levk(L/K). By Deﬁnition 4.1 there exists a tower

K = K0 ⊂ K1 ⊂ . . . ⊂ Km,

of ﬁnite ﬁeld extensions, where L embeds in Km over K and edk(Ki/Ki−1) ⩽ d for each
i = 1, . . . , m. Since K is complete, so are K1, . . . , Km; see [32, Section II.2, Proposition
3]. By Proposition 4.9 we may assume that each Ki+1/Ki is simple and either purely

12 ZINOVY REICHSTEIN

inseparable or Galois with Gal(Ki+1/Ki) a ﬁnite simple group. Passing to residue ﬁelds,
we obtain a tower Kν = (K0)ν ⊂ (K1)ν ⊂ . . . ⊂ (Km)ν
such that Lν embeds into (Km)ν over kν. In view of Lemma 4.7 it now suﬃces to show
that

(3) levkν ((Ki)ν/(Ki−1)ν) ⩽ max{d, 1} for each i = 1, . . . , m.

If Ki/Ki−1 is purely inseparable, then (Ki)ν/(Ki−1)ν is again purely inseparable. By
Lemma 4.6(c), levkν ((Ki)ν/(Ki−1)ν) ⩽ 1, and (3) holds.
If Ki/Ki−1 is Galois, and Gal(Ki/Ki−1) is simple and non-abelian, then

levkν ((Ki)ν/(Ki−1)ν) ⩽ edkν ((Ki)ν/(Ki−1)ν) ⩽ edk(Ki/Ki−1) ⩽ d,

and (3) follows. Here the ﬁrst inequality is given by Remark 4.2(3) and the second by
Lemma 5.2.
It remains to consider the case, where Hi = Gal(Ki/Ki−1) is abelian. Since we are as-
suming that Kν is perfect, (Ki)ν/(Ki−1)ν is a Galois extension, where Gal (
(Ki)ν/(Ki−1)ν)

is a quotient of Gal(Ki/Ki−1); see [32, Section 1.7, Proposition 20]. (Note that the de-
composition group is all of Gal(Ki/Ki−1) here, because Ki is complete.) In particular,
(Ki)ν/(Ki−1)ν is an abelian (and hence, solvable) extension. Consequently, levkν ((Ki)ν/(Ki−1)ν) ⩽
1 by Lemma 4.6. We conclude that the inequality (3) holds in this case as well. □

6. The level d closure of a field

Deﬁnition 6.1. Let K be a ﬁeld containing k and K be an algebraic closure of K and
d ⩾ 1 be an integer. We deﬁne the level d closure K (d) of K in K to be the compositum
of all intermediate extensions K ⊂ L ⊂ K such that [L : K] < ∞ and levk(L/K) ⩽ d.
Clearly K (1) ⊂ K (2) ⊂ K (3) ⊂ . . . . Up to isomorphism (over K) the level d closure K (d)

depends only on K and not on the choice of K. We will say that K is closed at level d if
K = K (d), i.e., if K has no non-trivial extensions of level ⩽ d.

Remark 6.2. If d = 0, then K (0) = kK, where k denotes the algebraic closure of k
and the compositum is taken in K. In particular, K is closed at level 0 if and only if K
contains an algebraic closure of k. This follows directly from Lemma 4.5.

In the case, where k is an algebraically closed ﬁeld and K = k(x1, . . . , xn) is a purely
transcendental extension, Deﬁnition 6.1 appeared in the short note of Arnold and Shimura
in [6], pp. 45-46. In this section we will prove the following properties of level d closure.
It seems likely that Arnold and Shimura had something like this in mind, through I have
not encountered any explicit statements along these lines in the literature.

Proposition 6.3. Let k ⊂ K ⊂ E be ﬁelds and d ⩾ 0 be an integer.
(a) Consider an intermediate ﬁeld K ⊂ L ⊂ K such that [L : K] < ∞. Then
levk(L/K) ⩽ d if and only if L ⊂ K (d).
(b) K (d) ⊂ E(d). Moreover, if E is a ﬁnite extension of K and levk(E/K) ⩽ d, then
equality holds, K (d) = E(d).
(c) E(d) = ⋃ E(d)
f.g., where the union is taken over the intermediate ﬁelds K ⊂ Ef.g. ⊂ E
with Ef.g. ﬁnitely generated over K.

HILBERT’S 13TH PROBLEM FOR ALGEBRAIC GROUPS 13

(d) (K (d))(n) = K (n) for every n ⩾ d. In particular, K (d) is closed at level d.

Our proof of Proposition 6.3 will rely on the following lemma.

Lemma 6.4. Let k ⊂ K ⊂ L be ﬁeld extensions such that [L : K] < ∞. Then L/K de-
scends to some L
′/K ′, where K ′ is ﬁnitely generated over k and levk(L
′/K ′) = levk(L/K).

Proof. Set d = levk(L/K) and choose a tower K = K0 ⊂ K1 ⊂ . . . ⊂ Km of ﬁnite ﬁeld
extensions such that L embeds into Km over K and edk(Ki/Ki−1) ⩽ d, as in Deﬁnition 4.1.
By Remark 4.2(4), we may assume that each intermediate extension Ki/Ki−1 is simple.
By Lemma 2.3, Ki/Ki−1 descends to some Ei/Fi−1, where Ei ⊂ Ki, k ⊂ Fi−1 ⊂ Ki−1,
Fi−1 is ﬁnitely generated over k and trdegk(Fi−1) = edk(Ei/Fi−1) = edk(Ki/Ki−1) ⩽ d.
Let Gi−1 be a ﬁnite set of generators for Fi−1 over k. By Lemma 3.2, Ei/Fi−1 is simple,
say, Ei = Fi−1(αi).
Similarly, by Lemma 2.1, the ﬁeld extension L/K descends to E′/F ′, where the inter-
mediate ﬁeld k ⊂ F ′ ⊂ K is ﬁnitely generated over k. Let H be a ﬁnite set of generators
for F ′ over k and B be a F ′-vector space basis for E′. These notations are summarized
in the diagram below, where ֒→ indicates descent.

Km

E′   • // L
 ④④④④④④④④④ .

Ki Ei? _oo Fi−1(αi)

Ki−1 Fi−1? _oo

.

F ′   • //

✬✬✬✬✬✬✬✬✬✬✬✬✬✬✬✬✬✬✬✬✬✬✬✬✬✬✬✬✬✬✬✬✬ K0

✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭ K

By Lemma 2.1, Km/K descends to some K ′
m/K ′ such that k ⊂ K ′ ⊂ K, K ′ is ﬁnitely
generated over k and K ′
m contains the ﬁnite subset

G0 ∪ . . . ∪ Gm−1 ∪ {α1, . . . , αm} ∪ H ∪ B

of Km. Consider the tower

(4) K ′ = K ′
0 ⊂ K ′
1 ⊂ . . . ⊂ K ′
m,

where K ′
i = K ′
m ∩Ki for each i. Note that K ′
i−1 contains k and Gi−1 and hence, k(Gi−1) =
Fi−1. Moreover, since K ′
i contains K ′
i−1 and αi, it also contains Fi−1(αi) = Ei.

14 ZINOVY REICHSTEIN

Since Km/K descends to K ′
m/K ′, we have

[K ′
m : K ′
m−1] · [K ′
m−1 : K ′
m−2] · . . . · [K ′
1 : K ′
0] = [K ′
m : K ′] =(5)
 [Km : K] = [Km : Km−1] · [Km−1 : Km−2] · . . . · [K1 : K0].

On the other hand, since αi ∈ K ′
i has degree [Ei : Fi−1] = [Ki : Ki−1] over Ki−1, it has
degree ⩾ [Ki : Ki−1] over K ′
i−1. Thus [K ′
i : K ′
i−1] ⩾ [Ki : Ki−1] for each i. In view of (5),
we conclude that [K ′
i : K ′
i−1] = [Ki : Ki−1] for each i. In other words, Ki/Ki−1 descends
to K ′
i/K ′
i−1 which, in turn, descends to Ei/Fi−1. Thus

edk(K ′
i/K ′
i−1) ⩽ edk(Ei/Fi−1) ⩽ trdegk(Fi−1) ⩽ d.

Finally, note that K ′ = K ′
0 contains H and thus K ′ contains k(H) = F ′. Set L
′ = K ′
m ∩L.
Since K ′
m contains B, this tells us that L/K descends to L
′/K ′. By our construction,
L
′ = K ′
m ∩ L embeds into K ′
m over K ′. The tower (4) now shows that levk(L
′/K ′) ⩽ d,
as desired. □

Proof of Proposition 8.1. (a) If levk(L/K) ⩽ d, then L ⊂ K (d) by the deﬁnition of K (d).
Conversely, if L ⊂ K (d) and [L : K] < ∞, then L is contained in a compositum L1L2 . . . Ln
of ﬁnitely many ﬁnite extension Li/K such that levk(Li/K) ⩽ d for each i. Using Lem-
mas 4.4 and 4.7 recursively, we see that

levk(L/K) ⩽ lev(L1 . . . Ln/K) ⩽ d.

(b) Recall that K (d) is generated by ﬁnite extensions L/K of level ⩽ d. In order to
prove that K (d) ⊂ E(d) it suﬃces to show that every such L is contained in E(d). This
follows from the inequality levk(LE/E) ⩽ levk(L/K) of Lemma 4.4.
Now suppose E is a ﬁnite extension of K and levk(E/K) ⩽ d. We want to prove that
in this case E(d) ⊂ K (d). It suﬃces to show that every ﬁnite extension M/E of level ⩽ d
lies in K (d), i.e., levk(M/K) ⩽ d. This follows from Lemma 4.7.

(c) Set U = ⋃ E(d)
f.g.. By part (b), E(d)
f.g. ⊂ E(d) for each ﬁnitely generated ﬁeld K ⊂
Ef.g. ⊂ E. Hence, U ⊂ E(d). To prove the opposite inclusion, we proceed in three steps.
(i) We reduce to the case, where K = k. Indeed, every intermediate ﬁeld k ⊂ E0 ⊂ E
such that E0 is ﬁnitely generated over k lies in E1 = KE0 which is ﬁnitely generated over
K. By part (b), E(d)
0 ⊂ E(d)
1 ⊂ U. Thus
⋃ E(d)
0 ⊂ U ⊂ E(d)

where the ﬁrst union is over ﬁnitely generated subextensions k ⊂ E0 ⊂ E. If we know
that the ﬁrst union is E(d), then both of these inclusions are equalities, and U = E(d), as
desired. From now on we will assume that K = k.
(ii) U is a subﬁeld of E(d). Indeed, suppose x1 ∈ E(d)
1 and x2 ∈ E(d)
2 , where k ⊂ Ei ⊂ E
and Ei is ﬁnitely generated over k for i = 1, 2. Assume x1 ̸= 0. We want to show that
x1 ± x2, x1 · x2 and x
−1
1 all lie in U. Indeed, the composite E3 = E1E2 (in E) is also
ﬁnitely generated over k. Hence E(d)
3 is contained in U. By part (b), x1 ∈ E(d)
1 ⊂ E(d)
3
and x2 ∈ E(d)
2 ⊂ E(d)
3 . We conclude that x1 ± x2, x1 · x2 and x
−1
1 ∈ E(d)
3 ⊂ U, as desired.
(iii) U contains E. This is because U contains k(x) for every x ∈ E.

HILBERT’S 13TH PROBLEM FOR ALGEBRAIC GROUPS 15

(iv) U contains E(d). It suﬃces to show that U contains every ﬁnite extension L/E such
that levk(L/E) ⩽ d. Recall that by Lemma 6.4, L/E descends to L0/E0 for some ﬁeld
k ⊂ E0 ⊂ E such that E0 is ﬁnitely generated over k and levk(L0/E0) = levk(L/E) ⩽ d.
Thus L0 ⊂ E(d)
0 ⊂ U. Since U is a subﬁeld of E containing both E and L0, it contains
L = EL0.

(d) Part (b) tells us that K (n) ⊂ (K (d))(n) = (K (n))(n). Thus it suﬃces to show that
(K (n))(n) = K (n), i.e., that K (n) is closed at level n. In other words, we may assume
without loss of generality that n = d.
Let E = K (d). We want to show that E(d) = K (d). By part (c), it suﬃces to show
that L
(d) = K (d) for every intermediate extension K ⊂ L ⊂ E = K (d), where L is ﬁnitely
generated (or equivalently, ﬁnite) over K. Since K ⊂ L ⊂ K (d), part (a) tells us that
levk(L/K) ⩽ d. The desired equality, L
(d) = K (d), is now given by the second assertion
in part (b). □

Corollary 6.5. Suppose K ∈ Fieldsk is closed at level d ⩾ 1. Then K is perfect and
solvably closed.

Proof. Suppose L/K is a solvable or purely inseparable extension. Our goal is to show that
K = L. Indeed, by Lemma 4.6, levk(L/K) ⩽ 1. By Proposition 6.3(a), K ⊂ L ⊂ K (d).
Since K is closed at level d, K (d) = K and thus K = L. □

7. The resolvent degree of a functor

Following Merkurjev, Berhuy and Favi [1], we will now deﬁne essential dimension for
a broader class of objects, beyond ﬁnite ﬁeld extensions. Let k be a base ﬁeld, and
F : Fieldsk → Sets be a functor from the category of ﬁeld extensions K/k to the category
of sets. All functors in this paper will be assumed to be covariant. We think of F as
specifying the type of object we are considering, and F (K) as the set of objects of this
type deﬁned over K. Given a ﬁeld extension k ⊂ K ⊂ K ′, we think of the natural map
F (K) → F (K ′) as base change. The image of α ∈ F (K) under this map will be denoted
by αK ′.

Deﬁnition 7.1. Any object α ∈ F (K) in the image of the natural map F (K0) → F (K)
is said to descend to K0. The essential dimension edk(α) is deﬁned as the minimal value
of trdegk(K0), where the minimum is taken over all intermediate ﬁelds k ⊂ K0 ⊂ K such
that α descends to K0.

Example 7.2. Consider the functor Alg : Fieldsk → Sets′, where Alg(K) is the set of iso-
morphism classes of ﬁnite-dimensional K-algebras. Here natural map Alg(K) → Alg(K ′)
takes a K-algebra A to the K ′-algebra K ′ ⊗K A. Let K ∈ Fieldsk and A be a ﬁnite-
dimensional K-algebra. If we view A as an object in F (K), then edk(A) given by Deﬁni-
tion 7.1 is the same as edk(A) given by Deﬁnition 2.2.

Now let F be a functor from the category Fieldsk of ﬁeld extensions K/k to the category
Sets′ of sets with a marked element. We will denote the marked element in F (K) by 1
and will refer to it as being “split”. We will say that a ﬁeld extension L/K splits an

16 ZINOVY REICHSTEIN

object α ∈ F (K) if αL = 1. Let us assume that

for every ﬁeld K/k and every α ∈ F (K), α can be(6)
 split by a ﬁeld extension L/K of ﬁnite degree.

This is a strong condition on F ; in particular, it implies that F (K) = {1} whenever K is
algebraically closed.

Deﬁnition 7.3. Let F : Fieldsk → Sets′ be a functor satisfying condition (6), K/k be a
ﬁeld extension and α ∈ F (K).
(a) The resolvent degree rdk(α) is the minimal integer d ⩾ 0 such that α is split by a
ﬁeld extension L/K of level d (or equivalently, of level ⩽ d).
(b) The resolvent degree rdk(F ) of the functor F is the maximal value of rdk(α), as K
ranges over all ﬁelds containing k and α ranges over F (K).

Remarks 7.4. (1) Note that the level levk(L/K) plays a similar role in Deﬁnition 7.3 to
the role played by the transcendence degree trdegk(K0) in Deﬁnition 7.1.
(2) Condition (6) ensures that rdk(α) is ﬁnite for every K ∈ Fieldsk and every α ∈
F (K). On the other hand, rdk(F ) can a priori be inﬁnite, even though no examples
where rdk(F ) > 1 are known.

Example 7.5. Consider the functor ´Etn : Fieldsk → Sets′, where ´Et(K) is the set of
isomorphism classes of n-dimensional ´etale algebras L/K. Recall that an n-dimensional
´etale algebra L is a direct product of the form L = L1 × . . . × Lr, where each Li is a ﬁnite
separable ﬁeld extension of K and [L1 : K] + . . . + [Lr : K] = n.

(a) If L/K is a separable ﬁeld extension of degree n, and [L] is its class in ´Etn(K), then
rdk([L]) = levk(L/K).
(b) More generally, if L = L1 × . . . × Lr is a direct product of separable extensions of
K as above, and [L] is its class in ´Etn(K), then rdk([L]) = maxi=1,...,r levk(Li/K).

(c) rdk(´Et) = max levk(L/K), where the maximum is taken over all separable ﬁeld
extensions L/K of degree ⩽ n.

Proof. (a) By the Primitive Element Theorem, L ≃K K[x]/(f (x)), where f (x) ∈ K[x] is
an irreducible separable polynomial of degree n. A ﬁeld extension L
′/K splits [L] if and
only if f (x) splits as a product of linear factors over L
′. Equivalently, L
′ splits L if and
only if L
′ contains the normal closure L
norm of L over K. By Remark 4.2(2),

rdk([L]) = min{levk(L
′/K) ∣
∣ L
norm ⊂ L
′} = levk(L
norm/K).

On the other hand, by Lemma 4.8, levk(L
norm/K) = levk(L/K).
(b) A ﬁeld extension L
′/K splits [L] if and only if it splits each [Li] ∈ ´Et[Li:K](K).
Hence, by part (a), rdk([L]) ⩾ maxi=1,...,r rdk([Li]) = maxi=1,...,r levk(Li/K). To prove
the opposite inequality, take L
′ to be the compositum of Li over K. Then L
′ splits [L].
Moreover, combining Lemmas 4.4 and 4.7, we obtain

rdk([L]) ⩽ levk(L
′/K) ⩽ max
i=1,...,r levk(Li/K).

(c) is an immediate consequence of (b). □

HILBERT’S 13TH PROBLEM FOR ALGEBRAIC GROUPS 17

Lemma 7.6. Let F : Fieldsk → Sets′ be a functor satisfying condition (6), K/k be a ﬁeld
extension and α ∈ F (K). Then
(a) rdk(αK ′) ⩽ rdk(α) for any ﬁeld K ′ containing K.
(b) rdk(α) ⩽ edk(α).
(c) rdk(F ) ⩽ edk(F ).

Proof. (a) If α is split by a ﬁnite extension L/K such that levk(L/K) = d, then αK ′ is
split by the ﬁnite extension K ′L/K ′ of level levk(K ′L/K ′) ⩽ d; see Lemma 4.4.
(b) Set d = edk(α). Then α descends to α0 ∈ F (K0) for some intermediate ﬁeld
k ⊂ K0 ⊂ K such that trdegk(K0) = d. Since F satisﬁes condition (6), α0 is split by
some ﬁnite extension L0/K0. Now

rdk(α) ⩽ rdk(α0) ⩽ levk(L0/K0) ⩽ edk(L0/K0) ⩽ d,

as desired. Here the ﬁrst inequality follows from part (a), the second from the deﬁnition of
rdk(α0), the third from Remark 4.2(3), and the fourth from the fact that trdegk(K0) = d.
(c) is an immediate consequence (b). □

Lemma 7.7. Let k ⊂ k′ ⊂ K be ﬁeld extensions, Let F : Fieldsk → Sets′ be a functor
satisfying condition (6) and α ∈ F (K). Then
(a) rdk(α) ⩾ rdk′(α).
(b) Moreover, equality holds if k′ is algebraic over k.
(c) Furthermore, there exists an intermediate ﬁeld k ⊂ l0 ⊂ k′ such that l0 is ﬁnitely
generated over k and rdl(α) = rdk′(α) for every ﬁeld l between l0 and k′.

Proof. For every ﬁnite extension L/K splitting α, we have levk(L/K) ⩾ levk′(L/K).
Moreover, equality holds if k′ is algebraic over k; see Lemma 4.3. This proves (a) and (b).
For part (c), choose a splitting extension L/K such that d = levk′(L/K) assumes its
minimal possible value, d = rdk′(α). Now choose l0 as in Lemma 4.3(c). Then for any
intermediate ﬁeld l0 ⊂ l ⊂ k′,

rdl(α) ⩽ levl(L/K) = levk′(L/K) = d = rdk′(α).

Combining this inequality with the inequality of part (a), we conclude that rdl(α) =
rdk′(α). □

Lemma 7.8. If k is algebraically closed, then rdk(α) > 0 for any K ∈ Fieldsk and any
1 ̸= α ∈ F (K). In particular, rdk(F ) = 0 if and only if F is the trivial functor, i.e., if
and only if F (K) = 1 for every K ∈ Fieldsk.

Proof. Immediate from Lemma 4.5. □

Lemma 7.9. Let F1, F2, F3 be functors Fieldsk → Sets′ satisfying (6).
(a) Suppose F1 → F2 → F3 is an exact sequence 1. Then rdk(F2) ⩽ max {rdk(F1), rdk(F3)}.
(b) If a morphism F1 → F2 of functors has trivial kernel, then rdk(F1) ⩽ rdk(F2).
(c) If a morphism F2 → F3 of functors is surjective, then rdk(F3) ⩽ rdk(F2).
(d) If 1 → F1 → F2 → F3 → 1 is a short exact sequence, then rd(F2) = max {rdk(F1), rdk(F3)}.
In particular, rdk(F1 × F3) = max {rdk(F1), rdk(F3)}.

1This means that F1(K) → F2(K) → F3(K) is an exact sequence in Sets′ for every ﬁeld K/k.

18 ZINOVY REICHSTEIN

Proof. (a) Suppose α ∈ F2(K) for some ﬁeld K/k. Denote the image of α in F3(K) by
β. After passing to an extension L/K of level ⩽ rd(F3), we may assume that β is split.
Hence, αL ∈ F2(L) is the image of some γ ∈ F3(L). A further extension L
′/L of level
⩽ rd(F1) splits γ. Thus the composite extension K ⊂ L ⊂ L
′ splits α. We conclude that

rdk(α) ⩽ levk(L
′/K) ⩽ max {levk(L/K), levk(L
′/L)} ⩽ max {rdk(F1), rdk(F2)},

where the inequality in the middle follows from Lemma 4.7. Taking the maximum over all
ﬁelds K/k and all objects α ∈ F2(K), we conclude that rd(F2) ⩽ max {rdk(F1), rdk(F3)}.

(b) and (c): Apply part (a) to the exact sequences 1 → F1 → F2 and F2 → F3 → 1,
respectively.

(d) For the ﬁrst assertion combine the inequalities of (a), (b) and (c). The second
assertion is a special case of the ﬁrst with F3 = F1 × F2. □

Proposition 7.10. Let A be a diagonalizable group (i.e., a closed subgroup of the split
torus G
d
m) deﬁned over k. Then the functor H 2(∗, A) satisﬁes condition (6) and

rdk(H 2(∗, A)) ⩽ 1.

Proof. First let us consider the special case, where A = Gm. Recall that H 2(K, Gm) is
in a natural (functorial) bijection with the Brauer group Br(K). Thus it suﬃces to show
that every central simple algebra A over every F ∈ Fieldsk can be split by a solvable
extension of K. By the Primary decomposition Theorem we may assume without loss of
generality that the index of A is a prime power, pr. If char(k) ̸= p, then the Merkurjev-
Suslin Theorem tells us that A can be split by a solvable extension of K; see [20, Corollary
2.5.9]. If p = char(k), then by a theorem of Albert, A is Brauer-equivalent to a cyclic
algebra and thus can be split by a cyclic (and hence, once again, solvable) ﬁeld extension
of K. This completes the proof in the case where A = Gm.
If A = µn, then H 2(∗, µn) ≃ n Br(K), where n Br(K) is the n-torsion subgroup of
Br(K), and the same argument applies.
In general we write A as a direct product A1 ×k . . . ×k Ar, where each Ai is k-isomorphic
to Gm or µn for some integer n. Then H 2(∗, A) = H 2(∗, A1) × . . . × H 2(∗, Ar), and the
desired conclusion follows from Lemma 7.9(d). □

Remark 7.11. If A ̸= 1 in Proposition 7.10, then equality holds: rdk(H 2(∗, A)) = 1.
To prove this, we readily reduce to the case, where A = µn for some n ⩾ 2. In this
case, assume the contrary. Then for every K ∈ Fieldsk, every α ∈ H 2(K, µn) can be split
by a ﬁnite extension L/K of level 0. In particular, by Remark 6.2, if K contains k, then
K is closed at level 0, i.e., there are no non-trivial ﬁnite extensions L/K of level 0 and
thus H 2(K, µn) = 1. On the other hand, it is well known that if K = k(x, y), where x and
y are variables, the symbol algebra (x, y)n represents a non-trivial class in H 2(K, µn), a
contradiction. □

Remark 7.12. Using the Norm Residue Isomorphism Theorem (formerly known as the
Bloch-Kato Conjecture) in place of the Merkurjev-Suslin Theorem, one shows in the same
manner that rdk(H d(∗, A)) ⩽ 1 for every d ⩾ 1 and that equality holds if A ̸= 1.

HILBERT’S 13TH PROBLEM FOR ALGEBRAIC GROUPS 19

8. Functors preserving direct limits

In this section we will assume that our functor F : Fieldsk → Sets′ respects direct
limits. Examples include Galois cohomology functors H 1(∗, G), where G is an algebraic
group over k, as well as H d(∗, G) for every d ⩾ 2, if G is abelian. For such functors F
the study of resolvent degree can be facilitated by using the notion of level d closure of of
ﬁeld introduced in Section 6.

Proposition 8.1. Assume that a functor F : Fieldsk → Sets′ satisﬁes condition (6) and
respects direct limits. Let K ∈ Fieldsk and α ∈ F (K). Then
(a) rdk(α) ⩽ d if and only if α splits over K (d), i.e., αK (d) = 1.
(b) rdk(F ) ⩽ d if and only if F (K) = 1 for every ﬁeld K closed at level d.
(c) Suppose rdk(αK (d)) ⩽ m. Then rdk(α) ⩽ max{d, m}.
(d) Suppose rdk(β) ⩽ m for every ﬁeld E ∈ Fieldsk closed at level d and every β ∈
F (E). Then rdk(F ) ⩽ max{d, m}.

Proof. (a) Suppose rdk(α) ⩽ d. Then α splits over a ﬁnite extension L of K such that
levk(L/K) ⩽ d. By deﬁnition of K (d), L embeds into K (d) over K. Hence, αK (d) = 1.
Conversely, suppose α splits over K (d). Since F respects direct limits, α splits over
some subextension K ⊂ L ⊂ K (d) such that [L : K] < ∞. By Proposition 6.3(a),
levk(L/K) ⩽ d. Thus rdk(α) ⩽ d.
(b) Suppose rdk(F ) ⩽ d and K ∈ Fieldsk is closed at level d. By part (a), any
α ∈ F (K) splits over K (d). By Proposition 6.3(d), K (d) = K and thus α = 1. This shows
that F (K) = 1.
Conversely, assume F (K) = 1 whenever K ∈ Fieldsk is closed at level d. Let F be
an arbitrary ﬁeld containing k and α ∈ F (F ). By our assumption (with K = F (d)),
αF (d) = 1. Since F respects direct limits, αE = 1 for some F ⊂ E ⊂ F (d), where E
is ﬁnitely generated over F , i.e., [E : F ] < ∞. By Proposition 6.3(a), levk(E/F ) ⩽ d.
Hence, rdk(α) ⩽ d.
(c) Let n = max{d, m}. In view of part (a), our goal is to show that αK (n) = 1.
Set E = K (d). By Proposition 6.3(d), E is closed at level d and E(n) = K (n). By our
assumption, rdk(αE) ⩽ m. By part (a), αE(m) = 1. Since E(m) ⊂ E(n), we conclude that
αK (n) = αE(n) = 1.
(d) is an immediate consequence of (c). □

Deﬁnition 8.2. Let F : Fieldsk → Sets′ be a functor. For any ﬁeld k′ containing k, we
deﬁne Fk′ : Fieldsk′ → Sets′ to be a restriction of F to Fieldsk′. In other words, Fk′(K)
is only deﬁned if K contains k′, and for such K, Fk′(K) = F (K).

Proposition 8.3. Assume that a functor F : Fieldsk → Sets′ satisﬁes condition (6).
(a) If k′/k is a ﬁeld extension, then the functor Fk′ also satisﬁes condition (6) and
rdk(F ) ⩾ rdk′(Fk′).
(b) Moreover, if k′/k is an algebraic ﬁeld extension and F respects direct limits, then
rdk(F ) = rdk′(Fk′).

Proof. Let K ∈ Fieldsk and α ∈ F (K).

20 ZINOVY REICHSTEIN

(a) The ﬁrst assertion is obvious from Deﬁnition 8.2. To prove the second assertion, it
suﬃces to show that

(7) rdk(α) ⩾ rdk(αk′K) ⩾ rdk′(αk′K),

where k′K is a compositum of k′ and K. Indeed, the maximal value of the left hand side
over all K ∈ Fieldsk and all α ∈ F (K) is rdk(F ), where as the maximal value of the
right hand side is rdk′(Fk′). The ﬁrst inequality in (7) follows from Lemma 7.6(a) and
the second from Lemma 7.7(a).

(b) Here it suﬃces to show that

(8) rdk(α) = rdk(αk′K) = rdk′(αk′K).

The second equality follows from Lemma 7.7(b). To prove the ﬁrst inequality, it suﬃces
to show that

(9) K (d) = (k′K)(d)

for every d ⩾ 0. Indeed, if we can prove this, then α is split by K (d) if and only if αk′K is
split by (k′K)(d), and the desired equality follows from Proposition 8.1(a).
To prove (9), note that by Remark 6.2, K ⊂ k′K ⊂ K (0). By Proposition 6.3,

K (d) ⊂ (k′K)(d) ⊂ (K (0))(d) = K (d),

and (9) follows. □

Example 8.4. Let ´Etn : Fieldsk → Sets′ be the functor of n-dimensional ´etale algebras
introduced in Example 7.5. If d ⩾ rdk(´Etn), and K ∈ Fieldsk is closed at level d, then
every polynomial of degree ⩽ n splits into a product of linear factors over K.

Proof. If n = 1, the assertion is vacuous, so we may assume that n ⩾ 2. One readily
checks that the functor (´Etn)k is non-trivial for any n ⩾ 2. Hence,

rdk(´Etn) ⩾ rdk (
(´Etn)k) ⩾ 1,

where k denotes an algebraic closure of k, the ﬁrst inequality follows from Proposi-
tion 8.3(a), the second from Lemma 7.8. Thus d ⩾ 1. By Corollary 6.5, K is perfect.
It remains to show that there does not exist an irreducible polynomial f (x) ∈ K[x] of
degree m for any 2 ⩽ m ⩽ n. Indeed, assume the contrary. Then

E = K[x]/(f (x)) × K × . . . × K︸ ︷︷ ︸
n − m times

is a non-split ´etale algebra of degree n. On the other hand, ´Etn(K) = 1 by Proposi-
tion 8.1(b), i.e., every ´etale algebra of degree n over K is split, a contradiction. □

Remark 8.5. Proposition 8.3(b) may fail if

(a) the functor F is not required to respect direct limits or if

(b) the ﬁeld k′ is not required to be algebraic over k.

HILBERT’S 13TH PROBLEM FOR ALGEBRAIC GROUPS 21

Proof. Our counterexamples in parts (a) and (b) will both rely on the following construc-
tion. Let F : Fieldsk → Sets′ be a functor and Λ be a collection of ﬁelds K ⊂ Fieldsk closed
under inclusion. That is, if L ∈ Λ and K ⊂ L, then K ∈ Λ. Set F Λ : Fieldsk → Sets′ by

F Λ(K) =
 {
F (K), if K ∈ Λ, and
{1}, if K ̸∈ Λ.

If K ⊂ L be a ﬁeld extension, the natural map F Λ(K) → F Λ(L) is deﬁned to be the
same as the natural map F (K) → F (L) if L ∈ Λ and to be the trivial map (sending every
element of F (K) to 1) if L ̸∈ Λ. It is easy to see that F Λ is well deﬁned. Moreover, if F
satisﬁes condition (6), then so does F Λ. Informally, we think of F Λ as a truncation of F .
The starting point for both parts is a functor F : Fieldsk → Sets′
k which satisﬁes (6),
respects direct limits, and such that rdk(F ) ⩾ 1. There are many examples of such
functors, e.g., F = H 2(∗, Gm); see Remark 7.11. Choose a ﬁeld K ∈ Fieldsk and an
object α ∈ F (K) such that rdk(α) ⩾ 1. Since F respects direct limits, α descends to
α0 ∈ F (K0) for some intermediate ﬁeld k ⊂ K0 ⊂ K such that K0 is ﬁnitely generated
over k. By Lemma 7.6(a), rdk(α0) ⩾ rdk(α) ⩾ 1. After replacing K by K0 and α by α0,
we may assume that K is ﬁnitely generated over k.
(a) Consider the truncated functor F Λ, where

Λ = {K/k ∣
∣ K is ﬁnitely generated over k}.

Note that rdk(α) ⩾ 1 whether we view α as an object in F or F Λ. On the other hand,
if the algebraic closure k is not ﬁnitely generated over k (e.g., if k = Q), then no ﬁeld
containing k can be ﬁnitely generated over k. This tells us that the truncated functor F Λ
k
is the trivial functor and consequently, rdk (F Λ
k ) = 0. We conclude that Proposition 8.3(b)
fails for F Λ if k′ = k.
(b) Set m = trdegk(K) and consider the truncated functor F Λ, where

Λ = {K/k ∣
∣ trdegk(K) ⩽ m}.

The functor F Λ continues to satisfy condition (6) and to respect direct limits. If trdegk(k′) >
m, then F Λ
k′ is trivial and thus rdk′(F Λ) = 0. On the other hand, rdk(α) ⩾ 1 whether
we view α as an object in F or F Λ. In summary, rdk(F Λ) ⩾ 1, rdk′(F Λ
k′) = 0, and
Proposition 8.3(b) fails for F Λ. □

9. Change of base field

As we saw in Remark 8.5(b), Proposition 8.3(b) fails if k′ is not assumed to be algebraic
over k. In this section we will show that under an additional condition on the functor F ,
the equality of Proposition 8.3(b) can be (largely) salvaged for an arbitrary ﬁeld extension
k′/k. The condition we will impose on F is as follows:

the natural map F (E) → F (E((t))) has trivial(10) kernel for every perfect ﬁeld E containing k.

Note that this is only slightly weaker than Condition (*) considered by Merkurjev in [25,
Section 3]. The only diﬀerence between the two is that in [25], E is not required to be
perfect. As is pointed out in [25], this is a natural condition, which is often satisﬁed.

22 ZINOVY REICHSTEIN

Proposition 9.1. Assume that a functor F : Fieldsk → Sets′ satisﬁes conditions (6)
and (10) and respects direct limits. Then

rdk′(Fk′) ⩽ rdk(F ) ⩽ max{rdk′(Fk′), 1}

for any ﬁeld extension k′/k.

The remainder of this section will be devoted to proving Proposition 9.1. We begin
with the following lemma.

Lemma 9.2. Assume that a functor F : Fieldsk → Sets′ satisﬁes condition (6) and re-
spects direct limits. Let k′/k be a ﬁeld extension, K ∈ Fieldsk and α ∈ F (K). Then
there exists an intermediate ﬁeld k ⊂ l ⊂ k′ such that l is ﬁnitely generated over k and
rdl(αlK) = rdk′(αk′K). Here k′K is some compositum of k′ and K over k. The compositum
lK is taken in k′K.

Proof. For any intermediate ﬁeld k ⊂ l ⊂ k′, we have

rdl(αlK) ⩾ rdl(αk′K) ⩾ rdk′(αk′K);

see (7). Our goal is to show that the opposite inequality holds for a suitably chosen
intermediate ﬁeld k ⊂ l ⊂ k′, where l is ﬁnitely generated over k.
Set d = rdk′(αk′K). By Lemma 7.7(c) there exists an intermediate extension k ⊂ l0 ⊂ k′

such that l0 is ﬁnitely generated over k, and d = rdl(αk′K) for any intermediate ﬁeld
l0 ⊂ l ⊂ k′. After replacing k by l0 and α by αl0K, we may assume without loss of
generality that k = l0. In particular, d = rdk(αk′K). By Proposition 8.1(a), α splits over
(k′K)(d). Since F preserves direct limits, α splits over L
(d) for some intermediate extension
K ⊂ L ⊂ (k′K) such that L is ﬁnitely generated over K. Any such L is contained in lK
for some intermediate ﬁeld k ⊂ l ⊂ k′, where l is ﬁnitely generated over k. Thus α splits
over (lK)(d). By Proposition 8.1(a) this implies that rdl(αlK) ⩽ d, as claimed. □

Proof of Proposition 9.1. The ﬁrst inequality rdk′(Fk′) ⩽ rdk(F ) is proved in Proposi-
tion 8.3(a). We will thus focus on proving the second inequality. Let K be a ﬁeld
containing k and α ∈ F (K). Our goal is to show that

(11) rdk(α) ⩽ max{rdk′(αk′K), 1}.

If we can prove this, then taking the maximum over all K ∈ Fieldsk and all α ∈ F (K),
we will obtain the desired inequality rdk(F ) ⩽ max{rdk′(Fk′), 1}.
We begin by reducing to the case where k′ is ﬁnitely generated over k. Indeed, choose
l as in Lemma 9.2. That is, l is ﬁnitely generated over k and rdl(αlK) = rdk′(αk′K). For
the purpose of proving (11) we may now replace k′ by l.
From now on we will assume k′ is ﬁnitely generated over k. Choose a transcendence
basis t1, . . . , tn for k′/k and set ki = k(t1, . . . , ti), so that k′ is algebraic over kn. By (8),

rdkn(αknK) = rdkn(αk′K) = rdk′(αk′K).

Thus we may further replace k′ by kn. It remains to show that

(12) rdk(α) ⩽ max{rdk(t)(αK(t)), 1},

where t is a variable. Indeed, applying this inequality recursively, we readily deduce (11):

rdk(α) ⩽ max{rdk1(αk1K), 1} ⩽ . . . ⩽ max{rdkn(αknK), 1}.

HILBERT’S 13TH PROBLEM FOR ALGEBRAIC GROUPS 23

(Recall that here k′ = kn.)
The remainder of the proof will be devoted to establishing the inequality (12). First
observe that we may assume without loss of generality that K is closed at level 1. Indeed,
let K (1) be the level 1 closure of K. By Proposition 8.1(c),

rdk(α) ⩽ max{rdk(αK (1)), 1}

and by Lemma 7.6(a), rdk(t)(αK (1)(t)) ⩽ rdk(t)(αK(t)),

where K (1) is the level 1 closure of K. These inequalities show that in the course of
proving (12), we may replace K by K (1) and α by αK (1). In other words, for the purpose
of proving (12), we may assume that K is closed at level 1. In particular, we may assume
that K is a perfect ﬁeld; see Corollary 6.5.
We now proceed with the proof of (12) under the assumption that K is a perfect ﬁeld.
First we observe that by Lemma 7.6(a), rdk(t)(αK(t)) ⩽ rdk(t)(αK((t))). Thus we only need
to show that

(13) rdk(α) ⩽ max{rdk(t)(αK((t))), 1},

Set d = rdk(t)(αK((t))). By deﬁnition there exists a ﬁnite ﬁeld extension L/K((t)) such
that αL = 1 and levk(t) (L/K((t))) = d.
The ﬁeld K((t)) carries a natural discrete valuation ν : K((t))∗ → Z with uniformizer

t, trivial on K. Lift ν to a discrete valuation L
∗ → 1
e Z, where e is the ramiﬁcation index.
By abuse of notation I will continue to denote this lifted valuation by ν. I will denote the
residue ﬁeld of L relative to this valuation by Lν.
Note that since K((t)) is complete with respect to ν, so is L. Moreover, since K is
perfect, so is Lν. Note also that we are in equal characteristic situation here:

char(Lν) = char(K) = char(k) = char(k(t)) = char(K((t))) = char(L).

By the Cohen Structure Theorem, L is isomorphic to the ﬁeld of Laurent series Lν((s))
in one variable over Lν. Since αL = 1 and Lν is perfect, the natural map

F (Lν) → F (Lν((s))) = F (L)

has trivial kernel, by our assumption (10). We conclude that αLν = 1. In other words,
Lν/K is a splitting extension for α. By Proposition 5.1,

rdk(α) ⩽ levk(Lν/K) ⩽ max{levk(L/K((t))), 1} = max{d, 1},

where K is the residue ﬁeld of K((t)). Proposition 5.1 applies here because we are
assuming that the residue ﬁeld Kν = K is perfect. This completes the proof of Proposi-
tion 9.1. □

10. The resolvent degree of an algebraic group

Let G be an algebraic group over k, not necessarily aﬃne, smooth or connected. Of
particular interest to us will be the functor H 1(∗, G) whose objects over K are isomorphism
classes of G-torsors over Spec(K). Here torsors are assumed to be locally trivial in the
ﬂat (fppf) topology. If G is smooth over k, this is equivalent to being trivial in the
´etale topology. For every ﬁeld K containing k, the set H 1(K, G) has a marked element,

24 ZINOVY REICHSTEIN

represented by the split G-torsor GK → Spec(K), where GK = G ×Spec(k) Spec(K). The
functor H 1(∗, G) satisﬁes condition (6).

Deﬁnition 10.1. We deﬁne edk(G) = edk(H 1(∗, G)) and rdk(G) = edk(H 1(∗, G)).

The essential dimension edk(G) of an algebraic group G/k has been much studied;
see [26, 27]. If G is an abstract ﬁnite group (viewed as an algebraic group over k) and
char(k) = 0, our deﬁnition of rdk(G) above coincides with the deﬁnition given by Farb and
Wolfson [16]. To the best of my knowledge, rdk(G) has not been previously investigated
for other algebraic groups G/k.
In view of Proposition 8.3(b), passing from G to Gk does not change the resolvent
degree. Thus from now on we will assume that k is algebraically closed.

Example 10.2. The functor ´Etn introduced in Example 7.5 is isomorphic to H 1(∗, Sn)
and thus rdk(´Etn) = rdk(Sn). By Example 7.5,

rdk(Sn) = max levk(L/K).

The algebraic form of Hilbert’s 13th Problem asks for the value of rd(n) = rdC(Sn).

Remark 10.3. Recall that the classical deﬁnition of rd(n) is motivated by wanting to
express a root of a general polynomial f (x) = x
n + a1x
n−1 + . . . + an as a composition of
algebraic functions in ⩽ d variables. This is equivalent to ﬁnding the smallest integer d
such that the 0-cycle in A1
K given by f (x) = 0 has an L-point, for some ﬁeld extension
L/K of level ⩽ d. If G is an algebraic group over k, K is a ﬁeld containing k and
T → Spec(K) is a G-torsor, then our deﬁnition of rdk(T ) retains this ﬂavor. Indeed,
saying that T is split by L is equivalent to saying that T has an L-point.

Remark 10.4. (cf. [16, Lemma 3.2]) Let G be an algebraic group deﬁned over a ﬁeld k,
K be a ﬁeld containing k, and α : T → Spec(K) be a G-torsor. Setting F = H 1(∗, G) in
Lemma 7.6, we obtain the inequalities rdk(α) ⩽ edk(α) and rdk(G) ⩽ edk(G).

Remark 10.5. (cf. [16, Lemma 3.13]) Let G be a ﬁnite group and H be a subgroup.
We will view G and H as algebraic groups over k. The long exact sequence in Galois
cohomology associated to 1 −→ H i
−→ G (see [34, Section I.5.4]) readily show that the
induced morphism i∗ : H 1(∗, H) → H 1(∗, G) has trivial kernel. By Lemma 7.9(b), we
conclude that rdk(H) ⩽ rdk(G).

Example 10.6. (cf. [16, Corollary 3.4]) If G is a solvable ﬁnite group, then rdk(G) ⩽ 1.
Indeed, every element of H 1(K, G) can be split by a solvable extension L/K, and a
solvable extension has level ⩽ 1 by Lemma 4.6(a). Moreover, if we further assume that
G ̸= 1, then rdk(G) = 1. This follows from Lemma 7.8 and Proposition 8.3(b).

Recall that an algebraic group G deﬁned over a ﬁeld k is called special if H 1(∗, G) is
the trivial functor, i.e., H 1(K, G) = 1 for every ﬁeld K containing k. This notion is due
to Serre [31]. (Note that [31] is reprinted in [35].)

Lemma 10.7. (a) Let G be an algebraic group over an algebraically closed ﬁeld k. Then
(a) G is special if and only if rdk(G) = 0.
(b) If G is connected and solvable, then rdk(G) = 0.

HILBERT’S 13TH PROBLEM FOR ALGEBRAIC GROUPS 25

(c) If G is the special linear group SLn or the symplectic group Sp2n, then rdk(G) = 0
for any n ⩾ 1.

Proof. (a) By Lemma 7.8, rdk(G) = 0 if and only if H 1(∗, G) is the trivial functor, i.e., if
and only if G is special.
(b) Every connected solvable group is special; see [31, Section 4.4(a)].
(c) SLn and Sp2n are special; see [31, Section 4.4(b) and (c)]. □

We now record several simple but useful observations about the behavior of resolvent
degree in exact sequences of groups.

Proposition 10.8. Consider a short exact sequence of algebraic groups

(14) 1 → A → B → C → 1

deﬁned over a ﬁeld k. Then

(a) rdk(B) ⩽ max {rdk(A), rdk(C)}.

(b) If B is isomorphic to the direct product A×C, then rdk(B) = max {rdk(A), rdk(C)}.

(c) If G is a diagonalizable algebraic group over k, then rdk(G) ⩽ 1.

(d) Suppose (14) is a central short exact sequence and A is diagonalizable over k. Then

rdk(B) ⩽ max {rdk(C), 1} and rdk(C) ⩽ max {rdk(B), 1}.

Proof. (a) follows from Lemma 7.9(a) applied to the exact sequence of functors H 1(∗, A) →
H 1(∗, B) → H 1(∗, C) induced by (14).
(b) follows from Lemma 7.9(d), since in this case the functor H 1(∗, B) is isomorphic to
H 1(∗, A) × H 1(∗, C).
(c) Write G as a product G1 × . . . × Gr, where each Gi is isomorphic either to Gm or
µn for some n ⩾ 2. By part (b), it suﬃces to show that rdk(Gi) ⩽ 1 for each i. Now
recall that rdk(Gm) = 0 by Lemma 10.7(b). On the other hand, rdk(µn) ⩽ edk(µn) by
Remark 10.4, and edk(µn) = 1 for every n ⩾ 2; see, e.g., [26, Example 3.5].
(d) To prove the ﬁrst inequality, combine parts (a) and (c). The second inequal-
ity follows from Lemma 7.9(a) applied to the exact sequences of functors H 1(∗, B) →
H 1(∗, C) → H 2(∗, A) induced by (14). Recall that rdk(H 2(∗, A)) ⩽ 1 by Proposi-
tion 7.10. □

Corollary 10.9. Let G be a connected reductive aﬃne algebraic group, T be a split max-
imal torus of G, N be the normalizer of T in G, and W = N/T be the Weyl group.
Then
 rdk(W ) ⩾ rdk(N) ⩾ rdk(G).

Proof. By [10, Corollary 5.3] the natural morphism H 1(K, N) → H 1(K, G) is surjective;
see also [34, Lemma III.4.3.6]. Hence, rdk(N) = rd(H 1(∗, N)) ⩾ rdk(H 1(∗, G)) = rdk(G)
by Lemma 7.9(c).
The inequality rdk(W ) ⩾ rdk(N) follows from Proposition 10.8(a) applied to the exact
sequence 1 → T → N → W → 1. Note that by Lemma 10.7(b), rdk(T ) = 0. □

26 ZINOVY REICHSTEIN

11. The resolvent degree of an abelian variety

In this section we will assume that the base ﬁeld k is algebraically closed. This assump-
tion is harmless in view of Proposition 8.3(b).
Recall that for every algebraic group G deﬁned over k, there exists a smooth (i.e.,
reduced) subgroup Gred such that G(k) = Gred(k); see [18, Exp.VIA, Section 0.2].

Lemma 11.1. Let K be a ﬁeld containing k and let i : Gred ֒→ G be the natural inclusion
and i∗ : H 1(K, Gred) → H 1(K, G) be the induced map in cohomology. Then
(a) i∗ is injective.
(b) If K is a perfect ﬁeld, then i∗ is bijective.

Proof. Let γ ∈ H 1(K, G). By [34, I.5.4, Corollary 2], the ﬁber of (i∗)−1(γ) may be
identiﬁed with the set of orbits of γG(K) in ( γG/ γGred)(K). 2 Here γG denotes the twist
of G by a cocycle representing γ, and similarly for Gred. Since the homogeneous space
G/Gred is purely inseparable over Spec(k), the homogeneous space γG/ γGred is purely
inseparable over Spec(K). (To see this, pass to a splitting ﬁeld of γ.) Thus ( γG/ γGred)
can have at most one Spec(K)-point. This shows that the ﬁber of (i∗)−1(γ) has at most
one element, proving (a). If K is perfect, then γG(K) in ( γG/ γGred) has exactly one K-
point. In this case the ﬁber of (i∗)−1(γ) has exactly one element for every γ ∈ H 1(K, Gred).
This proves (b). □

Recall that an inﬁnitesimal group is a connected 0-dimensional group. Non-trivial
inﬁnitesimal groups exist only in prime characteristic.

Proposition 11.2. Let G be an algebraic group over k. Then
(a) rdk(G) ⩽ max{rdk(Gred), 1}.
(b) If G be an inﬁnitesimal group over k, then rdk(G) ⩽ 1.
(c) Let G be a 0-dimensional abelian group over k (not necessarily smooth or connected).
Then rdk(G) ⩽ 1.

Proof. (a) In view of Proposition 8.1(d), it suﬃces to show that rdk(α) ⩽ rdk(Gred) for
every ﬁeld K/k such that K is closed at level 1 and every α ∈ H 1(K, G). Indeed, every
such ﬁeld K is perfect; see Corollary 6.5. Thus by Lemma 11.1, α is the image of some
β ∈ H 1(K, Gred). Every ﬁeld extension of K which splits β also splits α. This tells us
that rdk(α) ⩽ rdk(β) ⩽ rdk(Gred),
as claimed.
(b) If G is inﬁnitesimal, then Gred = 1. Thus rdk(Gred) = 0, and rdk(G) ⩽ 1 by part
(a).
(c) Consider the exact sequence 1 → G0 → G → G/G0 → 1. The group G0 is inﬁni-
tesimal; thus rdk(G0) ⩽ 1 by part (b). On the other hand, by [18, Exp. VIA, Proposition
5.5.1], G/G0 is ´etale. Since k is algebraically closed, this tells us that G/G0 is constant,
i.e., is isomorphic to an abstract ﬁnite abelian group, viewed as an algebraic group over
k. In particular, rdk(G/G0) ⩽ 1 by Example 10.6. Applying Proposition 10.8(a) to the
exact sequence 1 → G0 → G → G/G0 → 1, we obtain rdk(G) ⩽ 1. □

2In [34] only ´etale cohomology is considered. The same argument works for ﬂat cohomology.

HILBERT’S 13TH PROBLEM FOR ALGEBRAIC GROUPS 27

Proposition 11.3. Let A be an abelian variety over k. Then rdk(A) ⩽ 1.

Proof. Let K be a ﬁeld containing k. Recall that H 1(K, A) (the Weil-Chˆatelet group of
AK) is torsion. Thus it suﬃces to show that rdk (H 1(∗, A)[d]
) ⩽ 1 for every integer d ⩾ 1.
Examining the exact sequence in cohomology associated to

1 // A[d] // A × d // A // 1

we conclude that H 1(∗, A[d]) surjects onto H 1(∗, A)[d]; see [36, Section VIII.2] 3. Lemma 7.9(c)
now tells us that

rdk(A) = rdk (H 1(∗, A)[d]
) ⩽ rdk (
H 1(∗, A[d])) = rdk(A[d]).

Since A[d] is a 0-dimensional abelian group over k, rdk(A[d]) ⩽ 1 by Proposition 11.2(c),
and part (c) follows. □

12. Proof of Theorem 1.2

Setting F to be the non-abelian cohomology functor H 1(∗, G) in Proposition 8.3(b),
we obtain rdk(G) = rdk(G) and rdk′(G) = rdk′(Gk′), where k is the algebraic closure of k
and similarly for k′. After replacing k and k′ by k and k′, we may assume that k and k′

are algebraically closed.
The following two lemmas will allow us to complete the proof by appealing to Propo-
sition 9.1. Lemma 12.1 tells us that the conditions of Proposition 9.1 are satisﬁed by the
non-abelian cohomology functor F = H 1(∗, G) and thus

rdk′(Gk′) ⩽ rdk(G) ⩽ {rdk′(Gk′), 1}.

This yields the desired equality, rdk(G) = rdk′(Gk′), assuming rdk′(Gk′) ⩾ 1. Lemma 12.2
shows that this equality also holds when rdk′(Gk′) = 0.

Lemma 12.1. Let k be algebraically closed ﬁeld and G be an algebraic group over k.
Then the natural map H 1(E, G) → H 1(E((t)), G) has trivial kernel for every perfect ﬁeld
E containing k.

Proof. We begin by reducing the problem to the case where G is smooth. Indeed, let Gred
be the associated smooth group. Consider the following diagram

1 // H 1(E, Gred)

  
 // H 1(E, G)

  
 // 1

1 // H 1(E((t)), Gred) // H 1(E((t)), G),

where the bottom row is exact by Lemma 11.1(a) and the top row is exact by Lemma 11.1(b).
(Recall that we are assuming E to be perfect.) An easy diagram chase shows that if the
left vertical map has trivial kernel, then so does the right vertical map. In other words,
if the lemma holds for Gred, then it also holds for G. From now on we will assume that
G is smooth.

3A is assumed to be an elliptic curve in [36], but the same argument goes through for an abelian variety
of arbitrary dimension.

28 ZINOVY REICHSTEIN

Now suppose α ∈ H 1(E, G) lies in the kernel of the map H 1(E, G) → H 1(E((t)), G).
This means that the G-torsor π : T → Spec(E) representing α splits over Spec (E((t)))
.
In other words, πE[[t]] : T × Spec(E[[t]]) → Spec(E[[t]]) has a section s : Spec(E((t))) →
T × Spec(E((t))) over the generic point of Spec(E[[t]]). We would like to show that this
section extends to all of Spec(E[[t]]). If we were able to do this, then restricting to the
closed point of Spec(E[[t]]) (i.e., setting t = 0), would yield an E-point on T , showing
that T is split, i.e., α = [T ] = 1 in H 1(E, G), as desired. To show that s can be extended
to all of Spec(E[[t]]), it is natural to appeal to the valuative criterion for properness. If
G is proper over Spec(k) (i.e., the identity component of G is an abelian variety), then T
is proper over Spec(K), a desired lifting exists by the valuative criterion for properness,
and the proof is complete. In general, T is not proper over Spec(K), so the valuative
criterion for properness does not apply. Nevertheless, we will now show that a variant of
this argument still goes through, if we modify T slightly as follows.
By Chevalley’s Structure Theorem [12, 13] there exists a unique connected smooth
normal aﬃne k-subgroup N = G0
aﬀ of G0 such that the quotient G0/N is an abelian
variety. Since G is smooth and k is an algebraically closed ﬁeld, N is smooth, connected
and normal in G, and G/N is proper over Spec(k); see [3, Theorem 4.2 and Remark 4.3].
Let B be a Borel subgroup (i.e., a maximal connected solvable subgroup) of N. Then
the homogeneous space N/B is proper over Spec(k). Consequently G/B is proper over
G/N. Since G/N is proper over Spec(k), we conclude that G/B is proper over Spec(k)
and hence, T /B is proper over Spec(K). Now the valuative criterion for properness tells
us that the section
 s : Spec (
E((t))) → TSpec(E[[t]]) → (T /B)Spec(E[[t]])

extends to Spec(E[[t]]). Restricting to the closed point of Spec(E[[t]]), we obtain an E-
point on T /B. Denote this point by p : Spec(E) → T /B. The preimage of this E-point
under the natural map T → T /B is a B-torsor over Spec(E). Since B is connected and
solvable, it is special; see Lemma 10.7(b). Thus this B-torsor is split, i.e., has an E-point.
This shows that T has an E-point, i.e., T is split over E, as desired. □

Lemma 12.2. Let k ⊂ k′ be algebraically closed ﬁelds and G be an algebraic group over
k. Then the following conditions are equivalent.

(a) rdk′(G) = 0,

(b) Gk′ is a special group,

(c) Gk′ is aﬃne, and edk′(Gk′) = 0,

(d) G is aﬃne, and edk(G) = 0,

(e) G is a special group,

(f ) rdk(G) = 0.

Proof. (a) ⇐⇒ (b) and (e) ⇐⇒ (f) by Lemma 10.7(a).

(b) =⇒ (c): Suppose Gk′ is special, i.e., H 1(∗, Gk′) is the trivial functor. Then clearly
edk′(Gk′) = edk′(H 1(∗, Gk′)) = 0. Moreover, a special group is aﬃne; see [31, Theorem
4.1].
 HILBERT’S 13TH PROBLEM FOR ALGEBRAIC GROUPS 29

(c) ⇐⇒ (d): G is aﬃne if and only if Gk′ is aﬃne. Moreover, since k is algebraically
closed and G is aﬃne group over k, we have edk(G) = edk′(Gk′); see [4, Proposition 2.14]
or [43, Example 4.10].

(d) =⇒ (e) by [26, Proposition 3.16].

(f) =⇒ (a): By Proposition 8.3(a) with F = H 1(∗, G), rdk(G) ⩾ rdk′(Gk′). In particu-
lar, if rdk(G) = 0, then rdk′(Gk′) = 0. □

13. Proof of Theorem 1.3

Our proof of Theorem 1.3 will rely on the following proposition.

Proposition 13.1. Let D be a discrete valuation ring with fraction ﬁeld k and residue ﬁeld
k0. Let G be a smooth aﬃne group scheme over D. Assume that the connected component
G0 is reductive and the component group G/G0 is ﬁnite over D. If char(k) = 0 and
char(k0) = p > 0, assume further that the absolute ramiﬁcation index of D is 1. Then

rdk0(Gk0) ⩽ max{rdk(Gk), 1}.

Recall that the absolute ramiﬁcation index of D is deﬁned as ν(p), where ν : k∗ → Z is
the discrete valuation.

Proof. First observe that we may replace D by its completion ̂D. Indeed, denote the
fraction ﬁeld of ̂D by ̂k. Then k ⊂ ̂k, and the residue ﬁeld k0 remains unchanged.
By Proposition 8.3(a), rd̂k(Ĝk) ⩽ rdk(Gk). Thus it suﬃces to show that rdk0(Gk0) ⩽
max{rd̂k(Ĝk), 1}.
After replacing D by ̂D, we may assume that D is complete. Under the assumptions
of the proposition, D = W (k0); see [32, Sections II.4-5]. Here for any ﬁeld K0 containing
k0 we deﬁne W (K0) to be the ring of power series K0[[t]] if char(k) = char(k0) and the
ring of Witt vectors with coeﬃcients in K0 if char(k) = 0 and char(k0) = p > 0; see [32,
Section II.6].
Now let K0 be a ﬁeld containing k0 and π : T0 → Spec(K0) be a Gk0-torsor. Set
R = W (K0). Recall that R is a complete local ring relative to a valuation ν : R → Z
with residue ﬁeld K0, extending the valuation on D. By [19, XXIV, Proposition 8.1], the
natural map H 1(R, G) → H 1(K0, G) is bijective. In particular, there exists a GR-torsor
πR : T → Spec(R) which restricts to π over the closed point Spec(K0) → Spec(R). Let K
be the ﬁeld of fractions of R = W (K0) and πK : TK → Spec(K) be the restriction of π to
the generic point of Spec(R). Our goal is to show that

(15) rdl(TK0) ⩽ max{rdk(TK), 1}.

This inequality tells us that rdk0(TK0) ⩽ max{rdk(Gk), 1}. Taking the maximum of the
left hand side over all K0 ∈ Fieldsk0 and all Gk0-torsors T0 → Spec(K0), we arrive at
rdk0(Gk0) ⩽ max{rdk(Gk), 1}, as desired.
It remains to prove the inequality (15). By the deﬁnition of d = rdk(TK) there exists
a ﬁnite ﬁeld extension L/K such that L splits TK and levk(L/K) ⩽ d. The valuation ν
extends from K and to L. Once again, by abuse of notation I will continue to denote this

30 ZINOVY REICHSTEIN

extended valuation by ν : L
∗ → Z. I will also denote the valuation ring for this valuation
by S and the residue ﬁeld by L0. Now consider the diagram of natural morphisms

TS

  
 // TL

H 1(S, GS)  • //

  
 H 1(L, GL)

TL0 H 1(L0, GL0)

The horizontal map is injective by [29, Lemma 3.3(b)]. 4 Note that the assumptions of
Theorem 1.3, that G0 is reductive and G/G0 is ﬁnite over D (and hence, over R and over
S), are used to ensure that [29, Lemma 3.3(b)] applies.
Since TK splits over Spec(L), the injectivity of the horizontal map in the above diagram
tells us that that T splits over Spec(S). Consequently, TK0 splits over Spec(L0). This
tells us that
 rdk(TK0) ⩽ levk0(L0/K0) ⩽ max{levk(L/K), 1} ⩽ max{d, 1},

where the middle inequality is given by Proposition 5.1. This completes the proof of the
inequality (15) and thus of Proposition 13.1. □

We now proceed with the proof of Theorem 1.3. If char(k) = char(k0), then by The-
orem 1.2, edk(Gk) = edF (GF ) = edk0(Gk0), where F is the prime ﬁeld. Thus we may
assume without loss of generality that char(k) = 0 and char(k0) = p > 0. Moreover, we
are free to replace k by any ﬁeld of characteristic 0 and k0 by any ﬁeld of characteristic p.
If rdk(Gk) ⩾ 1 for some (and thus every) ﬁeld of characteristic 0, then the desired
inequality rdk0(Gk0) ⩽ rdk(Gk) readily follows from Proposition 13.1, applied to the group
scheme GD, where D = W (k0) = the ring of Witt vectors with coeﬃcients in k0.
The case, where rdk(Gk) = 0 needs to be treated separately (as in the previous section).
One again, we are free to choose k to be any ﬁeld of characteristic 0 and k0 to be any ﬁeld
of characteristic p. In particular, we may assume that both k and k0 are algebraically
closed. Now by Lemma 10.7(a), it suﬃces to show that if Gk is special, then Gk0 is special.
Indeed, if Gk is special, then Gk is connected [31, Theorem 4.1]. Hence, G and Gk0
are also connected. On the other hand, since k and k0 are algebraically closed, we may
appeal to the classiﬁcation of special groups over an algebraically closed ﬁeld due to
Grothendieck [21, Theorem 3]. According to this classiﬁcation, Gk is special if and only if
its derived subgroup is a direct product G1 ×. . .×Gr, where each Gi is a simply connected
simple group of type A or C. This property is encoded into the root datum, which is the
same for Gk, G, and Gk0; see [19, XXV, Section 1]. (Note that this is the only step in the
proof of Theorem 1.3 which uses the assumption that G0 is split.) We conclude that Gk
is special if and only if Gk0 is special. This ﬁnishes the proof of Theorem 1.3. □

4[29, Lemma 3.3(b)] is a variant of the Grothendieck-Serre Conjecture over a Henselian discrete valu-
ation ring. A theorem of Nisnevich, establishing the Grothendick-Serre Conjecture in this context, is a
key ingredient in our proof of both Proposition 13.1 and Theorem 1.3.

HILBERT’S 13TH PROBLEM FOR ALGEBRAIC GROUPS 31

14. Upper bounds on the resolvent degree of a group

Consider an action of a linear algebraic group G on an algebraic variety X (not nec-
essarily connected) deﬁned over a ﬁeld k. We will say that this action is generically free
if there exists a dense G-invariant open subset U ⊂ X such that the scheme-theoretic
stabilizer Gu is trivial for every geometric point u ∈ U. In this section we will prove the
following.

Proposition 14.1. Let G be a closed subgroup of PGLn deﬁned over k. Suppose there
exists a G-invariant closed subvariety X of Pn of degree a and dimension b.
(a) (cf. [45, Proposition 4.11]) If the G-action on X is generically free, then

rdk(G) ⩽ max{b − dim(G), rdk(Sa), 1},

where Sa denotes the symmetric group on a letters.
(b) Suppose char(k) ̸= 2 and there exists a G-invariant quadric hypersurface Q ⊂ P(V )
of rank r such that dim(Q ∩ X) = b − 1. Assume further the G-action on Q ∩ X is

generically free, and b ⩾ ⌊r + 1
2 ⌋. Then

rdk(G) ⩽ max{b − 1 − dim(G), rdk(Sa), 1}.

Remark 14.2. (1) Note that rdk(Sa) ⩾ 1 if a ⩾ 2. Thus for a ⩾ 2, the conclusions of
parts (a) and (b) simplify to rdk(G) ⩽ max{b − dim(G), rdk(Sa)} and rdk(G) ⩽ max{b −
dim(G) − 1, rdk(Sa)}, respectively.
(2) By the rank r of Q we mean the rank of some (and thus any) quadratic form
deﬁning Q. The maximal value of r is n + 1; it is attained when Q is non-singular. In

particular, the condition that b ⩾ ⌊r + 1
2 ⌋ is automatically satisﬁed if b ⩾ ⌊n + 2
2 ⌋. If X
is a hypersurface, i.e., b = n − 1, then it is automatically satisﬁed whenever n ⩾ 3.
(3) Note that by Theorem 1.2, rdk(Sa) = rdC(Sa) for any ﬁeld k of characteristic 0 and
rdk(Sa) ⩽ rdC(Sa) for any ﬁeld k of positive characteristic. Thus rdk(Sa) can be replaced
by rdC(Sa) in the statement of the proposition.

Example 14.3. (1) If we take X = Pn in part (a), we obtain rdk(G) ⩽ n − dim(G).
In particular, if an abstract ﬁnite group G has an n-dimensional faithful projective rep-
resentation over k, then rdk(G) ⩽ n. (The G-action on Pn is automatically generically
free in this case.) In particular, since the alternating group A5 acts faithfully on P1,
we obtain rdk(A5) ⩽ 1. Also, since A6 and A7 have complex projective representations
of dimension 2 and 3, respectively, we deduce classical upper bounds rdk(A6) ⩽ 2 and
rdk(A7) ⩽ 3; see [14, Section 3 and 4], [16, Theorem 5.6]. Note also that rdk(Sn) = rdk(An)
for any n ⩾ 3; this follows from Proposition 10.8(a) applied to the exact sequence
1 → An → Sn → Z/2Z → 1.
(2) More generally, the classical upper bound rdk(Sn) ⩽ n − 4 for any n ⩾ 5 can be
deduced from Proposition 14.1(b) as follows. Consider the (n − 1)-dimensional subspace
of kn given by x1 + x2 + . . . + xn = 0. The group Sn acts on this space by permuting the
coordinates. This yields an embedding Sn ֒→ PGLn−2. The desired inequality now follows
from Proposition 14.1(b), where we take X to be the cubic hypersurface given by s3 = 0

32 ZINOVY REICHSTEIN

and Q to be the quadric s2 = 0; see Remark 14.2(2). Here si denotes the ith elementary
symmetric polynomial.

None of the upper bounds in Example 14.3 are new; the point here is that they can all
be deduced from Proposition 14.1 in a uniform way. The remainder of this section will
be devoted to proving Proposition 14.1. We begin with two lemmas.

Lemma 14.4. Let k be a ﬁeld, K ∈ Fieldsk be closed at level d, and ∅ ̸= X ⊂ Pn be a
projective variety of degree ⩽ a deﬁned over K. If d ⩾ max{rdk(Sa), 1}, then
(a) K-points are dense in X.
(b) Assume further that Q ⊂ Pn be a quadric hypersurface of rank r deﬁned over K

and dim(X) ⩾ ⌊r + 1
2 ⌋. Then K-points are dense in X ∩ Q.

Proof. (a) We argue by induction on n. The base case, where n = 1, reduces to the
assertion that every non-constant homogeneous polynomial f (x, y) ∈ K[x, y] of degree
⩽ a splits into a product of linear factors over K. This assertion follows from Example 8.4.
(Recall that rdk(Sn) = rdk(´Etn)); see Example 10.2.)
For the induction step, assume n ⩾ 2 and consider the incidence variety

I = {(p, L) ∈ X × ̂Pn | p ∈ L}

π1

uu❧❧❧❧❧❧❧❧❧❧❧❧❧❧❧❧❧❧ π2
 ))❘❘❘❘❘❘❘❘❘❘❘❘❘❘❘❘❘❘

X ̂Pn,

where ̂Pn is the dual projective space parametrizing hyperplanes in Pn and π1, π2 are
projections to the ﬁrst and second factor, respectively. Clearly π1 is surjective; there is a
hyperplane in Pn through every point of X. By the induction assumption, K-points are
dense π−1
2 (L) for every L ∈ ̂Pn(K). Since K-points are dense in ̂Pn, we conclude that
K-points are dense in I. Projecting them to X via π1, we see that K-points are dense in
X, as desired.
(b) Since K is closed at level d ⩾ 1, every quadratic form splits over K. That is, Q is the
zero locus of a split quadratic form q(x0, . . . , xn) of rank r over K. Let m = ⌊ r
2 ⌋+(n+1−r)

and Grq(m, n + 1) be the isotropic Grassmannian of maximal isotropic subspaces of q.
In other words, Grq(m, n) parametrizes linear subspaces of (projective) dimension m − 1
which are contained in Q. Since q is split, K-points are dense in Grq(m, n). Consider the
incidence variety
 I = {(p, L) ∈ (Q ∩ X) × Grq(m, n) | p ∈ L}

π1

ss❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤ π2
 ++❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲

Q ∩ X Grq(m, n).

Note that there exists a maximal isotropic subspace through every point of Q; in partic-

ular, π1 is surjective. On the other hand, our assumption that dim(X) ⩾ ⌊r + 1
2 ⌋ ensures

that dim(L) + dim(X) = (m − 1) + dim(X) ⩾ n and thus L ∩ X ̸= ∅ every L ∈ Grq(m, n).

HILBERT’S 13TH PROBLEM FOR ALGEBRAIC GROUPS 33

This tells us that π2 is surjective. The ﬁber π−1
1 (L) = L ∩ X of a K-rational point L
of Grq(m, n) is a closed subvariety of degree d in L ≃ Pm−1 deﬁned over K. By part
(a), K-points are dense in every such ﬁber. Since K-points are dense in Grq(m, n), we
conclude that K-points are dense in I. Projecting them to Q ∩ X via π1, we see that
K-points are dense in Q ∩ X as well. □

Lemma 14.5. Consider a generically free action of an algebraic group G on an algebraic
variety X deﬁned over a ﬁeld k. Supposed that K-points are dense in the twisted variety

T X for every ﬁeld K containing k, closed at level d and every G-torsor T → Spec(K).
Then rdk(G) ⩽ max{d, dim(X) − dim(G)}.

Proof. Let K/k be a ﬁeld closed at level d and T → Spec(K) be a G-torsor. By Proposi-
tion 8.1(c) it suﬃces to show that

(16) rdk(T ) ⩽ dim(X) − dim(G).

After replacing X by a suitable G-invariant union of its irreducible components, we may
assume that G transitively permutes the irreducible components of X. In this case there
exists a G-invariant dense open subvariety U ⊂ X, which is the total space of a G-torsor
U → B. By our assumption T U has a K-point. Equivalently, there exists a G-equivariant
map T → U deﬁned over k; see, e.g., [15, Proof of Theorem 1.1(a) on p. 508]. This implies
that edk(T ) ⩽ dim(B) = dim(X) − dim(G). The desired inequality (16) now follows from
the inequality rdk(T ) ⩽ edk(T ) of Remark 10.4. □

Proof of Proposition 14.1. (a) Set d = max{rdk(Sa), 1}. Suppose a ﬁeld K ∈ Fieldsk is
closed at level d and T → Spec(K) is a G-torsor. Since d ⩾ 1, K is solvably closed; see
Corollary 6.5. By Lemma 14.5 it suﬃces to show that K-points are dense in T X.
Note that the G-equivariant closed immersion X ֒→ P(V ) induces a natural closed
immersion T X ֒→ T P(V ) of K-varieties. Here T P(V ) is a Brauer-Severi variety over K.
Since K is solvably closed, every Brauer-Severi variety over K is split. Thus T X is a
closed subvariety of P(V )K. The degree of T X in P(V )K is a, same as the degree of X
in P(V ). (To see this, pass to K.) By Lemma 14.4(a), K-points are dense in T X. The
desired inequality, rd(G) ⩽ {d, dim(X) − dim(G)}, now follows from Lemma 14.5.
(b) The argument here is the same as in part (a), with Lemma 14.4(b) used to show
that K-points are dense in T (Q ∩ X). □

15. Upper bounds on the resolvent degree of some reflection groups

The purpose of this section is to prove the following.

Proposition 15.1. Let W be Weyl group of the simple Lie algebra (or equivalently, a
simple algebraic group) of type Ei. Here i = 6, 7 or 8. Let k be an arbitrary ﬁeld. Then
rdk(W ) ⩽ i − 3.

The inequality rdk(W ) ⩽ 5, where W is the Weyl group of E8, will play an important
role in the proof of Theorem 1.1. We will only supply a proof of Proposition 15.1 in this
case (for i = 8). The other two inequalities (where i = 6 and 7) will not be used in
this paper. They are proved by a minor modiﬁcation of the same argument; we leave the
details as an exercise for the reader.

34 ZINOVY REICHSTEIN

Note that by Theorem 1.2, rdC(Wi) = rdQ(Wi) = rdk(Wi) for any ﬁeld k of character-
istic 0. Moreover, by Theorem 1.3, rdk(Wi) ⩽ rdC(Wi) for any ﬁeld k of characteristic p.
Thus the purpose of proving Theorem 15.1, we may assume that k = C. This places us
into the setting of Springer’s classic paper on complex reﬂection groups [37].
We now proceed with the proof of Proposition 15.1 for i = 8 and k = C. Consider the
natural representation W ֒→ GL(V ) = GL8 where V is a Cartan subalgebra of E8. The
kernel Z of this representation is the center of W ; it is a cyclic group of order 2. We will
denote the non-trivial element of Z by z and the image of W in PGL8 by W = W/Z.
Recall that the ring of invariants C[V ]W is a polynomial ring over C in 8 variables. The
generators f2, f8, f12, f14, f18, f20, f24 and f30 are called basic invariants; each fi is a
homogeneous G-invariant polynomial of degree i. These basic invariants are not unique
but their degrees are. That is, if C[V ]G is generated by 8 homogeneous elements g1, . . . , g8,
then the degrees of g1, . . . , g8 are

(17) 2, 8, 12, 14, 18, 20, 24, 30.

These integers are called the fundamental degrees of W .
Our strategy is to apply Proposition 14.1(b) with G = W , X ⊂ P(V ) = P7 the
hypersurface f8 = 0 and Q ⊂ P7 the quadric hypersurface f2 = 0. Denote the aﬃne cones
of Q and X by Q
aﬀ and X aﬀ, respectively.

Lemma 15.2. (a) W transitively permutes the irreducible components of Q ∩ X (or
equivalently, the irreducible components of Q
aﬀ ∩ X aﬀ).
(b) Each irreducible component of Q ∩ X is of dimension 5.

Lemma 15.3. The action of W on Q ∩ X is generically free.

Assume for a moment that we have established these two lemmas. Then Proposition 14.1(b)
tells us that
 rdC(W ) ⩽ max{dim(X) − 1, rdC(S8)} = max{5, 4} = 5.

Here I used the fact that rdC(S8) ⩽ 4; see [16, Theorem 5.6] or Example 14.3(b). Applying
Proposition 10.8(a) to the exact sequence 1 → Z → W → W → 1, we conclude that

rdC(W ) ⩽ max{rdC(W ), rdC(Z)} ⩽ max{5, 1} = 5,

as desired. It thus remains to prove Lemmas 15.2 and 15.3.

Proof of Lemma 15.2. The natural inclusion C[f2, f8, . . . , f30] = C[V ]W ֒→ C[V ] induces
the categorical quotient map π : V → A8 given by π : v → (f2(v), f8(v), . . . , f30(v)). Note
that π is a ﬁnite morphism, and the ﬁbers of C-points of A8 are precisely the W -orbits
in V . By deﬁnition, Q
aﬀ and X aﬀ the preimages of coordinate hyperplanes H1 and H2 in
A8 given by x1 = 0 and x2 = 0, respectively. Both (a) and (b) now follows from the fact
that H1 ∩ H2 ≃ A6 is irreducible of dimension 6. □

Proof of Lemma 15.3. Assume the contrary: the W -action on Q ∩ X is not generically
free. This means that Q
aﬀ ∩ X aﬀ is covered by the union of eigenspaces V (g, ζ), where g
ranges over W \ Z and ζ ranges over the roots of unity in C. Here

V (g, ζ) = {v ∈ V | g(v) = ζv}

HILBERT’S 13TH PROBLEM FOR ALGEBRAIC GROUPS 35

stands for the ζ-eigenspace of g, as in [37].
If ζ is a primitive root of unity of degree d, then dim(V (g, ζ)) ⩽ a(d), where a(d) is the
number of fundamental degrees (17) divisible by d; see [37, Theorem 3.4]. By inspection
we see that a(d) ⩽ 4 for any d ⩾ 3, with equality for d = 3, 4, 6. Thus the union of
eigenspaces g∈W \Z⋃

deg(ζ)⩾3 V (g, ζ)

is at most 4-dimensional. Since every irreducible component of Q
aﬀ ∩ X aﬀ is of dimension
6 (see Lemma 15.2(b)), Q
aﬀ ∩ X aﬀ is, in fact, covered by the union of V (g, ±1) = V g, as
g ranges over W \ Z. Since V (g, −1) = V (zg, 1) for each g, we conclude that

V non−free = ∪g∈W \Z V (g, 1)

covers one of the irreducible components of Q
aﬀ ∩ X aﬀ. Clearly V non−free is W -invariant.
By Lemma 15.2(a), if it covers one irreducible component of Q
aﬀ ∩ X aﬀ, it covers all of
them. In other words, Q
aﬀ ∩ X aﬀ ⊂ ⋃

1̸=g∈W V (g, 1).

Thus in order to produce a contradiction, it suﬃces to exhibit one point v ∈ V such that
(i) StabW (v) = {1} or equivalently, v ̸∈ V (g, 1) for any 1 ̸= g ∈ W , and
(ii) v ∈ Q
aﬀ ∩ X aﬀ of equivalently, f2(v) = f8(v) = 0.
By [37, p. 177, Table 3], W has a regular element of order 3. This means that V (g, ζ3)
contains a regular vector v, where ζ3 is a primitive cube root of unity. Recall that a vector
in V is called regular if it is not contained in any reﬂecting hyperplane, and that for any
regular vector v, the stabilizer StabW (v) = {1}; see [37, Proposition 4.1]. Moreover, if fd
is one of the fundamental invariants, then

fd(v) = fd(gv) = fd(ζ3v) = ζ d
3 fd(v).

In particular, fd(v) = 0 when d = 2 and 8. Thus the regular vector v satisﬁes conditions
(i) and (ii). This completes the proof of Lemma 15.3 and thus of Proposition 15.1 for
i = 8. □

16. Proof of Theorem 1.1

Once again, by Theorem 1.2, we may replace k by its algebraic closure and thus assume
without loss of generality that k is algebraically closed.
Reduction to the case, where G is smooth. Recall that rdk(G) ⩽ max{rdk(Gred), 1}
by Proposition 11.2(a). Thus in order to prove Theorem 1.1 for G, it suﬃces to prove it
for Gred.
Reduction to the case, where G is aﬃne. We may now assume that G is smooth.
By Chevalley’s structure theorem [12, 13] there exists a unique connected smooth normal
aﬃne k-subgroup Gaﬀ of G such that the quotient G/Gaﬀ is an abelian variety. By
Proposition 11.3, rdk(G/Gaﬀ) ⩽ 1. Applying Proposition 10.8(a) to the exact sequence
1 → Gaﬀ → G → G/Gaﬀ → 1, we obtain rdk(G) ⩽ max{rdk(Gaﬀ), 1}. Thus in order to
prove Theorem 1.1 for G, it suﬃces to prove it for Gaﬀ.

36 ZINOVY REICHSTEIN

Reduction to the case, where G is semisimple. We may now assume that G
is aﬃne. Let Rad(G) be the radical of G, i.e., the largest connected solvable normal
subgroup of G. Denote the quotient (semisimple) group by Gss and consider the natural
exact sequence 1 → Rad(G) → G → Gss → 1. By Lemma 10.7(b), rdk(Rad(G)) =
0. Proposition 10.8(a) now tells us that rdk(G) ⩽ rdk(Gss). Thus in order to prove
Theorem 1.1 for G, it suﬃces to prove it for Gss.
Reduction to the case, where G is almost simple. We will now assume that G
is semisimple. Then G isogenous to the direct product ̃G = G1 × . . . × Gr of its minimal
connected normal subgroups. That is, there exists a central exact sequence

1 → A → ̃G → G → 1,

where A is a ﬁnite subgroup of a maximal torus of G1; see [38, Section 9.6.1]. Since we are
assuming that k is algebraically closed, this tells us that A is a ﬁnite diagonalizable group.
Hence, rdk(A) ⩽ 1 by Proposition 10.8(c). The minimal connected normal subgroups
G1, . . . , Gr are (almost) simple; see [23, Section 27.5]. Proposition 10.8(d) now tells us
that it suﬃces to prove Theorem 1.1 for ̃G = G1 × . . . × Gr. Applying Proposition 10.8(b)
recursively, we see that

rdk(G1 × . . . × Gr) = max { rdk(G1), . . . , rdk(Gr) }.

Thus in order to prove Theorem 1.1 for G, it suﬃces to prove it for each (almost) simple
group Gi.
From now on we will assume that G is (almost) simple. To complete the proof of
Theorem 1.1, it remains to establish the following.

Proposition 16.1. Let k be an algebraically closed ﬁeld and G an almost simple group
deﬁned over k. Then (a) rdk(G) ⩽ 5 if G is of type E8 and (b) rdk(G) ⩽ 1 if G is of any
other type.

Proof. (a) Let G be a simple group of type E8 and let W8 be the Weyl group of G. Then

rdk(G) ⩽ rdk(W8) ⩽ 5,

where the ﬁrst inequality is given by Corollary 10.9, and the second by Proposition 15.1.
(b) Tits [41, Section 2] showed that if G is a simple group of any type other than E8,
then G has no non-trivial torsors over any ﬁeld K, closed under taking radicals. (Note
that [41] is reprinted in [42].) In particular, there are no non-trivial G-torsors over any
ﬁeld K closed at level 1. By Proposition 8.1(b) this implies that rdk(G) ⩽ 1, as claimed.
For the sake of completeness we will give a short direct proof of part (b), using the
terminology of this paper. We begin with two preliminary observations. First, recall
that every almost simple algebraic group is deﬁned over Z. Using Theorems 1.2 and 1.3,
we may assume without loss of generality that k = C is the ﬁeld of complex numbers.
This assumption will allow us to avoid some of the subtle points of the arguments in [41,
Section 2] which only come up in prime characteristic.
The second observation is that if G1 and G2 are almost simple groups of the same type,
then they are isogenous and hence, by Proposition 10.8(d), rdC(G1) ⩽ max {rdC(G2), 1}
and rdC(G2) ⩽ max {rdC(G1), 1}. Consequently, Proposition 16.1(b) holds for G1 if and

HILBERT’S 13TH PROBLEM FOR ALGEBRAIC GROUPS 37

only if it holds for G2. In other words, it suﬃces to prove that rdC(G) ⩽ 1 for one almost
simple group G of each type (other than E8).
G is of type Ar or Cr. Here we can take G to be G = SLr+1 and G = Sp2r, respectively.
By Lemma 10.7(c), in both cases, rdk(G) = 0.
If G is of type Br or Dr. Here we take G to the the special orthogonal group G = SOn,
which is of type Br if n = 2r + 1 and of type Dr if n = 2r. By [24, (29.29)], H 1(K, G)
can be represented by n-dimensional quadratic forms q of discriminant 1 over K. In a
suitable basis, q(x1, . . . , xn) = a1x
2 + . . . + anx
2
n for some a1, . . . , an. Thus q splits over
L = K(√a1, . . . , √an). Clearly rdC(L/K) ⩽ 1, and thus rdC(G) ⩽ 1, as claimed.

G is of type G2 and F4. In both cases the only primes dividing |W | are 2 and 3.
By Burnside’s Theorem, W is solvable 5. Thus rdk(G) ⩽ rdk(W ) ⩽ 1, where the ﬁrst
inequality follows from Corollary 10.9 and the second from Example 10.6.
G is a simply connected group of type E6. By [17, Example 9.12], G has a subgroup
S isomorphic to F4 × µ3 such that the map H 1(K, S) → H 1(K, G) is surjective; see [17,
Section 23]. Here F4 denotes the simply connected group of type F4. By Lemma 7.9(c),
rdC(S) = rdC H 1(∗, S) ⩾ rdC H 1(∗, G) = rdC(G). Since we know that rdC(F4) ⩽ 1,

rdC(G) ⩽ rdC(S) = rdC(F4 × µ3) = max{rdC(F4), rdC(µ3)} = 1.

G is a simply connected group of type E7. By [17, Example 12.3], G has a
subgroup ̃S isomorphic to E6 ⋊ µ4 such that the map H 1(K, ̃S) → H 1(K, G) is surjective;
see [17, Section 23]. Here E6 denotes the simply connected group of type E6. Once again,
by Lemma 7.9(c), rdC( ̃S) ⩾ rdC(G). Since we know that rdC(E6) ⩽ 1, we conclude that
rdC(G) ⩽ rdC( ̃S) = rdC(E6 ⋊ µ4) = max{rdC(E6), rdC(µ4)} = 1.
This completes the proof of Proposition 16.1 and thus of Theorem 1.1. □

Remark 16.2. For simply connected groups G of type G2, F4, E6 and E7, the inequality
rdC(G) ⩽ 1 of Proposition 16.1(b) can also be deduced from a theorem of Garibaldi which
asserts that for these groups the Rost invariant H 1(∗, G) → H 3(∗, Z/nGZ(2)) has trivial
kernel; see [17, Theorem 0.5] or [8].

17. Can the inequality of Theorem 1.1 be strengthened?

Recall that Conjecture 1.4 asserts that the inequality rdk(G) ⩽ 5 of Theorem 1.1 can
be strengthened to rdk(G) ⩽ 1. In this ﬁnal section we will show that this conjecture
follows from a positive answer to a long-standing open question of Serre [33, Question 2]
stated below.

Question 17.1. Let K be a ﬁeld, H be a smooth algebraic group over K, and T →
Spec(K) be a H-torsor. If Ki/K are ﬁnite extensions of K of relatively prime degrees,
i.e., gcd([Ki : K]) = 1, and each Ki splits T , then T is split over K.

For a detailed discussion of Question 17.1, we refer the reader to [44].

5One can also see check this directly, without appealing to Burnside’s theorem.

38 ZINOVY REICHSTEIN

Proposition 17.2. Assume that Question 17.1 has a positive answer in the following
special situation: K is a solvably closed ﬁeld containing C and H = (E8)K is the split
simple group of type E8 over K. Then rdk(G) ⩽ 1 for every ﬁeld k and every connected
algebraic group G over k.

Proof. It suﬃces to show that, under the assumption of the proposition, the inequality
rdk(E8) ⩽ 5 of Proposition 16.1(a) can be strengthened to rdk(E8) ⩽ 1. If we can do this,
then the argument of Section 16 will go through unchanged to show that rd(G) ⩽ 1 for
every ﬁeld k and every connected algebraic group G over k.
By Theorems 1.2 and 1.3 we may further assume that k = C, as we did in the proof
of Proposition 16.1 in the previous section. By Proposition 8.1(b) it suﬃces to show
that every E8-torsor T → Spec(K) is split for every ﬁeld K ∈ FieldsC, closed at level
1 (over C). In fact, we will show that this is the case whenever K is solvably closed;
cf. Corollary 6.5. By a theorem of Tits [40], T is split by a ﬁnite ﬁeld extension K⩾7/K
such that

(18) the only primes dividing [K⩾7 : K] are 2, 3 and 5;

see also [44]. 6

Now observe that since K is solvably closed, the Norm Residue Isomorphism Theorem
tells us that H d(K, µn) = 1 for every d, n ⩾ 1; cf. Remark 7.12. In particular, the class
of T lies in the kernel of the Rost Invariant R : H 1(K, E8) → H 3(K, µ60). Theorems of
Chernousov now tell us that

T is split by a ﬁnite extension K3/K such that 3 ̸ | [K3 : K];

and T is split by a ﬁnite extension K5/K such that 5 ̸ | [K5 : K];

see [9, 11]. Finally, T also lies in the kernel of the Semenov invariant

H 1(∗, E8)0 → H 3(∗, µ2),

where H 1(∗, E8)0 denote the kernel of the mod 4 Rost invariant, 15R. Consequently,
by [30, Theorem 8.7]

T is split by a ﬁnite extension K2/K such that 2 ̸ | [K2 : K].

In summary, T can be split by ﬁnite extensions K2, K3, K5 and K⩾7 of K whose degrees
are relatively prime. The assumption of the proposition now tells us that T is split over
K, as desired. □

Remark 17.3. Note that the Semenov invariant is only deﬁned in characteristic 0. In
prime characteristic our proof of Proposition 17.2 relies on Theorem 1.3.

Acknowledgement

The author is grateful to Jesse Wolfson for helpful detailed comments on an earlier
version of this paper.

6Note that this step is valid for every K; we do not use the assumption that K is solvably closed here.

HILBERT’S 13TH PROBLEM FOR ALGEBRAIC GROUPS 39

References

[1] G. Berhuy and G. Favi. Essential dimension: a functorial point of view (after A. Merkurjev). Doc.
Math. 2003;8(106):279-330., 2003.
[2] R. Brauer. On the resolvent problem. Ann. Mat. Pura Appl. (4), 102:45–55, 1975.
[3] M. Brion. On extensions of algebraic groups with ﬁnite quotient. Paciﬁc J. Math., 279(1-2):135–153,
2015.
[4] P. Brosnan, Z. Reichstein, and A. Vistoli. Essential dimension and algebraic stacks. arXiv preprint
math/0701903, 2007.
[5] P. Brosnan, Z. Reichstein, and A. Vistoli. Essential dimension in mixed characteristic. Doc. Math.,
23:1587–1600, 2018.
[6] F. E. Browder, editor. Mathematical developments arising from Hilbert problems, Proceedings of
Symposia in Pure Mathematics, Vol. XXVIII. American Mathematical Society, Providence, R. I.,
1976.
[7] J. Buhler and Z. Reichstein. On the essential dimension of a ﬁnite group. Compositio Mathematica,
106(2):159–179, 1997.
[8] V. Chernousov. The kernel of the Rost invariant, Serre’s conjecture II and the Hasse principle for
quasi-split groups 3,6D4, E6, E7. Math. Ann., 326(2):297–330, 2003.
[9] V. Chernousov. On the kernel of the Rost invariant for E8 modulo 3. In Quadratic forms, linear
algebraic groups, and cohomology, volume 18 of Dev. Math., pages 199–214. Springer, New York,
2010.
[10] V. Chernousov, P. Gille, and Z. Reichstein. Reduction of structure for torsors over semilocal rings.
Manuscripta Math., 126(4):465–480, 2008.
[11] V. I. Chernousov. A remark on the (mod 5)-invariant of Serre for groups of type E8. Mat. Zametki,
56(1):116–121, 157, 1994.
[12] C. Chevalley. Une d´emonstration d’un th´eor`eme sur les groupes alg´ebriques. J. Math. Pures Appl.
(9), 39:307–317, 1960.
[13] B. Conrad. A modern proof of Chevalley’s theorem on algebraic groups. J. Ramanujan Math. Soc.,
17:1–18, 01 2002.
[14] J. Dixmier. Histoire du 13e probl`eme de Hilbert. In Analyse diophantienne et g´eom´etrie alg´ebrique,
volume 3 of Cahiers S´em. Hist. Math. S´er. 2, pages 85–94. Univ. Paris VI, Paris, 1993.
[15] A Duncan and Z. Reichstein. Versality of algebraic group actions and rational points on twisted
varieties. J. Algebraic Geom., 24(3):499–530, 2015. With an appendix containing a letter from J.-P.
Serre.
[16] B. Farb and J. Wolfson. Resolvent degree, Hilbert’s 13th problem and geometry. Enseign. Math.,
65(3-4):303–376, 2019.
[17] S. Garibaldi. Cohomological invariants: exceptional groups and spin groups. Mem. Amer. Math.
Soc., 200(937):xii+81, 2009. With an appendix by Detlev W. Hoﬀmann.
[18] Ph. Gille and P. Polo, editors. Sch´emas en groupes (SGA 3). Tome I. Propri´et´es g´en´erales des
sch´emas en groupes, volume 7 of Documents Math´ematiques (Paris). Soci´et´e Math´ematique de
France, Paris, 2011. S´eminaire de G´eom´etrie Alg´ebrique du Bois Marie 1962–64. A seminar di-
rected by M. Demazure and A. Grothendieck with the collaboration of M. Artin, J.-E. Bertin, P.
Gabriel, M. Raynaud and J-P. Serre. Revised and annotated edition of the 1970 French original.
[19] Ph. Gille and P. Polo, editors. Sch´emas en groupes (SGA 3). Tome III. Structure des sch´emas en
groupes r´eductifs, volume 8 of Documents Math´ematiques (Paris). Soci´et´e Math´ematique de France,
Paris, 2011. S´eminaire de G´eom´etrie Alg´ebrique du Bois Marie 1962–64. A seminar directed by M.
Demazure and A. Grothendieck with the collaboration of M. Artin, J.-E. Bertin, P. Gabriel, M.
Raynaud and J-P. Serre. Revised and annotated edition of the 1970 French original.
[20] Philippe Gille and Tam´as Szamuely. Central simple algebras and Galois cohomology, volume 165 of
Cambridge Studies in Advanced Mathematics. Cambridge University Press, Cambridge, 2017.

40 ZINOVY REICHSTEIN

[21] A. Grothendieck. Torsion homologique et sections rationnelles, expos´e 5. In S´eminaire C. Chevalley;
2e ann´ee. Anneaux de Chow et applications, pages iii+134 pp. Secr´etariat math´ematique, 11 rue
Pierre Curie, Paris, 1958.
[22] C. Heberle and A. J. Sutherland. Upper bounds on resolvent degree via Sylvester’s obliteration
algorithm. arXiv:2110.08670, 2021.
[23] J. E. Humphreys. Linear algebraic groups. Graduate Texts in Mathematics, No. 21. Springer-Verlag,
New York-Heidelberg, 1975.
[24] M.-A. Knus, A. S. Merkurjev, M. Rost, and J.-P. Tignol. The book of involutions, volume 44 of Ameri-
can Mathematical Society Colloquium Publications. American Mathematical Society, Providence, RI,
1998. With a preface in French by J. Tits.
[25] A. S.. Merkurjev. Rost invariants of simply connected algebraic groups. In Cohomological invariants
in Galois cohomology, volume 28 of Univ. Lecture Ser., pages 101–158. Amer. Math. Soc., Providence,
RI, 2003. With a section by Skip Garibaldi.
[26] A. S. Merkurjev. Essential dimension: a survey. Transform. Groups, 18(2):415–481, 2013.
[27] Z. Reichstein. Essential dimension. In Proceedings of the International Congress of Mathematicians.
Volume II, pages 162–188. Hindustan Book Agency, New Delhi, 2010.
[28] Z. Reichstein. From Hilbert’s 13th problem to essential dimension and back. Eur. Math. Soc. Mag-
azine., 122:4–15, December 2021.
[29] Z. Reichstein and F. Scavia. The behavior of essential dimension under specialization.
arXiv:2112.13298, 2021.
[30] N. Semenov. Motivic construction of cohomological invariants. Comment. Math. Helv., 91(1):163–
202, 2016.
[31] J.-P. Serre. Espaces ﬁbr´es alg´ebriques, expos´e 1. In S´eminaire C. Chevalley; 2e ann´ee. Anneaux de
Chow et applications, pages iii+134 pp. Secr´etariat math´ematique, 11 rue Pierre Curie, Paris, 1958.
[32] J.-P. Serre. Local ﬁelds, volume 67 of Graduate Texts in Mathematics. Springer-Verlag, New York-
Berlin, 1979. Translated from the French by Marvin Jay Greenberg.
[33] J.-P. Serre. Cohomologie galoisienne: progr`es et probl`emes. Ast´erisque, Exp. No. 783, 4(227):229–
257, 1995. S´eminaire Bourbaki, Vol. 1993/94.
[34] J.-P. Serre. Galois cohomology. Springer-Verlag, Berlin, 1997. Translated from the French by Patrick
Ion and revised by the author.
[35] J.-P. Serre. Expos´es de s´eminaires (1950-1999), volume 1 of Documents Math´ematiques (Paris).
Soci´et´e Math´ematique de France, Paris, 2001.
[36] J. H. Silverman. The arithmetic of elliptic curves, volume 106 of Graduate Texts in Mathematics.
Springer, Dordrecht, second edition, 2009.
[37] T. A. Springer. Regular elements of ﬁnite reﬂection groups. Invent. Math., 25:159–198, 1974.
[38] T. A. Springer. Linear algebraic groups, volume 9 of Progress in Mathematics. Birkh¨auser Boston,
Inc., Boston, MA, second edition, 1998.
[39] A. J. Sutherland. Upper bounds on resolvent degree and its growth rate. Preprint arXiv:2107.08139,
2021.
[40] J. Tits. Sur les degr´es des extensions de corps d´eployant les groupes alg´ebriques simples. C. R. Acad.
Sci. Paris S´er. I Math., 315(11):1131–1138, 1992.
[41] J. Tits. The´eorie des groupes. R´esum´e de cours au Coll`ege de France 1991–92. Annuaire du Coll`ege
de France, pages 125–137, 1992.
[42] J. Tits. R´esum´es des cours au Coll`ege de France 1973–2000, volume 12 of Documents Math´ematiques
(Paris). Soci´et´e Math´ematique de France, Paris, 2013.
[43] D. Tossici. Essential dimension of group schemes over a local scheme. J. Algebra, 492:1–27, 2017.
[44] B. Totaro. Splitting ﬁelds for E8-torsors. Duke Math. J., 121(3):425–455, 2004.
[45] J. Wolfson. Tschirnhaus transformations after Hilbert. Enseign. Math., 66(3-4):489–540, 2020.

Department of Mathematics, University of British Columbia, Vancouver, BC V6T 1Z2,
Canada
Email address: reichst@math.ubc.ca
