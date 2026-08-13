<!-- source: https://arxiv.org/pdf/2108.09857 | converted from PDF -->

arXiv:2108.09857v5  [math.NT]  2 Oct 2022Uniform explicit Stewart’s theorem on prime
factors of linear recurrences

Yuri Bilu
a, Sanoli Gun
b and Haojie Hongc

Version of October 4, 2022

To the memory of Andrzej Schinzel

Abstract

Stewart (2013) proved that the biggest prime divisor of the nth term
of a Lucas sequence of integers grows quicker than n, answering famous
questions of Erd˝os and Schinzel. In this note we obtain a fully explicit
and, in a sense, uniform version of Stewart’s result.

Contents

1 Introduction 1
2 Notation and preliminaries 4
3 Logarithmic forms 5
4 Proof of Theorem 1.4 6
5 Quadratic ﬁelds 9
6 Multiplicatively independent elements 10
7 Proof of Theorem 1.5 13
8 Cyclotomic polynomials and primitive divisors 15
9 Proof of Theorem 1.2 17
10 Proof of Theorem 1.3 19

1 Introduction

For a non-zero algebraic number γ, denote by ω(γ) the number of distinct
primes p of the ﬁeld Q(γ) with the property νp(γ) ̸= 0. We denote by N γ the
Q-norm: N γ = NQ(γ)/Q(γ).
The following theorem was proved by Stewart in his seminal article [16].

aSupported by the SPARC Project P445 (India) and ANR project JINVARIANT
bSupported by the SPARC Project P445 (India)
cSupported by the China Scholarship Council grant CSC202008310189

1

Theorem 1.1. Let γ be a non-zero algebraic number, not a root of unity, sat-
isfying the following:

• either γ ∈ Q,

• or [Q(γ) : Q] = 2 and N γ = ±1.

Then there exists n0, depending only on ω(γ) and the ﬁeld K = Q(γ), with the
following property. For every n > n0 there exists a prime p of K, with the
underlying rational prime p, such that νp(γn − 1) ≥ 1 and

p ≥ n exp ( 1
104 log n
log log n
 ) .

This result answered famous questions posed by Erd˝os and Schinzel, see the
introduction of [16] for a historical account.
Note that Stewart’s [16, Theorem 1.1] is stated in diﬀerent terms, but what
he actually proves is exactly Theorem 1.1 above.
In this note we re-examine Stewart’s argument with the following objectives:

(uniformity) we show that Stewart’s n0 depends only on Q(γ), but not on
ω(γ); in particular, if γ ∈ Q then n0 is an absolute constant;

(explicitness) we obtain a totally explicit expression for n0.

We prove the following two theorems.

Theorem 1.2. Let γ be a non-zero rational number, distinct from ±1. Set
n0 = exp(106). Then for every n ≥ n0 there is a prime number p such that

νp(γn − 1) ≥ 1 and p ≥ n exp (0.0005 log n
log log n ).

Theorem 1.3. Let γ be a non-zero algebraic number of degree 2, not a root
of unity. We denote DK the discriminant of the number ﬁeld K = Q(γ), and
we set n0 = exp exp(max{109, 3|DK|}). Assume that N γ = ±1. Then for every
n ≥ n0 there exists a prime p of K, with the underlying rational prime p, such
that νp(γn − 1) ≥ 1 and
 p ≥ n exp (0.0002 log n
log log n
 ) .

Our numerical constants 0.0005 and 0.0002 are worse than Stewart’s 1/104.
On the other hand, our n0 do not depend on ω(γ). Our argument, being very
close to Stewart’s, allows one, in principle, to obtain 1/104 (but, probably, not
1/102), for the price of increasing the numerical value of n0.
We deduce Theorems 1.2 and 1.3 from the following two theorems (again,
essentially, due to Stewart, see [16, Section 4]), which are of independent interest.
We denote by h(·) the absolute logarithmic height, see Section 2. We also denote
log∗ = max{log, 1}, and we denote by N p the absolute norm of the ideal p; that
is, N p = #OK/p.
 2

Theorem 1.4. Let γ be a non-zero algebraic number of degree d, not a root
of unity. Set p0 = exp(80000d(log∗d)
2). Then for every prime p of the ﬁeld
K = Q(γ) with N p ≥ p0, and every positive integer n we have

νp(γn − 1) ≤ N p exp (
−0.002d
−1 log N p
log log N p
 ) h(γ) log∗n.

Theorem 1.5. Let γ be as in Theorem 1.3; that is, a non-zero algebraic number
of degree 2 and norm ±1, but not a root of unity. We again denote DK the
discriminant of the ﬁeld K = Q(γ), and we set p0 = exp exp(max{108, 2|DK|}).
Then for every prime p of K with underlying rational prime p ≥ p0, and every
positive integer n we have

νp(γn − 1) ≤ p exp (
−0.001 log p
log log p
 ) h(γ) log∗n. (1.1)

Remark 1.6. 1. The principal tool in the proof of Theorem 1.2 is Theo-
rem 1.4, which holds not only for γ ∈ Q, but for arbitrary algebraic γ.
One may wonder whether Theorem 1.2 can be extended to this general-
ity. One may expect the following statement: for n large enough, there
exists a prime p of the number ﬁeld Q(γ) such that νp(γn − 1) ≥ 1 and

N p ≥ n exp (c log n
log log n ), where c is a positive number not depending on n.

Unfortunately, the present argument does not seem to be capable of proving
this. See Remark 9.1 for more details.

2. Our values of n0 and p0 are rather huge numerically. In particular, in The-
orems 1.3 and 1.5 our n0, respectively p0, are double exponential in |DK|.
Of course, this is quite unsatisfactory for practical purposes. Unfortu-
nately, not much can be done here without involving substantially new
ideas. The reason is that we have to use the numerical Prime Number
Theorem from [2] (see Proposition 5.2). And using this theorem requires
parameter x therein to be exponential in |DK|. Since in the subsequent
proof of Theorem 1.5 this x is set to be around log p, this yields double
exponential dependence in |DK|. Note also that the original approach of
Stewart leads to even triple exponential dependence, as explained in Sec-
tion 6.

We follow the main lines of Stewart’s argument, with two changes. Uni-
formity in γ is achieved by using Lemmas 4.1 and 7.1. Another deviation of
Stewart’s argument is of more technical nature and is explained in detail in
Section 6.

Plan of the article Our principal tool is Yu’s [19] bound for a p-adic loga-
rithmic form. In Section 3, we present a simpliﬁed version of Yu’s result adapted
for our purposes. In Section 4, we prove Theorem 1.4.
In Section 5 and 6, we collect various facts about quadratic ﬁelds used in
the proof of Theorem 1.5, which is proved afterwards in Section 7.

3

In Section 8, we recall basic facts about cyclotomic polynomials and primitive
divisors, needed for the proofs of Theorems 1.2 and 1.3. These latter are proved
in the ﬁnal Sections 9 and 10 respectively.

2 Notation and preliminaries

Let K be a number ﬁeld. We denote by DK and hK the discriminant and
the class number of K. By a prime of K we mean a prime ideal of the ring
of integers OK. We denote by Fp the residue ﬁeld OK /p, and N p = #Fp the
absolute norm of p.
Let a, b be non-zero fractional ideals of K. We call them involved if there
exists a K-prime p such that νp(a), νp(b) ̸= 0. If no such prime exists, then we
call a, b disjoint (so that “not involved” and “disjoint” are synonyms). We call
α, β ∈ K × involved, resp. disjoint if so are the principal ideals (α), (β).
We denote by h(α) the usual absolute logarithmic height of α ∈ ¯Q:

h(α) = [K : Q]−1 ∑

v∈MK dv log+ |α|v,

where log+ = max{log, 0} and dv denotes the local degree. Here K is an ar-
bitrary number ﬁeld containing α, and the places v ∈ MK are normalized to
extend the standard places of Q; that is, |p|v = p−1 if v | p < ∞ and |x|v = |x|
if v | ∞ and x ∈ Q.
If K is a number ﬁeld of degree d and α ∈ K then the following formula is
an immediate consequence of the deﬁnition of the height:

h(α) = 1
d
 ( ∑

σ:K֒→C log+ |α
σ| + ∑

p max{0, −νp(α)} log N p
)
 ,

where the ﬁrst sum runs over the complex embeddings of K and the second
sum runs over the primes of K. If α ̸= 0 then h(α) = h(α
−1), and we obtain
the formula

h(α) = 1
d
 ( ∑

σ:K֒→C − log− |α
σ| + ∑

p max{0, νp(α)} log N p
)
 , (2.1)

where log− = min{log, 0}.
Besides log+ and log− we will also use log∗ = max{log, 1}.
We use O1(·) as the quantitative version of the familiar O(·) notation:
A = O1(B) means |A| ≤ B.
We will use the following estimates for the arithmetical functions ω(n), ϕ(n)

4

and π(x):
 ω(n) ≤ 1.4 log n
log log n (n ≥ 3), (2.2)

ϕ(n) ≥ 0.5 n
log log n (n ≥ 1020), (2.3)

x
log x ≤ π(x) ≤ 1.3 x
log x (x ≥ 3). (2.4)

See [12, Th´eor`eme 11], [13, Theorem 15] and [13, page 69, Corollary 1].

3 Logarithmic forms

In this section, K is a number ﬁeld of degree d, and p is a prime of K with
underlying rational prime p ≥ 5. Note that we will have p ≥ 5 in both Sections 4
and 7, where Theorem 3.1 will be applied: see (4.5) and (7.3). Let u be such
that K contains a primitive root of unity of order 2u, but not of order 2u+1.
We pick a primitive root of unity of order 2u and denote it ζ.
Our principal tool will be the following result of Yu [19]. Recall that α ∈ K ×

is called a p-adic unit if νp(α) = 0.

Theorem 3.1. Let α1, . . . , αk ∈ K × be multiplicatively independent p-adic units
Let δ and Ω be real numbers satisfying

δ ≤
 {[F×
p : ⟨¯ζ, ¯α1, . . . , ¯αk⟩
], if [K(α
1/2
1 , . . . , α
1/2
k ) : K] = 2k,
1, otherwise,

Ω = max
 { N p
δ
 ( k
log N p
 )k , ek log N p
}
 ,

where ⟨¯ζ, ¯α1, . . . , ¯αk⟩ is the subgroup of the multiplicative group F×
p generated by
the images of ζ, α1, . . . , αk.
Furthermore, let b1, . . . , bk be rational integers, not all 0, and denote

B = max{|b1|, . . . , |bk|}.

Then

νp(α
b1
1 · · · α
bk
k − 1) ≤ 105d
k+2(log∗d)
3 · 30kk5/2(log∗k)h(α1) · · · h(αk)Ω log∗B.
(3.1)

Proof. This is a simpliﬁcation (with slightly bigger numerical constants) of [16,
Lemma 3.1], which, on its own, is a simpliﬁcation of the main theorem of [19].
Let us explain how we deduce (3.1) from [16, Lemma 3.1]. Note that our k
corresponds to n in [16]. We will repeatedly use the observations of the following
kind: for a ≥ 0 and x, y ≥ 1 we have a + x + y ≤ (a + 2)xy.

5

Plugging the estimates

max{log∗B, (k + 1)(5.4k + log d)} ≤ log∗B · 13k2 log∗d,

(k + 1)
1/2 ≤ √
2k1/2,

7e p − 1
p − 2 ≤ 28
3 e (recall that p ≥ 5),

log(e4(k + 1)d) ≤ 8 log∗d log∗k

into [16, Lemma 3.1] (with n replaced by k), we bound the left-hand side of (3.1)
by
 376 (28
3 e)k d
k+2 · 104√
2k5/2 log∗k(log∗d)
3h(α1) · · · h(αk)Ω log∗B. (3.2)

This is clearly smaller that the right-hand side of (3.1).

4 Proof of Theorem 1.4

The following lemma is totally trivial, but we state it here because it is our
principal tool in making p0 independent of γ.

Lemma 4.1. Let K be a ﬁeld, γ1, . . . , γk ∈ K × multiplicatively independent,
and γ ∈ K × not a root of unity. Then, after a suitable renumbering of γ1, . . . , γk,
the numbers γ, γ2, . . . , γk become multiplicatively independent.

We will also need a lower bound for the height of an algebraic number.

Lemma 4.2. Let γ be an algebraic number of degree d, not a root of unity.
Then
 h(γ) ≥ log 2 for d = 1, (4.1)

2h(γ) ≥ log 1 + √
5
2 for d = 2, (4.2)

dh(γ) ≥ 1
4(log∗d)3 for any d. (4.3)

Proof. Inequality (4.1) is trivial, and (4.2) is a famous result of Schinzel [15] (see
also [6] for a very simple proof). Inequality (4.3), for suﬃciently large d, follows
from the famous work of Dobrowolski [5]. To obtain it for all d ≥ 3, we invoke
Voutier’s numerical adaptation [17] of Dobrowolski’s result. In particular, [17,
Corollary 2] gives dh(γ) ≥ 2/(log(3d))
3, which clearly implies (4.3) for d ≥ 3.
Finally, for d ≤ 2 inequality (4.3) follows from (4.1) and (4.2).

We can now start the proof of Theorem 1.4. To simplify notation, we denote
P = N p. We will assume that

N p = P ≥ p0 = exp
(
80000d(log∗d)
2) (4.4)

6

throughout the proof. Since N p ≤ pd, we have

p ≥ p1/d
0 ≥ exp
(
80000(log∗d)
2) ≥ 5, (4.5)

which is required to apply Theorem 3.1.
Let x be speciﬁed later to satisfy

x ≥ 200(log∗d)
2. (4.6)

Denote k = π(x). Let ℓ1, . . . , ℓk be the k primes not exceeding x numbered
somehow, not necessarily in the increasing order. Since ℓ1, . . . , ℓk are multi-
plicatively independent and γ is not a root of unity, Lemma 4.1 implies that,
after renumbering, the numbers γ, ℓ2, . . . , ℓk are multiplicatively independent.
We apply Theorem 3.1 with

α1 = γ
ℓ2 · · · ℓk ; αi = ℓi (i = 2, . . . , k);

bi = n (i = 1, . . . , k); δ = 1.

Since h(ℓi) = log ℓi ≤ log x, we obtain

νp(γn − 1) = νp(
α
n
1 ℓn
2 · · · ℓn
k − 1)

≤ 105d
k+2(log∗d)
3 · 30kk5/2(log∗k)h(α1)(log x)
k−1Ω log∗n,

where Ω = max{
P (k/ log P )
k, ek log P }
. We will see later, when we specify x,
that P (k/ log P )
k ≥ ek log P, (4.7)

and so we have Ω = P (k/ log P )
k.
Using Lemma 4.2, we estimate

h(α1) ≤ h(γ) + (k − 1) log x ≤ 4d(log∗d)
3h(γ)k log x.

Hence

νp(γn − 1) ≤ 4 · 105d
3(log∗d)
6k7/2(log∗k)P ( 30dk log x
log P
 )k h(γ) log∗n.

We want to simplify this estimate.
It follows from (4.6) that k ≥ π(200) = 46, which easily implies that

4 · 105k7/2(log∗k) ≤ 2k.

Also, using (2.4), we obtain
 k ≥ 200(log∗d)
2

log(
200(log∗d)2) ,

7

which implies that d
3(log∗d)
6 ≤ 2k. Indeed, this is obvious when d = 1, 2. When
d ≥ 3, it is suﬃcient to prove that

200(log d)
2

log(200) + 2 log log d ≥ 3 log d + 6 log log d
log 2 .

This is true since 200 log 2(log d)
2 ≥ 9 log d(log 200 + 2 log d) holds when d ≥ 3.
Finally, again using (2.4), we estimate k log x ≤ 1.3x. Since

2 · 2 · 1.3 · 30 < 160,

this implies the estimate

νp(γn − 1) ≤ P ( 160dx
log P
 )k h(γ) log∗n. (4.8)

It is the time to specify x. We set x = (1/400d) log P , which gives

νp(γn − 1) ≤ P · 0.4kh(γ) log∗n. (4.9)

Note that (4.6) is satisﬁed with our choice of x, because of (4.4).
Now we are almost done. Once again using (2.4), we obtain

k ≥ x
log x ≥ 1
400d log P
log log P .

Substituting this to (4.9), we obtain

νp(γn − 1) ≤ P exp (
−0.002d
−1 log P
log log P
 ) h(γ) log∗n,

as wanted.
We are left with checking that assumption (4.7) holds true with our choice
of x. It suﬃces to show that P ≥ (e log P )
k+1. As we have seen above, k ≥ 46,
and we use (2.4) to obtain

k + 1 ≤ 47
46 π(x) ≤ 1.4 x
log x ≤ 1.4
400 log P
log((1/400) log P ) .

Since P ≥ e80000, we have

1
400 log P ≥ (log P )
0.4, e log P ≤ (log P )
1.1.

It follows that

k + 1 ≤ 0.009 log P
log log P , (e log P )
k+1 ≤ P 0.01 ≤ P.

This completes the proof of the theorem.

8

5 Quadratic ﬁelds

We need to recall some facts about quadratic ﬁelds. In this section, unless
otherwise stated, K denotes a quadratic ﬁeld. We denote by DK and hK the
discriminant and the class number of K respectively. If K is a real quadratic
ﬁeld then we denote by ηK the fundamental unit η satisfying η > 1. It will
be convenient to set ηK = 1 for imaginary K. We denote by σ the non-trivial
Galois morphism of K over Q. Note that, when K is real, we have

ηK ≥ 1 + √5
2 . (5.1)

We set µ = #O×
K/2; in other words,

µ =
 



3, if K = Q(
√
−3),
2, if K = Q(i),
1, in all other cases.

Proposition 5.1. 1. Let K be an imaginary quadratic ﬁeld. Then

hK ≤ µπ−1|DK|1/2(2 + log |DK|). (5.2)

2. Let K be a real quadratic ﬁeld. Then

hK log ηK ≤ π−1D1/2
K (2 + log DK). (5.3)

3. For any quadratic ﬁeld, K, we have

hK ≤ 3|DK|1/2 log |DK|, (5.4)

log ηK ≤ |DK|1/2 log |DK|. (5.5)

Proof. Estimates (5.2) and (5.3) are well-known; see, for instance, Theorems 10.1
and 14.3 in [8, Chapter 12]. Estimate (5.4) follows, in the imaginary case, from
µ ≤ 3 and |DK| ≥ 3, and in the real case from (5.1) and |DK| ≥ 5. Finally, (5.5)
is trivial in the imaginary case, and in the real case it follows from hK ≥ 1 and
DK ≥ 5.

Denote by πs(x, K) the counting function of rational primes that split in K.

Proposition 5.2. For x ≥ max{1010, e|DK |} (5.6)

we have
 πs(x, K) ≥ 1
2 x
log x − ϕ(|DK |)
320 x
(log x)2 . (5.7)

9

Proof. We denote D = DK. An odd rational prime p splits in K if and only if
(D/p) = 1. Primes satisfying this condition belong to one of ϕ(|D|)/2 residue
classes mod|D|. If a mod |D| is one such class, then for x satisfying (5.6) we
have π(x; |D|, a) ≥ 1
ϕ(|D|) Li(x) − 1
160 x
(log x)2 ,

see Theorem 1.3 in Bennett et al. [2]. As usual, we denote by π(x; m, a) the
counting function for primes in the congruence class a mod m.
Note that Li(x) > x/ log x for x ≥ 7, because the function

f (x) = Li(x) − x/ log x

satisﬁes f ′(x) = 1/(log x)
2 > 0 and f (7) = 0.114 . . . > 0. It follows that

π(x; |D|, a) ≥ 1
ϕ(|D|) x
log x − 1
160 x
(log x)2 .

Summing up over the ϕ(|D|)/2 residue classes a mod |D|, we obtain (5.7).

6 Multiplicatively independent elements

We retain the notation and conventions of Section 5.
Stewart’s argument in the quadratic case [16, Section 4] requires producing
in K many multiplicatively independent elements of norm 1 and controllable
height. Stewart uses for this purpose prime numbers p with the following prop-
erties:

• p splits in K, and

• the K-primes above p are principal.

We call them Stewart primes in the sequel.
Let (π) be a principal K-prime above a Stewart prime p. If K is imaginary
then |π| = |πσ| = p1/2. If K is real then, multiplying π by a suitable power of
the fundamental unit ηK, we may assume that (p/ηK)
1/2 ≤ |π|, |πσ| ≤ (pηK)
1/2.
Stewart associates to p the algebraic number θp = π/πσ. For this θp we have
N θp = 1, and
 h(θp) = 1
2 log p + O1
 ( 1
2 log ηK
 ) ;

recall that O1(·) is quantitative version of O(·), see Section 2. Clearly, num-
bers θp corresponding to distinct Stewart primes p are multiplicatively indepen-
dent.
Using the Class Field Theory and the Tchebotarev Density Theorem, one
can show that the relative density of Stewart primes in the set of all primes is
(2hK)
−1. Moreover, using recent explicit versions of the Tchebotarev Density
Theorem, as in [1, 9, 18], one can give a totally explicit lower estimate for the
counting function of Stewart primes.
 10

Unfortunately, following this path, we end up with a rather huge value for
the constant p0 in Theorem 1.5, triple exponential in the discriminant of K.
For instance, Theorem 5 of [9] applies for x ≥ x1 := exp(|DL|12), where, in our
case, L is the Hilbert Class Field of K. We have |DL| = |DK|hK , which would
lead to a double exponential value for x1. And p0, as it is clear from the proof
of Theorem 1.5, is exponential in x1, leading to the triple exp dependence of p0
in |DK|. For this reason, we do not pursue this approach in the present article.
Instead of Stewart primes, which are quite sparse, we use all (suﬃciently
large) split primes, which have relative density 1/2. More precisely, denote by
S(K) the set of rational primes p which split in K and satisfy p ≥ |DK|1/2. To
every p ∈ S(K) we want to associate a certain element θp ∈ K. We do it as
follows.
Given p ∈ S(K), let p be a K-prime above p. Recall that every ideal class
contains an integral ideal a such that N a < |DK|1/2. We take such a in the
class of p−1, so that pa is a principal ideal. Let α be a generator of pa. Then
|αα
σ| = N (pa). Note also that, since N a < |DK|1/2, the number α is not in-
volved with any prime from the set S(K) other than p itself.
If K is imaginary then |α| = |α
σ| = N (pa)
1/2. If K is real then, multiply-
ing α be a suitable power of ηK, we may assume that

N (pa)
1/2η−1/2
K ≤ |α|, |α
σ| ≤ N (pa)
1/2η1/2
K . (6.1)

Now we set θp = α/α
σ.

Proposition 6.1. 1. For every p ∈ S(K) we have N θp = 1 and

h(θp) = 1
2 log p + O1
 ( 1
4 log |DK| + 1
2 log ηK
 ) .

2. In particular, if p ≥ exp(100|DK|1/2 log |DK|) then

h(θp) ≤ 0.51 log p. (6.2)

3. Each θp is involved with p, but disjoint from any other prime exceeding
|DK|1/2. In particular, it is disjoint from any prime belonging to the set
S(K). If p is a K-prime over p, then νp(θp) = ±1.

4. If p1, . . . , pk are distinct elements of S(K) then θp1 , . . . , θpk are multiplica-
tively independent. Moreover, [
K(√
θp1 , . . . , √
θpk ) : K] = 2k.

Proof. Items 1 and 3 follow from (6.1), the deﬁnition of θp and the upper bound
N a < |DK|1/2. To prove item 2, it suﬃces to show that

0.01 log p ≥ 1
4 log |DK| + 1
2 log ηK.

11

In view of (5.5), this would follow from

log p ≥ 100 ( 1
4 log |DK| + 1
2 |DK|1/2 log |DK|) .

And this is a consequence of our assumption about p.
To prove item 4, denote Li = K(√
θp1, . . . , √
θpi ) (with the convention
L0 = K), and let pi be a prime of K above pi. Item 3 implies that pi ramiﬁes
in Li but not in Li−1. Hence [Li : Li−1] = 2, whence the result.

Item 2 of this proposition suggests to count the split primes p satisfying
p ≥ exp(100|DK|1/2 log |DK|). The following is an immediate consequence of
Proposition 5.2.

Corollary 6.2. For x ≥ exp(max{107, |DK|}) we have

πs(x, K) − πs(
exp(100|DK|1/2 log |DK|), K) ≥ 0.49 x
log x .

Proof. Using Proposition 5.2,

πs(x, K)−πs(
exp(100|DK|1/2 log |DK|), K)

≥ 1
2 x
log x − ϕ(|DK |)
320 x
(log x)2 − exp(100|DK|1/2 log |DK|). (6.3)

Let us estimate both the extra terms in the right-hand side of (6.3). We have
log x ≥ |DK|, which implies that

ϕ(|DK|)
320 x
(log x)2 ≤ 1
320 x
log x .

Next, using log x ≥ |DK| and log x ≥ 107, we obtain

100|DK|1/2 log |DK| ≤ 100(log x)
1/2 log log x < 0.6 log x.

Hence exp(100|DK|1/2 log |DK|) < x
0.6 < 10−10 x
log x ,

where we again use the assumption log x ≥ 107.
We conclude that the right-hand side of (6.3) exceeds
( 1
2 − 1
320 − 10−10) x
log x ,

which is bigger than 0.49x/ log x.
 12

7 Proof of Theorem 1.5

As in Section 4, we start from a simple lemma.

Lemma 7.1. Let K be a ﬁeld of characteristic 0, let γ1, . . . , γk ∈ K × be such
that [
K(√
γ1, . . . , √
γk) : K] = 2k,

and let γ ∈ K × be not a square in K. Then, after suitable renumbering γ1, . . . , γk,
we have [
K(√
γ, √
γ2, . . . , √
γk) : K] = 2k. (7.1)

Proof. Let ¯γ, ¯γ1, . . . , ¯γk be the images of γ, γ1, . . . , γk in the group K ×/(K ×)
2.
Viewing the latter as an F2-vector space, the vectors ¯γ1, . . . , ¯γk are linearly inde-
pendent and vector ¯γ is non-zero. Hence, after renumbering, vectors ¯γ, ¯γ2, . . . , ¯γk
become linearly independent. This yields (7.1) by Kummer’s theory, as given,
for instance, in [10, Section VI.8]. Indeed, Theorem 8.1 therein implies that

[K(√
γ, √
γ2, . . . , √
γk) : K] = [Γ : (K ×)
2],

where Γ is the subgroup of K × generated by γ, γ2, . . . , γk and (K ×)
2. The
quotient Γ/(K ×)
2 is isomorphic, as F2-vector space, to the space generated by
¯γ, ¯γ2, . . . , ¯γk. Hence [Γ : (K ×)
2] = 2k, and we are done.

Now we are ready to start the proof of Theorem 1.5. In this section,
K = Q(γ) and p is a prime of K, whose underlying rational prime p satisﬁes

p ≥ p0 = exp exp
(
max{108, 2|DK|})
. (7.2)

In particular, p ≥ 5, (7.3)

which is required to apply Theorem 3.1.
If N p = p then Theorem 1.5 follows from the case d = 2 of Theorem 1.4.
Therefore we will assume that N p = p2. In particular, the residue ﬁeld Fp is
the ﬁnite ﬁeld Fp2.
Let x be a positive real number to be speciﬁed later to satisfy

x ≥ exp(max{107, |DK|}). (7.4)

The results of Section 6 imply the following. There exists a positive integer k
and distinct prime numbers ℓ1, . . . , ℓk ∈ S(K) such that

k ≥ 0.49 x
log x , ℓi ≤ x,

h(θℓi ) ≤ 0.51 log x (1 ≤ i ≤ k). (7.5)

Note also that k ≤ π(x) ≤ 1.3 x
log x , (7.6)

13

see (2.4).
Next, let r be the biggest positive integer with the following property: there
exists θ ∈ K × such that θr = γ. This θ is not a square in K by the deﬁnition
of r, and Lemma 7.1 implies that, after renumbering ℓ1, . . . , ℓk, we have
[
K(
√
θ, √
θℓ2 , . . . , √
θℓk ) : K] = 2k.

Denote by G the subgroup of the multiplicative group F×
p = F×
p2, consisting
of elements of norm ±1:

G = {x ∈ F×
p2 : NFp2 /Fp x = ±1}.

Since the norm map N : F×
p2 → F×
p is surjective (see, for instance, [11, The-
orem 2.28(ii)]), we have [F×
p2 : G] = (p − 1)/2. The Fp-images of θ, θℓ2, . . . , θℓk
belong to G. Hence we can use Theorem 3.1 with

α1 = θ
θℓ2 · · · θℓk ; αi = θℓi (i = 2, . . . , k);

bi = nr (i = 1, . . . , k); δ = p − 1
2 ; d = 2.

Note that α1, . . . , αk are p-adic units, as required in Theorem 3.1. Indeed,
item 3 of Proposition 6.1 implies that each αi is disjoint from any rational prime
exceeding |DK|1/2, except perhaps ℓ1, . . . , ℓk. We have p ̸= ℓ1, . . . , ℓk (because p
is inert in K, and the primes ℓi split in K), and p ≥ |DK|1/2 by (7.2). Hence αi
is disjoint from p, that is, it is a p-adic unit.
Using the upper bound (7.5) for the heights of θℓi ’s, we obtain

νp(γn − 1) = νp(
α
nr
1 θnr
ℓ2 · · · θnr
ℓk − 1)

≤ 106 · 60kk5/2(log∗k)h(α1)(0.51 log x)
k−1Ω log∗(nr), (7.7)

where
 Ω = max
 { 2p2

p − 1
 ( k
2 log p
 )k , 2ek log p
}
 .

We will see later that
 Ω = 2p2

p − 1
 ( k
2 log p
 )k (7.8)

with our choice of x. Using p ≥ p0, this implies that

Ω ≤ 2.1p ( k
2 log p
 )k .

Next, we have 2h(θ) ≥ log((1 + √5)/2) by Lemma 4.2. Using this, the deﬁnition
of α1 and the upper bound (7.5) for the height of the θℓi’s, we estimate

h(α1) ≤ h(θ) + 0.51(k − 1) log x ≤ 5h(θ)k log x = 5
r h(γ)k log x.

14

Also, a quick veriﬁcation shows that log∗(nr) ≤ r log∗n for all possible choices
of n and r. Substituting all these estimates into (7.7), we obtain

νp(γn − 1) ≤ 108k7/2(log∗k)p ( 15.3k log x
log p
 )k h(γ) log∗n.

We want to simplify this estimate. It follows from (7.4) that

k ≥ 0.49 x
log x ≥ exp(106),

which easily implies that 108k7/2(log∗k) < 1.1k. Also, k log x ≤ 1.3x by (7.6).
Since 1.1 · 1.3 · 15.3 < 30, we obtain the estimate

νp(γn − 1) ≤ p ( 30x
log p
 )k h(γ) log∗n.

Now we set x = 300−1 log p. Then (7.4) is satisﬁed, and we have

νp(γn − 1) ≤ p · 0.1kh(γ) log∗n.

Since k ≥ 0.49 x
log x > 0.001 log p
log log p ,

we obtain
 νp(γn − 1) ≤ p exp (
−0.002 log p
log log p
 ) h(γ) log∗n,

which is even better than wanted.
It remains to verify that (7.8) holds with our choice of x. It suﬃces to
prove that p > (2e log p)
k+1. Using the lower estimates p ≥ exp exp(108) and
x ≥ exp(107) (see (7.2), (7.4)) together with the upper estimate (7.6), we obtain

k + 1 < 1.4x
log x = 1.4
300 log p
log log p − log 300 < 0.01 log p
log log p

and log(2e log p) < 2 log log p. It follows that (k + 1) log(2e log p) < log p. This
completes the proof of the theorem.

8 Cyclotomic polynomials and primitive divi-
sors

In this section, we collect some results on cyclotomic polynomials and primitive
divisors. We denote by Φn(t) the cyclotomic polynomial of order n. Recall that
deg Φn = ϕ(n), the Euler totient.
The following results go back to Schinzel [14], but in the present form they
can be found in [4]. Recall (see Section 2) that A = O1(B) means |A| ≤ B.

15

Proposition 8.1. 1. Let γ be an algebraic number. Then

h(Φn(γ)) = ϕ(n)h(γ) + O1(2ω(n) log(πn)).

2. Let γ be a complex algebraic number of degree d, non-zero and not a root
of unity. Then
 log |Φn(γ)| ≥ −1014d
5h(γ) · 2ω(n) log∗n. (8.1)

Proof. Item 1 is [4, Theorem 3.1]. Item 2 follows from [4, Corollary 3.5], which
gives the inequality

log |Φn(γ)| ≥ −1012d
3(h(γ) + 1) · 2ω(n) log(n + 1).

We have clearly log(n + 1) ≤ 1.3 log∗n. Also, Lemma 4.2 implies that

d(h(γ) + 1) ≤ dh(γ)(1 + 4d(log∗d)
3) < 10d
3h(γ).

This proves (8.1).

Let K be a number ﬁeld of degree d and γ ∈ K × not a root of unity. We
consider the sequence un = γn − 1. We call a K-prime p primitive divisor of un
if νp(un) ≥ 1, νp(uk) = 0 (k = 1, . . . n − 1).

Let us recall some basic properties of primitive divisors.

Proposition 8.2. 1. Let p be a primitive divisor of un. Then νp(Φn(γ)) ≥ 1
and N p ≡ 1 mod n; in particular, N p ≥ n + 1.

2. Let p be a primitive divisor of un and p the rational prime underlying p.
If γ is of degree 2 and absolute norm 1, then p ≡ ±1 mod n.

3. Assume that n ≥ 2d+1. Let p be not a primitive divisor of un. Then
νp(Φn(γ)) ≤ νp(n).

Proof. Item 3 is Lemma 4 of Schinzel [14]; see also [4, Lemma 4.5]. Items 1
and 2 are well-known, but we include short proofs for the reader’s convenience.
To prove item 1, note ﬁrst of all that we must have νp(γ) = 0, because
νp(γn − 1) > 0. Furthermore,

νp(γn − 1) = ∑

m|n νp(Φm(γ)),

where each summand is non-negative because νp(γ) = 0. Since p is a primitive
divisor of un, we must have νp(Φm(γ)) = 0 for every m < n. It follows that
νp(Φn(γ) = νp(γn − 1) ≥ 1.
Let ¯γ be the image of γ in Fp = OK/p. Then saying that p is a primitive
divisor of γn − 1 is equivalent to saying that n is the order of ¯γ in the multi-
plicative group F×
p . In particular, n must divide N p − 1, the order of this group.
This complete the proof of item 1.
 16

In item 2, if N p = p then the result follows from item 1 (and we do not need
the assumption N γ = 1). Now assume that N p = p2. The subgroup

{x ∈ F×
p : NFp/Fpx = 1}

is of order p + 1, because the norm map is surjective [11, Theorem 2.28(ii)].
Since ¯γ belongs to this subgroup, we must have n | (p + 1). This proves item 2.

9 Proof of Theorem 1.2

We set n0 = exp(106) and we assume that n ≥ n0 in the sequel.
Let P be the biggest prime number p with the property νp(Φn(γ)) ≥ 1. We
want to show that
 P ≥ n exp (
0.0005 log n
log log n
 ) . (9.1)

We will deduce this from Theorem 1.4, used with d = 1, and the properties of
cyclotomic polynomials and primitive divisors collected in Section 8.
We apply equation (2.1) with α = Φn(γ). Here d = 1, and we obtain the
following:
 h
(Φn(γ)
) = − log
− |Φn(γ)| + ∑

p max
{0, νp(
Φn(γ)
)} log p. (9.2)

We estimate the ﬁrst term in (9.2) using item 2 of Proposition 8.1:

− log− |Φn(γ)| ≤ 1014h(γ) · 2ω(n) log n. (9.3)

Next, let us call p primitive if it is a primitive divisor of γn − 1, as deﬁned in
Section 8, and non-primitive otherwise. We split the sum in (9.2) into two sums:
∑

p max{
0, νp(
Φn(γ)
)} log p = ∑

p primi-
tive
 + ∑

p non-
primitive
 = Σp + Σnp.

We estimate Σnp using item 3 of Proposition 8.2:

Σnp ≤ ∑

p νp(n) log p = log n.

Thus, h
(Φn(γ)
) ≤ 1014h(γ) · 2ω(n) log n + log n + Σp.

On the other hand, item 1 of Proposition 8.1 implies the lower bound

h
(
Φn(γ)
) ≥ ϕ(n)h(γ) − 2ω(n) log(πn).

Combining the two bounds, we obtain the following lower estimate for Σp:

Σp ≥ ϕ(n)h(γ) − 2ω(n) log(πn) − 1014h(γ) · 2ω(n) log n − log n. (9.4)

17

Inequalities (2.2), (2.3) and our assumption n ≥ exp(106) imply that the right-
hand side of (9.4) is bounded from below by 0.9ϕ(n)h(γ). Thus, we obtain the
lower estimate Σp ≥ 0.9ϕ(n)h(γ). (9.5)

Now let us bound Σp from above. Recall that primitive p satisfy p ≡ 1 mod n.
In particular, p ≥ n + 1 > n0. Since our n0 is bigger than the p0 from Theo-
rem 1.4, the latter applies, and we obtain, for primitive p, the estimate

νp(
Φn(γ)
) = νp(γn − 1) ≤ p exp (
−0.002 log p
log log p
 ) h(γ) log n.

Since p > n > ee, we have
 log p
log log p ≥ log n
log log n .

Hence
 νp(
Φn(γ)
) ≤ P exp (−0.002 log n
log log n
 ) h(γ) log n.

It follows that

Σp ≤ ∑

p≡1 mod n
p≤P
 max
{0, νp(
Φn(γ)
)} log p

≤ π(P ; n, 1)h(γ)P exp (
−0.002 log n
log log n
 ) log n log P,

where, as usual, π(x; m, a) counts primes p ≤ x satisfying p ≡ a mod m. To
estimate π(P ; n, 1), Stewart uses the Brun-Titchmarsh inequality. However,
just the trivial estimate π(P ; n, 1) ≤ P/n would suﬃce. We obtain

Σp ≤ 2h(γ)P 2 log P exp (
−0.002 log n
log log n
 ) log n
n . (9.6)

Thus, we have a lower bound (9.5) and an upper bound (9.6) for Σp. Com-
bining the two, we obtain

P 2 log P ≥ 0.4 nϕ(n)
log n exp (
0.002 log n
log log n
 ) .

We may assume that P < n2, since otherwise there is nothing to prove. Using
this assumption and (2.3), we obtain

2P 2 log n ≥ P 2 log P

≥ 0.4 nϕ(n)
log n exp (
0.002 log n
log log n
 )

≥ 0.2 n2

log n log log n exp (
0.002 log n
log log n
 ) .

18

This can be re-written as

P ≥ √
0.1 n
log n√
log log n exp (0.001 log n
log log n
 ) .

Since n ≥ exp(106), we must have

√
0.1 n
log n√
log log n exp (
0.001 log n
log log n
 ) ≥ n exp (
0.0005 log n
log log n
 ) .

Hence (9.1) is proved.

Remark 9.1. As it is already indicated in the introduction, Theorem 1.2 holds
not only for γ ∈ Q, but for arbitrary algebraic γ, and one may wonder whether
Theorem 1.2 can be extended to this generality, like: for n large enough, there
exists a prime p of the number ﬁeld Q(γ) such that

νp(γn − 1) ≥ 1, N p ≥ n exp (c log n
log log n
 ) ,

where c is a positive number not depending on n.
Unfortunately, the present argument does not seem to be capable of proving
this. The reason is that, when γ /∈ Q, there is no good bound for the number
of p satisfying N p ≡ 1 mod n. For instance, if γ is of degree 2, we have to
count rational primes satisfying p2 ≡ 1 mod n. Since the ring Z/nZ may have
as much as 2ω(n) square roots of unity, we cannot obtain, without involving extra
ideas, an upper bound sharper than 2ω(n) for the number of such primes. And,
since ω(n) can be of magnitude as big as log n/ log log n, this would destroy the

tiny gain exp (
−0.002d
−1 log N p
log log N p ) obtained in Theorem 1.4.
In the case d = 2 this diﬃculty is overcome in [7], using ideas from the
previous article [3]. However, the case d ≥ 3 remains open.

10 Proof of Theorem 1.3

We follow the proof of Theorem 1.2 with appropriate modiﬁcation. In particular,
we set n0 = exp exp(max{109, 3|DK|}) and we assume that n ≥ n0 throughout
the proof.
Let P be the biggest element of the set

{p : p is a rational prime lying below a prime p of K, with νp(Φn(γ)) ≥ 1}.

We want to show that
 P ≥ n exp (
0.0002 log n
log log n
 ) . (10.1)

We apply equation (2.1) with α = Φn(γ). Here d = 2, and we obtain

2h
(
Φn(γ)
) = − log
− |Φn(γ)| − log− |Φn(γσ)| + ∑

p max
{0, νp(
Φn(γ)
)} log N p,

(10.2)

19

where σ is the non-trivial morphism of Q(γ)/Q.
We use item 2 of Proposition 8.1 to estimate the ﬁrst term of (10.2):

− log− |Φn(γ)| − log− |Φn(γσ)| ≤ 26 · 1014h(γ) · 2ω(n) log n. (10.3)

We split the sum in (10.2) into two parts:
∑

p max
{
0, νp(
Φn(γ)
)} log N p = ∑

p primi-
tive
 + ∑

p non-
primitive
 = Σp + Σnp.

By item 3 of Proposition 8.2, we can bound the non-primitive part,

Σnp ≤ ∑

p νp(n) log N p ≤ 2 log n.

Thus h
(
Φn(γ)
) ≤ 1016h(γ) · 2ω(n) log n + Σp/2 + log n. (10.4)

On the other hand, by item 1 of Proposition 8.1,

h
(Φn(γ)
) ≥ ϕ(n)h(γ) − 2ω(n) log(πn) (10.5)

Combining (10.4) and (10.5), we have

Σp/2 ≥ ϕ(n)h(γ) − 2ω(n) log(πn) − 1016h(γ)2ω(n) log n − log n (10.6)

Inequalities (2.2), (2.3) and our assumption n ≥ n0 ≥ exp exp(109) imply that
the right-hand side of (10.6) is bounded from below by 0.9ϕ(n)h(γ). Thus, we
obtain the lower estimate Σp ≥ 1.8ϕ(n)h(γ). (10.7)

Now let us bound Σp from above. By item 1 of Proposition 8.2, a primitive
divisor p of γn − 1 satisﬁes N p ≡ 1 mod n. In paticular N p ≥ n+ 1 and thus the
underlying rational prime p is bigger than √
n0 = exp(exp(max{109, 3|DK|})/2),
which is bigger than the p0 in Theorem 1.5. So we obtain, for primitive p with
underlying prime p,

νp(
Φn(γ)
) = νp(γn − 1) ≤ p exp (
−0.001 log p
log log p
 ) h(γ) log n.

Since p2 ≥ N p > n > ee, we have

log p
log log p ≥ 1
2 log n
log log n .

Hence
 νp(
Φn(γ)
) ≤ h(γ)P exp (
−0.0005 log n
log log n
 ) log n.

20

Using this and items 1, 2 of Proposition 8.2, we obtain

Σp ≤ ∑

N p≡1 mod n
p≤P
 max{
0, νp(
Φn(γ)
)} log N p

≤ 2(
π(P ; n, 1) + π(P ; n, −1)
)
h(γ)P exp (
−0.0005 log n
log log n
 ) log n log P.

As in Section 9, we estimate trivially π(P ; n, 1) + π(P ; n, −1) ≤ 2P/n. We ob-
tain
 Σp ≤ 8h(γ)P 2 log P exp (
−0.0005 log n
log log n
 ) log n
n . (10.8)

Combining the lower bound (10.7) the upper bound (10.8), we obtain

P 2 log P ≥ 0.1 nϕ(n)
log n exp (
0.0005 log n
log log n
 ) .

Using again n ≥ exp exp(109) we obtain (10.1), arguing as in the end of the
proof of Theorem 1.2 in Section 4.

Acknowledgments Yuri Bilu and Sanoli Gun acknowledge support of the
SPARC Project P445 “Arithmetical aspects of the Fourier coeﬃcients of mod-
ular forms”. Yuri Bilu was also supported by the ANR project JINVARI-
ANT. Haojie Hong was supported by the China Scholarship Council grant
CSC202008310189.
The authors thank Keith Conrad, Florian Luca, Kevin O’Bryant and Fa-
bien Pazuki for useful discussions. We especially thank the anonymous referee
for careful reading of the manuscript and many suggestions, that helped us to
correct mistakes and improve the presentation.

References

[1] Jeoung-Hwan Ahn and Soun-Hi Kwon, Lower estimates for the prime ideal of degree
one counting function in the Chebotarev density theorem, Acta Arith. 191 (2019), no. 3,
289–307. MR 4017533

[2] Michael A. Bennett, Greg Martin, Kevin O’Bryant, and Andrew Rechnitzer, Explicit
bounds for primes in arithmetic progressions, Illinois J. Math. 62 (2018), no. 1-4, 427–
532. MR 3922423

[3] Yuri Bilu, Haojie Hong, and Florian Luca, Big prime factors in orders of elliptic curves
over ﬁnite ﬁelds, Publ. Math. Debrecen, to appear; arXiv:2112.07046, 2021.

[4] Yuri Bilu and Florian Luca, Binary polynomial power sums vanishing at roots of unity,
Acta Arith. 198 (2021), no. 2, 195–217. MR 4228301

[5] E. Dobrowolski, On a question of Lehmer and the number of irreducible factors of a
polynomial, Acta Arith. 34 (1979), no. 4, 391–401. MR 543210

[6] G. H¨ohn and N.-P. Skoruppa, Un r´esultat de Schinzel, J. Th´eor. Nombres Bordeaux 5
(1993), no. 1, 185. MR 1251237

[7] Haojie Hong, Stewart’s theorem revisited: suppressing the norm ±1 hypothesis, Bol. Soc.
Mat. Mex. (3) 28 (2022), no. 3, Paper No. 60. MR 4462796

21

[8] Loo Keng Hua, Introduction to number theory, Springer-Verlag, Berlin-New York, 1982,
Translated from the Chinese by Peter Shiu. MR 665428

[9] Habiba Kadiri and Peng-Jie Wong, Primes in the Chebotarev density theorem for all
number ﬁelds (with an Appendix by Andrew Fiori), J. Number Theory 241 (2022), 700–
737. MR 4472459

[10] Serge Lang, Algebra, third ed., Graduate Texts in Mathematics, vol. 211, Springer-Verlag,
New York, 2002. MR 1878556

[11] Rudolf Lidl and Harald Niederreiter, Finite ﬁelds, second ed., Encyclopedia of Mathe-
matics and its Applications, vol. 20, Cambridge University Press, Cambridge, 1997, With
a foreword by P. M. Cohn. MR 1429394

[12] Guy Robin, Estimation de la fonction de Tchebychef θ sur le k-i`eme nombre premier et
grandes valeurs de la fonction ω(n) nombre de diviseurs premiers de n, Acta Arith. 42
(1983), no. 4, 367–389. MR 736719

[13] J. Barkley Rosser and Lowell Schoenfeld, Approximate formulas for some functions of
prime numbers, Illinois J. Math. 6 (1962), 64–94. MR 137689

[14] A. Schinzel, Primitive divisors of the expression An − Bn in algebraic number ﬁelds, J.
Reine Angew. Math. 268(269) (1974), 27–33. MR 344221

[15] , Addendum to the paper: “On the product of the conjugates outside the unit circle
of an algebraic number” (Acta Arith. 24 (1973), 385–399), Acta Arith. 26 (1974/75),
no. 3, 329–331. MR 371853

[16] Cameron L. Stewart, On divisors of Lucas and Lehmer numbers, Acta Math. 211 (2013),
no. 2, 291–314. MR 3143892

[17] Paul Voutier, An eﬀective lower bound for the height of algebraic numbers, Acta Arith.
74 (1996), no. 1, 81–95. MR 1367580

[18] Bruno Winckler, Th´eor`eme de Chebotarev eﬀectif, arXiv:1311.5715, 2013.

[19] Kunrui Yu, p-adic logarithmic forms and a problem of Erd˝os, Acta Math. 211 (2013),
no. 2, 315–382. MR 3143893

Yuri Bilu & Haojie Hong: Institut de Math´ematiques de Bordeaux, Uni-
versit´e de Bordeaux & CNRS, Talence, France

Sanoli Gun: The Institute of Mathematical Sciences, Taramani, Chennai,
Tamil Nadu, India
 22
