<!-- source: https://cs.uwaterloo.ca/journals/JIS/VOL10/Holdener/holdener7.pdf | converted from PDF -->

23 11 Article 07.9.6
Journal of Integer Sequences, Vol. 10 (2007),2
 3

6

1

47

Abundancy “Outlaws” of the Form σ(N )+t
N

William G. Stanton and Judy A. Holdener
Department of Mathematics
Kenyon College
Gambier, Ohio 43022
USA
stantonw@kenyon.edu
holdenerj@kenyon.edu

Abstract

The abundancy index of a positive integer n is deﬁned to be the rational number
I(n) = σ(n)/n, where σ is the sum of divisors function σ(n) = ∑d|n d. An abundancy
outlaw is a rational number greater than 1 that fails to be in the image of of the map
I. In this paper, we consider rational numbers of the form (σ(N ) + t)/N and prove
that under certain conditions such rationals are abundancy outlaws.

1 Introduction

The abundancy index of a positive integer n is deﬁned to be the rational number I(n) =
σ(n)/n, where σ is the sum of divisors function, σ(n) = ∑
d|n d. Positive integers having
integer-valued abundancy indices are said to be multiperfect numbers, and if I(n) = 2 in
particular, then n is perfect. More generally, the abundancy index of a number n can be
thought of as a measure of its perfection; if I(n) < 2 then n is said to be deﬁcient, and if
I(n) > 2 then n is abundant. In this way, the abundancy index is a useful tool in gaining a
better understanding of perfect numbers. In fact, the following theorem provides conditions
equivalent to the existence of an odd perfect number [2].

Theorem 1.1. There exists an odd perfect number if and only if there exist positive integers
p, n, and α such that p ≡ α ≡ 1 mod 4, where p is a prime not dividing n, and

I(n) = 2pα(p − 1)
pα+1 − 1 .

1

So, for example, if one could ﬁnd an integer n having abundancy index equal to 5/3,
then one would be able to produce an odd perfect number. Hence, it is useful to try to
characterize those rational numbers in (1, ∞) that do not appear as the abundancy index of
some positive integer. We will call such numbers abundancy outlaws.

Deﬁnition 1.2. A rational number r/s greater than 1 is said to be an abundancy outlaw if
I(x) = r/s has no solution among the positive integers.

In this paper, we consider the sequence of rational numbers in (1, ∞). For each numerator
a > 1, list the rationals a/b, with gcd(a, b) = 1, so that denominators 1 ≤ b < a appear in
ascending order: 2
1 , 3
1 , 3
2 , 4
1 , 4
3 , 5
1 , 5
2 , 5
3 , 5
4 , 6
1 , 6
5 , 7
1 , 7
2 , 7
3 , 7
4 , 7
5 , 7
6 , ...

While each term in the sequence is either an abundancy index or an abundancy outlaw,
it is generally diﬃcult to determine the status of a given rational. The sequence can be
partitioned into three sets: those rationals that are known to be abundancy indices, those
that are known to be outlaws, and those with abundancy index/outlaw status unknown.
Our goal is to capture outlaws from the third category, increasing the size of the second
category. Since rationals of the form (σ(N ) − t)/N , with t ≥ 1, are known to be outlaws
(see Property 2.3 below), we consider rational numbers of the form (σ(N ) + t)/N . We
prove that under certain conditions (σ(N ) + t)/N is an abundancy outlaw. It is worth
noting that our original interest in such rationals stemmed from our interest in the fraction
5/3 = (σ(3) + 1)/3. Unfortunately, our results do not allow us to say anything about
rationals of the form (σ(p) + 1)/p where p is a prime. Such elusive rationals remain in
category three. Nonetheless, we do prove that (σ(2p) + 1)/(2p) is an abundancy outlaw for
all primes p > 3. (Since I(6) = (σ(22) + 1)/22 and I(18) = (σ(6) + 1)/6, this provides a
complete characterization of fractions of this form.)

2 Preliminaries

It is useful to think of the abundancy index I as a function mapping the natural numbers
n ≥ 2 into the set of rational numbers in (1, ∞). Deﬁning D to be the image of I:

D = {I(n) : n ∈ N, n ≥ 2},

we can ask many questions about D. For instance, how are the abundancy indices distributed
among the set (1, ∞)? Certainly, we can ﬁnd elements of D arbitrarily close to 1 because
I(p) = (p + 1)/p for all primes p. Moreover, it is not hard to show that I(n!) ≥ ∑n
i 1/i, and
therefore D is unbounded. In fact, D is dense in (1, ∞) [3]. Even more interesting, P. Weiner
proved that the set of abundancy outlaws is also dense in (1, ∞) [5]! Hence it seems that the
situation is both complex and interesting. For our purposes, the following properties will be
helpful.

Property 2.1 I(kN ) ≥ I(N ) for all natural numbers k and N ≥ 2. (See [3], page 84.)

2

Property 2.2 If I(n) = k/m with gcd(k, m) = 1, then m|n. This follows directly from
setting σ(n)/n = k/m. Clearly, m|(nk) and since k and m are relatively prime, it
must be that m|n.

Property 2.3 If m < k < σ(m) and k is relatively prime to m, then k/m is an abundancy
outlaw. Hence if r/s is an abundancy index with gcd(r, s) = 1, then r ≥ σ(s). (See
[5], page 309. The property also appears in [1].)

Property 2.3 reveals a class of abundancy outlaws. Indeed, it was using this property
that Weiner was able to prove that the set of outlaws is dense in (1, ∞). It also worth noting
that Property 2.3 implies that (k + 1)/k is an abundancy index if and only if k is prime.
Similarly, (k + 2)/k is an abundancy outlaw whenever k is an odd composite number. If p
is a prime greater than 2, then it is unknown whether (p + 2)/p is an outlaw. (See [4], pages
512-513 for more discussion about this.)
Finally, recent progress has been made by R. Ryan in ﬁnding abundancy outlaws. In
2002, Ryan produced an example of an abundancy outlaw not captured by Property 2.3. (See
Theorem B.6 in [4].) Because the conditions describing Ryan’s outlaw are quite technical,
we will not restate them here. Nonetheless, we want to mention that the search for outlaws
employed in the next section was inspired by Ryan’s work.

3 A search for abundancy outlaws

As Property 2.1 implies, multiplying any number N = ∏n
i=1 pki
i by one of its prime divisors,
pj, will serve to increase its abundancy. The following lemma measures this increase.

Lemma 3.1. Let N = ∏n
i=1 pki
i for primes p1, p2, ..., pn. Then

σ(pkj +1
j )

σ(pkj +1
j ) − 1 = σ(pjN )
pjσ(N )

for all 1 ≤ j ≤ n.

Proof. The result follows from the fact that

pjσ(N ) = pjσ(pkj
j )σ(N/pkj
j )
= pj(∑kj
i=1 pi
j)σ(N/pkj
j )
= (σ(pkj +1
j ) − 1)σ(N/pkj
j ).

Therefore,
 σ (pjN )
pjσ(N ) = σ(pkj +1
j )σ(N/pkj
j )

(σ(pkj +1
j ) − 1)σ(N/pkj
j ) (3.1)

= σ(pkj +1
j )

σ(pkj +1
j ) − 1 . (3.2)

3

Next we present criteria that can be used in the search for abundancy outlaws. As the
assumptions given in Theorem 3.2 below indicate, our search focuses on those fractions r/s
(in reduced form) that satisfy I(N ) < r/s < I(piN ) for some prime divisor pi of a positive
integer N . To be more speciﬁc, keeping Properties 2.1 and 2.2 in mind, we look for those
values of s having divisors that lead to abundancy values exceeding I(piN ).

Theorem 3.2. Let r/s > 1 be a fraction in lowest terms such that there exists a divisor
N = ∏n
i=1 pki
i of s satisfying the following two conditions:

1. r/s < I(piN ) for all i ≤ n

2. The product σ(N )(s/N ) has a divisor M such that (M, r) = 1 and I(M ) ≥ σ(pkj +1
j )

σ(pkj +1
j )−1
for some positive integer j ≤ n.

Then r/s is an abundancy outlaw.

Proof. Let r/s > 1 be a fraction in lowest terms satisfying the above hypotheses. Suppose
that I(x) = r/s for some natural number x. Since r/s is in lowest terms, Property 2.2
ensures that s|x. Then, because N |s, N |x, and therefore, x = dN for some positive integer
d. However, since r/s < I(piN ) for 1 ≤ i ≤ n, the ﬁrst assumption requires that pki+1
i ∤ x
for all 1 ≤ i ≤ n, and thus, d is relatively prime to N .
Consequently, we can write

I(x) = I(dN ) = I(d)I(N ) = r
s .

Hence, σ(d)σ(N )(s/N ) = rd.

Now, by the second assumption, we know that there exists a positive integer M such that

M |σ(N )(s/N )

and M is relatively prime to r. Therefore, M |d and we can say that

I(x) = I(d)I(N ) ≥ I(M )I(N )

by Property 2.1. Then, by assumption 2) and Lemma 3.1,

I(M ) ≥ σ(pkj +1
j )

σ(pkj +1
j ) − 1 = σ(pjN )
pjσ(N )

for some 1 ≤ j ≤ n, so we know that

I(x) ≥ I(M )I(N ) ≥ σ(pjN )
pjσ(N ) σ(N )
N = σ(pjN )
pjN = I(pjN )

Therefore, I(x) ≥ I(pjN ), which contradicts our assumption that I(x) = r/s < I(piN ) for
all 1 ≤ i ≤ n. We conclude, then, that r/s is an abundancy outlaw.

4

Example 3.3. Theorem 3.2 can be used to show that 37/22 is an abundancy outlaw. Cer-
tainly 37/22 < I(22) = 7/4. Thus, assumption 1) is satisﬁed for N = 2. Next, note that
M = 3 divides σ(2) · (22/2), and because gcd(3, 37) = 1, with I(3) > σ(4)
σ(4)−1 = 7/6, assump-
tion 2) is satisﬁed as well. A computer search reveals many more examples. (See Table
3.4)
 Abundancy
outlaw r/s s σ(s)
29/12 22 · 3 28
37/22 2 · 11 36
43/20 22 · 5 42
43/26 2 · 13 42
55/34 2 · 17 54
59/34 2 · 17 54
61/24 23 · 3 60
61/38 2 · 19 60
65/38 2 · 19 60
73/30 2 · 3 · 5 72
73/46 2 · 23 72
73/51 3 · 17 72
77/46 2 · 23 72
79/45 32 · 5 78
79/46 2 · 23 72
91/40 23 · 5 90
91/58 2 · 29 90
95/58 2 · 29 90
97/42 2 · 3 · 7 96
97/58 2 · 29 90
97/62 2 · 31 96
97/69 3 · 23 96
101/58 2 · 29 90
101/62 2 · 31 96
103/62 2 · 31 96
107/62 2 · 31 96
115/74 2 · 37 114
119/74 2 · 37 114
121/56 23 · 7 120
121/74 2 · 37 114
121/87 3 · 29 120
125/48 24 · 3 124
 Abundancy
outlaw r/s s σ(s)
125/74 2 · 37 114
125/87 3 · 29 120
127/68 22 · 17 126
127/74 2 · 37 114
127/82 2 · 41 126
131/82 2 · 41 126
131/93 3 · 31 128
133/82 2 · 41 126
133/86 2 · 43 132
133/93 3 · 31 128
137/82 2 · 41 126
137/86 2 · 43 132
139/82 2 · 41 126
139/86 2 · 43 132
141/76 22 · 19 140
143/82 2 · 41 126
143/86 2 · 43 132
145/66 2 · 3 · 11 144
145/86 2 · 43 132
145/94 2 · 47 144
149/86 2 · 43 132
149/94 2 · 47 144
151/94 2 · 47 144
155/94 2 · 47 144
155/111 3 · 37 152
157/94 2 · 47 144
157/99 32 · 11 156
157/111 3 · 37 152
161/94 2 · 47 144
163/94 2 · 47 144
163/106 2 · 53 162
167/106 2 · 53 162

Table 3.4: A list of abundancy outlaws found using Theorem 3.2. These outlaws are
captured by Theorem 3.2, but not by Property 2.3.

5

4 The main results

Table 3.4 reveals some recognizable patterns. Most obvious is the indication that, for small
odd values of t (and p prime), reduced rational numbers of the form

r
s = σ(2mpn) + t
2mpn

often lead to abundancy outlaws. In fact, the results of this section will show that σ(2mp2n+1)+1
2mp2n+1
is an abundancy outlaw whenever gcd(p, σ(2m)) = 1. In particular, if p > 3, then (σ(2p) +
1)/(2p) is always an abundancy outlaw. Our main result, however, will address the more
general situation where r/s is a reduced rational number of the form (σ(N ) + t)/N . First
we will need a lemma.

Lemma 4.1. Let N = ∏n
i=1 pki
i , where pi is a prime for all 1 ≤ i ≤ n. Then, for a given
1 ≤ j ≤ n and a positive integer t,
 pj < 1
t σ
 ( N

pkj
j
 )

if and only if σ(N ) + t
N < I(pjN ).

Proof. Assume that σ(N ) + t
N < I(pjN )

for a given natural number j ≤ n. This is equivalent to

pjσ(N ) + pjt < σ(pjN ).

Then, since pjσ(pkj
j ) = σ(pkj +1
j ) − 1, we ﬁnd that this inequality is equivalent to

(σ(pkj +1
j ) − 1)σ (
 N

pkj
j
 ) + pjt < σ(pjN ),

or
 σ(pjN ) − σ (
 N

pkj
j
 ) + pjt < σ(pjN ).

Therefore,
 pj < 1
t σ
 ( N

pkj
j
 )
 .

We are now ready to present the main result.

6

Theorem 4.2. For a positive integer t, let σ(N )+t
N be a fraction in lowest terms, and let
N = ∏n
i=1 pki
i for primes p1, p2, ..., pn. If there exists a positive integer j ≤ n such that
pj < 1
t σ(N/pkj
j ) and σ(pkj
j ) has a divisor D > 1 such that at least one of the following is
true:

1. I(pkj
j )I(D) > σ(N )+t
N and gcd(D, t) = 1

2. gcd(D, N t) = 1

then σ(N )+t
N is an abundancy outlaw.

Proof. Case 1: Let N and t be natural numbers such that σ(N )+t
N is a fraction in lowest
terms, and let j ≤ n be a natural number satisfying pj < 1
t σ(N/pkj
j ) and D a divisor
of σ(pkj
j ) satisfying hypothesis (1). Suppose further that I(x) = σ(N )+t
N for some natural
number x. Since (σ(N ) + t, N ) = 1, N |x by Property 2.2. Say x = dN , where d is a positive
integer. Since pj satisﬁes pj < 1
t σ(N/pkj
j ), Lemma 4.1 implies that I(x) = σ(N )+t
N < I(pjN ).
Hence, gcd(pkj
j , dN/pkj
j ) = 1 and

I(x) = I(pkj
j )I(dN/pkj
j ) = σ(N ) + t
N .

Equivalently, σ(pkj
j )σ(dN/pkj
j ) = (σ(N ) + t)d.

Since σ(pkj
j )|σ(N ) and gcd(D, t) = 1, the divisor D of σ(pkj
j ) satisfying hypothesis (1)
also divides d. Hence D divides dN/pkj
j , and by Property 2.1, I(D) ≤ I(dN/pkj
j ). Thus

I(pkj
j )I(D) ≤ I(pkj
j )I(dN/pkj
j ) = I(x).

Given I(x) = σ(N )+t
N , we conclude then that

I(pkj
j )I(D) ≤ σ(N ) + t
N .

This contradicts the assumption that I(pkj
j )I(D) > σ(N )+t
N . Therefore, σ(N )+t
N is an abun-
dancy outlaw.

Case 2: Now let N = ∏n
i=1 pki
i and t be natural numbers such that σ(pj)kj has a divisor
D satisfying hypothesis (2) for some 1 ≤ j ≤ n, and assume that I(x) = σ(N )+t
N for some
natural number x. Since σ(N )+t
N is in lowest terms, N |x, so that x = sN for some natural
number s. By assumption, there exists a natural number j ≤ n so that pj < 1
t σ(N/pkj
j ). By
Lemma 4.1, I(x) = σ(N )+t
N < I(pjN ). Hence, pj ∤ s, so that

I(x) = I (pkj
j s N

pkj
j
 )

= I(pkj
j )I (
s N

pkj
j
 ) .

7

Next, we factor out the part of s, ∏n
i=1 pγi
i , that has divisors in common with N/pkj
j , so that

s = s
∏n
i=1 pγi
i ,

where γi is a non-negative integer for all i ≤ n.
Then, we can rewrite I(x) once more in the following form:

I(x) = I(pkj
j )I(s)I
 ( N

pkj
j
 n∏

i=1 pγi
i
 )

Because I(x) = σ(N )+t
N , we can see, then, that

I(pkr
r )I(s)I ( N
pkr
r ∏n
i=1 pγi
i ) = σ(N )+t
N ,

or equivalently,
 σ(pkr
r )σ(s)σ ( N
pkr
r ∏n
i=1 pγi
i ) = (σ(N ) + t)s ∏n
i=1 pγi
i .

Now consider the divisor D of σ(pkj
j ) satisfying hypothesis (2). Since σ(pkj
j )|σ(N ) and
gcd(D, N t) = 1, D divides s (so s > 1). This, then, means that I(s) ≥ I(D). Then,
since pj < 1
t σ(N/pkj
j ),
 pjσ(pkj
j ) < 1
t σ(N ),

which implies that the following is true:
 1

pjσ(pkj
j ) > t
σ(N ).

Thus, since D|σ(pkj
j ), D < pjσ(pkj
j ), so that 1/D > 1/pjσ(pkj
j ).
Hence, the following are true:

I(s) ≥ I(D)

≥ 1 + 1
D

> 1 + 1

pjσ(pkj
j )

> 1 + t
σ(N )

= σ(N ) + t
σ(N )

= σ(N ) + t

I(pkj
j )I(N/pkj
j )N

≥ σ(N ) + t

I(pkj
j )I((N/pkj
j ) ∏n
i=1 pγi
i )N .

8

Hence
 I(pkj
j )I(s)I
 ( N

pkj
j
 n∏

i=1 pγi
i
 )
 = I(x) > σ(N ) + t
N ,

which contradicts our original assumption that I(x) = σ(N )+t
N . Thus, σ(N )+t
N is an abundancy
outlaw.

If t = 1 we get the following corollary.

Corollary 4.3. Let σ(N )+1
N be a fraction in lowest terms, and let N = ∏n
i=1 pki
i for primes
p1, p2, ..., pn. If there exists a natural number j ≤ n such that pj < σ(N/pkj
j ) and σ(pkj
j ) has
a divisor D such that at least one of the following is true:

1. I(pkj
j )I(D) > σ(N )+1
N

2. gcd(D, N ) = 1

then σ(N )+1
N is an abundancy outlaw.

5 Constructing Sequences of Abundancy Outlaws

Using the results in the previous section, we can ﬁnd and construct sequences of abundancy
outlaws. The following lemma will be helpful.

Lemma 5.1. Let N = ∏n
i=1 pki
i for primes p1, p2, ..., pn. Then N is relatively prime to
σ(N ) + 1 if and only if pi is relatively prime to σ(N/pki
i ) + 1 for all 1 ≤ i ≤ n.

Proof. Since σ(pki
i ) ≡ 1 (mod pi),

σ(N ) + 1 = σ(pki
i )σ(N/pki
i ) + 1
≡ σ(N/pki
i ) + 1 (mod pi).

Thus, any prime divisor pi of N and σ(N ) + 1 must also be a prime divisor of σ(N/pki
i ) + 1,
and conversely, if pi|(σ(N/pki
i ) + 1), then pi divides both N and σ(N ) + 1.

Outlaws with even denominators

Corollary 5.2. For all natural numbers m and nonnegative integers n, and for all odd
primes p such that gcd(p, σ(2m)) = 1, the rational number

σ(2mp2n+1) + 1
2mp2n+1

is an abundancy outlaw.
 9

Proof. To see that (σ(2mp2n+1)+1)/2mp2n+1 is in lowest terms, apply Lemma 5.1. Since p and
2n+1 are odd, σ(p2n+1)+1 is odd, so gcd(2m, σ(p2n+1)+1) = 1. Also, gcd(p2n+1, σ(2m)+1) =
1, because σ(2m) + 1 = 2m+1. Next, we apply Corollary 4.3. Since 2 < σ(p2n+1), we consider
divisors D of σ(2m). Clearly, gcd(σ(2m), 2m) = 1, and because p does not divide σ(2m),
gcd(σ(2m), 2mp2n+1) = 1. Hence, D = σ(2m) is the divisor required to apply Corollary 4.3.
Thus, (σ(2mp2n+1))/2mp2n+1 is an abundancy outlaw.

Corollary 5.3. For all primes p > 3,
 σ(2p) + 1
2p

is an abundancy outlaw. If p = 2 or p = 3 then σ(2p)+1
2p is an abundancy index.

Proof. This result follows directly from Corollary 5.2. To prove that σ(2p)+1
2p is an abundancy

index when p = 2 and p = 3, note that I(6) = σ(22)+1
22 and I(18) = σ(6)+1
6 .

Remark 5.4. Corollary 5.3 actually has a very simple proof (and in fact, the results presented
in section 4 represent our attempt to push this simple proof as far as possible). Clearly,
(σ(2p) + 1)/(2p) = (3p + 4)/(2p) is in lowest terms. Thus, if I(N ) = (σ(2p) + 1)/2p, 2p|N .
Because p > 3, it can be shown that I(4p) > (σ(2p) + 1)/2p, so 4 ∤ N . Therefore, σ(2)|σ(N ),
and since σ(2) = 3 does not divide σ(2p) + 1, 3 divides N . Hence, I(N ) > I(6p) > 2 >
(σ(2p) + 1)/2p. This is a contradiction, so (σ(2p) + 1)/2p is an abundancy outlaw, and we
have captured the following sequence of outlaws:

19
10 , 25
14 , 37
22 , 43
26 , 55
34 , 61
38 , 73
46 , 91
58 , 97
62 , 115
74 , 127
82 , 133
86 , 145
94 , 163
106 , 181
118 , 187
122 , ...

Corollary 5.3 also captures another (potentially inﬁnite) set of outlaws having even de-
nominators...

Corollary 5.5. If N is an even perfect number,

σ(2N ) + 1
2N

is an abundancy outlaw.

Proof. Since N is an even perfect number, N = 2p−1(2p − 1), where p and 2p − 1 are both
prime. Hence, 2N = 2p(2p − 1).

Applying Corollary 5.2, we need only show that gcd(2p − 1, σ(2p)) = 1. This follows from
the fact that 2(2p − 1) = (2p+1 − 1) − 1,

which is clearly relatively prime to σ(2p) = 2p+1 − 1. Therefore, (σ(2N ) + 1)/2N is an
abundancy outlaw.
 10

Outlaws with odd denominators

Corollary 5.6. Let M be an odd natural number, and let p, α, and t be odd natural numbers
such that p ∤ M and p < 1
t σ(M ). Then, if (σ(pαM ) + t)/pαM is in lowest terms,

σ(pαM ) + t
pαM

is an abundancy outlaw.

Proof. Since (σ(pαM ) + t)/pαM is in lowest terms, we apply Theorem 4.2 to show that it
is an abundancy outlaw. Since p and α are both odd, σ(pα) is even. Hence, D = 2 divides
σ(pα), and since p, M , and t are all odd, gcd(D, pM t) = 1. Thus, (σ(pαM ) + t)/pαM is an
abundancy outlaw.

Corollary 5.7. For primes p and q, with 3 < q, p < q, and gcd(p, q + 2) = gcd(q, p + 2) = 1,

σ(pq) + 1
pq

is an abundancy outlaw.

Proof. The case for p = 2 follows from Corollary 5.3. Now suppose that q > p > 2. In this
case, neither p nor q divides σ(pq)+1 = pq+p+q+2, because gcd(p, q+2) = gcd(q, p+2) = 1.
Thus, σ(pq)+1
pq is in lowest terms. The result now follows from Corollary 5.6.

Corollary 5.7 produces outlaws with ease. To illustrate, let p and q be odd primes with
3 < p < q, and assume q ≡ 1 (mod p). Then p ∤ q + 2 and q ∤ p + 2. Since Dirichlet’s theorem
on arithmetic progressions of primes ensures the existence of an inﬁnite sequence of primes
q satisfying q ≡ 1 (mod p), Corollary 5.7 reveals an inﬁnite class of outlaws corresponding
to each odd prime p > 3. The sequences corresponding to the primes 5, 7, and 11 follow.

p = 5 : 73
55 , 193
155 , 253
205 , 373
305 , 433
355 , 613
505 , 793
655 , 913
755 , 1093
905 , 1153
955 , 1273
1055 , 1513
1255 , 1633
1355 , 1693
1405 , 1873
1555 , 1993
1655 , 2413
2005 , 2533
2105 , ...

p = 7 : 241
203 , 353
301 , 577
497 , 913
791 , 1025
889 , 1585
1379 , 1697
1477 , 1921
1673 , 2257
1967 , 2705
2359 , 3041
2653 , 3377
2947 , 3601
3143 , 3713
3241 , 3937
3437 , 4385
3829 , 4945
4319 , ...

p = 11 : 289
253 , 817
737 , 1081
979 , 2401
2189 , 3985
3641 , 4249
3883 , 4777
4367 , 5041
4609 , 5569
5093 , 7417
6787 , 7945
7271 , 8209
7513 , 8737
7997 , 10321
9449 , 10585
9691 , 11377
10417 , ...

Remark 5.8. It is interesting to note that if p and q = p + 2 are twin primes then Corollary
5.7 does not apply, and in this case

σ(p(p + 2)) + 1
p(p + 2) = σ(p) + 1
p = p + 2
p .

Once again, we are faced with that elusive ratio p+2
p !

11

6 Further explorations

R. Ryan considered the equation
 I(x) = p + 2
p = σ(p) + 1
p , (6.1)

where p is an odd prime [4]. Whether or not a solution x exists is still an open question.
This problem is interesting for two reasons. First, p+2
p is just barely out of reach of Weiner’s
2000 result, since p + 2 = σ(p) + 1 for all primes p. Second, as we have already mentioned,
if 5
3 = 3+2
3 is an abundancy index then there exists an odd perfect number.
It seems to be just as diﬃcult to ﬁnd a solution to the above equation as it is to show
that no such x exists. R. Ryan reports that I(x) = p+2
p has no solution for x < 1016 [4].
The investigations that led us to Theorems 3.2 and 4.2 were motivated in part by a desire to
show that equation 5.1 has no solutions. However, p+2
p has proven to be an elusive fraction.
The techniques we have employed in this paper cannot be applied to it. The diﬃculty lies
in the fact that p + 2
p > p
p − 1 > I(pα)

for all primes p and natural numbers α. Thus, one can never “trap” p+2
p between two
numbers: I(pαN ) < p + 2
p < I(pα+1N ).

Hence, Theorems 3.2 and 4.2 fail to capture this potential outlaw. In fact, proving that
p+2
p is an abundancy outlaw seems to require the discovery of an entirely new category of
abundancy outlaws.

There are also many interesting questions to consider relating to the size of these sets
of abundancy outlaws, in the sense of asymptotic density. Based on some preliminary com-
puter experiments, the proportion of outlaws captured by Theorem 4.2 seems to approach
1.7 percent. See the appendix for empirical data. Our future work will involve a deeper
exploration of the sizes of the sets of outlaws, indices, and rationals of unknown status.

7 Appendix

The following is a table containing empirical data relating to the asymptotic density of the
set of outlaws captured by Theorem 3.4. The second and third columns give the number of
outlaws with numerators less than or equal to n captured by Theorem 3.4 and Proposition
2.3, respectively. The fourth column gives the number of rationals in the image of the
abundancy index of the ﬁrst one million natural numbers with numerators less than or equal
to n. The ﬁfth column gives the total number of rationals with numerators less than or
equal to n, and the sixth column gives the value of column 2 divided by column 5. In other
words, the sixth column gives the proportion of outlaws captured by Theorem 3.4 in the set
of rationals with numerator less than or equal to n.

12

n Thm. 3.4 Prop. 2.3 Abundancy Index Total rationals Proportion
10 0 4 20 32 0
100 44 720 553 3044 0.0145
1000 5170 74927 7803 304192 0.01700
10000 518193 750174 62064 30397486 0.01705

Table 7.1: A table of empirical data on the asymptotic densities of the abundancy out-
laws and the abundancy indices.

As a way to visualize the distribution of abundancy outlaws, we include a list of the
rationals with numerators less than or equal to 100 (under the ordering described in the
introduction). Each rational number q is colored according to its abundancy index/outlaw
status:

• Blue: q is in the image of the abundancy index of the ﬁrst one million natural numbers,
or a natural number from 2 to 11 (the abundancy index of a known multiperfect
number)

• Green: q is an outlaw captured by Property 2.3.

• Red: q is an outlaw captured by Theorem 4.2.

• Black: q is not in any of the other categories (the outlaw status of q is “unknown”)

In the following list, 450 rationals are blue, 720 are green, 44 are red, and 1961 are black.

2, 3, 3/2, 4, 4/3, 5, 5/2, 5/3, 5/4, 6, 6/5, 7, 7/2, 7/3, 7/4, 7/5, 7/6, 8, 8/3, 8/5, 8/7,
9, 9/2, 9/4, 9/5, 9/7, 9/8, 10, 10/3, 10/7, 10/9, 11, 11/2, 11/3, 11/4, 11/5, 11/6, 11/7,
11/8, 11/9, 11/10, 12, 12/5, 12/7, 12/11, 13, 13/2, 13/3, 13/4, 13/5, 13/6, 13/7, 13/8,
13/9, 13/10, 13/11, 13/12, 14, 14/3, 14/5, 14/9, 14/11, 14/13, 15, 15/2, 15/4, 15/7, 15/8,
15/11, 15/13, 15/14, 16, 16/3, 16/5, 16/7, 16/9, 16/11, 16/13, 16/15, 17, 17/2, 17/3, 17/4,
17/5, 17/6, 17/7, 17/8, 17/9, 17/10, 17/11, 17/12, 17/13, 17/14, 17/15, 17/16, 18, 18/5,
18/7, 18/11, 18/13, 18/17, 19, 19/2, 19/3, 19/4, 19/5, 19/6, 19/7, 19/8, 19/9, 19/10, 19/11,
19/12, 19/13, 19/14, 19/15, 19/16, 19/17, 19/18, 20, 20/3, 20/7, 20/9, 20/11, 20/13, 20/17,
20/19, 21, 21/2, 21/4, 21/5, 21/8, 21/10, 21/11, 21/13, 21/16, 21/17, 21/19, 21/20, 22,
22/3, 22/5, 22/7, 22/9, 22/13, 22/15, 22/17, 22/19, 22/21, 23, 23/2, 23/3, 23/4, 23/5,
23/6, 23/7, 23/8, 23/9, 23/10, 23/11, 23/12, 23/13, 23/14, 23/15, 23/16, 23/17, 23/18,
23/19, 23/20, 23/21, 23/22, 24, 24/5, 24/7, 24/11, 24/13, 24/17, 24/19, 24/23, 25, 25/2,
25/3, 25/4, 25/6, 25/7, 25/8, 25/9, 25/11, 25/12, 25/13, 25/14, 25/16, 25/17, 25/18, 25/19,
25/21, 25/22, 25/23, 25/24, 26, 26/3, 26/5, 26/7, 26/9, 26/11, 26/15, 26/17, 26/19, 26/21,
26/23, 26/25, 27, 27/2, 27/4, 27/5, 27/7, 27/8, 27/10, 27/11, 27/13, 27/14, 27/16, 27/17,
27/19, 27/20, 27/22, 27/23, 27/25, 27/26, 28, 28/3, 28/5, 28/9, 28/11, 28/13, 28/15, 28/17,
28/19, 28/23, 28/25, 28/27, 29, 29/2, 29/3, 29/4, 29/5, 29/6, 29/7, 29/8, 29/9, 29/10,
29/11, 29/12, 29/13, 29/14, 29/15, 29/16, 29/17, 29/18, 29/19, 29/20, 29/21, 29/22, 29/23,

13

29/24, 29/25, 29/26, 29/27, 29/28, 30, 30/7, 30/11, 30/13, 30/17, 30/19, 30/23, 30/29, 31,
31/2, 31/3, 31/4, 31/5, 31/6, 31/7, 31/8, 31/9, 31/10, 31/11, 31/12, 31/13, 31/14, 31/15,
31/16, 31/17, 31/18, 31/19, 31/20, 31/21, 31/22, 31/23, 31/24, 31/25, 31/26, 31/27, 31/28,
31/29, 31/30, 32, 32/3, 32/5, 32/7, 32/9, 32/11, 32/13, 32/15, 32/17, 32/19, 32/21, 32/23,
32/25, 32/27, 32/29, 32/31, 33, 33/2, 33/4, 33/5, 33/7, 33/8, 33/10, 33/13, 33/14, 33/16,
33/17, 33/19, 33/20, 33/23, 33/25, 33/26, 33/28, 33/29, 33/31, 33/32, 34, 34/3, 34/5, 34/7,
34/9, 34/11, 34/13, 34/15, 34/19, 34/21, 34/23, 34/25, 34/27, 34/29, 34/31, 34/33, 35, 35/2,
35/3, 35/4, 35/6, 35/8, 35/9, 35/11, 35/12, 35/13, 35/16, 35/17, 35/18, 35/19, 35/22, 35/23,
35/24, 35/26, 35/27, 35/29, 35/31, 35/32, 35/33, 35/34, 36, 36/5, 36/7, 36/11, 36/13, 36/17,
36/19, 36/23, 36/25, 36/29, 36/31, 36/35, 37, 37/2, 37/3, 37/4, 37/5, 37/6, 37/7, 37/8, 37/9,
37/10, 37/11, 37/12, 37/13, 37/14, 37/15, 37/16, 37/17, 37/18, 37/19, 37/20, 37/21, 37/22,
37/23, 37/24, 37/25, 37/26, 37/27, 37/28, 37/29, 37/30, 37/31, 37/32, 37/33, 37/34, 37/35,
37/36, 38, 38/3, 38/5, 38/7, 38/9, 38/11, 38/13, 38/15, 38/17, 38/21, 38/23, 38/25, 38/27,
38/29, 38/31, 38/33, 38/35, 38/37, 39, 39/2, 39/4, 39/5, 39/7, 39/8, 39/10, 39/11, 39/14,
39/16, 39/17, 39/19, 39/20, 39/22, 39/23, 39/25, 39/28, 39/29, 39/31, 39/32, 39/34, 39/35,
39/37, 39/38, 40, 40/3, 40/7, 40/9, 40/11, 40/13, 40/17, 40/19, 40/21, 40/23, 40/27, 40/29,
40/31, 40/33, 40/37, 40/39, 41, 41/2, 41/3, 41/4, 41/5, 41/6, 41/7, 41/8, 41/9, 41/10, 41/11,
41/12, 41/13, 41/14, 41/15, 41/16, 41/17, 41/18, 41/19, 41/20, 41/21, 41/22, 41/23, 41/24,
41/25, 41/26, 41/27, 41/28, 41/29, 41/30, 41/31, 41/32, 41/33, 41/34, 41/35, 41/36, 41/37,
41/38, 41/39, 41/40, 42, 42/5, 42/11, 42/13, 42/17, 42/19, 42/23, 42/25, 42/29, 42/31,
42/37, 42/41, 43, 43/2, 43/3, 43/4, 43/5, 43/6, 43/7, 43/8, 43/9, 43/10, 43/11, 43/12,
43/13, 43/14, 43/15, 43/16, 43/17, 43/18, 43/19, 43/20, 43/21, 43/22, 43/23, 43/24, 43/25,
43/26, 43/27, 43/28, 43/29, 43/30, 43/31, 43/32, 43/33, 43/34, 43/35, 43/36, 43/37, 43/38,
43/39, 43/40, 43/41, 43/42, 44, 44/3, 44/5, 44/7, 44/9, 44/13, 44/15, 44/17, 44/19, 44/21,
44/23, 44/25, 44/27, 44/29, 44/31, 44/35, 44/37, 44/39, 44/41, 44/43, 45, 45/2, 45/4, 45/7,
45/8, 45/11, 45/13, 45/14, 45/16, 45/17, 45/19, 45/22, 45/23, 45/26, 45/28, 45/29, 45/31,
45/32, 45/34, 45/37, 45/38, 45/41, 45/43, 45/44, 46, 46/3, 46/5, 46/7, 46/9, 46/11, 46/13,
46/15, 46/17, 46/19, 46/21, 46/25, 46/27, 46/29, 46/31, 46/33, 46/35, 46/37, 46/39, 46/41,
46/43, 46/45, 47, 47/2, 47/3, 47/4, 47/5, 47/6, 47/7, 47/8, 47/9, 47/10, 47/11, 47/12, 47/13,
47/14, 47/15, 47/16, 47/17, 47/18, 47/19, 47/20, 47/21, 47/22, 47/23, 47/24, 47/25, 47/26,
47/27, 47/28, 47/29, 47/30, 47/31, 47/32, 47/33, 47/34, 47/35, 47/36, 47/37, 47/38, 47/39,
47/40, 47/41, 47/42, 47/43, 47/44, 47/45, 47/46, 48, 48/5, 48/7, 48/11, 48/13, 48/17, 48/19,
48/23, 48/25, 48/29, 48/31, 48/35, 48/37, 48/41, 48/43, 48/47, 49, 49/2, 49/3, 49/4, 49/5,
49/6, 49/8, 49/9, 49/10, 49/11, 49/12, 49/13, 49/15, 49/16, 49/17, 49/18, 49/19, 49/20,
49/22, 49/23, 49/24, 49/25, 49/26, 49/27, 49/29, 49/30, 49/31, 49/32, 49/33, 49/34, 49/36,
49/37, 49/38, 49/39, 49/40, 49/41, 49/43, 49/44, 49/45, 49/46, 49/47, 49/48, 50, 50/3, 50/7,
50/9, 50/11, 50/13, 50/17, 50/19, 50/21, 50/23, 50/27, 50/29, 50/31, 50/33, 50/37, 50/39,
50/41, 50/43, 50/47, 50/49, 51, 51/2, 51/4, 51/5, 51/7, 51/8, 51/10, 51/11, 51/13, 51/14,
51/16, 51/19, 51/20, 51/22, 51/23, 51/25, 51/26, 51/28, 51/29, 51/31, 51/32, 51/35, 51/37,
51/38, 51/40, 51/41, 51/43, 51/44, 51/46, 51/47, 51/49, 51/50, 52, 52/3, 52/5, 52/7, 52/9,
52/11, 52/15, 52/17, 52/19, 52/21, 52/23, 52/25, 52/27, 52/29, 52/31, 52/33, 52/35, 52/37,
52/41, 52/43, 52/45, 52/47, 52/49, 52/51, 53, 53/2, 53/3, 53/4, 53/5, 53/6, 53/7, 53/8,
53/9, 53/10, 53/11, 53/12, 53/13, 53/14, 53/15, 53/16, 53/17, 53/18, 53/19, 53/20, 53/21,
53/22, 53/23, 53/24, 53/25, 53/26, 53/27, 53/28, 53/29, 53/30, 53/31, 53/32, 53/33, 53/34,

14

53/35, 53/36, 53/37, 53/38, 53/39, 53/40, 53/41, 53/42, 53/43, 53/44, 53/45, 53/46, 53/47,
53/48, 53/49, 53/50, 53/51, 53/52, 54, 54/5, 54/7, 54/11, 54/13, 54/17, 54/19, 54/23, 54/25,
54/29, 54/31, 54/35, 54/37, 54/41, 54/43, 54/47, 54/49, 54/53, 55, 55/2, 55/3, 55/4, 55/6,
55/7, 55/8, 55/9, 55/12, 55/13, 55/14, 55/16, 55/17, 55/18, 55/19, 55/21, 55/23, 55/24,
55/26, 55/27, 55/28, 55/29, 55/31, 55/32, 55/34, 55/36, 55/37, 55/38, 55/39, 55/41, 55/42,
55/43, 55/46, 55/47, 55/48, 55/49, 55/51, 55/52, 55/53, 55/54, 56, 56/3, 56/5, 56/9, 56/11,
56/13, 56/15, 56/17, 56/19, 56/23, 56/25, 56/27, 56/29, 56/31, 56/33, 56/37, 56/39, 56/41,
56/43, 56/45, 56/47, 56/51, 56/53, 56/55, 57, 57/2, 57/4, 57/5, 57/7, 57/8, 57/10, 57/11,
57/13, 57/14, 57/16, 57/17, 57/20, 57/22, 57/23, 57/25, 57/26, 57/28, 57/29, 57/31, 57/32,
57/34, 57/35, 57/37, 57/40, 57/41, 57/43, 57/44, 57/46, 57/47, 57/49, 57/50, 57/52, 57/53,
57/55, 57/56, 58, 58/3, 58/5, 58/7, 58/9, 58/11, 58/13, 58/15, 58/17, 58/19, 58/21, 58/23,
58/25, 58/27, 58/31, 58/33, 58/35, 58/37, 58/39, 58/41, 58/43, 58/45, 58/47, 58/49, 58/51,
58/53, 58/55, 58/57, 59, 59/2, 59/3, 59/4, 59/5, 59/6, 59/7, 59/8, 59/9, 59/10, 59/11, 59/12,
59/13, 59/14, 59/15, 59/16, 59/17, 59/18, 59/19, 59/20, 59/21, 59/22, 59/23, 59/24, 59/25,
59/26, 59/27, 59/28, 59/29, 59/30, 59/31, 59/32, 59/33, 59/34, 59/35, 59/36, 59/37, 59/38,
59/39, 59/40, 59/41, 59/42, 59/43, 59/44, 59/45, 59/46, 59/47, 59/48, 59/49, 59/50, 59/51,
59/52, 59/53, 59/54, 59/55, 59/56, 59/57, 59/58, 60, 60/7, 60/11, 60/13, 60/17, 60/19,
60/23, 60/29, 60/31, 60/37, 60/41, 60/43, 60/47, 60/49, 60/53, 60/59, 61, 61/2, 61/3, 61/4,
61/5, 61/6, 61/7, 61/8, 61/9, 61/10, 61/11, 61/12, 61/13, 61/14, 61/15, 61/16, 61/17, 61/18,
61/19, 61/20, 61/21, 61/22, 61/23, 61/24, 61/25, 61/26, 61/27, 61/28, 61/29, 61/30, 61/31,
61/32, 61/33, 61/34, 61/35, 61/36, 61/37, 61/38, 61/39, 61/40, 61/41, 61/42, 61/43, 61/44,
61/45, 61/46, 61/47, 61/48, 61/49, 61/50, 61/51, 61/52, 61/53, 61/54, 61/55, 61/56, 61/57,
61/58, 61/59, 61/60, 62, 62/3, 62/5, 62/7, 62/9, 62/11, 62/13, 62/15, 62/17, 62/19, 62/21,
62/23, 62/25, 62/27, 62/29, 62/33, 62/35, 62/37, 62/39, 62/41, 62/43, 62/45, 62/47, 62/49,
62/51, 62/53, 62/55, 62/57, 62/59, 62/61, 63, 63/2, 63/4, 63/5, 63/8, 63/10, 63/11, 63/13,
63/16, 63/17, 63/19, 63/20, 63/22, 63/23, 63/25, 63/26, 63/29, 63/31, 63/32, 63/34, 63/37,
63/38, 63/40, 63/41, 63/43, 63/44, 63/46, 63/47, 63/50, 63/52, 63/53, 63/55, 63/58, 63/59,
63/61, 63/62, 64, 64/3, 64/5, 64/7, 64/9, 64/11, 64/13, 64/15, 64/17, 64/19, 64/21, 64/23,
64/25, 64/27, 64/29, 64/31, 64/33, 64/35, 64/37, 64/39, 64/41, 64/43, 64/45, 64/47, 64/49,
64/51, 64/53, 64/55, 64/57, 64/59, 64/61, 64/63, 65, 65/2, 65/3, 65/4, 65/6, 65/7, 65/8,
65/9, 65/11, 65/12, 65/14, 65/16, 65/17, 65/18, 65/19, 65/21, 65/22, 65/23, 65/24, 65/27,
65/28, 65/29, 65/31, 65/32, 65/33, 65/34, 65/36, 65/37, 65/38, 65/41, 65/42, 65/43, 65/44,
65/46, 65/47, 65/48, 65/49, 65/51, 65/53, 65/54, 65/56, 65/57, 65/58, 65/59, 65/61, 65/62,
65/63, 65/64, 66, 66/5, 66/7, 66/13, 66/17, 66/19, 66/23, 66/25, 66/29, 66/31, 66/35, 66/37,
66/41, 66/43, 66/47, 66/49, 66/53, 66/59, 66/61, 66/65, 67, 67/2, 67/3, 67/4, 67/5, 67/6,
67/7, 67/8, 67/9, 67/10, 67/11, 67/12, 67/13, 67/14, 67/15, 67/16, 67/17, 67/18, 67/19,
67/20, 67/21, 67/22, 67/23, 67/24, 67/25, 67/26, 67/27, 67/28, 67/29, 67/30, 67/31, 67/32,
67/33, 67/34, 67/35, 67/36, 67/37, 67/38, 67/39, 67/40, 67/41, 67/42, 67/43, 67/44, 67/45,
67/46, 67/47, 67/48, 67/49, 67/50, 67/51, 67/52, 67/53, 67/54, 67/55, 67/56, 67/57, 67/58,
67/59, 67/60, 67/61, 67/62, 67/63, 67/64, 67/65, 67/66, 68, 68/3, 68/5, 68/7, 68/9, 68/11,
68/13, 68/15, 68/19, 68/21, 68/23, 68/25, 68/27, 68/29, 68/31, 68/33, 68/35, 68/37, 68/39,
68/41, 68/43, 68/45, 68/47, 68/49, 68/53, 68/55, 68/57, 68/59, 68/61, 68/63, 68/65, 68/67,
69, 69/2, 69/4, 69/5, 69/7, 69/8, 69/10, 69/11, 69/13, 69/14, 69/16, 69/17, 69/19, 69/20,
69/22, 69/25, 69/26, 69/28, 69/29, 69/31, 69/32, 69/34, 69/35, 69/37, 69/38, 69/40, 69/41,

15

69/43, 69/44, 69/47, 69/49, 69/50, 69/52, 69/53, 69/55, 69/56, 69/58, 69/59, 69/61, 69/62,
69/64, 69/65, 69/67, 69/68, 70, 70/3, 70/9, 70/11, 70/13, 70/17, 70/19, 70/23, 70/27, 70/29,
70/31, 70/33, 70/37, 70/39, 70/41, 70/43, 70/47, 70/51, 70/53, 70/57, 70/59, 70/61, 70/67,
70/69, 71, 71/2, 71/3, 71/4, 71/5, 71/6, 71/7, 71/8, 71/9, 71/10, 71/11, 71/12, 71/13, 71/14,
71/15, 71/16, 71/17, 71/18, 71/19, 71/20, 71/21, 71/22, 71/23, 71/24, 71/25, 71/26, 71/27,
71/28, 71/29, 71/30, 71/31, 71/32, 71/33, 71/34, 71/35, 71/36, 71/37, 71/38, 71/39, 71/40,
71/41, 71/42, 71/43, 71/44, 71/45, 71/46, 71/47, 71/48, 71/49, 71/50, 71/51, 71/52, 71/53,
71/54, 71/55, 71/56, 71/57, 71/58, 71/59, 71/60, 71/61, 71/62, 71/63, 71/64, 71/65, 71/66,
71/67, 71/68, 71/69, 71/70, 72, 72/5, 72/7, 72/11, 72/13, 72/17, 72/19, 72/23, 72/25, 72/29,
72/31, 72/35, 72/37, 72/41, 72/43, 72/47, 72/49, 72/53, 72/55, 72/59, 72/61, 72/65, 72/67,
72/71, 73, 73/2, 73/3, 73/4, 73/5, 73/6, 73/7, 73/8, 73/9, 73/10, 73/11, 73/12, 73/13, 73/14,
73/15, 73/16, 73/17, 73/18, 73/19, 73/20, 73/21, 73/22, 73/23, 73/24, 73/25, 73/26, 73/27,
73/28, 73/29, 73/30, 73/31, 73/32, 73/33, 73/34, 73/35, 73/36, 73/37, 73/38, 73/39, 73/40,
73/41, 73/42, 73/43, 73/44, 73/45, 73/46, 73/47, 73/48, 73/49, 73/50, 73/51, 73/52, 73/53,
73/54, 73/55, 73/56, 73/57, 73/58, 73/59, 73/60, 73/61, 73/62, 73/63, 73/64, 73/65, 73/66,
73/67, 73/68, 73/69, 73/70, 73/71, 73/72, 74, 74/3, 74/5, 74/7, 74/9, 74/11, 74/13, 74/15,
74/17, 74/19, 74/21, 74/23, 74/25, 74/27, 74/29, 74/31, 74/33, 74/35, 74/39, 74/41, 74/43,
74/45, 74/47, 74/49, 74/51, 74/53, 74/55, 74/57, 74/59, 74/61, 74/63, 74/65, 74/67, 74/69,
74/71, 74/73, 75, 75/2, 75/4, 75/7, 75/8, 75/11, 75/13, 75/14, 75/16, 75/17, 75/19, 75/22,
75/23, 75/26, 75/28, 75/29, 75/31, 75/32, 75/34, 75/37, 75/38, 75/41, 75/43, 75/44, 75/46,
75/47, 75/49, 75/52, 75/53, 75/56, 75/58, 75/59, 75/61, 75/62, 75/64, 75/67, 75/68, 75/71,
75/73, 75/74, 76, 76/3, 76/5, 76/7, 76/9, 76/11, 76/13, 76/15, 76/17, 76/21, 76/23, 76/25,
76/27, 76/29, 76/31, 76/33, 76/35, 76/37, 76/39, 76/41, 76/43, 76/45, 76/47, 76/49, 76/51,
76/53, 76/55, 76/59, 76/61, 76/63, 76/65, 76/67, 76/69, 76/71, 76/73, 76/75, 77, 77/2,
77/3, 77/4, 77/5, 77/6, 77/8, 77/9, 77/10, 77/12, 77/13, 77/15, 77/16, 77/17, 77/18, 77/19,
77/20, 77/23, 77/24, 77/25, 77/26, 77/27, 77/29, 77/30, 77/31, 77/32, 77/34, 77/36, 77/37,
77/38, 77/39, 77/40, 77/41, 77/43, 77/45, 77/46, 77/47, 77/48, 77/50, 77/51, 77/52, 77/53,
77/54, 77/57, 77/58, 77/59, 77/60, 77/61, 77/62, 77/64, 77/65, 77/67, 77/68, 77/69, 77/71,
77/72, 77/73, 77/74, 77/75, 77/76, 78, 78/5, 78/7, 78/11, 78/17, 78/19, 78/23, 78/25, 78/29,
78/31, 78/35, 78/37, 78/41, 78/43, 78/47, 78/49, 78/53, 78/55, 78/59, 78/61, 78/67, 78/71,
78/73, 78/77, 79, 79/2, 79/3, 79/4, 79/5, 79/6, 79/7, 79/8, 79/9, 79/10, 79/11, 79/12, 79/13,
79/14, 79/15, 79/16, 79/17, 79/18, 79/19, 79/20, 79/21, 79/22, 79/23, 79/24, 79/25, 79/26,
79/27, 79/28, 79/29, 79/30, 79/31, 79/32, 79/33, 79/34, 79/35, 79/36, 79/37, 79/38, 79/39,
79/40, 79/41, 79/42, 79/43, 79/44, 79/45, 79/46, 79/47, 79/48, 79/49, 79/50, 79/51, 79/52,
79/53, 79/54, 79/55, 79/56, 79/57, 79/58, 79/59, 79/60, 79/61, 79/62, 79/63, 79/64, 79/65,
79/66, 79/67, 79/68, 79/69, 79/70, 79/71, 79/72, 79/73, 79/74, 79/75, 79/76, 79/77, 79/78,
80, 80/3, 80/7, 80/9, 80/11, 80/13, 80/17, 80/19, 80/21, 80/23, 80/27, 80/29, 80/31, 80/33,
80/37, 80/39, 80/41, 80/43, 80/47, 80/49, 80/51, 80/53, 80/57, 80/59, 80/61, 80/63, 80/67,
80/69, 80/71, 80/73, 80/77, 80/79, 81, 81/2, 81/4, 81/5, 81/7, 81/8, 81/10, 81/11, 81/13,
81/14, 81/16, 81/17, 81/19, 81/20, 81/22, 81/23, 81/25, 81/26, 81/28, 81/29, 81/31, 81/32,
81/34, 81/35, 81/37, 81/38, 81/40, 81/41, 81/43, 81/44, 81/46, 81/47, 81/49, 81/50, 81/52,
81/53, 81/55, 81/56, 81/58, 81/59, 81/61, 81/62, 81/64, 81/65, 81/67, 81/68, 81/70, 81/71,
81/73, 81/74, 81/76, 81/77, 81/79, 81/80, 82, 82/3, 82/5, 82/7, 82/9, 82/11, 82/13, 82/15,
82/17, 82/19, 82/21, 82/23, 82/25, 82/27, 82/29, 82/31, 82/33, 82/35, 82/37, 82/39, 82/43,

16

82/45, 82/47, 82/49, 82/51, 82/53, 82/55, 82/57, 82/59, 82/61, 82/63, 82/65, 82/67, 82/69,
82/71, 82/73, 82/75, 82/77, 82/79, 82/81, 83, 83/2, 83/3, 83/4, 83/5, 83/6, 83/7, 83/8,
83/9, 83/10, 83/11, 83/12, 83/13, 83/14, 83/15, 83/16, 83/17, 83/18, 83/19, 83/20, 83/21,
83/22, 83/23, 83/24, 83/25, 83/26, 83/27, 83/28, 83/29, 83/30, 83/31, 83/32, 83/33, 83/34,
83/35, 83/36, 83/37, 83/38, 83/39, 83/40, 83/41, 83/42, 83/43, 83/44, 83/45, 83/46, 83/47,
83/48, 83/49, 83/50, 83/51, 83/52, 83/53, 83/54, 83/55, 83/56, 83/57, 83/58, 83/59, 83/60,
83/61, 83/62, 83/63, 83/64, 83/65, 83/66, 83/67, 83/68, 83/69, 83/70, 83/71, 83/72, 83/73,
83/74, 83/75, 83/76, 83/77, 83/78, 83/79, 83/80, 83/81, 83/82, 84, 84/5, 84/11, 84/13,
84/17, 84/19, 84/23, 84/25, 84/29, 84/31, 84/37, 84/41, 84/43, 84/47, 84/53, 84/55, 84/59,
84/61, 84/65, 84/67, 84/71, 84/73, 84/79, 84/83, 85, 85/2, 85/3, 85/4, 85/6, 85/7, 85/8,
85/9, 85/11, 85/12, 85/13, 85/14, 85/16, 85/18, 85/19, 85/21, 85/22, 85/23, 85/24, 85/26,
85/27, 85/28, 85/29, 85/31, 85/32, 85/33, 85/36, 85/37, 85/38, 85/39, 85/41, 85/42, 85/43,
85/44, 85/46, 85/47, 85/48, 85/49, 85/52, 85/53, 85/54, 85/56, 85/57, 85/58, 85/59, 85/61,
85/62, 85/63, 85/64, 85/66, 85/67, 85/69, 85/71, 85/72, 85/73, 85/74, 85/76, 85/77, 85/78,
85/79, 85/81, 85/82, 85/83, 85/84, 86, 86/3, 86/5, 86/7, 86/9, 86/11, 86/13, 86/15, 86/17,
86/19, 86/21, 86/23, 86/25, 86/27, 86/29, 86/31, 86/33, 86/35, 86/37, 86/39, 86/41, 86/45,
86/47, 86/49, 86/51, 86/53, 86/55, 86/57, 86/59, 86/61, 86/63, 86/65, 86/67, 86/69, 86/71,
86/73, 86/75, 86/77, 86/79, 86/81, 86/83, 86/85, 87, 87/2, 87/4, 87/5, 87/7, 87/8, 87/10,
87/11, 87/13, 87/14, 87/16, 87/17, 87/19, 87/20, 87/22, 87/23, 87/25, 87/26, 87/28, 87/31,
87/32, 87/34, 87/35, 87/37, 87/38, 87/40, 87/41, 87/43, 87/44, 87/46, 87/47, 87/49, 87/50,
87/52, 87/53, 87/55, 87/56, 87/59, 87/61, 87/62, 87/64, 87/65, 87/67, 87/68, 87/70, 87/71,
87/73, 87/74, 87/76, 87/77, 87/79, 87/80, 87/82, 87/83, 87/85, 87/86, 88, 88/3, 88/5, 88/7,
88/9, 88/13, 88/15, 88/17, 88/19, 88/21, 88/23, 88/25, 88/27, 88/29, 88/31, 88/35, 88/37,
88/39, 88/41, 88/43, 88/45, 88/47, 88/49, 88/51, 88/53, 88/57, 88/59, 88/61, 88/63, 88/65,
88/67, 88/69, 88/71, 88/73, 88/75, 88/79, 88/81, 88/83, 88/85, 88/87, 89, 89/2, 89/3, 89/4,
89/5, 89/6, 89/7, 89/8, 89/9, 89/10, 89/11, 89/12, 89/13, 89/14, 89/15, 89/16, 89/17, 89/18,
89/19, 89/20, 89/21, 89/22, 89/23, 89/24, 89/25, 89/26, 89/27, 89/28, 89/29, 89/30, 89/31,
89/32, 89/33, 89/34, 89/35, 89/36, 89/37, 89/38, 89/39, 89/40, 89/41, 89/42, 89/43, 89/44,
89/45, 89/46, 89/47, 89/48, 89/49, 89/50, 89/51, 89/52, 89/53, 89/54, 89/55, 89/56, 89/57,
89/58, 89/59, 89/60, 89/61, 89/62, 89/63, 89/64, 89/65, 89/66, 89/67, 89/68, 89/69, 89/70,
89/71, 89/72, 89/73, 89/74, 89/75, 89/76, 89/77, 89/78, 89/79, 89/80, 89/81, 89/82, 89/83,
89/84, 89/85, 89/86, 89/87, 89/88, 90, 90/7, 90/11, 90/13, 90/17, 90/19, 90/23, 90/29,
90/31, 90/37, 90/41, 90/43, 90/47, 90/49, 90/53, 90/59, 90/61, 90/67, 90/71, 90/73, 90/77,
90/79, 90/83, 90/89, 91, 91/2, 91/3, 91/4, 91/5, 91/6, 91/8, 91/9, 91/10, 91/11, 91/12,
91/15, 91/16, 91/17, 91/18, 91/19, 91/20, 91/22, 91/23, 91/24, 91/25, 91/27, 91/29, 91/30,
91/31, 91/32, 91/33, 91/34, 91/36, 91/37, 91/38, 91/40, 91/41, 91/43, 91/44, 91/45, 91/46,
91/47, 91/48, 91/50, 91/51, 91/53, 91/54, 91/55, 91/57, 91/58, 91/59, 91/60, 91/61, 91/62,
91/64, 91/66, 91/67, 91/68, 91/69, 91/71, 91/72, 91/73, 91/74, 91/75, 91/76, 91/79, 91/80,
91/81, 91/82, 91/83, 91/85, 91/86, 91/87, 91/88, 91/89, 91/90, 92, 92/3, 92/5, 92/7, 92/9,
92/11, 92/13, 92/15, 92/17, 92/19, 92/21, 92/25, 92/27, 92/29, 92/31, 92/33, 92/35, 92/37,
92/39, 92/41, 92/43, 92/45, 92/47, 92/49, 92/51, 92/53, 92/55, 92/57, 92/59, 92/61, 92/63,
92/65, 92/67, 92/71, 92/73, 92/75, 92/77, 92/79, 92/81, 92/83, 92/85, 92/87, 92/89, 92/91,
93, 93/2, 93/4, 93/5, 93/7, 93/8, 93/10, 93/11, 93/13, 93/14, 93/16, 93/17, 93/19, 93/20,
93/22, 93/23, 93/25, 93/26, 93/28, 93/29, 93/32, 93/34, 93/35, 93/37, 93/38, 93/40, 93/41,

17

93/43, 93/44, 93/46, 93/47, 93/49, 93/50, 93/52, 93/53, 93/55, 93/56, 93/58, 93/59, 93/61,
93/64, 93/65, 93/67, 93/68, 93/70, 93/71, 93/73, 93/74, 93/76, 93/77, 93/79, 93/80, 93/82,
93/83, 93/85, 93/86, 93/88, 93/89, 93/91, 93/92, 94, 94/3, 94/5, 94/7, 94/9, 94/11, 94/13,
94/15, 94/17, 94/19, 94/21, 94/23, 94/25, 94/27, 94/29, 94/31, 94/33, 94/35, 94/37, 94/39,
94/41, 94/43, 94/45, 94/49, 94/51, 94/53, 94/55, 94/57, 94/59, 94/61, 94/63, 94/65, 94/67,
94/69, 94/71, 94/73, 94/75, 94/77, 94/79, 94/81, 94/83, 94/85, 94/87, 94/89, 94/91, 94/93,
95, 95/2, 95/3, 95/4, 95/6, 95/7, 95/8, 95/9, 95/11, 95/12, 95/13, 95/14, 95/16, 95/17,
95/18, 95/21, 95/22, 95/23, 95/24, 95/26, 95/27, 95/28, 95/29, 95/31, 95/32, 95/33, 95/34,
95/36, 95/37, 95/39, 95/41, 95/42, 95/43, 95/44, 95/46, 95/47, 95/48, 95/49, 95/51, 95/52,
95/53, 95/54, 95/56, 95/58, 95/59, 95/61, 95/62, 95/63, 95/64, 95/66, 95/67, 95/68, 95/69,
95/71, 95/72, 95/73, 95/74, 95/77, 95/78, 95/79, 95/81, 95/82, 95/83, 95/84, 95/86, 95/87,
95/88, 95/89, 95/91, 95/92, 95/93, 95/94, 96, 96/5, 96/7, 96/11, 96/13, 96/17, 96/19, 96/23,
96/25, 96/29, 96/31, 96/35, 96/37, 96/41, 96/43, 96/47, 96/49, 96/53, 96/55, 96/59, 96/61,
96/65, 96/67, 96/71, 96/73, 96/77, 96/79, 96/83, 96/85, 96/89, 96/91, 96/95, 97, 97/2, 97/3,
97/4, 97/5, 97/6, 97/7, 97/8, 97/9, 97/10, 97/11, 97/12, 97/13, 97/14, 97/15, 97/16, 97/17,
97/18, 97/19, 97/20, 97/21, 97/22, 97/23, 97/24, 97/25, 97/26, 97/27, 97/28, 97/29, 97/30,
97/31, 97/32, 97/33, 97/34, 97/35, 97/36, 97/37, 97/38, 97/39, 97/40, 97/41, 97/42, 97/43,
97/44, 97/45, 97/46, 97/47, 97/48, 97/49, 97/50, 97/51, 97/52, 97/53, 97/54, 97/55, 97/56,
97/57, 97/58, 97/59, 97/60, 97/61, 97/62, 97/63, 97/64, 97/65, 97/66, 97/67, 97/68, 97/69,
97/70, 97/71, 97/72, 97/73, 97/74, 97/75, 97/76, 97/77, 97/78, 97/79, 97/80, 97/81, 97/82,
97/83, 97/84, 97/85, 97/86, 97/87, 97/88, 97/89, 97/90, 97/91, 97/92, 97/93, 97/94, 97/95,
97/96, 98, 98/3, 98/5, 98/9, 98/11, 98/13, 98/15, 98/17, 98/19, 98/23, 98/25, 98/27, 98/29,
98/31, 98/33, 98/37, 98/39, 98/41, 98/43, 98/45, 98/47, 98/51, 98/53, 98/55, 98/57, 98/59,
98/61, 98/65, 98/67, 98/69, 98/71, 98/73, 98/75, 98/79, 98/81, 98/83, 98/85, 98/87, 98/89,
98/93, 98/95, 98/97, 99, 99/2, 99/4, 99/5, 99/7, 99/8, 99/10, 99/13, 99/14, 99/16, 99/17,
99/19, 99/20, 99/23, 99/25, 99/26, 99/28, 99/29, 99/31, 99/32, 99/34, 99/35, 99/37, 99/38,
99/40, 99/41, 99/43, 99/46, 99/47, 99/49, 99/50, 99/52, 99/53, 99/56, 99/58, 99/59, 99/61,
99/62, 99/64, 99/65, 99/67, 99/68, 99/70, 99/71, 99/73, 99/74, 99/76, 99/79, 99/80, 99/82,
99/83, 99/85, 99/86, 99/89, 99/91, 99/92, 99/94, 99/95, 99/97, 99/98, 100, 100/3, 100/7,
100/9, 100/11, 100/13, 100/17, 100/19, 100/21, 100/23, 100/27, 100/29, 100/31, 100/33,
100/37, 100/39, 100/41, 100/43, 100/47, 100/49, 100/51, 100/53, 100/57, 100/59, 100/61,
100/63, 100/67, 100/69, 100/71, 100/73, 100/77, 100/79, 100/81, 100/83, 100/87, 100/89,
100/91, 100/93, 100/97, 100/99

8 Acknowledgment

The authors would like to thank Carl Pomerance and an anonymous referee for their feedback,
which helped to improve both the content and the presentation of this article.

References

[1] C. W. Anderson, The solution of Σ(n) = σ(n)/n = a/b, Φ(n) = φ(n)/n = a/b and some
related considerations, unpublished manuscript, 1974.

18

[2] J. Holdener, Conditions equivalent to the existence of odd perfect numbers, Math. Mag.
79 (2006), 389–391.

[3] R. Laatsch, Measuring the abundancy of integers, Math. Mag. 59 (1986), 84–92.

[4] R. Ryan, Results concerning uniqueness for σ(x)/x = σ(pnqm)/(pnqm) and related top-
ics, Int. Math. J. 2 (2002), 497–514.

[5] P. A. Weiner, The abundancy ratio, a measure of perfection, Math. Mag. 73 (2000),
307–310.

2000 Mathematics Subject Classiﬁcation: Primary 11A25; Secondary 11Y55, 11Y70.

Keywords: abundancy index, abundancy outlaw, sum of divisors function, perfect numbers.

Received October 25 2006; revised version received August 31 2007; September 25 2007.
Published in Journal of Integer Sequences, September 25 2007.

Return to Journal of Integer Sequences home page.

19
