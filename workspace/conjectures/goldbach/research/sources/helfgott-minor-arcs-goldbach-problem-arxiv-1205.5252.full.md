<!-- source: https://arxiv.org/pdf/1205.5252 | converted from PDF -->

arXiv:1205.5252v4  [math.NT]  30 Dec 2013
MINOR ARCS FOR GOLDBACH’S PROBLEM

H. A. HELFGOTT

Abstract. The ternary Goldbach conjecture states that every odd number
n ≥ 7 is the sum of three primes. The estimation of sums of the form∑
p≤x e(αp), α = a/q + O(1/q2), has been a central part of the main ap-
proach to the conjecture since (Vinogradov, 1937). Previous work required q
or x to be too large to make a proof of the conjecture for all n feasible.
The present paper gives new bounds on minor arcs and the tails of major
arcs. This is part of the author’s proof of the ternary Goldbach conjecture.
The new bounds are due to several qualitative improvements. In particu-
lar, this paper presents a general method for reducing the cost of Vaughan’s
identity, as well as a way to exploit the tails of minor arcs in the context of
the large sieve.
 Contents

1. Introduction 1
1.1. Results 2
1.2. History 3
1.3. Comparison to earlier work 4
1.4. Acknowledgments 4
2. Preliminaries 5
2.1. Notation 5
2.2. Fourier transforms and exponential sums 5
2.3. Smoothing functions 7
2.4. Bounds on sums of µ(m) and Λ(n) 7
2.5. Basic setup 9
3. Type I 10
3.1. Trigonometric sums 10
3.2. Type I estimates 14
4. Type II 31
4.1. The sum S1: cancellation 32
4.2. The sum S2: the large sieve, primes and tails 44
5. Totals 50
5.1. Contributions of diﬀerent types 51
5.2. Adjusting parameters. Calculations. 62
5.3. Conclusion 72
Appendix A. Norms of Fourier transforms 73
References 77

1. Introduction

The ternary Goldbach conjecture (or three-prime conjecture) states that every
odd number greater than 5 is the sum of three primes. I. M. Vinogradov [Vin37]
1

2 H. A. HELFGOTT

showed in 1937 that every odd integer larger than a very large constant C is
indeed the sum of three primes. His work was based on the study of exponential
sums ∑

n≤N Λ(n)e(αn)

and their use within the circle method.
Unfortunately, further work has so far reduced C only to e3100 ([LW02]; see
also [CW89]), which is still much too large for all odd integers up to C to be
checked numerically. The main problem has been that existing bounds for (1.1)
in the minor arc regime – namely, α = a/q + O(1/q2), gcd(a, q) = 1, q relatively
large – have not been strong enough.
The present paper gives new bounds on smoothed exponential sums

(1.1) Sη(α, x) = ∑

n Λ(n)e(αn)η(n/x).

These bounds are clearly stronger than those on smoothed or unsmoothed expo-
nential sums in the previous literature, including the bounds of [Tao]. (See also
work by Ramar´e [Ram10].)
In particular, on all arcs around a/q, q > 1.5 · 105 odd or q > 3 · 105 even,
the bounds are of the strength required for a full solution to the three-prime
conjecture. The same holds on the tails of arcs around a/q for smaller q.
(The remaining arcs – namely, those around a/q, q small – are the major arcs;
they are treated in the companion paper [Hela].)
The quality of the results here is due to several new ideas of general applica-
bility. In particular, §4.1 introduces a way to obtain cancellation from Vaughan’s
identity. Vaughan’s identity is a two-log gambit, in that it introduces two con-
volutions (each of them at a cost of log) and oﬀers a great deal of ﬂexibility in
compensation. One of the ideas in the present paper is that at least one of two
logs can be successfully recovered after having been given away in the ﬁrst stage
of the proof. This reduces the cost of the use of this basic identity in this and,
presumably, many other problems.
We will also see how to exploit being on the tail of a major arc, whether in the
large sieve (Lemma 4.3, Prop. 4.6) or in other contexts.
There are also several technical improvements that make a qualitative diﬀer-
ence; see the discussions at the beginning of §3 and §4. Considering smoothed
sums – now a common idea – also helps. (Smooth sums here go back to Hardy-
Littlewood [HL23] – both in the general context of the circle method and in the
context of Goldbach’s ternary problem. In recent work on the problem, they
reappear in [Tao].)

1.1. Results. The main bound we are about to see is essentially proportional to
((log q)/
√φ(q)) · x. The term δ0 serves to improve the bound when we are on the
tail of an arc.

Main Theorem. Let x ≥ x0, x0 = 2.16 · 1020. Let Sη(α, x) be as in (1.1), with η
deﬁned in (1.4). Let 2α = a/q + δ/x, q ≤ Q, gcd(a, q) = 1, |δ/x| ≤ 1/qQ, where
Q = (3/4)x2/3. If q ≤ x1/3/6, then

(1.2) |Sη(α, x)| ≤ Rx,δ0q log δ0q + 0.5
√
δ0φ(q) · x + 2.5x
√δ0q + 2x
δ0q · Lx,δ0,q + 3.2x5/6,

MINOR ARCS FOR GOLDBACH’S PROBLEM 3

where

(1.3)
 δ0 = max(2, |δ|/4), Rx,t = 0.27125 log
 (
1 + log 4t

2 log 9x1/3
2.004t
 )
 + 0.41415

Lx,δ,q = min
 ( log δ 7
4 q 13
4 + 80
9
φ(q)/q , 5
6 log x + 50
9
 )
 + log q 80
9 δ 16
9 + 111
5 .

If q > x1/3/6, then

|Sη(α, x)| ≤ 0.2727x5/6(log x)
3/2 + 1218x2/3 log x.

The factor Rx,t is small in practice; for instance, for x = 1025 and δ0q = 5 · 105

(typical “diﬃcult” values), Rx,δ0q equals 0.59648 . . . .
The classical choice
1 for η in (1.1) is η(t) = 1 for t ≤ 1, η(t) = 0 for t > 1,
which, of course, is not smooth, or even continuous. We use

(1.4) η(t) = η2(t) = 4 max(log 2 − | log 2t|, 0),

as in Tao [Tao], in part for purposes of comparison. (This is the multiplicative
convolution of the characteristic function of an interval with itself.) Nearly all
work should be applicable to any other suﬃciently smooth function η of fast
decay. It is important that ̂η decay at least quadratically.

1.2. History. The following notes are here to provide some background; no claim
to completeness is made.
Vinogradov’s proof [Vin37] was based on his novel estimates for exponential
sums over primes. Most work on the problem since then, including essentially
all work with explicit constants, has been based on estimates for exponential
sums; there are some elegant proofs based on cancellation in other kinds of sums
([HB85], [IK04, §19]), but they have not been made to yield practical estimates.
The earliest explicit result is that of Vinogradov’s student Borodzin (1939).
Vaughan [Vau77] greatly simpliﬁed the proof by introducing what is now called
Vaughan’s identity.
The current record is that of Liu and Wang [LW02]: the best previous result
was that of [CW89]. Other recent work falls into the following categories.
Conditional results. The ternary Goldbach conjecture has been proven under
the assumption of the generalized Riemann hypothesis [DEtRZ97].
Ineﬀective results. An example is the bound given by Buttkewitz [But11]. The
issue is usually a reliance on the Siegel-Walﬁsz theorem. In general, to obtain
eﬀective bounds with good constants, it is best to avoid analytic results on L-
functions with large conductor. (The present paper implicitly uses known results
on the Riemann ζ function, but uses nothing at all about other L-functions.)
Results based on Vaughan’s identity. Vaughan’s identity [Vau77] greatly sim-
pliﬁed matters; most textbook treatments are by now based on it. The minor-arc
treatment in [Tao] updates this approach to current technical standards (smooth-
ing), while taking advantage of its ﬂexibility (letting variable ranges depend on
q).
Results based on log-free identities. Using Vaughan’s identity implies losing a
factor of (log x)2 (or (log q)2, as in [Tao]) in the ﬁrst step. It thus makes sense to
consider other identities that do not involve such a loss. Most approaches before

1Or, more precisely, the choice made by Vinogradov and followed by most of the literature
since him. Hardy and Littlewood [HL23] worked with η(t) = e−t.

4 H. A. HELFGOTT

q0 |Sη(a/q,x)|
x , HH |Sη(a/q,x)|
x , Tao
105 0.04522 0.34475
1.5 · 105 0.03821 0.28836
2.5 · 105 0.03097 0.23194
5 · 105 0.02336 0.17416
7.5 · 105 0.01984 0.14775
106 0.01767 0.13159
107 0.00716 0.05251
Table 1. Worst-case upper bounds on x−1|Sη(a/2q, x)| for q ≥
q0, |δ| ≤ 8, x = 1027. The trivial bound is 1.

Vaughan’s identity involved larger losses, but already [Vin37, §9] is relatively
economical, at least for very large x. The work of Daboussi [Dab96] and Daboussi
and Rivat [DR01] explores other identities. (A reading of [DR01] gave part of the
initial inspiration for the present work.) Ramar´e’s work [Ram10] – asymptotically
the best to date – is based on the Diamond-Steinig inequality (for k large).
* * *
The author’s work on the subject leading to the present paper was at ﬁrst
based on the (log-free) Bombieri-Selberg identity (k = 3), but has now been
redone with Vaughan’s identity in its foundations. This is feasible thanks to the
factor of log regained in §4.1.

1.3. Comparison to earlier work. Table 1 compares the bounds for the ratio
|Sη(a/q, x)|/x given by this paper and by [Tao] for x = 1027 and diﬀerent values
of q. We are comparing worst cases: φ(q) as small as possible (q divisible by
2 · 3 · 5 · · · ) in the result here, and q divisible by 4 (implying 4α ∼ a/(q/4)) in
Tao’s result. The main term in the result in this paper improves slowly with
increasing x; the results in [Tao] worsen slowly with increasing x.
The qualitative gain with respect to [Tao] is about log(q)
√φ(q)/q, which is
∼ log(q)/
√eγ(log log q) in the worst case.
The results in [DR01] are unfortunately worse than the trivial bound in this
range. Ramar´e’s results ([Ram10, Thm. 3], [Ramd, Thm. 6]) are not applicable
within the range, since neither of the conditions log q ≤ (1/50)(log x)1/3, q ≤ x1/48

is satisﬁed. Ramar´e’s bound in [Ramd, Thm. 6] is

(1.5)
 ∣
∣
∣
∣
∣
∣
 ∑

x<n≤2x Λ(n)e(an/q)

∣
∣
∣
∣
∣
∣ ≤ 13000 √q
φ(q) x

for 20 ≤ q ≤ x1/48. We should underline that, while both the constant 13000
and the condition q ≤ x1/48 keep (1.5) from being immediately useful in the
present context, (1.5) is asymptotically better than the results here as q → ∞.
(Indeed, qualitatively speaking, the form of (1.5) is the best one can expect
from results derived by the family of methods stemming from [Vin37].) There
is also unpublished work by Ramar´e (ca. 1993) with better constants for q ≪
(log x/ log log x)4.

1.4. Acknowledgments. The author is very thankful to O. Ramar´e for his cru-
cial help and feedback, and to D. Platt for his prompt and helpful answers. He is
also much indebted to A. Booker, B. Green, H. Kadiri, T. Tao and M. Watkins

MINOR ARCS FOR GOLDBACH’S PROBLEM 5

for many discussions on Goldbach’s problem and related issues. Thanks are also
due to B. Bukh, A. Granville and P. Sarnak for their valuable advice.
Travel and other expenses were funded in part by the Adams Prize and the
Philip Leverhulme Prize. The author’s work on the problem started at the Univer-
sit´e de Montr´eal (CRM) in 2006; he is grateful to both the Universit´e de Montr´eal
and the ´Ecole Normale Sup´erieure for providing pleasant working environments.
The present work would most likely not have been possible without free and
publicly available software: Maxima, PARI, Gnuplot, QEPCAD, SAGE, and, of
course, LATEX, Emacs, the gcc compiler and GNU/Linux in general.

2. Preliminaries

2.1. Notation. Given positive integers m, n, we say m|n∞ if every prime divid-
ing m also divides n. We say a positive integer n is square-full if, for every prime
p dividing n, the square p2 also divides n. (In particular, 1 is square-full.) We
say n is square-free if p2 ∤ n for every prime p. For p prime, n a non-zero integer,
we deﬁne vp(n) to be the largest non-negative integer α such that pα|n.
When we write ∑n, we mean ∑∞
n=1, unless the contrary is stated. As usual, µ,
Λ, τ and σ denote the Moebius function, the von Mangoldt function, the divisor
function and the sum-of-divisors function, respectively.
As is customary, we write e(x) for e2πix. We write |f |r for the Lr norm of a
function f .
We write O∗(R) to mean a quantity at most R in absolute value.

2.2. Fourier transforms and exponential sums. The Fourier transform on
R is normalized here as follows:

̂f (t) = ∫ ∞

−∞ e(−xt)f (x)dx.

If f is compactly supported (or of fast decay) and piecewise continuous, ̂f (t) =
̂f ′(t)/(2πit) by integration by parts. Iterating, we obtain that, if f is compactly
supported, continuous and piecewise C 1, then

(2.1) ̂f (t) = O∗ ( |̂f ′′|∞
(2πt)2
 )
 = O∗ ( |f ′′|1
(2πt)2
 ) ,

and so ̂f decays at least quadratically.
The following bound is standard (see, e.g., [Tao, Lemma 3.1]): for α ∈ R/Z
and f : R → C compactly supported and piecewise continuous,

(2.2)
 ∣
∣
∣
∣
∣
∑

n∈Z f (n)e(αn)

∣
∣
∣
∣
∣ ≤ min
 (
|f |1 + 1
2 |f ′|1,
 1
2 |f ′|1
| sin(πα)|
 )
 .

(The ﬁrst bound follows from ∑n∈Z |f (n)| ≤ |f |1 + (1/2)|f ′|1, which, in turn is
a quick consequence of the fundamental theorem of calculus; the second bound
is proven by summation by parts.) The alternative bound (1/4)|f ′′|1/| sin(πα)|2

given in [Tao, Lemma 3.1] (for f continuous and piecewise C 1) can usually be
improved by the following estimate.

6 H. A. HELFGOTT

Lemma 2.1. Let f : R → C be compactly supported, continuous and piecewise
C 1. Then

(2.3)
 ∣
∣
∣
∣
∣
∑

n∈Z f (n)e(αn)

∣
∣
∣
∣
∣ ≤
 1
4 |̂f ′′|∞
(sin απ)2

for every α ∈ R.

As usual, the assumption of compact support could be easily relaxed to an
assumption of fast decay.

Proof. By the Poisson summation formula,

∞∑

n=−∞ f (n)e(αn) =
 ∞∑

n=−∞ ̂f (n − α).

Since ̂f (t) = ̂f ′(t)/(2πit),

∞∑

n=−∞ ̂f (n − α) =
 ∞∑

n=−∞
 ̂f ′(n − α)
2πi(n − α) =
 ∞∑

n=−∞
 ̂f ′′(n − α)
(2πi(n − α))2 .

By Euler’s formula π cot sπ = 1/s + ∑∞
n=1(1/(n + s) − 1/(n − s)),

(2.4)
 ∞∑

n=−∞
 1
(n + s)2 = −(π cot sπ)
′ = π2

(sin sπ)2 .

Hence
∣
∣
∣
∣
∣
 ∞∑

n=−∞ ̂f (n − α)

∣
∣
∣
∣
∣ ≤ |̂f ′′|∞
 ∞∑

n=−∞
 1
(2π(n − α))2 = |̂f ′′|∞ · 1
(2π)2 · π2

(sin απ)2 .
 □

The trivial bound |̂f ′′|∞ ≤ |f ′′|1, applied to (2.3), recovers the bound in [Tao,
Lemma 3.1]. In order to do better, we will give a tighter bound for |̂f ′′|∞ when
f = η2 in Appendix A.
Integrals of multiples of f ′′ (in particular, |f ′′|1 and ̂f ′′) can still be made sense
of when f ′′ is undeﬁned at a ﬁnite number of points, provided f is understood as
a distribution (and f ′ has ﬁnite total variation). This is the case, in particular,
for f = η2.
 * * *

When we need to estimate ∑n f (n) precisely, we will use the Poisson summa-
tion formula: ∑

n f (n) = ∑

n ̂f (n).

We will not have to worry about convergence here, since we will apply the Pois-
son summation formula only to compactly supported functions f whose Fourier
transforms decay at least quadratically.

MINOR ARCS FOR GOLDBACH’S PROBLEM 7

2.3. Smoothing functions. For the smoothing function η2 in (1.4),

(2.5) |η2|1 = 1, |η′
2|1 = 8 log 2, |η′′
2 |1 = 48,

as per [Tao, (5.9)–(5.13)]. Similarly, for η2,ρ(t) = log(ρt)η2(t), where ρ ≥ 4,

(2.6)
 |η2,ρ|1 < log(ρ)|η2|1 = log(ρ)

|η′
2,ρ|1 = 2η2,ρ(1/2) = 2 log(ρ/2)η2(1/2) < (8 log 2) log ρ,

|η′′
2,ρ|1 = 4 log(ρ/4) + |2 log ρ − 4 log(ρ/4)| + |4 log 2 − 4 log ρ|

+ | log ρ − 4 log 2| + | log ρ| < 48 log ρ.

(In the ﬁrst inequality, we are using the fact that log(ρt) is always positive (and
less than log(ρ)) when t is in the support of η2.)
Write log+ x for max(log x, 0).

2.4. Bounds on sums of µ(m) and Λ(n). We will need explicit bounds on∑n≤N µ(n)/n and related sums involving µ. The situation here is less well-
developed than for sums involving Λ. The main reason is that the complex-
analytic approach to estimating ∑n≤N µ(n) would involve 1/ζ(s) rather than
ζ ′(s)/ζ(s), and thus strong explicit bounds on the residues of 1/ζ(s) would be
needed.
Fortunately all we need is a saving of (log n) or (log n)2 on the trivial bound.
This is provided by the following.
(1) (Granville-Ramar´e [GR96], Lemma 10.2)

(2.7)
 ∣
∣
∣
∣
∣
∣
 ∑

n≤x:gcd(n,q)=1
 µ(n)
n
 ∣
∣
∣
∣
∣
∣ ≤ 1

for all x, q ≥ 1,
(2) (Ramar´e [Ramc]; cf. El Marraki [EM95], [EM96])

(2.8)
 ∣
∣
∣
∣
∣
∣
∑

n≤x
 µ(n)
n
 ∣
∣
∣
∣
∣
∣ ≤ 0.03
log x

for x ≥ 11815.
(3) (Ramar´e [Rama])

(2.9) ∑

n≤x:gcd(n,q)=1
 µ(n)
n = O∗ ( 1
log x/q · 4
5 q
φ(q)
 )

for all x and all q ≤ x;

(2.10) ∑

n≤x:gcd(n,q)=1
 µ(n)
n log x
n = O∗ (1.00303 q
φ(q)
 )

for all x and all q.
Improvements on these bounds would lead to improvements on type I estimates,
but not in what are the worst terms overall at this point.
A computation carried out by the author has proven the following inequality
for all real x ≤ 1012:

(2.11)
 ∣
∣
∣
∣
∣
∣
∑

n≤x
 µ(n)
n
 ∣
∣
∣
∣
∣
∣ ≤
 √ 2
x

8 H. A. HELFGOTT

The computation was rigorous, in that it used D. Platt’s implementation [Pla11]
of double-precision interval arithmetic based on Lambov’s [Lam08] ideas. For the
sake of veriﬁcation, we record that

5.42625 · 10
−8 ≤ ∑

n≤1012
 µ(n)
n ≤ 5.42898 · 10
−8.

Computations also show that the stronger bound
∣
∣
∣
∣
∣
∣
∑

n≤x
 µ(n)
n
 ∣
∣
∣
∣
∣
∣ ≤ 1
2
√x

holds for all 3 ≤ x ≤ 7727068587, but not for x = 7727068588 − ǫ.
Earlier, numerical work carried out by Olivier Ramar´e [Ramb] had shown that
(2.11) holds for all x ≤ 1010.
We will make reference to various bounds on Λ(n) in the literature. The
following bound can be easily derived from [RS62, (3.23)], supplemented by a
quick calculation of the contribution of powers of primes p < 32:

(2.12) ∑

n≤x
 Λ(n)
n ≤ log x.

We can derive a bound in the other direction from [RS62, (3.21)] (for x > 1000,
adding the contribution of all prime powers ≤ 1000) and a numerical veriﬁcation
for x ≤ 1000:

(2.13) ∑

n≤x
 Λ(n)
n ≥ log x − log 3
√
2 .

We also use the following older bounds:
(1) By the second table in [RR96, p. 423], supplemented by a computation
for 2 · 106 ≤ V ≤ 4 · 106,

(2.14) ∑

n≤y Λ(n) ≤ 1.0004y

for y ≥ 2 · 106.
(2)

(2.15) ∑

n≤y Λ(n) < 1.03883y

for every y > 0 [RS62, Thm. 12].
For all y > 663,

(2.16) ∑

n≤y Λ(n)n < 1.03884 y2

2 ,

where we use (2.15) and partial summation for y > 200000, and a computation
for 663 < y ≤ 200000. Using instead the second table in [RR96, p. 423], together
with computations for small y < 107 and partial summation, we get that

(2.17) ∑

n≤y Λ(n)n < 1.0008 y2

2

for y > 1.6 · 106.
 MINOR ARCS FOR GOLDBACH’S PROBLEM 9

Similarly,

(2.18) ∑

n≤y Λ(n) < 2 · 1.0004
√y

for all y ≥ 1.
It is also true that

(2.19) ∑

y/2<p≤y(log p)
2 ≤ 1
2 y(log y)

for y ≥ 117: this holds for y ≥ 2 · 758699 by [RS75, Cor. 2] (applied to x = y,
x = y/2 and x = 2y/3) and for 117 ≤ y < 2 · 758699 by direct computation.

2.5. Basic setup. We begin by applying Vaughan’s identity [Vau77]: for any
function η : R → R, any completely multiplicative function f : Z+ → C and any
x > 0, U, V ≥ 0,

(2.20) ∑

n Λ(n)f (n)e(αn)η(n/x) = SI,1 − SI,2 + SII + S0,∞,

where

(2.21)
 SI,1 = ∑

m≤U µ(m)f (m) ∑

n (log n)e(αmn)f (n)η(mn/x),

SI,2 = ∑

d≤V Λ(d)f (d) ∑

m≤U µ(m)f (m) ∑

n e(αdmn)f (n)η(dmn/x),

SII = ∑

m>U f (m)
 



∑

d>U
d|m
 µ(d)





 ∑

n>V Λ(n)e(αmn)f (n)η(mn/x),

S0,∞ = ∑

n≤V Λ(n)e(αn)f (n)η(n/x).

The proof is essentially an application of the M¨obius inversion formula; see, e.g.,
[IK04, §13.4]. In practice, we will use the function

(2.22) f (n) =
 {1 if gcd(n, v) = 1,
0 otherwise,

where v is a small, positive, square-free integer. (Our ﬁnal choice will be v = 2.)
Then

(2.23) Sη(x, α) = SI,1 − SI,2 + SII + S0,∞ + S0,w,

where Sη(x, α) is as in (1.1) and

S0,v = ∑

n|v Λ(n)e(αn)η(n/x).

The sums SI,1, SI,2 are called “of type I” (or linear), the sum SII is called “of
type II” (or bilinear). The sum S0 is in general negligible; for our later choice of
V and η, it will be in fact 0. The sum S0,v will be negligible as well.

10 H. A. HELFGOTT

3. Type I

There are here three main improvements in comparison to standard treatments:

(1) The terms with m divisible by q get taken out and treated separately
by analytic means. This all but eliminates what would otherwise be the
main term.
(2) For large m, the other terms get handled by improved estimates on
trigonometric sums.
(3) The “error” term δ/x = α − a/q is used to our advantage. This happens
both through the Poisson summation formula and through the use of two
successive approximations.

3.1. Trigonometric sums. The following lemmas on trigonometric sums im-
prove on the best Vinogradov-type lemmas in the literature. (By this, we mean
results of the type of Lemma 8a and Lemma 8b in [Vin04, Ch. I]. See, in par-
ticular, the work of Daboussi and Rivat [DR01, Lemma 1].) The main idea is
to switch between diﬀerent types of approximation within the sum, rather than
just choosing between bounding all terms either trivially (by A) or non-trivially
(by C/| sin(παn)|2). There will also
2 be improvements in our applications stem-
ming from the fact that Lemmas 3.1 and Lemma 3.2 take quadratic (| sin(παn)|2)
rather than linear (| sin(παn)|) inputs.

Lemma 3.1. Let α = a/q + β/qQ, gcd(a, q) = 1, |β| ≤ 1, q ≤ Q. Then, for any
A, C ≥ 0,

(3.1) ∑

y<n≤y+q min (A, C
| sin(παn)|2
 ) ≤ min (2A + 6q2

π2 C, 3A + 4q
π
 √AC) .

Proof. We start by letting m0 = ⌊y⌋ + ⌊(q + 1)/2⌋, j = n − m0, so that j ranges
in the interval (−q/2, q/2]. We write

αn = aj + c
q + δ1(j) + δ2 mod 1,

where |δ1(j)| and |δ2| are both ≤ 1/2q; we can assume δ2 ≥ 0. The variable
r = aj + c mod q occupies each residue class mod p exactly once.
One option is to bound the terms corresponding to r = 0, −1 by A each and
all the other terms by C/| sin(παn)|2. The terms corresponding to r = −k and
r = k − 1 (2 ≤ k ≤ q/2) contribute at most

1
sin
2 π
q (k − 1
2 − qδ2) + 1
sin
2 π
q (k − 3
2 + qδ2) ≤ 1
sin2 π
q (k − 1
2 ) + 1
sin2 π
q (k − 3
2 ) ,

since x ↦→ 1
(sin x)2 is convex-up on (0, ∞). Hence the terms with r ̸= 0, 1 contribute
at most
 1
(sin π
2q )2 + 2 ∑

2≤r≤ q
2
 1
(sin π
q (r − 1/2)
)2 ≤ 1
(
sin π
2q )2 + 2 ∫ q/2

1
 1
(
sin π
q x)2 ,

2This is a change with respect to the ﬁrst version of this paper’s preprint [Helb]. The version
of Lemma 3.1 there has, however, the advantage of being immediately comparable to results in
the literature.
 MINOR ARCS FOR GOLDBACH’S PROBLEM 11

where we use again the convexity of x ↦→ 1/(sin x)2. (We can assume q > 2, as
otherwise we have no terms other than r = 0, 1.) Now
∫ q/2

1
 1
(
sin π
q x)2 dx = q
π
 ∫ π
2

π
q
 1
(sin u)2 du = q
π cot π
q .

Hence ∑

y<n≤y+q min (A, C
(sin παn)2
 ) ≤ 2A + C
(
sin π
2q )2 + C · 2q
π cot π
q .

Now, by [AS64, (4.3.68)] and [AS64, (4.3.70)], for t ∈ (−π, π),

(3.2)
 t
sin t = 1 + ∑

k≥0 a2k+1t2k+2 = 1 + t2

6 + . . .

t cot t = 1 − ∑

k≥0 b2k+1t2k+2 = 1 − t2

3 − t4

45 − . . . ,

where a2k+1 ≥ 0, b2k+1 ≥ 0. Thus, for t ∈ [0, t0], t0 < π,

(3.3) ( t
sin t
 )2 = 1 + t2

3 + c0(t)t4 ≤ 1 + t2

3 + c0(t0)t4,

where
 c0(t) = 1
t4
 (( t
sin t
 )2 − (1 + t2

3
 ))
 ,

which is an increasing function because a2k+1 ≥ 0. For t0 = π/4, c0(t0) ≤
0.074807. Hence,

t2

sin2 t + t cot 2t ≤ (1 + t2

3 + c0 ( π
4
 ) t4) + ( 1
2 − 2t2

3 − 8t4

45
 )

= 3
2 − t2

3 + (c0 ( π
4
 ) − 8
45
 ) t4 ≤ 3
2 − t2

3 ≤ 3
2

for t ∈ [0, π/4].
Therefore, the left side of (3.1) is at most

2A + C · ( 2q
π
 )2 · 3
2 = 2A + 6
π2 Cq2.

The following is an alternative approach yielding the other estimate in (3.1).
We bound the terms corresponding to r = 0, r = −1, r = 1 by A each. We let
r = ±r′ for r′ ranging from 2 to q/2. We obtain that the sum is at most

(3.4)
 3A + ∑

2≤r′≤q/2 min
 


A, C
(
sin π
q (r′ − 1
2 − qδ2))2
 




+ ∑

2≤r′≤q/2 min
 


A, C
(
sin π
q (r′ − 1
2 + qδ2))2
 


 .

12 H. A. HELFGOTT

We bound a term min(A, C/ sin((π/q)(r′ − 1/2 ± qδ2))2) by A if and only if
C/ sin((π/q)(r′ − 1 ± qδ2))2 ≥ A. The number of such terms is

≤ max(0, ⌊(q/π) arcsin(
√C/A) ∓ qδ2⌋),

and thus at most (2q/π) arcsin(
√C/A) in total. (Recall that qδ2 ≤ 1/2.) Each
other term gets bounded by the integral of C/ sin2(πα/q) from r′ − 1 ± qδ2 (≥
(q/π) arcsin(
√C/A)) to r′ ± qδ2, by convexity. Thus (3.4) is at most

3A + 2q
π A arcsin
 √C
A + 2 ∫ q/2

q
π arcsin √ C
A
 C
sin
2 πt
q dt

≤ 3A + 2q
π A arcsin
 √ C
A + 2q
π C
√ A
C − 1

We can easily show (taking derivatives) that arcsin x + x(1 − x2) ≤ 2x for
0 ≤ x ≤ 1. Setting x = C/A, we see that this implies that

3A + 2q
π A arcsin
 √ C
A + 2q
π C
√ A
C − 1 ≤ 3A + 4q
π
 √
AC.

(If C/A > 1, then 3A+(4q/π)
√AC is greater than Aq, which is an obvious upper
bound for the left side of (3.1).) □

Lemma 3.2. Let α = a/q+β/qQ, gcd(a, q) = 1, |β| ≤ 1, q ≤ Q. Let y2 > y1 ≥ 0.
If y2 − y1 ≤ q and y2 ≤ Q/2, then, for any A, C ≥ 0,

(3.5) ∑

y1<n≤y2
q∤n
 min (
A, C
| sin(παn)|2
 ) ≤ min ( 20
3π2 Cq2, 2A + 4q
π
 √AC) .

Proof. Clearly, αn equals an/q + (n/Q)β/q; since y2 ≤ Q/2, this means that
|αn − an/q| ≤ 1/2q for n ≤ y2; moreover, again for n ≤ y2, the sign of αn − an/q
remains constant. Hence the left side of (3.5) is at most

q/2∑

r=1 min
 (
A, C
(sin π
q (r − 1/2))2
 )
 +
 q/2∑

r=1 min
 (
A, C
(sin π
q r)2
 )
 .

Proceeding as in the proof of Lemma 3.1, we obtain a bound of at most

C
 ( 1
(sin π
2q )2 + 1
(sin π
q )2 + q
π cot π
q + q
π cot 3π
2q
 )

for q ≥ 2. (If q = 1, then the left-side of (3.5) is trivially zero.) Now, by (3.2),

t2

(sin t)2 + t
2 cot 2t ≤ (1 + t2

3 + c0 ( π
4
 ) t4) + 1
4
 (1 − 4t2

3 − 16t4

45
 )

≤ 5
4 + (c0 ( π
4
 ) − 4
45
 ) t4 ≤ 5
4

for t ∈ [0, π/4], and

t2

(sin t)2 + t cot 3t
2 ≤ (
1 + t2

3 + c0 ( π
2
 ) t4) + 2
3
 (1 − 3t2

4 − 81t4

24 · 45
 )

≤ 5
3 + (− 1
6 + (c0 ( π
2
 ) − 27
360
 ) ( π
2
 )2) t2 ≤ 5
3

MINOR ARCS FOR GOLDBACH’S PROBLEM 13

for t ∈ [0, π/2]. Hence,
( 1
(sin π
2q )2 + 1
(sin π
q )2 + q
π cot π
q + q
π cot 3π
2q
 )
 ≤ ( 2q
π
 )2 · 5
4 + ( q
π
 )2 · 5
3 ≤ 20
3π2 q2.

Alternatively, we can follow the second approach in the proof of Lemma 3.1, and
obtain an upper bound of 2A + (4q/π)
√AC. □

The following bound will be useful when the constant A in an application of
Lemma 3.2 would be too large. (This tends to happen for n small.)

Lemma 3.3. Let α = a/q+β/qQ, gcd(a, q) = 1, |β| ≤ 1, q ≤ Q. Let y2 > y1 ≥ 0.
If y2 − y1 ≤ q and y2 ≤ Q/2, then, for any B, C ≥ 0,

(3.6) ∑

y1<n≤y2
q∤n
 min ( B
| sin(παn)| , C
| sin(παn)|2
 ) ≤ 2B q
π max (2, log Ce3q
Bπ
 ) .

The upper bound ≤ (2Bq/π) log(2e2q/π) is also valid.

Proof. As in the proof of Lemma 3.2, we can bound the left side of (3.6) by

2
 q/2∑

r=1 min
 ( B
sin π
q (
r − 1
2 ) , C
sin2 π
q (r − 1
2 )
 )
 .

Assume B sin(π/q) ≤ C ≤ B. By the convexity of 1/ sin(t) and 1/ sin(t)2 for
t ∈ (0, π/2],

q/2∑

r=1 min
 ( B
sin π
q (r − 1
2 ) , C
sin2 π
q (r − 1
2 )
 )

≤ B
sin π
2q + ∫ q
π arcsin C
B

1
 B
sin π
q t dt + ∫ q/2

q
π arcsin C
B
 1
sin2 π
q t dt

≤ B
sin π
2q + q
π
 (B (log tan ( 1
2 arcsin C
B
 ) − log tan π
2q
 ) + C cot arcsin C
B
 )

≤ B
sin π
2q + q
π
 (B (log cot π
2q − log C
B − √B2 − C 2
 ) + √B2 − C 2) .

Now, for all t ∈ (0, π/2),

2
sin t + 1
t log cot t < 1
t log ( e2

t
 ) ;

we can verify this by comparing series. Thus

B
sin π
2q + q
π B log cot π
2q ≤ B q
π log 2e2q
π

for q ≥ 2. (If q = 1, the sum on the left of (3.6) is empty, and so the bound we
are trying to prove is trivial.) We also have

(3.7) t log(t − √t2 − 1) + √t2 − 1 < −t log 2t + t

14 H. A. HELFGOTT

for t ≥ 1 (as this is equivalent to log(2t2(1 − √1 − t−2)) < 1 − √1 − t−2, which
we check easily after changing variables to δ = 1 − √1 − t−2). Hence

B
sin π
2q + q
π
 (B (
log cot π
2q − log C
B − √B2 − C 2
 ) + √B2 − C 2)

≤ B q
π log 2e2q
π + q
π
 (B − B log 2B
C
 ) ≤ B q
π log Ce3q
Bπ

for q ≥ 2.
Given any C, we can apply the above with C = B instead, as, for any t > 0,
min(B/t, C/t2) ≤ B/t ≤ min(B/t, B/t2). (We refrain from applying (3.7) so as
to avoid worsening a constant.) If C < B sin π/q (or even if C < (π/q)B), we
relax the input to C = B sin π/q and go through the above. □

3.2. Type I estimates. Our main type I estimate is the following.
3 One of the
main innovations is the manner in which the “main term” (m divisible by q) is
separated; we are able to keep error terms small thanks to the particular way in
which we switch between two diﬀerent approximations.
(These are not necessarily successive approximations in the sense of continued
fractions; we do not want to assume that the approximation a/q we are given
arises from a continued fraction, and at any rate we need more control on the
denominator q′ of the new approximation a′/q′ than continued fractions would
furnish.)

Lemma 3.4. Let α = a/q + δ/x, gcd(a, q) = 1, |δ/x| ≤ 1/qQ0, q ≤ Q0, Q0 ≥ 16.
Let η be continuous, piecewise C 2 and compactly supported, with |η|1 = 1 and
η′′ ∈ L1. Let c0 ≥ | ̂η′′|∞.
Let 1 ≤ D ≤ x. Then, if |δ| ≤ 1/2c2, where c2 = (3π/5
√c0)(1 + √13/3), the
absolute value of

(3.8) ∑

m≤D µ(m) ∑

n e(αmn)η ( mn
x
 )

is at most

(3.9) x
q min (1, c0
(2πδ)2
 )
 ∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
 ∑

m≤ M
q
gcd(m,q)=1
 µ(m)
m
 ∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
 + O∗ (c0
 ( 1
4 − 1
π2
 ) ( D2

2xq + D
2x
 ))

plus

(3.10)
 2
√c0c1
π D + 3c1 x
q log+ D
c2x/q + √c0c1
π q log+ D
q/2

+ |η′|1
π q · max (2, log c0e3q2

4π|η′|1x
 ) + ( 2
√3c0c1
π + 3c1
c2 + 55c0c2
12π2
 ) q,

where c1 = 1 + |η′|1/(2x/D) and M ∈ [min(Q0/2, D), D]. The same bound holds
if |δ| ≥ 1/2c2 but D ≤ Q0/2.

3The current version of Lemma 3.4 is an improvement over that included in the ﬁrst preprint
of this paper.
 MINOR ARCS FOR GOLDBACH’S PROBLEM 15

In general, if |δ| ≥ 1/2c2, the absolute value of (3.8) is at most (3.9) plus

(3.11)
 2
√c0c1
π
 (
D + (1 + ǫ) min (⌊ x
|δ|q
 ⌋ + 1, 2D) (
̟ǫ + 1
2 log+ 2D
x
|δ|q
 ))

+ 3c1
 (
2 + (1 + ǫ)
ǫ log+ 2D
x
|δ|q
 ) x
Q0 + 35c0c2
6π2 q,

for ǫ ∈ (0, 1] arbitrary, where ̟ǫ = √3 + 2ǫ + ((1 + √13/3)/4 − 1)/(2(1 + ǫ)).

In (3.9), min(1, c0/(2πδ)2) always equals 1 when |δ| ≤ 1/2c2 (since (3/5)(1 +√13/3) > 1).

Proof. Let Q = ⌊x/|δq|⌋. Then α = a/q + O∗(1/qQ) and q ≤ Q. (If δ = 0,
we let Q = ∞ and ignore the rest of the paragraph, since then we will never
need Q′ or the alternative approximation a′/q′.) Let Q′ = ⌈(1 + ǫ)Q⌉ ≥ Q + 1.
Then α is not a/q + O∗(1/qQ′), and so there must be a diﬀerent approximation
a′/q′, gcd(a′, q′) = 1, q′ ≤ Q′ such that α = a′/q′ + O∗(1/q′Q′) (since such
an approximation always exists). Obviously, |a/q − a′/q′| ≥ 1/qq′, yet, at the
same time, |a/q − a′/q′| ≤ 1/qQ + 1/q′Q′ ≤ 1/qQ + 1/((1 + ǫ)q′Q). Hence
q′/Q + q/((1 + ǫ)Q) ≥ 1, and so q′ ≥ Q − q/(1 + ǫ) ≥ (ǫ/(1 + ǫ))Q. (Note also
that (ǫ/(1 + ǫ))Q ≥ (2|δq|/x) · ⌊x/δq⌋ > 1, and so q′ ≥ 2.)
Lemma 3.2 will enable us to treat separately the contribution from terms with
m divisible by q and m not divisible by q, provided that m ≤ Q/2. Let M =
min(Q/2, D). We start by considering all terms with m ≤ M divisible by q. Then
e(αmn) equals e((δm/x)n). By Poisson summation,
∑

n e(αmn)η(mn/x) = ∑

n ̂f (n),

where f (u) = e((δm/x)u)η((m/x)u). Now

̂f (n) = ∫ e(−un)f (u)du = x
m
 ∫ e ((
δ − xn
m
 ) u
) η(u)du = x
m ̂η ( x
m n − δ) .

By assumption, m ≤ M ≤ Q/2 ≤ x/2|δq|, and so |x/m| ≥ 2|δq| ≥ 2δ. Thus, by
(2.1),

(3.12)
 ∑

n ̂f (n) = x
m
 

̂η(−δ) + ∑

n̸=0 ̂η ( nx
m − δ)



= x
m
 

̂η(−δ) + O∗
 

∑

n̸=0
 1
(2π ( nx
m − δ))2
 

 · ∣
∣
∣ ̂η′′∣
∣
∣
∞




= x
m ̂η(−δ) + m
x c0
(2π)2 O∗
 

max
|r|≤ 1
2
 ∑

n̸=0
 1
(n − r)2
 

 .

Since x ↦→ 1/x2 is convex on R+,

max
|r|≤ 1
2
 ∑

n̸=0
 1
(n − r)2 = ∑

n̸=0
 1
(
n − 1
2 )2 = π2 − 4.

16 H. A. HELFGOTT

Therefore, the sum of all terms with m ≤ M and q|m is

∑

m≤M
q|m
 x
m ̂η(−δ) + ∑

m≤M
q|m
 m
x c0
(2π)2 (π2 − 4)

= xµ(q)
q · ̂η(−δ) · ∑

m≤ M
q
gcd(m,q)=1
 µ(m)
m

+ O∗ (µ(q)
2c0
 ( 1
4 − 1
π2
 ) ( D2

2xq + D
2x
 )) .

.

We bound |̂η(−δ)| by (2.1).
Let
 Tm(α) = ∑

n e(αmn)η ( mn
x
 ) .

Then, by (2.2) and Lemma 2.1,

(3.13) |Tm(α)| ≤ min
 ( x
m + 1
2 |η′|1,
 1
2 |η′|1
| sin(πmα)| , m
x c0
4 1
(sin πmα)2
 )
 .

For any y2 > y1 > 0 with y2 − y1 ≤ q and y2 ≤ Q/2, (3.13) gives us that

(3.14) ∑

y1<m≤y2
q∤m
 |Tm(α)| ≤ ∑

y1<m≤y2
q∤m
 min (A, C
(sin πmα)2
 )

for A = (x/y1)(1+ |η′|1/(2(x/y1))) and C = (c0/4)(y2/x). We must now estimate
the sum

(3.15) ∑

m≤M
q∤m
 |Tm(α)| + ∑

Q
2 <m≤D |Tm(α)|.

To bound the terms with m ≤ M , we can use Lemma 3.2. The question is then
which one is smaller: the ﬁrst or the second bound given by Lemma 3.2? A brief
calculation gives that the second bound is smaller (and hence preferable) exactly
when √C/A > (3π/10q)(1 + √13/3). Since √C/A ∼ (
√c0/2)m/x, this means
that it is sensible to prefer the second bound in Lemma 3.2 when m > c2x/q,
where c2 = (3π/5
√c0)(1 + √13/3).
It thus makes sense to ask: does Q/2 ≤ c2x/q (so that m ≤ M implies m ≤
c2x/q)? This question divides our work into two basic cases.
Case (a). δ large: |δ| ≥ 1/2c2, where c2 = (3π/5
√c0)(1 + √13/3). Then
Q/2 ≤ c2x/q; this will induce us to bound the ﬁrst sum in (3.15) by the very ﬁrst
bound in Lemma 3.2.

MINOR ARCS FOR GOLDBACH’S PROBLEM 17

Recall that M = min(Q/2, D), and so M ≤ c2x/q. By (3.14) and Lemma 3.2,
(3.16)
∑

1≤m≤M
q∤m
 |Tm(α)| ≤
 ∞∑

j=0
 ∑

jq<m≤min((j+1)q,M )
q∤m
 min
 ( x
jq + 1 + |η′|1
2 ,
 c0
4 (j+1)q
x
(sin πmα)2
 )

≤ 20
3π2 c0q3

4x
 ∑

0≤j≤ M
q
 (j + 1) ≤ 20
3π2 c0q3

4x · ( 1
2 M 2

q2 + 3
2 c2x
q2 + 1
)

≤ 5c0c2
6π2 M + 5c0q
3π2
 ( 3
2 c2 + q2

x
 ) ≤ 5c0c2
6π2 M + 35c0c2
6π2 q,

where, to bound the smaller terms, we are using the inequality Q/2 ≤ c2x/q,
and where we are also using the observation that, since |δ/x| ≤ 1/qQ0, the
assumption |δ| ≥ 1/2c2 implies that q ≤ 2c2x/Q0; moreover, since q ≤ Q0, this
gives us that q2 ≤ 2c2x. In the main term, we are bounding qM 2/x from above
by M · qQ/2x ≤ M/2δ ≤ c2M .
If D ≤ (Q + 1)/2, then M ≥ ⌊D⌋ and so (3.16) is all we need. Assume from
now on that D > (Q + 1)/2. The ﬁrst sum in (3.15) is then bounded by (3.16)
(with M = Q/2). To bound the second sum in (3.15), we use the approximation
a′/q′ instead of a/q. By (3.14) (without the restriction q ∤ m) and Lemma 3.1,

∑

Q/2<m≤D |Tm(α)| ≤
 ∞∑

j=0
 ∑

jq′+ Q
2 <m≤min((j+1)q′+Q/2,D) |Tm(α)|

≤
 ⌊ D−(Q+1)/2
q′ ⌋
∑

j=0
 (
3c1 x

jq′ + Q+1
2 + 4q′

π
 √ c1c0
4 x
jq′ + (Q + 1)/2 (j + 1)q′ + Q/2
x
 )

≤
 ⌊ D−(Q+1)/2
q′ ⌋
∑

j=0
 (
3c1 x

jq′ + Q+1
2 + 4q′

π
 √ c1c0
4
 (1 + q′

jq′ + (Q + 1)/2
 ))
 ,

where we recall that c1 = 1 + |η′|1/(2x/D). Since q′ ≥ (ǫ/(1 + ǫ))Q,

(3.17)
 ⌊ D−(Q+1)/2
q′ ⌋
∑

j=0
 x

jq′ + Q+1
2 ≤ x
Q/2 + x
q′
 ∫ D

Q+1
2
 1
t dt ≤ 2x
Q + (1 + ǫ)x
ǫQ log+ D
Q+1
2 .

Recall now that q′ ≤ (1 + ǫ)Q + 1 ≤ (1 + ǫ)(Q + 1). Therefore,
(3.18)

q′
 ⌊ D−(Q+1)/2
q′ ⌋
∑

j=0
 √
1 + q′

jq′ + (Q + 1)/2 ≤ q′√
1 + (1 + ǫ)Q + 1
(Q + 1)/2 + ∫ D

Q+1
2
 √
1 + q′

t dt

≤ q′√3 + 2ǫ + (D − Q + 1
2
 ) + q′

2 log+ D
Q+1
2 .

18 H. A. HELFGOTT

We conclude that ∑Q/2<m≤D |Tm(α)| is at most
(3.19)
2
√c0c1
π
 (
D + ((1 + ǫ)
√3 + 2ǫ − 1
2
 ) (Q + 1) + (1 + ǫ)Q + 1
2 log+ D
Q+1
2
 )

+ 3c1
 (
2 + (1 + ǫ)
ǫ log+ D
Q+1
2
 ) x
Q

We sum this to (3.16) (with M = Q/2), and obtain that (3.15) is at most

(3.20)
 2
√c0c1
π
 (
D + (1 + ǫ)(Q + 1)
 (
̟ǫ + 1
2 log+ D
Q+1
2
 ))

+ 3c1
 (
2 + (1 + ǫ)
ǫ log D
Q+1
2
 ) x
Q + 35c0c2
6π2 q,

where we are bounding
(3.21)
5c0c2
6π2 = 5c0
6π2 3π
5
√c0
 (
1 +
 √ 13
3
 )
 = √c0
2π
 (
1 +
 √ 13
3
 )
 ≤ 2
√c0c1
π · 1
4
 (
1 +
 √ 13
3
 )

and deﬁning

(3.22) ̟ǫ = √3 + 2ǫ +
 ( 1
4
 (
1 +
 √ 13
3
 )
 − 1

) 1
2(1 + ǫ) .

(Note that ̟ǫ < √3 for ǫ < 0.1741). A quick check against (3.16) shows that
(3.20) is valid also when D ≤ Q/2, even when Q+1 is replaced by min(Q+1, 2D).
We bound Q from above by x/|δ|q and log+ D/((Q+1)/2) by log+ 2D/(x/|δ|q+1),
and obtain the result.
Case (b): |δ| small: |δ| ≤ 1/2c2 or D ≤ Q0/2. Then min(c2x/q, D) ≤ Q/2.
We start by bounding the ﬁrst q/2 terms in (3.15) by (3.13) and Lemma 3.3:

(3.23)
 ∑

m≤q/2 |Tm(α)| ≤ ∑

m≤q/2 min
 ( 1
2 |η′|1
| sin(πmα)| , c0q/8x
| sin(πmα)|2
 )

≤ |η′|1
π q max (2, log c0e3q2

4π|η′|1x
 ) .

If q2 < 2c2x, we estimate the terms with q/2 < m ≤ c2x/q by Lemma 3.2,
which is applicable because min(c2x/q, D) < Q/2:
(3.24)
∑

q
2 <m≤D′

q∤m
 |Tm(α)| ≤
 ∞∑

j=1
 ∑

(j− 1
2 )q<m≤(j+ 1
2 )q

m≤min
( c2x
q ,D)

q∤m
 min
 ( x
(j − 1
2 ) q + |η′
1|
2 ,
 c0
4 (j+1/2)q
x
(sin πmα)2
 )

≤ 20
3π2 c0q3

4x
 ∑

1≤j≤ D′
q + 1
2
 (j + 1
2
 ) ≤ 20
3π2 c0q3

4x
 ( c2x
2q2 D′

q + 3
2
 ( c2x
q2
 ) + 5
8
 )

≤ 5c0
6π2
 (c2D′ + 3c2q + 5
4 q3

x
 ) ≤ 5c0c2
6π2
 (D′ + 11
2 q) ,

MINOR ARCS FOR GOLDBACH’S PROBLEM 19

where we write D′ = min(c2x/q, D). If c2x/q ≥ D, we stop here. Assume that
c2x/q < D. Let R = max(c2x/q, q/2). The terms we have already estimated are
precisely those with m ≤ R. We bound the terms R < m ≤ D by the second
bound in Lemma 3.1:

(3.25)
 ∑

R<m≤D|Tm(α)| ≤
 ∞∑

j=0
 ∑

m>jq+R
m≤min((j+1)q+R,D)
 min
 ( c1x
jq + R ,
 c0
4 (j+1)q+R
x
(sin πmα)2
 )

≤
 ⌊ 1
q (D−R)⌋
∑

j=0
 3c1x
jq + R + 4q
π
 √ c1c0
4
 (1 + q
jq + R
 )

(Note there is no need to use two successive approximations a/q, a′/q′ as in case
(a). We are also including all terms with m divisible by q, as we may, since
|Tm(α)| is non-negative.) Now, much as before,

(3.26)
 ⌊ 1
q (D−R)⌋
∑

j=0
 x
jq + R ≤ x
R + x
q
 ∫ D

R
 1
t dt ≤ min ( q
c2 , 2x
q
 ) + x
q log+ D
c2x/q ,

and
(3.27)
⌊ 1
q (D−R)⌋
∑

j=0
 √1 + q
jq + R ≤ √1 + q
R + 1
q
 ∫ D

R
 √1 + q
t dt ≤ √3+ D − R
q + 1
2 log+ D
q/2 .

We sum with (3.23) and (3.24), and we obtain that (3.15) is at most

(3.28)
 2
√c0c1
π
 (√
3q + D + q
2 log+ D
q/2
 ) + (
3c1 log+ D
c2x/q
 ) x
q

+ 3c1 min ( q
c2 , 2x
q
 ) + 55c0c2
12π2 q + |η′|1
π q · max (2, log c0e3q2

4π|η′|1x
 ) ,

where we are using the fact that 5c0c2/6π2 < 2
√c0c1/π. A quick check against
(3.24) shows that (because of the fact just stated) (3.28) is also valid when c2x/q ≥
D. □

We will need a version of Lemma 3.4 with m and n restricted to the odd
numbers. (We will barely be using the restriction of m, whereas the restriction
on n is both (a) slightly harder to deal with, (b) something that can be turned
to our advantage.)

Lemma 3.5. Let α ∈ R/Z with 2α = a/q + δ/x, gcd(a, q) = 1, |δ/x| ≤ 1/qQ0,
q ≤ Q0, Q0 ≥ 16. Let η be continuous, piecewise C 2 and compactly supported,
with |η|1 = 1 and η′′ ∈ L1. Let c0 ≥ | ̂η′′|∞.
Let 1 ≤ D ≤ x. Then, if |δ| ≤ 1/2c2, where c2 = 6π/5
√c0, the absolute value
of

(3.29) ∑

m≤D
m odd
 µ(m) ∑

n odd e(αmn)η ( mn
x
 )

20 H. A. HELFGOTT

is at most
(3.30)

x
2q min (1, c0
(πδ)2
 )
 ∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
 ∑

m≤ M
q
gcd(m,2q)=1
 µ(m)
m
 ∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
 + O∗ ( c0q
x
 ( 1
8 − 1
2π2
 ) ( D
q + 1
)2)

plus

(3.31)
 2
√c0c1
π D + 3c1
2 x
q log+ D
c2x/q + √c0c1
π q log+ D
q/2

+ 2|η′|1
π q · max (1, log c0e3q2

4π|η′|1x
 ) + ( 2
√3c0c1
π + 3c1
2c2 + 55c0c2
6π2
 ) q,

where c1 = 1 + |η′|1/(x/D) and M ∈ [min(Q0/2, D), D]. The same bound holds
if |δ| ≥ 1/2c2 but D ≤ Q0/2.
In general, if |δ| ≥ 1/2c2, the absolute value of (3.8) is at most (3.30) plus

(3.32)
 2
√c0c1
π
 (
D + (1 + ǫ) min (⌊ x
|δ|q
 ⌋ + 1, 2D) (√
3 + 2ǫ + 1
2 log+ 2D
x
|δ|q
 ))

+ 3
2 c1
 (
2 + (1 + ǫ)
ǫ log+ 2D
x
|δ|q
 ) x
Q0 + 35c0c2
3π2 q,

for ǫ ∈ (0, 1] arbitrary.

If q is even, the sum (3.30) can be replaced by 0.

Proof. The proof is almost exactly that of Lemma 3.4; we go over the diﬀerences.
The parameters Q, Q′, a′, q′ and M are deﬁned just as before (with 2α wherever
we had α).
Let us ﬁrst consider m ≤ M odd and divisible by q. (Of course, this case arises
only if q is odd.) For n = 2r + 1,

e(αmn) = e(αm(2r + 1)) = e(2αrm)e(αm) = e ( δ
x rm) e (( a
2q + δ
2x + κ
2
 ) m)

= e ( δ(2r + 1)
2x m) e ( a + κq
2 m
q
 ) = κ
′e ( δ(2r + 1)
2x m) ,

where κ ∈ {0, 1} and κ′ = e((a + κq)/2) ∈ {−1, 1} are independent of m and n.
Hence, by Poisson summation,

(3.33)
 ∑

n odd e(αmn)η(mn/x) = κ
′ ∑

n odd e((δm/2x)n)η(mn/x)

= κ′

2
 (∑

n ̂f (n) − ∑

n ̂f (n + 1/2)

)
 ,

where f (u) = e((δm/2x)u)η((m/x)u). Now

̂f (t) = x
m ̂η ( x
m t − δ
2
 ) .

MINOR ARCS FOR GOLDBACH’S PROBLEM 21

Just as before, |x/m| ≥ 2|δq| ≥ 2δ. Thus
(3.34)

1
2
 ∣
∣
∣
∣
∣

∑

n ̂f (n) − ∑

n ̂f (n + 1/2)

∣
∣
∣
∣
∣ ≤ x
m
 

 1
2
 ∣
∣
∣
∣̂η (− δ
2
 )∣
∣
∣
∣ + 1
2
 ∑

n̸=0
 ∣
∣
∣
∣̂η ( x
m n
2 − δ
2
 )∣
∣
∣
∣





= x
m
 

 1
2
 ∣
∣
∣
∣̂η (− δ
2
 )∣
∣
∣
∣ + 1
2 · O∗
 

∑

n̸=0
 1
(
π ( nx
m − δ))2
 

 · ∣
∣
∣ ̂η′′∣
∣
∣
∞




= x
2m
 ∣
∣
∣
∣̂η (− δ
2
 )∣
∣
∣
∣ + m
x c0
2π2 (π2 − 4)x.

The contribution of the second term in the last line of (3.34) is

∑

m≤M
m odd
q|m
 m
x c0
2π2 (π2 − 4) = q
x c0
2π2 (π2 − 4) · ∑

m≤M/q
m odd
 m = qc0
x
 ( 1
8 − 1
2π2
 ) ( M
q + 1
)2 .

Hence, the absolute value of the sum of all terms with m ≤ M and q|m is given
by (3.30).
We deﬁne Tm,◦(α) by

(3.35) Tm,◦(α) = ∑

n odd e(αmn)η ( mn
x
 ) .

Changing variables by n = 2r + 1, we see that

|Tm,◦(α)| =
 ∣
∣
∣
∣
∣

∑

r e(2α · mr)η(m(2r + 1)/x)

∣
∣
∣
∣
∣ .

Hence, instead of (3.13), we get that

(3.36) |Tm,◦(α)| ≤ min
 ( x
2m + 1
2 |η′|1,
 1
2 |η′|1
| sin(2πmα)| , m
x c0
2 1
(sin 2πmα)2
 )
 .

We obtain (3.14), but with Tm,◦ instead of Tm, A = (x/2y1)(1 + |η′|1/(x/y1)) and
C = (c0/2)(y2/x), and so c1 = 1 + |η′|1/(x/D).
The rest of the proof of Lemma 3.4 carries almost over word-by-word. (For
the sake of simplicity, we do not really try to take advantage of the odd support
of m here.) Since C has doubled, it would seem to make sense to reset the value
of c2 to be c2 = (3π/5
√2c0)(1 + √
13/3); this would cause complications related
to the fact that 5c0c2/3π2 would become larger than 2
√c0/π, and so we set c2 to
the slightly smaller value c2 = 6π/5
√c0 instead. This implies

(3.37) 5c0c2
3π2 = 2
√c0
π .

The bound from (3.16) gets multiplied by 2 (but the value of c2 has changed),
the second line in (3.19) gets halved, (3.21) gets replaced by (3.37), the second
term in the maximum in the second line of (3.23) gets doubled, the bound from
(3.24) gets doubled, and the bound from (3.26) gets halved. □

We will also need a version of Lemma 3.4 (or rather Lemma 3.5; we will decide
to work with the restriction that n and m be odd) with a factor of (log n) within
the inner sum.

22 H. A. HELFGOTT

Lemma 3.6. Let α ∈ R/Z with 2α = a/q + δ/x, gcd(a, q) = 1, |δ/x| ≤ 1/qQ0,
q ≤ Q0, Q0 ≥ max(16, 2
√x). Let η be continuous, piecewise C 2 and compactly
supported, with |η|1 = 1 and η′′ ∈ L1. Let c0 ≥ | ̂η′′|∞. Assume that, for any
ρ ≥ ρ0, ρ0 a constant, the function η(ρ)(t) = log(ρt)η(t) satisﬁes

(3.38) |η(ρ)|1 ≤ log(ρ)|η|1, |η′
(ρ)|1 ≤ log(ρ)|η′|1, |̂η′′
(ρ)|∞ ≤ c0 log(ρ)

Let √
3 ≤ D ≤ min(x/ρ0, x/e). Then, if |δ| ≤ 1/2c2, where c2 = 6π/5
√c0, the
absolute value of

(3.39) ∑

m≤D
m odd
 µ(m) ∑

n
n odd
(log n)e(αmn)η ( mn
x
 )

is at most
(3.40)

x
q min (1, c0/δ2

(2π)2
 )
 ∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
 ∑

m≤ M
q
gcd(m,q)=1
 µ(m)
m log x
mq
 ∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
 + x
q | ̂log ·η(−δ)|
 ∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
 ∑

m≤ M
q
gcd(m,q)=1
 µ(m)
m
 ∣
∣
∣
∣
∣
∣
∣
∣
∣
∣

+ O∗ (
c0
 ( 1
2 − 2
π2
 ) ( D2

4qx log e1/2x
D + 1
e
 ))

plus
(3.41)
2
√c0c1
π D log ex
D + 3c1
2 x
q log+ D
c2x/q log q
c2

+ ( 2|η′|1
π max (1, log c0e3q2

4π|η′|1x
 ) log x + 2
√c0c1
π
 (√
3 + 1
2 log+ D
q/2
 ) log q
c2
 ) q

+ 3c1
2
 √2x
c2 log 2x
c2 + 20c0c
3/2
2
3π2 √2x log 2
√ex
c2
for c1 = 1 + |η′|1/(x/D). The same bound holds if |δ| ≥ 1/2c2 but D ≤ Q0/2.
In general, if |δ| ≥ 1/2c2, the absolute value of (3.39) is at most
(3.42)
2
√c0c1
π D log ex
D +

2
√c0c1
π (1 + ǫ) ( x
|δ|q + 1
) (√
3 + 2ǫ · log+ 2
√e|δ|q + 1
2 log+ 2D
x
|δ|q log+ 2|δ|q
)

+ ( 3c1
4
 ( 2
√5 + 1 + ǫ
2ǫ log x) + 40
3
 √2c0c
3/2
2
 ) √
x log x

for ǫ ∈ (0, 1].

Proof. Deﬁne Q, Q′, M , a′ and q′ as in the proof of Lemma 3.4. The same
method of proof works as for Lemma 3.4; we go over the diﬀerences. When
applying Poisson summation or (2.2), use η(x/m)(t) = (log xt/m)η(t) instead of
η(t). Then use the bounds in (3.38) with ρ = x/m; in particular,

| ̂η′′
(x/m)|∞ ≤ c0 log x
m .

MINOR ARCS FOR GOLDBACH’S PROBLEM 23

For f (u) = e((δm/2x)u)(log u)η((m/x)u),

̂f (t) = x
m ̂η(x/m)
 ( x
m t − δ
2
 )

and so

1
2
 ∑

n
 ∣
∣
∣ ̂f (n/2)
∣
∣
∣ ≤ x
m
 

 1
2
 ∣
∣
∣
∣ ̂η(x/m)
 (− δ
2
 )∣
∣
∣
∣ + 1
2
 ∑

n̸=0
 ∣
∣
∣
∣̂η ( x
m n
2 − δ
2
 )∣
∣
∣
∣





= 1
2 x
m
 ( ̂log ·η (− δ
2
 ) + log ( x
m
 ) ̂η (− δ
2
 )) + m
x
 (
log x
m
 ) c0
2π2 (π2 − 4).

The part of the main term involving log(x/m) becomes

x̂η(−δ)
2
 ∑

m≤M
m odd
q|m
 µ(m)
m log ( x
m
 ) = xµ(q)
q ̂η(−δ) · ∑

m≤M/q
gcd(m,2q)=1
 µ(m)
m log ( x
mq
 )

for q odd. (We can see that this, like the rest of the main term, vanishes for m
even.)
In the term in front of π2 − 4, we ﬁnd the sum
∑

m≤M
m odd
q|m
 m
x log ( x
m
 ) ≤ M
x log x
M + q
2
 ∫ M/q

0 t log x/q
t dt = M
x log x
M + M 2

4qx log e1/2x
M ,

where we use the fact that t ↦→ t log(x/t) is increasing for t ≤ x/e. By the same
fact (and by M ≤ D), (M 2/q) log(e1/2x/M ) ≤ (D2/q) log(e1/2x/D). It is also
easy to see that (M/x) log(x/M ) ≤ 1/e (since M ≤ D ≤ x).
The basic estimate for the rest of the proof (replacing (3.13)) is

Tm,◦(α) = ∑

n odd e(αmn)(log n)η ( mn
x
 ) = ∑

n odd e(αmn)η(x/m) ( mn
x
 )

= O∗
 

min
 

 x
2m |η(x/m)|1 + |η′
(x/m)|1
2 ,
 1
2 |η′
(x/m)|1
| sin(2πmα)| , m
x
 1
2 | ̂η′′
(x/m)|∞
(sin 2πmα)2
 






= O∗ (
log x
m · min
 ( x
2m + |η′|1
2 ,
 1
2 |η′|1
| sin(2πmα)| , m
x c0
2 1
(sin 2πmα)2
 ))
 .

We wish to bound

(3.43) ∑

m≤M
q∤m
m odd
 |Tm,◦(α)| + ∑

Q
2 <m≤D |Tm,◦(α)|.

Just as in the proofs of Lemmas 3.4 and 3.5, we give two bounds, one valid for
|δ| large (|δ| ≥ 1/2c2) and the other for δ small (|δ| ≤ 1/2c2). Again as in the
proof of Lemma 3.5, we ignore the condition that m is odd in (3.15).
Consider the case of |δ| large ﬁrst. Instead of (3.16), we have

(3.44) ∑

1≤m≤M
q∤m
 |Tm(α)| ≤ 40
3π2 c0q3

2x
 ∑

0≤j≤ M
q
 (j + 1) log x
jq + 1 .

24 H. A. HELFGOTT

Since

∑

0≤j≤ M
q
 (j + 1) log x
jq + 1 ≤ log x + M
q log x
M + ∑

1≤j≤ M
q
 log x
jq + ∑

1≤j≤ M
q −1 j log x
jq

≤ log x + M
q log x
M + ∫ M
q

0 log x
tq dt + ∫ M
q

1 t log x
tq dt

≤ log x + ( 2M
q + M 2

2q2
 ) log e1/2x
M ,

this means that

(3.45)
 ∑

1≤m≤M
q∤m
 |Tm(α)| ≤ 40
3π2 c0q3

4x
 (
log x + ( 2M
q + M 2

2q2
 ) log e1/2x
M
 )

≤ 5c0c2
3π2 M log √ex
M + 40
3
 √2c0c
3/2
2 √
x log x,

where we are using the bounds M ≤ Q/2 ≤ c2x/q and q2 ≤ 2c2x (just as in
(3.16)). Instead of (3.17), we have

⌊ D−(Q+1)/2
q′ ⌋
∑

j=0
 (
log x

jq′ + Q+1
2
 ) x

jq′ + Q+1
2 ≤ x
Q/2 log 2x
Q + x
q′
 ∫ D

Q+1
2 log x
t dt
t

≤ 2x
Q log 2x
Q + x
q′ log 2x
Q log+ 2D
Q ;

recall that the coeﬃcient in front of this sum will be halved by the condition that
n is odd. Instead of (3.18), we obtain

q′
 ⌊ D−(Q+1)/2
q′ ⌋
∑

j=0
 √
1 + q′

jq′ + (Q + 1)/2
 (
log x

jq′ + Q+1
2
 )

≤ q′√3 + 2ǫ · log 2x
Q + 1 + ∫ D

Q+1
2
 (1 + q′

2t
 ) (log x
t
 ) dt

≤ q′√3 + 2ǫ · log 2x
Q + 1 + D log ex
D − Q + 1
2 log 2ex
Q + 1 + q′

2 log 2x
Q + 1 log 2D
Q + 1 .

(The bound ∫ b
a log(x/t)dt/t ≤ log(x/a) log(b/a) will be more practical than the
exact expression for the integral.) Hence ∑Q/2<m≤D |Tm(α)| is at most

2
√c0c1
π D log ex
D

+ 2
√c0c1
π
 ((1 + ǫ)
√3 + 2ǫ + (1 + ǫ)
2 log 2D
Q + 1
 ) (Q + 1) log 2x
Q + 1

− 2
√c0c1
π · Q + 1
2 log 2ex
Q + 1 + 3c1
2
 ( 2
√5 + 1 + ǫ
ǫ log+ D
Q/2
 ) √
x log √x.

MINOR ARCS FOR GOLDBACH’S PROBLEM 25

Summing this to (3.45) (with M = Q/2), and using (3.21) and (3.22) as before,
we obtain that (3.43) is at most

2
√c0c1
π D log ex
D

+ 2
√c0c1
π (1 + ǫ)(Q + 1) (√
3 + 2ǫ log+ 2
√ex
Q + 1 + 1
2 log+ 2D
Q + 1 log+ 2x
Q + 1
 )

+ 3c1
2
 ( 2
√
5 + 1 + ǫ
ǫ log+ D
Q/2
 ) √x log √x + 40
3
 √2c0c
3/2
2 √x log x.

Now we go over the case of |δ| small (or D ≤ Q0/2). Instead of (3.23), we have

(3.46) ∑

m≤q/2 |Tm,◦(α)| ≤ 2|η′|1
π q max (1, log c0e3q2

4π|η′|1x
 ) log x.

Suppose q2 < 2c2x. Instead of (3.24), we have
(3.47)
∑

q
2 <m≤D′

q∤m
 |Tm,◦(α)| ≤ 40
3π2 c0q3

6x
 ∑

1≤j≤ D′
q + 1
2
 (j + 1
2
 ) log x
(j − 1
2 ) q

≤ 10c0q3

3π2x
 (
log 2x
q + 1
q
 ∫ D′

0 log x
t dt + 1
q
 ∫ D′

0 t log x
t dt + D′

q log x
D′
 )

= 10c0q3

3π2x
 (log 2x
q + (2D′

q + (D′)2

2q2
 ) log √ex
D′
 )

≤ 5c0c2
3π2
 (4
√2c2x log 2x
q + 4
√2c2x log √ex
D′ + D′ log √ex
D′
 )

≤ 5c0c2
3π2
 (D′ log √ex
D′ + 4
√2c2x log 2
√e
c2 x)

where D′ = min(c2x/q, D). (We are using the bounds q3/x ≤ (2c2)3/2, D′q2/x ≤
c2q < c
3/2
2 √2x and D′q/x ≤ c2.) Instead of (3.25), we have

∑

R<m≤D|Tm,◦(α)| ≤
 ⌊ 1
q (D−R)⌋
∑

j=0
 ( 3c1
2 x
jq + R + 4q
π
 √ c1c0
4
 (1 + q
jq + R
 ))
 log x
jq + R ,

where R = max(c2x/q, q/2). We can simply reuse (3.26), multiplying it by
log x/R; we replace (3.27) by

q
 ⌊ 1
q (D−R)⌋
∑

j=0
 √1 + q
jq + R log x
jq + R ≤ q√1 + q
R log x
R + ∫ D

R
 √1 + q
t log x
t dt

≤ √3q log q
c2 + (
D log ex
D − R log ex
R
 ) + q
2 log q
c2 log+ D
R .

We sum with (3.46) and (3.47), and obtain (3.42) as an upper bound for (3.43).
□

We will apply the following only for q relatively large.

26 H. A. HELFGOTT

Lemma 3.7. Let α ∈ R/Z with 2α = a/q + δ/x, gcd(a, q) = 1, |δ/x| ≤ 1/qQ0,
q ≤ Q0, Q0 ≥ max(2e, 2
√x). Let η be continuous, piecewise C 2 and compactly
supported, with |η|1 = 1 and η′′ ∈ L1. Let c0 ≥ | ̂η′′|∞. Let c2 = 6π/5
√c0.
Assume that x ≥ e2c2/2.
Let U, V ≥ 1 satisfy U V + (19/18)Q0 ≤ x/5.6. Then, if |δ| ≤ 1/2c2, the
absolute value of

(3.48)
 ∣
∣
∣
∣
∣
∣
∣
∣
 ∑

v≤V
v odd
 Λ(v) ∑

u≤U
u odd
 µ(u) ∑

n
n odd
 e(αvun)η(vun/x)

∣
∣
∣
∣
∣
∣
∣
∣

is at most

(3.49)
 x
2q min (1, c0
(πδ)2
 ) log V q

+ O∗ ( 1
4 − 1
π2
 ) · c0
 ( D2 log V
2qx + 3c4
2 U V 2

x + (U + 1)2V
2x log q)

plus

(3.50)
 2
√c0c1
π
 (
D log D
√e + q (√3 log c2x
q + log D
2 log+ D
q/2
 ))

+ 3c1
2 x
q log D log+ D
c2x/q + 2|η′|1
π q max (
1, log c0e3q2

4π|η′|1x
 ) log q
2

+ 3c1
2
√2c2
 √x log c2x
2 + 25c0
4π2 (2c2)
3/2√x log x,

where D = U V and c1 = 1 + |η′|1/(2x/D) and c4 = 1.03884. The same bound
holds if |δ| ≥ 1/2c2 but D ≤ Q0/2.
In general, if |δ| ≥ 1/2c2, the absolute value of (3.48) is at most (3.49) plus
(3.51)
2
√c0c1
π D log D
e

+ 2
√c0c1
π (1 + ǫ) ( x
|δ|q + 1
) (

(
√3 + 2ǫ − 1) log
 x
|δ|q + 1
√2 + 1
2 log D log+ e2D
x
|δ|q
 )

+ ( 3c1
2
 ( 1
2 + 3(1 + ǫ)
16ǫ log x) + 20c0
3π2 (2c2)
3/2) √x log x

for ǫ ∈ (0, 1].

Proof. We proceed essentially as in Lemma 3.4 and Lemma 3.5. Let Q, q′ and
Q′ be as in the proof of Lemma 3.5, that is, with 2α where Lemma 3.4 uses α.
Let M = min(U V, Q/2). We ﬁrst consider the terms with uv ≤ M , u and v
odd, uv divisible by q. If q is even, there are no such terms. Assume q is odd.
Then, by (3.33) and (3.34), the absolute value of the contribution of these terms
is at most

(3.52) ∑

a≤M
a odd
q|a
 





 ∑

v|a
a/U ≤v≤V
 Λ(v)µ(a/v)







 (x̂η(−δ/2)
2a + O
 ( a
x | ̂η′′|∞
2π2 · (π2 − 4)

))
 .

MINOR ARCS FOR GOLDBACH’S PROBLEM 27

Now

∑

a≤M
a odd
q|a
 ∑

v|a
a/U ≤v≤V
 Λ(v)µ(a/v)
a

= ∑

v≤V
v odd
gcd(v,q)=1
 Λ(v)
v
 ∑

u≤min(U,M/V )
u odd
q|u
 µ(u)
u + ∑

pα≤V
p odd
p|q
 Λ(pα)
pα ∑

u≤min(U,M/V )
u odd
q
gcd(q,pα) |u
 µ(u)
u

= µ(q)
q
 ∑

v≤V
v odd
gcd(v,q)=1
 Λ(v)
v
 ∑

u≤min(U/q,M/V q)
gcd(u,2q)=1
 µ(u)
u

+ µ ( q
gcd(q,pα) )

q
 ∑

pα≤V
p odd
p|q
 Λ(pα)
pα/ gcd(q, pα)
 ∑

u≤min
( U
q/ gcd(q,pα) , M/V
q/ gcd(q,pα) )

u odd

gcd(
u, q
gcd(q,pα) )
=1
 µ(u)
u

= 1
q · O∗
 








 ∑

v≤V
gcd(v,2q)=1
 Λ(v)
v + ∑

pα≤V
p odd
p|q
 log p
pα/ gcd(q, pα)
 








 ,

where we are using (2.7) to bound the sums on u by 1. We notice that

∑

pα≤V
p odd
p|q
 log p
pα/ gcd(q, pα) ≤ ∑

p odd
p|q
 (log p)
 




vp(q) + ∑

α>vp(q)
pα≤V
 1
pα−vp(q)
 






≤ log q + ∑

p odd
p|q
 (log p) ∑

β>0
pβ≤ V

pvp(q)
 log p
pβ ≤ log q + ∑

v≤V
v odd
gcd(v,q)=1
 Λ(v)
v ,

and so
 ∑

a≤M
a odd
q|a
 ∑

v|a
a/U ≤v≤V
 Λ(v)µ(a/v)
a = 1
q · O∗
 





log q + ∑

v≤V
gcd(v,2)=1
 Λ(v)
v
 






= 1
q · O∗(log q + log V )

28 H. A. HELFGOTT

by (2.12). The absolute value of the sum of the terms with ̂η(−δ/2) in (3.52) is
thus at most
 x
q ̂η(−δ/2)
2 (log q + log V ) ≤ x
2q min (1, c0
(πδ)2
 ) log V q,

where we are bounding ̂η(−δ/2) by (2.1).
The other terms in (3.52) contribute at most

(3.53) (π2 − 4) | ̂η′′|∞
2π2 1
x
 ∑

u≤U
 ∑

v≤V
uv odd
uv≤M, q|uv
u sq-free
 Λ(v)uv.

For any R, ∑u≤R,u odd,q|u ≤ R2/4q + 3R/4. Using the estimates (2.12), (2.15)
and (2.16), we obtain that the double sum in (3.53) is at most
(3.54)∑

v≤V
gcd(v,2q)=1
Λ(v)v ∑

u≤min(U,M/v)
u odd
q|u
 u + ∑

pα≤V
p odd
p|q
 (log p)pα ∑

u≤U
u odd
q
gcd(q,pα) |u
 u

≤ ∑

v≤V
gcd(v,2q)=1
 Λ(v)v · ( (M/v)2

4q + 3M
4v
 ) + ∑

pα≤V
p odd
p|q
 (log p)pα · (U + 1)2

4

≤ M 2 log V
4q + 3c4
4 M V + (U + 1)2

4 V log q,

where c4 = 1.03884.
From this point onwards, we use the easy bound
∣
∣
∣
∣
∣
∣
∣
∣
∣
 ∑

v|a
a/U ≤v≤V
 Λ(v)µ(a/v)

∣
∣
∣
∣
∣
∣
∣
∣
∣
 ≤ log a.

What we must bound now is

(3.55) ∑

m≤U V
m odd
q ∤ m or m > M
(log m) ∑

n odd e(αmn)η(mn/x).

The inner sum is the same as the sum Tm,◦(α) in (3.35); we will be using the
bound (3.36). Much as before, we will be able to ignore the condition that m is
odd.
Let D = U V . What remains to do is similar to what we did in the proof of
Lemma 3.4 (or Lemma 3.5).
Case (a). δ large: |δ| ≥ 1/2c2. Instead of (3.16), we have

∑

1≤m≤M
q∤m
 (log m)|Tm,◦(α)| ≤ 40
3π2 c0q3

4x
 ∑

0≤j≤ M
q
 (j + 1) log(j + 1)q,

MINOR ARCS FOR GOLDBACH’S PROBLEM 29

and, since M ≤ min(c2x/q, D), q ≤ √
2c2x (just as in the proof of Lemma 3.4)
and

∑

0≤j≤ M
q
 (j + 1) log(j + 1)q ≤ M
q log M + ( M
q + 1
) log(M + 1) + 1
q2
 ∫ M

0 t log t dt

≤ (2 M
q + 1
) log x + M 2

2q2 log M
√e ,

we conclude that

(3.56)
 ∑

1≤m≤M
q∤m
 |Tm,◦(α)| ≤ 5c0c2
3π2 M log M
√
e + 20c0
3π2 (2c2)
3/2√x log x.

Instead of (3.17), we have

⌊ D−(Q+1)/2
q′ ⌋
∑

j=0
 x

jq′ + Q+1
2 log (jq′ + Q + 1
2
 ) ≤ x
Q+1
2 log Q + 1
2 + x
q′
 ∫ D

Q+1
2
 log t
t dt

≤ 2x
Q log Q
2 + (1 + ǫ)x
2ǫQ
 (
(log D)
2 − (log Q
2
 )2)
 .

Instead of (3.18), we estimate

q′
 ⌊ D− Q+1
2
q′
 ⌋

∑

j=0
 (log ( Q + 1
2 + jq′)) √
1 + q′

jq′ + Q+1
2

≤ q′ (log D + (
√3 + 2ǫ − 1) log Q + 1
2
 ) + ∫ D

Q+1
2 log t dt + ∫ D

Q+1
2
 q′ log t
2t dt

≤ q′ (log D + (√3 + 2ǫ − 1
) log Q + 1
2
 ) + (D log D
e − Q + 1
2 log Q + 1
2e
 )

+ q′

2 log D log+ D
Q+1
2 .

We conclude that, when D ≥ Q/2, the sum ∑Q/2<m≤D(log m)|Tm(α)| is at most

2
√c0c1
π
 (D log D
e + (Q + 1) ((1 + ǫ)(
√3 + 2ǫ − 1) log Q + 1
2 − 1
2 log Q + 1
2e
 ))

+ √c0c1
π (Q + 1)(1 + ǫ) log D log+ e2D
Q+1
2

+ 3c1
2
 ( 2x
Q log Q
2 + (1 + ǫ)x
2ǫQ
 (
(log D)
2 − (log Q
2
 )2))
 .

We must now add this to (3.56). Since

(1 + ǫ)(
√3 + 2ǫ − 1) log √2 − 1
2 log 2e + 1 + √13/3
2 log 2
√e > 0

30 H. A. HELFGOTT

and Q ≥ 2
√x, we conclude that (3.55) is at most
(3.57)
2
√c0c1
π D log D
e

+ 2
√c0c1
π (1 + ǫ)(Q + 1)
 (
(
√3 + 2ǫ − 1) log Q + 1
√2 + 1
2 log D log+ e2D
Q+1
2
 )

+ ( 3c1
2
 ( 1
2 + 3(1 + ǫ)
16ǫ log x) + 20c0
3π2 (2c2)
3/2) √x log x.

Case (b). δ small: |δ| ≤ 1/2c2 or D ≤ Q0/2. The analogue of (3.23) is a
bound of
 ≤ 2|η′|1
π q max (
1, log c0e3q2

4π|η′|1x
 ) log q
2

for the terms with m ≤ q/2. If q2 < 2c2x, then, much as in (3.24), we have

(3.58)
 ∑

q
2 <m≤D′

q∤m
 |Tm,◦(α)|(log m) ≤ 10
π2 c0q3

3x
 ∑

1≤j≤ D′
q + 1
2
 (
j + 1
2
 ) log(j + 1/2)q

≤ 10
π2 c0q
3x
 ∫ D′+ 3
2 q

q x log x dx.

Since ∫ D′+ 3
2 q

q x log x dx = 1
2
 (
D′ + 3
2 q)2 log D′ + 3
2 q
√
e − 1
2 q2 log q
√
e

= ( 1
2 D′2 + 3
2 D′q) (log D′
√e + 3
2 q
D′
 ) + 9
8 q2 log D′ + 3
2 q
√e − 1
2 q2 log q
√e

= 1
2 D′2 log D′
√
e + 3
2 D′q log D′ + 9
8 q2 ( 2
9 + 3
2 + log (D′ + 19
18 q)) ,

where D′ = min(c2x/q, D), and since the assumption (U V + (19/18)Q0) ≤ x/5.6
implies that (2/9 + 3/2 + log(D′ + (19/18)q)) ≤ x, we conclude that

(3.59)
 ∑

q
2 <m≤D′

q∤m
 |Tm,◦(α)|(log m)

≤ 5c0c2
3π2 D′ log D′
√e + 10c0
3π2
 ( 3
4 (2c2)
3/2√x log x + 9
8 (2c2)
3/2√x log x)

≤ 5c0c2
3π2 D′ log D′
√e + 25c0
4π2 (2c2)
3/2√x log x.

Let R = max(c2x/q, q/2). We bound the terms R < m ≤ D as in (3.25), with a
factor of log(jq + R) inside the sum. The analogues of (3.26) and (3.27) are

(3.60)
 ⌊ 1
q (D−R)
⌋
∑

j=0
 x
jq + R log(jq + R) ≤ x
R log R + x
q
 ∫ D

R
 log t
t dt

≤ √ 2x
c2 log √ c2x
2 + x
q log D log+ D
R ,

MINOR ARCS FOR GOLDBACH’S PROBLEM 31

where we use the assumption that x ≥ e2c/2, and

(3.61)
 ⌊ 1
q (D−R)
⌋
∑

j=0 log(jq + R)
√1 + q
jq + R ≤ √3 log R

+ 1
q
 (D log D
e − R log R
e
 ) + 1
2 log D log D
R

(or 0 if D < R). We sum with (3.59) and the terms with m ≤ q/2, and obtain,
for D′ = c2x/q = R,

2
√c0c1
π
 (D log D
√e + q (√3 log c2x
q + log D
2 log+ D
q/2
 ))

+ 3c1
2 x
q log D log+ D
c2x/q + 2|η′|1
π q max (1, log c0e3q2

4π|η′|1x
 ) log q
2

+ 3c1
2
√2c2
 √x log c2x
2 + 25c0
4π2 (2c2)
3/2√x log x,

which, it is easy to check, is also valid even if D′ = D (in which case (3.60) and
(3.61) do not appear) or R = q/2 (in which case (3.59) does not appear). □

4. Type II

We must now consider the sum

(4.1) SII = ∑

m>U
gcd(m,v)=1
 



∑

d>U
d|m
 µ(d)





 ∑

n>V
gcd(n,v)=1
 Λ(n)e(αmn)η(mn/x).

Here the main improvements over classical treatments are as follows:
(1) obtaining cancellation in the term
∑

d>U
d|m
 µ(d)

leading to a gain of a factor of log;
(2) using a large sieve for primes, getting rid of a further log;
(3) exploiting, via a non-conventional application of the principle of the large
sieve (Lemma 4.3), the fact that α is in the tail of an interval (when that
is the case).
Some of the techniques developed for (1) should be applicable to other instances
of Vaughan’s identity in the literature.
It is technically helpful to express η as the (multiplicative) convolution of two
functions of compact support – preferrably the same function:

(4.2) η(x) = ∫ ∞

0 η1(t)η1(x/t) dt
t .

For the smoothing function η(t) = η2(t) = 4 max(log 2 − | log 2t|, 0), (4.2) holds
with

(4.3) η1(t) =
 {
2 if t ∈ (1/2, 1]
0 otherwise.

32 H. A. HELFGOTT

We will work with η1(t) as in (4.3) for convenience, yet what follows should carry
over to other (non-negative) choices of η1.
By (4.2), the sum (4.1) equals
(4.4)

4 ∫ ∞

0
 ∑

m>U
gcd(m,v)=1
 



∑

d>U
d|m
 µ(d)





 ∑

n>V
gcd(n,v)=1
 Λ(n)e(αmn)η1(t)η1
 ( mn/x
t
 ) dt
t

= 4 ∫ x/U

V
 ∑

max( x
2W ,U)<m≤ x
W
gcd(m,v)=1
 



∑

d>U
d|m
 µ(d)





 ∑

max(V, W
2 )<n≤W

gcd(n,v)=1
 Λ(n)e(αmn) dW
W

by the substitution t = (m/x)W . (We can assume V ≤ W ≤ x/U because
otherwise one of the sums in (4.5) is empty.)
We separate n prime and n non-prime. By Cauchy-Schwarz, the expres-
sion within the integral in (4.4) is then at most √S1(U, W ) · S2(U, V, W ) +√S1(U, W ) · S3(W ), where

(4.5)
 S1(U, W ) = ∑

max( x
2W ,U)<m≤ x
W
gcd(m,v)=1
 



∑

d>U
d|m
 µ(d)






2
 ,

S2(U, V, W ) = ∑

max( x
2W ,U)<m≤ x
W
gcd(m,v)=1
 ∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
 ∑

max(V, W
2 )<p≤W

gcd(p,v)=1
 (log p)e(αmp)

∣
∣
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

and

(4.6)
 S3(W ) = ∑

x
2W <m≤ x
W
gcd(m,v)=1
 ∣
∣
∣
∣
∣
∣
∣
∣
 ∑

n≤W
n non-prime
 Λ(n)

∣
∣
∣
∣
∣
∣
∣
∣
2

= ∑

x
2W <m≤ x
W
gcd(m,v)=1
 (
1.42620W 1/2)2 ≤ 1.0171x + 2.0341W

(by [RS62, Thm. 13]). We will assume V ≤ w; thus the condition gcd(p, v) = 1
will be fulﬁlled automatically and can be removed.
The contribution of S3(W ) will be negligible. We must bound S1(U, W ) and
S2(U, V, W ) from above.

4.1. The sum S1: cancellation. We shall bound

S1(U, W ) = ∑

max(U,x/2W )<m≤x/W
gcd(m,v)=1
 



∑

d>U
d|m
 µ(d)






2
 .

MINOR ARCS FOR GOLDBACH’S PROBLEM 33

There will be what is perhaps a surprising amount of cancellation: the expres-
sion within the sum will be bounded by a constant on average.

4.1.1. Reduction to a sum with µ. We can write
(4.7)
 ∑

max(U,x/2W )<m≤x/W
gcd(m,v)=1
 



∑

d>U
d|m
 µ(d)






2
 = ∑

x
2W <m≤ x
W
gcd(m,v)=1
 ∑

d1,d2|m µ(d1 > U )µ(d2 > U )

= ∑

r1<x/W U
 ∑

r2<x/W U
gcd(r1,r2)=1
gcd(r1r2,v)=1
 ∑

l
gcd(l,r1r2)=1
r1l,r2l>U
gcd(ℓ,v)=1
 µ(r1l)µ(r2l) ∑

x
2W <m≤ x
W
r1r2l|m
gcd(m,v)=1
 1,

where we write d1 = r1l, d2 = r2l, l = gcd(d1, d2). (The inequality r1 < x/W U
comes from r1r2l|m, m ≤ x/W , r2l > U ; r2 < x/W U is proven in the same way.)
Now (4.7) equals

(4.8) ∑

s< x
W U
gcd(s,v)=1
 ∑

r1< x
W U s
 ∑

r2< x
W U s
gcd(r1,r2)=1
gcd(r1r2,v)=1
 µ(r1)µ(r2) ∑

max( U
min(r1,r2) , x/W
2r1r2s )
<l≤ x/W
r1r2s
gcd(l,r1r2)=1,(µ(l))2=1
gcd(ℓ,v)=1
 1,

where we have set s = m/(r1r2l).

Lemma 4.1. Let z, y > 0. Then

(4.9) ∑

r1<y
 ∑

r2<y
gcd(r1,r2)=1
gcd(r1r2,v)=1
 µ(r1)µ(r2) ∑

min
( z/y
min(r1,r2) , z
2r1r2
 )
<l≤ z
r1r2
gcd(l,r1r2)=1,(µ(l))2=1
gcd(ℓ,v)=1
 1

equals

(4.10)
 6z
π2 v
σ(v)
 ∑

r1<y
 ∑

r2<y
gcd(r1,r2)=1
gcd(r1r2,v)=1
 µ(r1)µ(r2)
σ(r1)σ(r2)
 (1 − max ( 1
2 , r1
y , r2
y
 ))

+ O∗
 

5.08 ζ ( 3
2
 )2 y√z · ∏

p|v
 (1 + 1
√p
 ) (1 − 1
p3/2
 )2

 .

If v = 2, the error term in (4.10) can be replaced by

(4.11) O∗ (
1.27ζ ( 3
2
 )2 y√z · (1 + 1
√2
 ) (1 − 1
23/2
 )2)
 .

34 H. A. HELFGOTT

Proof. By M¨obius inversion, (4.9) equals

(4.12)
 ∑

r1<y
 ∑

r2<y
gcd(r1,r2)=1
gcd(r1r2,v)=1
 µ(r1)µ(r2) ∑

l≤ z
r1r2

l>min
( z/y
min(r1,r2) , z
2r1r2
 )

gcd(ℓ,v)=1
 ∑

d1|r1,d2|r2
d1d2|l
 µ(d1)µ(d2)

∑

d3|v
d3|l
 µ(d3) ∑

m2|l
gcd(m,r1r2v)=1
 µ(m).

We can change the order of summation of ri and di by deﬁning si = ri/di, and
we can also use the obvious fact that the number of integers in an interval (a, b]
divisible by d is (b − a)/d + O∗(1). Thus (4.12) equals
(4.13) ∑

d1,d2<y
gcd(d1,d2)=1
gcd(d1d2,v)=1
 µ(d1)µ(d2) ∑

s1<y/d1
s2<y/d2
gcd(d1s1,d2s2)=1
gcd(s1s2,v)=1
 µ(d1s1)µ(d2s2)

∑

d3|v µ(d3) ∑

m≤√ z
d2
1s1d2
2s2d3
gcd(m,d1s1d2s2v)=1
 µ(m)
d1d2d3m2 z
s1d1s2d2
 (1 − max ( 1
2 , s1d1
y , s2d2
y
 ))

plus

(4.14) O∗
 








 ∑

d1,d2<y
gcd(d1d2,v)=1
 ∑

s1<y/d1
s2<y/d2
gcd(s1s2,v)=1
 ∑

d3|v
 ∑

m≤√ z
d2
1s1d2
2s2d3
m sq-free
 1










 .

If we complete the innermost sum in (4.13) by removing the condition m ≤√z/(d2
1sd2
2s2), we obtain (reintroducing the variables ri = disi)

(4.15)
 z · ∑

r1,r2<y
gcd(r1,r2)=1
gcd(r1r2,v)=1
 µ(r1)µ(r2)
r1r2
 (1 − max ( 1
2 , r1
y , r2
y
 ))

∑

d1|r1
d2|r2
 ∑

d3|v
 ∑

m
gcd(m,r1r2v)=1
 µ(d1)µ(d2)µ(m)µ(d3)
d1d2d3m2

MINOR ARCS FOR GOLDBACH’S PROBLEM 35

times z. Now (4.15) equals

∑

r1,r2<y
gcd(r1,r2)=1
gcd(r1r2,v)=1
 µ(r1)µ(r2)z
r1r2
 (1 − max (1
2 , r1
y , r2
y
 )) ∏

p|r1r2v
 (1 − 1
p
 ) ∏

p∤r1r2
p∤v
 (1 − 1
p2
 )

= 6z
π2 v
σ(v)
 ∑

r1,r2<y
gcd(r1,r2)=1
gcd(r1r2,v)=1
 µ(r1)µ(r2)
σ(r1)σ(r2)
 (
1 − max ( 1
2 , r1
y , r2
y
 )) ,

i.e., the main term in (4.10). It remains to estimate the terms used to complete
the sum; their total is, by deﬁnition, given exactly by (4.13) with the inequality
m ≤ √z/(d2
1sd2
2s2d3) changed to m > √z/(d2
1sd2
2s2d3). This is a total of size at
most

(4.16) 1
2
 ∑

d1,d2<y
gcd(d1d2,v)=1
 ∑

s1<y/d1
s2<y/d2
gcd(s1s2,v)=1
 ∑

d3|v
 ∑

m>√ z
d2
1s1d2
2s2d3
m sq-free
 1
d1d2d3m2 z
s1d1s2d2 .

Adding this to (4.14), we obtain, as our total error term,

(4.17) ∑

d1,d2<y
gcd(d1d2,v)=1
 ∑

s1<y/d1
s2<y/d2
gcd(s1s2,v)=1
 ∑

d3|v f (√ z
d2
1s1d2
2s2d3
 ) ,

where
 f (x) := ∑

m≤x
m sq-free
 1 + 1
2
 ∑

m>x
m sq-free
 x2

m2 .

It is easy to see that f (x)/x has a local maximum exactly when x is a square-free
(positive) integer. We can hence check that

f (x) ≤ 1
2
 (2 + 2 ( ζ(2)
ζ(4) − 1.25
)) x = 1.26981 . . . x

for all x ≥ 0 by checking all integers smaller than a constant and using {m :
m sq-free} ⊂ {m : 4 ∤ m} and 1.5 · (3/4) < 1.26981 to bound f from below for x
larger than a constant. Therefore, (4.17) is at most

1.27 ∑

d1,d2<y
gcd(d1d2,v)=1
 ∑

s1<y/d1
s2<y/d2
gcd(s1s2,v)=1
 ∑

d3|v
 √ z
d2
1s1d2
2s2d3

= 1.27
√z ∏

p|v
 (1 + 1
√
p
 ) ·
 





 ∑

d<y
gcd(d,v)=1
 ∑

s<y/d
gcd(s,v)=1
 1
d
√s
 






2
 .

36 H. A. HELFGOTT

We can bound the double sum simply by

∑

d<y
gcd(d,v)=1
 ∑

s<y/d
 1
√
sd ≤ 2 ∑

d<y
 √
y/d
d ≤ 2
√y · ζ (3
2
 ) ∏

p|v
 (1 − 1
p3/2
 ) .

Alternatively, if v = 2, we bound

∑

s<y/d
gcd(s,v)=1
 1
√s = ∑

s<y/d
s odd
 1
√s ≤ 1 + 1
2
 ∫ y/d

1
 1
√s ds = √y/d

and thus ∑

d<y
gcd(d,v)=1
 ∑

s<y/d
gcd(s,v)=1
 1
√sd ≤ ∑

d<y
gcd(d,2)=1
 √y/d
d ≤ √y (1 − 1
23/2
 ) ζ ( 3
2
 ) .
 □

Applying Lemma 4.1 with y = S/s and z = x/W s, where S = x/W U , we
obtain that (4.8) equals
(4.18)
6x
π2W v
σ(v)
 ∑

s<S
gcd(s,v)=1
 1
s
 ∑

r1<S/s
 ∑

r2<S/s
gcd(r1,r2)=1
gcd(r1r2,v)=1
 µ(r1)µ(r2)
σ(r1)σ(r2)
 (1 − max (1
2 , r1
S/s , r2
S/s
 ))

+ O∗
 

5.04ζ ( 3
2
 )3 S√ x
W
 ∏

p|v
 (1 + 1
√p
 ) (1 − 1
p3/2
 )3

 ,

with 5.04 replaced by 1.27 if v = 2. The main term in (4.18) can be written as

(4.19) 6x
π2W v
σ(v)
 ∑

s≤S
gcd(s,v)=1
 1
s
 ∫ 1

1/2
 ∑

r1≤ uS
s
 ∑

r2≤ uS
s
gcd(r1,r2)=1
gcd(r1r2,v)=1
 µ(r1)µ(r2)
σ(r1)σ(r2) du.

From now on, we will focus on the cases v = 1 and v = 2 for simplicity. (Higher
values of v do not seem to be really proﬁtable in the last analysis.)

4.1.2. Explicit bounds for a sum with µ. We must estimate the expression within
parentheses in (4.19). It is not too hard to show that it tends to 0; the ﬁrst
part of the proof of Lemma 4.2 will reduce this to the fact that ∑n µ(n)/n = 0.
Obtaining good bounds is a more delicate matter. For our purposes, we will need
the expression to converge to 0 at least as fast as 1/(log)2, with a good constant
in front. For this task, the bound (2.8) on ∑n≤x µ(n)/n is enough.

Lemma 4.2. Let
 gv(x) := ∑

r1≤x
 ∑

r2≤x
gcd(r1,r2)=1
gcd(r1r2,v)=1
 µ(r1)µ(r2)
σ(r1)σ(r2) ,

MINOR ARCS FOR GOLDBACH’S PROBLEM 37

where v = 1 or v = 2. Then

|g1(x)| ≤
 



1/x if 33 ≤ x ≤ 106,
1
x (111.536 + 55.768 log x) if 106 ≤ x < 1010,
0.0044325
(log x)2 + 0.1079√x if x ≥ 1010,

|g2(x)| ≤
 



2.1/x if 33 ≤ x ≤ 106,
1
x (1634.34 + 817.168 log x) if 106 ≤ x < 1010,
0.038128
(log x)2 + 0.2046√x . if x ≥ 1010.

Tbe proof involves what may be called a version of Rankin’s trick, using Dirich-
let series and the behavior of ζ(s) near s = 1. The statements for x ≤ 106 are
proven by direct computation.
4

Proof. Clearly

(4.20)
 g(x) = ∑

r1≤x
 ∑

r2≤x
gcd(r1r2,v)=1
 

 ∑

d| gcd(r1,r2) µ(d)



 µ(r1)µ(r2)
σ(r1)σ(r2)

= ∑

d≤x
gcd(d,v)=1
 µ(d) ∑

r1≤x
 ∑

r2≤x
d| gcd(r1,r2)
gcd(r1r2,v)=1
 µ(r1)µ(r2)
σ(r1)σ(r2)

= ∑

d≤x
gcd(d,v)=1
 µ(d)
(σ(d))2 ∑

u1≤x/d
gcd(u1,dv)=1
 ∑

u2≤x/d
gcd(u2,dv)=1
 µ(u1)µ(u2)
σ(u1)σ(u2)

= ∑

d≤x
gcd(d,v)=1
 µ(d)
(σ(d))2
 





 ∑

r≤x/d
gcd(r,dv)=1
 µ(r)
σ(r)
 






2
 .

Moreover, ∑

r≤x/d
gcd(r,dv)=1
 µ(r)
σ(r) = ∑

r≤x/d
gcd(r,dv)=1
 µ(r)
r
 ∑

d′|r
 ∏

p|d′
 ( p
p + 1 − 1
)

= ∑

d′≤x/d
µ(d′)2=1
gcd(d′,dv)=1
 

∏

p|d′
 −1
p + 1
 

 ∑

r≤x/d
gcd(r,dv)=1
d′|r
 µ(r)
r

= ∑

d′≤x/d
µ(d′)2=1
gcd(d′,dv)=1
 1
d′σ(d′)
 ∑

r≤x/dd′

gcd(r,dd′v)=1
 µ(r)
r

4Using D. Platt’s implementation [Pla11] of double-precision interval arithmetic. (In fact,
one gets 2.0895071/x instead of 2.1/x.)

38 H. A. HELFGOTT

and ∑

r≤x/dd′

gcd(r,dd′v)=1
 µ(r)
r = ∑

d′′≤x/dd′

d′′|(dd′v)∞
 1
d′′ ∑

r≤x/dd′d′′
 µ(r)
r .

Hence
(4.21)

|g(x)| ≤ ∑

d≤x
gcd(d,v)=1
 (µ(d))2

(σ(d))2
 








 ∑

d′≤x/d
µ(d′)2=1
gcd(d′,dv)=1
 1
d′σ(d′)
 ∑

d′′≤x/dd′

d′′|(dd′v)∞
 1
d′′ f (x/dd
′d
′′)










2
 ,

where f (t) = ∣
∣
∣
∑r≤t µ(r)/r∣
∣
∣.
We intend to bound the function f (t) by a linear combination of terms of the
form t−δ, δ ∈ [0, 1/2). Thus it makes sense now to estimate Fv(s1, s2, x), deﬁned
to be the quantity

∑

d
gcd(d,v)=1
 (µ(d))2

(σ(d))2
 





 ∑

d′
1
gcd(d′
1,dv)=1
 µ(d′
1)2

d′
1σ(d′
1)
 ∑

d′′
1 |(dd′
1v)∞
 1
d′′
1 · (dd
′
1d
′′
1)
1−s1













 ∑

d′
2
gcd(d′
2,dv)=1
 µ(d′
2)2

d′
2σ(d′
2)
 ∑

d′′
2 |(dd′
2v)∞
 1
d′′
2 · (dd
′
2d
′′
2)
1−s2





 .

for s1, s2 ∈ [1/2, 1]. This is equal to

∑

d
gcd(d,v)=1
 µ(d)2

ds1+s2 ∏

p|d
 1

(1 + p−1)
2 (1 − p−s1) ∏p|v 1
(1−p−s1 )(1−p−s2 ) (1 − p−s2)

·
 



 ∑

d′
gcd(d′,dv)=1
 µ(d′)2

(d′)s1+1 ∏

p′|d′
 1
(1 + p′−1) (1 − p′−s1)
 





·
 



 ∑

d′
gcd(d′,dv)=1
 µ(d′)2

(d′)s2+1 ∏

p′|d′
 1
(1 + p′−1) (1 − p′−s2)
 



 ,

which in turn can easily be seen to equal

(4.22)
 ∏

p∤v
 (1 + p−s1p−s2

(1 − p−s1 + p−1)(1 − p−s2 + p−1)
 ) ∏

p|v
 1
(1 − p−s1)(1 − p−s2)

· ∏

p∤v
 (1 + p−1p−s1

(1 + p−1)(1 − p−s1)
 ) · ∏

p∤v
 (1 + p−1p−s2

(1 + p−1)(1 − p−s2)
 )

MINOR ARCS FOR GOLDBACH’S PROBLEM 39

Now, for any 0 < x ≤ y ≤ x1/2 < 1,

(1+x−y)(1−xy)(1−xy2)−(1+x)(1−y)(1−x3) = (x−y)(y2 −x)(xy−x−1)x ≤ 0,

and so
(4.23)

1 + xy
(1 + x)(1 − y) = (1 + x − y)(1 − xy)(1 − xy2)
(1 + x)(1 − y)(1 − xy)(1 − xy2) ≤ (1 − x3)
(1 − xy)(1 − xy2) .

For any x ≤ y1, y2 < 1 with y2
1 ≤ x, y2
2 ≤ x,

(4.24) 1 + y1y2
(1 − y1 + x)(1 − y2 + x) ≤ (1 − x3)2(1 − x4)
(1 − y1y2)(1 − y1y2
2)(1 − y2
1y2) .

This can be checked as follows: multiplying by the denominators and changing
variables to x, s = y1 + y2 and r = y1y2, we obtain an inequality where the left
side, quadratic on s with positive leading coeﬃcient, must be less than or equal
to the right side, which is linear on s. The left side minus the right side can be
maximal for given x, r only when s is maximal or minimal. This happens when
y1 = y2 or when either yi = √x or yi = x for at least one of i = 1, 2. In each of
these cases, we have reduced (4.24) to an inequality in two variables that can be
proven automatically5 by a quantiﬁer-elimination program; the author has used
QEPCAD [HB11] to do this.
Hence Fv(s1, s2, x) is at most

(4.25)
 ∏

p∤v
 (1 − p−3)2(1 − p−4)
(1 − p−s1−s2)(1 − p−2s1−s2)(1 − p−s1−2s2) · ∏

p|v
 1
(1 − p−s1)(1 − p−s2)

· ∏

p∤v
 1 − p−3

(1 + p−s1−1)(1 + p−2s1−1)
 ∏

p∤v
 1 − p−3

(1 + p−s2−1)(1 + p−2s2−1)

= Cv,s1,s2 · ζ(s1 + 1)ζ(s2 + 1)ζ(2s1 + 1)ζ(2s2 + 1)
ζ(3)4ζ(4)(ζ(s1 + s2)ζ(2s1 + s2)ζ(s1 + 2s2))−1 ,

where

Cv,s1,s2 =
 {
1 if v = 1,
(1−2−s1−2s2 )(1+2−s1 −1)(1+2−2s1 −1)(1+2−s2 −1)(1+2−2s2 −1)
(1−2−s1 +s2 )−1(1−2−2s1 −s2 )−1(1−2−s1 )(1−2−s2 )(1−2−3)4(1−2−4) if v = 2.

For 1 ≤ t ≤ x, (2.8) and (2.11) imply

(4.26) f (t) ≤
 



√ 2
t if x ≤ 1010
√ 2
t + 0.03
log x ( x
t ) log log 1010

log x−log 1010 if x > 1010,

where we are using the fact that log x is convex-down. Note that, again by
convexity,

log log x − log log 1010

log x − log 1010 < (log t)
′|t=log 1010 = 1
log 1010 = 0.0434294 . . .

Obviously, √
2/t in (4.26) can be replaced by (2/t)1/2−ǫ for any ǫ ≥ 0.

5In practice, the case yi = √x leads to a polynomial of high degree, and quantiﬁer elimination
increases sharply in complexity as the degree increases; a stronger inequality of lower degree
(with (1 − 3x3) instead of (1 − x3)2(1 − x4)) was given to QEPCAD to prove in this case.

40 H. A. HELFGOTT

By (4.21) and (4.26),

|gv(x)| ≤ ( 2
x
 )1−2ǫ Fv(1/2 + ǫ, 1/2 + ǫ, x)

for x ≤ 1010. We set ǫ = 1/ log x and obtain from (4.25) that

(4.27) Fv(1/2 + ǫ, 1/2 + ǫ, x) ≤ Cv, 1
2 +ǫ, 1
2 +ǫ ζ(1 + 2ǫ)ζ(3/2)4ζ(2)2

ζ(3)4ζ(4)

≤ 55.768 · Cv, 1
2 +ǫ, 1
2 +ǫ · (1 + log x
2
 ) ,

where we use the easy bound ζ(s) < 1 + 1/(s − 1) obtained by

∑ ns < 1 + ∫ ∞

1 tsdt.

(For sharper bounds, see [BR02].) Now

C2, 1
2 +ǫ, 1
2 +ǫ ≤ (1 − 2−3/2−ǫ)2(1 + 2−3/2)2(1 + 2−2)2(1 − 2−1−2ǫ)
(1 − 2−1/2)2(1 − 2−3)4(1 − 2−4) ≤ 14.652983,

whereas C1, 1
2 +ǫ, 1
2 +ǫ = 1. (We are assuming x ≥ 106, and so ǫ ≤ 1/(log 106).)
Hence
 |gv(x)| ≤
 { 1
x (111.536 + 55.768 log x) if v = 1,
1
x (1634.34 + 817.168 log x) if v = 2.

for 106 ≤ x < 1010.
For general x, we must use the second bound in (4.26). Deﬁne c = 1/(log 1010).
We see that, if x > 1010,

|gv(x)| ≤ 0.032

(log x)2 F1(1 − c, 1 − c) · Cv,1−c,1−c

+ 2 · √
2
√x 0.03
log xF (1 − c, 1/2) · Cv,1−c,1/2

+ 1
x (111.536 + 55.768 log x) · Cv, 1
2 +ǫ, 1
2 +ǫ.

For v = 1, this gives

|g1(x)| ≤ 0.0044325
(log x)2 + 2.1626
√x log x + 1
x (111.536 + 55.768 log x)

≤ 0.0044325
(log x)2 + 0.1079
√x ;

for v = 2, we obtain

|g2(x)| ≤ 0.038128
(log x)2 + 25.607
√
x log x + 1
x (1634.34 + 817.168 log x)

≤ 0.038128
(log x)2 + 0.2046
√x .
 □

MINOR ARCS FOR GOLDBACH’S PROBLEM 41

4.1.3. Estimating the triple sum. We will now be able to bound the triple sum
in (4.19), viz.,

(4.28) ∑

s≤S
gcd(s,v)=1
 1
s
 ∫ 1

1/2 gv(uS/s)du,

where gv is as in Lemma 4.2.
As we will soon see, Lemma 4.2 that (4.28) is bounded by a constant (essentially
because the integral ∫ 1/2
0 1/t(log t)2 converges). We must give as good a constant
as we can, since it will aﬀect the largest term in the ﬁnal result.
Clearly gv(R) = gv(⌊R⌋). The contribution of each gv(m), 1 ≤ m ≤ S, to
(4.28) is exactly gv(m) times
(4.29)
∑

S
m+1 <s≤ S
m
 1
s

gcd(s,v)=1
 ∫ 1

ms/S du + ∑

S
2m <s≤ S
m+1
 1
s

gcd(s,v)=1
 ∫ (m+1)s/S

ms/S du + ∑

S
2(m+1) <s≤ S
2m
 1
s

gcd(s,v)=1
 ∫ (m+1)s/S

1/2 du

= ∑

S
m+1 <s≤ S
m
gcd(s,v)=1
 ( 1
s − m
S
 ) + ∑

S
2m <s≤ S
m+1
gcd(s,v)=1
 1
S + ∑

S
2(m+1) <s≤ S
2m
gcd(s,v)=1
 ( m + 1
S − 1
2s
 ) .

Write f (t) = 1/S for S/2m < t ≤ S/(m + 1), f (t) = 0 for t > S/m or t <
S/2(m+1), f (t) = 1/t−m/S for S/(m+1) < t ≤ S/m and f (t) = (m+1)/S−1/2t
for S/2(m + 1) < t ≤ S/2m; then (4.29) equals ∑n:gcd(n,v)=1 f (n). By Euler-
Maclaurin (second order),
(4.30)
∑

n f (n) = ∫ ∞

−∞ f (x) − 1
2 B2({x})f ′′(x)dx = ∫ ∞

−∞ f (x) + O∗ ( 1
12 |f ′′(x)|
) dx

= ∫ ∞

−∞ f (x)dx + 1
6 · O∗ (∣
∣
∣
∣f ′ ( 3
2m
 )∣
∣
∣
∣ + ∣
∣
∣
∣f ′ ( s
m + 1
 )∣
∣
∣
∣
)

= 1
2 log (1 + 1
m
 ) + 1
6 · O∗ (( 2m
s
 )2 + ( m + 1
s
 )2)
 .

Similarly,

∑

n odd f (n) = ∫ ∞

−∞ f (2x + 1) − 1
2 B2({x}) d2f (2x + 1)
dx2 dx

= 1
2
 ∫ ∞

−∞ f (x)dx − 2 ∫ ∞

−∞
 1
2 B2
 ({ x − 1
2
 }) f ′′(x)dx

= 1
2
 ∫ ∞

−∞ f (x)dx + 1
6
 ∫ ∞

−∞ O∗ (|f ′′(x)|
) dx

= 1
4 log (1 + 1
m
 ) + 1
3 · O∗ (( 2m
s
 )2 + ( m + 1
s
 )2)
 .

We use these expressions for m ≤ C0, where C0 ≥ 33 is a constant to be
computed later; they will give us the main term. For m > C0, we use the bounds
on |g(m)| that Lemma 4.2 gives us.

42 H. A. HELFGOTT

(Starting now and for the rest of the paper, we will focus on the cases v = 1,
v = 2 when giving explicit computational estimates. All of our procedures would
allow higher values of v as well, but, as will become clear much later, the gains
from higher values of v are oﬀset by losses and complications elsewhere.)
Let us estimate (4.28). Let

cv,0 =
 {
1/6 if v = 1,
1/3 if v = 2, cv,1 =
 {
1 if v = 1,
2.5 if v = 2,

cv,2 =
 {
55.768 . . . if v = 1,
817.168 . . . if v = 2, cv,3 =
 {
111.536 . . . if v = 1,
1634.34 . . . if v = 2,

cv,4 =
 {
0.0044325 . . . if v = 1,
0.038128 . . . if v = 2, cv,5 =
 {
0.1079 . . . if v = 1,
0.2046 . . . if v = 2.

Then (4.28) equals

∑

m≤C0gv(m) · ( φ(v)
2v log (1 + 1
m
 ) + O∗ (cv,0 5m2 + 2m + 1
S2
 ))

+ ∑

S/106≤s<S/C0
 1
s
 ∫ 1

1/2 O∗ ( cv,1
uS/s
 ) du

+ ∑

S/1010≤s<S/106
 1
s
 ∫ 1

1/2 O∗ ( cv,2 log(uS/s) + cv,3
uS/s
 ) du

+ ∑

s<S/1010
 1
s
 ∫ 1

1/2 O∗ ( cv,4
(log uS/s)2 + cv,5√uS/s
 )
 du,

which is
∑

m≤C0gv(m) · φ(v)
2v log (1 + 1
m
 ) + ∑

m≤C0 |g(m)| · O∗ (cv,0 5m2 + 2m + 1
S2
 )

+ O∗ (
cv,1 log 2
C0 + log 2
106 (cv,3 + cv,2(1 + log 10
6)
) + 2 − √
2
1010/2 cv,5
)

+ O∗
 

 ∑

s<S/1010
 cv,4/2
s(log S/2s)2
 



for S ≥ (C0 + 1). Note that ∑s<S/1010 1
s(log S/2s)2 = ∫ 2/1010

0 1
t(log t)2 dt.
Now

cv,4
2
 ∫ 2/1010

0
 1
t(log t)2 dt = cv,4/2
log(1010/2) =
 {
0.00009923 . . . if v = 1
0.000853636 . . . if v = 2.

and
 log 2
106 (
cv,3 + cv,2(1 + log 10
6)
) + 2 − √2
105 cv,5 =
 {
0.0006506 . . . if v = 1
0.009525 . . . if v = 2.

MINOR ARCS FOR GOLDBACH’S PROBLEM 43

For C0 = 10000,

φ(v)
v 1
2
 ∑

m≤C0 gv(m) · log (1 + 1
m
 ) =
 {
0.362482 . . . if v = 1,
0.360576 . . . if v = 2,

cv,0 ∑

m≤C0 |gv(m)|(5m2 + 2m + 1) ≤
 {
6204066.5 . . . if v = 1,
15911340.1 . . . if v = 2,

and
 cv,1 · (log 2)/C0 =
 {
0.00006931 . . . if v = 1,
0.00017328 . . . if v = 2.

Thus, for S ≥ 100000,

(4.31) ∑

s≤S
gcd(s,v)=1
 1
s
 ∫ 1

1/2 gv(uS/s)du ≤
 {
0.36393 if v = 1,
0.37273 if v = 2.

For S < 100000, we proceed as above, but using the exact expression (4.29)
instead of (4.30). Note (4.29) is of the form fs,m,1(S) + fs,m,2(S)/S, where both
fs,m,1(S) and fs,m,2(S) depend only on ⌊S⌋ (and on s and m). Summing over
m ≤ S, we obtain a bound of the form

∑

s≤S
gcd(s,v)=1
 1
s
 ∫ 1

1/2 gv(uS/s)du ≤ Gv(S)

with Gv(S) = Kv,1(|S|) + Kv,2(|S|)/S,

where Kv,1(n) and Kv,2(n) can be computed explicitly for each integer n. (For
example, Gv(S) = 1 − 1/S for 1 ≤ S < 2 and Gv(S) = 0 for S < 1.)
It is easy to check numerically that this implies that (4.31) holds not just
for S ≥ 100000 but also for 40 ≤ S < 100000 (if v = 1) or 16 ≤ S < 100000 (if
v = 2). Using the fact that Gv(S) is non-negative, we can compare ∫ T
1 Gv(S)dS/S
with log(T + 1/N ) for each T ∈ [2, 40] ∩ 1
N Z (N a large integer) to show, again
numerically, that

(4.32) ∫ T

1 Gv(S) dS
S ≤
 {
0.3698 log T if v = 1,
0.37273 log T if v = 2.

(We use N = 100000 for v = 1; already N = 10 gives us the answer above for
v = 2. Indeed, computations suggest the better bound 0.358 instead of 0.37273;
we are committed to using 0.37273 because of (4.31).)
Multiplying by 6v/π2σ(v), we conclude that

(4.33) S1(U, W ) = x
W · H1 ( x
W U
 ) + O∗ (
5.08ζ(3/2)
3 x3/2

W 3/2U
 )

if v = 1,

(4.34) S1(U, W ) = x
W · H2 ( x
W U
 ) + O∗ (
1.27ζ(3/2)
3 x3/2

W 3/2U
 )

44 H. A. HELFGOTT

if v = 2, where
(4.35)

H1(S) =
 { 6
π2 G1(S) if 1 ≤ S < 40,
0.22125 if S ≥ 40, H2(s) =
 { 4
π2 G2(S) if 1 ≤ S < 16,
0.15107 if S ≥ 16.

Hence (by (4.32))

(4.36) ∫ T

1 Hv(S) dS
S ≤
 {0.22482 log T if v = 1,
0.15107 log T if v = 2;

moreover, H1(S) ≤ 3/π2, H2(S) ≤ 2/π2 for all S.

* * *

Note. There is another way to obtain cancellation on µ, applicable when
(x/W ) > U q (as is unfortunately never the case in our main application). For
this alternative to be taken, one must either apply Cauchy-Schwarz on n rather
than m (resulting in exponential sums over m) or lump together all m near each
other and in the same congruence class modulo q before applying Cauchy-Schwarz
on m (one can indeed do this if δ is small). We could then write
∑

m∼W
m≡r mod q
 ∑

d|m
d>U
 µ(d) = − ∑

m∼W
m≡r mod q
 ∑

d|m
d≤U
 µ(d) = − ∑

d≤U µ(d)(W/qd + O(1))

and obtain cancellation on d. If U q ≥ (x/W ), however, the error term dominates.

4.2. The sum S2: the large sieve, primes and tails. We must now bound

(4.37) S2(U ′, W ′, W ) = ∑

U ′<m≤ x
W
gcd(m,v)=1
 ∣
∣
∣
∣
∣
∣
 ∑

W ′<p≤W(log p)e(αmp)

∣
∣
∣
∣
∣
∣
2
 .

for U ′ = max(U, x/2W ), W ′ = max(V, W/2). (The condition gcd(p, v) = 1 will
be fulﬁlled automatically by the assumption V > v.)
From a modern perspective, this is clearly a case for a large sieve. It is also
clear that we ought to try to apply a large sieve for sequences of prime support.
What is subtler here is how to do things well for very large q (i.e., x/q small).
This is in some sense a dual problem to that of q small, but it poses additional
complications; for example, it is not obvious how to take advantage of prime
support for very large q.
As in type I, we avoid this entire issue by forbidding q large and then taking
advantage of the error term δ/x in the approximation α = a
q + δ
x . This is one
of the main innovations here. Note this alternative method will allow us to take
advantage of prime support.
A key situation to study is that of frequencies αi clustering around given
rationals a/q while nevertheless keeping at a certain small distance from each
other.

Lemma 4.3. Let q ≥ 1. Let α1, α2, . . . , αk ∈ R/Z be of the form αi = ai/q + υi,
0 ≤ ai < q, where the elements υi ∈ R all lie in an interval of length υ > 0, and
where ai = aj implies |υi − υj| > ν > 0. Assume ν + υ ≤ 1/q. Then, for any

MINOR ARCS FOR GOLDBACH’S PROBLEM 45

W, W ′ ≥ 1, W ′ ≥ W/2,

(4.38)
 k∑

i=1
 ∣
∣
∣
∣
∣
∣
 ∑

W ′<p≤W (log p)e(αip)

∣
∣
∣
∣
∣
∣

2
 ≤ min (1, 2q
φ(q) 1
log ((q(ν + υ))−1)
 )

· (W − W ′ + ν−1) ∑

W ′<p≤W (log p)
2.

Proof. For any distinct i, j, the angles αi, αj are separated by at least ν (if
ai = aj) or at least 1/q − |υi − υj| ≥ 1/q − υ ≥ ν (if ai ̸= aj). Hence we can
apply the large sieve (in the optimal N + δ−1 − 1 form due to Selberg [Sel91] and
Montgomery-Vaughan [MV74]) and obtain the bound in (4.38) with 1 instead of
min(1, . . . ) immediately.
We can also apply Montgomery’s inequality ([Mon68], [Hux72]; see the expo-
sitions in [Mon71, pp. 27–29] and [IK04, §7.4]). This gives us that the left side
of (4.38) is at most
(4.39)






 ∑

r≤R
gcd(r,q)=1
 (µ(r))2

φ(r)
 





−1
 ∑

r≤R
gcd(r,q)=1
 ∑

a′ mod r
gcd(a′,r)=1
 k∑

i=1
 ∣
∣
∣
∣
∣
∣
 ∑

W ′<p≤W(log p)e((αi + a′/r)p)

∣
∣
∣
∣
∣
∣
2

If we add all possible fractions of the form a′/r, r ≤ R, gcd(r, q) = 1, to the
fractions ai/q, we obtain fractions that are separated by at least 1/qR2. If ν +υ ≥
1/qR2, then the resulting angles αi + a′/r are still separated by at least ν. Thus
we can apply the large sieve to (4.39); setting R = 1/
√(ν + υ)q, we see that we
gain a factor of
(4.40)
∑

r≤R
gcd(r,q)=1
 (µ(r))2

φ(r) ≥ φ(q)
q
 ∑

r≤R
 (µ(r))2

φ(r) ≥ φ(q)
q
 ∑

d≤R
 1
d ≥ φ(q)
2q log (
(q(ν + υ))
−1) ,

since ∑d≤R 1/d ≥ log(R) for all R ≥ 1 (integer or not). □

Let us ﬁrst give a bound on sums of the type of S2(U, V, W ) using prime
support but not the error terms (or Lemma 4.3).

Lemma 4.4. Let W ≥ 1, W ′ ≥ W/2. Let α = a/q + O∗(1/qQ), q ≤ Q. Then

(4.41)
 ∑

A0<m≤A1
 ∣
∣
∣
∣
∣
∣
 ∑

W ′<p≤W (log p)e(αmp)

∣
∣
∣
∣
∣
∣
2

≤ ⌈ A1 − A0
min(q, ⌈Q/2⌉)
 ⌉ · (W − W ′ + 2q) ∑

W ′<p≤W (log p)
2.

If q < W/2 and Q ≥ 3.5W , the following bound also holds:

(4.42)
 ∑

A0<m≤A1
 ∣
∣
∣
∣
∣
∣
 ∑

W ′<p≤W (log p)e(αmp)

∣
∣
∣
∣
∣
∣
2

≤ ⌈ A1 − A0
q
 ⌉ · q
φ(q) W
log(W/2q) · ∑

W ′<p≤W (log p)
2.

46 H. A. HELFGOTT

If A1 − A0 ≤ ̺q and q ≤ ρQ, ̺, ρ ∈ [0, 1], the following bound also holds:

(4.43)
 ∑

A0<m≤A1
 ∣
∣
∣
∣
∣
∣
 ∑

W ′<p≤W (log p)e(αmp)

∣
∣
∣
∣
∣
∣
2

≤ (W − W ′ + q/(1 − ̺ρ)) ∑

W ′<p≤W (log p)
2.

The inequality (4.42) can be stronger than (4.42) only when q < W/7.2638 . . .
(if q is odd) or q < W/92.514 . . . (if q is even).

Proof. Let k = min(q, ⌈Q/2⌉) ≥ ⌈q/2⌉. We split (A0, A1] into ⌈(A1 − A0)/k⌉
blocks of at most k consecutive integers m0 + 1, m0 + 2, . . . . For m, m′ in such a
block, αm and αm′ are separated by a distance of at least

|{(a/q)(m − m′)}| − O∗(k/qQ) = 1/q − O∗(1/2q) ≥ 1/2q.

By the large sieve

(4.44)
 q∑

a=1
 ∣
∣
∣
∣
∣
∣
 ∑

W ′<p≤W (log p)e(α(m0 + a)p)

∣
∣
∣
∣
∣
∣
2
 ≤ ((W − W ′) + 2q) ∑

W ′<p≤W (log p)
2.

We obtain (4.41) by summing over all ⌈(A1 − A0)/k⌉ blocks.
If A1 − A0 ≤ |̺q| and q ≤ ρQ, ̺, ρ ∈ [0, 1], we obtain (4.43) simply by applying
the large sieve without splitting the interval A0 < m ≤ A1.
Let us now prove (4.42). We will use Montgomery’s inequality, followed by
Montgomery and Vaughan’s large sieve with weights. An angle a/q + a′
1/r1 is
separated from other angles a′/q + a′
2/r2 (r1, r2 ≤ R, gcd(ai, ri) = 1) by at least
1/qr1R, rather than just 1/qR2. We will choose R so that qR2 < Q; this implies
1/Q < 1/qR2 ≤ 1/qr1R.
By Montgomery’s inequality [IK04, Lemma 7.15], applied (for each 1 ≤ a ≤ q)
to S(α) = ∑n ane(αn) with an = log(n)e(α(m0 + a)n) if n is prime and an = 0
otherwise,

(4.45)
 1
φ(r)
 ∣
∣
∣
∣
∣
∣
 ∑

W ′<p≤W (log p)e(α(m0 + a)p)

∣
∣
∣
∣
∣
∣
2

≤ ∑

a′ mod r
gcd(a′,r)=1
 ∣
∣
∣
∣
∣
∣
 ∑

W ′<p≤W(log p)e ((α (m0 + a) + a′

r
 ) p)∣
∣
∣
∣
∣
∣

2
 .

for each square-free r ≤ W ′. We multiply both sides of (4.45) by (W/2 +
(3/2)(1/qrR − 1/Q)−1)−1 and sum over all a = 0, 1, . . . , q − 1 and all square-
free r ≤ R coprime to q; we will later make sure that R ≤ W ′. We obtain
that

(4.46)
 ∑

r≤R
gcd(r,q)=1
 ( W
2 + 3
2
 ( 1
qrR − 1
Q
 )−1)−1 µ(r)2

φ(r)

·
 q∑

a=1
 ∣
∣
∣
∣
∣
∣
 ∑

W ′<p≤W (log p)e(α(m0 + a)p)

∣
∣
∣
∣
∣
∣

2

MINOR ARCS FOR GOLDBACH’S PROBLEM 47

is at most

(4.47)
 ∑

r≤R
gcd(r,q)=1
r sq-free
 ( W
2 + 3
2
 ( 1
qrR − 1
Q
 )−1)−1

q∑

a=1
 ∑

a′ mod r
gcd(a′,r)=1
 ∣
∣
∣
∣
∣
∣
 ∑

W ′<p≤W (log p)e ((α (m0 + a) + a′

r
 ) p)∣
∣
∣
∣
∣
∣

2

We now apply the large sieve with weights [MV73, (1.6)], recalling that each
angle α(m0 + a) + a′/r is separated from the others by at least 1/qrR − 1/Q; we
obtain that (4.47) is at most ∑W ′<p≤W (log p)2. It remains to estimate the sum
in the ﬁrst line of (4.46). (We are following here a procedure analogous to that
used in [MV73] to prove the Brun-Titchmarsh theorem.)
Assume ﬁrst that q ≤ W/13.5. Set

(4.48) R = (σ W
q
 )1/2 ,

where σ = 1/2e2·0.25068 = 0.30285 . . . . It is clear that qR2 < Q, q < W ′ and
R ≥ 2. Moreover, for r ≤ R,

1
Q ≤ 1
3.5W ≤ σ
3.5 1
σW = σ
3.5 1
qR2 ≤ σ/3.5
qrR .

Hence

W
2 + 3
2
 ( 1
qrR − 1
Q
 )−1 ≤ W
2 + 3
2 qrR
1 − σ/3.5 = W
2 + 3r
2 (1 − σ
3.5 ) R · 2σ W
2

= W
2
 (1 + 3σ
1 − σ/3.5 rW
R
 ) < W
2
 (1 + rW
R
 )

and so

∑

r≤R
gcd(r,q)=1
 ( W
2 + 3
2
 ( 1
qrR − 1
Q
 )−1)−1 µ(r)2

φ(r)

≥ 2
W
 ∑

r≤R
gcd(r,q)=1

(1 + rR−1)
−1 µ(r)2

φ(r) ≥ 2
W φ(q)
q
 ∑

r≤R(1 + rR−1)
−1 µ(r)2

φ(r) .

For R ≥ 2, ∑

r≤R(1 + rR−1)
−1 µ(r)2

φ(r) > log R + 0.25068;

this is true for R ≥ 100 by [MV73, Lemma 8] and easily veriﬁable numerically
for 2 ≤ R < 100. (It suﬃces to verify this for R integer with r < R instead of
r ≤ R, as that is the worst case.)
Now
 log R = 1
2
 (log W
2q + log 2σ) = 1
2 log W
2q − 0.25068.

48 H. A. HELFGOTT

Hence ∑

r≤R
(1 + rR−1)
−1 µ(r)2

φ(r) > 1
2 log W
2q

and the statement follows.
Now consider the case q > W/13.5. If q is even, then, in this range, inequality
(4.41) is always better than (4.42), and so we are done. Assume, then, that
W/13.5 < q ≤ W/2 and q is odd. We set R = 2; clearly qR2 < W ≤ Q and
q < W/2 ≤ W ′, and so this choice of R is valid. It remains to check that
1

W
2 + 3
2 ( 1
2q − 1
Q )−1 + 1

W
2 + 3
2 ( 1
4q − 1
Q )−1 ≥ 1
W log W
2q .

This follows because 1

1
2 + 3
2 ( t
2 − 1
3.5 )−1 + 1

1
2 + 3
2 ( t
4 − 1
3.5 )−1 ≥ log t
2

for all 2 ≤ t ≤ 13.5. □

We need a version of Lemma 4.4 with m restricted to the odd numbers.

Lemma 4.5. Let W ≥ 1, W ′ ≥ W/2. Let 2α = a/q + O∗(1/qQ), q ≤ Q. Then

(4.49)
 ∑

A0<m≤A1
m odd
 ∣
∣
∣
∣
∣
∣
 ∑

W ′<p≤W (log p)e(αmp)

∣
∣
∣
∣
∣
∣
2

≤ ⌈ A1 − A0
min(2q, Q)
 ⌉ · (W − W ′ + 2q) ∑

W ′<p≤W (log p)
2.

If q < W/2 and Q ≥ 3.5W , the following bound also holds:

(4.50)
 ∑

A0<m≤A1
m odd
 ∣
∣
∣
∣
∣
∣
 ∑

W ′<p≤W (log p)e(αmp)

∣
∣
∣
∣
∣
∣
2

≤ ⌈ A1 − A0
2q
 ⌉ · q
φ(q) W
log(W/2q) · ∑

W ′<p≤W (log p)
2.

If A1 − A0 ≤ 2̺q and q ≤ ρQ, ̺, ρ ∈ [0, 1], the following bound also holds:

(4.51)
 ∑

A0<m≤A1
 ∣
∣
∣
∣
∣
∣
 ∑

W ′<p≤W (log p)e(αmp)

∣
∣
∣
∣
∣
∣
2

≤ (W − W ′ + q/(1 − ̺ρ)) ∑

W ′<p≤W (log p)
2.

Proof. We follow the proof of Lemma 4.4, noting the diﬀerences. Let k =
min(q, ⌈Q/2⌉) ≥ ⌈q/2⌉, just as before. We split (A0, A1] into ⌈(A1 − A0)/k⌉
blocks of at most 2k consecutive integers; any such block contains at most k odd
numbers. For odd m, m′ in such a block, αm and αm′ are separated by a distance
of
 |{α(m − m′)}| = ∣
∣
∣
∣

{
2α m − m′

2
 }∣
∣
∣
∣ = |{(a/q)k}| − O∗(k/qQ) ≥ 1/2q.

MINOR ARCS FOR GOLDBACH’S PROBLEM 49

We obtain (4.49) and (4.51) just as we obtained (4.41) and (4.43) before. To
obtain (4.50), proceed again as before, noting that the angles we are working
with can be labelled as α(m0 + 2a), 0 ≤ a < q. □

The idea now (for large δ) is that, if δ is not negligible, then, as m increases,
αm loops around the circle R/Z roughly repeats itself every q steps – but with
a slight displacement. This displacement gives rise to a conﬁguration to which
Lemma 4.3 is applicable.

Proposition 4.6. Let x ≥ W ≥ 1, W ′ ≥ W/2, U ′ ≥ x/2W . Let Q ≥ 3.5W . Let
2α = a/q + δ/x, gcd(a, q) = 1, |δ/x| ≤ 1/qQ, q ≤ Q. Let S2(U ′, W ′, W ) be as in
(4.37) with v = 2.
For q ≤ ρQ, where ρ ∈ [0, 1],
(4.52)

S2(U ′, W ′, W ) ≤ (
max(1, 2ρ) ( x
8q + x
2W
 ) + W
2 + 2q) · ∑

W ′<p≤W (log p)
2

If q < W/2,
(4.53)

S2(U ′, W ′, W ) ≤ ( x
4φ(q) 1
log(W/2q) + q
φ(q) W
log(W/2q)
 ) · ∑

W ′<p≤W (log p)
2.

If W > x/4q, the following bound also holds:

(4.54) S2(U ′, W ′, W ) ≤ ( W
2 + q
1 − x/4W q
 ) ∑

W ′<p≤W(log p)
2.

If δ ̸= 0 and x/4W + q ≤ x/|δ|q,
(4.55)

S2(U ′, W ′, W ) ≤ min
 

1, 2q/φ(q)

log ( x
|δq| (q + x
4W )−1)
 

 · ( x
|δq| + W
2
 ) ∑

W ′<p≤W (log p)
2.

Lastly, if δ ̸= 0 and q ≤ ρQ, where ρ ∈ [0, 1),
(4.56)

S2(U ′, W ′, W ) ≤ ( x
|δq| + W
2 + x
8(1 − ρ)Q + x
4(1 − ρ)W
 ) ∑

W ′<p≤W(log p)
2.

The trivial bound would be in the order of

S2(U ′, W ′, W ) = (x/2 log x) ∑

W ′<p≤W(log p)
2.

In practice, (4.54) gets applied when W ≥ x/q.

Proof. Let us ﬁrst prove statements (4.53) and (4.52), which do not involve δ.
Assume ﬁrst q ≤ W/2. Then, by (4.50) with A0 = U ′, A1 = x/W ,

S2(U ′, W ′, W ) ≤ ( x/W − U ′

2q + 1
) q
φ(q) W
log(W/2q)
 ∑

W ′<p≤W (log p)
2.

Clearly (x/W − U ′)W ≤ (x/2W ) · W = x/2. Thus (4.53) holds.
Assume now that q ≤ ρQ. Apply (4.49) with A0 = U ′, A1 = x/W . Then

S2(U ′, W ′, W ) ≤ ( x/W − U ′

q · min(2, ρ−1) + 1
) (W − W ′ + 2q) ∑

W ′<p≤W(log p)
2.

50 H. A. HELFGOTT

Now ( x/W − U ′

q · min(2, ρ−1) + 1
) · (W − W ′ + 2q)

≤ ( x
W − U ′) W − W ′

q min(2, ρ−1) + max(1, 2ρ) ( x
W − U ′) + W/2 + 2q

≤ x/4
q min(2, ρ−1) + max(1, 2ρ) x
2W + W/2 + 2q.

This implies (4.52).
If W > x/4q, apply (4.43) with ̺ = x/4W q, ρ = 1. This yields (4.54).
Assume now that δ ̸= 0 and x/4W + q ≤ x/|δq|. Let Q′ = x/|δq|. For any m1,
m2 with x/2W < m1, m2 ≤ x/W , we have |m1 − m2| ≤ x/2W ≤ 2(Q′ − q), and
so

(4.57) ∣
∣
∣
∣ m1 − m2
2 · δ/x + qδ/x∣
∣
∣
∣ ≤ Q′|δ|/x = 1
q .

The conditions of Lemma 4.3 are thus fulﬁlled with υ = (x/4W ) · |δ|/x and
ν = |δq|/x. We obtain that S2(U ′, W ′, W ) is at most

min (1, 2q
φ(q) 1
log ((q(ν + υ))−1)
 ) (
W − W ′ + ν−1) ∑

W ′<p≤W (log p)
2.

Here W − W ′ + ν−1 = W − W ′ + x/|qδ| ≤ W/2 + x/|qδ| and

(q(ν + υ))
−1 = (q |δ|
x
 )−1 (q + x
4W
 )−1 .

Lastly, assume δ ̸= 0 and q ≤ ρQ. We let Q′ = x/|δq| ≥ Q again, and we split
the range U ′ < m ≤ x/W into intervals of length 2(Q′ − q), so that (4.57) still
holds within each interval. We apply Lemma 4.3 with υ = (Q′ − q) · |δ|/x and
ν = |δq|/x. We obtain that S2(U ′, W ′, W ) is at most
(1 + x/W − U
2(Q′ − q)
 ) (W − W ′ + ν−1) ∑

W ′<p≤W (log p)
2.

Here W − W ′ + ν−1 ≤ W/2 + x/q|δ| as before. Moreover,
( W
2 + x
q|δ|
 ) (1 + x/W − U
2(Q′ − q)
 ) ≤ ( W
2 + Q′) (
1 + x/2W
2(1 − ρ)Q′
 )

≤ W
2 + Q′ + x
8(1 − ρ)Q′ + x
4W (1 − ρ)

≤ x
|δq| + W
2 + x
8(1 − ρ)Q + x
4(1 − ρ)W .

Hence (4.56) holds. □

5. Totals

Let x be given. We will choose U , V , W later; assume from the start that
2 · 106 ≤ V < x/4 and U V ≤ x. Starting in section 5.2, we will also assume that
x ≥ x0 = 1025.
Let α ∈ R/Z be given. We choose an approximation 2α = a/q + δ/x,
gcd(a, q) = 1, q ≤ Q, |δ/x| ≤ 1/qQ. We assume Q ≥ max(16, 2
√x) and

MINOR ARCS FOR GOLDBACH’S PROBLEM 51

Q ≥ max(2U, x/U ). Let SI,1, SI,2, SII , S0 be as in (2.21), with the smooth-
ing function η = η2 as in (1.4).
The term S0 is 0 because V < x/4 and η2 is supported on [−1/4, 1]. We set
v = 2.

5.1. Contributions of diﬀerent types.

5.1.1. Type I terms: SI,1. The term SI,1 can be handled directly by Lemma
3.6, with ρ0 = 4 and D = U . (Condition (3.38) is valid thanks to (2.6).) Since
U ≤ Q/2, the contribution of SI,1 gets bounded by (3.40) and (3.41): the absolute
value of SI,1 is at most
(5.1)

x
q min (1, c0/δ2

(2π)2
 )
 ∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
 ∑

m≤ U
q
gcd(m,q)=1
 µ(m)
m log x
mq
 ∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
 + x
q | ̂log ·η(−δ)|
 ∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
 ∑

m≤ U
q
gcd(m,q)=1
 µ(m)
m
 ∣
∣
∣
∣
∣
∣
∣
∣
∣
∣

+ 2
√c0c1
π
 (U log ex
U + √3q log q
c2 + q
2 log q
c2 log+ 2U
q
 ) + 3c1
2 x
q log q
c2 log+ U
c2x
q

+ 3c1
2
 √ 2x
c2 log 2x
c2 + ( c0
2 − 2c0
π2
 ) ( U 2

4qx log e1/2x
U + 1
e
 )

+ 2|η′|1
π q max (1, log c0e3q2

4π|η′|1x
 ) log x,

where c0 = 31.521 (by Lemma A.5), c1 = 1.0000028 > 1 + (8 log 2)/V ≥ 1 +
(8 log 2)/(x/U ), c2 = 6π/5
√c0 = 0.67147 . . . . By (2.1), (A.17) and Lemma A.6,

| ̂log ·η(−δ)| ≤ min (2 − log 4, 24 log 2
π2δ2
 ) .

By (2.7), (2.9) and (2.10), the ﬁrst line of (5.1) is at most

x
q min (1, c′
0
δ2
 ) (
min
 ( 4
5 q/φ(q)
log+ U
q2 , 1

)
 log x
U + 1.00303 q
φ(q)
 )

+ x
q min (2 − log 4, c′′
0
δ2
 ) min
 ( 4
5 q/φ(q)
log+ U
q2 , 1

)
 ,

where c′
0 = 0.798437 > c0/(2π)2, c′′
0 = 1.685532. Clearly c′′
0/c0 > 1 > 2 − log 4.
Taking derivatives, we see that t ↦→ (t/2) log(t/c2) log+ 2U/t takes its max-
imum (for t ∈ [1, 2U ]) when log(t/c2) log+ 2U/t = log t/c2 − log+ 2U/t; since
t → log t/c2 − log+ 2U/t is increasing on [1, 2U ], we conclude that

q
2 log q
c2 log+ 2U
q ≤ U log 2U
c2 .

Similarly, t ↦→ t log(x/t) log+(U/t) takes its maximum at a point t ∈ [0, U for
which log(x/t) log+(U/t) = log(x/t) + log+(U/t), and so

x
q log q
c2 log+ U
c2x
q ≤ U
c2 (log x + log U ).

52 H. A. HELFGOTT

We conclude that
(5.2)

|SI,1| ≤ x
q min (1, c′
0
δ2
 ) (
min
 ( 4q/φ(q)
5 log+ U
q2 , 1

) (
log x
U + c3,I ) + c4,I q
φ(q)
 )

+ (
c7,I log q
c2 + c8,I log x max (1, log c11,I q2

x
 )) q + c10,I U 2

4qx log e1/2x
U

+ (
c5,I log 2U
c2 + c6,I log xU ) U + c9,I √x log 2x
c2 + c10,I
e ,

where c2 and c′
0 are as above, c3,I = 2.11104 > c′′
0/c′
0, c4,I = 1.00303, c5,I =
3.57422 > 2
√c0c1/π, c6,I = 2.23389 > 3c1/2c2, c7,I = 6.19072 > 2
√3c0c1/π,
c8,I = 3.53017 > 2(8 log 2)/π, c9,I = 2.58877 > 3
√2c1/2
√c2, c10,I = 9.37301 >
c0(1/2 − 2/π2) and c11,I = 9.0857 > c0e3/(4π · 8 log 2).

5.1.2. Type I terms: SI,2. The case q ≤ Q/V .
If q ≤ Q/V , then, for v ≤ V ,

2vα = va
q + O∗ ( v
Qq
 ) = va
q + O∗ ( 1
q2
 ) ,

and so va/q is a valid approximation to 2vα. (Here we are using v to label
an integer variable bounded above by v ≤ V ; we no longer need v to label the
quantity in (2.22), since that has been set equal to the constant 2.) Moreover,
for Qv = Q/v, we see that 2vα = (va/q) + O∗(1/qQv). If α = a/q + δ/x, then
vα = va/q + δ/(x/v). Now

(5.3) SI,2 = ∑

v≤V
v odd
 Λ(v) ∑

m≤U
m odd
 µ(m) ∑

n
n odd
 e((vα) · mn)η(mn/(x/v)).

We can thus estimate SI,2 by applying Lemma 3.5 to each inner double sum in
(5.3). We obtain that, if |δ| ≤ 1/2c2, where c2 = 6π/5
√c0 and c0 = 31.521, then
|SI,2| is at most

(5.4) ∑

v≤V Λ(v)
 




 x/v
2qv min (1, c0
(πδ)2
 )
 ∣
∣
∣
∣
∣
∣
∣
∣
∣
 ∑

m≤Mv/q
gcd(m,2q)=1
 µ(m)
m
 ∣
∣
∣
∣
∣
∣
∣
∣
∣
 + c10,I q
4x/v
 ( U
qv + 1
)2







plus
(5.5) ∑

v≤V Λ(v)
 ( 2
√c0c1
π U + 3c1
2 x
vqv log+ U
c2x
vqv + √c0c1
π qv log+ U
qv/2
 )

+ ∑

v≤V Λ(v) (c8,I max (log c11,I q2
v
x/v , 1
) qv + ( 2
√3c0c1
π + 3c1
2c2 + 55c0c2
6π2
 ) qv
) ,

MINOR ARCS FOR GOLDBACH’S PROBLEM 53

where qv = q/ gcd(q, v), Mv ∈ [min(Q/2v, U ), U ] and c1 = 1.0000028; if |δ| ≥
1/2c2, then |SI,2| is at most (5.4) plus
(5.6)
∑

v≤V Λ(v)
 

 √c0c1
π/2 U + 3c1
2
 

2 + (1 + ǫ)
ǫ log+ 2U

x/v
|δ|qv
 

 x/v
Q/v + 35c0c2
3π2 qv




+ ∑

v≤V Λ(v) √c0c1
π/2 (1 + ǫ) min (⌊ x/v
|δ|qv
 ⌋ + 1, 2U ) 



√3 + 2ǫ +
 log+ 2U⌊ x/v
|δ|qv
 ⌋
+1

2
 




Write SV = ∑v≤V Λ(v)/(vqv). By (2.12),

(5.7)
 SV ≤ ∑

v≤V
 Λ(v)
vq + ∑

v≤V
gcd(v,q)>1
 Λ(v)
v
 ( gcd(q, v)
q − 1
q
 )

≤ log V
q + 1
q
 ∑

p|q (log p)
 





vp(q) + ∑

α≥1
pα+vp(q)≤V
 1
pα − ∑

α≥1
pα≤V
 1
pα
 






≤ log V
q + 1
q
 ∑

p|q (log p)vp(q) = log V q
q .

This helps us to estimate (5.4). We could also use this to estimate the second
term in the ﬁrst line of (5.5), but, for that purpose, it will actually be wiser to
use the simpler bound

(5.8) ∑

v≤V Λ(v) x
vqv log+ U
c2x
vqv ≤ ∑

v≤V Λ(v) U/c2
e ≤ 1.0004
ec2 U V

(by (2.14) and the fact that t log+ A/t takes its maximum at t = A/e).
We bound the sum over m in (5.4) by (2.7) and (2.9). To bound the terms
involving (U/qv + 1)2, we use

∑

v≤V Λ(v)v ≤ 0.5004V 2 (by (2.17)),

∑

v≤V Λ(v)v gcd(v, q)
j ≤ ∑

v≤V Λ(v)v + V ∑

v≤V
gcd(v,q)̸=1
 Λ(v) gcd(v, q)
j ,

∑

v≤V
gcd(v,q)̸=1
 Λ(v) gcd(v, q) ≤ ∑

p|q (log p) ∑

1≤α≤logp V pvp(q) ≤ ∑

p|q (log p) log V
log p pvp(q)

≤ (log V ) ∑

p|q pvp(q) ≤ q log V

54 H. A. HELFGOTT

and ∑

v≤V
gcd(v,q)̸=1
 Λ(v) gcd(v, q)
2 ≤ ∑

p|q (log p) ∑

1≤α≤logp V pvp(q)+α

≤ ∑

p|q (log p) · 2pvp(q) · plogp V ≤ 2qV log q.

Using (2.14) and (5.7) as well, we conclude that (5.4) is at most

x
2q min (1, c0
(πδ)2
 ) min
 

 4
5 q/φ(q)

log+ min(Q/2V,U )
2q , 1



 log V q

+ c10,I
4x
 (
0.5004V 2q ( U
q + 1
)2 + 2U V q log V + 2U 2V log V
 )
 .

Assume Q ≤ 2U V /e. Using (2.14), (5.8), (2.18) and the inequality vq ≤ V q ≤
Q (which implies q/2 ≤ U/e), we see that (5.5) is at most

1.0004 (( 2
√c0c1
π + 3c1
2ec2
 ) U V + √c0c1
π Q log U
q/2
 )

+ (c5,I2 max (log c11,I q2

x , 2
) + c6,I2
) Q,

where c5,I2 = 3.53312 > 1.0004 · c8,I and

c6,I2 = 2
√3c0c1
π + 3c1
2c2 + 55c0c2
6π2 .

The expressions in (5.6) get estimated similarly. In particular,
∑

v≤V Λ(v) min (⌊ x/v
|δ|qv
 ⌋ + 1, 2U ) · 1
2 log+ 2U
⌊ x/v
|δ|qv
 ⌋ + 1

≤ ∑

v≤V Λ(v) max
t>0 t log+ U
t ≤ ∑

v≤V Λ(v) U
e = 1.0004
e U V,

but ∑

v≤V Λ(v) min (⌊ x/v
|δ|qv
 ⌋ + 1, 2U ) ≤ ∑

v≤ x
2U |δ|q
 Λ(v) · 2U

+ ∑

x
2U |δ|q <v≤V

gcd(v,q)=1
 Λ(v) x/|δ|
vq + ∑

v≤V Λ(v) + ∑

v≤V
gcd(v,q)̸=1
 Λ(v) x/|δ|
v
 ( 1
qv − 1
q
 )

≤ 1.03883 x
|δ|q + x
|δ|q max (log V − log x
2U |δ|q + log 3
√2 , 0
)

+ V + x
|δ| 1
q
 ∑

p|q (log p)vp(q)

≤ x
|δ|q
 (1.03883 + log q + log+ 6U V |δ|q
√2x
 ) + 1.0004V

by (2.12), (2.13), (2.14) and (2.15); we are proceeding much as in (5.7).

MINOR ARCS FOR GOLDBACH’S PROBLEM 55

If |δ| ≤ 1/2c2, then, assuming Q ≤ 2U V /e, we conclude that |SI,2| is at most

(5.9)
 x
2φ(q) min (1, c0
(πδ)2
 ) min
 ( 4/5

log+ Q
4V q2 , 1

)
 log V q

+ c8,I2 x
q
 ( U V
x
 )2 (1 + q
U
 )2 + c10,I
2
 (U V
x q log V + U 2V
x log V )

plus

(5.10) (c4,I2 + c9,I2)U V + (c10,I2 log U
q + c5,I2 max (log c11,I q2

x , 2
) + c12,I2) · Q,

where c4,I2 = 3.57422 > 2
√c0c1/π,
c5,I2 = 3.53312 > 1.0004 · c8,I ,

c8,I2 = 1.17257 > c10,I
4 · 0.5004,

c9,I2 = 0.82214 > 3c1 · 1.0004/2ec2,

c10,I2 = 1.78783 > 1.0004
√c0c1/π,
c12,I2 = 28.26771 > c6,I2 + c10,I2 log 2.

If |δ| ≥ 1/2c2, then |SI,2| is at most (5.9) plus
(5.11)

(c4,I2 + (1 + ǫ)c13,I2)U V + cǫ
 (c14,I2
 (log q + log+ 6U V |δ|q
√2x
 ) + c15,I2
) x
|δ|q

+ c16,I2
 (2 + 1 + ǫ
ǫ log+ 2U V |δ|q
x
 ) x
Q/V + c17,I2Q + cǫ · c18,I2V,

where
 c13,I2 = 1.31541 > 2
√c0c1
π · 1.0004
e ,

c14,I2 = 3.57422 > 2
√c0c1
π ,

c15,I2 = 3.71301 > 2
√c0c1
π · 1.03883,

c16,I2 = 1.50061 > 1.0004 · 3c1/2

c17,I2 = 25.0295 > 1.0004 · 35c0c2
3π2 ,

c18,I2 = 3.57565 > 2
√c0c1
π · 1.0004,

and cǫ = (1 + ǫ)
√3 + 2ǫ. We recall that c2 = 6π/5
√c0 = 0.67147 . . . . We will
choose ǫ ∈ (0, 1) later.
The case q > Q/V . We use Lemma 3.7 in this case.

5.1.3. Type II terms. As we showed in (4.1)–(4.6), SII (given in (4.1)) is at most

(5.12) 4 ∫ x/U

V
 √S1(U, W ) · S2(U, V, W ) dW
W + 4 ∫ x/U

V
 √S1(U, W ) · S3(W ) dW
W ,

where S1, S2 and S3 are as in (4.5) and (4.6). We bounded S1 in (4.33) and
(4.34), S2 in Prop. 4.6 and S3 in (4.6).

56 H. A. HELFGOTT

We ﬁrst recall our estimate for S1. In the whole range [V, x/U ] for W , we know
from (4.33) and (4.34) that S1(U, W ) is at most

(5.13) 2
π2 x
W + κ0ζ(3/2)
3 x
W
 √ x/W U
U ,

where κ0 = 1.27.
(We recall we are working with v = 2.)
We have better estimates for the constant in front in some parts of the range;
in what is usually the main part, (4.34) and (4.36) give us a constant of 0.15107
instead of 2/π2. Note that 1.27ζ(3/2)3 = 22.6417 . . . . We should choose U , V so
that the ﬁrst term dominates. For the while being, assume only

(5.14) U ≥ 5 · 10
5 x
V U ;

then (5.13) gives

(5.15) S1(U, W ) ≤ κ1 x
W ,

where κ1 = 2
π2 + 22.6418
√106/2 ≤ 0.2347.

This will suﬃce for our cruder estimates.
The second integral in (5.12) is now easy to bound. By (4.6),

S3(W ) ≤ 1.0171x + 2.0341W ≤ 1.0172x,

since W ≤ x/U ≤ x/5 · 105. Hence

4 ∫ x/U

V
 √S1(U, W ) · S3(W ) dW
W ≤ 4 ∫ x/U

V
 √κw,1 x
W · 1.0172x dW
W

≤ κ9 x
√V ,

where κ9 = 8 · √1.0172 · κ1 ≤ 3.9086.
(We are using the easy bound √a + b + c ≤ √
a + √
b + √c.)
Let us now examine S2, which was bounded in Prop. 4.6. Recall W ′ =
max(V, W/2), U ′ = max(U, x/2W ). Since W ′ ≥ W/2 and W ≥ V ≥ 117, we can
always bound

(5.16) ∑

W ′<p≤W (log p)
2 ≤ 1
2 W (log W ).

by (2.19).
Bounding S2 for δ arbitrary. We set

W0 = min(max(2θq, V ), x/U ),

where θ ≥ e is a parameter that will be set later.
For V ≤ W < W0, we use the bound (4.52):

S2(U ′, W ′, W ) ≤ (max(1, 2ρ) ( x
8q + x
2W
 ) + W
2 + 2q) · 1
2 W (log W )

≤ max ( 1
2 , ρ
) ( W
8q + 1
2
 ) x log W + W 2 log W
4 + qW log W,

MINOR ARCS FOR GOLDBACH’S PROBLEM 57

where ρ = q/Q.
If W0 > V , the contribution of the terms with V ≤ W < W0 to (5.12) is (by
5.15) bounded by

(5.17)
 4 ∫ W0

V
 √
κ1 x
W
 ( ρ0
4
 ( W
4q + 1
) x log W + W 2 log W
4 + qW log W ) dW
W

≤ κ2
2 √ρ0x ∫ W0

V
 √log W
W 3/2 dW + κ2
2 √
x ∫ W0

V
 √log W
W 1/2 dW

+ κ2
√ ρ0x2

16q + qx ∫ W0

V
 √
log W
W dW

≤ (κ2√ρ0 x
√
V + κ2√xW0
) √log W0

+ 2κ2
3
 √ ρ0x2

16q + qx (
(log W0)
3/2 − (log V )
3/2) ,

where ρ0 = max(1, 2ρ) and
 κ2 = 4
√κ1 ≤ 1.93768.

We now examine the terms with W ≥ W0. (If θq > x/U , then W0 = U/x, the
contribution of the case is nil, and the computations below can be ignored.)
We use (4.53):

S2(U ′, W ′, W ) ≤ ( x
4φ(q) 1
log(W/2q) + q
φ(q) W
log(W/2q)
 ) · 1
2 W log W.

By √a + b ≤ √
a + √b, we can take out the q/φ(q) · W/ log(W/2q) term and
estimate its contribution on its own; it is at most

(5.18)
 4 ∫ x/U

W0
 √
κ1 x
W · q
φ(q) · 1
2 W 2 log W
log W/2q dW
W

= κ2√2
 √ q
φ(q)
 ∫ x/U

W0
 √ x log W
W log W/2q dW

≤ κ2√2
 √ qx
φ(q)
 ∫ x/U

W0
 1
√W
 (
1 +
 √ log 2q
log W/2q
 )
 dW

Now ∫ x/U

W0
 1
√W
 √ log 2q
log W/2q dW ≤ √2q log 2q ∫ x/2U q

max(θ,V /2q)
 1
√t log t dt.

We bound this last integral somewhat crudely: for T ≥ e,

(5.19) ∫ T

e
 1
√t log t dt ≤ 2.3

√ T
log T

58 H. A. HELFGOTT

(by numerical work for e ≤ T ≤ T0 and by comparison of derivatives for T > T0,
where T0 = e(1−2/2.3)−1 = 2135.94 . . . ). Since θ ≥ e, this gives us that
∫ x/U

W0
 1
√
W
 (
1 +
 √ log 2q
log W/2q
 )
 dW

≤ 2
√ x
U + 2.3
√2q log 2q ·
 √ x/2U q
log x/2U q ,

and so (5.18) is at most

√2κ2√ q
φ(q)
 (
1 + 1.15

√ log 2q
log x/2U q
 ) x
√U .

We are left with what will usually be the main term, viz.,

(5.20) 4 ∫ x/U

W0
 √
S1(U, W ) · ( x
8φ(q) log W
log W/2q
 ) W dW
W ,

which, by (4.34), is at most x/
√φ(q) times the integral of

1
W
 √
√
√
√(
2H2 ( x
W U
 ) + κ4
2
 √ x/W U
U
 ) log W
log W/2q

for W going from W0 to x/U , where H2 is as in (4.35) and

κ4 = 4κ0ζ(3/2)
3 ≤ 90.5671.

By the arithmetic/geometric mean inequality, the integrand is at most 1/W times

(5.21) β + β−1 · 2H2(x/W U )
2 + β−1

2 κ4
2
 √ x/W U
U + β
2 log 2q
log W/2q
for any β > 0. We will choose β later.
The ﬁrst summand in (5.21) gives what we can think of as the main or worst
term in the whole paper; let us compute it ﬁrst. The integral is

(5.22)
 ∫ x/U

W0
 β + β−1 · 2H2(x/W U )
2 dW
W = ∫ x/U W0

1
 β + β−1 · 2H2(s)
2 ds
s

≤ ( β
2 + κ6
4β
 ) log x
U W0
by (4.36), where κ6 = 0.60428.
Thus the main term is simply

(5.23) ( β
2 + κ6
4β
 ) x
√φ(q) log x
U W0 .

The integral of the second summand is at most

β−1 · κ4
4
 √
x
U
 ∫ x/U

V
 dW
W 3/2 ≤ β−1 · κ4
2
 √ x/U V
U .

By (5.14), this is at most
 β−1
√2 · 10
−3 · κ4 ≤ β−1κ7/2,

MINOR ARCS FOR GOLDBACH’S PROBLEM 59

where
 κ7 = √
2κ4
1000 ≤ 0.1281.

Thus the contribution of the second summand is at most

β−1κ7
2 · x
√φ(q) .

The integral of the third summand in (5.21) is

(5.24) β
2
 ∫ x/U

W0
 log 2q
log W/2q dW
W .

If V < 2θq ≤ x/U , this is

β
2
 ∫ x/U

2θq
 log 2q
log W/2q dW
W = β
2 log 2q · ∫ x/2U q

θ
 1
log t dt
t

= β
2 log 2q · (log log x
2U q − log log θ) .

If 2θq > x/U , the integral is over an empty range and its contribution is hence 0.
If 2θq ≤ V , (5.24) is

β
2
 ∫ x/U

V
 log 2q
log W/2q dW
W = β log 2q
2
 ∫ x/2U q

V /2q
 1
log t dt
t

= β log 2q
2 · (log log x
2U q − log log V /2q)

= β log 2q
2 · log (1 + log x/U V
log V /2q
 ) .

(Of course, log(1 + (log x/U V )/(log V /2q)) ≤ (log x/U V )/(log V /2q); this is
smaller than (log x/U V )/ log 2q when V /2q > 2q.)
The total bound for (5.20) is thus

(5.25) x
√φ(q) · (
β · ( 1
2 log x
U W0 + Φ
2
 ) + β−1 ( 1
4 κ6 log x
U W0 + κ7
2
 )) ,

where

(5.26) Φ =
 



log 2q (
log log x
2U q − log log θ) if V /2θ < q < x/(2θU ).

log 2q log (
1 + log x/U V
log V /2q ) if q ≤ V /2θ.

Choosing β optimally, we obtain that (5.20) is at most

(5.27) x
√2φ(q)
 √(log x
U W0 + Φ) (κ6 log x
U W0 + 2κ7
),

where Φ is as in (5.26).
Bounding S2 for |δ| ≥ 8. Let us see how much a non-zero δ can help us. It
makes sense to apply (4.55) only when |δ| ≥ 4; otherwise (4.53) is almost certainly
better. Now, by deﬁnition, |δ|/x ≤ 1/qQ, and so |δ| ≥ 8 can happen only when
q ≤ x/8Q.

60 H. A. HELFGOTT

With this in mind, let us apply (4.55). Note ﬁrst that

x
|δq|
 (q + x
4W
 )−1 ≥ 1/|δq|
q
x + 1
4W ≥ 4/|δq|
1
2Q + 1
W

≥ 4W
|δ|q · 1
1 + W
2Q ≥ 4W
|δ|q · 1

1 + x/U
2Q .

This is at least 2 min(2Q, W )/|δq|. Thus we may apply (4.55)–(4.56) when |δq| ≤
2 min(2Q, W ). Since Q ≥ x/U , we know that min(2Q, W ) = W for all W ≤ x/U ,
and so it is enough to assume that |δq| ≤ 2W .
Recalling also (5.16), we see that (4.55) gives us
(5.28)

S2(U ′, W ′, W ) ≤ min
 



1, 2q/φ(q)

log ( 4W
|δ|q · 1
1+ x/U
2Q
 )
 




 ( x
|δq| + W
2
 ) · 1
2 W (log W ).

Similarly to before, we deﬁne W0 = max(V, θ|δq|), where θ ≥ 1 will be set later.
For W ≥ W0, we certainly have |δq| ≤ 2W . Hence the part of (5.12) coming from
the range W0 ≤ W < x/U is

(5.29)
 4 ∫ x/U

W0
 √S1(U, W ) · S2(U, V, W ) dW
W

≤ 4
√ q
φ(q)
 ∫ x/U

W0
 √
√
√
√
√S1(U, W ) · log W

log ( 4W
|δ|q · 1
1+ x/U
2Q
 ) (W x
|δq| + W 2

2
 ) dW
W .

By (4.34), the contribution of the term W x/|δq| to (5.29) is at most

4x
√|δ|φ(q)
 ∫ x/U

W0
 √
√
√
√
√
√
(
H2 ( x
W U
 ) + κ4
4
 √ x/W U
U
 ) log W

log ( 4W
|δ|q · 1
1+ x/U
2Q
 ) dW
W

Note that 1 + (x/U )/2Q ≤ 3/2. Proceeding as in (5.20)–(5.27), we obtain that
this is at most
 2x
√|δ|φ(q)
 √(log x
U W0 + Φ) (κ6 log x
U W0 + 2κ7
),

where

(5.30) Φ =
 



log (1+ǫ1)|δq|
4 log (1 + log x/U V
log 4V /|δ|(1+ǫ1)q ) if |δq| ≤ V /θ,

log 3|δq|
8 (
log log 8x
3U |δq| − log log 8θ
3 ) if V /θ < |δq| ≤ x/θU ,

where ǫ1 = x/2U Q. This is what we think of as the main term.
By (5.15), the contribution of the term W 2/2 to (5.29) is at most

(5.31) 4
√ q
φ(q)
 ∫ x/U

V
 √ κ1
2 x dW
√W · max
V ≤W ≤ x
U
 √
√
√
√ log W

max (
log 2W
|δq| , 2
) .

MINOR ARCS FOR GOLDBACH’S PROBLEM 61

Since t → (log t)/(log t/c) is decreasing for t > c, (5.31) is at most

4
√2κ1√ q
φ(q) x
√U
 √
√
√
√ log W0

max (
log 8W0
3|δq| , 8
3 ) .

If W0 > V , we also have to consider the range V ≤ W < W0. The part of
(5.12) coming from this is

4 ∫ θ|δq|

V
 √
S1(U, W ) · (log W ) ( W x
2|δq| + W 2

4 + W x
16(1 − ρ)Q + x
8(1 − ρ)
 ) dW
W .

We have already counted the contribution of W 2/4 in the above. The terms
W x/2|δ|q and W x/(16(1 − ρ)Q) contribute at most

4
√κ1
 ∫ θ|δq|

V
 √ x
W · (log W )W ( x
2|δq| + x
16(1 − ρ)Q
 ) dW
W

= 4
√κ1x
 ( 1
√2|δ|q + 1
4
√(1 − ρ)Q
 ) ∫ θ|δq|

V
 √
log W dW
W

≤ 2κ2
3 x
 ( 1
√2|δ|q + 1
4
√(1 − ρ)Q
 ) (
(log θ|δ|q)
3/2 − (log V )
3/2) .

The term x/8(1 − ρ) contributes

√κ1x ∫ θ|δq|

V
 √ log W
W (1 − ρ) dW
W ≤ √κ1x
√1 − ρ
 ∫ ∞

V
 √log W
W 3/2 dW

≤ κ2x

2
√(1 − ρ)V (
√log V + √1/ log V ),

where we use the estimate
∫ ∞

V
 √log W
W 3/2 dW = 1
√V
 ∫ ∞

1
 √log u + log V
u3/2 du

≤ 1
√V
 ∫ ∞

1
 √log V
u3/2 du + 1
√V
 ∫ ∞

1
 1
2
√log V log u
u3/2 du

= 2 √log V
√V + 1
2
√V log V · 4 ≤ 2
√V
 (√log V + √1/ log V ) .

* * *

It is time to collect all type II terms. Let us start with the case of general δ.
We will set θ ≥ e later. If q ≤ V /2θ, then |SII | is at most
(5.32)
 x
√
2φ(q) ·
 √(log x
U V + log 2q log (
1 + log x/U V
log V /2q
 )) (
κ6 log x
U V + 2κ7)

+ √
2κ2√ q
φ(q)
 (
1 + 1.15

√ log 2q
log x/2U q
 ) x
√U + κ9 x
√V .

62 H. A. HELFGOTT

If V /2θ < q ≤ x/2θU , then |SII| is at most
(5.33)
 x
√2φ(q) ·
 √(log x
U · 2θq + log 2q log log x/2U q
log θ
 ) (κ6 log x
U · 2θq + 2κ7
)

+ √2κ2√ q
φ(q)
 (
1 + 1.15

√ log 2q
log x/2U q
 ) x
√U + (κ2√log 2θq + κ9) x
√V

+ κ2
6
 (
(log 2θq)
3/2 − (log V )
3/2) x
√q

+ κ2
 (√2θ · log 2θq + 2
3 ((log 2θq)
3/2 − (log V )
3/2)
) √qx,

where we use the fact that Q ≥ x/U (implying that ρ0 = max(1, 2q/Q) equals 1
for q ≤ x/2U ). Finally, if q > x/2θU ,

(5.34)
 |SII| ≤ (κ2√2 log x/U + κ9) x
√V + κ2√log x/U x
√
U

+ 2κ2
3 ((log x/U )
3/2 − (log V )
3/2) ( x
2
√2q + √
qx) .

Now let us examine the alternative bounds for |δ| ≥ 8. If |δq| ≤ V /θ, then
|SII| is at most

(5.35)
 2x
√|δ|φ(q)
 √
√
√
√log x
U V + log |δq|(1 + ǫ1)
4 log
 (
1 + log x/U V
log 4V
|δ|(1+ǫ1)q
 )

· √κ6 log x
U V + 2κ7

+ κ2
√ 2q
φ(q) ·
 √ log V
log 2V /|δq| · x
√U + κ9 x
√V ,

where ǫ1 = x/2U Q. If |δq| > V /θ, then |SII | is at most
(5.36)

2x
√|δ|φ(q)
 √
√
√
√(
log x
U · θ|δ|q + log 3|δq|
8 log log 8x
3U |δq|
log 8θ/3
 ) (κ6 log x
U · θ|δq| + 2κ7
)

+ 2κ2
3
 ( x
√2|δq| + x
4
√Q − q
 ) (
(log θ|δq|)
3/2 − (log V )
3/2)

+
 ( κ2√2(1 − ρ)
 (√log V + √1/ log V ) + κ9
) x
√V

+ κ2√ q
φ(q) · √log θ|δq| · x
√
U ,

where ρ = q/Q. (Note that |δ| ≤ x/Qq implies ρ ≤ x/4Q2, and so ρ will be very
small and Q − q will be very close to Q.)

5.2. Adjusting parameters. Calculations. We must bound the exponential
sum ∑n Λ(n)e(αn)η(n/x). By (2.20), it is enough to sum the bounds we obtained
in §5.1. We will now see how it will be best to set U , V and other parameters.

MINOR ARCS FOR GOLDBACH’S PROBLEM 63

Usually, the largest terms will be

(5.37) C0U V,

where
(5.38)

C0 =
 {
c4,I2 + c9,I2 = 4.39636 if |δ| ≤ 1/2c2 ∼ 0.74463,
c4,I2 + (1 + ǫ)c13,I2 = 4.88963 + 1.31541ǫ if |δ| > 1/2c2

(from (5.10) and (5.11), type I; ǫ ∈ (0, 1) will be set later) and
(5.39)

x
√δ0φ(q)
 √
√
√
√log x
U V + (log δ0(1 + ǫ1)q) log
 (

1 + log x
U V
log V
δ0(1+ǫ1)q
 )√κ6 log x
U V + 2κ7

(from (5.32) and (5.35), type II; here δ0 = max(2, |δ|/4), while ǫ1 = x/2U Q for
|δ| > 8 and ǫ1 = 0 for |δ| < 8.
We set U V = κx/
√qδ0; we must choose κ > 0.
Let us ﬁrst optimise κ in the case |δ| ≤ 4, so that δ0 = 2 and ǫ1 = 0. For
the purpose of choosing κ, we replace √φ(q) by √q/C1, where C1 = 2.3536 ∼
510510/φ(510510), and also replace V by q2/c, c a constant. We use the approx-
imation

log
 (
1 + log x
U V
log V
|2q|
 )
 = log (1 + log(
√2q/κ)
log(q/2c)
 ) = log ( 3
2 + log 2
√c/κ
log q/2c
 )

∼ log 3
2 + 2 log 2
√c/κ
3 log q/2c .

What we must minimize, then, is
(5.40)

C0κ
√2q + C1√2q
 √
√
√
√(
log √2q
κ + log 2q
 (
log 3
2 + 2 log 2
√c
κ
3 log q
2c
 )) (κ6 log √2q
κ + 2κ7
)

≤ C0κ
√2q + C1
2
√q
 √
κ6
√κ′
1
 √
κ′
1 log q − ( 5
3 + 2
3 log 4c
log q
2c
 ) log κ + κ′
2

·
 √
κ′
1 log q − 2κ′
1 log κ + 4κ′
1κ7
κ6 + κ′
1 log 2

≤ C0√2q
 (
κ + κ
′
4
 (κ
′
1 log q − (( 5
6 + κ
′
1
) + 1
3 log 4c
log q
2c
 ) log κ + κ
′
3
)) ,

where
 κ
′
1 = 1
2 + log 3
2 , κ
′
2 = log √2 + log 2 log 3
2 + log 4c log 2q
3 log q/2c ,

κ
′
3 = 1
2
 (κ
′
2 + 4κ′
1κ7
κ6 + κ
′
1 log 2
) = log 4c
6 + (log 4c)2

6 log q
2c + κ
′
5,

κ
′
4 = C1
C0
 √ κ6
2κ′
1 ∼
 {
0.30925 if |δ| ≤ 4
0.27805
1+0.26902ǫ if |δ| > 4,

κ
′
5 = 1
2 (log √
2 + log 2 log 3
2 + 4κ′
1κ7
κ6 + κ
′
1 log 2) ∼ 1.01152.

64 H. A. HELFGOTT

Taking derivatives, we see that the minimum is attained when

(5.41) κ = ( 5
6 + κ
′
1 + 1
3 log 4c
log q
2c
 ) κ
′
4 ∼ (
1.7388 + log 4c
3 log q
2c
 ) · 0.30925

provided that |δ| ≤ 4. (What we obtain for |δ| > 4 is essentially the same, only
with log δ0q = log |δ|q/4 instead of log q, and 0.27805/(1 + 0.26902ǫ) in place of
0.30925.) For q = 5 · 105, c = 2.5 and |δ| ≤ 4 (typical values in the most delicate
range), we get that κ should be 0.55834 . . . , and the last line of (5.40) is then
0.02204 . . . ; for q = 106, c = 10, |δ| ≤ 4, we get that κ should be 0.57286 . . . , and
the last line of (5.40) is then 0.01656 . . . . If |δ| > 4, |δ|q = 5 · 105, c = 2.5 and
ǫ = 0.2 (say), then κ = 0.47637 . . . , and the last line of (5.40) is 0.02243 . . . ; if
|δ| > 4, |δ|q = 106, c = 10 and ǫ = 0.2, then κ = 0.48877 . . . , and the last line of
(5.40) is 0.01684 . . . .
(A back-of-the-envelope calculation suggests that choosing w = 1 instead of
w = 2 would have given bounds worse by about 15 percent.)
We make the choices

κ = 1/2, and so U V = 1
2
√qδ0
for the sake of simplicity. (Unsurprisingly, (5.40) changes very slowly around its
minimum.)
Now we must decide how to choose U , V and Q, given our choice of U V . We
will actually make two sets of choices. First, we will use the SI,2 estimates for
q ≤ Q/V to treat all α of the form α = a/q + O∗(1/qQ), q ≤ y. (Here y is
a parameter satisfying y ≤ Q/V .) The remaining α then get treated with the
(coarser) SI,2 estimate for q > Q/V , with Q reset to a lower value (call it Q′).
If α was not treated in the ﬁrst go (so that it must be dealt with the coarser
estimate) then α = a′/q′ + δ′/x, where either q′ > y or δ′q′ > x/Q. (Otherwise,
α = a′/q′ + O∗(1/q′Q) would be a valid estimate with q′ ≤ y.)
The value of Q′ is set to be smaller than Q both because this is helpful (it
diminishes error terms that would be large for large q) and because this is now
harmless (since we are no longer assuming that q ≤ Q/V ).

5.2.1. First choice of parameters: q ≤ y. The largest items aﬀected strongly by
our choices at this point are
(5.42)

c16,I2
 (2 + 1 + ǫ
ǫ log+ 2U V |δ|q
x
 ) x
Q/V + c17,I2Q (from SI,2, |δ| > 1/2c2),
(c10,I2 log U
q + 2c5,I2 + c12,I2
) Q (from SI,2, |δ| ≤ 1/2c2),

and

(5.43) κ2
√ 2q
φ(q)
 (
1 + 1.15

√ log 2q
log x/2U q
 ) x
√U + κ9 x
√V (from SII).

In addition, we have a relatively mild but important dependence on V in the
main term (5.39). We must also respect the condition q ≤ Q/V , the lower bound
on U given by (5.14) and the assumptions made at the beginning of section 5
(e.g. Q ≥ x/U , V ≥ 2 · 106). Recall that U V = x/
√qδ.
We set Q = x
8y ,

MINOR ARCS FOR GOLDBACH’S PROBLEM 65

since we will then have not just q ≤ y but also q|δ| ≤ x/Q = 8y, and so qδ0 ≤ 4y.
We want q ≤ Q/V to be true whenever q ≤ y; this means that

q ≤ Q
V = QU
U V = QU
x/2
√qδ0 = U √qδ0
4y

must be true when q ≤ y, and so it is enough to set U = 4y2/
√qδ0. The following
choices make sense: we will work with the parameters

(5.44) y = x1/3

6 , Q = x
8y = 3
4 x2/3, x/U V = 2
√qδ0 ≤ 2
√2y,

U = 4y2
√qδ0 = x2/3

9
√qδ0 , V = x
(x/U V ) · U = x
8y2 = 9x1/3

2 ,

where, as before, δ0 = max(2, |δ|/4). Thus ǫ1 ≤ x/2U Q ≤ 2
√6/x1/6. Assuming

(5.45) x ≥ 2.16 · 10
20,

we obtain that U/(x/U V ) ≥ (x3/2/9
√qδ0)/(2
√qδ0) = x2/3/18qδ0 ≥ x1/3/6 ≥
5 · 105, and so (5.14) holds. We also get that ǫ1 ≤ 0.002.
Since V = x/8y2 = (9/2)x1/3, (5.45) also implies that V ≥ 2 · 106 (in fact,
V ≥ 27 · 106). It is easy to check that

(5.46) V < x/4, U V ≤ x, Q ≥ √
ex, Q ≥ max(U, x/U ),

as stated at the beginning of section 5. Let θ = (3/2)3 = 27/8. Then

(5.47)
 V
2θq = x/8y2

2θq ≥ x
16θy3 = x
54y3 = 4 > 1,

V
θ|δq| = x/8y2

8θy ≥ x
64θy3 = x
216y3 = 1.

The ﬁrst type I bound is
(5.48)

|SI,1| ≤ x
q min (1, c′
0
δ2
 ) 


min
 



 4
5 q
φ(q)
log+ x2/3

9q 5
2 δ 1
2
0
 , 1




 (
log 9x 1
3 √
qδ0 + c3,I ) + c4,I q
φ(q)
 




+ (c7,I log y
c2 + c8,I log x) y + c10,I x1/3

3422q3/2δ
 1
2
0 (log 9x1/3√eqδ0)

+
 (
c5,I log 2x2/3

9c2√qδ0 + c6,I log x5/3

9
√qδ0
 ) x2/3

9
√qδ0 + c9,I √
x log 2x
c2 + c10,I
e ,

where the constants are as in §5.1.1. The function x → (log cx)/(log x/R), c, R ≥
1, attains its maximum on [R′, ∞], R′ > R, at x = R′. Hence, for qδ0 ﬁxed,

(5.49) min
 


 4/5

log+ 4x2/3

9(δ0q) 5
2
 , 1




 (
log 9x 1
3 √qδ0 + c3,I )

66 H. A. HELFGOTT

attains its maximum at x = (27/8)e6/5(qδ0)15/4, and so

min
 


 4/5

log+ 4x2/3

9(δ0q) 5
2
 , 1




 (log 9x 1
3 √qδ0 + c3,I ) + c4,I

≤ log 27
2 e
2/5(δ0q)
7/4 + c3,I + c4,I ≤ 7
4 log δ0q + 6.11676.

Examining the other terms in (5.48) and using (5.45), we conclude that
(5.50)

|SI,1| ≤ x
q min (
1, c′
0
δ2
 ) · min ( q
φ(q)
 ( 7
4 log δ0q + 6.11676
) , 1
2 log x + 5.65787
)

+ x2/3
√
qδ0 (0.67845 log x − 1.20818) + 0.0507x2/3,

where we are using (5.45) to simplify the smaller error terms. (The bound
(1/2) log x + 5.65787 comes from a trivial bound on (5.49).) We recall that
c′
0 = 0.798437 > c0/(2π)2.
Let us now consider SI,2. The terms that appear both for |δ| small and |δ|
large are given in (5.9). The second line in (5.9) equals

c8,I2
 ( x
4q2δ0 + 2U V 2

x + qV 2

x
 ) + c10,I2
2
 ( q
2
√qδ0 + x2/3

18qδ0
 )
 log 9x1/3

2

≤ c8,I2
 ( x
4q2δ0 + 9x1/3

2
√2 + 27
8
 )
 + c10,I2
2
 ( y1/6

23/2 + x2/3

18qδ0
 ) (1
3 log x + log 9
2
 )

≤ 0.29315 x
q2δ0 + (0.00828 log x + 0.03735) x2/3
√qδ0 + 0.00153
√x,

where we are using (5.45) to simplify. Now

(5.51) min
 ( 4/5

log+ Q
4V q2 , 1

)
 log V q = min
 ( 4/5
log+ y
4q2 , 1

)
 log 9x1/3q
2

can be bounded trivially by log(9x1/3q/2) ≤ (2/3) log x + log 3/4. We can also
bound (5.51) as we bounded (5.49) before, namely, by ﬁxing q and ﬁnding the
maximum for x variable. In this way, we obtain that (5.51) is maximal for
y = 4e4/5q2; since, by deﬁnition, x1/3/6 = y, (5.51) then equals

log 9(6 · 4e4/5q2)q
2 = 3 log q + log 108 + 4
5 ≤ 3 log q + 5.48214.

If |δ| ≤ 1/2c2, we must consider (5.10). This is at most

(c4,I2 + c9,I2) x
2
√qδ0 + (c10,I2 log x2/3

9q3/2√
δ0 + 2c5,I2 + c12,I2) · 3
4 x2/3

≤ 2.19818x
√qδ0 + (0.89392 log x + 23.0896)x2/3.

MINOR ARCS FOR GOLDBACH’S PROBLEM 67

If |δ| > 1/2c2, we must consider (5.11) instead. For ǫ = 0.07, that is at most

(c4,I2 + (1 + ǫ)c13,I2) x
2
√qδ0 + (3.30386 log δq3 + 16.4137) x
|δ|q

+ (68.8137 log |δ|q + 36.7795)x2/3 + 29.7467x1/3

= 2.49086 x
√qδ0 + (3.30386 log δq3 + 16.4137) x
|δ|q + (22.9379 log x + 56.576)x 2
3 .

Hence

(5.52)
 |SI,2| ≤ 2.49086 x
√qδ0

+ x · min (1, 4c′
0
δ2
 ) min
 ( 3
2 log q + 2.74107
φ(q) ,
 1
3 log x + 1
2 log 3
4
q
 )

+ 0.29315 x
q2δ0 + (22.9462 log x + 56.6134)x2/3

plus a term (3.30386 log δq2 + 16.4137) · (x/|δ|q) that appears if and only if |δ| ≥
1/2c2.
For type II, we have to consider two cases: (a) |δ| < 8, and (b) |δ| ≥ 8.
Consider ﬁrst |δ| < 8. Then δ0 = 2. Recall that θ = 27/8. We have q ≤ V /2θ
and |δq| ≤ V /θ thanks to (5.47). We apply (5.32), and obtain that, for |δ| < 8,
(5.53)

|SII | ≤ x
√
2φ(q) ·
 √
√
√
√ 1
2 log 4qδ0 + log 2q log
 (
1 +
 1
2 log 4qδ0
log V
2q
 )

· √0.30214 log 4qδ0 + 0.2562

+ 8.22088
√ q
φ(q)
 


1 + 1.15

√
√
√
√ log 2q

log 9x1/3√δ0
2
√q
 


 (qδ0)
1/4x2/3 + 1.84251x5/6

≤ x
√
2φ(q) ·
 √
Cx,2q log 2q + log q
2 · √0.30214 log 2q + 0.67506

+ 16.404
√ q
φ(q) x3/4 + 1.84251x5/6

where we deﬁne
 Cx,t := log
 (
1 + log 4t

2 log 9x1/3
2.004t
 )

for 0 < t < 9x1/3/2. (We have 2.004 here instead of 2 because we want a constant
≥ 2(1 + ǫ1) in later occurences of Cx,t, for reasons that will soon become clear.)
For purposes of later comparison, we remark that 16.404 ≤ 1.5785x3/4−4/5 for
x ≥ 2.16 · 1020.

68 H. A. HELFGOTT

Consider now case (b), namely, |δ| ≥ 8. Then δ0 = |δ|/4. By (5.47), |δq| ≤ V /θ.
Hence, (5.35) gives us that
(5.54)

|SII | ≤ 2x
√|δ|φ(q) ·
 √
√
√
√
√ 1
2 log |δq| + log |δq|(1 + ǫ1)
4 log
 

1 + log |δ|q

2 log 18x1/3
|δ|(1+ǫ1)q
 



· √0.30214 log |δ|q + 0.2562

+ 8.22088
√ q
φ(q)
 √
√
√
√ log 9x1/3
2
log 12x1/3
|δq| · (qδ0)
1/4x2/3 + 1.84251x5/6

≤ x
√δ0φ(q)
 √
Cx,δ0q log δ0(1 + ǫ1)q + log 4δ0q
2
 √0.30214 log δ0q + 0.67506

+ 1.68038
√ q
φ(q) x4/5 + 1.84251x5/6,

since

8.22088

√
√
√
√ log 9x1/3
2
log 12x1/3
|δq| ·(qδ0)
1/4 ≤ 8.22088

√ log 9x1/3
2
log 9 ·(x1/3/3)
1/4 ≤ 1.68038x4/5−2/3

for x ≥ 2.16 · 1020. Clearly

log δ0(1 + ǫ1)q ≤ log δ0q + log(1 + ǫ1) ≤ log δ0q + ǫ1.

Now note the fact ([RS62, Thm. 15]) that q/φ(q) < ̥(q), where

(5.55) ̥(q) = e
γ log log q + 2.50637
log log q .

Moreover, q/φ(q) ≤ 3 for q < 30. Since ̥(30) > 3 and ̥(t) is increasing for
t ≥ 30, we conclude that, for any q and for any r ≥ max(q, 30), q/φ(q) < ̥(r).
In particular, q/φ(q) ≤ ̥(y) = ̥(x1/3/6) (since, by (5.45), x ≥ 1803). It is easy
to check that x → √̥(x1/3/6)x4/5−5/6 is decreasing for x ≥ 1803. Using (5.45),
we conclude that 1.67718
√q/φ(q)x4/5 ≤ 0.83574x5/6. This allows us to simplify
the last lines of (5.53) and (5.54).
It is time to sum up SI,1, SI,2 and SII . The main terms come from the ﬁrst
lines of (5.53) and (5.54) and the ﬁrst term of (5.52). Lesser-order terms can be
dealt with roughly: we bound min(1, c′
0/δ2) and min(1, 4c′
0/δ2) from above by
2/δ0 (somewhat brutally) and 1/q2δ0 by 1/qδ0 (again, coarsely). For |δ| ≥ 1/2c2,

1
|δ| ≤ 4c2
δ0 , log |δ|
|δ| ≤ 2
e log 2 · log δ0
δ0 ;

MINOR ARCS FOR GOLDBACH’S PROBLEM 69

we use this to bound the term in the comment after (5.52). The terms inversely
proportional to q, φ(q) or q2 thus add up to at most

2x
δ0 · min
 ( 7
4 log δ0q + 6.11676
φ(q) ,
 1
2 log x + 5.65787
q
 )

+ 2x
δ0 · min
 ( 3
2 log q + 2.74107
φ(q) ,
 1
3 log x + 1
2 log 3
4
q
 )

+ 0.29315 x
qδ0 + 4c2x
qδ0 (3.30386 log q2 + 16.4137) + 2x
(e log 2)qδ0 · 3.30386 log δ0

≤ 2x
δ0 min
 ( log δ7/4
0 q13/4 + 8.858
φ(q) ,
 5
6 log x + 5.515
q
 )

+ 2x
δ0q (8.874 log q + 1.7535 log δ0 + 22.19)

≤ 2x
δ0
 

min
 ( log δ7/4
0 q13/4 + 8.858
φ(q) ,
 5
6 log x + 5.515
q
 )
 + log q 80
9 δ
 16
9
0 + 22.19
q
 

 .

As for the other terms – we use (5.45) to bound x2/3 and x2/3 log x by a small
constant times x5/6. We bound x2/3/
√qδ0 by x2/3/
√2 (in (5.50)).
The sums S0,∞ and S0,w in (2.23) are 0 (by (5.45)). We conclude that, for
q ≤ y = x1/3/6, x ≥ 2.16 · 1020 and η = η2 as in (1.4),
(5.56)
|Sη(x, α)| ≤ |SI,1| + |SI,2| + |SII |

≤ x
√φ(q)δ0
 √
Cx,δ0q(log δ0q + 0.002) + log 4δ0q
2
 √0.30214 log δ0q + 0.67506

+ 2.49086x
√qδ0 + 2x
δ0 min
 

 log δ
 7
4
0 q 13
4 + 80
9
φ(q) ,
 5
6 log x + 50
9
q
 

 + 2x
δ0
 log q 80
9 δ
 16
9
0 + 111
5
q

+ 3.14624x5/6,

where

(5.57) δ0 = max(2, |δ|/4), Cx,t = log
 (
1 + log 4t

2 log 9x1/3
2.004t
 )
 .

Since Cx,t is an increasing function as a function of t (for x ﬁxed and t ≤
9x1/3/2.004) and δ0q ≤ 2y, we see that Cx,t ≤ Cx,2y. It is clear that x ↦→ Cx,t
(ﬁxed t) is decreasing function of x. For x = 2.16 · 1020, Cx,2y = 1.39942 . . . .
Also, compare the value C3.1·1028,2·106 = 0.64020 . . . given by (5.57) to the value
of 1.196 . . . − 0.5 = 0.696 . . . for C3.1·1028,2·106 in a previous version [Helb] of the
present paper. (The largest gains are elsewhere.)

5.2.2. Second choice of parameters. If, with the original choice of parameters, we
obtained q > y = x1/3/6, we now reset our parameters (Q, U and V ). Recall
that, while the value of q may now change (due to the change in Q), we will be
able to assume that either q > y or |δq| > x/(x/8y) = 8y.

70 H. A. HELFGOTT

We want U/(x/U V ) ≥ 5 · 105 (this is (5.14)). We also want U V small. With
this in mind, we let

V = x1/3

3 , U = 500
√6x1/3, Q = x
U = x2/3

500
√6 .

Then (5.14) holds (as an equality). Since we are assuming (5.45), we have V ≥
2 · 106. It is easy to check that (5.45) also implies that U < √
x and Q > √ex,
and so the inequalities in (5.46) hold.
Write 2α = a/q + δ/x for the new approximation; we must have either q > y
or |δ| > 8y/q, since otherwise a/q would already be a valid approximation under
the ﬁrst choice of parameters. Thus, either (a) q > y, or both (b1) |δ| > 8 and
(b2) |δ|q > 8y. Since now V = 2y, we have q > V /2θ in case (a) and |δq| > V /θ
in case (b) for any θ ≥ 1. We set θ = e2.
By (5.2),

|SI,1| ≤ x
q min (1, c′
0
δ2
 ) (log x2/3 − log 500
√6 + c3,I + c4,I q
φ(q)
 )

+ (c7,I log Q
c2 + c8,I log x log c11,I Q2

x
 ) Q + c10,I U 2

4x log e1/2x2/3

500
√6 + c10,I
e

+
 (
c5,I log 1000
√6x1/3

c2 + c6,I log 500
√6x4/3)
 · 500
√6x1/3 + c9,I √
x log 2x
c2

≤ x
q min (1, c′
0
δ2
 ) ( 2
3 log x − 4.99944 + 1.00303 q
φ(q)
 ) + 1.063
10000 x2/3(log x)
2,

where we are bound log c11,I Q2/x by log x1/3. Just as before, we use the assump-
tion (5.45) when we have to bound a lower-order term (such as x1/2 log x) by a
multiple of a higher-order term (such as x2/3(log x)2).
We have q/φ(q) ≤ ̥(Q) (where ̥ is as in (5.55)) and we can check that

1.00303̥(Q) ≤ 0.0327 log x + 4.99944

for all x ≥ 106. We have either q > y or q|δ| > 8y; if q|δ| > 8y but q ≤ y, then
|δ| ≥ 8, and so c′
0/δ2q < 1/8|δ|q < 1/64y < 1/y. Hence

|SI,1| ≤ 4.1962x2/3 log x + 0.090843x2/3 + 0.001063x2/3(log x)
2

≤ 4.1982x2/3 log x + 0.001063x2/3(log x)
2.

We bound |SI,2| using Lemma 3.7. First we bound (3.49): this is at most

x
2q min (1, 4c′
0
δ2
 ) log x1/3q
3

+ c0
 ( 1
4 − 1
π2
 ) ( (U V )2 log x1/3
3
2x + 3c4
2 500
√6
9 + (500
√6x1/3 + 1)2x1/3

3x
 )
 ,

where c4 = 1.03884. We bound the second line of this using (5.45). As for the
ﬁrst line, we have either q ≥ y (and so the ﬁrst line is at most (x/2y)(log x1/3y/3))
or q < y and 4c′
0/δ2q < 1/16y < 1/y (and so the same bound applies). Hence
(3.49) is at most
 3
2 x2/3 ( 2
3 log x − log 9
) + 0.02017x2/3 log x.

MINOR ARCS FOR GOLDBACH’S PROBLEM 71

Now we bound (3.50), which comes up when |δ| ≤ 1/2c2, where c2 = 6π/5
√c0,
c0 = 31.521 (and so c2 = 0.6714769 . . . ). Since 1/2c2 < 8, it follows that q > y
(the alternative q ≤ y, |δq| > 2y is impossible). Then (3.50) is at most

(5.58)
 2
√c0c1
π
 (U V log U V
√e + Q (√
3 log c2x
Q + log U V
2 log U V
Q/2
 ))

+ 3c1
2 x
y log U V log U V
c2x/y + 16 log 2
π Q log c0e3Q2

4π · 8 log 2 · x log Q
2

+ 3c1
2
√2c2
 √x log c2x
2 + 25c0
4π2 (3c2)
1/2√x log x,

where c1 = 1.0000028 > 1 + (8 log 2)/V . Here log(c0e3Q2/(4π · 8 log 2 · x)) log Q/2
is at most log x1/3 log x2/3. Using this and (5.45), we get that (5.58) is at most

1177.617x2/3 log x + 0.0006406x2/3(log x)
2 + 29.5949x1/2 log x

≤ 1177.64x2/3 log x + 0.0006406x2/3(log x)
2.

If |δ| > 1/2c2, then we know that |δq| > max(y/2c2, 2y) = y/2c2. Thus (3.51)
(with ǫ = 0.01) is at most

2
√c0c1
π U V log U V
√e

+ 2.02
√c0c1
π
 ( x
y/2c2 + 1
) (
(
√3.02 − 1) log
 x
y/2c2 + 1
√2 + 1
2 log U V log e2U V
x
y/2c2
 )

+ ( 3c1
2
 ( 1
2 + 3.03
0.16 log x) + 20c0
3π2 (2c2)
3/2) √x log x.

Again by (5.45), this simpliﬁes to

≤ 1212.591x2/3 log x + 29.131x1/2 log x ≤ 1213.15x2/3(log x)
2.

Hence, in total and for any |δ|,

|SI,2| ≤ 1213.15x2/3(log x) + 0.0006406x2/3(log x)
2.

Now we must estimate SII. As we said before, either (a) q > y/4, or both (b1)
|δ| > 8 and (b2) |δ|q > 8y. Recall that θ = e2. In case (a), we use (5.33), and
obtain that, if y/4 < q ≤ x/2e2U , |SII | is at most
(5.59)

x√̥(q)
√2q
 √(log x
U · 2e2q + log 2q log log x/(2U q)
log e2
 ) (κ6 log x
U · 2e2q + 2κ7
)

+ √2κ2
√̥ ( x
2e2U
 ) (
1 + 1.15

√ log x/e2U
2
 ) x
√U + (κ2√log x/U + κ9) x
√V

+ κ2
6
 (
(log(e
2y/2))
3/2 − (log y)
3/2) x
√y

+ κ2
 (√2e2 · log x/U + 2
3 ((log x/U )
3/2 − (log V )
3/2)
) x
√2e2U ,

where ̥ is as in (5.55). It is easy to check that q → (log 2q)(log log q)/q is
decreasing for q ≥ y (indeed for q ≥ 9), and so the ﬁrst line of (5.59) is minimal
for q = y. Asymptotically, the largest term in (5.59) comes from the last line (of
order x5/6(log x)3/2), even if the ﬁrst line is larger in practice (while being of order

72 H. A. HELFGOTT

x5/6(log x) log log x). The ratio of (5.59) (for q = y = x1/3/6) to x5/6(log x)3/2 is
descending for x ≥ x0 = 2.16 · 1020; its value at x = x0 gives

(5.60) |SII | ≤ 0.272652x5/6(log x)
3/2

in case (a), for q ≤ x/2e2U .
If x/2e2U < q ≤ Q, we use (5.34). In this range, x/2
√2q + √
qx adopts its
maximum at q = Q (because x/2
√2q for q = x/2e2U is smaller than √qx for
q = Q, by (5.45)). A brief calculation starting from (5.34) then gives that

|SII | ≤ 0.10198x5/6(log x)
3/2,

where we use (5.45) yet again to simplify.
Finally, let us treat case (b), that is, |δ| > 8 and |δ|q > 8y; we can also assume
q ≤ y, as otherwise we are in case (a), which has already been treated. Since
|δ/x| ≤ x/Q, we know that |δq| ≤ x/Q = U . From (5.36), we obtain that |SII | is
at most

2x√̥(y)
√
8y
 √(log x
U · e2 · 8y + log 3y log log x/3U y
log 8e2/3
 ) (κ6 log x
U · e2 · 2y + 2κ7
)

+ 2κ2
3
 ( x
√
16y ((log 8e
2y)
3/2 − (log y)
3/2) + x/4
√
Q − y ((log e
2U )
3/2 − (log y)
3/2)
)

+
 ( κ2√2(1 − y/Q)
 (√log V + √1/ log V ) + κ9
) x
√
V

+ κ2√2̥(y) ·
 √ log e2U
log 8e2/3 · x
√
U ,

We take the maximum of the ratio of this to x5/6(log x)3/2, and obtain

|SII | ≤ 0.24956x5/6(log x)
3/2.

Thus (5.60) gives the worst case.
We now take totals, and obtain
(5.61)
Sη(x, α) ≤ |SI,1| + |SI,2| + |SII |

≤ (4.1982 + 1213.15)x2/3 log x + (0.001063 + 0.0006406)x2/3(log x)
2

+ 0.272652x5/6(log x)
3/2

≤ 0.27266x5/6(log x)
3/2 + 1217.35x2/3 log x,

where we use (5.45) yet again.

5.3. Conclusion.

Proof of main theorem. We have shown that |Sη(α, x)| is at most (5.56) for q ≤
x1/3/6 and at most (5.61) for q > x1/3/6. It remains to simplify (5.56) slightly.
Let
 ρ = Cx1,2q0(log 2q0 + 0.002) + log 8q0
2
0.30214 log 2q0 + 0.67506 = 3.61407 . . . ,

where x1 = 1025, q0 = 2 · 105. (We will be optimizing matters for x = x1, δ0q =
2q0, with very slight losses in nearby ranges.) By the geometric mean/arithmetic

MINOR ARCS FOR GOLDBACH’S PROBLEM 73

mean inequality,
√
Cx1,δ0q(log δ0q + 0.002) + log 4δ0q
2
 √
0.30214 log δ0q + 0.67506.

is at most
1
2
 ( 1
√ρ
 (Cx1,δ0q(log δ0q + 0.002) + log 4δ0q
2
 ) + √
ρ(0.30214 log δ0q + 0.67506)
)

≤ Cx,δ0q
2
√ρ (log δ0q + 0.002) + ( 1
4
√ρ + √ρ · 0.30214
2
 ) log δ0q

+ 1
2
 ( log 2
√ρ + √ρ
2 · 0.67506
)

≤ 0.27125 log
 (
1 + log 4t

2 log 9x1/3
2.004t
 )
 (log δ0q + 0.002) + 0.4141 log δ0q + 0.49911.

Now, for x ≥ x0 = 2.16 · 1020,
Cx,t
log t ≤ Cx0,t
log t ≤ 0.08659

for t ≤ 106, and

Cx,t
log t ≤ C6t3,t
log t ≤ 1
log t log
 (

1 + log 4t
2 log 27
1.002
 )
 ≤ 0.08659

if 106 < t ≤ x1/3/6. Hence

0.27125 · Cx,δ0q · 0.002 ≤ 0.000047 log δ0q.

We conclude that, for q ≤ x1/3/6,

|Sη(α, x)| ≤ Rx,δ0q log δ0q + 0.49911
√
φ(q)δ0 · x + 2.491x
√qδ0

+ 2x
δ0 min
 

 log δ
 7
4
0 q 13
4 + 80
9
φ(q) ,
 5
6 log x + 50
9
q
 

 + 2x
δ0
 log q 80
9 δ
 16
9
0 + 111
5
q + 3.2x5/6,

where
 Rx,t = 0.27125 log
 (
1 + log 4t

2 log 9x1/3
2.004t
 )
 + 0.41415.
 □

Appendix A. Norms of Fourier transforms

Our aim here is to give upper bounds on | ̂η′′
2 |∞, where η2 is as in (1.4). We
will do considerably better than the trivial bound | ̂η′′|∞ ≤ |η′′|1.

Lemma A.1. For every t ∈ R,

(A.1) |4e(−t/4) − 4e(−t/2) + e(−t)| ≤ 7.87052.

We will describe an extremely simple, but rigorous, procedure to ﬁnd the
maximum. Since |g(t)|2 is C 2 (in fact smooth), there are several more eﬃcient
and equally rigourous algorithms – for starters, the bisection method with error
bounded in terms of |(|g|2)′′|∞.

74 H. A. HELFGOTT

Proof. Let

(A.2) g(t) = 4e(−t/4) − 4e(−t/2) + e(−t).

For a ≤ t ≤ b,

(A.3) g(t) = g(a) + t − a
b − a (g(b) − g(a)) + 1
8 (b − a)
2 · O∗( max
v∈[a,b] |g′′(v)|).

(This formula, in all likelihood well-known, is easy to derive. First, we can
assume without loss of generality that a = 0, b = 1 and g(a) = g(b) = 0.
Dividing by g by g(t), we see that we can also assume that g(t) is real (and
in fact 1). We can also assume that g is real-valued, in that it will be enough
to prove (A.3) for the real-valued function ℜg, as this will give us the bound
g(t) = ℜg(t) ≤ (1/8) maxv |(ℜg)′′(v)| ≤ maxv |g′′(v)| that we wish for. Lastly, we
can assume (by symmetry) that 0 ≤ t ≤ 1/2, and that g has a local maximum or
minimum at t. Writing M = maxu∈[0,1] |g′′(u)|, we then have:

g(t) = ∫ t

0 g′(v)dv = ∫ t

0
 ∫ v

t g′′(u)dudv = O∗ (∫ t

0
 ∣
∣
∣
∣

∫ v

t M du
∣
∣
∣
∣ dv)

= O∗ (∫ t

0 (v − t)M dv) = O∗ ( 1
2 t2M ) = O∗ ( 1
8 M ) ,

as desired.)
We obtain immediately from (A.3) that

(A.4) max
t∈[a,b] |g(t)| ≤ max(|g(a)|, |g(b)|) + 1
8 (b − a)
2 · max
v∈[a,b] |g′′(v)|.

For any v ∈ R,

(A.5) |g′′(v)| ≤ ( π
2
 )2 · 4 + π2 · 4 + (2π)
2 = 9π2.

Clearly g(t) depends only on t mod 4π. Hence, by (A.4) and (A.5), to estimate
maxt∈R |g(t)| with an error of at most ǫ, it is enough to subdivide [0, 4π] into
intervals of length ≤ √8ǫ/9π2 each. We set ǫ = 10−6 and compute. □

Lemma A.2. Let η2 : R+ → R be as in (1.4). Then

(A.6) | ̂η′′
2 |∞ ≤ 31.521.

This should be compared with |η′′
2 |1 = 48.

Proof. We can write

(A.7) η′′
2 (x) = 4(4δ1/4(x) − 4δ1/2(x) + δ1(x)) + f (x),

where δx0 is the point measure at x0 of mass 1 (Dirac delta function) and

f (x) =
 



0 if x < 1/4 or x ≥ 1,
−4x−2 if 1/4 ≤ x < 1/2,
4x−2 if 1/2 ≤ x < 1.

Thus ̂η′′
2 (t) = 4g(t) + ̂f (t), where g is as in (A.2). It is easy to see that |f ′|1 =
2 maxx f (x) − 2 minx f (x) = 160. Therefore,

(A.8) ∣
∣
∣ ̂f (t)
∣
∣
∣ = ∣
∣
∣ ̂f ′(t)/(2πit)
∣
∣
∣ ≤ |f ′|1
2π|t| = 80
π|t| .

MINOR ARCS FOR GOLDBACH’S PROBLEM 75

Since 31.521 − 4 · 7.87052 = 0.03892, we conclude that (A.6) follows from Lemma
A.1 and (A.8) for |t| ≥ 655 > 80/(π · 0.03892).
It remains to check the range t ∈ (−655, 655); since 4g(−t) + ̂f (−t) is the
complex conjugate of 4g(t) + ̂f (t), it suﬃces to consider t non-negative. We use
(A.4) (with 4g + ̂f instead of g) and obtain that, to estimate maxt∈R |4g + ̂f (t)|
with an error of at most ǫ, it is enough to subdivide [0, 655) into intervals of

length ≤ √2ǫ/|(4g + ̂f )′′|∞ each and check |4g + ̂f (t)| at the endpoints. Now,
for every t ∈ R,
∣
∣
∣
∣( ̂f )′′ (t)
∣
∣
∣
∣ = ∣
∣
∣(−2πi)
2 ̂x2f (t)
∣
∣
∣ = (2π)
2 · O∗ (|x2f |1) = 12π2.

By this and (A.5), |(4g + ̂f )′′|∞ ≤ 48π2. Thus, intervals of length δ1 give an error
term of size at most 24π2δ2
1. We choose δ1 = 0.001 and obtain an error term less
than 0.000237 for this stage.
To evaluate ̂f (t) (and hence 4g(t) + ̂f (t)) at a point, we use Simpson’s rule
on subdivisions of the intervals [1/4, 1/2], [1/2, 1] into 200 · max(1, ⌊
√|t|⌋) sub-
intervals each.
6 The largest value of ̂f (t) we ﬁnd is 31.52065 . . . , with an error
term of at most 4.5 · 10−5. □

Lemma A.3. Let η2 : R+ → R be as in (1.4). Let ηy(t) = log(yt)η2(t), where
y ≥ 4. Then

(A.9) |η′
y|1 < (log y)|η′
2|1.

This was sketched in [Helb, (2.4)].

Proof. Recall that supp(η2) = (1/4, 1). For t ∈ (1/4, 1/2),

η′
y(t) = (4 log(yt) log 4t)
′ = 4 log 4t
t + 4 log yt
t ≥ 8 log 4t
t > 0,

whereas, for t ∈ (1/2, 1),

η′
y(t) = (−4 log(yt) log t)
′ = − 4 log yt
t − 4 log t
t = − 4 log yt2

t < 0,

where we are using the fact that y ≥ 4. Hence ηy(t) is increasing on (1/4, 1/2) and
decreasing on (1/2, 1); it is also continuous at t = 1/2. Hence |η′
y|1 = 2|ηy(1/2)|.
We are done by

2|ηy(1/2)| = 2 log y
2 · η2(1/2) = log y
2 · 8 log 2 < log y · 8 log 2 = (log y)|η′
2|1.
 □

Lemma A.4. Let y ≥ 4. Let g(t) = 4e(−t/4) − 4e(−t/2) + e(−t) and k(t) =
2e(−t/4) − e(−t/2). Then, for every t ∈ R,

(A.10) |g(t) · log y − k(t) · 4 log 2| ≤ 7.87052 log y.

Proof. By Lemma A.1, |g(t)| ≤ 7.87052. Since y ≥ 4, k(t) · (4 log 2)/ log y ≤ 6.
For any complex numbers z1, z2 with |z1|, |z2| ≤ ℓ, we can have |z1 − z2| > ℓ only
if | arg(z1/z2)| > π/3. It is easy to check that, for all t ∈ [−2, 2],
∣
∣
∣
∣arg ( g(t) · log y
4 log 2 · k(t)
 )∣
∣
∣
∣ = ∣
∣
∣
∣arg ( g(t)
k(t)
 )∣
∣
∣
∣ < 0.7 < π
3 .

6The author’s code uses D. Platt’s implementation [Pla11] of double-precision interval arith-
metic (based on Lambov’s [Lam08] ideas).

76 H. A. HELFGOTT

(It is possible to bound maxima rigorously as in (A.4).) Hence (A.10) holds. □

Lemma A.5. Let η2 : R+ → R be as in (1.4). Let η(y)(t) = (log yt)η2(t), where
y ≥ 4. Then

(A.11) |̂η′′
(y)|∞ < 31.521 · log y.

Proof. Clearly

η′′
(y)(x) = η′′
2 (x)(log y) + ((log x)η′′
2 (x) + 2
x η′
2(x) − 1
x2 η2(x)
)

= η′′
2 (x)(log y) + 4(log x)(4δ1/4(x) − 4δ1/2(x) + δ1(x)) + h(x),

where
 h(x) =
 



0 if x < 1/4 or x > 1,
4
x2 (2 − 2 log 2x) if 1/4 ≤ x < 1/2,
4
x2 (−2 + 2 log x) if 1/2 ≤ x < 1.

(Here we are using the expression (A.7) for η′′
2 (x).) Hence

(A.12) ̂η′′
(y)(t) = (4g(t) + ̂f (t))(log y) + (−16 log 2 · k(t) + ̂h(t)),

where k(t) = 2e(−t/4) − e(−t/2). Just as in the proof of Lemma A.2,

(A.13) | ̂f (t)| ≤ |f ′|1
2π|t| ≤ 80
π|t| , |̂h(t)| ≤ 160(1 + log 2)
π|t| .

Again as before, this implies that (A.11) holds for

|t| ≥ 1
π · 0.03892
 (80 + 160(1 + log 2)
(log 4)
 ) = 2252.51.

Note also that it is enough to check (A.11) for t ≥ 0, by symmetry. Our remaining
task is to prove (A.11) for 0 ≤ t ≤ 2252.21.
Let I = [0.3, 2252.21] \ [3.25, 3.65]. For t ∈ I, we will have

(A.14) arg
 ( 4g(t) + ̂f (t)

−16 log 2 · k(t) + ̂h(t)
 )
 ⊂ (− π
3 , π
3
 ) .

(This is actually true for 0 ≤ t ≤ 0.3 as well, but we will use a diﬀerent strategy
in that range in order to better control error terms.) Consequently, by Lemma
A.2 and log y ≥ log 4,

|̂η′′
(y)(t)| < max(|4g(t) + ̂f (t)| · (log y), |16 log 2 · k(t) − ̂h(t)|)

< max(31.521(log y), |48 log 2 + 25|) = 31.521 log y,

where we bound ̂h(t) by (A.13) and by a numerical computation of the maximum
of |̂h(t)| for 0 ≤ t ≤ 4 as in the proof of Lemma A.2.
It remains to check (A.14). Here, as in the proof of Lemma A.4, the allowable
error is relatively large (the expression on the left of (A.14) is actually contained
in (−1, 1) for t ∈ I). We decide to evaluate the argument in (A.14) at all t ∈
0.005Z ∩ I, computing ̂f (t) and ̂h(t) by numerical integration (Simpson’s rule)
with a subdivision of [−1/4, 1] into 5000 intervals. Proceeding as in the proof of
Lemma A.1, we see that the sampling induces an error of at most

(A.15) 1
2 0.005
2 max
v∈I ((4|g′′(v)| + |( ̂f )
′′(t)|) ≤ 0.0001
8 48π2 < 0.00593

MINOR ARCS FOR GOLDBACH’S PROBLEM 77

in the evaluation of 4g(t) + ̂f (t), and an error of at most

(A.16)
 1
2 0.005
2 max
v∈I ((16 log 2 · |k′′(v)| + |(̂h)
′′(t)|)

≤ 0.0001
8 (16 log 2 · 6π2 + 24π2 · (2 − log 2)) < 0.0121

in the evaluation of 16 log 2 · |k′′(v)| + |(̂h)′′(t)|.
Running the numerical evaluation just described for t ∈ I, the estimates for
the left side of (A.14) at the sample points are at most 0.99134 in absolute value;
the absolute values of the estimates for 4g(t) + ̂f (t) are all at least 2.7783, and
the absolute values of the estimates for | − 16 log 2 · log k(t) + ̂h(t)| are all at least
2.1166. Numerical integration by Simpson’s rule gives errors bounded by 0.17575
percent. Hence the absolute value of the left side of (A.14) is at most

0.99134 + arcsin ( 0.00593
2.7783 + 0.0017575
) + arcsin ( 0.0121
2.1166 + 0.0017575
)

≤ 1.00271 < π
3
for t ∈ I.
Lastly, for t ∈ [0, 0.3]∪[3.25, 3.65], a numerical computation (samples at 0.001Z;
interpolation as in Lemma A.2; integrals computed by Simpson’s rule with a
subdivision into 1000 intervals) gives

max
t∈[0,0.3]∪[3.25,3.65]
 (
|(4g(t) + ̂f (t))| + | − 16 log 2 · k(t) + ̂h(t)|
log 4
 )
 < 29.08,

and so maxt∈[0,0.3]∪[3.25,3.65] |̂η′′
(y)|∞ < 29.1 log y < 31.521 log y. □

An easy integral gives us that the function log ·η2 satisﬁes

(A.17) | log ·η2|1 = 2 − log 4

The following function will appear only in a lower-order term; thus, an ℓ1 estimate
will do.

Lemma A.6. Let η2 : R+ → R be as in (1.4). Then

(A.18) |(log ·η2)
′′|1 = 96 log 2.

Proof. The function log ·η(t) is 0 for t /∈ [1/4, 1], is increasing and negative for
t ∈ (1/4, 1/2) and is decreasing and positive for t ∈ (1/2, 1). Hence

|(log ·η2)
′′|∞ = 2 ((log ·η2)
′ ( 1
2
 ) − (log ·η2)
′ ( 1
4
 ))

= 2(16 log 2 − (−32 log 2)) = 96 log 2.
 □

References

[AS64] M. Abramowitz and I. A. Stegun. Handbook of mathematical functions with formu-
las, graphs, and mathematical tables, volume 55 of National Bureau of Standards
Applied Mathematics Series. For sale by the Superintendent of Documents, U.S.
Government Printing Oﬃce, Washington, D.C., 1964.
[BR02] G. Bastien and M. Rogalski. Convexit´e, compl`ete monotonie et in´egalit´es sur les
fonctions zˆeta et gamma, sur les fonctions des op´erateurs de Baskakov et sur des
fonctions arithm´etiques. Canad. J. Math., 54(5):916–944, 2002.

78 H. A. HELFGOTT

[But11] Y. Buttkewitz. Exponential sums over primes and the prime twin problem. Acta
Math. Hungar., 131(1-2):46–58, 2011.
[CW89] J. R. Chen and T. Z. Wang. On the Goldbach problem. Acta Math. Sinica,
32(5):702–718, 1989.
[Dab96] H. Daboussi. Eﬀective estimates of exponential sums over primes. In Analytic num-
ber theory, Vol. 1 (Allerton Park, IL, 1995), volume 138 of Progr. Math., pages
231–244. Birkh¨auser Boston, Boston, MA, 1996.
[DEtRZ97] J.-M. Deshouillers, G. Eﬃnger, H. te Riele, and D. Zinoviev. A complete Vinogradov
3-primes theorem under the Riemann hypothesis. Electron. Res. Announc. Amer.
Math. Soc., 3:99–104, 1997.
[DR01] H. Daboussi and J. Rivat. Explicit upper bounds for exponential sums over primes.
Math. Comp., 70(233):431–447 (electronic), 2001.
[EM95] M. El Marraki. Fonction sommatoire de la fonction de M¨obius. III. Majorations
asymptotiques eﬀectives fortes. J. Th´eor. Nombres Bordeaux, 7(2):407–433, 1995.
[EM96] M. El Marraki. Majorations de la fonction sommatoire de la fonction µ(n)
n . Univ.
Bordeaux 1, preprint (96-8), 1996.
[GR96] A. Granville and O. Ramar´e. Explicit bounds on exponential sums and the scarcity
of squarefree binomial coeﬃcients. Mathematika, 43(1):73–107, 1996.
[HB85] D. R. Heath-Brown. The ternary Goldbach problem. Rev. Mat. Iberoamericana,
1(1):45–59, 1985.
[HB11] H. Hong and Ch. W. Brown. QEPCAD B – Quantiﬁer elimination by partial cylin-
drical algebraic decomposition, May 2011. version 1.62.
[Hela] H. A. Helfgott. Major arcs for Goldbach’s problem. Preprint.
[Helb] H. A. Helfgott. Minor arcs for Goldbach’s problem. Preprint. Available as
arXiv:1205.5252.
[HL23] G. H. Hardy and J. E. Littlewood. Some problems of ‘Partitio numerorum’; III: On
the expression of a number as a sum of primes. Acta Math., 44(1):1–70, 1923.
[Hux72] M. N. Huxley. Irregularity in sifted sequences. J. Number Theory, 4:437–454, 1972.
[IK04] H. Iwaniec and E. Kowalski. Analytic number theory, volume 53 of American Math-
ematical Society Colloquium Publications. American Mathematical Society, Provi-
dence, RI, 2004.
[Lam08] B. Lambov. Interval arithmetic using SSE-2. In Reliable Implementation of Real
Number Algorithms: Theory and Practice. International Seminar Dagstuhl Castle,
Germany, January 8-13, 2006, volume 5045 of Lecture Notes in Computer Science,
pages 102–113. Springer, Berlin, 2008.
[LW02] M.-Ch. Liu and T. Wang. On the Vinogradov bound in the three primes Goldbach
conjecture. Acta Arith., 105(2):133–175, 2002.
[Mon68] H. L. Montgomery. A note on the large sieve. J. London Math. Soc., 43:93–98, 1968.
[Mon71] H. L. Montgomery. Topics in multiplicative number theory. Lecture Notes in Math-
ematics, Vol. 227. Springer-Verlag, Berlin, 1971.
[MV73] H. L. Montgomery and R. C. Vaughan. The large sieve. Mathematika, 20:119–134,
1973.
[MV74] H. L. Montgomery and R. C. Vaughan. Hilbert’s inequality. J. London Math. Soc.
(2), 8:73–82, 1974.
[Pla11] D. Platt. Computing degree 1 L-functions rigorously. PhD thesis, Bristol University,
2011.
[Rama] O. Ramar´e. Explicit estimates on several summatory functions involving the Moe-
bius function. Preprint.
[Ramb] O. Ramar´e. Explicit estimates on the summatory functions of the moebius function
with coprimality restrictions. Preprint.
[Ramc] O. Ramar´e. From explicit estimates for the primes to explicit estimates for the
Moebius function. Preprint.
[Ramd] O. Ramar´e. A sharp bilinear form decomposition for primes and moebius function.
Preprint. To appear in Acta. Math. Sinica.
[Ram10] O. Ramar´e. On Bombieri’s asymptotic sieve. J. Number Theory, 130(5):1155–1189,
2010.
[RR96] O. Ramar´e and R. Rumely. Primes in arithmetic progressions. Math. Comp.,
65(213):397–425, 1996.

MINOR ARCS FOR GOLDBACH’S PROBLEM 79

[RS62] J. B. Rosser and L. Schoenfeld. Approximate formulas for some functions of prime
numbers. Illinois J. Math., 6:64–94, 1962.
[RS75] J. B. Rosser and L. Schoenfeld. Sharper bounds for the Chebyshev functions θ(x)
and ψ(x). Math. Comp., 29:243–269, 1975. Collection of articles dedicated to Derrick
Henry Lehmer on the occasion of his seventieth birthday.
[Sel91] A. Selberg. Lectures on sieves. In Collected papers, vol. II, pages 66–247. Springer
Berlin, 1991.
[Tao] T. Tao. Every odd number greater than 1 is the sum of at most ﬁve primes. Preprint.
Available as arXiv:1201.6656.
[Vau77] R.-C. Vaughan. Sommes trigonom´etriques sur les nombres premiers. C. R. Acad.
Sci. Paris S´er. A-B, 285(16):A981–A983, 1977.
[Vin37] I. M. Vinogradov. Representation of an odd number as a sum of three primes. Dokl.
Akad. Nauk. SSR, 15:291–294, 1937.
[Vin04] I. M. Vinogradov. The method of trigonometrical sums in the theory of numbers.
Dover Publications Inc., Mineola, NY, 2004. Translated from the Russian, revised
and annotated by K. F. Roth and Anne Davenport, Reprint of the 1954 translation.

Harald Helfgott, ´Ecole Normale Sup´erieure, D´epartement de Math´ematiques,
45 rue d’Ulm, F-75230 Paris, France
E-mail address: harald.helfgott@ens.fr
