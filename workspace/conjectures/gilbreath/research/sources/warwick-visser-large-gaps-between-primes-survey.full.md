<!-- source: https://warwick.ac.uk/fac/sci/maths/people/staff/visser/large_gaps_between_primes.pdf | converted from PDF -->

Large Gaps Between Primes

Robin Visser

Essay setter: Dr Thomas Bloom
Part III Essay, 2020

University of Cambridge

Contents

Abstract 1

Introduction 1
Lower bound history . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
Upper bound history . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3

Preliminaries 5
Rankin’s bound . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8

Heuristic results 13
Cram´er’s model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
Alternate models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16

Computational results 17
Computation of G(x) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
Computation of Y (x) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19

Main result 21
Hypergraph covering . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
Covering theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
Applying the covering theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
Finishing up . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49

Conclusion 53

Acknowledgements 54

References 55

Appendix 61
Probability . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
Elementary upper bounds for G(x) . . . . . . . . . . . . . . . . . . . . . . . . . . 63
Partial integration results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
Mertens’ theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
Calculation of a constant c . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66

i

Abstract
Let pn be the n-th prime, and deﬁne the maximal prime gap G(x) as

G(x) = max
pn≤x(pn+1 − pn).

We give a summary of the lower and upper bounds that have been obtained for G(x)
over the last century, as well as discuss some heuristic models and computational results
obtained for G(x). Finally, we provide an overview of the proof of a recent lower bound of
G(x) ≫ log x log2 x log4 x/ log3 x that Ford, Green, Konyagin, Maynard, and Tao obtained in
2014, whilst providing a detailed proof of their key new contribution, being a generalisation
of a hypergraph covering theorem by Pippenger and Spencer.

Introduction

Prime numbers have long been known to be fundamental in the study of number theory. Around
300BC, the Greek Mathematician Euclid was one of the ﬁrst to provide a treatise on prime num-
bers and proved several key facts about primes, including that there are inﬁnitely many such
prime numbers, as well as proving the well-known fundamental theorem of arithmetic. This
was all written up in his textbook, The Elements, in what is considered today to be one of the
most inﬂuential textbooks of all time [14]. Since then, mathematicians have long held a keen
interest in prime numbers, with the study of the distribution of primes being central to analytic
number theory.

Let pn denote the n-th prime number. For all x ≥ 2, we deﬁne G(x) as the maximal prime gap

G(x) = max
pn≤x(pn+1 − pn).

Since the early 20th century, many mathematicians have studied the growth rate of G(x) and
several results have been proven regarding the function. We shall ﬁrst give a short history of the
lower and upper bounds that have been proven for G(x) to date. We also consider some conjec-
tural results about the growth rate of G(x), as well as look at some recent computational results.

The main goal of this essay is to give an overview of the most recent lower bound obtained for
G(x). In 2014, Ford, Green, Konyagin, Maynard and Tao [30] showed that

G(x) ≫ log x log2 x log4 x
log3 x . (1)

We shall focus on proving the key new contribution given in [30] which is a generalisation of a
hypergraph covering theorem from Pippenger, Spencer [85]. This result is based on the R¨odl
nibble method from [91], and was eﬃciently used in [30], along with current estimates about
primes given in [69], to provide the quantitative improvement in the lower bound of G(x), as
given in (1).

As is standard convention, we shall use the notation logn x to mean the n-th iterated logarithm.
That is log1 x = log x and logn+1 x = log (logn x) for all n ≥ 1. We also make frequent use of
Vinogradov’s notation f ≪ g to mean f = O(g) and f ≫ g to mean g = O(f ).

Lower bound history

It has been classically known that G(x) → ∞ as x → ∞. Indeed, for any n ≥ 2, note that
n! + k is divisible for k and hence composite for all k ∈ {2, . . . , n}. This gives a sequence of
n − 1 consecutive composite numbers, which yields the tricial lower bound of

G(n! + 1) ≥ n.

1

From Stirling’s approximation (or simply that log n! ≤ n log n), we thus obtain the lower bound

G(x) ≫ log x
log2 x .

We denote π(x) as the number of primes less than or equal to x. In around 1850, Chebyshev
[21] proved the upper bound π(x) ≪ x/ log x, which, by a simple pigeonhole principle argument,
implies G(x) ≫ log x.

Furthermore, the prime number theorem, which states more explicitly that π(x) ∼ x/ log x, was
proven in 1896 independently by Hadamard and de la Vall´ee Poussin. This yields the following
more explicit lower bound, where for any ϵ > 0,

G(x) ≥ (1 − ϵ) log x

for suﬃciently large x. The prime number theorem also tells us that the average prime gap is
∼ log x. The next natural question is to ask whether prime gaps grow larger than average, and
by how much.

Backlund [5] made the ﬁrst small step in this direction in 1929 by proving that, for any ϵ > 0,

G(x) ≥ (2 − ϵ) log x

for suﬃciently large x. In 1930, Brauer, Zeitz [15] then gave a slight improvement on this result
by showing that, for any ϵ > 0, G(x) ≥ (4 − ϵ) log x

for suﬃciently large x. Westzynthius [103] improved upon these results in 1931 by showing that
the average prime gap can be arbitrarily larger than the average gap. That is, he proved that

lim
x→∞ G(x)
log(x) → ∞

whilst speciﬁcally proving the following quantitative improvement of

G(x) ≫ log x log3 x
log4 x .

In 1934, Ricci [89] was able to improve this by eliminating a factor of log4 x to obtain

G(x) ≫ log x log3 x.

Erd˝os [25] improved this result in 1935 to obtain

G(x) ≫ log x log2 x
(log3 x)2

whilst Chang [20] obtained the same result in 1938 using simpler methods. Rankin [86] then
proved the following lower bound in 1938

G(x) ≫ log x log2 x log4 x
(log3 x)2 .

Speciﬁcally, he was able to show that, for any ϵ > 0, and for suﬃciently large x,

G(x) ≥ (c − ϵ) log x log2 x log4 x
(log3 x)2 (2)

where c = 1/3.1 Over the next several decades, only the constant c was improved upon,
with no improvement made to showing that c could be taken to be arbitrarily large. Several

2

authors proved incrementally larger values of c, as given in Table 1, with the most recent being
c = 2eγ ≈ 3.56, proved by Pintz [83] in 1997.

Table 1: Summary of improvements made to the constant c in equation (2).

Constant c Authors Year

1
3 ≈ 0.3333 Rankin [86] 1938

1
2 eγ ≈ 0.8905 Schonhage [93] 1963

eγ ≈ 1.7811 Rankin [87] 1963

1.31256eγ ≈ 2.0172 Maier, Pomerance [66] 1990

2eγ ≈ 3.5621 Pintz [83] 1997

At a meeting in Durham in 1979, Erd˝os oﬀered a $10,000 cash prize to anyone who could prove
that the constant c could be taken to be arbitrarily large [6, p. 468]. Famous for oﬀering cash
prizes to those who could solve some of his favourite open problems, it was his largest ever
prize that he oﬀered.2 This prize stood for nearly 35 years, until it was ﬁnally proven by Ford,
Green, Konyagin, Tao [31], and also independently by Maynard [70] that c could be taken to
be arbitrarily large.

The approaches of the two papers diﬀered in that the former paper relied on the work done
by Green, Tao [37] as well as Green, Tao, Ziegler [38] on the number of solutions to linear
equation in primes. On the other hand, Maynard relied on multidimensional prime-detecting
sieves introduced in an earlier paper of his regarding small gaps between primes [68].

Finally, a collaboration between all ﬁve above-mentioned authors in 2014 [30] produced the
following quantitative improvement of

G(x) ≫ log x log2 x log4 x
log3 x (3)

which is currently the best known lower bound for G(x). In a similar spirit to Erd˝os, Tao has
oﬀered a new $10,000 cash prize to anyone who can prove that the implied constant in (3) can
be taken to be arbitrarily large [99].

Upper bound history

By a similar argument Euclid used to prove the inﬁnitude of primes, we have the very elemen-
tary upper bound G(n) ≤ n! + 1, since by construction n! + 1 must consist of some prime greater
than n.

In 1852, Chebyshev proved Bertrand’s postulate, which states that, for all x ≥ 2, there is a
prime number between x and 2x. This therefore produces the upper bound G(x) ≤ x.

Furthermore, using the prime number theorem, we can generalise Bertrand’s postulate to prove
that, for any ϵ > 0, there exists a prime number between x and (1 + ϵ)x for suﬃciently large x.
This hence yields the bound G(x) = o(x), as shown in Theorem 18. One can keep track of the

1Rankin’s paper did mention though that Erd˝os obtained essentially the same result, but had not been
published [86, p. 242].
2Although the prize was originally $10,000, it was later reduced to $5000, with $10,000 oﬀered only for a proof
that G(x) ≫ (log x)1+ϵ for some ϵ > 0 [27].
 3

error term in the prime number theorem, to obtain the following quantitative improvement,

G(x) ≪ x
ea
√log x

for some constant a, as proven in Theorem 19 in the Appendix.

The next quantitative sublinear upper bound was obtained by in 1930 by Hoheisel [49], who
proved that there exists θ < 1 such that
 G(x) ≪ x
θ,

whilst speciﬁcally obtaining the possible value θ = 1 − 1
33000 . He achieved this by using results
on a zero-free region of the Riemann zeta function ζ(s) proved by Littlewood [63] in 1922. This
was subsequently improved in 1933 to θ = 1 − 1
250 by Heilbronn [46].

Since then, optimal values for θ have been chipped away by numerous authors over the last 100
years, as shown in Table 2. Of note is Ingham’s contribution [52] in 1937, where he proved a
fundamental relationship between maximal primes gaps and the growth rate of the zeta function
on the critical line |ζ(1/2 + it)|. Speciﬁcally, he proved that if
∣
∣
∣ζ( 1
2 + it)∣
∣
∣ = O(tc)

for some positive constant c, then

π(x + x
θ) − π(x) ∼ xθ

log x for any θ > 1 + 4c
2 + 4c .

As a consequence, this would imply G(x) ≪ xθ. Using these ideas, Ingham [52], Titchmarsh
[101], Min [74], and Haneke [41] all proved incrementally better bounds for G(x) using Ingham’s
result.

However, in 1971, Montgomery [75] proved an upper bound of G(x) ≪ x3/5+ϵ without using
results on the bound of |ζ(1/2 + it)|. Since then, all subsequent bounds obtained for G(x) did
not rely on Ingham’s method, whereas the best bound for |ζ(1/2 + it)| is currently c = 13/84,
obtained in 2017 by Bourgain [13], which only yields a value of θ = 34/55 + ϵ ≈ 0.61818.

Table 2: Summary of upper bounds of the form G(x) ≪ xθ proven to date.

Constant θ Authors Year

1 − 1/33000 ≈ 0.999969 . . . Hoheisel [49] 1930
1 − 1/250 = 0.996 Heilbronn [46] 1933
3/4 + ϵ = 0.75 Chudukov [100] 1936
5/8 + ϵ = 0.625 Ingham [52] 1937
5/8 − 1/616 + ϵ ≈ 0.623377 . . . Titchmarsh [101] 1942
5/8 − 1/488 + ϵ ≈ 0.622951 . . . Min [74] 1949
5/8 − 1/392 + ϵ ≈ 0.622449 . . . Haneke [41] 1962
3/5 + ϵ = 0.6 Montgomery [75] 1971
7/12 + ϵ ≈ 0.583333 . . . Huxley [50] 1972
13/23 ≈ 0.565217 . . . Iwaniec, Jutila [54] 1979
11/20 = 0.55 Heath-Brown, Iwaniec [45] 1979
11/20 − 1/406 ≈ 0.547537 . . . Iwaniec, Pintz [55] 1984
11/20 − 1/384 ≈ 0.547396 . . . Mozzochi [77] 1986
6/11 ≈ 0.545454 . . . Lou, Yao [64] 1992
107/200 = 0.535 Baker, Harman [9] 1996
21/40 = 0.525 Baker, Harman, Pintz [10] 2001

4

The best unconditional upper bound for G(x) was obtained in 2001 by Baker, Harman, and
Pintz [10], who proved that G(x) ≪ x0.525. Even assuming the Riemann Hypothesis, one only
obtains the slightly improved bound of G(x) ≪ √x log x, proven by Cram´er [23]. Heath-Brown
[44] obtained a marginally better conditional bound of G(x) ≪ √x log x, assuming both the Rie-
mann Hypothesis as well as some conjectured results on Montgomery’s pair correlation function.

In 1912, Landau presented four open problems regarding prime numbers at the International
Congress of Mathematicians, all of which are still unsolved as of today. One of these four
problems was Legendre’s conjecture, which states that, for every positive integer n, there exists
a prime between n2 and (n + 1)2. Solving this conjecture would be equivalent to proving the
upper bound G(x) ≤ 2
√x for all x ≥ 2. Given that this statement is stronger than a consequence
of the Riemann Hypothesis, one could conclude that there is still much progress to be done on
the upper bound for G(x) before a proof of Legendre’s conjecture could conceivably come to
fruition.

Preliminaries

Before giving a proof of (3), we note some preliminary deﬁnitions and results, which will lead up
to a proof of the lower bound which Rankin obtained in (2). We shall ﬁrst introduce a function
Y (x) which is related to G(x) and has been used to prove all recent lower bounds for G(x).

Deﬁnition 1: Let x be a positive integer. Deﬁne Y (x) as the largest integer y such that, for
all primes p ≤ x, there exists an integer ap such that, for all i ∈ {1, 2, . . . , y}, there exists p ≤ x
such that i ≡ ap mod p.

In other words, Y (x) is the largest y such that the interval {1, 2, . . . , y} can be sieved out by a
set of residue class ap mod p for each prime p ≤ x.

Example: Let x = 7. The primes less than or equal to x are {2, 3, 5, 7}. We can cover the
interval {1, . . . , 9} by choosing the following residue classes: a2 = 1, a3 = 2, a5 = 1, and a7 = 4,
as shown below:
 1 2 3 4 5 6 7 8 9

1 2 3 4 5 6 7 8 9

1 2 3 4 5 6 7 8 9

1 2 3 4 5 6 7 8 9
For p = 2, ap = 1

For p = 3, ap = 2

For p = 5, ap = 1

For p = 7, ap = 4

Furthermore, one can verify either by hand or computationally that no choice of residue classes
(ap mod p) for p ≤ 7 can cover {1, 2, . . . , 10}. This hence proves that Y (7) = 9.

We now show that proving a lower bound for Y (x) also yields a lower bound for G(x).

Lemma 2: [30, p. 67] Let ϵ > 0. Then, for suﬃciently large x, we have

G(x) ≥ Y ((1 − ϵ) log x).

5

Proof: Let P (x) denote the product of all primes no larger than x. We shall ﬁrst prove that

G(P (x) + x) ≥ Y (x).

Let x be a positive integer, and let y = Y (x). Thus, for each prime p ≤ x, there exists residues
ap such that, for all i ∈ {1, . . . , y}, there exists p where i ≡ ap mod p.

Now, by the Chinese Remainder Theorem, there exists some positive integer m such that
m ≡ −ap mod p for all p ≤ x. We can assume x < m ≤ x + P (x) where P (x) denotes
the product of all primes less than or equal to x.

Let t ∈ {1, 2, . . . , y}. Thus, there exists p ≤ x such that t ≡ ap mod p. Note that

m + t ≡ (−ap) + ap ≡ 0 mod p.

Thus, p divides m + t, and since p ≤ x < m < m + t, this implies that m + t is compossite, for all
t ∈ {1, . . . , y} Therefore, we have a sequence of y composite numbers, no larger than P (x) + x,
which proves that G(P (x) + x) ≥ Y (x).

Now, the Prime number theorem is equivalent to the statement that

ϑ(x) := ∑

p≤x log p ∼ x

which, by taking exponentials, implies that P (x) = e(1+o(1))x, which proves, for all ϵ > 0, we
have G(x) ≥ Y ((1 − ϵ) log x)

for suﬃciently large x.

The function Y (x) is also closely related to the Jacobsthal’s function j(n), ﬁrst studied by Ja-
cobsthal [56] in 1960.

Deﬁnition 3: For any positive integer n, deﬁne j(n) to be the maximal gap between integers
coprime to n. Equivalently, j(n) is the smallest positive integer m such that every sequence of
m consecutive integers contains an integer coprime to n.

Note that j(n) depends only on the prime factors dividing n. Thus, it suﬃces to study j(n)
when n is simply a product of distinct prime numbers.

Lemma 4: Let P (x) denote the product of all primes less than or equal to x. For all x ≥ 2,
we have Y (x) = j(P (x)) − 1.

Proof: The lemma follows almost immediately from the proof of Lemma 2. Let y = Y (x)
and deﬁne m in the same way as done in Lemma 2. We then obtain y consecutive composite
numbers from m + 1 to m + y, all with primes factors ≤ x, and thus have a common factor with
P (x). This proves j(P (x)) > Y (x).

Conversely, let m′ = j(P (x)). Thus, m′ is the minimal integer such that every sequence of m′

consecutive integers contains an integer with no prime factors less than or equal to x. Therefore,
there exists a sequence of m′ − 1 consecutive integers all of which have a prime factor less than
or equal to x. However, this simply yields a covering of {1, . . . , m′ − 1} with primes ≤ x, thus

6

proving Y (x) ≥ m′ − 1.

Therefore, combining both of the above results proves the lemma.

Regarding lower bounds for Y (x), we easily observe that Y (x) ≥ x − 1 by simply choosing
ap = −1 for all primes p < x. However, we note that we can do substantially better by proving
an easy explicit lower bound for Y (x).

Theorem 5: [40, p. 1076] Let px be the largest prime less than or equal to x, and let p′
x be the
second largest prime less than or equal to x. Then, for all x ≥ 3, we have

Y (x) ≥ 2p′
x − 1.

Proof: Given some x ≥ 3, let y = 2p′
x − 1. For each prime p ≤ x, we choose residue classes
ap mod p as follows
 ap =
 




p′
x for all primes p < p′
x,
p′
x − 1 for p = p′
x,
p′
x + 1 for p = px.

Let i ∈ {1, . . . , p′
x − 2}. Noting that p′
x − i ≥ 2, let q be a prime dividing p′
x − i. Then, by
deﬁnition we have i ≡ p′
x = aq mod q. Similarly, for any i ∈ {p′
x + 2, . . . , y}, let q be a prime
dividing i − p′
x. Then i ≡ p′
x = aq mod q.

Finally, by deﬁnition of the residue classes apx and ap′
x, we have that p′
x − 1, p′x and p′
x + 1 are
covered by the primes p′
x, 2 and px respectively. Thus, the set of positive integers {1, . . . , y} are
covered by primes less than or equal to x, and thus Y (x) ≥ 2p′
x − 1.

Remark: One can verify computationally that we actually have the equality Y (x) = 2p′
x − 1
for 3 ≤ x < 23. Currently, this is the best known explicit lower bound that we can obtain
algebraically without using sieve methods [40, p. 1076].

Also note that, together with the prime number theorem, this implies

G(x) ≥ (2 − ϵ) log x,

therefore obtaining the same result Backlund [5] achieved in 1929.

Regarding upper bounds for Y (x), Lemma 4 gives a trivial upper bound of Y (x) ≤ P (x) − 1.
Kanold [58] proved by elementary methods that Y (x) ≤ 2π(x) and furthermore than Y (x) ≤
2√
π(x) for π(x) ≥ e50. The best asymptotic upper bound known is due to Iwaniec [53], who
proved that Y (x) ≪ x2.

It has aso been conjectured by Maier and Pomerance [66] that, for any ϵ > 0, we have

Y (x) ≪ x(log x)2+ϵ.

If this is true, it would mean the best lower bound result we could hope to achieve for G(x)
using Lemma 2 is a result of the form

G(x) ≫ log x(log2 x)
2+ϵ,

which is still far from the conjectured lower bound of G(x) ≫ (log x)2. Note that this doesn’t
contradict Cram´er’s conjecture, as given in (14) on page 16, as presumably much is lost when

7

applying Lemma 2 to obtain a lower bound for G(x).

To obtain better lower bounds for Y (x) than that given in Theorem 5, we have to make use of
more sophisticated sieve methods.

Rankin’s bound

In this section, we shall prove the bound which Rankin originally obtained in 1938. Before
doing so, we need to establish an upper bound on smooth numbers.

We deﬁne a positive integer to be z-smooth if all of its prime factors are less than or equal to z.

Deﬁnition 6: Let ψ(x, y) denote the number of positive integers in the interval {1, . . . , x}
which are y-smooth (i.e. such that all prime factors are ≤ y) In other words, we have

ψ(x, y) = |{n ∈ {1, . . . , x} : p | x =⇒ p ≤ y for all primes p}| .

We shall now prove the following explicit bound for ψ(x, y) that will be used in both the proof
of Rankin’s bound and the main theorem.

Lemma 7: [86, p. 243] Let a be a ﬁxed positive constant. For all ϵ > 0, we have

ψ (x, exp ( log x log3 x
a log2 x
 )) < x
(log x)a−1−ϵ

for suﬃciently large x.

Proof: Let y = exp ( logx log3 x
a log2 x ), and let η = 1 − a log2 x
log x . Note that, as x → ∞, we have η
increases with limit η → 1. Thus, we may assume x is suﬃciently large such that η ∈ (3/4, 1).
First, we note that we can express ψ(x, y) as

ψ(x, y) = ∑

n≤x
n is y-smooth
 1 < ∑

n≤x
n is y-smooth
 ( x
n
 )η = xη ∑

n≤x
n is y-smooth
 1
nη < x
η ∑

n is y-smooth
 1
nη .

Note that we can also prime factorise the sum over all y-smooth numbers, as

∑

n is y-smooth
 1
nη = ∏

p≤y
p prime
(1 − p
−η)−1

which furthermore proves the sum is convergent. This therefore gives the following bound

ψ(x, y) < x
η ∏

p≤y
p prime
(1 − p−η)
−1.

Our goal is now to bound this product. Deﬁne

P := ∏

p≤y
p prime
(1 − p−η)
−1.

Taking logarithms, we thus obtain

log P = − ∑

p≤y
p prime
 log (1 − p
−η)

8

= −π(y) log (1 − y−η) + ∫ y

2 π(t) ηt−η−1

1 − t−η dt

= −π(y) log (1 − y−η) + η ∫ y

2
 π(t)
(tη − 1)t dt.

We now make use of the following estimate from the prime number theorem

π(y) = y
log y + O( y
(log y)2
 )
,

as well as the Taylor expansion of the logarithm log (1 + t) = O(t) as t → 0. This gives

log P = − ( y
log y + O( y
(log y)2
 )) · O(y−η) + η ∫ y

2
 1
(tη − 1)t
 ( t
log t + O( t
(log t)2
 )) dt

= O ( y1−η

log y
 ) + η ∫ y

2
 dt
(tη − 1) log t + O (∫ y

2
 dt
(tη − 1)(log t)2
 ) . (4)

Our goal is to now estimate and bound each of the three terms given above in (4). Firstly, by
deﬁnition of y and η, we have

y1−η

log y = exp ( log x log3 x
a log2 x · a log2 x
log x )

log x log3 x
a log2 x = exp (log3 x)
exp (log2 x + log4 x − log a − log3 x) = O(1). (5)

Estimating the second integral, we obtain
∫ y

2
 dt
(tη − 1) log t = ∫ y

2
 dt
tη log t + ∫ y

2
 dt
tη(tη − 1) log t

≤ ∫ y

2
 dt
tη log t + ∫ y

2
 dt
t3/4 · t1/2 + O(1)

= ∫ y

2
 dt
tη log t + 4
t1/4
 ∣
∣
∣
∣

y

2 + O(1)

= ∫ y

2
 dt
tη log t + O(1).

To further evaluate this integral, we apply the following substitution. Deﬁne δ := 1 − η, and
note that we have δ < 1/4 for suﬃciently large x. Now, we substitute u = δ log t. Thus, we get
eu = tδ = t1−η and du = δ
t dt and thus dt = (eu/δ/δ)du. Therefore

∫ y

2
 dt
tη log t = ∫ δ log y

δ log 2
 (eu/δ/δ)du
(e(ηu/δ)(u/δ) = ∫ δ log y

δ log 2
 eu

u du

= ∫ 1

δ log 2
 eu

u du + ∫ δ log y

1
 eu

u du

= log ( 1
δ
 ) + O(1) + yδ

δ log y + O ( yδ

δ2(log y)2
 ) (6)

where we have used the integration results given in Lemmas 20 and 21, also noting that
δ log y = log3 x → ∞ as x → ∞.

By a similar argument, we now bound the second term, noting that
∫ y

2
 dt
(tη − 1)(log t)2 ≤ ∫ y

2
 dt
tη(log t)2 + O(1)

9

= ∫ δ log y

δ log 2
 (eu/δ/δ)du
(e(ηu/δ)(u/δ)2 = δ ∫ δ log y

δ log 2
 eu

u2 du

= δ ∫ 1

δ log 2
 eu

u2 du + δ ∫ δ log y

1
 eu

u2 du

= δ ( 1
δ log 2 + O( log 1
δ
 )) + δ ( yδ

δ2(log y)2 + O( yδ

δ3(log y)3
 ))

= O(1) + O ( yδ

δ2 log y2
 ) (7)

where we have similarly used the integration results given in Lemmas 22 and 23.

Finally, combining the results obtained in equations (5), (6), and (7), we apply these bounds to
equation (4) to obtain the following bound for P ,

log P ≤ yδ

δ log y + log 1
δ + O ( yδ

δ2 log y2
 ) = exp(log3 x)
exp(log4 x) + log2 x + O(log3 x).

Thus, for any ϵ > 0, we have that, for suﬃciently large x,

ψ(x, y) ≤ exp (η log x) · P ≤ exp (
log x − a log2 x + log2 x + O( log2 x
log3 x
 )) < x
(log x)a−1−ϵ ,

which gives the desired result.

Remark: This is certainly not the best bound for ψ(x, y) that one can obtain. Indeed, bet-
ter bounds were obtained by de Bruijn [17] with further improvements achieved in the 1980s
[65, 47].3 However, the above bound is certainly suﬃcient for our purposes, both in the proof
of Rankin’s bound as well as the main theorem.

We now have suﬃcient machinery to prove Rankin’s original bound, given in (2).

Theorem 8: [86, p. 242] We have

G(x) ≫ log x log2 x log4 x
(log3 x)2 . (8)

The proof can essentially be summarised as follows:

1. Partition the primes from 1 to x into four disjoint sets based on their size. Using Lemma 2
along with a suitable choice of y, we aim to cover {1, . . . , y} with residue classes (ap mod p)
for primes p ≤ x.

2. Select residue classes ap = 0 for both the very small and medium sized primes.

3. Then, select the residue classes ap for the medium primes in a random manner, and
show by Chang’s averaging argument and Mertens’ theorem that the remaining number
of elements is ≪ x/ log x.

4. Finally, use a simple greedy strategy to allocate each of the remaining elements to residue
classes for the large primes.

3An extensive bibliography and survey of the results on smooth results obtained before 1970 can be found at
[79].
 10

Proof: [76, p. 221] Let x be a suﬃciently large real number, and deﬁne

L = log x log3 x
4(log2 x)2

and let y = xL/3. We ﬁrst aim to obtain a bound on ψ(y, LL) using Lemma 7. Note that for
suﬃciently large x, we have

log L = log2 x + log4 x − log 4 − 2 log3 x < 8
7 log2 x

noting that log L ∼ log2 x as x → ∞. Thus, for x in this range we have

L
L = exp (L log L) < exp ( log x log3 x
4(log2 x)2 · 8
7 log2 x
) = exp ( log x log3 x
3.5(log2 x)2
 ).

Therefore, applying Lemma 7 with a = 3.5, we have that, for all ϵ > 0,

ψ(y, LL) < ψ (
y, exp ( log x log3 x
3.5(log2 x)2
 )) < y
(log y)2.5−ϵ

for suﬃciently large x. Letting ϵ = 1/2, this therefore yields the bound

ψ(y, L
L) < y
(log y)2 < y
(log x)2 = x log3 x
12 log x(log2 x)2 < π(x/3) (9)

for suﬃciently large x.

We now partition all the prime numbers less than x into the following four disjoint sets.

P1 := {p prime : p ≤ L},

P2 := {p prime : L < p ≤ LL},

P3 := {p prime : L
L < p ≤ x/3},

P4 := {p prime : x/3 < p ≤ x}. (10)

For each i ∈ {1, 2, 3, 4}, denote Pi as the product of all primes in Pi. We deﬁne the set N as

N = {n ∈ {1, 2, . . . , y} : (n, P1P3) = 1}.

In other words, N is the set of positive integers less than or equal to y which are coprime to
all primes in P1 and P3. Now, let n ∈ N . Note that, if n is not prime, and has some prime
factor greater than x/3, then it must contain a prime factor smaller than L, and thus contains
a prime factor from P1, which results in a contradiction.

Thus, all elements of N are one of the following,

• The integer 1.

• Integers n consisting solely of prime factors of P2.

• Primes p such that x/3 < p ≤ y.

Therefore, using the bound on ψ(x, LL) given in (9), we have an upper bound for N ,

|N | ≤ 1 + ψ(y, L
L) + π(y) − π(x/3) ≤ 1 + π(y)

11

and thus, by the prime number theorem, we obtain

|N | ≤ 5
4 · y
log y < 5
4 · xL
3 log x = 5
12 · xL
log x

for suﬃciently large x. Our next goal is to choose a suitable M (mod P1P2P3P4) such that
every element in {M + n : 1 ≤ n ≤ y} has a common factor with P1P2P3P4. Therefore, using
Lemma 4, this will give us a lower bound for Y (x).

We begin by choosing M such that M ≡ 0 (mod P1P3). Now, for any positive integer m, deﬁne

Am = |{n ∈ N : (m + n, P2) = 1}|.

We now choose m such that Am is minimal, by doing the following averaging argument, which
is essentially due to Chang [20]. Note that

P2∑

m=1 Am =
 P2∑

m=1
 ∑

n∈N
(m+n,P2)=1
 1 = ∑

n∈N
 P2∑

m=1
(m+n,P2)=1
 1 = ∑

n∈N φ(P2) = |N | · ∏

p∈P2(p − 1).

Therefore, there must exist some M (mod P2) such that

AM ≤ |N | ∏

p∈P2
 (
1 − 1
p
 )

Now, by Mertens’ (third) theorem, we have that, as L → ∞,

∏

p∈P2
 (1 − 1
p
 ) =
 ∏p≤L (1 − 1
p )−1

∏p≤LL (1 − 1
p )−1 ∼ log L
L log L = 1
L .

Thus, for suﬃciently large L, we can ensure that this product is less than 3/2L. Therefore, we
obtain
 |{n ∈ {1, . . . , y} : (M + n, P1P2P3) = 1}| = |{n ∈ N : (M + n, P2) = 1}|

≤ |N | · 3
2L ≤ 5
12 · xL
log x · 3
2L = 5
8 · x
log x

for suﬃciently large x. Finally, again using the prime number theorem, we note a lower bound
for the number of primes in P4 as

|P4| = π(x) − π(x/3) ∼ 2
3 x
log x .

Thus, for suﬃciently large x, we have

|{n ∈ {1, . . . , y} : (M + n, P1, P2P3) = 1}| < |P4|.

Therefore, for each remaining element n ∈ {1, . . . , y} such that M + n is coprime to P1P2P3,
we can map n to a unique prime p ∈ P4. By choosing an appropriate residue M mod p, we can
ensure that p divides M + n, and thus, by the Chinese Remainder Theorem, we have the exis-
tence of some M such that, for every n ∈ {1, . . . , y}, there exists p ≤ x such that p divides M +n.

Therefore, by Lemma 4, we have Y (x) ≥ y, and thus by Lemma 2, this proves that, for all
ϵ > 0, we have
 G(x) ≥ Y ((1 − ϵ) log x) ≥ ( 1
12 − ϵ
) log x log2 x log4 x
(log3 x)2

12

for suﬃciently large x, thus completing the proof.

Note that we had room to spare in several places to improve on the constant. A ﬁnal constant
of 1/12 − ϵ works in our calculations done above, although Rankin did proved a constant of
1/3 − ϵ by simply tightening the relevant bounds using similar methods in his paper.

We shall return to a similar approach done here to ﬁnish proving the main theorem in [30].

Heuristic results

With the best current bounds for G(x) being

log x log2 x log4 x
log3 x ≪ G(x) ≪ x
0.525,

mathematicians are still a long way from proving a ﬁnal asymptotic growth rate for G(x). To
obtain a probable growth rate, we can resort to using probabilistic methods. This involves con-
sidering some heuristic regarding how the primes are roughly distributed at large, then applying
these heuristic models to investigate which statements hold with probability 1.

We note that these by no means constitute rigourous proofs by any measure. Indeed, for any
positive integer n, the probability P(n is prime) is simply 1 if n is prime, and 0 if n is not
prime.4 Instead, we consider taking a random sequence of integers satisfying some probabilistic
conditions based on known theorems regarding the distribution of primes (such as the prime
number theorem). The following heuristic model is one which is based on Cram´er’s model,
originally considered by the Swedish mathematician Harold Cram´er in 1936.

Cram´er’s model

From the prime number theorem, we know that the number of primes less than or equal to
x is roughly x/ log x, for suﬃciently large x. This suggests a heuristic where we say that the
probability that the integer n is prime is roughly 1/ log n.

With this in mind, we consider a sequence of independent random variables X2, X3, X4, . . .
where each random variable only has two possible outcomes, either 0 or 1, and

P(Xn = 1) =
 {
1 for n = 2,

1
log n for all n ≥ 3.

Note that, since 1/ log 2 > 1, we simply set X2 to always have value 1. Now, consider the
random variable Sn, which counts the number of Xi for i ≤ x which are 1,

Sx = ∑

2≤n≤x Xn = X2 + X3 + · · · + X⌊x⌋.

By linearity of expectation, we can calculate the expectation of Sx as

ESx = ∑

2≤n≤x EXn = 1 + ∑

3≤n≤x
 1
log n = 1 + ⌊x⌋
log x + ∫ x

3
 ⌊t⌋
t log2 t dt

= x
log x + O ( x
(log x)2
 )

4The prime numbers are a fully deterministic sequence, and not some random variable.

13

where we used partial summation to evaluate the above sum. This therefore yields ESx ∼
x/ log x which agrees with the prime number theorem. Indeed, by also calculating ES2
x and
applying Lemma 16, or alternatively by applying Hoeﬀding’s inequality, one can furthermore
show that we have Sx ∼ x
log x

with probability 1.

We now deﬁne the sequence of random variables P1, P2, P3, . . . (with Pn+1 being dependent
on Pn) in the following recursive manner. Let P1 = 2 and Pn+1 = min{i : Xi = 1 and i > Pn}
for n ≥ 2. Note that this matches the expected behaviour of the sequence of prime numbers
p1, p2, p3, . . . according to the prime number theorem. We remark that one can prove EPi is
some ﬁnite value, for each i ≥ 2. For example, we obtain

EP2 =
 ∞∑

n=3
 n
log n
 n−1∏

k=3
 (
1 − 1
log k
 ) ≈ 3.13.

Similarly, one can show EP3 ≈ 4.64, EP4 ≈ 6.47, and in general show that Pn ∼ n log n with
probability 1.

Similarly to our deﬁnition of G(x), we can deﬁne the heuristic maximal prime gap as the random
variable G(x) dependent on x, deﬁned as

G(x) = max
Pn≤x(Pn+1 − Pn).

We shall now prove that the following statement holds with probability 1,

lim sup
x→∞ G(x)
(log x)2 = 1.

Proof: [24, p. 27] Let c > 0 be a given ﬁxed constant. For each m ≥ 2, deﬁne Em as the event
that Xm, Xm+1, . . . , Xm+⌊c(log m)2⌋ are all 0. Thus, by independence of Xi, we have

PEm =
 ⌊c(log m)2⌋∏

i=1 (1 − P(Xi = 1)) =
 ⌊c(log m)2⌋∏

i=1
 (1 − 1
log(m + i)
 ) .

We now aim to obtain lower and upper bounds for PEm. Using the Taylor expansion log (1 + x) =
x + O(x2) for small x yields the estimate 1 + x = exp (x + O(x2)) which thus gives

PEm =
 ⌊c(log m)2⌋∏

i=1
 (1 − 1
log(m + i)
 ) =
 ⌊c(log m)2⌋∏

i=1 exp (
− 1
log(m + i) + O( 1
log(m + i)2
 ))

= exp
 

−
 ⌊c(log m)2⌋∑

i=1
 1
log(m + i) + O( ⌊c(log m)2⌋∑

i=1
 1
log(m + i)2
 )


 .

Firstly, we note that the error term is clearly bounded by c and is thus O(1). Now, applying
partial summation to the main term, we obtain

⌊c(log m)2⌋∑

i=1
 1
log(m + i) = c(log m)2

log (m + c(log m)2) + ∫ c(log m)2

1
 ⌊t⌋
(m + t)(log (m + t))2 dt.

14

The ﬁrst term yields

c(log m)2

log (m + c(log m)2) = c log m + c log m (log m − log (m + c(logm)2)
)

log (m + c(log m)2) = c log m + O(1),

whilst the integral can be bounded as follows

∫ c(log m)2

1
 ⌊t⌋
(m + t)(log (m + t))2 dt ≤ ∫ c(log m)2

1
 1
(log (m + t))2 dt ≤ c(log m)2

log (m + 1)2 ≤ c.

We therefore obtain
 PEm = exp (−c log m + O(1)) = eO(1)

mc

which implies there exists some constants A and B (dependent on c) such that

A
mc < PEm < B
mc (11)

for all m ≥ 2. Therefore, from the above bounds, we note that if c > 1, this tells us that the
sum of the probabilities PEm is ﬁnite,

∞∑

m=1 PEm <
 ∞∑

m=1
 B
mc = B · ζ(c) < ∞.

Thus, by the Borel-Cantelli lemma [19, p.334], we have that the probability that inﬁnitely many
of the events Em occur is 0. This proves that, with probability 1, we have G(x) ≥ c(log x)2 is
satisﬁed for only ﬁnitely many values of x. Thus, with probability 1, we have

lim sup
x→∞ G(x)
(log x)2 ≤ 1. (12)

Conversely, we now consider the case c < 1. By using the lower bound in (11), we now show
that, with probability one, inﬁnitely many of the events Ei will occur.

We consider the following recursively deﬁned sequence. Let m1 = 2 and for all i ≥ 1, deﬁne

mi+1 = mi + ⌊c(log mi)
2⌋ + 1.

Thus, by construction, we have that the sequence of events Em1, Em2, . . . are independent.

We can furthermore prove that mr < 100r(log r)2 for all r ≥ 2. Proceeding by induction, we
note the base case is easily satisﬁed, since

m2 ≤ 3 + (log 2)
2 < 10 < 200(log 2)2.

Now assume that, for some r ≥ 2, we have mr < 100r(log r)2. Therefore, we note

mr+1 = mr + ⌊c(log mr)
2⌋ + 1 ≤ mr + (log mr)
2 + 1

< 100r(log r)
2 + (log (100r(log r)
2))2 + 1

< 100r(log r)
2 + (log (25r3)
)2 + 1

= 100r(log r)
2 + (log (100r3) − log 4
)2 + 1

< 100r(log r)
2 + log (r10)
2

= 100r(log r)
2 + 100(log r)
2

15

< 100(r + 1)(log (r + 1))2

where we used the mild bound of 2 log r < r and 100 < r7 for all r ≥ 2. Therefore, by induction,
this hence proves that, for all r ≥ 2, we have the bound

mr < 100r(log r)
2.

Therefore, noting that c < 1, we deﬁne ϵ := (1 − c)/2. Since we have c + ϵ < 1, and noting that
(log i)2c < iϵ for suﬃciently large i, we obtain that

n∑

i=1 PEmi >
 n∑

i=1
 A
mc
i >
 n∑

i=1
 A
(100i(log i)2)
c > A
100c
 n∑

i=1
 1
ic+ϵ + O(1)

> A
100c
 ∫ n

1
 1
tc · tϵ dt + O(1) = A
100c tϵ

ϵ
 ∣
∣
∣
∣

n

1 + O(1)

which diverges as n → ∞, since ϵ > 0 (noting that the O(1) error term does not depend on
n). Thus, by the second Borel-Cantelli lemma [19, p.336], noting that the sequence of events
(Emi)∞
1 is mutually independent and the sum of probabilities diverges, we obtain with proba-
bility 1 that inﬁnitely many of the events Emi occur.

Thus, with probability 1, we have G(mi) ≥ c(log mi)2 for inﬁnitely many i, which therefore
implies
 lim sup
x→∞ G(x)
(log x)2 ≥ 1 (13)

with probability 1. Combining the above two results given in (12) and (13), we therefore obtain
with probability 1, that the following holds

lim sup
x→∞ G(x)
(log x)2 = 1,

thus completing the proof.

Using the above model, Cram´er naturally conjectured that the following similar result holds for
the prime numbers
 lim sup
x→∞ G(x)
(log x)2 = 1. (14)

This is often referred to as Cram´er’s conjecture. Furthermore, one can also show the stronger
statement that G(x) ∼ (log x)2 with probability 1 [11, p. 2]. Based on these observations,
Shanks [94] similarly made the stronger conjecture that G(x) ∼ (log x)2.

Alternate models

Several reﬁnements on Cram´er’s probabilistic model have been proposed, most notably by
Granville [36]. In fact, due to the work done by Granville, it is now widely believed that
Cram´er’s conjecture (14) is false. Indeed, there some theorems concerning short intervals be-
tween primes, such as Maier’s theorem [65], which contradict Cram´er’s model.

Based on these drawbacks, Granville [36] oﬀered the following probabilistic model as a reﬁne-
ment on Cram´er’s model. Let T be a suitably chosen parameter, and let X3, X4, . . . be a
sequence of random variables with only two possible outcomes, 0 or 1, such that, for n ≥ 3, if
n has some prime factor ≤ T , then Xn = 0, otherwise, let

P(Xn = 1) := ∏

p≤T
 ( p
p − 1
 ) · 1
log n .

16

Note that letting T = 1 gives us exactly Cram´er’s model, whereas Granville considered the case
where T grows slowly in x. What this new model does is essentially removes any integers which
have a small prime factor ≤ T (in a similar fashion to the sieve of Eratosthenes), and then only
do we consider density arguments to calculate P(Xn = 1).5 With this new model, Granville
obtained the conjecture that
 lim sup
x→∞ G(x)
(log x)2 ≥ 2e
−γ ≈ 1.12. (15)

Furthermore, it has been conjectured by Pintz [83] that G(x)/(log x)2 may in fact be unbounded,
and thus that the limsup given above is inﬁnite. A full discussion on Cram´er’s method and its
shortcomings can be found in [95].

Despite the above results, it is still believed [1] that the following (slightly weaker) result holds
for any ϵ > 0, G(X) ≪ (log x)2+ϵ.

Several others [18, 88, 104] have proposed reﬁned conjectured growth rates for G(x), most of
which are consistent with Cram´er’s model that G(x) ∼ (log x)2 A summary of these is graphed
alongside G(x) in Figure 1.

Most recently, Banks, Ford, Tao [11, p. 6] proposed a new probabilistic model GR(x) based
around the Hardy-Littlewood conjecture [42], which successfully reproduces Granville’s lower
bound given in (15). Furthermore, they proved that, for any ϵ > 0, one has with probability
one,
 (2e
−γ − ϵ)(log x)2 ≤ GR(x) ≤ (2e−γ + ϵ) (log x)2 log2 x
2 log3 x

for suﬃciently large x.

In summary, given how little we know about the structure of the primes, most mathematicians
would concur with the following quote from Vaughn [36]:

“It is evident that the primes are randomly distributed but, unfortunately, we don’t know what
’random’ means.” - R. C. Vaughan (February 1990)

Computational results

Computation of G(x)

Since classical times, mathematicians have long been interested in explicitly calculating the
prime gaps pn+1 − pn for small n. With the advent of digital computing in the mid 20th cen-
tury, the calculation of increasingly larger primes became vastly more attainable. Indeed, since
1951, all new prime gap records have been calculated electronically.6 In 1957, Lehmer [61]
calculated all maximal prime gaps below 37 million. Since then, many authors have increased
the list over the last 60 years, a summary of which is shown in Table 3.

A major computational milestone was achieved in September of 2018, when all maximal prime
gaps below 264 ≈ 1.8·1019 were calculated. This was done by a collaborative eﬀort between many

5For example, Granville’s model correctly gives that, for all x ≥ 3, it is impossible for both x and x + 1 to be
prime, whereas Cram´er’s model (incorrectly) predicts that there should be x/(log x)2 such pairs below x.
6The last time someone calculated a prime by hand was in 1951, when Aim´e Ferrier computed that(
2
148 + 1) /17 is prime using only a mechanical desk calculator [22].

17

diﬀerent contributors. Oliveira e Silva, Herzog, and Pardi [81], veriﬁed all gaps up to 4 · 1018

with the remaining checks done on the Prime Gap Search (PGS) thread on the Mersenne forum
[72]. The largest known maximal prime gap is a gap value of G(x) = 1550 for x ≈ 1.84 · 1019

found by Nyman [78] in 2014.

Table 3: Summary of the values of G(x) calculated for x ≤ X.

Upper bound X Attained by Year

3 · 106 Glaisher [35] 1878
1 · 107 Western [102] 1934
3.7 · 107 Lehmer [61] 1957
1.044 · 108 Gruenberger, Armerding, Baker [8, 39]7 1959
1.096 · 1010 Lander, Parkin [60] 1967
4.444 · 1012 Brent [16] 1980
7.263 · 1013 Young, Potler [105] 1989
1 · 1015 Nicely [78] 1999
5 · 1016 Nyman [80] 2003
4 · 1018 Oliveira e Silva, Herzog, Pardi [81] 2012
264 PGS (Mersenne Forum) [72] 2018

Calculating the Cram´er-Shanks-Granville ratio [78] for prime gaps below 264 whilst ignoring
erroneously small values, we obtain
 max
7<x≤264 G(x)
(log x)2 ≈ 0.9206

which is still below the conjectured value of 1 by Cram´er, and 2e−γ ≈ 1.12 by Granville.

101 102 103 104 105 106 107 108 109 1010101110121013101410151016101710181019
0

200

400

600

800

1,000

1,200

1,400

1,600

1,800

2,000
 x

Maximal prime gap G(x)
Heuristic expectation EG(x)
2e−γ(log x)2 (Granville)
(log x)2 (Cram´er)
(log x)2 − log x − 1 (Firoozbakht)
log x(log x − log2 x) (Cadwell)
log x(log x − 2 log2 x) (Wolf)
(log x − log2 x)2 (Rodriguez)

Figure 1: Comparison of G(x) with the heuristic expectation EG(x) calculated from Cram´er’s
model, along with several other conjectured growth rates.

7The attribution given to the discovery of prime gaps below 108 is somewhat uncertain. For example, Appel,
Rosser [4] published incomplete (but nonetheless still signiﬁcant) results on prime gaps below 10
8 in 1961. That
same year, Gruenberger, Armerding [39] gave conclusive results on prime gaps below 1.044 · 10
8 based on data
which was generated by Baker, Gruenberger [8] two years prior in 1959 [78].

18

The computational evidence alone thus does not seem to contradict Cram´er’s conjecture as of
yet, however, we note that even 264 is still minute by asymptotic standards, as several state-
ments regarding primes (most notably Littlewood’s result that π(x)−li(x) changes sign inﬁnitely
often) only occur for very large values of x. Many independent computers today are actively
searching for large values of x with Cram´er-Shanks-Granville ratio bigger than 1 [36].

Computation of Y (x)

Whilst values for G(x) have been computed for x ≤ 264, the computation of Y (x) is compara-
tively much slower, with even the best algorithms running not substantially faster than brute
force. Explicit values for Y (x) for x < p50 were calculated by Hagedorn [40], with values for
x < p55 obtained by Ziller, Morack [106]. Some further values for Y (x) upto x ≤ p57 have
recently been obtained on the Mersenne forums [34].

Given that a naive calculation of Y (x) takes O(P (x)) time (by simply trying every possible
residue ap for each prime p ≤ x), we instead calculate some suboptimal lower bounds using
both a greedy approach as well as modiﬁed greedy approach based on Rankin’s lower bound.

For the greedy algorithm, we consider calculating an lower bound inverse to Y (x). That is, for
some positive integer y, we denote q(y) as the minimal prime number p such that {1, . . . , y}
can be sieved out using only primes from 2 to p by applying a greedy strategy starting from the
smallest prime. In other words, for each y ≥ 1, q(y) is computed as follows:

• We initially set N := {1, 2, . . . , y}.

• Start with p = 2.

• Then, while N ̸= ∅,

– Choose a residue class ap mod p such that |{n ∈ N : n ≡ ap mod p}| is maximal.

– Sieve out these elements from N ,

N ↦→ {n ∈ N : n ̸≡ ap mod p}.

– If N ̸= ∅, then increment the prime p, pi ↦→ pi+1, and repeat.

• Once N = ∅, then output p as the value for q(y) .

Using this greedy approach, we can therefore calculate a lower bound for Y (x) by deﬁning Y ′
gr(x)
as the inverse function Y ′
gr(x) = max{y : q(y) = x}.

We do however note that, as calculated above, both functions q(y) and Y ′
gr(x) are not non-
decreasing. In fact, by direct computation, we obtain for example that q(18) = 17, whilst
q(21) = 13. To rectify this, we introduce

Ygr(x) = max{y : q(y) ≤ x}

which, by deﬁnition, yields a non-decreasing function which gives the optimal greedy choice of
y for each x. We note that the greedy algorithm coincides with the optimal value Y (x) = Ygr(x)
for x ≤ 16.

To calculate a further improvement on Ygr(x), we consider a modiﬁcation to the greedy algo-
rithm where we simply choose residue classes ap = 0 for very small primes p ≤ L, for some

19

suitable small value L. This strategy thus closely mimics that done in proving Rankin’s bound
in Theorem 8.

To this end, we deﬁne r(y, L) as the minimal prime p such that {1, . . . , y} can be sieved out
using primes from 2 to p, with ap = 0 for p ≤ L and ap chosen greedily for p > L. We then
let YRan(x) to be the maximal y such that r(y, L) is no greater than x, where for each x, L is
chosen to yield the most optimal value for YRan(x),

YRan(x) = max{y : ∃L ≤ y s.t. r(y, L) ≤ x}.

We do note that the values obtained for YRan(x), as shown in Figure 2, are marginally better
than those obtained by a pure greedy strategy, thus conﬁrming that a choice of ap = 0 for very
small primes can be more optimal than only using a greedy approach.

50 100 150 200 250 300 350 400 450 500 550 600
0

500

1,000

1,500

2,000

2,500
 x

Y (x)
2p′
x − 1
Greedy (non-inc) algorithm Y ′
gr(x)
Greedy algorithm Ygr(x)
Rankin’s algorithm YRan(x)
Pintz
Maier, Pomerance

Figure 2: Graph of known values for Y (x) for x ≤ 270. Several lower bounds are also graphed
in comparison, including the weak lower bound obtained in Theorem 5, as well as lower bounds
generated by the greedy strategy and Rankin’s bound. Furthermore, the lower bounds obtained
by Maier, Pomerance [66] and Pintz [83] are also shown for comparison.

Unfortunately, a heuristic model for Y (x) cannot easily be established as was done for G(x) us-
ing Cram´er’s probabilistic model. Indeed, if we take the naive approach and deﬁne the random
variable Y(x) in the similar manner as before (with x being ”prime” with probability 1/ log x),
then one obtains with non-zero probability that Y(x) is inﬁnite for all x ≥ 12 and hence EY(x)
is inﬁnite for x ≥ 12. 8

Even if one ﬁxes small primes, as is done in Granville’s model, we still obtain that EY(x) would
be inﬁnite for suﬃciently large x, by a result from Iannucci [51]. Nevertheless, it may still
be possible to analyse Y (x) using heuristic models, especially given some results based on the
recent new probabilistic model published by Banks, Ford, Tao [11].

8For example, this occurs if the integers {2, 3, 4, 6, 12} are taken to be ”prime”, then one can take residues
a2 = 0, a3 = 2, a4 = 1, a6 = 3 and a12 = 11 which will cover all the integers.

20

Main result

We now arrive at the heart of this essay, which is proving the lower bound given in (3). Mak-
ing the leap from Rankin’s bound given in (8) and proven in Theorem 8, to showing that the
constant c in (2) can be taken to be arbitrarily high is a highly non-trivial task and is the
culmination of work done by several authors over the past few years. We shall not give a full
proof of (3) from the ground up, but rather we shall focus on proving the key contribution given
in [30] which showed the quantitative improvement of a factor of log3 x given in (3).

Our overall strategy is described as follows. We begin by using a similar approach to that taken
in the proof of Theorem 8. We take x to be suﬃciently large, and deﬁne

y := cx log x log3 x
log2 x (16)

for some suitable small positive constant c. An explicit value for c is calculated in the Appendix
(e.g. we can take any c < 1
72000 log 5 ). By using Lemma 2, our goal would be to show that
Y (x) ≫ y for suﬃciently large x. We ﬁrst note that it suﬃces to only sieve out {x + 1, . . . , y}
with primes p ≤ x, since y − x ∼ y. As with Rankin’s proof, we begin by partitioning the primes
in {1, . . . , x} into four disjoint sets, ﬁrst by deﬁning

z := exp ( log x log3 x
4 log2 x
 )
, (17)

and then deﬁning the four sets of primes

P1 = {p prime : p ≤ (log x)20},

P2 = {p prime : (log x)20 < p ≤ z},

P3 = {p prime : z < p ≤ x/2},

P4 = {p prime : x/2 < p ≤ x}. (18)

Note that the deﬁnition of Pi given above diﬀers slightly from that given in (10). We then ﬁrst
proceed as done in Theorem 8 by choosing residue classes ap = 0 for both very small (p ∈ P1)
and medium (p ∈ P3) sized primes, whilst choosing residues randomly for small primes (p ∈ P2).

For ease of notation, we deﬁne Py as the set of primes in {x + 1, . . . , y},

Py := {p prime : x < p ≤ y}. (19)

Furthermore, for any i ∈ {1, 2, 3, 4}, and for any set of residue classes ⃗r = (rp mod p)p∈Pi, we
deﬁne the sifted set S(⃗r) as those integers not covered by any residue class (rp mod p) for any
prime p ∈ Pi, S(⃗r) = {n ∈ Z : n ̸≡ rp (mod p) for all p ∈ Pi}.

Therefore, after sifting out elements in {x+1, . . . , y} using primes from P1 and P3, what remains
is the set of primes Py along with a set of z-smooth numbers, the latter of which is essentially
negligible.

After selecting a set of random residue classes ⃗a = (ap mod p)p∈P2 from the small primes to
sift out further elements from Py, we obtain the set Py ∩ S(⃗a) which, by Mertens’ theorem, has
cardinality on the order of x
log x log2 x.

To obtain an improvement on (8), we are now required to choose residue classes ap for the
large primes p ∈ P4 in a more eﬃcient manner than done in Theorem 8, where we simply ap-
plied a greedy approach which only ensured that each residue class ap covered at least 1 element.

21

This is where Maynard’s key contribution comes in, where by using a slight modiﬁcation of
methods from [70], which itself is based on multidimensional sieve estimates obtained in [68],
we obtain tuples ap + h1p, ap + h2p, . . . , ap + hkp which contain ≫ log k prime numbers, for a
suitable large choice of k. Speciﬁcally, based on calculations done in [69], k can be taken to be
≫ (log x)1/5, which results in the residue classes (ap mod p) covering ≫ log2 x new elements,
instead of just 1 element compared to the greedy approach.

Therefore, for p ∈ P4, we choose ap randomly based on the following probability distribution,
which is a multidimensional generalisation of the Selberg sieve weights,

P(ap ≡ a mod p) := 1
W
 ∑

n≡a mod p
L1(n),...,Lk(n)∈S
 ( ∑

d1,...,dk
di|Li(n)
d1d2...dk<R
 µ(d)F ( log d1
log R , . . . , log dk
log R
 ))2, (20)

where W is the appropriate normalisation factor, Li(n) = n + hip for suitable values of hi, and
F : Rk → R is some suitable smooth function supported on [0, ∞)k [71, p. 10]. Doing this choice
for each p ∈ P4 independently, one obtains the following quantitative improvement,

G(x) ≫ log x log2 x
log3 x , (21)

due to unpublished calculations from Maynard [30, p. 5]. In order to obtain the more optimised
lower bound given in (3), instead of choosing (ap mod p) independently, we are required to ap-
ply further combinatorial techniques to achieve improved sieve eﬃciency. Speciﬁcally, we apply
a generalisation of a hypergraph covering theorem from Pippenger, Spencer [85], which is based
on the R¨odl nibble from [91], described in further detail on page 25. This allows us to obtain
the further quantitative improvement by a factor of log4 x as given in (3).

After applying the above, we are still left with ≪ x/ log x elements remaining. This can easily
be dealt with, by increasing x by some suitable constant K > 1. We thus deﬁne, for some
suitable K > 1, a set of very large primes P5 deﬁned as

P5 = {p prime : x < p ≤ Kx}.

Greedily allocating each remaining prime in Py to an element in P5 thus completes the sieving
process. A summary and comparison of this new strategy alongside that used in Rankin’s bound
is given in Table 4.

Table 4: Comparison between choice of residue classes ap mod p for Rankin’s method and our
new strategy.

Prime size Rankin’s method New method

p ∈ P1 (very small) Choose ap = 0. Choose ap = 0.

p ∈ P2 (small) Choose ap randomly. Choose ap randomly.

p ∈ P3 (medium) Choose ap = 0. Choose ap = 0.

p ∈ P4 (large) Choose the remaining
residues greedily.
 Choose ap randomly based on modiﬁed Selberg
sieve weights (20), introduced by Maynard [68].
Then, generate an eﬃcient covering of Py ∩ S(⃗a) by
(ap mod p) using a hypergraph covering theorem.

p ∈ P5 (very large) - Choose the remaining
residues greedily.

22

For the remainder of this essay, we shall assume Maynard’s results that, for suﬃciently large x,
there exists a suitable choice of (h1, . . . , hk) such that ap + h1p, . . . , ap + hkp captures ≫ log2 x
primes in Py, after having sieved out elements using the small primes. This statement is en-
coded in Theorem 13, which we state without proof.

We now focus our eﬀorts on proving the generalised hypergraph covering theorem. To do so,
we ﬁrst give a short introduction to the probabilistic method and how hypergraphs can be used
to reduce our problem to a combinatorial one.

Probabilistic method

We shall make full use of the probabilistic method [3] in our arguments. The basic idea is that,
to show the existence of some combinatorial structure with certain properties, we construct
random variables such that it attains the desired properties with non-zero probability. Thus,
there must exist some event which gives rise to these conditions.

The probabilistic method has been successfully applied to numerous problems over the last
80 years, primarily in combinatorics. Whilst Szele [97] was aware of the probabilistic method
in 1943, it was Erd˝os who ﬁrst understood the immense power the probabilistic method had
in applications to combinatorics, and frequently used it to prove a multitude of combinatorial
problems since the 1940s [26].

Note that in most cases our random variables will be discrete with only ﬁnitely many possible
outcomes, the only exception to this being the random variable tuple ⃗t deﬁned on page 44.
Thus, there is no need to distinguish between the essential range and range of a random vari-
able, and similarly with the notions of almost surely and surely.

All random variables will be denoted in boldface (e.g. X, Y, W). We will occasionally also
consider ﬁnite sequences of random variables, denoted as ⃗x = (xi)i∈I where I is the relevant
indexing set.

We now give a brief combinatorial interlude to show how obtaining lower bounds for Y (x) can
be reduced to a combinatorial problem, thus allowing us to apply the probabilistic method.

Hypergraph covering

Deﬁnition 9: A hypergraph G is a pair G = (V, E), where the set V is referred as the vertices
of the hypergraph, and E is a subset of P(V )\{∅}. Elements e of E are referred to as edges of
the hypergraph.

We furthermore deﬁne a hypergraph (V, E) as k-uniform if each of the edges e ∈ E has constant
size k. For some vertex v ∈ V , we deﬁne the degree d(v) as the number of edges in E containing
v. Similarly, given two vertices v, w, we deﬁne the codegree codeg(v, w) as the number of edges
in E containing both v and w.

Example: We can consider representing a choice of residue classes (ap mod p) as selecting
edges ei ∈ Ei from a collection of hypergraphs (V, Ei). For example, let V = {1, . . . , 9} and
consider the collection of four hypergraphs (V, Ep) for each prime p ≤ 7, where Ep represents the
p distinct residue classes (ap mod p) covering V . In our case, this corresponds to the following
set of edges
 For p = 2, Ep = {{1, 3, 5, 7, 9}, {2, 4, 6, 8}},

23

For p = 3, Ep = {{1, 4, 7}, {2, 5, 8}, {3, 6, 9}},

For p = 5, Ep = {{1, 6}, {2, 7}, {3, 8}, {4, 9}, {5}},

For p = 7, Ep = {{1, 8}, {2, 9}, {3}, {4}, {5}, {6}, {7}},

which can graphically be represented as given in Figure 3.

1
 2

3

4

5
 6
 7
 8

9
 p = 2
 1

2
 3
 4

5
 6
 7
8
 9
 p = 3

1 2

3

4

5
 6
 7

89
 p = 5

1
 2

3
 4

5
 6

7
 8
 9
 p = 7

Figure 3: Graphical representation of a collection of four hypergraphs (V, Ep) for p ∈ {2, 3, 5, 7},
each representing the residue classes for the primes p = 2, 3, 5, 7 over the set of integers
{1, 2, . . . , 9}.

Given that our goal is to eﬃciently cover V by selecting one edge ei from each hypergraph
(V, Ei), we can therefore make the following selection,

e2 = {1, 3, 5, 7, 9} ∈ E2,

e3 = {2, 5, 8} ∈ E3,

e5 = {1, 6} ∈ E5,

e7 = {4} ∈ E7, (22)

which gives the following optimal hypergraph covering, as shown in Figure 4.

1

2
 3

4

5
 6

7

8
 9

Figure 4: Optimal hypergraph covering of V = {1, . . . , 9} using edges selected in (22).

As demonstrated in the above example, we can therefore reduce the problem of eﬃciently
choosing residue classes (ap mod p) for each prime p ≤ x to cover {x + 1, . . . , y}, to a problem
regarding the eﬃcient covering of a hypergraph.

24

With this goal in mind, we therefore aim to use existing ideas from the literature on eﬃcient
hypergraph coverings. Whilst many results on various eﬃcient coverings of hypergraphs have
been published, we shall make particular use of the work done by Pippenger, Spencer [85]. In
1989, they were able to prove the following theorem.

Theorem 10: [85, p. 25] For every k ≥ 2 and δ > 0, there exists some positive integer N and
some δ′ > 0, such that the following theorem holds. Let (V, E) be a hypergraph with |V | > N
and with maximum degree D := max
v∈V d(v),

and such that G satisﬁes the following three conditions:

• (Constant edge size) (V, E) is k-uniform.

• (All degrees approximately the same) For all vertices v ∈ V , we have

d(v) ≥ (1 − δ′)D.

• (Small codegree) For all distinct vertices v, w ∈ V , we have

codeg(v, w) ≤ δ′D.

Then, we have that the following two conditions hold:

• There exists a partitioning of the edges E = ⊔{E1, . . . , Er} such that, for all i = 1, . . . , r,
and for all v ∈ V , v is contained in at most one edge in Ei (i.e. Ei is a packing of V ), and
such that r ≤ (1 + δ)D.

In other words, we have that the chromatic index χ(G) satisﬁes χ(G) ≤ (1 + δ)D.

• There exists a partitioning of the edges E = ⊔{E1, . . . , Er} such that, for all i = 1, . . . , r,
and for all v ∈ V , v is contained in at least one edge in Ei (i.e. Ei is a covering of V ),
and such that r ≥ (1 − δ)D.

An immediate corollary of the above theorem is that there exists a covering C of size

|C| ≤ 1
1 − δ |V |
k , (23)

which is precisely the type of statement we would wish to apply in our application. Note that,
since G is k-uniform, any covering C must have size at least |V |/k, and thus the bound given
in (23) is essentially the best attainable.

The above theorem extends previous results obtained by R¨odl [91] as well as Frankl, R¨odl [33].
A proof of the above theorem is based on the idea of the R¨odl nibble [91], which itself is a variant
of the semi-random method described in [2]. R¨odl came up with this strategy as a response to
the Er˝os-Hanani conjecture [28].

The R¨odl nibble describes an algorithm to produce an eﬃcient packing (and hence an eﬃcient
covering9) of a hypergraph. It goes roughly as follows:

9Note that if we have a packing P of size P ≥ (1 − ϵ)|V |/k, then at most ϵ|V | vertices remain uncovered.
Thus adjoining at most ϵ|V | edges to P , we obtain a covering of size ≤ ϵ|V | + |V |/k.

25

• (First nibble) Select at random a small number of edges with probability ϵ/D. We choose
ϵ small enough such that the edges are unlikely to overlap, therefore obtaining maximal
eﬃciency.

• Then, remove all edges from G that intersect with the edges chosen above in the ﬁrst
nibble.

• (Second nibble) Again, select at random a small number of edges, after which we again
remove any remaining edges from G that intersect with edges chosen in this second nibble.

• Repeat the above procedure, until a suﬃcient number of nibbles are taken to cover most
of the vertices.

Doing the above procedure remarkably yields an eﬃcient hypergraph packing. We also remark
that simply choosing edges independently at random results in requiring around (− log ϵ)|V |/k
edges to cover (1 − ϵ)|V | vertices, which essentially leads to the suboptimal lower bound for
G(x) given in (21). A full discussion describing the R¨odl nibble in further detail can be found
in [3, pp. 58-64].

Unfortunately, we cannot apply Pippenger, Spencer’s result directly as it relies on four crucial
hypotheses, not all of which are satisﬁed in our use case. A slight relaxation of these conditions
was obtained by Kahn [57] in 1996, although the statement of Kahn’s results is not applicable
in a format which we can use.

Upon further analysis of these four hypotheses, we note the following observations.

• The nibbling process is done on a single hypergraph G = (V, E). This condition is
not directly satisﬁed by our application, as we need to choose one edge ei from a collection
of hypergraphs (V, Ei). Fortunately, we have that the proof of Theorem 10 can easily be
modiﬁed in such a way to accommodate this .

• All degrees must be approximately uniform. This condition can be easily be estab-
lished, given that for each vertex v ∈ V , there is exactly one residue class (ap mod p) per
prime p that covers v.

• Codegrees must be small. Again, this condition is easily satisﬁed in our case, with
plenty of room to spare.

• Edges must be of constant size. This is unfortunately the biggest discrepancy be-
tween Pippenger, Spencer’s result and our application, as the size of the residue classes
(ap mod p) can vary considerably for diﬀerent values of p or ap.

If one attempts to directly apply the R¨odl nibble process to a hypergraph with varying edge
sizes, then this results in larger edges being far more likely to be eliminated by the nibbling
process compared to smaller edges, given that larger edges intersect a higher number of vertices.
This presents a clear problem in our application, since the larger edges are precisely those which
we wish to use for an eﬃcient hypergraph covering.

Ford, Green, Konyagin, Maynard, Tao’s solution to the above problem is to reweight the prob-
ability distribution of ei at each step of the nibbling process, so as to give larger edges greater
weight than smaller edges, thus compensating for this bias.

It is this key contribution which is given and proved in [30] and which shall be proved in detail
below.
 26

Covering theorem

Theorem 11: [30, p. 12] There exists a constant C0 ≥ 1 such that the following theorem holds:

Let D, r, A ≥ 1 and 0 < κ ≤ 1, and let m be a non-negative integer. Let δ > 0 satisfy the bound

δ ≤ ( κA

C0eAD
 )10m+2
 . (24)

Let V be a ﬁnite set (considered as the vertex set of a collection of m random hypergraphs)
and let I1, . . . , Im be disjoint ﬁnite non-empty sets, where for each j = 1, . . . , m and i ∈ Ij, we
have ei a random ﬁnite subset of V .

Assume we have the following four conditions:

• (A1) (Edges are bounded in size) For all j = 1, . . . , m, for all i ∈ Ij, and for all e in the
range of ei, we have |e| ≤ r; (25)

• (A2) (Sieve steps are sparse) For all j = 1, . . . , m, for all i ∈ Ij, and for all v ∈ V , we
have the following bound on the probability P(v ∈ ei)

P(v ∈ ei) ≤ δ
|Ij|1/2 ; (26)

• (A3) (Small codegrees) For all j = 1, . . . , m, for all i ∈ Ij, and for any distinct v1, v2 ∈ V ,
we have ∑

i∈Ij P(v1, v2 ∈ ei) ≤ δ; (27)

• (A4) (Degrees are bounded ) For each j = 1, . . . , m, and for every v ∈ V , we deﬁne the
normalised degrees dIj (v) as
 dIj (v) := ∑

i∈Ij P(v ∈ ei) (28)

and then, for each j = 0, 1, . . . , m and each v ∈ V , we recursively deﬁne the quantities
Pj(v) as
 P0(v) := 1 and Pj+1(v) := Pj(v) exp (
− dIj+1(v)
Pj(v)
 ) (29)

for j = 0, . . . , m − 1, and v ∈ V . We then we have the following bound on the normalised
degree dIj (v) as dIj (v) ≤ DPj−1(v) (30)

for all j = 1, . . . , m and v ∈ V , as well as the following lower bound for Pj(v) as

Pj(v) ≥ κ (31)

for all j = 0, . . . , m and v ∈ V .

Then, for each j = 1, . . . , m and for each i ∈ Ij, there exist random variables e′
i such that the
following two properties hold:

1. For each j = 1, . . . , m and i ∈ Ij, ei is either the empty set, or is contained in the range
of ei. In other words, for every e ⊂ V in the range of ei, we have either e = ∅ or
P(ei = e) > 0.
 27

2. For any 0 ≤ J ≤ m and any ﬁnite subset e of V such that |e| ≤ A − 2rJ, we have

P
 

e ⊂ V \
 J⋃

j=1
 ⋃

j∈Ij e
′
i


 = (1 + O(δ1/10J+1)) PJ (e) (32)

where Pj(e) := ∏

v∈e Pj(v). (33)

The full proof of the covering theorem is rather long and technical and uses several standard
results from probability, so we therefore ﬁrst give a summary of the main steps along with what
to apply. The proof is essentially an induction argument and can be summarised as follows:

1. Induct on m. Use the induction hypothesis to obtain random variables e′
i which satisfy
the induction hypothesis for m − 1.

2. Deﬁne the sifted set
 W := V \
 m−1⋃

j=1
 ⋃

i∈Ij e
′
i.

3. For each i ∈ Im, deﬁne random variables e′
i which depend conditionally on W, as follows.
For each W in the range of W, deﬁne the conditional probability distribution of ei as

P(e
′
i = ˜ei | W = W ) :=
 



 1˜ei⊂W
Xi(W ) P(ei = ˜ei)
Pm−1(˜ei) if |Xi(W ) − 1| ≤ δ 1
3×10m ,

0 otherwise,

where Xi(W ) is the normalisation factor

Xi(W ) := E ( 1ei⊂W
Pm−1(ei)
 ) .

4. Prove that e′
i satisﬁes the induction step for m,

P
 (

e ⊂ W\ ⋃

i∈Im e
′
i
)
 = (1 + O(δ 1
10m+1 )) Pm(e).

(a) Use Corollary 17 to prove the normalisation factor Xi(W ) is close to 1 with high
probability.

(b) For a ﬁxed e ⊂ V , and for any W in the range of W, deﬁne the quantity

Y (W ) := P
 (
e ⊂ W \ ⋃

i∈Im e
′
i
 ∣
∣
∣
∣
∣ W = W
 )

so that it suﬃces to calculate EY (W) to prove the induction hypothesis.

(c) Use independence to factorise Y (W ), then use standard probability estimates, includ-
ing the union bound, Taylor expansions, and inclusion-exclusion, to express Y (W )
in terms of P(v ∈ e′
i | W = W ).

(d) Using the deﬁnition of Pm(e) from (33) and (29) as well as bounds on the normalised
degree (30), show that it thus suﬃces to prove that, for all v ∈ e,

∑

i∈Im 1Fi(W)P(v ∈ ei | W) = dIm(v)
Pm−1(v) + O(δ 1
8×10m )

with probability 1 − O(δ 1
7×10m ), conditionally on the event that e ⊂ W. Use that
Xi(W ) tends to 1, to separate this into a main term M and an error term.

28

• Use Corollary 17 to estimate the main term by calculating EM and EM2 .
– To calculate EM, apply the induction hypothesis along with the idempotency
property. Finally, apply the small codegree bound (27) as well as the bound
on the normalised degrees (30).
– To calculate EM2, again apply the induction hypothesis, and use bounds on
the edge size (25), codegree (27), and normalised degree (30) to estimate the
error terms.
• Finally, use the deﬁnition of diJ (v) along with the degree bound diJ (v) ≤
DPj−1(v) and Markov’s inequality to bound the error term.

We now give a full proof of the covering theorem below.

Proof: [30, p. 18] We proceed by induction on m. Note that the base case m = 0 is easily
satisﬁed, since the ﬁrst condition 1 is vacuous, and for the second condition 2, we have that, if
J = 0, then for any ﬁnite subset e of V , we have

P
 

e ⊂ V \
 J⋃

j=1
 ⋃

i∈Ij e
′
i


 = P (e ⊂ V ) = 1.

Setting up the induction

Now, assume that m ≥ 1, and that the theorem holds for m − 1. Thus, by the induction
hypothesis, for each j = 1, . . . , m − 1 and i ∈ IJ , we have the existence of random variables
e′
i obeying the conclusions of the theorem for m − 1. In other words, the ﬁrst condition states
that, for every e in the range of e′
i, either e = ∅ or e lies in the range of ei.

To state the second condition, we consider the following sifted set,

W := V \
 m−1⋃

j=1
 ⋃

i∈Ij e
′
i.

Thus, by the induction hypothesis, we have

P(e ⊂ W) = (1 + O(δ1/10m)
) Pm−1(e) (34)

whenever e ⊂ V such that |e| ≤ A − 2r(m − 1).

To prove the induction step, we need to construct random variables e′
i for each i ∈ Im such that
the range of e′
i is contained in the range of ei along with the empty set, as well as such that

P
 (

e ⊂ W\ ⋃

i∈Im e
′
i
)
 = (1 + O(δ1/10m+1)
) Pm(e) (35)

for each e ⊂ V satisfying |e| ≤ A − 2rm. Note that we must also ensure the implied constant in
the error term of (35) is the same as that given in the error term of (34). We may also assume
that A > 2rm, since otherwise e = ∅, and thus (35) trivially holds since Pm(∅) = 1.

The normalisation factor Xi(W )

Before deﬁning the random variables e′
i for i ∈ Im, we ﬁrst deﬁne a normalisation factor Xi(W),
the properties of which we shall use later on when proving the induction step holds for m. For
each i ∈ Im and for every W in the range of W, we deﬁne the normalisation factor Xi(W ) as

Xi(W ) := E ( 1ei⊂W
Pm−1(ei)
 ) = ∑

˜ei⊂V
 1˜ei⊂W
Pm−1(˜ei) P(ei = ˜ei) = ∑

˜ei⊂W
 P(ei = ˜ei)
Pm−1(˜ei) . (36)

29

As we shall see later on, it is important in our arguments that Xi(W ) tends to 1, in order to
eﬀectively bound the size of P(v ∈ e′
i | W = W ), based on the deﬁnition given in (43). To ease
notation, for each i ∈ Im, we deﬁne Fi(W) as the event that

|Xi(W) − 1| ≤ δ 1
3×10m .

To prove that the normalisation factor Xi(W) tends to 1, we shall prove that Fi(W) occurs
with probability close to 1, using Corollary 17. Speciﬁcally, we shall prove that

P (|Xi(W) − 1| ≤ δ 1
3×10m ) = P(Fi(W)) = 1 − O(δ 1
3×10m )

which, by Corollary 17, implies that it suﬃces to show that both

EXi(W) = 1 + O(δ 1
10m ) and E(Xi(W)
2) = 1 + O(δ 1
10m ).

First, we calculate the expectation of Xi(W) using the induction hypothesis, given in (34),

EXi(W) = ∑

W ⊂V P(W = W )Xi(W ) = ∑

W P(W = W ) ∑

˜ei⊂W
 P(ei = ˜ei)
Pm−1(˜ei)

= ∑

˜ei⊂V
 P(ei = ˜ei)
Pm−1(˜ei)
 ∑

W :˜ei⊂W P(W = W )

= ∑

˜ei
 P(ei = ˜ei)
Pm−1(˜ei) P(ei ⊂ W)

= ∑

˜ei P(ei = ˜ei) · (1 + O(δ1/10m)
)

= 1 + O(δ1/10m), (37)

noting that for all ˜ei in the range of ei, we have |˜ei| ≤ r ≤ A − 2r(m − 1), therefore justifying
the use of (34).

We now similarly calculate the expectation of Xi(W)2 by again applying the induction hypoth-
esis. We ﬁrst note, from the deﬁnition of Pm−1(e) in (33), we have

Pm−1(˜ei ∪ ˆei)
Pm−1(˜ei)Pm−1(ˆei) = 1
Pm−1(˜e ∩ ˆei) .

Furthermore, note that if ˜e ∩ ˆei = ∅, then Pm−1(˜e ∩ ˆei) = 1. Otherwise, in general, we always
have the following lower bound

Pm−1(˜e ∩ ˆei) ≥ Pm−1(˜ei) ≥ ∏

v∈˜ei Pj(v) ≥ ∏

v∈˜ei κ = κ
|e| ≥ κ
r (38)

since κ < 1. This gives an upper bound of
 1
Pm−1(˜e ∩ ˆei) ≤ κ−r. (39)

Using these results, we now calculate E(Xi(W)2) by expanding the square

EXi(W)2 = ∑

W ⊂V P(W = W )Xi(W )
2 = ∑

W P(W = W )
 

 ∑

ei⊂W
 P(ei = ei)
Pm−1(ei)
 



2

= ∑

˜ei
 ∑

ˆei
 P(ei = ˜ei)P(ei = ˆei)
Pm−1(˜ei)Pm−1(ˆei)
 ∑

W :˜ei∪ˆei⊂W P(W = W )

30

= ∑

˜ei
 ∑

ˆei
 P(ei = ˜ei)P(ei = ˆei)
Pm−1(˜ei)Pm−1(ˆei) P(˜ei ∪ ˆei ⊂ W)

= (1 + O(δ1/10m)
) ∑

˜ei
 ∑

ˆei
 P(ei = ˜ei)P(ei = ˆei)
Pm−1(˜ei)Pm−1(ˆei) Pm−1(˜ei ∪ ˆei)

= (1 + O(δ1/10m)
) ∑

˜ei
 ∑

ˆei
 P(ei = ˜ei)P(ei = ˆei)
Pm−1(˜ei ∩ ˆei) , (40)

noting that for all ˜ei, ˆei in the range of ei, we have |˜ei ∪ ˆei| ≤ 2r ≤ A − 2r(m − 1), thus again
justifying the use of (34).

To evaluate the above double sum, we ﬁrst separate the terms based on whether the sets ˜ei and
ˆei are disjoint, then apply the bound obtained in (39) on the latter sum. We then subsequently
apply the bound on P(v ∈ ei) from (26), as well as the bound on |e| from (25) to obtain

∑

˜ei,ˆei
 P(ei = ˜ei)P(ei = ˆei)
Pm−1(˜ei ∩ ˆei) = ∑

˜ei P(ei = ˜ei) ∑

ˆei
 P(ei = ˆei)
Pm−1(˜ei ∩ ˆei)

= ∑

˜ei P(ei = ˜ei)
( ∑

ˆei
ˆei∩˜ei=∅
 P(ei = ˜ei) + ∑

ˆei
ˆei∩˜ei̸=∅
 P(ei = ˆei)
Pm−1(˜ei ∩ ˆei)
 )

= ∑

˜ei P(ei = ˜ei)
( ∑

ˆei P(ei = ˜ei) + ∑

ˆei
ˆei∩˜ei̸=∅
 ( 1
Pm−1(˜ei ∩ ˆei) − 1) P(ei = ˆei)

)

=
 (∑

e⊂V P(ei = e)
)2 + O
(

κ
−r ∑

˜ei P(ei = ˜ei) ∑

ˆei
ˆei∩˜ei̸=∅
 P(ei = ˆei)

)

= 1 + O
(

κ−r ∑

˜ei P(ei = ˜ei) ∑

v∈˜ei P(v ∈ ei)

)

= 1 + O
(

κ−r ∑

˜ei P(ei = ˜ei)rδ
)

= 1 + O (κ
−rrδ) . (41)

Therefore, combining the above two results from (40) and (41), we obtain

E(Xi(W)
2) = (1 + O(δ1/10m)) (
1 + O(rδκ
−r)
) = 1 + O(δ1/10m), (42)

noting that rδκ
−r ≤ Aδκ
−A ≤ δ · δ−1/10m+2 ≤ δ1/10m

from the smallness bound (24) on δ.

Using both (37) and (42), we can therefore now apply Corollary 17 with s = 1 and t = 3. This
gives u = st/(t − 2s) = 3, which proves that

P(Fi(W)) = P (|Xi(W) − 1| ≤ δ 1
3×10m ) = 1 − O(δ 1
3×10m ).

Deﬁning the random variables e′
i

We can now deﬁne the random variables e′
i for each i ∈ Im, conditional on the value of W. If
Fi(W) does not hold, we simply let e′
i = ∅. Otherwise, if Fi(W) holds, we let e′
i take values in

31

the range of ei such that, for each W in the range of W, we deﬁne the conditional probability
distribution as
 P(e
′
i = ˜ei | W = W ) := 1˜ei⊂W
Xi(W ) P(ei = ˜ei)
Pm−1(˜ei) . (43)

Note that, by deﬁnition of the normalisation factor Xi(W ) in (36), we get
∑

˜ei⊂V P(e
′
i = ˜ei | W = W ) = 1.

Thus, for all i ∈ Im, we have that e′
i are well-deﬁned as random variables.

Throughout the remaining parts of the proof, we shall ﬁx some subset e ⊂ V such that |e| ≤
A − 2rm. Let W be in the range of W. Deﬁne Y (W ) as

Y (W ) := P
 (

e ⊂ W \ ⋃

i∈Im e
′
i
 ∣
∣
∣
∣
∣ W = W
 )
 .

Note that, in order to prove the induction step, it suﬃces to calculate the expectation EY (W),
noting that

EY (W) = ∑

W P
 (

e ⊂ W \ ⋃

i∈Im e
′
i
 ∣
∣
∣
∣
∣ W = W
 )
 P(W = W ) = ∑

W P
 (

e ⊂ W \ ⋃

i∈Im e
′
i and W = W
 )

= P
 (

e ⊂ W\ ⋃

i∈Im e
′
i
)
 .

Our main goal of the remaining sections of the proof is to therefore show that

EY (W) = (1 + O(δ 1
10m+1 )
) Pm(e), (44)

which proves the induction step for m.

Calculating the expectation EY (W)

We proceed by calculating the expectation of Y (W), conditionally on the event e ⊂ W. Let W
be in the range of W, and suppose that e ⊂ W . First, note that we can factor Y (W ) as follows

Y (W ) = P
 ( ⋀

i∈Im e ∩ e
′
i = ∅
 ∣
∣
∣
∣
∣ W = W
 )
 = ∏

i∈Im P (e ∩ e
′
i = ∅ ∣
∣ W = W )

= ∏

i∈Im
 (1 − P (e ∩ e
′
i ̸= ∅ ∣
∣ W = W )) ,

noting that the e′
i are conditionally jointly independent for each i ∈ Im.
Now, note that if Fi(W ) fails, then e′
i = ∅ and thus P (e ∩ e′
i ̸= ∅ | W = W ) = 0. Hence, we can
write Y (W ) = ∏

i∈Im
 (1 − 1Fi(W )P (e ∩ e
′
i ̸= ∅ ∣
∣ W = W )) . (45)

We now assume that i ∈ Im and W is such that Fi(W ) holds. Note that, if e ∩ e′
i ̸= ∅, then
there exists some v ∈ e such that v ∈ e′
i. Thus, by the union bound, we have

P (e ∩ e
′
i ̸= ∅ ∣
∣ W = W ) = P
 (⋁

v∈e v ∈ ei
 ∣
∣
∣
∣
∣ W = W
 )

32

≤ ∑

v∈e P (v ∈ ei | W = W ) .

Now, applying the bound on 1/Pm−1(ei) given in (39) and using that Xi(W ) tends to 1 (noting
that Fi(W ) holds by assumption), we have

P (v ∈ e
′
i ∣
∣ W = W ) = P
 

 ⋁

˜ei:v∈˜ei e
′
i = ˜ei
 ∣
∣
∣
∣
∣
∣ W = W
 

 = ∑

˜ei:v∈˜ei P (e
′
i = ˜ei ∣
∣ W = W )

= ∑

ei:v∈˜ei
 1
Xi(W ) P(ei = ˜ei)
Pm−1(˜ei)

≤ 1

1 − δ 1
3×10m · κ
−r ∑

ei:v∈˜ei P(ei = ˜ei)

≪ κ
−r P(v ∈ ei).

We therefore obtain, using the sparseness of sieve step given in (26),

P(e ∩ e
′
i ̸= ∅ | W = W ) ≪ ∑

v∈e κ−r P(v ∈ ei) = κ
−r · |e| · δ
|Im|1/2 ≤ Aκ−rδ
|Im|1/2 .

Now, we use the Taylor expansion for the logarithmic function log(1 + x) = x + O(x2) to obtain
1 + x = ex+O(x2). Applying this to x = −1Fi(W )P (e ∩ e′
i ̸= ∅ | W = W ) we obtain

1−1Fi(W )P (e ∩ e
′
i ̸= ∅ ∣
∣ W = W ) = exp (
−1Fi(W )P (e ∩ e
′
i ̸= ∅ ∣
∣ W = W ) + O ( (Aκ−rδ)2

|Im|
 ))
.

(46)
Putting together (45) and (46), and using that ex = 1 + O(x), we obtain

Y (W ) = ∏

i∈Im exp (−1Fi(W )P (e ∩ e
′
i ̸= ∅ ∣
∣ W = W ) + O ( (Aκ−rδ)2

|Im|
 ))

= exp
 ( ∑

i∈Im
 (
−1Fi(W )P (e ∩ e
′
i ̸= ∅ ∣
∣ W = W ) + O ( (Aκ−rδ)2

|Im|
 )))

= exp
 ( ∑

i∈Im O ( (Aκ−rδ)2

|Im|
 ))
 · exp
 (
−1Fi(W ) ∑

i∈Im P (e ∩ e
′
i ̸= ∅ ∣
∣ W = W ))

= (1 + O((Aκ−rδ)2)
) exp
 (
−1Fi(W ) ∑

i∈Im P (e ∩ e
′
i ̸= ∅ ∣
∣ W = W ))

= (1 + O(δ 1
9×10m )
) exp
 (
−1Fi(W ) ∑

i∈Im P (e ∩ e
′
i ̸= ∅ ∣
∣ W = W ))
 (47)

where the last equality was obtained by noting the bound

δ1− 1
18×10m ≤ δ 1
10m+2 ≤ κA

eAD ≤ κr

A ,

which implies that Aκ−rδ ≤ δ 1
18×10m and thus (Aκ−rδ)2 ≤ δ 1
9×10m .

To get an explicit error term for the probability that e′
i intersects e, we apply the inclusion-
exclusion principle,

P (e ∩ e
′
i ̸= ∅ ∣
∣ W = W ) = P
 (⋁

v∈e v ∈ e
′
i
 ∣
∣
∣
∣
∣ W = W
 )

33

= ∑

∅̸=J⊂e
(−1)
|J|−1 P

( ⋀

vi∈J vi ∈ e
′
i
 ∣
∣
∣
∣
∣ W = W
 )

= ∑

v∈e P (v ∈ e
′
i ∣
∣ W = W ) − O
( ∑

v,w∈e
v̸=w
 P (v, w ∈ e
′
i ∣
∣ W = W ) )
 (48)

where the main term above consists of terms where |J| = 1, whilst the error term encompasses
the remaining terms where |J| ≥ 2.

Our next aim is to show that the above error term is suﬃciently small such that it can be
absorbed into the error term in Y (W ). To calculate the error term above, we let v, w be
distinct vertices in e, and note that

P(v, w ∈ e
′
i | W = W ) = ∑

˜ei:v,w∈˜ei P(e
′
i = ˜ei | W = W ) ≪ κ
−r ∑

˜ei:v,w∈˜ei P(e
′
i = ˜ei)

= κ
−r P(v, w ∈ ei). (49)

Therefore, by summing (49) over all i ∈ Im and all distinct pairs v, w ∈ e, we obtain
∑

i∈Im
 ∑

v,w∈e
v̸=w
 P(v, w ∈ ei | W = W ) ≪ κ−r ∑

v,w∈e
v̸=w
 ∑

i∈Im P(v, w ∈ ei)

≤ κ−r |e|
2 max
v,w∈e
v̸=w
 ∑

i∈Im P(v, w ∈ ei)

≤ κ
−rA2δ

≪ δ 1
9×10m . (50)

Thus, by combining the above three results given in (47), (48) and (50), we therefore obtain

Y (W ) = (1 + O(δ 1
9×10m )
) exp
 (
−1Fi(W ) ∑

i∈Im P(e ∩ e
′
i ̸= ∅ | W = W )
)

= (1 + O(δ 1
9×10m )
) exp
 (
 − 1Fi(W ) ∑

i∈Im
 ∑

v∈e P (v ∈ e
′
i ∣
∣ W = W ) − O( ∑

v,w∈e
v̸=w
 P (v, w ∈ e
′
i ∣
∣ W = W ) ))

= (1 + O(δ 1
9×10m )
) exp
 (
−1Fi(W ) ∑

i∈Im
 ∑

v∈e P (v ∈ e
′
i ∣
∣ W = W ) − O (A2κ−rδ))

= (1 + O(δ 1
9×10m )
) (
1 − O(δ 1
9×10m )) exp
 (

−1Fi(W ) ∑

v∈e
 ∑

i∈Im P(v ∈ e
′
i | W = W )

)

= (1 + O(δ 1
9×10m )
) exp
 (
−1Fi(W ) ∑

v∈e
 ∑

i∈Im P(v ∈ e
′
i | W = W )
)
 . (51)

What remains is to simplify Y (W ) further until we obtain the result given in (44), Therefore,
for the remainder of the proof, we shall aim to prove that, for each v ∈ e, we have

∑

i∈Im 1Fi(W)P(v ∈ e
′
i | W) = dIm(v)
Pm−1(v) + O(δ1/8×10m) (52)

with probability 1 − O(δ 1
7×10m ), conditionally on the event that e ⊂ W.

34

Showing that equation (52) completes the induction

Before proving (52), we ﬁrst show that doing so completes the proof. We ﬁrst note the following
two error bounds:
 |e| · δ 1
8×10m ≤ A · δ 1
8×10m ≤ δ− 1
100×10m · δ 1
8×10m ≤ δ 1
9×10m

and |e| · δ 1
7×10m ≤ A · δ 1
7×10m ≤ δ− 1
100×10m · δ 1
7×10m ≤ δ 1
8×10m ,

where the former is used to bound the error term in the sum below, and the latter is used to
bound the error term for the probability that the sum holds.

Thus, summing equation (52) over all v ∈ e gives us that

∑

v∈e
 ∑

i∈Im 1Fi(W)P(v ∈ e
′
i | W) = ∑

v∈e
 ( dIm(v)
Pm−1(v) + O(δ1/8×10m)
)

= ∑

v∈e
 dIm(v)
Pm−1(v) + |e| · O(δ1/8×10m)

= ∑

v∈e
 dIm(v)
Pm−1(v) + O(δ 1
9×10m )

holds with probability 1 − |e| · O(δ 1
7×10m ) = 1 − O(δ 1
8×10m ) by the union bound, conditionally
on the event that e ⊂ W.

Therefore, using our expression for Y (W ) obtained in (51), we have that the following holds
with probability 1 − O(δ 1
8×10m ), conditionally on e ⊂ W:

Y (W ) = (1 + O(δ 1
9×10m )) exp
 (

−1Fi(W ) ∑

v∈e
 ∑

i∈Im P(v ∈ e
′
i | W = W )
)

= (1 + O(δ 1
9×10m )) exp
 (

− ∑

v∈e
 dIm(v)
Pm−1(v) + O(δ 1
9×10m )
)

= (1 + O(δ 1
9×10m )) exp
 (

− ∑

v∈e
 dIm(v)
Pm−1(v)
 )
 . (53)

For each W in the range of W, let G(W) denote the event such that the above equation (53)
holds. Thus, we have P(G(W) | e ⊂ W) = 1 − O(δ 1
8×10m ).

We now also note the following error bound,

δ 1
9×10m · exp
 (

− ∑

v∈e
 dIm(v)
Pm−1(v)
 )
 ≥ δ 1
9×10m · exp (−AD)

≥ δ 1
9×10m · C0
κA δ 1
10m+2 ≥ δ 1
9×10m · δ 1
10m+2 ≥ δ 1
8×10m . (54)

Therefore, we can ﬁnally calculate the expectation EY (W), by ﬁrst noting that, for every W
in the range of W, we have Y (W ) = 0 if e ̸⊂ W . Thus we need only consider those values of
Y (W) when e ⊂ W. We then consider separately the contribution where G(W) holds and the
contribution where it doesn’t hold.
 35

Then we use (53) applied to the ﬁrst sum, whilst noting that 0 ≤ Y (W ) ≤ 1 for all W to
bound the second sum. The resulting error term obtained can be absorbed into the error term
obtained in (53), noting the bound proven in (54) above. This gives us

EY (W) = E(Y (W)1e⊂W) = P(e ⊂ W) · E(Y (W) | e ⊂ W)

= P(e ⊂ W)
 

 ∑

W : G(W ) Y (W )P(W = W | e ⊂ W) + ∑

W : ¬ G(W ) Y (W )P(W = W | e ⊂ W)




= P(e ⊂ W)
 (
(1 + O(δ 1
9×10m )
) exp
 (
− ∑

v∈e
 dIm(v)
Pm−1(v)
 )
 P(G(W) | e ⊂ W) + O(P(¬ G(W) | e ⊂ W))

)

= P(e ⊂ W)
 (
(1 + O(δ 1
9×10m )
) exp
 (
− ∑

v∈e
 dIm(v)
Pm−1(v)
 ) (1 − O(δ 1
8×10m )) + O(δ 1
8×10m )

)

= P(e ⊂ W)
 (
(1 + O(δ 1
9×10m )
) exp
 (
− ∑

v∈e
 dIm(v)
Pm−1(v)
 )
 + O(δ 1
8×10m )
)

= (1 + O(δ 1
10m )
) Pm−1(e)
 ((1 + O(δ 1
9×10m )
) exp
 (

− ∑

v∈e
 dIm(v)
Pm−1(v)
 )
 + O(δ 1
8×10m )

)

= (1 + O(δ 1
10m+1 ) Pm−1(e) exp
 (

− ∑

v∈e
 dIm(v)
Pm−1(v)
 )

= (1 + O(δ 1
10m+1 ) Pm(e).

This therefore proves (44), and thus proves the induction step for m, thus completing the proof.

What remains is to prove that equation (52) holds with probability 1 −O(δ 1
8×10m ), conditionally
on the event e ⊂ W.

Proving equation (52) holds

Firstly, by the deﬁnition given in (43), we have

1Fi(WP(v ∈ ei | W) = 1Fi(W ∑

˜ei:v∈˜ei P(ei = ˜ei | W) = 1Fi(W )
Xi(W )
 ∑

˜ei:v∈˜ei 1˜ei∈W P(ei = ˜ei)
Pm−1(˜ei) . (55)

Also, note that for every W in the range of W, we have

1Fi(W )
Xi(W ) =
 {
1 + O(δ 1
3×10m ) if Fi(W ) holds,
0 otherwise.

This therefore implies that
 1Fi(W)
Xi(W) = 1 + O (1 − 1Fi(W) + δ 1
3×10m ) . (56)

Substituting both (55) and (56) into the left hand side of (52) yields

∑

i∈Im 1Fi(W)P(v ∈ e
′
i | W) = ∑

i∈Im
 1Fi(W)
Xi(W)
 ∑

˜ei:v∈˜ei 1˜ei∈W P(ei = ˜ei)
Pm−1(˜ei)

= ∑

i∈Im
 (1 + O(1 − 1Fi(W) + δ 1
3×10m )
) ∑

˜ei:v∈˜ei 1˜ei∈W P(ei = ˜ei)
Pm−1(˜ei)

36

= ∑

i∈Im
 ∑

˜ei:v∈˜ei 1˜ei∈W P(ei = ˜ei)
Pm−1(˜ei) (57)

+ ∑

i∈Im O(1 − 1Fi(W) + δ 1
3×10m ) ∑

˜ei:v∈˜ei 1˜ei∈W P(ei = ˜ei)
Pm−1(˜ei) . (58)

We now have the left hand side expressed in terms of a main term (57) and error term (58).
We shall ﬁrst estimate the error term, then calculate the main term.

Calculating the error term

For ease of notation, we denote the error bound given in (58) as H(W),

H(W) := ∑

i∈Im O (1 − 1Fi(W) + δ 1
3×10m ) ∑

˜ei:v∈˜ei 1˜ei∈W P(ei = ˜ei)
Pm−1(˜ei) .

Using the bound on Pm−1(˜ei) given in (39), as well as the deﬁnition of dIm(v), we obtain

H(W) ≪ κ
−r ∑

i∈Im
 (1 − 1Fi(W) + δ 1
3×10m ) ∑

˜ei:v∈˜ei P(ei = ˜ei)

= κ−r ∑

i∈Im
 (1 − 1Fi(W) + δ 1
3×10m ) P(v ∈ ei).

For each i ∈ Im, we can calculate the unconditional expectation of 1 − 1Fi(W) + δ 1
3×10m as

E (1 − 1Fi(W) + δ 1
3×10m ) = 1 − E1Fi(W) + δ 1
3×10m = 1 − PFi(W) + δ 1
3×10m = O(δ 1
3×10m ).

Calculating the unconditional expectation of the error term, we therefore have

EH(W) ≪ κ−r ∑

i∈Im E (1 − 1Fi(W) + δ 1
3×10m ) P(v ∈ ei) ≪ κ
−rδ 1
3×10m ∑

i∈Im P(v ∈ ei)

= κ−rdIm(v) δ 1
3×10m .

Thus, calculating the conditional expectation, tied to the event e ⊂ W, we have

E (H(W) | e ⊂ W) ≤ EH(W)
P(e ⊂ W) ≪ κ
−r dIm(v)
Pm−1(e) δ 1
3×10m ≤ κ
−rDδ 1
3×10m ≪ κ−Aδ 1
3×10m .

Note that, by deﬁnition, H(W) is a non-negative random variable. Thus, applying Markov’s
inequality, we have

P (H(W) < δ 1
7×10m ∣
∣
∣ e ⊂ W) ≥ 1 − E (H(W) | e ⊂ W)

δ 1
7×10m = 1 − O(δ 1
7×10m ). (59)

Therefore, we have that the error term of H(W), conditional on e ⊂ W, is O(δ 1
7×10m ) with
probability 1 − O(δ 1
7×10m ).

Calculating the main term

Given the bounds obtained on the error term H(W) above, it suﬃces to prove that the main
term satisﬁes ∑

i∈Im
 ∑

˜ei:v∈˜ei 1˜ei∈W P(ei = ˜ei)
Pm−1(˜ei) = dIm(v)
Pm−1(v) + O(δ 1
8×10m )

37

with probability 1 − O(δ 1
7×10m ), conditionally on the event that e ⊂ W.

By making use of a conditional version of Corollary 17 (where we replace EX with E(X | E),
and EX2 with E(X2 | E), where E denotes the event e ⊂ W), it suﬃces to show that

E
 

 ∑

i∈Im
 ∑

˜ei:v∈˜ei 1˜ei∈W P(ei = ˜ei)
Pm−1(˜ei)
 ∣
∣
∣
∣
∣
∣ e ⊂ W


 = dIm(v)
Pm−1(v) + O(δ 1
2×10m ) (60)

and E
 

( ∑

i∈Im
 ∑

˜ei:v∈˜ei 1˜ei∈W P(ei = ˜ei)
Pm−1(˜ei)
 )2 ∣
∣
∣
∣
∣
∣ e ⊂ W


 = ( dIm(v)
Pm−1(v)
 )2 + O(δ 1
2×10m ). (61)

To calculate the expectation, we ﬁrst note that, for any i ∈ Im, and any ﬁxed e ⊂ V and ˜ei in
the range of W, we have

E(1˜ei⊂W | e ⊂ W) = P(˜ei ⊂ W | e ⊂ W) = P(˜ei ⊂ W ∧ e ⊂ W)
P(e ⊂ W) = P(˜ei ∪ e ⊂ W)
P(e ⊂ W) .

Furthermore, from the induction hypothesis (34), and using that (1 + O(x))−1 = 1 + O(x), we
have
 P(˜ei ∪ e ⊂ W)
P(e ⊂ W) =
 (1 + O(δ1/10m)
) Pm−1(e ∪ ˜ei)
(1 + O(δ1/10m)
) Pm−1(e) = (1 + O(δ1/10m)) Pm−1(e ∪ ˜ei)
Pm−1(e) ,

noting that |e ∪ ˜ei| ≤ 2r < A − 2r(m − 1). Also, by deﬁnition of P , we have, for every v ∈ e ∩ ˜ei,

Pm−1(e ∪ ˜ei)
Pm−1(˜ei)Pm−1(e) = 1
Pm−1(e ∩ ˜ei) = 1
Pm−1(v)Pm−1(˜ei ∩ e\{v}) .

Thus, putting the above together, we obtain that

E
 

 ∑

i∈Im
 ∑

˜ei:v∈˜ei 1˜ei∈W P(ei = ˜ei)
Pm−1(˜ei)
 ∣
∣
∣
∣
∣
∣ e ⊂ W


 = ∑

i∈Im
 ∑

˜ei:v∈˜ei E(1˜ei∈W | e ⊂ W) P(ei = ˜ei)
Pm−1(˜ei)

= ∑

i∈Im
 ∑

˜ei:v∈˜ei
 P(˜ei ∪ e ⊂ W)
P(e ⊂ W) P(ei = ˜ei)
Pm−1(˜ei)

= (1 + O(δ1/10m)
) ∑

i∈Im
 ∑

˜ei:v∈˜ei
 Pm−1(e ∪ ˜ei)
Pm−1(e) P(ei = ˜ei)
Pm−1(˜ei)

= 1 + O(δ1/10m)
Pm−1(v)
 ∑

i∈Im
 ∑

˜ei:v∈˜ei
 P(ei = ˜ei)
Pm−1(˜ei ∩ e\{v}) . (62)

To evaluate the double sum in (62) above, we ﬁrst note that, if ˜ei and e\{v} are disjoint, then
P (˜ei ∩ e\{v}) = 1. Otherwise, we always have the lower bound P (˜ei ∩ e\{v}) ≥ κr, due to (39).
Therefore, by doing a similar argument as done in (41), where we separate the inner sum based
on whether the sets ˜ei and e\{v} are disjoint, we obtain the following bound,

∑

i∈Im
 ∑

˜ei:v∈˜ei
 P(ei = ˜ei)
Pm−1(˜ei ∩ e\{v}) = ∑

i∈Im
 ( ∑

˜ei:v∈˜ei
˜ei∩e\{v}=∅
 P(ei = ˜ei) + ∑

˜ei:v∈˜ei
˜ei∩e\{v}̸=∅
 P(ei = ˜ei)
Pm−1(˜ei ∩ e\{v})
 )

= ∑

i∈Im
 ∑

˜ei:v∈˜ei P(ei = ˜ei) + O
(
κ
−r ∑

i∈Im
 ∑

˜ei:v∈˜ei
˜ei∩e\{v}̸=∅
 P(ei = ˜ei)

)

38

= ∑

i∈Im P(v ∈ ei) + O
(

κ−r ∑

i∈Im
 ∑

w∈e\{v}
 ∑

˜ei:v,w∈˜ei P(ei = ˜ei)
)

= dIm(v) + O
(
κ
−r ∑

i∈Im
 ∑

w∈e\{v} P(v, w ∈ ei)
)

= dIm(v) + O
(
κ
−r ∑

w∈e\{v} δ
)

= dIm(v) + O(Aδκ
−r). (63)

Putting together the results from (62) and (63), we obtain

E
 

 ∑

i∈Im
 ∑

˜ei:v∈˜ei 1˜ei∈W P(ei = ˜ei)
Pm−1(˜ei)
 ∣
∣
∣
∣
∣
∣ e ⊂ W


 = (1 + O(δ1/10m))
Pm−1(v) (dIm(v) + O(Aδκ
−r)
)

= dIm(v)
Pm−1(v) + O(Dδ 1
10m ) + O(Aδκ
−r−1) + O(δ 1
10m Aδκ
−r−1)

= dIm(v)
Pm−1(v) + O(δ 1
2×10m )

which proves (60). By a similar, albeit more lengthy argument, we can similarly calculate the
expectation of the square of the main term. Again, we ﬁrst note that, for any ˜ei, ˆei in the range
of W, we have

E(1˜ei⊂W1ˆei⊂W | e ⊂ W) = P(˜ei ⊂ W ∧ ˆei ⊂ W | e ⊂ W) = P(˜ei ⊂ W ∧ ˆei ⊂ W ∧ e ⊂ W)
P(e ⊂ W)

= P(˜ei ∪ ˆei ∪ e ⊂ W)
P(e ⊂ W)

as well as

P(˜ei ∪ ˆei ∪ e ⊂ W)
P(e ⊂ W) =
 (1 + O(δ1/10m)
) Pm−1(e ∪ ˜ei ∪ ˆei)
(1 + O(δ1/10m)
) Pm−1(e) = (1 + O(δ1/10m)) Pm−1(e ∪ ˜ei ∪ ˆei)
Pm−1(e) .

Furthermore, by inclusion-exclusion, we have

Pm−1(v)2Pm−1(˜ei ∪ ˆei ∪ e)
Pm−1(˜ei)Pm−1(ˆei)Pm−1(e) = Pm−1(v)2Pm−1(˜ei ∩ ˆei ∩ e)
Pm−1(˜ei ∩ ˆei)Pm−1(ˆei ∩ e)Pm−1(˜ei ∩ e)

= Pm−1(˜ei ∩ ˆei ∩ e)
Pm−1(˜ei ∩ ˆei)Pm−1(ˆei ∩ e\{v})Pm−1(˜ei ∩ e\{v}) (64)

where, for ease of notation, we denote the ratio in (64) above as R(˜ei, ˆei).

Therefore, if ˜ei ∩ ˆei = ˜ei ∩ e = ˆei ∩ e = {v} (i.e. the only common element amongst any two of
˜ei, ˆei and e is v), then we have R(˜ei, ˆei) = 1. Otherwise, in general, we always have that

Pm−1(˜ei ∩ ˆei ∩ e)
Pm−1(˜ei ∩ ˆei)Pm−1(ˆei ∩ e\{v})Pm−1(˜ei ∩ e\{v}) ≤ 1
Pm−1(˜e)Pm−1(ˆei) ≤ κ
−2r

Therefore, we can rewrite the left-hand side of (61) as

E
 



( ∑

i∈Im
 ∑

˜ei:v∈˜ei 1˜ei∈W P(ei = ˜ei)
Pm−1(˜ei)
 )2 ∣
∣
∣
∣
∣
∣ e ⊂ W




39

= E
 



 ∑

i,i′∈Im
 ∑

˜ei:v∈˜ei
ˆei:v∈ˆei
 1˜ei∈W P(ei = ˜ei)
Pm−1(˜ei) 1ˆei∈W P(ei′ = ˆei)
Pm−1(ˆei)
 ∣
∣
∣
∣
∣
∣
∣
∣
 e ⊂ W






= ∑

i,i′∈Im
 ∑

˜ei:v∈˜ei
ˆei:v∈ˆei
 E(1˜ei⊂W1ˆei⊂W | e ⊂ W) P(ei = ˜ei)P(ei′ = ˆei)
Pm−1(˜ei)Pm−1(ˆei)

= ∑

i,i′∈Im
 ∑

˜ei:v∈˜ei
ˆei:v∈ˆei
 (1 + O(δ1/10m)) Pm−1(e ∪ ˜ei ∪ ˆei)
Pm−1(e) P(ei = ˜ei)P(ei′ = ˆei)
Pm−1(˜ei)Pm−1(ˆei)

= 1 + O(δ1/10m)
Pm−1(v)2 ∑

i,i′∈Im
 ∑

˜ei:v∈˜ei
ˆei:v∈ˆei
 P(ei = ˜ei)P(ei′ = ˆei) Pm−1(v)2Pm−1(e ∪ ˜ei ∪ ˆei)
Pm−1(˜ei)Pm−1(ˆei)Pm−1(ei) . (65)

As before, we now aim to separate terms from the inner sum depending on whether or not
we have R(˜ei, ˆei) = 1. First, we note that we can bound the contribution from terms where
R(˜ei, ˆei) ̸= 1 by applying the union bound twice, as follows,
∑

˜ei:v∈˜ei
ˆei:v∈ˆei
R(˜ei,ˆei)̸=1
 1 ≤ ∑

˜ei:v∈˜ei
ˆei:v∈ˆei
˜ei∩e\{v}̸=∅
 1 + ∑

˜ei:v∈˜ei
ˆei:v∈ˆei
ˆei∩e\{v}̸=∅
 1 + ∑

˜ei:v∈˜ei
ˆei:v∈ˆei
˜ei∩ˆei\{v}̸=∅
 1

≤ ∑

ˆei:v∈ˆei
 ∑

w∈e\{v}
 ∑

˜ei:v,w∈˜ei 1 + ∑

˜ei:v∈˜ei
 ∑

w∈e\{v}
 ∑

ˆei:v,w∈ˆei 1 + ∑

˜ei:v∈˜ei
 ∑

w∈˜ei\{v}
 ∑

ˆei:v,w∈ˆei 1.

Now, separating terms where R(˜ei, ˆei) = 1 from those where R(˜ei, ˆei) ̸= 1, and applying the
above bound, we obtain
∑

i,i′∈Im
 ∑

˜ei:v∈˜ei
ˆei:v∈ˆei
 P(ei = ˜ei)P(ei′ = ˆei) Pm−1(v)2Pm−1(e ∪ ˜ei ∪ ˆei)
Pm−1(˜ei)Pm−1(ˆei)Pm−1(ei)

= ∑

i,i′∈Im
 






 ∑

˜ei:v∈˜ei
ˆei:v∈ˆei
R(˜ei,ˆei)=1
 P(ei = ˜ei)P(ei′ = ˆei) + ∑

˜ei:v∈˜ei
ˆei:v∈ˆei
R(˜ei,ˆei)̸=1
 R(˜ei, ˆei)P(ei = ˜ei)P(ei′ = ˆei)









= ∑

i,i′∈Im
 



 ∑

˜ei:v∈˜ei
ˆei:v∈ˆei
 P(ei = ˜ei)P(ei′ = ˆei) + O
(

κ
−r ∑

ˆei:v∈ˆei
 ∑

w∈e\{v}
 ∑

˜ei:v,w∈˜ei P(ei = ˜ei)P(ei′ = ˆei)
)

+ O
(
κ
−r ∑

˜ei:v∈˜ei
 ∑

w∈e\{v}
 ∑

ˆei:v,w∈ˆei P(ei = ˜ei)P(ei′ = ˆei)

)

+O
(
κ
−r ∑

˜ei:v∈˜ei
 ∑

w∈˜ei\{v}
 ∑

ˆei:v,w∈ˆei P(ei = ˜ei)P(ei′ = ˆei)

)



= ∑

i,i′∈Im
 ∑

˜ei:v∈˜ei
ˆei:v∈ˆei
 P(ei = ˜ei)P(ei′ = ˆei) + O
(
κ
−r ∑

i,i′∈Im
 ∑

w∈e\{v}
 ∑

ˆei:v∈ˆei
 ∑

˜ei:v,w∈˜ei P(ei = ˜ei)P(ei′ = ˆei)
)

+ O
(

κ−r ∑

i,i′∈Im
 ∑

w∈e\{v}
 ∑

˜ei:v∈˜ei
 ∑

ˆei:v,w∈ˆei P(ei = ˜ei)P(ei′ = ˆei)

)

40

+ O
(
κ
−r ∑

i,i′∈Im
 ∑

˜ei:v∈˜ei
 ∑

w∈˜ei\{v}
 ∑

ˆei:v,w∈ˆei P(ei = ˜ei)P(ei′ = ˆei)

)
.

(66)

We easily note that the main term evaluates to
∑

i,i′∈Im
 ∑

˜ei:v∈˜ei
ˆei:v∈ˆei
 P(ei = ˜ei)P(ei′ = ˆei) = ∑

i,i′∈Im P(v ∈ ei)P(v ∈ ei′) =
 ( ∑

i∈Im P(v ∈ ei)
)2 = dIm(v)
2.

(67)

We now obtain three error terms, which we bound. The ﬁrst error term can be estimated as
∑

i,i′∈Im
 ∑

w∈e\{v}
 ∑

ˆei:v∈ˆei
 ∑

˜ei:v,w∈˜ei P(ei = ˜ei)P(ei′ = ˆei) = ∑

i,i′∈Im
 ∑

w∈e\{v} P(v, w ∈ ei)P(v ∈ ei′)

= ∑

i′∈Im P(v ∈ ei′) ∑

w∈e\{v}
 ∑

i∈Im P(v, w ∈ ei)

= dIm(v) ∑

w∈e\{v}
 ∑

i∈Im P(v, w ∈ ei)

≤ DPm−1(v) · ∑

w∈e\{v} δ

≤ DAδ. (68)

By an analogous argument, we similarly obtain the bound for the second error term as
∑

i,i′∈Im
 ∑

w∈e\{v}
 ∑

˜ei:v∈˜ei
 ∑

ˆei:v,w∈ˆei P(ei = ˜ei)P(ei′ = ˆei) ≤ DAδ. (69)

Finally, we bound the third term
∑

i,i′∈Im
 ∑

˜ei:v∈˜ei
 ∑

w∈˜ei\{v}
 ∑

ˆei:v,w∈ˆei P(ei = ˜ei)P(ei′ = ˆei) = ∑

i,i′∈Im
 ∑

˜ei:v∈˜ei P(ei = ˜ei) ∑

w∈˜ei\{v} P(v, w ∈ ei′)

≤ ∑

i∈Im
 ∑

˜ei:v∈˜ei P(ei = ˜ei) ∑

w∈˜ei\{v} δ

≤ ∑

i∈Im
 ∑

˜ei:v∈˜ei P(ei = ˜ei)δr

= δr ∑

i∈Im P(v ∈ ei)

≤ δrdIm(v)

≤ Drδ. (70)

Finally, putting together the results obtained in (65) and (66), using the calculation for the
main term in (67), as well as the bounds for the error terms calculated in (68), (69), and (70)
above, we obtain

E
 


( ∑

i∈Im
 ∑

˜ei:v∈˜ei 1˜ei∈W P(ei = ˜ei)
Pm−1(˜ei)
 )2 ∣
∣
∣
∣
∣
∣ e ⊂ W


 = 1 + O(δ1/10m)
Pm−1(v)2 (dIm(v)
2 + O(DAδ)
)

= dIm(v)2

Pm−1(v)2 + O(δ 1
2×10m ).

which proves (61).
 41

Therefore, applying Corollary 17 using s = 2 and t = 8, we have ﬁnally proven that
∑

i∈Im
 ∑

˜ei:v∈˜ei 1˜ei⊂W P(ei = ˜ei)
Pm−1(˜ei) = dIm(v)
Pm−1(v) + O(δ 1
8×10m ) (71)

with probability 1 − O(δ 1
7×10m ), conditional on the event that e ⊂ W.

Finishing the proof

Using the triangle inequality, we now combine the results obtained from (71) and (59) to get
that, for each v ∈ e, we have
∑

i∈Im 1Fi(W)P(v ∈ e
′
i | W) = ∑

i∈Im
 ∑

˜ei:v∈˜ei 1˜ei∈W P(ei = ˜ei)
Pm−1(˜ei) + H(W) = dIm(v)
Pm−1(v) + O(δ 1
8×10m )

with probability 1 − 2 · O(δ 1
7×10m ) = 1 − O(δ 1
7×10m ), on condition that e ⊂ W.

This therefore proves equation (52) and thus, by the arguments given in the previous section,
this ﬁnally completes the proof of the covering theorem.

Applying the covering theorem

Both the statement and proof of Theorem 11 is formulated in a rather general probabilistic
fashion, and does not at ﬁrst seem to share much similarity with Pippenger and Spencer’s
result given in Theorem 10. However, we do note that one can prove a special case of The-
orem 11 given in a purely combinatorial fashion which generalises Theorem 10. This is given
as Corollary 2 in an earlier draft of Ford, Green, Konyagin, Maynard, and Tao’s paper [29, p. 13].

For our purposes, we shall now prove a speciﬁc corollary, which is applicable to our problem of
eﬃciently covering Py ∩ S(⃗a) by residue classes (ap mod p) from large primes p ∈ P4.

Corollary 12: [30, p. 13] For suﬃciently large x, we have the following holds. Let P, Q be
sets with |P| ≤ x and (log2 x)3 < |Q| ≤ x100. For each p ∈ P, let ep be a random subset of Q
satisfying the following four conditions:

• (B1) (Size is bounded ) For each p ∈ P,

|ep| ≤ log x log3 x
(log2 x)2 ;

• (B2) (Sparse sieve step) For all p ∈ P and q ∈ Q, we have

P(q ∈ ep) ≤ x−3/5;

• (B3) (Small codegrees) For any distinct q1, q2 ∈ Q, we have
∑

p∈P P(q1, q2 ∈ ep) ≤ x
−1/20;

• (B4) There exists some positive constant C satisfying

5
4 log 5 ≤ C (72)

such that, for all but at most O( 1
(log2 x)2 |Q|
) elements q ∈ Q, we have

∑

p∈P P(q ∈ ep) = C + O ( 1
(log2 x)2
 ) . (73)

42

Then for any positive integer m such that

m ≤ log3 x
log 5 , (74)

we can ﬁnd random sets e′
p ⊂ Q for each p ∈ P such that e′
p is either empty or some subset of
Q which ep attains with positive probability, and that

|{q ∈ Q : q ̸∈ e
′
p for all p ∈ P}| ∼ 5−m|Q| (75)

with positive probability.

Remark: It’s worth noting that the x100 bound on |Q| is completely arbitrary. The corollary
statement holds for any polynomial bound on Q, however, when applying the corollary, we only
need the much weaker bound of |Q| ≤ π(y).

The proof of the above corollary is a relatively straightforward application of the covering
theorem. To give an overview, we partition some subset of P into m disjoint sets I1, . . . , Im
deﬁned such that the hypotheses of the covering theorem hold. We then give suitable values for
the parameters D, r, A, κ, δ, a summary of which is given below

D := 2 log 5, r := log x log3 x
(log2 x)2 , A := 2rm + 2, κ := 1
2 log2 x , and δ := x−1/20.

We then simply check each of the four hypotheses of the covering theorem. The ﬁrst three con-
ditions follow almost immediately, and the fourth condition can be proven without too much
trouble by deﬁning suitable random variables given in equation (77), and applying Hoeﬀding’s
inequality.

Finally, after checking that δ satisﬁes the smallness bound, we apply the covering theorem to
obtain random variables e′
p satisfying (32). Making use of (32) with sets e ⊂ V of size 1 and 2,
along with Lemma 16, gives the ﬁnal result shown in (75).

We now give a full proof of the corollary.

Proof: Our main aim is to apply the covering theorem with V = Q. First, we shall prove
that it suﬃces to only consider those elements in Q which satisfy condition (B4), given in (73).
Therefore, let C be as given in (72) and deﬁne

Q
′ :=
 



q ∈ Q : ∑

p∈P P(q ∈ ep) = C + O ( 1
(log2 x)2
 )


 ,

noting that |Q′| ≥ (1 − O( 1
(log2 x)2 )
) |Q|, thus |Q′| ∼ |Q|.

We consider m disjoint intervals I1, I2, . . . , Im in [0, 1] deﬁned as follows. We recursively deﬁne
the sequence of non-negative real numbers r0, r1, . . . , rm by

r0 = 0 and ri+1 = ri + log 5
C · 5i

for all i = 0, . . . , m − 1. We then deﬁne the sequence of disjoint intervals I1, . . . , Im as In =
[rn−1, rn) for all n = 1, . . . , m, as illustrated below.

0 1r1 r2 r3 r4

I1 I2 I3 I4 . . .

43

Note that
 rm =
 m−1∑

i=0
 log 5
C · 5i = log 5
C
 ( 1 − (1/5)m

1 − 1/5
 ) < log 5
C · 5
4 ≤ 1

thus all the intervals Ii fall within [0, 1]. We now deﬁne ⃗t = (tp)p∈P as a tuple of |P| independent
random variables, each of which is a continuous uniform random variable drawn from the interval
[0, 1]. For each j = 1, . . . , m, we now deﬁne the random sets Ij(⃗t), dependent on ⃗t, as

Ij(⃗t) := {p ∈ P : tp ∈ Ij}. (76)

This is illustrated below, where each dot represents an element in P.

0 1r1 r2 r3 r4

I1 I2 I3 I4 . . .

⃗t :
 I1(⃗t) I2(⃗t) I3(⃗t) I4(⃗t)
 . . .

Note that the intervals Ij being disjoint clearly implies that the sets Ij(⃗t) are disjoint.

Checking the ﬁrst three conditions of covering theorem

Our task is to now verify the hypotheses of the covering theorem so that we may apply the
theorem with an appropriate choice of the relevant parameters.

Firstly, let r := log x log3 x
(log2 x)2 .

Thus, by deﬁnition, we have that condition (A1) is satisﬁed. Now, let δ = x−1/20. Note that
|Ij|1/2 ≤ |P|1/2 ≤ x1/2 ≤ x0.55. Thus, for all p ∈ P and q ∈ Q, we have

P(q ∈ ep) ≤ x−3/5 = x−1/20

x0.55 ≤ δ
|Ij|1/2

which proves condition (A2) is satisﬁed. By deﬁnition of δ, we clearly have that
∑

p∈P P(q1, q2 ∈ ep) ≤ x−1/20 = δ

for any distinct q1, q2 ∈ Q, which shows that (A3) is satisﬁed.

Checking the fourth condition of covering theorem

Now, to verify the fourth condition (A4), for each q ∈ Q′ and j = 1, . . . , m, we deﬁne the
random variables X(q,j)
p (dependent on ⃗t), as

X(q,j)
p (⃗t) =
 {
P(q ∈ ep) if p ∈ Ij(⃗t),
0 otherwise. (77)

Thus, we have that X(q,j)
p (⃗t) only takes two possible values: P(q ∈ ep) with probability P(p ∈
Ij(⃗t)) and 0 with probability 1−P(p ∈ Ij(⃗t)). Therefore, calculating the expectation of X(q,j)
p (⃗t)
is simply EX(q,t)
p (t) = P(q ∈ ep) · P(p ∈ Ij(⃗t)) + 0 = |Ij| · P(q ∈ ep),

44

noting that P(p ∈ Ij(⃗t)) = |Ij| by uniformity.

Thus, summing the expectation over all p ∈ P yields

∑

p∈P EX(q,t)
p (⃗t) = |Ij| · ∑

p∈P P(q ∈ ep) = 51−j log 5
C
 (
C + O ( 1
(log2 x)2
 ))

= 5
1−j log 5 + O ( log 5
C(log2 x)2
 )

= 5
1−j log 5 + O ( 4/5
(log2 x)2
 ) ,

noting that log 5/C ≤ 4/5, by condition (72). We now deﬁne the sequence of p random variables
Z(q,t)
p (⃗t) given by Z
(q,t)
p (⃗t) := X(q,t)
p (⃗t) − EX
(q,t)
p (⃗t).

To obtain a bound on |Z(q,t)
p (⃗t)|, we note the range of X
(q,t)
p satisﬁes

0 ≤ X
(q,t)
p (⃗t) ≤ P(q ∈ ep) ≤ x−3/5,

and thus |Z(q,t)
p (⃗t)| = |X(q,t)
p (⃗t) − EX(q,t)
p (⃗t)| ≤ x−3/5 − 0 = x−3/5.

We can now apply Hoeﬀding’s inequality to the sequence of |P| random variables (Z(q,t)
p (⃗t))p∈P
Note that, by deﬁnition EZ
(q,t)
p (⃗t) = 0, hence we obtain the following bound,

P
 


 ∣
∣
∣
∣
∣
∣
∑

p∈P Z(q,t)
p (⃗t)

∣
∣
∣
∣
∣
∣ ≥ 1
(log2 x)2
 

 ≤ 2 exp
 (

− (log2 x)−4

2 ∑
p∈P (x−3/5)2
 )

= 2 exp (
− (log2 x)−4

2 · |P| · x−6/5
 )

≤ 2 exp
 (

− x−1/5

2(log2 x)4
 )

≤ 1
x200 ,

where the last inequality follows for x suﬃciently large (indeed we have this inequality for any
fractional power of x).

Thus, noting that we have |Q′| ≤ x100 and m ≤ log3 x/ log 5, this proves that

P
 

 ⋁

q∈Q′
 ⋁

j∈{1,...,m}
 


 ∣
∣
∣
∣
∣
∣
∑

p∈P Z(q,t)
p (⃗t)

∣
∣
∣
∣
∣
∣ ≥ 1
(log2 x)2
 





 ≤ ∑

q∈Q′
 m∑

j=1
 1
x200

≤ x100 · log3 x
log 5 · 1
x200

= log3 x
log 5 · x100

which tends to 0 as x → ∞. Thus, for suﬃciently large x, we have that the probability on the
left hand-side is strictly less than 1, which implies there exists some possible outcome ⃗t of ⃗t,
occurring with non-zero probability, such that, for this choice ⃗t, we have
∣
∣
∣
∣
∣
∣
∑

p∈P Z(q,t)
p (⃗t)
∣
∣
∣
∣
∣
∣ < 1
(log2 x)2

45

for every q ∈ Q′ and every j ∈ {1, . . . , m}. We now ﬁx this choice ⃗t of ⃗t, to obtain
∣
∣
∣
∣
∣
∣
∑

p∈P X(q,t)
p (⃗t)

∣
∣
∣
∣
∣
∣ = ∑

p∈P EX
(q,t)
p (⃗t) + ∑

p∈P
 (X(q,t)
p (⃗t) − EX(q,t)
p (⃗t))

= ∑

p∈P EX(q,t)
p (⃗t) + O
 


 ∣
∣
∣
∣
∣
∣
∑

p∈P Z(q,t)
p (⃗t)
∣
∣
∣
∣
∣
∣
 



= 5
1−j log 5 + O ( 4/5
(log2 x)2
 ) + O ( 1
(log2 x)2
 )

= 5
1−j log 5 + O ( 1
(log2 x)2
 ) .

Now, calculating the normalised degrees dIj (q) deﬁned in (28), we obtain

dIj (q) = ∑

p∈Ij (⃗t) P(q ∈ ep) = 5
1−j log 5 + O ( 1
(log2 x)2
 )

= (
1 + O( 5j−1

(log2 x)2
 )) 5
1−j log 5

= (
1 + O( 1
log2 x
 )) 5
1−j log 5

noting that 5m ≤ 5(log3 x/ log 5) = log2 x.
We now prove by induction that

Pj(q) = (
1 + O( 4j

log2 x
 )) 5−j (78)

for all j = 0, . . . , m.
For the base case, j = 0, we have P0(q) = 1. Now assume that (78) holds for some j ≥ 0. Thus
we have
 Pj+1(q) = Pj(q) exp (− dIj+1(q)
Pj(q)
 )

= (
1 + O( 4j

log2 x
 )) 5−j · exp
 

−
 (1 + O( 1
log2 x )) 5−j log 5
(1 + O( 4j
log2 x )) 5−j
 



= (
1 + O( 4j

log2 x
 )) 5−j · exp (
− (1 + O( 4j

log2 x2
 )) log 5
)

= (
1 + O( 4j+1

log2 x
 )) 5−j−1

which proves the induction step for j + 1, and thus proves (78) for all j = 0, . . . , m by induction.
Now, furthermore, by the bound on m in (74), we have

4
j ≤ 4
m ≤ exp (log 4 · log3 x
log 5
 ) = (log2 x)(log 4/ log 5)

This implies
 Pj(q) = (1 + O ( 1
(log2 x)ν
 )) 5
−j

46

where ν = log (5/4)
log 5 ≈ 0.1386. Therefore, letting D = 2 log 5 and κ = 1
2 log2 x , we get

dij (q) = (
1 + O( 1
log2 x
 )) 5
−j+1 log 5 ≤ 2 (
1 + O( 1
(log2 x)ν
 )) 5−j+1 log 5 = DPj−1(q),

as well as Pj(q) ≥ 1
2 5−j ≥ 1
2 5−m ≥ 1
2 log2 x = κ,

thus verifying the fourth condition (A4).

Verifying the smallness condition on δ

We deﬁne A := 2rm + 2.

Note that, by the deﬁnition of r, and the bounds on m, we have

A = 2 log x log3 x
(log2 x)2 m + 2 ≤ 2 log x log3 x
(log2 x)2 m + 2 ≤ 3 log x(log3 x)2

(log2 x)2 . (79)

To verify that δ satisﬁes the smallness bound in (24), we ﬁrst use (79) to note that

κA

C0 exp AD = exp (A log κ − AD − log C0)

≥ exp (
−3 log x(log3 x)2

(log2 x)2 (log (1/2) − log3 x − 2 log 5) − log C0
)

≥ exp (
−4 log x(log3 x)3

(log2 x)2
 ).

Thus, by deﬁnition of δ, we obtain the bound

δ1/10m+2 = exp (
− 1
20 · 10m+2 log x) ≤ exp (
− 1
20 · 102 10
(− log3 x/ log 5) log x)

= exp (
− 1
20 · 102 log x
(log2 x)(log 10/ log 5)
 )

≤ exp (
− 1
20 · 102 log x
(log2 x)(3/2)
 )

≤ exp (
−4 log x(log3 x)2

(log2 x)2
 )

≤ κA

C0 exp AD .

Therefore, we have that δ satisﬁes the smallness bound

δ ≤ ( κA

C0 exp AD
 )10m+2
 ,

and thus we can apply Theorem 11.

Applying Theorem 11

As all conditions have been checked, we now apply Theorem 11. We therefore obtain random
variables e′
p for each p ∈ ⋃m
j=1 Ij(⃗t), such that, for every e in the range of e′
p, either e = ∅ or e

47

is contained in the range of ep. Furthermore, for any 0 ≤ J ≤ m and any ﬁnite subset e ⊂ V
with |e| ≤ A − 2rJ, we have

P
 

e ⊂ Q
′\
 J⋃

j=1
 ⋃

p∈Ij e
′
p


 = (1 + O(δ1/10J+1)) PJ (e). (80)

We now apply (80) with J = m. By deﬁnition of A, we have A − 2rm = 2. Therefore, we may
let e be a singleton vertex {q}, to obtain

P
 

q ̸∈
 m⋃

j=1
 ⋃

p∈Ij e
′
p


 = P
 

e ⊂ Q
′\
 m⋃

j=1
 ⋃

p∈Ij e
′
p


 = (1 + O(δ1/10m+1)) Pm(q)

= (1 + O(x− 1
20·10m+1 )
) · 5
−m (
1 + O( 1
log2 xµ
 ))

= 5
−m (
1 + O( 1
(log2 x)ν
 )) ,

noting that (log2 x)ν ≪ x 1
20·10m+1 . Similarly, letting e be a two-element set e = {q1, q2} for some
q1 ̸= q2, we obtain

P
 

q1, q2 ̸∈
 m⋃

j=1
 ⋃

p∈Ij e
′
p


 = (1 + O(δ1/10m+1)
) Pm(q1)Pm(q2)

= (1 + O(x− 1
20·10m+1 )
) · 5−2m (1 + O( 1
(log2 x)ν
 ))2

= 5
−2m (1 + O( 1
(log2 x)ν
 )) .

Let Aq denote the event that q ̸∈ ⋃m
j=1 ⋃p∈Ij e′
p, and let 1Aq be the indicator random variable
which is 1 if Aq holds and 0 otherwise. Note that the expectation of 1Aq is simply

E1Aq = P
 

q ̸∈
 m⋃

j=1
 ⋃

p∈Ij e
′
p


 = 5
−m (
1 + O( 1
(log2 x)ν
 )) .

For all p ∈ P\ ⋃m
j=1 Ij(⃗t), let e′
p = ∅. Now, we deﬁne the random variable Y which counts the
number of elements in Q′ not covered by e′
p.

Y := |{q ∈ Q
′ : q ̸∈ e
′
p for all p ∈ P }| = ∑

q∈Q′ 1Aq .

We can calculate the expectation of Y, by linearity of expectation,

EY = ∑

q∈Q′ E1Aq = ∑

q∈Q′ 5−m (
1 + O( 1
(log2 x)ν
 )) = |Q
′| · 5
−m (1 + O( 1
(log2 x)ν
 )) . (81)

Similarly, we calculate the expectation of Y2 as

EY2 = ∑

q1∈Q′
 ∑

q2∈Q′ E1Aq1 1Aq2 = ∑

q1∈Q′
 



 ∑

q2∈Q′
q2̸=q1
 E1Aq1 1Aq2 + E1Aq1
 





48

= ∑

q1∈Q
 



 ∑

q2∈Q
q2̸=q1
 5−2m (
1 + O( 1
(log2 x)ν
 )) + 5−m (
1 + O( 1
(log2 x)ν
 ))





= 5
−2m (
1 + O( 1
(log2 x)ν
 )) (|Q
′|2 − |Q′|
) + 5−m (
1 + O( 1
log2 xµ
 )) |Q
′|

= 5
−2m (
1 + O( 1
(log2 x)ν
 )) |Q
′|2 + O(5
−m|Q
′|).

To bound the error term, we use the lower bound of |Q′| > (log2 x)3, and note that

5
−m|Q| = exp (−m log 5) · |Q′| ≥ exp (− log3 x) · (log2 x)3 ≥ (log2 x)
ν.

This proves that 5−m(log2 x)−µ|Q′| ≥ 1, and thus we have the bound

5−m|Q
′| = O (5−2m(log2 x)
−µ|Q
′|
2)

which gives
 EY2 = 5
−2m (
1 + O( 1
(log2 x)ν
 )) |Q
′|
2. (82)

To obtain an estimate for Y, we now apply Lemma 16 using (81) and (82). Let γ > 0. Thus,
for any real ϵ such that 0 < ϵ < γ, we have for suﬃciently large x

5−m |Q
′| · (1 − ϵ) ≤ EY ≤ 5−m |Q
′| · (1 + ϵ)

and 5
−2m |Q
′|
2 · (1 − ϵ) ≤ EY2 ≤ 5
−2m |Q
′|2 · (1 + ϵ),

thus, by Lemma 16, we have

P (∣
∣ Y − 5
−m|Q| ∣
∣ ≥ γ · 5−m|Q|
) ≤ 3ϵ
(δ − ϵ)2 .

Taking the limit as ϵ → 0 for some ﬁxed γ, therefore yields

P (∣
∣ Y − 5−m|Q| ∣
∣ < γ · 5−m|Q|) → 1 as x → ∞

Applying this result for arbitrary γ > 0 therefore gives Y ∼ 5−m|Q′| and thus

Y ∼ 5−m|Q|

with positive probability, for suﬃciently large x. This completes the proof of the corollary.

Finishing up

In order to apply Corollary 12, we ﬁrst state the random construction theorem, which gives
the existence of a suitable choice of residue classes for large primes, each containing a suﬃcient
number of primes in Py ∩ S(⃗a).

Theorem 13: [30, p. 17] There exists constants A, B such that the following holds: Let x be a
suﬃciently large real number, let P2 and P4 be as given in (18), let c be some positive constant,
and deﬁne y := c log x log3 x
log2 x .

Then there exists some constant C such that
A
c ≤ C ≤ B
c (83)

as well as a tuple of r positive integers (h1, . . . , hr) with r ≤ √log x, and random vectors
⃗a = (ap mod p)p∈P2 consisting of residue classes mod p for each p ∈ P2 and ⃗n = (np)p∈P4 being
a random tuple of |P4| integers, such that the following three conditions hold:

49

• (C1) For each p ∈ P4, and for every a in the range of ⃗a, one has

P(q ∈ ep(⃗a) | ⃗a = ⃗a} ≤ x
−3/5

where ep(⃗a) := {np + hip : 1 ≤ i ≤ r} ∩ Py ∩ S(⃗a).

• (C2) We have, with probability greater than 1/2, that for suﬃciently large x.

|Py ∩ S(⃗a)| ∼ 80c x
log x log2 x.

• (C3) For an element ⃗a in the range of ⃗a, we deﬁne ⃗a as good if, for all but at most x
log x log2 x
elements q ∈ Py ∩ S(⃗a), one has

∑

p∈P P(q ∈ ep(⃗a) | ⃗a = ⃗a) = C + O ( 1
(log2 x)2
 ) .

Then ⃗a is good with probability greater than 1/2.

The proof of Theorem 13 is unfortunately outside the scope of this essay. The proof relies on
showing the existence of a good sieve weight, given as Theorem 25 in the Appendix, which itself
relies on estimates for multidimensional prime-detecting sieves given by Maynard in [69].

The theorem essentially provides us a way to choose residue classes (np mod p) for each large
prime in P4 such that, after sifting out primes from Py using randomly chosen residue classes
from P2, we have ≪ x log2 x/ log x primes remaining, each of which is covered by roughly the
same number of residue classes (np mod p) from P4. This therefore provides us with the neces-
sary conditions to apply the covering theorem which will enable us to use these residue classes
for each prime in P4 to eﬃciently sift out a further number of primes from Py, such that the
total number of primes remaining are ≪ x/ log x.

With this in mind, we shall now prove the penultimate theorem of this essay, Theorem 14, after
which we will then have the necessary results to prove the ﬁnal result in (3).

Theorem 14: [30, p. 9] Let x be suﬃciently large. Then there exists vectors ⃗a = (ap mod p)p∈P2
and ⃗b = (bp mod p)p∈P4, consisting of residue classes mod p for each prime p in P2 and P4
respectively, such that, for all ϵ > 0, we have

|Py ∩ S(⃗a) ∩ S(⃗b)| ≤ (80c + ϵ) x
log x

for suﬃciently large x.

Proof: We choose c to be a small positive constant such that C ≥ 5 log 5/4. An explicit value
for c is calculated in the Appendix (e.g. we can take any c < 1
72000 log 5 ). Now, we take m to be
the largest integer such that (74) holds:
m = ⌊ log3 x
log 5
 ⌋ .

We apply the construction given in Theorem 4 to yield the existence of random variables ⃗a
and ⃗n. Noting that the probability of conditions (C2) and (C3) holding are both larger than
1/2 respectively, we have there exists some value ⃗a such that both conditions (C2) and (C3) hold.

50

We now apply Corollary 12 with P = P4 and Q = Py ∩ S(⃗a) with random variables ep := ep(⃗a)
conditioned to ⃗a = ⃗a. By deﬁnition, we clearly have |P| ≤ x and

(log2 x)
3 < x
log x < |Q| ≤ π(y) ≤ x100

for suﬃciently large x. By deﬁnition of ep, we note that condition (B1) is easily satisﬁed, since,
for any e in the range of ep, we have

|e| ≤ r ≤ √
log x ≤ log x log3 x
(log2 x)2

which holds for suﬃciently large x.

Note that condition (B2) follows directly from (C1). To prove condition (B3) that the codegrees
are suﬃciently small, let q1, q2 ∈ Q be distinct integers, and consider the non-zero integer q1 −q2.
We consider three cases, based on the number of primes in P dividing q1 − q2.

• Case 1: q1 − q2 contain no prime factors from P. Therefore, for any p ∈ P, if q1, q2 ∈
ep(⃗a), then p|q1 − q2, which yields a contradiction. Thus P(q1, q2 ∈ ep(⃗a)) = 0 for all
p ∈ P, and therefore ∑

p∈P P(q1, q2 ∈ ep(⃗a)) = 0.

• Case 2: q1 − q2 contains exactly one prime factor from P. Denote this prime factor as
p0. As with the above case, we have P(q1, q2 ∈ ep(⃗a)) = 0 for all p ∈ P\{p0}. Thus
∑

p∈P P(q1, q2 ∈ ep(⃗a)) = P(q1, q2 ∈ ep0(⃗a)) ≤ x−3/5.

• Case 3: q1 − q2 contains at least two prime factors from P. Denote two of these prime
factors as p0 and p1. However, by a lower bound on P, we get

(x/2)
2 < p0p1 ≤ q1 − q2 ≤ y < x log x.

which gives a contradiction for suﬃciently large x.

Therefore, in all cases, we get
∑

p∈P P(q1, q2 ∈ ep(⃗a)) ≤ x−3/5 ≤ x−1/20,

thus satisfying condition (B3). Finally, condition (B4) follows from (C3), noting that

x
log x log2 x = 1/79c
(log2 x)2 · 79c x
log x log2 x ≤ 1/99c
(log2 x)2 |Py ∩ S(⃗a)| = O ( 1
(log2 x)2 |Q|
)

for suﬃciently large x. We now apply Corollary 12 to obtain random variables e′
p whose range
is contained in the range of ep along with ∅ and such that

|{q ∈ Py ∩ S(⃗a) : q ̸∈ e
′
p for all p ∈ P4}| ∼ 5−m|Py ∩ S(⃗a)| (84)

with positive probability. Thus, for each p ∈ P, we can choose an event e′
p in the range of e′
p
such that (84) holds. Note that either e′
p = ∅ or e′
p lies in the range of ep, in which case there
exists some integer n′
p such that e′
p = {n′
p + hip : 1 ≤ i ≤ r} ∩ Py ∩ S(⃗a).

Therefore, for each p ∈ P4, we set
 51

bp =
 {
n′
p if e′
p ̸= ∅,
0 otherwise.

Thus, we have
 |Py ∩ S(⃗a) ∩ S(⃗b)| = |{q ∈ Py ∩ S(⃗a) : q ∈ S(⃗b)}|

= |{q ∈ Py ∩ S(⃗a) : q ̸≡ bp for all p ∈ P4}|

= |{q ∈ Py ∩ S(⃗a) : q ̸∈ e′
p for all p ∈ P4}|

∼ 5−m|Py ∩ S(⃗a)|

∼ 80c x
log x ,

noting that 5−m ∼ 1/ log2 x. This therefore proves the claim.

We are now ﬁnally ready to prove the lower bound given in (3), in addition to providing an
explicit constant.

Theorem 15: [30, p. 2] Let c be a small positive constant chosen as in the proof of Theorem
14. Then, for all ϵ > 0, we have

G(x) ≥ ( c
1 + 80c − ϵ
) log x log2 x log4 x
log3 x

for suﬃciently large x.

Proof: We proceed in a similar manner to that of the proof of Rankin’s bound in Theorem
8. Note that by, Theorem 14, we have the existence of residue classes ⃗a = (ap mod p)p∈P2 and
⃗b = (bp mod p)p∈P4 such that, for all ϵ > 0,

|Py ∩ S(⃗a) ∩ S(⃗b)| ≤ (80c + ϵ) x
log x .

Now, using these tuples ⃗a and ⃗b, we extend these residue classes to a tuple of residue classes
rp mod p for all primes p ≤ x, deﬁned as follows:

rp =
 




0 if p ∈ P1,
ap if p ∈ P2,
0 if p ∈ P3,
bp if p ∈ P4.

Now consider the following sifted set,

N = {n ∈ {x + 1, x + 2, . . . , y} : n ̸≡ rp mod p for all p ≤ x}.

Note that, by construction, N does not contain any integers divisible by primes in P1 or P3.
Now, let n ∈ N . Note that, if n is not prime, and has some prime factor greater than x/2, then
it must contain a prime smaller than 2y/x, and thus contains a prime factor from P1, which
results in a contradiction.

Thus all elements of N are one of the following:

• Integers N consisting solely of prime factors of P2 .

• Primes p such that x < p ≤ y .
 52

Note that in the latter case, if n ∈ N such that n ∈ Py, then n ∈ Py ∩ S(⃗a) ∩ S(⃗b) by deﬁnition
of rp. Thus, we have the bound

|N | ≤ ψ(y, z) + |Py ∩ S(⃗a) ∩ S(⃗b)|.

Using Lemma 7, we note that, for any ϵ > 0, we have

ψ(y, z) = ψ (
y, exp ( log x log3 x
4 log2 x
 )) < y
(log y)3−ϵ < cx log3 x
log x log2 x ≤ ϵ x
log x

for suﬃciently large x. Thus, for any ϵ > 0, we have the following bound on |N |,

|N | ≤ (80c + ϵ) x
log x

for suﬃciently large x. As with Rankin’s proof, to sieve out with remaining elements, we simply
extend the range to include primes in (x, (1 + 80c + 2ϵ)x] for some ﬁxed ϵ > 0. By the prime
number theorem, we have

∣
∣
{p prime : p ∈ (x, (1 + 80c + 2ϵ)x
]}∣
∣ ≥ (80c + ϵ) x
log x ≥ |N |

for suﬃciently large x. Thus, each element in N can be mapped to a unique prime p such that
x < p ≤ (1 + 80c + 2ϵ)x. By choosing an appropriate residue class rp for this prime, we can
thus ensure that the entire interval (x, y] is sieved out with primes no larger than (1+80c+2ϵ)x.

Finally, we therefore obtain that, for all ϵ > 0,

Y ((1 + 80c + 2ϵ)x) ≥ y − x ≥ (1 − ϵ)y

for suﬃciently large x. Thus, by Theorem 2, we have

G(x) ≥ Y ((1 − ϵ) log x) ≥ ( c
1 + 80c + 2ϵ − ϵ
) log x log2 x log4 x
log3 x

for suﬃciently large x, which ﬁnally concludes the proof.

Remark: Using an explicit value for c where c < 1
72000 log 5 , as calculated in the Appendix, we
obtain the following explicit lower bound for G(x), where for any ϵ > 0, we have

G(x) ≥ ( 1
80 + 72000 log 5 − ϵ
) log x log2 x log4 x
log3 x

for suﬃciently large x.

Conclusion

Prime numbers have long been a fascination for many mathematicians, regarding both its ap-
parent simplicity as the building blocks of the natural numbers as well as its mysterious random
nature. The study of G(x) has especially been indispensable in proving many interesting con-
sequences regarding prime numbers [12, 59].

After Westzynthius [103] showed that G(x)/ log x → ∞ as x → ∞ in 1931, a quantitative
improvement to a lower bound for G(x) was made three times just within the following seven
years. In comparison, besides proving incrementally better values for c in (2), it then took more
than 75 years for the next improvement before Ford, Green, Konyagin, Maynard, and Tao made

53

their breakthrough in 2014. Despite the fact that Tao has oﬀered a cash prize on any further
improvement, it may well be another several decades before anyone can prove that the implied
constant in (3) can be taken to be arbitrarily large.

We note that the R¨odl nibble method used in [30] as described in our essay gives an essentially
near optimal bound for covering Py ∩ S(⃗a) using residue classes for large primes [71]. With this
in mind, any further progress to bounding G(x) using similar methods would presumably require
some improvement towards the Hardy-Littlewood prime k-tuples conjecture [42]. Otherwise,
it seems likely that an entirely new approach would be required to make any substantial progress.

We again remark that a conjectured upper bound for Y (x) made by Maier, Pomerance, implies
that it would not be possible to prove a lower bound better than log x(log2 x)2+ϵ for G(x) using
Lemma 2, suggesting that mathematicians are still a far way from proving the conjectured lower
bound of ≫ (log x)2.

Furthermore, given the relatively weak upper bound of G(x) ≪ x0.525 proven to date, with the
assumption of the Riemann hypothesis only improving this to G(x) ≪ √x log x, it is certain
that the progress towards a strong upper bound for G(x) has a long way to go.

Whilst a very marginal improvement to the upper bound for G(x) may be possible by applying
the most eﬃcient methods known so far, any signiﬁcant improvement to either the lower or
upper bound will require new ideas. It remains to be seen when this will happen, and who will
be the ﬁrst to make such an improvement.

Finally, we note many new results have been found on large gaps between primes, based on the
work done by Ford, Green, Konyagin, Maynard, Tao in [30]. A sequel to this paper published by
Ford, Maynard, Tao [32] used a combination of methods from [30] along with the Maier matrix
method to prove an analogous result to (3) for chains of large gaps between primes. Speciﬁcally,
they were able to prove that

max
pn+k≤x min(pn+1 − pn, . . . , pn+k − pn+k−1) ≫ 1
k2 log x log2 x log4 x
log3 x

for any ﬁxed k ≥ 1, for suﬃciently large x. The methods in [30] were also applied by Maier,
Rassias [67] to obtain large gaps between primes containing a perfect kth power, as well as by
Baker, Freiberg [7] to prove results on the density of limit points of prime gaps normalised by
functions suitably similar to that in (3).

In conclusion, there is no doubt that [30] has made a major contribution to the study of the
distribution of primes, with there being already more than 50 citations for such a recently
published paper. Despite (3) essentially being the near-optimal bound attainable with current
methods, this result will certainly not be the last such, and will hopefully push mathematicians
to explore new radical ideas to further progress known bounds for G(x).

Acknowledgements

I would like to give my sincere thanks to the essay setter, Dr Thomas Bloom, for his many in-
sightful comments and feedback regarding the essay. I would also like to thank the Cambridge
Faculty of Mathematics for providing this valuable opportunity to learn about new recent de-
velopments in mathematics outside the scope of material presented in lectures.

54

References

[1] Adleman, L., McCurley, K. (1994) Open Problems in Number Theoretic Complexity, II.
Algorithmic number theory (Ithaca, NY, 1994), pp.291-322, Lecture Notes in Comput.
Sci., Vol. 877, Springer, Berlin.

[2] Ajtai, M., Koml´os, J., Szemer´edi, E. (1981) A dense inﬁnite Sidon sequence, European J.
Combin. Vol. 2, No. 1, pp.1-11.

[3] Alon, N., Spencer, J.H. (2000) The probabilistic method. (2ed). New York: Wiley-
Interscience.

[4] Appel, K.I., Rosser, J.B. (1961) Table for estimating functions of primes, Communications
Research Division Technical Report Number 4, Institute for Defense Analyses, Princeton
NJ.

[5] Backlund, R.J. (1929) ¨Uber die Diﬀerenzen zwischen den Zahlen, die zu den ersten n
Primzahlen teilerfremd sind, Commentationes in honorem E. L. Lindel¨of. Annales Acad.
Sci. Fenn, Vol 32, No. 2, pp.1-9.

[6] Baker, A., Bollob´as, B. and Hajnal, A. (eds) (1990) A Tribute to Paul Erd˝os. Cambridge:
Cambridge University Press.

[7] Baker, R.C., Freiberg, T. (2016) Limit points and long gaps between primes. Q. J. Math.,
Vol. 67, No. 2, pp.233-260.

[8] Baker, C.L., Gruenberger, F.J. (1959) The First Six Million Prime Numbers, The RAND
Corp., July 1957, Microcard Foundation, West Salem, Wis.

[9] Baker, R., Harman, G. (1996) The diﬀerence between consecutive primes, Proc. London
Math. Soc. Vol. s3-72, No. 2, pp.261-280.

[10] Baker, R., Harman, G., Pintz, J. (2001) The Diﬀerence Between Consecutive Primes, II.
Proc. London Math. Soc (3) Vol. 83, No. 3, pp.532-562.

[11] Banks, W., Ford, K., Tao, T. (2019) Large prime gaps and probabilistic models,
arXiv:1908.08613 [math.NT].

[12] Banks, W.D., Freiberg, T., Maynard, J. (2016) On limit points of the sequence of nor-
malized prime gaps, Proceedings of the London Mathematical Society, Vol. 113, No. 4,
pp.515-539.

[13] Bourgain, J. (2017) Decoupling, exponential sums and the Riemann zeta function, J. Amer.
Math. Soc., Vol. 30 (1): pp.205-224.

[14] Boyer, C.B. (1991) Euclid of Alexandria, A History of Mathematics, (Second ed.). John
Wiley & Sons.

[15] Brauer, A., Zeitz, H. (1930) ¨Uber eine zahlentheoretische Behauptung von Legendre,
Sitzungsberichte Berliner Math. Ges. Vol. 29, pp. 116-125.

[16] Brent, R.P. (1980) The ﬁrst occurrence of certain large prime gaps, Mathematics of Com-
putation Vol.35, pp.1435-1436.

[17] de Bruijn, N.G. (1951) On the number of positive integers ≤ x and free of prime factor
> y, Nederl. Acad. Wetensch. Proc. Ser. A, Vol. 54, pp.50-60.

55

[18] Cadwell, J. H. (1971) Large Intervals Between Consecutive Primes, Mathematics of Com-
putation, Vol. 25, No. 116, pp.909–913.

[19] Cantelli, F.P. (1933) Considerazioni sulla legge uniforme dei grandi numeri e sulla gen-
eralizzazione di un fondamentale teorema del signor. Levy, Giornale d. Istituto Italiano
Attuari, Vol. 4, pp.327-350.

[20] Chang, T.H. (1938) ¨Uber aufeinanderfolgende Zahlen, von denen jede mindestens einer
vonn linearen Kongruenzen gen¨ugt, deren Moduln die erstenn Primzahlen sind. Schr.
Math. Sem. Berlin, Vol. 4, pp.35–55.

[21] Chebyshev, P.L. (1852) Memoire sur les nombres premiers, Oeuvres I, pp. 51-70.

[22] Cooper, S.B., Hodges, A. (2016) The Once and Future Turing. Cambridge University
Press. pp. 37-38.

[23] Cram´er, H. (1920) Some theorems concerning prime numbers, Ark. Mat. Astr. Fys. Vol.
15, No. 5, pp. 1-33.

[24] Cram´er, H. (1936) On the order of magnitude of the diﬀerence between consecutive prime
numbers. Acta Arithmetica, Vol. 2, No. 1, pp.23-46.

[25] Erd˝os, P. (1935) On the diﬀerence of consecutive primes, Quart. J. Math. Oxford Ser.
Vol. 6, pp.124-128.

[26] Erd˝os, P. (1947) Some remarks on the theory of graphs. Bull. Amer. Math. Soc. Vol. 53,
No. 4, pp.292-294.

[27] Erd˝os, P. (1996) Some of my favorite problems and results. In: Graham, R.L., Nesetﬁl,
J. eds. The Mathematics of Paul Erd˝os. Springer-Verlag, Berlin, pp.47-67.

[28] Erd˝os, P., Hanani, H. (1963) On a limit theorem in combinatorial analysis, Publ. Math.
Debrecen, Vol. 10, pp.10–13.

[29] Ford, K., Green, B., Konyagin, S., Maynard J., Tao, T. (2015) Long gaps between primes,
arXiv:1412.5029v2 [math.NT].

[30] Ford, K., Green, B., Konyagin, S., Maynard J., Tao, T. (2018) Long gaps between primes
J. Amer. Math. Soc. Vol. 31, No. 1, pp.65-105.

[31] Ford, K., Green, B., Konyagin, S., Tao, T (2016) Large gaps between consecutive prime
numbers, Annals of Math. Vol.183, pp.935–974.

[32] Ford K., Maynard J., Tao T. (2018) Chains of Large Gaps Between Primes. In: Pintz J.,
Rassias M. (eds) Irregularities in the Distribution of Prime Numbers. Springer, Cham.

[33] Frankl, P., R¨odl, V. (1985) Near Perfect Coverings in Graphs and Hypergraphs, European
Journal of Combinatorics, Vol. 6, No.4, pp.317-326.

[34] Gerbicz, R. (2017) Prime Gap Length with consecutive integers di-
visible by small primes [Online forum comment], Available at
https://www.mersenneforum.org/showthread.php?p=456531 (Accessed 03 March
2020).

[35] Glaisher, J.W.L. (1877) On long successions of composite numbers, Messenger of Mathe-
matics, Vol. 7, pp.102-106, 171-176.
 56

[36] Granville, A. (1995), Harald Cram´er and the distribution of prime numbers, Scandinavian
Actuarial Journal, Vol. 1, pp.12–28.

[37] Green, B.J., Tao, T.C. (2010) Linear equations in primes, Annals of Math. Vol. 171, No.
3, pp.1753–1850.

[38] Green, B., Tao, T., Ziegler, T. (2012) An inverse theorem for the Gowers U s+1[N ]-norm.
Ann. of Math. Vol. 176, No. 2, pp.1231–1372.

[39] Gruenberger, F., Armerding, G. (1961) Statistics on the First Six Million Prime Numbers,
Paper P-2460, The RAND Corp., Santa Monica, Calif.

[40] Hagedorn, T.R. (2009) Computation of Jacobsthal’s function h(n) for n < 50. Math.
Comp. Vol. 78, pp.1073-1087.

[41] Haneke, W. (1963) Versch¨arfung der Absch¨atzung von ζ(1/2 + it), Acta Arith. Vol. 8,
pp.357-430.

[42] Hardy, G.H., Littlewood, J.E. (1922) Some problems of Partitio Numerorum (III): On
the expression of a number as a sum of primes, Acta Math. Vol. 44, No. 1, pp.1–70.

[43] Hardy, G.H., Wright, W.M. (1979) An Introduction to the Theory of Numbers, 5th ed.
Oxford, England: Oxford University Press, pp. 19 and 415-416.

[44] Heath-Brown, D.R. (1982) Gaps between primes, and the pair correlation of zeros of the
zeta function, Acta Arith. Vol. 41, No. 1, pp.85-99.

[45] Heath-Brown, D.R., Iwaniec, H. (1979) On the diﬀerence between consecutive primes Bull.
Amer. Math. Soc. (N.S.) Vol.1, No. 5, pp.758-760.

[46] Heilbronn, H.A. (1933) ¨Uber den Primzahlsatz von Herrn Hoheisel. Mathematische
Zeitschrift. Vol. 36, pp.394–423.

[47] Hildebrand, A. (1986) On the number of positive integers ≤ x and free of prime factors
> y, Journal of Number Theory, Vol. 22, No. 3, pp.289-307.

[48] Hoeﬀding, W. (1963) Probability inequalities for sums of bounded random variables, Jour-
nal of the American Statistical Association. Vol. 58, pp.13–30.

[49] Hoheisel, G. (1930) Primzahlprobleme in der analysis. Sitz. Preuss. Akad. Wiss.Phys.-
Math. Klasse, pp.580–588.

[50] Huxley, M. N. (1972) On the Diﬀerence between Consecutive Primes. Inventiones Mathe-
maticae. Vol. 15 (2): pp.164–170.

[51] Ianucci, D.E. (2005) On the smallest abundant number not divisible by the ﬁrst k primes.
Bull. Belg. Math. Soc. Simon Stevin, Vol.12, No. 1, pp.39-44.

[52] Ingham, A. E. (1937) On the diﬀerence between consecutive primes. Quarterly Journal of
Mathematics. Oxford Series. Vol.8 (1): pp.255–266.

[53] Iwaniec, H. (1978) On the problem of Jacobsthal, Demonstratio Math. Vol. 11, pp.225–231.

[54] Iwaniec, H., Jutila, M. (1979) Primes in short intervals, Ark. Mat., Vol 17, No 1-2,
pp.167-176.

[55] Iwaniec, H., Pintz, J. (1984) Primes in short intervals. Monatshefte f¨ur Mathematik Vol.
98, pp.115–143.
 57

[56] Jacobsthal, E. (1960) ¨Uber Sequenzen ganzer Zahlen, yon denen keine zu n teilerfremd
ist. I—III. Norske. Vid. Selsk. Forhdl. Vol. 33, pp.117-124, 125-131, 132–139.

[57] Kahn, J. (1996) A linear programming perspective on the Frankl-R¨odl-Pippenger theorem,
Random Structures Algorithms, Vol. 8, No. 2, pp.149–157.

[58] Kanold, H.J. (1967) ¨Uber eine zahlentheoretische Funktion von Jacobsthal, Mathematische
Annalen, Vol. 170, pp.314-326.

[59] Kaptan, D.A. (2018) Large Gaps between Primes in Arithmetic Progressions,
arXiv:1809.09579 [math.NT].

[60] Lander, L., Parkin, T. (1967) On First Appearance of Prime Diﬀerences. Mathematics of
Computation, Vol. 21, No. 99, pp.483-488.

[61] Lehmer, D.H., (1957) Tables concerning the distribution of primes up to 37 millions. Copy
deposited in the UMT ﬁle and reviewed in MTAC Vol. 13 (1959) pp.56-57.

[62] Li, J., Pratt, K., Shakan, G. (2017) A lower bound for the least prime in an arithmetic
progression, Q. J. Math., Vol. 68, No. 3, pp.729–758.

[63] Littlewood, J.E. (1922) Researches in the Theory of the Riemann ζ-Function, Proceedings
of the London Mathematical Society, Vol. 20, No. 1, p. XXV.

[64] Lou, S., Yao Q. (1992) A Chebychev’s type of prime number theorem in a short interval
II. Hardy-Ramanujan Journal, Hardy-Ramanujan Society, Vol. 15, pp.1-33.

[65] Maier, H. (1985), Primes in short intervals, The Michigan Mathematical Journal, Vol. 32,
No. 2, pp.221–225.

[66] Maier, H., Pomerance, C. (1990) Unusually large gaps between consecutive primes. Trans.
Amer. Math. Soc. Vol. 322, No. 1, pp.201–237.

[67] Maier, H., Rassias, M.T. (2017) Large gaps between consecutive prime numbers containing
perfect k-th powers of prime numbers. J. Funct. Anal., Vol. 272, No. 6, pp.2659–2696.

[68] Maynard, J. (2015) Small gaps between primes, Annals of Math. Vol. 181, No.1, pp.383-
413.

[69] Maynard, J. (2016) Dense clusters of primes in subsets, Compositio Mathematica. London
Mathematical Society, Vol. 152, No. 7, pp. 1517–1554.

[70] Maynard, J. (2016) Large gaps between primes, Annals of Math. Vol.183, pp.915–933.

[71] Maynard, J. (2019) Gaps between primes, arXiv:1910.13450 [math.NT].

[72] Mersenne Forum, Prime Gap Search (2018) 1.8e19 to 2ˆ64-2ˆ32, [online] Available
at: https://www.mersenneforum.org/showthread.php?t=23513 (Accessed: 20 March
2020).

[73] Mertens, F. (1874) Ein Beitrag zur analytischen Zahlentheorie, J. reine angew. Math. Vol.
78, pp.46–62.

[74] Min, S.H. (1949) On the Order of ζ(1/2+it), Trans. Amer. Math. Soc, Vol. 65, pp.448-472.

[75] Montgomery, H.L, (1971) Topics in multiplicative number theory. Lecture notes in math-
ematics 227. Berlin-Heidelberg-New York: Springer.

58

[76] Montgomery, H.L., Vaughan, R.C. (2006) Multiplicative Number Theory: I. Classical
Theory, Cambridge University Press.

[77] Mozzochi, C.J. (1986) On the diﬀerence between consecutive primes Journal of Number
Theory, Vol. 24, No. 2, pp.181-187.

[78] Nicely, T.R. Some Results of Research in Computational Number Theory [online] Available
at http://web.archive.org/web/20191120044913/http://www.trnicely.net/ (Ac-
cessed: 02 March 2020).

[79] Norton, K.K. (1971) Numbers with Small Prime Factors, and the Least kth Power Non-
Residue, Amer. Math. Soc, Vol. 106, pp.1-106.

[80] Nyman, B., Nicely, T.R. (2003) New prime gaps between 1015 and 5 × 1016, Journal of
Integer Sequences, Vol. 6, Article 03.3.1, pp.1-6.

[81] Oliveira e Silva, T., Herzog, S., Pardi, S. (2014) Empirical veriﬁcation of the even Gold-
bach conjecture and computation of prime gaps up to 4 · 1018, Math. Comp. Vol. 83,
pp.2033–2060.

[82] Phillips, M. (1933) The zeta-function of Riemann; further developments of van der Cor-
put’s method, The Quarterly Journal of Mathematics, Vol. 4, No. 1, pp.209–225.

[83] Pintz, J. (1997) Very large gaps between consecutive primes. J. Number Theory, Vol. 63,
No. 2, pp.286–301.

[84] Pintz, J (2007), Cram´er vs. Cram´er. On Cram´er’s probabilistic model for primes, Func-
tiones et Approximatio Commentarii Mathematici, Vol. 37, No. 2, pp.361–376.

[85] Pippenger, N., Spencer, J. (1989) Asymptotic behavior of the chromatic index for hyper-
graphs, J. Combin. Theory Ser. A Vol.51, No. 1, pp.24–42.

[86] Rankin, R.A. (1938) The diﬀerence between consecutive prime numbers, J. London Math.
Soc. Vol. 13, No.4, pp.242–247.

[87] Rankin, R.A. (1963) The diﬀerence between consecutive prime numbers V, Proc. Edin-
burgh Math. Soc, Vol. 13, No.4, pp.331–332.

[88] Ribenboim, P. (2004) The Little Book of Bigger Primes Second Edition. Springer-Verlag.
p. 185.

[89] Ricci, G. (1934) Ricerche arithmetiche sui polinomi. II. Intorno a una proposizione non
vera di Legendre, Rend. Circ. Mat. Palermo Vol. 58, pp.190-207.

[90] Riesel, H. (2012) Prime Numbers and Computer Methods for Factorization [2nd ed]
Birkhauser.

[91] R¨odl, V. (1985) On a packing and covering problem, European J. Combin. Vol. 6, No. 1,
pp.69–78.

[92] Ruzka, I.Z., (1999) Primes and the Integers, Journal of Number Theory, Vol. 79, pp.115-
163.

[93] Sch¨onhage, A. (1963) Eine Bemerkung zur Konstruktion grosser Primzahll¨ucken, Arch.
Math. Vol.14, pp.29–30.

[94] Shanks, D. (1964) On maximal gaps between successive primes Math. Comp. Vol.18,
pp.646-651.
 59

[95] Soundararajan K. (2007) The Distribution of Prime Numbers. In: Granville A., Rudnick
Z. (eds) Equidistribution in Number Theory, An Introduction. NATO Science Series, Vol
237. Springer, Dordrecht.

[96] Stevens, H. (1977) On Jacobsthal’s g(n)-Function Mathematische Annalen, Vol. 226,
pp.95-98.

[97] Szele, T. (1943) Kombinatorikai vizsg´alatok az ir´anyitott teljes gr´aﬀal kapcsolatban, Mat.
Fiz. Lapok Vol. 50, pp.223–256.

[98] Tao, T. (2014) Large gaps between consecutive prime numbers [online], What’s new,
21 August. Available at: https://terrytao.wordpress.com/2014/08/21/large-gaps-
between-consecutive-prime-numbers/ (Accessed: 23 March 2020).

[99] Tao, T. (2014) Long gaps between primes [online], What’s new, 16 December. Available
at: https://terrytao.wordpress.com/2014/12/16/long-gaps-between-primes (Ac-
cessed: 23 March 2020).

[100] Tchudakoﬀ, N.G. (1936) On the diﬀerence between two neighboring prime numbers. Mat.
Sb. Vol. 1, pp.799–814.

[101] Titchmarsh, E.C. (1942) On the Order of ζ(1/2 + it), The Quarterly Journal of Mathe-
matics, Volume os-13, No. 1, pp.11–17.

[102] Western, A.E. (1934) Note on the magnitude of the diﬀerence between successive primes,
J. London Math. Soc. Vol. 9, No. 4, pp.276-278.

[103] Westzynthius, E. (1931) ¨Uber die Verteilung der Zahlen, die zu den n ersten Primzahlen
teilerfremd sind, Commentationes Physico– Mathematicae, Societas Scientarium Fennica,
Helsingfors Vol. 5, No. 25, pp.1–37.

[104] Wolf, M. (2014) Nearest-neighbor-spacing distribution of prime numbers and quantum
chaos, Phys. Rev. E, Vol. 89, No. 2, pp.022922.

[105] Young, J., Potler, A. (1989) First Occurrence Prime Gaps. Mathematics of Computation,
Vol. 52, No. 185, pp.221-224.

[106] Ziller, M., Morack, J. (2017) Algorithmic concepts for the computation of Jacobsthal’s
function, arXiv:1611.03310v2 [math.NT].

60

Appendix

Probability

Throughout this essay, we make use of many of the essential results in probability, especially
when proving the covering theorem (Theorem 11) as well as its application in proving a lower
bound for G(x).

All random variables are written in boldface (e.g. X, Y). We use P to denote probability and
EX to denote the expected value of some random variable X. Some of the fundamental results
used in this essay are given below.

Markov’s inequality: Let X be a non-negative countable random variable with expectation
EX. Then, for any λ > 0, we have
 P(X ≥ λ) ≤ EX
λ .

Proof: Let X have the possible outcomes x1, x2, . . . , which occur with probabilities p1, p2, . . . .
Thus, by deﬁnition of expectation, we have

EX = ∑ xipi ≥ ∑

xi≥λ xipi ≥ λ ∑

xi≥λ pi = λP(X ≥ λ),

noting that xi ≥ 0 for all possible outcomes xi. Dividing by λ then yields the desired inequal-
ity.

We note that a similar approach to the above also proves the case where X is a continuous ran-
dom variable, and thus Markov’s inequality holds for arbitrary non-negative random variables.

Chebyshev’s inequality: Let X be a countable random variable with expectation EX = µ
and variance VarX = σ2 . Then, for any a > 0, we have

P(|X − µ| ≥ a) ≤ σ2

a2 .

Proof: We apply Markov’s inequality to the random variable Y := (X − E[X])2. Note that
E[Y] = σ2 by deﬁnition of variance. Using λ = a2, this gives

P(|X − µ| ≥ a) = P((X − µ)2 ≥ a2) = P(Y ≥ λ) ≤ EY
λ = σ
a2

which yields the desired inequality.

Note that Chebyshev’s inequality is essentially the statement that, if the variance of a random
variable is small, then X has high probability of being close to it’s expectation µ. We can now
apply these facts to prove the following lemma, of which an easy corollary is frequently used in
the proof of the covering theorem (Theorem 11).

Lemma 16: Let X be a random variable with expectation EX = µ. Let A > 0 and 0 < ϵ < 1
be two real constants such that

A(1 − ϵ) ≤ EX ≤ A(1 + ϵ) and A2(1 − ϵ) ≤ EX2 ≤ A2(1 + ϵ).

Then, for any γ > ϵ, we have
 P(|X − A| ≥ γA) ≤ 3ϵ
(γ − ϵ)2 .

61

Proof: First, we obtain an upper bound on the variance

VarX = E[(X − µ)
2] = EX2 − µ2 ≤ A2(1 + ϵ) − A
2(1 − ϵ)
2 = A2(3ϵ − ϵ
2) ≤ 3ϵA2,

noting that A(1 − ϵ) is positive, since ϵ < 1.

Now, let γ > ϵ. By the ﬁrst given condition, we have that |A − µ| ≤ ϵA. Therefore, if
|X − A| ≥ γA, then by the triangle inequality, we obtain

|X − µ| ≥ |X − A| − |A − µ| ≥ γA − ϵA = (γ − ϵ)A.

Thus, the event |X − A| ≥ γA implies |X − µ| ≥ (γ − ϵ)A. Therefore, we now apply Chebyshev’s
inequality to obtain

P(|X − A| ≥ γA) ≤ P(|X − µ| ≥ (γ − ϵ)A] ≤ VarX
(γ − ϵ)2A2 ≤ 3ϵ
(γ − ϵ)2 ,

which proves the desired bound.

We note the following corollary, used in the proof of the covering theorem.

Corollary 17: Let m be a non-negative integer, and let s, t be positive integers such that
2s < t. Let δ be some real quantity such that 0 < δ < 1. Let X be a random variable such that

EX = A (1 + O(δ 1
s×10m )
) and EX2 = A2 (1 + O(δ 1
s×10m )
)

for some constant A. Then we have
 X = A(1 + O(δ 1
t×10m ))

with probability 1 − O(δ 1
u×10m ) where
 u = st
t − 2s .

Proof: By the given conditions on EX and EX2, we have that there exists some constant
C > 0 such that
 A(1 − Cδ 1
s×10m ) ≤ EX ≤ A(1 + Cδ 1
s×10m )

and A2(1 − Cδ 1
s×10m ) ≤ EX2 ≤ A2(1 + Cδ 1
s×10m ).

We now apply Lemma 16 with ϵ = Cδ 1
s×10m and γ = 2Cδ 1
t×10m . Note that, since s < t, we have
γ > 2ϵ. Therefore

P (|X − A| < 2Cδ 1
t×10m A
) = 1 − P (|X − A| ≥ γA) ≥ 1 − 3ϵ
(γ − ϵ)2 ≥ 1 − 3ϵ
(γ/2)2

= 1 − 12
C δ 1
t×10m − 2
t×10m = 1 − 12
C δ t−2s
st×10m = 1 − O(δ 1
u×10m )

where u = st/(t − 2s). This therefore proves the claim.

We also make use of Hoeﬀding’s inequality when proving Corollary 12.

62

Hoeﬀding’s inequality: [48] Let m be a positive integer, and let X1, X2, . . . , Xm be inde-
pendent random variables such that we have the expectation satisﬁes EXi = 0, and |Xi| ≤ Bi
for each i = 1, . . . , m. Then, for any real t > 0, we have

P(|X1 + X2 + · · · + Xm| ≥ t) ≤ 2 exp (
− t2

2(B2
1 + B2
2 + . . . B2
m)
 ).

Proof: A full proof can be found at [48].

Finally, we note the idempotency property of expectation.

Idempotency: Let X and Y be countable random variables, and let E(X | Y) be the random
variable which takes the value E(X | Y = Y ) on the event that Y = Y . Then, we have

E(E(X | Y)) = EX.

Proof: We simply apply the deﬁnition of expectation, summing over all Y in the range of Y,
as well as summing over all X in the range of X. Doing this yields

E(E(X | Y)) = ∑

Y E(X | Y = Y )P(Y = Y )

= ∑

Y
 ∑

X XP(X = X | Y = Y )P(Y = Y )

= ∑

X X ∑

Y P(X = X | Y = Y )P(Y = Y )

= ∑

X X ∑

Y P(X = X and Y = Y )

= ∑

x XP(X = X)

= EX,

thus proving the claim.

Elementary upper bounds for G(x)

Here, we prove some basic elementary upper bounds for G(x) only using the prime number
theorem. The ﬁrst lemma simply shows that G(x) = o(x) from the direct asymptotic state-
ment of the prime theorem, whereas the second gives a further quantitative bound based on
the error term obtained for ϑ(x), where ϑ(x) is the (ﬁrst) Chebyshev function ϑ(x) = ∑
p≤x log p.

Theorem 18: Let ϵ > 0. We have G(x) ≤ ϵx

for suﬃciently large x.

Proof: We simply use the asymptotic result that π(x) ∼ x/ log x. Indeed, let ϵ > 0 and let
δ = ϵ
2+ϵ . Thus, by the prime number theorem, we have

(1 − δ) x
log x ≤ π(x) ≤ (1 + δ) x
log x

for suﬃciently large x. Thus, for x in this range, we obtain

π(x) < (1 + δ) x
log x = 2 + 2ϵ
2 + ϵ x
log x = 2
2 + ϵ (1 + ϵ)x
log x = (1 − δ) x + ϵx
log x

63

< (1 − δ) x + 2ϵx
log (x + 2ϵx) ≤ π(x + 2ϵx).

Therefore, obtaining π(x) < π(x + 2ϵx) for suﬃciently large x. This implies there exists a prime
between x and x + 2ϵx, which thus proves the theorem.

Using an explicit error term of ϑ(x) in the prime number theorem, we have the following quan-
titative improvement:

Theorem 19: Let f (x) be a positive increasing function for suﬃciently large x such that
f (2x) < 2f (x) and f (x) = o(x) and that ϑ(x) = x + O(f (x)). Then

G(x) ≪ f (x).

Proof: Let C be a positive constant such that, for all suﬃciently large x, we have

x − Cf (x) < ψ(x) < x + Cf (x).

Thus, note that, for suﬃciently large x, we have

2f (x) < 3f (x)

=⇒ f (2x) < 3f (x)

=⇒ f (x + x) < 3f (x)

=⇒ f (x + 4Cf (x)) < 3f (x)

=⇒ Cf (x + 4Cf (x)) < 3Cf (x)

=⇒ x + Cf (x) < x + 4Cf (x) − Cf (x + 4Cf (x))

=⇒ ψ(x) < ψ(x + 4Cf (x)),

which implies there exists a prime between x and x + 4Cf (x), and therefore proving that
G(x) ≪ f (x).

Applying the above lemma to the error term that de la Poussin proved in 1899 yields the
following upper bound for G(x), G(x) ≪ x
ea
√log x ,

which was the ﬁrst sublinear bound obtained for G(x).

Partial integration results

When proving Rankin’s bound in Theorem 8, we make use of an upper bound on the number
of y-smooth integers less than or equal to x, ψ(x, y), proven in Theorem 7. The proof makes
use of the following four integral bounds.

Lemma 20: [86, p. 243] For suﬃciently large T , we have

∫ T

1
 et

t dt ≤ eT

T + O ( eT

T 2
 ) .

Proof: Applying integration by parts twice, we obtain

∫ T

1
 et

t dt = et

t
 ∣
∣
∣
∣

t=T

t=1 + ∫ T

1
 et

t2 dt

64

= eT

T + O(1) + et

t2
 ∣
∣
∣
∣

t=T

t=1 + 2 ∫ T

1
 et

t3 dt

≤ eT

T + eT

T 2 + O(1) + 2T max (
e, eT

T 3
 )

= eT

T + 3 eT

T 2 + O(1),

noting that et/t3 is an increasing function when t > 3. This yields the result.

Lemma 21: [86, p. 243] For suﬃciently large T , we have

∫ 1

1/T
 et

t dt = log T + O(1).

Proof: We use the elementary bound ex ≤ 1 + 2x for all x ∈ [0, 1], which can be veriﬁed using
standard derivative tests. This yields
∫ 1

1/T
 et

t dt ≤ ∫ 1

1/T
 1 + 2t
t dt

= ∫ 1

1/T
 1
t dt + 2 (
1 − 1
T
 )

= log t∣
∣
∣
t=1

t=1/T + O(1)

= log T + O(1),

which proves the lemma.

Lemma 22: [86, p. 243] For suﬃciently large T , we have

∫ T

1
 et

t2 dt ≤ eT

T 2 + O ( eT

T 3
 ) .

Proof: We proceed similarly as done in Lemma 20. Applying integration by parts twice, we
obtain ∫ T

1
 et

t2 dt = et

t2
 ∣
∣
∣
∣

t=T

t=1 + 2 ∫ T

1
 et

t3 dt

= eT

T 2 + O(1) + 2 et

t3
 ∣
∣
∣
∣
t=T

t=1 + 6 ∫ T

1
 et

t4 dt

≤ eT

T 2 + 2 eT

T 3 + O(1) + 6T max (
e, eT

T 4
 )

= eT

T 2 + 7 eT

T 3 + O(1),

noting that et/t4 is an increasing function when t > 4. This yields the result.

Lemma 23: [86, p. 243] For suﬃciently large T , we have

∫ 1

1/T
 et

t2 dt = T + O(log T ).

65

Proof: Again, we use the elementary bound ex ≤ 1 + 2x for all x ∈ [0, 1]. This yields
∫ 1

1/T
 et

t2 dt ≤ ∫ 1

1/T
 1 + 2t
t2 dt

= ∫ 1

1/T
 1
t2 dt + 2 ∫ 1

1/T
 1
t dt

= − 1
t
 ∣
∣
∣
∣
t=1

t=1/T + 2 log t∣
∣
∣
t=1

t=1/T

= T + O(log T ),

which proves the lemma.

Remark: We actually have equality in each of the four lemmas given above, however only
proving the inequality bound is suﬃcient for our purposes of proving Rankin’s theorem.

Mertens’ theorem

Theorem 24: [73] (Mertens’ third theorem) There exists some real constant c such that

∏

p≤x
 (1 − 1
p
 ) = c log x + O(1).

Proof: See [76, p. 50] .

Calculation of a constant c

To calculate an explicit constant c in the deﬁnition of y, given in (16), we begin by stating the
following theorem, which is used in [30] to prove Theorem 13.

Theorem 25: [30, p. 25] (Existence of good sieve weight) There exist positive constants A′ and
B′ such that the following theorem holds: Let x be a suﬃciently large real number and deﬁne
y as in (16),
 y = cx log x log3 x
log2 x .

Let P4 and Py be deﬁned as in (18) and (19) respectively. Let r be a positive integer with

r0 ≤ r ≤ (log x)1/5

for some suﬃciently large absolute constant r0 and let (h1, h2, . . . , hr) be an admissible r-tuple
contained in {1, 2, . . . , 2r2}. Then one can ﬁnd a positive quantity

τ ≥ x−o(1)

and a positive quantity u = u(r) depending only on r such that

A′ log r ≤ u ≤ B′ log r (85)

and a non-negative function w : P4 × Z → R+ supported on P4 × (Z ∪ [−y, y]) with the following
four properties

• Uniformly for every p ∈ P4, one has

∑

n∈Z w(p, n) = (1 + O( 1
(log2 x)10
 )) τ y
(log x)r .

66

• Uniformly for every q ∈ Py and i ∈ {1, . . . , r}, one has

∑

p∈P4 w(p, q − hip) = (
1 + O( 1
(log2 x)10
 )) τ u
r x
2(log x)r .

• Uniformly for every h = O(y/x) that is not equal to any of the hi, one has

∑

q∈Py
 ∑

p∈P4 w(p, q − hp) = O ( 1
(log2 x)10 τ x
(log x)r y
log x
 ) .

• Uniformly, for all p ∈ P4 and n ∈ Z,

w(p, n) = O(x
1/3+o(1)).

We shall not present a full proof of the above theorem, but simply show the relevant calculations
to obtain a numerical lower bound for the constant A′ in equation (85) above.

In [30, p. 35], the constant u is deﬁned to be

u := φ(B)
B log R
log x kJk
2Ik , (86)

where B is either 1 or a prime, k := r and R := (x/4)θ/3, where θ = 1/3.

The quantity B is deﬁned in [30, p. 31] to be either 1 or a prime of size ≫ log2 Q with
Q := exp c1√log x as given in [30, p. 32]. Thus, we have that

φ(B)
B ∼ 1

which implies, for all ϵ1 > 0, we have
 φ(B)
B ≥ 1 − ϵ1

for suﬃciently large x. Also, by deﬁnition of R and θ, we have

log R
log x = (θ/3) log (x/4)
log x ∼ θ
3 = 1
9 ,

thus, for all ϵ2 > 0, we have log R
log x ≥ 1
9 − ϵ2

for suﬃciently large x. The constants Ik and Jk are deﬁned in [30], where it is established in
[69, p. 20] that, for any ϵ3 > 0, Jk
Ik ≥ ( 1
4 − ϵ3
) log k
k

for suﬃciently large k. Thus, by deﬁnition of u in (86), we obtain the following lower bound for
u,
 u ≥ (1 − ϵ1) · ( 1
9 − ϵ2
) · ( 1
8 − ϵ3
2
 ) log r

which thus implies, for any ϵ4 > 0, we have

u ≥ ( 1
72 − ϵ4
) log r

67

for suﬃciently large x. This implies we take can A′ = 1/72 − ϵ4 in (85) in the statement of
Theorem 25.

Now, in the proof of Theorem 13 [30, p. 25], the value r was set to be the maximum permitted
value, r = ⌊(log x)1/5⌋,

which gives us that, for any ϵ5 > 0, we have

u ≥ ( 1
72 − ϵ4
) · log (⌊(log x)1/5⌋) ≥ ( 1
360 − ϵ5
) log2 x (87)

for suﬃciently large x. Also, the quantity C was deﬁned in [30, p. 28] to be

C := u
σ x
2y , (88)

where σ is the density of S(⃗a) in Z, which is

σ := ∏

p∈P2
 (
1 − 1
p
 ) .

We recall the deﬁnition of P2 := {p prime : (log x)20 ≤ p < z}. Now, by Mertens’ theorem, this
is
 σ ∼ log ((log x)20)

log z = 20 log2 x
(log x log3 x/4 log2 x) = 80(log2 x)2

log x log3 x . (89)

Therefore, substituting the bounds for u and σ obtained in (87) and (89), as well as x and y
into the deﬁnition of C in (88), we obtain

C ≥ (1/360 − ϵ5) log2 x
(80(log2 x)2/ log x log3 x) · x
(2cx log x log3 x/ log2 x) = ( 1
57600 − ϵ5
) 1
c ,

which yields a lower bound for the constant A in equation (83) as, for any ϵ > 0, one can take

A = 1
57600 − ϵ.

Finally, in order to apply Corollary 12, we must have that C satisﬁes

5
4 log 5 ≤ C,

which, by (83), implies it is suﬃcient to ensure 5 log 5/4 ≤ A/c. Thus, taking c to be any
positive real constant satisfying

c < A
(5/4) log 5 = 1
57600 · (5/4) log 5 − ϵ = 1
72000 · log 5 − ϵ

will work.

Remark: Certainly, this is not the best bound that can be achieved with the methods given in
[30]. Indeed, using a slightly better bound for smooth numbers obtained by de Bruijn [17], one
can modify the deﬁnition of z in (17) to be

z := exp ( log x log3 x
3 log2 x
 )

68

which gives the improved value of
 c = 1
54000 log 5 − ϵ

for any ϵ > 0.

Even still, the methods used in [30] to track the constants were far from optimal. Given that the
quantitative improvement over (8) using the covering theorem was the main goal, comparatively
little work was put into optimising the implied constant. One of the biggest contributions to
the denominator in c is the exponent of 20 in the logarithm (log x)20 in the deﬁnition of P2.
Decreasing this value (as well as the constant in the denominator of z) could potentially result
in a far more optimised value for c. It is however unlikely that these methods can be used to
improve a value of c beyond 1/2.
 69
