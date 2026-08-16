<!-- source: https://arxiv.org/pdf/2011.06136 | converted from PDF -->

arXiv:2011.06136v2  [math.NT]  3 Oct 2023Large Zsigmondy Primes

¨Omer Avcı∗

October 4, 2023

Abstract

If a > b and n > 1 are positive integers and a and b are relatively
prime integers, then a large Zsigmondy prime for (a, b, n) is a prime
p such that p | an − bn but p ∤ am − bm for 1 ≤ m < n and either
p2 | an − bn or p > n + 1. We classify all the triples of integers (a, b, n)
for which no large Zsigmondy prime exists.

1 Introduction

Let a > b be relatively prime positive integers and n be a positive integer. A
Zsigmondy prime for (a, b, n) is deﬁned as a prime p such that p | a
n − b
n but
p ∤ a
m − b
m for 1 ≤ m < n. Zsigmondy’s Theorem asserts that Zsigmondy
primes exist for all triples (a, b, n) except when (a, b, n) = (2, 1, 6) or n = 2
and a + b = 2k for some positive integer k (see [1]). Zsigmondy’s Theorem
was independently, but later, discovered by Birkhoﬀ and Vandiver [2].

In [3], Feit deals with the special case of Zsigmondy’s Theorem when b = 1
and deﬁnes a large Zsigmondy prime for the pair (a, n) as a prime p such
that p | a
n −1 but p ∤ a
m −1 for 1 ≤ m < n and either p2 | a
n −1 or p > n+1.

In our paper, we present a generalised version of Feit’s results.

Theorem 1.1 If a > b are relatively prime positive integers and n is an
integer greater than 1, then there exists a large Zsigmondy prime for (a, b, n)
except the following cases.

∗Department of Mathematics, Bo˘gazi¸ci University, 34342, Bebek, Istanbul, Turkey

1

(i) n = 2 and a + b = 2s or a + b = 3 · 2s where s is a non-negative integer.

(ii) n = 4 and (a, b) is (2, 1) or (3, 1).

(iii) n = 6 and (a, b) is one of the following {(2, 1), (3, 1), (3, 2), (5, 4)}.

(iv) n ∈ {10, 12, 18} and (a, b) = (2, 1).

Artin’s results about orders of linear groups (see [4]) also inspired Feit’s work
about the existence of large Zsigmondy primes. The motivation for Feit’s
work comes from the theory of ﬁnite groups [5]. Feit proved the existence of
large Zsigmondy primes in all cases except for ﬁnitely many, as stated in [6],
for the special case a ⩾ 3. Later on, he came up with a simpler proof of his
result, which also includes the case where a = 2, as presented in [3]. Roitman
also provided a nice proof of Feit’s result in [7].
For relatively prime positive integers a > b, we can generalize the deﬁ-
nition of a large Zsigmondy prime as a prime p such that p | a
n − b
n, but
p ∤ a
m − b
m for 1 ≤ m < n and either p2 | a
n − b
n or p > n + 1. We show that
there exists a large Zsigmondy prime for (a, b, n) except in the cases presented
in Theorem 1.1. Our proof is inspired by the elegant proof of Zsigmondy’s
Theorem given by Yan Sheng in [8].

2 Preliminaries

Lemma 2.1 [3] For any positive integer n, where φ(n) denotes Euler’s to-
tient function, it holds that:
 φ(n) ⩾ 1
2 √n.

Lemma 2.2 (Lifting the Exponent Lemma - LTE) For a prime p and
a positive integer n, let vp(n) denote the exponent of p in the prime factori-
sation of n. Let x and y be integers such that x ≡ y ̸≡ 0 (mod p).

(1) If p ⩾ 3, then
 vp(x
n − yn) = vp(x − y) + vp(n).

2

(2) If p = 2, then

v2(x
n − yn) =
 {
v2(x
2 − y2) + v2(n) − 1, if n is even
v2(x − y), if n is odd.

Deﬁnition 2.3 (Cyclotomic Polynomials) For any positive integer n, the
n-th cyclotomic polynomial Φn(x) is given by:

Φn(x) = ∏

gcd(k,n)=1
1⩽k⩽n
 (x − e
2iπ k
n ).

It is known that Φn(x) is a monic polynomial with integer coeﬃcients.

Deﬁnition 2.4 There is a generalization of cyclotomic polynomials into two
variables: Φn(a, b) = b
φ(n)Φn(a
b
 )
.

We can also express Φn(a, b) as

Φn(a, b) = ∏

gcd(k,n)=1
1⩽k⩽n
 ( a − b e
2iπ k
n ).

It is clear that Φn(x, y) is a two variable polynomial with integer coeﬃcients.

Lemma 2.5 [8] Let n be a positive integer. Then,

x
n − 1 = ∏

d|n Φd(x).

Corollary 2.6 [8] Let a, b, n are positive integers. Then,

a
n − b
n = ∏

d|n Φd(a, b).

Lemma 2.7 [8] Let p be a prime, n ⩾ 3 be an integer and x > 0. Then,

(x − 1)φ(n) < Φn(x) < (x + 1)φ(n).

3

Corollary 2.8 Let a, b, n are positive integers and n ⩾ 3. Then,

(a − b)φ(n) < Φn(a, b) < (a + b)φ(n).

Lemma 2.9 [8] Let p be a prime, a and b be distinct positive integers, and
n be a positive integer. Then,

Φpn(a, b) =
 {
Φn(a
p, b
p) if p | n
Φn(ap,bp)
Φn(a,b) if p ∤ n

Corollary 2.10 [8] Let p be a prime, a and b be distinct positive integers,
and n = pβk for some positive integers β, k with p ∤ k. Then,

Φn(a, b) = Φpk(a
pβ−1, b
pβ−1) = Φk(a
pβ , b
pβ )
Φk(apβ−1, bpβ−1).

Lemma 2.11 [8] Let p be a prime, a and b be distinct positive integers not
divisible to p, and n be a positive integer. Let k be the smallest positive integer
satisfying p | a
k − b
k. Then,

vp(Φn(a, b)) =
 




vp(a
k − b
k) n = k,
1 n = pβk, β ⩾ 1,
0 otherwise.

Lemma 2.12 [8] Let a and b be distinct odd positive integer and n be a
positive integer. Then,

v2 (Φn(a, b)) =
 



v2(a − b) n = 1
v2(a + b) n = 2
1 n = 2β, β ⩾ 2
0 else.

3 Results on Zsigmondy Primes

Lemma 3.1 Let a > b be two relatively prime positive integers and n be a
positive integer, p be a prime divisor of Φn(a, b) and k be the smallest positive
integer satisfying p | a
k − b
k. Let gpf(n) denote the largest prime divisor of
n, then one of the following holds:
 4

(i) p = 2 and n = 2β for some β ⩾ 1.

(ii) p ≥ 3 and n = k thus p is a Zsigmondy prime for (a, b, n).

(iii) p = gpf(n) > 2 and n = pβk for some β ⩾ 1 and vp(Φn(a, b)) = 1.

Proof: If p = 2, by Lemma 2.12, it follows that n = 2β for some β ⩾ 1 . If
p > 2, according to Lemma 2.11, there are two possibilities. Either n = k or
n = pβk holds. When n = k, it implies that p ∤ a
m − b
m for all 1 ≤ m < n,
which means that p is a Zsigmondy prime for (a, b, n). Since k is deﬁned as
the smallest positive integer such that p|a
k − b
k, it is evident that k | p − 1
holds. Moreover, it is clear that any prime divisor of k must be smaller than
p. Consequently, when n = pβk, we can conclude that p = gpf(n) since no
prime divisor of n can be greater than p. Furthermore, according to Lemma
2.11, we have vp(Φn(a, b)) = 1 in the case where n = pβk.

Lemma 3.2 Let a and b be distinct, relatively prime positive integers and
n ⩾ 2 be an integer. If p is a Zsigmondy prime for (a, b, n) then p | Φn(a, b).

Proof: From Corollary 2.6 we have

a
n − b
n = ∏

d|n Φd(a, b).

Therefore, such p divides Φd(a, b) for some d | n. If d < n, then p | Φd(a, b),
which implies p|a
d − b
d. This contradicts with p being a Zsigmondy prime for
(a, b, n). We conclude that d = n, hence p | Φn(a, b).

Lemma 3.3 Let a > b be relatively prime positive integers, and n ⩾ 2 be
an integer. If q is a Zsigmondy prime for (a, b, n) but not a large Zsigmondy
prime for (a, b, n), then n = q − 1.

Proof: Since q is a Zsigmondy prime for (a, b, n), n | q − 1; but since q is not
large Zsigmondy prime for (a, b, n), q ⩽ n + 1. Therefore n = q − 1.

Lemma 3.4 Let a and b be distinct, relatively prime, positive integers, and
n ⩾ 3 be an integer. Then there is a large Zsigmondy prime for (a, b, n), if
(n + 1) gpf(n) < Φn(a, b).
 5

Proof: Let us analyze the proof in two cases.
If Φn(a, b) is even, then n = 2β for some β ≥ 2 and 4 ∤ Φn(a, b) from 2.12.
Since Φn(a, b) > 2(n + 1) > 2, it has at least one odd prime divisor. Let p
be the greatest prime divisor of Φn(a, b). Since p > 2 and p ∤ n, we obtain
n|p − 1 from 2.11. If p > n + 1, then p is a large Zsigmondy prime for (a, b, n).
If p = n + 1, then only odd prime divisor of Φn(a, b) is p. Since 4 ∤ Φn(a, b)
and Φn(a, b) > 2(n + 1) we conclude that p2|Φn(a, b), and therefore p is a
large Zsigmondy prime for (a, b, n).
If Φn(a, b) is odd, it must have an odd prime divisor. Let p be the greatest
prime divisor of Φn(a, b). From 2.11, we obtain n|p − 1 or p|n. If n|p − 1 and
p > n + 1 then p is a large Zsigmondy prime for (a, b, n). If p = n + 1 and
p2|Φn(a, b) then it is a large Zsigmondy prime for (a, b, n). If p = n + 1 and
p2 ∤ Φn(a, b), then Φn(a, b) must have another prime divisor q because of the
assumption Φn(a, b) > (n + 1) gpf(n). Since q < p, this implies that n ∤ q − 1,
therefore q is the greatest prime divisor of n because of 2.11, and furthermore
q2 ∤ Φn(a, b). Thus only prime divisors of Φn(a, b) are p and q. Also, their
squares does not divide Φn(a, b). Ultimately Φn(a, b) = pq must hold but it
contradicts with Φn(a, b) > (n + 1) gpf(n) since p = n + 1 and q = gpf(n).

Proof of Theorem 1.1
We begin by proving the existence of a large Zsigmondy prime for (a, b, n),
when n is not equal to any of the numbers {2, 4, 6, 10, 12, 18}. Consider pos-
itive integers a > b and n > 1 with gcd(a, b) = 1. Let’s assume that there
is no large Zsigmondy prime for (a, b, n). If there is no Zsigmondy prime
for (a, b, n), we can determine the possible values of (a, b, n) based on Zsig-
mondy’s theorem. We will speciﬁcally investigate the case where there is a
Zsigmondy prime for (a, b, n) but no large Zsigmondy prime for (a, b, n).
Let n ⩾ 3 and q be a Zsigmondy prime for (a, b, n) but q is not a large
Zsigmondy prime for (a, b, n); therefore, n = q − 1 and q2 ∤ a
n − b
n. From
Lemma 3.2 we know that it is necessary for q | Φn(a, b) to hold. From Lemma
3.1, Φn(a, b) can have at most one non-Zsigmondy prime divisor p with the
possibilities p = 2 or p = gpf(n). Now, we have three cases to consider:

(i) Φn(a, b) = 2q and n = 2β where β ⩾ 2. In this case we have q = 2β + 1
therefore it must be a Fermat prime so β = 2s for some s ⩾ 1. From
Corollary 2.10 we have

Φn(a, b) = Φ2(a
2β−1, b
2β−1) = a
2β−1 + b
2β−1 ⩾ 22β−1 + 1.

6

For β ⩾ 4 we have 22β−1 + 1 > 2(2β + 1) therefore Φn(a, b) > 2(n + 1) =
2q, leading to a contradiction with our assumption. We are left with
two possibilities: n = 4 or n = 8. However, if n = 8 then q = n + 1
cannot be a prime. Therefore, the only possibility in this case is n = 4.

(ii) Φn(a, b) = pq, where p = gpf(n) > 2, is the greatest prime divisor of
n. Then n = pβk where β is a positive integer and k is the smallest
positive integer satisfying p | a
k − b
k. Clearly, k | p − 1.
We can divide this case into two subcases.

(a) If β ⩾ 2, then by combining Corollary 2.10 and Corollary 2.8, we
can get:
 Φn(a, b) = Φpk(a
pβ−1, b
pβ−1) ⩾ (a
pβ−1 − b
pβ−1)Φ(pk).

Since a > b, we can derive the inequality,

(a
pβ−1−b
pβ−1)Φ(pk) ⩾ (2pβ−1−1)Φ(pk) ⩾ (2pβ−1−1)p−1 ⩾ (2p−1−1)pβ−1.

Since k < p we have,

Φn(a, b) = pq = p(pβk + 1) < pβ+2.

Since p ⩾ 3, we have 2p−1 − 1 ⩾ p, thus,

Φn(a, b) ≥ (2p−1 − 1)pβ−1 ≥ ppβ−1.

Therefore β + 2 > pβ−1 must hold, which is not possible when
β ⩾ 3. Therefore, β ̸= 2, then a large Zsigmondy prime exists for
(a, b, n) in this case. Let’s investigate the case β = 2. By substi-
tuting β = 2 into our previous inequalities, we obtain,

p4 = pβ+2 > Φn(a, b) ⩾ (2pβ−1 − 1)p−1 = (2p − 1)p−1 ⩾ (2p − 1)2.

It is not possible when p ≥ 5. Therefore, there exists a large Zsig-
mondy prime for (a, b, n) when p ≥ 5 in this case. So, in the second
case, if there is no large Zsigmondy prime for (a, b, n), then p = 3,
β = 2, and k = 1 or k = 2. Thus, the only exceptional values
are n = 18 and n = 9. If n = 9 then n + 1 is not a prime, and
q = n + 1 is not a Zsigmondy prime for (a, b, n). Therefore, the
only possibility in this case is n = 18. We will ﬁnd the pairs (a, b)
at the end of the proof.
 7

(b) If β = 1, then by combining Corollary 2.10 and Corollary 2.8, we
can obtain,

Φn(a, b) = Φpk(a, b) = Φk(a
p, b
p)
Φk(a, b) ⩾ (a
p − b
p

a + b
 )φ(k) ⩾ (2p − 1
3
 )φ(k).

In this case, Φn(a, b) = (pk + 1)p < p3 holds. Then either 2p−1
3 < p
or φ(k) < 3. Which means either p ⩽ 3 or k ⩽ 6. If p = 3 then
n = 6. If p > 3 then φ(k) ≤ 2 thus k ∈ {1, 2, 3, 4, 6}.
If φ(k) = 2 then k ∈ {3, 4, 6} and

p3 > Φn(a, b) ≥ (2p − 1
3
 )2

holds which is not possible when p ≥ 7. If p = 5 then k = 4 must
hold since k|p−1. But then n = 20 so q = n+1 is not a Zsigmondy
prime for (a, b, n).
If φ(k) = 1 then k ∈ {1, 2} and

p3 > Φn(a, b) ≥ 2p − 1
3

holds which is not possible when p ≥ 13. If k = 1 then n = p
holds. But then q = n + 1 can not be a prime number. If k = 2
then n = 2p holds. If p = 11 then q = 23 and Φn(a, b) = 253.
But this contradicts with the fact Φ10(a, b) ≥ 210−1
3 = 341. If p = 7
then n = 14 but then q = n + 1 is not a prime number. Then p = 5
and n = 10 must hold.
Ultimately only possible values are n = 6 and n = 10 in this case.
Again we will handle the determination of pairs (a, b) at the end
of the proof.

(iii) Φn(a, b) = q, where q = n + 1, is an odd prime number. So, n must be
even. From Corollary 2.8 and Corollary 2.10, we obtain,

Φn(a, b) = Φq−1(a, b) ⩾ Φ q−1
2 (a
2, b
2)

Φ2(a, b) ⩾ (a
2 − b
2)φ( q−1
2 )

a + b .

We can further reﬁne the inequality as follows:

q = Φn(a, b) ⩾ (a + b)φ( q−1
2 )−1 ⩾ 3φ( q−1
2 )−1.

8

We will show that, this inequality is satisﬁed only when q ⩽ 7. From

Lemma 2.1 we have φ(n) ⩾ 1
2 √n. If we put this into the previous
inequality, we get q ⩾ 3φ( q−1
2 )−1 ⩾ 3
 √q−1
2 −1.

This is only possible when q ⩽ 113. By putting this back into the
inequality we obtain 35 > q ≥ 3φ( q−1
2 )−1.

This holds only when φ( q−1
2 ) ⩽ 5, which is only possible if q − 1 has no
prime divisors greater than 5. By manually checking all the remaining
possibilities of q, we can see that

q ≥ 3φ( q−1
2 )−1

is satisﬁed only when q ≤ 13. If we look up all the cases, we get n =
2, 4, 6, 12, with only n = 12 being new.

Now we will determine all the triples (a, b, n) such that there is no large
Zsigmondy prime for (a, b, n). We will use the Lemma 3.1 and Lemma 3.4 to
analyze the cases.

(i) If n = 2, and there is no large Zsigmondy prime for (a, b, n), then no
prime greater than 3 can divide a
n − b
n furthermore 9 ∤ a
n − b
n. Then
a + b = 2s3t for non-negative integers s, t such that t = 0, 1. The case
t = 0 is also an exceptional case of Zsigmondy’s theorem.

(ii) If n = 4, then Φ4(a, b) = a
2 + b
2 ⩽ 10 must hold. Furthermore we have
a
2 + b
2 ∈ {5, 10}. We can easily check that only possible values for (a, b)
are (2, 1) and (3, 1).

(iii) If n = 6, then Φ6(a, b) = a
2 − ab + b
2 ⩽ 21 must hold. Furthermore
we have Φ6(a, b) ∈ {7, 21}. From this we get (3, 1), (3, 2), (5, 4) as suit-
able values of (a, b). Also we have one exceptional case of Zsigmondy’s
Theorem here when (a, b) = (2, 1).

(iv) If n = 10, then Φ10(a, b) = a
4 − a
3b + a
2b
2 − ab
2 + b
4 ⩽ 55 must hold.
Furthermore we have Φ10(a, b) ∈ {11, 55}. We can easily check that
only possible value for (a, b) is (2, 1).

9

(v) If n = 12, then Φ12(a, b) = a
4 − a
2b
2 + b
4 ⩽ 39 must hold. Furthermore
we have Φ12(a, b) ∈ {13, 39}. We can easily check that only possible
value for (a, b) is (2, 1).

(vi) If n = 18, then Φ6(a, b) = a
6 − a
3b
3 + b
6 ⩽ 57 must hold. Furthermore
we have Φ18(a, b) ∈ {19, 57}. We can easily check that only possible
value for (a, b) is (2, 1).

References

[1] K. Zsigmondy, Zur Theorie der Potenzreste, Monatsch. Math. Phys. 3
(1892), 265-284

[2] G. D. Birkhoﬀ and H. S. Vandiver, On the integral divisors of a
n − b
n,
Ann. of Math. (2) 5 (1904), 173-180.

[3] W. Feit, On large Zsigmondy primes, Proc. Amer. Math. Soc. 102 (1988),
29-36. MR 89b:11009

[4] E. Artin, The orders of the linear groups, Comm. Pure and Appl. Math.
8 (1955), 355-365. Reprinted in Collected Papers, (edited by S. Lang and
J. Tate), 387-397, Addison-Wesley, Reading, Mass., 1965. MR 17:12d

[5] W. Feit, G.M. Seitz, On ﬁnite rational groups and related topics, Illinois
J. Math. 33 (1988),

[6] W. Feit, Extensions of cuspidal characters of GLm(q) Publ. Math. De-
brecen 34 (1987), 273-297. MR 89d:20007 103-131. MR 90a:20016

[7] M. Roitman, “On Zsigmondy primes,” Proc. Am. Math. Soc., 125, No.
7, 1913-1919 (1997).

[8] Yan Sheng: An Elementary Proof of Zsigmondy’s Theorem,
https://angyansheng.github.io/blog/an-elementary-proof-of-zsigmondys-theorem

10
