<!-- source: https://arxiv.org/pdf/1306.5656 | converted from PDF -->

arXiv:1306.5656v1  [math.GM]  19 Jun 2013
Three proofs of the Casas-Alvero conjecture

Luis J. Fern´andez de las Herasa,∗, Mar´ıa J. Fern´andez de las Herasb

aDpto. de Matem´atica Aplicada, E.T.S. de Ingenieros Industriales, Universidad
Polit´ecnica de Madrid, Jos´e G. Abascal 2, 28006 Madrid, Spain.
bCSIC, Centro de Ac´ustica Aplicada y Evaluaci´on no Destructiva, Serrano 144, 28006
Madrid, Spain.

Abstract

The Casas-Alvero conjecture claims that a complex univariate polynomial
having roots in common with each of its derivatives must be a power of a
linear polynomial. Up to now, only partial proofs and numerical evidences
have been presented. In this paper we give three diﬀerent proofs of the
conjecture.

Keywords: Polynomial interpolation, univariate polynomials.
2010 MSC: 41A05, 30E05

1. Introduction

This paper is concerned with the following question posed by E. Casas-
Alvero more than a decade ago.

Casas-Alvero Conjecture. Let f be a monic complex polynomial of degree
n in a single variable z. Suppose that gcd(f, f (k)) ̸= 1 for k = 1, . . . , n − 1,
where f (k) denotes the k-th derivative of f . Then, there exists a constant
a ∈ C such that f (z) = (z − a)n.

It may be proven that if the conjecture is true over C then it is true over
all ﬁelds of characteristic 0. In contrast, the conjecture is not true in prime
characteristic.
In [2] the Casas-Alvero conjecture was proven for polynomials of degree
n less than or equal to 7. The conjecture has also been proven for inﬁnitely
many values of n, see [1].

∗Corresponding author. Fax: +34 91 336 3001. Phone: +34 91 336 3106
Email addresses: lfernandez@etsii.upm.es (Luis J. Fern´andez de las Heras),
mjose@caend.upm-csic.es (Mar´ıa J. Fern´andez de las Heras)

Preprint submitted to J. Approx. Theory November 27, 2024

We can rewrite the conjecture in terms of interpolation polynomials on
the complex plane C, see [3, 4].

Theorem 1.1. Let z1, z2, . . . , zn be n complex numbers and let p be a monic
complex polynomial of degree n. Suppose that the polynomial p satisﬁes

p(zk) = 0, k = 1, . . . , n;
p(k)(zk+1) = 0, k = 1, . . . , n − 1.

Then p(z) = (z − a)
n, a ∈ C.

In the sequel any monic polynomial satisfying the conditions of Theorem
1.1 will be called a Casas-Alvero polynomial.

2. Birkhoﬀ interpolation

First, we pose the following problems which may be considered as par-
ticular cases of Birkhoﬀ or lacunary interpolation problems [5]. They are
closely related to the Casas-Alvero conjecture.

Problem 2.1. Given n complex numbers α1, . . . αn, ﬁnd all monic polyno-
mials p that satisfy

p(k)(αk+1) = 0, k = 0, 1, . . . , n − 1.

Solution. A monic polynomial pn of degree n can be expressed in the form

pn(z) =
 n∑

j=0 ajzj, (1)

where an = 1. For k = 1, . . . , n, its k-th derivative is given by

p(k)
n (z) =
 n∑

j=k aj j!
(j − k)! zj−k.

If we evaluate the above expressions at the nodes, we obtain

p(k)
n (αk+1) =
 n∑

j=k aj j!
(j − k)! α
j−k
k+1 = 0, k = 0, 1, . . . , n − 1.

2

We can write the above equations in matrix form as

A ·
 







 a0
a1
...
an−1
an
 






 =
 







 0
0
...
0
n!
 






 ,

where

A =
 














 1 α1 α2
1 · · · α
n−2
1 α
n−1
1 αn
1
0 1 2α2 · · · n−2
1 α
n−3
2 n−1
1 α
n−2
2 nα
n−1
2
0 0 2! · · · (n−2)!
(n−4)! α
n−4
3 (n−1)!
(n−3)! α
n−3
3 n!
(n−2)! α
n−2
3
... ... ... · · · ... ... ...
0 0 0 · · · (n − 2)! (n−1)!
1 αn−1 n!
2! α2
n−1
0 0 0 · · · 0 (n − 1)! n!αn
0 0 0 · · · 0 0 n!
 














 .

Clearly the interpolation problem has a solution and it is unique, because
the matrix is of full rank. The solution of the system is trivial but laborious.
The incidence matrix will have as many rows as the number of diﬀerent
nodes. In the extreme case that there is only one node, the problem is of
Hermite type. As in all cases the matrix is triangular, there is always a
unique solution.
A straightforward calculation shows that the unique solution pn of Prob-
lem 2.1 admits the following integral representation

pn(z) = n! ∫ z

α1 dx1
 ∫ x1

α2 dx2 . . . ∫ xn−2

αn−1 dxn−1
 ∫ xn−1

αn dxn. (2)

We can study now the inverse problem.

Problem 2.2. Given n complex numbers z1, z2, . . . , zn, let

ˆz = (z1, . . . , zn) and p(z) =
 n∏

k=1
(z − zk).

Find all the vectors of complex numbers

α = (α1, α2, ..., αn)

3

that satisfy p(k)(αk+1) = 0, k = 0, 1, ..., n − 1.

Solution. The problem has a solution. We begin with the last equation of
the system given by Problem 2.1 to obtain αn. Then we solve the (n − 1)-th
equation to get the two values of αn−1 and we continue until considering the
ﬁrst equation of degree n which allows us to obtain the n values of α1.
The problem has a solution but the solution is not unique. The problem
may have until n! diﬀerent solutions. Of course, it is possible to approxi-
mate the solutions by numerical methods, but it should be noticed that this
problem is invariant under permutation of the symmetric group of the n
components of ˆz. If we change the order of the roots in ˆz, the polynomial
p does not change and the solutions of the problem are the same ones as
before. The number of solutions is just equal to the number of permutations
of ˆz.
We can make Problem 2.2 more complicated considering additional con-
ditions like requiring the nodes of interpolation α to be equal to the zeros
of the polynomial p. Thus, the polynomial p and its derivatives will have
common zeros.

3. The ﬁrst proof

There are several diﬀerent ways to tackle the proof. We have chosen
to consider it as a problem of the same type as that of Problem 2.2. That
is, assuming that the roots of the polynomial are known, ﬁnd the nodes of
interpolation. Subsequently, impose the condition that the roots coincide
with the nodes. Then this problem is invariant under permutations of the
zeros of the polynomial as in Problem 2.2. But if we permute the zeros of the
polynomial, the interpolation nodes are automatically interchanged. Thus
the polynomial and its derivatives up to order n − 1 must take the value zero
at all the zeros of the polynomial. Therefore, all the zeros are of multiplicity
n. But this is possible only if there is a single zero of multiplicity n. Thus,
the Casas-Alvero conjecture is proven.

4

4. A second proof by induction

Taking account of the representation (2), for n = 2, the Casas-Alvero
polynomial is

p2(z) = 2! ∫ z

α1 dx1
 ∫ x1

α2 dx2 = 2! ∫ z

α2 dx1
 ∫ x1

α2 dx2

= (z − α2)
2 − (α1 − α2)
2 = (z − α2)
2 = (z − α1)
2.

Now suppose that, for k = 1, . . . , n − 1, any Casas-Alvero polynomial is of
the form
 pk(z) = (z − α1)
k.

Then
 pn(z) = n! ∫ z

α1 dx1
 ∫ x1

α2 dx2 · · · ∫ xn−2

αn−1 dxn−1
 ∫ xn−1

αn dxn.

Notice that pn(z) takes the value zero at z = αk from k = 1 to n. So, for
k = 1, . . . , n, we have

pn(z) = n! ∫ z

αk dx1
 ∫ x1

α2 dx2 · · · ∫ xn−2

αn−1 dxn−1
 ∫ xn−1

αn dxn.

Therefore

pn(z) = n! ∫ z

αk dx1
 ∫ x1

α2 dx2 · · · ∫ xn−2

αn−1 (xn−1 − αn)dxn−1

= n! ∫ z

αk dx1
 ∫ x1

α2 dx2 · · · ∫ xn−2

αn−1 xn−1dxn−1 − nαnpn−1(z),

for k = 1, . . . , n, where pn−1 is a Casas-Alvero polynomial of degree n − 1.
Then
 pn−1(z) = (z − α1)
n−1

and α1 = α2 = · · · = αn−1.

Therefore

pn(z) = n! ∫ z

α1 dx1
 ∫ x1

α1 dx2 · · · ∫ xn−3

α1
 1
2 (x2
n−2 − α
2
1) dxn−2 − nαnpn−1(z)

= n! ∫ z

α1 dx1
 ∫ x1

α1 dx2 · · · ∫ xn−3

α1
 1
2! x2
n−2 dxn−2

− n(n − 1)
2 α
2
1pn−2(z) − nαnpn−1(z),

5

where pn−2(z) = (z − α1)n−2.
If we continue the process of calculating the iterated integral, we arrived
at
 pn(z) = zn − α
n
1 −
 n−2∑

k=1
 ( n
k
 ) α
n−k
1 (z − α1)
k − nαnpn−1(z)

= zn −
 n−1∑

k=0
 ( n
k
 ) α
n−k
1 (z − α1)
k + n(α1 − αn)(z − α1)
n−1

= zn + (z − α1)
n −
 n∑

k=0
 ( n
k
 ) α
n−k
1 (z − α1)
k

+n(α1 − αn)(z − α1)
n−1

= (z − α1)
n + n(α1 − αn)(z − α1)
n−1,

since the number αn is a root of the polynomial pn. Actually

pn(αn) = (αn − α1)
n + n(α1 − αn)(αn − α1)
n−1

= −(n − 1)(αn − α1)
n = 0.

Then, αn = α1 and pn(z) = (z − α1)n, as we wanted to prove.

5. The third proof

Although we think that the previous two proofs are correct, we encourage
the reader to continue reading the article.

Lemma 5.1. Every Casas-Alvero polynomial has a root equal to the geo-
metric center of gravity of its roots.

Proof. Let pn be a monic polynomial of degree n expressed in the form (1).
Then p(n−1)
n (z) = n! z + (n − 1)! an−1.

Evaluating at the zero zn of the polynomial p(n−1)
n , we obtain

p(n−1)
n (zn) = n!zn + (n − 1)!an−1 = 0,

or, equivalently,
 zn = − an−1
n = 1
n
 n∑

j=1 zj.

6

Now, let pn be a monic polynomial of degree n. The polynomial pn may
be written in the form

pn(z) =
 n∑

k=0
 ( n
k
 ) (−1)
kckzn−k, (3)

where
 c0 = 1, c1 = ( n
1
 )−1 n∑

j=1 zj,

ck = ( n
k
 )−1 ji=0,1∑

j1+j2+...+jn=k
 ( n∏

i=1 zji
i
 )
 , k = 2, . . . , n.

Taking derivatives in (3), we obtain

p′
n(z) =
 n−1∑

k=0
 ( n
k
 ) (−1)
kck(n − k)zn−k−1

= n
 n−1∑

k=0
 ( n
k
 ) (−1)
kck n − k
n zn−k−1

= n
 n−1∑

k=0
 ( n − 1
k
 ) (−1)
kckzn−k−1.

The above calculation indicates that the zeros of the derivative of a
polynomial of degree n and the zeros of this polynomial have in common
the following quantities: the average of their zeros, the mean double product
of their zeros, and so forth until the average (n − 1) product of their zeros.
If pn is a Casas-Alvero polynomial, then, for k = 1, . . . , n − 1, the poly-
nomial p(k)
n has the same coeﬃcients cj, j = 1, . . . , n − k, as pn.
For k = n − 1, the zero shared by the polynomial and its derivative of
order n − 1 is precisely c1 and this determines the coeﬃcient of degree n − 1
of the polynomial pn.
For k = n − 2, which is the zero shared by the polynomial and the
derivative of order n − 2? The two zeros determine the same value for c2.
Therefore, whatever zero pn shares with its derivative we obtain same
result for the polynomial. But this reasoning is valid for all the derivatives
of pn. Then all the zeros of the successive derivatives of pn must be zeros of
pn, therefore all the zeros must be equal.

7

6. Concluding remarks

We conclude that the Casas-Alvero conjecture is true. In connection with
the work carried out in this paper, we are currently studying an optimization
problem in which symmetries play an important role. The results related to
this problem will appear elsewhere.
In our opinion solving a math problem is not to close the door but rather
open a window to new challenges. For this reason, we propose a degenerated
Birkhoﬀ interpolation problem in which the number of equations is greater
than the number of unknowns. Among the diﬀerent possibilities we have
chosen the problem stated below. Find the conditions to be met by the
interpolation nodes and their values for the following problem to be solvable.

Problem 6.1. Given 2n complex numbers α1, . . . , αn and c0, . . . , cn−1, ﬁnd
all the polynomials p of degree n that satisfy

p(αk+1) = p(k)(αk+1) = ck, k = 0, 1, . . . , n − 1.

References

[1] H.-C. Graf von Bothmer, O. Labs, J. Schicho, C. van de Woestijne,
The Casas-Alvero conjecture for inﬁnitely many degrees, J. Algebra
316 (2007) 224–230.

[2] G. Diaz-Toca, L. Gonz´alez-Vega, On a conjecture about univariate
polynomials and their roots, In: Algorithmic Algebra and Logic 2005,
Norderstedt, Germany, 2005, pp. 83–90.

[3] J. Draisma, J.P. de Jong, On the Casas-Alvero conjecture, Eur. Math.
Soc. Newsl. 80 (2011) 29–33.

[4] E. Casas-Alvero, Singularities of plane curves, London Mathematical
Society Lecture Note Series 276, Cambridge University Press, Cam-
bridge, 2000.

[5] G.G. Lorentz, K. Jetter, S.D. Riemenschneider, Birkhoﬀ Interpolation,
Addison-Wesley, Reading, Mass., 1982.

8
