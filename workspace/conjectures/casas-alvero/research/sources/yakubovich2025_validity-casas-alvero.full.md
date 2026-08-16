<!-- source: https://arxiv.org/pdf/1504.00274v1 | converted from PDF -->

arXiv:1504.00274v1  [math.CA]  1 Apr 2015
THE VALIDITY OF THE CASAS-ALVERO CONJECTURE

S. YAKUBOVICH

ABSTRACT. An interesting and attractive problem, conjectured in 2001 by E. Casas- Alvero is solved afﬁr-
matively in this note. It says, that any complex univariate polynomial, having a common root with each of its
non-constant derivative must be a power of a linear polynomial.

In 2001 E. Casas-Alvero [1] conjectured that an arbitrary polynomial f degree n ≥ 1 with complex
coefﬁcients of degree n ∈ N
 f (z) = a0z
n + a1z
n−1 + · · · + an−1z + an, a0 ̸= 0 (1)

is of the form f (z) = a(z−b)
n, a, b ∈ C, if and only if f shares a root with each of its derivatives f (1), f (2), . . . ,
f (n−1). It is proved for small degrees, for inﬁnitely many degrees, for instance, for all powers n, when
n is a prime (see in [2], [6] ). We will call these common roots of the corresponding derivatives by
z1, z2, . . . , zn−1 ∈ C (repeated terms are permitted). As it was recently observed by the author [7], the polyno-
mial (1), satisfying the Casas- Alvero conditions, can be identiﬁed, involving the familiar Abel-Goncharov
interpolation polynomials [3], namely

f (z) = Gn(z, z0, z1, . . . , zn−1) = n! ∫ z

z0
 ∫ s1

z1 . . . ∫ sn−1

zn−1 dsn . . . ds1 (2)

with the additional conditions (z0 is a root of f )

Gn(z j, z0, z1, . . . , zn−1) = 0, j = 1, 2, . . . , n − 1. (3)

Without loss of generality we assume that f is a monic polynomial of degree n ≥ 2, since for n = 1 there is
nothing to prove. In particular, it was shown in [7] that Gn satisﬁes the following upper bound

|Gn(z, z0, z1, . . . , zn−1)| ≤ 1
∑
k0=0
 2−k0
∑
k1=0 · · ·
 n−1−k0−k1−···−kn−3
∑
kn−2=0
 ( n
k0, k1, . . . , kn−2, n − k0 − k1 − · · · − kn−2
)

× n−1
∏
s=0 |zn−2−s − zn−1−s|ks ,

where z−1 ≡ z and ( n
l0, l1, . . . , lm
) = n!
l0!l1! . . . lm! , l0 + l1 · · · + lm = n.

Date: November 4, 2018.
2000 Mathematics Subject Classiﬁcation. Primary 26C05, 12D10, 41A05 ; Secondary 13F20 .
Key words and phrases. Casas-Alvero conjecture, Abel- Goncharov polynomials.

1

2 S. YAKUBOVICH

This estimate is sharper than the classical Goncharov upper bound [3]

|Gn(z, z0, z1, . . . , zn−1)| ≤
 (
|z − z0| + n−2
∑
s=0 |zs+1 − zs|
)n .

The Abel- Goncharov polynomials can be represented via the so-called Levinson binomial type expansion
(see in [5], p. 732)
 Gn(z, z0, z1, . . . , zn−1) = n
∑
k=1(z
k − z
k
0)
(
n
k
)Hn−k, (4)

where H0 = 1 and

Hn−k ≡ Hn−k(zk, zk+1, . . . , zn−1) = (n − k)! ∫ 0

zk
 ∫ sk+1

zk+1 . . . ∫ sn−1

zn−1 dsn . . . dsk+1, k = 1, . . . , n − 1. (5)

However we will prove in turn that the polynomials Hn−k can be represented in a determinant form of an
upper Hessenberg matrix (n − k) × (n − k) with the entries equal to 1 on the main subdiagonal [4].
Generally, it has
Lemma. Let n ∈ N and a j ∈ C, j = 1, . . . , n. Then

(−1)n

n! Hn(a1, a2, . . . , an) =
 ∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
a1 a2
1
2! a3
1
3! . . . an
1
n!
1 a2 a2
2
2! . . . an−1
2
(n−1)!
0 1 a3 . . . an−2
3
(n−2)!
... . . . . . . . . . ...
0 0 . . . 1 an
 ∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
 . (6)

Proof. Appealing to the principle of mathematical induction and easily verifying formula (6) for n = 1, 2 via
the calculation of the corresponding integral (5), i.e.

H1(a1) = −a1, 1
2 H2(a1, a2) =
 ∣
∣
∣
∣
∣
a1 a2
1
2!
1 a2
∣
∣
∣
∣
∣ = a1a2 − a2
1
2! ,

we assume that the statement holds for all 1 ≤ k ≤ n and will prove it for n + 1. Indeed, expanding the
corresponding determinant along the ﬁrst column by the Laplace theorem, we ﬁnd
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣

a1 a2
1
2! a3
1
3! . . . an+1
1
(n+1)!
1 a2 a2
2
2! . . . an
2
n!
0 1 a3 . . . an−1
3
(n−1)!
... . . . . . . . . . ...
0 0 . . . 1 an+1
 ∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
 = a1
 ∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
a2 a2
2
2! . . . an
2
n!
1 a3 . . . an−1
3
(n−1)!

. . . . . . . . . ...
0 . . . 1 an+1
 ∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
 −
 ∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
 a2
1
2! a3
1
3! . . . an+1
1
(n+1)!
1 a3 . . . an−1
3
(n−1)!

. . . . . . . . . ...
0 . . . 1 an+1
 ∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
 . (7)

The ﬁrst n × n determinant in the right-hand side of the latter equality by the induction hypothesis is equal
to ∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
a2 a2
2
2! . . . an
2
n!
1 a3 . . . an−1
3
(n−1)!

. . . . . . . . . ...
0 . . . 1 an+1
 ∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
 = (−1)n

n! Hn(a2, a3, . . . , an+1).

CASAS-ALVERO CONJECTURE 3

The second determinant we will expand in the same fashion to obtain
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
 a2
1
2! a3
1
3! . . . an+1
1
(n+1)!
1 a3 . . . an−1
3
(n−1)!

. . . . . . . . . ...
0 . . . 1 an+1
 ∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
 = a2
1
2!
 ∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
a3 a2
3
2! . . . an−1
3
(n−1)!
1 a4 . . . an−2
4
(n−2)!

. . . . . . . . . ...
0 . . . 1 an+1
 ∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
 −
 ∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
 a3
1
3! a4
1
4! . . . an+1
1
(n+1)!
1 a4 . . . an−2
4
(n−2)!

. . . . . . . . . ...
0 . . . 1 an+1
 ∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
 .

Continuing the same process and applying every time the induction hypothesis, we arrive at the ﬁnal expan-
sion of the determinant in the left-hand side of the equality (6)

(−1)
n+1
 ∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
a1 a2
1
2! a3
1
3! . . . an+1
1
(n+1)!
1 a2 a2
2
2! . . . an
2
n!
0 1 a3 . . . an−1
3
(n−1)!
... . . . . . . . .. ...
0 0 . . . 1 an+1
 ∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
 = − n+1
∑
k=1
 ak
1
k! Hn+1−k(ak, a3, . . . , an+1). (8)

Fortunately, the expression in the right-hand side of (8) is calculated by Levinson via the Taylor theorem (
cf. [5], p. 731) and we ﬁnd

− n+1
∑
k=1
 ak
1
k! Hn+1−k(ak, a3, . . . , an+1) = 1
(n + 1)! Hn+1(a1, a2, . . . , an+1).

Thus we get the validity of equality (6) for all n ∈ N and complete the proof of the Lemma. □

Corollary. The Levinson polynomials Hn, n ∈ N have the following determinant representation

Hn(a1, a2, . . . , an) = (−1)
n
 ∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
a1 a2
1 a3
1 . . . an
1
1 (2
1)
a2 (3
1)
a2
2 . . . (n
1)
an−1
2
0 1 (3
2)
a3 . . . (n
2)
an−2
3
... . . . . . . . . . ...
0 0 . . . 1 ( n
n−1
)
an
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
 . (9)

Proof. In fact, the proof easily follows from (6). For this we multiply the last column of the determinant by
n!, the second column by 2!, the third one by 3! etc., and the n − 1-th column by (n − 1)!. Then, dividing the
third row by 2!, the fourth row by 3! etc., and the last row by (n − 1)!, we get the result. □

Now we are ready to prove our main result of this Note.
Theorem. The Casas-Alvero conjecture is afﬁrmative.

Proof. Without loss of generality one can suppose that one of the polynomial roots, say, z0 = 0. Then for a
ﬁxed sequence {z j}n−1
1 of common roots of f and its derivatives up to the order n − 1 (4) implies

Gn(z, 0, z1, . . . , zn−1) = n
∑
k=1 z
k(
n
k
)
Hn−k. (10)

4 S. YAKUBOVICH

Assume that the conjecture is false. Then at least one of z1, . . . , zn−1 is nonzero, otherwise the polynomial has
the unique root of multiplicity n, which is equal to zero. Let the polynomial f , satisfying the Casas-Alvero
conditions have k nonzero common roots (1 ≤ k ≤ n − 1) in our sequence {z j}n−1
1

z j, j = i1, . . . , ik, {i1, . . . , ik} ⊂ {1, . . . , n − 1}, 1 ≤ i1 < i2 < · · · < ik ≤ n − 1, (11)

corresponding the derivatives of the order i1, . . . , ik, respectively. Hence, appealing to the Corollary and
observing from (2) and (5) that the left-hand side of (10) equals to Hn(z, z1, . . . , zn−1), we end up with the
equality
 Hn(z, z1, z2, . . . , zn−1) = (−1)
n
 ∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
z z2 z3 . . . zn

1 (2
1
)z1 (3
1
)
z2
1 . . . (n
1)
z
n−1
1
0 1 (3
2
)
z2 . . . (n
2)
z
n−2
2
... . . . . . . . . . ...
0 0 . . . 1 ( n
n−1
)
zn−1
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
 . (11)

Moreover, the determinant (11) can be compressed, eliminating rows, containing only one nonzero element
of the main subdiagonal of Hessenberg's matrix, which is equ al to 1. Therefore, we arrive at the equality for
any z ̸= 0

(−1)
n+k z
−i1Hn(z, z1, z2, . . . , zn−1) ≡ Dn,k(z) =
 ∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣

1 zi2−i1 . . . zik−i1 zn−i1

1 (
i2
i1)
z
i2−i1
i1 . . . (ik
i1)
z
ik−i1
i1 ( n
i1)
z
n−i1
i1
0 1 (i3
i2)
z
i3−i2
i2 . . . ( n
i2)
z
n−i2
i2
... . . . . . . . . . ...
0 0 . . . 1 ( n
ik)
z
n−ik
ik
 ∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
 , (12)

containing the determinant of the order (k + 1) × (k + 1) and letting Dn,0(z) = 1. Now, taking into account
the conditions Hn(z j, z1, . . . , zn−1) = 0, z j ̸= 0, j = i1, i2, . . . , ik,

we have
 Dn,k(z j) =
 ∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣

1 z
i2−i1
j . . . z
ik−i1
j z
n−i1
j
1 (i2
i1)
z
i2−i1
i1 . . . (ik
i1)
z
ik−i1
i1 ( n
i1)
z
n−i1
i1
0 1 (
i3
i2)
z
i3−i2
i2 . . . ( n
i2)
z
n−i2
i2
... . . . .. . . . . ...
0 0 . . . 1 ( n
ik)
z
n−ik
ik
 ∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
 = 0, j = i1, . . . , ik. (13)

Let k = 1, i.e. the polynomial has only one nonzero root zi1 ̸= 0 in our sequence of common roots z1, z2, . . . , zn−1,
which corresponds to the i1-th derivative. Hence, putting in (13) j = i1, the determinant
∣
∣
∣
∣
∣
1 z
n−i1
i1
1 ( n
i1)
z
n−i1
i1
 ∣
∣
∣
∣
∣ = 0.

But this is impossible, since we have ( n
i1) = 1, n > i1 ≥ 1. Hence 2 ≤ k ≤ n − 1. Expanding the determinant
(12) along the last row via the Laplace theorem, we derive (see (13))

Dn,k−1(z j) = (n
ik
)
z
n−ik
ik dk(z j), j = i1, . . . , ik, (14)

CASAS-ALVERO CONJECTURE 5

where
 dk(z j) =
 ∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣

1 z
i2−i1
j . . . z
ik−1−i1
j z
ik−i1
j
1 (i2
i1)
z
i2−i1
i1 . . . (ik−1
i1 )
z
ik−1−i1
i1 (ik
i1)
z
ik−i1
i1
0 1 (i3
i2)
z
i3−i2
i2 . . . (ik
i2)
z
ik−i2
i2
... . . . . . . . . . ...
0 0 . . . 1 ( ik
ik−1)
z
ik−ik−1
ik−1
 ∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣k×k
 .

On the other hand, doing, recursively, expansions of the lower order determinants (12) along the last row,
we ﬁnd the relations

Dn,k−s(z j) + Dn,k−s−1(z j) = ( n
ik−s
)
z
n−ik−s
ik−s dk−s(z j), s = 0, 1, . . . , k − 2, j = i1, . . . , ik, (15)

where Dn,k(z j) = 0 via (13). Further, subtracting equality (15) with s + 1 from the previous one with s, we
obtain
 Dn,k−s(z j) − Dn,k−s−2(z j) = ( n
ik−s
)
z
n−ik−s
ik−s dk−s(z j) − ( n
ik−s−1
)
z
n−ik−s−1
ik−s−1 dk−s−1(z j),

where we let naturally d1 = 1. Hence, making summation by s from 0 to k − 2, we deduce

k−2
∑
s=0
 [Dn,k−s(z j) − Dn,k−s−2(z j)
] = (n
ik
)z
n−ik
ik dk(z j) − (n
i1
)
z
n−i1
i1 , j = i1, . . . , ik. (16)

However, recalling (14) and the equality Dn,k(z j) = 0, the equality (16) will be drastically simpliﬁed. Con-
sequently, we come up with the ﬁnal relation

Dn,1(z j) + Dn,0(z j) = (n
i1
)
z
n−i1
i1 . (17)

But since Dn,0(z j) = 1 and
 Dn,1(z j) =
 ∣
∣
∣
∣
∣
1 z
n−i1
j
1 ( n
i1)
z
n−i1
i1
 ∣
∣
∣
∣
∣ ,

equality (17) yields the condition z
n−i1
j = 1, j = i1, . . . , ik and, therefore, |z j| = 1, j = i1, . . . , ik. Returning

to (13) and substituting the value z
n−i1
i1 = 1 in the ﬁrst row and values z
n−i1
j = 1, j = i2, . . . , ik. in the last
column, starting from the second row, after straightforward simpliﬁcations we end up with

An,k =
 ∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣

1 . . . (ik
i1)−1
(i2
i1)−1 z
ik−i2
i1 ( n
i1)−1
(
i2
i1)−1 z
i1−i2
i1

1 (i3
i2)
z
i3−i2
i2 . . . ( n
i2)
z
i1−i2
i2
... . . . . . . ...
0 . . . 1 ( n
ik)
z
i1−ik
ik
 ∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
k×k
 = 0.

If k = 2, the latter equality is ∣
∣
∣
∣
∣
∣
1 ( n
i1)−1
(
i2
i1)−1 z
i1−i2
i1

1 ( n
i2)
z
i1−i2
i2
 ∣
∣
∣
∣
∣
∣ = 0.

6 S. YAKUBOVICH

Calculating the determinant and then taking the modulus of both sides of the obtained equality, we ﬁnd
(n
i2
) =
 ( n
i1) − 1
(
i2
i1) − 1 , n > i2 > i1 ≥ 1. (18)

But since (
i2
i1) ≥ 2 to have (18) it should be ( n
i2) ̸= ( n
i1) and more precisely, ( n
i2) < ( n
i1)
. Indeed, if ( n
i2) > ( n
i1)
,
then we derive from (18)
( n
i1
) − 1 = (n
i2
) ((
i2
i1
) − 1) > (( n
i1
) − 1)((
i2
i1
) − 1).

Hence it yields (
i2
i1) < 2, giving a contradiction. However, using fundamental combinatorial identities, equal-
ity (18) can be rewritten in the form
(n
i1
) (( n − i1
i2 − i1
) − 1) = (n
i2
) − 1.

Hence, (n
i1
) ((n − i1
i2 − i1
) − 1) < (n
i1
)

and therefore, ( n−i1
i2−i1) < 2, which is impossible when n > i2 > i1 ≥ 1.
Finally, in the case k ≥ 3 the same scheme as above of expansions of the lower order determinants
An,k−s, s = 1, . . . , k − 2, and the corresponding eliminations will drive us at the ﬁnal equality

1 +
 ∣
∣
∣
∣
∣
∣

1 ( n
i1)−1
(
i2
i1)−1 z
i1−i2
i1

1 ( n
i2)
z
i1−i2
i2
 ∣
∣
∣
∣
∣
∣ = (n
i2
)
z
i1−i2
i2 ,

or, equivalently, ( n
i1) − 1
(
i2
i1) − 1 z
i1−i2
i1 = 1.

Taking the modulus of both sides of the latter equality, and since from the above discussions |z j| = 1, j =
i1, . . . , ik, we arrive at the conclusion ( n
i1
) = (
i2
i1
)
, n > i2 > i1 ≥ 1,

which ends with a contradiction. Thus the Casas-Alvero conjecture holds true and the proof is complete. □

REFERENCES

1. E. Casas-Alvero, Higher order polar germs, J. Algebra 240 (2001), N 1, 326-337.
2. J. Draisma and J. P. de Jong, On the Casas-Alvero conjecture, Eur. Math.Soc. Newsl., (2011), N 80, 29-33.
3. M.A. Evgrafov, The Abel-Goncharov Interpolation Problem, Gosudarstv. Izdat. Tehn.-Teor. Lit., Moscow, 1954 (in Russian).
4. R.A. Horn, C.R. Johnson, Matrix Analysis, Cambridge University Press, 1985.
5. N. Levinson, The Gontcharoff polynomials, Duke Math. J. 11 (1944), 729- 733.
6. H.-C. Graf von Bothmer, O. Labs, J. Schicho and C. van de Woestijne, The Casas-Alvero conjecture for inﬁnitely many degrees,
J. Algebra, 316 (2007), N 1, 224-230.
7. S. Yakubovich, Polynomial problems of the Casas-Alvero type, Journ. of Classical Analysis, 4(2014), N 2, 97-120.

CASAS-ALVERO CONJECTURE 7

DEPARTMENT OF MATHEMATICS, FAC. SCIENCES OF UNIVERSITY OF PORTO,RUA DO CAMPO ALEGRE, 687; 4169-007
PORTO (PORTUGAL)
E-mail address: syakubov@fc.up.pt
