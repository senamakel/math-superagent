<!-- source: https://arxiv.org/pdf/math/0208001 | converted from PDF -->

arXiv:math/0208001v1  [math.CO]  1 Aug 2002
Self-Dual Codes

E. M. Rains and N. J. A. Sloane

Information Sciences Research, AT&T Labs-Research
180 Park Avenue, Florham Park, NJ 07932-0971

May 19 1998

ABSTRACT

A survey of self-dual codes, written for the Handbook of Coding Theory.

Self-dual codes are important because many of the best codes known are of this type and
they have a rich mathematical theory. Topics covered in this chapter include codes over F2, F3,
F4, Fq, Z4, Zm, shadow codes, weight enumerators, Gleason-Pierce theorem, invariant theory,
Gleason theorems, bounds, mass formulae, enumeration, extremal codes, open problems. There
is a comprehensive bibliography.

1. Self-dual codes over rings and ﬁelds

1.1. Inner products

There are several diﬀerent kinds of self-dual codes. Let F be a ﬁnite set called the alphabet

(e.g. F = {0, 1} for binary codes). A code C over F of length n is any subset of F n. If F has the

structure of an additive group then C is additive if it is an additive subgroup of F n. If F has a

ring structure then C is linear over F if it is additive and also closed under multiplication by

elements of F. (We will always assume that multiplication in F is commutative.)

In order to deﬁne dual codes we must equip F with an inner product (cf. [178], [201]). We

denote this by ( , ) and require that it satisfy the following conditions:

(x + y, z) = (x, z) + (y, z) ,
(x, y + z) = (x, y) + (x, z) ,
if (x, y) = 0 for all x then y = 0 ,
if (x, y) = 0 for all y then x = 0 .

To deﬁne the dual of a linear code we impose the further condition that F has a conjugacy

operation, or “involutory anti-automorphism” (which may be the identity), denoted by a bar,

which satisﬁes
 x = x, x + y = x + y, xy = x y .

The inner product must then satisfy

(x, y) = (y, x), (ax, y) = (x, ay) .

The inner product of vectors x = (x1, . . . , xn), y = (y1, . . . , yn) in F n is deﬁned by

(x, y) =
 n∑

i=1(xi, yi) .

1.2. Families of self-dual codes

Families (2) through (mZ) include the most important families of codes we will consider in

this chapter.

(2) Binary linear codes: F = F2 = {0, 1}, with inner product (x, y) = xy, C = subspace of F n
2 .

(3) Ternary linear codes: F = F3 = {0, 1, 2}, (x, y) = xy, C = subspace of F n
3 .

(4H) Quaternary linear codes: F = F4 = {0, 1, ω, ω2}, where ω2 + ω + 1 = 0, ω3 = 1, x = x2

for x ∈ F4, with the Hermitian inner product (x, y) = xy, C = subspace of F n
4 . Note that for

x, y ∈ F4, (x + y)2 = x2 + y2, x4 = x.

(4E) Quaternary linear codes: F = F4, but with the Euclidean inner product (x, y) = xy.

(4H+) Quaternary additive codes: F = F4, with (x, y) = xy2 + x2y = trace(xy) (the trace from

F4 to F2); C = additive subgroup of F n
4 .

For completeness we should also mention family 4E+, quaternary additive codes with the

Euclidean trace inner product: F = F4, with (x, y) = xy + (xy)2 = trace(xy) (the trace from

F4 to F2); C = additive subgroup of F n
4 . However, the map

x = ωx1 + ωx2 ∈ F n
4 ↔ x1x2 ∈ F 2n
2

shows that these codes are equivalent to binary codes from family 2 with a particular pairing

of the coordinates. Since we don’t know any interesting examples of this family other than

linear codes, we shall say no more about them.

(qH) Linear codes over Fq (or q-ary linear codes), where q is an even power of an arbitrary

prime p, with x = x
√q for x ∈ Fq, (x, y) = xy, C = subspace of F n
q . Note that for x, y ∈ Fq,

(x + y)
√q = x
√
q + y√
q, xq = x.

(qE) Linear codes over Fq, but with (x, y) = xy. If q is a square, family qH is generally preferred

to qE.

(4
Z) Z4-linear codes: F = Z4 = {0, 1, 2, 3}, with (x, y) = xy (mod 4), C = linear subspace1 of

Zn
4 .

(mZ) F = Zm = Z/mZ, where m is an integer ≥ 2, with (x, y) = xy (mod m), C = linear

subspace2 of Zn
m.

Note that for the families 2, 3, 4
Z, mZ, an additive code is automatically linear.

The following families are less important for our present purposes:

(F1) Linear codes over Fq[u]/(u2), where u is an indeterminate, with u = −u, (x, y) = xy.

(References [8] and [101] consider such codes, as well as a noncommutative variant.)

(F2) Additive codes over F4, with (x, y) = xy.

If we relax the requirement that F be commutative and ﬁnite, we can add:

(F3) Linear codes over the p-adic integers.

(F4) Codes over Frobenius rings.

1Strictly speaking, a Z4-submodule.
2Strictly speaking, a Zm-submodule.
 3

(F5) Lattices in Rn (see Section 14).

1.3. The dual code

Once we have speciﬁed a family of codes by giving F and an inner product we can deﬁne

the dual of a code C to be

C ⊥ = {u ∈ F n : (u, v) = 0 for all v ∈ C} .

The dual of a binary linear code (family 2) is again a binary linear code. Similarly, the dual of

a code in any of families 3 through mZ is again a code of the same family. For family 4H+, the

dual of an additive code is additive; if C is also linear so is C ⊥, and then C ⊥ coincides with

the dual in family 4H. The dual in family 4E is the conjugate of the dual in family 4H.

For families 2 through mZ it is easily checked that we have

|C| |C ⊥| = |F|
n , (1)

which implies
 (C ⊥)
⊥ = C . (2)

In general, however, we can say only that

C ⊆ (C ⊥)
⊥ .

In particular, (2) does not necessarily hold for family F2 (consider, for example, the code

{00, 11} which has dual {00, 11, ωω, ωω}, containing only 4 words).

1.4. Self-dual codes

If C = C ⊥ then C is said to be self-dual. If C ⊆ C ⊥, C is self-orthogonal. (In the past, some

authors have used “self-orthogonal” and “weakly self-orthogonal” for these two concepts.)

In families 2 through mZ, if C is self-dual then

|C| = |F|
n/2 , (3)

and if |F| is not a square then n must be even. In particular, if C is linear over a ﬁeld, then

n is even and C is a subspace of dimension n/2. The only families from 2 through mZ that

contain self-dual codes of odd length are 4H+, 4
Z and mZ with m a square.

4

Remarks about the ﬁnal three families. (F3): Let C be a code of length n over the

p-adic integers Zp∞ (such codes have been studied in [46], [50]). In general it is not clear how

one should deﬁne C ⊥. However, if when we reduce C mod p it has the same dimension over

Fp as C had over Fp∞, then there is a natural way to deﬁne the dual so that it satisﬁes

(C ⊥)
⊥ = C, dim C + dim C ⊥ = n .

Namely, let D = Qp∞ ⊗ C be the code over the p-adic rationals Qp∞ generated by C. Since D

is a linear code over a ﬁeld, D⊥ exists and satisﬁes (D⊥)⊥ = D, dim D + dim D⊥ = n. Now

set C ⊥ = D⊥ ∩ Zn
p∞ .

(F4): J. A. Wood ([331], see also [323]) has investigated codes over noncommutative ﬁnite

rings F, and has shown that the two fundamental MacWilliams theorems (Theorem 4 below

and Theorems 10.4 and 10.6 of Chapter 1) hold precisely when F is a Frobenius ring. At present

however no interesting examples of self-dual codes over noncommutative rings are known.

(F5): Unimodular lattices are analogues of self-dual codes in Rn — see Section 14.

2. Equivalence of codes

2.1. Equivalent codes

Codes that diﬀer only in minor ways, such as in the order in which the coordinates are

arranged, are said to be equivalent. The transformations that we allow in deﬁning equivalence

for the above families of codes are as follows (these are precisely the transformations that

commute with the process of forming the dual).

(2) Permutations of the coordinates.

(3) Monomial transformations of the coordinates (that is, a permutation of the coordinates

followed by multiplication of the coordinates by nonzero ﬁeld elements).

(4H) Monomials; global conjugation.

(4E) Permutations; global conjugation.

(4H+) Monomials; conjugation of individual coordinates.

(qH) Monomials over the subgroup

{x ∈ Fq : xx = 1} ∼= F∗
q/F∗√q ,

5

where the star denotes the set of nonzero ﬁeld elements; global multiplication by elements of

F∗
q; global action of Galois group Gal(Fq/Fp)

(qE) Monomials over {±1}; global multiplication by units; global action of Galois group.

(4
Z) Monomials over {±1}.

(mZ) Monomials over square roots of unity; global multiplication by units of Zm.

2.2. Automorphism groups

In each case, the subset of such transformations that preserves the code forms the auto-

morphism group Aut(C) of the code.

Let G denote the full group of all transformations listed. The order of G in the above cases

is:

(2) n!

(3) 2nn!

(4H) 2.3nn!

(4E) 2.n!

(4H+) 6nn!

(qH) logp(q)(
√q − 1)(
√q + 1)nn!

(qE) logp(q) q−1
2 2nn!

(4
Z) 2nn!

(mZ) For m = 5, 6, 7, 8, 9 the orders are

5 − 1
2 2
nn!, 2
nn!, 7 − 1
2 2
nn!, 4
nn!, 3.2
nn!

respectively.

The number of codes that are equivalent to a given code C is then

|G|
|Aut(C)| .

In most cases it is possible to determine the total number Tn (say) of distinct self-dual codes

of length n in one of our families. Then

Tn = ∑

inequivalent
C
 |G|
|Aut(C)|

where the sum is over all inequivalent codes. In other words

∑

inequivalent
C
 1
|Aut(C)| = Tn
|G| . (4)

6

Equation (4) is called a mass formula. The appropriate values of Tn are:

(2) 1
2 n−1
∏

i=1 (2
i + 1) (n ≡ 0 (mod 2)) (5)

(2II) (weights divisible by 4):
 2
 1
2 n−2
∏

i=1 (2
i + 1) (n ≡ 0 (mod 8)) (6)

(3)
 2
 1
2 n−1
∏

i=1 (3
i + 1) (n ≡ 0 (mod 4)) (7)

(4H) 1
2 n−1
∏

i=0 (2
2i+1 + 1) (n ≡ 0 (mod 2)) (8)

(4E) 1
2 n−1
∏

i=1 (4
i + 1) (n ≡ 0 (mod 2)) (9)

(4H+) n∏

i=1
(2
i + 1) (10)

(4
H+
II ) (all weights even):
 2
 n−1∏

i=1(2
i + 1) (n ≡ 0 (mod 2)) (11)

(qH) 1
2 n−1
∏

i=0 (qi+ 1
2 + 1) (n ≡ 0 (mod 2)) (12)

(qE)
 b
 1
2 n−1
∏

i=1 (qi + 1) (n ≡ 0 (mod 2)) (13)

where b = 1 if q is even, 2 if q is odd

(4
Z) n/2∑

k=0 σ(n, k)2
k(k+1)/2 , (14)

where σ(n, k), the number of binary self-orthogonal [n, k] codes with all weights divisible by

4, is equal to 1 if k = 0, and otherwise is given by

k−1∏

i=0
 2n−2i−2 + 2[ n
2 ]−i−1 − 1
2i+1 − 1 , if n ≡ ±1 (mod 8) ,

7

k−1∏

i=0
 2n−2i−2 − 1
2i+1 − 1 , if n ≡ ±2 (mod 8) ,

k−1∏

i=0
 2n−2i−2 − 2[ n
2 ]−i−1 − 1
2i+1 − 1 , if n ≡ ±3 (mod 8) ,

[k−2∏

i=0
 2n−2i−2 + 2 n
2 −i−1 − 2
2i+1 − 1
 ]
 ·
 [ 1
2k−1 + 2n−2k + 2 n
2 −k − 2
2k − 1
 ]
 , if n ≡ 0 (mod 8) ,

[k−2∏

i=0
 2n−2i−2 − 2 n
2 −i−1 − 2
2i+1 − 1
 ]
 ·
 [ 1
2k−1 + 2n−2k − 2 n
2 −k − 2
2k − 1
 ]
 , if n ≡ 4 (mod 8) .

There is a similar but even more complicated formula for Tn for self-dual codes over Z4 with

Euclidean norms divisible by 8, see [101].

Formulae (5)–(13) are based on various sources including [134], [191], [226], [190, Chap. 19].

Equation (14) is due to Gaborit [101].

Here are two proofs of (5). (i) Let σn,k denote the number of [n, k] self-orthogonal codes C

containing 1. Any such C can be extended to an [n, k + 1] self-orthogonal code D by adjoining

any vector of C ⊥ \ C, and any D will arise 2k − 1 times from diﬀerent C’s. So we have σn,1 = 1,

σn,k+1
σn,k = 2n−2k − 1
2k − 1 ,

and σn,n/2 gives (5). (ii) A more sophisticated proof can be obtained by observing that the

Euclidean inner product induces a symplectic geometry structure on the space of even weight

vectors modulo 1. A self-dual code is then a maximally isotropic subspace. The number of

maximally isotropic subspaces of a symplectic geometry of dimension 2k is Πk
i=1(2i + 1) [34,

§9.4], and we obtain (5) by noting that our symplectic geometry has dimension n − 2.

Similarly, a binary self-dual code with weights divisible by 4 is a maximally totally singular

subspace of the orthogonal geometry of dimension n − 2 induced by 1
2 wt(v), which leads to (6).

Equations (7), (9), (11), (13) are also obtained via orthogonal geometry, (10) via symplectic

geometry, and (8) and (12) via unitary geometry.

These mass formulae are useful when one is attempting to ﬁnd all inequivalent codes of

a given length (compare Section 11). For example, suppose we are trying to ﬁnd all binary

self-dual codes of length 8. We immediately ﬁnd two codes, i2 ⊕i2 ⊕i2 ⊕i2, where i2 = [11], and

the Hamming code e8, and then it appears that there are no others. To prove this, we compute

the automorphism groups of these two codes: they have orders 244! = 384 and 8.7.6.4 = 1344,

respectively. We also calculate T8/|G| = 3.5.9/8! = 3/896 from (5), and see that indeed

1
384 + 1
1344 = 3
896 ,

8

verifying that this enumeration is complete. We will return to this in Section 11.

There are also formulae that give the total number of self-dual codes containing a ﬁxed

self-orthogonal vector or code — see [190, Chapter 19].

2.3. Codes over Z4

Codes over rings are probably less familiar to the reader than codes over ﬁelds, and so we

will add some remarks here about the ﬁrst such case, codes over Z4, family 4
Z.

Any code over Z4 is equivalent to one with generator matrix of the form
[ Ik1 X Y1 + 2Y2
0 2Ik2 2Z
 ]
 (15)

where X, Y1, Y2, Z are binary matrices. Then C is an elementary abelian group of type 4k12k2,

containing 22k1+k2 words. We indicate this by writing |C| = 4k12k2. The dual code C ⊥ has

generator matrix [ (−Y1 + 2Y2)tr − Z trX tr Z tr In−k1−k2
2X tr 2Ik2 0
 ]

and |C ⊥| = 4n−k1−k22k2.

There are two binary codes C (1) and C (2) associated with C, having generator matrices

[Ik1 X Y1] and
 [ Ik1 X Y1
0 Ik2 Z
 ]
 (16)

and parameters [n, k1] and [n, k1 + k2] respectively. If C is self-orthogonal then C (1) is doubly-

even and C (1) ⊆ C (2) ⊆ C (1)⊥. If C is self-dual then C (2) = C (1)⊥. The next two theorems

give the converse assertions.

Theorem 1. If A, B are binary codes with A ⊆ B then there is a code C over Z4 with

C (1) = A, C (2) = B. If in addition A is doubly-even and B ⊆ A⊥ then C can be made

self-orthogonal. If B = A⊥ then C is self-dual.

Proof. Suppose A, B have generator matrices as shown in (16). Then
[ I X Y
0 2I 2Z
 ]
 (17)

is a generator matrix for a code C with C (1) = A, C (2) = B. To establish the second assertion

we must modify (17) to make C self-orthogonal. This is accomplished by replacing the (j, i)th

entry of (17) by the inner product modulo 4 of rows i and j, for 1 ≤ i ≤ k1, 1 ≤ j ≤ k1 + k2,

i < j.
 9

In this way every self-orthogonal doubly-even binary code corresponds to one or more self-

dual codes over Z4.

Theorem 2. [101] A code C over Z4 with generator matrix (15) is self-dual if and only if

C (1) is doubly-even, C (2) = C (1)⊥, and Y2 is chosen so that if M = Y1Y tr
2 , then Mij + Mji ≡

1
2 wt(vi ∩ vj), where v1, . . . , vk1 are the generators of C (1).

In contrast to self-dual codes over ﬁelds, self-dual codes over Z4 exist for all lengths, even

or odd. Furthermore, a self-dual code C over Z4 of length n can be shortened to a self-dual

code of length n − 1 by deleting any one of its coordinates. This is accomplished as follows. If

the projection of C onto the ith coordinate contains all of Z4, the shortened code is obtained

by taking those words of C that are 0 or 2 in the ith coordinate and omitting that coordinate.

If the projection of C onto the ith coordinate contains only 0 and 2, we take the words of C

that are 0 on the ith coordinate and omit that coordinate.

In this way all self-dual codes over Z4 belong to a common “family tree”, with i1 = {0, 2}

at the root. The beginning of this tree, showing all self-dual codes of lengths n ≤ 8, is given

in Fig. 2 of [71].

3. Weight enumerators and MacWilliams theorem

3.1. Weight enumerators

The Hamming weight of a vector u = (u1, . . . , un) ∈ Fn, denoted by wt(u), is the number

of nonzero components ui.

Two other types of “weight” are useful for studying nonbinary codes. For the codes in

families 4
Z, mZ (and hence for 2, 3, and, if q is a prime, qE) we deﬁne the Lee weight and

Euclidean norm of u ∈ F by
 Lee(u) = min{|u|, |F| − |u|} ,

Norm(u) = (Lee(u))
2 .

For a vector u = (u1, . . . , un) ∈ Fn, we set

Lee(u) =
 n∑

i=1 Lee(ui) ,

Norm(u) =
 n∑

i=1 Norm(ui) .

10

Of course, if u is a binary vector, wt(u) = Lee(u) = Norm(u).

It is customary to use the symbol Ai to denote the number of vectors in a code C having

Hamming weight (or Lee weight, or Euclidean norm, depending on context) equal to i. Then

{A0, A1, A2, . . .} is called the weight distribution of the code. The Hamming weight enumerator

(abbreviated hwe) of C is deﬁned to be

WC(x, y) = ∑

u∈C x
n−wt(u)ywt(u) =
 n∑

i=0 Aixn−iyi . (18)

(The adjective “Hamming” is often omitted.) There are good reasons for taking the Hamming

weight enumerator to be a homogeneous polynomial of degree n (see below). However, no

information is lost if we set x = 1, and write it as a polynomial in the single variable y.

There is an analogous deﬁnition for nonlinear codes: for v ∈ F n, let Ai(v) be the number

of codewords at Hamming distance i from v. The average Hamming weight distribution for a

nonlinear or nonadditive code is then

Ai = 1
|C|
 ∑

c∈C Ai(c) ,

with associated Hamming weight enumerator

WC(x, y) =
 n∑

i=0 Aix
n−iyi .

Much more information about a code C is supplied by its complete weight enumerator

(abbreviated cwe) and deﬁned as follows. Let the elements of the alphabet F be ξ0, ξ1, . . . , ξa,

and introduce corresponding indeterminates x0, x1, . . . , xa. Then

cweC (x0, . . . , xa) = ∑

u∈C xn0(u)
0 x
n1(u)
1 · · · xna(u)
a , (19)

where nν(u) is the number of components of u that take the value ξν.

If there is a natural way to pair up some of the symbols in F then we can often reduce

the number of variables in the cwe without losing any essential information, by identifying

indeterminates corresponding to paired symbols. The result is a symmetrized weight enumer-

ator (abbreviated swe). Some examples will make this clear. For linear codes over F4 the

symmetrized weight enumerator is

sweC(x, y, z) = ∑

u∈C xn0(u)yn1(u)zNw(u) = cweC (x, y, z, z) , (20)

11

where n0(u), n1(u) are as above and Nw(u) is the number of components in u that are equal

to either ω or ω. For linear codes over Z4, the appropriate symmetrized weight enumerator is

sweC (x, y, z) = ∑

u∈C x
n0(u)yn±(u)zn2(z) = cweC (x, y, z, y) , (21)

where n±(u) is the number of components of u that are equal to either +1 or −1. There is an

obvious generalization of (21) to linear codes over Zm.

The swe contains only about half as many variables as the complete weight enumerator,

and yet still contains enough information to determine the Lee weight or norm distribution of

a code.

All the weight enumerators mentioned so far can be obtained from the “full weight enu-

merator” of the code. This is a generating function, or formal sum (not a polynomial), listing

all the codewords: ∑

u∈C zu1
1 zu2
2 · · · zun
n ,

where we use a diﬀerent indeterminate zi for each coordinate position. To obtain the sym-

metrized weight enumerator of a code over F4, for example, we replace each occurrence of z0
i

by x, each z1
i by y, and each zω
i or zω
i by z.

Still further weight enumerators that have proved useful can also be obtained from the full

weight enumerator. For example, the split Hamming weight enumerator of a code of length

n = 2m is
 splitC(x, y, X, Y ) = ∑

y∈C xm−l(u)yl(u)X m−r(u)Y r(u) ,

where l(u) (resp. r(u)) is the Hamming weight of the left half (resp. right half) of u. Split

weight enumerators have been investigated in [197], for example. Of course, the split need not

be into equal parts. Multiply-split weight enumerators have been extensively used in [156].

One may also deﬁne weight enumerators for translates of codes: if C is a translate of a

linear or additive code, its weight enumerator is

WC(x, y) = ∑

c∈C x
n−wt(c)ywt(c).

We will use such weight enumerators later in this chapter when studying the “shadow” of a

self-dual code.

The biweight enumerator of a code generalizes the weight enumerator to consider the over-

laps of pairs of codewords, and the joint weight enumerator of two codes C and D considers

12

the overlaps of pairs of codewords u ∈ C and v ∈ D. More generally, the k-fold multiple weight

enumerator of a code considers the composition of k codewords chosen simultaneously from

the code. Again there are generalizations of the MacWilliams and Gleason theorems ([188],

[190, Chap. 5], [280]). The connections between multiple weight enumerators of self-dual codes

and Siegel modular forms have been investigated by Duke [90], Ozeki [208], [212], [218] and

Runge [263]–[266].

Ozeki [218] has recently introduced another generalization of the weight enumerator of a

code C, namely its Jacobi polynomial. For a ﬁxed vector v ∈ Fn, this is deﬁned by

JacC,v(x, z) = ∑

u∈C xwt(u)zwt(u∩v) ,

which is essentially a split weight enumerator. These polynomials have been studied in [10],

[11], [24]. They have the same relationship to Jacobi forms [93] as weight enumerators do to

modular forms (cf. the remarks in Section 14).

For future reference we note the following relations between inner products and weights or

norms for four of our families:

(2):
 (u, v) = 1
2 {wt(u + v) − wt(u) − wt(v)} (22)

(4H+):
 (u, v) = wt(u + v) − wt(u) − wt(v) (23)

(4
Z), (mZ):
 (u, v) = 1
2 {Norm(u + v) − Norm(u) − Norm(v)} . (24)

3.2. Examples of self-dual codes and their weight enumerators

The following are some key examples of self-dual codes of the diﬀerent families mentioned

in Section 1, together with their weight enumerators. Some of these weight enumerators will

be labeled for later reference. Unless indicated otherwise, all the codes mentioned are self-dual

codes of the appropriate kind.

We write [n, k, d]q to indicate a linear code of length n, dimension k and minimal distance

d over the ﬁeld Fq, omitting q when it is equal to 2. [n, k, d]4+ indicates an additive code

over F4 containing 4k vectors (so k ∈ 1
2 Z). Usually the subscript on the symbol for a code

(e.g. e8) gives its length. We adopt the convention that parentheses in a vector mean that all

13

permutations indicated by the parentheses are to be applied to that vector. For example, in the

deﬁnition of e8 below, 1(1101000) stands for the seven vectors 11101000, 10110100, 10011010,

etc. The generators for the hexacode in (34) could have been abbreviated as (100)(1ωω).

The following codes are all self-dual.

(2) The ﬁrst example of a binary self-dual code is the [2, 1, 2] repetition code i2 = {00, 11},

with weight enumerator
 Wi2(x, y) = x2 + y2 = φ2 (say) , (25)

and |Aut(i2)| = 2.

The [8, 4, 4] Hamming code e8 (see Section 12 of Chapter 1; [70], p. 80) generated by

1(1101000), is self-dual with weight enumerator

We8(x, y) = x8 + 14x4y4 + y8 = φ8 , (26)

and group GA3(2) of order 8.7.6.4 = 1344.

The [24, 12, 8] binary Golay code g24 (Section 12 of Chapter 1; [70], Chaps. 3, 11), generated

by
 1(10101110001100000000000) , (27)

or equivalently by the idempotent generator

1(00000101001100110101111) , (28)

has weight enumerator

Wg24(x, y) = x
24 + 759x16y8 + 2576x
12y12 + 759x8y16 + y24 = φ24 . (29)

Aut(g24) is the Mathieu group M24, of order 24.23.22.21.20.48 = 244823040.

All three codes i2, e8, g24 are unique in the sense that any linear or nonlinear code with the

same length, size and minimal distance and containing the zero vector is linear and equivalent

to the code given above [227] (see also [291]).

(3) Self-dual codes over F3 exist if and only if the length n is a multiple of 4 (this follows from

Gleason’s theorem, see (101), and is also a consequence of the argument used to prove (7)

[226]). We use indeterminates x, y for the Hamming weight enumerator W (x, y) and x, y, z for

the cwe.

The [4, 2, 3]3 tetracode t4, generated by {1110, 0121} (Section 7 of Chapter 1; [70] p. 81)

has
 Wt4(x, y) = x4 + 8xy3 (30)

14

and cwe x{x3 + (y + z)3}. Aut(t4) = 2.S(4), where S(n) denotes a symmetric group of order

n!.
 The [12, 6, 6]3 ternary Golay code g12 (Section 12 of Chapter 1; [70], p. 85), generated by

1(11210200000), has
 Wg12(x, y) = x12 + 264x6y6 + 440x3y9 + 24y12 (31)

and (assuming the all-ones codeword is present)

cwe(x, y, z) = x12 + y12 + z12 + 22(x
6y6 + y6z6 + z6x
6) + 220(x
6y3z3 + x
3y6z3 + x3y3z6) . (32)

Aut(g12) = 2.M12 (where M12 is a Mathieu group), of order 190080.

These two codes are unique in the same sense as our binary examples [227].

(4H) We use indeterminates x, y for the Hamming weight enumerator, x, y, z for the swe

and x, y, z, t (corresponding to the symbols 0, 1, ω, ω) for the cwe, so that swe(x, y, z) =

cwe(x, y, z, z).

The [2, 1, 2]4 repetition code i2 = {00, 11, ωω, ωω} has

Wi2(x, y) = x
2 + 3y2 ,

swe = x
2 + y2 + 2z2 ,

cwe = x
2 + y2 + z2 + t2 , (33)

and a group of order 12.

The [6, 3, 4]4 hexacode h6 (Section 12 of Chapter 1, [70, p. 82]) in the form with generator

matrix 

 1 0 0 1 ω ω
0 1 0 ω 1 ω
0 0 1 ω ω 1
 

 (34)

has
 Wh6(x, y) = x
6 + 45x2y4 + 18y6, (35)

swe = x
6 + y6 + 2z6 + 15(2x2y2z2 + x
2z4 + y2z4) , (36)

cwe = x
6 + y6 + z6 + t6 + 15(x
2y2z2 + x2y2t2 + x2z2t2 + y2z2t2) (37)

and Aut(h6) = 3.S(6), of order 2160.

Again these codes are unique.
 15

Of course this i2 is simply the F4-span of the binary code i2 deﬁned above. In general, if

C is deﬁned over an alphabet F, and F′ ⊇ F is a larger alphabet, we write C ⊗ F′ to indicate

this process.

If C is a binary self-dual code then C ⊗ F4 is a self-dual code belonging to both families

4H and 4E. Conversely, it is not diﬃcult to show that if C is self-dual over F4 with respect to

both the Hermitian and Euclidean inner products, then C = B ⊗ F4 for some self-dual binary

code B.

(4E) The [4, 2, 3]4 Reed-Solomon code [ 1 1 1 1
0 1 ω ω
 ]

has
 W (x, y) = x
4 + 12xy3 + 3y4 ,

swe = x
4 + y4 + 2z4 + 12xyz2 ,

cwe = x
4 + y4 + z4 + t4 + 12xyzt .

The automorphism group is 3.S(4), of order 72.

(4H+) The smallest example is the [1, 1
2 , 1]4+ code i1 = {0, 1}, with automorphism group of

order 2 (conjugation). The [12, 6, 6]4+ dodecacode z12 can be deﬁned as the cyclic code with

generator ω10100100101 ([49], see also [134]). Aut(z12) is a semi-direct product of Z(3)3 with

S(4) (where Z(n) denotes a cyclic group of order n) and has order 648.

(qH) Since the norm map from Fq to F√q is surjective, there is an element a ∈ Fq with aa = −1.

Then [1a] is self-dual.

(qE) As in family 4H, there is a restriction on n: if q ≡ 3 (mod 4) then self-dual codes exist

if and only if n is a multiple of 4; for other values of q, n need only be even [226]. Provided

q ̸≡ (3) (mod 4), Fq contains an element i such that i2 = −1, and then [1i] is self-dual.

(4
Z) The smallest example is the self-dual code i1 = {0, 2} of length 1. The octacode o8 ([70],

[71]) is the length 8 code generated by the vectors 3(2001011), or equivalently with generator

matrix 




 1 0 0 0 2 1 1 1
0 1 0 0 3 2 1 3
0 0 1 0 3 3 2 1
0 0 0 1 3 1 3 2
 



 , (38)

having minimal Lee weight 6 and minimal norm 8,

swe = x
8 + 16y8 + z8 + 14x
4z4 + 112xy4z(x
2 + z2) ,

16

and |Aut(o8)| = 2.1344.

The most interesting property of the octacode is that when mapped to a binary code under

the Gray map
 0 → 00, 1 → 01, 2 → 11, 3 → 10 , (39)

o8 becomes the Nordstrom-Robinson code, a nonlinear binary code of length 16, minimal

distance 6, containing 256 words (Section 14 of Chapter 1, Chapter xx (Helleseth-Kumar),

[99], [119]). The latter is therefore a formally self-dual binary code, see Section 3.3.

The octacode reduces mod 2 to the Hamming code e8. There is another lift of e8 to Z4,

namely the code E8, with generator matrix






 1 0 0 0 0 1 1 1
0 1 0 0 3 0 1 3
0 0 1 0 3 3 0 1
0 0 0 1 3 1 3 0
 



 , (40)

but the minimal Lee weight and norm are now both only 4. However, not all binary self-dual

codes lift to self-dual codes over Z4, e.g. {00, 11} does not.

Theorem 3. (a) Let C be a binary self-dual code of length n. A necessary and suﬃcient

condition for C to be lifted to a self-dual code ˆC over Z4 is that all weights in C are divisible

by 4. (b) If this condition is satisﬁed, ˆC can be chosen so that all norms are divisible by 8.

(c) More generally, a self-dual code over Zm, m even, that reduces to a self-dual code mod 2

lifts to Z2m precisely when all norms are divisible by 2m, and in that case all norms in the

lifted code can be arranged to be divisible by 4m. Thus if a code lifts from Zm to Z2m then it

lifts to Z2km for all k. In particular, if a binary code lifts to Z4 then it lifts to a self-dual code

over the 2-adic integers.

Proof. (a) (Necessity) Suppose v ∈ C has weight wt(v) ̸≡ 0 (mod 4), and let ˆv ∈ ˆC be any

lift of v. Then Norm(ˆv) ≡ Norm(v) (mod 4) because for integers x, y if x ≡ y (mod 2) then

x2 ≡ y2 (mod 4).

(Suﬃciency) Without loss of generality C has a generator matrix of the form [IA] where

AAtr ≡ −I (mod 2). Let B be any lift of A to Z4. We wish to ﬁnd ˆA = B + 2M such that

ˆA ˆAtr ≡ −I (mod 4), since then we can take ˆC = [I ˆA]. We have

ˆA ˆA
tr ≡ BBtr + 2(M Btr + BM tr) (mod 4) .

17

The condition on C implies that BBtr + I has even coeﬃcients and is zero on the diagonal.

But then there exists a binary matrix M ′ such that 2(M ′ + M ′tr) = BBtr + I, and we take

M = M ′(B−1)tr. This completes the proof of (a).

(b) We need to show that we can choose ˆA so that the diagonal entries of ˆA ˆAtr + I are

zero mod 8. Set ˆA′ = ˆA − 2L ˆA, where L is symmetric, so that

ˆA
′( ˆA
′)
tr = ˆA ˆA
tr + 4L + 4L2(mod 8) .

Let ∆ = 1
4 ( ˆA ˆAtr + I). Then we need L2 + L + ∆ ( mod 2) to be symmetric with zero diagonal.

It is easy to see that we can accomplish this provided trace(∆) ≡ 0 (mod 2) (consider, for

instance, L = ( 1
1 1
0
 )
.) In fact, we have

1 ≡ det( ˆA ˆA
tr) ≡ 1 + 4 trace ∆ (mod 8)

so trace ∆ is even.

The proof of (c) is analogous.

It follows from Theorem 3 that the Golay code g24 can be lifted to Z4. Since g24 is

an extended cyclic code, the lift can be easily performed by Graeﬀe’s method [71], [313].

Suppose g2(x) divides xn − 1 (mod 2), and we wish to ﬁnd a monic polynomial g(x) over Z4

such that g(x) ≡ g2(x) (mod 2) and g(x) divides xn − 1 (mod 4). Let g2(x) = e(x) − d(x),

where e(x) contains only even powers and d(x) only odd powers. Then g(x) is given by

g(x2) = ±(e2(x) − d2(x)). Applying this technique to the generator polynomial for g24, that

is, to g2(x) = 1 + x + x5 + x6 + x7 + x9 + x11 (see (27)), we obtain g(x) = −1 + x + 2x4 − x5 −

x6 − x7 − x9 + 2x10 + x11, and so

3(31002333032100000000000) (41)

generates a self-dual code G24 of length 24 which is the Golay code lifted to Z4. Iterating this

process enables us to lift cyclic or extended cyclic codes to Z2m for arbitrarily large m.

(F1) Let q = 5. Then 

 1 −v v −1 0 0
0 1 −v v −1 0
0 0 1 −v v −1
 

 (42)

where v = (1 + u)/2, generates a self-dual code of length 6 over F5[u]/(u2).

The matrix (42) also generates self-dual codes from family qH. Suppose q is a prime power

such that v2 − v − 1 has no solution in Fq, and let v be a solution in Fq2. Then (42) deﬁnes

18

a Hermitian self-dual code over Fq2 with minimal distance 4. In the case q = 2 we get the

hexacode.

(F3) The 2-adic Hamming code [50] is the self-dual code of length 8 with generator matrix






 1 λ λ − 1 −1 0 0 0 1
0 1 λ λ − 1 −1 0 0 1
0 0 1 λ λ − 1 −1 0 1
0 0 0 1 λ λ − 1 −1 1
 



 ,

where λ is the 2-adic integer (1 + √
−7)/2. The 2-adic expansion of λ is

λ = 2 + 4 + 32 + 128 + 256 + 512 + 1024 + 2048 + 4096 + 32768 + · · ·

This is the cyclic code with generator

1, λ, λ − 1, −1, 0, 0, 0

with a 1 appended to each of the generators.

Similarly, the 2-adic self-dual Golay code of length 24 is the cyclic code with generator

1, 1 − λ, −2 − λ, −4, λ − 4, 2λ − 3, 2λ + 1, λ + 3, 4, 3 − λ, −λ, −1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,

where now λ = (1 + √−23)/2, with a 1 appended to each of the 12 generators.

The 3-adic self-dual Golay code of length 12 is the cyclic code with generator

1, λ, −1, 1, λ − 1, −1, 0, 0, 0, 0, 0 ,

where λ = (1 + √−11)/2, again with a 1 appended to each generator.

(F4) We shall not discuss these codes here, but refer the reader to Wood [331].

3.3. MacWilliams Theorems

MacWilliams ([185]; see also [190]) discovered that the Hamming weight distribution of

the dual of a linear code is determined just by the Hamming weight distribution of the code.

There are versions of this theorem for most of our families of codes. Although there are

several ways to state these identities, the simplest formulation is always in terms of the weight

enumerator polynomials (it is for this reason that we insist that the weight enumerator should

be a homogeneous polynomial).

Theorem 4. (MacWilliams and others.)
 19

(2) Three equivalent formulations of the result for binary self-dual codes are:

WC⊥(x, y) = 1
|C| WC(x + y, x − y) , (43)

∑

u∈C⊥ xn−wt(u)ywt(u) = 1
|C|
 ∑

u∈C(x + y)
n−wt(u)(x − y)
wt(u) , (44)

and, if {A⊥
0 , A⊥
1 , . . .} is the weight distribution of C ⊥,

A
⊥
k = 1
|C|
 n∑

i=0 AiPk(i) (45)

where
 Pk(x) =
 k∑

j=0
(−1)
j (x
j
 )(n − x
k − j
 )

, k = 0, . . . , n ,

is a Krawtchouk polynomial ([190], Chap. 5; etc.). There are analogous Krawtchouk polyno-

mials for any alphabet, see [190], p. 151. For the remaining cases we give just the formulation

in terms of weight enumerators.

(3)
 WC⊥(x, y) = 1
|C| WC(x + 2y, x − y) ,

cweC⊥(x, y, z) = 1
|C| cweC (x + y + z, x + ωy + ωz, x + ωy + ωz) .

(4H) and (4H+)

WC⊥(x, y) = 1
|C|WC(x + 3y, x − y) ,

sweC⊥(x, y, z) = 1
|C|sweC (x + y + 2z, x + y − 2z, x − y) ,

cweC⊥(x, y, z, t) = 1
|C|cweC (x + y + z + t, x + y − z − t, x − y + z − t, x − y − z + t) .

(4E)
 WC⊥(x, y) = 1
|C| WC(x + 3y, x − y) ,

sweC⊥(x, y, z) = 1
|C| sweC (x + y + 2z, x + y − 2z, x − y) ,

cweC⊥(x, y, z, t) = 1
|C| cweC⊥ (x + y + z + t, x + y − z − t, x − y − z + t, x − y + z − t) .

(qH)
 WC⊥(x, y) = 1
|C| WC(x + (q − 1)y, x − y) . (46)

20

Let λ be a nontrivial linear functional from Fq to Fp, and set

χβ(x) = e
2πiλ(βx)/p . (47)

The cwe for C ⊥ is obtained from the cwe for C by replacing each xj by

q−1∑

k=0 χξj (ξk)xk .

(We omit discussion of the swe, since there are several diﬀerent ways in which it might be

deﬁned.)

(qE) Same as for qH, but omitting the bar in (47).

(4
Z)
 WC⊥(x, y) = 1
|C| WC(x + 3y, x − y)

sweC⊥(x, y, z) = 1
|C| sweC(x + 2y + z, x − y, x − 2y + z)

cweC⊥(x, y, z, t) = 1
|C| cweC (x + y + z + t, x + iy − z − it, x − y + z − t, x − iy − z + it) .

(mZ)
 WC⊥(x, y) = 1
|C| WC(x + (m − 1)y, x − y) .

The cwe for C ⊥ is obtained from the cwe for C by replacing each xj by

m−1∑

k=0 e
2πijk/mxk . (48)

Proof. We prove the result for family 2. There are analogous proofs for the other cases, cf.

Section 10 of Chapter 1, Section 8 of Chapter xx (Helleseth-Kumar), [182], [190, Chap. 5].

Let f be a polynomial-valued function on Fn
2 . Deﬁne the Fourier (or Hadamard) transform

of f by
 ˆf (u) = ∑

v∈Fn
2 (−1)
u.vf (v), u ∈ Fn
2 .

If C is a linear code it is straightforward to verify that

∑

u∈C⊥ f (u) = 1
|C|
 ∑

u∈C ˆf (u) . (49)

(This is a version of the Poisson summation formula — cf. [91].) Now we set f (u) =

xn−wt(u)ywt(u), and after some algebra (the details can be found on p. 126 of [190]) discover

that
 ˆf (u) = (x + y)
n−wt(u)(x − y)
wt(u) . (50)

Equations (49) , (50) together imply (44).
 21

Examples

(a) The repetition code C over a ﬁeld Fq has Hamming weight enumerator

WC(x, y) = xn + (q − 1)yn ,

so from (46) we deduce that the dual code C ⊥, the zero-sum code, has weight enumerator

WC⊥(x, y) = 1
q {(x + (q − 1)y)
n + (q − 1)(x − y)
n} .

Note that when n = 2, WC⊥ = WC (compare case (e) of Theorem 5).

(b) The binary codes i2 and e8 are self-dual, and indeed one easily veriﬁes that their weight

enumerators x2 + y2 (25) and x8 + 14x4y4 + y8 (26) are left unchanged if x and y are replaced

by (x + y)/
√2 and (x − y)/
√2.

Remarks

1. The map that sends WC(x, y) to 1
|C| WC(x + y, x − y), or that sends {A0, A1, . . .} to

{A⊥
0 , A⊥
1 , . . .} as in (45), is often called the MacWilliams or Krawtchouk transform. A remark-

able theorem of Delsarte [78] — see Chapters xx (Brouwer), yy (Camion), zz (Levenshtein) —

shows that this transform is useful even for nonlinear codes.

2. For the families 2, 4H, 4E and 4H+ all the MacWilliams transforms have order 2, as they

do for the Hamming weight enumerators for families 3 and 4
Z and the swe for 4
Z. For the

cwe in families 3 and 4
Z the square of the MacWilliams transform takes xj to x−j. However,

this does not change the cwe of the code, and so, in all cases, if the MacWilliams transform is

applied twice, the original weight enumerator is recovered.

3. The identity for the swe in family mZ is left to the reader. For (F1) we refer to Bachoc

[8] and for (F4) to Wood [331]. Duality fails for (F2) and weights are undeﬁned in case (F3).

4. Shor and Laﬂamme [281] show that there is an analogue of the MacWilliams identity

for quantum codes. There is also an analogue of the shadow [251].

3.4. Isodual and formally self-dual codes

Following [72], we say that a linear code which is equivalent to its dual is isodual. A (possibly

nonlinear) code with the property that its weight enumerator coincides with its MacWilliams

transform is called formally self-dual. An isodual code is automatically formally self-dual.

It is easy to prove that any self-dual code from family 4
Z produces a formally self-dual

binary code using the Gray map (39) ([99], [119]). As already mentioned in Section 3.2, the

22

octacode o8 produces the (formally self-dual) Nordstrom-Robinson code in this way. Similarly,3

a self-dual code from family 4H+ produces an isodual binary code using the map

0 → 00, 1 → 11, ω → 01, ω → 10 . (51)

We give several examples of this construction.

(i) The code d
+
3 (see Section 11.7) produces the isodual [6, 3, 3] binary code with generator

matrix 


 11 11 00
11 00 11
10 10 10
 


 . (52)

(The dual, which is a diﬀerent code, is obtained by interchanging the last two columns.)

(ii) The shortened hexacode, h5, (see Section 12.4) produces an isodual [10, 5, 4] code.

(iii) The hexacode h6 produces an isodual [12, 6, 4] code. There is an additive but not linear

version of the hexacode, h′
6, found by Ran and Snyders [260], generated by (0011ωω), which

under the map (51) produces a second, inequivalent, isodual [12, 6, 4] code. As members of the

family 4H+, however, h6 and h′
6 are equivalent.

Further examples of formally self-dual codes will be mentioned in Remark 4 following

Theorem 5. Isodual and formally self-dual codes have also been studied in [87], [109], [113],

[121], [160], [190], [287] (see also [72]).

4. Restrictions on weights

4.1. Gleason-Pierce Theorem

It is elementary that in a binary self-orthogonal code the weight of every vector is even, in

a ternary self-dual code the weight of every vector is a multiple of 3, and in a Hermitian self-

dual code over F4 the weight of every vector is even. Furthermore, there are many well-known

binary self-dual codes whose weights are divisible by 4 — see above. The following theorem,

due to Gleason and Pierce, shows that these four are essentially the only possible nontrivial

divisibility restrictions that can be imposed on the weights of self-dual codes.

Theorem 5. (Gleason and Pierce [5].) If C is a self-dual code belonging to any of the families

2 through mZ which has all its Hamming weights divisible by an integer c > 1 then one of the

3We are indebted to Dave Forney for these remarks.

23

following holds:
 (a) |F| = 2, c = 2 (so family 2)

(b) |F| = 2, c = 4 (so family 2)

(c) |F| = 3, c = 3 (so family 3)

(d) |F| = 4, c = 2 (so families 4H, 4E, 4H+, 4
Z)

(e) |F| = q, q arbitrary, c = 2, and

the Hamming weight enumerator of C is

(x2 + (q − 1)y2)
n/2 .

Remarks. 1. The theorem may be proved by considering how the Hamming weight enumer-

ator behaves under the MacWilliams transform — see [285] for details. An alternative proof of

a somewhat more general result is given in [320] — see Theorem 13.5 of Chapter xx (Ward).

2. The same conclusion holds if “C is self-dual” is replaced by “C is formally self-dual”.

3. Note that there are no nontrivial examples from families qH, qE or mZ.

4. There are several points to be mentioned concerning case (e). Linear self-dual codes

with weight enumerator (x2 + (q − 1)y2)n/2 always exist in families 2, 4H, 4E, 4H+, qH; exist

in families qE and mZ precisely when there is a square root of −1 in Fq or Zm respectively; in

particular, they never exist in families 3 or 4
Z.

Furthermore, it is easy to see that any linear code over Fq for q > 2 with weight enumerator

(x2 + (q − 1)y2)n/2 is a direct sum of codes of length 2. However, in the binary case there

are many examples of linear codes with weight enumerator (x2 + y2)n/2 that are not self-dual:

these have been classiﬁed for n ≤ 16, see [287]. These are examples of formally self-dual

codes: see Section 3.4. There are also examples from family 4H+, e.g. the additive code

[1100, 0110, 0011, ωωωω] with weight enumerator (x2 + 3y2)2.

5. In some cases, analogous restrictions can be imposed on Euclidean norms of codewords.

In particular, suppose C is a self-dual code over Zm (that is, a code from families 4
Z or mZ)

where m is even. Then the Euclidean norms of the codewords must be divisible by m, and

may be divisible by 2m ([9], [27], [82], see also Theorem 3).

6. Codes from family (F1) with q = 2 can also satisfy case (d) of the theorem, since they

can be embedded in family 4H+ via the map a + bu → a + bω.

24

Examples

Many of the examples given in Section 3.2 satisfy one of these divisibility conditions:

(2): all self-dual codes satisfy (a), and e8 and g24 satisfy (b). Note that any code satisfying

(b) is self-orthogonal (from (22)).

(3): a code satisﬁes (c) precisely when it is self-orthogonal

(4H): a code satisﬁes (d) precisely when it is self-orthogonal

(4E): a self-dual code satisfying (d) is a linearized binary code

(4H+): The dodecacode z12 satisﬁes (d). Any code satisfying (d) is self-orthogonal.

4.2. Type I and Type II codes

A binary self-dual code C with all weights divisible by 4 is called doubly-even4 or of Type

II; if we do not impose this restriction then C is singly-even or of Type I. We denote these two

families by 2I and 2II. A Type I code may or may not also be of Type II: the classes are not

mutually exclusive. We say a code is strictly Type I if it is not of Type II.

Similarly, we will say that a self-dual code over Zm, m even, from the families 4
Z or mZ is

of Type II if the Euclidean norms are divisible by 2m, or of Type I if they are divisible by m.

(This terminology was introduced in [9], [27], [82].) We denote these families by 4
Z
I (or mZ
I )

and 4
Z
II (or mZ
II).

There is one other situation where a similar distinction can be made. An additive trace-

Hermitian self-dual code over F4 from the family 4H+ is of Type II if the Hamming weights are

even, or of Type I if odd weights may occur (if odd weights do occur then the code cannot be

linear). We denote these two families by 4
H+
I and 4
H+
II .

More generally, we will say that a binary code is doubly-even if all its weights are divisible

by 4, or singly-even if its weights are even. It follows from (22) that a doubly-even code is

necessarily self-orthogonal (and from (23) and (24) that Type II codes over Zm and F4 are

necessarily self-orthogonal).

In view of Theorem 5, in the past self-dual codes over F3 have been called Type III codes,

and Hermitian self-dual codes over F4 have been called Type IV codes. However, we shall not

use that terminology in this chapter.

4The unqualiﬁed term “even” has been used to denote both Type I and Type II codes, and is therefore to
be avoided when speaking of self-dual codes. Use “singly-even” or “doubly-even” instead.

25

5. Shadows

In the three cases where we can deﬁne a Type II code (see the previous section) we can also

deﬁne a certain canonical translate of a code called its shadow [69]. The weight enumerator

of the shadow can be obtained from the weight enumerator of the code via a transformation

analogous to the MacWilliams transform of Theorem 4.

We ﬁrst discuss binary codes.

Lemma 1. Let C be a self-orthogonal singly-even binary code, and let C0 be the subset of

doubly-even codewords. Then C0 is a linear subcode of index 2 in C.

Proof. From (22), 1
2 wt(u) is a linear functional on C, and C0 is its kernel.

Deﬁnition 1. [69]. The shadow5 S of a self-orthogonal binary code C is

S =
 



 C ⊥
0 \ C ⊥ if C is singly-even

C ⊥ if C is doubly-even
 


 .

The weight enumerator of the shadow of C will usually be denoted by SC(x, y).

Examples. (i) If C is the repetition code {0n, 1n} of even length n, then if n ≡ 0 (mod 4),

S = C ⊥ = all even weight vectors, but if n ≡ 2 (mod 4), S = all odd weight vectors. (ii) If

C = i2 ⊕ i2 ⊕ · · · ⊕ i2 then S is the translate of C by 1010 . . . 10. (iii) Let C be the [22, 11, 6]

shorter Golay code g22, obtained by “subtracting” (see Section 11.3) i2 from g24, so that g22

consists of all words of g24 that begin 00 or 11, with these two coordinates deleted. Then S

consists of the remaining words of g24 with the same two coordinates deleted.

Theorem 6. [69] The shadow S has the following properties:

(i) S is the set of “parity vectors” for C; that is,

S = {u ∈ Fn
2 : (u, v) ≡ 1
2 wt(v) mod 2 for all v ∈ C} (53)

(ii) S is a coset of C ⊥

(iii)
 SC(x, y) = 1
|C| WC(x + y, i(x − y)) . (54)

5A somewhat more general deﬁnition of shadow has been proposed in [35], but since it fails to possess the
crucial properties (i) and (iii) of Theorem 6 we shall not discuss it here.

26

Proof. If C is doubly-even then (i) and (ii) are immediate, and (iii) follows from the MacWilliams

transform and the fact that the weights are divisible by 4. Suppose C is singly-even, let C0 be

the doubly-even subcode, and let C1 = C \ C0. Then

C0 ⊆ C ⊆ C ⊥ ⊆ C ⊥
0 . (55)

The ﬁrst and last inclusions have index 2, so C ⊥
0 = C ⊥ ∪ (a + C ⊥), say, where (a, u) = 0 for

u ∈ C0, (a, v) = 1 for v ∈ C1. Thus S = C ⊥
0 \ C0 = a + C0 has the properties stated in (i) and

(ii). Also,
 WC0(x, y) = 1
2 {WC(x, y) + WC(x, iy)} ,

WC⊥
0 (x, y) = 1
|C| {WC(x + y, x − y) + WC(x + y, i(x − y)} ,

so
 SC(x, y) = WC⊥
0 − WC⊥ = 1
|C| WC(x + y, i(x − y)) .

If C is a singly-even self-dual code with doubly-even subcode C0, then C ⊥
0 is the union of

four translates of C0, say C0, C1, C2, C3, with

C = C0 ∪ C2, S = C1 ∪ C3 . (56)

When n is a multiple of 8 then C ′ = C0 ∪ C1 and C ′′ = C0 ∪ C3 are both Type II codes (in

the notation of Chapter xx (Pless), C ′ and C ′′ are neighbors of C). If C has a weight 2 word

then C ′ and C ′′ are equivalent.

Similar deﬁnitions for the shadow can be given in the other two cases mentioned. If C

is an additive trace-Hermitian self-orthogonal code over F4, let C0 be the subcode with even

Hamming weights, and secondly, if C is a self-orthogonal code over Zm (m even) let C0 be the

subcode with Euclidean norms divisible by 2m. In both cases the shadow is deﬁned by:

S =
 



 C ⊥
0 \ C0 if C ̸= C0

C ⊥ if C = C0 .

If C is self-dual from family 4H+ then the quotient group C ⊥
0 /C0 is isomorphic to Z(2) × Z(2).

If C is self-dual from family mZ then C ⊥
0 /C0 is isomorphic to Z(2) × Z(2) if n is even and to

Z(4) if n is odd.

There are analogues of Theorem 6.
 27

Theorem 7. Let C be a self-orthogonal additive code over F4, with shadow S.

(i) S = {u ∈ Fn
4 : (u, v) ≡ wt(v) (mod 2) for all v ∈ C}

(ii) S is a coset of C ⊥

(iii)
 SC(x, y) = 1
|C| WC(x + 3y, y − x) ,

sweS(x, y, z) = 1
|C| sweC (x + y + 2z, −x − y + 2z, y − x)

cweS(x, y, z, t) = 1
|C| cweC (x + y + z + t, −x − y + z + t, −x + y − z + t, −x + y + z − t) .

Remark. It follows from Theorem 7 that there is a code equivalent to C that has 1n ∈ S.

For the number of vectors of weight n in S is

SC(0, 1) = 1
|C| WC(3, 1) > 0 .

All vectors of full weight are equivalent.

Theorem 8. Let C be a self-orthogonal linear code over Z4, with shadow S.

(i) S = {u ∈ Zn
4 : (u, v) ≡ 1
2 Norm(v) (mod 4) for all v ∈ C}

(ii) S is a coset of C ⊥

(iii) sweS(x, y, z) = 1
|C| sweC(x + 2y + z, η(x − y), −x + 2y − z), where η = eπi/4,

cweS (x, y, z, t) = 1
|C| cweC (x + y + z + t, η(x + iy − z − it), −(x − y + z − t), η(x − iy − z + it)) .

Remark. It follows that the shadow contains a vector of the form ±1n. (For cweS (0, 1, 0, 1) =

1
|C| cweC (2, 0, 2, 0) = cweC (1, 0, 1, 0) > 0, since 0n ∈ C.) This observation, and a formula for

the swe equivalent to ours, can be found in [88]. In particular, a self-dual code from family 4
Z
II

contains a vector of the form ±1n.

Theorem 9. Let C be a self-orthogonal linear code over Zm, m even, with shadow S.

(i) S = {u ∈ Zn
m : (u, v) ≡ 1
2 Norm(v) (mod m) for all v ∈ C}

(ii) S is a coset of C ⊥

(iii) The cwe of S is obtained from the cwe of C by replacing each xj by

m−1∑

k=0 e
2πi(j2+2jk)/2mxk ,

and then dividing by |C|.

The proofs are analogous to that of Theorem 6.

28

6. Invariant theory

6.1. An introduction to invariant theory

If C is self-dual then its weight enumerator must be unchanged by the appropriate trans-

formation from Theorem 4. As we will see, this imposes strong restrictions on the weight

enumerator.

We begin by discussing the particular case of the weight enumerator W (x, y) of a binary

doubly-even self-dual code C. Since C is self-dual, Theorem 4 implies

W (x, y) = 1
2n/2 W (x + y, x − y)

= W ( x + y
√2 , x − y
√
2
 ) (57)

(for W (x, y) is homogeneous of degree n). Since all weights are divisible by 4, W (x, y) only

contains powers of y4. Therefore
 W (x, y) = W (x, iy) . (58)

The problem we wish to solve is to ﬁnd all polynomials W (x, y) satisfying (57) and (58).

Invariants. Equation (57) says that W (x, y) is unchanged, or invariant, under the linear

transformation replace x by x + y
√2 ,

T1 :
 replace y by x − y
√2 ,

or, in matrix notation,
 T1 : replace
 (
x
y
)
 by 1
√
2
 ( 1
1 1
−1
 ) (x
y
)
 .

Similarly, (58) says that W (x, y) is also invariant under the transformation

replace x by x
T2 : replace y by iy

or
 T2 : replace
 (
x
y
)
 by ( 1
0 0
i
 ) (x
y
)
 .

Of course W (x, y) must therefore be invariant under any combination T 2
1 , T1T2, T1T2T1, . . .

of these transformations. It is not diﬃcult to show (as we shall see in the next section) that

29

the matrices 1
√2
 ( 1
1 1
−1
 ) and ( 1
0 0
i
 )

when multiplied together in all possible ways produce a group G1 containing 192 matrices.

So our problem now says: ﬁnd the polynomials W (x, y) which are invariant under all 192

matrices in the group G1.

How many invariants? The ﬁrst thing we want to know is how many invariants there are.

This isn’t too precise, because of course if f and g are invariants, so is any constant multiple

cf and also f + g, f − g and the product f g. Also it is enough to study the homogeneous

invariants (in which all terms have the same degree).

So the right question to ask is: how many linearly independent, homogeneous invariants

are there of each degree d? Let’s call this number ad.

A convenient way to handle the numbers a0, a1, a2, . . . is by combining them into a power

series or generating function
 Φ(λ) = a0 + a1λ + a2λ
2 + · · · .

Conversely, if we know Φ(λ), the numbers ad can be recovered from the power series expansion

of Φ(λ).

At this point we invoke a beautiful theorem of T. Molien, published in 1897 ([202]; see also

[13], p. 21; [31], p. 110; [37], p. 301; [200], p. 259; [289], p. 86; [298], p. 29).

Theorem 10. (Molien) For any ﬁnite group G of complex m × m matrices, Φ(λ) is given by

Φ(λ) = 1
|G|
 ∑

A∈G
 1
det(I − λA) . (59)

We call Φ(λ) the Molien series of G. The proof of this theorem is given in the next section.

For our group G1, from the matrices corresponding to I, T1, T2, . . . we get

Φ(λ) = 1
192
 { 1
(1 − λ)2 + 1
1 − λ2 + 1
(1 − λ)(1 − iλ) + · · ·} . (60)

There are shortcuts, but it is quite feasible to work out the 192 terms directly (many are the

same) and add them. The result is a surprise: everything collapses to give

Φ(λ) = 1
(1 − λ8)(1 − λ24) . (61)

30

Interpreting Φ(λ). The very simple form of (61) is trying to tell us something. Expanding

in powers of λ, we have

Φ(λ) = a0 + a1λ + a2λ2 + · · ·

= (1 + λ
8 + λ16 + λ24 + · · ·)(1 + λ24 + λ48 + · · ·) . (62)

We can deduce one fact immediately: ad is zero unless d is a multiple of 8, i.e. the degree

of a homogeneous invariant must be a multiple of 8. (This already proves that the length of

a doubly-even binary self-dual code must be a multiple of 8.) But we can say more. The

right-hand side of (62) is exactly what we would ﬁnd if there were two “basic” invariants, of

degrees 8 and 24, such that all invariants are formed from sums and products of them.

This is because two invariants, θ, of degree 8, and φ, of degree 24, would give rise to the

following invariants. Degree d Invariants Number ad
0 1 1
8 θ 1
16 θ2 1
24 θ3, φ 2
32 θ4, θφ 2
40 θ5, θ2φ 2
48 θ6, θ3φ, φ2 3
· · · · · · · · ·
 (63)

Provided all the products θiφj are linearly independent — which is the same thing as saying

that θ and φ are algebraically independent — the numbers ad in (63) are exactly the coeﬃcients

in
 1 + λ8 + λ16 + 2λ24 + 2λ
32 + 2λ
40 + 3λ48 + · · ·

= (1 + λ8 + λ
16 + λ24 + · · ·)(1 + λ24 + λ
48 + · · ·)

= 1
(1 − λ8)(1 − λ24) , (64)

which agrees with (61). So if we can ﬁnd two algebraically independent invariants of degrees 8

and 24, we will have solved our problem. The answer will be that any invariant of this group

is a polynomial in θ and φ. Now φ8 (Eq. (26)) and φ24 (Eq. (29)), the weight enumerators

of the Hamming and Golay codes, have degrees 8 and 24 and are invariant under the group.

So we can take θ = φ8 and φ = φ24. (It’s not diﬃcult to verify that they are algebraically

independent.) Actually, it is easier to work with

φ
′
24 = φ3
8 − φ24
42 = x4y4(x4 − y4)
4 (65)

31

rather than φ24 itself. So we have proved the following theorem, discovered by Gleason in 1970.

Theorem 11. Any invariant of the group G1 is a polynomial in φ8 and φ′
24.

This also gives us the solution to our original problem:

Theorem 12. Any polynomial which satisﬁes Equations (57) and (58) is a polynomial in φ8

and φ′
24.

Finally, we have characterized the weight enumerator of a doubly-even binary self-dual

code.

Theorem 13. (Gleason [105].) The weight enumerator of any Type II binary self-dual code is

a polynomial in φ8 and φ′
24.

Alternative proofs of this astonishing theorem are given by Berlekamp et al. [14], and

Brou´e and Enguehard [33] (see also Assmus and Mattson [4]). But the proof given here seems

to be the most informative, and the easiest to understand and to generalize.

Notice how the exponents 8 and 24 in the denominator of (61) led us to guess the degrees

of the basic invariants.

This behavior is typical, and is what makes the technique exciting to use. One starts with

a group of matrices G, computes the complicated-looking sum shown in (59), and simpliﬁes the

result. Everything miraculously collapses, leaving a ﬁnal expression resembling (61) (although

not always quite so simple — the precise form of the ﬁnal expression is given in (88), (88)).

This expression then tells the degrees of the basic invariants to look for.

Finding the basic invariants. In general, ﬁnding the basic invariants is a simpler problem

than ﬁnding Φ(λ). In our applications we can often use the weight enumerators of codes

having the appropriate properties, as in the above example, or basic invariants can be found

by averaging, using the following simple result (proved in Section 6.2).

Theorem 14. If f (x) = f (x1, . . . , xm) is any polynomial in m variables, and G is a ﬁnite

group of m × m matrices, then
 f (x) = 1
|G|
 ∑

A∈G A ◦ f (x) (66)

is an invariant, where A ◦ f (x) denotes the polynomial obtained by applying the transformation

A to the variables in f .
 32

Of course f (x) may be zero. An example of the use of this theorem is given below.

To illustrate the use of Theorem 13, we use it to ﬁnd the weight enumerator of the [48, 24, 12]

extended quadratic residue code XQ47, using only the fact that it is a doubly-even self-dual

code with minimal distance 12. This implies that the weight enumerator of the code, which is

a homogeneous polynomial of degree 48, has the form

W (x, y) = x48 + A12x36y12 + · · · . (67)

The coeﬃcients of x47y, x46y2, . . . , x37y11 are zero. Here A12 is the unknown number of code-

words of weight 12. It is remarkable that, once we know Equation (67), the weight enumerator

is completely determined by Theorem 13. For Theorem 13 says that W (x, y) must be a poly-

nomial in φ8 and φ′
24. Since W (x, y) is homogeneous of degree 48, φ8 is homogeneous of degree

8, and φ′
24 is homogeneous of degree 24, this polynomial must be a linear combination of φ6
8,

φ3
8φ′
24 and φ′2
24.

Thus Theorem 13 says that

W (x, y) = a0φ
6
8 + a1φ
3
8φ
′
24 + a2φ
′2
24 , (68)

for some real numbers a0, a1, a2. Expanding (68), we have

W (x, y) = a0(x
48 + 84x44y4 + 2946x
40y8 + · · ·) + a1(x44y4 + 38x40y8 + · · ·)

+ a2(x40y8 − · · ·) , (69)

and equating coeﬃcients in (67), (69) we get

a0 = 1, a1 = −84, a2 = 246 .

Therefore W (x, y) is uniquely determined. When these values of a0, a1, a2 are substituted in

(68) we ﬁnd that

W (x, y) = x
48 + 17296x36y12 + 535095x
32y16

+ 3995376x28y20 + 7681680x
24y24 + 3995376x
20y28

+ 535095x16y32 + 17296x
12y36 + y48 . (70)

This is certainly faster than computing W by examining each of the 224 codewords.

There is a fair amount of algebra involved in computing (61). Here is a second example,

simple enough for the calculations to be shown in full.

33

For a self-dual code from family qH, from (46) the Hamming weight enumerator satisﬁes

W
 ( x + (q − 1)y
√q , x − y
√q
 )
 = W (x, y) . (71)

Let us consider the problem of ﬁnding all polynomials which satisfy (71).

The solution proceeds as before. Equation (71) says that W (x, y) must be invariant under

the transformation
 T3 : replace
 (x
y
)
 by A
 (
x
y
)
 ,

where
 A = 1
√q
 ( 1
1 q − 1
−1
 ) . (72)

Now A2 = I, so W (x, y) must be invariant under the group G2 consisting of the two matrices

I and A.

To ﬁnd how many invariants there are, we compute the Molien series Φ(λ) from (59). We

ﬁnd
 det(I − λI) = (1 − λ)
2 ,

det(I − λA) = det
 

 1 − λ√
q − q−1√q λ

− λ√q 1 + λ√q
 

 = 1 − λ2 ,

Φ(λ) = 1
2
 ( 1
(1 − λ)2 + 1
1 − λ2
 )

= 1
(1 − λ)(1 − λ2) . (73)

which is even simpler than (61). Equation (73) suggests that there might be two basic in-

variants, of degrees 1 and 2 (the exponents in the denominator). If algebraically independent

invariants of degrees 1 and 2 can be found, say g and h, then (73) implies that any invariant

of G2 is a polynomial in g and h.

This time we shall use the method of averaging to ﬁnd the basic invariants. Let us average

x over the group — i.e., apply Theorem 14 with f (x, y) = x. The matrix I leaves x unchanged,

of course, and the matrix A transforms x into (1/
√q)(x + (q − 1)y). Therefore the average,

f (x, y) = 1
2
 [
x + 1
√
q {x + (q − 1)y}

]
 = (
√q + 1){x + (
√q − 1)y}
2
√q ,

is an invariant. Of course any scalar multiple of f (x, y) is also an invariant, so we may divide

by (
√q + 1)/2
√q and take
 g = x + (
√q − 1)y (74)

34

to be the basic invariant of degree 1. To get an invariant of degree 2 we average x2 over the

group, obtaining 1
2
 [x
2 + 1
q {x + (q − 1)y}
2] .

This can be cleaned up by subtracting ((q + 1)/2q)g2 (which of course is an invariant), and

dividing by a suitable constant. The result is

h = y(x − y) ,

the desired basic invariant of degree 2.

Finally g and h must be shown to be algebraically independent: it must be shown that no

sum of the form ∑

i,j cijgih
j, cij complex and not all zero , (75)

is identically zero when expanded in powers of x and y. This can be seen by looking at the

leading terms. The leading term of g is x, the leading term of h is xy, and the leading term

of gihj is xi+jyj. Since distinct summands in (75) have distinct leading terms, (75) can only

add to zero if all the cij are zero. Therefore g and h are algebraically independent. So we have

proved:

Theorem 15. Any invariant of the group G2, or equivalently any polynomial satisfying (71),

or equivalently the Hamming weight enumerator of any self-dual code from family qH, is a

polynomial in g = x + (
√q − 1)y and h = y(x − y).

At this point the reader should cry Stop!, and point out that self-dual codes from family

qH must have even length, and so every term in the weight enumerator must have even degree.

But in Theorem 15, g has degree 1.

Thus we haven’t made use of everything we know about the code. W (x, y) must also be

invariant under the transformation

replace
 (x
y
)
 by B
 (
x
y
)
 ,

where
 B = ( −1
0 0
−1
 ) = −I .

This rules out terms of odd degree. So W (x, y) is now invariant under the group G3 generated

by A and B, which consists of I, A, − I, − A. The reader can easily work out that the

35

new Molien series is
 ΦG3(λ) = 1
2 {ΦG2(λ) + ΦG2(−λ)}

= 1
2
 { 1
(1 − λ)(1 − λ2) + 1
(1 + λ)(1 − λ2)
 }

= 1
(1 − λ2)2 . (76)

There are now two basic invariants, both of degree 2 (matching the exponents in the denom-

inator of (76)), say g2 and h, or the equivalent and slightly simpler pair g∗ = x2 + (q − 1)y2

and h = y(x − y). Hence:

Theorem 16. The Hamming weight enumerator of any Hermitian self-dual code over Fq is a

polynomial in g∗ and h.

The general plan of attack. As these examples have illustrated, there are two stages in

using invariant theory to solve a problem.

Stage I. Convert the assumptions about the problem (e.g. the code) into algebraic con-

straints on polynomials (e.g. weight enumerators).

Stage II. Use the invariant theory to ﬁnd all possible polynomials satisfying these con-

straints.

6.2. The basic theorems of invariant theory

Groups of matrices. Given a collection A1, . . . , Ar of m × m invertible matrices, we can

form a group G from them by multiplying them together in all possible ways. Thus G con-

tains the matrices I, A1, A2, . . . , A1A2, . . . , A2A
−1
1 A
−1
2 A3, . . .. We say that G is generated by

A1, . . . , Ar. We will suppose that G is ﬁnite, which covers all the cases encountered in this

chapter. (For inﬁnite groups, see for example Dieudonn´e and Carroll [79], Rallis [257], Springer

[294], Sturmfels [298], Weyl [326].)

Example. Let us show that the group G1 generated by the matrices

M = 1
√2
 ( 1
1 1
−1
 ) and J = ( 1
0 0
i
 )

36

that was encountered in Section 6.1 does indeed have order 192. The key is to discover (by

randomly multiplying matrices together) that G1 contains

J 2 = ( 1 0
0 −1
 ) , E = (M J)3 = 1+i√2
 ( 1 0
0 1
 ) ,

E2 = i ( 1 0
0 1
 ) , R = M J 2M = ( 0 1
1 0
 ) .

So G1 contains the matrices

α ( 1 0
0 ±1
 ) , α ( 0 1
±1 0
 ) , α ∈ {1, i, −1, −i} ,

which form a subgroup H1 of order 16. From this it is easy to see that G1 consists of the union

of 12 cosets of H1:
 G1 =
 12⋃

k=1 akH1 , (77)

where a1, . . . , a6 are respectively

( 1 0
0 1
 ) , ( 1 0
0 i
 ) , 1
√
2
 ( 1 1
1 −1
 ) , 1
√2
 ( 1 1
i −i
 ) , 1
√2
 ( 1 i
1 −i
 ) , 1
√2
 ( 1 i
i 1
 ) ,

a7 = ηa1, . . . , a12 = ηa6, and η = (1 + i)/
√2, an 8th root of unity. Thus G1 consists of the 192

matrices
 ην ( 1 0
0 α
 ) , ην ( 0 1
α 0
 ) , ην 1
√
2
 ( 1 β
α −αβ
 ) , (78)

for 0 ≤ ν ≤ 7 and α, β ∈ {1, i, −1, −i}.

As a check, one veriﬁes that every matrix in (78) can be written as a product of M ’s and

J’s; that the product of two matrices in (78) is again in (78); and that the inverse of every

matrix in (78) is in (78). Therefore (78) is a group, and is the group generated by M and J.

Thus G1 is indeed equal to (78).

We have gone into this example in some detail to emphasize that it is important to begin

by understanding the group thoroughly. (For an alternative way of studying G1, see [33,

pp. 160–161].

Invariants. To quote Hermann Weyl [325], “the theory of invariants came into existence

about the middle of the nineteenth century somewhat like Minerva: a grown-up virgin, mailed

in the shining armor of algebra, she sprang forth from Cayley’s Jovian head.” Invariant theory

became one of the main branches of nineteenth century mathematics, but dropped out of

fashion after Hilbert’s work: see Fisher [96] and Reid [261]. In the past thirty years, however,

37

there has been a resurgence of interest, with applications in algebraic geometry (Dieudonn´e and

Carroll [79], Mumford and Fogarty [205]), physics (see for example Agrawala and Belinfante [1]

and the references given there), combinatorics (Doubilet et al. [80], Rota [262], Stanley [296])

and coding theory ([188], [195], [197], [198]). Recently a number of monographs (Benson [13],

Bruns and Herzog [36], Smith [289], Springer [294], Sturmfels [298]) and conference proceedings

([100], [104], [172], [297]) on invariant theory have appeared.

There are several diﬀerent kinds of invariants, but here an invariant is deﬁned as follows.

Let G be a group of g m × m complex matrices A1, . . . , Ag, where the (i, k)th entry of

Aα is a
(α)
ik . In other words G is a group of linear transformations on the variables x1, . . . , xm,

consisting of the transformations

T (α) : replace xi by x
(α)
i =
 m∑

k=1 a
(α)
ik xk, i = 1, . . . , m (79)

for α = 1, 2, . . . , g. It is worthwhile giving a careful description of how a polynomial f (x) =

f (x1, . . . , xm) is transformed by a matrix Aα in G. The transformed polynomial is

Aα ◦ f (x) = f (x(α)
1 , . . . , x
(α)
m )

where each x
(α)
i is replaced by ∑m
k=1 a
(α)
ik xk. Another way of describing this is to think of

x = (x1, . . . , xm)T as a column vector. Then f (x) is transformed into

Aα ◦ f (x) = f (Aαx) , (80)

where Aαx is the usual product of a matrix and a vector. One can check that

B ◦ (A ◦ f (x)) = (AB) ◦ f (x) = f (ABx) . (81)

For example,
 A = ( 1 2
0 −1
 )

transforms x2
1 + x2 into (x1 + 2x2)2 − x2.

Deﬁnition. An invariant of G is a polynomial f (x) which is unchanged by every linear

transformation in G. In other words, f (x) is an invariant of G if

Aα ◦ f (x) = f (Aαx) = f (x) (82)

for all α = 1, . . . , g.
 38

Example. Let
 G4 = {( 1 0
0 1
 ) , ( −1 0
0 −1
 )} ,

a group of order g = 2. Then x2, xy and y2 are homogeneous invariants of degree 2.

Even if f (x) isn’t an invariant, its average over the group,

f (x) = 1
g
 g∑

α=1 Aα ◦ f (x) (83)

is, as was already stated in Theorem 14. To prove this, observe that any Aβ ∈ G transforms

the right-hand side of (83) into 1
g
 g∑

α=1(AαAβ) ◦ f (x) , (84)

by (81). As Aα runs through G, so does AαAβ, if Aβ is ﬁxed. Therefore (84) is equal to

1
g
 g∑

γ=1 Aγ ◦ f (x) ,

which is f (x). Therefore f (x) is an invariant.

More generally, any symmetric function of the g polynomials A1 ◦ f (x), . . . , Ag ◦ f (x) is an

invariant of G.

Clearly, if f (x) and h(x) are invariants of G, so are f (x) + h(x), f (x)h(x), and cf (x) (c

complex); or in other words the set of invariants of G, which we denote by J (G), forms a ring.

One of the main problems of invariant theory is to describe J (G). Since the transformations

in G do not change the degree of a polynomial, it is enough to describe the homogeneous

invariants (for any invariant is a sum of homogeneous invariants).

Basic invariants. Our goal is to ﬁnd a “basis” for the invariants of G, that is, a set of basic

invariants such that any invariant can be expressed in terms of this set. There are two diﬀerent

types of bases one might look for

Deﬁnition. Polynomials f1(x), . . . , fr(x) are called algebraically dependent if there is a poly-

nomial p in r variables with complex coeﬃcients, not all zero, such that p(f1(x), . . . , fr(x))

is identically zero. Otherwise f1(x), . . . , fr(x) are algebraically independent. A fundamental

result from algebra is (Jacobson [155], vol. 3, p. 154):

Theorem 17. Any m + 1 polynomials in m variables are algebraically dependent.

39

The ﬁrst type of basis we might look for is a set of m algebraically independent invariants

f1(x), . . . fm(x). Such a set is indeed a “basis,” for by Theorem 17 any invariant is algebraically

dependent on f1, . . . , fm and so is a root of a polynomial equation in f1, . . . , fm. The following

theorem guarantees the existence of such a basis.

Theorem 18. [37, p. 357] There always exist m algebraically independent invariants of G.

Proof. Consider the polynomial g∏

α=1(t − Aα ◦ xi)

in the variables t, x1, . . . , xm. Since one of the Aα is the identity matrix, t = x1 is a zero of this

polynomial. When the polynomial is expanded in powers of t, the coeﬃcients are invariants,

by the remark immediately following the proof of Theorem 14. Therefore x1 is an algebraic

function of invariants. Similarly each of x2, . . . , xm is an algebraic function of invariants. Now if

the number of algebraically independent invariants were m′ (< m), the m independent variables

x1, . . . , xm would be algebraic functions of the m′ invariants, a contradiction. Therefore the

number of algebraically independent invariants is at least m. But by Theorem 17 this number

cannot be greater than m.

Example. For the preceding group G4, we may take f1 = (x + y)2 and f2 = (x − y)2 as the

algebraically independent invariants. Then any invariant is a root of a polynomial equation in

f1 and f2. For example, x2 = 1
4 (√f1 + √f2)2 ,

xy = 1
4 (f1 − f2) ,

and so on.

However, by far the most convenient description of the invariants is a set f1, . . . , fl of

invariants with the property that any invariant is a polynomial in f1, . . . , fl. Then f1, . . . , fl is

called a polynomial basis (or an integrity basis) for the invariants of G. Of course if l > m then

by Theorem 17 there will be polynomial equations, called syzygies, relating f1, . . . , fl.

For example, f1 = x2, f2 = xy, f3 = y2 form a polynomial basis for the invariants of G4.

The syzygy relating them is
 f1f2 − f 2
2 = 0 .

The existence of a polynomial basis, and a method of ﬁnding it, is given by the next theorem.

40

Theorem 19. (Noether [206]; [326, p. 275].) The ring of invariants of a ﬁnite group G of

complex m × m matrices has a polynomial basis consisting of not more than (m+g
m ) invariants,

of degree not exceeding g, where g is the order of G. Furthermore this basis may be obtained

by taking the average over G of all monomials

x
b1
1 x
b2
2 · · · xbm
m

of total degree ∑ bi not exceeding g.

Proof. Let the group G consist of the transformations (79). Suppose

f (x1, . . . , xm) = ∑

e cex
e1
1 · · · xem
m ,

ce complex, is any invariant of G. (The sum extends over all e = e1 · · · em for which there is

nonzero term x
e1
1 · · · xem
m in f (x1, . . . , xm).) Since f (x1, . . . , xm) is an invariant, it is unchanged

when we average it over the group, so

f (x1, . . . , xm) = 1
g {f (x
(1)
1 , . . . , x
(1)
m ) + · · · + f (x(g)
1 , . . . , x
(g)
m )}

= 1
g
 ∑

e ce{(x(1)
1 )
e1 · · · (x(1)
m )
em + · · · + (x(g)
1 )
e1 · · · (x(g)
m )
em}

= 1
g
 ∑

e ceJe (say) .

Every invariant is therefore a linear combination of the (inﬁnitely many) special invariants

Je =
 g∑

α=1(x(α)
1 )
e1 · · · (x
(α)
m )
em .

Now Je is (apart from a constant factor) the coeﬃcient of ue1
1 · · · uem
m in

Pe =
 g∑

α=1(u1x(α)
1 + · · · + umx
(α)
m )
e , (85)

where e = e1 + · · · + em. In other words, the Pe are the power sums of the g quantities

u1x(1)
1 + · · · + umx
(1)
m , . . . , u1x
(g)
1 + · · · + umx
(g)
m .

Any power sum Pe, e = 1, 2, . . ., can be written as a polynomial with rational coeﬃcients in

the ﬁrst g power sums P1, P2, . . . , Pg. Therefore any Je for

e =
 m∑

i=1 ei > g

41

(which is a coeﬃcient of Pe) can be written as a polynomial in the special invariants

Je with e1 + · · · + em ≤ g

(which are the coeﬃcients of P1, . . . , Pg). Thus any invariant can be written as a polynomial in

those Je with ∑m
i=1 ei ≤ g. The number of such Je is the number of e1, e2, . . . , em with ei ≥ 0

and e1 + · · · + em ≤ g, which is (m+g
m )
. Finally, deg Je ≤ g, and Je is obtained by averaging

x
e1
1 · · · xem
m over the group.

Molien’s theorem. Since we know from Theorem 19 that a polynomial basis always exists,

we can go ahead with conﬁdence and try to ﬁnd it, using the methods described in Section 6.1.

To discover when a basis has been found, we use Molien’s theorem (Theorem 10). This states

that if ad is the number of linearly independent homogeneous invariants of G with degree d,

and
 ΦG(λ) =
 ∞∑

d=0 adλd ,

then
 ΦG(λ) = 1
g
 g∑

α=1
 1
det(I − λAα) . (86)

The proof depends on the following theorem.

Theorem 20. [200, p. 258], [277, p. 17] The number of linearly independent invariants of G

of degree 1 is
 a1 = 1
g
 g∑

α=1 trace(Aα) .

Proof. Let
 S = 1
g
 g∑

α=1 Aα .

Changing the variables on which G acts from x1, . . . , xm to y1, . . . , ym, where (y1, . . . , ym) =

(x1, . . . , xm)T tr, changes S to S′ = T ST −1. We may choose T so that S′ is diagonal (see [37,

p. 252]). Now S2 = S, (S′)2 = S′, hence the diagonal entries of S′ are 0 or 1. So with a change

of variables we may assume
 S =
 











 1 0
. . . 1 0 . . .
0 0
 












42

with say r 1’s on the diagonal. Thus S ◦ yi = yi if 1 ≤ i ≤ r, S ◦ yi = 0 if r + 1 ≤ i ≤ m.

Any linear invariant of G is certainly ﬁxed by S, so a1 ≤ r. On the other hand, by

Theorem 14,
 S ◦ yi = 1
g
 g∑

α=1 Aα ◦ yi

is an invariant of G for any i, and so a1 ≥ r.

Before proving Theorem 10 let us introduce some more notation. Equation (79) describes

how Aα transforms the variables x1, . . . , xm. The dth induced matrix, denoted by A
[d]
α , describes

how Aα transforms the products of the xi taken d at a time, namely xd
1, xd
2, . . . , x
d−1
1 x2, . . .

(Littlewood [183, p. 122]). E.g.
 Aα =
 (a b
c d

)

transforms x2
1, x1x2 and x2
2 into
 a
2x2
1 + 2abx1x2 + b2x
2
2 ,

acx
2
1 + (ad + bc)x1x2 + bdx2
2 ,

c
2x
2
1 + 2cdx1x2 + d
2x
2
2

respectively. Thus the 2nd induced matrix is

A
[2]
α =
 

 a2 2ab b2

ac ad + bc bd
c2 2cd d2
 

 ,

Proof of Theorem 10. To prove (86), note that ad is equal to the number of linearly

independent invariants of degree 1 of G[d] = {A
[d]
α : α = 1, . . . , g}. By Theorem 20,

ad = 1
g
 g∑

α=1 trace A
[d]
α .

Therefore, to prove Theorem 10, it is enough to show that the trace of A
[d]
α is equal to the

coeﬃcient of λd in 1
det(I − λAα) = 1
(1 − λω1) · · · (1 − λωm) , (87)

where ω1, . . . , ωm are the eigenvalues of Aα. By a suitable change of variables we can make

Aα =
 


 ω1 0
. . .
0 ωm
 


 , A
[d]
α =
 








 ωd
1 0
ωd
2 . . . ωd−1
1 ω2

0 . . .
 







 ,

43

and trace A
[d]
α = sum of the products of ω1, . . . , ωm taken d at a time. But this is exactly the

coeﬃcient of λd in the expansion of (87).

It is worth remarking that the Molien series does not determine the group. For example

there are two groups of 2 × 2 matrices of order 8 having

Φ(λ) = 1
(1 − λ2)(1 − λ4)

(namely the dihedral group D8 and the abelian group Z(2) × Z(4)). In fact there exist ab-

stract groups A and B whose matrix representations can be paired in such a way that every

representation of A has the same Molien series as the corresponding representation of B (Dade

[75]).

A standard form for the basic invariants. The following notation is very useful in

describing the ring J (G) of invariants of a group G. The complex numbers are denoted by

C, and if p(x), q(x), . . . are polynomials, C[p(x), q(x), . . .] denotes the set of all polynomials

in p(x), q(x), . . . with complex coeﬃcients. For example Theorem 11 just says that J (G1) =

C[φ8, φ′
24].

Also, ⊕ will denote the usual direct sum operation. For example a statement like J (G) =

R ⊕ S means that every invariant of G can be written uniquely in the form r + s where r ∈ R,

s ∈ S.

Using this notation we can now specify the most convenient form of polynomial basis for

J (G).

Deﬁnition. A good polynomial basis for J (G) consists of homogeneous invariants f1, . . . , fl

(l ≥ m) where f1, . . . , fm are algebraically independent and

J (G) = C[f1, . . . , fm] if l = m , (88)

or, if l > m,
 J (G) = C[f1, . . . , fm] ⊕ fm+1C[f1, . . . , fm] ⊕ · · · ⊕ flC[f1, . . . , fm] . (89)

In words, this says that any invariant of G can be written as a polynomial in f1, . . . , fm (if

l = m), or as such a polynomial plus fm+1 times another such polynomial plus · · · (if l > m).

f1, . . . , fm are called primary invariants and fm+1, . . . , fl (if present) are secondary invariants.

44

Speaking loosely, (88) and (89) say that when describing an arbitrary invariant, f1, . . . , fm are

“free” and can be used as often as needed, while fm+1, . . . , fl are “transients” and can each be

used at most once. Equations (88) and (89) are sometimes called a Hironaka decomposition of

J (G) ([298], p. 39).

For a good polynomial basis f1, . . . , fl we can say exactly what form the syzygies must take.

If l = m there are no syzygies. If l > m there are (l−m+1
2 ) syzygies expressing the products

fifj (m + 1 ≤ i ≤ j ≤ l) in terms of f1, . . . , fl.

It is important to note that the Molien series can be written down by inspection from the

degrees of a good polynomial basis. Let d1 = deg f1, . . . , dl = deg fl. Then

ΦG(λ) = 1
∏m
i=1(1 − λdi) , if l = m , (90)

or
 ΦG(λ) = 1 + ∑m
j=l+1 λdj
∏m
i=1(1 − λdi) , if l > m . (91)

(This is easily veriﬁed by expanding (90) and (91) in powers of λ and comparing with (88) and

(89).)

Some examples will make this clear.

(1) For the group G1 of Section 6.1, f1 = φ8 and f2 = φ′
24 form a good polynomial basis,

with degrees d1 = 8, d2 = 24. Indeed, from Theorem 11 and (61),

J (G1) = C[φ8, φ
′
24]

and
 ΦG1(λ) = 1
(1 − λ8)(1 − λ24) .

(2) For the group G4 deﬁned above, f1 = x2, f2 = y2, f3 = xy is a good polynomial basis,

with d1 = d2 = d3 = 2. The invariants can be described as

J (G4) = C[x
2, y2] ⊕ xyC[x
2, y2] . (92)

In words, any invariant can be written uniquely as a polynomial in x2 and y2 plus xy times

another such polynomial. E.g.

(x + y)
4 = (x
2)
2 + 6x2y2 + (y2)
2 + xy(4x2 + 4y2) .

The Molien series is
 ΦG4(λ) = 1
2
 { 1
(1 − λ)2 + 1
(1 + λ)2
 } = 1 + λ2

(1 − λ2)2

45

in agreement with (91) and (92). The single syzygy is x2 · y2 = (xy)2. Note that f1 = x2,

f2 = xy, f3 = y2 is not a good polynomial basis, for the invariant y4 is not in the ring

C[x2, xy] ⊕ y2C[x2, xy].

Fortunately the following result holds.

Theorem 21. (Hochster and Eagon [133, Proposition 13]) A good polynomial basis exists for

the invariants of any ﬁnite group of complex m × m matrices.

For the proof see [13], [36], [133] or [289].

So we know that for any group the Molien series can be put into the standard form of

(90), (91) (with denominator consisting of a product of m factors (1 − λdi) and numerator

consisting of sum of powers of λ with positive coeﬃcients); and that a good polynomial basis

(88), (89) can be found whose degrees match the powers of λ occurring in the standard form

of the Molien series.

On the other hand the converse is not true. It is not always true that when the Molien

series has been put into the form (90), (91) (by cancelling common factors and multiplying

top and bottom by new factors), then a good polynomial basis for J (G) can be found whose

degrees match the powers of λ in Φ(λ). This is shown by the following example, due to Stanley

[295].

Let G6 be the group of order 8 generated by the matrices diag{−1, −1, −1} and diag{1, 1, i}.

The Molien series is
 ΦG6(λ) = 1
(1 − λ2)3 (93)

= 1 + λ2

(1 − λ2)2(1 − λ4) . (94)

A good polynomial basis exists corresponding to (94), namely

J (G6) = C[x2, y2, z4] ⊕ xyC[x
2, y2, z4] ,

but there is no good polynomial basis corresponding to (93).

Remarks. (1) Shephard and Todd [279] have characterized those groups for which (88) holds,

i.e. for which a good polynomial basis exists consisting only of algebraically independent

invariants. These are the groups known as “unitary groups generated by reﬂections.” A

complete list of the 37 irreducible groups (or families of groups) of this type is given in [279]

and [289], p. 199.
 46

(2) Sturmfels [298] gives an algorithm for computing a good polynomial basis for the ring of

invariants of a ﬁnite group. The computer language MAGMA ([28], [29], [30]) has commands

for computing Molien series and ﬁnding a good polynomial basis (and many other things).

(3) Relative invariants. If χ is a homomorphism from G into the multiplicative group of

the complex numbers (i.e. a linear character of G), then a polynomial f (x) is called a relative

invariant of G with respect to χ if

A ◦ f (x) = χ(A)f (x) for all A ∈ G .

Molien’s theorem for relative invariants states that the number of linearly independent homo-

geneous relative invariants with respect to χ of degree ν is the coeﬃcient of λν in the expansion

of 1
|G|
 ∑

A∈G
 χ(A)
det |I − λA| .

7. Gleason’s theorem and generalizations

We now make use of the machinery developed in the previous section to give a series of

results that characterize the rings to which the various weight enumerators of self-dual codes

belong. The ﬁrst theorems of this type, for binary and ternary codes, were discovered by

Gleason [105]. The results can be proved by the generalizations of the arguments used to

establish Theorem 13. We remind the reader that hwe, swe and cwe stand for Hamming,

symmetrized and complete weight enumerators, respectively. The code under consideration is

denoted by C and its shadow by S.

In each case the conclusion is that the weight enumerator being considered must be an

element of a certain ring R. We describe R by giving its Molien series (also called a Hilbert

series or Poincar´e series)
 Φ(λ) =
 ∞∑

n=0
(dimC Rn)λ
n ,

where Rn is the subspace of homogeneous polynomials in R of degree n. We then give a good

polynomial basis for R (in the sense of (88), (88)).

In many cases R is obtained (as described in the previous sections) as the ring of invariants

of a certain matrix group G. If so then we start by giving generators for G, its order, and, if it

is a well-known group, a brief description. We have preferred to give natural generators for G,

rather than attempting to ﬁnd a minimal but less-intuitive set — in most cases two generators

47

would suﬃce. If G is a reﬂection group we give its number in Shephard and Todd’s list ([279];

[289], page 199).

In other cases (the symmetrized weight enumerator of a Hermitian self-dual code over F4,

(108), for example) the ring R cannot be found directly as the ring of invariants of any group,

but must be obtained by collapsing the ring of complete weight enumerators.

At the end of each subsection is a table that gives, for most of the rings mentioned, a

list of codes whose weight enumerators provide a polynomial basis for the ring. The weight

enumerators of the codes before the semicolon are primary invariants, those after the semicolon

(if present) are secondary invariants.

For example, the ﬁrst line of Table (100) is equivalent to Theorem 13.

7.1. Family 2I: Binary self-dual codes

hwe of code C. ([105], [14], [33], [188]) G = G16 = 〈 1√2
 ( 1
1 1
−1
 ) , ( 1
0 0
−1
 )〉 ∼= dihedral group

D16 (Shephard and Todd #2b), order 16

Φ = 1
(1 − λ2)(1 − λ8)

R : 1
φ2, θ8 , (95)

where φ2 = x2 + y2, θ8 = x2y2(x2 − y2)2. For example, since a Type II code is also a Type I

code, the weight enumerator of g24, (29), must be in this ring. It is:

φ24 = φ
12
2 − 12φ
8
2θ8 + 6φ
4
2θ2
8 − 64θ2
8 .

hwe of shadow S. It follows from Theorem 6 that if C has weight enumerator W (x, y) then

its shadow has weight enumerator S(x, y) = W ((x + y)/
√2, i(x − y)/
√2). This map from W

to S preserves multiplication and addition, so to evaluate it it suﬃces to consider the images

of the generators of the above ring. We ﬁnd that x2 + y2 becomes 2xy and x2y2(x2 − y2)2

becomes −4(x4 − y4)2. So S(x, y) belongs to the ring

R : 1
xy, (x4 − y4)2 . (96)

In particular, every element of the shadow has weight congruent to n/2 mod 4 (since this

is true of the generators).

The shadow must satisfy an additional constraint. If C is Type I, let W (j)(x, y) be the

weight enumerator of coset Cj, j = 0, . . . , 3 (see (56)). Then W (1)(x, y) − W (3)(x, y) is (up to

48

sign) a multiplicative function on codes, i.e., if C is the direct sum of two Type I codes C ′ and

C ′′, then W (1) − W (3) for C is ±1 times the product of the polynomials W (1) − W (3) for C ′

and C ′′. In order for this property to still hold when one (or both) of C ′ and C ′′ is of Type II,

we adopt the convention that for a Type II code, W (1) − W (3) is simply the weight enumerator

of the code.

Then the additional condition satisﬁed by the shadow is that (if C is Type I or Type II)

W (1)(x, y) − W (3)(x, y) is a relative invariant for the group G192 (see (98)) with respect to the

character
 χ ( 1
√
2
 ( 1
1 1
−1
 )) = i
n, χ (( 1
0 0
i
 )) = ηn

where η = (1 + i)/
√2 [69]. An equivalent assertion is that W (1) − W (3) is an absolute invariant

for the subgroup of G192 with determinant 1.

It follows (see [69] for the proof) that for a Type I code W (1)(x, y) − W (3)(x, y) lies in the

following ring:
 Φ = 1 + λ18

(1 − λ8)(1 − λ12)

R : 1, xy(x8 − y8)(x8 − 34x4y4 + y8)
x8 + 14x4y4 + y8, x2y2(x4 − y4)2 . (97)

One of the diﬀerences between binary codes of Types I and II is that whereas the weight

enumerator of the former is invariant under a group of order only 16, the weight enumerator of

the latter is invariant under a group of order 192 (see Eq. (98)). The above result restores the

balance to a certain extent, by requiring W (1) − W (3) to be a relative invariant for the larger

group.

7.2. Family 2II: Doubly-even binary self-dual codes

hwe of C ([105], [14], [33], [188])

G = G192 = 〈 1
√2
 ( 1
1 1
−1
 ) , ( 1
0 0
i
 )〉 , order 192 (98)

(Shephard and Todd #9)
 Φ = 1
(1 − λ8)(1 − λ24)

R : 1
x8 + 14x4y4 + y8, x4y4(x4 − y4)4 . (99)

49

Codes whose weight enumerators give generators for the above rings:

Ring Codes
(95) i2 (25), e8 (26)
(96) i2 (25), e8 (26)
(97) e8 (26), g24 (29); d
+
12, (d10e7f1)+ (§11.3)
(99) e8 (26), g24 (29)
 (100)

Remark. The above groups G16 and G192 are also the two-dimensional real and complex

Cliﬀord groups occurring in quantum coding theory [48], [49]. At present this appears to

be nothing more than a coincidence. However, in view of the other mysterious coincidences

involving the Cliﬀord groups, there may be a deeper explanation that is presently hidden

(compare the remarks in Section 7.9).

7.3. Family 3: Ternary codes

hwe of C ([105]; [14], [188], [190, p. 620])

G = 〈 1
√
3
 [ 1
1 2
−1
 ] , [ 1
0 0
ω
 ] , ω = e
2πi/3〉 , order 48

(Shephard & Todd #6)
 Φ = 1
(1 − λ4)(1 − λ12) (101)

R : 1
x4 + 8xy3, y3(x3 − y3)3 (102)

cwe of C, 1n ∈ C ([198]; [190, p. 617]) (This forces the length to be a multiple of 12.)

G =
 〈 1
√3
 


 1 1 1
1 ω ω
1 ω ω
 


 ,
 


 1 0 0
0 0 1
0 1 0
 


 ,
 


 0 1 0
0 0 1
1 0 0
 


 ,
 


 1 ω ω
 




〉
 ,

order 2592,
 Φ = 1 + λ24

(1 − λ12)2(1 − λ36)

R : 1, β6π2
9
α12, β2
6 , π4
9 (103)

where
 a = x
3 + y3 + z3, b = x
3y3 + y3z3 + z3x
3,

p = 3xyz, α12 = a(a
3 + 8p3),

β6 = a
12 − 12b, π9 = (x3 − y3)(y3 − z3)(z3 − x
3) .

50

cwe of C, not requiring that 1n ∈ C [199] (Now the length is just a multiple of 4.)

G =
 〈 1
√
3
 


 1 1 1
1 ω ω
1 ω ω
 


 ,
 


 1 0 0
0 0 1
0 1 0
 


 ,
 


 1 ω ω
 




〉
 ,

order 96
 Φ = 1 + 4λ12 + λ24

(1 − λ4)(1 − λ12)2 .

R :
 6∑

i=0 f (i)S

where S = C[θ4, θ2
6, t12], s = y + z, t = y − z, θ4 = x(x3 + s3), θ6 = 8x6 − 20x3s3 − s6, f (0) = 1,

f (1) = t2φ4θ6, φ4 = s(8x3 − s3), f (2) = t4φ2
4, f (3) = t6θ6, f (4) = t8φ4, f (5) = t10φ2
4θ6.

Codes: Ring Codes
(102) t4 (30), g12 (31)
(103) e
4+
3 (§11.4), g12 (31), S(36) (§12.2); XQ23 (§12.2) (104)

7.4. Family 4H: Self-dual codes over F4 with Hermitian inner product

hwe of C ([188]; [190, p. 621]):

G =
 〈 1
2
 ( 1 3
1 −1
 )
 ,
 ( 1 0
0 −1
 )〉
 = Weyl group of type G2 ∼= dihedral group D12

(Shephard & Todd #2b)
 Φ = 1
(1 − λ2)(1 − λ6)

R : 1
x2 + 3y2, y2(x2 − y2)2 (105)

cwe of C, 1n ∈ C (There must be some word of full weight, so this is not a severe restriction)

G =
 〈 1
2
 





 1 1 1 1
1 1 −1 −1
1 −1 1 −1
1 −1 −1 1
 




 ,
 





 1 −1 −1 −1
 




 ,
 





 0 1 0 0
1 0 0 0
0 0 0 1
0 0 1 0
 




 ,
 





 1 0 0 0
0 0 1 0
0 0 0 1
0 1 0 0
 






〉

order 576
 Φ = 1 + λ12

(1 − λ2)(1 − λ6)(1 − λ8)(1 − λ12)

R : 1, (x2 − y2)(x2 − z2)(x2 − t2)(y2 − z2)(y2 − t2)(z2 − t2)
x2 + y2 + z2 + t2, (37), f8, f12 (106)

51

where
 f8 = x
8 + · · · (4 terms) + 14x4y4 + · · · (6 terms) + 168x2y2z2t2 = cwe of e8 ⊗ F4

f12 = (s4 − 3x2y2 − 3z2t2)(s4 − 3x2z2 − 3y2t2)(s4 − 3x2t2 − 3y2z2) ,

s4 = x
2y2 + x2z2 + · · · (6 terms) .

cwe of C, assuming 1n ∈ C and C and C have same cwe:

G = previous G together with
 





 1 0 0 0
0 1 0 0
0 0 0 1
0 0 1 0
 






∼= Weyl group of type F4 (Shephard & Todd #28), order 1152

Φ = 1
(1 − λ2)(1 − λ6)(1 − λ8)(1 − λ12)

R : 1
x2 + y2 + z2 + t2, (37), f8, f12 (107)

swe of C, 1n ∈ C: (Set t = z in cwe)

Φ = 1 + λ12

(1 − λ2)(1 − λ6)(1 − λ8)

R : 1, {(x2 − z2)(y2 − z2)}3

x2 + y2 + 2z2, (36), {(x2 − z2)(y2 − z2)}2 (108)

Remark. If we try to apply invariant theory directly to the swe, we are led to the group

G =
 〈 1
2
 


 1 1 2
1 1 −2
1 −1 0
 


 ,
 


 0 1 0
1 0 0
0 0 1
 


 ,
 


 1 −1 −1
 



〉

(Weyl group of type B3, Shephard & Todd #2a) of order 48, with Molien series

Φ = 1
(1 − λ2)(1 − λ4)(1 − λ6) .

However, the invariant of degree 4 is

δ4 = (x2 − z2)(y2 − z2) ,

which cannot be obtained from the swe of any self-dual code of length 4. The ring of invariants

here and the ring in (108) have the same quotient ﬁeld. So there is no group whose ring of

invariants is (108).
 52

Codes: Ring Codes
(105) i2 (33), h6 (35)
(106) i2 (33), h6 (35), e8 ⊗ F4, (e7e5)+ (§11.5); d′
12
(107) i2 (33), h6 (35), e8 ⊗ F4, (e7e5)+ (§11.5)
(108) i2 (33), h6 (35), e8 ⊗ F4; (e7e5)+ (§11.5)
 (109)

Here d′
12 is the code obtained from d
+
12 of Section 11.3 by multiplying the last four coordinates

by ω.

7.5. Family 4E: Self-dual codes over F4 with Euclidean inner product

(This is inadequately treated in [189], where only even codes are considered.) Neither the

hwe nor the swe can be obtained directly from invariant theory, but must be obtained by

collapsing the cwe. Since (v, v) = 0 ⇔ ∑ v2
i = 0 ⇔ ∑ vi = 0 ⇔ (v, 1n) = 0, we may assume

1n ∈ C.

cwe of C
 G =
 〈 1
2
 





 1 1 1 1
1 1 −1 −1
1 −1 −1 1
1 −1 1 −1
 




 ,
 





 0 1 0 0
1 0 0 0
0 0 0 1
0 0 1 0
 




 ,
 





 1 0 0 0
0 0 1 0
0 0 0 1
0 1 0 0
 






〉

order 192
 Φ = 1 + λ16

(1 − λ2)(1 − λ4)(1 − λ6)(1 − λ8)

R : 1, abcd(a2 − b2)(a2 − c2) · · · (c2 − d2)
symmetric polynomials in a2, b2, c2, d2 (110)

where
 a = (+x − y − z − t)/2, b = (−x + y − z − t)/2 ,

c = (−x − y + z − t)/2, d = (−x − y − z + t)/2 .

cwe of C, assuming C has same cwe as C:

G = previous group together with
 





 1 0 0 0
0 1 0 0
0 0 0 1
0 0 1 0
 






(Weyl group of type B4, Shephard & Todd #2a), order 384

Φ = 1
(1 − λ2)(1 − λ4)(1 − λ6)(1 − λ8)

R : symmetric polynomials in a
2, b
2, c
2, d
2 . (111)

53

swe of C: (Set t = z in the above cwe)

Φ = 1 + λ8 + λ16

(1 − λ2)(1 − λ4)(1 − λ6)

R : 1, {(x2 − z2)(y2 − z2)}2, {(x2 − z2)(y2 − z2)}4

x2 + y2 + 2z2, x4 + y4 + 2z4 + 12xyz2, z2(x − y)2(xy − z2) . (112)

hwe of C: (Set t = z = y in the cwe)

Φ = 1 + λ6

(1 − λ2)(1 − λ4)

R : 1, y2(x2 − y2)2

x2 + 3y2, y2(x − y)2 . (113)

Rather surprisingly, (110), (112), (113) appear to be new.

Codes: The following codes will be used:

i2 = [11], cwe = x2 + y2 + z2 + t2, swe = x2 + y2 + 2z2, hwe = x2 + 3y2

c4 =
 [ 1 1 1 1
0 1 ω ω
 ]
 , a [4,2,3] Reed-Solomon code,

cwe = x4 + y4 + z4 + t4 + 12xyzt, swe = x4 + y4 + 2z4 + 12xyz2,
hwe = x4 + 12xy3 + 3y4 .

c6 =
 


 1 1 1 1 1 1
0 0 0 1 ω ω
1 ω ω 0 0 0
 


 ,

cwe = x6 + · · · (4 terms) + 6x3yzt + · · · (4 terms) + 9x2y2z2 + · · · (4 terms),
hwe = x6 + 6x3y3 + 27x2y4 + 18xy5 + 12y6 .
 (114)

Codes: Ring Codes
(110) i2, c4, c6, e8 ⊗ F4; ?
(111) i2, c4, c6, e8 ⊗ F4
(112) i2, c4, c6; e8 ⊗ F4
(113) i2, c4; c6
 (115)

Remark. The question mark in the ﬁrst line of the table indicates that we do not have a

code that produces the degree 16 polynomial in the numerator of (110). Such a code would

necessarily be odd and have the property that the cwe of C is not equal to that of C. Pre-

sumably a random self-dual code would do, but we would prefer to ﬁnd a code with some nice

structure.
 54

7.6. Family 4H+
I : Additive self-dual codes over F4 using trace inner product

hwe of C:
 G =
 〈1
2
 ( 1 3
1 −1
 )〉
 , order 2

Φ = 1
(1 − λ)(1 − λ2)

R : 1
x + y, y(x − y) (116)

cwe of C, 1n ∈ C:

G =
 〈
M4 = 1
2
 





 1 1 1 1
1 1 −1 −1
1 −1 1 −1
1 −1 −1 1
 




 , α4 =
 





 0 1 0 0
1 0 0 0
0 0 0 1
0 0 1 0
 





〉
 , order 8

Φ = 1 + λ3

(1 − λ)(1 − λ2)2(1 − λ4)

R : 1, BCD
A, B2 + C 2, D2, B2C 2 (117)

where
 A = (x + y)/2, B = (x − y)/2, C = (z + t)/2, D = (z − t)/2 . (118)

swe of C, 1n ∈ C: (Set t = z in cwe)

Φ = 1
(1 − λ)(1 − λ2)(1 − λ4)

R : 1
A, B2 + C 2, B2C 2 (119)

where
 A = (x + y)/2, B = (x − y)/2, C = z . (120)

cwe of C, 1n ∈ S: Note that (1n, u) = wt(u) − n1(u) ≡ wt(u) (mod 2) if and only if the

number of 1’s in u is even. So if 1n ∈ S, the cwe is invariant under diag{1, −1, 1, 1}.

G = ⟨M4, diag{1, −1, 1, 1}⟩ , order 6

Φ = 1
(1 − λ)2(1 − λ2)(1 − λ3)

R : 1
D, A + B + C, A2 + B2 + C 2, A3 + B3 + C 3 (121)

where A, B, . . . are as in (118).
 55

swe of C, 1n ∈ S: (Set t = z in cwe)

Φ = 1
(1 − λ)(1 − λ2)(1 − λ3)

R : 1
symmetric polynomials in A, B, C (122)

hwe of S:
 Φ : 1
(1 − λ)(1 − λ2)

R : 1
2y, − 1
2 (x2 − y2) (123)

As a corollary, the weight of a vector in the shadow is congruent to n (mod 2).

hwe of W (1) − W (3): Again we use the terminology W (i), i = 0, . . . , 3, for the cosets of C0

in C ⊥
0 (as in Sect. 5)
 G =
 〈
M2 = 1
2
 ( 1 3
1 −1
 )
 , α2 =
 ( 1 0
0 −1
 )〉

with character χ(M2) = 1, χ(α2) = (−1)n (Ker χ ∼= S3)

Φ = 1
(1 − λ2)(1 − λ3)

R : 1
x2 + 3y2, y(x2 − y2) . (124)

cwe of S, 1n ∈ C: Belongs to image of (117) under the map that sends (x, y, z, t) to

(x, y, z, t)β4M4:
 R : 1, ABD
C, A2 + B2, D2, A2B2 (125)

cwe of W (1) − W (3), 1n ∈ C: G = ⟨M4, α4, β4⟩ with character χ(M4) = 1, χ(α4) = χ(β4) =

(−1)n, order 48
 Φ = 1
(1 − λ)(1 − λ2)(1 − λ3)(1 − λ4)

R : 1
D, A2 + B2 + C 2, ABC, A4 + B4 + C 4 (126)

where
 A = x + y, B = x − y, C = z + t, D = z − t.

56

swe of W (1) − W (3), 1n ∈ C:
 Φ = 1
(1 − λ2)(1 − λ3)(1 − λ4)

R : 1
A2 + B2 + C 2, ABC, A4 + B4 + C 4 (127)

cwe of S, 1n ∈ S: Belongs to image of (121) under the map x → y, y → x, z → t, t → z:

R : 1
−D, A − B + C, A2 + B2 + C 2, A3 − B3 + C 3 (128)

swe of S, 1n ∈ S: Set D = 0 in (128).

hwe of S, 1n ∈ S: Same as (123).

cwe of W (1) −W (3), 1n ∈ S: G = ⟨M4, β4 = diag{1, −1, −1, −1}⟩, with character χ(M4) = 1,

χ(β4) = (−1)n, order 12
 Φ = 1
(1 − λ)2(1 − λ2)(1 − λ3)

R : 1
D, A − B − C, A2 + B2 + C 2, A3 − B3 − C 3 (129)

Remark. We may obtain W (1) − W (3) by applying α4 to W (0) − W (2), which in turn is

obtained by applying β4 to W (0) + W (2).

7.7. Family 4H+
II : Additive even self-dual codes over F4 using trace inner
product

hwe of C: Same as family 4H, see (105).

cwe of C, 1n ∈ C:
 G = ⟨M4, α4, β4⟩ , order 48

Φ = 1 + λ4

(1 − λ2)2(1 − λ4)(1 − λ6)

R : 1, ABCD
D2, A2 + B2 + C 2, A4 + B4 + C 4, A6 + B6 + D6 (130)

swe of C, 1n ∈ C: (Set t = z in cwe)

Φ = 1
(1 − λ2)(1 − λ4)(1 − λ6)

R : 1
symmetric polynomials in A2, B2, C 2 (131)

57

cwe of C (not assuming 1n ∈ C):

G = ⟨M4, β4⟩, order 12

Φ = 1 + λ2 + 2λ4

(1 − λ2)3(1 − λ6) (132)

Codes: The following codes will be used:

i1 = [1], cwe = swe = hwe = x + y

i
′
1 = [ω], cwe = swe = x + z

i
′′
1 = [ω], cwe = x + t, swe = x + z

i2 = [11, ωω], see (114)

i
′
2 = [11, ωω], cwe = x2 + y2 + 2zt, swe = x
2 + y2 + 2z2, hwe = x
3 + 3y2

c3 = [111, ωω0, ω0ω]

c4 = [1111, ω(ω00)]

c
′
4 = [ωωωω, 1(100)]
 Ring Codes
(116) i1, i2
(117) i1, i2, i′
2, c4; c3
(119) i1, i2, c4
(121) i′
1, i′′
1, i2, c′
3
(122) i′
1, i2, c′
3
(123) i1, i2
(125) i1, i2, i′
2, c4; c3
(129) i′
1, i′′
1, i2, c3
(130) i2, i′
2, c′
4, h6; c4
(131) i2, c′
4, h6
 (133)

7.8. Family qH: Codes over Fq, q a square, with Hermitian inner product

The case q = 4 has been studied in Section 7.4. The next case is q = 9, but as little

attention has been paid so far to codes over this ﬁeld we shall not discuss the cwe or swe

further. It is possible to say a little about the Hamming weight enumerator in the general

case.

hwe of C (See Theorem 16):

G =
 〈 1
√q
 ( 1 q − 1
1 −1
 )
 ,
 ( −1 0
0 −1
 )〉
 , order 4

58

Φ = 1
(1 − λ2)2

R : 1
x2 + (q − 1)y2, y(x − y) (134)

(This is somewhat unsatisfactory, since y(x − y) forces a vector of weight 1, which is impossible

in a self-dual code.)

7.9. Family qE: Codes over Fq with Euclidean inner product

The cases q = 2, 3 and 4 have been studied in Sections 7.1, 7.3, 7.5. As q increases the

results rapidly become more complicated.

We ﬁrst discuss the case q = 5 and then say a little about the general case.

cwe of C, q = 5: Let ξ = e2πi/5.

G = 〈 1
√5 (ξrs)r,s=0,...,4, diag{1, ξ, ξ−1, ξ−1, ξ}
〉 , order 240

Φ = φ(λ)
(1 − λ4)(1 − λ6)(1 − λ10)2 (135)

where φ(λ) is a polynomial of degree 26, with φ(1) = 60. A good basis for this ring would

therefore involve about 65 polynomials! Such Behavior is typical of most groups — see Huﬀman

and Sloane [150].

swe of C, q = 5

G =
 〈


 1 2 2
1 ξ + ξ4 ξ2 + ξ3

1 ξ2 + ξ3 ξ + ξ4
 


 , diag{1, ξ, ξ4},
 


 1 0 0
0 0 1
0 1 0
 




〉
 ,

(the reﬂection group [3, 5], a three-dimensional representation of the icosahedral group, Shep-

hard and Todd #23), order 120
Φ = 1
(1 − λ2)(1 − λ6)(1 − λ10)

R : 1
α, β, γ (136)

where
 α = x2 + 4yz

β = x
4yz − x
2y2z2 − x(y5 + z5) + 2y3z3

γ = 5x
6y2z2 − 4x5(y5 + z5) − 10x
4y3z3 + 10x3(y6z + yz6) + 5x2y4z4

− 10x(y7z2 + y2z7) + 6y5z5 + y10 + z10 .

59

Codes: [12], [(100)(133)] and either

d
2+
5 = [(01234)(00000), (00000)(01234), 1111111111]

or
 e
+
10 = [(00014)(00023), 1111111111] (137)

for the invariant of degree 10.

In [181] it was observed that these invariants were already known to Klein [164], [165]. This

paper then went on to remark that “it is worth mentioning that precisely the same invariants

have recently been studied by Hirzebruch in connection with cusps of the Hilbert modular

surface associated with Q(
√5) — see [131], p. 306. However, there does not seem to be any

connection between this work and ours”. An elegant explanation for this was soon found by

Hirzebruch [132]. The basic idea is to take a self-dual code over F5 and to obtain from it

(using a version of Construction A [70]) a lattice over Z[
√5]. The theta series of this lattice is

a Hilbert modular form which can be written down from the swe of the code. This produces

an isomorphism between the ring of swe’s and the appropriate ring of Hilbert modular forms.

The monograph [92] gives a comprehensive account of these connections.

Incidentally, we do not know if the cwe ring described by (135) collapses to (136).

hwe of C, q = 5: ([224]) (Set z = y in swe)

Φ = 1 + λ10 + λ20

(1 − λ2)(1 − λ6)

R : 1, γ, γ2

α, β

where
 α = x
2 + 4y2,

β = y2(x − y)
2(x2 + 2xy + 2y2),

γ = y4(x − y)
4(5x2 + 12xy + 8y2) .

cwe of C, q = 5, 1n ∈ C: (The group is now considerably larger, but the ring of invariants

is no simpler)
 G = ⟨previous group, diag{1, ξ, ξ2, ξ3, ξ4}⟩

60

∼= ±51+2.Sp2(5), a Cliﬀord group [20], [21], [44], [318] (see also [135]), order 30000

Φ = 1 + 3λ20 + 13λ30 + 18λ40 + 28λ50 + 34λ60 + 17λ70 + 4λ80 + 2λ90

(1 − λ10)(1 − λ20)2(1 − λ30)2 .

The sum of the coeﬃcients in the numerator is 120, so again there is no possibility of giving a

good basis.

The degree 10 invariant is the cwe of either of the codes of length 10 given in (137).

cwe of C, general q: It is hard to say anything in general, but if q is an odd prime p we

can at least describe the structure of the group G under which the cwe is invariant.

G =
 〈
M = 1
√p (ξrs)r,s=0,...,p−1, J = diag{1, ξ, ξ4, ξ9, . . .}, −I
〉
 .

If 1n ∈ C then the cwe is invariant under the larger group G+ = ⟨G, P ⟩, where

P : xj → xj+1, (subscripts mod p)

We use Ξ(H) to denote the center of a group H.

Theorem 22. (a) Suppose p ≡ 1 (mod 4). Then G has structure Z(2) × SL2(p) and center

Ξ(G) = ⟨−I⟩. G+ has structure Z(2) × p1+2 SL2(p) and Ξ(G+) = ⟨−I, ξI⟩. (b) Suppose

p ≡ 3 (mod 4). Then G has structure Z(4) × SL2(p) and Ξ(G) = ⟨iI⟩. G+ has structure

Z(4) × p1+2SL2(p) and Ξ(G+) = ⟨iI, ξI⟩. In either case G and G+ are preserved by the Galois

group Gal(Q[
√p, ξ]/Q).

Remarks. (i) The group G was ﬁrst studied in the present context by Gleason [105]. The

groups G and G+ (also for composite odd q, and with the appropriate modiﬁcation for even q

as well) are a special case of the construction in [324]. Weil obtains analogs of G+, in which

Fq can be replaced by any locally compact abelian group isomorphic to its Pontrjagin dual.6

(ii) The analogous results for p = 2 are given in Sections 7.1 and 7.2. (iii) In both cases (a)

and (b) G+ is the full normalizer (with coeﬃcients restricted to Q[
√
p, ξ]) of the extraspecial

p-group E = ⟨P, Q⟩, where Q = diag{1, ξ, ξ2, ξ3, . . .} (cf. [44]).

Proof. G normalizes E, since M P M −1 = Q−1, M QM −1 = P , JP J −1 = ξaP Q−2, JQJ −1 =

ξbQ for appropriate integers a and b. (Note that ξI = P QP −1Q−1 ∈ E.) Thus we have a

6We are grateful to N. D. Elkies for this comment.
 61

surjective homomorphism φ from G to SL2(p) : M → ( 0
1 −1
0
 ), J → ( 1
−2 0
1
 ). In particular G

is transitive on E/⟨ξI⟩.

Suppose G ∩ E is nontrivial. If there were a noncentral element of E in G then by the

transitivity of G it would follow that ξcP ∈ G and ξdQ ∈ G for some c, d. But then ξI ∈ G.

This would force the length of C to be a multiple of p, which is false (since there is always a

code of length 4). Hence G ∩ E = {I}.

E is irreducible, so the centralizer of E consists only of multiples of I. It follows that ker φ

consists of multiples of elements of E. But the fourth power of an element of ker φ would be in

E, and this must be I. Thus ker φ is either ⟨−I⟩ or ⟨iI⟩. If p ≡ 1 ( mod 4) then i ̸∈ Q[
√p, ξ], so

the ﬁrst possibility obtains. It remains to show that iI ∈ G when p ≡ 3 (mod 4). The matrix

(M J)pM 2 is readily veriﬁed to belong to ker φ. But det((M J)pM 2) = (det M )p+2. Since M 2

maps xj to x−j, det M 2 = −1, so det M = ±i. It follows that (M J)pM 2 is ±iI.

Corollary 1. If p ≡ 3 (mod 4) then a self-dual code over Fp must have length divisible by 4.

Proof. iI ∈ G.

The conclusion of Corollary 1 also holds for self-dual codes over Fq, q ≡ 3 (mod 4) [226].

hwe of C, general q: Belongs to the ring (134). If q ≡ 3 (mod 4) we can say more ([128]):

G =
 〈 1
√q
 ( 1 q − 1
1 −1
 )
 ,
 ( i 0
0 i
 )〉
 , order 8

Φ = 1 + λ4

(1 − λ4)2

R : 1, x2y2 − 2xy3 + y4

x4 + 4(q − 1)xy3 + (q − 1)(q − 3)y4, x3y + (q − 3)xy3 − (q − 2)y4

7.10. Family 4Z
I : Self-dual codes over Z4

cwe of C: ([167])

G =
 〈
M4 = 1
2
 





 1 1 1 1
1 i −1 −i
1 −1 1 −1
1 −i −1 i
 




 , α4 = diag{1, i, 1, i}

〉
 , order 64

Φ = 1 + λ10

(1 − λ)(1 − λ4)2(1 − λ8)

R : 1, (BCD)2(B4 − C 4)
A, B4 + C 4, D4, B4C 4 (138)

62

where
 A = x + z, B = y + t, C = x − z, D = y − t . (139)

swe of C: (Set t = y in cwe)
 Φ = 1
(1 − λ)(1 − λ4)(1 − λ8)

R : 1
A, B4 + C 4, B4C 4 (140)

hwe of C: (Set t = z = y in cwe)
 Φ = 1 + λ8

(1 − λ)(1 − λ4)

R : 1, y4(x − y)4

x + y, y(x − y)(x2 + xy + 2y2) (141)

cwe, 1n ∈ C
 G =
 〈

M4, α4,
 





 0 1 0 0
0 0 1 0
0 0 0 1
1 0 0 0
 





〉
 , order 1024

Φ = (1 + λ12)(1 + λ16)
(1 − λ4)(1 − λ8)2(1 − λ16)

R : (1, A12 + B12 + C 12 + D12) × (1, σ16)
A4 + B4 + C 4 + D4, A8 + B8 + C 8 + D8, σ8, A4B4C 4D4 (142)

where
 σ8 = A
4D4 + B4C 4 ,

σ16 = (ABCD)
2(A
4B4 + C 4D4 − A
4C 4 − B4D4)

swe of C, ±1n ∈ C (Set t = y in cwe)

Φ = 1 + λ12

(1 − λ4)(1 − λ8)2

R : 1, A4B4C 4

A4 + B4 + C 4, A8 B8 C 8, B4C 4 . (143)

This ring may also be described as R0 ⊕ B4C 4R0 ⊕ B8C 8R0, where R0 is the ring of symmetric

polynomials in A4, B4, C 4.
 63

hwe of C, ±1n ∈ C: (Set t = z = y in cwe)

Φ = (1 + λ8)(1 + λ12)
(1 − λ4)(1 − λ8)

R : (1, y2(x2 + 3y2)(x2 − y2)2) × (1, y4(x2 − y2)4)
(x2 + 3y2)2, y4(x − y)4 (144)

cwe of C, 1n ∈ S: If 1n ∈ S, Part (i) of Theorem 8 implies that if a vector 0a1b2cdd ∈ C

then b − d + 2c ≡ 1
2 (b + d) + 2c ( mod 4), i.e. b ≡ 3d ( mod 8), and so β4 = diag{1, η, 1, η5} ∈ G.

G = ⟨M4, β4⟩, order 192

Φ = 1 + λ18

(1 − λ)(1 − λ4)(1 − λ8)(1 − λ12)

R : 1, B2C 2D2(B4 − C 4)(B4 + D4)(C 4 + D4)
A, B4 + C 4 − D4, B8 + C 8 + D8, B12 + C 12 − D12 (145)

swe and hwe of C, ±1n ∈ S: Same as (140) and (141), respectively.

cwe of S: the image of (138) under A → B, B → ηC, C → A, D → η3D

Φ = (1 + λ10)
(1 − λ)(1 − λ4)2(1 − λ8)

R : 1, A2C 2D2(−A4 − C 4)
B, A4 − C 4, − D4, − A4C 4 (146)

swe of S: the image of (140) under A → B, B → ηC, C → A

Φ = 1
(1 − λ)(1 − λ4)(1 − λ8)

R : 1
B, A4 − C 4, − A4C 4 (147)

It follows that the norms of vectors in the shadow are congruent to n mod 8.

cwe of S, 1n ∈ C: the image of (143) under A → B, B → ηC, C → A, D → η3D.

swe of S, ±1n ∈ C:
 Φ = 1 + λ12

(1 − λ4)(1 − λ8)2

R : 1, − A4B4C 4

A4 + B4 − C 4, A8 + B8 + C 8, − A4C 4 (148)

64

cwe of S, 1n ∈ S:
R : 1, A2C 2D2(A4 + C 4)(C 4 + D4)(A4 − D4)
B, A4 − C 4 + D4, A8 + C 8 + D8, A12 − C 12 + D12 (149)

swe of S, ±1n ∈ S: same as (147).

cwe of W (1) − W (3):
 G = ⟨M4, γ4 = diag{1, η, −1, η}⟩ , order 768 ,

with character χ(M4) = in, χ(γ4) = ηn

Φ = 1 + λ18

(1 − λ)(1 − λ4)(1 − λ8)(1 − λ12)

R : 1, A2B2C 2(A4 + B4)(A4 + C 4)(B4 − C 4)
D, symmetric polynomials in A4, −B4, −C 4 (150)

swe of W (1) − W (3):
 Φ = 1 + λ18

(1 − λ4)(1 − λ8)(1 − λ12)

R : omit D from (150) (151)

(This ring has also been studied in [88].)

cwe of W (1) − W (3) with 1n ∈ C: G = ⟨M4, β4, γ4⟩, order 6144, with character χ(M4) = in,

χ(β4) = 1, χ(γ4) = ηn; ker(χ) has order 3072

Φ = 1 + λ32

(1 − λ4)(1 − λ8)(1 − λ12)(1 − λ16)

R : 1, A2B2C 2D2(A4 + B4)(A4 + C 4)(A4 − D4)(B4 − C 4)(B4 + D4)(C 4 + D4)
symmetric polynomials in A4, −B4, −C 4, D4 (152)

swe of W (1) − W (3) with 1n ∈ C:

Φ = 1
(1 − λ4)(1 − λ8)(1 − λ12)

R : 1
symmetric polynomials in A4, − B4, − C 4

65

7.11. Family 4Z
II: Type II self-dual codes over Z4

cwe of C, 1n ∈ C [51], [27] In view of the remarks following Theorem 8, this is not a severe

restriction.
 G = ⟨M4, β4, γ4⟩ , order 6144

Φ = (1 + λ16)(1 + λ32)
(1 − λ8)2(1 − λ16)(1 − λ24)

R : (1, f16) × (1, f32)
A8 + B8 + C 8 + D8, f8, A16 + · · · + D16, A24 + · · · + D24 (153)

where
 f8 = A
4C 4 + C 4D4 + D4B4 + B4A
4 − A
4D4 − B4C 4 ,

f16 = (ABCD)
4 ,

f32 = (ABCD)
2(A
4 + C 4)(C 4 + D4)(D4 + B4)(B4 + A
4)(A
4 − D4)(B4 − C 4)

swe of C, ±1n ∈ C
 Φ = 1 + λ16

(1 − λ8)2(1 − λ24)

R : 1, θ16
θ8, h8, θ24 (154)

where
 θ8 = x8 + 28x6z2 + 70x4z4 + 28x2z6 + z8 + 128y8 ,

θ16 = {x2z2(x
2 + z2)
2 − 4y8}{(x
4 + 6x
2z2 + z4)
2 − 64y8} ,

θ24 = y8(x
2 − z2)
8 ,

h8 = {xz(x
2 + z2) − 2y4}
2 .

cwe of C, 1n ∈ C, Lee weights divisible by 4 ([51])

G =
 〈
M4, β4, γ4,
 




 0 0 1 0
0 i 0 0
1 0 0 0
0 0 0 i
 




〉

(Shephard & Todd #2a), order 49152

Φ = 1
(1 − λ8)(1 − λ16)2(1 − λ24)

R : 1
f16, symmetric polynomials in A8, B8, C 8, D8 (155)

66

swe of C, ±1n ∈ C, Lee weights divisible by 4 ([51]) (Set t = y in cwe)

Φ = 1
(1 − λ8)(1 − λ16)(1 − λ24)

R : 1
θ8, θ16, θ24 (156)

However, the following result shows that the extra condition on the Lee weights may not be a

good thing. For it was shown in [119] that most interesting linear codes over Z4 do not have

linear images under the Gray map.

Theorem 23. [51] If C is a self-dual code over Z4 with all Lee weights divisible by 4, then the

binary image of C under the Gray map (39) is linear.

For the proof, see [51].

Codes. The following codes will be used: i1 and D⊕
4 are deﬁned in Section 11.8, and o8 is

the octacode (38). J10 is the self-dual code with generator matrix














 1 0 1 1 1 1 1 0 1 1
0 1 0 0 0 0 3 3 1 0
0 0 2 0 0 0 0 0 0 2
0 0 0 2 0 0 0 0 0 2
0 0 0 0 2 0 0 0 0 2
0 0 0 0 0 2 0 0 0 2
0 0 0 0 0 0 2 0 2 0
0 0 0 0 0 0 0 2 2 2
 














and |J10| = 4226 ([71]). J16 has generator matrix



















 1 0 0 0 0 0 1 1 1 0 3 3 1 0 3 2
0 1 0 0 0 0 1 0 0 1 3 3 1 1 2 3
0 0 1 0 0 0 1 0 0 0 0 2 2 0 3 3
0 0 0 1 0 0 0 1 1 1 3 0 2 3 3 1
0 0 0 0 1 0 0 1 1 1 0 0 1 1 1 1
0 0 0 0 0 1 0 0 0 0 0 3 2 0 1 1
0 0 0 0 0 0 2 0 0 0 0 2 0 2 0 2
0 0 0 0 0 0 0 2 0 0 0 0 0 2 2 2
0 0 0 0 0 0 0 0 2 0 0 0 0 2 2 2
0 0 0 0 0 0 0 0 0 2 0 0 0 2 0 0
 



















and |J16| = 4624.

K4m (m ≥ 1, but note that K4 ∼= D⊕
4 ) is a self-dual code introduced by Klemm [167],

having generator matrix 







 1 1 1 . . . 1 1
0 2 0 . . . 0 2
0 0 2 . . . 0 2
. . . . . . . .
0 0 0 . . . 2 2
 






 ; (157)

67

|K4m| = 4124m−2, g = 24m−1(4m)!, cwe = (A4m + B4m + C 4m + D4m)/2 (see (139)).

Ring Codes
(138) i1, D⊕
4 in 2 versions (177), o8; J10
(140) i1, D⊕
4 , o8
(141) i1, D⊕
4 ; o8
(142) K4, K8, o8, K16; K12, J16
(143) K4, K8, o8; K12
(144) K4, o8; K8, K12
(153) K8, o8, K16, K24; J16,?
(154) K8, o8, K24; J16
(156) K8, K16, K24
 (158)

Again the question mark indicates that we do not have a satisfactory code to produce the

desired polynomial.

7.12. Family m
Z: Self-dual codes over Zm

The Hamming weight enumerator of a self-dual code over Zm for general m has been

considered in [128].

8. Weight enumerators of maximally self-orthogonal codes

In some cases it is possible to prove results analogous to those in Section 7 for codes which

are maximally self-orthogonal yet not self-dual, the [7, 3, 4] Hamming code e7 with weight

enumerator p7 = x7 + 7x3y4 being a typical example. A more trivial example is the zero code

z1 = {0}, with weight enumerator p1 = x.

The following results are proved in [197].

For n odd, let C be an [n, 1
2 (n − 1)] self-orthogonal binary code. Thus C ⊥ = C ∪ (1 + C).

The weight enumerator of C belongs to the module R = p1C[x2 + y2, x2y2(x2 − y2)2] ⊕ p7C[x2 +

y2, x2y2(x2 − y2)2], which in the notation of the previous section would be described by

Φ = λ + λ7

(1 − λ2)(1 − λ8)

R : p1, p7
x2 + y2, x2y2(x2 − y2)2 (159)

(compare (95)). If in addition C is doubly-even, the module is described by:

(a) if n = 8m − 1,
 Φ = λ7 + λ23

(1 − λ8)(1 − λ24)

R : p7, p23
x8 + 14x4y4 + y8, x4y4(x4 − y4)4 (160)

68

(b) if n = 8m + 1,
 Φ = λ + λ17

(1 − λ8)(1 − λ24)

R : p1, p17
x8 + 14x4y4 + y8, x4y4(x4 − y4)4 (161)

(compare (99)). Here p17 = x17 + 17x13y4 + 187x9y8 + 51x5y12, p23 = x23 + 506x15y8 +

1288x11y12 + 253x7y16.

Codes. The code g23 is the cyclic version of g24 obtained by deleting any coordinate.

Ring Codes
(159) i2, e8; z1, e7
(160) e8, g24; e7, g23
(161) e8, g24; z1, (d10e7)+

There are analogous results for ternary codes: see [198].

9. Upper bounds

Of course, we are interested not just in codes per se, but also in good (or, at the very least,

interesting) codes, that is, codes with large minimal distance (Hamming, Lee, or Euclidean,

as appropriate). In order to know if a particular code is good, it is necessary to know how

good comparable codes could be; that is, for a given length and dimension, what is the optimal

minimal distance? For general codes, this question was studied in Chapters xx (Levenshtein),

yy (Brouwer) and zz (Litsyn); we are, of course, interested in self-dual codes. As one might

imagine, the constraint of self-duality usually leads to stronger bounds.

We will concentrate most of our attention on binary codes (family 2), pointing out analogues

to other families as they arise.

Essentially all of the bounds we will be discussing are special cases of the linear program-

ming (or LP) bound (Section 2.5 of Chapter yy (Brouwer)); that is, they rely on the fact that

both the weight enumerator of the code and the weight enumerator of its dual are nonnegative.

For a self-dual code, these weight enumerators are, of course, equal. So for Type II self-dual

binary codes, for instance, we have the following:

Theorem 24. If there exists a Type II self-dual binary code of length n and minimal distance

d, then there exists a homogeneous polynomial W (x, y) with nonnegative (integer) coeﬃcients

69

such that
 2
n/2W (x + y, x − y) = W (x, y)

W (1, y) = 1 + O(yd)

W (x, iy) = W (x, y).

These conditions assert that the code is self-dual, that it has minimal distance d, and that it

is of Type II, respectively.

The analogues for other classes of codes should be clear; in each case, the appropriate enu-

merator (Hamming, symmetrized, complete) is nonnegative, invariant under the appropriate

transformations (see Section 7), and is zero on all terms of low weight. In some cases, we can

add further constraints from shadow theory (Section 5), since the weight enumerator of the

shadow of the code is also nonnegative. For instance:

Theorem 25. If there exists a Type I self-dual binary code of length n and minimal distance

d, then there exist homogeneous polynomials W (x, y) and S(x, y) with nonnegative (integer)

coeﬃcients such that
 W (x, y) = 2
−n/2W (x + y, x − y)

W (1, y) = 1 + O(yd)

S(x, y) = 2
−n/2W (x + y, i(x − y)).

Again there are analogues for each family for which shadows are well-deﬁned (2, 4H+, 4
Z).

Remark. For a code C from family qH (linear over Fq, q a square, with Hermitian inner

product), it can be shown that the polynomial

S(x, y) = q−n/2W ((
√q − 1)x + (
√q + 1)y, y − x)

has nonnegative (but not necessarily integral) coeﬃcients; note that this agrees with the shadow

enumerator for q = 4. This can be used to strengthen the LP bound in those cases. The known

proof that this is nonnegative involves constructing a quantum code Q from C ([249]); S(x, y)

is then the shadow enumerator of Q ([252], proved nonnegative in [253]). There is surely a

more direct proof.

One way to apply the linear programming bound is to ignore the constraint that the coeﬃ-

cients of W (x, y) be nonnegative, and simply ask that the low order coeﬃcients be as speciﬁed.

70

This gives a surprisingly good bound for Type II binary codes. Recall from Theorem 13 that

for C of Type II, W (x, y) lies in the ring

R = C[x8 + 14x4y4 + y8, x
4y4(x
4 − y4)
4],

and if C has length n, W (x, y) has degree n. The subspace of R of degree n has dimension

D = [ n
24 ] + 1. This lets us set the ﬁrst D coeﬃcients of W (x, y) arbitrarily; in particular, there

exists a unique element W ∗(x, y) of R such that W ∗(1, y) = 1 + O(y4D). This is known as

the extremal enumerator, since W ∗ has the largest minimal distance of any Type II self-dual

enumerator. It follows immediately that the minimal distance of any Type II code of length n

is bounded above by the minimal distance of W ∗.

Theorem 26. [196] The ﬁrst nonzero coeﬃcient of W ∗(1, y) occurs precisely at degree 4D;

in particular, the minimal distance of a Type II self-dual binary code of length n is at most

4[n/24] + 4.

In fact it is possible to use the B¨urmann-Lagrange theorem (Theorem 32) to derive an

explicit formula for the number of words of weight 4D in the extremal enumerator. Let

µ = [n/24], so that D = µ + 1. Then we have

Theorem 27. (Mallows and Sloane [196].) A∗
4µ+4, the number of codewords of minimal

nonzero weight 4D = 4µ + 4 in the extremal weight enumerator, is given by:
(n
5
)(5µ − 2
µ − 1
 )∕
(4µ + 4
5
 )

, if n = 24µ , (162)

1
4 n(n − 1)(n − 2)(n − 4) (5µ)!
µ!(4µ + 4)! , if n = 24µ + 8 , (163)

3
2 n(n − 2) (5µ + 2)!
µ!(4µ + 4)! , if n = 24µ + 16 , (164)

and is never zero.

For the proof, see [196] or [190], Chapter 19. There is a similar formula for Type I binary

codes — see [190], Chapter 19, Problem (12).

Results similar to Theorem 26 hold for other families:

Theorem 28. The minimal distance of a Type I binary self-dual code is at most 2[n/8] + 2.

The minimal distance of a Type II binary self-dual code is at most 4[n/24] + 4. The minimal

71

distance of a self-dual code from family 3 is at most 3[n/12] + 3. The minimal distance of a

self-dual code from family 4H is at most 2[n/6] + 2. The minimal distance of a Type II self-dual

code from family 4H+ is at most 2[n/6] + 2. The minimal distance of a self-dual code from

families 4E, 4H+, qH or qE is at most [n/2] + 1.

Note that the last bound is simply the Singleton bound, obtained from the ring C[x2 + (q −

1)y2, y(x − y)] of (134). As we have already remarked in Section 7.8, this is not the correct

ring (that is, the smallest ring containing all Hamming enumerators of self-dual codes). In

some cases (q = 4 or q = 5), we know a smaller ring; however, since the ring is no longer

free, it is much more diﬃcult to use. In particular, it is no longer the case that we may set

the leading coeﬃcients arbitrarily. This leads to the extremal enumerator not being unique,

making it diﬃcult to determine its ﬁrst nonzero coeﬃcient. Similarly, any attempt to make an

analogous argument for families 4
Z or mZ will have the problem that, in those cases, we are

primarily interested in Lee weight or Euclidean norm, forcing us to work with the symmetrized

weight enumerator. This is, of course, much more diﬃcult to deal with than the Hamming

enumerator. A partial solution to this problem is provided by Theorem 34 below.

In each case it can be shown (cf. [193]) that the bounds of Theorems 26 and 28 can be

met for at most ﬁnitely many n: in fact, the next coeﬃcient (A∗
4µ+8) after the leading nonzero

coeﬃcient in the extremal enumerator becomes negative for suﬃciently large n. Furthermore,

for any constant α, the minimal distance can be within α of the bound only ﬁnitely often.

For Type II binary codes, for instance, it was shown in [193] that the A∗
4n+8 term ﬁrst goes

negative when n is around 3720. Ma and Zhu [184] and Zhang [338] have recently determined

precisely when the A∗
4n+8 term ﬁrst goes negative, and have obtained similar results for several

other families. The following result incorporates the work of several authors.

Theorem 29. [338] Let C be a self-dual code of length n from one of the families 2I, 2II, 3,

4H; and let c = 2, 4, 3, 2, respectively, and µ = [n/8], [n/24], [n/12], [n/6]. Then the coeﬃcient

A∗
c(µ+2) in the extremal Hamming weight enumerator is negative if and only if:

(2I): n = 8i (i ≥ 4), 8i + 2 (i ≥ 5), 8i + 4 (i ≥ 6), 8i + 6 (i ≥ 7);

(2II): n = 24i (i ≥ 154), 24i + 8 (i ≥ 159), 24i + 16 (i ≥ 164);

(3): n = 12i (i ≥ 70), 12i + 4 (i ≥ 75), 12i + 8 (i ≥ 78);

(4H): n = 6i (i ≥ 17), 6i + 2 (i ≥ 20), 6i + 4 (i ≥ 22).

In particular, the ﬁrst time A∗
4µ+8 goes negative for Type II codes is at 24 × 154 = 3696.

72

Of course other coeﬃcients in the extremal weight enumerator may go negative before this.

In the case of ternary self-dual codes, for example, family 3, the extremal Hamming weight

enumerator contains a negative coeﬃcient for lengths 72, 96, 120 and all n ≥ 144.

The best asymptotic bound presently known for Type II codes is the following.

Theorem 30. (Krasikov and Litsyn [173].) The minimal distance d of a Type II binary code

of length n satisﬁes
 d ≤ 0.166315 . . . n + o(n), n → ∞ .

The constant in this expression is the real root of 8x5 − 24x4 + 40x3 − 30x2 + 10x − 1.

The proof uses a variant of the linear programming bound.

For Type I binary codes, the bound of Theorem 28 is especially weak. Ward [319] has

shown that the minimal distance can be 2[n/8] + 2 precisely when n is one of 2, 4, 6, 8, 12,

14, 22 or 24. This suggests that the bound can be greatly strengthened, which is indeed the

case. Conway and Sloane [69] showed that d ≤ 2[(n + 6)/10] for n > 72, and Ward ([322], see

also Chapter “Ward”) established d ≤ n/6 + O(log n). It turns out, in fact, that the “correct”

bound is 4[n/24] + 4 (except when n + 2 is a multiple of 24), just as for Type II codes. The

key to proving this fact is the observation that we have not yet used the shadow enumerator.

Theorem 31. (Rains [250].) Suppose C is a [n, n/2, d] self-dual binary code. Then d ≤

4[n/24] + 4, except when n ≡ 22 ( mod 24), when d ≤ 4[n/24] + 6. If n is a multiple of 24, any

code meeting the bound is of Type II. If n ≡ 22 (mod 24), any code meeting the bound can be

obtained by shortening a Type II code of length n + 2 that also meets the bound.

Proof (sketch). From (95), W (x, y) lies in the ring C[x2 + y2, x2y2(x2 − y2)2]; consequently

we can write
 W (1, y) = ∑

j ajy2j

= ∑

i ci(1 + y2)
n/2−4i(y2(1 − y2)
2)
i.

Applying the shadow transform, we have

S(1, y) = ∑

j bjy2j+t

= ∑

i ci(2y)
n/2−4i(−(1 − y4)/2)
i,

73

where t = ((n/2) mod 4). Suppose C had minimal distance 4[n/24] + 6. This fact determines

ci for 0 ≤ i ≤ 2[n/24] + 2, and in particular c2[n/24]+2. On the other hand, we can also

express c2[n/24]+2 as a linear combination of the bj for small j. It turns out that these two

expressions for c2[n/24]+2 are incompatible; in particular, we ﬁnd that a certain nonnegative

linear combination of the bj is negative.

Rather than give the (somewhat messy) details of the proof, we will simply show how one

can compute the coeﬃcients in these linear combinations. This uses the B¨urmann-Lagrange

theorem:

Theorem 32. (B¨urmann-Lagrange.) Let f (x) and g(x) be formal power series, with g(0) = 0

and g′(0) ̸= 0. If coeﬃcients κij are deﬁned by

xjf (x) = ∑

0≤i κijg(x)
i,

then
 κij = 1
i [coeﬀ. of xi−1 in [jxj−1f (x) + xjf ′(x)] ( x
g(x)
 )i].

For proof and generalizations, see [327, p. 133], [106], [273], [274], [275].

For instance, to compute c2[n/24]+2, we note that

∑

i ci(1 + y2)
n/2−4i(y2(1 − y2)
2)
i = 1 + O(y4[n/24]+6).

Dividing both sides by (1 + y2)n/2 and substituting y = √Y , we get:

∑

i ci
 ( Y (1 − Y )2

(1 + Y )4
 )i = (1 + Y )
−n/2 + O(Y 2[n/24]+3).

We can then apply B¨urmann-Lagrange, with

f (Y ) = (1 + Y )
n/2, g(Y ) = Y (1 − Y )
2(1 + Y )
−4

to obtain
 ci = 1
i [coeﬀ. of Y i−1 in [ d
dY (1 + Y )−n/2] (
(1 + Y )4(1 − Y )−2)i]

= −n
2i [coeﬀ. of Y i−1 in (1 + Y )−n/2−1+4i(1 − Y )−2i]

= −n
2i [coeﬀ. of Y i−1 in (1 + Y )−n/2−1+6i(1 − Y 2)−2i].

In particular, for i = 2[n/24] + 2,

c2[n/24]+2 = −n
4[n/24] + 4 [coeﬀ. of Y 2[n/24]+1 in (1 + Y )−n/2+12[n/24]+11(1 − Y 2)−4[n/24]−4].

74

It follows that c2[n/24]+2 ≤ 0, with equality only when n ≡ 22 (mod 24), since all coeﬃcients

of any power series of the form (1 + Y )a(1 − Y 2)−b are positive whenever a, b > 0.

Similarly, we ﬁnd that the coeﬃcients of the expansion of c2[n/24]+2 in terms of the bj are

positive. This proves the bound, except when n ≡ 22 (mod 24); the proof that the bound

holds in that case and that a code meeting the bound is even if n ≡ 0 (mod 24) is left to the

reader.

This bound agrees with the full linear programming bound for n ≤ 200, and, most likely,

for much larger n. However, it is likely that again it can only be attained for ﬁnitely many n.

There is also an analogue of this bound for Type I codes from family 4H+.

Theorem 33. If C is an additive self-dual code of length n and minimal distance d from

family 4H+, then d ≤ 2[n/6] + 2, except when n ≡ 5 (mod 6)), when d ≤ 2[n/6] + 3. If n is a

multiple of 6, then any code meeting the bound is even.

We will call a code extremal if it meets the strongest of the applicable bounds from Theo-

rems 28, 31, and 33. For Type II binary codes, ternary codes, and linear codes over GF (4) this

agrees with the historical usage. For Type I binary codes, however, “extremal” has generally

been used to mean a code meeting the much weaker bound of Theorem 28; in the light of

Theorem 31, it seems appropriate to change the deﬁnition.

Concerning codes over Z4, Bonnecaze, Sol´e, Bachoc and Mourrain [27] show:

Theorem 34. Suppose C is a Type II self-dual code over Z4 of length n. Then the minimal

Euclidean norm of C is at most
 8 [ n
24
 ] + 8 . (165)

The proof uses C to deﬁne an even unimodular n-dimensional lattice Λ(C) = { 1
2 u ∈ Rn :

u (mod 4) ∈ C}, and examines its theta series.

As usual, one can derive an analogue for Type I codes:

Theorem 35. [256] Suppose C is a Type I self-dual code over Z4 of length n. The minimal

Euclidean norm of C is at most
 8 [ n
24
 ] + 8 , (166)

except when n ≡ 23 (mod 24), in which case the bound is

8 [ n
24
 ] + 12 . (167)

If equality holds in (167) then C is a shortened version of a Type II code of length n + 1.

75

We say that codes meeting either of these bounds are norm-extremal. For Type II codes

this agrees with the deﬁnition given in [27].

There should be an analogous concept of Lee-extremal, but at present we do not know what

this is. Of course, the bounds (166) and (167) also apply to Lee weight. But this is not a

satisfactory bound, since it is not even tight at length 24, where the highest attainable Lee

weight is 12 rather than 16 (see Table XVI).

The fact that, from Theorem 31, an extremal binary code of length a multiple of 24 must

be doubly-even suggests that these codes are likely to be particularly nice. Indeed, we have the

following result, which is a consequence of the Assmus-Mattson theorem (see [190, Chap. 6],

Theorem 11.14 of Chapter 1, Section 5 of Chapter xx (Tonchev)).

Theorem 36. Let C be an extremal binary code of length 24m. Then the codewords of C of

any given weight form a 5-design.

Similarly, the supports of the minimal codewords of an extremal ternary code of length

12m form a 5-design. For codewords of larger weight, the natural incidence structure is almost

a 5-design, except that it may have repeated blocks. Similarly, for an extremal additive code

over F4 of length 6m, the supports with multiplicities of the codewords of any ﬁxed weight form

a 5-design with repeated blocks. Harada [125] has shown that the Z4-lift of the Golay code g24

also yields 5-designs. More generally, one can show that the words of any ﬁxed symmetrized

type, in any of the 13 Lee-optimal self-dual codes of length 24 over Z4, form a colored 5-design,

possibly with repeated blocks [25]. See also [217].

10. Lower bounds

There are two ways to obtain lower bounds on the optimum minimal distance of a code

of length n. The ﬁrst way, naturally, is simply to construct a good code. Just as for general

linear codes, there is also a nonconstructive lower bound, analogous to the Gilbert-Varshamov

bound (cf. Theorems 3.1, 3.4, 3.5 of Chapter 1).

We ﬁrst consider the case of self-dual binary codes (family 2).

Theorem 37. [299], [191] Let n be any positive even integer. Let dGV be the largest integer

such that ∑

0<i<d
2|i
 (n
i
 )
 < 2
n/2−1 + 1. (168)

76

Then there exists a self-dual binary code of length n and minimal distance at least dGV .

Proof If we can show that the expected number of nonzero vectors of weight less than dGV

in a random self-dual code of length n is less than 1, it will immediately follow that there exists

some self-dual code of length n with no such vectors.

Let us therefore compute the average weight enumerator of the set of self-dual codes.

Consider the group G of binary matrices that preserve the quadratic form I. On the vector

space of even weight vectors, modulo the all 1’s vector, the quadratic form becomes symplectic,

and the group acts as the full symplectic group. In particular, it is therefore transitive on

nonzero vectors of even weight, modulo 1n. It follows that the expected number of vectors of

weight 2i in a random code must be proportional to ( n
2i
)
, except for i = 0 or i = n/2. Thus

the average weight enumerator has the form:

W (x, y) = ax
n + b ∑

1≤i≤n/2−1
 ( n
2i
)
x
n−2iy2i + cyn

= ax
n + cyn + b( 1
2 (x + y)
n + 1
2 (x − y)
n − x
n − yn).

Since every self-dual binary code contains the 0 vector and the all 1’s vector, W (1, 0) =

W (0, 1) = 1; since every self-dual code contains a total of 2n/2 vectors, W (1, 1) = 2n/2.

Solving for a, b, and c, we ﬁnd:

W (x, y) = xn + yn + 1
2n/2−1 + 1
 ∑

1≤i≤n/2−1
 ( n
2i
)
x
n−2iy2i .

Thus the average number of nonzero vectors of weight less than d is

1
2n/2−1 + 1
 ∑

0<i<d
2|i
 (n
i
 )

.

Corollary 2. [299], [191] There exists an inﬁnite sequence of self-dual [ni, ni/2, di] binary

codes, such that ni tends to inﬁnity, and

lim inf
i→∞ di
ni ≥ δ,

where δ ∼ .11002786 is the unique solution less than 1
2 of

H2(δ) = −δ log2(δ) − (1 − δ) log2(1 − δ) = 1
2 .

77

Proof. Take the logarithm of both sides of (168), divide by n, and let n tend to inﬁnity. The

resulting inequality is
 H2(δ) ≤ 1
2 ,

as desired.

Similar results hold if one restricts ones attention to codes of Type II:

Theorem 38. [299], [191] Let n be any positive multiple of 8. Let dGV be the largest integer

such that ∑

0<i<d
4|i
 (n
i
 )
 < 2
n/2−2 + 1 (169)

Then there exists a doubly-even self-dual binary code of length n and minimal distance at least

dGV .

Proof. Again we compute the average weight enumerator. The key observation is that the

function 1
2 wt(v) induces a quadratic form on the space of even weight vectors modulo the all

1’s vector. The group of matrices that preserve this quadratic form is transitive on the kernel

of this quadratic form; that is, vectors of weight divisible by 4, modulo 1n. This allows us to

write down the average weight enumerator:

W II (x, y) = x
n + yn + 1
2n/2−2 + 1
 ∑

0<i<n/4
 ( n
4i
)
xn−4iy4i.

Asymptotically, this agrees with Corollary 2 (as well as the Gilbert-Varshamov bound).

For ﬁnite n, it is actually (slightly) stronger! That is, the constraint that the code be Type II

makes it easier to ﬁnd good codes.

Similar arguments prove:

Theorem 39. In each family from the list 2I, 2II, 3, 4H, 4E, 4
H+
I , 4
H+
II , qH and qE there exists

a sequence of self-dual codes with length tending to inﬁnity satisfying

lim inf
i→∞ di
ni ≥ δ,

where
 Hq(δ) = δ logq(q − 1) − δ logq(δ) − (1 − δ) logq(1 − δ) = 1
2 .

The result for families qH and qE was ﬁrst given by Pless and Pierce [240].

Similar results hold for self-dual codes over Z4:

78

Theorem 40. There exists a family of Type II self-dual codes over Z4, with length tending to

inﬁnity, such that
 lim inf
i→∞ li
2ni ≥ δ,

where li is the minimal Lee weight of the ith code and δ = H −1
2 (1/2), as before.

Theorem 41. There exists a family of Type II self-dual codes over Z4, with length tending to

inﬁnity, such that
 lim inf
i→∞ Ni
ni ≥ .34737283 . . . ,

where Ni is the minimal Euclidean norm of the ith code.

11. Enumeration of self-dual codes

11.1. Gluing theory

Gluing is a technique for building up self-dual codes from smaller codes, and is especially

useful when one is attempting to classify all self-dual codes of a given length. Typically one

ﬁnds that there are many codes with low minimal distance and only a few with high minimal

distance. Gluing theory is good at ﬁnding all the codes of low distance.

The ﬁrst formal description of gluing theory appeared in [62]. It has also been used in [64],

[70], [71], [180], [181], etc.

The theory applies to codes from any of the families that we have discussed in this chapter.

Let C1, . . . , Ct be self-orthogonal codes of lengths n1, . . . , nt with generator matrices G1, . . . , Gt.

If C is a self-dual code with the generator matrix shown in Fig. 1 then we say that C is formed

by gluing the components C1, . . . , Ct together, and we write

C = (C1C2 . . . Ct)
+ (170)

to indicate this process. (Whenever possible the subcodes are chosen so that every minimal

weight codeword of C belongs to one of the Ci.) The codewords in C which contain a nonzero

linear combination of the rows of the matrix X are called glue words, since these hold the

components together. A glue word has the form

u = u1u2 . . . ut , (171)

where each glue element ui has length ni. Since C is self-dual, ui is in C ⊥
i .

79

X
 0

0 Gt

G2

G1

Figure 1: Generator matrix G for a code formed by gluing components C1, . . . , Ct together.
Gi is a generator matrix for Ci, and X denotes the rest of the generator matrix for C.

Let us choose coset representatives a0 = 0, a1, . . . , as−1 for Ci in C ⊥
i , where s = |C ⊥
i |/|Ci|,

so that
 C ⊥
i =
 s−1⋃

j=0
(aj + Ci) .

Then we can assume that each ui in (171) is one of a0, . . . , as−1.

As illustrations we give the two indecomposable binary Type I self-dual codes of length 18

(see Tables II and VI), using the components from the list in Section 11.3. The ﬁrst code is

formed by gluing three copies of the component d6 together:

1111
1111 1111
1111 1111
1111
010101 000011 010110
010110 010101 000011
000011 000011 000011
 (172)

The three glue vectors shown are abc, cab and bbb.

The second code is formed by gluing together d10, e7 and a “free” (or empty) component

80

f1: 1111
1111
1111
1111 1110100
0111010
0011101
0101010101 0000000 1
0101010110 1111111 0
 (173)

The two glue vectors shown are a0A and cd0.

Of course a self-dual code has no (nonzero) glue. If a self-orthogonal code C has a com-

ponent B, say, which is self-dual, then C is a direct sum C = B ⊕ C ′, where C ′ is again

self-orthogonal.

It may happen that there is a glue word in which only one ui is nonzero, in which case we

say that the component Ci has self-glue, and that u is a self-glue vector. So if C has a single

component C1 (say) with self-glue, we write C = C +
1 (compare (170)).

A basic result of gluing theory is the following.

Theorem 42. If a self-dual code C is formed by gluing together two codes C1 and C2 in such

a way that there is no self-glue, then the quotient groups C ⊥
1 /C1 and C ⊥
2 /C2 are isomorphic.

We omit the easy proof. The isomorphism is given by u1 + C1 → u2 + C2 whenever there

is a glue vector u1u2.

11.2. Automorphism groups of glued codes

One advantage of the gluing method is that it makes it much easier to ﬁnd the automor-

phism group of a self-dual code C. We will denote the group by G(C) rather than Aut(C) in

this section. It is essential that every automorphism of C takes the set of component codes

C1, . . . , Ct to itself. We will always choose the components so that this is true.

This being the case, any automorphism in G(C) will eﬀect some permutation of the Ci, so

that G(C) will have a normal subgroup G01 consisting of just those elements for which this

permutation is trivial. The group of permutations of the components that are realized in this

way we call G2(C) — it is isomorphic to the quotient group G(C)/G01.

Let G0(C) be the normal subgroup of G01 consisting of those automorphisms which, for

every i, send each glue element ui into a vector in the same coset ui + Ci, i.e. which ﬁx the

glue elements modulo the components. Then G01/G0(C) is isomorphic to a group acting on

81

Table I: Numbers of self-dual codes of length n. (a) Indecomposable Type II, (b) total Type
II, (c) indecomposable self-dual, (d) total self-dual.

n 0 2 4 6 8 10 12 14 16
a 1 − − − 1 − − − 1
b 1 − − − 1 − − − 2
c 1 1 0 0 1 0 1 1 2
d 1 1 1 1 2 2 3 4 7

n 18 20 22 24 26 28 30 32
a − − − 7 − − − 74
b − − − 9 − − − 85
c 2 6 8 26 45 148 457
d 9 16 25 55 103 261 731

the glue elements of each component: we call this group G1(C). Thus the full group G(C) is

compounded of the groups G0(C), G1(C) and G2(C), and has order

|G(C)| = |G0(C)||G1(C)||G2(C)| . (174)

Also G0(C) is the direct product of the groups G0(Ci). But in general G1(C) is only a subgroup

of the direct product of the G1(Ci), and therefore must be computed directly for each C.

11.3. Family 2: Enumeration of binary self-dual codes

The enumeration of binary self-dual codes of length n ≤ 32 has been carried out in a series

of papers: Pless [229] for n ≤ 20; Conway (unpublished) for Type II of length 24; Pless and

Sloane [242] for n = 22, 24; Conway and Pless [62] for n = 26 to 30 and Type II of length 32

(see also Pless [232]). Some errors in the last two references were corrected in Conway, Pless

and Sloane [65]. The results are summarized in Table I.

In this section we describe these codes, drawing heavily from the tables in [65].

Since (from (4)) there are at least 17493 inequivalent Type II codes of length 40, length 32

is probably a good place to stop.

Although the Type I codes of length 32 have not been classiﬁed, it is shown in [69] that

there are precisely three inequivalent [32, 16, 8] extremal Type I codes.

The following self-orthogonal codes will be used as components.

d4 : [1111], glue: a = 0011, b = 0101, c = 0110, |G0| = 4, G1 = S(3) on {a, b, c}, |G1| = 6.

d2n(n ≥ 3):
 [111100 . . . , 00111100 . . . , . . . , . . . 001111] , (175)

82

glue: a = 0101 . . . 01, b = 0000 . . . 11, c = 0101 . . . 10, |G0| = 2n−1n!, |G1| = 2 (swap a and c)

e7 : [(1110100)], glue: a = 1111111, G0 = L3(2), |G0| = 168, |G1| = 1.

e8 is the [8, 4, 4] Hamming code, see Section 3.2.

fn : If some coordinate positions contain very few codewords, it is often best to regard

these places as containing the free (or empty) component fn = {0n}. In this case we label

the coordinate positions by A, B, C, . . ., and use ABD for example to denote the glue word

110100 . . . . Also |G0| = 1.

The above components are important in view of the following decomposition theorem for

binary codes with low minimal distance.

Theorem 43. (a) If a self-orthogonal code C has minimal distance 2 then C = ik
2 ⊕ C ′, where

C ′ has minimal distance at least 4. (b) If a self-orthogonal code C is generated by words of

weight 4 then C is a direct sum of copies of the codes d2m (m ≥ 2), e7 and e8.

Proof. (a) Suppose C contains a word of weight 2, say u = 1100 . . . . Then any other word

v ∈ C must meet u evenly, so begins 00 . . . or 11 . . . . Hence C = B ⊕ C ′ where B = [11]. (b) A

set of mutually self-orthogonal words of weight 4 whose supports are linked is easily seen to

be either a d2m for some m ≥ 2, or an e7 or e8.

Remarks. (1) Suppose C is a self-dual code with minimal distance 4, and let C ′ be the

subcode generated by words of weight 4. Then C ′ is as described in part (b) of the theorem,

and C can be regarded as being obtained by gluing C ′ to some other subcode C ′′ (the latter

may be the free component fn).

(2) Generalizing Part (a) of the theorem, it is easy to show that any self-orthogonal code

over a ﬁeld Fq with length n > 2 and minimal distance 2 is decomposable ([64], Theorem 3).

The following are some additional components that will be used in Table II.

The code g24−m (m = 0, 2, 3, 4, 6, 8) is obtained by taking the words of the Golay code

g24 that vanish on m digits (and then deleting those digits). For the [16,5,8] ﬁrst-order Reed-

Muller code g16 the 8 digits must be a special octad, while for g18 they must be an umbral

hexad (see [70] for terminology). For 0 ≤ m ≤ 6, g24−m is a [24 − m, 12 − m, 8] code.

The [24,11,8] half-Golay code h24 consists of the Golay codewords that intersect a given

tetrad evenly.

The odd Golay code h
+
24 is the [24, 12, 6] Type I code generated by h24 and an appropriate

83

vector of weight 6. Alternatively, the odd Golay code may be obtained as follows. Let v ∈ F 24
2

be a ﬁxed vector of weight 4, say v = 14024. Then h
+
24 = {u ∈ g24 : wt(u ∩ v) even} ⋃{u + v :

u ∈ g24, wt(u ∩ v) odd}, with generator matrix

1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
1 1 1 1 0 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0
1 1 1 1 0 0 0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0
1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 0 0 0 0
1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1
1 1 0 0 0 0 0 0 0 0 0 0 1 1 0 0 1 0 1 0 1 0 1 0
0 0 0 0 1 1 0 0 0 0 0 0 1 0 1 0 1 1 0 0 1 0 1 0
0 0 0 0 0 0 0 0 1 1 0 0 1 0 1 0 1 0 1 0 1 1 0 0
1 0 1 0 0 0 0 0 0 0 0 0 1 0 1 0 1 0 0 1 1 0 0 1
0 0 0 0 1 0 1 0 0 0 0 0 1 0 0 1 1 0 1 0 1 0 0 1
0 0 0 0 0 0 0 0 1 0 1 0 1 0 0 1 1 0 0 1 1 0 1 0
1 0 0 0 1 0 0 0 1 0 0 0 1 0 0 0 1 0 0 0 1 0 0 0

This code has weight enumerator x24+64x18y6+375x16y8+960x14y10+1296x12y12+960x10y14+

375x8y16 + 64x8y18 + y24, and Aut(h
+
24) is the “sextet group” 26:3.S(6), of order 210.33.5 =

138240 ([242], [70, p. 309]).

The ﬁrst 11 rows of the above matrix generate h24; if the last row is replaced by

0 1 1 1 1 0 0 0 1 0 0 0 1 0 0 0 1 0 0 0 1 0 0 0

we get the Golay code g24 itself; and if the last row is replaced by

1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

we get (d6
4)+.

Under the action of Aut(g24) there are two distinct ways to select tetrads t = {c, d, e, f },

u = {a, b, e, f }, v = {a, b, c, d} so that t + u + v = 0, depending on whether {a, b, . . . , f }

is a special hexad or an umbral hexad (see Fig. 2). Correspondingly there are two [24,10,8]

quarter-Golay codes q+
24, q−
24, consisting of the codewords of g24 that intersect all of t, u, v evenly.

We refer to [62] and [65] for a description of the glue vectors for these codes.

Our ﬁrst table (Table II) lists all indecomposable binary self-dual codes of length n ≤ 22,

together with the indecomposable Type II codes of length 24, using the + notation of (170).

For these codes (and for most of those in the following tables) there is only one way to glue

the speciﬁed components together without introducing additional minimal-weight words. We

have therefore omitted the glue words from the table. (However, more information about these

codes, including the glue words, will be given in Table VI.)

84

Figure 2: Two choices for a hexad (special or umbral), used to deﬁne the two [24, 10, 8] quarter-
Golay codes q+
24 and q−
24.
 a b
c d
e f
 a b c d e f

Table II: Indecomposable binary self-dual codes of length n ≤ 24 (§ indicates a Type II code.
For length 24 only Type II codes are listed).

Length n Components
2 i2
8 e
§
8
12 d
+
12
14 e
2+
7
16 d
§
16, d
2+
8
18 (d10e7f1)+, d
3+
6
20 d
+
20, (d12d8)+, (d2
8d4)+, (e2
7d6)+, (d3
6f2)+, d
5+
4
22 g+
22, (d14e7f1)+, (d2
10f2)+, (d10d2
6)+, (d8e7d6f1)+,
(d8d2
6f2)+, (d2
6d2
4f2)+, (d4
4f 2
3 )+

24§ g24, d
+
24, d
2+
12 , (d10e2
7)+, d
3+
8 , d
4+
6 , d
6+
4

The next table (Tables III and IV) gives the full list of all 85 (decomposable or indecom-

posable) Type II codes of length 32. This table is taken from [65], and is a corrected version

of the table in [62]. The codes are labeled from C1 to C85 in the ﬁrst column (using the same

order as in [62] and [65]). The second column gives the components (omitting the superscripts

“+” to save space).

The third and fourth columns give the orders of the groups G1(C) and G2(C), and the

ﬁfth column gives the order of the full group, using (174), where |G0(C)| is the product of the

orders of the G0(Ci) for the components. The latter are given in Table V. The next column

gives A4, the number of codewords of weight 4. The weight enumerator of the code is then

(from Theorem 13)

(x8 + 14x
4y4 + y8)
4 − (56 − A4)x
4y4(x4 − y4)
4(x8 + 14x
4y4 + y8) .

The last four columns give the number of self-dual codes (the “children”, cf. Chapter xx

(Pless)) of lengths 30, 28, 26, 24 that arise from the code.

To save space, we have omitted the glue vectors from Tables III and IV. In many cases

85

they are uniquely determined by the components, and in any case they can be found in full in

[62], with corrections in [65].

The enumeration in Tables III and IV has been subjected to many checks, including the

veriﬁcation of the mass formula

∑ 1
|Aut(C)| = 391266122896364123
532283035423762022400

(in agreement with (4)).

Remark. There are just ﬁve Type II codes of length 32 with minimal distance 8: the

quadratic residue code C81 = q32, generated by

(1001000110110111100010101110000)1 ;

the second-order Reed-Muller code C82 = r32, generated by

(1110010000010000001100000000000)1 ;

and the three codes C83 = g2+
16 , C84 = f 8+
4 and C85 = f 16+
2 . Explicit generator matrices for

the last three are shown in Fig. 3.

Subtraction. Suppose for concreteness that C is a Type I code of length 26 with doubly

even subcode C0. Then we obtain a Type II code B (say) of length 32 by gluing C0 to d6, as

follows. Write C ⊥
0 = C0 ∪ C1 ∪ C2 ∪ C3, as in Section 5, where C = C0 ∪ C2, the shadow of C

is C1 ∪ C3, and Ci = ui + C0 for i = 1, 2, 3. Then B is generated by

C0 d6
u1 a
u2 b
u3 c
 (176)

This is a special case of the following construction. Let C, D be any strictly Type I codes,

of lengths n1 and n2, respectively, with C ⊥
0 = ∪3
i=0Ci, D⊥
0 = ∪3
i=0Di. Then B = ∪3
i=0Ci × Di

is self-dual if n1 + n2 ≡ 0 (mod 4), and is Type II if n1 + n2 ≡ 0 (mod 8). The weight

enumerator of B is then 3∑

i=0 WCi(x, y)WDi(x, y) .

Several constructions in the literature ([35], Theorems 1 and 2; [83], Theorem 3.1, for example)

are special cases of this construction. In (176) we have D = i3
2.

86

In this way any Type I code of length 26 leads to a unique (up to equivalence) Type II

code of length 32.

Conversely, all Type I codes of length 26 can be obtained by choosing a d6 inside a Type

II code of length 32 and inverting the above process.

More generally, suppose B is a Type II code of length n. We choose a copy of D = im
2 so

that D0 = d2m ⊂ B. Then we obtain a Type I code of length n − 2m by taking the vectors

v such that vw ∈ B for some w ∈ D. We call this process subtraction. Every Type I code

of length n − 2m can be obtained in this way by starting with a unique Type II code and

subtracting an appropriate d2m. Of course any Type II code of length n − 2m is a direct

summand of some Type II code of any greater length.

Table VI shows all (decomposable or indecomposable) codes of lengths n ≤ 22 with minimal

distance d ≥ 4, as obtained by subtracting suitable codes d2m from one of the codes in Tables III

and IV. The second column indicates the parent code in Tables III and IV and the d2m to be

subtracted. The next two columns gives the components, with a § to indicate a Type II code,

and the name (if any) given to this code in [229] or [242]. The remaining columns give the

orders of the glue groups G1 and G2, the weight distribution, and generators for the glue.

Table VII gives the self-dual codes (both Type I and Type II) of length 24 and minimal

distance d ≥ 4.

A complete list of all Type I or Type II self-dual codes of lengths n ≤ 24 can be obtained

by forming direct sums of the codes in Tables VI and VII in all possible ways with the codes

im
2 (m = 0, 1, . . .).

There are over 1000 self-dual codes of lengths 26–30 (see Table I, [62], [65]). The highest

minimal distance is 6, and there are respectively 1, 3 and 13 codes with d = 6 of lengths 26,

28 and 30.

11.4. Family 3: Enumeration of ternary self-dual codes

Ternary self-dual codes of lengths n ≤ 20 (and the maximal self-orthogonal codes of lengths

n ≤ 19, n ̸≡ 0 (mod 4) have been enumerated by Pless [227] and Mallows, Pless and Sloane

[194] for n ≤ 12, Conway, Pless and Sloane [64] for n ≤ 16, and Pless, Sloane and Ward [243]

for n ≤ 20. Leon, Pless and Sloane [180] give a partial enumeration of the self-dual codes of

length 24, making use of the complete list of Hadamard matrices of order 24, and show that

there are precisely two codes with minimal distance 9 (cf. Table XII below).

87

We will make use of the following components.

e3: [111], glue: ±a, a = 120. If the coordinates are labeled 1, 2, 3 then G0 is generated by

(1, 2, 3) and (1, 2) diag{−1, −1, −1} and has order 6; |G1| = 2.

t4 is the [4, 2, 3]3 tetracode, and g12 is the [12, 6, 6]3 ternary Golay code, see Section 3.2.

g10 is the [10, 4, 6]3 code consisting of the vectors u such that 00u ∈ g12. If x and y are

chosen so that 11x ∈ g12, 12y ∈ g12, then the glue words for g10 can be taken to be ±x, ±y,

±x ± y. |G0| = 360, |G1| = 8.

p13: Let Q0, Q1, . . . , Q12 be the points of a projective plane of order 3, labeled so that the

13 lines are represented by the cyclic shifts t0, t1, . . . , t12 of the vector t0 given by

Q0 Q1 Q2 Q3 Q4 Q5 Q6 Q7 Q8 Q9 Q10 Q11 Q12
1 1 0 1 0 0 0 0 0 1 0 0 0

([190], p. 695, [67]). The vectors t0, . . . , t12 generate a [13, 7, 4]3 code p⊥
13. The dual is p13, a

[13, 6, 6]3 self-orthogonal code consisting of the vectors ∑12
i=0 aiti with ai ∈ F3 and ∑ ai = 0,

and having weight distribution A0 = 1, A6 = 156, A9 = 494, A12 = 78. G0(p13) ≃ P GL3(3),

of order 5616, |G1(p13)| = 2. The glue words are ±t0.

The indecomposable self-dual codes of lengths n ≤ 16 are shown in Table VIII. H8 denotes

a suitably normalized version of the Hadamard matrix of order 8.

The analogue of Theorem 43 is: any self-orthogonal ternary code generated by words of

weight 3 is a direct sum of copies of e3 and t4. A technique for classifying self-orthogonal codes

generated by words of weight 6 (using “center sets”) is given in [243].

11.5. Family 4H: Enumeration of Hermitian self-dual codes over F4

These have been classiﬁed for lengths n ≤ 16 [64] — see Table IX.

We will make use of the following components.

d2n (n ≥ 2): generated by (175). There are 16 cosets of d2n in d⊥
2n, and as glue words we

choose 0, ωνa, ωνb, ωνc, ωνd, ων e, ν ∈ {0, 1, 2}, where

a = 1010 . . . 1010

b = 0000 . . . 0011

c = 1010 . . . 1001

d = 1010 . . . 10ωω

e = 1010 . . . 10ωω

88

Also |G0| = 2n−1n!, |G1| = 36 (n = 2), or 12 (n ≥ 3).

e5 : [ωωωω0, 0ωωωω], glue: ων1, ν ∈ {0, 1, 2}, G0 = A(5), of order 60, |G1| = 6.

h6 is the hexacode, e7 ⊗ F4, e8 ⊗ F4 are F4-versions of the Hamming codes in Sections 3.2,

and 1n is the [n, 1, n]4 repetition code.

Remarks. (1) The group orders diﬀer slightly form those in [64], since now we are allowing

conjugation in the group.

(2) The dots and double-dots in the glue column indicate multiplication by ω or ω2, re-

spectively.

(3) The unique distance 6 code at length 14, q14, is the [14, 7, 6]4 extended quadratic residue

code generated by
 1(1ωωωωωωωωωωωω) .

(4) The analogue of Theorem 43 is: (a) any self-orthogonal code with minimal distance 2

has i2 as a direct summand; (b) any self-orthogonal code generated by words of weight 4 is a

direct sum of copies of d4, d6, d8, . . ., e5, h6, e7 and e8.

11.6. Family 4E: Enumeration of Euclidean self-dual codes over F4

Although even codes of length up to 14 were classiﬁed in [189], the odd codes do not seem

to have been classiﬁed.

11.7. Family 4H+: Enumeration of trace self-dual additive codes over F4

These have been classiﬁed up to length 7 (and Type II code up to length 8) in [49], [134].

The analogue of Theorem 43 is the following. Let dn be the code of length n generated by

all even-weight binary vectors (n ≥ 2), and let i2 = [11, ωω]. Then any trace self-orthogonal

additive code over F4 generated by words of weight 2 is a direct sum of copies of i2, d2, d3,

d4, . . ..

d+
n (mentioned in Table XIV) is the code of length n, containing 2n words, generated by

dn and ωω . . . ω.

11.8. Family 4Z: Enumeration of self-dual codes over Z4

These have been classiﬁed for lengths up to 16 in the following papers: Conway and Sloane

[71] for n ≤ 9, Fields, Gaborit, Leon and Pless [95] for n ≤ 15, and Pless, Leon and Fields

[239] for Type II codes of length 16.
 89

In this section we will present enough component codes to state the analogue of Theorem 43.

The smallest self-dual code is i1 = {0, 2}. If a self-orthogonal code C contains a vector of

the form 210n−1 then C = i1 ⊕ C ′ is decomposable. The next-simplest possible vectors are

“tetrads”, of type ±140n−4. We list a number of self-orthogonal codes that are generated by

tetrads; t denotes the total number of tetrads in the code.

The ﬁrst four codes have the property that the associated binary code C (1) is the self-dual

code d2m of (175).

D2m (m ≥ 2) is generated by the tetrads 11130 . . . 0, 0011130 . . . 0, . . . , 0 . . . 01113; |D2m| =

4m−1, |Aut(D2m)| = 2.4! (m = 2) or 22.2m (m > 2), t = 2(m − 1). D⊥
2m/D2m is a group of

type 42 with generators v1 = 0101 . . . 01, v2 = 00 . . . 0011.

DO
2m (m ≥ 2) is generated by D2m and the tetrad 1300 . . . 0011 (or equivalently the vector

2020 . . . 20); |DO
2m| = 4m−12, |Aut(DO
2m)| = 22.8 (m = 2) or 2.2m−1.2m (m > 2), t = 2m.

(DO
2m)⊥/DO
2m is a cyclic group of order 4 generated by v1 (if m is odd), or a 4-group generated

by v1 and 2v2 (if m is even).

D+
2m (m ≥ 2, but note that D+
4 ≃ DO
4 ) is generated by D2m and 2v2; |D+
2m| = 4m−12,

|Aut(D+
2m)| = 2m.2m+1, t = 4(m − 1). (D+
2m)⊥/D+
2m is a 4-group generated by 2v1 and v2.

D⊕
2m (m ≥ 2) is the self-dual code generated by DO
2m and D+
2m; |D⊕
2m| = 4m−122, |Aut(D⊕
2m)| =

23.4! (m = 2) or 2m.2m.2m (m > 2), t = 4m. For use in (158) we note that there are two

permutation-inequivalent versions of D⊕
4 , with generator matrices

(a)
 

 1 1 1 1
0 2 0 2
0 0 2 2
 

 , (b)
 

 1 3 3 3
0 2 0 2
0 0 2 2
 

 . (177)

D⊕
4 (in either version) has swe = x4 + 6x2z2 + z4 + 8y4.

E7 is generated by 1003110, 1010031, 1101003; |E7| = 43, |Aut(E7)| = 2.4!, t = 8. E ⊥
7 /E7 is

a cyclic group of order 4 generated by 3111111.

E +
7 is the self-dual code generated by E7 and 2222222 (or equivalently by all cyclic shifts of

3110100); |E +
7 | = 432, |Aut(E +
7 )| = 2.168, t = 14, swe = x7 + z7 + 14y4(x3 + z3) +7x3z3(x +

z) + 42xy4z(x + z). For both E7 and E +
7 the associated binary code C (1) is the Hamming code

e7.
 E8 is the self-dual code generated by 0u, u ∈ E7 and 30001011. An equivalent generator

matrix has already been given in (40). |E8| = 44, g = 8.2.4! = 384, t = 16, swe = x8 + 16y8 +

z8 + 16y4(x4 + z4) + 14x4z4+ 48xy4z(x2 + z2) +96x2y4z2.

90

Theorem 44. Any self-orthogonal code over Z4 generated by vectors of the form ±140n−4 is

equivalent to a direct sum of copies of the codes

D2m, DO
2m, D+
2m, D⊕
2m(m = 1, 2, . . .), E7, E +
7 , E8 .

The (somewhat complicated) inclusions between the codes mentioned in the theorem can

be seen in Fig. 1 of [71].

12. Extremal and optimal self-dual codes

Recall from Section 9 that we have deﬁned a self-dual code from any of the families 2 through

qE to be extremal if it meets the strongest of the applicable bounds from Theorems 28, 31 and

33, that is, if its minimal distance d is equal to

(2I) 4 [ n
24 ] + 4 + ǫ, where ǫ = −2 if n = 2, 4 or 6, ǫ = 2 if n ≡ 22 (mod 24), and ǫ = 0

otherwise,

(2II) 4 [ n
24 ] + 4,

(3) 3 [ n
12 ] + 3,

(4H) 2 [ n
6 ] + 2,

(4E) [ n
2 ] + 1,

(4
H+
I ) 2 [ n
6 ] + 2 + ǫ′, where ǫ′ = −1 if n = 1, ǫ′ = 1 if n ≡ 5 (mod 6), and ǫ′ = 0 otherwise,

(4
H+
II ) 2 [ n
6 ] + 2,

(qH), (qE) [ n
2 ] + 1.

We also deﬁned a code over Z4 to be norm-extremal if its minimal norm is

(4
Z) 8 [ n
24 ] + 8 + ǫ′′

where ǫ′′ = 4 if n ≡ 23 (mod 4), ǫ′′ = 0 otherwise.

It is very likely (although we do not have a proof) that the above bounds for families 2

through qE are the highest minimal distance that is permitted by the pure linear programming

bound applied to the Hamming weight enumerator and (when relevant) the shadow enumerator.

In contrast, we call a code optimal if it has the highest minimal distance of any self-dual

code of that length. An extremal code is automatically optimal.

In this section we will summarize what is presently known about extremal and optimal

codes in the families we are considering. Earlier summaries of extremal codes and lattices have

appeared in Chapter 7 of [70], [147]. In the tables we have tried to list all known codes with

the speciﬁed minimal distance (a period indicating that the list is complete), or else to indicate

91

how many extremal codes are known. Whenever possible we have attempted to name at least

one extremal code.

12.1. Family 2: Binary codes

Type I codes meeting the d ≤ 2[n/8] + 2 bound of Theorem 28 (the old deﬁnition of

extremal) were completely classiﬁed by Ward [319] (ﬁnishing the work begun in [196], [229],

[242]): such codes exist if and only if n is 2 (i2), 4 (i2
2), 6 (i3
2), 8 (e8), 12 (d
+
12), 14 (e
2+
7 ), 22 (g+
22)

or 24 (g24) — compare Tables II and VI. In each case the code is unique.

However, there are many more Type I codes that are extremal in the new sense, and they

have not yet been fully classiﬁed. It is known (Theorem 29) that extremal Type II codes do

not exist for lengths ≥ 3952 and presumably a similar bound applies to extremal Type I codes.

Table X shows the highest possible minimal distance for binary self-dual codes of lengths

n ≤ 72. This is based on earlier tables in Fig. 19.2 of [190], [69] and [83]. In the table dI (resp.

dII ) denotes the highest minimal distance of any strictly Type I (resp. Type II) self-dual code.

Remarks on Table X

The fourth column of the table gives the known codes having the indicated minimal dis-

tance. As mentioned above, a period indicates that the lists of codes is complete. (The

enumeration for lengths n ≤ 32 has already been discussed in Section 11.3.) When n is a

multiple of 8 a semicolon separates the Type I and Type II codes.

In the years since the manuscript of [69] was ﬁrst circulated, a large number of sequels

have been written, supplying additional examples of self-dual codes in the range of Table X.

The bibliography includes all the manuscripts known to us, even though inevitably not all of

them will be published. It was not possible to mention all these references in the table, so

instead we list them here. This list also includes a number of older papers. Readers interested

in extremal self-dual codes, especially of Type I, in the range of the table should therefore

consult the following: [35], [38], [39], [40], [41], [42], [43], [81], [83], [84], [85], [86], [87], [107],

[108], [109], [110], [111], [113], [118], [120], [121], [122], [129], [126], [127], [130], [139], [151],

[152], [153], [157], [162], [219], [221], [234], [238], [247], [267], [268], [269], [305], [307], [309],

[310], [311], [312], [332], [333], [334], [335], [336], [337].

Note that if we don’t distinguish between Type I and Type II codes, but just ask what

is the highest minimal distance of a binary self-dual code, then the answer is known for all

92

n ≤ 60.

The symbol XQm in any of these tables indicates an extended quadratic residue code of

length m + 1. Both quadratic residue codes and double circulant codes provide many examples

of good self-dual codes (cf. Section 12 of Chapter 1, Chapter xx (Ward), Chapter yy (Pless),

[190, Chapter 16]). There are two basic types of binary double circulant codes, having generator

matrices of the form 1 0 1 1 1 1
1 1
1 1 R
1 1
1 1
 (178)

or 1 1 1 R
1 1
 , (179)

where R is a circulant matrix with ﬁrst row r (say). (178) is used only when the length is a

multiple of 4. Such codes and their generalizations to other ﬁelds have been studied by many

authors, including [12], [15], [108]–[118], [147], [153], [158], [186], [187], [190, Chap. 16], [248],

[267], [308], [317], [332]–[334]. Table XI, based on [69] and [204], gives a selection of double

circulant binary codes. Code H86 (from [83]) is the shortest Type I self-dual code presently

known with d = 16. The ﬁrst column gives the name of the codes, following [69], and the last

column gives r, the initial row of R, in hexadecimal. The codes marked (∗) are not necessarily

optimal. The minimal distance of the last two codes in the table was determined by Moore

[203], [204]. For these two codes r has 1’s at the squares modulo 43 and 67, respectively. Moore

remarked that the analogous code of length 168 might also have been extremal. However, Aaron

Gulliver (personal communication, Nov. 1997) has shown that the minimal distance of this

code is at most 28.

We see from Table X that there are extremal Type I codes (in the new sense) that are not

also Type II codes at lengths

2, 4, 6, 12, 14, 16, 18, 20, 22, 32, 36, 38, 40, 42, 44, 46, 60, 64, 66, 68

that such codes do not exist at length

8, 10, 24, 26, 28, 30, 34, 48, 50, 52, 54, 58 (180)

93

and that their existence at lengths
 56, 62, 70, 72 (181)

is at present an open question. The nonexistence of the Type I codes of lengths in (180) is

established by imposing the extra condition that the shadow enumerator must have integral

coeﬃcients.

Concerning extremal Type II codes, with d = 4[n/24] + 4, these exist for the following

values of n:
 8, 16, 24, 32, 40, 48, 56, 64, 80, 88, 104, 136

but their existence at lengths 72 and 96 and all greater lengths is open. For lengths 8, 24, 32,

48, 80 and 104 we can use extended quadratic residue codes, and for lengths 40, 56, 64, 88,

136 we can use double circulant codes (see Table XI).

Only one [48, 24, 12] code is presently known, XQ47, which is generated by 1 and

1(01111011110010101110010011011000101011000010000)

(with 1’s at the nonzero squares modulo 47). Huﬀman [139] has shown that any Type II

[48, 24, 12] code with a nontrivial automorphism of odd order is equivalent to XQ47. Houghten,

Lam and Thiel (cf. [136]) are attempting to establish by direct search that XQ47 is unique.

As Table X shows, if n ≥ 40 is congruent to 8 or 16 (mod 24) there are often large numbers

of extremal codes. It is easy to ﬁnd [72, 36, 12] Type II codes, for example XQ71; [83] shows

that there are at least 33 inequivalent codes with these parameters.

Concerning the existence of self-dual codes with a speciﬁed minimal distance, the following

results were established in [69]. Self-dual codes with minimal distance

d ≥ 6 exist precisely for n ≥ 22;

d ≥ 8 exist precisely for n = 24, 32, and n ≥ 36;

d ≥ 10 exist precisely for n ≥ 46;

d ≥ 12 exist7 for n = 48, 56, 60 and n ≥ 64; perhaps for n = 62; and do not exist for all

other values of n. (As pointed out in [69], the [58, 29, 12] self-dual code claimed in [15] is an

error.)

Dougherty, Gulliver and Harada [83], extending work in [69], show that codes with

7The existence of a [70, 35, 12] was not known when [69] was written, but such a code was later found by
Scharlau and Schomaker [276].
 94

d ≥ 14 exist for n ≥ 78; perhaps for n = 70, 72, 74, 76; and do not exist for all other values

of n;

d ≥ 16 exist for n = 80, 86, 88, 96, 100–104, 112 and n ≥ 120 (and possibly for other values

of n).

12.2. Family 3: Ternary codes

Table XII shows the highest possible minimal distance for ternary self-dual codes of lengths

n ≤ 72.

Remarks on Table XII

For the entries at lengths n ≤ 24, see the discussion in Section 11.4.

Extremal codes exist at lengths 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 56, 60 and 64.

Extremal codes do not exist at lengths 72, 96, 120 and all n ≥ 144, because then the extremal

Hamming weight enumerator contains a negative coeﬃcient. The existence of extremal codes

in the remaining cases (n = 52, 68, 76, . . ., 140) is undecided.

In Table XII, XQn denotes an extended quadratic residue code of length n + 1, and S(n)

denotes a Pless double circulant (or “symmetry”) code of length n (see Section 5 of Chapter

“coding-constructions”, [18], [19], [194], [228], [230]). A [28, 14, 9]3 code was discovered by

Cheng and R. Scharlau [58]. Another such code was given by Kschischang and Pasupathy

[174], namely the negacyclic code generated by the polynomial (x2 + x − 1)(x6 − x4 + x3 + x2 −

1)(x6 − x5 − x − 1), i.e. by the vectors

(2002021222020010000000000000)− ,

where the subscript − indicates that the code is negacyclic. Huﬀman [146] shows that there

are at least 14 inequivalent [28, 14, 9]3 codes with nontrivial automorphisms of odd order.

Ward [321] and Dawson [76] independently discovered that [40, 20, 12]3 codes can be con-

structed using generator matrices of the form [I20H20], where H20 is a Hadamard matrix of

order 20. There are three distinct Hadamard matrices of this order, and Dawson shows that all

three produce [40, 20, 12]3 codes. Harada [123] shows that these three codes are inequivalent.

Dawson also shows that the same construction using the Paley-Hadamard matrix of order 32

leads to a [64, 32, 18]3 self-dual code. A [64, 32, 18]3 code B24 (equivalent to Dawson’s) had

been constructed earlier by Beenker [12].
 95

The codes of length 32, 44, 52, 56 and 68 can be obtained by “subtracting” (see Section 11.3)

a copy of t4 from a code of length 4 greater.

Other constructions for ternary self-dual codes can be found in Harada [123] and Ozeki

[215].

12.3. Family 4H: Hermitian self-dual codes over F4

Table XIII shows the highest possible minimal distance for Hermitian self-dual codes over

F4 of lengths n ≤ 32.

Remarks on Table XIII

A period in the “Codes” column indicates that the list is complete.

For the entries at lengths n ≤ 16, see the discussion in Section 11.5.

Extremal codes exist at lengths 2, 4, 6, 8, 10, 14, 16, 18, 20, 22, 28 and 30. They do not

exist at lengths 12, 24, 102, 108, 114, 120, 122 and all n ≥ 126 (the larger n being eliminated

by the presence of negative coeﬃcients in the extremal Hamming weight enumerator). The

remaining lengths (26, 32, 34, . . .) are undecided.

The [18, 9, 8]4 code S18 generated by

1(1ωωωωωωωωωωωωωωωω)

has a number of interesting properties (see [189], [67], [59], [235]). It has automorphism group

3 × (P SL2(16).4), of order 48960 [59] and is the unique [18, 9, 8]4 code [148].

The long-standing question of the existence of a [24, 12, 10]4 code was settled in the negative

by Lam and Pless [176] (see also [141]). The code g24 ⊗ F4 is an example of a [24, 12, 8]4 code.

12.4. Family 4H+: Additive self-dual codes over F4

Table XIV, taken from [49], shows the highest possible minimal distance for additive codes

over F4 of lengths n ≤ 30 that are self-dual with respect to the trace inner product.

Remarks on Table XIV

A period in the “Codes” column indicates that the list is complete.

Extremal Type I codes exist at lengths 1–6, 8–12, 14–18, 20–22 and 28–30, and do not exist

at lengths 7, 13 and 25. Lengths 19, 23, 24, 26, 27 are undecided.

96

Many of the entries are copied from the table of Hermitian self-dual codes, Table XIII. The

codes d+
n are deﬁned in Section 11.7, h6 is the hexacode, and h5 is the [5, 2.5, 3]4+ shortened

hexacode, generated by (01ωω1), with weight enumerator x5 + 10x2y3 + 15xy4 + 6y5 and

|Aut(h5)| = 120. Also, c9, c15, c21, c23, c25 are cyclic codes with generators shown in Table XV.

If no name is given, the code can be obtained by shortening a code of length one greater.

12.5. Family 4Z: Self-dual codes over Z4

Table XVI gives the highest possible Hamming distance, Lee distance and Euclidean norm

for codes over Z4 of lengths n ≤ 24. This is based on [71], [88], [95], [149], [239] and [254]. The

columns headed # give the number of extremal codes.

Remarks on Table XVI

The length 16 code C16 is given in [239], where it is called 5 f5. It has |Aut(C16)| =

25+10325.7 and generator matrix






















 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 0 1 1 1 1 1 1 0 0 0 0 1 0 0 0
1 1 0 1 0 0 1 1 1 1 0 0 0 1 0 0
1 1 1 0 1 0 1 0 1 0 1 0 0 0 1 0
0 0 0 0 1 1 1 1 1 1 1 0 0 0 0 1
0 0 0 0 0 2 0 0 0 0 0 2 2 0 0 2
0 0 0 0 0 0 2 0 0 0 0 2 2 2 2 2
0 0 0 0 0 0 0 2 0 0 0 0 2 2 0 2
0 0 0 0 0 0 0 0 2 0 0 0 0 2 2 2
0 0 0 0 0 0 0 0 0 2 0 2 0 2 0 2
0 0 0 0 0 0 0 0 0 0 2 2 0 0 2 2
 






















The codes C17 and C18 mentioned in the table have generator matrices


















 1 0 0 0 0 0 0 0 1 2 1 1 1 1 1 1 2
0 1 0 0 0 0 0 0 1 1 0 0 0 1 2 2 0
0 0 1 0 0 0 0 0 1 3 2 0 0 2 3 2 2
0 0 0 1 0 0 0 0 1 3 0 0 0 2 0 3 0
0 0 0 0 1 0 0 0 0 1 3 3 3 3 1 1 2
0 0 0 0 0 1 0 0 0 0 0 3 1 0 2 0 3
0 0 0 0 0 0 1 0 0 0 3 2 1 0 0 0 3
0 0 0 0 0 0 0 1 0 0 1 3 2 0 0 0 3
0 0 0 0 0 0 0 0 2 2 2 2 2 0 0 0 0
 

















97

and 


















 1 0 0 3 0 0 0 0 0 3 2 0 3 0 2 0 0 0
0 1 0 0 3 0 0 0 0 0 3 2 2 3 0 0 0 0
0 0 1 0 0 3 0 0 0 2 0 3 0 2 3 0 0 0
0 0 0 1 0 0 3 0 0 0 0 0 3 2 0 3 0 2
0 0 0 0 1 0 0 3 0 0 0 0 0 3 2 2 3 0
0 0 0 0 0 1 0 0 3 0 0 0 2 0 3 0 2 3
0 0 0 0 0 0 1 3 0 0 3 3 0 3 3 3 2 1
0 0 0 0 0 0 0 1 3 3 0 3 3 0 3 1 3 2
0 0 0 0 0 0 0 0 2 0 2 2 0 2 2 0 2 0
0 0 0 0 0 0 0 0 0 2 2 2 2 2 2 2 2 2
 ,
 



















and automorphism groups of orders 576 and 144, respectively.

G24 was deﬁned in (41), and G19 through G23 are shortened versions of it.

Besides the norm-extremal codes of length 8, 12, 14–24 shown in the table, there are also

norm-extremal codes of lengths 32 and 48 obtained by lifting binary extended quadratic residue

codes to Z4. The code of length 32 has minimal Lee weight 14 and minimal norm 16. Pless

and Qian [241] have shown that the code of length 48 has minimal Lee weight 18 and minimal

norm 24.

Further examples of good self-dual codes over Z4 may be found in [22], [23], [27], [51], [88],

[102], [112], [115], [124], [149], [241], [244], [254].

13. Further topics

13.1. Decoding self-dual codes

The problem of decoding self-dual codes is an extremely important one for applications,

but we will not discuss it here. Decoding the binary Golay code, in particular, has been studied

in many papers — see [2], [66], [67], [70, Chapter 11], [233], [236], [259], [292], [315], [316]. See

also [258], [314], and Section 8 of Chapter “codes-and-groups”.

13.2. Applications to projective planes

There is a very nice application of self-dual codes to projective planes. If n is congruent to 2

(mod 4) then the incidence matrix of a projective plane of order n generates a self-orthogonal

code Cn, which when an overall parity-check is added becomes an [n2+n+2, 1
2 (n2+n+2), n+2]

Type II self-dual binary code (see [3], [192] or Chapter “assmus” for the proof).

It was a famous unsolved problem to decide if a projective plane of order 10 could exist.

The weight enumerator of C10 was initially studied in [192] (see also [197]). Finally, after

98

many years of work, Lam, Thiel and Swiercz [177] (see also [175]) succeeded in completing this

project and showed that C10 (and hence the putative plane of order 10) does not exist.

The possibility of the existence of a plane of order 18 (or 12, but then we do not obtain a

self-dual code) remains an open question.

13.3. Automorphism groups of self-dual codes

Various topics concerning the automorphism groups of self-dual codes are discussed in

chapter “codes-and-groups”, e.g. the full automorphism groups of extended quadratic residue

codes, the occurrence of self-dual codes with a trivial group (see [39], [69], [120], [180], [207],

[305]), and the existence of self-dual codes with any prescribed symmetry group ([207]).

13.4. Open problems

Do there exist [72, 36, 16] or [96, 48, 20] Type II self-dual binary codes? (Cf. [63], [94], [153],

[245], [282]).

Fill in the other gaps in Tables X, XII, XIII. No extremal Hermitian self-dual codes over

F4 of any length greater than 30 are presently known!

There is an interesting open question concerning self-dual codes of length 24. There exists

a unique [24, 12, 8] binary code, exactly two [24, 12, 9]3 ternary codes, and no [24, 12, 10]4

Hermitian or Euclidean self-dual code over F4 ([176]). But the possibility of an additive trace-

self-dual code of length 24 over F4 with minimal distance 10 remains open (see Table XIV).

From Theorem 33, if such a code exists then it must be even. However, all our attempts so far

to construct this code have failed, so it may not exist.

When is the ﬁrst time a Type I binary code has a higher minimal distance than the best

Type II code of the same length? (No such example is presently known.)

In this regard it is worth mentioning that there is a [32, 17, 8] binary code [60], which has

the same minimal distance as the best self-dual codes of length 32, yet contains twice as many

codewords. There are similar examples in the ternary case — see Chapter “Brouwer”.

The Nordstrom-Robinson code (see Chapter 1) is an example of a nonlinear code that has a

higher minimal distance than any self-dual (or even linear) code of the same length. However,

as mentioned in Section 3.2, the Nordstrom-Robinson code should really be regarded as a self-

dual linear code over Z4 (the octacode o8). When is the ﬁrst time a non-self-dual [n, n/2, d]

binary linear code has a higher minimal distance than any [n, n/2, d′] self-dual code? This

99

certainly happens at length 40, but may happen at length 36 or 38.

Is there any diﬀerence asymptotically, as n → ∞, between d/n for the best binary codes,

the best binary linear codes and the best binary self-dual codes?

Let Ωn denote the collection of binary self-dual codes that have the highest possible minimal

distance at length n, and let Ln, Un be respectively the smallest and largest orders of Aut(C),

C ∈ Ωn. When (if ever) is the ﬁrst time that Ln = Un = 1? Is there an inﬁnite sequence of

values of n with Un > 1? Show that Ln = 1 for all suﬃciently large n.

14. Self-dual codes and lattices

There are many connections and parallels between self-dual codes and lattice sphere pack-

ings. Our original intention was to end the chapter with an account of these connections, but

constraints of space and time have not permitted this. Instead, we give a brief list of some

of the parallels, to whet the reader’s appetite. For more information about the relationship

between the two ﬁelds, see [32], [33], [92], [97], [98], [103], [285], [287] and especially [70], [73].

Coding concept Lattice concept
Binary linear code Lattice
Dual code Dual lattice
Self-orthogonal code Integral lattice
Self-dual code Unimodular lattice
Doubly-even self-dual code Even unimodular lattice
Hamming code e8 Root lattice E8 ([70], p. 120)
Hexacode h6 Coxeter-Todd lattices K12 ([70], p. 127)
Binary Golay code g24 Leech lattice Λ24 ([70], p. 131)
Minimal distance Minimal norm
Number of minimal weight words Kissing number
Weight enumerator W (x, y) Theta series
MacWilliams identity (Eq. (33)) Jacobi identity ([70], p. 103)
(weight enumerator of dual code in terms (theta series of dual lattice in terms
of weight enumerator of code) of theta series of lattice)
Gleason’s theorem (Theorem 11) Hecke’s theorem ([70], p. 187)
(weight enumerator of doubly-even (theta series of even unimodular
code is polynomial in weight enumerators lattice is polynomial in theta series
of e8 and g24) of E8 and Λ24)

The similarity between the theorems of Gleason and Hecke is particularly striking, and we

will end the chapter by saying a little more about this. Suppose C is a binary code of length

n. Construction A produces an n-dimensional sphere packing Λ(C), consisting of the points

1√2 x for x ∈ Zn, x (mod 2) ∈ C. If C is linear, Λ(C) is a lattice; if C is self-dual, Λ(C) is

unimodular; and if C is Type II, Λ(C) is an even unimodular lattice.

100

If C is a linear code with weight enumerator WC(x, y), then WC(θ3(2z), θ2(2z)) is the theta

series of Λ(C), where
 θ3(z) =
 ∞∑

m=−∞ qm2, θ2(z) =
 ∞∑

m=−∞ q(m+1/2)2 ,

where q = eπiz, Im(z) > 0. This map gives an isomorphism between (a) the ring of weight

enumerators of Type I self-dual codes, C[φ2, θ8] (see Eq. 95), and the ring of theta series of

even-dimensional unimodular lattices, C[θ2
3, ∆8], where

∆8 = q
 ∞∏

m=1{(1 − q2m−1)(1 − q4m)}
8 ;

and (b) the ring of weight enumerators of Type II self-dual codes, C[φ8, φ′
24] (Theorem 13),

and the ring of theta series of even unimodular lattices, C[ΘE8, ∆24], where

ΘE8(z) = 1 + 240
 ∞∑

m=1 σ3(m)q2m ,

∆24 = q2 ∞∏

m=1
(1 − q2m)
24 ,

and σ3(m) is the sum of the cubes of the divisors of m. For further information see [70,

Chapter 7].

The bibliography also contains a number of references that are concerned with particular

constructions of lattices from self-dual codes, or of properties of lattices that are analogous to

properties of self-dual codes mentioned in this chapter: [8], [9], [22], [23], [26], [51], [55], [61],

[68], [72], [82], [112], [163], [168], [171], [174], [193], [209], [210], [212], [213], [214], [216], [256],

[270], [271], [272], [286].

Acknowledgements

Over the past 26 years NJAS has had the pleasure of collaborating with many of the people

whose names are listed in the bibliography: he wishes to express his appreciation to all of them.

We thank Eiichi Bannai, Dave Forney, Aaron Gulliver, Masaaki Harada, Cary Huﬀman, Michio

Ozeki, Vera Pless and Patrick Sol´e for helpful comments on the manuscript of this chapter.

We also thank Susan Pope for a superb typing job.

101

Table III: Doubly-even self-dual (or Type II) binary codes of length 32 (Part 1)

Code Components |G1| |G2| |G| A4 n30 n28 n26 n24
C1 d32 1 1 23036537211.13 120 2 2 1 1
C2 d24e8 1 1 22736527211 80 4 3 2 2
C3 d20d12 1 1 22636537 60 5 4 2 2
C4 d18e2
7 1 2 222365.73 50 5 3 2 1
C5 d2
16 1 2 229345272 56 3 2 1 1
C6 d16e2
8 1 2 227345.73 56 5 3 2 2
C7 d16d2
8 1 2 227345.7 40 6 4 2 2
C8 d14d10e7f1 1 1 220345272 38 11 5 3 2
C9 d14d3
6 1 6 220365.7 30 6 4 2 1
C10 d2
12e8 1 2 22535527 44 5 3 2 2
C11 d2
12d8 1 2 2253552 36 6 4 2 2
C12 d12d2
8d4 1 2 224345 28 11 7 2 2
C13 d12e2
7d6 1 2 219355.72 32 9 5 3 1
C14 d12d3
6f2 1 6 219365 24 9 4 2 1
C15 d12d5
4 1 120 2223352 20 5 3 1 1
C16 d3
10f2 1 6 2223453 30 5 2 1 1
C17 d2
10d2
6 1 4 2223452 26 7 4 2 1
C18 d10e8e2
7 1 2 220345.73 38 8 4 3 2
C19 d10d8e7d6f1 1 1 219345.7 26 17 7 4 2
C20 d10d8d2
6f2 1 2 220345 22 15 6 3 2
C21 d10d2
6d2
4f2 1 4 219335 18 16 6 2 1
C22 d10d4
4f6 6 24 219335 14 9 3 1 1
C23 d10g22 2 1 21533527.11 10 4 2 1 1
C24 e4
8 1 24 2273574 56 2 1 1 1
C25 e8d3
8 1 6 225357 32 5 3 2 2
C26 e8d4
6 1 24 221367 26 5 3 2 1
C27 e8d6
4 3 720 222345.7 20 4 2 1 1
C28 e8g24 1 1 216345.7211.23 14 3 1 1 1
C29 d4
8 1 24 22735 24 3 2 1 1
C30 d4
8 1 8 22734 24 4 2 1 1
C31 d3
8d2
4 1 6 22334 20 6 3 1 1
C32 d2
8e2
7f2 1 4 2203472 26 10 3 2 1
C33 d2
8d2
6f4 1 4 22034 18 14 4 2 1
C34 d2
8d4
4 1 16 22432 16 8 4 1 1
C35 d8e7d2
6d4f1 1 2 218347 20 18 7 3 1
C36 d8d4
6 1 8 22135 18 7 4 2 1
C37 d8d2
6d6d4f2 1 2 21834 16 22 9 3 1
C38 d8d2
6d2
4f4 1 4 21833 14 20 7 2 1
C39 d8d6d3
4f6 2 6 21733 12 17 6 2 1
C40 d8d6
4 1 48 22232 12 7 4 1 1
C41 d8d4
4f8 2 24 21832 10 12 4 1 1
C42 d8d2
4g16 36 2 21733 8 9 3 1 1
C43 d8h24 1 1 216345 6 5 2 1 1
C44 e4
7d4 1 24 2173574 29 4 2 1 0

102

Table IV: Doubly-even self-dual (or Type II) binary codes of length 32 (Part 2)

Code Components |G1| |G2| |G| A4 n30 n28 n26 n24
C45 e2
7d3
6 1 6 2163672 23 6 3 2 0
C46 e7d3
6d4f3 1 6 215357 17 13 4 2 0
C47 e7d6d4
4f3 1 24 217337 14 12 4 2 0
C48 e7d4
4f9 18 24 215347 11 7 2 1 0
C49 e7d4g21 6 1 212345.72 8 6 2 1 0
C50 d5
6f2 1 10 216355 15 6 2 1 0
C51 d4
6d2
4 1 48 22035 14 6 3 1 0
C52 d4
6d4f 2
2 1 8 21734 13 13 4 1 0
C53 d4
6f8 2 24 21635 12 8 2 1 0
C54 d3
6d3
4f2 1 6 21634 12 12 5 1 0
C55 d3
6d2
4f6 1 6 21434 11 15 3 1 0
C56 d2
6d4
4f 2
2 1 8 21732 10 16 4 1 0
C57 d2
6d4
4f4 2 16 21932 10 13 4 1 0
C58 d2
6d3
4f2f6 1 12 21433 9 18 4 1 0
C59 d2
6d2
4f12 12 4 21433 8 14 3 1 0
C60 d2
6g20 4 2 215335 6 6 2 1 0
C61 d6d2
4d3
4f 2
3 1 12 21532 8 19 6 1 0
C62 d6d4
4f10 2 8 2153 7 21 4 1 0
C63 d6d3
4f14 8 6 21332 6 18 4 1 0
C64 d6d2
4g18 36 2 21034 5 12 3 1 0
C65 d6d4g16f6 72 1 21233 4 14 4 1 0
C66 d6f 2
13 5616 2 283413 3 6 2 1 0
C67 d8
4 6 1344 223327 8 2 1 0 0
C68 d8
4 1 1152 22332 8 3 1 0 0
C69 d8
4 1 336 2203.7 8 2 1 0 0
C70 d6
4f8 4 48 2183 6 7 2 0 0
C71 d6
4f8 1 48 2163 6 9 2 0 0
C72 d4
4d4f12 6 24 21432 5 10 2 0 0
C73 d5
4f12 1 60 2123.5 5 6 1 0 0
C74 d4
4g16 8 24 2183 4 7 2 0 0
C75 d4
4f16 8 8 214 4 14 2 0 0
C76 d3
4g18f2 8 6 21032 3 13 2 0 0
C77 d2
4q+
24 6 2 21532 2 6 1 0 0
C78 d2
4q−
24 3 2 21032 2 8 1 0 0
C79 d4f 6
4 16 72 21132 2 8 1 0 0
C80 d4f 4
7 168 8 283.7 1 8 2 0 0
C81 q32 1 1 253.5.31 0 1 0 0 0
C82 r32 1 1 215325.7.31 0 1 0 0 0
C83 g2
16 20160 2 215325.7 0 2 0 0 0
C84 f 8
4 256 336 2123.7 0 2 0 0 0
C85 f 16
2 2 11520 29325 0 3 0 0 0

103

Table V: The groups G0 for the components mentioned in Tables II, III and IV.

Component G0 |G0|
d2m 2m−1.S(m) 2m−1m!
e7 L3(2) 168
e8 GA3(2) 1344
fn 1 1
g16 24 16
g18 Z(3) 3
g20 M20 263.5
g21 M21 26325.7
g22 M22 27325.7.11
g24 M24 210335.7.11.23
h24 26 : 3S(6) 29335
q+
24 26.(S(3) × 22) 293
q−
24 22 × S(4) 253

104

Figure 3: Generator matrices for the [32, 16, 8] Type II codes C83 = g2+
16 , C84 = f 8+
4 and
C85 = f 16+
2 .
 11101000111010000000000000000000
10110100101101000000000000000000
10011010100110100000000000000000
10001101100011010000000000000000
00000000000000001101100011011000
00000000000000001010110010101100
00000000000000001001011010010110
00000000000000001000101110001011
11011000110110001101100000000000
10101100101011001010110000000000
10010110100101101001011000000000
10001011100010111000101100000000
00000000111010001110100011101000
00000000101101001011010010110100
00000000100110101001101010011010
00000000100011011000110110001101

11101000000000001110100011101000
10110100000000001011010010110100
10011010000000001001101010011010
10001101000000001000110110001101
00000000111010001110100010110100
00000000101101001011010010011010
00000000100110101001101010001101
00000000100011011000110111000110
11011000110110001101100000000000
10101100101011001010110000000000
10010110100101101001011000000000
10001011100010111000101100000000
11011000101100010000000011011000
10101100110110000000000010101100
10010110101011000000000010010110
10001011100101100000000010001011

10000000000000001111100010001000
01000000000000001111010001000100
00100000000000001111001000100010
00010000000000001111000100010001
00001000000000001000111110001000
00000100000000000100111101000100
00000010000000000010111100100010
00000001000000000001111100010001
00000000100000001000100011111000
00000000010000000100010011110100
00000000001000000010001011110010
00000000000100000001000111110001
00000000000010001000100010001111
00000000000001000100010001001111
00000000000000100010001000101111
00000000000000010001000100011111

105

Table VI:

Binary self-dual codes with n ≤ 22, d ≥ 4
n Code Compts. Name |G1| |G2| A4 A6 A8 A10 A12 Generators for glue
0 C1(d32) i0 - 1 1 -
8 C2(d24) e8 A8 1 1 14 0 1 -
12 C3(d20) d12 B12 1 1 15 32 15 0 1 a
14 C4(d18) e2
7 D14 1 2 14 49 49 14 0 dd
16 C5(d16) d16 E16 1 1 28 0 198 0 28 a
C6(d16) e2
8 A8 ⊕ A8 1 2 28 0 198 0 28 -
C7(d16) d2
8 F16 1 2 12 64 102 64 12 (ab)
18 C8(d14) d10e7f1 I18 1 1 17 51 187 187 51 aoA, cd-
C9(d14) d3
6 H18 1 6 9 75 171 171 75 (abc), bbb
20 C3(d12) d20 J20 1 1 45 0 210 512 210 a
C10(d12) d12e8 A8 ⊕ B12 1 1 29 32 226 448 226 a-
C11(d12) d12d8 K20 1 1 21 48 234 416 234 (ab)
C12(d12) d2
8d4 S20 1 2 13 64 242 384 242 (ab)x, bby
C13(d12) e2
7d6 L20 1 2 17 56 238 400 238 doa, ddb
C14(d12) d3
6f2 R20 1 6 9 72 246 368 246 aaaA, cccB, (abc)-
C15(d12) d5
4 M20 1 120 5 80 250 352 250 (ooxyx)
22 C8(d10) d14e7f1 N22 1 1 28 49 246 700 700 aoA, bdA
C16(d10) d2
10f2 P22 1 2 20 57 270 676 676 (ao)∗, cc-
C17(d10) d10d2
6 Q22 1 2 16 61 282 664 664 aoc, oaa, bbb
C18(d10) e8e2
7 E8 ⊕ D14 1 2 28 49 246 700 700 -dd
C19(d10) d8e7d6f1 R22 1 1 16 61 282 664 664 odbA, boaA, aob-
C20(d10) d8d2
6f2 S22 1 2 12 65 294 652 652 baoA, aooAB, abb-,
occ-
C21(d10) d2
6d2
4f2 T22 1 4 8 69 306 640 640 aoxoA, ooyyAB,
aayo-, bozx-, obxz-
C22(d10) d4
4f6 U22 6 24 4 73 318 628 628 oxyzBC, ozxyAC,
ooxxAE, oyoyAD,
ozzoAF, xxxx-,
yyyy-
C23(d10) g22 G22 2 1 0 77 330 616 616 the all-ones vector

106

Table VII:

Binary self-dual codes with length 24 and d ≥ 4
Code Components Name d Code Components Name d
C2(e8) d24 § E24 4 C32(d8) d8e2
7f2 J24 4
C6(e8) d16e8 § — 4 C33(d8) d8d2
6f4 R24 4
C7(d8) d16d8 H24 4 C34(d8) d8d4
4 T24 4
C10(e8) d2
12 § A24 4 C35(d8) e7d2
6d4f1 P24 4
C11(d8) d2
12 — 4 C26(e8) d4
6 § D24 4
C12(d8) d12d8d4 I24 4 C36(d8) d4
6 Q24 4
C18(e8) d10e2
7 § B24 4 C37(d8) d2
6d6d4f2 S24 4
C19(d8) d10e7d6f1 K24 4 C38(d8) d2
6d2
4f2 U24 4
C20(d8) d10d2
6f2 N24 4 C39(d8) d6d3
4f6 W24 4
C24(e8) e3
8 § — 4 C27(e8) d6
4 § F24 4
C25(d8) e8d2
8 — 4 C40(d8) d6
4 V24 4
C25(e8) d3
8 § C24 4 C41(d8) d4
4f8 X24 4
C29(d8) d3
8 L24 4 C42(d8) d2
4g16 Y24 4
C30(d8) d3
8 M24 4 C43(d8) h24 Z24 6
C31(d8) d2
8d2
4 O24 4 C28(e8) g24 § G24 8

Table VIII: Indecomposable ternary self-dual codes of lengths n ≤ 20

n Components |G0| |G1| |G2| d glue
4 t4 48 1 1 3 −
8 −
12 e
4+
3 64 2 24 3 aaa0, 0¯aaa
g12 190080 1 1 6 −
16 (e4
3f4)+ 64.1 8 24 3 (a000)(2111)
(e2
3g10)+ 62.360 4 2 3 a0x, 0ay
(e3p13)+ 6.5616 2 1 3 at0
f 2+
8 12 27.168 2 6 [I|H8]
20 17 codes
– see [243]
 107

Table IX: Indecomposable Hermitian self-dual codes over F4 of lengths n ≤ 16

n Components |G0| |G1| |G2| d Glue
2 i2 12 1 1 2 −
4 − − − − − −
6 h6 2160 1 1 4 −
8 e8 8064 1 1 4 −
10 d
+
10 24.5! 6 1 4 d
e
2+
5 602 6 2 4 11
12 d
+
12 25.6! 6 1 4 a
(e7e5)+ 60.168 6 1 4 11
d
2+
6 242 6 2 4 (bd)
d
3+
4 43 54 6 4 (0de)
14 d
+
14 26.7! 6 1 4 d
e
2+
7 1682 6 2 4 11
(d8e5f1)+ 23.4!60 6 1 4 d01, e10
(e2
5d4)+ 4.602 18 2 4 01d, 10e
(d8d6)+ 234!223! 6 1 4 ab, bd
(d2
6f2)+ (22.3!)2 6 2 4 (d0)11, bbωω
(d6d2
4)+ 42223! 18 2 4 bbb, a0d, cd0
(d3
4f2)+ 43 6 6 4 aa011, 0aaωω, ˙b¨b0ωω, 0˙b¨bω1
(d2
416)+ 42 108 2 4 b00011ωω, a00ωω110,
0b01ω01ω, 0a011ωω0
q14 6552 1 1 6 −
16 31 codes
(see [64])
 108

Table X: Highest minimal distance of binary self-dual codes

n dI dII Codes
2 2 i2.
4 2 i2
2.
6 2 i3
2.
8 2 4 i4
2; e8.
10 2 i5
2, e8i2.
12 4 d
+
12.
14 4 e
2+
7 .
16 4 4 d
2+
8 ; d
+
16, e2
8.
18 4 d
3+
6 , (d10e7f1)+.
20 4 7 codes (Table II).
22 6 g22.
24 6 8 h
+
24; g24.
26 6 f 2
13 [62].
28 6 3 codes [62].
30 6 13 codes [62], [65].
32 8 8 3 codes [69]; 5 codes (Table III).
34 6 ≥ 200
36 8 ≥ 2
38 8 ≥ 3 [69], [127]
40 8 8 ≥ 22; ≥ 1000 (see text for references)
42 8 ≥ 30 [83]
44 8 ≥ 108 [83]
46 10 ≥ 1 [69]
48 10 12 ≥ 7; ≥ 1 (XQ47)
50 10 ≥ 6
52 10 ≥ 499 [152]
54 10 ≥ 54
56 10 or 12 12 ?; ≥ 166
58 10 ≥ 80 [83]
60 12 ≥ 5
62 10 or 12 ?
64 12 12 ≥ 5; ≥ 3270 [83]
66 12 ≥ 3
68 12 ≥ 65
70 12 or 14 ? [121], [276]
72 12 or 14 12 or 16 ?; ?
 109

Table XI: Double circulant binary codes

Name n k d Type Form r (hexadecimal)
g22 22 11 6 I (179) 97
g24 24 12 8 II (178) B7
A26 = f 2+
13 26 13 6 I (179) 5F7
A28 =D1 28 14 6 I (178) 8D
D2 34 17 6 I (179) 1ECE
D3 36 18 8 I (178) 2C6B
D4 38 19 8 I (179) 5793
D5 40 20 8 II (179) 57EB
D6 40 20 8 I (179) 11E35
D7 40 20 8 I (179) B393
D8 44 22 8 I (178) 5E6B5
D9 50 25 10 I (179) 31C4D
D10 52 26 10 I (178) 57F69D
D11 56 28 12 II (178) ADF1FF
D12 58 29 10 I (179) D5A89B
D12a 58 29 10 I (179) 2DD1D3
D13 60 30 12 I (178) 3EF6B77
D14 64 32 12 II (178) 427BD0B
D15 64 32 12 I (179) 2EF3DD75
D16 66 33 12 I (179) B2D97D9
D17 68 34 12 I (179) 1F5C885F
D18∗ 72 36 12 I (179) 2B8795E5
D19∗ 74 37 12 I (179) 1439372C7
D20∗ 82 41 12 I (179) A464B919B
H86 86 43 16 I (179) 7F7101712E2
M88 88 44 16 II (178)
M136 136 68 24 II (178)

110

Table XII: Highest minimal distance of ternary self-dual codes

n d Codes
4 3 t4.
8 3 t2
4.
12 6 g12.
16 6 f 2+
8 .
20 6 6 codes [243].
24 9 XQ23, S(24) [180].
28 9 ≥ 32 [58], [123], [174], [146]
32 9 ≥ 239 [146]
36 12 ≥ 1 (S(36))
40 12 ≥ 20 [321], [76], [123], [146]
44 12 ≥ 8 [123]
48 15 ≥ 2 (XQ47, S(48))
52 12 or 15 ?
56 15 ≥ 1
60 18 ≥ 2 (XQ59, S(60))
64 18 ≥ 1 [12], [76]
68 15 or 18 ?
72 18 ≥ 1 (XQ71[74])

Table XIII: Highest minimal distance of Hermitian self-dual codes over F4

n d Codes
2 2 i2.
4 2 i2
2.
6 4 h6.
8 4 e8.
10 4 d
+
10, e
2+
5 .
12 4 5 codes (Table IX).
14 6 q14.
16 6 4 codes [64].
18 8 S18 [148].
20 8 2 codes [148].
22 8 ≥ 38 codes [143], [145]
24 8 ≥ 1 code
26 8 or 10 ?
28 10 ≥ 3 codes [143], [145]
30 12 XQ29 [189]
32 ? ?
 111

Table XIV: Highest minimal distance of additive self-dual codes over F4

n d Codes n d Codes
1 1 i1. 16 6 ≥ 4 codes [64]
2 2 i2. 17 7
3 2 d
+
3 . 18 8 S18
4 2 3 codes. 19 7
5 3 h5. 20 8 ≥ 2 codes [148]
6 4 h6. 21 8 c21
7 3 22 8 ≥ 38 codes [143]
8 4 e8 23 8–9 c23
9 4 c9 24 8–10 g24 ⊗ F4
10 4 d
+
10 , e
2+
5 25 8–9 c25
11 5 26 8–10
12 6 z12. 27 9–10
13 5 28 10
14 6 q14 29 11
15 6 c15 30 12 XQ29

Table XV: Generators for cyclic additive codes over F4

c9 (ω10100101)
c15 (ω11010100101011)
c21 (ωω1ω00111101011011000), (101110010111001011100)
c23 (ω0101111000000001111010)
c25 (111010ω010111000000000000)

112

Table XVI: Highest Hamming distance (dH ), Lee distance (dL) and Euclidean norm (Norm)
of self-dual codes over Z4

Length Hamming Lee Norm
n dH code # dL code # Norm code #
1 1 i1 1 2 i1 1 4 i1 1
2 1 i2
1 1 2 i2
1 1 4 i2
1 1
3 1 i3
1 1 2 i3
1 1 4 i3
1 1
4 2 D⊕
4 1 4 D⊕
4 1 4 i4
1 2
5 1 D⊕
4 i1 2 2 D⊕
4 i1 2 4 i5
1 2
6 2 D⊕
6 1 4 D⊕
6 1 4 i6
1 3
7 3 E+
7 1 4 E+
7 1 4 i7
1 4
8 4 o8 2 6 o8 1 8 o8 1
9 1 o8i1 11 2 o8i1 11 4 i9
1 11
10 2 D⊕
4 D⊕
6 5 4 D⊕
4 D⊕
6 5 4 i10
1 16
11 2 D⊕
4 E+
7 3 4 D⊕
4 E+
7 3 4 i11
1 19
12 2 D⊕
4 o8 39 4 D⊕
4 o8 39 8 [95] 19
13 2 D⊕
6 E+
7 8 4 D⊕
6 E+
7 8 4 i13
1 66
14 3 (E+
7 )2 4 6 [95] 1 8 [95] 35
15 3 E+
7 o8 47 6 [95] 15 8 [95] 28
16 4 o2
8 ≥ 1 8 C16 ≥ 5 8 o2
8 ≥ 5
17 4 C17 62 6 C17 ≥ 17 8 C17 ≥ 17
18 4 C18 66 8 C18 7 8 C18 ≥ 39
19 3 G19 ≥ 1 6 G19 ≥ 1 8 G19 ≥ 1
20 4 G20 ≥ 1 8 G20 ≥ 1 8 G20 ≥ 1
21 5 G21 384 8 G21 384 8 G21 ≥ 384
22 6 G22 ≥ 19367 8 G22 ≥ 19367 8 G22 ≥ 19367
23 7 G23 ≥ 1.72 × 106 10 G23 30 12 G23 ≥ 30
24 8 G24 ≥ 1.47 × 108 12 G24 13 16 G24 ≥ 50

113

The bibliography uses the following abbreviations for journals:

DCC = Designs, Codes and Cryptography

DM = Discrete Mathematics

JCT = Journal of Combinatorial Theory

PGIT = IEEE Transactions on Information Theory

References

[1] V. K. Agrawala and J. G. Belinfante, An algorithm for computing SU (n) invariants, BIT

11 (1971), 1–15.

[2] O. Amrani, Y. Be’ery, A. Vardy, F.-W. Sun and H. C. A. van Tilborg, The Leech lattice

and the Golay code: bounded-distance decoding and multilevel constructions, PGIT 40

(1994), 1030–1043.

[3] E. F. Assmus, Jr. and J. D. Key, Designs and Their Codes, Cambridge Univ. Press, 1992.

[4] and H. F. Mattson, Jr., Coding and combinatorics, SIAM Review 16 (1974), 349–

388.

[5] and R. J. Turyn, Research to develop the algebraic theory of codes, Report

AFCRL-67-0365, Air Force Cambridge Res. Labs., Bedford, MA, June 1967.

[6] and V. Pless, On the covering radius of extremal self-dual codes, PGIT 29 (1983),

359–363.

[7] L. Babai, H. Oral and K. T. Phelps, Eulerian self-dual codes, SIAM J. Discr. Math. 7

(1994), 323–333.

[8] C. Bachoc, Applications of coding theory to the construction of modular lattices, JCT

A 78 (1997), 92–119.

[9] E. Bannai, S. T. Dougherty, M. Harada and M. Oura, Type II codes, even unimodular

lattices and invariant rings, preprint, June 1997.

[10] S. Minashima and M. Ozeki, On Jacobi forms of weight 4, Kyushu J. Math. 50

(1996), 335–370.
 114

[11] and M. Ozeki, Construction of Jacobi forms from certain combinatorial polynomials,

Proc. Japan Acad. A 72 (1996), 359–363.

[12] G. F. M. Beenker, A note on extended quadratic residue codes over GF (9) and their

ternary images, PGIT 30 (1984), 403–405.

[13] D. J. Benson, Polynomial Invariants of Finite Groups, Cambridge Univ. Press, 1993.

[14] E. R. Berlekamp, F. J. MacWilliams, and N. J. A. Sloane, Gleason’s theorem on self-dual

codes, PGIT 18, (1972), 409–414.

[15] V. K. Bhargava and C. Nguyen, Circulant codes based on the prime 29, PGIT 26 (1980),

363–364.

[16] and J. M. Stein, (v, k, d) conﬁgurations and self-dual codes, Inform. Contr. 28

(1975), 352–355.

[17] G. Young and A. K. Bhargava, A characterization of a (56, 28) extremal self-dual

code, PGIT 27 (1981), 258–260.

[18] I. F. Blake, Properties of generalized Pless codes, in Proc. 12th Allerton Conf. Circuit

and System Theory, Univ. Ill., Urbana, 1974, pp. 787–789.

[19] On a generalization of the Pless symmetry codes, Inform Control 27 (1975), 369–

373.

[20] B. Bolt, T. G. Room and G. E. Wall, On Cliﬀord collineation, transform and similarity

groups I, J. Australian Math. Soc. 2 (1961), 60–79.

[21] On Cliﬀord collineation, transform and similarity groups II, J. Australian

Math. Soc. 2 (1961), 80–96.

[22] A. Bonnecaze, A. R. Calderbank and P. Sol´e, Quaternary quadratic residue codes and

unimodular lattices, PGIT 41 (1995), 366–377.

[23] P. Gaborit, M. Harada, M. Kitazume and P. Sol´e, Niemeier lattices and Type II

codes over Z4, preprint.

[24] B. Mourrain and P. Sol´e, Jacobi polynomials, Type II codes, and designs, DCC,

submitted.
 115

[25] A. Bonnecaze, E. M. Rains and P. Sol´e, Z4 codes and 5-designs, preprint.

[26] and P. Sol´e, Quaternary constructions of formally self-dual binary codes and uni-

modular lattices, in Algebraic Coding, Lect. Notes. Comp. Sci. 781 (1994), 194–205.

[27] C. Bachoc and B. Mourrain, Type II codes over Z4, PGIT 43 (1997), 969–976.

[28] W. Bosma and J. Cannon, Handbook of Magma Functions, Sydney, May 22, 1995.

[29] and G. Mathews, Programming with algebraic structures: Design of the

Magma language, in Proceedings of the 1994 International Symposium on Symbolic and

Algebraic Computation, M. Giesbrecht, Ed., Association for Computing Machinery, 1994,

52–57.

[30] and C. Playoust, The Magma algebra system I: The user language, J. Symb.

Comp. 24 (1997), 235–265.

[31] N. Bourbaki, Groups et Alg`ebres de Lie, Chap. 4, 5 et 6, Hermann, Paris, 1968.

[32] M. Brou´e, Codes correcteurs d’erreures auto-orthogonal sur le corps `a deux ´el´ements

et formes quadratiques enti`eres d´eﬁnies positives `a discriminant +1, Comptes Rendus

Journ. Math. Soc. Math. France, Univ. Sci. Tech. Languedoc, Montpellier, 1974, pp. 71–

108.

[33] and M. Enguehard, Polynˆomes des poids de certains codes et fonctions thˆeta de

certains r´eseaux, Ann. Sci´ent. Ec. Norm. Sup. 5 (1972), 157–181.

[34] A. E. Brouwer, A. M. Cohen and A. Neumaier, Distance-Regular Graphs, Springer-

Verlag, Berlin, 1989.

[35] R. A. Brualdi and V. S. Pless, Weight enumerators of self-dual codes, PGIT 37 (1991),

1222–1225.

[36] W. Bruns and J. Herzog, Cohen-Macaulay Rings, Cambridge Univ. Press, 1993.

[37] W. Burnside, Group Theory, Dover, NY, 2nd ed., 1955.

[38] F. C. Bussemaker and V. D. Tonchev, New extremal doubly-even codes of length 56

derived from Hadamard matrices of order 28, DM 76 (1989), 45–49.

116

[39] Extremal doubly-even codes of length 40 derived from Hadamard matrices,

DM 82 (1990), 317–321.

[40] S. Buyuklieva, New extremal self-dual codes of lengths 42 and 44, PGIT 43 (1997),

1607–1612.

[41] On the binary self-dual codes with an automorphism of order 2, DCC 12 (1997),

39–48.

[42] and I. Boukliev, Extremal self-dual codes with an automorphism of order 2, PGIT

44 (1998), 323–328.

[43] and V. Y. Yorgov, Singly-even self-dual codes of length 40, DCC 9 (1996), 131–141.

[44] A. R. Calderbank, P. J. Cameron, W. M. Kantor and J. J. Seidel, Z4-Kerdock codes,

orthogonal spreads and extremal Euclidean line-sets, Proc. London Math. Soc. 75 (1997),

436–480.

[45] A. R. Hammons, Jr., P. V. Kumar, N. J. A. Sloane and P. Sol´e, A linear construction

for certain Kerdock and Preparata codes, Bull. Amer. Math. Soc. 29 (1993), 218–222.

[46] W.-C. W. Li and B. Poonen, A 2-adic approach to the analysis of cyclic codes,

PGIT 43 (1997), 977–986.

[47] G. McGuire, P. V. Kumar and T. Helleseth, Cyclic codes over Z4, locator polyno-

mials, and Newton’s identities, PGIT 42 (1996), 217–226.

[48] E. M. Rains, P. W. Shor and N. J. A. Sloane, Quantum error correction and

orthogonal geometry, Phys. Rev. Lett. 78 (1997) 405–409.

[49] Quantum error correction via codes over GF(4), PGIT 44 (1998),

to appear.

[50] and N. J. A. Sloane, Modular and p-adic cyclic codes, DCC 6 (1995), 21–35.

[51] Double circulant codes over Z4 and even unimodular lattices, J. Algebraic

Combinatorics 6 (1997), 119–131.

[52] P. Camion, ´Etude de codes binaires ab´eliens modulaires autoduaux de petites longueurs,

Revue du CETHEDEC 79-2 (1979), 3–24.

117

[53] B. Courteau and A. Montpetit, Coset weight enumerators of the extremal self-

dual binary codes of length 32, in EUROCODE ’92, CISM Courses and Lectures 339,

Springer-Verlag, NY, 1993, pp. 17–30.

[54] C. Carlet, On Z4-duality, PGIT 41 (1995), 1487–1494.

[55] R. Chapman and P. Sol´e, Universal codes and unimodular lattices, J. Th´eorie Nombres

Bordeaux 8 (1996), 369–376.

[56] P. Charpin, Self-dual codes which are principal ideals of the group algebra F2[{F2m , +}],

J. Statist. Plann. Infer. 56 (1996), 79–92.

[57] and F. Levy-dit-Vehel, On self-dual aﬃne-invariant codes, JCT A 67 (1994), 223–

244.

[58] Y. Cheng and R. Scharlau, personal communication, Sept., 1987.

[59] and N. J. A. Sloane, The automorphism group of an [18,9,8] quaternary code, DM

83 (1990), 205–212.

[60] Codes from symmetry groups and a [32,17,8] code, SIAM J. Discrete Math. 2

(1989), 28–37.

[61] J. H. Conway, A. M. Odlyzko, and N. J. A. Sloane, Extremal self-dual lattices exist only

in dimensions 1-8, 12, 14, 15, 23 and 24, Mathematika 25 (1978), 36–43. A revised version

appears as Chapter 14 of [70].

[62] and V. Pless, On the enumeration of self-dual codes, JCT A 28 (1980), 26–53.

[63] On primes dividing the group order of a doubly-even (72,36,16) code and the

group order of a quaternary (24,12,10) code, DM 38 (1982), 143–156.

[64] and N. J. A. Sloane, Self-dual codes over GF (3) and GF (4) of length not

exceeding 16, PGIT 25 (1979), 312–322.

[65] The binary self-dual codes of length up to 32: A revised enumeration,

JCT A 60 (1992), 183–195.

[66] and N. J. A. Sloane, Soft decoding techniques for codes and lattices, including the

Golay code and the Leech lattice, PGIT 32 (1986), 41–50.

118

[67] Low-dimensional lattices II: Subgroups of GL(n, Z), Proc. Royal Soc. A 419

(1988), 29–68.

[68] A new upper bound for the minimum of an integral lattice of determinant one,

Bull. Amer. Math. Soc. 23 (1990), 383–387. Erratum: volume 24 (April 1991), p. 479.

[69] A new upper bound on the minimal distance of self-dual codes, PGIT 36,

(1990), 1319–1333.

[70] Sphere Packings, Lattices and Groups, Springer-Verlag, NY, 2nd edition, 1993.

[71] Self-dual codes over the integers modulo 4, JCT A 62 (1993), 30–45.

[72] On lattices equivalent to their duals, J. Number Theory 48 (1994), 373–382.

[73] Codes and lattices, PGIT, to appear, 1998.

[74] D. Coppersmith and G. Seroussi, On the minimum distance of some quadratic residue

codes, PGIT 30 (1984), 407–411.

[75] E. C. Dade, Answer to a question of R. Brauer, J. Algebra 1 (1964), 1–4.

[76] E. Dawson, Self-dual ternary codes and Hadamard matrices, Ars Comb. 19A (1985),

303–308.

[77] A construction for the generalized Hadamard matrices GF (4q; EA(q)), J. Statist.

Plann. Inf. 11 (1985), 103–110.

[78] P. Delsarte, Bounds for unrestricted codes, by linear programming, Philips Res. Reports

27 (1972), 272–289.

[79] J. Dieudonn´e and J. B. Carroll, Invariant Theory, Old and New, Acad. Press, NY, 1971.

[80] P. Doubilet, G.-C. Rota and J. Stein, On the foundations of combinatorial theory. IX:

Combinatorial methods in invariant theory, Studies in Appl. Math. 53 (1974), 185–216.

[81] S. T. Dougherty, Shadow codes and weight enumerators, PGIT 41 (1995), 762–768.

[82] T. A. Gulliver and M. Harada, Type II self-dual codes over ﬁnite rings and even

unimodular lattices, J. Alg. Combin., to appear.

119

[83] Extremal binary self-dual codes, PGIT 43 (1997), 2036–2046..

[84] and M. Harada, Shadow optimal self-dual codes, Kyushu J. Math., to appear.

[85] New extremal self-dual codes of length 68, preprint.

[86] Self-dual codes constructed from Hadamard matrices and symmetric designs,

preprint.

[87] and M. Oura, Formally self-dual codes, preprint.

[88] and P. Sol´e, Shadow codes over Z4, Finite Fields Applic. to appear.

[89] Self-dual codes over rings and the Chinese remainder theorem, preprint,

1997.

[90] W. Duke, On codes and Siegel modular forms, Internat. Math. Res. Notices 5 (1993),

125–136.

[91] H. Dym and H. P. McKean, Fourier Series and Integrals, Acad. Press, NY, 1972.

[92] W. Ebeling, Codes and Lattices, Vieweg, Wiesbaden, 1994.

[93] M. Eichler and D. Zagier, The Theory of Jacobi Forms, Birkh¨auser, Boston, 1985.

[94] W. Feit, A self-dual even (96,48,16) code, PGIT 20 (1974), 136–138.

[95] J. Fields, P. Gaborit, J. Leon and V. Pless, All self-dual Z4 codes of length 15 or less are

known, PGIT 44 (1998), 311–322.

[96] C. S. Fisher, The death of a mathematical theory: a study in the sociology of knowledge,

Archiv. Hist. Exact. Sci. 3 (1967), 136–159.

[97] G. D. Forney, Jr., Coset codes I: introduction and geometrical classiﬁcation, PGIT 34

(1988), 1066–1070.

[98] Coset codes II: binary lattices and related codes, PGIT 34 (1988), 1152–1187.

[99] N. J. A. Sloane and M. D. Trott, The Nordstrom-Robinson code is the binary image

of the octacode, in Coding and Quantization: DIMACS/IEEE Workshop October 19–21,

1992, pp. 19–26, R. Calderbank, G. D. Forney, Jr. and and N. Moayeri, Eds., Amer.

Math. Soc. (1993).
 120

[100] R. Fossum et al., editors, Invariant Theory, Contemporary Math. 88 Amer. Math. Soc.,

1989.

[101] P. Gaborit, Mass formulas for self-dual codes over Z4 and Fq +uFq rings, PGIT 42 (1996),

1222–1228.

[102] and M. Harada, Construction of extremal Type II codes over Z4, DCC, submitted.

[103] and P. Sol´e, Self-dual codes over Z4 and unimodular lattices: a survey, preprint.

[104] F. Gherardelli, editor, Invariant Theory: Proceedings, Montecatini, 1982, Lect. Notes.

Math. 996, Springer-Verlag, NY, 1983.

[105] A. M. Gleason, Weight polynomials of self-dual codes and the MacWilliams identities,

in Actes, Congr´es International de Math´ematiques, Gauthier-Villars, Paris, 3 (1970),

211–215.

[106] I. J. Good, Generalizations to several variables of Lagrange’s expansion, with applications

to stochastic processes, Proc. Camb. Phil. Soc. 56 (1960), 367–380.

[107] T. A. Gulliver and V. K. Bhargava, Self-dual codes based on the twin prime product 35,

Appl. Math. Lett. 5 (1992), 95–98.

[108] and M. Harada, Weight enumerators of extremal singly-even [60, 30, 12] codes, PGIT

42 (1996), 658–659.

[109] Classiﬁcation of extremal double circulant formally self-dual even codes, DCC

11 (1997), 25–35.

[110] Weight enumerators of double circulant codes and new extremal self-dual

codes, DCC 11 (1997), 141–150.

[111] Classiﬁcation of extremal double circulant self-dual codes of lengths 64 to 72,

DCC 13 (1998), 257–269.

[112] Certain self-dual codes over Z4 and the odd Leech lattice, Proc. 12th Appl. Alg.

Algorithms and Error-Correcting Codes, Lect. Notes Comp. Sci. 1225 (1997), 130–137.

[113] On the existence of a formally self-dual even [70, 35, 14] code, Appl. Math.

Lett. 11 (1998), 95–98.
 121

[114] New optimal self-dual codes over GF (7), Graphs and Combin., to appear.

[115] Extremal double circulant Type II code over Z4 and construction of 5 −

(24, 10, 36) designs, DM, to appear

[116] Double circulant self-dual codes over GF (5), Ars Comb., to appear.

[117] Double circulant self-dual codes over Z2k, PGIT, submitted.

[118] and H. Kaneta, Classiﬁcation of extremal double circulant self-dual codes of

length up to 62, DM, to appear.

[119] A. R. Hammons, Jr., P. V. Kumar, A. R. Calderbank, N. J. A. Sloane, and P. Sol´e,

The Z4-linearity of Kerdock, Preparata, Goethals and related codes, PGIT 40 (1994),

301–319.

[120] M. Harada, Existence of new extremal doubly-even codes and extremal singly-even codes,

DCC 8 (1996), 273–284.

[121] The existence of a self-dual [70, 35, 12] code and formally self-dual codes, Finite

Fields Applic. 3 (1997), 131–139.

[122] Weighing matrices and self-dual codes, Ars Comb. 47 (1997), 65–73.

[123] New extremal ternary self-dual codes, Australasian J. Combin., to appear.

[124] New extremal Type II codes over Z4, DCC 13 (1998), 271–284.

[125] New 5-designs constructed from the lifted Golay code over Z4, J. Combin. Designs,

to appear.

[126] and H. Kimura, New extremal doubly-even [64, 33, 12] codes, DCC 6 (1995), 91–96.

[127] On extremal self-dual codes, Math. J. Okayama Univ. 37 (1995), 1–14.

[128] and M. Oura, On the Hamming weight enumerators of self-dual codes over Zk,

preprint, Oct. 1997.

[129] and M. Ozeki, Extremal self-dual codes with the smallest covering radius, preprint.

122

[130] and V.D. Tonchev, Singly-even self-dual codes and Hadamard matrices, in Proc.

Applied. Alg., Alg. Algorithms and Error-Correcting Codes, ed. G. Cohen, M. Giusti and

T. Mora, Lecture Notes in Computer Science 948 (1995), 279–284.

[131] F. Hirzebruch, The ring of Hilbert modular forms for real quadratic ﬁelds of small dis-

criminant, in Modular Functions of One Variable VI, pp. 288–323. Proceedings, Bonn

1976, Lecture Notes in Mathematics No. 627, Springer-Verlag, NY, 1977. (Ges. Abh.,

Vol. II, pp. 501–536.)

[132] Letter to N. J. A. Sloane, Aug. 19, 1986. Reproduced in F. Hirzebruch, Ges. Abh.,

Springer-Verlag, NY, Vol. II, 1987, pp. 796–798.

[133] M. Hochster and J. A. Eagon, Cohen-Macaulay rings, invariant theory, and the generic

perfection of determinantal loci, Amer. J. Math. 93 (1971), 1020–1058.

[134] G. H¨ohn, Self-dual codes over the Kleinian four-group, preprint, 1996.

[135] G. Horrocks and D. Mumford, A rank 2 vector bundle on P 4 with 15,000 symmetries,

Topology 12 (1973), 63–81.

[136] S. Houghten, C. Lam and L. Thiel, Construction of (48, 24, 12) doubly-even self-dual

codes, Congr. Number 103 (1994), 41–53.

[137] K. Huber, Codes over Gaussian integers, PGIT 40 (1994), 207–216.

[138] W. C. Huﬀman, The biweight enumerator of self-orthogonal codes, DM 26 (1978), 129–

143.

[139] Automorphisms of codes with applications to extremal doubly even codes of length

48, PGIT 28 (1982), 511–521.

[140] Decomposing and shortening codes using automorphisms, PGIT 32 (1986), 833–

836.

[141] On the [24,12,10] quaternary code and binary codes with an automorphism having

two cycles, PGIT 34 (1988), 486–493.

[142] On the equivalence of codes and codes with an automorphism having two cycles,

DM 83 (1990), 265–283.
 123

[143] On extremal self-dual quaternary codes of lengths 18 to 28, I, PGIT 36 (1990),

651–660.

[144] On 3-elements in monomial automorphism groups of quaternary codes, PGIT 36

(1990), 660–664.

[145] On extremal self-dual quaternary codes of lengths 18 to 28, II, PGIT 37 (1991),

1206–1216.

[146] On extremal self-dual ternary codes of lengths 28 to 40, PGIT 38 (1992), 1395–1400.

[147] On the classiﬁcation of self-dual codes, Proc. 34th Allerton Conf. Commun. Control

and Computing, October 2–4, 1996, pp. 302–311.

[148] Characterization of quaternary extremal codes of lengths 18 and 20, PGIT 43

(1997), 1613–1616.

[149] Decompositions and extremal type II codes over Z4, PGIT, 44 (1998), 800–809.

[150] and N. J. A. Sloane, Most primitive groups have messy invariants, Advances in

Math. 32 (1979), 118–127.

[151] and V. D. Tonchev, The existence of extremal [50, 25, 10] codes and quasi-symmetric

2-(49,9,6) designs, DCC 6 (1995), 97–106.

[152] The [52, 26, 10] binary self-dual codes with an automorphism of order 7,

preprint.

[153] and V. Y. Yorgov, A [72, 36, 16] doubly even code does not have an automorphism

of order 11, PGIT 33 (1987), 749–752.

[154] V. I. Iorgov: see V. Y. Yorgov.

[155] N. Jacobson, Lectures in Abstract Algebra, 3 vols., Van Nostrand, Princeton, 1951-1964.

[156] D. B. Jaﬀe, Binary linear codes: new results on nonexistence. Available from

http://www.math.unl.edu/∼djaﬀe/codes/code.ps.gz.

[157] S. N. Kapralov and V. D. Tonchev, Extremal doubly-even codes of length 64 derived

from symmetric designs, DM 83 (1990), 285–289.

124

[158] M. Karlin, New binary coding results by circulants, PGIT 15 (1969), 81–92.

[159] G. T. Kennedy, Weight distributions of linear codes and the Gleason-Pierce theorem,

JCT A 67 (1994), 72–88.

[160] and V. Pless, On designs and formally self-dual codes, DCC 4 (1994), 43–55.

[161] A coding theoretic approach to extending designs, DM 142 (1995), 155–168.

[162] H. Kimura, Extremal doubly even (56, 28, 12) codes and Hadamard matrices of order 28,

Australas. J. Combin. 10 (1994), 171–180.

[163] M. Kitazume, T. Kondo and I. Miyamoto, Even lattices and doubly even codes, J. Math.

Soc. Japan 43 (1991), 67–87.

[164] F. Klein, Weitere Untersuchunger ¨uber das Ikosaeder, Math. Ann. 12 (1877) (Ges. Math.

Abh. III, 321–384).

[165] Lectures on the Icosahedron and the Solution of Equations of the Fifth Degree, 2nd

ed., Dover, NY 1956.

[166] M. Klemm, Ueber die Identit¨at von MacWilliams f¨ur die Gewichtsfunktion von Codes,

Archiv Math. 49 (1987), 400-406.

[167] Selbstduale Codes ¨uber dem Ring der ganzen Zahlen modulo 4, Archiv Math. 53

(1989), 201–207.

[168] H. Koch, Unimodular lattices and self-dual codes, in Proc. Intern. Congress Math.,

Berkeley 1986, Amer. Math. Soc. Providence RI 1 (1987), pp. 457–465.

[169] On self-dual, doubly-even codes of length 32, JCT A 51 (1989), 63–76.

[170] On self-dual doubly-even extremal codes, DM 83 (1990), 291–300.

[171] and B. B. Venkov, Ueber ganzzahlige unimodulare euklidische Gitter, J. reine

angew. Math. 398 (1989), 144–168.

[172] S. S. Koh, editor, Invariant Theory, Lect. Notes Math. 1278, Springer-Verlag, NY, 1987.

[173] I. Krasikov and S. Litsyn, Linear programming bounds for doubly-even self-dual codes,

PGIT 43 (1997), 1238–1244.
 125

[174] F. R. Kschischang and S. Pasupathy, Some ternary and quaternary codes and associated

sphere packings, PGIT 38 (1992), 227–246.

[175] C. W. H. Lam, The search for a ﬁnite projective plane of order 10, Amer. Math. Monthly

98 (1991) 305–318.

[176] and V. Pless, There is no (24,12,10) self-dual quaternary code, PGIT 36 (1990),

1153–1156.

[177] L. Thiel and S. Swiercz, The non-existence of ﬁnite projective planes of order 10,

Canad. J. Math. 41 (1989), 1117–1123.

[178] S. Lang, Algebra, Addison-Wesley, Reading, MA, 1965.

[179] J. S. Leon, J. M. Masley and V. Pless, Duadic codes, PGIT 30 (1984), 709–714.

[180] V. Pless and N. J. A. Sloane, On ternary self-dual codes of length 24, PGIT 27,

(1981), 176–180.

[181] Self-dual codes over GF(5), JCT A 32 (1982), 178–194.

[182] J. H. van Lint, Introduction to Coding Theory, Springer-Verlag, NY, 1982.

[183] D. E. Littlewood, A University Algebra, Dover, NY, 2nd ed., 1970.

[184] X. Ma and L. Zhu, Nonexistence of extremal doubly even self-dual codes, preprint, 1997.

[185] F. J. MacWilliams, A theorem on the distribution of weights in a systematic code, Bell

Syst. Tech. J. 43 (1964), 485–505.

[186] Orthogonal matrices over ﬁnite ﬁelds, Amer. Math. Monthly 76 (1969), 152–164.

[187] Orthogonal circulant matrices over ﬁnite ﬁelds, and how to ﬁnd them, JCT 10

(1971), 1–17.

[188] C. L. Mallows and N. J. A. Sloane, Generalizations of Gleason’s theorem on weight

enumerators of self-dual codes, PGIT 18 (1972), 794–805.

[189] A. M. Odlyzko, N. J. A. Sloane and H. N. Ward, Self-dual codes over GF(4), JCT

A 25 (1978), 288–318
 126

[190] and N. J. A. Sloane, The Theory of Error-Correcting Codes, North-Holland, Ams-

terdam, 1977.

[191] and J. G. Thompson, Good self-dual codes exist, DM 3 (1972), 153–162.

[192] On the existence of a projective plane of order 10, JCT A 14 (1973),

66–78.

[193] C. L. Mallows, A. M. Odlyzko and N. J. A. Sloane, Upper bounds for modular forms,

lattices and codes, J. Algebra 36 (1975), 68–76.

[194] V. Pless and N. J. A. Sloane, Self-dual codes over GF (3), SIAM J. Appl. Math. 31

(1976), 649–666.

[195] and N. J. A. Sloane, On the invariants of a linear group of order 336, Proc. Camb.

Phil. Soc. 74 (1973) 435–440.

[196] An upper bound for self-dual codes, Information and Control 22 (1973), 188–

200.

[197] Weight enumerators of self-orthogonal codes, DM 9 (1974), 391–400.

[198] Weight enumerators of self-orthogonal codes over GF (3), SIAM J. Algebraic

and Discrete Methods 2 (1981), 425–460.

[199] R. J. McEliece, personal communication.

[200] G. A. Miller, H. F. Blichfeldt and L. E. Dickson, Theory and Applications of Finite

Groups, Dover, NY, 1961.

[201] J. Milnor and D. Husemoller, Symmetric Bilinear Forms, Springer-Verlag, NY, 1973.

[202] T. Molien, Ueber die invarianten der linear Substitutionsgruppe, Sitzungsber K¨onig.

Akad. Wiss., (1897), 1152–1156.

[203] E. H. Moore, Double Circulant Codes and Related Algebraic Structures, Ph.D. Disserta-

tion, Dartmouth College, July 1976.

[204] E. H. Moore, Using the group of a code to compute its minimal weights, preprint.

127

[205] D. Mumford and J. Fogarty, Geometric Invariant Theory, Springer-Verlag, NY, 2nd ed.,

1982.

[206] E. Noether, Der Endlichkeitsatz der Invarianten endlicher Gruppen, Math. Ann. 77

(1916), 89–92.

[207] H. Oral and K. T. Phelps, Almost all self-dual codes are rigid, JCT A 60 (1992), 264–276.

[208] M. Ozeki, On the basis problem for Siegel modular forms of degree 2, Acta Arith. 31

(1976), 17–30.

[209] On even unimodular positive deﬁnite quadratic lattices of rank 32, Math. Z. 191

(1986), 283–291.

[210] On the conﬁgurations of even unimodular lattices of rank 48, Archiv Math. 46

(1986), 54–61.

[211] Hadamard matrices and doubly even self-dual error-correcting codes, JCT A 44

(1987), 274–287.

[212] Examples of even unimodular extremal lattices of rank 40 and their Siegel theta-

series of degree 2, J. Number Theory 28 (1988), 119–131.

[213] Ternary code construction of even unimodular lattices, in Theorie des Nombres,

Quebec 1987, Gruyter, Berlin, 1989, pp. 772–784.

[214] On the structure of even unimodular extremal lattices of rank 40, Rocky Mtn. J.

Math. 19 (1989), 847–862.

[215] On a class of self-dual ternary codes, Science Reports Hirosaki Univ. 36 (1989),

184–191.

[216] Quinary code construction of the Leech lattice, Nihonkai Math. J. 2 (1991), 155–

167.

[217] On intersection properties of extremal ternary codes, JCT, to appear.

[218] On the notion of Jacobi polynomials for codes, Math. Proc. Camb. Phil. Soc. 121

(1997), 15–30.
 128

[219] On covering radius and coset weight distributions of extremal binary self-dual codes

of length 40, Theoret. Comp. Sci., to appear.

[220] G. Pasquier, The binary Golay code obtained from an extended cyclic code over F8,

Europ J. Combinatorics 1 (1980), 369–370.

[221] A binary extremal doubly-even self-dual code [64, 32, 12] obtained from an extended

Reed-Solomon code over F16, PGIT 27 (1981), 807–808.

[222] Projections et images binaries de codes sur F2m , Rev. CETHEDEC 2 (1981), 45–56.

[223] Binary images of some self-dual codes over GF (2m) with respect to trace-orthogonal

basis, DM 37 (1981), 127–129.

[224] N. J. Patterson, personal communication, 1980.

[225] P. M. Piret, Algebraic construction of cyclic codes over Z8 with a good Euclidean mini-

mum distance, PGIT 41 (1995), 815–817.

[226] V. Pless, The number of isotropic subspaces in a ﬁnite geometry, Rend. Cl. Scienze

ﬁsiche, matematiche e naturali, Acc. Naz. Lincei 39 (1965), 418–421.

[227] On the uniqueness of the Golay codes, JCT 5 (1968), 215–228.

[228] On a new family of symmetry codes and related new ﬁve-designs, Bull. Amer. Math.

Soc. 75 (1969), 1339–1342.

[229] A classiﬁcation of self-orthogonal codes over GF (2), DM 3 (1972), 209–246.

[230] Symmetry codes over GF (3) and new ﬁve-designs, JCT A 12 (1972), 119–142.

[231] 23 does not divide the order of the group of a (72,36,16) doubly even code, PGIT

28 (1982), 113–117.

[232] The children of the (32,16) doubly even codes, PGIT 24 (1978), 738–746.

[233] A decoding scheme for the ternary Golay code, in Proc. 20th Allerton Conf. Comm.

Control., Univ. of Ill., Urbana, 1982, pp. 682–687.

[234] On the existence of some extremal self-dual codes, in D. M. Jackson and S. A.

Vanstone, editors, Enumeration and Design, Academic Press, 1984, pp. 245–250.

129

[235] Q-codes, JCT A 43 (1986), 258–276.

[236] Decoding the Golay codes, PGIT 32 (1986), 561–567.

[237] Extremal codes are homogeneous, PGIT 35 (1989), 1329–1330.

[238] Parents, children, neighbors and the shadow, Contemporary Math. 168 (1994),

279–290.

[239] J. S. Leon and J. Fields, All Z4 codes of Type II and length 16 are known, JCT A

78 (1997), 32–50.

[240] and J. N. Pierce, Self-dual codes over GF (q) satisfy a modiﬁed Varshamov-Gilbert

bound, Information and Control 23 (1973), 35–40.

[241] and Z. Qian, Cyclic codes and quadratic residue codes over Z4, PGIT 42 (1996),

1594–1600.

[242] and N. J. A. Sloane, On the classiﬁcation and enumeration of self-dual codes, JCT

A 18 (1975), 313–335.

[243] and H. N. Ward, Ternary codes of minimum weight 6 and the classiﬁcation of

self-dual codes of length 20, PGIT 26 (1980), 305–316.

[244] P. Sol´e and Z. Qian, Cyclic self-dual Z4-codes, Finite Fields Appl. 3 (1997), 48–69.

[245] and J. G. Thompson, 17 does not divide the order of a group of a (72,36,16) code,

PGIT 28 (1982), 537–541.

[246] and V. D. Tonchev, Self-dual codes over GF (7), PGIT 33 (1987), 723–727.

[247] and J. Leon, On the existence of a certain (64, 32, 12) extremal code, PGIT

39 (1993), 214–215.

[248] A. Poli and C. Rigoni, Enumeration of self-dual 2k circulant codes, Lect. Notes. Comput.

Sci. 228 (1986), 61–70.

[249] E. M. Rains, Nonbinary quantum codes, preprint.

[250] Shadow bounds for self-dual codes, 44 (1998), 134–139.

130

[251] Quantum shadow enumerators, preprint.

[252] Quantum weight enumerators, preprint.

[253] Polynomial invariants of quantum codes, preprint.

[254] Optimal self-dual codes over Z4, preprint.

[255] Bounds for self-dual codes over Z4, preprint.

[256] and N. J. A. Sloane, The shadow theory of modular and unimodular lattices,

preprint.

[257] S. J. Rallis, New and old results in invariant theory with applications to arithmetic

groups, in Symmetric Spaces, W. M. Boothby and G. L. Weiss, Eds., Dekker, NY, 1972,

pp. 443–458.

[258] M. Ran and J. Snyders, On maximum likelihood soft decoding of binary self-dual codes,

IEEE Trans. Commun. 41 (1993), 439–443.

[259] Constrained designs for maximum likelihood soft decoding of RM (2, m) and

the extended Golay codes, IEEE Trans. Commun. 43 (1995), 812–820.

[260] A cyclic [6, 3, 4] group code and the hexacode over GF (4), PGIT 42 (1996),

1250–1253.

[261] C. Reid, Hilbert, Springer-Verlag, NY, 1970.

[262] C.-G. Rota, Combinatorial Theory and Invariant Theory, Bowdoin College, 1971.

[263] B. Runge, On Siegel modular forms I, J. reine angew. Math. 436 (1993), 57–85.

[264] On Siegel modular forms II, Nagoya Math. J. 138 (1995), 179–197.

[265] Thetafunctions and Siegel-Jacobi forms, Acta Math. 175 (1995), 165–196.

[266] Codes and Siegel modular forms, DM 148 (1996), 175–204.

[267] R. P. Ruseva, Uniqueness of the [36, 18, 8] double circulant code, in Proc. Internat. Work-

shop on Optimal Codes and Related Topics, May 26–June 1, 1995, Sozopol, Bulgaria,

126–129.
 131

[268] New extremal self-dual codes of length 36, in Proc. of the 25th Spring Conf. of the

UBM, 1996, 150–153.

[269] On the extremal self-dual binary codes of length 38 with an automorphism of order

7, preprint.

[270] J. A. Rush, A lower bound on packing density, Invent. Math. 98 (1989), 499–509.

[271] A bound, and a conjecture, on the maximum lattice-packing density of a superball,

Mathematika 40 (1993), 137–143.

[272] and N. J. A. Sloane, An improvement to the Minkowski-Hlawka bound for packing

superballs, Mathematika 34 (1987), 8–18.

[273] R. A. Sack, Interpretation of Lagrange’s expansion and its generalization to several vari-

ables as integration formulas, J. SIAM 13 (1965), 47–59.

[274] Generalization of Lagrange’s expansion for functions of several implicitly deﬁned

variables, J. SIAM 13 (1965), 913–926.

[275] Factorization of Lagrange’s expansion by means of exponential generating functions,

J. SIAM 14 (1966), 1–15.

[276] W. Scharlau and D. Schomaker, personal communication, April 1991.

[277] J.-P. Serre, Linear Representations of Finite Groups, Springer-Verlag, NY, 1977.

[278] P. Shankar, On BCH codes over arbitrary integer rings, PGIT 25 (1979), 480–483.

[279] G. C. Shephard and J. A. Todd, Finite unitary reﬂection groups, Canad. J. Math. 6

(1954), 274–304.

[280] K. Shiromoto, A new MacWilliams type identity for linear codes, Hokkaido Math. J. 25

(1996), 651–656.

[281] P. W. Shor and R. Laﬂamme, Quantum analog of the MacWilliams identities in classical

coding theory, Phys. Rev. Lett. 78 (1997), 1600–1602.

[282] N. J. A. Sloane, Is there a (72, 36) d = 16 self-dual code?, PGIT 19 (1973), 251.

132

[283] Weight enumerators of codes, in Combinatorics, M. Hall Jr. and J. H. van Lint,

Eds., Mathematical Centre, Amsterdam and Reidel Publishing Co., Dordrecht, Holland,

1975, pp. 115–142.

[284] Error-correcting codes and invariant theory: New applications of a nineteenth-

century technique, Amer. Math. Monthly 84 (1977), 82–107.

[285] Binary codes, lattices and sphere-packings, in Combinatorial Surveys: Proceedings

of the Sixth British Combinatorial Conference, P. J. Comeron, Ed., Academic Press, NY,

1977, pp. 117–164.

[286] Codes over GF (4) and complex lattices, J. Algebra 52 (1978), 168–181.

[287] Self-dual codes and lattices, in Relations Between Combinatorics and Other Parts

of Mathematics, Proc. Symp. Pure Math., Vol 34, American Mathematical Society, Prov-

idence, RI, 1979, pp. 273–308.

[288] and J. G. Thompson, Cyclic self-dual codes, PGIT 29 (1983), 364–366.

[289] L. Smith, Polynomial Invariants of Finite Groups, Peters, Wellesley, MA, 1995.

[290] Polynomial invariants of ﬁnite groups. A survey of recent developments, Bull. Amer.

Math. Soc. 34 (1997), 211–250.

[291] S. L. Snover, The uniqueness of the Nordstrom–Robinson and the Golay binary codes,

Ph.D. Dissertation, Department of Mathematics, Michigan State Univ., 1973.

[292] J. Snyders and Y. Be’ery, Maximum likelihood soft decoding of binary block codes and

decoders for the Golay codes, PGIT 35 (1989), 963–975.

[293] E. Spence and V. D. Tonchev, Extremal self-dual codes from symmetric designs, DM

110 (1992), 265–268.

[294] T. A. Springer, Invariant Theory, Lect. Notes. Math. 585, Springer-Verlag, NY, 1977.

[295] R. P. Stanley, personal communication.

[296] Invariants of ﬁnite groups and their applications to combinatorics, Bull. Amer.

Math. Soc. 1 (1979), 475–511.
 133

[297] D. Stanton, editor, Invariant Theory and Tableaux, Springer-Verlag, NY, 1990.

[298] B. Sturmfels, Algorithms in Invariant Theory, Springer-Verlag, NY, 1993.

[299] J. G. Thompson, Weighted averages associated to some codes, Scripta Math. 29 (1973),

449-452.

[300] V. D. Tonchev, Block designs of Hadamard type and self-dual codes, Probl. Pered. In-

form. 19 (1983), No. 4, 25–30; English translation in Prob. Inform. Trans. 19 (1983),

270–274.

[301] On the inequivalence of certain extremal self-dual codes, Compt. Rend. Acad. Bulg.

Sci. 36 (1983) 181–184.

[302] Quasi-symmetric designs and self-dual codes, European J. Combin. 7 (1986) 67–73.

[303] Combinatorial Conﬁgurations, Longman, London, 1988.

[304] Symmetric designs without ovals and extremal self-dual codes, Ann. Discr. Math.

37 (1988) 451–458.

[305] Self-orthogonal designs and extremal doubly-even codes, JCT A 52 (1989), 197–

205.

[306] Self-orthogonal designs, Contemporary Math. 111 (1990), 219–235.

[307] Self-dual codes and Hadamard matrices, Discr. Appl. Math. 33 (1991), 235–240.

[308] and R. V. Raev, Cyclic 2-(17, 8, 7) designs and related doubly even codes, Comput.

Rend. Acad. Bulg. Sci. 35 (1982).

[309] and V. Y. Yorgov, The existence of certain extremal [54, 27, 10] self-dual codes,

PGIT 42 (1996), 1628–1631.

[310] H.-P. Tsai, Existence of certain extremal self-dual codes, PGIT 38 (1992), 501–504.

[311] Existence of some extremal self-dual codes, PGIT 38 (1992), 1829–1833.

[312] The covering radius of extremal self-dual code D11 and its application, PGIT 43

(1997), 316–319.
 134

[313] J. V. Uspensky, Theory of Equations, McGraw-Hill, NY, 1948.

[314] A. Vardy, The Nordstrom-Robinson code: representation over GF (4) and eﬃcient de-

coding, PGIT 40 (1994), 1686–1693.

[315] Even more eﬃcient bounded-distance decoding of the hexacode, the Golay code,

and the Leech lattice, PGIT 41 (1995), 1495–1499.

[316] and Y. Be’ery, More eﬃcient soft-decision decoding of the Golay codes, PGIT 37

(1991), 667–672.

[317] M. Ventou and C. Rigoni, Self-dual doubly circulant codes, DM 56 (1985), 291–298.

[318] G. E. Wall, On Cliﬀord collineation, transform and similarity groups IV, Nagoya Math.

J. 21 (1962), 199–222.

[319] H. N. Ward, A restriction on the weight enumerator of self-dual codes, JCT 21 (1976),

253–255.

[320] Divisible codes, Archiv Math. (Basel) 36 (1981), 485–494.

[321] personal communication.

[322] A bound for divisible codes, PGIT 38 (1992), 191–194.

[323] and J. A. Wood, Characters and the equivalence of codes, JCT A 73 (1996), 348–

352.

[324] A. Weil, Sur certaines groupes d’op´erateurs unitaires, Acta Math. 11 (1964), 143–211.

[325] H. Weyl, Invariants, Duke Math. J. 5 (1939), 489–502.

[326] The Classical Groups, Princeton Univ. Press, Princeton, NJ, 1946.

[327] E. T. Whittaker and G. N. Watson, A Course of Modern Analysis, Cambridge Univ.

Press, 4th ed., 1963.

[328] J. Wolfmann, A new construction of the binary Golay code [24, 12, 8] using a group

algebra over a ﬁnite ﬁeld, DM 31 (1980), 337-338.

[329] A class of doubly even self-dual binary codes, DM 56 (1985), 299–303.

135

[330] A group algebra construction of binary even self-dual codes, DM 65 (1987), 81–89.

[331] J. A. Wood, Duality for modules over ﬁnite rings and applications to coding theory, 1996,

submitted to Amer. J. Math.

[332] V. Y. Yorgov, Binary self-dual codes with automorphisms of odd order, Probl. Pered.

Inform. 19 (1983); English translation in Prob. Inform. Trans. 19 (1983), 11–24.

[333] A method for constructing inequivalent self-dual codes with applications to length

56, PGIT 33 (1987), 77–82.

[334] Doubly-even codes of length 64, Probl. Pered. Inform. 22 (1986), 35–42; English

translation in Prob. Inform. Trans. 22 (1986), 277–284.

[335] and R. Ruseva, Two extremal codes of length 42 and 44, Probl. Pered. Inform. 29

(1993), 99–103; English translation in Prob. Inform. Trans. 29 (1994), 385–388.

[336] and N. Yankov, On the extremal binary codes of lengths 36 and 38 with an automor-

phism of order 5, Proc. of the 5th International Workshop on Algebraic and Combinatorial

Coding Theory, June 1–7, 1996, Sozopol, Bulgaria, 307–312.

[337] and N. P. Ziapkov, Doubly-even self-dual [40, 20, 8] codes with an automorphism of

odd order, Probl. Pered. Inform. 32 (1996), 41–46; English translation in Prob. Inform.

Trans. 32 (1996), 253–257.

[338] S. Zhang, On the nonexistence of extremal self-dual codes, preprint, 1997.

136
