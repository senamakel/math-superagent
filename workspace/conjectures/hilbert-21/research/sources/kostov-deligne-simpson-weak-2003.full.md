<!-- source: https://arxiv.org/pdf/math/0310441 | converted from PDF -->

arXiv:math/0310441v1  [math.AG]  28 Oct 2003
On the Deligne-Simpson problem and its weak version

Vladimir Petrov Kostov

To Prof. Yu. S. Il’yashenko

Abstract

We consider the Deligne-Simpson problem (DSP) (resp. the weak DSP): Give necessary
and suﬃcient conditions upon the choice of the p + 1 conjugacy classes cj ⊂ gl(n, C) or
Cj ⊂ GL(n, C) so that there exist irreducible (p + 1)-tuples (resp. (p + 1)-tuples with trivial
centralizers) of matrices Aj ∈ cj with zero sum or of matrices Mj ∈ Cj whose product
is I. The matrices Aj (resp. Mj) are interpreted as matrices-residua of Fuchsian linear
systems (resp. as monodromy matrices of regular linear systems) of diﬀerential equations
with complex time. In the paper we give suﬃcient conditions for solvability of the DSP in
the case when one of the matrices is with distinct eigenvalues.

1 Introduction

1.1 Basic notions and purpose of this paper

In the present paper we consider the Deligne-Simpson problem (DSP): Give necessary and suf-
ﬁcient conditions upon the choice of the p + 1 conjugacy classes cj ⊂ gl(n, C) or Cj ⊂ GL(n, C)
so that there exist irreducible (p + 1)-tuples of matrices Aj ∈ cj satisfying the condition

A1 + . . . + Ap+1 = 0 (1)

or of matrices Mj ∈ Cj satisfying the condition

M1 . . . Mp+1 = I (2)

Convention 1 In what follows we write “tuple” instead of “(p + 1)-tuple” and the matrices Aj
(resp. Mj) are always supposed to satisfy condition (1) (resp. (2)).

The matrices Aj (resp. Mj) are interpreted as matrices-residua of a Fuchsian system of linear
diﬀerential equations (resp. as monodromy matrices of a regular linear system) on Riemann’s
sphere; see a more detailed description in [Ko1] or [Ko2].

Remark 2 The version with matrices Aj (resp. Mj) is called the additive (resp. the multiplica-
tive) version of the DSP. The multiplicative version of the problem was formulated by P.Deligne
and C.Simpson was the ﬁrst to obtain results towards its resolution, see [Si1] and [Si2]. The
additive version is due to the author.

We presume the necessary condition ∏ det(Cj) = 1 (resp. ∑
Tr(cj) = 0) to hold. In terms
of the eigenvalues σk,j (resp. λk,j) of the matrices from Cj (resp. cj) repeated with their
multiplicities, this condition reads ∏n
k=1 ∏p+1
j=1 σk,j = 1 (resp. ∑n
k=1 ∑p+1
j=1 λk,j = 0).

1

Deﬁnition 3 An equality ∏p+1
j=1 ∏k∈Φj σk,j = 1, resp. ∑p+1
j=1 ∑k∈Φj λk,j = 0, is called a non-
genericity relation; the sets Φj contain one and the same number N < n of indices for all j (when
wishing to specify N we say “N -relation” instead of “non-genericity relation”). Eigenvalues
satisfying none of these relations are called generic.

Remarks 4 1) Reducible tuples of matrices Aj or Mj exist only for non-generic eigenvalues (the
eigenvalues of each diagonal block of a block upper-triangular tuple satisfy some non-genericity
relation). Therefore for generic eigenvalues existence of tuples implies automatically their irre-
ducibility. This is not true for non-generic eigenvalues.
2) It is clear that the presence of a non-genericity relation with N = N0 implies the presence
of one with N = n−N0 (just replace the sets Φj by their complements in {1, 2, . . . , n}). Therefore
in what follows we consider only non-genericity relations with N ≤ n/2.

Part 1) of the above remarks explains why for non-generic eigenvalues it is reasonable to
require instead of irreducibility of the tuple only triviality of its centralizer (i.e. only scalar
matrices to commute with all matrices from the tuple). This is the weak version of the DSP (or
just the weak DSP for short).

Deﬁnition 5 We say that the DSP (resp. the weak DSP) is solvable for a given tuple of
conjugacy classes cj or Cj if there exist irreducible tuples of matrices Aj ∈ cj or Mj ∈ Cj (resp.
if there exist tuples of such matrices with trivial centralizers).

We assume throughout the paper that there holds

Convention 6 The conjugacy classes c1 and C1 are with distinct eigenvalues.

The purpose of the present paper is to show as precisely as possible where passes the border
between the cases when the DSP is solvable and when it is not but the weak DSP is solvable.

1.2 The known results

Deﬁnition 7 Call Jordan normal form (JNF) of size n a family J n = {bi,l} (i ∈ Il, Il =
{1, . . . , sl}, l ∈ L) of positive integers bi,l whose sum is n. Here L is the set of indices of
eigenvalues (all distinct) and Il is the set of indices of Jordan blocks with eigenvalue l, bi,l is
the size of the i-th block with this eigenvalue. An n × n-matrix Y has the JNF J n (notation:
J(Y ) = J n) if to its distinct eigenvalues λl, l ∈ L, there belong Jordan blocks of sizes bi,l. We
use the following notation (illustrated by an example): the JNF {{3, 2}, {7, 6, 1}} is the one with
two eigenvalues to the ﬁrst (to the second) of which there belong two blocks, of sizes 3 and 2
(resp. three blocks, of sizes 7, 6 and 1).

Notation 8 1) We denote by C(Y ) the conjugacy class (in gl(n, C) or GL(n, C)) of the matrix

Y . We set C(Y ) = C(X) × C(Z) if Y =
 ( X 0
0 Z
 )
 (here X is l × l and Z is (n − l) × (n − l).

2) For a conjugacy class C in GL(n, C) or gl(n, C) denote by d(C) its dimension and by
J(C) the JNF it deﬁnes. For a matrix Y ∈ C set r(C) := minλ∈C rank(Y − λI). The integer
n − r(C) is the maximal number of Jordan blocks of J(Y ) with one and the same eigenvalue.
Set dj := d(Cj) (resp. d(cj)), rj := r(Cj) (resp. r(cj)). The quantities r(C) and d(C) depend
only on the JNF J(Y ) = J n, not on the eigenvalues, so we write sometimes r(J n) and d(J n).

2

Proposition 9 (C. Simpson, see [Si1].) The following couple of inequalities is a necessary
condition for the existence of irreducible (p + 1)-tuples satisfying (2) or (1):

d1 + . . . + dp+1 ≥ 2n2 − 2 (αn)

for all j, r1 + . . . + ˆrj + . . . + rp+1 ≥ n (βn)

The above proposition holds without Convention 6. When Convention 6 holds, then r1 =
n − 1 and condition (βn) is tantamount to r2 + . . . + rp+1 ≥ n.

Deﬁnition 10 The quantity κ = 2n2 − d1 − . . . − dp+1 (see Notation 8) is called the index of
rigidity of a given tuple of conjugacy classes or of JNFs. It has been introduced by N.Katz, see
[Ka]. If condition (αn) holds, then κ can take the values 2, 0, −2, −4, . . .. The case κ = 2 is
called the rigid one.

Deﬁnition 11 A multiplicity vector (MV) is a vector whose components are non-negative in-
tegers whose sum is n. Further in the text components of the MVs are the multiplicities of the
eigenvalues of n × n-matrices.

Remark 12 For a diagonalizable conjugacy class C with MV equal to (m1, . . . , ms) one has
d(C) = n2 − m2
1 − . . . − m2
s.

Deﬁnition 13 For a given JNF J n = {bi,l} deﬁne its corresponding diagonal JNF J ′n. A
diagonal JNF is a partition of n deﬁned by the multiplicities of the eigenvalues. For each l {bi,l}
is a partition of ∑
i∈Il bi,l and J ′ is the disjoint sum of the dual partitions. Thus if for each ﬁxed
l one has b1,l ≥. . .≥ bsl,l, then the eigenvalue l ∈ L is replaced by b1,l new eigenvalues h1,l, . . .,
hb1,l,l (hence, J ′n has ∑
l∈L b1,l distinct eigenvalues).

Remarks 14 One has the following properties of corresponding JNFs (see [Ko2]:)
1) For l ﬁxed, set gk for the multiplicity of the eigenvalue hk,l. Then the ﬁrst bsl,l numbers
gk equal sl, the next bsl−1,l − bsl,l equal sl − 1, . . ., the last b1,l − b2,l equal 1.
2) There hold the equalities r(J n) = r(J ′n) and d(J n) = d(J ′n).
3) To each diagonal JNF there corresponds a unique JNF with a single eigenvalue.

Lemma 15 Given the p + 1 diagonalizable conjugacy classes cj or Cj satisfying condition (βn)
and Convention 6, condition (αn) does not hold for them only in
Case A) : p = 2, n ≥ 4 is even and the MVs of c2 and c3 (resp. of C2 and C3) both equal
(n/2, n/2).

The lemma is proved at the end of the subsection.

Remark 16 Making use of Deﬁnition 13 and Remarks 14 one can extend the lemma to the case
of not necessarily diagonalizable matrices (except A1 or M1). In such a context, in Case A) each
conjugacy class c2, c3 or C2, C3 is either diagonalizable and as in the lemma or with a single
eigenvalue and n/2 Jordan blocks of size 2 belonging to it. Indeed, this is the only non-diagonal
JNF corresponding to the one with two eigenvalues each of multiplicity n/2.

The ﬁrst important result in the resolution of the DSP was the following

Theorem 17 (C.Simpson, see [Si1]) For generic eigenvalues and under Convention 6 condi-
tions (αn) and (βn) together are necessary and suﬃcient for the solvability of the DSP for given
conjugacy classes Cj.
 3

The same result for classes cj is proved in [Ko4], Theorem 19. For arbitrary eigenvalues
there holds the following theorem (see [Ko3], Theorem 6).

Theorem 18 Under Convention 6 conditions (αn) and (βn) together are necessary and suﬃ-
cient for the solvability of the weak DSP for given conjugacy classes cj or Cj.

Remarks 19 1) In [Si1] C.Simpson has considered the rigid case for diagonalizable matrices
and under Convention 6. He has shown that conditions (αn) and (βn) together hold only if p = 2
and the MVs of the three matrices correspond to one of the four cases:

(1, . . . , 1) (1, . . . , 1) (n − 1, 1) hypergeometric family

(1, . . . , 1) ( n
2 , n
2 − 1, 1) ( n
2 , n
2 ) even family

(1, . . . , 1) ( n−1
2 , n−1
2 , 1) ( n+1
2 , n−1
2 ) odd family

(1, 1, 1, 1, 1, 1, ) (2, 2, 2) (4, 2) extra case

Observe that in all four cases one has r2 + r3 = n, i.e. there is an equality in condition (βn).
Although C.Simpson considers only matrices Mj, the result is automatically extended to the case
of matrices Aj.
2) If one wants to get rid of the condition the matrices to be diagonalizable (except A1 or
M1), then to the above list one should add all cases when a diagonal JNF from the list is replaced
by a JNF corresponding to it. All JNFs corresponding to the one with n distinct eigenvalues
are the ones in which to each eigenvalue there belongs a single Jordan block. Using the notation
from Deﬁnition 7, give the list of all JNFs corresponding to the other diagonal JNFs (deﬁned by
the MVs) encountered in part 1) of the present remarks:

(n − 1, 1) {2, 1, . . . , 1}

( n
2 , n
2 − 1, 1) {3, 2, . . . , 2, 1} or {{1, . . . , 1}{2, 1, . . . , 1}} (n/2 and n/2 − 2 units)

( n
2 , n
2 ) {2, . . . 2}

( n−1
2 , n−1
2 , 1) {3, 2, . . . , 2} or {{1, . . . , 1}{2, 1, . . . , 1}} ((n − 1)/2 and (n − 3)/2 units)

( n+1
2 , n−1
2 ) {2, . . . , 2, 1}

(2, 2, 2) {3, 3} or {{2, 2}{1, 1}}

(4, 2) {2, 2, 1, 1}

Proof of Lemma 15:
10. Suppose ﬁrst that one has

rj ≤ n/2 for j = 2, . . . , p + 1 (∗)

Then one has dj ≥ 2rj(n − rj) and there is equality if and only if the MV of cj or Cj equals
(rj, n − rj). This follows from Remark 12.
 4

For r2 + . . . + rp+1 ﬁxed the sum d2 + . . . + dp+1 is minimal for r2 = r3 = [n/2] where [.]
stands for the entire part of. Indeed, one has d2 + . . . + dp+1 = (r2 + . . . + rp+1)n − r2
2 − . . . − r2
p+1
and one has to maximize r2
2 + . . . + r2
p+1 for r2 + . . . + rp+1 ﬁxed while respecting condition (∗).
If n is even and r2 = r3 = n/2, rj = 0 for j > 3, then condition (αn) fails if and only if n ≥ 4
(this is Case A)); if r4 ̸= 0, then condition (αn) holds. If n is odd, then the sum d2 + . . . + dp+1
is minimal for r2 = r3 = [n/2], r4 = 1 and condition (αn) holds. One cannot have rj = 0 for all
j > 3 because then condition (βn) does not hold.
20. Suppose that r2 > n/2. Denote the MV of the class c2 or C2 by (m1, . . . , ms), with
m1 ≥ . . . ≥ ms. Then d2 is minimal if m1 = m2 = . . . = ms−1 = n − r2, see Remark 12. The
sum d3 + . . . + dp+1 is minimal if r3 = m1 = n − r2, r4 = . . . = rp+1 = 0 and the MV deﬁning
the class c3 or C3 equals (r2, n − r2).
Set n = (s − 1)m1 + ms. Recall that 1 ≤ ms ≤ m1. Hence,

d1 = n2 − n , d2 = n2 − (s − 1)m2
1 − m2
s ≥ n2 − m1n , d3 = 2m1(n − m1) and

d1 + d2 + d3 ≥ 2n2 − n + m1n − 2m2
1 ≥ 2n2 − n + n − 2 = 2n2 − 2 because 1 ≤ m1 < n/2

The lemma is proved. ✷

1.3 The new results

Deﬁnition 20 The eigenvalues of the matrices Aj or Mj are called k-generic, k ∈ N, if they
satisfy non-genericity relations only with N ≥ k, see Deﬁnition 3 and part 2) of Remarks 4.

Theorem 21 Under Convention 6, if the eigenvalues are 2-generic, and if κ ≤ 0 (see Deﬁni-
tion 10), then conditions (αn) and (βn) are necessary and suﬃcient for the solvability of the
DSP.

The theorem is proved in Section 2. Examples 29 and 30 below show that the theorem
cannot be made stronger.

Theorem 22 Under Convention 6 and for arbitrary eigenvalues, if r2 + . . . + rp+1 ≥ n + 1, then
the DSP is solvable for such conjugacy classes.

The theorem is proved in Section 3. Example 29 below shows that for r2 + . . . + rp+1 = n
Theorem 22 is no longer true.

Remark 23 The above two theorems imply that under Convention 6 the weak DSP is solvable
but the DSP is not only if r2 + . . . + rp+1 = n and either κ = 2 or the eigenvalues satisfy a
1-relation.

Corollary 24 Under Convention 6 a block upper-triangular tuple of diagonalizable matrices Aj
or Mj with 3-generic eigenvalues can be deformed into one from the same conjugacy classes and
with trivial centralizer.

Indeed, 3-genericity implies that for each diagonal block (say, of size s ≥ 3) there holds
condition (βs) and Case A) from Lemma 15 is avoided; hence, condition (βn) holds for the tuple
of conjugacy classes (the quantity r computed for the whole matrix is not smaller than the
sum of the quantities r computed for the diagonal blocks), and Case A) is avoided (because
the blocks are of size ≥ 3 – we leave the details for the reader). Hence, for the given tuple of
conjugacy classes there hold conditions (αn) and (βn) (see Lemma 15). The claim follows now
from Lemma 24 from [Ko3]. ✷
 5

Corollary 25 Under Convention 6, if the eigenvalues are 2-generic, and if Case A) is avoided,
then for such a block upper-triangular tuple of diagonalizable matrices Aj or Mj there hold
conditions (βn) and (αn). Moreover, the tuple can be deformed into one from the same conjugacy
classes and with trivial centralizer.

The ﬁrst claim is proved as Corollary 24, the second follows from Lemma 24 from [Ko3].

Notation 26 For a tuple of matrices Aj or Mj in block upper-triangular form
 ( Pj Qj
0 Rj
 )

(where Pj ∈ gl(l, C), Rj ∈ gl(n − l, C)) set d1
j = d(Pj), r1
j = r(Pj), d2
j = d(Rj), r2
j = r(Rj),
sj =dimXj where Xj = {Z ∈ Ml,n−l|Z = PjXj − XjRj, Xj ∈ Ml,n−l}. Denote by P, R the
representations deﬁned by the tuples of matrices Pj, Rj.

Remark 27 If the MVs of the diagonalizable matrices Pj and Rj equal respectively (m′
1, . . . , m′
s),
(m′′
1, . . . , m′′
s ) (there might be zeros among these numbers as some eigenvalue might be absent in
Pj or Rj), then sj = l(n − l) − ∑s
i=1 m′
im′′
i . This implies that if one exchanges the positions of
the blocks Pj and Rj, then the quantities sj do not change.

Lemma 28 If the representations P and R are with trivial centralizers, then one has

δ := dim Ext
1(P, R) = s1 + . . . + sp+1 − 2l(n − l) .

Proof:
Notice ﬁrst that Xj is the space of right upper blocks of matrices of the form

( I Xj
0 I
 )−1 ( Pj 0
0 Rj
 ) ( I Xj
0 I
 )
 .

To obtain δ one must ﬁrst subtract l(n−l) from ∑p+1
j=1dimXj (because the sum of these right upper
blocks must be 0) and then again subtract l(n − l) (to factor out the simultaneous conjugation

with matrices
 ( I X
0 I
 )
; as A1 or M1 is with distinct eigenvalues, no such matrix with X ̸= 0

commutes with all matrices from the tuple). ✷

Example 29 Consider under Convention 6 a tuple of diagonalizable conjugacy classes cj for
which r2 + . . . + rp+1 = n, n > 2. Denote by µ1 an eigenvalue of c1 and by µ2, . . ., µp+1
eigenvalues of c2, . . ., cp+1 of maximal possible multiplicity; we assume these multiplicities to
be > n/2. Suppose that the eigenvalues of the classes cj satisfy the only non-genericity relation
µ1 + . . . + µp+1 = 0.
Denote by c′
j ⊂ gl(n−1, C) the conjugacy classes obtained from cj by deleting the eigenvalues
µj. Hence, condition (βn−1) holds for the classes c′
j and the sum of their eigenvalues is 0.
Moreover, the classes c′
j do not correspond to Case A) from Lemma 15 (we let the reader check
this oneself ).

Hence, there exist block upper-triangular matrices Aj =
 ( A′
j Dj
0 µj
 )
, A′
j ∈ c′
j, whose tuple

deﬁnes a semi-direct sum (but not a direct one); the matrices A′
j deﬁne an irreducible representa-
tion. Indeed, one checks directly that dim Ext1(A, M ) = 1 (this results from r2 + . . . + rp+1 = n).
The same equality shows that the variety V consisting of tuples of matrices Aj ∈ cj which are

6

block upper-triangular up to conjugacy (i.e. like Aj above) is of dimension dimW where W is
the variety of tuples with trivial centralizers from the classes cj.
This means that there exist no irreducible tuples from the classes cj. Indeed, should they exist,
their variety (which is part of W) should contain in its closure the variaty V (see Theorem 6
from [Ko3]), hence, one would have dimV <dimW which is a contradiction.
The example shows that Theorem 21 is not true without the condition the eigenvalues to be
2-generic and that Theorem 22 is not true if there is an equality in (βn).
A similar example can be given for matrices Mj.

Example 30 There exist triples of diagonalizable 2 × 2-matrices M 1
j (resp. M 2
j ) with (generic)
eigenvalues equal to (a, b), (µ, ν), (η, ξ) (resp. to (c, d), (µ, ν), (η, ζ)); same (diﬀerent) letters
denote same (diﬀerent) eigenvalues.

Then there exists a block upper-triangular triple of matrices Mj =
 ( M 1
j Bj
0 M 2
j
 )
 deﬁning a

semi-direct sum of the representations P 1 and P 2 deﬁned by the matrices M 1
j and M 2
j (because
dim Ext1(P 1, P 2) = 1).
One checks directly that
a) the centralizer of the matrices Mj is trivial;
b) their eigenvalues can be chosen 2-generic (we assume that they satisfy only the following
non-genericity relations: abµνηξ = 1 and cdµνηζ = 1);
c) one has κ = 2 for the triple of conjugacy classes of the matrices Mj.
As κ = 2, one cannot have coexistence of irreducible and reducible triples, see [Ka]. This
means that the DSP is not solvable for the triple of conjugacy classes of the matrices Mj (but
the weak DSP is, see a)). Hence, Theorem 21 is not true for κ = 2.
A similar example can be given for matrices Aj.

2 Proof of Theorem 21

2.1 The method of proof

10. Suppose that for the conjugacy classes cj or Cj (with 2-generic eigenvalues) there hold
conditions (αn) and (βn). The variety of matrices Aj ∈ cj (satisfying (1)) or of matrices Mj ∈ Cj
(satisfying (2)) is of dimension d′ := d1 + . . . + dp+1 − n2 + 1 at each tuple with trivial centralizer,
see [Ko6], Proposition 2.
Given a reducible tuple of matrices from these conjugacy classes (block upper-triangular up
to conjugacy, with trivial centralizer, with given sizes of the diagonal blocks and with given
conjugacy classes of the restrictions of the matrices to the diagonal blocks) we compute the
dimension d′′ of the variety of such tuples and we show that d′′ < d′. If this is the case of all
such reducible tuples, then the variety of tuples with trivial centralizers must contain irreducible
tuples as well. Hence, the DSP is solvable for the given conjugacy classes.

Lemma 31 Under Convention 6, suppose that the tuple of diagonalizable matrices Aj or Mj
is as in Notation 26, and that the representations P and R are with trivial centralizers. If
δ :=dim Ext1(P 1, P 2) > 1, then d′′ < d′.

All lemmas from the proof of the theorem are proved in Subsection 2.4.

Corollary 32 If the representations P and R from the lemma are irreducible, then there exist
irreducible tuples from the conjugacy classes c(Pj ) × c(Rj).

7

The corollary is immediate.
We prove the theorem for diagonalizable matrices in 20 – 50 and then we treat the general
case in 60 – 110.

2.2 The proof for diagonalizable matrices

20. Prove the theorem for diagonalizable matrices.

Lemma 33 Suppose that the tuples of diagonalizable matrices Pj ∈ gl(l, C) and Rj ∈ gl(n−l, C)
(resp. Pj ∈ GL(l, C) and Rj ∈ GL(n − l, C)) are with trivial centralizers, P1 and R1 being each
with distinct eigenvalues and with no eigenvalue in common, and that l ≥ n − l ≥ 2. Then
δ ≥ 2 with the exception of the cases listed below1. In all of them one has p = 2. (We give the
list of the eigenvalues of the matrices P2, R2 and P3, R3, equal (diﬀerent) letters denote equal
(diﬀerent) eigenvalues if they correspond to one and the same index j. In Cases C) – F) one
can exchange the roles of P2, R2 and P3, R3.)

Case B) l = n − l = 2 (a, b) (c, d)
(a, b) (c, d)

Case C) l = n − l = 2 (a, b) (c, d)
(a, g) (c, d)

Case D) l = n − l = 3 (a, b, c) (f, g, g)
(a, b, c) (f, g, g)

Case E) l = 2q + 1, n − l = 2 (a, . . . , a
︸ ︷︷ ︸
q times , b, . . . , b
︸ ︷︷ ︸
q times , c) (f, . . . , f
︸ ︷︷ ︸
q+1 times, g, . . . , g
︸ ︷︷ ︸
q times )

(a, b) (f, g)

Case F) l = 2q, n − l = 2 (a, . . . , a
︸ ︷︷ ︸
q times , b, . . . , b
︸ ︷︷ ︸
q−1 times, c) (f, . . . , f
︸ ︷︷ ︸
q times , g, . . . , g
︸ ︷︷ ︸
q times )

(a, b) (f, g)

In Case B) condition (αn) does not hold for the conjugacy classes C(Pj) × C(Rj), in the
other cases it holds and is an equality. One has δ = 0 in Case B) and δ = 1 in Cases C) – F).

Corollary 34 In the conditions of the lemma and if the representations P and R are irreducible
the DSP is solvable for the tuple of conjugacy classes C(Sj) = C(Pj) × C(Rj) (except for Cases
B) – F)).

Proof:
The condition δ > 0 implies that there exists a semi-direct sum of the representations P
and R (we use Notation 26 here) which is not reduced to a direct one. The centralizer of this
semi-direct sum is trivial. Indeed, one can assume that P1 and R1 are diagonal, so a matrix X
from the centralizer must be also diagonal. The P -block of X commutes with all matrices Pj,
hence, it is scalar (because the centralizer of P is trivial). In the same way the R-block of X
must be scalar. Finally, these blocks must be equal, otherwise the commutation relations imply
that all blocks Qj must be 0 which contradicts the sum of P and R not to be a direct one.

1When listing the cases we begin with B, not with A, in order to avoid mixing up with Case A) from Lemma 15

8

Hence, the variety V of tuples of matrices deﬁning semi-direct sums of P and R is non-
empty and its dimension is smaller than the dimension of the variety W ⊃ V of tuples with
trivial centralizers of matrices from the classes C(Sj) (see Lemma 31). Hence, V is locally a
proper subvariety of W and a tuple from V can be deformed into a tuple from W\V (see The-
orem 6 from [Ko3]). The latter must be irreducible. Indeed, V contains locally all reducible
tuples because P and R are irreducible. ✷

30. Deduce the theorem from the corollary. The weak DSP is solvable for conjugacy classes
in the conditions of the theorem. Indeed, 2-genericity implies that a tuple from the given
conjugacy classes is (up to conjugacy) block upper-triangular with diagonal blocks all of sizes
≥ 2 and deﬁning irreducible representations. (We assume that there is more than one diagonal
block, otherwise the tuple is irreducible and there is nothing to prove.)
The restriction of the tuple to the union of diagonal blocks is a tuple from the same conjugacy
classes (because the conjugacy classes are diagonalizable). Consider a couple of consecutive
diagonal blocks. (We denote the restrictions of the matrices Aj or Mj to these two blocks by
Ai
j, M i
j , i = 1, 2.) They are both of size ≥ 2, and if one is not in one of the Cases B) – F),
then one can apply the above corollary and obtain the existence of irreducible tuples of matrices
from the conjugacy classes C(A1
j ) × C(A2
j ) (resp. C(M 1
j ) × C(M 2
j )). Thus we obtain a block-
diagonal tuple of n × n-matrices with one diagonal block less. Continuing like this we end with
an irreducible tuple of matrices which solves the DSP for the conjugacy classes cj or Cj.
40. There might be a problem, however, with Cases B) – F). First of all notice that this does
not happen if p ≥ 3. Indeed, in this case one can always choose two diagonal blocks deﬁning
irreducible representations and in which at least four conjugacy classes C(A1
j ) × C(A2
j ) (resp.
C(M 1
j ) × C(M 2
j )) are not scalar (including j = 1). So one can permute the diagonal blocks (to
get two consecutive blocks not from Cases B) – F)) and the proof is carried out as in 30.
50. So suppose that p = 2. We start again with the restriction of the tuple to the set
of diagonal blocks deﬁning irreducible representations. It is not possible to have all couples
of diagonal blocks to correspond to Case B) from the lemma because this will mean that the
classes cj or Cj are from Case A) of Lemma 15. So choose a couple of consecutive diagonal
blocks which are not from Case B) and replace them by a single block B deﬁning a semi-direct
sum of the representations which they deﬁne while keeping the other diagonal blocks the same.
This is possible because for the chosen blocks one has δ ≥ 1, see the lemma.
At each next step one has a block-diagonal tuple with diagonal blocks deﬁning irreducible
representations except B which deﬁnes one with trivial centralizer. At each step choose a block
W diﬀerent from B and next to B (hence, their couple is not from Case B) because B is of size
> 2), so one can replace it by a new block (which is the new block B) deﬁning a semi-direct
sum of the representations they deﬁne. So at each step the blocks B, W are not from Case B).
At the last step we obtain a representation with trivial centralizer. The last couple of blocks
B, W is not from Cases B) – F). Indeed, should it be from these cases, then for the conjugacy
classes cj or Cj one should have κ ≥ 2 (to be checked directly).
Hence, for the last couple of blocks B, W one has δ ≥ 2. This means that d′′ < d′, see 10.
This proves the theorem in the case of diagonalizable matrices.

2.3 The proof in the general case

60.

Convention 35 From here till the end of this subsection when Case A) of Lemma 15 or Cases

9

B) – F) of Lemma 33 are cited the JNFs of the matrices Aj or Mj (j ≥ 2) will be assumed
either to be the ones given in these two lemmas or to correspond to them, see Remarks 16 and
19.
 Such a change of the deﬁnition of these cases does not change the quantity δ, see part 2) of
Remarks 14. Hence, Lemma 33 is applicable after the change as well.
70. Consider a tuple in block upper-triangular form whose diagonal blocks deﬁne irreducible
representations. Consider the restriction of the tuple to the set of diagonal blocks. The conjugacy
class c′
j (resp. C ′
j) of the restriction of the matrix Aj (resp. Mj) from the tuple to the set of
diagonal blocks belongs to the closure of cj (resp. of Cj) but is not necessarily equal to it (one
might obtain a “less generic” Jordan structure when cutting oﬀ the blocks above the diagonal;
the eigenvalues and their multiplicities do not change). If for the conjugacy classes c′
j or C ′
j the
index of rigidity is ≤ 0, then as in the case of diagonalizable conjugacy classes one shows that
the DSP is solvable for the classes c′
j or C ′
j. This implies its solvability for the classes cj (resp.
Cj) (which can be proved by analogy with part 2 of Lemma 53 from [Ko2]).
80. Suppose (in 80 – 110) that the index of rigidity of the tuple of conjugacy classes c′
j or
C ′
j is > 0. Then for some j0 > 1 there exists a conjugacy class c′′
j0 (or C ′′
j0; we write further only
c′′
j0 for short) such that
1) c′
j0 belongs to the closure of c′′
j0;
2) c′′
j0 is obtained from c′
j0 when a couple of Jordan blocks with one and the same eigenvalue,
of sizes l, s, l ≥ s, are replaced by Jordan blocks (with the same eigenvalues) of sizes l + 1, s − 1,
see Section 8 in [Ko2]; the rest of the Jordan structure remains the same;
3) c′′
j0 belongs to the closure of cj0 (eventually, c′′
j0 = cj0).
When passing from c′
j0 to c′′
j0 the index of rigidity decreases by at least 2. If the change 2)
can take place by changing the JNF of the restriction of Aj0 or Mj0 to some diagonal block, then
we perform this change and further the proof is done as in the case of diagonalizable matrices.
90. If for the change 2) one has to change a block above the diagonal, and if there are at
least 3 diagonal blocks, then one proceeds as in 50 and one proves that d′′ < d′ exactly in the
same way.
Indeed, at the ﬁrst step one replaces two diagonal blocks (deﬁning irreducible representations)
by a single one (deﬁning their semi-direct sum). Namely, using Notation 26, one chooses the
block Qj0 such that the change 2) to take place. Then one chooses the block Q1 such that
condition (1) or (2) to hold (recall that A1 and M1 are with distinct eigenvalues, therefore
changing the block Q1 while keeping P1 and R1 the same does not change the conjugacy class
of A1 or M1).
The next steps are as in 50.
100. If there are just two diagonal blocks, not from Case B), then one ﬁrst constructs a block
upper-triangular tuple (with trivial centralizer) deﬁning a semi-direct sum of the representations
deﬁned by the diagonal blocks but without changing the class c′
j0.
Then conjugate the tuple with a block upper-triangular matrix so that the matrix Aj0 or
Mj0 to be in JNF (hence, it will be block diagonal as well). After this perform a change
Aj0 ↦→ Aj0 + εU or Mj0 ↦→ Mj0 + εU , ε ∈ (C, 0) where only the left lower block of U is non-zero
and is not of the form Rj0X − XPj0; U is chosen such that for ε ̸= 0 one has Aj0 ∈ c′′
j0 (resp.
Mj0 ∈ C ′′
j0).
To preserve condition (1) or (2) one looks then for deformations of the matrices Aj or Mj,
j ̸= j0, analytic in ε. Such a deformation exists, see the description of the “basic technical
tool” in [Ko2] (one conjugates the matrices Aj or Mj, j ̸= 0, with matrices which are analytic
deformations of I).
 10

Lemma 36 For ε ̸= 0 small enough the constructed tuple is irreducible.

The lemma implies the theorem in this case.
110. If the two diagonal blocks are from Case B), then one change 2) is not suﬃcient to make
the index of rigidity ≤ 0. Hence, at least two changes are necessary. With the ﬁrst of them we
construct the semi-direct sum of representations deﬁned by the two diagonal blocks; this time
we change one of the JNFs for j = j∗ > 1. When performing this change we change the block
Qj∗ and then we change Q1 to restore condition (1) or (2).
Suppose that the second change must take place for j = j0 ̸= j∗. Then after the second
change 2) (performed as in 100, using an analytic deformation) one has an irreducible represen-
tation by full analogy with Lemma 36.
If j∗ = j0 (and, say, j0 = 2), then there are two possibilities. Either this JNF has a single
eigenvalue, or it is with two double eigenvalues and three Jordan blocks. In the ﬁrst case one can
assume that the couple A2, U (resp. M2, U ) looks like this (after the analog of the conjugation
from 100):
 A2 =
 





 a 1 0 0
0 a 0 1
0 0 a 1
0 0 0 a
 




 , U =
 





 0 0 0 0
0 0 0 0
1 0 0 0
0 0 0 0
 




 .

We underline the unit which is introduced after the ﬁrst change 2). Its introduction results in
changing the JNF like this: {2, 2} ↦→ {3, 1}. In the second case the couple looks like this:

A2 =
 





 a 0 1 0
0 b 0 0
0 0 a 0
0 0 0 b
 




 , U =
 





 0 0 0 0
0 0 0 0
0 0 0 0
0 1 0 0
 




 .

For the rest the proof is carried out as in 80 – 100. The theorem is proved. ✷

2.4 Proofs of the lemmas

Proof of Lemma 31:

To obtain d′′ one must add l(n − l) to d′′′, the dimension of the variety of block upper-
triangular tuples as in the lemma (truly block upper-triangular, not only up to conjugacy).
Indeed, l(n − l) is the size of the left lower block and adding this corresponds to taking into

account the possibility to conjugate such a tuple by matrices of the form
 ( I 0
X I
 )
.

One has d′′′ = ∆1 + ∆2 + ∆3 where ∆1 = ∑p+1
j=1 d1
j − l2 + 1, ∆2 = ∑p+1
j=1 d2
j − (n − l)2 + 1 and
∆3 = ∑p+1
j=1 sj − l(n − l) (the contributions to d′′′ from the P -, R- and Q-block).
On the other hand, dj = d1
j + d2
j + 2sj (this can be deduced from Remark 12). Hence, d′′′ =
∑p+1
j=1 dj −∑p+1
j=1 sj −n2 +l(n−l)+2 = ∑p+1
j=1 dj −δ −n2 −l(n−l)+2 and d′′ = ∑p+1
j=1 dj −δ −n2 +2.
One has d′ = ∑p+1
j=1 dj − n2 + 1 = d′′ + δ − 1. Hence, for δ > 1 one has d′ > d′′. ✷

Proof of Lemma 33:

We transform the proof of the lemma into ﬁnding the cases when δ ≤ 1.

11

Statement 37 One has sj ≥ r1
j (n − l) (A) and sj ≥ r2
j l (B) (see Notation 26).

Proof:

Use Remark 27 (and the notation from it) and Lemma 28. Denote by µ′ (resp. µ′′) the
biggest among the numbers m′
j (resp. m′′
j ). Then sj ≥ l(n − l) − µ′(n − l) = r1
j (n − l) because
∑s
i=1 m′
im′′
i ≤ µ′ ∑s
i=1 m′′
i = µ′(n − l). In the same way sj ≥ l(n − l) − µ′′l = r2
j l. ✷

Remark 38 Inequality (A) becomes an equality exactly if m′′
i = 0 whenever m′
i < µ′. Inequality
(B) becomes an equality exactly if m′
i = 0 whenever m′′
i < µ′′.

Statement 39 If for some index j > 1 (say, j = 2) one has r1
j = 0, r2
j > 0, then one has δ ≥ 2.
The same is true if r1
j = r2
j = 0 and cj is not scalar. The same is true if r1
j > 0, r2
j = 0.

Proof:

Consider the ﬁrst and the second of the three claims. By (A) one has s3 + . . . + sp+1 ≥
(r1
3 + . . . + r1
p+1)(n − l) ≥ l(n − l); recall that s1 = l(n − l). In the ﬁrst claim one has also
s2 ≥ r2
j l ≥ 2, hence, δ ≥ 2. In the second claim the conjugacy class c2 deﬁnes the MV (l, n − l)
and one has s2 = l(n − l) ≥ 2 and again δ ≥ 2. The third claim is proved in the same way as
the ﬁrst one using (B). ✷

Convention 40 From now till the end of the proof of the lemma we assume (using the above
statement) that for all indices j > 1 one has r1
j > 0, r2
j > 0.

Statement 41 If p ≥ 3, then δ ≥ 2.

Proof:

It suﬃces to consider the following two cases (up to permutation of the indices j > 1):
1) r1
2 ≥ l/2, r1
3 ≥ l/2, r1
4 > 0;
2) r1
2 > 0, l/2 > r1
j > 0 for j > 2.
In case 1) one has s2 + s3 ≥ l(n − l) (see (A)), s4 ≥ n − l ≥ 2, s1 = l(n − l), so δ ≥ 2, see
Lemma 28.
In case 2) recall ﬁrst that r2
j > 0 for j > 2. For j = 3, 4, . . . , p + 1 one has sj > r1
j (n − l), i.e.
sj ≥ r1
j (n − l) + 1, see Statement 37 and Remark 38. One has s1 = l(n − l), s2 ≥ r1
2(n − l) (see
(A)), hence, s1 + . . . + sp+1 ≥ 2l(n − l) + 2 and again δ ≥ 2. ✷

Convention 42 From now till the end of the proof of the lemma we assume that p = 2, see
Statement 41.

Statement 43 If r1
2 + r1
3 ≥ l + 1 or r2
2 + r2
3 ≥ n − l + 1, then δ ≥ 2.

Indeed, if r1
2 + r1
3 ≥ l + 1, then (see (A)) s2 + s3 ≥ (l + 1)(n − l) ≥ l(n − l) + 2 and δ ≥ 2. In
the same way if r2
2 + r2
3 ≥ n − l + 1, then s2 + s3 ≥ l(n − l + 1) ≥ l(n − l) + 2 and δ ≥ 2. ✷

Statement 44 If l is even and r1
2 = r1
3 = l/2, then δ ≥ 2, except in Cases B), C) and F) from
the lemma.
 12

Proof:

10. If l = 2, then n − l = 2 and one has δ ≤ 1 only in one of Cases B) or C) from the lemma.

20. If l ≥ 4, then δ ≥ 2. Indeed, to avoid Case A) from Lemma 15 for the block P , one must
suppose that at least one of the two matrices P2 and P3 (say, P2) has at least three distinct
eigenvalues. Assume that the MV of P2 looks like this: (m′
1, . . . , m′
s), with m′
1 = µ′ > m′
2 ≥
. . . ≥ m′
s (the inequality m′
1 > m′
2 results from r1
2 = l/2).
If for at least two indices i > 1 one has m′′
i ̸= 0, then for them one has m′
im′′
i < µ′m′′
i and
∑s
i=1 m′
im′′
i ≤ µ′ ∑s
i=1 m′′
i − 2 = µ′(n − l) − 2. Hence, s2 ≥ r1
2(n − l) + 2 (see Remark 27),
s3 ≥ r1
3(n − l) (see (A)) and δ ≥ 2.

30. If for only one index i > 1 one has m′′
i ̸= 0 (i.e. R2 has only two diﬀerent eigenvalues),
then similarly s2 ≥ r1
2(n − l) + 1 with equality only if the MV of P2 equals (l/2, l/2 − 1, 1) and
the two eigenvalues, of the two greatest multiplicities, are eigenvalues of R2 as well; moreover,
its only eigenvalues.

40. If P3 has at least three diﬀerent eigenvalues, then in the same way s3 ≥ r1
3(n − l) + 1 and,
hence, δ ≥ 2. So the only possibility to have δ ≤ 1 is the MV of P3 to be (l/2, l/2). If n − l = 2,
then δ ≤ 1 only in Case F). If n − l > 2, then R3 must have at least three distinct eigenvalues
(otherwise condition (αn−l) fails for the block R) and s3 ≥ lr2
3 + 1. One has also s2 ≥ lr2
2 + 1
(to be checked directly), hence, again δ ≥ 2. ✷

Statement 45 Suppose that r1
2 + r1
3 = l. If r1
2 > l/2, r1
3 < l/2 or r1
2 < l/2, r1
3 > l/2, then δ ≥ 2
except in Cases D), E) from the lemma.

Proof:

10. Without loss of generality we assume that r1
2 > l/2, r1
3 < l/2. If l = 3 and n − l = 2 or
n − l = 3, then one has δ ≤ 1 only in Case E) with q = 1 or in Case D) of the lemma. Indeed,
sj is minimal only if all eigenvalues of Rj are eigenvalues of Pj as well for j = 2, 3.

20. If l ≥ 5 and n − l ≥ 4, then δ ≥ 2. Indeed, if the MVs of P3 and R3 equal respectively
(m′
1, . . . , m′
s), (m′′
1, . . . , m′′
s ), with m′
1 = µ′ > m′
2 ≥ . . . ≥ m′
s, then one has m′
im′′
i ≤ (µ′ − 1)m′′
i
for i > 1 and m′′
i > 0; hence,

s∑

i=1 m′
im′′
i ≤ µ′m′′
1 + (µ′ − 1)
 s∑

i=2 m′′
i = µ′ s∑

i=1 m′′
i −
 s∑

i=2 m′′
i = µ′(n − l) −
 s∑

i=2 m′′
i .

If ∑s
i=2 m′′
i ≥ 2, then s3 ≥ r1
3(n − l) + 2 (see Remark 27), s2 ≥ r1
2(n − l) (see (A)) and δ ≥ 2.
So δ can be ≤ 1 only in case that ∑s
i=2 m′′
i = 1, i.e. the MV of R3 is of the form (n − l − 1, 1).
If this is so, then the MV of R2 is (1, . . . , 1) (otherwise (αn−l) fails for the block R), i.e. R2 has
distinct eigenvalues. Hence, s2 ≥ l(n − l − 1) whatever the eigenvalues of P2 are.
But then s3 is minimal if and only if the MV of P3 equals (l−1, 1) and P3 has the same eigen-
values as R3 (the proof of this is left for the reader). In this case s3 = (l − 1) + (n − l − 1) = n − 2,
hence, s2 + s3 ≥ l(n − l) + n − l − 2 and for n − l ≥ 4 one has δ ≥ 2.

30. If l ≥ 5 and n − l = 2, and if P2 has at least 4 distinct eigenvalues, then s2 ≥ l + 2.
Indeed, s2 is minimal only if each eigenvalue of R2 is eigenvalue of P2 as well.

13

In such a case one has s2 = 2l − m′
i1 − m′
i2 where m′
i1, m′
i2 are the multiplicities of the
eigenvalues of R2 as eigenvalues of P2. As m′
i1 + m′
i2 ≤ l − 2 (there are at least two more
eigenvalues of P2, each of multiplicity ≥ 1), one gets s2 ≥ l + 2. In a similar way, s3 ≥ l, with
equality when P3 has two eigenvalues which are eigenvalues of R3 as well, hence, δ ≥ 2.
If P2 has exactly three distinct eigenvalues, then one has s2 ≥ l+1 with equality exactly if the
eigenvalue which is not eigenvalue of P2 is simple. Hence, δ ≤ 1 only in Case E) from the lemma.

40. If l ≥ 5 and n − l = 3, then at least one of the matrices R2, R3 must have 3 distinct
eigenvalues (otherwise (β3) fails for the block R). The respective quantity sj must be ≥ 2l = r2
j l,
see (B). If the other matrix Rj (j = 2 or 3) has also 3 distinct eigenvalues, then s2 + s3 ≥ 4l >
3l + 2 and δ ≥ 2.
If the MV of the other matrix Rj (say, R3) equals (2, 1), then s3 is minimal exactly if P3
has the same eigenvalues as R3, of multiplicities l − 1 and 1. In this case s3 = l + 1. But then
P2 must be with distinct eigenvalues (otherwise (αl) fails for the block P ), s2 ≥ 3l−3, and δ > 2.

50. If l = 4, then one can have r1
2 > 2, r1
3 < 2 only if P3 has four distinct eigenvalues and
the MV of P3 is (1, 3). We let the reader check oneself that in all possible cases (n − l = 2, 3 or
4) one has δ ≥ 2. ✷

The lemma follows from Statements 39, 41, 43, 44 and 45. ✷

Proof of Lemma 36:

Denote by T , the matrix algebra of all block upper-triangular matrices with square diagonal
blocks of sizes l and n − l. A priori the representation deﬁned by the deformed matrices is
either irreducible (and the corresponding matrix algebra is gl(n, C)) or is reducible and deﬁnes
a matrix algebra which up to analytic conjugation equals T (the statement results from a more
general one which can be found in [Ko7]). The second case, however, is impossible because such
a conjugation of Aj0 or Mj0 (with a matrix I + O(ε)) cannot make the left lower block of U
disappear (because it is not of the form Rj0X − XPj0). ✷

3 Proof of Theorem 22

3.1 Proof in the case of matrices Aj

Deﬁnition 46 A conjugacy class is called regular if to every eigenvalue there corresponds a
single Jordan block of size equal to the multiplicity of the eigenvalue.

Remark 47 The JNFs of all regular conjugacy classes correspond to each other (see Deﬁni-
tion 13) and, in particular, to the diagonal JNF with distinct eigenvalues and to the JNF with
a single eigenvalue and a single Jordan block of size n.

Proposition 48 The DSP is positively solvable for classes cj where c1 is regular and one has
r2 + . . . + rp+1 ≥ n + 1.

The proposition implies the theorem in the case of matrices Aj. To prove the proposition
we need the following lemma.
 14

Lemma 49 The DSP is positively solved for tuples of nilpotent conjugacy classes cj with r1 +
. . . + rp+1 ≥ 2n in which r1 = n − 1, i.e. the conjugacy class c1 has a single Jordan block of size
n.
 The lemma is a particular case of the results in [Ko8]. It follows also from the ones in [C-B].

Proof of the proposition:

Given an irreducible tuple of nilpotent matrices Aj satisfying the conditions of the lemma
one can deform it analytically into an irreducible tuple of matrices A′
j where for each j either
J(A′
j) = J(Aj) or J(A′
j) corresponds to J(Aj). The eigenvalues of the matrices A′
j must be close
to 0. These statements can be deduced from [Ko2], see the deﬁnition of the basic technical tool
there which is a way to deform analytically tuples of matrices with trivial centralizers; compare
also with Lemma 53 from [Ko2].
Thus one obtains the positive solvability of the DSP for all tuples of JNFs J(cj ) satisfying
the condition r2 + . . . + rp+1 ≥ n + 1; see Deﬁnition 13 and Remarks 14 (especially part 2) of
them). However, solvability is proved only for eigenvalues close to 0.
By multiplying the tuples of matrices A′
j by non-zero complex numbers (i.e. (A′
1, . . . , A′
p+1) ↦→
(gA′
1, . . . , gA′
p+1), g ∈ C∗) one can obtain irreducible tuples with the same JNFs as A′
j and with
any eigenvalues whose sum (taking into account the multiplicities) is 0. This proves the propo-
sition. ✷

3.2 Proof for matrices Mj

Suppose that for some conjugacy classes Cj satisfying the conditions of the theorem there exist no
irreducible tuples. Then there exist tuples with trivial centralizers. This follows from Theorem 18
and from Lemma 15.
Each such tuple can be conjugated to a block upper-triangular form in which the diagonal
blocks deﬁne irreducible or one-dimensional representations. Denote by s1, . . ., sν the sizes of
the diagonal blocks. We say that these sizes (considered up to permutation) deﬁne the type of
the tuple. The tuple is called maximal if there is no tuple with trivial centralizer and of type
s′
1, . . ., s′
h such that h < ν and the sizes s′
i are obtained from the sizes sj by one or several
operations of the form (sj1, sj2) ↦→ sj1 + sj2. We say that the type s′
1, . . ., s′
h is greater than the
type s1, . . ., sν.

Lemma 50 Given a maximal tuple of matrices Mj one can construct a tuple of matrices Aj ∈ cj
of the same type, with trivial centralizer, with Mj = exp(2πiAj ) (up to conjugacy) where for
j > 1 the matrix Aj has no couple of eigenvalues whose diﬀerence is a non-zero integer.

The lemma is proved in the next subsection.

Remark 51 The condition “Mj = exp(2πiAj ) (up to conjugacy)” is introduced with the aim
to use the fact that the monodromy operators of the Fuchsian system dX/dt = (
∑p+1
j=1 Aj/(t −
aj))X (∗∗) in the absence of non-zero integer diﬀerences between the eigenvalues of the matrices
Aj equal (up to conjugacy) exp(2πiAj ). See the deﬁnition of the monodromy operators in the
Introduction of [Ko2].

For the tuple of matrices Aj from the lemma one has that they can be analytically deformed
into an irreducible tuple of such matrices. Indeed, for their conjugacy classes the DSP is posi-
tively solved (this is already proved in Subsection 3.1) and all reducible tuples from these classes
belong to the closure of the variety of irreducible tuples, see Theorem 6 from [Ko3].

15

All irreducible tuples of matrices A0
j close to tuples Aj from the lemma deﬁne Fuchsian sys-
tems dX/dt = (
∑p+1
j=1 A0
j /(t − aj))X (∗ ∗ ∗) whose monodromy groups must be (up to conjugacy)
from the type of the tuple of matrices Mj from the lemma. This follows from the tuple of
matrices Mj being maximal.
Consider the monodromy operators (denoted also by Mj) of systems (∗∗) with matrices-
residua Aj. One has Mj = exp(2πiAj ) (up to conjugacy) and there is a bijection between the
eigenvalues of the matrices Aj and the ones of the matrices Mj. For each diagonal block the
sum of the eigenvalues of the matrices Aj from the lemma is 0. Hence, the sum of the same
eigenvalues of the matrices A0
j is also 0. If the monodromy group of system (∗ ∗ ∗) is of the type
of the one of system (∗∗), then by Theorem 5.1.2 from [Bo] it should be possible to conjugate the
tuple of matrices A0
j to a block upper-triangular form with blocks as in the type of the matrices
Mj. This contradicts the irreducibility of the tuple of matrices A0
j .

Remark 52 When applying Theorem 5.1.2 from [Bo] we use the fact that there are no non-
zero integer diﬀerences between the eigenvalues of the matrices Aj. Thus to each eigenvalue σ
of Mj of a given multiplicity there corresponds only one eigenvalue λ of Aj (which is of the
same multiplicity) where σ = exp(2πiλ). Theorem 5.1.2 from [Bo] speaks about the exponents
(i.e. the eigenvalues of the matrices Aj) corresponding to an invariant subspace. In the absence
of non-zero integer diﬀerences these exponents are deﬁned by the eigenvalues of the monodromy
operators in a unique way.

The theorem is proved. ✷

3.3 Proof of Lemma 50

10. One can construct for each size si of the type a tuple of matrices A∗
i,j such that one has
(up to conjugacy) exp(2πiA∗
i,j) = M ∗
i,j (∗) where M ∗
i,j are the restrictions of the matrices Mj
to the diagonal block of size si, and the matrices A∗
i,j deﬁne an irreducible or one-dimensional
representation. In the one-dimensional case the claim is evident. In the irreducible case one can
construct a Fuchsian system with matrices-residua equal up to conjugacy to A∗
i,j (where A∗
i,j
satisfy (∗)) the real parts of whose eigenvalues can be chosen to belong to [0, 1) for j > 1 (to
avoid non-zero integer diﬀerences between eigenvalues); the construction is explained in [ArIl].

20. Consider the tuple of matrices A′
j which are block-diagonal their restrictions to each
diagonal block of size si being equal to the blocks A∗
i,j from 10. We complete them (in 30) by
adding entries in the blocks above the diagonal (the newly obtained matrices are denoted by
Aj) so that one would have exp(2πiAj ) = Mj up to conjugacy. We do this for j > 1 and then
we deﬁne A1 so that A1 + . . . + Ap+1 = 0. As A1 has distinct eigenvalues, whatever entries
we add in the blocks above the diagonal, they do not change the conjugacy class of A1. As
exp(2πiA′
1) = M1 up to conjugacy, one will also have exp(2πiA1) = M1 up to conjugacy.

30. One can conjugate the matrix Mj by a block upper-triangular matrix Bj so that the
diagonal blocks of (Bj)−1MjBj of sizes si to be in JNF and in the blocks above the diagonal
non-zero entries to be present only in positions (i, j) such that the i-th and j-the eigenvalues
coincide. For each eigenvalue σk,j of Mj denote by Mj(σk,j) the matrix whose restriction to the
rows and columns of the eigenvalue σk,j are the same as the ones of (Bj)−1MjBj and the rest
of its entries are 0.
 16

One can conjugate the matrices A′
j by block-diagonal matrices Dj so that the matrix
(Dj)−1A′
jDj to be in JNF and for each diagonal block there to hold exp(2πiA∗
i,j ) = M ∗
i,j (up to
conjugacy).
Set (Dj )−1A′
jDj = ∑
k,j λk,jA′
j(λk,j) where λk,j are the distinct eigenvalues of A′
j and
A′
j(λk,j) is the matrix whose restriction to the rows and columns of the eigenvalue λk,j is the
same as the one of (Dj)−1A′
jDj and the rest of its entries are 0. Deﬁne the matrices Aj(λk,j)
by analogy with the matrices A′
j(λk,j).
Recall that one has σk,j = exp(2πiλk,j). Hence, for each diagonal block and for each couple
(k, j) the restrictions of the matrices A′
j(λk,j) − λk,jI and Mj(σk,j) − σk,jI to it are equal.
Deﬁne the matrices (Dj)−1AjDj by the rule for all (k, j) the matrices Aj(λk,j) − λk,jI and
Mj(σk,j) − σk,jI to be equal. The rule implies that the JNFs of the matrices (Bj)−1MjBj and
(Dj)−1AjDj, hence, of Mj and Aj, coincide. As there are no non-zero integer diﬀerences be-
tween eigenvalues of Aj, one has also exp(2πiAj) = Mj (up to conjugacy).

40. The tuple of matrices Aj thus constructed might fail to be with trivial centralizer. Hence,
the tuple must deﬁne a direct sum of representations (this follows from A1 being with distinct
eigenvalues). So conjugate it to a block-diagonal form where each block (we call these blocks
big blocks) is small-block upper-triangular and with trivial centralizer. The small blocks are of
sizes si.
As in Lemma 24 from [Ko3] one shows that if there are two big blocks of sizes u, v where
u ≥ 3, v ≥ 2, then one can deform the tuple into one in which these two big blocks are replaced by
a single big block of size u + v (with trivial centralizer and with the same small blocks as the two
big blocks) while the other big blocks remain the same. The statement holds also if u = v = 2,
p = 2 (see again Lemma 24 from [Ko3]) and for at least one index j ≥ 2 the restrictions of the
tuple to the two big blocks belong to diﬀerent conjugacy classes, or if u = v = 2, p ≥ 3 and no
matrix is scalar.
If there is a big block B of size 1, then it follows from r2 + . . . + rp+1 ≥ n + 1 that for at
least one of the other big blocks B′ one has Ext1(B, B′) ≥ 1. Indeed, without loss of generality
one can assume that the restrictions of the matrices to the block B equal 0 for all values of j.
Hence, for each other big block B′ one has Ext1(B, B′) = ρ(B′) − 2σ(B′) where ρ(B′) is the
sum of the ranks rj(B′) of the matrices Aj|B′ and σ(B′) is the size of B′. (One subtracts σ(B′)
once because the sum of the matrices Aj is 0 and once to factor out conjugation with block
upper-triangular matrices; see the proof of Lemma 28.)
If for all blocks B′ one has Ext1(B, B′) ≤ 0, then one has

0 ≥ ∑

B′ (ρ(B′) − 2σ(B′)) = (

p+1∑

j=1
 ∑

B′ rj(B′)) − 2(n − 1) ≥ (

p+1∑

j=1 rj) − 2(n − 1)

i.e. ∑p+1
j=2 rj ≤ n − 1 (recall that r1 = n − 1) which is a contradiction.
Hence, one can replace the two blocks B, B′ by a single big block of size σ(B′) + 1.
There remains to be considered the case when there is no big block of size 1 or ≥ 3, i.e. all
big blocks are of size 2; moreover, p = 2, and for j > 1 the restrictions of the matrices Aj to the
big blocks belong to one and the same conjugacy class. In this case one has r2 + r3 = n, i.e. the
case has not to be considered. ✷
 17

References

[ArIl] V.I. Arnold, V.I. Ilyashenko, Ordinary diﬀerential equations (in Dynamical Systems
I, Encyclopaedia of Mathematical Sciences, t. 1, Springer 1988).

[Bo] A.A. Bolibrukh, Hilbert’s twenty-ﬁrst problem for linear Fuchsian systems, Proceed-
ings of the Steklov Inst. Math. No. 5, 206 (1995).

[C-B] W. Crawley-Boevey, On matrices in prescribed conjugacy classes with no common
invariant subspace and sum zero, preprint arXiv:math.LA/0103101, 15 March 2001,
to appear in Duke Math. J. 118 (2003).

[Ka] N.M. Katz, Rigid local systems, Annals of Mathematics, Studies Series, Study 139,
Princeton University Press, 1995.

[Ko1] V.P. Kostov, The Deligne-Simpson problem, C.R. Acad. Sci. Paris, t. 329, S´erie I, p.
657-662, 1999.

[Ko2] V.P. Kostov, On the Deligne-Simpson problem, Proceedings of the Steklov Institute,
vol. 238 (2002), Monodromy in problems of algebraic geometry and diﬀerential equa-
tions, p. 148 – 185 (Published also in the Russian version of the journal, but in
English: Trudy Mat. Inst. Steklova, vol. 238 (2002), p. 158 – 195). Electronic preprint
math.AG/0011013.

[Ko3] V.P. Kostov, The connectedness of some varieties and the Deligne-Simpson problem.
Electronic preprint math.AG/0206087.

[Ko4] V.P. Kostov, Some examples of rigid representations, Serdica Math. J. 26, p. 253-276
(2000).

[Ko5] V.P. Kostov, Monodromy groups of regular systems on Riemann’s sphere,
pr´epublication N 0 401 de l’Universit´e de Nice, 1994.

[Ko6] V.P. Kostov, Some examples related to the Deligne-Simpson problem (Appendix by
Ofer Gabber), Proceedings of Second International Conference on Geometry, Integra-
bility and Quantization, St. Constantine and Elena, Bulgaria, June 7-15, 2000, Edited
by Ivailo M. Mladenov and Gregory L. Naber, ISBN 954-90618-2-5, pp. 208 – 227.
Coral Press, Soﬁa (2001) Electronic preprint math.AG/0011015.

[Ko7] V.P. Kostov, A generalization of the Burnside theorem and of Schur’s lemma for
reducible representations, Journal of Dynamical and Control Systems, vol. 1, N 0 4,
October 1995, p. 551 – 580.

[Ko8] V.P. Kostov, On some aspects of the Deligne-Simpson problem, to appear in Journal
of Dynamical and Control Systems, vol. 9, No. 3 (July 2003). Electronic preprint
math.AG/0005016.

[Si1] C.T. Simpson, Products of matrices, Department of Mathematics, Princeton Uni-
versity, New Jersey 08544, published in “Diﬀerential Geometry, Global Analysis and
Topology”, Canadian Math. Soc. Conference Proceedings 12, AMS, Providence RI
(1991), 157 – 185. Proceedings of the Halifax Symposium, June 1990.

18

[Si2] C.T. Simpson, Solution of a stability game, Department of Mathematics, Princeton
University, New Jersey 08544, 1990.

Author’s address: Universit´e de Nice – Sophia Antipolis, Laboratoire de Math´ematiques,
Parc Valrose, 06108 Nice, Cedex 2, France; e-mail: kostov@math.unice.fr

19
