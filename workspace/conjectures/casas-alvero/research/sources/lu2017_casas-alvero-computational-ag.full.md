<!-- source: https://arxiv.org/pdf/1707.04754 | converted from PDF -->

arXiv:1707.04754v6  [math.AC]  16 Mar 2021
THE CASAS-ALVERO CONJECTURE IN COMPUTATIONAL
ALGEBRAIC GEOMETRY

ZHIPENG LU

Abstract. We study varieties deﬁned by parameterizing polynomials of derivatives
through a computational algebro-geometric approach, especially relying on Combina-
torial Nullstellensatz and Noether normalization. We establish that these polynomials
form regular sequences easily. This allows us to calculate the dimension of thus deﬁned
varieties and consequently give a proof to the Casas-Alvero conjecture.

1. Introduction

The Casas-Alvero conjecture, ﬁrst asked in [2], states that a complex polynomial f
having common roots with all its non-zero derivatives f (i) must be of the form a(x − b)n.
Since asked the conjecture has stood up with many attempts from diﬀerent technical
aspects and yet remains unproven. The current best partial result by Draisma-de Jong
[3] conﬁrmed the conjecture for pen, with n ∈ {1, 2, 3, 4}, e ≥ 0. Note that it is not true
over ﬁelds of ﬁnite characteristic since any xn − xp for n ≥ 1) is a counterexample over Fp.
However we will show that the problem can be dramatically resolved over ﬁnite ﬁelds Fp.
A natural idea on resolving the conjecture is by studying the resultants of f and its
derivatives. However the complexity of resultants makes detailed analysis unpractical.
Instead we formulate the problem in a more intuitive algebro-geometric set up which
dramatically reduces the problem to some computational or combinatorial considerations
in commutative algebra straightforwardly described below.
If a degree n ≥ 1 polynomial having common roots with all its n − 1 derivatives, we call
it a Casas-Alvero polynomial. Any monic polynomial f factors over C as

f (x) = (x − x1) . . . (x − xn).

Then the Casas-Alvero condition actually deﬁnes an algebraic set in An
C:

CAn := Z(F1, . . . , Fn−1),

in which
 Fi =
 n∏

k=1 f (i)(xk) ∈ C[x1, . . . , xn], ∀i = 1, . . . , n − 1.

Equivalently, CAn gives a parameterization of degree n monic Casas-Alvero polynomials
by their roots.
A simple yet key observation is, there would exist a two-dimensional linear subvariety
{c(x1, . . . , xn)+d(1, . . . , 1)|c, d ∈ C} ⊂ CAn, if (x1, . . . , xn) ∈ CAn with not all coordinates
identical. Hence if we can show CAn is of dimension one, then such points do not exist
and the conjecture follows. Now we can equivalently formulate the conjecture as follows

Theorem 1.1. dimC CAn = 1, ∀n ≥ 1.
 1

2 ZHIPENG LU

Since Fi’s with high degrees are cumbersome for computation, we study the branches
deﬁned by ⟨f (1)(xi1), · · · , f (n−1)(xin−1)⟩. These branches as algebraic varieties, though
should be of signiﬁcant interest, seem not well studied in classical literature. In this paper
we will try to describe some essential properties of these varieties. Especially we prove
the Casas-Alvero conjecture by establishing the following:

Theorem 1.2. For f = (x − x1)(x − x2) · · · (x − xn) as a polynomial in K[x, x1, . . . , xn]
for ﬁeld K = C or of characteristic large enough (≫ n!), deﬁne the derivative polyno-
mial f (i)(xj) as a degree n − i polynomial in K[x1, . . . , xn] for any 0 ≤ i, j ≤ n. Then
dim Z(f (1)(xi1), . . . , f (n−1)(xin−1)) = 1, for arbitrary 1 ≤ i1, . . . , in−1 ≤ n.

Moreover, the above result on branches of Casas-Alvero variety CAn can be generalized
to varieties deﬁned by n − 1 arbitrary derivative polynomials.

Theorem 1.3. With notations as above, for any n − 1 arbitrary distinct pairs (ik, jk) with
1 ≤ ik ≤ n and 1 ≤ jk ≤ n − 1, k = 1, . . . , n − 1, dim Z(f (j1)(xi1), . . . , f (jn−1)(xin−1 )) = 1.

For example, dim Z(f (n−1)(x1), . . . , f (n−1)(xn−1)) = 1 simply due to

f (n−1)(xi) − f (n−1)(xj) = (n − 1)(xi − xj), ∀1 ≤ i, j ≤ n.

Since polynomial rings are Cohen-Macaulay, the above theorem is equivalent to the fact
that any n − 1 distinct derivative polynomials form a regular sequence. In the following
sections, we will ﬁrst examine some easy cases of Theorem 1.2 by Taylor expansions. Then
to deal with general cases we introduce a model theoretic approach based on tools from
computational algebraic geometry including ﬁnite Nullstellensatz, combinatorial Nullstel-
lensatz and some explicit forms of Noether normalization.

Acknowledgement. The author is supported by Harald Helfgott’s Humboldt Professor-
ship.
 2. General reductions and special cases

We give evidence of Theorem 1.2 by proving the case of identical branches as follows.

Lemma 2.1. For any n ≥ 1, 1 ≤ k ≤ n and a ﬁeld K with char(K) = 0 or char(K) > n!,
dim Z(Ik) = 1, where Ik := ⟨f (1)(xk), . . . , f (n−1)(xk)⟩.

Proof. By Taylor’s expansion

f (xj) =f (xk) + f (1)(xk)(xj − xk) + . . .

+ 1
(n − 1)! f (n−1)(xk)(xj − xk)
n−1 + n!
n!(xj − xk)
n.

Then by f (xj) = f (xk) = 0 we have

(xj − xk)
n ∈ Ik, or (xj − xk) ∈ rad(Ik),

where rad(I) denotes the radical ideal of I. Hence

rad(⟨f (1)(xk), . . . , f (n−1)(xk)⟩) = ⟨xk − x1, · · · , xk − xn⟩

and the proposition follows. □

THE CASAS-ALVERO CONJECTURE IN COMPUTATIONAL ALGEBRAIC GEOMETRY 3

Slightly generalizing the above method, we can prove that the branch deﬁned by the
ideal Ij,l,k := ⟨f (1)(xk), . . . , f (j−1)(xk), f (j)(xl), f (j+1)(xk), . . . , f (n−1)(xk)⟩ always has di-
mension one for any 1 ≤ j ≤ n − 1 and 1 ≤ k ̸= l ≤ n. First, by Taylor’s expansion,

f (j)(xl) =f (j)(xk) + 1
1! f (j+1)(xk)(xl − xk) + . . .(1)
 + 1
(n − j − 1)! f (n−1)(xk)(xl − xk)
n−j−1 + n!
(n − j)! (xl − xk)
n−j.

We may kill the last term by combining it with the following expansion

0 = f (xl) =f (xk)(= 0) + f (1)(xk)(xl − xk) + . . .(2)
 + 1
(n − 1)! f (n−1)(xk)(xl − xk)
n−1 + n!
n! (xl − xk)
n.

Subtracting (2) multiplied by n!
(n−j)! (xl − xk)j from (1) gives

n!
(n − j)! (xl − xk)
jf (j)(xk) ∈ Ij,l,k.

For any prime ideal p ⊃ Ij,l,k we have either f (j)(xk) ∈ p or xl − xk ∈ p. If the lat-
ter happens, then f (j)(xk) ∼ f (j)(xl) ∼ 0 mod p. Thus f (j)(xk) ∈ p anyway, so that
f (j)(xk) ∈ ∩p⊃Ij,l,kp = rad(Ij,l,k), the radical ideal of Ij,l,k. This proves the following

Corollary 2.2. With the notations above, Z(Ij,l,k) = Z(Ik).

However, the same method applied to general branches does not directly give results
as well. For a general branch deﬁned by ⟨f (1)(xi1), · · · , f (n−1)(xin−1)⟩, we can write each
f (j)(xij ) as of (1) and kill the last terms by subtracting (2) similarly, so that we get a
system of n − 1 equations with (xij − xk)jf (j)(xij ) on the left hand side and expansions
involving f (1)(xk), . . . , f (n−1)(xk) on the right for any chosen 1 ≤ k ≤ n. Then by Gauss
elimination over C[x1, . . . , xn] we get

Fjf (j)(xk) ∈ ⟨f (1)(xi1 ), · · · , f (n−1)(xin−1 )⟩, ∀1 ≤ j ≤ n − 1,

where Fj is a polynomial in (xk − xi1), . . . , (xk − xin−1). If there are at least three distinct
indexes among i1, . . . , in−1, we can not conclude that f (j)(xk) all belong to the radical of
⟨f (1)(xi1), · · · , f (n−1)(xin−1)⟩ as we did in the proof of Corollary 2.2. For instance, if all
ij’s are distinct, then each Fj is a product of all (xk − xi1), . . . , (xk − xin−1) (with powers),
from which we can only conclude that (xk − xil) belongs to the radical for some il.
This prompts us to introduce new methods to deal with general branches. We start by
making the ﬁrst reduction using the Lang-Weil bound and a form of local-global principle.

Proposition 2.3. Suppose for any n ≥ 1 and large enough prime p ≫ n we have, over
Fp, Z(f (1)(xi1), · · · , f (n−1)(xin−1)) is of size p, for any branch. Then Theorem 1.2 (hence
the Casas-Alvero conjecture) holds for n and vice versa.

Proof. First, clearly CAn is deﬁned over any ﬁnite ﬁeld Fp. Then viewed as a variety over
Fp, we have by Lang-Weil bound (see Corollary 4 of [8]),

|CAn(Fp)| = (c(CAn(Fp)) + O(p−1/2))pdim(CAn(Fp)),

4 ZHIPENG LU

where c is the number of top-dimensional components of CAn and dim denotes for Krull
dimension. By hypothesis of the proposition, we have |CAn(Fp)| = p for all large enough
p. Then
 c(CAn(Fp)) = 1, and dim(CAn(Fp) = 1.

Particularly CAn is irreducible.
Second, we look at the structure morphism π : CAn(Z) −→ Spec Z, which is clearly of
ﬁnite presentation. Since we know that

{p ∈ Spec Z | dim CAn(Fp) = 1}

is an open set in Spec Z hence contains the generic point 0, i.e. dim CAn(Q) = 1. Then
by Proposition 2.7 in Chapter 3 of [7], dim CAn(Q) = 1. Further by Lefschetz principle
(see [1] for reference), dim CAn(C) = 1.
Conversely, if the Casas-Alvero conjecture stands, then

1 = dim CAn(Q) = dim CAn(Fp),

for all but ﬁnite primes p. Hence CAn(Fp) is a line and |CAn(Fp)| = p. □

The above reduction may be also stated in a lame language as follows. First, we may
only need to prove it over Q, because if otherwise dimQ(CAn) > 1 then similarly by
Proposition 2.7 in Chapter 3 of [7] dimC(CAn) > 1. Then essentially we need only to
prove it over Z, because if f (x) = (x − x1) · · · (x − xn) with all xi ∈ Q, by multiplying
the least common multiple of the denominators, we may assume that the roots are all
integers. Hence the conjecture is equivalent to for any branch

Proposition 2.4. For any branch Z(f (1)(xi1), · · · , f (n−1)(xin−1)) over C,

Z(f (1)(xi1), · · · , f (n−1)(xin−1 )) ∩ Zn = {(a, · · · , a) | a ∈ Z}.

Then we can further reduce it to modulo primes p, or even any ﬁnite integers as follows.

Proposition 2.5. If for any Casas-Alvero polynomial f (x) = (x − x1) · · · (x − xn) with
xi ∈ Z, there is some integer m ≥ 2 such that x1 ≡ x2 ≡ · · · ≡ xn (mod m), then Theorem
1.2 (hence the Casas-Alvero conjecture) holds for n.

Proof. Suppose xi are not all equal. Translating by adding an identical integer on each
coordinate, we may assume xi’s to be non-negative. By the hypothesis we have x1 ≡ x2 ≡
· · · ≡ xn ≡ l (mod m) for some m ≥ 2 and 0 ≤ l < m. Let xi,1 = (xi − l)/m, ∀i = 1, · · · , n,
then f1(x) := (x − xi,1) · · · (x − xn,1) is again a degree n Casas-Alvero polynomial having n
integer roots not all equal. Then again we have some m1 ≥ 2 such that x1,1 ≡ x2,1 ≡ · · · ≡
xn,1 ≡ l1 (mod m1) for some m1 ≥ 2 and 0 ≤ l1 < m1 and we can do the similar aﬃne
transform to get another degree n Casas-Alvero polynomial having n integer roots not all
equal. Clearly, this process gives an inﬁnite descent for the integers x1, · · · , xn, which is
impossible for ﬁnite non-negative integers. This contradiction implies the conjecture. □

In fact, we will prove for any n ≥ 1, all large enough prime p make the hypothesis of
Proposition 2.5 valid. This is done in section 4 based on further computational algebro-
geometric reduction.

THE CASAS-ALVERO CONJECTURE IN COMPUTATIONAL ALGEBRAIC GEOMETRY 5

3. Standard monomials, finite Nullstellensatz and Noether normalization

This section contributes to introducing some necessary computational notions and re-
sults. We ﬁrst deﬁne a standard order on monomials.

Deﬁnition 3.1 (Lexicographic order). α >lex β if the leftmost nonzero entry of α − β is
positive, for any α = (α1, · · · , αn), β = (β1, · · · , βn) ∈ Nn.

Deﬁnition 3.2 (Graded lexicographic order). Let α, β ∈ Nn. α >grlex β if

n∑

i=1 αi >
 n∑

i=1 βi, or
 n∑

i=1 αi >
 n∑

i=1 and α >lex β.

N

Deﬁnition 3.3. We deﬁne a monomial order on the set of monomials T = {xα1
1 · · · xαn
n |
αi ∈ N} ⊂ k[x1, · · · , xn] for any ﬁeld k by

xα > xβif α >grlex β, ∀α, β ∈ Nn.

It is a total well-ordering on T satisfying
(1) 1 ≤ t, ∀t ∈ T ;
(2) t1 · s ≤ t2 · s, ∀t1, t2, s ∈ T if t1 ≤ t2.

Deﬁnition 3.4 (Leading coeﬃcient, monomial and term). Let f = ∑α aαxα be a nonzero
polynomial in k[x1, · · · , xn] and > the monomial order as above. The multidegree of f is
deﬁned as multideg(f ) = max
> {α ∈ Nn | aα ̸= 0}.

Then the leading coeﬃcient of f is LC(f ) = amultideg(f ), the leading monomial is LM (f ) =
xmultdeg(f ) and the leading term of f is LT (f ) = LC(f ) · LM (f ).

Deﬁnition 3.5 (Ideal of leading monomials, leading terms). Let I be an ideal in k[x1, · · · , xn]
and ﬁx the monomial order on T . The ideal of leading monomials of I, ⟨LM (I)⟩, is the
ideal generated by the leading monomials of all polynomials in I. The ideal of leading
terms of I, ⟨LT (I)⟩, is the ideal generated by the leading terms of all polynomials in I.

Proposition 3.6 (Multivariate division principle). For a ﬁxed monomial order and poly-
nomials g1, · · · , gk in k[x1, · · · , xn], any g ∈ k[x1, · · · , xn] can be written as

g = a1g1 + · · · + akgk + r

where ai, r ∈ k[x1, · · · , xn] and either r = 0 or r is a linear combination of monomials not
divisible by any of LT (g1), · · · , LT (gk).

Now we are ready to introduce

Deﬁnition 3.7 (Standard Monomials). The set of standard monomials of any ideal J is

SM (J) = {xα | xα /∈ ⟨LM (J)⟩}.

Usually standard monomials are deﬁned together with a Gr¨obner basis but we do not
need such notion in our later application. We need the following results over ﬁnite ﬁelds.

Proposition 3.8 (Nullstellensatz over ﬁnite ﬁelds). For any ideal J ⊂ Fq[x1, · · · , xn], its
radical ideal is √J = J + ⟨xq
1 − x1, · · · , xq
n − xn⟩.

6 ZHIPENG LU

See proof of Theorem 3.1.2, [4]. Also

Proposition 3.9 (Theorem 3.2.4 of [4]). Let J ⊂ Fq[x1, · · · , xn] be any ideal and √J =
J + ⟨xq
1 − x1, · · · , xq
n − xn⟩. Then
 |SM (
√J)| = |V (J)|.

In addition, the following two explicit forms of Noether normalization theorem are
signiﬁcant to our applications.

Proposition 3.10 (Theorem 3.4.1 of [5]). Let K be a ﬁeld and I ⊂ K[x1, . . . , xn] be an
ideal. Then there exist an integer s ≤ n and an isomorphism ϕ : K[x1, . . . , xn] → A :=
K[y1, . . . , yn], such that:
(1) the induced morphism K[ys+1, . . . , yn] → A/ϕ(I), yi ↦→ yi mod ϕ(I) is injective
and ﬁnite.
(2) Moreover, ϕ can be chosen such that, for j = 1, . . . , s, there exist polynomials

gj = yej
j +
 ej−1∑

k=0 ξj,k(yj+1, . . . , yn) · yk
j ∈ ϕ(I)

satisfying ej ≥ deg(ξj,k) + k for k = 0, . . . , ej − 1.
(3) If I is homogeneous then gj can be chosen to be homogeneous too.
(4) If K is inﬁnite then ϕ can be chosen to be linear, i.e. ϕ(xi) = ∑j mijyj with
(mij) ∈ GLn(K).

Proposition 3.11 (Theorem 3.5.1 (6) of [5]). Let K be a ﬁeld, I ⊂ A = K[x] be an
ideal and u ⊂ x = {x1, . . . , xn} be a subset such that I ∩ K[u] = 0, then dim(A/I) ≥ #u.
Furthermore, there exists some u ⊂ x with I ∩ K[u] = 0 and dim(A/I) = #u.

4. Casas-Alvero conjecture over Q

In this section, we verify the hypothesis of Proposition 2.5 modulo large primes p, i.e.
over a ﬁnite ﬁeld Fp, through speciﬁcally realizing Noether normalization as of Proposition
3.10. To organize calculation, we use the following notation (so called Hasse derivative):

Hi(xk) = ∑

1≤j1<···<jn−i≤n(xk − xj1) · · · (xk − xjn−i), 1 ≤ i ≤ n − 1, 1 ≤ k ≤ n.

If f (x) = (x − x1) · · · (x − xn) = xn + an−1xn−1 + · · · + a1x + a0, its i−th Hasse derivative
is just:

(3) Hi(x) = (n
i
 )xn−i + (n − 1
i
 )an−1xn−1−i + · · · + (
i
i
)ai = 1
i! f (i)(x).

We ﬁrst deal with a special case of Theorem 1.2, i.e. the branches deﬁned by H1(xi1), . . . ,
Hn−1(xin−1) with i1, . . . , in−1 distinct. We call them the main branches. By symme-
try, they are all isomorphic to the one deﬁned by H1(xn−1), . . . , Hn−1(x1). Let J =
⟨H1, · · · , Hn−1⟩ with Hi := Hn−i(xi) and p be some suﬃciently large prime which we will
specify later. By Proposition 3.9, to verify the hypothesis of Proposition 2.5 for m = p,
we need

THE CASAS-ALVERO CONJECTURE IN COMPUTATIONAL ALGEBRAIC GEOMETRY 7

Proposition 4.1.
 |V (J)| = |SM (J + ⟨xp
1 − x1, · · · , xp
n − xn⟩)| = p,

which are all deﬁned over Fp, for some suﬃciently large p.

Obviously we have V (J) ⊃ {(a, a, · · · , a) ∈ Fn
p | a ∈ Fp}. So if we can show |V (J)| = p
for all suﬃciently large p, then this obvious subset with p elements must be V (J) itself.
By Proposition 2.5 we essentially need only to ﬁnd one such “good” prime p.
The proof of Proposition 4.1 relies on information of general Gr¨obner bases of J + ⟨xp
1 −
x1, · · · , xp
n − xn⟩. Here are some examples for small n.

Example 4.2. For n = 1, J = 0 is trivial and we can choose G = {xp
1 − x1} for any p.
Hence SM (G) = {1, x1, · · · , xp−1
1 } with cardinality p.
For n = 2, J = ⟨x1 − x2⟩, and we can choose G(J + ⟨xp
1 − x1, xp
2 − x2⟩) = {x1 −
x2, xp
2 − x2} for any p. Hence the missing monomials from ⟨LM (G)⟩ consist in SM (G) =
{1, x2, · · · , xp−1
2 }, again with cardinality p.
For n = 3, J = ⟨H1 = 2x1 − x2 − x3, H2 = (x2 − x1)(x2 − x3)⟩, we have

x1 = 1
2 (x2 + x3) mod ⟨H1⟩,

H2 = (x2 − 1
2 (x2 + x3)
) (x2 − x3) mod ⟨H1⟩

= 1
2 (x2 − x3)
2 mod ⟨H1⟩ =⇒ (x2 − x3)
2 ∈ J

=⇒ (x2 − x3)
p ∼ x2 − x3 ∈ J + ⟨xp
1 − x1, · · · , xp
n − xn⟩
hence we can choose G(J + ⟨xp
1 − x1, xp
2 − x2, xp
3 − x3⟩) = {x1 − x2, x2 − x3, xp
3 − x3} for any
odd p (so that 1/2 makes sense). Thus SM (G) = {1, x3, · · · , xp−1
3 } again with cardinality
p. For n = 4, we similarly get G = {x1 − x4, x2 − x4, x3 − x4, xp
4 − x4} for p > 7. Again
|SM (G)| = p.

These simple cases can all be computed by hand. However, the complexity of computing
these Gr¨obner bases exponentially increases along with the number of variables. For
simpliﬁcation, we show that Proposition 4.1 can be further reduced as follows.

Proposition 4.3. |V (J)| = p ⇔ |V (J)| < p2.

Proof. If there exists A = (a1, · · · , an) ∈ V (J) with coordinates not all equal, then
V (J) ⊃ span⟨(1, · · · , 1), A⟩ forms a two dimensional subspace, i.e. |V (J)| ≥ p2. The
other direction goes by the same observation. □

The above arithmetic reduction can be resolved by attaining a more computationally
manageable goal as follows.

Proposition 4.4. If for each k ∈ {1, · · · , n − 1}, there is an integer mk ≥ 1 such that
xmk
k ∈ LM (J), then for any p ≫ m1 · · · mn−1, |V (J)| < p2.

Proof. By the condition, if xα = xα1
1 · · · xαn
n /∈ LM (J) then αk < mk, k = 1, · · · , n − 1.
Thus we have

|SM (J + ⟨xp
1 − x1, · · · , xp
n − xn⟩)| ≤ m1 · · · mn−1p < p2, ∀p ≫ m1 · · · mn−1.
 □

8 ZHIPENG LU

We will see later that p is also conﬁned by the structural coeﬃcients depending on n in
derivation of the leading monomials xmk
k . With the last reduction by Proposition 4.4, in
case of main branches we need to prove

Proposition 4.5. For each k = 1, · · · , n − 1, n ≥ 3, there is an integer mk ≥ 1 s.t.
xmk
k ∈ LM (J), with J = ⟨H1, . . . , Hn−1⟩ (Hi = Hn−i(xi)) an ideal in Q[x1, · · · , xn].

The theorem suﬃces for proving Proposition 4.4 since the algorithm of obtaining those
leading terms involves fractions only depending on n and performs identically over Fp for
p suﬃciently larger than n and all denominators of the structural coeﬃcients used. Before
proving the theorem, we study some examples for small k ≤ n.

Example 4.6. Suppose n ≥ 4. For k = 1, H1 = (n − 1)x1 − (x2 + · · · + xn) gives a linear
relation between all the variables and x1 ∈ LM (J), so that we can always set m1 = 1.
For k = 2, replacing x1 by − 1
n−1(x2 + · · · + xn), we get

H2(x2) = G2x2
2 + G1x2 + G0 mod ⟨H1⟩,(4)

with G2, G1, G0 homogeneous polynomials in x3, · · · , xn, of degrees 0, 1, 2 respectively. We
can compute explicitly that

G2 = 1
n − 1 (n − 2)
2 + (n − 2
2
 ) = (n − 2)(n2 − 2n − 1)
2(n − 1) ̸= 0.

Thus we can always set m2 = 2.
Next, we show that m3 can always be set to 8. We still replace x1 by − 1
n−1 (x2 +· · ·+xn)
in H3 to get H3 = K2x2
2 + K1x2 + K0 mod ⟨H1⟩,
with K2, K1, K0 homogeneous polynomials in x3, · · · , xn, of degrees 1, 2, 3 respectively.
Using (4) we can kill x2
2 and get

H3 = L1x2 + L0 mod ⟨H1, H2⟩,

with L1, L0 homogeneous polynomials in x3, · · · , xn, of degrees 2, 3 respectively. Now to
kill x2 in H3 we need a non-linear cancellation aside with (4) as follows:

H 2
3 = L2
1x2
2 + 2L1L0x2 + L2
0
= L′
1x2 + L′
0 mod ⟨H1, H2⟩,

with L′
1, L′
0 homogeneous polynomials in x3, · · · , xn, of degrees 5, 6 respectively. Then

L1H 2
3 − L′
1H3 = L′′
0 mod ⟨H1, H2⟩,

with L′′
0 = L1L′
0 − L′
1L0 a homogeneous polynomial in x3, · · · , xn of degree 8. By carrying
out the detailed calculation we ﬁnd LM (L′′
0) = x8
3.

The above example inspires us to consider general higher order non-linear cancellations
likewise. Thus we introduce some extra notions besides those deﬁned in section 3, in that
we need to write down the coeﬃcients of the Hasse derivatives more explicitly.
Let [n] denote the chain (1 < 2 < · · · < n). If c = (j1 < · · · < jt), we say c is
a chain of length t, denoted by l(c) = t. By c ≤t [n] we indicate that c is a length t
sub-chain of [n]. We may also use c to denote a multichain (j1 ≤ j2 ≤ · · · ≤ jt) and
α(c) = (α(c)1, . . . , α(c)n) to denote its occurrence vector with the part j occurring α(c)j
times in c. Then l(c) = |α(c)| is the total number of occurrences and if no confusion

THE CASAS-ALVERO CONJECTURE IN COMPUTATIONAL ALGEBRAIC GEOMETRY 9

c ≤t [n] is a multichain with l(c) = t and all its parts belonging to [n]. For short, j ∈ c
means j occurs in c. Also, by c1 + c2 we mean a derived multichain (or chain) from two
multichains by collecting their parts into one.
For any vectors α, β ∈ Nn we deﬁne (β
α) := (β1
α1) · · · (βn
αn). The number of sub-multichains

c′ ≤ c with α(c′) = α prescribed is (α(c)
α ), which is also valid if α is not comparable with
α(c) since then (α(c)
α ) vanishes. In addition, α ≼ β means αj ≤ βj, j = 1, . . . , n. Clearly
(β
α
) > 0 if and only if α ≼ β.
Now direct computation on the Hasse derivative yields

H m
n−i(xk) =
 

 ∑

c≤i[n]
 ∏

j∈c(xk − xj)




m
 = ∑

c1,...,cm≤i[n]
 ∏

j∈c1+···+cm(xk − xj)(5)
 = ∑

c1,...,cm≤i[n]
 ∑

c≤c1+···+cm(−1)
l(c)(α(c1) + · · · + α(cm)
α(c)
 )
xα(c)xim−l(c)
k

= ∑

c1,...,cm≤i[n]
 ∑

α≼α(c1+···+cm)(−1)
|α|(α(c1 + · · · + cm)
α
 )
xαxim−|α|
k

= ∑

α∈Nn(−1)
|α| ∑

c1,...,cm≤i[n]
 (α(c1 + · · · + cm)
α
 )xαxim−|α|
k

= ∑

0<(α1,...,αk−1,0,...,0)=α≼(m,...,m) xαhα,m + (n
i
 )mxim
k + rikm,

where for short 0 = (0, . . . , 0) and rikm summons the remaining terms with xα < xim
k . For
any α = (α1, . . . , αk−1, 0, . . . , 0) with αj ≤ m, i.e. xα ≥ xim
k , the leading term LT (hα,m)
appears as

(−1)
|α| ∑

c1,...,cm≤i[n],α(cj)k=0
 (α(c1 + · · · + cm)
α
 )xim−|α|
k = Cα,i(m)xim−|α|
k ,

noting that the terms with αk ̸= 0 sum up to zero. It is worth to mention the easy
observation that for any two symmetric vectors α = σ · α′, i.e. α can be obtained by
permuting the coordinates of α′ using some σ ∈ Sk−1, we always have Cα,i(m) = Cα′,i(m).
Conversely one easily checks that identical columns corresponds to symmetric α’s.
Clearly those leading coeﬃcients Cα,i(m) do not vanish. If α ≼ α′, then the multichains
c with α′ ≼ α(c) also satisfy α ≼ α(c) whence |Cα,i(m)| ≥ |Cα′,i(m)|. Thus Cα,i(xk)
attains maximum only when α = 0 which is

C0,i(m) = ∑

c1,...,cm≤i[n],α(cj)k=0
 (α(c1 + · · · + cm)
0
 ) = (n − 1
i
 )m,

i.e. the coeﬃcient of xim
k . The minimum is attained when α1 = · · · = αk−1 = m which is
(n−k+1
i−k+1)m (vanishes if i < k − 1).
The above expression of Cα,i(m) is equivalent to using the multivariate Fa`a di Bruno’s
formula noting that Cα,i(m) is nothing but a multiple of ∂xim

∂xα1
1 ···∂xαk−1
k−1 ∂xim−|α|
k H m
n−i(xk).

10 ZHIPENG LU

However, a computationally more accessible formula is given by the following Combina-
torial Nullstellensatz as of [6].

Proposition 4.7. For any f ∈ K[x1, . . . , xn] of degree |α| over an arbitrary ﬁeld K, the
coeﬃcient of xα in f has the following expression:

[xα]f (x1, . . . , xn) = ∑

bj∈Aj
 f (b1, . . . , bn)
ϕ′
1(b1) · · · ϕ′
n(bn) ,

where Aj ⊂ K are any subsets of size αj + 1 and ϕj(x) = ∏b∈Aj (x − b).

If we choose Aj = {0, 1, . . . , αj} for j ≤ k − 1 and Ak+1 = · · · = An = {0}, the above
Nullstellensatz promises

(6) Cα,i(m) = ∑

bj ≤αj
 (H m
n−i(xk)
) (b1, . . . , bk−1, 1, 0, . . . , 0)
∏k−1
j=1 ∏bj ̸=b≤αj (bj − b) .

More signiﬁcantly, it implies the following arithmetic on Cα,i(m) which is crucial to our
later proof.

Lemma 4.8. Keep notations above and gather α = (α1, . . . , αk−1, 0, . . . , 0) ∈ Nn with
αj ≤ mj ∈ Z+, j = 1, . . . , k − 1, no two of which can be identiﬁed by permuting their ﬁrst
k − 1 coordinates. Denote by N the number of such vectors. Then for any M ∈ N, the N
by N square matrix (Cα,i(m)) with M + 1 ≤ m ≤ M + N is non-degenerate.

Proof. For j ≤ k − 1, choose Aj = {bj,0, . . . , bj,mj } ⊂ Q of mj + 1 numbers, such that
the values Hn−i(b1, . . . , bk−1, 1, 0, . . . , 0) ̸= 0 are all distinct for diﬀerent (b1, . . . , bk−1) ∈
A1 × · · · × Ak−1. (This is possible since the condition deﬁnes an open subset of Qk−1.)
Now following the Combinatorial Nullstellensatz, we can write

(Cα,i(M + l)) = (
H M +l
n−i (b1, . . . , bk−1, 1, 0, . . . , 0)
) (Φα) ,

where (H M +l
n−i (b1, . . . , bk−1, 1, 0, . . . , 0)
)
1≤l≤N,bj∈Aj =: H is an N by (m1 +1) · · · (mk−1+1)

matrix, and (Φα) is a matrix of N columns. Here corresponding to the formula of (6), for
each α, Φα = (φα
b1,...,bk−1) is designated to produce Cα,i(M + l) by multiplying the l-th row

of H for any l ≤ N . Thus φα
b1,...,bk−1 = 1
ϕ′
α,1(b1) · · · ϕ′
α,k−1(bk−1) for bj ranging from bj,0 to

bj,αj , otherwise φα
b1,...,bk−1 = 0, in which ϕα,j(x) = ∏αj
r=0(x − bj,r).
By our choice of Aj and noting that the number of columns of H is generally larger than
N , any N by N minor sub-matrix of H is a Vandermonde matrix, hence H has rank N .
If we can show (Φα) also has rank N , then (Cα,i(M + l)) is non-degenerate (of rank N ).
Suppose there exists linear dependence: ∑ fαΦα = 0. Pick all the columns with fα ̸= 0
and ﬁnd all the maximal ones among them along ≺ which are all unique. Say β is maximal,
then its (lowest) entry in the row indexed by β1, . . . , βk−1 is the only nonzero entry in this
row among all the picked columns, hence fβ must be zero, a contradiction. □

Remark 1. Employing generalized Vandermonde matrices, the matrix (Cα,i(m)) may
be shown non-degenerate for cases where N positive integers m are not necessarily con-
secutive. Also note that the hypothesis on symmetry is restricted to α with αj ≤ mj. For
example, if m1 = 2, m2 = 4, then x2
1x3
2 is not symmetric to x3
1x2
2 since the latter is not in
our consideration.

THE CASAS-ALVERO CONJECTURE IN COMPUTATIONAL ALGEBRAIC GEOMETRY 11

Proof of Proposition 4.5. Let Jk = ⟨H1, · · · , Hk⟩, 1 ≤ k ≤ n − 1. We want to show by
induction, for all k ≤ n − 1 Jk contains homogeneous polynomials g1, · · · , gk with leading
terms LT (gi) = xmi
i for some mi ≥ 1, i = 1, · · · , k, and gi’s are symmetric in xi+1, · · · , xn,
i.e. gi = xmi
i + ami−1xmi−1
i + · · · + a0 with al ̸= 0 being symmetric in xi+1, · · · , xn for
l ≤ mi − 1. Note that we can always set m1 = 1, m2 = 2, m3 = 8 by Example 4.6.
Assuming the cases for 1 ≤ k − 1 (≤ n − 2) we need to verify it for k. Let mk−1 =
(m1, · · · , mk−1, 0, · · · , 0) ∈ Nn. By (5) we write for any m ∈ Z+

H m
k = ∑

α=(α1,...,αk−1,0,...,0)>(0,...,0) xα1
1 · · · xαk−1
k−1 hα,m + (n
k
)mxkm
k + rm,

where rm collects the monomials smaller than xkm
k in lexicographic order. For any term
with α ≥ mk−1, say αi ≥ mi for some i ≤ k − 1, we can replace xαi
i by xαi−mi
i (gi − xmi
i )
when modulo Jk−1. Since gi is symmetric in xk, . . . , xn, gi − xmi
i can not have xmi
k as
leading monomial. Thus the replacement does not aﬀect xkm−|α|
k as the leading monomial
of hα,m by (5). After all such replacements until there is no αi ≥ mi for any i ≤ k − 1,

(7) H m
k = ∑

(0,...,0)<α≺mk−1 xαh
′
α,m + (
n
k
)mxkm
k + rm mod Jk−1,

where each h′
α,m is symmetric in xk, . . . , xn and LM (h′
α,m) = LM (hα,m) = xkm−|α|
k . Recall
that ≺ denotes for each coordinate of the left vector being zero or strictly less than that
of the right respectively.
Now similar to Gaussian elimination, by row reduction we may kill the terms with those
α, i.e. by performing

h
′
α′,m1H m2
k − h
′
α′,m2H m1
k

= ∑ xα (
h
′
α′,m1h
′
α,m2 − h
′
α′,m2h
′
α,m1)

+ h
′
α′,m1
 ((n
k
)m1ixkm2
k + rm2
) − h
′
α′,m2
 ((n
k
)m11xkm1
k + rm1
)

to kill the term with α′ in H m2
k (modulo the ideal Jk−1). Note that h′
α′,m1h′
α,m2 and

h′
α′,m2h′
α,m1 have identical leading monomial xk(m1+m2)−|α′|−|α|
k for α ̸= α′. Suppose their
leading coeﬃcients do not coincide, we can proceed likewise to kill terms with α2 and so
on until αt is killed if possible, and we are done with the proof.
In the process, the Gaussian elimination of leading terms is equivalent to that of leading
coeﬃcients Cα(m), which leads us to study the matrix C = (Cα(m))m∈N. Note that if
α′ and α are symmetric, their corresponding columns are identical so that the matrix
becomes degenerate. However, any row reductions performed on the two columns are also
identical. Thus if one is killed so is the other. This suggests what we should really study
is the matrix ˜C := Sn\C, i.e. the symmetric (identical) columns of C are assimilated.
Then ˜C ﬁts to the hypothesis of Lemma 4.8, and its full minors of consecutive rows have
full rank so that the Gauss elimination is promised to kill all terms with α ≺ mk−1 for
rows with large enough indexes m. Choose the smallest such m as mk and resulted H mk
k
as gk (uniformed to be monic if necessary). The symmetry of gk in xk+1, . . . , xn is due to
that of Hk. Hence we are done with the induction step and the theorem follows. □

12 ZHIPENG LU

Remark 2. For p larger than the denominators of any multipliers used in the Gauss
elimination, the proof works over Fp as well to establish Proposition 4.4. Our algorithm
is a specialization of Noether normalization as in Proposition 3.10.

By symmetry of roots, for any main branch with distinct indexes i1, · · · , in−1, the same
proof above works for the alphabetical order xi1 > xi2 > · · · > xin−1 > xj in which
{j} = {1, · · · , n} ∖ {i1, · · · , in−1}.

Corollary 4.9. For any J = ⟨Hn−1(xi1), · · · , H1(xin−1 )⟩ with i1, · · · , in−1 all distinct,
there exist mk ∈ Z+ such that xmk
ik ∈ LM (J) over Q, for k = 1, · · · , n − 1.

This proves Theorem 1.2 for all main branches. Under the rearranged alphabetical
order, the proof of Proposition 4.5 works regardless of choice of derivatives, i.e.

Corollary 4.10. For any 1 ≤ j1 < · · · < jk ≤ n − 1 and 1 ≤ i1, . . . , ik ≤ n distinct, there
are ml ∈ Z+, l = 1, . . . , k such that xml
il ∈ LM (⟨Hn−j1(xi1 ), . . . , Hn−jk (xik )⟩) over Q.

Complying with Proposition 3.11, we have ⟨Hn−j1(xi1), . . . , Hn−jk(xik )⟩ ∩ Q[u] = 0 for
u = {x1, . . . , xn} ∖ {xi1, . . . , xik }. Hence by Cohen-Macaulayness,

ht(⟨Hn−j1(xi1), . . . , Hn−jk (xik )⟩) = n − dim(Q[x1, . . . , xn]/I) = n − (n − k) = k,

where ht() denotes the height of an ideal. In other words, Hn−j1(xi1 ), . . . , Hn−jk(xik ) form
a regular sequence which also follows from Corollary 4.9.
For general branches deﬁned by J = ⟨Hn−1(xi1), · · · , H1(xin−1 )⟩ with i1, . . . , in−1 not
necessarily distinct, we may still obtain results as of Corollary 4.9 through linearized
Noether normalization as (4) of Proposition 3.10. If the number of distinct indexes oc-
curring is k ≤ n − 1, by symmetry we may assume {i1, . . . , in−1} = {1, . . . , k} so that our
algorithm in the proof of Proposition 4.5 proceeds as well. By Corollary 4.10 we obtain
xm1
1 , . . . , xmk
k ∈ LM (J), say by working on the sub-ideal J0 = ⟨Hn−j1(x1), . . . , Hn−jk(xk)⟩.
For u0 = {k + 1, . . . , n} we have J0 ∩ Q[u0] = 0 and ht(J0) = k.
Let l0 = {j1, . . . , jk}. For any j /∈ l0, if we can show that the intersection between
J1 = J0 + ⟨Hn−j(xij )⟩ and Q[u0] is not zero, then by Proposition 3.11, ht(J1) = k + 1 and
J1 ∩ Q[u1] = 0 for some u1 ⊂ u0 of size n − k − 1. Applying Proposition 3.10 (modulo an
isomorphism) we are guaranteed to have for some ik+1 ∈ u0 such that xmk+1
ik+1 ∈ LM (J1).
Subsequently update l1 := l0 ∪ {j} and J2 := J1 + ⟨Hn−j′(xij′ )⟩ for any j′ /∈ l1. By
further investigating J1 ∩ Q[u1], we may determine whether the height of J2 grows. If
each iteration of the process raises the height by one, at the end we may conclude that
ht(J) = n − 1. We consolidate this hypothetical procedure using Lemma 4.8 as follows.

Proposition 4.11. Any ideal J = ⟨Hn−1(xi1), · · · , H1(xin−1 )⟩ has ht(J) = n − 1. Con-
sequently dim Z(J) = 1 and Theorem 1.2 follows.

Proof. With the notations above, we verify that ht(J1) ∩ Q[u0] ̸= 0. Applying Lemma
4.8 to α = (α1, . . . , αk, 0, . . . , 0) ∈ Nn with conﬁnement, we see that (Cα,j(m)) is non-
degenerate, for M < m ≤ M + N with M ∈ Z+ large enough and N being the number of
α which are not symmetric to each other. Write H m
n−j(xij ) in the form below

(8) H m
n−j(xij ) = ∑

(0,...,0)<α≺(m1,...,mk,0,...,0) xαhα,m + rm mod J0,

where hα,m and rm are polynomials symmetric in u0. Then we similarly kill the terms
only involving xi1, . . . , xik by Gauss elimination. After the elimination, the residue terms

THE CASAS-ALVERO CONJECTURE IN COMPUTATIONAL ALGEBRAIC GEOMETRY 13

involving rm do not vanish similarly because of non-degeneracy of (Cα,j(m)) for α =
(α1, . . . , αk+1, 0, . . . , 0) by Lemma 4.8. Thus J1 ∩ Q[u0] ̸= 0 indeed and ht(J1) = k + 1.
Now by (4) and (2) of Proposition 3.10, we can choose a linear transform ϕ1 : Q[x1, . . . , xn] →
Q[x1, . . . , xn] such that ˜xm1
1 , . . . , ˜xmk+1
k+1 ∈ ϕ(J1) for some mj ∈ Z+ and ˜xj the image of
xj. Then guaranteed by Proposition 3.10 and Lemma 4.8 the iteration proceeds until at
step n − k when we choose a linear transform ϕn−k : Q[x1, . . . , xn] → Q[x1, . . . , xn] such
that ϕn−k(J) ∩ Q[un−k−1] ̸= 0 for some un−k−1 ⊂ {x1, . . . , xn} of size two. Then we see
ht(J) = n − 1 and dim(Z(J)) = 1, which proves Theorem 1.2. □

Proof of Theorem 1.3. Guaranteed by the non-degeneracy of coeﬃcients matrices as in
Lemma 4.8, the above proof works for ideals generated by Hasse derivatives of not nec-
essarily distinct degrees. The similar process of Gauss elimination and linear transforms
promises that ht(f (j1)(xi1), . . . , f (jn−1)(xin−1 )) = n − 1,
for any n − 1 arbitrary distinct pairs (ik, jk) with 1 ≤ ik ≤ n and 1 ≤ jk ≤ n − 1. □

References

[1] J. Barwise, P. Eklof, Lefschetz’s principle, Journal of Algebra, Volume 13, Issue 4, December 1969,
Pages 554-570.
[2] E. Casas-Alvero, Higher order polar germs, J. Algebra. 240 1, 326-337 (2001).
[3] Jan Draisma, Johan P. de Jong, On the Casas-Alvero conjecture, Newsletter of the EMS 80 (June 2011)
29-33.
[4] Sicun Gao, Counting Zeros over Finite Fields with Groebner Bases, MS Thesis in Logic, Carnegie
Mellon University 2009.
[5] G.-M. Greuel, G. Pﬁster, A SINGULAR Introduction to Commutative Algebra, Second Edition.
Springer (2007).
[6] R. N. Karasev, F. V. Petrov, Partitions of nonzero elements of a ﬁnite ﬁeld into pairs, Israel J. Math.
192, no. 1, 143-156 (2012).
[7] Qing Liu, Algebraic Geometry and Arithmetic Curves, Oxford Graduate Texts in Mathematics, 6
(2002).
[8] Terence Tao, https://terrytao.wordpress.com/2012/08/31/the-lang-weil-bound/
Email address: zhipeng.lu@uni-goettingen.de
