<!-- source: https://www.impan.pl/shop/en/publication/transaction/download/product/81923?download.pdf= | converted from PDF -->

ACTA ARITHMETICA
107.3 (2003)
 Visibility of lattice points

by

Yong-Gao Chen (Nanjing) and Lin-Feng Cheng (Xuzhou)

1. Introduction. Two integer points P (a1, . . . , ak) and Q(b1, . . . , bk)
are said to be visible to each other if either P = Q or there are no other
integer points on the line segment joining P and Q. It is not diﬃcult to
verify that if P ̸= Q, then P and Q are visible to each other if and only if
gcd(a1 − b1, . . . , ak − bk) = 1. We say that an integer point set A is visible
from an integer point set B if each point of A is visible from some point
of B.
For k ≥ 2, let

∆
k = {(x1, . . . , xk) : xi integers and 1 ≤ xi ≤ n (1 ≤ i ≤ n)}.

Deﬁne
 fk(n) = min{|S| : S ⊂ Zk, ∆k is visible from S},
Fk(n) = min{|S| : S ⊆ ∆k , ∆k is visible from S}.

It is clear that fk(n) ≤ Fk(n). Erd˝os, Gruber and Hammer [4] asked for
an explicit construction of S such that S ⊂ ∆2 , |S| = O(log n) and ∆2
is visible from S. A better construction of S was given by Adhikari and
Balasubramanian [2]. We have

F2(n) ≥ 1

2 log n
log log n , n ≥ n0, (Abbott [1])

F2(n) = O( log n log log log n
log log n
 )
, (Adhikari, Balasubramanian [2])

Fk(n) = O( log n
log log n
 )
, k ≥ 3, (Adhikari, Chen [3]).

2000 Mathematics Subject Classiﬁcation: 11H99, 11B75.
Supported by the National Natural Science Foundation of China, Grant No. 10171046
and the Teaching and Research Award Program for Outstanding Young Teachers in Nan-
jing Normal University.
 [203]

204 Y. G. Chen and L. F. Cheng

In fact, the method in Abbott [1] implies that

Fk(n) ≥ fk(n) ≥ 1
2 log n
log log n , n ≥ n0, for all k ≥ 2.

Thus, for k ≥ 3, the main orders of fk(n) and Fk(n) are log n/log log n. In
this note we are interested in the constant factors. Let

ζ(k) =
 ∞∑

m=1
 1
mk = ∏

p
 (
1 − 1
pk
 )
.

The following results are proved.

Theorem 1. For k ≥ 2 we have

fk(n) ≥ ζ(k) log n
log log n (1 + o(1)).

Theorem 2. For k ≥ 3 we have

Fk(n) ≤ ζ(k − 1) log n
log log n (1 + o(1)).

Remark. The ﬁrst author conjectures that

fk(n) = ζ(k) log n
log log n (1 + o(1)), Fk(n) = ζ(k) log n
log log n (1 + o(1)).

By an analogous argument to the proof of Theorem 2, we can prove that
the conjecture for k ≥ 3 follows from the conjecture that for every ﬁxed s,

max
s<m≤n ω((m − 1)(m − 2) . . . (m − s)) = (1 + o(1)) log n
log log n ,

and the conjecture for k = 2 follows from the conjecture that

max
sn<m≤n ω((m − 1)(m − 2) . . . (m − sn)) = (1 + o(1)) log n
log log n ,

where sn = [2 log n/log log n].

2. Proofs. Let p1, p2, . . . be all positive primes in increasing order, that
is, p1 = 2, p2 = 3, . . . As usual, we will use p to denote a prime. For two
points P and Q in Zk and an integer m, we say that P and Q are congruent
mod m if all coordinates are congruent mod m.

Lemma 1. Let B be a ﬁnite subset of Zk. Then there exist at least
|B|/pk points in B which are congruent mod p.

Proof. Lemma 1 follows from the fact that points in Zk mod p has pk

diﬀerent possible values.
 Visibility of lattice points 205

Proof of Theorem 1. Let 0 < ε < 1/8. We take an integer t such that

t∏

i=1
 (
1 − 1
pk
 ) ≤ ζ(k)−1(1 + ε).

For n ≥ n1(ε, k) there exists an integer r such that

ζ(k) log n

log log n (1 − 6ε) ≤ r ≤ ζ(k) log n
log log n (1 − 5ε), pkpk . . . pk | r.

Suppose that Q1, . . . , Qr are r distinct points in Zk. By Lemma 1 there
exists A1 ⊆ {Q1, . . . , Qr} such that |A1| = r/pk and the points in A1 are
congruent mod p1. Let B1 = {Q1, . . . , Qr} \ A1. Then |B1| = (1 − 1/pk)r is
divisible by pk. By Lemma 1 there exists A2 ⊆ B1 such that |A2| = |B1|/pk
and the points in A2 are congruent mod p2. Let B2 = B1 \ A2. Then |B2| =
(1 − 1/pk)(1 − 1/pk)r is divisible by pk. Similarly, we obtain A3, . . . , At and
B3, . . . , Bt such that |Ai| = |Bi−1|/pk, Bi = Bi−1 \ Ai and the points in Ai
are congruent mod pi for 3 ≤ i ≤ t. Then

|Bt| = (
1 − 1

pk
 )|Bt−1| = . . . = r
 t∏

i=1
 (
1 − 1

pk
 ) ≤ log n

log log n (1 − 4ε).

Hence, for n ≥ n2(ε, k),

(1) t + |Bt| ≤ log n
log log n (1 − 3ε).

Let s = t + |Bt|. Let Bt = At+1 ∪ . . . ∪ As with |Ai| = 1 and Ai ∩ Aj = ∅ for
t + 1 ≤ i, j ≤ s and i ̸= j. By the Chinese Remainder Theorem, there exists
a point Q in ∆kr+1)p1...ps which is diﬀerent from Q1, . . . , Qr and congruent
to the points of Ai mod pi for each i. For n ≥ n3(ε, k) by (1) we have

log((r + 1)p1 . . . ps) ≤ log(r + 1) + s log ps
≤ ε log n + (1 − 2ε) log n < log n.

Hence, Q ∈ ∆k and Q is invisible from any point of Q1, . . . , Qr. Therefore

fk(n) > r ≥ ζ(k) log n

log log n (1 − 6ε).

This completes the proof of Theorem 1.

Proof of Theorem 2. Let 0 < ε < 1/4. Let t be an integer with

2k−1 ∑

p>pt
 1
pk−1 < εζ(k − 1)−1.

For n ≥ n4(ε, k) there exists an integer r with

ζ(k − 1) log n
log log n 1 + 2ε
1 − ε ≤ rk−1 ≤ ζ(k − 1) log n
log log n 1 + 3ε
1 − ε , p1p2 . . . pt | r.

206 Y. G. Chen and L. F. Cheng

Let Gn = {(a1, . . . , ak−1, 1) : ai integers, 1 ≤ ai ≤ r (1 ≤ i ≤ k − 1)}

∪ {(2, 2, . . . , 2)}.

Given any point (x1, . . . , xk) ∈ ∆k . If xk = 1, then (x1, . . . , xk) is visible
from (2, 2, . . . , 2). Now we assume that xk > 1. We will show that there
exists at least one point (a1, . . . , ak−1, 1) ∈ Gn such that

(x1 − a1, . . . , xk−1 − ak−1, xk − 1) = 1.

In order to prove this, we use a simple sieving argument. Let q1, . . . , qm be
the prime divisors of xk − 1. We know that

m = ω(xk − 1) ≤ (1 + o(1)) log n/log log n.

We want to ﬁnd (a1, . . . , ak−1, 1) ∈ Gn so that no qi divides each xj −aj, 1 ≤
j ≤ k − 1.
For the primes qj that are among p1, . . . , pt we use the combinatorial
sieve. We ﬁnd that the number of remaining vectors is

rk−1 ∏(1 − p−(k−1)
i ) > ζ(k − 1)−1rk−1.

Each prime qj with pt < qj ≤ r excludes at most (1+[r/qj])k−1 < (2r/qj)k−1

vectors. The total number of these is

< (2r)k−1 ∑

qj >pt q−(k−1)
j < εζ(k − 1)−1rk−1.

Finally, a qj > r excludes at most one, altogether (1 + o(1)) log n/log log n
at most. Since

ζ(k − 1)−1rk−1 > (1 + ε) log n

log log n + εζ(k − 1)−1rk−1,

we are done.
Therefore

Fk(n) ≤ |Gn| + 1 ≤ rk−1 + 1 ≤ ζ(k − 1) 1 + 3ε
1 − ε log n
log log n + 1.

This completes the proof.

Acknowledgements. I am grateful to the referee for his/her sugges-
tions to shorten the proof of Theorem 2 and to add more remarks pertaining
to Theorem 2.
 References

[1] H. L. Abbott, Some results in Combinatorial Geometry, Discrete Math. 9 (1974),
199–204.
 Visibility of lattice points 207

[2] S. D. Adhikari and R. Balasubramanian, On a question regarding visibility of lattice
points, Mathematika 43 (1996), 155–158.
[3] S. D. Adhikari and Y.-G. Chen, On a question regarding visibility of lattice points,
II , Acta Arith. 89 (1999), 279–282.
[4] P. Erd˝os, P. M. Gruber and J. Hammer, Lattice Points, Pitman Monographs Surveys
Pure Appl. Math. 39, Wiley, New York, 1989.

Department of Mathematics
Nanjing Normal University
Nanjing 210097, China
E-mail: ygchen@pine.njnu.edu.cn
 Department of Mathematics
China University of Mining and Technology
Xuzhou 221008, China
E-mail: cumtclf@sina.com.cn

Received on 14.11.2001
and in revised form on 26.8.2002 (4145)
