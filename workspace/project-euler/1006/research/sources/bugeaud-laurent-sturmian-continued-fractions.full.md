<!-- source: https://hal.science/hal-03571109v1/preview/Arxiv_Bu_La.pdf | converted from PDF -->

HAL Id: hal-03571109

https://hal.science/hal-03571109v1

Submitted on 13 Feb 2022

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

HAL Authorization

Combinatorial structure of Sturmian words and continued
fraction expansions of Sturmian numbers

Yann Bugeaud, Michel Laurent

To cite this version:

Yann Bugeaud, Michel Laurent. Combinatorial structure of Sturmian words and continued fraction expan-
sions of Sturmian numbers. Annales de l’Institut Fourier, 2023, 73 (5), pp.2029-2078. ⟨10.5082/aif.3561⟩. ⟨hal-
03571109⟩arXiv:2104.09239v1  [math.NT]  19 Apr 2021
Combinatorial structure of Sturmian words
and continued fraction expansions of Sturmian numbers

YANN BUGEAUD and MICHEL LAURENT

Abstract. Let θ = [0; a1, a2, . . .] be the continued fraction expansion
of an irrational real number θ ∈ (0, 1). It is well-known that the charac-
teristic Sturmian word of slope θ is the limit of a sequence of ﬁnite words
(Mk)k≥0, with Mk of length qk (the denominator of the k-th convergent
to θ) being a suitable concatenation of ak copies of Mk−1 and one copy
of Mk−2. Our ﬁrst result extends this to any Sturmian word. Let b ≥ 2
be an integer. Our second result gives the continued fraction expansion
of any real number ξ whose b-ary expansion is a Sturmian word s over
the alphabet {0, b − 1}. This extends a classical result of B¨ohmer who
considered only the case where s is characteristic. As a consequence, we
obtain a formula for the irrationality exponent of ξ in terms of the slope
and the intercept of s.
 1. Introduction

Sturmian words are inﬁnite words over a two letters alphabet that have exactly n + 1
factors of length n for every n ≥ 1. They are the non-ultimately periodic words which are
closest to ultimately periodic words. They admit several equivalent deﬁnitions and appear
in many diﬀerent areas of mathematics, including combinatorics, number theory, and dy-
namical systems; good references include Chapter 2 of [22], [5], and [7]. The arithmetic
description of Sturmian words is as follows. Throughout this paper, we let ⌊x⌋ (resp., ⌈x⌉)
denote the largest (resp., smallest) integer less than or equal (resp., greater than or equal)
to the real number x.
Let θ and ρ be real numbers with 0 ≤ θ, ρ < 1 and θ irrational. For n ≥ 1, set

sn := sn(θ, ρ) = ⌊
nθ + ρ⌋ − ⌊
(n − 1)θ + ρ⌋
, s′
n := s′
n(θ, ρ) = ⌈
nθ + ρ⌉ − ⌈
(n − 1)θ + ρ⌉
.

Then, the inﬁnite words
 sθ,ρ := s1s2s3 . . . , s
′
θ,ρ := s′
1s′
2s′
3 . . .

2010 Mathematics Subject Classiﬁcation : 11J70, 11J82, 68R15. Keywords:
Combinatorics on words, Sturmian word, Continued fraction expansion, Ostrowski numer-
ation, Irrationality exponent.
 1

are, respectively, the lower and upper Sturmian words of slope θ and intercept ρ, written
over the alphabet {0, 1}. Observe that sθ,0 and s
′
θ,0 diﬀer only by their ﬁrst letter, thus,
there exists an inﬁnite word cθ, called the characteristic Sturmian word of slope θ, such
that sθ,0 = 0cθ, s
′
θ,0 = 1cθ.

Explicitly, we have cθ = sθ,θ = s
′
θ,θ = c1c2c3 . . . ,

with cn = ⌊(n + 1)θ⌋ − ⌊nθ⌋ = ⌈(n + 1)θ⌉ − ⌈nθ⌉, for n ≥ 1.

Alternatively, the characteristic word cθ = sθ,θ = s
′
θ,θ can be deﬁned as follows. Let
[0; a1, a2, . . .] denote the continued fraction expansion of the slope θ, with partial quotients
a1, a2, . . . and convergents pk/qk = [0; a1, . . . , ak] for k ≥ 1. Let (Mk)k≥0 be the sequence
of ﬁnite words over the alphabet {a, b} associated with (aj)j≥1 deﬁned by

M0 = a, M1 = aa1−1b, Mk = (Mk−1)ak Mk−2, for k ≥ 2.

Then, the limit limk→+∞ Mk exists: it is the characteristic Sturmian word of slope θ over
{a, b}. Replacing a by 0 and b by 1, we get

cθ = lim
k→+∞ Mk. (1.1)

Furthermore, the length (that is, the number of letters) of Mk is equal to qk for k ≥ 1.
Our ﬁrst result, stated as Theorem 2.1, extends (1.1) by showing how an arbitrary
Sturmian word of slope θ and intercept ρ can be expressed as the limit of a sequence of
ﬁnite words (Vk)k≥0, with Vk (of length qk) being a suitable concatenation of ak copies of
Vk−1 and one copy of Vk−2, deﬁned in terms of the θ-Ostrowski expansion of the intercept
ρ. Then, we will consider some Diophantine properties of the real numbers whose se-
quence of digits in some given integer base b form a Sturmian word. Such real numbers
are called b-Sturmian numbers, or shortly Sturmian numbers, when we do not need to re-
fer to the base. The transcendence of characteristic Sturmian numbers was established by
B¨ohmer [10] in 1927, assuming that the sequence of partial quotients (ak)k≥1 is unbounded.
He also gave explicitly their continued fraction expansion; see Theorem 2.2 below. This has
been rediscovered by Danilov [15], Davison [16], and by Adams and Davison [6] (see also
[2], Theorem 7.22 in [12], and Section 9.3 of [5] for a special case). Ferenczi and Mauduit
[17] used combinatorial properties of Sturmian words and a deep result from Diophantine
approximation (Ridout’s theorem, which is a p-adic extension of Roth’s theorem) to es-
tablish that Sturmian numbers are transcendental. Speciﬁcally, they proved that every
Sturmian word contains, for some positive ε, inﬁnitely many (2 + ε)-powers of blocks (that
is, a block followed by itself and by a preﬁx of it of relative length at least ε) occurring
not too far from its beginning.
Subsequently, Berth´e, Holton and Zamboni [8] established that any Sturmian word,
whose slope has a bounded continued fraction expansion, has inﬁnitely many preﬁxes which

2

are (2 + ε)-powers of blocks, for some positive real number ε depending only on the word.
This implies that the associated Sturmian number ξ is rather close to rational numbers
whose b-ary expansion is purely periodic and gives that the irrationality exponent of ξ is
at least equal to 2 + ε.

Deﬁnition 1.1. The irrationality exponent µ(ζ) of an irrational real number ζ is the
supremum of the real numbers µ such that the inequality
∣
∣
∣
∣ζ − p
q
 ∣
∣
∣
∣ < 1
qµ

has inﬁnitely many solutions in rational numbers p
q . If µ(ζ) is inﬁnite, then ζ is called a
Liouville number.

Recall that the irrationality exponent of an irrational number ζ is always at least equal
to 2, with equality for almost all ζ, in the sense of the Lebesgue measure. As observed in [1]
(see also Section 8.5 of [12]), it follows from the results of [8] and [4] that the irrationality
exponent of any Sturmian number exceeds 2. Further progress has been made recently
in [13], where it is proved that the irrationality exponent of a b-Sturmian number can be
read on its b-ary expansion. This is equivalent to say that, among the very good rational
approximants to a b-Sturmian number, inﬁnitely many of them can be constructed by
cutting its b-ary expansion and completing by periodicity.
Furthermore, Theorem 4.3 of [13] asserts that the irrationality exponent of a Sturmian
number is at least equal to 5
3 + 4√
10
15 = 2.5099 . . ., and that equality occurs in some cases.
This result is obtained by means of a careful analysis of the repetitions occurring near the
beginning of a given Sturmian word.
Our second main result, stated as Theorem 2.3, extends B¨ohmer’s result and gives
explicitly the continued fraction expansion of any b-Sturmian number over the alphabet
{0, b − 1}. From this we deduce in Theorem 2.4 an exact formula giving its irrationality
exponent. Our approach also allows us to improve the best known transcendence measures
for Sturmian numbers, see Theorem 2.7.

2. Results

Before stating our ﬁrst result, we brieﬂy recall the deﬁnition of the Ostrowski numer-
ation system; see e.g. Proposition 2 of [9]. We keep the notation from Section 1. Set
q0 = 1 and θk = qkθ − pk for k ≥ 0. Note that θk < 0 if and only if k is odd. Let σ be an
arbitrary number in the interval [−θ, 1 − θ]. Then σ can be written as

σ = ∑

k≥1 bkθk−1,

where 0 ≤ b1 ≤ a1 − 1, 0 ≤ bk ≤ ak for k ≥ 2, and bk = 0 if bk+1 = ak+1 (these are the
so-called Ostrowski numeration rules). Assume that σ does not belong to Zθ + Z, or that
σ belongs to Z≥0θ + Z. Then, we can moreover ensure that there are inﬁnitely many odd
(resp., even) integers k such that bk < ak. The latter condition guarantees the unicity
of the representation which is called the Ostrowski expansion of σ. When σ belongs to
Z≥0θ + Z, the digits bk vanish for large k.
 3

Theorem 2.1. Let θ and ρ be real numbers with 0 ≤ θ, ρ < 1 and θ irrational. Assume
that ρ does not belong to Zθ + Z, or that ρ belongs to Z≥1θ + Z. Then sθ,ρ = s
′
θ,ρ. Let

ρ − θ = ∑

h≥1 bhθh−1

be the Ostrowski expansion of ρ − θ in base θ. Deﬁne the words V−1, V0, V1, . . . by V−1 = 1,
V0 = 0, V1 = 0a1−b1−110b1 , and

Vk+1 = V ak+1−bk+1
k Vk−1V bk+1
k , k ≥ 1.

Then, the sequence (Vk)k≥0 converges and

sθ,ρ = s
′
θ,ρ = lim
k→+∞ Vk.

Furthermore, setting

tk = b1 + b2q1 + · · · + bkqk−1 and rk = qk − tk,

and denoting by Tk (resp., Rk) the preﬁx (resp., suﬃx) of length tk (resp., rk) of Mk for
k ≥ 1, we have Vk = RkTk and Mk = TkRk, k ≥ 1.

A similar result holds in the remaining case where ρ − θ = −mθ + p for integers
m ≥ 1 and p. This case corresponds to the sequences which are ultimately equal to the
characteristic word cθ. Some technical diﬃculties occur, due to the fact that the choice of
the lower / upper integral part does matter; see Section 3 for a precise statement and its
proof.
Theorem 2.1 is a key tool for our extension of the following result of B¨ohmer [10].

Theorem 2.2 (B¨ohmer). For a positive real irrational number θ = [0; a1, a2, . . .] in (0, 1)
and an integer b ≥ 2, set
 ξb(θ) = (b − 1)
 +∞∑

j=1
 1
b⌊j/θ⌋ .

For k ≥ 1, let pk/qk denote the k-th convergent to θ and set

Ak := bqk − bqk−2

bqk−1 − 1 ,

where q−1 = 0 and q0 = 1. Then, we have

ξb(θ) = [0; A1, A2, A3, . . .]

and the irrationality exponent of ξb(θ) is given by

µ(ξb(θ)) = 1 + lim sup
k→+∞
 qk
qk−1 .

4

Note that Ak is an integer multiple of bqk−2 since qk − qk−2 is an integer multiple of
qk−1.
The last assertion of the theorem follows from the well-known fact that the irrationality
exponent of an irrational real number ζ = [A0; A1, A2, . . .] is given by

µ(ζ) = 1 + lim sup
j→+∞
 log Qj+1
log Qj ,

where [A0; A1, A2, . . . , Aj] = Pj/Qj, for j ≥ 1. Indeed, the sequence (Pj/Qj)j≥1 comprises
all the best rational approximations to ζ and we have

1
2Qj+1Qj < ∣
∣
∣
∣ζ − Pj
Qj
 ∣
∣
∣
∣ < 1
Qj+1Qj .

Theorem 2.2 describes the ﬁrst known class of real numbers having the property that
both their b-ary expansion (for some integer b ≥ 2) and their continued fraction expansion
are explicitly determined. There are only few such classes; see Section 7.6 of [12] for other
examples.
Our second main result extends B¨ohmer’s theorem to an arbitrary b-Sturmian number
with digits in {0, b − 1}. Deﬁne

ξb(θ, ρ) = (b − 1)
 +∞∑

n=1
 sn(θ, ρ)
bn , ξ′
b(θ, ρ) = (b − 1)
 +∞∑

n=1
 s′
n(θ, ρ)
bn .

Let ξ denote one of these numbers. Let (bk)k≥1 and (tk)k≥1 be the sequences of integers
deﬁned in Theorem 2.1 (or in Theorem 4.2 if ρ is of the form −mθ+p, with m, p nonnegative
integers) applied to the Sturmian sequence deﬁning ξ. Put t0 = 0 and r0 = 1. For k ≥ 0,
set
 ck = brk+qk−1 b(ak+1−bk+1−1)qk − 1
bqk − 1 , dk = btk − 1,

ek = brk − 1, fk = btk bbk+1qk − 1
bqk − 1 .

We point out that some elements of these four sequences may not be positive integers. For
example, fk is equal to 0 when bk+1 = 0 and ck+1 is equal to 0 when ak+2 = bk+2 + 1.
More intriguing is the case where ak+2 = bk+2. Then, we have bk+1 = 0, thus rk + qk+1 =
rk+1 + qk and

ck+1 = brk+1+qk b−qk+1 − 1
bqk+1 − 1 = brk − brk+qk+1

bqk+1 − 1 = −brk = −ek − 1

is a negative integer. Keeping this in mind, and with some abuse of language, the next
theorem asserts that [0; c0, d0, 1, e0, f0, c1, d1, 1, e1, f1, c2, . . .]

is an (improper) continued fraction expansion of ξ. The precise statement is as follows.

5

Theorem 2.3. Let ξ be as above and keep the notation introduced above. If ak − bk ≥ 2
and bk ≥ 1 for every k ≥ 1, then the continued fraction expansion of ξ is given by

ξb(θ, ρ) = [0; c0 + 1, e0, f0, c1, d1, 1, e1, f1, c2, . . .].

Otherwise, let A1, A2, A3, . . . be the sequence of positive integers obtained from the se-
quence c0, d0, 1, e0, f0, c1, d1, 1, e1, f1, c2, . . . after the application of the following rules:

(i) For every k such that ck+1 < 0, replace the nine integers ck, dk, 1, ek, fk, ck+1, dk+1,

1, ek+1 by the positive integer ck + 1 + ek+1;

(ii) Replace any three consecutive elements of this new sequence of the form x, 0, y

by the integer x + y.

Then, the continued fraction expansion of ξ is given by

ξb(θ, ρ) = [0; A1, A2, A3, . . .].

Observe that the sequence (Aj)j≥1 is well-deﬁned. Indeed, ck and ck+1 cannot be
both negative, since we cannot have simultaneously ak+2 = bk+2 and ak+1 = bk+1.
Let us brieﬂy show that Theorem 2.3 includes B¨ohmer’s result. First, note that
ξb(θ) = ξb(θ, θ), since, for a positive integer j, we have ⌊j/θ⌋ equals the integer ℓ if and
only if ℓ < j/θ < ℓ + 1, that is, if and only if, ⌊(ℓ + 1)θ⌋ − ⌊ℓθ⌋ = 1. Then, observe that
the Ostrowski expansion of θ − θ = 0 in base θ is given by the constant sequence equal to
0. Consequently, the sequences deﬁned in Theorem 2.3 are equal to

dk = fk = 0, ek = bqk − 1, ck = bqk+qk−1 b(ak+1−1)qk − 1
bqk − 1 , k ≥ 0.

It then follows from Theorem 2.3 that

ξb(θ) =
[0; bq0+0 b(a1−1)q0 − 1
bq0 − 1 , 0, 1, bq0 − 1, 0, bq1+q0 b(a2−1)q1 − 1
bq1 − 1 , 0, 1, bq1 − 1, 0, c2, . . .
]

=
[0; bq0+0 b(a1−1)q0 − 1
bq0 − 1 + 1, bq0 − 1 + bq1+q0 b(a2−1)q1 − 1
bq1 − 1 + 1, bq1 − 1, 0, c2, . . .
]

=
[0; ba1q0 − 1
bq0 − 1 , bq2 − bq0

bq1 − 1 , bq1 − 1, 0, c2, . . .
]

=
[0; bq1 − 1
bq0 − 1 , bq2 − bq0

bq1 − 1 , bq3 − bq1

bq2 − 1 , . . .
].

We get the sequence of partial quotients c0 + 1, e0 + c1 + 1, e1 + c2 + 1, . . . and we recover
Theorem 2.2.
Theorem 2.3 is proved in Section 7, where we give additional informations on the
shape of the convergents to ξ and its partial quotients; see Proposition 7.2.

6

As a consequence of Theorem 2.3, we obtain an expression for the irrationality expo-
nent of any Sturmian number in terms of its slope and its intercept.
Keep our notation and deﬁne

νk(1) = 2 + tk
rk+1 , νk(2) = 2 + rk
rk+1 + tk ,

νk(3) = 1 + qk+1
rk+1 + qk , νk(4) = 1 + rk+2
qk+1 .

Put ν(1) = lim sup
k→+∞ {νk(1) : ak+1 − bk+1 ≥ 1 and ak+2 − bk+2 ≥ 1},

ν(2) = lim sup
k→+∞ {νk(2) : ak+2 − bk+2 ≥ 1},

and, for j = 3, 4, ν(j) = lim sup
k→+∞ νk(j).

Theorem 2.4. Let ξ be as above. Then, its irrationality exponent is equal to

max{ν(1), ν(2), ν(3), ν(4)}.

We recover, for the initial repetitions, the formulas found in [8] for the critical initial
exponent, namely the contributions of ν(2) and ν(4). Theorem 2.4 is established at the
end of Section 6; see Theorem 6.3.
Furthermore, we derive easily a necessary and suﬃcient condition under which a Stur-
mian number is a Liouville number, thereby reproving the ﬁrst part of Th´eor`eme 3.1 of [4]
(see also [19]).

Corollary 2.5. A Sturmian number is a Liouville number if and only if its slope has
unbounded partial quotients in its continued fraction expansion.

Theorem 2.4 allows us to study in depth the irrationality exponents of Sturmian
numbers. For instance, we can ﬁx a slope θ and consider the spectrum L(θ) consisting of
the set the irrationality exponents of Sturmian numbers of slope θ.

Theorem 2.6. Let θ be an irrational number in (0, 1) with bounded partial quotients.
Then,
 L(θ) ⊂ [ 5
3 + 4√10
15 , 1 + µ(ξb(θ))]

and there exists an intercept ρ(θ) such that

µ(ξb(θ, ρ(θ))) = 1 + µ(ξb(θ)).

A detailed study of the sets L(θ) will be the purpose of a forthcoming work.

7

Theorem 2.3 allows us also to improve the best known transcendence measures for
Sturmian numbers. Let ζ be a transcendental real number. Following Koksma [18], for
any integer d ≥ 1, we denote by w∗
d(ζ) the supremum of the exponents w for which

0 < |ζ − α| < H(α)−w−1

has inﬁnitely many solutions in real algebraic numbers α of degree at most d. Here, H(α)
stands for the na¨ıve height of the minimal deﬁning polynomial of α over Z. Clearly, the
functions µ − 1 and w∗
1 are equal and the functions w∗
d are invariant by rational translation
and by multiplication by a nonzero rational number, for d ≥ 1. We direct the reader to [11]
for classical results on the functions w∗
d and on Mahler’s and Koksma’s classiﬁcations of
real numbers. As a particular case of Th´eor`eme 1.1 of [4], we know that, for any Sturmian
number ξ which is not a Liouville number, there exists a positive real number c, depending
only on ξ, such that w∗
d(ξ) ≤ (2d)c(log 3d)(log log 3d), d ≥ 1.

This can be improved as follows.

Theorem 2.7. Let ξ be a Sturmian number. Assume that the partial quotients of its
slope are ultimately bounded from above by M . Then, there exists a positive real number
κ, depending only on M , such that

w∗
d(ξ) ≤ (2d)κ(log log 3d), d ≥ 1.

We point out that the transcendence measure obtained in Theorem 2.7 does not
depend on the intercept of the Sturmian number.
We believe that Theorem 2.1 will have many applications. We will use it in a follow-up
work devoted to the transcendence of Hecke–Mahler series evaluated at algebraic points.
We refer to [14, 20, 21] for various applications of Sturmian numbers to the dynamics of
piecewise aﬃne maps.
The present paper is organized as follows. We show in Section 3 that any Sturmian
word s of slope θ and intercept ρ can be expressed in a similar way as in (1.1) and we
deﬁne its formal intercept. The link between the formal intercept and the expansion of
the intercept ρ in the θ-Ostrowski numeration system is established in Section 4, thereby
proving Theorem 2.1. In Section 5, we apply Theorem 2.1 to give a precise description
of the repetitions occurring near the beginning of s. From this, in the next section, we
deduce four one-parametric families of rational numbers which approximate very well the
Sturmian number ξ associated to s, the exact rate of approximation to ξ by these rational
numbers being given in Theorem 6.1. We derive the continued fraction expansion of ξ
in Section 7, thereby proving Theorems 2.4 and 2.5, since we see that all the very good
approximants to ξ belong to one of the four families deﬁned in Section 6. The ﬁnal Section
is devoted to the proofs of the other results stated in Section 2.

3. The formal intercept of a Sturmian word

We keep the notation of Section 1 with the alphabet {0, 1}. Let s be an arbitrary
Sturmian word of slope θ. The goal of this section is to establish that any Sturmian word

8

can be expressed as in (1.1), that is, as the limit of a suitable sequence (Vk)k≥1 of binary
words Vk of length qk constructed inductively.
Throughout, the length |W | of a ﬁnite word W , that is, the number of letters com-
posing W , is denoted by |W |. If W has at least one letter (resp., at least two letters),
then W − (resp., W −−) denotes the work W deprived of its last letter (resp., its last two
letters).

Deﬁnition 3.1. A word V is a conjugate of Mk if there exist words T and R such that

V = RT and Mk = T R,

with 0 ≤ t := |T | < qk. Then, R is the non-empty suﬃx of Mk of length qk − t.

Observe that the qk conjugates V of the word Mk are distinct. We label these trans-
lated words V by the length t, 0 ≤ t < qk of the (possibly empty) preﬁx T in the decom-
position Mk = T R, V = RT . The whole set of conjugates V of Mk is clearly obtained as
the set of factors of length qk in the word MkM −
k . Each such factor V is determined by
its qk − 1 ﬁrst letters which form the qk distinct factors of length qk − 1 contained in the
word MkM −−
k .
As an example, for k = 1, we have M1 = 0a1−11. Any conjugate V of M1 can be
written in the form

V = 0a1−1−b1 10b1 = RT, M1 = T R, with T = 0b1 , R = 0a1−1−b1 1,

for some integer b1 with 0 ≤ b1 ≤ a1 − 1. Thus, in this case, we have t = b1.

Deﬁnition 3.2. For each k ≥ 1, let Vk be the conjugate of Mk whose ﬁrst qk − 1 letters
coincide with those of s. Let Tk and Rk be the words such that

Vk = RkTk and Mk = TkRk,

with Rk non-empty. Denote by tk the length of Tk. Put R−1 = 1, R0 = 0, and let T−1
and T0 be the empty word.

Then, the following recursion formulae hold. The notion of formal intercept was ﬁrst
introduced by Wojcik [23], but our presentation is diﬀerent.

Lemma 3.3 (formal intercept). Put t1 = b∗
1. For any k ≥ 1, there exists an integer
b∗
k+1 such that 0 ≤ b∗
k+1 ≤ ak+1 and

tk+1 = tk + b∗
k+1qk.

When b∗
k+1 = ak+1, we necessarily have tk < qk−1, so that b∗
k = 0 and tk = tk−1 in this
case. Moreover, the sequences of words (Tk)k≥0 and (Rk)k≥0 satisfy the recursion formulae

Tk+1 = M b
∗
k+1
k Tk = TkV b
∗
k+1
k

9

and
 Rk+1 =
 { RkM ak+1−b
∗
k+1−1
k Mk−1 if b∗
k+1 < ak+1,
Rk−1 if b∗
k+1 = ak+1,

for k ≥ 0. The sequence (b∗
k)k≥1 is called the formal intercept of s.

Proof. The word Vk+1 is a factor of the word Mk+1M −
k+1 beginning somewhere on the ﬁrst
factor Mk+1. Assume ﬁrst that Vk+1 begins on the preﬁx M ak+1
k of Mk+1 = M ak+1
k Mk−1
and let P be the preﬁx of length qk of Vk+1. Thus, for some integer 0 ≤ b∗
k+1 < ak+1, the

preﬁx P begins on the second factor Mk in the product M ak+1
k = M b
∗
k+1
k MkM ak+1−b
∗
k+1−1
k .
Then, P is a factor of

MkM ak+1−b
∗
k+1−1
k M −
k+1 = MkM 2ak+1−b
∗
k+1−1
k M −
k−1

beginning on the ﬁrst factor Mk. Since 2ak+1 − b∗
k+1 − 1 ≥ 1, we see that P is located

over the product MkM −
k , where M −
k is the preﬁx of M 2ak+1−b
∗
k+1−1
k of length qk − 1. As
the ﬁrst qk − 1 letters of P coincide with those of s, we deduce that P = Vk = RkTk, and
next that Tk+1 = M b
∗
k+1
k Tk and Rk+1 = RkM ak+1−b
∗
k+1−1
k Mk−1.

Note ﬁnally that
 M b
∗
k+1
k Tk = (TkRk)b
∗
k+1Tk = Tk(RkTk)b
∗
k+1 = TkV b
∗
k+1
k .

Suppose now that Vk+1 begins on the second factor Mk−1 in

Mk+1M −
k+1 = M ak+1
k Mk−1M −
k+1 = M ak+1
k Tk−1Rk−1M −
k+1

and put b∗
k+1 = ak+1. Then,

Tk+1 = M ak+1
k Tk−1 and Rk+1 = Rk−1,

observing that Vk−1 = Rk−1Tk−1 equals the preﬁx of Vk+1 of length qk−1. Notice now that
Mk is a preﬁx of Mk−1M −
k+1. Writing

Mk−1M −
k+1 = Mk · · · = Tk−1Rk−1M ak−1
k−1 Mk−2 · · ·

we see that Tk = Tk−1 and Rk = Rk−1M ak−1
k−1 Mk−2. Thus b∗
k = 0 by the preceding case
applied to the level k − 1.

We now deal with binary recursions expressing Vk+1 in terms of Vk and Vk−1 extending
the classical formulae Mk+1 = M ak+1
k Mk−1. Set V−1 = R−1T−1 = 1 and V0 = R0T0 = 0.

10

Lemma 3.4 (binary recursion). We have the relation V1 = V a1−1−b
∗
1
0 V−1V b
∗
1
0 , while for
any k ≥ 1, we have Vk+1 = V ak+1−b
∗
k+1
k Vk−1V b
∗
k+1
k .

Proof. The expression V1 = 0a1−1−b
∗
1 10b
∗
1

yields obviously the relation for V1.
For k ≥ 1, we distinguish two cases, either b∗
k+1 < ak+1 or b∗
k+1 = ak+1. Assume ﬁrst
that b∗
k+1 < ak+1. According to Lemma 3.3, we write Vk+1 = Rk+1Tk+1 with

Rk+1 = RkM ak+1−b
∗
k+1−1
k Mk−1 = Rk(TkRk)ak+1−b
∗
k+1−1Tk−1Rk−1

= (RkTk)ak+1−b
∗
k+1−1RkTk−1Rk−1 = V ak+1−b
∗
k+1−1
k RkTk−1Rk−1

and Tk+1 = TkV b
∗
k+1
k .

Thus Vk+1 = V ak+1−b
∗
k+1−1
k RkTk−1Rk−1TkV b
∗
k+1
k .

Since
RkTk−1Rk−1Tk = RkTk−1Rk−1Tk−1(Rk−1Tk−1)b
∗
k = RkTkRk−1Tk−1 = VkVk−1,

we get Vk+1 = V ak+1−b
∗
k+1
k Vk−1V b
∗
k+1
k .

Assume now that b∗
k+1 = ak+1. Then b∗
k = 0. From Lemma 3.3, we know that
Tk = Tk−1 and that

Tk+1 = TkV b
∗
k+1
k = Tk−1V b
∗
k+1
k and Rk+1 = Rk−1.

Thus Vk+1 = Rk+1Tk+1 = Rk−1Tk−1V b
∗
k+1
k = Vk−1V b
∗
k+1
k ,

as asserted.

We conclude this section with a corollary, which shows how any preﬁx of Mn+1 can
be expressed in terms of M0, . . . , Mn.
Recall that the Ostrowski numeration system in base θ is deﬁned as follows: every
positive integer N can be uniquely written in the form

N = d1 + d2q1 + . . . + dr+1qr,

where 0 ≤ dj ≤ aj for j = 1, . . . , r + 1, dr+1 > 0, d1 < a1 and dj = 0 if dj+1 = aj+1.

11

Corollary 3.5 (product formula for preﬁxes). Let T be the preﬁx of Mn+1 of length
t < qn+1. Write t = d1 + d2q1 + · · · + dn+1qn

where d1, . . . , dn+1 are the digits of the integer t in the Ostrowski numeration system in
base θ. Then, we have the product formula

T = M dn+1
n M dn
n−1 · · · M d1
0 = V d1
0 V d2
1 · · · V dn+1
n ,

where the words V0, . . . , Vn are deﬁned recursively by the formulae

V0 = 1, V1 = 0a1−d1−110d1 , Vk+1 = V ak+1−dk+1
k Vk−1V dk
k , 1 ≤ k < n.

Proof. By Lemma 3.3, we have T = Tn+1 and t = tn+1. The recurrence relations

Tk+1 = M dk+1
k Tk = TkV dk+1
k

yield inductively the product formula

T = Tn+1 = M dn+1
n M dn
n−1 · · · M d1
0 = V d1
0 V d2
1 · · · V dn+1
n .

This establishes the corollary.

4. Linking formal intercept and Ostrowski numeration

We link the formal intercept, that is the sequence (b∗
k)k≥1 such that

tk = b∗
1 + b∗
2q1 + · · · + b∗
kqk−1, k ≥ 1,

to the intercept ρ thanks to the

Proposition 4.1. Let 0 < ρ < 1 be a real number either not belonging to Zθ + Z, or of
the form Z≥1θ + Z. Let ρ − θ = ∑

h≥1 bhθh−1

be the Ostrowski expansion of ρ − θ in base θ. For every k ≥ 1, put

tk = b1 + b2q1 + · · · + bkqk−1.

Then, tk is the length of the word Tk associated to the Sturmian word sθ,ρ = s
′
θ,ρ. In other
words, we have bk = b∗
k for k ≥ 1, meaning that the formal intercept of this Sturmian word
coincides with the sequence of digits of the number ρ − θ in its Ostrowski expansion in
base θ.

Proof. By deﬁnition, we have

sn = ⌊nθ + ρ⌋ − ⌊(n − 1)θ + ρ⌋, n ≥ 1,

12

and s′
n = ⌈nθ + ρ⌉ − ⌈(n − 1)θ + ρ⌉, n ≥ 1,

while the n-th letter of cθ is

cn = ⌊(n + 1)θ⌋ − ⌊nθ⌋ = ⌈(n + 1)θ⌉ − ⌈nθ⌉, n ≥ 1.

Thus

sn = ⌊(n + 1)θ + ρ − θ⌋ − ⌊nθ + ρ − θ⌋ = ⌊(n + 1 + tk)θ + σk⌋ − ⌊(n + tk)θ + σk⌋,

and
s′
n = ⌈(n + 1)θ + ρ − θ⌉ − ⌈nθ + ρ − θ⌉ = ⌈(n + 1 + tk)θ + σk⌉ − ⌈(n + tk)θ + σk⌉,

where we have set σk = ∑

h≥k bh+1θh.

We claim that ⌊qθ + σk⌋ = ⌊qθ⌋ and ⌈qθ + σk⌉ = ⌈qθ⌉

for every integer q with 1 ≤ q ≤ qk + tk. This yields that

sn = ⌊(n + 1 + tk)θ + σk⌋ − ⌊(n + tk)θ + σk⌋ = ⌊(n + 1 + tk)θ⌋ − ⌊(n + tk)θ⌋ = cn+tk

and

s′
n = ⌈(n + 1 + tk)θ + σk⌉ − ⌈(n + tk)θ + σk⌉ = ⌈(n + 1 + tk)θ⌉ − ⌈(n + tk)θ⌉ = cn+tk

for every 1 ≤ n ≤ qk − 1, and will establish the proposition, noting that MkMk is a preﬁx
of cθ.
To that purpose, we bound |σk|. Observe that θk is positive when k is even and
negative when k is odd. Moreover bh+1 ≤ ah+1 for any h ≥ 1, while b1 ≤ a1 − 1. Thus,

|σk| < max(|ak+1θk + ak+3θk+2 + · · · |, |ak+2θk+1 + ak+4θk+3 + · · · |)

= max(|θk−1|, |θk|) = |θk−1|,

noting that

ak+1θk + ak+3θk+2 + · · · = lim
n→∞
(
(
 n∑

h=0 ak+2h+1qk+2h)θ − (
 n∑

h=0 ak+2h+1pk+2h))

= lim
n→∞
( n∑

h=0
(qk+2h+1 − qk+2h−1)θ −
 n∑

h=0
(pk+2h+1 − pk+2h−1))

= lim
n→∞
 ((qk+2n+1 − qk−1)θ − (pk+2n+1 − pk−1)) = −θk−1.

13

The inequality |σk| < |θk−1| is strict because either ρ − θ does not belong to Zθ + Z, or
ρ − θ belong to Z≥0θ + Z, so that the sequence of digits (bh)h≥1 cannot be ultimately of
the form ak+1, 0, ak+3, 0 . . ..
Observe now that

|σk − bk+1θk| < ak+2|θk+1| + ak+4|θk+3| + · · · = |θk|.

It follows that σk and θk share the same sign when bk+1 ≥ 1 and that |σk| < |θk| when
bk+1 = 0. In particular, the stronger inequality |σk| < |θk| holds when θk and σk have
opposite signs.
The upper bound |σk| < |θk−1| can also be sharpened when tk ≥ qk−1. Indeed in this
case we have bk ≥ 1 and thus bk+1 cannot be equal to ak+1 by Ostrowski’s numeration
rules. We now bound bk+1 ≤ ak+1 − 1 to obtain

|σk| < |θk−1| − |θk|. (4.1)

Denote by ∥x∥ the distance from the real number x to the closest integer. We now
show that ∥qθ∥ is larger than |σk| when q diﬀers from qk, so that qθ and qθ + σk belong to
the same integer open interval of length 1 and have thus the same upper and lower integer
parts. We distinguish three cases. If q < qk, then

∥qθ∥ ≥ |θk−1| > |σk|,

as required. Assume secondly that tk < qk−1 and q = qk + v for some 1 ≤ v ≤ tk. Then

∥qθ∥ = ∥vθ + θk∥ ≥ ∥vθ∥ − |θk| ≥ |θk−2| − |θk| = |θk−2 − θk| ≥ |θk−1| > |σk|.

Thirdly, assume tk ≥ qk−1 and q = qk + v with 1 ≤ v ≤ qk − 1. Then,

∥qθ∥ ≥ ∥vθ∥ − |θk| ≥ |θk−1| − |θk| > |σk|,

by (4.1).
These three cases cover all the values of q with 1 ≤ q ≤ qk + tk, except q = qk, which
we consider now. We have ∥qkθ∥ = |θk|. When θk and σk share the same sign, we have

|θk| < |θk + σk| = |θk| + |σk| ≤ |θk| + |θk−1| < 1.

Thus, qkθ and qkθ + σk both belong either to (pk, pk + 1) or to (pk − 1, pk). When θk
and σk have opposite signs, we know that |σk| < |θk|, so that θk and θk + σk have the
same sign and both have absolute value less than 1. The claim is proved, which yields the
proposition.

A similar result holds in the remaining case where ρ − θ = −mθ + p for integers m ≥ 1
and p. Assume ﬁrst that ρ is positive, that is to say m ≥ 2. Let l ≥ 0 be deﬁned by the
inequalities ql < m ≤ ql+1 and let

ql+1 − m = b1q0 + · · · + bl+1ql

14

be the Ostrowski expansion of the integer ql+1 − m (see the deﬁnition at the end of Section
3). Observe that

bl+1 ≤ al+1 − 1 and that bl = 0 when bl+1 = al+1 − 1.

Then ρ − θ ∈ (−θ, 1 − θ) has two Ostrowski expansions of the form

ρ − θ = b1θ0 + · · · + bl+1θl + ∑

k≥1 al+2k+1θl+2k

and
 ρ − θ = b1θ0 + · · · + blθl−1 + (bl+1 + 1)θl + (al+2 − 1)θl+1 + ∑

k≥2 al+2kθl+2k−1,

when l ≥ 1, or ρ − θ = (b1 + 1)θ0 + (a2 − 1)θ1 + ∑

k≥2 a2kθ2k−1,

when l = 0. Set bl+2 = 0, bl+3 = al+3, bl+4 = 0, bl+5 = al+5, . . .

and
 b′
1 = b1, . . . , b′
l = bl, b′
l+1 = bl+1 + 1, b′
l+2 = al+2 − 1, b′
l+3 = 0, b′
l+4 = al+4, . . .

when l ≥ 1, or b′
1 = b1 + 1, b′
2 = a2 − 1, b′
3 = 0, b′
4 = a4, . . .

when l = 0, so that (bk)k≥1 and (b′
k)k≥1 are the sequences of digits appearing in the two
above expansions of ρ − θ. Notice that both sequences satisfy the Ostrowski numeration
rules for digits in base θ. When ρ = 0, we use the two proper expansions

1 − θ = (a1 − 1)θ0 + ∑

k≥1 a2k+1θ2k,

and −θ = ∑

k≥1 a2kθ2k−1,

to deﬁne respectively the sequences of digits (bk)k≥1 and (b′
k)k≥1. Then, we have the
following analogue of Theorem 2.1.

Theorem 4.2. Assume that ρ − θ = −mθ + p where m ≥ 1 and p are integers. When
m ≥ 2, let l ≥ 0 be deﬁned by the inequalities ql < m ≤ ql+1. When m = 1, set l = 0. Let
(Vk)k≥0 and (V ′
k)k≥0 be the two sequences of words recursively deﬁned as in Theorem 2.1,
with respect to the two sequences of digits (bk)k≥1 and (b′
k)k≥1 deﬁned above. When l is
odd, we have sθ,ρ = lim
k→+∞ Vk and s
′
θ,ρ = lim
k→+∞ V ′
k.

15

When l is even, we have
sθ,ρ = lim
k→+∞ V ′
k and s
′
θ,ρ = lim
k→+∞ Vk.

Moreover, the analogous decompositions Vk = RkTk and V ′
k = R′
kT ′
k, as in Theorem 2.1,
hold true with
 tk = b1 + · · · + bkqk−1 and t′
k = b′
1 + · · · + b′
kqk−1.

Proof. We only give a complete proof for the sequence of digits

(bk)k≥1 = {
b1, . . . , bl+1, 0, al+3, 0, al+5, . . . }.

Assume that m ≥ 2 and l is odd, and recall the notations

tk = b1 + · · · + bkqk−1 and σk = bk+1θk + bk+2θk+2 + · · ·

The argumentation is similar to the proof of Proposition 4.1. It suﬃces to show that

⌊qθ + σk⌋ = ⌊qθ⌋ (4.2)

for every integer q with 1 ≤ q ≤ qk + tk. If k ≤ l, we compute

σk = bk+1θk + · · · + bl+1θl+1 − θl+1.

Since the tail bk+1, bk+2 . . . of the sequence (bk)k≥1 contains the subsequence . . . bl+1, 0, al+3, . . .
and that bl+1 ≤ al+1 − 1, observe that this tail is neither of the form aj, 0, aj+1, 0, . . . nor
0, aj, 0, aj+1 . . .. Then, (4.2) holds true by taking again the proof of Proposition 4.1. When
k ≥ l + 1, we have
 tk = { −m + qk−1 if k = l + 2j, (j ≥ 1),
−m + qk if k = l + 2j + 1, (j ≥ 0),

and
 σk = { −θk−1 if k = l + 2j, (j ≥ 1),
−θk if k = l + 2j + 1, (j ≥ 0).

Assume ﬁrst that k has the same parity as l, namely k = l + 2j for some j ≥ 1. Then
σk = −θk−1 and tk = −m + qk−1. In order to check (4.2), we distinguish three subcases.
Assume ﬁrst q ≤ qk −1. Then ∥qθ∥ ≥ |θk−1| with equality only when q = qk−1. If q ̸= qk−1,
we have ∥qθ∥ > |θk−1|,

so that qθ and qθ − θk−1 are located in the same open interval of length one, so that (4.2)
holds true. If q = qk−1, then we have

qk−1θ − θk−1 = pk−1 and qk−1θ = pk−1 + θk−1,

16

so that (4.2) holds, since θk−1 is positive, noting that k − 1 = l − 1 + 2j is even. Assume
secondly that q = qk. Then,

qkθ − θk−1 = pk + θk − θk−1 and qkθ = pk + θk.

This shows that (4.2) holds, since both numbers θk and θk − θk−1 are negative with
absolute value less than 1. Assume thirdly that q = qk + v for some integer v with
1 ≤ v ≤ tk = −m + qk−1. Then,

qθ − θk−1 = pk + θk − θk−1 + vθ and qθ = pk + θk + vθ.

Notice now that ∥vθ∥ ≥ |θk−2| with equality only when v = qk−2. If v ̸= qk−2, we have

∥vθ∥ > |θk−2|.

Then, qθ and qθ − θk−1 are located in the same open interval of length one, since

|θk−2| ≥ |θk| + |θk−1|,

so that (4.2) holds true. If v = qk−2, then we have

qθ − θk−1 = pk + pk−2 + θk − θk−1 + θk−2 and qθ = pk + pk−2 + θk + θk−2,

so that (4.2) holds, since θk − θk−1 + θk−2 and θk + θk−2 are both negative with absolute
value less than 1.
We assume now that k = l + 2j + 1 for some j ≥ 0. Then σk = −θk and tk = −m + qk.
We distinguish again three subcases. Assume ﬁrst that q ≤ qk − 1. Then, ∥qθ∥ ≥ |θk−1|,
so that qθ and qθ − θk are located in the same open interval of length one. It folllows that
(4.2) holds. Assume secondly that q = qk. Then,

qkθ − θk = pk and qkθ = pk + θk.

This shows that (4.2) holds, since θk is positive because k = l + 2j + 1 is even. Assume
thirdly that q = qk + v for some integer v with 1 ≤ v ≤ tk = −m + qk. Then,

qθ − θk = pk + vθ and qθ = pk + θk + vθ.

Notice now that ∥vθ∥ ≥ |θk−1| > |θk|. Thus (4.2) holds. All cases have been checked.
When l is even, the numbers θl+2j (resp. θl+2j+1) turn to be positive (resp. negative),
and the above argumentation remains valid provided that we replace the usual integer part
⌊·⌋ by the upper integer part ⌈·⌉.

To illustrate this statement, take ρ = 0, a1 = 5, a2 = 3, a3 = 2; then

V0 = 0, V1 = 104, V2 = 1041041040,

17

V3 = 10410410410401041041040 = 104104104105104104105,

V ′
0 = 0, V ′
1 = 041, V ′
2 = 0041041041,

V ′
3 = 00410410410041041041041 = 051041041051041041041.

Note also that M0 = 0, M1 = 041, M2 = 0410410410,

M3 = 04104104100410410410041 = 041041041051041041051.

By induction, we check that Vn is the mirror image of V ′
n. We know that M −−
n is a
palindrome. We also have that
 −V −
n = −(V ′
n)− = M −−
n ,

where −W means the word W deprived of its ﬁrst letter. In other words, for n ≥ 1, the
words Vn and V ′
n deprived of their ﬁrst and last letters are equal to the palindrome M −−
n .

5. Repetitions in a Sturmian word

We keep our notation. Recall that s denotes an arbitrary Sturmian word of slope θ.
We show that Proposition 1 of [14] can be deduced from the recursion formulae for
the words Vk and we give further informations on the occurrence of the various cases.
Proposition 5.1 will be used in the next section to compare s with four families of (shifted
for two of them) periodic words, depending on a parameter k, constructing thus families
of strong rational approximations to the associated Sturmian number.

Proposition 5.1. Let k be an integer with k ≥ 0. Then, there exist a uniquely determined
non-empty suﬃx Uk of MkMk+1 = (Mk)ak+1+1Mk−1 and an integer ˜ak+1 such that

˜ak+1 ∈ {ak+1, ak+1 + 1}

and s = Uk(Mk)˜ak+1 Mk−1M −
k . . .

More precisely, when ak+2 − bk+2 ≥ 2, we have

Uk = Rk+1 and ˜ak+1 = ak+1.

When ak+2 − bk+2 = 1, we have

Uk = Rk+1 and ˜ak+1 = { ak+1 + 1 if bk+3 < ak+3,
ak+1 if bk+3 = ak+3.

When ak+2 = bk+2, we have Uk = RkMk+1. Moreover ˜ak+1 = ak+1, unless

ak+2 = 1, ak+3 − bk+3 ≥ 2,

18

or ak+2 = 1, ak+3 = 1, bk+3 = 0, ak+4 = bk+4,

in which cases ˜ak+1 = ak+1 + 1.

Remark. The fact that s = Uk(Mk)˜ak+1Mk−1M −
k . . . means that after the preﬁx of
length |Uk|, we have exactly ˜ak+1 + 1 copies of Mk, followed by the preﬁx of Mk of length
qk−1 − 2, since Mk−1M −
k and MkM −
k−1 diﬀer only by their last letter. In addition, we
observe that when ak+2 = bk+2 we have bk+1 = 0 and we take Uk−1 = Rk.

Proof. The idea of the proof is to show that the preﬁx of s of length 2qk+1 +qk −1 coincides
with one of the three words V 2
k+1V −
k or Vk+1VkV −
k+1 or VkVk+1V −
k+1.
Assume ﬁrst that ak+2 − bk+2 ≥ 2. Then

Vk+2 = V ak+2−bk+2
k+1 VkV bk+2
k+1 = V 2
k+1V −
k . . . ,

observing that V −
k is a preﬁx of Vk+1 (this follows from Deﬁnition 2.2). But

Vk+1Vk+1Vk = Rk+1Tk+1Rk+1Tk+1RkTk
= Rk+1Mk+1Tk+1RkTk

= Rk+1Mk+1M bk+1
k TkRkTk

= Rk+1Mk+1M bk+1+1
k Tk = Rk+1M ak+1
k Mk−1Mk . . .

Assume secondly that ak+2 − bk+2 = 1 and that ak+3 − bk+3 ≥ 1. Then

Vk+3 = V ak+3−bk+3
k+2 Vk+1V bk+3
k+2 = Vk+2V −
k+1 . . . = (Vk+1VkV bk+2+1
k+1 )− . . . = Vk+1VkV −
k+1 . . .

Actually, we can be more precise and claim that Vk+1VkVk+1V −
k is a preﬁx of s. This is
obvious unless bk+2 = 0 (then ak+2 = 1 and Vk+2 = Vk+1Vk) and ak+3 − bk+3 = 1 and
bk+3 = 0 (then Vk+3 = Vk+2Vk+1 = Vk+1VkVk+1). Assume that these three equalities hold.
If ak+4 > bk+4, we have

Vk+4 = Vk+3V −
k+2 . . . = Vk+1VkVk+1V −
k+2 . . . = Vk+1VkVk+1Vk+1V −
k . . . ,

then Vk+1VkVk+1V −
k is indeed a preﬁx of s. Otherwise, we have

Vk+4 = Vk+2Vk+3 . . . = Vk+1VkVk+1VkVk+1 . . . = Vk+1VkVk+1Vk . . . ,

and the same conclusion holds.
We claim that
 Vk+1VkVk+1Vk = Rk+1M ak+1+1
k Mk−1M bk+1+1
k Tk,

which yields that Uk = Rk+1 and ˜ak+1 = ak+1 + 1. For the proof, we distinguish two cases,
either ak+1 > bk+1, or ak+1 = bk+1. In the ﬁrst case, we have

Tk+1 = M bk+1
k Tk and Rk+1 = RkM ak+1−bk+1−1
k Mk−1,

19

so that we compute

Vk+1VkVk+1Vk = Rk+1Tk+1RkTkRk+1Tk+1RkTk

= Rk+1M bk+1
k TkRkTkRkM ak+1−bk+1−1
k Mk−1M bk+1
k TkRkTk

= Rk+1M ak+1+1
k Mk−1M bk+1+1
k Tk.

For the latter case, we have

Tk = Tk−1, Rk = Rk−1M ak−1
k−1 Mk−2, Tk+1 = M ak+1
k Tk−1 = M ak+1
k Tk, Rk+1 = Rk−1.

Thus
 Vk+1VkVk+1Vk = Rk+1Tk+1RkTkRk+1Tk+1RkTk

= Rk+1M ak+1
k Tk−1Rk−1M ak−1
k−1 Mk−2Tk−1Rk−1M ak+1
k TkRkTk

= Rk+1M ak+1+1
k Mk−1M ak+1+1
k Tk.

The claim is established.
Assume thirdly that ak+2 − bk+2 = 1 and that ak+3 = bk+3. Then, bk+2 = 0 and
ak+2 = 1. We ﬁnd

Vk+3 = Vk+1V ak+3
k+2 = Vk+1(Vk+1Vk)ak+3 = V 2
k+1Vk . . . .

The ﬁrst case shows that Uk = Rk+1 and ˜ak+1 = ak+1, as asserted.
Suppose ﬁnally that ak+2 = bk+2. Then bk+1 = 0 and ak+3 > bk+3, since ak+3 = bk+3
should yield ak+2 = bk+2 = 0. Thus,

Vk+3 = V ak+3−bk+3
k+2 Vk+1V bk+3
k+2 = Vk+2V −
k+1 . . . = VkV ak+2
k+1 V −
k+1 . . . = VkVk+1V −
k+1 . . .

Here, again, we can be more precise and show that s is either of the form

s = VkVk+1VkVk+1V −
k . . . , (5.1)

or of the form s = VkVk+1Vk+1V −
k . . . . (5.2)

If ak+2 ≥ 2, we have

Vk+3 = Vk+2V −
k+1 . . . = VkV ak+2
k+1 V −
k . . . = VkV 2
k+1V −
k . . .

Thus (5.2) holds. When ak+2 = 1 and ak+3 − bk+3 ≥ 2, we have Vk+2 = VkVk+1 and

Vk+3 = V 2
k+2V −
k+1 . . . = VkVk+1VkVk+1V −
k . . .

Thus (5.1) holds. When ak+2 = 1, ak+3 − bk+3 = 1 and bk+3 ≥ 1, we have

Vk+3 = Vk+2Vk+1V bk+3
k+2 = VkV 2
k+1V bk+3
k+2 ,

20

so that (5.2) holds true. When ak+2 = 1, ak+3 = 1 and bk+3 = 0, we have Vk+3 = VkV 2
k+1.
If ak+4 − bk+4 ≥ 1, we have

Vk+4 = Vk+3V −
k+2 . . . = VkV 2
k+1V −
k . . .

so that (5.2) holds, while

Vk+4 = Vk+2Vk+3 . . . = VkVk+1VkV 2
k+1 . . .

if ak+4 = bk+4. Then (5.1) holds. Now, we compute

VkVk+1Vk+1Vk = RkTkRk+1Tk+1Rk+1Tk+1RkTk = RkTk(RkM ak+1−1
k Mk−1)Mk+1TkRkTk
= RkM ak+1
k Mk−1M ak+1
k Mk−1MkTk = RkMk+1M ak+1
k Mk−1Tk,

and
 VkVk+1VkVk+1Vk = RkTkRk+1Tk+1RkTkRk+1Tk+1RkTk

= RkTkRkM ak+1−1
k Mk−1TkRkTkRkM ak+1−1
k Mk−1TkRkTk

= RkM ak+1
k Mk−1M ak+1+1
k Mk−1MkTk

= RkMk+1M ak+1+1
k Mk−1MkTk.

Thus Uk = RkMk+1 in both cases. We have ˜ak+1 = ak+1 when (5.2) holds, while ˜ak+1 =
ak+1 + 1 whenever (5.1) is satisﬁed.

We have used at several places the obvious property that V −
k is a preﬁx of Vk+1, which
holds since by deﬁnition Vk, Vk+1 and s share the same preﬁx of length qk − 1. A question
which arises naturally is to know when Vk is a preﬁx of Vk+1.

Proposition 5.2. For any k ≥ 0, the word Vk is a preﬁx of Vk+1 if and only if the
sequence b1, . . . , bk+1 diﬀers from 0, a2, 0, a4, . . . , ak+1 when k is odd, or diﬀers from a1 −
1, 0, a3, 0, . . . , ak+1 when k is even.

For k ≥ 0, let Wk denote the longest common preﬁx of Vk+1Vk and VkVk+1.

Lemma 5.3. We have W0 = 0a1−1−b1 and Wk+1 = V ak+2−bk+2
k+1 Wk for k ≥ 0. Conse-
quently, the length wk of Wk is given by

wk = a1 − 1 − b1 +
 k∑

j=1(aj+1 − bj+1)qj = qk+1 + qk − tk+1 − 2, k ≥ 0.

Proof. Recall that V−1 = 1, V0 = 0, and V1 = V a1−1−b1
0 V−1V b1
0 . This implies that
V0V1 = V a1−b1
0 V−1V b1
0 , thus

W0 = V a1−1−b1
0 , w0 = a1 − 1 − b1.

21

We proceed by induction. Let k ≥ 0 be an integer.
Assume ﬁrst that ak+2 − bk+2 ≥ 1.
Since Vk+2 = V ak+2−bk+2
k+1 VkV bk+2
k+1 , we get

Vk+2Vk+1 = V ak+2−bk+2
k+1 VkV bk+2+1
k+1

and Vk+1Vk+2 = V ak+2−bk+2+1
k+1 VkV bk+2
k+1 ,

thus Wk+1 = V ak+2−bk+2
k+1 Wk.

Assume now that ak+2 = bk+2. In that case, we know that bk+1 = 0. Then,

Vk+2Vk+1 = VkV ak+2+1
k+1 = VkV ak+1
k Vk−1V ak+1
k Vk−1V ak+2−1
k+1

and Vk+1Vk+2 = V ak+1
k Vk−1VkV ak+2
k+1 ,

thus Wk+1 = V ak+1
k Wk−1 = Wk = V ak+2−bk+2
k+1 Wk.

Since qk is the length of Vk, this proves the lemma.

Proof of Proposition 5.2. The word Vk is a preﬁx of Vk+1 exactly when wk ≥ qk. Lemma
5.3 tells us that wk ≥ qk if and only if tk+1 ≤ qk+1 −2. Observe ﬁnally that tk+1 ≤ qk+1 −1
with equality if and only if

bk+1 = ak+1, bk = 0, bk−1 = ak−1, bk−2 = 0, . . . .

This completes the proof.

6. The sequence of convergents contributing to the exponent of irrationality

In this section and the next one, b ≥ 2 is an integer and ξ denotes one of the num-
bers ξb(θ, ρ) or ξ′
b(θ, ρ). We analyze the convergents which contribute to the exponent of
irrationality of ξ, which we call ‘strong convergents’. According to [13], all of them are
obtained by truncating the b-ary expansion of ξ and completing by periodicity. Thus, their
denominators are either of the form bs − 1 (purely periodic case) or br(bs − 1) (existence
of a preperiod).
We adopt the following conventions of writing. Any ﬁnite word Y = y1 . . . yr with
letters in {0, . . . , b − 1} is as well viewed as the natural integer

Y = y1br−1 + · · · + yr,

22

whose sequence of b-ary digits is given by Y . Then, for any words Y = y1 . . . yr and
Z = z1 . . . zs, we have the b-ary expansions

Z
bs − 1 = 0.Z ∞,

and Y Z − Y
br(bs − 1) = 0.Y Z ∞,

where 0.z1z2 . . . = z1
b + z2
b2 + · · · and Y Z stands for the number whose b-ary sequence of
digits is the concatenation of the words Y and Z, that is, Y Z = y1 . . . yr z1 . . . zs.
Let u and v be two positive quantities depending upon a parameter k. As usual, we
write u ≍ v when there exist positive constants c1 and c2, independent of k, such that
c1u ≤ v ≤ c2u.
The candidates for the sequence of strong convergents belong to four types. We label
them by the index k ≥ 0. The sequences of ﬁnite words (Rk)k≥0, (Tk)k≥0, (Vk)k≥0 are given
by Theorem 2.1 (or Theorem 4.2), but we now replace the alphabet {0, 1} by {0, b − 1}.
We recall that R0 = 0 and T0 is the empty word. Below, the height means the logarithmic
height log H/ log b, that is, roughly speaking, the largest exponent of b appearing in the
denominator.
The ﬁrst possible convergent is

(1)k = Rk+1 − Rk
brk (brk+1−rk − 1) ,

with height ≍ rk+1 and b-ary expansion

(1)k = 0.Rk(M ak+1−bk+1−1
k Mk−1)∞.

Of course (1)k is meaningful only when rk+1 > rk, that is to say when ak+1 − bk+1 ≥ 1.
The second candidate is (2)k = Rk+1Tk
brk+1+tk − 1 ,

with height ≍ rk+1 + tk, associated to the periodic word (Rk+1Tk)∞. The third is

(3)k = Rk+1Mk − Mk
brk+1(bqk − 1) ,

with height ≍ rk+1 + qk, associated to the word Rk+1M ∞
k . The fourth is

(4)k = Vk+1
bqk+1 − 1 ,

with height ≍ qk+1 = rk+1 + tk+1, associated to the periodic word V ∞
k+1 = (Rk+1Tk+1)∞.
We say that a rational x precedes another one y, and we write x ≺ y, when the height
of x is less than the height of y. Clearly

(1)k ≺ (2)k ≼ (4)k.

23

We have (2)k = (4)k exactly when tk = tk+1, that is to say when bk+1 = 0. Then,

(1)k ≺ (2)k = (4)k ≺ (3)k.

If bk+1 ≥ 1, we have tk+1 ≥ tk + qk,

so that (1)k ≺ (2)k ≺ (3)k ≺ (4)k,

in this case. When ak+1 = bk+1, obviously bk+1 ≥ 1, so that the above inequality

(2)k ≺ (3)k ≺ (4)k

hold with (1)k being omitted.
An important observation is that we have the following coincidences between levels
k − 2, k − 1 and k.
If ak+1 − bk+1 = 1, then we have
 (1)k = (3)k−1,

since Rk(M ak+1−bk+1−1
k Mk−1)∞ = RkM ∞
k−1.

If ak+1 = bk+1, then we have
 (2)k = (4)k−2,

since we have Rk+1 = Rk−1 and Tk = Tk−1 (because bk = 0), so that

Rk+1Tk = Rk−1Tk−1 = Vk−1.

If, in addition, bk−1 = 0, then Tk−1 = Tk−2 and (2)k−2 = (2)k = (4)k−2.
Observe also that if ak+1 − bk+1 = 1, then we have

(2)k = VkVk−1
bqk+qk−1 − 1 ,

since Rk+1Tk = RkMk−1M bk
k−1Tk−1 = RkTkRk−1Tk−1 = VkVk−1,

noting that

TkRk−1 = Tk−1V bk
k−1Rk−1 = Tk−1(Rk−1Tk−1)bk Rk−1 = (Tk−1Rk−1)bk+1 = M bk+1
k−1 .

To go further for linking consecutive blocks (with indices k − 1 and k), we need to
know when the rationals (1)k, (2)k, (3)k, (4)k are indeed convergents. We indicate as well
in the next proposition the value of the exponential rate of approximation µk(j) such

|ξ − (j)k| ≍ 1
H((j)k)µk(j) = 1
bh((j)k)µk(j) ,

24

for all large k and 1 ≤ j ≤ 4, where h((j)k) is the base-b logarithm of the height H((j)k)
of (j)k. We determine in which cases the exponent µk(j) is bigger than 2, thanks to
Proposition 5.1. To that purpose, let us introduce the following quantities

νk(1) = 1 + rk+1 + tk
rk+1 , νk(2) = 1 + rk+1 + qk
rk+1 + tk ,

νk(3) = 1 + qk+1
rk+1 + qk , νk(4) = 1 + rk+2
qk+1 .

They are equal to one plus the ratio of the height of two consecutive points in the sequence
. . . (1)k, (2)k, (3)k, (4)k, (1)k+1, . . .. Then, we can state the following criterion.

Proposition 6.1. Let k ≥ 2 be an integer such that tk−1 is positive. The rational

(1)k = Rk+1 − Rk
brk (brk+1−rk − 1)

is a convergent to ξ if and only if

ak+1 − bk+1 ≥ 1, ak+2 − bk+2 ≥ 1 and then µk(1) = νk(1),

or bk ≥ 1, ak+1 = 1, bk+1 = 0, ak+2 = bk+2 and then µk(1) = νk−1(3).

The rational
 (2)k = Rk+1Tk
brk+1+tk − 1

is a convergent to ξ if and only if ak+2 − bk+2 ≥ 1 and then

µk(2) =
 



 νk(2) if bk+1 ≥ 1,
νk(4) if bk+1 = 0, ak+3 − bk+3 ≥ 1,
νk+2(2) if bk+1 = 0, ak+3 = bk+3 .

The rational
 (3)k = Rk+1Mk − Rk+1
brk+1 (bqk − 1)

is a convergent to ξ if and only if

bk+1 ≥ 1, ak+2 − bk+2 ≥ 2 and then µk(3) = νk(3),

or ak+2 − bk+2 = 1, ak+3 − bk+3 ≥ 1 and then µk(3) = νk+1(1),

or bk+1 ≥ 1, ak+2 = 1, bk+2 = 0, ak+3 = bk+3 and then µk(3) = νk(3),

25

The rational (4)k = Vk+1
bqk+1 − 1

is a convergent to ξ if and only if

ak+2 − bk+2 ≥ 2, ak+3 − bk+3 ≥ 1 and then µk(4) = νk(4),

or
 bk+1 = 0, ak+2 − bk+2 = 1, ak+3 − bk+3 ≥ 1 and then µk(4) = νk(2) = νk(4),

or ak+3 = bk+3 and then µk(4) = νk+2(2) = 1 + νk(4).

Proof. We only prove Proposition 6.1 assuming that tk−1 is large enough. In fact, crude
estimates of the constants involved in the symbols ≍ show that the lower bound btk−1 ≥ 4 is
suﬃcient for our purpose. Relaxing the assumption to tk−1 ≥ 1 follows from an alternative
argumentation which will be given in the next Section 7. Our present approach is based
on Legendre’s theorem asserting that P/Q is a convergent to ξ when |ξ − P/Q| < 1/(2Q2).
Let s be the Sturmian word composed of the b-ary digits of ξ.
For (1)k, the relevant assumption is ak+1−bk+1 ≥ 1. Assume ﬁrst that ak+2−bk+2 ≥ 1.
Then, Proposition 5.1 gives

s = Rk+1M ˜ak+1
k Mk−1M −
k . . .

= RkM ak+1−bk+1−1
k Mk−1M ˜ak+1
k Mk−1 . . .

= RkM ak+1−bk+1−1
k Mk−1M ak+1−bk+1−1
k M ˜ak+1−ak+1+bk+1+1
k Mk−1 . . .

= RkM ak+1−bk+1−1
k Mk−1M ak+1−bk+1−1
k MkMk−1 . . . ,

to be compared with the word Rk(M ak+1−bk+1−1
k Mk−1)∞. When ak+1 − bk+1 ≥ 2, we can
write
 Rk(M ak+1−bk+1−1
k Mk−1)∞ = RkM ak+1−bk+1−1
k Mk−1M ak+1−bk+1−1
k Mk−1Mk . . .

to obtain the estimate

|ξ − (1)k| ≍ 1
brk+2(ak+1−bk+1−1)qk+2qk−1+qk = 1
b2rk+1+tk .

When ak+1 − bk+1 = 1 the same estimate holds, since then

s = RkMk−1MkMk−1 . . . = RkM ak+1
k−1 Mk−2Mk−1 . . . ,

while Rk(M ak+1−bk+1−1
k Mk−1)∞ = RkM ∞
k−1 = RkM ak+1
k−1 Mk−1Mk−2 . . . .

26

Thus (1)k is a convergent to ξ and

µk(1) = 2rk+1 + tk
rk+1 = 1 + rk+1 + tk
rk+1 = νk(1).

When ak+2 = bk+2, we have bk+1 = 0, Uk = RkMk+1, and Proposition 5.1 gives

s = Uk . . . = RkM ak+1−1
k MkMk−1 . . .

We distinguish two subcases. If ak+1 ≥ 2, we write

Rk(M ak+1−1
k Mk−1)∞ = RkM ak+1−1
k Mk−1MkM ak+1−2
k Mk−1 . . . .

Thus,
 |ξ − (1)k| ≍ 1
brk+ak+1qk+qk−1 = 1
brk+1+qk ,

so that

(rk+1 + qk) − 2rk+1 = qk − rk+1 = qk − (rk + (ak+1 − 1)qk + qk−1) = tk − qk+1 + qk

is negative, since qk+1 > 2qk. Therefore (1)k is not a convergent in this subcase. When
ak+1 = 1, write s = RkMkMk−1 . . . = RkM ak
k−1Mk−2Mk−1 . . . ,

while RkM ∞
k−1 = RkM ak
k−1Mk−1Mk−2 . . .

Thus,
 |ξ − (1)k| ≍ 1
brk+(ak+1)qk−1+qk−2 = 1
brk+qk+qk−1 = 1
brk+1+qk ,

so that
 (rk+1 + qk) − 2rk+1 = −rk+1 + qk = −(rk + qk−1) + qk
= tk − qk−1 = tk−1 + (bk − 1)qk−1.

We conclude by noticing that tk−1 + (bk − 1)qk−1 is positive if bk ≥ 1 and negative when
bk = 0. Thus,
 µk(1) = rk+1 + qk
rk+1 = 1 + qk
rk+1 = 1 + qk
rk + qk−1 = νk−1(3).

Observe that, in this case, we have the ordering

(1)k = (3)k−1 ≺ (2)k+1 = (4)k−1,

while (2)k, (3)k, (4)k and (1)k+1 are not convergents to ξ.
We now deal with (2)k. Assume ﬁrst that ak+2 − bk+2 ≥ 1.

27

In the subcase ak+1 − bk+1 ≥ 1 and bk+1 ≥ 1, we have Rk+1 = RkM ak+1−bk+1−1
k Mk−1
and Proposition 5.1 gives

s = Rk+1M ˜ak+1
k Mk−1M −
k . . .

= RkM ak+1−bk+1−1
k Mk−1M ˜ak+1
k Mk−1M −
k . . .

= RkM ak+1−bk+1−1
k Mk−1M ak+1−bk+1
k M ˜ak+1−ak+1+bk+1
k Mk−1M −
k . . .

= RkM ak+1−bk+1−1
k Mk−1M ak+1−bk+1
k MkMk−1 . . .

since ˜ak+1 − ak+1 + bk+1 ≥ 1. Comparing with the word

(RkM ak+1−bk+1−1
k Mk−1Tk)∞ = RkM ak+1−bk+1−1
k Mk−1M ak+1−bk+1
k Mk−1Mk . . . ,

we obtain |ξ − (2)k| ≍ 1
brk+2(ak+1−bk+1)qk+2qk−1 = 1
b2(rk+1+tk)+rk .

Thus, (2)k is a convergent of ξ and

µk(2) = 2(rk+1 + tk) + rk
rk+1 + tk = 2 + rk
rk+1 + tk = 1 + rk+1 + qk
rk+1 + tk = νk(2).

In the subcase ak+1 = bk+1 (and thus bk+1 ≥ 1), we have (2)k = (4)k−2. Assuming
temporarily that Proposition 6.1 has been checked for (4)k−2, it yields that (2)k is again
a convergent to ξ with exponent µk(2) = µk−2(4) = νk(2) as asserted.
Consider ﬁnally the subcase bk+1 = 0. Then (2)k = (4)k and Proposition 6.1 for (4)k,
tells us that (2)k is indeed a convergent to ξ with exponent µk(2) = µk(4) which will be
computed below.
Assume now that ak+2 = bk+2. Then, Proposition 5.1 gives

s = RkMk+1 . . . = RkM ak+1
k Mk−1 . . . = RkM ak+1−1
k MkMk−1 . . . ,

while (Rk+1Tk)∞ = RkM ak+1−1
k Mk−1TkRk . . . = RkM ak+1−1
k Mk−1Mk . . .

since bk+1 = 0. It follows that

|ξ − (2)k| ≍ 1
brk+ak+1qk+qk−1 = 1
brk+1+qk = 1
b2(rk+1+tk)−(qk+1−rk) .

Then (2)k is not a convergent to ξ.
We now deal with (3)k. Assume ﬁrst that ak+2 − bk+2 ≥ 1. Proposition 5.1 gives

s = Rk+1M ˜ak+1
k Mk−1M −
k . . .

Since Rk+1M ∞
k = Rk+1M ˜ak+1
k MkMk−1 . . .

28

we obtain the estimate |ξ − (3)k| ≍ 1
brk+1+(˜ak+1+1)qk+qk−1 .

Write
 (rk+1 + (˜ak+1 + 1)qk + qk−1) − 2(rk+1 + qk) = −rk+1 + (˜ak+1 − 1)qk + qk−1
= tk+1 + (˜ak+1 − ak+1 − 1)qk.

If ak+2 − bk+2 = 1 and ak+3 − bk+3 ≥ 1, we know that ˜ak+1 = ak+1 + 1, so that tk+1 +
(˜ak+1 − ak+1 − 1)qk > 0. If ak+2 − bk+2 ≥ 2, or if ak+2 = 1, bk+2 = 0, ak+3 = bk+3, we
know that ˜ak+1 = ak+1, so that

tk+1 + (˜ak+1 − ak+1 − 1)qk = tk + (bk+1 − 1)qk.

Now, tk + (bk+1 − 1)qk is positive when bk+1 ≥ 1 and negative when bk+1 = 0. We get the
three cases announced. Concerning the exponent µk(3), we ﬁnd

µk(3) = rk+1 + (˜ak+1 + 1)qk + qk−1
rk+1 + qk .

When ˜ak+1 = ak+1, we get

µk(3) = rk+1 + qk+1 + qk
rk+1 + qk = 1 + qk+1
rk+1 + qk = νk(3),

while, in the case ˜ak+1 = ak+1 + 1, we have

µk(3) = rk+1 + qk+1 + 2qk
rk+1 + qk = 1 + qk+1 + qk
rk+1 + qk = 1 + rk+2 + tk+1
rk+2 = νk+1(1),

since rk+2 = rk+1 + qk when ak+2 − bk+2 = 1. It remains for us to prove that (3)k is not
a convergent when ak+2 = bk+2. Then, bk+1 = 0 and rk+1 = rk + (ak+1 − 1)qk + qk−1. In
this case, Proposition 5.1 gives

s = RkMk+1 . . . = RkM ak+1−1
k MkMk−1 . . .

while Rk+1M ∞
k = RkM ak+1−1
k Mk−1Mk . . . .

Thus |ξ − (3)k| ≍ 1
brk+ak+1qk+qk−1 ≍ 1
brk+1+qk ,

and (3)k is not a convergent to ξ.
For the last rational (4)k = Vk+1
bqk+1 − 1

29

Proposition 5.1 tells us that s = V 2
k+1V −
k . . . whenever

ak+2 − bk+2 ≥ 2

or ak+2 = 1 and bk+2 = 0 and ak+3 = bk+3.

Then, the initial exponent of repetition of Vk+1 is clearly larger than 2, so that (4)k is a
convergent to ξ. When ak+2 − bk+2 = 1 and ak+3 − bk+3 ≥ 1, we have

s = Vk+1VkV −
k+1 . . .

By Lemma 5.3, the common preﬁx Wk to VkVk+1 and Vk+1Vk has length

wk = a1 − 1 − b1 +
 k∑

j=1(aj+1 − bj+1)qj = qk+1 + qk − tk+1 − 2.

Noting that
 tk+1 =
 k∑

j=0 bj+1qj

is larger or smaller than qk when bk+1 ≥ 1 or bk+1 = 0, we deduce that (4)k is then a
convergent to ξ when bk+1 = 0 and is not when bk+1 ≥ 1. This yields the case

bk+1 = 0 and ak+2 − bk+2 = 1 and ak+3 − bk+3 ≥ 1.

When ak+3 − bk+3 ≥ 1 and ak+2 − bk+2 ≥ 1, Proposition 5.1, with k replaced by k + 1,
tells us that s = Rk+2Mk+1 . . . = Rk+1M ak+2−bk+2−1
k+1 MkMk+1 . . . ,

while V ∞
k+1 = Rk+1M ∞
k+1 = Rk+1M ak+2−bk+2−1
k+1 Mk+1Mk . . . .

It follows that |ξ − (4)k| ≍ 1
brk+1+(ak+2−bk+2)qk+1+qk = 1
brk+2+qk+1 .

Thus,
 µk(4) = rk+2 + qk+1
qk+1 = 1 + rk+2
qk+1 = νk(4).

Notice that νk(4) = νk(2) in the case ak+2 − bk+2 = 1 and bk+1 = 0, since (1)k+1 = (3)k
and (4)k = (2)k.
When ak+3 = bk+3, Proposition 5.1 with k replaced by k + 1, gives

s = Rk+1Mk+2M ˜ak+2
k+1 . . . = Rk+1M ak+2
k+1 MkMk+1 . . .

30

It follows that |ξ − (4)k| ≍ 1
brk+1+(ak+2+1)qk+1+qk = 1
brk+2+2qk+1 ,

since rk+2 = rk+1 + (ak+2 − 1)qk+1 + qk. Thus,

µk(4) = rk+2 + 2qk+1
qk+1 = 2 + rk+2
qk+1 = 1 + νk(4) = νk+2(2),

noting that rk+2 + qk+1 = rk+1 + qk+2 = rk+3 + qk+2,

and qk+1 = rk+1 + tk+1 = rk+3 + tk+2,

since bk+2 = 0.
When ak+2 = bk+2, the word s has a preﬁx of the form

s = Vk+2 . . . = VkV bk+2
k+1 . . .

and the common preﬁx of V ∞
k+1 and s has length at most

wk ≤ qk+1 + qk − 2 < 2qk+1.

Thus, (4)k cannot be a convergent to ξ.

The next proposition describes a tail of the sequence of strong convergents ordered by
increasing height. We start with the cyclic sequence S

(1)0, (2)0, (3)0, (4)0, (1)1, . . . , (4)k−1, (1)k, (2)k, (3)k, (4)k, (1)k+1, . . .

built with the (j)k. As already observed, some elements of S may coincide and the height
function is not necessarily increasing along S. Assume that s diﬀers from cθ, so that tk
is positive for any k ≥ h and some h ≥ 1. Then, let S+ be the tail of S formed by
the elements (j)k with k ≥ h + 1. Assuming moreover that 1 ≤ bk ≤ ak − 2 for every
k ≥ h + 1, Proposition 6.1 tells us that the sequence of strong convergents (j)k, restricted
to the indices k ≥ h + 1, coincides with S+. Otherwise, the following modiﬁcations are
needed.

Proposition 6.2. A tail of the ordered sequence of strong convergents to ξ is obtained by
applying to S+ the following replacement rules.
(i) Assume ak+2 = bk+2. When bk ≥ 1, we replace the string of seven elements
(4)k−1, . . . , (2)k+1 by the single element (4)k−1 = (2)k+1. When bk = 0, we replace the
string of nine elements (2)k−1, . . . , (2)k+1 by the single element (2)k−1 = (4)k−1 = (2)k+1.
(ii) Assume ak+2 − bk+2 = 1 and ak+3 − bk+3 ≥ 1. When bk+1 ≥ 1, we replace the
three elements (3)k, (4)k, (1)k+1 by the single element (3)k = (1)k+1, and the four elements
(2)k, (3)k, (4)k, (1)k+1 by the pair

(2)k = (4)k ≺ (3)k = (1)k+1,

31

when bk+1 = 0.
(iii) Assume that ak+2 − bk+2 ≥ 2 and ak+3 − bk+3 ≥ 1. When bk+1 = 0, we replace
the three elements (2)k, (3)k, (4)k by the single element (2)k = (4)k.

Remark. Observe that there is no overlap for the above replacement rules, since the case
(i) cannot appear for two consecutive indices k by Ostrowski’s numeration rules.

Proof. We check in each case (i), (ii) and (iii) that the elements (j)k in S which are
erased do not belong to the list provided by Proposition 6.1, while the remaining ones
belong indeed to the list.
For instance, in the case (i) with bk = 0, Proposition 6.1 tells us that µk−1(2) =
νk+1(2). Moreover, (2)k−1 = (4)k−1 = (2)k+1 ≺ (3)k+1

are convergents to ξ, while the intermediate rationals (3)k−1, (1)k, (2)k, (3)k, (4)k, (1)k+1
are not, as can be veriﬁed by reading the necessary and suﬃcient conditions displayed in
Proposition 6.1 for each element involved.

It will be proved in Proposition 7.2 that the subset of convergents to ξ given by
Proposition 6.1 provides all the convergents contributing to the irrationality exponent of
ξ. We thus obtain the

Theorem 6.3. The irrationality exponent of ξ is equal to

lim sup
k→+∞ max{µk(1), µk(2), µk(3), µk(4)} = max{ν(1), ν(2), ν(3), ν(4)},

where ν(1) = lim sup
k→+∞ {νk(1) : ak+1 − bk+1 ≥ 1 and ak+2 − bk+2 ≥ 1},

ν(2) = lim sup
k→+∞ {νk(2) : ak+2 − bk+2 ≥ 1},

ν(3) = lim sup
k→+∞ {νk(3)},

ν(4) = lim sup
k→+∞ {νk(4)}.

Proof. For any convergent (j)k to ξ, we have expressed µk(j) as some value νk′ (j′), thanks
to Proposition 6.1. Conversely, for any given νk(j), we analyze under which conditions it
contributes to the exponent of irrationality of ξ. For instance, Proposition 6.1 tells us that
νk(1) occurs exactly when ak+1 − bk+1 ≥ 1 and ak+2 − bk+2 ≥ 1, leading to the deﬁnition
of ν(1). Similarly, νk(2) appears in Proposition 6.1 if and only if

bk+1 ≥ 1, ak+2 − bk+2 ≥ 1,

or bk+1 = 0, ak+2 − bk+2 = 1, ak+3 − bk+3 ≥ 1,

32

or ak+1 = bk+1.

Remark ﬁrst that the third case is included in the ﬁrst case, because ak+1 = bk+1 implies
ak+2 − bk+2 ≥ 1 by Ostrowski’s rules. Recall that (2)k = (4)k when bk+1 = 0. Observe
now that the assumptions bk+1 = 0 and ak+2 −bk+2 ≥ 1 yield the inequality νk(2) ≤ νk(4),
with equality if and only if ak+2 − bk+2 = 1, since tk+1 = tk and

νk(2) = 1 + rk+1 + qk
rk+1 + tk = 1 + rk+2 − (ak+2 − bk+2 − 1)qk+1
qk+1 ≤ 1 + rk+2
qk+1 = νk(4).

We may thus remove the condition bk+1 ≥ 1 in the ﬁrst case, since the additional con-
tributions are taken into account by ν(4). Finally, the single constraint ak+2 − bk+2 ≥ 1
remains. We are thus led to introduce the quantity ν(2).
We now deal with the contribution of νk(4). It occurs in Proposition 6.1 exactly when

ak+2 − bk+2 ≥ 2, ak+3 − bk+3 ≥ 1,

or bk+1 = 0, ak+2 − bk+2 = 1, ak+3 − bk+3 ≥ 1.

Observe that νk(4) = 1 + rk+2
qk+1 is at most equal to 2 when bk+1 ≥ 1 and ak+2 − bk+2 = 1,
since then

rk+2 = rk+1 + qk = { rk + qk+1 − bk+1qk ≤ qk+1 − tk if ak+1 − bk+1 ≥ 1,
rk−1 + qk ≤ qk+1 if ak+1 = bk+1.

We may thus forget the condition bk+1 = 0 in the second case above. Observe also that
νk(4) < 2 when ak+2 = bk+2. It remains the constraint ak+3 − bk+3 ≥ 1. Notice however
that we may remove this last constraint as asserted. Indeed, when ak+3 = bk+3, Proposition
6.1 tells us that (4)k = (2)k+2 is a convergent to ξ with approximation exponent νk+2(2) =
1 + νk(4). Since ak+4 − bk+4 ≥ 1 by Ostrowski’s rules, the number νk+2(2) > νk(4) is taken
into account by ν(2). We may thus deﬁne ν(4) unconditionally as above.
We ﬁnally deal with the contribution of νk(3). It appears when

bk+1 ≥ 1, ak+2 − bk+2 ≥ 2,

or bk+1 ≥ 1, ak+2 = 1, bk+2 = 0, ak+3 = bk+3.

We may relax the constraints as follows. We ﬁrst forget the assumption bk+1 ≥ 1, since
when bk+1 = 0, we have rk+1 = rk + qk+1 − qk, so that

νk(3) = 1 + qk+1
rk+1 + qk = 1 + qk+1
rk + qk+1 < 2.

33

We may also relax the assumptions ak+2 = 1, bk+2 = 0, ak+3 = bk+3 in the second case
above to ak+2 − bk+2 = 1, since when ak+2 − bk+2 = 1 and ak+3 − bk+3 ≥ 1, we have
(3)k = (1)k+1, while

νk(3) = 1 + qk+1
rk+1 + qk = 1 + qk+1
rk+2 < 1 + qk+1 + qk
rk+2 = 1 + rk+2 + tk+1
rk+2 = νk+1(1).

The additional contributions are then covered by ν(1). It remains the constraint ak+2 −
bk+2 ≥ 1. But when ak+2 = bk+2, we have bk+1 = 0, so that νk(3) ≤ 2, as already
observed.
 7. The partial quotients

We keep the notation of the previous section.
For k ≥ 0, recall that we have set

ck = brk+qk−1 b(ak+1−bk+1−1)qk − 1
bqk − 1 , dk = btk − 1,

ek = brk − 1, fk = btk bbk+1qk − 1
bqk − 1 .

The integers ck, dk, ek, fk are positive, unless tk = 0 (and then dk = 0) or bk+1 = 0 (and
then fk = 0) or ak+1 − bk+1 ≤ 1 (and then ck = 0 if ak+1 − bk+1 = 1, while otherwise
ck = −brk−1 = −ek−1 − 1, by (2.3)).
Recall that we have deﬁned the possible convergents by

(1)k = Rk+1 − Rk
brk (brk+1−rk − 1) , (2)k = Rk+1Tk
brk+1+tk − 1 , k ≥ 0,

(3)k = Rk+1Mk − Mk
brk+1(bqk − 1) , (4)k = Vk+1
bqk+1 − 1 , k ≥ 0.

Put also (4)−1 = V0
bq0 − 1 = 0
b − 1 .

From a Diophantine point of view, (1)k is meaningful only when rk+1 > rk, that is to say
when ak+1 − bk+1 ≥ 1. Nevertheless, it can be formally deﬁned as well when rk+1 < rk, in
which case numerator and denominator are negative integers.
In the sequel, the notation (1)k = ck ·(4)k−1 +(3)k−1 means that the numerator (resp.,
denominator) of (1)k is equal to ck times the numerator (resp., denominator) of (4)k−1
plus the numerator (resp., denominator) of (3)k−1. With some abuse of notation,

(2)k − (1)k = Rk+1Tk − (Rk+1 − Rk)
brk+1+tk − 1 − (brk+1 − brk )

stands below for the ratio of the diﬀerence between the numerators and denominators of
(2)k and (1)k.
 34

Lemma 7.1. For k ≥ 0, we have the following relations:

(1)k = ck · (4)k−1 + (3)k−1, (k ̸= 0),

(2)k − (1)k = dk · (1)k + (4)k−1,

(2)k = 1 · ((2)k − (1)k) + (1)k,

(3)k = ek · (2)k + ((2)k − (1)k),

(4)k = fk · (3)k + (2)k.

Proof. Let us begin with the ﬁrst equality. If ak+1 − bk+1 ≥ 1, then

ck(bqk − 1) + brk (bqk−1 − 1) = brk+qk−1 (b(ak+1−bk+1−1)qk − 1) + brk (bqk−1 − 1)

= brk+(ak+1−bk+1−1)qk+qk−1 − brk

= brk+1 − brk ,

which is the denominator of (1)k. Likewise, we have

Vk × brk+qk−1 b(ak+1−bk+1−1)qk − 1
bqk − 1
= RkTk × (brk+qk−1 + brk+qk−1+qk + . . . + brk+qk−1+(ak+1−bk+1−2)qk )

= (RkTk)ak+1−bk+1−1brk+qk−1

= (RkTk)ak+1−bk+1−1RkMk−1 − RkMk−1
= Rk+1 − RkMk−1 = (Rk+1 − Rk) − (RkMk−1 − Rk),

if ak+1 − bk+1 ≥ 2, while

Vk × brk+qk−1 b(ak+1−bk+1−1)qk − 1
bqk − 1 = 0 = (Rk+1 − Rk) − (RkMk−1 − Rk),

if ak+1 − bk+1 = 1, because we then have Rk+1 = RkMk−1. In both cases we end up with
the numerator of (1)k minus the numerator of (4)k−1.
Now, assume that ak+1 = bk+1. Then, ck = −brk−1 and we check that

(−brk−1 )(bqk − 1) + brk (bqk−1 − 1) = brk−1 − brk = brk+1 − brk ,

since rk−1 + qk = rk + qk−1 and rk−1 = rk+1. As for the numerators, we have

Vk × (−brk−1) = −VkRk−1 + Rk−1
= −RkTkRk−1 + Rk−1
= −RkMk−1 + Rk+1 = (Rk+1 − Rk) − (RkMk−1 − Rk),

which conﬁrms our claim.
 35

For the second equality, observe that

btk (
brk (brk+1−rk − 1)) + (bqk − 1) = bqk+rk+1 − btk+rk + bqk − 1 = bqk+rk+1 − 1

is the denominator of (2)k. Note also that

btk (Rk+1 − Rk) = Rk+1Tk − RkTk = Rk+1Tk − Vk

is the numerator of (2)k minus the numerator of (4)k. This completes the proof of the
second equality. The third one is a tautology. The remaining two equalities are proved in
a similar way than the second one. We omit the details.

Deﬁne two sequences (Pj)j≥−1 and (Qj)j≥−1 of integers by setting

P−1 = b − 1, Q−1 = 0, P0 = 0, Q0 = b − 1,

and, denoting by (αj)j≥1 the sequence of integers c0, d0, 1, e0, f0, c1, . . .,

Pj+2 = αj+2Pj+1 + Pj, Qj+2 = αj+2Qj+1 + Qj, j ≥ −1.

Since
 c0 = ba1−b1 − b
b − 1 , d0 = 0, e0 = b − 1,

we get
 P1 = b − 1, Q1 = ba1−b1 − b, P2 = P0, Q2 = Q0,

P3 = b − 1, Q3 = ba1−b1 − 1, P4 = (b − 1)2, Q4 = ba1−b1 (b − 1), . . . .

Thus P1
Q1 = (1)0, P2
Q2 = (2)0 − (1)0, P3
Q3 = (2)0, P4
Q4 = (3)0, . . . .

Using Lemma 7.1, we check by induction on j ≥ 1 that the greatest prime divisor of the
integers Pj and Qj is equal to b−1 and that Pj and Qj are the numerator and denominator
of a fraction of one of the ﬁve types (1)k, (2)k − (1)k, (2)k, (3)k, (4)k, more precisely, they
correspond to
∗ the fraction (1)k if αj = ck;
∗ the fraction (2)k − (1)k if αj = dk;
∗ the fraction (2)k if αj = 1;
∗ the fraction (3)k if αj = ek;
∗ the fraction (4)k if αj = fk.
We explain below how to derive the sequence of partial quotients of ξ from the sequence
(αj)j≥1.
To do this, we work with matrices and recall that
( Pj+1 Pj
Qj+1 Qj
 ) = ( Pj Pj−1
Qj Qj−1
 ) · ( αj+1 1
1 0
 )

= ( 0 b − 1
b − 1 0
 ) ( α1 1
1 0
 ) · · · ( αj+1 1
1 0
 ) , j ≥ 0.

36

So we have a product of elementary integer 2 by 2 matrices ( αj 1
1 0
 )
, exactly as in the

continued fraction algorithm. Here, however, some coeﬃcients αj may be 0 or negative.
The point is that it is possible to transform this formal inﬁnite product into a product of

elementary integer 2 by 2 matrices ( α′′
j 1
1 0
 ) where all the α′′
j ’s are positive. This deﬁnes

a regular continued fraction and we show that this is precisely the continued fraction
expansion of ξ.
Simple calculations show that for nonnegative integers x and y we have
( x 1
1 0
 ) · ( 0 1
1 0
 ) · ( −x − 1 1
1 0
 ) = ( −1 1
1 0
 ) (7.1)

and ( y 1
1 0
 ) · ( 1 1
1 0
 ) · ( −1 1
1 0
 ) · ( y 1
1 0
 ) · ( 1 1
1 0
 ) = ( 0 1
1 1
 ) . (7.2)

If for some integer j ≥ 1 the integer αj+5 = ck+1 is negative, then ck+1 = −ek − 1 and,
as bk+1 = 0, we get dk+1 = dk, fk = 0, and the septuple (αj+1, . . . , αj+7) is equal to
(dk, 1, ek, 0, −ek − 1, dk, 1). Consequently, by (7.1) and (7.2), we have

( αj+1 1
1 0
 ) · · · ( αj+7 1
1 0
 ) = ( 0 1
1 1
 ) .

We derive that
( Pj+8 Pj+7
Qj+8 Qj+7
 ) = ( Pj−1 Pj−2
Qj−1 Qj−2
 ) · ( αj 1
1 0
 ) · · · ( αj+8 1
1 0
 )

= ( Pj−1 Pj−2
Qj−1 Qj−2
 ) · ( αj 1
1 0
 ) · ( 0 1
1 1
 ) · ( αj+8 1
1 0
 )

= ( Pj−1 Pj−2
Qj−1 Qj−2
 ) · ( αj + αj+8 + 1 1
1 0
 )

= ( (αj + αj+8 + 1)Pj−1 + Pj−2 Pj−2
(αj + αj+8 + 1)Qj−1 + Qj−2 Qj−2
 )

= ( (ck + ek+1 + 1)Pj−1 + Pj−2 Pj−1
(ck + ek+1 + 1)Qj−1 + Qj−2 Qj−1
 ) .
 (7.3)

This shows that Pj−1 is followed by Pj+8 = (ck + ek+1 + 1)Pj−1 + Pj−2, and similarly for
Qj−1.
Consider now the sequence (α′
j)j≥1 constructed inductively from (αj)j≥1 as follows.
We put α′
j = αj for j < j0, where j0 ≥ 1 is the smallest integer such that αj0 = ck, with
αj0+5 = ck+1 < 0. Then, we put α′
j0 = ck + ek+1 + 1 and α′
j0+1 = αj0+9 = fk+1. We
continue with α′
j0+2 = ck+2, unless ck+3 < 0, in which case we put α′
j0+2 = ck+2 +ek+3 +1.
And so on. The sequence (α′
j)j≥1 is well-deﬁned since ck and ck+1 cannot be simultaneously
negative.
 37

Said diﬀerently, for each index k such that ck+1 < 0, we replace the 10 consecutive
partial quotients ck, dk, . . . , ek+1, fk+1 by the 2 partial quotients ck + ek+1 + 1, fk+1. Let
us add that fk+1 is positive since bk+2 is positive.
We have constructed from (αj)j≥1 a sequence of nonnegative integers (α′
j)j≥1. Deﬁne

P ′
−1 = b − 1, P ′
0 = 0, Q′
−1 = 0, Q′
0 = b − 1,

and P ′
j+2 = α′
j+2Pj+1 + P ′
j, Q′
j+2 = α′
j+2Qj+1 + Q′
j, j ≥ −1.

By construction, the sequence of pairs ((P ′
j, Q′
j))j≥0 is a subsequence of ((Pj, Qj))j≥0.
Furthermore, it follows from (7.3) that P ′
j and Q′
j are the numerator and denominator of
∗ the fraction (1)k if α′
j = ck;
∗ the fraction (2)k − (1)k if α′
j = dk;
∗ the fraction (2)k if α′
j = 1;
∗ the fraction (3)k if α′
j = ek;
∗ the fraction (3)k+1 if α′
j = ck + ek+1 + 1;
∗ the fraction (4)k if α′
j = fk.
Now, we have to get rid of the 0’s in (α′
j)j≥1 and construct a sequence (α′′
j )j≥1 of
positive integers. Since ek is positive for k ≥ 0, there are no sequences of more than 3
consecutive 0’s in (α′
j)j≥1.
As already observed, we have for nonnegative integers x and y we have
( x 1
1 0
 ) · ( 0 1
1 0
 ) · ( y 1
1 0
 ) = ( x + y 1
1 0
 )

and, if α′
j+1 = 0, we get

( P ′
j+2 P ′
j+1
Q′
j+2 Q′
j+1
 ) = ( P ′
j−1 P ′
j−2
Q′
j−1 Q′
j−2
 ) · ( α′
j 1
1 0
 ) · ( α′
j+1 1
1 0
 ) · ( α′
j+2 1
1 0
 )

= ( P ′
j−1 P ′
j−2
Q′
j−1 Q′
j−2
 ) · ( α′
j + α′
j+2 1
1 0
 )

= ( (α′
j + α′
j+2)P ′
j−1 + P ′
j−2 P ′
j−1
(α′
j + α′
j+2)Q′
j−1 + Q′
j−2 Q′
j−1
 ) .
 (7.4)

This shows that P ′
j−1 is followed by P ′
j+2 = (α′
j + α′
j+2)Pj−1 + Pj−2, and similarly for
Q′
j−1.
By (7.4), if x, 0, y are consecutive elements in (α′
j)j≥1, they have to be replaced by
the single element x + y in (α′′
j )j≥1 and the pair associated with the partial quotients x + y
is the pair associated to α′
j+2, that is, the pair (P ′
j+2, Q′
j+2). Deﬁne recursively

P ′′
−1 = b − 1, P ′′
0 = 0, Q′′
−1 = 0, Q′′
0 = b − 1,

and P ′′
j+2 = α′′
j+2P ′′
j+1 + P ′′
j , Q′′
j+2 = α′′
j+2Q′′
j+1 + Q′′
j , j ≥ −1.

38

By construction, the sequence of pairs ((P ′′
j , Q′′
j ))j≥0 is a subsequence of ((P ′
j, Q′
j))j≥0,
hence of ((Pj, Qj))j≥0. Let us discuss more in details which are the possible elements of
the sequence (α′′
j )j≥1. The following cases may occur:

(i) 1, ek, fk = 0, ck+1 + ek+2 + 1 ̸= 0, fk+2 are consecutive elements of (α′
j)j≥1, in
which case we get the partial quotient ek + ck+1 + ek+2 + 1 in (α′′
j )j≥1 and

[0; α′′
1 , . . . , ek + ck+1 + ek+2 + 1] = (3)k+2,

the preceding convergent being (2)k.
(ii) 1, ek, fk = 0, ck+1 ̸= 0, dk+1 ̸= 0 are consecutive elements of (α′
j)j≥1, in which
case we get the partial quotient ek + ck+1 in (α′′
j )j≥1 and

[0; α′′
1 , . . . , ek + ck+1] = (1)k+1,

the preceding convergent being (2)k.
(iii) ek, fk ̸= 0, ck+1 = 0, dk+1 ̸= 0, 1 are consecutive elements of (α′
j)j≥1, in which
case we get the partial quotient fk + dk+1 in (α′′
j )j≥1 and

[0; α′′
1 , . . . , ek, fk + dk+1] = (2)k+1 − (1)k+1,

the preceding convergent being (3)k.
(iv) 1, ek, fk = 0, ck+1 ̸= 0, dk+1 = 0, 1 are consecutive elements of (α′
j)j≥1, in which
case we get the partial quotient ek + ck+1 + 1 in (α′′
j )j≥1 and

[0; α′′
1 , . . . , ek + ck+1 + 1] = (2)k+1,

the preceding convergent being (2)k.
(v) 1, ek, fk ̸= 0, ck+1 ̸= 0, dk+1 = 0, 1 are consecutive elements of (α′
j)j≥1, in which
case we get the partial quotient ck+1 + 1 in (α′′
j )j≥1 and

[0; α′′
1 , . . . , ck+1 + 1] = (2)k+1,

the preceding convergent being (4)k.
(vi) 1, ek, fk = 0, ck+1 = 0, dk+1 = 0, 1 are consecutive elements of (α′
j)j≥1, in which
case we get the partial quotient ek + 1 in (α′′
j )j≥1 and

[0; α′′
1 , . . . , ek + 1] = (2)k+1,

the preceding convergent being (2)k.

The cases (iv) to (vi) occur only when dk+1 = 0, that is, when b1 = . . . = bk+1 = 0.
They are not reﬂected in Proposition 6.2, where it is assumed that tk is positive.
Note that if fk = ck+1 = 0 or if ck+1 = dk+1 = 0, then there is nothing to do: we
simply remove these two 0’s from the sequence (α′
j)j≥1.

The link with Proposition 6.2 is as follows:

39

∗ Case (i) of Proposition 6.2 corresponds to the construction of (α′
j)j≥1 from (αj)j≥1,
with, if in addition bk is nul, Case (i) above.
∗ Case (ii) of Proposition 6.2 corresponds to Case (iii) above if bk+1 is positive, while
if bk+1 = 0 we remove two consecutive 0’s in the sequence (α′
j)j≥1, thereby deleting two
putative convergents.
∗ Case (iii) of Proposition 6.2 corresponds to Case (ii) above.
Since the sequence (α′′
j )j≥1 is composed of positive integers, the real number

ζ := [0; α′′
1, α′′
2 , . . .]

is well deﬁned by its continued fraction expansion. We have proved that all of its conver-
gents are of the form Pj/Qj for some index j.
It also follows from our discussion that (2)k+1 is a convergent to ζ if ck+1 and ck+2
are nonnegative. If ck+1 < 0 and fk−1 > 0, then fk−1 is an element of (α′′
j )j≥1, associated
with (4)k−1 = (2)k+1. If ck+1 < 0 and fk−1 = 0, then bk = 0 and 1, ek−1 + ck + ek+1 + 1
are consecutive elements of (α′′
j )j≥1, with this partial quotient 1 being associated to (2)k−1
and we have (2)k−1 = (4)k−1 = (2)k+1. To summarize, we have shown that (2)k+1 is a
convergent to ζ unless ck+2 is negative, that is, unless ak+3 = bk+3. However, Proposition
6.1 asserts that (2)k+1 is a convergent to ξ if and only if ak+3 ≥ bk+3 + 1. Since there
are inﬁnitely many h such that ah ≥ bh + 1, we deduce that ξ and ζ have inﬁnitely many
partial quotients in common, thus ξ = ζ.
The next statement summarizes what we have established. For j ≥ 1, write Pj/Qj =
[0; α′′
1 , α′′
2 , . . . , α′′
j ] for the j-th convergent to ξ.

Proposition 7.2. All of the convergents to ξ are of one of the ﬁve types (1)k, (2)k − (1)k,
(2)k, (3)k, (4)k. All its partial quotients are of the form

1, ck, dk, ek, fk,

or belong to the set

{ck + ek+1 + 1, ek−1 + ck + ek+1 + 1, ek + ck+1, fk + dk+1, ek + ck+1 + 1, ek + 1, ck + 1}.

More precisely, we have

Pj/Qj =
 



 (1)k if α′′
j ∈ {ck, ek−1 + ck},
(2)k − (1)k if α′′
j ∈ {dk, fk−1 + dk},
(2)k if α′′
j ∈ {1, ek−1 + ck + 1, ek−1 + 1, ck + 1},
(3)k if α′′
j ∈ {ek, ck−1 + ek + 1, ek−2 + ck−1 + ek + 1},
(4)k if α′′
j = fk.

8. Remaining proofs

Proof of Corollary 2.5. Assume that θ has unbounded partial quotients (the case of
bounded partial quotients is treated in Theorem 2.6). Let K be an inﬁnite set of positive

40

integers such that the subsequence (ak)k∈K is increasing. Assume ﬁrst that there exists an
inﬁnite set K′ ⊂ K such that (ak − bk)k∈K′ is increasing. For k ≥ 3 in K′ we have

νk−2(4) = 1 + rk
qk−1 ≥ 1 + (ak − bk − 1)qk−1
qk−1 ,

and, since ak − bk can be arbitrarily large with k in K′, we deduce that ν(4) is inﬁnite.
Assume now that there exist an inﬁnite set K′ ⊂ K and a nonnegative integer δ such
that ak − bk = δ for k in K′. For k ≥ 3 in K′ we have

νk−1(3) = 1 + qk
rk + qk−1 ≥ akqk−1
rk−1 + δqk−1 + qk−2 ≥ ak
δ + 2 .

We deduce that ν(3) is inﬁnite. Consequently, any Sturmian number whose slope has
unbounded partial quotients is a Liouville number.

Proof of Theorem 2.6. Assume that θ has bounded partial quotients. Observe that

νk(3) = 1 + qk+1
rk+1 + qk ≤ 1 + qk+1
qk , νk(4) = 1 + rk+2
qk+1 ≤ 1 + qk+2
qk+1 .

If ak+1 = bk+1, then rk+1 = rk−1 and tk = tk−1, thus

νk(2) = 2 + rk
rk+1 + tk = 2 + rk
rk−1 + tk−1 ≤ 2 + qk
qk−1 .

If ak+1 > bk+1, then rk+1 ≥ rk + qk−1, thus

νk(2) = 2 + rk
rk+1 + tk ≤ 2 + rk
rk + tk ≤ 3,

and νk(1) = 2 + tk
rk+1 ≤ 2 + tk
rk + qk−1 ≤ 2 + qk
qk−1 .

This shows that the irrationality exponent of ξb(θ, ρ) satisﬁes

µ(ξb(θ, ρ)) ≤ 2 + lim sup
k→+∞
 qk
qk−1 = 1 + µ(ξb(θ)). (8.1)

Let us now show that there exist intercepts ρ for which equality holds. Let K be an
inﬁnite set of positive integers such that

lim
k→+∞,k∈K qk
qk−1 = µ(ξb(θ)) − 1.

Take k1 ≥ 3 in K and set b1 = . . . = bk1 = 0. Put ak1+1 = bk1+1 and bk1+2 = bk1+3 = . . . =
bk2 = 0, where k2 > k1 + 2 is in K and suﬃciently large to ensure that rk2 ≥ qk2 /2. Then,
put bk2+1 = ak2+1 and bk2+2 = . . . = bk3 = 0, where k3 > k2 + 2 is in K and suﬃciently
large to ensure that rk3 ≥ 2qk3 /3. Proceeding like this, we deﬁne inductively an icreasing

41

sequence (kj)j≥2 of integers in K such that bkj +1 = akj +1 and bk = 0 for every k not in
(kj)j≥2. In addition, we have rkj ≥ (j − 1)qkj /j, for j ≥ 2.
Denote by ρ the intercept deﬁned by this sequence (bk)k≥1 and let us determine the
irrationality exponent of ξb(θ, ρ).
Recall that for an index h such that bh+1 = ah+1 we have rh+1 = rh−1 and th = th−1,
thus νh(2) = 2 + rh
rh+1 + th = 2 + rh
rh−1 + th−1 = 2 + rh
qh−1 .

Consequently, we get
 νkj (2) ≥ 2 + (j − 1)qkj
jqkj −1 , j ≥ 2,

and
 µ(ξb(θ, ρ)) ≥ ν(2) ≥ 2 + lim sup
j→+∞
 qkj
qkj −1 = 2 + lim
k→+∞,k∈K qk
qk−1 = µ(ξb(θ)) + 1.

The reverse inequality follows from (8.1). Consequently, we get

µ(ξb(θ, ρ)) = 1 + µ(ξb(θ)).

This proves the theorem.

Proof of Theorem 2.7. Assume that not all bk are 0. Let k be an integer large enough
to ensure that tk is positive and that ak, ak+1, . . . are all at most equal to M . Then, it
follows from Proposition 6.2 that there are four (possibly overlapping) cases:
(i) If ak+2 = bk+2, then (2)k+1 is a convergent to ξ;
(ii) If ak+3 = bk+3, then (2)k+2 is a convergent to ξ;
(iii) If ak+4 = bk+4, then (2)k+3 is a convergent to ξ;
(iv) If (i), (ii), and (iii) do not hold, then (1)k+1 and (2)k+1 are convergents to ξ.
In case (i), the rate of approximation of ξ by (2)k+1 is at least equal to

νk+1(2) = 2 + rk+1
rk+2 + tk+1 = 2 + rk+1
qk ≥ 2 + qk−1
qk ≥ 2 + 1
M + 1 ,

since rk+2 = rk, tk+1 = tk, and rk+1 ≥ qk−1.
Similarly, in case (ii) (resp., (iii)), the rate of approximation of ξ by (2)k+2 (resp., by
(2)k+3) is at least equal to 2 + 1/(M + 1).
In case (iv), note that rk+2 + tk+1 ≤ (ak+2 + 1)qk+1, thus

νk+1(1) = 2 + tk+1
rk+2 ≥ 2 + tk+1
(M + 1)qk+1 , νk+1(2) = 2 + rk+1
rk+2 + tk+1 ≥ 2 + rk+1
(M + 1)qk+1 .

Recalling that rk+1 + tk+1 = qk+1, we get

max{νk+1(1), νk+1(2)} ≥ 2 + 1
2(M + 1) .

42

This shows that, for every suﬃciently large k, there exists a rational number P/Q with

bqk ≤ Q ≤ bqk+4 (8.2)

such that |ξ − P/Q| ≤ Q−2−1/(2(M +1)). We are then in position to apply Th´eor`eme 3.1 of
[3] with ε = 1
2(M +1) and S the empty set. Note that, by (8.2), the number c introduced in
(3.2) of its proof can be taken to be (M + 1)5. Consequently, the upper bound

w∗
d(ξ) ≤ (2d)κ(log log 3d), d ≥ 1,

given by Th´eor`eme 3.1 of [3] holds with a real number κ depending only on M .

References

[1] B. Adamczewski, On the expansion of some exponential periods in an integer base,
Math. Ann. 346 (2010), 107–116.

[2] B. Adamczewski and J.-P. Allouche, Reversals and palindromes in continued frac-
tions, Theor. Comput. Sci. 380 (2007), 220–237.

[3] B. Adamczewski et Y. Bugeaud, Mesures de transcendance et aspects quantitatifs de
la m´ethode de Thue–Siegel–Roth–Schmidt, Proc. London Math. Soc. 101 (2010),
1–31.

[4] B. Adamczewski and Y. Bugeaud, Nombres r´eels de complexit´e sous-lin´eaire : mesures
d’irrationalit´e et de transcendance, J. Reine Angew. Math. 658 (2011), 65–98.

[5] J.-P. Allouche and J. Shallit, Automatic Sequences: Theory, Applications, General-
izations, Cambridge University Press, 2003.

[6] W. W. Adams and J. L. Davison, A remarkable class of continued fractions, Proc.
Amer. Math. Soc. 65 (1977), 194–198.

[7] P. Arnoux, Sturmian sequences. In: Substitutions in dynamics, arithmetics and
combinatorics, 143–198, Lecture Notes in Math., 1794, Springer, Berlin, 2002.

[8] V. Berth´e, C. Holton, and L. Q. Zamboni, Initial powers of Sturmian sequences, Acta
Arith. 122 (2006), 315–347.

[9] V. Berth´e, Autour du syst`eme de num´eration d’Ostrowski, Bull. Belg. Math. Soc.
Simon Stevin 8 (2001), 209–239.

[10] P. E. B¨ohmer, ¨Uber die Transzendenz gewisser dyadischer Br¨uche, Math. Ann. 96
(1927), 367–377.

[11] Y. Bugeaud, Approximation by algebraic numbers. Cambridge Tracts in Mathemat-
ics 160, Cambridge, 2004.

[12] Y. Bugeaud, Distribution modulo one and Diophantine approximation. Cambridge
Tracts in Mathematics 193, Cambridge, 2012.

43

[13] Y. Bugeaud and D. H. Kim, A new complexity function, repetitions in Sturmian
words, and irrationality exponents of Sturmian numbers, Trans. Amer. Math. Soc.
371 (2019), 3281–3308.

[14] Y. Bugeaud, D. H. Kim, M. Laurent and A. Nogueira, On the Diophantine nature
of the elements of Cantor sets arising in the dynamics of contracted rotations, Ann.
Scuola Normale Superiore di Pisa. To appear. https://arxiv.org/abs/2001.00380

[15] L. V. Danilov, Certain classes of transcendental numbers Mat. Zametki 12 (1972),
149–154 (in Russian). English translation in Math. Notes 12 (1972), 524–527.

[16] J. L. Davison, A series and its associated continued fraction, Proc. Amer. Math.
Soc. 63 (1977), 29–32.

[17] S. Ferenczi and Ch. Mauduit, Transcendence of numbers with a low complexity
expansion, J. Number Theory 67 (1997), 146–161.

[18] J. F. Koksma, ¨Uber die Mahlersche Klasseneinteilung der transzendenten Zahlen
und die Approximation komplexer Zahlen durch algebraische Zahlen, Monats. Math.
Phys. 48 (1939), 176–189.

[19] T. Komatsu, A certain power series and the inhomogeneous continued fraction ex-
pansions, J. Number Theory 59 (1996), 291–312.

[20] M. Laurent and A. Nogueira, Rotation number of contracted rotations, J. Mod. Dyn.
12 (2018), 175–191.

[21] M. Laurent and A. Nogueira, Dynamics of 2-interval piecewise aﬃne maps and
Hecke-Mahler series, J. Mod. Dyn. 17 (2021), 33–63.

[22] M. Lothaire, Algebraic combinatorics on words. Encyclopedia of Mathematics and
its Applications, vol. 90, Cambridge University Press, Cambridge, 2002.

[23] C. Wojcik, Factorisations des mots de basse complexit´e. Doctoral thesis, Universit´e
de Lyon, 2019.

Yann Bugeaud Michel Laurent
Universit´e de Strasbourg, CNRS Aix-Marseille Universit´e, CNRS, Centrale Marseille
IRMA, UMR 7501 Institut de Math´ematiques de Marseille
7, rue Ren´e Descartes 163 avenue de Luminy, Case 907
67084 STRASBOURG (FRANCE) 13288 MARSEILLE C´edex 9 (FRANCE)

bugeaud@math.unistra.fr michel-julien.laurent@univ-amu.fr

44
