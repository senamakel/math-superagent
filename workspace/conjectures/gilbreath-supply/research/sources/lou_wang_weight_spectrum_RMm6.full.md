<!-- source: https://arxiv.org/pdf/2406.03803 | converted from PDF -->

arXiv:2406.03803v1  [cs.IT]  6 Jun 2024
Determining the Weight Spectrum of the
Reed–Muller Codes RM (m − 6, m)

Yueying Lou
∗ and Qichun Wang †‡

Abstract

The weight spectra of the Reed-Muller codes RM (r, m) were un-
known for r = 3, ..., m − 5. In IEEE Trans. Inform. Theory 2024,
Carlet determined the weight spectrum of RM (m − 5, m) for m ≥ 10
using the Maiorana-McFarland construction, where the result was tried
to be extended to RM (m − 6, m), but many problems occurred and
much work needed to be done. In this paper, we propose a novel way of
constructing Reed–Muller codewords and determine the weight spec-
trum of RM (m − 6, m) for m ≥ 12, which gives a positive answer to
an open question on the weight spectrum of RM (m − c, m) for c = 6.
Moreover, we put forward a conjecture and verify it for some cases.
If the conjecture is true, then that open question can be completely
solved.

Keywords: Reed–Muller codes, weight spectrum, Boolean functions.

1 Introduction

An m-variable Boolean function is a map from Fm
2 into the ﬁnite ﬁeld F2.
The r–th order Reed–Muller code of length 2m is denoted by RM (r, m). Its
codewords are the truth tables (output values) of the set of all m-variable
Boolean functions of degree ≤ r.
The low Hamming weights are well–known for all Reed–Muller codes,
and the only Hamming weights in RM (r, m) belonging to the range [2m−r, 2m−r+1]
are of the form 2m−r+1 −2m−r+1−i, where i ≤ max(min(m−r, r), m−r+2
2 ) [9].

∗School of Computer and Electronic Information/School of Artiﬁcial Intelligence, Nan-
jing Normal University, Nanjing, China. Email: 232212001@njnu.edu.cn.
†School of Computer and Electronic Information/School of Artiﬁcial Intelligence, Nan-
jing Normal University, Nanjing, China. Email: qcwang@fudan.edu.cn.
‡Corresponding author.
 1

This result was extended and all the weights lying between the minimum
distance 2m−r and 2m−r+1 + 2m−r−1 were determined by Kasami, Tokura
and Azumi in [8].
The weight spectra of the Reed-Muller codes RM (r, m) are also well–
known for r = 0, 1, 2, m − 2, m − 1, m (see e.g. [5, 11]). In 2023, Carlet
and Sol´e determined the weight spectra of RM (m − c, m) for c = 3, 4 [5].
Recently, Carlet determined the weight spectrum of RM (m − 5, m) for m ≥
10 using the Maiorana-McFarland construction, where he tried to extend
the result to RM (m − 6, m), but not succeeded [2].
In this paper, we propose a novel way of constructing Reed–Muller code-
words and determine the weight spectrum of RM (m − 6, m) for m ≥ 12,
which gives a positive answer to an open question on the weight spectrum of
RM (m − c, m) for c = 6. Moreover, we put forward a conjecture and verify
it for some cases. If the conjecture is true, then that open question can be
completely solved.
The paper is organized as follows. In Section 2, the necessary background
is established. We determine the weight spectrum of RM (m − 6, m) in
Section 3, and try to extend the result to RM (m − c, m) in Section 4. We
end in Section 5 with conclusion.

2 Preliminaries

Let Fm
2 be the m-dimensional vector space over the ﬁnite ﬁeld F2. We denote
by Bm the set of all m-variable Boolean functions, from Fm
2 into F2.
Any Boolean function f ∈ Bm can be uniquely represented as a multi-
variate polynomial in F2[x1, · · · , xm],

f (x1, . . . , xm) = ∑

K⊆{1,2,...,m} aK ∏

k∈K xk,

which is called its algebraic normal form (ANF). The algebraic degree of f ,
denoted by deg(f ), is the number of variables in the highest order term with
nonzero coeﬃcient.
The r-th order Reed-Muller code of length 2m is denoted by RM (r, m).
Its codewords are the truth tables (output values) of the set of all m-variable
Boolean functions of degree ≤ r.
We use |A| to denote the cardinality of the set A. Let f ∈ Bm and

1f = {x ∈ Fm
2 |f (x) = 1}, 0f = {x ∈ Fm
2 |f (x) = 0}.

2

The cardinality |1f | is called the Hamming weight of f , and will be denoted
by wt(f ). The Hamming distance between two functions f and g is the
Hamming weight of f + g, and will be denoted by d(f, g). It is well–known
that wt(f ) is odd if and only if deg(f ) = m.
Weights of the Reed-Muller code RM (r, m) are the Hamming weights
of all its codewords. That is, the Hamming weights of all f ∈ Bm with
deg(f ) ≤ r. The weight spectrum of RM (r, m) is the set of all distinct
weights.
It is well-known that the weights in RM (r, m) are multiples of 2
⌊ m−1
r ⌋

(McEliece divisiblity theorem [10]), and its minimum nonzero weight equals
2m−r. The low Hamming weights are well–known for all Reed–Muller codes
which can be seen from the following theorem.

Theorem 1 ([8]). Let w be a weight of RM (r, m) in the range 2m−r ≤ w <
2m−r+1. Let α = min(r, m − r) and β = m−r+2
2 . Then w is of the form
2m−r+1 + 2m−r+1−i, where 1 ≤ i ≤ max(α, β). Conversely, for any such i,
there is a weight w of that form in the range 2m−r ≤ w < 2m−r+1.

Kasami, Tokura and Azumi determined later in [9] all the weights lying
between the minimum distance 2m−r and 2m−r+1 + 2m−r−1.
We use || to denote the concatenation, that is,

(f1||f2)(x1, . . . , xm, xm+1) = (xm+1+1)f1(x1, . . . , xm)+xm+1f2(x1, . . . , xm),

and f1||f2||f3||f4 =

(xm+1+1)(xm+2+1)f1+xm+1(xm+2+1)f2+(xm+1+1)xm+2f3+xm+1xm+2f4,

where f1, f2, f3, f4 ∈ Bm. There are many results on Boolean functions
deduced through using concatenation techniques (see e.g. [2, 13, 14]).

3 Determining the weight spectrum of the Reed-
Muller codes RM(m − 6, m)

In this section, we will use the concatenation technique and construct func-
tions of B12 with the form g0||g1||g2||(g1 + g2 + g3) which can achieve all
the possible weights of of RM (6, 12), where g0, g3 ∈ RM (4, 10) and g1, g2 ∈
RM (5, 10).

Lemma 1. Let g = g0||g1||g2||(g1 + g2 + g3), where g0, g3 ∈ RM (4, 10) and
g1, g2 ∈ RM (5, 10). Then g ∈ RM (6, 12).

3

Proof. Clearly,

g = (x11 + 1)(x12 + 1)g0 + x11(x12 + 1)g1 + (x11 + 1)x12g2 + x11x12(g1 + g2 + g3)

= (x11 + 1)(x12 + 1)g0 + x11g1 + x12g2 + x11x12g3,

and the result follows.

By the results of [8, 9], The set of all weights < 2.5 ∗ 26 = 160 in
RM (6, 12) is known, which is shown as the following lemma.

Lemma 2 ([8, 9]). The set of all weights < 160 in RM (6, 12) equals

{0, 64, 96, 112, 120, 124, 126, 128, 136, 144, 148, 152, 154, 156, 158}.

Using the Maiorana-McFarland construction, Carlet found that all the
even weights from 154 to 190 can be reached except for 166. He then showed
that weight 166 can be achieved, but it is a little complex [2]. We now give
a simple way to construct a codeword with the weight 166.

Lemma 3. Let f = xi1xi2xi3xi4xi5 + xi6xi7xi8xi9xi10 ∈ B10. Let I =
{i1, i2, i3, i4, i5} and J = {i6, i7, i8, i9, i10}. If |I ⋂ J| = c, then wt(f ) =
64 − 2c+1.

Proof. Let f1 = xi1xi2xi3xi4xi5 and f2 = xi6xi7xi8xi9xi10. Clearly,

wt(f ) = |1f1 ∩ 0f2| + |1f2 ∩ 0f1|

= (2
5 − 2
10−|I∪J|) + (2
5 − 2
10−|J∪I|)

= (32 − 2
|I∩J|) + (32 − 2
|I∩J |)

= 64 − 2
c+1.

By Lemma 3, the set of all weights for functions of the form xi1xi2xi3xi4xi5+
xi6xi7xi8xi9xi10 ∈ B10 is {0, 32, 48, 56, 60, 62}. Since 62 + 56 + 48 = 166, it
is natural to construct a codeword with weight 166 using the concatenation
0||g1||g2||(g1 + g2) satisfying wt(g1) = 62, wt(g2) = 56 and wt(g1 + g2) = 48.

Lemma 4. Let g = 0||g1||g2||(g1+g2), where g1 = x1x2x3x4x5+x6x7x8x9x10
and g2 = x1x2x3x4x5 + x1x2x6x7x8 Then g ∈ RM (6, 12) and wt(g) = 166.

Proof. By Lemma 1, g ∈ RM (6, 12). By Lemma 3, wt(g1) = 62, wt(g2) = 56
and wt(g1 + g2) = 48. Therefore, wt(g) = 62 + 56 + 48 = 166, and the result
follows.
 4

Inspired by the above method to construct the codeword of weight 166,
we consider the following construction.

Construction 1. Let g1 = x1x2x3x4x5 + xi1xi2xi3xi4xi5 + xi6xi7xi8xi9xi10
and g2 = x1x2x3x4x5 + xi1xi2xi3xi4xi5 + xi11xi12xi13 xi14xi15, where g1, g2 ∈
B10 and 1 ≤ i1, . . . , i15 ≤ 10. We then construct g = 0||g1||g2||(g1 + g2).

Clearly, g1 and g2 in Construction 1 are with at most three monomials
and g1 + g2 is with at most two monomials. By Lemma 1, g ∈ RM (6, 12).
Let J = {i6, i7, i8, i9, i10} and K = {i11, i12, i13, i14, i15}. If |J ⋂ K| = c,
then by Lemma 3, wt(g1 + g2) = 64 − 2c+1. We now determine the weights
of functions with three monomials.

Lemma 5. Let f = x1x2x3x4x5 + xi1xi2xi3xi4xi5 + xi6xi7xi8xi9xi10 ∈ B10.
Let I = {1, 2, 3, 4, 5}, J = {i1, i2, i3, i4, i5} and K = {i6, i7, i8, i9, i10}. If
|I ∩ J| = c1, |I ∩ K| = c2, |J ∩ K| = c3 and |I ∩ J ∩ K| = c4, then

wt(f ) = 2
c1+c2+c3−c4−3 − 2
c1+1 − 2
c2+1 − 2
c3+1 + 96.

Proof. Let f1 = x1x2x3x4x5, f2 = xi1xi2xi3xi4xi5 and f3 = xi6xi7xi8xi9xi10.
Clearly, wt(f ) =

|1f1 ∩ 0f2 ∩ 0f3| + |1f2 ∩ 0f1 ∩ 0f3| + |1f3 ∩ 0f1 ∩ 0f2| + |1f1 ∩ 1f2 ∩ 1f3|.

By the inclusion-exclusion principle, |I ∪ J ∪ K| = 15 − c1 − c2 − c3 + c4.
Therefore,
 |1f1 ∩ 1f2 ∩ 1f3| = 2
c1+c2+c3−c4−5.

Moreover, we have

|1f1 ∩ 0f2 ∩ 0f3|

= (2
|J−K−I| − 1)(2
|K−J−I| − 1)2
10−|I∪J∪K| + 32 − 2
5−|J∩K−I|

= (2
5−c1−c3+c4 − 1)(2
5−c2−c3+c4 − 1)2
c1+c2+c3−c4−5 + 32 − 2
5−c3+c4

= 2
c1+c2+c3−c4−5 − 2
c1 − 2
c2 + 32.

Similarly,
 |1f2 ∩ 0f1 ∩ 0f3| = 2
c1+c2+c3−c4−5 − 2
c1 − 2
c3 + 32

|1f3 ∩ 0f1 ∩ 0f2| = 2
c1+c2+c3−c4−5 − 2
c2 − 2
c3 + 32,

and the result follows.
 5

By Lemma 5, the set of all weights for functions of the form x1x2x3x4x5+
xi1xi2xi3xi4xi5 + xi6xi7xi8xi9xi10 is {32, 48, 56, 60, 62, 64, 68, 72, 74, 76, 80}.
By choosing suitable functions with three monomials, Construction 1 can
generate functions whose weights range over all those integers between 154
and 210 that are congruent with 2 modulo 4.

Lemma 6. Take g1 = x1x2x3x4x5 + x1x2x3x4x6 + x1x2x3x4x7 and g2 =
x1x2x3x4x5+x1x2x3x4x6+h, where h = x5x6x8x9x10 or x5x7x8x9x10. Then
Construction 1 generates the functions with the weights 154 and 158.

Proof. By Lemma 5, wt(g1) = 25 − 25 − 25 − 25 + 96 = 32 and

wt(g2) = { 23 − 25 − 22 − 22 + 96 = 64, if h = x5x6x8x9x10,
22 − 25 − 22 − 21 + 96 = 62, if h = x5x7x8x9x10.

By Lemma 3,

wt(g1 + g2) = { 64 − 21 = 62, if h = x5x6x8x9x10,
64 − 22 = 60, if h = x5x7x8x9x10.

Clearly, 32+64+62=158 and 32+62+60=154, and the result follows.

Lemma 7. Take g1 = x1x2x3x4x5 + x1x2x3x6x7 + x4x5x8x9x10 and g2 =
x1x2x3x4x5 + x1x2x3x6x7 + h, where h is a monomial of degree 5. Then
Construction 1 can generate the functions with the weights

{162, 174, 178, 182, 186, 190, 194, 198, 202, 210}.

Proof. By Lemma 5, wt(g1) = 22 − 24 − 23 − 21 + 96 = 74. Similarly, the
values of wt(g2) and wt(g1 + g2) can be computed and their values are given
by the following table. Then we can calculate wt(g1) + wt(g2) + wt(g1 + g2),

h x1x2x3x4x5 x1x4x5x8x9 x1x2x3x4x8 x1x2x3x4x6 x1x2x3x8x9
wt(g2) 32 68 48 48 56
wt(g1 + g2) 56 32 56 60 56
h x1x2x6x7x8 x1x2x4x5x6 x1x2x4x6x7 x1x4x6x7x8 x1x4x5x6x7
wt(g2) 56 64 64 72 80
wt(g1 + g2) 60 56 60 56 56

and the result follows.
 6

Proposition 1. The set of the weights of 12–variable Boolean functions of
the form 0||g1||g2||(g1 + g2) contains all those integers between 154 and 214
that are congruent with 2 modulo 4, where g1, g2 ∈ B10 are homogeneous
polynomials of degree 5.

Proof. By Lemmas 4, 6 and 7, Construction 1 can generate the functions
with the weights

{154, 158, 162, 166, 174, 178, 182, 186, 190, 194, 198, 202, 210}.

Let g1 = x1x2x3x4x5+x1x2x3x6x7+x4x5x8x9x10. If we take g2 = x1x2x3x4x5+
x1x6x8x9x10 + x4x5x8x9x10, then g1 + g2 = x1x2x3x6x7 + x1x6x8x9x10. By
Lemmas 3 and 5, wt(g1) = 74, wt(g2) = 76 and wt(g1 + g2) = 56. Therefore,
0||g1||g2||(g1 + g2) is of weight 206. Take g2 = x1x2x3x4x5 + x1x6x7x8x9 +
x6x7x8x9x10, then wt(g2) = 62 and g1 + g2 = x1x2x3x6x7 + x1x6x7x8x9 +
x4x5x8x9x10 +x6x7x8x9x10. It is easy to be calculated that wt(g1 +g2) = 78.
Therefore, 0||g1||g2||(g1 + g2) is of weight 214, and the result follows.

Based on Construction 1, we can obtain all weights between 1050 and
1110 that are congruent with 2 modulo 4 by ﬂipping some bits, which can
be seen from the following proposition.

Proposition 2. Let g1 = x1x2x3x4x5 + x1x2x3x6x7 + x4x5x8x9x10 and
g2 = x1x2x3x4x5 + x1x2x3x6x7 + h, where g1, g2 ∈ B10 and h is a monomial
of degree 5. Then the set of the weights of 12–variable Boolean functions of
the form 0||(g1+a1)||(g2+a2)||(g1+g2+a3) contains all those integers between
1050 and 1110 that are congruent with 2 modulo 4, where a1, a2, a3 ∈ F2.

Proof. Since wt(g1) = 74, we have

wt(0||(g1 + 1)||g2||(g1 + g2)) = 876 + wt(0||g1||g2||(g1 + g2)).

Then by Lemma 7,

{1050, 1054, 1058, 1062, 1066, 1070, 1074, 1078, 1086} ⊆ {wt(0||(g1+1)||g2||(g1+g2))}.

Take h = x1x4x6x7x8, then wt(g2) = 72 and wt(g1 + g2) = 56. Hence

wt(0||g1||(g2 + 1)||(g1 + g2)) = 74 + 1024 − 72 + 56 = 1082.

Take h = x1x2x3x4x8, then wt(g2) = 48 and wt(g1 + g2) = 56. Therefore,

wt(0||g1||(g2 + 1)||(g1 + g2)) = 74 + 1024 − 48 + 56 = 1106,

wt(0||g1||g2||(g1 + g2 + 1)) = 74 + 48 + 1024 − 56 = 1090.

7

Take h = x1x2x6x7x8, then wt(g2) = 56 and wt(g1 + g2) = 60. Hence,

wt(0||g1||(g2 + 1)||(g1 + g2)) = 74 + 1024 − 56 + 60 = 1102,

wt(0||g1||g2||(g1 + g2 + 1)) = 74 + 56 + 1024 − 60 = 1094.

Take h = x1x2x3x8x9, then wt(g2) = 56, wt(g1 + g2) = 56 and

wt(0||g1||(g2 + 1)||(g1 + g2)) = 74 + 1024 − 56 + 56 = 1098.

Take h = x1x2x3x4x6, then wt(g2) = 48 and wt(g1 + g2) = 60. Therefore,

wt(0||g1||(g2 + 1)||(g1 + g2)) = 74 + 1024 − 48 + 60 = 1110,

and the result follows.

Based on Construction 1, we can also obtain all weights between 1056
and 1116 that are congruent with 0 modulo 4.

Proposition 3. Let g1 = x1x2x3x4x5 + x1x2x3x6x7 + x1x7x8x9x10 and
g2 = x1x2x3x4x5 + x1x2x3x6x7 + h, where g1, g2 ∈ B10 and h is a monomial
of degree 5. Then the set of the weights of 12–variable Boolean functions of
the form 0||(g1+a1)||(g2+a2)||(g1+g2+a3) contains all those integers between
1056 and 1116 that are congruent with 0 modulo 4, where a1, a2, a3 ∈ F2.

Proof. By Lemma 5, wt(g1) = 22 − 24 − 22 − 23 + 96 = 72. Take h =
x1x2x3x4x7, then wt(g2) = 48 and wt(g1 + g2) = 56. Hence

wt(0||(g1 + 1)||g2||(g1 + g2)) = 1024 − 72 + 48 + 56 = 1056,

wt(0||g1||(g2 + 1)||(g1 + g2)) = 72 + 1024 − 48 + 56 = 1104,

wt(0||g1||g2||(g1 + g2 + 1)) = 72 + 48 + 1024 − 56 = 1088.

Take h = x1x2x3x4x6, then wt(g2) = 48 and wt(g1 + g2) = 60. Therefore,

wt(0||(g1 + 1)||g2||(g1 + g2)) = 1024 − 72 + 48 + 60 = 1060,

wt(0||g1||(g2 + 1)||(g1 + g2)) = 72 + 1024 − 48 + 60 = 1108,

wt(0||g1||g2||(g1 + g2 + 1)) = 72 + 48 + 1024 − 60 = 1084.

Take h = x1x2x4x5x8, then wt(g2) = 56 and wt(g1 + g2) = 56. Hence,

wt(0||(g1 + 1)||g2||(g1 + g2)) = 1024 − 72 + 56 + 56 = 1064,

wt(0||g1||(g2 + 1)||(g1 + g2)) = 72 + 1024 − 56 + 56 = 1096.

8

Take h = x1x4x5x8x9, then wt(g2) = 68 and wt(g1 + g2) = 48. Therefore,

wt(0||(g1 + 1)||g2||(g1 + g2)) = 1024 − 72 + 68 + 48 = 1068,

wt(0||g1||(g2 + 1)||(g1 + g2)) = 72 + 1024 − 68 + 48 = 1076,

wt(0||g1||g2||(g1 + g2 + 1)) = 72 + 68 + 1024 − 48 = 1116.

Take h = x1x2x4x5x7, then wt(g2) = 64, wt(g1 + g2) = 56 and

wt(0||(g1 + 1)||g2||(g1 + g2)) = 1024 − 72 + 64 + 56 = 1072.

Take h = x1x2x4x5x6, then wt(g2) = 64 and wt(g1 + g2) = 60. Hence

wt(0||g1||(g2 + 1)||(g1 + g2)) = 72 + 1024 − 64 + 60 = 1092,

wt(0||g1||g2||(g1 + g2 + 1)) = 72 + 64 + 1024 − 60 = 1100.

Take h = x1x4x5x6x8, then wt(g2) = 72 and wt(g1 + g2) = 56. Therefore,

wt(0||g1||(g2 + 1)||(g1 + g2)) = 72 + 1024 − 72 + 56 = 1080,

wt(0||g1||g2||(g1 + g2 + 1)) = 72 + 72 + 1024 − 56 = 1112,

and the result follows.

From the OEIS sequence A146976 [12], the set of weights in RM (4, 8)
contains all 16i, for 0 ≤ i ≤ 16. Moreover, the set of weights in RM (5, 10)
was determined by Carlet recently which contains all even integers between
72 and 952 [2].

Lemma 8 ([7, 12]). The set of weights in RM (4, 8) contains all 16i, where
i ranges over the set of consecutive integers from 0 to 16.

Lemma 9 ([2]). The set of weights in RM (5, 10) contains all even integers
between 72 and 952.

Proposition 4. Let A = {0, 64, 96, 112, 120, 124, 126, 128, 136, 144, 148} and
S be the set of all weights in RM (6, 12). Then

S = A ∪ {152 + 2i} ∪ {2
12 − a | a ∈ A},

where i ranges over the set of consecutive integers from 0 to 211 − 152.

Proof. Consider those functions of the form g = g0||g1||g2||(g1 + g2 + g3),
where g0, g3 ∈ RM (4, 10) and g1, g2 ∈ RM (5, 10). By Lemma 1, g ∈
RM (6, 12). Clearly,

wt(g) = wt(g0) + wt(0||g1||g2||(g1 + g2 + g3)).

9

By Lemma 8, wt(g0) can achieve all 64i, for 0 ≤ i ≤ 16. Therefore, by
Propositions 1 and 2, wt(g) can achieve all the numbers of the set

{154 + 64i ≤ a ≤ 214 + 64i} ∪ {1050 + 64i ≤ a ≤ 1110 + 64i},

where a ≡ 2 (mod 4) and 0 ≤ i ≤ 16. Hence, S contains all those integers
between 154 and 2134 that are congruent with 2 modulo 4. If f ∈ RM (5, 10),
then g = 0||0||f ||f ∈ RM (6, 12) and wt(g) = 2wt(f ). Therefore, by Lemma
9, S contains all those integers between 152 and 1904 that are congruent
with 0 modulo 4. Moreover, by Lemma 8 and Proposition 3, S contains all
those integers between 1908 and 2048 that are congruent with 0 modulo 4.
Therefore, {152 + 2i | 0 ≤ i ≤ 2
11 − 76} ⊆ S.

Then by Lemma 2 and wt(g + 1) = 212 − wt(g) for g ∈ RM (6, 12),

S = A ∪ {152 + 2i} ∪ {2
12 − a | a ∈ A},

where i ranges over the set of consecutive integers from 0 to 212 − 152.

Theorem 2. Let A = {0, 64, 96, 112, 120, 124, 126, 128, 136, 144, 148} and S
be the set of all weights in RM (m − 6, m), where m ≥ 12. Then

S = A ∪ {152 + 2i} ∪ {2
m − a | a ∈ A},

where i ranges over the set of consecutive integers from 0 to 2m−1 − 152.

Proof. By Proposition 4, the result is correct for m = 12. Assuming the
result is correct for m, we now prove that it is also correct for m + 1. Let S
be the set of all weights in RM (m−7, m+1). Since 0||f ∈ RM (m−7, m+1)
for any f ∈ RM (m − 6, m), and wt(0||f ) = wt(f ), we have

A ∪ {152 + 2i | 0 ≤ i ≤ 2
m−1 − 152} ⊆ S. (1)

Let g1 ∈ RM (m − 6, m) with wt(g1) = 152. Since g1||g2 ∈ RM (m − 7, m + 1)
for any g2 ∈ RM (m − 6, m) and wt(g1||g2) = 152 + wt(g2), we have

{152 + 2i | 2
m−1 − 152 ≤ i ≤ 2
m−1} ⊆ S. (2)

Moreover, wt(f + 1) = 2m+1 − wt(f ), for any f ∈ RM (m − 7, m + 1). Then
by (1) and (2), we have

A ∪ {152 + 2i} ∪ {2
m+1 − a | a ∈ A} ⊆ S,

10

where i ranges over the set of consecutive integers from 0 to 2m − 152. Then
by [8, 9] and the fact that the weights in RM (m − 6, m) must be even, we
have S ⊆ A ∪ {152 + 2i} ∪ {2
m+1 − a | a ∈ A},

and the result follows.

This conﬁrms for c = 6 the conjecture stated in [5] about the weight
spectrum of RM (m − c, m), which was later presented as an open question
since it seemed to be very diﬃcult to make a prediction by further study [2].
However, by studying Construction 1 and its generalization, we think that
the conjecture could be true. So, we prefer to state it as a conjecture.

Conjecture 1 (Conjecture of [5], Open question of [2]). Let c be any positive
integer. For m ≥ 2c, the weight spectrum of RM (m − c, m) is of the form

{0} ∪ A ∪ B ∪ C ∪ B ∪ A ∪ {2
m},

where:
A ⊆ [2c, 2c+1] is given by Kasami and Tokura [8],
B ⊆ [2c+1, 2c+1 + 2c−1] is given by Kasami, Tokura and Azumi [9],
C ⊆ [2c+1+2c−1, 2m−1 −2c+1−2c−1] consists of all consecutive even integers,
A stands for the complement to 2m of A, and B stands for the complement
to 2m of B.

4 Trying to extend the result to RM(m − c, m)

Inspired by the above method to deal with RM (6, 12), we consider the
following more general construction.

Construction 2. Let g1 = x1x2 · · · xm + xi1xi2 · · · xim + xim+1 · · · xi2m and
g2 = x1x2 · · · xm + xi2m+1 · · · xi3m + xi3m+1 · · · xi4m, where g1, g2 ∈ B2m and
1 ≤ i1, . . . , i4m ≤ 2m. We then construct g = 0||(g1 +a1)||g2||(g1 +g2 +a2) ∈
RM (m + 1, 2m + 2), where a1, a2 ∈ F2.

By analyzing the weights of those functions in Construction 2 for m =
4, 5, we propose the following more ambitious conjecture, which implies Con-
jecture 1.

Conjecture 2. Let S be the set of all weights generated by Construction 2.
Then {2
m+2 + 2
m + 2i} ∪ {2
2m + 2
m + 2i} ⊆ S,

where 0 ≤ i < 2m and m ≥ 4.
 11

From the discussion in Section 3, Conjecture 1 is true for m = 5. It
is quite easy to verify the conjecture for m = 4. In fact, we calculate the
weights for those functions of Construction 2 using the computer, and ﬁnd
that there exist many functions achieving the values of {80+2i}∪{272+2i},
which can be seen from the following Table 1, where num(f ) denotes the
number of functions in Construction 2 with the weight wt(f ).

Table 1: Number of f ∈ B10 in Construction 2 with the desired weight

wt(f ) 80 82 84 86 88 90 92 94
num(f ) 1426248 85248 1680384 208224 2789312 351872 3152040 541824
wt(f ) 96 98 100 102 104 106 108 110
num(f ) 3690240 516192 3553440 465024 2186472 190080 940032 33696
wt(f ) 272 274 276 278 280 282 284 286
num(f ) 2801168 323648 4203144 601632 6844464 849888 7165472 916336
wt(f ) 288 290 292 294 296 298 300 302
num(f ) 7051536 816576 5449440 629808 3956448 373984 2145576 173088

Proposition 5. Conjecture 2 implies Conjecture 1.

Proof. Let S be the set of all weights of those functions 0||(g1 +a1)||g2||(g1 +
g2 + a2) ∈ RM (m + 1, 2m + 2), where g1, g2 ∈ RM (m, 2m) and a1, a2 ∈ F2.
If Conjecture 2 is true, then we have

{2
m+2 + 2
m + 2i} ∪ {2
2m + 2
m + 2i} ⊆ S, (3)

where 0 ≤ i < 2m and m ≥ 4. We ﬁrst prove that the weight spectrum of
RM (m, 2m) is the same as that of Conjecture 1. Assuming this is true for
m ≤ k, we now consider m = k+1. Let g0 ∈ RM (k−1, 2k). Then wt(g0) can
achieve the values 4i, where i ranges over all the weights of RM (k−1, 2k−2).
By the assumption, wt(g0) can achieve 2k+1i, for 0 ≤ i ≤ 2k−1. Hence by
(3), {2k+2 + 2k + 2i} ⊆ S, where 0 ≤ i ≤ 22k. Then by the results of [8, 9]
and wt(g+1) = 22k+2 −wt(g) for g ∈ RM (k+1, 2k+2), the weight spectrum
of RM (k + 1, 2k + 2) is also the same as that of Conjecture 1. Then similar
to the proof of Theorem 2, we can deduce the result.

To prove Conjecture 1, by Proposition 5, we only need to determine the
weights of some functions in Construction 2 and prove that Conjecture 2 is
true. This seems to be feasible if all the desired weights can be achieved

12

by those functions of Construction 2 satisfying that g1 + g2 is with two
monomials, which is true for m = 4. However, for m = 5, the weight 214
cannot be achieved by such functions. If further study shows that for m ≥ 6
all the desired weights can be achieved by those functions such that g1 + g2
is with two monomials, then by using Lemmas 3 and 5, one may prove the
conjecture and determine the weight spectra of all codes RM (m − c, m)
for m ≥ 2c, which would be a milestone in the research on Reed–Muller
codes. However, if unlucky, some weights cannot be achieved, we then need
to investigate the weights of those functions with four monomials and try to
deduce an elegant formula. That is, a formula for wt(f ) with

f = x1x2 · · · xm + xi1 · · · xim + xim+1 · · · xi2m + xi2m+1 · · · xi3m ∈ B2m,

where {i1, i2, · · · , i3m} ⊆ {1, 2, · · · , 2m}. If we succeed, then it could still
be feasible to prove Conjecture 2.

5 Conclusion

Determining the weight distributions and the weight spectra of the Reed-
Muller codes RM (r, m) is a challenging task. The weight spectra of the
Reed–Muller codes RM (r, m) were unknown for r = 3, ..., m − 5. In 2024,
Carlet determined the weight spectrum of RM (m − 5, m) for m ≥ 10 using
the Maiorana–McFarland construction, where he tried to extend the result
to RM (m − 6, m), but not succeeded. In this paper, we propose a novel way
of constructing Reed–Muller codewords and determine the weight spectrum
of RM (m − 6, m) for m ≥ 12, which gives a positive answer to an open
question on the weight spectrum of RM (m − c, m) for c = 6.
We propose a construction based on the concatenation of four functions
which can provide many weights, and put forward a conjecture on that
construction. We verify the conjecture for some cases, and it seems to be
feasible to prove it. Further study may verify the conjecture for RM (7, 14)
and determine the weight spectrum of RM (m − 7, m). If the conjecture is
true, then that open question can be completely solved, which would be a
milestone in the research on Reed-Muller codes.

Acknowledgment

The authors would like to thank the ﬁnancial support from the National
Natural Science Foundation of China (Grant 62172230) and Natural Science

13

Foundation of Jiangsu Province (No. BK20201369). We also thank the
anonymous reviewers, whose comments helped improving the paper.

References

[1] C. Carlet, “Boolean Functions for Cryptography and Coding Theory,”
Cambridge University Press, 2021.

[2] C. Carlet, “The weight spectrum of the Reed-Muller codes
RM (m − 5, m),” to appear in IEEE Trans. Inform. Theory. See
https://ieeexplore.ieee.org/document/10363215.

[3] C. Carlet, D. K. Dalai, K. C. Gupta and S. Maitra, “Algebraic immu-
nity for cryptographically signiﬁcant Boolean functions: analysis and
construction,” IEEE Trans. Inf. Theory 52:7 (2006), 3105–3121.

[4] C. Carlet, S. Mesnager, “On the supports of the Walsh transforms of
Boolean functions,” Proceeding of First Workshop on Boolean Func-
tions: Cryptography and Applications (BFCA 2005), 2005.

[5] C. Carlet and P. Sol´e, “The weight spectrum of two families of Reed-
Muller codes,” Discrete Mathematics 346:10 (2023), 113568. See also
http://arxiv.org/abs/2301.13497.

[6] T. W. Cusick, P. St˘anic˘a, “Cryptographic Boolean Functions and Ap-
plications,” Elsevier–Academic Press, 2009.

[7] Y. Desaki, T. Fujiwara and T. Kasami, “Weight distribution,”
https://isec.ec.okayama-u.ac.jp/home/kusaka/wd/index.html.

[8] T. Kasami and N. Tokura, “On the weight structure of the Reed–Muller
codes, ” IEEE Trans. Inform. Theory 16 (1970), 752–759.

[9] T. Kasami, N. Tokura and S. Azumi, “On the Weight Enumeration
of Weights Less than 2.5d of Reed–Muller Codes, ” Information and
Control 30 (1976), 380–395.

[10] R. J. McEliece, “Weight congruence for p-ary cyclic codes,” Discrete
Mathematics 3 (1972), 177–192.

[11] F. J. MacWilliams and N. J. Sloane, “The theory of error-correcting
codes, ” North Holland. 1977.
 14

[12] N.J. Sloane, “Online Encyclopedia of Integer Sequences (OEIS), ”
https://oeis.org/A146976.

[13] Q. Wang, “The covering radius of the Reed–Muller code RM (2, 7) is
40,” Discrete Mathematics 342 (2019), 111625.

[14] Q. Wang, C. H. Tan and P. St˘anic˘a, “Concatenations of the Hidden
Weighted Bit Function and Their Cryptographic Properties,” Advances
in Mathematics of Communications 8:2 (2014), 153–165.

15
