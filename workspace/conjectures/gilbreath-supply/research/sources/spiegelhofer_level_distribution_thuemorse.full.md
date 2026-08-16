<!-- source: https://arxiv.org/pdf/1803.01689 | converted from PDF -->

arXiv:1803.01689v1  [math.NT]  5 Mar 2018
THE LEVEL OF DISTRIBUTION OF THE THUE–MORSE SEQUENCE

LUKAS SPIEGELHOFER

Abstract. The level of distribution of a complex valued sequence b measures “how well b
behaves” on arithmetic progressions nd + a. Determining whether θ is a level of distribution
for b involves summing a certain error over d ≤ D, where D depends on θ; this error is given
by comparing a ﬁnite sum of b along nd + a and the expected value of the sum. We prove that
the Thue–Morse sequence has level of distribution 1, which is essentially best possible. More
precisely, this sequence gives one of the ﬁrst nontrivial examples of a sequence satisfying
a Bombieri–Vinogradov type theorem for each exponent θ < 1. In particular, this result
improves on the level of distribution 2/3 obtained by M¨ullner and the author.
As an application of our method, we show that the subsequence of the Thue–Morse se-
quence indexed by ⌊nc⌋, where 1 < c < 2, is simply normal. That is, each of the two symbols
appears with asymptotic frequency 1/2 in this subsequence. This result improves on the
range 1 < c < 3/2 obtained by M¨ullner and the author and closes the gap that appeared
when Mauduit and Rivat proved (in particular) that the Thue–Morse sequence along the
squares is simply normal. In the proofs, we reduce both problems to an estimate of a certain
Gowers uniformity norm of the Thue–Morse sequence similar to that given by Konieczny
(2017).
 1. Introduction

The Thue–Morse sequence t is one of the most easily deﬁned automatic sequences. Like any
automatic sequence, it can be deﬁned using a constant-length substitution over a ﬁnite alphabet:
t is the unique ﬁxed point of the substitution 0 ↦→ 01, 1 ↦→ 10 that starts with 0. Therefore
t = 0110100110010110 . . .. Alternatively, this sequence can be deﬁned using the binary sum-of-
digits function s, which counts the number of 1s in the binary expansion of a nonnegative integer
n: we have t(n) = 0 if and only if s(n) ≡ 0 mod 2. The equivalence of these two deﬁnitions can
be proved via a third description: start with the one-element sequence t
(0) := (0) and deﬁne
t
(n+1) by concatenating t
(n) and the Boolean complement ¬t
(n). Then t is the pointwise limit of
these ﬁnite sequences. In this work, we will adapt the second viewpoint. In fact, in the proofs we
will work with the sequence (−1)
s(n) instead of t. For an overview on the Thue–Morse sequence,
we refer the reader to the article by Allouche and Shallit [1], which points out occurrences of
this sequence in diﬀerent ﬁelds of mathematics and oﬀers a good bibliography. Moreover, we
wish to mention the paper [24] by Mauduit. For a comprehensive account of automatic and
morphic sequences, see the book [2] by Allouche and Shallit.
The main topic of this article is the study of t along arithmetic progressions and, more
generally, along Beatty sequences ⌊nα+β⌋. This topic can be traced back at least to Gelfond [18],
who proved the following theorem on the base-q sum-of-digits function sq.

2010 Mathematics Subject Classiﬁcation. Primary 11N69, 11B25, 11B85; Secondary 11A63, 11K16, 11B83.
Key words and phrases. Thue–Morse sequence, level of distribution, Bombieri–Vinogradov theorem, Elliott–
Halberstam conjecture, arithmetic progression, Piatetski-Shapiro sequence, simply normal sequence, Gelfond
problem .
The author acknowledges support by the Austrian Science Fund (FWF), Project F5502-N26, which is a part
of the Special Research Program “Quasi Monte Carlo methods: Theory and Applications”. Moreover, the author
wishes to acknowledge support by the project MuDeRa, which is a joint project between the FWF (I-1751-N26)
and the ANR (Agence Nationale de la Recherche, France, ANR-14-CE34-0009).

1

2 LUKAS SPIEGELHOFER

Theorem A (Gelfond). Let q, m, d, b, a be integers and q, m, d ≥ 2. Suppose that gcd(m, q−1) =
1. Then ∣
∣{1 ≤ n ≤ x : n ≡ a mod d, sq(n) ≡ b mod m}∣
∣ = x
dm + O(x
λ)

for some λ < 1 not depending on x, d, a, and b.

We are particularly interested in the error term for sparse arithmetic progressions, having
large common diﬀerence d. This leads us directly to the other main concept of this paper, the
notion of level of distribution. Very roughly speaking, the level of distribution is a measure of
how well a given sequence behaves on arithmetic progressions. A formal deﬁnition is given by
Fouvry and Mauduit [14], for example, which we adapt here.

Deﬁnition 1. Let c = (cn)n≥0 be a sequence of complex numbers, and for each integer d ≥ 1
let Q(d) and R(d) ̸= ∅ be subsets of Z/dZ such that Q(d) ⊆ R(d). The sequence c has level of
distribution θ with respect to Q and R if for all ε > 0 and A > 0 we have for all x ≥ 1

∑

1≤d≤xθ−ε max
0≤y≤x max
0≤a<d
a+dZ∈Q(d)

∣
∣
∣
∣
∣
 ∑

0≤n<y
n≡a mod d
 cn − 1
|R(d)|
 ∑

0≤n<y
n+dZ∈R(d)
 cn
∣
∣
∣
∣
∣

= O
(( ∑

0≤n<x|cn|
)
(log 2x)
−A)
.

The implied constant may depend on A and ε. Moreover, in this deﬁnition the maximum over
the empty index set is deﬁned as 0.

The level of distribution (also called exponent of distribution by some authors) is an important
concept in sieve theory. As a striking application, a variant of this concept was used in the
“bounded gaps between primes” paper by Zhang [36]. For more information on this subject, we
refer the reader to the survey by Kontorovich [22]. Moreover, we wish to draw the attention of
the reader to the book [16] on sieve theory by Friedlander and Iwaniec, in particular Chapter 22
on the level of distribution.
We are ready to present our main result.

Theorem 1.1. The Thue–Morse sequence has level of distribution 1 with respect to Q and R
given by Q(d) = R(d) = Z/dZ. More precisely, for all ε > 0 we have

∑

1≤d≤D max
0≤y≤x max
0≤a<d

∣
∣
∣
∣
∣
 ∑

0≤n<y
n≡a mod d

(−1)
s(n)∣
∣
∣
∣
∣ = O(x
1−η)

for some η > 0 depending on ε, where D = x
1−ε.

Before presenting some history, we wish to say a word about the proof: we are going to
reduce the problem to the estimation of a certain Gowers uniformity norm of the Thue–Morse
sequence. These expressions appear by repeated application of van der Corput’s inequality and
have the form ∑

0≤n<2
ρ
0≤r1,...,rm<2
ρ
 ∏

ε∈{0,1}m(−1)
sρ(n+ε·r),

where ε · r = ∑
1≤i≤m εiri and sρ is the truncated sum-of-digits function in base 2 deﬁned by
sρ(n) = s(n mod 2ρ). The proof of a very similar statement was given recently by Konieczny [21],
and we use ideas from that paper to prove our estimate.
In order to put Theorem 1.1 into context, we present some related theorems. The well-known
Bombieri–Vinogradov theorem concerns the level of distribution of the von Mangoldt function

LEVEL OF DISTRIBUTION OF THUE–MORSE 3

Λ, which is deﬁned by Λ(n) = log p if n = pk for some prime p and some k ≥ 1 and Λ(n) = 0
otherwise. This theorem states that Λ has level of distribution 1/2 with respect to Q and R
given by Q(d) = R(d) = (Z/dZ)
∗.

Theorem B (Bombieri–Vinogradov). Let d ≥ 1 and a be integers and deﬁne

ψ(x; d, a) = ∑

1≤n≤x
n≡a mod d
 Λ(n).

For all real numbers A > 0 there exist B > 0 and a constant C such that setting D =
x
1/2(log x)
−B we have for all x ≥ 2
∑

1≤d≤D max
1≤y≤x max
0≤a<d
gcd(a,d)=1
 ∣
∣
∣
∣ψ(y; d, a) − y
ϕ(d)
 ∣
∣
∣
∣ ≤ Cx(log x)
−A.

Here ϕ denotes Euler’s totient function.

No improvement on the level of distribution 1/2 in this theorem is currently known; meanwhile
the Elliott–Halberstam conjecture [10] states that we can choose D = x
1−ε for any ε > 0. That
is, it is conjectured that the primes have level of distribution 1. Improvements on the exponent
1/2 exist for certain sequences of integers; we refer to the articles [11, 12] by Fouvry, by Fouvry
and Iwaniec [13] and by Friedlander and Iwaniec [17]. Moreover, we note the series [3, 4, 5] by
Bombieri, Friedlander and Iwaniec concerning these questions. In this context, we also note the
result of Goldston, Pintz, and Yıldırım [19], who showed in particular the following conditional
result: if the primes have level of distribution θ for some θ > 1/2, there is a constant C such
that pn+1 − pn < C inﬁnitely often, where pn is the n-th prime. In a groundbreaking paper we
mentioned before, Zhang [36] used the Goldston–Pintz–Yıldırım method and a variant of the
Bombieri–Vinogradov theorem to prove the above result unconditionally. Maynard [29] later
proved the bounded gaps result using only the classical Bombieri–Vinogradov theorem.
Improvements on the level 1/2 are also known for the sum-of-digits function modulo m.
Fouvry and Mauduit [15] established 0.5924 as level of distribution of the Thue–Morse sequence,
with respect to Q and R, where Q(d) = R(d) = Z/dZ.

Theorem C (Fouvry–Mauduit). Set

A(x; d, a) = ∣
∣{
0 ≤ n < x : t(n) = 0, n ≡ a mod d
}∣
∣.

Then

(1.1) ∑

1≤d≤D max
1≤y≤x max
0≤a<d
∣
∣
∣A(y; d, a) − y
2d
 ∣
∣
∣ ≤ Cx(log 2x)
−A

for all real A and D = x
0.5924.

More generally, for m ≥ 2 they also study the sum-of-digits function in base 2 modulo m,
obtaining the weaker level of distribution 0.55711. Using sieve theory, they apply this result to
the study of the sum of digits modulo m of numbers having at most two prime factors. Later,
Mauduit and Rivat [28], in an important paper, managed to treat the sum of digits modulo m
of prime numbers, thereby answering one of the questions posed by Gelfond [18].
M¨ullner and the author [31] improved the exponent 0.5924 to 2/3 − ε, thereby establishing
2/3 as an admissible level of distribution of the Thue–Morse sequence.
Fouvry and Mauduit [14] also considered, more generally, the sum-of-digits function sq in
base q modulo an integer m such that gcd(m, q − 1) = 1. They obtain the remarkable result
that the level of distribution approaches 1 as the base q gets larger.

4 LUKAS SPIEGELHOFER

Theorem D (Fouvry–Mauduit). Let q ≥ 2, m ≥ 1 and b be integers such that gcd(m, q−1) = 1.
Then for all A and ε > 0 we have for all x ≥ 1

∑

1≤d≤xθq −ε max
0≤y≤x max
0≤a<d

∣
∣
∣
∣
∣
 ∑

n<y,sq(n)≡b mod m
n≡a mod d
 1 − 1
d
 ∑

n<y,sq(n)≡b mod m 1
∣
∣
∣
∣
∣ = O(x(log 2x)
−A),

where θq → 1 as q → ∞. The implied constant depends at most on m, q, A and ε.

As an application of this theorem, they study the sum ∑
n<x,sq(n)≡b mod m Λk(n), where Λk
is the generalized von Mangoldt function of order k ≥ 1 ([14, Corollaire 2]).
Theorem D motivates us to ask which sequences have level of distribution equal to 1. In
the above-cited paper by Fouvry and Mauduit [14], for example, a list of sequences having this
property is given. Moreover, we note [16, Chapter 22.3], which studies the level of distribution
for additive convolutions, giving further examples. However, in these examples, other than the
trivial example cn = 1 for all n, the maximum over a does not play a rˆole: the set Q(d) consists
of at most one element.
We are interested in sequences c having level of distribution 1 and such that the set Q(d)
contains “many” residue classes. In other words, we want to ﬁnd analogues of the Elliott–
Halberstam conjecture. Requiring monotonicity of c, examples can be constructed easily: c(n) =
n is such an example, and more generally, increasing sequences c satisfying certain growth
conditions have this property. Apart from such “trivial” sequences, no other examples seem to
be known. Our Theorem 1.1, giving such an example, is therefore of considerable signiﬁcance.
Moreover, we note that our method can certainly be adapted to sq(n) mod m for general
bases q ≥ 2 and m ≥ 1, which yields θq = 1 in Theorem D.
The second focus of this paper concerns Piatetski-Shapiro sequences, which are sequences
of the form (⌊nc⌋)n≥0 for some c ≥ 1. For stating the second main theorem, we do not need
additional preparation.

Theorem 1.2. Let 1 < c < 2. The Thue–Morse sequence along ⌊nc⌋ is simply normal. That
is, each of the letters 0 and 1 appears with asymptotic frequency 1/2 in n ↦→ t(⌊nc⌋).

By the argument given in our earlier paper [31] with M¨ullner, this theorem is proved via a
Beatty sequence variant of Theorem 1.1. That theorem in turn is proved by arguments analogous
to the arguments in the proof of Theorem 1.1, and reduces to the same estimate of the Gowers
uniformity norm of Thue–Morse. Theorem 1.2 is therefore an application of the method of proof
of Theorem 1.1.
Again, we present some historical background. Studying Piatetski–Shapiro subsequences of a
given sequence can be seen as a step towards proving theorems on polynomial subsequences. For
example, it is unknown whether there are inﬁnitely many primes of the form n2 + 1; therefore it
is of interest to consider primes of the form ⌊nc⌋ for 1 < c < 2 and prove an asymptotic formula
for the number of such primes. Piatetski-Shapiro [32] proved such a formula for 1 < c < 12/11,
and the currently best known bound is 1 < c < 2817/2426 due to Rivat and Sargos [33]. In an
analogous way, the study of the sum-of-digits function along ⌊nc⌋ was motivated. It is another
problem posed by Gelfond [18] to study the distribution of the sum of digits of polynomial
sequences in residue classes. Since this problem could not be solved at ﬁrst, Mauduit and
Rivat [25, 26] considered q-multiplicative functions along ⌊nc⌋ (where a q-multiplicative function
f : N → {z ∈ C : |z| = 1} satisﬁes f (aqk + b) = f (aqk)f (b) for nonnegative integers a, b, k such
that b < qk) and they obtained an asymptotic formula for c < 7/5.

Theorem E (Mauduit–Rivat). Let 1 < c < 7/5 and set γ = 1/c. For all δ ∈ (0, (7−5c)/9) there
exists a constant C > 0 such that for all q-multiplicative functions f : N → {z ∈ C : |z| = 1}

LEVEL OF DISTRIBUTION OF THUE–MORSE 5

and all x ≥ 1 we have ∣
∣
∣
∣
∣
∣
 ∑

1≤n≤x f (⌊nc⌋) − ∑

1≤m≤xc γmγ−1f (m)

∣
∣
∣
∣
∣
∣ ≤ Cx
1−δ.

Since the Thue–Morse sequence is 2-multiplicative, it follows in particular that the the sub-
sequence indexed by ⌊nc⌋ assumes each of the two values 0, 1 with asymptotic frequency 1/2,
as long as 1 < c < 7/5. This means that this subsequence is simply normal. In the paper [7] by
Deshouillers, Drmota, and Morgenbesser, a statement as in Theorem E for arbitrary automatic
sequences and 1 < c < 7/5 is proved.
Some progress on Gelfond’s question on polynomials was made by Drmota and Rivat [9] and
by Dartyge and Tenenbaum [6]; ﬁnally, Mauduit and Rivat [27] managed to answer Gelfond’s
question for the polynomial n2. This latter paper was generalized by Drmota, Mauduit and
Rivat [8], who showed that in fact t(n2) deﬁnes a normal sequence, by which we understand
an inﬁnite sequence on {0, 1} such that every ﬁnite sequence of length k occurs as a factor
(contiguous ﬁnite subsequence) with asymptotic frequency 2−k. This result also generalizes a
paper by Moshe [30] who showed that every ﬁnite word on {0, 1} occurs as a factor of n ↦→ t(n2)
at least once.
However, the distribution of the sum of digits of ⌊nc⌋ in residue classes, for c ∈ [1.4, 2),
remained an open problem. Progress in this direction was made by the author [34], who improved
the bound on c to 1 < c ≤ 1.42 for the Thue–Morse sequence. The key idea in that paper is to
approximate ⌊nc⌋ by a Beatty sequence ⌊nα + β⌋ and thus reduce the problem to a linear one.
M¨ullner and the author [31], using the same linearization argument and a Bombieri–Vinogradov
type theorem for the Thue–Morse sequence on Beatty sequences, were able to extend this range
to 1 < c < 3/2. Moreover, we could handle occurrences of factors in Piatetski-Shapiro subse-
quences of t, thus showing that t (⌊nc⌋) deﬁnes a normal sequence for 1 < c < 3/2.

Theorem F (M¨ullner–Spiegelhofer). Let 1 < c < 3/2. Then the sequence u = (
t (⌊nc⌋)
)

n≥0 is
normal. More precisely, for any L ≥ 1 there exists an exponent η > 0 and a constant C such
that ∣
∣
∣∣
∣{
n < N : u(n + i) = ωi for 0 ≤ i < L}∣
∣ − N/2L∣
∣
∣ ≤ CN 1−η

for all (
ω0, . . . , ωL−1) ∈ {0, 1}L.

This theorem also improved on an earlier result by the author [35], who obtained normality
for 1 < c < 4/3, using an estimate for Fourier coeﬃcients related to the Thue–Morse sequence
provided by Drmota, Mauduit and Rivat [8].
Our Theorem 1.2 ﬁnally closes the gap in the set of exponents c such that we have an
asymptotic formula for Thue–Morse on ⌊nc⌋. This gap appeared with the Mauduit–Rivat result
on squares; at that time, the gap was [1.4, 2), now it was only left to close the smaller gap
[1.5, 2).
However, the case c > 2 remains open for now, for c ∈ Z (which is contained in Gelfond’s
problem on polynomial subsequences) as well as for Piatetski-Shapiro sequences. For example,
it is a notorious open question to prove that 0 occurs with frequency 1/2 in n ↦→ t(n3). (If this
result is proved some day, there will be a new gap to be closed.)
Mauduit [24, Conjecture 1] conjectures that

lim
N →∞ 1
N {1 ≤ n ≤ N : sq(⌊nc⌋) ≡ b mod m} = 1
m
for almost all c > 1, where q ≥ 2, m ≥ 1 and b are integers. While this almost-all result is
known for 1 < c < 2, as he notes just before this conjecture, we believe (as we noted before)
that our method can be adapted to generalize our results to general sequences sq(n) mod m and

6 LUKAS SPIEGELHOFER

thus to prove the asymptotic identity for all c ∈ (1, 2). However, while we are conﬁdent that
the asymptotic identity in Mauduit’s conjecture holds for all non-integer c > 1, the case c > 2
cannot yet be handled by our methods.
Moreover, we note that it would be interesting to generalize the normality result from Theo-
rem F to all exponents 1 < c < 2.

Notation. For a real number x, we write e(x) = exp(2πix), {x} = x − ⌊x⌋, ∥x∥ = minn∈Z|x − n|
and ⟨·⟩ = ⌊x+ 1/2⌋ (the “nearest integer” to x). For a prime number p let νp(n) be the exponent
of p in the prime factorization of n. We deﬁne the truncated binary sum-of-digits function

sλ(n) := s(n′),

where 0 ≤ n′ < 2λ and n′ ≡ n mod 2λ, which is the 2λ-periodic extension of the restriction of s
to {0, . . . , 2λ − 1}. For µ ≤ λ we deﬁne the two-fold restricted binary sum-of-digits function

sµ,λ(n) = sλ(n) − sµ(n).

For a real number x ≥ 0, we set
 log+x = max {1, log x} .

The symbol N denotes the set of nonnegative integers.

2. Results

In order to (re)state our main theorem, we introduce some notation. Let α, β, y and z be
nonnegative real numbers such that α ≥ 1. We deﬁne

A(y, z; α, β) = ∣
∣
{y ≤ m < z : t(m) = 0 and ∃n ∈ Z such that m = ⌊nα + β⌋}∣
∣.

For integers d = α and a = β, we clearly have

A(y, z; d, a) = ∣
∣{
y ≤ m < z : t(m) = 0 and m ≡ a mod d
}∣
∣.

Our main theorem is the following result, analogous to the Elliott–Halberstam conjecture.

Theorem 2.1. The Thue–Morse sequence has level of distribution 1. More precisely, for all
ε > 0 there exist η > 0 and C such that
∑

1≤d≤D max
y,z
0≤y≤z
z−y≤x
 max
0≤a<d
 ∣
∣
∣A(y, z; d, a) − y
2d
 ∣
∣
∣ ≤ Cx
1−η

for x ≥ 1 and D = x
1−ε.

Note that this theorem allows intervals [y, z) for arbitrary y ≥ 0, which is more general than
our deﬁnition of a level of distribution.
Our second result concerns Piatetski-Shapiro subsequences of the Thue–Morse sequence.

Theorem 2.2. Let 1 < c < 2. Then the sequence n ↦→ t(⌊nc⌋) is simply normal. More precisely,
there exists an exponent η > 0 and a constant C such that
∣
∣
∣
∣ 1
N
 ∣
∣{
0 ≤ n < N : t(⌊nc⌋) = 0}∣
∣ − 1
2
 ∣
∣
∣
∣ ≤ CN −η.

For proving this theorem, we follow the general argument presented in Section 4.2 of [31].
This argument uses linear approximation of ⌊nc⌋ by ⌊nα + β⌋ and thus reduces the problem to
Beatty sequences. Therefore Theorem 2.2 is a corollary of the following Beatty sequence version
of a statement on the level of distribution.

LEVEL OF DISTRIBUTION OF THUE–MORSE 7

Theorem 2.3. Let 0 < θ1 ≤ θ2 < 1. There exist η > 0 and C such that
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
∣A(y, z; α, β) − z − y
2α
 ∣
∣
∣
∣ dα ≤ Cx
1−η

for all x and D such that x ≥ 1 and x
θ1 ≤ D ≤ x
θ2.

In order to derive Theorem 2.2 from this result, it is essential that we have the maximum
over β inside the integral over α, since we need to approximate ⌊nc⌋ by inhomogeneous (shifted)
Beatty sequences ⌊nα + β⌋.
Concerning Theorem 2.1, a version of this result without the maximum over a follows from
work of Martin, Mauduit and Rivat, as we show now.

Remark. Martin, Mauduit and Rivat [23, Proposition 3] proved an estimate of a sum of type
II containing the following special case: let am and bn be complex numbers satisfying |am| ≤ 1
and |bn| ≤ 1. Assume that x ≥ 2, 0 < ε ≤ 1/2, x
ε ≤ M, N ≤ x and M N ≤ x. Then

S0 = ∑

M<m≤2M
 ∑

N <n≤2N
mn≤x
 ambn(−1)
s(mn) ≪ x
1−η

for an absolute implied constant and some η > 0 only depending on ε. By dyadic decomposition
and using the trivial estimate for n < x
ε, we obtain

∑

M<m≤2M
∣
∣
∣
∣
∣
 ∑

0≤n≤2N
mn≤x
 (−1)
s(mn)∣
∣
∣
∣
∣ ≪ x
1−η log N + M x
ε

for M and N satisfying the same restrictions, and with an implied constant that may depend
on ε. Let x be given and assume that x
ε ≤ M ≤ x
θ for some θ ∈ (1/2, 1). Set ε = 1−θ
2 ≤ 1/2
and N = x/M . Then N ≥ x
ε and the condition mn ≤ x implies n ≤ 2N . We obtain

∑

M<m≤2M
∣
∣
∣
∣
∣
 ∑

0≤k≤x
k≡0 mod m
(−1)
s(k)∣
∣
∣
∣
∣ ≪ x
1−η log x + M x
ε.

We use dyadic decomposition again (in m), moreover Fouvry and Mauduit [15] in order to
handle residue classes having small modulus m, that is, m ≤ x
ε. Moreover, we note (as we did
in [31]) that the error term in their estimate [15, (1.6)] is in fact x
1−η for some η > 0, which
follows from their Th´eor`eme 2. We obtain
∑

1≤d≤D
∣
∣
∣
∣
∣
 ∑

0≤n≤x
n≡0 mod d
(−1)
s(n)∣
∣
∣
∣
∣ ≤ Cx
1−η

for D = x
θ and some η > 0 and C depending on θ. This is a weak version of a statement of the
type “the Thue–Morse sequence has level of distribution 1”, where Q(d) has only one element.
(We note that we could also handle the maximum over y ≤ x, using the factor e(βmn) that
appears in [23, Proposition 3].) The additional value of our paper lies in the maximum over the
residue classes modulo d.

Finally, we note the following open questions concerning Theorems 2.1 and 2.2:
(1) In Theorem 2.1, can we choose D = x(log x)
−B for some B > 0 (using x(log x)
−A as
error term)?
(2) Does Theorem 2.2 hold for ⌊x
2(log x)
−C ⌋ (and similar sequences, possibly with a worse
error term)?

8 LUKAS SPIEGELHOFER

Plan of the paper. In Section 3 we state two results (Propositions 3.1 and 3.2) from which
Theorems 2.1 and 2.3 follow, moreover an important Gowers uniformity norm estimate of the
Thue–Morse sequence, Proposition 3.3. We also give an idea of the proof of Proposition 3.1. In
Section 4 we state lemmas needed for proving the results from Section 3. Section 5 is devoted
to proving Propositions 3.1 and 3.2. Finally, we prove Proposition 3.3 and a technical lemma
appearing in the proof of Propositions 3.1 and 3.2.

3. Auxiliary results

As in our earlier paper with M¨ullner ([31, Section 4.1], and using Fouvry and Mauduit [15,
Th´eor`eme 2] for handling small d), it is suﬃcient to prove the following two results in order to
obtain our main theorems.

Proposition 3.1. For real numbers N, D ≥ 1 and ξ set

(3.1) S0 = S0(N, D, ξ) = ∑

D≤d<2D max
a≥0
 ∣
∣
∣
∣
∣
 ∑

0≤n<N e ( 1
2 s(nd + a)
) e(nξ)

∣
∣
∣
∣
∣.

Let ρ2 ≥ ρ1 > 0. There exists an η > 0 and a constant C such that
S0
N D ≤ CN −η

holds for all ξ ∈ R and all real numbers N, D ≥ 1 satisfying N ρ1 ≤ D ≤ N ρ2 .

Proposition 3.2. For real numbers D, N ≥ 1 and ξ set

(3.2) S0 = S0(N, D, ξ) = ∫ 2D

D max
β≥0
 ∣
∣
∣
∣
∣
 ∑

0≤n<N e ( 1
2 s(
⌊nα + β⌋)
) e(nξ)

∣
∣
∣
∣
∣ dα.

Let ρ2 ≥ ρ1 > 0. There exist η > 0 and a constant C such that
S0
N D ≤ CN −η

holds for all real numbers D, N ≥ 1 satisfying N ρ1 ≤ D ≤ N ρ2 and for all ξ ∈ R.

In the proof of these results, we will use the following essential Gowers uniformity norm
estimate of the Thue–Morse sequence (see Konieczny [21]).

Proposition 3.3. Let m ≥ 2 be an integer. There exists some η > 0 and some C such that

1
2(m+1)ρ ∑

0≤n<2
ρ
0≤r1,...,rm<2
ρ
 e
 

 1
2
 ∑

ε∈{0,1}m sρ(n + ε · r)



 ≤ C2−ρη

for all ρ ≥ 0, where ε · r = ∑1≤i≤m εiri.

We wish to give a rough idea of the proof of Proposition 3.1 (Proposition 3.2 being proved
essentially in the same way.)
Idea of the proof of Proposition 3.1. The key idea is to reduce the number of digits that
have to be taken into account, and thus to replace the sum-of-digits function s by its truncated
version sρ. Here 2ρ will be signiﬁcantly smaller than N , so that (we simplify things a bit to
convey the idea) we may replace the sum over s(nd + a) by a full sum over the periodic function
sρ(n). This reducing of the digits is achieved by a reﬁnement of the method used by M¨ullner
and the author [31], which in turn builds on the ideas from the papers [27, 28] by Mauduit and
Rivat.
First, we apply van der Corput’s inequality and use a “carry propagation lemma” in order
to replace s by sλ. In general, 2λ will be much larger than N , so that we have to reduce λ

LEVEL OF DISTRIBUTION OF THUE–MORSE 9

further. The next step is to apply the generalized van der Corput inequality repeatedly. With
each application, we remove µ many digits. This is achieved by appealing to the Dirichlet
approximation theorem, by which we can ﬁnd a multiple of α = d/2jµ that is close to a multiple
of 2µ. This property can be used to discard the µ lowest digits.
By this repeated application the estimate is reduced to an estimate of a so-called Gow-
ers uniformity norm of the Thue–Morse sequence; a related estimate was recently given by
Konieczny [21].
 4. Lemmas

We have the following series of lemmas that can also be found in our earlier paper with
M¨ullner [31].
The ﬁrst lemma can be proved by elementary considerations.

Lemma 4.1. Let a, b ∈ R and n ∈ N.

If ∥a∥ < ε and ∥b∥ ≥ ε, then ⌊a + b⌋ = ⟨a⟩ + ⌊b⌋.(4.1)
 ∥na∥ ≤ n∥a∥.(4.2)
 If ∥a∥ < ε and 2nε < 1, then ⟨na⟩ = n⟨a⟩.(4.3)

As an essential tool, we will use repeatedly the following generalized van der Corput inequal-
ity [27, Lemme 17].

Lemma 4.2. Let I be a ﬁnite interval containing N integers and let zn be a complex number
for n ∈ I. For all integers K ≥ 1 and R ≥ 1 we have

(4.4)
 ∣
∣
∣
∣
∣

∑

n∈I zn
∣
∣
∣
∣
∣
2
 ≤ N + K(R − 1)
R
 ∑

0≤|r|<R
 (
1 − |r|
R
 ) ∑

n∈I
n+Kr∈I
 zn+Krzn.

Assume that α is a real number and N is a nonnegative integer. We deﬁne the discrepancy
of the sequence nα modulo 1:

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
∣ .

Applying this deﬁnition, using x = 1/(KT ) and α/K instead of α, we obtain the following
lemma.

Lemma 4.3. Let J be an interval in R containing N integers and let α and β be real numbers.
Assume that t, T, k and K are integers such that 0 ≤ t < T and 0 ≤ k < K. Then
∣
∣
∣
∣{n ∈ J : t
T ≤ {nα + β} < t + 1
T , ⌊nα + β⌋ ≡ k mod K}
∣
∣
∣
∣ = N
KT + O (
N DN ( α
K
 ))

with an absolute implied constant.

In the estimation of our error terms, we will use the following mean discrepancy results.

Lemma 4.4. For integers µ ≥ 0 and N ≥ 1 we have
∑

0≤d<2µ DN
 ( d
2µ
 ) ≪ N + 2µ

N (log+N )
2.

Moreover, the estimate ∫ 1

0 DN (α) dα ≪ (log+N )
2

N
holds. The implied constants in these estimates are absolute.

10 LUKAS SPIEGELHOFER

The following “carry propagation lemma” will allow us to replace the sum-of-digits function
s by its truncated version sλ. Statements of this type were used by Mauduit and Rivat in their
papers on the sum of digits of primes and squares [27, 28].

Lemma 4.5. Let r, N, λ be nonnegative integers and α > 0, β ≥ 0 real numbers. Assume that
I is an interval containing N integers. Then
∣
∣
{n ∈ I : s(
⌊(n + r)α + β⌋) − s(
⌊nα + β⌋) ̸= sλ(
⌊(n + r)α + β⌋)
−sλ(
⌊nα + β⌋)}∣
∣

≤ r(N α/2λ + 2).

Let Fn the set of rational numbers p/q such that 1 ≤ q ≤ n, the Farey series of order n. Each
a ∈ Fn has two neighbours aL, aR ∈ Fn, satisfying aL < a < aR and (aL, a)∩Fn = (a, aR)∩Fn =
∅. We have the following elementary lemma concerning this set (see [20, chapter 3]).

Lemma 4.6. Assume that a/b, c/d are reduced fractions such that b, d > 0 and a/b < c/d.
Then a/b < (a + c)/(b + d) < c/d. If a/b and c/d are neighbours in the Farey series Fn, then
bc − ad = 1 and b + d > n, moreover

(a + c)/(b + d) − a/b < 1
bn and c/d − (a + c)/(b + d) < 1
dn .

Let α ∈ R and Q a positive integer. We assign a fraction pQ(α)/qQ(α) to α according to
the Farey dissection of the reals: consider reduced fractions a/b < c/d that are neighbours in
the Farey series FQ, such that a/b ≤ α < c/d. If α < (a + c)/(b + d), then set pQ(α) = a and
qQ(α) = b, otherwise set pQ(α) = c and qQ(α) = d. Lemma 4.6 implies

(4.5) ∣
∣qQ(α)α − pQ(α)
∣
∣ < Q−1.

We will call an interval of the form {α ∈ R : pQ(α) = p, qQ(α) = q} a Farey interval around
p/q.
 5. Proof of Propositions 3.1 and 3.2

As in the proof of Proposition 2.5 in [31], it is suﬃcient to prove that there exists η > 0 and
a constant C such that S0(N, 2ν, ξ)
N 2ν ≤ CN −η

for all real numbers ξ and for all positive integers N and ν such that there exists a real number
D ≥ 1 satisfying N ρ1 ≤ D ≤ N ρ2 and D < 2ν ≤ 2D, where S0 is deﬁned according to (3.1)
and (3.2).
In order to treat the two propositions to some extent in parallel, we will work with two
measures µ: for Proposition 3.1 we take the measure deﬁned by µ(A) = |A ∩ Z|, while for
Proposition 3.1, µ is the Lebesgue measure. Moreover, we note that in this proof, implied
constants in estimates depend only on m.
By Cauchy–Schwarz, followed by van der Corput’s inequality (4.4) (R0 will be speciﬁed later),
we obtain

∣
∣S0(N, 2ν, ξ)
∣
∣2 ≤ 2ν N + R0
R0
 ∫ 2
ν+1

2ν sup
β≥0
 ∑

0≤|r0|<R0
(
1 − |r0|
R0
 ) e(
r0ξ)

× ∑

0≤n<N
0≤n+r0<N
 e
( 1
2 s(
⌊(n + r0)α + β⌋) − 1
2 s(
⌊nα + β⌋)
)
 dµ(α)

LEVEL OF DISTRIBUTION OF THUE–MORSE 11

We apply the “carry propagation lemma” (Lemma 4.5), treat the summand r0 = 0 separately,
and omit the condition 0 ≤ n + r0 < N . Moreover, we consider r0 and −r0 synchronously. In
this way we obtain for all λ ≥ 0

∣
∣S0(N, 2ν, ξ)
∣
∣2 ≪ (
2νN )2E0 + 2νN
R0
 ∑

1≤r0<R0

× ∫ 2
ν+1

2ν sup
β≥0

∣
∣
∣
∣
∣
 ∑

0≤n<N e
( 1
2 sλ(
⌊(n + r0)α + β⌋) − 1
2 sλ(
⌊nα + β⌋)
)∣
∣
∣
∣
∣ dµ(α),

where
 E0 = 1
R0 + R0 2ν

2λ + R0
N .

We apply Cauchy–Schwarz on the sum over r0 and the integral over α in order to prepare
our expression for another application of van der Corput’s inequality. It follows that

∣
∣S0(N, 2ν, ξ)
∣
∣4 ≪ 23νN 2

R0
 ∑

1≤r0<R0
 ∫ 2
ν+1

2ν sup
β≥0

∣
∣S1∣
∣2 dµ(α) + (
2νN )4E0

where
 S1 = ∑

0≤n<N e
( 1
2 sλ(
⌊(n + r0)α + β⌋) − 1
2 sλ(
⌊nα + β⌋))

.

(Note that the error term is also squared, but if it is larger or equal to 1, the estimate is
trivial anyway. We will use this argument again in a moment.) We apply van der Corput’s
inequality (4.4) with R = R1 and K = K1 to be chosen later:

∣
∣S1∣
∣2 ≤ N + K1(R1 − 1)
R1
 ∑

0≤|r1|<R1
(
1 − |r1|
R1
 )

× ∑

0≤n<N
0≤n+r1K1<N
 e
( 1
2
 ∑

ε0,ε1∈{0,1} sλ(
⌊(n + ε0r0 + ε1r1K1)α + β⌋)
)
,

therefore, taking together the summands for r1 and −r1 and omitting the condition 0 ≤ n +
r1K1 < N ,

∣
∣S0(N, 2ν, ξ)
∣
∣4 ≪ 23νN 3

R0 R1
 ∑

1≤r0<R0
0≤r1<R1
 ∫ 2
ν+1

2ν sup
β≥0

∣
∣S2∣
∣ dµ(α) + (
2νN )4(
E0 + E1)
,

where
 S2 = ∑

0≤n<N e

( 1
2
 ∑

ε0,ε1∈{0,1} sλ(
⌊(n + ε0r0 + ε1r1K1)α + β⌋)
)

and
 E1 = R1K1
N .

Cauchy–Schwarz over r0, r1 and α yields

∣
∣S0(N, ν, ξ)
∣
∣8 ≪ 27νN 6

R0R1
 ∑

1≤r0<R0
0≤r1<R1
 ∫ 2
ν+1

2ν sup
β≥0
|S2|2 dµ(α) + (
2νN )8(
E0 + E1)
.

12 LUKAS SPIEGELHOFER

We apply van der Corput’s inequality with R = R2 and K = K2 to be chosen later:
∣
∣S0(N, 2ν, ξ)
∣
∣8
(
2νN )8 ≪ (
E0 + E1 + E2) + 1
R0R1R22νN
 ∑

1≤r0<R0
0≤r1<R1
0≤r2<R2
 ∫ 2
ν+1

2ν sup
β≥0

∣
∣S3∣
∣ dµ(α)

where
 S3 = ∑

0≤n<N e
( 1
2
 ∑

ε0,ε1,ε2∈{0,1} sλ(
⌊nα + β + ε0r0α + ε1r1K1α + ε2r2K2α⌋))

and E2 = R2K2/N. Continuing in this manner and replacing the range of integration (we note
that we are going to choose λ > ν later), we obtain

(5.1) ∣
∣
∣
∣ S0(N, 2ν, ξ)
2νN
 ∣
∣
∣
∣

2
m+1
 ≪ (
E0 + E1 + · · · + Em)

+ 1
R0R1 · · · Rm2νN
 ∑

1≤r0<R0
0≤ri<Ri,1≤i≤m
 ∫ 2
λ

0 sup
β≥0
 ∣
∣S4∣
∣ dµ(α),

where

S4 = ∑

0≤n<N e
( 1
2
 ∑

ε0,...,εm∈{0,1} sλ(⌊nα + β + ε0r0α + ε1r1K1α + · · · + εmrmKmα⌋)
)

and
 E0 = 1
R0 + R0 2ν

2λ + R0
N ,

Ei = Ri Ki
N for 1 ≤ i ≤ m.

Now we choose the multiples K1, . . . , Km in such a way that the number of digits to be taken
into account is reduced from λ to ρ := λ − (m + 1)µ, where µ is chosen later. For this we use
Farey series, see (4.5). Let

K1 = q22µ+2σ ( α
22µ
 ) q2σ ( p22µ+2σ (
α/22µ)

2(m−1)µ
 )
;

Ki = q2µ+2σ ( α
2(i+1)µ
 ) q2σ ( p2µ+2σ (
α/2(i+1)µ)

2(m−i)µ
 ) for 2 ≤ i < m;

Km = q2µ+σ ( α
2(m+1)µ
 ) ,

where σ is chosen later. Moreover, we set

M1 = p22µ+2σ ( α
22µ
 )q2σ
 ( p22µ+2σ (
α/22µ)

2(m−1)µ
 )
 ;

Mi = p2µ+2σ ( α
2(i+1)µ
 )q2σ
 ( p2µ+2σ (
α/2(i+1)µ)

2(m−i)µ
 )
 for 2 ≤ i < m;

Mm = p2µ+σ ( α
2(m+1)µ
 )
.

By Lemma 4.6, estimating the second factor in the deﬁnition of Ki and Mi by 2σ, we have

LEVEL OF DISTRIBUTION OF THUE–MORSE 13

∣
∣K1α − 22µM1∣
∣ < 2−σ;
∣
∣
∣
∣ Kiα
2iµ − 2µMi
∣
∣
∣
∣ < 2−σ for 2 ≤ i < m;(5.2) ∣
∣
∣
∣ Kmα
2mµ − 2µMm
∣
∣
∣
∣ < 2−σ.

We are going to use these inequalities in order to replace riKiα in the sum S4, starting with
r1K1α. We treat the case that α is an integer ﬁrst: in this case, K1α = 22µM1, and by the fact
that the arguments of sλ corresponding to ε1 = 0, 1 diﬀer by a multiple of 22µ we may shift the
argument by 2µ digits and thus reduce the number of digits to be taken into account from λ to
λ − 2µ.

S4 = ∑

0≤n<N e
( 1
2
 ∑

ε0,...,εm∈{0,1} s2µ,λ (⌊nα + β

+ε0r0α + ε1r1M122µ + ε2r2K2α + · · · + εmrmKmα
⌋)
)

= ∑

0≤n<N e
( 1
2
 ∑

ε0,...,εm∈{0,1} sλ−2µ
(⌊ nα + β
22µ + ε0r0α
22µ +ε1r1M1+ ε2r2K2α
22µ +· · ·+ εmrmKmα
22µ
 ⌋))
.

In the case α ̸∈ Z, we use the inequalities (5.2) and the argument that nα-sequences are usually
not close to an integer. This can be made precise as follows. Assume that

(5.3) ∥nα + β′∥ ≥ R1/2σ,

where β′ = β + ε0r0α + ε2r2K2α + · · · + εmrmKmα, and that 2R1 < 2σ. Using the inequal-
ity (4.3) in Lemma 4.1 with ε = 1/2σ, where σ ≥ 1 is chosen later, and (4.5), we obtain
〈
r1K1α
〉 = r1〈K1α
〉 = r122µM1.

Applying (4.1), setting ε = R1/2σ, we see that (5.3) together with (5.2) implies

⌊nα + r1K1α + β′⌋ = ⌊nα + r122µM1 + β′⌋.

The number of n where hypothesis (5.3) fails for some ε0, ε2, . . . , εm can be estimated by dis-
crepancy estimates for {nα}-sequences: for all positive integers N and 2R1 < 2σ we have
∣
∣{
n ∈ [0, N − 1] : ∥nα + β′∥ ≤ R1/2σ}∣
∣

= ∣
∣
{n ∈ [0, N − 1] : nα + β′ ∈ [−R1/2σ, R1/2σ] + Z
}∣
∣

= ∣
∣
{n ∈ [0, N − 1] : nα ∈ [0, 2R1/2σ] − β′ − R1/2σ + Z
}∣
∣

≤ N DN (α) + 2R1N/2σ.

Therefore, the number of n ∈ [0, N − 1] such that ∥nα + β′∥ ≤ R1/2σ for some ε0, ε2, . . . , εm ∈
{0, 1} is bounded by 2mN (
DN (α)+2R1/2σ)
, which is ≪ N (
DN (α)+2R1/2σ) by our convention
that implied constants may depend on m.
We replace K1α by 22µM1 and subsequently shift the digits by 2µ and obtain

S4 = O(
N DN (α) + N R1/2σ) + ∑

0≤n<N e
( 1
2
 ∑

ε0,...,εm∈{0,1} sλ−2µ
(⌊ nα + β
22µ

14 LUKAS SPIEGELHOFER

+ ε0r0α
22µ + ε1r1M1 + ε2r2K2α
22µ + · · · + εmrmKmα
22µ
 ⌋))
.

Repeating this argument for all i ∈ {2, . . . , m}, we obtain

S4 = N O ( ̃DN (α) + DN ( α
22µ
 ) + · · · + DN ( α
2mµ
 ) + R1 + · · · + Rm
2σ
 )

+ ∑

0≤n<N e
( 1
2
 ∑

ε1,...,εm∈{0,1} sλ−(m+1)µ
(⌊ nα + β
2(m+1)µ + ε0r0α
2(m+1)µ + ∑

1≤i≤m
 εiriMi
2(m−i)µ
 ⌋))
,

where ̃DN (α) = DN (α) if α ̸∈ Z and ̃DN (α) = 0 otherwise.
Now the second factor in the deﬁnition of Ki comes into play. We use the deﬁnition of
Mi together with the approximation property (4.5), and apply the discrepancy estimate for
nα-sequences again to obtain

(5.4) S4 = N O ( ̃DN (α) + DN ( α
22µ
 ) + · · · + DN ( α
2(m+1)µ
 ) + R1 + · · · + Rm
2σ
 ) + S5,

where
S5 = ∑

0≤n<N e
( 1
2
 ∑

ε0,...,εm∈{0,1} sλ−(m+1)µ
(⌊ nα + β
2(m+1)µ + ε0r0α
2(m+1)µ
 ⌋ + ∑

1≤i≤m εiripi
))
,

and
 p1 = p2σ
 ( p22µ+2σ (
α/22µ)

2(m−1)µ
 )
 ;

pi = p2σ
 ( p2µ+2σ (
α/2(i+1)µ)

2(m−i)µ
 )
 for 2 ≤ i < m;(5.5)
 pm = p2µ+σ ( α
2(m+1)µ
 ) .

Our next goal is to remove the Beatty sequence occurring in S5, and also to remove the
integers pi. The resulting expression can be handled by the Gowers norm estimate given in
Proposition 3.3, which will ﬁnish the proof.
We start by splitting the Beatty sequence into two summands. Let t, T be integers such that
0 ≤ t < T and deﬁne

S6 = ∑

0≤n<N

t
T ≤{ nα+β
2(m+1)µ }< t+1
T
 e
( 1
2
 ∑

ε0,...,εm∈{0,1} sλ−(m+1)µ
(⌊ nα + β + ε0r0α
2(m+1)µ
 ⌋ + ∑

1≤i≤m εiripi
))
.

We deﬁne
 G = {
1 ≤ t < T : [ t
T + ε0r0α
2(m+1)µ , t + 1
T + ε0r0α
2(m+1)µ
 ) ∩ Z = ∅}
.

Clearly we have |G| ≥ T − 2, since we have to exclude at most one t. For t ∈ {0, . . . , T − 1} \ G
we estimate S6 trivially, using Lemma 4.3: we obtain

(5.6) S6 ≪ N
T + N DN ( α
2(m+1)µ
 ) .

Assume that t ∈ G and that t/T ≤ {(nα + β)/2(m+1)µ} < (t + 1)/T . Then
⌊ nα + β
2(m+1)µ
 ⌋ + t
T + ε0r0α
2(m+1)µ ≤ nα + β + ε0r0α
2(m+1)µ < ⌊ nα + β
2(m+1)µ
 ⌋ + t + 1
T + ε0r0α
2(m+1)µ

LEVEL OF DISTRIBUTION OF THUE–MORSE 15

and the assumption t ∈ G gives
⌊ nα + β + ε0r0α
2(m+1)µ
 ⌋ = ⌊ nα + β
2(m+1)µ
 ⌋ + ⌊ t
T + ε0r0α
2(m+1)µ
 ⌋

for ε0 ∈ {0, 1}. From these observations we obtain for t ∈ G:

S6 = ∑

0≤k<2ρ
 ∑

0≤n<N

t
T ≤{ nα+β

2(m+1)µ }< t+1
T⌊ nα+β

2(m+1)µ ⌋≡k mod 2
ρ
 e
( 1
2
 ∑

ε0,...,εm∈{0,1} sρ
(
k + ⌊ t
T + ε0r0α
2(m+1)µ
 ⌋ + ∑

1≤i≤m εiripi
))
.

Note that the Beatty sequence ⌊(nα + β)/2(m+1)µ⌋ does not occur in the summand any more.
We may therefore remove the second summation by estimating the number of times the three
conditions under the summation sign are satisﬁed. At this point we want to stress the fact that
N is going to be signiﬁcantly larger than 2ρ = 2λ−(m+1)µ. Using Lemma 4.3 and the usually
very small discrepancy of nα-sequences, this fact will enable us to remove the summation over
n, while introducing only a negligible error term for most α. This is the point in the proof where
the successive “cutting away” of binary digits with the help of Farey series pays oﬀ.
By Lemma 4.3, applied with K = 2ρ, and noting that λ = (m + 1)µ + ρ, we obtain for t ∈ G

(5.7) S6 = N
2ρT S7 + O (2ρN DN ( α
2λ
 )) ,

where
 S7 = ∑

0≤k<2ρ e
( 1
2
 ∑

ε0,...,εm∈{0,1} sρ
(
k + ⌊ t
T + ε0r0α
2(m+1)µ
 ⌋ + ∑

1≤i≤m εiripi
))

.

We note the important fact that this expression is independent of β. This will allow us to
remove the maximum over β inside the integral over α, and thus prove the strong statement on
the level of distribution.
We wish to simplify this expression in such a way that Proposition 3.3 is applicable. To this
end, we use the summation over ri and the integral over α. We deﬁne

S8 = ∫ 2
λ

0
 ∑

0≤r1,...,rm<2
ρ
∣
∣S7∣
∣ dµ(α),

which is an expression that will appear when we expand the original sum S0.
We are going to apply the argument that for most α < 2λ (with respect to µ) the 2-valuation
of p1, . . . , pm is small. For these α, the term ripi mod 2ρ attains each k ∈ {0, . . . , 2ρ − 1} not
too often, as ri runs. We may therefore replace rip1 by ri and thus obtain full sums over ri (we
note that we will set Ri = 2ρ for 1 ≤ i ≤ m). In order to make this argument work, we are
going to utilize the following technical result, the proof of which we give in section 5.2.

Lemma 5.1. Let µ, λ, σ, γ, m be nonnegative integers such that m ≥ 2 and

(5.8) λ ≥ (m + 1)µ, γ ≤ λ − (m + 1)µ,
µ ≥ 4σ, σ ≥ γ ≥ 1.

Let p1, . . . , pm be deﬁned by (5.5) and set

A = {α ∈ {0, . . . , 2λ − 1} : 23γ | pi for some i = 1, . . . , m}.

Then |A| = O(2λ−γ)
.

16 LUKAS SPIEGELHOFER

Analogously, if A = {α ∈ [0, 2λ] : 23γ | pi for some i = 1, . . . , m}.
Then λ(A) = O(2λ−γ)
,
where λ is the Lebesgue measure. The implied constants are independent of µ, λ, σ, and γ.

Let A be deﬁned as in this lemma. We choose Ri = 2ρ for 1 ≤ i ≤ m.
Assume that α ̸∈ A. Then by an elementary argument, ripi mod 2ρ attains each value not
more than 23γ times, as ri runs through {0, . . . , 2ρ − 1}. The contribution for α ∈ A will be
estimated trivially by the lemma. We obtain

S8 ≤ O (2λ+(m+1)ρ−γ) + 23γm ∫ 2
λ

0
 ∑

0≤r1,...,rm<2ρ |S9| dµ(α),

where
 S9 = ∑

0≤n<2ρ e
( 1
2
 ∑

ε0,...,εm∈{0,1} sρ
(
n + ⌊ t
T + ε0r0α
2(m+1)µ
 ⌋ + ∑

1≤i≤k εiri
))
.

The next step is removing the remaining ﬂoor function, using the integral over α. In the
continuous case, the expression ⌊
t/T + r0K0α/2(m+1)µ⌋ mod 2ρ runs through {0, . . . , 2ρ − 1} in
a completely uniform manner. That is, for r0 ̸= 0 we have

λ ({
α ∈ [0, 2λ] : ⌊t/T + r0α/2(m+1)µ⌋ ≡ k mod 2ρ}) = 2λ−ρ,

where λ is the Lebesgue measure. We consider the discrete case. Assume that r0 ≤ 2(m+1)µ

(we will choose R0 very small at the end of the proof, so that this will be satisﬁed). Then the
set of α ∈ {0, . . . , 2λ − 1} such that ⌊t/T + r0α/2(m+1)µ⌋ ≡ k mod 2ρ decomposes into at most
r0 + 1 many intervals (note that λ = (m + 1)µ + ρ), each having ≤ 2(m+1)µ/r0 + 1 elements. In
total we have ≪ 2λ−ρ elements, where the implied constant is absolute. It follows that

S8 ≪ 2λ+(m+1)ρ−γ + 2λ−ρ+3γm ∑

0≤r0,...,rm<2ρ|S10(r0, . . . , rm)|,

where
 S10(r0, . . . , rm) = ∑

0≤n<2ρ e
 

 1
2
 ∑

ε0,...,εm∈{0,1} sρ
 

n + ∑

0≤i≤m εiri






 .

As a ﬁnal step in the procedure of reducing the main theorems to Proposition 3.3, we are
going to to remove the absolute value around S10. For brevity, we set

g(n) = ∑

ε0,...,εm∈{0,1} sρ
 

n + ∑

0≤i≤m εiri




By the 2ρ-periodicity of g we have
∑

0≤r0,...,rm<2ρ|S10(r0, . . . , rm)|2 = ∑

0≤r0,...,rm<2ρ
 ∑

0≤n1,n2<2ρ e ( 1
2 g(n1) + 1
2 g(n2)
)

= ∑

0≤r0,...,rm<2ρ
 ∑

0≤n1<2ρ
 ∑

0≤rm+1<2ρ e ( 1
2 g(n1) + 1
2 g(n1 + rm+1)
)

= ∑

0≤r0,...,rm+1<2ρ
 ∑

0≤n1<2ρ e ( 1
2 g(n1) + 1
2 g(n1 + rm+1)
)

LEVEL OF DISTRIBUTION OF THUE–MORSE 17

= ∑

0≤r0,...,rm+1<2ρ
 ∑

0≤n1<2ρ e
 

 1
2
 ∑

ε0,...,εm∈{0,1}
 ∑

εm+1∈{0,1} sρ(n1 + ε · r + εm+1rm+1)





= ∑

0≤r0,...,rm+1<2ρ S10(r0, . . . , rm+1).

We have therefore removed the absolute value around S10 for the price an additional variable
rm+1. This means that we have reduced our main theorems to Proposition 3.3.
By this Proposition and Cauchy-Schwarz we obtain

(5.9) S8 ≪ 2λ+(m+1)ρ (
2−γ + 23γm−ηρ)

for some η > 0.
It remains to collect the error terms and to choose values for the free variables. Using (5.7)
and (5.6), we obtain

S5 ≪ ∑

t̸∈G O ( N
T + N DN ( α
2(m+1)µ
 )) + ∑

t∈G
 ( N
2ρT S7 + O (2ρN DN ( α
2λ
 )))

= N
2ρT
 ∑

t∈G S7 + O ( N
T + N DN ( α
2(m+1)µ
 ) + 2ρN T DN ( α
2λ
 ))

and by (5.4) and (5.1) we obtain

(5.10) ∣
∣
∣
∣ S0(N, ν, ξ)
2νN
 ∣
∣
∣
∣
2
m+1
 ≪ O ( 1
R0 + R0 2ν

2λ + R0
N + R1K1
N · · · + RmKm
N
 )

+ 1
2νN
 ∫ 2
λ

0 N O ( ̃DN (α) + DN ( α
22µ
 ) + · · · + DN ( α
2(m+1)µ
 ) + R1 + · · · + Rm
2σ
 ) dµ(α),

+ 1
2νN
 ∫ 2
λ

0 O ( N
T + N DN ( α
2(m+1)µ
 ) + 2ρN T DN ( α
2λ
 )) dµ(α),

+ 1
R0 · · · Rm2νN N
2ρT
 ∑

t∈G
 ∑

1≤r0<R0
 ∫ 2
λ

0
 ∑

0≤r1,...,rm<2
ρ
∣
∣S7∣
∣ dµ(α).

We employ the mean discrepancy estimates from Lemma 4.4. Assume that δ ≤ λ. In the
continuous case we have

1
2ν
 ∫ 2
λ

0 DN ( α
2δ
 ) dα ≪ 2λ−ν−δ ∫ 2
δ

0 DN ( α
2δ
 ) dα ≪ 2λ−ν (log+N )
2

N ,

while the discrete case gives

1
2ν ∑

0≤d<2λ DN
 ( d
2δ
 ) ≪ 2λ−δ−ν N + 2δ

N (log+N )
2 = 2λ−ν(log+N )
2 ( 1
N + 1
2δ
 )

In total, noting that λ ≥ (m + 1)µ, the discrepancy terms can be estimated by

≪ 2λ−ν(log+N )
22ρT ( 1
N + 1
22µ
 ) .

By (5.9), the last summand in (5.10) can be estimated by

≪ 2λ−ν (
2−γ + 23γm−ηρ) .

Moreover, using the facts R1 = · · · = Rm = 2ρ and Ki ≤ 22µ+3σ for 1 ≤ i ≤ m, we obtain

18 LUKAS SPIEGELHOFER

(5.11) ∣
∣
∣
∣ S0(N, ν, ξ)
2νN
 ∣
∣
∣
∣
2
m+1
 ≪ 1
R0 + R0 2ν

2λ + R0
N + 2ρ+2µ+3σ

N +

2λ−ν(log+N )
22ρT ( 1
N + 1
22µ
 ) + 2ρ−σ+λ−ν + 1
T + 2λ−ν (
2−γ + 23γm−ηρ)

with some implied constant only depending on m. Collecting also the requirements on the
variables we assumed in the course of our calculation, we see that this estimate is valid as long
as

(5.12)
 R0, T ≥ 1, m ≥ 2, γ, ν, λ, ρ, µ ≥ 0, R1 = · · · = Rm = 2ρ,

λ > ν, ρ = λ − (m + 1)µ,

γ ≤ ρ < σ − 1, µ ≥ 4σ,

R0 ≤ 2(m+1)µ.

It remains to choose the variables within these constraints. Choose the integer j ≥ 1 in such
a way that N j−1 ≤ 2ν < N j and set m = 3j − 1. Clearly, m ≥ 2. We deﬁne

µ = ⌊ ν
m + 1 + 1/8
 ⌋ , σ = ⌊µ/4⌋, ̃ρ = ν − (m + 1)µ.

We obtain the inequalities N ≥ 23µ, µ ≥ 4σ, ̃ρ ≥ 0. Moreover, for large ν we obtain ̃ρ ∼ µ/8.
Choose γ = ⌊̃ρη/(6m)⌋ and R0 = ⌊2γ/4⌋. Then the last summand in (5.11) is ≪ 2λ−ν(
2−γ +
2−̃ρη/2)
≪ 2λ−ν−γ. Finally, set λ = ν + ⌊γ/2⌋, T = 2γ and ρ = λ − (m + 1)µ. It follows that
ρ = ̃ρ + ⌊γ/2⌋ ∼ µ
8 (1 + η/(12m)) ≤ µ/8 + µ/192. Using these deﬁnitions, it is not hard to see
that, for large N and ν, the requirements (5.12) are met.
Moreover, using the statements N ρ1 ≤ D ≤ N ρ2 and D < 2ν ≤ 2D we can easily esti-
mate (5.11) term by term and conclude that S0(N, ν, ξ)/(2νN ) ≤ CN −η′ for some η′ > 0 and
some constant C. This ﬁnishes the proof of Propositions 3.1 and 3.2 and therefore of our main
theorems. It remains to prove our auxiliary results.

5.1. Proof of Proposition 3.3. We utilize ideas from the paper [21] by Konieczny. Set

Aρ(a) = 1
2(m+1)ρ ∑

0≤n<2
ρ
0≤r1,...,rm<2
ρ
 e
 

 1
2
 ∑

ε∈{0,1}m sρ(n + ε · r + aε)



 .

Then in analogy to equation (16) of [21], we get after a similar calculation (using m ≥ 2)

(5.13) Aρ+1(a) = (−1)
|a|

2m+1 ∑

e0,...,em∈{0,1} Aρ(δ(a, e)),

where |a| = ∑
ε∈{0,1}m aε and

δ(a, e)ε = ⌊ aε + e0 + ∑
1≤i≤m εiei
2
 ⌋ .

We deﬁne a directed graph with weighted edges according to (5.13). The set of vertices is
given by the set of families a ∈ Z
{0,1}
m . There is an edge from a to b if and only if there is an
e = (e0, . . . , em) ∈ {0, 1}m+1 such that δ(a, e) = b and this edge has the weight

w(a, b) = (−1)
|a|

2m+1 ∣
∣
{e ∈ {0, 1}m+1 : δ(a, e) = b}∣
∣ .

LEVEL OF DISTRIBUTION OF THUE–MORSE 19

Note that

(5.14) ∑

b∈Z{0,1}m|w(a, b)| = 1,

which we will need later. We are interested in the subgraph (V, E, w) induced by the set of
vertices reachable from 0. This graph is ﬁnite: we have

max
ε∈{0,1}m|δ(a, e)ε| ≤ 1
2
 ( max
ε∈{0,1}m|aε| + m + 1)

and by induction, it follows that maxε∈{0,1}m |aε| < m + 1 for all a ∈ V , which implies the
ﬁniteness of V .
Moreover, this subgraph is strongly connected. We prove this by showing that 0 is reachable
from each a ∈ V . This follows immediately by considering the path (a = a
(0), a
(1)), . . . , (a
(k), a
(k+1))
deﬁned by a
(j+1) = δ(a
(k), (0, . . . , 0)). It is clear from the deﬁnition of δ that such a path reaches
0 if k is large enough.
We wish to apply (5.13) recursively. We therefore deﬁne, for two vertices a, b ∈ V and a
positive integer k, the weight wk(a, b) as the sum of all weights of paths of length k from a to
b. (Here the weight of a path is the product of the weights of the edges.)
In order to prove Proposition 3.3, it is suﬃcient to prove that there is a k such that
∑

b∈V |wk(a, b)| < 1

for all a ∈ V . In order to prove this, it is suﬃcient, by the strong connectedness of the
graph and (5.14), to prove that there are two paths of the same length from 0 to 0 such
that their respective weights have diﬀerent sign. One of this paths is the trivial one, choosing
e0 = · · · = em = 0 in each step. This path has positive weight.
For the second path, we follow Konieczny [21, proof of Proposition 2.3]. As in that paper,
we deﬁne a
(0) = a
(m+1) = 0 and for 1 ≤ j ≤ m,

a
(j)
ε =
 {1, if ε1 = · · · = εj = 1;
0, otherwise.

Assuming for a moment that there is an edge from a
(j) to a
(j+1) for all j ∈ {0, . . . , m}, it is
easy to see that each edge (a
(j), a
(j+1)) has positive weight for 0 ≤ j < m, while (a
(m), a
(m+1))
has negative weight. Proving that these vertices indeed deﬁne a path is contained completely
in the argument given by Konieczny. This ﬁnishes the proof of Lemma 3.3.

5.2. Proof of Lemma 5.1. We choose an integer γ > 0 and bound the size of the set of α < 2λ

such that 23γ | pi for some i ∈ {1, . . . , m}. We will need the following two lemmas.

Lemma 5.2. Let λ be the Lebesgue measure. Assume that K ≥ 1 and γ ≥ 0 are integers. Then

λ(
{x ∈ [0, 1] : 2γ | qK(x)}) ≪ 1
2γ + 1
K .

The constant in this estimate is absolute.

Proof. We have to sum up the lengths of the Farey intervals around p/q such that 2γ | q. By
Lemma 4.6, each such fraction contributes at most 2/(Kq). By summing over p ∈ {1, . . . , q},
this gives a contribution 2/K for each multiple q of 2γ, and we obtain a total contribution

≪ ∑

1≤q≤K
2
γ |q
 1
K ≤ 1
2γ + 1
K .
 □

20 LUKAS SPIEGELHOFER

Lemma 5.3. Let x0, . . . , xM−1 ∈ [0, 1] and δ > 0. Assume that ∥xi − xj ∥ ≥ δ for i ̸= j. Then

∣
∣{n ∈ {0, . . . , M − 1} : 2γ | qK(xi)}∣
∣ ≪ K 2

2γ + 1
δ
 ( 1
2γ + 1
K
 ) .

The implied constant is absolute.

Proof. In each Farey interval around p/q such that q is divisible by 2γ there are at most
2/(Kqδ) + 1 many points xi. By summing over p and q, we can bound the number of points in
such intervals by

≪ ∑

1≤q≤K
2
γ |q
 ∑

1≤p≤q
 ( 1
qKδ + 1) = ∑

1≤q≤K
2
γ |q
 ( 1
Kδ + q) = (
K2−γ + 1) 1
Kδ + ∑

1≤q≤K
2
γ |q
 q

≤ 1
2γδ + 1
Kδ + 2γ ∑

1≤q′≤⌊K2−γ ⌋ q′ ≪ K 2

2γ + 1
2γδ + 1
Kδ . □

We proceed to the proof of Lemma 5.1. Consider p1 and the case “α discrete”. In this
case, we have p22µ+2σ (α/22µ) = α. Assume therefore that α = α0 + 2(m−1)µα1, where α0 ∈
{0, . . . , 2(m−1)µ − 1} and α1 ∈ {0, . . . , 2λ−(m−1)µ − 1}.
Then
 p1 = p2σ (
α/2(m−1)µ) = p2σ (
α0/2(m−1)µ) + q2σ (
α0/2(m−1)µ)
α1.

By Lemma 5.3, using also (5.8), it follows that the number of α0 ∈ {0, . . . , 2(m−1)µ − 1} such
that 2γ ∤ q2σ (
α0/2(m−1)µ) is 2(m−1)µ (1 − O(2−γ)). For each such α0, we let α1 run through
{0, . . . , 2λ−(m−1)µ − 1}. Then two occurrences α1, α
′
1 such that 22γ | p1 are separated by at
least 2γ steps; it follows that the number of such α1 is bounded by 2λ−(m−1)µ−γ. Putting these
errors together, we see that the number of α ∈ {0, . . . , 2λ − 1} such that 22γ ∤ p1 is given by
2(m−1)µ (1 − O(2−γ)) 2λ−(m−1)µ (1 − O(2−γ)) = 2λ (1 − O(2−γ)).
Next, we consider the continuous case. We write α = α0 + 22µα1 + 2(m+1)µα2 , where
α0 ∈ [0, 22µ) is real and α1 < 2(m−1)µ and α2 < 2λ−(m+1)µ are nonnegative integers. Set
p = p22µ+2σ (
α0/22µ) and q = q22µ+2σ (
α0/22µ)
. Then

p22µ+2σ (
α/22µ)

2(m−1)µ = p + (
α1 + 2(m−1)µα2)
q
2(m−1)µ = p + α1q
2(m−1)µ + α2q.

By the approximation property (4.5) (note that σ ≥ 1) we have

p1 = 〈( p + α1q
2(m−1)µ + α2q) q2σ ( p + α1q
2(m−1)µ
 )〉

= 〈 p + α1q
2(m−1)µ q2σ ( p + α1q
2(m−1)µ
 )〉 + α2q q2σ ( p + α1q
2(m−1)µ
 )

and we note that the ﬁrst summand does not depend on α2.
As α0 runs through [0, 22µ], we have by Lemma 5.2 2γ ∤ q in a set of measure 22µ(1 − O(2−γ +
2−2µ−2σ)). By (5.8), this is 22µ(
1 − O(2−γ))
. Assume that α0 is such that 2γ ∤ q and set
γ′ = ν2(q) < γ. Next, we let α1 run. We choose xj = {(p+ jq)/2(m−1)µ} for 0 ≤ j < 2(m−1)µ−γ′

and we note that these points satisfy ∥xi − xj ∥ ≥ 1/2(m−1)µ−γ′ for i ̸= j. By Lemma 5.3 it
follows that
{
α1 ∈ {0, . . . , 2(m−1)µ−γ′ − 1} : 2γ | q2σ ( p + α1q
2(m−1)µ
 )} ≪ 22σ

2γ + 2(m−1)µ−γ′ ( 1
2γ + 1
2σ
 ) .

LEVEL OF DISTRIBUTION OF THUE–MORSE 21

By (5.8), this is ≪ 2(m−1)µ−γ′−γ. Performing this also for the other intervals of length 2(m−1)µ−γ′,
we obtain {
α1 ∈ {0, . . . , 2(m−1)µ − 1} : 2γ | q2σ ( p + α1q
2(m−1)µ
 )} ≪ 2(m−1)µ−γ.

Finally, α2 runs through {0, . . . , 2λ−(m+1)µ − 1} and we consider p1. For given good α1 and
α0 (such that 2γ ∤ q and 2γ ∤ q2σ ((p + α1q)/2(m−1)µ)), p1 is an arithmetic progression in α2
whose common diﬀerence is not divisible by 22γ. Similarly to the discrete case, it follows that
p1 is divisible by 23γ for at most 2λ−(m+1)µ−γ many α2. It follows that there is a set of measure

22µ(
1 − O(2−γ)
)2(m−1)µ(1 − O(2−γ)
)2λ−(m+1)µ(
1 − O(2−γ)
) = 2λ(1 − O(2−γ)
)

of α < 2λ such that 23γ ∤ p1.
The cases 2 ≤ i ≤ m do not require any new ideas; we only give a sketch of a proof. Let
2 ≤ i < m. We treat the discrete and continuous cases in parallel. We write α = α0 +2(i+1)µα1 +
2(m+1)µα2, where α0 < 2(i+1)µ, and α1 < 2(m−i)µ and α2 < 2λ−(m+1)µ are nonnegative integers.
Set p = p2µ+2σ (
α0/2(i+1)µ) and q = q2µ+2σ (
α0/2(i+1)µ)
. Then

pi = 〈 p + α1q
2(m−i)µ q2σ ( p + α1q
2(m−i)µ
 )〉 + α2q q2σ ( p + α1q
2(m−i)µ
 ) ,

as before. By Lemmas 5.2 and 5.3 we have 2γ ∤ q for α0 in a set of measure 2(i+1)µ(1 − O(2−γ)),
where we used 2µ + 4σ ≤ (i + 1)µ in the discrete case. (We note that this last inequality is the
reason for deﬁning p1 separately, using 22µ instead of 2µ.) The remaining steps are as before,
and this case is ﬁnished.
Finally, in the case i = m we write α = α0 + 2(m+1)µα1, where α0 < (m + 1)µ and α1 ∈
{0, . . . , 2λ−(m+1)µ − 1}. Then

pm = p2µ+σ (
α0/2(m+1)µ) + q2µ+σ (
α0/2(m+1)µ)
α1.

By Lemmas 5.2 and 5.3 and (5.8) we have 2γ | q2µ+σ (
α0/2(m+1)µ) for α0 in a set of measure
O(2(m+1)µ−γ) and the statement follows as before.
In total, we have a set of measure 2λ(
1 − O(2−γ)
) of α < 2λ such that 23γ ∤ pi for all i.

Acknowledgements

The author wishes to thank Thomas Stoll for helpful discussions during his stay in Nancy,
where the work on this project began. Moreover, the author wishes to thank Michael Drmota
and Clemens M¨ullner for several fruitful discussions on the topic. Finally, the author is indebted
to Etienne Fouvry for valuable advice.
 References

[1] J.-P. Allouche and J. Shallit, The ubiquitous Prouhet-Thue-Morse sequence, in Sequences and their
applications (Singapore, 1998), Springer Ser. Discrete Math. Theor. Comput. Sci., Springer, London, 1999,
pp. 1–16.
[2] , Automatic sequences, Cambridge University Press, Cambridge, 2003. Theory, applications, general-
izations.
[3] E. Bombieri, J. B. Friedlander, and H. Iwaniec, Primes in arithmetic progressions to large moduli, Acta
Math., 156 (1986), pp. 203–251.
[4] , Primes in arithmetic progressions to large moduli. II, Math. Ann., 277 (1987), pp. 361–393.
[5] , Primes in arithmetic progressions to large moduli. III, J. Amer. Math. Soc., 2 (1989), pp. 215–224.
[6] C. Dartyge and G. Tenenbaum, Congruences de sommes de chiﬀres de valeurs polynomiales, Bull. London
Math. Soc., 38 (2006), pp. 61–69.
[7] J.-M. Deshouillers, M. Drmota, and J. F. Morgenbesser, Subsequences of automatic sequences indexed
by ⌊nc⌋ and correlations, J. Number Theory, 132 (2012), pp. 1837–1866.
[8] M. Drmota, C. Mauduit, and J. Rivat, The Thue-Morse sequence along squares is normal. To appear in
J. Eur. Math. Soc.

22 LUKAS SPIEGELHOFER

[9] M. Drmota and J. Rivat, The sum-of-digits function of squares, J. London Math. Soc. (2), 72 (2005),
pp. 273–292.
[10] P. D. T. A. Elliott and H. Halberstam, A conjecture in prime number theory, in Symposia Mathematica,
Vol. IV (INDAM, Rome, 1968/69), Academic Press, London, 1970, pp. 59–72.
[11] E. Fouvry, R´epartition des suites dans les progressions arithm´etiques, Acta Arith., 41 (1982), pp. 359–382.
[12] , Autour du th´eor`eme de Bombieri-Vinogradov, Acta Math., 152 (1984), pp. 219–244.
[13] E. Fouvry and H. Iwaniec, On a theorem of Bombieri-Vinogradov type, Mathematika, 27 (1980), pp. 135–
152 (1981).
[14] E. Fouvry and C. Mauduit, M´ethodes de crible et fonctions sommes des chiﬀres, Acta Arith., 77 (1996),
pp. 339–351.
[15] , Sommes des chiﬀres et nombres presque premiers, Math. Ann., 305 (1996), pp. 571–599.
[16] J. Friedlander and H. Iwaniec, Opera de cribro., Providence, RI: American Mathematical Society (AMS),
2010.
[17] J. B. Friedlander and H. Iwaniec, Incomplete Kloosterman sums and a divisor problem, Ann. of Math.
(2), 121 (1985), pp. 319–350. With an appendix by Bryan J. Birch and Enrico Bombieri.
[18] A. O. Gel′fond, Sur les nombres qui ont des propri´et´es additives et multiplicatives donn´ees, Acta Arith.,
13 (1967/1968), pp. 259–265.
[19] D. A. Goldston, J. Pintz, and C. Y. Yıldırım, Primes in tuples. I, Ann. of Math. (2), 170 (2009),
pp. 819–862.
[20] G. H. Hardy and E. M. Wright, An introduction to the theory of numbers, Oxford, at the Clarendon
Press, 1954. 3rd ed.
[21] J. Konieczny, Gowers norms for the Thue-Morse and Rudin-Shapiro sequences, 2017. Preprint,
http://arxiv.org/abs/1611.09985.
[22] A. Kontorovich, Levels of distribution and the aﬃne sieve, Ann. Fac. Sci. Toulouse Math. (6), 23 (2014),
pp. 933–966.
[23] B. Martin, C. Mauduit, and J. Rivat, Th´eor´eme des nombres premiers pour les fonctions digitales, Acta
Arith., 165 (2014), pp. 11–45.
[24] C. Mauduit, Multiplicative properties of the Thue-Morse sequence, Period. Math. Hungar., 43 (2001),
pp. 137–153.
[25] C. Mauduit and J. Rivat, R´epartition des fonctions q-multiplicatives dans la suite ([nc])n∈N, c > 1, Acta
Arith., 71 (1995), pp. 171–179.
[26] , Propri´et´es q-multiplicatives de la suite ⌊nc⌋, c > 1, Acta Arith., 118 (2005), pp. 187–203.
[27] , La somme des chiﬀres des carr´es, Acta Math., 203 (2009), pp. 107–148.
[28] , Sur un probl`eme de Gelfond: la somme des chiﬀres des nombres premiers, Ann. of Math. (2), 171
(2010), pp. 1591–1646.
[29] J. Maynard, Small gaps between primes, Ann. of Math. (2), 181 (2015), pp. 383–413.
[30] Y. Moshe, On the subword complexity of Thue-Morse polynomial extractions, Theoret. Comput. Sci., 389
(2007), pp. 318–329.
[31] C. M¨ullner and L. Spiegelhofer, Normality of the Thue–Morse sequence along Piatetski-Shapiro se-
quences, II, Israel J. Math., 220 (2017), pp. 691–738.
[32] I. I. Piatetski-Shapiro, On the distribution of prime numbers in sequences of the form [f (n)], Mat. Sbornik
N.S., 33(75) (1953), pp. 559–566.
[33] J. Rivat and P. Sargos, Nombres premiers de la forme ⌊nc⌋, Canad. J. Math., 53 (2001), pp. 414–433.
[34] L. Spiegelhofer, Piatetski-Shapiro sequences via Beatty sequences, Acta Arith., 166 (2014), pp. 201–229.
[35] , Normality of the Thue–Morse sequence along Piatetski-Shapiro sequences, Q. J. Math., 66 (2015),
pp. 1127–1138.
[36] Y. Zhang, Bounded gaps between primes, Ann. of Math. (2), 179 (2014), pp. 1121–1174.

Institute of Discrete Mathematics and Geometry, Vienna University of Technology, Wiedner
Hauptstrasse 8–10, 1040 Vienna, Austria
