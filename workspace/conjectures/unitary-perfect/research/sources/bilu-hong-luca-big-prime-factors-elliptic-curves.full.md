<!-- source: https://arxiv.org/pdf/2112.07046 | converted from PDF -->

arXiv:2112.07046v1  [math.NT]  13 Dec 2021Big prime factors in orders of elliptic curves over
ﬁnite ﬁelds

Yuri Bilu
a, Haojie Hongb and Florian Lucaa

December 15, 2021

Abstract

Let E be an elliptic curve over the ﬁnite ﬁeld Fq. We prove that,
when n is a suﬃciently large positive integer, #E(Fqn ) has a prime factor
exceeding n exp(c log n/ log log n).

Contents

1 Introduction 1
1.1 Notation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
2 Auxiliary facts 4
2.1 The Theorems of Stewart . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
2.2 Cyclotomic polynomials and primitive divisors . . . . . . . . . . . . . . . . . . 4
2.3 Counting S-units . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
3 Proof of Theorem 1.1 7
3.1 Case (3.3) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
3.2 Case (3.4) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8

1 Introduction

A Lucas sequence (un)n≥0 is a binary recurrent sequence of integers satisfying
un+2 = run+1 + sun for all n ≥ 0, and with u0 = 0, u1 = 1. The parameters
r, s are assumed to be nonzero coprime integers such that r2 + 4s ̸= 0. In this
case,
 un = α
n − βn

α − β holds for all n ≥ 0,

where α, β are the two roots of the quadratic x
2 − rx − s = 0. It is further as-
sumed that α/β is not a root of unity. The Lucas sequences have nice divisibility
properties. For example, if m, n are positive integers with m | n then um | un.
A primitive divisor of un is a prime factor p of un which does not divide
um for any positive integer m < n and does not divide r2 + 4s. Working with

aSupported by the ANR project JINVARIANT
bSupported by the China Scholarship Council grant CSC202008310189

1

the sequence of algebraic integers of general term vn = (α − β)un = α
n − βn,
one can reformulate the above deﬁnition by saying that a primitive divisor is a
prime number p which divides vn but not vm for any positive integer m < n.
It was shown in [2] that primitive divisors always exist if n ≥ 31. Particular
instances of this result were proved much earlier by Zsygmondy [14] (the case
of rational integers α, β) and Carmichael [5] (the case of real α, β).
It is known that primitive divisors are congruent to ±1 (mod n). In par-
ticular, writing P (m) for the largest prime factor of the integer m with the
convention that P (0) = P (±1) = 1, one has P (un)/n ≥ (n − 1)/n for n ≥ 31.
Erd˝os [7] conjectured that P (un)/n tends to inﬁnity. This was proved to be
so by Stewart [13] who showed that P (un) > n exp(log n/(104 log log n)) holds
for n > n0, where n0 is a constant which Stewart did not compute and which
depends on the discriminant of the ﬁeld Q(α) and the number of distinct prime
factors of s. Explicit values for n0 were computed in [3] at the cost of replacing
1/104 by somewhat smaller constants (see Theorem s 2.1 and 2.2 below). It is
also shown in [3] that n0 depends only on the ﬁeld Q(α), but is independent of
the number of prime divisors of s.
Schinzel [11] generalized the primitive divisor theorem to algebraic numbers
in the following way. Let γ be an algebraic number of degree d which is not
a root of unity, and denote vn = γn − 1. A prime ideal p ⊂ OK is called a
primitive divisor of vn if p appears at positive exponent in the factorization of
the principal fractional ideal vnOK but p does not appear in the factorization
of vmOK for any positive integer m < n.
Schinzel proved that vn has a primitive divisor for n ≥ n0(d). Stewart [12]
gave an explicit value for n0(d) but he assumed that γ has a representation of
the form γ = α/β with coprime integers α, β in OK. An explicit value for n0
without any additional hypothesis was given in [4].
In this note we show that Stewart’s type result can be obtained for recurrent
sequences other than Lucas. We look at the prime factors of a certain linear
recurrent sequences of order 4 which is a particular instance of a norm of a
complex quadratic Lucas sequence. Namely, we let q and a be integers satisfying

q ≥ 2, |a| < 2√
q.

We denote α and ¯α the complex conjugate roots of x
2 − ax + q. We prove the
following theorem.

Theorem 1.1. Set n0 := exp exp(max{1010, 3q}) Let n be a positive integer sat-
isfying n ≥ n0. Then the rational integer (α
n − 1)(¯α
n − 1) has a prime divisor p
satisfying
 p ≥ n exp (0.0001 log n
log log n
 ) .

When q is a prime power, the number

(α − 1)(¯α − 1) = α ¯α − (α + ¯α) + 1 = q − a + 1

is the order of the group #E(Fq) of Fq-rational points on a certain elliptic
curve E. Furthermore, (α
n − 1)(¯α
n − 1) represents the order of the group

2

#E(Fqn ) of Fqn -rational points. The numbers (#E(Fqn ))n≥1 form a linearly re-
current sequence of order 4 with roots 1, α, ¯α, q. Like the Lucas sequences, these
numbers have the property that #E(Fqm ) | #E(Fqn ) when m | n (because Fqn
is an extension of Fqm of degree n/m). However, in spite of those similarities,
some non-trivial new ideas are needed to extend Stewart’s argument to these
sequences, see Subsection 3.2.
Note that big prime factors of orders of elliptic curves were studied before,
albeit in a diﬀerent set-up. For instance, Akbary [1] studied big prime factors of
#E(Fq), where E is a ﬁxed elliptic curve over Q with complex multiplication.
He proved that, for a positive proportion of primes q, the number #E(Fq) has a
prime divisor bigger than qθ, where θ = 1 − e−1/4/2 = 0.6105 . . . We invite the
reader to consult the comprehensive survey [6] for more information.

1.1 Notation

Unless the contrary is stated explicitly, m and n (with or without indices) always
denote positive integers and p (with or without indices) denotes a prime number.
Let K be a number ﬁeld. We denote DK and hK the discriminant and the
class number of K. By a prime of K we mean a prime ideal of the ring of
integers OK. If p is prime of K with underlying rational prime p, then we
denote fp its absolute residual degree and N p = pfp its absolute norm.
We denote h(α) the usual absolute logarithmic height of α ∈ ¯Q:

h(α) = [K : Q]
−1 ∑

v∈MK[Kv : Qv] log+ |α|v,

where log+ = max{log, 0}. Here K is an arbitrary number ﬁeld containing α,
and the places v ∈ MK are normalized to extend standard places of Q; that is,
|p|v = p−1 if v | p < ∞ and |2021|v = 2021 if v | ∞.
If K is a number ﬁeld of degree d and α ∈ K then the following formula is
an immediate consequence of the deﬁnition of the height:

h(α) = 1
d
 ( ∑

σ:K֒→C log+ |σ(α)| + ∑

p max{0, −νp(α)} log N p
)
 ,

where the ﬁrst sum runs over the complex embeddings of K and the second sum
runs over the primes of K. If α ̸= 0 then h(α) = h(α
−1), and we obtain the
formula
 h(α) = 1
d
 ( ∑

σ:K֒→C − log− |α
σ| + ∑

p max{0, νp(α)} log N p
)
 , (1.1)

where log− = min{log, 0}.
Besides log+ and log− we will also widely use

log∗ = max{log, 1}.

We use O1(·) as the quantitative version of the familiar O(·) notation:
A = O1(B) means |A| ≤ B.
 3

2 Auxiliary facts

2.1 The Theorems of Stewart

The following two theorems are, essentially, due to Stewart [13], though in the
present form they can be found in [3], see Theorems 1.4 and 1.5 therein.

Theorem 2.1. Let γ be a non-zero algebraic number of degree d, not a root
of unity. Set p0 = exp(80000d(log∗d)
2). Then for every prime p of the ﬁeld
K = Q(γ) whose absolute norm N p satisﬁes N p ≥ p0, and every positive inte-
ger n we have

νp(γn − 1) ≤ N p exp (
−0.002d
−1 log N p
log log N p
 ) h(γ) log∗n.

Theorem 2.2. Let γ be a non-zero algebraic number of degree 2, not a root of
unity. Assume that N γ = ±1. Set p0 = exp exp(max{108, 2|DK|}), where DK
is the discriminant of the quadratic ﬁeld K = Q(γ). Then for every prime p of K
with underlying rational prime p ≥ p0, and every positive integer n we have

νp(γn − 1) ≤ p exp (
−0.001 log p
log log p
 ) h(γ) log∗n. (2.1)

2.2 Cyclotomic polynomials and primitive divisors

Let K be a number ﬁeld of degree d and γ ∈ K× not a root of unity. We consider
the sequence un = γn − 1. We call a K-prime p primitive divisor of un if

νp(un) ≥ 1, νp(uk) = 0 (k = 1, . . . , n − 1).

Let us recall some basic properties of primitive divisors. We denote by Φn(t)
the nth cyclotomic polynomial.
Items 1 and 2 of the following proposition are well-known and easy, and
item 3 is Lemma 4 of Schinzel [11]; see also [4, Lemma 4.5].

Proposition 2.3. 1. Let p be a primitive divisor of un. Then νp(Φn(γ)) ≥ 1
and N p ≡ 1 mod n; in particular, N p ≥ n + 1.

2. Let p be a primitive divisor of un and p the rational prime underlying p.
If γ is of degree 2 and absolute norm 1, then p ≡ ±1 mod n. More specif-
ically,
 p ≡
 {1 mod n if p splits in Q(γ),
−1 mod n if p is intert in Q(γ).

3. Assume that n ≥ 2d+1. Let p be not a primitive divisor of un. Then
νp(Φn(γ)) ≤ νp(n).

Remark 2.4. In item (2) the ramiﬁed p seem to be missing. However, it is
easy to show that, when N γ = 1 and p ramiﬁes in Q(γ) then νp(γ − 1) > 0 or
νp(γ + 1) > 0. Hence, n = 1 or n = 2 in this case.

4

2.3 Counting S-units

Let S be a set of prime numbers. A positive integer is called S-unit if all its
prime factors belong to S. We denote Θ(x, S) the counting function for S-units:

Θ(x, S) = #{n ≤ x : p | n ⇒ p ∈ S}.

We want to bound this function from above.

Proposition 2.5. Let S be a set of k prime numbers. Then for x ≥ 3 we have

Θ(x, S) ≤ exp (
2k1/2 log log x + 20 ( log x
log∗k
 ) log∗( k log∗k
log x
 )) . (2.2)

To start with, note the following trivial bound.

Proposition 2.6. In the set-up of Proposition 2.5 assuming x ≥ 7 we have

Θ(x, S) ≤ exp(2k log log x). (2.3)

Proof. If n ≤ x then for every p we have νp(n) ≤ log x/ log 2. Hence

Θ(x, S) ≤ ( log x
log 2 + 1)k ≤ exp(2k log log x),

as wanted.

Next, let us consider a special case, when the primes from S are not too
small.

Proposition 2.7. In the set-up of Proposition 2.5, assume that p ≥ k1/2 for
every p ∈ S. Then

Θ(x, S) ≤ exp (
10 ( log x
log∗k
 ) log∗( k log∗k
log x
 )) . (2.4)

Proof. If x < 7, then either Θ(x, S) = 0 so the above inequality is trivially true,
or k ≤ 25, and the right–hand side above is at least

exp (( 10
log 25
 ) log x
) > x
3 > ⌊x⌋ ≥ Θ(x, S).

If x ≥ 7 and k ≤ 2 then (2.4) follows from (2.3). From now on we assume that
k ≥ 3; in particular, log∗k = log k. Write S = {p1, p2, . . . , pk}. Then every S-
unit n can be presented as pa1
1 · · · pak
k with non-negative integers a1, . . . , ak. If
n ≤ x then a1 log p1 + · · · + ak log pk ≤ log x.

By the assumption, log pi ≥ (1/2) log k for i = 1, . . . , k. Hence,

a1 + · · · + ak ≤ ℓ, (2.5)

5

where ℓ = ⌊2 log x/ log k⌋. We may assume that ℓ ≥ 1: if ℓ = 0 then the only
solution of (2.5) is a1 = · · · = ak = 0, and Θ(x, S) = 1. For further use, note
that log x
log k ≤ ℓ ≤ 2 ( log x
log k
 ) .

Inequality 2.5 has exactly ℓ∑

i=0
 (
k + i
i
 )

solutions in (a1, . . . , ak) ∈ Z
k
≥0. Hence,

Θ(x, S) ≤ (ℓ + 1)
(
k + ℓ
ℓ
 )

≤ (ℓ + 1) (
e ( k + ℓ
ℓ
 ))ℓ

≤ exp (
ℓ log (
2e ( k + ℓ
ℓ
 ))) (we used ℓ + 1 ≤ 2ℓ)

≤ exp (
2 ( log x
log k
 ) log (
2e ( k + ℓ
ℓ
 ))) .

If k ≤ 9ℓ then
 log (
2e k + ℓ
ℓ
 ) ≤ log(20e) < 4,

and we are done. If k ≥ 9ℓ then

log (
2e ( k + ℓ
ℓ
 )) ≤ log (
8 ( k
ℓ
 )) ≤ log (8 ( k log k
log x
 )) ≤ 4 log∗( k log k
log x
 ) ,

and we are done again.

Proof of Proposition 2.5. Write S = S1 ∪ S2, where

S1 = {p ∈ S : p < k1/2}, S2 = {p ∈ S : p ≥ k1/2}.

Then, clearly Θ(x, S) ≤ Θ(x, S1)Θ(x, S2). We estimate Θ(x, S1) using Proposi-
tion 2.6 and Θ(x, S2) using Proposition 2.7:

Θ(x, S1) ≤ exp(2k1/2 log log x),

Θ(x, S2) ≤ exp (
10 ( log x
log∗(k − k1/2)
 ) log∗( k log∗k
log x
 ))

≤ exp (
20 ( log x
log∗k
 ) log∗( k log∗k
log x
 )) .

The result follows.
 6

3 Proof of Theorem 1.1

Denote K = Q(α). It is an imaginary quadratic ﬁeld. Hence, for a non-zero
θ ∈ OK we have
 h(θ) = log |θ| = 1
2
 ∑

p νp(θ) log N p,

the sum being over the ﬁnite primes of K.
We apply this with θ = Φn(α) (recall that Φn(t) denotes the nth cyclotomic
polynomial). We have

log |Φn(α)| = ϕ(n) log |α|+∑

d|n µ ( n
d
 ) log |1−α
−d| = 1
2 ϕ(n) log q+O1(5). (3.1)

Indeed, we have |α| = q1/2 ≥ √
2 and ∣
∣log |1 + z|
∣
∣ ≤ 2|z| for |z| ≤ 1/√
2. Hence
∣
∣
∣
∣
∣
∣
∑

d|n µ ( n
d
 ) log |1 − α
−d|
∣
∣
∣
∣
∣
∣ < 2
 ∞∑

d=1 |α|−d < 5,

which proves (3.1). Thus,
∑

p νp(Φn(α)) log N p = ϕ(n) log q + O1(10).

Proposition 2.3.3 implies that, for n ≥ 8,
∑

p not primitive νp(Φn(α)) log N p ≤ 2 log n,

the sum being over p which are non-primitive divisors of α
n − 1. Hence,
∑

p primitive νp(Φn(α)) log N p ≥ ϕ(n) log q − 10 − 2 log n.

The Euler totient function ϕ(n) satisﬁes

ϕ(n) ≥ 0.5 n
log log n (n ≥ 1020) (3.2)

(see [10, Theorem 15]). Hence for n ≥ 1020 we have
∑

p primitive νp(Φn(α)) log N p ≥ 0.8ϕ(n) log q.

From now on, the proof splits into two cases, depending on whether the primes
with residual degree 1 contribute more to the sum, or those with residual de-
gree 2 do. Precisely, we have

either ∑

p primitive
fp=1
 νp(Φn(α)) log N p ≥ 0.4ϕ(n) log q, (3.3)

or ∑

p primitive
fp=2
 νp(Φn(α)) log N p ≥ 0.4ϕ(n) log q. (3.4)

7

Case (3.3) is easier, the proof follows the same lines as the proof of Theorem 1.2
in [3]. Case (3.4) is harder and requires more intricate arguments.

3.1 Case (3.3)

We will apply Theorem 2.1 with γ = α and K = Q(α), so that d = 2 and
p0 = exp(160000). We may assume that n > p0, because n0 from Theorem 1.1
is bigger than p0.
Let P be the biggest rational prime p with the following two properties: p
splits in K = Q(α), and α
n − 1 admits a primitive divisor p with underlying
prime p. We want to show that

P > n exp (
0.0002 log n
log log n
 ) . (3.5)

Let p be a primitive divisor of α
n − 1 with fp = 1, and p the underlying rational
prime. Then p ≤ P and p = N p ≡ 1 mod n by Proposition 2.3.1. In particular,
p > n > p0, and Theorem 2.1 applies:

νp(α
n − 1) ≤ p exp (
−0.001 log p
log log p
 ) · 1
2 log q log n

≤ P exp (
−0.001 log n
log log n
 ) log q log n.

Hence,

∑

p primitive
fp =1
 νp(Φn(α)) log N p ≤ π(P ; n, 1)P exp (
−0.001 log n
log log n
 ) log q log n log P,

where, as usual π(x; m, a) counts prime in the residue class a mod m. Estimating
trivially π(P ; n, 1) ≤ P/n, we obtain

∑

p primitive
fp=1
 νp(Φn(α)) log N p ≤ P 2 log P
n exp (
−0.001 log n
log log n
 ) log n log q.

Compared with (3.3), this implies

P 2 log P ≥ 0.4 nϕ(n)
log n exp (
0.001 log n
log log n
 ) .

Using (3.2), this implies (3.5) for n > n0.

3.2 Case (3.4)

If p is a prime of K with fp = 2 then it is a rational prime, and we write p
instead of p. For such p we have νp(α
n − 1) = νp(¯α
n − 1). Setting γ = ¯α/α, we
obtain
 νp(γn − 1) ≥ νp(
(¯α
n − 1) − (α
n − 1)
) ≥ νp(α
n − 1) ≥ νp(Φn(α)).

8

Hence, (3.4) implies the inequality
∑

p∈P νp(γn − 1) log p ≥ 0.2ϕ(n) log q

(note that N p = p2), where the set P consists of the rational primes p inert
in K and satisfying νp(α
n − 1) > 0:

P = {p inert in K and νp(α
n − 1) > 0}.

We are now tempted to bound the sum on the left as we did in Subsection 3.1,
but with Theorem 2.1 replaced by Theorem 2.2, which applies here because
N γ = 1. However, now instead of p ≡ 1 mod n we have merely p2 ≡ 1 mod n,
and we have to use a more delicate argument.
Denote vn = γn − 1. If νp(vn) > 0 then there is a divisor d of n such that p
is primitive for vn/d. We denote it dp. We have

νp(vn) ≤ νp(vn/dp ) + ∑

m|n
m̸=n/dp
 νp(Φm(γ)).

Proposition 2.3.3 bounds the sum on the right by

∑

m|n νp(m) +
 7∑

m=1 νp(Φm(γ)).

It follows that
∑

p∈P νp(γn − 1) log p ≤ ∑

p∈P νp(vn/dp ) + ∑

m|n log m +
 7∑

m=1
 ∑

p νp(Φm(γ)) log p.

The middle sum on the right is trivially estimated by τ (n) log n, where τ (n)
denotes the number of divisors of n:

τ (n) = ∑

m|n 1.

To estimate the double sum on the right, note that

νp(Φm(γ)) ≤ νp(vm) ≤ 1
2 νp((α
m − ¯α
m)
2)
.

Since (α
m − ¯α
m)
2 is a rational integer of absolute value not exceeding 4qm, this
implies that ∑

p νp(vm) log p ≤ 1
2 m log q + log 2. (3.6)

Hence, 7∑

m=1
 ∑

p νp(Φm(γ)) log p ≤ 14 log q + 7 log 2.

Putting all this together, we obtain the inequality
∑

p∈P νp(vn/dp ) log p ≥ 0.2ϕ(n) log q − τ (n) log n − 14 log q − 7 log 2.

9

3.2.1 Disposing of big dp

We want to get rid in our sum of primes p with dp ≥ τ (n) log n. Using (3.6), we
obtain ∑

dp≥τ (n) log n νp(vn/dp ) log p ≤ 1
2 n log q ∑

d|n
d≥τ (n) log n
 1
d + τ (n) log 2

The sum on the right is trivially estimated as

τ (n)
τ (n) log n = 1
log n .

Hence , ∑

dp≥τ (n) log n νp(vn/dp ) log p ≤ n
2 log n log q + τ (n) log 2.

Denote by P ′ the subset of P consisting of p with dp < τ (n) log n:

P ′ = {p ∈ P : dp < τ (n) log n}.

Then we obtain
∑

p∈P ′ νp(vn/dp ) log p ≥ 0.2ϕ(n) log q − τ (n) log n − 14 log q − 7 log 2

− n
2 log n log q − τ (n) log 2.

We have
 τ (n) ≤ exp (
1.1 log n
log log n
 ) (n ≥ 3) (3.7)

(see [8, Theorem 1]). Using this and (3.2), we deduce that, for

n ≥ n0 ≥ exp exp(1010)

(which is true by assumption), we have
∑

p∈P ′ νp(vn/dp ) log p ≥ 0.1ϕ(n) log q. (3.8)

3.2.2 Counting divisors d < τ (n) log n

The number of divisors d < τ (n) log n can be estimated using Proposition 2.5.
Denote x = τ (n) log n and denote by S the set of prime factors of n, so that
#S = ω(n). Then

#{d | n : d < x} ≤ Θ(x, S)

≤ exp (
2ω(n)
1/2 log log x + 20 log x
log∗ω(n) log∗ ω(n) log∗ω(n)
log x
 ) .

10

For further use, note the trivial estimates

log τ (n) ≥ ω(n) log 2, (3.9)

log τ (n) ≤ ω(n) log ( log n
log 2 + 1) ≤ 2ω(n) log log n (3.10)

(recall that n ≥ exp exp(1010)). Note also the estimates

log τ (n) ≤ 1.1 log n
log log n , (3.11)

ω(n) ≤ 1.4 log n
log log n (3.12)

(see (3.7) and [9, Th´eor`eme 11]).
Using (3.11) and (3.12), we deduce that, for n ≥ exp exp(1010), we have

2ω(n)
1/2 log log x ≤ (log n)
1/2 log log n. (3.13)

Using (3.9) and (3.12), we deduce that

ω(n) log∗ω(n)
log x ≤ ω(n) log∗ω(n)
log τ (n) ≤ log∗ω(n)
log 2 ≤ 2 log log n. (3.14)

To estimate log x/ log∗ω(n), we consider two cases. Assume ﬁrst that

ω(n) ≤ log n
(log log n)3 .

In this case, using (3.10), we estimate

log x
log∗ω(n) ≤ 2ω(n) log log n + log log n
1 ≤ 3ω(n) log log n ≤ 3 log n
(log log n)2 .

Now assume that ω(n) ≥ log n
(log log n)3 .

In this case, using (3.11), we obtain

log x
log∗ω(n) ≤ 1.1 log n
log log n + log log n

log log n − 3 log log log n ≤ 3 log n
(log log n)2 .

Thus, in any case log x
log∗ω(n) ≤ 3 log n
(log log n)2 .

Putting this all together, we obtain

#{d | n : d < x} ≤ exp (
(log n)
1/2 log log n + 20 · 3 log n
(log log n)2 log(2 log log n)
)

≤ exp (
70 log n log log log n
(log log n)2
 ) . (3.15)

11

3.2.3 The cardinality of P ′

The crucial step is estimating the number of primes in the set P ′. Denote P
the biggest element of P ′. We are going to prove that

#P ′ ≤ ( P
n + 1) exp (
80 log n log log log n
(log log n)2
 ) . (3.16)

Let p be a prime from the set P ′. Recall that n | p2 − 1; in particular,
p > 2. Assume ﬁrst that n is odd. In this case the numbers gcd(p − 1, n) and
gcd(p + 1, n) are coprime. We write them, respectively, d and n/d. Thus, we
have p ≡ −1 mod n/d, p ≡ 1 mod d (3.17)

for some d dividing n and such that gcd(n/d, d) = 1. By the deﬁnition of dp we
must have d | dp. In particular, if p ∈ P ′ then d < τ (n) log n.
By the Chinese Remainder Theorem, for every d | n such that gcd(n/d, d) = 1,
there exists a unique ad ∈ {1, . . . , n − 1} such that p ≡ ad mod n holds for ev-
ery p satisfying (3.17). It follows that

#P ′ ≤ ∑

d|n
d<τ (n) log n
 π(P ; n, ad).

We estimate trivially π(P ; n, ad) ≤ P/n + 1. Hence, when n is odd, we have the
upper bound
 #P ′ ≤ ( P
n + 1) #{d | n : d < τ (n) log n}. (3.18)

If n is even, the argument is similar, but slightly more complicated. Assume,
for instance, that p ≡ 3 mod 4. Then the numbers

gcd ( p − 1
2 , n
2
 ) , gcd (p + 1, n
2
 )

are coprime, and we write them d and n/2d, respectively; note also that d is odd.
We have 2d | dp, and, in particular, d < τ (n) log n. The system of congruences

p ≡ −1 mod n
2d , p ≡ 1 mod d

is equivalent to p ≡ ad mod n/2, where ad ∈ {1, . . . , n/2 − 1} depends only on d.
Similarly, when p ≡ 1 mod 4, we have p ≡ bd mod n/2, where d < τ (n) log n and
bd ∈ {1, . . . , n/2 − 1} depends only on d. We obtain

#P ′ ≤ ∑

d|n
d<τ (n) log n
 (
π(P ; n/2, ad) + π(P ; n/2, bd)
)

≤ (
4 P
n + 2) #{d | n : d < τ (n) log n}. (3.19)

12

We see that upper bound (3.19) holds in all cases. Combining it with (3.15),
we obtain
 #P ′ ≤ ( P
n + 1
2
 ) exp (
70 log n log log log n
(log log n)2 + log 4) ,

which is sharper than (3.16).

3.2.4 Using Stewart

Now it is the time to use Theorem 2.2. To start with, note that |DK| ≤ q.
Hence, p0 from Theorem 2.2 does not exceed n1/2
0 . Now if νp(γn − 1) > 0 then
n | p2 − 1, see Proposition 2.3.1. Hence, p > n1/2 ≥ n1/2
0 ≥ p0, and Theorem 2.2
applies. For p ∈ P ′ it gives

νp(γn − 1) ≤ p exp (
−0.001 log p
log log p
 ) h(γ) log n

≤ 2P exp (−0.0005 log n
log log n
 ) log q log n, (3.20)

because p ≤ P, log p
log log p ≥ 1
2 log n
log log n , h(γ) ≤ 2q.

Since νp(vn/dp ) ≤ νp(γn − 1), we can combine (3.20) with (3.8), obtaining

2P log P exp (−0.0005 log n
log log n
 ) #P ′ log q log n ≥ 0.1ϕ(n) log q.

Using (3.16) and (3.2), this implies, for n ≥ exp exp(1010), that

P (P + n) log P ≥ n2 exp ((
0.0004 − 100 log log log n
log log n
 ) log n
log log n
 )

≥ n2 exp (
0.0003 log n
log log n
 ) .

If P < n then the latter inequality is clearly impossible for n ≥ exp exp(1010).
Hence, P ≥ n, and we obtain

P 2 log P ≥ 1
2 n2 exp (
0.0003 log n
log log n
 ) ,

which implies
 P ≥ n exp (
0.0001 log n
log log n
 ) .

Theorem 1.1 is proved.
 13

References

[1] Amir Akbary, On the greatest prime divisor of Np, J. Ramanujan Math. Soc. 23 (2008),
no. 3, 259–282. MR 2446601

[2] Yu. Bilu, G. Hanrot, and P. M. Voutier, Existence of primitive divisors of Lucas and
Lehmer numbers, J. Reine Angew. Math. 539 (2001), 75–122, With an appendix by M.
Mignotte. MR 1863855

[3] Yuri Bilu, Haojie Hong, and Sanoli Gun, Uniform explicit Stewart’s theorem on prime
factors of linear recurrences, arXiv:2108.09857 (2021).

[4] Yuri Bilu and Florian Luca, Binary polynomial power sums vanishing at roots of unity,
Acta Arith. 198 (2021), no. 2, 195–217. MR 4228301

[5] R. D. Carmichael, On the numerical factors of the arithmetic forms αn ± βn, Ann. of
Math. (2) 15 (1913/14), no. 1-4, 49–70. MR 1502459

[6] Alina Carmen Cojocaru, Primes, elliptic curves and cyclic groups, Analytic methods
in arithmetic geometry, Contemp. Math., vol. 740, Amer. Math. Soc., [Providence], RI,
[2019] ©2019, With an appendix by Cojocaru, Matthew Fitzpatrick, Thomas Insley and
Hakan Yilmaz, pp. 1–69. MR 4033729

[7] Paul Erd˝os, Some recent advances and current problems in number theory, Lectures on
Modern Mathematics, Vol. III, Wiley, New York, 1965, pp. 196–244. MR 0177933

[8] J.-L. Nicolas and G. Robin, Majorations explicites pour le nombre de diviseurs de N ,
Canad. Math. Bull. 26 (1983), no. 4, 485–492. MR 716590

[9] Guy Robin, Estimation de la fonction de Tchebychef θ sur le k-i`eme nombre premier et
grandes valeurs de la fonction ω(n) nombre de diviseurs premiers de n, Acta Arith. 42
(1983), no. 4, 367–389. MR 736719

[10] J. Barkley Rosser and Lowell Schoenfeld, Approximate formulas for some functions of
prime numbers, Illinois J. Math. 6 (1962), 64–94. MR 137689

[11] A. Schinzel, Primitive divisors of the expression An − Bn in algebraic number ﬁelds, J.
Reine Angew. Math. 268(269) (1974), 27–33. MR 344221

[12] C. L. Stewart, Primitive divisors of Lucas and Lehmer numbers, Transcendence the-
ory: advances and applications (Proc. Conf., Univ. Cambridge, Cambridge, 1976), 1977,
pp. 79–92. MR 0476628

[13] Cameron L. Stewart, On divisors of Lucas and Lehmer numbers, Acta Math. 211 (2013),
no. 2, 291–314. MR 3143892

[14] K. Zsigmondy, Zur Theorie der Potenzreste, Monatsh. Math. Phys. 3 (1892), no. 1,
265–284. MR 1546236

Yuri Bilu & Haojie Hong: Institut de Math´ematiques de Bordeaux, Universit´e de
Bordeaux & CNRS, Talence, France

Florian Luca: School of Maths, Wits University, South Africa and King Abdulaziz Uni-
versity, Jeddah, Saudi Arabia and IMB, Universit´e de Bordeaux, France and Centro de Cien-
cias Matematicas UNAM, Morelia, Mexico
 14
