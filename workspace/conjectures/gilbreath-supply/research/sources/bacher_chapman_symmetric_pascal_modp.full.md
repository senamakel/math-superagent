<!-- source: https://arxiv.org/pdf/math/0212144 | converted from PDF -->

arXiv:math/0212144v2  [math.NT]  31 Jan 2003
Symmetric Pascal matrices modulo p

Roland Bacher∗and Robin Chapman

30 January 2003

1 Introduction

This paper presents results and conjectures concerning symmetric matrices
associated to Pascal’s triangle. We ﬁrst give a formula for the determinant
over Z of the reduction modulo 2 with values in {0, 1} for such a matrix. We
then study the reduction modulo a prime p of the characteristic polynomials
of these matrices. Our main results imply a formula for the prime p = 2
and a conjectural formula for p = 3.
Consider the symmetric matrix P (n) with coeﬃcients

pi,j =
 (i + j
i
 )
, 0 ≤ i, j < n .

We call P (n) the symmetric Pascal matrix of order n. The entries of P (n)
satisfy the recurrence pi,j = pi−1,j + pi,j−1.

In [2] the ﬁrst author studied the determinant of the general matrix with
entries satisfying this recurrence.
An easy computation yields P (∞) = T T t where T is the inﬁnite unipo-
tent lower triangular matrix

T =
 








 1
1 1
1 2 1
1 3 3 1
... . . .
 







 = exp
 








 0
1 0
0 2 0
0 3 0 . . .
 









with coeﬃcients ti,j = (i
j)
. This shows that det(P (n)) = 1 and that P (n)
is positive deﬁnite for all n ∈ N. Hence all zeroes of the characteristic
polynomial χn(t) = det(tI(n) − P (n)) (where I(n) denotes the identity

∗Support from the Swiss National Science Foundation is gratefully acknowledged.

1

matrix of size n) of P (n) are positive reals. The inverse P (n)−1 of P (n) is
given by
 P (n)
−1 = (
T (n)
t)−1 T (n)
−1

and T (n)−1 has coeﬃcients (−1)i+j (i
j)
, 0 ≤ i, j < n. Hence T (n) and
T (n)−1 are conjugate, and thus also P (n) and P (n)−1 are conjugate. The
characteristic polynomial χn(t) therefore satisﬁes χn(t) = (−t)nχ(1/t) and
1 is always an eigenvalue of P (2n + 1), cf. [4]. The polynomials χn(t),
especially their behaviour modulo primes, will be our main object of study.
For convenience, we write I for I(n) whenever the size of the identity matrix
is unambiguous.
Deﬁne P (n)2 as the reduction modulo 2 of P (n) with values in {0, 1} by
setting
 pi,j =
 ((i + j
i
 )
 (mod 2)

)
 ∈ {0, 1} .

The Thue-Morse sequence sn = ∑ νi (mod 2) counts the parity of all
non-zero digits of a binary integer n = ∑ νi2i. It can also be deﬁned recur-
sively by s0 = 0, s2k = sk and s2k+1 = 1 − sk (cf. for instance [1]).

Theorem 1.1 The determinant (over Z) of P (n)2 is given by

det(P (n)2) =
 n−1∏

k=0(−1)
sk .

A similar result holds for the reduction modulo 3 of P (n) with values in
{−1, 0, 1}.
In the sequel, we will be interested in the characteristic polynomial
det(tI − P (n)) (mod p) for p a prime number. The next result yields a
formula for n = pl and is of crucial importance in the sequel.

Proposition 1.2 Given a power q = pl of a prime p, the matrix P (q) has
order 3 over Fp. Its characteristic polynomial χq(t) = det(tI(q) − P (q))
satisﬁes χq(t) ≡ (t2 + t + 1) q−ǫ(q)
3 (t − 1) q+2ǫ(q)
3 (mod p)

where ǫ(q) ∈ {−1, 0, 1} satisﬁes ǫ(q) ≡ q (mod 3).

In particular, P (q) can be diagonalized over Fp2 except when p = 3. For
instance, P (3) has a unique Jordan block over F3.
This proposition (except for the diagonalization part) admits the follow-
ing generalization:

Theorem 1.3 When q = pl is a power of a prime p and 0 ≤ k ≤ q/2 then

χq−k(t) ≡ (t2 + t + 1)
(q−ǫ(q))/3−k(t − 1)
(q+2ǫ(q))/3−k det(t2I + P (k)) (mod p)

where ǫ(q) ∈ {−1, 0, 1} satisﬁes ǫ(q) ≡ q (mod 3).

2

Theorem 1.3 completely determines the reduction modulo 2 of χn(t) as
follows: Deﬁne a sequence γ(0) = 0, γ(1), . . . recursively by

γ(2
l − k) = 2l + 2(−1)l

3 − k + 2γ(k), 0 ≤ k ≤ 2
l−1 .

Theorem 1.4 For all n ∈ N

χn(t) ≡ (t + 1)
γ(n)(t2 + t + 1)
γ2(n) (mod 2)

where γ2(n) = 1
2 (n − γ(n)).

It follows immediately that the matrix I − P (n)3 is nilpotent over F2 for
all n ∈ N.
The ﬁrst terms γ(1), . . . , γ(32) and γ2(1), . . . , γ2(32) are given by

n 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
γ(n) 1 0 3 2 5 0 3 2 5 0 11 6 9 4 7 6
γ2(n) 0 1 0 1 0 3 2 3 2 5 0 3 2 5 4 5
n 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32
γ(n) 9 4 15 10 21 0 11 6 9 4 15 10 13 8 11 10
γ2(n) 4 7 2 5 0 11 6 9 8 11 6 9 8 11 10 11

The sequence γ(0), γ(1), . . . has many interesting arithmetic features.
In order to describe them, let us introduce the number b(n) of “blocks”
of adjacent ones in the binary representation of a positive integer n. For
instance 667 = (1010011011)2 and so b(667) = 4. Notice that b(2n) = b(n)
and b(2n + 1) = b(n) + 1 − (n (mod 2)) (with n (mod 2) ∈ {0, 1}). This,
together with b(0) = 0, deﬁnes the sequence b(n) recursively.

Theorem 1.5 (i) We have

γ(2
l + k) = 2l + 2(−1)l

3 − k + 4γ(k)

for all 0 ≤ k ≤ 2l−1.
(ii) We have for all n ∈ N and 2l−2 ≤ k ≤ 2l−1

γ(2
l − k) = γ(k) + 2γ(2
l−1 − k) .

(iii) We have

γ(2
l + k) = 1 + γ(2
l + k − 1) + 2γ(2
l − k) − 2γ(2
l + 1 − k)

for 1 ≤ k ≤ 2l.
(iv) We have

γ(2n) = n − γ(n) ,
γ(2n − 1) = γ(2n) + (4b(2n−1) − 1)/3 = n − γ(n) + (4b(2n−1) − 1)/3 ,
γ(2n + 1) = γ(2n) + (21+2b(n) + 1)/3 = n − γ(n) + (21+2b(n) + 1)/3 .

3

Part (iv) of this Theorem gives an alternative recursive deﬁnition of the
sequence (γ(n)).
Theorem 1.3 seems to have many generalizations. A ﬁrst one is given by
the following:

Conjecture 1.6 For each integer k ≥ 0 there exists a monic polynomial
ck(t) ∈ Z[t] of degree 4k such that ck(t) = t4kck(t−1) with the following
property: if q is a power of a prime p, and 0 ≤ k ≤ q/2 then

χq+k(t) ≡ (t2 + t + 1)
(q−ǫ(q))/3−k(t − 1)
(q+2ǫ(q))/3−k ck(t) (mod p)

where ǫ(q) ∈ {−1, 0, 1} satisﬁes ǫ(q) ≡ q (mod 3).

The ﬁrst few of these conjectural polynomials ck(t) are

c0(t) = 1,

c1(t) = t4 − 2t3 − 2t + 1,

c2(t) = t8 − 6t7 + 4t6 − 4t5 + 15t4 − 4t3 + 4t2 − 6t + 1,

c3(t) = (t4 − 2t3 − 2t + 1)(t8 − 16t7 + 4t6 − 4t5 + 40t4 − 4t3 + 4t2 − 16t + 1),

c4(t) = t16 − 58t15 + 288t14 − 240t13 + 393t12 − 1440t11 + 836t10 − 902t9

+ 2376t8 − 902t7 + · · · − 58t + 1,

c5(t) = c1(t)(t16 − 196t15 + 2112t14 − 792t13 + 1290t12 − 10560t11

+ 2768t10 − 2972t9 + 17424
8 − 2972t7 + · · · − 196t + 1).

For p = 2, it follows from Theorem 1.4 and assertion (ii) in Theorem 1.5
that if ck(t) exists then

ck(t) ≡ (det(tI + P (k)))4 (mod 2).

Computations suggest:

Conjecture 1.7 We have

ck(t) ≡ (t + 1)
3k det(tI + P (k)) (mod 3) .

This conjecture, together with Theorem 1.3 yields conjectural recursive
formulas for pn(t) = det(tI(n) − P (n)) (mod 3) as follows: Set p0(t) = 1
(mod 3), p1(t) = 1 − t (mod 3). For n = 3l ± k > 1 with 0 ≤ k < 3l
2 the
characteristic polynomial χn(t) (mod 3) is then conjecturally given by

(t − 1)
3l−3k det(t2I + P (k)) if n = 3
l − k ,
(t − 1)
3l−3k (t + 1)
3k det(tI + P (k)) if n = 3
l + k .

In particular, all roots of χn(t) modulo 3 should be of multiplicative order
a power of 2 in the algebraic closure of F3.
We conclude ﬁnally by mentioning a last conjectural observation:

4

Conjecture 1.8 Given a prime-power q = pl ≡ 2 (mod 3), we have

χ(q+1)/3(t) ≡ (t + 1)
(q+1)/3 (mod p)

and χ(2q−1)/3(t) ≡ (t + 1)
(q+1)/3 (t − 1)
(q−2)/3 (mod p).

Remark 1.9 (i) The matrix C = P ( q+1
3 ) + I( q+1
3 ) for q = pl ≡ 2 (mod 3)
a prime-power, appears to have a unique Jordan block of maximal length
over Fp. If so, the rows of C (q+1)/6 generate a self-dual code over Fp.
(ii) Given a prime power q = pl ≡ 2 (mod 3) as above we set n = 2q+2
3
and k = 2q−1
3 . We conjecture that the characteristic polynomial of the matrix
˜Pk(n) with coeﬃcients

˜pi,j =
 (i + j + 2k
i + k
 )
, 0 ≤ i, j < n

satisﬁes det(tI − ˜Pk(n)) ≡ (1 + t)n (mod p).

Remark 1.10 In [3, Theorems 32 and 35] Krattenthaler gives evaluations
of determinants related to ours, namely of det(ωI + Q(n)) where ω is a sixth
root of unity, and Q(n) has entries (2µ+i+j
j ) (0 ≤ i, j < n).

The sequel of this paper is organized as follows:
Section 2 is devoted to autosimilar matrices. Such matrices generalize
the matrix P (∞)2 and their properties imply easily Theorem 1.1.
Section 3 contains proofs of Proposition 1.2 and Theorem 1.3.
Section 4 contains proofs of Theorems 1.4 and 1.5.

2 Autosimilar matrices

Let b ≥ 1 be a natural integer. An inﬁnite matrix M with coeﬃcients mi,j
(i, j ≥ 0) is b-autosimilar if m0,0 = 1 and if

ms,t = ∏

i mσi,τi

where the indices s = ∑ σibi, t = ∑ τibi are written in base b, that is,
σi, τi ∈ {0, . . . , b − 1} for all i = 0, 1, 2, . . ..
We denote by M (n) the ﬁnite sub-matrix of M with coeﬃcients mi,j, 0 ≤
i, j < n. A b-autosimilar matrix M is non-degenerate if the determinants

det(M (n))

are invertible for n = 2, . . . , b.
 5

Theorem 2.1 Let b ≥ 2 be an integer and let M be a b-autosimilar matrix
which is non-degenerate. One has then a factorization

M = LDU

where L, D, U are b-autosimilar and where L is unipotent lower-triangular,
D is diagonal and U is unipotent upper-triangular.

Corollary 2.2 Given a non-degenerate b-autosimilar matrix M one has

det(M (n)) =
 n−1∏

i=0 dνi

for all n = ∑ νibi with d0 = 1 and

dk = det(M (k + 1))/ det(M (k))

for k = 1, . . . , b − 1.

Remark 2.3 In general, one can compute determinants of arbitrary b-autosimilar
matrices over a ﬁeld K by applying Corollary 2.2 to the b-autosimilar matrix
obtained from a generic perturbation of the form

Mt(b) = (1 − t)M (b) + tP (b)

(where P (b) is a suitable matrix) and working over the rational function
ﬁeld K(t).

Proof of Theorem 2.1. The genericity of M implies that

M (b) = L(b)D(b)U (b)

where L(b) and U (b) are unipotent upper and lower triangular matrices
and the diagonal matrix D(b) has entries d0,0 = 1 and dk,k = det(M (k +
1))/ det(M (k)) for k = 1, . . . , b − 1. Extending L(b), D(b) and U (b) in the
unique possible way to inﬁnite b-autosimilar matrices L, D and U we have

(LDU )s,t = ∑

k Ls,kDk,kUk,t

= ∑

k=∑ κibi
 ∏

i Lσi,κiDκi,κiUκi,τi

= ∏

i
 b−1∑

κi=0 Lσi,κiDκi,κiUκi,τi

= ∏

i Mσi,τi = Ms,t

for all s = ∑ σibi, t = ∑ τibi ∈ N. ✷
The identity det(M (n)) = det(D(n))

implies immediately Corollary 2.2.
 6

2.1 Binomial coeﬃcients modulo a prime p

Let p be a prime number. We have then

(1 + x)
n = ∏
(1 + x)
νipi ≡ (1 + xpi)
νi (mod p)

(using properties of the Frobenius automorphism in characteristic p). This
implies immediately the equality
(n
k
)
 = ∏

i
 (νi
κi
)

allowing (for small primes) an eﬃcient computation of binomial coeﬃcients
(mod p).
This equality shows that the reductions modulo 2 or 3 of the symmetric
Pascal triangle P with coeﬃcients

pi,j =
 ((i + j
i
 )
 (mod 2)

)
 ∈ {0, 1}

respectively
 pi,j =
 ((i + j
i
 )
 (mod 3)

)
 ∈ {−1, 0, 1}

are 2− (respectively 3−) autosimilar matrices.
For p = 2 we have
( 1 1
1 0
 )
 =
 ( 1 0
1 1
 ) ( 1 0
0 −1
 ) ( 1 1
0 1
 )

which yields d0 = 1, d1 = −1 and Corollary 2.2 implies now Theorem 1.1.

Remark 2.4 One can show that the inverse of the integral matrix P (n)2
considered in Theorem 1.1 has all its coeﬃcients in {−1, 0, 1} for all n.

For p = 3 we have



 1 1 1
1 −1 0
1 0 0
 


 =
 


 1 0 0
1 1 0
1 1
2 1
 



 


 1 0 0
0 −2 0
0 0 − 1
2
 



 


 1 1 1
0 1 1
2
0 0 1
 




This shows that det(P (n)3) (over Z) equals (−2)a−b where a and b are the
number of digits 1 and 2 needed in order to write all natural integers < n
in base 3.
 7

3 Proofs of Proposition 1.2 and Theorem 1.3

Proof of Proposition 1.2 Let R be a commutative ring, and let

A =
 ( a b
c d
 )
 ∈ GL(2, R).

Then A determines a (graded R-algebra) automorphism φA of R[X, Y ] via
φA(X) = aX + bY and φA(Y ) = cX + dY , or alternatively
( φA(X)
φA(Y )
 )
 = A
 ( X
Y
 )
 .

It is easy to see that φA ◦ φB = φBA. Each φA restricts to an R-module
automorphism of the homogeneous polynomials R[X, Y ]n−1 of degree n − 1.
Let A(n) denote the matrix of this endomorphism with respect to the basis
X n−1, X n−2Y , X n−3Y 2, . . . , Y n−1, that is









 φA(X n−1)
φA(X n−2Y )
φA(X n−3Y 2)
...
φA(Y n−1)
 







 = A
(n)
 








 X n−1

X n−2Y
X n−3Y 2
...
Y n−1
 







 .

Then A(n) ∈ GL(n, R) and (AB)(n) = A(n)B(n). (Another way of expressing
this is to say that A(n) is the (n − 1)-th symmetric power of A.)
Let us specialize to the case R = Fp = Z/pZ and n = pl. In this case
A(n) = I if and only if A is a scalar matrix. The matrix

A =
 ( 1 −1
1 0
 )

yields A(n) ≡ P (pl) (mod p). Since A3 = −I, the matrix A(n) has order 3.
Let us now compute the multiplicities of the three eigenvalues of P =
P (p) (mod p) over Fp (the formula for P (pl) is then a straightforward
consequence of the fact the P (pl) is the l−fold Kronecker product of P (p)
with itself).
The easy identity (2k
k ) = ((p−1)/2
k )
(−4)k (mod p) for p an odd prime
and 0 ≤ k ≤ (p − 1)/2 shows

(p−1)/2∑

k=0
 (
2k
k
 ) ( −x
4
 )k ≡ (1 + x)
(p−1)/2 (mod p)

and yields tr(P ) ≡ (−3)(p−1)/2 ≡ ǫ(p) (mod p) (where ǫ(p) ∈ {−1, 0, 1}
satisﬁes ǫ(p) ≡ p (mod 3)) by quadratic reciprocity.

8

Since the characteristic polynomial for P has antisymmetric coeﬃcients
(αk = −αp−k) the two eigenvalues ̸= 1 of P have equal multiplicity r. Lifting
into positive integers ≤ p−1
2 the solution of the linear system −r + (p − 2r) ≡
tr(P ) (mod p) yields now the result.
The case p = 2 is easily solved by direct inspection. ✷

Remark 3.1 Recall that we have (with the notations of the above proof )
P = P (n) = A(n) (mod p) for n = pl and introduce L = L(n) = B(n)

(mod p) and ˜L = ˜L(n) = C (n) (mod p) where

A =
 ( 1 −1
1 0
 )
 , B =
 ( 1 0
−1 −1
 )
 , C =
 ( 1 0
1 −1
 )
 .

It is straightforward to check that L and ˜L have coeﬃcients

li,j = (−1)
i(i
j
)
 (mod p) and ˜li,j = (−1)
j (i
j
)
 (mod p)

for 0 ≤ i, j < n.
Then A3 = −I, but (−I)(n) is the identity. Hence P 3 = I. Also C 2 = I
and CAC = A−1. It follows that A and C generate a dihedral group of order
12, containing −I. Hence A(n) = P and C (n) = ˜L generate a dihedral group
of order 6.
The group Gp generated by P and L depends on the prime p (but not on
the power l of n = pl). It is isomorphic to a subgroup of PGL2(Fp). For
all but ﬁnitely many primes p, Gp is isomorphic to PSL2(Fp) or PGL2(Fp)
according to whether −1 is or is not a square in Fp. The exceptional primes
are 5, 7 and 29 where Gp has order 24, 42 and 120 respectively.

Proof of Theorem 1.3 Using Proposition 1.2, we can rewrite the equation
to be proved as

(t3 − 1)
k det(tI − P (q − k)) ≡ det(tI − P (q)) det(t2I + P (k)) (mod p).

Here, and in the sequel, we write I for I(n) whenever this notation is un-
ambiguous; also we denote the zero matrix of any size by O.
We now work over the ﬁeld Fp. Unless otherwise stated vectors will be
row vectors.
It is convenient to deﬁne a category E = EFp as follows. Its objects will
be pairs (V, α) where V is a ﬁnite-dimensional vector space over Fp and α
is a vector space endomorphism of V . A morphism φ : (V, α) → (W, β)
in E will be a linear map φ : V → W with φ ◦ α = β ◦ φ. (In fact E
is equivalent to the category of ﬁnitely generated torsion modules over the
polynomial ring Fp[X].) If (V, α) is an object of E we deﬁne χ(V, α, t) as the
characteristic polynomial of α acting on V , that is, χ(V, α, t) = det(tI − A)

9

where A is a matrix representing α with respect to some basis of V . An r
by r matrix A deﬁnes an object ((Fp)r, α), denoted by ((Fp)r, A), where α
is the endomorphism deﬁned by A.
It is easy to see that E is an abelian category, and that if

0 → (V, α) → (X, γ) → (W, β) → 0

is a short exact sequence, then χ(X, γ, t) = χ(V, α, t)χ(W, β, t). This is
because there is a basis for X with respect to which the matrix of γ (acting
on row vectors from the the right) is
( A O
C B
 )

where A and B are matrices representing α and β respectively.
Set k′ = q − k. We can partition the Pascal matrices P (k′) and P (q) as
follows:
 P (k′) =
 ( A B
Bt C
 )
 and P (q) =
 


 A B D
Bt C O
Dt O O
 




where A = P (k).
Let A denote the matrix obtained by rotating A through 180◦. Then
P (q)2 = P (q) and P (q)3 = I. Hence

P (q)
2 =
 


 O O Dt

O C Bt

D B A
 


 .

Thus A
2 + BBt + DDt = O

and so
 P (k′)
2 =
 ( −DDt O
O C
 )
 .

From P (q)2 = P (q) it follows that AD = Dt and from P (q)P (q) = I it
follows that DtDt = I. Hence ADDt = I and so

P (k′)
2 =
 ( −A−1 O
O C
 )
 .

Let V = (Fp)q and X = (Fp)3k. Let

Q1 =
 


 O I(k) O
O O I(k)
I(k) O O
 


 .

10

Let φ : X → V be the map deﬁned by the matrix



 I O O
A B D
O O Dt
 


 .

Then
 Q1
 


 I O O
A B D
O O Dt
 


 =
 


 A B D
O O Dt

I O O
 




and



 I O O
A B D
O O Dt
 


 P (q) =
 


 I O O
A B D
O O Dt
 



 


 A B D
Bt C O
Dt O O
 


 =
 


 A B D
O O Dt

I O O
 




where we have used the formulas P (q)2 = P (q) and P (q)P (q) = I. Hence φ
is a morphism from ((Fp)3k, Q1) to ((Fp)q, P (q)) in E.
Let W = (Fp)k′ and Y = (Fp)2k. Let

Q2 =
 ( O I(k)
−A−1 O
 )
 .

Let ψ : Y → W be the map deﬁned by the matrix
( I O
A B
 )
 .

Then
 Q2
 ( I O
A B
 )
 =
 ( A B
−A−1 O
 )

and ( I O
A B
 )
 P (k′) =
 ( I O
A B
 ) ( A B
Bt C
 )
 =
 ( A B
−A−1 O
 )

where we have used the formula

P (k′)
2 =
 ( −A−1 O
O C
 )
 .

Hence ψ is a morphism from ((Fp)2k, Q2) to ((Fp)k′, P (k′)) in E.
We need to divide into the cases k ≤ q/3 and k ≥ q/3. In the former
cases φ and ψ are injective and in the latter case they are surjective. In the
former case we consider their cokernels, in the latter case their kernels.

11

The matrix B has size k by q −2k. If B has rank k (which is only possible
if k ≤ q/3) then φ and ψ are injective. If B has rank q − 2k (which is only
possible if k ≥ q/3) then φ and ψ are surjective.
The matrix B contains a submatrix
((i + j + k
i
 ))r−1

i,j=0

where r = min(k, q − 2k). This submatrix has determinant 1 (consider it as
a matrix over Z and reduce it to a Vandermonde matrix or see for instance
[2]). Thus B has rank r and indeed φ and ψ are injective for k ≤ q/3 and
surjective for k ≥ q/3.
Consider ﬁrst the case where k ≤ q/3. Let (X1, θ1) and (X2, θ2) denote
the cokernels of φ : ((Fp)3k, Q1) → ((Fp)q, P (q)) and ψ : ((Fp)2k, Q2) →
((Fp)k′, P (k′)) in E. Then

χ((Fp)
q, P (q), t) = χ((Fp)
3k, Q1, t)χ(X1, θ1, t)

and χ((Fp)
k′, P (k′), t) = χ((Fp)
2k, Q2, t)χ(X2, θ2, t).

It is apparent that χ((Fp)
3k, Q1, t) = (t3 − 1)
k

and χ((Fp)
2k, Q2, t) = det(t2I + A
−1) = det(t2I + A)

as A and A−1 are similar. Hence

det(tI − P (q)) = (t3 − 1)
kχ(X1, θ1, t)

and det(tI − P (k′)) = det(t2I + A)χ(X2, θ2, t).

It suﬃces to prove that (X1, θ1) and (X2, θ2) are isomorphic in E.
As Dt is nonsingular, it is apparent that X1 is isomorphic to (Fp)q−2k/Y
where Y is the row space of B and that the action of θ1 is induced by that of
the matrix C on (Fp)q−2k. It is even more apparent that X2 is isomorphic
to (Fp)q−2k/Y and that the action of θ2 is induced by C. Hence (X1, θ1)
and (X2, θ2) are isomorphic in E. This completes the argument in the case
k ≤ q/3.
Now suppose that k ≥ q/3. Let (K1, θ1) and (K2, θ2) denote the kernels
of φ : ((Fp)3k, Q1) → ((Fp)q, P (q)) and ψ : ((Fp)2k, Q2) → ((Fp)k′, P (k′)) in
E. Then χ((Fp)
q, P (q), t)χ(K1, θ1, t) = χ((Fp)
3k, Q1, t)

and χ((Fp)
k′, P (k′), t)χ(K2, θ2, t) = χ((Fp)
2k, Q2, t).

12

Hence (t3 − 1)k

det(tI − P (q)) = χ(K1, θ1, t)

and det(t2I + A)
det(tI − P (k′)) = χ(K2, θ2, t).

It suﬃces to prove that (K1, θ1) and (K2, θ2) are isomorphic in E.
As Dt is nonsingular and has inverse Dt, it is apparent that

K1 = {(−uA, u, −uDDt) = (−uA, u, −uA
−1) : u ∈ (Fp)
k, uB = 0}

and we have
 (−uA, u, −uA
−1)Q1 = (−uA
−1, −uA, u) .

Also K2 = {(−uA, u) : u ∈ (Fp)
k, uB = 0}

and (−uA, u)Q2 = (−uA
−1, −uA) .

Hence the linear map
 (−uA, u, −uA
−1) ↦−→ (−uA, u)

induces an isomorphism between (K1, θ1) and (K2, θ2). ✷

4 Proofs for the prime p = 2

Proof of Theorem 1.4. Set n = 2l − k and q = 2l where 1 ≤ k ≤ 2l−1.
Theorem 1.3 yields then over F2

χn(t) = χq−k(t) = (t2 + t + 1)
(q−ǫ(q))/3−k(t + 1)
(q+2ǫ(q))/3−k det(tI + P (k))
2

since x ↦−→ x2 is an automorphism in characteristic 2.
By induction on l, the only possible irreducible factors of det(tI(n) −
P (n)) (mod 2) are (1+t) and (1+t+t2). The multiplicity µ(n) = µ(2l −k)
of the factor (1 + t) in this polynomial is hence recursively deﬁned by

µ(n) = 2l + 2(−1)l

3 − k + 2µ(k)

and coincides hence with the sequence γ of Theorem 1.4. The remaining
factor of det(tI(n) − P (n)) (mod 2) is hence given by (1 + t + t2)γ2(n)

where γ2(n) = 1
2 (n − γ(n)) and this proves the result. ✷

13

Proof of Theorem 1.5. We have for 0 ≤ k ≤ 2l−1

γ(2
l + k) = γ(2
l+1 − (2
l − k))

= 2l+1 − 2(−1)l

3 − 2
l + k + 2γ(2
l − k)

= 2l+1 − 2(−1)l

3 − 2
l + k + 2 2l + 2(−1)l

3 − 2k + 4γ(k)

which is assertion (i).
We have for all 2l−2 ≤ k ≤ 2l−1

γ(2
l − k) = 2l + 2(−1)l

3 − k + γ(k) + γ(2
l−1 − (2
l−1 − k))

= 2l + 2(−1)l

3 − k + γ(k) + 2l−1 − 2(−1)l

3 − 2
l−1 + k + 2γ(2
l−1 − k)

= γ(k) + 2γ(2
l−1 − k)

which proves assertion (ii).
Similarly, we have for 1 ≤ k ≤ 2l

γ(2
l + k) − γ(2
l + k − 1) = γ(2
l+1 − (2
l − k)) − γ(2
l+1 − (2
l − k + 1))

= 1 + 2γ(2
l − k) − 2γ(2
l − k + 1)

which proves assertion (iii).
Writing 2n = 2l − 2k with 1 ≤ k ≤ 2l−2 we have, using induction on n,

γ(2
l − 2k) = 2l − (−1)l

3 − 2k + 2γ(2k)

= 2l − (−1)l

3 − 2k + 2 (k − γ(k))

= (2
l−1 − k) −
 ( 2l−1 − (−1)l−1

3 − k + 2γ(k)

)

= (2
l−1 − k) − γ(2
l−1 − k)

which proves the ﬁrst equality of assertion (iv) (this equality follows also
from the fact that P (2n) is the Kronecker product of P (n) with P (2)
over F2).
The second identity of assertion (iv) amounts to the equality

γ(2n − 1) − γ(2n) = 4b(2n−1) − 1
3 .

We prove ﬁrst by induction on n that this identity is equivalent to the last
identity.
 14

The last identity and induction yield

γ(2n − 1) − γ(2n) = γ(2n − 1) − γ(2n − 2) + γ(2n − 2) − γ(2n)

= 21+2b(n−1) + 1
3 − 1 + γ(n) − γ(n − 1).

We now divide into cases according to the parity of n.
Suppose ﬁrst that n = 2m is even. Then inductively

γ(n) − γ(n − 1) = γ(2m) − γ(2m − 1) = − 4b(2m−1)−1

3 = − 4b(n−1)−1

3
Hence

γ(2n − 1) − γ(2n) = −1 + 21+2b(n−1) + 1
3 − 22b(n−1) − 1
3 = 22b(n−1) − 1
3 .

But 2
2b(n−1) = 4
b(n−1) = 4
b(2n−1)

as the binary representation of n − 1 ends in 1 and that of 2n − 1 is obtained
by appending 1.
Now suppose that n = 2m + 1 is odd. Then

γ(n) − γ(n − 1) = γ(2m + 1) − γ(2m) = 21+2b(m) + 1
3 = 21+2b(2m) + 1
3 .

Hence(2n − 1) − γ(2n) = −1 + 21+2b(n−1) + 1

3 + 21+2b(n−1) + 1
3 = 22+2b(n−1) − 1
3 .

But 2
2+2b(n−1) = 4
1+b(n−1) = 4
b(2n−1)

as the binary representation of n − 1 ends in 0 and that of 2n − 1 is obtained
by appending 1.
This completes the proof of equivalence of the two last identities in as-
sertion (iv).
We prove now the last identity by induction on n.
The last identity of assertion (iv) is equivalent to

γ(2n + 1) − γ(2n) = 21+2b(n) + 1
3 .

Writing 2n + 1 = 2l + k with 1 ≤ k < 2l and applying assertion (iii) and the
second identity of assertion (iv) (which holds by induction) we have

γ(2n + 1) − γ(2n) = 1 + 2γ(2
l − k) − 2γ(2
l + 1 − k)

= 1 + 2 4b(2l−k) − 1
3

= 21+2b(2l−k) + 1
3

15

Since (2l + k − 1) + (2l − k) = 2l+1 − 1 and since 2l + k − 1 is even and
greater than 2l − k, they have the same number of blocks 1 . . . 1 in their
binary expansion. This shows b(2l − k) = b(2n) = b(n) and establishes the
last identity of assertion (iv). ✷

The ﬁrst author wishes to thank J.-P. Allouche, F. Sigrist, U. Vishne
and A. Wassermann for interesting comments and remarks.

References

[1] J.-P. Allouche, J. Shallit, The ubiquitous Prouhet-Thue-Morse sequence,
Proceedings of SETA 98 (C. Ding, T. Helleseth, H. Niederreiter, edi-
tors), Springer (1999).

[2] R. Bacher, Determinants of matrices related to the Pascal triangle, J.
de Th. des Nombres de Bordeaux 14 (2002), 19–41.

[3] C. Krattenthaler, Advanced determinant calculus, S´emin. Lothar.
Comb. 42, B42q (1999), 67 pages.

[4] W.F. Lunnon, The Pascal matrix, Fib. Quart. vol. 15 (1977), 201–204.

Roland Bacher, Institut Fourier, UMR 5582, Laboratoire de Math´ematiques,
BP 74, 38402 St. Martin d’H`eres Cedex, France, Roland.Bacher@ujf-grenoble.fr
Robin Chapman, University of Exeter, School of Mathematical Sciences,
North Park Road, EX4 4QE Exeter, UK, rjc@maths.ex.ac.uk

16
