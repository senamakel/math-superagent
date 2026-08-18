<!-- source: https://msp.org/ent/2022/1-1/ent-v1-n1-p02-p.pdf | converted from PDF -->

ESSENTIAL
NUMBER THEORYmsp
 Exceptional zeros, sieve parity, Goldbach

John B. Friedlander and Henryk Iwaniec

2022

vol. 1 no. 1

msp
 Essential Number Theory
Vol. 1, No. 1, 2022

https://doi.org/10.2140/ent.2022.1.13

Exceptional zeros, sieve parity, Goldbach

John B. Friedlander and Henryk Iwaniec

We survey connections between the possible existence of exceptional real zeros of
Dirichlet L-functions and the sieve parity barrier and then show how recent work
tying them to the Goldbach problem can be viewed in a considerably generalized
framework.
 1. Introduction

A fundamental problem in analytic number theory is that of establishing excellent
upper and lower bounds in general sieve methods, most especially in the linear sieve.
Following a great deal of progress, stretching now over a century, one gradually
became aware of a general “parity barrier” which governs the limitations of what
one can hope to accomplish, at least in general.
A fundamental problem in analytic number theory is that of establishing zero-free
regions for Dirichlet L-functions. In case the corresponding character χ (mod q)
is complex or, alternatively, for all complex zeros ρ = β + iγ with γ ̸= 0, one has
long known how to produce zero-free regions of the type

σ ≥ 1 − c/ log q(|t| + 1) (1-1)

where s = σ + it with a positive constant c. In the remaining situation, where
both χ and s are real, much less is known, nothing more recent than a famous
“ineffective” estimate of Siegel for the L-function at s = 1 which enables a bound
like (1-1) but only with the replacement of log q by q ε with arbitrary ε > 0 and a
numerically uncomputable c depending on ε. This exponentially weaker result has
been a serious impediment to progress in many basic questions.
It is not unfair to claim that much progress in mathematics proceeds by analogy.
The two problems above, in many aspects, ring familiar to each other. The first
purpose of this paper is to illustrate ways in which this has been found to be true.
Our second purpose is to, in the case of one close recently discovered connection,
carry forward this investigation to a new, deeper and more general setting.

Friedlander was supported in part by NSERC grant A5123.
MSC2020: 11M20, 11N05, 11N35, 11P32.
Keywords: primes, sieves, exceptional zeros, Goldbach conjecture.

13

14 JOHN B. FRIEDLANDER AND HENRYK IWANIEC

We recall, that an “exceptional” zero is a real zero β that does lie in the region (1-1)
for a constant c. If however there were only a finite number of these we could
(since the L-functions do not vanish at s = 1) adjust the constant c to exclude them
all from the region. Thus the name is really not a very good one for an individual
zero since the concept requires an infinite sequence of these. Nevertheless, it is
ingrained in the literature; when we use it we are thinking of such a sequence. It is
known, essentially due to Landau, that such a sequence of moduli, should one exist,
must be very lacunary; the zeros would all be simple, at most one per modulus and
indeed with the exceptional moduli qi satisfying

log qi+1
log qi → ∞.

Failing a proof of their nonexistence, it is the lack of any examples of exceptional
zeros that leads to the ineffectivity in results such as that of Siegel. Specific real (or
nearly real) zeros can and do lead to computationally effective results, even when,
as first realized in [Friedlander 1976], they are all the way over at s = 1
2 , a location
where the GRH does not prohibit their appearance.
In the absence of a solution to the problem of whether there exist exceptional
zeros, there have naturally been attempts to relate the question to other very difficult
problems. One class of results of this type deals with showing that the assumption
of the existence of exceptional zeros leads to consequences for prime number
distribution that are beyond current reach, but are nevertheless expected to be true.
There have been in recent years quite a number of such results, several by the
current authors; see [Heath-Brown 1983; Friedlander and Iwaniec 2003; 2004;
2005; Merikoski 2021].
These statements, although conditional, can be quite deep and spectacular. For
example, in the case of [Friedlander and Iwaniec 2003], we derived asymptotics for
the counting of primes p ≤ x in arithmetic progressions of modulus q < x 1/2+δ, so
beyond the reach of the generalized Riemann hypothesis. An essential ingredient for
this was our asymptotic formula for the divisor function τ3(n), n ≤ x in progressions
to modulus q ≤ x 1/2+δ′, which we deduced [Friedlander and Iwaniec 1985] from
the expected estimates for exponential sums over relevant varieties, proofs of which
were provided for us by Birch and Bombieri, using in turn the Riemann hypothesis
for varieties, proved by Deligne. The type of applications of Deligne’s work,
pioneered in [Friedlander and Iwaniec 1985], has since been extensively developed,
for example by Y. Zhang [2014] and, especially, in a whole series of papers by
E. Fouvry, E. Kowalski and P. Michel.
Results of this type are not however the primary concern in this paper. On the
contrary, we are here highlighting an admittedly smaller class of examples, wherein
the assumption of exceptional zeros leads to consequences that are beyond current

EXCEPTIONAL ZEROS, SIEVE PARITY, GOLDBACH 15

reach, but are nevertheless expected to be false. If one does not believe in the
existence of exceptional zeros, then one can dream that this is more promising.
One early example of this class we here consider, by now folklore, shows that
the nonexistence of such zeros would follow from improvements, seductively small,
in the Brun–Titchmarsh theorem which gives uniform upper bounds for the number
of primes in an arithmetic progression. We shall recall this situation in more detail
in Section 3.
In more recent years, results have been obtained showing how relatively good
bounds for exceptional zeros would follow from assumptions about the less obvi-
ously related Goldbach conjecture. The latter famous statement predicts that every
even integer exceeding two can be written as the sum of two primes. Hardy and
Littlewood [1923] put forth a conjectured asymptotic formula for the number of
representations of n as the sum of two primes. Following the normal practice in
the subject, we find it simpler to consider a weighted sum over the representations
involving the von Mangoldt function, one which leads to an entirely equivalent
conjecture. Let
 G(n) = ∑

m1+m2=n
2∤m1m2
 3(m1)3(m2). (1-2)

The Hardy–Littlewood conjecture predicts that, for n even, we have G(n) ∼ S(n)n
where S(n) is a certain positive product over the primes, to be defined in (4-2), and
easily large enough to imply Goldbach for all sufficiently large even n.
In Section 4 we recall how even a much weakened form of this conjectured
asymptotic completely eliminates the possible existence of any exceptional zeros.
Then, in the subsequent sections, we are going to generalize considerably the results
of Section 4, for the purpose of showing clearly that the questions are linked to the
parity barrier of sieve theory.
But first, in the next section, we give a review of that barrier.

2. Parity problem and the asymptotic sieve

We are interested in counting prime numbers. Beginning from the very earliest
works, but especially over the past century, a significant component of this exercise
has been the development of sieve methods.
Already from Brun’s early successes, a striking achievement was the attain-
ment of upper bounds of the correct order for the number of primes in interesting
subsequences of the positive integers.
The attainment of a positive lower bound however seemed always a bit beyond
reach. What one could succeed in getting was a lower bound for the number of
integers having no more than k prime factors for some value of k, fairly small

16 JOHN B. FRIEDLANDER AND HENRYK IWANIEC

but invariably greater than one. These results created an interest in the so-called
“almost primes”.
Gradually, around the middle of the last century, it began to be noticed that the
constant factor in the upper bound was never better than twice the expected, though,
in the most favorable situations, it could come very close to that.
Analogously, although the lower bound the machinery spewed out for the number
of primes was never positive, here too, in the most favorable situations, it could
come very close to being so. This has in places been attributed to the incapability of
the sieve to distinguish between integers with an odd number of prime factors and
those having an even number. The apparent inevitability of this situation has led to
the name “parity phenomenon”, a name which will seem more clearly appropriate
in what follows.
In the same way that, for reasons which are both elementary (think Chebyshev)
and analytic (think Riemann), it turns out to be both convenient and elegant to study
the primes using the von Mangoldt function, the study of almost primes of order
k is facilitated with the introduction of its generalization, given by the Dirichlet
convolution
 3k = µ ∗ logk, (2-1)

which, as its progenitor (k = 1), is supported on integers having at most k distinct
prime factors, satisfies (by induction) the recurrence

3k+1 = 3k · log +3k ∗ 3, (2-2)

obeys the bounds
 0 ≤ 3k(n) ≤ (log n)k (2-3)

and yields the asymptotic formula
∑

n≤x 3k(n) ∼ kx(log x)
k−1. (2-4)

In case k = 1 this last result is of course the prime number theorem and from that
and (2-2) one can easily obtain the others. However, it turns out, due to Selberg,
that for k = 2 and hence for larger k, the formula admits an elementary proof.
In retrospect, we can see that this difference in the levels of difficulty between
k = 1 and larger k is mirrored in the analytic behavior of their generating functions.
The Dirichlet series for 3k, namely

∑

n≥1 3k(n)n−s = (−1)
k ζ (k)(s)
ζ (s) , (2-5)

EXCEPTIONAL ZEROS, SIEVE PARITY, GOLDBACH 17

has a pole of order k at s = 1. As soon as k ≥ 2 this pole has multiple order and its
effect cannot be canceled out by a simple real zero. Still, it does seem strange that
zeta in particular feels the need to worry that she might have an exceptional zero.
It is interesting to note that, although for k = 1 the contribution to the sum in (2-4)
comes entirely from the integers with an odd number of distinct prime factors, on
the contrary, for each k ≥ 2 the contribution comes half from odd and half from
even.
The original motivation for Selberg’s discovery was that it could then be combined
with other arguments (which he implemented, as did Erdös) leading to elementary
proofs for the prime number theorem itself. But that is not the issue here (although
perhaps some day it could be).
We are concerned with the counting of primes in more general sequences and,
with rare exceptions, we are still far from this goal. It was Bombieri [1976] (see
also [Friedlander and Iwaniec 1978; 1996; 2010]) who made breakthroughs in
enormously generalizing the elementary results for k ≥ 2 with his asymptotic sieve.
To avoid using excessive space and notation we shall give only the flavor of these
results.
We consider a sequence (an) of nonnegative reals which satisfies certain basic
axioms of linear sieve type. Without the possibility of providing an exhaustive list
(see [Friedlander and Iwaniec 2010]) we mention the most essential ones.
We consider, for given d ≥ 1, the congruence sum

Ad (x) = ∑

n≤x
n≡0 (mod d)
 an (2-6)

and assume it satisfies the approximation

Ad (x) = A1(x)g(d) + rd (x) (2-7)

where the function g(d) in the “main term” is multiplicative and satisfies the linear
sieve condition ∑

p≤y g( p) log p = log y + cg + O A((log y)
−A) (2-8)

for arbitrary A and all y ≤ x.
For the same A and y the “remainder terms” rd (y) are assumed to satisfy, for
every ε > 0, D = x 1−ε, the bound
∑

d≤D|rd (y)| ≪ A1(x)(log D)
−A. (2-9)

We remark that, of these conditions, that for the main term, i.e., (2-8), is known to
hold for many interesting sequences. On the other hand, the latter assumption (2-9),

18 JOHN B. FRIEDLANDER AND HENRYK IWANIEC

although expected to hold for many of those natural sequences that are not very
sparse (in that they satisfy A1(x) ≫ x(log x)−B for some B), is in most cases quite
difficult to prove.
By weakening the assumption (2-9), requiring it to hold only for some smaller
value of D (the“level of distribution”), one can verify it for many sequences and still
can get useful results (see [Friedlander and Iwaniec 1978]), but then the connection
to the parity principle rapidly falls off.
We now loosely describe the main thrusts of Bombieri’s results [1976].
By heuristic arguments, one is led to the conjecture that for a nice sequence (an)
satisfying (2-8) one might expect, in place of (2-4), the asymptotic formula
∑

n≤x an3k(n) ∼ k H ∑

n≤x an(log n)
k−1 ∼ k H A1(x)(log x)
k−1, (2-10)

where H is given by the product

H = ∏

p (1 − g( p))
(
1 − 1
p
 )−1. (2-11)

Bombieri shows in particular that, given a sequence (an) satisfying (2-8), (2-9)
and some quite mild additional conditions, for each k ≥ 2 the asymptotic for-
mula (2-10) holds. In fact, one gets more precise information which describes,
apart from one glaring loophole, a rather precise picture of the contribution to these
sums coming from the integers having a specified number of prime factors.
Given our sequence (an) having these properties, there exists a function δ(x),
defined up to o(1), such that the following happens. For each integer r ≥ 1 let ∑r

denote a sum restricted to positive integers with precisely r distinct prime factors.
We fix some k ≥ 2 and some r with 1 ≤ r ≤ k. Then we have
∑r

n≤x an3k(n) ∼ δ(x)k H ∑r

n≤x an(log n)
k−1. (2-12)

Moreover, the same formula holds with the same value of δ(x) for every other
r ≤ k having the same parity and with the value 2 − δ(x) for every r ≤ k having
the opposite parity.
In particular, we see that 0 ≤ δ(x) ≤ 2. As it happens, for each such real number,
one can give examples of sequences satisfying the axioms which give rise to that
particular value. We noted earlier that, for each k ≥ 2, the contribution to the sum
in (2-4) comes half from those integers with an odd number of distinct prime factors
and half from those with an even number. We can now say that this happens for the
more general sequence (an) provided that δ(x) = 1.
Bombieri goes on to show that results of the same type apply to sums over an
weighted by functions far more general, supported on almost primes. To do this he

EXCEPTIONAL ZEROS, SIEVE PARITY, GOLDBACH 19

first studies convolutions of the various 3k and finite linear combinations of these.
He then shows, using the Weierstrass approximation theorem, that quite general
normalized smooth functions f , defined at squarefree n = p1 · · · pr by

fr (n) = Fr
 ( log p1
log n , . . . , log pr
log n
 ), (2-13)

with Fr (u1, . . . , ur ) continuous and symmetric, one for each value of r, can be
closely approximated by these linear combinations. This allows him to deduce
statements for the sums ∑r

n≤x an Fr
 ( log p1
log n , . . . , log pr
log n
 ), (2-14)

similar to that for the special case (2-12). One needs some growth conditions on
the weight function (2-14) which imply that the small prime factors of n do not
make an essential contribution. For example, Fr (u1, . . . , ur ) ≪ u1 · · · ur is fine.

3. Primes in arithmetic progressions

That there are relations between the parity barrier and the existence of exceptional
zeros becomes particularly evident in connection with the study of the distribution
of primes in an arithmetic progression.
Analytic methods have so far succeeded to prove, for example,

ψ(x; q, a) = ∑

n≤x
n≡a (mod q)

3(n) = x
ϕ(q) − χ(a)
ϕ(q) x β

β + O(x exp(−c√
log x)). (3-1)

Here the second term is to be deleted if there is no exceptional zero β. When
combined with Siegel’s bound, this gives the asymptotic formula, but only with a
uniformity in q bounded by an arbitrary fixed power of log x.
For numerous applications it is desirable to have a much wider uniformity so
it is of great utility that one has at least an upper bound with that feature, the
Brun–Titchmarsh theorem, which is provided by sieve methods.
That upper bound, after years of successive improvement by a constant factor, is

π(x; q, a) = ∑

p≤x
p≡a (mod q)
 1 ≤ (2 + ε)x
ϕ(q) log(x/q) . (3-2)

The Selberg sieve and the beta sieve (see [Friedlander and Iwaniec 2010]) both give
this constant 2 and fail to do significantly better. This failure seems inevitable when
one considers that the replacement of 2 by 2 − η with a fixed positive η in a range
x > q A(η), would lead to the banishment of exceptional zeros. The proof of this

20 JOHN B. FRIEDLANDER AND HENRYK IWANIEC

result (in somewhat weaker form) is found in [Siebert 1983] with a deeper, more
precise, statement in [Granville 2020]. The basic idea is to combine (3-1) and (3-2),
the latter having been adjusted to a bound for ψ(x; q, a).
Moreover, using more sophisticated ideas, Siebert and then, in definitive form,
Granville show this result to be a special case of the following more general
statement.
The linear sieve produces specific upper and lower bound functions F(s) and
f (s) respectively, first discovered by Jurkat and Richert [1965], (see Section 12.1
of [Friedlander and Iwaniec 2010]), which apply when we are dealing with a
sequence (an), n ≤ x satisfying the linear sieve axiom (2-8) and we are sieving
by a set of primes p ≤ D1/s. It is known that these functions F, f are optimal in
general, although the specific sequences which provide a counterexample do not
resemble arithmetic progressions. Siebert, respectively Granville, show that a fixed
improvement of the value of either F(s), f (s) for any value of s, again in the case
of arithmetic progressions and with x larger than a sufficiently large power of q,
implies that exceptional zeros do not exist.
We should mention as well that Granville considers also, and in considerable
detail, the corresponding problem in which one sieves by small primes, the integers
in a short interval.
Before we leave the topic of arithmetic progressions, we draw attention to
an interesting feature of Bombieri’s sieve in this case. Naturally enough, the
results of the last section are applicable in particular to this most basic sequence
{n ≤ x; n ≡ a (mod q)}. Moreover, for this particular sequence, the level of
distribution axiom (2-9) holds uniformly in the modulus q in a much wider range
than q ≪ (log x)A, which was our limit for k = 1. Hence, we have the following
result.
For each integer k ≥ 2 and (a, q) = 1 there holds the asymptotic formula

∑

n≤x
n≡a (mod q)
 3k(n) ∼ k x
ϕ(q) (log x)
k−1, (3-3)

now valid for q in the much larger range

log q = o(log x).

The proof of this is to be found in [Friedlander 1981] for k = 2 and extends
easily to larger k. As was the situation with ζ (s), for k ≥ 2 the principal L-function
has a pole of multiple order, whereas any potential exceptional zero must be simple.
This fact offers an analytic explanation for the resulting extra level of uniformity as
compared to that for k = 1.

EXCEPTIONAL ZEROS, SIEVE PARITY, GOLDBACH 21

4. The Goldbach problem

In relation to this problem Hardy and Littlewood [1923] conjectured the following
asymptotic formula for the sum (1-2).

G(n) = ∑

m1+m2=n
2∤m1m2
 3(m1)3(m2) ∼ S(n)n, (4-1)

for n even, where

S(n) = 2 ∏

p>2

(1 − 1
( p − 1)2
 ) ∏

p | n
p>2

(
1 + 1
p − 2
 ). (4-2)

A rather weakened (though still seemingly far from reach) form of the Hardy–
Littlewood conjecture which features in our work is as follows.

Weak Hardy–Littlewood–Goldbach conjecture. For all sufficiently large even n,
we have δS(n)n < G(n) < (2 − δ)S(n)n, (4-3)

for some fixed 0 < δ < 1.

In [Friedlander and Iwaniec 2021; Friedlander et al. 2022] the following result
is proved.

Theorem. Assume that the Weak Hardy–Littlewood–Goldbach conjecture holds for
all sufficiently large even n. Then, there are no zeros of any Dirichlet L-function in
the region (1-1) with a positive constant c which is now allowed to depend on δ.

Earlier results in this direction had been given in [Fei 2016; Bhowmik et al. 2019;
Bhowmik and Halupczok 2021; Jia 2022; Goldston and Suriajaya 2021]. Those
works had narrowed the escape window for the exceptional zeros but did not close
it tightly.
In the following sections we are going to consider the arguments that lead to this
theorem but in considerably more general form.

5. A generalized Goldbach problem

We let a(ℓ), b(m) be given sequences of real numbers having some interesting
arithmetical structure and, for every n ≥ 2 we consider

F(n) = ∑

ℓ+m=n a(ℓ)b(m). (5-1)

For example, if a(ℓ) = 3(ℓ), b(m) = 3(m) for 2∤ℓm then F(n) reduces to the sum
G(n) in (1-2). We shall, in any case, be interested in the representations ℓ + m = n

22 JOHN B. FRIEDLANDER AND HENRYK IWANIEC

with ℓ, m being almost primes, hence having a number of prime factors bounded
by a fixed quantity, say r ≥ 1. From now on, some of the constants implied in our
estimates may depend on r .
In the appendix we employ heuristic arguments to predict an asymptotic formula

F(n) ∼ S(n)8(n), (5-2)

as n → ∞, n even and where 8(n) will be defined in (12-2). Then, in Section 14,
we mention somewhat weaker estimates

δS(n)8(n) < F(n) < (2 − δ)S(n)8(n), (5-3)

with a fixed 0 < δ < 1 for all even n sufficiently large. The punchline of this
heuristic thinking, as it was in [Friedlander et al. 2022], is the following.

Conclusion. The region s = σ + it with

σ ≥ 1 − c/ log q(|t| + 1) (5-4)

is free of zeros of L(s, χ) for all characters χ (mod q) and all q ≥ 3, where c = c(δ)
is a positive constant computable in terms of δ.

Remarks. Although our results are more general than those in [Friedlander et al.
2022] we shall appeal to some of the statements there without change. In particular,
the Bombieri version of zero density estimates is a key input to both works; see
(4.3) in [Friedlander et al. 2022].

Our generalization from G(n) to F(n) lets us see the parity issue of sieve methods
in a more transparent, picturesque context. The arguments we provide are amenable
to still further generalization than we have given in this work. However, this would
have made the paper more complicated and the extra results would have drifted the
topic away from this very connection.
Incidentally, one should not lose hope of proving the original Goldbach conjecture
before killing off the exceptional characters because, to this end, when one is
not worried about quantitative bounds, one can skip counting many inconvenient
representations. Ironically, the existence of exceptional characters might conceivably
help to solve the original Goldbach problem, as it does for the twin prime problem
and for other questions about prime numbers. In this connection, see as we have
mentioned earlier, [Heath-Brown 1983; Friedlander and Iwaniec 2003; 2004; 2005;
Merikoski 2021].
 EXCEPTIONAL ZEROS, SIEVE PARITY, GOLDBACH 23

6. A series of F(n)

Let N ≥ q ≥ 3. We are going to consider the series

S(N , q) = ∑

n≡0 (mod q) F(n)e−n/N (6-1)

by means of L-functions, similarly to [Goldston and Suriajaya 2021; Friedlander
and Iwaniec 2021; Friedlander et al. 2022]. First, we detect the congruence n =
ℓ + m ≡ 0 (mod q) by characters χ (mod q), getting

S(N , q) = 1
ϕ(q)
 ∑

χ (mod q) χ(−1)A(N , χ)B(N , χ) + E(N , q) (6-2)

where

A(N , χ) = ∑

ℓ χ(ℓ)a(ℓ)e−ℓ/N , B(N , χ) = ∑

m χ(m)b(m)e−m/N (6-3)

and E(N , q) is the contribution from the terms ℓ, m with (ℓm, q) ̸= 1, that is

E(N , q) = ∑ ∑

ℓ+m≡0 (mod q)
(ℓm,q)̸=1
 a(ℓ)b(m)e−(ℓ+m)/N . (6-4)

Remark. Naturally, one may think that the main part of (6-2) comes from the
principal character χ0, but the exceptional character χ1 cannot be dismissed. All the
other characters will be shown to yield a negligible contribution. The last term (6-4)
will also turn out to be negligible due to the properties of a(ℓ).

7. Properties of a(ℓ)

We assume throughout that a(ℓ) is supported on squarefree almost primes and that
a(ℓ) is quite small if ℓ has a small prime factor. We express this latter property in
the following fashion:
 a(ℓ) ≪ log p, for all p | ℓ. (7-1)

We assume that a(1) ≪ 1. As for ℓ > 1, the examples

a(ℓ) = 3(ℓ), a(ℓ) = 3r (ℓ)(log ℓ)1−r

and the r -fold convolution

a(ℓ) = (3 ∗ · · · ∗ 3)(ℓ)(log ℓ)
1−r ,

24 JOHN B. FRIEDLANDER AND HENRYK IWANIEC

all satisfy (7-1); see (2-3). Our assumption means that a(ℓ) is majorized by

C(ℓ) = ∑

p1··· pr =ℓ
p1<···< pr
 log p1, if ω(ℓ) = r ≥ 1, (7-2)

where ω(ℓ) as usual denotes the number of distinct prime factors of ℓ. For ℓ = 1
we set C(1) = 1. Note that the subsequence a(dℓ) also satisfies (7-1).

Remark. We do not assume that a(ℓ) is positive nor that it is equidistributed over
reduced residue classes except for the heuristic arguments in the Appendix. The
arguments in that section are loose and lacking in mathematical rigor. They serve
in this presentation as a motivation to expect the asymptotic formula (12-1), (12-2)
(a generalization of the Hardy–Littlewood formula for G(n)), which we use in
Section 13 to build a reliable model R(N , q) for S(N , q) and then to compare the
two in the discussions of Section 14.

Lemma 7.1. For x ≥ 2 we have
∑

ℓ≤x |a(ℓ)|ℓ−1 ≪ log x. (7-3)

Proof. For the sum over ℓ prime we have the bound

∑

p≤x
 log p
p ≪ log x. (7-4)

For the sum over ℓ having r ≥ 2 prime factors we use the bound
∑

p1··· pr ≤x
p1<···< pr
 ( p1 · · · pr )
−1 log p1 ≪ log x, (7-5)

which follows by repeated application of (7-4). □

Actually, we can derive from (7-1) the following bound.

Lemma 7.2. We have ∑

x<ℓ≤q x|a(ℓ)|ℓ−1 ≪ log q. (7-6)

Proof. If x ≤ qr the result follows from (7-3). If ℓ is prime the result follows from

∑

x<ℓ≤q x
 log p
p = log q + O(1).

Now, let ℓ = pℓ′, x < ℓ ≤ q x where ℓ′ has all of its r − 1 prime factors smaller
than p. Then, for x > qr we have ℓ′ ≤ (q x)1−1/r ≤ x 1−1/r 2. Hence, the contribution

EXCEPTIONAL ZEROS, SIEVE PARITY, GOLDBACH 25

to the sum (7-6) is bounded by
∑

ℓ′≤x 1−1/r 2
 C(ℓ′)
ℓ′ ∑

x/ℓ′< p≤q x/ℓ′
 1
p ≪ log q
log x
 ∑

ℓ′≤x
 C(ℓ′)
ℓ′ ≪ log q;

see (7-3) for the function(7-2) . □

Lemma 7.3. For x ≥ 2 we have ∑

ℓ≤x |a(ℓ)| ≪ x. (7-7)

Proof. For the sum over ℓ prime we have the bound O(x). For the sum over ℓ
having r ≥ 2 prime factors, √x < ℓ ≤ x, we estimate as follows:
∑

√x< p1··· pr ≤x
p1<···< pr
 log p1 ≪ ∑

p1··· pr −1≤x 1−1/(2r )
p1<···< pr −1
 log p1
p1 · · · pr −1
 r x
log x ≪ x.

The contribution of ℓ ≤ √x is negligible. □

By similar arguments one shows that (use the Brun–Titchmarsh theorem) that
∑

ℓ≤x
ℓ≡α (mod q)
|a(ℓ)| ≪ x
ϕ(q) if (α, q) = 1 and x ≥ qr +1. (7-8)

Lemma 7.4. For x ≥ 2 and p prime, we have
∑

p̸=ℓ≤x
ℓ≡0 (mod p)
|a(ℓ)| ≪ x
p . (7-9)

Proof. The contribution of those ℓ having all prime factors ≥ p is bounded by
(apply the sieve over the range P( p): the product of all primes less than p)
∑

p<ℓ≤x/ p
(ℓ,P( p))=1
 log p ≪ x
p log p
log p = x
p .

If p is not the smallest prime divisor of ℓ then a(ℓp) with 1 ≤ ℓ ≤ x/ p satisfies (7-1)
so, as in the proof of (7-7), we get a contribution ≪ x/ p. □

Lemma 7.5. Let r ≥ 1. For x ≥ 2 and p prime we have

∑

ℓ≤x
ℓ≡0 (mod p)
ω(ℓ)=r +1
 |a(ℓ)| ≪ x
p log p
log x
 (log
(1 + log x
log p
 ))r −1, (7-10)

where, we recall that ω(ℓ) denotes the number of distinct prime factors of ℓ.

26 JOHN B. FRIEDLANDER AND HENRYK IWANIEC

Proof. If p > √x, then (7-10) follows from (7-9). If p ≤ √x, and r = 1 then (7-10)
is obvious. If p ≤ √x, and r ≥ 2, then, using (7-5), we see that the sum is bounded
by
 ∑

p1··· pr ≤x/ p
p1<···< pr
 min(log p, log p1) ≪ x
p log x
 ∑

p1<···< pr −1<x
 min(log p, log p1)
p1 · · · pr −1

≪ x
p log p
log x
 ∑

0≤ j<r
( ∑

p< p′<x
 1
p′
 ) j

≪ x
p log p
log x
 (log log x
log p
 )r −1.
 □

Corollary 7.6. Suppose a(ℓ) is supported on squarefree numbers having at most r
prime factors and that (7-1) holds. Then, for x ≥ 2 and z ≥ 2 we have

∑

p≤z
 ∑

ℓ≤x
ℓ≡0 (mod p)
|a(ℓ)| ≪ x log z
log x
 (log
(1 + log x
log z
 ))r −1. (7-11)

Actually, for r ≥ 2 we can take the stronger exponent r − 2 rather than r − 1.

Lemma 7.7. For x ≥ 2 and q ≥ 2 we have
∑

ℓ≤x
(ℓ,q)̸=1

|a(ℓ)| ≪ x
log x (log log 2x)
r −1 log log 2q. (7-12)

Here, r ≥ 1 is the bound for the number of prime divisors of ℓ.

Proof. This follows from (7-10) and the easy bound

∑

p | q
 log p
p ≪ log log 2q.
 □

Lemma 7.8. Let d = (α, q) ̸= 1. For x ≥ q 2r +2 we have

∑

ℓ≤x
ℓ≡α (mod q)

|a(ℓ)| ≪ x log p(d)
ϕ(q) log x
 (log log x
log p(d)
 )r −1, (7-13)

where p(d) denotes the smallest prime divisor of d and the implied constant depends
only on r .
 EXCEPTIONAL ZEROS, SIEVE PARITY, GOLDBACH 27

Proof. The contribution of ℓ ≤ q 2r is negligible by (7-7). Let q 2r ≤ ℓ ≤ x. We
write ℓ = pℓ′ with ℓ′ having at most r − 1 prime divisors, each of them smaller
than p. Therefore p > q 2, ℓ′ < x 1−1/r and a(ℓ) ≪ C(ℓ′), d | ℓ′, where we recall the
definition (7-2). Since d ̸= 1, r ≥ 2. The contribution of these terms to (7-13) is
estimated as follows:
∑

ℓ′<x 1−1/r
ℓ′≡0 (mod d)
 C(ℓ′) ∑

q< p≤x/ℓ′
pℓ′≡α (mod q)
 1 ≪ x
ϕ(q/d) log x
 ∑

ℓ′≤x
ℓ′≡0 (mod d)
 C(ℓ′)
ℓ′

by the Brun–Titchmarsh theorem for primes p ≡ β (mod q/d) where βℓ′ ≡ α
(mod q). Note that (β, q/d) = 1 because p ∤q. The above sum of C(ℓ′)/ℓ′ is
estimated using the arrangements as in the proof of (7-10). Let p(d) denote the
least prime divisor of d. Then, the sum of C(ℓ′)/ℓ′ over ℓ′ ≡ 0 (mod d), ℓ′ ≤ x is
estimated by

1
d
 ∑

ℓ≤x
ω(ℓ)≤r −2
 C(dℓ)
ℓ ≤ 1
d
 ∑

0≤s≤r −2

( ∑

p1<···< ps ≤ p(d)
 log p1
p1 · · · ps
 )( ∑

p(d)< p≤x
 1
p
 )r −2−s

≪ log p(d)
d
 (
log log x
log p(d)
 )r −2.

Here, if s = 0 the sum over p1 < · · · < ps is taken to have the value 1.
This completes the proof of (7-13), using dϕ(q/d) ≥ ϕ(q). □

8. Properties of b(m)

We could work with b(m) as with a(ℓ) but for simplicity (in order to apply (3.3) of
[Friedlander et al. 2022] without modification) we shall assume that

b(m) = ∑

hk=m λ(h)3(k), (8-1)

where λ(h) is supported on squarefree almost primes and

λ(h) ≪ log p for all p | h. (8-2)

We take λ(1) = 1. If h > 1, for example, λ(h) = 3r (h)(log h)1−r is good. Note
that λ(h) satisfies (7-3)–(7-13). Moreover, we have
∑

m≤x|b(m)| ≪ x log x (8-3)

for every x ≥ 2, because ∑

h≤x|λ(h)|h−1 ≪ log x, (8-4)

28 JOHN B. FRIEDLANDER AND HENRYK IWANIEC

by (7-3) for the lambda function. Actually, we have the stronger result
∑

x<h≤q x|λ(h)|h−1 ≪ log q, (8-5)

for every x ≥ 2; see (7-6) for the lambda function.

Remark. Many interesting functions supported on almost primes can be well-
approximated by sums of functions like λ ∗ 3. For example, we can take

b(m) = Fr
 ( log p1
log m , . . . , log pr
log m
 )
(log m)
2

if m = p1 · · · pr , where we recall Fr in (2-13) is as in Bombieri’s asymptotic sieve;
see Chapters 3 and 16 of [Friedlander and Iwaniec 2010].

In the case b(m) = 3(m) we have λ(h) = 0 except for λ(1) = 1. Therefore,
in this special case some of our estimates can be improved by a log factor from
those displayed. In particular, in (8-3) the factor log x can be removed and in (8-4)
the “sum” is bounded. In the arguments of the following sections, this special
case is therefore much easier, yet the need for these slightly stronger bounds
would complicate the exposition. Since the results for this particular example are
anyway just those already given in [Friedlander et al. 2022], we omit them from
this presentation.
 9. Evaluation of S(N, q), first steps

Let χ1 (mod q) be a real primitive character of modulus q such that L(s, χ1) has a
simple real zero β1 close to s = 1. We single out the contributions of χ0 and χ1
to (6-2) and estimate the remaining parts as follows:

Q(N , q) = ∑

χ ̸=χ0,χ1 χ(−1)A(N , χ)B(N , χ) = S(H, N , q) + T (H, N , q), (9-1)

say, where S(H, N , q) is the partial sum restricted to h ≤ H and T (H, N , q) is the
complementary partial sum. The first one is bounded by
(∑

ℓ |a(ℓ)|e−ℓ/N ) ∑

h≤H|λ(h)| ∑

χ̸=χ0,χ1
∣
∣
∣
∣
∑

k χ(k)3(k)e−hk/N ∣
∣
∣
∣. (9-2)

The sum over ℓ in (9-2) is bounded by O(N ); see (7-7). The sum over k is (3.3)
from [Friedlander et al. 2022], so it satisfies

∑

χ ̸=χ0,χ1
∣
∣
∣
∣∑

k χ(k)3(k)e−hk/N ∣
∣
∣
∣ ≪ N
h (1 − β1) log q, (9-3)

EXCEPTIONAL ZEROS, SIEVE PARITY, GOLDBACH 29

provided that N h−1 ≥ q b for a suitably large b; see (5.1) and (3.5) of [Friedlander
et al. 2022]. This condition is satisfied for N ≥ H q b. Hence, we get

S(H, N , q) ≪ N 2(1 − β1)(log q)(log H ). (9-4)

Recall that (9-3) exploits the Bombieri zero density theorem with the repulsion
effect of the exceptional zero β1. We do not apply this effect, nor do we need it, for
the estimation of T (H, N , q). We write

T (H, N , q) = ∑

χ ̸=χ0,χ1
χ(−1)
(∑

ℓ a(ℓ)χ(ℓ)e−ℓ/N ) ∑

h>H
 ∑

k χ(hk)λ(h)3(k)e−hk/N.

Hence, inserting the corresponding sum for the missing two characters and using
orthogonality, we find that

T (H, N , q)

= ϕ(q) ∑ ∑ ∑

ℓ+hk≡0 (mod q)
(ℓ,q)=1, h>H
 a(ℓ)λ(h)3(k)e−(ℓ+hk)/N + O(N 2 ∑

h>H|λ(h)|h−1e−h/2N )
,

on using the trivial bound for the contribution of the two additional characters.
Using (7-8), we see that the above main term is also bounded by the above error
term. Moreover, this error term is ≪ N 2 log(N /H ), as seen by applying (8-5) for
x = H, q H, q 2 H, . . . . Choosing H = N q −b we conclude that

T (H, N , q) ≪ N 2 log q. (9-5)

On adding these estimates (9-4) and(9-5), we see that the sum in (9-1) satisfies
Q(N , q) ≤ ε(N , q)N 2 log N where

ε(N , q) ≪ (1 − β1) log q + log q
log N . (9-6)

We still need to estimate E(N , q) in (6-2) which is given by (6-4). This term
is negligible and is actually smaller than the main term by a saving factor log N .
Nevertheless, we give simpler arguments producing an estimate somewhat weaker,
yet still sufficient for our applications; see (9-7) and (9-8). Recall that a(ℓ), λ(h)
are supported on squarefree numbers having at most r prime divisors. By (7-13)
we obtain
 |E(N , q)| ≤ ∑

d | q
d̸=1
 ∑ ∑

ℓ+m≡0 (mod q)
(m,q)=d
 |a(ℓ)b(m)|e−(ℓ+m)/N

≪ N
ϕ(q) (log log N )r −1

log N
 ∑

d | q
d̸=1
(log p(d))W (N , d)

30 JOHN B. FRIEDLANDER AND HENRYK IWANIEC

where

W (N , d) = ∑

m≡0 (mod d)|b(m)|e−m/N ≤ ∑

uv=d
 ∑ ∑

h≡0 (mod u)
k≡0 (mod v)
 λ(h)3(k)e−hk/N .

Since k is prime we have v = 1 or v = k. The sum with v = 1 contributes

W1(N , d) = ∑

h≡0 (mod d) λ(h) ∑

k 3(k)e−hk/N

≪ ∑

h≡0 (mod d)|λ(h)|h−1e−h/2N

≪ log d
d N (log log N )
r −1,

by the trivial bound λ(h) ≪ log d. Then we need, here and later, the easy bound
∑

d | q (log d)
2d −1 ≪ (log log q)
3.

Next, the sum with v = k contributes

W2(N , d) = ∑

uv=d 3(v) ∑

h≡0 (mod u)|λ(h)|e−hv/N .

The partial sum of W2(N , d) with u = 1 is

W21(N , d) = 3(d) ∑

h |λ(h)|e−dh/N ≪ 3(d)
d N ;

see (7-7) for the λ function. The remaining part of W2(N , d) is

W22(N , d) = ∑

uv=d
u̸=1
 3(v) ∑

h≡0 (mod u)|λ(h)|e−hv/N .

Hence, ∑

d | q (log p(d))W22(N , d) ≤ ∑

uv | q 32(v) ∑

u | h
(h,q)̸=1

|λ(h)|e−hv/N

≪ ∑

v | q 32(v) ∑

(h,q)̸=1
|λ(h)|e−hv/N

because τ (h) ≪r 1. Applying (7-12), we find this is bounded by
(∑

v | q
 32(v)
v
 ) N
log N (log log N )
r ≪ N
log N (log log N )
r +3.

EXCEPTIONAL ZEROS, SIEVE PARITY, GOLDBACH 31

Gathering the above estimates, we obtain

E(N , q) ≪ N 2

ϕ(q) (log log N )2r +2

log N . (9-7)

This is stronger than we needed, namely

E(N , q) ≪ N 2 log q
ϕ(q) . (9-8)

Now, (6-2) becomes

ϕ(q)S(N , q)

= A(N , χ0)B(N , χ0) + χ1(−1)A(N , χ1)B(N , χ1) + (ε(N , q)N 2 log N ). (9-9)

The coprimality of ℓ, m with q in the main term A(N , χ0)B(N , χ0) can be dropped
within the existing error term, specifically

A(N , χ0) = A(N , 1) + O(N (log log N )r

log N
 ) (9-10)

and B(N , χ0) = B(N , 1) + O(N (log log N )
r ), (9-11)

by direct applications of (7-12) for a(ℓ) and b(m)/ log N respectively. Note that
(log log N )r ≪ (log(log N / log q))r log q.

10. Evaluation of A(N, χ1) and B(N, χ1)

The exceptional character pretends to be the Möbius function on squarefree numbers,
so we are able to replace
A(N , χ1) = ∑

ℓ χ1(ℓ)a(ℓ)e−ℓ/N (10-1)

by
 A(N , µ) = ∑

ℓ µ(ℓ)a(ℓ)e−ℓ/N . (10-2)

In this section we use the Linnik zero repulsion phenomenon (see [Bombieri 1987])
to estimate the error caused in making this replacement. For ℓ squarefree we have

|χ1(ℓ) − µ(ℓ)| ≤ ∑

p | ℓ(1 + χ1( p)). (10-3)

Hence

|A(N , χ1) − A(N , µ)| ≤ ∑

p (1 + χ1( p)) ∑

ℓ≡0 (mod p)|a(ℓ)|e−ℓ/N . (10-4)

32 JOHN B. FRIEDLANDER AND HENRYK IWANIEC

The contribution of ℓ = p is bounded by 9(N ), where

9(y) = ∑

p (1 + χ1( p))(log p)e− p/y. (10-5)

For y ≥ z = q b we have (apply (5.3) of [Friedlander et al. 2022]):

9(y) ≪ (1 − β1)y log y + y(log y)−1. (10-6)

For p > z and N > z we write

e−ℓ/N ≤ e−ℓ/2N e− p/2N ≤ 6e−ℓ/2N (e− p/2N − e− p/z).

Hence, the terms ℓ, p with ℓ ̸= p > z contribute to (10-4) at most

N
log N
 (
log(1 + log N
log z
 ))r −1 ∑

p (1 + χ1( p)) log p
p (e− p/2N − e− p/z) (10-7)

by (7-10). The sum over all p above is equal to
∫ 2N

z 9(y)y−2dy ≪ (1 − β1)(log N )
2 + log( log 2N
log z
 )

by (10-6). Hence (10-7) is bounded by

N (log
(1 + log N
log z
 ))r (
(1 − β1) log N + 1
log N
 ). (10-8)

For p ≤ z we use (7-11) obtaining a contribution to (10-4) at most

N log z
log N
 (
log(1 + log N
log z
 ))r . (10-9)

Combining estimates (10-6), (10-7), (10-9), we conclude that, if N ≥ q b, then

|A(N , χ1) − A(N , µ)| ≪ η(N , q)N (10-10)

where
 η(N , q) ≪ ((1 − β1) log N + log q
log N
 )(log log N
log q
 )r . (10-11)

Similarly, we can replace B(N , χ1) by B(N , µ). Since the function b(m)/ log N
satisfies, for m ≤ N 2021, the same conditions as a(ℓ), hence the same arguments as
those between (10-3) and (10-11) yield

|B(N , χ1) − B(N , µ)| ≪ η(N , q)N log N , (10-12)

where η(N , q) satisfies (10-11), the contribution of m > N 2021 being microscopic.

EXCEPTIONAL ZEROS, SIEVE PARITY, GOLDBACH 33

11. Evaluation of S(N, q), conclusion

Collecting the results of the last two sections we formulate our basic result:

Proposition 11.1. Let a(ℓ) and b(m) be supported on squarefree numbers having
at most r prime factors. Suppose (7-1), (8-1), (8-2) hold. Then, for N ≥ q b with a
suitable constant b, we have

ϕ(q)S(N , q) = A(N , 1)B(N , 1) + χ1(−1)A(N , µ)B(N , µ) + η(N , q)N 2 log N
(11-1)
with
 η(N , q) ≪ ((1 − β1) log N + log q
log N
 )(log log N
log q
 )r , (11-2)

the implied constant depending on r and where χ1 (mod q) is the exceptional
character and β1 is the zero of L(s, χ1) in the segment

1 − c(log q)
−1 < β1 < 1 (11-3)

with c a small positive constant.

Proof. In (9-9) use (9-10), (9-11) to replace χ0 by 1, use (10-10) and (10-12) to
replace χ1 by µ. □

In case b(m) = 3(m) we have λ(h) = 0 except for λ(1) = 1 and, as mentioned in
Section 8, in this special, much easier case some of our estimates can be improved
by a log factor from those displayed. As an upshot, our final formula (11-1) holds
with the error term η(N , q)N 2.
For N = q A with A a large exponent we have

η(N , q) ≪ (A(1 − β1) log q + A−1)(log A)
r . (11-4)

Given δ > 0 we can make |η(N , q)| < δ (11-5)

if the exceptional zero satisfies (11-3) with c sufficiently small:

A ≍ 1
δ
 (log 1
δ
 )r , c ≤ A−2. (11-6)

We can write (11-1) in the form

ϕ(q)S(N , q) = ∑

ℓ
 ∑

m (1+χ1(−1)µ(ℓm))a(ℓ)b(m)e−(ℓ+m)/N +η(N , q)N 2 log N ,

(11-7)
where η(N , q) satisfies (11-2).

34 JOHN B. FRIEDLANDER AND HENRYK IWANIEC

Remarks. Our conditions on a(ℓ) and λ(h) imply that A(N , 1) ≪ N and B(N , 1) ≪
N log N . However, the formula (11-1) is meaningful if

A(N , 1) ≍ N , B(N , 1) ≍ N log N , for N ≥ q b. (11-8)

As we have already mentioned, the factor log N in the error term of (11-1) can be
deleted if b(m) = 3(m). This is the case of λ(h) = 30(h), which function vanishes
except for λ(1) = 30(1) = 1.

12. Asymptotic formula for F(n): prediction

Recall that F(n) is given by (5-1) with a(ℓ) satisfying (7-1) and b(m) given by (8-1)
with λ(h) satisfying (8-2). As such, F(n) is a generalization of the Goldbach sum
so it is too much to be expected to evaluate it unconditionally. Nevertheless, in the
Appendix we show heuristic arguments which permit us to predict the following
generalization of the Hardy–Littlewood conjecture (4-1).

Corollary. Under the above-mentioned (in Sections 7 and 8) conditions on the
sequences a(ℓ), b(m) = (λ ∗ 3)(m), we have

F(n) = ∑

ℓ+m=n a(ℓ)b(m) ∼ S(n)8(n) (12-1)

as n → ∞, n even, where S(n) is given by (4-2) and

8(n) = ∑ ∑

ℓ+h<n a(ℓ)λ(h)h−1. (12-2)

Examples. If b(m) = 3(m), we have λ(1) = 1, λ(h) = 0 for h > 1. Hence

8(n) = ∑

ℓ<n−1 a(ℓ).

Moreover, if a(ℓ) = 3(ℓ) then we have 8(n) ∼ n and

F(n) = G(n) = ∑

ℓ+m=n 3(ℓ)3(m) ∼ S(n)n, (12-3)

recovering (4-1). More generally, keeping b(m) = 3(m) but choosing a(ℓ) =
3k(ℓ)/(log n)k−1, we have

F(n) = ∑

ℓ+m=n a(ℓ)3(m) ∼ kS(n)n. (12-4)

EXCEPTIONAL ZEROS, SIEVE PARITY, GOLDBACH 35

13. Evaluation of R(N, q)

Injecting the asymptotic formula (12-1) into the series (6-1) we obtain the following
model for S(N , q):

R(N , q) = ∑

n≡0 (mod q) S(n)8(n)e−n/N

= ∑

ℓ
 ∑

h a(ℓ)λ(ℓ)h−1 ∑

n≡0 (mod q)
ℓ+h<n, n even
 S(n)e−n/N . (13-1)

Using (6.5) of [Friedlander et al. 2022] one can derive the asymptotic formula
∑

n≡0 (mod q)
n≤x, n even
 S(n) ∼ x
ϕ(q) .

Hence, the last sum over n in (13-1) is asymptotic to

∼ 1
ϕ(q)
 ∫ ∞

ℓ+h e−x/N d x = N
ϕ(q) e−(ℓ+h)/N

and
 ϕ(q)R(N , q) ∼ N (∑

ℓ a(l)e−ℓ/N )(∑

h λ(h)h−1e−h/N )
. (13-2)

On the other hand, we have

B(N , 1) = ∑

m b(m)e−m/N = ∑

h λ(h) ∑

k 3(k)e−hk/N ∼ N ∑

h λ(h)h−1e−h/N .

Hence, (13-2) becomes
 ϕ(q)R(N , q) ∼ A(N , 1)B(N , 1). (13-3)

This should be compared with (11-1) subject to the conditions (11-8).

14. Exceptional zero effects

It is instructive to observe what happens if we compare the legitimate formula (11-1)
with the heuristic (13-3) in the range N = q A. Take A sufficiently large and assume,
as we may, that the exceptional constant c ≤ A−2 so that η(N , q) is negligible. It
follows that A(N , µ)B(N , µ) is significantly smaller than A(N , 1)B(N , 1). This
observation is attractive if the coefficients a(ℓ), b(m) are each supported on almost
primes having a fixed parity in the number of their prime divisors, because the

36 JOHN B. FRIEDLANDER AND HENRYK IWANIEC

Möbius function is then constant and

A(N , µ) = µA A(N , 1) where µA = ±1,

B(N , µ) = µB B(N , 1) where µB = ±1.

Hence
 |A(N , µ)B(N , µ)| = |A(N , 1)B(N , 1)|

and
 ϕ(q)S(N , q) = ν A(N , 1)B(N , 1) + o(N 2 log N )

with ν = 0 or 2. This inconsistency with (13-3) implies that the exceptional character
does not exist! Indeed, it means that one may, a fortiori, kill the exceptional
character by assuming the weaker conjecture (5-3) with any 0 < δ < 1, under
suitable conditions on the coefficients a(ℓ), b(m), as has been done in [Friedlander
and Iwaniec 2021] and [Friedlander et al. 2022] for a(ℓ) = 3(ℓ), b(m) = 3(m).
If, on the other hand, we choose instead a(ℓ) = 3a(ℓ)(log ℓ)1−a and λ(h) =
3b(h)(log h)1−b with numbers a + b > 2, that is not both 1, then the effect on the
exceptional zero no longer shows itself in our arguments. The point is that the series

∑

ℓ 3a(ℓ)ℓ
−s = (−1)
a ζ (s)(a)

ζ (s)

has a pole at s = 1 of order a, while the series

∑

ℓ µ(ℓ)3a(ℓ)ℓ
−s = ζ (s) ∑

n
 µ(n)
ns (log n)
a ∏

p | n
(1 − 1
ps
 )

has only a simple pole at s = 1 for any a ≥ 1. Hence A(N , µ) is smaller than A(N , 1)
by a factor (log N )a−1, so it yields a negligible contribution if a ≥ 2. Similarly
for B(N , µ) if b ≥ 2. This is the same feature which, in the case of arithmetic
progressions, led to the wider range of uniformity in Selberg’s formula (2-4) and,
more generally, in (3-3).
In view of the above, our formula (11-1) is relevant to the issue of exceptional
characters only if its coefficients a(ℓ), b(m), can be approximated, via the Weier-
strass theorem, by linear combinations of scaled down 3a(ℓ), 3b(m), in which
a = b = 1 appears (cannot be canceled out). The components with a + b > 2 can
be dismissed in (the highest order term of) A(N , µ)B(N , µ).
We encourage the reader to learn the Bombieri approximations by the von Man-
goldt functions from the original paper [Bombieri 1976] and to look at Chapters 3
and 16 of [Friedlander and Iwaniec 2010]; see also [Friedlander and Iwaniec 1985],
especially Section 20.

EXCEPTIONAL ZEROS, SIEVE PARITY, GOLDBACH 37

Appendix: Heuristic arguments

Again we recall that F(n) is given by (5-1) with a(ℓ) satisfying (7-1) and b(m)
given by (8-1) with λ(ℓ) satisfying (8-2). The coefficients a(ℓ), b(m) are small if ℓ,
m have small prime divisors so we can assume that ℓ, m are odd and that n = ℓ + m
is even. We write 3(k) = − ∑

d | k µ(d) log d

and replace b = λ ∗ 3 by
 − ∑

dh | m
d<y
 λ(h)µ(d) log d,

where y is neither too small nor too large. Next, we interpret the equation ℓ+m = n
by the congruence ℓ ≡ n (mod dh) with (ℓ, n) = 1, ℓ < n and (dh, n) = 1. Arguing
by the randomness of µ(n), we replace F(n) by

− ∑

d<y
(d,n)=1
 µ(d) log d ∑

h<n/d
(h,n)=1
 λ(h) ∑

ℓ<n−dh, (ℓ,n)=1
ℓ≡n (mod dh)
 a(ℓ).

Next, assuming the equidistribution of a(ℓ) over reduced residue classes, we replace
the sum over ℓ by 1
ϕ(dh)
 ∑

ℓ<n−dh,
(ℓ,n)=1
 a(ℓ).

We may think of ℓ < n as being not very close to n because otherwise m = n − ℓ
would be very small, hence so would b(m). Similarly, h < n − ℓ should not be
close to n − ℓ because otherwise k = (n − ℓ)/ h would be very small. Therefore,
the sum over d,
 − ∑

d<y, dh<n−ℓ
(d,n)=1
 µ(d)
ϕ(d) log d,

is not short, so it is reasonable to replace it by the infinite series

− ∑

(d,n)=1
 µ(d)
ϕ(d) log d = S(n);

see for example Lemma 19.3 of [Iwaniec and Kowalski 2004]. Now, we can drop
the restriction (ℓh, n) = 1 because a(ℓ), λ(h) are supported on almost primes and
are relatively small if ℓ, h have any small prime divisors. For the same reason, we
have already replaced ϕ(dh) by ϕ(d)h.

38 JOHN B. FRIEDLANDER AND HENRYK IWANIEC

The above lines show how we are led to the conjecture (12-1). The arguments of
Hardy and Littlewood are rather different. They approach the issue by way of the
circle method rather than using the randomness of the Möbius function.

Acknowledgement

We thank D.A. Goldston and A.I. Suriajaya whose preprint [Goldston and Suriajaya
2021] sparked our interest in the relevence to the Goldbach problem of the question
of exceptional zeros, leading to the joint paper [Friedlander et al. 2022] and to the
current work.
We thank Lillian Pierce for having invited us to submit this work on the occasion
of the inauguration of her exciting new journal.
We thank the referees for many interesting suggestions.

References

[Bhowmik and Halupczok 2021] G. Bhowmik and K. Halupczok, “Conditional bounds on Siegel
zeros”, pp. 25–39 in Combinatorial and additive number theory IV, edited by M. B. Nathanson,
Springer Proc. Math. Stat. 347, Springer, 2021. MR

[Bhowmik et al. 2019] G. Bhowmik, K. Halupczok, K. Matsumoto, and Y. Suzuki, “Goldbach
representations in arithmetic progressions and zeros of Dirichlet L-functions”, Mathematika 65:1
(2019), 57–97. MR Zbl

[Bombieri 1976] E. Bombieri, “The asymptotic sieve”, Rend. Accad. Naz. XL (5) 1(2) (1976),
243–269. MR Zbl

[Bombieri 1987] E. Bombieri, “Le grand crible dans la théorie analytique des nombres”, pp. i+87
Astérisque 18, Soc. Mat. de France, Paris, 1987. 2ieme ed. MR Zbl

[Fei 2016] J. Fei, “An application of the Hardy–Littlewood conjecture”, J. Number Theory 168 (2016),
39–44. MR Zbl

[Friedlander 1976] J. B. Friedlander, “On the class numbers of certain quadratic extensions”, Acta
Arith. 28:4 (1976), 391–393. MR

[Friedlander 1981] J. B. Friedlander, “Selberg’s formula and Siegel’s zero”, pp. 15–23 in Recent
progress in analytic number theory (Durham, 1979), vol. 1, edited by H. Halberstam and C. Hooley,
Academic Press, London, 1981. MR

[Friedlander and Iwaniec 1978] J. Friedlander and H. Iwaniec, “On Bombieri’s asymptotic sieve”,
Ann. Scuola Norm. Sup. Pisa Cl. Sci. (4) 5:4 (1978), 719–756. MR

[Friedlander and Iwaniec 1985] J. B. Friedlander and H. Iwaniec, “Incomplete Kloosterman sums
and a divisor problem”, Ann. of Math. (2) 121:2 (1985), 319–350. With an appendix by Bryan J.
Birch and Enrico Bombieri. MR

[Friedlander and Iwaniec 1996] J. Friedlander and H. Iwaniec, “Bombieri’s sieve”, pp. 411–430 in
Analytic number theory (Allerton Park, IL, 1995), vol. 1, edited by B. C. Berndt et al., Progr. Math.
138, Birkhäuser, Boston, 1996. MR Zbl

[Friedlander and Iwaniec 2003] J. B. Friedlander and H. Iwaniec, “Exceptional characters and prime
numbers in arithmetic progressions”, Int. Math. Res. Not. 2003:37 (2003), 2033–2050. MR

[Friedlander and Iwaniec 2004] J. B. Friedlander and H. Iwaniec, “Exceptional characters and prime
numbers in short intervals”, Selecta Math. (N.S.) 10:1 (2004), 61–69. MR

EXCEPTIONAL ZEROS, SIEVE PARITY, GOLDBACH 39

[Friedlander and Iwaniec 2005] J. B. Friedlander and H. Iwaniec, “The illusory sieve”, Int. J. Number
Theory 1:4 (2005), 459–494. MR

[Friedlander and Iwaniec 2010] J. Friedlander and H. Iwaniec, Opera de cribro, American Mathemat-
ical Society Colloquium Publications 57, American Mathematical Society, Providence, RI, 2010.
MR Zbl

[Friedlander and Iwaniec 2021] J. Friedlander and H. Iwaniec, “Note on a note of Goldston and
Suriajaya”, preprint, 2021. arXiv 2105.09038

[Friedlander et al. 2022] J. B. Friedlander, D. A. Goldston, H. Iwaniec, and A. I. Suriajaya, “Excep-
tional zeros and the Goldbach problem”, J. Number Theory 233 (2022), 78–86. MR

[Goldston and Suriajaya 2021] D. A. Goldston and A. I. Suriajaya, “Note on the Goldbach conjecture
and Landau–Siegel zeros”, preprint, 2021. arXiv 2104.09407v1

[Granville 2020] A. Granville, “Sieving intervals and Siegel zeros”, preprint, 2020. arXiv 2010.01211

[Hardy and Littlewood 1923] G. H. Hardy and J. E. Littlewood, “Some problems of ‘Partitio numero-
rum’; III: On the expression of a number as a sum of primes”, Acta Math. 44:1 (1923), 1–70. MR
Zbl

[Heath-Brown 1983] D. R. Heath-Brown, “Prime twins and Siegel zeros”, Proc. London Math. Soc.
(3) 47:2 (1983), 193–224. MR Zbl

[Iwaniec and Kowalski 2004] H. Iwaniec and E. Kowalski, Analytic number theory, American
Mathematical Society Colloquium Publications 53, American Mathematical Society, Providence, RI,
2004. MR Zbl

[Jia 2022] C. H. Jia, “On the conditional bounds for Siegel zeros”, Acta Math. Sin. (Engl. Ser.) 38:5
(2022), 869–876. MR Zbl

[Jurkat and Richert 1965] W. B. Jurkat and H.-E. Richert, “An improvement of Selberg’s sieve
method, I”, Acta Arith. 11 (1965), 217–240. MR Zbl

[Merikoski 2021] J. Merikoski, “Exceptional characters and prime numbers in sparse sets”, preprint,
2021. arXiv 2108.01355

[Siebert 1983] H. Siebert, “Sieve methods and Siegel’s zeros”, pp. 659–668 in Studies in pure
mathematics, edited by P. Erd˝os, Birkhäuser, Basel, 1983. MR Zbl

[Zhang 2014] Y. Zhang, “Bounded gaps between primes”, Ann. of Math. (2) 179:3 (2014), 1121–1174.
MR Zbl

Received 24 Aug 2021. Revised 22 Dec 2021.

JOHN B. FRIEDLANDER:

frdlndr@math.toronto.edu
Department of Mathematics, University of Toronto, Toronto, ON, Canada

HENRYK IWANIEC:

iwaniec@comcast.net
Department of Mathematics, Rutgers University, Piscataway, NJ, United States
 msp

ESSENTIAL NUMBER THEORY
 msp.org/ent

EDITOR-IN-CHIEF

Lillian B. Pierce Duke University
pierce@math.duke.edu

EDITORIAL BOARD

Adebisi Agboola UC Santa Barbara
agboola@math.ucsb.edu

Valentin Blomer Universität Bonn
ailto:blomer@math.uni-bonn.de

Ana Caraiani Imperial College
a.caraiani@imperial.ac.uk

Laura DeMarco Harvard University
demarco@math.harvard.edu

Ellen Eischen University of Oregon
eeischen@uoregon.edu

Kirsten Eisenträger Penn State University
kxe8@psu.edu

Amanda Folsom Amherst College
afolsom@amherst.edu

Edray Goins Pomona College
edray.goins@pomona.edu

Kaisa Matomäki University of Turku
ksmato@utu.fi

Sophie Morel ENS de Lyon
sophie.morel@ens-lyon.fr

Raman Parimala Emory University
parimala.raman@emory.edu

Jonathan Pila University of Oxford
jonathan.pila@maths.ox.ac.uk

Peter Sarnak Princeton University/Institute for Advanced Study
sarnak@math.princeton.edu

Richard Taylor Stanford University
rltaylor@stanford.edu

Anthony Várilly-Alvarado Rice University
av15@rice.edu

Akshay Venkatesh Institute for Advanced Study
akshay@math.ias.edu

John Voight Dartmouth College
john.voight@dartmouth.edu

Melanie Matchett Wood Harvard University
mmwood@math.harvard.edu

Zhiwei Yun MIT
zyun@mit.edu

Tamar Ziegler Hebrew University
tamar.ziegler@mail.huji.ac.il

PRODUCTION

Silvio Levy (Scientific Editor)
production@msp.org

See inside back cover or msp.org/ent for submission instructions.

Essential Number Theory (ISSN 2834-4634 electronic, 2834-4626 printed) at Mathematical Sciences Publishers,
798 Evans Hall #3840, c/o University of California, Berkeley, CA 94720-3840 is published continuously online.

ENT peer review and production are managed by EditFlow® from MSP.

PUBLISHED BY
mathematical sciences publishers
nonprofit scientific publishing
https://msp.org/
© 2022 Mathematical Sciences Publishers

ESSENTIAL NUMBER THEORY

2022 vol. 1 no. 1
 1The cubic case of Vinogradov’s mean value theorem
D. R. HEATH-BROWN 13Exceptional zeros, sieve parity, Goldbach
JOHN B. FRIEDLANDER and HENRYK IWANIEC 41A note on Tate’s conjectures for abelian varieties
CHAO LI and WEI ZHANG 51A Diophantine problem about Kummer surfaces
WILLIAM DUKE 57Quartic index form equations and monogenizations of quartic orders
SHABNAM AKHTARI 73Modularity lifting theorems
TOBY GEE

ESSENTIAL NUMBER THEORY2022vol.1no.1
