<!-- source: https://arxiv.org/pdf/0708.1430 | converted from PDF -->

arXiv:0708.1430v3  [math.NT]  12 May 2008
Determinants related to Dirichlet characters
modulo 2, 4 and 8 of binomial coeﬃcients and the
algebra of recurrence matrices

Roland Bacher

Abstract: Using recurrence matrices, deﬁned and described with some
details, we study a few determinants related to evaluations of binomial co-
eﬃcients on Dirichlet characters modulo 2, 4 and 8. 1

1 Introduction

The aim of this paper is twofold: It contains computations of a few de-
terminants related to binomial coeﬃcients. The most interesting example,
discovered after browsing through [7], is obtained by considering binomial
coeﬃcients modulo 4. We include two similar examples taken from [2] and
[3]. The second topic discussed in this work are recurrence matrices, see [3]
for a very condensed outline. They are deﬁned as certain sequences of matri-
ces involving self-similar structures and they form an algebra. Computations
in the algebra of recurrence matrices are the main tool for proving the de-
terminant formulae mentionned above. Recurrence matrices are however of
independent interest since they are closely linked for example to automatic
sequences, see [1], to rational formal power series in free noncommuting
variables and to groups of automata, see [9] for the perhaps most important
example. The determinant calculations of this paper can thus be considered
as illustrations of some interesting features displayed by recurrence matrices.
The sequel of this paper is organised as follows:
The next section recalls mostly well-known facts concerning binomial
and q−binomial coeﬃcients and states the main results.
Section 3 deﬁnes the algebra R of recurrence matrices. It describes them
with more details than necessary for proving the formulae of Section 2.
Section 4 discusses a few features of the group of invertible elements in
R.
1Math. Class: 05A10,05A30,11B65,11B85,15-99 Keywords: binomial coeﬃcient,
q−binomial coeﬃcient, Dirichlet character, determinant, recurrence matrix

1

Section 5 proves formulae for the determinant of the reduction modulo
2 of the symmetric Pascal matrix (already contained in [2]) and of a deter-
minant related to the 2−valuation of the binomial coeﬃcients (essentially
contained in [3]).
Section 6 is devoted to the proof of our main result, a formula for
det(Z(n)) where Z(n) is the matrix with coeﬃcients χB(
(s+t
s )
) ∈ {0, ±1}, 0 ≤
s, t < n obtained by considering the “Beeblebrox reduction” (given by the
Dirichlet character χB(2m) = 0, χB(4m ± 1) = ±1 for m ∈ Z) of binomial
coeﬃcients. The proof uses an LU factorisation of the inﬁnite symmet-
ric matrix Z = Z(∞) and suggests to consider two (perhaps interesting)
groups ΓL and ΓZ whose generators display beautiful “self-similar” struc-
tures. This section ends with a short digression on the “lower triangular
Beeblebrox matrix” and the associated group.
Section 7 contains some data concerning the reduction of binomial coef-
ﬁcients by a Dirichlet character modulo 8 related to the Jacobi symbol.
Section 8 reproves a known formula for evaluating q−binomial coeﬃ-
cients at roots of unity. This formula yields easily formulae for some deter-
minants associated to the reduction modulo 2 and the Beeblebrox reduction
of (real and imaginary parts) of q−binomial coeﬃcients evaluated at q = −1
and q = i.

2 Main results

2.1 Reductions modulo 2

Let P (n) be the integral symmetric n × n matrix with coeﬃcients Ps,t ∈
{0, 1}, 0 ≤ s, t < n deﬁned by

Ps,t ≡ (s + t
s
 ) (mod 2)

where (s+t
s ) = (s+t)!
s! t! denotes the usual binomial coeﬃcient involved in the
expansion (x + y)n = ∑n
k=0 (n
k)xkyn−k.
The evaluation (s+t
s ) (mod 2) can be computed using a Theorem of Lu-
cas, see [11], page 52. Given a prime number p, it states that
(n
k
) ≡ ∏

j≥0
 (νj
κj
) (mod p)

where νi, κi ∈ {0, 1, . . . , p − 1} are the coeﬃcients of the p−ary expansion of
n = ∑j≥0 νjpj and k = ∑j≥0 κjpj. Another formula (due to Kummer) for
(n
k) (mod 2) will be presented in Section 2.2.

Let ds(n) = ∑⌊log2(n)⌋
j=0 νj ∈ N denote the digit-sum of a natural integer
with binary expansion n = ∑j≥0 νj2j, ν0, ν1, · · · ∈ {0, 1}.

2

Theorem 2.1. We have
 det(P (2n)) = (−1)
n

and det(P (2n + 1)) = (−1)
n+ds(n) .

Remark 2.2. The inﬁnite symmetric integral matrix ˜P with coeﬃcients
˜Ps,t = (s+t
s ) given by the binomial coeﬃcients is sometimes called the Fer-
mat matrix. Vandermonde’s identity ∑k=0 (s
k)(t
k) = ∑k=0 (s
k)( t
t−k) = (s+t
t )

shows that det( ˜P (n)) = 1 where ˜P (n) is the symmetric n × n submatrix with
coeﬃcients (s+t
s ), 0 ≤ s, t < n of ˜P .

2.2 2−valuations

Given a prime p, we denote by vp : Q∗ −→ N the p−valuation. Any rational
number α can thus be written in the form α = pvp(α) n
m with n, m ∈ Z
coprime to p. Let V (n) be the symmetric n × n matrix with coeﬃcients
Vs,t ∈ {±1, ±i} given by

Vs,t = i
v2((
s+t
s )), 0 ≤ s, t < n .

The p−valuation vp(
(s+t
s )) of a binomial coeﬃcient can be computed
using a Theorem of Kummer stating that vp(
(s+t
s )) equals the number of
carries occuring during the addition of the p−ary integers s = ∑j≥0 σjpj

and t = ∑j≥0 τjpj. More precisely, Kummer shows the identity

vp(x!) = 1
p − 1
 

x − ∑

j≥0 ξj




(see Lehrsatz, page 115 of [10]) where x = ∑j≥0 ξjpj ∈ N with ξj ∈
{0, 1, . . . , p − 1}. This implies the formula

vp(
(s + t
s
 )) = vp((s + t)!) − vp(s!) − vp(t!) = 1
p − 1
 ∑

j≥0(σj + τj − uj)

(see [10], page 116) where σj, τj, uj ∈ {0, 1, . . . , p − 1} are deﬁned by the
p−ary expansions s = ∑j≥0 σjpj, t = ∑j≥0 τjpj and s + t = ∑j≥0 ujpj.
The next result uses the regular folding sequence f : {1, 2, . . . } −→ {±1}.
It is deﬁned recursively by f (2n) = 1 and f (2n + a) = −f (2n − a) for
1 ≤ a < 2n, see for example [1].

Theorem 2.3. We have

det(V (2n)) = (−1)
n 2n−1∏

k=1 (1 − f (k)i) ∈ Z[i]

3

and
 det(V (2n + 1)) = (−1)
n+ds(n) 2n∏

k=1
(1 − f (k)i) ∈ Z[i]

(with ds(
∑j=0 νj2j) = ∑j≥0 νj denoting the binary digit-sum).

Remark 2.4. Let D denote the diagonal matrix with diagonal entries ids(0), ids(1), ids(2), . . . .
The paper [3] deals with the Hankel matrix H deﬁned by Hs,t = ids(s+t), 0 ≤
s, t related by H = DV D to the complex conjugate V of the matrix V in-
volved in Theorem 2.3.
Let us also mention that slight extensions of the computations occuring in
our proof of Theorem 2.3 establish the existence of nice continued J−fraction
expansions for the formal power series (cf. [3])

∞∏

k=0
(1 + ix2k ) ,

1
x
 ( 1 + i
2 + 1 − x
i − 1
 ∞∏

k=0
(1 + ix2k )

)
 ,

1
x2
 ( 1 + i
2 + i − 1
2 x + 1 − x2

i − 1
 ∞∏

k=0
(1 + ix2k )

)
 .

2.3 Beeblebrox reduction

The idea (and the “Beeblebrox” terminology) of considering the “Beeblebrox
reduction” of binomial coeﬃcients are due to Granville, see [7] and [8].
We deﬁne the “Beeblebrox reduction” as the Dirichlet character χB :
Z −→ {0, ±1} given by

χB(x) =
 



 0 if x ≡ 0 (mod 2)
1 if x ≡ 1 (mod 4)
−1 if x ≡ 3 (mod 4)

or equivalently by χB(2Z) = 0, χB(4Z ± 1) = ±1. Beeblebrox reduction is
the unique Dirichlet character modulo 4 not factorising through Z/2Z.
The following result allows fast computations of χB(
(n
k)
).

Theorem 2.5. We have

χB(
(2n
2k)) = χB(
(n
k)
)
χB(
( 2n
2k+1
)) = 0
χB(
(2n+1
2k )
) = (−1)k χB(
(n
k))
χB(
(2n+1
2k+1)
) = (−1)n(k+1) χB(
(n
k)
)

We denote by Z(n) (where the letter Z stands for Zaphod Beeblebrox,
following the amusing terminology of [7] and [8]) the symmetric Beeblebrox

4

matrix of size n × n with coeﬃcients Zs,t ∈ {−1, 0, 1} for 0 ≤ s, t < n given
by the Beeblebrox reduction Zs,t = χB(
(s+t
s )) of binomial coeﬃcients.
Deﬁne f : N −→ ±3Z by f (0) = 1, f (1) = −1 and recursively by

f (2
a + b) = { 3f (b) if 2b < 2a

1
3 f (b) otherwise

for n = 2a + b ≥ 2 where 0 ≤ b < 2a. Laurent Bartholdi pointed out that
the value f (n) of a binary integer n = ∑i≥0 νi2i is also given by

f (n) = (−1)
n3
♯{i | νi=0, νi+1=1}−♯{i | νi=νi+1=1}

= (−1)
n ∏

i≥0 3
(1−2νi)νi+1 .

Theorem 2.6. We have

det(Z(n)) =
 n−1∏

k=0 f (k) ∈ ±3
N .

2.4 The Jacobi-character modulo 8

Let χJ : N −→ {0, ±1} denote the Dirichlet character modulo 8 deﬁned by
χJ (2Z) = 0 and

χJ (n) = { 1 if n ≡ ±1 (mod 8) ,
−1 if n ≡ ±3 (mod 8) .

Since χJ (p) ≡ 2(p−1)/2 (mod 2) for p an odd prime, we call χJ the Jacobi-
character and we consider the matrix J(n) with coeﬃcients Js,t = χJ (
(s+t
s )
)
for 0 ≤ s, t < n. The techniques of this paper can be used to prove the
following result:

Theorem 2.7. We have

det(J(n)) =
 n−1∏

k=0 g(k) ∈ ±3
N

where g(n) = (−1)
n ∏

k≥0 3
e(⌊n/2k⌋)

with e(k) the 8−periodic function given by the table

k 0 1 2 3 4 5 6 7
e(k) 0 0 1 −1 0 −2 3 −1

5

The matrices Z(n) and J(n) share many features. However the consid-
erable greater complexity of all objects attached to J makes it more diﬃcult
to pin down interesting algebraic structures associated to J.
Let me also add that the remaining Dirichlet character modulo 8 (given
by ˜χ(2Z) = 0 and ˜χ(ǫa + 8Z) = ǫ for a ∈ {1, 3} and ǫ ∈ {±1}) does not
seem to give something interesting: the symmetric inﬁnite matrix obtained
by applying ˜χ to binomial coeﬃcients has probably no LU decomposition
in the algebra of recurrence matrices.
Similarly, there seem to be no new interesting Dirichlet characters
(mod 16) (with values in the Gaussian integers {±1, ±√−1}.

Remark 2.8. The case of the character n ↦−→ χ(n) = ǫn ≡ n(p−1)/2

(mod p) with ǫn ∈ {0, ±1} for p an odd prime gives rise to similar re-
sults which are somewhat trivial. Indeed, Lucas’s theorem implies that the
corresponding inﬁnite matrix with coeﬃcients χ(
(i+j
i )), 0 ≤ i, j has a struc-
ture of an inﬁnite tensor-power (corresponding to a “recurrence matrix of
complexity 1”). It is thus not very interesting and easy to handle.
The same remark holds for the remaining characters (mod p) when
working in a suitable ﬁeld (or integral subring) of cyclotomic numbers.

2.5 q−binomials

The expansion (x + y)n = ∑n
k=0 (n
k)
qxkyn−k involving two non-commuting
variables x, y related by yx = qxy where q is a central variable deﬁnes the
q−binomials coeﬃcients

(n
k
)
q =
 ∏n
j=1(1 − qj)
(∏k
j=1(1 − qj)
) (∏n−k
j=1 (1 − qj)
) ∈ N[q] .

An ordinary binary coeﬃcient (s+t
s ) can be identiﬁed with the number of
lattice paths with steps (1, 0) and (0, −1), starting at (0, s) and ending at
(t, 0). Similarly, the coeﬃcient of qc in the q−binomial (s+t
s )
q counts the
number of such paths delimiting a polygon of area c in the ﬁrst quadrant
{(x, y) ∈ R2 | x, y ≥ 0}.
Reﬂecting all paths contributing to (s+t
s )
q with respect to the diagonal
line x = y yields the equality
(s + t
s
 )
q = (s + t
t
 )
q .

Rotating all paths contributing to (s+t
s )
q by a half-turn centered at 1
2 (t, s)
shows the identity (s + t
s
 )
q = qst(s + t
s
 )
q−1 .

6

Partitioning all paths contributing to (s+t
s )

q accordingly to the nature of
their ﬁrst step (horizontal or vertical) shows the recursive formula
(s + t
s
 )
q = qs(s + t − 1
s
 )
q + (s + t − 1
s − 1
 )
q

or equivalently (n
k)

q = qk(n−1
k )
q + (n−1
k−1)
q which is the q−version of the

celebrated recurrence relation (n
k) = (n−1
k ) + (n−1
k−1) for ordinary binomial
coeﬃcients.
Cutting all lattice paths γ contributing to (s+t
s )
q along the diagonal line
s = t in two lattice paths shows the formula

∑

k qk2(s
k
)
q
 (t
k
)

q = (s + t
s
 )
q

where k ∈ {0, 1, . . . , min(s, t)}. This identity amounts to the matrix iden-
tity Pq = LqDqLt
q where Pq is the inﬁnite symmetric matrix with coef-
ﬁcients (
s+t
s )
q, 0 ≤ s, t, where Lq is the lower triangular unipotent ma-
trix with coeﬃcients (s
t)
q, 0 ≤ s, t and where Dq is diagonal with diag-
onal coeﬃcients 1, q, q4, q9, q16, q25, . . . . Denoting by Pq(n) the submatrix(s+t
s )

q, 0 ≤ s, t < n formed by the ﬁrst n rows and columns of Pq we

have the identity det(Pq(n)) = qPn−1
j=0 j2 which specialises to the identity
det(P1(n)) = 1 of Remark 2.2. Appendix I of [6] contains many more for-
mulae for (n
k)

q.
The formula of Lucas
(a
b
) ≡ (⌊a/p⌋
⌊b/p⌋
) (a (mod p)
b (mod p)
) (mod p)

(where p is a prime number and where a (mod p), b (mod p) ∈ {0, 1, . . . , p −
1}), see Section 2.1 or [11], has the following known analogue for q−binomials
which reduces their evaluation at roots of 1 of small order to evaluations of
ordinary binomial coeﬃcients.

Theorem 2.9. If ω = e2iπk/n is a primitive n−th root of 1 (ie. (k, n) = 1
with k ∈ Z and n ∈ N) then
(a
b
)
ω = (⌊a/n⌋
⌊b/n⌋
)
1
 (a (mod n)
b (mod n)
)
ω

for all a, b ∈ N where a (mod n), b (mod n) ∈ {0, 1, . . . , n − 1}.

Theorem 2.9 can be used to establish formulae for determinants of the
symmetric matrices obtained by considering the reduction modulo 2, the
Beeblebrox reduction or the reduction using the Jacobi character modulo 8
of (the real and imaginary part of) (s+t
s )
q, 0 ≤ s, t < n evaluated at q = −1
and q = i.
 7

3 The algebra of recurrence matrices

Recurrence matrices, introduced in [3], are a convenient tool for proving
our main results. Recurrence matrices are closely related to rational formal
power series in free non-commutative variables and can be considered as
generalisations of ﬁnite state automata or of iterated tensor products. They
arise also naturally in the context of “automata groups”, a notion generalis-
ing a famous group of Grigorchuk, see [9]. The following exposition does not
strive for exhaustivity or for the largest possible generality. Generalisations
(e.g. by replacing the ﬁeld of complex numbers by an arbitrary commutative
ﬁeld or by considering sequences of square matrices of size kn × kn, n ∈ N
for k ∈ {1, 2, 3, . . . }) are fairly straightforward and contained in [3] or with
more details in [4].
The papers [5] and [12] deal with interesting subalgebras, called self-
similar algebras, formed by recurrence matrices.

3.1 Recurrence matrices

Consider the vector space
 A =
 ∞∏

n=0 M2n×2n(C)

whose elements are sequences A = (A[0], A[1], A[2], . . . ) with A[n] ∈ M2n×2n(C)
denoting a complex square matrix of size 2n × 2n. The obvious product

AB = (A[0]B[0], A[1]B[1], A[2]B[2], . . . )

turns A into an associative algebra. Denoting by

ρ(0, 0)A, ρ(0, 1)A, ρ(1, 0)A, ρ(1, 1)A ∈ A

the four “corners” of

A = A[0], ( (ρ(0, 0)A)[0] (ρ(0, 1)A)[0]
(ρ(1, 0)A)[0] (ρ(1, 1)A)[0]
 ) , ( (ρ(0, 0)A)[1] (ρ(0, 1)A)[1]
(ρ(1, 0)A)[1] (ρ(1, 1)A)[1]
 ) , . . .

obtained (after deletion of the 1 × 1 matrix A[0]) by considering for all n ≥ 1
the 2n−1 × 2n−1 submatrix deﬁned by the ﬁrst or last 2n−1 rows and by
the ﬁrst or last 2n−1 columns of A[n], we get four linear endomorphisms
ρ(s, t) ∈ End(A), 0 ≤ s, t ≤ 1, of the vector space A. We call these
endomorphisms shift maps. Using a hopefully suggestive synthetic notation,
an element A ∈ A can thus be written as

A = A[0], ( ρ(0, 0)A ρ(0, 1)A
ρ(1, 0)A ρ(1, 1)A
 )

8

with A[0] ∈ C and ρ(0, 0)A, ρ(0, 1)A, ρ(1, 0)A, ρ(1, 1)A ∈ A.
Deﬁnition A subspace V ⊂ A is recursively closed if ρ(s, t)V ⊂ V for all
s, t.
The recursive closure S of a subset S ∈ A is the smallest recursively
closed subspace of A which contains S. We denote by A the recursive closure
of the subset {A} reduced to a single element A ∈ A. The complexity of
A ∈ A is the dimension dim(A) ∈ N ∪ {∞} of the recursive closure A ⊂ A.
An element A ∈ A is a recurrence matrix if its recursive closure A is of
ﬁnite dimension. We denote by R ⊂ A the subset of all recurrence matrices.
Writing ρ(Xs,t)A or simply Xs,tA for ρ(s, t)A, 0 ≤ s, t ≤ 1, the shift
maps ρ(s, t) ∈ End(A) induce a linear representation (still denoted) ρ :
{X0,0, X0,1, X1,0, X1,1}∗ −→ End(A), recursively deﬁned by

(Xs1,t1Xs2,t2 · · · Xsl,tl)A = (Xs1,t1Xs2,t2 · · · Xsl−1,tl−1)(ρ(sl, tl)A) ,

of the free non-commutative monoid {X0,0, X0,1, X1,0, X1,1}∗, called the shift
monoid, in four generators X0,0, X0,1, X1,0, X1,1 representing shift maps.
Subrepresentations of ρ correspond to recursively closed subspaces V of A
spanned by (unions of) orbits under {X0,0, X0,1, X1,0, X1,1}∗.
The linear action of the monoid {X0,0, X0,1, X1,0, X1,1}∗ on A suggests
to consider the bijective map which associates an element A ∈ A with the
non-commutative formal power series
∑

X∈{X0,0,X0,1,X1,0,X1,1}∗((XA)[0])X ∈ C⟨⟨X0,0, X0,1, X1,0, X1,1⟩⟩

in four free non-commutative variables X0,0, X0,1, X1,0, X1,1. This bijection
restricts to a bijection between the vector space R of recurrence matrices
and rational elements in C⟨⟨X0,0, X0,1, X1,0, X1,1⟩⟩.
The algebraic structure of R ⊂ A is described by the following result.

Proposition 3.1. (i) We have dim(λA) = dim(A) for all λ ∈ C∗ and for
all A ∈ A.
(ii) We have dim(A + B) ≤ dim(A) + dim(B) for all A, B ∈ A.
(iii) We have dim(AB) ≤ dim(A) dim(B) for all A, B ∈ A.

Remark 3.2. The inequalities of assertion (ii) and (iii) can of course be
strict: Consider two elements A, B ∈ A deﬁned by A[n] = 1+(−1)n

2 Id[n], B[n] =
1−(−1)n
2 Id[n] where Id[n] denotes the identity matrix of size 2n × 2n. The
elements A,B have common recursive closure A = B = CA + CB of dimen-
sion 2. Their sum A + B = Id ∈ R is the identity element having complexity
1 and their product AB = 0 has complexity 0.

Corollary 3.3. The set R of recurrence matrices is a subalgebra of A.

9

Proof of Proposition 3.1 (i) and (ii) are obvious.
Denoting (slightly abusively) by A B = {
∑ XiYi |Xi ∈ A, Yi ∈ B}
the vector space spanned by all products XY, X ∈ A, Y ∈ B, we have
AB ∈ A B.
For
 XY = (X[0]Y [0]), ( ρ(0, 0)(XY ) ρ(0, 1)(XY )
ρ(1, 0)(XY ) ρ(1, 1)(XY )
 ) ∈ A B

with X ∈ A, Y ∈ B, the computation

ρ(0, 0)(XY ) = (ρ(0, 0)X)(ρ(0, 0)Y ) + (ρ(0, 1)X)(ρ(1, 0)Y )
ρ(0, 1)(XY ) = (ρ(0, 0)X)(ρ(0, 1)Y ) + (ρ(0, 1)X)(ρ(1, 1)Y )
ρ(1, 0)(XY ) = (ρ(1, 0)X)(ρ(0, 0)Y ) + (ρ(1, 1)X)(ρ(1, 0)Y )
ρ(1, 1)(XY ) = (ρ(1, 0)X)(ρ(0, 1)Y ) + (ρ(1, 1)X)(ρ(1, 1)Y )

shows that A B is recursively closed of dimension ≤ dim(A) dim(B). As-
sertion (iii) follows now from the obvious inclusion AB ⊂ A B. ✷

Remark 3.4. Certain properties of binomial coeﬃcients (mod pd) are easy
to study using “recurrence matrices” given by sequences of matrices of size
pj × pj, j = 0, 1, . . . with entries in the associative ring Z/pdZ.

3.2 Recursive presentations

An element A ∈ A is completely determined by the action of the shift maps
ρ(s, t) on its recursive closure A (spanned by {X0,0, X0,1, X1,0, X1,1}∗A),
together with the restriction to A of the augmentation map π0 ∈ A∗ deﬁned
by projecting an element X = (X[0], X[1], . . . ) ∈ A onto its initial value
π0(X[0], X[1], X[2], . . . ) = X[0] ∈ C.
A recurrence matrix A can thus be given by a ﬁnite amount of data:
An (expression describing the) element A of the ﬁnite-dimensional vec-
tor space A, the restriction (still denoted) π0 ∈ A
∗ of the augmentation
map expressing the initial values of elements in A, and a 2 × 2 matrix

ρ = ( ρ(0, 0) ρ(0, 1)
ρ(1, 0) ρ(1, 1)
 ) ∈ M2×2(A ⊗ A
∗) of tensors encoding the shift

maps. The coeﬃcients of the matrix A[n] ∈ M2n×2n are then obtained by
“contractions” of π0 ρn A.
This leads to the notion of recursive presentations. A recursive presen-
tation for A ∈ R is given by the choice of a basis A1 = A, . . . , Aa of A (or
more generally of a ﬁnite set A1, . . . , Aa spanning a recursively closed vector
space containing A) and by recursive identities

Aj = π0(Aj), ( ρ(0, 0)Aj = ∑a
k=1 ρ(0, 0)k,j Ak ρ(0, 1)Aj = ∑a
k=1 ρ(0, 1)k,jAk
ρ(1, 0)Aj = ∑a
k=1 ρ(1, 0)k,j Ak ρ(1, 1)Aj = ∑a
k=1 ρ(1, 1)k,jAk
 )

10

encoding the initial values π0(Aj) and the values ρ(s, t)(Aj ) ∈ A of the shift
maps. A recursive presentation deﬁnes the elements A1 = A, . . . , Aa span-
ning (a recursively closed subspace containing) A recursively by expressing
the four “blocks” of Aj[n + 1] as linear combinations of A1[n], . . . , Aa[n].

Remark 3.5. We use the convention that 0 ∈ R admits the empty presen-
tation and 0 is “the” element of an empty basis. We speak thus of “the”
basis A1, . . . of 0 representing 0 = A1.

3.3 Saturation level

We denote by πl(A) = A[l] the projection of a matrix sequence A = (A[0], A[1], A[2], . . . ) ∈
A onto its square matrix A[l] of size 2l × 2l. Similarly,

π≤l(A) = (π0(A), π1(A), . . . , πl(A)) = (A[0], A[1], . . . , A[l]) ∈ ⊕l
j=0M2j ×2j (C)

denotes the projection of the sequence A onto its ﬁrst l + 1 matrices.
The saturation level of a ﬁnite dimensional subspace V ⊂ A is the small-
est integer N ∈ N such that K≤N (V) = K≤N +1(V) where K≤l(V) ⊂ V is the
kernel of the projection π≤l : V −→ π≤l(A) = ⊕l
j=0M2j ×2j .

Proposition 3.6. We have K≤N (V) = {0} for the saturation level N of a
ﬁnite-dimensional subspace V ⊂ A which is recursively closed.
In particular, π≤N : V −→ ⊕N
j=0M2j ×2j deﬁnes an injection.

Proof The obvious inclusions ρ(s, t)K≤l+1(V) ⊂ K≤l(V) imply that K≤N (V) =
K≤N +1(V) ⊂ V is recursively closed. Since the restriction to K≤N +1(V) ⊂
K≤0 of the augmentation map π0 : A −→ C is trivial, we have (XK)[0] = 0
for all X ∈ {X0,0, X0,1, X1,0, X1,1}∗ and for all K ∈ K≤N (V). This shows
K≤N (V) = {0}. ✷
Proposition 3.6 enables us to extract a basis from a ﬁnite set S spanning
a recursively closed vector space V ⊂ R. Similarly, Proposition 3.6 allows
the construction of a basis of the subspace A ⊂ V for an element A ∈ V of
a ﬁnite-dimensional recursively closed vector space V ⊂ R.
These operations are the necessary ingredients for eﬀective computations
in the algebra R. Eﬀectivity means that there exists an algorithm involving
only a ﬁnite number of elementary operations in the groundﬁeld C and a
ﬁnite amount of data which computes the result of an algebraic expression
(given by a non-commutative polynomial) involving (recursive presentations
of) a ﬁnite number of elements in R.
The necessary elementary algorithms can be brieﬂy described as follows:

3.3.1 Multiplication of A ∈ R by a non-zero scalar λ ∈ C∗

A presentation of λA is obtained from a presentation of A by multiplying
the initial values π(Aj) = Aj[0] ∈ C with λ (and by keeping the same shift
maps).
 11

3.3.2 Addition of two elements A, B ∈ R

Add a ﬁrst element A1 + A2 having the obvious initial value π0(A + B) =
A1[0] + B1[0] to the list of not necessarily linearly independent elements
A1, . . . , Aa, B1, . . . , Bb spanning A + B. The elements ρ(s, t)(A1+A2), ρ(s, t)Aj , ρ(s, t)Bj
are given by

ρ(s, t)(A1 + B1) =
 a∑

k=1 ρ(s, t)
A
k,1Ak +
 b∑

k=1 ρ(s, t)
B
k,1Bk

and
 ρ(s, t)Ai =
 a∑

k=1 ρ(s, t)
A
k,iAk, ρ(s, t)Bj =
 b∑

k=1 ρ(s, t)
B
k,jBk

for all 0 ≤ s, t ≤ 1, 1 ≤ i ≤ a, 1 ≤ j ≤ b where ρ(s, t)A and ρ(s, t)B are the
obvious shift maps with respect to bases A = A1, . . . , Aa and B = B1, . . . , Bb
of A and B. Working with the ﬁnite-dimensional recursively closed subspace
C(A1 + B1) + ∑a
i=1 CAi + ∑b
j=1 CBj ⊂ R one can now give a presentation
of A1 + B1 by computing a basis of A1 + B1, followed by the computation
of the coeﬃcients (with respect to this basis) of the shift maps.

Remark 3.7. The algorithms 3.3.1 and 3.3.2 can be used to compare two
elements A, B ∈ R by computing a presentation of A − B.

3.3.3 Multiplication of two elements A, B ∈ R

Consider the ab elements Ci,j = AiBj, 1 ≤ i ≤ a, 1 ≤ j ≤ b with initial
values Ci,j[0] = π0(AiBj) = Ai[0]Bj [0]. Shift maps are given by

(∗)ρ(s, t)Ci,j = ∑a
k=1 ∑b
l=1 (
ρ(s, 0)A
k,iρ(0, t)B
l,j + ρ(s, 1)A
k,iρ(1, t)B
l,j) Ck,l

using the notations of 3.3.2. One constructs now a recursive presentation of
C1,1 = AB by proceeding as above using the recursively closed vector space
∑a
i=1 ∑b
j=1 CCi,j ⊃ C1,1.

Remark 3.8. The formulae (*) occuring in 3.3.3 deﬁne an associative prod-
uct on the set L of all equivalence-classes of ﬁnite-dimensional linear rep-
resentations of the monoid {X0,0, X0,1, X1,0, X1,1}∗. Considering also di-
rect sums of linear representations turns L into a semi-ring. The semi-
ring L has a homomorphism ϕ into the semi-ring (with addition V + W =
{X + Y | X ∈ V, Y ∈ W} and product VW = {
∑i XiYi | Xi ∈ V, Yi ∈ W})
formed by all ﬁnite-dimensional recursively closed subspaces of R. The ele-
ments of ϕ(L) have two equivalent descriptions: They can be identiﬁed with
the subset L′ ⊂ L given by all equivalence classes of ﬁnite-dimensional linear
representations of {X0,0, X0,1, X1,0, X1,1}∗ containing no equivalence class of

12

a subrepresentation with multiplicity > 1. The second descriptions involves
birecursively closed vector spaces which are deﬁned as follows: A vector space
V ⊂ R is birecursively closed if it is recursively closed and if an arbitrary
generic modiﬁcation of the initial values in a recursive presentation of an
element in V yields again a presentation of an element in V.
The homomorphism of semi-rings ϕ associates to a ﬁnite-dimensional
linear representation ρf of {X0,0, X0,1, X1,0, X1,1} the unique maximal bire-
cursively closed subspace of R whoses shift maps involve only equivalence
classes of subrepresentations in ρf .
Finite-dimensional birecursively closed subspaces of R are stable under
direct sums and products and their semi-ring is the quotient semi-ring ϕ(L)
of L.

3.4 The LU decomposition of a convergent non-singular ele-
ment in R

An element P ∈ A such that P = ρ(0, 0)P is called convergent. It is given
by considering the sequence

P0,0, ( P0,0 P0,1
P1,0 P1,1
 ) ,
 




 P0,0 P0,1 P0,2 P0,3
P1,0 P1,1 P1,2 P1,3
P2,0 P2,1 P2,2 P2,3
P3,0 P3,1 P3,2 P3,3
 



 , . . .

of all square submatrices formed by the ﬁrst 2n rows and columns of an
inﬁnite “limit”matrix 



 P0,0 P0,1 P0,2 . . .
P1,0 P1,1 P1,2 . . .
...
 


 .

Henceforth we denote generally a convergent element in A and the associated
inﬁnite matrix by the same letter. This should not lead to confusions except
in cases where both interpretations are correct.
We call an inﬁnite matrix P non-singular if the k × k square matrix P (k)
formed by its ﬁrst k rows and columns has non-zero determinant for all k ≥ 1.
Such a non-singular matrix P has an LU −decomposition: It can be written
as P = LU with L lower triangular unipotent (1’s on the diagonal) and U
upper triangular non-singular. The identity P = LU implies the equality
det(P (k)) = det(U (k)) for all k ≥ 1 and gives rise to an LU −decomposition
in A by considering as above for n = 0, 1, 2, . . . the submatrices formed by
the ﬁrst 2n rows and columns of of P, L and U . If P is symmetric we have
moreover U = DLt where D is diagonal non-singular and Lt is obtained by
transposing the matrix L.
All proofs of the results presented in Section 2 boil down to LU −decompositions
with P = P t = LU, L, D, U = DLt ∈ R.

13

Remark 3.9. Call an element A ∈ A non-singular if it involves only non-
singular matrices A[0], A[1], . . . . Such an element has an LU −decomposition
(in the obvious sense) in A.
Proving the non-existence of an LU −decomposition in R for a suitable
given non-singular recurrence matrix A ∈ R is probably diﬃcult.
The related problem of constructing the (existing) recurrence matrices
L, U ∈ R from the knowledge (of a recursive presentation) of A = LU ∈ R
has however an algorithmic answer: One proceeds as for the existence of
an inverse element by guessing recursive presentations for L and U using
LU −decompositions of ﬁnitely many matrices A[0], A[1], . . . , A[N + 1]. In
case of succes, the resulting hypothetical decomposition, if correct, can then
be proven to hold. The necessary algorithm is obtained after minor modiﬁca-
tions from the algorithm for computing the inverse A−1 ∈ R of an invertible
element A ∈ R described in Section 4.1

4 Invertible recurrence matrices

The set of all recurrence matrices which are invertible in the algebra R forms
the group of units in R. Determining the inclusion in the unit group of R
of a recurrence matrix A is perhaps a diﬃcult problem without algorithmic
solution. Indeed, we have the following result.

Proposition 4.1. (i) For every natural integer n there exist invertible re-
currence matrices A, B = A−1 ∈ R such that dim(A) = 2 and dim(B) > n.
(ii) There exist elements in R which are invertible in the algebra A but
not in the subalgebra R of recurrence matrices.

Remark 4.2. The assumption dim(A) = 2 is optimal: Invertible recurrence
matrices of complexity 1 form a subgroup (isomorphic to C∗ × GL2(C)) in
R.

Proof of Proposition 4.1 For ω ∈ C∗, consider the convergent element

A = 1, ( 1
−ω 1
 ) ,
 




 1
−ω 1
0 −ω 1
0 0 −ω 1
 



 , · · · ∈ A

consisting of lower triangular unipotent matrices with constant subdiagonal
−ω. It deﬁnes a recurrence matrix A = A1 of complexity 2 recursively
presented by
 A1 = 1, ( A1 0
A2 A1
 ) , A2 = −ω, ( 0 A2
0 0
 ) .

14

Since A is given by a sequence of unipotent lower triangular matrices, it
is invertible in the algebra A with inverse the convergent element

B = A
−1 = 1, ( 1
ω 1
 ) ,
 




 1
ω 1
ω2 ω 1
ω3 ω2 ω 1
 



 , · · · ∈ A

whose limit is the inﬁnite unipotent lower triangular Toeplitz matrix with
constant subdiagonals associated to the geometric progression 1, ω, ω2, . . . .
For k a strictly positive integer, we consider the element

Sk = ω20k, ω21k ( 1 ω
ω ω2
 ) , ω22k
 




 1 ω ω2 ω3

ω ω2 ω3 ω4

ω2 ω3 ω4 ω5

ω3 ω4 ω5 ω6
 



 , · · · ∈ A

given by (Sk[n])i,j = ω2nk+i+j, 0 ≤ i, j < 2n. A straightforward computa-
tion shows ρ(s, t)Sk = Ss+t+2k for all s, t. Since we have

B = 1, ( B 0
S1 B
 )

(using the notation of recursive presentations), the algebraic closure B of B
is spanned by the set

{X0,0, X0,1, X1,0, X1,1}
∗B = B ∪ {Sk | k ≥ 1} .

Since ωN = 1 implies Sk+N = Sk, this set contains at most 1 + N elements
if ω is a root of 1 of ﬁnite order N .
In order to prove assertion (i), we consider the case where ω is a root
of 1 having odd order N > 2n and we denote by a ≥ log2(N + 1) > n the
order of 2 in the multiplicative group (Z/N Z)∗. The action of the monoid
ρ(0, 0)N on Sk corresponds then to the action of the Galois map ω ↦−→ ω2

on the upper left coeﬃcients

ω20k, ω21k, ω22k, ω23k, . . .

of Sk. Elementary number theory (for instance reduction modulo 2 by choos-
ing ω among the primitive N −th roots of 1 in the ﬁeld extension F2a of de-
gree a over F2) shows that the set S2N spans a subspace of dimension a > n
in B. This implies assertion (i).
Consider now A as above with ω ∈ C \ Q transcendental. This allows to
consider ω as a variable and we have dim(Bω) ≥ dim(Bξ) for the complexity
of the inverse element Bω = A−1
ω where ξ ∈ Q is any algebraic specialisation
of ω. Assertion (ii) follows now from assertion (i). ✷

15

Remark 4.3. An example of B = A−1 ∈ A \ R with A ∈ R invert-
ible only in A is also given by A, B as above with ω = 2 (the argu-
ment below works in fact for any ω of norm |ω| ≥ 1). Indeed, other-
wise, up to a constant, the initial values 2, 22, 24, 28, . . . of the sequence
ρ(1, 0)B, ρ(0, 0)ρ(1, 0)B, ρ(0, 0)2 ρ(1, 0)B, . . . should be bounded above by a
geometric progression 1, µ, µ2, . . . for any positive µ exceeding the spectral
radius (absolute value of the largest eigenvalue) of ρ(0, 0) ∈ End(B).
The simplest element of R with an inverse in A \ R is perhaps given by
the central diagonal recurrence matrix A of complexity 2 deﬁned by A[n] =
(n + 1)Id[n] where Id[n] denotes the identity matrix of size 2n × 2n. We give
two proofs that the inverse element A−1, given by A−1[n] = 1
n+1 Id[n], has
inﬁnite complexity.
A ﬁrst proof follows from the observation that the sequences of diagonal
coeﬃcients 1
n+k+1 = (ρ(0, 0)kA−1)[n] form the rows of the Hilbert matrix of
inﬁnite rank with coeﬃcients Hi,j = 1
1+i+j , 0 ≤ i, j.
In order to give a second proof, we observe that all coeﬃcients of A−1

are rational numbers and every prime number appears as a denominator in
a suitable coeﬃcient of A−1. This is impossible for an element B ∈ R with
rational coeﬃcients. Indeed, such an element B has a recursive presentation
with data (consisting of initial values and coeﬃcients of shift maps with
respect to a basis ⊂ {X0,0, X0,1, X1,0, X1,1}∗B of B) given by a ﬁnite set D
of rational numbers. Since all coeﬃcients of B are evaluations of integral
polynomials on D, all denominators of coeﬃcients in B involve only prime
numbers occuring in the denominators of the ﬁnite set D.

Remark 4.4. The quotient group of invertible elements modulo C∗Id can
be turned into a metric group by considering the positive real function

A ↦−→∥ A ∥= max(log(dim(A + CId)), log(dim(A−1 + CId)))

on the group Γ of units in R. It satisﬁes ∥ A ∥≥ 0 with ∥ A ∥= 0 only
for A ∈ C∗Id, ∥ AB ∥≤∥ A ∥ + ∥ B ∥ and ∥ A ∥=∥ A−1 ∥ and deﬁnes
thus a left-invariant distance on the quotient group Γ/C∗Id by considering
d(A, B) =∥ A−1B ∥.
The corresponding group over a ﬁnite ﬁeld has ﬁnitely many elements in
balls of ﬁnite radii and it would be interesting to understand the generating
function ∑

A∈Γ(Fpe ) tmax(dim(A+CId),dim(A−1+CId)) ∈ N[[t]]

where the sum is over all elements of the unit group Γ(Fpe) of the algebra
R(Fpe) deﬁned in the obvious way over the ﬁnite ﬁeld Fpe.
The related generating function
∑

A∈R(Fpe ) tdim(A) ∈ N[[t]]

16

counting all elements of given complexity in the algebra R(Fpe) is probably
fairly easy to compute. It has convergency radius 0 and is thus transcenden-
tal.

4.1 Algorithm for computing A
−1 ∈ R for A ∈ R invertible in
R

The following algorithm computes the inverse of an element A ∈ R if it has
an inverse in R and fails (does never stop and uses more and more memory)
for an element A as in assertion (ii) of Proposition 4.1. Non-invertibility in
A will eventually be detected (assuming exact arithmetics over the ground
ﬁeld) by exhibiting an integer k for which A[k] is singular.
Input: A (presentation of a) recurrence matrix A ∈ R.
Set N = 1 and M = 1.
Loop Compute, if possible, the matrices B[0] = A[0]−1, B[1] = A[1]−1, . . . , B[N +
M + 1] = A[N + M + 1]−1.
If a matrix A[k] with k ≤ N + M + 1 is not invertible, print “The matrix
A[k] is singular and A has thus no inverse in A” and stop.
We denote by ˜B ∈ A the sequence B[0], . . . , B[N + M + 1] completed
by arbitrary matrices ˜B[k] of size 2k × 2k (for example by zero matrices) if
k > N + M + 2.
For n, m ∈ N such that n + m ≤ N + M + 1, we denote by V(n, m) ⊂
⊕n
j=0M2j ×2j (C) the vector-space spanned by all 1 + 4 + · · · + 4m elements

(π≤n(X ˜B))X∈X ≤m where X ≤m denotes the set of all 1−4m+1
1−4 = 1 + 4 + 42 +
· · · + 4m words of length ≤ m in the alphabet X = {X0,0, X0,1, X1,0, X1,1}.
If dim(V(N, M )) < dim(V(N + 1, M )), then increase N by 1 and iterate
the Loop.
If dim(V(N, M )) < dim(V(N, M + 1)), then increase M by 1 and iterate
the Loop.
Setting d = dim(V(N, M )), the identity dim(V(N, M )) = dim(V(N +
1, M )) shows that the ﬁnite sequence B[0], . . . , B[N + M + 1] can be com-
pleted to a uniquely deﬁned element B ∈ R which is of complexity d and of
saturation level ≤ N . Use the natural isomorphisms between V(N, M ), V(N +
1, M ) and V(N, M +1) and the inclusions ρ(s, t)V(N, M +1) ⊂ V(N, M ), 0 ≤
s, t ≤ 1 (where ρ(s, t) acts in the obvious way) for writing down a recursive
presentation of B.
Check if AB = 1 using the algorithms of Section 3.3.
If yes, print the presentation found for B and stop.
Otherwise, increase N by 1 and iterate the Loop.
End of Loop

Remark 4.5. The above algorithm can perhaps be improved. In particular,
it is probably not necessary to consider all (4M +1 −1)/3 words of X ≤M ⊂ X ∗

during the computation of the dimension of V(N + 1, M ).

17

5 Modulo 2 and 2−valuations

Proof of Theorem 2.1 The inﬁnite symmetric Pascal matrix P with co-
eﬃcients ((i+j
i ) (mod 2)
) ∈ {0, 1} for 0 ≤ i, j deﬁnes a convergent element
(still denoted) P ∈ A. It follows from Lucas’s formula (see Section 2.1) that
P is a recurrence matrix of complexity 1 recursively presented by

P = 1, ( P P
P
 )

(zero-entries are omitted). The recurrence matrix P ∈ R has an LU decom-
position in R given by the equality P = LDLt with L, D ∈ R of complexity
1 deﬁned by the recursive presentations

L = 1, ( L
L L
 ) and D = 1, ( D −D
 )

where L is lower triangular unipotent and D is diagonal. An easy analysis
of the coeﬃcients of the diagonal recurrence matrix D ends the proof. ✷

Remark 5.1. The convergent lower triangular recurrence matrix L and the
convergent diagonal recurrence matrix D correspond to the inﬁnite limit-
matrices (still denoted) L, D with coeﬃcients given by Li,j = ((i+j
i ) (mod 2)
) ∈

{0, 1} (for 0 ≤ i, j) and Dn,n = (−1)ν0+ν1+ν2+... = (−1)ds(n) where n =∑j≥0 νj2j ≥ 0 is a binary integer.

Remark 5.2. Recurrence matrices of complexity 1 are, up to scalars, of the
form 1, M, M ⊗ M, M ⊗ M ⊗ M, . . . where M is a complex 2 × 2 matrix.
It follows that the matrices L and D (and thus also P = LDLt) involved
in the proof of Theorem 2.1 are invertible in R. The recurrence matrix
D is its own inverse. The inverse L−1 of L is recursively presented by

L−1 = 1, ( L−1

−L−1 L−1
 ).

Remark 5.3. The spectrum of recurrence matrices of complexity 1 is easy
to compute: Given a square matrix M of size d × d with characteristic
polynomial ∏d
j=1(t − λj) we have

∏

(j1,...,jn)∈{1,...,d}n(t − λj1 · · · λjn)

for the characteristic polynomial of the iterated tensor power M ⊗n.

Proof of Theorem 2.3 The inﬁnite matrix V with coeﬃcients

Vs,t = i
v2((s+t
s )) = i
ds(s)+ds(t)−ds(s+t)

18

gives rise to a convergent element V ∈ A. A bit of work using Kummer’s
formulae (see Section 2.2) shows that V = V1 is recurrence matrix given by
the recursive presentation

V1 = 1, ( V1 V2
V2 iV1
 )

V2 = 1, ( V1 −iV1 + (1 + i)V2
−iV1 + (1 + i)V2 −V1
 )

We have V = LDLt ∈ R with L = L1 ∈ R recursively presented by

L1 = 1, ( L1
L3 L4
 )

L2 = 0, ( 0 −iL2
−L1 + L3 −iL2 − iL4
 )

L3 = 1, ( L1 L2
−iL1 + (1 + i)L3 L2 + (1 + i)L4
 )

L4 = 1, ( L1
(1 − i)L1 + iL3 L4
 )

and with diagonal D = D1 ∈ R recursively presented by

D1 = 1, ( D1 D2
 )

D2 = −1 + i, ( D3 2D1 − D2 + 2D3
 )

D3 = −1 + i, ( D3 −D2
 )

An analysis (left to the reader) of the diagonal entries of D1 ends the proof.
✷

Remark 5.4. The recurrence matrices L, D and V = LDLt are invertible
in R, see [3].

6 Beeblebrox reduction

This section is devoted to proofs and complements involving the Beeblerox
reduction χB(
(n
k)
) of binomial coeﬃcients.
Proof of Theorem 2.5 We have
(2n
2k
) = (2n) · · · (2n − 2k + 1)
(2k) · · · 1 = (n
k
) (2n − 1)(2n − 3) · · · (2n − 2k + 1)
(2k − 1)(2k − 3) · · · 1

where both the numerator and the denominator of the fraction

F = (2n − 1)(2n − 3) · · · (2n − 2k + 1)
(2k − 1)(2k − 3) · · · 1

19

contain k terms. If k is even, we have F ≡ 1 (mod 4) since the numerator
and denominator of the fraction F contain both k/2 factors ≡ 1 (mod 4)
and k/2 factors ≡ −1 (mod 4). If k and n are both odd, the numerator and
denominator of F contain both (k + 1)/2 factors ≡ 1 (mod 4) and (k − 1)/2
factors ≡ −1 (mod 4) and we have again F ≡ 1 (mod 4). If k is odd and n
is even, then both binomial coeﬃcients (2n
2k) and (n
k) are even and we have
thus χB(
(2n
2k)
) = χB(
(n
k)) = 0. This proves the ﬁrst equality.
The binomial coeﬃcient ( 2n
2k+1
) is obviously even and this implies the
second equality.
In the next case we have
(2n + 1
2k
 ) = (n
k
) (2n + 1)(2n − 1) · · · (2n − 2k + 3)
(2k − 1)(2k − 3) · · · (1)

and the last fraction equals 1 (mod 4) if k is even.
For k odd and n even, we have χB(
(2n+1
2k )) = χB(
(n
k)
) = 0 since (2n+1
2k ) ≡(n
k) ≡ 0 (mod 2).
For n, k both odd, the correction (−1)k = −1 equals the fraction modulo
4. This ends the proof of the third equality.
In the case of the last equality, we have
(2n + 1
2k + 1
) = 2n + 1
2k + 1
 (2n
2k
)

which is even if n ≡ 0 (mod 2) and k ≡ 1 (mod 2). If n ≡ k (mod 2) then
2n+1
2k+1 ≡ 1 (mod 4). For n odd and k even we have 2n+1
2k+1 ≡ −1 = (−1)n(k+1)

(mod 4). The ﬁrst equality and these observations complete the proof. ✷

6.1 Proof of Theorem 2.6

Proof As in Section 3.4, we consider the element (still denoted) Z ∈ A
associated to the inﬁnite matrix Z with coeﬃcients Zs,t = χB(
(s+t
s )
), 0 ≤
s, t.
We have to show that Z is a recurrence matrix and we have to ﬁnd
a recursive presentation for Z. This can be done in the following way:
We consider left shift-maps λ(0, 0), λ(0, 1), λ(1, 0), λ(1, 1) which associate to
A = (A[0], A[1], . . . ) ∈ A the element λ(s, t)A ∈ A where (λ(s, t)A)[n] is
the submatrix of A[n + 1] corresponding to row-indices ≡ s (mod 2) and
column-indices ≡ t (mod 2). A subspace V ⊂ A is left-recursively closed
if it is invariant under all four left shift-maps and the left-recursive closure
A
λ ⊂ A of A ∈ A is the smallest left-recursively closed subspace containing
A. Theorem 2.5 implies that Zλ is ﬁnite-dimensional. One shows that
dim(Aλ) = dim(A) for all A ∈ A (see for example [4] for the details).
This proves that Z is a recurrence matrix. A little bit of work based on

20

properties of the saturation index shows now that Z = Z1 is given by the
recursive presentation
 Z1 = 1, ( Z1 Z2
Z3 0
 )

Z2 = 1, ( Z1 Z2
−Z3 0
 )

Z3 = 1, ( Z1 −Z2
Z3 0
 )

We have the identity Z = LDLt with L = L1 ∈ R lower triangular
unipotent given by the recursive presentation

L1 = 1, ( L1
L3 L4
 ) L2 = 2, ( − 2
3 L1 2L2
2
3 L3 2L4
 )

L3 = 1, ( L1 L2
L3 L4
 ) L4 = 1, ( L1
1
3 L3 L4
 )

The diagonal matrix D = D1 ∈ R has recursive presentation

D1 = 1, ( D1 D2
 ) , D2 = −1, ( 3D1 1
3 D2
 )

An easy inspection of the diagonal entries of D1 completes the proof. ✷

Remark 6.1. The birecursively closed subspaces of A appearing in Remark
3.8 are the recursively closed subspaces of A which are also left-recursively
closed, ie. invariant under all four left shift-maps mentionned above.

6.1.1 The group ΓL

All four recurrence matrices L1, L2, L3, L4 involved in our recursive presen-
tation of L = L1 are invertible in R. Their inverses are given by

L−1
1 = M1, L−1
2 = − 1
2 M3, L−1
3 = − 1
2 M2, L−1
4 = M4

with M1, M2, M3, M4 recursively presented by

M1 = 1, ( M1
M3 M4
 ) M2 = −2, ( 2M1 2M2
2M3 2M4
 )

M3 = −1, ( M1 M2
1
3 M3 − 1
3 M4
 ) M4 = 1, ( M1
1
3 M3 M4
 )

We have the curious inclusions

ρ(0, 0)L ∈ QL1, ρ(0, 1)L ∈ QL2,
ρ(1, 0)L ∈ QL3, ρ(1, 1)L ∈ QL4

21

for L ∈ L1 = L2 = L3 = L4 = ⊕4
j=1CLj. The analogous property holds also
for their inverses

M1 = L−1
1 , M2 = −2L−1
3 , M3 = −2L−1
2 , M4 = L−1
4 .

This suggests that it would perhaps be interesting to understand the
group ΓL = ⟨a, b, c, d⟩ ⊂ R generated by the normalised recurrence matrices

a = L1 = 1, ( 1
1 1
 ) ,
 




 1
1 1
1 2 1
1 1 1
3 1
 



 , . . .

b = 1
2 L2 = 1, ( − 1
3 2
1
3 1
 ) ,
 




 − 1
3 0 − 2
3 4
− 1
3 − 1
3 2
3 2
1
3 2
3 1 0
1
3 1
3 1
3 1
 



 , . . .

c = L3 = 1, ( 1 2
1 1
 ) ,
 




 1 0 − 2
3 4
1 1 2
3 2
1 2 1 0
1 1 1
3 1
 



 , . . .

d = L4 = 1, ( 1
1
3 1
 ) ,
 




 1
1 1
1
3 2
3 1
1
3 1
3 1
3 1
 



 , . . .

corresponding to the invertible “projective” elements Q∗Li. In particular,
it would be interesting to understand if ΓL is a linear group. This would
certainly be implied by the existence (which I ignore) of a natural integer
N for which the projection ΓL −→ π≤N (ΓL) is one-to-one.
L. Bartholdi communicated to me the following list implying all relations
of length ≤ 12 in ΓL: bd
−1ca−1,
ca
−1ca−1,
cad
−1a
−1d
2a
−1b−1,
cad
−1c
−1bda
−1b−1,
cda−2dad
−1b−1,
ca
2d
−1a
−2dada−2b−1,
d
2ad
−2b−1cada
−3,
cdad
−2a−1dada−2b−1.

He observed that they are all of the form unv−1
n wnx−1
n , where un, vn, wn, xn
are positive words of length n with respect to the generators {a, b, c, d}.
More generally, it should also be interesting to understand the subalgebra
L ⊂ R generated by the recurrence matrices a±1, b±1, c±1, d±1 ∈ R.

22

The algebra L is of course a quotient of the group algebra C[ΓL] and it
would be interesting to describe the kernel of the associated homomorphism.
The algebra L is a quotient of the free non-commutative algebra

N = C⟨A, A
−1, B, B−1, C, C −1, D, D−1⟩

in eight free non-commutative variables A±1, B±1, C ±1, D±1. The corre-
sponding natural homomorphism π : N −→ L (given by Z ±1 ↦−→ z±1 ∈ R
for (Z, z) ∈ {(A, a), (B, b)(C, c), (D, d)}) factorises through the group alge-
bra of the abstract group ΓL. The kernel I = ker(π) ⊂ N contains thus all
relation of ΓL and in particular the trivial relations

AA
−1 − 1, BB−1 − 1, CC −1 − 1, DD−1 − 1 .

In order to gain some information on I, we can consider the morphism
of algebras µ1 : N −→ M2×2(N ) given by

A ↦−→ ( A 0
C D
 ) , A
−1 ↦−→ ( A−1 0
−B−1 D−1
 ) ,

B ↦−→ ( −A/3 2B
C/3 D
 ) , B−1 ↦−→ ( −A−1 2C −1

B−1/3 D−1/3
 ) ,

C ↦−→ ( A 2B
C D
 ) , C −1 ↦−→ ( −A−1 2C −1

B−1 −D−1
 ) ,

D ↦−→ ( A 0
C/3 D
 ) , D−1 ↦−→ ( A−1 0
−B−1/3 D−1
 ) ,

This morphism factors through π and induces a homomorphism of alge-
bras µ1 : L −→ M2×2(L) which removes simply the ﬁrst matrix X[0] from
an element X[0], X[1], · · · ∈ L. This is due to the deﬁnition of µ1 which
corresponds to the maps R −→ M2×2(R) given by

X ↦−→ ( ρ(0, 0)X ρ(0, 1)X
ρ(1, 0)X ρ(1, 1)X
 )

for X ∈ {a±1, b±−1, c±1, d±1}. We have thus in particular µ1(I) ⊂ M2×2(I).
Application of µ1 to some known element in I can sometimes be used for
the discovery of new elements in I: The computation

µ1(AA
−1) = ( A
C D
 ) ( A−1

−B−1 D−1
 ) = ( AA−1

CA−1 − DB−1 DD−1
 )

shows that application of µ1 to the trivial relation AA−1 − 1 ∈ I implies the
already known inclusions AA−1 − 1, DD−1 − 1 ∈ I and produces the non-
trivial relation CA−1 − DB−1 ∈ I. Since elements of I involving only two
monomials induce relations on the group ΓL, we get the relation bd−1ca−1

in ΓL which is the ﬁrst relation in Bartholdi’s list.

23

“Iterating” the map µ1 produces homomorphisms µn : N −→ M2n×2n(N )
with similar properties. In particular, we have µn(I) ⊂ M2n×2n(I). Index-
ing the coeﬃcients of matrices in M2n×2n(N ) by elements X ∈ {X0,0, X0,1, X1,0, X1,1}n,
we get linear maps µX : N −→ N by considering the coeﬃcient correspond-
ing to X in µn(N ). The reader should be warned that the map X ↦−→ µX ∈
End(N ) is not a morphism of monoids from {X0,0, X0,1, X1,0, X1,1}∗ into
End(N ). The monoid generated by all maps µX, X ∈ {X0,0, X0,1, X1,0, X1,1}∗,
preserves however the ideal I.
Denoting by N (Z) the subring of noncommutative polynomials with in-
tegral coeﬃcients, relations of the form r1 = r2 in ΓL are in bijection with
pairs of roots in the inﬁnite-dimensional Euclidean lattice (with respect to
the orthonormal basis given by monomials) I ∩ N (Z).
The peculiar form of all relations in Bartholdi’s list is partially explained
by the formulae for µ1. They imply that the maps µX preserve sign struc-
tures: The vector space spanned by the orbit under the monoid generated
by the maps µX of a relation of the form unv−1
n = xnw−1
n contains only
relations of the same form.
It would be interesting to know if the ideal I is ﬁnitely generated as
an {µX}X∈{X0,0,X0,1,X1,0,X1,1}∗ −module: Otherwise stated, does I contain a
ﬁnite subset G such that I is the smallest bilateral ideal which contains G
and which is preserved by all maps µX?

Remark 6.2. The techniques used in this Section can of course be applied to
other subsets in R. One needs a (preferably ﬁnitely generated) algebra S (eg.
the algebra generated by suitable elements of a subgroup in R) such that the
recursive closure of every element in S is spanned by elements of S. The
choice of a generating set G allows to consider the free non-commutative
algebra N on G which gives rise to the natural surjective homomorphism
π : N −→ S. Choosing lifts of the shift maps, one constructs homomor-
phisms µN : N −→ M2n×2n(N ) giving rise to the linear maps µX ∈ End(N )
preserving the bilateral ideal I = ker(π).
The maps µX can be choosen in order to preserve the grading of N if
the generating set G spans a recursively closed subspace.

6.1.2 The inverses of D1, D2 and the group ΓZ

The inverses of the diagonal recurrence matrices D1, D2 (deﬁned by the
decomposition Z = LD1Lt and by D2 = ρ(1, 1)D1) are E1 = D−1
1 , E2 =
D−1
2 recursively presented by

E1 = 1, ( E1 E2
 ) , E2 = −1, ( 1
3 E1 3E2
 )

The inverses of the matrices Z1, Z2, Z3 are U1 = Z −1
1 , U3 = Z −1
2 , U2 =

24

Z −1
3 recursively presented by

U1 = 1, ( 0 U2
U3 U1 − U2 − U3
 ) ,

U2 = 1, ( 0 U2
−U3 −U1 + U2 + U3
 ) ,

U3 = 1, ( 0 −U2
U3 −U1 + U2 + U3
 ) .

Since Z1 = Z t
1 and Z2 = Z t
3, the group ΓZ = ⟨a, b, c⟩ ⊂ R generated by
a = Z1, b = Z2, c = Z3 has an involutive automorphism given by a ↦→
a−1, b ↦→ c−1, c ↦→ b−1. Two relations in ΓZ are (ab−1)2 and ab = ca.
Using the relation a2 = cb following from the computation

a2 = aab
−1b = aba
−1b = caa
−1b = cb ,

every element of ΓZ can be expressed as an element of aǫ⟨b, c⟩ with ǫ ∈ {0, 1}.
Since det(π2(a)) = −1 and det(π2(b)) = det(π2(c)) = 1, the subgroup
generated by b, c is of index 2 in ΓZ .

6.2 The triangular Beeblebrox matrix

We deﬁne the lower triangular Beeblebrox matrix as the inﬁnite lower tri-
angular matrix with coeﬃcients Ls,t = χB(
(s
t)), 0 ≤ s, t, given by the Bee-
blebrox reduction of binomial coeﬃcients.
One of the main results of [7] states that any ﬁxed row of L contains
either no coeﬃcients −1 or the same number (given by a power of 2) of
coeﬃcients 1 and −1. This can of course also be deduced from Theorem
2.5 or by computing LJ where J is the “recurrence vector” obtained by
considering the sequence of column vectors

(1), (1, 1)
t, (1, 1, 1, 1)
t, (1, 1, 1, 1, 1, 1, 1, 1)
t , . . . .

The triangular Beeblebrox matrix L deﬁnes a recurrence matrix (still
denoted) L = L1 ∈ R recursively presented by

L1 = 1, ( L1
L2 L3
 ) , L2 = 1, ( L1
L2 −L3
 ) , L3 = 1, ( L1
−L2 L3
 ) .

6.2.1 The recurrence matrices L−1
i

The lower triangular recurrence matrices L1, L2, L3 deﬁned above are invert-
ible in R with inverse elements M1 = L−1
1 , M2 = L−1
2 , M3 = L−1
3 recursively
presented by

M1 = 1, ( M1
M M3
 ) , M2 = 1, ( M1
−M −M3
 ) , M3 = 1, ( M1 0
−M M3
 )

where M = M1 − M2 − M3.
 25

Proposition 6.3. The map

L1 ↦−→
 

 1 0 2
0 1 0
0 0 1
 

 , L2 ↦−→
 

 0 1 1
1 0 1
0 0 1
 

 , L3 ↦−→
 

 1 0 0
0 1 2
0 0 1
 



(where the three matrices correspond to the three aﬃne maps (x, y) ↦→ (x +
2, y), (x, y) ↦→ (y + 1, x + 1), (x, y) ↦→ (x, y + 2) of R2) deﬁnes a faithful linear
representation of the group ⟨L1, L2, L3⟩ ⊂ R generated by L1, L2, L3.
Moreover, the group homomorphism Li ↦−→ π2(Li) is faithful on ⟨L1, L2, L3⟩.

Proof We check that L1 and L3 commute. They generate thus an abelian
subgroup Γa which is easily seen to be free abelian of rank 2 by considering
the 4 × 4 matrices π2(L1) and π2(L3). Checking the relations

L2
2 = L1L3, L2L3 = L1L2, L2L1 = L3L2

shows that Γa is of index 2 in ⟨L1, L2, L3⟩ and these relations deﬁne the
aﬃne group of Proposition 6.3.
Faithfulness of the homomorphism Li ↦−→ π2(Li) follows from the obser-
vation that the subgroup generated by π2(L1), π2(L3) is free abelian of rank
2 and does not contain π2(L2). ✷

7 On the Jacobi-Dirichlet character

This section contains the most important data for proving Theorem 2.7. We
omit the somewhat lengthy details.
Tedious work proving formulae analogous to Theorem 2.5 or general
principles show that the matrix J = J1 with coeﬃcients χJ (
(s+t
s )
), 0 ≤ s, t
is of complexity 9 and has a recursive presentation given by

J1 = 1, ( J1 J2
J t
2
 ) ,

J2 = 1, ( J3 J4
J5
 ) , J t
2 = 1, ( J t
3 J t
5
J t
4
 ) ,

J3 = 1, ( J1 J2
−J t
2
 ) , J t
3 = 1, ( J1 −J2
J t
2
 ) ,

J4 = 1, ( J3 J4
−J5
 ) , J t
4 = 1, ( J t
3 −J t
5
J t
4
 ) ,

J5 = −1, ( J t
3 J t
5
−J t
4
 ) , J t
5 = −1, ( J3 −J4
J5
 ) ,

where X t = X[0]t, X[1]t, X[2]t, . . . for X ∈ A.
The matrix J has an J = LDLt decomposition in R with L of complexity
20 and D of complexity 4.
 26

The lower triangular recurrence matrix L = L1 involved in the decom-
position J = LDLt has the recursive presentation:

L1 = 1, ( L1 0
L2 L3
 ) , L2 = 1, ( L4 L5
L6 L7
 ) ,

L3 = 1, ( L8 0
L9 L10
 ) , L4 = 1, ( L1 L11
L2 L3
 ) ,

L5 = 2, ( L12 L13
0 0
 ) , L6 = 1, ( L4 L14
L6 L7
 ) ,

L7 = 1, ( L8 − L12 L15
L9 L10
 ) , L8 = 1, ( L1 0
1/3L2 L3
 ) ,

L9 = 1/3, ( L4 3L5
1/3L6 L7
 ) , L10 = 1, ( L8 0
1/3L9 L10
 ) ,

L11 = 2, ( L16 L13
L17 L18
 ) , L12 = 4/3, ( L19 4L5
0 0
 ) ,

L13 = 4, ( 2/3L12 2L13
0 0
 ) , L14 = 0, ( L12 + L16 L20
L17 L18
 ) ,

L15 = 2, ( −2/3L12 + L16 L13
1/3L17 L18
 ) , L16 = −2/3, ( −2/3L1 2L11
2/3L2 2L3
 ) ,

L17 = 2/3, ( −2/3L4 −4L5 + 2L14
2/3L6 2L7
 ) ,

L18 = 2, ( −2/3L8 − 2/3L12 2L15
2/3L9 2L10
 ) ,

L19 = 8/3, ( 2L19 8/3L5
0 0
 ) ,

L20 = −4, ( 4/3L12 − 2/3L16 −2L13 + 2L20
2/3L17 2L18
 ) .

The four matrices L5, L12, L13, L19 span a somewhat trivial four-dimensional
subalgebra consisting only of matrix sequences with zero coeﬃcients except
for the ﬁrst row.
Consideration of the images ρ(s, t)L yields the following decomposition
of the recursively closed vector space L = ⊕20
j=1 CLj:

ρ(0, 0)V = CL1 ⊕ CL4 ⊕ CL8 ⊕ CL12 ⊕ CL16 ⊕ CL19 ,
ρ(0, 1)V = CL5 ⊕ CL11 ⊕ CL13 ⊕ CL14 ⊕ CL15 ⊕ CL20 ,
ρ(1, 0)V = CL2 ⊕ CL6 ⊕ CL9 ⊕ CL17 ,
ρ(1, 1)V = CL3 ⊕ CL7 ⊕ CL10 ⊕ CL18 .

I ignore if the vector space L contains generators of interesting algebras
or groups.
The diagonal recurrence matrix D = D1 involved in J = LDLt is of

27

complexity 4 with recursive presentation

D1 = 1, ( D1 D2
 ) , D2 = −1, ( D3 D4
 ) ,

D3 = 3, ( 3D1 1/3D2
 ) , D4 = −1/3, ( 3D3 1/3D4
 ) .

8 q−binomials

Proof of Theorem 2.9 The result holds for b = 0 or for a ≤ b. An
induction on a + b ends the proof. It splits into the four following subcases:
If a, b ̸≡ 0 (mod n):
(a
b)
q = ωb(a−1
b )

ω + (a−1
b−1)
ω
= (⌊a/n⌋
⌊b/n⌋) (
ωb(a−1 (mod n)
b (mod n) )
ω + (a−1 (mod n)
b−1 (mod n))

ω
)

= (⌊a/n⌋
⌊b/n⌋)(a (mod n)
b (mod n))
ω

If a ≡ 0 (mod n), b ̸≡ 0 (mod n):
(a
b)
q = ωb(a−1
b )
ω + (a−1
b−1)

ω
= (a/n−1
⌊b/n⌋ ) (
ωb( n−1
b (mod n)
)
ω + ( n−1
(b−1) (mod n)
)
ω
)

= (a/n−1
⌊b/n⌋ )( n
b (mod n))

ω

and ( n
b (mod n))

ω = 0 since b ̸≡ 0 (mod n) implies that it is divisible by the
n−th cyclotomic polynomial.
If a ̸≡ 0, b ≡ 0 (mod n):
(a
b)
q = ωb(a−1
b )
ω + (a−1
b−1)

ω
= (a−1
b )
ω + ( ⌊a/n⌋
b/n−1
)(a−1 (mod n)
n−1 )
ω
= (⌊a/n⌋
b/n )(a−1 (mod n)
0 )

ω + 0

= (⌊a/n⌋
b/n )(a (mod n)
0 )

ω

If a ≡ b ≡ 0 (mod n):
(a
b)
q = ωb(a−1
b )
ω + (a−1
b−1)

ω
= (a/n−1
b/n )(n−1
0 )
ω + (a/n−1
b/n−1)(n−1
n−1
)
ω
= (a/n
b/n)(
0
0)

ω ✷

Remark 8.1. I thank C. Krattenthaler for pointing out that Theorem 2.9
follows also from the classical q−binomial identity

n−1∏

j=0(1 − qjt) =
 n∑

k=0(−t)
kq(
k
2)(n
k
)
q .

28

Setting n = a and q = ω for ω a primitive d−th root of 1 and equating the
coeﬃcients of tb on both sides implies the result easily for odd d. The case
of d even requires also a sign analysis.
The above identity follows by induction on n from the easy computation

∏n
j=0(1 − qjt) = (1 − qnt) ∑n
k=0(−t)kq(k
2)(n
k)

q
= 1 + ∑n+1
k=1(−t)kq(
k
2) (( n
n−k)
q + qn+1−k( n
n+1−k)
q
)

= ∑n+1
k=0(−t)kq(k
2)(n+1
k )

q .

Theorem 2.9 implies in particular that for ω = e2iπk/n, the complex
numbers (
a
b)

ω, a, b ∈ N belong to the ﬁnite subset ∪0≤b≤a<nR≥0(a (mod n)
b (mod n))

ω
of real half-lines in C.
For n = 2, the matrix (a
b)
−1, 0 ≤ a, b < 2 is given by

( 1 0
1 1
 ) .

This implies that (a
b)
−1 ∈ N for all a, b ∈ N.
For n = 4 we get (a
b)
i ∈ N ∪ iN ∪ (1 + i)N since we have






 1
1 1
1 1 + i 1
1 i i 1
 





for the matrix with coeﬃcients (a
b)

i, 0 ≤ a, b < 4.

8.1 Tensor products

Replacing coeﬃcients in the ground-ﬁeld C by multiples of a ﬁxed matrix
X of size 2K × 2K , one can consider the tensor product

A ⊗ X = (A[0] ⊗ X, A[1] ⊗ X, . . . )

of A ∈ A or A ∈ R with X. Such an element has an LU decomposition
A ⊗ X = (L′ ⊗ LX)(U ′ ⊗ UX) involving elements of the same form if and
only if we have decompositions A = L′U ′ ∈ R and X = LXUX.

Remark 8.2. More generally, one can consider the quotient algebras A/FS
and R/FS where FS is the ideal of all matrix sequences in A which in-
volve only ﬁnitely many non-zero matrices. Elements of the quotient alge-
bra R/FS can be represented as linear combinations of suitable elements
in ∪K∈NR ⊗ M2K ×2K and such representations are sometimes simpler than
recursive presentations of preimages in R.

29

8.2 The Beeblebrox reduction of (s+t
s )
−1

We denote by Z ′ the inﬁnite symmetric matrix with coeﬃcients Z ′
s,t =
χB(
(s+t
s )
−1) given by the Beeblebrox reduction of q−binomials evaluated
at q = −1.
Theorem 2.9 and Section 8.1 imply that Z ′ = L′D′(L′)t where

Z ′ = Z ⊗ ( 1 1
1
 ) , L′ = L ⊗ ( 1
1 1
 ) , D′ = D ⊗ ( 1 −1
 )

(the tensor product X ⊗ M denotes the matrix(-sequence) obtained by re-
placing a scalar entry λ of Z by the 2 × 2 matrix M ) with Z, L, D as in the
proof of Theorem 2.6.

In particular, using Theorem 2.6 and the LU decomposition of ( 1 1
1
 ) =
(
χB(
(s+t
s )

−1)
)

0≤s,t≤1, one can easily write down a formula for det(Z ′(n)) ∈

±3N with Z ′(n) denoting the symmetric n × n submatrix consisting of the
ﬁrst n rows and columns of Z ′.

Remark 8.3. The case of the matrix (with coeﬃcients in {0, 1}) obtained by
reducing (s+t
s )
−1 modulo 2 yields nothing new since (s+t
s )
−1 ≡ (s+t
s )
1 = (s+t
s )

(mod 2).

8.3 Reduction modulo 2 and Beeblebrox reduction of (s+t
s )

i
Let M ′ be the symmetric matrix with coeﬃcients

ψ(
(s + t
s
 )
i) ∈ {0, ±1, ±x, ±y}, 0 ≤ s, t

where
 ψ(ξ) =
 



 γ(ξ) if ξ ∈ N
γ(a)x if ξ = ai ∈ iN
γ(a)y if ξ = a(1 + i) ∈ (1 + i)N

where γ : N −→ {0, ±1} is either the reduction modulo 2 with values in
{0, 1} or the Beeblebrox reduction χB.

30

As in section 8.2 we have M ′ = L′D′(L′)t where

M ′ = M ⊗
 




 1 1 1 1
1 y x
1 x
1
 



 ,

L′ = L ⊗
 




 1
1 1
1 1−x
1−y 1
1 1
1−y y−x
x2−2x+y 1
 



 ,

D′ = D ⊗
 





 1 y − 1 x2−2x+y
1−y −x2
x2−2x+y
 




 .

M, L, D are given by the matrices P, L, D, respectively Z, L, D occuring in
the proof of Theorem 2.1, respectively 2.6, if γ is the reduction modulo 2,
respectively the Beeblebrox reduction.
It follows that the determinant det(M ′(n)) of the ﬁnite matrix M ′(n)
consisting of the ﬁrst n rows and columns of M ′ is of the form

±3
Nx2N(y − 1)
{0,1}(x2 − 2x + y)
{0,1}

with powers of 3 only involved if γ is the Beeblebrox reduction. The factor
(y − 1) appears if and only if n ≡ 2 (mod 4) and the factor (x2 − 2x + y)
appears if and only if n ≡ 3 (mod 4). Using Theorem 2.1, respectively
Theorem 2.6, it is easy to write down a formula for det(M ′(n)).
Acknowledgements I thank L. Bartholdi, M. Brion, P. de la Harpe
and C. Krattenthaler for helpful comments and discussions.

References

[1] J.-P. Allouche, J. Shallit, Automatic Sequences. Theory, Applications,
Generalizations, Cambridge University Press (2003).

[2] R. Bacher, R. Chapman, Symmetric Pascal matrices modulo p, Europ.
J. of Comb. 25 (2004), 459–473.

[3] R. Bacher, La suite de Thue-Morse et la cat´egorie Rec, C. R. Acad. Sci.
Paris, Ser. I.

[4] R. Bacher, Recurrence matrices, arXiv:math/0601372.

[5] L. Bartholdi, Branch rings, thinned rings, tree enveloping rings, Israel
J. Math. 154 (2006), 93–139.
 31

[6] G. Gasper, M.Rahman, Basic hypergeometric series, Encyclopedia of
mathematics and its applications (96), Cambridge University Press.

[7] A. Granville, Zaphod Beeblebrox’s brain and the ﬁfty-ninth row of Pas-
cal’s triangle, Amer. Math. Monthly 99 (1992), no. 4, 318-331.

[8] A. Granville, Correction to: ”Zaphod Beeblebrox’s brain and the ﬁfty-
ninth row of Pascal’s triangle”, Amer. Math. Monthly 104 (1997), no.
9, 848-851.

[9] R.I. Grigorchuk, Burnside’s problem on periodic groups, Funct. Anal.
Appl. 14 (1980), 41–43.

[10] E.E. Kummer, ¨Uber die Erg¨anzungss¨atze zu den allgemeinen Re-
ciprocit¨atsgesetzen, J. Reine Angew. Math. 44 (1852), 93–146.

[11] E. Lucas, Sur les congruences des nombres eul´eriens et les coeﬃcients
diﬀ´erentiels des fonctions trigonom´etriques suivant un module premier,
Bull. Soc. Math. France 6 (1878), 49–54.

[12] S. Sidki, A primitive ring associated to a Burnside 3-group. J. London
Math. Soc. (2) 55 (1997), 55–64.

Roland BACHER
INSTITUT FOURIER
Laboratoire de Math´ematiques
UMR 5582 (UJF-CNRS)
BP 74
38402 St Martin d’H`eres Cedex (France)

e-mail: Roland.Bacher@ujf-grenoble.fr

32
