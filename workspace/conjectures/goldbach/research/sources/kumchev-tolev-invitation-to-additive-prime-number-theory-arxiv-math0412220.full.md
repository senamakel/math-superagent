<!-- source: https://arxiv.org/pdf/math/0412220 | converted from PDF -->

arXiv:math/0412220v1  [math.NT]  10 Dec 2004
An invitation to additive prime number theory

A. V. Kumchev and D. I. Tolev

November 26, 2024

Abstract

The main purpose of this survey is to introduce the inexperienced reader to additive
prime number theory and some related branches of analytic number theory. We state
the main problems in the ﬁeld, sketch their history and the basic machinery used to
study them, and try to give a representative sample of the directions of current research.
2000 MSC: 11D75, 11D85, 11L20, 11N05, 11N35, 11N36, 11P05, 11P32, 11P55.

1 Introduction

Additive number theory is the branch of number theory that studies the representations of
natural numbers as sums of integers subject to various arithmetic restrictions. For example,
given a sequence of integers
 A = {a1 < a2 < a3 < · · · }

one often asks what natural numbers can be represented as sums of a ﬁxed number of
elements of A; that is, for any ﬁxed s ∈ N, one wants to ﬁnd the natural numbers n such
that the diophantine equation
 x1 + · · · + xs = n(1.1)

has a solution in x1, . . . , xs ∈ A. The sequence A may be described in some generality (say,
one may assume that A contains “many” integers), or it may be a particular sequence of
some arithmetic interest (say, A may be the sequence of kth powers, the sequence of prime
numbers, the values taken by a polynomial F (X) ∈ Z[X] at the positive integers or at the
primes, etc.). In this survey, we discuss almost exclusively problems of the latter kind. The
main focus will be on two questions, known as Goldbach’s problem and the Waring–Goldbach
problem, which are concerned with representations as sums of primes and powers of primes,
respectively.

1.1 Goldbach’s problem

Goldbach’s problem appeared for the ﬁrst time in 1742 in the correspondence between Gold-
bach and Euler. In modern language, it can be stated as follows.

1

Goldbach’s Conjecture. Every even integer n ≥ 4 is the sum of two primes, and every
odd integer n ≥ 7 is the sum of three primes.

The two parts of this conjecture are known as the binary Goldbach problem and the
ternary Goldbach problem, respectively. Clearly, the binary conjecture is the stronger one.
It is also much more diﬃcult.
The ﬁrst theoretical evidence in support of Goldbach’s conjecture was obtained by Brun [27],
who showed that every large even integer is the sum of two integers having at most nine
prime factors. Brun also obtained an upper bound of the correct order for the number of
representations of a large even integer as the sum of two primes.
During the early 1920s Hardy and Littlewood [67]–[72] developed the ideas in an earlier
paper by Hardy and Ramanujan [73] into a new analytic method in additive number theory.
Their method is known as the circle method. In 1923 Hardy and Littlewood [69, 71] applied
the circle method to Goldbach’s problem. Assuming the Generalized Riemann Hypothesis
1

(GRH), they proved that all but ﬁnitely many odd integers are sums of three primes and
that all but O (x
1/2+ε) even integers n ≤ x are sums of two primes. (Henceforth, ε denotes
a positive number which can be chosen arbitrarily small if the implied constant is allowed
to depend on ε.)
During the 1930s Schnirelmann [201] developed a probabilistic approach towards prob-
lems in additive number theory. Using his method and Brun’s results, he was able to prove
unconditionally that there exists a positive integer s such that every suﬃciently large integer
is the sum of at most s primes. Although the value of s arising from this approach is much
larger than the conjectured s = 3, Schnirelmann’s result represented a signiﬁcant achieve-
ment, as it defeated the popular belief at the time that the solution of Goldbach’s problem
must depend on GRH. (Since its ﬁrst appearance, Schnirelmann’s method has been polished
signiﬁcantly. In particular, the best result to date obtained in this fashion by Ramare [193]
states that one can take s = 7.)
In 1937 I. M. Vinogradov [236] found an ingenious new method for estimating sums over
primes, which he applied to the exponential sum

f (α) = ∑

p≤n e(αp),(1.2)

where α is real, p denotes a prime, and e(α) = exp (2πiα). Using his estimate for f (α),
Vinogradov was able to give a new, unconditional proof of the result of Hardy and Littlewood
on the ternary Goldbach problem. His result is known as Vinogradov’s three prime theorem.

Theorem 1 (Vinogradov, 1937). For a positive integer n, let R(n) denote the number of
representations of n as the sum of three primes. Then

R(n) = n
2

2(log n)3 S(n) + O (
n
2(log n)−4) ,(1.3)

where
 S(n) = ∏

p|n
 (
1 − 1
(p − 1)2
 ) ∏

p∤n
 (
1 + 1
(p − 1)3
 ) .(1.4)

1An important conjecture about certain Dirichlet series; see §2.2 for details.

2

In particular, every suﬃciently large odd integer is the sum of three primes.

The products in (1.4) are over the primes dividing n and over those not dividing n,
respectively. In particular, when n is even, we have S(n) = 0, making (1.3) trivial. On the
other hand, when n is odd, we have S(n) ≥ 1. We describe the proof of Theorem 1 in §3.1.
It should be noted that the independence of GRH in Theorem 1 comes at the price of
a mind-boggling implied constant. If one avoids O-notation and makes all the constants
explicit, one ﬁnds that the original (GRH-dependent) work of Hardy and Littlewood estab-
lishes the ternary Goldbach conjecture for n ≥ 1050, whereas Vinogradov’s method requires
n ≥ 106 800 000 and even its most reﬁned version available today (see Liu and Wang [163])
requires n ≥ 101 346. To put these numbers in perspective, we remark that even the bound
1050 is beyond hope of “checking the remaining cases by a computer”. In fact, only recently
have Deshouillers et al. [51] proved that if GRH is true, the ternary Goldbach conjecture
holds for all odd n ≥ 7.
In 1938, using Vinogradov’s method, Chudakov [42], van der Corput [43], and Ester-
mann [54] each showed that almost all even integers n ≤ x are sums of two primes. More
precisely, they proved that for any A > 0 we have

E(x) = O (
x(log x)−A) ,(1.5)

where E(x) denotes the number of even integers n ≤ x that cannot be represented as the
sum of two primes. The ﬁrst improvement on (1.5) was obtained by Vaughan [220]. It was
followed by a celebrated work by Montgomery and Vaughan [173] from 1975, in which they
established the existence of an absolute constant δ > 0 such that

E(x) = O (x
1−δ) .(1.6)

The ﬁrst to compute an explicit numerical value for δ were Chen and Pan [36]. They showed
that the method of Montgomery and Vaughan yields (1.6) with δ = 0.01. Subsequently,
this result has been sharpened by several authors and currently (1.6) is known to hold with
δ = 0.086 (see Li [136]). In June 2004, Pintz [186] announced a further improvement on
(1.6). He has established the above bound with δ = 1
3 and can also show that for all but
O(x
3/5+ε) even integers n ≤ x either n or n − 2 is the sum of two primes.
One may also think of the binary Goldbach conjecture as a claim about the primes in
the sequence
 A = A(n) = {n − p : p prime number, 2 < p < n} ,(1.7)

namely, that such primes exist for all even n ≥ 6. Denote by Pr an integer having at most
r prime factors, counted with their multiplicities, and refer to such a number as an almost
prime of order r (thus, Brun’s result mentioned above asserts that every large even n can be
represented in the form n = P9 + P ′
9). In 1947 R´enyi [195] proved that there is a ﬁxed integer
r such that the sequence A contains a Pr-number when n is suﬃciently large. Subsequent
work by many mathematicians reduced the value of r in R´enyi’s result almost to the possible
limit and fell just short of proving the binary Goldbach conjecture. The best result to date
was obtained by Chen [35].
 3

Theorem 2 (Chen, 1973). For an even integer n, let r(n) denote the number of represen-
tations of n in the form n = p + P2, where p is a prime and P2 is an almost prime of order
2. There exists an absolute constant n0 such that if n ≥ n0, then

r(n) > 0.67 ∏

p>2
 (
1 − 1
(p − 1)2
 ) ∏

p>2
p|n
 ( p − 1
p − 2
 ) n
(log n)2 .

In particular, every suﬃciently large even integer n can be represented in the form n = p+P2.

1.2 Waring’s problem

Before proceeding with the Waring–Goldbach problem, we will make a detour to present the
most important results in Waring’s problem, as those results and the work on Goldbach’s
problem have been the main motivation behind the Waring–Golbach problem. It was prob-
ably the ancient Greeks who ﬁrst observed that every positive integer is the sum of four
integer squares, but it was not until 1770 that a complete proof of this remarkable fact was
given by Lagrange. Also in 1770, Waring proposed a generalization of the four square theo-
rem that became known as Waring’s problem and arguably led to the emergence of additive
number theory. In modern terminology, Waring’s conjecture states that for every integer
k ≥ 2 there exists an integer s = s(k) such that every natural number n is the sum of at
most s kth powers of natural numbers. Several special cases of this conjecture were settled
during the 19th century, but the complete solution eluded mathematicians until 1909, when
Hilbert [95] proved the existence of such an s for all k by means of a diﬃcult combinatorial
argument.
Let g(k) denote the least possible s as above. Hilbert’s method produced a very poor
bound for g(k). Using the circle method, Hardy and Littlewood were able to improve greatly
on Hilbert’s bound for g(k). In fact, through the eﬀorts of many mathematicians, the circle
method in conjunction with elementary and computational arguments has led to a nearly
complete evaluation of g(k). In particular, we know that g(k) is determined by certain special
integers n < 4k that can only be represented as sums of a large number of kth powers of 1,
2 and 3 (see [228, §1.1] for further details on g(k)).
A much more diﬃcult question, and one that leads to a much deeper understanding of
the additive properties of kth powers, is that of estimating the function G(k), deﬁned as the
least s such that every suﬃciently large positive integer n is the sum of s kth powers. This
function was introduced by Hardy and Littlewood [70], who obtained the bound

G(k) ≤ (k − 2)2k−1 + 5.(1.8)

In fact, they proved more than that. Let Ik,s(n) denote the number of solutions of the
diophantine equation
 x
k
1 + x
k
2 + · · · + x
k
s = n(1.9)

in x1, . . . , xs ∈ N. Hardy and Littlewood showed that if s ≥ (k − 2)2k−1 + 5, then

Ik,s(n) ∼ Γs (1 + 1
k )

Γ ( s
k ) Sk,s(n)n
s/k−1 as n → ∞,(1.10)
 4

where Γ stands for Euler’s gamma-function and Sk,s(n) is an absolutely convergent inﬁnite
series, called the singular series, such that

Sk,s(n) ≥ c1(k, s) > 0.

While the upper bound (1.8) represents a tremendous improvement over Hilbert’s result,
it is still quite larger than the trivial lower bound G(k) ≥ k + 1.
2 During the mid-1930s
I. M. Vinogradov introduced several reﬁnements of the circle method that allowed him to
obtain a series of improvements on (1.8) for large k. In their most elaborate version, Vino-
gradov’s methods yield a bound of the form
3

G(k) ≤ 2k(log k + O(log log k)).

First published by Vinogradov [240] in 1959, this bound withstood any signiﬁcant improve-
ment until 1992, when Wooley [245] proved that

G(k) ≤ k(log k + log log k + O(1)).

The latter is the sharpest bound to date for G(k) when k is large. For smaller k, one can
obtain better results by using more specialized techniques (usually reﬁnements of the circle
method). The best known bounds for G(k), 3 ≤ k ≤ 20, are of the form G(k) ≤ F (k), with
F (k) given by Table 1 below.

k 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

F (k) 7 16 17 24 33 42 50 59 67 76 84 92 100 109 117 125 134 142

Table 1. Bounds for G(k), 3 ≤ k ≤ 20.

With the exception of the bound G(3) ≤ 7, all of these results have been obtained by an
iterative version of the circle method that originated in the work of Davenport [46, 48]
and Davenport and Erd¨os [50]. The bound for G(3) was established ﬁrst by Linnik [141]
and until recently lay beyond the reach of the circle method. The result on G(4) is due to
Davenport [47], and in fact states that G(4) = 16. This is because 16 biquadrates are needed
to represent integers of the form n = 31 · 16r, r ∈ N. Other than Lagrange’s four squares
theorem, this is the only instance in which the exact value of G(k) is known. However,
Davenport [47] also proved that if s ≥ 14, all suﬃciently large integers n ≡ r (mod 16),
1 ≤ r ≤ s, can be written as the sum of s biquadrates; Kawada and Wooley [120] obtained
a similar result for as few as 11 biquadrates. The remaining bounds in Table 1 appear in a
series of recent papers by Vaughan and Wooley [229]–[232].

2 Let X be large. If n ≤ X, any solution of (1.9) must satisfy 1 ≤ x1, . . . , xs ≤ X 1/k. There at most
X s/k such s-tuples, which yield at most (1/s! + o(1))X s/k distinct sums x
k
1 + · · · + x
k
s . Thus, when s ≤ k,
there are not enough sums of s kth powers to represent all the integers.
3 In this and similar results appearing later, one can obtain an explicit expressions in place of the O-terms,
but those are too complicated to state here.
 5

A great deal of eﬀort has also been dedicated to estimating the function ˜G(k), which
represents the least s for which the asymptotic formula (1.10) holds. For large k, Ford [57]
showed that
 ˜G(k) ≤ k2(log k + log log k + O(1)),(1.11)

thus improving on earlier work by Vinogradov [238], Hua [101], and Wooley [246]. Further-
more, Vaughan [226, 227] and Boklan [18] obtained the bounds

˜G(k) ≤ 2k (k ≥ 3) and ˜G(k) ≤ 7
8 · 2k (k ≥ 6),

which supersede (1.11) when k ≤ 8.

The work on Waring’s problem has inspired research on several other questions concerned
with the additive properties of kth powers (and of more general polynomial sequences). Such
matters, however, are beyond the scope of this survey. The reader interested in a more
comprehensive introduction to Waring’s problem should refer to the monographs [4, 228] or
to a recent survey article by Vaughan and Wooley [233] (the latter also provides an excellent
account of the history of Waring’s problem).

1.3 The Waring–Goldbach problem

Vinogradov’s proof of the three prime theorem provided a blueprint for subsequent applica-
tions of the Hardy–Littlewood circle method to additive problems involving primes. Shortly
after the publication of Theorem 1, Vinogradov himself [237] and Hua [100] began studying
Waring’s problem with prime variables, known nowadays as the Waring–Goldbach problem.
They were able to generalize the asymptotic formula (1.3) to kth powers for all k ≥ 1 and
ultimately their eﬀorts led to the proof of Theorem 3 below.
In order to describe the current knowledge about the Waring–Goldbach problem, we ﬁrst
need to introduce some notation. Let k be a positive integer and p a prime. We denote by
θ = θ(k, p) the (unique) integer such that pθ | k and pθ+1 ∤ k, and then deﬁne

γ = γ(k, p) =
 {
θ + 2, if p = 2, 2 | k,
θ + 1, otherwise, K(k) = ∏

(p−1)|k pγ.(1.12)

In particular, we have K(1) = 2. It is not diﬃcult to show that if an integer n is the sum
of s kth powers of primes greater than k + 1, then n must satisfy the congruence condition
n ≡ s (mod K(k)). Furthermore, deﬁne

S(q, a) =
 q∑

h=1
(h,q)=1
 e (ah
k

q
 ) , S∗
k,s(n) =
 ∞∑

q=1
 q∑

a=1
(a,q)=1
 S(q, a)s

φ(q)s e (−an
q
 ) ,(1.13)

where (a, q) stands for the greatest common divisor of a and q, and φ(q) is Euler’s totient
function, that is, the number of positive integers n ≤ q which are relatively prime to q. The
following result will be established in §3.3 and §3.4.

6

Theorem 3. Let k, s and n be positive integers, and let R∗
k,s(n) denote the number of solu-
tions of the diophantine equation
 pk
1 + pk
2 + · · · + pk
s = n(1.14)

in primes p1, . . . , ps. Suppose that

s ≥
 



2k + 1, if 1 ≤ k ≤ 5,

7
8 · 2k + 1, if 6 ≤ k ≤ 8,
k2(log k + log log k + O(1)), if k > 8.

Then
 R∗
k,s(n) ∼ Γs (1 + 1
k )

Γ ( s
k ) S∗
k,s(n) n
s/k−1

(log n)s as n → ∞,(1.15)

where S∗
k,s(n) is deﬁned by (1.13). Furthermore, the singular series S∗
k,s(n) is absolutely
convergent, and if n ≡ s (mod K(k)), then S∗
k,s(n) ≥ c2(k, s) > 0.

In particular, we have the following corollaries to Theorem 3.

Corollary 3.1. Every suﬃciently large integer n ≡ 5 (mod 24) can be represented as the
sum of ﬁve squares of primes.

Corollary 3.2. Every suﬃciently large odd integer can be represented as the sum of nine
cubes of primes.

Hua introduced a function H(k) similar to the function G(k) in Waring’s problem. H(k)
is deﬁned as the least integer s such that equation (1.14) has a solution in primes p1, . . . , ps
for all suﬃciently large n ≡ s (mod K(k)). It is conjectured that H(k) = k + 1 for all k ≥ 1,
but this conjecture has not been proved for any value of k yet. When k ≤ 3, the sharpest
known upper bounds for H(k) are those given by Theorem 3, that is,

H(1) ≤ 3, H(2) ≤ 5, H(3) ≤ 9.

When k ≥ 4, the best results in the literature are as follows.

Theorem 4. Let k ≥ 4 be an integer, and let H(k) be as above. Then

H(k) ≤
 {F (k), if 4 ≤ k ≤ 10,
k(4 log k + 2 log log k + O(1)), if k > 10,

where F (k) is given by the following table.

k 4 5 6 7 8 9 10

F (k) 14 21 33 46 63 83 107

Table 2. Bounds for H(k), 4 ≤ k ≤ 10.

7

The cases k = 6 and 8 ≤ k ≤ 10 of Theorem 4 are due to Thanigasalam [211], and the
cases k = 4, 5 and 7 are recent results of Kawada and Wooley [121] and Kumchev [127],
respectively. The bound for k > 10 is an old result of Hua, whose proof can be found in
Hua’s book [102]. To the best of our knowledge, this is the strongest published result for
large k, although it is well-known to experts in the ﬁeld that better results are within the
reach of Wooley’s reﬁnement of Vinogradov’s methods. In particular, by inserting Theorem
1 in Wooley [247] into the machinery developed in Hua’s monograph, one obtains

H(k) ≤ k( 3
2 log k + O(log log k)) for k → ∞.

1.4 Other additive problems involving primes

There are several variants and generalizations of the Waring–Goldbach problem that have
attracted a lot of attention over the years. For example, one may consider the diophantine
equation
 a1pk
1 + a2pk
2 + · · · + aspk
s = n,(1.16)

where n, a1, . . . , as are ﬁxed, not necessarily positive, integers. There are several questions
that we can ask about equations of this form. The main question, of course, is that of
solubility. Furthermore, in cases where we do know that (1.16) is soluble, we may want to
count the solutions with p1, . . . , ps ≤ X, where X is a large parameter. A famous problem of
this type is the twin-prime conjecture: there exist inﬁnitely many primes p such that p + 2
is also prime, that is, the equation
 p1 − p2 = 2

has inﬁnitely many solutions. It is believed that this conjecture is of the same diﬃculty as
the binary Goldbach problem, and in fact, the two problems share a lot of common history.
In particular, while the twin-prime conjecture is still open, Chen’s proof of Theorem 2 can
be easily modiﬁed to establish that there exist inﬁnitely many primes p such that p + 2 = P2.
Other variants of the Waring–Goldbach problem consider more general diophantine equa-
tions of the form
 f (p1) + f (p2) + · · · + f (ps) = n,

where f (X) ∈ Z[X], or systems of equations of the types (1.1) or (1.16). For example,
Chapters 10 and 11 in Hua’s monograph [102] deal with the system

pj
1 + pj
2 + · · · + pj
s = nj (1 ≤ j ≤ k).

The number of solutions of this system satisﬁes an asymptotic formula similar to (1.15), but
the main term in that asymptotic formula is less understood than the main term in (1.15)
(see [3, 41, 102, 170] for further details).
Another classical problem in which a system of diophantine equations arises naturally
concerns the existence of non-trivial arithmetic progressions consisting of r primes. It has

8

been conjectured that for every integer r ≥ 3 there are inﬁnitely many such arithmetic
progressions. In other words, the linear system

pi − 2pi+1 + pi+2 = 0 (1 ≤ i ≤ r − 2)

has inﬁnitely many solutions in distinct primes p1, . . . , pr. In the case r = 3 this can be
established by a variant of Vinogardov’s proof of the three primes theorem, but when r > 3
the above system lies beyond the reach of the circle method. In fact, until recently the most
signiﬁcant insight into progressions of more than three primes were the following two results:

• Heath-Brown [83] succeeded to prove that there exist inﬁnitely many arithmetic pro-
gressions of three primes and a P2-number.

• Balog [11] proved that for any r there are r distinct primes p1, . . . , pr such that all the
averages 1
2(pi + pj) are prime.

Thus, the specialists in the ﬁeld were stunned when Green and Tao [64] announced their
amazing proof of the full conjecture. The reader will ﬁnd a brief description of their ideas
and of some related recent work in the last section.
Finally, instead of (1.1), one may study the inequality

|x1 + · · · + xs − α| < ε,

where α is a real number, ε is a small positive number and x1, . . . , xs are real variables taking
values from a given sequence (or sequences). For example, by setting xj = pc
j where c > 1
in not an integer, we can generalize the Waring–Goldbach problem to fractional powers of
primes. We will mention several results of this form in §5.7.

2 The distribution of primes

In this section we discuss brieﬂy some classical results about primes, which play an important
role in additive prime number theory.

2.1 The Prime Number Theorem

The ﬁrst result on the distribution of primes is Euclid’s theorem that there are inﬁnitely
many prime numbers. In 1798 Legendre conjectured that the prime counting function π(x)
(i.e., the number of primes p ≤ x) satisﬁes the asymptotic relation

lim
x→∞ π(x)
x/(log x) = 1;(2.1)

this is the classical statement of the Prime Number Theorem. Later Gauss observed that
the logarithmic integral
 li x = ∫ x

2
 dt
log t

9

seemed to provide a better approximation to π(x) than the function x/(log x) appearing in
(2.1), and this is indeed the case. Thus, in anticipation of versions of the Prime Number
Theorem that are more precise than (2.1), we deﬁne the error term

∆(x) = π(x) − li x.(2.2)

The ﬁrst step toward a proof of the Prime Number Theorem was made by Chebyshev.
In the early 1850s he proved that (2.1) predicts correctly the order of π(x), that is, he
established the existence of absolute constants c2 > c1 > 0 such that

c1x
log x ≤ π(x) ≤ c2x
log x.

Chebyshev also showed that if the limit on the left side of (2.1) exists, then it must be equal
to 1.
In 1859 Riemann published his famous memoir [197], in which he demonstrated the
intimate relation between π(x) and the function which now bears his name, that is, the
Riemann zeta-function deﬁned by

ζ(s) =
 ∞∑

n=1 n
−s = ∏

p
 (1 − p−s)−1 (Re(s) > 1).(2.3)

This and similar series had been used earlier by Euler
4 and Dirichlet, but only as functions of
a real variable. Riemann observed that ζ(s) is holomorphic in the half-plane Re(s) > 1 and
that it can be continued analytically to a meromorphic function, whose only singularity is a
simple pole at s = 1. It is not diﬃcult to deduce from (2.3) that ζ(s) ̸= 0 in the half-plane
Re(s) > 1. Riemann observed that ζ(s) has inﬁnitely many zeros in the strip 0 ≤ Re(s) ≤ 1
and proposed several conjectures concerning those zeros and the relation between them and
the Prime Number Theorem. The most famous among those conjecture—and the only one
that is still open—is known as the Riemann Hypothesis.

Riemann Hypothesis (RH). All the zeros of ζ(s) with 0 ≤ Re(s) ≤ 1 lie on the line
Re(s) = 1
2.

The remaining conjectures in Riemann’s paper were proved by the end of the 19th century.
In particular, it was proved that the Prime Number Theorem follows from the nonvanishing
of ζ(s) on the line Re(s) = 1. Thus, when in 1896 Hadamard and de la Vall´ee Poussin
proved (independently) that ζ(1 + it) ̸= 0 for all real t, the Prime Number Theorem was
ﬁnally proved. In 1899 de la Vall´ee Poussin obtained the following quantitative result.
5

(Henceforth, we often use Vinogradov’s notation A ≪ B, which means that A = O(B).)

4 In particular, Euler established the equality between ζ(s) and the inﬁnite product in (2.3), which is
known as the Euler product of ζ(s).
5 Functions of the type f (x) = exp (
(log x)
λ)
, where λ is a constant, are quite common in analytic number
theory. To help the reader appreciate results such as Theorems 5 and 6, we remark that as x → ∞ such a
function with 0 < λ < 1 grows more rapidly than any ﬁxed power of log x, but less rapidly than x
ε for any
ﬁxed ε > 0.
 10

Theorem 5 (de la Vall´ee Poussin, 1899). Let ∆(x) be deﬁned by (2.2). There exists an
absolute constant c > 0 such that

∆(x) ≪ x exp ( − c√log x)
.

De la Vall´ee Poussin’s theorem has been improved somewhat, but not nearly as much as
one would hope. The best result to date is due to I. M. Vinogradov [239] and Korobov [123],
who obtained (independently) the following estimate for ∆(x).

Theorem 6 (Vinogradov, Korobov, 1958). Let ∆(x) be deﬁned by (2.2). There exists
an absolute constant c > 0 such that

∆(x) ≪ x exp ( − c(log x)3/5(log log x)−1/5)
.

In comparison, if the Riemann Hypothesis is assumed, one has

∆(x) ≪ x
1/2 log x,(2.4)

which, apart from the power of the logarithm, is best possible. The reader can ﬁnd fur-
ther information about the Prime Number Theorem and the Riemann zeta-function in the
standard texts on the subject (e.g., [49, 103, 117, 191, 212]).

2.2 Primes in arithmetic progressions

In a couple of memoirs published in 1837 and 1840, Dirichlet proved that if a and q are
natural numbers with (a, q) = 1, then the arithmetic progression a mod q contains inﬁnitely
many primes. In fact, Dirichlet’s argument can be reﬁned as to establish the asymptotic
formula
 ∑

p≤x
p≡a (mod q)
 log p
p ∼ 1
φ(q)
 ∑

p≤x
 log p
p as x → ∞,(2.5)

valid for all a and q with (a, q) = 1. Fix q and consider the various arithmetic progressions
a mod q (here φ(q) is Euler’s totient function). Since all but ﬁnitely many primes lie
in progressions with (a, q) = 1 and there are φ(q) such progressions, (2.5) suggests that
each arithmetic progression a mod q, with (a, q) = 1, “captures its fair share” of prime
numbers, i.e., that the primes are uniformly distributed among the (appropriate) arithmetic
progressions to a given modulus q. Thus, one may expect that if (a, q) = 1, then

π(x; q, a) = ∑

p≤x
p≡a (mod q)
 1 ∼ li x
φ(q) as x → ∞.(2.6)

This is the prime number theorem for arithmetic progressions. One may consider (2.6) from
two diﬀerent view points. First, one may ﬁx a and q and ask whether (2.6) holds (allowing the
convergence to depend on q and a). Posed in this form, the problem is a minor generalization

11

of the Prime Number Theorem. In fact, shortly after proving Theorem 5, de la Vall´ee Poussin
established that
 ∆(x; q, a) = π(x; q, a) − li x
φ(q) ≪ x exp ( − c√log x
),

where c = c(q, a) > 0 and the implied constant depends on q and a. The problem becomes
much more diﬃcult if one requires an estimate that is explicit in q and uniform in a. The
ﬁrst result of this kind was obtained by Page [176], who proved the existence of a (small)
positive number δ such that
 ∆(x; q, a) ≪ x exp (−(log x)δ) ,(2.7)

whenever 1 ≤ q ≤ (log x)2−δ and (a, q) = 1. In 1935 Siegel [208] (essentially) proved the
following result known as the Siegel–Walﬁsz theorem.

Theorem 7 (Siegel, 1935). For any ﬁxed A > 0, there exists a constant c = c(A) > 0
such that
 π(x; q, a) = li x
φ(q) + O(
x exp ( − c√log x))

whenever q ≤ (log x)A and (a, q) = 1.

Remark. While this result is clearly sharper than Page’s, it does have one signiﬁcant draw-
back: it is ineﬀective, that is, given a particular value of A, the proof does not allow the
constant c(A) or the O-implied constant to be computed.

The above results have been proved using the analytic properties of a class of generaliza-
tions of the Riemann zeta-function known as Dirichlet L-functions. For each positive integer
q there are φ(q) functions χ : Z → C, called Dirichlet characters mod q, with the following
properties:

• χ is totally multiplicative: χ(mn) = χ(m)χ(n);

• χ is q-periodic;

• |χ(n)| = 1 if (n, q) = 1 and χ(n) = 0 if (n, q) > 1;

• if (n, q) = 1, then
 ∑

χ mod q χ(n) =
 {
φ(q) if n ≡ 1 (mod q),
0 otherwise.

For more information about the construction and properties of the Dirichlet characters we
refer the reader to [49, 108, 116, 191].
Given a character χ mod q, we deﬁne the Dirichlet L-function

L(s, χ) =
 ∞∑

n=1 χ(n)n
−s = ∏

p
 (1 − χ(p)p−s)−1 (Re(s) > 1).

12

Similarly to ζ(s), L(s, χ) is holomorphic in the half-plane Re(s) > 1 and can be continued
analytically to a meromorphic function on C that has at most one pole, which (if present)
must be a simple pole at s = 1. Furthermore, just as ζ(s), the continued L(s, χ) has inﬁnitely
many zeros in the strip 0 ≤ Re(s) ≤ 1, and the horizontal distribution of those zeros has
important implications on the distribution of primes in arithmetic progressions. For example,
the results of de la Vall´ee Poussin, Page and Siegel mentioned above were proved by showing
that no L-function can have a zero “close” to the line Re(s) = 1. We also have the following
generalization of the Riemann Hypothesis.

Generalized Riemann Hypothesis (GRH). Let L(s, χ) be a Dirichlet L-function. Then
all the zeros of L(s, χ) with 0 ≤ Re(s) ≤ 1 lie on the line Re(s) = 1
2.

Assuming GRH, we can deduce easily that if (a, q) = 1, then

π(x; q, a) = li x
φ(q) + O (
x
1/2 log x
) ,(2.8)

which is nontrivial when 1 ≤ q ≤ x
1/2(log x)−2−ε.
In many applications one only needs (2.8) to hold “on average” over the moduli q. Dur-
ing the 1950s and 1960s several authors obtained estimates for averages of ∆(x; q, a). In
particular, the following quantity was studied extensively:

E(x, Q) = ∑

q≤Q max
(a,q)=1 max
y≤x |∆(y; q, a)|.

The trivial bound for this quantity is E(x, Q) ≪ x log x. One usually focuses on ﬁnding the
largest value of Q for which one can improve on this trivial bound, even if the improvement
is fairly modest. The sharpest result in this direction was established (independently) by
Bombieri [19] and A. I. Vinogradov [234] in 1965. Their result is known as the Bombieri–
Vinogradov theorem and (in the slightly stronger form given by Bombieri) can be stated as
follows.

Theorem 8 (Bombieri, Vinogradov, 1965). For any ﬁxed A > 0, there exists a B =
B(A) > 0 such that
 E(x, Q) ≪ x(log x)−A,(2.9)

provided that Q ≤ x
1/2(log x)−B.

We should note that other than the value of B(A) the range for Q in this result is as long
as the range we can deduce from GRH. Indeed, GRH yields B = A + 1, whereas Bombieri
obtained Theorem 8 with B = 3A + 22 and more recently Vaughan [223] gave B = A + 5/2.

2.3 Primes in short intervals

Throughout this section, we write pn for the nth prime number. We are interested in
estimates for the diﬀerence pn+1 − pn between two consecutive primes. Cram´er was the

13

ﬁrst to study this question systematically. He proved [44] that the Riemann Hypothesis
implies
 pn+1 − pn ≪ p1/2
n log pn.

Cram´er also proposed a probabilistic model of the prime numbers that leads to very precise
(and very bold) predictions of the asymptotic properties of the primes. In particular, he
conjectured [45] that
 lim sup
n→∞ pn+1 − pn
log2 pn = 1.(2.10)

A non-trivial upper bound for pn+1 − pn can be obtained as a consequence of the Prime
Number Theorem, but Hoheisel [96] found a much sharper result. He proved unconditionaly
the asymptotic formula

π(x + h) − π(x) ∼ h(log x)−1 as x → ∞,(2.11)

with h = x
1−(3300)−1 . There have been several improvements on Hoheisel’s result and it is
now known that (2.11) holds with h = x
7/12 (see Heath-Brown [86]). Furthermore, several
mathematicians have shown that even shorter intervals must contain primes (without estab-
lishing an asymptotic formula for the number of primes in such intervals). The best result in
this directions is due to Baker, Harman, and Pintz [9], who proved that for each n one has

pn+1 − pn ≪ p0.525
n .

A related problem seeks small gaps between consecutive primes. In particular, the twin-
prime conjecture can be stated in the form

lim inf
n→∞ (pn+1 − pn) = 2.

It is an exercise to show that the Prime Number Theorem implies the inequality

lim inf
n→∞ pn+1 − pn
log pn ≤ 1.

Improvements on this trivial bound, on the other hand, have proved notoriously diﬃcult
and, so far, the best result, due to Maier [165], is

lim inf
n→∞ pn+1 − pn
log pn ≤ 0.2486 . . . .

2.4 Primes in sparse sequences

We say that an inﬁnite sequence of primes S is sparse if

π(S; x) := #
{p ∈ S : p ≤ x
} = o(π(x)) as x → ∞.

14

A classical example that has attracted a great deal of attention but has proved notoriously
diﬃcult is that of primes represented by polynomials. To this day, there is not a single
example of a polynomial f (X) ∈ Z[X] of degree at least 2 which is known to take on inﬁnitely
many prime values. The closest approximation is a result of Iwaniec [104], who showed that
if a, b, c are integers such that a > 0, (c, 2) = 1, and the polynomial f (X) = aX 2 + bX + c is
irreducible, then f (X) takes on inﬁnitely many P2-numbers. On the other hand, in recent
years there has been some exciting progress in the direction of ﬁnding polynomials in two
variables that represent inﬁnitely many primes. In 1998 Friedlander and Iwaniec [58] proved
that the polynomial X 2+Y 4 represents inﬁnitely many primes. We note that this polynomial
takes on O(x
3/4) values up to x. In 2001 Heath-Brown [89] obtained an analogous result for
the polynomial X 3 + 2Y 3 whose values are even sparser: it takes on O(x
2/3) values up to x.
Furthermore, Heath-Brown and Moroz [92] extended the latter result to general irreducible
binary cubic forms in Z[X, Y ] (subject to some mild necessary conditions).
Another class of sparse sequences of prime numbers arises in the context of diophantine
approximation. The two best known examples of this kind are the sequences

Sλ = {
p : p is prime with {√p} < p−λ}
(2.12)

and
 Pc = {p : p = [n
c] for some integer n} .(2.13)

Here, λ ∈ (0, 1) and c > 1 are ﬁxed real numbers, {x} denotes the fractional part of the real
number x, and [x] = x − {x}. The sequence Sλ was introduced by I. M. Vinogradov, who
proved (see [241, Chapter 4]) that if 0 < λ < 1/10, then

π(Sλ; x) ∼ x
1−λ

(1 − λ) log x as x → ∞.

The admissible range for λ has been subsequently extended to 0 < λ < 1/4 by Balog [10]
and Harman [76], while Harman and Lewis [81] showed that Sλ is inﬁnite for 0 < λ < 0.262.
The ﬁrst to study the sequence (2.13) was Piatetski-Shapiro [185], who considered Pc as
a sequence of primes represented by a “polynomial of degree c”. Piatetski-Shapiro proved
that Pc is inﬁnite when 1 < c < 12/11. The range for c has been extended several times and
it is currently known (see Rivat and Wu [199]) that Pc is inﬁnite when 1 < c < 243/205.
Furthermore, it is known (see Rivat and Sargos [198]) that when 1 < c < 1.16117 . . . , we
have
 π(Pc; x) ∼ x
1/c

log x as x → ∞.

3 The Hardy–Littlewood circle method

Most of the results mentioned in the Introduction have been proved by means of the Hardy–
Littlewood circle method. In this section, we describe the general philosophy of the circle
method, using its applications to the Goldbach and Waring–Goldbach problems to illustrate
the main points.
 15

3.1 Vinogradov’s three prime theorem

3.1.1 Preliminaries

Using the orthogonality relation

∫ 1

0 e(αm) dα =
 {
1, if m = 0,
0, if m ̸= 0,
(3.1)

we can express R(n) as a Fourier integral. We have

R(n) = ∑

p1,p2,p3≤n
 ∫ 1

0 e (α (p1 + p2 + p3 − n)) dα(3.2)
 = ∫ 1

0 f (α)3e(−αn) dα,

where f (α) is the exponential sum (1.2).
The circle method uses (3.2) to derive an asymptotic formula for R(n) from estimates for
f (α). The analysis of the right side of (3.2) rests on the observation that the behavior of f (α)
depends on the distance from α to the set of fractions with “small” denominators. When
α is “near” such a fraction, we expect f (α) to be “large” and to have certain asymptotic
behavior. Otherwise, we can argue that the numbers e(αp) are uniformly distributed on the
unit circle and hence f (α) is “small”. In order to make these observations rigorous, we need
to introduce some notation. Let B be a positive constant to be chosen later and set

P = (log n)B.(3.3)

If a and q are integers with 1 ≤ a ≤ q ≤ P and (a, q) = 1, we deﬁne the major arc6

M(q, a) = [a
q − P
qn , a
q + P
qn
] .(3.4)

The integration in (3.2) can be taken over any interval of length one and, in particular, over[P n
−1, 1 + P n
−1]. We partition this interval into two subsets:

M = ⋃

q≤P
 ⋃

1≤a≤q
(a,q)=1
 M(q, a) and m = [P n
−1, 1 + P n
−1] \ M,(3.5)

called respectively the set of major arcs and the set of minor arcs. Then from (3.2) and
(3.5) it follows that
 R(n) = R(n, M) + R(n, m),(3.6)

6This term may seem a little peculiar at ﬁrst, given that M(q, a) is in fact an interval. The explanation
is that, in the original version of the circle method, Hardy and Littlewood used power series and Cauchy’s
integral formula instead of exponential sums and (3.1) (see [228, §1.2]). In that setting, the role of M(q, a)
is played by a small circular arc near the root of unity e(a/q).

16

where we have denoted
 R(n, B) = ∫

B f (α)3e(−αn) dα.

In the next section we explain how, using Theorem 7 and standard results from elementary
number theory, one can obtain an asymptotic formula for R(n, M) (see (3.13) below). Then
in §3.1.3 and §3.1.4 we discuss how one can show that R(n, m) is of a smaller order of
magnitude than the main term in that asymptotic formula (see (3.14)).

3.1.2 The major arcs

In this section we sketch the estimation of the contribution from the major arcs. The
interested reader will ﬁnd the missing details in [116, Chapter 10] or [228, Chapter 2].
It is easy to see that the major arcs M(q, a) are mutually disjoint. Thus, using (3.4) and
(3.5), we can write

R(n, M) = ∑

q≤P
 ∑

1≤a≤q
(a,q)=1
 ∫ P/(qn)

−P/(qn) f (a/q + β)3e
( − (a/q + β)n
) dβ.(3.7)

We now proceed to approximate f (
a/q + β) by a simpler expression. To motivate our
choice of the approximation, we ﬁrst consider the case β = 0. We split the sum f (
a/q) into
subsums according to the residue of p modulo q and take into account the deﬁnition (2.6).
We get
 f (a
q
 ) =
 q∑

h=1
 ∑

p≤n
p≡h (mod q)
 e (ap
q
 ) =
 q∑

h=1 e (ah
q
 ) π(n; q, h).

The contribution of the terms with (h, q) > 1 is negligible (at most q). If (h, q) = 1, our
choice (3.3) of the parameter P ensures that we can appeal to Theorem 7 to approximate
π(n; q, h) by φ(q)−1 li n. We deduce that

f ( a
q
 ) = li n
φ(q)
 q∑

h=1
(h,q)=1
 e (ah
q
 ) + O (qnP −4) .(3.8)

The exponential sum on the right side of (3.8) is known as the Ramanujan sum and is usually
denoted by cq(a). Its value is known for every pair of integers a and q (see [74, Theorem
271]). In particular, when (a, q) = 1 we have cq(a) = µ(q), where µ is the M¨obius function

µ(n) =
 



1, if n = 1,
(−1)k, if n = p1 · · · pk is the product of k distinct primes,
0, otherwise.
(3.9)
 17

The situation does not change much if instead of α = a/q we consider α = a/q +β ∈ M(q, a).
In this case we ﬁnd that
 f ( a
q + β) = µ(q)
φ(q) · v(β) + O (nP −3) ,(3.10)

where
 v(β) = ∫ n

2
 e(βu)
log u du.

Raising (3.10) to the third power and inserting the result into the right side of (3.7), we
obtain
 R(n, M) = ∑

q≤P
 µ(q)cq(−n)
φ(q)3
 ∫ P/(qn)

−P/(qn) v(β)3e(−βn) dβ + O (n
2P −1) .(3.11)

At this point, we extend the integration over β to the whole real line, and then the summation
over q to all positive integers. The arising error terms can be controlled easily by means of
well-known bounds for the functions v(β) and φ(q), and we ﬁnd that

R(n, M) = S(n)J(n) + O (n
2P −1) ,(3.12)

where S(n) and J(n) are the singular series and the singular integral deﬁned by

S(n) =
 ∞∑

q=1
 µ(q)cq(−n)
φ(q)3 , J(n) = ∫ ∞

−∞ v(β)3e(−βn) dβ.

The series S(n) actually satisﬁes (1.4). Indeed, the function

g(q) = µ(q)cq(−n)φ(q)−3

is multiplicative in q, that is, g(q1q2) = g(q1)g(q2) whenever (q1, q2) = 1. Hence, using
the absolute convergence of S(n) and the elementary properties of the arithmetic functions
involved in the deﬁnition of g(q), we can represent the singular series as an Euler product:

S(n) =
 ∞∑

q=1 g(q) = ∏

p
 (1 + g(p) + g(p2) + · · · )

= ∏

p|n
 (
1 − 1
(p − 1)2
 ) ∏

p∤n
 (1 + 1
(p − 1)3
 ) .

Also, an application of Fourier’s inversion formula and some calculus reveal that

J(n) = n
2

2(log n)3 + O (
n
2(log n)−4) .

Therefore, if B ≥ 4 we can conclude that

R(n, M) = n
2

2(log n)3 S(n) + O (n
2(log n)−4) .(3.13)
 18

3.1.3 The minor arcs

In view of (3.6) and (3.13), it suﬃces to prove that (for some B ≥ 4)

R(n, m) ≪ n
2(log n)−4.(3.14)

We have
 |R(n, m)| ≤ ∫
m |f (α)|3 dα ≤ ( sup
m |f (α)|) ∫ 1

0 |f (α)|2 dα.(3.15)

By Parseval’s identity and the Prime Number Theorem,
∫ 1

0 |f (α)|2 dα = ∑

p≤n 1 ≪ n(log n)−1.(3.16)

Thus, (3.14) will follow from (3.15), if we show that

sup
m |f (α)| ≪ n(log n)−3.(3.17)

We note that the trivial estimate for f (α) is

f (α) ≪ ∑

p≤n 1 ≪ n(log n)−1,

so in order to establish (3.17), we have to save a power of log n over this trivial estimate
(uniformly with respect to α ∈ m). We can do this using the following lemma, which provides
such a saving under the assumption that α can be approximated by a reduced fraction whose
denominator q is “neither too small, nor too large.”

Lemma 3.1. Let α be real and let a and q be integers satisfying

1 ≤ q ≤ n, (a, q) = 1, |qα − a| ≤ q−1.

Then
 f (α) ≪ (log n)3 (nq−1/2 + n
4/5 + n
1/2q1/2) .

This is the sharpest known version of the estimate for f (α) established by I. M. Vino-
gradov [236] in 1937. As we mentioned in the Introduction, that result was the main inno-
vation in Vinogradov’s proof of Theorem 1. The above version is due to Vaughan [225].
We shall explain the proof of Lemma 3.1 in the next section and now we shall use it to
establish (3.17). To this end we need also the following lemma, known as Dirichlet’s theorem
on diophantine approximation; its proof is elementary and can be found in [228, Lemma 2.1].

Lemma 3.2 (Dirichlet). Let α and Q be real and Q ≥ 1. There exist integers a and q
such that
 1 ≤ q ≤ Q, (a, q) = 1, |qα − a| < Q
−1.

19

Let α ∈ m. By (3.5) and Lemma 3.2 with Q = nP −1, there are integers a and q such
that
 P < q ≤ nP −1, (a, q) = 1, |qα − a| < P n
−1 ≤ q−1.

Hence, an appeal to (3.3) and Lemma 3.1 gives

f (α) ≪ (log n)3 (
nP −1/2 + n
4/5) ≪ n(log n)3−B/2.(3.18)

and (3.17) follows on choosing B ≥ 12. This completes the proof of Theorem 1.

The above proof of Vinogradov’s theorem employs the Siegel–Walﬁsz theorem and, there-
fore, is ineﬀective (recall the remark following the statement of Theorem 7). The interested
reader can ﬁnd an eﬀective proof (with a slightly weaker error term) in [116, Chapter 10].

3.1.4 The estimation of f (α)

The main tool in the proof of Lemma 3.1 are estimates for bilinear sums of the form

S = ∑

X<x≤2X
 ∑

Y <y≤2Y
xy≤n
 ξxηye(αxy).(3.19)

We need to control two kinds of such sums, known as type I sums and type II sums. For
simplicity, we describe these two types of sums in the simplest cases, noting that the more
general sums arising in the actual proof of Lemma 3.1 can be reduced to these special cases
using standard trickery:

• type I sums: sums (3.19) with |ξx| ≤ 1, ηy = 1 for all y, and X is “not too large”;

• type II sums: sums (3.19) with |ξx| ≤ 1, |ηy| ≤ 1, and X, Y are “neither large, nor
small”.

Vinogradov reduced the estimation of f (α) to the estimation of type I and type II sums
by means of an intricate combinatorial argument. Nowadays we can achieve the same result
almost instantaneously by referring to the combinatorial identities of Vaughan [223, 225]
or Heath-Brown [84]. Let Λ(k) denote von Mangoldt’s function, whose value is log p or 0
according as k is a power of a prime p or not. Vaughan’s identity states that if U and V are
real parameters exceeding 1, then

Λ(k) = ∑

dm=k
1≤d≤V
 µ(d) log m − ∑

dlm=k
1≤d≤V
1≤m≤U
 µ(d)Λ(m) − ∑

dlm=k
1≤d≤V
m>U,dl>V
 µ(d)Λ(m).(3.20)

Heath-Brown’s identity states that if k ≤ x and J is a positive integer, then

Λ(k) =
 J∑

j=1
 (
J
j
 )
(−1)
j−1 ∑

m1···m2j =k
m1,...,mj ≤x1/J
 µ(m1) · · · µ(mj) log m2j,

20

where µ(m) is the M¨obius function.
Both identities can be used to reduce f (α) to type I and type II sums with equal success.
Here, we apply Vaughan’s identity with U = V = n
2/5. We obtain
∑

k≤n Λ(k)e(αk) = W1 − W2 − W3,(3.21)

with
 Wj = ∑

k≤n aj(k)e(αk) (1 ≤ j ≤ 3)

where aj(k) denotes the jth sum on the right side of (3.20). The estimation of the sum on
the left side of (3.21) is essentially equivalent to that of f (α). The sums W1 and W2 on the
right side of (3.21) can be reduced to type I sums with X ≪ n
4/5; W3 can be reduced to
type II sums with n
2/5 ≪ X, Y ≪ n
3/5. The reader can ﬁnd all the details in the proof of
[228, Theorem 3.1]. Here we will be content with a brief description of the estimation of the
type I and type II sums.
Consider a type I sum S1. We have

|S1| ≤ ∑

X<x≤2X
 ∣
∣
∣ ∑

Y <y≤Y ′ e(αxy)∣
∣
∣,(3.22)

where Y ′ = min(2Y, n/x). We can estimate the inner sum in (3.22) by means of the elemen-
tary bound ∣
∣
∣ ∑

a<y≤b e(αy)∣
∣
∣ ≤ min (b − a + 1, ∥α∥−1) ,(3.23)

where ∥α∥ denotes the distance from α to the nearest integer. This inequality follows on
noting that the sum on the left is the sum of a geometric progression. We obtain

|S1| ≤ ∑

x≤2X min (Y, ∥αx∥−1) = T (α), say.(3.24)

Obviously, the trivial estimate for T (α) is

T (α) ≪ XY.

However, under the hypotheses of Lemma 3.1, one can establish by elementary methods that
(see [228, Lemma 2.2])
 T (α) ≪ XY ( 1
q + 1
Y + q
XY
 ) log(2XY q).(3.25)

Inserting this bound into the right side of (3.24), we obtain a satisfactory bound for S1.
To estimate a type II sum S2, we ﬁrst apply Cauchy’s inequality and get

|S2|2 ≪ Y ∑

Y <y≤2Y
 ∣
∣
∣ ∑

X<x≤X′ ξxe(αxy)∣
∣
∣
2,

21

where X ′ = min(2X, n/y). Squaring out and interchanging the order of summation, we
deduce
 |S2|2 ≪ Y ∑

Y <y≤2Y
 ∑

X<x1,x2≤X′ ξx1ξx2e(α(x1 − x2)y)

≪ Y ∑

X<x1,x2≤2X
 ∣
∣
∣ ∑

Y <y≤Y ′ e(α(x1 − x2)y)∣
∣
∣

≪ Y ∑

X<x≤2X
 ∑

|h|<X
 ∣
∣
∣ ∑

Y <y≤Y ′ e(αhy)∣
∣
∣,

where Y < Y ′ ≤ 2Y . We remark that the innermost sum is now free of “unknown” weights
and can be estimated by means of (3.23). We get

|S2|2 ≪ XY 2 + XY T (α),(3.26)

and (3.25) again leads to a satisfactory bound for S2.

3.2 The exceptional set in Goldbach’s problem

We now sketch the proof of (1.5). We will not discuss the proof of the more sophisticated
results of Montgomery and Vaughan [173] and Pintz [186], since they require knowledge of
the properties of Dirichlet L-functions far beyond the scope of this survey. The reader can
ﬁnd excellent expositions of the Montgomery–Vaughan result in their original paper and also
in the monograph [177].
For an even integer n, let r(n) denote the number of representations of n as the sum of
two primes, let Z(N) denote the set of even integers n ∈ (N, 2N] with r(n) = 0, and write
Z(N) = |Z(N)|. Since
 E(x) =
 ∞∑

j=1 Z(x2−j),

it suﬃces to bound Z(N) for large N.
Deﬁne f (α), M, and m as before, with N in place of n. When n is an even integer in
(N, 2N], a variant of the method in §3.1.2 gives
∫

M f (α)2e(−αn) dα = S2(n) n
(log n)2 + O ( N
(log N)3
 ) ,

where
 S2(n) = ∏

p∤n
 (1 − 1
(p − 1)2
 ) ∏

p|n
 ( p
p − 1
 )

is the singular series. In particular, we have S2(n) ≥ 1 for even n. Thus, for n ∈ Z(N), we
have ∣
∣
∣
∣
 ∫
m f (α)2e(−αn) dα∣
∣
∣
∣ = ∣
∣
∣
∣ − ∫

M f (α)2e(−αn) dα∣
∣
∣
∣ ≫ N(log N)−2,(3.27)
 22

whence
 Z(N) ≪ N −2(log N)4 ∑

n∈Z(N )
 ∣
∣
∣
∣
 ∫
m f (α)2e(−αn) dα∣
∣
∣
∣

2.(3.28)

On the other hand, by Bessel’s inequality,

∑

n∈Z(N )
 ∣
∣
∣
∣
 ∫
m f (α)2e(−αn) dα∣
∣
∣
∣

2 ≤ ∫

m |f (α)|4 dα,(3.29)

and (3.16) and (3.18) yield
∫

m |f (α)|4 dα ≤ ( sup
α∈m |f (α)|)2 ∫ 1

0 |f (α)|2 dα ≪ N 3P −1(log N)5.(3.30)

Combining (3.28)–(3.30), we conclude that

Z(N) ≪ NP −1(log N)9 ≪ N(log N)−A,

on choosing, say, P = (log N)A+9. This completes the proof of (1.5).

3.3 The circle method in the Waring–Goldbach problem

We now turn our attention to Theorems 3 and 4. Much of the discussion in §3.1 can be
generalized to kth powers (k ≥ 2). Using (3.1), we can write R∗
k,s(n) as

R∗
k,s(n) = ∫ 1

0 f (α)se(−αn) dα,

where now
 f (α) = ∑

p≤N e (αpk) , N = n
1/k.

Deﬁne the sets of major and minor arcs as before (that is, by (3.4) and (3.5), with P =
(log N)B and B = B(k, s) to be chosen later). The machinery in §3.1.2 generalizes to kth
powers with little extra eﬀort. The argument leading to (3.10) gives

f (a
q + β) = φ(q)−1S(q, a) v(β) + error term,(3.31)

where S(q, a) is deﬁned by (1.13) and

v(β) = ∫ N

2
 e (βuk)

log u du.

23

We now raise (3.31) to the sth power and integrate the resulting approximation for f (α)s

over M. Using known estimates for v(β) and S(q, a), we ﬁnd that when s ≥ k + 1,
∫

M f (α)se(−αn) dα = S∗
k,s(n)J ∗
k,s(n) + O (
N s−kP −1/k+ε) ,(3.32)

where S∗
k,s(n) is deﬁned by (1.13) and J ∗
k,s(n) is the singular integral

J ∗
k,s(n) = ∫ ∞

−∞ v(β)se(−βn) dβ

= Γs (1 + 1
k )

Γ ( s
k ) n
s/k−1

(log n)s + O (n
s/k−1(log n)−s−1) .

This reduces the proof of Theorem 3 to the estimate
∫

m f (α)se(−αn) dα ≪ N s−k(log N)−s−1.(3.33)

Notice that when k = 1 and s = 3, (3.33) turns into (3.14). Thus, it is natural to try to
obtain variants of (3.16) and (3.17) for f (α) when k ≥ 2. To estimate the maximum of f (α)
on the minor arcs, we use the same tools as in §3.1.4, that is:

• Heath-Brown’s or Vaughan’s identity to reduce the estimation of f (α) to the estimation
of bilinear sums ∑

X<x≤2X
 ∑

Y <y≤2Y
xy≤N
 ξxηye (
α(xy)k) ;

• Cauchy’s inequality to bound those bilinear sums in terms of the quantity T (α) ap-
pearing in (3.24).

The following result due to Harman [75] is the analogue of Lemma 3.1 for k ≥ 2.

Lemma 3.3. Let k ≥ 2, let α ∈ R, and suppose that a and q are integers satisfying

1 ≤ q ≤ N k, (a, q) = 1, |qα − a| < q−1.

There is a constant c = c(k) > 0 such that

f (α) ≪ N(log N)c (q−1 + N −1/2 + qN −k)41−k .

On choosing the constant B (in the deﬁnition of m) suﬃciently large, one can use Lemmas
3.2 and 3.3 to show that, for any ﬁxed A > 0,

sup
α∈m |f (α)| ≪ N(log N)−A.

Hence, if s = 2r + 1, one has
∫

m |f (α)|s dα ≤ sup
α∈m |f (α)| ∫ 1

0 |f (α)|2r dα ≪ N(log N)−A ∫ 1

0 |f (α)|2r dα,

and it suﬃces to establish the estimate

Ir(N) := ∫ 1

0 |f (α)|2rdα ≪ N 2r−k(log N)c,(3.34)

with c = c(k, r).
 24

3.4 Mean-value estimates for exponential sums

We now turn to the proof of (3.34). By (3.1), Ir(N) represents the number of solutions of
the diophantine equation {
x
k
1 + · · · + x
k
r = x
k
r+1 + · · · + x
k
2r,
1 ≤ x1, . . . , x2r ≤ N
(3.35)

in primes x1, . . . , x2r, and therefore, Ir(N) does not exceed the number of solutions of (3.35)
in integers x1, . . . , x2r. Using (3.1) to write the latter quantity as a Fourier integral, we
conclude that
 Ir(N) ≤ ∫ 1

0 |g(α)|2rdα, g(α) = ∑

x≤N e (αx
k) .(3.36)

This reduces the estimation of the even moments of f (α) to the estimation of the respective
moments of the exponential sum g(α), whose analysis is much easier. In particular, we have
the following two results.

Lemma 3.4 (Hua’s lemma). Suppose that k ≥ 1, and let g(α) be deﬁned by (3.36). There
exists a constant c = c(k) ≥ 0 such that
∫ 1

0 |g(α)|2kdα ≪ N 2k−k(log N)c.(3.37)

Lemma 3.5. Suppose that k ≥ 11 and g(α) is deﬁned by (3.36). There exists a constant
c = c(k) > 0 such that for r > 1
2 k2(log k + log log k + c),

∫ 1

0 |g(α)|2rdα ≪ N 2r−k.(3.38)

These lemmas are, in fact, rather deep and important results in the theory of Waring’s
problem. Unfortunately, their proofs are too complicated to include in this survey in any
meaningful way. The reader will ﬁnd a proof of a somewhat weaker version of Hua’s lemma
(with a factor of N ε in place of (log N)c) in [228, Lemma 2.5] and a complete proof in
[102, Theorem 4]. Results somewhat weaker than Lemma 3.5 are classical and go back to
Vinogradov’s work on Waring’s problem (see [102, Lemma 7.13] or [228, Theorem 7.4]).
Lemma 3.5 itself follows from the results in Ford [57] (in particular, see [57, (5.4)]).
Combining (3.36) and Lemmas 3.4 and 3.5, we get (3.34) with

r =
 {
2k−1, if k ≤ 10,
[ 1
2 k2(log k + log log k + c)] + 1, if k ≥ 11.

Clearly, this completes the proof of Theorem 3, except for the case 6 ≤ k ≤ 8, which we will
skip in order to avoid the discussion of certain technical details.

25

3.5 Diminishing ranges

In this section, we describe the main new idea that leads to the bounds for H(k) in Theorem
4. This idea, known as the method of diminishing ranges, appeared for the ﬁrst time in the
work of Hardy and Littlewood on Waring’s problem and later was developed into a powerfull
technique by Davenport.
The limit of the method employed in §3.3 is set by the mean-value estimates in Lemmas
3.4 and 3.5. The key observation in the method of diminishing ranges is that it can be
much easier to count the solutions of the equation in (3.35) if the unknowns x1, . . . , x2r are
restricted to proper subsets of [1, N]. For example, the simplest version of the method that
goes back to Hardy and Littlewood uses that when N2, . . . , Nr are deﬁned recursively by

Nj = k−1N 1−1/k
j−1 (2 ≤ j ≤ r),

the equation {
x
k
1 + · · · + x
k
r = x
k
r+1 + · · · + x
k
2r,
Nj < xj, xr+j ≤ 2Nj (1 ≤ j ≤ r),
(3.35*)

has only “diagonal” solutions with xr+j = xj, j = 1, . . . , r. Thus, the number of solutions of
(3.35*) is bounded above by
 N1 · · · Nr ≪ N 2−λ
1 (N2 · · · Nr)2

where
 λ = 1 + (1 − 1
k ) + · · · + (1 − 1
k )r−1 ≥ k − ke
−r/k.

That is, we have the bound
∫ 1

0
 ∣
∣g1(α)g2(α) · · · gr(α)∣
∣2dα ≪ N 2−λ
1 (N2 · · · Nr)2,(3.39)

where
 gj(α) = ∑

Nj <x≤2Nj e (
αx
k) (1 ≤ j ≤ r).

We can use (3.39) as a replacement for the mean-value estimates in §3.4. Let Tk,s(n)
denote the number of solutions of
 pk
1 + pk
2 + · · · + pk
s = n

in primes p1, . . . , ps subject to

Nj < pj, pr+j ≤ 2Nj (1 ≤ j ≤ r), N1 < p2r+1, . . . , ps ≤ 2N1.

Then
 Tk,r(n) = ∫ 1

0 f1(α)s−2r+2f2(α)2 · · · fr(α)2e(−αn) dα,(3.40)
 26

where
 fj(α) = ∑

Nj <p≤2Nj e (αpk) (1 ≤ j ≤ r).

When r ∼ ck log k, we can use (3.39) to derive a bound of the form
∫ 1

0
 ∣
∣f1(α)2f2(α) · · · fr(α)∣
∣
2dα ≪ N 4−k
1 (N2 · · · Nr)2.

Furthermore, assuming that s is just slightly larger than 2r (it suﬃces to assume that
s ≥ 2r + 3, for example), we can then obtain an asymptotic formula for the right side of
(3.40) by the methods sketched in §3.3. This is (essentially) how one proves Theorem 4 for
k ≥ 11. The proof for k ≤ 10 follows the same general approach, except that we use more
elaborate choices of the parameters N1, . . . , Nr in (3.35*).

3.6 Kloosterman’s reﬁnement of the circle method

Consider again equation (1.9) with k = 2. The Hardy–Littlewood method in its original
form establishes the asymptotic formula (1.10) for s > 4, but it fails to prove Lagrange’s
four squares theorem. In 1926 Kloosterman [122] proposed a variant of the circle method,
known today as Kloosterman’s reﬁnement, which he used to prove an asymptotic formula
for the number of solutions of the equation

a1x
2
1 + · · · + a4x
2
4 = n,(3.41)

where ai are ﬁxed positive integers.
Denote by I(n) the number of solutions of (3.41) in positive integers xi. By (3.1),

I(n) = ∫ 1

0 H(α)e(−αn) dα,(3.42)

where
 H(α) = h(a1α) · · · h(a4α), h(α) = ∑

x≤N e (αx
2) , N = n
1/2.

A “classical” Hardy–Littlewood decomposition of the right side of (3.42) into integrals over
major and minor arcs is of little use here, since we cannot prove that the contribution from
the minor arcs is smaller than the expected main term. Kloosterman’s idea is to eliminate
the minor arcs altogether.
The elimination of the minor arcs requires greater care in the handling of the major arcs.
Let X be the integer with X − 1 < N ≤ X. It is clear that the integration in (3.42) can
be taken over the interval (X −1, 1 + X −1], which can be represented as a union of disjoint
intervals (X −1, 1 + X −1] = ⋃

q≤N
 ⋃

1≤a≤q
(a,q)=1
 (a
q − 1
qq1 , a
q + 1
qq2
 ] ,(3.43)
 27

where for each pair q, a in the union, the positive integers q1 = q1(q, a) and q2 = q2(q, a) are
uniquely determined and satisfy the conditions

N < q1, q2 ≤ 2N, aq1 ≡ 1 (mod q), aq2 ≡ −1 (mod q).(3.44)

The decomposition (3.43) is known as the Farey decomposition and provides a natural way
of partitioning of the unit interval into non-overlapping major arcs (see Hardy and Wright
[74, Section 3.8]). Let M(q, a) denote the interval in the Farey decomposition “centered” at
a/q. We have
 I(n) = ∑

q≤N
 ∑

1≤a≤q
(a,q)=1
 e
( −an
q
 ) ∫

B(q,a) H(a
q + β)
e(−βn) dβ,(3.45)

where B(q, a) is deﬁned by

B(q, a) = {β ∈ R : a/q + β ∈ M(q, a)} .(3.46)

We can ﬁnd an asymptotic formula for the integrand on the right side of (3.45). The
contribution of the main term in that asymptotic formula produces the expected main term
in the asymptotic formula for I(n). However, in order to obtain a satisfactory bound for the
contribution of the error term, we have to take into account the cancellation among terms
corresponding to diﬀerent Farey fractions a/q with the same denominator. To this end, we
want to interchange the order of integration and summation over a in (3.45). Since the
endpoints of B(q, a) depend on a, the total contribution of the error terms can be expressed
as ∑

q≤N
 ∫ 1/(qN )

−1/(qN )
 { ∑(β)

1≤a≤q
(a,q)=1
 E (a
q + β) e (−an
q
 ) }
e(−βn) dβ,(3.47)

where E(a/q + β) is the error term in the major arc approximation to H(a/q + β) and
the superscript in ∑(β) indicates that the summation is restricted to those a for which
B(q, a) ∋ β. Using (3.44) and (3.46), we can transform the latter constraint on a into a
condition about the multiplicative inverse of a modulo q, that is, the unique residue class ¯a
modulo q with ¯aa ≡ 1 (mod q). Thus, a special kind of exponential sums enter the scene:
the Kloosterman sums
 K(q; m, n) =
 q∑

x=1
(x,q)=1
 e
( mx + n¯x
q
 ).

There also other (in fact, more substantial) reasons for the Kloosterman sums to appear,
but those are too technical to include here.
The success of Kloosterman’s method hinges on the existence of suﬃciently sharp esti-
mates for K(q; m, n). The ﬁrst such estimate was found by Kloosterman himself and later
his result has been improved. Today it is known that

|K(q; m, n)| ≤ τ (q) q1/2 (m, n, q)1/2,(3.48)
 28

where (m, n, q) is the greatest common divisor of m, n, q and τ (q) is the number of positive
divisors of q. In 1948 A. Weil [243] proved (3.48) in the most important case: when q is a
prime. In the general case (3.48) was established by Estermann [55]. This estimate plays an
important role not only in the Kloosterman reﬁnement of the circle method, but in many
other problems in number theory.
Kloosterman’s method has been applied to several additive problems, and in particular,
to problems with primes and almost primes. We refer the reader, for example, to Ester-
mann [56], Hooley [99], Heath-Brown [85, 87, 88], Br¨udern and Fouvry [24], Heath-Brown
and Tolev [94].

4 Sieve methods

In this section we describe the so-called sieve methods, which are an important tool in
analytic number theory and, in particular, in the proof of Chen’s theorem (Theorem 2 in the
Introduction). We start with a brief account of the main idea of the method (§4.1 and §4.2).
This allows us in §4.3 to present a proof of a slightly weaker (but much simpler) version of
Chen’s result, in which P2-numbers are replaced by P4-numbers. We conclude the section by
sketching some of the new ideas needed to obtain Chen’s theorem in its full strength (§4.4)
and of some further work on sieve methods (§4.5).

4.1 The sieve of Eratosthenes

Let A be a ﬁnite integer sequence. We will be concerned with the existence of elements of
A that are primes or, more generally, almost primes Pr, with r bounded. In general, sieve
methods reduce such a question to counting the elements a ∈ A not divisible by small primes
p from some suitably chosen set of primes P. To be more explicit, we consider a set of prime
numbers P and a real parameter z ≥ 2 and deﬁne the sifting function

S(A, P, z) = |{a ∈ A : (a, P (z)) = 1}| , P (z) = ∏

p<z
p∈P
p,(4.1)

where |A| denotes the number of elements of a sequence A (not the cardinality of the
underlying set). In applications, the set P is usually taken to be the set of possible prime
divisors of the elements of A, so the sifting function (4.1) counts the elements of A free of
prime divisors p < z.
In order to bound S(A, P, z), we recall the following fundamental property of the M¨obius
function (see [74, Theorem 263]):

∑

d|k µ(d) =
 {1, if k = 1,
0, if k > 1.
(4.2)

Using this identity, we can express the sifting function in the form

S(A, P, z) = ∑

a∈A
 ∑

d|(a,P (z)) µ(d).(4.3)
 29

We can now interchange the order of summation to get

S(A, P, z) = ∑

d|P (z) µ(d)|Ad|,(4.4)

where
 Ad = {a ∈ A : a ≡ 0 (mod d)}.

To this end, we suppose that there exist a (large) parameter X and a multiplicative function
ω(d) such that |Ad| can be approximated by Xω(d)/d. We write r(X, d) for the error term
in this approximation, that is,
 |Ad| = X ω(d)
d + r(X, d).(4.5)

We expect r(X, d) to be ‘small’, at least in some average sense over d. Substituting (4.5)
into the right side of (4.4), we ﬁnd that

S(A, P, z) = XV (z) + R(X, z),(4.6)

where
 V (z) = ∑

d|P (z) µ(d) ω(d)
d , R(X, z) = ∑

d|P (z) µ(d)r(X, d).(4.7)

We would like to believe that, under ‘ideal circumstances’, (4.6) is an asymptotic formula
for the sifting function S(A, P, z), XV (z) being the main term and R(X, z) the error term.
However, such expectations turn out to be unrealistic, as we are about to demonstrate.
Let us try to apply (4.6) to bound above the number of primes ≤ x. We choose

A = {n ∈ N : n ≤ x}, P = {p : p is a prime}.(4.8)

Then
 |Ad| = [ x
d
 ] = x
d + r(x, d), |r(x, d)| ≤ 1,

that is, X = x and ω(d) = 1 for all d. Using an elementary property of multiplicative
functions (see [74, Theorem 286]), we can write V (z) as

V (z) = ∏

p<z
 (
1 − ω(p)
p
 ) .(4.9)

When ω(p) = 1, this identity and an asymptotic formula due to Mertens (see [74, Theorem
429]) reveal that the main term in (4.6) is

XV (z) = X ∏

p<z
 (
1 − 1
p
 ) ∼ X e
−γ

log z as z → ∞;(4.10)
 30

here γ = 0.5772 . . . is Euler’s constant. Thus, if A and P are as in (4.8) and z = x
1/2, the
projected ‘main term’ in (4.6) is ∼ 2e
−γx(log x)−1 as x → ∞, whereas the true size of the
sifting function on the left side is

S(A, P, √x) = π(x) − π(√x) + 1 ∼ x
log x as x → ∞,

by the Prime Number Theorem. Since 2e
−γ = 1.122 . . . , we conclude that the ‘error term’
R(x, √x) is in this case of the same order of magnitude as the ‘main term’.
Identity (4.6) is known as the sieve of Eratosthenes–Legendre. The basic idea goes back
to the ancient Greeks (usually attributed to Eratosthenes), while the formal exposition above
is essentially due to Legendre, who used the above argument to show that

π(x) ≪ x
log log x.

The sieve of Eratosthenes–Legendre can be extremely powerful in certain situations
7, but in
most cases the sum R(X, z) contains ‘too many’ terms for (4.6) to be of any practical use
(e.g., in the above example, R(X, z) contains 2π(z) terms). Modern sieve methods use various
clever approximations to the left side of (4.2) to overcome this problem. In the following
sections, we describe one of the variants of one the existing approaches. The reader can ﬁnd
other constructions, comparisons of the various approaches, and proofs in the monographs
on sieve methods [63, 66, 174] or in [90] (see also the remarks in §4.5 for other references).

4.2 The linear sieve

Let y > 0 be a parameter to be chosen later in terms of X and suppose that λ+(d) and
λ−(d) are real-valued functions supported on the squarefree integers d (i.e., λ±(d) = 0 if d is
divisible by the square of a prime). Furthermore, suppose that

|λ±(d)| ≤ 1 and λ±(d) = 0 for d ≥ y,(4.11)

and that ∑

d|n λ−(d) ≤ ∑

d|n µ(d) ≤ ∑

d|n λ+(d) for all n = 1, 2, . . . .(4.12)

Using (4.3) and the left inequality in (4.12), we obtain

S(A, P, z) ≥ ∑

a∈A
 ∑

d|(a,P (z)) λ−(d).

7For example, I. M. Vinogradov’s combinatorial argument for converting sums over primes into linear
combinations of type I and type II sums is based on a variant of (4.6). See Harman [79] for other applications
and further discussion.
 31

We can interchange the order of summation in the right side of this inequality and apply
(4.5) and (4.11) to get the bound

S(A, P, z) ≥ ∑

d|P (z) λ−(d)|Ad| = ∑

d|P (z) λ−(d) (
X ω(d)
d + r(X, d))

= X ∑

d|P (z) λ−(d) ω(d)
d + ∑

d|P (z) λ−(d)r(X, d) ≥ XM− − R,

where
 M± = ∑

d|P (z) λ±(d) ω(d)
d , R = ∑

d|P (z)
d<y
 |r(X, d)|.(4.13)

In a similar fashion, we can use the right inequality in (4.12) to estimate the sifting function
from above. That is, we have

XM− − R ≤ S(A, P, z) ≤ XM+ + R.(4.14)

We are now in a position to overcome the diﬃculty caused by the “error term” in the
Eratosthenes–Legendre sieve. The sum R is similar to the error term R(X, z) deﬁned in
(4.7), but unlike R(X, z) we can use the parameter y to control the number of terms in
R. Thus, our general strategy will be to construct functions λ±(d) which satisfy (4.11) and
(4.12) and for which the sums M± are of the same order as the sum V (z) deﬁned in (4.7).
There are various constructions of such functions λ±(d). However, since it is not our goal to
give a detailed treatment of sieve theory here, we will simply state one of the modern sieves
in a form suitable for an application to the binary Goldbach problem.
The sieve method we will use is known as the Rosser–Iwaniec sieve. Its idea appeared
for the ﬁrst time in an unpublished manuscript by Rosser. The full-ﬂedged version of this
sieve was developed independently by Iwaniec [105, 106]. Suppose that the multiplicative
function ω in (4.5) satisﬁes the condition

∏

w1≤p<w2
 (
1 − ω(p)
p
 )−1 ≤ (log w2
log w1
 )κ (1 + K
log w1
 ) (2 ≤ w1 < w2),(4.15)

where κ > 0 is an absolute constant known as the sieve dimension and K > 0 is independent
of w1 and w2. This inequality is usually interpreted as an average bound for the values taken
by ω(p) when p is prime, since it is consistent with the inequality ω(p) ≤ κ. In our application
of the sieve to Goldbach’s problem, we will have to deal with a sequence A (given by (1.7))
for which (4.15) holds with κ = 1, so we will state the Rosser–Iwaniec sieve in this special
case, in which it is known as the linear sieve.
Suppose that ω(p) satisﬁes (4.15) with κ = 1 and that

0 < ω(p) < p when p ∈ P and ω(p) = 0 when p ̸∈ P.(4.16)
 32

We put λ±(1) = 1 and λ±(d) = 0 if d is not squarefree. If d > 1 is squarefree and has prime
decomposition d = p1 · · · pr, p1 > p2 > · · · > pr, we deﬁne

λ+(d) =
 {(−1)
r if p1 · · · p2lp3
2l+1 < y whenever 0 ≤ l ≤ (r − 1)/2,
0 otherwise,
(4.17)
 λ−(d) =
 {(−1)
r if p1 · · · p2l−1p3
2l < y whenever 1 ≤ l ≤ r/2,
0 otherwise.
(4.18)

It can be shown (see [63, 105]) that these two functions satisfy conditions (4.11) and (4.12).
Furthermore, if the quantities M± are deﬁned by (4.13) with λ±(d) given by (4.17) and
(4.18), we have

V (z) ≤ M+ ≤ V (z) (F (s) + O(
e
−s(log y)−1/3)) for s ≥ 1,(4.19)
 V (z) ≥ M− ≥ V (z) (f (s) + O(
e
−s(log y)−1/3)) for s ≥ 2,(4.20)

where s = log y/ log z and the functions f (s) and F (s) are the continuous solutions of a
system of diﬀerential delay equations (see [63, 105]). The analysis of that system reveals
that the function F (s) is strictly decreasing for s > 0, that the function f (s) is strictly
increasing for s > 2, and that

0 < f (s) < 1 < F (s) for s > 2.(4.21)

Furthermore, both functions are very close to 1 for large s. More precisely, they satisfy

F (s), f (s) = 1 + O(s−s) as s → ∞.(4.22)

Substituting (4.19) and (4.20) into (4.14), we obtain

S(A, P, z) ≤ XV (z) (F (s) + O(
(log y)−1/3)) + R for s ≥ 1,(4.23)
 S(A, P, z) ≥ XV (z) (f (s) + O(
(log y)−1/3)) − R for s ≥ 2,(4.24)

where R is deﬁned by (4.13).
We now return to our initial goal—namely, to prove that the sequence A contains almost
primes. We want to use (4.24) to show that

S(A, P, X α) > 0(4.25)

for some ﬁxed α > 0. This will imply the existence of an a ∈ A all of whose prime divisors
exceed X α. If |a| ≪ X g for all a ∈ A, it will then follow that A contains a Pr-number, where
r ≤ g/α. Clearly, since we want to minimize r, we would like to take α as large as possible.
On the one hand, in order to derive (4.25) from (4.24), we need to ensure that the main
term in (4.24) is positive and that the error term R is of a smaller order of magnitude than
the main term. It is the balancing of these two requirements that determines the optimal
choice for z and, ultimately, the quality of our result. In view of (4.21), the positivity of the
main term in (4.24) requires choosing y slightly larger than z2. On the other hand, while in
some applications the estimation of R is easier than in others, it is always the case that it
imposes a restriction on how large we can choose y, and hence, how large we can choose z.
In the next section, we demonstrate how this general approach works when applied to the
binary Goldbach problem.
 33

4.3 The linear sieve in the binary Goldbach problem

In this section, we apply the linear Rosser–Iwaniec sieve to the sequence A in (1.7) and the
set P of odd primes that do not divide n, that is,

A = A(n) = {n − p : 2 < p < n} and P = {p : p > 2, p ∤ n}.

It is clear that all elements of A are odd numbers and that at most log n of them may have
a common prime factor with n (for (n, n − p) > 1 implies p | n, and n has at most log n odd
prime factors). Thus, P is the set of “typical” prime divisors of elements of A.
Next, we proceed to deﬁne the quantity X and the multiplicative function ω(d) in (4.5).
We have
 |Ad| = ∑

2<p<n
p≡n (mod d)
 1 = π(n; d, n) − 1,(4.26)

so the prime number theorem for arithmetic progressions suggests the choice

X = li n and ω(d) =
 {d/φ(d) if (d, n) = 1,
0 otherwise.
(4.27)

With this choice, the error terms r(X, d) deﬁned by (4.5) satisfy the inequality

|r(X, d)| ≤
 



1 + ∣
∣
∣
∣π(n; d, n) − li n
φ(d)
 ∣
∣
∣
∣ if (d, n) = 1,

1 otherwise.

It then follows from the Bombieri–Vinogradov theorem (Theorem 8) that

R ≤ y + ∑

d≤y max
(a,d)=1
 ∣
∣
∣
∣π(n; d, a) − li n
φ(d)
∣
∣
∣
∣ ≪ n(log n)−3,(4.28)

whenever y ≤ n
1/2(log n)−6. Furthermore, we have

V (z) = ∏

p<z
p∤n
 (1 − 1
p − 1
 ) ≥ ∏

p<z
 (
1 − 1
p − 1
 ) ≫ (log z)−1.(4.29)

On choosing y = n
1/2(log n)−6 and z = n
2/9, we have

log y
log z = 9
4 + O ( log log n
log n
 ) > 2.2,

provided that n is suﬃciently large. Hence, we deduce from (4.21), (4.24) and (4.27)–(4.29)
that
 S(A, P, z) ≫ n(log n)−2.(4.30)
 34

That is, there are ≫ n(log n)−2 elements of A that have no prime divisors smaller than n
2/9.
Since the numbers in A do not exceed n, the elements of A counted on the left side of (4.30)
have at most four prime divisors each, that is, the left side of (4.30) counts solutions of
n − p = P4.

We have some freedom in our choice of parameters in the above argument. For example,
we could have set z = n
α, where α is any ﬁxed real number in the range 1/5 < α < 1/4. Of
course, what we would really like to do is set z = n
α, where α > 1/4. With such a choice for z,
the above argument would establish the existence of inﬁnitely many solutions to n − p = P3.
Unfortunately, our choice of z is restricted (via the condition s = log y/ log z > 2) by the
largest value of Q admissible in the Bombieri–Vinogradov theorem. In particular, in order
to be able to choose z = n
1/4, we would need a version of the Bombieri–Vinogradov theorem
that holds for Q ≤ x
1/2+ε.

4.4 Weighted sieves and Chen’s theorem

The idea of a weighted sieve was introduced by Kuhn [124] who observed that instead of the
sifting function S(A, P, z) one may consider a more general sum of the type

W (A, P, z) = ∑

a∈A,
(a,P (z))=1
 w(a),(4.31)

where w(a) are weights at one’s disposal to choose. It is common to use weights of the form

w(a) = 1 − ∑

p|a
z≤p<z1
 ωp,(4.32)

with suitably chosen 0 ≤ ωp < 1. With such a choice of w(a), (4.31) can be written in the
form
 W (A, P, z) = S(A, P, z) − ∑

z≤p<z1 ωpS(Ap, P, p).(4.33)

We can now use an ordinary sieve to estimate the right side of (4.33). For example, we
can appeal to (4.24) to bound S(A, P, z) from below and to (4.23) to bound each sifting
function S(Ap, P, p) from above. If the resulting lower bound for the right side of (4.33) is
positive, we then conclude that there exist elements a of A with w(a) > 0. Such numbers a
have no prime divisors p < z and the number of their prime divisors with z ≤ p < z1 can be
controlled via the choice of the ωp’s.
The above idea plays an important role in improvements on the result established in §4.3.
Using weighted sieves, Buchstab [29] and Richert [196] proved that every suﬃciently large
even n can be represented as the sum of a prime and a P3-number. Richert used weights of
the form
 w(a) = 1 − θ ∑

p|a
z≤p<z1
 (1 − log p
log z1
 ) ,

35

while Buchstab’s weights were somewhat more complicated. Chen’s proof of Theorem 2 uses
weights of the form (4.32) with z = n
1/10, z1 = n
1/3, and

ωp = 1
2 + 1
2 δp(a),

where
 δp(a) =
 {
1 if a = pp1p2 with p1 ≥ z1,
0 otherwise.

Here, n is the even number appearing in the statement of Theorem 2 and a is an element of
the sequence (1.7). With this choice of ωp, successful sifting produces numbers a ∈ A with
w(a) > 0 and no prime divisors p < n
1/10. One can prove that any such number a must in
fact be a P2-number. The reader can ﬁnd a detailed proof of Chen’s theorem in [66, Chapter
11], [175, Chapter 10], or [178, Chapter 9].

4.5 Other sieve methods

We conclude our discussion of sieve methods with a brief account of some of the important
ideas in sieve theory left out of the previous sections.

Selberg’s sieve. The Rosser–Iwaniec sieve deﬁned by (4.17) and (4.18) is not particularly
sensitive to the arithmetical nature of the sequence A that is being sifted. In fact, the
only piece of information about A that the Rosser–Iwaniec sieve does take into account
is its sieve dimension. Such sieves are known as combinatorial. Selberg [204] proposed
another approach, which uses the multiplicative function ω(d) appearing in (4.5) to construct
essentially best possible upper sieve weights λ+(d) for a given sequence A.
Suppose that ρ(d) is a real function such that ρ(1) = 1. Then

∑

d|n µ(d) ≤
 


∑

d|n ρ(d)




2
 .

We can apply this inequality to estimate S(A, P, z) as follows:

S(A, P, z) ≤ ∑

a∈A
 


∑

d|n ρ(d)




2
 = ∑

a∈A
 ∑

d1,d2|n ρ(d1)ρ(d2)

= ∑

d1,d2 ρ(d1)ρ(d2)∣
∣A[d1,d2]∣
∣,

where |Ad| is as before and [d1, d2] is the least common multiple of d1 and d2. Using (4.5),
we ﬁnd that
 S(A, P, z) ≤ XW + R
′,

36

where
 W = ∑

d1,d2 ρ(d1)ρ(d2) ω([d1, d2])
[d1, d2] , R
′ = ∑

d1,d2 ρ(d1)ρ(d2)r(X, [d1, d2]).

In order to control the “error term” R
′, we further assume that ρ(d) = 0 when d > ξ, where
ξ > 0 is a parameter. The double sum W is a quadratic form in the variables ρ(d), 1 < d ≤ ξ.
Selberg’s idea is to choose the values of these variables as to minimize this quadratic form.
More information about Selberg’s sieve—including the techniques used to construct the
lower sieve function λ−(d) of Selberg’s sieve—can be found in [66, 174] and in Selberg’s
collected works [205, 206].

The large sieve. The method known as the large sieve was introduced in 1941 by Linnik
[140], but its systematic study did not commence until R´enyi’s work [195] on the binary
Goldbach problem. The original idea of Linnik and R´enyi evolved into a general analytic
principle that has penetrated analytic number theory on many levels (and perhaps does not
warrant the name “sieve” anymore, but the term has survived for historical reasons). The
most prominent application of the large sieve is the Bombieri–Vinogradov theorem. The
reader will ﬁnd discussion of the number-theoretic aspects of the large sieve in [20, 49, 171]
and of the analytic side of the story in [49, 171, 172].

Alternative form of the error term in the sieve. Iwaniec [106] obtained a variant of
the linear sieve featuring an error term that is better suited for certain applications than the
error term R deﬁned in (4.13). It is of the form
∑

m<M
m|P (z)
 ∑

n<N
n|P (z)
 ambnr(X, mn),(4.34)

where the coeﬃcients am and bn are bounded above in absolute value and r(X, mn) are
the remainder terms deﬁned earlier. In some applications, one can use the bilinearity of this
expression to estimate the double sum when the product MN is larger than the largest value
of y for which one can obtain a satisfactory bound for R. Iwaniec [104] used this idea in his
proof that certain quadratic polynomials take on inﬁnitely P2-numbers (recall §2.4).

Prime detecting sieves. For a long time it was believed that sieve methods are not
capable of detecting prime numbers; there are even a couple of prominent papers (see [21,
205]) that quantify the shortcomings of the classical sieve technology. In short, classical
sieves are incapable of distinguishing between integers having even number of prime divisors
and those having an odd number of prime divisors (this is known in sieve theory as the parity
obstacle). A prime detecting sieve overcomes the parity obstacle by combining the general
sieve philosophy with additional analytic information. A variant of the basic idea can be
traced all the way back to Vinogradov’s work on sums over primes, but the ﬁrst explicit
uses of prime detecting sieves appeared in the late 1970s in investigations of the distribution
of primes in short intervals (see [91, 107]). The method ﬂourished during the last decade

37

and has been instrumental in the proofs of several of the restults mentioned in the previous
sections: the result of Friedlander and Iwaniec [58] on prime values of x
2 + y4; the results
of Heath-Brown and Moroz [89, 92] on prime values of binary cubic forms; and the result
of Baker, Harman, and Pintz [9] on primes in short intervals are just three such examples.
Compared to classical sieve methods, the theory of prime detecting sieves is still in its infancy
and thus the general literature on the subject is relatively scarce, but the reader eager to
learn more about such matters will ﬁnd two excellent expositions in [59] and [79].

5 Other work on the Waring–Goldbach problem

In the Introduction, we mentioned the cornerstones in the study of the Goldbach and Waring–
Goldbach problems. However, as is often the case in mathematics, those results are inter-
twined with a myriad of other results on various aspects and variants of the two main
problems. In this ﬁnal section, we describe some of the more important results of the latter
kind. The circle method, sieve methods, or a combination of them play an essential role in
the proofs of all these.

5.1 Estimates for exceptional sets

Inspired by the work of Chudakov [42] and Estermann [54] on the exceptional set in the
binary Goldbach problem, Hua studied the function h(k), deﬁned to be the least s such that
almost all integers n ≤ x, n ≡ s (mod K(k)), can be written as the sum of s kth powers of
primes (K(k) is deﬁned by (1.12)). Let Ek,s(x) denote the number of exceptions, that is, the
number of integers n, with n ≤ x and n ≡ s (mod K(k)), for which (1.14) has no solution
in primes p1, . . . , ps. Hua showed (essentially) that if H(k) ≤ s0(k), then Ek,s(x) = o(x) for
any s ≥ 1
2s0(k). Later, Schwarz [202] reﬁned Hua’s method to show that

Ek,s(x) ≪ x(log x)−A(5.1)

for any ﬁxed A > 0.
In recent years, motivated by the estimate (1.6) of Montgomery and Vaughan, several
authors have pursued similar estimates for exceptional sets for squares and higher powers of
primes. The ﬁrst to obtain such an estimate were Leung and Liu [134], who showed that
E2,3(x) ≪ x
1−δ, with an absolute constant δ > 0. Explicit versions of this result were later
given in [16, 80, 128, 159, 160], the best result to date being the estimate (see Harman and
Kumchev [80])
 E2,3(x) ≪ x
6/7+ε.

Furthermore, several authors [80, 147, 149, 155, 249] obtained improvements on Hua’s bound
(5.1) for E2,4(x), the most recent being the bound

E2,4(x) ≪ x
5/14+ε,

38

established by Harman and Kumchev [80]. Ren [194] studied the exceptional set for sums of
ﬁve cubes of primes and proved that

E3,s(x) ≪ x
1−(s−4)/153 (5 ≤ s ≤ 8).

This estimate has since been improved by Wooley [248] and Kumchev [126]. In particular,
Kumchev [126] showed that

E3,5(x) ≪ x
79/84, E3,6(x) ≪ x
31/35,
E3,7(x) ≪ x
51/84, E3,8(x) ≪ x
23/84.

Finally, Kumchev [126] has developed the necessary machinery to obtain estimates of the
form Ek,s(x) ≪ x
1−δ, with explicit values of δ = δ(k, s) > 0, for all pairs of integers k ≥ 4
and s for which an estimate of the form (5.1) is known.
In 1973 Ramachandra [192] considered the exceptional set for the binary Goldbach prob-
lem in short intervals. He proved that if y ≥ x
7/12+ε and A > 0, then

E(x + y) − E(x) ≪ y(log x)−A,

where the implied constant depends only on A and ε. After a series of improvements on this
result [8, 52, 53, 111, 112, 115, 135, 167, 182], this estimate is now known for y ≥ x
7/108+ε

(see Jia [115]). Lou and Yao [164, 250] were the ﬁrst to pursue a short interval version of
the estimate (1.6) of Montgomery and Vaughan. Their result was substantially improved by
Peneva [180] and the best result in this direction, due to Languasco [131], states that there
exists a small constant δ > 0 such that

E(x + y) − E(x) ≪ y1−δ/600,

whenever y ≥ x
7/24+7δ.
Furthermore, J. Liu and Zhan [157] and Mikawa [169] studied the quantity E2,3(x) in
short intervals and the latter author showed that

E2,3(x + y) − E2,3(x) ≪ y(log x)−A

for any ﬁxed A > 0 and any y ≥ x
1/2+ε.

5.2 The Waring–Goldbach problem with almost
primes

There have also been attempts to gain further knowledge about the Waring–Goldbach prob-
lem by studying closely related but more accessible problems. The most common such vari-
ants relax the multiplicative constraint on (some of) the variables. Consider, for example,
Lagrange’s equation
 x
2
1 + x
2
2 + x
2
3 + x
2
4 = n.(5.2)

Greaves [62] proved that every suﬃciently large n ̸≡ 0, 1, 5 (mod 8) can be represented in
the form (5.2) with x1, x2 primes and x3, x4 (unrestricted) integers. Later, Plaksin [189] and

39

Shields [207] found independently an asymptotic formula for the number of such representa-
tions. Br¨udern and Fouvry [24] proved that every suﬃciently large integer n ≡ 4 (mod 24)
can be written as the sum of four squares of P34-numbers. Heath-Brown and Tolev [94]
established, under the same hypothesis on n, that one can solve (5.2) in one prime and three
almost primes of type P101 or in four almost primes, each of type P25. Tolev [218] has recently
improved the results in [94], replacing the types of the almost primes involved by P80 and
P21, respectively. We must also mention the recent result by Blomer and Br¨udern [17] that
all suﬃciently large integers n such that n ≡ 3 (mod 24) and 5 ∤ n are sums of three almost
primes of type P521 (and of type P371 if n is also squarefree).
In 1951 Roth [200] proved that if n is suﬃciently large, the equation

x
3 + p3
1 + · · · + p3
7 = n(5.3)

has solutions in primes p1, . . . , p7 and an integer x. Br¨udern [22] showed that if n ≡
4 (mod 18), then x can be taken to be a P4-number, and Kawada [118] used an idea from
Chen’s proof of Theorem 2 to obtain a variant of Br¨udern’s result for almost primes of type
P3. Furthemore, Br¨udern [23] proved that every suﬃciently large integer is the sum of the
cubes of a prime and six almost-primes (ﬁve P5-numbers and a P69-number) and Kawada
[119] has shown that every suﬃciently large integer is the sum of seven cubes of P4-numbers.
Wooley [249] showed that all but O(
(log x)6+ε) integers n ≤ x, satisfying certain natural
congruence conditions can be represented in the form (5.2) with prime variables x1, x2, x3
and an integer x4. Tolev [219] established a result of similar strength for the exceptional set
for equation (5.2) with primes x1, x2, x3 and an almost prime x4 of type P11.

5.3 The Waring–Goldbach problem with restricted
variables

Through the years, a number of authors have studied variants of the Goldbach and Waring–
Goldbach problems with additional restrictions on the variables. In 1951 Haselgrove [82]
announced that every suﬃciently large odd integer n is the sum of three primes p1, p2, p3
such that |pi − n/3| ≤ n
63/64+ε. In other words, one can take the primes in Vinogradov’s
three prime theorem to be “almost equal”. Subsequent work by several mathematicians
[7, 34, 109, 110, 177, 254] tightened the range for the pi’s to |pi − n/3| ≤ n
4/7 (see Baker and
Harman [7]).
Furthermore, Bauer, Liu, and Zhan [13, 156, 158] considered the problem of representa-
tions of an integer as sums of ﬁve squares of almost equal primes. The best result to date is
due to Liu and Zhan [158], who proved that every suﬃciently large integer n ≡ 5 (mod 24)
can be written as
 n = p2
1 + · · · + p2
5,

with primes p1, . . . , p5 satisfying |p2
i − n/5| < n
45/46+ε. Liu and Zhan [156] also showed that
the exponent 45
46 can be replaced by 19
20 on the assumption of GRH.
In 1986 Wirsing [244] proved that there exist sparse sequences of primes S such that
every suﬃciently large odd integer can be represented as the sum of three primes from S.

40

However, his method was probabilistic and did not yield an example of such a sequence.
Thus, Wirsing proposed the problem of ﬁnding “natural” examples of arithmetic sequences
having this property. The ﬁrst explicit example was given by Balog and Friedlander [12].
They proved that the sequence of Piatetski-Shapiro primes (recall (2.13)) is admissible for
1 < c < 21/20. Jia [113] improved the range for c to 1 < c < 16/15, and Peneva [181]
studied the binary problem with a Piatetski-Shapiro prime and an almost prime. Tolev [215]–
[217] and Peneva [179] considered additive problems with prime variables p such that the
integers p + 2 are almost-primes. For example, Tolev [217] proved that every suﬃciently
large n ≡ 3 (mod 6) can be represented as the sum of primes p1, p2, p3 such that p1 + 2 = P2,
p1 + 2 = P5, and p1 + 2 = P7. Green and Tao announced at the end of [64] that, using their
method, one can prove that there are arbitrarily long non trivial arithmetic progressions
consisting of primes p such that p + 2 = P2. They presented in [65] a proof of this result for
progressions of three primes.

5.4 Linnik’s problem and variants

In the early 1950s Linnik proposed the problem of ﬁnding sparse sequences A such that all
suﬃciently large integers n (possibly subject to some parity condition) can be represented
as sums of two primes and an element of A. He considered two special sequences. First,
he showed [143] that if GRH holds, then every suﬃciently large odd n is the sum of three
primes p1, p2, p3 with p1 ≪ (log n)3. Montgomery and Vaughan [173] sharpened the bound
on p1 to p1 ≪ (log n)2 and also obtained an unconditional result with p1 ≪ n
7/72+ε; the
latter bound has been subsequently improved to p1 ≪ n
0.02625 (this follows by the original
argument of Montgomery and Vaughan from recent results of Baker, Harman, and Pintz [9]
and Jia [114]).
Linnik [142, 144] was also the ﬁrst to study additive representations as sums of two primes
and a ﬁxed number of powers of 2. He proved, ﬁrst under GRH and later unconditionally,
that there is an absolute constant r such that every suﬃciently large even integer n can be
expressed as the sum of two primes and r powers of 2, that is, the equation

p1 + p2 + 2ν1 + · · · + 2νr = n,

has solutions in primes p1, p2 and non-negative integers ν1, . . . , νr. Later Gallagher [60]
established the same result by a diﬀerent method. Several authors have used Gallagher’s
approach to ﬁnd explicit values of the constant r above (see [137, 138, 150, 151, 152, 242]);
in particular, Li [138] proved that r = 1906 is admissible and Wang [242] obtained r =
160 under GRH. Recently, Heath-Brown and Puchta [93] and Pintz and Ruzsa [187] made
(independently) an important discovery that leads to a substantial improvement on the
earlier results. Their device establishes Linnik’s result with r = 13 (see [93]) and with
r = 7 under GRH (see [93, 187]). Furthermore, Pintz and Rusza [188] have announced an
unconditional proof of the case r = 8.
There is a similar approximation to the Waring–Goldbach problem for four squares of
primes. J. Y. Liu, M. C. Liu, and Zhan [153, 154] proved that there exists a constant r such
that every suﬃciently large even integer n can be expressed in the form

p2
1 + p2
2 + p2
3 + p2
4 + 2ν1 + · · · + 2νr = n,

41

where p1, . . . , p4 are primes and ν1, . . . , νr are non-negative integers. J. Y. Liu and M. C. Liu
[148] established this result with r = 8330 and considered also the related problem about
representations of integers as sums of a prime, two squares of primes and several powers of
2.

5.5 Additive problems with mixed powers

In 1923 Hardy and Littlewood [71] used the general philosophy underlying the circle method
to formulate several interesting conjectures. For example, they stated a conjectural asymp-
totic formula for the number of representations of a large integer n in the form

p + x
2 + y2 = n,(5.4)

where p is a prime and x, y are integers. Their prediction was conﬁrmed in the late 1950s,
ﬁrst by Hooley [97] under the assumption of GRH and then unconditionally by Linnik [145].
The reader will ﬁnd the details of the proof in [98, 146].
In another conjecture, Hardy and Littlewood proposed an asymptotic formula for the
number of representations of a large integer n as the sum of a prime and a square. While
such a result appears to lie beyond the reach of present methods, Miech [166] showed that
this conjecture holds for almost all integers n ≤ x. Let Ek(x), k ≥ 2, denote the number of
integers n ≤ x such that the equation n = p + x
k has no solution in a prime p and an integer
x. Miech obtained the bound E2(x) ≪ x(log x)−A for any ﬁxed A > 0. Subsequent work
of Br¨udern, Br¨unner, Languasco, Mikawa, Perelli, Pintz, Polyakov, A. I. Vinogradov, and
Zaccagnini [26, 28, 132, 168, 183, 190, 235, 251] extended and sharpened Miech’s estimate
considerably. Here is a list of some of their results:

• For any ﬁxed k ≥ 2, we have Ek(x) ≪ x
1−δk , where δk > 0 depends at most on k; see
[28, 190, 235] for the case k = 2 and [183, 251] for the general case.

• Assuming GRH, we have Ek(x) ≪ x
1−δk , where δk = 1/(k2k) or δk = 1/(25k) according
as 2 ≤ k ≤ 4 or k ≥ 5; see [183] and [26].

• If k ≥ 2 is a ﬁxed integer and K = 2k−2 then there exists a small absolute constant
δ > 0 such that
 Ek(x + y) − Ek(x) ≪ y1−δ/(5K),

provided that x
(7/12)(1−1/k)+δ ≤ y ≤ x; see [132].

Furthermore, several mathematicians [14, 15, 26, 157] obtained variants of the above bounds
in the case when the variable x is also restricted to primes, while Zaccagnini [252] studied
the more general problem of representing a large integer n in the form n = p + f (x), where
f (X) ∈ Z[X].
Several interesting theorems were proved by Br¨udern and Kawada [25]. For example, one
of them states that if k is an integer with 3 ≤ k ≤ 5, then all suﬃciently large integers n
can be represented as
 x + p2
1 + p3
2 + pk
3 = n,

where pi are primes and x = P2.
 42

5.6 The Waring–Goldbach problem “with coeﬃcients”

In this section we discuss the solubility of equations of the form (1.16), which we intro-
duced in §1.4 as a natural generalization of the Waring–Goldbach problem. There are two
substantially diﬀerent contexts in which one can study this problem. Suppose ﬁrst that
all a1, . . . , as, n are all of the same sign. Then one expects that (1.16) must have solutions
for suﬃciently large |n|. When “suﬃciently large” is understood as |n| ≥ C(a1, . . . , as),
with some unspeciﬁed constant depending on the aj’s, this is a trivial modiﬁcation of the
Waring–Goldbach problem (that can be handled using essentially the same tools). On
the other hand, the problem of ﬁnding solution when |n| is not too large compared to
|a|∞ = max{|a1|, . . . , |as|} is signiﬁcantly more challanging. Similarly, if a1, . . . , as are not
all of the same sign, one wants to ﬁnd solutions of (1.16) in primes p1, . . . , ps that are not
too large compared to |a|∞ and |n|. Such questions were investigated ﬁrst by Baker [5], who
studied the case k = 1 and s = 3. Later, Liu and Tsang [161] showed, again for k = 1 and
s = 3, that (1.16) has solutions when:

• a1, a2, a3 are of the same sign and |n| ≫ |a|A
∞ for some absolute constant A > 0;

• a1, a2, a3 are not of the same sign and max{p1, p2, p3} ≪ |a|A−1
∞ + |n|.

In these results, the coeﬃcients a1, a2, a3, n must satisfy also certain necessary congruence
conditions (which generalize the requirement that n be odd in Vinogradov’s three primes
theorem). Through the eﬀorts of several mathematicians, the constant A has been evaluated
and it is known that the value A = 38 is admissible (see Li [139]). Furthermore, if we replace
the natural arithmetic conditions on the coeﬃcients by another set of conditions, which are
somewhat more restrictive but also simplify greatly the analysis, we can decrease the value
of A further. In particular, Choi and Kumchev [38] have shown that A = 23/3 is admissible
under such stronger hypotheses.
Liu and Tsang [162] studied also the quadratic case of (1.16) in ﬁve variables and obtained
results similar to those stated above for the linear case. In this problem, explicit values of
the analogue of A above were given by Choi and Liu [39, 40], Choi and Kumchev [37], and
Harman and Kumchev [80]. In particular, it is proved in [80] that (1.16) with k = 2 and
s = 5 has solutions when:

• a1, . . . , a5 are of the same sign and |n| ≫ |a|15+ε
∞ ;

• a1, . . . , a5 are not of the same sign and max{p1, . . . , p5} ≪ |a|7+ε
∞ + |n|1/2.

5.7 Diophantine inequalities with primes

Some variants of the Waring–Goldbach problem are stated most naturally in terms of dio-
phantine inequalities. The best-known problem of this kind concerns the distribution of the
values of the forms
 λ1pk
1 + · · · + λspk
s ,(5.5)

where k and s are positive integers, λ1, . . . , λs are nonzero real numbers, and p1, . . . , ps are
prime variables. It is natural to conjecture that if λ1, . . . , λs are not all of the same sign

43

and if λi/λj is irrational for some pair of indices i, j, then the values attained by the form
(5.5) are dense in R whenever s ≥ s0(k). In other words, given any ε > 0 and α ∈ R, the
inequality ∣
∣λ1pk
1 + · · · + λspk
s − α∣
∣ < ε(5.6)

should have a solution in primes p1, . . . , ps. The ﬁrst results in this problem were obtained
by Schwarz [203], who established the solvability of (5.6) under the same restrictions on
s as in Theorem 3. Baker [5] and Vaughan [221, 222, 224] proposed the more diﬃcult
problem of replacing the ﬁxed number ε on the right side of (5.6) by an explicit function
of max{p1, . . . , ps} that approaches 0 as max{p1, . . . , ps} → ∞. Further work has focused
primarily on the case of small k. For example, Harman [78] has shown that under the above
assumptions on λ1, λ2, λ3, the diophantine inequality
∣
∣λ1p1 + λ2p2 + λ3p3 − α∣
∣ < max{p1, p2, p3}−1/5+ε

has inﬁnitely many solutions in primes p1, p2, p3. Baker and Harman [6] showed that on
GRH the exponent 1
5 in this result can be replaced by 1
4. Furthermore, Harman [77] proved
that if λ1/λ2 is a negative irrational number, then for any real α the inequality
∣
∣λ1p + λ2P3 − α∣
∣ < p−1/300

has inﬁnitely many solutions in a prime p and a P3-almost prime. (This improves on an
earlier result of Vaughan [224], where the almost prime is a P4-number.)
In 1952 Piatetski-Shapiro [184] considered a variant of the Waring–Goldbach problem for
non-integer exponents c > 1. He showed that for any ﬁxed c > 1, which is not an integer,
there exists an integer H(c) with the following property: if s ≥ H(c), the inequality
∣
∣pc
1 + · · · + pc
s − α∣
∣ < ε(5.7)

has solutions in primes p1, . . . , ps for any ﬁxed ε > 0 and α ≥ α0(ε, c). In particular,
Piatetski-Shapiro showed that H(c) ≤ 5 for 1 < c < 3/2. Motivated by Vinogradov’s three
prime theorem, Tolev [213] proved that H(c) ≤ 3 for 1 < c < 15/14. The range of validity of
Tolev’s result was subsequently extended by several authors [32, 33, 125, 130]; in particular,
Kumchev [125] has given the range 1 < c < 61/55. Furthemore, it follows from the work
of Kumchev and Laporta [129, 133] that H(c) ≤ 4 for 1 < c < 6/5 and for almost all (in
the sense of Lebesgue measure) 1 < c < 2, while Garaev [61] has showed that H(c) ≤ 5 for
1 < c < (1 + √
5)/2 = 1.61 . . . . Finally, Tolev [214] and Zhai [253] have studied systems of
inequalities of the form (5.7).
Several authors [1, 2, 30, 31] have studied variants of Goldbach’s problem, suggested by
results about additive inequalities. For example, Arkhipov, Chen, and Chubarikov [2] proved
that if λ1/λ2 is an algebraic irrationality, then all but O(x
2/3+ε) positive integers n ≤ x can
be represented in the form
 [λ1p1] + [λ2p2] = n,

where p1, p2 are primes.
 44

6 A new path: arithmetic progressions of
primes

Finally, we should say a few words about the astonishing result of Green and Tao [64] on
the existence of arbitrarily long arithmetic progressions of prime numbers. They deduce the
existence of such arithmetic progressions from a generalization of a celebrated theorem of
Szemer´edi [209, 210], which is itself a deep result in combinatorial number theory. Let A be
a set of positive integers with positive upper density, that is,

δ(A) = lim sup
N →∞ #{n ∈ A : n ≤ N}
N > 0.

In its original, most basic form, Szemer´edi’s theorem asserts that such a set A contains an
arithmetic progression of length k for all integers k ≥ 3. From this basic statement, Green
and Tao deduce the following more general result.

Theorem 9 (Szemer´edi’s theorem for pseudorandom measures). Let δ ∈ (0, 1] be a
ﬁxed real number, let k ≥ 3 be a ﬁxed integer, and let N be a large prime. Suppose that ν is a
“k-pseudorandom measure8” on ZN = (Z/NZ) and f : ZN → [0, ∞) is a function satisfying

0 ≤ f (x) ≤ ν(x) for all x ∈ ZN(6.1)

and ∑

x∈ZN f (x) ≥ δN.

Then ∑

x∈ZN
 ∑

r∈ZN f (x)f (x + r) . . . f (x + (k − 1)r) ≫ N 2,(6.2)

the implied constant depending at most on δ and k.

To relate this result to the version of Szemer´edi’s theorem stated earlier, consider the case
where ν(x) = 1 for all x (this is a k-pseudorandom measure) and f (x) is the characteristic
function of the set AN = A ∩ [1, N] considered as a subset of ZN . Then the left side of (6.2)
counts (essentially) the k-term arithmetic progressions in the set AN (the majority of which
are also k-term arithmetic progressions in A ∩ Z).
To derive the result on arithmetic progressions of primes, Green and Tao take f (x) to be a
function which, in some sense (see [64] for details), approximates the characteristic function
of the primes in the interval [c1N, c2N], where 0 < c1 < c2 < 1 are suitable constants.
Then they construct a pseudorandom measure ν(x) such that (6.1) holds. This leads to the
following theorem.

8A k-pseudorandom measure on ZN is a non-negative function on ZN whose average over ZN is close to
1 and which is subject to a couple of additional constraints that are too technical to state here. See [64] for
details.
 45

Theorem 10 (Green and Tao, 2004). Let k ≥ 3 and let A be a set of prime numbers
such that
 lim sup
N →∞ #{n ∈ A : n ≤ N}
π(N) > 0.

Then A contains inﬁnitely many k-term arithmetic progresions. In particular, there are
inﬁnitely many k-term arithmetic progresions of prime numbers.

We remark that the inﬁnitude of the k-term progressions of primes is a consequence of
(6.2). In fact, using the explicit form of the function f (x) to which they apply Theorem
9, Green and Tao establish the existence of ≫ N 2(log N)−k k-term progressions within
A ∩ [1, N].
Several other interesing results are announced in [64]. For example, one of them asserts
that there are inﬁnitely many progressions of primes p1, . . . , pk such that each pi + 2 is a
P2-number (a proof of this result in the case k = 3 is presented in [65]).

Conclusion. With this, our survey comes to a close. We tried to describe the central problems
and the main directions of research in the additive theory of prime numbers and to introduce
the reader to the classical methods. Complete success in such an undertaking is perhaps an
impossibility, but hopefully we have been able to paint a representative picture of the current
state of the subject and to motivate the reader to seek more information from the literature.
Maybe some of our readers will one day join the ranks of the number theorists trying to turn
the great conjectures mentioned above into beautiful theorems!

Acknowledgements. This paper was written while the ﬁrst author enjoyed the beneﬁts of
postdoctoral positions at the University of Toronto and at the University of Texas at Austin.
He would like to take this opportunity to express his gratitude to these institutions for their
support. The second author was supported by Plovdiv University Scientiﬁc Fund grant
03-MM-35. Last but not least, the authors would like to thank Professors J. Friedlander
and D.R. Heath-Brown for several valuable discussions over the years and for some useful
comments about the preliminary version of the survey.

References

[1] G. I. Arhipov, K. Buriev, and V. N. Chubarikov, On the exceptional set in the generalized binary
Goldbach problem, Dokl. Ross. Akad. Nauk 365 (1999), 151–153, in Russian.

[2] G. I. Arhipov, J. Y. Chen, and V. N. Chubarikov, On the cardinality of an exceptional set in a binary
additive problem of the Goldbach type, in “Proceedings of the Session in Analytic Number Theory and
Diophantine Equations”, Bonner Math. Schriften 360, Bonn, 2003.

[3] G. I. Arhipov and V. N. Chubarikov, On the number of summands in Vinogradov’s additive problem and
its generalizations, in “Modern Problems of Number Theory and its Applications: Current Problems”,
vol. 1, Moscow, 2002, pp. 5–38, in Russian.

[4] G. I. Arhipov, V. N. Chubarikov, and A. A. Karatsuba, Theory of Multiple Trigonometric Sums,
Nauka, 1987, in Russian.

[5] A. Baker, On some diophantine inequalities involving primes, J. Reine Angew. Math. 228 (1967),
166–181.
 46

[6] R. C. Baker and G. Harman, Diophantine approximation by prime numbers, J. London Math. Soc. (2)
25 (1982), 201–215.

[7] , The three primes theorem with almost equal summands, R. Soc. London Philos. Trans. Ser. A
356 (1998), 763–780.

[8] R. C. Baker, G. Harman, and J. Pintz, The exceptional set for Goldbach’s problem in short intervals, in
“Sieve Methods, Exponential Sums and their Applications in Number Theory”, Cambridge University
Press, 1997, pp. 1–54.

[9] , The diﬀerence between consecutive primes. II, Proc. London Math. Soc. (3) 83 (2001), 532–562.

[10] A. Balog, On the fractional parts of pθ, Arch. Math. (Basel) 40 (1983), 434–440.

[11] , Linear equations in primes, Mathematika 39 (1992), 367–378.

[12] A. Balog and J. B. Friedlander, A hybrid of theorems of Vinogradov and Piatetski-Shapiro, Paciﬁc J.
Math. 156 (1992), 45–62.

[13] C. Bauer, A note on sums of ﬁve almost equal prime squares, Arch. Math. (Basel) 69 (1997), 20–30.

[14] , On the sum of a prime and the kth power of a prime, Acta Arith. 85 (1998), 99–118.

[15] , On the exceptional set for the sum of a prime and the kth power of a prime, Studia Sci. Math.
Hungar. 35 (1999), 291–330.

[16] C. Bauer, M. C. Liu, and T. Zhan, On a sum of three prime squares, J. Number Theory 85 (2000),
336–359.

[17] V. Blomer and J. Br¨udern, A three squares theorem with almost primes, Bull. London Math. Soc., to
appear.

[18] K. D. Boklan, The asymptotic formula in Waring’s problem, Mathematika 41 (1994), 329–347.

[19] E. Bombieri, On the large sieve, Mathematika 12 (1965), 201–225.

[20] , Le grand crible dans le th´eorie analytique des nombres, Ast´erisque 18, Soci´et´e Math. France,
1974.

[21] , The asymptotic sieve, Rend. Accad. Naz. XL (5) 1/2 (1975/76), 243–269.

[22] J. Br¨udern, A sieve approach to the Waring–Goldbach problem. I. Sums of four cubes, Ann. Sci. ´Ecole
Norm. Sup. (4) 28 (1995), 461–476.

[23] , A sieve approach to the Waring–Goldbach problem. II. On the seven cubes theorem, Acta Arith.
72 (1995), 211–227.

[24] J. Br¨udern and E. Fouvry, Lagrange’s four squares theorem with almost prime variables, J. Reine
Angew. Math. 454 (1994), 59–96.

[25] J. Br¨udern and K. Kawada, Ternary problems in additive prime number theory, in “Analytic Number
Theory”, Kluwer Acad. Publ., 2002, pp. 39–91.

[26] J. Br¨udern and A. Perelli, The addition of primes and powers, Canad. J. Math. 48 (1996), 512–526.

[27] V. Brun, Le crible d’Eratost`ene et la th´eor`eme de Goldbach, C. R. Acad. Sci. Paris 168 (1919), 544–546.

[28] R. Br¨unner, A. Perelli, and J. Pintz The exceptional set for the sum of a prime and a square, Acta
Math. Hungar. 53 (1989), 347–365.

[29] A. A. Buchstab, Combinatorial intensiﬁcation of the sieve method of Eratosthenes, Uspehi Mat. Nauk
22 (1967), 205–233, in Russian.

[30] K. Buriev, An additive problem with prime numbers, Dokl. Akad. Nauk Tadzh. SSR 30 (1987), 686–688,
in Russian.
 47

[31] , An exceptional set in the Hardy–Littlewood problem for nonintegral powers, Mat. Zametki 46
(1989), 127–128, in Russian.

[32] Y. C. Cai, On a diophantine inequality involving prime numbers, Acta Math. Sinica 39 (1996), 733–742,
in Chinese.

[33] , On a diophantine inequality involving prime numbers. III, Acta Math. Sinica (N.S.) 15 (1999),
387–394.

[34] J. R. Chen, On large odd numbers as sum of three almost equal primes, Sci. Sinica 14 (1965), 1113–
1117.

[35] , On the representation of large even integer as the sum of a prime and the product of at most
two primes, Sci. Sinica 16 (1973), 157–176.

[36] J. R. Chen and C. D. Pan, The exceptional set of Goldbach numbers, Sci. Sinica 23 (1980), 416–430.

[37] K. K. Choi and A. V. Kumchev, Quadratic equations with ﬁve prime unknowns, J. Number Theory
107 (2004), 357–367.

[38] , Mean values of Dirichlet polynomials and applications to linear equations with prime variables,
preprint.

[39] K. K. Choi and J. Y. Liu, Small prime solutions of quadratic equations, Canad. J. Math. 54 (2002),
71–91.

[40] , Small prime solutions of quadratic equations. II, Proc. Amer. Math. Soc., to appear.

[41] V. N. Chubarikov, On simultaneous representation of natural numbers by sums of powers of prime
numbers, Dokl. Akad. Nauk SSSR 286 (1986), 828–831, in Russian.

[42] N. G. Chudakov, On the density of the sets of even integers which are not representable as a sum of
two odd primes, Izv. Akad. Nauk SSSR Ser. Mat. 2 (1938), 25–40, in Russian.

[43] J. G. van der Corput, Sur l’hypoth`ese de Goldbach, Proc. Akad. Wet. Amsterdam 41 (1938), 76–80.

[44] H. Cram´er, Some theorems concerning prime numbers, Arkiv f¨or Mat. Astronom. och Fysik 15 (1920),
1–32.

[45] , On the order of magnitude of the diﬀerence between consecutive primes, Acta Arith. 2 (1937),
23–46.

[46] H. Davenport, On sums of positive integral kth powers, Proc. R. Soc. London Ser. A 170 (1939),
293–299.

[47] , On Waring’s problem for fourth powers, Ann. of Math. (2) 40 (1939), 731–747.

[48] , On sums of positive integral kth powers, Amer. J. Math. 64 (1942), 189–198.

[49] , Multiplicative Number Theory, Third ed. revised by H. L. Montgomery, Springer-Verlag, 2000.

[50] H. Davenport and P. Erd¨os, On sums of positive integral kth powers, Ann. of Math. (2) 40 (1939),
533–536.

[51] J.-M. Deshouillers, G. Eﬃnger, H. te Riele, and D. Zinoviev, A complete Vinogradov 3-primes the-
orem under the Riemann hypothesis, Electron. Res. Announc. Amer. Math. Soc. 3 (1997), 99–104,
(electronic).

[52] G. Dufner, Bin¨ares Goldbachproblem in kursen Intervallen. I. Die explizite Formel, Period. Math.
Hungar. 29 (1994), 213–243.

[53] , Bin¨ares Goldbachproblem in kursen Intervallen. II, Period. Math. Hungar. 30 (1995), 37–60.

[54] T. Estermann, On Goldbach’s problem: Proof that almost all even positive integers are sums of two
primes, Proc. London Math. Soc. (2) 44 (1938), 307–314.

48

[55] , On Kloosterman’s sum, Mathematika 8 (1961), 83–86.

[56] , A new application of the Hardy–Littlewood–Kloosterman method,

Proc. London Math. Soc. (3) 12 (1962), 425–444.

[57] K. B. Ford, New estimates for mean values of Weyl sums, Internat. Math. Res. Notices (1995), 155–171.

[58] J. B. Friedlander and H. Iwaniec, The polynomial X 2 + Y 4 captures its primes, Ann. of Math. (2) 148
(1998), 963–1040.

[59] , Asymptotic sieve for primes, Ann. of Math. (2) 148 (1998), 1041–1065.

[60] P. X. Gallagher, Primes and powers of 2, Invent. Math. 29 (1975), 125–142.

[61] M. Z. Garaev, On the Waring–Goldbach problem with small noninteger exponents, Acta Arith. 108
(2003), 297–302.

[62] G. Greaves, On the representation of a number in the form x
2 + y2 + p2 + q2 where p and q are odd
primes, Acta Arith. 29 (1976), 257–274.

[63] , Sieves in Number Theory, Springer-Verlag, 2001.

[64] B. Green and T. Tao, The primes contain arbitrarily long arithmetic progressions, preprint.

[65] , Restriction theory of Selberg’s sieve, with applications, preprint.

[66] H. Halberstam and H. E. Richert, Sieve Methods, Academic Press, 1974.

[67] G. H. Hardy and J. E. Littlewood, A new solution of Waring’s problem, Quart. J. Math. Oxford 48
(1919), 272–293.

[68] , Some problems of “Partitio Numerorum”. I. A new solution of Waring’s problem, G¨ottingen
Nach. (1920), 33–54.

[69] , Some problems of “Partitio Numerorum”. III. On the expression of a number as a sum of primes,
Acta Math. 44 (1923), 1–70.

[70] , Some problems of “Partitio Numerorum”. IV. The singular series in Waring’s problem and the
value of the number G(k), Math. Z. 12 (1922), 161–188.

[71] , Some problems of “Partitio Numerorum”. V. A further contribution to the study of Goldbach’s
problem, Proc. London Math. Soc. (2) 22 (1923), 46–56.

[72] , Some problems of “Partitio Numerorum”. VI. Further researches in Waring’s problem, Math.
Z. 23 (1925), 1–37.

[73] G. H. Hardy and S. Ramanujan, Asymptotic formulae in combinatory analysis, Proc. London Math.
Soc. (2) 17 (1918), 75–115.

[74] G. H. Hardy and E. M. Wright, An Introduction to the Theory of Numbers, Fifth ed., Oxford University
Press, 1979.

[75] G. Harman, Trigonometric sums over primes. I, Mathematika 28 (1981), 249–254.

[76] , On the distribution of √
p modulo one, Mathematika 30 (1983), 104–116.

[77] , Diophantine approximation with a prime and an almost–prime, J. London Math. Soc. (2) 29
(1984), 13–22.

[78] , Diophantine approximation by prime numbers, J. London Math. Soc. (2) 44 (1991), 218–226.

[79] , Eratosthenes, Legendre, Vinogradov and beyond (the hidden power of the simplest sieve), in
“Sieve Methods, Exponential Sums and their Applications in Number Theory”, Cambridge University
Press, 1997, pp. 161–173.
 49

[80] G. Harman and A. V. Kumchev, On sums of squares of primes, Math. Proc. Cambridge Philos. Soc.,
to appear.

[81] G. Harman and P. A. Lewis, Gaussian primes in narrow sectors, Mathematika 48 (2001), 119–135.

[82] C. B. Haselgrove, Some theorems in the analytic theory of numbers, J. London Math. Soc. 26 (1951),
273–277.

[83] D. R. Heath-Brown, Three primes and an almost-prime in arithmetic progression, J. London Math.
Soc. (2) 23 (1981), 396–414.

[84] , Prime numbers in short intervals and a generalized Vaughan identity, Canad. J. Math. 34 (1982),
1365–1377.

[85] , Cubic forms in ten variables, Proc. London Math. Soc. (3) 47 (1983), 225–257.

[86] , The number of primes in a short interval, J. Reine Angew. Math. 389 (1988), 22–63.

[87] , A new form of the circle method, and its application to quadratic forms, J. Reine Angew. Math.
481 (1996), 149–206.

[88] , The circle method and diagonal cubic forms, R. Soc. London Philos. Trans. Ser. A 356 (1998),
673–699.

[89] , Primes represented by x
3 + 2y3, Acta Math. 186 (2001), 1–84.

[90] , Lectures on sieves, in “Proceedings of the Session in Analytic Number Theory and Diophantine
Equations”, Bonner Math. Schriften 360, Bonn, 2003.

[91] D. R. Heath-Brown and H. Iwaniec, On the diﬀerence between consecutive primes, Invent. Math. 55
(1979), 49–69.

[92] D. R. Heath-Brown and B. Z. Moroz, Primes represented by binary cubic forms, Proc. London Math.
Soc. (3) 84 (2002), 257–288.

[93] D. R. Heath-Brown and J.-C. Puchta, Integers represented as a sum of primes and powers of two,
Asian J. Math. 6 (2002), 535–565.

[94] D. R. Heath-Brown and D. I. Tolev, Lagrange’s four squares theorem with one prime and three almost-
prime variables, J. Reine Angew. Math. 558 (2003), 159–224.

[95] D. Hilbert, Beweis f¨ur die Darstellbarkeit der ganzen Zahlen durch eine feste Anzahl nter Potenzen
(Waringsche Problem), Math. Ann. 67 (1909), 281–300.

[96] G. Hoheisel, Primzahlprobleme in der Analysis, Sitz. Preuss. Akas. Wiss. 2 (1930), 1–13.

[97] C. Hooley, On the representation of a number as the sum of two squares and a prime, Acta Math. 97
(1957), 189–210.

[98] , Applications of Sieve Methods to the Theory of Numbers, Cambridge University Press, 1976.

[99] , On Waring’s problem, Acta Math. 157 (1986), 49–97.

[100] L. K. Hua, Some results in the additive prime number theory, Quart. J. Math. Oxford 9 (1938), 68–80.

[101] , An improvement of Vinogradov’s mean-value theorem and several applications, Quart. J. Math.
Oxford 20 (1949), 48–61.

[102] , Additive Theory of Prime Numbers, American Mathematical Society, 1965.

[103] A. Ivic, The Riemann Zeta-function, John Wiley & Sons, 1985.

[104] H. Iwaniec, Almost-primes represented by quadratic polynomials, Invent. Math. 47 (1978), 171–188.

[105] , Rosser’s sieve, Acta Arith. 36 (1980), 171–202.

[106] , A new form of the error term in the linear sieve, Acta Arith. 37 (1980), 307–320.

50

[107] H. Iwaniec and M. Jutila, Primes in short intervals, Ark. Mat. 17 (1979), 167–176.

[108] H. Iwaniec and E. Kowalski, Analytic Number Theory, American Mathematical Society, 2004.

[109] C. H. Jia, The three primes theorem over short intervals, Acta Math. Sinica 32 (1989), 464–473, in
Chinese.

[110] , Three primes theorem in a short interval. VII, Acta Math. Sinica (N.S.) 10 (1994), 369–387.

[111] , Goldbach numbers in a short interval. I, Sci. China Ser. A 38 (1995), 385–406.

[112] , Goldbach numbers in a short interval. II, Sci. China Ser. A 38 (1995), 513–523.

[113] , On the Piatetski-Shapiro–Vinogradov theorem, Acta Arith. 73 (1995), 1–28.

[114] , Almost all short intervals containing prime numbers, Acta Arith. 76 (1996), 21–84.

[115] , On the exceptional set of Goldbach numbers in a short interval, Acta Arith. 77 (1996), 207–287.

[116] A. A. Karatsuba, Basic Analytic Number Theory, translated from the second Russian edition, Springer-
Verlag, 1993.

[117] A. A. Karatsuba and S. M. Voronin, The Riemann Zeta-function, Walter de Gruyter, 1992.

[118] K. Kawada, Note on the sum of cubes of primes and an almost prime, Arch. Math. (Basel) 69 (1997),
13–19.

[119] , On sums of seven cubes of almost primes, preprint.

[120] K. Kawada and T. D. Wooley, Sums of fourth powers and related topics, J. Reine Angew. Math. 512
(1999), 173–223.

[121] , On the Waring–Goldbach problem for fourth and ﬁfth powers, Proc. London Math. Soc. (3) 83
(2001), 1–50.

[122] H. D. Kloosterman, On the representation of numbers in the form ax
2 + by2 + cz2 + dt2, Acta Math.
49 (1926), 407–464.

[123] N. M. Korobov, Estimates of trigonometric sums and their applications, Uspehi Mat. Nauk 13 (1958),
185–192, in Russian.

[124] P. Kuhn, Zur Viggo Brun’schen Siebmethode. I, Norske Vid. Selsk. Forh. Trondhjem 14 (1941), 145–
148.

[125] A. V. Kumchev, A diophantine inequality involving prime powers, Acta Arith. 89 (1999), 311–330.

[126] , On the Waring–Goldbach problem: Exceptional sets for sums of cubes and higher powers, Canad.
J. Math., to appear.

[127] , On the Waring–Goldbach problem for seventh powers, Proc. Amer. Math. Soc., to appear.

[128] , On Weyl sums over primes and almost primes, preprint.

[129] A. V. Kumchev and M. B. S. Laporta, On a binary diophantine inequality involving prime powers, in
“Number Theory for the Millennium”, vol. 2, AK Peters, 2002, pp. 307–329.

[130] A. V. Kumchev and T. Nedeva, On an equation with prime numbers, Acta Arith. 83 (1998), 117–126.

[131] A. Languasco, On the exceptional set of Goldbach’s problem in short intervals, Monatsh. Math. 141
(2004), 147–169.

[132] , On the exceptional set of Hardy–Littlewood’s numbers in short intervals, Tsukuba J. Math. 28
(2004), 169–191.

[133] M. B. S. Laporta, On a binary diophantine inequality involving prime numbers, Acta Math. Hungar.
83 (1999), 179–187.
 51

[134] M. C. Leung and M. C. Liu, On generalized quadratic equations in three prime variables, Monatsh.
Math. 115 (1993), 133–169.

[135] H. Z. Li, Goldbach numbers in short intervals, Sci. China Ser. A 38 (1995), 641–652.

[136] , The exceptional set of Goldbach numbers. II, Acta Arith. 92 (2000), 71–88.

[137] , The number of powers of 2 in representation of large even integers by sums of such powers and
of two primes, Acta Arith. 92 (2000), 229–237.

[138] , The number of powers of 2 in representation of large even integers by sums of such powers and
of two primes. II, Acta Arith. 96 (2001), 369–379.

[139] , Small prime solutions of linear ternary equations, Acta Arith. 98 (2001), 293–309.

[140] Yu. V. Linnik, The large sieve, Dokl. Akad. Nauk SSSR 30 (1941), 292–294, in Russian.

[141] , On the representation of large numbers as sums of seven cubes, Mat. Sbornik N.S. 12 (1943),
218–224, in Russian.

[142] , Prime numbers with powers of two, Trudy Mat. Inst. Steklov 38 (1951), 152–169, in Russian.

[143] , Some conditional theorems concerning the binary Goldbach problem, Izv. Akad. Nauk SSSR Ser.
Mat. 16 (1952), 503–520, in Russian.

[144] , Addition of prime numbers with powers of one and the same number, Mat. Sbornik N.S. 32
(1953), 3–60, in Russian.

[145] , An asymptotic formula in the Hardy–Littlewood additive problem, Izv. Akad. Nauk SSSR Ser.
Mat. 24 (1960), 629–706.

[146] , The Dispersion Method in Binary Additive Problems, American Mathematical Society, 1963.

[147] J. Y. Liu, On Lagrange’s theorem with prime variables, Quart. J. Math. Oxford (2) 54 (2003), 453–462.

[148] J. Y. Liu and M. C. Liu, Representations of even integers as sums of squares of primes and powers of
2, J. Number Theory 83 (2000), 202–225.

[149] , The exceptional set in the four prime squares problem, Illinois J. Math. 44 (2000), 272–293.

[150] J. Y. Liu, M. C. Liu, and T. Wang, The number of powers of 2 in an representation of large even
integers. I, Sci. China Ser. A 41 (1998), 386–398.

[151] , The number of powers of 2 in an representation of large even integers. II, Sci. China Ser. A 41
(1998), 1255–1271.

[152] , On the almost Goldbach problem of Linnik, J. Th´eor. Nombres Bordeaux 11 (1999), 133–147.

[153] J. Y. Liu, M. C. Liu, and T. Zhan, Squares of primes and powers of 2, Monatsh. Math. 128 (1999),
283–313.

[154] , Squares of primes and powers of 2. II, J. Number Theory 92 (2002), 99–116.

[155] J. Y. Liu, T. D. Wooley, and G. Yu, The quadratic Waring–Goldbach problem, J. Number Theory 107
(2004), 298–321.

[156] J. Y. Liu and T. Zhan, On sums of ﬁve almost equal prime squares, Acta Arith. 77 (1996), 369–383.

[157] , On a theorem of Hua, Arch. Math. (Basel) 69 (1997), 375–390.

[158] , Hua’s theorem on prime squares in short intervals, Acta Math. Sinica (N.S.) 16 (2000), 669–690.

[159] , Distribution of integers that are sums of three squares of primes, Acta Arith. 98 (2001), 207–228.

[160] , An iterative method in the Waring–Goldbach problem, preprint.

[161] M. C. Liu and K. M. Tsang, Small prime solutions of some additive equations, Monatsh. Math. 111
(1991), 147–169.
 52

[162] , Small prime solutions of linear equations, in “Th´eorie de nombres”, Walter de Gruyter, 1989,
pp. 595–624.

[163] M. C. Liu and T. Z. Wang, On the Vinogradov bound in the three primes Goldbach conjecture, Acta
Arith. 105 (2002), 133-175.

[164] S. T. Lou and Q. Yao, The exceptional set of Goldbach numbers in a short interval, Acta Math. Sinica
24 (1981), 269–282, in Chinese.

[165] H. Maier, Small diﬀerences between prime numbers, Michigan Math. J. 35 (1988), 323–344.

[166] R. J. Miech, On the equation n = p + x
2, Trans. Amer. Math. Soc. 130 (1968), 494–512.

[167] H. Mikawa, On the exceptional set in Goldbach’s problem, Tsukuba J. Math. 16 (1992), 513–543.

[168] , On the sum of a prime and a square, Tsukuba J. Math. 17 (1993), 299–310.

[169] , On the sum of three squares of primes, in “Analytic Number Theory”, Cambridge University
Press, 1997, pp. 253–264.

[170] D. A. Mitkin, The number of terms in the Hilbert-Kamke problem in prime numbers, Diskret. Mat. 4
(1992), 149–158, in Russian.

[171] H. L. Montgomery, Topics in Multiplicative Number Theory, Springer–Verlag, 1971.

[172] , The analytic principal of the large sieve, Bull. Amer. Math. Soc. 84 (1978), 547–567.

[173] H. L. Montgomery and R. C. Vaughan, The exceptional set in Goldbach’s problem, Acta Arith. 27
(1975), 353–370.

[174] Y. Motohashi, Sieve Methods and Prime Number Theory, Tata Institute for Fundamental Research,
1983.

[175] M. B. Nathanson, Additive Number Theory. The Classical Bases, Springer-Verlag, 1996.

[176] A. Page, On the number of primes in an arithmetic progression, Proc. London Math. Soc. (2) 39
(1935), 116–141.

[177] C. B. Pan and C. D. Pan, On estimations of trigonometric sums over primes in short intervals. II,
Sci. China Ser. A 32 (1989), 641–653.

[178] , Goldbach Conjecture, Science Press, 1992.

[179] T. P. Peneva, On the ternary Goldbach problem with primes pi such that pi + 2 are almost-prime, Acta
Math. Hungar. 86 (2000), 305–318.

[180] , On the exceptional set for Goldbach’s problem in short intervals, Monatsh. Math. 132 (2001),
49–65; Corrigendum: ibid. 141 (2004), 209–217.

[181] , An additive problem with Piatetski-Shapiro primes and almost-primes, Monatsh. Math. 140
(2003), 119–133.

[182] A. Perelli and J. Pintz, On the exceptional set for Goldbach’s problem in short intervals, J. London
Math. Soc. (2) 47 (1993), 41–49.

[183] A. Perelli and A. Zaccagnini, On the sum of a prime and a k–th power, Izv. Ross. Akad Nauk Ser.
Math. 59 (1995), 185–200.

[184] I. I. Piatetski-Shapiro, On a variant of Waring–Goldbach’s problem, Mat. Sbornik N.S. 30 (1952),
105–120, in Russian.

[185] , On the distribution of prime numbers in sequences of the form [f (n)], Mat. Sbornik N.S. 33
(1953), 559–566, in Russian.

[186] J. Pintz, Explicit formulas and the exceptional set in Goldbach’s problem, lecture at the CNTA VIII
meeting in Toronto, June 20–25, 2004.
 53

[187] J. Pintz and I. Z. Ruzsa, On Linnik’s approximation to Goldbach’s problem. I, Acta Arith. 109 (2003),
169–194.

[188] , On Linnik’s approximation to Goldbach’s problem. II, preprint.

[189] V. A. Plaksin, An asymptotic formula for the number of solutions of an equation with primes, Izv.
Akad. Nauk SSSR Ser. Math. 45 (1981), 321–397, in Russian.

[190] I. V. Polyakov, Addition of a prime number and the square of an integer, Mat. Zametki 47 (1990),
90–99, in Russian.

[191] K. Prachar, Primzahlverteilung, Springer–Verlag, 1957.

[192] K. Ramachandra, On the number of Goldbach numbers in small intervals, J. Indian Math. Soc. (N.S.)
37 (1973), 157–170.

[193] O. Ramar´e, On Snirel’man’s constant, Ann. Scuola Norm. Sup. Pisa (4) 22 (1995), 645–706.

[194] X. Ren, The Waring–Goldbach problem for cubes, Acta Arith. 94 (2000), 287–301.

[195] A. R´enyi, On the representation of an even number as the sum of a single prime and a single almost-
prime number, Dokl. Akad. Nauk SSSR 56 (1947), 455–458, in Russian.

[196] H.-E. Richert, Selberg’s sieve with weights, Mathematika 16 (1969), 1-22.

[197] G. F. B. Riemann, ¨Uber die Anzahl der Primzahlen unter einer gegebenen Gr¨osse, Monatsber. Berliner
Akad., 1859.

[198] J. Rivat and P. Sargos, Nombres premiers de la forme ⌊nc⌋, Canad. J. Math. 53 (2001), 414–433.

[199] J. Rivat and J. Wu, Prime numbers of the form [nc], Glasgow Math. J. 43 (2001), 237–254.

[200] K. F. Roth, On Waring’s problem for cubes, Proc. London Math, Soc. (2) 53 (1951), 268–279.

[201] L. G. Schnirelmann, ¨Uber additive Eigenschaften von Zahlen, Math. Ann. 107 (1932/33), 649–690.

[202] W. Schwarz, Zur Darstellun von Zahlen durch Summen von Primzahlpotenzen, J. Reine Angew. Math.
206 (1961), 78–112.

[203] , ¨Uber die L¨osbarkeit gewisser Ungleichungen durch Primzahlen, J. Reine Angew. Math. 212
(1963), 150–157.

[204] A. Selberg, On an elementary method in the theory of primes, Norske Vid. Selsk. Forh. Trondhjem 19
(1947), 64–67.

[205] , Collected Papers, vol. 1, Springer-Verlag, 1989.

[206] , Collected Papers, vol. 2, Springer-Verlag, 1991.

[207] P. Shields, Some applications of the sieve methods in number theory, Ph.D. thesis, University of Wales,
1979.

[208] C. L. Siegel, ¨Uber die Classenzahl quadratischer K¨orper, Acta Arith. 1 (1935), 83–86.

[209] E. Szemer´edi, On sets of integers containing no four elements in arithmetic progression, Acta Math.
Acad. Sci. Hungar. 20 (1969), 89–104.

[210] , On sets of integers containing no k elements in arithmetic progression, Acta Arith. 27 (1975),
299–345.

[211] K. Thanigasalam, Improvement on Davenport’s iterative method and new results in additive number
theory. III, Acta Arith. 48 (1987), 97–116.

[212] E. C. Titchmarsh, The Theory of the Riemann Zeta-function, Second ed. revised by D. R. Heath-
Brown, Oxford University Press, 1986.

[213] D. I. Tolev, On a diophantine inequality involving prime numbers, Acta Arith. 61 (1992), 289–306.

54

[214] , On a system of two diophantine inequalities with prime numbers, Acta Arith. 69 (1995), 387–400.

[215] , Arithmetic progressions of prime–almost-prime twins, Acta Arith. 88 (1999), 67–98.

[216] , Additive problems with prime numbers of special type, Acta Arith. 96 (2000), 53–88; Corrigen-
dum: ibid. 105 (2002), 205.

[217] , Representations of large integers as sums of two primes of special type, in “Algebraic Number
Theory and Diophantine Analysis”, Walter de Gruyter, 2000, pp. 485–495.

[218] , Lagrange’s four squares theorem with variables of special type, in “Proceedings of the Session in
Analytic Number Theory and Diophantine Equations”, Bonner Math. Schriften 360, Bonn, 2003.

[219] , On the exceptional set of Lagrange’s equation with three prime and one almost-prime variables,
preprint.

[220] R. C. Vaughan, On Goldbach’s problem, Acta Arith. 22 (1972), 21–48.

[221] , Diophantine approximation by prime numbers. I, Proc. London Math. Soc. (3) 28 (1974), 373–
384.

[222] , Diophantine approximation by prime numbers. II, Proc. London Math. Soc. (3) 28 (1974),
385–401.

[223] , Mean value theorems in prime number theory, J. London Math. Soc. (2) 10 (1975), 153–162.

[224] , Diophantine approximation by prime numbers. III, Proc. London Math. Soc. (3) 33 (1976),
177–192.

[225] , Sommes trigonom´etriques sure les nombres premiers, C. R. Acad. Sci. Paris S´er. A 285 (1977),
981–983.

[226] , On Waring’s problem for cubes, J. Reine Angew. Math. 365 (1986), 122–170.

[227] , On Waring’s problem for smaller exponents. II, Mathematika 33 (1986), 6–22.

[228] , The Hardy–Littlewood Method, Second ed., Cambridge University Press, 1997.

[229] R. C. Vaughan and T. D. Wooley, Further improvements in Waring’s problem, Acta Math. 174 (1995),
147–240.

[230] , Further improvements in Waring’s problem. II. Sixth powers, Duke Math. J. 76 (1994), 683–710.

[231] , Further improvements in Waring’s problem. III. Eighth powers, Roy. Soc. London Philos. Trans.
Ser. A 345 (1993), 385–396.

[232] , Further improvements in Waring’s problem. IV. Higher powers, Acta Arith. 94 (2000), 203–285.

[233] , Waring’s problem: a survey, in “Number Theory for the Millennium”, vol. 3, AK Peters, 2002,
pp. 301–340.

[234] A. I. Vinogradov, The density hypothesis for Dirichlet L-series, Izv. Akad. Nauk SSSR Ser. Mat. 29
(1965), 903–934; Corrigendum: ibid. 30 (1966), 719–720, in Russian.

[235] , The binary Hardy–Littlewood problem, Acta Arith. 46 (1985), 33–56, in Russian.

[236] I. M. Vinogradov, Representation of an odd number as the sum of three primes, Dokl. Akad. Nauk
SSSR 15 (1937), 291–294, in Russian.

[237] , Some theorems concerning the theory of primes, Mat. Sbornik N.S. 2 (1937), 179–195, in Russian.

[238] , The Method of Trigonometrical Sums in the Theory of Numbers, Trudy Mat. Inst. Steklov 23
(1947), in Russian.

[239] , A new estimate for ζ(1 + it), Izv. Akad. Nauk SSSR Ser. Mat. 22 (1958), 161–164, in Russian.

[240] , On an upper bound for G(n), Izv. Akad. Nauk SSSR Ser. Mat. 23 (1959), 637–642, in Russian.

55

[241] , Special Variants of the Method of Trigonometric Sums, Nauka, 1976, in Russian.

[242] T. Z. Wang, On Linnik’s almost Goldbach theorem, Sci. China Ser. A 42 (1999), 1155–1172.

[243] A. Weil, On some exponential sums, Proc. Nat. Acad. Sci. U.S.A. 34 (1948), 204–207.

[244] E. Wirsing, Thin subbases, Analysis 6 (1986), 285–308.

[245] T. D. Wooley, Large improvements in Waring’s problem, Ann. of Math. (2) 135 (1992), 131–164.

[246] , On Vinogradov’s mean value theorem, Mathematika 39 (1992), 379–399.

[247] , New estimates for Weyl sums, Quart. J. Math. Oxford (2) 46 (1995), 119–127.

[248] , Slim exceptional sets for sums of cubes, Canad. J. Math. 54 (2002), 417–448.

[249] , Slim exceptional sets for sums of four squares, Proc. London Math. Soc. (3) 85 (2002), 1–21.

[250] Q. Yao, The exceptional set of Goldbach numbers in a short interval, Acta Math. Sinica 25 (1982),
315–322.

[251] A. Zaccagnini, On the exceptional set for the sum of a prime and kth power, Mathematika 39 (1992),
400–421.

[252] , A note on the sum of a prime and a polynomial, Quart. J. Math. Oxford (2) 52 (2001), 519–524.

[253] W. Zhai, On a system of two diophantine inequalities with prime numbers, Acta Arith. 92 (2000),
31–46.

[254] T. Zhan, On the representation of large odd integer as a sum of three almost equal primes, Acta Math.
Sinica (N.S.) 7 (1991), 259–272.

Department of Mathematics, 1 University Station, C1200, The University of Texas at
Austin, Austin, TX 78712, U.S.A.
E-mail: kumchev@math.utexas.edu

Department of Mathematics, Plovdiv University “P. Hilendarski”, 24 Tsar Asen Street,
Plovdiv 4000, Bulgaria
E-mail: dtolev@pu.acad.bg
 56
