<!-- source: https://imar.ro/journals/Revue_Mathematique/pdfs/2019/1/6.pdf | converted from PDF -->

EHRHART POLYNOMIAL FOR LATTICE SQUARES, CUBES AND HYPERCUBES
 EUGEN J. IONASCU

Communicated by Alexandru Zaharescu

In this paper, we are constructing integer lattice squares, cubes or hypercubes in
Rn with n ∈ {2, 3, 4}. We ˝nd a complete description of their Ehrhart polyno-
mial. We characterize all the integer squares in R4, in terms of two Pythagorean
quadruple representations of the form a
2 + b2 + c
2 = d2, and then prove a pa-
rametrization in terms of two quaternions of all such squares. We introduce the
sequence of almost perfect squares in dimension n . In dimension two, this is very
close to the sequence A194154 (in OEIS).

AMS 2010 Subject Classi˝cation: 52C07, 05A15, 68R05.

Key words: Ehrhart polynomial, linear Diophantine equations, lattice square,
lattice cube, quaternions, icube, Pythagorean quadruple, twin vec-
tors.
 1. INTRODUCTION

Eug`ene Ehrhart [9,10] proved that given a d-dimensional compact simpli-
cial complex in Rn ( 1 ≤ d ≤ n), denoted here generically by P, whose vertices
are in the lattice Zn, there exists a polynomial L(P, t) ∈ Q[t] of degree d,
associated with P, satisfying

L(P, t) = the cardinality of {tP} ∩ Z
n, t ∈ N.

It is very interesting that one can say more about three of the coe˚cients
of L(P, t):

(1) L(P, t) = V ol(P)td + 1
2 V ol(∂P)t
d−1 + ... + χ(P),

where V ol(P) is the usual volume of P normalized with respect to the sublattice
containing P, V ol(∂P) is the surface area of P normalized with respect to the
sublattice on each face of P and χ(P) is the Euler characteristic of P (in the
sense of polytopal complexes, so for a convex polytope it is equal to one). In
general, the other coe˚cients in (1) may have complicated expressions in terms
of the vertices of P.

REV. ROUMAINE MATH. PURES APPL. 64 (2019), 1, 5780

58 Eugen J. Ionascu 2

It is also known that the number of points in the interior of tP is given
by (−1)dL(P, −t). For a polytope that is a cross product of two polytopes, the
Ehrhart polynomial is the product of the corresponding smaller degree Ehrhart
polynomials. In this article, we are studying this polynomial for lattice squares,
cubes, and hypercubes in Rn. Such objects have been constructed and counted
in several works (see [13, 15, 20, 25]).
 2. SQUARES

2.1. Squares in two dimensions

How general can a lattice square in two dimensions look like? We may
assume that one of the vertices is at the origin. Then the other vertices, in
counterclockwise order, are given by A(a, b), B(a − b, a + b) and C(−b, a) where
a and b are integers, not both zero, and such that gcd(a, b) = 1. Using the
facts mentioned in the Introduction, the polynomial in (1) is simply E2(t) =
(a2 + b2)t2 + 2t + 1 and of course, E ◦
2(t) = (a2 + b2)t2 − 2t + 1, t ∈ N.

Fig. 1  Square with a = 5 and b = 2.

In Figure 1, we see the 28 points inside of the square OABC, with A(5, 2),
B(3, 8) and C(−2, 5). One interesting problem here is to determine the sequence

3 Ehrhart polynomial for lattice squares, cubes and hypercubes 59

of possible lattice points in the interior of such a square. The ˝rst hundred terms
of this sequence, listed in increasing order, are included in the table below:

0 1 4 5 9 12 13 16 17 24 25 28 33 36 37 40 41 49 52 57
60 61 64 65 72 73 81 84 85 88 96 97 100 101 105 108 112 113 116 121
124 129 133 136 144 145 148 153 156 161 168 169 172 177 180 181 184 192 193 196
197 201 204 209 217 220 221 225 228 229 232 240 241 249 256 257 264 265 268 273
276 280 288 289 292 293 297 301 304 305 312 313 316 324 325 328 336 337 345 348

Let us call this sequence the almost perfect squares sequence. In Figure 2,
we see some of the squares that show that the above numbers are indeed in
the sequence. As a curiosity, 2015 is not in this sequence but 2016 is. This
sequence is very close to A194154 in the OEIS (On-Line Encyclopedia of Integer
Sequences), but 20 is the ˝rst term that is not in our sequence.

Fig. 2  Various squares.

Let us give a reformulation of the exact form of the Ehrhart polyno-
mial above in conjunction with the reciprocity property (about interior points),
which can by shown independently using Pick's Theorem.

Proposition 2.1 . Given a, b with gcd(a, b) = 1 and t ∈ N, then

♯{(x, y) ∈ Z
2 : ax + by, ay − bx ∈ [1, t(a2 + b
2) − 1]} = (a2 + b
2)t
2 − 2t + 1.

Proof. Counting the points inside the square OABC, with O(0, 0), A(a, b),
B(a − b, a + b) and C(−b, a), is equivalent to count the solutions (x, y) of the
system (x, y) = α(ta, tb) + β(−tb, ta) with α, β ∈ (0, 1). Since α = (x, y) ·
(a, b)/t(a2 + b2) = ax+by
t(a2+b2) and β = (x, y) · (−b, a)/t(a2 + b2) = ay−bx
t(a2+b2) we see
that the constraints on α and β is equivalent to ax + by, ay − bx ∈ [1, t(a2 +
b2) − 1]. Hence, the result follows from the Ehrhart polynomial expression. □

60 Eugen J. Ionascu 4

So, every term of the sequence of almost perfect squares is the answer to
a counting as in Proposition 2.1, which in particular gives the justi˝cation of
one of our earlier claims:
 ♯{(x, y) ∈ Z
2 : 44x + 9y, 44y − 9x ∈ [1, 2016]} = 2016.

2.2. Squares in three dimensions

In R3, we can obtain a lattice square by taking two orthogonal vectors
with integer coordinates of the same length: u = (a, b, c), v = (a′, b′, c′) such
that a2 + b2 + c2 = a′2 + b′2 + c′2 = ℓ and aa′ + bb′ + cc′ = 0. In [13], two
such vectors are called twin vectors. The number of such twin vectors having
a given length is calculated in [13]. In [20], this concept is generalized to m
dimensions and called m-icube (a set of m vectors in Zn, mutually orthogonal
and of the same length). Since we are interested in generalizing these ideas to
any dimension, we are going to use this terminology also.
Although it does not make much of a di˙erence it is natural to assume that
the square is irreducible , i.e., gcd(a, b, c, a′, b′, c′) = 1. If we set d = gcd(a, b, c),
d′ = gcd(a′, b′, c′) and D = gcd(bc′−b′c, ac′−a′c, ab′−b′a), we have the following
more general formula, than in two dimensions, for the E2(t).

Theorem 2.2 . The Ehrhart polynomial of a lattice square embedded into
R3, described above and with the notation introduced is given by

(2) E2(t) = Dt
2 + (d + d
′)t + 1.

Proof. The fundamental domain of the lattice containing the triangle has
a volume equal to √
n2
1 + n2
2 + n2
3 where −→n = [n1, n2, n3] is a vector normal
to the plane containing the triangle and such that gcd(n1, n2, n3) = 1 (see [1]
and [19]). Such a vector is given clearly by the cross-product of u and v:
n = 1
D u × v = 1
D (bc′ − b′c, −(ac′ − a′c), ab′ − b′a). Let us observe that because
of Lagrange's Identity ℓ2 = (a2 + b2 + c2)(a′2 + b′2 + c′2) = (aa′ + bb′ + cc′)2 +
(bc′ − b′c)2 + (ac′ − a′c)2 + (ab′ − b′a)2, we conclude that |n| = ℓ
D . Hence, we see

that the ˝rst coe˚cient of the Ehrhart polynomial is √ℓ2/( ℓ
D ) = D. Similar
argument goes for the second coe˚cient. □

Standard Examples. Let us analyze some examples which are not xy, xz
or yz-plane examples. First, let us take u = (3, −3, 0) and v = (1, 1, 4); observe
that |u|2 = |v|2 = 18 and u · v = 0. In this case n = 6(−2, −2, 1), and the
equation of the plane is 2x + 2y − z = 0 and E2(t) = 6t2 + 4t + 1. We know
that E2(−1) = 3 represents the number of lattice points in the interior of
the square. We notice that 3 (and E2(−2) = 17) was not an almost perfect

5 Ehrhart polynomial for lattice squares, cubes and hypercubes 61

number. Hence we may want to generalize that sequence to almost perfect
squares in dimension n.
What is interesting is that in the plane 2x + 2y − z = 0 we have another
square: u = (2, −1, 2) and v = (−1, 2, 2). Also, the square above can be
written in terms of this one basically like in two dimensions: u = u − v and
v = u + v. For this square, n = 3(−2, −2, 1) and so the Ehrhart polynomial is
E{u,v}(t) = 3t2 + 2t + 1. We see that E{u,v}(−1) = 2 which is yet new for the
almost perfect square sequence compared with dimension two.
If we take the twin vectors u = (6, −2, 3) and v = (−2, 3, 6) we get
n = 7(−3, −6, 2) and so the Ehrhart polynomial is E(t) = 7t2 + 2t + 1. There
seem to be very few numbers that are not perfect squares in 3D: 7, 14, 23,...
For an example of an irreducible square, for which d and d′ in Theorem 2.2
are both greater than one, we refer to u = 5(8, 12, 9) and v = 17(0, −3, 4). Its
polynomial is E(t) = (5t + 1)(17t + 1).
How does one construct such squares in R3? We observed in the proof
of Theorem 2.2 that every such square is contained in a plane whose normal
n = (n1, n2, n3) satis˝es

(3) ℓ2 = n2
1 + n2
2 + n2
3.

A solution of this type of Diophantine equation is usually referred in the
literature as a Pythagorean quadruple . For the number of primitive solutions of
(3) in terms of ℓ, we refer the reader to a recent paper of Werner H¨urlimann [15]
but also [4]. There are at least two other terms used for these quadruples of
integers: cuboids [15] and Lorenz quadruples (see [14]). We include in the next
tables all primitive solutions for odd values ℓ ∈ {1, 3, ..19}:

ℓ [a,b,c], gcd(a, b, c) = 1, c even
1 [1,0,0]
3 [1,2,2]
5 [3,4,0]
7 [3,6,2]
9 [1, 4, 8], [7, 4, 4]
 ,
 ℓ [a,b,c], gcd(a, b, c) = 1 , c even
11 [9, 2, 6], [7, 6, 6]
13 [5, 12, 0], [3, 4, 12]
15 [5, 14, 2], [11, 2, 10]
17 [15, 0, 8], [1, 12, 12], [9, 12, 8]
19 [1, 6, 18], [17, 6, 6], [15, 6, 10]

So, having a Pythagorean quadruple, how can we construct a related twin
set of vectors? We include a partial answer to this question at this point, but
we will include the complete solution later in this paper.

Theorem 2.3 . Suppose that u′ = (a, b, c) satis˝es n1a + n2b + n3c = 0,
where n2
1 + n2
2 + n2
3 = ℓ2 with all variables involved being integers. Then there
exist v = (a′, b′, c′) such that ℓu′ and v de˝ne a lattice square in the plane of
normal n = (n1, n2, n3).

62 Eugen J. Ionascu 6

Proof. We de˝ne v to be the cross-product of u′ and n. Clearly v is per-
pendicular to n and so it is in the right plane. Since u′ and n are perpendicular,
|v| = |u′||n| = ℓ|u′|. □

It is natural to look for the smallest square in the plane n1a+n2b+n3c =
0. This leads us to the shortest vector problem (SVP), i.e. , ˝nding a non-zero
vector in a lattice of minimum norm. An interesting problem, at this point, is
to characterize all the values ℓ so that √ℓ appears as side-lengths for an lattice
embedded square in Rm, m ≥ 2. If we denote this set by L, from the two
dimensions construction, we see that L is invariant under multiplication with
numbers which are sums of two squares. For m = 3, it is also clear all the
numbers of the form 4k(8s − 1) are not in L, since these are not representable
as sums of three squares (Legendre's three-square theorem). Also, 3, 11 or 19
(see the sequence A223732 in OEIS) are not in L, since they have only one
representation as sum of three squares and these representations contain only
odd numbers. Hence the sum aa′ + bb′ + cc′ is also odd and so, it cannot be
zero. We will describe the set L at the end of the subsection. We will see that
in R4 and beyond, L = N.
We have the following parametrization for those squares whose side-lengths
are natural numbers of the form x2 + y2 + z2 + t2 (see [18] and [25]):

(4) u := (2ty + 2zx, 2tz − 2yx, t
2 − z2 − y2 + x2), v := (2zy − 2tx,

z2 − t
2 + x2 − y2, 2tz + 2yx),

having normal vector n = (−x2 + t2 − y2 + z2, −2(tx + zy), 2(ty − zx)), |n| =
x2 + y2 + z2 + t2. Next, we show that, as in [18] and [25], the following similar
parametrization for the solutions of (3) takes place. The proof is essentially the
same as in [25] but we include it for the convenience of the reader.

Theorem 2.4 ( [25]) . Every primitive solution of (3), after a permutation
of variables and change of signs, is given by n1 = 2(zy − tx), n2 = 2(tz + yx)
and n3 = z2 − t2 + x2 − y2, and ℓ = x2 + y2 + z2 + t2 for some integers x, y, z
and t.
Proof. As usual, a primitive solution of (3) is one for which gcd(n1, n2, n3)
= 1. We must have ℓ odd since otherwise gcd(n1, n2, n3) ≥ 2. In this case, one
of the ni must be odd and the other two even. Without loss of generality, let
us assume that n1 and n2 are even. Then, we have

(ℓ − n3)(ℓ + n3) = n2
1 + n2
2.

We know that ℓ + n3 = 2α and ℓ − n3 = 2β are both even, and then the above
equality becomes
 αβ = (n1/2)
2 + (n2/2)
2 = A2 + B2 = (A + Bi)(A − Bi),

7 Ehrhart polynomial for lattice squares, cubes and hypercubes 63

where A = n1/2 and B = n2/2. A Gaussian prime of the form p = 4k + 3
which divides αβ, must divide both A and B. So, it cannot divide both α and
β because it then divides ℓ = (α + β)/2 and n3 = (α − β)/2, which implies
that gcd(n1, n2, n3) ≥ p. Hence, α and β are both sums of two squares. If we
let gcd(A + iB, α) = t + iy and gcd(A + iB, β) = x + iz. Let us make the
observation that these equalities are de˝ned up to a unit, i.e. , ±1 or ±i.
Since α is real, t − iy divides α and so α = (t2 + y2)α′. But every prime
factor of α, appears as a factor of either A + Bi or A − Bi. Taking into account
the multiplicities we see that α divides t2 + y2 and so α′ = 1. Similarly, we have
β = x2 + z2. Also, t + iy divides A + iB and also x + iz divides A + iB. Hence
A + iB = (t + iy)(x + iz)k and from here A2 + B2 = (t2 + y2)(x2 + z2)|k|2 which
together with what we have shown earlier forces |k| = 1. So, by changing x
and y we can assume that k = 1. Hence we have A = tx − zy and B = xy + tz.
Then ℓ = α + β = x2 + y2 + z2 + t2 and n3 = α − β = t2 + y2 − x2 − z2. □

Theorem 2.4 allows us to characterize L. The result is not new, as we
found recently, it is contained in [13]. We include a proof of it, based on our
development of the ideas.
 Theorem 2.5 . The set of all ℓ so that √ℓ is the side-lengths for an em-
bedded square in Z3 is the set of positive integers which are sums of two squares.

Proof. In one direction, i.e. , L contains the set of all positive integers
which are sums of two squares, we can observe that the lengths for squares in
two dimensions are of the form √a2 + b2. For the other direction, if we start
with an arbitrary square, S, in Z3, let us suppose the side is √ℓ. As in the proof
of Theorem 2.3, this square is contained in a plane of normal n = (n1, n2, n3),
with n2
1 + n2
2 + n2
3 = ℓ2. By Theorem 2.4, we can ˝nd x, y, z and t, such
that n1 = 2zy − 2tx, n2 = 2tz + 2yx and n3 = z2 − t2 + x2 − y2. Then the
parametrization (4) gives a square in the same plane as S, whose sides are ℓ.
We can then write the vector of this square in the basis given by two of the
vectors in S: w = αu + βv for some α and β ∈ Q. Then, taking norms we
get ℓ2 = α2ℓ + β2ℓ so ℓ = α2 + β2. This shows that ℓ = A2 + B2 for some A,
B ∈ Z. □

Theorem 2.3 and Theorem 2.5 imply the next consequence which one can
also prove elementary.
 Corollary 2.6 . Given a point P = (x, y, z) ∈ Z3 in the plane of equation
n1x + n2y + n3z = 0 with n2
1 + n2
2 + n2
3 = ℓ2 for some ℓ ∈ N, then the number
x2 + y2 + z2 is actually a sum of two squares.

64 Eugen J. Ionascu 8

2.3. Squares in R4

Perhaps, one of the simplest ways to construct squares in Z4 is to take two
squares in two dimensions and add them together, each on its own dimensions.
In other words, the two vectors u and v that de˝ne the square, as we have seen
before, are of the form u = (a, b, c, d) and v = (−b, a, −d, c). We have clearly
u · v = 0 and ∥u∥2 = ∥v∥2 = a2 + b2 + c2 + d2. This simple example allows
us to answer the question about the possible side-lengths of such squares. By
Lagrange's Four Square Theorem, we see that every natural number is a possible
side-length of a square. Are these squares the most general situation that one
can expect? We observe that u and v are essentially the ˝rst two rows of the
following pseudo-orthogonal matrix (every two rows are mutually orthogonal
and have the same norm):
 Oa,b,c,d =
 




 a b c d
−b a d −c
−c −d a b
−d c −b a
 



 .

It is not di˚cult to see that the product of matrices like these ( OT O = tI)
is of the same form. This allows one to de˝ne a certain multiplication on vectors
in R4 which is exactly the quaternion multiplication that we will be using latter.

Example 1 . Let us compute the Ehrhart polynomial for a particular case
like this which gives a new value for its sides. We have u = (2, 1, 1, 1) and
v = (−1, 2, −1, 1). Using the same idea as in the three dimensions we are
computing two normal vectors that de˝ne the orthogonal space of the plane
generated by u and v. For a generic point P = (x, y, z, t) ∈ R4, the two
equations, computed with the help of the cross-product in the three dimensions,
are 3x − y − 5z = 0 and 2y + z − 3t = 0.

We observe that both u and v satisfy these equations. Since these two equations
can be solved for y and t, we can ˝nd two integer vectors which generate the
lattice Z4 intersected with the plane de˝ned by u and v: y = 3x − 5z and
t = 2x − 3z which gives the two vectors α = (1, 3, 0, 2) and β = (0, −5, 1, −3).
We know then that these two vectors form a fundamental domain, so we need
to compute the area of the parallelogram generated by these two vectors: A =
|α||β| sin(γ) where cos γ = α · β/|α||β| = −3/
√10. This gives A = 7 and so,
the Ehrhart polynomial is
 E2(t) = t
2 + 2t + 1 = (t + 1)2.

9 Ehrhart polynomial for lattice squares, cubes and hypercubes 65

For a set of vectors S in R4 we denote as usual by S ⊥ the set of all vectors
x ∈ R4 perpendicular to every vector v in S, i.e. ,

S ⊥ = {(x1, x2, x3, x4) ∈ R4|x1v1 + x2v2 + x3v3 + x4v4 = 0

for all v = (v1, v2, v3, v4), v ∈ S}.

Theorem 2.7 . (i) Given integer vectors u = (u1, u2, u3, u4) and v =
(v1, v2, v3, v4) such that

0 < ℓ = u
2
1 + u
2
2 + u
2
3 + u
2
4 = v2
1 + v2
2 + v2
3 + v2
4, u1v1 + u2v2 + u3v3 + u4v4 = 0,

then there exist an odd k ∈ N dividing ℓ and two vectors w1 and w2 with
integer coordinates such that w1 = (0, α1 − β1, α2 − β2, α3 − β3) and w2 =
(α3 − β3, −α2 − β2, α1 + β1, 0) with

(5) k2 = α2
1 + α2
2 + α2
3 = β2
1 + β2
2 + β2
3,

αi and βi of the same parity and u, v ∈ {w1, w2}⊥. One can permute the
coordinates of u and v and/or change their signs in order to have w1 and w2
linearly independent. (ii) If gcd(α1, β1, α2, β2, α3, β3) = 1 then the volume of the fundamental
domain of the minimal lattice containing u and v is equal to k.

Proof. Using Lagrange's Identity, we get

ℓ
2 = (
 4∑

i=1 u
2
i )(
 4∑

i=1 v2
i ) = (
 4∑

i=1 uivi)2 + ∑

1≤i<j≤4
(uivj − ujvi)
2.

Since u1v1 + u2v2 + u3v3 + u4v4 = 0, this implies that

(6) ℓ2 = ∑

1≤i<j≤4(uivj − ujvi)
2.

If we denote by ∆ij = (−1)i−j(uivj − ujvi), it is not di˚cult to check that

(7) ∆12∆34 − ∆13∆24 + ∆14∆23 = 0.

This helps us change (6) into

(8) ℓ2 = (∆12 ± ∆34)
2 + (∆13 ∓ ∆24)
2 + (∆14 ± ∆23)2.

One can check that

(9)
 




u1(0) + u2∆34 + u3∆24 + u4∆23 = 0
v1(0) + v2∆34 + v3∆24 + v4∆23 = 0
u1∆23 + u2∆13 + u3∆12 + u4(0) = 0
v1∆23 + v2∆13 + v3∆12 + v4(0) = 0.

66 Eugen J. Ionascu 10

Let us observe that if 2 divides ℓ, then all ∆ij are divisible by 2, because all
ui ( vi) are all even or all odd. In order to prove the claim, we simplify (8) by
the greatest power of 2 possible and take α1 = (∆12 + ∆34)/ℓ′, α2 = (−∆13 +
∆24)/ℓ′, α3 = (∆14 + ∆23)/ℓ′, β1 = (∆12 − ∆34)/ℓ′, β2 = (−∆13 − ∆24)/ℓ′, and
β3 = (∆14 − ∆23)/ℓ′, with ℓ′ so that gcd(α1, β1, α2, β2, α3, β3) = 1.
It is easy to check that if α3 ̸= β3 then the two vectors w1 and w2 are
linearly independent and so the orthogonal space {w1, w2}⊥ is two-dimensional.
By permuting coordinates and/or changing their signs, we can insure that α3 −
β3 = 2∆23/ℓ′ ̸= 0, since by (6) and the assumption that ℓ > 0, we see that not
all of the ∆ij are equal to zero.
(ii) Let us denote by L the minimal lattice which contains the given square
{u, v} and by V its volume. As we observed in part (i) this lattice is the same
as Z4 ∩ {w1, w2}⊥ if α3 ̸= β3. Let us observe that the two vectors U :=
(0, ∆12, −∆13, ∆14) and V := (∆14, −∆24, ∆34, 0) are in L. This shows that
2U/ℓ′ = (0, α1 + β1, α2 + β2, α3 + β3) and 2V /ℓ′ = (α3 + β3, −α2 + β2, α1 − β1, 0)
are in L also. The area of the parallelogram determined by these two vectors
is given by the square root of the Gramian determinant
∣
∣
∣
∣ (α1 +β1)2 +(α2 +β2)2 +(α3 +β3)2 (α1 +β1)(β2 − α2)+(α2 +β2)(α1 −β1)
(α1 +β1)(β2 − α2)+(α2 +β2)(α1 − β1) (α3 +β3)2 +(α2 − β2)2 +(α1 − β1)2
 ∣
∣
∣
∣=

= ∣
∣
∣
∣2(k2 + α1β1 + α2β2 + α3β3) 2(α1β2 − β1α2)
2(α1β2 − β1α2) 2(k2 + α3β3 − α2β2 − α1β1)
∣
∣
∣
∣ .

This means that the vectors U/ℓ′ and V /ℓ′, still in L, form a parallelogram of
an area, which is the square root of
 (1/4)[(k2 + α3β3)
2 − (α2β2 + α1β1)
2 − (α1β2 − β1α2)
2] =

(1/4)[k4 + 2k2α3β3 + α2
3β2
3 − (k2 − α2
3)(k2 − β2
3)] = k2((α3 + β3)/2)
2.

It follows that V divides k|α3+β3|/2. In a similar way, we can show that V divi-
des k|αi ± βi|/2 for i = 1, 2, 3. Given the assumption that gcd(α1, β1, α2, β2, α3,
β3) = 1, we conclude that V divides k.
In order to conclude that V = k, let us look at the Gram determinant of
the vectors w1/(α3 − β3) and w2/(α3 − β3), which if added to L extends the
lattice and gives a basis for it. Since its volume can be determined by the same
method as above, a similar calculation gives V ′ = k/|α3 − β3|. This implies
that V /V ′ is an integer, or k divides V |α3 − β3|. Since we can obtain similarly
that k divides V |αi ± βi|, we conclude that V = k. □

Example 2 . As in the case of equilateral triangles (see [17]), there is a
converse of Theorem 2.7. Let us take the ˝rst odd ℓ for which we get two
essentially di˙erent representations as in (5):
 11
2 = 9
2 + 62 + 22 = 7
2 + 62 + 62.

11 Ehrhart polynomial for lattice squares, cubes and hypercubes 67

We can then choose α1 = 9, β1 = 7, α2 = 6, β2 = 6, α3 = 2, and
β3 = 6. Then the two vectors, de˝ned in Theorem 2.7, are w1 = (0, 2, 0, −4) and
w2 = (−4, −12, 16, 0). Then the space {w1, w2}⊥ is de˝ned by the equations
y − 2t = 0 and x + 3y − 4z = 0. These can be simpli˝ed to y = 2t and
x = 4z − 6t. Because the generic vector in {w1, w2}⊥ ∩ Z4 is u = (4z −
6t, 2t, z, t) = z(4, 0, 1, 0) + t(−6, 2, 0, 1) we can calculate, as before the volume
of the fundamental domain and obtain indeed 11. Then we get a quadratic
form QF (z, t) = (4z − 6t)2 + (2t)2 + z2 + t2 = 17z2 − 48zt + 41t2 that should
lead to the solutions we need solving the Diophantine equation QF (z, t) = 11k.
It turns out that the smallest multiple for which we have solutions is k = 11
and then two of the vectors which de˝ne the square are u = (−4, 8, 5, 4) and
v = (10, 2, 4, 1). Its Ehrhart polynomial is then E2(t) = 11t2 + 2t + 1. We
observe that we get new terms, such as 10, 94, and 266 for instance, for the
sequence of almost perfect squares in dimension 4, compared to dimension 2.
This is an example when all the ∆ij are divisible by 11.
As we have seen in [17], the following result gives a certain converse to
Theorem 2.7.
 Theorem 2.8 . Given k odd, and two di˙erent representations

k2 = a
2 + b
2 + c
2 = a
′2 + b
′2 + c
′2, with gcd(a, b, c, a
′, b
′, c
′) = 1, c
′ > c,

and a, a′ both odd. Then if we set ∆12 = a′−a
2 , ∆34 = a+a′
2 , ∆13 = − b′−b
2 ,
∆24 = b+b′
2 , ∆14 = c+c′
2 , and ∆23 = c′−c
2 the equations (7) and (8) are satis˝ed.
Moreover, the two dimensional space S of all vectors [u, v, w, t] ∈ Z4, such that

(10)
 {
(0)u + ∆34v + ∆24w + ∆23t = 0
∆23u + ∆13v + ∆12w + (0)t = 0

contains a family of squares.
Proof. By construction we see that (8) is true. Since a, a′ are odd, the
others must be even and so, all numbers de˝ned above are integers. We have
then indeed
∆12∆34 − ∆13∆24 + ∆14∆23 = (1/4)[a′2 − a2 − (b
2 − b
′2) + (c
′2 − c
2)] = 0.

One can also check that k2 = ∑
i<j ∆2
ij. We see that the assumption
∆23 > 0 insures that the equations (10) de˝ne a two dimensional space in R4.
We can solve the equations (10) for t and u:

t = − ∆34v + ∆24w
∆23 , u = − ∆13v + ∆12w
∆23 , with v, w ∈ Z.

If we denote a generic point P ∈ R4 in the plane (10), in terms of v and w, i.e. ,

P (v, w) = [− ∆13v + ∆12w
∆23 , v, w, − ∆34v + ∆24w
∆23 ],

68 Eugen J. Ionascu 12

we observe that for two pairs of the parameters, (v, w) and (v′, w′), we obtain
∆′
23 = wv′ − vw′,

∆′
12 = v(− ∆13v′ + ∆12w′

∆23 ) + ∆13v + ∆12w
∆23 v′ = ∆12∆′
23/∆23,

and similarly ∆′
13 = ∆13∆′
23/∆23, etc.
We want to show that a non-zero square of the form OP (v, w)P (v′, w′)Q
( OQ = OP (v, w) + OP (v′, w′)) exists for some integer values of v, w, v′ and
w′. We need to have OP (v, w)2 = OP (v′, w′)2 = ℓ and P (v, w) · P (v′, w′) = 0.
If such a square exists, by Theorem 2.7, we may want ℓ of the form ℓ = kℓ′

for some ℓ′ ∈ N.
By Lagrange's identity, calculations similar to those in the derivation of
(6), show that if |P (v, w)|2 = |P (v′, w′)|2 = kℓ′ then

(P (v, w) · P (v′, w′))
2 = k2ℓ′2 − (
∑

i,j ∆2
ij) ( ∆′
23
∆23
 )2 = k2ℓ′2 − k2 ( ∆′
23
∆23
 )2 .

Hence, to get P (v, w)·P (v′, w′) = 0, it is enough to have ∆′
23 = ℓ′∆23 (provided
that we have already shown that |P (v, w)|2 = |P (v′, w′)|2 = kℓ′). In other
words, a square exists if there exist integer pairs (v, w) and (v′, w′) such that

(11) |OP (v, w)|
2 = |OP (v′, w′)|
2 = k ∆′
23
∆23 .

The essential object in this analysis is the quadratic form

QF (v, w) := |OP (u, v)|
2 = ( ∆34v + ∆24w
∆23
 )2 + v2 + w2 + ( ∆13v + ∆12w
∆23
 )2 ,

or
 QF (v, w) =

(∆2
34 + ∆2
13 + ∆2
23)v2 + 2(∆34∆24 + ∆13∆12)vw + (∆2
24 + ∆2
12 + ∆2
23)w2

∆2
23 .

We use Lagrange's identity again, which we will write in the form

(α2+β2+γ2)(ζ 2+η2+θ2) = (αζ−βη+γθ)2+(αη+βζ)
2+(αθ−γζ)
2+(βθ+γη)
2.

Then the determinant of the form QF (v, w) (excluding its denominator) is
equal to −∆/4 = (∆2
34 + ∆2
13 + ∆2
23)(∆2
12 + ∆2
24 + ∆2
23) − (∆34∆24 + ∆13∆12)2 =

(∆12∆34 − ∆13∆24 + ∆2
23)2 + (∆12∆23 − ∆34∆23)2 + (∆13∆23 + ∆24∆23)2 ⇒

−∆/4 = ∆2
23 [(∆23 − ∆14)2 + (∆12 − ∆34)2 + (∆13 + ∆24)2] = ∆2
23(k2)

⇒ ∆ = −(2k∆23)2.

13 Ehrhart polynomial for lattice squares, cubes and hypercubes 69

This implies that for v0 = −(∆34∆24 + ∆13∆12) and w0 = ∆2
13 + ∆2
23 + ∆2
34 we
get QF (v0, w0) = k2(∆
2
34 + ∆2
13 + ∆2
23),
and

(12) QF (v, w) = (w0v − v0w)2 + k2w2∆2
23
∆2
23w0 .

So, by (11) and (12) we need to have solutions (v, w) and (v′, w′) of
(13)(w0v − v0w)2 + k2w2∆2
23 = (w0v′ − v0w′)
2 + k2w′2∆2
23 = k∆23w0(wv′ − vw′).

In general, if the Diophantine quadratic equation x2 + y2 = n has a solution
(x, y), then it has other solutions such as (y, −x).
Given (v, w), let us assume that (v′, w′) gives exactly this other solution
( x = w0v − v0w, y = kw∆23) when substituted in (13):





w0v′ − v0w′ = kw∆23

k∆23w′ = −(w0v − v0w).

This allows us to solve for v′ and w′ in order to calculate ∆′
23:

v′ = v2
0w − v0w0v + k2∆2
23w
2k∆23w0 , w′ = v0w − w0v
k∆23 ,

∆′
23 = wv′ − vw′ = (w0v − v0w)2 + k2w2∆2
23
k∆23w0 .

This means that (13) is automatically satis˝ed with this choice of (v′, w′). In
fact, we have shown that, for every integer values of (v, w), such that

(14) (w0v − v0w)2 + k2w2∆2
23 = (kw0ℓ
′)∆
2
23
taking (v′, w′) as above, we automatically get a square determined by vectors
OP (v, w), P (v′, w′) ∈ Q4, which may not have integer coordinates. In order for
(14) to have rational solutions, in v and w, we need to have kw0ℓ′ a positive
integer which is a product of primes of the form 4s+1, and all the other primes,
in its prime factorization, have even exponents. Clearly, there exists a smallest
positive integer ℓ′ with this property. □

As we have seen in Proposition 2.2 [17], we can similarly show the existence
in every plane of equations (10), of a square that is minimal , in the sense that the
side-lengths are the smallest possible. Then, a similar result to Proposition 2.2
[17] takes place: every square in the same plane can be written in terms of a
square that is minimal (same formulae as in 2 dimensions). For a proof, we
just invite the reader to study Figure 3 (a proof without words exercise).

70 Eugen J. Ionascu 14

Fig. 3 Minimal squares.

As in dimension 3, we also have parametric formulae for squares, which
are more general than the ones at the beginning of the subsection. The two
vectors are

(15) u = ±(−ta−zb+yc−xd, −tb+za−yd−xc, −tc−zd−ya+xb, −td+zc+yb+xa)

v = ±(ax − by − cz − dt, ay + bx + ct − dz, az − bt + cx + dy, at + bz − cy + dx)

and one can check that u · v = 0 and |u|2 = |v|2 = (x2 + y2 + z2 + t2)(a2 + b2 +
c2 + d2). The two relations as in (5) can be simpli˝ed by (x2 + y2 + z2 + t2)2

and (a2 + b2 + c2 + d2)2 respectively and reduced to

(16) (x2 + y2 + z2 + t
2)
2 = (x2 + y2 − z2 − t
2)2 + (2xt + 2yz)
2 + (2ty − 2xz)
2,

(a
2 + b
2 + c
2 + d
2)
2 = (a
2 + b
2 − c
2 − d
2)
2 + (2ad − 2bc)
2 + (2ac + 2bd)2.

These relations can be reduced even farther depending upon what q1 and
q2 are. A simple observation here is that the simpli˝ed relations (16) depend
only on the plane containing the square and every other square contained in the
same plane has the same simpli˝ed relations. This implies that the minimal

15 Ehrhart polynomial for lattice squares, cubes and hypercubes 71

square contained in the plane has the sides at most √
k1k2, where the k2
i =
A2
i + B2
i + C2
i are the primitive versions of (16).

Example 3 . We start with two equalities as in (16): 92 = 72 + 42 + 42 and
152 = 112 + 102 + 22. This implies that 452 = 332 + 302 + 62 = 352 + 202 + 202.
As in Theorem 2.8, we can take a = 33, a′ = 35, b = 30, b′ = 20, c = 6
and c′ = 20. Then ∆12 = 1, ∆34 = 34, ∆13 = 5, ∆24 = 25, ∆14 = 13,
and ∆23 = 7, and the equations of the plane are 34v + 25w + 7t = 0 and
7u + 5v + w = 0. The system can be solved easily in terms of u and v:
w = −7u − 5v and t = 25u + 13v. Then two vectors that generate the lattice
in this plane are (1, 0, −7, 25) and (0, 1, −5, 13). Then the volume of the
fundamental domain is 45. The quadratic form is Q(u, v) = 675u2 + 720uv +
195v2 or Q(u, v) = 15(45u2 + 48uv + 13v2). So, the equation Q(u, v) = 45ℓ
is equivalent to (13v + 24u)2 + 9u2 = 3(13)ℓ. Then it is clear that v has
to be a multiple of 3 and if we take ℓ = 3, v = 3 and u = −2 we obtain
a solution. This gives u = (−2, 3, −1, −11), and v = 6 and u = −3 gives
v = (−3, 6, −9, 3) = 3(−1, 2, −3, 1) (which is indeed a square). This means that
the Ehrhart polynomial of this square is E2(t) = 3t2 + 4t + 1 = (t + 1)(3t + 1),
t ∈ N. Taking the parameterizations as in Theorem 2.4 for the two equalities,
92 = 72 + 42 + 42 and 152 = 112 + 102 + 22, we observe that this square is
covered by the parametrization (15) by taking a = x = z = 1, b = d = t = 2,
c = 0, and y = 3. It is surprising that such a square with a big size for its side
lengths has no lattice points in the interior.

In order to understand better what is happening we will reformulate ever-
ything in terms of quaternions.
We remind the reader that the Hamilton quaternion algebra over the real
numbers, denoted by H(R), is the associative unitary algebra given by the
requirements: (I) H(R) is the free R-module over the symbols i, j, and k, with 1 the
multiplicative unit; (II) i2 = j2 = k2 = −1, ij = −ji = k, jk = −kj = i and ki = −ik = j.
If q = x + yi + zj + tk ∈ H(R) the conjugate of q is q = x − yi − zj − tk
and the norm of q is N (q) = x2 + y2 + z2 + t2. Some standard notation is then
naturally appearing: Re(q) = x and Im(q) = yi + zj + tk.
By H(Z) we denote the subset of quaternions whose components are all
integers. We imbed Z4 into H(Z) in the natural way: (x, y, z, t) ↪→ x + yi +
zj + tk. Also, we will think of R3 imbedded in H(R) in a, more or less, natural
way (y, z, t) ↪→ yi + zj + tk; in other words, R3 is the hyperplane Re(q) = 0.
It is known that this norm is multiplicative, i.e. N (q1q2) = N (q1)N (q2),
and q1q2 = q2 q1.

72 Eugen J. Ionascu 16

For the important results about the arithmetic of H(Z), we recommend
the reader the recent treatment in [5]. Using the same terminology as in [5], a
quaternion q is called odd , if N (q) is an odd number.
The parametrization in Theorem 2.4 is basically equivalent to

(17) n1i + n2j + n3k = q(ϵ)q, where q = x + yi + zj + tk, and ϵ ∈ {i, j, k}.

In case ϵ = k, n1 = 2(xz + yt), n2 = 2(zt − xy), and n3 = x2 − y2 − z2 + t2.
The parametrization (15) is equivalent to
(18)
u = q1ϵ2q2 and v = q1ϵ3q2, where q1 = x + yi + zj + tk, q2 = a + bi + cj + dk,

with ϵ2 and ϵ3 ˝xed in {i, j, k}. In what follows we are going to take ϵ2 = j and
ϵ3 = k. This square is in a plane de˝ned by equations similar to (10) obtained
from the two Pythagorean quadruples de˝ned by q1 and q2 as in (17) using
ϵ = ϵ1 such that {ϵ1, ϵ2, ϵ3} = {i, j, k}.

Observation 1 . If we substitute q = ̃q(α + βk) into (17) for ϵ = k, we see
that because (α + βk)k = k(α + βk), we have

n1i + n2j + n3k = ̃q(k)(α + βk)(α − βk)̃q = (α2 + β2)̃q(k)̃q

= (α2 + β2)(̃n1i + ̃n2j + ̃n3k).

This implies that ni = ̃ni(α2 + β2), i = 1, 2, 3, which means that the primitive
solutions of the equation (3) have to arise from quaternions q which have no
right factors of the form α + βk. We obtain the same conclusion if q = ̃q(1 + i)
or q = ̃q(1 + j), because (1 + i)k = −j(1 + i) and (1 + j)k = i(1 + j). We have
the following converse of this observation.

Proposition 2.9 . If in (17), we have gcd(n1, n2, n3) = n > 1, i.e. if
n1 = 2(xz + yt), n2 = 2(zt − xy) and n3 = x2 − y2 − z2 + t2, are divisible by n,
then q = x + yi + zj + tk = (x′ + y′i + z′j + t′k)η where η ∈ {1 + i, 1 + j, α + kβ}
for some integers α and β.

Proof. Let us pick a prime p which divides n. Since

n2
1 + n2
2 = 4[(xz + yt)
2 + (zt − xy)
2] = 4(x2 + t
2)(y2 + z2)

is divisible by n2 it is divisible by p. First, we assume that p > 2. Then p
divides either A := x2 + t2 or B := y2 + z2. Since n3 = A − B and p divides
n3, we must have, in fact, A and B both divisible by p. If p = 2, then A and
B are either both even or both odd. If A and B are both even, then we have
the same conclusion as in the case p > 2. In the case A and B are both odd,
we have, lets say x = 2x′, y = 2y′, z = 2z′ + 1, t = 2t′ + 1. This implies that

q = x + yi + zj + tk = 2x′ + 2y′i + 2z′j + 2t
′k + j + k

17 Ehrhart polynomial for lattice squares, cubes and hypercubes 73

= (x′ + y′i + z′j + t
′k)(1 − i)(1 + i) + k(1 + i) = ̃q(1 + i)

which proves our claim. Similar conclusion can be drawn if x and z, t and y,
or t and z are even.
If p is a prime of the form 4k + 3, then automatically x = px′, z = pz′,
t = pt′, and y = py′, which shows that q = x+yi+zj +tk = (x′ +y′i+z′j +t′k)p
and the conclusion of our proposition follows, with α = p and β = 0.
Finally, if p is a prime of the form 4k + 1, then p = α2 + β2. Because
A = (x + tk)(x − tk) and η = α + βk is a Gaussian prime integer, it divides
x+tk or x−tk. Without loss of generality we may assume that η divides x+tk.
If this is not the case we continue with η. Next we observe that since p divides
xz + yt and zt − xy, then p divides (x + tk)(y + zk) = (xy − tz) + (ty + xz)k.
This implies that if η does not divides x + tz, then η must divide y + zk. Since
η divides B = (y + zk)(y − zk), then η divides either y + zk or y − zk. Let us
assume ˝rst that η divides y − zk. Then we can write

q = x + yi + zj + tk = x + tk + i(y − zk) = (x′ + t′k)η + i(y′ + z′k)η = ̃qη.

If η divides y + zk, then η divides y − zk. If η divides z + tz then we
proceed as above, with a small change:

q = x + yi + zj + tk = x + tk + i(y − zk) = (x′ + t′k)η + i(y′ + z′k)η = ̃qη.

If η does not divides x + tz, then we have shown above that in this case,
η must divide y + zk, which is the same thing as η dividing y − zk. This puts
us in the same position as above. □

Observation 2 . If we substitute q1 = ̃q1(α + βi) into (18), we see that
because (α + βi)k = αk − βj and (α + βi)j = αj + βk, we have ̃u = αu − βv
and ̃v = βu + αv. This is saying that the twin pair ̃u and ̃v is in the same plane
as u and v. A similar statement can be obtained if we substitute q2 = ̃q2(α+βi)
into (18).
 Let us recall, for the convenience of the reader, the statement of Lemma
2.6.5 in [5], with the only di˙erence that the important factors appear on the
right (so, this new statement follows by conjugation and a symmetry type
transformation i → −i, j → −j, and k → −k).

Lemma 2.10 ([5]) . Every integer quaternion q ∈ H(Z) has unique factori-
zation

(19) q = 2
ℓq ̃qη,

where ̃q ∈ H(Z) is odd, ηq ∈ {1, 1 + i, 1 + j, 1 + k, (1 + j)(1 + i), (1 − k)(1 + i)}
and for some non-negative ℓq ∈ Z.

74 Eugen J. Ionascu 18

This new statement follows by conjugation and a symmetry type trans-
formation i → −i, j → −j, and k → −k from the original statement in [5].

Theorem 2.11 . (i) We assume that q1 and q2 in the parametrization (18)
represented as in (19), are not right-divisible by quaternions of the form π =
α + βi, |π| > 1, then the square in the parametrization (18) is minimal.
(ii) The parametrization (18) represents all the integer squares.

Proof. (i) We observe ˝rst that under our hypothesis, ℓq1 = ℓq2 = 0 and
ηq1, ηq2 ∈ {1 + j, 1 + k} in (19). By way of contradiction, if the construction
of the square S = {u, v} in (18) is not minimal, there exists an integer square
S0 = {u0, v0} in the same plane in such a way S can be obtain from S0 by
a simple transformation which involves two integer parameters α and β: u =
αu0 + βv0 and v = −βu0 + αv0. We may assume that p = α2 + β2 is a prime,
otherwise we rede˝ne the twin pair S0 in such a way this condition is satis˝ed.
Let us ˝rst assume that p > 2. Since q1 is not right-divisible by η = α + βi
(which is a prime in H(Z), η odd quaternion), we conclude that gcd(q1, η)r = 1
(the right greatest-common divisor as de˝ned in [5]). By Theorem 2.6.6 in [5],
which is the equivalent of B´ezout's relation in H(Z), we can ˝nd γ and δ in
H(Z[ 1
2 ]) such that γq1 + δη = 1.

If p = 2, then |u|2 = |v|2 = N (q1)N (q2) = 2|u0|2 and so 2 divides N (q1)
or N (q2). Using Lemma 2.10 we conclude that q1 is of the form q′
1(1 + k) or
q′
1(1 + j) with q′
1 odd. So we can still obtain a B´ezout's relation as above, with
q′
1 and η, which can be easily transformed into one for q1 and η.
Solving for u0, the above system, in terms of u and v, we have

u0 = (1/p)(αu − βv) = (1/p)q1(α + iβ)kq2.

Multiplying on the right with (1/p)(α + iβ)kq2 the above B´ezout's relation, we
obtain γu0 + δkq2 = (1/p)(α + iβ)kq2.
From this relation we see that q2 = ̃q2(α − iβ) for some ̃q2 ∈ H(Z[ 1
2 ]).
Hence 2kq2 = q′
2(α − iβ) for some q′
2 ∈ H(Z). Using Lemma 2.10 again, we
conclude that q2 is right divisible by α − iβ which is in contradiction with our
hypothesis. Therefore, it must be true that the S = {u, v} in (18) is minimal.
(ii) Let us start with an arbitrary square, S0. We then use Theorem 2.7
to ˝nd the reduced equations of the plane that it is contained in, as those
given by (10). Then we can apply the Theorem 2.4 twice, and ˝nally use the
two sets of parameters (8 in total) to construct a square S1, with formulae
(15). The quaternions involved have the property in part (i) (both odd), and
so the square S1 is minimal. Then S0 can be written in terms of S1 using two

19 Ehrhart polynomial for lattice squares, cubes and hypercubes 75

numbers α and β. Using the substitutions described before the statement of the
theorem, we can write S0 as in (18) by multiplying either of the quaternions by
α + βi. □

Theorem 2.12 . Assuming we have two odd integer quaternions q1 and q2
as in (ii) in Theorem 2.11, then the fundamental domain of the integer lattice
containing the square {u, v} in (18), has volume equal to V = lcm(N (q1)),
N (q2)). The Ehrhart polynomial of the square (18) is

E2(t) = gcd(N (q1), N (q2))t
2 + (D1 + D2)t + 1,

where D1 = gcd(u1, u2, u3, u4) and D2 = gcd(v1, v2, v3, v4).

Proof. This follows from Theorem 2.7 (part (ii)), Proposition 2.9 and the
observation that lcm(N (q1), N (q2))2 = a2 + b2 + c2 = a′2 + b′2 + c′2 for some
integers a, b, c, a′, b′, and c′ with gcd(a, b, c, a′, b′, c′) = 1. □

Observation 3 . To get back in dimension 3, we identi˝ed R3 with the
subspace of quaternions q for which Re(q) = 0. We have seen that only one
Pythagorean quadruple equation is necessary: ∆13 = ∆12 = 0 which implies
∆14 = 0. To accomplish this, we can take q1 = q2 = q where q is odd. This
implies that the most general square in dimension 3 is of the form (4) combined
with the usual variations from dimension 2 in the respective plane: ̃u = αu−βv
and ̃v = βu + αv with {u, v} as in (4).

There seems to be plenty of numerical evidence that the sequence of almost
perfect squares in dimension four is the set of all non-negative integers. Let us
denote the set of all such numbers by AP S4. We include some partial result in
this direction.
 Theorem 2.13 . (i) The set AP S4 contains all odd numbers.
(ii) The set AP S4 contains all even numbers of the form p − 1 with p a
prime p ≥ 11.

Proof. (i) Let us take an odd k, k ≥ 1, and a primitive Pythagorean
quadruple representation k2 = a2 + b2 + c2. Without loss of generality we may
assume that a is odd and both b and c are even. If we multiply this equality by
2, we obtain 2k2 = 2a2 +2b2 +2c2 = 2c2 +(a+b)2 +(a−b)2. Hence we can build
the square u = (k, k, 0, 0) and v = (c, −c, a + b, a − b). It is clear that D1 = k
and D2 = 1 ( a−b and a+b are odd) as de˝ned in Theorem 2.12. Since the sides
have length k√2 and the two equations de˝ning the plane containing {u, v} are
k2 = (−c)2 + b2 + a2 = (−c)2 + a2 + b2, we conclude by Theorem 2.12 that the
Ehrhart polynomial is Eu,v(t) = 2kt2 + (k + 1)t + 1. Hence Eu,v(−1) = k. This
proves the ˝rst statement.

76 Eugen J. Ionascu 20

(ii) If p is a prime p ≥ 11, then we can ˝nd two distinct primitive Pytha-
gorean quadruple representations p2 = a2 +b2 +c2 = a′2 +b′2 +c′2 and construct
a square as in (18), whose Ehrhart polynomial is E(t) = pt2 + (D1 + D2)t + 1,
where Di divide p. It is not possible to have Di = p since this puts us in the
position where one of the vectors de˝ning the square, say u, is of the form
u = (p, 0, 0, 0). This leads essentially to only one equation which de˝nes the
plane containing {u, v}, but we have two di˙erent equations that de˝ne the
plane. Hence, since E(−1) = p − 1 the claim in (ii) follows. □

Numerical evidence shows that given an odd k ≥ 9, one can ˝nd a square
whose Ehrhart polynomial is E(t) = kt2 + 2t + 1. For instance, for k = 2015
we found u = (−836, 584, −1592, −697) and v = (−506, 1414, 203, 1328) that
does the job.
 3. CUBES

If a general lattice cube in R3 is given by the orthogonal matrix

(20) Cℓ = 1
ℓ
 

a1 b1 c1
a2 b2 c2
a3 b3 c3


 ,

with ai, bi and ci integers satisfying aiaj + bibj + cicj = δi,jℓ2 for all i, j in
{1, 2, 3}), we de˝ne di := gcd(ai, bi, ci). It is clear that the di are divisors of
ℓ. Assuming that the matrix in (20) is irreducible (no smaller ℓ can be used,
which implies ℓ odd), then we have shown in [19] the following.

Theorem 3.1 . Given a cube Cℓ constructed from a matrix as in (20), its
Ehrhart polynomial is given by

(21) L(Cℓ, t) = ℓ3t3 + ℓ(d1 + d2 + d3)t2 + (d1 + d2 + d3)t + 1 or

(ℓt + 1)[ℓ2t2 + (d1 + d2 + d3 − ℓ)t + 1] , t ∈ N.

Similar formula takes place for the cubes in dimension four. In general, a
square can be completed in various ways to a cube and even to a hypercube.
Let us assume that the cube is given by the ˝rst three vectors in the rows of
the following matrix

(22)
 




a1 b1 c1 d1
a2 b2 c2 d2
a3 b3 c3 d3
a4 b4 c4 d4




 ,

21 Ehrhart polynomial for lattice squares, cubes and hypercubes 77

with ai, bi, ci and di integers aiaj + bibj + cicj + didj = δi,jℓ for all i, j
in {1, 2, 3, 4}). In this case, we de˝ne Di := gcd(ai, bi, ci, di) and ζij be the
greatest common divisor of all the 2-by-2 determinants of the matrix [ ai bi ci di
aj bj cj dj
 ] ,

for every i and j with 1 ≤ i < j ≤ 3.

Theorem 3.2 . Given a cube Cℓ constructed from a matrix as in (22), its
Ehrhart polynomial is given by

(23) L(Cℓ, t) = ℓD4t3 + ∆t2 + ∆′t + 1, t ∈ N,

where ∆ := ζ12 + ζ13 + ζ23 and ∆′ := D1 + D2 + D3.

Proof. For the ˝rst coe˚cient the volume of the cube is ℓ√ℓ and the
volume of the fundamental domain of the lattice containing it is equal to√a2
4 + b2
4 + c2
4 + d2
4/D4 = √ℓ
D4 . For the second coe˚cient, the area of each
of the six faces is ℓ. Using the Theorem 2.11 to ˝nd the volume of the fun-
damental domain of the lattice containing the faces determined by rows i and
j, we obtain ℓ/δij, which implies the stated value of ∆. Finally, for the coef-
˝cient ∆′, we proceed like in the proof of Theorem 3.1 [19]. The main idea
is essentially based on the fact that the topological equivalent in our cube to
[0, 1)3 (containing κ lattice points) has the fundamental domain property: the
dilation with a factor t contains exactly t3κ lattice points. This implies that
κ = ℓD4 and so

ℓD4 = 1 + (ℓD4 − ∆ + ∆′ − 1) + ∑

ij (ζij − (Di + Dj) + 1) + ∑

i (Di − 1).

Solving for ∆′ we obtain the stated value in the theorem. □

3.1. Hypercubes

Hypercubes in dimension four can be constructed using quaternion techni-
ques described earlier. A few orthogonal matrices in dimension 4, together with
the Ehrhart polynomial associated to the corresponding hypercube, are inclu-
ded next:
 1
√2
 




1 1 0 0
1−10 0
0 0 1 1
0 0 0−1






4t4 + 8t3 + 8t2 + 4t + 1
= (2t2 + 2t + 1)2
 , 1
√3
 




 1 1 1 0
−1 1 0 1
0 −11 1
−1 0 1−1






9t4 + 12t3 + 6t2 + 4t + 1
= (t + 1)(3t + 1)(3t2 + 1)
, 1
2
 




 1 1 1 −1
−1 1 1 1
1 −1 1 1
1 1 −1 1
 





16t4 + 16t3 + 12t2 + 4t + 1
= (1 + 2t + 4t2)2
 ,

78 Eugen J. Ionascu 22

1
√5
 




2 1 0 0
1−20 0
0 0 2 1
0 0 1−2






25t4 + 20t3 + 14t2 + 4t + 1
= (1 + 2t + 5t2)2
 , 1
√6
 




2 1 1 0
1−2 0 1
1 0 −2−1
0 1 −1 2
 





36t4+24t3+8t2+4t+1
 , 1
√7
 




2 1 1 1
1−2−1 1
1 1 −2−1
1−1 1 −2






49t4+28t3+6t2+4t+1
 ,

1
3
 




30 0 0
02 2 1
02−1−2
01−2 2
 





81t4 + 54t3 + 18t2 + 6t + 1
= (3t + 1)2(9t2 + 1)
 , 1
3
 




2 2 1 0
2−2 0 1
1 0 −2−2
0 1 −2 2
 





81t4+36t3+6t2+4t+1

, 1
√10
 




2 2 1 1
2−2−1 1
1 1 −2−2
1−1 2 −2






100t4+40t3+16t2+4t+1
,

1
√10
 




3−10 0
1 3 0 0
0 0 3 1
0 0 1−3






100t4 + 40t3 + 24t2 + 6t + 1
= (10t2 + 2t + 1)2
 , 1
√11
 




3 1 1 0
1−3 0 1
1 0 −3−1
0 1 −1 3
 





121t4+44t3+6t2+4t+1
 , and 1
√13
 




2 2 2 1
2−2 1 −2
2−1−2 2
1 2 −2−2






169t4+53t3+6t2+4t+1
 .

We see that several of these examples are cross polytopes (squares in two
dimensions) and indeed the resulting polynomial is the product of the smaller
degree polynomials involved. Let us assume that in general we have

(24) Hℓ = 1
√ℓ
 




a1 b1 c1 d1
a2 b2 c2 d2
a3 b3 c3 d3
a4 b4 c4 d4




 ,

where aiaj + bibj + cicj + didj = δijℓ for i, j ∈ {1, 2, 3, 4}. We de˝ne Di =
gcd(ai, bi, ci, di) for i ∈ {1, 2, 3, 4} and assume that Hℓ is irreducible, i.e. ,
gcd(D1, D2, D3, D4) = 1. The Ehrhart polynomial associated to the hyper-
cube constructed in a natural way using the orthogonal matrix Hℓ is then

(25) EH(ℓ)(t) = ℓ
2t
4 + α1t
3 + α2t2 + α3t + 1.

Proposition 3.3 . With the notation introduced earlier α1 = ℓ(D1 + D2 +
D3 + D4).

Proof. Let us look at a 3-dimensional face, say generated by ˝rst three
rows of (22). Its volume is ℓ√ℓ and the volume of the lattice containing it
is equal to √
a2
4 + b2
4 + c2
4 + d2
4/D4 = √ℓ
D4 . Since there are eight such faces the
general theory gives the value claimed. □

23 Ehrhart polynomial for lattice squares, cubes and hypercubes 79

Theorem 3.4 . We have

(26) α2 = α3 + δ − ∆,

where δ = ∑
1≤i<j≤4 ζij and ∆ = D1 + D2 + D3 + D4.

Proof. We are going to use the same property of the part of hypercube
that is topologically equivalent to [0, 1)4, as in the proof of Theorem 3.2. The
balancing of points in each of the corresponding sets of the partition

[0, 1)
4

= (0, 0, 0, 0)∪(0, 1)
4 ⋃

all f our 3D cubes
(0, 1)
3 ⋃

all six 2D f aces
(0, 1)
2 ⋃

all f our 1D sides
(0, 1)

gives (using Theorem 3.2 )

ℓ
2 = 1+(ℓ2−α1+α2−α3+1)+(ℓ∆−2δ+4∆−4)+ ∑

1≤i<j≤4
(ζij−(Di+Dj)+1)+∆−4.

From this, one can easily derive (26). □

Looking at the examples we have so far, we notice that α3 = ∆, and so
the Ehrhart polynomial of an hypercube would result into the following simple
form

(27) EH(ℓ)(t) = ℓ
2t
4 + ℓ∆t
3 + δt
2 + ∆t + 1.

This is indeed the case since it follows from Theorem 9.9 in [2]. Of course,
one may want to look into all these concepts for dimensions bigger than four,
although it seems that very little is known about the essentially new related
objects in dimensions ˝ve or beyond. For other further developments, it may
be useful to analyze the roots or calculate better bounds for them, such as those
in [3], for the type of polytopes studied here.
 REFERENCES

[1] A. Barvinok, Integer Points in Polyhedra . Zur. Lect. Adv. Math., European Mathema-
tical Society, Zurich, 2008.
[2] M. Beck and S. Robins, Computing the Continuous Discretely: Integer-Point Enumera-
tion in Polyhedra . Undergrad. Texts Math., Springer-Verlag, New York, 2015.
[3] M. Beck, J.A. Deloera, M. Develin, J. Pfei˛e and R. Stanley, Coe˚cients and roots of
Ehrhart polynomials . Contemp. Math. 374 (2005), 1536.
[4] S. Cooper and M. Hirschhorn, On the number of primitive representations of integers as
a sum of squares . Ramanujan J. 13 (2007), 725.
[5] G. Davido˙, P. Sarnak and A. Valente, Elementary Number Theory, Group Theory and
Ramanujan Graphs . London Math. Soc. Stud. Texts 55 , Cambridge, 2003.
[6] M. Beck, R. Diaz and S. Robins, The Frobenius problem, rational polytopes, and Fourier-
Dedekind sums . J. Number Theory 96 (2002), 121.

80 Eugen J. Ionascu 24

[7] R. Diaz and S. Robins, The Ehrhart polynomial of a lattice polytope . Ann. of Math.
145 (1997), 503518.
[8] E. Ehrhart, Sur les polygones et les poly`edres r´eguliers entiers. Enseign. Math. (2) 5
(1959), 8185.
[9] E. Ehrhart, Sur les poly`edres rationnels homoth´etiques `a n dimensions . C.R. Acad.
Sci. Paris 154 (1962), 616618.
[10] E. Ehrhart, Sur un probl`eme de g´eom´etrie diophantienne lin´eaire. I. P oly`edres et
r´eseaux. J. Reine Angew. Math. 226 (1967), 129.
[11] E. Ehrhart, Solution to problem 6179 [1977, 744] . Amer. Math. Monthly (1980), 826
827.
[12] S. Frischa and L. Vasersteinba, Parametrization of Pythagorean triples by a single triple
of polynomials . J. Pure Appl. Algebra 212 (2008), 271274.
[13] L.M. Goswick, E.W. Kiss, G. Moussong and N. Sim´anyi, Sums of squares and orthogonal
integeral vectors . J. Number Theory 132 (2012), 3753.
[14] R.L. Graham, J.C. Lagarias, C.L. Mallows, A.R. Wilks and C.H. Yan, Apollonian circle
packings: number theory . J. Number Theory 100 (2003), 145.
[15] W. H¨urlimann, Exact and asymptotic evaluation of the number of distinct primitive
cuboids . J. Integer Seq. 18 (2015), 2 , Article 15.2.5
[16] W. H¨urlimann, On the number of primitive of Pythagorean quintuples . Journal of Alge-
bra, Number Theory: Advances and Applications 13 (2015), 1 , 1328.
[17] E.J. Ionascu, Equilateral triangles in Z4. Vietnam J. Math. 43 (2015), 3 , 525539.
[18] E.J. Ionascu, New parametrization of A
2 + B2 + C 2 = 3D2 and Lagrange's four-square
theorem. An. Stiint. Univ. Al. I. Cuza Iasi. Mat. (N.S.) 62 (2016), 3 , 823833.
[19] E.J. Ionascu, Lattice platonic solids and their Ehrhart polynomial . Acta Math. Univ.
Comenian. 82 (2013), 1 , 147158.
[20] E.W. Kiss and P. Kutas, Cubes of integral vectors in dimension four. (English summary) .
Studia Sci. Math. Hungar. 49 (2012), 4 , 525537.
[21] A. Osborne and H. Liebeck, Orthogonal bases of R3 with integer coordinates and integer
lengths . Amer. Math. Monthly 96 (1989), 4953.
[22] A. Osborne and H. Liebeck, The generation of all rational orthogonal matrices . Amer.
Math. Monthly 98 (1991), 131133.
[23] S. Sam, A bijective proof for a theorem of Ehrhart . Amer. Math. Monthly 116 (2009),
8 , 688701.
[24] I.J. Schoenberg, Regular simplices and quadratic forms . J. Lond. Math. Soc. 12 (1937),
4855.
[25] R. Spira, The Diophantine equation x
2 + y2 + z2 = m
2. Amer. Math. Monthly 69
(1962), 36065.

Received 1 December 2017 Columbus State University
Department of Mathematics
4225 University Avenue
Columbus, GA 31907
Honori˝c Member
of the Romanian Institute
of Mathematics Simion Stoilow
ionascu@columbusstate.edu math@ejionascu.ro
