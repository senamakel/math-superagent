<!-- source: https://arxiv.org/pdf/2301.02107 | converted from PDF -->

arXiv:2301.02107v2  [math.NT]  1 Feb 2024
UNIVERSALLY DEFINING Z IN Q WITH 10 QUANTIFIERS

NICOLAS DAANS

Abstract. We show that for a global ﬁeld K, every ring of S-integers has a
universal ﬁrst-order deﬁnition in K with 10 quantiﬁers. We also give a proof
that every ﬁnite intersection of valuation rings of K has an existential ﬁrst-
order deﬁnition in K with 3 quantiﬁers.

1. Introduction

It is a longstanding open problem whether the ring of integers Z has an exis-
tential ﬁrst-order deﬁnition in the ﬁeld of rational numbers Q in the signature
of rings. In more algebraic terms, the question is whether there exist a natural
number m and a polynomial F ∈ Q[X, Y1, . . . , Ym] such that

Z = {x ∈ Q | ∃y1, . . . , ym ∈ Q : F (x, y1, . . . , ym) = 0}.

While the answer to this question still eludes us, Koenigsmann was able to show
that the complement Q \ Z is existentially deﬁnable in Q [Koe16]. In other
words, he showed that there exist a natural number m and a polynomial F ∈
Q[X, Y1, . . . , Ym] such that

(1) Z = {x ∈ Q | ∀y1, . . . , ym ∈ Q : F (x, y1, . . . , ym) ̸= 0}.

One also says that Z has a universal ﬁrst-order deﬁnition in Q, and the number
m is called the number of quantiﬁers. In this note, we show that one can ﬁnd
a polynomial F such that (1) holds already for m = 10, i.e. Z has a universal
ﬁrst-order deﬁnition in Q with 10 quantiﬁers.
In fact, we show something more. Work by Park [Par13], Eisentr¨ager and
Morrison [EM18] and the author [Daa21] revealed that Koenigsmann’s method
can be applied more generally to show that in any global ﬁeld K, any ring of
S-integers has a universal ﬁrst-order deﬁnition. By a global ﬁeld we mean either
a number ﬁeld, i.e. a ﬁnite ﬁeld extension of Q, or a global function ﬁeld, i.e. a
function ﬁeld in one variable over a ﬁnite ﬁeld. For a global ﬁeld K and a ﬁnite
(possibly empty) set S of valuations on K, the ring of S-integers is deﬁned to
be the intersection of all valuation rings of K except those which are given by

Date: Friday 2nd February, 2024.
This is the accepted version of the following article, which has been published in ﬁnal form
at https://doi.org/10.1112/jlms.12864:
Nicolas Daans. “Universally deﬁning Z in Q with 10 quantiﬁers”. In: Journal of the London
Mathematical Society 109.2 (2024), e12864 . 1

2 NICOLAS DAANS

valuations in S. Observe that Z is the ring of ∅-integers of Q. Our main result
can be summarised as follows.

Theorem (see Theorem 5.6). Let K be a global ﬁeld, S a ﬁnite set of valuations
on K. There exists a polynomial F ∈ K[X, Y1, . . . , Y10] such that, for the ring of
S-integers OS, we have

OS = {x ∈ K | ∀y1, . . . y10 ∈ K : F (x, y1, . . . , y10) ̸= 0}.

In [Koe16; Par13; EM18] the number of quantiﬁers was not counted; according
to a preprint of Koenigsmann’s article, his technique leads to a universal deﬁnition
with 418 quantiﬁers [Koe10, Theorem 1]. In [Daa21] it was shown that rings of
S-integers in global ﬁelds have a universal deﬁnition with 37 quantiﬁers; in the
case of Z in Q, this was further reﬁned by Sun and Zhang to 32 quantiﬁers in
[ZS22].
The study of the number of quantiﬁers needed to existentially deﬁne subsets
of ﬁelds is motivated for several reasons. For example, it is well-known that,
if Z would be existentially deﬁnable in Q, then it would follow that there is
no algorithm which decides whether or not a polynomial equation has a zero in
Q. This observation can be made quantitative (see [DDF21, Proposition 8.21,
Remark 8.22]): if Z would be existentially deﬁnable in Q with N quantiﬁers for
some natural number N, then it would follow that every recursively enumerable
subset of Q would be existentially deﬁnable with 12N quantiﬁers. In particular,
it would then follow from the negative solution to Hilbert’s 10th Problem that
there is no algorithm which decides whether or not a polynomial equation in 12N
variables has a zero over Q.
We can use a similar argument to deduce the following undecidability result
from the universal deﬁnability of Z in Q with 10 quantiﬁers:

Corollary (see Corollary 6.2). There exists F ∈ Z[X, Y1, . . . , Y9, Z1, . . . , Z10] with
the following property. There is no algorithm which decides, for a given x ∈ Q,
whether or not

∀y1, . . . , y9 ∈ Q ∃z1, . . . , z10 ∈ Q : F (x, y1, . . . , y9, z1, . . . , z10) = 0.

Said informally, the above corollary says that the ∀9∃10-theory of Q is unde-
cidable. Koenigsmann already showed that the ∀∃-theory of Q is undecidable
(i.e. without counting the number of universal or existential quantiﬁers). The
undecidability of the ∀9∃32-theory of Q was observed in [ZS22, Theorem 1.3].
On the way to the proof of our main theorem, we further obtain some other
classical existential deﬁnability results with better bounds. For example:

Proposition (see Proposition 4.2). Let K be a global ﬁeld, R a ﬁnite intersection
of valuation rings of K. Then there exists a polynomial F ∈ K[X, Y1, Y2, Y3] such
that R = {x ∈ K | ∃y1, y2, y3 ∈ K : F (x, y1, y2, y3) = 0}.

UNIVERSALLY DEFINING Z IN Q WITH 10 QUANTIFIERS 3

The fact that valuation rings (and hence also ﬁnite intersections of valuation
rings) of global ﬁelds are existentially deﬁnable has been known for decades, and
in certain cases this was even already shown to be possible with 3 quantiﬁers; see
the discussion in Remark 4.3. We provide a conceptually lean argument for the
above proposition which covers all cases at once, and which furthermore does so
uniformly, see Remark 4.4.
This paper is structured as follows. The following two sections contain pre-
liminaries. More precisely, in Section 2 some general (mostly well-known) results
are stated on existentially deﬁnable subsets over ﬁelds, in particular global ﬁelds,
with special attention given to the number of quantiﬁers. Quaternion algebras
(and quadratic forms) over global ﬁelds have played a historic role in establishing
existential deﬁnability of subrings of global ﬁelds. Hence, in Section 3 we survey
some algebraic ingredients regarding global ﬁelds and quaternion algebras - more
details can be found in [Daa21, Sections 3 and 4].
In Section 4 we state and prove the announced existential deﬁnability result for
valuation rings in global ﬁelds. We also develop some techniques to existentially
deﬁne certain subsets of valuation rings and cartesian products of valuation rings
with fewer quantiﬁers than one would do naively. Section 5 contains the proof of
the main theorem. Finally, in the shorter Section 6, we discuss the implications
of this result on the study of recursively enumerable subsets of Q.

Acknowledgements. The author thanks Yong Hu for pointing out an error in a
previous version of this manuscript in the beginning of Section 4, Silvain Rideau-
Kikuchi for pointing out some ambiguities in a previous version of the proof of
Theorem 5.6, and the anonymous referee for multiple suggestions which helped
improve the presentation of the article.
This work grew out of the author’s PhD dissertation [Daa22], which was sup-
ported by the FWO PhD Fellowship fundamental research grants 51581 and
83494.

2. Existentially definable subsets of fields and number of
quantifiers

There are diﬀerent ways to deﬁne what it means for a subset of a ﬁeld to be
existentially deﬁnable, and it can be convenient to switch between these equiv-
alent deﬁnitions depending on the context. These equivalences are well-known,
but are often proven without the goal in mind of keeping the number of quan-
tiﬁers low. As such, in this section, we provide short proofs or references for
these statements with quantitative bounds. We conclude the section with some
general results about the number of quantiﬁers for existentially deﬁnable subsets
of global ﬁelds.
We denote by N the set of natural numbers, and by N+ the proper subset of
nonzero natural numbers.

4 NICOLAS DAANS

We will use the basic set-up of ﬁrst-order languages, as covered by many intro-
ductory textbooks on logic or model theory, see e.g. [EFT94, Chapter II-III]. We
denote by Lring the signature of rings. It consists of two constant symbols 0 and
1, and three binary operation symbols +, − and ·. Similarly, Lﬁeld denotes the
signature of ﬁelds, which consists of two constant symbols 0 and 1, three binary
operation symbols +, − and ·, and a unary operation symbol .
−1. Given a ﬁeld
K, we interpret K as an Lring-structure or as an Lﬁeld-structure in the natural
way; we take the convention that 0−1 = 0. When C ⊆ K, we denote by Lring(C)
the signature obtained by adding to Lring a constant symbol for every element of
C, and we can then interpret K as an Lring(C)-structure in the natural way.
For a signature L, an L-formula ϕ, a variable X and an L-term t, we write
ϕ(X | t) for the formula obtained by substituting all freely occurring instances of
X in ϕ by t. When introducing a ﬁrst-order formula ϕ in a signature L, we might
write ϕ(X1, . . . , Xn) to indicate that its free variables are among X1, . . . , Xn.
Given an L-structure K and a tuple (a1, . . . , an) ∈ K n, we can then simply write
ϕ(a1, . . . , an) instead of ϕ(X1 | a1, . . . , Xn | an). As usual, for a sentence ϕ, we
write K |= ϕ to say that ϕ holds in K.
We will primarily consider existential L-formulas. Following [DDF21], for m ∈
N, we write ∃m-L-formula for “existential L-formula with m quantiﬁers”, i.e. a
formula which is logically equivalent to a formula of the form ∃X1, . . . Xmψ for
some quantiﬁer-free L-formula ψ. Similarly, we write ∀m-L-formula for “universal
L-formula with m quantiﬁers”, i.e. a formula which is logically equivalent to a
formula of the form ∀X1, . . . , Xmψ for some quantiﬁer-free L-formula ψ. Given
m1, m2 ∈ N, an ∃m1∀m2-L-formula is a formula equivalent to one of the form
∃X1, . . . , Xm1ψ where ψ is an ∀m2-L-formula; similarly, one deﬁnes ∀m1∃m2-L-
formulas.

2.1. Deﬁnition. Let K be a ﬁeld, m, n ∈ N. A set D ⊆ K n is called existentially
deﬁnable with m quantiﬁers if it is deﬁnable in K n by an ∃m-Lring(K)-formula.

This coincides with the deﬁnition hinted at in the introduction in all interesting
cases:

2.2. Proposition. Let K be a ﬁeld, m, n ∈ N+, and suppose D ⊆ K n is exis-
tentially deﬁnable with m quantiﬁers. Then there exist r ∈ N and polynomials
f1, . . . , fr ∈ K[X1, . . . , Xn, Y1, . . . , Ym] such that

(2) D = {x ∈ K n | ∃y ∈ K m : f1(x, y) = . . . = fr(x, y) = 0}.

Furthermore, if K is not algebraically closed, we may assume without loss of
generality that r = 1 in (2).

Proof. By [DDF21, Corollary 4.12] we have that D is deﬁnable by a positive-
existential Lring(K)-formula with m quantiﬁers, i.e. a formula which is logically
equivalent to ∃Y1, . . . , Ymψ for some Lring(K)-formula ψ built up from atomic
Lring(K)-formulas using only conjunctions and disjunctions (no negations). By

UNIVERSALLY DEFINING Z IN Q WITH 10 QUANTIFIERS 5

[DDF21, Remark 3.4] this implies that D can be described as in (2) for certain r
and f1, . . . , fr, where one may choose r = 1 when K is not algebraically closed.
□

We further observe that nothing would be gained if we were to work in the
signature of ﬁelds Lﬁeld instead of the signature of rings Lring:

2.3. Proposition. Let ϕ(x1, . . . , xn) be a quantiﬁer-free Lﬁeld-formula. There
exists a quantiﬁer-free Lring-formula ψ(x1, . . . , xn) such that, for every ﬁeld K
interpreted as an Lﬁeld-structure in the natural way, and for all (a1, . . . , an) ∈ K n,
we have K |= ϕ(a1, . . . , an) ⇔ K |= ψ(a1, . . . , an).

Said informally, this proposition states that one can “clear denominators” from
a quantiﬁer-free Lﬁeld-formula to obtain a quantiﬁer-free Lring-formula. For com-
pleteness, we provide a formal proof.

Proof of Proposition 2.3. Consider n ∈ N and two Lring-terms t(x1, . . . , xn) and
s(x1, . . . , xn). We can ﬁnd polynomials f, g ∈ Z[X1, . . . , Xn] such that t
K(a) =
f (a) and sK(a) = g(a) for all ﬁelds K and a ∈ K n. Let d ∈ N and f0, . . . , fd ∈
Z[X2, . . . , Xn] be such that f = ∑d
i=0 X i
1fi(X2, . . . , Xn), and consider

h =
 d∑

i=0 X d−i
1 fi(X2, . . . , Xn).

We see now that the formula t(x1 | x
−1
1 ) .
= s is equivalent for all ﬁelds to

(h(x1, . . . , xn) .
= x
d
1g(x1, . . . , xn) ∧ ¬(x1 .
= 0))

∨ (x1 .
= 0 ∧ f (0, x2, . . . , xn) .
= g(0, x2, . . . , xn)).

By recursively applying this procedure to a quantiﬁer-free Lﬁeld-formula ϕ, one
can get rid of all occurrences of −1 and obtain an equivalent quantiﬁer-free Lring-
formula. □

2.4. Corollary. Let K be a ﬁeld, m, n ∈ N. If a subset D ⊆ K n is deﬁnable by
an ∃m-Lﬁeld(K)-formula, then it is deﬁnable by an ∃m-Lring(K)-formula.

Proof. This is immediate from Proposition 2.3. □

We further observe that, if D1, D2 ⊆ K n are existentially deﬁnable with m1
and m2 quantiﬁers respectively, then D1 ∪ D2 is existentially deﬁnable with
max{m1, m2} quantiﬁers. On the other hand, in the same situation, D1 ∩ D2
is naively deﬁnable with m1 + m2 quantiﬁers. The following result says that, a.o.
for global ﬁelds, we can do slightly better in the latter case as well.

2.5. Theorem. Let K be a ﬁeld which is ﬁnitely generated over a perfect subﬁeld.
For any m1, m2, n ∈ N with m1, m2 ≥ 1 and D1, D2 ⊆ K n such that D1 is ∃m1-
Lring(K)-deﬁnable and D2 is ∃m2-Lring(K)-deﬁnable, we have that D1 ∩ D2 is
∃m1+m2−1-Lring(K)-deﬁnable.

6 NICOLAS DAANS

Proof. See [DDF21, Theorem 1.4]. □

Finally, we mention that we currently do not have many adequate techniques
available to show that a given subset of a global ﬁeld is not ∃m-Lring(K)-deﬁnable
for a given natural number m; see the discussion in [DDF21, Section 8]. In
particular, we do not have any example of an ∃-Lring(K)-deﬁnable subset of a
global ﬁeld K of which we can show that it is not ∃2-Lring(K)-deﬁnable.
On the other hand, some necessary criteria have been found for a subset of a
global ﬁeld K to be ∃1-Lring(K)-deﬁnable. If K is an imperfect ﬁeld of charac-
teristic p (e.g. a global ﬁeld of characteristic p) and k ∈ N, then the set of pk-th
powers K (pk) is an ∃1-Lring-deﬁnable inﬁnite proper subring of K. If K is a global
ﬁeld, one can show that these are the only ∃1-Lring(K)-deﬁnable inﬁnite proper
subrings of K:

2.6. Theorem. Let K be a global ﬁeld, R ⊆ K an inﬁnite proper subring of K.
Then K \ R is not ∃1-Lring(K)-deﬁnable in K. If char(K) = p > 0, and R is
∃1-Lring(K)-deﬁnable in K, then R = K (pk) for some k ∈ N.

Proof. Let p = char(K). Assume ﬁrst that, if p > 0, then R ̸⊆ K (p); we will later
see how to reduce to this case.
By [DDF21, Corollary 8.5] (in view of [DDF21, Corollary 4.21]), to show that
R and K \ R are not ∃1-Lring(K)-deﬁnable in K, it suﬃces to show that R and
K \ R are not thin subsets of K (see [DDF21, Deﬁnition 8.1]). We will use that,
if L/K is a ﬁnite separable ﬁeld extension and D ⊆ L is a thin subset of L, then
D ∩ K is a thin subset of K [FJ08, Corollary 12.2.3].
If p = 0, let K0 = Q. Otherwise, ﬁx a transcendental element T ∈ R such
that K/Fp(T ) is a separable ﬁnite ﬁeld extension, and set K0 = Fp(T ). Let
R0 = R ∩ K0. Since R0 contains either Z or Fp[T ], it is not thin in K0 [DDF21,
Remark 8.14], whereby R is not thin in K. This concludes the proof that R is
not ∃1-Lring(K)-deﬁnable in K if R ̸⊆ K (p).
To show that K \ R is not ∃1-Lring(K)-deﬁnable in K, we consider two cases.
For the ﬁrst case, suppose that R0 = K0. Then R is a ﬁeld, hence there exists
x ∈ K such that xR ⊆ K \ R. Since R is not thin in K, neither is xR, hence
neither is K \ R. In the second case, R0 ̸= K0. Then (K0 \ R0)−1 contains
the maximal ideal of a discrete valuation on K0, hence is not thin K0, whereby
K0 \ R0 is not thin in K0 and thus K \ R is not thin in K. We conclude that
K \ R is not ∃1-Lring(K)-deﬁnable in K if R ̸⊆ K (p).
We now consider the case where R ⊆ K (p). In this case, R is thin in K, whence
K \ R is not thin in K, and hence K \ R is not ∃1-Lring(K)-deﬁnable. We further
make the following observation: if R would be ∃1-Lring(K)-deﬁnable in K, then it
would also be ∃1-Lring(K (p))-deﬁnable in K (p). Indeed, by Proposition 2.2 there
would exist f ∈ K[X, Y ] such that

R = {x ∈ K | ∃y ∈ K : f (x, y) = 0} = {x ∈ K (p) | ∃y ∈ K (p) : f (x, y1/p)p = 0}.

UNIVERSALLY DEFINING Z IN Q WITH 10 QUANTIFIERS 7

Since f (X, Y 1/p)p ∈ K (p)[X, Y ], we obtain the desired ∃1-Lring(K (p))-deﬁnability
of R in K (p). Furthermore, unless R = K (p), we have that R ∩ K (p) is an inﬁnite
proper subring of the global ﬁeld K (p). Applying this observation repeatedly, and
using that R ̸⊆ K (pk) for some k ∈ N, we may reduce to the case where R ̸⊆ K (p),
which we covered before, and conclude that indeed R is not ∃1-Lring(K)-deﬁnable
in K. □

3. Quaternion algebras over global and local fields

We recall some basic facts regarding global ﬁelds and quaternion algebras over
them; most of these are also contained in [Daa21, Sections 3 and 4].
For a valuation v on a ﬁeld K, we denote by Ov the valuation ring of v, by mv
the unique maximal ideal of Ov, and by Kv the fraction ﬁeld of the completion
of Ov. We also call the pair (K, v) a valued ﬁeld. Given a ∈ Ov, we denote by
a
v the residue of a modulo mv. Similarly, for a polynomial f ∈ Ov[X1, . . . , Xn],
we denote by f v the corresponding residue polynomial in Kv[X1, . . . , Xn]. For a
ﬁeld K, we denote by VK the set of Z-valuations on K, i.e. the set of valuations
on K with value group Z.
Suppose now that K is a global ﬁeld. In this case, a Z-valuation on K cor-
responds to what is often called a ﬁnite place. Observe that for x ∈ K × there
exist only ﬁnitely many v ∈ VK for which v(x) ̸= 0 (or see e.g. [OMe00, Theo-
rem 33:1]). For v ∈ VK, the ﬁeld Kv is a complete Z-valued ﬁeld with a ﬁnite
residue ﬁeld. We call a complete Z-valued ﬁeld with ﬁnite residue ﬁeld a local
ﬁeld. We will call a valuation v on a ﬁeld K dyadic if v(2) > 0 (equivalently,
char(Kv) = 2), and non-dyadic otherwise.
We mention two standard results from valuation theory for later use. For a
univariate polynomial f , we denote by f ′ its formal derivative.

3.1. Theorem (Hensel’s Lemma). Let K be ﬁeld endowed with a complete Z-
valuation v. Let f ∈ Ov[X] be a polynomial, and let a0 ∈ Ov be such that
v(f (a0)) > 2v(f ′(a0)). Then there exists some a ∈ Ov with f (a) = 0 and v(a0 −
a) > v(f ′(a0)).

Proof. See e.g. [EP05, Theorem 1.3.1]. □

More generally, we call a valuation v on a ﬁeld K henselian if it satisﬁes the
conclusion of Theorem 3.1. We refer to [EP05, Chapter 4] for a discussion of the
structure theory of valued ﬁelds. The only henselian valuations appearing in this
paper will be the complete Z-valuations on local ﬁelds, but we will state some
auxiliary results for general henselian valuations.

3.2. Theorem (Weak Approximation Theorem). Let K be a ﬁeld, n ∈ N, and let
v1, . . . , vn be pairwise diﬀerent Z-valuations on K. For any a1, . . . , an ∈ K and
γ ∈ Z, there exists an x ∈ K with vi(x − ai) > γ for all i ∈ {1, . . . , n}.

8 NICOLAS DAANS

Proof. See e.g. [EP05, Theorem 2.4.1]; the independency assumption mentioned
there is automatically satisﬁed for pairwise diﬀerent Z-valuations. □

A ﬁeld is called real if it carries a ﬁeld ordering, nonreal otherwise. For a global
ﬁeld K there is a one-to-one correspondence between the set of ﬁeld orderings on
K and the set of ﬁeld embeddings of K into R. In particular, a global ﬁeld is
real if and only if it can be embedded into R.
A quaternion algebra over a ﬁeld K is a 4-dimensional central simple K-algebra.
We call a quaternion algebra split if it has zero divisors, non-split otherwise.
Given a ﬁeld extension L/K and a quaternion algebra Q over K, we have that
Q⊗K L is a quaternion algebra over L. We say that Q is split over L (respectively
non-split over L) if Q ⊗K L is split (respectively non-split).
Given a, b ∈ K with b(1 + 4a) ̸= 0, we deﬁne the 4-dimensional K-algebra
[a, b)K = K ⊕ Ku ⊕ Kv ⊕ Kuv with u2 − u = a, v2 = b and uv + vu = v. This is a
K-quaternion algebra, and in fact every K-quaternion algebra is of this form for
some a and b [Alb39, Section IX.10]. For a K-quaternion algebra Q, we denote
by Trd and Nrd the reduced trace and reduced norm maps Q → K respectively;
see [Sch85, Section 8.5] for the deﬁnition and basic properties.
A quaternion algebra Q over a global ﬁeld K is called nonreal if Q is split over
every embedding of K into R. By deﬁnition, if K cannot be embedded into R
(i.e. K is nonreal) then all quaternion algebras over K are nonreal.
Let Q be a quaternion algebra over a ﬁeld K. Deﬁne

∆Q = {v ∈ VK | Q is non-split over Kv}.

3.3. Proposition. Let K be a local ﬁeld. For every quadratic ﬁeld extension L/K
and any quaternion algebra Q over K, Q is split over L.

Proof. See [Pie82, Section 17.10]. □

3.4. Proposition. Let K be a local ﬁeld with Z-valuation v. Let a, b ∈ K be
such that (1 + 4a)b ̸= 0 and [a, b)K is non-split over K. Then v(a) ≤ 0, and
furthermore at least one of the following holds:
(a) v(b) is odd,
(b) v(2) = 0 and v(1 + 4a) is odd,
(c) v(2) > 0 and v(a) < 0.

Proof. This is a rephrasing of [Daa21, Proposition 4.1]. □

3.5. Theorem (Albert-Brauer-Hasse-Noether Theorem and Hilbert Reciprocity).
Let K be a global ﬁeld and let Q be a nonreal K-quaternion algebra. Then |∆Q|
is even, and furthermore we have ∆Q = ∅ if and only if Q is split. Conversely,
given a subset S ⊆ VK such that |S| is even, there exists up to K-isomorphism a
unique nonreal K-quaternion algebra Q such that ∆Q = S.

Proof. See [NSW08, Theorem 8.1.17]. □

UNIVERSALLY DEFINING Z IN Q WITH 10 QUANTIFIERS 9

3.6. Proposition. Let K be a ﬁeld. Let a, b ∈ K be such that (1 + 4a)b ̸= 0 and
set Q = [a, b)K. Furthermore, let c, d ∈ K. The following are equivalent.
(i) Q is split over the splitting ﬁeld of X 2 − cX + d.
(ii) There exists α ∈ Q \ K such that Trd(α) = c and Nrd(α) = d.
(iii) There exist x, y, z ∈ K with 2x − c, y and z not all zero such that

x
2 + x(c − 2x) − a(c − 2x)2 − b(y2 + yz − az2) = d.

Proof. The equivalence between (ii) and (iii) follows immediately from the for-
mulas for reduced norm and trace given in [Daa21, Section 3].
We now discuss the equivalence between (i) and (ii). If Q is already itself
split, then Q ∼= M2(K), Trd coincides with the matrix trace, and Nrd with
the matrix determinant (see again [Sch85, Section 8.5]). Since there exist non-
diagonal matrices in M2(K) with any prescribed trace and determinant, it follows
that both (i) and (ii) are satisﬁed.
Assume from now on that Q is non-split. For α ∈ Q \ K we have by deﬁnition
of reduced trace and norm that α2 − Trd(α)α + Nrd(α) = 0. If (ii) holds, then
K(α) is thus the splitting ﬁeld of X 2 − cX + d. Since Q is split over its subﬁeld
K(α) (see e.g. [Sch85, Theorem 5.4]), we obtain (i).
Conversely, assume that (i) holds. Since Q is non-split, the splitting ﬁeld of
X 2 − cX + d is a proper quadratic extension of K. By [Alb39, Theorem IV.27]
the splitting ﬁeld of X 2 − cX + d embeds over K into Q. Denoting by α ∈ Q
an element for which α2 − cα + d = 0, we obtain that α ̸∈ K, Trd(α) = c and
Nrd(α) = d, as desired. □

4. Defining valuation rings, individually and uniformly

In this section, we will show that a subring R of a global ﬁeld K which is a
ﬁnite intersection of valuation rings of K, is ∃3-Lring(K)-deﬁnable in K (Propo-
sition 4.2). This implies that in fact Rn is ∃3-Lring(K)-deﬁnable in K n for every
natural number n, as we will see in Proposition 4.8. Finally, at the end of this
section, we recall a result on uniform existential deﬁnability of ﬁnite intersections
of valuation rings (essentially due to Poonen and Koenigsmann), see Proposi-
tion 4.10.
For a ﬁeld K and a ∈ K, denote by K(a) the splitting ﬁeld of X 2 − X − a
over K. In other words, K(a) = K if X 2 − X − a has a root in K, otherwise
K(a) ∼= K[X]/(X 2 − X − a).

4.1. Lemma. Let K be a global ﬁeld. Let S be a ﬁnite set of Z-valuations on K,
Q a nonreal quaternion algebra over K such that S ⊆ ∆Q. Let π, a ∈ K × such
that for all v ∈ ∆Q one has v(π) = 1, v(a) ≥ v(1 + 4a) = 0, and X 2 − X − a has
a root over Kv if and only if v ∈ S. Then

(3) ⋂

v∈S Ov = {0} ∪ {x ∈ K | Q is split over K(a−(πx2)−1)}.

10 NICOLAS DAANS

Proof. Consider x ∈ K × and let L = K(a−(πx2)−1). Since Q is nonreal (and hence
remains nonreal over L) it follows by Theorem 3.5 that Q is split over L if and
only if it is split over Lw for all Z-valuations w on L. Since for any Z-valuation
w on L we have that Lw ∼= LKv = (Kv)(a−(πx2)−1) for some Z-valuation v on K,
we conclude that Q is split over L if and only if it is split over (Kv)(a−(πx2)−1)
for all v ∈ ∆Q. In order to show (3), we thus have to show that x ∈ ⋂
v∈S Ov
if and only if Q is split over (Kv)(a−(πx2)−1) for all v ∈ ∆Q. Finally, in view of
Proposition 3.3, for any v ∈ ∆Q, we have that Q is split over (Kv)(a−(πx2)−1) if
and only if (Kv)(a−(πx2)−1)/Kv is a quadratic ﬁeld extension, i.e. if and only if
X 2 − X − (a − (πx
2)−1) is irreducible over Kv. In summary, we are left to show
the following:

x ∈ ⋂

v∈S Ov ⇔ ∀v ∈ ∆Q : X 2 − X − (a − (πx
2)−1) is irreducible over Kv.

Consider a valuation v ∈ ∆Q. Assume ﬁrst that x ∈ Ov. Suppose that α ∈ Kv
were a root of X 2 − X − (a − (πx
2)−1). Since we then must have v(α) < 0, we
compute that 2v(α) = v(α2−α−a) = v((πx
2)−1) = −1−2v(x), which contradicts
the fact that v is a Z-valuation. We obtain that X 2 − X − (a − (πx
2)−1) is
irreducible over Kv.
On the other hand, for v ∈ ∆Q and x ∈ K \ Ov one has that X 2 − X − (a −
(πx
2)−1) ≡ X 2 − X − a mod mv, so by Hensel’s Lemma (Theorem 3.1) we have
that X 2 − X − (a − (πx
2)−1) is has a root over Kv if and only if X 2 − X − a has
a root over Kv, which by assumption is precisely the case when v ∈ S.
As desired, we conclude that for x ∈ K × and v ∈ ∆Q, we have that X 2 − X −
(a − (πx
2)−1) is irreducible over Kv if and only if either v ̸∈ S or x ∈ Ov. □

4.2. Proposition. Let K be a global ﬁeld. Let S be a ﬁnite set of Z-valuations
on K. Then ⋂
v∈S Ov has an ∃3-Lring(K)-deﬁnition in K.

Proof. There exists a nonreal quaternion algebra Q over K such that S ⊆ ∆Q,
and furthermore, ∆Q is ﬁnite. This follows from the second part of Theorem 3.5,
but can also be seen more elementarily, see e.g. [Daa22, Lemma 6.3.6].
By Weak Approximation (Theorem 3.2), we can ﬁnd π, a ∈ K × such that
the criteria of Lemma 4.1 are satisﬁed and thus (3) holds. Thus it suﬃces to
show that the set on the right in (3) has an ∃3-Lring(K)-deﬁnition in K. This is
immediate from Proposition 3.6. □

4.3. Remark. The proof technique from Lemma 4.1 and Proposition 4.2 goes
back to Julia Robinson. In fact, she showed that, for K = Q, ⋂
v∈S Ov is ∃3-
Lring-deﬁnable with S = {v2, vp} where p is a prime with p ≡ 3 mod 4. Similarly,
she showed that ⋂
v∈S Ov is ∃3-Lring-deﬁnable with S = {vp, vq} where p and q
are primes with p ≡ 1 mod 4 and such that q is not a square modulo p [Rob49,
Lemma 3 and 4]. A similar argument can be found in [ZS22, Lemma 3.1] for
S = {v2}.
 UNIVERSALLY DEFINING Z IN Q WITH 10 QUANTIFIERS 11

It is in any case well-known that in a global ﬁeld, any valuation ring (and
hence also any ﬁnite intersection of valuations rings) is existentially deﬁnable,
see e.g. [KR92, Proposition 3.1] for number ﬁelds, [Shl94, Lemma 3.22] for global
ﬁelds of odd characteristic, or [Eis98, Theorem 5.15] for a proof covering all
characteristics. Our argument has the advantage of yielding in all cases a formula
requiring only 3 existential quantiﬁers.

4.4. Remark. Inspection of the proof of Proposition 4.2 reveals that the deﬁn-
ing formula is uniform in the following sense: there exists an ∃3-Lring-formula
ϕ(X, C1, . . . , Cm) such that, for every global ﬁeld K and every ﬁnite set S of
Z-valuations on K, there exist parameters c1, . . . , cm ∈ K such that
⋂

v∈S Ov = {x ∈ K | K |= ϕ(x, c1, . . . , cm)}.

An even more robust formula, but with more quantiﬁers, will be given in Propo-
sition 4.10.

In the setting of Proposition 4.2 and with S ̸= ∅, by Theorem 2.6 we have that⋂
v∈S Ov is not ∃1-Lring(K)-deﬁnable in K.

4.5. Question. Let K be a global ﬁeld. Let S be a non-empty ﬁnite set of Z-
valuations on K. Does ⋂
v∈S Ov have an ∃2-Lring(K)-deﬁnition in K?

When R is a subring of a ﬁeld K and R is existentially deﬁnable in K, then
clearly also R× is existentially deﬁnable in K, and Rn is existentially deﬁnable
in K n for all n ∈ N. However, if for example R is ∃m-Lring(K)-deﬁnable in K,
then the naive way to existentially deﬁne Rn in K n requires nm quantiﬁers, or
n(m − 1) + 1 quantiﬁers if one can apply Theorem 2.5. We investigate cases
in which a better bound on the number of required quantiﬁers can be found, in
particular when R is a ﬁnite intersection of valuation rings.

4.6. Proposition. Let R be an integrally closed domain and K = Frac(R). For
x ∈ K one has
 x ∈ R× if and only if x ̸= 0 and x + x
−1 ∈ R.

In particular, if R is ∃m-Lring(K)-deﬁnable for m ∈ N, then also R× is ∃m-
Lring(K)-deﬁnable.

Proof. The implication from left to right is immediate. Conversely, assume that
x + x
−1 ∈ R, then x ∈ R[x
−1]. This implies that x is integral over R, and thus
by assumption x ∈ R. Then also x
−1 = (x + x
−1) − x ∈ R, and thus x ∈ R×.
The deﬁnability statement follows immediately. □

4.7. Lemma. Let K be a ﬁeld, n ∈ N, v a valuation on K. Let f (X1, . . . , Xn) ∈
Ov[X1, . . . , Xn] be a homogeneous polynomial such that f v ∈ Kv[X1, . . . , Xn] has
no non-trivial zeros. For any elements a1, . . . , an ∈ K we have that

v(f (a1, . . . , an)) = deg(f ) min{v(ai) | i ∈ {1, . . . , n}}

12 NICOLAS DAANS

Proof. If a1 = . . . = an = 0 there is nothing to show, so we may suppose that
this is not the case. The validity of the statement is not aﬀected if (a1, . . . , an)
is scaled by an element of K ×, so we may assume without loss of generality
that minn
i=1 v(ai) = 0; we need to show that v(f (a1, . . . , an)) = 0. If not, then
we would have f v(a1v, . . . , anv) = f (a1, . . . , an)v = 0 in Kv, contradicting the
assumption that f v has no non-trivial zeros. □

4.8. Proposition. Let K be a ﬁeld and let S be a ﬁnite set of valuations on K.
Let R = ⋂
v∈S Ov. Suppose that Kv is not algebraically closed for all v ∈ S.
For each n ∈ N+, there exists a polynomial G ∈ K[X1, . . . , Xn] such that, for
all x ∈ K n, we have G(x) ∈ R if and only if x ∈ Rn. In particular, if R is
∃m-Lring(K)-deﬁnable for some m ∈ N, then also Rn is ∃m-Lring(K)- deﬁnable.

Proof. By replacing S with an appropriate subset if necessary, we may assume
that Ov ̸⊆ Ow for any two distinct v, w ∈ S.
By the assumption on the residue ﬁelds and a version of Weak Approximation
[EP05, Theorem 3.2.7.(3)], we can ﬁnd for each v ∈ S a monic polynomial fv ∈
R[X] such that its residue fv v is of degree at least 2 and irreducible over Kv. Let
d = ∏

v∈S deg(fv) and dv = d/ deg(fv) for each v ∈ S. Denote by f ∗
v ∈ R[X, Y ]
the homogenisation of fv, and observe that f ∗
v v has no non-trivial zeros over Kv.
Finally, again invoking [EP05, Theorem 3.2.7.(3)], ﬁx for each v ∈ S an element
αv ∈ R such that v(αv) = 0 and w(αv) > 0 for all w ∈ S \ {v}. We now deﬁne

F (X, Y ) = ∑

v∈S αvf ∗
v (X, Y )dv ∈ R[X, Y ],

which is homogeneous of degree d. Consider v ∈ S. We claim that for all x, y ∈ K
we have v(F (x, y)) = d min{v(x), v(y)}
To see, this, note that by Lemma 4.7 we have

v(αvf ∗
v (x, y)dv) = 0 + (deg(fv)dv) min{v(x), v(y)} = d min{v(x), v(y)},

whereas for w ∈ S \ {v} we have

v(αwf ∗
w(x, y)dw) ≥ v(αw) + (deg(fw)dw) min{v(x), v(y)} > d min{v(x), v(y)},

from which the desired statement follows. Since this holds for all v ∈ S, we
obtain that, for all x, y ∈ K, one has

F (x, y) ∈ R ⇔ x ∈ R and y ∈ R.

We can now inductively for i ≥ 1 deﬁne polynomials Gi(X1, . . . , Xi) by setting
G1(X1) = X1 and Gi(X1, . . . , Xi) = F (Gi−1(X1, . . . , Xi−1), Xi). We see that, for
x1, . . . , xn ∈ K, we have

Gn(x1, . . . , xn) ∈ R ⇔ x1, . . . , xn ∈ R,

so G is as desired. The deﬁnability statement follows immediately. □

UNIVERSALLY DEFINING Z IN Q WITH 10 QUANTIFIERS 13

We conclude this section with a brief discussion of a uniform existential deﬁn-
ability result essentially due to Poonen and Koenigsmann [Poo09; Koe16], which
will play a central role in the proof of the main theorem. We recall from [Daa21,
Section 5] the following deﬁnition. For a ﬁeld K and a quaternion algebra Q over
K, we deﬁne the following subset of K:

S(Q) = {Trd(α) | α ∈ Q \ K, Nrd(x) = 1}.

4.9. Theorem. Let Q be a nonreal quaternion algebra over a global ﬁeld K. Then
⋂

v∈∆Q Ov = {x + y | x, y ∈ S(Q)}.

Proof. See [Dit18, Proposition 2.9]. In the case K = Q, the argument goes back
to [Koe16, Proposition 6], using ideas already developed in [Poo09]. □

4.10. Proposition. Let K be a global ﬁeld. There exists an ∃6-Lring(K)-formula
ϕ(X, A, B) such that, for all a, b ∈ K with (1 + 4a)b ̸= 0 and such that [a, b)K is
nonreal, we have ⋂

v∈∆[a,b)K Ov = {x ∈ K | K |= ϕ(x, a, b)}.

Proof. In view of Proposition 3.6 we have that

{(x, a, b) ∈ K 3 | (1 + 4a)b ̸= 0 and x ∈ S([a, b)K)}

is ∃3-Lring-deﬁnable. Furthermore, by Theorem 4.9, we have for a, b ∈ K with
(1 + 4a)b ̸= 0 and [a, b)K nonreal that

x ∈ ⋂

v∈∆[a,b)K Ov ⇔ ∃y ∈ K : y ∈ S([a, b)K) and x − y ∈ S([a, b)K).

By applying Theorem 2.5 with

D1 = {(x, y, a, b) ∈ K 4 | (1 + 4a)b ̸= 0 and y ∈ S([a, b)K)} and

D2 = {(x, y, a, b) ∈ K 4 | (1 + 4a)b ̸= 0 and x − y ∈ S([a, b)K)}

and using that D1 and D2 are both ∃3-Lring(K)-deﬁnable, we obtain the desired
result. □

5. Universally defining rings of S-integers

We now work our way towards the universal deﬁnability of rings of S-integers
in global ﬁelds with 10 quantiﬁers (Theorem 5.6).

5.1. Lemma. Let V be a non-empty set of valuations on a ﬁeld K, n ∈ N. The
set ⋃
v∈V mv has an ∃n-Lring(K)-deﬁnition in K if and only if ⋂
v∈V Ov has an
∀n-Lring(K)-deﬁnition in K.

14 NICOLAS DAANS

Proof. By Corollary 2.4 it suﬃces to show that ⋃
v∈V mv has an ∃n-Lﬁeld(K)-
deﬁnition in K if and only if ⋂
v∈V Ov has an ∀n-Lﬁeld(K)-deﬁnition in K. This
in turn follows from the observation

⋂

v∈V Ov =
 

K \
 ( ⋃

v∈V mv
)−1

 ∪ {0}.
 □

Following [Daa21, Section 6], for a global ﬁeld K, a non-empty ﬁnite set S ⊆ VK
and u ∈ ⋂
v∈S O×
v , deﬁne the set

Φ
S
u =
 {
(a, b) ∈ K 2 ∣
∣
∣
∣
∣ b ∈ ⋂

v∈S O×
v , a ≡ u mod ∏

v∈S mv
}
 .

5.2. Lemma. Let K be a global ﬁeld, S ⊆ VK a non-empty ﬁnite set and u ∈⋂
v∈S O×
v . The set Φ
S
u has an ∃3-Lring(K)-deﬁnition in K 2.

Proof. By Weak Approximation, we can ﬁnd π ∈ K × with v(π) = 1 for all v ∈ S.
We see that for a, b ∈ K we have that

(a, b) ∈ Φ
S
u ⇔ b ∈ ⋂

v∈S O×
v and a − u
π ∈ ⋂

v∈S Ov

⇔ b
2 + 1
b , a − u
π ∈ ⋂

v∈S Ov.

where the second equivalence follows from Proposition 4.6. By Proposition 4.2⋂
v∈S Ov is ∃3-Lring(K)-deﬁnable, and then the desired result follows from Propo-
sition 4.8 (and Corollary 2.4). □

5.3. Lemma. Let (K, v) be a valued ﬁeld and consider the rational function

g(X, Y ) = 16X 4

1 + 4X 2 − ((Y − 1)2

Y
 )2 ∈ K(X, Y ).

Let a, b ∈ K with (1 + 4a
2)b ̸= 0. We have the following:
(1) If 1 + 4a
2, b ∈ O×
v , then g(a, b) ∈ Ov.
(2) If v(1 + 4a
2) = 0 and v(b) ̸= 0, then v(g(a, b)) = −2|v(b)|.
(3) If v is henselian and non-dyadic, X 2 − X − a
2 is irreducible, and g(a, b) ∈
Ov, then 1 + 4a
2, b ∈ O×
v .

Proof. We can compute that for a ∈ K we have

v ( 16a
4

1 + 4a2
 ) 



= −v(1 + 4a
2) < 0 if v(1 + 4a
2) > 0,
= 2v(a) + 2v(2) < 0 if v(1 + 4a
2) < 0,
≥ 0 if v(1 + 4a
2) = 0,

UNIVERSALLY DEFINING Z IN Q WITH 10 QUANTIFIERS 15

and similarly, for b ∈ K

v ((b − 1)2

b
 ) {= −|v(b)| < 0 if v(b) ̸= 0,
≥ 0 if v(b) = 0.

(1) and (2) now follow immediately.
For (3), assume that v is henselian and non-dyadic, X 2 − X − a
2 is irreducible,
and either 1 + 4a
2 ̸∈ O×
v or b ̸∈ O×
v ; we need to show that g(a, b) ̸∈ Ov. If b ∈ O×
v ,
then this is immediate from the computations in the above paragrapgh. Assume
for the sake of a contradiction that b ̸∈ O×
v and v(g(a, b)) ≥ 0. Then

v
 (( 4a
2b
(b − 1)2
 )2 1
1 + 4a2 − 1
)
 = v
 (( b
(b − 1)2
 )2 g(a, b)
)
 ≥ |v(b)| > 0.

Using that (K, v) is henselian and non-dyadic, this implies that 1+4a
2 is a square
in K, contradicting the assumption that X 2 − X − a
2 was irreducible. □

5.4. Lemma. Let (K, v) be a valued ﬁeld and consider the rational function

g(X, Y ) = X 5 (( (Y − 1)2

Y
 )2 − ( (Y − 1)2

Y
 ) − X 2)
 ∈ K(X, Y ).

Let a, b ∈ K ×. We have the following:

(1) If a, b ∈ O×
v , then g(a, b) ∈ Ov.
(2) If v(a) = 0 and v(b) ̸= 0, then v(g(a, b)) = −2|v(b)|.
(3) If char(K) = 2, v is henselian, X 2−X −a
2 is irreducible, and g(a, b) ∈ Ov,
then a, b ∈ O×
v .

Proof. For b ∈ K we have

v ((b − 1)2

b
 ) {= −|v(b)| < 0 if v(b) ̸= 0,
≥ 0 if v(b) = 0.

From this, (1) and (2) follow immediately.
For (3), assume that char(K) = 2, v is henselian, X 2 − X − a
2 is irreducible,
and either a ̸∈ O×
v or b ̸∈ O×
v ; we need to show that g(a, b) ̸∈ Ov. Observe that
anyway v(a) ≤ 0; otherwise X 2 − X − a
2 would be reducible by the henselianity
of v. More, precisely, we have for any y ∈ K that v(y2 − y − a
2) ≤ −4v(a) since
v is henselian. If v(a) < 0, we thus obtain that v(g(a, b)) < v(a) < 0. On the
other hand, if v(a) = 0 and v(b) ̸= 0, we obtain that v(g(a, b)) = −2|v(b)| < 0 by
(2). This concludes the proof of (3). □

For a ﬁeld K and c ∈ K ×, deﬁne the set

Odd(c) = {v ∈ VK | v(c) is odd}.

16 NICOLAS DAANS

5.5. Lemma. Let K be a global ﬁeld. Let π ∈ K × be such that S = Odd(π) has
odd cardinality. Let u ∈ K × be such that for all v ∈ S one has v(u) = 0 and
X 2 − X − u2 is irreducible over Kv. If char(K) = 2, let g(X, Y ) ∈ K(X, Y )
be as in Lemma 5.4. If char(K) ̸= 2, then assume that S contains all dyadic
valuations, and let g(X, Y ) ∈ K(X, Y ) be as in Lemma 5.3.
For x ∈ K we have

x ∈ ⋃

v∈VK \S mv ⇔ ∃(a, b) ∈ Φ
S
u : a
2x
2g(a, b)
1 − x − a2x2 ∈ ⋂

v∈∆[a2,bπ)K Ov.

Proof. We ﬁrst consider the implication from left to right. Consider x ∈ mw for
some w ∈ VK \ S. As in the proof of [Daa21, Lemma 6.6], we can ﬁnd (a, b) ∈ Φ
S
u
such that ∆[a
2, bπ)K = S ∪ {w} and w(1 + 4a
2) = 0. We must then have that
w(bπ) is odd by Proposition 3.4, and since w(π) is even, this implies that w(b) is
odd. After rescaling b by a square in K if necessary (which does not aﬀect the
K-isomorphism class of [a
2, bπ)K), we may assume without loss of generality that
w(b) = 1.
By either Lemma 5.3 or Lemma 5.4 we obtain that w(g(a, b)) = −2, whereas
v(g(a, b)) ≥ 0 for v ∈ S. Furthermore, since for all v ∈ S ∪ {w} one has that
X 2 − X − a
2 is irreducible over Kv, and hence the form X 2 − XY − a
2Y 2 has no
non-trivial zeroes over Kv, we compute by Lemma 4.7 that for v ∈ S ∪ {w} =
∆[a
2, bπ)K one has

v ( a
2x
2g(a, b)
1 − x − a2x2
 ) = 2v(a) + 2v(x) + v(g(a, b)) − min{0, 2v(a) + 2v(x)}

= max{v(g(a, b)), 2v(x) + v(g(a, b))} ≥ 0

where the inequality in the end follows from the fact that v(g(a, b)) ≥ 0 for
v ∈ S, and from w(g(a, b)) = −2 and w(x) ≥ 1. We conclude that a2x2g(a,b)
1−x−a2x2 ∈⋂
v∈∆[a2,bπ)K Ov as desired.
For the other implication, consider (a, b) ∈ Φ
S
u arbitrary. As in the proof of
[Daa21, Lemma 6.6] we see that S ⊆ ∆[a
2, bπ)K and that [a
2, bπ)K is nonreal, so
that by Theorem 3.5 there exists w ∈ ∆[a
2, bπ)K \ S. By Proposition 3.4, using
that w is non-dyadic if char(K) ̸= 2, at least one of the following occurs:

(i) w(bπ) is odd. Since w(π) is even, this implies w(b) is odd,
(ii) char(K) ̸= 2 and w(1 + 4a
2) is odd,
(iii) char(K) = 2 and w(a) < 0.

Furthermore, we know that X 2 − X − a
2 is irreducible over Kw, since [a
2, bπ)K
is non-split over Kw. It follows by Lemma 5.3 or Lemma 5.4 that w(g(a, b)) < 0.

UNIVERSALLY DEFINING Z IN Q WITH 10 QUANTIFIERS 17

We compute that for x ∈ K with a2x2g(a,b)
1−x−a2x2 ∈ ⋂
v∈∆[a2,b)K Ov we have

0 ≤ w ( a
2x
2g(a, b)
1 − x − a2x2
 ) ≤ 2w(a) + 2w(x) + w(g(a, b)) − min{0, 2w(a) + 2w(x)}

= max{2w(a) + 2w(x) + w(g(a, b)), w(g(a, b))}

Since w(g(a, b)) < 0, we infer that 2w(x) ≥ −2w(a) − w(g(a, b)) > 0, whereby
x ∈ mw. This shows the other implication. □

5.6. Theorem. Let K be a global ﬁeld, S ⊆ VK a non-empty ﬁnite set. The set⋂
v∈V\S Ov has an ∀10-Lring(K)-deﬁnition in K.

Proof. In view of Lemma 5.1, we only need to show that ⋃
v∈V\S mv has an ∃10-
Lring(K)-deﬁnition in K. Furthermore, it suﬃces to show this for some ﬁnite set
S′ of valuations containing the set S. Indeed we have
⋃

v∈V\S mv = ⋃

v∈S′\S mv ∪ ⋃

v∈V\S′ mv

and, for each v ∈ S′ \ S individually, mv is ∃3-Lring(K)-deﬁnable by Proposi-
tion 4.2: after ﬁxing a uniformiser π of v, one has mv = {x ∈ K | xπ−1 ∈ Ov}.
Since S′ \ S is ﬁnite, ∃10-Lring(K)-deﬁnability of ⋃
v∈V\S mv thus follows from
∃10-Lring(K)-deﬁnability of ⋃
v∈V\S′ mv. As such, in the rest of the proof, we may
without loss of generality replace S by a larger ﬁnite set.
If char(K) = 0, we enlarge S so that it contains all dyadic valuations. By
[Daa21, Lemma 6.7] we may further enlarge S so that S = Odd(π) for some
π ∈ K × and |S| is odd. Fix u ∈ ⋂
v∈S O×
v such that X 2 − X − u2 is irreducible
over Kv for all v ∈ S; such element u exists by Weak Approximation and [Daa21,
Lemma 6.5]. By Lemma 5.5 there is a rational function g(X, Y ) ∈ K(X, Y ) such
that, for any x ∈ K, one has

x ∈ ⋃

v∈VK \S mv ⇔ ∃a, b ∈ K : (a, b) ∈ Φ
S
u and a
2x
2g(a, b)
1 − x − a2x2 ∈ ⋂

v∈∆[a2,bπ)K Ov.

Since Φ
S
u is ∃3-Lring(K)-deﬁnable by Lemma 5.2 and the sets ⋂
v∈∆[a2,bπ)K Ov are
uniformly ∃6-Lring(K)-deﬁnable by Proposition 4.10, we obtain that ⋂
v∈VK \S mv
is existentially deﬁnable with 2 + 3 + 6 − 1 = 10 quantiﬁers by Theorem 2.5 (and
in view of Proposition 2.3). □

5.7. Question. What is the smallest natural number m such that Z is ∀m-Lring-
deﬁnable in Q?

By Theorem 5.6 and Theorem 2.6 we obtain that the answer to Question 5.7
is at least 2 and at most 10.

18 NICOLAS DAANS

6. Recursively enumerable subsets of Q

We conclude with a proof of the promised undecidability result concerning
the ∀9∃10-Lring-theory of Q (Corollary 6.2). We present the argument in a way
that makes transparent how further quantitative improments to the universal
deﬁnability of Z in Q would impact the undecidability result. The argument is
essentially a reformulation of the proof of [ZS22, Theorem 1.3].
To be precise: when we say that the ∀m∃n-Lring-theory of a ring R is unde-
cidable, we mean that there is no algorithm which takes as input an arbitrary
∀m∃n-Lring-sentence ϕ and, after a ﬁnite amount of steps, outputs YES if R |= ϕ
and NO if R ̸|= ϕ.

6.1. Proposition. Let m ∈ N such that m ≥ 4. Assume that Z is ∀m-Lring-
deﬁnable in Q. Then every recursively enumerable subset of Q is ∃10∀m-Lring-
deﬁnable in Q. Furthermore, every recursively enumerable subset of Z is ∃9∀m-
Lring-deﬁnable in Q.
In particular, the ∀9∃m-Lring-theory of Q is undecidable.

Proof. Fix a polynomial f ∈ Z[X, Y ] such that f deﬁnes an injection Z × Z → N
(see e.g. [DDF21, Lemma 8.19]). For a subset A ⊆ Q, deﬁne

˜A = {f (a, b) | a, b ∈ Z, b ̸= 0, a
b ∈ A}

and observe that for any a ∈ Q we have

a ∈ A ⇔ ∃y0 ∈ Q(y0 ∈ Z, ay0 ∈ Z and f (ay0, y0) ∈ ˜A).

Now assume that A is recursively enumerable. Then also ˜A is recursively enumer-
able. By [Sun21, Theorem 1.1(i)] there exists a polynomial g ˜A ∈ Z[X, Y1, . . . , Y9]
such that ˜A = {x ∈ N | ∃y1, . . . , y8 ∈ Z, y9 ∈ N : g ˜A(x, y1, . . . , y9) = 0}.

We obtain that, for any a ∈ Q, we have that a ∈ A if and only if
(4)
∃y0, . . . , y9 ∈ Q (ay0, y0, . . . , y9 ∈ Z, y9 ≥ 0, and g ˜A(f (ay0, y0), y1, . . . , y9) = 0)

Since Z is ∀m-Lring-deﬁnable in Q and the set of non-negative elements is ∀4-Lring-
deﬁnable in Q by Euler’s Four-Square Theorem, we obtain the desired ∃10∀m-
Lring-deﬁnability of A in Q. If A ⊆ Z then one may remove the quantiﬁcation
over y0 in (4) and equivalently write

(5) ∃y1, . . . , y9 ∈ Q (y1, . . . , y9 ∈ Z, y9 ≤ 0, and g ˜A(f (a, 1), y1, . . . , y9) = 0)

to obtain that A is ∃9∀m-Lring-deﬁnable in Q.
For the ﬁnal statement, ﬁx a recursively enumerable subset A of N such that
N \ A is not recursively enumerable (in other words, A is not recursive). By the
above, A is ∃9∀m-Lring-deﬁnable in Q. But since A is not recursive, there cannot
be an algorithm which decides whether a given element of Q lies in A. This

REFERENCES 19

shows that the ∃9∀m-Lring-theory - or, equivalently, the ∀9∃m-Lring-theory - of Q
is undecidable. □

6.2. Corollary. Every recursively enumerable subset of Q is ∃10∀10-Lring-deﬁnable
in Q. Furthermore, every recursively enumerable subset of Z is ∃9∀10-Lring-
deﬁnable in Q.
In particular, the ∀9∃10-Lring-theory of Q is undecidable.

Proof. This follows from Proposition 6.1 and Theorem 5.6. □

References

[Alb39] A. Adrian Albert. Structure of Algebras. American Mathematical So-
ciety, 1939.
[Daa21] Nicolas Daans. “Universally deﬁning ﬁnitely generated subrings of
global ﬁelds”. In: Documenta Mathematica 26 (2021), pp. 1851–1869.
[Daa22] Nicolas Daans. “Existential ﬁrst-order deﬁnitions and quadratic forms”.
PhD thesis. Universiteit Antwerpen, 2022.
[DDF21] Nicolas Daans, Philip Dittmann, and Arno Fehm. “Existential rank
and essential dimension of diophantine sets”. Available as arXiv:2102.06941.
2021.
[Dit18] Philip Dittmann. “Irreducibility of polynomials over number ﬁelds is
diophantine”. In: Compositio Mathematica 154 (2018), pp. 761–772.
[EFT94] H.-D. Ebbinghaus, J. Flum, and W. Thomas. Mathematical logic. Sec-
ond edition. Springer, 1994.
[Eis98] Kirsten Eisentr¨ager. “Hilbert’s Tenth Problem and Arithmetic Geom-
etry”. PhD thesis. University of California, 1998.
[EM18] Kirsten Eisentr¨ager and Travis Morrison. “Universally and existen-
tially deﬁnable subsets of global ﬁelds”. In: Mathematical Research
Letters 25.4 (2018), pp. 1173–1204.
[EP05] Antonio J. Engler and Alexander Prestel. Valued Fields. Springer,
2005.
[FJ08] Michael D. Fried and Moshe Jarden. Field Arithmetic. Second edition.
Springer, 2008.
[Koe10] Jochen Koenigsmann. “Deﬁning Z in Q”. Preprint. Available as arXiv:1011.3424v1.
Oct. 2010.
[Koe16] Jochen Koenigsmann. “Deﬁning Z in Q”. In: Annals of Mathematics.
183 (2016), pp. 73–93.
[KR92] Ki Hang Kim and Fred Roush. “An Approach to Rational Diophantine
Undecidability”. In: Proceedings of Asian Mathematical Conference
1990. World Scientiﬁc, 1992, pp. 242–248.
[NSW08] J¨urgen Neukirch, Alexander Schmidt, and Kay Wingberg. Cohomology
of Number Fields. Second edition. Springer, 2008.
[OMe00] Timothy O’Meara. Introduction to Quadratic Forms. Springer, 2000.

20 REFERENCES

[Par13] Jennifer Park. “A universal ﬁrst-order formula deﬁning the ring of
integers in a number ﬁeld”. In: Mathematical Research Letters 20 nr.
5 (2013), pp. 961–980.
[Pie82] Richard S. Pierce. Associative Algebras. Springer, 1982.
[Poo09] Bjorn Poonen. “Characterizing integers among rational numbers with
a universal-existential formula”. In: American Journal of Mathematics
131 (2009), pp. 675–682.
[Rob49] Julia Robinson. “Deﬁnability and decision problems in arithmetic”.
In: Journal of Symbolic Logic 14 (Feb. 1949), pp. 98–114.
[Sch85] Winfried Scharlau. Quadratic and Hermitian Forms. Springer, 1985.
[Shl94] Alexandra Shlapentokh. “Diophantine Classes of Holomorphy Rings
of Global Fields”. In: Journal of Algebra 1 (1994), pp. 139–175.
[Sun21] Zhi-Wei Sun. “Further results on Hilbert’s Tenth Problem”. In: Science
China Mathematics 64.2 (2021), pp. 281–306.
[ZS22] Geng-Rui Zhang and Zhi-Wei Sun. “Q\Z is diophantine over Q with 32
unknowns”. In: Bulletin Polish Acad. Sci. Math. 70.2 (2022), pp. 93–
106.

Universiteit Antwerpen, Departement Wiskunde, Middelheimlaan 1, 2020 Antwer-
pen, Belgium.

Charles University, Faculty of Mathematics and Physics, Department of Al-
gebra, Sokolovsk´a 83, 186 75 Praha 8, Czech Republic.
Email address: nicolas.daans@matfyz.cuni.cz
