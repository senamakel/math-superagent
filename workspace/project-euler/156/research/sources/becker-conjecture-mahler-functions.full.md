<!-- source: https://inria.hal.science/hal-01885598v1/file/BellChyzakCoonsDumas-2018-BCM.pdf | converted from PDF -->

HAL Id: hal-01885598

https://inria.hal.science/hal-01885598v1

Submitted on 2 Oct 2018

HAL is a multi-disciplinary open access archive
for the deposit and dissemination of scientific re-
search documents, whether they are published or not.
The documents may come from teaching and research
institutions in France or abroad, or from public or pri-
vate research centers.
 L’archive ouverte pluridisciplinaire HAL, est des-
tinée au dépôt et à la diffusion de documents scien-
tifiques de niveau recherche, publiés ou non, émanant
des établissements d’enseignement et de recherche
français ou étrangers, des laboratoires publics ou
privés.

Distributed under a Creative Commons CC BY 4.0 - Attribution - International License

Becker’s conjecture on Mahler functions

Jason P. Bell, Frédéric Chyzak, Michael Coons, Philippe Dumas

To cite this version:

Jason P. Bell, Frédéric Chyzak, Michael Coons, Philippe Dumas. Becker’s conjecture on Mahler functions.
Transactions of the American Mathematical Society, 2019, 372, pp.3405–3423. ⟨10.1090/tran/7762⟩. ⟨hal-
01885598⟩
 BECKER’S CONJECTURE ON MAHLER FUNCTIONS

JASON P. BELL, FR´ED´ERIC CHYZAK, MICHAEL COONS, AND PHILIPPE DUMAS

Abstract. In 1994, Becker conjectured that if F (z) is a k-regular power series,
then there exists a k-regular rational function R(z) such that F (z)/R(z) satisﬁes
a Mahler-type functional equation with polynomial coeﬃcients where the initial
coeﬃcient satisﬁes a0(z) = 1. In this paper, we prove Becker’s conjecture in
the best-possible form; we show that the rational function R(z) can be taken
to be a polynomial zγ Q(z) for some explicit non-negative integer γ and such
that 1/Q(z) is k-regular.
 1. Introduction

Let k ⩾ 2 be an integer. A Laurent power series F (z) ∈ C((z)) is called k-Mahler
provided there exist a positive integer d and polynomials a0(z), . . . , ad(z) ∈ C[z]
with a0(z)ad(z) ̸= 0 such that F (z) satisﬁes the Mahler-type functional equation

(1) a0(z)F (z) + a1(z)F (zk) + · · · + ad(z)F (zkd ) = 0.

The minimal d for which such an equation exists is called the degree of F (z).
There has been a ﬂurry of recent activity involving the study of Mahler series—see,
e.g. [2, 5, 6, 7, 8, 11, 17, 18, 19]—in large part due to the fact that one can often
deduce transcendence of special values of Mahler series by knowing transcendence
of the series itself, and also due to the guiding principle that much of the theory
of Mahler series should mirror the much better developed theory of solutions to
homogeneous diﬀerential equations.
A special subclasses of Mahler functions is the ring of k-regular power series.
These functions are deﬁned from their coeﬃcient sequences. More speciﬁcally, a
power series F (z) = n⩾0 f (n)zn is k-regular provided there is a positive integer D,
vectors ℓ, c ∈ CD×1, and matrices A0, . . . , Ak−1 ∈ CD×D, such that for all n ⩾ 0,

f (n) = ℓ
T Ais · · · Ai0c,

where (n)k = is · · · i0 is the base-k expansion of n. Allouche and Shallit [3] introduced
k-regular sequences in the early nineties as a generalisation of k-automatic sequences;
Becker [4, Theorem 1] showed that a k-regular power series is k-Mahler.
Since a k-regular power series is k-Mahler, an immediate question arises: can
one determine if a solution to (1) is k-regular, or not, based solely on properties of
the functional equation? Towards answering this question, Becker [4, Theorem 2]
showed that if a0(z) = 1, then F (z) is k-regular. He conjectured [4, p. 279] that

Date: April 20, 2018.
2010 Mathematics Subject Classiﬁcation. Primary 11B85, 30B10; Secondary 68R15.
Key words and phrases. Automatic sequences, regular sequences, Mahler functions.
The research of J. P. Bell was partially supported by an NSERC Discovery Grant. M. Coons
was visiting the Alfr´ed R´enyi Institute of the Hungarian Academy of Sciences during the time this
research was undertaken; he thanks the Institute and its members for their kindness and support.

1

2 JASON P. BELL, FR´ED´ERIC CHYZAK, MICHAEL COONS, AND PHILIPPE DUMAS

a sort of converse to this result also holds. Speciﬁcally, Becker conjectured that
if F (z) is a k-regular power series, then there exists a nonzero k-regular rational
function R(z) such that F (z)/R(z) satisﬁes a Mahler-type functional equation (1)
with a0(z) = 1. In view of this conjecture, a power series F (z) is called k-Becker
provided it satisﬁes a functional equation (1) with a0(z) = 1.
The historical signiﬁcance of the k-Becker property lies in the fact that zeros of
a0(z) in the minimal Mahler equation (1) for F (z) are values α at which the theorems
proving transcendence of F (α) based upon knowledge of algebraic independence
of certain related Mahler functions do not apply; this point is highlighted in the
works of Loxton and van der Poorten [13, 14] and the celebrated result of Nishioka
[15, 16]. In this paper, we prove (a bit more than) Becker’s conjecture.

Theorem 1. If F (z) is a k-regular power series, there exist a nonzero polynomial
Q(z) with Q(0) = 1 such that 1/Q(z) is k-regular and a nonnegative integer γ such
that F (z)/zγQ(z) satisﬁes a Mahler-type functional equation (1) with a0(z) = 1.

Moreover, if the Mahler-type functional equation of minimal degree for F (z) is known,
then the polynomial Q(z) in Theorem 1 can be easily written down. Speciﬁcally,
if (1) is the minimal functional equation for F (z), and we write A for the set of
roots of unity ζ such that ζ kM ̸= ζ for all M ⩾ 1 and a0(ζ) = 0, then there is an N
depending on a0(z) such that

Q(z) :=
 ζ∈A
 N −1

j=0 (1 − zkj ζ kN )
νζ (a0(z)),

where for a given Laurent power series g(z), νζ(g(z)) is the order of the zero of g(z)
at z = ζ. For more details, see the proof of Lemma 10. Noting that all of the zeros
of the polynomial Q(z) are roots of unity of order not coprime to k, we may combine
this with a result of Dumas [10, Th´eor`eme 30] to give the following proposition.

Proposition 2. Let F (z) ∈ C[[z]], then F (z) is k-regular if and only if F (z) satisﬁes
some functional equation (1) such that all of the zeros of a0(z) are either zero or
roots of unity of order not coprime to k.

Note that the functional equation alluded to in the above proposition need not be
minimal.
To prove Theorem 1, we will show that if F (z) is k-regular satisfying (1), then,
essentially, one can ‘remove’ all of the zeros of a0(z) that are roots of unity. We then
show that, after dividing by an appropriate power of z, the resulting function satisﬁes
another Mahler-type functional equation with a0(z) = 1, but is not necessarily k-
Becker, since it may not be a power series.
This line of reasoning is inspired by a recent paper of Kisielewski [12], who
considered Becker’s conjecture for a subclass of regular functions. Indeed, Kisielewski
[12, Proposition 2] showed that Becker’s conjecture holds for every k-regular function
F (z) satisfying a functional equation (1) of minimal degree d such that a0(z) has no
zeros that are roots of unity; speciﬁcally, for a function F (z) in this class, he showed
there exists a k-regular rational function R(z) such that F (z)/R(z) is k-Becker; his
result is purely existential concerning the rational function R(z). In comparison,
Theorem 1 has the following corollary in this context.

PROOF OF BECKER’S CONJECTURE 3

Corollary 3. Suppose that F (z) is a k-regular function satisfying a functional
equation (1) of minimal degree d such that a0(0) ̸= 0 and a0(z) has no zeros that
are roots of unity. Then F (z) is k-Becker.

This paper is outlined as follows. Section 2 contains preliminary results that will
be needed in Section 3, which contains the proof of Theorem 1. Section 4 contains
justiﬁcation that Theorem 1 is the best-possible resolution of Becker’s conjecture;
in particular, in that section, we give an example of a k-regular function F (z) such
that for any rational function R(z), the function R(z)F (z) cannot simultaneously be
a power series and satisfy the conclusion of Becker’s conjecture. Finally, in Section 5
we prove Proposition 2.
 2. Preliminaries

We require the following deﬁnition, and lemmas due to Becker [4, Lemma 3] and
Kisielewski [12, Lemma 8], respectively.

Deﬁnition 4. Let C(z) = n⩾0 c(n)zn. Given a positive integer k ⩾ 2, for each
i ∈ {0, . . . , k − 1}, we deﬁne the Cartier operator Λi : C[[z]] → C[[z]] by

Λi(C)(z) =
 n⩾0 c(kn + i)zn.

Lemma 5 (Becker [4]). The function F (z) ∈ C[[z]] is k-regular if and only if the
C-vector space
 V := ⟨{Λrn · · · Λr1(F )(z) : 0 ⩽ ri < k, n ∈ N}⟩C
is ﬁnite-dimensional.

If one lets W denote the ﬁnitely generated C[z]-submodule of the ﬁeld of Laurent
power series C((z)) spanned by the ﬁnite-dimensional C-vector space V , then W
has the property that W ⊆
 h(z)∈W C[z]h(zk).

To see this, we let {h1(z), . . . , hr(z)} be a basis for V . Then notice that for
i = 0, . . . , k − 1, we have
 Λi(hj)(z) =
 r

ℓ=1 ci,j,ℓhℓ(z)

for some constants ci,j,ℓ ∈ C. This then gives that

hj(z) =
 r

ℓ=1
 k−1

i=0 ci,j,ℓzi hℓ(zk),

which gives the desired claim.

Lemma 6 (Kisielewski [12]). Let c(z) ∈ C(z), α ∈ C \ {0}, and να(c(z)) be the
order of the zero of c(z) at z = α. There is an r ∈ {0, . . . , k − 1} such that
να Λr(c)(zk) ⩽ να (c(z)) .

We will use the functional equation (1) in a slightly diﬀerent form. For a Mahler
function satisfying (1) of degree d, setting

F(z) := [F (z), F (zk), . . . , F (zkd−1 )]
T

4 JASON P. BELL, FR´ED´ERIC CHYZAK, MICHAEL COONS, AND PHILIPPE DUMAS

and
 A(z) := − a1(z)
a0(z) − a2(z)
a0(z) · · · − ad(z)
a0(z)
I(d−1)×(d−1) 0(d−1)×1 ,

we have

(2) F(z) = A(z)F(zk).

We will be speciﬁcally interested in the matrices

(3) Bn(z) := A(z)A(zk) · · · A(zkn−1 ).

Note that F(z) = Bn(z)F(zkn) for every n ⩾ 1. In what follows, for i = 1, . . . , d,
we write ei := 01×(i−1) 1 01×(d−i) T .

Kisielewski’s lemma above states that a Cartier operator can be used to (possibly)
reduce the order of a zero. We use this result in the following lemma to ﬁnd an
upper bound on the order of certain poles of the matrices Bn(z).

Lemma 7. Suppose F (z) is k-regular, Bn(z) is as deﬁned in (3), and ξ is a root
of unity such that ξk = ξ. Then the poles at z = ξ of the entries of the matrices
{Bn(z) : n ⩾ 1} have uniformly bounded order. In particular, there is a polynomial
h(z) ∈ C[z] such that for each n the matrix h(z) · Bn(z) has polynomial entries.

Proof. For each i ∈ {1, . . . , d} and each n ∈ N, set

ci,n(z) := eT
1 Bn(z)ei.

Then for each n we have

(4) F (z) =
 d

i=1 ci,n(z)F (zki+n−1 ).

If we apply n Cartier operators to (4), we have

(5) Λrn · · · Λr1 (F )(z) =
 d

i=1 Λrn · · · Λr1(ci,n)(z) · F (zki−1 ).

Since d here is minimal, the functions F (z), . . . , F (zkd−1) are linearly independent
over C(z).
Now suppose F (z) is k-regular. Since the C-vector space V deﬁned in Lemma 5 is
ﬁnite-dimensional, its ﬁnite number of generators are of the form d
i=1 hi(z)F (zki−1 ),
for some rational functions hi(z). Since, as we run over a ﬁnite generating set,
the hi(z) that occur are a ﬁnite number of rational functions and the functions
F (z), . . . , F (zkd−1 ) are linearly independent over C(z), there is a nonzero polynomial
h(z) such that
 V ⊆ h(z)
−1 d

i=1 C[z]F (zki−1).

This, requires for every i ∈ {1, . . . , d}, n ∈ N and choice of Cartier operators that
the inequality

(6) νξ h(z)
−1 ⩽ νξ (Λrn · · · Λr1 (ci,n)(z))

PROOF OF BECKER’S CONJECTURE 5

holds between orders of the zeros at z = ζ. Since ξk = ξ, for each rational function
c(z), we have νξ (c(z)) = νξ c(zk) . By Lemma 6 and (6), for each n ∈ N there is a
choice of Cartier operators Λr1 , . . . , Λrn such that, for zero orders,

νξ (h(z)) ⩽ νξ (Λrn · · · Λr1(ci,n)(z)) = νξ Λrn · · · Λr1(ci,n)(zkn ) ⩽ νξ (ci,n(z)) .

Thus the poles of the entries ci,n(z) of the ﬁrst row of the matrices Bn(z) at z = ξ
have uniformly bounded order; speciﬁcally, they are bounded above by νζ(h(z)).
It remains now to show this for the rest of the rows, but this follows due to the
structure of the matrix A(z). In fact, consider the (i, j) entry of the matrix Bn(z)
for some i ∈ {2, . . . , d}. Using the deﬁnition of Bn(z), we have

eT
i Bn(z)ej = eT
i A(z)Bn−1(zk)ej.

Now, eT
i A(z) = eT
i−1. So,

(7) νξ(eT
i Bn(z)ej) = νξ(eT
i−1Bn−1(zk)ej) = νξ(eT
i−1Bn−1(z)ej),

where the last equality uses, again, the facts that ξk = ξ and for every rational
function νξ (c(z)) = νξ c(zk) . Applying (7) i − 1 times, we have

(8) νξ(eT
i Bn(z)ej) = νξ(e
T
1 Bn−i+1(z)ej),

which immediately implies the desired result. □

Proposition 8. If F (z) is k-Mahler satisfying (1) of degree d, a0(ξ) = 0 for some
root of unity ξ with ξk = ξ, and gcd(a0(z), a1(z), . . . , ad(z)) = 1, then F (z) is not
k-regular.

Proof. Towards a contradiction, assume that F (z) is k-regular and suppose that ξ
is a root of unity with ξk = ξ such that a0(ξ) = 0. Using Lemma 7, let Y denote
the minimal uniform bound of the order of the poles at z = ξ of {Bn(z) : n ⩾ 1},
and note that Y > 0 since gcd(a0(z), a1(z), . . . , ad(z)) = 1.
We examine the ﬁrst row of B1(z) = A(z). In particular, set

N := min i ∈ {1, . . . , d} : νξ ai(z)
a0(z) ⩽ νξ aj(z)
a0(z) for all j ∈ {1, . . . , d} ,

and note, again using gcd(a0(z), a1(z), . . . , ad(z)) = 1, that

(9) X := −νξ aN (z)
a0(z) > 0.

By the minimality of N , we have both

νξ(ai(z)/a0(z)) > −X for i < N,

and νξ(ai(z)/a0(z)) ⩾ −X for i > N.

Since B1(z) = A(z) has only constant entries outside of its ﬁrst row, (7) and (8)
imply there is some minimal n, say m, for which the maximal order of the pole at
z = ξ of the entries of Bm(z) is Y , occurs in the ﬁrst row of Bm(z), say in the (1, J)
entry, and all of the other rows have entries with poles at z = ξ of order strictly less
than Y . That is, speciﬁcally, within the J-th column of Bm(z), we have

(10) νξ eT
1 Bm(z)eJ = −Y < 0 and νξ eT
i Bm(z)eJ > −Y,

for each i ∈ {2, . . . , d}.

6 JASON P. BELL, FR´ED´ERIC CHYZAK, MICHAEL COONS, AND PHILIPPE DUMAS

Now, deﬁne the rational functions b1(z), . . . , bd(z) by

Bm+N −1(zk)eJ = b1(z) · · · bd(z) T ,

and note that by (8) we have, since ξk = ξ and for every rational function νξ (c(z)) =
νξ c(zk) , that

(11) −Y = νξ(eT
1 Bm(z)eJ ) = νξ(eT
N Bm+N −1(z)eJ ) = νξ(bN (z)).

By the minimality of m, we have

νξ(bi(z)) > −Y for i > N,

and trivially νξ(bi(z)) ⩾ −Y and i < N.
We put together the results of the previous paragraphs to give the desired result.
Indeed, consider the ﬁrst entry of the Jth column of Bm+N (z). We have

eT
1 Bm+N (z)eJ = eT
1 A(z)Bm+N −1(zk)eJ

= − a1(z)
a0(z) − a2(z)
a0(z) · · · − ad(z)
a0(z) Bm+N −1(zk)eJ

= −
 N −1

i=1
 ai(z)bi(z)
a0(z) − aN (z)bN (z)
a0(z) −
 d

i=N +1
 ai(z)bi(z)
a0(z) .(12)

For i ̸= N , using the comments immediately below Equations (11) and (9), respec-
tively, we have

(13) νξ ai(z)bi(z)
a0(z) = νξ ai(z)
a0(z) + νξ (bi(z)) > −X − Y,

since both νξ (ai(z)/a0(z)) > −X for i ∈ {1, . . . , N − 1} and νξ (bi(z)) > −Y for
i ∈ {N + 1, . . . , d}. Also, by (11) and (9), we have

(14) νξ aN (z)bN (z)
a0(z) = νξ aN (z)
a0(z) + νξ (bN (z)) = −X − Y.

Hence, using (13) and (14), Equation (12) gives the inequality

νξ eT
1 Bm+N (z)eJ = −X − Y < −Y,

contradicting that Y is a uniform bound on the pole order at z = ξ over all
eT
i Bn(z)ej. Thus F (z) is not k-regular. □

Corollary 9. Suppose F (z) is k-regular satisfying (1) of degree d. Let I be the
ideal of polynomials p(z) such that

p(z)F (z) ∈
 j⩾1 C[z]F (zkj )

and let q(z) be a generator for I. If ξ is a zero of q(z) such that ξkM = ξ for some
M ⩾ 1, then ξ = 0.

Proof. Suppose that there exists M ⩾ 1 and ξ such that q(ξ) = 0 with ξkM = ξ and
ξ ̸= 0. Let q0(z)F (z) + q1(z)F (zkM ) + · · · + qD(z)F (zkM D ) = 0
be a relation with q0(z) ̸= 0, gcd(q0(z), q1(z), . . . , qD(z)) = 1 and D minimal. Then
q(z) divides q0(z) and so q0(ξ) = 0. But ξkM = ξ and by Proposition 8 this

PROOF OF BECKER’S CONJECTURE 7

contradicts the fact that F (z) is kM -regular. Since F (z) is kM -regular if and only
if it is k-regular [3, Theorem 2.9], this proves the corollary. □

Lemma 10. Let F (z) be a k-regular power series satisfying (1) of degree d. Then
there exist a polynomial Q(z) with Q(0) ̸= 0 such that 1/Q(z) is k-regular and
a nonnegative integer γ such that G(z) := F (z)/zγQ(z) satisﬁes a Mahler-type
functional equation

q0(z)G(z) + q1(z)G(zk) + · · · + qd(z)G(zkd ) = 0,

of degree d, qi(z) ∈ C[z] with q0(0) ̸= 0, and if ζ is a zero of q0(z) that is a root of
unity then there is some M ⩾ 1 such that ζ kM = ζ.

The proof of Lemma 10 requires the following characterisation of Mahler functions
due to Dumas [10, Theorem 1, p. 151].

Theorem 11 (Structure Theorem of Dumas). A k-Mahler function is the quotient
of a series and an inﬁnite product which are k-regular. That is, if F (z) is the
solution of the Mahler functional equation

a0(z)F (z) + a1(z)F (zk) + · · · + ad(z)F (zkd ) = 0,

where a0(z)ad(z) ̸= 0, the ai(z) are polynomials, then there exists a k-regular series
G(z) such that
 F (z) = G(z)

j⩾0 Γ(zkj ) ,

where a0(z) = ρzδΓ(z), with ρ ̸= 0 and Γ(0) = 1.

Proof of Lemma 10. Suppose that F (z) is a k-Mahler power series of degree d
satisfying (1). Let A be the set of roots of unity ζ such that a0(ζ) = 0 and there
does not exist M ⩾ 1 such that ζ kM = ζ and set νζ(a0) := νζ(a0(z)). For each
ζ ∈ A, the sequence {ζ ki}i⩾0 is eventually periodic, so that there is an Mζ such
that ζ k2Mζ = ζ kMζ . Note that this then implies that ζ kpMζ = ζ kMζ for all p ⩾ 1.
Now, set
 N :=
 ζ∈A Mζ,

so that ζ k2N = ζ kN for all ζ ∈ A. Deﬁne the polynomial Q(z) by

Q(z) :=
 ζ∈A
 N −1

j=0 (1 − zkj ζ kN )
νζ (a0).

Then
 Q(zk)
Q(z) =
 ζ∈A
 1 − zkN ζ kN

1 − zζ kN
 νζ (a0)
 ∈ C[z],

since for each ζ ∈ A,

1 − zkN ζ kN = 1 − (zζ kN )
kN = (1 − zζ kN )(1 + (zζ kN ) + · · · + (zζ kN )kN −1).

8 JASON P. BELL, FR´ED´ERIC CHYZAK, MICHAEL COONS, AND PHILIPPE DUMAS

But also for each ξ ∈ A,

Q(zk)
Q(z) (1−zξkN )
νξ(a0)

= 1 − (zξ)
kN νξ(a0)
 ζ∈A\{ξ}
 1 − zkN ζ kN

1 − zζ kN
 νζ (a0)

= (1 − zξ)
νξ(a0) kN −1

j=0 (zξ)
j
 νξ(a0)
 ζ∈A\{ξ}
 1 − zkN ζ kN

1 − zζ kN
 νζ (a0)

is a polynomial. Since ξ ̸= ξkN , we have that (1 − zξ)
νξ(a0) divides the polynomial
Q(zk)/Q(z). As this is true for all ξ ∈ A, there is a polynomial h(z) such that

(15) Q(zk)
Q(z) =
 ζ∈A
(1 − zζ)νζ (a0) · h(z).

Thus the polynomial Q(z) satisﬁes

(16) Q(z) =
 j⩾0 ζ∈A(1 − zkj ζ)
νζ (a0)
 −1
 j⩾0 h(zkj )
 −1
 .

We factor a0(z) = czγΓ(z) = czγa(z) ζ∈A(1 − zζ)νζ (a0), where a(ζ) ̸= 0 for every
ζ ∈ A and a(0) = 1. By Proposition 8, since F (z) is k-regular, a0(1) ̸= 0. Then
using Theorem 11 and (16), there is a k-regular function G(z) such that

F (z) = G(z)

j⩾0 Γ(zkj ) = G(z) · Q(z) · j⩾0 h(zkj )

j⩾0 a(zkj ) .

Setting H(z) := G(z) j⩾0 h(zkj ), we have that

J(z) := F (z)
zγQ(z) = H(z)
zγ j⩾0 a(zkj ) ,

where 1/Q(z) is k-regular by an above-mentioned result of Becker [4, Theorem 2]
and (16). The function J(z) satisﬁes the Mahler functional equation

ca(z)J(z) +
 d

i=1 zγ(ki−2)ai(z)
 i−1

j=1 ζ∈A(1 − ζzkj )
νζ (a0) i−1

j=0 h(zkj ) J(zki) = 0.

Note that here d is (still) minimal, since d is the degree of F (z). □

Our method of proof of Lemma 10 is inspired by remarks of Becker [4, p. 279] as
well as an argument of Adamczewski and Bell [1, Proposition 7.2].

3. Proof of the main result

Proof of Theorem 1. Suppose that F (z) is a k-regular function satisfying (1) of
degree d. By Lemma 10, there exist a polynomial Q(z) with Q(0) = 1 such that

PROOF OF BECKER’S CONJECTURE 9

1/Q(z) is k-regular and a nonnegative integer γ such that the k-Mahler function
G(z) := z−γF (z)/Q(z) satisﬁes a Mahler functional equation

(17) q0(z)G(z) + q1(z)G(zk) + · · · + qd(z)G(zkd ) = 0

of minimal degree d, qi(z) ∈ C[z], and q0(z) has the property that q0(0) ̸= 0 and if
q0(ζ) = 0 with ζ a root of unity then there is some M ⩾ 1 such that ζ kM = ζ.
We let I be the ideal of polynomials p(z) such that

p(z)G(z) ∈
 j⩾1 C[z]G(zkj ).

Since G is k-Mahler, I is nonzero, and we let q(z) be a generator for I whose leading
coeﬃcient is 1. Since q0(z) ∈ I, we have q(z) divides q0(z) and so we have q(0) ̸= 0.
By Corollary 9, if ζ is a zero of q(z), then there does not exist M ⩾ 1 such that
ζ kM = ζ. Thus if ζ is a root of q(z) then ζ cannot be a root of unity, since we have
shown that any zero of q0(z) that is a root of unity must satisfy ζ kM = ζ for some
M ⩾ 1, and we have also shown that each zero ζ of q0(z) that is a root of unity has
the property that there is no M ⩾ 1 such that ζ kM = ζ. Hence q(z) has no zeros
that are either zero or a root of unity. Thus G(z) has the property that there is a
relation q(z)G(z) ∈
 j⩾1 C[z]G(zkj )

with q(z) having no zeros that are roots of unity and with q(0) ̸= 0.
We now claim that q(z) = 1. To see this, suppose that q(z) is non-constant.
Then there is a nonzero complex number λ that is not a root of unity such that
q(λ) = 0. Since G(z) is k-regular, the C-vector space spanned by all elements of
the form Λrm · · · Λr0(G)(z) (including also G(z)) is ﬁnite-dimensional. Moreover,
its basis elements are of the form d
i=1 hi(z)G(zki−1), for some rational functions
hi(z), where d is the degree of the Mahler function G. Since, as we run over
a basis, only ﬁnitely many rational functions hi(z) occur and since the functions
F (z), . . . , F (zkd−1 ) are linearly independent over C(z), there is a nonzero polynomial
h(z) such that
 V ⊆ h(z)−1 d

i=1 C[z]G(zki−1 ).

Now since λ is nonzero and is not a root of unity, there exists some positive integer
N such that λkN is not a zero of h(z). Repeatedly using the Mahler Equation (17),
we obtain a relation of the form

Q(z)G(z) =
 d

j=1 Qj(z)G(zkN +j−1 )

with Q(z), Q1(z), . . . , Qd(z) polynomials and Q(z) ̸= 0 and gcd(Q(z), Q1(z), . . . ,
Qd(z)) = 1. Since Q(z) ∈ I, we see that q(z) divides Q(z) and so λ is a root of
Q(z).
Now we write
 G(z) =
 d

j=1 Rj(z)G(zkN +j−1),

10 JASON P. BELL, FR´ED´ERIC CHYZAK, MICHAEL COONS, AND PHILIPPE DUMAS

with Rj(z) := Qj(z)/Q(z).

Moreover, since gcd(Q(z), Q1(z), . . . , Qd(z)) = 1, we have νλ(Rℓ(z)) < 0 for some
ℓ ∈ {1, . . . , d}. By Lemma 6, there exists (r1, . . . , rN ) ∈ {0, 1, . . . , k − 1}N such that

νλ(ΛrN · · · Λr1(Rℓ)(zkN )) ⩽ νλ(Rℓ(z)) < 0.

Thus νλkn (ΛrN · · · Λr1(Rℓ)(z)) < 0.

Now set Tj(z) := ΛrN · · · Λr1(Rj)(z) for j = 1, . . . , d.

Then ΛrN · · · Λr1 (G)(z) ∈ V and so

d

j=1 Tj(z)G(zkj−1) ∈ V.

Since G(z), . . . , G(zkd−1) are linearly independent over C(z) we must have that
h(z)Tj(z) ∈ C[z] for j = 1, . . . , d. But νλkN (h(z)) = 0 and so νλkN (h(z)Tℓ(z)) < 0,
which contradicts the fact that h(z)Tj(z) must be a polynomial, giving the claim.
It follows that q(z) = 1.
Speciﬁcally, 1 ∈ I and so
 G(z) ∈
 j≥1 C[z]G(zkj ),

which says that G(z) satisﬁes a Mahler functional equation of the form (1) with
a0(z) = 1. This ﬁnishes the proof of Theorem 1. □

4. Optimality of the Theorem 1

The careful reader will notice that, while we prove Becker’s conjecture completely,
the resulting function F (z)/zγQ(z) that satisﬁes a Mahler-type functional equation
(1) with a0(z) = 1 is not necessarily a power series, so that (strictly speaking) it is
neither k-regular nor k-Becker. One may argue, that probably the ﬁeld of Laurent
series is a preferable setting for solutions to (1), and indeed a result of Dumas’s [10,
Th´eor`eme 7] gives reasonable bounds on the valuation at z = 0 of the solutions.

Theorem 12 (Dumas). Let F (z) be a Laurent power series solution to a Mahler-type
functional equation (1) of degree d. Then F (z) ∈ z−νC[[z]], where

ν := max ν0(ad(z))
kd , ν0(ad(z)/a0(z))
(kd − 1)
  .

In this section, we show, by giving an example, that a stronger variant of Becker’s
conjecture with the added conclusion that the resulting function F (z)/R(z) is a
power series cannot hold; that is, with the currently in-use deﬁnitions, such a
function is not necessarily k-Becker. We now state this result.

Theorem 13. Let k ⩾ 2 be a natural number. Then there exists a k-regular power
series F (z) such that there is no nonzero rational function R(z) with the property
that F (z)R(z) is a k-Becker power series.

PROOF OF BECKER’S CONJECTURE 11

We note that this does not contradict the conclusion of Theorem 1, but merely
shows that one must necessarily work in the ring of Laurent power series in order
to obtain the conclusion. More precisely, the examples we give in establishing
Theorem 13 have the property that F (z)/z is k-Becker with a pole at z = 0 and so
it has a Laurent power series expansion, but not an expansion in the ring of formal
power series around z = 0; moreover, one must introduce a pole at z = 0 in order to
obtain a k-Becker function.
Towards the goal of producing these examples, let k be a natural number that is
greater than or equal to two and consider the functional equation

A(z) = (1 − z + zk−1)A(zk) − zk2−k(1 − z)A(zk2).

Then using Hensel lemma style arguments in which one inductively produces a
consistent family of solutions mod (zn) for every n ⩾ 1, one can show that there is
a unique power series solution H(z) to this functional equation with H(0) = 1. We
also note that the function H0(z) := 1/z is a solution to this functional equation.
We continue by setting

(18) F0(z) := H(z) + 1
z ,

which again satisﬁes

(19) F0(z) = (1 − z + zk−1)F0(zk) − zk2−k(1 − z)F0(zk2).

As H(z) is a k-Becker power series, it is k-regular, thus

(20) F (z) := zF0(z) = 1 + zH(z)

is k-regular, as the k-regular power series form a ring. We note that F0(z) = F (z)/z
is k-Becker and is a Laurent power series. We show, however, that there does not
exist a nonzero rational function R(z) such that F (z)R(z) is a k-Becker power series;
that is, in order to obtain a k-Becker function that is a nonzero rational function
multiple of F (z) one must work in the ring of Laurent power series and cannot
restrict one’s focus to the ring of formal power series. In order to show the desired
result, we ﬁrst establish two key lemmas.

Lemma 14. Let k ⩾ 2 and let F0(z) be as in Equation (18). Then the Laurent
power series F0(z) and F0(zk) are linearly independent over C(z).

Proof. Suppose not. Then since F0(z) is nonzero, there is a rational function a(z)
such that F0(zk)/F (z) = a(z). We note that

F0(z) = 1
z + 1 + O(z)

and so F0(zk)
F0(z) = z1−k(1 − z + O(z2)).

It follows that there are relatively prime polynomials P (z) and Q(z) with P (0) =
Q(0) = 1 such that a(z) = z1−kP (z)/Q(z). Then since

F0(zk2) = a(z)a(zk)F0(z),

Equation (19) gives

1 = (1 − z + zk−1)z1−k · P (z)
Q(z) − zk2−k(1 − z)z1−k2 · P (z)P (zk)
Q(z)Q(zk) .

12 JASON P. BELL, FR´ED´ERIC CHYZAK, MICHAEL COONS, AND PHILIPPE DUMAS

Clearing denominators, we see

(21) zk−1Q(z)Q(zk) = (1 − z + zk−1)P (z)Q(zk) − (1 − z)P (z)P (zk).

In particular, Q(zk) divides (1 − z)P (z)P (zk) and since P (z) and Q(z) are relatively
prime, we then have that Q(zk) divides (1 − z)P (z). Similarly, P (z) divides
zk−1Q(z)Q(zk) and since P (0) = 1, and P (z) and Q(z) are relatively prime, we
see that P (z) divides Q(zk). So we may write Q(zk) = P (z)b(z) with b(z) dividing
(1 − z). Since Q(0) = P (0) = 1, we see that b(z) = 1 or b(z) = (1 − z).
Then substituting P (z) = Q(zk)/b(z) into Equation (21), we ﬁnd

zk−1Q(z)b(z)b(zk) = (1 − z + zk−1)Q(zk)b(zk) − (1 − z)Q(zk2).

Now let D denote the degree of Q(z). Then since

(1 − z)Q(zk2) = −zk−1Q(z)b(z)b(zk) + (1 − z + zk−1)Q(zk)b(zk),

and since b(z) has degree at most 1, we have

k2D + 1 ⩽ max{2k + D, 2k − 1 + kD}.

We note that this forces D ⩽ 1 with equality if and only if b(z) = 1 − z and k = 2.
To this end, we consider two quick cases. When k ⩾ 3 or k = 2 and b(z) = 1, we
have D = 0. Thus Q(z) is a constant polynomial and the condition that Q(0) = 1
gives Q(z) = 1. Then since P (z) divides Q(zk) we have that P (z) is also 1 and so
a(z) = z1−k. But
 F0(zk)
F0(z) = z1−k(1 − z + O(z2)) ̸= z1−k = a(z),

and so we get a contradiction. Thus it remains to handle the case when k = 2 and
b(z) = 1 − z. In this case, Q(z) has degree one and we have Q(z2) = P (z)(1 − z).
Plugging in z = 1 gives Q(1) = 0 and since Q(z) has degree 1 and Q(0) = 0 we have
Q(z) = 1 − z. Then Q(z2) = P (z)(1 − z) gives that P (z) = 1 + z and so

a(z) = 1
z · 1 + z
1 − z = 1
z + 2 + O(z).

But F (z2)
F (z) = 1
z − 1 + O(z),

and so we obtain a contradiction. Thus F0(z) and F0(zk) are linearly independent
over C(z). □

Lemma 15. Let F0(z) be as deﬁned above, let r ∈ N, and let h0(z), . . . , hr(z) be
rational functions such that hi(z)/zki−1 does not have a pole at z = 0 for i = 0, . . . , r.
Then, if r

i=0 hi(z)F0(zki) = 0,

then h0(0) = 0.

Proof. We prove this by induction on r. For r = 0 and r = 1, the result follows by
Lemma 14 since F0(z) and F0(zk) are linearly independent over C(z). So suppose
that the result holds for r < m with m ⩾ 2 and consider the case when r = m.

PROOF OF BECKER’S CONJECTURE 13

Towards a contradiction, suppose that

m

i=0 hi(z)F0(zki) = 0

with h0(0) nonzero and zki−1 dividing hi(z) in the local ring C[z](z). For i = 1, . . . , m,
set
 gi(z) := z−ki+1 hi(z)
h0(z) .

Then since h0(0) is nonzero, each gi(z) is regular at z = 0 and

F0(z) +
 m

i=1 gi(z)zki−1F0(zki) = 0.

Applying the Cartier operator Λ0 gives

Λ0(F0)(z) +
 m

i=1 Λ0(gi(z)zk−1)zki−1−1F0(zki−1 ) = 0.

But by (19), we have Λ0(F0)(z) = F0(z) − zk−1F0(zk), so we have

(22) 0 = (1 + Λ0(g1(z)zk−1)F0(z)

+ (−1 + Λ0(g2(z)zk−1)zk−1F0(zk)

+
 m−1

i=2 Λ0(gi+1(z)zk−1)zki−1F0(zki).

Since g1(z) is regular at z = 0, we have that g1(z)zk−1 has a power series expansion
with zero constant term and hence Λ0(g1(z)zk−1) vanishes at z = 0, and so 1 +
Λ0(g1(z)zk−1) is a rational function which is nonzero at z = 0. Since each of the
higher-index coeﬃcients in (22) are of the form zki−1 times a rational function
regular at z = 0, the induction hypothesis applies and we get a contradiction. This
contradiction proves the lemma. □

Proof of Theorem 13. Let F (z) be the k-regular power series deﬁned in (20). We
claim that there is no nonzero rational function R(z) such that function R(z)F (z) is
a k-Becker power series. Since F (0) = 1, if R(z)F (z) has a power series expansion
at z = 0, R(z) must be regular at z = 0. Suppose towards a contradiction that
there is a rational function R(z) such that R(z) is regular at z = 0 and such that
F (z)R(z) is k-Becker. Then we write R(z) = zaR0(z) with a ⩾ 0 and with R0(0)
nonzero. Then there exist a natural number d and polynomials b1(z), . . . , bd(z) such
that
 R0(z)F (z) = b1(z)zka−aR0(zk)F (zk) + · · · + bd(z)zkda−aR0(zkd )F (zkd ).

As deﬁned above, F (z) = zF0(z), so we have

R0(z)F0(z) = b1(z)zka−a+k−1R0(zk)F0(zk)(23)
 + · · · + bd(z)zkda−a+kd−1R0(zkd )F0(zkd ).

But this contradicts Lemma 15. The result follows. □

14 JASON P. BELL, FR´ED´ERIC CHYZAK, MICHAEL COONS, AND PHILIPPE DUMAS

5. A structure of Mahler functional equations for regular functions

In this section, we prove Proposition 2; that is, we show for F (z) ∈ C[[z]], the
series F (z) is k-regular if and only if F (z) satisﬁes some functional equation (1) such
that all of the zeros of a0(z) are either zero or roots of unity of order not coprime to
k. As stated in the Introduction, Proposition 2 is obtained by combining Theorem
1 with a result of Dumas [10, Th´eor`eme 30]. Dumas’s result [10, Th´eor`eme 30] is
proved by appealing to results for degree-one Mahler functions via his Structure
Theorem recorded above as Theorem 11. By appealing to Theorem 11 and the ring
structure of the set of k-regular power series, one can show that a series F (z) is
k-regular, if one can show that the inﬁnite product

H(z) := 1

j⩾0 Γ(zkj )

is k-regular. This is exactly what Dumas did via the following lemma; see [10,
Lemme 8].

Lemma 16 (Dumas). The inﬁnite product H(z) = j⩾0 Γ(zkj )−1 is k-regular if
and only if the C-vector space

 Λrn · · · Λr1 1
n−1
j=0 Γ(zkj ) : 0 ⩽ ri < k, n ∈ N

 C
is ﬁnite-dimensional.

Lemma 16 follows from Lemma 5 combined with the equality

Λrn · · · Λr1H(z) = Λrn · · · Λr1 1
n−1
j=0 Γ(zkj )

 H(z),

which itself follows from the fact that H(z) is a degree-one Mahler function satisfying
the functional equation Γ(z)H(z) − H(zk) = 0.
We require the following proposition for the necessary direction of Proposition 2.
As stated previously, the argument is due to Dumas [10, Th´eor`eme 30]. We state
the result here in a slightly diﬀerent form.

Proposition 17 (Dumas). Let Γ(z) be a polynomial with Γ(0) = 1. If all of the
zeros of Γ(z) are roots of unity of order not coprime to k, then H(z) = j⩾0 Γ(zkj )
−1

is k-regular.

To prove Proposition 17, Dumas proved that the functions

Λrn · · · Λr1
 n−1

j=0 Γ(zkj )−1 ,

for n ⩾ 1, have only ﬁnitely many poles with bounded multiplicities and then applied
Lemma 16; see also [9, Theorem 10]. Compare with Lemma 7.
For the suﬃcient direction of Proposition 2, we will use the following result.

Lemma 18. Let k ⩾ 2 be an integer, Q(z) be a polynomial and suppose that all of
the zeros of Q(z) are either zero or roots of unity of order not coprime to k. Then
for any integer m ⩾ 1, the zeros of Q(zkm ) are either zero or roots of unity of order
not coprime to k.
 PROOF OF BECKER’S CONJECTURE 15

Proof. Since all zeros of Q(z) are either zero or roots of unity, it is clear that all
zeros of Q(zkm) are either zero or roots of unity.
Now suppose to the contrary that there is a zero z = ζ of Q(zkm ) that is a root
of unity of order coprime to k, say ℓ. Then since gcd(k, ℓ) = 1, there is a positive
integer M dividing ϕ(ℓ) such that kM ≡ 1 (mod ℓ). Thus for this M , we have

(24) ζ kM = ζ.

Since z = ζ is a zero of Q(zkm), we have that z = ξ := ζ km is a zero of Q(z). But
then, using (24), we have z = ξ is a zero of Q(z) such that

ξ = ζ km = ζ kM km = ζ km kM = ξkM .

If we denote by n the order of ξ, this gives that kM ≡ 1 (mod n), so that we have
gcd(k, n) = 1, a contradiction, which proves the lemma. □

Proof of Proposition 2. We prove suﬃciency ﬁrst. Towards this, suppose that F (z)
is k-regular and satisﬁes the minimal functional equation (1). Following the com-
ments after Theorem 1, we denote by A the set of roots of unity ζ such that ζ kM ̸= ζ
for all M ⩾ 1 and a0(ζ) = 0; note that this condition is equivalent to the condition
that the order of ζ is not coprime to k. Then there is a nonnegative integer γ and
an N depending on a0(z) such that for

Q(z) :=
 ζ∈A
 N −1

j=0 (1 − zkj ζ kN )
νζ (a0),

the function F (z)/zγQ(z) satisﬁes a Mahler-type functional equation (1) with
a0(z) = 1. In particular, we write

F (z)
zγQ(z) +
 D

i=1 bi(z) · F (zki)
zγkiQ(zki) = 0.

Now multiplying by zγkD Q(z)Q(zk) · · · Q(zkd ) gives

(25) zγ(kD−1)Q(zk) · · · Q(zkD )F (z)

+
 D

i=1 bi(z)zγ(kD−ki) D
j=0 Q(zkj )

Q(zki) · F (zki) = 0.

By the deﬁnition of Q(z) and Lemma 18, we have that F (z) satisﬁes a (new)
functional equation (1), speciﬁcally Equation (25), such that all of the zeros of

a0(z) = zγ(kD−1)Q(zk) · · · Q(zkD )

are either zero or roots of unity of order not coprime to k. This proves necessity.
For suﬃciency, we use both Theorem 11 and Proposition 17. To this end, suppose
that F (z) satisﬁes some functional equation (1) such that all of the zeros of a0(z)
are either zero or roots of unity of order not coprime to k. Now write

a0(z) = ρzδΓ(z),

16 JASON P. BELL, FR´ED´ERIC CHYZAK, MICHAEL COONS, AND PHILIPPE DUMAS

where Γ(0) = 1. Thus all the zeros of Γ(z) are roots of unity of order not coprime
to k. Now, Theorem 11, gives that there is a k-regular series G(z) such that

F (z) = G(z)

j⩾0 Γ(zkj ) .

Applying Proposition 17 gives that the function

H(z) := 1

j⩾0 Γ(zkj )

is k-regular. Since k-regular series form a ring, we have that F (z) = G(z)H(z) is
k-regular. This proves suﬃciency, and completes the proof of the proposition. □

References

1. B. Adamczewski and J. P. Bell, A problem about mahler functions, Ann. Sc. Norm. Super.
Pisa, to appear.
2. B. Adamczewski and C. Faverjon, M´ethode de Mahler: relations lin´eaires, transcendance et
applications aux nombres automatiques, Proc. Lond. Math. Soc. (3) 115 (2017), no. 1, 55–90.
MR 3669933
3. J.-P. Allouche and J. Shallit, The ring of k-regular sequences, Theoret. Comput. Sci. 98 (1992),
no. 2, 163–197. MR 1166363
4. P.-G. Becker, k-regular power series and Mahler-type functional equations, J. Number Theory
49 (1994), no. 3, 269–286. MR 1307967
5. J. P. Bell and M. Coons, Transcendence tests for Mahler functions, Proc. Amer. Math. Soc.
145 (2017), no. 3, 1061–1070. MR 3589306
6. R. P. Brent, M. Coons, and W. Zudilin, Algebraic independence of Mahler functions via radial
asymptotics, Int. Math. Res. Not. IMRN (2016), no. 2, 571–603. MR 3493426
7. P. Bundschuh and K. V¨a¨an¨anen, Guided by Schwarz’ functions: a walk through the garden of
Mahler’s transcendence method, From arithmetic to zeta-functions, Springer, [Cham], 2016,
pp. 91–101. MR 3642351
8. M. Coons, Zero order estimates for Mahler functions, New Zealand J. Math. 46 (2016), 83–88.
MR 3576022
9. Ph. Dumas, Algebraic aspects of B-regular series, Automata, languages and programming
(Lund, 1993), Lecture Notes in Comput. Sci., vol. 700, Springer, Berlin, 1993, pp. 457–468.
MR 1252426
10. , R´ecurrences mahl´eriennes, suites automatiques, ´etudes asymptotiques, Institut Na-
tional de Recherche en Informatique et en Automatique (INRIA), Rocquencourt, 1993, Th`ese,
Universit´e de Bordeaux I, Talence, 1993. MR 1346304
11. A. Goto and T. Tanaka, Algebraic independence of the values of functions satisfying Mahler
type functional equations under the transformation represented by a power relatively prime to
the characteristic of the base ﬁeld, J. Number Theory 184 (2018), 384–410. MR 3724170
12. T. Kisielewski, Criteria for regularity of Mahler power series and Becker’s conjecture, J.
Number Theory 174 (2017), 456–486. MR 3597403
13. J. H. Loxton and A. J. van der Poorten, Arithmetic properties of the solutions of a class of
functional equations, J. Reine Angew. Math. 330 (1982), 159–172. MR 641817
14. , Arithmetic properties of automata: regular sequences, J. Reine Angew. Math. 392
(1988), 57–69. MR 965057
15. K. Nishioka, New approach in Mahler’s method, J. Reine Angew. Math. 407 (1990), 202–219.
MR 1048535
16. , Mahler functions and transcendence, Lecture Notes in Mathematics, vol. 1631,
Springer-Verlag, Berlin, 1996. MR 1439966
17. P. Philippon, Groupes de Galois et nombres automatiques, J. Lond. Math. Soc. (2) 92 (2015),
no. 3, 596–614. MR 3431652
18. J. Roques, On the reduction modulo p of Mahler equations, Tohoku Math. J. (2) 69 (2017),
no. 1, 55–65. MR 3640014
19. , On the algebraic relations between Mahler functions, Trans. Amer. Math. Soc. 370
(2018), no. 1, 321–355. MR 3717982

PROOF OF BECKER’S CONJECTURE 17

Department of Pure Mathematics, University of Waterloo, Canada
Email address: jpbell@uwaterloo.ca

INRIA, Universit´e Paris–Saclay, France
Email address: Frederic.Chyzak,Philippe.Dumas@inria.fr

School of Mathematical and Physical Sciences, University of Newcastle, Australia
Email address: Michael.Coons@newcastle.edu.au
