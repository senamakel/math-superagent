<!-- source: https://arxiv.org/pdf/1201.6656 | converted from PDF -->

arXiv:1201.6656v4  [math.NT]  3 Jul 2012
EVERY ODD NUMBER GREATER THAN 1 IS THE SUM OF AT
MOST FIVE PRIMES

TERENCE TAO

Abstract. We prove that every odd number N greater than 1 can be expressed as
the sum of at most ﬁve primes, improving the result of Ramar´e that every even natural
number can be expressed as the sum of at most six primes. We follow the circle method
of Hardy-Littlewood and Vinogradov, together with Vaughan’s identity; our additional
techniques, which may be of interest for other Goldbach-type problems, include the use
of smoothed exponential sums and optimisation of the Vaughan identity parameters to
save or reduce some logarithmic losses, the use of multiple scales following some ideas
of Bourgain, and the use of Montgomery’s uncertainty principle and the large sieve
to improve the L2 estimates on major arcs. Our argument relies on some previous
numerical work, namely the veriﬁcation of Richstein of the even Goldbach conjecture
up to 4 × 1014, and the veriﬁcation of van de Lune and (independently) of Wedeniwski
of the Riemann hypothesis up to height 3.29 × 109.

1. Introduction

Two of most well-known conjectures in additive number theory are the even and odd
Goldbach conjectures, which we formulate as follows
1:

Conjecture 1.1 (Even Goldbach conjecture). Every even natural number x can be
expressed as the sum of at most two primes.

Conjecture 1.2 (Odd Goldbach conjecture). Every odd number x larger than 1 can be
expressed as the sum of at most three primes.

It was famously established by Vinogradov [47], using the Hardy-Littlewood circle
method, that the odd Goldbach conjecture holds for all suﬃciently large odd x. Vino-
gradov’s argument can be made eﬀective, and various explicit thresholds for “suﬃciently
large” have been given in the literature; in particular, Chen and Wang [5] established the
odd Goldbach conjecture for all x ⩾ exp(exp(11.503)) ≈ exp(99012), and Liu & Wang
[24] subsequently extended this result to the range x ⩾ exp(3100). At the other extreme,
by combining Richstein’s numerical veriﬁcation [41] of the even Goldbach conjecture for
x ⩽ 4 × 1014 with eﬀective short intervals containing primes (based on a numerical
veriﬁcation of the Riemann hypothesis by van de Lune and Wedeniwski [50]), Ramar´e
and Saouter [40] veriﬁed the odd Goldbach conjecture for n ⩽ 1.13 × 1022 ≈ exp(28).
By using subsequent numerical veriﬁcations of both the even Goldbach conjecture and
the Riemann hypothesis, it is possible to increase this lower threshold somewhat, but

1The odd Goldbach conjecture is also often formulated in an almost equivalent (and slightly stronger)
fashion as the assertion that every odd number greater than seven is the sum of three odd primes.
1

2 TERENCE TAO

there is still a very signiﬁcant gap between the lower and upper thresholds for which
the odd Goldbach conjecture is known
2.

To explain the reason for this, let us ﬁrst quickly recall how Vinogradov-type theorems
are proven. To represent a number x as the sum of three primes, it suﬃces to obtain a
suﬃciently non-trivial lower bound for the sum
∑

n1,n2,n3:n1+n2+n3=x Λ(n1)Λ(n2)Λ(n3)

where Λ is the von Mangoldt function (see Section 2 for deﬁnitions). By Fourier analysis,
we may rewrite this expression as the integral
∫
R/Z S(x, α)3e(−xα) dα (1.1)

where e(x) := e
2πix and S(x, α) is the exponential sum

S(x, α) := ∑

n⩽x Λ(n)e(nα).

The objective is then to obtain suﬃciently precise estimates on S(x, α) for large x. Using
the Dirichlet approximation theorem, one can approximate α = a
q + β for some natural
number 1 ⩽ q ⩽ Q, some integer a with (a, q) = 1, and some β with |β| ⩽ 1
qQ, where Q
is a threshold (somewhat close to N) to be chosen later. Roughly speaking, one then
divides into the major arc case when q is small, and the minor arc case when q is large
(in practice, one may also subdivide these cases into further cases depending on the
precise sizes of q and β). In the major arc case, the sum S(x, α) can be approximated
by sums such as
 S(x, a/q) = ∑

n⩽x Λ(n)e(an/q),

which can be controlled by a suitable version of the prime number theorem in arithmetic
progressions, such as the Siegel-Walﬁsz theorem. In the minor arc case, one can instead
follow the methods of Vinogradov, and use truncated divisor sum identities (such as
(variants of) Vaughan’s identity, see Lemma 4.11 below) to rewrite S(x, α) into various
“type I” sums such as ∑

d⩽U µ(d) ∑

n⩽x/d log ne(αdn)

and “type II” sums such as∑

d>U
 ∑

w>V µ(d)( ∑

b|w:b>V Λ(b))e(αdw) (1.2)

which one then estimates by standard linear and bilinear exponential sum tools, such
as the Cauchy-Schwarz inequality.

2We remark however that the odd Goldbach conjecture is known to be true assuming the generalised
Riemann hypothesis; see [9].

EVERY ODD NUMBER GREATER THAN 1 IS THE SUM OF AT MOST FIVE PRIMES 3

A typical estimate in the minor arc case takes the form

|S(x, α)| ≪
 ( x
√q + x
√
x/q + x
4/5)
 log3 x; (1.3)

see e.g. [19, Theorem 13.6]. An eﬀective version of this estimate (with slightly diﬀerent
logarithmic powers) was given by Chen & Wang [6]; see (1.13) below. Note that one

cannot hope to obtain a bound for S(x, α) that is better than x√φ(q)
q without making
progress on the Siegel zero problem (in order to decorrelate Λ from the quadratic char-
acter with conductor q); see [35] for further discussion. In a similar spirit, one should
not expect to obtain a bound better than x√x/q unless one exploits a non-trivial error

term in the prime number theorem for arithmetic progressions (or equivalently, if one
shows that L-functions do not have a zero on the line ℜs = 1), as one needs to decorre-
late
3 Λ from Archimedean characters n
it with t comparable to x/q, (or from combined
characters χ(n)n
it).

If one combines (1.3) with the L
2 bound
∫
R/Z |S(x, α)|2 dα ≪ x log x (1.4)

arising from the Plancherel identity and the prime number theorem, one can obtain
satisfactory estimates for all minor arcs with q ≫ log8 x (assuming that Q was chosen
to be signiﬁcantly less than x/ log8 x). To ﬁnish the proof of Vinogradov’s theorem,
one thus needs to obtain good prime number theorems in arithmetic progressions whose
modulus q can be as large as log8 x. While explicitly eﬀective versions of such theorems
exist (see e.g. [27], [23], [39], [11], [20]), their error term decays very slowly (and is
sensitive to the possibility of a Siegel zero for one exceptional modulus q); in particular,
errors of the form O(x exp(−c√log x)) for some explicit but moderately small constant
c > 0 are typical. Such errors can eventually overcome logarithmic losses such as log x,
but only for extremely large x, e.g. for x much larger than 10100, which can be viewed
as the principal reason why the thresholds for Vinogradov-type theorems are so large.

It is thus of interest to reduce the logarithmic losses in (1.3), particularly for moderately
sized x such as x ∼ 1030, as this would reduce the range
4 of moduli q that would have
to be checked in the major arc case, allowing for stronger prime number theorems in
arithmetic progressions to come into play. In particular, the numerical work of Platt

3Indeed, suppose for sake of heuristic argument that the Riemann zeta function had a zero very
close to 1 + ix/q, then the von Mangoldt explicit formula ∑
n⩽x Λ(n) would contain a term close to
− ∑
n⩽x n−ix/q, which suggests upon summation by parts that S(x, α) would contain a term close to
− ∑
n⩽x n−ix/qe(αx), which can be of size comparable to x/√
x/q when α is close to (say) 1/q. A
similar argument involving Dirichlet L-functions also applies when α is close to other multiples of 1/q.
This suggests that one would need to use zero-free regions for zeta functions and L-functions in orderto
improve upon the x√
x/q bound.

4It seems however that one cannot eliminate the major arcs entirely. In particular, one needs to
prevent the majority of the primes from concentrating in the quadratic non-residues modulo q for q = 3,
q = 4, or q = 5, as this would cause the residue class 0 mod q to have almost no representations as
the sum of three primes.

4 TERENCE TAO

[33] has established zero-free regions for Dirichlet L-functions of conductor up to 105

(building upon earlier work of Rumely [39] who obtained similar results up to conductor
102), and it is likely that such results would be useful in future work on Goldbach-type
problems.

Several improvements or variants to (1.3) are already known in the literature. For
instance, prior to the introduction of Vaughan’s identity in [46], Vinogradov [48] had
already established a bound of the shape

|S(x, α)| ≪
 ( x
√q + x
√x/q + exp(− 1
2 √
log x)
)
 log11/2 x

by sieving out small primes. This was improved by Chen [4] and Daboussi [7] to obtain

|S(x, α)| ≪
 ( x
√q + x
√
x/q + exp(− 1
2√log x)
)
 log3/4 x(log log x)1/2

and the constants made explicit (with some slight degradation in the logarithmic ex-
ponents) by Daboussi and Rivat [8]. Unfortunately, due to the slow decay of the
exp(− 1
2√log x) term, this estimate only becomes non-trivial for x ⩾ 10184 (see [8, §8]),
and is thus not of direct use for smaller values of x.

In [2], Buttkewitz obtained the bound

|S(x, α)| ≪A x
√q log1/4 x + x
x/q log log log x + x
logA x (1.5)

for any A ⩾ 1 (assuming β extremely small), using Lavrik’s estimate [22] on the average
error term in twin prime type problems, but the constants here are ineﬀective (as
Lavrik’s estimate uses the Siegel-Walﬁsz theorem). Finally, in the “weakly minor arc”
regime log q ⩽ 1
50 log1/3 x, Ramar´e [37] used the Bombieri sieve to obtain an eﬀective
bound of the form
 |S(x, α)| ≪ x
√q
φ(q) (1.6)

which, as mentioned previously, is an essentially sharp eﬀective bound in the absence
of any progress on the Siegel zero problem. Unfortunately, the constants in [37] are not
computed explicitly, and seem to be far too large to be useful for values of x such as
1030.

In this paper we will not work directly with the sums S(x, α), but instead with the
smoothed out sums
 Sη,q0(x, α) := ∑

n Λ(n)e(αn)1(n,q0)=1η(n/x)

for some (piecewise) smooth functions η : R → C and a modulus q0. The modulus q0 is
only of minor technical importance, and should be ignored at a ﬁrst reading (see Lemma
4.1 for a precise version of this statement). For sake of explicit constants we will often
work with a speciﬁc choice of cutoﬀ η, namely the cutoﬀ

η0(t) := 4(log 2 − | log 2t|)+, (1.7)

EVERY ODD NUMBER GREATER THAN 1 IS THE SUM OF AT MOST FIVE PRIMES 5

which is a Lipschitz continuous cutoﬀ of unit mass supported on the interval [1/4, 1].
The use of smooth cutoﬀs to improve the behaviour of exponential sums is of course
well established in the literature (indeed, the original work of Hardy and Littlewood [16]
on Goldbach-type problems already used smoothed sums). The reason for this speciﬁc
cutoﬀ is that one has the identity

η0(dw/x) = 4 ∫ ∞

0 1[ x
2W , x
W ](d)1[ W
2 ,W ](w) dW
W (1.8)

for any d, w, x > 0, which will be convenient for factorising the Type II sums into a
tractable form. In some cases we will take q0 to equal 2, in order to restrict all sums to
be over odd numbers, rather than all natural numbers; this has the eﬀect of saving a
factor of two in the explicit constants. Because of this, though, it becomes natural to
approximate 4α by a rational number a/q, rather than α itself.

Our main exponential sum result can be stated as follows.

Theorem 1.3 (Exponential sum estimate). Let x ⩾ 1020 be a real number, and let
4α = a
q + β for some natural number 100 ⩽ q ⩽ x/100 with (a, q) = 1 and some
β ∈ [−1/q2, 1/q2]. Let q0 be a natural number, such that all prime factors of q0 do not
exceed √x. Then

|Sη0,q0(x, α)| ⩽
 (
0.14 x
√
q + 0.64 x
√
x/q + 0.15x
4/5)
 log x(log x + 11.3) (1.9)

If q ⩽ x
1/3, one has the reﬁnement

|Sη0,q0(x, α)| ⩽ 0.5 x
q (log 2x)(log 2x + 15) + 0.31 x
√
q log q(log q + 8.9) (1.10)

and similarly when q ⩾ x
2/3, one has the reﬁnement

|Sη0,q0(x, α)| ⩽ 3.12 x
x/q (log 2x)(log q + 8) + 1.19 x
√
x/q log x
q (log x
q + 2.3). (1.11)

If q ⩾ x
2/3 and a = ±1, one has the further reﬁnement

|Sη0,q0(x, α)| ⩽ 9.73 x
(x/q)2 log2 x + 1.2 x
√
x/q log x
q (log x
q + 2.4). (1.12)

The ﬁrst estimate (1.9) is basically a smoothed out version of the standard estimate
(1.3), with the Lipschitz nature of the cutoﬀ η0 being responsible for the saving of one
logarithmic factor, and will be proven by basically the same method (i.e. Vaughan’s
identity, followed by linear and bilinear sum estimates of Vinogradov type); it can be
compared for instance with the explicit estimate

|S1[0,1],1(x, 4α)| ⩽ 0.177 x
√
q log3 x + 0.08 x
√
x/q log3.5 x + 3.8x
4/5 log2.2 x (1.13)

of Chen & Wang [6], rewritten in our notation. In practice, for x of size 1030 or so, the
estimate (1.3) improves upon the Chen-Wang estimate by about one to two orders of
magnitude, though this is admittedly for a smoothed version of the sum considered in
[6].

6 TERENCE TAO

The estimate (1.9) is non-trivial in the regime log4 x ≪ q ≪ x/ log4 x. The key point,
though, is that one can obtain further improvement over (1.9) in the most important
regimes when q is close to 1 or to x, by reducing the argument of the logarithm (or
by squaring the denominator); indeed, (1.9) when combined with (1.10), (1.11) is now
non-trivial in the larger range log2 x ≪ q ≪ x/ log2 x, and with (1.12) one can extend
the upper threshold of this range from x/ log2 x to x/ log x, at least when a = ±1.

The bounds in Theorem 1.3 are basically achieved by optimising in the cutoﬀ parameters
U, V in Vaughan’s identity, and (in the case of (1.12)) a second integration by parts,
exploiting the fact that the derivative of η0 has bounded total variation. Asymptotically,
the bounds here are inferior to those in (1.5), (1.6), but unlike those estimates, the
constants here are reasonable enough that the bounds are useful for medium-sized values
of x, for instance for x between 1030 and 101300. There is scope for further improvement5

in the exponential sum bounds in these ranges by eliminating or reducing more of the
logarithmic losses (and we did not fully attempt to optimise all the explicit constants),
but the bounds indicated above will be suﬃcient for our applications.

We will actually prove a slightly sharper (but more technical) version of Theorem 1.3,
with two additional parameters U and V that one is free to optimise over; see Theorem
5.1 below.

As an application of these exponential sum bounds, we establish the following result:

Theorem 1.4. Every odd number x larger than 1 can be expressed as the sum of at
most ﬁve primes.

This improves slightly upon a previous result of Ramar´e [35], who showed (by a quite
diﬀerent method) that every even natural number can be expressed as the sum of at
most six primes. In particular, as a corollary of this result we may lower the upper
bound on Shnirelman’s constant (the least number k such that all natural numbers
greater than 1 can be expressed as the sum of at most k primes) from seven to six
(note that the even Goldbach conjecture would imply that this constant is in fact three,
and is in fact almost equivalent to this claim). We remark that Theorem 1.4 was also
established under the assumption of the Riemann hypothesis by Kaniecki [21] (indeed,
by combining his argument with the numerical work in [41], one can obtain the stronger
claim that any even natural number is the sum of at most four primes).

Our proof of Theorem 1.4 also establishes that every integer x larger than 8.7 × 1036 can
be expressed as the sum of three primes and a natural number between 2 and 4 × 1014;
see Theorem 8.2 below.

5Indeed, since the release of an initial preprint of this paper, such improvements to the above bounds
have been achieved in [18]. The author expects however that in the case of most critical interest, namely
when q is very close to 1 or to x, the Vaughan identity-based methods in the above theorem are not
the most eﬃcient way to proceed. Thus, one can imagine in future applications that Theorem 1.3 (or
variants thereof) could be used to eliminate from consideration all values of q except those close to
1 and x, and then other methods (e.g. those based on the zeroes of Dirichlet L-functions, or more
eﬃcient identities than the Vaughan identity) could be used to handle those cases.

EVERY ODD NUMBER GREATER THAN 1 IS THE SUM OF AT MOST FIVE PRIMES 7

To prove Theorem 1.4, we will also need to rely on two numerically veriﬁed results in
addition to Theorem 1.3:

Theorem 1.5 (Numerical veriﬁcation of Riemann hypothesis). Let T0 := 3.29 × 109.
Then all the zeroes of the Riemann zeta function ζ in the strip {s : 0 < ℜ(s) < 1; 0 ⩽
ℑ(s) ⩽ T0} lie on the line ℜ(s) = 1/2. Furthermore, there are at most 1010 zeroes in
this strip.

Proof. This was achieved independently by van de Lune (unpublished), by Wedeniwski
[50], by Gourdon [14], and by Platt [34]. Indeed, the results of Wedeniwski allow one
to take T0 as large as 5.72 × 1010, and the results of Gourdon allow one to take T0
as large as 2.44 × 1012; using interval arithmetic, Platt also obtained this result with
T0 as large as 3.06 × 1010. (Of course, in these latter results there will be more than
1010 zeroes.) However, we will use the more conservative value of T0 = 3.29 × 109 in
this paper as it suﬃces for our purposes, and has been veriﬁed by four independent
numerical computations.

Theorem 1.6 (Numerical veriﬁcation of even Goldbach conjecture). Let N0 := 4×1014.
Then every even number between 4 and N0 is the sum of two primes.

Proof. This is the main result of Richstein [41]. A subsequent (unpublished) veriﬁcation
of this conjecture by the distributed computing project of Oliveira e Silva [32] allows one
to take N0 as large as 2.6 × 1018 (with the value N0 = 1017 being double-checked), but
again we shall use the more conservative value of N0 = 4×1014 in this paper as it suﬃces
for our purposes, and has been veriﬁed by three independent numerical computations.

The proof of Theorem 1.4 is given in Section 8 proceeds according to the circle method
with smoothed sums as discussed earlier, but with some additional technical reﬁnements
which we now discuss. The ﬁrst reﬁnement is to take advantage of Theorem 1.6 to
reduce the ﬁve-prime problem to the problem of representing a number x as the sum of
three primes n1, n2, n3 and a number between 2 and N0. As far as the circle method is
concerned, this eﬀectively restricts the frequency variable α to the arc {α : ∥α∥R/Z ≪
1/N0}. At the other end of the spectrum, by using Theorem 1.5 and the von Mangoldt
explicit formula one can control quite precisely the contribution of the major arc {α :
∥α∥R/Z ≪ T0/x}; see Proposition 7.2. Thus leaves only the “minor arc”

T0
x ≪ ∥α∥R/Z ≪ 1
N0 (1.14)

that remains to be controlled.

By using Theorem 1.6 and Theorem 1.5 (or more precisely, an eﬀective prime number
theorem in short intervals derived from Theorem 1.5 due to Ramar´e and Saouter [40]),
we will be able to assume that x is moderately large (and speciﬁcally, that x ⩾ 8.7 ×
1036). By using existing Vinogradov-type theorems, we may also place a large upper
bound on x; we will use the strongest bound in the literature, namely the bound x ⩽

8 TERENCE TAO

exp(3100) of6 Liu & Wang [24]. In particular, log x is relatively small compared to the
quantities N0 and T0, allowing one to absorb a limited number of powers of log x in the
estimates.

It remains to obtain good L
2 and L
∞ estimates on the minor arc region (1.14). We will
of course use Theorem 1.3 for the L
∞ estimates. A direct application of the Plancherel
identity would cost a factor of log x in the L
2 estimates, which turns out to be unac-
ceptable. One can use the uncertainty principle of Montgomery [28] to cut this loss
down to approximately 2 log x
log N0 (see Corollary 4.7), but it turns out to be more eﬃcient
still to use a large sieve estimate of Siebert [45] on the number of prime pairs (p, p + h)
less than x for various h to obtain an L
2 estimate which only loses a factor of 8 (see
Proposition 4.10).

In order to nearly eliminate some additional “Archimedean” losses arising from convolv-
ing together various cutoﬀ functions η on the real line R, we will use a trick of Bourgain
[3], and restrict one of the three summands n1, n2, n3 to a signiﬁcantly smaller order of
magnitude (of magnitude x/K instead of x for some K, which we will set to be 103, in
order to be safely bounded away from both 1 and T0). By estimating the exponential
sums associated to n1, n2 in L
2 and the sum associated to n3 in L
∞, one can avoid
almost all Archimedean losses.

As it turns out, the combination of all of these tricks, when combined with the expo-
nential sum estimate and the numerical values of N0 and T0, are suﬃcient to establish
Theorem 1.4. However, there is one ﬁnal trick which could be used to reduce certain
error terms further, namely to let K vary over a range (e.g. from 103 to 106) instead of
being ﬁxed, and average over this parameter. This turns out to lead to an additional
saving (of approximately an order of magnitude) in the weakly minor arc case when α
is slightly larger than T0/x. While we do not actually utilise this trick here as it is not
needed, it may be useful in other contexts, and in particular in improving the known
upper threshold for Vinogradov’s theorem.

1.7. Acknowledgments. The author is greatly indebted to Ben Green and Harald
Helfgott for several discussions on Goldbach-type problems, and to Julia Wolf, Westin
King, Mark Kerstein, and several anonymous readers of my blog for corrections. The
author is particularly indebted to the anonymous referee for detailed comments, correc-
tions, and suggestions. The author is supported by NSF grant DMS-0649473.

6The numerology in our argument is such that one could also use the weaker bound x ⩽
exp(exp(11.503)) provided by Chen & Wang [5], provided one assumed the even Goldbach conjec-
ture to be veriﬁed up to N0 = 1017, a fact which has been double-checked in [32]. Alternatively, if one
uses the very recent minor arc bounds in [18] that appeared after the publication of this paper, then
no Vinogradov type theorem is needed at all to prove our result, as the bounds in [18] do not contain
any factors of log x that need to be bounded.

EVERY ODD NUMBER GREATER THAN 1 IS THE SUM OF AT MOST FIVE PRIMES 9

2. Notation

All summations in this paper will be over the natural numbers N = {1, 2, 3, . . .} unless
otherwise indicated, with the exceptions of sums over the index p, which are always
understood to be over primes.

We use (a, b) to denote the greatest common divisor of two natural numbers, and [a, b]
for the least common multiple. We write a|b to denote the assertion that a divides b.

Given a statement E, we use 1E to denote its indicator, thus 1E equals 1 when E is
true and 0 otherwise. Thus, for instance 1(n,q)=1 is equal to 1 when n is coprime to q,
and equal to 0 otherwise.

We will use the following standard arithmetic functions. If n is a natural number, then

• Λ(n) is the von Mangoldt function of n, deﬁned to equal log p when n is a power
of a prime p, and zero otherwise.
• µ(n) is the M¨obius function of n, deﬁned to equal (−1)k when n is the product
of k distinct primes, and zero otherwise.
• φ(n) is the Euler totient function of n, deﬁned to equal the number of residue
classes of n that are coprime to n.
• ω(n) is the number of distinct prime factors of n.

Given two arithmetic functions f, g : N → C, we deﬁne the Dirichlet convolution f ∗ g :
N → C by the formula f ∗ g(n) := ∑

d|n f (d)g( n
d ),

thus for instance µ ∗ 1(n) = 1n=0, Λ ∗ 1(n) = log(n), and µ ∗ log(n) = Λ(n).

Given a positive real Q, we also deﬁne the primorial Q♯ of Q to be the product of all
the primes up to Q: Q♯ := ∏

p⩽Q p.

Thus, for instance 1(n,Q♯)=1 equals 1 precisely when n has no prime factors less than or
equal to Q.

We use the usual L
p norms
 ∥f ∥Lp(R) := (∫
R |f (x)|p dx
)1/p

for 1 ⩽ p < ∞, with ∥f ∥L∞(R) denoting the essential supremum of f . Similarly for other
domains than R which have an obvious Lebesgue measure; we deﬁne the ℓp norms for
discrete domains (such as the integers Z) in the usual manner.

We use R/Z to denote the unit circle. By abuse of notation, any 1-periodic function on
R is also interpreted as a function on R/Z, thus for instance we can deﬁne | sin(πα)| for

10 TERENCE TAO

any α ∈ R/Z. We let ∥α∥R/Z be the distance to the nearest integer for α ∈ R, and this
also descends to R/Z. We record the elementary inequalities

2∥α∥R/Z ⩽ | sin(πα)| ⩽ π∥α∥R/Z ⩽ | tan(πα)|, (2.1)

valid for any α ∈ R/Z. In a similar vein, if a ∈ Z/qZ, we consider a
q as an element of
R/Z.

When considering a quotient X
Y with a non-negative denominator Y , we adopt the
convention that X
Y = +∞ when Y is zero. Thus for instance 1
∥α∥R/Zis equal to +∞
when α is an integer.

We will occasionally use the usual asymptotic notation X = O(Y ) or X ≪ Y to
denote the estimate |X| ⩽ CY for some unspeciﬁed constant C. However, as we will
need explicit bounds, we will more frequently (following Ramar´e [35]) use the exact
asymptotic notation X = O∗(Y ) to denote the estimate |X| ⩽ Y . Thus, for instance,
X = Y + O∗(Z) is synonymous with |X − Y | ⩽ Z.

If F : R → C is a smooth function, we use F ′, F ′′ to denote the ﬁrst and second
derivatives of F , and F (k) to denote the k-fold derivative for any k ⩾ 0.

If x is a real number, we denote e(x) := e
2πix, we denote x+ := max(x, 0), and we
denote ⌊x⌋ to be the greatest integer less than or equal to x. We interpret the x ↦→ x+
operation to have precedence over exponentiation, thus for instance x
2
+ denotes the
quantity max(x, 0)2 rather than max(x
2, 0).

If E is a ﬁnite set, we use |E| to denote its cardinality. If I is an interval, we use |I| to
denote its length. We will also occasionally use translations I + x := {y + x : y ∈ I}
and dilations λI := {λy : y ∈ I} of such an interval.

The natural logarithm function log takes precedence over addition and subtraction, but
not multiplication or division; thus for instance

log 2x + 15 = (log(2x)) + 15.

3. Exponential sum estimates

We now record some estimates on linear exponential sums such as
∑

n∈Z F (n)e(αn)

for various smooth functions F : R → C, as well as bilinear exponential sums such as
∑

n∈Z
 ∑

m∈Z anbme(αnm)

for various sequences (an)n∈Z and (bm)m∈Z . These bounds are standard (at least if one
is only interested in bounds up to multiplicative constants), but we will need to make
all constants explicit. Also, in order to save a factor of two or so in the explicit bounds,

EVERY ODD NUMBER GREATER THAN 1 IS THE SUM OF AT MOST FIVE PRIMES 11

we will frequently restrict the summation to odd integers by inserting weights such as
1(n,2)=1, and will therefore need to develop variants of the standard bounds for this
purpose.

We begin with some standard bounds on linear exponential sums with smooth cutoﬀs.

Lemma 3.1. Let α ∈ R/Z, and let F : R → C be a smooth, compactly supported
function. Then we have the bounds
∑

n∈Z F (n) = ∫

R F (y) dy + O∗ ( 1
2∥F ′∥L1(R)) (3.1)

and ∣
∣
∣
∣
∣
∑

n∈Z F (n)e(αn)
∣
∣
∣
∣
∣ ⩽ ∑

n |F (n)| ⩽ ∥F ∥L1(R) + 1
2∥F ′∥L1(R) (3.2)

and ∣
∣
∣
∣
∣

∑

n∈Z F (n)e(αn)
∣
∣
∣
∣
∣ ⩽ 1
|2 sin(πα)|k ∥F (k)∥L1(R) (3.3)

for all natural numbers k ⩾ 1.

Proof. These bounds appear in [13] and in [29, Lemma 1.1], but we reproduce the proof
here for the reader’s convenience. From the fundamental theorem of calculus one has

F (n) = F (y) + O∗ (∫ n+1/2

n |F ′(t)| dt

)

for all y ∈ [n, n + 1/2] and

F (n) = F (y) + O∗ (∫ n

n−1/2 |F ′(t)| dt
)

for all y ∈ [n − 1/2, n]; averaging over y, we conclude that

F (n) = ∫ n+1/2

n−1/2 F (y) dy + 1
2O∗ (∫ n+1/2

n−1/2 |F ′(t)| dt

)
 .

Summing over n, we obtain (3.1). Taking ℓ1 norms instead, one obtains
∑

n∈Z |F (n)| ⩽ ∥F ∥L1(R) + 1
2∥F ′∥L1(R)

giving (3.2).

Now we obtain the k = 1 case of (3.3). We may assume α ̸= 0. By summation by parts,
one has ∑

n∈Z (F (n + 1) − F (n))e(αn) = (1 − e(−α)) ∑

n∈Z F (n)e(αn)

and thus ∣
∣
∣
∣
∣

∑

n∈Z F (n)e(αn)
∣
∣
∣
∣
∣ = 1
2| sin(πα)|| ∑

n∈Z (F (n + 1) − F (n))e(αn)|. (3.4)

12 TERENCE TAO

Since |F (n + 1) − F (n)| ⩽ ∫ 1
0 |F ′(n + t)| dt, we obtain the k = 1 case of (3.3). To obtain
the higher cases, observe from (3.4), the fundamental theorem of calculus F (n + 1) −
F (n) = ∫ 1
0 F ′(n + t) dt and Minkowski’s inequality that

| ∑

n∈Z F (n)e(αn)| ⩽ 1
2| sin(πα)| | ∑

n∈Z F ′(n + t)e(αn)|

for some 0 ⩽ t < 1. One can now deduce (3.3) for general k from the k = 1 case by
induction.

We can save a factor of two by restricting to odd numbers:

Corollary 3.2. With the same hypotheses as Lemma 3.1, we have

| ∑

n∈Z F (n)e(αn)1(2,n)=1| ⩽ 1
2∥F ∥L1(R) + 1
2∥F ′∥L1(R)

and
 | ∑

n∈Z F (n)e(αn)1(2,n)=1| ⩽ 1
2| sin(2πα)|k ∥F (k)∥L1(R)

for all k ⩾ 1.

Proof. We can rewrite
∑

n∈Z F (n)e(αn)1(2,n)=1 = e(α) ∑

n∈Z F (2n + 1)e(2αn).

Applying the previous lemma with α replaced by 2α, and F (x) replaced by F (2x + 1),
we obtain the claim.

We also record a continuous variant:

Lemma 3.3. Let F : R → C be a smooth, compactly supported function. Then one has
∣
∣
∣
∣
∫

R F (y)e(αy) dy∣
∣
∣
∣ ⩽ ∥F (k)∥L1(R)
(2π|α|)k

for any k ⩾ 0 and α ∈ R.

Proof. The claim is trivial for k = 0. For higher k, we may assume α ̸= 0. By integration
by parts, we have ∫

R F (y)e(αy) dy = − 1
2πiα
 ∫

R F ′(y)e(αy) dy,

and the claim then follows by induction.

In order to sum the bounds arising from Corollary 3.2 (particularly when k = 1), the
following lemma is useful.

EVERY ODD NUMBER GREATER THAN 1 IS THE SUM OF AT MOST FIVE PRIMES 13

Lemma 3.4 (Vinogradov-type lemma). Let α = a
q + β for some β = O∗(1/q2). Then
for any x < y, A, B > 0, and θ ∈ R/Z, we have
∑

x<n⩽y min (
A, B
| sin(παn + θ)|
 ) ⩽ (⌊y − x
q
 ⌋ + 1) (2A + 2
π Bq log 4q).

Proof. We may normalise B = 1. By subdivision of the interval [x, y] it suﬃces to show
that ∑

x<n⩽x+q min(A, 1
| sin(παn + θ)| ) ⩽ 2A + 2
π q log 4q

for all x. The claim then follows from [8, Lemma 1]. (Strictly speaking, the phase shift θ
is not present in the statement of that lemma, but the proof of the lemma is unchanged
with that phase shift. Alternatively, one can perturb α to be irrational, and then by
Kronecker’s theorem one can obtain a dense set of phase shifts by shifting the interval
[x, y] by an integer, and the claim for general θ then follows by a limiting argument.)

Once again, we can save a factor of two by restricting to odd n:

Corollary 3.5 (Restricting to odd integers). Let 2α = a
q + β for some β = O∗(1/q2).
Then for any x < y, A, B > 0, and θ ∈ R/Z, we have
∑

x<n⩽y min (
A, B
| sin(παn + θ)|
 ) 1(n,2)=1 ⩽ (⌊y − x
2q
 ⌋ + 1) (2A + 2
π Bq log 4q).

Proof. Writing n = 2m + 1, the expression on the left-hand side is
∑

(x−1)/2<m⩽(y−1)/2 min (
A, B
| sin(2παm + πα + θ)|
) .

The claim then follows from Lemma 3.5.

Now we turn to bilinear estimates. A key tool here is

Lemma 3.6 (Large sieve inequality). Let ξ1, . . . , ξR ∈ R/Z be such that ∥ξi −ξj∥R/Z ⩾ δ
for all 1 ⩽ i < j ⩽ R and some δ > 0. Let I = [N1, N2] be an interval of length
|I| = N2 − N1 ⩾ 1. Then we have

R∑

i=1 | ∑

n∈I∩Z ane(ξin)|2 ⩽ (|I| + δ−1)∥an∥2
ℓ2(Z )

for all complex-valued sequences (an)n∈Z .

Proof. See [30, Theorem 3] (noting that the number of integer points in I is at most
|I| + 1).

Specialising to ξj that are consecutive multiples of α and applying the Cauchy-Schwarz
inequality, we conclude

14 TERENCE TAO

Corollary 3.7 (Special case of large sieve inequality). Let I, J ⊂ R be intervals of
length at least 1, and let α ∈ R/Z. Then one has

| ∑

n∈I∩Z
 ∑

m∈J∩Z anbme(nmα)| ⩽ (
|I| + 1
inf 1⩽j⩽|J| ∥jα∥R/Z
 )1/2 ∥(an)n∈Z ∥ℓ2(Z )∥(bm)n∈Z ∥ℓ2(Z )

for all complex-valued sequences (an)n∈Z , (bm)m∈Z .

Again, we can obtain a saving of a factor of 2 in the main term by restricting n, m to
odd numbers:

Corollary 3.8 (Restricting to odd numbers). Let I, J ⊂ R be intervals of length at
least 2, and let α ∈ R/Z. Then one has

| ∑

n∈I∩Z
 ∑

m∈J∩Z an1(n,2)=1bm1(m,2)=1e(nmα)| ⩽
 

 1
2 |I| + 1
inf 1⩽j⩽ 1
2 |J| ∥4jα∥R/Z
 



1/2
 ∥(an)n∈Z ∥ℓ2(Z )∥(bm)n∈Z ∥

for all complex-valued sequences (an)n∈Z , (bm)m∈Z .

Proof. We can rewrite the left-hand side as

| ∑

n∈ 1
2 I−1∩Z
 ∑

m∈ 1
2 J−1∩Z
 ˜an˜bme(4nmα)|

where ˜an := a2n+1e(2nα) and ˜bm := b2m+1e(2mα), and the claim then follows from
Corollary 3.7.

The above corollary is useful whenever the 4jα for 1 ⩽ j ⩽ 1
2|J| stay far away from the
origin. When J is large, this is not always the case, but one can of course rectify this
by a subdivision argument:

Corollary 3.9 (Subdivision). Let I, J ⊂ R be intervals of length at least 2, and let
α ∈ R/Z. Let M ⩾ 1. Then one has

| ∑

n∈I∩Z
 ∑

m∈J∩Z an1(n,2)=1bm1(m,2)=1e(nmα)| ⩽ (
 1
2|I| + 1
inf 1⩽j⩽M ∥4jα∥R/Z
 )1/2

× (⌊ J
2M
 ⌋ + 1)1/2 ∥an∥ℓ2(Z )∥bm∥ℓ2(Z ).

for all complex-valued sequences (an)n∈Z , (bm)m∈Z .

Proof. We subdivide J into intervals J1, . . . , Jk of length 2M, where k := ⌊ J
2M ⌋ + 1. The
claim then follows by applying Corollary 3.8 to each sub-interval, summing, and using
the Cauchy-Schwarz inequality.

EVERY ODD NUMBER GREATER THAN 1 IS THE SUM OF AT MOST FIVE PRIMES 15

4. Basic bounds on Sη,q(x, α)

In all the lemmas in this section, x ⩾ 1 is a real number, α ∈ R/Z is a frequency,
η : R → R+ is a bounded non-negative measurable function supported in [0, 1], and
q ⩾ 1 is a natural number. In some of the lemmas we will also make the additional
hypothesis that η is smooth, although in applications one can often relax this regularity
requirement by a standard limiting argument. In some cases we will also need η to
vanish near zero.

The purpose of this section is to collect some basic estimates for manipulating the
exponential sums
 Sη,q(x, α) := ∑

n Λ(n)e(αn)1(n,q)=1η(n/x) (4.1)

that already appeared in the introduction.

We ﬁrst make the easy observation that Sη,q(x, α) barely depends on the parameter q.

Lemma 4.1. We have

Sη,q(x, α) = Sη,1(x, α) + O∗(ω(q)∥η∥L∞(R) log x)

In particular, if the largest prime factor of q is at most √x, then

Sη,q(x, α) = Sη,1(x, α) + O∗(2.52√
x∥η∥L∞(R))

In practice, we expect Sη,q(x, α) to be of size comparable to x, and so in practice the
error terms here will be utterly negligible in applications, and we will be able to absorb
them without any diﬃculty into a larger error term.

Proof. We have
 |Sη,q(x, α) − Sη,1(x, α)| ⩽ ∥η∥L∞(R) ∑

n⩽x:(n,q)>1 Λ(n).

Note that if Λ(n) is non-zero and (n, q) > 1, then n is a power of a prime p dividing q,
thus ∑

n⩽x:(n,q)>1 Λ(n) = ∑

p|q log p ∑

j:pj⩽x 1.

Since ∑

j:pj⩽x 1 ⩽ log x
log p , the ﬁrst claim follows. For the second claim, observe that

ω(q) ⩽ ∑

p⩽√
x 1 ⩽ 2.52 √x
log x ,

where the last inequality follows from [43, Corollary 1].

Next, we make a simple summation by parts observation that allows one to replace η
by the sharply truncated cutoﬀ 1[0,1] if desired.

16 TERENCE TAO

Lemma 4.2. If η is smooth, then one has

|Sη,q(x, α)| ⩽ ∥η′∥L1(R) sup
y⩽x |S1[0,1],q(y, α)|.

Proof. Since η(n/x) = − 1
x ∫ x
0 η′(y/x)1n⩽y dy for all n ⩽ x, we have

Sη,q(x, α) = − 1
x
 ∫ x

0 η′(y/x) ∑

n Λ(n)e(αn)1n⩽y1(n,q)=1 dy

and thus
 |Sη,q(x, α)| ⩽ 1
x
 ∫ x

0 |η′(y/x)||S1[0,1],q(y, α)| dy,

and the claim follows.

We trivially have
 |Sη,q(x, α)| ⩽ Sη,q(x, 0) (4.2)

and we now consider the estimation of the quantity Sη,q(x, 0).

Lemma 4.3. We have

Sη,q(x, 0) ⩽ ∥η∥L∞(R)S1[0,1],1(x, 0) ⩽ 1.04∥η∥L∞(R)x. (4.3)

If η is smooth and supported on [c, 1] for some c > 0 with cx ⩾ 108, then

Sη,1(x, 0) = ∥η∥L1(R)x + O∗ ( 1
40 log cx∥η′∥L1(R)x
) . (4.4)

We remark that sharper estimates can be obtained using the machinery from Section
7, at least when η is fairly smooth, though we will not need such improvements here.

Proof. The ﬁrst inequality of (4.3) is trivial, and the ﬁnal inequality of (4.3) follows from
[43, Theorem 12] (indeed, one can replace the constant 1.04 with the slightly smaller
1.03883).

For (4.4), we argue as in Lemma 4.2 and write

Sη,1(x, 0) = − 1
x
 ∫ x

cx η′(y/x) ∑

n⩽y Λ(n) dy.

From [44, Theorem 7] (and the hypothesis cx ⩾ 108) one has

∑

n⩽y Λ(n) = y + O∗ ( y
40 log cx
)

EVERY ODD NUMBER GREATER THAN 1 IS THE SUM OF AT MOST FIVE PRIMES 17

and hence
 Sη,1(x, 0) = − 1
x
 ∫ x

cx η′(y/x)y dy

+ O∗ ( 1
x 1
40 log cx
 ∫ x

cx |η′(y/x)|y dy) .

Using the crude bound ∫ x

cx |η′(y/x)|y dy ⩽ ∥η′∥L1(R)x

the claim follows.

As Λ and η are real, we have the self-adjointness symmetry

Sη,q(x, −α) = Sη,q(x, α). (4.5)

Also, since e(n(α + 1/2)) = −e(nα) when n is odd, we have the anti-symmetry

Sη,q(x, α + 1/2) = −Sη,q(x, α) (4.6)

whenever q is even. More generally, we have the following inequality of Montgomery
[28]:

Lemma 4.4 (Montgomery’s uncertainty principle). For any q0 dividing q, we have

∑

a∈Z /q0Z :(a,q0)=1
 ∣
∣
∣
∣Sη,q(x, α + a
q0 )∣
∣
∣
∣

2 ⩾ µ(q0)2

φ(q0) |Sη,q(x, α)|2.

Proof. We may of course take q0 to be square-free. Let an := Λ(n)e(αn)1(n,q)=1η(n/x),
S( a
q0 ) := ∑

n ane(an/q0), and Z := ∑

n an, then the inequality reads

∑

a∈Z /q0Z :(a,q0)=1 |S( a
q0 )|2 ⩾ 1
∏
p|q0(p − 1)|Z|2.

But this follows from [28] (particularly equation (10) and the ﬁnal display in Section 3,
and setting ω(p) = 1 for all p|q0). Another proof of this inequality may be found in [19,
Lemma 7.15].

Now we consider L
2 estimates on Sη,q(x, α). We have a global estimate:

Lemma 4.5 (Global L
2 estimate). We have
∫

R/Z |Sη,q(x, α)|2 dα ⩽ Sη2,q(x, 0) log x.

Proof. From the Plancherel identity we have
∫
R/Z |Sη,q(x, α)|2 dα = ∑

n η(n/x)2Λ(n)21(n,q)=1.

Bounding Λ(n)2 ⩽ Λ(n) log x on the support of η(n/x)2, we obtain the claim.

18 TERENCE TAO

We can largely remove
7 the logarithmic factor in the above lemma by restricting to
major arcs:

Lemma 4.6 (Local L
2 estimate). Let Q, R ⩾ 1, and let Σ ⊂ R/Z be the set

Σ := ⋃

q0⩽Q
 ⋃

(a0,q0)=1
[ a0
q0 − 1
2Q2R2 , a0
q0 + 1
2Q2R2 ].

If R♯|q, then ∫

Σ |Sη,q(x, α)|2 dα ⩽
 (∏

p⩽Q
 p
p − 1
 ) log x
log R Sη2,q(x, 0). (4.7)

Proof. From Lemma 4.4 one has

µ2(q1)
φ(q1)
 ∫

Σ |Sη,q(x, α)|2 dα ⩽ ∑

a1∈Z /q1Z :(a1,q1)=1
 ∫

Σ+ a1
q1 |Sη,q(x, α)|2 dα

for any q1. Summing over all q1 ⩽ R coprime to Q♯ and rearranging, we obtain the
bound
∫

Σ |Sη,q(x, α)|2 dα ⩽
 ∑

q1⩽R:(q1,Q♯)=1 ∑

a1∈Z /q1Z :(a1,q1)=1 ∫

Σ+ a1
q1 |Sη,q(x, α)|2 dα
∑

q1⩽R:(q1,Q♯)=1 µ2(q1)
φ(q1) .

Set
 G(R) := ∑

q1⩽R
 µ2(q1)
φ(q1) .

Observe that
 G(R) ⩽
 

 ∑

q1⩽R:(q1,Q♯)=1
 µ2(q1)
φ(q1)
 

 (∏

p⩽Q 1 + 1
φ(p)
 )

and thus 1
∑

q1⩽R:(q1,Q♯)=1 µ2(q1)
φ(q1) ⩽
 ∏

p⩽Q p
p−1
G(R) .

Also, from [26] or [31, Lemma 3] one has G(R) ⩾ log R + 1.07 for R ⩾ 6, so by direct
computation for 1 ⩽ R ⩽ 6 we have G(R) ⩾ log R for R ⩾ 1.

To conclude the proof, it thus suﬃces (in view of Lemma 4.5) to show that the sets
Σ+ a1
q1 are disjoint up to measure zero sets as a1, q1 vary in the indicated range. Suppose

this is not the case, then Σ + a1
q1 and Σ + a′
1
q′
1 intersect in a positive measure set for some
distinct a1, q1 and a
′
1, q′
1 in the indicated range. Thus one has

| a0
q0 + a1
q1 − a
′
0
q′
0 − a
′
1
q′
1 | < 1
Q2R2

7A version of this inequality was also obtained in an unpublished note of Heath-Brown, which was
communicated to me by Harald Helfgott.

EVERY ODD NUMBER GREATER THAN 1 IS THE SUM OF AT MOST FIVE PRIMES 19

for some q0, q0 ⩽ Q with (a0, q0) = (a
′
0, q′
0) = 1. The left-hand side is a fraction with
denominator at most Q
2R2, and therefore vanishes. Since q1q′
1 is coprime with q0q′
0 we
conclude that a1
q1 = a′
1
q′
1 , contradiction. The claim follows.

Remark. As pointed out by the anonymous referee, a slightly stronger version of Lemma
4.6 (saving a factor of e
γ asymptotically) can also be established by modifying the proof
of [38, Theorem 5]; the main idea is to decompose into Dirichlet characters, as in [1].

There are several eﬀective bounds on the expression ∏

p⩽Q p
p−1 appearing in Lemma 4.6;
see [43, Theorem 8], [10], [12, Theorem 6.12]. However, in this paper we will only need
to work with the Q = 1 case, and so we will not use the above lemma here. Specialising
Lemma 4.6 to the case Q = 1, we conclude

Corollary 4.7. If 0 < r < 1/2 and √
1/2r♯|q, one has
∫
∥α∥R/Z⩽r |Sη,q(x, α)|2 dα ⩽ 2

1 − log(2rx)
log x Sη2,q(x, 0).

We can complement this upper bound with a lower bound:

Proposition 4.8. Let η be smooth and 0 ⩽ r ⩽ 1/2. Then
∫
∥α∥R/Z⩽r |Sη,q(x, α)|2 dα ⩾ (Sη2,q(x, 0) − 1
π2rx∥η′η′ + ηη′′∥L1(R)Sη,q(x, 0))2
+
∥η∥2
L2(R)x + ∥ηη′∥L1(R) .

Ignoring the error terms, this gives a lower bound of Sη2,q(x, 0), showing that Corollary
4.7 is essentially sharp up to a factor of 2 when rx is not too large.

Proof. From the Parseval formula, one has

Sη2,q(x, 0) = ∫
R/Z Sη,q(x, α)F (α) dα

where F (α) := ∑

n η(n/x)e(−αn). In particular,
∣
∣
∣
∣
∣
∫

∥α∥R/Z⩽r Sη,q(x, α)F (α) dα
∣
∣
∣
∣
∣ ⩾ Sη2,q(x, 0) − Sη,q(x, 0) ∫

∥α∥R/Z>r |F (α)| dα.

and thus by the Cauchy-Schwarz inequality
∫
∥α∥⩽r |Sη,q(x, α)|2 dα ⩾ (Sη2,q(x, 0) − Sη,q(x, 0) ∫

∥α∥R/Z>r |F (α)| dα)2
+
∫
R/Z |F (α)|2 dα .

By the Plancherel theorem, one has
∫
R/Z |F (α)|2 dα = ∑

n η(n/x)2

and hence by (3.1) ∫

R/Z |F (α)|2 dα = ∥η∥2
L2(R)x + O∗(∥ηη′∥L1(R)).

20 TERENCE TAO

Similarly, from (3.3) (with k = 2) one has

|F (α)| ⩽ 1
2x| sin(πα)|2 ∥η′η′ + ηη′′∥L1(R)

for any α and thus ∫

∥α∥R/Z⩾r |F (α)| dα ⩽ cot(πr)
πx ∥η′η′ + ηη′′∥L1(R).

Bounding
 cot(πr) ⩽ 1
πr
the claim follows.

We can clean up the error terms as follows:

Corollary 4.9. Let η be smooth and supported on [c, 1] for some c > 0, and suppose
that 1
2x ⩽ r ⩽ 1/2 and q = √x♯. We normalise ∥η∥L2(R) = 1. Assume furthermore that

cx ⩾ 108 (4.8)

x ⩾ 104∥ηη′∥L1(R) (4.9)

log(cx) ⩾ 5∥ηη′∥L1(R) (4.10)

x ⩾ 108∥η∥4
L∞(R). (4.11)

rx ⩾ 20∥η′η′ + ηη′′∥L1(R)∥η∥L∞(R) (4.12)

Then one has Sη2,q(x, 0) = x(1 + O∗(0.02)) (4.13)
and ∫
∥α∥⩽r |Sη,q(x, α)|2 dα ⩾ 0.94x (4.14)

Proof. From Lemma 4.3 and (4.8), (4.10) one has

Sη2,1(x, 0) = x(1 + O∗(0.01))

and by Lemma 4.1 and (4.11) we conclude (4.13).

Let us denote the quantity ∫

∥α∥⩽r |Sη,q(x, α)|2 dα by A. By Proposition 4.8, (4.9) and
Lemma 4.3 we have

A ⩾ 0.999 1
∥η∥2
L2(R)x
 (
Sη2,q(x, 0) − 1.04
π2r ∥η′η′ + ηη′′∥L1(R)∥η∥L∞(R)
)2

+ .

By (4.12), (4.13) we have
1.04
π2r ∥η′η′ + ηη′′∥L1(R)∥η∥L∞(R) ⩽ 0.01Sη2,q(x, 0)

and so A ⩾ 0.97 1
xSη2,q(x, 0)2

and thus by (4.13) A ⩾ 0.94x,

EVERY ODD NUMBER GREATER THAN 1 IS THE SUM OF AT MOST FIVE PRIMES 21

which is (4.14).

The estimate in Corollary 4.7 is quite sharp when r is small (of size close to 1/x), but
not when r is large. For this, we have an alternate estimate:

Proposition 4.10 (Mesoscopic L
2 estimate). Suppose that q = √x♯. Let H ⩾ 102, and
write DH(α) := ∑H
h=1 e(hα) for the Dirichlet-type kernel. Then we have
∫

R/Z |Sη,q(x, α)|2|DH(α)|2 dα ⩽ (1 + ε) × 8H 2x∥η∥2
L∞(R)

where ε is the quantity

ε := 0.13 log x
H + (e
γ log log(2H) + 2.507
log log(2H) ) log(9H)

2H . (4.15)

By applying this proposition with H slightly larger than log x and using standard lower
bounds on |DH(α)|, we conclude that
∫
∥α∥=o( 1
log x ) |Sη,q(x, α)|2 dα ⩽ (8 + o(1))x∥η∥2
L∞(R).

In comparison, Corollary 4.7 gives an upper bound of (2 + o(1)) log x
log log xx∥η∥2
L2(R) for this
integral, while Proposition 4.8 gives a lower bound of (1−o(1))x∥η∥2
L2(R) (if η is smooth).
Thus we see that the bound in Proposition 4.10 is only oﬀ by a factor of 8 or so, if η is
close to 1[0,1]. It seems of interest to ﬁnd eﬃcient variants of this proposition in which
the |DH(α)|2 weight is replaced by a weight concentrated on multiple major arcs, as in
Lemma 4.6, as this may be of use in further work on Goldbach-type problems.

Proof. We may normalise ∥η∥L∞(R) = 1. By the Plancherel identity, we may write the
left-hand side as

H∑

h=1
 H∑

h′=1
 ∑

n Λ(n)η(n/x)1(n,q)=1Λ(n + h
′ − h)η((n + h
′ − h)/x)1(n+h′−h,q)=1.

The diagonal contribution h = h
′ can be bounded by

H ∑

n Λ(n)η(n/x) log x

which by Lemma 4.3 is bounded by 1.04Hx log x. Now we consider the oﬀ-diagonal
contribution h ̸= h
′. As Λ(n)1(n,q)=1 is supported on the odd primes p less than or
equal to x, we restrict attention to the contribution when h − h
′ is even, and can bound
this contribution by

H∑

h′=1
 ∑

1⩽h⩽H:h̸=h′;2|h−h′ log2 x|{p ⩽ x : p + h − h
′ prime, p + h − h
′ ⩽ x}|,

which by the pigeonhole principle is bounded by

H ∑

1⩽h⩽H:h̸=h′;2|h−h′ log2 x|{p ⩽ x : p + h − h
′ prime, p + h − h
′ ⩽ x}|, (4.16)

22 TERENCE TAO

for some 1 ⩽ h
′ ⩽ H, which we now ﬁx. Applying the main result of Siebert [45], we
have
 |{p ⩽ x : p + h − h
′ prime, p + h − h
′ ⩽ x}| ⩽ 8Si2 x
log2 x
 ∏

p|h−h′;p>2
 p − 1
p − 2

where S2 := 2 ∏

p>2(1 − 1
(p−1)2 ) is the twin prime constant. We can thus bound (4.16)
by
 8S2Hx ∑

1⩽h⩽H:h̸=h′;2|h−h′
 ∏

p|h−h′;p>2
 p − 1
p − 2.

If we let f be the multiplicative function

f (n) := 1(n,2)=1µ2(n) ∏

p|n:p>2
 1
p − 2

then we have ∏

p|h−h′;p>2
 p − 1
p − 2 = ∑

1⩽n⩽H;(n,2)=1:n|h−h′ f (n)

whenever 1 ⩽ h, h
′ ⩽ H with h ̸= h
′, so we may bound the preceding expression by

8S2Hx ∑

1⩽n⩽H:(n,2)=1 f (n) ∑

1⩽h⩽H:2n|h−h′ 1.

We may bound ∑

1⩽h⩽H:2n|h−h′ 1 ⩽ H
2n + 1 (4.17)

so that (4.16) is then bounded by

8S2Hx
 (

H
 ∞∑

n=1
 f (n)
2n + ∑

1⩽n⩽H f (n)
)
 .

By evaluating the Euler product one sees that

∞∑

n=1
 f (n)
2n = 1
2 ∏

p (1 + f (p)) = 1
S2 .

To evaluate the f summation, we observe that8

f (n) = 1(n,2)=1 µ2(n)
φ(n) 2n
φ(2n)
 1
2 ∏

p|n:p>2
(1 − 1
(p − 1)2 )−1.

We can bound
 1
2 ∏

p|n>2
(1 − 1
(p − 1)2 )−1 ⩽ 1
S2

and from [43, Theorem 15] one has
2n
φ(2n) ⩽ e
γ log log(2n) + 2.507
log log(2n) .

8Alternatively, one can sum f directly by using eﬀective bounds on sums of multiplicative functions,
as in [35]. This will save a factor of log log H in the upper bounds, but in our applications this loss is
quite manageable.

EVERY ODD NUMBER GREATER THAN 1 IS THE SUM OF AT MOST FIVE PRIMES 23

Since n ⩽ H and H ⩾ 102, we conclude that
2n
φ(2n) ⩽ e
γ log log(2H) + 2.507
log log(2H)
for any 1 ⩽ n ⩽ H with (n, 2) = 1 (the cases when n is so small that e
γ log log(2n) +
2.507
log log(2n) can exceed e
γ log log(2H) + 2.507
log log(2H) , and speciﬁcally when n = 1, 3, 5, can be
veriﬁed by hand). Thus we may bound

S2 ∑

1⩽n⩽H f (n) ⩽ (
e
γ log log(2H) + 2.507
log log(2H)
) ∑

n⩽H:(n,2)=1
 µ2(n)
φ(n) .

Since φ(n) = φ(2n) when n is odd, we have
∑

n⩽H:(n,2)=1
 µ2(n)
φ(n) ⩽ 1
2 ∑

n⩽2H
 µ2(n)
φ(n)

and hence by [35, Lemma 3.5], one has
∑

n⩽H:(n,2)=1
 µ2(n)
φ(n) ⩽ 1
2(log(2H) + 1.4709) ⩽ 1
2 log(9H).

Combining all these estimates we obtain the claim.

Remark. As observed by the anonymous referee, when H is an integer, the second
term in (4.15) may be deleted by using [36, Lemma 5.1] as a substitute for (4.17) (and
retaining the sum over h
′, rather than working only with the worst-case h
′).

To deal with Sη,q(x, α) on minor arcs, we follow the standard approach of Vinogradov
by decomposing this expression into linear (or “Type I”) and bilinear (or “Type II”)
sums. We will take advantage of the following variant of Vaughan’s identity [46], which
we formulate as follows:

Lemma 4.11 (A variant of Vaughan’s identity). Let U, V ⩾ 1. Then for any function
F : Z → C supported on the interval (V, UV 2), one has

| ∑

n Λ(n)F (n)| ⩽ TI + TII

where TI is the Type I sum9

TI := ∑

d⩽U V | ∑

n (log n + cd log d)F (dn)|

for some complex coeﬃcients cd (depending on F ) with |cd| ⩽ 1, and TII is the Type II
sum TII := | ∑

d>U
 ∑

w>V µ(d)g(w)F (dw)|

where g(w) is the function
 g(w) := ∑

b|w:b>V Λ(b) − 1
2 log w.

9Strictly speaking, TI is an average of Type I sums, rather than a single Type I sum; however we
shall abuse notation and informally refer to TI as a Type I sum.

24 TERENCE TAO

This diﬀers slightly from the standard formulation of Vaughan’s identity, as we have
subtracted a factor of 1
2 log w from the coeﬃcient g(w) of the Type II sum. This has
the eﬀect of improving the Type II sum by a factor of two, with only a negligible cost
to the (less important) Type I term.

Proof. We split µ = µ1⩽U + µ1>U and Λ = Λ1⩽V + Λ1>V , where 1⩽U (n) := 1n⩽U , and
similarly for 1>U , 1⩽V , 1>V . We then have
Λ = µ ∗ Λ ∗ 1
= µ1⩽U ∗ Λ ∗ 1 − µ1⩽U ∗ Λ1⩽V ∗ 1 + µ1>U ∗ Λ1>V ∗ 1 + µ ∗ Λ1⩽V ∗ 1
= µ1⩽U ∗ log −µ1⩽U ∗ Λ1⩽V ∗ 1 + µ1>U ∗ Λ1>V ∗ 1 + Λ1⩽V
 (4.18)

We sum this against F , noting that F vanishes on the support of the ﬁnal term Λ1⩽V ,
to conclude that ∑

n Λ(n)F (n) = ∑

d⩽U µ(d) ∑

n (log n)F (dn)

− ∑

d⩽U V f (d) ∑

n F (dn)

+ ∑

d>U
 ∑

w>V µ(d)(g(w) + 1
2 log w)F (dw)

where f (d) := ∑

b|d:d/U ⩽b⩽V µ( d
b )Λ(b).

Observe that when d > U and w > V , then the term µ(d)( 1
2 log w)F (dw) vanishes unless
U < d ⩽ UV . We may thus bound

| ∑

n Λ(n)F (n)| = ∑

d⩽U V | ∑

n (log n)F (dn)|

+ ∑

d⩽U V |f (d)|| ∑

n F (dn)|

+ | ∑

d>U
 ∑

w>V µ(d)g(w)F (dw)|.

Note that |f (d)| ⩽ ∑

b|d Λ(b) = log d.

Since
 | ∑

n (log n)F (dn)| + | ∑

n F (dn)| log d = | ∑

n (log n + cd log d)F (dn)|

for some complex constant cd with |cd| = 1, we obtain the claim.

Note that as 0 ⩽ ∑

b|w:b>V Λ(b) ⩽ ∑

b|w Λ(b) = log w

we have the bound |g(w)| ⩽ 1
2 log w. (4.19)

EVERY ODD NUMBER GREATER THAN 1 IS THE SUM OF AT MOST FIVE PRIMES 25

5. Minor arcs

We now prove the following exponential sum estimate, which will then be used in the
next section to derive Theorem 1.3:

Theorem 5.1 (Bound for minor arc sums). Let 4α = a
q + β for some natural number
q ⩾ 4 with (a, q) = 1 and some β = O∗(1/q2). Let 1 < U, V < x, and suppose that we
have the hypotheses
 UV ⩽ x/4 (5.1)

UV 2 ⩾ x (5.2)

U, V ⩾ 40. (5.3)

Then one has

|Sη,2(x, α)| ⩽ 0.5 x
q (log x) log (2UV
q + 4) + 0.89 (
UV + 5
2 q) (8 + log q) log(2x) (5.4)

+
 (
0.1 x
√
q + 0.39 x
√
x/q
 )
 (log x
UV ) log V x
U (5.5)

+ (
0.55 x
√
U + 0.78 x
√V
 ) log x
U . (5.6)

Furthermore, if a = ±1 and UV < q − 1, then we may replace the term (5.4) in the
above estimate with 96
π2 x
(x/q)2 log(4x) log 4eq
π . (5.7)

We now prove Theorem 5.1. By Lemma 4.11, we have

|Sη0,2(x, 1)| ⩽ TI + TII

where TI is the Type I sum

TI := ∑

d⩽U V :(d,2)=1 | ∑

n:(n,2)=1
(log n + cd log d)e(αdn)η0(dn/x)|

and TII is the Type II sum

TII := | ∑

d>U :(d,2)=1
 ∑

w>V :(w,2)=1 µ(d)g(w)e(αdw)η0(dw/x)|.

5.2. Estimation of the Type I sum. We ﬁrst bound the Type I sum TI. We begin
by estimating a single summand

| ∑

n (log n + cd log d)e(dnα)η0(dn/x)1(n,2)=1|. (5.8)

By Corollary 3.2, we may bound this expression by

min (
 1
2 ∥F ∥L1(R) + 1
2∥F ′∥L1(R), ∥F ′∥L1(R)
2| sin(2πdα)|, ∥F ′′∥L1(R)
2| sin(2πdα)|2
 )

26 TERENCE TAO

where F (y) = Fd(y) := η0(dy/x)(log y + cd log d). We have

F ′(y) = d
x η′
0(dy/x)(log y + cd log d) + η0(dy/x)
y

and
 F ′′(y) = d2

x2 η′′
0 (dy/x)(log y + cd log d) + 2 d
x η′
0(dy/x)
y − η0(dy/x)
y2 .

Strictly speaking, F is not inﬁnitely smooth, and so Corollary 3.2 cannot be directly
applied; however, we may perform the standard procedure of mollifying η0 (and thus
F ) by an inﬁnitesimal amount in order to make all derivatives here well-deﬁned, and
then performing a limiting argument. Rather than present this routine argument ex-
plicitly, we shall abuse notation and assume that η0 has been inﬁnitesimally molliﬁed
(alternatively, one can interpret the derivatives here in the sense of distributions, and
replace the L
1 norm by the total variation norm in the event that the expression inside
the norm becomes a signed measure instead of an absolutely integrable function).

Since d ⩽ U and η is supported on [1/4, 1], η(dy/x) is supported on [x/4d, x/d]. In
particular, | log y + cd log d| ⩽ log x. We thus have

∥F ∥L1(R) ⩽ ∥η0∥L1(R) x
d log x

∥F ′∥L1(R) ⩽ ∥η′
0∥L1(R) log x + ∥η0∥L∞(R) log 4

∥F ′′∥L1(R) ⩽ ∥η′′
0 ∥L1(R) d
x log x + 2∥η′
0∥L∞(R) d
x log 4 + ∥η0∥L∞(R) 4d
x .

Routine computations using (1.7) show that

∥η0∥L1(R) = 1 (5.9)

∥η0∥L∞(R) = 4 log 2 (5.10)

∥η′
0∥L1(R) = 8 log 2 (5.11)

∥η′
0∥L∞(R) = 16 (5.12)

∥η′′
0 ∥L1(R) = 48. (5.13)

Note that ∥η′
0∥L1(R) and ∥η′′
0 ∥L1(R) can also be interpreted as the total variation of the
functions η0 and η′
0 respectively, which may be an easier computation (especially since
η′′
0 is not a function before molliﬁcation, but is merely a signed measure). Inserting
these bounds, we conclude that

∥F ∥L1(R) ⩽ x
d log x

∥F ′∥L1(R) ⩽ 8(log 2) log 2x

∥F ′′∥L1(R) ⩽ 48 d
x log 4x.

We conclude that

TI ⩽ ∑

d⩽U V 1(d,2)=1 min (
 1
2 x
d log x + 4(log 2) log 2x, 4(log 2) log 2x
| sin(2πdα)| , d
x 24 log 4x
| sin(2πdα)|2
 ) .

(5.14)

EVERY ODD NUMBER GREATER THAN 1 IS THE SUM OF AT MOST FIVE PRIMES 27

We ﬁrst control the contribution to (5.14) when d ⩽ q/2. In this case, d is not divisible
by q; as (a, q) = 1, this implies that ad is not divisible by q either. We therefore have

∥4dα∥R/Z ⩾ ∥ad/q∥R/Z − d|β| ⩾ 1
q − q/2
q2 = 1
2q (5.15)

and thus 1
| sin(2πdα)| ⩽ 1
| sin(π/4q)| ⩽ 2q (5.16)

thanks to (2.1). Thus contribution here (5.14) of the d ⩽ q/2 terms are bounded by

4(log 2) log 2x ∑

d⩽q/2 1(d,2) min(2q, 1
| sin(2πdα)|).

By Corollary 3.5 one has
∑

d∈Z :−q/2⩽d⩽q/2 1(d,2) min(2q, 1
| sin(2πdα)|) ⩽ 2
π q log 4q + 4q

so by symmetry we may thus bound the contribution of the d ⩽ q/2 terms to (5.14) by

2 log 2 log 2x( 2
π q log 4q + 4q).

Now consider the contribution to (5.14) of a block of the form 2jq+ q
2 < d ⩽ 2(j +1)q+ q
2
for a natural number j with j ⩽ U V
2q − 1
4 . This contribution can be bounded by

∑

2jq+ q
2 <d⩽2(j+1)q+ q
2
 1(d,2)=1 min (
 1
2 x
2jq + q
2 log x + 4(log 2) log 2x, 4(log 2) log 2x
| sin(2πdα)|
 ) ,

which by Corollary 3.5 is bounded by
x
2jq + q
2 log x + 8(log 2) log 2x + 4(log 2) log 2x 2
π q log 4q

which we can crudely bound by
x
2jq + q
2 log x + 4(log 2) log 2x( 2
π q log 4q + 4q).

Combining all the contributions to (5.14), we obtain the bound

TI ⩽ ∑

0⩽j⩽ U V
2q − 1
4
 x
2jq + q
2 log x

+ ( UV
2q + 5
4 )( 2
π q log 4q + 4q) × 4(log 2) log 2x.

By the integral test, one has
∑

0⩽j⩽ U V
2q − 1
4
( x
2jq + q
2 ) ⩽ 1
2q
 ∫ U V +2q

q/2
 x
y dy

= x
2q log( 2UV
q + 4)

28 TERENCE TAO

and so
TI ⩽ x
2q log( 2UV
q + 4) log x + ( UV
2q + 5
4 )( 2
π q log 4q + 4q) × 4(log 2) log 2x.

We can write 2
π q log 4q + 4q ⩽ 2
π q(8 + log q)

and
 1
2 × 2
π × 4 log 2 ⩽ 0.89

and so
 TI ⩽ 0.5 x
q log( 2UV
q + 4) log x + 0.89(UV + 5
2q)(8 + log q) log x (5.17)

which gives the term (5.4).

Now suppose that a = ±1 and UV < q − 1. By the symmetry (4.5) we may take a = 1,
thus α = 1
4q + O∗( 1
4q2 ) ⩽ 1
4(q−1) . In particular, for d ⩽ UV one has d ⩽ q − 2 and
therefore 0 < 2πdα < π/2. In particular, we have

sin(2πdα) ⩾ sin ( 2πd
4(q − 1)
 ) .

From (5.14), we conclude that

TI ⩽ 24 log 4x
x
 q−2∑

d=1 d cosec2 πd
2(q − 1) .

The function d ↦→ d cosec2 πd
2(q−1) is convex on [0, π] (indeed, both factors are already
convex), and so by the trapezoid rule

TI ⩽ 24 log 4x
x
 ∫ q−3/2

1/2 ycosec2 πy
2(q − 1) dy.

Using the anti-derivative ∫ ycosec
2y dy = log | sin y| − y cot y

we can evaluate the right-hand side as

( 2(q − 1)
π )2 24 log 4x
x (log | sin y| − y cot y)|y=π/2−π/4(q−1)
y=π/4(q−1)

The function y cot y varies between 0 and 1 on [0, π/2], and thus

TI ⩽ ( 2(q − 1)
π )2 24 log 4x
x (log cot π
4(q − 1) + 1)

which, on bounding cot π
4(q−1) ⩽ 4(q−1)
π ⩽ 4q
π and 2(q−1)
π ⩽ 2q
π , gives

TI ⩽ 96
π2 x
(x/q)2 log(4x) log( 4eq
π ) (5.18)

which is the alternate contribution (5.7).

EVERY ODD NUMBER GREATER THAN 1 IS THE SUM OF AT MOST FIVE PRIMES 29

5.3. Estimation of the Type II sum. We now control TII. From (1.8) and the
triangle inequality, we thus have

TII ⩽ 4 ∫ ∞

0 F (W ) dW
W (5.19)

where

F (W ) := | ∑

d>U
 ∑

w>V µ(d)1(d,2)=11[x/2W,x/W ](d)g(w)1(w,2)=11[W/2,W ](w)e(αdw)|.

Observe that F (W ) vanishes unless
 V ⩽ W ⩽ x
U , (5.20)

and we henceforth restrict attention to this regime.

From (5.20), (5.3) we see that the intervals [x/2W, x/W ], [W/2, W ] both have length
at least 2. We now apply Corollary 3.9 with M := q/2 and use (4.19) to bound

F (W ) ⩽ 1
2
 (
 1
2 W
2 + 1
δ
 )1/2 (⌊ x
2W q ⌋ + 1)1/2 A
1/2B1/2 (5.21)

where
10
 δ := inf
1⩽j⩽q/2 ∥4jα∥R/Z

A := ∑

d∈[x/2W,x/W ] 1(d,2)=1

B := ∑

w∈[W/2,W ] 1(w,2)=1 log2 w.

From the computation (5.15) we have
 δ ⩾ 1
2q . (5.22)

Now we bound A and B. Clearly we have

|A| ⩽ x
4W + 1.

Similarly, for B we bound log2 w by log2 W , and conclude that

|B| ⩽ ( W
4 + 1) log2 W.

By (5.3), (5.20) we thus have
 |A| ⩽ 1.1
4 x
W

|B| ⩽ 1.1
4 W log2 W

10One could achieve a very slight improvement to the A factor by exploiting the fact that µ2(n)
vanishes when n is divisible by an odd square, but we will not do so here to keep the exposition simple.

30 TERENCE TAO

and thus by (5.21), (5.22)

F (W ) ⩽ 1.1
8 ( W
4 + 2q)1/2( x
2W q + 1)1/2x
1/2 log W.

Crudely bounding11 (a + b)1/2 ⩽ a
1/2 + b
1/2 we thus have

F (W ) ⩽ 1.1
8 ( 1
2√2 x
√q + 1
2√xW + 1
√2 x
√W + √2 x
√x/q ) log W.

We integrate this expression over (5.20) against the measure 4dW
W to bound (5.19). To
simplify the computations slightly at the cost of a slight degradation of the numerical
constants, we bound log W crudely by log x
U for the middle two terms for F (W ). Since

4 ∫

V ⩽W ⩽ x
U
 dW
W = 2 log x
UV log V x
U ,

we thus obtain the bound

TII ⩽ 1.1
4
 ( 1
2√2 x
√q + √2 x
√x/q
 )
 log x
UV log V x
U

+ 1.1 (
 1
2 x
√U + 1
√2 x
√V
 ) log W.

Combining this with (5.17) and (5.18) we obtain the claim.

Remark. When β is very small (of size O(1/x) or so), one can eliminate most of the
0.5 x
q log x log( 2U V
q + 4) term in (5.4) by working with Sη,q(x, α) − µ2(q)
φ(q) Sη,q(x, β) in-
stead of Sη,2(x, α), which eﬀectively replaces the phase e(αn) with the variant phase
(e(an/q) − µ2(q)
φ(q) )e(βn)1(n,q)=1. The main purpose of this replacement is to delete the
non-cancellative component of the Type I sum (which, for small values of β, occurs when
d is divisible by q), which would otherwise generate the x
q log2 x type term in (1.10).
Such an improvement may be useful in subsequent work on Goldbach-type problems,
but we will not pursue it further here
12.

6. Proof of Theorem 1.3

In this section we use Theorem 5.1 to establish Theorem 1.3, basically by applying
speciﬁc values of U and V . With more eﬀort, one could optimise in U and V more
carefully than is done below, which would improve the numerical values in Theorem 1.3
by a modest amount, but we will not do so here to keep the exposition as simple as
possible.

We begin with (1.9). We apply Theorem 5.1 with

U := 1
4 x
2/5, V := 1
2 x
2/5.

11By avoiding this step, one could save a modest amount in the numerical constants in the estimates,
but at the cost of a more complicated argument.
12For very small values of q, it is likely that one should instead proceed using diﬀerent identities than
Vaughan-type identities, for instance by performing an expansion into Dirichlet characters instead.

EVERY ODD NUMBER GREATER THAN 1 IS THE SUM OF AT MOST FIVE PRIMES 31

As x ⩾ 1020, the hypotheses of the theorem are obeyed, and we conclude that

|Sη,2(x, α)| ⩽ 0.5 x
q log x log(x
4/5) + 0.89( 1
8x
4/5 + 5
2 q)(8 + log q) log 2x

+ (0.1 x
√q + 0.39 x
√
x/q ) log(8x
1/5) log(2x)

+ 2.3x
4/5 log(2x
3/5).

As x ⩾ 1020 and q ⩽ x/100, one can compute that

log(8x
1/5) log(2x) ⩽ 1
5 log x(log x + 11.3)

(8 + log q)(log 2x) ⩽ 1.1 log x(log x + 11.3)

log(2x
3/5) ⩽ 0.011 log x(log x + 11.3);

inserting these bounds and collecting terms, we conclude that

|Sη,2(x, α)| ⩽ (0.4 x
q + 0.1 x
√q + 2.45 x
x/q + 0.39 x
√
x/q + 0.149x
4/5) log x(log x + 11.3).

Since 100 ⩽ q ⩽ x/100, one has
 0.4 x
q ⩽ 0.04 x
√q

and 2.45 x
x/q ⩽ 0.245 x
√
x/q
and the claim (1.9) follows, after using Lemma 4.1 to replace Sη,2(x, α) with Sη,q0(x, α)
(at the cost of replacing the 0.149x
4/5 term with 0.15x
4/5).

Now we verify (1.10). Here we use the choice

U := x
q2 ; V := q.

The hypotheses of Theorem 5.1 are easily veriﬁed, and we conclude that

|Sη,2(x, α)| ⩽ 0.5 x
q log x log( 2x
q2 + 4) + 0.89( x
q + 5
2 q)(8 + log q) log(2x)

+ (0.1 x
√q + 0.39 x
√
x/q ) × 3 log2 q

+ (0.55 x
√
x/q2 + 0.78 x
√
q ) × 2 log q.

Since q ⩽ x
1/3 and x ⩾ 1020, one has x
√x/q2 ⩽ x
√q

and x
√
x/q ⩽ 0.001 x
√
q
and q ⩽ 0.001 x
q

32 TERENCE TAO

and so
 |Sη,2(x, α)| ⩽ x
q log(2x)[0.5 log( 2x
q2 + 4) + 0.9(8 + log q)]

+ (0.301 log2 q + 2.66 log q) x
√q .

Since
 0.5 log( 2x
q2 + 4) + 0.9(8 + log q) ⩽ 0.5(log(2x + 4q2) + 14.4)

⩽ 0.5(log(2x) + 15)

(using the hypotheses q ⩽ x
1/3 and x ⩾ 1020) and

0.301 log2 q + 2.66 log q ⩽ 0.301 log q(log q + 8.9)

we obtain the claim (1.10), after using Lemma 4.1 to replace Sη,2(x, α) with Sη,q0(x, α)
(and replacing 0.301 with 0.31).

Now we prove (1.11). Here we use the choice

U := x
(x/q)2 ; V := x/q.

Again, the hypotheses of Theorem 5.1 are easily veriﬁed, and we conclude that

|Sη,2(x, α)| ⩽ 0.5 x
q log x log 6 + 0.89( 7
2q)(8 + log q) log(2x)

+ (0.1 x
√
q + 0.39 x
√
x/q ) × 3 log2 x
q

+ (0.55 x
√
x/(x/q)2 + 0.78 x
√
x/q ) × 2 log x
q .

Since q ⩾ x
2/3 and x ⩾ 1020, one has x
√
x/(x/q)2 ⩽ x
√
x/q

and x
√q ⩽ 0.001 x
√
x/q
and x
q ⩽ 0.001q

and thus
 |Sη,2(x, α)| ⩽ 3.12q(8 + log q) log(2x)

+ (1.181 log2 x
q + 2.66 log x
q ) x
√
x/q .

Writing 1.181 log2 x
q + 2.66 log x
q ⩽ 1.181 log x
q (log x
q + 2.3)

we obtain the claim (1.11), after using Lemma 4.1 to replace Sη,2(x, α) with Sη,q0(x, α)
(and replacing 1.181 with 1.19).

EVERY ODD NUMBER GREATER THAN 1 IS THE SUM OF AT MOST FIVE PRIMES 33

Finally, we establish (1.12). Here we use the choice

U := x
(1.02x/q)2 ; V := 1.02x/q

to ensure that UV < q − 1. We may now use the term (5.7) and conclude that

|Sη,2(x, α)| ⩽ 96
π2 x
(x/q)2 log(4x) log 4eq
π

+ (0.1 x
√
q + 0.39 x
√
x/q ) × 3 log2(1.02x/q)

+ (0.55 x
√
x/(1.02x/q)2 + 0.78 x
√
1.02x/q ) × 2 log(1.02x/q).

We can bound
 log 4eq
π ⩽ log(x/4)

and hence log(4x) log(x/4) ⩽ log2 x.

Also, as q ⩾ x
1/3 and x ⩾ 1020, onehas
x
√x/(1.02x/q)2 ⩽ 1.02 x
√
x/q

and x
√q ⩽ 0.001 x
√
x/q

and thus
 |Sη,2(x, α)| ⩽ 96
π2 x
(x/q)2 log2 x

+ 1.19 x
√
x/q log2(1.02x/q)

+ 2.67 x
√
x/q log(1.02x/q).

The last two terms can be bounded by (1.19 log 1.02x
q ) × (log 1.02x
q + 2.3). Since

1.19 log 1.02x
q ⩽ 1.2 log x
q

and
 log 1.02x
q + 2.3 ⩽ log x
q + 2.35

and 96
π2 ⩽ 9.73

the claim (1.12) follows, after using Lemma 4.1 to replace Sη,2(x, α) with Sη,q0(x, α)
(and replacing 2.35 with 2.4).

34 TERENCE TAO

7. Major arc estimate

In this section we use Theorem 1.5 to control exponential sums in the “major arc”
regime α = O(T0/x). To link the von Mangoldt function to the zeroes of the zeta
function we use the following standard identity:

Proposition 7.1 (Von Mangoldt explicit formula). Let η : R → C be a smooth, com-
pactly supported function supported in [2, +∞). Then
∑

n Λ(n)η(n) = ∫

R (1 − 1
x3 − x)η(y) dy − ∑

ρ
 ∫

R η(y)yρ−1 dy (7.1)

where ρ ranges over the non-trivial zeroes of the Riemann zeta function.

Proof. See, for instance, [19, §5.5].

Proposition 7.2 (Major arc sums). Let T0 be as in Theorem 1.5. Let η : R → R+ be a
smooth non-negative function supported on [c, c′], and let x, α ∈ R be such that cx ⩾ 103

and |α| ⩽ T0
4πc′x . (7.2)

Then

|Sη,1(x, α) − x ∫

R η(y)e(αxy) dy| ⩽ Alog T0
3T0 x + 2.01c−1/2x
1/2N(T0)∥η∥L1(R), (7.3)

where A is the quantity

A := 60∥η∥L1(R) + 32c′∥η′∥L1(R) + 4(c′)2∥η′′∥L1(R) (7.4)

and N(T0) is the number of zeroes of ζ in the strip {0 ⩽ ℜ(s) ⩽ 1; 0 ⩽ ℑ(s) ⩽ T0}.

As should be clear from the proof, the constant A can be improved somewhat by a
more careful argument, for instance by exploiting the functional equation for ζ, which
places at most half of the zeroes to the right of the critical line ℜρ = 1/2. However, this
does not end up being of much signiﬁcance, as the right-hand side of (7.3) is already
small enough for our purposes (thanks to the large denominator of T0). It may appear
odd that the condition (7.2) allows for |α| to exceed 1, but the estimate (7.3) becomes
weaker than the trivial bound in Lemma 4.3 in this case.

For our particular choice of T0, namely T0 := 3.29 × 109, the quantity N(T0) can be
bounded by 1010 (indeed, the value of T0 we have chosen arose from the veriﬁcation
that the ﬁrst 1010 zeroes of ζ were on the critical line).

Proof. We have Sη,1(x, α) = ∑

n Λ(n)η(n/x)e(αn).

Applying (7.1), we conclude that the left-hand side of (7.3) is bounded by
∫

R
 1
y3 − y η(y/x) dy + ∑

ρ
 ∣
∣
∣
∣

∫
R η(y/x)e(αy)yρ−1 dy∣
∣
∣
∣

EVERY ODD NUMBER GREATER THAN 1 IS THE SUM OF AT MOST FIVE PRIMES 35

Crudely bounding 1
y3−y by 2
(cx)3 on the support of η(y/x), the ﬁrst term is at most
2c−3x
−2∥η∥L1(R). Now we turn to the second sum. We write ρ = σ + it with 0 < σ < 1
and t ∈ R.

We ﬁrst consider the contribution of those zeroes with |t| ⩽ T0. By hypothesis, σ = 1/2
for these zeroes, and we may bound this portion of the sum by
∑

ρ:|t|⩽T0
 ∫
R η(y/x)y−1/2 dy

which we may bound in turn by

2c−1/2x
1/2N(T0)∥η∥L1(R).

As T0 ⩾ 103 and cx ⩾ 103, we may clearly absorb the much smaller error term
2c−3x
−2∥η∥L1(R) into this term by increasing the 2 factor to 2.01.

Finally, we consider the terms with |t| > T0. We may rewrite a single integral

| ∫

R η(y/x)e(αy)yρ−1 dy| (7.5)

as
 | ∫

R f (y)e
i(2παy+t log y) dy|

where f (y) := η(y/x)yσ−1. Since

e
i(2παy+t log y) = 1
i(2πα + t/y) d
dy e
i(2παy+t log y)

with the denominator non-vanishing on the support of η(y/x) thanks to (7.2), we may
integrate by parts and write the preceding integral as

| ∫

R
 d
dy
 ( 1
2πα + t/y f (y)) e
i(2παy+t log y) dy|.

A second integration by parts then rewrites the above expression as

| ∫

R
 d
dy
 ( 1
2πα + t/y d
dy
 ( 1
2πα + t/y f (y))) e
i(2παy+t log y) dy|

which we then bound by
∫

R | d
dy
 ( 1
2πα + t/y d
dy
 ( 1
2πα + t/y f (y))) | dy.

The expression inside the absolute value can be expanded as

t
2/y4 − 4παt/y3

(2πα + t/y)4 f (y)

+ 3t/y2

(2πα + t/y)3 f ′(y)

+ 1
(2πα + t/y)2 f ′′(y).

36 TERENCE TAO

On the support of f one has y ⩽ c′x. From (7.2) we may thus lower bound

|2πα + t/y| ⩾ |t|
2y

and upper bound
 |t
2/y4 − 4παt/y3| ⩽ 2t
2

y4 ,

and so the preceding integral may be bounded by

32
t2
 ∫

R |f (y)|dy

+ 24
t2
 ∫

R y|f ′(y)| dy

+ 4
t2
 ∫

R y2|f ′′(y)| dy.

Since 0 ⩽ σ ⩽ 1, we have the crude bounds

|f (y)| ⩽ η(y/x)

|f ′(y)| ⩽ 1
x|η′(y/x)| + 1
y η(y/x)

|f ′′(y)| ⩽ 1
x2 |η′′(y/x)| + 2
xy |η′(y/x)| + 1
y2 η(y/x)

and so (on bounding y from above by c′x) we may bound (7.5) by

A x
t2

where A is the quantity deﬁned in (7.4). From [40, Lemma 2], we may bound
∑

ρ:|t|⩾T0
 1
t2 ⩽ 1
πT0 (log T0
2π + 1) + 1.34
T 2
0 (2 log T0
2π + 1),

which under the hypothesis T0 ⩾ 103 can be bounded above by

log T0
3T0 .

The claim then follows.
 8. Sums of five primes

In this section we establish Theorem 1.4. We recall the following result of Ramar´e and
Saouter:

Theorem 8.1. If x ⩾ 1.1 × 1010 is a real number, then there is at least one prime p ⩽ x
with x − p ⩽ x
2.8×107 .

EVERY ODD NUMBER GREATER THAN 1 IS THE SUM OF AT MOST FIVE PRIMES 37

Proof. See [40, Theorem 3]. One of the main tools used in the proof is Theorem 1.5.
By using the more recent numerical veriﬁcations of the Riemann hypothesis, one can
improve this result; see [18]. However, we will not need to do so here.

By combining the above result with Theorem 1.6, we see that

• Every odd number between 3 and (2.8 × 107)N0 is the sum of at most three
primes.
• Every even number between 2 and (2.8 × 107)2N0 is the sum of at most four
primes.
• Every odd number between 3 and (2.8 × 107)3N0 is the sum of at most ﬁve
primes.

In particular, Theorem 1.4 holds up to (2.8 × 107)3N0 ⩾ 8.7 × 1036. Thus, it suﬃces to
verify Theorem 1.4 for odd numbers larger than 8.7 × 1036.

On the other hand, in [24] it is shown that every odd number larger than exp(3100) is
the sum of three primes. It will then suﬃce to show that

Theorem 8.2. Let 8.7 × 1036 ⩽ x ⩽ exp(3100) be an integer. Then there is an integer
in the interval [x − N0, x − 2] which is the sum of three odd primes.

We establish this theorem by the circle method. Fix x as above. We will need a
symmetric, Lipschitz, L
2-normalised cutoﬀ function η1 which is close to 1[0,1]. For sake
of concreteness we will take

η1(t) := (1 − 10 dist(t, [0.2, 0.8]))+,

which is supported on [0.1, 0.9] and obeys the symmetry

η1(1 − t) = η1(t) for all t ∈ R. (8.1)

For future reference we record some norms on η1 (after performing an inﬁnitesimal
molliﬁcation):
 ∥η1∥L2(R) =
 √2
3 (8.2)

∥η1∥L∞(R) = 1 (8.3)

∥η1∥L1(R) = 7
10 (8.4)

∥η′
1∥L∞(R) = 10 (8.5)

∥η′
1∥L1(R) = 2 (8.6)

∥η1η′
1∥L1(R) = 1 (8.7)

∥η′′
1 ∥L1(R) = 40 (8.8)

∥η′
1η′
1 + η1η′′
1 ∥L1(R) = 40. (8.9)

38 TERENCE TAO

For a parameter K ⩾ 1 to be chosen later, we will consider the quantity
13
∑

n1,n2,n3
 ∑

1⩽h1,h2,h3⩽N0/3Λ(n1)1(n1,√
x♯)=1η1(n1/x)Λ(n2)1(n2,√
x♯)=1η1(n2/x)

× Λ(n3)1
(n3,√x/K♯)=1η0(Kn3/x)1x=n1+n2+n3+h1+h2+h3 (8.10)

Observe that the summand is only non-zero when n1, n2, n3 are odd primes (of magni-
tudes less than x, x, and x/K respectively) with n1 + n2 + n3 ∈ [x − N0, x − 2]. Thus, to
prove Theorem 8.2, it suﬃces to show that the quantity (8.10) is strictly positive. Ap-
plying the prime number heuristic Λ ≈ 1 and (8.2), we see that we expect the quantity
(8.10) to be of size roughly 2
3 x
3K −1(N0/3)3.

Note that we have made the third prime n3 somewhat smaller than the other two.
This trick, originally due to Bourgain [3], helps remove some losses associated to the
convolution of the cutoﬀ functions η1, η0.

By Fourier analysis, we may rewrite (8.10) as
∫

R/Z Sη1,√x♯(x, α)2Sη0,√x/K♯(x/K, α)DN0/3(α)3e(−xα) dα (8.11)

where DN0/2(α) is the Dirichlet-type kernel

DN0/2(α) := ∑

1⩽n⩽N0/3 e(nα).

It thus suﬃces to show that the expression is non-zero for some K. It turns out that
there is some gain to be obtained (of about an order of magnitude) in the weakly minor
arc regime when α is slightly larger than T0/x, by integrating K over an interval inside
[1, T0] that is well separated from both endpoints; for instance, one could integrate
K from 103 to 106. Such a gain could be useful for further work on Goldbach type
problems; however, for the problem at hand, it will be suﬃcient to select a single value
of K, namely K := 103.

As mentioned previously, the expected size of the quantity (8.11) is roughly 2
3 x2
K (N0/3)3.
This heuristic can be supported by the following major arc estimate:

Proposition 8.3 (Strongly major arc estimate). We have
∫

∥α∥R/Z⩽ T0
3.6πx Sη1,√x♯(x, α)2Sη0,√x/K♯(x/K, α)DN0/3(α)3e(−xα) dα

= x
2

K (N0/3)3( 2
3 + O∗(0.1)).
 (8.12)

13The ranges of the h1, h2, h3 parameters are not optimal; one could do a bit better, for instance,
by requiring 1 ⩽ h1, h2 ⩽ N0/20 and 1 ⩽ h3 ⩽ 0.9N0 instead, as this barely impacts Proposition 8.4,
but reduces the upper bound in (8.19) by almost a factor of three. However, we will not need this
improvement here.

EVERY ODD NUMBER GREATER THAN 1 IS THE SUM OF AT MOST FIVE PRIMES 39

Proof. From the mean value theorem one has

DN0/3(α) = (N0/3)(1 + O∗(2π(N0/3)∥α∥R/Z )) = (N0/3)(1 + O∗( N0T0
5.4x ))

when ∥α∥R/Z ⩽ T0
3.6πx . Since N0 = 4 × 1014, T0 = 3.29 × 109, and x ⩾ 8.7 × 1036, we
conclude that DN0/3(α) = (N0/2)(1 + O∗(10−10)) (8.13)

(with plenty of room to spare). Also, by Proposition 7.2, for α in the interval [− T0
3.6πx , T0
3.6πx ]
(and in fact for all α in the wider interval [− KT0
4πx , KT0
4πx ]), one has

Sη0,1(x/K, α) = x
K ˆη0(αx/K) + O∗(A2 log T0
3T0
 x
K + 2.01x
1/2K −1/2N(T0)∥η0∥L1(R))

where ˆη0(α) := ∫

R η0(y)e(αxy) dy and

A2 := 60∥η0∥L1(R) + 32∥η′
0∥L1(R) + 4∥η′′
0 ∥L1(R).

From (5.9), (5.11), (5.13) one has

A2 = 252 + 256 log 2 ⩽ 330

and with x ⩾ 8.7 × 1036, K = 103, T0 = 3.29 × 109, and N(T0) ⩽ 1010, we conclude that

Sη0,1(x/K, α) = x
K (ˆη0(αx/K) + O∗(10−6)).

By Lemma 4.1 and (8.13) (and bounding ˆη0(αx) as O∗(1) whenever necessary) we then
have
 Sη0,√x/K♯(x/K, α)DN0/3(α)3 = x(N0/3)3

K (ˆη0(αx) + O∗(1.1 × 10−6)).

Let us consider the contribution of the error term x(N0/3)3

K O∗(1.1 × 10−6) to (8.12). By
Corollary 4.7, we may bound this contribution in magnitude by

1.1 × 10−6 x(N0/3)3

K 2

1 − log(2T0/3π)
log x Sη2
1 ,√
x/K♯(x, 0)

which by Lemma 4.3 and the bounds T0 = 3.29 × 109, x ⩾ 8.7 × 1036 can be safely
bounded by
 10−3 x
2(N0/3)3

K .

Thus it will suﬃce to show that
∫

|α|⩽ T0
3πx Sη1,√
x♯(x, α)2 ˆη0(αx/K)e(−xα) dα = x( 2
3 + O∗(0.09)). (8.14)

We apply Proposition 7.2 again to obtain

Sη1,1(x, α) = xˆη1(αx) + O∗(A1 log T0
3T0 x + 2.01c−1/2
1 x
1/2N(T0)∥η1∥L1(R))

where ˆη1(α) := ∫

R η1(y)e(αxy) dy and

A1 := 60∥η1∥L1(R) + 32c′
1∥η′
1∥L1(R) + 4(c′
1)2∥η′′
1 ∥L1(R)

40 TERENCE TAO

with c1 := 0.1, c′
1 = 0.9. From (8.4), (8.6), (8.8) one has

A1 = 229.2

and with x ⩾ 8.7 × 1036, T0 = 3.29 × 109, and N(T0) ⩽ 1010, we conclude that

Sη1,1(x, α) = x(ˆη1(αx) + O∗(10−6)).

Bounding ˆη0 as O∗(1), we may thus express the left-hand side of (8.14) as the sum of
the main term
 x
2 ∫

|α|⩽ T0
3.6πx ˆη1(αx)2 ˆη0(αx/K)e(−xα) dα

and the two error terms
 O∗(10−6x ∫

|α|⩽ T0
3.6πx |Sη1,1(x, α)| dα) (8.15)

and
 O∗(10−6x
2 ∫

|α|⩽ T0
3.6πx |ˆη1(αx)| dα). (8.16)

We ﬁrst estimate (8.15). From Corollary 4.7 and Lemma 4.3 we have
∫

|α|⩽ T0
3.6πx |Sη1,1(x, α)|2 dα ⩽ 2

1 − log(2T0/3.6π)
log x × 4 log 2 × 1.04x

and so by Cauchy-Schwarz we may bound (8.15) by

10−6x

√ T0
3.6π ( 2

1 − log(2T0/3.6π)
log x × 4 log 2 × 1.04)1/2;

since x ⩾ 8.7 × 1036, T0 = 3.29 × 109, we may bound (8.15) by 0.02x. A similar (in
fact, slightly better) bound obtains for (8.16) (using Plancherel’s theorem in place of
Corollary 4.7). We conclude that it will suﬃce to show that
∫

|α|⩽ T0
3.6πx ˆη1(αx)2 ˆη0(αx/K)e(−xα) dα = 1
x (1 + O∗(0.05)).

By Lemma 3.3 we have
 |ˆη1(αx)| ⩽ ∥η′
1∥L1(R)
2π|α| = 1
π|α|;

from this and the choice T0 = 3.29 × 109 one easily veriﬁes that
∫

|α|> T0
3.6πx ˆη1(αx)2 ˆη0(αx/K)e(−xα) dα = O∗(0.01 1
x)

and so it remains to show that
∫
R ˆη1(αx)2 ˆη0(αx/K)e(−xα) dα = 1
x(1 + O∗(0.04)).

The left-hand side can be expressed as

1
x
 ∫
R
 ∫

R η1(s)η1(1 − s − t/K)η0(t) dsdt;

EVERY ODD NUMBER GREATER THAN 1 IS THE SUM OF AT MOST FIVE PRIMES 41

as η0 has an L
1 norm of 1, it thus suﬃces to show that
∫
R η1(s)η1(1 − s − t/K) ds = 1 + O∗(0.04)

for all t = O∗(1). By (8.1) and (8.5) one has

η1(1 − s − t/K) = η1(s) + O∗(10/K)

and so (by (8.4) and the L
1-normalisation of η0)
∫
R η1(s)η1(1 − s − t/K) ds = 1 + O∗(10/K).

Since K = 103, the claim follows.

In view of the above proposition, it suﬃces to show that
∫

∥α∥R/Z⩾ T0
3.6πx |Sη1,√x♯(x, α)|2|Sη0,√
x/K♯(x/K, α)||DN0/3(α)|3 dα ⩽ 0.56 x
2

K (N0/3)2.

(8.17)

We have the following L
2 estimate:

Proposition 8.4 (L
2 estimate). We have
∫

∥α∥R/Z⩾ T0
3.6πx |Sη1,√
x♯(x, α)|2|DN0/3(α)|2 dα ⩽ 7.09(N0/3)2x.

Proof. By Proposition 4.10 we have
∫

R/Z |Sη1,√
x♯(x, α)|2|DN0/3(α)|2 dα ⩽ 8H 2x
 (
1 + 0.13 log x
H + (e
γ log log(2H) + 2.507
log log(2H) ) log(9H)

2H
 )
 .

where H := ⌊N0/3⌋. Since log x ⩽ 3100 and N0 = 4 × 1014, a brief computation then
shows that ∫

R/Z |Sη1,√x♯(x, α)|2|DN0/3(α)|2 dα ⩽ 8.001(N0/3)2x.

Meanwhile, from Corollary 4.8 (using the values x ⩾ 8.7 ×1036, T0 = 3.29 ×109, c = 0.1,
and the estimates (8.3), (8.7), (8.9) to verify the hypotheses of that corollary), we have
∫

∥α∥R/Z⩾ T0
3.6πx |Sη1,√
x♯(x, α)|2 dα ⩾ 0.92x.

and thus by (8.13)
∫

∥α∥R/Z⩾ T0
3.6πx |Sη1,√x♯(x, α)|2|DN0/3(α)|2 dα ⩾ 0.919(N0/3)2x.

Subtracting, one obtains the bound.

In view of this proposition and H¨older’s inequality, it suﬃces to show the L
∞ estimate
that |Sη0,√x/K♯(x/K, α)||DN0/3(α)| ⩽ 0.078x(N0/3) x
K (8.18)

42 TERENCE TAO

whenever ∥α∥R/Z ⩾ T0
3.6πx ; comparing this with Lemma 4.3, we see that we have to
beat the “trivial” bounds in that lemma by a factor of roughly 13. By the conjugation
symmetry (4.5) we may assume that
 T0
3πx ⩽ α ⩽ 1
2.

We ﬁrst consider the case of the weakly major arc regime

T0
3.6πx < α ⩽ KT0
4πx .

By the computations in the proof of Proposition 8.3, we have

Sη0,√
x/K♯(x/K, α) = x
K (ˆη0(αx/K) + O∗(1.1 × 10−6))

in this regime, so by the trivial bound |DN0/3(α)| ⩽ (N0/3) it suﬃces to show that

|ˆη0(αx/K)| ⩽ 0.077.

By Lemma 3.3, we have
 |ˆη0(αx/K)| ⩽ ∥η′
0∥L1(R)
2π|α|x/K .

Since α ⩾ T0
3.6πx , we conclude from (5.10) that

|ˆη0(αx/K)| ⩽ 7.2K log 2
T0 ,

and the claim follows (with plenty of room to spare) from the choices K = 103, T0 =
3.29 × 109.

Next, we observe from Lemma 4.3 and (5.11) (and the lower bound x/K ⩾ 8.7 × 1033)
that |Sη0,√x/K♯(x/K, α)| ⩽ Sη0,1(x/K, 0) ⩽ 1.01 x
K ;

combining this with the crude bound

|DN0/3(α)| ⩽ 2
|1 − e(α)| = 1
| sin(πα)| ⩽ 1
2α

(by (2.1)), we have
 |Sη0,√x/K♯(x/K, α)||DN0/3(α)| ⩽ 1.01
2α x
K
which gives (8.18) whenever
 α ⩾ 20
N0
and so we may assume that KT0
3πx ⩽ α < 20
N0 . (8.19)

In this regime we use the crude bound |DN0/3(α)| ⩽ N0/3, and reduce to showing that

|Sη0,√x/K♯(x/K, α)| ⩽ 0.078x. (8.20)

EVERY ODD NUMBER GREATER THAN 1 IS THE SUM OF AT MOST FIVE PRIMES 43

We may write 4α = 1
q + O∗(1/q2) for some

1
4α − 1 ⩽ q ⩽ 1
4α ;

in particular N0
80 − 1 ⩽ q ⩽ πx
KT0 .

We ﬁrst consider the weakly minor arc case

(x/K)2/3 ⩽ q ⩽ πx
KT0 .

In this case we may use (1.12) to bound the left-hand side of (8.20) by

(9.73 1
(x/Kq)2 log2(x/K) + 1.2 1
√x/Kq log x
Kq (log x
Kq + 2.4)) x
K .

Since x/q ⩾ T0/π, we can bound this by

(9.73( π
T0 )2 log2 x + 1.19 √π
√T0 log(T0/π)(log(T0/π) + 2.3)) x
K .

As log x ⩽ 3100 and T0 = 3.29 × 109, the expression inside the parentheses is certainly
less than 0.078 (in fact it is less than 0.004). Note here that the computations would
not have worked if we had used the weaker bounds (1.9), (1.11) in place of (1.12).

Next, we consider the intermediate minor arc case

(x/K)1/3 ⩽ q ⩽ (x/K)2/3.

Here, we use (1.9) to bound the left-hand side of (8.20) by

(0.14 y
√
q + 0.64 1
√
y/q + 0.15y−1/5) log y(log y + 11.3) × x
K .

where y := x/K. Using the bounds on q, this can be bounded in turn by

(0.8y−1/6 + 0.027y−1/5) log y(log y + 11.3) × x
K .

Since y ⩾ 8.7 × 1033, the expression (0.8y−1/6 + 0.15y−1/5) log y(log y + 11.3) is bounded
by 0.078 (in fact it is less than 0.013), so this case is also acceptable.

Finally, we consider the strongly minor arc case
N0
80 − 1 ⩽ q ⩽ (x/K)1/3.

Note that this case can be vacuous if x is too small. In this case we use (1.10) to bound
the left-hand side of (8.20) by

[0.5 1
q log(2x/K)(log(2x/K) + 15) + 0.31 1
√q log q(log q + 8.9)] × x
K .

Since log(2x/K) ⩽ log x ⩽ 3100 and q ⩾ N0
80 − 1 = 5 × 1012 − 1, the expression in
brackets is bounded by 0.078 (in fact it is less than 0.0002). This concludes the proof
of (8.18) in all cases, and hence of Theorem 1.4.

44 TERENCE TAO

References

[1] E. Bombieri, H. Davenport, On the large sieve method, Abh. aus Zahlentheorie und Analysis zur
Erinnerung an Edmund Landau, Deut. Verlag Wiss., Berlin, 1122, 1968.
[2] Y. Buttkewitz, Exponential sums over primes and the prime twin problem, Acta Math. Hungar.
131 (2011), no. 1-2, 46-58.
[3] J. Bourgain, On triples in arithmetic progression, Geom. Funct. Anal. 9 (1999), no. 5, 968984.
[4] J. Chen, On the estimation of some trigonometric sums and their applications (Chinese), Scientia
Sinica 28 (1985), 449–458.
[5] J. R. Chen and T. Z. Wang, On odd Goldbach problem, Acta Math. Sinica 32 (1989), 702-718.
[6] J. Chen, T. Wang, Estimation of linear trigonometric sums with primes (Chinese), Acta Mathe-
matica Sinica 37 (1994), 25–31.
[7] H. Daboussi, Eﬀective estimates of exponential sums over primes, Analytic Number Theory, Vol.
1, Progr. Math. 138, Birkh¨auser, Boston 1996, 231–244.
[8] H. Daboussi, J. Rivat, Explicit upper bounds for exponential sums over primes, Math. Computation
70 (2000), 431–447.
[9] J.-M. Deshouillers, G. Eﬃnger, H. te Riele, D. Zinoviev, A complete Vinogradov 3-primes theorem
under the Riemann hypothesis, Electron. Res. Announc. Amer. Math. Soc. 3 (1997), 99-104.
[10] P. Dusart, In´egalit´es explicites pour ψ(X), θ(X), π(X) et les nombres premiers., C. R. Math.
Acad. Sci., Soc. R. Can., 21 (1999), 53-59.
[11] P. Dusart, Estimates of θ(x; k, l) for large values of x, Math. Comp. 71 (2002), no. 239, 1137-1168.
[12] P. Dusart, Estimates of some functions over primes without R. H., preprint. arXiv:1002.0442 .
[13] P. X. Gallagher, The large sieve, Mathematika, 14 (1967), 14-20.
[14] X. Gourdon, P. Demichel, The ﬁrst 1013 zeros of the Rie-
mann Zeta function, and zeros computation at very large height,
http://numbers.computation.free.fr/Constants/Miscellaneous/zetazeros1e13-1e24.pdf,
2004.
[15] B. Green, T. Tao, Restriction theory of the Selberg sieve, with applications, J. Th´eor. Nombres
Bordeaux 18 (2006), no. 1, 147-182.
[16] G. H. Hardy, J. E. Littlewood, Some problems of ‘Partitio numerorum’; III: On the expression of
a number as a sum of primes, Acta Math. 44 (1923), no. 1, 1-70.
[17] D. R. Heath-Brown, Zero-free regions for Dirichlet L-functions, and the least prime in an arith-
metic progression, Proc. London Math. Soc. (3) 64 (1992), no. 2, 265-338.
[18] H. Helfgott, Minor arcs for Goldbach’s problem, preprint.
[19] H. Iwaniec, E. Kowalski, Analytic number theory. American Mathematical Society Colloquium
Publications, 53. American Mathematical Society, Providence, RI, 2004.
[20] H. Kadiri, Short eﬀective intervals containing primes in arithmetic progressions and the seven
cubes problem, Math. Comp. 77 (2008), no. 263, 17331748.
[21] L. Kaniecki, On Snirelman’s constant under the Riemann hypothesis, Acta Arith. 72 (1995), no.
4, 361-374.
[22] A. F. Lavrik, On the twin prime hypothesis of the theory of primes by the method of I. M. Vino-
gradov, Soviet Math. Dokl., 1 (1960), 700-702.
[23] M. Liu, T. Wang, Distribution of zeros of Dirichlet L-functions and an explicit formula for ψ(t, χ),
Acta Arith. 102 (2002), no. 3, 261–293.
[24] M. Liu, T. Wang, On the Vinogradov bound in the three primes Goldbach conjecture, Acta Arith.
105 (2002), no. 2, 133-175.
[25] J. van de Lune, H. J. J. te Riele, D. T. Winter, On the zeros of the Riemann zeta function in the
critical strip. IV, Math. Comp. 46 (1986), no. 174, 667-681.
[26] J. E. van Lint, H. E. Richert, On primes in arithmetic progressions, Acta Arith., 11 (1965),
209-216.
[27] K. McCurley, Explicit estimates for the error term in the prime number theorem for arithmetic
progressions, Math. Comp. 42 (1984), no. 165, 265-285.
[28] H. L. Montgomery, A note on the large sieve, J. London Math. Soc. 43 (1968), 93-98.
[29] H. L. Montgomery, Topics in Multiplicative Number Theory. Lecture Notes in Mathematics
(Berlin), 227 (1971), 178pp.

EVERY ODD NUMBER GREATER THAN 1 IS THE SUM OF AT MOST FIVE PRIMES 45

[30] H. Montgomery, The analytic principle of the large sieve, Bull. Amer. Math. Soc. 84 (1978), no.
4, 547567.
[31] H. L. Montgomery, R. C. Vaughan, The large sieve, Mathematika 20 (1973), 119-134.
[32] T. Oliveira e Silva, http://www.ieeta.pt/∼tos/goldbach.html
[33] D. Platt, Computing degree 1 L-functions rigorously, Ph.D. Thesis, University of Bristol, 2011.
[34] D. Platt, Computing π(x) analytically, preprint.
[35] O. Ramar´e, On Snirel’man’s constant, Ann. Scu. Norm. Pisa 22 (1995), 645–706.
[36] O. Ramar´e, Eigenvalues in the large sieve inequality, Funct. Approximatio, Comment. Math., 37
(2007), 7-35.
[37] O. Ramar´e, On Bombieri’s asymptotic sieve, J. Number Theory 130 (2010), no. 5, 1155-1189.
[38] O. Ramar´e, I. M. Ruzsa, Additive properties of dense subsets of sifted sequences. J. Th´eorie N.
Bordeaux, 13 (2001), 559-581.
[39] O. Ramar´e, R. Rumely, Primes in arithmetic progressions, Math. Comp. 65 (1996), no. 213,
397-425.
[40] O. Ramar´e, Y. Saouter, Short eﬀective intervals containing primes, J. Number Theory 98 (2003),
no. 1, 10-33.
[41] J. Richstein, Verifying the Goldbach conjecture up to 4 × 1014, Mathematics of Computation 70
(2000), 1745–1749.
[42] J.B. Rosser, Explicit bounds for some functions of prime numbers, Amer. J. Math. 63 (1941)
211-232.
[43] J.B. Rosser, L. Schoenfeld, Approximate formulas for some functions of prime numbers, Ill. J.
Math. 6 (1962), 64–94.
[44] J.B. Rosser, L. Schoenfeld, Sharper bounds for the Chebyshev functions θ(x) and ψ(x), Collection
of articles dedicated to Derrick Henry Lehmer on the occasion of his seventieth birthday. Math.
Comp. 29 (1975), 243-269.
[45] H. Siebert, Montgomery’s weighted sieve for dimension two, Monatshefte f¨ur Mathematik 82
(1976), 327–336.
[46] R. C. Vaughan, Sommes trigonometriques sur les nombres premiers, C.R. Acad. Sci. Paris, Ser A.
(1977), 981-983.
[47] I. M. Vinogradov, Representation of an odd number as a sum of three primes, Comptes Rendus
(Doklady) de l’Academy des Sciences de l’USSR 15 (1937), 191–294.
[48] I. M. Vinogradov, The Method of Trigonometric Sums in Number Theory, Interscience Publ.
(London, 1954).
[49] D. R. Ward, Some series involving Euler’s function, London Math. Soc, 2 (1927), 210–214.
[50] S. Wedeniwski, ZetaGrid - Computational veriﬁcation of the Riemann Hypothesis, Conference in
Number Theory in Honour of Professor H.C. Williams, Banﬀ, Alberta, Canada, May 2003.

UCLA Department of Mathematics, Los Angeles, CA 90095-1596.

E-mail address: tao@math.ucla.edu
