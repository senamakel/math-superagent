<!-- source: https://arxiv.org/pdf/1511.01671 | converted from PDF -->

arXiv:1511.01671v2  [math.NT]  15 Nov 2017
NORMALITY OF THE THUE–MORSE SEQUENCE ALONG
PIATETSKI-SHAPIRO SEQUENCES, II

CLEMENS M ¨ULLNER AND LUKAS SPIEGELHOFER

Abstract. We prove that the Thue–Morse sequence t along subsequences indexed by ⌊nc⌋
is normal, where 1 < c < 3/2. That is, for c in this range and for each ω ∈ {0, 1}L, where
L ≥ 1, the set of occurrences of ω as a factor (contiguous ﬁnite subsequence) of the sequence
n ↦→ t⌊nc⌋ has asymptotic density 2−L. This is an improvement over a recent result by the
second author, which handles the case 1 < c < 4/3.
In particular, this result shows that for 1 < c < 3/2 the sequence n ↦→ t⌊nc⌋ attains both
of its values with asymptotic density 1/2, which improves on the bound c < 1.4 obtained by
Mauduit and Rivat (who obtained this bound in the more general setting of q-multiplicative
functions, however) and on the bound c ≤ 1.42 obtained by the second author.
In the course of proving the main theorem, we show that 2/3 is an admissible level of
distribution for the Thue–Morse sequence, that is, it satisﬁes a Bombieri–Vinogradov type
theorem for each exponent η < 2/3. This improves on a result by Fouvry and Mauduit, who
obtained the exponent 0.5924. Moreover, the underlying theorem implies that every ﬁnite
word ω ∈ {0, 1}L is contained as an arithmetic subsequence of t.

1. Introduction

The Thue–Morse sequence t is a well-known inﬁnite sequence on the two symbols 0 and 1,
which can be deﬁned as follows. Starting with the 1-element sequence t
(0) = (0) and constructing
t
(n+1) by concatenating t
(n) and its Boolean complement ¬t
(n), the inﬁnite sequence

t = 0110100110010110 . . .

is the pointwise limit of these ﬁnite sequences. In other words, it is the ﬁxed point, starting
with 0, of the substitution 0 ↦→ 01, 1 ↦→ 10. The sequence t can therefore be seen as a 2-
automatic sequence (see the book [2] by Allouche and Shallit), indeed it is one of the simplest
such sequences. Another equivalent deﬁnition uses the binary sum-of-digits function s, which
counts the number of 1s in the binary expansion of a nonnegative integer: we have tn = 0 if and
only if 2 | s(n). Since t is an automatic sequence, its factor complexity is bounded above by a
linear function, that is, the number P (k) of diﬀerent factors of length k of t is bounded by Ck
for some constant C. (For the Thue–Morse sequence, we have lim sup P (k)/k = 10/3 [4].) More
about the Thue–Morse sequence can be found in the article [1] by Allouche and Shallit, which
gathers occurrences of the Thue–Morse sequence in diﬀerent ﬁelds of mathematics and oﬀers a
good bibliography, and in the article [13] by Mauduit.
Although the sequence t itself has low complexity, the situation changes completely if we
consider the subsequence indexed by the squares 0, 1, 4, 9, 16, . . .. Moshe [19] proved that this
subsequence has full factor complexity, that is, every block {ε0, . . . , εL−1} ∈ {0, 1}L, for L ≥

The ﬁrst author was supported by the Austrian Science Fund (FWF), Project F5502-N26, which is a part of
the Special Research Program “Quasi Monte Carlo Methods: Theory and Applications”, and Project F5002-N15,
which is a part of the Special Research Program “Algorithmic and Enumerative Combinatorics”.
The second author was supported by the Austrian Science Fund (FWF), Project F5502-N26, which is a part
of the Special Research Program “Quasi Monte Carlo Methods: Theory and Applications”, and Project I1751,
called MuDeRa (Multiplicativity, Determinism, and Randomness).

1

2 C. M ¨ULLNER AND L. SPIEGELHOFER

1, occurs as a factor of the sequence n ↦→ tn2 . Drmota, Mauduit and Rivat [7] proved the
stronger statement that each of these blocks in fact occurs with density 2−L, in other words,
this subsequence is a normal sequence. This latter result was the motivation for our research.
The second author [23] recently proved (using an estimate for discrete Fourier coeﬃcients
from [7]) an analogous result for subsequences indexed by so-called Piatetski-Shapiro sequences,
which are sequences of the form ⌊nc⌋.

Theorem 0 (Spiegelhofer 2015). Assume that 1 < c < 4/3. Then the sequence (
t⌊nc⌋)

n≥0 is
normal.

The study of Piatetski-Shapiro sequences, “Polynomials of degree c”, can be motivated by
problems for polynomials of degree 2. For example, while it is unknown whether there are
inﬁnitely many primes of the form n2 + 1, the Piatetski-Shapiro Prime Number Theorem [20]
states that for 1 < c < 12/11 the number of primes of the form ⌊nc⌋ behaves asymptotically as
one would expect by heuristic arguments. The exponent c has been improved several times, the
currently best known bound c < 2817/2426 being due to Rivat and Sargos [21].
In a similar way the problem of studying the sum of digits of ⌊nc⌋ can be motivated. It
was asked by Gelfond [11] to investigate the distribution in residue classes of the sum of digits
of values of polynomials f such that f (N) ⊆ N. This problem could not be solved even for
polynomials of degree two, and so Mauduit and Rivat [14, 15] ﬁrst proved a nontrivial result on
sequences n ↦→ ϕ
(⌊nc⌋)
, where 1 ≤ c < 1.4 and ϕ is a q-multiplicative function with values on
the unit circle S1. We do not give a deﬁnition of this term, we only note that the Thue–Morse
sequence in the form n ↦→ (−1)
s(n) is a 2-multiplicative function. (The cited result [15] was also
transferred to automatic sequences by Deshouillers, Drmota and Morgenbesser [6]. They also
proved in that article that for 1 < c < 10/9 blocks of length 2 in Piatetski-Shapiro subsequences
of t occur with frequency 1/4.) Dartyge and Tenenbaum [5] made some progress on the original
question of Gelfond, and ﬁnally Mauduit and Rivat [16] could tackle the sum of digits of squares.
(This result was later generalized to compact groups by Drmota and Morgenbesser [8].) However,
there remained a gap to be closed—nothing was known on Piatetski-Shapiro subsequences of
q-multiplicative functions for c in the range [1.4, 2). In 2014, the second author [22] extended
the bound for c in the case of the Thue–Morse sequence, obtaining the result that for c ≤ 1.42
the sequence n ↦→ t⌊nc⌋ attains both of its values with asymptotic density 1/2 (that is, this
sequence is simply normal ).
In the present paper, we improve on the known results on normality and simple normality of
Piatetski-Shapiro subsequences of t. Our main theorem is the following.

Theorem 1. Let 1 < c < 3/2. Then the sequence u = (
t⌊nc⌋)

n≥0 is normal. More precisely,
for any L ≥ 1 there exists an exponent η > 0 and a constant C such that
∣
∣
∣∣
∣
{n < N : (
u(n), u(n + 1), . . . , u(n + L − 1)
) = ω}∣
∣ − N/2L∣
∣
∣ ≤ CN 1−η

for all ω = (
ω0, . . . , ωL−1) ∈ {0, 1}L.

The essential innovation provided by this theorem lies in the new bound 3/2 = 1.5, which re-
places the bound 4/3 = 1. ˙3 for (proper) normality as in Theorem 0. For comparison, we note that
4/3 is the bound that Mauduit and Rivat obtained in the ﬁrst paper [14] on Piatetski-Shapiro
subsequences of q-multiplicative functions, while 1.42 [22] is the most recent improvement on
the exponent c, concerning simple normality of Piatetski-Shapiro subsequences of t. The new
bound 3/2 established in our theorem therefore is a signiﬁcant improvement—not only does it
surpass the bound 1.42 for simple normality (which is the case that L = 1), it also pushes the
bound for proper normality beyond this value. Another improvement on Theorem 0 is the error
term CN 1−η, where both the exponent η and the constant can be made completely explicit.

NORMALITY OF THE THUE–MORSE SEQUENCE 3

In the proof of Theorem 1, we reduce the problem of handling Piatetski-Shapiro sequences
to the study of Beatty sequences ⌊nα + β⌋, where α, β ∈ R and n is contained in a small inter-
val in N of length N , a process that is basically Taylor approximation of degree 1 [22]. This
yields sums of the form ∑
n∈I t(⌊nα + β⌋). In order to deal with these sums, we use methods
by Mauduit and Rivat [16, 17], introducing the two-fold restricted sum-of-digits function. Af-
terwards, we eliminate the Beatty sequences ⌊nα + β⌋ from our expressions by exploiting the
usually very small discrepancy (modulo 1) of nα-sequences. The resulting expression can be
estimated nontrivially with the help of a new estimate (similar to [7, Proposition 1]) for discrete
Fourier coeﬃcients related to the sum-of-digits function, which ﬁnishes the proof of Theorem 1.
Let us give a few more details on the methods used in the proof. By Taylor approximation,
we may approximate ⌊nc⌋ on short intervals I by Beatty sequences in such a way that ⌊nc⌋ =
⌊nα + β⌋ for most n ∈ I. This method is summarized in Proposition 2.8 and leads to a statement
reminiscent of the Bombieri–Vinogradov theorem in prime number theory: in order to prove our
theorem, we have to study the distribution of the Thue–Morse sequence on Beatty sequences
⌊nα + β⌋, where we take an average in α over dyadic intervals [D, 2D] (see Theorem 2.4). Of
course, greater values of D correspond to greater exponents c in the original problem. Therefore
we want to obtain a nontrivial distribution result for given length N of the Beatty sequence,
and D as large as possible. This Beatty sequence approach has been followed by the second
author [22]. In that article, trigonometric approximation of indicator functions was used in order
to dispose of the Beatty sequences, which led to the integral (2.6) in Section 2. An estimate for
this integral, taken from [10], yielded the new bound 1.42, which surprisingly beat the formerly
best bound 1.4 [15] (concerning simple normality of subsequences of t). However, we also have
a lower bound on this integral, which sets a limit for this method. In particular, 3/2 can not be
reached in this way.
In the second part of the proof of Theorem 1 we therefore use a method diﬀerent from
trigonometric approximation in order to handle Beatty subsequences of t. This method is based
on the fact that Beatty sequences ⌊nα + β⌋, for most α, are uniformly distributed in residue
classes, their discrepancy being very small. To put it simply, we will have to deal with sums
∑

n∈I f (⌊nα + β⌋),(1.1)

where f is 2γ-periodic and I ⊆ Z is an interval slightly longer than 2γ, for instance |I| = 2γ(1+ε).
By a result on the mean discrepancy of nα-sequences (Lemma 3.4), we may replace this sum,
on average, by
 |I|
2γ ∑

n<2γ f (n) + O(
2γ(log|I|)
2)
.

In order to apply this argument, we have to obtain sums of the form (1.1). To this end, we
adapt methods by Mauduit and Rivat [16, 17], thereby introducing the two-fold restricted sum-
of-digits function sµ,λ (which we deﬁne below). The transition from the sum-of-digits function
s to the truncated version sλ is straightforward and can also be carried out for ⌊nc⌋ (see [23]).
It is not so clear, however, how to get rid of the lowest µ digits of ⌊nc⌋, that is, how to proceed
from sλ(⌊nc⌋) to sµ,λ(⌊nc⌋). At this point, Beatty sequences ⌊nα + β⌋ come into play: using
rational approximations to α and a generalization of van der Corput’s inequality (Lemma 3.2),
it is possible to eliminate the lowest µ digits of ⌊nα + β⌋, so that we are left with only γ := λ − µ
binary digits of ⌊nα + β⌋. This further reduction of the number of digits to be taken into account
ultimately allows us to achieve the improvement 3/2 over the bound 4/3 obtained in [23]. As the
last step of the proof, we use Proposition 2.7 from below. This proposition is a new estimate for
discrete Fourier coeﬃcients, related to a result by Drmota, Mauduit and Rivat [7, Proposition 1],

4 C. M ¨ULLNER AND L. SPIEGELHOFER

and allows us not only to deal with general block lengths L ≥ 1, but also to derive an explicit
error term of the form stated in Theorem 1.
The classical Bombieri–Vinogradov Theorem is a statement on the average distribution of
prime numbers in arithmetic progressions nd + j, where the average is taken in the modulus d.
Let
 ψ(x; d, j) = ∑

1≤n≤x
n≡j mod d
 Λ(n),

where Λ is the von Mangoldt function deﬁned by Λ(n) = log p if n = pk for some prime p and
some k ≥ 1 and Λ(n) = 0 otherwise. Then the Bombieri–Vinogradov Theorem [3, Theorem 4]
states that for all positive real numbers A > 0 there exist B > 0 and a constant C such that

∑

1≤d≤D max
1≤y≤x max
j∈Z
(j,d)=1
 ∣
∣
∣
∣ψ(y; d, j) − y
φ(d)
 ∣
∣
∣
∣ ≤ Cx(log x)
−A,

where D = x
1/2(log x)
−B. While no improvement on the exponent 1/2 is known, the Elliott–
Halberstam conjecture [9] asks whether we can choose D = x
1−ε for any ε > 0. In other words,
it is conjectured that 1 is an admissible level of distribution for the primes, whereas the largest
known admissible level (as of 2015) equals 1/2. In the article [10], Fouvry and Mauduit prove
a Bombieri–Vinogradov type theorem for the sum-of-digits function s in base 2. In particular,
for the case of the Thue–Morse sequence they set

A
±(x; d, j) = ∣
∣
∣{n < x : (−1)
s(n) = ±1, n ≡ j mod d
}∣
∣
∣

and obtain

(1.2) ∑

1≤d≤D max
1≤y≤x max
j∈Z
 ∣
∣
∣A
±(y; d, j) − y
2d
 ∣
∣
∣ ≤ Cx(log 2x)
−A

for all real A and D = x
0.5924. The exponent 0.5924 can therefore be called admissible level of
distribution for the Thue–Morse sequence. (We note that Fouvry and Mauduit obtain in fact an
error term x
1−η for some η > 0, which follows from [10, Th´eor`eme 2]. We will use this improved
estimate in the proof of Corollary 2.2.) Using sieve theory, they apply this result to the study
of the sum of digits of almost prime numbers, that is, integers that are the product of at most
two prime factors. Later and by diﬀerent means, Mauduit and Rivat [17] studied the sum of
digits of prime numbers, which was not accessible by the Fouvry–Mauduit method.
As we indicated earlier, the backbone of our main result is a Bombieri–Vinogradov type
theorem for t. We establish 2/3 as an admissible level of distribution for the Thue–Morse
sequence, improving on the bound established by Fouvry and Mauduit. A Beatty sequence
version of this result, combined with linear approximation of ⌊nc⌋, allows us to obtain the
improvement 1.5 over the bound 1.42.

Notation. We use the common abbreviations e(x) = exp(2πix), {x} = x − ⌊x⌋, and ∥x∥ =
minn∈Z |x − n|, where x is a real number. For a prime number p let νp(n) be the exponent of p
in the prime factorization of n. We deﬁne the truncated binary sum-of-digits function

sλ(n) = s(˜n),

where 0 ≤ ˜n < 2λ and ˜n ≡ n mod 2λ, which only takes into account the digits of n at positions
smaller than λ, and for µ ≤ λ the two-fold restricted binary sum-of-digits function

sµ,λ(n) = sλ(n) − sµ(n),

NORMALITY OF THE THUE–MORSE SEQUENCE 5

which only depends on the digits at the positions µ, . . . , λ − 1. The functions sλ and sµ,λ are
periodic with period 2λ. In estimates we use the convenient abbreviation

log+x = max {1, log x} .

Summation variables are always assumed to be nonnegative. In particular, we often omit con-
ditions such as 0 ≤ n under summation signs. In this article, the symbol N denotes the set of
nonnegative integers. Moreover, constants implied by the symbols ≪ and O depend at most on
L, that is, on the length of a factor ω = (ω0, . . . , ωL−1) of the sequences considered.

2. Results and overall structure of the proofs

In the introduction we have already stated our main theorem (Theorem 1), concerning the
normality of Piatetski-Shapiro subsequences of t for exponents c < 3/2. In the current section
we state auxiliary results used for proving this theorem: approximation of ⌊nc⌋ by Beatty
sequences (Proposition 2.8), a Beatty–Bombieri–Vinogradov theorem for t (Theorem 2.4 and its
precursor, Proposition 2.6), and an estimate for discrete Fourier coeﬃcients (Proposition 2.7).
Moreover, we state results analogous to Theorem 2.4 and Proposition 2.6, concerning arithmetic
progressions (Theorem 2.1 and Proposition 2.5), which follow from the same method of proof.
Let α, β, y and z be nonnegative real numbers such that α ≥ 1, and ω = (ω0, . . . , ωL−1) ∈
{0, 1}L, where L ≥ 1 is an integer. We deﬁne

Aω(y, z; α, β) = ∣
∣
{y ≤ m < z : ∃n ∈ Z such that m = ⌊nα + β⌋ and

s(⌊(n + ℓ)α + β⌋) ≡ ωℓ mod 2 for 0 ≤ ℓ < L}∣
∣.

Note that for L = 1, α, β ∈ Z and y = 0 this yields the sets A
±(x; d, j) that occur in [10] (in
that article, however, general moduli q ≥ 2 are handled. In the present article, we are only
concerned with the case q = 2, that is, the Thue–Morse sequence.) The ﬁrst auxiliary result,
a Bombieri–Vinogradov type theorem, is an average result on the sets Aω(y, z; d, j) and might
also be of independent interest.

Theorem 2.1. Let L ≥ 1 be an integer and ω = (ω0, . . . , ωL−1) ∈ {0, 1}L. Assume that

0 < δ1 ≤ δ2 < 2/3.

There exist η > 0 and a constant C such that

∑

D<d≤2D max
y,z
0≤y≤z
z−y≤x
 max
j∈Z
 ∣
∣
∣
∣Aω(y, z; d, j) − z − y
2Ld
 ∣
∣
∣
∣ ≤ Cx
1−η

for all x and D such that x ≥ 1 and x
δ1 ≤ D ≤ x
δ2 .

(Note that the maximum is well-deﬁned by a ﬁniteness argument. The same holds true for
the subsequent results.) This theorem diﬀers in several aspects from [10, Corollary 3]. The most
important novelty is the exponent 2/3, which improves on the exponent 0.5924. Moreover, the
left endpoint of the interval [y, z) may be an arbitrary nonnegative real number (which works
well in the sum-of-digits setting, but fails for prime numbers). Finally, this theorem handles
consecutive elements of arithmetic subsequences of the Thue–Morse sequence t. This latter
feature necessitates a nontrivial lower bound for D, since factors of length 2 of t do not appear
with frequency 1/4, therefore the contribution of d = 1 would already be too large.
Setting L = 1 and using the above-cited result (with the improved error term x
1−η) in order
to handle small step lengths d, we obtain the following corollary.

6 C. M ¨ULLNER AND L. SPIEGELHOFER

Corollary 2.2. For real y ≥ 0 and integers d ≥ 1 and j ≥ 0 set

A(y; d, j) = |{m < y : s(m) ≡ 0 mod 2, m ≡ j mod d}| .

For all δ ∈ (0, 2/3) there exist η > 0 and C such that
∑

1≤d≤D max
y≤x max
j∈Z
 ∣
∣
∣A(y; d, j) − y
2d
 ∣
∣
∣ ≤ Cx
1−η

for x ≥ 1 and D = x
δ.

A simple but interesting consequence of Theorem 2.1 is the following result.

Corollary 2.3. Every ﬁnite sequence on the symbols 0 and 1 appears as an arithmetic subse-
quence of the Thue–Morse sequence.

An adaptation of the proof of Theorem 2.1 yields the following Beatty sequence analogue.

Theorem 2.4. Let L ≥ 1 be an integer, ω = (ω0, . . . , ωL−1) ∈ {0, 1}L and 0 < δ1 ≤ δ2 < 2/3.
There exist η > 0 and C such that
∫ 2D

D max
y,z
0≤y≤z
z−y≤x
 max
β≥0
 ∣
∣
∣
∣Aω(y, z; α, β) − z − y
2Lα
 ∣
∣
∣
∣ dα ≤ Cx
1−η

for all x and D such that x ≥ 1 and x
δ1 ≤ D ≤ x
δ2 .

As we announced in the introduction, this theorem can be used to obtain Theorem 1.
The proofs of Theorems 2.1 and 2.4 are based on exponential sum estimates. In order to
establish Theorem 2.1, it is suﬃcient to prove the following proposition.

Proposition 2.5. Let L ≥ 1 be an integer, a = (a0, . . . , aL−1) ∈ {0, 1}L and a ̸= (0, . . . , 0).
For real numbers N, D ≥ 1 and ξ set

S1 = S1(N, D, ξ) = ∑

D≤d<2D max
j≥0
 ∣
∣
∣
∣
∣
 ∑

n<N e
( 1
2
 ∑

ℓ<L aℓs(
(n + ℓ)d + j)
)
 e(nξ)

∣
∣
∣
∣
∣.

Let 0 < ρ1 ≤ ρ2 < 2. There exists an η > 0 and a constant C such that

(2.1) S1
N D ≤ CN −η

holds for all ξ ∈ R and all real numbers N, D ≥ 1 satisfying N ρ1 ≤ D ≤ N ρ2 .

For L = 1 this result intuitively states that for most step lengths d slightly smaller than the
square of the length of the sum, we have a nontrivial estimate for sums over the Thue–Morse
sequence on arithmetic progressions.
Analogously, Theorem 2.4 is based on the following result.

Proposition 2.6. Let L ≥ 1 be an integer, a = (a0, . . . , aL−1) ∈ {0, 1}L and a ̸= (0, . . . , 0).
For real numbers D, N ≥ 1 and ξ set

˜S1 = ˜S1(N, D, ξ) = ∫ 2D

D max
β≥0
 ∣
∣
∣
∣
∣
 ∑

n<N e
( 1
2
 ∑

ℓ<L aℓs(
⌊(n + ℓ)α + β⌋))
 e(nξ)

∣
∣
∣
∣
∣ dα.

Let 0 < ρ1 ≤ ρ2 < 2. There exist η > 0 and a constant C such that

(2.2) ˜S1
N D ≤ CN −η

holds for all real numbers D, N ≥ 1 satisfying N ρ1 ≤ D ≤ N ρ2 and for all ξ ∈ R.

NORMALITY OF THE THUE–MORSE SEQUENCE 7

The proofs of Propositions 2.5 and 2.6 in turn rely on an estimate for discrete Fourier coef-
ﬁcients related to the sum-of-digits function. These Fourier coeﬃcients have been used as an
essential tool in the article [7] on the normality of the Thue–Morse sequence along the sequence
of squares. For nonnegative integers d and λ, for sequences i : N → N and a : N → Z, where a
has ﬁnite support, and for h ∈ Z we deﬁne

(2.3) G
i,a
λ (h, d) = 1
2λ ∑

u<2λ e
( 1
2
 ∑

ℓ∈N aℓsλ(
u + ℓd + iℓ) − hu
2λ
 )
.

The function h ↦→ G
i,a
λ (h, d) is the discrete Fourier transform of the 2λ-periodic sequence

n ↦→ e

( 1
2
 ∑

ℓ≥0 aℓsλ(
n + ℓd + iℓ)
)

.

We have the following important technical estimate for these Fourier terms.

Proposition 2.7. Let L ≥ 1 be an integer and choose m ≥ 5 such that 2m−5 ≤ L < 2m−4.
Assume that (aℓ)ℓ∈Z is a sequence such that a0 = 1, a1, . . . , aL−1 ∈ {0, 1} and aℓ = 0 for
ℓ ̸∈ [0, L). For r ≥ 1 and ℓ ≥ 0 let br
ℓ = aℓ−r − aℓ. There exist η > 0 and C such that for all
λ ≥ 0 and r ≥ 1 satisfying 2m ≤ ν2(r) ≤ λ/4, and for all sequences (iℓ)ℓ∈Z satisfying i0 = 0
and 0 ≤ iℓ+1 − iℓ ≤ 1 for 0 ≤ ℓ < L + r − 1 we have
1
2λ ∑

d<2λ max
h<2λ
 ∣
∣
∣G
i,b
r

λ (h, d)
∣
∣
∣2 ≤ C2−ηλ.

This result diﬀers from [7, Proposition 1] in two aspects. First, the maximum over h is inside
the sum over d; second, the sequence br consists of two identical blocks (modulo 2) spaced by r.
The constant as well as the exponent do not depend on the shift r, which will allow us to prove
the quantitative normality result as stated in Theorem 1.

Remark. Combining Proposition 2.7 with the method of proof from [23], we could obtain a
quantitative version of Theorem 0 that diﬀers from our main theorem only in the (worse) bound
c < 4/3.

Finally, we state the following result, which allows replacing ⌊nc⌋ by ⌊nα + β⌋.

Proposition 2.8. Assume that ϕ : N → Ω is a function into a ﬁnite set Ω and assume that
ω = (ω0, . . . , ωL−1) ∈ ΩL, where L ≥ 1 is an integer. We write f (x) = x
c, where 1 < c < 2 is a
real number. Let δ ∈ [0, 1] and deﬁne, for real N, K > 0,

(2.4) J(N, K) = 1
f ′(2N ) − f ′(N )
 ∫ f ′(2N )

f ′(N ) max
f (N )<β≤f (2N )

∣
∣
∣
∣ 1
K
 ∣
∣{
n < K :

ϕ
(
⌊(n + ℓ)α + β⌋) = ωℓ for 0 ≤ ℓ < L}∣
∣ − δ∣
∣
∣
∣ dα.

There exists a constant C such that for all N ≥ 2 and K > 0 we have

(2.5) ∣
∣
∣
∣ 1
N
 ∣
∣
{n ∈ (N, 2N ] : ϕ
(
⌊f (n + ℓ)⌋) = ωℓ for 0 ≤ ℓ < L}∣
∣ − δ∣
∣
∣
∣

≤ C(
f ′′(N )K 2 + (log N )
2

K + J(N, K)
)
.

Results on the distribution of values of an arithmetic function ϕ : N → Ω on Beatty sequences
can therefore be used for proving statements concerning ϕ on Piatetski-Shapiro sequences n ↦→
⌊nc⌋, at least in cases where the shift β does not cause problems. (This is the case for our

8 C. M ¨ULLNER AND L. SPIEGELHOFER

problem concerning t, however, this proposition cannot be used for the original Piatetski-Shapiro
problem, since our knowledge on primes in short intervals is not suﬃcient.) Proposition 2.8
is a modiﬁcation of [22, Proposition 1], which, together with the statement by Fouvry and
Mauduit [10, Th´eor`eme 3 and inequality (1.5)] asserting that
∫ 1

0
 ∏

j<k
∣
∣sin
(
2jπθ)∣
∣ dθ ∼ κλ
k(2.6)

for some κ ∈ R and some λ ∈ (0.6543, 0.6632), enabled the second author to obtain simple
normality of n ↦→ t(⌊nc⌋) for c ≤ 1.42.
The plan of the paper is as follows. In Section 3 we state a number of lemmas. In Section 4 we
show how to prove Theorems 2.1, 2.4 and 1 from Propositions 2.5 and 2.6. Section 5 is concerned
with the proof of Proposition 2.5, while Section 6, which is shorter, proves Proposition 2.6 in
a way that is to a large extent analogous. (This section is shorter because some parts that
have been treated in detail in the ﬁrst proof have been left out. We also note that it would
be possible to unify to a large extent the proofs of Propositions 2.5 and 2.6 by rewriting some
sums as integrals with respect to some measure. However, we refrained from doing so since we
wanted to keep the presentation clear.)
The last two sections are dedicated to the proofs of Propositions 2.7 and 2.8.

3. Lemmas

We begin with the following elementary facts about the functions ⌊·⌋, ∥·∥ and ⟨·⟩, where
⟨x⟩ = ⌊x + 1/2⌋ (the “nearest integer” to x). The (easy) proofs are left to the reader.

Lemma 3.1. Let a, b ∈ R and n ∈ N.

(i) If ∥a∥ < ε and ∥b∥ ≥ ε, then ⌊a + b⌋ = ⟨a⟩ + ⌊b⌋.
(ii) ∥na∥ ≤ n ∥a∥.
(iii) If ∥a∥ < ε and 2nε < 1, then ⟨na⟩ = n ⟨a⟩.

An essential tool in our proofs is the following generalization of van der Corput’s inequality
(see [16, Lemme 17]).

Lemma 3.2. Let I be a ﬁnite interval containing N integers and let an be a complex number
for n ∈ I. For all integers K ≥ 1 and R ≥ 1 we have
∣
∣
∣
∣
∣
∑

n∈I an
∣
∣
∣
∣
∣

2
 ≤ N + K(R − 1)
R
 ∑

|r|<R

(
1 − |r|
R
 ) ∑

n∈I
n+Kr∈I
 an+Kran.

In particular, the right hand side is a nonnegative real number.

The following simple lemma will help us to remove the expression ⌊nα + β⌋, which appears in
our calculations via linear approximation. It introduces the discrepancy of a sequence (modulo 1)
instead.

Lemma 3.3. Let J be an interval in R containing N integers and let α and β be real numbers.
Assume that t, T, k and K are integers such that 0 ≤ t < T and 0 ≤ k < K. Then
∣
∣
∣
∣

{n ∈ J : t
T ≤ {nα + β} < t + 1
T , ⌊nα + β⌋ ≡ k mod K}∣
∣
∣
∣
 = N
KT + O(N DN ( α
K
 ))
,

NORMALITY OF THE THUE–MORSE SEQUENCE 9

where
 DN (α) = sup
0≤x≤1
y∈R
 ∣
∣
∣
∣
∣ 1
N
 ∑

n<N c[0,x)+y+Z(nα) − x

∣
∣
∣
∣
∣.

Proof. We set I = [(T k + t)/(KT ), (T k + t + 1)/(KT )
)
, which is a subinterval of [0, 1) of length
1/(KT ). The two conditions t/T ≤ {nα + β} < (t + 1)/T and ⌊nα + β⌋ ≡ k mod K are satisﬁed
if and only if {nα/K +β/K} ∈ I and the lemma follows by inserting the deﬁnition of DN (α). □

In order to handle the discrepancy (of nα-sequences) thus introduced, we will use average
results as in the following lemma.

Lemma 3.4. Let J be a ﬁnite interval in R containing N integers. Then

(3.1) ∑

k<2ρ
∣
∣
∣
∣
∣

∑

j∈J e( jmk
2ρ
 )∣
∣
∣
∣
∣ ≪ 2ν2(m)N + 2ρ log+N

for all integers ρ ≥ 0 and m ̸= 0. For integers µ ≥ 0 and N ≥ 1 we have

(3.2) ∑

d<2µ DN
 ( d
2µ
 ) ≪ N + 2µ

N (
log+N )2.

Moreover, the estimate

(3.3) ∫ 1

0 DN (α) dα ≪
 (
log+N )2

N
holds. The implied constants in these three estimates are absolute.

Proof. We prove the ﬁrst claim. The estimate is trivial for N ≤ 1. We assume therefore that
N ≥ 2. Let 0 < a ≤ b. We have
∑

a≤k<b
 1
k = ∑

⌊a⌋+1≤k<⌊b⌋
 1
k + O(1) = log(⌊b⌋) − log(⌊a⌋ + 1) + O(1)

≤ log b − log a + O(1).

Therefore we get for all integers ρ ≥ 1
∑

k<2ρ min
{
N, ∥k/2ρ∥−1} = 2 ∑

k<2ρ−1 min{
N, |k/2ρ|−1}

≪ N ∣
∣{
k < 2ρ−1 : k < 2ρ/N }∣
∣ + 2ρ ∑

2ρ/N ≤k<2ρ−1
 1
k

≪ N (1 + 2ρ/N ) + 2ρ(
1 + log 2ρ − log(2ρ/N )
)

≪ N + 2ρ log+N.

This estimate is also valid for ρ = 0. Let 2η | m and 2η+1 ∤ m, that is, ν2(m) = η. If η ≤ ρ, we
have ∑

k<2ρ min{
N, ∥km/2ρ∥
−1} = 2η ∑

k<2ρ−η min{
N, ∥
∥k/2ρ−η∥
∥−1}

≪ 2ηN + 2ρ log+N.

Note that this estimate holds trivially for η > ρ. The statement (3.1) follows therefore from the
inequality ∣
∣
∣
∣
∣

∑

j∈J e(
jmk/2ρ)
∣
∣
∣
∣
∣ ≤ min
{
N, ∥km/2ρ∥−1}
.

10 C. M ¨ULLNER AND L. SPIEGELHOFER

In order to prove the ﬁrst result on the average discrepancy, we use the Erd˝os–Tur´an inequality
and (3.1) and obtain

N ∑

d<2µ DN
 ( d
2µ
 ) ≪ 2µ + ∑

1≤h≤N
 1
h
 ∑

d<2µ
∣
∣
∣
∣
∣
 ∑

n<N e( hnd
2µ
 )∣
∣
∣
∣
∣

≪ 2µ + ∑

ρ≤ log N
log 2
 ∑

1≤h≤N
ν2(h)=ρ
 1
h (
2ρN + 2µ log+N )

≪ 2µ + log+N ∑

ρ≤ log N
log 2
 1
2ρ (2ρN + 2µ log+N )

≪ (
N + 2µ)(
log+N )2.

The proof of the last statement is analogous. □

The following lemma concerning the discrete Fourier transform can easily be proved using
orthogonality relations.

Lemma 3.5. Assume that M ≥ 1 is an integer and that f : Z → C is an M -periodic function.
Then

(3.4) 1
M
 ∑

n<M f (n + t)f (n) = ∑

h<M
∣
∣ ˆf (h)
∣
∣2 e (ht/M ) ,

where ˆf (h) = 1
M
 ∑

u<M f (u) e (−hu/M ) .

We also need the following carry propagation lemma for the sum-of-digits function. State-
ments of this type were used in the articles [16, 17] by Mauduit and Rivat on the sum of digits
of primes and squares.

Lemma 3.6. Let r, L, N, λ be nonnegative integers and α > 0, β ≥ 0 real numbers. Assume
that I is an interval containing N integers. Then
∣
∣{
n ∈ I : ∃ℓ ∈ [0, L) such that s(⌊(n + ℓ + r)α + β⌋) − s(⌊(n + ℓ)α + β⌋)

̸= sλ(⌊(n + ℓ + r)α + β⌋) − sλ(⌊(n + ℓ)α + β⌋)
}∣
∣

≤ (r + L)(N α/2λ + 2).

Proof. Let E = (r + L)α. The statement is trivial for E ≥ 2λ. We assume therefore that
E < 2λ. Moreover, we may assume that L ≥ 1, since the estimate is trivial for L = 0. We ﬁrst
note that if

(3.5) nα + β ∈ [0, 2λ − E) + 2λZ,

then

s(⌊(n + ℓ + r)α + β⌋) − s(⌊(n + ℓ)α + β⌋)
 = sλ(⌊(n + ℓ + r)α + β⌋) − sλ(⌊(n + ℓ)α + β⌋)

for all ℓ < L. This follows easily by studying the binary representation of the arguments: if
hypothesis (3.5) is satisﬁed, then (n + 0)α + β, . . . , (n + L − 1 + r)α + β are contained in an
interval [k2λ, (k + 1)2λ − 1), therefore the digits of ⌊(n + ℓ + r)α + β⌋ and ⌊(n + ℓ)α + β⌋ with
indices ≥ λ are the same, for all ℓ < L. It remains to count the number of exceptions to (3.5).

NORMALITY OF THE THUE–MORSE SEQUENCE 11

For k ∈ Z let ak = min{n : k2λ ≤ nα + β} and bk = min{n : (k + 1)2λ − E ≤ nα + β}.
Then for ak ≤ n < bk we have nα + β ∈ [0, 2λ − E) + 2λZ. It is therefore suﬃcient to count the
number of n ∈ I such that bk ≤ n < ak+1 for some k.
Clearly we have ak+1 − bk = r + L. Assume that I = [a, b) and choose k in such a way that
k2λ ≤ aα + β < (k + 1)2λ. Then ak ≤ a. Moreover (b − 1)α + β < aα + β + (b − a − 1)α <
(k + 1 + (b − a − 1)α/2λ)2λ < (k + ⌊N α2−λ⌋ + 2)2λ, therefore b − 1 < ak+⌊N α2−λ⌋+2. It follows
that the exceptional indices n are contained in one of ⌊N α2−λ⌋ + 2 intervals of length r + L. □

The following standard lemma allows us to extend the range of a summation in exchange for
a controllable factor.

Lemma 3.7. Let x ≤ y ≤ z be real numbers and an ∈ C for x ≤ n < z. Then
∣
∣
∣
∣
∣
∣
 ∑

x≤n<y an
∣
∣
∣
∣
∣
∣ ≤ ∫ 1

0 min {
y − x + 1, ∥ξ∥−1} ∣
∣
∣
∣
∣
∣
 ∑

x≤n<z an e (nξ)

∣
∣
∣
∣
∣
∣ dξ.

Proof. Since ∫ 1
0 e (kξ) dξ = δk,0 for k ∈ Z we have

∑

x≤n<y an = ∑

x≤n<z an ∑

x≤m<y δn−m,0 = ∫ 1

0
 ∑

x≤m<y e (−mξ) ∑

x≤n<z an e (nξ) dξ,

from which the statement follows. □

Let Fn be the Farey series of order n, by which we understand the set of rational numbers
p/q such that 1 ≤ q ≤ n. It is easy to see that each a ∈ Fn has two neighbours aL, aR ∈ Fn,
satisfying aL < a < aR and (aL, a) ∩ F = (a, aR) ∩ F = ∅. We have the following elementary
lemma concerning this set, which follows from the theorems in chapter 3 of the book [12] by
Hardy and Wright.

Lemma 3.8. Assume that a/b, c/d are reduced fractions such that b, d > 0 and a/b < c/d.
Then a/b < (a + c)/(b + d) < c/d. If a/b and c/d are neighbours in Fn, then bc − ad = 1 and
b + d > n, moreover
 (a + c)/(b + d) − a/b < 1
bn
and
 c/d − (a + c)/(b + d) < 1
dn .

We will also use the large sieve inequality, which we state here in the form provided by Selberg
(see for example Montgomery [18, Theorem 3]).

Lemma 3.9 (Selberg). Let N ≥ 1, R ≥ 1 and M be integers, α1, . . . , αR ∈ R and aM+1, . . . ,
aM+N ∈ C. Assume that ∥αr − αs∥ ≥ δ for r ̸= s, where δ > 0. Then

R∑

r=1
 ∣
∣
∣
∣
∣
 M+N∑

n=M+1 an e(nαr)

∣
∣
∣
∣
∣
2
 ≤ (N − 1 + δ−1)
 M+N∑

n=M+1 |an|2 .

4. Reduction of the problem

Before proving Propositions 2.5 and 2.6, we want to show that these results imply Theo-
rems 2.1 and 2.4 respectively.

12 C. M ¨ULLNER AND L. SPIEGELHOFER

4.1. Reducing Theorems 2.1 and 2.4 to Propositions 2.5 and 2.6. We only deduce
Theorem 2.1 from Proposition 2.5. The second implication can be shown in an analogous way.
Assume that the statement of Proposition 2.5 holds for some ρ1, ρ2 such that 0 < ρ1 ≤ ρ2.
Note that we allow ρi ≥ 2 to keep the proof more general. We want to show that in Theorem 2.1
we may choose δ1 = ρ1/(ρ1 + 1) and δ2 = ρ2/(ρ2 + 1). Choosing ρ2 close to 2, justiﬁed by
Proposition 2.5, we see that δ2 approaches 2/3.
For real numbers x, D ≥ 1 we deﬁne

(4.1) S0 = S0(x, D) = ∑

D<d≤2D max
y,z
0≤y≤z
z−y≤x
 max
j∈Z
 ∣
∣
∣
∣Aω(y, z; d, j) − z − y
2Ld
 ∣
∣
∣
∣ .

Let x ≥ 1 and D be real numbers such that x
δ1 ≤ D ≤ x
δ2 . We rewrite the diﬀerence appearing
in S0 to exponential sums, using orthogonality relations:

Aω(y, z; d, j) − z − y
2Ld

= ∑

m,n
y≤m<z
m=nd+j
 { 1 if s((n + ℓ)d + j) ≡ ωℓ mod 2 for ℓ < L
0 otherwise
 } − z − y
2Ld

= ∑

n< z−y
d
 { 1 if s((n + ℓ)d + j + ⌊(y − j)/d⌋ d) ≡ ωℓ mod 2 for ℓ < L
0 otherwise
 }

− z − y
2Ld + O(1)

= 1
2L ∑

a∈{0,1}
L

a̸=(0,...,0)
 e (
− 1
2 (a0ω0 + · · · + aL−1ωL−1)
)

× ∑

n<(z−y)/d e
 ( 1
2
 ∑

ℓ<L aℓs((n + ℓ)d + j + ⌊(y − j)/d⌋ d)

)
 + O(1).

It follows that

S0 ≤ 1
2L ∑

a∈{0,1}
L

a̸=(0,...,0)
 ∑

D≤d<2D max
u≤x max
j≥0
 ∣
∣
∣
∣
∣
∣
 ∑

n<u/d e
 ( 1
2
 ∑

ℓ<L aℓs((n + ℓ)d + j)

)∣
∣
∣
∣
∣
∣ + O(D).

In order to dispose of the maximum over u, we apply Lemma 3.7. We exchange the appearing
integral with the maximum over j and with the sum over d:

(4.2) S0(x, D) ≤ 1
2L ∑

a∈{0,1}
L

a̸=(0,...,0)
 ∫ 1

0 min { x
D + 1, ∥ξ∥
−1}

× ∑

D≤d<2D max
j≥0
 ∣
∣
∣
∣
∣
∣
 ∑

n<x/D e
 ( 1
2
 ∑

ℓ<L aℓs((n + ℓ)d + j)

)
 e (nξ)

∣
∣
∣
∣
∣
∣ dξ + O(D).

Proposition 2.5 therefore implies that there exist a constant C and an exponent η > 0 such that
for all a0, . . . , aL−1 ∈ {0, 1}, not all equal to zero, for all real numbers x, D ≥ 1 satisfying
( x
D
 )ρ1 ≤ D ≤ ( x
D
 )ρ2 ,

NORMALITY OF THE THUE–MORSE SEQUENCE 13

and for all ξ ∈ R we have

(4.3) ∑

D≤d<2D max
j≥0
 ∣
∣
∣
∣
∣
∣
 ∑

n<x/D e
 ( 1
2
 ∑

ℓ<L aℓs((n + ℓ)d + j)

)
 e (nξ)

∣
∣
∣
∣
∣
∣ ≤ CD ( x
D
 )1−η .

The condition on D can be rewritten as x
δ1 ≤ D ≤ x
δ2 . By the estimate
∫ 1

0 min {
A, ∥ξ∥−1} dξ = 2
 (∫ 1/A

0 A dξ + ∫ 1/2

1/A ξ−1 dξ
)
 ≪ log A,

which holds for A ≥ 2, and by (4.2) and (4.3), there exists some η1 > 0 and constants C and
C1 such that for all x, D ≥ 1 satisfying x
δ1 ≤ D ≤ x
δ2 we have

S0(x, D) ≤ Cx ( D
x
 )η log+x + O(D) ≤ C1x
1−η1 ,

which proves the theorem.

4.2. Proving Theorem 1 from Theorem 2.4 and Proposition 2.8. We show the more
general implication that if the statement of Theorem 2.4 holds for some 0 < δ1 ≤ δ2 < 1, then we
may choose c < 2/(2 − δ2) in Theorem 1. Choosing δ2 close to 2/3 yields the desired statement.
We have to ﬁnd an estimate for J(N, K) deﬁned in (2.4). Therefore we calculate:
∣
∣{n < K : s(⌊(n + ℓ)α + β⌋) ≡ ωℓ mod 2 for ℓ < L}∣
∣

= ∣
∣{⌊β⌋ ≤ m < ⌊Kα + β⌋ : ∃n ∈ Z : m = ⌊nα + β⌋,

s(⌊(n + ℓ)α + β⌋) ≡ ωℓ mod 2 for ℓ < L}∣
∣

= ∣
∣{β ≤ m < Kα + β : ∃n ∈ Z : m = ⌊nα + β⌋,

s(⌊(n + ℓ)α + β⌋) ≡ ωℓ mod 2 for ℓ < L}∣
∣ + O(1)

= Aω(β, Kα + β; α, β) + O(1).

We use the deﬁnition (2.4), where we set δ = 2−L, and deﬁne D = f ′(N ). Noting that
f ′(2N ) = 2c−1D ≤ 2D, we obtain

J(N, K) ≤ 1
f ′(2N ) − f ′(N ) 1
K
 ∫ f ′(2N )

f ′(N ) max
β≥0
 ∣
∣
∣
∣Aω(β, Kα + β; α, β)

− Kα + β − β
2Lα
 ∣
∣
∣
∣ dα + O(1/K)

≤ 1
(2c−1 − 1)DK
 ∫ 2D

D max
y,z
0≤y≤z
z−y≤2DK
 max
β≥0
 ∣
∣
∣
∣Aω(y, z; α, β)

− z − y
2Lα
 ∣
∣
∣
∣ dα + O(1/K).

It follows from Theorem 2.4 that for (2DK)
δ1 ≤ D ≤ (2DK)
δ2, that is, for 1
2 D1/δ2−1 ≤ K ≤
1
2 D1/δ1−1, we have
 J(N, K) ≤ C
DK (2DK)
1−η + O(1/K)

for some η > 0 and C depending on c and L. Setting K = 1
2 D1/δ2−1, we obtain

J(N, K) ≤ CD−η/δ2 + 2D1−1/δ2.

14 C. M ¨ULLNER AND L. SPIEGELHOFER

By Proposition 2.8 we get
∣
∣
∣
∣ 1
N
 ∣
∣
{n ∈ (N, 2N ] : s(⌊(n + ℓ)
c⌋) = ωℓ for 0 ≤ ℓ < L}∣
∣ − 1
2L
 ∣
∣
∣
∣

≤ C1
 (
f ′′(N )K 2 + (log N )
2

K + J(N, K)
)

≤ C2
 (
N c−2+2(c−1)(1/δ2−1) + (log N )
2

N (c−1)(1/δ2−1) + N −η(c−1)/δ2 ) .

All of the occurring exponents of N are negative by the conditions c < 2/(2−δ2) and 0 < δ2 < 1,
which proves Theorem 1.
 5. Proof of Proposition 2.5

Assume that L ≥ 1 is an integer, a = (a0, . . . , aL−1) ∈ {0, 1}L and that aℓ = 1 for some ℓ.
It is easy to see, using the shift j, that we may assume a0 = 1. We also assume that N ≥ 1 is
an integer; the general statement follows from the estimate S1(N, D, ξ) − S1(⌊N ⌋ , D, ξ) ≪ D.
Moreover, it is suﬃcient to prove the statement
S1(N, 2ν, ξ)
N 2ν ≤ CN −η

for all integers N, ν ≥ 1 and real numbers D ≥ 1 such that N ρ1 ≤ D ≤ N ρ2 and D < 2ν ≤ 2D.
This can be seen by considering sums (in d) over the intervals [2ν−1, 2ν) and [2ν, 2ν+1) and
using the estimate S1(N, 2ν−1, ξ) ≤ S1(N, 2ν, ξ), which follows from the identity s(2m) = s(m).
Choose η and C according to Proposition 2.7. Moreover, let τ = 2m, where 2m−5 ≤ L < 2m−4,
and λ ≥ 0. By the Cauchy–Schwarz inequality we have

(5.1) |S1(N, 2ν, ξ)|2 ≤ 2ν ∑

2ν ≤d<2ν+1 max
j≥0 S2(N, d, j, ξ),

where
 S2 = S2(N, d, j, ξ) =
 ∣
∣
∣
∣
∣
 ∑

n<N e
 ( 1
2
 ∑

ℓ<L aℓs((n + ℓ)d + j)

)
 e(nξ)

∣
∣
∣
∣
∣
2
 .

We apply Lemma 3.2 (the generalized inequality of van der Corput) with K = 2τ . Let R ≥ 1
be an integer. Then

S2 ≤ N + 2τ (R − 1)
R
 ∑

|r|<R
 (
1 − |r|
R
 ) e(r2τ ξ)

× ∑

0≤n,n+r2τ <N e
 ( 1
2
 ∑

ℓ<L aℓ(
s((n + ℓ + r2τ )d + j) − s((n + ℓ)d + j)
))
 .

Using Lemma 3.6 and treating the summand r = 0 separately, moreover omitting the condition
0 ≤ n + r2τ < N , we obtain for all λ ≥ 0

S2 ≪ O ( N 2

R + N R2τ + N 2 R2τ d
2λ
 )

+ N
R
 ∑

1≤r<R
 ∣
∣
∣
∣
∣
 ∑

n<N e
 ( 1
2
 ∑

ℓ<L aℓ(
sλ((n + ℓ + r2τ )d + j) − sλ((n + ℓ)d + j)
)
)∣
∣
∣
∣
∣

with an implied constant depending only on the block length L. Note that we also replaced
N + (R − 1)2τ by N ; this is clearly admissible if R2τ ≤ N , otherwise we use the trivial estimate
|S2| ≤ N 2 and note the presence of the error term O(N R2τ ).

NORMALITY OF THE THUE–MORSE SEQUENCE 15

We set aℓ to 0 for ℓ ̸∈ {0, . . . , L−1} and deﬁne br
ℓ = aℓ−r2τ −aℓ. Applying the Cauchy–Schwarz
inequality twice and using (5.1) gives

(5.2) |S1(N, 2ν, ξ)|2 ≪ (2ν N )
2O ( 1
R + R2τ 2ν

2λ + R2τ

N
 )

+ 23ν/2N
 

 1
R
 ∑

1≤r<R S3(N, r, λ, ν)




1/2
 ,

where

(5.3) S3(N, r, λ, ν) = ∑

2ν ≤d<2ν+1 max
j≥0
 ∣
∣
∣
∣
∣
 ∑

n<N e
 ( 1
2
 ∑

ℓ∈Z br
ℓsλ((n + ℓ)d + j)

)∣
∣
∣
∣
∣
2
 .

Applying Lemma 3.2 for K = 2µ, we obtain for all integers M ≥ 1 and µ ≥ 0

(5.4)
 ∣
∣
∣
∣
∣
 ∑

n<N e
 ( 1
2
 ∑

ℓ∈Z br
ℓsλ((n + ℓ)d + j)

)∣
∣
∣
∣
∣
2
 ≤ N + 2µ(M − 1)
M
 ∑

|m|<M
 (
1 − |m|
M
 )

× ∑

0≤n,n+m2µ<N e
 ( 1
2
 ∑

ℓ∈Z br
ℓ(sµ,λ((n + ℓ + m2µ)d + j) − sµ,λ((n + ℓ)d + j)
)
)

≪ N |S4| + 2µM N,

where
 S4 = S4(N, M, d, j, r, µ, λ) = 1
M
 ∑

|m|<M
 (
1 − |m|
M
 )

× ∑

n<N e
( 1
2
 ∑

ℓ∈Z br
ℓ
(
sλ−µ
 (⌊ (n + ℓ)d + j
2µ
 ⌋ + md
)

−sλ−µ
 (⌊ (n + ℓ)d + j
2µ
 ⌋)))
.

The replacement of sλ by the two-fold restricted sum-of-digits function sµ,λ, which we performed
in (5.4), is admissible since the arguments diﬀer by a multiple of 2µ and therefore the diﬀerence
does not depend on the lower digits. We obtain

(5.5) S3 ≪ N ∑

2ν ≤d<2ν+1 max
j≥0 |S4| + 2µ+νM N.

The rough idea at this point is to estimate S4 by a nonnegative real number independent of j,
which will allow us to remove the maximum over j and the absolute value appearing in (5.5).
In the following we will work out the details of this process. We want to split the summation
over N into T parts, according to the fractional part of (nd + j)2−µ. Let t, T be integers such
that 0 ≤ t < T . We deﬁne

S5 = S5(N, T, a, d, j, r, m, t, µ, λ)

= ∑

n<N
t
T ≤{ nd+j
2µ }< t+1
T
 e
( 1
2
 ∑

ℓ∈Z br
ℓ
(
sλ−µ
 (⌊ (n + ℓ)d + j
2µ
 ⌋ + md
)

16 C. M ¨ULLNER AND L. SPIEGELHOFER

−sλ−µ
 (⌊ (n + ℓ)d + j
2µ
 ⌋)))
.

We will see that, for most values of d, the values of the ﬂoor function distribute evenly modulo
2λ−µ as n runs through the set deﬁned by the two conditions under the summation sign. For this
to hold, we have to assure that N > 2λ−µ. Inspecting the error terms in (5.2) and (5.5), we see
that we also need 2µ < N and ν < λ in order to get a nontrivial estimate. These observations
ultimately lead to the restriction ρ2 < 2 in Proposition 2.5.
The idea behind the decomposition into T subintervals [t/T, (t+1)/T ) of [0, 1) is the following.
Let At be the set of n such that {(nd + j)/2µ} lies in the t-th interval. Then the diﬀerences
⌊ (n + 1)d + j
2µ
 ⌋ − ⌊ nd + j
2µ
 ⌋ , . . . , ⌊ (n + L − 1)d + j
2µ
 ⌋ − ⌊ nd + j
2µ
 ⌋

should not depend on n ∈ At. This will in fact be the case for most, but not for all, t, so that
we have to take out some t. We deﬁne a set of “good” values,

G = G(T, d, r, µ) = {
t < T : [ t
T + ℓd
2µ , t + 1
T + ℓd
2µ
 ) ∩ Z = ∅

for all ℓ ∈ [0, L) ∪ [r2τ , r2τ + L)
}
.

We have

(5.6) |G| ≥ T − 2L,

since the intervals in the deﬁnition of G(d, T, R, µ) are disjoint and cover an interval of length
1, therefore we have to exclude at most one integer t for each ℓ.
We diﬀerentiate between the cases t ∈ G and t ̸∈ G. For t ̸∈ G we estimate the sum in S5
trivially, that is, we count the number of summands, using Lemma 3.3. We apply this lemma
for K = 2λ−µ (note that we could also take K = 1, however, our choice spares us the separate
treatment of an error term) and multiply with 2λ−µ, which accounts for the 2λ−µ residue classes
we have to collect. We obtain

(5.7) S5 ≪ N
T + 2λ−µN DN
 ( d
2λ
 ) .

Let t ∈ G and assume that t/T ≤ {(nd + j)2−µ} < (t + 1)/T . By the second assumption we
obtain ⌊ nd + j
2µ
 ⌋ + t
T + ℓd
2µ ≤ (n + ℓ)d + j
2µ < ⌊ nd + j
2µ
 ⌋ + t + 1
T + ℓd
2µ

and using the ﬁrst assumption yields
⌊ (n + ℓ)d + j
2µ
 ⌋ = ⌊ nd + j
2µ
 ⌋ + ⌊ t
T + ℓd
2µ
 ⌋

for all ℓ ∈ [0, L) ∪ [r2τ , r2τ + L). For t ∈ G we obtain therefore

S5 = ∑

k<2λ−µ
 ∑

n<N
t
T ≤{ nd+j
2µ }< t+1
T
⌊ nd+j
2µ ⌋≡k mod 2
λ−µ
 e
( 1
2
 ∑

ℓ∈Z br
ℓ
 (
sλ−µ
 (
k + ⌊ t
T + ℓd
2µ
 ⌋ + md
)

− sλ−µ
 (
k + ⌊ t
T + ℓd
2µ
 ⌋)))

NORMALITY OF THE THUE–MORSE SEQUENCE 17

Since the summand does not depend on n, we count the number of times the three conditions
under the second summation sign are satisﬁed. To this end, we use again Lemma 3.3 with
K = 2λ−µ. We obtain for t ∈ G

(5.8) S5 = N
2λ−µT
 ∑

k<2λ−µ e
( 1
2
 ∑

ℓ∈Z br
ℓ
(
sλ−µ
 (
k + ⌊ t
T + ℓd
2µ
 ⌋ + md
)

− sλ−µ
 (
k + ⌊ t
T + ℓd
2µ
 ⌋)))
 + O (
2λ−µN DN
 ( d
2λ
 )) .

Note that this expression is independent of the shift j. Moreover, as we noted earlier, we see
that it is necessary that we have N ≥ 2λ−µ in order to get a useful result, since the error term
would be too large otherwise. Setting

id,t
ℓ = ⌊ t
T + ℓ { d
2µ
 }⌋ ,

we get the almost trivial identity ⌊ t
T + ℓd
2µ
 ⌋ = ℓ ⌊ d
2µ
 ⌋ + id,t
ℓ .

In Lemma 3.5 we set t = md and

f (n) = e
 ( 1
2
 ∑

ℓ∈Z br
ℓsλ−µ
 (
n + ℓ ⌊ d
2µ
 ⌋ + id,t
ℓ
 ))

and obtain for t ∈ G

(5.9) S5 = N
T
 ∑

h<2λ−µ
 ∣
∣
∣
∣G
i
d,t,b
r

λ−µ
 (h, ⌊ d
2µ
 ⌋)∣
∣
∣
∣
2 e ( hmd
2λ−µ
 ) + O (
2λ−µN DN
 ( d
2λ
 )) ,

where the Fourier coeﬃcients G(h, d) are deﬁned by (2.3). By the deﬁnitions of S4 and S5 we
have

(5.10) S4 = 1
M
 ∑

|m|<M
 (
1 − |m|
M
 ) ∑

t<T S5.

Using (5.6), (5.7), (5.9) and (5.10) we obtain

(5.11) S4 = N
T
 ∑

t<T
 1
M
 ∑

|m|<M
 (
1 − |m|
M
 ) ∑

h<2λ−µ
 ∣
∣
∣
∣G
i
d,t,b
r

λ−µ
 (
h, ⌊ d
2µ
 ⌋)∣
∣
∣
∣
2 e ( hmd
2λ−µ
 )

+ O (
N L
T + 2λ−µT N DN
 ( d
2λ
 )) ,

where the reinsertion of the indices t ̸∈ G is accounted for by the error term N L/T , which can
be seen using Parseval’s identity.
Note the important fact that the right hand side gives an estimate for S4 that is independent
of the shift j (that is, independent of the residue class modulo d). Using also the nonnegativity
of the main term, which follows from the elementary identity

∑

|m|<M(M − |m|) e(mx) =
 ∣
∣
∣
∣
∣
 ∑

m<M e(mx)

∣
∣
∣
∣
∣
2
 ,

we may remove the maximum together with the absolute value in (5.5) while keeping the im-
portant factor e (
hmd/2λ−µ) in (5.11). We obtain, treating the summand m = 0 separately,

18 C. M ¨ULLNER AND L. SPIEGELHOFER

(5.12) S3 ≪ N 2

T
 ∑

t<T
 1
M
 ∑

1≤|m|<M
 (
1 − |m|
M
 ) S6

+ 2νN 2O
( 1
M + 2µM
N + L
T + 2λ−µT 1
2ν ∑

d<2ν+1 DN
 ( d
2λ
 ))
,

where
(5.13) S6 = S6(d, r, m, t, λ, µ, ν)
 = ∑

2ν ≤d<2ν+1
 ∑

h<2λ−µ
 ∣
∣
∣
∣G
i
d,t,b
r

λ−µ
 (
h, ⌊ d
2µ
 ⌋)∣
∣
∣
∣
2 e ( hmd
2λ−µ
 ) .

We want to show that S6 is substantially smaller than 2ν (which is a trivial upper bound by
Parseval’s identity). In order to estimate the right hand side of (5.13), we note that the ﬁrst
factor depends only in a weak way on d. We state this more precisely in the following.
The term ⌊d/2µ⌋ does not depend on the lowest µ binary digits of d. Moreover, we want to
decompose [0, 2µ) into few intervals I r,t
u in such a way that the values id,t
ℓ , where ℓ ∈ M and
M = [0, L) ∪ [r2τ , r2τ + L), are constant for d ∈ I r,t
u . (Note that the indices ℓ ̸∈ M are not of
interest, since br
ℓ = 0 for these.)
Let t < T be given. We deﬁne the (lexicographical) order on NM by (iℓ)ℓ∈M < (jℓ)ℓ∈M if
and only if iℓ ̸= jℓ for some ℓ ∈ M and iℓ < jℓ for ℓ = min{k ∈ M : ik ̸= jk}. It is easy to check
that the assignment
 d ↦→ id,t |M

is 2µ-periodic and nondecreasing for d < 2µ with respect to this total ordering. It follows that
the set {0, . . . , 2µ − 1} decomposes into intervals I r,t
0 , . . . , I r,t
U−1 such that the same sequence
(
id,t
ℓ )

ℓ∈M is deﬁned for each d ∈ I r,t
u + 2µZ. By the property 0 ≤ ir,t
ℓ+1 − ir,t
ℓ ≤ 1, the number U
of intervals thus deﬁned satisﬁes

(5.14) U ≤ 22L(r2τ − L) ≤ r22L+τ .

From (5.13), we obtain sums of the form
∑

d∈I r,t
u +2µk e (
hmd/2λ−µ)

for u < U and some k ∈ Z. Using also the estimate for the Fourier coeﬃcients Gλ−µ from
Proposition 2.7, we will estimate S6 nontrivially.
Let I = IL+r2τ −1 be the set of sequences i0, . . . , iL+r2τ −1 such that i0 = 0 and 0 ≤ iℓ+1 −iℓ ≤
1 for 0 ≤ ℓ < L + r2τ − 1. Assume that m ̸= 0 and λ ≥ ν ≥ µ. Writing d = d1 + 2µd2, and
choosing iu such that iu = id1,t for all d1 ∈ I r,t
u , we obtain

∣
∣S6∣
∣ =
 ∣
∣
∣
∣
∣
∣
 ∑

u<U
 ∑

d1∈I r,t
u
 ∑

d2<2ν−µ
 ∑

h<2λ−µ
 ∣
∣
∣G
i
d1 ,t,b
r

λ−µ (h, d2)
∣
∣
∣
2 e ( hm(d1 + d22µ)
2λ−µ
 )
∣
∣
∣
∣
∣
∣

=
 ∣
∣
∣
∣
∣
∣
 ∑

u<U
 ∑

d2<2ν−µ
 ∑

h<2λ−µ
 ∣
∣
∣G
iu,b
r

λ−µ (h, d2)
∣
∣
∣2 ∑

d1∈I r,t
u e ( hm(d1 + d22µ)
2λ−µ
 )
∣
∣
∣
∣
∣
∣

≤ ∑

u<U max
i∈I
 ∑

d2,h<2λ−µ
 ∣
∣
∣G
i,b
r

λ−µ (h, d2)
∣
∣
∣2 ∣
∣
∣
∣
∣
∣
 ∑

d1∈I r,t
u e ( hmd1
2λ−µ
 )
∣
∣
∣
∣
∣
∣ .

NORMALITY OF THE THUE–MORSE SEQUENCE 19

We apply the Cauchy–Schwarz inequality to the sum over h and d2 and obtain with the help of
Parseval’s identity

∣
∣S6∣
∣ ≤ ∑

u<U max
i∈I
 

 ∑

d2,h<2λ−µ
 ∣
∣
∣G
i,b
r

λ−µ(h, d2)
∣
∣
∣4


1/2

×
 


 ∑

d2,h<2λ−µ
 ∣
∣
∣
∣
∣
∣
 ∑

d1∈I r,t
u e ( hmd1
2λ−µ
 )
∣
∣
∣
∣
∣
∣

2




1/2

≤ 2(λ−µ)/2 max
i∈I
 

 ∑

d2<2λ−µ max
h<2λ−µ
 ∣
∣
∣G
i,b
r

λ−µ(h, d2)
∣
∣
∣2


1/2

(5.15)
 × ∑

u<U
 


 ∑

h<2λ−µ
 ∣
∣
∣
∣
∣
∣
 ∑

k<2λ−µ au
k e ( hk
2λ−µ
 )
∣
∣
∣
∣
∣
∣

2




1/2
,

where au
k = au,r,t,m
k = ∣
∣{d1 ∈ I r,t
u : d1m ≡ k mod 2λ−µ}∣
∣ .

In order to estimate the sum over d2 in (5.15), we use Proposition 2.7: there exist η > 0 and C,
which only depend on L, such that for all λ ≥ µ ≥ 0 and all r ≥ 1 satisfying ν2(r)+τ ≤ (λ−µ)/4
we have

(5.16) max
i∈I
 

 ∑

d2<2λ−µ max
h<2λ−µ
 ∣
∣
∣G
i,b
r

λ−µ(h, d2)
∣
∣
∣2


1/2
 ≤ C2(1−η)(λ−µ)/2.

The sum over h in (5.15) can be estimated by Lemma 3.9 (the large sieve inequality) and the
estimate
 au,r,t,m
k ≤
 {2ν2(m) µ ≤ λ − µ
2ν2(m)2µ/2λ−µ µ > λ − µ

(which is clear for odd m and follows easily by the decomposition m = m02ν2(m) otherwise).
This gives

(5.17)
 


 ∑

h<2λ−µ
 ∣
∣
∣
∣
∣
∣
 ∑

k<2λ−µ au,r,t,m
k e ( hk
2λ−µ
 )
∣
∣
∣
∣
∣
∣
2



1/2
 ≪
 

2λ−µ ∑

k<2λ−µ
∣
∣au,r,t,m
k ∣
∣2


1/2

≪ 2λ−µ2ν2(m) max{1, 22µ−λ}.

Combining (5.16), (5.17) and (5.14), we get

|S6| ≪ r22L+τ 2ν2(m) max{1, 22µ−λ}2(2−η/2)(λ−µ)

≪ r2ν2(m) max{1, 22µ−λ}2(2−η/2)(λ−µ).

with an implied constant depending only on L. We translate this estimate back to an estimate
for S1. By the estimate ∑

1≤m<M 2ν2(m) ≪ M log M

20 C. M ¨ULLNER AND L. SPIEGELHOFER

valid for M ≥ 1, which is easy to show by splitting the summation according to the value of
ν2(m), we obtain

(5.18) 1
RM
 ∑

1≤r<R
 ∑

1≤|m|<M
 (
1 − |m|
M
 ) S6 ≪ R log M max{1, 22µ−λ}2(2−η/2)(λ−µ).

We collect the error terms, using (5.2), (5.12) and (5.18) and use the discrepancy estimate (3.2),
obtaining

(5.19) ∣
∣
∣
∣ S1(N, 2ν, ξ)
N 2ν
 ∣
∣
∣
∣
4 ≤ C( 1
R2 + ( R2ν

2λ
 )2 + ( R
N
 )2 + 1
M + 2µM
N + 1
T

+ T 2λ−µ

N N + 2λ

2ν (
log+N )2 + R2(2−η/2)(λ−µ)−ν log M max{1, 22µ−λ})

with a constant C depending only on L. This estimate is valid for all integers M, N, R, T ≥ 1
and λ, µ, ν ≥ 0 such that µ ≤ ν < ν + 1 ≤ λ and R2τ ≤ 2(λ−µ)/4, and for all real numbers
ξ. Moreover, this estimate also holds for real-valued parameters M, R, T, λ, µ satisfying these
restrictions (with a possibly diﬀerent constant C). In order to ﬁnish the proof of Proposition 2.5,
we have to choose the parameters M, R, T, λ and µ, depending on N and D. Let 0 < ρ1 ≤ ρ2 < 2
be given and choose θ and ε in such a way that

max
{
1, ρ2, 3ρ2
1 + ρ2 , 2 − η/2} < θ < 2

and
 0 < ε < min
{
2 − θ, θ/ρ2 − 1, θ − 1, θ 1 + ρ2
ρ2 − 3, θ − (2 − η/2), 1/4}
.

Assume that D ≥ 1 is a real number and that N, ν ≥ 1 are integers such that N ρ1 ≤ D ≤ N ρ2
and D < 2ν ≤ 2D. Set µ = ν/θ, λ = 2µ and R = M = T = 2εµ. Using these choices it is not
diﬃcult to check, proceeding term by term, that

S1(N, 2ν , ξ)
N 2ν ≤ C2−νη1(
log+N )2

for some C and η1 > 0 depending only on ρ2 and L. Finally, we insert the lower bound N ρ1 ≤ 2ν

(so far we did not use ρ1), which completes the proof of Proposition 2.5.

6. Proof of Proposition 2.6

We follow the proof of Proposition 2.5 and start, without loss of generality, with the same
assumptions. Assume that L ≥ 1 is an integer, a0 = 1 and a1, . . . , aL−1 ∈ {0, 1}. Choose m ≥ 5
such that 2m−5 ≤ L < 2m−4 and set τ = 2m. Assume that D, N, ν ≥ 1, where N and ν are
integers satisfying N ρ1 ≤ N ≤ N ρ2 and D < 2ν ≤ 2D.
We apply van der Corput’s inequality for K = 2τ and obtain, in analogy to (5.2),

(6.1) ∣
∣
∣ ˜S1∣
∣
∣2 ≪ (2νN )
2O ( 1
R + R2τ 2ν

2λ + R2τ

N
 )
 + 23ν/2N
 

 1
R
 ∑

1≤r<R ˜S3(N, r, λ, ν)




1/2
 ,

where

(6.2) ˜S3(N, r, λ, ν) = ∫ 2
ν+1

2ν max
β≥0
 ∣
∣
∣
∣
∣
 ∑

n<N e
 ( 1
2
 ∑

ℓ∈Z br
ℓ sλ (⌊(n + ℓ)α + β⌋)

)∣
∣
∣
∣
∣

2
 dα

NORMALITY OF THE THUE–MORSE SEQUENCE 21

and br
ℓ = aℓ−r2τ − aℓ, and aℓ is assumed to be zero for ℓ ̸∈ [0, L). The estimate (6.1) is valid for
N, R ≥ 1 and λ, ν ≥ 0.
Next we want to “cut oﬀ” the µ lowest digits, that is, replace sλ by sµ,λ. This was accom-
plished by a simple application of Lemma 3.2, setting K = 2µ, in the proof of Proposition 2.5.
Since we are now considering Beatty sequences (having in general non-integer step length α),
we need to modify our strategy. To do so, we use Diophantine approximation, more precisely,
Farey series. Let α ∈ R be given. We assign a fraction p(α)/q(α) to α according to the Farey
dissection of the circle: consider reduced fractions a/b < c/d that are neighbours in the Farey
series F2µ+σ , where σ ≥ 1 is chosen later, such that a/b ≤ α/2µ < c/d. If α/2µ < (a + c)/(b + d),
then set p(α) = a and q(α) = b, otherwise set p(α) = c and q(α) = d. Lemma 3.8 implies

(6.3) ∣
∣q(α)α − p(α)2µ∣
∣ < 2−σ.

Applying Lemma 3.2 with K = q(α) and noting that q(α) ≤ 2µ+σ, we obtain for all integers
M ≥ 1 and µ ≥ 0

(6.4)
 ∣
∣
∣
∣
∣
 ∑

n<N e
 ( 1
2
 ∑

ℓ∈Z br
ℓsλ (⌊(n + ℓ)α + β⌋)
)∣
∣
∣
∣
∣

2

≪ O(2µ+σM N ) + N
M
 ∑

|m|<M
 (
1 − |m|
M
 )

× ∑

n<N e
 ( 1
2
 ∑

ℓ∈Z br
ℓ(
sλ (⌊(n + ℓ + m q(α))α + β⌋) − sλ (⌊(n + ℓ)α + β⌋))
)
 .

In order to reduce this expression to a sum analogous to S4, we want to shift the expression
m q(α)α out of the ﬂoor function. To this end, we use (6.3) and the argument that m q(α)α
is close to an integer, while (n + ℓ)α + β usually is not. This can be made precise as follows.
Assume that

(6.5) ∥(n + ℓ)α + β∥ ≥ M/2σ

and that 2M < 2σ. Using part (iii) of Lemma 3.1 with ε = 1/2σ and (6.3), moreover noting
that σ ≥ 1, we obtain ⟨m q(α)α⟩ = m ⟨q(α)α⟩ = m p(α)2µ.
Applying part (i) of Lemma 3.1, setting ε = M/2σ, we see that (6.5) implies

(6.6) ⌊(n + ℓ + m q(α))α + β⌋ = m p(α)2µ + ⌊(n + ℓ)α + β⌋ .

The number of n where hypothesis (6.5) fails for some ℓ can be estimated by discrepancy
estimates for {nα}-sequences: for all positive integers N and 2M < 2σ we have

(6.7)
 ∣
∣{
n < N : ∥(n + ℓ)α + β∥ ≤ M/2σ}∣
∣

= ∣
∣{
n < N : (n + ℓ)α + β ∈ [−M/2σ, M/2σ] + Z
}∣
∣

= ∣
∣{
n < N : nα ∈ [0, 2M/2σ] − β − ℓα − M/2σ + Z
}∣
∣

≤ N DN (α) + 2M N/2σ.

Multiplying this error by 2L (which is O(1) according to our conventions stated in the introduc-
tion), we obtain an upper bound for the number of n < N such that ∥(n + ℓ)α + β∥ ≤ M/2σ for
some ℓ ∈ [0, L) ∪ [r2τ , r2τ + L). Treating these integers separately and using (6.4) through (6.7),
we obtain

(6.8)
 ∣
∣
∣
∣
∣
 ∑

n<N e
 ( 1
2
 ∑

ℓ∈Z br
ℓsλ (⌊(n + ℓ)α + β⌋)
)∣
∣
∣
∣
∣

2

22 C. M ¨ULLNER AND L. SPIEGELHOFER

≪ N ∣
∣ ˜S4∣
∣ + O(2µ+σN M + N 2DN (α) + N 2M/2σ)
,

where
 ˜S4 = ˜S4(N, M, α, β, r, µ, λ) = 1
M
 ∑

|m|<M
 (
1 − |m|
M
 )

× ∑

n<N e
( 1
2
 ∑

ℓ∈Z br
ℓ
(
sλ−µ
 (⌊ (n + ℓ)α + β
2µ
 ⌋ + m p(α)
)

−sλ−µ
 (⌊ (n + ℓ)α + β
2µ
 ⌋)))
.

Note that (6.8) is, except for the error terms, completely analogous to equation (5.4) in the
proof of Proposition 2.5. From (6.2) and (6.8) we get

(6.9) ˜S3(N, r, λ, ν) ≪ N ∫ 2
ν+1

2ν max
β≥0 ∣
∣ ˜S4∣
∣ dα + N 2 ∫ 2
ν+1

2ν DN (α) dα

+ 2µ+σ+ν M N + N 22νM/2σ.

Let t, T be integers such that 0 ≤ t < T and deﬁne

˜S5 = ∑

n<N
t
T ≤{ nα+β
2µ }< t+1
T
 e
 ( 1
2
 ∑

ℓ∈Z br
ℓ
(
sλ−µ
 (⌊ (n + ℓ)α + β
2µ
 ⌋ + m p(α)
)

− sλ−µ
 (⌊ (n + ℓ)α + β
2µ
 ⌋)))

and

G = G(T, α, r, µ) = {
t < T : [ t
T + ℓα
2µ , t + 1
T + ℓα
2µ
 ) ∩ Z = ∅

for all ℓ ∈ [0, L) ∪ [r2τ , r2τ + L)
}
.

Again, we have

(6.10) G ≥ T − 2L

and we distinguish between the cases t ∈ G and t ̸∈ G. For t ̸∈ G we estimate ˜S5 trivially,
applying Lemma 3.3 with K = 2λ−µ. We obtain

(6.11) ˜S5 ≪ N
T + 2λ−µN DN ( α
2λ
 ) .

Let t ∈ G and assume that t/T ≤ {(nα + β)2−µ} < (t + 1)/T . Then, as before,
⌊ (n + ℓ)α + β
2µ
 ⌋ = ⌊ nα + β
2µ
 ⌋ + ⌊ t
T + ℓα
2µ
 ⌋

for ℓ ∈ [0, L) ∪ [r2τ , r2τ + L). For t ∈ G we obtain

˜S5 = ∑

k<2λ−µ
 ∑

n<N
t
T ≤{ nα+β
2µ }< t+1
T
⌊ nα+β
2µ ⌋≡k mod 2
λ−µ
 e
( 1
2
 ∑

ℓ∈Z br
ℓ
(
sλ−µ
 (
k + ⌊ t
T + ℓα
2µ
 ⌋ + m p(α)
)

NORMALITY OF THE THUE–MORSE SEQUENCE 23

− sλ−µ
 (
k + ⌊ t
T + ℓα
2µ
 ⌋)))
.

We apply Lemma 3.3, setting K = 2λ−µ, and obtain for t ∈ G

(6.12) ˜S5 = N
2λ−µT
 ∑

k<2λ−µ e
( 1
2
 ∑

ℓ∈Z br
ℓ
 (
sλ−µ
 (k + ⌊ t
T + ℓα
2µ
 ⌋ + m p(α)
)

− sλ−µ
 (
k + ⌊ t
T + ℓα
2µ
 ⌋) ))
 + O (2λ−µN DN ( α
2λ
 )) .

Setting
 iα,t
ℓ = ⌊ t
T + ℓ { α
2µ
 }⌋ ,

we have ⌊ t
T + ℓα
2µ
 ⌋ = ℓ ⌊ α
2µ
 ⌋ + iα,t
ℓ .

In Lemma 3.5 we set t = m p(α) and

f (n) = e
 ( 1
2
 ∑

ℓ∈Z br
ℓ sλ−µ (n + ℓ ⌊ α
2µ
 ⌋ + iα,t
ℓ ))

and obtain for t ∈ G

(6.13) ˜S5 = N
T
 ∑

h<2λ−µ
 ∣
∣
∣G
i
α,t,b
r

λ−µ (
h, ⌊ α
2µ
 ⌋)∣
∣
∣2 e ( hm p(α)
2λ−µ
 ) + O (2λ−µN DN ( α
2λ
 )) .

Using the identity
 ˜S4 = 1
M
 ∑

|m|<M
 (
1 − |m|
M
 ) ∑

t<T ˜S5

as well as (6.10), (6.11) and (6.13), we obtain, in analogy to (5.11),

˜S4 = N
T
 ∑

t<T
 1
M
 ∑

|m|<M
 (
1 − |m|
M
 )

× ∑

h<2λ−µ
 ∣
∣
∣G
i
α,t,b
r

λ−µ (h, ⌊ α
2µ
 ⌋)∣
∣
∣
2 e ( hm p(α)
2λ−µ
 )
(6.14)
 + O ( N
T + 2λ−µT N DN ( α
2λ
 )) .

From (6.9) and (6.14), treating the summand for m = 0 separately, we get

(6.15) ˜S3 ≪ N 2

T
 ∑

t<T
 1
M
 ∑

1≤|m|<M
 (
1 − |m|
M
 ) ˜S6 + 2νN 2 O
( 1
M + 2µ+σM
N

+ 1
T + 2λ−µT
2ν
 ∫ 2
ν+1

2ν DN ( α
2λ
 ) dα + 1
2ν
 ∫ 2
ν+1

2ν DN (α) dα + M
2σ
 )
,

where

˜S6 = ˜S6(α, r, m, t, λ, µ, ν)

24 C. M ¨ULLNER AND L. SPIEGELHOFER

= ∫ 2
ν+1

2ν
 ∑

h<2λ−µ
 ∣
∣
∣G
i
α,t,b
r

λ−µ (h, ⌊ α
2µ
 ⌋)∣
∣
∣2 e ( hm p(α)
2λ−µ
 ) dα.

As in the proof of Proposition 2.5 we obtain intervals I r,t
0 , . . . , I r,t
U−1 ⊆ R, where U ≤ r22L+τ ,
such that α ↦→ iα,t |M is constant on each I r,t
u . Deﬁne I as before, that is, as the set of sequences
(iℓ)ℓ<L+r2τ −1 such that 0 ≤ iℓ+1 − iℓ ≤ 1 for 0 ≤ i < L + r2τ − 1. Moreover, we assume from
now on that m ̸= 0 and λ ≥ ν ≥ µ. We obtain, applying the Cauchy–Schwarz inequality to the
sum over (h, d2),

∣
∣ ˜S6∣
∣ =
 ∣
∣
∣
∣
∣
∣
 ∑

u<U
 ∫

I r,t
u
 ∑

d2<2ν−µ
 ∑

h<2λ−µ
 ∣
∣
∣G
i
α,t,b
r

λ−µ (h, d2)
∣
∣
∣2 e ( hm p(α + d22µ)
2λ−µ
 ) dα

∣
∣
∣
∣
∣
∣

≤ ∑

u<U max
i∈I
 ∑

d2<2λ−µ
 ∑

h<2λ−µ
 ∣
∣
∣G
i,b
r

λ−µ(h, d2)
∣
∣
∣2 ∣
∣
∣
∣

∫
I r,t
u e ( hm p(α + d22µ)
2λ−µ
 ) dα
∣
∣
∣
∣

≤ ∑

u<U max
i∈I
 

 ∑

d2,h<2λ−µ
 ∣
∣
∣G
i,b
r

λ−µ(h, d2)
∣
∣
∣4


1/2

×
 

 ∑

d2,h<2λ−µ
 ∣
∣
∣
∣

∫

I r,t
u e ( hm p(α + d2 2µ)
2λ−µ
 ) dα
∣
∣
∣
∣
2


1/2

≤ max
i∈I
 

 ∑

d2<2λ−µ max
h<2λ−µ
 ∣
∣
∣G
i,b
r

λ−µ(h, d2)
∣
∣
∣2


1/2

× ∑

u<U
 


 ∑

d,h<2λ−µ
 ∣
∣
∣
∣
∣
∣
 ∑

k<2λ−µ au,d
k e ( hk
2λ−µ
 )
∣
∣
∣
∣
∣
∣
2



1/2
,

where au,d
k = ar,m,t,u,d,µ,λ
k = λ (
{α ∈ I r,t
u : m p(α + d 2µ) ≡ k mod 2λ−µ}) ,

and λ denotes the Lebesgue measure. Assume that r2τ ≤ 2(λ−µ)/4. Then, using Proposition 2.7,
the ﬁrst factor can be estimated by C2(1−η)(λ−µ)/2. The second factor can be estimated by the
large sieve inequality (Lemma 3.9) and |U | ≪ r, which yields

∣
∣ ˜S6∣
∣ ≪ r 2(1−η)(λ−µ)/2 max
u<U
 

 ∑

d<2λ−µ 2λ−µ ∑

k<2λ−µ
 ∣
∣
∣au,d
k ∣
∣
∣
2



1/2
 .

It remains to ﬁnd estimates for au,d
k . In order to do so, we ﬁrst note that

(6.16) q(α + d 2µ) = q(α)

p(α + d 2µ) = p(α) + q(α)d

for all d ∈ N. Lemma 3.8 implies

(6.17) λ ({α ∈ [0, 2µ) : p(α) = p, q(α) = q}) ≤ 2 2µ

2µ+σq .

Formulas (6.17) and (6.16) together with the estimate
∣
∣{p < 2µ+σ : mp ≡ k mod 2λ−µ}∣
∣ ≤ 2ν2(m) max{1, 22µ−λ+σ}

NORMALITY OF THE THUE–MORSE SEQUENCE 25

imply
 λ (
{α ∈ [0, 2µ) : m p(α + d 2µ) ≡ k mod 2λ−µ, q(α + d 2µ) = q})

= λ (
{α ∈ [0, 2µ) : m p(α) ≡ k − d q mod 2λ−µ, q(α) = q})

≤ 2ν2(m) max{1, 22µ−λ+σ} 2
2σq

By a summation over q ≤ 2µ+σ we obtain

au,d
k ≪ 2ν2(m) max{1, 22µ−λ+σ}(µ + σ)/2σ.

Therefore ∣
∣ ˜S6∣
∣ ≪ R2ν2(m)(µ + σ) 2(2−η′)(λ−µ) max{2−σ, 22µ−λ},

which leads to

(6.18)
 1
RM
 ∑

1≤r<R
 ∑

1≤|m|<M
 (
1 − |m|
M
 ) ˜S6

≪ R log M (µ + σ) 2(2−η′)(λ−µ) max{2−σ, 22µ−λ}.

By analogous reasoning as in the proof of Proposition 2.6, leading to (5.19), and using (6.1),
(6.15) and (6.18) and the estimate for the integral mean of the discrepancy (Lemma 3.4), we
obtain
∣
∣
∣
∣
∣
 ˜S1(N, ν, ξ)
N 2ν
 ∣
∣
∣
∣
∣

4
 ≪ 1
R2 + ( R2ν+τ

2λ
 )2 + ( R2τ

N
 )2 + 1
M + 2µ+σM
N + 1
T + M
2σ

+ T 2λ−µ

N
 (
log+N )2 + R log M (µ + σ)2(2−η′)(λ−µ)+2µ−λ−ν

for all integers T, R, M, N, σ ≥ 1 and λ, µ, ν ≥ 0 such that µ ≤ ν ≤ λ ≤ 2ν, 2M < 2σ,
R2τ ≤ 2(λ−µ)/4 and for all ξ ∈ R. An analogous argument as in the proof of Proposition 2.5
ﬁnishes the proof.
 7. Proof of Proposition 2.7

7.1. A recurrence for Fourier coeﬃcients. In order to get started with the proof of Propo-
sition 2.7, we recall the deﬁnition of the discrete Fourier coeﬃcients G
i,b
λ (h, d), which is equa-
tion (2.3). For nonnegative integers d and λ, for sequences i : N → N (for notational reasons we
use, in this section, the function notation i(ℓ) to denote the ℓ-th element) and b : N → Z, where
b has ﬁnite support, and for h ∈ Z we have

G
i,b
λ (h, d) = 1
2λ ∑

u<2λ e
 

 1
2
 ∑

ℓ≥0 bℓsλ(u + ℓd + i(ℓ)) − hu
2λ
 

 .

For any K ≥ 0, we denote by IK the set of sequences i : N → N with support in [0, K) such
that i(ℓ + 1) − i(ℓ) ∈ {0, 1} for 0 ≤ ℓ < K − 1. For (δ, ε) ∈ {0, 1}2, we deﬁne a transformation
Tδ,ε : IK → IK by
 Tδ,ε(i)(ℓ) = ⌊ i(ℓ) + ℓδ + ε
2
 ⌋

for 0 ≤ ℓ < K. Note that this transformation is well-deﬁned. We also deﬁne weights by

f i,b
δ,ε = e
 ( 1
2
 ∑

ℓ<K bℓ(i(ℓ) + ℓδ + ε)

)
 .

26 C. M ¨ULLNER AND L. SPIEGELHOFER

These quantities appear in the following recurrence for the discrete Fourier coeﬃcients, com-
pare [7, Lemma 13].

Lemma 7.1. Assume that b : N → Z and i ∈ IK. Then for all integers d, λ ≥ 0 and h, and
ε ∈ {0, 1} we have

(7.1) G
i,b
λ (h, 2d + δ) = 1
2
 1∑

ε=0 e (
− hε
2λ
 ) f i,b
δ,ε G
Tδ,ε(i),b
λ−1 (h, d).

Proof. By splitting the sum in the deﬁnition of G
i,b
λ (h, d) according to the parity of u, we obtain
(writing ε0(n) for the lowest binary digit of n)

G
i,b
λ (h, 2d + δ)

= 1
2λ
 1∑

ε=0
 ∑

u<2λ−1 e
 ( 1
2
 ∑

ℓ<K bℓsλ(2u + ε + ℓ(2d + δ) + i(ℓ)) − h(2u + ε)2−λ)

= 1
2λ
 1∑

ε=0 e (− hε
2λ
 ) ∑

u<2λ−1 e
 ( 1
2
 ∑

ℓ<K bℓ
(
sλ−1
 (
u + ℓd + ⌊ i(ℓ) + ℓδ + ε
2
 ⌋)

+ε0(i(ℓ) + ℓδ + ε)
) − hu2λ−1)

= 1
2
 1∑

ε=0 e (
− hε
2λ
 ) f i,b
δ,ε G
Tδ,ε(i),b
λ−1 (h, d).
 □

We want to study compositions of elementary transformations Tδ,ε. We therefore extend
this notation as follows. Assume that d, e, m ≥ 0 are integers. For d, e < 2m, we deﬁne
T (m)
d,e : IK → IK by setting, for i ∈ IK and ℓ < K,

(7.2) T (m)
d,e (i)(ℓ) = ⌊ i(ℓ) + ℓd + e
2m
 ⌋ .

For general integers d, e ≥ 0 we set

T (m)
d,e = T (m)
d mod 2m, e mod 2m.

Note that we have

(7.3) T (m)
d,0 (i)(ℓ) ≤ T (m)
d,e (i)(ℓ) ≤ T (m)
d,0 (i)(ℓ) + 1

for all e ≥ 0. By a straightforward induction it follows that

(7.4) T (m)
d,e = Tδm−1,εm−1 ◦ · · · ◦ Tδ0,ε0 ,

for m ≥ 1, where ∑i≥0 δi2i and ∑
i≥0 εi2i are the binary expansions of d and e respectively.

Moreover, T (0)
d,e is the identity on IK. We also deﬁne, generalizing the notation f i,b
δ,ε,

(7.5) f (m),i,b
d,e = f T (m−1)
d,e (i),b
δm−1,εm−1 · · · f T (1)
d,e (i),b
δ1,ε1 · f i,b
δ0,ε0.

In order to obtain a recurrence relation for |G
i,b
λ (h, d)|2, we deﬁne

Φi1,i2,b
λ (h, d) = G
i1,b
λ (h, d)G
i2,b
λ (h, d).

Using (7.1), this immediately yields

NORMALITY OF THE THUE–MORSE SEQUENCE 27

(7.6) Φi1,i2,b
λ (h, 2d + δ)
 = 1
4
 ∑

ε1<2
 ∑

ε2<2 e (
− (ε1 − ε2)h
2λ
 ) f i1,b
δ,ε1 f i2,b
δ,ε2 ΦTδ,ε1 (i1),Tδ,ε2 (i2),b
λ−1 (h, d)

for δ ∈ {0, 1}, and applying this identity iteratively one gets, for m ∈ N and d
′ < 2m,

(7.7) Φi1,i2,b
λ (h, 2md + d
′) = 1
4m ∑

e1<2m
 ∑

e2<2m e (
− (e1 − e2)h
2λ
 )

× f (m),i1,b
d′,e1 f (m),i2,b
d′,e2 ΦT (m)
d′,e1 (i1),T (m)
d′,e2 (i2),b

λ−m (h, d).

Obviously this implies for all d
′ < 2m

(7.8)
 ∣
∣
∣G
i,b
λ (h, 2md + d
′)
∣
∣
∣2 = ∣
∣
∣Φi,i,b
λ (h, 2md + d
′)
∣
∣
∣

≤ max
e1,e2<2m
 ∣
∣
∣
∣ΦT (m)
d′,e1 (i),T (m)
d′,e2 (i),b

λ−m (h, d)
∣
∣
∣
∣

= max
e<2m
 ∣
∣
∣
∣G
T (m)
d′,e (i),b

λ−m (h, d)
∣
∣
∣
∣
2 ,

an estimate that is also valid for m = 0.

7.2. An estimate for Fourier coeﬃcients. In this section, we are concerned with such se-
quences b originating from a sequence a = (a0, . . . , aL−1) ∈ {0, 1}L, where 1 ≤ L ≤ r, via the
assignment

(7.9) bℓ =
 



aℓ, 0 ≤ ℓ < L,
−aℓ−r, r ≤ ℓ < L + r − 1,
0, otherwise.

That is, the sequence b consists of two blocks, identical modulo 2. From now on, we assume that
b is such a sequence and that K = L + r (such that bℓ, for ℓ < K, captures all nonzero values).
For brevity, and since b is constant in what follows, we omit b as an upper index of G, Φ and
f . Moreover, we assume throughout this section that λ ≥ 0, r ≥ 1 and m ≥ 5 are integers such
that
 2m−5 ≤ L < 2m−4,(7.10)
 2m ≤ ν2(r) ≤ λ/4.(7.11)

For brevity, we write x = ν2(r).

Lemma 7.2. Assume that the sequence i ∈ IK satisﬁes

(7.12) i(r) mod 2m ∈ {1, 2}.

Let z ≥ 0 and h be integers and 0 ≤ d < 2z. Then

∣
∣G
i
z+m(h, d 2m + 1)
∣
∣2 ≤ (1 − η) max
e<2m
 ∣
∣
∣
∣G
T (m)
1,e (i)
z (h, d)
∣
∣
∣
∣
2

for η = 2
4m .

Proof. We rewrite the left hand side via the identity (7.7), setting i1 = i2 = i, and want to ﬁnd
pairs of indices (e′
1, e′
2), (e′′
1 , e′′
2 ) such that the corresponding two summands on the right hand
side of (7.7) cancel. This will give the announced saving. That is, we want

T (m)
1,e′
1 (i) = T (m)
1,e′′
1 (i),(7.13)

28 C. M ¨ULLNER AND L. SPIEGELHOFER

T (m)
1,e′
2 (i) = T (m)
1,e′′
2 (i),(7.14)
 f (m),i
1,e′
1 f (m),i
1,e′
2 = −f (m),i
1,e′′
1 f (m),i
1,e′′
2 and(7.15)
 e′
1 − e′
2 = e′′
1 − e′′
2 .(7.16)

We show that these conditions are satisﬁed for the choice

e′
1 = (0101m−3)2, e′
2 = (1001m−3)2,

e′′
1 = (0111m−3)2, e′′
2 = (1011m−3)2,

where (εν . . . ε0)2 = ∑i≤ν εi2i and 1k means k-fold repetition of the digit 1. Condition (7.16)
is clearly true. In order to verify (7.13) and (7.14), we note that the binary representations of
e′
1, e′
2, e′′
1 , e′′
2 all start with m − 3 ones. We therefore deﬁne

j = T (m−3)
1,(1m−3)2(i).

By (7.10), which implies i(ℓ) + ℓ < 2m−3 for 0 ≤ ℓ < L, we have

(7.17) j(ℓ) = ⌊ i(ℓ) + ℓ + 2m−3 − 1
2m−3
 ⌋ =
 {0, ℓ = 0,
1, 1 ≤ ℓ < L.

Moreover, by (7.12) we obtain i(r + ℓ) + ℓ − 1 mod 2m ∈ {0, . . . , 2L − 1}. Using also (7.10)
and (7.11), we get

(7.18) j(r + ℓ) = ⌊ i(r + ℓ) + r + ℓ + 2m−3 − 1
2m−3
 ⌋ ≡ 1 mod 8

for 0 ≤ ℓ < L. Since j ∈ IK, this equation implies that the value j(ℓ) is constant for ℓ ∈ [r, r+L).
By (7.4) we obtain (7.13) and (7.14) as soon as we show that T (3)
0,2 (j) = T (3)
0,3 (j) = T (3)
0,4 (j) =

T (3)
0,5 (j). Using (7.17) and (7.18) we have for 0 ≤ e ≤ 6 and 0 ≤ ℓ < L

T (3)
0,e (j)(ℓ) = ⌊ j(ℓ) + e
8
 ⌋ ≤ ⌊ 7
8
 ⌋ = 0,

T (3)
0,e (j)(r + ℓ) = ⌊ j(r + ℓ) + e
8
 ⌋ = ⌊ j(r) − 1
8 + e + 1
8
 ⌋ = j(r) − 1
8 .

It remains to verify (7.15), which is clearly equivalent to

f (m),i
1,e′
1 f (m),i
1,e′′
1 = −f (m),i
1,e′
2 f (m),i
1,e′′
2 ,

since the weights have absolute value 1. By (7.4), (7.5) and the deﬁnition of e′
1, e′
2, e′′
1 , e′′
2 this
equation is equivalent to

(7.19) f (3),j
0,2 f (3),j
0,3 = −f (3),j
0,4 f (3),j
0,5 .

By (7.9) we have, for any sequence i ∈ IK and all δ, ε ∈ {0, 1},

f i
δ,ε = e
 ( 1
2
 ∑

ℓ<L aℓ(i(ℓ) − i(r + ℓ))

)
 .

Using this identity, (7.17), (7.18) and the assumption a0 = 1 the veriﬁcation of (7.19) is straight-
forward, which completes the proof. □

Let d = (dλ−1 · · · d0)2 < 2λ. We call a position µ good (a notion that depends on λ, d, i, r and
m), if the following properties are satisﬁed.
(a) 0 ≤ µ ≤ λ − m.
(b) (dµ+m−1, . . . , dµ+1, dµ) = (0, . . . , 0, 1).

NORMALITY OF THE THUE–MORSE SEQUENCE 29

(c) T (µ)
d,0 (i)(r) ≡ 1 mod 2m.
The point of this notion is that at each good position, using Lemma 7.2, we win a factor 1 − η
in the estimate of Φ(h, d). This argument is carried out in the following lemma.

Lemma 7.3. Let i ∈ IK and k ≥ 0 and assume that d < 2λ is such that the number of good
positions µ is at least k. Then ∣
∣G
i
λ(h, d)
∣
∣2 ≤ (1 − η)
k

holds for all h ∈ Z and η = 2/4m.

Proof. Let 0 ≤ µ0 < . . . < µk−1 be good positions. We set µk = λ. The estimate (7.8) implies
that ∣
∣G
i
λ(h, d)
∣
∣2 ≤ max
e<2µ0
 ∣
∣
∣
∣G
T (µ0 )
d,e (i)
λ−µ0 (h, ⌊d/2µ0⌋)
∣
∣
∣
∣
2 .

Let 0 ≤ j < k. Since the position µj is good, we know by (c) and (7.3) that T (µj )
d,e (r) mod 2m ∈
{1, 2} for all e < 2µj . Thus we can apply Lemma 7.2, the identity (7.4) and the estimate (7.8)
and obtain
 max
e<2
µj
 ∣
∣
∣
∣G
T (µj )
d,e (i)
λ−µj (h, ⌊d/2µj ⌋)
∣
∣
∣
∣
2

≤ max
e<2
µj (1 − η) max
e′<2m
 ∣
∣
∣
∣
∣
G
T (m)
1,e′ ◦T (µj )
d,e (i)

λ−µj −m (
h, ⌊
d/2µj+m⌋)
∣
∣
∣
∣
∣

2

= (1 − η) max
e<2
µj +m
 ∣
∣
∣
∣G
T (µj +m)
d,e (i)
λ−µj −m (
h, ⌊
d/2µj+m⌋)
∣
∣
∣
∣

2

≤ (1 − η) max
e<2
µj+1
 ∣
∣
∣
∣G
T (µj+1 )
d,e (i)
λ−µj+1 (h, ⌊d/2µj+1 ⌋)
∣
∣
∣
∣
2 .

This proves the desired upper bound. □

In order to show that for most d there are many good positions, we have a closer look at
condition (7.12).

Lemma 7.4. Write r = 2xr0 with r0 odd and assume that y ≥ 0 and 0 ≤ d0 < 2y. Let i ∈ IK.
There exists a unique d1 ∈ {0, . . . , 2m − 1} such that for all d2 ∈ {0, . . . , 2x−m − 1} we have

T (x+y)
d,0 (i)(r) ≡ 1 mod 2m,

where d = 2y+md2 + 2yd1 + d0.
If d
′
1 < 2y is diﬀerent from d1, we have T (x+y)
d,0 (i)(r) ̸≡ 1 mod 2m for all d2 ∈ {0, . . . , 2x−m −
1}.

Proof. Since r0 is odd, the statements follow from

T (x+y)
d,0 (i)(r) = ⌊ i(r)
2x+y + r0d0
2y
 ⌋ + r0d1 + r02md2 ≡ ⌊ i(r)
2x+y + r0d0
2y
 ⌋ + r0d1 mod 2m.
 □

Note that the good-ness of a position µ does not depend on the digits of d with indices
µ − x + m, . . . , µ − 1. Let λ ≥ 0. We decompose the set {0, . . . , λ − 1} into intervals as follows.
Consider the mutually disjoint sets of indices
A1 = {2ℓ1x + ℓ0m : 0 ≤ ℓ1 < ⌊λ/(2x)⌋ and 0 ≤ ℓ0 < ⌊x/m⌋},

A2 = {(2ℓ1 + 1)x + ℓ0m : 0 ≤ ℓ1 < ⌊λ/(2x)⌋ and 0 ≤ ℓ0 < ⌊x/m⌋},

30 C. M ¨ULLNER AND L. SPIEGELHOFER

which form the starting points of intervals of length m. We call these intervals to be of type 1
and 2 respectively. The integers in [0, λ) not contained in an interval of type 1 or 2 form
intervals of type 3, having total length λ − 2m ⌊λ/(2x)⌋ ⌊x/m⌋. Assume that λ ≥ 2x, which
will be guaranteed by the hypotheses of Proposition 2.7. Then, beginning at 0, the resulting
partition starts with ⌊x/m⌋ intervals of type 1, followed possibly (if and only if m ∤ x) by an
interval of type 3 , which ﬁlls up the gap up to position x. This is followed by ⌊x/m⌋ intervals of
type 2 and possibly an interval of type 3, reaching 2x. This pattern continues up to 2x ⌊λ/(2x)⌋,
the last interval of type 3 however extends up to λ.

Lemma 7.5. Let M be a k-element subset of A2. The number of d < 2λ such that M is the set
of good positions in A2 equals 2λ−2mλ0 (22m − 1)
λ0−k, where λ0 = |A1| = |A2| = ⌊λ/(2x)⌋ ⌊x/m⌋.

Proof. We construct recursively the set of admissible d = (dλ−1 · · · d0)2 < 2λ. In order to do
so, we let µ run through the set A1 ∪ A2 ∪ A3 in ascending order and choose digits of d in
such a way that all digits up to position µ have already been chosen when we reach µ. If we
encounter an index µ ∈ A1, we set the 2m digits dµ, . . . , dµ+m−1, dµ+x, . . . , dµ+x+m−1 according
to two cases: if µ + x ∈ M , we have to guarantee good-ness of the position µ + x, we therefore
set (dµ+m−1, . . . , dµ) according to Lemma 7.4 and (dµ+x+m−1, . . . , dµ+x) = (0, . . . , 0, 1). If
µ + x ̸∈ M , we may choose any of the remaining 22m − 1 possibilities for these 2m digits, such
that the position µ + x will not be good. If we encounter µ ∈ A2, we do nothing, since the
corresponding block of length m has already been ﬁlled. If we ﬁnd an index µ ∈ A3, it is the
starting point of an interval I of type 3. We may set the digits of d with indices in I freely.
Therefore we can choose λ − 2m|A1| digits arbitrarily, and |A1| − k times we may choose out of
22m − 1 possibilities. This implies the statement of the lemma. □

The proof of Proposition 2.7 is now easy.

Proof of Proposition 2.7. Let λ0 = ⌊λ/(2x)⌋ ⌊x/m⌋. It follows from Lemma 7.5 that there are
precisely (
λ0
k )2λ−2mλ0(
22m − 1)λ0−k integers d ∈ {0, . . . , 2λ − 1} such that exactly k positions
from A2 are good. Since each d occurs for some k ≤ λ0, Lemma 7.3 implies

∑

d<2λ max
h<2λ ∣
∣G
i
λ(h, d)
∣
∣2 ≤ 2λ−2mλ0 λ0∑

k=0
 (
λ0
k
 )
(22m − 1)
λ0−k(1 − η)
k

= 2λ(1 − 2/16m)
λ0 .

By (7.11) we obtain

λ0 = ⌊λ/(2x)⌋ ⌊x/m⌋ ≥ λ − 2x
2x x − m
m ≥ λ/2
2x x/2
m = λ
8m .

This ﬁnishes the proof. □

8. Proof of Proposition 2.8

The following elementary lemma summarizes (and extends) Lemmas 9 through 11 from [22].

Lemma 8.1. Let a, b be real numbers such that a ≤ b and set K = b − a. Assume that
f : [a, b] → R is twice diﬀerentiable and |f ′′| ≤ B. Then for all α ∈ f ′([a, b]) the following
statements hold.
(i) For a ≤ x ≤ b we have
 |xα + f (a) − aα − f (x)| ≤ BK 2.

(ii) If x ∈ [a, b] is such that ∥xα + f (a) − aα∥ > BK 2, then

⌊f (x)⌋ = ⌊xα + f (a) − aα⌋ .

NORMALITY OF THE THUE–MORSE SEQUENCE 31

(iii) If a, b are integers, L ≥ 1 is an integer, f : [a, b + L − 1] → R is twice diﬀerentiable,
α ∈ f ′([a, b]) and |f ′′| ≤ B, then

|{n ∈ (a, b] : ⌊f (n + ℓ)⌋ ̸= ⌊(n + ℓ)α + f (a) − aα⌋ for some ℓ < L}|

≤ 2B(K + L − 1)
3L + KLDK(α).

We prove Proposition 2.8. For convenience, let ϕ(n) = 0 for n ≤ 0 and set f (n) = nc. We
follow the proof of [22, Proposition 1]. By analogous considerations as given there, we may
assume that K is an integer and that 2 ≤ K ≤ N .
Deﬁne integral partition points ai = ⌈N ⌉+iK for i ≥ 0 and set M = max{i : ai+L−1 ≤ 2N }.
The integer M satisﬁes the estimate KM ≤ N . We have the decomposition

(8.1) (N, 2N ] = (N, ⌈N ⌉] ∪ ⋃

0≤i<M(ai, ai+1] ∪ (aM , 2N ].

Let α ∈ R. Then by the triangle inequality and the relation ai+1 − ai = K we have for i < M

(8.2) ∣
∣|{n ∈ (ai, ai+1] : ϕ (⌊(n + ℓ)
c⌋) = ωℓ for 0 ≤ ℓ < L}| − Kδ∣
∣
 ≤ T1(α, i) + T2(α, i),

where
 T1(α, i) = ∣
∣|{n ∈ (ai, ai+1] : ϕ (⌊(n + ℓ)
c⌋) = ωℓ for 0 ≤ ℓ < L}|

− |{n ∈ (ai, ai+1] : ϕ (⌊(n + ℓ)α + f (ai) − aiα⌋) = ωℓ for 0 ≤ ℓ < L}|
∣
∣

T2(α, i) = ∣
∣|{n ∈ (ai, ai+1] : ϕ (⌊(n + ℓ)α + f (ai) − aiα⌋) = ωℓ for 0 ≤ ℓ < L}|

− Kδ∣
∣

We integrate both sides of (8.2) in the variable α from f ′(ai) to f ′(ai+1), divide by the length
of the integration range, and take the sum over i from 0 to M − 1, which yields

(8.3) ∣
∣|{n ∈ (a0, aM ] : ϕ (⌊(n + ℓ)
c⌋) = ωℓ for 0 ≤ ℓ < L}| − M Kδ∣
∣

≤ ∑

0≤i<M
 1
f ′(ai+1) − f ′(ai)
 ∫ f ′(ai+1)

f ′(ai)
 (
T1(α, i) + T2(α, i)
) dα.

We estimate the ﬁrst summand. If 0 ≤ i < M and α ∈ f ′([ai, ai+1]), Lemma 8.1 gives

(8.4) T1(α, i) ≤ 2f ′′(N )(K + L − 1)
3L + LKDK(α).

By the Mean Value Theorem we have
1
f ′(ai+1) − f ′(ai) ≪ N
K 1
f ′(2N ) − f ′(N )
(8.5)

for 0 ≤ i < M . Using this and the integral mean discrepancy estimate (3.3) we obtain

∑

0≤i<M
 1
f ′(ai+1) − f ′(ai)
 ∫ f ′(ai+1)

f ′(ai) DK(α) dα

≤ N
K 1
f ′(2N ) − f ′(N )
 ∑

0≤i<M
 ∫ f ′(ai+1)

f ′(ai) DK(α) dα

≤ N
K f ′(2N ) − f ′(N ) + 1
f ′(2N ) − f ′(N )
 ∫ 1

0 DK(α) dα

≪ (N + 1
f ′′(N )
 ) (
log+K)2

K 2 .

32 C. M ¨ULLNER AND L. SPIEGELHOFER

By the estimates KM ≤ N and N ≥ C/f ′′(N ) this implies

∑

0≤i<M
 1
f ′(ai+1) − f ′(ai)
 ∫ f ′(ai+1)

f ′(ai) T1(α, i) dα
 ≤ C1N L(
f ′′(N )K 2 +
 (
log+N )2

K
 )

for some constant C1 depending on c and L. We turn our attention to the second summand
in (8.3). Inserting (8.5) and the deﬁnition of T2(α, i), we easily obtain

(8.6) ∑

0≤i<M
 1
f ′(ai+1) − f ′(ai)
 ∫ f ′(ai+1)

f ′(ai) T2(α, i) dα ≪ N J(N, K).

Estimating also the contributions of the ﬁrst and the last interval in (8.1) trivially and collecting
the error terms, we obtain
∣
∣
∣
∣ 1
N
 ∣
∣{
n ∈ (N, 2N ] : ϕ
(⌊
(n + ℓ)
c⌋) = ωℓ for 0 ≤ ℓ < L}∣
∣ − δ∣
∣
∣
∣

≤ C2
(f ′′(N )K 2 + (log N )
2

K + J(N, K) + K
N
 )
,

for some C2 depending on c and L. By the estimate f ′′(N ) ≥ C/N the last term is dominated
by the ﬁrst, which ﬁnishes the proof of Proposition 2.8.

References

[1] J.-P. Allouche and J. Shallit, The ubiquitous Prouhet-Thue-Morse sequence, in Sequences and their
applications (Singapore, 1998), Springer Ser. Discrete Math. Theor. Comput. Sci., Springer, London, 1999,
pp. 1–16.
[2] , Automatic sequences, Cambridge University Press, Cambridge, 2003. Theory, applications, general-
izations.
[3] E. Bombieri, On the large sieve, Mathematika, 12 (1965), pp. 201–225.
[4] S. Brlek, Enumeration of factors in the Thue-Morse word, Discrete Appl. Math., 24 (1989), pp. 83–96.
[5] C. Dartyge and G. Tenenbaum, Congruences de sommes de chiﬀres de valeurs polynomiales, Bull. London
Math. Soc., 38 (2006), pp. 61–69.
[6] J.-M. Deshouillers, M. Drmota, and J. F. Morgenbesser, Subsequences of automatic sequences indexed
by ⌊nc⌋ and correlations, J. Number Theory, 132 (2012), pp. 1837–1866.
[7] M. Drmota, C. Mauduit, and J. Rivat, The Thue-Morse sequence along squares is normal. Submitted.
[8] M. Drmota and J. F. Morgenbesser, Generalized Thue-Morse sequences of squares, Israel J. Math., 190
(2012), pp. 157–193.
[9] P. D. T. A. Elliott and H. Halberstam, A conjecture in prime number theory, in Symposia Mathematica,
Vol. IV (INDAM, Rome, 1968/69), Academic Press, London, 1970, pp. 59–72.
[10] E. Fouvry and C. Mauduit, Sommes des chiﬀres et nombres presque premiers, Math. Ann., 305 (1996),
pp. 571–599.
[11] A. O. Gel′fond, Sur les nombres qui ont des propri´et´es additives et multiplicatives donn´ees, Acta Arith.,
13 (1967/1968), pp. 259–265.
[12] G. H. Hardy and E. M. Wright, An introduction to the theory of numbers, Oxford, at the Clarendon
Press, 1954. 3rd ed.
[13] C. Mauduit, Multiplicative properties of the Thue-Morse sequence, Period. Math. Hungar., 43 (2001),
pp. 137–153.
[14] C. Mauduit and J. Rivat, R´epartition des fonctions q-multiplicatives dans la suite ([nc])n∈N, c > 1, Acta
Arith., 71 (1995), pp. 171–179.
[15] , Propri´et´es q-multiplicatives de la suite ⌊nc⌋, c > 1, Acta Arith., 118 (2005), pp. 187–203.
[16] , La somme des chiﬀres des carr´es, Acta Math., 203 (2009), pp. 107–148.
[17] , Sur un probl`eme de Gelfond: la somme des chiﬀres des nombres premiers, Ann. of Math. (2), 171
(2010), pp. 1591–1646.
 NORMALITY OF THE THUE–MORSE SEQUENCE 33

[18] H. L. Montgomery, The analytic principle of the large sieve, Bull. Amer. Math. Soc., 84 (1978), pp. 547–
567.
[19] Y. Moshe, On the subword complexity of Thue-Morse polynomial extractions, Theoret. Comput. Sci., 389
(2007), pp. 318–329.
[20] I. I. Piatetski-Shapiro, On the distribution of prime numbers in sequences of the form [f (n)], Mat. Sbornik
N.S., 33(75) (1953), pp. 559–566.
[21] J. Rivat and P. Sargos, Nombres premiers de la forme ⌊nc⌋, Canad. J. Math., 53 (2001), pp. 414–433.
[22] L. Spiegelhofer, Piatetski-Shapiro sequences via Beatty sequences, Acta Arith., 166 (2014), pp. 201–229.
[23] , Normality of the Thue-Morse sequence along Piatetski-Shapiro sequences, Q. J. Math., 66 (2015),
pp. 1127–1138.

Institute of Discrete Mathematics and Geometry,, Vienna University of Technology, Vienna,
Austria

Institute of Discrete Mathematics and Geometry,, Vienna University of Technology, Vienna,
Austria
