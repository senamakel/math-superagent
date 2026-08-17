<!-- source: https://repositorio-aberto.up.pt/bitstream/10216/90434/2/171243.pdf | converted from PDF -->

arXiv:1504.00274v2  [math.CA]  14 Aug 2015
TOWARDS THE CASAS-ALVERO CONJECTURE

S. YAKUBOVICH

ABSTRACT. We investigate necessary and sufﬁcient conditions for an arbitrary polynomial of degree n to be
trivial, i.e. to have the form a(z − b)n. These results are related to an open problem, conjectured in 2001
by E. Casas- Alvero. It says, that any complex univariate polynomial, having a common root with each of
its non-constant derivative must be a power of a linear polynomial. In particular, we establish determinantal
representation of the Abel-Goncharov interpolation polynomials, related to the problem and having its own
interest. Among other results are new Sz.-Nagy type identities for complex roots and a generalization of the
Schoenberg conjectured analog of Rolle's theorem for polyn omials with real and complex coefﬁcients.

In 2001 E. Casas-Alvero [1] conjectured that an arbitrary polynomial f degree n ≥ 1 with complex
coefﬁcients of degree n ∈ N
 f (z) = a0z
n + a1z
n−1 + · · · + an−1z + an, a0 ̸= 0 (1)

is of the trivial monomial form f (z) = a(z − b)n, a, b ∈ C, if and only if f shares a root with each of its
derivatives f (1), f (2), . . . , f (n−1). It is proved for small degrees, for inﬁnitely many degrees, for instance, for
all powers n, when n is a prime (see in [2], [8] ). We will call these common roots of the corresponding
derivatives by z1, z2, . . . , zn−1 ∈ C (repeated terms are permitted). As it was recently observed by the author
[11], the polynomial (1), satisfying the Casas- Alvero conditions (the CA-polynomial), can be identiﬁed,
involving the familiar Abel-Goncharov interpolation polynomials [3], which are deﬁned by the following
recurrence relation

f (z) ≡ Gn(z, z0, z1, . . . , zn−1) = z
n − n−1
∑
k=0
 (
n
k
)
z
n−k
k Gk(z, z0, z1, . . . , zk−1), G0(z) ≡ 1 (2)

with the additional conditions (z0 is a root of f )

Gn(z j, z0, z1, . . . , zn−1) = 0, j = 1, 2, . . . , n − 1. (3)

It is known [3], that the Abel-Goncharov polynomial can be represented as a multiple integral in the complex
plane
 f (z) = Gn(z, z0, z1, . . . , zn−1) = n! ∫ z

z0
 ∫ s1

z1 . . . ∫ sn−1

zn−1 dsn . . . ds1 (4)

Moreover, making simple changes of variables in (4), it can be veriﬁed that Gn(z) is shift-invariant and a
homogeneous function of degree n (cf. [7]). Namely, for any α ∈ C\{0}, β ∈ C it has

Gn(αz + β) ≡ Gn (αz + β, αz0 + β, αz1 + β, . . . , αzn−1 + β) = αnGn(z, z0, z1, . . . , zn−1) ≡ αnGn(z). (5)

Date: August 17, 2015.
2000 Mathematics Subject Classiﬁcation. Primary 26C05, 12D10, 41A05 ; Secondary 13F20 .
Key words and phrases. Casas-Alvero conjecture, Abel- Goncharov interpolation polynomials.

1

2 S. YAKUBOVICH

Without loss of generality one can assume in the sequel that f is a monic polynomial of degree n ∈ N, i.e.
a0 = 1 in (1). Generally, it has k distinct roots λj of multiplicities r j, j = 1, . . . , k, 1 ≤ k ≤ n such that

r1 + r2 + . . . rk = n. (6)

By r we denote the maximum of multiplicities in (6), i.e. r = max1≤ j≤k r j. Since for n = 1 the polynomial
is trivial, we will consider n ≥ 2. Moreover, a possible non-trivial CA-polynomial cannot have all distinct
roots, because at least one root is common with its ﬁrst derivative. Therefore the maximum of multiplicities
is at least 2 and a maximum of possible distinct roots is n − 1. Another observation tells that a polynomial
whose distinct roots are of the same multiplicity m ≥ 2, i.e.

f (z) = [(z − λ1)(z − λ2) . . . (z − λk)]m

of degree n = km cannot satisfy the Casas-Alvero conditions since the derivative f (m) has no common roots
with f . Consequently, at least two roots are of different multiplicities.
Recently (see [11]), the author proved the following propositions.
Proposition 1. A polynomial with only real roots of degree n ≥ 2 is trivial, if and only if its n − 2nd
derivative has a double root.
Proposition 2. A possible non-trivial polynomial f of degree n ≥ 6 with only real roots, sharing a root
with its n − 2nd and n − 1st derivatives, has at least ﬁve distinct roots.
Proposition 3. A possible non-trivial polynomial f of degree n ≥ 7 with only real roots, sharing roots
with its n − 2nd and n − 1st derivatives, where roots of the n − 2nd derivative have different multiplicities as
roots of f , has at least six distinct roots.
Basing on the homogeneity property (5) we also proved
Proposition 4. The Casas-Alvero conjecture holds true, if and only if it is true for common roots lying in
the unit circle.
Proposition 5. A possible non-trivial CA-polynomial with only real zeros has at least 5 distinct roots.
Concerning the Abel-Goncharov polynomials it was shown in [11] that Gn satisﬁes the following upper
bound

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

This estimate is sharper than the classical Goncharov upper bound [3]

|Gn(z, z0, z1, . . . , zn−1)| ≤
 (
|z − z0| + n−2
∑
s=0 |zs+1 − zs|
)n .

These polynomials can be represented via the so-called Levinson binomial type expansion (see in [7], p.
732)
 Gn(z, z0, z1, . . . , zn−1) = n
∑
k=1(z
k − z
k
0)
(
n
k
)Hn−k, (7)

CASAS-ALVERO CONJECTURE 3

where H0 = 1 and

Hn−k ≡ Hn−k(zk, zk+1, . . . , zn−1) = (n − k)! ∫ 0

zk
 ∫ sk+1

zk+1 . . . ∫ sn−1

zn−1 dsn . . . dsk+1, k = 1, . . . , n − 1. (8)

However we will prove in turn that the polynomials Hn−k can be represented in a determinantal form of an
upper Hessenberg matrix (n − k) × (n − k) with the entries equal to 1 on the main subdiagonal [5].
Generally, it has
Lemma 1. Let n ∈ N and a j ∈ C, j = 1, . . . , n. Then

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
 . (9)

Proof. Appealing to the principle of mathematical induction and easily verifying formula (9) for n = 1, 2 via
the calculation of the corresponding integral (8), i.e.

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
 . (10)

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

4 S. YAKUBOVICH

Continuing the same process and applying every time the induction hypothesis, we arrive at the ﬁnal expan-
sion of the determinant in the left-hand side of the equality (9)

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
k! Hn+1−k(ak, a3, . . . , an+1). (11)

Fortunately, the expression in the right-hand side of (8) is calculated by Levinson via the Taylor theorem (
cf. [7], p. 731) and we ﬁnd

− n+1
∑
k=1
 ak
1
k! Hn+1−k(ak, a3, . . . , an+1) = 1
(n + 1)! Hn+1(a1, a2, . . . , an+1).

Thus we get the validity of equality (9) for all n ∈ N and complete the proof of the Lemma. □

Corollary 1. The Levinson polynomials Hn, n ∈ N have the following determinantal representation

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
 . (12)

Proof. In fact, the proof easily follows from (9). For this we multiply the last column of the determinant by
n!, the second column by 2!, the third one by 3! etc., and the n − 1-th column by (n − 1)!. Then, dividing the
third row by 2!, the fourth row by 3! etc., and the last row by (n − 1)!, we get the result. □

The determinantal form (12) can be involved to investigate the Casas-Alvero conjecture. Precisely, the
shift-invariant property (5) for the Abel-Goncharov polynomials allows to suppose without loss of generality
that one of the polynomial roots, say, z0 = 0. Then for a ﬁxed sequence {z j}n−1
1 of common roots of f and
its derivatives up to the order n − 1 (7) implies

Gn(z, 0, z1, . . . , zn−1) = n
∑
k=1 z
k(
n
k
)
Hn−k. (13)

Assuming the existence of a possible non-trivial CA-polynomial f , it follows that at least one of z1, . . . , zn−1
is nonzero, otherwise the polynomial has the unique root of multiplicity n, which is equal to zero. Let f have
s nonzero common roots (1 ≤ s ≤ n − 1) in our sequence {z j}n−1
1

z j, j = i1, . . . , is, {i1, . . . , is} ⊂ {1, . . . , n − 1}, 1 ≤ i1 < i2 < · · · < is ≤ n − 1, (14)

corresponding the derivatives of the order i1, . . . , is, respectively. Hence, appealing to Corollary 1 and ob-
serving from (4) and (8) that the left-hand side of (13) equals to −Hn(z, z1, . . . , zn−1), we end up with the

CASAS-ALVERO CONJECTURE 5

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
 . (14)

Moreover, the determinant (14) can be compressed, eliminating rows, containing only one nonzero element
of the main subdiagonal of Hessenberg's matrix, which is equ al to 1. Therefore, we arrive at the equality for
any z ̸= 0
 (−1)
s z
−i1Hn(z, z1, z2, . . . , zn−1) =
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

1 zi2−i1 . . . zis−i1 zn−i1

1 (i2
i1)
z
i2−i1
i1 . . . (ik
i1)
z
is−i1
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
0 0 . . . 1 (n
is)
z
n−is
is
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
 , (15)

containing the determinant of the order (s + 1) × (s + 1). Now, taking into account the conditions (see (3))

Hn(z j, z1, . . . , zn−1) = 0, z j ̸= 0, j = i1, i2, . . . , is, (16)

we have ∣
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
is−i1
j z
n−i1
j
1 (
i2
i1)
z
i2−i1
i1 . . . (ik
i1)
z
is−i1
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
... . . . . . . . . . ...
0 0 . . . 1 (n
is)
z
n−is
is
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
 = 0, j = i1, . . . , is. (17)

Let s = 1, i.e. the polynomial has only one nonzero root zi1 ̸= 0 in our sequence of common roots z1, z2, . . . , zn−1,
which corresponds to the i1-th derivative. Hence, putting in (17) j = i1, the determinant
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
∣ = 0. (18)

But this is impossible, since we have ( n
i1) = 1, n > i1 ≥ 1. Hence 2 ≤ s ≤ n − 1. Returning to (13) and using
conditions (16), we sum up these s equalities to obtain

s+1
∑
j=1
 s+1
∑
m=1 z
im
i j
 ( n
im
)
Hn−im(zim , 0, . . . , zim+1, . . . , zn−1) = s+1
∑
m=1
 ( n
im
)
PmHn−im = 0, (19)

where is+1 = n and Pm = ∑
s+1
j=1 z
im
i j . Equalities (19) are analogs of the familiar Newton identities for nonzero
roots of a possible non-trivial CA-polynomial.
Recalling distinct roots of f (z) λj, j = 1, . . . , k and assuming that the root of the n − 1st derivative takes,
for instance, the value λ1, we use the ﬁrst Vi´ete formula to write the identity (cf. [11])

k
∑
j=2 r j(λj − λ1) = 0. (20)

6 S. YAKUBOVICH

Proposition 6. A possible non-trivial polynomial of degree n ≥ 2 with k distinct roots λj, j = 1, . . . , k,
sharing the root λ1 with its n − 1st derivative must contain at least one root λj, j ̸= 1 outside of the disk
Dµ = {z ∈ C : |z − λ1 − 1| ≤ µ} , µ ∈ (0, 1).

Proof. The proof is based on the inequality involving weighted arithmetic and geometric means for complex
numbers proved in [4]. Indeed, let λj ∈ Dµ, j ̸= 1. Then according to [4] we ﬁnd from equality (20) the
following estimate

0 = 1
(1 − µ2)(n − r1)
 ∣
∣
∣
∣
∣
 k
∑
j=2r j(λj − λ1)

∣
∣
∣
∣
∣ ≥ 1 − µ
2µ log ( 1 + µ
1 − µ
 ) exp (
1 − 1 − µ
2µ log ( 1 + µ
1 − µ
 ))

× k
∏
j=2
∣
∣λj − λ1∣
∣r j/(n−r1) ̸= 0,

which gives a contradiction. □

Employing the Sz.-Nagy type identity for complex roots of f and its mth derivative

(zn−1 − zn−2)
2 = 1
n(n − 1)
 [ k
∑
j=1 r j(λj − z)
2 − n(zn−1 − z)
2]

= 1
(n − m)(n − m − 1)
 [n−m
∑
j=1(ξ (m)
j − z)
2 − (n − m)(zn−1 − z)
2]
 , z ∈ C, (21)

which is proved in [11], we let m = 1 and z = 0, writing, in particular, the equality

n−1
∑
j=1
 [
ξ (1)
j ]2 = n − 2
n
 k
∑
j=1 r jλ 2
j + z
2
n−1. (22)

The unique root zn−1 of the n − 1st derivative is called the centroid of the sets λj and ξ (m)
j and it satisﬁes the
Sz.-Nagy type identity (cf. [11])

zn−1 − z = 1
n
 k
∑
j=1r j(λj − z) = 1
n − m
 n−m
∑
j=1(ξ (m)
j − z), z ∈ C. (23)

But since among the roots of the ﬁrst derivative f ′ are roots λj of multiplicities r j − 1, correspondingly, we
let m = 1 and z = 0 in (23) to ﬁnd k
∑
j=1λj = k−1
∑
j=1 ˆξ (1)
j + zn−1, (24)

where ˆξ (1)
j are roots of the logarithmic derivative (log f (z))′. The corresponding identity for squares of these
roots can be obtained from (21), (22), and we have

k−1
∑
j=1
[ ˆξ (1)
j ]2 = k
∑
j=1 λ 2
j − 2(n − 1)(zn−1 − zn−2)
2 − z
2
n−1. (25)

Following [9] we say that the set of 2n − 1 points is rectilinear, if k roots λj with multiplicities r j and n − 1
roots ξ (1)
j are on a straight line in the complex plane, which passes through the origin. Then the centroid
zn−1 and the root zn−2 of the n − 2nd derivative are contained on this line as well. Hence there is an angle ϕ

CASAS-ALVERO CONJECTURE 7

such that λj = ±|λj|eiϕ, ξ (1)
j = ±|ξ (1)
j |eiϕ for all j and zn−1 = ±|zn−1|eiϕ, zn−2 = ±|zn−2|eiϕ. Consequently,
equalities (22) and (25) imply the identities

n−1
∑
j=1
 ∣
∣
∣ξ (1)
j ∣
∣
∣2 = n − 2
n
 k
∑
j=1r j |λ|2
j + |zn−1|2 , (26)

k−1
∑
j=1
∣
∣
∣ ˆξ (1)
j ∣
∣
∣2 = k
∑
j=1|λ|2
j − 2(n − 1) (|zn−1| − |zn−2|)2 − |zn−1|2 , (27)

respectively. When zn−1 = ±|zn−1|eiϕ but zn−2 = ∓|zn−2|eiϕ the latter equality becomes

k−1
∑
j=1
∣
∣
∣ ˆξ (1)
j ∣
∣
∣2 = k
∑
j=1|λ|2
j − 2(n − 1) (|zn−1| + |zn−2|)2 − |zn−1|2 . (28)

Furthermore, equality (26) suggests a generalization of the Schoenberg conjecture. Indeed, we have
Conjecture 1. For any complex roots of f and its ﬁrst derivative we have the inequality

n−1
∑
j=1
 ∣
∣
∣ξ (1)
j ∣
∣
∣2 ≤ n − 2
n
 k
∑
j=1r j |λ|2
j + |zn−1|2 , (29)

with the equality sign if and only if all roots lie on a straight line, passing through the origin.
The Sz.-Nagy type identities (21) yield the following proposition for polynomials (1) whose centroid is
zero.
Proposition 7. A monic polynomial f of degree n ≥ 2 whose roots lie on a straight line passing through
the origin is f (z) = zn , if and only if z = 0 is the double root of the n − 2nd derivative.

Proof. The necessity is obvious. To prove the sufﬁciency we see that if zn−2 = zn−1 = 0 then the ﬁrst identity
in (21) with z = 0 presumes
 k
∑
j=1r jλ 2
j = 0.

But since λj = ±|λj|eiϕ, j = 1, . . . , k it has all roots should be zero and f (z) = zn. □

Further, we generalize Proposition1 for polynomials whose roots are lying on the vertical or horizontal
line of the complex plane. In fact, we have
Proposition 8. A polynomial of degree n ≥ 2 whose roots lie on the vertical (horizontal ) line of the
complex plane is trivial, if and only if its n − 2nd derivative has a double root.

Proof. Let distinct roots have the form λj = a + i Imλj, a ∈ R, j = 1, . . . , k and zn−2 is the double root of
n − 2nd derivative. Then zn−2 = zn−1. Hence the left-hand side of the ﬁrst identity in (21) is zero. Moreover,
evidently, the centroid lies on the same vertical line. Letting in (21) z = zn−1 it gives

k
∑
j=1r j(λj − zn−1)
2 = 0

or k
∑
j=1r jIm2 [λj − zn−1] = 0.

Hence, Imλj = Imzn−1, j = 2, . . . , k and the polynomial is trivial. On the same manner we prove the propo-
sition for roots lying on the horizontal line of the complex plane. The necessity is obvious. □

8 S. YAKUBOVICH

Recalling identity (25) we generalize it for polynomials of degree n ≥ 2 with simple n roots w j, j =
1, . . . , n and roots of its m-th derivative. Precisely, with the use of (21) we ﬁnd

n−m
∑
j=1
 [
ξ (m)
j ]2 = n
∑
j=1 w
2
j − m(2n − m − 1)(zn−1 − zn−2)
2 − mz
2
n−1, m = 0, 1, . . . , n. (30)

Next we will derive a formula, involving higher order derivatives of log f (z), which seems to be new.
Lemma 2. Let m ∈ N0, z ∈ C and f (z) ̸= 0. Then the following formula takes place

(log f (z))(m+1) = ( f ′(z)
f (z)
 )(m) = m
∑
j=0
 (−1) j

j + 1
 (
m + 1
j + 1
 ) (
[ f (z)] j+1)(m+1)

[ f (z)] j+1 . (31)

Proof. In order to prove (31) we call the familiar Hoppe formula (see [6], p. 224) for higher derivatives of
the composition of two functions. Thus we derive

(log f (z))(m+1) = ( f ′(z)
f (z)
 )(m) = m+1
∑
s=0
 (−1)s(s − 1)!
s! [ f (z)]s
 s
∑
j=0
(−1)
s− j(s
j
) [ f (z)]s− j ([ f (z)] j)(m+1)

= m+1
∑
s=0 (s − 1)! s
∑
j=0
 (−1) j+1

j!(s − j)!
 ([ f (z)] j)(m+1)

[ f (z)] j

= m+1
∑
j=0(−1) j+1
 (
[ f (z)] j)(m+1)

j! [ f (z)] j
 m
∑
s= j−1
 s!
(s + 1 − j)!

= m+1
∑
j=1(−1) j+1
 ([ f (z)] j)(m+1)

j! [ f (z)] j
 m
∑
s= j−1
 s!
(s + 1 − j)!.

Hence a simple substitution in the index of summation and the use of the combinatorial identity

m
∑
s= j
 (s
j
) = (
m + 1
j + 1
 )

lead to (31) and complete the proof of Lemma 2. □

Let a possible non-trivial CA- polynomial f have real zeros only . Proposition 5 says that it has at least 5
distinct zeros, i.e k ≥ 5. Then, by virtue of the Rolle theorem all zeros of the derivatives f ( j)(x), x ∈ R, j =
r − 1, r, . . . , n − 1, where 2 ≤ r = max1≤ j≤k r j are simple. Denoting by

A = {λ1, . . . , λk}, B j = {ξ ( j)
1 , . . . , ξ ( j)
n− j}, j = r − 1, r, . . . , n − 1

sets of roots of f and its mth derivatives, we have by deﬁnition of the CA-polynomial B j ∩ A ̸= /0, j =
r − 1, r, . . . , n − 1. Moreover, letting in (31) m = 1, we write the Laguerre inequality for derivatives f ( j) (see,
for instance, in [10]) d2

dx2
 [
log f ( j)(x)
] < 0, j = r − 1, r, . . . , n − 2, (32)

or, in the equivalent form, [ f ( j+1)(x)
]2 > f ( j)(x) f ( j+2)(x), j = r − 1, r, . . . , n − 2. (33)

CASAS-ALVERO CONJECTURE 9

The latter inequality implies the property B j ∩ B j+1 = /0. Let C j ⊂ A be a subset of B j, containing n j ∈ N
common roots of f ( j) with f , i.e. C j = {λj,1, . . . , λj,n j } ⊂ B j.
Clearly, the number nr−1 of common roots with the r − 1st derivative does not exceed min(k − 1, n − r + 1)
and n j ≤ min(k − 2, n − j) j = r, . . . , n − 1 because the minimal and maximal roots of f cannot be zeros of
f ( j), j ≥ r. Condition (33) says that it may happen that C j ∩C j+2 ̸= /0, 2 ≤ s ≤ n − r. Writing equality (30)
for roots of the m th and m + s th derivatives, where r − 1 ≤ m ≤ n − s − 1, we ﬁnd

n−m
∑
j=1
 [
ξ (m)
j ]2 − n−m−s
∑
j=1
 [
ξ (m+s)
j ]2 = s(2(n − m) − s − 1)(xn−1 − xn−2)
2 + sx2
n−1. (34)

Hence we arrive at
Proposition 9. Let m = r − 1, r, . . . , n − 1, where 2 ≤ r = max1≤ j≤k r j and 2 ≤ s ≤ n − r. Then roots of
the m th and m + sth derivatives of a possible non-trivial CA-polynomial with only real zeros satisfy the
condition ∑

1≤ j≤n−m, ξ (m)
j /∈ Cm∩Cm+s
 [
ξ (m)
j ]2 ≥ ∑

1≤ j≤n−m−s, ξ (m)
j /∈ Cm∩Cm+s
 [
ξ (m+s)
j ]2 .

REFERENCES

1. E. Casas-Alvero, Higher order polar germs, J. Algebra 240 (2001), N 1, 326-337.
2. J. Draisma and J. P. de Jong, On the Casas-Alvero conjecture, Eur. Math.Soc. Newsl., (2011), N 80, 29-33.
3. M.A. Evgrafov, The Abel-Goncharov Interpolation Problem, Gosudarstv. Izdat. Tehn.-Teor. Lit., Moscow, 1954 (in Russian).
4. R. Fournier, Inequalities involving weighted means in a disk of the complex plane, Journ. of Math. Anal. and Appl., 243 (2000),
313- 325.
5. R.A. Horn, C.R. Johnson, Matrix Analysis, Cambridge University Press, 1985.
6. W.P. Johnson, The curious history of Faa di Bruno's formul a, The Amer. Math. Monthly, 109 (2002), 3, 217- 234.
7. N. Levinson, The Gontcharoff polynomials, Duke Math. J. 11 (1944), 729- 733.
8. H.-C. Graf von Bothmer, O. Labs, J. Schicho and C. van de Woestijne, The Casas-Alvero conjecture for inﬁnitely many degrees,
J. Algebra, 316 (2007), N 1, 224-230.
9. I.T. Schoenberg, A conjectured analog of Rolle's theorem for polynomials with real and complex coefﬁcients, The Amer. Math.
Monthly, 93(1986), 8-13.
10. B. Shapiro, Problems around polynomials: the good, the bad and the ugly... , Arnold Math. J., DOI 10.1007/s40598-015-0008-4
(2015).
11. S. Yakubovich, Polynomial problems of the Casas-Alvero type, Journ. of Classical Analysis, 4(2014), N 2, 97-120.

DEPARTMENT OF MATHEMATICS, FAC. SCIENCES OF UNIVERSITY OF PORTO,RUA DO CAMPO ALEGRE, 687; 4169-007
PORTO (PORTUGAL)
E-mail address: syakubov@fc.up.pt
