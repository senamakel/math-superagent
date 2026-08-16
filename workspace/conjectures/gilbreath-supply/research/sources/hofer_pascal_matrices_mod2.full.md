<!-- source: https://arxiv.org/pdf/2502.01343 | converted from PDF -->

A note on matrices over Z with entries stemming from
binomial coefficients and from Catalan numbers once pure
and once taken modulo 2

Roswitha Hofer∗

February 4, 2025

Abstract

The Pascal matrix, which is related to Pascal’s triangle, appears in many places in the
theory of uniform distribution and in many other areas of mathematics. Examples are the
construction of low-discrepancy sequences as well as normal numbers or the binomial trans-
forms of Hankel matrices. Hankel matrices which are defined by Catalan numbers and related
to the paperfolding sequence are interesting objects in number theory. Therefore, matrices
that share many properties with the Pascal matrix or such Hankel matrices are of interest.
In this note we will collect common features of the Pascal matrix and the same modulo 2 as
well as the Hankel matrix defined by Catalan numbers once pure and once modulo 2 in the
ring of integers. Hankel matrices with only 0 and 1 entries in e.g. finite fields gave recently
access to counterexamples to the so-called X-adic Liouville conjecture. This justifies as well
as motivates our consideration of further matrices with 0 and 1 entries.

Keywords: Pascal matrices, Hankel matrices, Catalan numbers, paperfolding sequences
MSC2010: 11C20, 11B50.

1 Introduction

In this note we collect and work out nice coincidences between the pure Pascal matrix—that is
built by the binomial coefficients—and between this Pascal matrix taken modulo 2, both consid-
ered as matrices in the ring of integers. Further interesting coincidences are detected between
different Hankel matrices determined by the Catalan numbers once pure and once modulo 2. We
will organize our note as follows. Section 2 is devoted to the Pascal matrix which is used for
constructing digital sequences in the sense of Niederreiter and for constructing normal numbers
both satisfying low discrepancy bounds. The noted coincidences with the Pascal matrix modulo
2, therefore makes this matrix to a potential candidate for constructing further low-discrepancy
sequences and further interesting normal numbers. Section 3 is centred on Hankel matrices deter-
mined by the Catalan numbers once pure and once modulo 2. Such Hankel matrices are related
to low-discrepancy Kronecker-type sequences. Matrices and sequences with 0-1 entries exclusively
but considered in a field or ring with more than two elements, might be interesting in various
branches in mathematics. One recent example is the Hankel matrix determined via a paperfold-
ing 0-1 sequence (fk)k≥1 considered as elements in the finite field with 3 elements. The related
formal Laurent series ∑

k≥0 fkX −k over F3 has been identified as a counterexample to the X-adic
Littlewood conjecture by Adiceam, Nesharim, and Lunnon [1] (see also [10] fur further results).
A concluding Section 4 discusses the role of the matrices in this note for different areas of mathe-
matics.

∗Institute of Financial Mathematics and Applied Number Theory, Johannes Kepler University Linz, Altenberg-
erstr. 69, 4040 Linz, Austria. e-mail: roswitha.hofer@jku.at

1arXiv:2502.01343v1  [math.NT]  3 Feb 2025
We will make use of the following notation. For a matrix C = (ci,j)i,j≥0 over any set we
denote by C (n,m,k) the n × m matrix (ci,j)0≤i≤n,k≤j≤k+m, in words the upper n × m submatrix
of C starting with column k. If m = n we will write C (n,k) instead of C (n,n,k) for the sake of
simplicity. If, furthermore, k = 0 we just write C (n) for C (n,n,0).

2 Nice coincidences for the Pascal matrix

There are two ways of defining the so-called Pascal matrix related to Pascal’s triangle. The first
gives an upper triangular matrix, i.e.,
 P1 := ((j
i
))
i,j≥0,

where (j
i) is considered to be zero if i > j. The second a symmetric matrix, i.e.

P2 := ((
j + i
i
 ))
i,j≥0.

As well as the binomial coefficient, the Pascal matrices are well studied objects. In the following
Theorem A we list some nice and well-known properties of these two versions of the Pascal matrix
and add some references for the interested reader.

Theorem A. 1. We have P T
1 P1 = P2. (See e.g. [19, Equ. (6)]).

2. Let a ∈ Z \ {0}. Then P a
1 = (
(j
i)a
j−i)i,j≥0 =: P1(a). (Cf. e.g. [15, Proposition 2]).

3. We set P1(0) = (δi,j)i,j≥0, where δi,i = 1 and δi,j = 0 whenever i ̸= j. Then P1(a)P1(b) =
P1(a + b) for all a, b ∈ Z. (This is an easy consequence of Item 2.)

4. The matrices P1(0), P1(1), . . . , P1(p − 1) all taken (mod p) with p ∈ P are qualified to
construct a so-called (0, p)-sequence in the sense of Niederreiter. These sequences are well-
established as Faure sequences in the literature. (Cf. e.g. [15, Example 2] and the references
therein.)

5. The matrix P2 mod p with p ∈ P is qualified to construct a normal number in base p with
best known discrepancy behavior. (See [16, 17, 18]).

6. Every upper left n × n submatrix of P2 has determinant 1, i.e. det(P (n)
2 ) = 1 for every
n ∈ N. (See [7, Theorem 1.2].)

7. Every upper n × n submatrix of P1 has determinant 1, i.e., det(P (n,k)
1 ) = 1 for every n ∈ N
and every k ∈ N0. (See [7, Theorem 1.1].)

8. Every upper n × n submatrix of P2 has determinant 1, i.e., det(P (n,k)
2 ) = 1 for every n ∈ N
and every k ∈ N0. (This is an easy consequence of Items 7 and 1.)

Remark 1. The statement in Item 4 above uses the notion of (t, s)-sequences in the sense of
Niederreiter. A condition for s, N0 ×N0-matrices C1, C2, . . . , Cs over Fp, with p ∈ P such that they
are qualified to construct a low-discrepancy (t, s)-sequence with fixed t ∈ N0 can be formulated as
follows. For every integer m > t and all choices of d1, d2, . . . , ds ∈ N0 such that d1 + d2 + · · · + ds =
m − t the (m − t) × m matrix formed by stacking C (d1,m,0)
1 , C (d2,m,0)
2 , ..., C (ds,m,0)
s has full row
rank m − t. (The interested reader is referred to e.g. [9] for the construction algorithm of the
s-dimensional sequence based on C1, C2, . . . , Cs over Fp—the so-called digital method—and for
the definition and properties of the discrepancy of a sequence.)

2

In the following we define the Pascal matrices over Z with 0-1 entries, which we abbreviate to
M1 and M2, by taking the entries of P1 and P2 modulo 2, i.e.

M1 = ((
j
i
) (mod 2))
i,j≥0 and M2 = ((
j + i
i
 ) (mod 2))
i,j≥0.

Furthermore, we set for a ∈ Z \ {0}

M1(a) := (((j
i
) (mod 2))a
s2(j)−s2(i))
i,j≥0,

where s2(n) denotes the binary sum-of-digits, i.e. s2(n) = n0 + n1 + n2 + · · · where n =
n0 + n12 + n222 + · · · is the unique binary representation of n with ni ∈ {0, 1} for all i ≥ 0.
For a = 0, we set M (0) = (δi,j)i,j≥0.

Some of the items in Theorem A were already (partially) re-identified for M1 and M2 resp.

(I) Every upper left n × n submatrix of M2 ∈ Z
N0×N0 has determinant ±1. Indeed we have
det(M (n)
2 ) = ∏n−1
k=0 (−1)s2(k) for every n ∈ N. (See [5, Theorem 1.1 (i)].) This is an analogue
to Item 6.

(II) Every upper n × n submatrix of M1 has determinant ±1, i.e. det(M (n,k)
1 ) = ±1 for every
n ∈ N and every k ∈ N0. (See [20, Theorem 1].) This is an analogue of Item 7 in Theorem A.

(III) The matrix M2 in Z
N0×N0 is qualified to construct a normal number in any base b ∈ N \ {1}
with good discrepancy behavior. (See [18], in which Item (II) was claimed but not proven.)
This is an analogue of Item 5 in Theorem A.

In the following Theorem 1 and its corollaries we show some more coincidences between M1, M2
and P1, P2 as well as M1(a) and P1(a).

We start with the main Theorem 1 that represents an analogue of Item 2 as well as Item 3 in
Theorem A.

Theorem 1. We have M1(a)M1(b) = M1(a + b) for all a, b ∈ Z.

Proof. We may assume that both a and b are nonzero. Note that the case where a = 0 or b = 0
is obvious. We heavily use Lucas’ Theorem modulo 2, which states
(j
i
) (mod 2) =
 ∞∏

k=0
 (jk
ik
 ), (1)

where i = i0 + i12 + i222 + · · · and j = j0 + j12 + j22
2 + · · · are the binary representations of i
and j. Obviously, (j
i) mod 2 = 1, if jk ≥ ik for all k ≥ 0 and (j
i) mod 2 = 0, else. Here and in
the following [C]i,j denotes the coefficient of C ∈ Z
N0×N0 in the ith row and jth column.
We compute [M1(a) · M1(b)]i,j by using the binary representation of l = l0 + l12 + l22
2 + · · · :

[M1(a) · M1(b)]i,j =
 ∞∑

l=0[M1(a)]i,l · [M1(b)]l,j

=
 ∞∑

l=0
 ((l
i
) (mod 2))a
s2(l)−s2(i)((j
l
) (mod 2))bs2(j)−s2(l)

= a
−s2(i)b
s2(j) ∞∏

k=0
 1∑

lk=0
 (jk
lk
 )(lk
ik
)
alk b−lk

=
 ∞∏

k=0 a
−ik bjk jk∑

lk=ik
 (jk
lk
 )(lk
ik
)
a
lk b−lk .

3

We observe

a−ik bjk jk∑

lk=ik
 (
jk
lk
 )(lk
ik
)a
lk b
−lk =
 



 0 = (jk
ik)(a + b)
jk−ik if 1 = ik > jk = 0
a
−ik bjk = (jk
ik)(a + b)
jk−ik if ik = jk = 0
a
−ik bjk a+b
b = (jk
ik)(a + b)
jk−ik if 0 = ik < jk = 1
a
−ik bjk a
b = (jk
ik)(a + b)
jk−ik if ik = jk = 1.

Finally, we arrive at the desired equality,

[M1(a) · M1(b)]i,j =
 ∞∏

k=0 a
−ik bjk jk∑

lk=ik
 (
jk
lk
 )(lk
ik
)a
lk b
−lk

=
 ∞∏

k=0
 (
jk
ik
 )
(a + b)
jk−ik = (
(
j
i
) (mod 2))(a + b)s2(j)−s2(i) = [M1(a + b)]i,j.

The following Lemma 1 reproves the LDU factorisation of M2 ∈ Z
N0×N0 , which was also used
in [20]. This Lemma 1 is an analogue to Item 1 in Theorem A.

Lemma 1. We have M T
1 diag(((−1)ti)i≥0)M1 = M2 where ti := s2(i) (mod 2) is the i-th element
of the Thue–Morse sequence (ti)i≥0.

Proof. We compute by applying Lucas’ Theorem modulo 2 (see equation (1)) and by using the
binary representation of l = l0 + l12 + l22
2 + · · · :

[M T
1 diag((−1)
ti)i≥0)M1]i,j = ∑

l≥0
 ((i
l
) (mod 2))(−1)s2(l)((j
l
) (mod 2))

= ∏

k≥0
 1∑

lk=0
 (
ik
lk
)(−1)lk (
jk
lk
 )

= ∏

k≥0
 (1 + (−1)(
ik
1
 )(jk
1
 ))

= ∏

k≥0
 ((
ik + jk
ik
 ) (mod 2))

= (i + j
i
 ) (mod 2),

where in the last step we used that (i+j
i ) (mod 2) = 0 if there occurs at least one carry when
adding the binary expansions i = i0 + i12 + i22
2 + · · · and j = j0 + j12 + j22
2 + · · · , and (i+j
i )

(mod 2) = 1 else.

The following Corollary 1 reproves [5, Theorem 1.1] that serves as an analogue Item 6 of
Theorem A.

Corollary 1. Let n ∈ N. Every upper left n × n submatrix of M2 has determinant ∏n−1
i=0 (−1)s2(i),
i.e., det(M (n)
2 ) = ∏n−1
i=0 (−1)s2(i) for every n ∈ N.

Proof. From Lemma 1 we know (M (n)
1 )
T diag((−1)ti)0≤i<nM (n)
1 = M (n)
2 . Since M1 is a non-
singular upper triangular matrix with diagonal entries all 1 we immediately obtain det(M (n)
2 ) =
det(diag((−1)ti)0≤i<n) = ∏n−1
i=0 (−1)s2(i).

The next Corollary 2 even generalizes [20, Theorem 1] the analogue of Item 7 in Theorem A .

4

Corollary 2. Let n ∈ N, k ∈ N0, and a ̸= 0. The upper n × n submatrix of M1(a) starting with
column k has determinant ± ∏n−1
i=0 a
s2(i+k)−s2(i), i.e., det(M (n,k)
1 (a)) = ± ∏n−1
i=0 a
s2(i+k)−s2(i) for
every n ∈ N and every k ∈ N0.

Proof. We observe first M1(a) = diag((a−s2(i))i≥0)M1(1)diag((a
s2(i))i≥0). Thus

M1(a)
(n,k) = diag((a
−s2(i))0≤i<n)M1(1)
(n,k)diag((a
s2(i))k≤i<n+k).

Using [20, Theorem 1] we know det(M1(1)
(n,k)) = ±1 and the result follows.

Finally, Corollary 3 and Remark 2 partially give an analogue of Item 4 of Theorem A, as
they ask whether matrices in {M1(a) : a ∈ N0} might be used to construct low-discrepancy (t, s)-
sequences in the sense of Niederreiter or not. Note that the matrices in {P1(a) : a ∈ N0} are used
to construct the low-discrepancy Faure sequences (see Item 4 in Theorem A.)

Corollary 3. Let p ∈ P and a, b ∈ Z such that a ̸≡ b (mod p). Then M1(a), M1(b) modulo p are
qualified to construct a (0, 2)-sequence over Fp in the sense of Niederreiter.

Proof. Let c := b − a ̸≡ 0 (mod p), m ∈ N, and d1, d2 ≥ 0 such that d1 + d2 = m. Corollary 2
ensures that every upper d2 × d2 submatrix of M1(c) has determinant ̸≡ 0 (mod p). This together
with the fact that M1(0) = (δi,j)i,j≥0 immediately yields the linear independence of the system
of vectors ([M1(0)]i,0, . . . , ([M1(0)]i,m−1), 0 ≤ i < d1 and ([M1(c)]i,0, . . . , ([M1(c)]i,m−1), 0 ≤
i < d2. Hence M1(0), M1(c) are qualified to construct a (0, 2) sequence in base p in the sense of
Niederreiter. From the fact that M1(a) is a non-singular upper triangular matrix with determinant
1 we know then that the system of vectors ([M1(0)M1(a)]i,0, . . . , ([M1(0)M1(a)]i,m−1), 0 ≤ i < d1
and ([M1(c)M1(a)]i,0, . . . , ([M1(c)M1(a)]i,m−1), 0 ≤ i < d2 are linear independent modulo p. From
Theorem 1 we obtain that M1(0)M1(a) = M1(a), that M1(c)M1(a) = M1(b). Thus M1(a), M1(b)
are qualified to construct a (0, 2)-sequence in base p in the sense of Niederreiter.

Remark 2. Theorem A, Item 4 allows to construct three-dimensional low-discrepancy (0, 3)-
sequences over Fp with any odd prime p by using, e.g., P1(0), P1(1), P1(2) taken modulo p ≥ 3.
It is not possible to further generalize the statement in Corollary 3 to dimensions > 2 in the
sense of Item 4 in Theorem A. Choose e.g. C1 = M (0), C2 = M (1), C3 = M (2), m = 3, and
d1 = d2 = d3 = 1. Then the three vectors (1, 0, 0), (1, 1, 1), and (1, 2, 2) are linearly dependent,
which contradicts the condition for a (0, 3)-sequence in base p ≥ 3.
An interesting question, however, is: does there exist a non-singular upper triangular matrix
C ∈ Z
N0×N0 such that M (0), M (1), C are qualified to construct a (0, 3)-sequence (or at least a
(t, 3)-sequence in base 3 with small t ∈ N0) and if so finding an explicit formula for the entries
of C might be of interest. Note that the condition on C1, C2, C3 that are qualified to construct a
(0, 3)-sequence over F3 is quite strict. (See e.g. [14] and [15] for discussions on C1, C2 over F2 to
be qualified to construct a (0, 2)-sequence.)

3 The nice coincidences for the Hankel matrix determined
by the Catalan numbers

A Hankel matrix H = (hi,j)i,j≥0 can be uniquely described by a sequence (ck)k≥0 as hi,j = ci+j
for all i, j ≥ 0. In this section we focus on Hankel matrices H1, H2 with (ck)k≥0 stemming from
Catalan numbers interspersed with zeros, i.e.,

c2k = (−1)kCk and c2k+1 = 0

for all k ≥ 0 with Ck := (2k
k ) − ( 2k
k−1
) = 1
k+1 (2k
k ) once taken pure and once taken modulo 2 but
both considered as integers.
Hence H1 = (h
(1)
i,j )i,j≥0 and H2 = (h
(2)
i,j )i,j≥0

5

with h
(1)
i,j = ci+j and h
(2)
i,j = (ci+j (mod 2)). Note that as an easy consequence of Lucas’ Theorem

modulo 2 (see equation (1)), H2 = (h
(2)
i,j )i,j≥0 with h
(2)
i,j = 1 if i + j = 2
k − 2 for some some k ∈ N

and h
(2)
i,j = 0 otherwise.

We start with a common property of the principal minors of both Hankel matrices H1 and H2.
The nth principal minor of a matrix C is the determinant of the upper left n × n submatrix, i.e.
det(C (n)).

Theorem 2. We have det(H (n)
1 ) = ±1 as well as det(H (n)
2 ) = ±1 for all n ∈ N.

Proof. The first is a consequence of [13, Lemma 1] together with [13, Proposition 1], which ensures
det(H (n)
1 ) (mod p) ̸≡ 0 for every n ∈ N and every p ∈ P.
The second is an immediate consequence of the ArXiv paper [4, Theorem 10.1 (i)], which gives
the LDU decomposition of H2. (Details on the LDU decomposition can be found in the subsequent
Remark 3). As [4] is an ArXiv paper we give a proof of the second statement of this Theorem 2.

We observe that H (2k−1)
2 is an anti-diagonal upper triangular matrix with anti-diagonal-entries all

equal to 1 for all k ∈ N. Hence, obviously det(H (2k−1)
2 ) = ±1 for all k. For det(H (n)
2 ) = ±1 for all
2k − 1 < n < 2
k+1 − 1 we proceed by induction on k. Let k in N and assume that n = 2
k − 1 + l
with 1 ≤ l < 2k. The induction hypothesis ensures det(H (m)
2 ) = ±1 for all m ≤ 2k − 1. We do row

as well as column manipulation in H (2k−1+l)
2 without changing the determinant. In more details
we exploit the anti-diagonal part denoted by J2l+1 in the right bottom of this matrix. We obtain

then a matrix Q of the form Q =
 (H (2k−1−l+1)
2 0
0 J2l−1
)
 where 0 stands for a submatrix with

all entries equal to 0. Now obviously, det(Q) = det(H (2
k−1−l+1)
2 ) · det(J2l−1) = ±1, where for the

last equality we used the induction hypothesis for n = 2
k − l. A sketch of the matrices H (2k−1+l)
2
and Q, which contains H (2k−1−l+1)
2 and J2l−1, can be found in Figure 1.

Figure 1: Sketch of H (2
k−1+l)
2 and Q.

Remark 3. One consequence of Theorem 2 is that both matrices H1 and H2 have a unique LDU
decomposition where L is a lower triangular matrix with diagonal-entries all 1, U is an upper
triangular matrix with diagonal-entries all 1 and D is a diagonal-matrix with entries ±1. [4,
Theorem 10.1 (i)] gives the LDU decomposition of H2, which was already used as an alternative
argument in the proof of Theorem 2. Such LDU decomposition with additionally U = L
T were
already investigated e.g. in [21], where L is constructed row wise using a tritriangular so-called
Stieltjes matrix. See also [4] and [22]. In [4] the LDU decomposition of some further Hankel
matrices are given. One example is the Hankel matrix H = (hi,j)i,j≥0 over Z with hi,j = Ci+j
(mod 2) (see [4, Theorem 10.1]).
 6

A slightly different version of this LDU decomposition is an LU decomposition with L and
U be non-singular lower or upper resp. triangular matrices. Theorem 1 and Proposition 1 in
[13] investigate such an LU decomposition of H1 together with the continued fraction expansion
of the related formal Laurent series ∑

k≥0 ckX −k−1. The relevant tool for the investigation is
a construction of L and U with tritriangular matrices comparable with the Stieltjes matrix in
[21] but defined via the continued fraction expansions with coefficients having all degrees 1 of the
formal Laurent series. Using [13, Lemma 1] together with Theorem 2 we see that both Laurent
series ∑
k≥0 ckX −k−1 as well as ∑

k≥0(ck (mod 2))X −k−1 have continued fraction expansion with
[0; A1(X), A2(X), A3(X), . . .] with deg(Ai(X)) = 1 for all i ≥ 1. The following proposition gives
explicit formulas for those Ai(X). Although these results are not new, we would like to summarise
them here in a proposition for the interested reader.

Proposition 1. Let L1 = ∑
k≥0 ckX −k−1 and L2 = ∑
k≥0(ck (mod 2))X −k−1 be formal Laurent
series over Q, with c2k = (−1)
kCk and c2k+1 = 0.

The continued fraction expansions of L1 and L2 satisfy

L1 = [0; X] and L1 = [0; s1X, s2X, s3X, . . .]

with (si)i≥1 in {1, −1} is a paperfolding sequence often denoted by F(1, −1, −1, −1, . . .) (cf. e.g.
[3] for this notation), that defines (si)i≥1 = limi→∞ wi via the recursion w1 = s1 = (1), wi+1 =
wi · (−1) · (−wiR) for i ≥ 1. Here · denotes the concatenation of the finite sequences, wR denotes
the finite sequence w in reflected order, and the − in front of a finite sequence changes the signs
of the elements of the sequence.

Proof. The continued fraction L1 = [0; X] is the starting point in [13] to obtain the formal Laurent
series L1 = ∑

k≥0 ckX −k−1 determined via the Catalan numbers. Hence the first equality L1 =
[0; X] can be found in [13].
The equality [0, s1X, s2X, s3X, . . .] = ∑

k≥0(ck (mod 2))X −k−1 can be found in e.g. [3, Equa-
tion (9)], previously in e.g. [23, Theorem 1].

4 Closing discussions

The content of this note touches on results from several branches of mathematics, as, e.g.:

- Problems for a formal Laurent series ∑

k≥j ckX −k and its simple continued fraction expan-
sions. See e.g. [3] for so-called folded continued fractions, that are e.g. continued fractions
determined by paperfolding sequences, and their formal Laurant series expansions. (See also
e.g. [4], [13], [22], [23].) For work and discussions on analogs of the Littlewood conjecture
in the set of Laurent series see e.g. [1].

- Various aspects on Hankel matrices. As specific LDU or LU decompositions and determi-
nants of submatrices (see e.g. [4], [13], [21]).

- Properties of the Pascal matrices as e.g. determinants of submatrices (see e.g. [5], [19], [20]),
their usage for constructing low-discrepancy sequences and normal numbers (see e.g. [8] and
[18]).

- Finding matrices that are qualified to construct low-discrepancy (t, s)-sequences over Fp
(see e.g. the monograph [9] for an overview.) In particular the existence of Hankel matrices
over Fp that are qualified to construct (t, s)-sequences for s > 1 is an open problem. Exis-
tence would contradict the analog of the Littlewood conjecture in the set of formal Laurent
series over Fp. Such (t, s)-sequences, which are constructed via Hankel matrices, are well-
established as Kronecker-type sequences. Kronecker-type sequences are frequently studied
(see e.g. [12] and the references therein).
 7

- Finding normal numbers with low-discrepancy (see [18] and also e.g. [6], [16], [17]). As M (2n)
2
is a simple column reflection of M (2
n)
1 and it might be used for constructing low-discrepancy
normal numbers. Also the simple column reflected M (2n)
1 (a) might be a candidate for con-
structing normal numbers. An open problem for these normal numbers is to identify the
exact order of its discrepancies (cf. e.g. [16] and [17]).

- Problems concerning apwenian sequences (see e.g. [11] and the references therein.). A
0-1 apwenian sequence (cj)j≥0 can be defined via determinants of the Hankel matrix H =
(hi,j)i,j≥0 with hi,j = ci+j, namely (cj)j≥0 over {0, 1} is apwenian if and only if det(H (n)) ≡ 1
(mod 2) for every n ∈ N. From this definition a connection to the study of determinants
of submatrices of Hankel matrices is obvious. Interesting connections between apwenian
sequences and the so-called perfect linear complexity profile of pseudo random 0-1 sequences
were identified in [2]. In there a further connection to the related formal Laurent series over
F2 and its continued fraction expansion is pointed out.

We would like to close this note with the following comment stemming from the interdisciplinary
paper [2] by Allouche, Han, and Niederreiter who motivated the work therein via the sentences
“We hope that this will help gathering two distinct communities of researchers” and “One of the
intense pleasures in mathematical research is to discover a link between two fields that either did
not seem immediately related or were studied from distinct point of views”. The same two sentences
but with “two” replaced by “several” might be used to summarize the motivation of this note.

References

[1] Adiceam F., Nesharim E., and Lunnon F., On the t-adic Littlewood conjecture, Duke Math.
J. 170 (2021), no. 10, 2371–2419.

[2] Allouche J.-P., Han G.-N., and Niederreiter H., Perfect linear complexity profile and apwenian
sequences, Finite Fields Appl. 68 (2020), 101761.

[3] Allouche J.-P., Lubiw A., Mend´es France M., van der Porten, A. J., and Shallit J., Convergents
of folded continued fractions, Acta Arith. 77 (1996), no. 1, 77–96.

[4] Bacher R., Paperfolding and Catalan numbers,arXiv paper (2004), https://arxiv.org/abs/
math/0406340.

[5] Bacher R. and Chapman R., Symmetric Pascal matrices modulo p, European Journal of
Combinatorics 25 (2004), 459–473.

[6] Becher V. and Carton O., Normal numbers and nested perfect necklaces, J. Complexity 54
(2019), 101403.

[7] Bicknell M. and Hoggart V.E., Jr., Unit determinants in Pascal triangles, Fib. Quart. vol 11
(1973), no. 2, 131–144.

[8] Faure H., Discr´epance de suites associ´ees `a un syst`eme de num´eration (en dimension s), Acta
Arith. 41 (1982), no. 4, 337–351.

[9] Dick J. and Pillichshammer F., Digital nets and sequences. Discrepancy theory and quasi-
Monte Carlo integration. Cambridge University Press, Cambridge, 2010.

[10] Garrett S. and Robertson S., Counterexamples to the p(t)-adic Littlewood Conjecture Over
Small Finite Fields, arXiv:2405.14454.

[11] Guo Y., Han G., and Wu W., Criteria for apwenian sequences, Advances in Mathematics 389
(2021), 107899.
 8

[12] Hofer R., Kronecker-Halton sequences in Fp((X −1)), Finite Fields Appl. 50 (2018), 154–177.

[13] Hofer R., Finding both, the continued fraction and the Laurent series expansion of golden
ratio analogs in the field of formal power series, J. Number Theory 223 (2021), 168–194.

[14] Hofer R. and Suzuki, K., A complete classification of digital (0, m, 3) -nets and digital (0, 2)
-sequences in base 2, Unif. Distrib. Theory 14 (2019), No. 1, 43–52.

[15] Hofer R. and Larcher G., On existence and discrepancy of certain digital Niederreiter-Halton
sequences, Acta Arith. 141 (2010), no. 4, 369–394.

[16] Hofer R. and Larcher G., The exact order of discrepancy for Levin’s normal number in base
2, J. Th´eor. Nombres Bordeaux 35 (2023), no. 3, 999–1023.

[17] Hofer R. and Larcher G., Discrepancy bounds for normal numbers generated by necklaces in
arbitrary base, J. Complexity 78 (2023), Paper No. 101767, 26 pp.

[18] Levin B. M., On the discrepancy estimate of normal numbers, Acta Arithmetica, vol. 88
(1999) no. 2, pp. 99–111.

[19] Lunnon W. F., The Pascal matrix, Fib. Quart. vol. 15 (1977), no. 3, 201–204.

[20] Mereb M., On determinants of matrices related to the Pascal’s triangle, Periodica Mathemat-
ica Hungarica 89 (2024), 168–174.

[21] Peart P. and Woan W.-J., Generating Functions via Hankel and Stieltjes Matrices, Journal
of Integer Sequences 3 (2000), no. 2, Article 00.2.1.

[22] van der Poorten A., Formal power series and their continued fraction expansion, Algorithmic
Number Theory (1998), pp. 358–371, Proceedings of the Third International Symposium,
ANTS-III, Portland, Orgeon, USA, June 21-25, 1998.

[23] van der Poorten A. J. and Shallit J., Folded continued fractions, J. Number Theory 40 (1992),
no. 2, 237–250.
 9
