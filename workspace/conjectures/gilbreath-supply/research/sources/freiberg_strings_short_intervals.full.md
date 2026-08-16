<!-- source: https://arxiv.org/pdf/1005.4703 | converted from PDF -->

arXiv:1005.4703v2  [math.NT]  26 Aug 2010
STRINGS OF CONGRUENT PRIMES IN SHORT INTERVALS

TRISTAN FREIBERG

Abstract. Fix ǫ > 0, and let p1 = 2, p2 = 3, . . . be the sequence of all primes. We prove
that if (q, a) = 1 then there are inﬁnitely many pairs pr, pr+1 such that pr ≡ pr+1 ≡ a mod q
and pr+1 − pr < ǫ log pr. The proof combines the ideas of Shiu [9] and Goldston-Pintz-
Yıldırım [6].
 1. Introduction

Fix any ǫ > 0. In 2005, Goldston, Pintz and Yıldırım proved [4, 6] that there are arbitrarily
large x for which there are at least two primes in the interval (x, x+ ǫ log x], thus establishing
the longstanding conjecture that there are inﬁnitely many pairs of consecutive primes pr, pr+1
with pr+1 − pr < ǫ log pr.

In [5] they extended their original argument to prove that there are arbitrarily large x for
which there are at least two primes in the interval (x, x + ǫ log x] which are both in the
arithmetic progression a mod q, provided (q, a) = 1. However one cannot deduce that these
are consecutive primes for there might be a prime in-between them that is not ≡ a mod q.
Hence one can only deduce that either there are inﬁnitely many pairs of consecutive primes
pr ≡ pr+1 ≡ a mod q with pr+1 − pr < ǫ log pr, or that there are inﬁnitely many triples of
consecutive primes pr, pr+1, pr+2 with pr+2 − pr < ǫ log pr. Presumably both statements are
true but one can only deduce that one of them is true, and one does not know which one,
from the result in [5].

In [9], Shiu proved an old conjecture of Chowla that there are inﬁnitely many pairs of
consecutive primes pr, pr+1 which are both ≡ a mod q. Indeed he was even able to extend
this to k consecutive primes. In this paper we will combine the methods of Goldston-Pintz-
Yıldırım and of Shiu to establish the following hybrid of those results:

Theorem 1.1. Let q ⩾ 3 and a be integers with (q, a) = 1, and ﬁx any ǫ > 0. There
exist inﬁnitely many pairs of consecutive primes pr, pr+1 such that pr ≡ pr+1 ≡ a mod q and
pr+1 − pr < ǫ log pr.
 1

2. Preliminaries

In this section we will state two key technical propositions, to be proved in sections 4 and
5. The ﬁrst proposition requires some preparation. We begin by quoting the Landau-Page
theorem, a proof of which can be found in [2, Chapter 14]. This theorem is used to handle
problems arising from possible irregularities in the distribution of primes, hence in Bombieri-
Vinogradov type theorems (see Lemma 4.2), caused by potential Siegel zeros.

Lemma 2.1 (Landau-Page theorem). There exists a constant c such that the following holds
for any Y > c. There is at most one integer q0 ⩽ Y , and at most one real primitive character
χ0 mod q0, such that
 L(1 − δ, χ0, q0) = 0 for some δ ⩽ 1
3 log Y .

If q0 exists, then q0 > (log Y )2. We call χ0 an exceptional character and q0 an exceptional
modulus.

Throughout, we ﬁx a number ǫ > 0, we let H be a real parameter tending monotonically to
inﬁnity, and we set N := exp(H/ǫ), that is H = ǫ log N. If there is an exceptional modulus
q0 := q0(H) ⩽ exp(H/ǫ(log(H/ǫ))2) = N 1/(log log N )2, let p0 := p0(H) be its greatest prime
factor; otherwise let p0 = 1.

For all suﬃciently large H, either

p0 = 1 or p0 is a prime with p0 > log H. (2.1)

To see this, note that all real primitive characters are products of Legendre symbols with
diﬀerent odd primes, and possibly either the unique real character mod 4 or one of the two
primitive real characters mod 8. Thus if q0 exists it is of the form 2αp1 · · · pk, where α ⩽ 3
and the pi’s are distinct odd primes. If this is the case and p0 ⩽ log H, then the prime
number theorem implies q0 ≪ exp((1 + o(1)) log H) ≪ log N, but Lemma 2.1 states that
q0 > (log N/(log log N)2)2.

We let Q := Q(H) be a positive integer, upon which we will impose the following conditions:

Q is composed only of primes p ⩽ H, (2.2)

Q is divisible by all primes p ⩽ log H, (2.3)

Q ⩽ exp (
cH/(log H)2) for some constant c > 0, (2.4)

if p0(H) ̸= 1 then p0(H) does not divide Q. (2.5)

2

We let
 H := {Qx + h1, . . . , Qx + hk}, h1, . . . , hk ∈ [1, H] ∩ Z, (2.6)

denote a set of distinct linear forms, and we deﬁne

ΛR(n; H, j) := 1
j!
 ∑′

d|P (n;H)
d⩽R
 µ(d)(log R/d)j, (2.7)

where ∑′ denotes summation over indices coprime with Qp0, and

P (n; H) := (Qn + h1) · · · (Qn + hk). (2.8)

Finally, we let
 ϑ(n) :=
 



log n if n is prime,

0 otherwise.

Proposition 2.2. Given ǫ > 0 and suﬃciently large H, let N and p0 = p0(H) be as
deﬁned earlier, and let Q = Q(H) be a positive integer satisfying (2.2) – (2.5). Fix positive
integers k and ℓ, and let H = {Qx + h1, . . . , Qx + hk} be a set of distinct linear forms with
h1, . . . , hk ∈ [1, H] ∩ Z and (Q, h1, . . . , hk) = 1. Let h ∈ [1, H] ∩ Z and suppose (Q, h) = 1,
and let R = N 1/4−ǫ′ for some ǫ
′ ∈ (0, 1/4). As H → ∞, we have

1
N
 (φ(Q)
Q
 )k ∑

N <n⩽2N ΛR(n; H, k + ℓ)2 ∼ (
2ℓ
ℓ
 )(log R)k+2ℓ

(k + 2ℓ)! (2.9)

and
 1
N
 (φ(Q)
Q
 )k ∑

N <n⩽2N ϑ(Qn + h)ΛR(n; H, k + ℓ)2

∼
 



 Q
φ(Q)
(2ℓ
ℓ
 ) (log R)k+2ℓ

(k + 2ℓ)! if Qx + h ̸∈ H,

(
2(ℓ + 1)
ℓ + 1
 ) (log R)k+2ℓ+1

(k + 2ℓ + 1)! if Qx + h ∈ H.
 (2.10)

Proposition 2.3. Let q ⩾ 3 and a be integers with (q, a) = 1, and for a given H, let
p0 = p0(H) be as deﬁned earlier. There is an inﬁnite sequence of integers H1 < H2 < . . .
such that for any i, taking H = Hi, there exists a positive integer Q = Q(H), divisible by q
and satisfying (2.2) – (2.5), such that

|S| − |T | ≫q H (φ(Q)
Q
 ) , (2.11)

3

where
 S = S(H) := {h ∈ (0, H] : (Q, h) = 1 and h ≡ a mod q},

T = T (H) := {h ∈ (0, H] : (Q, h) = 1 and h ̸≡ a mod q}. (2.12)

The implied constant in (2.11) depends at most on q.

3. Proof of Theorem 1.1

Fix integers q ⩾ 3 and a with (q, a) = 1. Recall that H = ǫ log N, with ǫ > 0 ﬁxed, and p0 is
the greatest prime factor of the exceptional modulus q0 ⩽ N 1/(log log N )2, if it exists, otherwise
p0 = 1. We choose H, Q = Q(H), S = S(H), and T = T (H) as in Proposition 2.3, so that
Q is divisible by q and satisﬁes (2.2) – (2.5), and

Q
φ(Q) |S| − |T |
log N ⩾ c(q)ǫ (3.1)

for some constant c(q) > 0, depending on q at most.

We ﬁx positive integers k, ℓ (to be speciﬁed later), and we let H = {Qx + h1, . . . , Qx + hk}
be a set of distinct linear forms such that, for each i, hi ∈ [1, H] ∩ a mod q and (Q, hi) = 1.
We let R = N 1/4−ǫ′ with 0 < ǫ
′ < 1/4 (to be speciﬁed later), and we put

L :=

1
N
 ( φ(Q)
Q
 )k ∑

N <n⩽2N
 (
∑

h∈S ϑ(Qn + h) − ∑

h∈T ϑ(Qn + h) − log 3QN
)
 ΛR(n; H, k + ℓ)2.

We now show that if L > 0 for a sequence of numbers N, tending to inﬁnity, then Theorem
1.1 follows.

Let
 An := {p ∈ (Qn, Qn + H] : p ≡ a mod q} = {p : p = Qn + h, h ∈ S}

Bn := {p ∈ (Qn, Qn + H] : p ̸≡ a mod q} = {p : p = Qn + h, h ∈ T }.

If L > 0, then there is some n ∈ (N, 2N] such that

|An| log(Qn + H) ⩾ ∑

h∈S ϑ(Qn + h) > ∑

h∈T ϑ(Qn + h) + log 3QN ⩾ |Bn| log Qn + log 3QN.

Now |An| log (1 + H/Qn) ⩽ |An| H/Qn ⩽ H 2/QN < log(3/2)
4

if N is suﬃciently large, and so

log(3/2) + (|An| − |Bn|) log Qn > log 3QN

and hence, as n ⩽ 2N, |An| − |Bn| > 1. But as these are integers, |An| ⩾ |Bn| + 2, and so,
by the pigeonhole principle, An contains a pair of consecutive primes pr, pr+1. These primes
satisfy pr+1 − pr < H < ǫ log QN < ǫ log pr.

Now, by our choice of H, a straightforward application of Proposition 2.2 yields

L = (2ℓ
ℓ
 ) (log R)k+2ℓ

(k + 2ℓ)!

×
 { Q
φ(Q)
 ∑

h∈S
Qx+h̸∈H
 1 + 2(2ℓ + 1)
ℓ + 1 log R
k + 2ℓ + 1
 ∑

h∈S
Qx+h∈H
 1 − Q
φ(Q)
 ∑

h∈T 1 − (1 + o(1)) log 3QN
}
.

We have ∑

h∈S
Qx+h∈H
 1 = k, ∑

h∈S
Qx+h̸∈H
 1 = |S| − k,

log R = (1/4 − ǫ
′) log N, and log 3QN ∼ log N by (2.4), therefore

L = (
2ℓ
ℓ
 )(log R)k+2ℓ

(k + 2ℓ)! log N

× { Q
φ(Q) |S| − |T |
log N + 2(2ℓ + 1)
ℓ + 1 k
k + 2ℓ + 1
 ( 1
4 − ǫ
′) − (1 + o(1))} .

We have written o(1) for kQ/(φ(Q) log N), because Q/φ(Q) ≪ log log Q ≪ log log N.

By choosing ℓ = [√k] and k suﬃciently large, the bracketed expression {· · · } above is, by
(3.1), ⩾ c(q)ǫ + 1 − 5ǫ
′ − (1 + o(1)) = c(q)ǫ − 5ǫ
′ − o(1).

By choosing ǫ
′ = c(q)ǫ/10 (we may assume that ǫ is small enough so that ǫ
′ < 1/4), we
deduce that
 L ≫k c(q)ǫ(log N)k+2ℓ+1 (3.2)

holds if N is suﬃciently large. By Proposition 2.3, we may choose H, equivalently N, from
a sequence of numbers tending to inﬁnity, and Theorem 1.1 follows.

5

4. Proof of Proposition 2.2

The estimates (2.9) and (2.10) of Proposition 2.2 are essentially the same as estimates already
in the literature, so we will only outline a proof of each of them, referring to [3] and [5] for
details.

Let Q = Q(H) satisfy (2.2) and (2.3). For a set of distinct linear forms H, as in (2.6), and
positive integers d, we deﬁne

Ω(d) = Ω(d; H) := {n mod d : P (n; H) ≡ 0 mod d},

where P (n; H) is as in (2.8). A Chinese remainder theorem argument shows that n mod d ∈
Ω(d) if and only if pr || P (n; H) for every pr || d, and so |Ω(d)| deﬁnes a multiplicative
function of d. Thus, if we deﬁne

λR(d; j) :=
 



 1
j!µ(d)(log R/d)j if d ⩽ R,

0 if d > R, (4.1)

we see from (2.7) that

ΛR(n; H, j) := 1
j!
 ∑′

d|P (n;H)
d⩽R
 µ(d)(log R/d)j = ∑′

n mod d
∈Ω(d)
 λR(d; j). (4.2)

We call H admissible if |Ω(p)| < p for all p, and one can prove that this is equivalent to
S(H) ̸= 0, where
 S(H) := ∏

p
 (
1 − |Ω(p)|
p
 ) (1 − 1
p
 )−k

is the singular series for H.

Lemma 4.1. Let H be a real number, let Q = Q(H) be a positive integer satisfying (2.2)
and (2.3), and let H be as in (2.6), with k ﬁxed. We have

|Ω(p)| = k for all p > H. (4.3)

For k ⩽ log H, H is admissible if and only if (Q, h1 · · · hk) = 1. Moreover, as H → ∞, for
(Q, h1 · · · hk) = 1 we have
 S(H) ∼ ( Q
φ(Q)
)k . (4.4)

Proof. For primes p that do not divide Q, we have

Ω(p) = {−h1Q
−1, . . . , −hkQ
−1} mod p,

6

and hence 1 ⩽ |Ω(p)| ⩽ min(k, p). For such p, we have |Ω(p)| = k if and only if the −hiQ
−1

are all distinct modulo p, that is if and only if p ∤ ∆, where

∆ = ∆(H) := ∏

1⩽i<j⩽k |hi − hj| .

By (2.2), p > H implies p ∤ Q, and since 1 ⩽ |hi − hj| ⩽ H for every i, j, p > H also implies
p ∤ ∆, and hence |Ω(p)| = k. We have established (4.3).

If some prime p divides (Q, h1 · · · hk), then P (n; H) ≡ h1 · · · hk ≡ 0 mod p for every n mod p,
hence |Ω(p)| = p, and so H is not admissible if (Q, h1 · · · hk) ̸= 1. If (Q, h1 · · · hk) = 1,
then P (n; H) ≡ h1 · · · hk ̸≡ 0 mod p, and hence |Ω(p)| = 0, for every p dividing Q. For
every other p we have 1 ⩽ |Ω(p)| ⩽ min(k, p). Then for k ⩽ log H and p ∤ Q, we have
1 ⩽ |Ω(p)| ⩽ k ⩽ log H < p by (2.3), hence H is admissible.

Now assume H is large enough so that log H ⩾ 2k, and suppose (Q, h1 · · · hk) = 1. Then for
(4.4), since |Ω(p)| = 0 if p | Q, it suﬃces to show that

S′(H) := ∏

p∤Q
 (
1 − |Ω(p)|
p
 ) (
1 − 1
p
 )−k ∼ 1 (4.5)

as H tends to inﬁnity. We break S′(H) into two products according as p | ∆ or p ∤ ∆, and
use the fact that |Ω(p)| = k for p ∤ Q∆:

S′(H) = ∏

p∤Q
 (
1 − k
p
 ) (
1 + k − |Ω(p)|
p − k
 ) (
1 − 1
p
 )−k

= ∏

p∤Q
 (
1 − k
p
 ) (
1 − 1
p
 )−k ∏

p∤Q
p|∆
 (
1 + k − |Ω(p)|
p − k
 ) . (4.6)

In this product p − k ̸= 0 because, by (2.3), p ∤ Q implies p > log H ⩾ 2k. For the same
reason, the logarithm of the ﬁrst product of the last line of (4.6) is
∑

p∤Q
 {(
−k
p − k2

2p2 − · · · ) − k (
−1
p − 1
2p2 − · · · )} ≪ k2 ∑

p>log H
 1
p2 ≪ k2

log H log log H .

For the second product, note that since k/ log H ⩽ 1/2, we have

0 < k − |Ω(p)|
p − k ⩽ k
p − k ⩽ 2k
p < 1.

Hence the logarithm of the second product is

⩽ ∑

p|∆
p>log H
 log (
1 + k − |Ω(p)|
p − k
 ) ≪ ∑

p|∆
p>log H
 k
p ≪ k
log H
 ∑

p|∆ 1 ≪ k log ∆
log H log log ∆ ≪ k3

log log H

7

by the prime number theorem, because ∆ ⩽ H(k
2). Exponentiating and letting H tend to
inﬁnity yields (4.5). □

We now assume all of the hypotheses of Proposition 2.2. The proof of (2.9) is almost identical
to the proof of Lemma 1 of [3], the only diﬀerence being that primes p | Qp0 are excluded
from the representation of F (s1, s2; Ω), where

F (s1, s2; Ω) := ∑′

d1,d2 µ(d1)µ(d1) |Ω([d1, d2])|
[d1, d2]ds1
1 ds2
2

= ∏

p∤Qp0
 (1 − |Ω(p)|
p
 ( 1
ps1 + 1
ps2 − 1
ps1+s2
 ))

in the region of absolute convergence. Since |Ω(p)| = k for p > H by (4.3), we put

G(s1, s2; Ω) := F (s1, s2; Ω) (ζ(s1 + 1)ζ(s2 + 1)
ζ(s1 + s2 + 1)
 )k .

In the proof of Lemma 1 of [3], G(0, 0; Ω) = S(H), but in our situation, we have

G(0, 0; Ω) = ∏

p∤Qp0
 (1 − |Ω(p)|
p
 ) ∏

p
 (
1 − 1
p
 )−k = S(H) ∏

p|p0
 (
1 − |Ω(p)|
p
 )−1 ,

because (Q, p0) = 1 and |Ω(p)| = 0 if p | Q. The last product is ∼ 1 by (2.1). Now applying
(4.4), and proceeding as in the proof of Lemma 1 of [3], (2.9) is established.

The proof of (2.10) follows that of Lemma 2 of [3] very closely: there is one important
diﬀerence concerning the error

E∗(N, q) := max
x⩽N max
(a,q)=1
 ∣
∣
∣
∣
∣
 ∑

p⩽x
p≡a mod q
 log p − x
φ(q)
∣
∣
∣
∣
∣
.

The usual Bombieri-Vinogradov theorem will not suﬃce here, but the next lemma, which is
Lemma 2 of [5], will.

Lemma 4.2. Let Q be an integer and Y, M be numbers such that

Q
2 ⩽ Y ⩽ M, exp (2√
log M) ⩽ Y. (4.7)

If there is an exceptional modulus q0 ⩽ Y , suppose p0 ∤ Q for some p0 | q0; otherwise, let
p0 = 1. If
 R∗ := M 1/2Q
−3 exp (−
√log M ) , (4.8)

8

then we have, with explicitly calculable positive constants c1 and c2,
∑

D⩽R∗
(D,Qp0)=1
 E∗(M, QD) ⩽ c1 M
Q exp (
−c2 log M
log Y
 ) . (4.9)

By (2.2) – (2.5), we see that (4.7) is satisﬁed with

Y = exp (2cH/(log H)2) = N 2cǫ(1+o(1))/(log log N )2,

and M = 3QN. We also have

R2 = N 1/2−2ǫ′ ⩽ R∗ = (3QN)1/2Q
−3 exp (
−
√log 3QN) ,

for all suﬃciently large N, and

c2 log M/ log Y = c2(1 + o(1)) log N/ log Y = c2(1 + o(1))(log log N)2/2cǫ.

Letting c3 = c2/12cǫ and putting this into (4.9), we deduce from Lemma 4.2 that
∑′

D⩽R2 E∗(3QN, QD) ≪ N(log N)−5c3 log log N (4.10)

for all suﬃciently large N.

Now, abbreviating λR(d; k + ℓ) to λd, by (4.2) we have
∑

N <n⩽2N ϑ(Qn + h)ΛR(n; H, k + ℓ)2 = ∑′

d1,d2 λd1λd2 ∑

N <n⩽2N
[d1,d2]|P (n;H)
 ϑ(Qn + h)

= ∑′

d1,d2 λd1λd2 ∑

m mod [d1,d2]
∈Ω([d1,d2])
 ∑

QN +h<p⩽2QN +h
p≡h mod Q
p≡Qm+h mod [d1,d2]
 log p. (4.11)

We may assume (Qm + h, [d1, d2]) = (Q, [d1, d2]) = 1 in the last sum, so we deﬁne

Ω
∗(d) := Ω(d) \ {m mod d : (Qm + h, d) ̸= 1}.

For d1, d2 with (Q, [d1, d2]) = 1 and m mod [d1, d2] ∈ Ω
∗([d1, d2]), we let hm mod Q[d1, d2]
be the unique congruence class mod Q[d1, d2] satisfying hm ≡ h mod Q and hm ≡ Qm +
h mod [d1, d2]. Thus, the last sum in (4.11) is equal to
∑

QN +h<p⩽2QN +h
p≡hm mod Q[d1,d2]
 log p = 2QN + h
φ(Q[d1, d2]) − QN + h
φ(Q[d1, d2]) + O (E∗(3QN, Q[d1, d2])) ,

and (4.11) becomes
 QN
φ(Q) T ∗ + O(E ∗), (4.12)

9

with

T ∗ := ∑′

d1,d2
 λd1λd2 |Ω
∗([d1, d2])|
φ([d1, d2]) , E ∗ := ∑′

d1,d2 |λd1λd2| |Ω
∗([d1, d2])| E∗(3QN, Q[d1, d2]).

Now from the deﬁnition (4.1) it is clear that |λd| ⩽ (log R)k+ℓ. Also, as we saw in the
beginning of the proof of Lemma 4.1, since (Q, h1 · · · hk) = 1 we have |Ω(p)| ⩽ k for all p,
and so |Ω
∗(d)| ⩽ |Ω(d)| ⩽ kω(d) for squarefree d. Thus

E ∗ ⩽ (log R)2(k+ℓ) ∑′

D⩽R2 µ2(D)kω(D)E∗(3QN, QD) ∑

[d1,d2]=D 1

= (log R)2(k+ℓ) ∑′

D⩽R2 µ2(D)(3k)ω(D)E∗(3QN, QD).

By the trivial inequality
 E∗(3QN, QD) ≪ QN log QN
QD ≪ N log N
D ,

and the Cauchy-Schwarz inequality, we have
∑′

D⩽R2 µ2(D)(3k)ω(D)E∗(3QN, QD)

≪
 

N log N ∑

D⩽R2
 µ2(D)(3k)2ω(D)

D
 


1/2 

 ∑′

D⩽R2 E∗(3QN, QD)




1/2
 .

For positive integers κ, we have
∑

D⩽R2
 µ2(D)κ
ω(D)

D = ∑

d···dκ⩽R2
 µ2(d1) · · · µ2(dκ)
d1 · · · dκ ≪ (log R2)κ ≪ (log N)κ,

so combining and applying (4.10) yields

E ∗ ≪ N (log N)2(k+ℓ)+(3k)2/2+1/2

(log N)−2c3 log log N ⩽ N(log N)−c3 log log N . (4.13)

We will now evaluate T ∗, assuming ﬁrst that Qx + h ̸∈ H. Let H+ = H ∪ {Qx + h} and
observe that for p ∤ Q,
 |Ω
∗(p)| = |Ω(p; H+)| − 1 := |Ω
+(p)| − 1.

As with |Ω(d)|, a Chinese remainder theorem argument shows that |Ω
∗(d)| deﬁnes a multi-
plicative function of d. Thus

|Ω
∗([d1, d2])| = ∏

p|[d1,d2]
 (
|Ω
+(p)| − 1) ,

10

provided [d1, d2] is squarefree and (Q, [d1, d2]) = 1, as is the case for d1, d2 appearing in the
sum deﬁning T ∗.

We now proceed as in the proof of Lemma 2 of [3]: again, the only modiﬁcation necessary is
to G(0, 0; Ω
+). First note that

S(H+) = ∏

p
 (p − |Ω
+(p)|
p
 ) ( p
p − 1
 ) (
1 − 1
p
 )−k = ∏

p
 (
1 − |Ω
+(p)| − 1
p − 1
 ) (
1 − 1
p
)−k .

By (4.3), |Ω
+(p)| = |H+| = k + 1 for p > H, and if

G(s1, s2; Ω
+) := ∏

p∤Qp0
 (
1 − |Ω
+(p)| − 1
p − 1
 ( 1
ps1 + 1
ps1 − 1
ps1+s2
 )) · ( ζ(s1 + 1)ζ(s2 + 1)
ζ(s1 + s2 + 1)
 )k ,

then
 G(0, 0; Ω
+) = ∏

p∤Qp0
 (
1 − |Ω
+(p)| − 1
p − 1
 ) ∏

p
 (
1 − 1
p
 )−k

= S(H+) ∏

p|Q
 (
1 + 1
p − 1
 )−1 ∏

p|p0
 (
1 − |Ω
+(p)| − 1
p − 1
 )−1

∼ ( Q
φ(Q)
 )k ,

by Lemma 4.1 and (2.1). Therefore

T ∗ ∼ ( Q
φ(Q)
)k (
2ℓ
ℓ
 )(log R)k+2ℓ

(k + 2ℓ)! . (4.14)

We remark that since (Q, h) = (Q, h1 · · · hk) = 1, H+ is admissible (for all suﬃciently large
N) by Lemma 4.1, so we do not have to consider the other case as in the proof of Lemma 2
in [3]. Combining (4.14) with (4.13) and (4.12) yields the ﬁrst case of (2.10). For the case
Qx + h ∈ H, we observe that, similarly to (2.2) of [3], we have
∑

N <n⩽2N ϑ(Qn + h)ΛR(n; H, k + ℓ)2 = ∑

N <n⩽2N ϑ(Qn + h)ΛR(n; H \ {Qx + h}, k + ℓ)2,

so the above evaluation applies with the translation k ↦→ k − 1, ℓ ↦→ ℓ + 1 to (4.14).

5. Proof of Proposition 2.3

5.1. Auxiliary lemmas. To prove Proposition 2.3, we will use the following lemmas.

11

Lemma 5.1. Fix integers q and a with (q, a) = 1. There is a constant c(q, a) > 0, depending
only on q and a, such that ∏

p⩽x
p≡a mod q
 (1 − 1
p
 ) ∼ c(q, a)
(log x)1/φ(q)

as x → ∞.

Proof. This follows from the prime number theorem for arithmetic progressions. For a more
precise estimate, with the constant c(q, a) given explicitly, see [10, Theorem 1]. □

Lemma 5.2. Let S (x) denote the set of positive integers which are ⩽ x and composed only
of primes p ≡ 1 mod q. There is a constant c(q) > 0, depending only on q, such that

|S (x)| = (c(q) + O ( 1
log x
 )) x
log x (log x)1/φ(q).

Proof. See [9, Lemma 3], in which the constant c(q) is given explicitly. □

The next lemma concerns Ψ(x, y), the number of positive integers which are ⩽ x and free
of prime factors > y (y-smooth numbers). The ratio Ψ(x, y)/x depends essentially on u =
log x/ log y, and for u in a certain range is approximated by ρ(u), where ρ(u) is the Dickman-
de Bruijn ρ-function, deﬁned as the continuous solution to

ρ(u) :=
 


1 0 ⩽ u ⩽ 1,

1
u ∫ u
u−1 ρ(t) dt u > 1. (5.1)

Lemma 5.3. The estimate
Ψ(yu, y)
yu = ρ(u) (
1 + O (log(u + 2)
log y
 )) (5.2)

holds uniformly in the range

y ⩾ 3, 1 ⩽ u ⩽ exp ((log y)3/5−δ) , (5.3)

where δ is any ﬁxed positive number. The estimate

ρ(u) = exp (−u log u − u log log u + O(u)) (5.4)

holds for u > 3, and
 Ψ(yu, y)
yu = exp (−u log u − u log log u + O(u)) (5.5)

12

holds uniformly in the range
 3 < u ⩽ y1−δ. (5.6)

Finally, as y → ∞,
 Ψ(y, (log y)A)
y = 1
y1/A+o(1) (5.7)

holds for any ﬁxed number A > 1.

Proof. We refer to the survey article of Granville [7]. The asymptotic (5.2) was shown to hold
for the range (5.3) by Hildebrand [8]: see [7, (1.8), (1.10)]. Hildebrand [8] also established
that the less precise estimate

Ψ(yu, y)
yu = ρ(u) exp (Oδ (u exp (
−(log u)3/5−δ)))

holds, for any ﬁxed number δ > 0, in the wider range (5.6). (See displayed formulas [7, (1.11),
(1.13)].) That (5.5) holds in the same range can be deduced from (5.4). (The estimate (5.5)
is less precise, but suﬃcient for our purposes.) For the estimate (5.7), see [7, (1.14)].

The value of the Dickman-de Bruijn ρ-function is discussed in [7, 3.7 – 3.9], and (5.4) was
proved by de Bruijn in [1]. □

Lemma 5.4. Let P be a subset of the primes. As y → ∞, the estimate
∏

p⩽y
p∈P
 (
1 − 1
p
 ) ∑

n>yu
p|n⇒p⩽y
p∈P
 1
n ⩽ (1 + o(1))e
−γ ∫ ∞

u ρ(v) dv. (5.8)

holds uniformly for u satisfying

u ⩾ 1, u = exp (
(log y)3/5−δ) , (5.9)

where δ is any ﬁxed positive number.

Proof. Deﬁne
 ̺(x, y; P) := ∏

p⩽y
p∈P
 (
1 − 1
p
 ) ∑

n⩽x
p|n⇒p⩽y
p∈P
 1
n.

If ℓ ⩽ y is prime, then

̺(x, y; P) = ∏

p⩽y
p∈P∪{ℓ}
 (1 − 1
p
 ) · (1 − 1
ℓ
 )−1 ∑

n⩽x
p|n⇒p⩽y
p∈P
 1
n.

13

Now (
1 − 1
ℓ
 )−1 ∑

n⩽x
p|n⇒p⩽y
p∈P
 1
n = (
1 + 1
ℓ + 1
ℓ2 + · · · ) ∑

n⩽x
p|n⇒p⩽y
p∈P
 1
n ⩾ ∑

m⩽x
p|m⇒p⩽y
p∈P∪{ℓ}
 1
m,

because every m appearing in the last sum may be written as nℓα for some α ⩾ 0 and some
n appearing in the second last sum. Hence,

̺(x, y; P) ⩾ ̺(x, y; P ∪ {ℓ}),

and applying this inequality repeatedly, we obtain

̺(x, y; P) ⩾ ∏

p⩽y
 (
1 − 1
p
 ) ∑

n⩽x
p|n⇒p⩽y
 1
n .

Subtracting both sides from ̺(∞, y; P) = 1 = ̺(∞, y; {p ⩽ y}), we deduce that
∏

p⩽y
p∈P
 (
1 − 1
p
 ) ∑

n>x
p|n⇒p⩽y
p∈P
 1
n ⩽ ∏

p⩽y
 (
1 − 1
p
) ∑

n>x
p|n⇒p⩽y
 1
n. (5.10)

By partial summation,
∑

n>x
p|n⇒p⩽y
 1
n = ∫ ∞

x
 dΨ(t, y)
t = −Ψ(x, y)
x + ∫ ∞

x
 Ψ(t, y)
t2 dt ⩽ ∫ ∞

x
 Ψ(t, y)
t2 dt. (5.11)

Now we assume x = yu, with u satisfying (5.9) and y tending to inﬁnity. We will divide the
range of the last integral in (5.11) into three parts. First of all, ﬁx any ǫ ∈ (0, 1) and suppose
t ⩾ exp(yǫ), that is y ⩽ (log t)1/ǫ. By (5.7) we have

Ψ(t, y)
t2 ⩽ Ψ(t, (log t)1/ǫ)
t2 = 1
t1+ǫ+o(1)

as t, and hence as y, tends to inﬁnity. Thus, we may suppose y is large enough so that
Ψ(t, y)/t
2 ⩽ 1/t
1+ǫ/2, say, and
∫ ∞

exp(yǫ)
 Ψ(t, y)
t2 dt ⩽ ∫ ∞

exp(yǫ)
 dt
t1+ǫ/2 = 2
ǫ exp (ǫyǫ/2). (5.12)

For the range x ⩽ t ⩽ exp(yǫ), the substitution t = yv yields
∫ exp(yǫ)

x
 Ψ(t, y)
t2 dt = log y ∫ yǫ/ log y

u
 Ψ(yv, y)
yv dv. (5.13)

14

Next, we let u1 = 2 exp ((log y)3/5−δ), and for u1 ⩽ v ⩽ yǫ, we use the estimate (5.5):

Ψ(yv, y)
yv = exp (−v log v − v log log v + O(v)) ⩽ 1
vv ,

where the last inequality holds for all suﬃciently large v, hence for all suﬃciently large y.
Thus ∫ yǫ/ log y

u1
 Ψ(yv, y)
yv dv ⩽ ∫ ∞

u1
 dv
vv ≪ 1
uu1
1 (5.14)

for all suﬃciently large y.

For u ⩽ v ⩽ u1, we use the estimate (5.2):
∫ u1

u
 Ψ(yv, y)
yv dv = ∫ u1

u ρ(v) (
1 + O (log(v + 2)
log y
 )) dv

= (1 + o(1)) ∫ ∞

u ρ(v) dv − (1 + o(1)) ∫ ∞

u1 ρ(v) dv. (5.15)

By (5.4) we have, similarly to (5.14), the estimate
∫ ∞

u1 ρ(v) dv ⩽ ∫ ∞

u1
 dv
vv ≪ 1
uu1
1 (5.16)

for all suﬃciently large y.

Combining (5.11) – (5.16), we see that
∫ ∞

x
 Ψ(t, y)
t2 dt = (1 + o(1)) log y ∫ ∞

u ρ(v) dv + O (u−u1
1 log y) (5.17)

for all suﬃciently large y. Now by deﬁnition (5.1),
∫ ∞

u ρ(v) dv ⩾ ∫ u+1

u ρ(v) dv = (u + 1)ρ(u + 1),

and by (5.4), u−u1
1 = o((u+1)ρ(u+1)) as u1 ⩾ 2u, and u1 tends to inﬁnity with y. Therefore,
combining (5.17) with (5.11) in fact gives
∑

n>yu
p|n⇒p⩽y
 1
n ⩽ (1 + o(1)) log y ∫ ∞

u ρ(v) dv (5.18)

as y → ∞, for u in the range (5.9). Finally, combining (5.18) with (5.10) and applying
Mertens’ theorem, we obtain (5.8). □

5.2. The proof of Proposition 2.3. We are now ready to deﬁne Q explicitly. The con-
struction is modelled on that of Shiu’s [9]. For the rest of this section we let q ⩾ 3 and a be
15

integers with (q, a) = 1. If a ≡ 1 mod q, let

P(H) := {p ⩽ log H : p ≡ 1 mod q} ∪ {p ⩽ H/(log H)2 : p ̸≡ 1 mod q},

otherwise let

P(H) := {p ⩽ log H : p ≡ 1 mod q} ∪ {p ⩽ H/(log H)2 : p ̸≡ 1, a mod q}

∪ {t(H) ⩽ p ⩽ H/(log H)2 : p ≡ 1 mod q} ∪ {p ⩽ H/t(H) : p ≡ a mod q},

with
 t(H) := exp (log H log log log H
2 log log H
 ) ,

and put
 ˜Q(H) := q ∏

p∈P(H) p, Q = Q(H) := q ∏

p∈P(H)
p̸=p0
 p. (5.19)

We check that (2.2) – (2.5) are indeed satisﬁed by Q: only (2.4) is not immediate, but it
follows from the prime number theorem.

Analogously to (2.12), we deﬁne

˜S(H) := {h ∈ (0, H] : ( ˜Q(H), h) = 1 and h ≡ a mod q},

˜T (H) := {h ∈ (0, H] : ( ˜Q(H), h) = 1 and h ̸≡ a mod q}. (5.20)

Proposition 2.3 will follow from the next lemma.

Lemma 5.5. Let H be a real parameter tending to inﬁnity, and let ˜Q(H) be as in (5.19).
We have
 | ˜T (H)| ≪ H
log H . (5.21)

Moreover, there is a constant A = A(q), depending on q at most, such that for all suﬃciently
large X, there is some H satisfying
 X
(log X)A ⩽ H ⩽ X, (5.22)

such that
 | ˜S(H)| ≫q H φ( ˜Q(H))
˜Q(H) . (5.23)

The implied constant in (5.21) is absolute, and that in (5.23) depends on q at most.

16

Proof of Proposition 2.3. Let S(H) and T (H) be as in (2.12). If p0 ̸= 1 then by (2.1) there
are at most H/p0 < H/ log H multiples of p0 in T (H), so

|T (H)| ≪ H
log H

by (5.21). We also have |S(H)| ⩾ | ˜S(H)|. An application of Lemma 5.1 reveals that

φ( ˜Q(H))
˜Q(H) = ∏

p∈P(H)
 (1 − 1
p
 ) ≫q
 



 1
log H ( log H
log log H )1/φ(q) if a ≡ 1 mod q,

1
log H ( log t(H)
log log H )1/φ(q) if a ̸≡ 1 mod q.

Therefore, in either case, combining (5.21) and (5.23) gives

|S(H)| − |T (H)| ≫ | ˜S(H)| − | ˜T (H)| ≫q H φ( ˜Q(H))
˜Q(H) ≫ H φ(Q(H))
Q(H) .

Proposition 2.3 now follows from Lemma 5.5. □

Proof of Lemma 5.5. We assume a ̸≡ 1 mod q as the case a ≡ 1 mod q is similar and simpler.

There are ≪ H/ log H primes in ˜T (H), so let us count the composites h ∈ ˜T (H). If
h = pm for some prime p > H/(log H)2, with m > 1, then m < (log H)2 is com-
posed only of primes > log H and ≡ 1 mod q, by the construction of P(H). Thus, m
must be prime itself, and p ⩽ H/ log H. We partition (H/(log H)2, H/ log H] into sub-
intervals Il = (e
l−1H/(log H)2, e
lH/(log H)2], and (log H, (log H)2] into sub-intervals Jl =
(log H, (log H)2/e
l], 1 ⩽ l ⩽ log log H, and using the prime number theorem, we deduce that
the contribution from elements with a large prime factor is at most
∑

1⩽l⩽log log H
 ∑

p∈Il
p̸≡1 mod q
 ∑

p′∈Jl
p≡1 mod q
 1 ≪ ∑

1⩽l⩽log log H
 e
lH
(log H)3 (log H)2

el log log H ≪ H
log H .

If h = pm with p ≡ a mod q, then p > H/t(H), and m < t(H) must be composed only of
primes ≡ 1 mod q, a contradiction as h ̸≡ a mod q. The only elements left uncounted must
be composed only of primes p ≡ 1 mod q with log H < p < t(H). By (5.5), the number of
such elements is at most

Ψ(H, t(H)) = H exp (−u log u − u log log u + O(u)) ,

where u = log H
log t(H) = 2 log log H
log log log H .

Thus u log u + u log log u + O(u) ∼ u log u ∼ 2 log log H,
17

and so Ψ(H, t(H)) ≪ H
log H .

Combining these estimates yields (5.21).

Now suppose H is in the range (5.22). To bound the size of ˜S(H) from below we will ﬁrst
do the same for
 S′(X) := {h ∈ (0, X] : (Q
′(X), h) = 1 and h ≡ a mod q},

where Q
′(X) := q ∏

p∈P′(X) p, P ′(X) := P(X) \ {p ⩽ log X : p ≡ 1 mod q}.

Now pm ∈ S′(X) if X/t(X) < p ≡ a mod q and m ∈ S (X/p). We partition (X/t(X), X]
into sub-intervals Il = (e
l−1X/t(X), e
lX/t(X)], 1 ⩽ l ⩽ log t(X), and deduce, using the
prime number theorem for arithmetic progressions and Lemma 5.2, that

|S′(X)| ⩾ ∑

1⩽l⩽log t(X)
 ∑

p∈Il
p≡a mod q
 ∑

m∈S (t(X)/el ) 1

≫q ∑

1⩽l⩽ 1
2 log t(X)
 e
lX
t(X) log X · t(X)
el log t(X) (log t(X))1/φ(q)

≫ X
log X (log t(X))1/φ(q).
 (5.24)

Now, we may write any h ∈ S′(X) uniquely as h = dm, where d is composed only of primes
p ⩽ log X with p ≡ 1 mod q, and m ∈ ˜S(X). Thus, by (5.24), there is a constant c1(q) > 0,
depending on q at most, such that for all suﬃciently large X,

c1(q) X
log X (log t(X))1/φ(q) ⩽ |S′(X)| = ∑

d⩽X
p|d⇒p⩽log X
p≡1 mod q
 ∑

m⩽X/d
m∈ ˜S(X)
 1 ⩽ ∑

d⩽X
p|d⇒p⩽log X
p≡1 mod q
 | ˜S(X/d)|. (5.25)

The inequality on the right is not immediate: in fact if Z ⩽ X, then ˜S(X) ∩ (0, Z] ⊆ ˜S(Z).
To see this, ﬁrst note that as all of the functions used to deﬁne P(X) are monotonically
increasing with X,
 P(Z) ⊆ P(X) ∪ {t(Z) ⩽ p ⩽ t(X) : p ≡ 1 mod q}.

Suppose m ∈ ˜S(X) ∩ (0, Z], but m ̸∈ ˜S(Z). Then p ∈ P(Z) for some p | m, but p ̸∈ P(X),
so t(Z) ⩽ p ⩽ t(X) and p ≡ 1 mod q. Since m ≡ a ̸≡ 1 mod q, there must be some p′ | m
with p′ ̸≡ 1 mod q and p′ ⩽ m/p ⩽ Z/t(Z) ⩽ X/t(X). Then p′ ∈ P(X), a contradiction.

18

Suppose for a contradiction that for some constant c2(q) > 0, depending on q at most, we
have
 | ˜S(H)| ⩽ c1(q)
3c2(q) H
log X
 ( log t(X)
log log X
 )1/φ(q) (5.26)

for all H in the range (5.22). Then

∑

d⩽(log X)A
p|d⇒p⩽log X
p≡1 mod q
 | ˜S(X/d)| ⩽ c1(q)
3c2(q) X
log X
 ( log t(X)
log log X
 )1/φ(q) ∑

d⩽(log X)A
p|d⇒p⩽log X
p≡1 mod q
 1
d

⩽ c1(q)
3c2(q) X
log X
 ( log t(X)
log log X
 )1/φ(q) ∏

p⩽log X
p≡1 mod q
 (
1 − 1
p
 )−1

⩽ c1(q)
3 X
log X (log t(X))
1/φ(q) ,
 (5.27)

provided X is suﬃciently large, and for a suitable choice of c2(q) (given by Lemma 5.1).

Now, by the fundamental lemma of Brun’s sieve, we have

| ˜S(X/d)| ≪ X
d
 ∏

p∈P(X/d)
 (1 − 1
p
 ) (5.28)

for any d. If (log X)A < d ⩽ √X, then log(X/d) ≍ log X, and applying Lemma 5.1 to the
sieve upper bound (5.28), we see that

∑

(log X)A<d⩽√X
p|d⇒p⩽log X
p≡1 mod q
 | ˜S(X/d)| ⩽ c3(q) X
log X
 ( log t(X)
log log X
 )1/φ(q) ∑

(log X)A<d⩽√
X
p|d⇒p⩽log X
p≡1 mod q
 1
d (5.29)

for some constant c3(q) > 0. By lemmas 5.4 and 5.1 respectively, we have

∑

(log X)A<d⩽√
X
p|d⇒p⩽log X
p≡1 mod q
 1
d ⩽ ∏

p⩽log X
p≡1 mod q
 (1 − 1
p
 )−1 (1 + o(1))e
−γ ∫ ∞

A ρ(v) dv

⩽ c4(q)(log log X)1/φ(q) ∫ ∞

A ρ(v) dv
 (5.30)

for some constant c4(q) > 0. Now by (5.4),
∫ ∞

A ρ(v) dv → 0 as A → ∞,

19

so we may choose A = A(c1(q), c3(q), c4(q)) = A(q) so that
∫ ∞

A ρ(v) dv ⩽ c1(q)
4c3(q)c4(q).

For any such A, combining (5.29) and (5.30) yields
∑

(log X)A<d⩽√
X
p|d⇒p⩽log X
p≡1 mod q
 | ˜S(X/d)| ⩽ c1(q)
4 X
log X (log t(X))1/φ(q). (5.31)

Finally, using Rankin’s trick, we see that

∑

√X<d⩽X
p|d⇒p⩽log X
p≡1 mod q
 | ˜S(X/d)| ⩽ ∑

√X<d⩽X
p|d⇒p⩽log X
 X
d
 ( d
√X
 )1/3 ⩽ X 5/6 ∏

p⩽log X
 (
1 − 1
p2/3
 )−1

⩽ X 5/6 exp
 ( ∑

p⩽log X
 3
p2/3
 )
 ⩽ X 5/6 exp (
9(log X)1/3)

= X 5/6+o(1)
 (5.32)

by the prime number theorem.

Combining (5.25), (5.27), (5.31), and (5.32), we obtain c1(q) ⩽ 2c1(q)/3, which is absurd.
We conclude that for all suﬃciently large X, there is some H in the range (5.22) for which

| ˜S(H)| ≫q H
log X
 ( log t(X)
log log X
 )1/φ(q) ≫ H
log H
 ( log t(H)
log log H
 )1/φ(q) .

A ﬁnal application of Lemma 5.1 shows that this is ≫q Hφ( ˜Q(H))/ ˜Q(H). □

6. A lower bound

In this section we will show how to obtain a quantitative version of Theorem 1.1. We will
use the assumptions and notation of sections 3 – 5, and show that

|{pr+1 ⩽ Y : pr+1 ≡ pr ≡ a mod q and pr+1 − pr < ǫ log pr}| ⩾ Y 1/3(log log Y )A (6.1)

for all suﬃciently large Y . Here A = A(q) is the constant given in Lemma 5.5. This lower
bound could be improved by a sharpening of the range (5.22) for H.

We will ﬁrst prove that the estimate
∑

N <n⩽2N Λ(n; H, k + ℓ)4 ≪ N(log N)19k+4ℓ (6.2)

20

holds, with an absolute implied constant. For by (4.1) and (4.2),
∑

N <n⩽2N Λ(n; H, k + ℓ)4 = ∑′

d1,...,d4 λd1 · · · λd4 ∑

N <n⩽2N
[d1,...,d4]|P (n;H)
 1

= ∑′

d1,...,d4 λd1 · · · λd4 ∑

m mod [d1,...,d4]
∈Ω([d1,...,d4])
 ∑

N <n⩽2N
n≡m mod [d1,...,d4]
 1

⩽ ∑

d1,...,d4
squarefree
 |λd1 · · · λd4| ∑

m mod [d1,...,d4]
∈Ω([d1,...,d4])
 ( N
[d1, . . . , d4] + O(1))

≪ N(log R)4(k+ℓ) ∑

d1,...,d4⩽R
squarefree
 |Ω([d1, . . . , d4])|
[d1, . . . , d4] .
 (6.3)

To see the last inequality, note that [d1, ..., d4] ⩽ R4 = N 1−4ǫ′ = o(N), and so N/[d1, ..., d4] +
O(1) ≪ N/[d1, ..., d4].

As observed in Section 4, |Ω(d)| ⩽ kω(d) for squarefree d, so

∑

d1,...,d4⩽R
squarefree
 |Ω([d1, . . . , d4])|
[d1, . . . , d4] ⩽ ∑

D⩽R4
 µ2(D)kω(D)

D
 ∑

d1,...,d4
[d1,...,d4]=D
 1

= ∑

D⩽R4
 µ2(D)(15k)ω(D)

D ⩽ ∏

p⩽R4
 (
1 + 15k
p
 )

≪ (log R4)15k.
 (6.4)

Since R4 < N, combining (6.3) and (6.4) yields (6.2).

Now choose N so that (3.2) holds. If we restrict the outer sum in the deﬁnition of L to
those n for which (Qn, Qn + H] contains a prime string pr+1 ≡ pr ≡ a mod q, we remove no
positive terms. Thus, if ∑∗ denotes this restricted sum, then

L ⩽

1
N
 (φ(Q)
Q
 )k ∑∗

N <n⩽2N
 (∑

h∈S ϑ(Qn + h) − ∑

h∈T ϑ(Qn + h) − log 3QN
)
 ΛR(n; H, k + ℓ)2. (6.5)

For each n ∈ (N, 2N],
∑

h∈S ϑ(Qn + h) − ∑

h∈T ϑ(Qn + h) − log 3QN ⩽ H log 3QN, (6.6)

21

and by the Cauchy-Schwartz inequality,

∑∗

N <n⩽2N ΛR(n; H, k + ℓ)2 ⩽
 ( ∑∗

N <n⩽2N 1
)1/2 ( ∑

N <n⩽2N ΛR(n; H, k + ℓ)4)1/2 . (6.7)

Combining (6.5) – (6.7) yields

∑∗

N <n⩽2N 1 ⩾ N 2(Q/φ(Q))2kL 2(H log 3QN)−2 ( ∑

N <n⩽2N ΛR(n; H, k + ℓ)4)−1 .

Using H = ǫ log N, log 3QN = (1 + o(1)) log N, and Q/φ(Q) ⩾ 1, then applying (3.2) and
(6.2), we see that the right-hand side is ≫k,q N/(log N)17k+2. Since k depends on ǫ, we may
write ∑∗

N <n⩽2N 1 ≫ǫ,q N
(log N)B(ǫ) , (6.8)

where B(ǫ) is a constant depending on ǫ.

Now ﬁx a large number Y , and let

X := ǫ (
1 + 2cǫ
(log log Y )2
 )−1 log Y,

with c > 0 ﬁxed. By Lemma 5.5, we may choose H in the range

X/(log X)A ⩽ H ⩽ X

so that (3.2), hence (6.1), holds with N = exp(H/ǫ). By (2.4),

3Q(H)N ⩽ exp (H
ǫ + cH
(log H)2
 ) ⩽ Y,

because H
ǫ + cH
(log H)2 = H
ǫ
 (
1 + cǫ
(log H)2
 ) ⩽ X
ǫ
 (
1 + 2cǫ
(log log Y )2
 ) = log Y.

Here we have used log H = (1 + o(1)) log X = (1 + o(1)) log log Y . Also,

log N = H/ǫ ⩾ X/ǫ(log X)A ⩾ log Y /2(log log Y )A.

Therefore, using (6.8) as a lower bound for the number of prime strings up to Y , we deduce
(6.1). (At best, we may have H = X, in which case we could deduce a lower bound of
Y 1−c′/(log log Y )2, for some constant c′ > 0.)
 22

7. Concluding remarks

Proposition 2.2 is similar to a special case of Propositions 1 and 2 of [5], which are used to
prove that
 lim inf
r→∞ p′
r+ν − p′
r
φ(q) log p′
r ⩽ e
−γ(√ν − 1)2,

where p′
j denotes the jth smallest prime in the arithmetic progression a mod q, (q, a) = 1.
By considering Hν = (ν − 1 + ǫ) log N instead of H, Q = Q(Hν) instead of Q(H), and

Lν :=

1
N
 (φ(Q)
Q
 )k ∑

N <n⩽2N
 (∑

h∈S ϑ(Qn + h) − ν ∑

h∈T ϑ(Qn + h) − ν log 3QN
)
 ΛR(n; H, k + ℓ)2

instead of L , it is possible to prove that the interval (Qn, Qn + Hν] contains a string of
ν + 1 consecutive primes ≡ a mod q, for some n ∈ (N, 2N] and a sequence N → ∞. It may
be feasible to prove a similar result with Hν = (e
−γ(√ν − 1)2 + ǫ) log N.

8. Acknowledgements

I would like to thank Andrew Granville, without whose help and encouragement this work
would not have materialized. For many productive discussions, my thanks also to Jorge
Jim´enez Urroz, and my colleagues Farzad Aryan, Mohammad Bardestani, Daniel Fiorilli
and Kevin Henriot.
 References

[1] N. G. de Bruijn, ‘The asymptotic behaviour of a function occurring in the theory of primes’, J. Indian
Math. Soc. (N.S.) 15 (1951), 25–32. MR0043838 (13:326f)
[2] H. Davenport, Multiplicative number theory, 3rd edn (Revised and with a preface by H. L. Montgomery;
Springer-Verlag, New York, 2000). MR1790423 (2001f:11001)
[3] D. A. Goldston, Y. Motohashi, J. Pintz, and C. Y. Yıldırım, ‘Small gaps between primes exist’, Proc.
Japan Acad. Ser. A Math. Sci. 82 (2006), 61–65. MR2222213 (2007a:11135)
[4] D. A. Goldston, J. Pintz, and C. Y. Yıldırım, ‘Primes in tuples I’, Preprint, 2005, http://arxiv.org/
abs/math/0508185v1.
[5] D. A. Goldston, J. Pintz, and C. Y. Yıldırım, ‘Primes in tuples III. On the diﬀerence pn+ν − pn’, Funct.
Approx. Comment. Math. 35 (2006), 79–89. MR2271608 (2008f:11102)
[6] D. A. Goldston, J. Pintz, and C. Y. Yıldırım, ‘Primes in tuples I’, Ann. of Math. (2) 170 (2009), 819–862.
MR2552109
[7] A. Granville, ‘Smooth numbers: computational number theory and beyond’, Algorithmic number theory:
lattices, number ﬁelds, curves and cryptography (eds J. P. Buhler and P. Stevenhagen), Mathematical
23

Sciences Research Institute Publications 44 (Cambridge University Press, Cambridge, 2008), 267–323.
MR2467549
[8] A. Hildebrand, ‘On the number of positive integers ⩽ x and free of prime factors > y’, J. Number The-
ory 22 (1986), 289–307. MR831874 (87d:11066)
[9] D. K. L. Shiu, ‘Strings of congruent primes’, J. London Math. Soc. (2) 61 (2000), 359–373. MR1760689
(2001f:11155)
[10] K. S. Williams, ‘Mertens’ theorem for arithmetic progressions’, J. Number Theory 6 (1974), 353–359.
MR0364137 (51:392)

D´epartement de math´ematiques et de statistique
Universit´e de Montr´eal
CP 6128, succ. Centre-ville
Montr´eal, Qu´ebec H3C 3J7
Canada

E-mail address: freiberg@dms.umontreal.ca
 24
