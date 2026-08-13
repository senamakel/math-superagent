<!-- source: https://arxiv.org/pdf/2107.09107 | converted from PDF -->

arXiv:2107.09107v1  [math.NT]  19 Jul 2021
REPETITIONS OF MULTINOMIAL COEFFICIENTS AND A
GENERALIZATION OF SINGMASTER’S CONJECTURE

Jean-Marie de Koninck
D´epartement de math´ematiques, Universit´e Laval, Qu´ebec, Canada
jmdk@mat.ulaval.ca

Nicolas Doyon
D´epartement de math´ematiques, Universit´e Laval, Qu´ebec, Canada
Nicolas.Doyon@mat.ulaval.ca

William Verreault
D´epartement de math´ematiques, Universit´e Laval, Qu´ebec, Canada
william.verreault.2@ulaval.ca

Abstract
Given two integers k ≥ 2 and a > 1, let Nk(a) stand for the number of multi-
nomial coeﬃcients, with k terms, equal to a. We study the behavior of Nk(a)
and show that its average and normal orders are equal to k(k − 1). We also prove
that Nk(a) = O (
(log a/ log log a)
k−1) and make several propositions about extreme
results regarding large values of Nk(a).

1. Introduction

Let N (a) denote the number of times the integer a > 1 occurs as a binomial co-

eﬃcient, that is, N (a) = # {
(n, r) ∈ N2 : (
n
r
) = a}
. Singmaster [7] conjectured

that N (a) = O(1) and proved that N (a) = O(log a). Abbott, Erd˝os, and Hanson

[1] later showed that N (a) = O ( log a
log log a
 ) and that its average and normal orders

are 2. Finally, Kane [3], [4] improved the bounds to O ( log a log log log a
(log log a)2
 ) and

O ( log a log log log a
(log log a)3
 )
, respectively.

Considering the properties of Pascal’s triangle, one can reformulate the problem
as follows. Is there an upper bound for the number of times a given integer appears
in Pascal’s triangle?
Despite the fact that inﬁnitely many positive integers appear at least six times
in Pascal’s triangle [8], only nine such integers, namely

1, 120, 210, 1540, 3003, 7140, 11 628, 24 310 and 61218182743304701891431482520,

have been found to satisfy this property up to 1060 [6]. It is worth noting that

2

N (3003) = 8, and that this is the highest known value of N (a). Singmaster [8]
actually conjectured that its maximal value might be 8, 10 or 12.
In what follows, we study repetitions of multinomial coeﬃcients, that is, for

a ﬁxed integer k ≥ 2, those numbers ( m
m1, . . . , mk
) = m!
m1! · · · mk! , where m =

k∑

i=1 mi.

Given an integer k ≥ 2, let m = (m1, . . . , mk) ∈ Nk, and let

Nk(a) = # {
m ∈ Nk : ( m
m1, . . . , mk
) = a}

denote the number of times the integer a > 1 occurs as a multinomial coeﬃcient.
As such, Nk(a) is a generalized version of N (a) where we consider multinomial
coeﬃcients of k terms equal to a, and in particular, N (a) = N2(a).
If one considers Pascal’s k-simplices as a generalization of Pascal’s triangle in
dimension k, where the entries of the simplex are given by multinomial coeﬃcients
of k terms, then the problem is equivalent to asking whether there is an upper
bound on the number of times an integer appears in Pascal’s k-simplex for a given
k ≥ 2.
A simple program tells us that in the ﬁrst 1000 lines of Pascal’s triangle, 494
integers appear once, 248 861 twice, 5 three times, 63 four times and 3 six times. In
comparison, Pascal’s 3-simplex, often called Pascal’s pyramid, has 445 666 distinct
integers in its ﬁrst 250 layers, of which 429 135 appear exactly six times. These
results were to be expected, as we will see.
Obviously, it may be the case that for any ﬁxed value of k ≥ 2, Nk(a) is bounded.
We will also pursue this investigation for large values of k.

2. Main results

We start by showing that the average and normal orders of Nk(a) are both k(k − 1).
Intuitively, the average order of Nk(a) is another arithmetic function which takes
the same values on average, while its normal order is an arithmetic function which
is close to Nk(a) for almost all values of a. Consequently, our ﬁrst theorem implies
that for any given integer a > 1, there are almost always k(k − 1) multinomial
coeﬃcients with k terms equal to a. An immediate corollary is that almost always
one can ﬁnd any given integer a total of k(k − 1) times in Pascal’s k-simplex.

Remark 1. A multinomial coeﬃcient of the form ( a
a − 1, 1, 0, . . . , 0
) is always

equal to a. As such, one gets Nk(a) ≥ k(k − 1) for all k ≥ 2. Now notice that

3

a = 1 and a = 2 are the only exceptions to this, and while 1 appears inﬁnitely many

times, 2 occurs (
k
2
) times as a multinomial coeﬃcient, for it must be of the form
( 2
1, 1, 0, . . . , 0

)
.

Theorem 1. Let k ≥ 2 be a ﬁxed integer and Nk(a) be deﬁned as above. Then, the
average and normal orders of Nk(a) are both k(k − 1).

Proof. Let M be a positive integer. We deﬁne

S(k, M ) = {
m : 2 < ( m
m1, . . . , mk
) ≤ M } ,

S1(k, M ) = {m ∈ S(k, M ) : mi = m − 1 for some i ∈ {1, . . . , k}} ,

S2(k, M ) = S(k, M ) \ S1(k, M ).

Following Remark 1, we ﬁnd that

∑

1<a≤M Nk(a) = (
k
2
) + ∑

m∈S(k,M) 1 (1)

= (
k
2
) + ∑

m∈S1(k,M) 1 + ∑

m∈S2(k,M) 1.

Now, since ∑

m∈S1(k,M) 1 = k(k − 1) ∑

2<( m
1,0,...,0,m−1)≤M 1 (2)

= k(k − 1) ∑

2<m≤M 1

= k(k − 1)(M − 2),

it only remains to consider ∑

m∈S2(k,M) 1.

If m ∈ S2(k, M ), then 2 < ( m
m1, . . . , mk
) ≤ M and mi < m−1 for i = 1, 2, . . . , k.

Assume, without loss of generality, that mi ≤ mi+1 for i = 1, 2, . . . , k − 1. Then we
have the inequalities

M ≥ ( m
m1, . . . , mk
) ≥ m!
mj!(m − mj)! ≥ (
2mj
mj
 ) ≥ 2mj (j = 1, 2, . . . , k − 1) (3)

and
 M ≥ ( m
m1, . . . , mk
) ≥ m!
mk!(m − mk)! ≥ (
m
2
 ) = m(m − 1)
2 ,
 4

which implies that mj = O(log M ) and m = O(M 1/2), respectively.
Since the value of mk is entirely determined by that of m, m1, m2, . . . , mk−1, we
get ∑

m∈S2(k,M) 1 = ∑

2<( m
m1 ,...,mk)≤M
0≤mi<m−1
 1 = ∑

mi
1≤i≤k−1
 ∑

m 1 = O (M 1/2 (log M )
k−1) . (4)

Using (2) and (4) in (1), we obtain

∑

1<a≤M Nk(a) = (
k
2
) + k(k − 1)(M − 2) + O (M 1/2 (log M )
k−1) , (5)

and therefore,

lim
M→∞ 1
M
 ∑

1<a≤M Nk(a)

= lim
M→∞ 1
M
 ((
k
2
) + k(k − 1)(M − 2) + O(M 1/2(log M )
k−1)
)

= k(k − 1),

which provides the average order of Nk(a).
For the normal order, let

fk(M ) = # {1 < a ≤ M : Nk(a) < k(k − 1)} ,

gk(M ) = # {1 < a ≤ M : Nk(a) = k(k − 1)} ,

hk(M ) = # {1 < a ≤ M : Nk(a) > k(k − 1)} .

We wish to prove that Nk(a) − k(k − 1) ≤ εk(k − 1) for all ε > 0 and for almost all
a. It should be clear that this inequality holds only if Nk(a) = k(k − 1), for Nk(a)
only takes integral values. As such, it suﬃces to show that fk(M ) + hk(M ) = o(M )
as M → ∞.
Now Remark 1 implies that fk(M ) = 1. Also, gk(M ) + hk(M ) = M − 2 since
they only exclude a = 1 and a = 2. Thus,
∑

1<a≤M Nk(a) ≥ fk(M ) + k(k − 1)gk(M ) + (k(k − 1) + 1)hk(M )

= 1 + k(k − 1)(gk(M ) + hk(M )) + hk(M )

= 1 + k(k − 1)(M − 2) + hk(M ). (6)

Comparing (6) with (5), we get that hk(M ) = O (
M 1/2(log M )
k−1), which means
that fk(M ) + hk(M ) = o(M ) as M → ∞ and in turn implies that the normal order
of Nk(a) is indeed k(k − 1).
 5

We also state an additional result, even though it is weaker than our claim

Nk(a) = O
 (( log a
log log a
 )k−1)
 ,

be it simply for the fact that our proof is both more general and simpler than that
of Singmaster in [7].

Proposition 1. Let k ≥ 2 be a ﬁxed integer. Then Nk(a) = O (logk−1 a) .

Proof. Since ( m+1
m1,...,mj+1,...,mk)

( m
m1,...,mk) =
 m+1
mj +1 ( m
m1,...,mk)

( m
m1,...,mk) = m + 1
mj + 1 ≥ 1,

the multinomial coeﬃcients are strictly increasing in mj for all 1 ≤ j ≤ k, which
implies that if we ﬁx k − 1 parameters in the multinomial coeﬃcient, say all but
mi, then
 # {
mi : ( m
m1, . . . , mk
) = a} ≤ 1. (7)

The proof is based on the observation that, for all 1 ≤ i ≤ k,

Nk(a) = ∑

mj
j ∈ {1,...,k}\{i}
 # {
mi : ( m
m1, . . . , mk
) = a} ,

so that in particular,

Nk(a) = ∑

mj
1≤j≤k−1
 # {
mk : ( m
m1, . . . , mk
) = a} ≤ ∑

mj
1≤j≤k−1
 1 = O(logk−1 a),

where we used (7) and (3).

Remark 2. One may be tempted to write Nk(a) as a sum over less than k − 1
ﬁxed parameters, but then it becomes quite a tedious task to determine the number
of multinomial coeﬃcients equal to a. This is why we should be satisﬁed with this
bound for now.

Next, we generalize a result of Abbott, Erd˝os, and Hanson [1], obtaining a better
upper bound for Nk(a). We will need two lemmas.

Lemma 1 (Baker, Harman, and Pintz [2]). There exists a real number x0 such that
the interval [x, x + x
0.525] contains at least one prime number for all x > x0.

Lemma 2. For each j = 1, 2, . . . , k, we have ( m
m1, . . . , mk
) ≥ ( m
mj
 )mj .
 6

Proof. We proceed by induction on mj. At ﬁrst, if mj = 1, then,
( m
m1, . . . , mk
) = (
m1 + · · · + mj−1 + 1 + mj+1 + · · · + mk
m1, . . . , mj−1, 1, mj+1 . . . , mk
 )

= (m1 + · · · + mj−1 + 1 + mj+1 + · · · + mk)
(
m1 + · · · + mj−1 + mj+1 + · · · + mk
m1, . . . , mj−1, mj+1, . . . , mk
 )

≥ (m1 + · · · + mj−1 + 1 + mj+1 + · · · + mk).

Now, ( m + 1
m1, . . . , mj + 1, . . . , mk
) = m + 1
mj + 1
 ( m
m1, . . . , mk
)

≥ m + 1
mj + 1
 ( m
mj
 )mj

≥ m + 1
mj + 1
 ( m + 1
mj + 1
 )mj

= ( m + 1
mj + 1
 )mj +1 ,

where the second to last inequality holds since m ≥ mj.

Theorem 2. Let k ≥ 2 be a ﬁxed integer. Then, Nk(a) = O
 (( log a
log log a
 )k−1)
 .

Proof. We let mi ≤ mi+1 for i = 1, 2, . . . , k − 1 without loss of generality.
Let
 A = {
m ∈ Nk(a) : m > log 22
21 a} ,

B = {
m ∈ Nk(a) : m ≤ log 22
21 a} ,

so that Nk(a) = #A + #B. Hence, it is suﬃcient to show that #A and #B are
both
 O
 (( log a
log log a
 )k−1)
 .

First, assume m is in A, so that
m > log 22
21 a. (8)

Notice that in (3), we have not used the fact that mi < m − 1 for all 1 ≤ i ≤ k.
Thus, we can write
 mi ≤ log a
log 2 (i = 1, 2, . . . , k − 1). (9)

7

Using Lemma 2, (8) and (9), we get

mi ≤ log a
log m
mi < log a

log log 22
21 a
log a/ log 2
 = O ( log a
log log a
 ) (i = 1, 2, . . . , k − 1).

By monotonicity, for ﬁxed m1, . . . , mk−1, there is only one mk that yields a
multinomial coeﬃcient equal to a. Hence,

#A = O
 (( log a
log log a
 )k−1)
 . (10)

Secondly, assume m is in B. Let M = M1+M2 +· · ·+Mk be the greatest element
for which the associated M = (M1, . . . , Mk) lies in B. We also deﬁne S = M − M1.
Then,
 a = M !
M1! · · · Mk! < M !
(M − S)! = M (M − 1) · · · (M − S + 1) < M S.

From M ≤ log 22
21 a and a < M S, we get

M < (S log M ) 22
21 .

Note that log 22
21 M ≤ S 18
21 for all M ≥ 2.

Since k ≥ 2 and M1 is maximal when all parameters are equal, it is suﬃcient
to show that the result holds for M1 = M/2. It is easy to verify that log 22
21 M ≤
(M/2) 18
21 for all M ≥ 2.
Therefore, M ≤ S22/21S18/21 < S40/21 + S or, equivalently, (M − S)
21/40 < S.
Adding M − S on both sides, we ﬁnally have (M − S)
21/40 + (M − S) < M, that is,

M1 + M 21/40
1 < M. (11)

Using Lemma 1, there exists a prime in [
M1, M1 + M
 21
40
1 ]. Combining the latter

with (11), there is a largest prime P satisfying

M1 ≤ P < M,

which tells us that P divides our ﬁxed a, so the same can be said of any m for which
the associated m is in B. Thus, P ≤ m ≤ M whenever m ≤ log 22
21 a. As such, there
are at most M − P elements in B.
Next, let x = P in Lemma 1 and let Q be the largest prime in the interval[
P, P + P 21
40 ]
. Then, since P is the largest prime less than M , we must have

P < M ≤ Q ≤ P + P 21/40,
 8

and so it follows that

#B ≤ M − P ≤ P 21
40 < M 21
40 ≤ (log 22
21 a) 21
40 = log 11
20 a = O
 (( log a
log log a
 )k−1)
 ,

which, combined with (10), yields the desired result.

We end this paper by stating some partial results regarding large values of Nk(a).
We will see that we can do much better than the naive bound Nk(a) ≥ k(k − 1) for
all k ≥ 2.

Proposition 2. For any integer k > 2,

#{a ≤ x : Nk(a) ≥ k!} ≫ x 2
(k−1)(k−2) .

Proof. We will force a to take the form of a multinomial coeﬃcient by counting the
integers a that can be written as

a = (m + (k − 1)(k − 2)/2)!
0!1! · · · (k − 2)!m! ≤ x, (12)

which obviously has at least k! representations as a multinomial coeﬃcient once x
is big enough, by permuting the terms in the denominator. We have

(m + (k − 1)(k − 2)/2)!
0!1! · · · (k − 2)!m! =
 k−2∏

j=1
 1
j!
 (k−1)(k−2)/2∏

j=1 (m + j) ∼ Ckm
 (k−1)(k−2)
2

as m → ∞, where
 Ck =
 k−2∏

j=1
 1
j! .

It follows that for x large enough, (12) holds as long as

(1 + ε)Ckm(k−1)(k−2)/2 ≤ x

for any given ε > 0, that is

m ≤ 1

((1 + ε)Ck) 2
(k−1)(k−2) x 2
(k−1)(k−2) ,

which proves our claim.

Proposition 3. For each k ≥ 4,

#{a : Nk(a) ≥ 2 · k! + k(k − 1)} = ∞.
 9

Note that this proposition also works for k = 2 since inﬁnitely many positive
integers appear at least six times in Pascal’s triangle.

Proof. Our proof follows from the simple identity

12!2!1! = 11!4!0!, (13)

from which we have, for any m ≥ 15,

a(m) := m!
12!2!1!(m − 15)! = m!
11!4!0!(m − 15)! .

If m ≥ 28, all the integers appearing in the denominator of the above equation
are distinct, thus providing 2 · 4! = 48 distinct vectors. To obtain the remaining
4 · 3 = 12 vectors, we just have to consider the expression

a(m)!
(a(m) − 1)!1!0!0! ,

thus completing the proof of the proposition when k = 4. This idea can easily be
generalized for k > 4 by observing that

(m + m5 + m6 + · · · + mk)!
12!2!1!(m − 15)!m5!m6! · · · mk! = (m + m5 + m6 + · · · mk)!
11!4!0!(m − 15)!m5!m6! · · · mk! .

Proposition 4. For each k ≥ 7,

#{a : Nk(a) ≥ 7 · k!/2 + k(k − 1)} = ∞.

Proof. First observe the identity

24!5!3!1! = 23!6!4!0!. (14)

From equations (13) and (14), we have

24!5!3!1!12!2! = 23!6!4!0!12!2! = 24!5!3!11!4!0! = 23!6!4!0!11!4!0!,

from which we can deduce that for any m ≥ 47,

m!
24!12!5!3!2!1!(m − 47)! = m!
23!12!6!4!2!0!(m − 47)! = m!
24!11!5!4!3!0!(m − 47)!

= m!
23!6!4!0!11!4!0!(m − 47)! .

By choosing m ≥ 72, we ensure that all the integers appearing in the denominator
are distinct, except 0 in the last denominator, which provides 7 · 7!/2 = 17 640
solutions. To obtain the 7 · 6 = 42 remaining solutions, we set

a(m) = m!
24!12!5!3!2!1!(m − 47)!
 10

and consider the quantity
 a(m)!
(a(m) − 1)!1!0!0!0!0!0!.

This argument can be generalized for k > 7, by observing that

(m + m8 + m9 + · · · + mk)!
24!12!5!3!2!1!(m − 47)!m8!m9! · · · mk!

= (m + m8 + m9 + · · · + mk)!
23!12!6!4!2!0!(m − 47)!m8!m9! · · · mk!

= (m + m8 + m + m9 + · · · + mk)!
24!11!5!4!3!0!(m − 47)!m8!m9! · · · mk!

= (m + m8 + m + m9 + · · · + mk)!
23!6!4!0!11!4!0!(m − 47)!m8!m9! · · · mk! .

From this we have that for k ≥ 7,

#{a : Nk(a) ≥ 7 · k!/2 + k(k − 1)} = ∞.

We also looked numerically for large values of N3(a) and N4(a). With a =
2671465728531600, we found that N3(a) ≥ 30 and N4(a) ≥ 180. Recall that we
expect N3(a) = 6 and N4(a) = 12. The bound N3(a) ≥ 30 comes from the fact that

a = 37!
7!11!9! = 38!
19!11!8! = 39!
19!14!6! = 40!
19!16!5! = a!
(a − 1)!1!0! .

To prove the bound N4(a) ≥ 180, it suﬃces to observe that

a = 37!
17!11!9!0! = 38!
19!11!8!0! = 39!
19!14!6!0!

= 40!
19!16!5!0! = 40!
20!16!3!1! = 39!
21!13!4!1! = 38!
22!10!4!2! = a!
(a − 1)!1!0!0!.

3. Concluding remarks

At this point, it seems natural to ask whether Nk(a) = O(1) for all k ≥ 2. How-
ever, the problem seems just as hard as in the basic case of binomial coeﬃcients.
Obviously, as multinomial coeﬃcients can be rewritten as a product of binomial
coeﬃcients, it would be particularly interesting to show that proving Singmaster’s
conjecture is equivalent to proving its generalization in any dimension k ≥ 2. Per-
haps considering symmetries and patterns in Pascal’s k-simplex would help. For
example, setting a parameter to 0 in m leads us to Pascal’s (k − 1)-simplex, and
induction seems to be the way forward.
 11

Our ﬁnal remark is that there is still a lot we don’t know about repetitions of
multinomial coeﬃcients. For instance, whether N2(a) = 5 or N2(a) = 7 is even
possible. Furthermore, Singmaster [8] showed that
(
F2i+2F2i+3
F2iF2i+3
 ) = (
F2i+2F2i+3 − 1
F2iF2i+3 + 1
 ),

where Fn is the nth Fibonacci number, by solving a type of Pell equation. The
same result has been proved in [5]. This implies that inﬁnitely many integers are
going to appear at least six times in Pascal’s triangle, as stated in the Introduction.
Perhaps similar considerations, such as the ones we made in Propositions 2, 3 and
4, can be made in higher dimensions to ﬁnd equal multinomial coeﬃcients, although
equations in several variables would have to be solved in a diﬀerent manner.

References

[1] H.L. Abbott, P. Erd˝os, and D. Hanson, On the number of times an integer occurs as a
binomial coeﬃcient, Amer. Math. Monthly 81 (1974), no. 4, 256–261.

[2] R.C. Baker, G. Harman, and J. Pintz, The diﬀerence between consecutive primes, II, Proc.
London Math. Soc. (3) 83 (2001), no. 3, 532–562.

[3] D. Kane, New bounds on the number of representations of t as a binomial coeﬃcient, Integers
4 (2004), A7, 10 pp.

[4] D. Kane, Improved bounds on the number of ways of expressing t as a binomial coeﬃcient,
Integers 7 (2007), A53, 7 pp.

[5] D.A. Lind, The quadratic ﬁeld Q(
√5) and a certain Diophantine equation, Fibonacci Quart.
6 (1968), no. 3, 86–93.

[6] OEIS Foundation Inc. (2019), The On-Line Encyclopedia of Integer Sequences,
https://oeis.org/A003015.

[7] D. Singmaster, Research problems: How often does an integer occur as a binomial coeﬃcient?,
Amer. Math. Monthly 78 (1971), no. 4, 385–386.

[8] D. Singmaster, Repeated binomial coeﬃcients and Fibonacci numbers, Fibonacci Quart. 13
(1975), no. 4, 295–298.
