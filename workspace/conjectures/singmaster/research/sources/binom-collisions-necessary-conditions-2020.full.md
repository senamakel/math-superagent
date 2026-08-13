<!-- source: https://arxiv.org/pdf/2002.07043 | converted from PDF -->

arXiv:2002.07043v1  [math.NT]  17 Feb 2020
NECESSARY CONDITIONS FOR BINOMIAL COLLISIONS

TOMOHIRO YAMADA*

Abstract. We shall give some necessary conditions for the equation (
x
a) =
(
y
b) to hold: if (
2n+δ
n−m) = (
2n+l
n−k ) with δ = 0 or 1, 0 < m ≤ 0.735k, k < n and n
suﬃciently large, then l > (cn/ log n)40/21 for some constant c.

1. Introduction

Several authors have studied integers appearing in Pascal’s triangle more than
once in a nontrivial way. Clearly, we have (x
0) = 1 for every nonnegative integer
x, (x
k) = ( x
x−k) and, writing N = (x
k), (N
1 ) = ( N
N −1
) = (x
k). So that, we should
consider the equation

(1) N = (x
a
) = (y
b
)

in nonnegative integers a, b, x, y with 2 ≤ a ≤ x/2 and 2 ≤ b ≤ y/2. Moreover,
we may assume that x > y, which implies a < b since (x
c) ≥ (x
a) > (y
a) for
a ≤ c ≤ x/2. For example,

(2)
 (16
2
 ) = (10
3
 ) = 120, (21
2
 ) = (10
4
 ) = 210,
(56
2
 ) = (22
3
 ) = 1540, (120
2
 ) = (36
3
 ) = 7140,
(153
2
 ) = (19
5
 ) = 11628, (221
2
 ) = (17
8
 ) = 24310,
(78
2
 ) = (15
5
 ) = (14
6
 ) = 3003.

An inﬁnite family has been found by Lind [11] and rediscovered by Singmaster
[19] and Tovey [22]. Let Fi be the n-th Fibonacci number, deﬁned by F0 =
0, F1 = 1 and Fi+2 = Fi+1 + Fi for i = 0, 1, 2, . . .. Then, for every i = 0, 1, 2, . . .,

(3) (F2i+2F2i+3
F2iF2i+3
 ) = (F2i+2F2i+3 − 1
F2iF2i+3 + 1
 ).

We note that this family includes (15
5 ) = (14
6 ) but (78
2 ) does not appear in this
family.

2010 Mathematics Subject Classiﬁcation. Primary 11B65; Secondary 11A05, 11D61, 11D72.
Key words and phrases. Binomial coeﬃcient, exponential diophantine equation.
1

2 TOMOHIRO YAMADA

Let (a, b, x, y, N ) be any further solution of (1). de Weger [23] proved that any
further solution of (1) must satisfy a ≥ 5, y > 1000 and N > 1030 and conjectured
that (1) has no further solution. Blokhuis, Brouwer and de Weger [4] pushed de
Weger’s lower bounds up to y > 106 an N > 1060.

Several pairs have been shown to never appear as (a, b). Avanesov [1] showed
that (a, b) ̸= (2, 3) and Pint´er showed that (a, b) ̸= (2, 4). Mordell’s result [13]
on the equation Y (Y + 1) = X(X + 1)(X + 2) implies that (a, b) ̸= (3, 4), as
de Weger [23] pointed out. Extending these results, Stroeker and de Weger
[20] showed that (a, b) ̸= (2, 3), (2, 4), (2, 6), (2, 8), (3, 4), (3, 6), (4, 6), (4, 8). These
results can be obtained by determining all integer points on elliptic curves derived
from (1) for these values of a, b. For other values of a, b, (1) will be diﬃcult to
solve since it yields curves genus > 1. Using recently developed techniques on
hyperelliptic curves, Bugeaud, Mignotte, Siksek, Stoll and Tengely [5] showed
that (a, b) ̸= (2, 5).

An approach from the opposite direction will be the study of (1) in the case
b is near to y/2. Let y = 2n + δ with δ = 0 or 1 and x = 2n + l with l > δ.
Moreover, let m = n − b and k = n − a, so that 0 ≤ m < k < n/2. Now (1)
becomes

(4) (2n + δ
n − m
) = (2n + l
n − k
 ).

Now, we shall state our result.

Theorem 1.1. If n, m, l, k are integers satisfying (4) with 0 ≤ m < k < n/2 and
m ≤ 0.735k, then l > n(1.3132 log2(2n) − 2.00271). Furthermore, if c < 0.68943,
then l > (cn/ log n)40/21 for suﬃciently large n.

Our argument would be generalized to show that, for any constants η < 1
and c < 0.68943, (4) has only ﬁnitely many solutions with m ≤ ηk and l <
(cn/ log n)40/21. Moreover, Cramer’s conjecture that the next prime after p is
smaller than p + c1 log2 p would allow us to replace (cn/ log n)40/21 by exp(c2√n),
where c2 depends on c1.

We would like to given an outline of our proof of the Theorem. We put k0 =
2(k + l) − δ − 1. Under the condition given in the Theorem, we shall prove that,
after preliminaries, i) if n + k + l > k3/2
0 , then l ≥ 0.001n, ii) if n + k + l ≤ k3/2
0 ,
then l ≥ 0.001n (hence, l ≥ 0.001n in any case) and iii) if l ≥ 0.001n, then the
conclusions of theorem holds.

(4) can be restated as

(5)
 k∏

i1=m+1
(n − i1)
 l∏

i3=δ+1(2n + i3) =
 k+l∏

i2=m+δ+1(n + i2)

NECESSARY CONDITIONS FOR BINOMIAL COLLISIONS 3

or, equivalently,

(6)
 l−δ∏

i=1
 ( 2n + δ + i
n + k + δ + i
 ) =
 k−m∏

j=1
 ( n + δ + m + j
n − k − 1 + j
 ) .

From (5), we see that n − i1 and n + i2 in these products must be composed of
small prime factors. Writing P (ν) for the largest prime factor of an integer ν > 1,
we can easily give an upper bound for P (
∏k
i1=m+1(n − i1) ∏k+l
i2=m+δ+1(n + i2)),
as we do in Lemma 2.3.

Many results have been known concerning the largest prime factor of the
product of consecutive integers. Beginning with Sylvester’s theorem [21] that
P (
∏k
i=1(x + i)) > k for x ≥ k, many results concerning the multiplicative
properties of ∏k
i=1(x + i) have been known. Erd˝os [7] gave a more elemen-
tary proof of Sylvester’s theorem. By elementary means, Hanson [8] showed that
P (
∏k
i=1(x + i)) > 1.5k for x ≥ k and (x, k) ̸= (2, 2), (7, 2), (5, 5). Using combina-
torial arguments, but with the aid of explicit estimates for π(x), Laishram and
Shorey [9] showed that P (
∏k
i=1(x + i)) > 2k for x ≥ max{k + 13, (279/262)k}
and > 1.97k for x ≥ k + 13. With the aid of other related results such as [3],
[12] and [10], Nair and Shorey [14] shows that, if x > 4k and k ≥ 2, then,
P (
∏k
i=1(x + i)) > 4.42k except only ﬁnitely many pairs (x, k), which they deter-
mined explicitly.

Methods developed in these papers allow us to prove that i) and ii), i.e., we
cannot have l < 0.001n. Indeed, our argument is essentially similar to an ar-
gument from [14]. However, in order to manipulate two products of consecutive
integers, we need a preliminary inequality given in Lemma 2.2. Moreover, we
need more complicated calculation than in papers concerning to one product of
consecutive integers. We also need some explicit estimates for the distribution of
primes and an explicit version of Stirling’s formula as in [14].

In the case n + k + l > k3/2
0 , we shall prove an inequality involving π(k0) in
Lemma 3.1 and then an upper bound for k + l in Lemma 3.2. With the aid of
preliminary estimates, we are led to an upper bound for n. Using an argument
involving prime gaps and some calculation, we show that Lemma 2.3 can never
hold for n if l < 0.001n.

In the case n + k + l ≤ k3/2
0 , we shall prove upper and lower bounds for the
size of a product of two binomial coeﬃcient in Lemmas 4.1 and 4.2 respectively.
Lemma 4.1 follows from Lemma 2.3 and Lemma 4.2 follows from an explicit
version of Stirling’s formula. But these bounds are incompatible if l < 0.001n.
Finally, it is relatively easy to prove iii) using known results for prime gaps.

In contrast, it seems to be diﬃcult to obtain a general result for (4) in cases such
as the case m ∼ k but k − m → ∞ and the case l > exp(nA) with A > 1/2. Even
speciﬁc equations such as (2n
n ) = (y
2) seem to be far beyond present techniques.

4 TOMOHIRO YAMADA

2. Preliminary lemmas

In this section, we shall introduce some preliminary lemmas. We shall begin
by some elementary lemmas.

Lemma 2.1.

(7) (l − δ) log 2n + l
n + k + l < (k − m)(k + m + δ + 1)
n − k
and

(8) (l − δ) log 2n
n + k > (k − m)(k + m + δ + 1)
n + k + δ .

Proof. It immediately follows from (6) that

(9) ( 2n + l
n + k + l
 )l−δ ≤ ( n + m + δ + 1
n − k
 )k−m

and therefore
 (l − δ) log 2n + l
n + k + l ≤(k − m) log n + m + δ + 1
n − k

< (k − m)(k + m + δ + 1)
n − k .
(10)

Similarly,

(11) ( 2n
n + k
 )l−δ ≥ ( 2n + δ + 1
n + k + δ + 1
 )l−δ ≥ ( n + k + δ
n − m − 1
 )k−m

yields that

(12) (l − δ) log 2n
n + k ≥ (k − m) log n + k + δ
n − m − 1 > (k − m)(k + m + δ + 1)
n + k + δ .
 □

This gives the following preliminary condition for k and l.

Lemma 2.2. If m ≤ 0.735k and l < 0.001n, then 588 ≤ k < 0.00151n and
l < 0.00271k.

Proof. We begin by showing that k ≥ 588. Indeed, if k ≤ 587, then, using (7)
again, we obtain

(13) l − δ < k2

(n − k) log 2.001
1.001+ k
n
 < 1

and therefore l = δ, which is impossible. Thus, we must have k ≥ 588.

Since we have assumed that m ≤ 0.735k, it immediately follows from (8) that

(14) 0.459775k2

(n + k + 1) log 2n
n+k ≤ k2 − m2

(n + k + 1) log 2n
n+k < l

NECESSARY CONDITIONS FOR BINOMIAL COLLISIONS 5

and, recalling that n ≥ 500000,

(15) 0.459775(k/n)2

(1 + (k/n) + 2 × 10−6) log 2
1+(n/k) < 0.001.

Hence, we have k/n < 0.00151.

Similarly, since we have assumed that l < 0.001n, it follows from (7) that

(16) l < 1 + (k − m)(k + m + 2)
(n − k) log 2n+l
n+k+l < 1 + (k2 − m2)(1 + 2/k)
(n − k) log 2.001n
1.001n+k .

Dividing both sides by k, recalling the assumption that m ≤ 0.735k and using
k < 0.00151n, we have

(17) l
k < 1
k + 0.459775k(1 + 2/k)
0.99849n log 2.001
1.00251 < 1
k + 0.001005 (1 + 2
k
 ) .

Now we know that k ≥ 588. Hence, we have l/k < 0.001005(1 + 1/294) + 1/588 <
0.00271. This completes the proof of the lemma. □

We write P (ν) for the largest prime factor of an integer ν > 1. The following
lemma relates our problem to the largest prime factor of a product of integers
over two intervals.

Lemma 2.3. We have

(18) P
 ( k∏

i1=m+1(n − i1)
 l+k∏

i2=m0+1
(n + i2)

)
 ≤ k0,

where m0 = max{m + δ, ⌊l/2⌋} and, as mentioned above, k0 = 2(l + k) − δ − 1.

Remark 2.4. A similar argument applied to 2n + i3 with i3 odd and δ + 1 ≤ i3 ≤ l
yields that the largest prime factor of the product of such integers is also ≤ k0.
However, this does not seem to improve our estimates.

Proof. If a prime p divides one of (n − i1)’s with m + 1 ≤ i1 ≤ k, then, by (5),
p must divide some n + i2 with m0 + 1 ≤ i2 ≤ l + k. Thus p divides i1 + i2 and
therefore p ≤ 2k + l.

Similarly, if a prime p divides one of (n + i2)’s with m0 + 1 ≤ i2 ≤ l + k, then p
must divide some n − i1 with m + 1 ≤ i1 ≤ k or 2n + i3 with δ + 1 ≤ i3 ≤ l. Thus
p divides i1 + i2 or 2i2 − i3. We see that 2i2 − i3 ̸= 0 since i2 ≥ 2(m0 + 1) > l ≥ i3.
Hence, we have p ≤ 2(l + k) − (δ + 1) = k0. □

We shall use a new explicit estimate for π(x) of Dusart in [6, Theorem 5.1],
although weaker estimates would still suﬃces.

Lemma 2.5. For x > 1,

(19) π(x) < x
log x
 (1 + 1
log x + 2
log2 x + 7.59
log3 x
 ) .

6 TOMOHIRO YAMADA

We shall also use the following version of Stirling’s formula proved by Robbins
[16].

Lemma 2.6. For any integer ν > 1, we have g−(ν) < ν! < g+(ν), where g−(z) =
(z/e)z (2πz)1/2e1/12(z+1) and g+(z) = (z/e)z (2πz)1/2e1/12z .

3. The first part of the Theorem - the case n + k + l > k3/2
0

In this section, we shall prove that l ≥ 0.001n under the condition that n +
k + l > k3/2
0 .

We assume that n, m, l, k are integers satisfying (4) with 0 ≤ m < k <
n/2, m ≤ 0.735k, l < 0.001n and n + k + l > k3/2
0 . As mentioned in the In-
troduction, we know that n ≥ 500000.

We begin by the following estimate similar to Lemma 2.9 in [14] and (17) in
[18].

Lemma 3.1.

(20) (n − k)
2k+l−m−m0−π(k0) ≤ (2k + l)
π(k0)(k − m)!(l + k − m0)!.

Proof. We write S1 and S2 for the sets of integers, respectively, n − i1 with
m + 1 ≤ i1 ≤ k and n + i2 with m0 + 1 ≤ i2 ≤ l + k and, for a given prime p, we
write vp(ν) for the exponent of a prime p dividing ν.

For a given prime p, let np,j be the integer divisible by the highest power of
p among all integers in the interval Sj for each j = 1, 2 and np be the integer
divisible by the highest power of p among all integers in S1 ∪ S2.

We see that, for any prime power pa, there exist at most
⌊ n − m − 1
pa
 ⌋ − ⌊ n − k − 1
pa
 ⌋ ≤ ⌊ k − m
pa
 ⌋ + 1

integers in S1 and at most
⌊ n + l + k
pa
 ⌋ − ⌊ n + m0
pa
 ⌋ ≤ ⌊ l + k − m0
pa
 ⌋ + 1

integers in S2 which are divisible by pa.

Since vp((k − m)!) = ∑a≥1 ⌊(k − m)/pa⌋ and vp((l + k − m0)!) =
∑a≥1 ⌊(l + k − m0)/pa⌋, we have

(21) vp
 

 ∏

n−i∈S1(n − i)



 ≤ vp(np,1) + vp((k − m)!)

and

(22) vp
 

 ∏

n+i∈S2(n + i)



 ≤ vp(np,2) + vp((l + k − m0)!).

NECESSARY CONDITIONS FOR BINOMIAL COLLISIONS 7

Moreover, if pa divides both np,1 and np,2, then pa must divide np,2 − np,1 and
therefore pa ≤ np,2 − np,1 ≤ 2k + l. These observations lead to

vp
 

 ∏

n−i1∈S1(n − i1) ∏

n+i2∈S2(n + i2)





≤ max{vp(np,1), vp(np,2)} + log(2k + l)
log p + vp((k − m)!(l + k − m0)!)

=vp(np) + log(2k + l)
log p + vp((k − m)!(l + k − m0)!).

(23)

Multiplication over all primes ≤ k0 gives

(24)
 k∏

i1=m+1
(n−i1)
 l+k∏

i2=m0+1
(n+i2) ≤
 

 ∏

p≤k0 np


 (2k+l)
π(k0)(k−m)!(l+k−m0)!

by exploiting Lemma 2.3. Now, omitting np’s for p ≤ k0 from two products in
the left hand side, we conclude that

(25) (n − k)
2k+l−m−m0−π(k0) ≤ (2k + l)
π(k0)(k − m)!(l + k − m0)!.

This proves the lemma. □

Combining Lemma 3.1 with the estimate for π(x) given in Lemma 2.5, we shall
show that k + l must be small.

Lemma 3.2. If m ≤ 0.735k, l < 0.001n and n+k +l > k3/2
0 , then k +l ≤ 871155.

Proof. Since m0 ≤ m + 1, Lemma 3.1 yields that

π(2(k + l)) log((2k + l)(k3/2
0 − 2k − l)) + log((k − m)!(l + k − m − 1)!)

≥ (2k + l − 2m − 1) log(k3/2
0 − 2k − l).
(26)

Now we write m1 = 0.735k. By Lemma 2.2, we have k < l + k < n − k and
⌊l/2⌋ < ⌊0.01k⌋ < m1. Thus, using Lemma 2.6, we obtain

π(2(k + l)) log((2k + l)(k3/2
0 − 2k − l)) + f (k − m1) + f (l + k − m1 − 1)

≥ (2k + l − 2m1 − 1) log(k3/2
0 − 2k − l),
(27)

where f (z) = log g+(z) = z log z − z + (log(2πz))/2 + 1/(12z), and therefore

π(2(k + l)) log(2k + l) + f (0.265k) + f (l + 0.265k)

− (0.53k + l − 1 − π(2(k + l))) log(k3/2
0 − 2k − l)
≥ 0.

(28)

We put F = k + l. Since k0 ≥ 2F − 2, the above inequality yields that

π(2F ) log(F + k) + f (0.265k) + f (F − 0.735k)

− (0.53k + l − 1 − π(2F )) log((2F − 2)
3/2 − F − k)
≥ 0.

(29)

8 TOMOHIRO YAMADA

Since we know that 588 ≤ k < F ≤ 1.00271k from Lemma 2.2, we have

(30) 0.53k + l − 1 − π(2F ) > 0.53F − 1 − π(2F ) > 0,

where the last inequality folllows from Lemma 2.5, and therefore

π(2F )
F + k + 0.265f ′(0.265k) − 0.735f ′(F − 0.735k)

+ 0.47 log((2F − 2)
3/2 − F − k) + F − 0.47k − 1 − π(2F )
(2F − 2)3/2 − 2k − l

>0.265 log(0.265k) − 0.735 log F + 0.47 log(F 3/2)

− 0.3675
F − 0.735k + F − 0.47k − 1 − π(2F )
(2F − 2)3/2

≥0.265 log(0.265k) − 0.03 log(1.00271k) − 0.3675
0.265k > 0.

(31)

This means that, for each ﬁxed F , the left-hand side of (29) is increasing with k
under the condition 1 ≤ l < 0.00271k. Now (29) implies that

π(2F ) log(2F − 1) + f (0.265(F − 1)) + f (F − 0.735(F − 1))

− (0.53(F − 1) − π(2F )) log((2F − 2)
3/2 − 2F + 1)
≥ 0.

(32)

With the aid of Lemma 2.5, we must have F ≤ 871155. □

Now we shall prove that (4) cannot hold when 0 ≤ m < k < n/2, m ≤
0.735k, l < 0.001n and n + k + l > k3/2
0 .

By Lemmas 2.2 and 3.2, we must have 589 ≤ k + l ≤ 871155 and l < 0.00271k.
Using Lemma 3.1, we obtain n ≤ 31754673611.

Let d(p) be the gap of primes q − p, where q is the next prime after p. We
know that d(p) ≤ 456 for any prime p ≤ 3.2 × 1010 from [15].

By Lemma 2.3, there exist no prime in S2 since k0 < 2(k +l) < n. Hence, if p is
the largest prime p ≤ n+m0, then k+l−m0 ≤ d(p)−1. Since n+m0 < 3.2×1010,
we have k + l − m0 ≤ 455. It immediately follows that 0.265k + l ≤ 455, k ≤ 1713
and k0 ≤ 2(k + l) − 1 ≤ 3427.

Using Lemma 2.3 again, we have P (
∏m+1≤i≤k(n − i)) ≤ 3413. There exists
no prime among such n − i’s since n − k > 0.5n > 3413. Hence, we can take two
consecutive primes q and q′ satisfying q ≤ n − k − 1 < n − m ≤ q′ = q + d(q). We
see that q ≤ n ≤ 31754673611 and d(q) ≥ 158 since d(q) ≥ 0.265k + 1 > 157.

Our computer search found exactly 572960 primes q ≤ 31754673611 with
d(q) ≥ 158. For all of such primes, we conﬁrmed that P (
∏152≤i≤156(q + i)) >
3427 ≥ k0 and P (
∏303≤i≤308(q + i)) > 3427 ≥ k0. Recalling that d(q) ≤
456 for q ≤ 31754673611, we conclude that P (
∏1≤i≤156(z + i)) > 3427 for
any positive integer z ≤ 31754673611. This implies that we can never have

NECESSARY CONDITIONS FOR BINOMIAL COLLISIONS 9

P (
∏m+1≤i≤k(n − i)) ≤ 3413. Thus, (4) cannot hold when 0 ≤ m < k < n/2, m ≤

0.735k, l < 0.001n and n + k + l > k3/2
0 .

4. The first part of the Theorem - the case n + k + l ≤ k3/2
0

Nextly, we shall prove that l ≥ 0.001n in the case n + k + l ≤ k3/2
0 . We begin
by proving the following lemma, which is similar to Lemma 3 of [18].

Lemma 4.1. If n + k + l ≤ k3/2
0 , then

(33) (n − m − 1
k − m
 )(n + k + l
l + k
2 − δ
) ≤ (2.83)
k0+3k3/4
0 .

Proof. We begin by introducing Chebyshev’s functions θ(x) = ∑p≤x log p and
ψ(x) = ∑pe≤x log p, where pe runs all prime powers below x.

Lemma 2.3 immediately implies that

(34) P ((n − m − 1
k − m
 )(n + k + l
l + k
2 − δ
)) ≤ k0.

As in [7], we observe that, for any prime p and integers ν ≥ r ≥ 0 with pa dividing(ν
r)
, we have pa ≤ ν. Hence, we obtain

(n − m − 1
k − m
 )(n + k + l
l + k
2 − δ
) ≤
 

 ∏

p≤k0 p



 

∏

u≥2
 

 ∏

p<(n+k+l)1/u p




2



=e
θ(k0)+∑u≥2 2θ((n+k+l)1/u).

(35)

The sum in the exponent is at most

2 ∑

v≥1 θ((n + k + l)
1/(2v)) + 2 ∑

v≥1 θ((n + k + l)
1/(2v+1))

≤3 ∑

v≥1 θ((n + k + l)
1/(2v)) + ∑

v≥1 θ((n + k + l)
1/(2v+1))

=3ψ((n + k + l)
1/2) + ∑

v≥1 θ((n + k + l)
1/(2v+1)).

(36)

Since we have assumed that n + k + l ≤ k3/2
0 , we obtain

(37) ∑

v≥1 θ((n + k + l)
1/(2v+1)) < ∑

v≥1 θ(k1/(2v)
0 )

and
 θ(k0) + ∑

u≥2 2θ((n + k + l)
1/u) < ψ(k0) + 3ψ(k3/4
0 ).(38)

By Theorem 12 of [17], we have ψ(z) < 1.03883z < z log(2.83) for any real z > 0.
This proves the lemma. □

10 TOMOHIRO YAMADA

We also need the other inequality, which can be derived from the explicit
version of Stirling’s formula given in Lemma 2.6.

Lemma 4.2. If m ≤ 0.735n, l < 0.001n and n + k + l ≤ k3/2
0 , then

(39) log ((n − m − 1
k − m
 )( n + k + l
l + k − m0
)) > 4.6623k − 2.879 − log k.

Proof. We write m1 = 0.735k as in the previous lemma. It is clear that m ≤
ηk < αηn. Thus Lemma 2.6 gives
(n − m − 1
k − m
 ) ≥ n − k
n − m
 (n − m
k − m
)

= n − k
n − m (n − m)!
(n − k)!(k − m)!

≥ n − k
n − m g−(n − m)
g+(n − k)g+(k − m)

≥ n − k
n − m1
 g−(n − m1))
g+(n − k)g+(k − m1) ,

(40)

where we note that g−(n − z)/((n − z)g+(k − z)) is a decreasing function of z for
0 ≤ z ≤ 0.735k.

We observe that for any real z, z1 > 0,

log (z + z1)z+z1

zzzz1
1 = log (1 + z1/z)z+z1

(z1/z)z1

=z [(
1 + z1
z
 ) log (1 + z1
z
 ) − z1
z log z1
z
 ]

=z ∫ 1+z1/z

z1/z (1 + log t)dt > z log ez1
z .

(41)

With the aid of this inequality, we obtain

g−(n − m1)
g+(n − k)g+(k − m1) > (n − m1)n−m1

(n − k)n−k(k − m1)k−m1
 √ n − m1
2π(n − k)(k − m1)

× e
 1
12(n−m1 +1) − 1
12(n−k) − 1
12(k−m1 )

> (e ( n − k
k − m1
 ))k−m1 √ n − m1
2π(n − k)(k − m1)

× e
 1
12(n−m1 +1) − 1
12(n−k) − 1
12(k−m1 ) .

(42)

Thus, (40) becomes

log (n − m − 1
k − m
 ) ≥ log n − k
n − m + (k − m1) (1 + log ( n − k
k − m1
 ))

+ 1
2 log n − m1
2π(n − k)(k − m1) − 1
12(n − k) − 1
12(k − m1) .

(43)
 NECESSARY CONDITIONS FOR BINOMIAL COLLISIONS 11

From the assumption and Lemma 2.2, we see that k − m1 ≥ 0.265k > 155 and
n − k ≥ 0.99849n ≥ 499245. Hence, putting α = k/n, we obtain

log (n − m − 1
k − m
 ) ≥ log 1 − α
1 − 0.735α + 0.265αn (1 + log ( 1 − α
1 − 0.735α
 ))

+ 1
2 log 1 − 0.735α
0.53πα(1 − α)n − 0.0006.
(44)

We have α ≤ 0.00151 by Lemma 2.2 and therefore

log 1 − α
1 − 0.735α + 1
2 log 1 − 0.735α
0.53π(1 − α) = 1
2 log 1 − α
0.53π(1 − 0.735α)
> − 0.2552.
(45)

Thus, we conclude that

(46) log (n − m − 1
k − m
 ) ≥ 0.265αn (1 + log ( 1 − α
1 − 0.735α
 )) − log(αn)
2 − 0.2558.

Similarly, we have

g−(n + k + l))
g+(k + l − m1)g+(n + m1) > ( e(n + m1)
k + l − m1
 )k+l−m1

×
√ n + k + l
2π(n + m1)(k + l − m1) × e
 1
12(n+k+l+1) − 1
12(n+m1 ) − 1
12(k+l−m1)
(47)

and, noting that m0 ≤ max{m + 1, l/2} ≤ max{m1 + 1, 0.002k} = m1 + 1,

log ( n + k + l
k + l − m0
) ≥ log k + l − m1
n + m1 + 1 + (k + l − m1) (1 + log n + m1
k + l − m1
 )

+ 1
2 log n + k + l
2π(n + m1)(k + l − m1) − 1
12(n + m1) − 1
12(k + l − m1)

≥ log (0.265 + λ)α
1 + 0.735α + (0.265 + λ)αn (1 + log 1 + 0.735α
(0.265 + λ)α
 )

+ 1
2 log 1 + α(1 + λ)
2π(0.265 + λ)(1 + 0.735α)αn − 0.0006,

(48)

where we put λ = l/k and used the fact that k − m1 ≥ 0.265k > 156 and
n − k ≥ 499245.

We have α ≤ 0.00151 and λ ≤ 0.00271 by Lemma 2.2 and therefore

log (0.265 + λ)α
1 + 0.735α + 1
2 log 1 + α(1 + λ)
2π(0.265 + λ)(1 + 0.735α)

= 1
2 log (1 + α(1 + λ))(0.265 + λ)
2π(1 + 0.735α)3

≥ 1
2 log 0.265(1 + α)
2π(1 + 0.735α)3 > −1.5788.

(49)

12 TOMOHIRO YAMADA

Thus, we conclude that

log ( n + k + l
k + l − m0
) ≥(0.265 + λ)αn (1 + log 1 + 0.735α
(0.265 + λ)α
 )

+ log(α/n)
2 − 1.5794.

(50)

Combining (46) and (50), we obtain

log ((n − m − 1
k − m
 )( n + k + l
l + k − m0
))

>0.265αn (1 + 1 − α
0.265α
 ) + (0.265 + λ)αn (1 + 1 + 0.735α
(0.265 + λ)α
 )

− 1.8352 − log n.

(51)

We put

(52) h(α, λ) = 0.265 (1 + log 1 − α
0.265α
 ) + (0.265 + λ) (1 + log 1 + 0.735α
α (0.265 + λ)
 ) .

For a ﬁxed λ, h(α, λ) is decreasing over 0 < α < 1 since ∂h/∂α = −0.265/α(1 −
α) − (0.265 + λ)/α(1 + 0.735α) < 0. On the other hand, for a ﬁxed α, h(α, λ)
is increasing over 0 < λ < 0.00271 since ∂h/∂λ(α, λ) = log(1 + 0.735α)/(α(λ +
0.265)) > 0. Hence, h(α, λ) ≥ h(0.00151, 0) > 4.6623. Now (51) gives

(53) log ((n − m − 1
k − m
 )( n + k + l
l + k − m0
)) > 4.6623αn − 1.8352 − log n.

Since we have assumed that n + k + l ≤ k3/2
0 = (2(k + l) − δ − 1)3/2 and Lemma
2.2 gives l < 0.00271k, we have n < (2(k + l))3/2 < (2.00542k)3/2. Hence,
1.8352 + log n < 2.879 + (3/2) log k. This proves the lemma. □

Now we shall prove that (4) cannot hold when 0 ≤ m < k < n/2, m ≤
0.735k, l < 0.001n and n + k + l ≤ k3/2
0 . We apply Lemma 4.1 to obtain
(54)

log ((n − m − 1
k − m
 )( n + k + l
l + k − m0
)) ≤ k0 + 3k3/4
0 log(2.83) < 1.0433k + 3.13k3/4,

where we used Lemma 2.2 to see that k0 ≤ k + l < 1.00271k. Now, using Lemma
4.2, we have

(55) 4.6623k − 1.8344 − log k < 1.0433k + 3.13k3/4,

which is impossible for k ≥ 588. Thus, we see that (4) can never hold when
0 ≤ m < k < n/2, m ≤ 0.735k and l < 0.001n.

5. The remaining case: l ≥ 0.001n

In this section, we discuss the remaining case: n, m, l, k are integers satisfying
(4) with 0 ≤ m < k < n/2, m ≤ 0.735k and l ≥ 0.001n. Since n ≥ 500000,

NECESSARY CONDITIONS FOR BINOMIAL COLLISIONS 13

Proposition 5.4 of [6] implies that there exists at least one prime 2n + δ + 1 ≤
p ≤ 2n + l.

Now, let 2n + t be the largest prime ≤ 2n + l. From (5), it is clear that
2n + t must divide n + i for some i ≤ k + l. Using Proposition 5.4 of [6] again,
we must have n − k ≤ l − t < (2n + l)/ log3(2n + l) and therefore log (2n+l
n−k ) <
(n − k) log(2n + l) < (2n + l)/ log2(2n + l).

On the other hand, since m ≤ 0.735k < 0.735n, we have
(2n + δ
n − m
) > g−(2n)
g+(0.735n)g+(1.265n)

> ( (2/0.735)2

((2/0.735) − 1)1.265
 )n √ 1
0.929775πn

× e
 1
12(2n+1) − 1
12n
 ( 1
η + 1
2−η
 )

(56)

by Lemma 2.6. Taking its logarithm, we have

(57) 2n + l
log2(2n + l) > 1.3132n − 1
2 log n − 0.5359.

Observing that log2(2n)((1/2) log n + 0.5359) < 0.00271n for n > 500000, we
conclude that

(58) l > n(1.3132 log2(2n) − 2.00271).

Furthermore, from the result of [2], we must have n − k ≤ l − t < (2n + l)21/40

for suﬃciently large n. Proceeding as above, we obtain

(59) (2n + l)
21/40 log(2n + l) > 1.3132n − 1
2 log n − 0.5359.

Thus, we conclude that l > (cn/ log n)40/21 for suﬃciently large n. This completes
the proof of the Theorem.
 References

[1] `E. T. Avanesov, Solutions of a problem on ﬁgurate numbers (Russian), Acta Arith. 12 (1966),
409–420.
[2] R. C. Baker, G. Harman and J. Pintz, The diﬀerence between consecutive primes, II, Proc.
London. Math. Soc. (3) 83, 532–562.
[3] Mark Bauer and Michael A. Bennett, Prime factors of consecutive integers, Math. Comp.
77 (2008), 2455–2459.
[4] Aart Blokhuis, Andries Brouwer and Benne de Weger, Binomial collisions and near collisions,
Integers 17 (2017), A64.
[5] Yann Bugeaud, Maurice Mignotte, Samir Siksek, Michael Stoll and Szabolic Tengely, Integral
points on hyperelliptic curves, Algebra Number Theory 2 (2008), 859–885.
[6] Pierre Dusart, Explicit estimates of some functions over primes, Ramanujan J. 45 (2018),
227–251.
[7] Paul Erd˝os, A theorem of Sylvester and Schur, J. London Math. Soc. 9 (1934), 282–288.
[8] D. Hanson, On a theorem of Sylvester and Schur, Canada Math. Bull. 16 (1973), 195–199.
[9] Shanta Laishram and T. N. Shorey, The greatest prime divisor of a product of consecutive
integers, Acta Arith. 120 (2005), 299-306.

14 TOMOHIRO YAMADA

[10] Shanta Laishram and T. N. Shorey, Grimm’s conjecture on consecutive integers, Int. J.
Number Theory 2 (2006), 207–211.
[11] D. A. Lind, The quadratic ﬁeld Q(√5) and a certain diophantine equation, Fibonacci Quart.
6 (3) (1968), 86–93.
[12] Florian Luca and Filip Najman, On the largest prime factor of x2 − 1, Math. Comp. 80
(2011), 429–435.
[13] L. J. Mordell, On the integer solutions of y(y + 1) = x(x + 1)(x + 2), Paciﬁc J. Math. 13
(1963), 1347–1351.
[14] Saranya G. Nair and T. N. Shorey, Lower bounds for the greatest prime factor of product
of consecutive positive integers, J. Number Theory 159 (2016), 307–328.
[15] Thomas R. Nicely, First occurrence prime gaps, http://www.trnicely.net/gaps/gaplist.html
[16] H. Robbins, A remark on Stirling’s formula, Amer. Math. Monthly, 62 (1955), 26–29.
[17] J. Barkley Rosser and Lowell Schoenfeld, Approximate formula for some functions of prime
numbers, Illinois J. Math. 6 (1962), 64–94.
[18] N. Saradha and T. N. Shorey, Almost squares and factorisations in consecutive integers,
Compos. Math. 138 (2003), 113–124.
[19] David Singmaster, Repeated binomial coeﬃcients and Fibonacci numbers, Fibonacci Quart.
13 (1975), 295–298.
[20] Roelof J. Stroeker and Benjamin M. M. de Weger, Elliptic binomial diophantine equations,
Math. Comp. 68 (1999), 1257–1281.
[21] J. J. Sylvester, On arithmetical series, Messenger of Math. 21 (1892), 1–19.
[22] Craig A. Tovey, Multiple occurences of binomial coeﬃcients, Fibonacci Quart. 23 (1985),
356–358.
[23] Benjamin M. M. de Weger, Equal binomial coeﬃcients: some elementary considerations, J.
Number Theory 63 (1997), 373–386.

* Center for Japanese language and culture
Osaka University
562-8558
8-1-1, Aomatanihigashi, Minoo, Osaka
JAPAN

E-mail address: tyamada1093@gmail.com
