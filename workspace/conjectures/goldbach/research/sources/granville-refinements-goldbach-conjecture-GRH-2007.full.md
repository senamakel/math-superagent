<!-- source: https://dms.umontreal.ca/~andrew/PDF/GoldbachFinal.pdf | converted from PDF -->

Functiones et Approximatio
XXXVII (2007), 7–21

REFINEMENTS OF GOLDBACH’S CONJECTURE, AND THE
GENERALIZED RIEMANN HYPOTHESIS

Andrew Granville
 To Jean-Marc Deshouillers
on the occasion of his sixtieth birthday

Abstract: We present three remarks on Goldbach’s problem. First we suggest a reﬁnement of
Hardy and Littlewood’s conjecture for the number of representations of 2n as the sum of two
primes positing an estimate with a very small error term. Next we show that if a strong form
of Goldbach’s conjecture is true then every even integer is the sum of two primes from a rather
sparse set of primes. Finally we show that an averaged strong form of Goldbach’s conjecture is
equivalent to the Generalized Riemann Hypothesis; as well as a similar equivalence to estimates
for the number of ways of writing integers as the sum of k primes.
Keywords: Goldbach, additive number theory, Riemann zeta function.

1. Three remarks on Goldbach’s conjecture

In 1740 Goldbach conjectured, in a letter to Euler, that every integer > 1 is the
sum of at most three primes. Euler replied that it would suﬃce to prove

Every even integer > 2 is the sum of two primes

and this is now known as “Goldbach’s conjecture”. Recently a publisher, seeking
publicity for a new novel, oﬀered a million dollars for its resolution, but the con-
jecture remains as open today as it ever has been. In 1922 Hardy and Littlewood
[5] guesstimated, via a heuristic based on the circle method, an asymptotic for the
number of representations of an even integer as the sum of two primes: Deﬁne

g(2N ) = #
{p, q prime : p + q = 2N }
.

Their conjecture is equivalent to g(2N ) ∼ I(2N ) where

I(2N ) = C2 ∏

p|N
p>2
 ( p − 1
p − 2
 ) 2N −2∫

2
 dt
log t log(2N − t)

2001 Mathematics Subject Classiﬁcation: 11P32, 11M26.

8 Andrew Granville

and C2 , the “twin prime constant”, is deﬁned by

C2 = 2 ∏

p>2

(
1 − 1
(p − 1)2
 )
 = 1.320323 . . .

We believe that a better guesstimate for g(2N ) is given by

I ∗(2N ) := I(2N )
 

1 − 4
√
2N
 ∏

p⩾3
 (
1 − (2N/p)
p − 2
 )


 , (1.1)

as we will discuss in Section 2; indeed it could well be that

g(2N ) = I ∗(2N ) + O
 ( √
N
log N log log N
 )
 .

In analytic number theory it is usual to study the function ∑
pk⩽x log p in place
of ∑p⩽x 1 since this lends itself more naturally to complex analysis; and then
to recover results about ∑p⩽x 1 by partial summation. Thus we introduce the
function G(2N ) = ∑

p+q=2N
p,q prime
 log p log q.

The analysis of Hardy and Littlewood suggests that G(2N ), plus some terms
corresponding to solutions of pk + ql = 2N , should be very “well-approximated”
by
 J(2N ) := C2 ∏

p|N
p>2
 ( p − 1
p − 2
 ) · 2N,

and the approximation g(2N ) ∼ I(2N ) is then deduced by partial summation.
(In fact we believe that G(2N ) = J(2N ) + O(N 1/2+o(1)).) However this was done
ignoring the contribution of solutions to pk + ql = 2N . So, by including a suitable
correction term to account for this (much like Riemann’s “correction term” in
estimating π(x) which takes account of the contribution of squares of primes in
the explicit formula), we obtain the guesstimate I ∗(2N ) above.
If we believe that G(2N ) is always very well approximated by J(2N ) then,
although this is too hard to prove, it may well be that some averaged form of this
assertion is provable. In our ﬁrst theorem we study the average of this diﬀerence.

Theorem 1A. The Riemann Hypothesis is equivalent to the estimate
∑

2N ⩽x
(G(2N ) − J(2N )) ≪ x
3/2+o(1).

Attempting to generalize this to ﬁnd an equivalent to the generalized Rie-
mann Hypothesis is not quite so simple.
 Goldbach’s conjecture 9

Theorem 1B. The Riemann Hypothesis for Dirichlet L -functions L(s, χ), over
all characters χ mod m which are odd squarefree divisors of q , is equivalent to the
estimate ∑

2N ⩽x
2N ≡2 (mod q)
 (G(2N ) − J(2N )) ≪ x
3/2+o(1).

A similar result holds when the sum is over 2N ≡ a (mod q) with (a, q) = 1 .
Thus we only get a result for characters of squarefree conductor when we consider
these “usual” arithmetic progressions mod q . However we can get a result involving
all Dirichlet characters when we consider the arithmetic progression 0 (mod q).

Theorem 1C. The Riemann Hypothesis for Dirichlet L -functions L(s, χ), χ mod q
is equivalent to the conjectured estimate

∑

2N ⩽x
q|2N
 G(2N ) = 1
φ(q)
 ∑

2N ⩽x G(2N ) + O (
x
1+o(1)) . (1.2)

However notice here that the main term is of size ≍q x
2 so the error term
involves an amazing saving (that is, more than the “usual” x
1/2+o(1) ), which is
unsatisfying.
It is worth noting that similar results hold when trying to write integers as
the sum of k primes: Deﬁne

Gk(n) = ∑

p1+p2+...+pk=n log p1 log p2 . . . log pk

so that G(n) = G2(n). After Vinogradov we know asymptotics for this sum for
each suﬃciently large n, when k ⩾ 3 is given. In fact Gk(n) ∼ Jk(n) for each
n ≡ k mod 2 , where Jk is deﬁned in Section 6. We prove the following.

Theorem 1D. The Riemann Hypothesis is equivalent to the estimate
∑

n⩽x
n≡k (mod 2)
 (Gk(n) − Jk(n)) ≪ x
k−1/2+o(1).

Theorems 1A and 1D are based on the estimate, obtained after summation
on the explicit formula for the number of primes up to x:

∑

n⩽x
Gk(n) = x
k

k! − k ∑

ρ: ζ(ρ)=0
|Imρ|⩽x
 x
ρ+k−1

ρ(ρ + 1)(ρ + 2) . . . (ρ + k − 1) + O(x
k−2+2B+o(1)) (1.3)

where B = sup{Re ρ : ζ(ρ) = 0} .
The prime number theorem states that there are ∼ x/ log x primes ⩽ x
implying that there are ∼ x
2/2 log2 x sums p + q ⩽ x with p, q prime. Thus “on
average” an even integer n ⩽ x has ∼ x/ log2 x representations as p + q with p, q

10 Andrew Granville

prime. This is a lot of representations so one might think that ﬁnding at least one
such representation would not be so diﬃcult. In fact I(2N ) ⩾ C2(2N )/ log2(2N )
for all N ⩾ 4 , so we might expect that

g(2N ) ⩾ C2(2N )/ log
2(2N ) for all N ⩾ 2674.

Musing on the expected large number of representations of each even integer
n as the sum of two primes, it seems likely that there must exist a relatively
“thin” subset P of the primes such that every even integer is the sum of two
primes in P . Deﬁne P (x) to be the number of elements of P up to x. There are
⩽ (
P (x)
2 + P (x)
) /2 distinct pairs p + q ⩽ x with p, q ∈ P (x), so if every even
integer is the sum of two primes in P (x) then

x/2 − 1 ⩽ (
P (x)2 + P (x)
) ∕2,

and thus P (x) ⩾ √
x − 1 for x ⩾ 4 . Our goal, then, is to show that if the Goldbach
conjecture is true then there is such a set P with P (x) “close” to √
x (note that
if we take P to be the set of all primes then P (x) ∼ x/ log x, which is much bigger
than √
x).
The Central Limit Theorem tells us that large sets of random choices, taken
together, tend to converge to a predictable distribution, the “Bell curve”. This
extraordinary tendency allows us to use randomness in all sorts of surprising ways
to prove results in “non-random” problems — This viewpoint was championed by
Paul Erd¨os and discussed in detail in [1]. We use this here to prove:

Theorem 2. Suppose that there exists a constant γ > 0 such that every even
integer n > 2 can be written in more than γn/ log
2 n ways as p+q with p, q prime.
Then there exists a constant η > 0 such that there is an inﬁnite set of primes P ,
with no more than η√x log x elements ⩽ x, such that every even integer n can
be written as p + q with p, q ∈ P.

We shall show that there is such a “thin” set of primes P with this property,
via a fairly simple application of the Central Limit Theorem. We also indicate,
via probabilistic considerations, why we believe that any such set P must have
lim inf P (x)/√x log x > 0 Note that, “on average”, an even integer n has about
log n representations as p + q with p, q ∈ P , far fewer than before.
Wirsing [16] showed that for any integer k ⩾ 3 , there is a set of primes
P , with ≪ (x log x)
1/k elements ⩽ x, such that every integer n ≡ k mod 2 can
be written as p1 + p2 + . . . + pk with p1, p2, . . . , pk ∈ P . In fact our Theorem 2
follows from Wirsing’s Theorem 1 (though was not observed by him) 1 . We were
inspired to prove the above result after reading [15] on a related question, and
before seeing [16].
This result is conditional (on Goldbach’s Conjecture) and it is desirable to
prove something like this unconditionally: By very similar methods we will prove
the following:

1 The right side of the hypothesis (8) in [15] should be “ M (x)x−1/k ”, not “ M (x)−1/k ”.

Goldbach’s conjecture 11

Theorem 3. For any ε > 0 there exists a constant κε > 0 such that there exists
a set of primes Pε with

Pε(x) ⩽ κε√
x for x suﬃciently large,

for which all but at most εx even integers up to x can be written as p + q with
p, q ∈ Pε(x).

Letting ε → 0 we can deduce the following

Corollary. Let g(x) be any function that → ∞ as x → ∞. There exists a set of
primes P such that P (x) ⩽ √
xg(x) for x suﬃciently large for which all but o(x)
even integers up to x can be written as p + q with p, q ∈ P (x).

We will also try to justify our belief later that this cannot be improved.
Let us now review what is known, and what we need to know about Gold-
bach’s problem, and about the Central Limit Theorem.

2. A brief history of Goldbach’s problem: A reﬁned conjecture

Computers have veriﬁed that every even integer 2n ⩽ 4 · 1014 is the sum of two
primes [12]. Chudakov [2], Van der Corput [13] and Estermann [4] showed in 1937
that “almost all” integers are the sum of two primes (that is, all but o(x) up to x):
In 1976 Montgomery and Vaughan [9] showed that the number of exceptions is
O(x
1−c) for some c > 0 , and recently Pintz [10] announced that one can take
c = 1/3 . In 1937 Vinogradov [14] showed that every suﬃciently large odd integer
is the sum of three primes; and in 1995 Ramar´e [11] showed that every integer > 1
can be written as the sum of at most seven primes
The modern heuristic to obtain the constant C2 ∏
 p|N
p>2 p−1
p−2 in I(2N ) runs as
follows: For each prime l , if we take integer p “at random” then the probability
that l does not divide p is 1 − 1/l ; and similarly for q . However if we pick p “at
random” and q = 2N − p then l divides p or q if p ≡ 0 mod l or p ≡ 2N mod l ,
respectively. So the probability that l does not divide either p or q is 1 − 2/l if
l ̸ | 2N , and is 1 − 1/l if l divides 2N . Therefore “the ratio” of these probabilities
is, 2 if l = 2 , and is

1 − 2/l

(1 − 1/l)
2 times { 1 if l ̸ | 2N
(l − 1)/(l − 2) if l|2N, l ⩾ 3.

We will modify this to justify the reﬁnement I ∗ of I , when approximating g .
Let E(2N ) = ∑

pk +ql =2N
k,l⩾1
k+l⩾3
 log p log q.

12 Andrew Granville

First note that
∑

pk +ql=2N
k⩾3
 log p log q ⩽ log2 N · ∑

pk ⩽2N
k⩾3
 1 ≪ N 1/3 log2 N,

and a similar argument works for l ⩾ 3. Also it is well-known that there are N o(1)

pairs of integer p, q with p2 + q2 = 2N. Thus

E(2N ) = 2 ∑

p+q2=2N log p log q + O(N 1/3 log2 N ).

Now, when we study solutions to p+ q2 = 2N we ﬁnd that l divides p if and
only if 2N ≡ q2 mod l . Thus if (2N/l) = 0 or − 1 then l divides pq if and only if
q ≡ 0 mod l . If (2N/l) = 1 then there are 2 non-zero values of q mod l for which
l divides p, and we also need to count when l divides q . Therefore our factor is
2 if l = 2 , and

(1 − 2+(2N/l)
l )

(1 − 1/l)2 times { 1 if l ̸ |2N
(l − 1)/(l − 2) if l|2N, l ⩾ 3.

Now #{m, n > 0 : m + n2 = 2N } = √2N + O(1) so we predict that

∑

p+q2=2N log p log q ∼ ∏

l⩾3
 (1 − (2N/l)
l − 2
 ) C2 ∏

p|2N
p>2
 ( p − 1
p − 2
 ) √
2N .

and thus, after partial summation, that

2 ∑

p+q2 =2N
p,q prime
 1 ∼ 4 ∏

l⩾3
 (
1 − (2N/l)
l − 2
 ) C2 ∏

p|2N
p>2
 ( p − 1
p − 2
 ) √
2N
log2(2N ) .

Subtracting this from I(2N ), we obtain the prediction I ∗(2N ), as in (1.1). We
can give the more accurate prediction

C2 ∏

p|N
p>2
 ( p − 1
p − 2
 )2N −2∫

2
 1
log t log(2N − t)
 

1 − ∏

p⩾3

(
1 − (2N/p)
p − 2
 )( 1
√
t + 1
√
2N − t
 )


 dt

with this method, though this is also signiﬁcantly trickier to calculate.
One might guess that the distribution of

g(2N ) − I ∗(2N )
√
I ∗(2N )
 Goldbach’s conjecture 13

looks Normal; though computer experiments with small 2N by me, and for larger
2N by Richstein, do not seem to justify this guess. It would be good to understand
why not.

3. The Central Limit Theorem and the proofs of the Theorems

Let X1, X2, . . . Xk, be independent random variables and let Y = X1 + . . . + Xk .
Evidently E(Y ) = ∑k
i=1 E(Xi) and a simple computation reveals that the variance

V(Y ): = E
((
Y − E(Y )
)2) =
 k∑

i=1 V(Xi).

Now V(Xi) = E(X 2
i ) − E(Xi)
2 , so if Xi only takes values 0 or 1 then
X 2
i = Xi so that V(Xi) = E(Xi) − E(Xi)
2 ⩽ E(Xi).
The central limit theorem tells us that if E(Y ) → ∞ as k → ∞ then the
probability that Y ⩽ E(Y ) + τ √V(Y ) tends to

1
√2π
 τ∫

−∞ e−t
2/2 dt,

a remarkable result.
In this paper we need explicit results for “small” k in the case that the Xi ’s
only take values 0 or 1 . In this case Chernoﬀ’s Theorem [1] is particularly useful:

Prob
(∣
∣Y − E(Y )
∣
∣ > τ E(Y )
) ⩽ 2 exp
(
−κτ E(Y )
) (3.1)

where κτ = min{
τ 2/2, (1 + τ ) log(1 + τ ) − 1}. In fact κ1 = log(4/e) so that

Prob
(
Y = 0) ⩽ 2(
e/4)E(Y ). (3.2)

Using these results from probability we will deduce the following uncondi-
tional theorem from which we deduce Theorem 2.

Proposition 3.1. For given γ > 0 deﬁne N = Nγ = {2n : g(2n) > 4γn/ log
2(2n)} .
There exists a constant η = ηγ > 0 such that there is an inﬁnite set of primes P ,
with no more than η√x log x elements ⩽ x, such that every integer n ∈ N can
be written as p + q with p, q ∈ P.

Theorem 2 follows immediately from Proposition 3.1. From the proof below
we ﬁnd that we can take η = 4/√
γ + o(1). As we noted in the introduction
we expect that all suﬃciently large n ∈ N when γ = C2/2 ; and Theorem 2
would follow with η = 8/√
2C2 ≈ 4.923057346 . (In fact Proposition 3.1 follows,
more-or-less, from Corollary 2 of [16].)

14 Andrew Granville

Note that, by a strong form of the result of Chudakov/Van der Corput/Ester-
mann, we know that almost all integers n belong to N if γ is suﬃciently small.

In this section we deﬁne Pn = { primes p < n/2 : p and n − p is prime
}

and so #Pn > γn/ log
2 n + O(1) if n ∈ Nγ .
Let θ(x) be a positive real-valued function such that θ(x)/√x is decreasing
for suﬃciently large x, with limit 0 .
Let {wp, p prime} be independent random variables with each wp = 0 or 1 ,
and Prob(wp = 1) = θ(p)/√
p.

For each p ∈ Pn deﬁne vn,p = wpwn−p and note that these are independent
random variables. We have

E(vn,p) = E(wp)E(wn−p) = θ(p)
√
p θ(n − p)
√
n − p ⩾ ( θ(n)
√
n
 )2

if p is suﬃciently large (independent of n). Therefore for

Yn = ∑

pεPn vn,p,

and n ∈ N , we have

E(Yn) = ∑

p∈Pn E(vn,p) ⩾ ( θ(n)
√
n
 )2 · γn
log2 n + O(1) = γ( θ(n)
log n
 )2 + O(1).

Proof of Proposition 3.1. Taking θ(x) = 2(
(log3 x)/γ)1/2 we get E(Yn) ⩾

4 log n + O(1) and so, by (3.1),

Prob(Yn = 0) ≪ (e/4)
4 log n ≪ 1/n3/2. (3.3)

Thus
 Eθ: = E
(
#{n ∈ N: Yn = 0}) ⩽ ∑

n∈N Prob(Yn = 0) ≪ ∑

n⩾1
 1
n3/2 ≪ 1.

Note that Prob
(
#{n ∈ N : Yn = 0} > 100Eθ) ⩽ 1/100.

Thus if we choose a set of primes P “at random” (where “at random” is
according to our probabilities above) then there is a ⩾ 99% chance that no more
than 100Eθ elements of N are not the sum of two elements of P (and so there
certainly exists such a set P ). For such n ∈ N, add p and q to P for some primes

Goldbach’s conjecture 15

p, q with p + q = n. Thus our new set of primes P ′ has the desired property; and
P ′ \ P is ﬁnite.
Next we wish to examine P (x) = #
{
p ∈ P : p ⩽ x
} : Let Wx = ∑
p⩽x wp so
that
 E(Wx) = ∑

p⩽x
 θ(p)
√
p = 2
√
γ
 ∑

p⩽x
 (log p)
3/2

p1/2 ∼ 4√ x
γ log x

by the prime number theorem. By (3.1) we see that

Wx ≪ √
x log x

with probability 1 − o(1) and thus Proposition 3.1 follows.

Proof of Theorem 3. By the result of Chudakov/Van der Corput/Estermann
we know that #{n ∈ N: n ⩽ x} ∼ x/2 . Let ϑ(x) = A log x for some very
large A > 0 , in the argument above, so that E(Yn) = γA
2 + o(1), and thus
Prob (Yn = 0) ≪ (e/4)
γA2 for each n ∈ N. Therefore

E
(
#
{n ⩽ x : Yn = 0}
) ⩽ #{n ⩽ x: n ̸∈ N} + ∑

n⩽x

n∈N
 Prob (Yn = 0)

⩽ o(x) + O(x (e/4)
γA2),

and so there certainly exist such sets P with

#
{
n ⩽ x: Yn = 0} ≪ x(e/4)
γA2.

At the same time we note that

E(Wx) = A ∑

p⩽x
 log p
√p ∼ 2Ax
1/2.

Thus in Theorem 3 we may take ε ≍ (e/4)
γA2 so that κε = 3A ≍ √
log(1/ε).

4. Heuristic

Let Wn be independent random variables with each Wn = 0 or 1 and Prob (Wn =
1) = θ(n)/√n. Let Zn = ∑a+b=n WaWb. Then

Prob(Zn = 0) = ∏

1⩽a⩽n/2 Prob(WaWn−a = 0)

= ∏

1⩽a⩽n/2

(
1 − θ(a)
√
a θ(n − a)
√n − a
 )

16 Andrew Granville

Now ∑

a⩽n−1

( θ(a)θ(n − a)
√
a√n − a
 )2 ⩽ (max
a⩽n θ(a)
)4 ∑

a⩽n−1
 1
a(n − a)

≪ log n
n max
a⩽n (
θ(a)
)4.

So if θ(a) = ao(1),

Prob (Zn = 0) ∼ exp
 

− ∑

1⩽a<n/2
 θ(a)θ(n − a)
√
a(n − a)
 

 .

Suppose θ is non-decreasing and θ (
n1−o(1)) ∼ θ(n). Then it can be shown that

∑

1⩽a<n/2
 θ(a)θ(n − a)
√
a(n − a) ∼ π
2 θ(n)
2 since
 1/2∫

0
 dt
√
t(1 − t) = π
2 .

On the other hand

E
 

∑

a⩽n Wa


 = ∑

a⩽n
 θ(a)
√
a ∼ 2 θ(n)
√
n.

Therefore if we have a random set S of ∼ κ√
x integers up to x, then we expect
that about e−πκ2/8x of the integers n ⩽ x are not the sum of two elements of S .
In particular we don’t believe that the corollary can be improved.
Moreover we expect all but ﬁnitely many integers to be the sum of two
elements of S provided
 ∑

n exp
(− π
2 θ(n)
2) converges.

This happens for θ(n) >
√( 2
π + ε)
log n. So we doubt the consequence of Theorem 2

can be improved (though this suggests we must have η > √
8/π ≈ 1.595769122 ,
whereas above we suggested we could take η < 4.923057346 . . . so there is still
some room for improvement).

5. Goldbach and the Generalized Riemann Hypothesis

The explicit version of the prime number theorem gives a formula of the form

∑

p⩽x log p = x − ∑

ρ
|Im ρ|⩽x
 x
ρ

ρ + O(log2 x),

Goldbach’s conjecture 17

where the sum is over zeros ρ of ζ(ρ) = 0 with Re(ρ) > 0 . In Littlewood’s famous
paper [7] he investigates the sign of π(x) − Li(x) by a careful examination of a
sum of the form ∑ρ: |Im ρ|⩽T Li(x
ρ), showing that this gets bigger than x
1/2−ε for
certain values of x, and smaller than −x
1/2−ε for other values of x. His method
can easily be modiﬁed to show that the above implies that

max
y⩽x
 ∣
∣
∣
∣
∣
 ∑

p⩽y log p − y
∣
∣
∣
∣
∣ = x
B+o(1)

where B = sup
{Re ρ: ζ(ρ) = 0} (note that 1 ⩾ B ⩾ 1/2 ). By partial summation
it is not hard to show that

∑

2N ⩽x G(2N ) = ∑

p+q⩽x log p log q = x
2

2 − 2 ∑

ρ
|Im ρ|⩽x
 x
1+ρ

ρ(1 + ρ) + O(x
2B+o(1)) (5.1)

so that, by Littlewood’s method,

max
y⩽x
 ∣
∣
∣
∣
∣
 ∑

2N ⩽y G(2N ) − y2

2
 ∣
∣
∣
∣
∣ = x
1+B+o(1).

Therefore the Riemann Hypothesis (B = 1/2) is equivalent to the conjectured
estimate ∑

2N ⩽x G(2N ) = x
2

2 + O (x
3/2+o(1)) . (5.2)

This implies Theorem 1A since

∑

2n⩽x J(2n) = C2 ∑

2n⩽x 2n ∑

d|n
d odd
 µ
2(d)
∏

p|d(p − 2)

= 2C2 ∑

d⩽x/2
d odd
 µ
2(d)
∏
p|d(p − 2)
 ∑

n⩽x/2
d|n
 n

= 2C2 ∑

d⩽x/2
d odd
 µ
2(d)
∏
p|d(p − 2)
 ( x
2

8d + O(x)
)

= x
2

2 + O(x log x).
 (5.3)

Going further we note that for any coprime integers a, q ⩾ 2

∑

p⩽x
p≡a (mod q)
 log p = 1
φ(q)
 (
x − ∑

χ (mod q) χ (a) ∑

ρ:L(ρ,χ)=0
|Im ρ|⩽x
 x
ρ

ρ
 ) + O(log2(qx));

18 Andrew Granville

and thus
 max
y⩽x
 ∣
∣
∣
∣ ∑

p⩽y
p≡a (mod q)
 log p − y
φ(q)
 ∣
∣
∣
∣ = x
Bq+o(1), (5.4)

where Bq = sup{Re ρ : L(ρ, χ) = 0 for some χ (mod q)} . R.C. Vaughan noted, in
an exchange of email, that by the same methods but now using the above formula,
we get a remarkable cancellation which leads to the explicit formula

∑

2N ⩽x
q|2N
 G(2N ) − 1
φ(q)
 ∑

2N ⩽x G(2N )

= 1
φ(q)
 ∑

χ (mod q)
χ̸=χ0
 χ(−1) ∑

ρ:L(ρ,χ)=0
σ:L(σ,χ)=0
|Im ρ|,|Im σ|⩽x
 cρ,σ x
ρ+σ + O(x log2(qx))

where cρ,σ = 1∫

0
 1
ρ (1 − t)
ρ tσ−1 dt is a constant depending only on ρ and σ (and

note that cρ,σ = cσ,ρ , integrating by parts, when Re ρ, Re σ > 0 ). Thus Theorem
1C follows since cρ,σ ⩽ (1/ρ) ∫ 1
0 tσ−1dt = 1/ρσ and as ∑
|Im σ|⩽x 1/ρ ≪ log2(qx).
As in the proof of (5.3) we have

∑

2n⩽x
q|2n
 J(2n) = x
2

2φ(q) + O(x log x). (5.5)

Now, Hardy and Littlewood showed that Generalized Riemann Hypothesis implies
that ∑

2n⩽x
 ∣
∣
∣G(2n) − J(2n)
∣
∣
∣
2 ≪ x
5/2+o(1). (5.6)

We expect, as we saw in section 2, that G(2n) − J(2n) ≪ n1/2+o(1) and so we
believe that ∑

2n⩽x
 ∣
∣
∣G(2n) − J(2n)
∣
∣
∣2 ≪ x
2+δ+o(1) (5.7)

for δ = 0 . This implies, by Cauchy’s inequality, that

∑

2n⩽x G(2n) = ∑

2n⩽x J(2n) + O (
x 3+δ
2 +o(1))

= x
2/2 + O (x
(3+δ)/2+o(1))

by (5.3), which implies the Riemann Hypothesis if δ = 0 (as after (5.2) above);
and implies that ζ(ρ) ̸= 0 if Re ρ > 3/4 if δ = 1/2 (that is, assuming Hardy and
Littlewood’s (5.6))
 Goldbach’s conjecture 19

We ﬁnd that (1.2) is too delicate to obtain the Riemann Hypothesis for
L(s, χ), χ (mod q) from (5.7). Instead we note that

∑

2N ⩽x
2N ≡2 (mod q)

G(2N ) = cq
 


 x
2

2 − 2 ∑

m|q
m odd
 µ(m)
∏
 p|m
p>2 (p − 2)
 ∑

χ mod m
χ primitive
 χ(2) ∑

ρ:L(ρ,χ)=0
|Im ρ|⩽x
 x
ρ+1

ρ(ρ + 1)
 




plus an error term O(x
2Bq +o(1)), where cq = (2,q)
q ∏
 p|q
p odd
 p(p−2)
(p−1)2 . As in (5.3) one

can show that ∑

2N ⩽x
2N ≡2 (mod q)
 J(2N ) = cq x
2

2 + O(x log x),

so that ∑

2N ⩽x
2N ≡2 (mod q)
 (G(2N ) − J(2N )) = O(x
1+Cq +o(1))

where Cq = sup{Re ρ : L(ρ, χ) = 0 for some χ mod m, where m|q and m is odd
and squarefree} . This implies Theorem 1B. By the above we see that if (5.7)
holds with δ = 0 then Cq = 1/2 and thus the Riemann Hypothesis follows for
L -functions with squarefree conductor (this was also proved in unpublished work
of Montgomery and Vaughan [8] in 1971 by somewhat diﬀerent means). Surely
one can obtain the Riemann Hypothesis for L -functions with other conductors by
this method, though I have, as yet, been unable to do so.

6. Multi-sums

By methods similar to the previous section one can easily show (1.3) so that

max
y⩽x
 ∣
∣
∣
∣
∣
 ∑

n⩽y G(n) − yk

k!
 ∣
∣
∣
∣
∣ = x
k−1+B+o(1). (6.1)

Therefore the Riemann Hypothesis is equivalent to the conjectured estimate

∑

n⩽x Gk(n) = x
k

k! + O (x
k−1/2+o(1)) .

To use the heuristic of Section 2 we note that

#{a1, . . . , ak mod p : p ̸ |a1 . . . ak and a1 + . . . + ak ≡ n mod p}

= (p − 1)
k − (−1)
k

p + (−1)
kδn,0,

20 Andrew Granville

where δi,j = 1 if i = j , and = 0 otherwise. Now deﬁne

Ck = 2 ∏

p>2
 (p − 1)
k − (−1)
k

(p − 1)k .

If n ̸≡ k mod 2 then deﬁne Jk(n) = 0 . If n ≡ k mod 2 then deﬁne

Jk(n) = Ck nk−1

(k − 1)!
 ∏

p|n
p>2
 (
1 + p(−1)
k

(p − 1)k − (−1)k
 ) .

Let εd be a multiplicative function with εp := p(−1)
k/((p − 1)
k − (−1)
k). Then

∑

n⩽x Jk(n) = Ck ∑

n⩽x
n≡k mod 2
 nk−1

(k − 1)!
 ∑

d|n
d odd
 µ
2(d)εd

= Ck ∑

d⩽x
d odd
 µ
2(d)εd
 ( x
k

2d(k!) + O(x
k−1)
)

= Ck x
k

2(k!)
 ∏

p>2
 (
1 + εp
p
 ) + O(x
k−1) = x
k

k! + O(x
k−1)

for k ⩾ 3 . We deduce Theorem 1D.

7. Concluding remark

Evidently 0 ⩽ g(2N ) ⩽ 2π(2N ) − π(N ) − π(N − 1). Goldbach’s conjecture asserts
that this lower bound in not attained for any N > 1 , that is g(2N ) ̸= 0 for
N ⩾ 2 . We might also ask how often the upper bound is attained? One ﬁnds
that this upper bound is attained for 2N = 210 and Deshouillers, Narkiewicz,
Pomerance and I proved [3] that this is the largest even integer for which this
upper bound is obtained. It is with this collaboration in mind that I am happy to
dedicate this further article on the Goldbach problem to Jean-Marc.

Acknowledgements. I would like to thank Dan Goldston and Bob Vaughan
for useful email discussion concerning section 6; Joerg Richstein for doing the
requested calculations from section 2; and the referee for pointing out the references
[2] and [4].

References
[1] Noga Alon and Joel H. Spencer, The Probabilistic Method, Wiley 1992.
[2] N. Chudakov, On Goldbach’s problem (Russian), Dokl. Akad. Nauk SSSR 17
(1937), 331–334.
 Goldbach’s conjecture 21

[3] Jean-Marc Deshouillers, Andrew Granville, Wladyslaw Narkiewicz and Carl
Pomerance, An upper bound in Goldbach’s problem, Math. Comp. 61 (1993),
209–213.
[4] T. Estermann, On Goldbach’s problem: Proof that almost all even positive
integers are sums of two primes, Proc. London Math. Soc 44 (1938), 307–314.
[5] G.H. Hardy and J.E. Littlewood, Some problems of ’partitio numerorum’;
V: A further contribution to the study of Goldbach’s problem Proc. London
Math. Soc 22 (1924), 46–56.
[6] M. Kolountzakis, On the additive complements of the primes and sets of
similar growth, Acta Arith 77 (1996), 1–8.
[7] J.E. Littlewood, Distribution des nombres premiers, C. R. Acad. Sci. Paris
158 (1914), 1869–1872.
[8] H.L. Montgomery and R.C. Vaughan, Error terms in additive prime number
theory and the GRH, to appear.
[9] H.L. Montgomery and R.C. Vaughan, The exceptional set in Goldbach’s pro-
blem, Acta. Arith 27 (1975), 353–370.
[10] J. Pintz, Explicit formulas and the exceptional set in Goldbach’s problem, to
appear.
[11] O. Ramar´e, On S’nirel’man’s constant, Ann. Sci. Norm. Super. Pisa 21
(1995), 645–705.
[12] J. Richstein, Verifying the Goldbach conjecture up to 4 · 1014, Math. Comp
70 (2000), 1745–1749.
[13] J. G. Van der Corput, Sur l’hypoth`ese de Goldbach, Proc. Acad. Wet. Am-
sterdam 41 (1938), 76–80.
[14] I. M. Vinogradov, Representation of an odd number as a sum of three primes,
Comptes Rendus (Doklady) de l’Acad´emie des Sciences de l’URSS 15 (1937),
291–294.
[15] Van Vu, High order complementary bases of primes, Integers 2 (2002).
[16] E. Wirsing, Thin subbases, Analysis 6 (1986), 285–308.

Address: D´epartement de Math´ematiques et statistique, Universit´e de Montral, CP 6128
succ. Centre-Ville, Montr´eal QC H3C 3J7, Canada
E-mail: andrew@dms.umontreal.ca
Received: 25 April 2006; revised: 7 June 2006
