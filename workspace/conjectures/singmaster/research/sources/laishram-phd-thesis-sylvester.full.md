<!-- source: https://www.isid.ac.in/~shanta/PhDThesis.pdf | converted from PDF -->

Some Topics in Number Theory
(Reﬁnements, Extensions and Generalisations of a Theorem
of Sylvester on the prime factors of a product of consecutive
integers)

A Thesis

Submitted to the
Tata Institute of Fundamental Research, Mumbai
for the degree of Doctor of Philosophy
in Mathematics

by

Shanta Laishram

School of Mathematics,
Tata Institute of Fundamental Research,
Mumbai, India

April, 2007

DECLARATION

This thesis is a presentation of my original research work. Wherever contributions of others
are involved, every eﬀort is made to indicate this clearly, with due reference to the literature, and
acknowledgement of collaborative research and discussions.
The work was done under the guidance of Professor T. N. Shorey, at the Tata Institute of
Fundamental Research, Mumbai.
 Shanta Laishram

In my capacity as supervisor of the candidate’s thesis, I certify that the above statements are
true to the best of my knowledge.

Professor T. N. Shorey
Date:
 Acknowledgements

It is my great pleasure to express my heart-felt gratitude to all those who helped and encouraged
me at various stages.
I am indebted to my advisor Professor T. N. Shorey for his invaluable guidance and constant
support. His concern and encouragement have always comforted me throughout.
I would like to thank Professors N. Saradha, E Ghate, C. S. Rajan and A. Sankaranarayanan
for introducing me to diﬀerent topics in Number Theory.
I would like to thank Professor Rob Tijdeman for helpful discussions and encouragement.
I would like to thank Professor Ravi Rao for being always available for any kind of help and
discussions. I would like to thank School of Mathematics staﬀ for helping me in administrative
matters and Dr Pablo and Mr Nandagopal for help in computer related matters.
My sincere thanks to Dr H Jayantakumar and Professors M Ranjit and M. B. Rege for their
constant support and encouragements throughout since my school days.
Though one should not thank friends, I would like to mention Ajay, Amala, Amit, Anand, Anoop,
Anupam, Apoorva, Ashutosh, Arati, Chandrakant, Deepankar, Deepshikha, Ig, Meera, Rabeya, Rama
Reddy, Ritumoni, Sarita, Shripad, Sriram, Umesh, Vaibhav, Vishal, Vivek and others with whom
I had spent a lot of time and for making my stay at TIFR lively and enjoyable one. I also really
enjoyed the company and time I spent with many other research scholars in school of mathematics
and other departments in TIFR.
I also cannot forget my friends outside TIFR whom I am in contact and whom I can always rely
upon. My school and college friends like Aken, Doren, Herachandra, Kebi, Marjit, Nirmal, Shekhar,
Shanta and Suhesh and other friends whom I met over the years like Binod, Birendra, Debbie,
Indrajit, Joykumar, Jugeshor, Kebi, Korou, Miranda, Nobin, Sarat, Shyam and Sanjoy. Also I have
been fortunate to meet quite a few frens while doing Mathematics like Aaloka, Anisa, Arindam,
Brundavan, Malapati, Purushottam, Rohit, Sanoli, Satadal, Sunayana, Swaralipy, Thyagaraju and
Vikram.
Finally, to my parents Mahajon and Sanahanbi, my grandmother Angou, my brothers and sister
and other relatives who are always there for me and whom I cannot thank enough!

List of Publications

This thesis is based on the results of my publications listed here. All the papers have been either
published or accepted for publication other than (ix) which has been submitted for publication. The
results of (ix) are stated in Chapter 2(Section 2.6) and proved in Chapter 12. All other chapters of
this thesis are independent of (ix).

(i) (with T. N. Shorey), Number of prime divisors in a product of consecutive integers, Acta
Arith. 113 (2004), 327-341.
(ii) (with T. N. Shorey), Number of prime divisors in a product of terms of an arithmetic
progression, Indag. Math., 15(4) (2004), 505-521.
(iii) An estimate for the length of an arithmetic progression the product of whose terms is almost
square, Pub. Math. Debrecen, 68 (2006), 451-475.
(iv) (with T. N. Shorey), Greatest prime factor of a product of consecutive integers, Acta Arith.,
120 (2005), 299-306.
(v) (with T. N. Shorey), The greatest prime divisor of a product of terms in an arithmetic
progression, Indag. Math., 17(3) (2006), 425-436.
(vi) (with T. N. Shorey), Grimm’s Conjecture on consecutive integers, Int. Jour. Number
Theory, 2 (2006), 207-211.
(vii) (with Hirata-Kohno, T. N. Shorey and R. Tijdeman), An extension of a theorem of Euler,
Acta Arith., accepted for publication.
(viii) (with T. N. Shorey), The equation n(n + d) · · · (n + (k − 1)d) = by2 with ω(d) ≤ 6 or
d ≤ 1010, Acta Arith., accepted for publication.
(ix) (with T. N. Shorey), Squares in products in arithmetic progression with at most two terms
omitted and common diﬀerence a prime power, submitted.

Contents

Introduction i

Chapter 1. A survey of reﬁnements and extensions of Sylvester’s theorem 1
1.1. Sylvester’s theorem 1
1.2. Improvements of ω(∆(n, k)) > π(k) 1
1.3. Results on reﬁnement of P (∆(n, k)) > k 5
1.4. Sharpenings of ω(∆(n, d, k)) ≥ πd(k) when d > 1 6
1.5. Results on reﬁnements of P (∆(n, d, k)) > k for d > 1 8

Chapter 2. A survey of results on squares in products of terms in an arithmetic progression 9
2.1. Introduction 9
2.2. Conjecture 2.1.2 with k ﬁxed 10
2.3. Equation (2.1.1) with k as a variable 10
2.4. Conjecture 2.1.2 with d ﬁxed 11
2.5. Equation (2.1.1) with ω(d) ﬁxed 11
2.6. Equation ∆(n, d, k) = by2 with ω(d) = 1 and at most two terms omitted 12

Chapter 3. Results from prime number theory 15
3.1. Estimates of some functions on primes and Stirling’s formula 15

Part 1. Proof of results on reﬁnements and extensions of Sylvester’s theorem 19

Chapter 4. Reﬁnement of Sylvester’s theorem on the number of prime divisors in a product of
consecutive integers: Proof of Theorems 1.2.1 and 1.2.4 21
4.1. An Alternative Formulation 21
4.2. Lemmas 22
4.3. Proof of Theorem 4.1.1 29

Chapter 5. Grimm’s Conjecture for consecutive integers:
Proof of Theorem 1.2.6 31
5.1. Introduction 31
5.2. Proof of Theorem 5.1.1 31

Chapter 6. Reﬁnement of Sylvester’s theorem on the greatest prime divisor of a product of
consecutive integers: Proof of Theorems 1.3.1, 1.3.3 and Corollary 1.3.2 35
6.1. Lemmas 35
6.2. Proof of Theorem 1.3.3 (a) 36
6.3. Proof of Theorem 1.3.3 (b) 37
6.4. Proof of Theorem 1.3.1 38
6.5. Proof of Corollary 1.3.2 38

Chapter 7. Reﬁnement of an analogue of Sylvester’s theorem for arithmetic progressions:
Proof of Theorem 1.4.1 39
7.1. Reﬁnement of fundamental inequality of Sylvester and Erd˝os 39
7.2. Lemmas for the proof of Theorem 1.4.1 (contd.) 41
7.3. Proof of Theorem 1.4.1 for k with 2k − 1 prime 42

a

7.4. Proof of Theorem 1.4.1 47
7.5. Proof of (1.4.8) 48

Chapter 8. Reﬁnement of Sylvester’s theorem on the greatest prime divisor of a product of
terms of an arithmetic progression: Proof of Theorem 1.5.1 49
8.1. Lemmas 49
8.2. The case k = 3 51
8.3. The case k = 4 51
8.4. The cases k = 6, 7, 9, 10 52
8.5. The cases k = 12, 15, 16 54
8.6. The case k ≥ 19 with 2k − 1 prime 54

Part 2. Proof of results on squares in products of terms in an arithmetic
progression 57

Chapter 9. Notation, Preliminaries and General Lemmas 59
9.1. Notations and Preliminaries 59
9.2. Some counting functions 61
9.3. Lemmas for the upper bound of n + (k − 1)d 63
9.4. Lemmas for the lower bound for n + (k − 1)d 73
9.5. Estimates on the general upper bound of ν(a) for a ∈ R 78

Chapter 10. Extensions of a result of Euler:
Proof of Theorems 2.1.1, 2.2.1 and 2.2.2 81
10.1. Introduction 81
10.2. The case k = 5 81
10.3. A Covering Lemma 81
10.4. Lemmas for the Proof of Theorem 10.1.1 (contd.) 83
10.5. Proof of Lemma 10.4.2 85
10.6. Proof of Lemma 10.4.3 93
10.7. Proof of Lemma 10.4.4 95
10.8. Proof of Theorem 10.1.1 97
10.9. Proof of Theorem 2.1.1 99

Chapter 11. Equation (2.1.1) with with ω(d) ≤ 6 or d ≤ 1010:
Proof of Theorems 2.3.1, 2.4.1, 2.5.1, 2.5.2, 2.5.3 101
11.1. Computational Lemmas 101
11.2. Further Lemmas 107
11.3. Proof of Theorem 2.5.2 114
11.4. Proof of Theorem 2.5.3 114
11.5. Proof of Theorem 2.3.1 116
11.6. Proof of Theorem 2.4.1 116
11.7. Proof of Theorem 2.5.1 117

Chapter 12. Equation (2.6.1) with t ≥ k − 2 and ω(d) = 1:
Proof of Theorem 2.6.2 119
12.1. Introduction 119
12.2. Lemmas 119
12.3. Equation (2.6.1) implies t − |R| ≤ 1 120
12.4. Proof of Theorem 2.6.2 121

Bibliography 125

Introduction

An old and well known theorem of Sylvester for consecutive integers [77] states that a product
of k consecutive integers each of which exceeds k is divisible by a prime greater than k.
In this thesis, we give reﬁnements, extensions, generalisations and applications of the above
theorem. First we give some notation which will be used throughout the thesis.
Let pi denote the i-th prime number. Thus p1 = 2, p2 = 3, . . .. We always write p for a prime
number. For an integer ν > 1, we denote by ω(ν) and P (ν) the number of distinct prime divisors
of ν and the greatest prime factor of ν, respectively. Further we put ω(1) = 0 and P (1) = 1. For
positive real number ν and positive integers l, a with gcd(l, a) = 1, we denote

π(ν) = ∑

p≤ν 1,

πa(ν) = ∑

p≤ν
gcd(p,a)=1
 1,

π(ν, a, l) = ∑

p≤ν
p≡l(mod a)

1.

We say that a number is eﬀectively computable if it can be explicitly determined in terms
of given parameters. We write computable number for an eﬀectively computable number. Let
d ≥ 1, k ≥ 2, n ≥ 1 and y ≥ 1 be integers with gcd(n, d) = 1. We denote by

∆ = ∆(n, d, k) = n(n + d) · · · (n + (k − 1)d)

and we write
 ∆(n, k) = ∆(n, 1, k).

In the above notation, Sylvester’s theorem can be stated as

P (∆(n, k)) > k if n > k.(1)

On the other hand, there are inﬁnitely many pairs (n, k) with n ≤ k such that P (∆) ≤ k. We
notice that ω(∆(n, k)) ≥ π(k) since k! divides ∆(n, k). The ﬁrst improvement in this direction is
the following statement equivalent to (1)

ω(∆(n, k)) > π(k) if n > k.(2)
 Let d > 1. Sylvester [77] proved that

P (∆) > k if n ≥ k + d.(3)

Langevin [38] improved (3) to
 P (∆) > k if n > k.

Finally Shorey and Tijdeman [75] proved that

P (∆) > k unless (n, d, k) = (2, 7, 3).(4)

We observe that it is necessary to exclude the triple (2, 7, 3) in the above result since P (2 · 9 · 16) = 3.
We give a brief description of the thesis. The thesis is broadly divided into two parts. In Chapter
1, we give a survey on reﬁnements and generalisations of Sylvester’s Theorem. These include the
statements of our new results and the proofs are given in Chapters 4 − 8 in the Part 1 of the thesis.

i

ii INTRODUCTION

In Chapter 2, we give a survey of results on the parity of power of primes greater than k dividing
∆ including our new results which are proved in the Chapters 9 − 12 in the Part 2 of the thesis.
For proving these results, we require certain estimates on π function and other functions involving
primes. In Chapter 3, we collect these results.
We begin with results stated in Chapter 1. First we consider results on the lower bound of
ω(∆(n, k)). Saradha and Shorey [61, Corollary 3] sharpened (2) by showing

ω(∆(n, k)) ≥ π(k) + [ 1
3 π(k)
] + 2 if n > k ≥ 3(5)

except when (n, k) belongs to an explicitly given ﬁnite set. This is best known for 3 ≤ k ≤ 18. We
improve 1
3 in (5) to 3
4 for k ≥ 19. We have

Theorem 1. (Laishram and Shorey [28])
Let k ≥ 3 and n > k. Then ω(∆(n, k)) ≥ π(k) + [ 3
4 π(k)] − 1 except when (n, k) belongs to an
explicitly given ﬁnite set.

A more precise statement including the exceptional set is given in Theorem 1.2.1 and a proof is
given in Section 4.1. We observe that ω(∆(k + 1, k)) = π(2k) and therefore, 3
4 in Theorem 1 cannot
be replaced by a number greater than 1. We refer to Theorem 1.2.4 and Corollary 1.2.5 for results
in this regard.
An open conjecture of Grimm [20] states that if n, n+1, · · · , n+k −1 are all composite numbers,
then there are distinct primes pij such that pij |(n + j) for 0 ≤ j < k. Erd˝os and Selfridge (see [48])
showed that Grimm’s Conjecture implies that there is a always a prime between two consecutive
squares. The latter result is out of bounds even after assuming Riemann hypothesis. Thus a proof
of Grimm’s Conjecture is very diﬃcult. The best known result on Grimm’s Conjecture is due to
Ramachandra, Shorey and Tijdeman [52]. Grimm’s Conjecture implies that if n, n + 1, · · · , n + k − 1
are all composite, then ω(∆(n, k)) ≥ k which is also open. In Chapter 5, we conﬁrm Grimm’s
Conjecture for n ≤ 1.9 × 1010 and for all k and as a consequence, we have

Theorem 2. (Laishram and Shorey, [31])
Assume that n, · · · , n + k − 1 are all composite and n ≤ 1.9 × 1010. Then ω(∆(n, k)) ≥ k.

The next result is on a lower bound for P (∆(n, k)).

Theorem 3. (Laishram and Shorey [30])
We have
 P (∆(n, k)) > 1.95k for n > k > 2

unless (n, k) belongs to an explicitly given ﬁnite set.

We observe from P (∆(k + 1, k)) ≤ 2k that 1.95 in Theorem 3 cannot be replaced by 2. Section
1.3 contains a more precise statement with an explicit list of the exceptions and some further results
viz., Theorems 1.3.1, 1.3.3 and Corollary 1.3.2. A proof of these results are given in Chapter 6.
Theorem 3 has been applied by Filaseta, Finch and Leidy [18] to prove irreducibility results for
certain Generalised Laguerre polynominals over rationals. We refer to Section 1.3 for results in this
regard. Now we turn to d > 1. We have the following result on ω(∆).

Theorem 4. (Laishram and Shorey [29])
Let d > 1. Then
 ω(∆(n, d, k)) ≥ π(2k) − 1

except when (n, d, k) = (1, 3, 10).

The above result is best possible for d = 2 since ω(1 · 3 · · · (2k − 1)) = π(2k) − 1. Theorem 4
solves a conjecture of Moree [43]. We refer to Section 1.4 on some more general results, particularly
Theorem 1.4.1 from where Theorem 4 follows. We give a proof of Theorem 1.4.1 in Section 7.4.
On a lower bound for P (∆), we have the following result.

INTRODUCTION iii

Theorem 5. (Laishram and Shorey [32])
Let d > 2 and k ≥ 3. Then
 P (∆(n, d, k)) > 2k

unless (n, d, k) is given by given by an explicit ﬁnite set.

The case d = 2 for the inequality of Theorem 5 can be reduced to that of d = 1. A more precise
statement with an explicit description of the exceptions is given in Theorem 1.5.1 and a proof is
given in Chapter 8. The assertions of Theorem 1, 3 and 5 are not valid for the exceptions and
therefore, it is necessary to exclude them.
Now we turn to Chapter 2 where we discuss the parity of power of primes greater than k dividing
∆(n, d, k). For this, we consider the equation

∆(n, d, k) = by2.(6)

with P (b) ≤ k. In Chapter 9, we state the preliminaries and the general Lemmas for the proofs of
the results stated in Chapter 2.
Let d = 1. It is a consequence of some old diophantine results that (6) with k = 3 is possible
only when n = 1, 2, 48. Let k ≥ 4. Erd˝os [11] and Rigge [55], independently, proved that product
of two or more consecutive positive integers is never a square. More generally, Erd˝os and Selfridge
[13] proved that (6) with P (b) < k does not hold under the necessary assumption that the left hand
side of (6) is divisible by a prime greater than or equal to k. The assumption P (b) < k has been
relaxed to P (b) ≤ k by Saradha [60] again under the necessary assumption that the left hand side
of (6) is divisible by a prime exceeding k. We refer to Section 2.1 for details.
Therefore we suppose that d > 1. Let k = 3. There are inﬁnitely many three squares in
arithmetic progression and hence (6) has inﬁnitely many solutions. Therefore we assume from now
onwards that k ≥ 4. Fermat (see Mordell [42, p.21]) showed that there are no four squares in an
arithmetic progression. Euler ([15], cf. [42, p.21-22], [43]) proved a more general result that a
product of four terms in arithmetic progression can never be a square. In Section 10.9, we prove the
following extension of Euler’s result.

Theorem 6. (Hirata-Kohno, Laishram, Shorey and Tijdeman [25])
Equation (6) with 4 ≤ k ≤ 109 and b = 1 is not possible.

The case k = 5 is due to Obl´ath [50]. Independently, Bennett, Bruin, Gy˝ory and Hajdu [1]
proved Theorem 6 with 6 ≤ k ≤ 11. A general conjecture states that ∆ is divisible by a prime > k
to an odd power unless k = 4, b = 6. In other words,

Conjecture 1. Equation (6) with P (b) ≤ k implies that k = 4, b = 6.

A weaker version of Conjecture 1 is the following conjecture due to Erd˝os.

Conjecture 2. Equation (6) with P (b) ≤ k implies k is bounded by a computable absolute
constant.

In Chapter 2, we give a survey of results on Conjectures 1 and 2.
We now consider Conjecture 1 with k ﬁxed. Equation (6) with k = 4 and b = 6 has inﬁnitely
many solutions. On the other hand, (6) with k = 4 and b ̸= 6 does not hold. Therefore we consider
(6) with k ≥ 5. We write
 n + id = aix
2
i for 0 ≤ i < k(7)

where ai are squarefree integers such that P (ai) ≤ max(P (b), k − 1) and xi are positive integers.
Every solution to (6) yields a k-tuple (a0, a1, . . . , ak−1). We re-write (6) as

m(m − d) · · · (m − (k − 1)d) = by2, m = n + (k − 1)d.(8)

The equation (8) is called the mirror image of (6). The corresponding k-tuple (ak−1, ak−2, . . . , a0)
is called the mirror image of (a0, a1, . . . , ak−1).
Let P (b) < k. In Chapter 10 (see Section 10.1), we prove the following result.

iv INTRODUCTION

Theorem 7. (Hirata-Kohno, Laishram, Shorey and Tijdeman [25])
Equation (6) with P (b) < k and 5 ≤ k ≤ 100 implies that (a0, a1, . . . , ak−1) is among the
following tuples or their mirror images.

k = 8 : (2, 3, 1, 5, 6, 7, 2, 1), (3, 1, 5, 6, 7, 2, 1, 10);

k = 9 : (2, 3, 1, 5, 6, 7, 2, 1, 10);

k = 14 : (3, 1, 5, 6, 7, 2, 1, 10, 11, 3, 13, 14, 15, 1);

k = 24 : (5, 6, 7, 2, 1, 10, 11, 3, 13, 14, 15, 1, 17, 2, 19, 5, 21, 22, 23, 6, 1, 26, 3, 7).

(9)
 Theorem 7 with k = 5 is due to Mukhopadhyay and Shorey [45]. A proof is given in Section
10.2. Theorem 7 with k = 6 is due to Bennett, Bruin, Gy˝ory and Hajdu [1]. They also showed,
independently, that (6) with 7 ≤ k ≤ 11 and P (b) ≤ 5 is not possible.
Let P (b) = k. Then the case k = 5 and P (b) = k in (6) is open. For k ≥ 7, we prove the
following result in Chapter 10 (see Section 10.1).

Theorem 8. (Hirata-Kohno, Laishram, Shorey and Tijdeman [25])
Equation (6) with P (b) = k and 7 ≤ k ≤ 100 implies that (a0, a1, . . . , ak−1) is among the
following tuples or their mirror images.

k = 7 : (2, 3, 1, 5, 6, 7, 2), (3, 1, 5, 6, 7, 2, 1), (1, 5, 6, 7, 2, 1, 10);

k = 13 : (3, 1, 5, 6, 7, 2, 1, 10, 11, 3, 13, 14, 15),

(1, 5, 6, 7, 2, 1, 10, 11, 3, 13, 14, 15, 1);

k = 19 : (1, 5, 6, 7, 2, 1, 10, 11, 3, 13, 14, 15, 1, 17, 2, 19, 5, 21, 22);

k = 23 : (5, 6, 7, 2, 1, 10, 11, 3, 13, 14, 15, 1, 17, 2, 19, 5, 21, 22, 23, 6, 1, 26, 3),

(6, 7, 2, 1, 10, 11, 3, 13, 14, 15, 1, 17, 2, 19, 5, 21, 22, 23, 6, 1, 26, 3, 7).

(10)
Now we turn to (6) with k as a variable. When d is ﬁxed, Marszalek [40] conﬁrmed Conjecture
2 by showing that k is bounded by an explicit constant depending only on d. This was reﬁned by
Shorey and Tijdeman [76] when ω(d) is ﬁxed. They showed that (6) implies that k is bounded by
a computable number depending only on ω(d) conﬁrming Conjecture 2 when ω(d) is ﬁxed. In fact
they showed that (6) implies
 2ω(d) > c1 k
log k

which gives
 d > kc2 log log k(11)

where c1 > 0 and c2 > 0 are absolute constants. Laishram [26] gave an explicit version of this result
by showing
 k <
 {
2.25ω(d)4
ω(d) if d is even
11ω(d)4
ω(d) if d is odd

for ω(d) ≥ 12 whenever (6) holds. Further Laishram and Shorey [33] improved it to

Theorem 9. (Laishram and Shorey [33])
Equation (6) implies that
 k < 2ω(d)2
ω(d).

A proof of Theorem 9 is given in Section 11.5.
Let d be ﬁxed. We consider Conjecture 1. Saradha and Shorey [63] solved (6) completely for
d ≤ 104 and k ≥ 4, see Section 2.4 for earlier results. The following result conﬁrms Conjecture 1 for
d ≤ 1010, k ≥ 6 and sharpens (11).
 INTRODUCTION v

Theorem 10. (Laishram and Shorey [33])
Equation (6) with k ≥ 6 implies that

d > max(1010, klog log k).

We give a proof of this theorem in Section 11.6.
Now we turn to Conjecture 1 with ω(d) ﬁxed. Let b = 1. Saradha and Shorey [63] proved that
(6) with ω(d) = 1 does not hold. In fact they proved it without the condition gcd(n, d) = 1. Thus a
product of four or more terms in an arithmetic progression with common diﬀerence a prime power
can never be a square. We extend this to ω(d) = 2 in the following result.

Theorem 11. (Laishram and Shorey [33])
A product of eight or more terms in arithmetic progression with common diﬀerence d satisfying
ω(d) = 2 is never a square.

A proof of Theorem 11 is given in Section 11.7. Further we solve (6) with ω(d) ≤ 5 and b = 1
completely. We have

Theorem 12. (Laishram and Shorey [33])
Equation (6) with b = 1 and ω(d) ≤ 5 does not hold.

A proof of this result is given in Section 10.3. It contains the case ω(d) = 1 already proved by
Saradha and Shorey [63].
Let P (b) ≤ k. As stated earlier, equation (6) with k = 6 is not possible by Bennett, Bruin,
Gy˝ory and Hajdu [1]. Also (6) with P (b) < k does not hold by Mukhopadhyay and Shorey [45] for
k = 5 and Hirata-Kohno, Laishram, Shorey and Tijdeman [25] for k = 7. We have no results on (6)
with k ∈ {5, 7} and P (b) = k. Therefore we assume k ≥ 8 in the next result. Let S1 be the set of
tuples (a0, . . . , ak−1) given by

k = 8 : (2, 3, 1, 5, 6, 7, 2, 1), (3, 1, 5, 6, 7, 2, 1, 10);

k = 9 : (2, 3, 1, 5, 6, 7, 2, 1, 10);

k = 13 : (3, 1, 5, 6, 7, 2, 1, 10, 11, 3, 13, 14, 15), (1, 5, 6, 7, 2, 1, 10, 11, 3, 13, 14, 15, 1)

and their mirror images. Further S2 be the set of tuples (a0, a1, . . . , ak−1) given by

k = 14 : (3, 1, 5, 6, 7, 2, 1, 10, 11, 3, 13, 14, 15, 1);

k = 19 : (1, 5, 6, 7, 2, 1, 10, 11, 3, 13, 14, 15, 1, 17, 2, 19, 5, 21, 22);

k = 23 : (5, 6, 7, 2, 1, 10, 11, 3, 13, 14, 15, 1, 17, 2, 19, 5, 21, 22, 23, 6, 1, 26, 3),

(6, 7, 2, 1, 10, 11, 3, 13, 14, 15, 1, 17, 2, 19, 5, 21, 22, 23, 6, 1, 26, 3, 7);

k = 24 : (5, 6, 7, 2, 1, 10, 11, 3, 13, 14, 15, 1, 17, 2, 19, 5, 21, 22, 23, 6, 1, 26, 3, 7)

and their mirror images. We have

Theorem 13. (Laishram and Shorey [33])
(a) Equation (6) with k ≥ 8 and ω(d) ≤ 4 implies that either ω(d) = 2, k = 8, (a0, a1, . . . , a7) ∈
{(3, 1, 5, 6, 7, 2, 1, 10), (10, 1, 2, 7, 6, 5, 1, 3)} or ω(d) = 3, (a0, a1, . . . , ak−1) ∈ S1 is given by an explicit
set of tuples or ω(d) = 4, (a0, a1, . . . , ak−1) ∈ S1 ∪ S2.
(b) Equation (6) with ω(d) ∈ {5, 6} and d even does not hold.

A proof of Theorem 13 is given in Section 11.4.
We now consider an equation more general than (6) when ω(d) = 1. Let k ≥ 5, t ≥ k − 2 and
γ1 < γ2 < · · · < γt be integers with 0 ≤ γi < k for 1 ≤ i ≤ t. Thus t ∈ {k, k − 1, k − 2}, γt ≥ k − 3
and γi = i − 1 for 1 ≤ i ≤ t if t = k. We put ψ = k − t. Let b be a positive squarefree integer and
we shall always assume, unless otherwise speciﬁed, that P (b) ≤ k. We consider the equation

(12) (n + γ1d) · · · (n + γtd) = by2

vi INTRODUCTION

in positive integers n, d, k, b, y, t where n and d are not necessarily relatively prime. Thus n and d
need not be relatively prime in Theorem 14 but we always assume that d ∤ n otherwise (12) has
inﬁnitely many solutions. When ψ = 0, then (12) is the same as (6). Therefore we consider ψ = 1, 2.
Let ψ = 1. We may assume that γ1 = 0 and γt = k − 1 otherwise this is the case ψ = 0. It has
been shown in [61] that 6!
5 = (12)2, 10!
7 = (720)2

are the only squares that are products of k−1 distinct integers out of k consecutive integers conﬁrming
a conjecture of Erd˝os and Selfridge [13]. This corresponds to the case b = 1 and d = 1 in (12). In
general, it has been proved in [61] that (12) with d = 1 and k ≥ 4 implies that (b, k, n) = (2, 4, 24)
under the necessary assumption that the left hand side of (12) is divisible by a prime > k. Further
it has been shown in [63, Theorem 4] and [46] that (6) with d > 1, gcd(n, d) = 1, ω(d) = 1 and
P (b) < k implies that k ≤ 8.
Let ψ = 2. Let d = 1. Then it has been shown by Mukhopadhyay and Shorey [47, Corollary 3]
that a product of k − 2 distinct terms out of k consecutive positive integers is a square only if it is
given by an explicitly given ﬁnite set, see Section 2.6 for a more precise statement. For the general
case, it follows from [47, Theorem 2] that (12) with k ≥ 6 is not valid unless k = 6 and n = 45, 240
whenever the left hand side of (12) is divisible by a prime > k. We extend it to k ≥ 5 in Theorem
2.6.1. In Section 12.4, we prove the following result for ω(d) = 1.

Theorem 14. (Laishram and Shorey [34])
Let ψ = 2, k ≥ 15 and d ∤ n. Assume that P (b) < k if k = 17, 19. Then (12) with ω(d) = 1 does
not hold.

As an immediate consequence of Theorem 14, we see that (2.1.1) with ω(d) = 1, ψ = 0, d ∤
n, k ≥ 15, P (b) ≤ pπ(k)+1 if k = 17, 19 and P (b) ≤ pπ(k)+2 if k > 19 does not hold.

CHAPTER 1

A survey of reﬁnements and extensions of Sylvester’s
theorem

1.1. Sylvester’s theorem

Let n, d and k ≥ 2 be positive integers such that gcd(n, d) = 1. For a pair (n, k) and a
positive integer h, we write [n, k, h] for the set of all pairs (n, k), · · · , (n + h − 1, k) and we set
[n, k] = [n, k, 1] = {(n, k)}.
Let W (∆) denote the number of terms in ∆ divisible by a prime > k. We observe that every
prime exceeding k divides at most one term of ∆. On the other hand, a term may be divisible by
more than one prime exceeding k. Therefore we have

W (∆) ≤ ω(∆) − πd(k).(1.1.1)

If max(n, d) ≤ k, we see that n + (k − 1)d ≤ k2 and therefore no term of ∆ is divisible by more than
one prime exceeding k. Thus
 W (∆) = ω(∆) − πd(k) if max(n, d) ≤ k.(1.1.2)

We are interested in ﬁnding lower bounds for P (∆), ω(∆) and W (∆). The ﬁrst result in this
direction is due to Sylvester [77] who proved that

P (∆) > k if n ≥ d + k.(1.1.3)

This immediately gives
 ω(∆) > πd(k) if n ≥ d + k.(1.1.4)

We give a survey of several results in this direction. The proofs depend on certain estimates from
prime number theory stated in Chaper 2.

1.2. Improvements of ω(∆(n, k)) > π(k)

Let d = 1. Let k = 2 and n > 2. We see that ω(n(n + 1)) ̸= 1 since gcd(n, n + 1) = 1. Thus
ω(n(n + 1)) ≥ 2. Suppose ω(n(n + 1)) = 2. Then both n and n + 1 are prime powers. If either n or
n + 1 is a prime, then n + 1 or n is a power of 2, respectively. A prime of the form 2
2m + 1 is called
a Fermat prime and a prime of the form 2m − 1 is called a Mersenne prime. Thus we see that either
n is a Mersenne prime or n + 1 is a Fermat prime. Now assume that n = pα, n + 1 = qβ where p, q
are distinct primes and α > 1, β > 1. Thus qβ − pα = 1 which is Catalan equation. In 1844, Catalan
[2] conjectured that 8 and 9 are the only perfect powers that diﬀer by 1. Tijdeman [78] proved in
1976 that there are only ﬁnitely many perfect powers that diﬀer by 1. Catalan’s conjecture has been
conﬁrmed recently by Mih˘ailescu [41]. Thus n = 8 is the only other n for which ω(n(n + 1)) = 2.
For all other n, we have ω(n(n + 1)) ≥ 3.
We assume that k ≥ 3 from now onwards in this section. We observe that

ω(∆(n, k)) = π(2k) if n = k + 1.(1.2.1)

If k + 1 is prime and 2k + 1 is composite, then we observe from (1.2.1) by writing

∆(k + 2, k) = ∆(k + 1, k) 2k + 1
k + 1

2 INTRODUCTION

that
 ω(∆(k + 2, k)) = π(2k) − 1.(1.2.2)

Let k + 1 be a prime of the form 3r + 2. Then 2k + 1 = 3(2r + 1) is composite. Since there are
inﬁnitely many primes of the form 3r + 2, we see that there are inﬁnitely many k for which k + 1 is
prime and 2k + 1 is composite. Therefore (1.2.2) is valid for inﬁnitely many k. Thus an inequality
sharper than ω(∆(n, k)) ≥ π(2k) − 1 for n > k is not valid.
Saradha and Shorey [61, Corollary 3] extended the proof of Erd˝os [10] for (1.1.3) to sharpen
(1.1.4) and gave explicit bound of ω(∆(n, k)) as

ω(∆(n, k)) ≥ π(k) + [ 1
3 π(k)
] + 2 if n > k(1.2.3)

unless (n, k) ∈ S1 where S1 is the union of sets





[4, 3], [6, 3, 3], [16, 3], [6, 4], [6, 5, 4], [12, 5], [14, 5, 3], [23, 5, 2],
[7, 6, 2], [15, 6], [8, 7, 3], [12, 7], [14, 7, 2], [24, 7], [9, 8], [14, 8],
[14, 13, 3], [18, 13], [20, 13, 2], [24, 13], [15, 14], [20, 14], [20, 17].
(1.2.4)

Laishram and Shorey [28] improved 1
3 in (1.2.3) to 3
4 . Deﬁne

δ(k) =
 




2 if 3 ≤ k ≤ 6
1 if 7 ≤ k ≤ 16
0 otherwise

so that [ 3
4 π(k)
] − 1 + δ(k) ≥ [ 1
3 π(k)
] + 2.

We have

Theorem 1.2.1. (Laishram and Shorey, [28])
Let n > k. Then
 ω(∆(n, k)) ≥ π(k) + [ 3
4 π(k)
] − 1 + δ(k)(1.2.5)

unless (n, k) ∈ S1 ∪ S2
where S1 is given by (1.2.4) and S2 is the union of sets





[20, 19, 3], [24, 19], [21, 20], [48, 47, 3], [54, 47], [49, 48], [74, 71, 2], [74, 72],
[74, 73, 3], [84, 73], [75, 74], [84, 79], [84, 83], [90, 83], [108, 83], [110, 83],
[90, 89], [102, 89], [104, 89], [108, 103], [110, 103, 2], [114, 103, 2], [110, 104],
[114, 104], [108, 107, 12], [109, 108, 10], [110, 109, 9], [111, 110, 7], [112, 111, 5],
[113, 112, 3], [114, 113, 7], [138, 113], [140, 113, 2], [115, 114, 5], [140, 114],
[116, 115, 3], [117, 116], [174, 173], [198, 181], [200, 181, 2], [200, 182],
[200, 193, 2], [200, 194], [200, 197], [200, 199, 3], [201, 200], [282, 271, 5],
[282, 272], [284, 272, 2], [284, 273], [278, 277, 3], [282, 277, 5], [279, 278],
[282, 278, 4], [282, 279, 3], [282, 280], [282, 281, 7], [283, 282, 5],
[284, 283, 5], [294, 283], [285, 284, 3], [286, 285], [294, 293].

(1.2.6)

We note here that the right hand sides of (1.2.3) and (1.2.5) are identical for 3 ≤ k ≤ 18.
Theorem 1.2.1 is an improvement of (1.2.3) for k ≥ 19. Therefore we shall prove Theorem 1.2.1 for
k ≥ 19. The proof of this theorem uses sharp bounds of π function due to Dusart given by Lemma
3.1.2. We derive the following two results from Theorem 1.2.1. We check that the exceptions in
Theorem 1.2.1 satisfy ω(∆(n, k)) ≥ π(2k) − 1. Hence Theorem 1.2.1 gives

1.2. IMPROVEMENTS OF ω(∆(n, k)) > π(k) 3

Corollary 1.2.2. Let n > k. Then

ω(∆(n, k)) ≥ min (π(k) + [ 3
4 π(k)
] − 1 + δ(k), π(2k) − 1) .(1.2.7)

Further all the exceptions in Theorem 1.2.1 except (n, k) ∈ {(114, 109), (114, 113)} satisfy
ω(∆(n, k)) ≥ π(k) + [ 2
3 π(k)
] − 1. Thus we obtain the following result from Theorem 1.2.1.

Corollary 1.2.3. Let n > k. Then

ω(∆(n, k)) ≥ π(k) + [ 2
3 π(k)
] − 1(1.2.8)

unless
 (n, k) ∈ {(114, 109), (114, 113)}.(1.2.9)

The constant 3
4 in Theorem 1.2.1 can be replaced by a number close to 1 if n > 17
12 k.

Theorem 1.2.4. (Laishram and Shorey, [28])
Let (n, k) ̸= (6, 4). Then we have

ω(∆(n, k)) ≥ π(2k) if n > 17
12 k.(1.2.10)

The inequality (1.2.10) is an improvement of (1.2.3) for k ≥ 10. Therefore we shall prove
Theorem 1.2.4 for k ≥ 10. We observe that 17
12 k in Theorem 1.2.4 is optimal since ω(∆(34, 24)) =
π(48) − 1. Also the assumption (n, k) ̸= (6, 4) is necessary since ω(∆(6, 4)) = π(8) − 1. We recall
that there are inﬁnitely many pairs (n, k) = (k + 2, k) satisfying (1.2.2). Thus there are inﬁnitely
many pairs (n, k) with n ≤ 17
12 k such that ω(∆(n, k)) < π(2k). Let n = k + r with 0 < r ≤ k. We
observe that every prime p with k ≤ n − 1 < p ≤ n + k − 1 is a term of ∆(n, k). Since k > n−1
2 , we
also see that 2p is a term in ∆(n, k) for every prime p with k < p ≤ n+k−1
2 . Further all primes ≤ k
divide ∆(n, k). Thus

ω(∆(n, k)) = π(2k + r − 1) − π(k + r − 1) + π(k + r − 1
2 ) = π(2k) + F (k, r)

where
 F (k, r) = π(2k + r − 1) − π(2k) − (π(k + r − 1) − π(k + r − 1
2 )
) .

We use the above formula for ﬁnding some pairs (n, k) as given below when k < 5000 and k < n ≤ 2k
for which ω(∆(n, k)) < π(2k):

ω(∆(n, k)) = π(2k) − 1 if (n, k) = (6, 4), (34, 24), (33, 25), (80, 57)

ω(∆(n, k)) = π(2k) − 2 if (n, k) = (74, 57), (284, 252), (3943, 3880)

ω(∆(n, k)) = π(2k) − 3 if (n, k) = (3936, 3879), (3924, 3880), (3939, 3880)

ω(∆(n, k)) = π(2k) − 4 if (n, k) = (1304, 1239), (1308, 1241), (3932, 3879)

ω(∆(n, k)) = π(2k) − 5 if (n, k) = (3932, 3880), (3932, 3881), (3932, 3882).

It is also possible to replace 3
4 in Theorem 1.2.1 by a number close to 1 if n > k and k is
suﬃciently large. Let k < n < 17
12 k. Then

ω(∆(n, k)) ≥ π(n + k − 1) − π(n − 1) + π(k).

4 INTRODUCTION

Let ϵ > 0 and k ≥ k0 where k0 exceeds a suﬃciently large number depending only on ϵ. Using the
estimates (i) and (ii) of Lemma 3.1.2, we get

π(n + k − 1) − π(n − 1) ≥ n + k − 1
log(n + k − 1) − 1 − n
log n − 1.2762n
log2 n

≥ n + k − 1
log n − n
log n − 1.2762n
log2 n

≥ k − 1
log n − 1.2762k
log2 k
≥ (1 − ϵ)π(k).

Thus ω(∆(n, k)) ≥ (2 − ϵ)π(k) for k < n < 17
12 k which we combine with Theorem 1.2.4 to conclude
the following result.

Corollary 1.2.5. Let ϵ > 0 and n > k. Then there exists a computable number k0 depending
only on ϵ such that for k ≥ k0, we have

ω(∆(n, k)) ≥ (2 − ϵ)π(k).(1.2.11)

Proofs of Theorems 1.2.1 and 1.2.4 are given in Chapter 4, see Section 4.1. We end this section
with a conjecture of Grimm [20]:
Suppose n, n + 1, · · · , n + k − 1 are all composite numbers, then there are distinct primes pij
such that pij |(n + j) for 0 ≤ j < k.
This conjecture is open. The conjecture implies that if n, n + 1, · · · , n + k − 1 are all composite,
then ω(∆(n, k)) ≥ k which is also open. In Chapter 5, we conﬁrm Grimm’s Conjecture for n ≤
1.9 × 1010 and for all k. Let N0 = 8.5 × 108. We prove

Theorem 1.2.6. (Laishram and Shorey, [31])
Grimm’s Conjecture holds for n ≤ pN0 and for all k.

We observe that pN0 = 19236701629 > 1.9 × 1010. As a consequence of Theorem 1.2.6, we have

Corollary 1.2.7. Assume that n, n + 1, · · · , n + k − 1 are all composite and n ≤ pN0. Then

ω(∆(n, k)) ≥ k.(1.2.12)

Let g(n) be the largest integer such that there exist distinct prime numbers P0, · · · Pg(n) with
Pi|n + i. A result of Ramachandra, Shorey and Tijdeman [52] states that

g(n) > c1
 ( log n
log log n
 )3

where c1 > 0 is a computable absolute constant. Further Ramachandra, Shorey and Tijdeman [53]
showed that
 ω(∆(n, k)) ≥ k for 1 ≤ k ≤ exp(c2(log n) 1
2 )

where c2 is a computable absolute constant. The proof of these results depend on the theory of
linear forms in logarithms. The constants c1 and c2 in the above results turns out to be very small.
Therefore the above results are valid only for large values of n. Erd˝os and Selfridge (see [48]) showed
that Grimm’s Conjecture implies that there is a always a prime between two consecutive squares.
The latter result is out of bounds even after assuming Riemann hypothesis. Thus a proof of Grimm’s
conjecture is very diﬃcult.
We need to prove only Theorems 1.2.1, 1.2.4 (see Chapter 4) and Theorem 1.2.6 (see Chapter
5) from this section.
 1.3. RESULTS ON REFINEMENT OF P (∆(n, k)) > k 5

1.3. Results on reﬁnement of P (∆(n, k)) > k

Let d = 1. We observe that P (∆(1, k)) ≤ k and therefore, the assumption n > k in (1.1.3)
cannot be removed. The assertion (1.1.3) was rediscovered and proved by Schur [68] and Erd˝os
[10] gave another proof. For n > k, Moser [44] sharpened (1.1.3) to P (∆(n, k)) > 11
10 k and Hanson
[23] to P (∆(n, k)) > 1.5k unless (n, k) = (3, 2), (8, 2), (6, 5). Further Faulkner [16] proved that
P (∆(n, k)) > 2k if n is greater than or equal to the least prime exceeding 2k and (n, k) ̸= (8, 2), (8, 3).
We sharpen the results of Hanson and Faulkner. Let k = 2. Then we observe (see Lemma 6.1.5)
that P (∆(n, k)) > 2k unless n = 3, 8 and that P (∆(3, 2)) = P (∆(8, 2)) = 3. Thus the estimates
(1.3.1)-(1.3.4) are valid for k = 2 whenever n ̸= 3, 8 in the case of (1.3.1) and (1.3.2). Therefore we
assume k ≥ 3 from now onwards in this section. Let

E10 = {58}; E8 = E10 ∪ {59}; E6 = E8 ∪ {60};

E4 = E6 ∪ {12, 16, 46, 61, 72, 93, 103, 109, 151, 163};

E2 = E4 ∪ {4, 7, 10, 13, 17, 19, 25, 28, 32, 38, 43, 47, 62, 73, 94, 104, 110, 124, 152, 164, 269}

and E2i+1 = E2i for 1 ≤ i ≤ 5. Further let

E1 = E2 ∪ {3, 5, 6, 8, 9, 11, 14, 15, 18, 20, 23, 26, 29, 33, 35, 39, 41, 44, 48, 50, 53,

56, 63, 68, 74, 78, 81, 86, 89, 95, 105, 111, 125, 146, 153, 165, 173, 270}.

Finally we denote E0

E0 = {(8, 3), (6, 4), (7, 4), (15, 13), (16, 13)} ∪ {(k + 1, k) : k = 3, 4, 5, 8, 11, 13, 14, 18, 63}.

Then

Theorem 1.3.1. (Laishram and Shorey, [30])
We have
 P (∆(n, k)) > 1.95k for n > k(1.3.1)

unless (n, k) ∈ [k + 1, k, h] for k ∈ Eh with 1 ≤ h ≤ 11 or (n, k) = (8, 3).

We observe that P (∆(k + 1, k)) ≤ 2k and therefore, 1.95 in (1.3.1) cannot be replaced by 2.
There are few exceptions if 1.95 is replaced by 1.8 in Theorem 1.3.1. We derive from Theorem 1.3.1
the following result.

Corollary 1.3.2. We have
 P (∆(n, k)) > 1.8k for n > k(1.3.2)

unless (n, k) ∈ E0.

Recently Corollary 1.3.2 has been applied to prove the irreducibility results over rationals for
certain Generalised Laguerre polynominals

L
(α)
m (x) =
 m∑

j=0
 (m + α)(m − 1 + α) · · · (j + 1 + α)
j!(m − j)! (−x)
j

where m ∈ N and α ∈ R. Schur ([69], [70]) showed that the polynomials L
(0)
m (x), L
(1)
m (x) are
irreducible for all m. Filaseta, Finch and Leidy [18] used Corollary 1.3.2 to give a generalisation
of Schur’s result. They showed that for all integers m ≥ 1 and integers α with 0 ≤ α ≤ 10, the
polynomial
 L
(α)
m (x) is irreducible

unless (m, α) ∈ {(2, 2), (4, 5), (2, 7)}. We ﬁnd that for each of these exceptional pairs (m, α), the
polynomial L
(α)
m (x) has the factor x − 6 and hence reducible.
The proofs of Theorem 1.3.1 and Corollary 1.3.2 are given in Sections 6.4 and 6.5, respectively.
However if we replace n > k by stronger conditions, then we obtain better estimates of P (∆(n, k)).
In Sections 6.2 and 6.3, we prove the following result.

6 INTRODUCTION

Theorem 1.3.3. (Laishram and Shorey, [30])
We have
(a)
 P (∆(n, k)) > 2k for n > max(k + 13, 279
262 k).(1.3.3)

(b)
 P (∆(n, k)) > 1.97k for n > k + 13.(1.3.4)

We observe that 1.97 in (1.3.4) cannot be replaced by 2 since there are arbitrary long chains
of consecutive composite positive integers. The same reason implies that Theorem 1.3.3 (a) is not
valid under the assumption n > k + 13. Further the assumption n > 279
262 k in Theorem 1.3.3 (a) is
necessary since P (∆(279, 262)) ≤ 2 × 262.
When k is suﬃciently large, we obtain sharper estimates of P (∆(n, k)). See Shorey and Tijdeman
[73, Chapter 7]. Ramachandra and Shorey [51] proved that

P (∆(n, k)) > c4k log k ( log log k
log log log k
 ) 1
2 if n > k 3
2

where c4 > 0 is a computable absolute constant. Further it follows from the work of Jutila [24] and
Shorey [71] that
 P (∆(n, k)) > c5k log k log log k
log log log k if n > k 3
2

where c5 is a computable absolute positive constant. If n ≤ k 3
2 , it follows from the results on
diﬀerence between consecutive primes that ∆(n, k) has a term which is prime. The proof of the
result of Ramachandra and Shorey depends on Sieve method and the theory of linear forms in
logarithms. The proof of the result of Jutila and Shorey depends on estimates from exponential
sums and the theory of linear forms in logarithms. Langevin [35], [36] proved that for any ϵ > 0,

P (∆(n, k)) > (1 − ϵ)k log log k if n ≥ c6 = c6(k, ϵ)

where c6 is a computable number depending only on k and ϵ. For an account of results in this
direction, see Shorey and Tijdeman [73, p. 135].

1.4. Sharpenings of ω(∆(n, d, k)) ≥ πd(k) when d > 1

Let d > 1. The case k = 2 is trivial and we assume k ≥ 3 in this section. We state Schinzel’s
Hypothesis H [66]:
Let f1(x), · · · , fr(x) be irreducible non constant polynomials with integer coeﬃcients and the
leading coeﬃcients positive. Assume that for every prime p, there is an integer a such that the
product f1(a) · · · fr(a) is not divisible by p. Then there are inﬁnitely many positive integers m such
that f1(m), · · · , fr(m) are all primes.
We assume Schinzel’s hypothesis. Then 1 + d and 1 + 2d are primes for inﬁnitely many d.
Therefore
 ω(∆) = π(k), k = 3(1.4.1)

for inﬁnitely many pairs (n, d) = (1, d). Let fr(x) = 1 + rx for r = 1, 2, 3, 4. For a given p, we see
that p ∤ f1(p)f2(p) · · · f4(p). Hence there are inﬁnitely many d such that 1 + d, 1 + 2d, 1 + 3d, 1 + 4d
are all primes. Thus
 ω(∆) = π(k) + 1, k = 4, 5(1.4.2)

for inﬁnitely many pairs (n, d) = (1, d).
Shorey and Tijdeman [74] proved that
ω(∆) ≥ π(k).(1.4.3)
 1.4. SHARPENINGS OF ω(∆(n, d, k)) ≥ πd(k) WHEN d > 1 7

Thus (1.4.3) is likely to be best possible when k = 3 by (1.4.1). In fact, (1.4.3) is likely to be best
possible for k = 3 when n = 1. Moree [43] sharpened (1.4.3) to

ω(∆) > π(k) if k ≥ 4 and (n, d, k) ̸= (1, 2, 5).(1.4.4)

If k = 4, 5, then (1.4.4) is likely to be best possible by (1.4.2) when n = 1.
Saradha and Shorey [62] showed that for k ≥ 4, ∆ is divisible by at least 2 distinct primes
exceeding k except when (n, d, k) ∈ {(1, 5, 4), (2, 7, 4), (3, 5, 4), (1, 2, 5), (2, 7, 5), (4, 7, 5), (4, 23, 5)}.
Further Saradha, Shorey and Tijdeman [65, Theorem 1] improved (1.4.4) to

ω(∆) > 6
5 π(k) + 1 for k ≥ 6(1.4.5)

unless (n, d, k) ∈ V0 where V0 is

{(1, 2, 6), (1, 3, 6), (1, 2, 7), (1, 3, 7), (1, 4, 7), (2, 3, 7), (2, 5, 7), (3, 2, 7),

(1, 2, 8), (1, 2, 11), (1, 3, 11), (1, 2, 13), (3, 2, 13), (1, 2, 14)}.
(1.4.6)

In fact they derived (1.4.5) from

W (∆) > 6
5 π(k) − πd(k) + 1 for k ≥ 6(1.4.7)

unless (n, d, k) ∈ V0. It is easy to see that the preceding result is equivalent to [65, Theorem 2]. By
Schinzel’s Hypothesis, we observe that (1.4.5) is likely to be best possible for k = 6, 7 when n = 1.
For k = 8, we sharpen (1.4.7) by showing

W (∆) ≥ k − 1 − πd(k)(1.4.8)

except when n = 1, d ∈ {2, 3, 4, 5, 7};

n = 2, d ∈ {3, 5}; n = 3, d = 2;

n = 4, d = 3; n = 7, d ∈ {3, 5}.
(1.4.9)

Again by Schinzel’s Hypothesis, (1.4.8) is likely to be best possible for k = 8 when n = 1. A proof
of (1.4.8) is given in Section 7.5.
For k ≥ 9, Laishram and Shorey [29] sharpened (1.4.7) as

Theorem 1.4.1. (Laishram and Shorey, [29])
Let k ≥ 9 and (n, d, k) /∈ V where V is given by





n = 1, d = 3, k = 9, 10, 11, 12, 19, 22, 24, 31;
n = 2, d = 3, k = 12; n = 4, d = 3, k = 9, 10;
n = 2, d = 5, k = 9, 10; n = 1, d = 7, k = 10.
(1.4.10)

Then
 W (∆) ≥ π(2k) − πd(k) − ρ(1.4.11)

where
 ρ = ρ(d) =
 {
1 if d = 2, n ≤ k
0 otherwise. .

When d = 2 and n = 1, we see that
 ω(∆) = π(2k) − 1

and
 W (∆) = π(2k) − πd(k) − 1

by (1.1.2), for every k ≥ 2. This is also true for n = 3, d = 2 and 2k + 1 is not a prime. Thus (1.4.11)
is best possible when d = 2. We see from Theorem 1.4.1 and (1.1.1) that

ω(∆) ≥ π(2k) − ρ if (n, d, k) /∈ V.(1.4.12)

8 INTRODUCTION

For (n, d, k) ∈ V , we see that ω(∆) = π(2k) − 1 except at (n, d, k) = (1, 3, 10). This is also the case
for (n, d, k) ∈ V0 with k = 6, 7, 8. Now, we apply Theorem 1.4.1, (1.4.5) for k = 6, 7, 8 and (1.4.4)
for k = 4, 5 to get the following result immediately.

Corollary 1.4.2. Let k ≥ 4. Then
 ω(∆) ≥ π(2k) − 1(1.4.13)

except at (n, d, k) = (1, 3, 10).

This solves a conjecture of Moree [43]. The proof of Theorem 1.4.1 is given in Section 7.4.

1.5. Results on reﬁnements of P (∆(n, d, k)) > k for d > 1

We observe that P (∆(n, d, 2)) = 2 if and only if n = 1, d = 2r − 1 with r > 1. Therefore we
suppose that k ≥ 3 in this section. Let d = 2. If n > k, then (1.5.2) follows from Theorem 1.4.1. Let
n ≤ k. Then we observe that P (∆(n, 2, k)) ≤ 2k implies P (∆(n + k, 1, k)) ≤ 2k. Therefore the case
d = 2 when considering P (∆(n, 2, k)) > 2k reduces to considering P (∆(n + k, 1, k)) > 2k discussed
above in the case d = 1. Therefore we may suppose that d > 2.
Langevin [38] sharpened (1.1.3) to
 P (∆) > k if n > k.

Shorey and Tijdeman [75] improved the above result as

P (∆) > k unless (n, d, k) = (2, 7, 3).(1.5.1)

We have

Theorem 1.5.1. (Laishram and Shorey, [32])
Let d > 2. Then
 P (∆) > 2k(1.5.2)

unless (n, d, k) is given by
 k = 3, n = 1, d = 4, 7;

n = 2, d = 3, 7, 23, 79;

n = 3, d = 61; n = 4, d = 23;

n = 5, d = 11; n = 18, d = 7;

k = 4, n = 1, d = 3, 13; n = 3, d = 11;

k = 10, n = 1, d = 3.

It is necessary to exclude the exceptions stated in Theorem 1.5.1. A proof of Theorem 1.5.1 is
given in Chapter 8. It depends on Theorem 1.4.1 and the theory of linear forms in logarithms.

CHAPTER 2

A survey of results on squares in products of terms in an
arithmetic progression

2.1. Introduction

Let n, d, k, b, y be positive integers such that b is square free, d ≥ 1, k ≥ 2, P (b) ≤ k and
gcd(n, d) = 1. We consider the equation

(2.1.1) ∆(n, d, k) = n(n + d) · · · (n + (k − 1)d) = by2.

If k = 2, we observe that (2.1.1) has inﬁnitely many solutions. Therefore we always suppose that
k ≥ 3. Let p > k, p|(n + id). Then p ∤ (n + jd) for j ̸= i otherwise p|(i − j) and |i − j| < k. Equating
powers of p on both sides of (2.1.1), we see that ordp(n + id) is even. From (2.1.1), we have

n + id = aix
2
i = AiX 2
i(2.1.2)

with ai squarefree and P (ai) ≤ k, P (Ai) ≤ k and (Xi, ∏
p<k p) = 1 for 0 ≤ i < k. Since gcd(n, d) = 1,
we also have
 (Ai, d) = (ai, d) = (Xi, d) = (xi, d) = 1 for 0 ≤ i < k.(2.1.3)

We call (ak−1, ak−2, · · · , a1, a0) as the mirror image of (a0, a1, a2, · · · , ak−1).
Let d = 1. We recall that ∆(n, 1, k) = ∆(n, k). Several particular cases of (2.1.1) have been
treated by many mathematicians. We refer to Dickson [5] for a history. It is a consequence of
some old diophantine results that (2.1.1) with k = 3 is possible only when n = 1, 2, 48. Let k ≥
4. As mentioned in the beginning of Section 1.2, there are inﬁnitely many pairs (n, k) such that
P (∆(n, k)) ≤ k. Then (2.1.1) is satisﬁed with P (y) ≤ k for these inﬁnitely many pairs. Therefore
we consider (2.1.1) with P (∆(n, k)) > k. This assumption is satisﬁed when n > k by (1.1.3).
Developing on the earlier work of Erd˝os [11] and Rigge [55], it was shown by Erd˝os and Selfridge
[13] that (2.1.1) with n > k2 and P (b) < k does not hold. Suppose P := P (∆(n, k)) > k. Then
there is a unique i with 0 ≤ i < k such that n + i is divisible by P . Hence by (2.1.1), n + i is divisible
by P 2 showing that n + i ≥ (k + 1)
2 giving n > k2. Thus it follows from the result of Erd˝os and
Selfridge [13] that (2.1.1) with P > k and P (b) < k does not hold. The assumption P (b) < k has
been relaxed to P (b) ≤ k in Saradha [60].
Therefore we suppose that d > 1. Let k = 3. Then it follows from inﬁnitude of solutions of
Pell’s equation that there are inﬁnitely many solutions of (2.1.1). Therefore we assume from now
onward that k ≥ 4. Fermat (see Mordell [42, p.21]) showed that there are no four squares in an
arithmetic progression. Euler proved a more general result that a product of four terms in arithmetic
progression can never be a square. We prove the following result in Section 10.9.

Theorem 2.1.1. (Hirata-Kohno, Laishram, Shorey and Tijdeman, [25])
Equation (2.1.1) with 4 ≤ k ≤ 109 and b = 1 is not possible.

By Euler, Theorem 2.1.1 is valid when k = 4. The case when k = 5 is due to Obl´ath [50].
Independently, Bennett, Bruin, Gy˝ory and Hajdu [1] proved that (2.1.1) with 6 ≤ k ≤ 11 does not
hold.
We know that (2.1.1) with k = 4 and b = 6 has inﬁnitely many solutions. A general conjecture
states that ∆ is divisible by a prime > k to an odd power. In other words,

Conjecture 2.1.2. Equation (2.1.1) with P (b) ≤ k implies that k = 4, b = 6.

9

10 2. A SURVEY OF RESULTS ON SQUARES IN ARITHMETIC PROGRESSION

A weaker version of Conjecture 2.1.2 is the following conjecture due to Erd˝os.

Conjecture 2.1.3. Equation (2.1.1) with P (b) ≤ k implies k is bounded by a computable
absolute constant.

Granville (unpublished) showed that Conjecture 2.1.3 follows from Oesterl´e and Masser’s abc-
conjecture, see Laishram [27, Section 9.4] for a proof. Now we turn to results towards Conjectures
2.1.2 and 2.1.3.
 2.2. Conjecture 2.1.2 with k ﬁxed

Let k be ﬁxed. As already stated, (2.1.1) with k = 4 and b = 6 has inﬁnitely many solutions.
On the other hand, (2.1.1) with k = 4 and b ̸= 6 does not hold. Therefore we consider (2.1.1) with
k ≥ 5. By (2.1.2), the equation (2.1.1) yields a k-tuple (a0, a1, . . . , ak−1). We re-write (2.1.1) as

m(m − d) · · · (m − (k − 1)d) = by2, m = n + (k − 1)d.(2.2.1)

The equation (2.2.1) is called the mirror image of (2.1.1). The corresponding k-tuple (ak−1, ak−2, . . . , a0)
is called the mirror image of (a0, a1, . . . , ak−1).
Let P (b) < k. In Chapter 10 (see Section 10.1), we prove the following result.

Theorem 2.2.1. (Hirata-Kohno, Laishram, Shorey and Tijdeman [25])
Equation (2.1.1) with P (b) < k and 5 ≤ k ≤ 100 implies that (a0, a1, . . . , ak−1) is among the
following tuples or their mirror images.

k = 8 : (2, 3, 1, 5, 6, 7, 2, 1), (3, 1, 5, 6, 7, 2, 1, 10);

k = 9 : (2, 3, 1, 5, 6, 7, 2, 1, 10);

k = 14 : (3, 1, 5, 6, 7, 2, 1, 10, 11, 3, 13, 14, 15, 1);

k = 24 : (5, 6, 7, 2, 1, 10, 11, 3, 13, 14, 15, 1, 17, 2, 19, 5, 21, 22, 23, 6, 1, 26, 3, 7).

(2.2.2)

Theorem 2.2.1 with k = 5 is due to Mukhopadhyay and Shorey [45]. A diﬀerent proof is given in
Section 10.2. Initially, Bennett, Bruin, Gy˝ory, Hajdu [1] and Hirata-Kohno, Shorey (unpublished),
independently, proved Theorem 2.2.1 with k = 6 and (a0, a1, . . . .a5) ̸= (1, 2, 3, 1, 5, 6), (6, 5, 1, 3, 2, 1).
Next Bennett, Bruin, Gy˝ory and Hajdu [1] removed the assumption on (a0, a1, . . . , a5) in the above
result. They also showed, independently, that (2.1.1) with 7 ≤ k ≤ 11 and P (b) ≤ 5 is not possible.
This is now a special case of Theorem 2.2.1.
Let P (b) = k. The case k = 5 and P (b) = 5 in (2.1.1) is still open. For k ≥ 7, Hirata-Kohno,
Laishram, Shorey and Tijdeman [25] showed that

Theorem 2.2.2. (Hirata-Kohno, Laishram, Shorey and Tijdeman [25])
Equation (2.1.1) with P (b) = k and 7 ≤ k ≤ 100 implies that (a0, a1, · · · , ak−1) is among the
following tuples or their mirror images.

k = 7 : (2, 3, 1, 5, 6, 7, 2), (3, 1, 5, 6, 7, 2, 1), (1, 5, 6, 7, 2, 1, 10);

k = 13 : (3, 1, 5, 6, 7, 2, 1, 10, 11, 3, 13, 14, 15),

(1, 5, 6, 7, 2, 1, 10, 11, 3, 13, 14, 15, 1);

k = 19 : (1, 5, 6, 7, 2, 1, 10, 11, 3, 13, 14, 15, 1, 17, 2, 19, 5, 21, 22);

k = 23 : (5, 6, 7, 2, 1, 10, 11, 3, 13, 14, 15, 1, 17, 2, 19, 5, 21, 22, 23, 6, 1, 26, 3),

(6, 7, 2, 1, 10, 11, 3, 13, 14, 15, 1, 17, 2, 19, 5, 21, 22, 23, 6, 1, 26, 3, 7).

(2.2.3)

A proof of Theorem 2.2.2 is given in Chapter 10 (see Section 10.1).

2.3. Equation (2.1.1) with k as a variable

Let us now consider (2.1.1) with k as a variable. When d is ﬁxed, Marszalek [40] conﬁrmed
Conjecture (2.1.3) by showing that k is bounded by a computable constant depending only on d.
This was reﬁned by Shorey and Tijdeman [76] when ω(d) is ﬁxed. They showed that (2.1.1) implies

2.5. EQUATION (2.1.1) WITH ω(d) FIXED 11

that k is bounded by a computable number depending only on ω(d) conﬁrming Conjecture (2.1.3)
when ω(d) is ﬁxed. In fact they showed that (2.1.1) implies

2ω(d) > c1 k
log k
(2.3.1)

which gives
 d > kc2 log log k(2.3.2)

where c1 > 0 and c2 > 0 are absolute constants. Laishram [26] gave an explicit version of (2.3.1)
by showing
 k <
 {
2.25ω(d)4
ω(d) if d is even
11ω(d)4
ω(d) if d is odd

for ω(d) ≥ 12 whenever (2.1.1) holds. Further Laishram and Shorey [33] improved it to

Theorem 2.3.1. (Laishram and Shorey [33])
Equation (2.1.1) implies that
 k < 2ω(d)2
ω(d).

A proof of Theorem 2.3.1 is given in Section 11.5.

2.4. Conjecture 2.1.2 with d ﬁxed

Let d be ﬁxed. We consider Conjecture 2.1.2. For a given value of d, we observe that (2.1.1)
with k ∈ {4, 5} can be solved via ﬁnding all the integral points on elliptic curves by MAGMA or
SIMATH as in [17] and [63]. Equation (2.1.1) was completely solved for k ≥ 4 and 1 < d ≤ 104
in Saradha and Shorey [63]. For earlier results, see Saradha [59] and Filakovszky and Hajdu [17].
The following theorem conﬁrms Conjecture 2.1.2 for d ≤ 1010 and k ≥ 6.

Theorem 2.4.1. (Laishram and Shorey [33])
Equation (2.1.1) with k ≥ 6 implies that

d > max(1010, klog log k).

We give a proof of this theorem in Section 11.6.

2.5. Equation (2.1.1) with ω(d) ﬁxed

Let ω(d) be ﬁxed. Let b = 1. Saradha and Shorey [63] proved that (2.1.1) with ω(d) = 1 does
not hold. In fact they proved it without the condition gcd(n, d) = 1. Thus a product of four or more
terms in an arithmetic progression with common diﬀerence a prime power can never be a square.
We extend this to ω(d) = 2 in the following result.

Theorem 2.5.1. (Laishram and Shorey [33])
A product of eight or more terms in arithmetic progression with common diﬀerence d satisfying
ω(d) = 2 is never a square.

A proof of Theorem 2.5.1 is given in Section 11.7. However we solve (2.1.1) with ω(d) ≤ 5 and
b = 1 completely when gcd(n, d) = 1. We have

Theorem 2.5.2. (Laishram and Shorey [33])
Equation (2.1.1) with b = 1 and ω(d) ≤ 5 does not hold.

A proof of this result is given in Section 11.3. Theorem 2.5.2 contains the case ω(d) = 1 already
proved by Saradha and Shorey [63].
Let P (b) ≤ k. As stated earlier, equation (2.1.1) with k = 6 is not possible by Bennett, Bruin,
Gy˝ory and Hajdu [1]. Also (2.1.1) with P (b) < k does not hold by Mukhopadhyay and Shorey [45]
for k = 5 and Hirata-Kohno, Laishram, Shorey and Tijdeman [25] for k = 7. We have no results on

12 2. A SURVEY OF RESULTS ON SQUARES IN ARITHMETIC PROGRESSION

(2.1.1) with k ∈ {5, 7} and P (b) = k. Therefore we assume k ≥ 8 in the next result. Let S1 be the
set of tuples (a0, . . . , ak−1) given by

k = 8 : (2, 3, 1, 5, 6, 7, 2, 1), (3, 1, 5, 6, 7, 2, 1, 10);

k = 9 : (2, 3, 1, 5, 6, 7, 2, 1, 10);

k = 13 : (3, 1, 5, 6, 7, 2, 1, 10, 11, 3, 13, 14, 15), (1, 5, 6, 7, 2, 1, 10, 11, 3, 13, 14, 15, 1)

and their mirror images. Further S2 be the set of tuples (a0, a1, . . . , ak−1) given by

k = 14 : (3, 1, 5, 6, 7, 2, 1, 10, 11, 3, 13, 14, 15, 1);

k = 19 : (1, 5, 6, 7, 2, 1, 10, 11, 3, 13, 14, 15, 1, 17, 2, 19, 5, 21, 22);

k = 23 : (5, 6, 7, 2, 1, 10, 11, 3, 13, 14, 15, 1, 17, 2, 19, 5, 21, 22, 23, 6, 1, 26, 3),

(6, 7, 2, 1, 10, 11, 3, 13, 14, 15, 1, 17, 2, 19, 5, 21, 22, 23, 6, 1, 26, 3, 7);

k = 24 : (5, 6, 7, 2, 1, 10, 11, 3, 13, 14, 15, 1, 17, 2, 19, 5, 21, 22, 23, 6, 1, 26, 3, 7)

and their mirror images. We have

Theorem 2.5.3. (Laishram and Shorey [33])
(a) Equation (2.1.1) with k ≥ 8 and ω(d) ≤ 4 implies that either ω(d) = 2, k = 8, (a0, a1, . . . , a7) ∈
{(3, 1, 5, 6, 7, 2, 1, 10), (10, 1, 2, 7, 6, 5, 1, 3)} or ω(d) = 3, (a0, a1, . . . , ak−1) ∈ S1 or ω(d) = 4, (a0, a1,
. . . , ak−1) ∈ S1 ∪ S2.
(b) Equation (2.1.1) with ω(d) ∈ {5, 6} and d even does not hold.

A proof of Theorem 2.5.3 is given in Section 11.4. Theorem 2.5.3 contains already proved case
ω(d) = 1 where it has been shown in [63] for k > 29 and [45] for 4 ≤ k ≤ 29 that (2.1.1) implies
that either k = 4, (n, d, b, y) = (75, 23, 6, 140) or k = 5, P (b) = k. We do not use this result in the
proof of Theorem 2.5.3.

2.6. Equation ∆(n, d, k) = by2 with ω(d) = 1 and at most two terms omitted

We now consider a equation more general than (6). Let k ≥ 5, t ≥ k − 2 and γ1 < γ2 < · · · < γt
be integers with 0 ≤ γi < k for 1 ≤ i ≤ t. Thus t ∈ {k, k − 1, k − 2}, γt ≥ k − 3 and γi = i − 1 for
1 ≤ i ≤ t if t = k. We put ψ = k − t. Let b be a positive squarefree integer and we shall always
assume, unless otherwise speciﬁed, that P (b) ≤ k. We consider the equation

(2.6.1) (n + γ1d) · · · (n + γtd) = by2

in positive integers n, d, k, b, y, t. We shall follow the above assumptions stated in this section when-
ever we refer to (2.6.1). When ψ = 0, then (2.6.1) is the same as (2.1.1). Therefore we consider
ψ = 1, 2.
Let ψ = 1. We may assume that γ1 = 0 and γt = k − 1 otherwise this is the case ψ = 0. It has
been shown in [61] that
 6!
5 = (12)2, 10!
7 = (720)2

are the only squares that are products of k−1 distinct integers out of k consecutive integers conﬁrming
a conjecture of Erd˝os and Selfridge [13]. This corresponds to the case b = 1 and d = 1 in (2.6.1). In
general, it has been proved in [61] that (2.6.1) with d = 1 and k ≥ 4 implies that (b, k, n) = (2, 4, 24)
under the necessary assumption that the left hand side of (2.6.1) is divisible by a prime > k. Further
it has been shown in [63, Theorem 4] and [46] that (2.1.1) with d > 1, gcd(n, d) = 1, ω(d) = 1 and
P (b) < k implies that k ≤ 8.
Let ψ = 2. Let d = 1. Then it has been shown in [47, Corollary 3] that a product of k − 2
distinct terms out of k consecutive positive integers is a square only if it is given by

6!
1.5 = 7!
5.7 = 12
2, 10!
1.7 = 11!
7.11 = 720
2.

2.6. EQUATION ∆(n, d, k) = by2 WITH ω(d) = 1 AND AT MOST TWO TERMS OMITTED 13

and 



 4!
2.3 = 2
2, 6!
4.5 = 6
2, 8!
2.5.7 = 24
2, 10!
2.3.4.6.7 = 60
2, 9!
2.5.7 = 72
2,

10!
2.3.6.7 = 120
2, 10!
2.7.8 = 180
2, 10!
7.9 = 240
2, 10!
4.7 = 360
2,

21!
13!.17.19 = 5040
2, 14!
2.3.4.11.13 = 5040
2, 14!
2.3.11.13 = 10080
2.
These corresponds to (2.1.1) with b = 1. For the general case, we have

Theorem 2.6.1.
Let ψ = 2, d = 1 and k ≥ 5. Assume that the left hand side of (2.6.1) is divisible by a prime > k.
Then (2.6.1) is not valid unless k = 5, n ∈ {45, 46, 47, 48, 96, 239, 240, 241,
242, 359, 360} and k = 6, n ∈ {45, 240}.

We observe that n + k − 1 ≥ p2
π(k)+1 ≥ (k + 1)
2 since the left hand side of (2.6.1) is divisible
by a prime > k. Thus n > k2 and the assertion for k ≥ 6 follows immediately from [47, Theorem
2]. Let k = 5. Then n ≥ 72 − 4 = 45. Multiplying both sides of (2.1.1) by b3 and putting
X = b(n + γ2), Y = b2y, we get the elliptic curve

Y 2 = X 3 + b(γ1 + γ3 − 2γ2)X 2 + b2(γ1 − γ2)(γ3 − γ2)X.

For each choice of triplets (γ1, γ2, γ3) with 0 ≤ γ1 < γ2 < γ3 ≤ 4 and for each b ∈ {1, 2, 3, 6, 5, 10, 15, 30},
we check for the integral points on the elliptic curve using MAGMA. Observing that b|X, b2|Y and
X = b(n + γ2) ≥ 45b, we ﬁnd that all the solutions of (2.1.1) are given by those listed in the as-
sertion of Theorem 2.6.1. For instance, when (γ1, γ2, γ3) = (0, 2, 4) and b = 3, we have the curve
Y 2 = X 3 − 36X and the integral points with X ≥ 45b is X = 294, Y = 5040. Then n + 2 = 294
3 = 98
giving n = 96 and we see that 96 · 98 · 100 = 12(4 × 7 × 10)
2 gives a solution.
Let d > 1. In Section 12.4, we prove the following result.

Theorem 2.6.2. (Laishram and Shorey [34])
Let ψ = 2, k ≥ 15. Assume that P (b) < k if k = 17, 19. Then (2.6.1) with ω(d) = 1 does not hold.

As an immediate consequence of Theorem 2.6.2, we see that (2.1.1) with ω(d) = 1, ψ = 0, d ∤
n, k ≥ 15, P (b) ≤ pπ(k)+1 if k = 17, 19 and P (b) ≤ pπ(k)+2 if k > 19 does not hold. For the proof,
we delete the terms, if any, divisibly by primes {k, pπ(k)+1} if k = 17, 19 and {pπ(k)+1, pπ(k)+2}
otherwise. Then the assertion follows from Theorem 2.6.2.
The assumption gcd(n, d) = 1 can be replaced by d ∤ n in Theorem 2.6.2. Consider Theorem
2.6.2 with gcd(n, d) > 1. Let pβ =gcd(n, d), n′ = n
pβ and d′ = d
pβ . Then d′ > 1 since d ∤ n. Now, by
dividing (pβ)
t on both sides of (2.6.1), we have

(2.6.2) (n′ + γ1d′) · · · (n′ + γtd′) = pϵb′y′2

where y′ > 0 is an integer with P (b′) ≤ k, P (b′) < k when k = 17 and ϵ ∈ {0, 1}. Since p|d′ and
gcd(n′, d′) = 1, we see that p ∤ (n′ + γ1d′) · · · (n′ + γtd′) giving ϵ = 0 and assertion follows.

CHAPTER 3

Results from prime number theory

In this chapter, we state the results from Prime Number Theory and related areas which we will
be using in the proofs in the subsequent chapters.

3.1. Estimates of some functions on primes and Stirling’s formula

We begin with the bounds for π(ν) given by Rosser and Schoenfeld, see [58, p. 69-71].

Lemma 3.1.1. For ν > 1, we have

(i) π(ν) < ν
log ν
 (1 + 3
2 log ν
 )

(ii) π(ν) > ν
log ν − 1
2 for ν ≥ 67

(iii) ∏

pa≤ν pa < (2.826)
ν

(iv) ∏

p≤ν p < (2.763)
ν

(v) pi ≥ i log i for i ≥ 2.

The following sharper estimates are due to Dusart [6, p.14; Prop 1.7]. See also [7, p.55], [8,
p.414].

Lemma 3.1.2. For ν > 1, we have

(i) π(ν) ≤ ν
log ν
 (1 + 1.2762
log ν
 ) =: a(ν)

(ii) π(ν) ≥ ν
log ν − 1 =: b(ν) for ν ≥ 5393

(iii) ∏

p≤ν p < 2.71851ν.

The next lemma is on the estimate of ∑

p≤pi log p due to G. Robin [56, Theorem 6].

Lemma 3.1.3. For i ≥ 2, we have
∑

p≤pi log p > i(log i + log log i − 1.076868).

The following lemma is due to Ramar´e and Rumely [54, Theorems 1, 2].

Lemma 3.1.4. Let k ∈ {3, 4, 5, 7}, l be a positive integer such that gcd(l, k) = 1 and

θ(x, k, l) = ∑

p≤x
p≡l(mod k)
 log p.

Then for x0 ≤ 1010, we have

θ(x, k, l) ≥
 { x
φ(k) (1 − ϵ
′) for x ≥ 1010

x
φ(k) (1 − ϵφ(k)
√
x0
 ) for 1010 > x ≥ x0
(3.1.1)
 15

16 3. RESULTS FROM PRIME NUMBER THEORY

and
 θ(x, k, l) ≤
 { x
φ(k) (1 + ϵ
′) for x ≥ 1010

x
φ(k) (1 + ϵφ(k)
√
x0
 ) for 1010 > x ≥ x0
(3.1.2)

where ϵ := ϵ(k) and ϵ
′ := ϵ
′(k) are given by

k 3 4 5 7
ϵ 1.798158 1.780719 1.412480 1.105822
ϵ
′ 0.002238 0.002238 0.002785 0.003248

In the next lemma, we derive estimates for π(x, k, l) and π(2x, k, l) − π(x, k, l) from Lemma
3.1.4.

Lemma 3.1.5. Let k ∈ {3, 4, 5, 7} and l be a positive integer such that gdc(l, k) = 1. Then we
have
 π(x, k, l) ≥ x
log x
 (c1 + c2
log x
2
 ) f or x ≥ x0(3.1.3)

and
 π(2x, k, l) − π(x, k, l) ≤ c3 x
log x f or x ≥ x0(3.1.4)

where c1, c2, c3 and x0 are given by

k 3 4 5 7
c1 0.488627 0.443688 0.22175 0.138114
c2 0.167712 0.145687 0.0727974 0.043768
c3 0.527456 0.6359475 0.3182006 0.235598
x0 25000 1000 2500 1500

Proof. We have
 θ(x, k, l) = ∑

p≤x
p≡l(mod k)
 log p ≤ π(x, k, l) log x

so that
 π(x, k, l) ≥ θ(x, k, l)
log x .(3.1.5)

Also,

θ(x, k, l) ≤ π( x
2 , k, l) log x
2 + (π(x, k, l) − π( x
2 , k, l)
) log x = π(x, k, l) log x − π( x
2 , k, l) log 2

giving
 π(x, k, l) log x ≥ θ(x, k, l) + π( x
2 , k, l) log 2.

Now we use (3.1.5) for x
2 to derive

π(x, k, l) ≥ x
log x
 ( θ(x, k, l)
x + θ( x
2 , k, l) log 2
x 1
log x
2
 ) .(3.1.6)

Let k = 3, 4, 5, 7 and x0 := x0(k) be as given in the statement of the lemma. Since x0 ≤ 50000 ≤
( ϵφ(k)
ϵ′ )
2, we have from (3.1.1) that

θ(x, k, l) ≥ x
φ(k)
 (1 − ϵφ(k)
√x0
 ) for x ≥ x0,

θ( x
2 , k, l) ≥ x
2φ(k)
 (

1 − ϵφ(k)
√ x0
2
 )
 for x ≥ x0.
(3.1.7)
 3.1. ESTIMATES OF SOME FUNCTIONS ON PRIMES AND STIRLING’S FORMULA 17

This with (3.1.6) implies (3.1.3). Further we also have from (3.1.2) that

θ(2x, k, l) ≤ 2x
φ(k)
 (1 + ϵφ(k)
√2x0
 ) for x ≥ x0.

This with (3.1.7), (3.1.6) and

θ(2x, k, l) − θ(x, k, l) ≥ (π(2x, k, l) − π(x, k, l)) log x

implies
 π(2x, k, l) − π(x, k, l) ≤ x
log x
 ( 2
φ(k) (1 + ϵφ(k)
√2x0 − 1
φ(k) (1 − ϵφ(k)
√x0 )
)

= x
log x
 ( 1
φ(k) + (1 + √2)ϵ
√x0
 )
 ≤ c3 x
log x

for x ≥ x0, giving (3.1.4). □

The next lemma gives a lower bound for ordp(k − 1)!.

Lemma 3.1.6. For a prime p < k, we have

ordp(k − 1)! ≥ k − p
p − 1 − log(k − 1)
log p .

Proof. Let ph ≤ k − 1 < p
h+1. Then we have

ordp(k − 1)! = [ k − 1
p
 ] + · · · + [ k − 1
ph
 ] .

Now, we note that [ k−1
pi ] ≥ k−1
pi − p
i−1
pi = k
pi − 1 for i ≥ 1. Hence

ordp(k − 1)! ≥
 h∑

i=1
 ( k
pi − 1) = k
p − 1 (1 − 1
ph ) − h = k
p − 1 − 1
p − 1 k
ph − h.

Since ph ≤ k − 1 < k ≤ ph+1, we have h ≤ log(k−1)
log p and k
ph ≤ p, which we use in the estimate for
ordp((k − 1)!) above to get the lemma. □

We end this chapter with a lemma on Stirling’s formula, see Robbins [57].

Lemma 3.1.7. For a positive integer ν, we have
√2πν e
−νννe 1
12ν+1 < ν! < √2πν e
−νννe 1
12ν .

Part 1

Proof of results on reﬁnements and
extensions of Sylvester’s theorem

CHAPTER 4

Reﬁnement of Sylvester’s theorem on the number of prime
divisors in a product of consecutive integers: Proof of
Theorems 1.2.1 and 1.2.4

In this chapter we prove Theorems 1.2.1 and 1.2.4. For x ≥ k, we write

∆′ = ∆
′(x, k) = ∆(x − k + 1, k).

4.1. An Alternative Formulation

As remarked in Section 1.2, we prove Theorem 1.2.1 for k ≥ 19 and Theorem 1.2.4 for k ≥ 10.
Further we derive these two theorems from the following more general result.

Theorem 4.1.1.
(a) Let k ≥ 19, x ≥ 2k and (x, k) /∈ S3 where S3 is the union of all sets [x, k, h] such that
[x − k + 1, k, h] belongs to S2 given by (1.2.6). Let f1 < f2 < · · · < fµ be all the integers in [0, k)
satisfying
 P ((x − f1) · · · (x − fµ)) ≤ k.(4.1.1)

Then
 µ ≤ k − [ 3
4 π(k)
] + 1.(4.1.2)

(b) Let k ≥ 10, x > 29
12 k − 1. Assume (4.1.1). Then we have

µ ≤ k − M (k)(4.1.3)

where
 M (k) = max(π(2k) − π(k), [ 3
4 π(k)
] − 1).(4.1.4)

Thus, under the assumptions of the theorem, we see that the number of terms in ∆′ = x(x −
1) · · · (x − k + 1) divisible by a prime > k is at least k − µ. Since each prime > k can divide at most
one term, there are at least k − µ primes > k dividing ∆′. Thus

ω(∆′) ≥ π(k) + k − µ.

Putting x = n + k − 1, we see that ∆′ = ∆ and hence

ω(∆) ≥ π(k) + k − µ

and the Theorems 1.2.1 for k ≥ 19 and Theorem 1.2.4 for k ≥ 10 follow from (4.1.2) and (4.1.3),
respectively.
We give a sketch of the proof of Theorem 4.1.1. We ﬁrst show that it is enough to prove Theorem
4.1.1 (a) for k which are primes and Theorem 4.1.1 (b) for k such that 2k − 1 is prime. The estimates
of π function given in Lemma 3.1.2 have been applied to count the number of terms in ∆′(x, k)
which are primes and the number of terms of the form ap with 2 ≤ a ≤ 6 and p > k. The latter
contribution is crucial for keeping the estimates well under computational range. It has been applied
in the interval 2k ≤ x < 7k. In fact this interval has been partitioned into several subintervals and it
has been applied to each of those subintervals. This leads to sharper estimates. See Lemmas 4.2.6,
4.2.7, 4.2.9. For covering the range x ≥ 7k, the ideas of Erd˝os [10] have been applied, see Lemmas
4.2.3, 4.2.5, 4.2.8.
 21

22 4. PROOF OF THEOREMS 1.2.1 AND 1.2.4

4.2. Lemmas

Lemma 4.2.1. We have
 M (k) =
 {[ 3
4 π(k)
] − 1 if k ∈ K1
π(2k) − π(k) otherwise
(4.2.1)

where K1 is given by

K1 = {19, 20, 47, 48, 73, 74, 83, 89, 107, 108, 109, 110, 111, 112, 113, 114,

115, 116, 173, 199, 200, 277, 278, 281, 282, 283, 284, 285, 293}.
(4.2.2)

Proof. By Lemma 3.1.2 (i) and (ii), we have

π(2k) − π(k) − [ 3
4 π(k)
] + 1 ≥ 2k
log(2k) − 1 − 7
4 k
log k
 (1 + 1.2762
log k
 ) + 1

for k ≥ 2697. The right hand side of the above inequality is an increasing function of k and it
is non-negative at k = 2697. Hence π(2k) − π(k) ≥ [ 3
4 π(k)
] − 1 for k ≥ 2697 thereby giving
M (k) = π(2k) − π(k) for k ≥ 2697. For k < 2697, we check that (4.2.1) is valid. □

Lemma 4.2.2. (i) Let k′ < k′′ be consecutive primes. Suppose Theorem 4.1.1 (a) holds at k′.
Then it holds for all k with k′ ≤ k < k′′.
(ii) Let k1 < k2 be such that 2k1 − 1 and 2k2 − 1 are consecutive primes. Suppose Theorem 4.1.1
(b) holds at k1. Then Theorem 4.1.1 (b) holds for all k with k1 ≤ k < k2, k /∈ K1.

Proof. For the proof of (4.1.2) and (4.1.3), it suﬃces to show that

W (∆′) ≥ [ 3
4 π(k)
] − 1(4.2.3)

and
 W (∆′) ≥ M (k),(4.2.4)

respectively.
Suppose that Theorem 4.1.1 (a) holds at k′ for k′ prime. Let k as in the statement of the
Lemma and x ≥ 2k. Then x ≥ 2k1 and ∆′ = x(x − 1) · · · (x − k′ + 1)(x − k′) · · · (x − k + 1). Thus

W (∆′) ≥ W (x(x − 1) · · · (x − k′ + 1)) ≥ [ 3
4 π(k′)
] − 1 = [ 3
4 π(k)
] − 1.

We now prove (ii). Assume that Theorem 4.1.1 (b) holds at k1. Let k be as in the statement of the
lemma. Further let x ≥ 29
12 k − 1 ≥ 29
12 k1 − 1. Since k /∈ K1, we have M (k) = π(2k) − π(k) by Lemma
4.2.1. Also π(2k1) = π(2k1 − 1) = π(2k − 1) = π(2k). Therefore

W (∆′) ≥ W (x(x − 1) · · · (x − k1 + 1)) ≥ M (k1) ≥ π(2k1) − π(k1) ≥ π(2k) − π(k) = M (k).
 □

For the next lemma, we need some notations. Let P0 > 0 and ν ≥ 0 with g1, g2, · · · gν be all
the integers in [0, k) such that each of x − gi with 1 ≤ i ≤ ν is divisible by a prime exceeding P0.
Further we write
 (x − g1) · · · (x − gν) = GH(4.2.5)

with gcd(G, H) = 1, gcd(H, ∏

p≤P0p) = 1. Then we have

Lemma 4.2.3. If x < P
 3
2
0 , then

(x
k
) ≤ (2.83)
P0+
√
xx
ν
 

G ∏

p>P0 pordp(k!)



−1
 .(4.2.6)
 4.2. LEMMAS 23

Proof. We observe that

ordp
(x
k
) =
 ∞∑

ν=1
 ([ x
pν
 ] − [ x − k
pν
 ] − [ k
pν
 ]) .

Each of the summand is at most 1 if pν ≤ x and 0 otherwise. Therefore ordp(x
k) ≤ s where
ps ≤ x < p
s+1. Thus
 pordp(
x
k) ≤ ps ≤ x.(4.2.7)

Therefore ∏

p≤P0 pordp(
x
k) ≤ ∏

p≤P0
pa ≤x
 pa ≤ ∏

p≤P0 p ∏

p≤x 1
2 p ∏

p≤x 1
3 p · · · .(4.2.8)

From Lemma 3.1.1 (iii) with ν = √x and ν = P0, we get
∏

p≤x 1
2 p ∏

p≤x 1
4 p ∏

p≤x 1
6 p · · · . < (2.83)
√
x(4.2.9)

and ∏

p≤P0 p ∏

p≤P 1
2
0
 p ∏

p≤P 1
3
0
 p · · · . < (2.83)
P0,

respectively. Since x < P
 3
2
0 , we have P
 1
l
0 > x 1
2l−1 for l ≥ 2 so that the latter inequality implies
∏

p≤P0
 ∏

p≤x 1
3 p ∏

p≤x 1
5 p · · · . < (2.83)
P0.(4.2.10)

Combining (4.2.8), (4.2.9) and (4.2.10), we get
∏

p≤P0 pordp(
x
k) ≤ (2.83)
P0+
√
x.(4.2.11)

By (4.2.5), we have ∏

p>P0 pordp(
x
k) = (x − g1) · · · (x − gν)
G ∏
p>P0 pordp(k!) .(4.2.12)

Further we observe that
 (x − g1) · · · (x − gν) < x
ν.(4.2.13)

Finally, we combine (4.2.11), (4.2.12) and (4.2.13) to conclude (4.2.6). □

Lemma 4.2.3 with P0 = k implies the following result immediately, see Saradha and Shorey [61,
Lemma 3].

Corollary 4.2.4. Let x < k 3
2 . Assume that (4.1.1) holds. Then
(x
k
) ≤ (2.83)
k+
√
xx
k−µ.

Lemma 4.2.5. Assume (4.1.1) and
 µ ≥ k − M (k) + 1(4.2.14)

where M (k) is given by (4.1.4). Then we have

(i) x < k 3
2 for k ≥ 71
(ii) x < k 7
4 for k ≥ 25
(iii) x < k2 for k ≥ 13
(iv) x < k 9
4 for k ≥ 10.

24 4. PROOF OF THEOREMS 1.2.1 AND 1.2.4

Proof. Since (x − f1) · · · (x − fµ) divides (x
k)k!, we observe from (4.1.1) and (4.2.7) that

(x − f1) · · · (x − fµ) ≤
 

 ∏

p≤k pordp(
x
k)


 k! ≤
 

 ∏

p≤k x



 k! = x
π(k)k!.(4.2.15)

Also
 (x − f1) · · · (x − fµ) ≥ (x − fµ)
µ ≥ (x − k + 1)
µ > x
µ (1 − k
x
 )µ .

Comparing this with (4.2.15), we get
 k! > x
µ−π(k) (1 − k
x
 )µ .(4.2.16)

Let k ≥ 71. We assume that x ≥ k 3
2 and we shall arrive at a contradiction. From (4.2.16), we
have
 k! > k 3
2 (µ−π(k)) (1 − 1
√k
 )µ
(4.2.17)

and since µ ≤ k,
 k! > k 3
2 (µ−π(k)) (1 − 1
√k
 )k .(4.2.18)

We use (4.2.18), (4.2.14), (4.2.1) and Lemmas 3.1.2 (i) and 3.1.7 to derive for k ≥ 294 that

1 > 2.718k 1
2 − 3
log2k (1+ 1.2762
log2k )(1 − 1
√k )

since exp
( log 0.3989k
k − 1
12k2 ) ≥ 1. The right hand side of above inequality is an increasing function

of k and it is not valid at k = 294. Thus k ≤ 293. Further we check that (4.2.18) is not valid for
71 ≤ k ≤ 293 except at k = 71, 73 by using (4.2.14) with µ = k − M (k) + 1 and the exact values of
k! and M (k). Let k = 71, 73. We check that (4.2.17) is not satisﬁed if (4.2.14) holds with equality
sign. Thus we may suppose that (4.2.14) holds with strict inequality. Then we ﬁnd that (4.2.18)
does not hold. This proves (i). For the proofs of (ii), (iii) and (iv), we may assume that x ≥ k 7
4 for
25 ≤ k ≤ 70, x ≥ k2 for 13 ≤ k ≤ 24 and x ≥ k 9
4 for k = 10, 11, 12, respectively, and arrive at a
contradiction. □

The next four lemmas show that under the hypothesis of Theorem 4.1.1, k is bounded. Further
we show that Theorem 4.1.1 (a) is valid for primes k if x ≤ 29
12 k − 1 and Theorem 4.1.1 (b) is valid
for all k ∈ K where
 K = K1 ∪ {k∣
∣k ≥ 10 and 2k − 1 is a prime}.(4.2.19)

Lemma 4.2.6. (a) Let k ≥ 19 be a prime, 2k ≤ x ≤ 29
12 k − 1 and (x, k) /∈ S3. Then Theorem
4.1.1(a) is valid.
(b) Let k ≥ 10, 29
12 k − 1 < x < 3k. Then Theorem 4.1.1(b) holds for all k ∈ K.

Proof. Let 2k ≤ x < 3k. We observe that every prime p with k ≤ x − k < p ≤ x is a term of
∆′. Since k > x−k
2 , we also see that 2p is a term in ∆′ for every prime p with k < p ≤ x
2 . Thus

W (∆′) ≥ π(x) − π(x − k) + π ( x
2
 ) − π(k).(4.2.20)

The contribution of π( x
2 ) − π(k) in the above expression is necessary to get an upper bound for k
which is not very large.
(a) Let 2k ≤ x ≤ 29
12 k − 1 with (x, k) /∈ S3. We will show that (4.2.3) holds. Let (2 + t1)k ≤ x <
(2 + t2)k with 0 ≤ t1 < t2 ≤ 1 and t2 − t1 ≤ 1
4 . Then we have from (4.2.20) that

W (∆′) ≥ π(2k + t1k) − π(k + t2k) + π(k + t1k
2 ) − π(k).

4.2. LEMMAS 25

Hence it is enough to prove

π((2 + t1)k) − π((1 + t2)k) + π((1 + t1
2 )k) − π(k) − [ 3
4 π(k)
] + 1 ≥ 0.(4.2.21)

Using Lemma 3.1.2 (i), (ii) and

log Y
log Z = 1 + log( Y
Z )
log Z and log Y
log Z − 1 = 1 + 1 + log( Y
Z )
log Z − 1 ,

we see that the left hand side of (4.2.21) is at least

2∑

i=1 b ( 2 + t1
i k) − a((1 + t2)k) − 7
4 a(k) + 1

= k
(log(2 + t1)k)2
 {f (k, t1, t2) − g(k, t1, t2) − 7
4 g(k, t1, 0)
} + 1

(4.2.22)

for k ≥ 5393, where

f (k,t1,t2) = (1.5t1 −t2 + 1
4 )(log(2 + t1)k)+
 2∑

i=1
 (2 + t1)(1+log i)
i
 (
1 + 1+log i
log((2+t1)k/i)−1

)

and
 g(k,t1,t2) = (1+t2)
 (

1 + log( 2+t1
1+t2 )

log((1 + t2)k)

)(

1.2762+log (
2 + t1
1 + t2
) + 1.2762 log( 2+t1
1+t2 )

log((1 + t2)k)
 )
 .

Then we have

kf ′(k, t1, t2) = (1.5t1 − t2 + 1
4 ) −
 2∑

i=1
 ( 2 + t1
i
 ) ( 1 + log i
log((2 + t1)k/i) − 1
 )2 .

We write
 1.5t1 − t2 + 1
4 = 0.5t1 − (t2 − t1) + 1
4

to observe that the left hand side is positive unless (t1, t2) = (0, 1
4 ) and we shall always assume that
(t1, t2) ̸= (0, 1
4 ).
Let k0 = k0(t1, t2) be such that kf ′(k, t1, t2) is positive at k0. Since kf ′(k, t1, t2) is an increasing
function of k, we see that f (k, t1, t2) is also an increasing function of k for k ≥ k0. Also g(k, t1, t2)
is a decreasing function of k. Hence (4.2.22) is an increasing function of k for k ≥ k0. Let k1 =
k1(t1, t2) ≥ k0 be such that (4.2.22) is non-negative at k1. Then (4.2.21) is valid for k ≥ k1. For
k < k1, we check inequality (4.2.21) by using the exact values of π(ν). Again for k not satisfying
(4.2.21), we take x = 2k + r with t1k ≤ r < t2k and check that the right hand side of (4.2.20) is at
least the right hand side of (4.2.3).
Let 2k ≤ x < 49
24 k. Then t1 = 0, t2 = 1
24 and we ﬁnd k1 = 5393 by (4.2.22). For k < 5393 and k
prime, we check that (4.2.21) holds except at the following values of k:
{
19, 47, 71, 73, 83, 89, 103, 107, 109, 113, 151, 167, 173, 191, 193, 197,
199, 269, 271, 277, 281, 283, 293, 449, 463, 467, 491, 503, 683, 709.

Thus (4.2.3) is valid for all primes k except at above values of k. For these values of k, we take
x = 2k + r with 0 ≤ r < k
24 and show that the right hand side of (4.2.20) is at least the right hand
side of (4.2.3) except at (x, k) /∈ S3.
We divide the interval [ 49
24 k, 29
12 k) into following subintervals
[ 49
24 k, 25
12 k) , [ 25
12 k, 13
6 k) , [ 13
6 k, 9
4 k) , [ 9
4 k, 19
8 k) and [ 19
8 k, 29
12 k) .

26 4. PROOF OF THEOREMS 1.2.1 AND 1.2.4

We ﬁnd k1 = 5393 for each of these intervals. For k < 5393 and k prime, we check that (4.2.21)
holds except at following values of k for the intervals:
[ 49
24 k, 25
12 k) :
 {
19, 47, 67, 71, 73, 79, 83, 103, 107, 109, 113, 131, 151, 167, 181, 199,
211, 263, 271, 277, 293, 467, 683
[ 25
12 k, 17
8 k) : {
19, 71, 83, 101, 103, 107, 113, 179, 181, 199, 257, 281, 283, 467, 683
[ 17
8 k, 13
6 k) : {
19, 37, 47, 61, 73, 89, 113, 197
[ 13
6 k, 9
4 k) : {
19, 43, 61, 67, 83, 89, 113, 139, 193, 197, 199, 257, 281, 283

[ 9
4 k, 19
8 k) :
 {
19, 23, 31, 43, 47, 61, 79, 83, 109, 113, 139, 151, 167, 193, 197, 199,
239, 283, 359

and there are no exceptions for the subinterval [ 19
8 k, 29
12 k). Now we apply similar arguments as in
the case 2k ≤ x < 49
24 k to each of the above subintervals to complete the proof.
For the proof of (b), we divide 29
12 k − 1 < x < 3k into subintervals ( 29
12 k − 1, 5
2 k), [ 5
2 k, 21
8 k),[ 21
8 k, 11
4 k) and [ 11
4 k, 3k). We apply the arguments of (a) to each of these subintervals to conclude
that the right hand side of (4.2.20) is at least the right hand side of (4.2.4). Infact we have the
inequality
 π((2 + t1)k) − π((1 + t2)k) + π((1 + t1
2 )k) − π(k) − M (k) ≥ 0(4.2.23)

analogous to that of (4.2.21). As in (a), using (4.2.1), we derive that k1 = 5393 in each of these
intervals. For k < 5393 and k ∈ K, we check that (4.2.23) hold except at the following values of k
for the intervals:( 29
12 k − 1, 5
2 k): {54, 55, 57, 73, 79, 142},[ 5
2 k, 21
8 k): {12, 52, 55, 70},[ 21
8 k, 11
4 k): {22, 27}[ 11
4 k, 3k): {10, 12, 19, 21, 22, 24, 37, 54, 55, 57, 59, 70, 91, 100, 121, 142, 159}.
Now we proceed as in (a) to get the required result. □

Lemma 4.2.7. Let k ∈ K and 3k ≤ x < 7k. Then Theorem 4.1.1 (b) is valid.

We prove a stronger result that Theorem 4.1.1 (b) holds for all k ≥ 29000 and for k ∈ K.

Proof. Let 3k ≤ x < 7k. We show that (4.2.4) holds. Let (s + t1)k ≤ x < (s + t2)k with
integers 3 ≤ s ≤ 6 and t1, t2 ∈ {0, 1
4 , 1
2 , 3
4 , 1} such that t2 − t1 = 1
4 . Then ∆′ contains a term equal
to ip with x−k
i < p ≤ x
i for each i with 1 ≤ i < s and a term equal to sp for k < p ≤ x
s . Therefore

W (∆′) ≥
 s−1∑

i=1
 (π ( x
i
 ) − π ( x − k
i
 )) + π ( x
s
 ) − π(k).(4.2.24)

Since x ≥ (s + t1)k and x − k < (s − 1 + t2)k, we observe from (4.2.24) that

W (∆′) ≥
 s−1∑

i=1
 (π ( s + t1
i k) − π ( s − 1 + t2
i k)) + π ( s + t1
s k) − π(k).

Hence it is enough to show

s−1∑

i=1
 (π ( s + t1
i k) − π ( s − 1 + t2
i k)) + π ( s + t1
s k) − π(k) − M (k) ≥ 0.(4.2.25)
 4.2. LEMMAS 27

Using (4.2.1) and Lemma 3.1.2 (i), (ii), we see that the left hand side of (4.2.25) is at least

s−1∑

i=1
 (b ( s + t1
i k) − a ( s − 1 + t2
i k)) + b ( s + t1
s k) − a(2k)

= k
(log(s + t1)k)2
 {

F (k, s, t1, t2) −
 s−1∑

i=1 G(k, s, t1, t2, i) − G(k, s, t1, 1, s
2 )

}(4.2.26)

for k ≥ 5393, where

F (k, s, t1, t2) =
 (s−1∑

i=1
 ( 1 + t1 − t2
i
 ) + t1
s − 1
)
 (log(s + t1)k) +

+
 s∑

i=1
 (s + t1)(1 + log i)
i
 (1 + 1 + log i
log((s + t1)k/i) − 1
 )

and
 G(k, s, t1, t2, i) = ( s − 1 + t2
i
 ) 

1 + log ( (s+t1)i
s−1+t2
 )

log ( s−1+t2
i k)
 

 ×



1.2762 + log ( (s + t1)i
s − 1 + t2
 ) + 1.2762 log ( (s+t1)i
s−1+t2
 )

log ( s−1+t2
i k)
 

 .

Then
 kF ′(k,s,t1,t2) =
 (s−1∑

i=1
(
1 + t1 − t2
i
 ) + t1
s − 1

)
−
 s∑

i=1
 (s + t1)
i
 ( 1 + log i
log((s + t1)k/i) − 1

)2 .

If s = 2, we note that F and G are functions similar to f and g appearing in Lemma 4.2.6. As
in Lemma 4.2.6, we ﬁnd K1 := K1(s, t1, t2) such that (4.2.26) is non negative at k = K1 and it is
increasing for k ≥ K1. Hence (4.2.25) is valid for k ≥ K1. For k < K1, we check inequality (4.2.25)
by using the exact values of π function in (4.2.25) for k with 2k − 1 prime or primes k given by
(4.2.2). Again for k not satisfying (4.2.25), we take x = sk + r with t1k ≤ r < t2k and check that
the right hand side of (4.2.24) is at least the right hand side of (4.2.4).
Let 3k ≤ x < 13
4 k. Here t1 = 0, t2 = 1
4 and and we ﬁnd K1 = 29000. We check that (4.2.25)
holds for 3 ≤ k < 29000 except at k = 10, 12, 19, 22, 40, 42, 52, 55, 57, 100, 101, 126, 127, 142. For
these values of k, putting x = 3k + r with 0 ≤ r < 1
4 k , we show that the right hand side of (4.2.24)
is at least the right hand side of (4.2.4). Hence the assertion follows in 3k ≤ x < 13
4 k. For x ≥ 13
4 k,
we apply similar arguments to intervals (s + t1)k ≤ x < (s + t2)k with integers 3 ≤ s ≤ 6 and
t1, t2 ∈ {0, 1
4 , 1
2 , 3
4 , 1} such that t2 − t1 = 1
4 . We ﬁnd K1 = 5393 for each of these intervals except for
6k ≤ x < 25
4 k where K1 = 5500. □

In view of Lemmas 4.2.6 and 4.2.7, it remains to prove Theorem 4.1.1 for x ≥ 7k which we
assume. Further we may also suppose (4.2.14). Otherwise (4.1.3) follows. Now we derive from
Lemma 4.2.5 that x < k 9
4 . On the other hand, we prove x ≥ k 9
4 . This is a contradiction. We split
the proof of x ≥ k 9
4 in the following two lemmas.

Lemma 4.2.8. Let k ∈ K. Assume (4.1.1), (4.2.14) with x ≥ 7k. Then x ≥ k 3
2 .

Proof. We prove it by contradiction. We assume (4.1.1), (4.2.14) and 7k ≤ x < k 3
2 . Then
k ≥ 50. Further by Corollary 4.2.4 and (x
k) ≥ (7k
k ), we have
(7k
k
 ) < (2.83)
k+k 3
4 k 3
2 (M (k)−1)(4.2.27)

28 4. PROOF OF THEOREMS 1.2.1 AND 1.2.4

since x < k 3
2 . We observe from Lemma 3.1.7 that
(7k
k
 ) = (7k)!
k!(6k)! >
 √14πkexp
−7k(7k)
7kexp 1
84k+1
√2πkexp−kkkexp 1
12k √12πkexp−6k(6k)6kexp 1
72k

> 0.4309
√k exp 1
84k+1 − 7
72k (17.65)
k.

Combining this with (4.2.27), we get

1 > exp (log(0.4309k) + 1
84k + 1 − 7
72k
 ) (17.65)
k(2.83)
−k−k 3
4 k− 3
2 M (k).(4.2.28)

Using (4.2.1), Lemma 1(i), (ii) and exp
( log(0.4309k)
k + 1
84k2+k − 7
72k2 ) ≥ 1, we derive for k ≥ 5393
that
 1 > 6.2367(2.83)
−k− 1
4 k− 3
log 2k (1+ 1.2762
log 2k )+ 3
2(log k−1)

> 6.2367 exp ( 3
2 + 3
2 log k − 2
 ) (2.83)
−k− 1
4 k− 3
log 2k (1+ 1.2762
log 2k )

> 27.95(2.83)
−k− 1
4 k− 3
log 2k (1+ 1.2762
log 2k ) := h(k)

since exp
( 3
2 log k−2 ) > 1 for k ≥ 3. We see that h(k) is an increasing function of k and h(k) > 1 at

k = 5393. Therefore k < 5393. By using the exact values of M (k), we now check that (4.2.28) does
not hold for 50 ≤ k < 5393 and k ∈ K. □

Lemma 4.2.9. Let k ∈ K. If (4.1.1) and (4.2.14) hold and x ≥ k 3
2 , then x ≥ k 9
4 .

Proof. We prove by contradiction. Assume (4.1.1), (4.2.14) and k 3
2 ≤ x < k 9
4 . We derive from
Lemma 4.2.5 that k ≤ 70. Let k = 10, 11, 12, 13. By Lemmas 4.2.5, 4.2.7 and 4.2.8, we can take
max(7k, k 3
2 ) ≤ x < k 9
4 for k = 10, 11, 12 and max(7k, k 3
2 ) ≤ x < k2 for k = 13. For these values of
x and k, we ﬁnd that
 W (∆′) ≥
 6∑

i=1
 (π ( x
i
 ) − π ( x − k
i
 )) ≥ M (k)

contradicting (4.2.14).
Therefore we assume that k ≥ 14. Let k 3
2 ≤ x < k 25
16 . By Lemma 4.2.7 and 4.2.8, we can take
x ≥ max(7k, k 3
2 ) so that we can assume k ≥ 32. Then
(x
k
) ≥ (max(7k, ⌈k 3
2 ⌉)
k
 )

where ⌈ν⌉ denotes the least integer ≥ ν. From (4.2.7), we have ordp(
(x
k)) ≤ [ log x
log p ] ≤ [ 25
16 log k
log p ] and
hence (x
k
) ≤
 


π(k)∏

i=1 p
h 25
16 log k
log pi
 i

i
 

 x
k−µ <
 


π(k)∏

i=1 p
h 25
16 log k
log pi
 i

i
 

 k 25
16 (M (k)−1)

by (4.2.14). Combining the above estimates for (x
k), we get

(max(7k, ⌈k 3
2 ⌉)
k
 ) <
 


π(k)∏

i=1 p
h 25
16 log k
log pi
 i

i
 

 k 25
16 (M (k)−1)

which is not possible for 32 ≤ k ≤ 70. By similar arguments, we arrive at a contradiction for
max(7k, k 25
16 ) ≤ x < k 26
16 in 23 ≤ k ≤ 70, max(7k, k 26
16 ) ≤ x < k 27
16 in 17 ≤ k ≤ 70 and max(7k, k 27
16 ) ≤

4.3. PROOF OF THEOREM 4.1.1 29

x < k 7
4 in 14 ≤ k ≤ 70 except at k = 16. Let k = 16 and max(7k, k 27
16 ) ≤ x < k 7
4 . Then we observe
that
 W (∆′) ≥
 6∑

i=1
 (π ( x
i
 ) − π ( x − 16
i
 )) ≥ 5 = M (16)

contradicting (4.2.14).
Now we consider x ≥ k 7
4 . We observe that k 7
4 ≥ 7k since k ≥ 14. Further we derive from
Lemma 4.2.5 that k ≤ 24. We apply similar arguments for 14 ≤ k ≤ 24 as above to arrive at a
contradiction in the intervals k 7
4 ≤ x < k 15
8 except at k = 16, k 15
8 ≤ x < k 31
16 and k 31
16 ≤ x < k2.
The case k = 16 and k 7
4 ≤ x < k 15
8 is excluded as earlier. □

4.3. Proof of Theorem 4.1.1

Suppose that the hypothesis of Theorem 4.1.1 (b) is valid and k ≥ 10. By Lemmas 4.2.6 (b),
4.2.7, 4.2.8 and 4.2.9, we see that Theorem 4.1.1 (b) is valid for all k ∈ K. Thus (4.2.4) holds for
all k ∈ K and x > 29
12 k − 1. Let k /∈ K and k1 < k be the largest integer with 2k1 − 1 prime. Then
k1 ≥ 10. For x > 29
12 k − 1 > 29
12 k1 − 1, we see that (4.2.4) is valid at (x, k1). By Lemma 4.2.2 (ii),
(4.2.4) is valid at (x, k) too. Hence Theorem 4.1.1 (b) is valid for all k.
Suppose that the hypothesis of Theorem 4.1.1 are satisﬁed and k ≥ 19. We have from Lemma
4.2.6 (a) that (4.2.3) holds for (x, k) with k prime, x ≤ 29
12 k − 1 and (x, k) /∈ S3. By Theorem
4.1.1(b), (4.2.4) and hence (4.2.3) is valid for all k and x > 29
12 k − 1. Thus (4.2.3) holds for (x, k)
with k prime and (x, k) /∈ S3. Let k be a composite number and k′ < k be the greatest prime. Then
k′ ≥ 19. Suppose (x, k′) /∈ S3. Then (4.2.3) is valid at (x, k′) and hence valid at (x, k) by Lemma
4.2.2 (i). Suppose now that (x, k′) ∈ S3. Then we check the validity of (4.2.3) at (x, k). We see
that (4.2.3) does not hold only if (x, k) ∈ S3. We explain this with two examples. Let k = 20.
Then k′ = 19. Since (42, 19) ∈ S3, we check the validity of (4.2.3) at (42, 20) which is true. Hence
(42, 20) /∈ S3. Again let k = 72. Then k′ = 71. Since (145, 71) ∈ S3, we check the validity of (4.2.3)
at (145, 72) and see that (4.2.3) does not hold at (145, 72) which is an element of S3. This completes
the proof. □

CHAPTER 5

Grimm’s Conjecture for consecutive integers:
Proof of Theorem 1.2.6

In this chapter, we prove Theorem 1.2.6.

5.1. Introduction

We recall that N0 = 8.5 × 108. For the proof of Theorem 1.2.6, it suﬃces to prove the following.

Theorem 5.1.1.
Grimm’s Conjecture is valid when n = pN + 1 and k = k(N ) = pN +1 − pN − 1 for 1 < N ≤ N0.

For the proof of Theorem 5.1.1, we verify the conjecture of Cramer whenever N ≤ N0. We have

Lemma 5.1.2. Let k(N ) = pN +1 − pN − 1. Then

k(N ) < (log pN )
2 for N ≤ N0.(5.1.1)

We observe that (5.1.1) can be sharpened for several values of N and this is important for the
value of N0 in Theorem 1.2.6. We also apply the following result of Phillip Hall [22] on distinct
representations.

Lemma 5.1.3. A family F = {Si : i ∈ I} of ﬁnite subsets of a set E possesses a system of
distinct representatives if and only if for every ﬁnite subset J if I, the number of elements in J does
not exceed the number of elements of in the set ∪j∈J Sj.

5.2. Proof of Theorem 5.1.1

Let 1 < N ≤ N0. We put n = pN + 1 and k = k(N ) = pN +1 − pN − 1. We check that Theorem
5.1.1 is valid for N ≤ 9. Thus we may suppose that 10 ≤ N ≤ N0. Assume that the assertion of
Theorem 5.1.1 is not valid. Now we apply Lemma 5.1.3. Since Grimm’s conjecture is not valid, we
derive from Lemma 5.1.3 that there exists t > 0 and integers pN < n0 < n1 < · · · < nt < n + k =
PN +1 with
 ω(n0n1 · · · nt) ≤ t.(5.2.1)

Let t = t(N ) be minimal in the above assertion. Then P (ni) < k for 0 ≤ i ≤ t and (5.2.1) holds with
equality sign. We apply a fundamental argument of Sylvester and Erd˝os. For every prime divisor p
of n0n1 · · · nt, we take an nip such that p does not appear to a higher power in the factorisation of
any element of {n0, n1, · · · , nt} =: S. By deleting all nip with p dividing n0n1 · · · nt in S, we are left
with at least one ni0 ∈ S. If pν is the highest power of a prime p dividing ni0, then pν also divides
nip and hence it divides |ni0 − nip| < k. Therefore

pN < ni0 < kt(5.2.2)

since ω(ni0) ≤ t. By Lemma 5.1.2, we getlog pN
log log pN < 2t(N ).(5.2.3)

We see that the left hand side of (5.2.3) is an increasing function of N . For i ≥ 2, let Ni be the
largest integer N such that log pN
log log pN < 2i.

32 5. GRIMM’S CONJECTURE FOR CONSECUTIVE INTEGERS: PROOF OF THEOREM 1.2.6

Then we calculate
 N2 = 727, N3 = 1514619, N4 = 8579289335.(5.2.4)

Let Ar and Mr be deﬁned by

A2r−1 = ∏

pα<2r−1≤pα+1 pα, M2r−1 = π(A2r−1).

Then

Lemma 5.2.1. Suppose that Theorem 5.1.1 is not valid at N with N > M2r−1. Then k(N ) >
2r − 1.

Proof. Assume that k(N ) = pN +1 − pN − 1 ≤ 2r − 1. Since Theorem 5.1.1 is not valid, (5.2.1)
holds for some t and hence there exists a term ¯n such that

pN < ¯n ≤ A2r−1.

This is a contradiction since N > M2r−1. □

We compute M2r−1 for some values of r :

M11 = 368, M13 = 3022, M15 = 30785, M17 = 58083, M19 = 803484,

M21 = M23 = 12787622, M25 = 250791570.

Let
 SN = {pN + i : P (pN + i) < k, 1 ≤ i ≤ k}

and put t′ = t′(N ) = |SN |. We see that t′ ≥ t + 1. For the proof of Theorem 5.1.1, it suﬃces to
ﬁnd distinct prime divisors of the elements of SN since a prime ≥ k divides at most one pN + i with
1 ≤ i ≤ k.
First we consider N ≤ N2. Let t = 1. Then there are 1 ≤ j < i ≤ k and a prime p such that
pN + i = pα and pN + j = pβ. This gives

pN + j = pβ ≤ pβ(pα−β − 1) = i − j < k = pN +1 − pN − 1

implying 2pN < pN +1−1, a contradiction. Let t = 2. Then (5.2.2) holds only when N = 30. We have
S30 = {120, 121, 125, 126} and we choose 3, 11, 5 and 7 as distinct prime divisors of 120, 121, 125 and
126, respectively. Therefore the assertion of Theorem 5.1.1 holds for N = 30. Thus t ≥ 3 implying
t′ ≥ t + 1 ≥ 4. Now, by calculating t′, we see that N = 30, 99, 217, 263, 327, 367, 457, 522, 650 and
we verify the assertion of Theorem 5.1.1 as above in each of these values of N .
Hence N > N2. Therefore t ≥ 3 by the deﬁnition of N2 and thus t′ ≥ 4. Next we consider
N2 < N ≤ N3. We divide this interval into the following subintervals:

I11 = (N2, M13], I13 = (M13, M15], I15 = (M15, M17], I17 = (M17, M19], I19 = (M19, N3].

By Lemma 5.2.1, we restrict to those N for which k(N ) > 2r−1 whenever N ∈ I2r−1 with 6 ≤ r ≤ 10.
Let t = 3. By (5.2.2) and t′ ≥ 4, we ﬁnd that N is one of the following:

757, 1183, 1229, 1315, 1409, 1831, 1879, 2225, 2321, 2700, 2788, 2810, 3302, 3385,

3427, 3562, 3644, 3732, 3793, 3795, 3861, 4009, 4231, 4260, 4522, 4754, 5349, 5949,

6104, 6880, 9663, 9872, 10229, 10236, 11214, 11684, 12542, 14357, 14862, 15783,

16879, 17006, 17625, 18266, 19026, 19724, 23283, 23918, 25248, 28593, 31545, 31592,

33608, 34215, 38590, 40933, 44903, 47350, 66762, 104071, 118505, 126172, 141334, 149689.

Let P (SN ) = {P (pN + i) : pN + i ∈ SN }. For the proof of Theorem 5.1.1, we may suppose that

|P (SN )| < |SN |.(5.2.5)

In view of (5.2.5), all above possibilities for N other than the following are excluded:
1409, 1831, 2225, 2788, 3302, 3385, 3562, 3644, 4522,

14862, 16879, 17006, 23283, 28593, 34215, 104071.
(5.2.6)
 5.2. PROOF OF THEOREM 5.1.1 33

Let N be given by (5.2.6). We check that |P (SN )| = |SN | − 1. Let (i, j) with i < j be the unique
pair satisfying P (pN + i) = P (pN + j). We check that ω(pN + i) ≥ 2. Now we take Pµ = P (pN + µ) if
µ ̸= i and Pi to be the least prime divisor of pN + i. Thus all the possibilities in (5.2.6) are excluded.
Therefore t ≥ 4 implying t′ ≥ 5. If pN < k3, then N is already excluded. Consequently we suppose
that pN ≥ k3. Now we calculate t′ to ﬁnd that N is one of the following:

11159, 19213, 30765, 31382, 40026, 42673, 51943, 57626, 65274, 65320, 80413,

81426, 88602, 106286, 184968, 189747, 192426, 212218, 245862, 256263, 261491,

271743, 278832, 286090, 325098, 327539, 405705, 415069, 435081, 484897, 491237,

495297, 524270, 528858, 562831, 566214, 569279, 629489, 631696, 822210, 870819,

894189, 938452, 1036812, 1150497, 1178800, 1319945, 1394268, 1409075.

By (5.2.5), it suﬃces to restrict N to

57626, 65320, 80413, 106286, 271743, 415069, 822210.

These cases are excluded as in (5.2.6).
Thus we may assume that N > N3. Then t ≥ 4 by the deﬁnition of N3 and t′ ≥ 5. We divide
the interval (N3, N0] into the following subintervals:

J19 = (N3, M23], J23 = (M23, N0].

By Lemma 5.2.1, we restrict to those N for which k(N ) > 2r − 1 whenever N ∈ J2r−1, r = 10, 12.
By calculating t′, we ﬁnd that N is one of the following:

1515930, 1539264, 1576501, 1664928, 2053917, 2074051, 2219883, 2324140,

2341680, 2342711, 2386432, 2775456, 2886673, 3237613, 3695514, 5687203,

6169832, 6443469, 6860556, 7490660, 7757686, 8720333, 9558616, 10247124,

10600736, 10655462, 11274670, 11645754, 12672264, 13377906, 14079145,

14289335, 18339279, 24356055, 28244961, 33772762, 42211295, 53468932,

64955634, 110678632, 118374763, 231921327, 264993166, 398367036.

By (5.2.5), it suﬃces to consider only the following values of N :

1539264, 2053917, 2775456, 12672264, 110678632

which are excluded as in (5.2.6). This completes the proof of Theorem 5.1.1. □

CHAPTER 6

Reﬁnement of Sylvester’s theorem on the greatest prime
divisor of a product of consecutive integers: Proof of
Theorems 1.3.1, 1.3.3 and Corollary 1.3.2

In this chapter we prove Theorems 1.3.1, 1.3.3 and Corollary 1.3.2. We give a sketch of the
proof. For k = 2, 4, we use a particular case of Catalan’s equation to get the assertion. For k = 3
and 5 ≤ k ≤ 8, we use estimates on ω(∆(n, k) given by (1.2.3). For 9 ≤ k ≤ 16, we ﬁrst bound n and
the assertion follows by a computational argument. For k > 17, we use arguments similar to that of
proving Theorem 1.2.1 and the number of primes in intervals (X, (1 + θ)X] with 0 < θ < e − 1.

6.1. Lemmas

We begin with a well known result due to Levi ben Gerson on a particular case of Catalan
equation.

Lemma 6.1.1. The solutions of

2a − 3b = ±1 in integers a > 0, b > 0

are given by (a, b) = (1, 1), (2, 1), (3, 2).

Lemma 6.1.2. We have

pi+1 − pi <
 




35 for pi ≤ 5591
15 for pi ≤ 1123, pi ̸= 523, 887, 1069
21 for pi = 523, 887, 1069
9 for pi ≤ 361, pi ̸= 113, 139, 181, 199, 211, 241, 283, 293, 317, 337.

(6.1.1)

Lemma 6.1.3. Let N be a positive real number and k0 a positive integer. Let I(N, k0) = {i|pi+1 −
pi ≥ k0, pi ≤ N}. Then
 P (n(n + 1) · · · (n + k − 1)) > 2k

for 2k ≤ n < N and k ≥ k0 except possibly when pi < n < n + k − 1 < pi+1 for i ∈ I(N, k0).

Proof. Let 2k ≤ n < N and k > k0. We may suppose that none of n, n + 1, · · · , n + k − 1
is a prime, otherwise the result follows. Let pi < n < n + k − 1 < pi+1. Then i = π(n) and
pπ(n) < n < N. For π(n) /∈ I(N, k0), we have

k − 1 = n + k − 1 − n < pπ(n)+1 − pπ(n) < k0
which implies k − 1 < k0 − 1, a contradiction. Hence the assertion. □

Lemma 6.1.4. Let X > 0 and 0 < θ < e − 1 be real numbers. For l ≥ 0, let

X0 = max ( 5393
1 + θ , exp( log(1 + θ) + 0.2762
θ )
) ,

Xl+1 = max
 ( 5393
1 + θ , exp( log(1 + θ) + 0.2762)

θ + 1.2762(1−log(1+θ))
log2 Xl )

)
 .

Then we have
 π((1 + θ)X) − π(X) > 0

35

36 6. PROOF OF THEOREMS 1.3.1, 1.3.3 AND COROLLARY 1.3.2

for X > Xl.

Proof. Let l ≥ 0 and X > Xl. Then (1 + θ)X ≥ 5393. By Lemma 3.1.2, we have

δ := π((1 + θ)X) − π(X) ≥ (1 + θ)X
log(1 + θ)X − 1 − X
log X
 (1 + 1.2762
log X
 )

≥ X
log(1 + θ)X − 1
 {1 + θ − log(1 + θ)X − 1
log X
 (1 + 1.2762
log X
 )}

≥ X
log(1 + θ)X − 1
 {1 + θ − (1 − 1 − log(1 + θ)
log X
 ) (
1 + 1.2762
log X
 )}

≥ X
log(1 + θ)X − 1 {F (X) + G(X)}

where F (X) = θ − log(1+θ)+0.2762
log X and G(X) = 1.2762(1−log(1+θ))
log2 X . We see that G(X) > 0 and
decreasing since 0 < θ < e − 1. Further we observe that {Xi} is a non-increasing sequence. We
notice that δ > 0 if F (X) + G(X) > 0. But F (X) + G(X) > F (X) > 0 for X > X0 by the
deﬁnition of X0. Thus δ > 0 for X > X0. Let X ≤ X0. Then F (X) + G(X) ≥ F (X) + G(X0) and
F (X) + G(X0) > 0 if X > X1 by the deﬁnition of X1. Hence δ > 0 for X > X1. Now we proceed
inductively as above to see that δ > 0 for X > Xl with l ≥ 2. □

Lemma 6.1.5. Let n > k and k ≤ 16. Then

P (∆(n, k)) ≤ 2k(6.1.2)

implies that (n, k) ∈ {(8, 2), (8, 3)} or (n, k) ∈ [k + 1, k] for k ∈ {2, 3, 5, 6, 8, 9, 11, 14, 15} or (n, k) ∈
[k + 1, k, 3] for k ∈ {4, 7, 10, 13} or (n, k) ∈ [k + 1, k, 5] for k ∈ {12, 16}.

Proof. We apply Lemma 6.1.1 to derive that (6.1.2) is possible only if n = 3, 8 when k =
2 and n = 5, 6, 7 when k = 4. For the latter assertion, we apply Lemma 6.1.1 after securing
P ((n + i)(n + j)) ≤ 3 with 0 ≤ i < j ≤ 3 by deleting the terms divisible by 5 and 7 in n, n + 1, n + 2
and n + 3. For k = 3 and 5 ≤ k ≤ 8, the assertion follows from (1.2.3).
Thus we may assume that k ≥ 9. Assume that (6.1.2) holds. Then there are at most 1 + [ k−1
p ]
terms divisible by the prime p. After removing all the terms divisible by p ≥ 7, we are left with
at least 4 terms only divisible by 2, 3 and 5. Further out of these terms, for each prime 2, 3 and
5, we remove a term in which the prime divides to a maximal power. Then we are left with
a term n + i such that n ≤ n + i ≤ 8 × 9 × 5 = 360. Let n ≥ 2k. We now apply Lemma
6.1.3 with N = 361, k0 = 9 and (6.1.1) to get P (∆(n, k)) > 2k for k ≥ 9 except possibly when
pi < n < n + k − 1 < pi+1, pi = 113, 139, 181, 199, 211, 241, 283, 293, 317, 337. For these values of n,
we check that P (∆(n, k)) > 2k is valid for 9 ≤ k ≤ 16. Thus it suﬃces to consider k < n < 2k. We
calculate P (∆(n, k)) for (n, k) with 9 ≤ k ≤ 16 and k < n < 2k. We ﬁnd that (6.1.2) holds only if
(n, k) is given in the statement of the Lemma 6.1.5. □

Lemma 6.1.6. Assume (4.1.1) and

µ ≥ k − π(2k) + π(k).(6.1.3)

Then we have
 x < k 3
2 for k ≥ 87; x < k 7
4 for k ≥ 40; x < k2 for k ≥ 19.(6.1.4)

Lemma 6.1.7. Let k ≥ 57. Assume (4.1.1), (6.1.3) with x ≥ 7k. Then x ≥ k 3
2 .

The proofs of Lemmas 6.1.6, 6.1.7 are similar to that of Lemmas 4.2.5, 4.2.8, respectively.

6.2. Proof of Theorem 1.3.3 (a)

Let n > max(k + 13, 279
262 k). In view of Lemma 6.1.5, we may take k ≥ 17 since n ≤ k + 5 for the
exceptions (n, k) given in Lemma 6.1.5. It suﬃces to prove (1.3.3) for k such that 2k − 1 is prime.

6.3. PROOF OF THEOREM 1.3.3 (b) 37

Let k1 < k2 be such that 2k1 − 1 and 2k2 − 1 are consecutive primes. Suppose (1.3.3) holds at k1.
Then for k1 < k < k2, we have

P (n(n + 1) · · · (n + k − 1)) ≥ P (n · · · (n + k1 − 1)) > 2k1

implying P (∆(n, k)) ≥ 2k2 − 1 > 2k. Therefore we may suppose that k ≥ 19 since 2k − 1 with
k = 17, 18 are composites. We assume from now onward in the proof of Theorem 1.3.3 (a) that
2k −1 is prime. We may suppose ω(∆(n, k)) ≤ π(2k) otherwise (1.3.3) follows. We put x = n+k −1.
Then ∆(n, k) = x(x−1) · · · (x−k +1) and ω(x(x−1) · · · (x−k +1)) ≤ π(2k). Let f1 < f2 < · · · < fµ
be all the integers in [0, k) such that (4.1.1) holds. Then

µ ≥ k − π(2k) + π(k)(6.2.1)

Now we apply Lemmas 6.1.6 and 6.1.7 to get x < 7k for k ≥ 87. Putting back n = x − k + 1 and
using (6.1.4), we may assume that n < 6k + 1 for k ≥ 87, n < k 7
4 − k + 1 for 40 ≤ k < 87 and
n < k2 − k + 1 for 19 ≤ k < 40.
Let k < 87. Suppose n ≥ 2k. Then 2k ≤ n < k 7
4 − k + 1 for 40 ≤ k < 87 and 2k ≤ n < k2 − k + 1
for 19 ≤ k < 40. Thus Lemma 6.1.3 with N = 87 7
4 − 87 + 1, k0 = 35 and (6.1.1) implies that
P (∆(n, k)) > 2k for k ≥ 35. We note here that 2k ≤ n < N for 35 ≤ k < 40. Let k < 35.
Taking N = 342 − 34 + 1, k0 = 21 for 21 ≤ k ≤ 34 and N = 192 − 19 + 1, k0 = 19 for k = 19,
we see from Lemma 6.1.3 and (6.1.1) that P (∆(n, k)) > 2k for k ≥ 19. Here the case k = 20 is
excluded since 2k − 1 is composite. Therefore we may assume that n < 2k. Further we observe that
π(n+k −1)−π(2k) ≥ π(2k +13)−π(2k) since n > k +13. Next we check that π(2k +13)−π(2k) > 0.
This implies that [2k, n + k − 1] contains a prime.
Thus we may assume that k ≥ 87. Then we write n = αk + 1 with 279
262 − 1
k < α ≤ 6 if k ≥ 201
and 1 + 12
k < α ≤ 6 if k < 201. Further we consider π(n + k − 1) − π(max(n − 1, 2k)) which is

= π((α + 1)k) − π(αk) for α ≥ 2

≥ π([ 541
262 k]) − π(2k) for α < 2 and k ≥ 201

≥ π(2k + 13) − π(2k) for α < 2 and k < 201.

We check by using exact values of π function that π(2k + 13) − π(2k) > 0 for k < 201 and π([ 541
262 k]) −
π(2k) > 0 for 201 ≤ k ≤ 2616. Thus we may suppose that k > 2616 if α < 2. Also [ 541
262 k] ≥ 540
262 k for
k > 2616. Now we apply Lemma 6.1.4 with X = αk, θ = 1
α , l = 0 if α ≥ 2 and X = 2k, θ = 4
131 , l = 1
if α < 2 to get π(n+k −1)−π(max(n−1, 2k)) > 0 for X > X0 = 5393
1+ 1
α if α ≥ 2 and X > X1 = 5393
1+ 4
131
if α < 2. Further when α < 2, we observe that X = 2k > X1 since k > 2616. Thus the
assertion follows for n < 2k. It remains to consider the case α ≥ 2 and X ≤ 5393(1 + 1
α )
−1.
Then 2k ≤ n < n + k − 1 = X(1 + 1
α ) ≤ 5393. Now we apply Lemma 6.1.3 with N = 5393, k0 = 35
and (6.1.1) to conclude that P (∆(n, k)) > 2k. □

6.3. Proof of Theorem 1.3.3 (b)

In view of Lemma 6.1.5 and Theorem 1.3.3 (a), we may assume that k ≥ 17 and k < n ≤ 279
262 k.
Let X = 279
262 k, θ = 245
279 , l = 0. Then for k < n ≤ X, we see from Lemma 6.1.4 that

π(2k) − π(n − 1) ≥ π((1 + θ)X) − π(X) > 0

for X > X0 = 5393(1 + θ)
−1 which is satisﬁed for k > 2696 since (1 + θ)X = 2k. Thus we may
suppose that k ≤ 2696. Now we check with exact values of π function that π(2k) − π( 279
262 k) > 0.
Therefore P (∆(n, k)) ≥ P (n(n + 1) · · · 2k) ≥ pπ(2k). Further we apply Lemma 6.1.4 with X = 1.97k,
θ = 3
197 and l = 25. We calculate that Xl ≤ 284000. We conclude by Lemma 6.1.4 that

π(2k) − π(1.97k) = π((1 + θ)X) − π(X) > 0

for k > 145000. Let k ≤ 145000. Then we check that π(2k) − π(1.97k) > 0 is valid for k ≥ 680 by
using the exact values of π function. Thus

pπ(2k) > 1.97k for k ≥ 680.(6.3.1)

38 6. PROOF OF THEOREMS 1.3.1, 1.3.3 AND COROLLARY 1.3.2

Therefore we may suppose that k < 680. Now we observe that for n > k+13, π(n+k−1)−π(1.97k) ≥
π(2k + 13) − π(1.97k) > 0, the latter inequality can be checked by using exact values of π function.
Hence the assertion follows since n < 1.97k. □

6.4. Proof of Theorem 1.3.1

By Theorem 1.3.3 (b), we may assume that n ≤ k + 13. Also we may suppose that k < 680
by (6.3.1). For k ≤ 16, we calculate P (∆(n, k)) for all the pairs (n, k) given in the statement of
Lemma 6.1.5. We ﬁnd that either P (∆(n, k)) > 1.95k or (n, k) is an exception stated in Theorem
1.3.3 (a). Thus we may suppose that k ≥ 17. Now we check that π(n + k − 1) − π(1.95k) > 0 except
for (n, k) ∈ [k + 1, k, h] for k ∈ Ah with 1 ≤ h ≤ 11 and the assertion follows. □

6.5. Proof of Corollary 1.3.2

We calculate P (∆(n, k)) for all (n, k) with k ≤ 270 and k + 1 ≤ n ≤ k + 11. This contains the
set of exceptions given in Theorem 1.3.1. We ﬁnd that P (∆(n, k)) > 1.8k unless (n, k) ∈ E0. Hence
the assertion (1.3.2) follows from Theorem 1.3.1. □

CHAPTER 7

Reﬁnement of an analogue of Sylvester’s theorem for
arithmetic progressions: Proof of Theorem 1.4.1

In this chapter, we prove Theorem 1.4.1. The proof of Theorem 1.4.1 depends on the sharpening
of the upper bound for P in the fundamental inequality of Sylvester and Erd˝os, see Lemma 7.1.1.
Further we also give a better lower bound for P, see (7.3.12). Comparing the upper and lower
bounds for P, we bound n, d and k. For the ﬁnitely many values of n, d, k thus obtained, we check
the validity of (1.4.11) on a computer. When d ≤ 7, we also need to use estimates on primes in
arithmetic progression given in Lemma 3.1.5. We apply these estimates to count the number of
terms of ∆ which are of the form ap where 1 ≤ a < d, gcd(a, d) = 1 and p > k, see Lemma 7.2.3.

7.1. Reﬁnement of fundamental inequality of Sylvester and Erd˝os

For 0 ≤ i < k, let
 n + id = BiB′
i(7.1.1)

where Bi and B′
i are positive integers such that P (Bi) ≤ k and gcd(B′
i, ∏

p≤kp) = 1. Let S ⊂

{B0, · · · , Bk−1}. Let p ≤ k be such that p ∤ d and p divides at least one element of S. Choose
Bip ∈ S such that p does not appear to a higher power in the factorisation of any other element of
S. Let S1 be the subset of S obtained by deleting from S all such Bip. Let P be the product of all
the elements of S1.
The following lemma gives an upper bound for P which is in fact a reﬁnement of fundamental
inequality of Sylvester and Erd˝os.

Lemma 7.1.1. Let S, S1, P be as above and let a
′ be the number of terms in S1 divisible by 2.
Also we denote
 n0 = gcd(n, k − 1)

and
 θ =
 {
1 if 2|n0
0 otherwise.
(7.1.2)

Then
 P ≤ n0∏

p∤d pordp((k−2)!).(7.1.3)

Further for d odd, we have
 P ≤ 2−θn02a
′+ord2([ k−2
2 ]!) ∏

p∤2d
pordp((k−2)!).(7.1.4)

Proof. Let p < k, p ∤ d be such that p divides at least one element of S. Let rp ≥ 0 be the
smallest integer such that p | n + rpd. Write n + rpd = pn1. Then

n + rpd, n + rpd + pd, · · · , n + rpd + p[ k − 1 − rp
p ]d

are all the terms in ∆ divisible by p. Let Brp+pip be such that p does not divide any other term
of S to a higher power. Let ap be the number of terms in S1 divisible by p. We note here that

39

40 7. PROOF OF THEOREM 1.4.1

ap ≤ [ k−1−rp
p ]. For any Brp+pi ∈ S1, we have ordp(Brp+pi) =ordp(n + rpd + pid) ≤ordp((n + rpd +
pid)) − (n + rpd + pipd)) = 1+ordp(i − ip). Therefore

(7.1.5) ordp(P) ≤ ap + ordp
 



[ k−1−rp
p ]
∏

i=0
i̸=ip
 (i − ip)




 ≤ ap + ordp
 (ip![ k − 1 − rp
p − ip]!
)

Thus
 ordp(P) ≤ ap + ordp([ k − 1 − rp
p ]!).(7.1.6)

Let p ∤ n. Then rp ≥ 1 and hence ap ≤ [ k−2
p ]. From (7.1.6), we have

ordp(P) ≤ [ k − 2
p ] + ordp([ k − 2
p ]!) = ordp((k − 2)!).(7.1.7)

Let p = 2. Then a2 = a
′ so that
 ord2(P) ≤ a
′ + ord2([ k − 2
2 ]!).(7.1.8)

Let p|n. Then rp = 0. Assume that p ∤ (k − 1). Then from (7.1.6), we have

ordp(P) ≤ ap + ordp([ k − 2
p ]!).(7.1.9)

Assume p|(k−1) and let i0 ∈ {0, k−1
p } with i0 ̸= ip be such that ordp(n+pi0d) =min (ordp(n),ordp(k−
1)). If ordp(n) =ordp(k − 1), we take i0 = 0 if ip ̸= 0 and i0 = k−1
p otherwise. From (7.1.5), we have

ordp(P) ≤ min(ordp(n), ordp(k − 1)) + ap − 1 + ordp
 



 k−1
p∏

i=0
i̸=i0,ip
(i − ip)




 .

Thus
 ordp(P) ≤ min(ordp(n), ordp(k − 1)) + ap − 1 + ordp(( k − 1 − p
p )!).(7.1.10)

From (7.1.9) and (7.1.10), we conclude

ordp(P) ≤ min(ordp(n), ordp(k − 1)) + [ k − 2
p ] + ordp([ k − 2
p ]!)

since ap ≤ [ k−1
p ]. Thus

ordp(P) ≤ min(ordp(n), ordp(k − 1)) + ordp((k − 2)!).(7.1.11)

Now (7.1.3) follows from (7.1.7) and (7.1.11). Let p = 2. By (7.1.9) and (7.1.10), we have in case of
even n that
 ord2(P) ≤ min(ord2(n), ord2(k − 1)) − θ + a
′ + ord2([ k − 2
2 ]!)

which, together with (7.1.7), (7.1.8) and (7.1.11), implies (7.1.8). □

The following Lemma is a consequence of Lemma 7.1.1.

Lemma 7.1.2. Let α ≥ 0 and m ≥ 0. Suppose W (∆) ≤ m. Then there exists a set T =
{n + ihd|0 ≤ h ≤ t, i0 < i1 < · · · < it} such that 1 + t := |T| ≥ k − m − πd(k) satisfying

dt ≤ n0
n
 ∏

p∤d pordp((k−2)!)

(α + i1) · · · (α + it) if n = αd(7.1.12)
 7.2. LEMMAS FOR THE PROOF OF THEOREM 1.4.1 (CONTD.) 41

and
 (n + i0d) · · · (n + itd)
2a ≤ 2−θn02ord2([ k−2
2 ]!) ∏

p∤2d
pordp((k−2)!) if d is odd(7.1.13)

where a is the number of even elements in T.

Proof. Let α > 0 be given by n = αd. Let S be the set of all terms of ∆ composed of primes
not exceeding k. Then |S| ≥ k − m. For every p dividing an element of S, we delete an f (p) ∈ S
such that
 ordp(f (p)) = max
s∈S ordp(s).

Then we are left with a set T with 1 + t := |T| ≥ k − m − πd(k) elements of S. Let

P :=
 t∏

ν=0(n + id) ≥ (n + i0d)(α + i1) · · · (α + it)dt.

We now apply Lemma 7.1.1 with S = S and S1 = T so that P = P. Thus the estimates (7.1.3) and
(7.1.4) are valid for P. Comparing the upper and lower bounds of P, we have (7.1.12) and further
(7.1.13) for d odd. □

7.2. Lemmas for the proof of Theorem 1.4.1 (contd.)

The following lemma is analogue of Lemma 4.2.2 (ii) for d > 1.

Lemma 7.2.1. Let k1 < k2 be such that 2k1 − 1 and 2k2 − 1 are consecutive primes. Suppose
(1.4.11) holds at k1. Then it holds for all k with k1 ≤ k < k2.

Proof. Assume that (1.4.11) holds at k1. Let k be as in the statement of the lemma. Then
π(2k1) = π(2k). From ∆(n, d, k) = n(n + d) · · · (n + (k1 − 1)d)(n + k1d) · · · (n + (k − 1)d), we have

W (∆(n, d, k)) ≥ W (∆(n, d, k1)) ≥ π(2k1) − πd(k1) − ρ ≥ π(2k) − πd(k) − ρ

since πd(k) ≥ πd(k1). □

Lemma 7.2.2. Let max(n, d) ≤ k. Let 1 ≤ r < k with gcd(r, d) = 1 be such that

W (∆(r, d, k)) ≥ π(2k) − ρ.

Then for each n with r < n ≤ k and n ≡ r(mod d), we have

W (∆(n, d, k)) ≥ π(2k) − ρ.

Proof. For r < n ≤ k, we write

∆(n, d, k) = r(r + d) · · · (r + (k − 1)d)(r + kd) · · · (n + (k − 1)d)
r(r + d) · · · (n − d)

= ∆(r, d, k) (r + kd) · · · (n + (k − 1)d)
r(r + d) · · · (n − d) .

We observe that p | ∆(n, d, k) for every prime p > k dividing ∆(r, d, k). □

Lemma 7.2.3. Let d ≤ k. For each 1 ≤ r < d with gcd(r, d) = 1, let r′ be such that rr′ ≡
1(mod d). Then
(a) For a given n with 1 ≤ n ≤ k, Theorem 1.2.1 holds if

∑

1≤r<d
gcd(r,d)=1
 π ( n + (k − 1)d
r , d, nr′) − π(2k) + ρ ≥ 0(7.2.1)

42 7. PROOF OF THEOREM 1.4.1

is valid.
(b) For a given n with k < n < 1.5k, Theorem 1.2.1 holds if

(7.2.2) ∑

1≤r<d
gcd(r,d)=1
 π ( k(d + 1) − d + 1
r , d, nr′) − π(2k) + π(k, d, n) − π(1.5k, d, n) ≥ 0

is valid.
(c) For a given n with k < n ≤ 2k, Theorem 1.2.1 holds if

(7.2.3) ∑

1≤r<d
gcd(r,d)=1
 π ( k(d + 1) − d + 1
r , d, nr′) − π(2k) + π(k, d, n) − π(2k, d, n) ≥ 0

is valid.

Proof. Let 1 ≤ r < d ≤ k, gcd(r, d) = 1. Then for each prime p ≡ nr′(mod d) with
max(k, n−1
r ) < p ≤ n+(k−1)d
r , there is a term rp = n + id in ∆(n, d, k). Therefore

W (∆(n, d, k)) ≥ ∑

1≤r<d
gcd(r,d)=1
 (π ( n + (k − 1)d
r , d, nr′) − π(max(k, n − 1
r ), d, nr′)
).(7.2.4)

Since ∑

1≤r<d
gcd(r,d)=1
 π(k, d, nr′) = πd(k),(7.2.5)

it is enough to prove (7.2.1) for deriving (1.4.11) for 1 ≤ n ≤ k. This gives (a).
Let k < n < k′ where k′ = 1.5k or 2k + 1. Then from (7.2.4) and (7.2.5), we have

W (∆(n, d, k)) ≥ ∑

1≤r<d
gcd(r,d)=1
 (

π ( k + 1 + (k − 1)d
r , d, nr′) − π(max(k, k′ − 1
r ), d, nr′)

)

≥ ∑

1≤r<d
gcd(r,d)=1
π ( k(d + 1) − d + 1
r , d, nr′) − π(k′ − 1, d, n) − πd(k) + π(k, d, n)

since r′ = 1 for r = 1. Hence it suﬃces to show (7.2.2) for proving (1.4.11) for k < n < 1.5k or
(7.2.3) for proving (1.4.11) for k < n ≤ 2k. Hence (b) and (c) are valid. □

7.3. Proof of Theorem 1.4.1 for k with 2k − 1 prime

Let
 χ = χ(n) =
 




min
 

1, k−1
n ∏

p|2d p−ordp(k−1)


 if 2 ∤ n

min
 

2θ−1, k−1
n ∏

p|d p−ordp(k−1)


 if 2 | n

(7.3.1)

and
 χ1 = χ1(n) = min
 



1, k − 1
n
 ∏

p|d p−ordp(k−1)



 .(7.3.2)

We observe that χ is non increasing function of n even and n odd separately. Further χ1 is a non
increasing function of n. We also check that
n0
n ≤ χ ≤ χ1(7.3.3)

and χ(1) = 1, χ(2) = 2θ−1.

7.3. PROOF OF THEOREM 1.4.1 FOR k WITH 2k − 1 PRIME 43

We take (n, d, k) /∈ V , n > k when d = 2 so that ρ = 0. We assume that (1.4.11) is not valid
and we shall arrive at a contradiction. We take m = π(2k) − πd(k) − 1 in Lemma 7.1.2. Then
t ≥ k − π(2k) in Lemma 7.1.2 and we have from (7.1.12) and (7.3.3) that

dk−π(2k) ≤ χ1(n)
 (k − 2)!
∏

p|d p−ordp((k−2)!)

(α + 1) · · · (α + k − π(2k))
(7.3.4)

where n = αd which is also the same as

k−π(2k)∏

i=1 (n + id) ≤ χ1(n)(k − 2)!
∏

p|d p−ordp((k−2)!).(7.3.5)

From (7.3.4), we have

dk−π(2k) ≤
 




χ1(αd)[α]!(k−2) · · · ([α]+k−π(2k)+1)
∏

p|d p−ordp(k−2)! if [α] ≤ π(2k) − 3,

χ1(αd)[α]!
∏

p|d p−ordp(k−2)! if [α] = π(2k) − 2,

χ1(αd) [α]!
(k−1)k(k+1)···([α]+k−π(2k)) ∏

p|d p−ordp(k−2)! if [α] ≥ π(2k) − 1.

(7.3.6)

We observe that the right hand sides of (7.3.4), (7.3.5) and (7.3.6) are non-increasing functions
of n = αd when d and k are ﬁxed. Thus (7.3.6) and hence (7.3.4) and (7.3.5) are not valid for
n ≥ n0 whenever it is not valid at n0 = α0d for given d and k. This will be used without reference
throughout this chapter. We obtain from (7.3.4) and χ1 ≤ 1 that

dk−π(2k) ≤ (k − 2) · · · (k − π(2k) + 1)∏

p|d p−ordp(k−2)!(7.3.7)

which implies that

dk−π(2k) ≤
 {
(k − 2) · · · (k − π(2k) + 1)2−ord2(k−2)! if d is even,
(k − 2) · · · (k − π(2k) + 1) if d is odd
(7.3.8)

and
 d ≤ (k − 2)
 π(2k)−2
k−π(2k) ∏

p|d p
 −ordp(k−2)!
k−π(2k) .(7.3.9)

Using Lemmas 3.1.2 (i) and 3.1.6, we derive from (7.3.9) that

d ≤ exp
 [ 2 log(k−2)
log 2k (1 + 1.2762
log 2k ) − 2 log(k−2)
k
1 − 2
log 2k (1 + 1.2762
log 2k )
 ] ∏

p|d p− max{0,( k−1−p
p−1 − log(k−2)
log p )/(k− 2k
log 2k (1+ 1.2762
log 2k ))}

(7.3.10)

which implies
 d ≤
 




exp [ 2 log(k−2)
log 2k (1+ 1.2762
log 2k )− 2 log(k−2)
k −((1− 3
k ) log 2− log(k−2)
k )
1− 2
log 2k (1+ 1.2762
log 2k )
 ] for d even,

exp [ 2 log(k−2)
log 2k (1+ 1.2762
log 2k )− 2 log(k−2)
k
1− 2
log 2k (1+ 1.2762
log 2k )
 ] for d odd.
(7.3.11)

We use the inequalities (7.3.5)-(7.3.11) at several places.
Let d be odd. Then for n even, 2 | n + id if and only if i is even and for n odd, 2 | n + id if and
only if i is odd. Let b = k − π(2k) + 1 − a and a0 = min(k − π(2k) + 1, [ k−2+θ
2 ]). We note here that
a ≤ [ k−2+θ
2 ] where θ is given by (7.1.2). Let ne, de, no and do be positive integers with ne even and

44 7. PROOF OF THEOREM 1.4.1

no odd. Let n ≥ ne and d ≤ de for n even, and n ≥ no and d ≤ do for n odd. Assume (7.1.13). The
left hand side of (7.1.13) is greater than




 n
2 dk−π(2k)a−1∏

i=1
 ( ne
2de + i
) b∏

j=1
 ( ne
de + 2j − 1) := n
2 dk−π(2k)F (a) if n is even

ndk−π(2k) a∏

i=1
 ( no
2do + i − 1
2
 ) b−1∏

j=1
 ( no
do + 2j) := ndk−π(2k)G(a) if n is odd.

(7.3.12)

Let Ae := min (a0, ⌈ 2
3 (k − π(2k)) + ne
6de + 1
3 ⌉) and Ao := min (a0, ⌈ 2
3 (k − π(2k)) + no
6do − 1
6 ⌉). By

considering the ratios F (a+1)
F (a) and G(a+1)
G(a) , we see that the functions F (a) and G(a) take minimal
values at Ae and Ao, respectively. Thus (7.1.13) with (7.3.3) implies that

dk−π(2k)F (Ae) ≤ 2−θ+1χ(ne)2
ord2([ k−2
2 ]!) ∏

p∤2d
pordp(k−2)! for n even(7.3.13)

since χ(n) ≤ χ(ne) and

dk−π(2k)G(Ao) ≤ χ(no)2
ord2([ k−2
2 ]!) ∏

p∤2d
pordp((k−2)!) for n odd(7.3.14)

since χ(n) ≤ χ(no). In the following two lemmas, we bound d if (1.4.11) does not hold.

Lemma 7.3.1. Let d be even. Assume that (1.4.11) does not hold. Then d ≤ 4.

Proof. Let d be even. By (7.3.11), d ≤ 6 for k ≥ 860. For k < 860, we use (7.3.8) to derive
that d ≤ 12 for k ≥ 9; d ≤ 10 for k = 100; d ≤ 8 for k > 57;

d ≤ 6 for k > 255, k ̸= 262, 310, 331, 332, 342.
(7.3.15)

Let d be a multiple of 6. Then we see from (7.3.10) that k ≤ 100. Again for k ≤ 100, (7.3.7) does
not hold. Let d be a multiple of 10. Then we see from (7.3.15) that k = 100 and k ≤ 57. Again,
(7.3.7) does not hold at these values of k.
Let d = 8. By (7.3.15), we may assume that k ≤ 255 and k = 262, 310, 331, 332, 342. Let n ≤ k.
From Lemma 7.2.2, we need to consider only n = 1, 3, 5, 7 and (1.4.11) is valid for these values of
n. Let n = k + 1. Then, we see that (7.3.5) does not hold. Thus (7.3.5) is not valid for all n > k.
Hence d ≤ 4. □

Lemma 7.3.2. Let d be odd. Assume that (1.4.11) does not hold. Then d ≤ 53 and d is prime.

Proof. Let d be odd. We may assume that d > 53 whenever d is prime. Firstly we use (7.3.11)
and then (7.3.8) to derive that d ≤ 15 for k ≥ 2164, d ≤ 59 for k ≥ 9 except at k = 10, 12, and
d ≤ 141 for k = 10, 12.
We further bring down the values of d and k by using (7.3.13) and (7.3.14). We shall be using
(7.3.13) with ne = 2, χ(ne) = 2
θ−1 and (7.3.14) with no = 1, χ(no) = 1 unless otherwise speciﬁed.
Let k < 2164. We take de = do = 59 when k ̸= 10, 12 and de = do = 141 for k = 10, 12. Let n be
even. From (7.3.13), we derive that
d ≤ 27 for k ≥ 9, k ̸= 10, 12, 16, 22, 24, 31, 37, 40, 42, 54, 55, 57;

d ≤ 57 for k = 10, 12, 16, 22, 24, 31, 37, 40, 42, 54, 55, 57;

d ≤ 21 for k > 100, k ̸= 106, 117, 121, 136, 139, 141, 142, 147, 159;

d ≤ 17 for k > 387, k ̸= 415, 420, 432, 442, 444;

d ≤ 15 for k > 957, k ̸= 1072, 1077, 1081.

(7.3.16)

Further we check that (7.3.16) holds for n odd using (7.3.14). Let d > 3 with 3 | d. Then k ≤ 1600
by (7.3.10) and k ≤ 850 by (7.3.7). Further we apply (7.3.13) and (7.3.14) with de = do = 57 to
conclude that d = 9, k ≤ 147, k = 157, 159, 232, 234 and d = 15, k = 10. The latter case is excluded
by applying (7.3.13) and (7.3.14) with de = do = 15. Let d = 9. Suppose n ≤ k. We check that

7.3. PROOF OF THEOREM 1.4.1 FOR k WITH 2k − 1 PRIME 45

(1.4.11) is valid for 1 ≤ n < 9 and gcd(n, 3) = 1. Now we apply Lemma 7.2.2 to ﬁnd that (1.4.11) is
valid for all n ≤ k. Let n > k. Taking ne = 2
⌈ k+1
2 ⌉, no = 2
⌈ k
2 ⌉ + 1, de = do = 9, we see that (7.3.13)
and (7.3.14) are not valid for n > k.
Let d > 15 with 5 | d and 3 ∤ d. Then k ≤ 159 by (7.3.16). Now, by taking de = do = 55,
we see that (7.3.13) and (7.3.14) do not hold unless k = 10, d = 25 and n odd. We observe that
(7.3.14) with no = 3 and do = 25 is not valid at k = 10. Thus (n, d, k) = (1, 25, 10) and we
check that (1.4.11) holds. Let d > 7 and 3 ∤ d, 5 ∤ d. Then we see from (7.3.16) that d = 49 and
k = 10, 12, 16, 22, 24, 31, 37, 40, 42, 54, 55, 57. Taking de = do = 49, we see that both (7.3.13) and
(7.3.14) do not hold. Thus d < 57 and the least prime divisor of d when d /∈ {3, 5, 7} is at least 11.
Hence d is prime and d ≤ 53. □

In view of Lemmas 7.3.1 and 7.3.2, it suﬃces to consider d = 2, 4 and primes d ≤ 53. We now
consider some small values of d.

Lemma 7.3.3. Let d = 2, 3, 4, 5 and 7. Assume that n ≤ k and (n, d, k) /∈ V . Then (1.4.11)
holds.

Proof. First, we consider the case 1 ≤ n ≤ k and (n, d, k) /∈ V . By Lemma 7.2.2, we may
assume that 1 ≤ n < d and gcd(n, d) = 1. Let d = 2. Then

π(n + 2(k − 1), 2, 1) − π(2k) + 1 = π(n + 2k − 2) − 1 − π(2k − 1) + 1 ≥ 0.

Now the assertion follows from Lemma 7.2.3. Let d = 3, 4, 5 or 7. We may assume that k is diﬀerent
from those given by (n, d, k) ∈ V , otherwise the assertion follows by direct computations. By using
the bounds for π(x, d, l) and π(x) from Lemmas 3.1.5 and 3.1.2, we see that the left hand side of
(7.2.1) is at least
 k
 {d−1∑

i=1
 ( d
i − d−1
ik )

log 1+dk−d
i
 (

c1 + c2
log 1+dk−d
2i
 )
 − 2
log 2k
 (1 + 1.2762
log 2k
 )}

(7.3.17)

for k ≥ d−1
d (1 + x0) at d = 3, 5, 7 and

k
 



 ∑

i=1,3
 ( 4
i − 3
ik )

log 4k−3
i
 (

c1 + c2
log 4k−3
2i
 )
 − 2
log 2k
 (1 + 1.2762
log 2k
 )



(7.3.18)

for k ≥ 3
4 (1 + x0) at d = 4. Here x0 is as given in Lemma 3.1.5. We see that (7.3.17) and (7.3.18)
are increasing functions of k and (7.3.17) is non negative at k = 20000, 2200, 1500 for d = 3, 5 and
7, respectively, and (7.3.18) is non negative at k = 751. Therefore, by Lemma 7.2.3, we conclude
that k is less than 20000, 751, 2200 and 1500 according as d = 3, 4, 5 and 7, respectively. Further we
recall that n < d. For these values of n and k, we check directly that (1.4.11) is valid. □

Therefore, by Lemma 7.3.3, we conclude that n > k when d = 2, 3, 4, 5 and 7.

Lemma 7.3.4. Let d = 2, 3, 4, 5 and 7. Assume that k < n ≤ 2k if d ̸= 2 and k < n < 1.5k if
d = 2. Then (1.4.11) holds.

Proof. Let d = 2 and k < n < 1.5k. By Lemma 7.2.3, it suﬃces to prove (7.2.2). By using
the bounds for π(k) from Lemma 3.1.2, we see that the left hand side of (7.2.2) is at least

k { 3
log 3k − 1 + 1
log k − 1 − 2
log 2k
 (1 + 1.2762
log 2k
 ) − 1.5
log 1.5k
 (1 + 1.2762
log 1.5k
 )} − 1

for k ≥ 5393 since π(3k − 1, 2, 1) = π(3k) − 1. We see that the above expression is an increasing
function of k and it is non negative at k = 5393. Thus (7.2.2) is valid for k ≥ 5393. For k < 5393, we
check using exact values of π function that (7.2.2) is valid except at k = 9, 10, 12. For these values
of k, we check directly that (1.4.11) is valid since k < n < 1.5k.
Let d = 3, 4, 5, 7 and k < n ≤ 2k. By Lemma 7.2.3, it suﬃces to prove (7.2.3). By using the
bounds for π(x, d, l), π(2x, d, l) − π(x, d, l) and π(k) from Lemmas 3.1.5 and 3.1.2, respectively, we
see that (7.2.3) is valid for k ≥ 20000, 4000, 2500, 1500 at d = 3, 4, 5 and 7, respectively. Thus we
need to consider only k < 20000, 4000, 2500, 1500 for d = 3, 4, 5 and 7, respectively. (The estimate

46 7. PROOF OF THEOREM 1.4.1

(2.4) in [27] should have been replaced by (3.1.4) but it is clear that this causes no problem). Taking
ne = 2⌈ k+1
2 ⌉, no = 2⌈ k
2 ⌉ + 1, de = do = d for d = 3, 5, 7 in (7.3.13) and (7.3.14), and n = k + 1 for
d = 4 in (7.3.5), we see that

k ≤ 3226 or k = 3501, 3510, 3522 when d = 3

k ≤ 12 or k = 16, 22, 24, 31, 37, 40, 42, 52, 54, 55, 57, 100, 142 when d = 4

k ≤ 901 or k = 940 when d = 5

k ≤ 342 when d = 7.

For these values of k, we check that (1.4.11) holds whenever k < n < 1.5k. Hence we may assume
that n ≥ 1.5k. Taking ne = 2⌈ 1.5k
2 ⌉, no = 2⌈ 1.5k−1
2 ⌉ + 1, de = do = d for d = 3, 5, 7 in (7.3.13) and
(7.3.14), and n = ⌈1.5k⌉ for d = 4 in (7.3.5), we see that

k ∈ {54, 55, 57} when d = 3

k ∈ {10, 22, 24, 40, 42, 54, 55, 57, 70, 99, 100, 142} when d = 5

k ∈ {10, 12, 24, 37, 40, 42, 54, 55, 57, 100} when d = 7.

For these values of k, we check directly that (1.4.11) holds for 1.5k ≤ n ≤ 2k. □

Lemma 7.3.5. Let d = 2, 3, 4, 5 and 7. Assume n > 2k if d ̸= 2 and n ≥ 1.5k if d = 2. Then
(1.4.11) holds.

Proof. Let d = 2 and n ≥ 1.5k. Then we take α = 1.5k
2 so that n ≥ αd. Further we observe
that α ≥ π(2k) − 1. Then we see from (7.3.6) and (7.3.2) that

2k−π(2k) ≤
 ⌈.75k⌉!
1.5k2(k + 1) · · · (
⌈.75k⌉ + k − π(2k)) 2−ord2(k−1)!.(7.3.19)

Now we apply Lemmas 3.1.7, 3.1.6 and 3.1.2 (i) in (7.3.19) to derive that

2 ≤
 ( 8
3 √2π exp(−.75k)(.75(k + 1))
.75(k+1)+ 1
2 exp( 1
9k )2
π(2k)

k2(k + 1).75k−π(2k)
 ) 1

2k− log(k−1)
log 2

≤ exp
 ( 2 log 2(k+1)
log 2k (1 + 1.2762
log 2k ) − .75 + .75 log .75 + 1
9k2 + 1.25 log(k+1)−2 log k+1.54017
k
2 − log(k−1)
k log 2
 )

for k ≥ 9. This does not hold for k ≥ 700. Thus k < 700. Further using (7.3.5) with n = ⌈1.5k⌉, we
get k ∈ {16, 24, 54, 55, 57, 100, 142}. For these values of k, taking n = 2k + 1, we see that (7.3.5) is
not valid. Thus n ≤ 2k. Now we check that (1.4.11) holds for these values of k and 1.5 ≤ n ≤ 2k.
Let d = 3, 4, 5 and 7 and n > 2k. Then we take α = 2k+1
d so that n ≥ αd. We proceed as in
the case d = 2 to derive from (7.3.5) that k < 70, 69, 162 and 1515 for d = 3, 4, 5 and 7, respectively.
Let d = 3, 5 and 7. We use (7.3.13) and (7.3.14) with ne = 2k + 2, no = 2k + 1 and de = do = d if
d = 3, 5, 7, respectively to get d = 5, k = 10 and n even. Let k = 10, d = 5 and n even. We take
ne = 2k + 6, de = 5 to see that (7.3.13) holds. Hence n ≤ 2k + 4. Now we check directly that (1.4.11)
is valid for n = 2k + 2, 2k + 4. Finally we consider d = 4 and k < 69. Taking n = 2k + 1, we see
that (7.3.5) is not valid. Thus (1.4.11) holds for all n > 2k. □

By Lemmas 7.3.1, 7.3.2, 7.3.3, 7.3.4, and 7.3.5, it remains to consider

11 ≤ d ≤ 53, d prime.

We prove Theorem 1.4.1 for these cases in the next section.

7.3.1. The Case d≥ 11 with d prime. Our strategy is as follows. Let U0, U1, · · · be sets of
positive integers. For any two sets U and V , we denote U − V = {u ∈ U |u /∈ V }. Let d be given.
We take de = do = d always unless otherwise speciﬁed. We apply steps 1 − 5 as given below.

7.4. PROOF OF THEOREM 1.4.1 47

1. Let d = 11, 13. We ﬁrst use (7.3.10) to bound k. We reduce this bound considerably using
(7.3.7). For d > 13, we use (7.3.16) to bound k. Then we apply (7.3.13) and (7.3.14) with
ne = n(0)
e = 2, no = n(0)
o = 1 to bring down the values of k still further. Let U0 be these
ﬁnite set of values of k.
2. For each k ∈ U0, we check that (1.4.11) is valid for 1 ≤ n < d. Hence by Lemma 7.2.2, we
get n > k.
3. For k ∈ U0, we apply (7.3.5) with n = k + 1 to ﬁnd a subset U ′
0 ⊊ U0.
4. For k ∈ U ′
0, we apply (7.3.13) and (7.3.14) with ne = n(1)
e = 2
⌈ k+1
2 ⌉, no = n(1)
o = 2
⌈ k
2 ⌉ + 1
to get a subset U1 ⊊ U ′
0.
5. Let i ≥ 2. For k ∈ Ui−1, we apply (7.3.13) and (7.3.14) with suitable values of ne = n(i)
e and
no = n(i)
o to get a subset Ui ⊊ Ui−1. Thus for k ∈ Ui−1−Ui, we have k < n < max(n(i)
e , n(i)
o )
and we check that (1.4.11) is valid for these values of n and k. We stop as soon as Ui = φ.
We explain the above strategy for d = 11. From (7.3.10), we get k ≤ 11500 which is reduced to
k ≤ 5589 by (7.3.7). By taking n(0)
e = 2, n(0)
o = 1, we get

U0 = {k|k ≤ 2977, k = 3181, 3184, 3187, 3190, 3195, 3199}.

We now check that (1.4.11) is valid for 1 ≤ n < 11 for each k ∈ U0 so that we conclude n > k. By
Step 3, we get U ′
0 = {k|k ≤ 252}. Further by step 4, we ﬁnd

U1 = {9, 10, 12, 16, 21, 22, 24, 27, 31, 37, 40, 42, 45, 52, 54, 55, 57, 70, 91, 99, 100, 121, 142}.

Now we take
 n(2)
e = 2
⌈ 1.5k
2 ⌉, n(2)
o = 2
⌈ 1.5k − 1
2 ⌉ + 1

to get U2 = {10, 22, 37, 42, 54, 55, 57}. Then we have

k < n < 1.5k for k ∈ U1 − U2.(7.3.20)

Next we take n(3)
e = 2k + 2, n(3)
o = 2k + 1 to get U3 = {10, 22, 55} and we have

k < n < 2k for k ∈ U2 − U3.(7.3.21)

Finally we take n(4)
e = 4k, n
(4)
o = 4k + 1 to get U4 = φ and hence

k < n < 4k for k ∈ U3(7.3.22)

and our procedure stops here since U4 = φ. Now we check that (1.4.11) holds for k and n as given
by (7.3.20), (7.3.21) and (7.3.22).
We follow steps 1 − 5 with the same parameters as for d = 11 in the cases d = 13, 17, 19 and
23. Let 23 < d ≤ 53, d prime. We modify our steps 1 − 5 slightly to cover all these values of d
simultaneously. For each of k ∈ U0, we check that (1.4.11) is valid for 1 ≤ n ≤ min(d, k) and coprime
to d. Thus n > k. Now we apply step 4 with de = do = 53 to get U1 = {10, 12, 16, 24, 37, 55, 57}. In
step 5, we take n(2)
e = 2
⌈ 3k+1
2 ⌉, n(2)
o = 2
⌈ 3k
2 ⌉ + 1, de = do = 53 to see that that U2 = φ. Thus

k < n < 3k for k ∈ U1.(7.3.23)

Now we check that (1.4.11) holds for k and n as given by (7.3.23) for every d with 23 < d ≤ 53 and
d prime. □

7.4. Proof of Theorem 1.4.1

By the preceding section, Theorem 1.4.1 is valid for all k such that 2k − 1 is prime. Let k be
any integer and k1 < k < k2 be such that 2k1 − 1, 2k2 − 1 are consecutive primes. By Lemma
7.2.3, we see that (1.4.11) is valid except possibly for those triples (n, d, k) with (n, d, k1) ∈ V . We
check the validity of (1.4.11) at those (n, d, k). For instance, let k = 11. Then k1 = 10. We see
that (1, 3, 10), (4, 3, 10), (2, 5, 10), (1, 7, 10) ∈ V . We check that (1.4.11) does not hold at (1, 3, 11)
and (1.4.11) holds at (4, 3, 11), (2, 5, 11) and (1, 7, 11). Thus (1, 3, 11) ∈ V . We ﬁnd that all the
exceptions to Theorem 1.4.1 are given by V . □

48 7. PROOF OF THEOREM 1.4.1

7.5. Proof of (1.4.8)

Let k = 8 and (n, d) be diﬀerent from the ones given by (1.4.9). Suppose (1.4.8) is not valid.
Then
 W (∆) ≤ k − 2 − πd(k).(7.5.1)

We apply Lemma 7.1.2 with m = k − 2 − πd(k). We see from t ≥ 1 and (7.1.12) that

n + d ≤ n0
n 6!
∏

p|d p−ordp(6!).(7.5.2)

Since n0 = 7 if 7|n and 1 otherwise, we observe that 1 + d ≤ n + d ≤ 6!
∏

p|d p−ordp(6!). For instance,

we get n + d ≤ 3 · 15 = 15 when 2|d. For each d with 1 < d ≤ 6!
∏

p|d p−ordp(6!) − 1 and for each n

satisfying (7.5.2), we check that
 |{P (n + id) : 0 ≤ i ≤ 7}| ≥ 7

hold except when (n, d) is given by

d = 4, n = 21; d = 7, n ∈ {3, 5, 6};

d = 11, n = 3; d = 17, n = 6;

d = 19, n = 5; d = 23, n = 1.
(7.5.3)

Now we get a contradiction from (7.5.1) since (7.5.1) is not valid for (n, d) given by (7.5.3) and

W (∆) = |{P (n + id) : 0 ≤ i ≤ 7}| − |{P (n + id) : P (n + id) ≤ k, 0 ≤ i ≤ 7}| ≥ 7 − πd(k)

for (n, d) diﬀerent from (7.5.3). □

CHAPTER 8

Reﬁnement of Sylvester’s theorem on the greatest prime
divisor of a product of terms of an arithmetic progression:
Proof of Theorem 1.5.1

In this chapter, we prove Theorem 1.5.1. The proof of Theorem 1.5.1 depends on Theorem 1.4.1
and the theory of linear forms in logarithms. The cases k = 3, 4, 5 involve solving particular cases of
Catalan’s equation and Generalised Fermat’s equation. The cases 6 ≤ k ≤ 11 requires solving some
Thue equations. For 12 ≤ k ≤ 18, we get a bound for n and d by counting the number of terms in
∆ divisible by a prime ≤ 2k and we check the assertion. When k ≥ 19, we follow the arguments in
the proof of Theorem 1.4.1 under certain assumptions which are valid in the present context.

8.1. Lemmas

We begin with

Lemma 8.1.1. It suﬃces to prove Theorem 1.5.1 for k such that 2k − 1 is prime.

Proof. Let (n, d, k) be as in Theorem 1.5.1. Let k1 and k2 be such that k1 < k < k2 and
2k1 − 1, 2k2 − 1 are consecutive primes. Assume that (1.5.2) holds at (n, d, k1). Then

P (n(n + d) · · · (n + (k − 1)d) ≥ P (n · · · (n + (k1 − 1)d)) > 2k1

implying P (∆(n, d, k)) ≥ 2k2 − 1 > 2k. Thus (1.5.2) holds at (n, d, k).
Therefore (1.5.2) is valid except possibly for those triples (n, d, k) with (n, d, k1) as one of the
exceptions in Theorem 1.5.1. We check the validity of (1.5.2) at those (n, d, k). For instance, let
k = 11. Then k1 = 10. We see that (1, 3, 10) is the only exception in Theorem 1.5.1. We check that
(1.5.2) holds at (1, 3, 11). □

For a proof of the following result, we refer to de Weger [80, Theorem 5.2]. It is a particular
case of Catalan equation which has been solved completely by Mih˘ailescu [41].

Lemma 8.1.2. Let a, b ∈ {2, 3, 5} and a < b. Then the solutions of

a
x − by = ±1 in integers x > 0, y > 0

are given by
 (a
x, by) ∈ {(2
2, 3), (2, 3), (2
3, 32), (2
2, 5)}.

The next result is due to Nagell [49], see [3].

Lemma 8.1.3. Let a, b, c ∈ {2, 3, 5} and a < b. Then the solutions of

a
x + by = c
z in integers x > 0, y > 0, z > 0

are given by
 (a
x, by, cz) ∈ {(2, 3, 5), (2
4, 32, 52), (2, 52, 33),

(2
2, 5, 32), (3, 5, 23), (3
3, 5, 25), (3, 53, 27)}.

We shall also need some more equations given by the following. See also de Weger [80, Theorem
5.5].
 49

50 8. PROOF OF THEOREM 1.5.1

Lemma 8.1.4. Let δ ∈ {1, −1}. The solutions of

(i) 2x − 3y5z = δ

(ii) 3x − 2y5z = δ

(iii) 5
x − 2y3z = δ

in integers x > 0, y > 0, z > 0 are given by

(x, y, z, δ) =
 




(4, 1, 1, 1) for (i);
(4, 4, 1, 1), (2, 1, 1, −1) for (ii);
(2, 3, 1, 1), (1, 1, 1, −1) for (iii),

respectively.

Proof. (i) Let δ = 1. By 2x ≡ 1(mod 5), we get 4|x. This implies 2 x
2 − 1 = 3
y, 2 x
2 + 1 = 5
z

and the assertion follows from Lemma 8.1.2. Let δ = −1. Then 2
x ≡ −1(mod 5) and 2
x ≡ −1(mod
3) implying 2|x and 2 ∤ x, respectively. This is a contradiction.
(ii) Let δ = 1. By 3
x ≡ 1(mod 5) giving 4|x and the assertion follows as in (i) with δ = 1. Let
δ = −1. Let y ≥ 2. Then 3x ≡ −1(mod 5) and 3x ≡ −1(mod 4) implying 2|x and 2 ∤ x, respectively.
Therefore y = 1 and we rewrite equation (ii) as 2 · 5z − 3x = 1. We may assume that z ≥ 2 and
further x is even by reading mod 4. Thus 3
x ≡ −1(mod 25) giving x ≡ 10(mod 20). Then x
10 is odd
and
 1 + 95 divides 1 + (9
5) x
10 = 2 · 5z,

a contradiction.
(iii) Let δ = 1. By mod 3, we get x even and the assertion follows as in (i) with δ = 1. Let
δ = −1. We may assume that y = 1 by mod 4 and z ≥ 2. Then we derive as in (ii) with δ = −1
that x
3 is odd by using mod 9 and 1 + 53 divides 1 + 5
x = 2 · 3z, a contradiction. □

We write p(d) for the least prime divisor of d. We shall use the following computational result.

Lemma 8.1.5. Assume that p(d) > k if k = 6, 7 and p(d) > 2k if k = 9, 10, 12, 15, 16. Then
(1.5.2) holds if
 n + d ≤ N

where
 N =
 




20 · 35 if k = 6, 7,
40 · 36 if k = 9, 10,
360 if = 12, 15, 16.

Proof. For each n with 1 ≤ n ≤ N and P (n) ≤ 2k, we check the validity of max{P (n + (k −
1)d), P (n + (k − 2)d), P (n + (k − 3)d)} > 2k whenever d ≤ N − n and p(d) > k if k = 6, 7 and
p(d) > 2k if k ≥ 9. If max{P (n + (k − 1)d), P (n + (k − 2)d), P (n + (k − 3)d)} ≤ 2k, then we check the
validity of max{P (n + d), P (n + 2d)} > 2k. Then we ﬁnd that either max{P (n + d), P (n + 2d)} > 2k
or
 (n, d) ∈ {(33, 31), (64, 31)} if k = 12 and (n, d) ∈ {(3, 31), (34, 31), (35, 43)} if k = 15.(8.1.1)

For (n, d, k) given by (8.1.1), we check that P (∆(n, d, k)) > 2k. □

Let n ≥ 1, d > 2 and k ≥ 3. By Lemma 8.1.1, we may restrict to those k for which 2k − 1 is
prime. For (n, d, k) ∈ V0 ∪ V where V0 and V are deﬁned in (1.4.6) and (1.4.10), respectively, we
check that P (∆(n, d, k)) > 2k. Therefore we assume that (n, d, k) /∈ V0 ∪ V . If p(d) ≤ k for k = 6, 7
and p(d) ≤ 2k for k ≥ 9, then the assertion follows from (1.4.5) and (1.4.12), respectively. Thus
we may suppose that p(d) > k for k = 6, 7 and p(d) > 2k for k ≥ 9. Therefore the assumption of
Lemma 8.1.5 is satisﬁed. We shall follow the assumptions stated in this paragraph throughout this
chapter. We split the proof of Theorem 1.5.1 for k = 3; k = 4; k = 6, 7, 9, 10; k = 12, 15, 16 and
k ≥ 19 with 2k − 1 prime in sections 8.2, 8.3, 8.4, 8.5 and 8.6, respectively.

8.3. THE CASE k = 4 51

8.2. The case k = 3

We assume that P (n(n + d)(n + 2d)) ≤ 5 and (n, d) is diﬀerent from the exceptions given in
Theorem 1.5.1. Let 5 ∤ ∆. Then either

n = 1, 1 + d = 2
α, 1 + 2d = 3
β or n = 2, 2 + d = 3
β, 2 + 2d = 2
α.

Assume the ﬁrst possibility. Then 2α+1 − 3β = 1 implying 2
α+1 = 4, 3β = 3 by Lemma 8.1.2.
Thus d = 1, a contradiction. Now we turn to the second. We get 3β − 2α−1 = 1. Therefore either
3β = 2, 2α−1 = 2 or 3
β = 9, 2α−1 = 8 by Lemma 8.1.2. The former is not possible since P 2kd > 1
and the latter implies that d = 7 which is excluded. Hence 5|∆.
Suppose 3 ∤ ∆. We observe that 5 ∤ n since gcd(n + d, n + 2d) = 1. Let 5|n + 2d. Then
n = 1, 1 + d = 2α, 1 + 2d = 5γ implying 2α+1 − 5γ = 1 which is not possible by Lemma 8.1.2. Let
5|n + d. Then n = 2
η, n + d = 5
γ, n + 2d = 2
α implying n = 2, 5γ − 2α−1 = 1. Therefore by Lemma
8.1.2, we get n = 2, d = 3 which is excluded. Hence 3|∆.
Let 15|n + id for some i ∈ {0, 1, 2}. We observe that 15 ∤ n since gcd(n + d, n + 2d) = 1. Let
15|n + d. Then n = 2, 2 + d = 3
β5γ, 2 + 2d = 2
α giving 2α−1 − 3β5γ = −1 which is not possible by
Lemma 8.1.4 (i). Let 15|n + 2d. Then n = 1, 1 + d = 2
α, 1 + 2d = 3
β5γ giving 2α+1 − 3β5γ = 1.
Therefore by Lemma 8.1.4 (i), we get n = 1, d = 7 which is excluded. Thus 15 ∤ n + id for i = 0, 1, 2.
Suppose 2 ∤ ∆. Then

n = 1, 1 + d = 3
β, 1 + 2d = 5
γ or n = 1, 1 + d = 5
γ, 1 + 2d = 3
β

which imply 5
γ − 2 · 3β = −1 or 3β − 2 · 5γ = −1, respectively. Therefore (n, d) = (1, 2) or (1, 4) by
Lemma 8.1.4. This is not possible. Hence 2|∆.
Let n = 1. In view of the above conclusions in this section, we have

1 + d = 2
α3β, 1 + 2d = 5
γ or 1 + d = 2
α5γ, 1 + 2d = 3
β

implying 5
γ − 2α+1 · 3β = −1 or 3
β − 2α+1 · 5γ = −1, respectively, contradicting Lemma 8.1.4
since α ≥ 1. Let n = 2. Then 2 + d = 3
β, 2 + 2d = 2
α5γ or 2 + d = 5
γ, 2 + 2d = 2
α3β implying
3β − 2α−1 · 5γ = 1 or 5
γ − 2α−1 · 3β = 1, respectively. By Lemma 8.1.4, the ﬁrst equation gives
d = 79 and the second one gives d = 23 which are excluded. Thus n > 2. Now we have

n = 2
α, n + d = 3
β, n + 2d = 2 · 5γ or n = 2
α, n + d = 5
γ, n + 2d = 2 · 3β

or n = 2 · 3β, n + d = 5
γ, n + 2d = 2
α or n = 2 · 5γ, n + d = 3
β, n + 2d = 2
α

or n = 3
β, n + d = 2
α, n + 2d = 5
γ or n = 5
γ, n + d = 2
α, n + 2d = 3
β.

By using the identity
 n + (n + 2d) − 2(n + d) = 0,(8.2.1)

we see that the above relations imply equations of the form given by Lemma 8.1.3. Now we use
Lemma 8.1.3 to ﬁnd all the pairs (n, d) arising out of the solutions of these equation. Finally we
observe that these pairs (n, d) are already excluded. □

8.3. The case k = 4

We shall derive Theorem 1.5.1 with k = 4 from the case k = 3 and the following more general
result. We put ∆1 = n(n + 2d)(n + 3d) and ∆2 = n(n + d)(n + 3d). Let

S41 = {(1, 13), (3, 11), (4, 7), (6, 7), (6, 13), (18, 119), (30, 17)}

and
 S42 = {(1, 3), (1, 5), (1, 8), (1, 53), (3, 2), (3, 5), (3, 17),

(3, 29), (3, 47), (9, 7), (9, 247), (15, 49), (27, 23)}.

52 8. PROOF OF THEOREM 1.5.1

Lemma 8.3.1. We have
 P (∆1) ≥ 7 unless (n, d) ∈ S41(8.3.1)

and
 P (∆2) ≥ 7 unless (n, d) ∈ S42.(8.3.2)

Proof. First we prove (8.3.1). Assume that (n, d) /∈ S41 and P (∆1) ≤ 5. Suppose 5 ∤ ∆1.
Then either
 n = 1, 1 + 2d = 3
β, 1 + 3d = 2
α or n = 6, 6 + 2d = 2
α, 6 + 3d = 3
β.

This is not possible by Lemma 8.1.2 since d > 1. Suppose 3 ∤ ∆1. Then either n = 1, 1 + 2d =
5γ, 1 + 3d = 2
α or n = 2, 2 + 2d = 2
α, 2 + 3d = 5
γ. This is again not possible by Lemma 8.1.4 (i),
(iii). Suppose 2 ∤ ∆1. Then either n = 1, 1 + 2d = 3
β, 1 + 3d = 5
γ or n = 3, 3 + 2d = 5
γ, 3 + 3d = 3
β.
This is not valid by Lemma 8.1.4 (ii), (iii). Hence 2 · 3 · 5 | ∆1.
Let n = 1. Then either 1 + 2d = 3β5γ, 1 + 3d = 2α or 1 + 2d = 3β, 1 + 3d = 2α5γ. The ﬁrst
possibility is excluded by Lemma 8.1.4 (i) and second possibility implies d = 13 by Lemma 8.1.4
(ii). Let n = 2. Then 2 + 2d = 2
α3β, 2 + 3d = 5
γ which is not possible by Lemma 8.1.4 (iii). Let
n = 3. Then 3 + 2d = 5
γ, 3 + 3d = 2
α3β implying d = 11 by Lemma 8.1.4 (iii). Let n = 6. Then
either 6 + 2d = 2
α5γ, 6 + 3d = 3
β or 6 + 2d = 2
α, 6 + 3d = 3
β5γ. The ﬁrst possibility implies d = 7
by Lemma 8.1.4 (ii) and second implies d = 13 by Lemma 8.1.4 (i).
Let n = 4, 5 or n > 6. We observe that n = 2δ15γ with δ1 ≥ 1 or 3
δ25γ with δ2 ≥ 1 are not
possible since otherwise P (n+3d) > 5 or P (n+2d) > 5, respectively. Let n = 2
δ13δ2 or n = 2
δ13δ25γ

with δ1 ≥ 1, δ2 ≥ 1. Then
 δ1 = 1, n = 2 · 3β, n + 2d = 2
α, n + 3d = 3 · 5γ

or δ2 = 1, n = 3 · 2α, n + 2d = 2 · 5γ, n + 3d = 3
β.

if n = 2
δ13δ2 and
 δ1 = 1, δ2 = 1, n = 6 · 5γ, n + 2d = 2
α, n + 3d = 3
β

if n = 2
δ13δ25γ. Further
 n + 2d = 2 · 3β, n + 3d = 5
γ if n = 2
α

n + 2d = 5
γ, n + 3d = 3 · 2α if n = 3
β

n + 2d = 3
β, n + 3d = 2
α if n = 5
γ.

This exhaust all the possibilities. For each of the above relations, we use the identity

n + 2(n + 3d) − 3(n + 2d) = 0(8.3.3)

to obtain an equation of the form given by Lemma 8.1.3. Finally we apply Lemma 8.1.3 as in the
preceding section to conclude that (n, d) ∈ S41, a contradiction.
The proof of (8.3.2) is similar to that of (8.3.1). Here we use the identity 2n+(n+3d)−3(n+d) =
0 in place of (8.3.3). □

Now we turn to the proof of Theorem 1.5.1 for k = 4. We assume P (∆) ≤ 7. In view of the
case k = 3, we may assume that 7|n + d or 7|n + 2d. Thus P (∆1) ≤ 5 if 7|n + d and P (∆2) ≤ 5 if
7|n + 2d. Now we conclude from Lemma 8.3.1 that (n, d) ∈ S41 if 7|n + d and (n, d) ∈ S42 if 7|n + 2d.
Finally we check that P (∆) ≥ 11 for (n, d) ∈ S41 ∪ S42 unless (n, d) ∈ {(1, 3), (1, 13), (3, 11)}. □

8.4. The cases k = 6, 7, 9, 10

We assume P (∆) ≤ 2k. Further by Lemma 8.1.5, we may assume that

n + d >
 {
20 · 35 if k = 6, 7,
40 · 36 if k = 9, 10.
(8.4.1)
 8.4. THE CASES k = 6, 7, 9, 10 53

There are at most 1 + [ k−1
p ] terms in ∆ divisible by a prime p. After removing all the terms in ∆
divisible by p ≥ 7, we are left with at least 4 terms divisible by 2, 3 and 5 only. After deleting the
terms in which 2, 3, 5 appear to maximal power, we are left with a term n + i0d with 0 ≤ i0 < k such
that P (n + i0d) ≤ 5 and n + i0d is at most 4 · 3 · 5 if k = 6, 7; 8 · 3 · 5 if k = 9 and 8 · 9 · 5 if k = 10. If
i0 > 0, we get n + d ≤ 360 contradicting (8.4.1). Thus we may suppose that i0 = 0 and the terms in
which 2, 3, 5 appear to maximal power are diﬀerent. Let n + i2d and n + i3d be the terms in which
2 and 3 appear to maximal power, respectively. Since 5 can divide at most 2 terms, we see that 5
can divide at most one of n + i2d and n + i3d. Also 5 ∤ n if 5|(n + i2d)(n + i3d). We write

n + i2d = 2
α23β25γ2, n + i3d = 2
α33β35γ3(8.4.2)

with (γ2, γ3) ∈ {(0, 0), (1, 0), (0, 1). We observe that α3 is at most 2 and 3 if k = 6, 7 and k = 9, 10,
respectively, and β2 is at most 1 and 2 if k = 6, 7, 9 and k = 10, respectively. If k = 6, 7, then α2 ≥ 7
otherwise n + d ≤ n + i2d ≤ 26 · 3 · 5 contradicting (8.4.1). Similarly we derive β3 ≥ 6 if k = 6, 7 and
α2 ≥ 8, β3 ≥ 7 if k = 9, 10. From i3(n + i2d) − i2(n + i3d) = (i3 − i2)n, we get

i32α23β25γ2 − i22α33β35γ3 = (i3 − i2)n(8.4.3)

Let
 α = ord2
 ( i32α2

i22α3
 ) , β = ord3
 ( i23β3

i33β2
 ) .(8.4.4)

We show that α ≥ α2 − δ where δ = 2 if k = 6, 7 and δ = 3 if k = 9, 10. It suﬃces to
prove ord2( i3
i22α3 ) ≥ −δ. If ord2(i3) ≥ord2(i2), then it is clear. Thus we may assume that
ord2(i3) <ord2(i2). From (8.4.2), we get (i2 −i3)d = 2
α3(2
α2−α3O2 −O3) with O2, O3 odd. Therefore
α3 =ord2(i2 − i3) since α2 > α3. Thus ord2(i3) = α3. Since i2 < k, we get the desired inequality
ord2( i3
i22α3 ) ≥ −δ. Hence α ≥ α2 − δ ≥ 5. Similarly we derive β ≥ 5.
We obtain from (8.4.3) the equation
 i2α − j3β = t(8.4.5)

with
 α ≥ 5, β ≥ 5,(8.4.6)

i, j ∈ {1, 5, 7, 25, 35}, t ∈ {±1, ±5, ±7, ±25, ±35} and gcd(i, j) =gcd(i, t) =gcd(j, t) = 1. From
Lemmas 8.1.2, 8.1.3 and 8.1.4, we see that equations of the form

2α − 3β = ±1, 2α − 3β = ±5, ±25,

2α − 5 · 3β = ±1, 5 · 2α − 3β = ±1,

2α − 25 · 3β = ±1, 25 · 2α − 3β = ±1

are not possible by (8.4.6). Let the equations given by (8.4.5) be diﬀerent from the above. Each of
the equation gives rise to a Thue equality
 X 3 + AY 3 = B(8.4.7)

with integers X, Y, A > 0, B > 0 given by

54 8. PROOF OF THEOREM 1.5.1

Equation A B X Y

(i) 2α − 3β = ±7 2a
′3b′ 7 · 2a
′ ±2 α+a′

3 ±3 β−b′

3

(ii) 7 · 2α − 3β = ±1, ±5, ±25 7 · 2a
′3b′ 3b′, 5 · 3b′, 25 · 3b′ ±3 β+b′

3 ±2 α−a′

3

(iii) 2α − 7 · 3β = ±1, ±5, ±25 7 · 2a
′3b′ 2a
′, 5 · 2a
′, 25 · 2a
′ ±2 α+a′

3 ±3 β−b′

3

(iv) 25 · 2α − 3β = ±7 5 · 2a
′3b′ 35 · 2a
′ ±5 · 2 α+a′

3 ±3 β−b′

3

(v) 2α − 25 · 3β = ±7 5 · 2a
′3b′ 35 · 3b′ ±5 · 3 β+b′

3 ±2 α−a′

3

(vi) 5 · 2α − 7 · 3β = ±1 25 · 7 · 2a
′3b′ 25 · 2a
′ ±5 · 2 α+a′

3 ±3 β−b′

3

(vii) 7 · 2α − 5 · 3β = ±1 25 · 7 · 2a
′3b′ 25 · 3b′ ±5 · 3 β+b′

3 ±2 α−a′

3

(viii) 2α − 5 · 3β = ±7 5 · 2a
′3b′ 7 · 2a
′ ±2 α+a′

3 ±3 β−b′

3

(ix) 5 · 2α − 3β = ±7 5 · 2a
′3b′ 7 · 3b′ ±3 β+b′

3 ±2 α−a′

3

(x) 35 · 2α − 3β = ±1 35 · 2a
′3b′ 3b′ ±3 β+b′

3 ±2 α−a′

3

(xi) 2α − 35 · 3β = ±1 35 · 2a
′3b′ 2a
′ ±2 α+a′

3 ±3 β−b′

3

(xii) 2α − 3β = ±35 2a
′3b′ 35 · 2a
′ ±2 α+a′

3 ±3 β−b′

3

(xiii) 7 · 2α − 25 · 3β = ±1 5 · 7 · 2a
′3b′ 5 · 3b′ ±5 · 3 β+b′

3 ±2 α−a′

3

(xiv) 25 · 2α − 7 · 3β = ±1 5 · 7 · 2a
′3b′ 5 · 2a
′ ±5 · 2 α+a′

3 ±3 β−b′

3

where 0 ≤ a
′, b′ < 3 are such that X, Y are integers. Further

max{ord2(X), ord3(X)} ≥ 2, max{ord2(Y ), ord3(Y )} ≥ 1(8.4.8)

by (8.4.6). Using Magma, we compute all the solutions in integers X, Y of the above Thue equations.
We ﬁnd that all the solutions of Thue equations other than (ii) and (viii) do not satisfy (8.4.8).
Further we check that the solutions of (ii) and (viii) satisfy (8.4.8) but they do not satisfy (8.4.6). □

8.5. The cases k = 12, 15, 16

We assume P (∆) ≤ 2k. Let k = 12, 15. Then P ((n + d) · · · (n + (k − 1)d)) ≤ 2k. After deleting
the terms from {n + d, · · · , n + (k − 1)d} divisible by primes p with 7 ≤ p ≤ 2k, we get at least 4
terms n + id composed of 2, 3 and 5 only. This is also the case when k = 16 since 7 and 13 together
divide at most 4 terms. Therefore there exists an i with 1 ≤ i ≤ k − 1 such that n + id divides
8 · 9 · 5. Thus n + d ≤ 360. Now the assertion follows from Lemma 8.1.5. □

8.6. The case k ≥ 19 with 2k − 1 prime

It suﬃces to prove W (∆) ≥ π(2k) − π(k) + 1 since π(k) = πd(k) by our assumption. We
may suppose that W (∆) = π(2k) − π(k) by Theorem 1.2.1. Further we observe that d > 2k since
p(d) > 2k.
By taking m = π(2k) − π(k) in Lemma 7.1.2, we conclude that

dk−π(2k)−1 ≤ (k − 2) · · · (k − π(2k))(8.6.1)

and hence
 2k < d < (k − 2)
 π(2k)−1
k−π(2k)−1 .(8.6.2)

Using Lemma 3.1.2, we see that

k − 2π(2k) ≥ k
log 2k
 (log 2k − 4(1 + 1.2762
log 2k )
) ≥ 0

for k ≥ 76. With exact values of π function, we see that k ≥ 2π(2k) for 60 ≤ k < 76. This implies
π(2k) − 1 ≤ k − π(2k) − 1 for k ≥ 60. Therefore for k ≥ 60, we see that (8.6.2) does not hold.
Thus k < 60. From (8.6.1), we see that d ≤ 2k for k ≥ 30, k ̸= 31. Thus it remains to consider
k = 19, 21, 22, 24, 27, 31. We see that d ≤ 71 if k = 27, 31; d ≤ 83 if k = 19, 21 and d ≤ 113 if
k = 22, 24.
 8.6. THE CASE k ≥ 19 WITH 2k − 1 PRIME 55

The next argument is analogous to (7.3.13) and (7.3.14) where k − π(2k) + 1 has been replaced
by k − π(2k). Let ne, de, no and do be positive integers with ne even and no odd. For (n, d, k) with
n even, n ≥ ne, d ≤ de, we derive from (7.1.13) with m = π(2k) − π(k) that

dk−π(2k)−1 Ae−1∏

i=1
 ( ne
2de + i
) k−π(2k)−Ae∏

j=1
 ( ne
de + 2j − 1) ≤ min (1, k − 1
ne 2−θ+1) (k − 2)!

× 2ord2([ k−2
2 ]!)−ord2((k−2)!)

(8.6.3)

where Ae =min(k − π(2k), ⌈ 2
3 (k − π(2k)) + ne
6de − 1
3 ⌉), θ = 1 if k is odd, 0 otherwise. For (n, d, k)
with n odd, n ≥ no, d ≤ do, we have

dk−π(2k)−1 Ao∏

i=1
 ( no
2do + i − 1
2
 ) k−π(2k)−Ao−1∏

j=1
 ( no
do + 2j) ≤ min (1, k − 1
no
 ) (k − 2)!

× 2ord2([ k−2
2 ]!)−ord2((k−2)!)

(8.6.4)

where Ao =min(k − π(2k), ⌈ 2
3 (k − π(2k)) + no
6do − 5
6 ⌉). Here we have used k − π(2k) ≤ [ k−2
2 ] for
the expressions given by Ae and Ao. We take ne = 2, no = 1, de = do = 83 if k = 19, 21, 27, 31
and ne = 2, no = 1, de = do = 113 if k = 22, 24. We get a contradiction for k = 27, 31 since
d > 2k. Thus we may assume that k ∈ {19, 21, 22, 24}. We obtain d ≤ De if n is even where
De = 47, 47, 67 and 61 according as k = 19, 21, 22 and 24, respectively. If n is odd, then d ≤ Do where
Do = 53, 47, 71 and 67 according as k = 19, 21, 22 and 24, respectively. By taking ne = 4k, de = De
and no = 4k + 1, do = Do, we derive from (8.6.3) and (8.6.4) that d < 2k. This is a contradiction.
Thus n < 4k. For these values of n, d and k, we check that P (∆(n, d, k)) > 2k is valid. This
completes the proof. □

Part 2

Proof of results on squares in products of
terms in an arithmetic progression

CHAPTER 9

Notation, Preliminaries and General Lemmas

In this chapter, we deﬁne notation, preliminaries and general lemmas which will used in the
following chapters.
 9.1. Notations and Preliminaries

Let n, d, k, b, y be positive integers such that b is square free, d ≥ 1, k ≥ 4, P (b) ≤ k and
gcd(n, d) = 1. Let t ≤ k and γ1 < γ2 < · · · < γt be integers with 0 ≤ γi < k for 1 ≤ i ≤ t. Let
ψ = k − t. We consider the equation

(9.1.1) (n + γ1d) · · · (n + γtd) = by2.

If t = k, we observe that γi = i − 1 and (9.1.1) coincides with (2.1.1). Assume that (9.1.1) holds.
Then we have
 n + γid = aγix
2
γi for 1 ≤ i ≤ t(9.1.2)

with aγi squarefree such that P (aγi) ≤ k. Also

n + γid = AγiX 2
γi for 1 ≤ i ≤ t(9.1.3)

P (Aγi) ≤ k and gcd(Xγi, ∏
p≤k p) = 1. Further we write

bi = aγi, Bi = Aγi, yi = xγi, Yi = Xγi.

Since gcd(n, d) = 1, we see from (9.1.2) and (9.1.3) that

(bi, d) = (Bi, d) = (yi, d) = (Yi, d) = 1 for 1 ≤ i ≤ t.(9.1.4)

By taking m = n + γtd and γ′
i = γt − γi, we re-write (9.1.1) as

(m − γ′
1d) · · · (m − γ′
td) = by2.(9.1.5)

The equation (9.1.5) is called the mirror image of (9.1.1). The corresponding t-tuple (aγ′
1, aγ′
2, · · · , aγ′
t)
is called the mirror image of (aγ1, · · · , aγt).
Let
 R = {bi : 1 ≤ i ≤ t}.

For bi ∈ R, let ν(bi) = |{j : 1 ≤ j ≤ t, bj = bi}| and

νo(bi) = |{j : 1 ≤ j ≤ t, bj = bi, 2 ∤ yj}|, νe(bi) = |{j : 1 ≤ j ≤ t, bj = bi, 2|yj}|.

We deﬁne

Rµ = {bi ∈ R : ν(bi) = µ}, rµ = |Rµ|, r = ∣
∣{(i, j) : bi = bj, bi, bj ∈ R and i > j}∣
∣.

Let
 T = {γi : Yi = 1, 1 ≤ i ≤ t}, T1 = {γi : Yi > 1, 1 ≤ i ≤ t}, S1 = {Bi : γi ∈ T1}.

Note that Yi > k for i ∈ T1. For i ∈ T1, we denote by ν(Bi) = |{γj ∈ T1 : Bj = Bi}|.
Let
 δ = min(3, ord2(d)), δ′ = min(1, ord2(d)),(9.1.6)
 η =
 {
1 if ord2(d) ≤ 1,
2 if ord2(d) ≥ 2
(9.1.7)
 59

60 9. NOTATION, PRELIMINARIES AND GENERAL LEMMAS

and
 ρ =
 {
3 if 3|d,
1 if 3 ∤ d.
(9.1.8)

Let d′ | d and d′′ = d
d
′ be such that gcd(d′, d′′) = 1. We write

d′′ = d1d2, gcd(d1, d2) =
 {
1 if ord2(d′′) ≤ 1
2 if ord2(d′′) ≥ 2

and we always suppose that d1 is odd if ord2(d′′) = 1. We call such pairs (d1, d2) as partitions of
d′′. We observe that the number of partitions of d′′ is 2
ω(d
′′ )−θ1 where

θ1 := θ1(d′′) =
 {
1 if ord2(d′′) = 1, 2
0 otherwise

and we write θ for θ1(d). In particular, by taking d′ = 1 and d′′ = d, the number of partitions of d
is 2
ω(d)−θ.
Let bi = bj, i > j. Then from (9.1.2) and (9.1.4), we have

(γi − γj)
bi d′ = y2
i − y2
j
d′′ = (yi − yj)(yi + yj)
d′′ .(9.1.9)

such that gcd(d′′, yi − yj, yi + yj) = 1 if d′′ is odd and 2 if d′′ is even. Thus a pair (i, j) with i > j
and bi = bj corresponds to a partition (d1, d2) of d′′ such that d1 | (yi − yj), d2 | (yi + yj) and
it is unique. Similarly, we have unique partition of d′′ corresponding to every pair (i, j) whenever
Bi = Bj, i, j ∈ T1.
Let p1 < p2 < · · · be the odd primes dividing d. Let

d =
 {
2δq1q2 · · · qω(d)−1 if δ = 1, 2
q1q2 · · · qω(d) otherwise

where q1 < q2 < · · · qω(d)−θ are prime powers dividing d
2δθ . By induction, we have

p1p2 · · · ph ≤ q1q2 · · · qh ≤ ( d
2δθ
 ) h
ω(d)−θ
(9.1.10)

for any h with 1 ≤ h ≤ ω(d) − θ. Further we deﬁne

Ah = {Bi ∈ T1 : Bi < q1q2 · · · qh}, λh = |Ah|.(9.1.11)

for any h with 1 ≤ h ≤ ω(d) − θ.
We end this section with the following lemma.

Lemma 9.1.1. Let ψ be ﬁxed. Suppose that (9.1.1) with P (b) ≤ k has no solution at k = k1
with k1 prime. Then (9.1.1) with P (b) ≤ k has no solution at k with k1 ≤ k < k2 where k2 is the
smallest prime larger than k1.

Proof. Let k1, k2 be consecutive primes such that k1 ≤ k < k2. Suppose (n, d, b, y) is a solution
of
 (n + γ1d) · · · (n + γtd) = by2

with P (b) ≤ k. Then P (b) ≤ k1. We observe that γk1−ψ < k1 and by (9.1.2),

(n + γ1d) · · · (n + γk1−ψd) = b′y′2

holds for some b′ with P (b′) ≤ k1 giving a solution of (9.1.1) at k = k1. This is a contradiction. □

9.2. SOME COUNTING FUNCTIONS 61

9.2. Some counting functions

Let p be a prime ≤ k and coprime to d. Then the number of i’s for which bi are divisible by q
is at most
 σq = ⌈ k
q ⌉.

Let r ≥ 5 be any positive integer. Deﬁne F (k, r) and F ′(k, r) as

F (k, r) = |{i : P (bi) > pr}| and F ′(k, r) =
 π(k)∑

i=r+1 σpi.

Then |{bi : P (bi) > pr}| ≤ F (k, r) ≤ F ′(k, r) − ∑

p|d,p>prσp. Let

Br = {bi : P (bi) ≤ pr}, Ir = {i : bi ∈ Br} and ξr = |Ir|.

We have
 ξr ≥ t − F (k, r) ≥ t − F ′(k, r) + ∑

p|d,p>prσp(9.2.1)

and
 t − |R| ≥ t − |{bi : P (bi) > pr}| − |{bi : P (bi) ≤ pr}|(9.2.2)
 ≥ t − F (k, r) − |{bi : P (bi) ≤ pr}|(9.2.3)
 ≥ t − F ′(k, r) + ∑

p|d,p>prσp − |{bi : P (bi) ≤ pr}|(9.2.4)
 ≥ t − F ′(k, r) + ∑

p|d,p>prσp − 2r.(9.2.5)

We write S := S(r) for the set of positive squarefree integers composed of primes ≤ pr. Let
δ =min{3,ord2(d)}. Let p = q = 2
δ or p ≤ q be odd primes dividing d. Let p = q = 2
δ. Then
bi ≡ n(mod 2
δ). Considering modulo 2
δ for elements of S(r), we see by induction on r that

|Br| ≤ 2r−δ =: g2δ,2δ =: g2δ .(9.2.6)

For any odd prime p dividing d, all bi’s are either quadratic residues mod p or non-quadratic residues
mod p. For odd primes p, q dividing d with p ≤ q, we consider four sets:

S1(n′, r) = S1(δ, n′, p, q, r) = {s ∈ S : s ≡ n′(mod 2
δ), ( s
p
 ) = 1, ( s
q
 ) = 1},

S2(n′, r) = S2(δ, n′, p, q, r) = {s ∈ S : s ≡ n′(mod 2
δ), ( s
p
 ) = 1, ( s
q
 ) = −1},

S3(n′, r) = S3(δ, n′, p, q, r) = {s ∈ S : s ≡ n′(mod 2
δ), ( s
p
 ) = −1, ( s
q
 ) = 1},

S4(n′, r) = S4(δ, n′, p, q, r) = {s ∈ S : s ≡ n′(mod 2
δ), ( s
p
 ) = −1, ( s
q
 ) = −1}.

(9.2.7)

We take n′ = 1 if δ = 0, 1; n′ = 1, 3 if δ = 2 and n′ = 1, 3, 5, 7 if δ = 3. Then Br ⊆ Sj(n′, r) for some
n and some j with 1 ≤ j ≤ 4. Let

gp,q := gp,q(r) = max
n′ (|S1(n′, r)|, |S2(n′, r)|, |S3(n′, r)|, |S4(n′, r)|)(9.2.8)

and we write gp = gp,p. Then
 |Br}| ≤ gp,q.(9.2.9)

62 9. NOTATION, PRELIMINARIES AND GENERAL LEMMAS

In view of (9.2.6) and (9.2.9), the inequality (9.2.4) is improved as

t − |R| ≥ t − F ′(k, r) + ∑

p|d,p>prσp − min
p|d,q|d
{gp,q}.(9.2.10)

We observe that gcd(s, pq) = 1 for s ∈ Sl, 1 ≤ l ≤ 4. Hence we see that Sl(n′, r + 1) = Sl(n′, r)
if p = pr+1 or q = pr+1 implying

gp,q(r + 1) = gp,q(r) if p = pr+1 or q = pr+1.(9.2.11)

Assume that pr+1 /∈ {p, q}. Let 1 ≤ l ≤ 4. We write S ′
l (n′, r + 1) = {s : s ∈ Sl(n′, r + 1), pr+1|s}.
Then s = pr+1s
′ with P (s
′) ≤ pr whenever s ∈ S ′
l (n′, r + 1). Let l = 1. Then s
′ ≡ n′p−1
r+1 ≡ n′′(mod

2δ) where n′′ = 1 if δ = 0, 1; n′′ = 1, 3 if δ = 2 and n′′ = 1, 3, 5, 7 if δ = 3. Further ( s′
p ) = ( pr+1
p ) and
( s′
q ) = ( pr+1
q ) for s ∈ S ′
l (r + 1). This implies S ′
1(n′, r + 1) = pr+1Sm(n′′, r) for some m, 1 ≤ m ≤ 4.

Therefore |S ′
1(n′, r + 1)| ≤ gp,q(r) by (9.2.8). Similarly |S ′
l (n′, r + 1)| ≤ gp,q(r) for each l, 1 ≤ 1 ≤ 4.
Hence we get from Sl(n′, r + 1) = Sl(n′, r) ∪ S ′
l (n′, r + 1) that

gp,q(r + 1) ≤ 2gp,q(r).(9.2.12)

We now use the above assertions to calculate gp,q.
i) Let δ = 0, r = 3, 4 and 2 < p ≤ 220. Then

gp(r) =
 {
2r−2 if p ≤ pr
2r−1 if p > pr
(9.2.13)

except when r = 3, p ∈ {71, 191} where gp = 2
r. ii) Let 5 ≤ r ≤ 7, p ≤ 547 when δ = 0, 1;
5 ≤ r ≤ 7, p ≤ 547 when δ = 2 and 5 ≤ r ≤ 7, p ≤ 89 when δ = 3. Then

gp(r) =
 {
max(1, 2r−δ−2) if p ≤ pr
max(1, 2r−δ−1) if p > pr
(9.2.14)

except when δ = 0, r = 5, p = 479 where gp = 2
r;
δ = 1, r = 5, p ∈ {131, 421, 479}, r = 6, p = 131 where gp = 2
r−δ;
δ = 2, r = 5, p ∈ {41, 101, 131, 331, 379, 421, 461, 479, 499} where gp = 2
r−δ;
δ = 2, r = 6, p ∈ {101, 131}, r = 7, p = 101 where gp = 2
r−δ;
δ = 3, r = 5, p = 3 where gp = 2
r−δ−1, r = 5, p = 41 where gp = 2
r−δ.
iii) Let 5 ≤ r ≤ 7, p ≤ 19, q ≤ 193, 23 ≤ p < q ≤ 97 when δ = 0 and r = 5, 6, p < q ≤ 37 when
δ ≥ 1. Then
 gp,q(r) =
 




max(1, 2r−δ−4) if p < q ≤ pr
max(1, 2r−δ−3) if p ≤ pr < q
max(1, 2r−δ−2) if pr < p < q
(9.2.15)
 9.3. LEMMAS FOR THE UPPER BOUND OF n + (k − 1)d 63

except when

δ = 0 and
 




r = 5, gp,q = 2
r−2 for (p, q) ∈ {(5, 43), (5, 167), (7, 113), (7, 127),
(7, 137), (11, 61), (11, 179), (11, 181)};
r = 5, gp,q = 2
r−1 for (p, q) ∈ {(19, 139), (23, 73), (37, 83)};
r = 6, gp,q = 2
r−2 for (p, q) = (7, 137);
r = 6, gp,q = 2
r−1 for (p, q) = (37, 83);

δ = 1 and
 




r = 5, gp,q = 2
r−4 for (p, q) ∈ {(5, 7), (5, 11)};
r = 5, gp,q = 2
r−3 for (p, q) = (5, 37);
r = 5, gp,q = 2
r−2 for (p, q) ∈ {(13, 23), (29, 31)};
r = 6, gp,q = 2
r−4 for (p, q) = (5, 7);

δ = 2 and
 




r = 5, gp,q = 2
r−4 for (p, q) ∈ {(3, 19), (5, 17), (5, 37), (7, 13),
(7, 23), (7, 29), (7, 31), (11, 19), (11, 29), (11, 31)};
r = 5, gp,q = 2
r−3 for (p, q) ∈ {(13, 23), (17, 37), (29, 31)};
r = 6, gp,q = 2
r−5 for (p, q) ∈ {(5, 7), (7, 13)};
r = 6, gp,q = 2
r−4 for (p, q) ∈ {(7, 29), (11, 31), (13, 23)}.

Now we combine (9.2.14), (9.2.15), (9.2.12) and (9.2.11). We obtain (9.2.14) with = replaced
by ≤ for r ≥ 7 and p ≤ 89 and we shall refer it as (9.2.14, ≤). Further we obtain (9.2.15) with =
replaced by ≤ for r ≥ 7 and either p < q ≤ 97 when δ = 0 or p = 3, q = 5 when δ ≥ 1 and we shall
refer it as (9.2.15, ≤).
 9.3. Lemmas for the upper bound of n + (k − 1)d

In this section, we assume that (9.1.1) holds. Let i > j, g > h, 0 ≤ i, j, g, h < k be such that

bi = bj, bg = bh, γi + γj ≥ γg + γh(9.3.1)

and
 yi − yj = d1r1, yi + yj = d2r2, yg − yh = d1s1, yg + yh = d2s2(9.3.2)

where (d1, d2) is a partition of d. We write V (i, j, g, h, d1, d2) for such double pairs. We call
V (i, j, g, h, d1, d2) degenerate if
 bi = bg, r1 = s1 or bi = bg, r2 = s2.(9.3.3)

Otherwise we call it non-degenerate. Let q1 and q2 be given by

|bir2
1 − bgs
2
1| = q1d2 and |bir2
2 − bgs
2
2| = q2d1.(9.3.4)

We shall also write V (i, j, g, h, d1, d2) = V (i, j, g, h, d1, d2, q1, q2).
Let Ω be a set of pairs (i, j) with i > j such that bi = bj. Then we say that Ω has Property
ND if the the following holds: For any two distinct pairs (i, j) and (g, h) in Ω corresponding to
a partition (d1, d2) of d, the double pair V (i, j, g, h, d1, d2) is non-degenerate. We begin with the
following lemma.

Lemma 9.3.1. Let d = θ1(k−1)
2, n = θ2(k−1)
3 with θ1 > 0 and θ2 > 0. Let V (i, j, g, h, d1, d2, q1, q2)
be a non-degenerate double pair. Then

θ2 < 1
2
 { 1
q1q2 − θ1 +
 √ 1
(q1q2)2 + θ1
q1q2
 }

(9.3.5)

and
 d1 < θ1(k − 1)
q1(2θ2 + θ1) , d2 < 4(k − 1)
q2 .(9.3.6)

64 9. NOTATION, PRELIMINARIES AND GENERAL LEMMAS

Proof. We have from (9.3.2) that yi = d1r1+d2r2
2 and yg = d1s1+d2s2
2 . Further from (9.1.2) and
(9.3.1), we get

(γi − γg)d = biy2
i − bgy2
g = 1
4 {(bir2
1 − bgs
2
1)d2
1 + (bir2
2 − bgs
2
2)d2
2 + 2d(bir1r2 − bgs1s2)
} .

We observe from (9.3.2), (9.3.1) and (9.1.2) that bir1r2 = γi − γj, bgs1s2 = γg − γh. Therefore

2(γi + γj − γg − γh)d = (bir2
1 − bgs
2
1)d2
1 + (bir2
2 − bgs
2
2)d2
2.(9.3.7)

Then reading modulo d1, d2 separately in (9.3.7), we have

d2∣
∣
∣(bir2
1 − bgs
2
1), d1∣
∣
∣(bir2
2 − bgs
2
2) if ord2(d) ≤ 1

d2
2
 ∣
∣
∣(bir2
1 − bgs
2
1), d1
2
 ∣
∣
∣(bir2
2 − bgs
2
2) if ord2(d) ≥ 2.
(9.3.8)

Hence 2q1, 2q2 are non-negative integers. We see that q1 ̸= 0 and q2 ̸= 0 since V (i, j, g, h, d1, d2, q1, q2)
is non-degenerate. Further we see from (9.1.2) that

biy2
i − bgy2
g = (γi − γg)d, bjy2
j − bhy2
h = (γj − γh)d.(9.3.9)

Therefore, by (9.3.2), we have

0 ̸= F1 := (bir2
1 − bgs
2
1)d2
1 = bi(yi − yj)
2 − bg(yg − yh)
2

= (γi + γj − γg − γh)d − 2(biyiyj − bgygyh)
(9.3.10)

and 0 ̸= F2 := (bir2
2 − bgs
2
2)d2
2 = bi(yi + yj)
2 − bg(yg + yh)
2

= (γi + γj − γg − γh)d + 2(biyiyj − bgygyh).
(9.3.11)

We note here that F1 < 0, F2 < 0 is not possible since γi + γj ≥ γg + γh.
Let a and b be positive real numbers with a ̸= b. We have 2√ab = (a + b)(1 − ( a−b
a+b )
2) 1
2 . By

using 1 − x < (1 − x) 1
2 < 1 − x
2 for 0 < x < 1, we get a + b − (a−b)2

a+b < 2√ab < a + b − (a−b)2

2(a+b) . We

use it with a = n + γid and b = n + γjd so that √ab = biyiyj by (9.1.2) and (9.3.1). We obtain

2n + (γi + γj)d − (γi − γj)
2d2

2n + (γi + γj)d < 2biyiyj < 2n + (γi + γj)d − (γi − γj)
2d2

4n + 2(γi + γj)d .(9.3.12)

Similarly we get

2n + (γg + γh)d − (γg − γh)
2d2

2n + (γg + γh)d < 2bgygyh < 2n + (γg + γh)d − (γg − γh)
2d2

4n + 2(γg + γh)d .(9.3.13)

Therefore we have from (9.3.4), (9.3.10), (9.3.12) and (9.3.13) that

q1dd1 <(γi + γj − γg − γh)d − (2n + (γi + γj)d) + (γi − γj)
2d2

2n + (γi + γj)d

+ (2n + (γg + γh)d) − (γg − γh)
2d2

4n + 2(γg + γh)d if F1 > 0

and
 q1dd1 <(2n + (γi + γj)d) − (γi − γj)
2d2

4n + 2(γi + γj)d − (2n + (γg + γh)d)

+ (γg − γh)
2d2

2n + (γg + γh)d − (γi + γj − γg − γh)d if F1 < 0.

Thus
 q1d1 <
 



 (γi−γj )2d
2n+(γi+γj )d = θ1(γi−γj )2

2θ2(k−1)+θ1(γi+γj ) if F1 > 0,

(γg−γh)2d
2n+(γg+γh)d = θ1(γg−γh)2

2θ2(k−1)+θ1(γg+γh) if F1 < 0.
(9.3.14)
 9.3. LEMMAS FOR THE UPPER BOUND OF n + (k − 1)d 65

Similarly from (9.3.4), (9.3.11), (9.3.12) and (9.3.13), we have

q2d2 <
 



2(γi + γj − γg − γh) + θ1(γg−γh)2

2θ2(k−1)+θ1(γg+γh) if F2 > 0

θ1(γi−γj )2

2θ2(k−1)+θ1(γi+γj ) − 2(γi + γj − γg − γh) if F2 < 0.
(9.3.15)

Let
 ni,j := (k − 1)
2 {
θ2(k − 1) + θ1(γi + γj)
2 − θ2
1(γi − γj)
2

2(2θ2(k − 1) + θ1(γi + γj))
 }

and
 ng,h := (k − 1)
2 {
θ2(k − 1) + θ1(γg + γh)
2 − θ2
1(γg − γh)
2

2(2θ2(k − 1) + θ1(γg + γh))
 } .

Then we see from (9.3.12) and (9.3.13) that ni,j < biyiyj < 1
4 bi(yi + yj)
2 and ng,h < bgygyh <
1
4 bg(yg + yh)
2, respectively. Assume F1 > 0. Then from (9.3.4), (9.3.11) and (9.3.2), we have

ni,jq1d2d2
1 < 1
4 bi(yi + yj)
2bi(yi − yj)
2 = 1
4 (γi − γj)
2d2

implying
 θ1 + θ2 = ni,j
(k − 1)3 + θ1
k − 1
 (k − 1 − γi + γj
2 + θ1(γi − γj)
2

2(2θ2(k − 1) + θ1(γi + γj))
 )

< (γi − γj)
2

4q1(k − 1)3 d2 + θ1 ≤ d2
4q1(k − 1) + θ1 if F1 > 0
(9.3.16)

by estimating θ1(γi−γj )2

2(2θ2(k−1)+θ1(γi+γj )) ≤ (γi−γj )2

2(γi+γj ) < γi+γj
2 . Similarly

θ1 + θ2 < d2
4q1(k − 1) + θ1 if F1 < 0.(9.3.17)

We separate the possible cases:
Case I: Let F1 > 0, F2 > 0. From (9.3.14) and (9.3.15), we have

q1q2θ1(k − 1)
2 < θ1(γi − γj)
2

2θ2(k − 1) + θ1(γi + γj)
 {2(γi + γj − γg − γh) + θ1(γg − γh)
2

2θ2(k − 1) + θ1(γg + γh)
 }

< θ1(γi − γj)
2

2θ2(k − 1) + θ1(γi + γj) {2(γi + γj) − 2(γg + γh) + γg − γh}

< 2θ1(γi − γj)
2(γi + γj)
2θ2(k − 1) + θ1(γi + γj) ≤ 2θ1γ3
i
2θ2(k − 1) + θ1γi ≤ 2θ1(k − 1)
3

2θ2(k − 1) + θ1(k − 1)

since 2θ1γ3
i
2θ2(k−1)+θ1γ3
i is an increasing function of γi. Therefore 2θ2 + θ1 < 2
q1q2 which gives (9.3.5).
Further from (9.3.14) and (9.3.15), we have

d1 < θ1(γi − γj)
2

q1(2θ2(k − 1) + θ1(γi + γj)) < θ1γ2
i
q1(2θ2(k − 1) + θ1γi) ≤ θ1(k − 1)
q1(2θ2 + θ1)

and
 d2 < 1
q2 {2(γi + γj) − 2(γg + γh) + γg − γh} < 2(γi + γj)
q2 < 4(k − 1)
q2

giving (9.3.6).
Case II: Let F1 > 0, F2 < 0. From (9.3.14), we have

d1 < θ1(γi − γj)
2

q1(2θ2(k − 1) + θ1(γi + γj)) < θ1(k − 1)
q1(2θ2 + θ1) .

66 9. NOTATION, PRELIMINARIES AND GENERAL LEMMAS

Similarly d2 < 1
q2 θ1(k−1)
2θ2+θ1 < k−1
q2 from (9.3.15) and γi + γj ≥ γg + γh. Therefore (9.3.6) follows.
Further
 θ1(k − 1)
2 = d = d1d2 < θ2
1(k − 1)
2

q1q2(2θ2 + θ1)2

implying (2θ2 + θ1)
2 < θ1
q1q2 . Hence (9.3.5) follows.
Case III: Let F1 < 0, F2 > 0. From (9.3.14) and (9.3.15), we have

θ1(k − 1)
2 < θ1γ2
g
q1q2(2θ2(k − 1) + θ1γg)
 {

2(γi + γj − γg) + θ1γ2
g
2θ2(k − 1) + θ1γg
 }
 .

Let χ(γg) = 1− 2θ2(k−1)
2θ2(k−1)+θ1γg so that γgχ(γg) = θ1γ2
g
2θ2(k−1)+θ1γg ≤ θ1(k−1)
2θ2+θ1 and both χ(γg) and γgχ(γg)
are increasing functions of γg. Since γi + γj ≤ 2(k − 1), we have

θ1(k − 1)
2 < γgχ(γg)
q1q2 {2(2(k − 1) − γg) + γgχ(γg)} = χ(γg)
q1q2
 {2γg(2(k − 1) − γg) + γ2
g χ(γg)
} .

We see that γg(2(k − 1) − γg) is an increasing function of γg since γg ≤ k − 1. Therefore the right
hand side of the above inequality is an increasing function of γg. Hence we obtain

θ1 < 1
(k − 1)2 θ1
q1q2(2θ2 + θ1)
 {2(k − 1)
2 + θ1(k − 1)
2

2θ2 + θ1
 } = θ1
q1q2(2θ2 + θ1)
 {2 + θ1
2θ2 + θ1
 } .

Thus (2θ2 + θ1)
2 < 3θ1+4θ2
q1q2 . Then we derive

(2θ2 + θ1 − 1
q1q2 )
2 < 1
(q1q2)2 + θ1
q1q2 .

Thus we get either 2θ2 + θ1 < 1
q1q2 or 2θ2 + θ1 − 1
q1q2 < √ 1
(q1q2)2 + θ1
q1q2 giving (9.3.5). Further from

(9.3.14), we have
 d1 < θ1(γg − γh)
2

q1(2θ2(k − 1) + θ1(γg + γh)) < θ1(k − 1)
q1(2θ2 + θ1) .

As in Case I, we have d2 < 4(k−1)
q2 . Thus (9.3.6) follows. □

Let θ1, θ2 be as in as the statement of Lemma 9.3.1.

Corollary 9.3.2. We have

θ1 < 3
q1q2 , θ1 + θ2 < θ1 + 2θ2 < 3
q1q2 .(9.3.18)

Proof. Since θ2 > 0, we see from (9.3.5) that either θ1 < 1
q1q2 or (θ1 − 1
q1q2 )
2 < 1
(q1q2)2 + θ1
q1q2
giving θ1 < 3
q1q2 . Hence we get from (9.3.5) that

θ1 + 2θ2 < 1
q1q2 +
 √ 1
(q1q2)2 + θ1
q1q2 < 3
q1q2 .

Thus (9.3.18) is valid. □

Lemma 9.3.3. Let bi = bj, bg = bh and (d1, d2) ̸= (η, d
η ) be a partition of d. Suppose that (i, j)
and (g, h) correspond to the partitions (d1, d2) and (d2, d1), respectively. Then

d1 < η(k − 1)
2, d2 < η(k − 1)
2.(9.3.19)

Proof. We write

yi − yj = d1r1, yi + yj = d2r2, yg − yh = d2s2, yg + yh = d1s1.

with
 bir1r2 = γi − γj, bgs1s2 = γg − γh.(9.3.20)
 9.3. LEMMAS FOR THE UPPER BOUND OF n + (k − 1)d 67

Then as in the proof of Lemma 9.3.1, we get (9.3.7) and (9.3.8). If both bir2
1 − bgs
2
1 ̸= 0 and
bir2
2 − bgs
2
2 ̸= 0, we obtain max(d1, d2) < η max(bir2
1, bgs
2
1, bir2
2, bgs
2
2) ≤ η(k − 1)
2 by (9.3.20). Thus
we may assume that either bir2
1 − bgs
2
1 = 0 or bir2
2 − bgs
2
2 = 0. Note that bir2
1 − bgs
2
1 = bir2
2 − bgs
2
2 = 0
is not possible. Suppose bir2
1 − bgs
2
1 = bir2
2 − bgs
2
2 = 0. Then bi = bg, r1 = s1, r2 = s2 implying
yi = yg, yj = yh. Hence we get γi = γg, γj = γh from (9.1.2) implying (i, j) = (g, h) which is a
contradiction. Now we consider the case bir2
1 − bgs
2
1 = 0 and the proof for the other is similar. From

bir2
2 −bgs
2
2 ̸= 0 and (9.3.7), we obtain 2(γi+γj −γg −γh)d1 = (bir2
2 −bgs
2
2)d2 implying d1∣
∣
∣η(bir2
2 −bgs
2
2)

and d2∣
∣
∣2η(γi + γj − γg − γh). Hence by (9.3.20), d1 < η(k − 1)
2, d2 < 2η(k − 1 + k − 2 − 1) ≤ η(k − 1)
2

implying (9.3.19). □

For two pairs (a, b), (c, d) with positive rationals a, b, c, d, we write (a, b) ≥ (c, d) if a ≥ c, b ≥ d.

Lemma 9.3.4. Let (d1, d2) be a partition of d. Suppose that there is a set G of at least z0 distinct
pairs corresponding to the partition (d1, d2) such that V (i, j, g, h, d1, d2) is non-degenerate for any
(i, j) and (g, h) in G. Then (9.3.5), (9.3.6) and (9.3.18) hold with (q1, q2) ≥ (Q1, Q2) where (Q1, Q2)
is given by the following table.
z0 d odd 2||d 4||d 8|d
2 (1, 1) (2, 1) ( 1
2 , 1
2 ) (1, 1
2 ) if 2||d1, ( 1
2 , 1) if 2||d2
3 (2, 2) (4, 4) or (8, 2) (2, 2) (2, 2)
5 (4, 4) (8, 4) (2, 8) or (8, 2) (2, 8) if 2||d1, (8, 2) if 2||d2
Table 1

For example, (Q1, Q2) = (1, 1) if z0 = 2, d odd and (Q1, Q2) = (2, 2) if z0 = 3, 4||d. If there
exists a non-degenerate double pair V (i, j, g, h, d1, d2), then we can apply Lemma 9.3.4 with z0 = 2.

Proof. For any pair (i, j) ∈ G, we write

yi − yj = r1(i, j)d1 and yi + yj = r2(i, j)d2(9.3.21)

where r1 = r1(i, j) and r2 = r2(i, j) are integers.
Let d be odd. Then r1 ≡ r2(mod 2) for any pair (i, j) by (9.3.21) and we shall use it in this
paragraph without reference. We observe that q1 ≥ 1, q2 ≥ 1 by (9.3.8), (9.3.4) and the assertion
follows for z0 = 2. Let z0 = 3. If there are two distinct pairs (i, j) with bir1 even, then q1 ≥ 2, q2 ≥ 2
by (9.3.8). Thus we may assume that there is at most one pair (i, j) for which bir1 is even. Therefore,
for the remaining two pairs, we see that both bir1’s are odd and the assertion follows again by (9.3.8).
Let z0 = 5. We may suppose that there is at most one (i, j) for which r1 is even otherwise the result
follows from (9.3.8). Now we consider remaining four pairs (i, j) for which r2
1 ≡ 1(mod 4). Out of
these pairs, there are (i1, j1) and (i2, j2) such that bi1 ≡ bi2(mod 4) since b’s are square free. Now
the assertion follows from (9.3.8).
Let d be even. We observe that

8|(y2
i − y2
j ) and gcd(yi − yj, yi + yj) = 2(9.3.22)

for any pair (i, j). Let 2||d. Then d1 is odd and d2 is even implying r1 is even by (9.3.22). Further
from (9.3.22), we have either 4|r1, 2 ∤ r2 or 2||r1, 2|r2. Therefore (q1, q2) ≥ (2, 1) by (9.3.8) since r1
is even and the assertion follows for z0 = 2. Let z0 = 3. Then there are two pairs (i1, j1) and (i2, j2)
such that r2(i1, j1) ≡ r2(i2, j2)(mod 2). Assume that r2 is odd. Then 4|r1 which implies 8|q1 and
2|q2 by (9.3.8). Now we suppose that r2 is even. Then 2||r1. We write r1 = 2r′
1 and

bi1r2
1(i1, j1) − bi2r2
1(i2, j2) = 4(bi1r′2
1 (i1, j1) − bi2r′2
1 (i2, j2)) ≡ 0(mod 8).

Hence 4|q1, 4|q2 by (9.3.8). Let z0 = 5. We choose three pairs (i, j) for which all bi’s ≡ 1(mod 4)
or all bi’s ≡ 3(mod 4). Out of these, we choose two pairs both of which satisfy either 4|r1, 2 ∤ r2 or
2||r1, 2|r2. Now we argue as above and use bi1 ≡ bi2(mod 4) to get the result.
Let 4||d. Then both d1 and d2 are even. From (9.3.22), we have either 2|r1, 2 ∤ r2 or 2 ∤ r1, 2|r2.
Since (q1, q2) ≥ ( 1
2 , 1
2 ) by (9.3.8), the the assertion follows for z0 = 2. Let z0 = 3. Then there are
two pairs (i1, j1) and (i2, j2) such that r1(i1, j1) ≡ r1(i2, j2)(mod 2) and r2(i1, j1) ≡ r2(i2, j2)(mod

68 9. NOTATION, PRELIMINARIES AND GENERAL LEMMAS

2). Since bi ≡ n(mod 4) for each i, we get from (9.3.8) and (9.3.4) that 2|q1 and 2|q2. Thus
(q1, q2) ≥ (2, 2). Let z0 = 5. Then we get 3 pairs (i, j) for which 2|r1(i, j), 2 ∤ r2(i, j) or 3 pairs (i, j)
for which 2 ∤ r1(i, j), 2|r2(i, j). Assume the ﬁrst case. Then there are 2 pairs (i1, j1) and (i2, j2) such
that r1(i1, j1) ≡ r1(i2, j2)(mod 4). This, with bi ≡ n(mod 4) and (9.3.4), implies that 16|q1d2 and
4|q2d1. Hence (q1, q2) ≥ (8, 2). In the latter case, we get (q1, q2) ≥ (2, 8) similarly.
Let 8|d. Then we have from (9.3.21) and (9.3.22) that either 2||d1 implying all r1’s are odd, or
2||d2 implying all r2’s are odd. Also bi ≡ n(mod 8) for all i. We prove the result for 2||d1 and the
proof for the other case is similar. From (9.3.7), we derive

2(γi1 + γj1 − γi2 − γj2) d1
2 d2
2 = (bi1r2
1 − bi2s
2
1) ( d1
2
 )2 + (bi1r2
2 − bi2s
2
2) ( d2
2
 )2
(9.3.23)

where r1 = r1(i1, j1), s1 = r1(i2, j2), r2 = r2(i1, j1) and s2 = r2(i2, j2). Noting that 4d2|d2
2 and
taking modulo d2, we get (q1, q2) ≥ (1, 1
2 ) implying the assertion for z0 = 2. Let z0 = 3. Then
there are 2 pairs (i1, j1) and (i2, j2) such that r2(i1, j1) ≡ r2(i2, j2)(mod 2). Using this and (9.3.4),
we get 4|q2d1. Further from bir1r2 = γi − γj, we see that γi1 − γj1 ≡ γi2 − γj2(mod 2) implying
γi1 + γj1 ≡ γi2 + γj2(mod 2). Now we see from (9.3.23) that 4 d2
2 |q1d2. Thus (q1, q2) ≥ (2, 2). Let
z0 = 5. We see that bi ≡ n or n+8 modulo 16 so that bir2
2(mod 16) is equal to 0 if 4|r2, 4n if 2||r2 and
n, n+8 if 2 ∤ r2. Now we can ﬁnd 2 pairs (i1, j1) and (i2, j2) such that bi1r2
2(i1, j1) ≡ bi2r2
2(i2, j2)(mod
16). This gives 16|q2d1 by (9.3.4). Further again 2|(γi1 + γj1 − γi2 − γj2) and hence 4 d2
2 |q1d2 from
(9.3.23). Therefore (q1, q2) ≥ (2, 8). □

Lemma 9.3.5. (i) Assume that
 n + γtd > η2γ2
t .(9.3.24)

Then for any pair (i, j) with bi = bj, the partition (dη−1, η) is not possible.
(ii) Let d = d′d′′ with gcd(d′, d′′) = 1. Then for any pair (i, j) with Bi = Bj ≥ d′, i, j ∈ T1, the
partition (d′′η−1, η) is not possible. In particular, the partition (dη−1, η) is not possible.

Proof. (i) Suppose the pair (i, j) with bi = bj correspond to the partition (dη−1, η). From
n+γid
n+γtd > γi
γt and (9.3.24), we get n + γid > η2γiγt. Then from (9.1.9), we have

γi − γj ≥ bi(yi + yj)
η ≥ (biy2
i ) 1
2 + (bjy2
j ) 1
2

η > η(
√γiγt + √γjγt)
η ≥ γi + γj,

a contradiction.
(ii) Suppose the pair (i, j) with Bi = Bj ≥ d′ correspond to the partition (d′′η−1, η). As in (9.1.9),
we have
 γi − γj ≥ (γi − γj) d′

Bi ≥ Yi + Yj
η > 2k
2

since Yi ≥ Yj > k. This is a contradiction. The latter assertion follows by taking d′ = 1, d′′ = d. □

Lemma 9.3.6. (i) Assume (9.3.24). Let 1 ≤ i0 ≤ t and ν(bi0) = µ. Let (d1, d2) be any partition
of d. Then the number of pairs (i, j) with bi = bj = bi0, i > j corresponding to (d1, d2) is at most [ µ
2 ].
(ii) Let d = d′d′′ with gcd(d′, d′′) = 1. Let i0 ∈ T1, Bi0 ≥ d′ and ν(Bi0) = µ. Let (d1, d2) be any
partition of d′′. Then the number of pairs (i, j) with Bi = Bj = Bi0, i > j corresponding to (d1, d2) is
at most [ µ
2 ].

Proof. (i) Suppose there are µ
′ = [ µ
2 ]+1 pairs (il, jl) with il > jl, 0 ≤ l < µ
′ and bil = bjl = bi0
corresponding to (d1, d2). We consider the sets I = {il|0 ≤ l < µ
′} and J = {jl|0 ≤ l < µ
′}. If
|I| < µ
′ or |J| < µ
′ or I ∩ J ̸= φ, then there are l ̸= m such that

d1|(yjl − yjm ), d2|(yjl − yjm ) if il = im
d1|(yil − yim ), d2|(yil − yim ) if jl = jm
d1|(yjl − yim ), d2|(yjl − yim ) if il = jm.

9.3. LEMMAS FOR THE UPPER BOUND OF n + (k − 1)d 69

We exclude the ﬁrst possibility and proofs for the others are similar. Without loss of generality, we
may assume that jl > jm. Then lcm(d1, d2)
∣
∣(yjl − yjm ) so that the pair (jl, jm) correspond to the
partition (dη−1, η). This is not possible by Lemma 9.3.5 (i). Thus |I| = µ
′, |J| = µ
′ and I ∩ J = φ.
Now we see that |I ∪ J| = |I| + |J| = 2µ
′ > µ and bi = bi0 for every i ∈ I ∪ J. This contradicts
ν(bi0) = µ.
(ii) The proof is similar to that of (i) and we use Lemma 9.3.5 (ii). □

As a corollary, we have

Corollary 9.3.7. (i) Assume (9.3.24). For 1 ≤ i ≤ t, we have ν(bi) ≤ 2ω(d)−θ.
(ii) Let d = d′d′′ with gcd(d′, d′′) = 1. For Bi ≥ d′, we have ν(Bi) ≤ 2ω(d
′′ )−θ1. In particular,
ν(Bi) ≤ 2ω(d)−θ.

Proof. (i) Let ν(bi) = µ. Then there are µ(µ−1)
2 pairs (g, h) with g > h and bg = bh = bi.
Since there are at most 2ω(d)−θ − 1 permissible partitions of d, we see from Lemma 9.3.6 (i) that
µ(µ−1)
2 ≤ µ
2 (2
ω(d)−θ − 1). Hence the assertion follows.
(ii) The proof of the assertion (ii) is similar and we use Lemma 9.3.6 (ii). □

Corollary 9.3.8. Let Th+1 = {i ∈ T1 : Bi ≥ q1q2 · · · qh} and sh+1 = |{Bi : i ∈ Th+1}|. Then

|Th+1| ≥ |T1| −
 h−1∑

µ=1 2ω(d)−µ−θλµ − 2ω(d)−h−1−θλh

and
 sh+1 ≥ |T1|
2ω(d)−h−θ −
 h−1∑

µ=1 2h−µλµ − 2λh

where λ’s are as deﬁned in (9.1.11).

Proof. We apply Corollary 9.3.7 (ii) with d′ = q1q2 · · · qµ to derive that ν(Bi) ≤ 2ω(d)−µ−θ

for Bi ≥ q1q2 · · · qµ, µ ≥ 1 since θ1 ≥ θ. Therefore

|Th+1| ≥ |T1| − 2ω(d)−θλ1 − 2ω(d)−1−θ(λ2 − λ1) − · · · − 2ω(d)−h+1−θ(λh − λh−1).

and the ﬁrst assertion follows. Further from ν(Bi) ≤ 2ω(d)−h−θ for i ∈ Th+1, we have sh+1 ≥
|Th+1|
2ω(d)−h−θ and the last assertion follows. □

Lemma 9.3.9. Assume (9.3.24). There exists a set Ω of at least

t − |R| + ∑

µ>1
µ odd
 rµ ≥ t − |R|

pairs (i, j) having Property ND.

Proof. We have
 t = ∑

µ µrµ and |R| = ∑

µ rµ.

Each bi0 ∈ Rµ gives rise to µ(µ−1)
2 pairs (i, j) with i > j such that bi = bj = bi0 and each
pair corresponds to a partition of d. By Lemma 9.3.6, we know that there are at most [ µ
2 ] pairs
corresponding to any partition of d. For each 1 ≤ j ≤ [ µ
2 ] = µ1, let vj be the number of partitions
of d for which there are j pairs out of the ones given by bi0 ∈ Rµ corresponding to that partition.
Then
 µ(µ − 1)
2 =
 µ1∑

j=1 jvj.(9.3.25)

70 9. NOTATION, PRELIMINARIES AND GENERAL LEMMAS

For each partition having j pairs with vj > 0, we remove j − 1 pairs. Then we remove in all∑µ1
j=1(j − 1)vj pairs. Rewriting (9.3.25) as

µ(µ − 1)
2 = µ1
 µ1∑

j=1 vj −
 µ1∑

j=1(µ1 − j)vj,

we see that we are left with at least
µ1∑

j=1 vj = µ(µ − 1)
2µ1 +
 µ1∑

j=1(1 − j
µ1 )vj ≥ µ(µ − 1)
2µ1 =
 {
µ − 1 if µ is even
µ if µ is odd

pairs. Let Ω be the union of all such pairs taken over all bi0 ∈ Rµ and for all µ ≥ 2. Since |Rµ| = rµ,
we have
 |Ω| ≥ ∑

µ even(µ − 1)rµ + ∑

µ>1
µ odd
 µrµ = t − |R| + ∑

µ>1
µ odd
 rµ.

Further we see from the construction of the set Ω that Ω satisfy Property ND. □

Corollary 9.3.10. Assume (9.3.24). Let z be a positive integer and h(z) = (z − 1)(2
ω(d)−θ −
1) + 1. Let z0 ∈ {2, 3, 5}. Suppose that t − |R| ≥ h(z0). Then there exists a partition (d1, d2) of d
such that (9.3.5), (9.3.6) and (9.3.18) hold with (q1, q2) ≥ (Q1, Q2) where (Q1, Q2) is given by Table
1.
 Proof. By Lemma 9.3.9, there exists a set Ω with at least h(z0) pairs satisfying Property ND.
Since there are at most 2ω(d)−θ − 1 permissible partitions of d by Lemma 9.3.5 (i), we can ﬁnd a
partition (d1, d2) of d and a subset G ⊂ Ω of at least z0 pairs corresponding to (d1, d2). Now the
result follows by Lemma 9.3.4. □

Corollary 9.3.11. Assume (9.3.24). Suppose that t − |R| ≥ 2ω(d)−θ−1 + 1. Then there exists
a partition (d1, d2) of d such that (9.3.19) holds.

Proof. By Lemma 9.3.9, there exists a set Ω with at least 2ω(d)−θ−1 + 1 pairs (i, j) satisfying
Property ND. We may assume that for each partition (d1, d2) of d, there is at most 1 pair corre-
sponding to (d1, d2) otherwise the assertion follows by z0 = 2 in Lemma 9.3.4. We see that there are
2ω(d)−θ−1 − 1 partitions (d1, d2) with d1 > d2, 2ω(d)−θ−1 − 1 partitions (d1, d2) with η < d1 < d2 and
the partition (η, dη−1). Since there are at least 2ω(d)−θ−1 + 1 pairs, we can ﬁnd two pairs (i, j) and
(g, h) corresponding to the partitions (d1, d2) and (d2, d1), respectively. Now the assertion follows
by Lemma 9.3.3. □

Lemma 9.3.12. Assume (9.3.24).
(i) Let |S1| ≤ |T1| − h(3). Then (9.3.18) is valid with

q1q2 ≥
 




144ρ−1 if 2 ∤ d
16 if 2||d
4 if 4|d.
(9.3.26)

(ii) Let d be even and |S1| ≤ |T1| − h(5). Then (9.3.18) is valid with

q1q2 ≥
 




144ρ−1 if 2||d
36 if 4|d and 3 ∤ d
16 if 4|d and 3|d.
(9.3.27)

Proof. Let Bi = Bj with i > j and i, j ∈ T1. Then there is a partition (d1, d2) of d such that
Yi − Yj = d1r′
1, Yi + Yj = d2r′
2 with r′
1, r′
2 even, 24ρ−1|r′
1r′
2 if d is odd and r′
1 even, 12ρ−1|r′
1r′
2 if
2||d and 3ρ−1|r′
1r′
2 if 4|d. Since BiY 2
i = biy2
i and bi is squarefree, we see that p|bi if and only if p|Bi
with ordp(Bi) odd. Therefore bi = bj implying b2 = Bi
bi = Bj
bj and yi = bYi, yj = bYj. Hence

yi − yj = d1br′
1 = d1r1(i, j) = d1r1, yi + yj = d2br′
2 = d2r2(i, j) = d2r2

9.3. LEMMAS FOR THE UPPER BOUND OF n + (k − 1)d 71

with r1 = br′
1, r2 = br′
2 even, 24ρ−1|r1r2 if d is odd; r1 even, 12ρ−1|r1r2 if 2||d and 3ρ−1|r1r2 if
4|d. Let z ∈ {3, 5} and |S1| ≤ |T1| − h(z). We argue as in Lemma 9.3.9 and Corollary 9.3.10 with t
and |R| replaced by |T1| and |S1|. There exists a partition (d1, d2) of d and z pairs corresponding
to (d1, d2) such that V (i, j, g, h, d1, d2) is non-degenerate for any two such distinct pairs (i, j) and
(g, h). Let z = 3. By Lemma 9.3.4 with z0 = 3, we may suppose that d is odd. Let 3 ∤ d. Then we
can ﬁnd two distinct pairs (i1, j1) and (i2, j2) both of which satisfy either 3|r1(i1, j1), 3|r1(i2, j2) or
3|r2(i1, j1), 3|r2(i2, j2). Now (9.3.26) follows from (9.3.8) and (9.3.4) since r1, r2 are even. Assume
that 3|d. Let 3|d1. Then we can ﬁnd two distinct pairs (i1, j1) and (i2, j2) both of which satisfy
either 3|r1(i1, j1), 3|r1(i2, j2) or 3 ∤ r1(i1, j1), 3 ∤ r1(i2, j2). Since bi ≡ n(mod 3) and r2 ≡ 1(mod 3)
for 3 ∤ r, the assertion follows from (9.3.8) and (9.3.4) since r1, r2 are even. The same assertion hold
for 3|d2 in which case r1 is replaced by r2. This proves (9.3.26) and we turn to the proof of (9.3.27).
Let d be even and z = 5. Let 3 ∤ d. Out of these ﬁve pairs, we can ﬁnd three distinct pairs (i, j)
for which either r1(i, j)’s are all divisible by 3 or r2(i, j)’s are all divisible by 3. As in the proof of
Lemma 9.3.4 with d even and z0 = 3, we ﬁnd two distinct pairs (i1, j1) and (i2, j2) such that 16|q1q2
if 2||d and 4|q1q2 if 4|d. Further 9|q1q2 since either r1(i, j)’s are all divisible by 3 or r2(i, j)’s are
all divisible by 3 and hence the assertion. Assume now that 3|d. By Lemma 9.3.4 with z0 = 5, we
may suppose that 2||d. Let 3|d1. Then we can ﬁnd three pairs (i, j) for which either 3 divides all
r1(i, j)’s or 3 does not divide any r1(i, j). Then for any two such pairs (i1, j1) and (i2, j2), we have
3|(bi1r2
1(i1, j1) − bi2r2
1(i2, j2)). Therefore by the proof of Lemma 9.3.4 with d even and z0 = 3, we
get 3 · 16|q1q2. The other case 3|d2 is similar. □

The next result depends on an idea of Erd˝os and Rigge.

Lemma 9.3.13. Let z1 > 1 be a real number, h0 > i0 ≥ 0 be integers such that ∏
bi∈R bi ≥

z|R|−i0
1 (|R| − i0)! for |R| ≥ h0. Suppose that t − |R| < g and let g1 = k − t + g − 1 + i0. For
k ≥ h0 + g1 and for any real number m > 1, we have

g1 >
 k log
 

 z1n0
2.71851 ∏

p≤m
p
 2
p2−1 (1− 1
pn(k,p) )

 + (k + 1
2 ) log(1 − g1
k )

log(k − g1) − 1 + log z1 +

(.5ℓ + 1) log k − log
 

n
−1
1 ∏

p≤m
p1.5n(k,p)




log(k − g1) − 1 + log z1

(9.3.28)

and
 g1 >
 k log
 

 z1n0
2.71851 ∏

p≤m
p
 2
p2−1
 

 + (k + 1
2 ) log(1 − g1
k )

log(k − g1) − 1 + log z1 −

(1.5π(m) − .5ℓ − 1) log k + log
 

n
−1
1 n2 ∏

p≤m
p.5+ 2
p2−1
 



log(k − g1) − 1 + log z1

(9.3.29)

where
 n(k, p) =
 {
[ log(k−1)
log p ] if [ log(k−1)
log p ] is even
[ log(k−1)
log p ] − 1 if [ log(k−1)
log p ] is odd,

ℓ = |{p ≤ m : p|d}|, n0 = ∏

p|d
p≤m
 p 1
p+1 , n1 = ∏

p|d
p≤m
 p
 p−1
2(p+1) and n2 =
 {
2 1
6 if 2 ∤ d
1 otherwise.

72 9. NOTATION, PRELIMINARIES AND GENERAL LEMMAS

Proof. Since |R| ≥ t − g + 1 = k − g1 + i0, we get
∏

bi∈R bi ≥ zk−g1
1 (k − g1)!.(9.3.30)

Let
 ϑp = ordp
 ( ∏

bi∈R bi
)
 , ϑ′
p = 1 + ordp((k − 1)!).

Let h be the positive integer such that ph ≤ k − 1 < p
h+1 and ϵ = 1 or 0 according as h is even or
odd, respectively. Then
 ϑ′
p − 1 = [ k − 1
p
 ] + [ k − 1
p2
 ] + · · · + [ k − 1
ph
 ] .(9.3.31)

Let p ∤ d. We show that

ϑp − ϑ′
p < − 2k
p2 − 1 (1 − 1
pn(k,p) ) + 1.5n(k, p)(9.3.32)
 < − 2k
p2 − 1 + 1.5 log k
log p + .5 + 2
p2 − 1 + n3(9.3.33)

where n3 = 1
6 if p = 2 and 0 otherwise. We see that ϑp is the number of elements in {n + γ1d, n +
γ2d, . . . , n + γtd} divisible by p to an odd power. For a positive integer s with s ≤ h, let 0 ≤ ips < p
s

be such that ps|n + ips d. Then we observe that ps divides exactly 1 + [ k−1−ips
ps ] elements in

{n, n + d, . . . , n + (k − 1)d}. After removing a term to which p appears to a maximal power, the
number of remaining elements in {n, n + d, . . . , n + (k − 1)d} divisible by p to an odd power is at
most [ k − 1 − ip
p
 ] − [ k − 1 − ip2
p2
 ] + [ k − 1 − ip3
p3
 ] − · · · + (−1)
ϵ [ k − 1 − iph
ph
 ] .

Since [ k
ps ] − 1 ≤ [ k−1−ips
ps ] ≤ [ k−1
ps ], we obtain

ϑp − 1 ≤ [ k − 1
p
 ] − [ k
p2
 ] + [ k − 1
p3
 ] − · · · + (−1)
ϵ [ k − 1 + ϵ
ph
 ] + h − 1 + ϵ
2 .

This with (9.3.31) implies

ϑp − ϑ′
p ≤ −
 h−1+ϵ
2∑

j=1
 ([ k − 1
p2j
 ] + [ k
p2j
 ]) + h − 1 + ϵ
2 .(9.3.34)

Since [ k
p2j ] ≥ [ k−1
p2j ] ≥ k−1
p2j − 1 + 1
p2j = k
p2j − 1, we obtain

ϑp − ϑ′
p ≤ −2k
 h−1+ϵ
2∑

j=1
 1
p2 + 1.5(h − 1 + ϵ)

giving (9.3.32) since n(k, p) = h − 1 + ϵ. Further from (9.3.32), k ≤ ph+1 and h < log k
log p , we get

ϑp − ϑ′
p < − 2k
p2 − 1 + 1.5 log k
log p + 2p2−ϵ

p2 − 1 + 1.5(ϵ − 1)

giving (9.3.33). For p|d, we get ϑp − ϑ′
p = −1 − ordp(k − 1)! which together with Lemma 3.1.6 gives

ϑp − ϑ′
p < − k
p − 1 + log k
log p + 1
p − 1

< − 2k
p2 − 1 + 1.5 log k
log p + .5 + 2
p2 − 1 − k
p + 1 − .5 log k
log p − p − 1
2(p + 1) .
(9.3.35)
 9.4. LEMMAS FOR THE LOWER BOUND FOR n + (k − 1)d 73

For m > 1, we have
 ∏

bi∈R bi ∣
∣
∣ (k − 1)!
 

 ∏

p≤k p


 ∏

p≤m pϑp−ϑ
′
p.

Therefore from Lemma 3.1.2 (iii), (9.3.35), (9.3.32) and (9.3.33), we have

∏

bi∈R bi < k!k−.5ℓ−1
 

n
−1
1 ∏

p≤m p1.5n(k,p)



 

 n0
2.71851
 ∏

p≤m p
 2
p2−1 (1− 1
pn(k,p) )


−k

(9.3.36)

and
 ∏

bi∈R bi < k!k1.5π(m)−.5ℓ−1
 

n
−1
1 n2 ∏

p≤m p.5+ 2
p2−1
 


 

 n0
2.71851
 ∏

p≤m p
 2
p2−1
 


−k
 .(9.3.37)

Comparing (9.3.36) and (9.3.37) with (9.3.30), we get

(9.3.38) zg1
1 k!
(k − g1)! > k.5ℓ+1
 

n
−1
1 ∏

p≤m p1.5n(k,p)



−1 

 z1n0
2.71851
 ∏

p≤m p
 2
p2−1 (1− 1
pn(k,p) )


k

and

(9.3.39) zg1
1 k!
(k − g1)! > k−1.5π(m)+.5ℓ+1
 

n
−1
1 n2 ∏

p≤m p.5+ 2
p2−1
 


−1 

 z1n0
2.71851
 ∏

p≤m p
 2
p2−1
 


k
 .

By Lemma 3.1.7, we have

zg1
1 k!
(k − g1)! < zg1
1 e
−g1(k − g1)
g1 ( k
k − g1
 )k+ 1
2 = ( z1(k − g1)
e
 )g1 (1 − g1
k
 )−k− 1
2 .

This together with (9.3.38) and (9.3.39) imply the assertions (9.3.28) and (9.3.29), respectively. □

9.4. Lemmas for the lower bound for n + (k − 1)d

We observe that |S1| ≥ |T1|
2ω(d)−θ and n + (k − 1)d ≥ |S1|k2. We give lower bound for |T1|. We
have

Lemma 9.4.1. Let k ≥ 4. Then

|T1| > t − (k − 1) log (k − 1) − ∑

p|d,p<k max (0, (k−1−p) log p
p−1 − log(k − 2)
)

log (n + (k − 1)d) − πd(k) − 1.(9.4.1)

Proof. The proof depends on an idea of Sylvester and Erd˝os and it is similar to [63, Lemma
3]. Since |T1| = t − |T |, we may assume that |T | > πd(k). For a prime q with q ≤ k and q ∤ d, let iq
be a term such that ordq(Biq ) is maximal. Let T ′ = T \ {iq : q ≤ k, q ∤ d}. Thus |T ′| ≥ |T | − πd(k).
Let i ∈ T ′. Then n + γid = Bi and ordq(n + γid) ≤ordq(γi − γiq ) since gcd(n, d) = 1. Therefore

ordq( ∏

i∈T ′(n + γid)) ≤ ordq((γiq )!(k − 1 − γiq )!) ≤ ordq(k − 1)!.

This, with n + id ≥ i
k−1 (n + (k − 1)d) for i > 0, gives

(|T ′| − 1)! ( n + (k − 1)d
k − 1
 )|T ′|−1 < ∏

i∈T ′(n + γid) ≤ (k − 1)!ϱ−1

where ϱ = ∏
q|d qordq(k−1)!. Therefore

(|T | − πd(k) − 1) log(n + (k − 1)d)

<(|T ′| − 1) log(k − 1) + log((k − 1) · · · |T ′|) − log ψ ≤ (k − 1) log(k − 1) − log ϱ.

74 9. NOTATION, PRELIMINARIES AND GENERAL LEMMAS

Now the assertion (9.4.1) follows from Lemma 3.1.6. □

Lemma 9.4.2. Let S ⊆ {Bi : 1 ≤ i ≤ t} and min
Bi∈SBi ≥ U . Let h ≥ 1 and P1 < P2 < · · · < Ph be

a subset of odd primes dividing d. Assume that

|S| > Q ( P1 − 1
2
 ) · · · ( Ph − 1
2
 )
(9.4.2)

where Q ≥ 1 is an integer. Then
 max
Bi∈SBi ≥ 2δQP1 · · · Ph + U.(9.4.3)

Proof. For an odd p|d, we have from
( Bi
p
 ) = ( BiY 2
i
p
 ) = ( n
p
 )

that Bi belongs to at most p−1
2 distinct residue classes modulo p. If d is even, then Bi also belongs
to a unique residue class modulo 2
δ. Hence, by Chinese remainder theorem, Bi belongs to at most
( P1−1
2 ) · · · ( Pj −1
2 ) distinct residue classes modulo 2δP1 · · · Pj for each j, 1 ≤ j ≤ h. Assume that

(9.4.3) does not hold. Then
 max
Bi∈SAi − (U − 1) ≤ 2δQP1 · · · Ph.

Therefore
 |S| ≤ 2δQP1 · · · Ph
2δP1 · · · Ph
 ( P1 − 1
2
 ) · · · ( Ph − 1
2
 )

contradicting (9.4.2). □

Corollary 9.4.3. Let S ⊆ {Bi : 1 ≤ i ≤ t}. Let h ≥ 1 and P1 < P2 < · · · < Ph be a subset of
odd primes dividing d. For |S| > ( P1−1
2 ) · · · ( Ph−1
2 ), we have

max
Bi∈SBi ≥
 




2δρ(|S| − 1) + 1 if h = 1, 2|d or 3|d
3
4 2h+δ|S| if 3 ∤ d, h > 1 if 2|d
9
8 2h+δ|S| if 3|d, h > 1.
(9.4.4)

Proof. The assertion (9.4.4) with h = 1, 2|d or 3|d follows by taking residue classes modulo 2δ

and 3. Thus we suppose h ≥ 2 if 2|d or 3|d. We have |S| = Q ( P1−1
2 ) + ε with Q ≥ 1, 0 ≤ ε < P1−1
2
if h = 1 and |S| = Q ( P1−1
2 ) · · · ( Ph−1
2 ) + Q
′ ( P1−1
2 ) · · · ( Ph−1−1
2 ) + ε with Q ≥ 1, 0 ≤ Q
′ < Ph−1
2

and 0 ≤ ε < ( P1−1
2 ) · · · ( Ph−1−1
2 ) if h > 1. If ε > 0, then we take Qh = Q, Q
′
h = Q
′, εh = ε; if

ε = 0, Q
′ > 0, we take Qh = Q, Q
′
h = Q
′ − 1, εh = ( P1−1
2 ) · · · ( Ph−1−1
2 ). If ε = 0, Q
′ = 0, then Q ≥ 2

and we take Qh = Q − 1, Q′
h = Ph−1
2 , εh = ( P1−1
2 ) · · · ( Ph−1−1
2 ). We write

|S| =
 {
Q1 ( P1−1
2 ) + ε1 if h = 1

Qh ( P1−1
2 ) · · · ( Ph−1
2 ) + Q
′
h ( P1−1
2 ) · · · ( Ph−1−1
2 ) + εh if h > 1.
(9.4.5)

We arrange the elements of S in increasing order and let S1
(h) ⊆ S be the ﬁrst εh elements. Further

for h > 1, let S2
(h) consist of the ﬁrst Q
′
h ( P1−1
2 ) · · · ( Ph−1−1
2 ) + εh elements of S. By taking modulo

2δ and ρ, we get max Bi ≥ 2δρ(εh − 1) + 1 for Bi ∈ S1
(h).
Let h = 1 and gcd(d, 6) = 1. Then we see from Lemma 9.4.2 with U = ε1, h = 1 and Q = Q1
that
 max
Bi∈SBi ≥ Q1P1 + ε1.

Now we observe from ε1 ≤ P1−1
2 and (9.4.5) that (9.4.4) is valid.

9.4. LEMMAS FOR THE LOWER BOUND FOR n + (k − 1)d 75

Thus h > 1. If Q
′ > 0, we apply Lemma 9.4.2 with S = S2
(h), U = 2
δρ(εh − 1) + 1, Q = Q
′
h to
derive
 max
Bi∈S2
(h)Bi ≥ 2δQ
′
hP1P2 · · · Ph−1 + 2δρ(εh − 1) + 1 := U1.

The same assertion is also valid when Q
′ = 0. Now we apply Lemma 9.4.2 in S with U = U1, Q = Qh
to get
 max
Bi∈SBi ≥ 2δQhP1P2 · · · Ph + 2δQ
′
hP1P2 · · · Ph−1 + 2δρ(εh − 1) + 1 := U ′.

Let 3 ∤ d. Since εh ≤ ( P1−1
2 ) · · · ( Ph−1−1
2 ) and (Ph−1 − 1)(Ph − 1) ≤ Ph−1Ph − 2Ph−1, for deriving

(9.4.4), it suﬃces to prove

QhP1 · · · Ph + Q
′
hP1 · · · Ph−1 ≥ 3
4 {QhP1 · · · Ph + (2Q
′
h + 2 − 2Qh)P1 · · · Ph−1} .

This follows from
 QhPh + 6(Qh − 1) − 2Q
′
h ≥ 0(9.4.6)

which is true since Qh ≥ 1 and Q
′
h ≤ Ph−1
2 .
Thus 3|d. Then P1 = 3. Let h = 2. Then ε = 1 since 1 ≤ ε ≤ P1−1
2 and it suﬃces to prove

QhP2 + Q
′
h ≥ 3
4 {Qh(P2 − 1) + 2Q
′
h + 2}

From Qh ≥ 1, Q′
h ≤ P2−1
2 , we see that QhP2 + 3(Qh − 2) − 2Q
′
h ≥ 0 if either Qh > 1 or Q
′
h < P2−1
2 .
Therefore we may suppose that Qh = 1 and Q
′
h < P2−1
2 implying |S| = 2( P2−1
2 ) + 1. Now we
get from Lemma 9.4.2 that Max Bi ≥ 2δ · 3 · 2P2 + 1 for Bi ∈ S. Now the assertion follows since
|S| = P2| + 1 and P2 ≥ 5. Hence h > 2. To derive (9.4.4), it is enough to prove

QhP2 · · · Ph + Q
′
hP2 · · · Ph−1 ≥ 3
4 {QhP2 · · · Ph + (2Q
′
h + 2 − 2Qh)P2 · · · Ph−1} .

As in 3 ∤ d, it follows from (9.4.6) which is true since Qh ≥ 1 and Q
′
h ≤ Ph−1
2 . □

Corollary 9.4.4. We have λ1 < 2
3 q1 if 2 ∤ d, 3 ∤ d and λ1 < q1
ρ2δ + 1 otherwise. For h ≥ 2, we
have
 λh <
 



 q1q2···qh
3·2h−2 if 2 ∤ d, 3 ∤ d
q1···qh
9·2h−3 if 2 ∤ d, 3|d
q1···qh
3·2δ+h−3 if 2|d, 3 ∤ d
min( q1···qh
3·2δ + 1, q1···qh
9·2h−2 ) if 6|d.

Proof. Let 2 ∤ d and 3 ∤ d. If λh ≥ q1···qr
3·2h−2 , then λh > q1−1
2 · · · qh−1
2 ≥ p1−1
2 · · · ph−1
2 giving
q1 · · · qh > max
Bi∈AhBi ≥ 3
4 2hλh by (9.4.4) with S = Ah. This is a contradiction.

Let 2|d or 3|d. Then we derive from Chinese remainder theorem that λh < q1···qh
ρ2δ + 1. Thus we
may suppose that h ≥ 2. Further we may also assume that h ≥ δ + 1 when 6|d.
Let 2 ∤ d and 3|d. Suppose λh ≥ q1···qh
9·2h−3 . Then q1 ≥ p1 = 3 implying λh > q2−1
2 · · · qh−1
2 ≥
p1−1
2 p2−1
2 · · · ph−1
2 . Therefore q1 · · · qh > 9
4 2h−1λh by (9.4.4) with S = Ah. This is a contradiction.
Let 2|d and 3 ∤ d. Suppose λh ≥ q1···qh
3·2δ+h−3 . Then qh ≥ 7 since h ≥ 2 implying q′ := max(qh, 2δ) ≥
7 implying

λh ≥ 2h−1q′

3 · 2δ+h−3 p1 − 1
2 · · · ph−1 − 1
2 ≥ q′

6 p1 − 1
2 · · · ph−1 − 1
2 > p1 − 1
2 · · · ph−1 − 1
2 .

Now we apply (9.4.4) with S = Ah to get a contradiction.

76 9. NOTATION, PRELIMINARIES AND GENERAL LEMMAS

Let 6|d. Suppose λh ≥ q1···qh
9·2h−2 . Let 2||d or 4||d. Then λh > q2−1
2 · · · qh−1−1
2 ≥ p1−1
2 p2−1
2 · · · ph−2−1
2
since q1qh ≥ 9 and p1 = 3. Now we apply (9.4.4) with S = Ah to get a contradiction. Thus it

remains to consider 8|d. Then λh > q2−1
2 · · · qh−1−1
2 ≥ p1−1
2 p2−1
2 · · · ph−1−1
2 since

λh ≥ 2h−2q1q′

9 · 2h−2 p1 − 1
2 · · · ph−2 − 1
2 > p1 − 1
2 · · · ph−2 − 1
2 .

where q′ := max(qh, 8). Now we apply (9.4.4) with S = Ah to get a contradiction. □

Let tν denote the ν-th odd squarefree positive integer. We recall here sν is the ν-th squarefree
positive integer. The next lemma gives a bound for sν and tν.

Lemma 9.4.5. We have
 si ≥ 1.6i f or i ≥ 78(9.4.7)

and
 ti ≥ 2.4i f or i ≥ 51.(9.4.8)

Further we have
 l∏

i=1 si ≥ (1.6)
ll! f or l ≥ 286(9.4.9)

and
 l∏

i=1 ti ≥ (2.4)
ll! f or l ≥ 200.(9.4.10)

Proof. The proof is similar to that of [63, (6.9)]. For (9.4.7) and (9.4.8), we check that
si ≥ 1.6i for 78 ≤ i ≤ 286 and ti ≥ 2.4i for 51 ≤ i ≤ 132, respectively. Further we observe that
in a given set of 144 consecutive integers, there are at most 90 squarefree integers and at most 60
odd squarefree integers by deleting multiples of 4, 9, 25, 49, 121 and 2, 9, 25, 49, respectively. Then
we continue as in the proof of [63, (6.9)] to get (9.4.7) and (9.4.8). Further we check that (9.4.9)
holds at l = 286 and (9.4.10) holds at l = 200. Then we use (9.4.7) and (9.4.8) to obtain (9.4.9) and
(9.4.10), respectively. □

Lemma 9.4.6. Let X > 1 be a positive integer. Then

X−1∑

i=1 2ω(i) ≤ ϕ(X)X log X(9.4.11)

where
 ϕ := ϕ(X) =
 




1 if X = 1
X−1∑

i=1 2ω(i)

X log X if 1 < X < 248
0.75 if X ≥ 248.

(9.4.12)

Proof. We check that (9.4.11) holds for 1 < X < 11500. Thus we may assume X ≥ 11500.
Let sj be the largest squarefree integer ≤ X. Then i ≥ 78 and hence by Lemma 9.4.5, we have
1.6j ≤ sj ≤ X so that j ≤ [ X
1.6 ]
. We have 2ω(i) = ∑

e|i |µ(e)|. Therefore

X−1∑

i=1 2ω(i) =
 X−1∑

i=1
 ∑

e|i |µ(e)| ≤ ∑

1≤e<X
 [ X − 1
e
 ] |µ(e)| ≤ (X − 1) ∑

1≤e<X
 |µ(e)|
e ≤ X [ X
1.6 ]∑

i=1
 1
si .

9.4. LEMMAS FOR THE LOWER BOUND FOR n + (k − 1)d 77

We check that there are 6990 squarefree integers upto 11500. By using (9.4.7), we have

X−1∑

i=1 2ω(i) ≤ X
 




6990∑

i=1
 1
si − 1
1.6
 6990∑

i=1
 1
i + 1
1.6
 [ X
1.6 ]∑

i=1
 1
i
 




≤ X
 {
6990∑

i=1
 1
si − 1
1.6
 6990∑

i=1
 1
i + 1
1.6
 (1 + log X
1.6
 )}

≤ 3
4 X log X { 4
3 1.1658
log X + 4
3 1
1.6
 }

implying (9.4.11). □

Lemma 9.4.7. Let c > 0 be such that c2ω(d)−3 > 1, µ ≥ 2 and

Cµ = {Bi : i ∈ T1, ν(Bi) = µ, Bi > ρ2δk
3c2ω(d) }.

Then
 C := ∑

µ≥2
 µ(µ − 1)
2 |Cµ| ≤ c
8 ϕ(c2ω(d)−3)2
ω(d)(2
ω(d)−θ − 1)(log c2ω(d)−3).(9.4.13)

Proof. Let i1 > i2 · · · > iµ be such that Bi1 = Bi2 = · · · = Biµ. These give rise to µ(µ−1)
2
pairs of (i, j), i > j with Bi = Bj. Therefore the total number of pairs (i, j) with i, j ∈ T1, i > j and
Bi = Bj > ρ2δk
3c2ω(d) is C.
We know that there is a unique partition of d corresponding to each pair (i, j), i > j such
that Bi = Bj. Hence by Box Principle, there exists at least C
2ω(d)−θ−1 pairs of (i, j), i > j with
Bi = Bj and a partition (d1, d2) of d corresponding to these pairs. For every such pair (i, j), we
write Yi − Yj = d1rij, Yi + Yj = d2sij. Then gcd(Yi − Yj, Yi + Yj) = 2 and 24|(Y 2
i − Y 2
j ). Hence

24
ρ2δ |rijsij. Let r′
ij = rij
gcd(rij , 24
ρ2δ ) and s
′
ij = sij
gcd(sij , 24
ρ2δ ) so that r′
ijs
′
ij = ρ2δ

24 rijsij. Then

r′
ijs
′
ij = ρ2δ

24 rijsij = ρ2δ

24 Y 2
i − Y 2
j
d = ρ2δ

24 i − j
Bi < ρ2δ

24 k
Bi < c2ω(d)−3

since Bi > ρ2δk
3c2ω(d) . There are at most
 c2ω(d)−3−1∑

i=1 2ω(i) possible pairs of (r′
ij, s′
ij), and hence an equal

number of possible pairs of (rij, sij). By Lemma 9.4.6, we estimate

c2ω(d)−3−1∑

i=1 2ω(i) ≤ ϕ(c2ω(d)−3)c2ω(d)−3(log c2ω(d)−3).

Thus if we have C
2ω(d)−θ − 1 > ϕ(c2ω(d)−3)c2ω(d)−3(log c2ω(d)−3),

then there exist distinct pairs (i, j) ̸= (g, h), i > j, g > h with Bi = Bj, Bg = Bh such that
rij = rgh, sij = sgh giving

Yi − Yj = d1rij = Yg − Yh and Yi + Yj = d2sij = Yg + Yh.

Thus Yi = Yg, Yj = Yh implying (i, j) = (g, h), a contradiction. Hence

C
2ω(d)−θ − 1 ≤ ϕ(c2ω(d)−3)c2ω(d)−3(log c2ω(d)−3)

implying (9.4.13). □

78 9. NOTATION, PRELIMINARIES AND GENERAL LEMMAS

9.5. Estimates on the general upper bound of ν(a) for a ∈ R

In this section, we give upper bound of ν(a) with a ∈ R which are independent of ω(d).

Let ¯f (x) = ⌈x
⌉ − [ ⌈x
⌉

4 ] for x > 0 and Ka = k
a23−δ for a ∈ R. We have

Lemma 9.5.1. Let a ∈ R and µ be a positive integer. Let p, q be distinct odd primes.
(i) Let f0(k, a, δ) = ¯f (Ka),
f1(k, a, p, µ, δ) = p − 1
2
 µ−1∑

l=0 ¯f ( Ka
p2l+1 ) + ¯f ( Ka
p2µ )

and
 f2(k, a, p, q, µ, δ) = p − 1
2
 µ−1∑

l=0
 ( q − 1
2 ¯f ( Ka
p2l+1q ) + ¯f ( Ka
p2l+1q2 )
) + ¯f ( Ka
p2µ ).

Then
 νo(a) ≤
 




f0(k, a, δ)
f1(k, a, p, µ, δ) if p ∤ d
f2(k, a, p, q, µ, δ) if p ∤ d, q ∤ d.
(9.5.1)

(ii) Let d be odd. Let
 g0(k, a, µ) =
 µ−1∑

l=1 ¯f ( Ka
22l ) + ¯f ( k
a22µ ),

g1(k, a, p, µ) = p − 1
2
 µ−1∑

l=0
 2∑

j=1 ¯f ( Ka
2jp2l+1 ) +
 2∑

j=1 ¯f ( Ka
2jp2µ )

and
 g2(k, a, p, q, µ) = p − 1
2
 µ−1∑

l=0
 2∑

j=1
 ( q − 1
2 ¯f ( Ka
2jp2l+1q ) + ¯f ( Ka
2jp2l+1q2 )
) +
 2∑

j=1 ¯f ( Ka
2jp2µ ).

Then
 νe(a) ≤
 




g0(k, a, µ)
g1(k, a, p, µ) if p ∤ d
g2(k, a, p, q, µ) if p ∤ d, q ∤ d.
(9.5.2)

Proof. Let I ⊆ {i : ai = a} and τ |(i − j) whenever i, j ∈ I. Let τ ′ be the lcm of all τ1
such that τ1|(i − j) whenever i, j ∈ I. Then τ |τ ′ and a|τ ′ since a|(i − j) whenever i, j ∈ I. Let
i0 = min
i∈I i, N = n+i0d
a and D = τ ′
a d. Then we see that ax
2
i with i ∈ I come from the squares in

the set {N, N + D, · · · , N + (⌈ k−i0
τ ⌉ − 1)D}. Dividing this set into consecutive intervals of length 4

and using Euler’s result, we see that there are at most ⌈ k−i0
τ ′ ⌉ − [ ⌈ k−i0
τ ′ ⌉

4 ] ≤ ⌈ k
τ ′ ⌉ − [ ⌈ k
τ ′ ⌉

4 ] = ¯f ( k
τ ′ ) of
them which can be squares. Hence |I| ≤ ¯f ( k
τ ′ ) ≤ ¯f ( k
τ ) since τ |τ ′.
Let I o = {i : ai = a, 2 ∤ xi} and I e = {i : ai = a, 2|xi}. Then νo(a) = |I o| and νe(a) = |I e|.
First we prove (9.5.1). For i, j ∈ I o, we observe from x
2
i , x
2
j ≡ 1(mod 8) and (i−j)d = a(x
2
i −x
2
j )
that a23−δ|(i − j). Therefore |I o| ≤ ¯f (Ka) = f0(k, a, δ).
For a prime p′, let
 Qp′ = {m : 1 ≤ m < p′, ( m
p′
 ) = 1}.

Let p ∤ d. Let
 I o
l = {i ∈ I o : pl||xi} for 0 ≤ l < µ and I o
µ = {i ∈ I o : pµ|xi}.

9.5. ESTIMATES ON THE GENERAL UPPER BOUND OF ν(a) FOR a ∈ R 79

Then a23−δp2µ|(i − j) whenever i, j ∈ I o
µ giving |I o
µ| ≤ ¯f ( Ka
p2µ ). For each l, 0 ≤ l < µ and for each
m ∈ Qp, let
 I o
lm = {i ∈ I o
l : ( xi
pl )
2 ≡ m(mod p)}.

Then a23−δp2l+1|(i−j) whenever i, j ∈ I o
lm giving |I o
lm| ≤ ¯f ( Ka
p2l+1 ). Therefore |I o
l | = ∑

m∈Qp |I o
lm| ≤

p−1
2 ¯f ( Ka
p2l+1 ). Hence |I o| = |I o
µ| + ∑µ−1
l=0 |I o
l | ≤ f1(k, a, p, µ, δ).
Thus we may assume that p ∤ d and q ∤ d. For each l with 0 ≤ l < µ, m ∈ Qp and for each
u ∈ Qq, let
 I o
lmu = {i ∈ I o
lm : x
2
i ≡ u(mod q)} and I o
lm0 = {i ∈ I o
lm : q|xi)}.

Then a23−δp2l+1q|(i − j) for i, j ∈ I o
lmu and a23−δp2l+1q2|(i − j) for i, j ∈ I o
lm0 implying |I o
lmu| ≤
¯f ( Ka
p2l+1q ) for u ∈ Qq and |I o
lm0| ≤ ¯f ( Ka
p2l+1q2 ). Now the assertion νo(a) ≤ f2(k, a, p, q, µ, δ) follows
from
 |I o
lm| ≤ |I o
lm0| + ∑

u∈Qq |I o
lmu|, |I o
l | = ∑

m∈Qp |I o
lm|, and |I o| = |I o
µ| +
 µ−1∑

l=0 |I o
l |.

Now we turn to the proof of (9.5.2). Let

I el = {i ∈ I e : 2
l||xi} for 1 ≤ l < µ and I eµ = {i ∈ I e : 2
µ|xi}.

Since xi
2l is odd, we get a22l+3|(i − j) whenever i, j ∈ I el implying |I el| ≤ ¯f ( Ka
22l ) for 0 ≤ l < µ.
Further a22µ|(i − j) for i, j ∈ I eµ giving |I eµ| ≤ ¯f ( k
a22µ ). Now the assertion νe(a) ≤ g0(k, a, µ) from
|I e| = |I eµ| + ∑

l<µ |I el|.
For the remaining proofs of (9.5.2), we consider I e1 = {i ∈ I e : 2||xi}, I e2 = {i ∈ I e : 4|xi}
so that |I e| = |I e1| + |I e2|. Then 32a|(i − j) for i, j ∈ I e1 and 16a|(i − j) for i, j ∈ I e2. We now
continue the proof as in that of (9.5.1) with I e1, I e2 in place of I o to get νe(a) ≤ g1(k, a, p, µ) when
p ∤ d and νe(a) ≤ g2(k, a, p, q, µ) when p ∤ d, q ∤ d. □

From Lemma 9.5.1, we derive

Lemma 9.5.2. For a ∈ R, let

f3(k, a, δ) =
 




1 if k ≤ a23−δ

¯f (Ka) if k > a23−δ, 3|d, 5|d
¯f ( Ka
3 ) + ¯f ( Ka
9 ) if k > a23−δ, 3 ∤ d, 5|d
¯f (Ka) if a23−δ < k ≤ 2a23−δ, 3|d, 5 ∤ d
2 ¯f ( Ka
5 ) + ¯f ( Ka
25 ) if k > 2a23−δ, 3|d, 5 ∤ d
¯f ( Ka
3 ) + ¯f ( Ka
9 ) if a23−δ < k ≤ 24a23−δ, 3 ∤ d, 5 ∤ d
2 ( ¯f ( Ka
15 ) + ¯f ( Ka
135 )
) +
¯f ( Ka
75 ) + ¯f ( Ka
675 ) + ¯f ( Ka
81 ) if 24a23−δ < k ≤ 324a23−δ, 3 ∤ d, 5 ∤ d
2 ( ¯f ( Ka
15 ) + ¯f ( Ka
135 ) + ¯f ( Ka
1215 )
) +
¯f ( Ka
75 ) + ¯f ( Ka
675 ) + ¯f ( Ka
6075 ) + ¯f ( Ka
729 ) if k > 324a23−δ, 3 ∤ d, 5 ∤ d

80 9. NOTATION, PRELIMINARIES AND GENERAL LEMMAS

and
 g3(k, a) =
 




1 if k ≤ 4a
∑2
j=1 ¯f ( Ka
2j ) if 4a < k ≤ 32a
∑2
j=1 ¯f ( Ka
2j ) k > 32a, 3|d, 5|d
∑2
j=1 ( ¯f ( Ka
2·3j ) + ¯f ( Ka
4·3j )
) if k > 32a, 3 ∤ d, 5|d
∑2
j=1 ¯f ( Ka
2j ) 32a < k ≤ 64a, 3|d, 5 ∤ d
2 ∑2
j=1 ¯f ( Ka
2j ·5 ) + ∑2
j=1 ¯f ( Ka
2j ·25 ) if k > 64a, 3|d, 5 ∤ d
∑2
j=1 ∑2
l=1 ¯f ( Ka
2j ·3l ) if 32a < k ≤ 576a, 3 ∤ d, 5 ∤ d
2 ∑2
j=1 ∑2
l=1 ¯f ( Ka
2j ·32l−1·5 )+
∑2
j=1 ∑2
l=1 ¯f ( Ka
2j ·32l−1·25 ) + ∑2
j=1 ¯f ( Ka
2j ·81 ) if k > 576a, 3 ∤ d, 5 ∤ d.

Then for a ∈ R, we have
 νo(a) ≤ f3(k, a, δ), νe(a) ≤ g3(k, a)

and
 ν(a) ≤ F0(k, a, δ) :=
 




1 if k ≤ a
f3(k, a, δ) if k > a and d even
f3(k, a, 0) + g3(k, a) if k > a and d odd.

Proof. Since a|(i − j) whenever ai = aj = a, we get ν(a) ≤ 1, νo(a) ≤ 1, νe(a) ≤ 1 for k ≤ a.
In fact νo(a) ≤ 1 for k ≤ a23−δ and νe(a) ≤ 1 for k ≤ 4a. Thus we suppose that k > a. We have
ν(a) = νo(a) + νe(a). It suﬃces to show νo(a) ≤ f3(k, a, δ) for k > a23−δ and νe(a) ≤ g3(k, a) for
k > 4a since νe(a) = 0 for d even. From (9.5.1), we get the assertion νo(a) ≤ f3(k, a, δ) for k > a23−δ

since
 νo(a) ≤
 




f0(k, a, δ) if 15|d
f1(k, a, 3, 1, δ) if 3 ∤ d, 5|d
min(f0(k, a, δ), f1(k, a, 5, 1, δ)) if 3|d, 5 ∤ d
min(f1(k, a, 3, 1, δ), f2(k, a, 3, 5, 2, δ),
f2(k, a, 3, 5, 3, δ)) if 3 ∤ d, 5 ∤ d.

The assertion νe(a) ≤ g3(k, a) for k > 4a follows from (9.5.2) since νe(a) ≤ g0(k, a, 2) for 4a < k ≤
32a and
 νe(a) ≤
 




g0(k, a, 2) if 15|d
g1(k, a, 3, 1)) if 3 ∤ d, 5|d
min(g0(k, a, 2), g1(k, a, 5, 1)) if 3|d, 5 ∤ d
min(g1(k, a, 3, 1), g2(k, a, 3, 5, 2)) if 3 ∤ d, 5 ∤ d

for k > 32a. □

We observe that there are p−1
2 distinct quadratic residues and p−1
2 distinct quadratic non-residue
modulo an odd prime p. The next lemma follows easily from this fact.

Lemma 9.5.3. Assume (2.1.1) holds. Let k be an odd prime. Suppose that k ∤ d. Then ν(a) ≤
k−1
2 for any a ∈ R.
 CHAPTER 10

Extensions of a result of Euler:
Proof of Theorems 2.1.1, 2.2.1 and 2.2.2

10.1. Introduction

For the convenience of the proofs, we consider Theorems 2.2.1 and 2.2.2 together. Therefore we
formulate

Theorem 10.1.1.
Let d > 1, P (b) ≤ k and 5 ≤ k ≤ 100. Suppose that k ̸= 5 if P (b) = k. Then (2.1.1) does not
hold except for the (a0, a1, · · · , ak−1) among (2.2.2), (2.2.3) and their mirror images.

It is clear that Theorem 10.1.1 implies Theorems 2.2.1 and 2.2.2. In fact the proof of Theorem
10.1.1 provides a method for solving (2.1.1) for any given value of k. We have restricted k up to 100
for keeping the computational load under control. We begin by proving the assertion for k = 5.

10.2. The case k = 5

Let k = 5. We show that (2.1.1) with P (b) < k does not hold.
Assume that n(n + d)(n + 2d)(n + 3d)(n + 4d) = by2 where b ∈ {1, 2, 3, 6}. Then

(n + 2d)
2{(n + 2d)
2 − d2}{(n + 2d)
2 − 4d2} = b′y′2

where (n+2d)by2 = b′y′2, b′ is the squarefree part of b(n+2d) and further b′ ∈ {1, 2, 3, 6}. Multiplying
both sides by b′3
d6 and putting X = b′ (n+2d)2

d2 , Y = b′2y′

d3 , we obtain the elliptic equation

Y 2 = X(X − b′)(X − 4b′) = X 3 − 5b′X 2 + 4b′2X.

For b′ ∈ {1, 2, 3, 6}, we check using MAGMA that the above curves have rank 0. Further the torsion
points are given by
 b′ = 1 : (X, Y ) = (0, 0), (1, 0), (4, 0),

b′ = 2 : (X, Y ) = (0, 0), (2, 0), (8, 0),

b′ = 3 : (X, Y ) = (0, 0), (3, 0), (12, 0),

b′ = 6 : (X, Y ) = (0, 0), (6, 0), (24, 0).

We observe from Y > 0 that the above torsion points do not give any solution for (2.1.1). □
From now on, we may suppose throughout this chapter that k > 5.

10.3. A Covering Lemma

In this section, we give a lemma central to the proof of Theorem 10.1.1.
Let q1, q2 be distinct primes and

Λ1(q1, q2) := {p ≤ 97 : ( p
q1
 ) ̸= ( p
q2
 )}.

We write Λ(q1, q2) = Λ(q1, q2, k) := {p ∈ Λ1(q1, q2) : p ≤ k}. We compute

Lemma 10.3.1. We have
 81

82 10. PROOF OF THEOREMS 2.1.1, 2.2.1 AND 2.2.2

(q1, q2) Λ1(q1, q2)
(5, 11) {3, 19, 23, 29, 37, 41, 47, 53, 61, 67, 79, 97}
(7, 17) {11, 13, 19, 23, 29, 37, 47, 59, 71, 79, 83, 89}
(11, 13) {5, 17, 29, 31, 37, 43, 47, 59, 61, 67, 71, 79, 89, 97}
(11, 59) {7, 17, 19, 23, 29, 31, 37, 41, 47, 67, 79, 89, 97}
(11, 61) {13, 19, 23, 31, 37, 41, 53, 59, 67, 71, 73, 83, 89}
(19, 29) {11, 13, 17, 43, 47, 53, 59, 61, 67, 71, 73}
(23, 73) {13, 19, 29, 31, 37, 47, 59, 61, 67, 79, 89, 97}
(23, 97) {11, 13, 29, 41, 43, 53, 59, 61, 71, 79, 89}
(31, 89) {7, 11, 17, 19, 41, 53, 59, 73, 79}
(37, 83) {17, 23, 29, 31, 47, 53, 59, 61, 67, 71, 73}
(41, 79) {11, 13, 19, 37, 43, 59, 61, 67, 89, 97}
(43, 53) {7, 23, 29, 31, 37, 41, 67, 79, 83, 89}
(43, 67) {11, 13, 19, 29, 31, 37, 41, 53, 71, 73, 79, 89, 97}
(53, 67) {7, 11, 13, 19, 23, 43, 71, 73, 83, 97}
(59, 61) {7, 13, 17, 29, 47, 53, 71, 73, 79, 83, 97}
(73, 97) {11, 19, 23, 31, 37, 41, 43, 47, 53, 67, 71}
(79, 89) {13, 17, 19, 23, 31, 47, 53, 71, 83}

Let P be a set of primes and I ⊆ [0, k) ∩ Z. We say that I is covered by P if, for every j ∈ I,
there exists p ∈ P such that p|aj. Further for i ∈ I, let

i(P) = |{p ∈ P : p divides ai}|.(10.3.1)

For a prime p with gcd(p, d) = 1, let ip be the smallest i ≥ 0 such that p|n + id. For I ⊆ [0, k) ∩ Z
and primes p1, p2 with gcd(p1p2, d) = 1, we write

I ′ = I(p1, p2) = I \ ∪
2
j=1{ipj + pji : 0 ≤ i < ⌈ k
pj
 ⌉}.

Lemma 10.3.2. Let P0 be a set of primes. Let p1, p2 be primes such that gcd(p1p2, d) = 1. Let
(i1, i2) = (ip1, ip2), I ⊆ [0, k) ∩ Z and I ′ = I(p1, p2) be such that i(P0 ∩ Λ(p1, p2)) is even for each
i ∈ I ′. Deﬁne

I1 = {i ∈ I ′ : ( i − i1
p1
 ) = ( i − i2
p2
 )} and I2 = {i ∈ I ′ : ( i − i1
p1
 ) ̸= ( i − i2
p2
 )}.

Let P = Λ(p1, p2) \ P0. Let ℓ be the number of terms n + id with i ∈ I ′ divisible by primes in P.
Then either
 |I1| ≤ ℓ, I1 is covered by P, I2 = {i ∈ I ′ : i(P) is even}

or
 |I2| ≤ ℓ, I2 is covered by P, I1 = {i ∈ I ′ : i(P) is even}.

We observe that ℓ ≤ ∑

p∈P ⌈ k
p ⌉.

Proof. Let i ∈ I ′. Let U0 = {p : p|ai}, U1 = {p ∈ U0 : p /∈ Λ(p1, p2)}, U2 = {p ∈ U0 : p ∈
P0 ∩ Λ(p1, p2)} and U3 = {p ∈ U0 : p ∈ P}. Then we have from ai = ∏
p∈U0 p that
( ai
p1
 ) = ∏

p∈U1
 ( p
p1
 ) ∏

p∈U2
 ( p
p1
 ) ∏

p∈U3
 ( p
p1
 ) = (−1)
i(P)+|U2| ∏

p∈U0
 ( p
p2
 ) = (−1)
i(P) ( ai
p2
 )

since |U2| = i(P0 ∩ Λ(p1, p2)) is even. Therefore

L := {i ∈ I ′ : ( ai
p1
 ) ̸= ( ai
p2
 )} = {i ∈ I ′ : i(P) is odd}.(10.3.2)

In particular L is covered by P and hence
 |L| ≤ ℓ.(10.3.3)
 10.4. LEMMAS FOR THE PROOF OF THEOREM 10.1.1 (CONTD.) 83

We see that ( ai
pj
 ) = ( n+id
pj
 ) = ( i−ij
pj
 ) ( d
pj
 ) for i ∈ I ′ and j = 1, 2. Therefore L = I1 or I2 according

as ( d
p1
 ) ̸= ( d
p2
 ) or ( d
p1
 ) = ( d
p2
 ), respectively. Now the assertion of the Lemma 10.3.2 follows from

(10.3.2) and (10.3.3). □

Let P consist of one prime p. We observe that p|n + id if and only if p|(i − ip). Then I1 or I2
is contained in one residue class modulo p and p ∤ ai for i in the other set.

Corollary 10.3.3. Let p1, p2, i1, i2, P0, P, I, I ′, I1, I2 and ℓ be as in Lemma 10.3.2. Assume
that
 ℓ < 1
2 |I ′|.(10.3.4)

Then |I1| ̸= |I2|. Let
 M =
 {
I1 if |I1| < |I2|
I2 otherwise
(10.3.5)

and
 B =
 {
I2 if |I1| < |I2|
I1 otherwise.
(10.3.6)

Then |M| ≤ ℓ, M is covered by P and B = {i ∈ I ′|i(P) is even}.

Proof. We see from Lemma 10.3.2 that min(|I1|, |I2|) ≤ ℓ and from (10.3.4) that max(|I1|, |I2|) ≥
1
2 |I ′| > ℓ. Now the assertion follows from Lemma 10.3.2. □

We say that (M, B, P, ℓ) has P roperty H if |M| ≤ ℓ, M is covered by P and i(P) is even for
i ∈ B.
 10.4. Lemmas for the Proof of Theorem 10.1.1 (contd.)

We recall that (2.1.1) is the equation (9.1.1) with t = k and γi = i − 1 so that (9.1.2) and (9.1.3)
give (2.1.2) and (9.1.4) is (2.1.3). Further we have R = {ai : 0 ≤ i < k}. For the proof of Theorem
10.1.1, we use the following Corollary which follows from Lemma 9.5.2.

Corollary 10.4.1. For a ∈ R, let

f4(k, a, δ) =
 




1 if k ≤ a23−δ

¯f (Ka) if k > a23−δ, 3|d
¯f ( Ka
3 ) + ¯f ( Ka
9 ) if k > a23−δ, 3 ∤ d

and
 g4(k, a) =
 




1 if k ≤ 4a
⌈ Ka
2 ⌉ + 1 if 4a < k ≤ 32a
¯f ( Ka
2 ) + ¯f ( Ka
4 ) if k > 32a, 3|d
¯f ( Ka
6 ) + ¯f ( Ka
12 ) + ¯f ( Ka
18 ) + ¯f ( Ka
36 ) if k > 32a, 3 ∤ d.

Then we have
 νo(a) ≤ f4(k, a, δ), νe(a) ≤ g4(k, a)

and
 ν(a) ≤ F1(k, a, δ) :=
 




1 if k ≤ a
f4(k, a, δ) if k > a and d even
f4(k, a, 0) + g4(k, a) if k > a and d odd.

84 10. PROOF OF THEOREMS 2.1.1, 2.2.1 AND 2.2.2

Lemma 10.4.2. Let k be a prime with 7 ≤ k ≤ 97 and assume (2.1.1). For k ≥ 11, assume that
Theorem 10.1.1 is valid for all primes k1 with 7 ≤ k1 < k. For 11 ≤ k ≤ 29, assume that k ∤ d and
k ∤ n + id for 0 ≤ i < k − k′ and k′ ≤ i < k where k′ < k are consecutive primes. Let (q1, q2) = (5, 7)
if k = 7; (5, 11) if k = 11; (11, 13) if 13 ≤ k ≤ 23; (19, 29) if 29 ≤ k ≤ 59; (59, 61) if k = 61; (43, 67)
if k = 67, 71; (23, 73) if k = 73, 79; (37, 83) if k = 83; (79, 89) if k = 89 and (23, 97) if k = 97. Then
q1|d or q2|d unless (a0, a1, · · · , ak−1) is given by the following or their mirror images.

k = 7 : (2, 3, 1, 5, 6, 7, 2), (3, 1, 5, 6, 7, 2, 1), (1, 5, 6, 7, 2, 1, 10);

k = 13 : (3, 1, 5, 6, 7, 2, 1, 10, 11, 3, 13, 14, 15), (1, 5, 6, 7, 2, 1, 10, 11, 3, 13, 14, 15, 1);

k = 19 : (1, 5, 6, 7, 2, 1, 10, 11, 3, 13, 14, 15, 1, 17, 2, 19, 5, 21, 22);

k = 23 : (5, 6, 7, 2, 1, 10, 11, 3, 13, 14, 15, 1, 17, 2, 19, 5, 21, 22, 23, 6, 1, 26, 3),

(6, 7, 2, 1, 10, 11, 3, 13, 14, 15, 1, 17, 2, 19, 5, 21, 22, 23, 6, 1, 26, 3, 7).

We shall prove Lemma 10.4.2 in Section 10.5.

Lemma 10.4.3. Let k be a prime with 29 ≤ k ≤ 97 and Q0 a prime dividing d. Assume (2.1.1)
with k ∤ d and k ∤ n + id for 0 ≤ i < k − k′ and k′ ≤ i < k where k′ < k are consecutive primes.
Then there are primes Q1 and Q2 given in the following table such that either Q1|d or Q2|d.
k Q0 (Q1, Q2) k Q0 (Q1, Q2)
29 ≤ k ≤ 59 19 (7, 17) 73, 79 23 (53, 67)
31 ≤ k ≤ 59 29 (7, 17) 79 73 (53, 67)
61 59 (11, 61) 83 37 (23, 73)
67, 71 43 (53, 67) 89 79 (23, 73)
71 67 (43, 53) 97 23 (73, 97), (37, 83)

The proofs of Lemmas 10.4.2 and 10.4.3 depend on the repeated application of Lemma 10.3.2
and Corollary 10.3.3. We shall prove Lemma 10.4.3 in section 10.6. Next we apply Lemmas 10.4.1,
9.5.3 and 10.4.3 to prove the following result.

Lemma 10.4.4. Let k be a prime with 7 ≤ k ≤ 97. Assume (2.1.1) with k ∤ d. Further for
k ≥ 29, assume that k ∤ n + id for 0 ≤ i < k − k′ and k′ ≤ i < k where k′ < k are consecutive
primes. Let (q1, q2) be as in Lemma 10.4.2. Then q1 ∤ d and q2 ∤ d.

The Section 10.7 contains a proof of Lemma 10.4.4. Assume that 3 ∤ d and 5 ∤ d. We deﬁne
some more notation. For a subset J ⊆ [0, k) ∩ Z, let

I 0
3 = I 0
3 (J ) := {i ∈ J |i ≡ i3(mod 3)}, I +
3 = I +
3 (J ) := {i ∈ J | ( i − i3
3
 ) = 1},

I −
3 = I −
3 (J ) := {i ∈ J | ( i − i3
3
 ) = −1}

and
 I +
5 = I +
5 (J ) := {i ∈ J | ( i − i5
5
 ) = 1}, I −
5 = I −
5 (J ) := {i ∈ J | ( i − i5
5
 ) = −1}.

Assume that ai ∈ {1, 2, 7, 14} for i ∈ I +
3 ∪ I −
3 . Then either ai ∈ {1, 7} for i ∈ I +
3 , ai ∈ {2, 14} for
i ∈ I −
3 or ai ∈ {2, 14} for i ∈ I +
3 , ai ∈ {1, 7} for i ∈ I −
3 . We deﬁne (I 1
3 , I 2
3 ) = (I +
3 , I −
3 ) in the
ﬁrst case and (I 1
3 , I 2
3 ) = (I −
3 , I +
3 ) in the latter. We observe that i’s have the same parity whenever
ai ∈ {2, 14}. Thus if i’s have the same parity in one of I +
3 or I −
3 but not in both, then we see that
(I 1
3 , I 2
3 ) = (I +
3 , I −
3 ) or (I −
3 , I +
3 ) according as i’s have the same parity in I −
3 or I +
3 , respectively.
Further we write
 J1 = I 1
3 ∩ I +
5 , J2 = I 1
3 ∩ I −
5 , J3 = I 2
3 ∩ I +
5 , J4 = I 2
3 ∩ I −
5

and aµ = {ai|i ∈ Jµ} for 1 ≤ µ ≤ 4. Since ( 1
5 ) = ( 14
5 ) = 1 and ( 2
5 ) = ( 7
5 ) = −1, we see that

(a1, a2, a3, a4) ⊆ ({1}, {7}, {14}, {2}) or ({7}, {1}, {2}, {14})(10.4.1)
 10.5. PROOF OF LEMMA 10.4.2 85

where (a1, a2, a3, a4) ⊆ (S1, S2, S3, S4) denotes aµ ⊆ Sµ, 1 ≤ µ ≤ 4. We use 7|(i − i
′) whenever
ai, ai′ ∈ {7, 14} to exclude one of the above possibilities.

10.5. Proof of Lemma 10.4.2

Let k′ < k be consecutive primes. We may suppose that if (2.1.1) holds for some k > 29, then
k ∤ d and k ∤ ai for 0 ≤ i < k − k′ and k′ ≤ i < k, otherwise the assertion follows from Theorem
10.1.1 with k replaced by k′. The subsections 3.1 to 3.10 will be devoted to the proof of Lemma
10.4.2. We may assume that q1 ∤ d and q2 ∤ d otherwise the assertion follows.

10.5.1. The case k = 7. Then 5 ∤ d. By taking mirror images (2.2.1) of (2.1.1), there is no loss
of generality in assuming that 5|n + i5d, 7|n + i7d for some pair (i5, i7) with 0 ≤ i5 < 5, 0 ≤ i7 ≤ 3.
Further we may suppose i7 ≥ 1, otherwise the assertion follows from the case k = 6. We apply
Lemma 10.3.2 with P0 = ∅, p1 = 5, p2 = 7, (i1, i2) = (i5, i7), I = [0, k) ∩ Z, P = Λ(5, 7) = {2} and
ℓ ≤ ℓ1 = ⌈ k
2 ⌉ to conclude that either

|I1| ≤ ℓ1, I1 is covered by P, I2 = {i ∈ I ′|i(P) is even}

or
 |I2| ≤ ℓ1, I2 is covered by P, I1 = {i ∈ I ′|i(P) is even}.

Let (i5, i7) = (3, 1). Then I1 = {0, 2, 6} and I2 = {4, 5}. We see that I1 is covered by P and hence
i(P) is even for i ∈ I2. Thus 2 ∤ ai for i ∈ I2. Therefore a4, a5 ∈ {1, 3} and a0, a2, a6 ∈ {2, 6}.
If a0 = 6 or a6 = 6, then 3 ∤ a4a5 so that a4 = a5 = 1. This is not possible by modulo 3. Thus

a0 = a6 = 2. Since ( a0
5 ) ( a2
5 ) = ( (−3d)(−d)
5 ) = −1, we get a2 = 6. Hence a4 = 1. Further

a5 = 3 since ( a5
5 ) ( a4
5 ) = ( (2d)(1d)
5 ) = −1. Also 5|a3 and 7|a1, otherwise the assertion follows

from the results [45] for k = 5 and [1] for k = 6, respectively, stated in Section 7.2. In fact
a1 = 7, a3 = 5 by gcd(a1a3, 6) = 1. Thus (a0, a1, a2, a3, a4, a5, a6) = (2, 7, 6, 5, 1, 3, 2). The proofs for
the other cases of (i5, i7) are similar. We get (a0, · · · , a6) = (1, 5, 6, 7, 2, 1, 10) when (i5, i7) = (1, 3),
(a0, · · · , a6) = (1, 2, 7, 6, 5, 1, 3) when (i5, i7) = (4, 2) and all the other pairs are excluded. Hence
Lemma 10.4.2 with k = 7 follows. □

10.5.2. The case k = 11. Then 5 ∤ d. By taking mirror images (2.2.1) of (2.1.1), there is no
loss of generality in assuming that 5|n + i5d, 11|n + i11d for some pair (i5, i11) with 0 ≤ i5 < 5, 4 ≤
i11 ≤ 5. We apply Lemma 10.3.2 with P0 = ∅, p1 = 5, p2 = 11, (i1, i2) = (i5, i11), I = [0, k) ∩ Z,
P = Λ(5, 11) = {3} and ℓ ≤ ℓ1 = ⌈ k
3 ⌉ to derive that either

|I1| ≤ ℓ1, I1 is covered by P, I2 = {i ∈ I ′|i(P) is even}

or
 |I2| ≤ ℓ1, I2 is covered by P, I1 = {i ∈ I ′|i(P) is even}.

We compute I1, I2 and we restrict to those pairs (i5, i11) for which min(|I1|, |I2|) ≤ ℓ1 and either I1
or I2 is covered by P. We ﬁnd that (i5, i11) = (0, 4), (1, 5). Let (i5, i11) = (0, 4). Then I1 = {3, 9}
is covered by P, i3 = 0 and i(P) is even for i ∈ I2 = {1, 2, 6, 7, 8}. Thus 3 ∤ ai for i ∈ I2. Further
p ∈ {2, 7} whenever p|ai with i ∈ I2. Therefore ai ∈ {1, 2, 7, 14} for i ∈ I2. By taking J = I2, we
have I2 = I 0
3 ∪ I +
3 ∪ I −
3 and I2 = I +
5 ∪ I −
5 with

I 0
3 = {6}, I +
3 = {1, 7}, I −
3 = {2, 8}, I +
5 = {1, 6}, I −
5 = {2, 7, 8}.

Let (I 1
3 , I 2
3 ) = (I +
3 , I −
3 ). Then

J1 = {1}, J2 = {7}, J3 = ∅, J4 = {2, 8}.

The possibility (a1, a2, a3, a4) ⊆ ({7}, {1}, {2}, {14}) is excluded since 7|(i − i
′) whenever ai, ai′ ∈
{7, 14}. Therefore a1 = 1, a7 = 7, a2 = a8 = 2. Further a6 = 1 since 6 ∈ I +
5 and a1 = 1, a7 = 7.

This is not possible since 1 = ( a6
7 ) ( a8
7 ) = ( (−d)(d)
7 ) = −1. Let (I 1
3 , I 2
3 ) = (I −
3 , I +
3 ). Then we argue
as above to conclude that a2 = a8 = 1, a1 = 2, a7 = 14 which is not possible since n + 2d and n + 8d
cannot both be odd squares. The other case (i5, i11) = (1, 5) is excluded similarly. □

86 10. PROOF OF THEOREMS 2.1.1, 2.2.1 AND 2.2.2

10.5.3. The cases 13 ≤ k ≤ 23. Then 11 ∤ d and 13 ∤ d. There is no loss of generality in
assuming that 11|n + i11d, 13|n + i13d for some pair (i11, i13) with 0 ≤ i11 < 11, 0 ≤ i13 ≤ k−1
2 and
further i13 ≥ 2 if k = 13. We have applied Lemma 10.3.2 once in each of cases k = 7 and k = 11 but
we apply it twice for every case 13 ≤ k ≤ 23 in this section. Let P0 = ∅, p1 = 11, p2 = 13, (i1, i2) =
(i11, i13), I = [0, k) ∩ Z, P = P1 := Λ(11, 13) and ℓ ≤ ℓ1 where ℓ1 = 3 if k = 13; ℓ1 = ⌈ k
5 ⌉ + ⌈ k
17 ⌉

if k > 13. Then ℓ1 < 1
2 |I ′| since |I ′| ≥ k − ⌈ k
11 ⌉ − ⌈ k
13 ⌉. By Corollary 10.3.3, we derive that I ′ is
partitioned into M =: M1 and B =: B1 such that (M1, B1, P1, ℓ1) has P roperty H. Now we restrict
to all such pairs (i11, i13) satisfying |M1| ≤ ℓ1 and M1 is covered by P1. We check that |M1| > 2.
Therefore 5 ∤ d since M1 is covered by P1. Thus there exists i5 with 0 ≤ i5 < 5 such that 5|n + i5d.
Now we apply Lemma 10.3.2 with p1 = 5, p2 = 11 and partition B1(5, 11) into two subsets.
Let P0 = Λ(11, 13) ∪ {11, 13}, (i1, i2) = (i5, i11), I = B1, P = P2 := Λ(5, 11) ⊆ {3, 19, 23} and
ℓ ≤ ℓ2 where ℓ2 = 5, 6, 8, 11 if k = 13, 17, 19, 23, respectively. Hence B′
1 is partitioned into I1 and I2
satisfying either
 |I1| ≤ ℓ2, I1 is covered by P2, I2 = {i ∈ I ′|i(P2) is even}

or
 |I2| ≤ ℓ2, I2 is covered by P2, I1 = {i ∈ I ′|i(P2) is even}.

We compute I1, I2 and we restrict to those pairs (i11, i13) for which min(|I1|, |I2|) ≤ ℓ2 and either
I1 or I2 is covered by P2. We ﬁnd that (i11, i13) = (4, 2), (5, 3) if k = 13; (0, 0), (5, 3) if k = 17;
(0, 0), (0, 9), (7, 5), (7, 9),
(8, 6), (9, 7), (10, 8) if k = 19 and (0, 0), (0, 9), (1, 10), (2, 11), (4, 0), (5, 1), (5, 7), (6, 2), (6, 8), (7, 9), (8, 10), (9, 11)
if k = 23.
Let (i11, i13) be such a pair. We write M for the one of I1 or I2 which is covered by P2 and B
for the other. For i ∈ B′
1, we see that p ∤ ai whenever p ∈ P0 since 17|ai implies 5|ai. Therefore

i(P2) is even for i ∈ B and p ∤ ai for i ∈ B whenever p ∈ P0,(10.5.1)

since B ⊆ B′
1. Further we check that |M | > 1 if k ̸= 23 and > 3 if k = 23 implying 3 ∤ d.
By taking J = B, we get B = I 0
3 ∪ I +
3 ∪ I −
3 and B = I +
5 ∪ I −
5 . Then p ∈ {2, 7} whenever p|ai
with i ∈ I +
3 ∪ I −
3 by (10.5.1). By computing I +
3 , I −
3 , we ﬁnd that i’s have the same parity in exactly
one of I +
3 , I −
3 . Therefore we get from (10.4.1) that

(a1, a2, a3, a4) ⊆ ({1}, {7}, {14}, {2}) or ({7}, {1}, {2}, {14}) .

Let k = 13 and (i11, i13) = (4, 2). Then we have M1 = {0, 5, 10}, i5 = 0, M = {3, 9, 12} and
B = {1, 6, 7, 8, 11} since the latter set is not covered by P2 = {3}. Further i3 = 0, I 0
3 = {6},
I 1
3 = I −
3 = {8, 11}, I 2
3 = I +
3 = {1, 7}, I +
5 = {1, 6, 11}, I −
5 = {7, 8}, J1 = {11}, J2 = {8},
J3 = {1}, J4 = {7}. Therefore a11 = 1, a8 = 7, a1 = 14, a7 = 2 or a11 = 7, a8 = 1, a1 = 2, a7 = 14.
The second possibility is excluded since a11 = 7, a7 = 14 is not possible. Further from (10.5.1), we
get a6 = 1 since 2 ∤ a6 and 7 ∤ a6. Since 13|n + 2d and 7|n + d, we get ( i−2
13 ) = ( aia6
13 ) = ( ai
13 ) and
− ( i−1
7 ) = ( aia6
7 ) = ( ai
7 ). We observe that 13|n+2d, 11|n+4d, 7|n+d, 5|n, 3|n, 2|n+d, 5|ai for i ∈ M
and 3|ai for i ∈ M1. Now we see that a0 ∈ {5, 15} and a0 = 5 is excluded since ( 5
7 ) ̸= − ( −1
7 ). Thus
a0 = 15. Next a1 = 14, a2 = 13 and a3 = 3. Also a4 ∈ {1, 11} and a4 ̸= 1 since ( a4
13 ) = ( 2
13 ) = −1.
Similarly we derive that a5 = 10, a6 = 1, a7 = 2, a8 = 7, a9 = 6, a10 = 5, a11 = 1 and a12 = 3. Thus
(a0, a1, · · · , a12) = (15, 14, 13, · · · , 5, 1, 3). The other case (i11, i13) = (5, 3) is similar and we get
(a0, a1, · · · , a12) = (1, 15, 14, · · · , 5, 1).
Let k = 17 and (i11, i13) = (0, 0). Then we have M1 = {5, 10, 15} and i5 = 0. We see from the
assumption of Lemma 10.4.2 with k = 17, k′ = 13 that 4 ≤ i17 < 13. Hence, from i17 ∈ ∪
p=5,11,13{ip +

pj : 0 ≤ j < ⌈ k
p ⌉}, we get i17 ∈ {5, 10, 11}. Further M = {3, 6, 12}, B = {1, 2, 4, 7, 8, 9, 14, 16}, i3 =
0, I 0
3 = {9}, I 1
3 = {1, 4, 7, 16}, I 2
3 = {2, 8, 14}, I +
5 = {1, 4, 9, 14, 16}, I −
5 = {2, 7, 8}, J1 = {1, 4, 16},
J2 = {7}, J3 = {14} and J4 = {2, 8}. Therefore a1 = a4 = a16 = 1, a7 = 7, a14 = 14, a2 = a8 = 2.
Thus a9 = 1 by (10.5.1) and 2 ∤ a9, 7 ∤ a9. Now we see by Legendre symbol mod 17 that a1 = a4 =
a9 = a16 = 1 is not possible. The case (i11, i13) = (5, 3) is excluded similarly.

10.5. PROOF OF LEMMA 10.4.2 87

Let k = 19 and (i11, i13) = (0, 0). Then we have M1 = {5, 10, 15, 17}, i5 = 0, i17 = 0, M =
{3, 6, 12}, B = {1, 2, 4, 7, 8, 9, 14, 16, 18} and i3 = 0. We see from i19 ∈ ∪
p=3,5,11,13,17{ip + pj :

0 ≤ j < ⌈ k
p ⌉} and 2 ≤ i19 < 17 that i19 ∈ {3, 5, 6, 9, 10, 11, 12, 13, 15}. Further I 0
3 = {9, 18},
I 1
3 = {1, 4, 7, 16}, I 2
3 = {2, 8, 14}, I +
5 = {1, 4, 9, 14, 16}, I −
5 = {2, 7, 8, 18}, J1 = {1, 4, 16}, J2 = {7},
J3 = {14} and J4 = {2, 8}. Therefore a1 = a4 = a16 = 1 which is not possible by mod 19. The
case (i11, i13) = (7, 5) is excluded similarly. Let (i11, i13) = (0, 9). Then M1 = {2, 5, 7, 12, 17},
i5 = 2, i17 = 5, M = {1, 3, 10, 16}, B = {4, 6, 8, 13, 14, 15, 18}, i3 = 1 and i19 = 3. We now
consider (n + 6d)(n + 7d) · · · (n + 18d) = b′y′2. Then P (b′) ≤ 13. By the case k = 13, we get
(a6, a7, · · · , a18) = (1, 15, · · · 6, 5, 1) since 5|a7 and 3|a16. From 19|n + 3d, we get ( ai
19 ) = ( aia6
19 ) =
− ( i−3
19 ) which together with 13|n + 9d, 11|n, 7|n + d, 2|n, 5|a2, 17|a5, 3|a1 implies a0 ∈ {2, 22},
a1 ∈ {3, 21}, a2 = 5, a3 = 19, a4 = 2 and a5 = 17. Now from ( ai
17 ) = ( aia6
17 ) = ( i−5
17 ), we get
a0 = 22, a1 = 21. Thus (a0, a1, · · · , a18) = (22, 21, · · · , 6, 5, 1). The case (i11, i13) = (7, 9) is similar
and we get (a0, a1, · · · , a18) = (1, 5, 6, · · · , 21, 22). For the pair (i11, i13) = (10, 8), we get similarly
(a0, a1, · · · , a18) = (21, 5, · · · , 6, 5, 1, 3). This is excluded by considering (n + 3d)(n + 6d) · · · (n + 18d)
and k = 6. For the pairs (i11, i13) = (8, 6), (9, 7), we get i19 = 0, 1, respectively, which is not possible
since i19 ≥ 2 by the assumption of the Lemma.
Let k = 23 and (i11, i13) = (0, 0). Then M1 = {5, 10, 15, 17, 20}, i5 = 0, i17 = 0, M =
{3, 6, 12, 19, 21}, B = {1, 2, 4, 7, 8, 9, 14, 16, 18}, i3 = 0 and i19 = 0 since 23 ∤ a19. We have i23 ∈
{5, 6, 9, 10, 11, 12, 13, 15, 17, 18} since 4 ≤ i23 < 19. Here we observe that 23 ∤ a19 and 4 ≤ i23 < 19
in view of our assumption that k ∤ ai for 0 ≤ i < k − k′ and k′ ≤ i < k with k = 23, k′ = 19.
Further I 0
3 = {9, 18}, I 1
3 = {1, 4, 7, 16}, I 2
3 = {2, 8, 14}, I +
5 = {1, 4, 9, 14, 16}, I −
5 = {2, 7, 8, 18},
J1 = {1, 4, 16}, J2 = {7}, J3 = {14} and J4 = {2, 8}. Therefore a1 = a4 = a16 = 1, a7 = 7, a14 =
14, a2 = a8 = 2. This is not possible since ( a1
23 ) = ( a4
23 ) = ( a16
23 ) = ( a2
23 ) = ( a8
23 ) = 1. The cases
(i11, i13) = (0, 9), (1, 10), (2, 11), (4, 0), (7, 9), (8, 10), (9, 11) are excluded similarly. Let (i11, i13) =
(5, 1). Then M1 = {7, 10, 12, 17, 22}, i5 = 2, i17 = 10, M = {0, 3, 4, 6, 8, 15, 21}, B = {9, 11, 13, 18,
19, 20} and i3 = 0. This implies either 23|a4, 19|a8 or 23|a8, 19|a4. Further I 0
3 = {9, 18}, I 1
3 =
{11, 20}, I 2
3 = {13, 19}, I +
5 = {11, 13, 18}, I −
5 = {9, 19, 20}, J1 = {11}, J2 = {20}, J3 = {13}
and J4 = {19}. Therefore a11 = 1, a20 = 7, a13 = 14, a19 = 2. Further from (10.5.1), we get a9 ∈
{1, 2}, a18 = 1 since 7 ∤ a9a18, 2 ∤ a18. However a9 = 2 as 9 ∈ I −
5 , 18 ∈ I +
5 . Since ( a11
23 ) = ( a18
23 ) = 1,

we see that 23|a4, 19|a8. By using ( ai
p ) = ( aia11
p ) = ( (i−ip)(11−ip)
p ), we get ( ai
23 ) = − ( i−4
23 ),
( ai
11 ) = − ( i−5
11 ), ( ai
7 ) = − ( i−6
7 ) and ( ai
5 ) = ( i−2
5 ). Now from 23|a4, 19|a8, 17|a10, 13|n + d, 11|n +
5d, 7|n + 6d, 5|n + 2d, 3|n, 2|n + d, M1 is covered by {5, 17}, M is covered by {3, 19, 23}, we derive
that (a0, a1, · · · , a22) = (3, 26, · · · , 6, 5). The pairs (i11, i13) = (5, 7), (6, 2), (6, 8) are similar and we
get (a0, a1, · · · , a22) = (6, 7, · · · , 3, 7),
(7, 3, · · · , 7, 6), (5, 6, 7, · · · , 3), respectively. □

10.5.4. Introductory remarks on the cases k ≥ 29. Assume q1 ∤ d and q2 ∤ d. Then, by
taking mirror image (2.2.1) of (2.1.1), there is no loss of generality in assuming that q1|n+iq1d, q2|n+
iq2d for some pair (iq1, iq2) with 0 ≤ iq1 < q1, 0 ≤ iq2 ≤ k−1
2 and further iq2 ≥ k − k′ if q2 = k.
For k = 61, by taking (n + 8d) · · · (n + 60d) and k = 53, we may assume that max(i59, i61) ≥ 8 if
i59 ≥ 2. Let P0 = ∅, p1 = q1, p2 = q2, (i1, i2) = (iq1, iq2), I = [0, k) ∩ Z, P = P1 := Λ(q1, q2) and
ℓ ≤ ℓ1 = ∑

p∈P1 ⌈ k
p ⌉. We check that ℓ1 < 1
2 |I ′| since |I ′| ≥ k − ⌈ k
q1 ⌉ − ⌈ k
q2 ⌉. By Corollary 10.3.3, we
get M =: M1 and B =: B1 with (M1, B1, P1, ℓ1) having P roperty H. We now restrict to all such
pairs (iq1, iq2) for which |M1| ≤ ℓ1 and M1 is covered by P1. We ﬁnd that there is no such pair
(iq1, iq2) when k = 97.

88 10. PROOF OF THEOREMS 2.1.1, 2.2.1 AND 2.2.2

10.5.5. The cases 29 ≤ k ≤ 59. As stated in Lemma 10.4.2, we have q1 = 19, q2 = 29 and
P1 = Λ(19, 29) ⊆ {11, 13, 17, 43, 47, 53, 59}. Then the pairs (iq1, iq2) are given by

k = 29 : (0, 9), (1, 10), (2, 11), (3, 12), (4, 13), (15, 5), (16, 6), (17, 7), (18, 8);

k = 31 : (0, 0), (0, 9), (1, 10), (2, 11), (3, 12), (4, 13), (11, 1),

(12, 2), (13, 3), (14, 4), (15, 5), (16, 6), (17, 7), (18, 8);

k = 37 : (0, 0), (0, 9), (1, 10), (2, 11), (3, 12), (4, 13), (17, 7), (18, 8);

k = 41 : (0, 0), (2, 11), (3, 12), (4, 13);

k = 43 : (0, 0), (1, 1), (3, 12), (4, 13), (5, 14), (6, 15), (7, 16), (8, 17);

k = 47 : (0, 0), (1, 1), (7, 16), (8, 17), (9, 18), (10, 19), (11, 20),

(12, 21), (13, 22), (13, 23), (14, 23);

k = 53 : (0, 0), (1, 0), (1, 1), (13, 22), (13, 23), (14, 23), (14, 24),

(15, 24), (15, 25), (16, 25), (16, 26), (17, 26);

k = 59 : (0, 0), (0, 28), (1, 0), (1, 1), (2, 1), (3, 2), (17, 27), (18, 28).

Let k = 31 and (i19, i29) = (0, 9). We see that P1 = {11, 13, 17}, M1 = {4, 5, 12, 16,
21, 25, 27} and B1 = {1, 2, 3, 6, 7, 8, 10, 11, 13, 14, 15, 17, 18, 20, 22, 23, 24, 26, 28, 29, 30}. Since M1 is
covered by P1, we get 11 divides a5, a16, a27; 13 divides a12, a25 and 17 divides a4, a21 so that i11 =
5, i13 = 12, i17 = 4. We see that gcd(11 · 13 · 17, ai) = 1 for i ∈ B1. Now we take P0 = P1 ∪ {19, 29},
p1 = 11, p2 = 13, (i1, i2) := (i11, i13) = (5, 12), I = B1, P = P2 := Λ(11, 13) \ P0 = {5, 31}
and ℓ ≤ ℓ2 = ∑

p∈P2 ⌈ k
p ⌉ = 8. Thus |I ′| = |B1| = 21 > 2ℓ2. Then the condition of Corollary
10.3.3 are satisﬁed and we have M =: M2, B =: B2 and (M2, B2, P2, ℓ2) has P roperty H. We
get M2 = {1, 3, 7, 8, 18, 23, 28}. This is not possible since M2 is not covered by P2. Further the
following pairs (i19, i29) are excluded similarly:

k = 29 : (0, 9), (1, 10), (2, 11), (3, 12), (4, 13), (15, 5), (16, 6), (17, 7), (18, 8);

k = 31 : (1, 10), (2, 11), (3, 12), (4, 13), (18, 8).

Thus k > 29.
Let k = 59 and (i19, i29) = (0, 0). Then we see that P1 = {11, 13, 17, 43, 47, 53, 59}, M1 =
{11, 13, 17, 22, 26, 33, 34, 39, 43, 44, 47, 51, 52, 53, 55}, B1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 18,
20, 21, 23, 24, 25, 27, 28, 30, 31, 32, 35, 36, 37, 40, 41, 42, 45, 46, 48, 49, 50, 54, 56}, i11 = i13 = i17 = 0,
{43, 47, 53} is covered by {43, 47, 53, 59} =: P ′
1. Let p|ai for i ∈ B1 and p ∈ P1. Then we show that
i ∈ {4, 6, 10}. Let 59|a43. Then {47, 53} is covered by {43, 47, 53}. Let 43|a47. If 43|ai with i ∈ B1,
then i = 4 and 43 · p|a4 with p ∈ {47, 53} since i(P1) is even. This implies either 53|a53, 43 · 47|a4
or 47|a53, 43 · 53|a4. Similarly we get i ∈ {4, 6, 10} by considering all the cases 59|a43, 59|a47 and
59 ∤ a43a47a53. We observe that 59 ∤ a53 since 6 ≤ i59 < 53. Hence we conclude that p ∤ ai for
i ∈ B1 \ {4, 6, 10} and p ∈ P ′
1. Further we observe that

i59 ∈ M1 ∪ {19, 29, 38} ∪ {6, 10}.(10.5.2)

Now we take P0 = P1 ∪ {19, 29}, p1 = 11, p2 = 13, (i1, i2) := (0, 0), I = B1 \ {4, 6, 10}, P =
P2 := Λ(11, 13) \ P0 = {5, 31, 37} and ℓ ≤ ℓ2 = ∑

p∈P2 ⌈ k
p ⌉ = 16. Thus |I ′| = |B1| − 2 >
2ℓ2. Then the conditions of Corollary 10.3.3 are satisﬁed and we have M =: M2, B =: B2
with (M2, B2, P2, ℓ2) having P roperty H. We get M2 = {5, 15, 20, 30, 31, 35, 37, 40, 45}, B2 =
{1, 2, 3, 7, 8, 9, 12, 14, 16, 18, 21, 23, 24, 25, 27, 28, 32, 36, 41, 42, 46, 48, 49, 50, 54, 56}, i5 = 0, 31|a31, 37|a37
or 31|a37, 37|a31. Now we take P0 = P1 ∪ P2 ∪ {19, 29}, p1 = 5, p2 = 11, (i1, i2) := (0, 0), I = B2,
P = P3 := Λ(5, 11) \ P0 = {3, 23, 41} and ℓ ≤ ℓ3 = ∑

p∈P3 ⌈ k
p ⌉. Then by Lemma 10.3.2,
we see that M = {3, 6, 12, 21, 23, 24, 27, 41, 42, 46, 48, 54} is covered by P3 and i(P3) is even for
i ∈ B = {1, 2, 7, 8, 9, 14, 16, 18, 28, 32, 36, 49, 56}. Thus i3 = i23 = i41 = 0 and p ∈ {2, 7} whenever

10.5. PROOF OF LEMMA 10.4.2 89

p|ai with i ∈ B. Putting J = B, we have B = I 0
3 ∪ I 1
3 ∪ I 2
3 and B = I +
5 ∪ I −
5 with

I 0
3 = {9, 18, 36}, I 1
3 = {1, 7, 16, 28, 49}, I 2
3 = {2, 8, 14, 32, 56}

and
 I +
5 = {1, 9, 14, 16, 36, 49, 56}, I −
5 = {2, 7, 8, 18, 28, 32}.

so that
 J1 = {1, 16, 49}, J2 = {7, 28}, J3 = {14, 56}, J4 = {2, 8, 32}.

Hence (a1, a2, a3, a4) ⊆ ({1}, {7}, {14}, {2}) by (10.4.1). Thus a1 = a16 = a49 = 1, a7 = a28 =
7, a14 = a56 = 14, a2 = a8 = a32 = 2. Further we get a9 = a36 = 1 and a18 = 2 since 9, 36 ∈ I +
5 and
18 ∈ I −
5 . Since ( ai
59
 ) = 1 for ai ∈ {1, 7},(10.5.3)

we see that ( ai
59 ) = 1 for i ∈ {1, 7, 9, 16, 28, 36, 49} which is not possible by (10.5.2).
Let k = 41 and (i19, i29) = (2, 11). Then we see that P1 = {11, 13, 17}, M1 = {1, 6, 7, 14, 18, 23, 27,
29}, B1 = {0, 3, 4, 5, 8, 9, 10, 12, 13, 15, 16, 17, 19, 20, 22, 24, 25, 26, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39},
i11 = 7, i13 = 1, i17 = 6. Further gcd(ai, 11 · 13 · 17) = 1 for i ∈ B1. Now we take P0 = P1 ∪ {19, 29},
p1 = 11, p2 = 13, (i1, i2) := (7, 1), I = B1, P = P2 := Λ(11, 13) \ P0 = {5, 31, 37} and ℓ ≤ ℓ2 =∑

p∈P2 ⌈ k
p ⌉ = 13. Then |I ′| = |B1| > 2ℓ2. Thus the conditions of Corollary 10.3.3 are satisﬁed
and we get M =: M2 and B =: B2 such that (M2, B2, P2, ℓ2) has P roperty H. We have M2 =
{0, 3, 5, 9, 10, 20, 25, 30, 35}, B2 = {4, 8, 12, 13, 15, 16, 17, 19, 22, 24, 26, 28, 31, 32, 33, 34, 36, 37, 38, 39},
i5 = 0. Further 31 · 37|a3a9, 31 ∤ a34. We take P0 = P1 ∪ P2 ∪ {19, 29}, p1 = 5, p2 = 11,
(i1, i2) := (0, 7), I = B2, P = P3 := Λ(5, 11) \ P0 = {3, 23, 41}, ℓ ≤ ∑

p∈P3 ⌈ k
p ⌉ and apply
Lemma 10.3.2 to see that M = {13, 16, 17, 19, 28, 34, 37} is covered by P3, i3 = 1, i(P3) is even
for i ∈ B = {4, 8, 12, 22, 24, 26, 31, 32, 33, 36, 38, 39}. Further i23 = 17, i41 ∈ {2, 11, 21} ∪ M1 ∪ M2 ∪
M ∪ {4, 22, 31} or vice-versa. Here we observe that i41 exists since 41 ∤ d. Thus 23 · 41| ∏ ai where i
runs through the set {2, 11, 21} ∪ M1 ∪ M2 ∪ {4, 22, 31}. Therefore ai ∈ {1, 2, 7, 14} for i ∈ I 1
3 ∪ I 2
3
where B = I 0
3 ∪ I 1
3 ∪ I 2
3 , B = I +
5 ∪ I −
5 with

I 0
3 = {4, 22, 31)}, I 1
3 = {12, 24, 33, 36, 39}, I 2
3 = {8, 26, 32, 38}

and
 I +
5 = {4, 24, 26, 31, 36, 39}, I −
5 = {8, 12, 22, 32, 33, 38}

by taking J = B. We get

J1 = {24, 36, 39}, J2 = {12, 33}, J3 = {26}, J4 = {8, 32, 38},

and a24 = a36 = a39 = 1, a12 = a33 = 7, a26 = 14, a8 = a32 = a38 = 2 by (10.4.1). Since
( ai
41
 ) = 1 for ai ∈ {1, 2},(10.5.4)

we see that ( ai
41 ) = 1 for i ∈ {8, 24, 32, 36, 38, 39} which is not valid by the possibilities of i41.
All other cases are excluded similarly. Analogous to (10.5.3) and (10.5.4), we use ( ai
k ) = 1 for

ai ∈ {1, 7} if k = 37, 53, 59; ai ∈ {1, 2} if k = 31, 41, 47; ai ∈ {1, 14} if k = 43

to exclude the remaining possibilities. □

10.5.6. The case k = 61. We have q1 = 59, q2 = 61 and P1 = {7, 13, 17, 29, 47, 53}. Then the
pairs (iq1, iq2) are given by (8, 6), (9, 7), (10, 8), (11, 9), i.e. (i + 2, i) with 6 ≤ i ≤ 9.
Let (i59, i61) = (8, 6). Then P1 = {7, 13, 17, 29, 47, 53}, M1 = {2, 4, 9, 11, 14, 15, 16, 20, 25, 28, 32,
33, 38, 39, 41, 46, 50, 53, 54, 60}, B1 = {0, 1, 3, 5, 7, 10, 12, 13, 17, 18, 19, 21, 22, 23, 24, 26, 27, 29, 30, 31,
34, 35, 36, 37, 40, 42, 43, 44, 45, 47, 48, 49, 51, 52, 55, 56, 57, 58, 59}, i7 = 4, i13 = 2, i17 = 16, i29 = 9
and a14, a20 are divisible by 47, 53. Further gcd(p, ai) = 1 for i ∈ B1 and p ∈ P1. Let P0 = P1 ∪
{59, 61}, p1 = 7, p2 = 17, (i1, i2) := (4, 16), I = B1, P = P2 := Λ(7, 17)\P0 = {11, 19, 23, 37} and ℓ ≤
ℓ2 = ∑

p∈P2 ⌈ k
p ⌉ = 15. Then 2ℓ2 < |I ′| = |B1| − 1. By Corollary 10.3.3, we get M =: M2, B =: B2

90 10. PROOF OF THEOREMS 2.1.1, 2.2.1 AND 2.2.2

and (M2, B2, P2, ℓ2) has P roperty H. We ﬁnd that M2 = {1, 10, 12, 21, 23, 29, 30, 34, 44, 45, 48, 56},
B2 = {0, 3, 5, 7, 13, 17, 19, 22, 24, 26, 27, 31, 35, 36, 37, 40, 42,
43, 47, 49, 51, 52, 55, 57, 58, 59}, i11 = 1, i19 = 10, i23 = 21, i37 = 30. Now we take P0 = P1 ∪ P2 ∪
{59, 61}, p1 = 11, p2 = 59, (i1, i2) := (1, 8), I = B2, P = P3 := Λ(11, 59) \ P0 = {31, 41} and
ℓ ≤ ℓ3 = ∑

p∈P3 ⌈ k
p ⌉ = 4. Then 2ℓ3 < |I ′| = |B2|. By Corollary 10.3.3, we get M =: M3 and
B =: B3 such that (M3, B3, P3, ℓ3) has P roperty H. We get M3 = {0, 5, 26, 36} which cannot be
covered by P3. This is a contradiction. The remaining cases are excluded similarly. □

10.5.7. The cases k = 67, 71. We have q1 = 43, q2 = 67 and P1 ⊆ {11, 13, 19, 29, 31, 37, 41,
53, 71}. Then the pairs (iq1, iq2) are given by

k = 67 : (i, i), 6 ≤ i ≤ 33;

k = 71 : (i, i), 0 ≤ i ≤ 35, i ̸= 24, 25 and (24, 0), (25, 1), (26, 2), (27, 3).

Let k = 71 and (i43, i67) = (27, 3). We see that P1 = {11, 13, 19, 29, 31, 37, 41, 53, 71}, M1 =
{4, 5, 8, 12, 13, 15, 17, 18, 26, 29, 31, 32, 33, 37, 39, 41, 44, 48, 51, 57, 59}, B1 = {0, 1, 2, 6, 7, 9, 10, 11, 14,
16, 19, 20, 21, 22, 23, 24, 25, 28, 30, 34, 35, 36, 38, 40, 42, 43, 45, 46, 47, 49, 50, 52, 53, 54, 55, 56, 58, 60, 61,
62, 63, 64, 65, 66, 67, 68, 69}, i11 = 4, i13 = 5, i19 = 13. Therefore {8, 12, 17, 29, 33, 39, 41} is covered
by 29, 31, 37, 41, 53, 71 implying either i29 = 12 or i29 ∈ {17, 29, 33}, i31 = 8. Let i ∈ B1 and p|ai
with p ∈ P1. Then there is a q ∈ P1 such that pq|ai since i(P1) is even. Next we consider the case
i31 = 8. Then {12, 17, 29, 33, 41} =: M
′
1 is covered by 29, 37, 41, 53, 71 and i29 ̸= 12. For 29 ∈ M′
1,
we may suppose that either 29|a29, 41|a17, 29 · 41|a58 or 29|a29, 41|a41, 29 · 41|a0. Thus 0 or 58 in B1
correspond to 29. We argue as above that for any other element of M
′
1, there is no corresponding
element in B1. For the ﬁrst case, we derive similarly that 31|a33, 37|a39, 31 · 37|a2 or 37|a17, 37 · 71|a54
or 37|a29, 37 · 71|a63 or 41|a17, 37 · 71|a58. Therefore

29 · 31 · 37 · 41 · 53 · 71 | ∏
(n + id) for i ∈ M1 ∪ {3, 27, 70} ∪ B′
1

where B′
1 = {2, 54, 58, 63} if i29 = 12 and {0, 58} otherwise. Further

i71 ∈ M1 ∪ {27} ∪ B′
1 and i71 ̸= 32.(10.5.5)

For each possibility i29 ∈ {0, 4, 12, 17}, we now take P0 = P1 ∪ {43, 67}, p1 = 19, p2 = 29,
(i1, i2) := (13, i29), I = B1 \ B′
1, P = P2 := Λ(19, 29) \ P0 = {17, 47, 59, 61} and ℓ = ℓ2 =∑

p∈P2 ⌈ k
p ⌉ = 11. Then |I ′| = |B1| − 4 > 2ℓ2. Thus the conditions of Corollary 10.3.3 are
satisﬁed and we get M =: M2 and B =: B2 with (M2, B2, P2, ℓ2) having P roperty H. We
check that |M2| ≤ ℓ2 only at i29 = 12 in which case we get M2 = {9, 11, 19, 23, 36, 53}, B2 =
{0, 1, 6, 7, 10, 14, 6, 20, 21, 22, 24, 25, 28, 30, 34, 35, 38, 40, 42, 43, 45, 46, 47, 49, 50, 52, 55, 56, 60, 61, 62,
63, 64, 65, 67, 68, 69}, i17 = 2, {9, 11, 23} is covered by 47, 59, 61. Thus 47 · 59 · 61 | a9a11a23. Further
p ∤ ai for i ∈ B2 and p ∈ P2. We now take P0 = P1 ∪ P2 ∪ {43, 67}, p1 = 11, p2 = 13, (i1, i2) :=
(4, 5), I = B2, P = P3 := Λ(11, 13) \ P0 = {5} and ℓ = ℓ3 = ⌈ k
5 ⌉ = 15. Then |I ′| = |B2| > 2ℓ3. By
Corollary 10.3.3, we get M =: M3 and B =: B3 such that (M3, B3, P3, ℓ3) has P roperty H. We calcu-
late M3 = {0, 10, 25, 30, 35, 40, 50, 55, 60, 65}, B3 = {1, 6, 7, 14, 16, 20, 21, 22, 24, 28, 34, 38, 42, 43, 45,
46, 47, 49, 52, 54, 56, 58, 61, 62, 63, 64, 66, 67, 68, 69}, i5 = 0 and further 5 ∤ a20a45. Lastly we take
P0 = P1 ∪ P2 ∪ P3 ∪ {43, 67}, p1 = 5, p2 = 11, (i1, i2) := (0, 4), I = B3, P = P4 := Λ(5, 11) \ P0 =
{3, 23} and ℓ = ℓ4 = ∑

p∈P4 ⌈ k
p ⌉. By Lemma 10.3.2, we see that M = {16, 22, 24, 28, 43, 46, 47, 49, 64, 67}
is covered by P4, i3 = i23 = 1, B = {1, 6, 7, 14, 21, 34, 38, 42, 52, 56, 61, 62, 63, 68, 69} and hence
3 ∤ a7a34a52a61 and possibly 3 · 23|a1. Therefore ai ∈ {1, 2, 7, 14} for i ∈ B \ {1}. By taking
J = B \ {1}, we have B \ {1} = I 0
3 ∪ I 1
3 ∪ I −
3 = I +
5 ∪ I −
5 with

I 0
3 = {7, 34, 52, 61}, I 1
3 = {6, 21, 42, 63, 69}, I −
3 = {14, 38, 56, 62, 68}

and
 I +
5 = {6, 14, 21, 34, 56, 61, 69}, I −
5 = {7, 38, 42, 52, 62, 63, 68}.

Therefore
 J1 = {6, 21, 69}, J2 = {42, 63}, J3 = {14, 56}, J4 = {38, 62, 68}.

10.5. PROOF OF LEMMA 10.4.2 91

and hence a6 = a21 = a69 = 1, a42 = a63 = 7, a14 = a56 = 14, a38 = a62 = a68 = 2 by (10.4.1).
Further we get a34 = a61 = 1 and a52 = 2 by taking residue classes modulo 5. Since ( 1
71 ) = ( 2
71 ) = 1,
we see that ( ai
71 ) = 1 for i ∈ {6, 21, 34, 38, 52, 61, 62, 68, 69} which is not valid by the possibilities of
i71 given by (10.5.5).
Let k = 67 and (i43, i67) = (9, 9). We see that P1 = {11, 13, 19, 29, 31, 37, 41, 53}, M1 =
{20, 22, 28, 31, 35, 38, 40, 42, 46, 47, 48, 50, 53, 61, 62, 64, 66}, B1 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14,
15, 16, 17, 18, 19, 21, 23, 24, 25, 26, 27, 29, 30, 32, 33, 34, 36, 37, 39, 41, 43, 44, 45, 49, 51, 54, 55, 56, 57, 58,
59, 60, 63, 65}, i11 = i13 = i19 = 9 and {38, 40, 46, 50, 62} is covered by 29, 31, 37, 41, 53. Fur-
ther p ∤ ai for i ∈ B1 and p ∈ P1 except possibly when 29|a50, 41|a62, 29 · 41|a21. Now we
take P0 = P1 ∪ {43, 67}, p1 = 11, p2 = 13, (i1, i2) := (9, 9), I = B1 \ {21} and P = P2 :=
Λ(11, 13) \ P0 = {5, 17, 47, 59, 61}. If 5 ∤ d, we observe that there is at least 1 multiple of
5 among n + (i11 + 11i)d, 0 ≤ i ≤ 5 and ℓ ≤ ∑

p∈P2 ⌈ k
p ⌉ − 1 = 23. Thus we always have
ℓ ≤ 23 = ℓ2. Then |I ′| = |B1| − 1 > 2ℓ2 since |B1| = 48. Thus the conditions of Corol-
lary 10.3.3 are satisﬁed and we get M =: M2, B =: B2 and (M2, B2, P2, ℓ2) has P roperty H.
We have M2 = {0, 1, 2, 3, 5, 6, 7, 8, 14, 19, 24, 26, 29, 39, 43, 44, 49, 54, 56, 60} which cannot be cov-
ered by P2. This is a contradiction. The cases k = 67, (i43, i67) = (i, i) with 9 ≤ i ≤ 28 and
k = 71, (i43, i67) = (i, i) with 13 ≤ i ≤ 28, i ̸= 24, 25 are excluded similarly as in this paragraph.
The remaining cases are excluded similarly as k = 71, (i43, i67) = (27, 3) given in the preceding
paragraph. □

10.5.8. The cases k = 73, 79. We have q1 = 23, q2 = 73 and P1 ⊆ {13, 19, 29, 31, 37, 47,
59, 61, 67, 79}. Then the pairs (iq1, iq2) are given by

k = 73 : (6, 2), (7, 3), (8, 4), (9, 5);

k = 79 : (0, 0), (1, 1), (2, 2), (7, 3), (8, 4), (9, 5), (10, 6), (11, 7), (12, 8),

(13, 9), (14, 10), (15, 11), (16, 12), (17, 13), (18, 14), (19, 15).

These pairs are of the form (i + 4, i) except for (0, 0), (1, 1), (2, 2) in the case k = 79.
Let k = 79 and (i23, i73) = (8, 4). We see that P1 = {13, 19, 29, 31, 37, 47, 59, 61, 67, 79}, M1 =
{1, 3, 10, 12, 15, 16, 18, 19, 20, 25, 30, 38, 39, 40, 46, 48, 51, 58, 64, 78}, B1 = {0, 2, 5, 6, 7, 9, 11, 13, 14, 17,
21, 22, 23, 24, 26, 27, 28, 29, 32, 33, 34, 35, 36, 37, 41, 42, 43, 44, 45, 47, 49, 50, 52, 53, 55, 56, 57, 59, 60, 61,
62, 63, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76}, i13 = 12, i19 = 1 and {3, 10, 15, 16, 18, 19, 30, 40, 46, 48,
78} is covered by 29, 31, 37, 47, 59, 61, 67, 79. Thus

29 · 31 · 37 · 47 · 59 · 61 · 67 · 79 | ∏
(n + id) for i ∈ {3, 10, 15, 16, 18, 19, 30, 40, 46, 48, 78}.

Further we have
 i79 ∈ {10, 15, 16, 18, 19, 30, 40, 46, 48}(10.5.6)

and either i29 = 19 or i29 ∈ {1, 10, 16, 18}, i31 = 15, i37 = 3, i59 = 19. Also for p ∈ P1, we have
p ∤ ai for i ∈ B1 since i(P1) is even for i ∈ B1. For each possibility i29 ∈ {1, 10, 16, 18, 19}, we now
take P0 = P1 ∪ {23, 73}, p1 = 19, p2 = 29, (i1, i2) := (1, i29), I = B1, P = P2 := Λ(19, 29) \ P0 =
{11, 17, 43, 53, 71} and ℓ = ℓ2 = ∑

p∈P2 ⌈ k
p ⌉ = 19. Then |I ′| ≥ |B1| − 2 > 2ℓ2. Thus the conditions of
Corollary 10.3.3 are satisﬁed and we have M =: M2, B =: B2 and (M2, B2, P2, ℓ2) has P roperty H
implying i29 = 19 in which case we get M2 = {0, 6, 9, 11, 22, 24, 26, 33, 34, 43, 44, 55, 60, 66}, B2 =
{2, 5, 7, 13, 14, 17, 21, 23, 27, 28, 29, 32, 35, 36, 37, 41, 42, 45, 47, 49, 50, 52, 53, 56, 57, 59, 61, 62, 63, 65, 67,
68, 69, 70, 71, 72, 73, 74, 75, 76}, i11 = 0, i17 = 9, {6, 24, 34} is covered by 43, 53, 71. Thus 43 · 53 · 71 |
a6a24a34. Further p ∤ ai for i ∈ B2 and p ∈ P2. We now take P0 = P1 ∪ P2 ∪ {23, 73},
p1 = 11, p2 = 13, (i1, i2) := (0, 12), I = B2, P = P3 := Λ(11, 13) \ P0 = {5} and ℓ = ℓ3 =⌈ k
5 ⌉ = 16. Then |I ′| = |B2| > 2ℓ3. By Corollary 10.3.3, we get M =: M3 and B =: B3 with
(M3, B3, P3, ℓ3) having P roperty H. We calculate M3 = {7, 17, 32, 37, 42, 47, 57, 62, 67, 72}, B3 =
{2, 5, 13, 14, 21, 23, 27, 28, 29, 35, 36, 41, 45, 49, 50, 52, 53, 56, 59, 61, 63, 65, 68, 69, 70, 71, 73, 74, 75, 76},
i5 = 2 and 5 ∤ ai for i ∈ B3. Lastly we take P0 = P1 ∪ P2 ∪ P3 ∪ {23, 73}, p1 = 5, p2 = 11,
(i1, i2) := (2, 0), I = B3, P = P4 := Λ(5, 11) \ P0 = {3, 41} and ℓ = ℓ4 = ∑

p∈P4 ⌈ k
p ⌉. By Lemma
10.3.2, we see that M = {23, 29, 35, 36, 50, 53, 56, 65, 71, 74} is covered by P4, i3 = 2, i41 = 36,

92 10. PROOF OF THEOREMS 2.1.1, 2.2.1 AND 2.2.2

B = {5, 13, 14, 21, 28, 41, 45, 49, 59, 61, 63,
68, 69, 70, 73, 75, 76} and hence ai ∈ {1, 2, 7, 14} for i ∈ B. By taking J = B, we have B =
I 0
3 ∪ I 1
3 ∪ I −
3 = I +
5 ∪ I −
5 with

I 0
3 = {5, 14, 41, 59, 68}, I 1
3 = {13, 28, 49, 61, 70, 76}, I −
3 = {21, 45, 63, 69, 75}

and
 I +
5 = {13, 21, 28, 41, 61, 63, 68, 73, 76}, I −
5 = {5, 14, 45, 49, 59, 69, 70, 75}.

Thus
 J1 = {13, 28, 61, 76}, J2 = {49, 70}, J3 = {21, 63}, J4 = {45, 69, 75}.

and hence a13 = a28 = a61 = a76 = 1, a49 = a70 = 7, a21 = a63 = 14, a45 = a69 = a75 = 2 by (10.4.1).
Further we get a41 = a68 = 1 and a5 = a59 = 2 by residue modulo 5. Since ( 1
79 ) = ( 2
79 ) = 1, we see
that ( ai
71 ) = 1 for i ∈ {5, 13, 28, 41, 45, 59, 61, 68, 69, 75, 76} which is not valid by the possibilities of
i79 given by (10.5.6). The other cases are excluded similarly. □

10.5.9. The case k = 83. We have q1 = 37, q2 = 83 and P1 = {17, 23, 29, 31, 47, 53, 59, 61, 67, 71,
73}. Then the pairs (iq1, iq2) are given by

(13, 4), (14, 5), (15, 6), (16, 7), (17, 8), (18, 9), (19, 10),

(20, 11), (21, 12), (22, 13), (23, 14), (24, 15), (25, 16), (26, 17).

These pairs are of the form (i + 9, i) with 4 ≤ i ≤ 17.
Let (i37, i83) = (13, 4). We see that P1 = {17, 23, 29, 31, 47, 53, 59, 61, 67, 71, 73}, M1 = {0, 2, 14,
16, 18, 19, 20, 25, 26, 28, 29, 34, 36, 40, 41, 53, 56, 58, 64, 70}, B1 = {1, 3, 5, 6, 7, 8, 9, 10, 11, 12, 15, 17, 21,
22, 23, 24, 27, 30, 31, 32, 33, 35, 37, 38, 39, 42, 43, 44, 45, 46, 47, 48, 49, 51, 52, 54, 55, 57, 59, 60, 61, 62, 63,
65, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82}, i17 = 2, i23 = 18, i29 = 0, i31 = 25 and
{14, 16, 20, 26, 28, 34, 40} is covered by 47, 53, 59, 61, 67, 71, 73. Further p ∤ ai for i ∈ B1 and p ∈ P1.
For each possibility i73 ∈ {14, 16, 20, 26, 28, 34, 40}, we take P0 = P1 ∪ {37, 83}, p1 = 23, p2 = 73,
(i1, i2) := (18, i73), I = B1, P = P2 := Λ(23, 73) \ P0 = {13, 19, 79} and ℓ = ℓ2 = ∑

p∈P2 ⌈ k
p ⌉ = 14.
Then |I ′| = |B1| > 2ℓ2. Thus the conditions of Corollary 10.3.3 are satisﬁed and we get M =: M2,
B =: B2 and (M2, B2, P2, ℓ2) has P roperty H which is possible only if i73 = 14. Then M2 =
{8, 9, 11, 22, 30, 35, 48, 49, 61, 68, 74}. Therefore i13 = 9, i19 = 11 and i79 = 8. This is not possible by
applying the case k = 73 to (n + 9d) · · · (n + 81d). Similarly for (i37, i83) = (14, 5), we get i73 = 15,
i79 = 9 and this is excluded by applying the case k = 73 to (n + 10d) · · · (n + 82d). For all the
remaining cases, we continue similarly to ﬁnd that M2 is not covered by P2 for possible choices of
i73 and hence they are excluded. □

10.5.10. The case k = 89. We have q1 = 79, q2 = 89 and P1 = {13, 17, 19, 23, 31, 47, 53, 71, 83}.
Then the pairs (iq1, iq2) are given by (16, 6), (17, 7), (18, 8), (19, 9), (20, 10), (21, 11). These pairs are
of the form (i + 10, i) with 6 ≤ i ≤ 11.
Let (i79, i89) = (16, 6). We see that P1 = {13, 17, 19, 23, 31, 47, 53, 71, 83}, M1 = {0, 1, 2, 3, 4, 10,
12, 17, 19, 24, 26, 27, 30, 33, 38, 42, 43, 44, 48, 49, 56, 57, 61, 64, 69, 72, 76, 78, 82}, B1 = {5, 7, 8, 9, 11, 13,
14, 15, 18, 20, 21, 22, 23, 25, 28, 29, 31, 32, 34, 35, 36, 37, 39, 40, 41, 45, 46, 47, 50, 51, 52, 53, 54, 55, 58, 59,
60, 62, 63, 65, 66, 67, 68, 70, 71, 73, 74, 75, 77, 79, 80, 81, 83, 84, 85, 86, 87, 88}, i13 = 4, i17 = 10, i19 =
0, i23 = 3, i31 = 2, i47 = 1 and {12, 24, 42} is covered by 53, 71, 83. Further p ∤ ai for i ∈
B1 and p ∈ P1. Now we take P0 = P1 ∪ {79, 89}, p1 = 31, p2 = 89, (i1, i2) := (2, 6), I =
B1 and P = P2 := Λ(31, 89) \ P0 = {7, 11, 41, 59, 73}. If 7 ∤ d, we observe that there is at
least 1 multiple of 7 among n + (i13 + 13i)d, 0 ≤ i ≤ 6 and ℓ ≤ ℓ2 = ∑

p∈P2 ⌈ k
p ⌉ − 1 =
28. Thus in all cases, we have ℓ ≤ ℓ2 and |I ′| = |B1| > 2ℓ2. Therefore the conditions of
Corollary 10.3.3 are satisﬁed and we get M =: M2 and B =: B2 with (M2, B2, P2, ℓ2) having
P roperty H. We ﬁnd M2 = {7, 11, 13, 22, 25, 29, 32, 36, 39, 40, 51, 53, 54, 60, 62, 67, 73, 74, 81, 84, 88},
B2 = {5, 8, 9, 14, 15, 18, 20, 21, 23, 28, 31, 34, 35, 37, 41, 45, 46, 47, 50, 52, 55, 58, 59, 63, 65, 66, 68, 70, 71,
75, 77, 79, 80, 83, 85, 86, 87}, i7 = 4, i11 = 7, i41 = 13 and {22, 36} is covered by 59, 73. Further for
p ∈ P2, p ∤ ai for i ∈ B2 \ {18}. We take P0 = P1 ∪ P2 ∪ {79, 89}, p1 = 41, p2 = 79, (i1, i2) := (13, 16),

10.6. PROOF OF LEMMA 10.4.3 93

I = B2 \ {18}, P = P3 := Λ(41, 79) \ P0 = {37, 43, 61, 67} and ℓ = ℓ3 = ∑

p∈P3 ⌈ k
p ⌉ = 10. Then
|I ′| = |I| = |B2| − 1 > 2ℓ3. Thus the conditions of Corollary 10.3.3 are satisﬁed and we have
M =: M3, B =: B3 and (M3, B3, P3, ℓ3) has P roperty H. We get M3 = {9, 21, 28, 34, 52, 58}, B3 =
{5, 8, 14, 15, 20, 23, 31, 35, 37, 41, 45, 46, 47, 50, 55, 59, 63, 65, 66, 68, 70, 71, 75, 77, 79, 80, 83, 85, 86, 87},
i37 = 21, i43 = 9 and {28, 34} is covered by 61, 67. Therefore p ∈ {2, 3, 5, 29} whenever p|ai for i ∈ B3.
Now we take P0 = P1 ∪ P2 ∪ P3 ∪ {79, 89}, p1 = 7, p2 = 17, (i1, i2) := (4, 10), I = B3, P = P4 :=
Λ(7, 17) \ P0 = {29} and ℓ = ℓ4 = ⌈ k
29 ⌉ = 4. Then |I ′| = |B3| − 1 since 46 ∈ B3 and |B3| − 1 > 2ℓ3.
By Corollary 10.3.3, we get M =: M4 and B =: B4 with (M4, B4, P4, ℓ4) having P roperty H. We ﬁnd
M4 = {8, 37, 66}, B4 = {5, 14, 15, 20, 23, 31, 35, 41, 45, 47, 50, 55, 59, 63, 65, 68, 70, 71, 75, 77, 79, 80, 83,
85, 86, 87}, i29 = 8 and P (ai) ≤ 5 for i ∈ B4. Now we get a contradiction by taking k = 6 and
(n + 47d)(n + 55d)(n + 63d)(n + 71d)(n + 79d)(n + 87d) = b′y′2. Similarly the pair (i79, i89) = (17, 7)
is excluded by applying k = 6 to (n + 48d)(n + 56d)(n + 64d)(n + 72d)(n + 80d)(n + 88d). For all
the remaining cases, we continue similarly to ﬁnd that M3 is not covered by P3 and hence they are
excluded. □

10.6. Proof of Lemma 10.4.3

Assume that Q1 ∤ d and Q2 ∤ d. Then, by taking mirror image (2.2.1) of (2.1.1), there is no loss
of generality in assuming that 0 ≤ iQ1 < Q1, 0 ≤ iQ2 ≤ min(Q2 − 1, k−1
2 ). Further iQ2 ≥ k − k′

if Q2 = k. Let P0 = {Q0}, p1 = Q1, p2 = Q2, (i1, i2) := (iQ1, iQ2), I = [0, k) ∩ Z and P = P1 :=
Λ(Q1, Q2) \ P0. Then |I ′| ≥ k − ⌈ k
Q1 ⌉ − ⌈ k
Q2 ⌉ and ℓ ≤ ℓ1 where ℓ1 = ∑

p∈P1 ⌈ k
p ⌉. In fact we can take
ℓ1 = ∑

p∈P1 ⌈ k
p ⌉ − 1 if (k, Q0) = (79, 23) or (k, Q0) = (59, 29) with i7 ≤ 2 by considering multiples
of 13, 11 or 19, 7, 11, respectively.
Let (k, Q0) ̸= (79, 73). Then ℓ1 < 1
2 |I ′|. We observe that i(P0) = 0 for i ∈ I ′ since Q0|d and by
Corollary 10.3.3, we get M =: M1, B =: B1 and (M1, B1, P1, ℓ1) has P roperty H. We now restrict
to all such pairs (iQ1, iQ2) with |M1| ≤ ℓ1 and M1 is covered by P1. These pairs are given by
k Q0 (Q1, Q2) (iQ1, iQ2) k Q0 (Q1, Q2) (iQ1, iQ2)
29 19 (7, 17) (0, 0), (0, 11) 59 29 (7, 17) (1, 1), (1, 6)
37 19 or 29 (7, 17) (0, 0), (1, 2) 71 43 (53, 67) (0, 0)
47 29 (7, 17) (0, 0), (4, 12) 89 79 (23, 73) (0, 0), (19, 15)
Let (k, Q0) = (79, 73) and (Q1, Q2) = (53, 67). We apply Lemma 10.3.2 to derive that either
|I1| ≤ ℓ1, I1 is covered by P1, i(P1) is even for i ∈ I2 or |I2| ≤ ℓ1, I2 is covered by P1, i(P1) is even
for i ∈ I1. We compute I1, I2 and we ﬁnd that both I1 and I2 are not covered by P1 for each pair
(i53, i67) with 0 ≤ i53 < 53, 0 ≤ i67 ≤ k−1
2 .
Let (k, Q0) = (37, 29), (Q1, Q2) = (7, 17) and (i7, i17) = (1, 2). Then P1 = {11, 13, 19, 23, 37}.
We ﬁnd that M1 = {3, 7, 10, 13, 14, 17, 23, 25}, B1 = {0, 4, 5, 6, 9, 11, 12, 16, 18, 20, 21, 24, 26, 27, 28, 30,
31, 32, 33, 34, 35}, i11 = 3, i13 = 10 and {7, 13, 17} is covered by 19, 23, 37. Further p ∤ ai for
p ∈ P1, i ∈ B1. Now we take P0 = P1 ∪ {7, 17, 29}, p1 = 11, p2 = 13, (i1, i2) := (3, 10),
I = B1, P = P2 := Λ(11, 13) \ P0 = {5, 31} and ℓ = ℓ2 = ∑

p∈P2 ⌈ k
p ⌉ = 10. Thus |I ′| =
|I| = |B1| = 21 > 2ℓ2. Then the conditions of Corollary 10.3.3 are satisﬁed and we have M =:
M2, B =: B2 and (M2, B2, P2, ℓ2) has P roperty H. We get M2 = {5, 6, 16, 21, 26, 31}, B2 =
{0, 4, 9, 11, 12, 18, 20, 24, 27, 28, 30, 32, 33, 34, 35}, i5 = 1, 31|a5 and 5 ∤ a11. Also P (ai) ≤ 3 for
i ∈ B2 and P (a31) = 5. Thus P (a30a31 · · · a35) ≤ 5 and this is excluded by the case k = 6. The
other cases for k = 29, 37, 47 are excluded similarly. Each possibility is excluded by the case k = 6
after showing P (a1a2 · · · a6) ≤ 5 when (k, Q0) ∈ {(29, 19), (37, 19), (37, 29), (47, 29)}, (i7, i17) =
(0, 0); P (a22a23 · · · a27) ≤ 5 when (k, Q0) = (29, 19), (i7, i17) = (0, 11); P (a30a31 · · · a35) ≤ 5 when
(k, Q0) = (37, 19), (i7, i17) = (1, 2) and P (a40a41 · · · a45) ≤ 5 when (k, Q0) = (47, 29), (i7, i17) =
(4, 12).
Let (k, Q0) = (59, 29), (Q1, Q2) = (7, 17) and (i7, i17) = (1, 1). Then P1 = {11, 13, 19, 23, 37, 47, 59}.
We ﬁnd that M1 = {0, 12, 14, 20, 23, 24, 27, 30, 34, 38, 39, 40, 45, 47, 48, 53, 56, 58}, B1 = {2, 3, 4, 5, 6, 7, 9,
10, 11, 13, 16, 17, 19, 21, 25, 26, 28, 31, 32, 33, 37, 41, 42, 44, 46, 49, 51, 54, 55}, i11 = i13 = i19 = i23 = 1,
{30, 38, 48} is covered by 37, 47, 59. Further p ∤ ai for p ∈ P1, i ∈ B1. Now we take P0 = P1 ∪
{7, 17, 29}, p1 = 11, p2 = 13, (i1, i2) := (1, 1), I = B1, P = P2 := Λ(11, 13) \ P0 = {5, 31, 43} and ℓ =

94 10. PROOF OF THEOREMS 2.1.1, 2.2.1 AND 2.2.2

ℓ2 = ∑

p∈P2 ⌈ k
p ⌉. By Lemma 10.3.2, we get M = {6, 11, 16, 21, 31, 32, 41, 44, 46}, i5 = 1, 31·43|a32a44
and i(P2) is even for i ∈ B = {2, 3, 4, 5, 7, 9, 10, 13, 17, 19, 25, 26, 28, 33, 37, 42, 49, 51, 54, 55}. Further
for p ∈ P2, p ∤ ai for i ∈ B. Finally we apply Lemma 10.3.2 with P0 = P1 ∪ P2 ∪ {7, 17, 29},
p1 = 5, p2 = 11, (i1, i2) := (1, 1), I = B and P = P3 := Λ(5, 11) \ P0 = {3, 41, 53}. We get
M1 = {4, 7, 13, 25, 28, 42, 49, 54, 55} which is covered by P3, i3 = 1, {42, 54} is covered by {41, 53}
and i(P3) is even for i ∈ B1 = {2, 3, 5, 9, 10, 17, 19, 33, 37}. Hence P (ai) ≤ 2 for i ∈ B1. Since( ai
29 ) = ( n
29 ) and ( 2
29 ) ̸= 1, we see that ai = 1 for i ∈ B1. By taking J = B1, we derive that either
I +
5 = ∅ or I −
5 = ∅ which is a contradiction. The other case (i7, i17) = (1, 6) is excluded similarly.
Let (k, Q0) = (71, 43), (Q1, Q2) = (53, 67), (i53, i67) = (0, 0). Then P1 = {7, 11, 13, 19, 23, 71}.
We get M1 = {7, 11, 13, 14, 19, 21, 22, 23, 26, 28, 33, 35, 38, 39, 42, 43, 44, 46, 52, 55, 56, 57, 63, 65, 66, 69,
70}, B1 = {1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 17, 18, 20, 24, 25, 27, 29, 30, 31, 32, 34, 36, 37, 40, 41, 45, 47,
48, 49, 50, 51, 54, 58, 59, 60, 61, 62, 64, 68}, i7 = i11 = i13 = i19 = i23 = 0, i71 = 43. Further, for p ∈
P1, p ∤ ai for i ∈ B1. Now we take P0 = P1 ∪ {43, 53, 67}, p1 = 11, p2 = 13, (i1, i2) := (0, 0), I = B1,
P = P2 := Λ(11, 13) \ P0 = {5, 17, 29, 31, 37, 47, 59, 61} and ℓ = ℓ2 = ∑

p∈P2 ⌈ k
p ⌉. By Lemma 10.3.2,
we see that M = {5, 10, 15, 17, 20, 29, 30, 31, 34, 37, 40, 45, 47, 51, 58, 59, 60, 61, 62, 68} is covered by
P2, i(P2) is even for i ∈ B = {1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 25, 27, 32, 36, 41, 48, 49, 50, 54, 64}. We
get i5 = i17 = i29 = i31 = 0, and {37, 47, 59, 61} is covered by 37, 47, 59, 61. Thus 37 · 47 · 59 ·
61|a37a47a59a61. Further p ∤ ai for i ∈ B and p ∈ P2. We take P0 = P1 ∪ P2 ∪ {43, 53, 67},
p1 = 5, p2 = 11, (i1, i2) := (0, 0), I = B2, P = P3 := Λ(5, 11)\P0 = {3, 41} and ℓ = ℓ3 = ∑

p∈P3 ⌈ k
p ⌉.
By Lemma 10.3.2, we see that M1 = {3, 6, 12, 24, 27, 41, 48, 54} is covered by P3, i(P3) is even for
i ∈ B1 = {1, 2, 4, 8, 9, 16, 18, 32, 36, 49, 64}. Thus i3 = 0 implying i41 = 0 and p = 2 whenever p|ai
for i ∈ B1. By taking J = B1, we have B1 = I +
5 ∪ I −
5 with

I +
5 = {1, 4, 9, 16, 36, 49, 64}, I −
5 = {2, 8, 18, 32}.

Thus ai = 1 for i ∈ I +
5 and ai = 2 for i ∈ I −
5 since ai ∈ {1, 2} for i ∈ B1. This is a contradiction
since 43|d, ( ai
43 ) = ( n
43 ) and ( 1
43 ) ̸= ( 2
43 ).
Let k = 89, Q0 = 79, (Q1, Q2) = (23, 73), (i23, i73) = (19, 15). Then P1 = {13, 19, 29, 31, 37, 47, 59,
61, 67, 79, 89}. We ﬁnd that M1 = {1, 9, 10, 12, 14, 21, 23, 26, 27, 29, 30, 31, 36, 41, 49, 50, 51, 57, 59, 62,
69, 75}, B1 = {0, 2, 3, 4, 5, 6, 7, 8, 11, 13, 16, 17, 18, 20, 22, 24, 25, 28, 32, 33, 34, 35, 37, 38, 39, 40, 43, 44, 45,
46, 47, 48, 52, 53, 54, 55, 56, 58, 60, 61, 63, 64, 66, 67, 68, 70, 71, 72, 73, 74, 76, 77, 78, 79, 80, 81, 82, 83, 84,
85, 86, 87}, i13 = 10, i19 = 12, i29 = 1, i31 = 26, i37 = 14 and {9, 21, 27, 29, 41} is covered by
47, 59, 61, 67, 89. Thus i89 ∈ {9, 21, 27, 29, 41}. Further for p ∈ P1, p ∤ ai for i ∈ B1. Now we take
P0 = P1 ∪ {23, 73, 79}, p1 = 19, p2 = 29, (i1, i2) := (12, 1), I = B1, P = P2 := Λ(19, 29) \ P0 =
{11, 17, 43, 53, 71} and ℓ = ℓ2 = ∑

p∈P2 ⌈ k
p ⌉ = 22. Thus |I ′| = |I| = |B1| > 2ℓ2. By Corol-
lary 10.3.3, we have M =: M2, B =: B2 and (M2, B2, P2, ℓ2) has P roperty H. We get M2 =
{0, 2, 3, 11, 17, 20, 22, 33, 35, 37, 44, 45, 54, 55, 66, 71, 77}, B2 = {4, 5, 6, 7, 8, 13, 16, 18, 24, 25, 28, 32, 34,
38, 39, 40, 43, 46, 47, 48, 52, 53, 56, 58, 60, 61, 63, 64, 67, 68, 70, 72, 73, 74, 76, 78, 79, 80, 81, 82, 83, 84, 85,
86, 87}, i11 = 0, i17 = 3, i43 = 2 and {17, 35} is covered by 53, 71. Further p ∤ ai for i ∈ B2
and p ∈ P2. We take P0 = P1 ∪ P2 ∪ {23, 73, 79}, p1 = 11, p2 = 13, (i1, i2) := (0, 10), I = B2,
P = P3 := Λ(11, 13) \ P0 = {5} and ℓ = ℓ3 = ∑

p∈P2 ⌈ k
p ⌉ = 18. Thus |I ′| = |I| = |B2| > 2ℓ3.
Then the conditions of Corollary 10.3.3 are satisﬁed and we have M =: M3, B =: B3 with
(M3, B3, P3, ℓ3) having P roperty H. We get M3 = {8, 18, 28, 43, 48, 53, 58, 68, 73, 78, 83}, B3 =
{4, 5, 6, 7, 13, 16, 24, 25, 32, 34, 38, 39, 40, 46, 47, 52, 56, 60, 61, 63, 64, 67, 70, 72, 74, 76, 79, 80, 81, 82, 84,
85, 86, 87}, i5 = 3. Lastly we take P0 = P1 ∪ P2 ∪ P3 ∪ {23, 73, 79}, p1 = 5, p2 = 11, (i1, i2) :=
(3, 0), I = B3, P = P4 := Λ(5, 11) \ P0 = {3, 41} and ℓ = ℓ4 = ∑

p∈P4 ⌈ k
p ⌉. By Lemma
10.3.2, we see that M = {4, 6, 34, 40, 46, 47, 61, 64, 67, 76, 82, 85} is covered by P4, i(P4) is even
for i ∈ B = {5, 7, 16, 24, 25, 32, 39, 52, 56, 60, 70, 72, 74, 79, 80, 81, 84, 86, 87}. Thus i3 = 1, i41 = 6
and p ∈ {2, 7, 83} whenever p|ai for i ∈ B. Since 79|d, we see that ai ∈ {1, 2, 83, 2 · 83} or
ai ∈ {7, 14, 7 · 83, 14 · 83} for i ∈ B. The latter possibility is excluded since 7 ∤ (i − i
′) for all
i, i
′ ∈ B. By taking J = B, we have B = I +
5 ∪ I −
5 with

I +
5 = {7, 24, 32, 39, 52, 72, 74, 79, 84, 87}, I −
5 = {5, 16, 25, 56, 60, 70, 80, 81, 86}.

10.7. PROOF OF LEMMA 10.4.4 95

Then we observe that either ai ∈ {1, 2 · 83} for i ∈ I +
5 and ai ∈ {2, 83} for i ∈ I −
5 or vice-versa.
This is not possible by parity argument. The other case (i23, i73) = (0, 0) is excluded similarly. □

10.7. Proof of Lemma 10.4.4

Let 7 ≤ k ≤ 97 be primes. Suppose that the assumptions of Lemma 10.4.4 are satisﬁed. Assume
that q1|d or q2|d and we shall arrive at a contradiction. We divide the proof in subsections 5.1 and
5.2
 10.7.1. The cases 7 ≤ k ≤ 23. We take r = 3 in (9.2.1). We may suppose that 5|d if k = 7, 11
and 11|d if k = 13. Let 5|d. Then
 Br ⊆ {1, 6} or Br ⊆ {2, 3}(10.7.1)

according as ( n
5 ) = 1 or −1, respectively. Thus (10.7.1) holds if k = 7, 11. Let 11|d. Then

Br ⊆ {1, 3, 5, 15} or Br ⊆ {2, 6, 10, 30}(10.7.2)

according as ( n
11 ) = 1 or −1, respectively. Let 13|d. Then

Br ⊆ {1, 3, 10, 30} or Br ⊆ {2, 5, 6, 15}(10.7.3)

according as ( n
13 ) = 1 or −1, respectively. Thus either (10.7.2) or (10.7.3) holds if 13 ≤ k ≤ 23.
We have
 F (k, r) ≤ t′
1 :=
 




F ′(k, 3) if k = 7, 11
F ′(k, 3) − 2 if 13 ≤ k < 23
F ′(k, 3) − 3 if k = 23.

For the last expression, we observe that 7 and 11 together divide at most six ai’s when k = 23.
Therefore we get from (9.2.1) that
 ξr ≥ k − t′
1(10.7.4)

We divide the proof into 4 cases.
Case I. Let 2 ∤ d and 3 ∤ d. From (10.7.1), (10.7.2), (10.7.3) and Corollary 10.4.1, we get

ξr ≤ t1 :=
 {
max(f4(k, 1, 0) + f4(k, 6, 0), f4(k, 2, 0) + f4(k, 3, 0)) + ⌈ k
4 ⌉ if k = 7, 11,
f4(k, 1, 0) + f4(k, 3, 0) + f4(k, 5, 0) + f4(k, 15, 0) + ⌈ k
4 ⌉ if k > 11

since f4(k, a, δ) is non-increasing function of a and ∑

a∈R νe(a) ≤ ⌈ k
4 ⌉. We check that t1 + t′
1 < k
contradicting (10.7.4).
Thus we have either 2|d or 3|d. Let k = 7, 11. If 2|d, then Br ⊆ {1} or Br ⊆ {3}. If 3|d, we have
Br ⊆ {1} or Br ⊆ {2}. By Lemma 9.5.3, we get ξr ≤ k−1
2 . We check that k−1
2 + t′
1 < k contradicting
(10.7.4). From now on, we may also that suppose that 13 ≤ k ≤ 23.
Case II. Let 2|d and 3 ∤ d. Then Br ⊆ {1, 3, 5, 15} if 11|d and Br ⊆ {1, 3} or Br ⊆ {5, 15} if 13|d.
Let 2||d. From Corollary 10.4.1 with δ = 1, we get

ξr ≤ F1(k, 1, 1) + F1(k, 3, 1) + F1(k, 5, 1) + F1(k, 15, 1) =: t2.

Let 4||d. From ai ≡ n(mod 4), we see that Br ⊆ {1, 5} or Br ⊆ {3, 15} if 11|d and either S = ∅ or
S = {1}, {3}, {5} or {15} if 13|d. Therefore

ξr ≤ F1(k, 1, 2) + F1(k, 5, 2) =: t3.

by Corollary 10.4.1 with δ = 2. Let 8|d. Then ai ≡ n(mod 8) and Corollary 10.4.1 with δ = 3 imply

ξr ≤ F1(k, 1, 3) =: t4.

Thus ξr ≤max(t2, t3, t4). This contradicts (10.7.4).
Case III. Let 2 ∤ d and 3|d. From ai ≡ n(mod 3), we see that either S = ∅ or S = {1}, {2}, {5} or
{10} if 11|d and Br ⊆ {1, 10} or Br ⊆ {2, 5} if 13|d. By Corollary 10.4.1, we get

ξr ≤ F1(k, 1, 0) + F1(k, 5, 0),

contradicting (10.7.4).

96 10. PROOF OF THEOREMS 2.1.1, 2.2.1 AND 2.2.2

Case IV. Let 2|d and 3|d. Then Br ⊆ {1}, {5}. By Lemma 9.5.3, we get ξr ≤ k−1
2 . We check that
k−1
2 + t′
1 < k. This contradicts (10.7.4).

10.7.2. The cases k ≥ 29. Let 29 ≤ k ≤ 59 and 19|d. Then by Lemma 10.4.3 with Q0 = 19,
we get 7|d or 17|d. Thus we get a prime pair (Q, Q
′) = (7, 19) or (Q, Q
′) = (17, 19) such that
QQ
′|d. Similarly we get (Q, Q
′) = (7, 29) or (Q, Q
′) = (17, 29) with QQ
′|d when 31 ≤ k ≤ 59 and
29|d. Let k = 71. Then we have either 43|d, 67|d or 43|d, 67 ∤ d or 43 ∤ d, 67|d. We get prime pair
(Q, Q
′) = (43, 67) with QQ
′|d if 43|d, 67|d. If 43|d, 67 ∤ d, we get from Lemma 10.4.3 with Q0 = 43
that 53|d and we take (Q, Q
′) = (43, 53) such that QQ
′|d. If 43 ∤ d, 67|d, we get from Lemma 10.4.3
with Q0 = 67 that 53|d and we take (Q, Q
′) = (53, 67) such that QQ
′|d. Similarly we get prime
pairs (Q, Q
′) with QQ
′|d for each 61 ≤ k ≤ 97 are given in the table below. For r ≤ 7, we see that

F (k, r) ≤ ∑

p>pr
p̸=Q,Q′
 ⌈ k
p ⌉ ≤ F ′(k, r) − t′
2

where t′
2 = 2, 4, 7 according as 29 ≤ k ≤ 61, 61 < k < 97, k = 97, respectively. Therefore we get
from (9.2.1) that
 ξr ≥ k + t′
2 − F ′(k, r).(10.7.5)

Case I. Let 2 ∤ d and 3 ∤ d. We take r = 5 if k = 71, (Q, Q
′) = (43, 67) and r = 4 otherwise. Then
Br ⊆ Sj(1, r) = Sj(0, 1, Q, Q′, r) for some some j with 1 ≤ j ≤ 4 where Sj(1, r) is given by (9.2.7).
For each value of k, we give below a table for (Q, Q
′) and Sj(1, r) for 1 ≤ j ≤ 4.

k (Q, Q
′) S1(1, r), S2(1, r), S3(1, r), S4(1, r)
29 ≤ k ≤ 59 (7, 19), (7, 29) {1, 30}, {2, 15}, {3, 10}, {5, 6}
29 ≤ k ≤ 59 (17, 19), (17, 29) {1, 30, 35, 42}, {2, 15, 21, 70}, {3, 10, 14, 105}, {5, 6, 7, 210}
61 (11, 59) {1, 3, 5, 15}, {2, 6, 10, 30}, {7, 21, 35, 105}, {14, 42, 70, 210}
67, 71 (43, 53) {1, 6, 10, 15}, {2, 3, 5, 30}, {7, 42, 70, 105}, {14, 21, 35, 210}
71 (43, 67) See (10.7.6)
71 (53, 67) {1, 6, 10, 15}, {2, 3, 5, 30}, {7, 42, 70, 105}, {14, 21, 35, 210}
73 (23, 53) {1, 6, 70, 105}, {2, 3, 35, 210}, {5, 14, 21, 30}, {7, 10, 15, 42}
73 (23, 67) {1, 6, 35, 210}, {2, 3, 70, 105}, {5, 7, 30, 42}, {10, 14, 15, 21}
79 (23, 53), (53, 73) {1, 6, 70, 105}, {2, 3, 35, 210}, {5, 14, 21, 30}, {7, 10, 15, 42}
79 (23, 67), (67, 73) {1, 6, 35, 210}, {2, 3, 70, 105}, {5, 7, 30, 42}, {10, 14, 15, 21}
83 (23, 37), (37, 73) {1, 3, 70, 210}, {2, 6, 35, 105}, {5, 14, 15, 42}, {7, 10, 21, 30}
89 (23, 79), (73, 79) {1, 2, 105, 210}, {3, 6, 35, 70}, {5, 10, 21, 42}, {7, 14, 15, 30}
97 (23, 37), (23, 83) {1, 3, 70, 210}, {2, 6, 35, 105}, {5, 14, 15, 42}, {7, 10, 21, 30}

For k = 71, (Q, Q
′) = (43, 67), we get from r = 5 that

S1(1, r) = {1, 6, 10, 14, 15, 21, 35, 210}, S2(1, r) = {2, 3, 5, 7, 30, 42, 70, 105}

S3(1, r) = {11, 66, 110, 154, 165, 231, 385, 2310}, S4(1, r) = {22, 33, 55, 77, 330, 462, 770, 1155}.

(10.7.6)

From Corollary 10.4.1, we get
 ξr ≤ t5 := max
1≤j≤4{ ∑

s∈Sj (1,r) F1(k, s, 0).

We check that t5 + F ′(k, r) − t′
2 < k contradicting (10.7.5).
Case II. Let 2|d and 3 ∤ d. We take r = 4 for 2||d, 4||d and r = 5 for 8|d. Let 2||d. Then
Br ⊆ {1, 3, 5, 7, 15, 21, 35, 105} =: B(2). From Corollary 10.4.1 with δ = 1, we get

ξr ≤ ∑

b∈B(2) F1(k, b, 1) =: t6

10.8. PROOF OF THEOREM 10.1.1 97

Let 4||d. Then we see that either Br ⊆ {1, 5, 21, 105} =: B(41) or Br ⊆ {3, 7, 15, 35} =: B(43). From
Corollary 10.4.1 with δ = 2, we get

ξr ≤ max
i=1,3
 ∑

b∈B(4i) F1(k, b, 2) =: t7.

Hence, if 8 ∤ d, then ξr ≤max(t6, t7). We obtain max(t6, t7) + F ′(k, r) − t′
2 < k. This contradicts
(10.7.5).
Let 8|d. Then we see from ai ≡ n(mod 8) that Br ⊆ {1, 33, 105, 385} =: B(81) or Br ⊆
{3, 11, 35, 1155} =: B(83) or Br ⊆ {5, 21, 77, 165} =: B(85) or Br ⊆ {7, 15, 55, 231} =: B(87). Then

ξr ≤ max
i=1,3,5,7
 ∑

b∈B(8i) F1(k, b, 3) =: t8.

by Corollary 10.4.1 with δ = 3. We check that t8 + F ′(k, r) − t′
2 < k contradicting (10.7.5).
Case III. Let 2 ∤ d and 3|d. We take r = 5. Then by modulo 3, we get either Br ⊆ {1, 7, 10, 22, 55, 70,
154, 385} =: B(31) or Br ⊆ {2, 5, 11, 14, 35, 77, 110, 770} =: B(32). By Corollary 10.4.1, we get

ξr ≤ max
i=1,2
 ∑

b∈B(3i) F1(k, b, 0) =: t9.

This together with (10.7.5) implies t9 + F ′(k, 5) − t′
2 ≥ k. This is contradiction.
Case IV. Let 2|d and 3|d. Let 2||d. We take r = 4. Then we see that either Br ⊆ {1, 7} or
Br ⊆ {5, 35}. By Corollary 10.4.1, we get ξr ≤ F1(k, 1, 1) + F1(k, 7, 1) which contradicts (10.7.5).
Let 4||d. We take r = 6. From ai ≡ n(mod 12), we see that

Br ⊆ B′ ∈ B := {{1, 13, 385, 5005}, {5, 65, 77, 1001}, {7, 55, 91, 715}, {11, 35, 143, 455}}.

Then
 ξr ≤ max
B′∈B
 ∑

b∈B′ F1(k, b, 2)

contradicting (10.7.5).
Let 8|d. We take r = 7. From ai ≡ n(mod 24), we see that Br ⊆ B′ = {1, 385, 1105, 17017} or
Br ⊆ B′′ ∈ B1 where B1 is the union of sets

{5, 77, 221, 85085}, {7, 55, 2431, 7735}, {11, 35, 1547, 12155}, {13, 85, 1309, 5005},

{17, 65, 1001, 6545}, {91, 187, 595, 715}, {119, 143, 455, 935}.

Let Br ⊆ B′′ ∈ B1. Then
 ξr ≤ max
B′′ ∈B1
 ∑

b∈B′′ F1(k, b, 3) =: t10

by Corollary 10.4.1. Let Br ⊆ B′. By Lemma 9.5.3, we get ν(1) ≤ k−1
2 . This together with
ν(1105) + ν(17017) ≤ 1 by 13 · 17|gcd(1105, 17017) and ν(385) ≤ 1 by Corollary 10.4.1 gives ξr ≤
k−1
2 + 2. Therefore ξr ≤max(t10, k−1
2 + 2). Now we get a contradiction from (10.7.5). □

10.8. Proof of Theorem 10.1.1

Let k = 7. By the case k = 6, we may assume that 7 ∤ d. Now the assertion follows from Lemmas
10.4.4 and 10.4.2. Let k = 8. Then by applying the case k = 7 twice to n(n + d) · · · (n + 6d) = b′y′2

and (n + d) · · · (n + 7d) = b′′y′′2, we get

(a0, · · · , a6), (a1, · · · , a7) ∈ {(2, 3, 1, 5, 6, 7, 2), (3, 1, 5, 6, 7, 2, 1), (1, 5, 6, 7, 2, 1, 10),

(2, 7, 6, 5, 1, 3, 2), (1, 2, 7, 6, 5, 1, 3), (10, 1, 2, 7, 6, 5, 1)}.

This gives (a0, · · · , a7) = (2, 3, 1, 5, 6, 7, 2, 1), (3, 1, 5, 6, 7, 2, 1, 10) or their mirror images and the
assertion follows. Let k = 9. By applying the case k = 8 twice to n(n + d) · · · (n + 7d) = b′y′2

and (n + d) · · · (n + 8d) = b′′y′′2, we get the result. Let k = 10. By applying k = 9 twice, we get
(a0, a1, · · · , a8), (a1, a2, · · · , a8, a9) ∈ {(2, 3, · · · , 1, 10), (10, 1, · · · , 3, 2)} which is not possible.

98 10. PROOF OF THEOREMS 2.1.1, 2.2.1 AND 2.2.2

Let k ≥ 11 and k′ < k be consecutive primes. We suppose that Theorem 10.1.1 is valid with
k replaced by k′. Let k|d. Then ( ai
k ) = ( n
k ) for all 0 ≤ i < k. By applying the case k = k′ to
n(n+d) · · · (n+(k′−1)d) = b′y′2 with P (b′) ≤ k′, we get k′ ≤ 23 and 1, 2, 3, 5 ∈ {a0, a1, a2, · · · , ak′−1}
in view of (2.2.2) and (2.2.3). Therefore ( 2
k ) = ( 3
k ) = ( 5
k ) = 1 which is not possible.
Thus we may assume that k ∤ d and k|n + id for some 0 ≤ i ≤ k−1
2 by considering the mirror
image (2.2.1) of (2.1.1) whenever Theorem 10.1.1 holds at k′. We shall use this assertion without
reference in the proof of Theorem 10.1.1.
Let k = 11. By Lemmas 10.4.4 and 10.4.2, we see that 11|n + id for 0 ≤ i ≤ 3. If 11|n, the
assertion follows by the case k = 10. Let 11|n + d. We consider (n + 2d) · · · (n + 10d) = b′y′2 with
P (b′) ≤ 7 and the case k = 9 to get (a2, a3, · · · , a10) ∈ {(2, 3, 1, 5, 6, 7, 2, 1, 10), (10, 1, 2, 7
, 6, 5, 1, 3, 2)}. The ﬁrst possibility is excluded since 1 = ( 14
11 ) = ( a2a7
11 ) = ( 1·6
11 ) = −1. For the
second possibility, we observe P (a0) ≤ 5 since gcd(a0, 7 · 11) = 1 and this is excluded by the case
k = 6 applied to n(n + 2d)(n + 4d)(n + 6d)(n + 8d)(n + 10d). Let 11|n + 2d. Then by the case k = 8,
we have (a3, a4, · · · , a10) ∈ {(2, 3, 1, 5, 6, 7, 2, 1), (3, 1, 5, 6, 7, 2, 1, 10), (1, 2, 7, 6, 5, 1, 3, 2),
(10, 1, 2, 7, 6, 5, 1, 3)}. The ﬁrst three possibilities are excluded by considering the values of Legendre
symbol mod 11 at a3, a8; a3, a4 and a3, a5, respectively. If the last possibility holds, then a0 = 1
since gcd(a0, 2 · 3 · 5 · 7 · 11) = 1 and this is not possible since 1 = ( a0a4
11 ) = ( (−2)2
11 ) = −1. Let

11|n + 3d. We consider (n + 4d) · · · (n + 10d) = b′y′2 with P (b′) ≤ 7 and the case k = 7 to get
(a4, · · · , a10) ∈ {(2, 3, 1, 5, 6, 7, 2), (3, 1, 5, 6, 7, 2, 1), (1, 5, 6, 7, 2, 1, 10), (2, 7, 6, 5, 1, 3, 2),
(1, 2, 7, 6, 5, 1, 3), (10, 1, 2, 7, 6, 5, 1)} which is not possible as above. This completes the proof for
k = 11. The assertion for k = 12 follows from that of k = 11.
Let k = 13. Then the assertion follows from Lemmas 10.4.4, 10.4.2 and the case k = 11. Let
k = 14. By applying k = 13 to n(n + d) · · · (n + 12d) = b′y′2 and (n + d) · · · (n + 13) = b′′y′′2, we get
the assertion. Let k = 15. Then applying k = 14 both to n(n+d) · · · (n+13d) and (n+d) · · · (n+14d)
gives the result. Now k = 16 follows from the case k = 15.
Let k = 17. Then 17|n + 2d or 17|n + 3d by Lemmas 10.4.4, 10.4.2 and the case k = 15. Let
17|n + 2d. Then by applying the case k = 14 to (n + 3d) · · · (n + 16d) = b′y′2 with P (b′) ≤ 13, we get
(a3, a4, · · · , a16) ∈ {(3, 1, · · · , 15, 1), (1, 15, · · · , 1, 3)}. The ﬁrst possibility is excluded by Legendre
symbol mod 17 at a3, a4. For the second, we observe that gcd(a1, 7 · 11 · 13 · 17) = 1 which is not
possible by the case k = 6 applied to (n+d)(n+4d)(n+7d)(n+10d)(n+13d)(n+16d). Let 17|n+3d.
By considering (n + 4d) · · · (n + 16d) = b′y′2 with P (b′) ≤ 13, it follows from the case k = 13 that
(a4, · · · , a16) ∈ {(3, 1, · · · , 14, 15), (1, 5, · · · , 15, 1), (15, 14, · · · , 1, 3), (1, 15, · · · , 5, 1)}. The ﬁrst three
possibilities are excluded by considering Legendre symbol mod 17 at a4, a5. If the last possibility
holds, we observe that a1 = 1 since gcd(a1, ∏
p≤17 p) = 1 and then 1 = ( a1a4
17 ) = ( (−6)(−3)
17 ) = −1,
a contradiction. The assertion for k = 18 follows from that of k = 17.
Let k = 19. Then the assertion follows from Lemmas 10.4.4, 10.4.2 and the case k = 17. By
applying k = 19 twice to n(n + d) · · · (n + 18d) and (n + d) · · · (n + 18d)(n + 19d), the assertion for
k = 20 follows and this implies the cases k = 21, 22.
Let k = 23. We see from Lemmas 10.4.4, 10.4.2 and the case k = 20 that 23|n + 3d. We consider
k = 19 and (n + 4d) · · · (n + 22d) = b′y′2 with P (b′) ≤ 19 to get (a4, a5, · · · , a22) = (1, 5, · · · , 21, 22)
or (22, 21, · · · , 5, 1). By considering the values of Legendre symbol mod 23 at a4 and a5, we may
assume the second possibility. Now P (a2) ≤ 11 and this is not possible by the case k = 11 applied to
(n + 2d)(n + 4d) · · · (n + 22d). Let k = 24. We get (a0, a1, · · · , a23) = (5, 6, · · · , 3, 7), (7, 3, · · · , 6, 5)
by considering k = 23 both to n(n + d) · · · (n + 22d) and (n + d) · · · (n + 23d). Further the assertion
for 25 ≤ k ≤ 28 follows from k = 24.
Let k ≥ 29. First we consider k = 29. We see from Lemmas 10.4.4, 10.4.2 and the case k = 25
that 29|n+4d or 29|n+5d. Let 29|n+4d. Then considering k = 24 and (n+5d)(n+6d) · · · (n+28d), we
get (a5, a6, · · · , a28) = (5, 6, · · · , 3, 7) or (7, 3, · · · , 6, 5). By observing 1 = ( 30
29 ) = ( a5a6
29 ) = ( 1·2
29 ) =

−1, we may assume the second possibility. Then a1 = 1 implying 1 = ( a2a8
29 ) = ( (−2)4
29 ) = −1,

a contradiction. Let 29|n + 5d. Now by considering k = 23 and (n + 6d) · · · (n + 28d), we get
(a6, a7, · · · , a28) ∈ {(5, 6, · · · , 26, 3), (6, 7, · · · , 3, 7), (3, 26, · · · , 6, 5),

10.9. PROOF OF THEOREM 2.1.1 99

(7, 3, · · · , 7, 6)}. Then we may restrict to the last possibility by considering the Legendre symbol
mod 29 at the ﬁrst two entries in the remaining possibilities. It follows that a3 = 1 implying
1 = ( a3a9
29 ) = ( (−2)4
29 ) = −1, a contradiction. This completes the proof for k = 29. We now proceed
by induction. By Lemmas 10.4.4 and 10.4.2, the assertion follows for all primes k. Now Lemma
9.1.1 completes the proof of Theorem 10.1.1. □

10.9. Proof of Theorem 2.1.1

Observe that for all tuples in (2.2.2) and (2.2.3), the product of the ai’s is not a square. Hence,
by Theorem 10.1.1, we may assume that 101 ≤ k ≤ 109. Assume (2.1.1) with b = 1. Then
ordp(a0a1 · · · ak−1) is even for each prime p. Let 101 ≤ k ≤ 105. Then P (a4a5 · · · a100) ≤ 97. Now
the assertion follows from Theorem 10.1.1 by considering (n + 4d) · · · (n + 100d) and k = 97. Let
k = 106, 107. Then P (a4a5 · · · a102) ≤ 101. We may suppose that P (a4a5) = 101 or P (a101a102) =
101 otherwise the assertion follows by the case k = 99 in Theorem 10.1.1. Let P (a4a5) = 101.
Then P (a6 · · · a102) ≤ 97 and the assertion follows by k = 97 in Theorem 10.1.1. This is also
the case when P (a101a102) = 101 since P (a4 · · · a100) ≤ 97 in this case. Let k = 108, 109. Then
P (a6 · · · a102) ≤ 101. Thus either P (a6a7) = 101 or P (a101a102) = 101. Let P (a6a7) = 101. Then
P (a8 · · · a102) ≤ 97. We may assume that 97|a8a9a10a11 or 97|a97 · · · a101a102. Let 97|a8a9a10a11.
Then P (a12a13 · · · a102) ≤ 89 and the assertion follows by the case k = 91 of Theorem 10.1.1. Let
97|a97 · · · a102. Then P (a8a9 · · · a96) ≤ 89 and the assertion follows from the case k = 89 of Theorem
10.1.1. When P (a101a102) = 101, we argue as above to get the assertion. □

CHAPTER 11

Equation (2.1.1) with with ω(d) ≤ 6 or d ≤ 10
10:
Proof of Theorems 2.3.1, 2.4.1, 2.5.1, 2.5.2, 2.5.3

In this chapter, we prove Theorems 2.3.1, 2.4.1, 2.5.1, 2.5.2 and 2.5.3. From now on, we take
t = k. Thus bj = aj−1, Bj = Aj−1, yj = xj−1 and Yj = Xj−1 for 1 ≤ j ≤ k in (9.1.2) and (9.1.3).
By using Theorem 10.1.1, we take k > 100. As in [76], the proof of our theorems depend on
showing that the upper bound and lower bound for n + (k − 1)d are not consistent whenever it is
possible to ﬁnd a non-degenerate double pair. A lower bound for n + (k − 1)d is obtained by using
lemmas stated in Section 9.4 and Lemma 11.1.3. Further by using the lemmas stated in Section 9.3,
we give an upper bound for n + (k − 1)d whenever it is possible to ﬁnd a non-degenerate double pair.
This is always the case whenever k − |R| ≥ 2ω(d)−θ. If we do not have this, we use Lemmas 9.3.13
and 11.1.2 depending on an idea of Erd˝os to give an upper bound for k. Thus there are only ﬁnitely
many possibilities for k and we use counting arguments given in Section 9.2 and computational
lemmas in Section 11.1 to exclude these possibilities. For example, we show in Lemma 11.1.1 that k
is large whenever d is divisible by two small primes. This is very useful in our proofs and increases
considerably a lower bound for d in Theorem 2.4.1.

11.1. Computational Lemmas

Lemma 11.1.1. Let k ≥ 101. Assume (2.1.1).
(a) Let d be odd and p < q be primes such that pq|d with p ≤ 19, q ≤ 47. Then k ≥ 1733.
(b) Let d be odd and p < q be primes such that pq|d with 23 ≤ p < q ≤ 43, (p, q) ̸= (31, 41). Then
k ≥ 1087.
(c) Let d be even such that p|d with 3 ≤ p ≤ 47. Then k ≥ 1801.

Proof. We shall use the notation and results of Section 8.2 without reference. By Lemma
9.1.1, it suﬃces to prove Lemma 11.1.1 when k is a prime. Let P0 be the largest prime ≤ k such
that P0 ∤ d. Then (2.1.1) holds at k = P0. Therefore P0 ≥ 101 by Theorem 10.1.1 with k = 97.
Thus there is no loss of generality in assuming that k ∤ d for the proof of Lemma 11.1.1.
(a) Let d be odd and p, q be as in (a). Assume k < 1733. It suﬃces to consider 4 cases, viz
(i) 5 < p < q, 3 ∤ d, 5 ∤ d; (ii) p = 3, q > 5, 5 ∤ d; (iii) p = 5, q > 5, 3 ∤ d and (iv) p = 3, q = 5. We
take r ≥ 7. We see that Br is contained in one of the four sets Sµ = Sµ(1, r) with 1 ≤ µ ≤ 4. Let
S ′
µ = {s ∈ Sµ : s < 2000} with 1 ≤ µ ≤ 4. We have ν(s) ≤ F0(k, s, 0) by Lemma 9.5.2. Further
ν(s) ≤ 1 for s ≥ k and hence for s ∈ Sµ \ S ′
µ. Observe that 1 ∈ S ′
1 ⊆ S1.
Assume that 1 /∈ R in the case (iv). For the case (i), we take r = 7 for 101 ≤ k < 1087
and r = 8 for 1087 ≤ k < 1733. For all other cases, we take r = 7 for 101 ≤ k < 941,
r = 8 for 941 ≤ k < 1297 and r = 9 for 1297 ≤ k < 1733. Then ξr ≤ max ∑

s∈Sµ ν(s) ≤

max (gp,q − |S ′
µ| + ∑

s∈S ′
µ F (k, s, 0)
) ≤ gp,q + max ∑

s∈S ′
µ(F0(k, s, 0) − 1) =: ˜ξr where the maximum

is taken over 1 ≤ µ ≤ 4 and we remove 1 from S ′
1 ⊆ S1 when the case (iv) holds. We now check that

k − F ′(k, r) − ˜ξr >
 




0 if p < q ≤ pr
−
⌈ k
q ⌉ if p ≤ pr < q
−
⌈ k
p ⌉ − ⌈ k
q ⌉ if pr < p < q.
(11.1.1)

This contradicts (9.2.1) by using the estimates for gp,q and ˜ξr ≥ ξr.

101

102 11. PROOF OF THEOREMS 2.3.1, 2.4.1, 2.5.1, 2.5.2, 2.5.3

Thus it remains to consider (iv) with 1 ∈ R. Then ( ai
3 ) = ( ai
5 ) = 1 for all ai ∈ R. Suppose
that p′ ∤ d for some prime p′ ∈ P = {7, 11, 13}. We take r = 9. We have Br ⊆ S1. Further
|S1| = 32 and S ′
1 = {1, 19, 34, 46, 91, 154, 286, 391, 646, 874, 1309, 1729, 1771}. We get from (9.5.1)
that νo(a) ≤ min(f0(k, a, 0), f1(k, a, p
′, 1, 0)) ≤ min(f0(k, a, 0), max
p′∈P{f1(k, a, p
′, 1, 0)}) := G1(k, a).

Similarly we get from (9.5.2) that νe(a) ≤min(g0(k, a, 2), max
p′∈P{g1(k, a, p
′, 1, 0)} := G2(k, a). Let

G(k, a) = 1 if k ≤ a and G(k, a) = G1(k, a) + G2(k, a) if k > a. Then ν(a) ≤ G(k, a) implying
ξr ≤ 32 + ∑

s∈S ′
1(G(k, s) − 1) =: ˜ξr as above. We check that

k − F ′(k, r) − ˜ξr > 0.(11.1.2)

This contradicts (9.2.1). Thus p′|d for each prime p ∈ P. Now we take r = 14. Since 1 ∈ R,

we have ( ai
p ) = 1 for all ai ∈ R and for each p with 3 ≤ p ≤ 13. Therefore Br ⊆ {s ∈ S(r) :
( s
p ) = 1, 3 ≤ p ≤ 13} = {1, 1054} ∪ S ′′ where |S ′′| = 14 and s > 2000 for each s ∈ S ′′. Hence

ξr ≤ ν(1) + ν(1054) + 14 ≤ ν(1) + 16 since ν(1054) ≤ 2 by Lemma 9.5.2. From (9.5.1) and (9.5.2)
with µ = 3, we get ν(1) ≤ f0(k, 1, 0) + g0(k, 1, 3). Therefore ξr ≤ f0(k, 1, 0) + g0(k, 1, 3) + 16 =: ˜ξr
and we compute that (11.1.2) holds contradicting (9.2.1).
(b) Let d be odd and p, q be as in (b). Assume k < 1013. By (a), we may assume that 3 ∤
d, 5 ∤ d. We continue the proof as above in the case (i) of (a). We take r = 7 and check that
k − F ′(k, r) − ˜ξr + ⌈ k
p ⌉ + ⌈ k
q ⌉ > 0. This contradicts (9.2.1).
(c) Let d be even and p be as in (c). Assume k < 1801. For any set W of squarefree integers, let
W ′ = W ′(δ) = {s ∈ W : s < 2000
23−δ }. We consider four cases, viz (i) p > 5, 3 ∤ d, 5 ∤ d; (ii) p = 5, 3 ∤ d;
(iii) p = 3, 5 ∤ d and (iv) 15|d. We take r ≥ 7. Assume that (i), (ii) or (iii) holds. Then from (9.2.7)
with p = q, we get 2
δ sets Uµ, 1 ≤ µ ≤ 2δ given by S1(n′, r), S4(n′, r). Without loss of generality, we
put S1(1, r) = U1. Further |Uµ| ≤ gp for 1 ≤ µ ≤ 2δ. Assume (iv). We take p = 3, q = 5 in (9.2.7).
We get 2
δ+1 sets Vµ, 1 ≤ µ ≤ 2δ+1 given by Sj(n′, r), 1 ≤ j ≤ 4 and we put S1(1, r) = V1. Further
|Vµ| ≤ 2r−δ−4 for 1 ≤ µ ≤ 2δ+1. We deﬁne g′ by g′ = 2r−δ−4 if (iv) holds and g′ = gp otherwise.
Further let Wµ with 1 ≤ µ ≤ 2δ+1 be given by Wµ = Vµ if (iv) holds and Wµ = Uµ for 1 ≤ µ ≤ 2δ,
Wµ = ∅ for µ > 2δ if (i), (ii) or (iii) holds. We see from Lemma 9.5.2 that ν(s) ≤ F0(k, s, δ) and
ν(s) ≤ 1 for s ∈ Wµ \ W ′
µ. Observe that 1 ∈ W ′
1 ⊆ W1.
Assume that 1 /∈ R in the cases (ii), (iii) or (iv). We take r = 8 for 101 ≤ k ≤ 941, r = 9 for
941 < k ≤ 1373 and r = 10 for 1373 < k < 1801 in the case (i) with 8|d. For all other cases, we
take r = 7 for 101 ≤ k ≤ 941, r = 8 for 941 < k ≤ 1373 and r = 9 for 1373 < k < 1801. Then
ξr ≤ max ∑

s∈Wµ F (k, s, δ) ≤ g′ + max ∑

s∈W ′
µ(F0(k, s, δ) − 1) =: ˜ξr where maximum is taken over

1 ≤ µ ≤ 2δ+1 and we remove 1 from W ′
1 ⊆ W1 when (ii), (iii) or (iv) holds. We check that

k − F ′(k, r) − ˜ξr >
 {
−
⌈ k
p ⌉ if (i) holds with p > pr
0 otherwise.

This contradicts (9.2.1).
Thus it remains to consider the cases (ii), (iii) or (iv) and 1 ∈ R. Then ai ≡ 1(mod 2
δ)

and ( ai
p ) = 1 for all p|d whenever ai ∈ R. Let P0 = {5}, {3}, {3, 5} when (ii), (iii), (iv) holds,

respectively. Then ( ai
p ) = 1 for p ∈ P0.

Assume that 7 ∤ d when 8|d, 15|d. Let P = {7} if 8|d, 3|d, 5 ∤ d; P = {7, 11, 13, 17, 19} if 4||d, 15|d;
P = {11, 13, 17, 19} if 8|d, 15|d and P = {7, 11, 13} in all other cases. Suppose that p′ ∤ d for some
prime p′ ∈ P. Let r be given by the following table:

(ii), (iii), 2||d, 4||d (ii), (iii), 8|d (iv), 2||d (iv), 4||d, 8|d{
8 for k ≤ 941
9 for k > 941
 {
10 for k ≤ 941
11 for k > 941 9 11

11.1. COMPUTATIONAL LEMMAS 103

We get Br ⊆ W1. For s ∈ W ′
1, we get from (9.5.1) that ν(s) = νo(s) ≤ G(k, s, δ) := min(f0(k, s, δ), G1, G2)
where
 (G1, G2) =
 




(f1(k, s, 3, 2, δ), maxp′∈P f2(k, s, 3, p′, 2, δ)) when (ii) holds, 8 ∤ d
(f1(k, s, 5, 1, δ), maxp′∈P f2(k, s, 5, p′, 1, δ)) when (iii) holds, 8 ∤ d
(f1(k, s, 3, 1, 3), maxp′∈P f2(k, s, 3, p′, 2, 3)) when (ii) holds, 8|d
(f1(k, s, 5, 1, 3), maxp′∈P f2(k, s, 5, p′, 2, 3)) when (iii) holds, 8|d

and when (iv) holds, G1 = G2 = maxp′∈P f1(k, s, p
′, 1, δ) if 2||d or 4||d, G1 = G2 = maxp′∈P f2(k, s, 7, p′, 1, 3)
if 8|d. Therefore ξr ≤ g′ + ∑

s∈W ′
1(G(k, s, δ) − 1) =: ˜ξr. Now we check (11.1.2) contradicting (9.2.1).
Thus p′|d for each prime p′ ∈ P. Let r and g1 be given by the following table:

Cases: (ii), (iii), 2||d (ii), (iii), 4||d (ii), 8|d (iv), 2||d (iv), 8|d
(r, g1) (12, 8) (12, 4) (15, 16) (13, 4) (17, 4)

Suppose that one of the above case hold. Then Br ⊆ {s ∈ S(r) : s ≡ 1(mod 2
δ), ( s
p′ ) = 1, p′ ∈

P ∪ P0} = {1} ∪ W ′′ with |W ′′| = g1 − 1 and s ≥ 2000
23−δ for s ∈ W ′′. Therefore ξr ≤ ν(1) + g1 − 1.
From (9.5.1), we get ν(1) ≤ G(k) where G(k) = f1(k, 1, 3, 2, δ) if (ii) holds; f1(k, 1, 5, 2, δ) if (iii)
holds, 8 ∤ d; G(k) = f0(k, 1, 1) if (iv) holds with 2||d and G(k) = f1(k, 1, 7, 2, 3) if (iv) holds with 8|d.
Therefore ξr ≤ G(k) + g1 − 1 =: ˜ξr and we compute that (11.1.2) holds. This contradicts (9.2.1).
Thus either (A) : (iv) holds, 4||d or (B) : (iii) holds, 8|d. Assume that p′ ∤ d with p′ ∈ P1 where
P1 = {23, 29, 31, 37}, {11, 13, 17, 19} when (A), (B) holds, respectively. In the remaining part of this
paragraph, by ’respectively”, we mean “when (A), (B) holds, respectively’. We take r = 18, 11,

respectively. Then Br ⊆ {s ∈ S(r) : s ≡ 1(mod 2
δ), ( s
p′ ) = 1, p′ ∈ P ∪ P0} ⊆ {1, 1705} ∪ W ′′ with

|W ′′| = g1 and s ≥ 2000
23−δ for s ∈ W ′′ where g1 = 3, 14, respectively. Hence ξr ≤ ν(1) + ν(1705) + g1 ≤
G(k) + 2 + g1 =: ˜ξr where ν(1) ≤ G(k) = maxp′∈P1 f1(k, 1, p′, 1, 2), maxp′∈P1 f2(k, 1, 5, p′, 1, 3),
respectively by (9.5.1). We check (11.1.2), contradicting (9.2.1). Thus p′|d with p′ ≤ 37 if (A) holds
and p′|d with p′ ≤ 19, p′ ̸= 5 if (B) holds. Now we take r = 22, 16, respectively to get Br ⊆ {1} ∪ W ′′

with |W ′′| = g2 and s ≥ 2000
23−δ for s ∈ W ′′ where g2 = 0, 3, respectively. From (9.5.1), we get
ν(1) ≤ G(k) with G(k) = f0(k, 1, 2), f1(k, 1, 5, 2, 3), respectively. Hence ξr ≤ G(k) + g2 =: ˜ξr and
we compute that (11.1.2) holds. This contradicts (9.2.1).
Thus it remains to consider the case (iv) with 8|d and 7|d. Then

ai ≡ 1(mod 8) and ( ai
p
 ) = 1 for p = 3, 5, 7(11.1.3)

whenever ai ∈ R. Let k < 263. By taking r = 12, we ﬁnd that Br ⊆ {s ∈ S(r) : s ≡

1(mod 8), ( s
pj
 ) = 1, 2 ≤ j ≤ 4} = {1, 6409, 9361, 12121, 214489, 268801, 4756609, 59994649}. Then

by Lemma 9.5.3, ν(1) ≤ k−1
2 since k ∤ d by our assumption. Further ν(6409) + ν(268801) +
ν(4756609) + ν(59994649) ≤ ⌈ k
13·29 ⌉ ≤ 1, ν(9361) + ν(214489) ≤ ⌈ k
11·37 ⌉ ≤ 1 and ν(12121) ≤ 1.
Therefore ξr ≤ k−1
2 + 3 =: ˜ξr. We check (11.1.2) contradicting (9.2.1). Thus k ≥ 263. By (11.1.3),
we see that ai is not a prime ≤ 89. Hence for ai ∈ R with P (ai) ≤ 89, we have ω(ai) ≥ 2. Further
by (11.1.3), ai = p′q′ with 11 ≤ p′ ≤ 37 and 41 ≤ q′ ≤ 89 is not possible. For integers P1, P2 with
P1 < P2, let
 I(P1, P2) = {i : p′q′|ai, P1 ≤ p′ < q′ ≤ P2}.

Then |I(P1, P2)| ≤ ∑

P1≤p′<q′≤P2 ⌈ k
p′q′ ⌉. Suppose that pj ∤ d for some prime j ∈ {5, 6}. Then
ν(1) ≤ G0(k) := maxj=5,6 f1(k, 1, pj, 2, 3) by (9.5.1). We take r = 23. For P0 ∈ {11, 13}, let
A(P0) = {ai : ai = P0p′ with P0 < p′ ≤ 37 or ai = P0p′q′ with P0 < p′ ≤ 37, 41 ≤ q′ ≤ 83}. Then
from (11.1.3), we get A(11) ⊆ {6721, 8569, 25201} and A(13) ⊆ {17329, 17641, 27001}. Therefore we

104 11. PROOF OF THEOREMS 2.3.1, 2.4.1, 2.5.1, 2.5.2, 2.5.3

get from
 Ir ⊆{i : ai = 1} ∪ I(17, 37) ∪ I(41, 83)∪

{i : ai ∈ A(11) ∪ A(13)} ∪ {i : 11 · 13p′|ai, 17 ≤ p′ ≤ 37}

that
 ξr ≤ G0(k) + ∑

17≤p′<q′≤37
 ⌈ k
p′q′ ⌉ + ⌈ k
41 · 43 ⌉ + 54 + 3 + 3 + 6 =: ˜ξr

since p′q′ > k for 41 ≤ p′ < q′ ≤ 83 except when p′ = 41, q′ = 43. Now we compute that (11.1.2)
holds contradicting (9.2.1). Thus pj|d for j ≤ 6. Assume that pj ∤ d for some j with 7 ≤ j ≤ 9.
Then ν(1) ≤ G1(k) := max7≤j≤9 f1(k, 1, pj, 1, 3) by (9.5.1). We take r = 24. Then Ir ⊆ {i :
ai = 1} ∪ I(17, 37) ∪ I(41, 89). Therefore ξr ≤ G1(k) + ∑

17≤p′<q′≤37 ⌈ k
p′q′ ⌉ + ⌈ k
41·43 ⌉ + 65 =: ˜ξr
and we check (11.1.2). This contradicts (9.2.1). Thus pj|d for j ≤ 9. Suppose that pj ∤ d for
some j with 10 ≤ j ≤ 14. Then ν(1) ≤ G2(k) := max10≤j≤14 f1(k, 1, pj, 1, 3) by (9.5.1). We take

r = 21. Then Br ⊆ {s ∈ S(r) : s ≡ 1(mod 8) and ( s
pi
 ) = 1, i ≤ 9} = {1, 241754041} giving

ξr ≤ G2(k) + 1 =: ˜ξr. Now we check (11.1.2) contradicting (9.2.1). Hence pj|d for j ≤ 14. Suppose
that pj ∤ d for some j with 15 ≤ j ≤ 22. Then ν(1) ≤ G3(k) := max15≤j≤22 f1(k, 1, pj, 1, 3) by
(9.5.1). We take r = 26. Then Br ⊆ {1} as above giving ξr ≤ G2(k) =: ˜ξr. We compute that
(11.1.2) holds contradicting (9.2.1). Thus pj|d for j ≤ 22. Finally we take r = 32. Then Br ⊆ {1}
as above giving ξr ≤ ν(1) ≤ k−1
2 =: ˜ξr by Lemma 9.5.3. We check (11.1.2). This contradicts
(9.2.1). □

Lemma 11.1.2. We have
 k − |R| ≥ g for k ≥ k0(g)(11.1.4)

where g and k0(g) are given by
(i)
 g 9 14 17 29 33 61 65 129 256 2s with s ≥ 9, s ∈ Z
k0(g) 101 299 308 489 556 996 1057 2100 4252 s2s+1

(ii) d even:
 g 18 29 33 61 64 128 256 512 1024
k0(g) 101 223 232 409 430 900 1895 4010 8500

(iii) 4||d:
 g 26 32 33 61 64 128 256 512 1024
k0(g) 101 126 129 286 303 640 1345 2860 6100

(iv) 8|d:
 g 33 61 64 128 256 512 1024
k0(g) 101 209 220 466 990 2110 4480

(v) 3|d:
 g 26 32 33 64 125 128 256 512
k0(g) 101 126 129 351 720 735 1550 3300

(vi) p|d with p ∈ {5, 7} :
 g 33 64 128 256
k0(g) 240 460 930 1940

Further we have k0(128) = 1200 if p|d with p ≤ 19 and k0(256) = 2870 if p|d with p ≤ 47.
(vii) Further k0(256) = 1115 if pq|d with p ∈ {5, 7, 11}; k0(256) = 1040 if 2p|d with p ∈ {3, 5};
k0(512) = 1400 if 105|d; k0(512) = 1440 if 30|d and k0(512) = 1480 if 8p|d with p ∈ {3, 5}.

11.1. COMPUTATIONAL LEMMAS 105

Proof. (i) Let g be given as in (i). Assume that k ≥ k0(g) and k − |R| < g. We shall arrive at
a contradiction.
Let g ̸= 9. From (9.4.9), we have ∏
ai∈R ai ≥ (1.6)
|R|(|R|)! whenever |R| ≥ 286. We observe
that (9.3.28) and (9.3.29) hold with i0 = 0, h0 = 286, z1 = 1.6, g1 = g − 1, m =min(89, √k0(g)), ℓ =
0, n0 = 1, n1 = 1 and n2 = 2 1
6 for k ≥ g1 + 286 and thus for k ≥ k0(g).
Let g = 2
s with s ≥ 9. Then g1
k ≤ 2s
s2s+1 ≤ 1
18 and we get from (9.3.29)

2s − 1 > c1k − c2 log k − c3
log c4k = c1k − c3 + c2 log c4
log c4k − c2(11.1.5)

where
 c1 = log
 

 1.6
2.71851
 ∏

p≤m
p
 2
p2−1
 

 + log(1 − 1
18 ), c2 = 1.5π(m) − 1,

c3 = log
 

2 1
6 ∏

p≤m
p.5+ 2
p2−1
 

 − 1
2 log(1 − 1
18 ), c4 = 1.6
e

Here we check that c1k −c2 log k −c3 > 0 at k = 9·210 and hence (11.1.5) is valid. Further we observe
that the right hand side of (11.1.5) is an increasing function of k. Putting k = k0(g) = s2s+1, we
get from (11.1.5) that
 2s { 2c1 − c3−c2 log c4
s2s
log 2 + log(2c4s)
s − c2 − 1
2s − 1
}
 < 0.

The expression inside the brackets is an increasing function of s and it is positive at s = 9. Hence
(11.1.5) does not hold for all k ≥ k0(g). Therefore k − |R| ≥ g = 2
s whenever s ≥ 9 and k ≥ s2s+1.
Let g ∈ {14, 17, 29, 33, 61, 65, 129, 256} and k1(g) = 299, 316, 500, 569, 1014, 1076, 2126, 4295 ac-
cording as g = 14, 17, 29, 33, 61, 65, 129, 256, respectively. We see that the right hand side of (9.3.29)
is an increasing function of k and we check that it exceeds g1 at k = k1(g). Therefore (9.3.29) is
not possible for k ≥ k1(g). Thus g ̸= 14 and k < k1(g). For every k with k0(g) ≤ k < k1(g), we
compute the right hand side of (9.3.28) and we ﬁnd it greater than g1. This is not possible.
Thus we may assume that g = 9 and k < 299. By taking r = 4 for 101 ≤ k ≤ 181 and r = 5
for 181 < k < 299 in (9.2.3) and (9.2.5), we get k − |R| ≥ k − F ′(k, r) − 2r ≥ 9 for k ≥ 101
except when 103 ≤ k ≤ 120, k ̸= 106 where k − |R| ≥ k − F (k, r) − 2r ≥ k − F ′(k, r) − 2r = 8. Let
103 ≤ k ≤ 120, k ̸= 106. We may assume that k−|R| = 8 and hence F (k, r) = F ′(k, r). Thus for each
prime 11 ≤ p ≤ k, there are exactly σp number of i’s for which p|ai and for any i, pq ∤ ai whenever
11 ≤ q ≤ k, q ̸= p. Now we get a contradiction by considering the i’s for which ai’s are divisible by
primes 17, 101; 103, 17; 13, 103; 53, 13; 107, 53; 11, 109; 37, 11; 19, 113; 23, 19; 29, 23; 13, 29; 59, 13; 17, 59
when k = 103, 104, 105, 107, 108, 111, 112, 115, 116, 117, 118, 119, 120, respectively; 107, 53, 13, 103, 17
when k = 109, 109, 107, 53 when k = 110; 37, 11, 109, 107 when k = 113 and 113, 37, 11 when k = 114.
For instance let k = 113. Then 37|ai for i ∈ {0, 37, 74, 111} or i ∈ {1, 38, 75, 112}. We consider the
ﬁrst case and the other case follows similarly. Then 11|ai for i ∈ {2 + 11j : 0 ≤ j ≤ 10} and 109|ai
for i ∈ {1, 110}. Now σ107 = 2 implies that 107|aiai+107 for i ∈ {j : 0 ≤ j ≤ 5}, a contradiction.
The other cases are excluded similarly.
(ii) Let d be even and g be given as in (ii). Assume that k ≥ k0(g) and k − |R| < g. From (9.4.10),
we have ∏
ai∈R ai ≥ (2.4)
|R|(|R|)! whenever |R| ≥ 200. By taking i0 = 0, h0 = 200, m = √
k0(g),
z1 = 2.4, ℓ = 1, n0 = 2 1
3 , n1 = 2 1
6 and n2 = 1, we observe that (9.3.28) and (9.3.29) are valid for
k ≥ g − 1 + 200. Let g ∈ {33, 61, 64, 128, 256, 512, 1024}. Thus (9.3.28) and (9.3.29) are valid for k ≥
k0(g). Let k1(g) = 232, 414, 435, 904, 1907, 4024, 8521 according as g = 33, 61, 64, 128, 256, 512, 1024,
respectively. We see that (9.3.29) is not possible for k ≥ k1(g). Therefore g ̸= 33 and k < k1(g). For
every k with k0(g) ≤ k < k1(g), we check that (9.3.28) is contradicted. Therefore g ∈ {18, 29} and
we may assume that k < 232. We take r = 5 for 101 ≤ k < 200 and r = 6 for 200 ≤ k < 232. From
(9.2.10) and (9.2.6), we get k−|R| ≥ k−F ′(k, r)−2r−1. We compute that k−F ′(k, r)−2r−1 ≥ 18, 29
for k ≥ 101, 217, respectively. Hence the assertion (ii) follows.

106 11. PROOF OF THEOREMS 2.3.1, 2.4.1, 2.5.1, 2.5.2, 2.5.3

(iii), (iv) Let g be given as in (iii), (iv). Suppose that k ≥ k0(g) and k − |R| < g. We have∏
ai∈R ai ≥ (2
δ)
|R|−1(|R| − 1)! since ai ≡ n(mod 2δ). We take z1 = 4 if 4||d and z1 = 8 if 8|d.
We observe that (9.3.28) and (9.3.29) are valid for k ≥ k0(g) with i0 = 1, h0 = 1, m = √
k0(g),
z1 = 2
,ℓ = 1, n0 = 2 1
3 , n1 = 2 1
6 and n2 = 1.
Let 4||d and g ∈ {61, 64, 128, 256, 512, 1024}. Let k1(g) = 288, 306, 640, 1350, 2870, 6100 accord-
ing as g = 61, 64, 128, 256, 512, 1024, respectively. We see that (9.3.29) is not possible for k ≥ k1(g).
Therefore g ̸= 128, 1024 and k < k1(g). For every k with k0(g) ≤ k < k1(g), we check that (9.3.28)
is contradicted.
Let 8|d and g ∈ {61, 64, 128, 256, 512, 1024}. Let k1(g) = 210, 221, 468, 994, 2111, 4485 according
as g = 61, 64, 128, 256, 512, 1024, respectively. We see that (9.3.29) is not possible for k ≥ k1(g).
Therefore k < k1(g). For every k with k0(g) ≤ k < k1(g), we check that (9.3.28) is contradicted.
Thus we may assume that g ∈ {26, 32, 33}, k < 286 if 4||d and g = 33, k < 209 if 8|d. By taking
r = 6 for 101 ≤ k < 286, we get from (9.2.10) and (9.2.6) that k − |R| ≥ k − F ′(k, r) − 2r−δ ≥ g for
k ≥ k0(g). Hence the assertions (iii) and (iv) follows.
(v) Let 3|d. Suppose that k ≥ k0(g) and k − |R| < g. We have ∏
ai∈R ai ≥ 3|R|−1(|R| − 1)!
since ai ≡ n(mod 3). We observe that (9.3.28) and (9.3.29) are valid with i0 = 1, h0 = 1, m =√
k0(g), z1 = 3, ℓ = 1, n0 = 3 1
4 , n1 = 3 1
4 and n2 = 2 1
6 . Let g ∈ {64, 125, 128, 256, 512} and
k1(g) = 354, 720, 737, 1556, 3300 according as g = 64, 125, 128, 256, 512, respectively. We see that
(9.3.29) is not possible for k ≥ k1(g). Therefore g ̸= 125, 512 and k < k1(g). For every k with
k0(g) ≤ k < k1(g), we check that (9.3.28) is contradicted.
Thus it remains to consider g ∈ {26, 32, 33} and k < 351. We take r = 6 for 101 ≤ k < 351. We
get from (9.2.10) and (9.2.14) with p = 3 that k − |R| ≥ k − F ′(k, r) − 2r−2 ≥ g for k ≥ k0(g).
(vi) Suppose g ∈ {33, 64, 128, 256}, k ≥ k0(g) and k − |R| < g. By (ii) and (v), we may assume that
2 ∤ d and 3 ∤ d. We observe that ∏
ai∈R ai ≥ ( 2p
p−1 )
|R|− p−1
2 (|R| − p−1
2 )! since the number of quadratic

residues or quadratic non-residues mod p is p−1
2 . Let p|d with p ≤ p′. Then ( 2p
p−1 )
|R|− p−1
2 (|R| −

p−1
2 )! ≥ ( 2p
′

p′−1 )
|R|− p′−1
2 (|R| − p
′−1
2 ). We take p′ = 7, 19 and 47 in the ﬁrst, second and third case,

respectively. Then (9.3.28) and (9.3.29) are valid with z1 = 2p
′

p′−1 , i0 = h0 = p
′−1
2 , m = √
k0(g), ℓ = 1,

n0 = p′ 1
p′+1 , n1 = 5 1
3 and n2 = 2 1
6 . We ﬁnd that (9.3.29) is not possible for k ≥ k0(g) + 24 and
(9.3.28) is not possible for each k with k0(g) ≤ k < k0(g) + 24. This is a contradiction.
(vii) Let (z1, i0, ℓ′, n
′
0, n
′
1) be given by

pq|d, p, q ∈ {5, 7, 11} 2δp|d, δ ∈ {1, 3}, p ∈ {3, 5} 105|d 30|d
(z1, i0) ( 77
15 , 15) (2
δ−15, 2) ( 35
2 , 6) (15, 2)
ℓ
′ 2 2 3 3
n
′
0 z2(7)z2(11) z2(2)z2(5) z2(3)z2(5)z2(7) z2(2)z2(3)z2(5)
n
′
1 z3(5)z3(7) z3(2)z3(3) z3(3)z3(5)z3(7) z3(2)z3(3)z3(5)
n
′
2 2 1
6 1 2 1
6 1

where z2(p) = p 1
p+1 , z3(p) = p
 p−1
2(p+1) . We observe that ∏
ai∈R ai ≥ z|R|−i0
1 (|R|−i0)! with (z1, i0) given
above. Suppose g ∈ {256, 512}, k ≥ k0(g) and k −|R| < g. We see that (9.3.28) and (9.3.29) are valid
for k ≥ k0(g) with h0 = i0, m = √
k0(g), ℓ = ℓ
′, n0 = n
′
0, n1 = n
′
1 and n2 = n
′
2. We ﬁnd that (9.3.29)
is not possible for k ≥ k0(g) + 2 and (9.3.28) is not possible for each k with k0(g) ≤ k < k0(g) + 2.
This is a contradiction. □

Lemma 11.1.3. We have
 |T1| > αk for k ≥ Kα(11.1.6)

where α and Kα are given by
 α .3 .35 .4 .42
Kα 101 203 710 1639

11.2. FURTHER LEMMAS 107

Proof. Let k ≥ Kα. Thus k ≥ 101. From Theorem 1.5.1, we have n + (k − 1)d > 4k2. We see
from (9.4.1) that

|T1| + πd(k) >k − 1 − (k − 1) log k
2 log 2k = k
2 + 1
2
 { (k − 1) log 2
log 2k − 1} > k
2 .

Therefore n + (k − 1)d > ( k
2 log k
2 )
2 by Lemma 3.1.2 (v).
For 0 < β < 1, let
 n + (k − 1)d > (βk log βk)
2.(11.1.7)

We may assume that β ≥ 1
2 . Put Xβ = Xβ(k) = β log(βk). Then log(n+(k−1)d) > 2 log Xβ+2 log k.
From (9.4.1), we see that

|T1| + πd(k) >k − 1 − (k − 1) log k
2 log Xβ + 2 log k = k
2
 (1 − 1
k
 ) (
1 + log Xβ
log Xβ + log k
 )

= k
2
 (1 − 1
k
 ) (

1 + 1
1 + log k
log Xβ
 )
 =: gβ(k)k =: gβk.
(11.1.8)

By using πd(k) ≤ π(k) and Lemma 3.1.2 (i), we get from (11.1.8) that

|T1| > gβk − k
log k
 (1 + 1.2762
log k
 ) .(11.1.9)

Let β = 1
2 . We observe that

14
13 log k − (1 + log k
log Xβ
 ) (
1 + 1.2762
log k
 ) = ( 14
13 − 1
log Xβ
 ) log k − ( 1.2762
log k + 1.2762
log Xβ
 ) − 1

is an increasing function of k and it is positive at k = 2500. Therefore

1
1 + log k
log Xβ > 13
14 1
log k
 (1 + 1.2762
log k
 ) for k ≥ 2500

which, together with (11.1.9) and (11.1.8), implies

|T1|
k > 1
2 − 1
2k − 1
28 log k
 (1 + 1.2762
log k
 ) (
15 + 13
k
 ) > .42 for k ≥ 2500

since the middle expression is an increasing function of k. Thus we may suppose that k < 2500.
From (11.1.8), we get |T1| + πd(k) > g 1
2 k =: β1k. Then (11.1.7) is valid with β replaced by β1 and
we get from (11.1.8) that |T1| + πd(k) > gβ1k =: β2k. We iterate this process with β replaced by
β2 to get gβ2 =: β3 and further with β3 to get |T1| + πd(k) > gβ3k =: β4k. Finally we see that
|T1| > β4k − π(k) ≥ αk for k ≥ Kα. □

11.2. Further Lemmas

We observe that (9.3.24) is satisﬁed when k ≥ 11 by Theorem 1.5.1. We shall use it without
reference in this section.

Lemma 11.2.1. Let d be odd and p, q be primes dividing d. Let ω(d) ≤ 4 and k ≤ 821. Assume
that gp,q(r) ≤ 2r−ω(d) for r = 5, 6. Then (2.1.1) with k ≥ 101 has no solution.

Proof. Suppose equation (2.1.1) has a solution. Let r = 5 if 101 ≤ k < 257 and r = 6 if
257 ≤ k ≤ 821. From (9.2.9), ν(ai) ≤ 2ω(d) and (9.2.1), we get k − F ′(k, r) ≤ ξr ≤ 2ω(d)gp,q ≤ 2r.
We ﬁnd k − F ′(k, r) > 2r by computation. This is a contradiction. □

Lemma 11.2.2. Equation (2.1.1) with k ≥ 101 and ω(d) ≤ 4 is not possible.

108 11. PROOF OF THEOREMS 2.3.1, 2.4.1, 2.5.1, 2.5.2, 2.5.3

Proof. We may assume that k is prime by Lemma 9.1.1. Let d be even. For k − |R| ≥
h(5) = 4(2
ω(d)−θ − 1) + 1, we get from Corollary 9.3.10 with z0 = 5 that n + (k − 1)d < 3
Q k3 with
Q = 32 if 2||d and 16 if 4|d. Let ω(d) ≤ 3. Since k − |R| ≥ h(5) by Lemma 11.1.2 (ii), (iii), (iv) and
|S1| ≥ |T1|
2ω(d)−θ ≥ .3k
23−θ by Lemma 11.1.3, we get 3
Q k3 > n + (k − 1)d > 2δ( .3k
23−θ − 1)k2, a contradiction.

Thus ω(d) = 4. Let k ≥ 710. Then k − |R| ≥ h(5) by Lemma 11.1.2 and |S1| ≥ |T1|
2ω(d)−θ ≥ .4k
24−θ by
Lemma 11.1.3. Hence we get 3
Q > n + (k − 1)d > 2δ( .4k
24−θ − 1)k2, a contradiction again. Therefore
k < 710. By Lemma 11.1.2, we get k − |R| ≥ h(3) implying d < 3
16 k2 if 2||d and d < 3
4 k2 if 4|d
by Corollary 9.3.10 with z0 = 3. However d ≥ 2δ · 53 · 59 · 61 by Lemma 11.1.1 (c). This is a
contradiction.
Thus d is odd. Suppose |S1| ≤ |T1| − h(3). By Lemma 9.3.12, we have

d < ρ
48 k2, n + (k − 1)d < ρ
48 k3.(11.2.1)

Let k ≥ 710. Since ν(ai) ≤ 2ω(d), we derive from Lemma 11.1.3 that |S1| ≥ |T1|
2ω(d) > .4k
16 = .025k.
Therefore max
Ai∈S1Ai > ρ(.025k−1) giving n+(k−1)d > ρ(.025k−1)k2 which contradicts (11.2.1). Thus

k < 710. We see from Lemma 11.1.3 that |T1| > .3k. For ω(d) ≤ 3, we have max
Ai∈S1Ai > ρ( .3k
8 − 1)

giving n + (k − 1)d > ρ( .3k
8 − 1)k2 which contradicts (11.2.1). Let ω(d) = 4. By Lemma 11.1.1 (a),
we see that d ≥min(3 · 53 · 59 · 61, 23 · 29 · 31 · 37) > 3
48 k2 contradicting (11.2.1).
Hence |S1| ≥ |T1| − h(3) + 1. Therefore

n + (k − 1)d ≥ ρ(|T1| − h(3))k2.(11.2.2)

Let k − |R| ≥ h(5). By Corollary 9.3.10 with z0 = 5, we get n + (k − 1)d < 3
16 k3 which, together
with |T1| ≥ .3k by Lemma 11.1.3, contradicts (11.2.2) when ω(d) ≤ 2. Further k ≤ 133, 275 when
ω(d) = 3, 4, respectively. Thus either
 k − |R| < h(5)(11.2.3)

or
 ω(d) > 2; k ≤ 131 if ω(d) = 3; k ≤ 271 if ω(d) = 4.(11.2.4)

We now apply Lemma 11.1.2 (i) to get ω(d) ≥ 2 and k ≤ 293, 487, 991 for ω(d) = 2, 3, 4, respectively.
Let 3|d. Then we have from Lemma 11.1.2 (v) that ω(d) > 2 and k ≤ 131, 350 when ω(d) = 3, 4,

respectively. By Lemma 11.1.1, we get p2 ≥ 53 and hence 53 ≤ p2 ≤ ( d
3 ) 1
ω(d)−1 . By Corollary 9.3.10
with z0 = 3 if ω(d) = 3, z0 = 2 if ω(d) = 4 and Lemma 11.1.2 (v), we get d < 3
4 k2 if ω(d) = 3 and
< 3k2 if ω(d) = 4. Therefore 53 ≤ p2 < k
2 < 67 if ω(d) = 3 and 53 ≤ p2 < k 2
3 ≤ 350 2
3 < 53 if
ω(d) = 4. Therefore ω(d) = 3 and 53 ≤ p2 ≤ 61. Now we get a contradiction from Lemma 11.2.1
with (p, q) = (3, p2) and (9.2.15).
Thus we may assume that 3 ∤ d. Therefore k ≤ 293, 487, 991 for ω(d) = 2, 3, 4, respectively,
as stated above. Let ω(d) = 4 and k < 308. From k − |R| ≥ 9 by Lemma 11.1.2 (i) and by
Corollary 9.3.11, there exists a partition (d1, d2) of d such that max(d1, d2) < (k − 1)
2. Thus p1p2 ≤
max(d1, d2) < (k−1)
2 giving p1 < k−1. By taking r = 5 for 101 ≤ k < 251, r = 6 for 251 ≤ k < 308,
we get from (9.2.10) and gp1 ≤ 2r−1 by (9.2.14) with p = p1 that k − |R| ≥ k − F ′(k, r) − 2r−1 ≥ 16.
Now we return to ω(d) = 2, 3, 4. By Lemma 11.1.2 (i), we get k − |R| ≥ 2ω(d). Then we see from
Corollary 9.3.10 with z0 = 2 that there is a partition (d1, d2) of d with d1 < k −1, d2 < 4(k −1). Thus
p1 < k. We take r = 5 for 101 ≤ k < 211 and r = 6 for 211 ≤ k < 556 for the next computation
and we use Lemma 11.1.2 (i) for k ≥ 556. From (9.2.10) with p = q = p1 and (9.2.14) with p = p1,
and since ∑

p|d,p>pr σp − gp1 ≥ 2 − 2r−1 if p1 > pr and ≥ −2r−2 if p1 ≤ pr, we get

k − |R| ≥ k − F ′(k, r) + 2 − 2r−1 ≥
 




20 for k ≥ 101
29 for k ≥ 211
33 for k ≥ 251.
(11.2.5)
 11.2. FURTHER LEMMAS 109

Therefore we get from (11.2.3), (11.2.4) that ω(d) > 2 and k ≤ 199, 991 when ω(d) = 3, 4, respec-
tively.
Let ω(d) = 3. By Corollary 9.3.10 with z0 = 3, there is a partition (d1, d2) with d1 < k−1
2
and d2 < 2(k − 1). Thus p1p2 ≤max(d1, d2) < 2(k − 1) giving p1 < √2(k − 1) ≤ √2 · 198 and
hence p1 ≤ 19. Further the possibility p1 = 19 is excluded since 19 · 23 > 2(k − 1). Also p2 ≤
79, 53, 31, 29, 23 for p1 = 5, 7, 11, 13, 17, respectively. Now we apply Lemma 11.1.1 (a) to derive that
either p1 = 5, 53 ≤ p2 ≤ 79 or p1 = 7, p2 = 53. Further from 5 · 53 < 2(k − 1), we get k ≥ 134. Thus
k − |R| ≤ 28 by (11.2.3) and (11.2.4). Now we take r = 6 for 134 ≤ k ≤ 199 in the next computation.
We get from (9.2.10) and (9.2.15) with (p, q) = (p1, p2) that k − |R| ≥ k − F ′(k, r) − 2r−2 ≥ 29. This
is a contradiction.
Let ω(d) = 4. By Lemma 11.1.1 (a), (b), we get d ≥min(5·53·59·61, 23·47·53·59, 31·41·47·53) =
953735. Further by Corollary 9.3.10 with z0 = 2 if k < 251, z0 = 3 if k ≥ 251 and (11.2.5), we
obtain d < 3k2 if k < 251 and d < 3
4 k2 for k ≥ 251. This is a contradiction since k ≤ 991. □

Lemma 11.2.3. Assume (2.1.1) with ω(d) ≥ 12. Suppose that

d < 3
16 k2, n + (k − 1)d < 3
16 k3.(11.2.6)

Then k < ω(d)4
ω(d).

Proof. Assume that k ≥ ω(d)4
ω(d). Then from 40 · ( 3
16 ) 2
11 < (12) 7
11 2 36
11 and ω(d) ≥ 12, we get
( 3k2
16 ) 2
11 ≤ k
40·2ω(d) . This together with q1q2 ≤ ( d
2δθ ) 2
ω(d)−θ < ( 3k2
16 ) 2
11 by (9.1.10) and (11.2.6) gives

q1q2 < k
40·2ω(d) . Hence we derive from Corollary 9.3.7 (ii) with d′ = q1q2 that

ν(Ai) ≤ 2ω(d)−2−θ whenever Ai ≥ k
40 · 2ω(d) .(11.2.7)

Let
 T (1) = {i ∈ T1 : Ai > 2δρk
6 · 2ω(d) }, T (2) = T1 \ T (1)(11.2.8)

and
 S(1) = {Ai : i ∈ T (1)}, S(2) = {Ai : i ∈ T (2)}.(11.2.9)

Then considering residue classes modulo 2
δρ, we derive that

2δρk
6 · 2ω(d) ≥ max
Ai∈S(2)Ai ≥ 2δρ(|S(2)| − 1) + 1

so that |S(2)| ≤ k
6·2ω(d) + 1 ≤ k
6·2ω(d) + 1. We have from (11.2.8), (11.2.9) and (11.2.7) together with
ν(Ai) ≤ 2ω(d) by Corollary 9.3.7 (ii) that

|T (2)| ≤ k
40 · 2ω(d) 2ω(d) + ( k
6 · 2ω(d) − k
40 · 2ω(d) + 1) 2ω(d)−2

≤ k
40 + 1
4
 ( k
6 − k
40
 ) + 2ω(d)−2 ≤ k
24 + 3k
160 + k
480 = k
16

since k ≥ ω(d)4
ω(d) and ω(d) ≥ 12. By Lemma 11.1.3 and k > 1639, we have

|T (1)| > |T1| − |T (2)| ≥ .42k − k
16 = .3575k.

Let C, Cµ be as in Lemma 9.4.7 with c = 2. Then .3575k < |T (1)| = |S(1)| + ∑

µ≥2(µ −
1)|Cµ| ≤ |S(1)| + C ≤ |S(1)| + 3 log 2
16 ω(d)4
ω(d) by Lemma 9.4.7. Now we use 3 log 2
16 < 1
7.6 to get
.3575k < |S(1)| + k
7.6 implying |S(1)| > 0.2259k. Therefore n + (k − 1)d ≥ ( max
Ai∈S(1)Ai)k2 ≥ 0.2259k3

contradicting (11.2.6). □

Lemma 11.2.4. Assume (2.1.1) with ω(d) ≥ 5. Then there is no non-degenerate double pair.

110 11. PROOF OF THEOREMS 2.3.1, 2.4.1, 2.5.1, 2.5.2, 2.5.3

Proof. Assume (2.1.1) with ω(d) ≥ 5. Further we suppose that there exists a non-degenerate
double pair. Then we derive from Lemma 9.3.4 with z0 = 2 that

d < X0k2, n + (k − 1)d < X0k3(11.2.10)

where
 X0 = 3, 3
2 , 12, 6 if 2 ∤ d, 2||d, 4||d, 8|d, respectively.(11.2.11)

This with d ≥ 2δ ∏ω(d)+1−δ′

i=2 pi implies k2 > 1
6 ∏ω(d)
i=1 pi. Therefore we get from Lemmas 3.1.1 (v)
and 3.1.3 that

log( k
ω(d)2ω(d) ) ≥ ω(d) { log ω(d) + log log ω(d) − 1.076868
2 − log 2 − log ω(d)
ω(d)
 } − log 6
2 .

The right side of the above inequality is an increasing function of ω(d) and hence k > 9ω(d)2
ω(d)

for ω(d) ≥ 12. We ﬁnd from X0k2 > d ≥ 2δ ∏ω(d)+1−δ′

i=2 pi that k > 3.2ω(d)2
ω(d) if ω(d) = 10, 11.
Further k > 2.97ω(d)2
ω(d) if ω(d) = 8, 9 when d is odd. Also k > 2542, 12195 when ω(d) = 8, 9,
respectively if 2||d or 8|d and k > 1271, 6097 when ω(d) = 8, 9, respectively if 4||d.
Suppose k < 1733. Then ω(d) ≤ 8 if 4||d and ω(d) < 8 otherwise. By Lemma 11.1.1 (a), (c),
we get d ≥min(3 · 53 · 59 · 61 · 67, 23 · 29 · 31 · 37 · 41) if d is odd and d ≥ 2δ · 53 · 59 · 61 · 67 if d is even.
This is not possible since d < X0k2. Hence k ≥ 1733.
Let d be even and ω(d) = 8, 9. Since k ≥ 1733, we get k − |R| ≥ h(3) by Lemma 11.1.2
(ii), (iii), (iv) implying d < 3
16 k2, 3
4 k2 if 2||d, 4|d, respectively, by Corollary 9.3.10 with z0 = 3.
Therefore k ≥ 2.48ω(d)2
ω(d) if 4||d and k ≥ 3.2ω(d)2
ω(d) otherwise.
Therefore for ω(d) ≥ 8, we have

k ≥
 




2.48ω(d)2
ω(d) if 4||d
2.97ω(d)2
ω(d) if d is odd, ω(d) = 8, 9
3.2ω(d)2
ω(d) otherwise
(11.2.12)

Suppose that |S1| ≤ |T1| − h(3) if d is odd and |S1| ≤ |T1| − h(5) if d is even. We put

X :=
 



 ρ
48 if ord2(d) ≤ 1
1
12 if ord2(d) ≥ 2, 3 ∤ d
3
16 if ord2(d) ≥ 2, 3|d.

Then
 d < X k2, n + (k − 1)d < X k3(11.2.13)

by Lemma 9.3.12. Therefore k < ω(d)4
ω(d) for ω(d) ≥ 12 by Lemma 11.2.3.
Let ω(d) ≥ 19. Then
(

2δ 9∏

i=2 pi
)
 (29)
ω(d)−8−δ′ ≤ d < X k2 < W :=
 { 3
48 ω(d)
2(16)
ω(d) if ord2(d) ≤ 1
3
16 ω(d)
2(16)
ω(d) if ord2(d) ≥ 2.

Therefore
 29
16 <
 


(

64
 9∏

i=3 pi
)−1
 299ω(d)
2



 1
ω(d)
 .

We see that the right hand side of the above inequality is a non-increasing function of ω(d) and
the inequality does not hold at ω(d) = 26. Thus ω(d) ≤ 25. Further we get a contradiction from
2δ ∏ω(d)+1−δ′

i=2 pi ≤ d < W since ω(d) ≥ 19.

11.2. FURTHER LEMMAS 111

Thus ω(d) ≤ 18. We get from (9.1.10) and d < X k2 that

q1 · · · qh < X h
1 :=
 




( ρ
48 ) h
ω(d) k
 2h
ω(d) if d is odd
( ρ
96 ) h
ω(d)−1 k
 2h
ω(d)−1 if 2||d
( 1
12·4θ ) h
ω(d)−θ k
 2h
ω(d)−θ if 4|d, 3 ∤ d
( 3
16·4θ ) h
ω(d)−θ k
 2h
ω(d)−θ if 4|d, 3|d

for 1 ≤ h ≤ ω(d) − θ. Further from X k2 > d ≥ 2δp1 · · · pω(d)−δ′, we get

k > k1 :=
 




√ 2δ
X ∏ω(d)+1−δ′
i=2 pi if 3|d
√ 2δ
X ∏ω(d)+2−δ′
i=3 pi if 3 ∤ d.

Thus
 k > k2 := max(1733, k1)(11.2.14)

Further we derive from (11.2.13) that

p1 − 1
2 · · · ph − 1
2 < X h
2 :=
 



 1
2h−1 ( X k2

3·2δ ) h−1
ω(d)−1−δ′ if 3|d

1
2h ( X k2

2δ ) h
ω(d)−δ′ if 3 ∤ d

for 1 ≤ h ≤ ω(d) − δ′.
We take r = [ ω(d)−1
2 ] if d is odd and r = [ ω(d)
2 ]−1 if d is even. By Corollary 9.3.8 and |T1| > .42k
by Lemma 11.1.3, we have

sr+1 ≥ .42k
2ω(d)−r−θ − 2λr − 2r−1λ1 −
 r−1∑

µ=2 2r−µλµ.(11.2.15)

This with Corollary 9.4.4 and q1q2 · · · qh < X h
1 gives (11.2.13) gives

sr+1 ≥ X3 :=
 



 .42k
2ω(d)−r − X r
1
3·2r−3 − ∑r−1
µ=1 2r+2
3 X µ
1
22µ if 2 ∤ d, 3 ∤ d

.42k
2ω(d)−θ−r − X r
1
3·2r−4+δ − 2r−1( X1
2δ + 1) − ∑r−1
µ=2 2r+3−δ
3 X µ
1
22µ if 2|d, 3 ∤ d

.42k
2ω(d)−θ−r − X r
1
9·2r−4+δ′ − 2r−1( X1
3·2δ + 1) − ∑r−1
µ=2 2r+3−δ′

9 X µ
1
22µ if 3|d, 8 ∤ d

.42k
2ω(d)−r − 2( X r
1
24 + 1) − ∑r−1
µ=1 2r−µ( X µ
1
24 + 1) if 8|d, 3|d, r ≤ 3

.42k
2ω(d)−r − X r
1
9·2r−3 − ∑3
µ=1 2r−µ( X µ
1
24 + 1) − ∑r−1
µ=4 2r+2
9 X µ
1
22µ if 8|d, 3|d, r ≥ 4.

By observing that X3−X r
2
k is an increasing function of k and is positive at k = k2 except when
ω(d) = 7, d odd and 3|d in which case it is positive at k = 11500. Let k ≥ 25500 when ω(d) = 7, d
odd and 3|d. Then sr+1 ≥ X3 > X r
2 > p1−1
2 · · · pr−1
2 . Therefore by Lemma 9.4.3 with S = {Ai : i ∈
Tr+1}, |S| = sr+1, h = r and (11.2.13), we get

X k3 > n + (k − 1)d ≥ X4k2 :=
 { 3
4 2r+δX3k2 if 3 ∤ d
9
4 2r+δ−1X3k2 if 3|d.

This is a contradiction by checking that X4
k − X > 0 except when d odd, 3|d and ω(d) = 6, 8, 9.
Thus we may assume that d is odd, 3|d, 6 ≤ ω(d) ≤ 9 and k < 25500 if ω(d) = 7. Also we check
that X4
k − X > 0 for k = 5000, 62000, 350000 according as ω(d) = 6, 8, 9, respectively. Thus we
may assume that k < 5000, 25500, 62000, 350000 whenever ω(d) = 6, 7, 8, 9, respectively. If q1 ≥ 7,
then we get a contradiction from d < X k2 = 1
16 k2 and d
7·9·11·13·17·19 ≥ 1, 23, 23 · 25, 23 · 25 · 29
for ω(d) = 6, 7, 8, 9, respectively. Thus q1 ∈ {3, 5}. Further we get q1 ≤ 5, q2 ≤ 7 if ω(d) = 6,
q1 ≤ 5, q2 ≤ 7, q3 ≤ 11 if ω(d) = 7, 8 and q1 = 3, q2 = 5, q3 = 7 if ω(d) = 9. Thus p1 = 3 and

p2 ∈ {5, 7} if ω(d) = 6, p2, p3 ∈ {5, 7, 11} if ω(d) > 6. Since ( ai
p ) = ( n
p ) for p|d, we consider
Legendre symbols modulo 3, q1, q2 to all squarefree positive integers ≤ q1 and ≤ q1q2 to obtain
λ1 ≤ 1, λ2 ≤ 3. Further for ω(d) > 6, we consider Legendre symbols modulo 3, q1, q2 and q3 if q3 ̸= 9

112 11. PROOF OF THEOREMS 2.3.1, 2.4.1, 2.5.1, 2.5.2, 2.5.3

to all squarefree positive integers ≤ q1q2q3 to get λ3 ≤ 17. Therefore we get from (11.2.15) and
Corollary 9.4.4 that
 sr+1 ≥ X5 :=
 



 .42k
24 − 8 if ω(d) = 6
.42k
2ω(d)−3 − 44 if ω(d) = 7, 8

.42k
25 − 1
9 ( 1
16 ) 4
9 k 8
9 − 54 if ω(d) = 9.

We check that sr+1 ≥ X5 > X r
2 > p1−1
2 · · · pr−1
2 by observing X5−X r
2
k is an increasing function of k
and is positive at k =max(1733, k1). Therefore by Lemma 9.4.3 with h = r and (11.2.13), we get
1
16 k3 > n + (k − 1)d ≥ 9
8 2rX5k2. This is a contradiction since X5
k − 1
18·2r > 0.
Thus |S1| ≥ X6 using |T1| > .42k by Lemma 11.1.3 where X6 = .42k − h(3) + 1 if d is odd and
X6 = .42k − h(5) + 1 if d is even. Since there exists a non-degenerate double pair, we apply Lemma
9.3.4 with z0 = 2 to get a partition (d1, d2) of d with





p1p2 · · · p[ ω(d)+1
2 ] ≤ max(d1, d2) < 4k if 2 ∤ d

p1p2 · · · p[ ω(d)
2 ] ≤ max(d1, d2) < 4k if 2||d

2p1p2 · · · p[ ω(d)
2 ] ≤ max(d1, d2) < 8k if 4|d.

Let ω(d) ≥ 7 + δ′. Then we see from (11.2.12) that |S1| ≥ X6 > k
4 > p1−1
2 · · · p4−1
2 . We now apply
Lemma 9.4.3 with h = 4 to get X0k > n + (k − 1)d ≥ 3
4 24+δX6k2 > 3 · 2δk3 since X6 > k
4 . This
contradicts (11.2.11). Thus ω(d) ≤ 6 + δ′ and k ≥ 1733 by (11.2.12).
Assume that k − |R| ≥ h(3). Then from Corollary 9.3.10 with z0 = 3, we get n + (k − 1)d <
X7k3 where X7 = 3
16 if 2||d and 3
4 otherwise. If 2|d or 3|d, then n + (k − 1)d ≥ 3(X6 − 1)k2 if
3|d and n + (k − 1)d ≥ 2δ(X6 − 1)k2 if 2|d contradicting n + (k − 1)d < X7k3. Thus d is odd,
3 ∤ d and ω(d) = 5, 6. By Corollary 9.3.10 with z0 = 3, there is a partition (d1, d2) of d with
p1p2p3 ≤max(d1, d2) < 2(k − 1). Now we get k
4 > p1−1
2 p2−1
2 p3−1
2 . Further we check X6 > k
4
implying |S1| ≥ X6 > p1−1
2 p2−1
2 p3−1
2 . Therefore we derive from Lemma 9.4.3 with h = 3 that
3
4 k3 = X7k3 > n + (k − 1)d ≥ 6X6k2 > 3
2 k3, a contradiction. Hence k − |R| < h(3). By Lemma
11.1.2 (i) − (iv), we get d odd, ω(d) = 6 and 1733 ≤ k < 2082. Further from Lemma 11.1.2 (v), (vi),
we get p1 ≥ 11. Now 11 · 13 · 17 · 19 · 23 · 29 ≤ d < 3k2 by (11.2.10) and (11.2.11). This is a
contradiction. □

Corollary 11.2.5. Equation (2.1.1) with ω(d) ≥ 5 implies that k − |R| < 2ω(d)−θ.

Proof. Assume (2.1.1) with ω(d) ≥ 5 and k −|R| ≥ 2ω(d)−θ. By Lemma 9.3.9, there exists a set
Ω with at least 2
ω(d)−θ pairs satisfying Property ND. Since there are at most 2ω(d)−θ − 1 permissible
partitions of d by Lemma 9.3.5 (i), we can ﬁnd a partition (d1, d2) of d and a non-degenerate double
pair with respect to (d1, d2). This contradicts Lemma 11.2.4. □

Lemma 11.2.6. Equation (2.1.1) with d odd, k ≥ 101 and 5 ≤ ω(d) ≤ 7 implies that k − |R| ≤
2ω(d)−1.

Proof. Let d be odd. Assume (2.1.1) with 5 ≤ ω(d) ≤ 7 and k − |R| ≥ 2ω(d)−1 + 1. By
Corollary 11.2.5, we may suppose that k − |R| < 2ω(d). Further by Lemma 11.1.2 (i), we obtain
k ≤ 555, 1056, 2099 when ω(d) = 5, 6, 7, respectively. Since k − |R| ≥ 2ω(d)−1 + 1, we derive from
Corollary 9.3.11 that there exists a partition (d1, d2) of d such that D12 :=max(d1, d2) < (k − 1)
2.
Let ω(d) = 5. Then p1p2p3 ≤ D12 < (k − 1)
2 implying p1 ≤ 61 since 67 · 71 · 73 > 5552. Also
p2 < k−1√p1 . By taking r = 6 for 208 < k ≤ 547, we get from (9.2.10) and (9.2.14) with p = p1

that k − |R| ≥ k − F ′(k, r) + min(−2r−2, σ61 − 2r−1) ≥ 32 if k > 208. Thus k ≤ 208. Further
p1 ≤ 29 since 31 · 37 · 41 > 2082. If p1 ≥ 17, then we obtain from Lemma 11.1.1 (a), (b) that
2072 > D12 ≥min(17 · 53 · 59, 23 · 47 · 53), a contradiction. Therefore p1 ≤ 13 and hence 53 ≤ p2 < k
by Lemma 11.1.1 (a). By taking r = 6, we get from (9.2.15) with (p, q) = (p1, p2) that gp1,p2 = 2
r−3

if k ≤ 127 and gp1 = 2r−2 if k > 127 by (9.2.14) with p = p1. From (9.2.10) and σp2 ≥ 2, we have

11.2. FURTHER LEMMAS 113

k − |R| ≥ k − F ′(k, r) + 2 − 2r−3 if k ≤ 127 and k − |R| ≥ k − F ′(k, r) + 2 − 2r−2 if k > 127 giving
k − |R| ≥ 32, a contradiction.
Let ω(d) = 6. Then p2p3p4 ≤ D12 < (k − 1)
2 implying p1 < p2 ≤ 97 since 101 · 103 · 107 > 10552.
By taking r = 7 for 384 < k ≤ 1039, we get from (9.2.10) and (9.2.15) with (p, q) = (p1, p2) that
k − |R| ≥ k − F ′(k, r) − 2r−2 ≥ 64 if k > 384. Thus k ≤ 384. Further p2 ≤ 43 since 47 · 53 · 59 > 3832.
Then we derive from Lemma 11.1.1 (a), (b) that p1 = 31, p2 = 41, p3 ≥ 47. Also k > 319 since
41 · 47 · 53 > 3192. By taking r = 7 for 319 < k ≤ 384, we obtain from (9.2.10) and (9.2.15) with
(p, q) = (31, 41) that k − |R| ≥ k − F ′(k, r) + σ31 + σ41 − 2r−2 ≥ 64. This is a contradiction.
Let ω(d) = 7. Suppose p1 ≤ 19. By Lemma 11.1.2 (v), (vi), vii), we get k < 735, 930, 1200
according as p1 = 3, p1 ∈ {5, 7}, p1 ≥ 11, respectively. By Lemma 11.1.1 (a), we obtain p2 ≥ 53.
Now 53 · 59 · 61 ≤ D12
p1 < 7352
3 , 9302
5 , 12002
11 according as p1 = 3, p1 ∈ {5, 7}, p1 ≥ 11, respectively. This
is not possible. Thus p1 ≥ 23. Further p1 ≤ 41, p2 ≤ 53 from p1p2p3p4 ≤ D12 < (k − 1)
2 ≤ 20982.
By taking r = 9, we get from (9.2.10) and (9.2.15) with (p, q) = (p1, p2) that k − |R| ≥ k −
F ′(k, r) + min(−2r−3 + σ53, −2r−2 + σ41 + σ53) ≥ 128 for k > 1007. Therefore k ≤ 1007. Now
10072 > D12 ≥min(23 · 47 · 53 · 59, 31 · 41 · 47 · 53) by Lemma 11.1.1 (b). This is not possible. □

Corollary 11.2.7. Assume (2.1.1) with ω(d) ≥ 5. Then k < 308, 556, 1057, 2870 and 2(ω(d) −
θ)2
ω(d)−θ for ω(d) = 5, 6, 7, 8 and ≥ 9, respectively. In particular k < 2ω(d)2
ω(d).

Proof. By Corollary 11.2.5 and Lemma 11.2.6, we derive that k − |R| < 2ω(d)−θ and k − |R| ≤
2ω(d)−1 if d is odd, 5 ≤ ω(d) ≤ 7. By Lemma 11.1.2 (i), (ii), we get k < 2(ω(d) − θ)2
ω(d)−θ for
ω(d) ≥ 9 + θ, k < 4252 if ω(d) = 8 and k < 308, 556, 1057 according as ω(d) = 5, 6, 7, respectively.
Now it remains to consider ω(d) = 9 if 2||d, 4||d and ω(d) = 8. By Lemma 11.1.2 (ii), it suﬃces
to consider d odd and ω(d) = 8. Further k < 4252 and k − |R| < 256. Suppose k ≥ 2870. Then
k − |R| ≥ 129 by Lemma 11.1.2 (i) and we derive from Corollary 9.3.11 that there exists a partition
(d1, d2) of d with max(d1, d2) < (k − 1)
2. Let p1 ≥ 53. Then 42524 > d ≥ 53 · 59 · 61 · 67 · 71 · 73 · 79 · 83,
a contradiction. Thus p1 ≤ 47. Now we obtain from Lemma 11.1.2 (vi) that k − |R| ≥ 256, a
contradiction. □

Lemma 11.2.8. (i) Let d be odd and ω(d) = 5, 6. Suppose that d is divisible by a prime ≤ k
when ω(d) = 5. Further assume that there exist distinct primes p and q with pq|d, p ≤ 19, q ≤ k
when ω(d) = 6. Then (2.1.1) with k ≥ 101 has no solution.
(ii) Let d be even and 5 ≤ ω(d) ≤ 6 + θ. Assume that p|d with p ≤ 47 when ω(d) = 7. Then (2.1.1)
with k ≥ 101 has no solution.

Proof. By Lemma 11.2.5, we may suppose that k − |R| < 2ω(d)−θ.
(i) Let d be odd. From Corollary 11.2.7, we get k < 308, 556 when ω(d) = 5, 6, respectively. Let
ω(d) = 5. By taking r = 5 for 101 ≤ k < 308, we get from (9.2.10) and (9.2.14) with p = p1 that
k − |R| ≥ k − F ′(k, r) − 2r−1 ≥ 17 which is not possible by Lemma 11.2.6.
Let ω(d) = 6. Then 53 ≤ p2 ≤ k by Lemma 11.1.1 (a). We take r = 6. Let p1 ≤ 13. Then
we get from (9.2.15) with (p, q) = (p1, p2) that gp1,p2 = 2
r−3 if k ≤ 127 and gp1 = 2
r−2 if k > 127
by (9.2.14) with p = p1. From (9.2.10) and σp2 ≥ 1, we have k − |R| ≥ k − F ′(k, r) + 1 − 2r−3 if
k ≤ 127 and k − |R| ≥ k − F ′(k, r) + 1 − 2r−2 if k > 127 giving k − |R| ≥ 33. This contradicts
Lemma 11.2.6. Thus p1 ∈ {17, 19}. We get from (9.2.15) with (p, q) = (p1, p2) that gp1,p2 = 2r−2 if
k ≤ 193 and gp1 = 2
r−1 if k > 193 by (9.2.14) with p = p1. From (9.2.10) and σp1 + σp2 ≥ σ19 + 1,
we get k − |R| ≥ 33, a contradiction.
(ii) Let d be even. Then from Lemma 11.1.2 (ii), (iii), (iv), we get ω(d) = 6, k < 252 and
ω(d) = 7, k < 430 if 2||d; ω(d) = 6, k < 127 and ω(d) = 7, k < 303 if 4||d; ω(d) = 6, k < 220 if 8|d.
By Lemma 11.1.1, we obtain ω(d) = 6, k < 252 and p1 ≥ 53. Further by Lemma 11.1.2, we get
k − |R| ≥ 2ω(d)−θ−1 + 1. This with Corollary 9.3.11 gives max(d1, d2) < (k − 1)
2 for some partition
(d1, d2) of d. Since max(d1, d2) ≥ p1p2p3 ≥ 533 > 4302, we get a contradiction. □

Lemma 11.2.9. Equation (2.1.1) with k ≥ 101 implies that d > 1010.

114 11. PROOF OF THEOREMS 2.3.1, 2.4.1, 2.5.1, 2.5.2, 2.5.3

Proof. Assume (2.1.1) with k ≥ 101 and d ≤ 1010. By Lemma 11.2.2, we have ω(d) ≥ 5.
Further we obtain from Corollary 11.2.5 that k − |R| < 2ω(d)−θ which we use without reference in
the proof.
Let d be odd. Then ω(d) ≤ 9 otherwise d ≥ ∏11
i=2 pi > 1010. By Lemma 11.2.8 (i), we see that
d > k5 > 1010 if ω(d) = 5. Thus ω(d) ≥ 6.
Let ω(d) = 6. If p1 ≤ 19, then d > k5 > 1010 by Lemma 11.2.8 (i). Therefore p1 ≥ 23. Also
p1 ≤ 37 otherwise d ≥ 41 · 43 · 47 · 53 · 59 · 61 > 1010. Further k < 556 by Corollary 11.2.7. Therefore
by Lemma 11.1.1 (b), we obtain d ≥min(23 · 47 · 53 · 59 · 61 · 67, 31 · 41 · 47 · 53 · 59 · 61) > 1010.
Thus ω(d) ≥ 7. Then p1 ≤ 13 otherwise d ≥ ∏13
j=7 pi > 1010. Further k ≥ 1733 otherwise
d ≥ 3 · 536 > 1010 by Lemma 11.1.1 (a). By Corollary 11.2.7, we obtain ω(d) ≥ 8.
Let ω(d) = 8. Then p1 ≤ 7. Now Lemma 11.1.2 (v), (vi) gives p1 ∈ {5, 7}. Further p2 ≤ 11
since 5 ∏12
j=6 pi > 1010. This is not possible by Lemma 11.1.2 (vii) since k ≥ 1733.
Let ω(d) = 9. Then p1 = 3, p2 = 5 and p3 = 7. This is not possible by Lemma 11.1.2 (vii) since
k ≥ 1733.
Let d be even. Then ω(d) ≤ 10 otherwise d ≥ ∏11
i=1 pi > 1010. Further ω(d) ≤ 9 for 4|d since
4 ∏10
i=2 pi > 1010. By Lemma 11.2.8 (ii), we have ω(d) ≥ 7. Further k ≥ 1801 by Lemma 11.1.1 (c)
since 2 ∏21
i=16 pi > 1010. Now we use Lemma 11.1.2 (ii), (iii), (iv) to obtain either 2||d, ω(d) = 9, 10
or 8|d, ω(d) = 9.
Let 2||d. Let ω(d) = 9. Then p1 ≤ 5 otherwise d ≥ 2 ∏11
i=4 pi > 1010. Then k − |R| ≥ 256 by
Lemma 11.1.2 (vii), a contradiction. Let ω(d) = 10. Then p1 = 3, p2 = 5 and hence k − |R| ≥ 512
by Lemma 11.1.2 (vii). This is not possible.
Let 8|d and ω(d) = 9. Then p1 ≤ 5 since 8 ∏11
i=4 pi > 1010. By Lemma 11.1.2, we get k − |R| ≥
512 which is a contradiction. □

11.3. Proof of Theorem 2.5.2

Suppose that (2.1.1) with b = 1 has a solution. By Theorem 2.1.1, Lemmas 11.2.2, 11.2.6
and Corollary 11.2.7, we get ω(d) = 5, d odd, k − |R| ≤ 16 and 110 ≤ k < 308. We ob-
serve that ordp(a0a1 · · · ak−1) is even for each prime p. Therefore the number of i’s for which
ai are divisible by p is at most σ′
p = ⌈ k
p ⌉ or ⌈ k
p ⌉ − 1 according as ⌈ k
p ⌉ is even or odd, respec-

tively. Let r = 4. Then from (9.2.3), we get k − |R| ≥ k − F (k, r) − 2r ≥ k − ∑

p>prσ′
p − 2r

which is ≥ 17 except at k = 110, 112, 114, 116, 118, 120, 122, 124 where k − |R| ≥ 16. Therefore
k = 110, 112, 114, 116, 118, 120, 122, 124 and k − |R| = 16. Further we may assume that for each
prime 11 ≤ p ≤ k, there are exactly σ′
p number of i’s for which p|ai and for any i, pq ∤ ai when-
ever 11 ≤ q ≤ k, q ̸= p. By considering the i’s for which ai’s are divisible by primes 109, 107
when k = 110; 37, 109, 107 when k = 112; 113, 37, 109, 107 when k = 114; 23, 113, 37, 109, 107
when k = 116; 13, 23, 113, 37, 109, 107 when k = 118; 17, 13, 23, 113, 37, 109, 107 when k = 120;
11, 17, 13, 23, 113, 37, 109, 107 when k = 122 and 41, 11, 17, 13, 23, 113, 37, 109, 107 when k = 124, we
get P (aςk aςk+1 · · · aςk+105) ≤ 103 where ςk = 2 + k−110
2 . This is excluded. For instance let k = 124.
Then P (a9a10 · · · a114) ≤ 103. This gives 1032|ajaj+103 for j ∈ {9, 10, 11}. Let 103
2|a9a112. Then
1012|ajaj+101 for j ∈ {10, 12, 13} so that P (a14a15 · · · a110) ≤ 97. This is excluded by considering
by Theorem 10.1.1 with k = 97. If 103
2|a1a114, we obtain similarly that P (a13a14 · · · a109) ≤ 97 and
it is excluded. Thus 1032|a10a113. If 1012|ajaj+101 for j ∈ {11, 13}, we get P (a14a15 · · · a110) ≤ 97
and is excluded. Hence 1012|a9a110 implying P (a11a12 · · · a107) ≤ 97 and it is excluded again. □

11.4. Proof of Theorem 2.5.3

By Theorem 10.1.1 and Lemmas 11.2.2, 11.2.8 (ii), we may suppose that d is odd, either
ω(d) = 3, (a0, a1, · · · , ak−1) ∈ S2 or ω(d) ≤ 2, (a0, a1, · · · , ak−1) ∈ S1 ∪ S2, (a0, a1, · · · , a7) ̸=

(3, 1, 5, 6, 7, 2, 1, 10) or its mirror image when k = 8, ω(d) = 2. For p|d, we observe from ( q
p ) = 1 for

q ∈ {2, 3, 5, 7} that p ≥ 311 and therefore d ≥ 311ω(d). Further we observe from Theorem 1.5.1 that
(9.3.24) is valid.
 11.4. PROOF OF THEOREM 2.5.3 115

Let ω(d) = 1. If k − |R| ≥ 2, we get d = d2 < 4(k − 1) by Corollary 9.3.10 with z0 =
2, a contradiction since d ≥ 311. Therefore it remains to consider k = 8 and (a0, · · · , a7) =
(3, 1, 5, 6, 7, 2, 1, 10) or its mirror image. We exclude the possibility (a0, · · · , a7) = (3, 1, 5, 6, 7, 2,
1, 10) and the proof for excluding its mirror image is similar. We write

n = 3x
2
0, n + d = x
2
1, n + 2d = 5x
2
2, n + 3d = 6x
2
3,

n + 4d = 7x
2
4, n + 5d = 2x
2
5, n + 6d = x
2
6, n + 7d = 10x
2
7.

Then we get 5d = x
2
6 − x
2
1 = (x6 − x1)(x6 + x1) implying either x6 − x1 = 1, x6 + x1 = 5d
or x6 − x1 = 5, x6 + x1 = d. We apply Runge’s method to arrive at a contradiction. Suppose
x6 − x1 = 1, x6 + x1 = 5d. Then 5d = 2x1 + 1 and x1 ≥ 14. We obtain (125 · 6x0x3x5)
2 = (25(n +
d)−25d)(25(n+d)+50d)(25(n+d)+100d) = (25x
2
1 −10x1 −5)(25x
2
1 +20x1 +10)(25x
2
1 +40x1 +20) =
15625x
6
1 + 31250x
5
1 + 20625x
4
1 − 3000x
3
1 − 10750x
2
1 − 6000x1 − 1000 =: ˜E(x1). We see that

(125x
3
1 + 125x
2
1 + 20x1 − 32)
2 > ˜E(x1) > (125x
3
1 + 125x
2
1 + 20x1 − 33)
2.

This is a contradiction. Let x6 − x1 = 5, x6 + x1 = d. Then we argue as above to conclude that
d = 2x1 + 5, x1 ≥ 66 and

(x
3
1 + 5x
2
1 + 4x1 − 32)
2 > ˜E1(x1) > (x
3
1 + 5x
2
1 + 4x1 − 33)
2

where ˜E1(x1) = x
6
1 + 10x
5
1 + 33x
4
1 − 24x
3
1 − 430x
2
1 − 1200x1 − 1000 is a square. This is again not
possible.
Thus ω(d) ≥ 2. Let k ≥ 13 and (a0, a1, · · · , a12) ̸= (3, 1, 5, 6, 7, 2, 1, 10, 11, 3, 13, 14, 15) or its
mirror image when k = 13. Let g = 3, 4, 5 if k = 13, 14, ≥ 19, respectively. Then from ν(1) = 3
and Lemma 9.3.9, we get a set Ω of pairs (i, j) with |Ω| ≥ k − |R| + r3 ≥ g having Property ND.
Therefore there exists a non-degenerate double pair for k ≥ 14 when ω(d) = 2. Further there are
distinct pairs corresponding to partitions (d1, d2), (d2, d1) for some divisor d1 of d for k ≥ 13 when
ω(d) = 2 and for k ≥ 19 when ω(d) = 3.
Suppose that there is a non-degenerate double pair. Then we get from Lemma 9.3.4 with z0 = 2
that d < 3k2 ≤ 3 · 242 contradicting d ≥ 3112. Thus there is no non-degenerate double pair
corresponding to any partition. Again, if there are pairs (i, j), (g, h) corresponding to partitions
(d1, d2), (d2, d1) for some divisor d1 of d, then we derive from Lemma 9.3.3 that d < (k − 1)
4. This
is not possible since 311
2 ≤ d < 124 when ω(d) = 2 and 311
3 ≤ d < 234 when ω(d) = 3. Therefore
there are no distinct pairs corresponding to partitions (d1, d2), (d2, d1) for any divisor d1 of d. Thus
it remains to consider k = 14 when ω(d) = 3 and either k = 8, 9 or k = 13, (a0, a1, · · · , a12) =
(3, 1, 5, 6, 7, 2, 1, 10, 11, 3, 13, 14, 15) or its mirror image when ω(d) = 2. Also we may suppose that
there is a pair (i, j) with ai = aj corresponding to the partition (1, d) for each of these possibilities.
Let k = 8 and ω(d) = 2. We exclude the possibility (a0, a1, · · · , a7) = (2, 3, 1, 5, 6, 7, 2, 1)
and the proof for excluding its mirror image is similar. We see that either the pair (0, 6) or (2, 7)
corresponds to (1, d) and we arrive at a contradiction as in the case k = 8, ω(d) = 1 and (a0, · · · , a7) =
(3, 1, 5, 6, 7, 2, 1, 10). Let the pair (0, 6) corresponds to (1, d). Then either x6 −x0 = 1, x6 +x0 = 3d or
x6−x0 = 3, x6+x0 = d. Suppose x6−x0 = 1, x6+x0 = 3d. Then we obtain 3d = 2x0+1, x0 ≥ 100 and
(3x2x7)
2 = (3n+6d)(3n+21d) = (6x
2
0+4x0+2)(6x
2
0+14x0+7) = 36x
4
0+108x
3
0+110x
2
0+56x0+14 :=
ψ2(x0) is a square. This is a contradiction since (6x
2
0 + 9x0 + 3)2 > ψ2(x0) > (6x
2
0 + 9x0 + 2)2.
Let x6 − x0 = 3, x6 + x0 = d. Then we argue as above to conclude that d = 2x0 + 3, x0 ≥ 100
and 4x
4
0 + 36x
3
0 + 11x
2
0 + 168x0 + 126 := ˜E3(x0) is a square. This is again not possible since
(2x
2
0 + 9x0 + 8)
2 > ˜E3(x0) > (2x
2
0 + 9x0 + 7)
2. The other possibility of the pair (2, 7) corresponding
to (1, d) is excluded similarly.
Let k = 9 and ω(d) = 2. Then (2.1.1) holds with k = 8 and (a0, · · · , a7) = (2, 3, 1, 5, 6, 7, 2, 1)
or its mirror image. This is already excluded. The case k = 13, ω(d) = 2 and (a0, · · · , a12) =
(3, 1, 5, 6, 7, 2, 1, 10, 11, 3, 13,
14, 15) or its mirror image is excluded as above in the case k = 8.
Let k = 14 and ω(d) = 3. Let (a0, · · · , a13) = (3, 1, 5, 6, 7, 2, 1, 10, 11, 3, 13, 14, 15, 1). Then one
of the pairs (0, 9), (1, 6), (1, 13), (6, 13) corresponds to the partition (1, d). This is excluded as above in

116 11. PROOF OF THEOREMS 2.3.1, 2.4.1, 2.5.1, 2.5.2, 2.5.3

the case k = 8, ω(d) = 2. The proof for excluding the mirror image (1, 15, 14, 13, 3, 11, 10, 1, 2, 7, 6, 5, 1, 3)
is similar. □

11.5. Proof of Theorem 2.3.1

Theorem 2.3.1 follow immediately from Theorem 2.5.3 and Lemma 11.2.7. □

11.6. Proof of Theorem 2.4.1

First we show that d > 1010. By Lemma 11.2.9 and Theorem 10.1.1, it suﬃces to consider the
case k = 7 and (a0, a1, · · · , a6) given by

(2, 3, 1, 5, 6, 7, 2), (3, 1, 5, 6, 7, 2, 1), (1, 5, 6, 7, 2, 1, 10)(11.6.1)

or their mirror images. Then for p|d, we have ( q
p ) = 1 for q ∈ {2, 3, 5, 7}. Suppose that d ≤ 1010.

Since ω(d) ≥ 2, we have p1 ≤ 105. For X > 0, let

P0 = P0(X) = {p ≤ X : ( q
p
 ) = 1, q = 2, 3, 5, 7}.

We ﬁnd that that P0(10
5) = {311, 479, 719, 839, 1009, · · · }. Thus p1 ≥ 311 by p1 ∈ P0(10
5). Since
311 · 479 · 719 · 839 > 1010, we have ω(d) ≤ 3. Further from 3112 · 4792 > 1010, we get either
ω(d) = 2, d = p1p2, p2
1p2, p1p2
2 or ω(d) = 3, d = p1p2p3.
Consider (a0, a1, · · · , a6) = (2, 3, 1, 5, 6, 7, 2). From d = n + d − n = 3x
2
1 − 2x
2
0, 3 ∤ x0, 4 ∤ x0x1,
we get d ≡ −2 ≡ 1(mod 3) and d ≡ 3 − 2 ≡ 1(mod 8) giving d ≡ 1(mod 24). Again from
2(x
2
6 − x
2
0) = n + 6d − n = 6d = 6d1d2, we get x6 − x0 = r1d1, x6 + x0 = r2d2 with r1r2 = 3,
r1d1 < r2d2 and (r1d1, r2d2) ∈ D3 with

D3 =
 




{(1, 3q1q2), (3, q1q2), (q1, 3q2), (3q1, q2), (q2, 3q1)} if ω(d) = 2
{(1, 3p1p2p3), (3, p1p2p3), (p1, 3p2p3), (3p1, p2p3),
(p2, 3p1p3), (3p2, p1p3), (p3, 3p1p2), (3p3, p1p2)} if ω(d) = 3.

Then x0 = r2d2−r1d1
2 giving x
2
2 = n+2d = 2x
2
0 +2d1d2 = 1
2 {(r1d1)
2 +(r2d2)
2 −2d1d2} a square. Now
we see from 3x
2
1 = n + d = 2x
2
0 + d = 1
2 {(r1d1)
2 + (r2d2)
2 − 4d1d2} that 1
6 {(r1d1)
2 + (r2d2)
2 − 4d1d2}
is an square. For each d = q1q2, we ﬁrst check for d ≡ 1(mod 24) and restrict to such d. Further for
each possibility of (r1d1, r2d2) ∈ D3 with r1d1 < r2d2, we check for 1
2 {(r1d1)
2+(r2d2)
2−2d1d2} being
a square and restrict to such pairs (r1d1, r2d2). Finally we check that 1
6 {(r1d1)
2 + (r2d2)
2 − 4d1d2} is
not a square. For example, let d = 1319·4919. Then q1 = 1319, q2 = 4919. We check that d ≡ 1(mod
24). For each choice (r1d1, r2d2) ∈ D3 with r1d1 < r2d2, we check for 1
2 {(r1d1)
2 + (r2d2)
2 − 2d1d2}
being a square which is possible only for (r1d1, r2d2) = (1319, 3 · 4919). However we ﬁnd that
1
6 {(r1d1)
2 + (r2d2)
2 − 4d1d2} is not a square for (r1d1, r2d2) = (1319, 3 · 4919).
Next we consider (a0, a1, · · · , a6) = (3, 1, 5, 6, 7, 2, 1). From d = n + 6d − (n + 5d) = x
2
6 − 2x
2
5,
3 ∤ x5, 3|x
2
6 and 2 ∤ x6, 4|x
2
5, we get d ≡ 1(mod 24). Again from x
2
6−x
2
1 = n+6d−(n+d) = 5d = 5d1d2
we get x6 − x1 = r1d1, x6 + x1 = r2d2 with r1r2 = 5, r1d1 < r2d2 and

D5 =
 




{(1, 5q1q2), (5, q1q2), (q1, 5q2), (5q1, q2), (q2, 5q1)} if ω(d) = 2
{(1, 5p1p2p3), (5, p1p2p3), (p1, 5p2p3), (5p1, p2p3),
(p2, 5p1p3), (5p2, p1p3), (p3, 5p1p2), (5p3, p1p2)} if ω(d) = 3.

Thus x6 = r2d2+r1d1
2 giving 2x
2
5 = n + 5d = x
2
6 − d = 1
4 {(r1d1)
2 + (r2d2)
2 + 6d} implying 1
2 {(r1d1)
2 +
(r2d2)
2 + 6d} is a square. Further from 7x
2
4 = n + 4d = n + 6d − 2d = x
2
6 − 2d = 1
4 {(r1d1)
2 +
(r2d2)
2 + 2d1d2}, we get 1
7 {(r1d1)
2 + (r2d2)
2 + 2d1d2} is a square. For each d = q1q2, we ﬁrst
check for d ≡ 1(mod 24) and restrict to such d. Further for each possibility of (r1d1, r2d2) ∈ D5
with r1d1 < r2d2, we check for 1
2 {(r1d1)
2 + (r2d2)
2 + 6d} being a square and restrict to such pairs
(r1d1, r2d2). Finally we check that 1
7 {(r1d1)
2 + (r2d2)
2 + 2d} is not a square. Further the case
(a0, a1, · · · , a6) = (1, 5, 6, 7, 2, 1, 10) is excluded by the preceding test.

11.7. PROOF OF THEOREM 2.5.1 117

The case (a0, a1, · · · , a6) = (2, 7, 6, 5, 1, 3, 2) is similar to (a0, a1, · · · , a6) = (2, 3, 1, 5, 6, 7, 2)
and we obtain d ≡ −1(mod 24), 1
2 {(r1d1)
2 + (r2d2)
2 + 2d} and 1
6 {(r1d1)
2 + (r2d2)
2 + 4d} are
squares for each possibility of (r1d1, r2d2) ∈ D3 with r1d1 < r2d2. This is excluded. The cases
(a0, a1, · · · , a6) = (1, 2, 7, 6, 5, 1, 3), (10, 1, 2, 7,
6, 5, 1) are also similar to that of (a0, a1, · · · , a6) = (3, 1, 5, 6, 7, 2, 1), (1, 5, 6, 7, 2, 1, 10) and is ex-
cluded. Thus d > 1010.
Now we show that d > klog log k. Since klog log k < 1010 for k < 22027, we may assume that k ≥
22027. By Corollary 11.2.7, we obtain ω(d) ≥ 9 and k < 2(ω(d)−θ)2
ω(d)−θ =: Ψ0(ω(d)−θ). Further
we derive from 22027 ≤ k < 2ω(d)2
ω(d) that ω(d) ≥ 11. It suﬃces to show that log d > (log Ψ0(ω(d)−
θ))(log log Ψ0(ω(d) − θ)) =: Ψ1(ω(d) − θ). Let Ψ2(l) = l(log l + log log l − 1.076868) for l > 1. From
d ≥ 2δ ∏ω(d)+1−δ′

i=2 pi and Lemma 3.1.3, we get log d > Ψ2(ω(d) + 1) − log 2, Ψ2(ω(d)) + (δ − 1) log 2
when 2 ∤ d, 2|d, respectively. It suﬃces to check for ω(d) ≥ 11 that Ψ2(ω(d)+1)−log 2−Ψ1(ω(d)) > 0
if 2 ∤ d, Ψ2(ω(d)) − Ψ1(ω(d) − 1) > 0 if 2||d, 4||d and Ψ2(ω(d)) + log 4 − Ψ1(ω(d)) > 0 if 8|d. This is
the case. □

11.7. Proof of Theorem 2.5.1

Suppose Theorem 2.5.1 is not true. Then (2.1.1) is valid with k ≥ 8, b = 1 and ω(d) = 2 but n
and d are not necessarily coprime. Let n′ = n
gcd(n,d) and d′ = d
gcd(n,d) . Now, by dividing gcd(n, d)
k

on both sides of (2.1.1), we have

(11.7.1) n′(n′ + d′) · · · (n′ + (k − 1)d′) = pδ1
1 pδ2
2 y2
1
where y1 > 0 is an integer and δ1, δ2 ∈ {0, 1}. We may assume that k is odd and (δ1, δ2) ̸= (0, 0) by
Theorem 2.5.2 with ω(d) = 2. Let d′ = 1. Then we see from (1.2.3) for k ̸= 13, 17 and Corollary
1.2.3 for k = 13, 17 that the left hand side of (11.7.1) is divisible by at least three primes > k.
Therefore there exists a prime p with p ̸= p1, p ̸= p2, p > k such that it divides a term on the left
hand side of (11.7.1) to power at least 2. This implies n′ > k2. Now we see from [47, Theorem
2] that the left hand side of (11.7.1) is divisible by at least three primes > k to odd powers. This
contradicts (11.7.1). Thus d′ > 1 implying (δ1, δ2) ̸= (1, 1) by gcd(n′, d′) = 1. Now we may assume
that (δ1, δ2) = (1, 0). Then d′ is a power of p2. Further we may suppose that p1 ≥ k by Theorem
2.5.3. Let n + i0d with 0 ≤ i0 < k be the term divisible by p1 on the left hand side of (11.7.1). Then

n′ · · · (n′ + (i0 − 1)d′)(n′ + (i0 + 1)d′) · · · (n′ + (k − 1)d′) = b′y2
2
where P (b′) < k and y2 > 0 is an integer. Now k = 8 by [46, Theorem 1]. This is not possible since
k is odd. □

CHAPTER 12

Equation (2.6.1) with t ≥ k − 2 and ω(d) = 1:
Proof of Theorem 2.6.2

12.1. Introduction

We shall prove Theorem 2.6.2 in this chapter. From now on, we assume (9.1.1) is valid with
ψ = 2, ω(d) = 1 and we shall suppose it without reference. Let d = pα. Then (1, 2) is the only
partition if d = 2 and (2, 2) is the only partition if d = 4. For d ̸= 2, 4, we see that (η, d
η ) and ( d
η , η)
are the only distinct partitions of d.
In view of Lemma 9.1.1 with ψ = 2, there is no loss of generality in assuming that k is prime
whenever k ≥ 23 in the proof of Theorem 2.6.2. Therefore we suppose from now onward without
reference that k is prime if k ≥ 23.
 12.2. Lemmas

We apply Theorem 1.4.1 and Lemma 9.4.1 to derive the following result.

Lemma 12.2.1. Let k ≥ 9. Then we have

|T1| > 0.1754k for k ≥ 81.(12.2.1)

and
 n + γtd > η2k2.(12.2.2)

Proof. We observe that π(2k) − π(k) > 2 since k ≥ 9. Therefore P (∆) > k by Theorem 1.4.1.
Now we see from (9.1.1) that
 n + γtd > k2.(12.2.3)

By (9.4.1), t ≥ k − 2, πd(k) ≤ π(k) and Lemma 3.1.2 (i), we get

|T1| >k − 3 − (k − 1) log k
2 log k − k
log k
 (1 + 1.2762
log k
 ) .

Since the right hand side of the above inequality exceeds 0.1754k for k ≥ 81, the assertion (12.2.1)
follows.
Now we turn to the proof of (12.2.2). By (12.2.3), it suﬃces to consider d = 2
α with α > 1.
From Theorem 1.4.1 and (9.1.1), we have n + (k − 1)d > p
2
π(2k)−2. Now we see from (9.4.1) that

|T1| + πd(k) − π(2k) >k − 3 − (k − 1) log(k − 1) − (k − 3) log 2 + log(k − 2)
2 log pπ(2k)−2 − π(2k)(12.2.4)

and
 |T1| + πd(k) − π(2k) >k − 3 − (k − 1) log k − (k − 3) log 2 + log k
2 log k − 2k
log 2k
 (1 + 1.2762
log 2k
 )

by Lemma 3.1.2 (i). When k ≥ 60, we observe that the right hand side of the preceding inequality
is positive. Therefore |T1| + πd(k) > π(2k) implying n + γtd > 4k2 for k ≥ 60. Thus we may assume
k < 60. Now we check that the right hand side of (12.2.4) is positive for k ≥ 33. Therefore we may
suppose that k < 33 and n + (k − 3)d ≤ n + γtd ≤ 4k2. Hence d = 2
α < 4k2
k−3 . For n, d, k satisfying

k < 33, d < 4k2
k−3 , n + (k − 3)d ≤ 4k2 and n + (k − 1)d ≥ p2
π(2k)−2, we check that there are at least

119

120 12. EQUATION (2.6.1) WITH t ≥ k − 2 AND ω(d) = 1: PROOF OF THEOREM 2.6.2

three i with 0 ≤ i < k such that n + id is divisible by a prime > k to the ﬁrst power. This is not
possible. □

Lemma 12.2.2. We have
 t − |R| ≥
 




5 for k ≥ 81
5 − ψ for k ≥ 55
4 − ψ for k ≥ 28, k ̸= 31
3 − ψ for k = 31.

(12.2.5)

Proof. Suppose t − |R| < 5 and k ≥ 292. Then |R| ≥ 286 since t ≥ k − 2 and ∏
bi∈R bi ≥
(1.6)
|R|(|R|)! by (9.4.9). We observe that (9.3.29) hold for k ≥ 292 with i0 = 0, h0 = 286, z1 =
1.6, g1 = 6, m = 17, ℓ = 0, n0 = 1, n1 = 1 and n2 = 2 1
6 . We check that the right hand side
of (9.3.29) is an increasing function of k and it exceeds g1 at k = 292 which is a contradiction.
Therefore t − |R| ≥ 5 for k ≥ 292. Thus we may assume that k < 292. By taking r = 3 for
k < 50, r = 4 for 50 ≤ k ≤ 181 and r = 5 for 181 < k < 292 in (9.2.3) and (9.2.5), we get
t − |R| ≥ k − ψ − F ′(k, r) − 2r ≥ 7 − ψ, 5 − ψ, 4 − ψ for k ≥ 81, 55, 28, respectively except at
k = 29, 31, 43, 47 where t − |R| ≥ k − ψ − F (k, r) − 2r ≥ k − ψ − F ′(k, r) − 2r = 3 − ψ. We may
suppose that k = 29, 43, 47, t − |R| = 3 − ψ and F (k, r) = F ′(k, r). Further we may assume that
for each prime 7 ≤ p ≤ k, there are exactly σp number of i’s for which p|bi and for any i, pq ∤ bi
whenever 7 ≤ q ≤ k, q ̸= p. Now we get a contradiction by considering the i’s for which bi’s are
divisible by primes 7, 13; 7, 41; 23, 11 when k = 29, 43, 47, respectively. For instance let k = 29. Then
7|bi for i ∈ {0, 7, 14, 21, 28}. Then 13|bi for i ∈ {h + 13j : 0 ≤ j ≤ 2} with h = 0, 1, 2. This is not
possible. □

Lemma 12.2.3. Let 9 ≤ k ≤ 23 and d odd. Suppose that t − |R| ≥ 3 for k = 23 and t − |R| ≥ 2
for k < 23. Then (9.1.1) does not hold.

Proof. Suppose (9.1.1) holds. From (12.2.2) and Lemma 9.3.5, the partition (η, dη−1) is the
only permissible partition for any pair (i, j) with bi = bj. Let Q = 2 if k = 23 and Q = 1 if k < 23.
We now apply Lemma 9.3.10 with z0 = 3 for k = 23 and z0 = 2 for k < 23 to get d < 4
Q (k − 1),
θ1 < 4
Q(k−1) and
θ1 + θ2 < 1
2
 { 1
Q2 + 4
Q(k − 1) +
 √ 1
Q4 + 4
Q3(k − 1)
 }
 =: Θ(k − 1).

Further from (1.4.11), we have n + (k − 1)d ≥ n + γtd ≥ p2
π(2k)−2. Therefore pα = d < 4
Q (k − 1) and
p2
π(2k)−2 ≤ n + (k − 1)d < (k − 1)
3Θ(k − 1). For these possibilities of n, d and k, we check that there
are at least three i with 0 ≤ i < k such that n + id is divisible by a prime > k to an odd power.
This contradicts (9.1.1). □

12.3. Equation (2.6.1) implies t − |R| ≤ 1

Lemma 12.3.1. Equation 9.1.1 with k ≥ 9 implies that t − |R| ≤ 1.

Proof. Assume that k ≥ 9 and t − |R| ≥ 2. Let d = 2, 4. Then |R| ≤ t − 2 contradicting
|R| = t by (12.2.2) and Lemma 9.3.7. Thus d ̸= 2, 4. Further by (12.2.2) and Lemma 9.3.7, we have
ν(bi0) ≤ 2 and ν(Bi0) ≤ 2. Also by Lemma 9.3.5, the partition (eta, dη−1) is the only permissible
partition for any pair (i, j) with bi = bj.
Let k ≥ 81. Then t − |R| ≥ 5 by Lemma 12.2.2. Now we derive from Lemma 9.3.10 with z0 = 5
to get d < k − 1 giving θ1 ≤ 1
k−1 and hence

n + (k − 1)d = (θ1 + θ2)(k − 1)
3 < (k − 1)
3

2
 { 1
16 + 1
k − 1 +
 √ 1
(16)2 + 1
16(k − 1)
 }

12.4. PROOF OF THEOREM 2.6.2 121

from (9.3.5). On the other hand, we get from (12.2.1) and ν(Bi0) ≤ 2 that n+(k −1)d ≥ 0.1754k
2 k2 ≥
0.1754 k3
2 . Comparing the upper and lower bounds of n + (k − 1)d, we obtain

0.1754 <
 { 1
16 + 1
k − 1 +
 √ 1
(16)2 + 1
16(k − 1)
 }
 ≤ 0.144

since k ≥ 81. This is a contradiction.
Thus k < 81. Let d be even. We see from ν(ai) ≤ 2 and (9.2.6) that ξr ≤ 2g2δ ≤ 2r−2. Let
r = 3. From (9.2.1), we get k − 2 − F ′(k, r) ≤ ξr ≤ 2r−2. We ﬁnd k − 2 − F ′(k, r) > 2r−2 by
computation. This is a contradiction.
Therefore d is odd. Since t − |R| ≥ 2, we get from Lemmas 12.2.2 and 9.3.10 with z0 = 2, 3 that
d < 2(k − 1) if k ≥ 55 and d < 4(k − 1) if k < 55. Since gp(r) ≤ 2r−1 for r = 4, p < 220 by (9.2.14),
we get from (9.2.10) with r = 4 that t − |R| ≥ k − 2 − F ′(k, r) − 2r−1 which is ≥ 5 for k ≥ 29 and
≥ 3 for k = 23.
Let k ≥ 29. Then we get from Lemma 9.3.10 with z0 = 5 that d < k − 1. By taking r = 3
for k < 53 and r = 4 for 53 ≤ k < 81, we derive from (9.2.9), (9.2.14), ν(ai) ≤ 2 and (9.2.1) that
k − 2 − F ′(k, r) ≤ ξr ≤ 2gp ≤ 2r. We check by computation that k − 2 − F ′(k, r) > 2r. This is a
contradiction.
Thus k ≤ 23. Then t − |R| ≥ 3 for k = 23 and t − |R| ≥ 2 for k < 23. By Lemma 12.2.3, this is
not possible. □

Corollary 12.3.2. Let k ≥ 9. Equation (9.1.1) implies that either k ≤ 23 or k = 31. Also
P (d) > k.

Proof. By Lemmas 12.2.2 and 12.3.1, we see that either k ≤ 23 or k = 31. Suppose that
P (d) ≤ k. Since gP (d)(r) ≤ 2r−1 for r = 3 by (9.2.14), we get from (9.2.10) with r = 3 that
t − |R| ≥ k − 2 − F ′(k, r) − 2r−1 ≥ 2 except at k = 9 where t − |R| ≥ 1. This contradicts Lemma
12.3.1 for k > 9. Let k = 9. By taking r = 4, we get from gP (d)(r) ≤ 2r−2 by (9.2.14) and (9.2.10)
that t − |R| ≥ k − 2 − F ′(k, 4) − 24−2 ≥ 2. This contradicts Lemma 12.3.1. □

Corollary 12.3.3. Let ψ = 0. Equation (9.1.1) with P (b) < k implies that k ≤ 9.

Proof. Let k ≥ 10. By Corollary 12.3.2, we see that either k ≤ 23 or k = 31. Let k = 10. Then
we get from (9.2.5) with r = 2 that t − |R| ≥ k − F ′(k, r) − 2r = 2 contradicting Lemma 12.3.1. Thus
(2.1.1) does not hold at k = 10. By induction, we may assume k ∈ {12, 14, 18, 20} and further there
is at most one i for which p|ai with p = k − 1. We take r = 2 for k = 12, 14 and r = 3 for k = 18, 20.
Now we get from |{bi : P (bi) > pr}| ≤ F ′(k, r) − 1 and (9.2.2) that t − |R| ≥ k − F ′(k, r) + 1 − 2r ≥ 2.
This contradicts Lemma 12.3.1. □

12.4. Proof of Theorem 2.6.2

Suppose that the assumptions of Theorem 2.6.2 are satisﬁed and assume (2.1.1) with ω(d) = 1.
By Corollary 12.3.2, we have P (d) > k and further we restrict to k ≤ 23 and k = 31. Also t − |R| ≤ 1
by Lemma 12.3.1. Further it suﬃces to prove the assertion for k ∈ {15, 18, 20, 23, 31} since the cases
k = 16, 17; k = 19 and k = 21, 22 follows from those of k = 15, 18 and 20, respectively.
We shall arrive at a contradiction by showing t − |R| ≥ 2. For any prime p, let σ′
p = |{ai : p|ai}|.
Then σ′
p ≤ σp. We use some notation and terminologies as in Section 9.2.
For any subset I ⊆ [0, k) ∩ Z and primes p1 and p2, we have the sets I1 and I2 deﬁned in

Lemma 10.3.2. Then from ( ai
p ) = ( i−ip
p ) ( d
p ), we see that either ( ai
p1
 ) ̸= ( ai
p2
 ) for all i ∈ I1 or
( ai
p1
 ) ̸= ( ai
p2
 ) for all i ∈ I2. We deﬁne (M, B) = (I1, I2) in the preceding case and (M, B) = (I2, I1)

in the latter case. We call (I1, I2, M, B) = (I k
1 , I k
2 , M k, Bk) when I = [0, k) ∩ Z. Then for any
I ⊆ [0, k) ∩ Z, we have
 I1 ⊆ I k
1 , I2 ⊆ I k
2 , M ⊆ M k, B ⊆ Bk

122 12. EQUATION (2.6.1) WITH t ≥ k − 2 AND ω(d) = 1: PROOF OF THEOREM 2.6.2

and
 |M | ≥ |M k| − (k − |I|), |B| ≥ |Bk| − (k − |I|).(12.4.1)

12.4.1. The case k = 15. Then σ′
7 = 3 implies that 7|a7j for j = 0, 1, 2 and σ′
7 ≤ 2 if
7 ∤ a0a7a14. Similarly σ′
13 = 2 implies 13|a0, 13|a13 or 13|a1, 13|a14 and σ′
13 ≤ 1 otherwise. Thus
|{ai : 7|ai or 13|ai}| ≤ 4. It suﬃces to have

|{ai : p|ai for 5 ≤ p ≤ 13}| ≤ 7(12.4.2)

since then t − |R| ≥ k − 2 − |{ai : p|ai for 5 ≤ p ≤ 13}| − 4 ≥ 2 by (9.2.2) with r = 2, a contradiction.
Let p1 = 11, p2 = 13 and I = {γ1, γ2, · · · , γt}. We observe that P (ai) ≤ 7 for i ∈ M ∪ B. Since( 5
11 ) ̸= ( 5
13 ) but ( q
11 ) = ( q
13 ) for a prime q < k other than 5, 11, 13, we observe that 5|ai whenever
i ∈ M. Since σ5 ≤ 3 and |I| = k − 2, we obtain from (12.4.1) that |M
k| ≤ 5 and 5|ai for at least
|M
k| − 2 i’s with i ∈ Mk. Further 5 ∤ ai for i ∈ B.
By taking the mirror image (9.1.5) of (2.1.1), we may suppose that 0 ≤ i13 ≤ 7. For each
possibility 0 ≤ i11 < 11 and 0 ≤ i13 ≤ 7, we compute |I k
1 |, |I k
2 | and restrict to those pairs (i11, i13)
with min(|I k
1 |, |I k
2 |) ≤ 5. We see from max(|I k
1 |, |I k
2 |) ≥ 6 that M
k is exactly one of I k
1 or I k
2 with
minimum cardinality and hence Bk is the other. Now we restrict to those pairs (i11, i13) for which
there are at most two elements i ∈ M
k such that 5 ∤ ai. There are 31 such pairs. By counting the
multiples of 11 and 13 and also the maximum multiples of 5 in M
k and the maximum number of
multiples of 7 in Bk, we again restrict to those pairs (i11, i13) which do not satisfy (12.4.2). With
this procedure, all pairs (i11, i13) are excluded other than

(0, 6), (1, 3), (2, 4), (3, 5), (4, 6), (5, 3).(12.4.3)

We ﬁrst explain the procedure by showing how (i11, i13) = (0, 0) is excluded. Now M
k = {5, 10}
and Bk = {1, 2, 3, 4, 6, 7, 8, 9, 12, 14}. Then there are 3 multiples of 11 and 13, at most 2 multiples of
5 in M
k and at most 2 multiples of 7 in Bk implying (12.4.2). Thus (i11, i13) = (0, 0) is excluded.
Let (i11, i13) = (5, 3). Then M
k = {1, 6, 11} and Bk = {0, 2, 4, 7, 8, 9, 10, 12, 13, 14} giving
i5 = 1 and 5|a1a6a11. We may assume that 7|ai for i ∈ {0, 7, 14} otherwise (12.4.2) holds. By
taking p1 = 5, p2 = 11 and I = Bk, we get I1 = {4, 10, 13} and I2 = {0, 2, 7, 8, 9, 12, 14}. Since( 2
5 ) = ( 2
11 ), ( 7
5 ) = ( 7
11 ) and ( 3
5 ) ̸= ( 3
11 ), we observe that 3|ai for i ∈ I1 ∩ B and 3 ∤ ai for i ∈ I2 ∩ B.
Thus ai ∈ {3, 6} for i ∈ I1 ∩ B and ai ∈ {1, 2, 7, 14} for i ∈ I2 ∩ B. Now from ( ai
7 ) = ( i−0
7 ) ( d
7 )

and ( 3
7 ) = ( 6
7 ), we see that at least one of 4, 10, 13 is not in B implying i /∈ B for at most one
i ∈ I2. Therefore there are distinct pairs (i1, i2) and (j1, j2) with i1, i2, j1, j2 ∈ I2 ∩ B such that
ai1 = ai2, i1 > i2 and aj1 = aj2, j1 > j2 giving t − |R| ≥ 2. This is a contradiction. Similarly, all
other pairs (i11, i13) in (12.4.3) are excluded.

12.4.2. The case k = 18. We may assume that σ′
17 = 1 and 17 ∤ a0a1a2a15a16a17 otherwise
the assertion follows the case k = 15. If |{ai : P (ai) = 5}| = 4, we see from {ai : P (ai) = 5} ⊆
{5, 10, 15, 30} that ai5ai5+5ai5+10ai5+15 = (150)2 implying (n + i5d)(n + (i5 + 5)d)(n + (i5 + 10)d)(n +
(i5 + 15)d) is a square, contradicting Eulers’ result for k = 4. Thus we have |{ai : P (ai) = 5}| ≤ 3.
Further for each prime 7 ≤ p ≤ 13, we may also assume that σ′
p = σp and for any i, pq ∤ ai whenever
7 ≤ q ≤ 17, q ̸= p otherwise t − |R| ≥ k − 2 − ∑

7≤p≤17 σ′
p − 3 − 4 ≥ 2 by (9.2.2) with r = 2.
Let p1 = 11, p2 = 13 and I = {γ1, γ2, · · · , γt}. Since ( 5
11 ) ̸= ( 5
13 ) and ( 17
11 ) ̸= ( 17
13 ) but( q
11 ) = ( q
13 ) for q < k, q ̸= 5, 17, 11, 13, we observe that for i ∈ M, exactly one of 5|ai or 17|ai holds.
Thus 5 · 17 ∤ ai whenever i ∈ M. For i ∈ B, either 5 ∤ ai, 17 ∤ ai or 5|ai, 17|ai. Thus for i ∈ B, we
have P (ai) ≤ 7 except possibly for one i for which 5 · 17|ai. Since σ5 ≤ 4 and σ′
17 ≤ 1, we obtain
|M
k| ≤ 7 and 5|ai for at least |M
k| − 3 i’s with i ∈ Mk. Hence |M
k| = 7 implies that either

{a + 5j : 0 ≤ j ≤ 3} ⊆ I k
1 or {b + 5j : 0 ≤ j ≤ 3} ⊆ I k
2(12.4.4)

for some a, b ∈ {0, 1, 2}.
Since σ′
11 = 2 and σ′
13 = 2, we may suppose that 0 ≤ i11 ≤ 6 and 0 ≤ i13 ≤ 4. Further i11 ̸= i13
and i11 + 11 ̸= i13 + 13. We observe that either min(|I k
1 |, |I k
2 |) ≤ 6 or |I k
1 | = |I k
2 | = 7. For pairs
(i11, i13) with |I k
1 | = |I k
2 | = 7, we check that (12.4.4) is not valid. Thus we restrict to those pairs
satisfying min(|I k
1 |, |I k
2 |) ≤ 6. There are 16 such pairs. Further we see from max(|I k
1 |, |I k
2 |) ≥ 8

12.4. PROOF OF THEOREM 2.6.2 123

that M
k is exactly one of I k
1 or I k
2 with minimum cardinality and hence Bk is the other one.
Now we restrict to those pairs (i11, i13) for which 5|ai for at least 3 elements i ∈ M
k otherwise
t − |R| ≥ k − 2 − ∑

7≤p≤17 σ′
p − 2 − 4 ≥ 2 by (9.2.2) with r = 2. We ﬁnd that (i11, i13) ∈
{(1, 3), (2, 4), (4, 0), (5, 1)}. For these pairs (i11, i13), we check that there are at most 4 multiples ai
of 5 and 17 with i ∈ Mk ∪ Bk. Thus if |{i : i ∈ B, 7|ai}| ≤ 2, then t − |R| ≥ 2 by (9.2.2) with
r = 2. Therefore we may assume that |{i : i ∈ B, 7|ai}| = 3 and hence |{i : i ∈ Bk, 7|ai}| = 3.
We now restrict to those pairs (i11, i13) for which |{i : i ∈ Bk, 7|ai}| = 3. They are given by
(i11, i13) ∈ {(2, 4), (4, 0)}.
Let (i11, i13) = (2, 4). Then by taking p1 = 11 and p2 = 13 as above, we have M
k = {1, 6, 8, 11}
and Bk = {0, 3, 5, 7, 9, 10, 12, 14, 15, 16} giving i5 = 1 and 5|a1a6a11. We may assume that 17|a8
since 17 ∤ a16. Hence P (ai) ≤ 7 for i ∈ B. Consequently P (ai) ≤ 7 for exactly 8 elements i ∈ Bk

and other 2 elements are not in B. Further 7|ai for i ∈ {0, 7, 14} and 0, 7, 14 ∈ B. Now we take
p1 = 5, p2 = 11 and I = Bk to get I1 = {0, 5, 7, 9} and I2 = {3, 10, 12, 14, 15}. Since ( 2
5 ) = ( 2
11 ),( 7
5 ) = ( 7
11 ) and ( 3
5 ) ̸= ( 3
11 ), we observe that either 3|ai for i ∈ I1 ∩ B or 3|ai for i ∈ I2 ∩ B. The
former possibility is excluded since 0, 7 ∈ I1 ∩ B and the latter is not possible since 14 ∈ I2 ∩ B. The
other case (i11, i13) = (4, 0) is excluded similarly.

12.4.3. The case k = 20. We may assume that σ′
19 = 1 and 19 ∤ a0a19 otherwise the assertion
follows from the case k = 18. Also we have |{ai : P (ai) = 5}| ≤ 3 by Eulers’ result for k = 4.
Further for each prime 7 ≤ p ≤ 17, we may also assume that σ′
p = σp and for any i, pq ∤ ai whenever
7 ≤ p < q ≤ 19 otherwise t − |R| ≥ k − 2 − ∑

7≤p≤17 σ′
p − 3 − 4 ≥ 2 by (9.2.2) with r = 2.
Let p1 = 11, p2 = 13 and I = {γ1, γ2, · · · , γt}. Then as in the case k = 18, we observe that for
i ∈ M, exactly one of 5|ai or 17|ai holds but 5 · 17 ∤ ai. For i ∈ B, either 5 ∤ ai, 17 ∤ ai or 5|ai, 17|ai.
Since σ5 ≤ 4 and σ17 ≤ 2, we obtain |M
k| ≤ 8 and 5|ai for at least |M
k| − 4 i’s with i ∈ Mk. Hence
|M
k| = 8 implies that either

{a + 5j : 0 ≤ j ≤ 3} ⊆ I k
1 or {b + 5j : 0 ≤ j ≤ 3} ⊆ I k
2(12.4.5)

for some a, b ∈ {0, 1, 2, 3, 4}.
Since σ′
11 = 2 and σ′
13 = 2, we may suppose that 0 ≤ i11 ≤ 8 and 0 ≤ i13 ≤ 6. Further i11 ̸= i13
and i11 + 11 ̸= i13 + 13. We observe that either min(|I k
1 |, |I k
2 |) ≤ 7 or |I k
1 | = |I k
2 | = 8. For pairs
(i11, i13) with |I k
1 | = |I k
2 | = 8, we check that (12.4.5) is not valid. Thus we restrict to those pairs
satisfying min(|I k
1 |, |I k
2 |) ≤ 7. There are 40 such pairs. Further we see from max(|I k
1 |, |I k
2 |) ≥ 8
that M
k is the one of I k
1 or I k
2 with minimum cardinality and hence Bk is the other. Now we
restrict to those pairs (i11, i13) for which 5|ai for at least 3 elements i ∈ Mk otherwise t − |R| ≥
k − 2 − 1 − ∑

7≤p≤17 σ′
p − 2 − 4 ≥ 2 by (9.2.2) with r = 2. We are left with 22 such pairs.
Further by (12.4.1) with |I| = k − 2, we restrict to those pairs (i11, i13) for which there are at least
|M
k| − 2 elements i ∈ Mk such that 5|ai or 17|ai. There are 12 such pairs (i11, i13) and for these
pairs, we check that there are at most 4 multiples ai of 5 and 17 with i ∈ M
k ∪ Bk. This implies
t−|R| ≥ k −2−1−4−∑

11≤p≤13 σ′
p −4 ≥ 2 by (9.2.2) with r = 2. For instance, let (i11, i13) = (3, 5).
Then M
k = {2, 7, 9, 12} and Bk = {0, 1, 4, 6, 8, 10, 11, 13, 15, 16, 17, 19}. Since 5|ai for at least three
elements i ∈ M
k, we get 5|ai for i ∈ {2, 7, 12} giving i5 = 2. Further 17|a9 or 5 · 17|a17 giving 4
multiples ai of 5 and 17 with i ∈ Mk ∪ Bk. Thus t − |R| ≥ 2 as above.

12.4.4. The case k = 23. We may assume that σ′
23 = 1 and 23 ∤ ai for 0 ≤ i ≤ 2 and
20 ≤ i < 23 otherwise the assertion follows from the case k = 20. We have σ′
11 = 3 if 11|a11j with
j = 0, 1, 2 and σ′
11 ≤ 2 if 11 ∤ a0a11a22. Also σ′
7 = 4 implies that 7|a7j or 7|a1+7j with 0 ≤ j ≤ 3
and σ′
7 ≤ 3 otherwise. Thus |{ai : 7|ai or 11|ai}| ≤ 6. Further by Eulers result for k = 4, we obtain
|{ai : P (ai) = 5}| ≤ 4. If

|{ai : p|ai, 5 ≤ p ≤ 23} ≤ 4 + ∑

7≤p≤23 σp − 1 − 2 = 15,

124 12. EQUATION (2.6.1) WITH t ≥ k − 2 AND ω(d) = 1: PROOF OF THEOREM 2.6.2

then we get from (9.2.2) with r = 2 that t − |R| ≥ k − 2 − 15 − 4 = 2, a contradiction. Therefore we
have
 4 + ∑

7≤p≤23 σp − 2 ≤ |{ai : p|ai, 5 ≤ p ≤ 23} ≤ 4 + ∑

7≤p≤19 σp − 1.(12.4.6)

Let p1 = 11, p2 = 13 and I = {γ1, γ2, · · · , γt}. Then as in the case k = 18, we observe that
for i ∈ M, exactly one of 5|ai or 17|ai holds but 5 · 17 ∤ ai. Further for i ∈ B, either 5 ∤ ai, 17 ∤ ai
or 5 · 17|ai. Since σ5 ≤ 5 and σ17 ≤ 2, we obtain |M
k| ≤ 9 and 5|ai for at least |M
k| − 4 i’s with
i ∈ Mk.
By taking the mirror image (9.1.5) of (2.1.1), we may suppose that 0 ≤ i11 < 11 and 0 ≤ i13 ≤ 11.
For each of these pairs (i11, i13), we compute |I k
1 |, |I k
2 | and check that max(|I k
1 |, |I k
2 |) > 9. First
we restrict to those pairs (i11, i13) for which min(|I k
1 |, |I k
2 |) ≤ 9. Therefore M
k is exactly one of
I k
1 or I k
2 with minimum cardinality and hence Bk is the other set. Now we restrict to those pairs
(i11, i13) for which there are at least |M
k| − 2 elements i ∈ Mk such that either 5|ai or 17|ai. There
are 31 such pairs. Next we count the number of multiples of 11, 13, maximum multiples of 5, 17 in
M
k ∪ Bk and 7, 19 in Bk to check that (12.4.6) is not valid. This is a contradiction. For example,
let (i11, i13) = (0, 2). Then M
k = {4, 6, 9, 18, 19, 20} and Bk = {1, 3, 5, 7, 8, 10, 12, 13, 14, 16, 17, 21}
giving 5|ai for i ∈ {4, 9, 19}, i5 = 4. Further 17|ai for exactly one i ∈ {6, 18, 20} and other two
i’s in {6, 18, 20} deleted. Thus 5 · 17 ∤ a14 so that (12.4.6) is not valid. For another example, let
(i11, i13) = (4, 0). Then M
k = {6, 9, 11, 16, 21} and Bk = {1, 2, 3, 5, 7, 8, 10, 12, 14, 17, 18, 19, 20, 22}
giving 5|ai for i ∈ {6, 11, 16, 21}, i5 = 1. Further we have either 17|a9, gcd(5 · 17, a1) = 1 or
9 /∈ M, 5 · 17|a1. Now 7|ai for at most 3 elements i ∈ Bk so that (12.4.6) is not satisﬁed. This is a
contradiction.

12.4.5. The case k = 31. From t − |R| ≥ k − 2 − ∑

7≤p≤31 σ′
p − 8 ≥ k − 2 − ∑

7≤p≤31 σp − 8 = 1
by (9.2.2) and (9.2.5) with r = 3, we may assume for each prime 7 ≤ p ≤ 31 that σ′
p = σp and
for any i, pq ∤ ai whenever 7 ≤ p < q ≤ 31. Let I = {γ1, γ2, · · · , γt}. By taking the mirror image
(9.1.5) of (2.1.1) and σ19 = σ29 = 2, we may assume that i29 = 0 and 1 ≤ i19 ≤ 11, i19 ̸= 10.
For p ≤ 31 with p ̸= 19, 29, since ( p
19 ) ̸= ( p
29 ) if and only if p = 11, 13, 17, we observe that for
i ∈ M, either 11|ai or 13|ai or 17|ai. Since σ11 + σ13 + σ17 ≤ 8, we obtain |M
k| ≤ 10 and p|ai for
at least |M
k| − 2 elements i ∈ Mk and p ∈ {11, 13, 17}. Now for each of the pair (i19, i29) given
by i29 = 0, 1 ≤ i19 ≤ 11, i19 ̸= 10, we compute |I k
1 |, |I k
2 |. Since max(|I k
1 |, |I k
2 |) ≥ 14, we restrict to
those pairs (i19, i29) with min(|I k
1 |, |I k
2 |) ≤ 10. Then we are left with the only pair (i19, i29) = (1, 0).
Further noticing that M
k is exactly one of I k
1 or I k
2 with minimum cardinality, we get M
k =
{3, 5, 6, 7, 11, 14, 15, 19, 24, 25} and Bk = {2, 4, 8, 9, 10, 12, 13, 16, 17, 18, 21, 22, 23, 26, 27, 28, 30}. We
ﬁnd that there are at most 7 elements i ∈ M
k for which either 11|ai or 13|ai or 17|ai. This is not
possible. □

Bibliography

[1] M.A. Bennett, N Bruin, K. Gy¨ory and L. Hajdu, Powers from products of consecutive terms
in arithmetic progression, Proc. London Math. Soc. 92 (2006), 273-306.
[2] E. Catalan, Note extraite d’une lettre adress´ee `a l’´editeur, J. reine angew. Math. 27 (1844).
[3] Z. Cao, A note on the Diophantine equation a
x + by = c
z, Acta Arith., 91 (1999), 85-93.
[4] H. Cram´er, On the order of magnitude of the diﬀerence between consecutive prime numbers,
Acta Arith. 2 (1937), 23-46.
[5] L. E. Dickson, History of the theory of numbers, Vol II, Carnegie Institution, Washington,
1920. Reprinted by Chelsea Publishing Company, (1971).
[6] P. Dusart, Autour de la fonction qui compte le nombre de nombres premiers, Ph.D thesis,
Universit´e de Limoges, (1998).
[7] —, In´egaliti´es explicites pour ψ(X), θ(X), π(X) et les nombres premiers, C. R. Math. Rep.
Acad. Sci. Canada 21(1)(1999), 53-59, 55.
[8] —, The kth prime is greater than k(logk + log logk − 1) for k ≥ 2, Math. Comp. 68 (1999),
no. 225, 411-415.
[9] N. Elkies, ABC implies Mordell, Int. Math. Res. Not. 7 (1991).
[10] P. Erd˝os, A theorem of Sylvester and Schur, J. London Math. Soc. 9 (1934), 282-288.
[11] —, Note on the product of consecutive integers(II), J.London Math.Soc. 14 (1939), 245-249.
[12] —, Note on the product of consecutive integers(III), Indag. Math. 17 (1955), 85-90.
[13] P. Erd˝os and J. L. Selfridge, The product of consecutive integers is never a power, Illinois
Jour. Math. 19 (1975), 292-301.
[14] —, Some problems on the prime consecutive integers II, Proc. Wash. State Univ. Conference
on Number Theory, Dept. of Math., Washington State Univ., Pullman, Washington, (1971),
13-21.
[15] L. Euler, M´em. Acad. Sc. St. Peters. 8, 1817-1818 (1780), 3. Comm. Arith., II, 411-413.
[16] M. Faulkner, On a theorem of Sylvester and Schur, J. Lond. Math. Soc., 41 (1966), 107-110.
[17] P. Filakovszky and L. Hajdu, The resolution of the diophantine equation x(d + d) · · · (x +
(k − 1)d) = by2 for ﬁxed d, Acta Arith., 98 (2001), 151-154.
[18] M. Filaseta, C. Finch and J. R. Leidy, T. N. Shorey’s inﬂuence in the theory of irreducible
polynomials, Proceedings of the Diophantine Conference in Honor of T. N. Shorey, to appear.
[19] A. Granville and T. J. Tucker, It’s as easy as abc, Notices of the AMS, 49, 1224-31.
[20] C. A. Grimm, A conjecture on consecutive composite numbers, Amer. Math. monthly, 76
(1969), 1126-1128.
[21] K. Gy˝ory, On the Diophantine equation n(n+1) · · · (n+k −1) = bx
l, Acta Arith. 83 (1998),
87-92, [Ch 9].
[22] P Hall, On representatives of subsets, J. London Math. Soc., 10 (1935), 26-30.
[23] D. Hanson, On a theorem of Sylvester and Schur, Canad. Math. Bull., 16 (1973), 195-199.
[24] M. Jutila, On numbers with a large prime factor II, J. Indian Math. Soc. (N.S.) 38 (1974),
125-30.
[25] N. Hirata-Kohno, S. Laishram, T. N. Shorey and R. Tijdeman, An extension of a theorem
of Euler, Acta Arith., accepted for publication.
[26] S. Laishram, An estimate for the length of an arithmetic progression the product of whose
terms is almost square, Pub. Math. Debr., 68 (2006), 451-475.
[27] —, Topics in Diophantine equations, M.Sc. Thesis, Mumbai University, 2004, online at
http://www.math.tifr.res.in/∼shanta/MScthesis.pdf.

125

126 BIBLIOGRAPHY

[28] S. Laishram and T. N. Shorey, Number of prime divisors in a product of consecutive integers,
Acta Arith. 113 (2004), 327-341.
[29] —, Number of prime divisors in a product of terms of an arithmetic progression, Indag.
Math., 15(4) (2004), 505-521.
[30] —, Greatest prime factor of a product of consecutive integers, Acta Arith., 120 (2005),
299-306.
[31] —, Grimm’s Conjecture on consecutive integers, Int. Jour. of Number Theory, 2 (2006),
1-5.
[32] —, The greatest prime prime divisor of a product of terms in an arithmetic progression,
Indag. Math., 17(3) (2006), 425-436.
[33] —, The equation n(n + d) · · · (n + (k − 1)d) = by2 with ω(d) ≤ 6 or d ≤ 1010, Acta Arith.,
accepted for publication.
[34] —, Squares in products in arithmetic progression with at most two terms omitted and com-
mon diﬀerence a prime power, to appear.
[35] M. Langevin, Plus grand facteur premier d’entiers cons´ecutifs, C.r. hebd. S´eanc. Acad. Sci.,
Paris A 280 (1975), 1567-70.
[36] —, Plus grand facteur premier d’entiers voisins, C.r. hebd. S´eanc. Acad. Sci., Paris A 281
(1975), 491-3.
[37] —, M´ethodes ´el´ementaires en vue du th´eorem`ede Sylvester, S´em. Delange-Pisot-Poitou
1975/76, Exp. G2 pp. 9.
[38] —, Plus grand facteur premier d’entiers en progression arith ´metique, S´em. Delange - Pisot
- Poitou, 18 ean´nee, 1976/77, No.3. pp. 6.
[39] —, Facteurs premiers d’entiers en progression arith ´metique, S´em. Delange - Pisot - Poitou,
1977/78, Paris, Exp 4. pp. 7.
[40] R. Marszalek, On the product of consecutive elements of an arithmetic progression, Monatsh.
f¨ur. Math. 100 (1985), 215-222.
[41] P. Mih˘ailescu, Primary cyclotomic units and a proof of Catalan’s conjecture, J. Reine Angew
. Math. 572 (2004), 167-195.
[42] L.J. Mordell, Diophantine Equations, Academic Press, London (1969).
[43] P. Moree, On arithmetical progressions having only few diﬀerent prime factors in comparison
with their length, Acta Arith. 70 (1995), 295-312.
[44] L. Moser, Insolvability of (2n
n ) = (2a
a )(2b
b ), Canad. Math. Bull.(2), 6 (1963), 167-169.
[45] A. Mukhopadhyay and T. N. Shorey, Almost squares in arithmetic progression (II), Acta
Arith., 110 (2003), 1-14.
[46] —, Almost squares in arithmetic progression (III), Indag. Math., 15 (2004), 523-533.
[47] —, Square free part of products of consecutive integers, Publ. Math. Debrecen, 64 (2004),
79-99.
[48] R. Murty, Prime Numbers and Marriage, Appendix 1, The little book of bigger primes by
P. Ribenboim, Springer, 269-273.
[49] T. Nagell, Sur une classe d’´equations exponentielles, Ark. Mat. 3 (1958), 569-582.
[50] R. Obl´ath, ¨Uber das Produkt funf aufeinander folgender zahlen in einer arithmetischen
Reihe, Publ.Math.Debrecen, 1, (1950), 222-226.
[51] K. Ramachandra and T. N. Shorey, On gaps between numbers with a large prime factor,
Acta Arith., 24 (1973), 99-111.
[52] K. Ramachandra, T. N. Shorey and R. Tijdeman, On Grimm’s problem relating to factori-
sation of a block of consecutive integers, J. reine angew. Math. 273 (1975), 109-124.
[53] —, On Grimm’s problem relating to factorisation of a block of consecutive integers II, J.
reine angew. Math. 288 (1976), 192-201.
[54] O. Ramar´e and R. Rumely, Primes in Arithmetic Progression, Math. Comp. 65 (1996),
397-425.
[55] O. Rigge, On a diophantine problem, Ark. Mat. Astr. Fys. 27A, 3, (1940), 10 pp.

BIBLIOGRAPHY 127

[56] G. Robin, Estimation de la fonction de Tchebychef θ sur le k-i`eme nombre premier et
grandes valeurs de la fonction ω(n) nombre de diviseurs premiers de n, Acta Arith., 42
(1983), 367-389.
[57] H. Robbins, A remark on stirling’s formula, Amer. Math. Monthly 62, (1955). 26-29.
[58] J. B. Rosser and L. Schoenfeld, Approximate formulas for some functions of prime numbers,
Illinois Jour. Math 6 (1962), 64-94.
[59] N. Saradha, Squares in products with terms in an arithmetic profession, Acta Arith., 86
(1998), 27-43.
[60] —, On perfect powers in products with terms from arithmetic progressins, Acta Arith., 82,
(1997), 147-172.
[61] N. Saradha and T. N. Shorey, Almost squares and factorisations in consecutive integers,
Compositio Math. 138 (2003), 113-124.
[62] —, Almost perfect powers in arithmetic progression, Acta Arith. 99 (2001), 363-388.
[63] —, Almost squares in arithmetic progression, Compositio Math. 138 (2003), 73-111.
[64] —, Contributions towards a conjecture of Erdos on perfect powers in arithmetic progressions,
(to appear).
[65] N. Saradha, T. N. Shorey and R. Tijdeman, Some extensions and reﬁnements of a theorem
of Sylvester, Acta Arith. 102 (2002), 167-181.
[66] A. Schinzel and W. Sierpi´nski, Sur certaines hypoth`eses concernant les nombres premiers,
Acta Arith. 4, (1958), 185-208, corrected in Acta Arith. 5, (1959), 259.
[67] L. Schoenfeld, Sharper bounds for the Chebyshev functions θ(x) and ψ(x), II, Math. Comp.
30 (1976), 337-360.
[68] I. Schur, Einige S¨atze ¨ubner Primzahlen mit Anwendung auf Irreduzibilit¨atsfragen, Sit-
szungsber. Preuss. Akad. Wiss. Phys. Math. Kl., 23, (1929), 1-24.
[69] I. Schur, Einige S¨atze ¨ubner Primzahlen mit Anwendung auf Irreduzibilit¨atsfragen I, Sit-
szungsber. Preuss. Akad. Wiss. Phys. Math. Kl., 14, (1929), 125-136.
[70] I. Schur, Aﬀektlose Gleichungen in der Theorie der Laguerreschen und Hermiteschen Poly-
nome, J. Reine Angew. Math., 165, (1931), 52-58.
[71] T. N. Shorey, On gaps between numbers with a large prime factor II, Acta Arith., 25 (1974),
365-73.
[72] —, Exponential diophantine equations involving products of consecutive intergers and re-
lated equations, Number Theory edited by R.P. Bambah, V.C. Dumir and R.J. Hans-Gill,
Hindustan Book Agency (1999), 463-495.
[73] T. N. Shorey and R. Tijdeman, Exponential diophantine equations, Cambridge University
Press (1986).
[74] —, On the number of prime factors of a ﬁnite arithmetical progression, Sichuan Daxue
Xuebao 26 (1989), 72-74.
[75] —, On the greatest prime factor of an arithmetical progression, A tribute to Paul Erd˝os,
ed. by A. Baker, B. Bollob´as and A. Hajnal, Cambridge University Press (1990), 385-389.
[76] —, Perfect powers in products of terms in an arithmetical progression, Compositio Math.
75 (1990), 307-344.
[77] J. J. Sylvester, On arithmetical series, Messenger of Mathematics, XXI (1892), 1-19, 87-
120, and Mathematical Papers, 4 (1912), 687-731.
[78] R. Tijdeman, On the equation of Catalan, Acta Arith. 29 (1976), 197-209.
[79] —, Diophantine equations and diophantine approximations, Number Theory and Applica-
tions, Kluwer Acad. Press, 1989, 215-243.
[80] B. de Weger, Algorithms for diophantine equations, Ph.D thesis, CWI, Amsterdam, 1987.
