<!-- source: https://arxiv.org/pdf/1312.7748 | converted from PDF -->

THE TERNARY GOLDBACH CONJECTURE IS TRUE

H. A. HELFGOTT

Abstract. The ternary Goldbach conjecture, or three-primes problem, as-
serts that every odd integer n greater than 5 is the sum of three primes. The
present paper proves this conjecture.
Both the ternary Goldbach conjecture and the binary, or strong, Goldbach
conjecture had their origin in an exchange of letters between Euler and Gold-
bach in 1742. We will follow an approach based on the circle method, the
large sieve and exponential sums. Some ideas coming from Hardy, Littlewood
and Vinogradov are reinterpreted from a modern perspective. While all work
here has to be explicit, the focus is on qualitative gains.
The improved estimates on exponential sums are proven in the author’s
papers on major and minor arcs for Goldbach’s problem. One of the highlights
of the present paper is an optimized large sieve for primes. Its ideas get
reapplied to the circle method to give an improved estimate for the minor-arc
integral.
 Contents

1. Introduction 2
1.1. Results 2
1.2. History 3
1.3. Main ideas 5
1.4. Dependency diagram 7
1.5. Acknowledgments 8
2. Preliminaries 8
2.1. Notation 8
2.2. Dirichlet characters and L functions 8
2.3. Fourier transforms 9
2.4. Mellin transforms 9
3. The integral over the major arcs 10
3.1. Decomposition of Sη(α, x) by characters 11
3.2. The integral over the major arcs: the main term 13
3.3. The ℓ2 norm over the major arcs 16
3.4. The integral over the major arcs: error terms. Conclusion 20
4. Optimizing and coordinating smoothing functions 22
4.1. The symmetric smoothing function η◦ 23
4.2. The smoothing function η∗: adapting minor-arc bounds 25
5. The ℓ2 norm and the large sieve 31
5.1. The ℓ2 norm over arcs: variations on the large sieve for primes 31
5.2. Bounding the quotient in the large sieve for primes 35
6. The integral over the minor arcs 46
6.1. Putting together ℓ2 bounds over arcs and ℓ∞ bounds 46
6.2. The minor-arc total 48
7. Conclusion 56
1arXiv:1312.7748v2  [math.NT]  17 Jan 2014
2 H. A. HELFGOTT

7.1. The ℓ2 norm over the major arcs: explicit version 56
7.2. The total major-arc contribution 58
7.3. The minor-arc total: explicit version 62
7.4. Conclusion: proof of main theorem 69
Appendix A. Sums over primes 71
Appendix B. Sums involving φ(q) 73
Appendix C. Checking small n by checking zeros of ζ(s) 76
References 77

1. Introduction

1.1. Results. The ternary Goldbach conjecture (or three-prime problem) states
that every odd number n greater than 5 can be written as the sum of three
primes. Both the ternary Goldbach conjecture and the (stronger) binary Gold-
bach conjecture (stating that every even number greater than 2 can be written
as the sum of two primes) have their origin in the correspondence between Euler
and Goldbach (1742). See [Dic66, Ch. XVIII] for the early history of the problem.
I. M. Vinogradov [Vin37] showed in 1937 that the ternary Goldbach conjecture
is true for all n above a large constant C. Unfortunately, while the value of
C has been improved several times since then, it has always remained much
too large (C = e3100, [LW02]) for a mechanical veriﬁcation up to C to be even
remotely feasible. The situation was paradoxical: the conjecture was known
above an explicit C, but, even after seventy years of improvements, this C was
so large that it could not be said that the problem could be attacked by any
conceivable computational means within our physical universe. (The number of
picoseconds since the beginning of the universe is less than 1030, whereas the
number of protons in the observable universe is currently estimated at ∼ 1080

[Shu92], thereby making even parallel computers somewhat limited.) Thus, the
only way forward was a series of drastic improvements in the mathematical, rather
than computational, side.
The present paper proves the ternary Goldbach conjecture.

Main Theorem. Every odd integer n greater than 5 can be expressed as the sum
of three primes.

The proof given here works for all n ≥ C = 1027. (It is typical of analytic
proofs to work for all n larger than a constant; see §1.2.1.) Verifying the main
theorem for n < 1027 is really a minor computational task; it was already done
for all n ≤ 8.875 · 1030 in [HP]. (Appendix C provides an alternative approach.)
This ﬁnishes the proof of the main theorem for all n.
We are able to set major arcs to be few and narrow because the minor-arc
estimates in [Helb] are very strong; we are forced to take them to be few and
narrow because of the kind of L-function bounds we will rely upon. (“Major
arcs” are small intervals around rationals of small denominator; “minor arcs” are
everything else. See the deﬁnitions at the beginning of §1.3.)
As has been the case since Hardy and Littlewood [HL23], the approach is
based on Fourier analysis, and, more particularly, on a study of exponential sums∑
p e(αp)η(p/x), where η is a weight of our choice (a “smoothing function”, or
simply a “smoothing”). Such exponential sums are estimated in [Hela] and [Helb]

THE TERNARY GOLDBACH CONJECTURE IS TRUE 3

for α lying in the major and minor arcs, respectively. Here we will focus on the
eﬃcient use of such estimates to solve the main problem.
One of the main lessons of the proof – also present in [Helb] – is the close
relation between the circle method and the large sieve; rather than see large-sieve
methods as a black box, we will use them as a source for ideas. This applies,
in particular, to the ideas behind an improved large sieve for primes, which we
derive here following and completing Ramar´e’s ideas on the subject [Ram09].
Another guiding thought is really a relativization of a common dictum (“al-
ways smooth”). Smoothing is more useful for some tasks than for others, and
diﬀerent kinds of smoothing functions may be appropriate for diﬀerent parts of
one problem. The main results in [Hela] and [Helb] are stated in terms of diﬀer-
ent smoothing functions. Here, we will see how to coordinate the use of diﬀerent
smoothings. We will also discuss how to choose smoothings so as to make the
main term as large as possible with respect to the error term. (The emphasis
elsewhere is, of course, on giving upper bounds for the error term that are as
small as possible.)

1.2. History. The following brief remarks are here to provide some background;
no claim to completeness is made. Results on exponential sums over the primes
are discussed more speciﬁcally in [Helb, §1].

1.2.1. Results towards the ternary Goldbach conjecture. Hardy and Littlewood
[HL23] proved that every odd number larger than a constant C is the sum of three
primes, conditionally on the generalized Riemann Hypothesis. This showed, as
they said, that the problem was not unangreifbar (as it had been called by Landau
in [Lan12]).
Vinogradov [Vin37] made the result unconditional. An explicit value for C
(namely, C = 3315) was ﬁrst found by Borodzin in 1939. This value was improved
to C = 3.33 · 1043000 by J.-R. Chen and T. Z. Wang [CW89] and to C = 2 · 101346

by M.-Ch. Liu and T. Wang [LW02]. (J.-R. Chen had also proven that every
large enough even number is either the sum of two primes or the sum p1 + p2p3
of a prime p1 and the product p2p3 of two primes.)
There is a good reason why analytic proofs generally establish a result only for
integers n larger than a constant C. An analytic proof, such as the one in this
paper, gives not only the existence of a way to express a number n in a certain
form (say, as the sum of three primes), but also an estimate on the (weighted)
number of ways to do so. Such an estimate is of the form

main term + error term,

where the main term is a precise function f (n) and the error term is shown
to be bounded from above by a function g(n); the proof works if g(n) < f (n)
asymptotically as n → ∞. Of course, this means that such a proof works only
once g(n) ≤ f (n), that is, once n is greater than some constant C, thus leaving
small n to be veriﬁed by direct computation.
In [DEtRZ97], the ternary Goldbach conjecture was proven for all n condition-
ally on the generalized Riemann hypothesis. There, as here, the theorem was
proven analytically for all n larger than a moderate constant C, and then the
task was completed by a numerical check for all odd n < C.

4 H. A. HELFGOTT

1.2.2. Checking Goldbach for small n. Numerical veriﬁcations of the binary Gold-
bach conjecture for small n were published already in the late nineteenth cen-
tury; see [Dic66, Ch. XVIII]. Richstein [Ric01] showed that every even integer
4 ≤ n ≤ 4 · 1014 is the sum of two primes. Oliveira e Silva, Herzog and Pardi
[OeSHP13] have proven that every even integer 4 ≤ n ≤ 4 · 1018 is the sum of two
primes.
Clearly, if one can show that every interval of length ≥ 4 · 1018 − 4 within
[1, N ] contains a prime, then [OeSHP13] implies that every odd number between
7 and N can be written as the sum of three primes: we let p be the largest prime
≤ N − 4, and observe that p − N is an even number ≤ 4 · 1018, and thus can be
written as the sum of two primes.
Appendix C proves that every interval of length ≥ 4 · 1018 − 4 within [1, N ]
contains a prime for N = 1.23 · 1027 using a rigourous veriﬁcation [Plaa] of the
fact that the ﬁrst 1.1 · 1011 zeros of the Riemann zeta function lie on the critical
line. Alternatively, one can simply construct a sequence of primes up to N such
that any two consecutive primes in the list diﬀer by at most 4 · 1018 − 4. This
was done in [HP] for N = 8.875694 · 1030; thus, the ternary Goldbach conjecture
has been veriﬁed up to that value of N .
The task of constructing the sequence of primes up to 1027 – enough to complete
the proof of the main theorem – takes only about 25 hours on a single processor
core on a modern computer (or ﬁve hours on ﬁve cores, since the algorithm is
trivially parallelizable), provided that [OeSHP13] is taken as a given. In other
words, verifying the theorem up to the point where the analytic proof in the
present paper starts working is a small, easily replicable task well within home-
computing range.

1.2.3. Work on Schnirelman’s constant. “Schnirelman’s constant” is a term for
the smallest k such that every integer n > 1 is the sum of at most k primes.
(Thus, Goldbach’s binary and ternary conjecture, taken together, are equivalent
to the statement that Schnirelman’s constant is 3.) In 1930, Schnirelman [Sch33]
showed that Schnirelman’s constant k is ﬁnite, developing in the process some of
the bases of what is now called additive or arithmetic combinatorics.
In 1969, Klimov proved that k ≤ 6 · 109; he later improved this result to
k ≤ 115 [KPˇS72] (with G. Z. Piltay and T. A. Sheptiskaya) and k ≤ 55. Results
by Vaughan [Vau77] (k = 27), Deshouillers [Des77] (k = 26) and Riesel-Vaughan
[RV83] (k = 19) then followed.
Ramar´e showed in 1995 that every even n > 1 is the sum of at most 6 primes
[Ram95]. Recently, Tao [Tao] established that every odd number n > 1 is the
sum of at most 5 primes. These results imply that k ≤ 6 and k ≤ 5, respectively.
The present paper implies that k ≤ 4.

Corollary 1.1 (to Main Theorem). Every integer n > 1 is the sum of at most 4
primes.

Proof. If n is odd and > 5, the main theorem applies. If n is even and > 8, apply
the main theorem to n − 3. Do the cases n ≤ 8 separately. □

1.2.4. Other approaches. Since [HL23] and [Vin37], the main line of attack on
the problem has gone through exponential sums. There are proofs based on
cancellation in other kinds of sums ([HB85], [IK04, §19]), but they have not
been made to yield practical estimates. The same goes for proofs based on other
principles, such as that of Schnirelman’s result or the recent work of X. Shao

THE TERNARY GOLDBACH CONJECTURE IS TRUE 5

[Sha]. (It deserves to be underlined that [Sha] establishes Vinogradov’s three-
prime result without using L-function estimates at all; its constant C is, however,
extremely large.)

1.3. Main ideas. We will limit the discussion here to the general setup and to
the use of exponential-sum estimates. The derivation of new exponential-sum
estimates is the subject of [Helb] and [Hela].
In the circle method, the number of representations of a number N as the
sum of three primes is represented as an integral over the “circle” R/Z, which is
partitioned into major arcs M and minor arcs m = (R/Z) \ M:

(1.1)
 ∑

n1+n2+n3=NΛ(n1)Λ(n2)Λ(n3) = ∫

R/Z(S(α, x))
3e(−N α)dα

= ∫

M(S(α, x))
3e(−N α)dα + ∫

m(S(α, x))
3e(−N α)dα,

where S(α, x) = ∑n≤x Λ(n)e(αn), e(t) = e2πit and Λ is the von Mangoldt func-
tion (Λ(n) = log p if n = pα, α ≥ 1, and Λ(n) = 0 if n is not a power of a prime).
The aim is to show that the sum of the integral over M and the integral over m
is positive; this will prove the three-primes theorem.
The major arcs M = Mr0 consist of intervals (a/q − cr0/qx, a/q + cr0/qx)
around the rationals a/q, q ≤ r0, where c is a constant. In previous work
1, r0
grew with x; in our setup, r0 is a constant. Smoothing changes the left side of
(1.1) into a weighted sum, but, since we aim at an existence result rather than
at an asymptotic for the number of representations p1 + p2 + p3 of N , this is
obviously acceptable.
Typically, work on major arcs yields rather precise estimates on the integral
over ∫

M in (1.1), whereas work on minor arcs gives upper bounds on the absolute
value of the integral over ∫
m in (1.1).

1.3.1. Using major arc bounds. We will be working with smoothed sums

(1.2) Sη(α, x) =
 ∞∑

n=1 Λ(n)χ(n)e(δn/x)η(n/x).

Our integral will actually be of the form

(1.3) ∫

M Sη+(α, x)
2Sη∗(α, x)e(−N α)dα,

where η+ and η∗ are two diﬀerent smoothing functions.
Estimating the sums (1.2) on M reduces to estimating the sums

(1.4) Sη(δ/x, x) =
 ∞∑

n=1 Λ(n)χ(n)e(δn/x)η(n/x)

for χ varying among all Dirichlet characters modulo q ≤ r0 and for |δ| ≤ cr0/q,
i.e., |δ| small. The estimation of (1.4) for such χ and δ is the subject of [Hela].
(It is in [Hela], and not elsewhere, that the major L-function computation in
[Plab] gets used; it allows to give good estimates on sums such as (1.4).)

1Ramar´e’s work [Ram10] is in principle strong enough to allow r0 to be an unspeciﬁed large
constant. Tao’s work [Tao] reaches this standard only for x of moderate size.

6 H. A. HELFGOTT

The results in [Hela] allow us to use any smoothing based on the Gaussian
η♥(t) = e−t2/2; this leaves us some freedom in choosing η+ and η∗. The main
term in our estimate for (1.3) is of the form

(1.5) C0
 ∫ ∞

0
 ∫ ∞

0 η+(t1)η+(t2)η∗
 ( N
x − (t1 + t2)
) dt1dt2,

where C0 is a constant. Our upper bound for the minor-arc integral, on the
other hand, will be proportional to |η+|2
2|η∗|1. (Here, as is usual, we write |f |p
for the ℓp norm of a function f .) The question is then how to make (1.5) divided
by |η+|2
2|η∗|1 as large as possible. A little thought will show that it is best for
η+ to be symmetric, or nearly symmetric, around t = 1 (say), and for η∗ be
concentrated on a much shorter interval than η+, while x is set to be x/2 or
slightly less.
It is easy to construct a function of the form t ↦→ h(t)η♥(t) symmetric around
t = 1, with support on [0, 2]. We will deﬁne η+(t) = hH (t)η♥(t), where hH is an
approximation to h that is band-limited in the Mellin sense. This will mean that
we will be able to use the estimates in [Hela].
How to choose η∗? The bounds in [Helb] were derived for η2 = (2I[1/2,1]) ∗M
(2I[1/2,1]), which is nice to deal with in the context of combinatorially ﬂavored
analytic number theory, but it has a Mellin transform that decays much too
slowly.
2 The solution is to use a smoothing that is, so to speak, Janus-faced,
viz., η∗ = (η2 ∗M φ)(κt), where φ(t) = t2e−t2/2 and κ is a large constant. We
estimate sums of type Sη(α, x) by estimating Sη2(α, x) if α lies on a minor arc,
or by estimating Sφ(α, x) if α lies on a major arc. (The Mellin transform of φ is
just a shift of that of η♥.) This is possible because η2 has support bounded away
from zero, while φ is also concentrated away from 0.
Now that the smoothing functions have been chosen, it remains to actually
estimate (1.3) using the results from [Hela], which are estimates on (1.4) (and
hence on (1.2)) for individual α. Doing so well is a delicate task. Some of the
main features are the use of cancellation to prove a rather precise estimate for
the ℓ2 norm over the major arcs, and the arrangement of error terms so that they
are multiplied by the said ℓ2 norm. (The norm will appear again later, in that it
will be substracted from the integral over a union of somewhat larger arcs, as in
(1.7).) We will actually start by ﬁnding the main term, namely, (3.23); it is what
one would expect, but extracting it at the cost of only a small error term will
require some careful use of a smoothing η+ approximated by other smoothing
η◦. (The main term is obtained by completing several sums and integrals, whose
terms must be shown to decrease rapidly.)

1.3.2. Minor arc bounds: exponential sums and the large sieve. Let mr be the
complement of Mr. In particular, m = mr0 is the complement of M = Mr0. Expo-
nential sum-estimates, such as those in [Helb], give bounds on maxα∈mr |S(α, x)|
that decrease with r.

2This parallels the situation in the transition from Hardy and Littlewood [HL23] to Vino-
gradov [Vin37]. Hardy and Littlewood used the smoothing η(t) = e−t, whereas Vinogradov
used the brusque (non-)smoothing η(t) = I[0,1]. Arguably, this is not just a case of technological
decay; I[0,1] has compact support and is otherwise easy to deal with in the minor-arc regime.

THE TERNARY GOLDBACH CONJECTURE IS TRUE 7

We need to do better than

(1.6)
 ∫

m
 ∣
∣S(α, x)
3e(−N α)
∣
∣ dα ≤ (max
α∈m |S(α, x)|∞) · ∫

m |S(α, x)|
2dα

≤ (max
α∈m |S(α, x)|∞) · (|S|
2
2 − ∫

M |S(α, x)|2dα) ,

as this inequality involves a loss of a factor of log x (because |S|2
2 ∼ x log x).
Fortunately, minor arc estimates are valid not just for a ﬁxed r0, but for the
complement of Mr, where r can vary within a broad range. By partial summation,
these estimates can be combined with upper bounds for

(1.7) ∫

Mr |S(α, x)|
2dα − ∫

Mr0 |S(α, x)|2dα.

Giving an estimate for the integral over Mr0 (r0 a constant) will be part of our
task over the major arcs. The question is how to give an upper bound for the
integral over Mr that is valid and non-trivial over a broad range of r.
The answer lies in the deep relation between the circle method and the large
sieve. (This was obviously not available to Vinogradov in 1937; the large sieve
is a slightly later development (Linnik [Lin41], 1941) that was optimized and
fully understood later still.) A large sieve is, in essence, an inequality giving a
discretized version of Plancherel’s identity. Large sieves for primes show that the
inequality can be sharpened for sequences of prime support, provided that, on
the Fourier side, the sum over frequencies is shortened. The idea here is that
this kind of improvement can be adapted back to the continuous context, so as
to give upper bounds on the L2 norms of exponential sums with prime support
when α is restricted to special subsets of the circle. Such an L2 norm is nothing
other than ∫
Mr |S(α, x)|2dα.
The ﬁrst version of [Helb] used an idea of Heath-Brown’s3 that can indeed be
understood in this framework. In §5.1, we shall prove a better bound, based on a
large sieve for primes due to Ramar´e [Ram09]. We will re-derive this sieve using
an idea of Selberg’s. We will then make it fully explicit in the crucial range (5.2).
(This, incidentally, also gives fully explicit estimates for Ramar´e’s large sieve in
its original discrete context, making it the best large sieve for primes in a wide
range.)
The outcome is that ∫
Mr |S(α, x)|2dα is bounded roughly by 2x log r, rather
than by x log x (or by 2eγx log r, as was the case when Heath-Brown’s idea was
used). The lack of a factor of log x makes it possible to work with r0 equal to a
constant, as we have done; the factor of eγ reduces the need for computations by
more than an order of magnitude.

1.4. Dependency diagram. As usual, if two sections on the diagram are con-
nected by a line, the upper one depends on the lower one. We use only the main
results in [Hela] and [Helb], namely, [Hela, Main Thm.] and the statements in
[Helb, §1.1]; these are labelled “majarcs” and “minarcs”, respectively.

3Communicated by Heath-Brown to the author, and by the author to Tao, as acknowledged
in [Tao]. The idea is based on a lemma by Montgomery (as in, e.g., [IK04, Lemma 7.15]).

8 H. A. HELFGOTT

 7

3 4 5

 6

majarcs  minarcs

1.5. Acknowledgments. The author is very thankful to O. Ramar´e for his help
and feedback, especially regarding §5 and Appendix B. He is also much indebted
to A. Booker, B. Green, H. Kadiri, D. Platt, T. Tao and M. Watkins for many
discussions on Goldbach’s problem and related issues. Thanks are also due to B.
Bukh, A. Granville and P. Sarnak for their valuable advice.
Travel and other expenses were funded in part by the Adams Prize and the
Philip Leverhulme Prize. The author’s work on the problem started at the Univer-
sit´e de Montr´eal (CRM) in 2006; he is grateful to both the Universit´e de Montr´eal
and the ´Ecole Normale Sup´erieure for providing pleasant working environments.
The present work would most likely not have been possible without free and
publicly available software: PARI, Maxima, Gnuplot, VNODE-LP, PROFIL /
BIAS, SAGE, and, of course, LATEX, Emacs, the gcc compiler and GNU/Linux in
general. Some exploratory work was done in SAGE and Mathematica. Rigorous
calculations used either D. Platt’s interval-arithmetic package (based in part on
Crlibm) or the PROFIL/BIAS interval arithmetic package underlying VNODE-
LP.
 2. Preliminaries

2.1. Notation. As is usual, we write µ for the Moebius function, Λ for the von
Mangoldt function. We let τ (n) be the number of divisors of an integer n and
ω(n) the number of prime divisors. For p prime, n a non-zero integer, we deﬁne
vp(n) to be the largest non-negative integer α such that pα|n.
We write (a, b) for the greatest common divisor of a and b. If there is any risk
of confusion with the pair (a, b), we write gcd(a, b). Denote by (a, b∞) the divisor
∏p|b pvp(a) of a. (Thus, a/(a, b∞) is coprime to b, and is in fact the maximal
divisor of a with this property.)
As is customary, we write e(x) for e2πix. We write |f |r for the Lr norm of a
function f .
We write O∗(R) to mean a quantity at most R in absolute value.

2.2. Dirichlet characters and L functions. A Dirichlet character χ : Z → C
of modulus q is a character χ of (Z/qZ)∗ lifted to Z with the convention that
χ(n) = 0 when (n, q) ̸= 1. Again by convention, there is a Dirichlet character of
modulus q = 1, namely, the trivial character χT : Z → C deﬁned by χT (n) = 1
for every n ∈ Z.
If χ is a character modulo q and χ′ is a character modulo q′|q such that χ(n) =
χ′(n) for all n coprime to q, we say that χ′ induces χ. A character is primitive if

THE TERNARY GOLDBACH CONJECTURE IS TRUE 9

it is not induced by any character of smaller modulus. Given a character χ, we
write χ∗ for the (uniquely deﬁned) primitive character inducing χ. If a character
χ mod q is induced by the trivial character χT , we say that χ is principal and
write χ0 for χ (provided the modulus q is clear from the context). In other words,
χ0(n) = 1 when (n, q) = 1 and χ0(n) = 0 when (n, q) = 0.
A Dirichlet L-function L(s, χ) (χ a Dirichlet character) is deﬁned as the ana-
lytic continuation of ∑
n χ(n)n−s to the entire complex plane; there is a pole at
s = 1 if χ is principal.
A non-trivial zero of L(s, χ) is any s ∈ C such that L(s, χ) = 0 and 0 < ℜ(s) <
1. (In particular, a zero at s = 0 is called “trivial”, even though its contribution
can be a little tricky to work out. The same would go for the other zeros with
ℜ(s) = 0 occuring for χ non-primitive, though we will avoid this issue by working
mainly with χ primitive.) The zeros that occur at (some) negative integers are
called trivial zeros.
The critical line is the line ℜ(s) = 1/2 in the complex plane. Thus, the gen-
eralized Riemann hypothesis for Dirichlet L-functions reads: for every Dirichlet
character χ, all non-trivial zeros of L(s, χ) lie on the critical line. Veriﬁable ﬁnite
versions of the generalized Riemann hypothesis generally read: for every Dirichlet
character χ of modulus q ≤ Q, all non-trivial zeros of L(s, χ) with |ℑ(s)| ≤ f (q)
lie on the critical line (where f : Z → R+ is some given function).

2.3. Fourier transforms. The Fourier transform on R is normalized as follows:

̂f (t) = ∫ ∞

−∞ e(−xt)f (x)dx

for f : R → C.
The trivial bound is | ̂f |∞ ≤ |f |1. Integration by parts gives that, if f is
diﬀerentiable k times outside ﬁnitely many points, then

(2.1) ̂f (t) = O∗ ( | ̂f (k)|∞
2πt
 )
 = O∗ ( |f (k)|1
(2πt)k
 )
 .

It could happen that |f (k)|1 = ∞, in which case (2.1) is trivial (but not false).
In practice, we require f (k) ∈ L1. In a typical situation, f is diﬀerentiable k
times except at x1, x2, . . . , xk, where it is diﬀerentiable only (k − 2) times; the
contribution of xi (say) to |f (k)|1 is then | limx→x+
i f (k−1)(x)−limx→x−
i f (k−1)(x)|.

2.4. Mellin transforms. The Mellin transform of a function φ : (0, ∞) → C is

(2.2) M φ(s) := ∫ ∞

0 φ(x)xs−1dx.

In general, M (f ∗M g) = M f · M g and

(2.3) M (f · g)(s) = 1
2πi
 ∫ σ+i∞

σ−i∞ M f (z)M g(s − z)dz [GR00, §17.32]

provided that z and s−z are within the strips on which M f and M g (respectively)
are well-deﬁned.
The Mellin transform is an isometry, in the sense that

(2.4) ∫ ∞

0 |f (t)|
2t2σ dt
t = 1
2π
 ∫ ∞

−∞ |M f (σ + it)|
2dt.

10 H. A. HELFGOTT

provided that σ + iR is within the strip on which M f is deﬁned. We also know
that, for general f ,

(2.5) M (tf ′(t))(s) = −s · M f (s),

M ((log t)f (t))(s) = (M f )
′(s)

(as in, e.g., [BBO10, Table 1.11]).
Since (see, e.g., [BBO10, Table 11.3] or [GR00, §16.43])

(M I[a,b])(s) = bs − as

s ,

we see that

(2.6) M η2(s) = ( 1 − 2−s

s
 )2 , M η4(s) = ( 1 − 2−s

s
 )4 .

Let fz = e−zt, where ℜ(z) > 0. Then

(M f )(s) = ∫ ∞

0 e−ztt
s−1dt = 1
zs
 ∫ ∞

0 e
−tdt

= 1
zs
 ∫ z∞

0 e−uu
s−1du = 1
zs
 ∫ ∞

0 e−tt
s−1dt = Γ(s)
zs ,

where the next-to-last step holds by contour integration, and the last step holds
by the deﬁnition of the Gamma function Γ(s).

3. The integral over the major arcs

Let

(3.1) Sη(α, x) = ∑

n Λ(n)e(αn)η(n/x),

where α ∈ R/Z, Λ is the von Mangoldt function and η : R → C is of fast enough
decay for the sum to converge.
Our ultimate goal is to bound from below

(3.2) ∑

n1+n2+n3=N Λ(n1)Λ(n2)Λ(n3)η1(n1/x)η2(n2/x)η3(n3/x),

where η1, η2, η3 : R → C. As can be readily seen, (3.2) equals

(3.3) ∫

R/Z Sη1(α, x)Sη2(α, x)Sη3(α, x)e(−N α)dα.

In the circle method, the set R/Z gets partitioned into the set of major arcs
M and the set of minor arcs m; the contribution of each of the two sets to the
integral (3.3) is evaluated separately.
Our object here is to treat the major arcs: we wish to estimate

(3.4) ∫

M Sη1(α, x)Sη2(α, x)Sη3(α, x)e(−N α)dα

for M = Mδ0,r, where
(3.5)

Mδ0,r = ⋃

q≤r
q odd
 ⋃

a mod q
(a,q)=1
 ( a
q − δ0r
2qx , a
q + δ0r
2qx
 ) ∪ ⋃

q≤2r
q even
 ⋃

a mod q
(a,q)=1
 ( a
q − δ0r
qx , a
q + δ0r
qx
 )

and δ0 > 0, r ≥ 1 are given.

THE TERNARY GOLDBACH CONJECTURE IS TRUE 11

In other words, our major arcs will be few (that is, a constant number) and
narrow. While [LW02] used relatively narrow major arcs as well, their number,
as in all previous proofs of Vinogradov’s result, is not bounded by a constant.
(In his proof of the ﬁve-primes theorem, [Tao] is able to take a single major arc
around 0; this is not possible here.)
What we are about to see is the general framework of the major arcs. This is
naturally the place where the overlap with the existing literature is largest. Two
important diﬀerences can nevertheless be singled out.

• The most obvious one is the presence of smoothing. At this point, it im-
proves and simpliﬁes error terms, but it also means that we will later need
estimates for exponential sums on major arcs, and not just at the middle
of each major arc. (If there is smoothing, we cannot use summation by
parts to reduce the problem of estimating sums to a problem of counting
primes in arithmetic progressions, or weighted by characters.)
• Since our L-function estimates for exponential sums will give bounds that
are better than the trivial one by only a constant – even if it is a rather
large constant – we need to be especially careful when estimating error
terms, ﬁnding cancellation when possible.

3.1. Decomposition of Sη(α, x) by characters. What follows is largely clas-
sical; compare to [HL23] or, say, [Dav67, §26]. The only diﬀerence from the
literature lies in the treatment of n non-coprime to q, and the way in which we
show that our exponential sum (3.8) is equal to a linear combination of twisted
sums Sη,χ∗ over primitive characters χ∗. (Non-primitive characters would give us
L-functions with some zeroes inconveniently placed on the line ℜ(s) = 0.)
Write τ (χ, b) for the Gauss sum

(3.6) τ (χ, b) = ∑

a mod q χ(a)e(ab/q)

associated to a b ∈ Z/qZ and a Dirichlet character χ with modulus q. We let
τ (χ) = τ (χ, 1). If (b, q) = 1, then τ (χ, b) = χ(b−1)τ (χ).
Recall that χ∗ denotes the primitive character inducing a given Dirichlet char-
acter χ. Writing ∑
χ mod q for a sum over all characters χ of (Z/qZ)∗), we see
that, for any a0 ∈ Z/qZ,
(3.7) 1
φ(q)
 ∑

χ mod q τ (χ, b)χ∗(a0) = 1
φ(q)
 ∑

χ mod q
 ∑

a mod q
(a,q)=1
 χ(a)e(ab/q)χ
∗(a0)

= ∑

a mod q
(a,q)=1
 e(ab/q)
φ(q)
 ∑

χ mod q χ
∗(a−1a0) = ∑

a mod q
(a,q)=1
 e(ab/q)
φ(q)
 ∑

χ mod q′ χ(a
−1a0),

12 H. A. HELFGOTT

where q′ = q/ gcd(q, a∞
0 ). Now, ∑
χ mod q′ χ(a−1a0) = 0 unless a = a0 (in which
case ∑χ mod q′ χ(a−1a0) = φ(q′)). Thus, (3.7) equals

φ(q′)
φ(q)
 ∑

a mod q
(a,q)=1
a≡a0 mod q′
 e(ab/q) = φ(q′)
φ(q)
 ∑

k mod q/q′

(k,q/q′)=1
 e ( (a0 + kq′)b
q
 )

= φ(q′)
φ(q) e ( a0b
q
 ) ∑

k mod q/q′

(k,q/q′)=1
 e ( kb
q/q′
 ) = φ(q′)
φ(q) e ( a0b
q
 ) µ(q/q′)

provided that (b, q) = 1. (We are evaluating a Ramanujan sum in the last step.)
Hence, for α = a/q + δ/x, q ≤ x, (a, q) = 1,

1
φ(q)
 ∑

χ τ (χ, a) ∑

n χ
∗(n)Λ(n)e(δn/x)η(n/x)

equals ∑

n
 µ((q, n∞))
φ((q, n∞)) Λ(n)e(αn)η(n/x).

Since (a, q) = 1, τ (χ, a) = χ(a)τ (χ). The factor µ((q, n∞))/φ((q, n∞)) equals 1
when (n, q) = 1; the absolute value of the factor is at most 1 for every n. Clearly
∑

n
(n,q)̸=1
 Λ(n)η ( n
x
 ) = ∑

p|q log p ∑

α≥1 η ( pα

x
 ) .

Recalling the deﬁnition (3.1) of Sη(α, x), we conclude that

(3.8)

Sη(α, x) = 1
φ(q)
 ∑

χ mod q χ(a)τ (χ)Sη,χ∗ ( δ
x , x
) + O∗
 

2 ∑

p|q log p ∑

α≥1 η ( pα

x
 )


 ,

where

(3.9) Sη,χ(β, x) = ∑

n Λ(n)χ(n)e(βn)η(n/x).

Hence Sη1(α, x)Sη2(α, x)Sη3(α, x)e(−N α) equals

(3.10)
 1
φ(q)3 ∑

χ1
 ∑

χ2
 ∑

χ3 τ (χ1)τ (χ2)τ (χ3)χ1(a)χ2(a)χ3(a)e(−N a/q)

· Sη1,χ∗
1 (δ/x, x)Sη2,χ∗
2 (δ/x, x)Sη3,χ∗
3 (δ/x, x)e(−δN/x)

plus an error term of absolute value at most

(3.11) 2
 3∑

j=1
 ∏

j′̸=j |Sηj′ (α, x)| ∑

p|q log p ∑

α≥1 ηj
 ( pα

x
 ) .

We will later see that the integral of (3.11) over S1 is negligible – for our choices
of ηj, it will, in fact, be of size O(x(log x)A), A a constant. (In (3.10), we have
reduced our problems to estimating Sη,χ(δ/x, x) for χ primitive; a more obvious
way of reaching the same goal would have made (3.11) worse by a factor of about

THE TERNARY GOLDBACH CONJECTURE IS TRUE 13

√q. The error term O(x(log x)A) should be compared to the main term, which
will be of size about a constant times x2.)

3.2. The integral over the major arcs: the main term. We are to estimate
the integral (3.4), where the major arcs Mδ0,r are deﬁned as in (3.5). We will use
η1 = η2 = η+, η3(t) = η∗(κt), where η+ and η∗ will be set later.
We can write

(3.12) Sη,χ(δ/x, x) = Sη(δ/x, x) = ∫ ∞

0 η(t/x)e(δt/x)dt + O∗(errη,χ(δ, x)) · x

= ̂η(−δ) · x + O∗(errη,χT (δ, x)) · x

for χ = χT the trivial character, and

(3.13) Sη,χ(δ/x) = O∗(errη,χ(δ, x)) · x

for χ primitive and non-trivial. The estimation of the error terms err will come
later; let us focus on (a) obtaining the contribution of the main term, (b) using
estimates on the error terms eﬃciently.
The main term: three principal characters. The main contribution will be
given by the term in (3.10) with χ1 = χ2 = χ3 = χ0, where χ0 is the principal
character mod q.
The sum τ (χ0, n) is a Ramanujan sum; as is well-known (see, e.g., [IK04,
(3.2)]),

(3.14) τ (χ0, n) = ∑

d|(q,n) µ(q/d)d.

This simpliﬁes to µ(q/(q, n))φ((q, n)) for q square-free. The special case n = 1
gives us that τ (χ0) = µ(q).
Thus, the term in (3.10) with χ1 = χ2 = χ3 = χ0 equals

(3.15) e(−N a/q)
φ(q)3 µ(q)
3Sη+,χ∗
0 (δ/x, x)
2Sη∗,χ∗
0 (δ/x, x)e(−δN/x),

where, of course, Sη,χ∗
0 (α, x) = Sη(α, x) (since χ∗
0 is the trivial character). Sum-
ming (3.15) for α = a/q + δ/x and a going over all residues mod q coprime to q,
we obtain

µ ( q
(q,N ) ) φ((q, N ))

φ(q)3 µ(q)
3Sη+,χ∗
0 (δ/x, x)
2Sη∗,χ∗
0 (δ/x, x)e(−δN/x).

The integral of (3.15) over all of M = Mδ0,r (see (3.5)) thus equals
(3.16) ∑

q≤r
q odd
 φ((q, N ))
φ(q)3 µ(q)
2µ((q, N )) ∫ δ0r
2qx

− δ0r
2qx S2
η+,χ∗
0 (α, x)Sη∗,χ∗
0 (α, x)e(−αN )dα

+ ∑

q≤2r
q even
 φ((q, N ))
φ(q)3 µ(q)2µ((q, N )) ∫ δ0r
qx

− δ0r
qx S2
η+,χ∗
0 (α, x)Sη∗,χ∗
0 (α, x)e(−αN )dα.

14 H. A. HELFGOTT

The main term in (3.16) is
(3.17)

x3 · ∑

q≤r
q odd
 φ((q, N ))
φ(q)3 µ(q)
2µ((q, N )) ∫ δ0r
2qx

− δ0r
2qx (̂η+(−αx))
2 ̂η∗(−αx)e(−αN )dα

+x3 · ∑

q≤2r
q even
 φ((q, N ))
φ(q)3 µ(q)2µ((q, N )) ∫ δ0r
qx

− δ0r
qx (̂η+(−αx))
2 ̂η∗(−αx)e(−αN )dα.

We would like to complete both the sum and the integral. Before, we should
say that we will want to be able to use smoothing functions η+ whose Fourier
transforms are not easy to deal with directly. All we want to require is that there
be a smoothing function η◦, easier to deal with, such that η◦ be close to η+ in ℓ2
norm.
Assume, then, that
 |η+ − η◦|2 ≤ ϵ0|η◦|,

where η◦ is thrice diﬀerentiable outside ﬁnitely many points and satisﬁes η(3)
◦ ∈
L1. Then (3.17) equals
(3.18)
x
3 · ∑

q≤r
q odd
 φ((q, N ))
φ(q)3 µ(q)
2µ((q, N )) ∫ δ0r
2qx

− δ0r
2qx ( ̂η◦(−αx))
2 ̂η∗(−αx)e(−αN )dα

+x3 · ∑

q≤2r
q even
 φ((q, N ))
φ(q)3 µ(q)2µ((q, N )) ∫ δ0r
qx

− δ0r
qx ( ̂η◦(−αx))
2 ̂η∗(−αx)e(−αN )dα.

plus

(3.19) O∗ (
x2 · ∑

q
 µ(q)2

φ(q)2
 ∫ ∞

−∞ |(̂η+(−α))
2 − ( ̂η◦(−α))
2|| ̂η∗(−α)|dα
)
 .

Here (3.19) is bounded by 2.82643x2 (by (B.4)) times

| ̂η∗(−α)|∞ ·
 √∫ ∞

−∞ |̂η+(−α) − ̂η◦(−α)|2dα · ∫ ∞

−∞ |̂η+(−α) + ̂η◦(−α)|2dα

≤ |η∗|1 · |̂η+ − ̂η◦|2|̂η+ + ̂η◦|2 = |η∗|1 · |η+ − η◦|2|η+ + η◦|2

≤ |η∗|1 · |η+ − η◦|2(2|η◦|2 + |η+ − η◦|2) = |η∗|1|η◦|
2
2 · (2 + ϵ0)ϵ0.

THE TERNARY GOLDBACH CONJECTURE IS TRUE 15

Now, (3.18) equals
(3.20)

x3 ∫ ∞

−∞( ̂η◦(−αx))
2 ̂η∗(−αx)e(−αN ) ∑

q
(q,2) ≤min( δ0r
2|α|x ,r)

µ(q)2=1
 φ((q, N ))
φ(q)3 µ((q, N ))dα

= x3 ∫ ∞

−∞( ̂η◦(−αx))
2 ̂η∗(−αx)e(−αN )dα ·
 


∑

q≥1
 φ((q, N ))
φ(q)3 µ(q)2µ((q, N ))





−x3 ∫ ∞

−∞( ̂η◦(−αx))
2 ̂η∗(−αx)e(−αN ) ∑

q
(q,2) >min( δ0r
2|α|x ,r)

µ(q)2=1
 φ((q, N ))
φ(q)3 µ((q, N ))dα.

The last line in (3.20) is bounded
4 by

(3.21) x2| ̂η∗|∞
 ∫ ∞

−∞ | ̂η◦(−α)|
2 ∑

q
(q,2) >min( δ0r
2|α| ,r) µ(q)2

φ(q)2 dα.

By (2.1) (with k = 3), (B.11) and (B.12), this is at most

x2|η∗|1
 ∫ δ0/2

−δ0/2 | ̂η◦(−α)|
2 4.31004
r dα

+ 2x2|η∗|1
 ∫ ∞

δ0/2
 ( |η(3)
◦ |1
(2πα)3
 )2 8.62008|α|
δ0r dα

≤ |η∗|1
 (

4.31004|η◦|2
2 + 0.00113 |η(3)
◦ |2
1
δ5
0
 ) x2

r .

It is easy to see that

∑

q≥1
 φ((q, N ))
φ(q)3 µ(q)2µ((q, N )) = ∏

p|N
 (1 − 1
(p − 1)2
 ) · ∏

p∤N
 (1 + 1
(p − 1)3
 ) .

Expanding the integral implicit in the deﬁnition of ̂f ,

(3.22)
 ∫ ∞

∞ ( ̂η◦(−αx))
2 ̂η∗(−αx)e(−αN )dα =

1
x
 ∫ ∞

0
 ∫ ∞

0 η◦(t1)η◦(t2)η∗
 ( N
x − (t1 + t2)
) dt1dt2.

(This is standard. One rigorous way to obtain (3.22) is to approximate the inte-
gral over α ∈ (−∞, ∞) by an integral with a smooth weight, at diﬀerent scales;
as the scale becomes broader, the Fourier transform of the weight approximates
(as a distribution) the δ function. Apply Plancherel.)

4This is obviously crude, in that we are bounding φ((q, N ))/φ(q) by 1. We are doing so in
order to avoid a potentially harmful dependence on N .

16 H. A. HELFGOTT

Hence, (3.17) equals

(3.23)
 x2 · ∫ ∞

0
 ∫ ∞

0 η◦(t1)η◦(t2)η∗
 ( N
x − (t1 + t2)
) dt1dt2

· ∏

p|N
 (1 − 1
(p − 1)2
 ) · ∏

p∤N
 (1 + 1
(p − 1)3
 ) .

(the main term) plus

(3.24)
 


2.82643|η◦|
2
2(2 + ϵ0) · ϵ0 + 4.31004|η◦|2
2 + 0.00113 |η(3)
◦ |2
1
δ5
0
r
 


 |η∗|1x2

Here (3.23) is just as in the classical case [IK04, (19.10)], except for the fact
that a factor of 1/2 has been replaced by a double integral. We will later see
how to choose our smoothing functions (and x, in terms of N ) so as to make the
double integral as large as possible.
What remains to estimate is the contribution of all the terms of the form
errη,χ(δ, x) in (3.12) and (3.13). Let us ﬁrst deal with another matter – bounding
the ℓ2 norm of |Sη(α, x)|2 over the major arcs.

3.3. The ℓ2 norm over the major arcs. We can always bound the integral
of |Sη(α, x)|2 on the whole circle by Plancherel. If we only want the integral on
certain arcs, we use the bound in Prop. 5.2 (based on work by Ramar´e). If these
arcs are really the major arcs – that is, the arcs on which we have useful analytic
estimates – then we can hope to get better bounds using L-functions. This will
be useful both to estimate the error terms in this section and to make the use of
Ramar´e’s bounds more eﬃcient later.
By (3.8),

∑

a mod q
gcd(a,q)=1
 ∣
∣
∣
∣Sη
 ( a
q + δ
x , χ
)∣
∣
∣
∣
2

= 1
φ(q)2 ∑

χ
 ∑

χ′ τ (χ)τ (χ′)
 





 ∑

a mod q
gcd(a,q)=1
 χ(a)χ′(a)





 · Sη,χ∗(δ/x, x)Sη,χ′∗(δ/x, x)

+ O∗ (2(1 + √q)(log x)2|η|∞ max
α |Sη(α, x)| + ((1 + √q)(log x)
2|η|∞)2)

= 1
φ(q)
 ∑

χ |τ (χ)|
2|Sη,χ∗(δ/x, x)|
2 + Kq,1(2|Sη(0, x)| + Kq,1),

where Kq,1 = (1 + √q)(log x)
2|η|∞.
As is well-known (see, e.g., [IK04, Lem. 3.1])

τ (χ) = µ ( q
q∗
 ) χ∗ ( q
q∗
 ) τ (χ∗),

where q∗ is the modulus of χ∗ (i.e., the conductor of χ), and

|τ (χ
∗)| = √
q∗.

THE TERNARY GOLDBACH CONJECTURE IS TRUE 17

Using the expressions (3.12) and (3.13), we obtain

∑

a mod q
(a,q)=1
 ∣
∣
∣
∣Sη
 ( a
q + δ
x , x
)∣
∣
∣
∣

2 = µ2(q)
φ(q) |̂η(−δ)x + O∗ (errη,χT (δ, x) · x)|
2

+ 1
φ(q)
 

 ∑

χ̸=χT µ2 ( q
q∗
 ) q∗ · O∗ (| errη,χ(δ, x)|
2x
2)

 + Kq,1(2|Sη(0, x)| + Kq,1)

= µ2(q)x2

φ(q) (|̂η(−δ)|
2 + O∗ (|errη,χT (δ, x)(2|η|1 + errη,χT (δ, x))|)
)

+ O∗ (
q max
χ̸=χT | errη,χ∗(δ, x)|2x2 + Kq,2x) ,

where Kq,2 = Kq,1(2|Sη(0, x)|/x + Kq,1/x).
Thus, the integral of |Sη(α, x)|2 over M (see (3.5)) is

(3.25)
 ∑

q≤r
q odd
 ∑

a mod q
(a,q)=1
 ∫ a
q + δ0r
2qx

a
q − δ0r
2qx |Sη(α, x)|2 dα + ∑

q≤2r
q even
 ∑

a mod q
(a,q)=1
 ∫ a
q + δ0r
qx

a
q − δ0r
qx |Sη(α, x)|2 dα

= ∑

q≤r
q odd
 µ2(q)x2

φ(q)
 ∫ δ0r
2qx

− δ0r
2qx |̂η(−αx)|
2 dα + ∑

q≤2r
q even
 µ2(q)x2

φ(q)
 ∫ δ0r
qx

− δ0r
qx |̂η(−αx)|
2 dα

+ O∗ (
∑

q
 µ2(q)x2

φ(q) · gcd(q, 2)δ0r
qx
 (ET
η, δ0r
2 (2|η|1 + ET
η, δ0r
2 )
))

+ ∑

q≤r
q odd
 δ0rx
q · O∗
 





q max
χ mod q
χ̸=χT
|δ|≤δ0r/2q
 | errη,χ∗(δ, x)|2 + Kq,2
x
 







+ ∑

q≤2r
q even
 2δ0rx
q · O∗
 





q max
χ mod q
χ̸=χT
|δ|≤δ0r/q
 | errη,χ∗(δ, x)|
2 + Kq,2
x
 





 ,

where
 ETη,s = max
|δ|≤s | errη,χT (δ, x)|

and χT is the trivial character. If all we want is an upper bound, we can simply
remark that

18 H. A. HELFGOTT

x ∑

q≤r
q odd
 µ2(q)
φ(q)
 ∫ δ0r
2qx

− δ0r
2qx |̂η(−αx)|
2 dα + x ∑

q≤2r
q even
 µ2(q)
φ(q)
 ∫ δ0r
qx

− δ0r
qx |̂η(−αx)|2 dα

≤
 



 ∑

q≤r
q odd
 µ2(q)
φ(q) + ∑

q≤2r
q even
 µ2(q)
φ(q)
 



 |̂η|2
2 = 2|η|2
2 ∑

q≤r
q odd
 µ2(q)
φ(q) .

If we also need a lower bound, we proceed as follows.
Again, we will work with an approximation η◦ such that (a) |η − η◦|2 is small,
(b) η◦ is thrice diﬀerentiable outside ﬁnitely many points, (c) η(3)
◦ ∈ L1. Clearly,

x ∑

q≤r
q odd
 µ2(q)
φ(q)
 ∫ δ0r
2qx

− δ0r
2qx |̂η(−αx)|
2 dα

≤ ∑

q≤r
q odd
 µ2(q)
φ(q)
 (∫ δ0r
2q

− δ0r
2q | ̂η◦(−α)|2 dα + 2⟨| ̂η◦| , |̂η − ̂η◦|⟩ + |̂η − ̂η◦|
2
2
)

= ∑

q≤r
q odd
 µ2(q)
φ(q)
 ∫ δ0r
2q

− δ0r
2q | ̂η◦(−α)|
2 dα

+ O∗ ( 1
2 log r + 0.85
) (2 |η◦|2 |η − η◦|2 + |η◦ − η|
2
2) ,

where we are using (B.6) and isometry. Also,

∑

q≤2r
q even
 µ2(q)
φ(q)
 ∫ δ0r
qx

− δ0r
qx |̂η(−αx)|
2 dα = ∑

q≤r
q odd
 µ2(q)
φ(q)
 ∫ δ0r
2qx

− δ0r
2qx |̂η(−αx)|2 dα.

By (2.1) and Plancherel,

∫ δ0r
2q

− δ0r
2q | ̂η◦(−α)|
2 dα = ∫ ∞

−∞ | ̂η◦(−α)|
2 dα − O∗ (

2 ∫ ∞

δ0r
2q
 |η(3)
◦ |2
1
(2πα)6 dα
)

= |η◦|
2
2 + O∗ ( |η(3)
◦ |2
1q5

5π6(δ0r)5
 )
 ,

Hence

∑

q≤r
q odd
 µ2(q)
φ(q)
 ∫ δ0r
2q

− δ0r
2q | ̂η◦(−α)|
2 dα = |η◦|
2
2 · ∑

q≤r
q odd
 µ2(q)
φ(q) + O∗
 



 ∑

q≤r
q odd
 µ2(q)
φ(q) |η(3)
◦ |2
1q5

5π6(δ0r)5
 



 .

THE TERNARY GOLDBACH CONJECTURE IS TRUE 19

Using (B.13), we get that

∑

q≤r
q odd
 µ2(q)
φ(q) |η(3)
◦ |2
1q5

5π6(δ0r)5 ≤ 1
r
 ∑

q≤r
q odd
 µ2(q)q
φ(q) · |η(3)
◦ |2
1
5π6δ5
0

≤ |η(3)
◦ |2
1
5π6δ5
0 · (
0.64787 + log r
4r + 0.425
r
 ) .

Going back to (3.25), we use (B.2) to bound

∑

q
 µ2(q)x2

φ(q) gcd(q, 2)δ0r
qx ≤ 2.59147 · δ0rx.

We also note that ∑

q≤r
q odd
 1
q + ∑

q≤2r
q even
 2
q = ∑

q≤r
 1
q − ∑

q≤ r
2
 1
2q + ∑

q≤r
 1
q

≤ 2 log er − log r
2 ≤ log 2e2r.

We have proven the following result.

Lemma 3.1. Let η : [0, ∞) → R be in L1 ∩ L∞. Let Sη(α, x) be as in (3.1) and
let M = Mδ0,r be as in (3.5). Let η◦ : [0, ∞) → R be thrice diﬀerentiable outside
ﬁnitely many points. Assume η(3)
◦ ∈ L1.
Assume r ≥ 182. Then
(3.26)∫

M |Sη(α, x)|
2dα = Lr,δ0x + O∗ (
5.19δ0xr (
ET
η, δ0r
2 · (
|η|1 + ETη,δ0r/2
2
 )))

+ O∗ (δ0r(log 2e2r) (x · E2
η,r,δ0 + Kr,2)) ,

where
(3.27)
Eη,r,δ0 = max
χ mod q
q≤r·gcd(q,2)
|δ|≤gcd(q,2)δ0r/2q
 √q| errη,χ∗(δ, x)|, ETη,s = max
|δ|≤s | errη,χT (δ, x)|,

Kr,2 = (1 + √2r)(log x)
2|η|∞(2|Sη(0, x)|/x + (1 + √2r)(log x)
2|η|∞/x)

and Lr,δ0 satisﬁes both

(3.28) Lr,δ0 ≤ 2|η|
2
2 ∑

q≤r
q odd
 µ2(q)
φ(q)

and

(3.29)
 Lr,δ0 = 2|η◦|2
2 ∑

q≤r
q odd
 µ2(q)
φ(q) + O∗(log r + 1.7) · (2 |η◦|2 |η − η◦|2 + |η◦ − η|
2
2)

+ O∗ ( 2|η(3)
◦ |2
1
5π6δ5
0
 )
 · (
0.64787 + log r
4r + 0.425
r
 ) .

20 H. A. HELFGOTT

The error term xrETη,δ0r will be very small, since it will be estimated using
the Riemann zeta function; the error term involving Kr,2 will be completely
negligible. The term involving xr(r + 1)E2
η,r,δ0; we see that it constrains us to
have | errη,χ(x, N )| less than a constant times 1/r if we do not want the main
term in the bound (3.26) to be overwhelmed.

3.4. The integral over the major arcs: error terms. Conclusion. There
are at least two ways we can evaluate (3.4). One is to substitute (3.10) into (3.4).
The disadvantages here are that (a) this can give rise to pages-long formulae, (b)
this gives error terms proportional to xr| errη,χ(x, N )|, meaning that, to win, we
would have to show that | errη,χ(x, N )| is much smaller than 1/r. What we will
do instead is to use our ℓ2 estimate (3.26) in order to bound the contribution of
non-principal terms. This will give us a gain of almost √r on the error terms; in
other words, to win, it will be enough to show later that | errη,χ(x, N )| is much
smaller than 1/√r.
The contribution of the error terms in Sη3(α, x) (that is, all terms involving
the quantities errη,χ in expressions (3.12) and (3.13)) to (3.4) is

(3.30)
 ∑

q≤r
q odd
 1
φ(q)
 ∑

χ3 mod qτ (χ3) ∑

a mod q
(a,q)=1
 χ3(a)e(−N a/q)

∫ δ0r
2qx

− δ0r
2qx Sη+(α + a/q, x)
2 errη∗,χ∗
3 (αx, x)e(−N α)dα

+ ∑

q≤2r
q even
 1
φ(q)
 ∑

χ3 mod qτ (χ3) ∑

a mod q
(a,q)=1
 χ3(a)e(−N a/q)

∫ δ0r
qx

− δ0r
qx Sη+(α + a/q, x)2 errη∗,χ∗
3 (αx, x)e(−N α)dα.

We should also remember the terms in (3.11); we can integrate them over all of
R/Z, and obtain that they contribute at most

∫

R/Z2
 3∑

j=1
 ∏

j′̸=j |Sηj′ (α, x)| · max
q≤r
 ∑

p|q log p ∑

α≥1 ηj
 ( pα

x
 ) dα

≤ 2
 3∑

j=1
 ∏

j′̸=j |Sηj′ (α, x)|2 · max
q≤r
 ∑

p|q log p ∑

α≥1 ηj
 ( pα

x
 )

= 2 ∑

n Λ2(n)η2
+(n/x) · log r · max
p≤r
 ∑

α≥1 η∗
 ( pα

x
 )

+ 4√
∑

n Λ2(n)η2
+(n/x) · ∑

n Λ2(n)η2
∗(n/x) · log r · max
p≤r
 ∑

α≥1 η∗
 ( pα

x
 )

by Cauchy-Schwarz and Plancherel.

THE TERNARY GOLDBACH CONJECTURE IS TRUE 21

The absolute value of (3.30) is at most

(3.31)
 ∑

q≤r
q odd
 ∑

a mod q
(a,q)=1
√q ∫ δ0r
2qx

− δ0r
2qx
 ∣
∣Sη+(α + a/q, x)∣
∣2 dα · max
χ mod q
|δ|≤δ0r/2q
 | errη∗,χ∗(δ, x)|

+ ∑

q≤2r
q even
 ∑

a mod q
(a,q)=1
√q ∫ δ0r
qx

− δ0r
qx
 ∣
∣Sη+(α + a/q, x)
∣
∣2 dα · max
χ mod q
|δ|≤δ0r/q
 | errη∗,χ∗(δ, x)|

≤ ∫

Mδ0,r
 ∣
∣Sη+(α)
∣
∣2 dα · max
χ mod q
q≤r·gcd(q,2)
|δ|≤gcd(q,2)δ0r/q
 √q| errη∗,χ∗(δ, x)|.

We can bound the integral of |Sη+(α)|2 by (3.26).
What about the contribution of the error part of Sη2(α, x)? We can obviously
proceed in the same way, except that, to avoid double-counting, Sη3(α, x) needs
to be replaced by

(3.32) 1
φ(q) τ (χ0) ̂η3(−δ) · x = µ(q)
φ(q) ̂η3(−δ) · x,

which is its main term (coming from (3.12)). Instead of having an ℓ2 norm as
in (3.31), we have the square-root of a product of two squares of ℓ2 norms (by
Cauchy-Schwarz), namely, ∫

M |S∗
η+(α)|2dα and

(3.33)
 ∑

q≤r
q odd
 µ2(q)
φ(q)2
 ∫ δ0r
2qx

− δ0r
2qx | ̂η∗(−αx)x|
2 dα + ∑

q≤2r
q even
 µ2(q)
φ(q)2
 ∫ δ0r
qx

− δ0r
qx | ̂η∗(−αx)x|2 dα

≤ x| ̂η∗|
2
2 · ∑

q
 µ2(q)
φ(q)2 .

By (B.4), the sum over q is at most 2.82643.
As for the contribution of the error part of Sη1(α, x), we bound it in the same
way, using solely the ℓ2 norm in (3.33) (and replacing both Sη2(α, x) and Sη3(α, x)
by expressions as in (3.32)).
The total of the error terms is thus

(3.34)
 x · max
χ mod q
q≤r·gcd(q,2)
|δ|≤gcd(q,2)δ0r/q
 √q · | errη∗,χ∗(δ, x)| · A

+ x · max
χ mod q
q≤r·gcd(q,2)
|δ|≤gcd(q,2)δ0r/q
 √q · | errη+,χ∗(δ, x)|(
√A + √B+)
√
B∗,

where A = (1/x) ∫
M |Sη+(α, x)|2dα (bounded as in (3.26)) and

(3.35) B∗ = 2.82643|η∗|
2
2, B+ = 2.82643|η+|
2
2.

In conclusion, we have proven

Proposition 3.2. Let x ≥ 1. Let η+, η∗ : [0, ∞) → R. Assume η+ ∈ C2, η′′
+ ∈ L2
and η+, η∗ ∈ L1 ∩ L2. Let η◦ : [0, ∞) → R be thrice diﬀerentiable outside ﬁnitely
many points. Assume η(3)
◦ ∈ L1 and |η+ − η◦|2 < ϵ0|η◦|2, where ϵ0 ≥ 0.

22 H. A. HELFGOTT

Let Sη(α, x) = ∑
n Λ(n)e(αn)η(n/x). Let errη,χ, χ primitive, be given as in
(3.12) and (3.13). Let δ0 > 0, r ≥ 1. Let M = Mδ0,r be as in (3.5).
Then, for any N ≥ 0,
∫

M Sη+(α, x)
2Sη∗(α, x)e(−N α)dα

equals
(3.36)

C0Cη◦,η∗x2 +
 


2.82643|η◦|
2
2(2 + ϵ0) · ϵ0 + 4.31004|η◦|2
2 + 0.0012 |η(3)
◦ |2
1
δ5
0
r
 


 |η∗|1x2

+ O∗(Eη∗,r,δ0Aη+ + Eη+,r,δ0 · 1.6812(√
Aη+ + 1.6812|η+|2)|η∗|2) · x2

+ O∗ (2Zη2
+,2(x)LSη∗(x, r) · x + 4√
Zη2
+,2(x)Zη2
∗,2(x)LSη+(x, r) · x) ,

where

(3.37)
 C0 = ∏

p|N
 (
1 − 1
(p − 1)2
 ) · ∏

p∤N
 (
1 + 1
(p − 1)3
 ) ,

Cη◦,η∗ = ∫ ∞

0
 ∫ ∞

0 η◦(t1)η◦(t2)η∗
 ( N
x − (t1 + t2)
) dt1dt2,

(3.38)
Eη,r,δ0 = max
χ mod q
q≤gcd(q,2)·r
|δ|≤gcd(q,2)δ0r/2q
 √q · | errη,χ∗(δ, x)|, ETη,s = max
|δ|≤s/q | errη,χT (δ, x)|,

Aη = 1
x
 ∫

M
 ∣
∣Sη+(α, x)∣
∣2 dα, Lη,r,δ0 ≤ 2|η|
2
2 ∑

q≤r
q odd
 µ2(q)
φ(q) ,

Kr,2 = (1 + √2r)(log x)2|η|∞(2Zη,1(x)/x + (1 + √2r)(log x)
2|η|∞/x),

Zη,k(x) = 1
x
 ∑

n Λk(n)η(n/x), LSη(x, r) = log r · max
p≤r
 ∑

α≥1 η ( pα

x
 ) ,

and errη,χ is as in (3.12) and (3.13).

Here is how to read these expressions. The error term in the ﬁrst line of (3.36)
will be small provided that ϵ0 is small and r is large. The third line of (3.36) will
be negligible, as will be the term 2δ0r(log er)Kr,2 in the deﬁnition of Aη. (Clearly,
Zη,k(x) ≪η (log x)k−1 and LSη(x, q) ≪η τ (q) log x for any η of rapid decay.)
It remains to estimate the second line of (3.36). This includes estimating Aη
– a task that was already accomplished in Lemma 3.1. We see that we will have
to give very good bounds for Eη,r,δ0 when η = η+ or η = η∗. We also see that we
want to make C0Cη+,η∗x2 as large as possible; it will be competing not just with
the error terms here, but, more importantly, with the bounds from the minor
arcs, which will be proportional to |η+|2
2|η∗|1.

4. Optimizing and coordinating smoothing functions

One of our goals is to maximize the quantity Cη◦,η∗ in (3.37) relative to
|η◦|2
2|η∗|1. One way to do this is to ensure that (a) η∗ is concentrated on a very

THE TERNARY GOLDBACH CONJECTURE IS TRUE 23

short5 interval [0, ϵ), (b) η◦ is supported on the interval [0, 2], and is symmetric
around t = 1, meaning that η◦(t) ∼ η◦(2 − t). Then, for x ∼ N/2, the integral
∫ ∞

0
 ∫ ∞

0 η◦(t1)η◦(t2)η∗
 ( N
x − (t1 + t2)
) dt1dt2

in (3.37) should be approximately equal to

(4.1) |η∗|1 · ∫ ∞

0 η◦(t)η◦
 ( N
x − t
) dt = |η∗|1 · ∫ ∞

0 η◦(t)
2dt = |η∗|1 · |η◦|2
2,

provided that η0(t) ≥ 0 for all t. It is easy to check (using Cauchy-Schwarz in
the second step) that this is essentially optimal. (We will redo this rigorously in
a little while.)
At the same time, the fact is that major-arc estimates are best for smoothing
functions η of a particular form, and we have minor-arc estimates from [Helb] for
a diﬀerent speciﬁc smoothing η2. The issue, then, is how do we choose η◦ and η∗
as above so that we can
• η∗ is concentrated on [0, ϵ),
• η◦ is supported on [0, 2] and symmetric around t = 1,
• we can give minor-arc and major-arc estimates for η∗,
• we can give major-arc estimates for a function η+ close to η◦ in ℓ2 norm?

4.1. The symmetric smoothing function η◦. We will later work with a
smoothing function η♥ whose Mellin transform decreases very rapidly. Because
of this rapid decay, we will be able to give strong results based on an explicit
formula for η♥. The issue is how to deﬁne η◦, given η♥, so that η◦ is symmetric
around t = 1 (i.e., η◦(2 − x) ∼ η◦(x)) and is very small for x > 2.
We will later set η♥(t) = e−t2/2. Let

(4.2) h : t ↦→
 {
t3(2 − t)3et−1/2 if t ∈ [0, 2],
0 otherwise

We deﬁne η◦ : R → R by

(4.3) η◦(t) = h(t)η♥(t) =
 {
t3(2 − t)3e−(t−1)2/2 if t ∈ [0, 2],
0 otherwise.

It is clear that η◦ is symmetric around t = 1 for t ∈ [0, 2].

4.1.1. The product η◦(t)η◦(ρ − t). We now should go back and redo rigorously
what we discussed informally around (4.1). More precisely, we wish to estimate

(4.4) η◦(ρ) = ∫ ∞

−∞ η◦(t)η◦(ρ − t)dt = ∫ ∞

−∞ η◦(t)η◦(2 − ρ + t)dt

for ρ ≤ 2 close to 2. In this, it will be useful that the Cauchy-Schwarz inequality
degrades slowly, in the following sense.

Lemma 4.1. Let V be a real vector space with an inner product ⟨·, ·⟩. Then, for
any v, w ∈ V with |w − v|2 ≤ |v|2/2,

⟨v, w⟩ = |v|2|w|2 + O∗(2.71|v − w|2
2).

5This is an idea due to Bourgain in a related context [Bou99].

24 H. A. HELFGOTT

Proof. By a truncated Taylor expansion,

√1 + x = 1 + x
2 + x2

2 max
0≤t≤1 1
4(1 − (tx)2)3/2

= 1 + x
2 + O∗ ( x2

23/2
 )

for |x| ≤ 1/2. Hence, for δ = |w − v|2/|v|2,

|w|2
|v|2 =
 √

1 + 2⟨w − v, v⟩ + |w − v|2
2
|v|2
2 = 1 + 2 ⟨w−v,v⟩
|v|2
2 + δ2

2 + O∗ ( (2δ + δ2)2

23/2
 )

= 1 + δ + O∗ (( 1
2 + (5/2)2

23/2
 ) δ2) = 1 + ⟨w − v, v⟩
|v|2
2 + O∗ (
2.71 |w − v|2
2
|v|2
2
 ) .

Multiplying by |v|2
2, we obtain that

|v|2|w|2 = |v|
2
2 + ⟨w − v, v⟩ + O∗ (2.71|w − v|
2
2) = ⟨v, w⟩ + O∗ (2.71|w − v|
2
2) .
□

Applying Lemma 4.1 to (4.4), we obtain that

(4.5)
 (η◦ ∗ η◦)(ρ) = ∫ ∞

−∞ η◦(t)η◦((2 − ρ) + t)dt

=
 √∫ ∞

−∞ |η◦(t)|2dt
√∫ ∞

−∞ |η◦((2 − ρ) + t)|2dt

+ O∗ (
2.71 ∫ ∞

−∞ |η◦(t) − η◦((2 − ρ) + t)|
2 dt
)

= |η◦|2
2 + O∗ (

2.71 ∫ ∞

−∞
 (∫ 2−ρ

0
 ∣
∣η′
◦(r + t)∣
∣ dr)2 dt

)

= |η◦|2
2 + O∗ (
2.71(2 − ρ) ∫ 2−ρ

0
 ∫ ∞

−∞
 ∣
∣η′
◦(r + t)
∣
∣2 dtdr)

= |η◦|2
2 + O∗(2.71(2 − ρ)
2|η′
◦|
2
2).

We will be working with η∗ supported on the non-negative reals; we recall that
η◦ is supported on [0, 2]. Hence
(4.6)
∫ ∞

0
 ∫ ∞

0 η◦(t1)η◦(t2)η∗
 ( N
x − (t1 + t2)
) dt1dt2 = ∫ N
x

0 (η◦ ∗ η◦)(ρ)η∗
 ( N
x − ρ
) dρ

= ∫ N
x

0 (|η◦|2
2 + O∗(2.71(2 − ρ)
2|η′
◦|
2
2)) · η∗
 ( N
x − ρ
) dρ

= |η◦|
2
2
 ∫ N
x

0 η∗(ρ)dρ + 2.71|η′
◦|
2
2 · O∗ (∫ N
x

0 ((2 − N/x) + ρ)
2η∗(ρ)dρ
)
 ,

provided that N/x ≥ 2. We see that it will be wise to set N/x very slightly larger
than 2. As we said before, η∗ will be scaled so that it is concentrated on a small
interval [0, ϵ).
 THE TERNARY GOLDBACH CONJECTURE IS TRUE 25

4.2. The smoothing function η∗: adapting minor-arc bounds. Here the
challenge is to deﬁne a smoothing function η∗ that is good both for minor-arc
estimates and for major-arc estimates. The two regimes tend to favor diﬀerent
kinds of smoothing function. For minor-arc estimates, both [Tao] and [Helb] use

(4.7) η2(t) = 4 max(log 2 − | log 2t|, 0) = ((2I[1/2,1]) ∗M (2I[1/2,1]))(t),

where I[1/2,1](t) is 1 if t ∈ [1/2, 1] and 0 otherwise. For major-arc estimates, we
will use a function based on η♥ = e−t2/2.

We will actually use here the function t2e−t2/2, whose Mellin transform is M η♥(s+
2) (by, e.g., [BBO10, Table 11.1]).)
We will follow the simple expedient of convolving the two smoothing functions,
one good for minor arcs, the other one for major arcs. In general, let ϕ1, ϕ2 :
[0, ∞) → C. It is easy to use bounds on sums of the form

(4.8) Sf,ϕ1(x) = ∑

n f (n)ϕ1(n/x)

to bound sums of the form Sf,ϕ1∗M ϕ2:

(4.9)
 Sf,ϕ1∗M ϕ2 = ∑

n f (n)(ϕ1 ∗M ϕ2) ( n
x
 )

= ∫ ∞

0
 ∑

n f (n)ϕ1 ( n
wx
 ) ϕ2(w) dw
w = ∫ ∞

0 Sf,ϕ1(wx)ϕ2(w) dw
w .

The same holds, of course, if ϕ1 and ϕ2 are switched, since ϕ1 ∗M ϕ2 = ϕ2 ∗M ϕ1.
The only objection is that the bounds on (4.8) that we input might not be valid,
or non-trivial, when the argument wx of Sf,ϕ1(wx) is very small. Because of this,
it is important that the functions ϕ1, ϕ2 vanish at 0, and desirable that their ﬁrst
derivatives do so as well.
Let us see how this works out in practice for ϕ1 = η2. Here η2 : [0, ∞) → R is
given by

(4.10) η2 = η1 ∗M η1 = 4 max(log 2 − | log 2t|, 0),

where η1 = 2 · I[1/2,1]. Bounding the sums Sη2(α, x) on the minor arcs was the
main subject of [Helb].
Before we use [Helb, Main Thm.], we need an easy lemma so as to simplify its
statement.

Lemma 4.2. For any q ≥ 1 and any r ≥ max(3, q),
q
φ(q) < ϝ(r),

where

(4.11) ϝ(r) = e
γ log log r + 2.50637
log log r .

Proof. Since ϝ(r) is increasing for r ≥ 27, the statement follows immediately for
q ≥ 27 by [RS62, Thm. 15]: q
φ(q) < ϝ(q) ≤ ϝ(r).

For r < 27, it is clear that q/φ(q) ≤ 2 · 3/(1 · 2) = 3; it is also easy to see that
ϝ(r) > eγ · 2.50637 > 3 for all r > e. □

26 H. A. HELFGOTT

It is time to quote the main theorem in [Helb]. Let x ≥ x0, x0 = 2.16 · 1020.
Let 2α = a/q + δ/x, q ≤ Q, gcd(a, q) = 1, |δ/x| ≤ 1/qQ, where Q = (3/4)x2/3.
Then, if 3 ≤ q ≤ x1/3/6, [Helb, Main Thm.] gives us that

(4.12) |Sη2(α, x)| ≤ gx
 (
max (1, |δ|
8
 ) · q) x,

where

(4.13) gx(r) = (Rx,2r log 2r + 0.5)
√
ϝ(r) + 2.5
√2r + Lr
r + 3.2x−1/6,

with

(4.14) Rx,t = 0.27125 log
 (

1 + log 4t

2 log 9x1/3
2.004t
 )
 + 0.41415

Lt = ϝ(t) (log 2 7
4 t 13
4 + 80
9
 ) + log 2 16
9 t 80
9 + 111
5 ,

(We are using Lemma 4.2 to bound all terms 1/φ(q) appearing in [Helb, Main
Thm.]; we are also using the obvious fact that, for δ0q ﬁxed and 0 < a < b, δa
0 qb is
maximal when δ0 is minimal.) If q > x1/3/6, then, again by [Helb, Main Thm.],

(4.15) |Sη2(α, x)| ≤ h(x)x,

where

(4.16) h(x) = 0.2727x−1/6(log x)3/2 + 1218x−1/3 log x.

We will work with x varying within a range, and so we must pay some attention
to the dependence of (4.12) and (4.15) on x. Let us prove two auxiliary lemmas
on this.

Lemma 4.3. Let gx(r) be as in (4.13) and h(x) as in (4.16). Then

x ↦→
 {
h(x) if x < (6r)3

gx(r) if x ≥ (6r)3

is a decreasing function of x for r ≥ 3 ﬁxed and x ≥ 21.

Proof. It is clear from the deﬁnitions that x ↦→ h(x) (for x ≥ 21) and x ↦→ gx,0(r)
are both decreasing. Thus, we simply have to show that h(x1) ≥ gx1,0(r) for
x1 = (6r)3. Since x1 ≥ (6 · 11)3 > e12.5,

Rx1,2r ≤ 0.27125 log(0.065 log x1 + 1.056) + 0.41415

≤ 0.27125 log((0.065 + 0.0845) log x1) + 0.41415 ≤ 0.27215 log log x1.

Hence

Rx1,2r log 2r + 0.5 ≤ 0.27215 log log x1 log x1/3
1 − 0.27215 log 12.5 log 3 + 0.5
≤ 0.09072 log log x1 log x1 − 0.255.

At the same time,

(4.17) ϝ(r) = e
γ log log x1/3
1
6 + 2.50637
log log r ≤ e
γ log log x1 − eγ log 3 + 1.9521

≤ e
γ log log x1

THE TERNARY GOLDBACH CONJECTURE IS TRUE 27

for r ≥ 37, and we also get ϝ(r) ≤ eγ log log x1 for r ∈ [11, 37] by the bisection
method with 10 iterations. Hence

(Rx1,2r log 2r + 0.5)
√
ϝ(r) + 2.5

≤ (0.09072 log log x1 log x1 − 0.255)
√
eγ log log x1 + 2.5

≤ 0.1211 log x1(log log x1)
3/2 + 2,

and so

(Rx1,2r log 2r + 0.5)
√
ϝ(r) + 2.5
√2r ≤ (0.21 log x1(log log x1)3/2 + 3.47)x−1/6
1 .

Now, by (4.17),

Lr ≤ eγ log log x1 · (
log 2 7
4 (x
1/3
1 /6)
13/4 + 80
9
 ) + log 2 16
9 (x1/3
1 /6) 80
9 + 111
5

≤ eγ log log x1 · ( 13
12 log x1 + 4.28
) + 80
27 log x + 7.51.

It is clear that
4.28eγ log log x1 + 80
27 log x1 + 7.51

x
1/3
1 /6 < 1218x−1/3
1 log x1.

for x1 ≥ e.
It remains to show that

(4.18) 0.21 log x1(log log x1)3/2 + 3.47 + 3.2 + 13
12 e
γx−1/6
1 log x1 log log x1

is less than 0.2727(log x1)3/2 for x1 large enough. Since t ↦→ (log t)3/2/t1/2 is
decreasing for t > e3, we see that

0.21 log x1(log log x1)3/2 + 6.67 + 13
12 eγx
−1/6
1 log x1 log log x1
0.2727(log x1)3/2 < 1

for all x1 ≥ e34, simply because it is true for x = e34 > ee3.
We conclude that h(x1) ≥ gx1,0(r) = gx1,0(x
1/3
1 /6) for x1 ≥ e34. We check
that h(x1) ≥ gx1,0(x1/3
1 /6) for all x1 ∈ [5832, e34] as well by the bisection method
(applied to [5832, 583200] and to [583200, e34] with 30 iterations – in the latter
interval, with 20 initial iterations). □

Lemma 4.4. Let Rx,r be as in (4.13). Then t → Ret,r(r) is convex-up for
t ≥ 3 log 6r.

Proof. Since t → e−t/6 and t → t are clearly convex-up, all we have to do is to
show that t → Ret,r is convex-up. In general, since

(log f )
′′ = ( f ′

f
 )′ = f ′′f − (f ′)2

f 2 ,

a function of the form (log f ) is convex-up exactly when f ′′f − (f ′)2 ≥ 0. If
f (t) = 1 + a/(t − b), we have f ′′f − (f ′)2 ≥ 0 whenever

(t + a − b) · (2a) ≥ a
2,

i.e., a2 + 2at ≥ 2ab, and that certainly happens when t ≥ b. In our case, b =
3 log(2.004r/9), and so t ≥ 3 log 6r implies t ≥ b. □

28 H. A. HELFGOTT

Now we come to the point where we prove bounds on the exponential sums
Sη∗(α, x) (that is, sums based on the smoothing η∗) based on our bounds (from
[Helb]) on the exponential sums Sη2(α, x). This is straightforward, as promised.

Proposition 4.5. Let x ≥ Kx0, x0 = 2.16 · 1020, K ≥ 1. Let Sη(α, x) be as
in (3.1). Let η∗ = η2 ∗M ϕ, where η2 is as in (4.10) and ϕ : [0, ∞) → [0, ∞) is
continuous and in L1.
Let 2α = a/q + δ/x, q ≤ Q, gcd(a, q) = 1, |δ/x| ≤ 1/qQ, where Q = (3/4)x2/3.
If q ≤ (x/K)1/3/6, then

(4.19) Sη∗(α, x) ≤ gx,ϕ
 (max (
1, |δ|
8
 ) q) · |ϕ|1x,

where

(4.20) gx,ϕ(r) = (Rx,K,ϕ,2r log 2r + 0.5)
√
ϝ(r) + 2.5
√2r + Lr
r + 3.2K1/6x−1/6,

Rx,K,ϕ,t = Rx,t + (Rx/K,t − Rx,t) Cϕ,2,K/|ϕ|1
log K
with Rx,t and Lr are as in (4.14), and

(4.21) Cϕ,2,K = − ∫ 1

1/K ϕ(w) log w dw.

If q > (x/K)1/3/6, then

|Sη∗(α, x)| ≤ hϕ(x/K) · |ϕ|1x,

where

(4.22)
 hϕ(x) = h(x) + Cϕ,0,K/|ϕ|1,

Cϕ,0,K = 1.04488 ∫ 1/K

0 |ϕ(w)|dw

and h(x) is as in (4.16).

Proof. By (4.9),

Sη∗(α, x) = ∫ 1/K

0 Sη2(α, wx)ϕ(w) dw
w + ∫ ∞

1/K Sη2(α, wx)ϕ(w) dw
w .

We bound the ﬁrst integral by the trivial estimate |Sη2(α, wx)| ≤ |Sη2(0, wx)|
and Cor. A.3:
∫ 1/K

0 |Sη2(0, wx)|ϕ(x) dw
w ≤ 1.04488 ∫ 1/K

0 wxϕ(w) dw
w

= 1.04488x · ∫ 1/K

0 ϕ(w)dw.

If w ≥ 1/K, then wx ≥ x0, and we can use (4.12) or (4.15). If q > (x/K)1/3/6,
then |Sη2(α, wx)| ≤ h(x/K)wx by (4.15); moreover, |Sη2(α, y)| ≤ h(y)y for
x/K ≤ y < (6q)3 (by (4.15)) and |Sη2(α, y)| ≤ gy,1(r) for y ≥ (6q)3 (by (4.12)).
Thus, Lemma 4.3 gives us that
∫ ∞

1/K |Sη2(α, wx)|ϕ(w) dw
w ≤ ∫ ∞

1/K h(x/K)wx · ϕ(w) dw
w

= h(x/K)x ∫ ∞

1/K ϕ(w)dw ≤ h(x/K)|ϕ|1 · x.

THE TERNARY GOLDBACH CONJECTURE IS TRUE 29

If q ≤ (x/K)1/3/6, we always use (4.12). We can use the coarse bound
∫ ∞

1/K 3.2x−1/6 · wx · ϕ(w) dw
w ≤ 3.2K1/6|ϕ|1x
5/6

Since Lr does not depend on x,
∫ ∞

1/K
 Lr
r · wx · ϕ(w) dw
w ≤ Lr
r |ϕ|1x.

By Lemma 4.4 and q ≤ (x/K)1/3/6, y ↦→ Rey,t is convex-up and decreasing for
y ∈ [log(x/K), ∞). Hence

Rwx,t ≤
 { log w
log 1
K Rx/K,t + (1 − log w
log 1
K
 ) Rx,t if w < 1,

Rx,t if w ≥ 1.

Therefore
∫ ∞

1/KRwx,t · wx · ϕ(w) dw
w

≤ ∫ 1

1/K
 ( log w
log 1
K Rx/K,t +
 (

1 − log w
log 1
K
 )
 Rx,t
)
 xϕ(w)dw + ∫ ∞

1 Rx,tϕ(w)xdw

≤ Rx,tx · ∫ ∞

1/K ϕ(w)dw + (Rx/K,t − Rx,t) x
log K
 ∫ 1

1/K ϕ(w) log wdw

≤ (
Rx,t|ϕ|1 + (Rx/K,t − Rx,t) Cϕ,2
log K
 ) · x,

where
 Cϕ,2,K = − ∫ 1

1/K ϕ(w) log w dw.
 □

We ﬁnish by proving a couple more lemmas.

Lemma 4.6. Let x > K · (6e)3, K > 1. Let η∗ = η2 ∗M ϕ, where η2 is as in
(4.10) and ϕ : [0, ∞) → [0, ∞) is continuous and in L1. Let gx,ϕ be as in (4.20).
Then gx,ϕ(r) is a decreasing function of r for r ≥ 175.

Proof. Taking derivatives, we can easily see that

(4.23) r ↦→ log log r
r , r ↦→ log r
r , r ↦→ (log r)2 log log r
r

are decreasing for r ≥ 20. The same is true if log log r is replaced by ϝ(r), since
ϝ(r)/ log log r is a decreasing function for r ≥ e. Since (Cϕ,2/|φ|1)/ log K ≤ 1,
we see that it is enough to prove that r ↦→ Ry,t log 2r√log log r/
√2r is decreasing
on r for y = x and y = x/K (under the assumption that r ≥ 175).
Looking at (4.14) and at (4.23), it remains only to check that

(4.24) r ↦→ log
 (

1 + log 8r

2 log 9x1/3
4.008r
 ) √ log log r
r

30 H. A. HELFGOTT

is decreasing on r for r ≥ 175. Taking logarithms, and then derivatives, we see
that we have to show that

1
r ℓ+ log 8r
r
2ℓ2
(1 + log 8r
2ℓ ) log (1 + log 8r
2ℓ ) + 1
2r log r log log r < 1
2r ,

where ℓ = log 9x1/3
4.008r . Since r ≤ x1/3/6, ℓ ≥ log 54/4.008 > 2.6. Thus, it is enough
to ensure that

(4.25) 2/2.6
(1 + log 8r
2ℓ ) log (1 + log 8r
2ℓ ) + 1
log r log log r < 1.

Since this is true for r = 175 and the left side is decreasing on r, the inequality
is true for all r ≥ 175. □

Lemma 4.7. Let x ≥ 1025. Let φ : [0, ∞) → [0, ∞) be continuous and in L1.
Let gx,φ(r) and h(x) be as in (4.20) and (4.16), respectively. Then

gx,φ
 ( 3
8 x4/15) ≥ h(2x/ log x).

Proof. We can bound gx,φ(r) from below by

gmx(r) = (Rx,r log 2r + 0.5)
√
ϝ(r) + 2.5
√2r .

Let r = (3/8)x4/15. Using the assumption that x ≥ 1025, we see that

Rx,r = 0.27125 log
 


1 + log ( 3x4/15
2 )

2 log ( 9
2.004· 3
8 · x 1
3 −4/15)
 


 + 0.41415 ≥ 0.63368.

Using x ≥ 1025 again, we get that

ϝ(r) = eγ log log r + 2.50637
log log r ≥ 5.68721.

Since log 2r = (4/15) log x + log(3/4), we conclude that

gmx(r) ≥ 0.40298 log x + 3.25765
√
3/4 · x2/15 .

Recall that
 h(x) = 0.2727(log x)3/2

x1/6 + 1218 log x
x1/3 .

A simple derivative test gives us that

x ↦→ (log x + 3)/x2/15

(log(x/ log x))3/2/(x/ log x)1/6

is increasing for x ≥ 1025 (and indeed for x ≥ e28, or even well before then) and
that (1/x2/15)/((log(x/ log x))/(x/ log x)1/3) is increasing for x ≥ e7. Since

0.40298(log x + 3)
√
3/4 · x2/15 ≥ 0.2727(log(2x/ log x))3/2

(2x/ log x)1/6 ,

3.25765 − 3 · 0.40298
√
3/4 · x2/15 ≥ 1218 log(2x/ log(x))
(2x/ log(x))1/3

THE TERNARY GOLDBACH CONJECTURE IS TRUE 31

for x ≥ 1025, we are done. □

5. The ℓ2 norm and the large sieve

Our aim here is to give a bound on the ℓ2 norm of an exponential sum over
the minor arcs. While we care about an exponential sum in particular, we will
prove a result valid for all exponential sums S(α, x) = ∑
n ane(αn) with an of
prime support.
We start by adapting ideas from Ramar´e’s version of the large sieve for primes
to estimate ℓ2 norms over parts of the circle (§5.1). We are left with the task
of giving an explicit bound on the factor in Ramar´e’s work; this we do in §5.2.
As a side eﬀect, this ﬁnally gives a fully explicit large sieve for primes that is
asymptotically optimal, meaning a sieve that does not have a spurious factor of
eγ in front; this was an arguably important gap in the literature.

5.1. The ℓ2 norm over arcs: variations on the large sieve for primes.
We are trying to estimate an integral ∫
R/Z |S(α)|3dα. Rather than bound it
by |S|∞|S|2
2, we can use the fact that large (“major”) values of S(α) have to
be multiplied only by ∫
M |S(α)|2dα, where M is a union (small in measure) of
minor arcs. Now, can we give an upper bound for ∫

M |S(α)|2dα better than
|S|2
2 = ∫
R/Z |S(α)|2dα?
The ﬁrst version of [Helb] gave an estimate on that integral using a tech-
nique due to Heath-Brown, which in turn rests on an inequality of Montgomery’s
([Mon71, (3.9)]; see also, e.g., [IK04, Lem. 7.15]). The technique was commu-
nicated by Heath-Brown to the present author, who communicated it to Tao
([Tao, Lem. 4.6] and adjoining comments). We will be able to do better than
that estimate here.
The role played by Montgomery’s inequality in Heath-Brown’s method is played
here by a result of Ramar´e’s ([Ram09, Thm. 2.1]; see also [Ram09, Thm. 5.2]).
The following proposition is based on Ramar´e’s result, or rather on one possible
proof of it. Instead of using the result as stated in [Ram09], we will actually be
using elements of the proof of [Bom74, Thm. 7A], credited to Selberg. Simply
integrating Ramar´e’s inequality would give a non-trivial if slightly worse bound.

Proposition 5.1. Let {an}∞
n=1, an ∈ C, be supported on the primes. Assume
that {an} is in ℓ1 ∩ ℓ2 and that an = 0 for n ≤ √x. Let Q0 ≥ 1, δ0 ≥ 1 be such
that δ0Q2
0 ≤ x/2; set Q = √
x/2δ0 ≥ Q0. Let

(5.1) M = ⋃

q≤Q0
 ⋃

a mod q
(a,q)=1
 ( a
q − δ0r
qx , a
q + δ0r
qx
 ) .

Let S(α) = ∑
n ane(αn) for α ∈ R/Z. Then
∫

M |S(α)|
2 dα ≤ (max
q≤Q0 max
s≤Q0/q Gq(Q0/sq)
Gq(Q/sq)
 ) ∑

n |an|2,

where

(5.2) Gq(R) = ∑

r≤R
(r,q)=1
 µ2(r)
φ(r) .

32 H. A. HELFGOTT

Proof. By (5.1),

(5.3) ∫

M |S(α)|2 dα = ∑

q≤Q0
 ∫ δ0Q0
qx

− δ0Q0
qx
 ∑

a mod q
(a,q)=1
 ∣
∣
∣
∣S ( a
q + α)∣
∣
∣
∣

2 dα.

Thanks to the last equations of [Bom74, p. 24] and [Bom74, p. 25],

∑

a mod q
(a,q)=1
 ∣
∣
∣
∣S ( a
q
 )∣
∣
∣
∣

2 = 1
φ(q)
 ∑

q∗|q
(q∗,q/q∗)=1
µ2(q/q∗)=1
 q∗ · ∑∗

χ mod q∗
 ∣
∣
∣
∣
∣
∑

n anχ(n)
∣
∣
∣
∣
∣

2

for every q ≤ √x, where we use the assumption that n is prime and > √x (and
thus coprime to q) when an ̸= 0. Hence

∫

M |S(α)|2 dα = ∑

q≤Q0
 ∑

q∗|q
(q∗,q/q∗)=1
µ2(q/q∗)=1
 q∗ ∫ δ0Q0
qx

− δ0Q0
qx
 1
φ(q)
 ∣
∣
∣
∣
∣

∑

n ane(αn)χ(n)

∣
∣
∣
∣
∣
2 dα

= ∑

q∗≤Q0
 q∗

φ(q∗)
 ∑

r≤Q0/q∗

(r,q∗)=1
 µ2(r)
φ(r)
 ∫ δ0Q0
q∗rx

− δ0Q0
q∗rx
 ∑∗

χ mod q∗
 ∣
∣
∣
∣
∣

∑

n ane(αn)χ(n)

∣
∣
∣
∣
∣
2 dα

= ∑

q∗≤Q0
 q∗

φ(q∗)
 ∫ δ0Q0
q∗x

− δ0Q0
q∗x
 ∑

r≤ Q0
q∗ min(
1, δ0
|α|x )

(r,q∗)=1
 µ2(r)
φ(r)
 ∑∗

χ mod q∗
 ∣
∣
∣
∣
∣
∑

n ane(αn)χ(n)

∣
∣
∣
∣
∣

2 dα

Here |α| ≤ δ0Q0/q∗x implies (Q0/q)δ0/|α|x ≥ 1. Therefore,

(5.4) ∫

M |S(α)|
2 dα ≤ ( max
q∗≤Q0 max
s≤Q0/q∗ Gq∗(Q0/sq∗)
Gq∗(Q/sq∗)
 ) · Σ,

where

Σ = ∑

q∗≤Q0
 q∗

φ(q∗)
 ∫ δ0Q0
q∗x

− δ0Q0
q∗x
 ∑

r≤ Q
q∗ min(1, δ0
|α|x )

(r,q∗)=1
 µ2(r)
φ(r)
 ∑∗

χ mod q∗
 ∣
∣
∣
∣
∣
∑

n ane(αn)χ(n)

∣
∣
∣
∣
∣

2 dα

≤ ∑

q≤Q
 q
φ(q)
 ∑

r≤Q/q
(r,q)=1
 µ2(r)
φ(r)
 ∫ δ0Q
qrx

− δ0Q
qrx
 ∑∗

χ mod q
 ∣
∣
∣
∣
∣
∑

n ane(αn)χ(n)

∣
∣
∣
∣
∣
2 dα.

As stated in the proof of [Bom74, Thm. 7A],

χ(r)χ(n)τ (χ)cr(n) =
 qr∑

b=1
(b,qr)=1
 χ(b)e
2πin b
qr

THE TERNARY GOLDBACH CONJECTURE IS TRUE 33

for χ primitive of modulus q. Here cr(n) stands for the Ramanujan sum

cr(n) = ∑

u mod r
(u,r)=1
 e2πnu/r.

For n coprime to r, cr(n) = µ(r). Since χ is primitive, |τ (χ)| = √q. Hence, for
r ≤ √x coprime to q,

q
 ∣
∣
∣
∣
∣
∑

n ane(αn)χ(n)

∣
∣
∣
∣
∣
2 =
 ∣
∣
∣
∣
∣
∣
∣
∣
 qr∑

b=1
(b,qr)=1
 χ(b)S ( b
qr + α)
∣
∣
∣
∣
∣
∣
∣
∣

2
 .

Thus,
 Σ = ∑

q≤Q
 ∑

r≤Q/q
(r,q)=1
 µ2(r)
φ(rq)
 ∫ δ0Q
qrx

− δ0Q
qrx
 ∑∗

χ mod q
 ∣
∣
∣
∣
∣
∣
∣
∣
 qr∑

b=1
(b,qr)=1
 χ(b)S ( b
qr + α)∣
∣
∣
∣
∣
∣
∣
∣

2
 dα

≤ ∑

q≤Q
 1
φ(q)
 ∫ δ0Q
qx

− δ0Q
qx
 ∑

χ mod q
 ∣
∣
∣
∣
∣
∣
∣
∣
 q∑

b=1
(b,q)=1
 χ(b)S ( b
q + α)
∣
∣
∣
∣
∣
∣
∣
∣

2
 dα

= ∑

q≤Q
 ∫ δ0Q
qx

− δ0Q
qx
 q∑

b=1
(b,q)=1
 ∣
∣
∣
∣S ( b
q + α)∣
∣
∣
∣

2 dα.

Let us now check that the intervals (b/q − δ0Q/qx, b/q + δ0Q/qx) do not overlap.
Since Q = √
x/2δ0, we see that δ0Q/qx = 1/2qQ. The diﬀerence between two
distinct fractions b/q, b′/q′ is at least 1/qq′. For q, q′ ≤ Q, 1/qq′ ≥ 1/2qQ +
1/2Qq′. Hence the intervals around b/q and b′/q′ do not overlap. We conclude
that Σ ≤ ∫

R/Z |S(α)|
2 = ∑

n |an|
2,

and so, by (5.4), we are done. □

We will actually use Prop. 5.1 in the slightly modiﬁed form given by the fol-
lowing statement.

Proposition 5.2. Let {an}∞
n=1, an ∈ C, be supported on the primes. Assume
that {an} is in ℓ1 ∩ ℓ2 and that an = 0 for n ≤ √x. Let Q0 ≥ 1, δ0 ≥ 1 be such
that δ0Q2
0 ≤ x/2; set Q = √
x/2δ0 ≥ Q0. Let M = Mδ0,Q0 be as in (3.5).
Let S(α) = ∑
n ane(αn) for α ∈ R/Z. Then

∫

Mδ0,Q0 |S(α)|
2 dα ≤
 


 max
q≤2Q0
q even
 max
s≤2Q0/q Gq(2Q0/sq)
Gq(2Q/sq)
 


 ∑

n |an|2,

where

(5.5) Gq(R) = ∑

r≤R
(r,q)=1
 µ2(r)
φ(r) .

34 H. A. HELFGOTT

Proof. By (3.5),

∫

M |S(α)|
2 dα = ∑

q≤Q0
q odd
 ∫ δ0Q0
2qx

− δ0Q0
2qx
 ∑

a mod q
(a,q)=1
 ∣
∣
∣
∣S ( a
q + α)∣
∣
∣
∣
2 dα

+ ∑

q≤Q0
q even
 ∫ δ0Q0
qx

− δ0Q0
qx
 ∑

a mod q
(a,q)=1
 ∣
∣
∣
∣S ( a
q + α)∣
∣
∣
∣
2 dα.

We proceed as in the proof of Prop. 5.1. We still have (5.3). Hence ∫

M |S(α)|
2 dα
equals

∑

q∗≤Q0
q∗ odd
 q∗

φ(q∗)
 ∫ δ0Q0
2q∗x

− δ0Q0
2q∗x
 ∑

r≤ Q0
q∗ min(1, δ0
2|α|x )

(r,2q∗)=1
 µ2(r)
φ(r)
 ∑∗

χ mod q∗
 ∣
∣
∣
∣
∣

∑

n ane(αn)χ(n)
∣
∣
∣
∣
∣

2 dα

+ ∑

q∗≤2Q0
q∗ even
 q∗

φ(q∗)
 ∫ δ0Q0
q∗x

− δ0Q0
q∗x
 ∑

r≤ 2Q0
q∗ min(1, δ0
2|α|x )

(r,q∗)=1
 µ2(r)
φ(r)
 ∑∗

χ mod q∗
 ∣
∣
∣
∣
∣

∑

n ane(αn)χ(n)
∣
∣
∣
∣
∣

2 dα.

(The sum with q odd and r even is equal to the ﬁrst sum; hence the factor of 2
in front.) Therefore,

(5.6)
 ∫

M |S(α)|
2 dα ≤
 


 max
q∗≤Q0
q∗ odd
 max
s≤Q0/q∗ G2q∗(Q0/sq∗)
G2q∗(Q/sq∗)
 


 · 2Σ1

+
 


 max
q∗≤2Q0
q∗ even
 max
s≤2Q0/q∗ Gq∗(2Q0/sq∗)
Gq∗(2Q/sq∗)
 


 · Σ2,

where
 Σ1 = ∑

q≤Q
q odd
 q
φ(q)
 ∑

r≤Q/q
(r,2q)=1
 µ2(r)
φ(r)
 ∫ δ0Q
2qrx

− δ0Q
2qrx
 ∑∗

χ mod q
 ∣
∣
∣
∣
∣

∑

n ane(αn)χ(n)
∣
∣
∣
∣
∣

2 dα

= ∑

q≤Q
q odd
 q
φ(q)
 ∑

r≤2Q/q
(r,q)=1
r even
 µ2(r)
φ(r)
 ∫ δ0Q
qrx

− δ0Q
qrx
 ∑∗

χ mod q
 ∣
∣
∣
∣
∣
∑

n ane(αn)χ(n)

∣
∣
∣
∣
∣
2 dα.

Σ2 = ∑

q≤2Q
q even
 q
φ(q)
 ∑

r≤2Q/q
(r,q)=1
 µ2(r)
φ(r)
 ∫ δ0Q
qrx

− δ0Q
qrx
 ∑∗

χ mod q
 ∣
∣
∣
∣
∣

∑

n ane(αn)χ(n)
∣
∣
∣
∣
∣

2 dα.

The two expressions within parentheses in (5.6) are actually equal.

THE TERNARY GOLDBACH CONJECTURE IS TRUE 35

Much as before, using [Bom74, Thm. 7A], we obtain that

Σ1 ≤ ∑

q≤Q
q odd
 1
φ(q)
 ∫ δ0Q
2qx

− δ0Q
2qx
 q∑

b=1
(b,q)=1
 ∣
∣
∣
∣S ( b
q + α)∣
∣
∣
∣

2 dα,

Σ1 + Σ2 ≤ ∑

q≤2Q
q even
 1
φ(q)
 ∫ δ0Q
qx

− δ0Q
qx
 q∑

b=1
(b,q)=1
 ∣
∣
∣
∣S ( b
q + α)∣
∣
∣
∣
2 dα.

Let us now check that the intervals of integration (b/q − δ0Q/2qx, b/q + δ0Q/2qx)
(for q odd), (b/q − δ0Q/qx, b/q + δ0Q/qx) (for q even) do not overlap. Recall
that δ0Q/qx = 1/2qQ. The absolute value of the diﬀerence between two distinct
fractions b/q, b′/q′ is at least 1/qq′. For q, q′ ≤ Q odd, this is larger than 1/4qQ +
1/4Qq′, and so the intervals do not overlap. For q ≤ Q odd and q′ ≤ 2Q even (or
vice versa), 1/qq′ ≥ 1/4qQ + 1/2Qq′, and so, again the intervals do not overlap.
If q ≤ Q and q′ ≤ Q are both even, then |b/q − b′/q′| is actually ≥ 2/qq′. Clearly,
2/qq′ ≥ 1/2qQ + 1/2Qq′, and so again there is no overlap. We conclude that

2Σ1 + Σ2 ≤ ∫

R/Z |S(α)|2 = ∑

n |an|
2.
 □

5.2. Bounding the quotient in the large sieve for primes. The estimate
given by Proposition 5.1 involves the quotient

(5.7) max
q≤Q0 max
s≤Q0/q Gq(Q0/sq)
Gq(Q/sq) ,

where Gq is as in (5.2). The appearance of such a quotient (at least for s = 1) is
typical of Ramar´e’s version of the large sieve for primes; see, e.g., [Ram09]. We
will see how to bound such a quotient in a way that is essentially optimal, not
just asymptotically, but also in the ranges that are most relevant to us. (This
includes, for example, Q0 ∼ 106, Q ∼ 1015.)
As the present work shows, Ramar´e’s work gives bounds that are, in some
contexts, better than those of other large sieves for primes by a constant factor
(approaching eγ = 1.78107 . . . ). Thus, giving a fully explicit and nearly optimal
bound for (5.7) is a task of clear general relevance, besides being needed for our
main goal.
We will obtain bounds for Gq(Q0/sq)/Gq(Q/sq) when Q0 ≤ 2 · 1010, Q ≥ Q2
0.
As we shall see, our bounds will be best when s = q = 1 – or, sometimes, when
s = 1 and q = 2 instead.
Write G(R) for G1(R) = ∑
r≤R µ2(r)/φ(r). We will need several estimates for
Gq(R) and G(R). As stated in [Ram95, Lemma 3.4],

(5.8) G(R) ≤ log R + 1.4709

for R ≥ 1. By [MV73, Lem. 7],

(5.9) G(R) ≥ log R + 1.07

36 H. A. HELFGOTT

for R ≥ 6. There is also the trivial bound

(5.10)
 G(R) = ∑

r≤R
 µ2(r)
φ(r) = ∑

r≤R
 µ2(r)
r
 ∏

p|r
 (
1 − 1
p
 )−1

= ∑

r≤R
 µ2(r)
r
 ∏

p|r
 ∑

j≥1
 1
pj ≥ ∑

r≤R
 1
r > log R.

The following bound, also well-known and easy,

(5.11) G(R) ≤ q
φ(q) Gq(R) ≤ G(Rq),

can be obtained by multiplying Gq(R) = ∑r≤R:(r,q)=1 µ2(r)/φ(r) term-by-term
by q/φ(q) = ∏p|q(1 + 1/φ(p)).
We will also use Ramar´e’s estimate from [Ram95, Lem. 3.4]:

(5.12) Gd(R) = φ(d)
d
 

log R + cE + ∑

p|d
 log p
p
 

 + O∗ (7.284R−1/3f1(d))

for all d ∈ Z+ and all R ≥ 1, where

(5.13) f1(d) = ∏

p|d (1 + p−2/3)
 (

1 + p1/3 + p2/3

p(p − 1)
 )−1

and

(5.14) cE = γ + ∑

p≥2
 log p
p(p − 1) = 1.3325822 . . .

by [RS62, (2.11)].
If R ≥ 182, then

(5.15) log R + 1.312 ≤ G(R) ≤ log R + 1.354,

where the upper bound is valid for R ≥ 120. This is true by (5.12) for R ≥ 4 · 107;
we check (5.15) for 120 ≤ R ≤ 4 · 107 by a numerical computation.6 Similarly,
for R ≥ 200,

(5.16) log R + 1.661
2 ≤ G2(R) ≤ log R + 1.698
2
by (5.12) for R ≥ 1.6·108, and by a numerical computation for 200 ≤ R ≤ 1.6·108.
Write ρ = (log Q0)/(log Q) ≤ 1. We obtain immediately from (5.15) and (5.16)
that

(5.17)
 G(Q0)
G(Q) ≤ log Q0 + 1.354
log Q + 1.312
G2(Q0)
G2(Q) ≤ log Q0 + 1.698
log Q + 1.661

for Q, Q0 ≥ 200. What is hard is to approximate Gq(Q0)/Gq(Q) for q large and
Q0 small.
Let us start by giving an easy bound, oﬀ from the truth by a factor of about eγ.
(Specialists will recognize this as a factor that appears often in ﬁrst attempts at

6Using D. Platt’s implementation [Pla11] of double-precision interval arithmetic based on
Lambov’s [Lam08] ideas.

THE TERNARY GOLDBACH CONJECTURE IS TRUE 37

estimates based on either large or small sieves.) First, we need a simple explicit
lemma.

Lemma 5.3. Let m ≥ 1, q ≥ 1. Then

(5.18) ∏

p|q∨p≤m
 p
p − 1 ≤ eγ(log(m + log q) + 0.65771).

Proof. Let P = ∏p≤m∨p|q p. Then, by [RS75, (5.1)],

P ≤ q ∏

p≤m p = qe
∑p≤m log p ≤ qe
(1+ϵ0)m,

where ϵ0 = 0.001102. Now, by [RS62, (3.42)],
n
φ(n) ≤ e
γ log log n + 2.50637
log log n ≤ e
γ log log x + 2.50637
log log x

for all x ≥ n ≥ 27 (since, given a, b > 0, the function t ↦→ a + b/t is increasing on
t for t ≥ √
b/a). Hence, if qem ≥ 27,

P
φ(P) ≤ eγ log((1 + ϵ0)m + log q) + 2.50637
log(m + log q)

≤ eγ (log(m + log q) + ϵ0 + 2.50637/eγ

log(m + log q)
 ) .

Thus (5.18) holds when m + log q ≥ 8.53, since then ϵ0 + (2.50637/eγ)/ log(m +
log q) ≤ 0.65771. We verify all choices of m, q ≥ 1 with m + log q ≤ 8.53 compu-
tationally; the worst case is that of m = 1, q = 6, which give the value 0.65771
in (5.18). □

Here is the promised easy bound.

Lemma 5.4. Let Q0 ≥ 1, Q ≥ 182Q0. Let q ≤ Q0, s ≤ Q0/q, q an integer.
Then
 Gq(Q0/sq)
Gq(Q/sq) ≤ eγ log ( Q0
sq + log q) + 1.172

log Q
Q0 + 1.312 ≤ eγ log Q0 + 1.172

log Q
Q0 + 1.312 .

Proof. Let P = ∏p≤Q0/sq∨p|q p. Then

Gq(Q0/sq)GP (Q/Q0) ≤ Gq(Q/sq)

and so

(5.19) Gq(Q0/sq)
Gq(Q/sq) ≤ 1
GP (Q/Q0) .

Now the lower bound in (5.11) gives us that, for d = P, R = Q/Q0,

GP (Q/Q0) ≥ φ(P)
P G(Q/Q0).

By Lem. 5.3, P
φ(P) ≤ e
γ (
log ( Q0
sq + log q) + 0.658) .

Hence, using (5.15), we get that

(5.20) Gq(Q0/sq)
Gq(Q/sq) ≤ P/φ(P)
G(Q/Q0) ≤ eγ log ( Q0
sq + log q) + 1.172

log Q
Q0 + 1.312 ,

38 H. A. HELFGOTT

since Q/Q0 ≥ 184. Since
( Q0
sq + log q)′ = − Q0
sq2 + 1
q = 1
q
 (
1 − Q0
sq
 ) ≤ 0,

the rightmost expression of (5.20) is maximal for q = 1. □

Lemma 5.4 will play a crucial role in reducing to a ﬁnite computation the
problem of bounding Gq(Q0/sq)/Gq(Q/sq). As we will now see, we can use
Lemma 5.4 to obtain a bound that is useful when sq is large compared to Q0
– precisely the case in which asymptotic estimates such as (5.12) are relatively
weak.

Lemma 5.5. Let Q0 ≥ 1, Q ≥ 200Q0. Let q ≤ Q0, s ≤ Q0/q. Let ρ =
(log Q0)/ log Q ≤ 2/3. Then, for any σ ≥ 1.312ρ,

(5.21) Gq(Q0/sq)
Gq(Q/sq) ≤ log Q0 + σ
log Q + 1.312

holds provided that Q0
sq ≤ c(σ) · Q
(1−ρ)e−γ
0 − log q,

where c(σ) = exp(exp(−γ) · (σ − σ2/5.248 − 1.172)).

Proof. By Lemma 5.4, we see that (5.21) will hold provided that

(5.22) eγ log ( Q0
sq + log q) + 1.172 ≤ log Q
Q0 + 1.312

log Q + 1.312 · (log Q0 + σ).

The expression on the right of (5.22) equals

log Q0 + σ − (log Q0 + σ) log Q0
log Q + 1.312

= (1 − ρ)(log Q0 + σ) + 1.312ρ(log Q0 + σ)
log Q + 1.312
≥ (1 − ρ)(log Q0 + σ) + 1.312ρ2

and so (5.22) will hold provided that

eγ log ( Q0
sq + log q) + 1.172 ≤ (1 − ρ)(log Q0) + (1 − ρ)σ + 1.312ρ
2.

Taking derivatives, we see that

(1 − ρ)σ + 1.312ρ
2 − 1.172 ≥ (1 − σ
2.624
 ) σ + 1.312 ( σ
2.624
 )2 − 1.172

= σ − σ2

4 · 1.312 − 1.172.

Hence it is enough that

Q0
sq + log q ≤ e
e−γ (
(1−ρ) log Q0+σ− σ2
4·1.312 −1.172
) = c(σ) · Q(1−ρ)e−γ
0 ,

where c(σ) = exp(exp(−γ) · (σ − σ2/5.248 − 1.172)). □

THE TERNARY GOLDBACH CONJECTURE IS TRUE 39

Proposition 5.6. Let Q ≥ 20000Q0, Q0 ≥ Q0,min, where Q0,min = 105. Let
ρ = (log Q0)/ log Q. Assume ρ ≤ 0.6. Then, for every 1 ≤ q ≤ Q0 and every
s ∈ [1, Q0/q],

(5.23) Gq(Q0/sq)
Gq(Q/sq) ≤ log Q0 + c+
log Q + cE ,

where cE is as in (5.14) and c+ = 1.36.

An ideal result would have c+ instead of cE, but this is not actually possible:
error terms do exist, even if they are in reality smaller than the bound given in
(5.12); this means that a bound such as (5.23) with c+ instead of cE would be
false for q = 1, s = 1.
There is nothing special about the assumptions Q ≥ 20000Q0, Q0 ≥ 105,
(log Q0)/(log Q) ≤ 0.6: they can all be relaxed at the cost of an increase in c+.

Proof. Deﬁne errq,R so that

(5.24) Gq(R) = φ(q)
q
 

log R + cE + ∑

p|q
 log p
p
 

 + errq,R .

Then (5.23) will hold if

(5.25)
 log Q0
sq + cE + ∑

p|q
 log p
p + q
φ(q) err
q, Q0
sq

≤
 

log Q
sq + cE + ∑

p|q
 log p
p + q
φ(q) err
q, Q
sq
 

 log Q0 + c+
log Q + cE .

This, in turn, happens if


log sq − ∑

p|q
 log p
p
 

 (
1 − log Q0 + c+
log Q + cE
 ) + c+ − cE

≥ q
φ(q)
 (
err
q, Q0
sq − log Q0 + c+
log Q + cE err
q, Q
sq
 ) .

Deﬁne
 ω(ρ) = log Q0,min + c+
1
ρ log Q0,min + cE = ρ + c+ − ρcE
1
ρ log Q0,min + cE .

Then ρ ≤ (log Q0 + c+)/(log Q + cE) ≤ ω(ρ) (because c+ ≥ ρcE). We conclude
that (5.25) (and hence (5.23)) holds provided that
(5.26)

(1−ω(ρ))
 

log sq − ∑

p|q
 log p
p
 

+c∆ ≥ q
φ(q)
 (err
q, Q0
sq +ω(ρ) max (
0, − err
q, Q
sq
 )) ,

where c∆ = c+ − cE. Note that 1 − ω(ρ) > 0.
First, let us give some easy bounds on the error terms; these bounds will yield
upper bounds for s. By (5.8) and (5.11),

errq,R ≤ φ(q)
q
 

log q − ∑

p|q
 log p
p + (1.4709 − cE)





40 H. A. HELFGOTT

for R ≥ 1; by (5.15) and (5.11),

errq,R ≥ − φ(q)
q
 

∑

p|q
 log p
p + (cE − 1.312)





for R ≥ 182. Therefore, the right side of (5.26) is at most

log q − (1 − ω(ρ)) ∑

p|q
 log p
p + ((1.4709 − cE) + ω(ρ)(cE − 1.312)),

and so (5.26) holds provided that

(5.27) (1 − ω(ρ)) log sq ≥ log q + (1.4709 − cE) + ω(ρ)(cE − 1.312) − c∆.

We will thus be able to assume from now on that (5.27) does not hold, or, what
is the same, that

(5.28) sq < (cρ,2q)
 1
1−ω(ρ)

holds, where cρ,2 = exp((1.4709 − cE) + ω(ρ)(cE − 1.312) − c∆).
What values of R = Q0/sq must we consider for q given? First, by (5.28), we
can assume R > Q0,min/(cρ,2q)1/(1−ω(ρ)). We can also assume

(5.29) R > c(c+) · max(Rq, Q0,min)
(1−ρ)e−γ − log q

for c(c+) is as in Lemma 5.5, since all smaller R are covered by that Lemma.
Clearly, (5.29) implies that

R1−τ > c(c+) · qτ − log q
Rτ > c(c+)qτ − log q,

where τ = (1 − ρ)e−γ, and also that R > c(c+)Q(1−ρ)e−γ
0,min − log q. Iterating, we
obtain that we can assume that R > ϖ(q), where

(5.30) ϖ(q) = max
 (

ϖ0(q), c(c+)Q
τ
0,min − log q, Q0,min

(cρ,2q)
 1
1−ω(ρ)
 )

and
 ϖ0(q) =
 




(c(c+)qτ − log q

(c(c+)qτ −log q) τ
1−τ
 ) 1
1−τ if c(c+)qτ > log q + 1,

0 otherwise.

Looking at (5.26), we see that it will be enough to show that, for all R satisfying
R > ϖ(q), we have

(5.31) errq,R +ω(ρ) max (0, − errq,tR) ≤ φ(q)
q κ(q)

for all t ≥ 20000, where

κ(q) = (1 − ω(ρ))
 

log q − ∑

p|q
 log p
p
 

 + c∆.

Ramar´e’s bound (5.12) implies that

(5.32) | errq,R | ≤ 7.284R−1/3f1(q),

with f1(q) as in (5.13), and so

errq,R +ω(ρ) max (0, − errq,tR) ≤ (1 + βρ) · 7.284R−1/3f1(q),

THE TERNARY GOLDBACH CONJECTURE IS TRUE 41

where βρ = ω(ρ)/200001/3. This is enough when

(5.33) R ≥ λ(q) = ( q
φ(q) 7.284(1 + βρ)f1(q)
κ(q)
 )3 .

It remains to do two things. First, we have to compute how large q has to be for
ϖ(q) to be guaranteed to be greater than λ(q). (For such q, there is no checking
to be done.) Then, we check the inequality (5.31) for all smaller q, letting R
range through the integers in [ϖ(q), λ(q)]. We bound errq,tR using (5.32), but we
compute errq,R directly.
How large must q be for ϖ(q) > λ(q) to hold? We claim that ϖ(q) > λ(q)
whenever q ≥ 2.2 · 1010. Let us show this.
It is easy to see that (p/(p−1))·f1(p) and p → (log p)/p are decreasing functions
of p for p ≥ 3; moreover, for both functions, the value at p ≥ 7 is smaller than
for p = 2. Hence, we have that, for q < ∏p≤p0 p, p0 a prime,

(5.34) κ(q) ≥ (1 − ω(ρ))
 (
log q − ∑

p<p0
 log p
p
 )
 + c∆

and

(5.35) λ(q) ≤
 

 ∏

p<p0
 p
p − 1 · 7.284(1 + βρ) ∏p<p0 f1(p)

(1 − ω(ρ)) (log q − ∑p<p0 log p
p ) + c∆
 



3
 .

If we also assume that 2 · 3 · 5 · 7 ∤ q, we obtain

(5.36) κ(q) ≥ (1 − ω(ρ))
 



log q − ∑

p<p0
p̸=7
 log p
p
 



 + c∆

and

(5.37) λ(q) ≤
 



 ∏

p<p0
p̸=7
 p
p − 1 · 7.284(1 + βρ) ∏p<p0,p̸=7 f1(p)

(1 − ω(ρ)) (log q − ∑
p<p0,p̸=7 log p
p ) + c∆
 





3

for q < ∏p≤p0. (We are taking out 7 because it is the “least helpful” prime to
omit among all primes from 2 to 7, again by the fact that (p/(p − 1)) · f1(p) and
p → (log p)/p are decreasing functions for p ≥ 3.)
We know how to give upper bounds for the expression on the right of (5.35).
The task is in essence simple: we can base our bounds on the classic explicit work
in [RS62], except that we also have to optimize matters so that they are close to
tight for p1 = 29, p1 = 31 and other low p1.
By [RS62, (3.30)] and a numerical computation for 29 ≤ p1 ≤ 43,
∏

p≤p1
 p
p − 1 < 1.90516 log p1

for p1 ≥ 29. Since ω(ρ) is increasing on ρ and we are assuming ρ ≤ 0.6, Q0,min =
100000, ω(ρ) ≤ 0.627312, βρ ≤ 0.023111.

42 H. A. HELFGOTT

For x > a, where a > 1 is any constant, we obviously have
∑

a<p≤x log (1 + p−2/3) ≤ ∑

a<p≤x(log p) p−2/3

log a .

by Abel summation (see (6.3)) and the estimates [RS62, (3.32)] for θ(x) =∑p≤x log p,

∑

a<p≤x(log p)p
−2/3 = (θ(x) − θ(a))x
− 2
3 − ∫ x

a (θ(u) − θ(a)) (− 2
3 u
− 5
3 ) du

≤ (1.01624x − θ(a))x− 2
3 + 2
3
 ∫ x

a (1.01624u − θ(a)) u
− 5
3 du

= (1.01624x − θ(a))x− 2
3 + 2 · 1.01624(x1/3 − a
1/3) + θ(a)(x−2/3 − a
−2/3)

= 3 · 1.01624 · x1/3 − (2.03248a
1/3 + θ(a)a
−2/3).

We conclude that ∑
104<p≤x log(1 + p−2/3) ≤ 0.33102x1/3 − 7.06909 for x > 104.
Since ∑p≤104 log p ≤ 10.09062, this means that

∑

p≤x log(1 + p
−2/3) ≤ (0.33102 + 10.09062 − 7.06909
104/3
 ) x1/3 ≤ 0.47126x1/3

for x > 104; a direct computation for all x prime between 29 and 104 then
conﬁrms that ∑

p≤x log(1 + p−2/3) ≤ 0.74914x1/3

for all x ≥ 29. Thus,

∏

p≤x f1(p) ≤ e
∑p≤x log(1+p−2/3)
∏p≤29 (1 + p1/3+p2/3
p(p−1) ) ≤ e0.74914x1/3

6.62365

for x ≥ 29. Finally, by [RS62, (3.24)], ∑p≤p1 log p
p < log p1.
We conclude that, for q < ∏p≤p0 p0, p0 a prime, and p1 the prime immediately
preceding p0,

(5.38) λ(q) ≤
 



1.90516 log p1 · 7.45235 · ( e0.74914p1/3
1
6.62365
 )

0.37268(log q − log p1) + 0.02741
 




3

≤ 190.272(log p1)3e2.24742p
1/3
1
(log q − log p1 + 0.07354)3 .

It is clear from (5.30) that ϖ(q) is increasing as soon as

q ≥ max(Q0,min, Q
1−ω(ρ)
0,min /cρ,2)

and c(c+)qτ > log q + 1, since then ϖ0(q) is increasing and ϖ(q) = ϖ0(q). Here it
is useful to recall that cρ,2 ≥ exp(1.4709−c+), and to note that c(c+)qτ −(log q+1)
is increasing for q ≥ 1/(τ · c(c+))1/τ ; we see also that 1/(τ · c(c+))1/τ ≤ 1/((1 −
0.6)e−γc(c+))1/((1−0.6)e−γ ) for ρ ≤ 0.6. A quick computation for our value of c+
makes us conclude that q > 1.12Q0,min = 112000 is a suﬃcient condition for ϖ(q)
to be equal to ϖ0(q) and for ϖ0(q) to be increasing.

THE TERNARY GOLDBACH CONJECTURE IS TRUE 43

Since (5.38) is decreasing on q for p1 ﬁxed, and ϖ0(q) is decreasing on ρ and
increasing on q, we set ρ = 0.6 and check that then

ϖ0 (2.2 · 10
10) ≥ 846.765,

whereas, by (5.38),
 λ(2.2 · 10
10) ≤ 838.227 < 846.765;

this is enough to ensure that λ(q) < ϖ0(q) for 2.2 · 1010 ≤ q < ∏p≤31 p.
Let us now give some rough bounds that will be enough to cover the case
q ≥ ∏p≤31 p. First, as we already discussed, ϖ(q) = ϖ0(q) and, since c(c+)qτ >
log q + 1,

(5.39) ϖ0(q) ≥ (c(c+)qτ − log q) 1
1−τ ≥ (0.911q0.224 − log q)
1.289 ≥ q0.2797

by q ≥ ∏p≤31 p. We are in the range ∏p≤p1 p ≤ q ≤ ∏p≤p0 p, where p1 < p0
are two consecutive primes with p1 ≥ 31. By [RS62, (3.16)] and a computation
for 31 ≤ q < 200, we know that log q ≥ ∏p≤p1 log p ≥ 0.8009p1. By (5.38) and
(5.39), it follows that we just have to show that

e0.224t > 190.272(log t)3e2.24742t1/3

(0.8009t − log t + 0.07354)3

for t ≥ 31. Now, t ≥ 31 implies 0.8009t − log t + 0.07354 ≥ 0.6924t, and so, taking
logarithms we see that we just have to verify

(5.40) 0.224t − 2.24742t1/3 > 3 log log t − 3 log t + 6.3513

for t ≥ 31, and, since the left side is increasing and the right side is decreasing
for t ≥ 31, this is trivial to check.
We conclude that ϖ(q) > λ(q) whenever q ≥ 2.2 · 1010.
It remains to see how we can relax this assumption if we assume that 2·3·5·7 ∤ q.
We repeat the same analysis as before, using (5.36) and (5.37) instead of (5.34)
and (5.35). For p1 ≥ 29,

∏

p≤p1
p̸=7
 p
p − 1 < 1.633 log p1, ∏

p≤p1
p̸=7
 f1(p) ≤ e0.74914x1/3−log(1+7−2/3)

5.8478 ≤ e0.74914x1/3

7.44586

and ∑
p≤p1:p̸=7(log p)/p < log p1 − (log 7)/7. So, for q < ∏p≤p0:p̸=7 p, and p1 ≥ 29
the prime immediately preceding p0,

λ(q) ≤
 



1.633 log p1 · 7.45235 · ( e
0.74914p1/3
1
7.44586
 )

0.37268 (log q − log p1 + log 7
7 ) + 0.02741
 




3

≤ 84.351(log p1)3e2.24742p
1/3
1
(log q − log p1 + 0.35152)3 .

Thus we obtain, just like before, that

ϖ0(3.3 · 10
9) ≥ 477.465, λ(3.3 · 10
9) ≤ 475.513 < 477.465.

We also check that ϖ0(q0) ≥ 916.322 is greater than λ(q0) ≤ 429.731 for q0 =∏p≤31:p̸=7 p. The analysis for q ≥ ∏p≤37:p̸=7 p is also just like before: since

44 H. A. HELFGOTT

log q ≥ 0.8009p1 − log 7, we have to show that

e0.224t

7 > 84.351(log t)3e2.24742t1/3

(0.8009t − log t + 0.07354)3

for t ≥ 37, and that, in turn, follows from

0.224t − 2.24742t
1/3 > 3 log log t − 3 log t + 6.74849,

which we check for t ≥ 37 just as we checked (5.40).
We conclude that ϖ(q) > λ(q) if q ≥ 3.3 · 109 and 210 ∤ q.
Computation. Now, for q < 3.3·109 (and also for 3.3·109 ≤ q < 2.2·1010, 210|q),
we need to check that the maximum mq,R,1 of errq,R over all ϖ(q) ≤ R < λ(q)
satisﬁes (5.31). Note that there is a term errq,tR in (5.31); we bound it using
(5.32).
Since log R is increasing on R and Gq(R) depends only on ⌊R⌋, we can tell
from (5.24) that, since we are taking the maximum of errq,R, it is enough to check
integer values of R. We check all integers R in [ϖ(q), λ(q)) for all q < 3.3 · 109

(and all 3.3 · 109 ≤ q < 2.2 · 1010, 210|q) by an explicit computation.7 □

Finally, we have the trivial bound

(5.41) Gq(Q0/sq)
Gq(Q/sq) ≤ 1,

which we shall use for Q0 close to Q.

Corollary 5.7. Let {an}∞
n=1, an ∈ C, be supported on the primes. Assume that
{an} is in ℓ1 ∩ ℓ2 and that an = 0 for n ≤ √
x. Let Q0 ≥ 105, δ0 ≥ 1 be such that
(20000Q0)2 ≤ x/2δ0; set Q = √
x/2δ0.
Let S(α) = ∑
n ane(αn) for α ∈ R/Z. Let M as in (5.1). Then, if Q0 ≤ Q0.6,
∫

M |S(α)|
2 dα ≤ log Q0 + c+
log Q + cE
 ∑

n |an|2,

where c+ = 1.36 and cE = γ + ∑
p≥2(log p)/(p(p − 1)) = 1.3325822 . . . .
Let Mδ0,Q0 as in (3.5). Then, if (2Q0) ≤ (2Q)0.6,
∫

Mδ0,Q0 |S(α)|
2 dα ≤ log 2Q0 + c+
log 2Q + cE
 ∑

n |an|2.

Here, of course, ∫
R/Z |S(α)|2 dα = ∑n |an|2 (Plancherel). If Q0 > Q0.6, we will
use the trivial bound

(5.42) ∫

Mδ0,r |S(α)|
2 dα ≤ ∫

R/Z |S(α)|
2 dα = ∑

n |an|
2.

Proof. Immediate from Prop. 5.1, Prop. 5.2 and Prop. 5.6. □

7This is by far the heaviest computation in the present paper, though it is still rather minor
(about two weeks of computing on a single core of a fairly new (2010) desktop computer carrying
out other tasks as well; this is next to nothing compared to the computations in [Plab], or even
those in [HP]). For the applications in the present paper, we could have assumed ρ ≤ 8/15,
and that would have reduced computation time drastically; the lighter assumption ρ ≤ 0.6 was
made with views to general applicability in the future. As elsewhere in this section, numerical
computations were carried out by the author in C; all ﬂoating-point operations used D. Platt’s
interval arithmetic package.

THE TERNARY GOLDBACH CONJECTURE IS TRUE 45

Obviously, one can also give a statement derived from Prop. 5.1; the resulting
bound is ∫

M |S(α)|
2dα ≤ log Q0 + c+
log Q + cE
 ∑

n |an|2,

where M is as in (5.1).
We also record the large-sieve form of the result.

Corollary 5.8. Let N ≥ 1. Let {an}∞
n=1, an ∈ C, be supported on the integers
n ≤ N . Let Q0 ≥ 105, Q ≥ 20000Q0. Assume that an = 0 for every n for which
there is a p ≤ Q dividing n.
Let S(α) = ∑
n ane(αn) for α ∈ R/Z. Then, if Q0 ≤ Q0.6,

∑

q≤Q0
 ∑

a mod q
(a,q)=1
 |S(a/q)|
2 dα ≤ log Q0 + c+
log Q + cE · (N + Q2) ∑

n |an|2,

where c+ = 1.36 and cE = γ + ∑
p≥2(log p)/(p(p − 1)) = 1.3325822 . . . .

Proof. Proceed as Ramar´e does in the proof of [Ram09, Thm. 5.2], with Kq =
{a ∈ Z/qZ : (a, q) = 1} and un = an); in particular, apply [Ram09, Thm. 2.1].
The proof of [Ram09, Thm. 5.2] shows that

∑

q≤Q0
 ∑

a mod q
(a,q)=1
 |S(a/q)|2 dα ≤ max
q≤Q0 Gq(Q0)
Gq(Q) · ∑

q≤Q0
 ∑

a mod q
(a,q)=1
 |S(a/q)|
2 dα.

Now, instead of using the easy inequality Gq(Q0)/Gq(Q) ≤ G1(Q0)/G1(Q/Q0),
use Prop. 5.6. □

* * *

It would seem desirable to prove a result such as Prop. 5.6 (or Cor. 5.7, or
Cor. 5.8). without computations and with conditions that are as weak as possible.
Since, as we said, we cannot make c+ equal to cE, and since c+ does have to
increase when the conditions are weakened (as is shown by computations; this is
not an artifact of our method of proof) the right goal might be to show that the
maximum of Gq(Q0/sq)/Gq(Q/sq) is reached when s = q = 1.
However, this is also untrue without conditions. For instance, for Q0 = 2 and
Q large, the value of Gq(Q0/q)/Gq(Q/q) at q = 2 is larger than at q = 1: by
(5.12),

G2 ( Q0
2 )

G2 ( Q
2 ) ∼ 1

1
2 (log Q
2 + cE + log 2
2 ) = 2

log Q + cE − log 2
2 > 2
log Q + cE ∼ G(Q0)
G(Q) .

The same holds for Q0 = 3, Q0 = 5 or Q0 = 30, say, since in all these cases
Q0/φ(Q0) > log Q0. Thus, it is clear that, at the very least, a lower bound on Q0
is needed as a condition. This also dims the hopes somewhat for a combinatorial
proof of Gq(Q0/q)G(Q) ≤ Gq(Q/q)G(Q0); at any rate, while such a proof would
be welcome, it could not be extremely straightforward, since there are terms in
Gq(Q0/q)G(Q) that do not appear in Gq(Q/q)G(Q0).

46 H. A. HELFGOTT

6. The integral over the minor arcs

The time has come to bound the part of our triple-product integral (3.3) that
comes from the minor arcs m ⊂ R/Z. We have an ℓ∞ estimate (from Prop. 4.5,
based on [Helb]) and an ℓ2 estimate (from §5). Now we must put them together.
There are two ways in which we must be careful. A trivial bound of the form
ℓ3
3 = ∫ |S(α)|3dα ≤ ℓ2
2 · ℓ∞ would introduce a fatal factor of log x coming from ℓ2.
We avoid this by using the fact that we have ℓ2 estimates over Mδ0,Q0 for varying
Q0.
We must also remember to substract the major-arc contribution from our es-
timate for Mδ0,Q0; this is why we were careful to give a lower bound in Lem. 3.1,
as opposed to just the upper bound (3.28).

6.1. Putting together ℓ2 bounds over arcs and ℓ∞ bounds. Let us start
with a simple lemma – essentially a way to obtain upper bounds by means of
summation by parts.

Lemma 6.1. Let f, g : {a, a + 1, . . . , b} → R+
0 , where a, b ∈ Z+. Assume that,
for all x ∈ [a, b],

(6.1) ∑

a≤n≤x f (n) ≤ F (x),

where F : [a, b] → R is continuous, piecewise diﬀerentiable and non-decreasing.
Then
 b∑

n=a f (n) · g(n) ≤ (max
n≥a g(n)) · F (a) + ∫ b

a (max
n≥u g(n)) · F ′(u)du.

Proof. Let S(n) = ∑n
m=a f (m). Then, by partial summation,

(6.2)
 b∑

n=a f (n) · g(n) ≤ S(b)g(b) +
 b−1∑

n=a S(n)(g(n) − g(n + 1)).

Let h(x) = maxx≤n≤b g(n). Then h is non-increasing. Hence (6.1) and (6.2)
imply that
 b∑

n=a f (n)g(n) ≤
 b∑

n=a f (n)h(n)

≤ S(b)h(b) +
 b−1∑

n=a S(n)(h(n) − h(n + 1))

≤ F (b)h(b) +
 b−1∑

n=a F (n)(h(n) − h(n + 1)).

In general, for αn ∈ C, A(x) = ∑
a≤n≤x αn and F continuous and piecewise
diﬀerentiable on [a, x],

(6.3) ∑

a≤n≤x αnF (x) = A(x)F (x) − ∫ x

a A(u)F ′(u)du. (Abel summation)

THE TERNARY GOLDBACH CONJECTURE IS TRUE 47

Applying this with αn = h(n)−h(n+1) and A(x) = ∑
a≤n≤x αn = h(a)−h(⌊x⌋+
1), we obtain

b−1∑

n=a
F (n)(h(n) − h(n + 1))

= (h(a) − h(b))F (b − 1) − ∫ b−1

a (h(a) − h(⌊u⌋ + 1))F ′(u)du

= h(a)F (a) − h(b)F (b − 1) + ∫ b−1

a h(⌊u⌋ + 1)F ′(u)du

= h(a)F (a) − h(b)F (b − 1) + ∫ b−1

a h(u)F ′(u)du

= h(a)F (a) − h(b)F (b) + ∫ b

a h(u)F ′(u)du,

since h(⌊u⌋ + 1) = h(u) for u /∈ Z. Hence

b∑

n=a f (n)g(n) ≤ h(a)F (a) + ∫ b

a h(u)F ′(u)du.
 □

We will now see our main application of Lemma 6.1. We have to bound an in-
tegral of the form ∫

Mδ0,r |S1(α)|2|S2(α)|dα, where Mδ0,r is a union of arcs deﬁned

as in (3.5). Our inputs are (a) a bound on integrals of the form ∫

Mδ0,r |S1(α)|2dα,
(b) a bound on |S2(α)| for α ∈ (R/Z) \ Mδ0,r. The input of type (a) is what we
derived in §5.1 and §5.2; the input of type (b) is a minor-arcs bound, and as such
is the main subject of [Helb].

Proposition 6.2. Let S1(α) = ∑
n ane(αn), an ∈ C, {an} in L1. Let S2 :
R/Z → C be continuous. Deﬁne Mδ0,r as in (3.5).
Let r0 be a positive integer not greater than r1. Let H : [r0, r1] → R+ be a
continuous, piecewise diﬀerentiable, non-decreasing function such that

(6.4) 1
∑ |an|2
 ∫

Mδ0,r+1 |S1(α)|2dα ≤ H(r)

for some δ0 ≤ x/2r2
1 and all r ∈ [r0, r1]. Assume, moreover, that H(r1) = 1. Let
g : [r0, r1] → R+ be a non-increasing function such that

(6.5) max
α∈(R/Z)\Mδ0,r |S2(α)| ≤ g(r)

for all r ∈ [r0, r1] and δ0 as above.
Then

(6.6)
 1
∑
n |an|2
 ∫

(R/Z)\Mδ0,r0 |S1(α)|2|S2(α)|dα

≤ g(r0) · (H(r0) − I0) + ∫ r1

r0 g(r)H ′(r)dr,

where

(6.7) I0 = 1
∑
n |an|2
 ∫

Mδ0,r0 |S1(α)|
2dα.

48 H. A. HELFGOTT

The condition δ0 ≤ x/2r2
1 is there just to ensure that the arcs in the deﬁnition
of Mδ0,r do not overlap for r ≤ r1.

Proof. For r0 ≤ r < r1, let

f (r) = 1
∑
n |an|2
 ∫

Mδ0,r+1\Mδ0,r |S1(α)|
2dα.

Let f (r1) = 1
∑
n |an|2
 ∫

(R/Z)\Mδ0,r1 |S1(α)|2dα.

Then, by (6.5),
 1
∑
n |an|2
 ∫

(R/Z)\Mδ0,r0 |S1(α)|2|S2(α)|dα ≤
 r1∑

r=r0 f (r)g(r).

By (6.4),

(6.8)
 ∑

r0≤r≤x f (r) = 1
∑n |an|2
 ∫

Mδ0,x+1\Mδ0,r0 |S1(α)|
2dα

=
 ( 1
∑
n |an|2
 ∫

Mδ0,x+1 |S1(α)|2dα
)
 − I0 ≤ H(x) − I0

for x ∈ [r0, r1). Moreover,
∑

r0≤r≤r1 f (r) = 1
∑
n |an|2
 ∫

(R/Z)\Mδ0,r0 |S1(α)|
2

=
 ( 1
∑
n |an|2
 ∫

R/Z |S1(α)|
2)
 − I0 = 1 − I0 = H(r1) − I0.

We let F (x) = H(x) − I0 and apply Lemma 6.1 with a = r0, b = r1. We obtain
that r1∑

r=r0 f (r)g(r) ≤ (max
r≥r0 g(r))F (r0) + ∫ r1

r0 (max
r≥u g(r))F ′(u) du

≤ g(r0)(H(r0) − I0) + ∫ r1

r0 g(u)H ′(u) du.
 □

6.2. The minor-arc total. We now apply Prop. 6.2. Inevitably, the main state-
ment involves some integrals that will have to be evaluated at the end of the
section.

Theorem 6.3. Let x ≥ 1025 · κ, where κ ≥ 1. Let

(6.9) Sη(α, x) = ∑

n Λ(n)e(αn)η(n/x).

Let η∗(t) = (η2 ∗M ϕ)(κt), where η2 is as in (4.10) and ϕ : [0, ∞) → [0, ∞) is
continuous and in ℓ1. Let η+ : [0, ∞) → [0, ∞) be a bounded, piecewise diﬀeren-
tiable function with limt→∞ η+(t) = 0. Let Mδ0,r be as in (3.5) with δ0 = 8. Let
105 ≤ r0 < r1, where r1 = (3/8)(x/κ)4/15.
Let Zr0 = ∫

(R/Z)\M8,r0 |Sη∗(α, x)||Sη+(α, x)|2dα.

THE TERNARY GOLDBACH CONJECTURE IS TRUE 49

Then
 Zr0 ≤
 (√ |ϕ|1x
κ (M + T ) + √
Sη∗(0, x) · E
)2 ,

where

(6.10)
 S = ∑

p>√x(log p)2η2
+(n/x),

T = Cϕ,3(log x) · (S − (√J − √E)
2),

J = ∫

M8,r0 |Sη+(α, x)|
2 dα,

E = ((Cη+,0 + Cη+,2) log x + (2Cη+,0 + Cη+,1)
) · x1/2,

(6.11)
 Cη+,0 = 0.7131 ∫ ∞

0
 1
√t (sup
r≥t η+(r))
2dt,

Cη+,1 = 0.7131 ∫ ∞

1
 log t
√t (sup
r≥t η+(r))
2dt,

Cη+,2 = 0.51942|η+|
2
∞,

Cϕ,3(K) = 1.04488
|ϕ|1
 ∫ 1/K

0 |ϕ(w)|dw

and
(6.12)

M = g(r0) · ( log(r0 + 1) + c+

log √x + c− · S − (√J − √E)
2)

+
 ( 2
log x + 2c−
 ∫ r1

r0
 g(r)
r dr +
 ( 7
15 + −2.14938 + 8
15 log κ
log x + 2c−
 )
 g(r1)

)
 · S

where g(r) = gx/κ,ϕ(r) with K = log(x/κ)/2 (see (4.20)), c+ = 2.3912 and
c− = 0.6294.

Proof. Let y = x/κ. Let Q = (3/4)y2/3, as in [Helb, Main Thm.] (applied with
y instead of x). Let α ∈ (R/Z) \ M8,r, where r ≥ r0 and y is used instead of x
to deﬁne M8,r (see (3.5)). There exists an approximation 2α = a/q + δ/y with
q ≤ Q, |δ|/y ≤ 1/qQ. Thus, α = a′/q′ + δ/2y, where either a′/q′ = a/2q or
a′/q′ = (a + q)/2q holds. (In particular, if q′ is odd, then q′ = q; if q′ is even,
then q′ may be q or 2q.)
There are three cases:

(1) q ≤ r. Then either (a) q′ is odd and q′ ≤ r or (b) q′ is even and q′ ≤ 2r.
Since α is not in M8,r, then, by deﬁnition (3.5), |δ|/2y ≥ δ0r/2qy, and so
|δ| ≥ δ0r/q = 8r/q. In particular, |δ| ≥ 8.
Thus, by Prop. 4.5,

(6.13) |Sη∗(α, x)| = |Sη2∗M φ(α, y)| ≤ gy,ϕ
 ( |δ|
8 q) · |ϕ|1y ≤ gy,ϕ(r) · |ϕ|1y,

where we use the fact that g(r) is a decreasing function (Lemma 4.6).

50 H. A. HELFGOTT

(2) r < q ≤ y1/3/6. Then, by Prop. 4.5 and Lemma 4.6,
(6.14)

|Sη∗(α, x)| = |Sη2∗M φ(α, y)| ≤ gy,ϕ
 (max ( |δ|
8 , 1
) q) · |ϕ|1y ≤ gy,ϕ(r) · |ϕ|1y.

(3) q > y1/3/6. Again by Prop. 4.5,

(6.15) |Sη∗(α, x)| = |Sη2∗M φ(α, y)| ≤ (h ( y
K
 ) + Cϕ,3(K)
) |ϕ|1y,

where h(x) is as in (4.16). (Note that Cϕ,3(K), as in (6.11), equals
Cϕ,0,K/|φ|1, where Cϕ,0,K is as in (4.22).) We set K = (log y)/2. Since
y = x/κ ≥ 1025, it follows that y/K = 2y/ log y > 2.16 · 1020.

Let
 r1 = 3
8 y4/15, g(r) =
 {
gx,ϕ(r) if r ≤ r1,
gx,ϕ(r1) if r > r1.

By Lemma 4.6, g(r) is a decreasing function for r ≥ 175; moreover, by Lemma
4.7, gy,φ(r1) ≥ h(2y/ log y), where h is as in (4.16), and so g(r) ≥ h(2y/ log y) for
all r ≥ r0 > 175. Thus, we have shown that

(6.16) |Sη∗(y, α)| ≤ (
g(r) + Cϕ,3
 ( log y
2
 )) · |ϕ|1y

for all α ∈ (R/Z) \ M8,r.
We ﬁrst need to undertake the fairly dull task of getting non-prime or small n
out of the sum deﬁning Sη+(α, x). Write

S1,η+(α, x) = ∑

p>√x(log p)e(αp)η+(p/x),

S2,η+(α, x) = ∑

n non-prime
n>√x
 Λ(n)e(αn)η+(n/x) + ∑

n≤√x Λ(n)e(αn)η+(n/x).

By the triangle inequality (with weights |Sη+(α, x)|),
√∫

(R/Z)\M8,r0 |Sη∗(α, x)||Sη+(α, x)|2dα

≤
 2∑

j=1
 √∫

(R/Z)\M8,r0 |Sη∗(α, x)||Sj,η+(α, x)|2dα.

Clearly,
∫

(R/Z)\M8,r0 |Sη∗(α, x)||S2,η+(α, x)|
2dα

≤ max
α∈R/Z |Sη∗(α, x)| · ∫

R/Z |S2,η+(α, x)|2dα

≤
 ∞∑

n=1 Λ(n)η∗(n/x) ·
 

 ∑

n non-prime Λ(n)2η+(n/x)2 + ∑

n≤√x Λ(n)2η+(n/x)2


 .

THE TERNARY GOLDBACH CONJECTURE IS TRUE 51

Let η+(z) = supt≥z η+(t). Since η+(t) tends to 0 as t → ∞, so does η+. By
[RS62, Thm. 13], partial summation and integration by parts,
∑

n non-prime
Λ(n)2η+(n/x)2 ≤ ∑

n non-prime Λ(n)
2η+(n/x)
2

≤ − ∫ ∞

1
 



 ∑

n≤t
n non-prime
 Λ(n)
2




 (η+2(t/x))′ dt

≤ − ∫ ∞

1 (log t) · 1.4262
√t (η+2(t/x))′ dt

≤ 0.7131 ∫ ∞

1
 log e2t
√t · η+2 ( t
x
 ) dt

=
 (
0.7131 ∫ ∞

1/x
 2 + log tx
√t η+2(t)dt

) √x,

while, by [RS62, Thm. 12],
∑

n≤
√x Λ(n)2η+(n/x)2 ≤ 1
2 |η+|
2
∞(log x) ∑

n≤
√x Λ(n)

≤ 0.51942|η+|
2
∞ · √x log x.

This shows that
∫

(R/Z)\M8,r0 |Sη∗(α, x)||S2,η+(α, x)|
2dα ≤
 ∞∑

n=1 Λ(n)η∗(n/x) · E = Sη∗(0, x) · E,

where E is as in (6.10).
It remains to bound

(6.17) ∫

(R/Z)\M8,r0 |Sη∗(α, x)||S1,η+(α, x)|2dα.

We wish to apply Prop. 6.2. Corollary 5.7 gives us an input of type (6.4); we have
just derived a bound (6.16) that provides an input of type (6.5). More precisely,
by Corollary 5.7, (6.4) holds with

H(r) =
 { log(r+1)+c+

log √x+c− if r < r1,

1 if r ≥ r1,

where c+ = 2.3912 > log 2 + 1.698 and c− = 0.6294 < log(1/
√2 · 8) + log 2 +
1.3225822. (We can apply Corollary 5.7 because (2(r1 + 1)) ≤ ((4/9)x4/15 + 2) ≤
(2
√
x/16)0.6 for x ≥ 1025 (or even for x ≥ 1000).) Since r1 = (3/8)y4/15 and
x ≥ 1025 · κ,

lim
r→r+
1 H(r) − lim
r→r−
1 H(r) = 1 − log((3/8)(x/κ)4/15 + 1) + c+

log √x + c−

≤ 1 −
 ( 4/15
1/2 + log 3
8 + c+ − 4
15 log κ − 8
15 c−

log √x + c−
 )

≤ 7
15 + −2.14938 + 8
15 log κ
log x + 2c− .

52 H. A. HELFGOTT

We also have (6.5) with

(6.18) (
g(r) + Cϕ,3
 ( log y
2
 )) · |ϕ|1y

instead of g(r) (by (6.16)). Here (6.18) is a decreasing function of r because g(r)
is, as we already checked. Hence, Prop. 6.2 gives us that (6.17) is at most

(6.19) g(r0)·(H(r0) − I0) + (1 − I0) · Cϕ,3
 ( log y
2
 )

+ 1
log √x + c−
 ∫ r1

r0
 g(r)
r + 1 dr + 0.4156g(r1)

times |ϕ|1y · ∑
p>√x(log p)2η2
+(p/x), where

(6.20) I0 = 1
∑
p>√x(log p)2η2
+(n/x)
 ∫

M8,r0 |S1,η+(α, x)|
2 dα.

By the triangle inequality,
√∫

M8,r0 |S1,η+(α, x)|2 dα =
 √∫

M8,r0 |Sη+(α, x) − S2,η+(α, x)|2 dα

≥
 √∫

M8,r0 |Sη+(α, x)|2 dα −
 √∫

M8,r0 |S2,η+(α, x)|2 dα

≥
 √∫

M8,r0 |Sη+(α, x)|2 dα −
 √∫

R/Z |S2,η+(α, x)|2 dα.

As we already showed,
∫

R/Z |S2,η+(α, x)|
2 dα = ∑

n non-prime
or n ≤ √x
 Λ(n)2η+(n/x)2 ≤ E.

Thus, I0 · S ≥ (
√J − √E)2,
and so we are done. □

We now should estimate the integral in (6.12). It is easy to see that
(6.21) ∫ ∞

r0
 1
r3/2 dr = 2

r1/2
0 , ∫ ∞

r0
 log r
r2 dr = log er0
r0 , ∫ ∞

r0
 1
r2 dr = 1
r0 ,

∫ r1

r0
 1
r dr = log r1
r0 , ∫ ∞

r0
 log r
r3/2 dr = 2 log e2r0
√r0 , ∫ ∞

r0
 log 2r
r3/2 dr = 2 log 2e2r0
√r0 ,

∫ ∞

r0
 (log 2r)2

r3/2 dr = 2P2(log 2r0)
√r0 , ∫ ∞

r0
 (log 2r)3

r3/2 dr = 2P3(log 2r0)

r1/2
0 ,

where

(6.22) P2(t) = t2 + 4t + 8, P3(t) = t
3 + 6t2 + 24t + 48.

We also have

(6.23) ∫ ∞

r0
 dr
r2 log r = E1(log r0)

THE TERNARY GOLDBACH CONJECTURE IS TRUE 53

where E1 is the exponential integral

E1(z) = ∫ ∞

z
 e−t

t dt.

We must also estimate the integrals

(6.24) ∫ r1

r0
 √ϝ(r)
r3/2 dr, ∫ r1

r0
 ϝ(r)
r2 dr, ∫ r1

r0
 ϝ(r) log r
r2 dr, ∫ r1

r0
 ϝ(r)
r3/2 dr,

Clearly, ϝ(r) − eγ log log r = 2.50637/ log log r is decreasing on r. Hence, for
r ≥ 105, ϝ(r) ≤ eγ log log r + cγ,

where cγ = 1.025742. Let F (t) = eγ log t + cγ. Then F ′′(t) = −eγ/t2 < 0. Hence

d2√
F (t)
dt2 = F ′′(t)

2
√
F (t) − (F ′(t))2

4(F (t))3/2 < 0

for all t > 0. In other words, √F (t) is convex-down, and so we can bound
√F (t) from above by √
F (t0) + √F ′(t0) · (t − t0), for any t ≥ t0 > 0. Hence, for
r ≥ r0 ≥ 105,

√
ϝ(r) ≤ √
F (log r) ≤ √
F (log r0) + d
√
F (t)
dt |t=log r0 · log r
r0

= √
F (log r0) + eγ
√F (log r0) · log r
r0
2 log r0 .

Thus, by (6.21),
(6.25)
∫ ∞

r0
 √
ϝ(r)
r3/2 dr ≤ √
F (log r0) (
2 − eγ

F (log r0)
 ) 1
√r0 + eγ
√F (log r0) log r0
 log e2r0
√r0

= 2
√
F (log r0)
√r0
 (1 + eγ

F (log r0) log r0
 ) .

The other integrals in (6.24) are easier. Just as in (6.25), we extend the range
of integration to [r0, ∞]. Using (6.21) and (6.23), we obtain
∫ ∞

r0
 ϝ(r)
r2 dr ≤ ∫ ∞

r0
 F (log r)
r2 dr = eγ ( log log r0
r0 + E1(log r0)
) + cγ
r0 ,
∫ ∞

r0
 ϝ(r) log r
r2 dr ≤ eγ ( (1 + log r0) log log r0 + 1
r0 + E1(log r0)
) + cγ log er0
r0 ,

By [OLBC10, (6.8.2)],
 1
r(log r + 1) ≤ E1(log r) ≤ 1
r log r .

(The second inequality is obvious.) Hence
∫ ∞

r0
 ϝ(r)
r2 dr ≤ eγ(log log r0 + 1/ log r0) + cγ
r0 ,

∫ ∞

r0
 ϝ(r) log r
r2 dr ≤ eγ (log log r0 + 1
log r0
 ) + cγ

r0 · log er0.

54 H. A. HELFGOTT

Finally, ∫ ∞

r0
 ϝ(r)
r3/2 ≤ e
γ ( 2 log log r0
√r0 + 2E1
 ( log r0
2
 )) + 2cγ
√r0

≤ 2
√r0
 (
F (log r0) + 2eγ

log r0
 ) .

It is time to estimate

(6.26) ∫ r1

r0
 Rz,2r log 2r√
ϝ(r)
r3/2 dr,

where z = y or z = y/((log y)/2) (and y = x/κ, as before), and where Rz,t is as
deﬁned in (4.14). By Cauchy-Schwarz, (6.26) is at most
√∫ r1

r0
 (Rz,2r log 2r)2

r3/2 dr ·
 √∫ r1

r0
 ϝ(r)
r3/2 dr.

We have already bounded the second integral. Let us look at the ﬁrst one. We
can write Rz,t = 0.27125R◦
z,t + 0.41415, where

(6.27) R◦
z,t = log
 (

1 + log 4t

2 log 9z1/3
2.004t
 )
 .

Clearly,
 R◦
z,et/4 = log
 (

1 + t/2

log 36z1/3
2.004 − t
 )
 .

Now, for f (t) = log(c + at/(b − t)) and t ∈ [0, b),

f ′(t) = ab
(c + at
b−t ) (b − t)2 , f ′′(t) = −ab((a − 2c)(b − 2t) − 2ct)
(c + at
b−t )2 (b − t)4 .

In our case, a = 1/2, c = 1 and b = log 36z1/3 − log(2.004) > 0. Hence, for t < b,

−ab((a − 2c)(b − 2t) − 2ct) = b
2
 (
2t + 3
2 (b − 2t)
) = b
2
 ( 3
2 b − t) > 0,

and so f ′′(t) > 0. In other words, t → R◦
z,et/4 is convex-up for t < b, i.e., for

et/4 < 9z1/3/2.004. It is easy to check that, since we are assuming y ≥ 1025,

2r1 = 3
16 y4/15 < 9
2.004
 ( 2y
log y
 )1/3 ≤ 9z1/3

2.004 .

We conclude that r → R◦
z,2r is convex-up on log 8r for r ≤ r1, and hence so is
r → Rz,r, and so, in turn, is r → R2
z,r. Thus, for r ∈ [r0, r1],

(6.28) R2
z,2r ≤ R2
z,2r0 · log r1/r
log r1/r0 + R2
z,2r1 · log r/r0
log r1/r0 .

THE TERNARY GOLDBACH CONJECTURE IS TRUE 55

Therefore, by (6.21),
(6.29)∫ r1

r0
 (Rz,2r log 2r)2

r3/2 dr ≤ ∫ r1

r0
 (
R2
z,2r0 log r1/r
log r1/r0 + R2
z,2r1 log r/r0
log r1/r0
 ) (log 2r)2 dr
r3/2

= 2R2
z,2r0
log r1
r0
 (( P2(log 2r0)
√r0 − P2(log 2r1)
√r1
 ) log 2r1 − ( P3(log 2r0)
√r0 − P3(log 2r1)
√r1
 ))

+ 2R2
z,2r1
log r1
r0
 (( P3(log 2r0)
√r0 − P3(log 2r1)
√r1
 ) − ( P2(log 2r0)
√r0 − P2(log 2r1)
√
r1
 ) log 2r0
)

= 2
 (

R2
z,2r0 − log 2r0
log r1
r0 (R2
z,2r1 − R2
z,2r0)
)
 · ( P2(log 2r0)
√r0 − P2(log 2r1)
√r1
 )

+ 2 R2
z,2r1 − R2
z,2r0
log r1
r0
 ( P3(log 2r0)
√r0 − P3(log 2r1)
√r1
 )

= 2R2
z,2r0 · ( P2(log 2r0)
√r0 − P2(log 2r1)
√r1
 )

+ 2 R2
z,2r1 − R2
z,2r0
log r1
r0
 ( P −
2 (log 2r0)
√r0 − P3(log 2r1) − (log 2r0)P2(log 2r1)
√r1
 ) ,

where P2(t) and P3(t) are as in (6.22), and P −
2 (t) = P3(t)−tP2(t) = 2t2 +16t+48.
Putting all terms together, we conclude that

(6.30) ∫ r1

r0
 g(r)
r dr ≤ f0(r0, y) + f1(r0) + f2(r0, y),

where

(6.31)
 f0(r0, y) = ((1 − cϕ) √
I0,r0,r1,y + cϕ√
I0,r0,r1, 2y
log y
 ) √ 2
√
r0 I1,r0

f1(r0) =
 √
F (log r0)
√2r0
 (
1 + eγ

F (log r0) log r0
 ) + 5
√2r0

+ 1
r0
 (( 13
4 log er0 + 10.102
) Jr0 + 80
9 log er0 + 23.433
)

f2(r0, y) = 3.2 ((log y)/2)1/6

y1/6 log r1
r0 ,

where F (t) = eγ log t + cγ, cγ = 1.025742, y = x/κ (as usual),
(6.32)

I0,r0,r1,z = R2
z,2r0 · ( P2(log 2r0)
√r0 − P2(log 2r1)
√r1
 )

+ R2
z,2r1 − R2
z,2r0
log r1
r0
 ( P −
2 (log 2r0)
√r0 − P3(log 2r1) − (log 2r0)P2(log 2r1)
√r1
 )

Jr = F (log r) + eγ

log r , I1,r = F (log r) + 2eγ

log r , cϕ = Cϕ,2, log y
2 /|ϕ|1

log log y
2

and Cϕ,2,K is as in (4.21).

56 H. A. HELFGOTT

7. Conclusion

We now need to gather all results, using the smoothing functions

η∗ = (η2 ∗M ϕ)(κt),

where ϕ(t) = t2e−t2/2, η2 = η1 ∗M η1 and η1 = 2 · I[−1/2,1/2], and

η+ = h200(t)te−t2/2,

where
 hH (t) = ∫ ∞

0 h(ty−1)FH (y) dy
y ,

h(t) =
 {
t2(2 − t)3et−1/2 if t ∈ [0, 2],
0 otherwise, FH (t) = sin(H log y)
π log y .

Both η∗ and η+ were studied in [Hela]. We also saw η∗ in Thm. 6.3 (which
actually works for general ϕ : [0, ∞) → [0, ∞), as its statement says). We will set
κ soon.
We ﬁx a value for r, namely, r = 150000. Our results will have to be valid for
any x ≥ x+, where x+ is ﬁxed. We set x+ = 4.9 · 1026, since we want a result
valid for N ≥ 1027, and, as was discussed in (4.1), we will work with x+ slightly
smaller than N/2.

7.1. The ℓ2 norm over the major arcs: explicit version. We apply Lemma
3.1 with η = η+ and η◦ as in (4.3). Let us ﬁrst work out the error terms deﬁned
in (3.27). Recall that δ0 = 8. By [Hela, Thm. 1.4],

(7.1)
 ETη+,δ0r/2 = max
|δ|≤δ0r/2 | errη,χT (δ, x)|

= 3.34 · 10−11 + 251100
√x+ ≤ 1.1377 · 10
−8,

(7.2)
 Eη+,r,δ0 = max
χ mod q
q≤r·gcd(q,2)
|δ|≤gcd(q,2)δ0r/2q
 √q| errη+,χ∗(δ, x)|

≤ 6.18 · 10
−12 + 1.14 · 10−10
√
2 + 1
√x+
 (499100 + 52√300000
)

≤ 2.3921 · 10
−8,

where, in the latter case, we are using the fact that the stronger bound for q = 1
(namely, (7.1)) allows us to assume q ≥ 2.
We also need to bound a few norms: by the estimates in [Hela, App. B.3 and
B.5] (applied with H = 200),

(7.3) |η+|1 ≤ 1.062319, |η+|2 ≤ 0.800129 + 274.8569
2007/2 ≤ 0.800132

|η+|∞ ≤ 1 + 2.06440727 · 1 + 4
π log H
H ≤ 1.079955.

By (3.12), Sη+(0, x) = ̂η+(0) · x + O∗ (errη+,χT (0, x)
) · x

≤ (|η+|1 + ETη+,δ0r/2)x ≤ 1.063x.

THE TERNARY GOLDBACH CONJECTURE IS TRUE 57

This is far from optimal, but it will do, since all we wish to do with this is to
bound Kr,2 in (3.27):

Kr,2 = (1 + √300000)(log x)
2 · 1.079955

· (2 · 1.062319 + (1 + √300000)(log x)21.079955/x)

≤ 1259.06(log x)
2 ≤ 9.71 · 10
−21x

for x ≥ x+. By (7.1), we also have

5.19δ0r
 (
ET
η+, δ0r
2 ·
 (

|η+|1 + ET
η+, δ0r
2
2
 ))
 ≤ 0.075272

and δ0r(log 2e2r) (E2
η+,r,δ0 + Kr,2/x) ≤ 1.0034 · 10
−8.

We know (see [Hela, App. B.2 and B.3]) that

(7.4) 0.8001287 ≤ |η◦|2 ≤ 0.8001288

and

(7.5) |η+ − η◦|2 ≤ 274.856893
H 7/2 ≤ 2.42942 · 10
−6.

Symbolic integration gives

(7.6) |η′
◦|
2
2 = 2.7375292 . . .

We bound |η(3)
◦ |1 using the fact that (as we can tell by taking derivatives) η(2)
◦ (t)
increases from 0 at t = 0 to a maximum within [0, 1/2], and then decreases to
η(2)
◦ (1) = −7, only to increase to a maximum within [3/2, 2] (equal to that within
[0, 1/2]) and then decrease to 0 at t = 2:

(7.7) |η(3)
◦ |1 = 2 max
t∈[0,1/2] η(2)
◦ (t) − 2η(2)
◦ (1) + 2 max
t∈[3/2,2] η(2)
◦ (t)

= 4 max
t∈[0,1/2] η(2)
◦ (t) + 14 ≤ 4 · 4.6255653 + 14 ≤ 32.5023,

where we compute the maximum by the bisection method with 30 iterations
(using interval arithmetic, as always).
We evaluate explicitly ∑

q≤r
q odd
 µ2(q)
φ(q) = 6.798779 . . .

Looking at (3.29) and (3.28), we conclude that

Lr,δ0 ≤ 2 · 6.798779 · 0.8001322 ≤ 8.70531,

Lr,δ0 ≥ 2 · 6.798779 · 0.80012872 + O∗((log r + 1.7) · (3.889 · 10−6 + 5.91 · 10
−12))

+ O∗ (1.342 · 10
−5) · (
0.64787 + log r
4r + 0.425
r
 ) ≥ 8.70517.

Lemma 3.1 thus gives us that

(7.8)
 ∫

M8,r0
 ∣
∣Sη+(α, x)
∣
∣2 dα = (8.70524 + O∗(0.00007))x + O∗(0.075272)x

= (8.7052 + O∗(0.0754))x ≤ 8.7806x.

58 H. A. HELFGOTT

7.2. The total major-arc contribution. First of all, we must bound from
below

(7.9) C0 = ∏

p|N
 (
1 − 1
(p − 1)2
 ) · ∏

p∤N
 (
1 + 1
(p − 1)3
 ) .

The only prime that we know does not divide N is 2. Thus, we use the bound

(7.10) C0 ≥ 2 ∏

p>2
 (
1 − 1
(p − 1)2
 ) ≥ 1.3203236.

The other main constant is Cη◦,η∗, which we deﬁned in (3.37) and already
started to estimate in (4.6):

(7.11) Cη◦,η∗ = |η◦|
2
2
 ∫ N
x

0 η∗(ρ)dρ+2.71|η′
◦|2
2·O∗ (∫ N
x

0 ((2 − N/x) + ρ)
2η∗(ρ)dρ
)

provided that N ≥ 2x. Recall that η∗ = (η2 ∗M ϕ)(κt), where ϕ(t) = t2e−t2/2.
Therefore,
∫ N/x

0 η∗(ρ)dρ = ∫ N/x

0 (η2 ∗ ϕ)(κρ)dρ = ∫ 1

1/4 η2(w) ∫ N/x

0 ϕ ( κρ
w
 ) dρ dw
w

= |η2|1|ϕ|1
κ − 1
κ
 ∫ 1

1/4 η2(w) ∫ ∞

κN/xw ϕ(ρ)dρdw.

Now ∫ ∞

y ϕ(ρ)dρ = ye
−y2/2 + √2 ∫ ∞

y/
√2 e−t2dt < (y + 2
y
 ) e−y2/2

by [OLBC10, (7.8.3)]. Hence
∫ ∞

κN/xw ϕ(ρ)dρ ≤ ∫ ∞

2κ ϕ(ρ)dρ < (
2κ + 1
κ
 ) e−2κ2

and so, since |η2|1 = 1,

(7.12)
 ∫ N/x

0 η∗(ρ)dρ ≥ |ϕ|1
κ − ∫ 1

1/4 η2(w)dw · (
2 + 1
κ2
 ) e−2κ2

≥ |ϕ|1
κ − (
2 + 1
κ2
 ) e
−2κ2.

Let us now focus on the second integral in (7.11). Write N/x = 2+c1/κ. Then
the integral equals
∫ 2+c1/κ

0 (−c1/κ + ρ)
2η∗(ρ)dρ ≤ 1
κ3
 ∫ ∞

0 (u − c1)2 (η2 ∗M ϕ)(u) du

= 1
κ3
 ∫ 1

1/4 η2(w) ∫ ∞

0 (vw − c1)
2ϕ(v)dvdw

= 1
κ3
 ∫ 1

1/4 η2(w) (
3√ π
2 w2 − 2 · 2c1w + c
2
1
√ π
2
 ) dw

= 1
κ3
 ( 49
48
 √ π
2 − 9
4 c1 + √ π
2 c
2
1
) .

THE TERNARY GOLDBACH CONJECTURE IS TRUE 59

It is thus best to choose c1 = (9/4)/√2π = 0.89762 . . . . Looking up |η′
◦|2
2 in (7.6),
we obtain
 2.71|η′
◦|
2
2· ∫ N
x

0 ((2 − N/x) + ρ)
2η∗(ρ)dρ

≤ 7.4188 · 1
κ3
 ( 49
48
 √ π
2 − (9/4)2

2√2π
 ) ≤ 2.0002
κ3 .

We conclude that

Cη◦,η∗ ≥ 1
κ |ϕ|1|η◦|
2
2 − |η◦|2
2
 (
2 + 1
κ2
 ) e−2κ2 − 2.0002
κ3 .

Setting κ = 49
and using (7.4), we obtain

(7.13) Cη◦,η∗ ≥ 1
κ (|ϕ|1|η◦|
2
2 − 0.000834).

Here it is useful to note that |ϕ|1 = √ π
2 , and so, by (7.4), |ϕ|1|η◦|2
2 = 0.80237 . . . .
We have ﬁnally chosen x in terms of N :

(7.14) x = N
2 + c1
κ = N

2 + 9/4
√2π 1
49 = 0.495461 . . . · N.

Thus, we see that, since we are assuming N ≥ 1027, we in fact have x ≥
4.95461 . . . · 1026, and so, in particular,

(7.15) x ≥ 4.9 · 1026, x
κ ≥ 10
25.

Let us continue with our determination of the major-arcs total. We should
compute the quantities in (3.38). We already have bounds for Eη+,r,δ0, Aη+ (see
(7.8)), Lη,r,δ0 and Kr,2. By [Hela, Cor. 1.3], we have

(7.16)
 Eη∗,r,8 ≤ max
χ mod q
q≤r·gcd(q,2)
|δ|≤gcd(q,2)δ0r/2q
 √q| errη∗,χ∗(δ, x)|

≤ 1
κ
 (
4.269 · 10
−14 + 1
√x+
 (380600 + 76√300000
))

≤ 1.9075 · 10−8

κ ,

where the factor of κ comes from the scaling in η∗(t) = (η2 ∗M ϕ)(κt) (which in
eﬀect divides x by κ). It remains only to bound the more harmless terms of type
Zη,2 and LSη.
Clearly, Zη2
+,2 ≤ (1/x) ∑
n Λ(n)(log n)η2
+(n/x). Now, by [Hela, Prop. 1.5],

(7.17)
 ∞∑

n=1
Λ(n)(log n)η2(n/x)

= (
0.640206 + O∗ (
2 · 10
−6 + 310.84
√x
 )) x log x − 0.021095x

≤ (0.640206 + O∗(3 · 10
−6))x log x − 0.021095x.

Thus, Zη2
+,2 ≤ 0.640209x log x.

60 H. A. HELFGOTT

We will proceed a little more crudely for Zη2
∗,2:

(7.18) Zη2
∗,2 = 1
x
 ∑

n Λ2(n)η2
∗(n/x) ≤ 1
x
 ∑

n Λ(n)η∗(n/x) · (η∗(n/x) log n)

≤ (|η∗|1 + | errη∗,χT (0, x)|) · (|η∗(t) · log+(κt)|∞ + |η∗|∞ log(x/κ)),

where log+(t) := max(0, log t). It is easy to see that

(7.19) |η∗|∞ = |η2 ∗M ϕ|∞ ≤ ∣
∣
∣
∣ η2(t)
t
 ∣
∣
∣
∣
1 |ϕ|∞ ≤ 4(log 2)
2 · 2
e ≤ 1.414,

and, since log+ is non-decreasing and η2 is supported on a subset of [0, 1],

|η∗(t) · log+(κt)|∞ = |(η2 ∗M ϕ) · log+ |∞ ≤ |η2 ∗M (ϕ · log+)|∞

≤ ∣
∣
∣
∣ η2(t)
t
 ∣
∣
∣
∣
1 · |ϕ · log+ |∞ ≤ 1.921813 · 0.381157 ≤ 0.732513

where we bound |ϕ · log+ |∞ by the bisection method with 25 iterations. We
already know that

(7.20) |η∗|1 = |η2|1|ϕ|1
κ = |ϕ|1
κ =
 √
π/2
κ .

By [Hela, Cor. 1.3],

| errη∗,χT (0, x)| ≤ 4.269 · 10
−14 + 1
√x+ (380600 + 76) ≤ 1.71973 · 10
−8.

We conclude that
(7.21)
Zη2
∗,2 ≤ (
√
π/2/49 + 1.71973 · 10−8)(0.732513 + 1.414 log(x/49)) ≤ 0.0362 log x.

We have bounds for |η∗|∞ and |η+|∞. We can also bound

|η∗ · t|∞ = |(η2 ∗M ϕ) · t|∞
κ ≤ |η2|1 · |ϕ · t|∞
κ ≤ 33/2e−3/2

κ ;

we quote the bound

(7.22) |η+ · t|∞ = 1.064735 + 3.25312 · (1 + (4/π) log 200)/200 ≤ 1.19073

from [Hela, § B.5].
We can now bound LSη(x, r) for η = η∗, η+:

LSη(x, r) = log r · max
p≤r
 ∑

α≥1 η ( pα

x
 ) ≤ (log r) · max
p≤r
 



 log x
log p |η|∞ + ∑

α≥1
pα≥x
 |η · t|∞
pα/x
 





≤ (log r) · max
p≤r
 ( log x
log p |η|∞ + |η · t|∞
1 − 1/p
 )

≤ (log r)(log x)
log 2 |η|∞ + 2(log r)|η · t|∞,

THE TERNARY GOLDBACH CONJECTURE IS TRUE 61

and so

(7.23)
 LSη∗ ≤
 ( 1.414
log 2 log x + 2 · (3/e)3/2

49
 )
 log r ≤ 24.32 log x + 0.57,

LSη+ ≤ ( 1.07996
log 2 log x + 2 · 1.19073
) log r ≤ 18.57 log x + 28.39.

We can now start to put together all terms in (3.36). Let ϵ0 = |η+ − η◦|2/|η◦|2.
Then, by (7.5), ϵ0|η◦|2 ≤ |η+ − η◦|2 ≤ 2.43 · 10
−6.

Thus,
 2.82643|η◦|2
2(2 + ϵ0) · ϵ0 + 4.31004|η◦|2
2 + 0.0012 |η(3)
◦ |2
1
δ5
0
r
is at most
 2.82643 · 2.43 · 10
−6 · (2 · 0.80013 + 2.43 · 10
−6)

+ 4.3101 · 0.800132 + 0.0012 · 32.5032
85
150000 ≤ 2.9387 · 10
−5

by (7.4), (7.7), and (7.20).
Since η∗ = (η2 ∗M ϕ)(κx) and η2 is supported on [1/4, 1],

|η∗|2
2 = |η2 ∗M ϕ|2
2
κ = 1
κ
 ∫ ∞

0
 (∫ ∞

0 η2(t)ϕ ( w
t
 ) dt
t
 )2 dw

≤ 1
κ
 ∫ ∞

0
 (1 − 1
4
 ) ∫ ∞

0 η2
2(t)ϕ
2 ( w
t
 ) dt
t2 dw

= 3
4κ
 ∫ ∞

0
 η2
2(t)
t
 (∫ ∞

0 ϕ
2 ( w
t
 ) dw
t
 ) dt

= 3
4κ |η2(t)/
√t|
2
2 · |ϕ|2
2 = 3
4κ · 32
3 (log 2)
3 · 3
8 √π ≤ 1.77082
κ .

Recalling the bounds on Eη∗,r,δ0 and Eη+,r,δ0 we obtained in (7.2) and (7.16),
we conclude that the second line of (3.36) is at most x2 times

1.9075 · 10−8

κ · 8.7806 + 2.3921 · 10
−8 · 1.6812

· (
√8.7806 + 1.6812 · 0.80014)

√ 1.77082
κ ≤ 1.7815 · 10−6

κ ,

where we are using the bound Aη+ ≤ 8.8013 we obtained in (7.8). (We are also
using the bounds on norms in (7.3).)
By the bounds (7.18), (7.21) and (7.23), we see that the third line of (3.36) is
at most

2 · (0.640209 log x) · (24.32 log x + 0.57) · x

+ 4√
0.640209 log x · 0.0362 log x(18.57 log x + 28.39)x ≤ 43(log x)2x,

where we just use the very weak assumption x ≥ 1015 to simplify, though we can
by now assume (7.15).

62 H. A. HELFGOTT

Using the assumption x ≥ x+ = 4.9 · 1026, we conclude that, for r = 150000,
the integral over the major arcs
∫

M8,r Sη+(α, x)2Sη∗(α, x)e(−N α)dα

is
(7.24)

C0 · Cη0,η∗x2 + O∗ (
2.9387 · 10
−5 ·
 √
π/2
κ x2 + 1.7815 · 10−6

κ x
2 + 43(log x)2x
)

= C0 · Cη0,η∗x2 + O∗ ( 3.8613 · 10−5 · x2

κ
 ) = C0 · Cη0,η∗x2 + O∗(7.881 · 10
−7x2),

where C0 and Cη0,η∗ are as in (3.37). Notice that C0Cη0,η∗x2 is the expected
asymptotic for the integral over all of R/Z.
Moreover, by (7.10), (7.13) and (7.4), as well as |ϕ|1 = √π/2,

C0 · Cη0,η∗ ≥ 1.3203236 ( |ϕ|1|η◦|2
2
κ − 0.000834
κ
 )

≥ 1.0594001
κ − 0.001102
κ ≥ 1.058298
49 .

Hence

(7.25) ∫

M8,r Sη+(α, x)2Sη∗(α, x)e(−N α)dα ≥ 1.058259
κ x2,

where, as usual, κ = 49. This is our total major-arc bound.

7.3. The minor-arc total: explicit version. We need to estimate the quan-
tities E, S, T , J, M in Theorem 6.3. Let us start by bounding the constants in
(6.11). The constants Cη+,j, j = 0, 1, 2, will appear only in the minor term A2,
and so crude bounds on them will do.
By (7.3) and (7.22),

sup
r≥t η+(r) ≤ min (
1.07996, 1.19073
t
 )

for all t ≥ 0. Thus,

Cη+,0 = 0.7131 ∫ ∞

0
 1
√t
 (
sup
r≥t η+(r))2 dt

≤ 0.7131 (∫ 1

0
 1.079962
√t dt + ∫ ∞

1
 1.190732

t5/2 dt
) ≤ 2.3375.

Similarly,
 Cη+,1 ≤ 0.7131 ∫ ∞

1
 log t
√t
 (
sup
r≥t η+(r)
)2 dt

≤ 0.7131 ∫ ∞

1
 1.190732 log t
t5/2 dt ≤ 0.4494.

Immediately from (7.3),

Cη+,2 = 0.51941|η+|
2
∞ ≤ 0.60579.

THE TERNARY GOLDBACH CONJECTURE IS TRUE 63

We get

(7.26) E ≤ ((2.3375 + 0.60579) log x + (2 · 2.3375 + 0.4494)) · x1/2

≤ (2.9433 log x + 5.1244) · x1/2 ≤ 8.4031 · 10
−12 · x,

where E is deﬁned as in (6.10), and where we are using the assumption x ≥ x+ =
4.9 · 1026. Using (7.16) and (7.20), we see that

Sη∗(0, x) = (|η∗|1 + O∗(ETη∗,0))x = (√
π/2 + O∗(1.9075 · 10
−8)
) x
κ .

Hence

(7.27) Sη∗(0, x) · E ≤ 1.0532 · 10
−11 · x2

κ .

We can bound

(7.28) S ≤ ∑

n Λ(n)(log n)η2
+(n/x) ≤ 0.640209x log x − 0.021095x

by (7.17). Let us now estimate T . Recall that ϕ(t) = t2e−t2/2. Since
∫ u

0 ϕ(t)dt = ∫ u

0 t2e−t2/2dt ≤ ∫ u

0 t
2dt = u3

3 ,

we can bound

Cϕ,3 (log x
κ
 ) = 1.04488
√
π/2
 ∫ 2
log x/κ

0 t
2e
−t2/2dt ≤ 0.2779
((log x/κ)/2)3 .

By (7.8), we already know that J = (8.7052 + O∗(0.0754))x. Hence

(7.29) (√J − √E)2 = (
√
(8.7052 + O∗(0.0754))x − √8.4031 · 10−12 · x)
2

≥ 8.6297x,

and so
 T = Cϕ,3
 ( 1
2 log x
κ
 ) · (S − (
√J − √E)2)

≤ 8 · 0.2779
(log x/κ)3 · (0.640209x log x − 0.021095x − 8.6297x)

≤ 0.17792 8x log x
(log x/κ)3 − 2.40405 8x
(log x/κ)3

≤ 1.42336 x
(log x/κ)2 − 13.69288 x
(log x/κ)3 .

for κ = 49. Since x/κ ≥ 1025, this implies that

(7.30) T ≤ 3.5776 · 10
−4 · x.

It remains to estimate M . Let us ﬁrst look at g(r0); here g = gx/κ,ϕ, where
gx/κ,ϕ is deﬁned as in (4.20) and φ(t) = t2e−t2/2, as usual. Write y = x/κ. We
must estimate the constant Cϕ,2,K deﬁned in (4.22):

Cϕ,2,K = − ∫ 1

1/K ϕ(w) log w dw ≤ − ∫ 1

0 ϕ(w) log w dw

≤ − ∫ 1

0 w2e
−w2/2 log w dw ≤ 0.093426,

64 H. A. HELFGOTT

where again we use VNODE-LP for rigorous numerical integration. Since |ϕ|1 =√π/2 and K = (log y)/2, this implies that

(7.31) Cϕ,2,K/|ϕ|1
log K ≤ 0.07455

log log y
2
and so

(7.32) Ry,K,ϕ,t = 0.07455

log log y
2 Ry/K,t +
 (

1 − 0.07455

log log y
2
 )
 Ry,t.

Let t = 2r0 = 300000; we recall that K = (log y)/2. Recall from (7.15) that
y = x/κ ≥ 1025; thus, y/K ≥ 3.47435 · 1023 and log((log y)/2) ≥ 3.35976. Going
back to the deﬁnition of Rx,t in (4.14), we see that

(7.33) Ry,,2r0 ≤ 0.27125 log
 (

1 + log(8 · 150000)

2 log 9·(1025)1/3
2.004·2·150000
 )
 + 0.41415 ≤ 0.58341,

(7.34)

Ry/K,2r0 ≤ 0.27125 log
 (

1 + log(8 · 150000)

2 log 9·(3.47435·1023)1/3
2.004·2·150000
 )
 + 0.41415 ≤ 0.60295,

and so
 Ry,K,ϕ,2r0 ≤ 0.07455
3.35976 0.60295 + (
1 − 0.07455
3.35976
 ) 0.58341 ≤ 0.58385.

Using
 ϝ(r) = eγ log log r + 2.50637
log log r ≤ 5.42506,

we see from (4.14) that

Lr0 = 5.42506 · (
log 2 7
4 150000 13
4 + 80
9
 ) + log 2 16
9 150000 80
9 + 111
5 ≤ 394.316.

Going back to (4.20), we sum up and obtain that

g(r0) = (0.58385 · log 300000 + 0.5)
√5.42506 + 2.5
√2 · 150000 + 394.316
150000 + 3.2 ( log y
2y
 )1/6

≤ 0.041014.

Using again the bound x ≥ 4.9 · 1026, we obtain

log(150000 + 1) + c+

log √x + c− · S − (
√J − √E)
2

≤ 13.6164
1
2 log x + 0.6294 · (0.640209x log x − 0.021095x) − 8.6297x

≤ 17.4347x − 11.2606x
1
2 log x + 0.6294 − 8.6297x

≤ (17.4347 − 8.6297)x ≤ 8.805x,

where c+ = 2.3912 and c− = 0.6294. Therefore,

(7.35) g(r0) · ( log(150000 + 1) + c+

log √x + c− · S − (√
J − √E)
2) ≤ 0.041061 · 8.805x

≤ 0.36155x.

THE TERNARY GOLDBACH CONJECTURE IS TRUE 65

This is one of the main terms.
Let r1 = (3/8)y4/15, where, as usual, y = x/κ and κ = 49. Then

(7.36)
 Ry,2r1 = 0.27125 log
 

1 + log (8 · 3
8 y4/15)

2 log 9y1/3

2.004· 3
4 y4/15
 

 + 0.41415

= 0.27125 log
 

1 +
 4
15 log y + log 3
2 ( 1
3 − 4
15 ) log y + 2 log 9
2.004· 3
4
 

 + 0.41415

≤ 0.27125 log
 (

1 +
 4
15
2 ( 1
3 − 4
15 )
 )
 + 0.41415 ≤ 0.71215.

Similarly, for K = (log y)/2 (as usual),
(7.37)

Ry/K,2r1 = 0.27125 log
 


1 + log (8 · 3
8 y4/15)

2 log 9(y/K)1/3

2.004· 3
4 y4/15
 


 + 0.41415

= 0.27125 log
 

1 +
 4
15 log y + log 3

2
15 log y − 2
3 log log y + 2 log 9·21/3
2.004· 3
4
 

 + 0.41415

= 0.27125 log
 (
3 +
 4
3 log log y − c

2
15 log y − 2
3 log log y + 2 log 12·21/3
2.004
 )
 + 0.41415,

where c = 4 log(12 · 21/3/2.004) − log 3. Let

f (t) =
 4
3 log t − c

2
15 t − 2
3 log t + 2 log 12·21/3
2.004 .

The bisection method with 32 iterations shows that

(7.38) f (t) ≤ 0.019562618

for 180 ≤ t ≤ 30000; since f (t) < 0 for 0 < t < 180 (by (4/3) log t − c < 0) and
since, by c > 20/3, we have f (t) < (5/2)(log t)/t as soon as t > (log t)2 (and so,
in particular, for t > 30000), we see that (7.38) is valid for all t > 0. Therefore,

(7.39) Ry/K,2r1 ≤ 0.71392,

and so, by (7.32), we conclude that

Ry,K,ϕ,2r1 ≤ 0.07455
3.35976 · 0.71392 + (
1 − 0.07455
3.35976
 ) · 0.71215 ≤ 0.71219.

Since r1 = (3/8)y4/15 and ϝ(r) is increasing for r ≥ 27, we know that
(7.40)

ϝ(r1) ≤ ϝ(y4/15) = eγ log log y4/15 + 2.50637
log log y4/15

= eγ log log y + 2.50637
log log y − log 15
4 − e
γ log 15
4 ≤ eγ log log y − 1.43644

66 H. A. HELFGOTT

for y ≥ 1025. Hence, (4.14) gives us that

Lr1 ≤ (e
γ log log y − 1.43644)
 (
log
 (

2 7
4 ( 3
8
 ) 13
4 y 13
15
 )
 + 80
9
 )

+ log
 (
2 16
9 ( 3
8
 ) 80
9 y 64
27
 )
 + 111
5 ≤ 13
15 eγ log y log log y + 1.1255 log y

+ 12.3147 log log y + 4.78195 ≤ (1.8213 log y + 13.49459) log log y.

Moreover, again by (7.40)

√ϝ(r1) ≤ √
eγ log log y − 1.43644
2
√eγ log log y

and so, by y ≥ 1025,

(0.71219 log 3
4 y 4
15 + 0.5)
√
ϝ(r1)

≤ (0.18992 log y + 0.29512) (√
eγ log log y − 1.43644
2
√eγ log log y
 )

≤ 0.19505
√
eγ log log y − 0.19505 · 1.43644 log y
2√
eγ log log y

≤ 0.26031 log y√log log y − 3.00147.

Therefore, by (4.20),

gy,ϕ(r1) ≤ 0.26031 log y√log log y + 2.5 − 3.00147
√ 3
4 y 4
15

+ (1.8213 log y + 13.49459) log log y

3
8 y 4
15 + 3.2((log y)/2)1/6

y1/6

≤ 0.30059 log y√log log y

y 2
15 + 5.48127 log y log log y

y 4
15 + 0.84323(log y)1/6

y1/6

≤ 0.30782 log y√log log y

y 2
15 ,

where we use y ≥ 1025 and verify that the functions t ↦→ (log t)1/6/t1/6−2/15 and
t ↦→ √
log log t/t4/15−2/15 are decreasing for t ≥ y (just taking derivatives).
Since κ = 49, one of the terms in (6.12) simpliﬁes easily:

7
15 + −2.14938 + 8
15 log κ
log x + 2c− ≤ 7
15 .

By (7.28) and y = x/κ = x/49, we conclude that
(7.41)
7
15 g(r1)S ≤ 7
15 · 0.30782 log y√log log y

y 2
15 · (0.640209 log x − 0.021095)x

≤ 0.14365 log y√log log y

y 2
15 (0.640209 log y + 2.4705)x ≤ 0.30386x,

THE TERNARY GOLDBACH CONJECTURE IS TRUE 67

where we are using the fact that y ↦→ (log y)2√log log y/y2/15 is decreasing for
y ≥ 1025 (because y ↦→ (log y)5/2/y2/15 is decreasing for y ≥ e75/4 and 1025 >
e75/4).
It remains only to bound
 2S
log x + 2c−
 ∫ r1

r0
 g(r)
r dr

in the expression (6.12) for M . We will use the bound on the integral given
in (6.30). The easiest term to bound there is f1(r0), deﬁned in (6.31), since it
depends only on r0: for r0 = 150000,

f1(r0) = 0.0163662 . . . .

It is also not hard to bound f2(r0, x), also deﬁned in (6.31):

f2(r0, y) = 3.2 ((log y)/2)1/6

y1/6 log
 3
8 x 4
15

r0

≤ 3.2 (log y)1/6

(2y)1/6
 ( 4
15 log y + 0.05699 − log r0
) ,

and so, since r0 = 150000 and y ≥ 1025,

f2(r0, y) ≤ 0.001332.

Let us now look at the terms I1,r, cϕ in (6.32). We already saw in (7.31) that

cϕ = Cϕ,2/|ϕ|1
log K ≤ 0.07455

log log y
2 ≤ 0.02219.

Since F (t) = eγ log t + cγ with cγ = 1.025742,

(7.42) I1,r0 = F (log r0) + 2eγ

log r0 = 5.73826 . . .

It thus remains only to estimate I0,r0,r1,z for z = y and z = y/K, where K =
(log y)/2.
We already know that

Ry,2r0 ≤ 0.58341, Ry/K,2r0 ≤ 0.60295,
Ry,2r1 ≤ 0.71215, Ry/K,2r1 ≤ 0.71392

by (7.33), (7.34), (7.36) and (7.39). We also have the trivial bound Rz,t ≥ 0.41415
valid for any z and t for which Rz,t is deﬁned.
Omitting negative terms from (6.32), we easily get the following bound, crude
but useful enough:

I0,r0,r1,z ≤ R2
z,2r0 · P2(log 2r0)
√r0 + R2
z,2r1 − 0.414152

log r1
r0
 P −
2 (log 2r0)
√
r0 ,

where P2(t) = t2 + 4t + 8 and P −
2 (t) = 2t2 + 16t + 48. For z = y and r0 = 150000,
this gives

I0,r0,r1,y ≤ 0.58341
2 · P2(log 2r0)
√r0 + 0.712152 − 0.414152

log 3y4/15
8r0 · P −
2 (log 2r0)
√r0

≤ 0.19115 + 0.49214
4
15 log y − log 800000 ;

68 H. A. HELFGOTT

for z = y/K, we proceed in the same way, and obtain

I0,r0,r1,y/K ≤ 0.20416 + 0.49584
4
15 log y − log 800000 .

This gives us

(7.43)
 (1 − cϕ)√
I0,r0,r1,y + cϕ√
I0,r0,r1, 2y
log y

≤ 0.97781 ·
 √
0.19115 + 0.49214
4
15 log y − log 800000

+ 0.02219
√

0.20416 + 0.49584
4
15 log y − log 800000 .

We can now conclude the argument in one of two ways. First, we can simply use
the fact that y ≥ 1025, and obtain that

(1 − cϕ)
√
I0,r0,r1,y + cϕ√
I0,r0,r1, 2y
log y ≤ 0.68659.

Therefore, by (6.31),

f0(r0, y) ≤ 0.68659 ·
 √ 2
√r0 5.73827 ≤ 0.11819.

Again, this is crude, but it would be just about enough for our purposes.
The alternative is to apply a bound such as (7.43) only for y large. Assume
for a moment that y ≥ 10150, say. Then

Ry,r0 ≤ 0.27125 log
 

1 + log 4r0

2 log 9(10150)1/3
2.004r0
 

 + 0.41415 ≤ 0.43086,

and, similarly, R2y/ log y ≤ 0.43113. Since

0.430862 · P2(log 2r0)
√r0 ≤ 0.10426, 0.431132 · P2(log 2r0)
√r0 ≤ 0.10439,

we obtain that

(7.44)
 (1 − cϕ)
√
I0,r0,r1,y + cϕ√
I0,r0,r1, 2y
log y

≤ 0.97781 ·
 √

0.10426 + 0.49214
4
15 log y − log 800000

+ 0.02219
√

0.10439 + 0.49584
4
15 log y − log 800000 ≤ 0.33247

for y ≥ 10150. For y between 1025 and 10150, we evaluate the left side of (7.44)
directly, using the deﬁnition (6.32) of I0,r0,r1,z instead, as well as the bound
cϕ ≤ 0.07455/ log((log y)/2) from (7.31). (It is clear from the second and third
lines of (6.29) that I0,r0,r1,z is decreasing on z for r0, r1 ﬁxed, and so the upper
bound for cϕ does give the worst case.) The bisection method (applied to the
interval [25, 150] with 30 iterations, including 30 initial iterations) gives us that

(7.45) (1 − cϕ)√
I0,r0,r1,y + cϕ√
I0,r0,r1, 2y
log y ≤ 0.4153461

THE TERNARY GOLDBACH CONJECTURE IS TRUE 69

for 1025 ≤ y ≤ 10140. By (7.44), (7.45) is also true for y > 10150. Hence

f0(r0, y) ≤ 0.4153461 ·
 √ 2
√r0 5.73827 ≤ 0.069219.

By (6.30), we conclude that
∫ r1

r0
 g(r)
r dr ≤ 0.069219 + 0.016367 + 0.001332 ≤ 0.086918.

By (7.28),

2S
log x + 2c− ≤ 2(0.640209x log x − 0.021095x)
log x + 2c− ≤ 2 · 0.640209x = 1.280418x,

where we recall that c− = 0.6294 > 0. Hence

(7.46) 2S
log x + 2c−
 ∫ r1

r0
 g(r)
r dr ≤ 0.111292x.

Putting (7.35), (7.41) and (7.46) together, we conclude that the quantity M
deﬁned in (6.12) is bounded by

(7.47) M ≤ 0.36155x + 0.30386x + 0.111292x ≤ 0.77671x.

Gathering the terms from (7.27), (7.30) and (7.47), we see that Theorem 6.3
states that the minor-arc total

Zr0 = ∫

(R/Z)\M8,r0 |Sη∗(α, x)||Sη+(α, x)|
2dα

is bounded by

(7.48)
 Zr0 ≤
 (√ |ϕ|1x
κ (M + T ) + √Sη∗(0, x) · E
)2

≤ (√
|ϕ|1(0.77671 + 3.5776 · 10−4) x
√κ + √1.0532 · 10−11 x
√κ
 )2

≤ 0.97392 x2

κ

for r0 = 150000, x ≥ 4.9 · 1026, where we use yet again the fact that |ϕ|1 = √
π/2.
This is our total minor-arc bound.

7.4. Conclusion: proof of main theorem. As we have known from the start,

(7.49)
 ∑

n1+n2+n3=NΛ(n1)Λ(n2)Λ(n3)η+(n1)η+(n2)η∗(n3)

= ∫

R/Z Sη+(α, x)
2Sη∗(α, x)e(−N α)dα.

70 H. A. HELFGOTT

We have just shown that, assuming N ≥ 1027, N odd,
∫

R/ZSη+(α, x)
2Sη∗(α, x)e(−N α)dα

= ∫

M8,r0 Sη+(α, x)2Sη∗(α, x)e(−N α)dα

+ O∗ (∫

(R/Z)\M8,r0 |Sη+(α, x)|2|Sη∗(α, x)|dα
)

≥ 1.058259 x2

κ + O∗ (0.97392 x2

κ
 ) ≥ 0.08433 x2

κ

for r0 = 150000, where x = N/(2+9/(196
√2π)), as in (7.14). (We are using (7.25)
and (7.48).) Recall that κ = 49 and η∗(t) = (η2 ∗M ϕ)(κt), where ϕ(t) = t2e−t2/2.
It only remains to show that the contribution of terms with n1, n2 or n3 non-
prime to the sum in (7.49) is negligible. (Let us take out n1, n2, n3 equal to 2 as
well, since some prefer to state the ternary Goldbach conjecture as follows: every
odd number ≥ 9 is the sum of three odd primes.) Clearly

(7.50)
 ∑

n1+n2+n3=N
n1, n2 or n3 even or non-prime
 Λ(n1)Λ(n2)Λ(n3)η+(n1)η+(n2)η∗(n3)

≤ 3|η+|
2
∞|η∗|∞ ∑

n1+n2+n3=N
n1 even or non-prime
 Λ(n1)Λ(n2)Λ(n3)

≤ 3|η+|2
∞|η∗|∞·(log N ) ∑

n1 ≤ N non-prime
or n1 = 2
 Λ(n1) ∑

n2≤N Λ(n2).

By (7.3) and (7.19), |η+|∞ ≤ 1.079955 and |η∗|∞ ≤ 1.414. By [RS62, Thms. 12
and 13], ∑

n1 ≤ N non-prime
or n1 = 2
 Λ(n1) < 1.4262
√N + log 2 < 1.4263
√N ,

∑

n1 ≤ N non-prime
or n1 = 2
 Λ(n1) ∑

n2≤N Λ(n2) = 1.4263
√N · 1.03883N ≤ 1.48169N 3/2.

Hence, the sum on the ﬁrst line of (7.50) is at most

7.3306N 3/2 log N.

Thus, for N ≥ 1027 odd,
∑

n1+n2+n3=N
n1, n2, n3 odd primes

Λ(n1)Λ(n2)Λ(n3)η+(n1)η+(n2)η∗(n3)

≥ 0.08433 x2

κ − 7.3306N 3/2 log N

≥ 0.00042248N 2 − 1.4412 · 10
−11 · N 2 ≥ 0.000422N 2

by κ = 49 and (7.14). Since 0.000422N 2 > 0, this shows that every odd number
N ≥ 1027 can be written as the sum of three odd primes.

THE TERNARY GOLDBACH CONJECTURE IS TRUE 71

Since the ternary Goldbach conjecture has already been checked for all N ≤
8.875 · 1030 [HP], we conclude that every odd number N > 7 can be written as
the sum of three odd primes, and every odd number N > 5 can be written as the
sum of three primes. The main theorem is hereby proven: the ternary Goldbach
conjecture is true.
 Appendix A. Sums over primes

Here we treat some sums of the type ∑
n Λ(n)ϕ(n), where ϕ has compact
support. Since the sums are over all integers (not just an arithmetic progression)
and there is no phase e(αn) involved, the treatment is relatively straightforward.
The following is standard.

Lemma A.1 (Explicit formula). Let ϕ : [1, ∞) → C be continuous and piecewise
C1 with ϕ′′ ∈ ℓ1; let it also be of compact support contained in [1, ∞). Then

(A.1) ∑

n Λ(n)ϕ(n) = ∫ ∞

1
 (
1 − 1
x(x2 − 1)
 ) ϕ(x)dx − ∑

ρ (M ϕ)(ρ),

where ρ runs over the non-trivial zeros of ζ(s).

The non-trivial zeros of ζ(s) are, of course, those in the critical strip 0 <
ℜ(s) < 1.
Remark. Lemma A.1 appears as exercise 5 in [IK04, §5.5]; the condition there
that ϕ be smooth can be relaxed, since already the weaker assumption that ϕ′′

be in L1 implies that the Mellin transform (M ϕ)(σ +it) decays quadratically on t
as t → ∞, thereby guaranteeing that the sum ∑
ρ(M ϕ)(ρ) converges absolutely.

Lemma A.2. Let x ≥ 10. Let η2 be as in (4.7). Assume that all non-trivial
zeros of ζ(s) with |ℑ(s)| ≤ T0 lie on the critical line.
Then

(A.2) ∑

n Λ(n)η2 ( n
x
 ) = x + O∗ (
0.135x
1/2 + 9.7
x2
 ) + log eT0
2π
T0
 ( 9/4
2π + 6.03
T0
 ) x.

In particular, with T0 = 3.061 · 1010 in the assumption, we have, for x ≥ 2000,
∑

n Λ(n)η2 ( n
x
 ) = (1 + O∗(ϵ))x + O∗(0.135x1/2),

where ϵ = 2.73 · 10−10.

The assumption that all non-trivial zeros up to T0 = 3.061 · 1010 lie on the
critical line was proven rigorously in [Plaa]; higher values of T0 have been reached
elsewhere ([Wed03], [GD04]).

Proof. By Lemma A.1,
∑

n Λ(n)η2 ( n
x
 ) = ∫ ∞

1 η2
 ( t
x
 ) dt − ∫ ∞

1
 η2(t/x)
t(t2 − 1) dt − ∑

ρ (M ϕ)(ρ),

where ϕ(u) = η2(u/x) and ρ runs over all non-trivial zeros of ζ(s). Since η2 is
non-negative, ∫ ∞
1 η2(t/x)dt = x|η2|1 = x, while
∫ ∞

1
 η2(t/x)
t(t2 − 1) dt = O∗ (∫ 1

1/4
 η2(t)
tx2(t2 − 1/100) dt
)
 = O∗ ( 9.61114
x2
 ) .

72 H. A. HELFGOTT

By (2.6),

∑

ρ (M ϕ)(ρ) = ∑

ρ M η2(ρ)·xρ = ∑

ρ
 ( 1 − 2−ρ

ρ
 )2 x
ρ = S1(x)−2S1(x/2)+S1(x/4),

where

(A.3) Sm(x) = ∑

ρ
 xρ

ρm+1 .

Setting aside the contribution of all ρ with |ℑ(ρ)| ≤ T0 and all ρ with |ℑ(ρ)| > T0
and ℜ(s) ≤ 1/2, and using the symmetry provided by the functional equation,
we obtain
 |Sm(x)| ≤ x1/2 · ∑

ρ
 1
|ρ|m+1 + x · ∑

ρ
|ℑ(ρ)|>T0
|ℜ(ρ)|>1/2
 1
|ρ|m+1

≤ x1/2 · ∑

ρ
 1
|ρ|m+1 + x
2 · ∑

ρ
|ℑ(ρ)|>T0
 1
|ρ|m+1 .

We bound the ﬁrst sum by [Ros41, Lemma 17] and the second sum by [RS03,
Lemma 2]. We obtain

(A.4) |Sm(x)| ≤ ( 1
2mπT m
0 + 2.68
T m+1
0
 ) x log eT0
2π + κmx1/2,

where κ1 = 0.0463, κ2 = 0.00167 and κ3 = 0.0000744.
Hence
∣
∣
∣
∣
∣

∑

ρ (M η)(ρ) · xρ∣
∣
∣
∣
∣ ≤ ( 1
2πT0 + 2.68
T 2
0
 ) 9x
4 log eT0
2π + ( 3
2 + √2) κ1x1/2.

For T0 = 3.061 · 1010 and x ≥ 2000, we obtain
∑

n Λ(n)η2 ( n
x
 ) = (1 + O∗(ϵ))x + O∗(0.135x1/2),

where ϵ = 2.73 · 10−10. □

Corollary A.3. Let η2 be as in (4.7). Assume that all non-trivial zeros of ζ(s)
with |ℑ(s)| ≤ T0, T0 = 3.061 · 1010, lie on the critical line. Then, for all x ≥ 1,

(A.5) ∑

n Λ(n)η2 ( n
x
 ) ≤ min ((1 + ϵ)x + 0.2x1/2, 1.04488x
) ,

where ϵ = 2.73 · 10−10.

Proof. Immediate from Lemma A.2 for x ≥ 2000. For x < 2000, we use computa-
tion as follows. Since |η′
2|∞ = 16 and ∑
x/4≤n≤x Λ(n) ≤ x for all x ≥ 0, computing
∑
n≤x Λ(n)η2(n/x) only for x ∈ (1/1000)Z ∩ [0, 2000] results in an inaccuracy of
at most (16 · 0.0005/0.9995)x ≤ 0.00801x. This resolves the matter at all points
outside (205, 207) (for the ﬁrst estimate) or outside (9.5, 10.5) and (13.5, 14.5)
(for the second estimate). In those intervals, the prime powers n involved do not
change (since whether x/4 < n ≤ x depends only on n and [x]), and thus we can
ﬁnd the maximum of the sum in (A.5) just by taking derivatives. □

THE TERNARY GOLDBACH CONJECTURE IS TRUE 73

Appendix B. Sums involving φ(q)

We need estimates for several sums involving φ(q) in the denominator.
The easiest are convergent sums, such as ∑
q µ2(q)/(φ(q)q). We can express
this as ∏p(1 + 1/(p(p − 1))). This is a convergent product, and the main task is
to bound a tail: for r an integer,

(B.1) log ∏

p>r
 (
1 + 1
p(p − 1)
 ) ≤ ∑

p>r
 1
p(p − 1) ≤ ∑

n>r
 1
n(n − 1) = 1
r .

A quick computation
8 now suﬃces to give

(B.2) 2.591461 ≤ ∑

q
 gcd(q, 2)µ2(q)
φ(q)q < 2.591463

and so

(B.3) 1.295730 ≤ ∑

q odd
 µ2(q)
φ(q)q < 1.295732,

since the expression bounded in (B.3) is exactly half of that bounded in (B.2).
Again using (B.1), we get that

(B.4) 2.826419 ≤ ∑

q
 µ2(q)
φ(q)2 < 2.826421.

In what follows, we will use values for convergent sums obtained in much the
same way – an easy tail bound followed by a computation.
By [Ram95, Lemma 3.4],

(B.5)
 ∑

q≤r
 µ2(q)
φ(q) = log r + cE + O∗(7.284r−1/3),

∑

q≤r
q odd
 µ2(q)
φ(q) = 1
2
 (
log r + cE + log 2
2
 ) + O∗(4.899r−1/3),

where
 cE = γ + ∑

p
 log p
p(p − 1) = 1.332582275 + O∗(10−9/3)

by [RS62, (2.11)]. As we already said in (5.15), this, supplemented by a compu-
tation for r ≤ 4 · 107, gives

log r + 1.312 ≤ ∑

q≤r
 µ2(q)
φ(q) ≤ log r + 1.354

for r ≥ 182. In the same way, we get that

(B.6) 1
2 log r + 0.83 ≤ ∑

q≤r
q odd
 µ2(q)
φ(q) ≤ 1
2 log r + 0.85

for r ≥ 195. (The numerical veriﬁcation here goes up to 1.38·108; for r > 3.18·108,
use B.6.)

8Using D. Platt’s integer arithmetic package.

74 H. A. HELFGOTT

Clearly

(B.7) ∑

q≤2r
q even
 µ2(q)
φ(q) = ∑

q≤r
q odd
 µ2(q)
φ(q) .

We wish to obtain bounds for the sums
∑

q≥r
 µ2(q)
φ(q)2 , ∑

q≥r
q odd
 µ2(q)
φ(q)2 , ∑

q≥r
q even
 µ2(q)
φ(q)2 ,

where N ∈ Z+ and r ≥ 1. To do this, it will be helpful to express some of the
quantities within these sums as convolutions.9 For q squarefree and j ≥ 1,

(B.8) µ2(q)qj−1

φ(q)j = ∑

ab=q
 fj(b)
a ,

where fj is the multiplicative function deﬁned by

fj(p) = pj − (p − 1)j

(p − 1)jp , fj(pk) = 0 for k ≥ 2.

We will also ﬁnd the following estimate useful.

Lemma B.1. Let j ≥ 2 be an integer and A a positive real. Let m ≥ 1 be an
integer. Then

(B.9) ∑

a≥A
(a,m)=1
 µ2(a)
aj ≤ ζ(j)/ζ(2j)
Aj−1 · ∏

p|m
 (
1 + 1
pj
 )−1 .

It is useful to note that ζ(2)/ζ(4) = 15/π2 = 1.519817 . . . and ζ(3)/ζ(6) =
1.181564 . . . .

Proof. The right side of (B.9) decreases as A increases, while the left side depends
only on ⌈A⌉. Hence, it is enough to prove (B.9) when A is an integer.
For A = 1, (B.9) is an equality. Let

C = ζ(j)
ζ(2j) · ∏

p|m
 (1 + 1
pj
 )−1 .

Let A ≥ 2. Since ∑

a≥A
(a,m)=1
 µ2(a)
aj = C − ∑

a<A
(a,m)=1
 µ2(a)
aj

and
 C = ∑

a
(a,m)=1
 µ2(a)
aj < ∑

a<A
(a,m)=1
 µ2(a)
aj + 1
Aj + ∫ ∞

A
 1
tj dt

= ∑

a<A
(a,m)=1
 µ2(a)
aj + 1
Aj + 1
(j − 1)Aj−1 ,

9The author would like to thank O. Ramar´e for teaching him this technique.

THE TERNARY GOLDBACH CONJECTURE IS TRUE 75

we obtain
∑

a≥A
(a,m)=1
 µ2(a)
aj = 1
Aj−1 · C + Aj−1 − 1
Aj−1 · C − ∑

a<A
(a,m)=1
 µ2(a)
aj

< C
Aj−1 + Aj−1 − 1
Aj−1 · ( 1
Aj + 1
(j − 1)Aj−1
 ) − 1
Aj−1 ∑

a<A
(a,m)=1
 µ2(a)
aj

≤ C
Aj−1 + 1
Aj−1
 ((1 − 1
Aj−1
 ) ( 1
A + 1
j − 1
 ) − 1
) .

Since (1 − 1/A)(1/A + 1) < 1 and 1/A + 1/(j − 1) ≤ 1 for j ≥ 3, we obtain that
(
1 − 1
Aj−1
 ) ( 1
A + 1
j − 1
 ) < 1

for all integers j ≥ 2, and so the statement follows. □

We now obtain easily the estimates we want: by (B.8) and Lemma B.1 (with
j = 2 and m = 1),

(B.10)
 ∑

q≥r
 µ2(q)
φ(q)2 = ∑

q≥r
 ∑

ab=q
 f2(b)
a µ2(q)
q ≤ ∑

b≥1
 f2(b)
b
 ∑

a≥r/b
 µ2(a)
a2

≤ ζ(2)/ζ(4)
r
 ∑

b≥1 f2(b) =
 15
π2
r
 ∏

p
 (1 + 2p − 1
(p − 1)2p
 ) ≤ 6.7345
r .

Similarly, by (B.8) and Lemma B.1 (with j = 2 and m = 2),

(B.11)
 ∑

q≥r
q odd
 µ2(q)
φ(q)2 = ∑

b≥1
b odd
 f2(b)
b
 ∑

a≥r/b
a odd
 µ2(a)
a2 ≤ ζ(2)/ζ(4)
1 + 1/22 1
r
 ∑

b odd f2(b)

= 12
π2 1
r
 ∏

p>2
 (
1 + 2p − 1
(p − 1)2p
 ) ≤ 2.15502
r

(B.12) ∑

q≥r
q even
 µ2(q)
φ(q)2 = ∑

q≥r/2
q odd
 µ2(q)
φ(q)2 ≤ 4.31004
r .

Lastly,
(B.13)
∑

q≤r
q odd
 µ2(q)q
φ(q) = ∑

q≤r
q odd
 µ2(q) ∑

d|q
 1
φ(d) = ∑

d≤r
d odd
 1
φ(d)
 ∑

q≤r
d|q
q odd
 µ2(q) ≤ ∑

d≤r
d odd
 1
2φ(d)
 ( r
d + 1)

≤ r
2
 ∑

d odd
 1
φ(d)d + 1
2
 ∑

d≤r
d odd
 1
φ(d) ≤ 0.64787r + log r
4 + 0.425,

where we are using (B.3) and (B.6).

76 H. A. HELFGOTT

Appendix C. Checking small n by checking zeros of ζ(s)

In order to show that every odd number n ≤ N is the sum of three primes, it
is enough to show for some M ≤ N that
(1) every even integer 4 ≤ m ≤ M can be written as the sum of two primes,
(2) the diﬀerence between any two consecutive primes ≤ N is at most M − 4.
(If we want to show that every odd number n ≤ N is the sum of three odd primes,
we just replace M − 4 by M − 6 in (2).) The best known result of type (1) is
that of Oliveira e Silva, Herzog and Pardi ([OeSHP13], M = 4 · 1018). As for
(2), it was proven in [HP] for M = 4 · 1018 and N = 8.875694 · 1030 by a direct
computation (valid with M − 4 or M − 6 in the statement of (2)). See §1.2.2.
Alternatively, one can establish results of type (2) by means of numerical ver-
iﬁcations of the Riemann hypothesis up to a certain height. This is a classical
approach, followed in [RS75] and [Sch76], and later in [RS03]; we will use the
version of (1) kindly provided by Ramar´e in [Ram]. We carry out this approach
in full here, not because it is preferrable to [HP] – it is still based on computa-
tions, and it is slightly more indirect than [HP] – but simply to show that one
can establish what we need by a diﬀerent route.
A numerical veriﬁcation of the Riemann hypothesis up to a certain height
consists simply in checking that all (non-trivial) zeroes z of the Riemann zeta
function up to a height H (meaning: ℑ(z) ≤ H) lie on the critical line ℜ(z) = 1/2.
The height up to which the Riemann hypothesis has actually been fully veriﬁed
is not a matter on which there is unanimity. The strongest claim in the literature
is in [GD04], which states that the ﬁrst 1013 zeroes of the Riemann zeta function
lie on the critical line ℜ(z) = 1/2. This corresponds to checking the Riemann
hypothesis up to height H = 2.44599·1012. It is unclear whether this computation
was or could be easily made rigorous; as pointed out in [SD10, p. 2398], it has
not been replicated yet.
Before [GD04], the strongest results were those of the ZetaGrid distributed
computing project led by S. Wedeniwski [Wed03]; the method followed in it
was more traditional, and should allow rigorous veriﬁcation involving interval
arithmetic. Unfortunately, the results were never formally published. The state-
ment that the ZetaGrid project veriﬁed the ﬁrst 9 · 1011 zeroes (corresponding to
H = 2.419 · 1011) is often quoted (e.g., [Bom10, p. 29]); this is the point to which
the project had got by the time of Gourdon and Demichel’s announcement. We-
deniwski asserts in private communication that the project veriﬁed the ﬁrst 1012

zeroes, and that the computation was double-checked (by the same method).
The strongest claim prior to ZetaGrid was that of van de Lune (H = 3.293·109,
ﬁrst 1010 zeroes; unpublished). Recently, Platt [Plaa] checked the ﬁrst 1.1 · 1011

zeroes (H = 3.061 · 1010) rigorously, following a method essentially based on that
in [Boo06]. Note that [Plaa] uses interval arithmetic, which is highly desirable
for ﬂoating-point computations.

Proposition C.1. Every odd integer 5 ≤ n ≤ n0 is the sum of three primes,
where

n0 =
 




5.90698 · 1029 if [GD04] is used – H = 2.44 · 1012,
6.15697 · 1028 if ZetaGrid results are used (H = 2.419 · 1011),
1.23163 · 1027 if [Plaa] is used ( H = 3.061 · 1010).

Proof. For n ≤ 4 · 1018 + 3, this is immediate from [OeSHP13]. Let 4 · 1018 + 3 <
n ≤ n0. We need to show that there is a prime p in [n − 4 − (n − 4)/∆, n − 4],

THE TERNARY GOLDBACH CONJECTURE IS TRUE 77

where ∆ is large enough for (n − 4)/∆ ≤ 4 · 1018 − 4 to hold. We will then have
that 4 ≤ n − p ≤ 4 + (n − 4)/∆ ≤ 4 · 1018. Since n − p is even, [OeSHP13] will
then imply that n − p is the sum of two primes p′, p′′, and so

n = p + p
′ + p
′′.

Since n − 4 > 1011, the interval [n − 4 − (n − 4)/∆, n − 4] with ∆ = 28314000
must contain a prime [RS03]. This gives the solution for (n − 4) ≤ 1.1325 · 1026,
since then (n − 4) ≤ 4 · 1018 − 4. Note 1.1325 · 1026 > e59.
From here onwards, we use the tables in [Ram] to ﬁnd acceptable values of ∆.
Since n − 4 ≥ e59, we can choose

∆ =
 




52211882224 if [GD04] is used (case (a)),
13861486834 if ZetaGrid is used (case (b)),
307779681 if [Plaa] is used (case (c)).

This gives us (n − 4)/∆ ≤ 4 · 1018 − 4 for n − 4 < er0, where r0 = 67 in case (a),
r0 = 66 in case (b) and r0 = 62 in case (c).
If n − 4 ≥ er0, we can choose (again by [Ram])

∆ =
 




146869130682 in case (a),
15392435100 in case (b),
307908668 in case (c).

This is enough for n − 4 < e68 in case (a), and without further conditions for (b)
or (c).
Finally, if n − 4 ≥ e68 and we are in case (a), [Ram] assures us that the choice

∆ = 147674531294

is valid; we verify as well that (n0 − 4)/∆ ≤ 4 · 1018 − 4. □

In other words, the rigorous results in [Plaa] are enough to show the result for
all odd n ≤ 1027. Of course, [HP] is also more than enough, and gives stronger
results than Prop. C.1.
 References

[BBO10] J. Bertrand, P. Bertrand, and J.-P. Ovarlez. Mellin transform. In A. D. Poularikas,
editor, Transforms and applications handbook. CRC Press, Boca Raton, FL, 2010.
[Bom74] E. Bombieri. Le grand crible dans la th´eorie analytique des nombres. Soci´et´e
Math´ematique de France, Paris, 1974. Avec une sommaire en anglais, Ast´erisque,
No. 18.
[Bom10] E. Bombieri. The classical theory of zeta and L-functions. Milan J. Math., 78(1):11–
59, 2010.
[Boo06] A. R. Booker. Artin’s conjecture, Turing’s method, and the Riemann hypothesis.
Experiment. Math., 15(4):385–407, 2006.
[Bou99] J. Bourgain. On triples in arithmetic progression. Geom. Funct. Anal., 9(5):968–984,
1999.
[CW89] J. R. Chen and T. Z. Wang. On the Goldbach problem. Acta Math. Sinica,
32(5):702–718, 1989.
[Dav67] H. Davenport. Multiplicative number theory, volume 1966 of Lectures given at the
University of Michigan, Winter Term. Markham Publishing Co., Chicago, Ill., 1967.
[Des77] J.-M. Deshouillers. Sur la constante de ˇSnirel
′man. In S´eminaire Delange-Pisot-
Poitou, 17e ann´ee: (1975/76), Th´eorie des nombres: Fac. 2, Exp. No. G16, page 6.
Secr´etariat Math., Paris, 1977.

78 H. A. HELFGOTT

[DEtRZ97] J.-M. Deshouillers, G. Eﬃnger, H. te Riele, and D. Zinoviev. A complete Vinogradov
3-primes theorem under the Riemann hypothesis. Electron. Res. Announc. Amer.
Math. Soc., 3:99–104, 1997.
[Dic66] L. E. Dickson. History of the theory of numbers. Vol. I: Divisibility and primality.
Chelsea Publishing Co., New York, 1966.
[GD04] X. Gourdon and P. Demichel. The ﬁrst 10
13 zeros of the Riemann zeta function,
and zeros computation at very large height. http://numbers.computation.free.
fr/Constants/Miscellaneous/zetazeros1e13-1e24.pdf, 2004.
[GR00] I. S. Gradshteyn and I. M. Ryzhik. Table of integrals, series, and products. Aca-
demic Press Inc., San Diego, CA, sixth edition, 2000. Translated from the Russian,
Translation edited and with a preface by Alan Jeﬀrey and Daniel Zwillinger.
[HB85] D. R. Heath-Brown. The ternary Goldbach problem. Rev. Mat. Iberoamericana,
1(1):45–59, 1985.
[Hela] H. A. Helfgott. Major arcs for Goldbach’s problem. Preprint. Available at
arXiv:1203.5712.
[Helb] H. A. Helfgott. Minor arcs for Goldbach’s problem. Preprint. Available as
arXiv:1205.5252.
[HL23] G. H. Hardy and J. E. Littlewood. Some problems of ‘Partitio numerorum’; III: On
the expression of a number as a sum of primes. Acta Math., 44(1):1–70, 1923.
[HP] H. A. Helfgott and D. Platt. Numerical veriﬁcation of the ternary Goldbach
conjecture up to up to 8.875e30. To appear in Experiment. Math. Available at
arXiv:1305.3062.
[IK04] H. Iwaniec and E. Kowalski. Analytic number theory, volume 53 of American Math-
ematical Society Colloquium Publications. American Mathematical Society, Provi-
dence, RI, 2004.
[KPˇS72] N. I. Klimov, G. Z. Pil
′tja˘ı, and T. A. ˇSeptickaja. An estimate of the absolute
constant in the Goldbach-ˇSnirel
′man problem. In Studies in number theory, No. 4
(Russian), pages 35–51. Izdat. Saratov. Univ., Saratov, 1972.
[Lam08] B. Lambov. Interval arithmetic using SSE-2. In Reliable Implementation of Real
Number Algorithms: Theory and Practice. International Seminar Dagstuhl Castle,
Germany, January 8-13, 2006, volume 5045 of Lecture Notes in Computer Science,
pages 102–113. Springer, Berlin, 2008.
[Lan12] E. Landau. Gel¨oste und ungel¨oste Probleme aus der Theorie der Primzahlverteilung
und der Riemannschen Zetafunktion. In Proceedings of the ﬁfth Itnernational Con-
gress of Mathematicians, volume 1, pages 93–108. Cambridge, 1912.
[Lin41] U. V. Linnik. The large sieve. C. R. (Doklady) Acad. Sci. URSS (N.S.), 30:292–294,
1941.
[LW02] M.-Ch. Liu and T. Wang. On the Vinogradov bound in the three primes Goldbach
conjecture. Acta Arith., 105(2):133–175, 2002.
[Mon71] H. L. Montgomery. Topics in multiplicative number theory. Lecture Notes in Math-
ematics, Vol. 227. Springer-Verlag, Berlin, 1971.
[MV73] H. L. Montgomery and R. C. Vaughan. The large sieve. Mathematika, 20:119–134,
1973.
[OeSHP13] T. Oliveira e Silva, S. Herzog, and S. Pardi. Empirical veriﬁcation of the even
goldbach conjecture, and computation of prime gaps, up to 4 · 10
18. Accepted for
publication in Math. Comp., 2013.
[OLBC10] F. W. J. Olver, D. W. Lozier, R. F. Boisvert, and Ch. W. Clark, editors. NIST hand-
book of mathematical functions. U.S. Department of Commerce National Institute
of Standards and Technology, Washington, DC, 2010. With 1 CD-ROM (Windows,
Macintosh and UNIX).
[Plaa] D. Platt. Computing π(x) analytically. To appear in Math. Comp.. Available as
arXiv:1203.5712.
[Plab] D. Platt. Numerical computations concerning GRH. Preprint. Available at
arXiv:1305.3087.
[Pla11] D. Platt. Computing degree 1 L-functions rigorously. PhD thesis, Bristol University,
2011.
[Ram] O. Ramar´e. Short eﬀective intervals containing primes, ii. Preprint.
[Ram95] O. Ramar´e. On ˇSnirel
′man’s constant. Ann. Scuola Norm. Sup. Pisa Cl. Sci. (4),
22(4):645–706, 1995.

THE TERNARY GOLDBACH CONJECTURE IS TRUE 79

[Ram09] O. Ramar´e. Arithmetical aspects of the large sieve inequality, volume 1 of Harish-
Chandra Research Institute Lecture Notes. Hindustan Book Agency, New Delhi,
2009. With the collaboration of D. S. Ramana.
[Ram10] O. Ramar´e. On Bombieri’s asymptotic sieve. J. Number Theory, 130(5):1155–1189,
2010.
[Ric01] J. Richstein. Verifying the Goldbach conjecture up to 4 · 10
14. Math. Comp.,
70(236):1745–1749 (electronic), 2001.
[Ros41] B. Rosser. Explicit bounds for some functions of prime numbers. Amer. J. Math.,
63:211–232, 1941.
[RS62] J. B. Rosser and L. Schoenfeld. Approximate formulas for some functions of prime
numbers. Illinois J. Math., 6:64–94, 1962.
[RS75] J. Barkley Rosser and Lowell Schoenfeld. Sharper bounds for the Chebyshev func-
tions θ(x) and ψ(x). Math. Comp., 29:243–269, 1975. Collection of articles dedicated
to Derrick Henry Lehmer on the occasion of his seventieth birthday.
[RS03] O. Ramar´e and Y. Saouter. Short eﬀective intervals containing primes. J. Number
Theory, 98(1):10–33, 2003.
[RV83] H. Riesel and R. C. Vaughan. On sums of primes. Ark. Mat., 21(1):46–74, 1983.
[Sch33] L. Schnirelmann. ¨Uber additive Eigenschaften von Zahlen. Math. Ann., 107(1):649–
690, 1933.
[Sch76] L. Schoenfeld. Sharper bounds for the Chebyshev functions θ(x) and ψ(x). II. Math.
Comp., 30(134):337–360, 1976.
[SD10] Y. Saouter and P. Demichel. A sharp region where π(x) − li(x) is positive. Math.
Comp., 79(272):2395–2405, 2010.
[Sha] X. Shao. A density version of the Vinogradov three prime theorem. Preprint. Avail-
able as arXiv:1206.6139.
[Shu92] F. H. Shu. The Cosmos. In Encyclopaedia Britannica, Macropaedia, volume 16,
pages 762–795. Encyclopaedia Britannica, Inc., 15 edition, 1992.
[Tao] T. Tao. Every odd number greater than 1 is the sum of at most ﬁve primes. Preprint.
Available as arXiv:1201.6656.
[Vau77] R. C. Vaughan. On the estimation of Schnirelman’s constant. J. Reine Angew.
Math., 290:93–108, 1977.
[Vin37] I. M. Vinogradov. Representation of an odd number as a sum of three primes. Dokl.
Akad. Nauk. SSR, 15:291–294, 1937.
[Wed03] S. Wedeniwski. ZetaGrid - Computational veriﬁcation of the Riemann hypothesis.
Conference in Number Theory in honour of Professor H. C. Williams, Banﬀ, Alberta,
Canada, May 2003.

Harald Helfgott, ´Ecole Normale Sup´erieure, D´epartement de Math´ematiques,
45 rue d’Ulm, F-75230 Paris, France
E-mail address: harald.helfgott@ens.fr
