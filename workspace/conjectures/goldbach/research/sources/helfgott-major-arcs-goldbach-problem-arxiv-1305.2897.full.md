<!-- source: https://arxiv.org/pdf/1305.2897 | converted from PDF -->

arXiv:1305.2897v4  [math.NT]  14 Apr 2014
MAJOR ARCS FOR GOLDBACH’S PROBLEM

H. A. HELFGOTT

Abstract. The ternary Goldbach conjecture states that every odd number
n ≥ 7 is the sum of three primes. The estimation of the Fourier series∑
p≤x e(αp) and related sums has been central to the study of the problem
since Hardy and Littlewood (1923).
Here we show how to estimate such Fourier series for α in the so-called
major arcs, i.e., for α close to a rational of small denominator. This is part of
the author’s proof of the ternary Goldbach conjecture.
In contrast to most previous work on the subject, we will rely on a ﬁnite
veriﬁcation of the Generalized Riemann Hypothesis up to a bounded conduc-
tor and bounded height, rather than on zero-free regions. We apply a rigorous
veriﬁcation due to D. Platt; the results we obtain are both rigorous and un-
conditional.
The main point of the paper will be the development of estimates on para-
bolic cylinder functions that make it possible to use smoothing functions based
on the Gaussian. The generality of our explicit formulas will allow us to work
with a wide variety of such functions.

Contents

1. Introduction 2
1.1. Results 3
1.2. Main ideas 5
1.3. Acknowledgments 6
2. Preliminaries 7
2.1. Notation 7
2.2. Dirichlet characters and L functions 7
2.3. Mellin transforms 8
3. The Mellin transform of the twisted Gaussian 9
3.1. How to choose a smoothing function? 11
3.2. The Mellin transform of the twisted Gaussian 12
3.3. General approach and situation 13
3.4. Setup 13
3.5. The saddle point 13
3.6. The contour 17
3.7. The integral over the main contour segment C2 18
3.8. The integral over the rest of the contour 24
3.9. Conclusion 27
4. Explicit formulas 30
4.1. A general explicit formula 31
4.2. Sums and decay for the Gaussian: η♥(t) = e−t2/2 40
4.3. The case of η(t) = t2e−t2/2 and η∗(t) 44
4.4. The case of η+(t) 49
4.5. A sum for η+(t)2 52
4.6. A veriﬁcation of zeros and its consequences 56
1

2 H. A. HELFGOTT

Appendix A. Extrema via bisection and truncated series 60
Appendix B. Norms of smoothing functions 68
B.1. The decay of M h(iτ ) 69
B.2. The diﬀerence η+ − η◦ in ℓ2 norm. 72
B.3. Norms involving η+ 73
B.4. Norms involving η′
+ 74
B.5. The ℓ∞-norm of η+ 76
References 78

1. Introduction

The ternary Goldbach conjecture (or three-prime problem) states that every
odd number n greater than 5 can be written as the sum of three primes. Hardy
and Littlewood (1923) were the ﬁrst to treat the problem by means of the circle
method, i.e., Fourier analysis over Z. (Fourier transforms of functions on Z live
on the circle R/Z.)
I. M. Vinogradov [Vin37] showed in 1937 that the ternary Goldbach conjecture
is true for all n above a large constant C. The main innovation in his work
consisted in the estimation of sums of the form

(1.1) ∑

n≤N Λ(n)e(αn)

for α outside the so-called “major arcs” – these being a union of short intervals
in R/Z around the rationals with small denominator. (Here Λ(n) is the von
Mangoldt function, deﬁned as Λ(n) = log p for n a power of a prime p and
Λ(n) = 0 for n having at least two prime factors, whereas e(t) = e2πit.)
The estimation of such sums for α in the major arcs is also important, and
goes back to Hardy and Littlewood [HL23]. In some ways, their work is rather
modern – in particular, it studies a version of (1.1) with smooth truncation:

Sη(α, x) = ∑

n Λ(n)e(αn)η(n/x),

where η : R+ → C is a smooth function; in [HL23], η(t) = e−t.
We will show how to estimate sums such as Sη(α, x) for α in the major arcs.
We will see how we can obtain good estimates by using smooth functions η based
on the Gaussian e−t2/2. This will involve proving new, fully explicit bounds for
the Mellin transform1 of the twisted Gaussian, or, what is the same, parabolic
cylindrical functions in certain ranges. It will also require explicit formulae that
are general and strong enough, even for moderate values of x.
Any estimate on Sη(α, x) for α in the major arcs relies on the properties of
L-functions L(s, χ) = ∑
n χ(n)n−s, where χ : (Z/qZ)∗ → C is a multiplicative
character. In particular, what is key is the location of the zeroes of L(s, χ) in
the critical strip 0 ≤ ℜ(s) ≤ 1 (a region in which L(s, χ) can be deﬁned by
analytic continuation). In contrast to most previous work, we will not use zero-
free regions, which are too narrow for our purposes. Rather, we use a veriﬁcation
of the Generalized Riemann Hypothesis up to bounded height for all conductors
q ≤ 300000 (due to D. Platt [Plab]).

1See §2.3 for deﬁnitions.

MAJOR ARCS FOR GOLDBACH’S PROBLEM 3

The bounds we will obtain have shown themselves to be strong enough to prove
the ternary Goldbach conjecture. See [Helb]. A key feature of the present work
is that it allows one to mimic a wide variety of smoothing functions by means
of estimates on the Mellin transform of a single smoothing function – here, the
Gaussian e−t2/2.

1.1. Results. Write η♥(t) = e−t2/2. Let us ﬁrst give a bound for exponential
sums on the primes using η♥ as the smooth weight.

Theorem 1.1. Let x be a real number ≥ 108. Let χ be a primitive character
mod q, 1 ≤ q ≤ r, where r = 300000.
Then, for any δ ∈ R with |δ| ≤ 4r/q,

∞∑

n=1 Λ(n)χ(n)e ( δ
x n) e
− (n/x)2

2 = Iq=1 · ̂η♥(−δ) · x + E · x,

where Iq=1 = 1 if q = 1, Iq=1 = 0 if q ̸= 1, and

|E| ≤ 5.281 · 10
−22 + 1
√
x
 (650400
√q + 112
) .

We normalize the Fourier transform ̂f as follows: ̂f (t) = ∫ ∞
−∞ e(−xt)f (x)dx.
Of course, ̂η♥(−δ) is just √2πe−2π2δ2 .
As it turns out, smooth weights based on the Gaussian are often better in
applications than the Gaussian η♥ itself. Let us give a bound based on η(t) =
t2η♥(t).

Theorem 1.2. Let η(t) = t2e−t2/2. Let x be a real number ≥ 108. Let χ be a
primitive character mod q, 1 ≤ q ≤ r, where r = 300000.
Then, for any δ ∈ R with |δ| ≤ 4r/q,

∞∑

n=1 Λ(n)χ(n)e ( δ
x n) η(n/x) = Iq=1 · ̂η(−δ) · x + E · x,

where Iq=1 = 1 if q = 1, Iq=1 = 0 if q ̸= 1, and

|E| ≤ 4.269 · 10−14

q + 1
√x
 ( 276600
√
q + 56
) .

The advantage of η(t) = t2η♥(t) over η♥ is that it vanishes at the origin (to
second order); as we shall see, this makes it is easier to estimate exponential
sums with the smoothing η ∗M g, where ∗M is a Mellin convolution and g is
nearly arbitrary. Here is a good example that is used, crucially, in [Helc].

Corollary 1.3. Let η(t) = t2e−t2/2 ∗M η2(t), where η2 = η1 ∗M η1 and η1 =
2 · I[1/2,1]. Let x be a real number ≥ 108. Let χ be a primitive character mod q,
1 ≤ q ≤ r, where r = 300000.
Then, for any δ ∈ R with |δ| ≤ 4r/q,

∞∑

n=1 Λ(n)χ(n)e ( δ
x n) η(n/x) = Iq=1 · ̂η(−δ) · x + E · x,

where Iq=1 = 1 if q = 1, Iq=1 = 0 if q ̸= 1, and

|E| ≤ 4.269 · 10−14

q + 1
√x
 ( 380600
√
q + 76
) .

4 H. A. HELFGOTT

Let us now look at a diﬀerent kind of modiﬁcation of the Gaussian smoothing.
Say we would like a weight of a speciﬁc shape; for example, for the purposes of
[Helc], we would like an approximation to the function

(1.2) η◦ : t ↦→
 {
t3(2 − t)3e−(t−1)2/2 for t ∈ [0, 2],
0 otherwise.

At the same time, what we have is an estimate for the Mellin transform of the
Gaussian e−t2/2, centered at t = 0.
The route taken here is to work with an approximation η+ to η◦. We let

(1.3) η+(t) = hH (t) · te
−t2/2,

where hH is a band-limited approximation to

(1.4) h(t) =
 {
t2(2 − t)3et−1/2 if t ∈ [0, 2],
0 otherwise.

By band-limited we mean that the restriction of the Mellin transform of hH to
the imaginary axis is of compact support. (We could, alternatively, let hH be a
function whose Fourier transform is of compact support; this would be techni-
cally easier in some ways, but it would also lead to using GRH veriﬁcations less
eﬃciently.)
To be precise: we deﬁne

(1.5) FH(t) = sin(H log y)
π log y ,

hH(t) = (h ∗M FH)(y) = ∫ ∞

0 h(ty−1)FH (y) dy
y

and H is a positive constant. It is easy to check that M FH (iτ ) = 1 for −H <
τ < H and M FH (iτ ) = 0 for τ > H or τ < −H (unsurprisingly, since FH
is a Dirichlet kernel under a change of variables). Since, in general, the Mellin
transform of a multiplicative convolution f ∗M g equals M f · M g, we see that
the Mellin transform of hH , on the imaginary axis, equals the truncation of the
Mellin transform of h to [−iH, iH]. Thus, hH is a band-limited approximation
to h, as we desired.
The distinction between the odd and the even case in the statement that follows
simply reﬂects the two diﬀerent points up to which computations where carried
out in [Plab]; these computations, in turn, were tailored to the needs of [Hela]
(as was the shape of η+ itself).

Theorem 1.4. Let η(t) = η+(t) = hH (t)te−t2/2, where hH is as in (1.5) and
H = 200. Let x be a real number ≥ 1012. Let χ be a primitive character mod q,
where 1 ≤ q ≤ 150000 if q is odd, and 1 ≤ q ≤ 300000 if q is even.
Then, for any δ ∈ R with |δ| ≤ 600000 · gcd(q, 2)/q,

∞∑

n=1 Λ(n)χ(n)e ( δ
x n) η(n/x) = Iq=1 · ̂η(−δ) · x + E · x,

where Iq=1 = 1 if q = 1, Iq=1 = 0 if q ̸= 1, and

|E| ≤ 6.18 · 10−12
√
q + 1.14 · 10−10

q + 1
√x
 ( 499100
√q + 52
) .

MAJOR ARCS FOR GOLDBACH’S PROBLEM 5

If q = 1, we have the sharper bound

|E| ≤ 3.34 · 10
−11 + 251100
√x .

This is a paradigmatic example, in that, following the proof given in §4.4, we
can bound exponential sums with weights of the form hH (t)e−t2/2, where hH
is a band-limited approximation to just about any continuous function of our
choosing.
Lastly, we will need an explicit estimate of the ℓ2 norm corresponding to the
sum in Thm. 1.4, for the trivial character.

Proposition 1.5. Let η(t) = η+(t) = hH(t)te−t2/2, where hH is as in (1.5) and
H = 200. Let x be a real number ≥ 1012.
Then
∞∑

n=1 Λ(n)(log n)η2(n/x) = x · ∫ ∞

0 η2
+(t) log xt dt + E1 · x log x

= 0.640206x log x − 0.021095x + E2 · x log x,

where |E1| ≤ 1.536 · 10
−15 + 310.84
√x |E2| ≤ 2 · 10
−6 + 310.84
√x .

1.2. Main ideas. We will be working with smoothed sums

(1.6) Sη(α, x) =
 ∞∑

n=1 Λ(n)χ(n)e(δn/x)η(n/x).

Our integral will actually be of the form

(1.7) ∫

M Sη+(α, x)
2Sη∗ (α, x)e(−N α)dα,

where η+ and η∗ are two diﬀerent smoothing functions to be discussed soon.
Estimating the sums (1.6) on M reduces to estimating the sums

(1.8) Sη(δ/x, x) =
 ∞∑

n=1 Λ(n)χ(n)e(δn/x)η(n/x)

for χ varying among all Dirichlet characters modulo q ≤ r0 and for |δ| ≤ cr0/q,
i.e., |δ| small. Sums such as (1.8) are estimated using Dirichlet L-functions L(s, χ)
(see §2.2). An explicit formula gives an expression

(1.9) Sη,χ(δ/x, x) = Iq=1̂η(−δ)x − ∑

ρ Fδ(ρ)xρ + small error,

where Iq=1 = 1 if q = 1 and Iq=1 = 0 otherwise. Here ρ runs over the complex
numbers ρ with L(ρ, χ) = 0 and 0 < ℜ(ρ) < 1 (“non-trivial zeros”). The function
Fδ is the Mellin transform of e(δt)η(t) (see §2.3).
The questions are then: where are the non-trivial zeros ρ of L(s, χ)? How fast
does Fδ(ρ) decay as ℑ(ρ) → ±∞?
Write σ = ℜ(s), τ = ℑ(s). The belief is, of course, that σ = 1/2 for every
non-trivial zero (Generalized Riemann Hypothesis), but this is far from proven.
Most work to date has used zero-free regions of the form σ ≤ 1 − 1/C log q|τ |, C
a constant. This is a classical zero-free region, going back, qualitatively, to de la
Vall´ee-Poussin (1899). The best values of C known are due to McCurley [McC84]
and Kadiri [Kad05].

6 H. A. HELFGOTT

These regions seem too narrow to yield a proof of the three-primes theorem.
What we will use instead is a ﬁnite veriﬁcation of GRH “up to Tq”, i.e., a com-
putation showing that, for every Dirichlet character of conductor q ≤ r0 (r0 a
constant, as above), every non-trivial zero ρ = σ + iτ with |τ | ≤ Tq satisﬁes
ℜ(σ) = 1/2. Such veriﬁcations go back to Riemann; modern computer-based
methods are descended in part from a paper by Turing [Tur53]. (See the histori-
cal article [Boo06].) In his thesis [Pla11], D. Platt gave a rigorous veriﬁcation for
r0 = 105, Tq = 108/q. In coordination with the present work, he has extended
this to

• all odd q ≤ 3 · 105, with Tq = 108/q,
• all even q ≤ 4 · 105, with Tq = max(108/q, 200 + 7.5 · 107/q).

This was a major computational eﬀort, involving, in particular, a fast implemen-
tation of interval arithmetic (used for the sake of rigor).
What remains to discuss, then, is how to choose η in such a way Fδ(ρ) decreases
fast enough as |τ | increases, so that (1.9) gives a good estimate. We cannot hope
for Fδ(ρ) to start decreasing consistently before |τ | is at least as large as a multiple
of 2π|δ|. Since δ varies within (−cr0/q, cr0/q), this explains why Tq is taken
inversely proportional to q in the above. As we will work with r0 ≥ 150000, we
also see that we have little margin for maneuver: we want Fδ(ρ) to be extremely
small already for, say, |τ | ≥ 80|δ|. We also have a Scylla-and-Charybdis situation,
courtesy of the uncertainty principle: roughly speaking, Fδ(ρ) cannot decrease
faster than exponentially on |τ |/|δ| both for |δ| ≤ 1 and for δ large.
The most delicate case is that of δ large, since then |τ |/|δ| is small. It turns
out we can manage to get decay that is much faster than exponential for δ large,
while no slower than exponential for δ small. This we will achieve by working
with smoothing functions based on the (one-sided) Gaussian η♥(t) = e−t2/2.
The Mellin transform of the twisted Gaussian e(δt)e−t2/2 is a parabolic cylinder
function U (a, z) with z purely imaginary. Since fully explicit estimates for U (a, z),
z imaginary, have not been worked in the literature, we will have to derive them
ourselves.
Once we have fully explicit estimates for the Mellin transform of the twisted
Gaussian, we are able to use essentially any smoothing function based on the
Gaussian η♥(t) = e−t2/2. As we already saw, we can and will consider smoothing
functions obtained by convolving the twisted Gaussian with another function
and also functions obtained by multiplying the twisted Gaussian with another
function. All we need to do is use an explicit formula of the right kind – that
is, a formula that does not assume too much about the smoothing function or
the region of holomorphy of its Mellin transform, but still gives very good error
terms, with simple expressions.
All results here will be based on a single, general explicit formula (Lem. 4.1)
valid for all our purposes. The contribution of the zeros in the critical trip can
be handled in a uniﬁed way (Lemmas 4.3 and 4.4). All that has to be done for
each smoothing function is to bound a simple integral (in (4.24)). We then apply
a ﬁnite veriﬁcation of GRH and are done.

1.3. Acknowledgments. The author is very thankful to D. Platt, who, work-
ing in close coordination with him, provided GRH veriﬁcations in the necessary
ranges, and also helped him with the usage of interval arithmetic. Warm thanks

MAJOR ARCS FOR GOLDBACH’S PROBLEM 7

are due to A. C´ordoba and J. Cilleruelo, for discussions on the method of sta-
tionary phase, and to V. Blomer and N. Temme, for further help with para-
bolic cylinder functions. Gratitude is also felt towards A. Booker, B. Green, R.
Heath-Brown, H. Kadiri, O. Ramar´e, T. Tao and M. Watkins, for discussions
on Goldbach’s problem and related issues. Additional references were graciously
provided by R. Bryant, S. Huntsman and I. Rezvyakova.
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
The calculations contained in this paper used a nearly trivial amount of re-
sources; they were all carried out on the author’s desktop computers at home
and work. However, D. Platt’s computations [Plab] used a signiﬁcant amount
of resources, kindly donated to D. Platt and the author by several institutions.
This crucial help was provided by MesoPSL (aﬃliated with the Observatoire de
Paris and Paris Sciences et Lettres), Universit´e de Paris VI/VII (UPMC - DSI -
Pˆole Calcul), University of Warwick (thanks to Bill Hart), University of Bristol,
France Grilles (French National Grid Infrastructure, DIRAC instance), Univer-
sit´e de Lyon 1 and Universit´e de Bordeaux 1. Both D. Platt and the author would
like to thank the donating organizations, their technical staﬀ, and all academics
who helped to make these resources available to them.

2. Preliminaries

2.1. Notation. As is usual, we write µ for the Moebius function, Λ for the von
Mangoldt function. We let τ (n) be the number of divisors of an integer n and
ω(n) the number of prime divisors. For p prime, n a non-zero integer, we deﬁne
vp(n) to be the largest non-negative integer α such that pα|n.
We write (a, b) for the greatest common divisor of a and b. If there is any risk
of confusion with the pair (a, b), we write gcd(a, b). Denote by (a, b∞) the divisor∏
p|b pvp(a) of a. (Thus, a/(a, b∞) is coprime to b, and is in fact the maximal
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
it is not induced by any character of smaller modulus. Given a character χ, we

8 H. A. HELFGOTT

write χ∗ for the (uniquely deﬁned) primitive character inducing χ. If a character
χ mod q is induced by the trivial character χT , we say that χ is principal and
write χ0 for χ (provided the modulus q is clear from the context). In other words,
χ0(n) = 1 when (n, q) = 1 and χ0(n) = 0 when (n, q) = 0.
A Dirichlet L-function L(s, χ) (χ a Dirichlet character) is deﬁned as the ana-
lytic continuation of ∑n χ(n)n−s to the entire complex plane; there is a pole at
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

2.3. Mellin transforms. The Mellin transform of a function φ : (0, ∞) → C is

(2.1) M φ(s) := ∫ ∞

0 φ(x)xs−1dx.

If φ(x)xσ−1 is in ℓ1 with respect to dt (i.e., ∫ ∞
0 |φ(x)|xσ−1dx < ∞), then the
Mellin transform is deﬁned on the line σ + iR. Moreover, if φ(x)xσ−1 is in ℓ1 for
σ = σ1 and for σ = σ2, where σ2 > σ1, then it is easy to see that it is also in
ℓ1 for all σ ∈ (σ1, σ2), and that, moreover, the Mellin transform is holomorphic
on {s : σ1 < ℜ(s) < σ2}. We then say that {s : σ1 < ℜ(s) < σ2} is a strip of
holomorphy for the Mellin transform.
The Mellin transform becomes a Fourier transform (of η(e−2πv)e−2πvσ) by
means of the change of variables x = e−2πv. We thus obtain, for example, that
the Mellin transform is an isometry, in the sense that

(2.2) ∫ ∞

0 |f (x)|
2x2σ dx
x = 1
2π
 ∫ ∞

−∞ |M f (σ + it)|
2dt.

Recall that, in the case of the Fourier transform, for | ̂f |2 = |f |2 to hold, it is
enough that f be in ℓ1 ∩ ℓ2. This gives us that, for (2.2) to hold, it is enough that
f (x)xσ−1 be in ℓ1 and f (x)xσ−1/2 be in ℓ2 (again, with respect to dt, in both
cases).
We write f ∗M g for the multiplicative, or Mellin, convolution of f and g:

(2.3) (f ∗M g)(x) = ∫ ∞

0 f (w)g ( x
w
 ) dw
w .

In general,

(2.4) M (f ∗M g) = M f · M g

and

(2.5) M (f · g)(s) = 1
2πi
 ∫ σ+i∞

σ−i∞ M f (z)M g(s − z)dz [GR00, §17.32]

MAJOR ARCS FOR GOLDBACH’S PROBLEM 9

provided that z and s−z are within the strips on which M f and M g (respectively)
are well-deﬁned.
We also have several useful transformation rules, just as for the Fourier trans-
form. For example,

(2.6)
 M (f ′(t))(s) = −(s − 1) · M f (s − 1),

M (tf ′(t))(s) = −s · M f (s),

M ((log t)f (t))(s) = (M f )
′(s)

(as in, e.g., [BBO10, Table 1.11]).
Since (see, e.g., [BBO10, Table 11.3] or [GR00, §16.43])

(M I[a,b])(s) = bs − as

s ,

we see that

(2.7) M η2(s) = ( 1 − 2−s

s
 )2 , M η4(s) = ( 1 − 2−s

s
 )4 .

Let fz = e−zt, where ℜ(z) > 0. Then

(M f )(s) = ∫ ∞

0 e
−ztts−1dt = 1
zs
 ∫ ∞

0 e
−tdt

= 1
zs
 ∫ z∞

0 e
−uu
s−1du = 1
zs
 ∫ ∞

0 e
−tts−1dt = Γ(s)
zs ,

where the next-to-last step holds by contour integration, and the last step holds
by the deﬁnition of the Gamma function Γ(s).

3. The Mellin transform of the twisted Gaussian

Our aim in this section is to give fully explicit, yet relatively simple bounds for
the Mellin transform Fδ(ρ) of e(δt)η♥(t), where η♥(t) = e−t2/2 and δ is arbitrary.
The rapid decay that results will establish that the Gaussian η♥ is a very good
choice for a smoothing, particularly when the smoothing has to be twisted by an
additive character e(δt).
Gaussian smoothing has been used before in number theory; see, notably,
Heath-Brown’s well-known paper on the fourth power moment of the Riemann
zeta function [HB79]. What is new here is that we will derive fully explicit bounds
on the Mellin transform of the twisted Gaussian. This means that the Gaussian
smoothing will be a real option in explicit work on exponential sums in number
theory and elsewhere from now on.
(There has also been work using the Gaussian after a logarithmic change of
variables; see, in particular, [Leh66]. In that case, the Mellin transform is simply
a Gaussian (as in, e.g., [MV07, Ex. XII.2.9]). However, for δ non-zero, the Mellin
transform of a twist e(δt)e−(log t)2/2 decays very slowly, and thus would not be in
general useful.)

Theorem 3.1. Let fδ(t) = e−t2/2e(δt), δ ∈ R. Let Fδ be the Mellin transform of
fδ. Let s = σ + iτ , σ ≥ 0, τ ̸= 0. Let ℓ = −2πδ. Then, if sgn(δ) ̸= sgn(τ ),

(3.1) |Fδ(s)| ≤ C0,τ,ℓ · e
−E( |τ |
(πδ)2 )
·|τ |

+ C1,τ · e
−0.4798|τ | + C2,τ,ℓ · e
− min
( 1
8 ( τ
πδ )
2, 25
32 |τ |),

10 H. A. HELFGOTT

where
(3.2)

E(ρ) = 1
2
 (arccos 1
υ(ρ) − 2(υ(ρ) − 1)
ρ
 ) ,

C0,τ,ℓ = min
 (
2,
 √|τ |

2π|δ|
3.3
 ) (1 + max(7.83
1−σ, 1.63
σ−1)
) 

 3/2

min ( |τ |
2π|δ| , √|τ |)
 


1−σ
 ,

C1,τ =
 (
1 + 1 + √2
|τ |
 )
 |τ | σ
2 , υ(ρ) =
 √ 1 + √1 + ρ2

2 ,

C2,τ,ℓ = Pσ
 (min ( |τ |
2π|δ| , 5
4
 √|τ |)) ,

where Pσ(x) = xσ−2 if σ ∈ [0, 2], Pσ(x) = xσ−2 + (σ − 2)xσ−4 if σ ∈ (2, 4] and
Pσ(x) = xσ−2 + (σ − 2)xσ−4 + . . . + (σ − 2k)xσ−2(k+1) if σ ∈ (2k, 2(k + 1)].
If sgn(δ) = sgn(τ ) (or δ = 0) and |τ | ≥ 2,

(3.3) |Fδ(s)| ≤ C ′
τ,ℓe
− π
4 |τ |,

where
 C ′
τ,ℓ ≤ eπ/2|τ |σ/2

2 ·
 


1 + 2π3/2|δ|√
|τ | for σ ∈ [0, 1],

Γ(σ/2) for σ > 0 arbitrary.

As we shall see, the choice of η(t) = e−t2/2 can be easily motivated by the
method of stationary phase, but the problem is actually solved by the saddle-
point method. One of the challenges here is to keep all expressions explicit and
practical. This turns out to require the use of validated numerics (Appendix A);
in particular, the bisection method (implemented using interval arithmetic) gets
combined with a closer examination at inﬁnity and near extrema.
The expressions in Thm. 3.1 can be easily simpliﬁed further in applications
with some mild constraints, especially if one is ready to make some sacriﬁces in
the main term.

Corollary 3.2. Let fδ(t) = e−t2/2e(δt), δ ∈ R. Let Fδ be the Mellin transform
of fδ. Let s = σ + iτ , where σ ∈ [0, 1] and |τ | ≥ max(100, 4π2|δ|). Then, for
0 ≤ k ≤ 2,

(3.4) |Fδ(s + k)| + |Fδ(k + 1 − s)| ≤ ck ·
 



( |τ |
2π|δ| )k e
−0.1065( τ
πδ )
2 if |τ | < 3
2 (πδ)2,

|τ |k/2e−0.1598|τ | if |τ | ≥ 3
2 (πδ)2,

where c0 = 4.226, c1 = 3.516, c2 = 3.262.

It is natural to look at |Fδ(s + k)| + |Fδ(k + 1 − s)| with s in the critical strip
ℜ(s) ∈ [0, 1], since such expressions are key to the study of exponential sums with
a smoothing function equal to or based on tke−t2/2.
Let us end by a remark that may be relevant to applications outside number
theory. By (3.8), Thm. 3.1 gives us bounds on the parabolic cylinder function
U (a, z) for z purely imaginary and |ℜ(a)| ≤ 1/2. The bounds are useful when
|ℑ(a)| is at least somewhat larger than |ℑ(z)| (i.e., when |τ | is large compared
to ℓ). While the Thm. 3.1 is stated for σ ≥ 0 (i.e., for ℜ(a) ≥ 0), extending the

MAJOR ARCS FOR GOLDBACH’S PROBLEM 11

result to larger half-planes for a is not too hard – integration by parts can be
used to push a to the right.
As we shall see in §3.2, the literature on parabolic cylinder functions is rich
and varied. However, it stopped short of giving fully explicit expressions for a
general and z imaginary. That precluded, for instance, the use of the Gaussian
in explicit work on exponential sums in number theory. Such work will now be
possible.

3.1. How to choose a smoothing function? The method of stationary phase
([Olv74, §4.11], [Won01, §II.3])) suggests that the main contribution to the inte-
gral

(3.5) Fδ(t) = ∫ ∞

0 e(δt)η(t)ts dt
t

should come when the phase has derivative 0. The phase part of (3.5) is

e(δt) = tℑ(s) = e
2πiδt+τ log t

(where we write s = σ + iτ ); clearly,

(2πδt + τ log t)
′ = 2πδ + τ
t = 0

when t = −τ /2πδ. This is meaningful when t ≥ 0, i.e., sgn(τ ) ̸= sgn(δ). The
contribution of t = −τ /2πδ to (3.5) is then

(3.6) η(t)e(δt)ts−1 = η ( −τ
2πδ
 ) e
−iτ ( −τ
2πδ
 )σ+iτ −1

multiplied by a “width” approximately equal to a constant divided by

√|(2πiδt + τ log t)′′| = √| − τ /t2| = 2π|δ|
√
|τ | .

The absolute value of (3.6) is

(3.7) η (
− τ
2πδ
 ) · ∣
∣
∣
∣ −τ
2πδ
 ∣
∣
∣
∣

σ−1 .

In other words, if sgn(τ ) ̸= sgn(δ) and δ is not too small, asking that Fδ(σ +iτ )
decay rapidly as |τ | → ∞ amounts to asking that η(t) decay rapidly as t → 0.
Thus, if we ask for Fδ(σ + iτ ) to decay rapidly as |τ | → ∞ for all moderate δ, we
are requesting that

(1) η(t) decay rapidly as t → ∞,
(2) the Mellin transform F0(σ + iτ ) decay rapidly as τ → ±∞.

Requirement (2) is there because we also need to consider Fδ(σ + it) for δ very
small, and, in particular, for δ = 0.
There is clearly an uncertainty-principle issue here; one cannot do arbitrarily
well in both aspects at the same time. Once we are conscious of this, the choice
η(t) = e−t in Hardy-Littlewood actually looks fairly good: obviously, η(t) = e−t

decays exponentially, and its Mellin transform Γ(s + iτ ) also decays exponentially
as τ → ±∞. Moreover, for this choice of η, the Mellin transform Fδ(s) can be
written explicitly: Fδ(s) = Γ(s)/(1 − 2πiδ)s.

12 H. A. HELFGOTT

It is not hard to work out an explicit formula
2 for η(t) = e−t. However, it is
not hard to see that, for Fδ(s) as above, Fδ(1/2 + it) decays like e−t/2π|δ|, just as
we expected from (3.7). This is a little too slow for our purposes: we will often
have to work with relatively large δ, and we would like to have to check the zeroes
of L functions only up to relatively low heights t. We will settle for a diﬀerent
choice of η: the Gaussian.
The decay of the Gaussian smoothing function η(t) = e−t2/2 is much faster than
exponential. Its Mellin transform is Γ(s/2), which decays exponentially as ℑ(s) →
±∞. Moreover, the Mellin transform Fδ(s) (δ ̸= 0), while not an elementary or
very commonly occurring function, equals (after a change of variables) a relatively
well-studied special function, namely, a parabolic cylinder function U (a, z) (or,
in Whittaker’s [Whi03] notation, D−a−1/2(z)).
For δ not too small, the main term will indeed work out to be proportional to
e−(τ /2πδ)2/2, as the method of stationary phase indicated. This is, of course, much
better than e−τ /2π|δ|. The “cost” is that the Mellin transform Γ(s/2) for δ = 0
now decays like e−(π/4)|τ | rather than e−(π/2)|τ |. This we can certainly aﬀord.

3.2. The Mellin transform of the twisted Gaussian. We wish to approxi-
mate the Mellin transform

Fδ(s) = ∫ ∞

0 e
−t2/2e(δt)ts dt
t ,

where δ ∈ R. The parabolic cylinder function U : C2 → C is given by

U (a, z) = e−z2/4

Γ ( 1
2 + a) ∫ ∞

0 ta− 1
2 e
− 1
2 t2−ztdt

for ℜ(a) > −1/2; this can be extended to all a, z ∈ C either by analytic con-
tinuation or by other integral representations ([AS64, §19.5], [Tem10, §12.5(i)]).
Hence

(3.8) Fδ(s) = e
(πiδ)2Γ(s)U (s − 1
2 , −2πiδ) .

The second argument of U is purely imaginary; it would be otherwise if a Gaussian
of non-zero mean were chosen.
Let us brieﬂy discuss the state of knowledge up to date on Mellin transforms of
“twisted” Gaussian smoothings, that is, e−t2/2 multiplied by an additive character
e(δt). As we have just seen, these Mellin transforms are precisely the parabolic
cylinder functions U (a, z).
The function U (a, z) has been well-studied for a and z real; see, e.g., [Tem10].
Less attention has been paid to the more general case of a and z complex. The
most notable exception is by far the work of Olver [Olv58], [Olv59], [Olv61],
[Olv65]; he gave asymptotic series for U (a, z), a, z ∈ C. These were asymptotic
series in the sense of Poincar´e, and thus not in general convergent; they would
solve our problem if and only if they came with error term bounds. Unfortunately,
it would seem that all fully explicit error terms in the literature are either for a

2There may be a minor gap in the literature in this respect. The explicit formula given in
[HL23, Lemma 4] does not make all constants explicit. The constants and trivial-zero terms
were fully worked out for q = 1 by [Wig20] (cited in [MV07, Exercise 12.1.1.8(c)]; the sign of
hypκ,q(z) there seems to be oﬀ). As was pointed out by Landau (see [Har66, p. 628]), [HL23,
Lemma 4] actually has mistaken terms for χ non-primitive. (The author thanks R. C. Vaughan
for this information and the references.)

MAJOR ARCS FOR GOLDBACH’S PROBLEM 13

and z real, or for a and z outside our range of interest (see both Olver’s work and
[TV03].) The bounds in [Olv61] involve non-explicit constants. Thus, we will
have to ﬁnd expressions with explicit error bounds ourselves. Our case is that of
a in the critical strip, z purely imaginary.

3.3. General approach and situation. We will use the saddle-point method
(see, e.g., [dB81, §5], [Olv74, §4.7], [Won01, §II.4]) to obtain bounds with an
optimal leading-order term and small error terms. (We used the stationary-phase
method solely as an exploratory tool.)
What do we expect to obtain? Both the asymptotic expressions in [Olv59] and
the bounds in [Olv61] make clear that, if the sign of τ = ℑ(s) is diﬀerent from that
of δ, there will a change in behavior when τ gets to be of size about (2πδ)2. This is
unsurprising, given our discussion using stationary phase: for |ℑ(a)| smaller than
a constant times |ℑ(z)|2, the term proportional to e−(π/4)|τ | = e−|ℑ(a)|/2 should
be dominant, whereas for |ℑ(a)| much larger than a constant times |ℑ(z)|2, the

term proportional to e
− 1
2 ( τ
2πδ )
2 should be dominant.

3.4. Setup. We write

(3.9) φ(u) = u2

2 − (2πiδ)u − iτ log u

for u real or complex, so that

Fδ(s) = ∫ ∞

0 e
−φ(u)u
σ du
u .

We will be able to shift the contour of integration as we wish, provided that
it starts at 0 and ends at a point at inﬁnity while keeping within the sector
arg(u) ∈ (−π/4, π/4).
We wish to ﬁnd a saddle point. At a saddle point, φ′(u) = 0. This means that

(3.10) u − 2πiδ − iτ
u = 0, i.e., u2 + iℓu − iτ = 0,

where ℓ = −2πδ. The solutions to φ′(u) = 0 are thus

(3.11) u0 = −iℓ ± √−ℓ2 + 4iτ
2 .

The second derivative at u0 is

(3.12) φ
′′(u0) = 1
u2
0
 (
u2
0 + iτ ) = 1
u2
0 (−iℓu0 + 2iτ ).

Assign the names u0,+, u0,− to the roots in (3.11) according to the sign in front
of the square-root (where the square-root is deﬁned so as to have argument in
(−π/2, π/2]).
We assume without loss of generality that τ ≥ 0. We shall also assume at ﬁrst
that ℓ ≥ 0 (i.e., δ ≤ 0), as the case ℓ < 0 is much easier.

3.5. The saddle point. Let us start by estimating

(3.13) ∣
∣
∣us
0,+e
y/2∣
∣
∣ = |u0,+|
σe
− arg(u0,+)τ e
y/2,

14 H. A. HELFGOTT

where y = ℜ(−ℓiu0). (This is the main part of the contribution of the saddle
point, without the factor that depends on the contour.) We have

(3.14) y = ℜ (− iℓ
2
 (
−iℓ + √−ℓ2 + 4iτ )) = ℜ
 (

− ℓ2

2 − iℓ2

2
 √
−1 + 4iτ
ℓ2
 )
 .

Solving a quadratic equation, we get that

(3.15)
 √
−1 + 4iτ
ℓ2 =
 √ j(ρ) − 1
2 + i

√ j(ρ) + 1
2 ,

where j(ρ) = (1 + ρ2)1/2 and ρ = 4τ /ℓ2. Thus

y = ℓ2

2
 (√ j(ρ) + 1
2 − 1

)
 .

Let us now compute the argument of u0,+:

(3.16)
 arg(u0,+) = arg (
−iℓ + √−ℓ2 + 4iτ ) = arg (−i + √−1 + iρ)

= arg
 (
−i +
 √ −1 + j(ρ)
2 + i

√ 1 + j(ρ)
2
 )

= arcsin
 






 √ 1+j(ρ)
2 − 1
√
2
√ 1+j(ρ)
2
 (√ 1+j(ρ)
2 − 1
)
 







= arcsin
 



√
√
√
√ 1
2
 (
1 −
 √ 2
1 + j(ρ)
 )

 = 1
2 arccos
 √ 2
1 + j(ρ)

(by cos 2θ = 1 − 2 sin2 θ). Thus

(3.17) − arg(u0,+)τ + y
2 = −
 (

arccos
 √ 2
1 + j(ρ) − ℓ2

2τ
 (√ j(ρ) + 1
2 − 1

)) τ
2

= − (
arccos 1
υ(ρ) − 2(υ(ρ) − 1)
ρ
 ) τ
2 ,

where υ(ρ) = √(1 + j(ρ))/2.
It is clear that

(3.18) lim
ρ→∞
 (arccos 1
υ(ρ) − 2(υ(ρ) − 1)
ρ
 ) = π
2
whereas

(3.19) arccos 1
υ(ρ) − 2(υ(ρ) − 1)
ρ ∼ ρ
2 − ρ
4 = ρ
4

as ρ → 0+.
We are still missing a factor of |u0,+|σ (from (3.13)), a factor of |u0,+|−1 (from
the invariant diﬀerential du/u) and a factor of 1/
√|φ′′(u0,+)| (from the passage
by the saddle-point along a path of steepest descent). By (3.12), this is

|u0,+|σ−1
√|φ′′(u0,+)| = |u0,+|σ−1

1
|u0,+| √|−iℓu0,+ + 2iτ | = |u0,+|σ
√|−iℓu0,+ + 2iτ | .

MAJOR ARCS FOR GOLDBACH’S PROBLEM 15

By (3.11) and (3.15),

(3.20)
 |u0,+| =
 ∣
∣
∣
∣
∣ −iℓ + √−ℓ2 + 4iτ
2
 ∣
∣
∣
∣
∣ = ℓ
2 ·
 ∣
∣
∣
∣
∣

√ −1 + j(ρ)
2 +
 (√ 1 + j(ρ)
2 − 1

)
 i

∣
∣
∣
∣
∣

= ℓ
2
 √ −1 + j(ρ)
2 + 1 + j(ρ)
2 + 1 − 2

√ 1 + j(ρ)
2

= ℓ
2
 √
1 + j(ρ) − 2

√ 1 + j(ρ)
2 = ℓ
√2
 √υ(ρ)2 − υ(ρ).

Proceeding as in (3.14), we obtain that

(3.21)
 |−iℓu0,+ + 2iτ | =
 ∣
∣
∣
∣
∣
− iℓ
2
 (
−iℓ + ℓ
√
−1 + 4iτ
ℓ2
 )
 + 2iτ
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
− ℓ2

2 + 2iτ + ℓ2

2
 √ j(ρ) + 1
2 − iℓ2

2
 √ j(ρ) − 1
2
 ∣
∣
∣
∣
∣

= ℓ2

2
 √
√
√
√(
−1 +
 √ j(ρ) + 1
2
 )2 +
 (
ρ −
 √ j(ρ) − 1
2
 )2

= ℓ2

2
 √
j(ρ) + ρ2 + 1 − 2

√ j(ρ) + 1
2 − 2ρ
√ j(ρ) − 1
2 .

Since √j(ρ) − 1 = ρ/
√j(ρ) + 1, this means that
(3.22)

|−iℓu0,+ + 2iτ | = ℓ2

2
 √
√
√
√j(ρ) + ρ2 + 1 −
 √ 2
j(ρ) + 1 (j(ρ) + 1 + ρ2)

= ℓ2

2
 √j(ρ) + j(ρ)2 − (υ(ρ))−1(j(ρ) + j(ρ)2)

= ℓ2

2
 √2υ(ρ)2j(ρ)(1 − (υ(ρ))−1) = ℓ2√
j(ρ)
√2
 √υ(ρ)2 − υ(ρ).

Hence

|u0,+|σ
√
|−iℓu0,+ + 2iτ | =
 ( ℓ√2 √υ(ρ)2 − υ(ρ))σ

ℓ(j(ρ))1/4

21/4 (υ(ρ)2 − υ(ρ))1/4 = ℓσ−1

2 σ
2 − 1
4 j(ρ) 1
4 (υ(ρ)
2 − υ(ρ)) σ
2 − 1
4

= 2 σ
2 − 3
4

ρ σ−1
2 j(ρ) 1
4 (υ(ρ)
2 − υ(ρ)) σ
2 − 1
4 · τ σ−1
2 .

It remains to determine the direction of steepest descent at the saddle-point
u0,+. Let v ∈ C point in that direction. Then, by deﬁnition, v2φ′′(u0,+) is real
and positive, where φ is as in 3.9. Thus arg(v) = − arg(φ′′(u0,+))/2. By (3.12),

arg(φ
′′(u0,+)) = arg(−iℓu0,+ + 2iτ ) − 2 arg(u0,+).

Starting as in (3.21), we obtain that

arg(−iℓu0,+ + 2iτ ) = arctan
 

 ρ − √ j−1
2

−1 + √ j+1
2
 

 ,

16 H. A. HELFGOTT

and
(3.23)

ρ − √ j−1
2

−1 + √ j+1
2
 =
 (ρ − √ j−1
2
 ) (1 + √ j+1
2
 )

−1 + j+1
2 = ρ − √
2(j − 1) + ρ√2(j + 1)
j − 1

= ρ + √ 2
j+1 (
−√j2 − 1 + ρ · (j + 1)
)

j − 1 = ρ + 1
υ (−ρ + ρ · (j + 1))
j − 1

= ρ(1 + j/υ)
j − 1 = (j + 1)(1 + j/υ)
ρ = 2υ(υ + j)
ρ .

Hence, by (3.16),

arg(φ
′′(u0,+)) = arctan 2υ(υ + j)
ρ − arccos υ(ρ)
−1.

Therefore, the direction of steepest descent is

(3.24) arg(v) = − arg(φ′′(u0,+))
2 = arg(u0,+) − 1
2 arctan 2v(v + j)
ρ
= arg(u0,+) − arctan Υ,

where

(3.25) Υ = tan 1
2 arctan 2v(v + j)
ρ .

Since
 tan α
2 = 1
sin α − 1
tan α =
 √
1 + 1
tan2 α − 1
tan α ,

we see that

(3.26) Υ =
 (√

1 + ρ2

4υ2(υ + j)2 − ρ
2υ(υ + j)
 )
 .

Recall as well that

cos α
2 =
 √1 + cos α
2 , sin α
2 =
 √ 1 − cos α
2 .

Hence, if we let

(3.27) θ0 = arg(u0,+) = 1
2 arccos 1
υ(ρ) ,

we get that

(3.28)
 cos θ0 = cos ( 1
2 arccos 1
υ(ρ)
 ) =
 √ 1
2 + 1
2υ(ρ) ,

sin θ0 = sin ( 1
2 arccos 1
υ(ρ)
 ) =
 √ 1
2 − 1
2υ(ρ) .

We will prove now the useful inequality

(3.29) arctan Υ > θ0,

MAJOR ARCS FOR GOLDBACH’S PROBLEM 17

i.e., arg(v) < 0. By (3.24), (3.25) and (3.27), this is equivalent to arccos(1/υ) ≤
arctan 2υ(υ + j)/ρ. Since tan α = √1/ cos2 α − 1, we know that arccos(1/υ) =
arctan √
υ2 − 1; thus, in order to prove (3.29), it is enough to check that
√υ2 − 1 ≤ 2υ(υ + j)
ρ .

This is easy, since j > ρ and √υ2 − 1 < υ < 2υ.

3.6. The contour. We must now choose the contour of integration. First, let
us discuss our options. By (A.2), Υ ≥ 0.79837; moreover, it is easy to show
that Υ tends to 1 when either ρ → 0+ or ρ → ∞. This means that neither the
simplest contour (a straight ray from the origin within the ﬁrst quadrant) nor
what is arguably the second simplest contour (leaving the origin on a ray within
the ﬁrst quadrant, then sliding down a circle centered at the origin, passing past
the saddle point until you reach the x-axis, which you then follow to inﬁnity)
are acceptable: either contour passes through the saddle point on a direction
close to 45 degrees (= arctan(1)) oﬀ from the direction of steepest descent. (The
saddle-point method allows in principle for any direction less than 45 degrees oﬀ
from the direction of steepest descent, but the bounds can degrade rapidly – by
more than a constant factor – when 45 degrees are approached.)
It is thus best to use a curve that goes through the saddle point u+,0 in the
direction of steepest descent. We thus should use an element of a two-parameter
family of curves. The curve should also have a simple description in terms of
polar coordinates.
We decide that our contour C will be a lima¸con of Pascal. (Excentric circles
would have been another reasonable choice.) Let C be parameterized by

(3.30) y = (
− c1
ℓ r + c0) r, x = √r2 − y2

for r ∈ [(c0 − 1)ℓ/c1, c0ℓ/c1], where c0 and c1 are parameters to be set later.
The curve goes from (0, (c0 − 1)ℓ/c1) to (c0ℓ/c1, 0), and stays within the ﬁrst
quadrant.
3 In order for the curve to go through the point u0,+, we must have

(3.31) − c1r0
ℓ + c0 = sin θ0,

where

(3.32) r0 = |u0,+| = ℓ
√2
 √υ(ρ)2 − υ(ρ),

and θ0 and sin θ0 are as in (3.27) and (3.28). We must also check that the curve
C goes through u0,+ in the direction of steepest descent. The argument of the
point (x, y) is
 θ = arcsin y
r = arcsin (
− c1r
ℓ + c0) .

Hence
 r dθ
dr = r d arcsin (
− c1r
ℓ + c0)

dr = r · −c1/ℓ
cos arcsin (
− c1r
ℓ + c0) = −c1r
ℓ cos θ .

This means that, if v is tangent to C at the point u0,+,

tan(arg(v) − arg(u0,+)) = r dθ
dr = −c1r0
ℓ cos θ0 ,

3Because c0 ≥ 1, by (A.14).

18 H. A. HELFGOTT

and so, by (3.24),

(3.33) c1 = ℓ cos θ0
r0 Υ,

where Υ is as in (3.25). In consequence,

c0 = c1r0
ℓ + sin θ0 = (cos θ0) · Υ + sin θ0,

and so, by (3.28),

(3.34) c1 =
 √ 1 + 1/υ
υ2 − υ · Υ, c0 =
 √ 1
2 + 1
2υ · Υ +
 √ 1
2 − 1
2υ .

Incidentally, we have also shown that the arc-length inﬁnitesimal is

(3.35) |du| =
 √
1 + (
r dθ
dr
 )2dr =
 √
1 + (c1r/ℓ)2

cos2 θ dr =
 √
√
√
√1 + r2

ℓ2
c2
1 − ( c0
c1 ℓ − r)2 dr.

The contour will be as follows: ﬁrst we go out of the origin along a straight
radial segment C1; then we meet the curve C, and we follow it clockwise for a
segment C2, with the saddle-point roughly at its midpoint; then we follow another
radial ray C3 up to inﬁnity. For ρ small, C3 will just be the x-axis. Both C1 and
C3 will be contained within the ﬁrst quadrant; we will specify them later.

3.7. The integral over the main contour segment C2. We recall that

(3.36) φ(u) = u2

2 + ℓiu − iτ log u.

Our aim is now to bound the integral
∫
C2 e
−ℜ(φ(u))uσ−1du

over the main contour segment C2. We will proceed as follows. First, we will
parameterize the integral using a real variable ν, with the value ν = 0 corre-
sponding to the saddle point u = u0,+. We will bound ℜ(φ(u)) from below by
an expression of the form ℜ(φ(u0,+)) + ην2. We then bound |u|σ−1|du/dν| from
above by a constant. This procedure will give a bound that is larger than the
true value by at most a (very moderate) constant factor.
For u = x + iy (or (r, θ) in polar coordinates), (3.36) gives us

(3.37) ℜ(φ(u)) = x2 − y2

2 − ℓy + θτ = r2 − 2y2

2 − ℓy + τ arcsin y
r

= ( 4τ
ℓ
 )2 ψ0(ν) = ℓ2ρ
2ψ0(ν),

where, by (3.30), (3.31), and (3.34),

ψ0(ν) = (ν + ν0)2

2 (1 − 2(sin θ0 − c1ρν)
2)

− ν + ν0
ρ (sin θ0 − c1ρν) + arcsin(sin θ0 − c1ρν)
4ρ ,

and

(3.38) ν = r − r0
ℓρ , ν0 = r0
ℓρ .

MAJOR ARCS FOR GOLDBACH’S PROBLEM 19

By (3.30), (3.31) and (3.38),

(3.39) y
r = c0 − c1ρ(ν + ν0) = sin θ0 − c1ρν

and so

(3.40) c0 − c1ν0ρ = sin θ0.

The variable ν will range within an interval

(3.41) [α0, α1] ⊂ (− 1 − sin θ0
c1ρ , sin θ0
c1ρ
 ] .

(Here ν = −(1 − sin θ0)/(c1ρ) corresponds to the intersection with the y-axis, and
ν = (sin θ0)/(c1ρ) corresponds to the intersection with the x-axis.)
We work out the expansions around 0 of
(3.42)
(ν + ν0)2

2 (1 − 2(sin θ0 − c1ρν)
2) = ν2
0 cos 2θ0
2 + (ν0 cos 2θ0 + 2ν2
0 c1ρ sin θ0)ν

+ ( cos 2θ0
2 + 4c1ν0ρ sin θ0 − c
2
1ρ2ν2
0
 ) ν2

+ 2(−ν0c
2
1ρ
2 + c1ρ sin θ0)ν3 − c
2
1ρ2ν4,

− ν + ν0
ρ (sin θ0 − c1ρν) = − ν0 sin θ0
ρ + (− sin θ0
ρ + c1ν0
) ν + c1ν2,

arcsin(sin θ0 − c1ρν)
4ρ = θ0
4ρ + 1
4ρ
 ∞∑

k=1
 Pk(sin θ0)
(cos θ0)2k−1 (−c1ρ)k

k! νk

= θ0
4ρ + 1
4ρ
 ( −c1ρ
cos θ0 ν + (c1ρ)2 sin θ0
2(cos θ0)3 ν2 + . . . ) ,

where P1(t) = 1 and Pk+1(t) = P ′
k(t)(1−t2)+(2k−1)tP (t) for k ≥ 1. (This follows
from (arcsin z)′ = 1/
√1 − z2; it is easy to show that (arcsin z)(k) = Pk(z)(1 −
z2)−(k−1/2).)
We sum these three expressions and obtain a series ψ0(ν) = ∑k akνk. We
already know that

(1) a0 equals the value of ℜ(φ(u))/(ℓ2ρ2) at the saddle point u0,+,
(2) a1 = 0,
(3)

a2 = 1
2
 ( 1
ℓρ
)2 ( dr
dν
 )2 |φ
′′(u0,+)| ∣
∣
∣
∣ du
dr |r=r0
∣
∣
∣
∣
2 = 1
2 |φ
′′(u0,+)| ∣
∣
∣
∣ du
dr |r=r0
∣
∣
∣
∣

2 .

Here, as we know from (3.12), (3.22) and (3.20),

|φ
′′(u0,+)| = | − iℓu0,+ + 2iτ |
|u0,+|2 = ℓ2√ j(ρ)
2 √υ2 − υ

ℓ2
2 (υ2 − υ) =
 √ 2j(ρ)
υ2 − υ ,

20 H. A. HELFGOTT

and, by (3.34) and (3.35),

(3.43)
 ∣
∣
∣
∣ du
dr |r=r0
∣
∣
∣
∣ = |du|
|dr| |r=r0 =
 √
√
√
√1 + r2
0

ℓ2
c2
1 − ( c0
c1 ℓ − r0)2 =
 √
1 + c2
1
ℓ2 r2
0
1 − sin
2 θ0

=
 √
1 + c2
1
ℓ2
 ℓ2
2 (υ2 − υ)

1
2 + 1
2υ =
 √
1 + c2
1 υ2 − υ
1 + 1/υ

= √1 + Υ2.

Thus,
 a2 = 1
2
 √ 2j(ρ)
υ2 − υ (1 + Υ2),

where Υ is as in (3.26).
Let us simplify our expression for ψ0(ν) somewhat. We can replace the third
series in (3.42) by a truncated Taylor series ending at k = 2, namely,

arcsin(sin θ0 − c1ρν)
4ρ = θ0
4ρ + 1
4ρ
 ( −c1ρ
cos θ0 ν + (c1ρ)2 sin θ1
2(cos θ1)3 ν2)

for some θ1 between θ0 and θ. Then θ1 ∈ [0, π/2], and so

arcsin(sin θ0 − c1ρν)
4ρ ≥ θ0
4ρ + 1
4ρ · −c1ρ
cos θ0 ν.

Since
 R(ν) = −c
2
1ρ2ν2 + 2(sin θ0 − c1ρν0)c1ρν

is a quadratic with negative leading coeﬃcient, its minimum within [−α0, α1] (see
(3.41)) is bounded from below by min(R(−(1 − sin θ0)/(c1ρ)), R((sin θ0)/(c1ρ))).
We compare
 R ( sin θ0
c1ρ
 ) = 2c3 sin θ0 − sin2 θ0,

where c3 = sin θ0 − c1ρν0, and

R (− 1 − sin θ0
c1ρ
 ) = −2c3(1 − sin θ0) − (1 − sin θ0)
2

= 2c3 sin θ0 − sin2 θ0 − 2c3 − 1 + 2 sin θ0
.

The question is whether

R (− 1 − sin θ0
c1ρ
 ) − R ( sin θ0
c1ρ
 ) = −2c3 − 1 + 2 sin θ0

= −2(sin θ0 − c1ρν0) − 1 + 2 sin θ0
= 2c1ρν0 − 1

is positive. It is:

c1ρν0 = c1ρ0
ℓ = c1
√ υ2 − υ
2 =
 √ 1 + 1/υ
2 · Υ ≥ Υ
√2 ,

MAJOR ARCS FOR GOLDBACH’S PROBLEM 21

and, as we know from (A.2), Υ > 0.79837 is greater than 1/
√2 = 0.70710 . . . .
Hence, by (3.40),

R(ν) ≥ R ( sin θ0
c1ρ
 ) = 2c3 sin θ0 − sin2 θ0 = sin
2 θ0 − 2c1ρν0 sin θ0

= sin2 θ0 − 2(c0 − sin θ0) sin θ0 = 3 sin2 θ0 − 2c0 sin θ0

= 3 sin2 θ0 − 2((cos θ0) · Υ + sin θ0) sin θ0 = sin
2 θ0 − (sin 2θ0) · Υ.

We conclude that

(3.44) ψ0(ν) ≥ ℜ(φ(u0,+))
ℓ2ρ2 + ην2,

where

(3.45) η = a2 − 1
4ρ (c1ρ)2 sin θ0
2(cos θ0)3 + sin2 θ0 − (sin 2θ0) · Υ.

We can simplify this further, using

1
4ρ (c1ρ)2 sin θ0
2(cos θ0)3 = ρ
8 · 1 + 1/υ
υ2 − υ · Υ2 ·
 √ 1
2 − 1
2υ
( 1
2 + 1
2υ )3/2 = ρ
4 Υ2

υ2 − υ
 √1 − 1/υ
√1 + 1/υ

= ρ
4 Υ2

υ√υ2 − 1 = ρ
4 Υ2
√ j+1
2
 √ j−1
2
 = ρ
4 Υ2
√ρ2/4 = Υ2

2

and (by (3.28))
 sin 2θ0 = 2 sin θ0 cos θ0 = 2

√ 1
4 − 1
4υ2 =
 √υ2 − 1
υ

= υ√υ2 − 1
υ2 = ρ/2
(j + 1)/2 = ρ
j + 1 .

Therefore (again by (3.28))

(3.46) η = 1
2
 √ 2j
υ2 − υ (1 + Υ2) − Υ2

2 + 1
2 − 1
2υ − ρ
j + 1 · Υ.

Now recall that our task is to bound the integral

(3.47)
 ∫

C2 e
−ℜ(φ(u))|u|
σ−1|du| = ∫ α1

α0 e
−ℓ2ρ2ψ0(ν)(ℓρ(ν + ν0))
σ−1 ∣
∣
∣
∣ du
dr · dr
dν
 ∣
∣
∣
∣ dν

≤ (ℓρ)
σe
−ℜ(φ(u0,+)) · ∫ α1

α0 e
−ηℓ2ρ2·ν2(ν + ν0)
σ−1 ∣
∣
∣
∣ du
dr
 ∣
∣
∣
∣ dν.

(We are using (3.37) and (3.44).) Since u0,+ is a solution to equation (3.10), we
see from (3.9) that

ℜ(φ(u0,+)) = ℜ
 ( u2
0,+
2 + ℓiu0,+ − iτ log u0,+
)

= ℜ ( ℓiu0,+
2 + iτ
2 + τ arg(u0,+)
) = 1
2 ℜ(ℓiu0,+) + τ arg(u0, +).

We deﬁned y = ℜ(−ℓiu0) (after (3.13)), and we computed y/2 − arg(u0,+)τ in
(3.17). This gives us
 e
−ℜ(φ(u0,+)) = e
−(
arccos 1
υ − 2(υ−1)
ρ
 ) τ
2 .

22 H. A. HELFGOTT

If σ ≤ 1, we can bound

(3.48) (ν + ν0)
σ−1 ≤
 {
νσ−1
0 if ν ≥ 0,
(α0 + ν0)σ−1 if ν < 0,

provided that α0 + ν0 > 0 (as will be the case). If σ > 1, then

(ν + ν0)
σ−1 ≤
 {
νσ−1
0 if ν ≤ 0,
(α1 + ν0)σ−1 if ν > 0.

By (3.35), ∣
∣
∣
∣ du
dr
 ∣
∣
∣
∣ =
 √
1 + (c1r/ℓ)2

cos2 θ =
 √
1 + (c1ρ(ν + ν0))2

1 − (sin θ0 − c1ρν)2

(This diverges as θ → π/2; this is main reason why we cannot actually follow the
curve all the way to the y-axis.) Since we are aiming at a bound that is tight
only up to an order of magnitude, we can be quite brutal here, as we were when
using (3.48): we bound (c1r/ℓ)2 from above by its value when the curve meets
the x-axis (i.e., when r = c0ℓ/c1). We bound cos2 θ from below by its value when
ν = α1. We obtain
∣
∣
∣
∣ du
dr
 ∣
∣
∣
∣ =
 √
1 + c2
0
1 − (sin θ0 − c1ρα1)2 =
 √
1 + c2
0
cos2 θ− ,

where θ− is the value of θ when ν = α1.
Finally, we complete the integral in (3.47), we split it in two (depending on
whether ν ≥ 0 or ν < 0) and use
∫ α

0 e
ηℓ2ρ2·ν2dν ≤ 1
ℓρ
√η
 ∫ ∞

0 e
−ν2dν = √π/2
ℓρ
√η .

Therefore,
(3.49)∫

C2e
−ℜ(φ(u))|u|
σ−1|du|

= (ℓρ)
σe
−(
arccos 1
υ − 2(υ−1)
ρ
 ) τ
2
 √
1 + c2
0
cos2 θ− · √π/2
ℓρ
√η · (νσ−1
0 + (αjσ + ν0)
σ−1)

= √π
2 rσ−1
0
 


(
1 + (1 + αjσ
ν0
 )σ−1) √
1 + c2
0
cos2 θ−
 

 e
−(
arccos 1
υ − 2(υ−1)
ρ
 ) τ
2
√η ,

where jσ = 0 if σ ≤ 1 and jσ = 1 if σ > 1. We can set α1 = (sin θ0)/(c1ρ). We
can also express α0 + ν0 in terms of θ−:

(3.50) α0 + ν0 = r−
ℓρ = (c0 − sin θ−) ℓ
c1
ℓρ = c0 − sin θ−
c1ρ .

Since ν0 = r0/(ℓρ) (by (3.38)) and r0 is as in (3.32),

ν0 =
 √υ(ρ)2 − υ(ρ)
√2ρ .

Deﬁnition (3.25) implies immediately that Υ ≤ 1. Thus, by (3.34),

(3.51) c1ρν0 = Υ · √2(1 + 1/υ) ≤ 2Υ ≤ 2,

MAJOR ARCS FOR GOLDBACH’S PROBLEM 23

while, by (A.2),

(3.52) c1ρν0 = Υ · √2(1 + 1/υ) ≥ 0.79837 · √2

By (3.50) and (3.51),

(3.53) (1 + α0
ν0
 )−1 = ν0
α0 + ν0 = c1ρν0
c0 − sin θ− ≤ 2
c0 − sin θ− ,

whereas (1 + α1
ν0
 ) = 1 + sin θ0
c1ρν0 ≤ 1 + 1/
√2
0.79837 · √2 ≤ 1.62628.

We will now use some (rigorous) numerical bounds, proven in Appendix A. First
of all, by (A.14), c0 > 1 for all ρ > 0; this assures us that c0 − sin θ− > 0, and
so the last expression in (3.53) is well deﬁned. By (3.50), this also shows that
α0 + ν0 > 0, i.e., the curve C stays within the ﬁrst quadrant for 0 ≤ θ ≤ π/2, as
we said before.
We would also like to have an upper bound for

(3.54)
 √ 1
η
 (1 + c2
0
cos2 θ−
 ),

using (3.46). With this in mind, we ﬁnally choose θ−:

(3.55) θ− = π
4 .

Thus, by (A.29),
√ 1
η
 (1 + c2
0
cos2 θ−
 ) ≤
 √ 1 + 2c2
0
η ≤ √min(5, 0.86ρ) ≤ min(
√5, 0.93
√ρ).

We also get 2
c0 − sin θ− ≤ 2
1 − 1/
√2 ≤ 7.82843.

Finally, by (A.32),
√ υ2 − υ
2 ≥
 {ρ/6 if ρ ≤ 4,
√
ρ
2 − 1
23/2 ≤ (
1 − 1
23/2 ) √ρ
2 if ρ > 4

and so, since ρℓ = 4τ /ℓ, √ρℓ = 2
√τ and (1 − 1/23/2) ≤ 2/3, (3.32) gives us

r0 ≥
 { 2
3 τ
ℓ if τ ≤ ℓ2

2
3 √τ if τ > ℓ2 = 2
3 min ( τ
ℓ , √τ ) .

We conclude that

(3.56) ∫
C2 e
−ℜ(φ(u))|u|
σ−1|du| = Cτ,ℓ · e
−(
arccos 1
υ − 2(υ−1)
ρ
 ) τ
2 ,

where
(3.57)

Cτ,ℓ = min (2, 3.3
√τ
ℓ
 ) (1 + max (
7.83
1−σ, 1.63
σ−1)) ( 3/2
min(τ /ℓ, √τ )
 )1−σ

for all τ > 0, ℓ > 0 and all σ. By reﬂection on the x-axis, the same bound holds
for τ < 0, ℓ < 0 and all σ. Lastly, (3.56) is also valid for ℓ = 0, provided we
replace (3.57) and the exponent of (3.56) by their limits as ℓ → 0+.

24 H. A. HELFGOTT

3.8. The integral over the rest of the contour. It remains to complete the
contour. Since we have set θ− = π/4, C1 will be a segment of the ray at 45
degrees from the x-axis, counterclockwise (i.e., y = x, x ≥ 0). The segment will
go from (0, 0) up to (x, y) = (r−/
√2, r−/
√2), where, by (3.30),
1
√2 = y
r− = − c1
ℓ r + c0,

and so

(3.58) r− = ℓ
c1
 (c0 − 1
√2
 ) .

Let w = (1 + i)/
√2. Looking at (3.9), we see that
(3.59)∣
∣
∣
∣
∫

C1 e
−u2/2e(δu)us−1du∣
∣
∣
∣ = ∣
∣
∣
∣
∫

C1 e
−φ(u)uσ−1du∣
∣
∣
∣

≤ ∫
C1 e
−ℜ(φ(u))|u|
σ−1|du| = ∫ r−

0 e
−ℜ(φ(tw))tσ−1dt,

where φ(u) is as in (3.36). Here

(3.60) ℜ(φ(tw)) = ℜ ( t2

2 i + ℓiwt − iτ (
log t + i π
4
 )) = − ℓt
√
2 + π
4 τ,

and, by (A.33),

− ℓr−√
2 + π
4 τ ≥ −0.07639ℓ2ρ + π
4 τ = ( π
4 − 0.30556
) τ > 0.4798τ.

Consider ﬁrst the case σ ≥ 1. Then
∫ r−

0 e
−ℜ(φ(tw))tσ−1dt ≤ rσ−1
−
 ∫ r−

0 e
 ℓt√
2 − π
4 τ dt ≤ rσ
−e
 ℓr−√
2 − π
4 τ .

By (3.58) and (A.33),

(3.61) r− ≤ √ρℓ/2 ≤ √τ ,

Hence, for σ ≥ 1,

(3.62) ∣
∣
∣
∣

∫

C1 e
−u2/2e(δu)us−1du
∣
∣
∣
∣ ≤ τ σ/2e
−0.4798τ .

Assume now that 0 ≤ σ < 1, s ̸= 0. We can see that it is wise to start by an
integration by parts, so as to avoid convergence problems arising from the term
tσ−1 within the integral as σ → 0+. We have
∫
C1 e
−u2/2e(δu)us−1du = e
−u2/2e(δu) us

s |
wr−
0 − ∫

C1
 (e
−u2/2e(δu)
)′ us

s du.

By (3.60), ∣
∣
∣
∣e
−u2/2e(δu) us

s |
wr−
0
 ∣
∣
∣
∣ = e
−ℜ(φ(wr−)) · rσ
−
|s| ≤ rσ
−
τ · e
 ℓr−√2 − π
4 τ

As for the integral,
(3.63)∫

C1
 (e
−u2/2e(δu)
)′ us

s du = − ∫

C1 (u + ℓi)e
−u2/2−ℓiu us

s du

= − 1
s
 ∫
C1 e
−u2/2e(δu)us+1du − ℓi
s
 ∫
C1 e
−u2/2e(δu)usdu.

MAJOR ARCS FOR GOLDBACH’S PROBLEM 25

Hence, by (3.59) and (3.60),
∣
∣
∣
∣
∫

C1
 (e
−u2/2e(δu)
)′ us

s du∣
∣
∣
∣ ≤ 1
|s|
 ∫ r−

0 e
 ℓt√2 − π
4 τ tσ+1dt + ℓ
|s|
 ∫ r−

0 e
 ℓt√2 − π
4 τ tσdt

≤
 ( rσ+1
−
|s| + ℓrσ
−
|s|
 ) ∫ r−

0 e
 ℓt√2 − π
4 τ dt

≤ rσ+1
− + ℓrσ
−
τ · min
 ( √2
ℓ , r−
)
 · e
 ℓr−
2 − π
4 τ

≤
 ( rσ+2
−
τ +
 √2rσ
−
τ
 )
 · e
 ℓr−
2 − π
4 τ .

By (3.61), ( rσ+2
−
τ + (1 + √2)rσ
−
τ
 )
 ≤ τ σ
2 +1 + (1 + √2)τ σ
2
τ .

We conclude that
∣
∣
∣
∣

∫
C1 e
−u2/2e(δu)us−1du
∣
∣
∣
∣ ≤ τ σ
2 +1 + (1 + √2)τ σ
2
τ · e
− ℓr−
2 + π
4 τ

≤
 (
1 + 1 + √2
τ
 )
 τ σ
2 · e
−0.4798τ

when σ ∈ [0, 1); by (3.62), this is true for σ ≥ 1 as well.
Now let us examine the contribution of the last segment C3 of the contour.
Since C2 hits the x-axis at c0ℓ/c1, we deﬁne C3 to be the segment of the x-axis
going from x = c0ℓ/c1 till x = ∞. Then

(3.64)
 ∣
∣
∣
∣

∫
C3 e
−t2/2e(δt)ts dt
t
 ∣
∣
∣
∣ =
 ∣
∣
∣
∣
∣

∫ ∞

c0ℓ
c1 e
−x2/2e(δx)xs dx
x
 ∣
∣
∣
∣
∣ ≤ ∫ ∞

c0ℓ
c1 e
−x2/2xσ dx
x .

Now (
−e
−x2/2xσ−2)′ = e
−x2/2xσ−1 − (σ − 2)e
−x2/2xσ−3

(−e
−x2/2(xσ−2 + (σ − 2)xσ−4)
)′ = e
−x2/2xσ−1 − (σ − 2)(σ − 4)e
−x2/2xσ−5

and so on, implying that
∫ ∞

t e
−x2/2xσ dx
x

≤ e
−x2/2 ·
 




xσ−2 if 0 ≤ σ ≤ 2,
(xσ−2 + (σ − 2)xσ−4) if 2 ≤ σ ≤ 4.
xσ−2 + (σ − 2)xσ−4 + (σ − 2)(σ − 4)xσ−6 if 4 ≤ σ ≤ 6,

and so on. By (A.36), c0ℓ
c1 ≥ min ( τ
ℓ , 5
4 √τ ) .

We conclude that
∣
∣
∣
∣
∫

C3 e
−t2/2e(δt)ts dt
t
 ∣
∣
∣
∣ ≤ Pσ
 (min ( τ
ℓ , 5
4 √τ )) e
− min
( 1
2 ( τ
ℓ )
2, 25
32 τ ),

26 H. A. HELFGOTT

where we can set Pσ(x) = xσ−2 if σ ∈ [0, 2], Pσ(x) = xσ−2+(σ−2)xσ−4 if σ ∈ [2, 4]
and Pσ(x) = xσ−2 + (σ − 2)xσ−4 + . . . + (σ − 2k)xσ−2(k+1) if σ ∈ [2k, 2(k + 1)].

* * *

We have left the case ℓ < 0 for the very end. In this case, we can aﬀord to use
a straight ray from the origin as our contour of integration. Let C ′ be the ray at
angle π/4 − α from the origin, i.e., y = (tan(π/4 − α))x, x > 0, where α > 0 is
small. Write v = e(π/4−α)i. The integral to be estimated is

I = ∫

C′ e
−u2/2e(δu)us−1du.

Let us try α = 0 ﬁrst. Much as in (3.59) and (3.60), we obtain, for ℓ < 0,

(3.65)
 |I| ≤ ∫ ∞

0 e
−( −ℓt√2 + π
4 τ )tσ−1dt = e
− π
4 τ ∫ ∞

0 e
−|ℓ|t/
√
2tσ dt
t

= e
− π
4 τ ·
 ( √2
|ℓ|
 )σ ∫ ∞

0 e
−ttσ dt
t =
 ( √2
|ℓ|
 )σ Γ(σ) · e
− π
4 τ

for σ > 0. Recall that Γ(σ) ≤ σ−1 for 0 < σ < 1 (because σΓ(σ) = Γ(σ + 1) and
Γ(σ) ≤ 1 for all σ ∈ [1, 2]; the inequality Γ(σ) ≤ 1 for σ ∈ [1, 2] can in turn be
proven by Γ(1) = Γ(2) = 1, Γ′(1) < 0 < Γ′(2) and the convexity of Γ(σ)). We
see that, while (3.65) is very good in most cases, it poses problems when either
σ or ℓ is close to 0.
Let us ﬁrst deal with the issue of ℓ small. For general α and ℓ ≤ 0,

|I| ≤ ∫ ∞

0 e
−( t2
2 sin 2α−ℓt cos( π
4 −α)+( π
4 −α)τ )tσ−1dt

≤ e
−( π
4 −α)τ ∫ ∞

0 e
− t2
2 sin 2αtσ dt
t = e
−( π
4 −α)τ

(sin 2α)σ/2
 ∫ ∞

0 e
− t2
2 tσ dt
t

= e
−( π
4 −α)τ

(sin 2α)σ/2 · 2
σ/2−1 ∫ ∞

0 e
−yy σ
2 dy
y = eατ

2(sin 2α)σ/2 · 2
σ/2Γ(σ/2)e
− π
4 τ .

Here we can choose α = (arcsin 2/τ )/2 (for τ ≥ 2). Then 2α ≤ (π/2) · (2/τ ) =
π/τ , and so

(3.66) |I| ≤ e π
2τ ·τ

2(2/τ )σ/2 · 2
σ/2Γ(σ/2)e
− π
4 τ ≤ eπ/2

2 τ σ/2Γ(σ/2) · e
− π
4 τ .

The only issue that remains is that σ may be close to 0, in which case Γ(σ/2)
can be large. We can resolve this, as before, by doing an integration by parts. In
general, for −1 < σ < 1, s ̸= 0:

(3.67)
 |I| ≤ e
−u2/2e(δu) us

s |
v∞
0 − ∫

C′
 (
e
−u2/2e(δu)
)′ us

s du

= ∫

C′(u + ℓi)e
−u2/2−ℓiu us

s du

= 1
s
 ∫
C′ e
−u2/2e(δu)us+1du + ℓi
s
 ∫
C′ e
−u2/2e(δu)usdu.

MAJOR ARCS FOR GOLDBACH’S PROBLEM 27

Now we apply (3.65) with s + 1 and s + 2 instead of s, and get that

|I| = 1
|s|
 ( √2
|ℓ|
 )σ+2 Γ(σ + 2) · e
− π
4 τ + |ℓ|
|s|
 ( √2
|ℓ|
 )σ+1 Γ(σ + 1) · e
− π
4 τ

≤ 1
τ
 ( √2
|ℓ|
 )σ ( 4
ℓ2 + √2) e
− π
4 τ .

Alternatively, we may apply (3.66) and obtain

|I| ≤ 1
|s| eπ/2

2 Γ((σ + 2)/2) · τ (σ+2)/2e
− π
4 τ + |ℓ|
|s| eπ/2

2 Γ((σ + 1)/2) · τ (σ+1)/2e
− π
4 τ

≤ eπ/2τ σ/2

2
 (1 + √π|ℓ|
√τ
 ) e
− π
4 τ

for σ ∈ [0, 1], where we are using the facts that Γ(s) ≤ √
π for s ∈ [1/2, 1] and
Γ(s) ≤ 1 for s ∈ [1, 2].

3.9. Conclusion. Summing (3.56) with the bounds obtained in §3.8, we obtain
our ﬁnal estimate. Recall that we can reduce the case τ < 0 to the case τ > 0 by
reﬂection. This ﬁnishes the proof of Theorem 3.1. Let us now extract its main
corollary – in eﬀect, a simpliﬁed restatement of the theorem.

Proof of Corollary 3.2. Let E(ρ) be as in (3.2). Let

(3.68) L(ρ) =
 {
0.1598 if ρ ≥ 1.5,
0.1065ρ if ρ < 1.5.

Note that 0.1598 ≤ E(1.5), whereas 0.1065 ≤ E(1.5)/1.5. We claim that E(ρ) ≥
L(ρ): this is so for ρ ≥ 1.5 because E(ρ) is increasing on ρ, and for ρ ≤ 1.19
because of (3.79), and for ρ ∈ [1.19, 1.5] by the bisection method (with 20 itera-
tions).
By Thm. 3.1, for 0 ≤ k ≤ 2 and s = σ + iτ with σ ∈ [0, 1] and |τ | ≥
max(4π2|δ|, 100),
 |Fδ(s + k)| + |Fδ(k + 1 − s)|

is at most

(3.69) C0,τ,ℓ ·e
−E( |τ |
(πδ)2 )
·τ +C1,τ ·e
−0.4798τ +C2,τ,ℓ ·e
− min
( 1
8 ( τ
πδ )
2, 25
32 |τ |) +C ′
τ e
− π
4 |τ |,

where C0,τ,ℓ is at most

2 · (1 + 7.83
1−σ) ( 3/2
2π
 )1−σ ≤ 4.217 if k = 0,

2 · (1 + 1.63)
 

 min ( |τ |
|ℓ| , √|τ |
)

3/2
 

 ≤ 3.507 min ( |τ |
|ℓ| , √|τ |) if k = 1,

2 · (1 + 1.63
2) ·
 

 min ( |τ |
|ℓ| , √|τ |
)

3/2
 



2
 ≤ 3.251 min
 (( τ
|ℓ|
 )2 , |τ |

)
 if k = 2,

28 H. A. HELFGOTT

and where
(3.70)

C1,τ ≤
 (
1 + 1 + √2
|τ |
 )
 |τ | k+1
2 , C2,τ,ℓ ≤
 




min ( |τ |
|ℓ| , 5
4 √|τ |
)−1 if k = 0,

1 if k = 1,

min ( |τ |
|ℓ| , 5
4 √|τ |
) + 1 if k = 2,

C ′
τ,ℓ ≤ eπ/2|τ | k+1
2
2 ·
 



1 + √π|ℓ|√|τ | for k = 0,
√π for k = 1,
1 for k = 2.

(We deﬁne, as usual, ℓ = −2πδ.)
Since |τ | ≥ max(2π|ℓ|, 100),

(3.71)
 (
1 + 1 + √2
|τ |
 )
 + eπ/2

2 max
 (
1 + √π|ℓ|
√|τ | , √π
)
 · e
−( π
4 −0.4798)|τ |

≤ 1.0242 + 2.406 max
 (
1 + |τ |1/2

2
√π , √π
)
 e
−( π
4 −0.4798)|τ |

≤ 1.0242 + 9.194e
−( π
4 −0.4798)100 ≤ 1.025

and so

(3.72) C1,τ · e
−0.4798|τ | + C ′
τ e
− π
4 |τ | ≤ 1.025|τ | k+1
2 e
−0.4798|τ |.

Since |τ | ≥ 100 and tre−ct (r, c ≥ 0) is decreasing for t ≥ r/c,

(3.73) 1.025|τ |
(k+1)/2e
−0.4798|τ | ≤ 1.025 · 10
k+1 · e
−(0.4798−0.1598)·100e
−0.1598|τ |

≤ 1.3 · 10
−11 · e
−0.1598|τ |

for k ≤ 2.
Yet again by |τ | ≥ max(4π2|δ|, 100),

(3.74) e
− 1
8 ( τ
πδ )2 ≤ e
−0.0184( τ
πδ )
2 · e
−0.1066( τ
πδ )2 ≤ 0.055 · e
−0.1066( τ
πδ )
2,

e
− 25
32 τ ≤ 1.03 · 10
−27 · e
−0.1598|τ |.

We also get (starting from (3.70))

(3.75) 0.055 · C2,τ,ℓ

min (( τ
|ℓ| )k , |τ | k
2 ) ≤
 



0.055/ min(2π, 12.5) ≤ 0.0088 if k = 0,
0.055/2π ≤ 0.0088 if k = 1,
0.055((2π)−1 + (2π)−2) ≤ 0.0102 if k = 2.

It is easy to see from (3.68) that

e
−L( |τ |
(πδ)2 )·|τ | ≥ max (
e
−0.1066( τ
πδ )
2, e
−0.1598|τ |) ,

whether |τ |/(πδ)2 is greater than 1.5 or not. We conclude that (3.69) is at most

(4.217 + 0.0089)e
−L(|τ |/(πδ)2 )

if k = 0, at most
 (3.507 + 0.0089) min(|τ |/ℓ, √|τ |)e
−L(|τ |/(πδ)2)

MAJOR ARCS FOR GOLDBACH’S PROBLEM 29

if k = 1, and at most

(3.251 + 0.0103) min((|τ |/ℓ)
2, |τ |)e
−L(|τ |/(πδ)2)

if k = 2. (We see that the error terms coming from (3.73) and the second line
of (3.74) are being absorbed by the least signiﬁcant digits of the bound from
(3.75).) We simplify matters further by using min((|τ |/ℓ)2, |τ |) = (|τ |/|ℓ|)2 for
|τ | < 1.5(πδ)2, and bounding min((|τ |/ℓ)2, |τ |) ≤ |τ | for |τ | ≥ 1.5(πδ)2. □

Let us take a second look at Thm. 3.1. While, in the present paper, we will
use it only through Corollary 3.2, it seems worthwhile to say a few words more
on the behavior of its bounds.
The terms in (3.1) other than C0,τ,ℓ · e−E(|τ |/(πδ)2)|τ | are usually very small. In
practice, Thm. 3.1 should be applied when |τ |/2π|δ| is larger than a moderate
constant (say 8) and |τ | is larger than a somewhat larger constant (say 100). The
assumptions of Cor. 3.2 are thus typical.
For comparison, the Mellin transform of e−t2/2 (i.e., F0 = M f0) is 2s/2−1Γ(s/2),
which decays like e−(π/4)|τ |. For τ very small (e.g., |τ | < 2), it can make sense to
use the trivial bound

(3.76) |Fδ(s)| ≤ F0(σ) = ∫ ∞

0 e
−t2/2tσ dt
t = 2
σ/2−1Γ(σ/2) ≤ 2σ/2

σ

for σ ∈ (0, 1]. Alternatively, we could use integration by parts (much as in (3.67)),
followed by the trivial bound:

(3.77) Fδ(s) = − ∫ ∞

0
 (
e
−u2/2e(δu)
)′ us

s du = Fδ(s + 2)
s − 2πδi
s Fδ(s + 1),

and so

(3.78) |Fδ(s)| ≤ 2 σ+2
2 −1Γ ( σ+2
2 ) + 2 σ+1
2 −1|2πδ|Γ ( σ+1
2 )

|s| ≤ √ π
2 · 1 + 2π|δ|
|s|

for 0 ≤ σ ≤ 1, since 2xΓ(x) ≤ √
2π for x ∈ [1/2, 3/2].
In the proof of Corollary 3.2, we used a somewhat crude approximation to the
function E(ρ) deﬁned in (3.2). It is worthwhile to give some approximations to
E(ρ) that, while still simple, are a little better.

Lemma 3.3. Let E(ρ) and υ(ρ) be as in (3.2). Then

(3.79) E(ρ) ≥ 1
8 ρ − 5
384 ρ3

for all ρ > 0. We can also write

(3.80) E(ρ) = π
4 − β
2 − sin 2β
4(1 + sin β) ,

where β = arcsin 1/υ(ρ).

Clearly, (3.79) is useful for ρ small, whereas (3.80) is useful for ρ large (since
then β is close to 0). Taking derivatives, we see that (3.80) implies that E(ρ) is
decreasing on β; thus, E(ρ) is increasing on ρ. Note that (3.79) gives us that

(3.81) E ( |τ |
(πδ)2
 ) · |τ | ≥ 1
2
 ( τ
2πδ
 )2 ·
 (
1 − 5
48π4
 ( τ
|δ|2
 )2)
 .

30 H. A. HELFGOTT

Proof. Let α = arccos 1/υ(ρ). Then υ(ρ) = 1/(cos α), whereas

(3.82)
 √1 + ρ2 = 2υ2(ρ) − 1 = 2
cos2 α − 1,

ρ =
 √( 2
cos2 α − 1
)2 − 1 =
 √ 4
cos4 α − 4
cos2 α

= 2
√1 − cos2 α
cos2 α = 2 sin α
cos2 α .

Thus
(3.83)

2E(ρ) = α − 2 ( 1
cos α − 1
)

2 sin α
cos2 α = α − (1 − cos α) cos α
sin α = α − (1 − cos2 α) cos α
sin α(1 + cos α)

= α − sin α cos α
1 + cos α = α − sin 2α
4 cos2 α
2 .

By (A.37) and (3.82), this implies that

2E(ρ) ≥ ρ
4 − 5ρ3

24 · 8 ,

giving us (3.79).
To obtain (3.80), simply deﬁne β = π/2 − α; the desired inequality follows
from the last two steps of (3.83). □

4. Explicit formulas

An explicit formula is an expression restating a sum such as Sη,χ(δ/x, x) as a
sum of the Mellin transform Gδ(s) over the zeros of the L function L(s, χ). More
speciﬁcally, for us, Gδ(s) is the Mellin transform of η(t)e(δt) for some smoothing
function η and some δ ∈ R. We want a formula whose error terms are good both
for δ very close or equal to 0 and for δ farther away from 0. (Indeed, our choice(s)
of η will be made so that Fδ(s) decays rapidly in both cases.)
We will be able to base all of our work on a single, general explicit formula,
namely, Lemma 4.1. This explicit formula has simple error terms given purely in
terms of a few norms of the given smoothing function η. We also give a common
framework for estimating the contribution of zeros on the critical strip (Lemmas
4.3 and 4.4).
The ﬁrst example we work out is that of the Gaussian smoothing η(t) = e−t2/2.
We actually do this in part for didactic purposes and in part because of its
likely applicability elsewhere; for our applications, we will always use smoothing
functions based on te−t2/2 and t2e−t2/2, generally in combination with something
else. Since η(t) = e−t2/2 does not vanish at t = 0, its Mellin transform has a pole
at s = 0 – something that requires some additional work (Lemma 4.2; see also
the proof of Lemma 4.1).
Other than that, for each function η(t), all that has to be done is to bound
an integral (from Lemma 4.3) and bound a few norms. Still, both for η∗ and
for η+, we ﬁnd a few interesting complications. Since η+ is deﬁned in terms of
a truncation of a Mellin transform (or, alternatively, in terms of a multiplicative
convolution with a Dirichlet kernel, as in (1.3) and (1.5)), bounding the norms
of η+ and η′
+ takes a little work. We leave this to Appendix B. The eﬀect of

MAJOR ARCS FOR GOLDBACH’S PROBLEM 31

the convolution is then just to delay the decay a shift, in that a rapidly decaying
function f (τ ) will get replaced by f (τ − H), H a constant.
The smoothing function η∗ is deﬁned as a multiplicative convolution of t2e−t2/2

with something else. Given that we have an explicit formula for t2e−t2/2, we
obtain an explicit formula for η∗ by what amounts to just exchanging the order
of a sum and an integral; this is an idea valid in general (see (4.54)).

4.1. A general explicit formula. We will prove an explicit formula valid when-
ever the smoothing η and its derivative η′ satisfy rather mild assumptions – they
will be assumed to be L2-integrable and to have strips of deﬁnition containing
{s : 1/2 ≤ ℜ(s) ≤ 3/2}, though any strip of the form {s : ǫ ≤ ℜ(s) ≤ 1 + ǫ}
would do just as well.
(For explicit formulas with diﬀerent sets of assumptions, see, e.g., [IK04, §5.5]
and [MV07, Ch. 12].)
The main idea in deriving any explicit formula is to start with an expression
giving a sum as integral over a vertical line with an integrand involving a Mellin
transform (here, Gδ(s)) and an L-function (here, L(s, χ)). We then shift the line
of integration to the left. If stronger assumptions were made (as in Exercise 5 in
[IK04, §5.5]), we could shift the integral all the way to ℜ(s) = −∞; the integral
would then disappear, replaced entirely by a sum over zeros (or even, as in the
same Exercise 5, by a particularly simple integral). Another possibility is to shift
the line only to ℜ(s) = 1/2 + ǫ for some ǫ > 0 – but this gives a weaker result,
and at any rate the factor L′(s, χ)/L(s, χ) can be large and messy to estimate
within the critical strip 0 < ℜ(s) < 1.
Instead, we will shift the line to ℜs = −1/2. We can do this because the
assumptions on η and η′ are enough to continue Gδ(s) analytically up to there
(with a possible pole at s = 0). The factor L′(s, χ)/L(s, χ) is easy to estimate
for ℜs < 0 and s = 0 (by the functional equation), and the part of the integral
on ℜs = −1/2 coming from Gδ(s) can be estimated easily using the fact that the
Mellin transform is an isometry.

Lemma 4.1. Let η : R+
0 → R be in C 1. Let x ∈ R+, δ ∈ R. Let χ be a primitive
character mod q, q ≥ 1.
Write Gδ(s) for the Mellin transform of η(t)e(δt). Assume that η(t) and η′(t)
are in ℓ2 (with respect to the measure dt) and that η(t)tσ−1 and η′(t)tσ−1 are in
ℓ1 (again with respect to dt) for all σ in an open interval containing [1/2, 3/2].
Then

(4.1)
 ∞∑

n=1
Λ(n)χ(n)e ( δ
x n) η(n/x) = Iq=1 · ̂η(−δ)x − ∑

ρ Gδ(ρ)xρ

− R + O∗ (
(log q + 6.01) · (|η′|2 + 2π|δ||η|2)
) x−1/2,

where

(4.2) Iq=1 =
 {
1 if q = 1,
0 if q ̸= 1,

R = η(0) (log 2π
q + γ − L′(1, χ)
L(1, χ)
 ) + O∗(c0)

for q > 1, R = η(0) log 2π for q = 1 and

(4.3) c0 = 2
3 O∗ (∣
∣
∣
∣ η′(t)
√
t
 ∣
∣
∣
∣1 + ∣
∣
∣η′(t)
√t
∣
∣
∣1 + 2π|δ| (∣
∣
∣
∣ η(t)
√t
 ∣
∣
∣
∣1 + |η(t)
√t|1
)) .

32 H. A. HELFGOTT

The norms |η|2, |η′|2, |η′(t)/
√t|1, etc., are taken with respect to the usual measure
dt. The sum ∑ρ is a sum over all non-trivial zeros ρ of L(s, χ).

Proof. Since (a) η(t)tσ−1 is in ℓ1 for σ in an open interval containing 3/2 and (b)
η(t)e(δt) has bounded variation (since η, η′ ∈ ℓ1, implying that the derivative of
η(t)e(δt) is also in ℓ1), the Mellin inversion formula (as in, e.g., [IK04, 4.106])
holds:
 η(n/x)e(δn/x) = 1
2πi
 ∫ 3
2 +i∞

3
2 −i∞ Gδ(s)xsn−sds.

Since Gδ(s) is bounded for ℜ(s) = 3/2 (by η(t)t3/2−1 ∈ ℓ1) and ∑n Λ(n)n−3/2

is bounded as well, we can change the order of summation and integration as
follows:

(4.4)
 ∞∑

n=1 Λ(n)χ(n)e(δn/x)η(n/x) =
 ∞∑

n=1 Λ(n)χ(n) · 1
2πi
 ∫ 3
2 +i∞

3
2 −i∞ Gδ(s)xsn−sds

= 1
2πi
 ∫ 3
2 +i∞

3
2 −i∞
 ∞∑

n=1 Λ(n)χ(n)Gδ(s)xsn−sds

= 1
2πi
 ∫ 3
2 +i∞

3
2 −i∞ − L′(s, χ)
L(s, χ) Gδ(s)xsds.

(This is the way the procedure always starts: see, for instance, [HL23, Lemma
1] or, to look at a recent standard reference, [MV07, p. 144]. We are being very
scrupulous about integration because we are working with general η.)
The ﬁrst question we should ask ourselves is: up to where can we extend
Gδ(s)? Since η(t)tσ−1 is in ℓ1 for σ in an open interval I containing [1/2, 3/2],
the transform Gδ(s) is deﬁned for ℜ(s) in the same interval I. However, we
also know that the transformation rule M (tf ′(t))(s) = −s · M f (s) (see (2.6); by
integration by parts) is valid when s is in the holomorphy strip for both M (tf ′(t))
and M f . In our case (f (t) = η(t)e(δt)), this happens when ℜ(s) ∈ (I − 1) ∩ I (so
that both sides of the equation in the rule are deﬁned). Hence s · Gδ(s) (which
equals s · M f (s)) can be analytically continued to ℜ(s) in (I − 1) ∪ I, which is an
open interval containing [−1/2, 3/2]. This implies immediately that Gδ(s) can
be analytically continued to the same region, with a possible pole at s = 0.
When does Gδ(s) have a pole at s = 0? This happens when sGδ(s) is non-zero
at s = 0, i.e., when M (tf ′(t))(0) ̸= 0 for f (t) = η(t)e(δt). Now

M (tf ′(t))(0) = ∫ ∞

0 f ′(t)dt = lim
t→∞ f (t) − f (0).

We already know that f ′(t) = (d/dt)(η(t)e(δt)) is in ℓ1. Hence, limt→∞ f (t)
exists, and must be 0 because f is in ℓ1. Hence −M (tf ′(t))(0) = f (0) = η(0).
Let us look at the next term in the Laurent expansion of Gδ(s) at s = 0. It is

lim
s→0 sGδ(s) − η(0)
s = lim
s→0 −M (tf ′(t))(s) − f (0)
s = − lim
s→0 1
s
 ∫ ∞

0 f ′(t)(ts − 1)dt

= − ∫ ∞

0 f ′(t) lim
s→0 ts − 1
s dt = − ∫ ∞

0 f ′(t) log t dt.

Here we were able to exchange the limit and the integral because f ′(t)tσ is in ℓ1
for σ in a neighborhood of 0; in turn, this is true because f ′(t) = η′(t) + 2πiδη(t)
and η′(t)tσ and η(t)tσ are both in ℓ1 for σ in a neighborhood of 0. In fact, we will

MAJOR ARCS FOR GOLDBACH’S PROBLEM 33

use the easy bounds |η(t) log t| ≤ (2/3)(|η(t)t−1/2|1 + |η(t)t1/2|1), |η′(t) log t| ≤
(2/3)(|η′(t)t−1/2|1 + |η′(t)t1/2|1), resulting from the inequality

(4.5) 2
3
 (
t− 1
2 + t 1
2 ) ≤ | log t|,

valid for all t > 0.
We conclude that the Laurent expansion of Gδ(s) at s = 0 is

(4.6) Gδ(s) = η(0)
s + c0 + c1s + . . . ,

where c0 = O∗(|f ′(t) log t|1)

= 2
3 O∗ (∣
∣
∣
∣ η′(t)
√t
 ∣
∣
∣
∣
1 + ∣
∣
∣η′(t)
√t∣
∣
∣
1 + 2πδ (∣
∣
∣
∣ η(t)
√t
 ∣
∣
∣
∣1 + |η(t)
√t|1
)) .

We shift the line of integration in (4.4) to ℜ(s) = −1/2. We obtain

(4.7)
 1
2πi
 ∫ 2+i∞

2−i∞ − L′(s, χ)
L(s, χ) Gδ(s)xsds = Iq=1Gδ(1)x − ∑

ρ Gδ(ρ)xρ − R

− 1
2πi
 ∫ −1/2+i∞

−1/2−i∞
 L′(s, χ)
L(s, χ) Gδ(s)xsds,

where
 R = Ress=0 L′(s, χ)
L(s, χ) Gδ(s).

Of course,
 Gδ(1) = M (η(t)e(δt))(1) = ∫ ∞

0 η(t)e(δt)dt = ̂η(−δ).

Let us work out the Laurent expansion of L′(s, χ)/L(s, χ) at s = 0. By the
functional equation (as in, e.g., [IK04, Thm. 4.15]),

(4.8) L′(s, χ)
L(s, χ) = log π
q − 1
2 ψ ( s + κ
2
 ) − 1
2 ψ ( 1 − s + κ
2
 ) − L′(1 − s, χ)
L(1 − s, χ) ,

where ψ(s) = Γ′(s)/Γ(s) and

κ =
 {
0 if χ(−1) = 1
1 if χ(−1) = −1.

By ψ(1 − x) − ψ(x) = π cot πx (immediate from Γ(s)Γ(1 − s) = π/ sin πs) and
ψ(s) + ψ(s + 1/2) = 2(ψ(2s) − log 2) (Legendre; [AS64, (6.3.8)]),

(4.9) − 1
2
 (ψ ( s + κ
2
 ) + ψ ( 1 − s + κ
2
 )) = −ψ(1 − s) + log 2 + π
2 cot π(s + κ)
2 .

Hence, unless q = 1, the Laurent expansion of L′(s, χ)/L(s, χ) at s = 0 is

1 − κ
s + (log 2π
q − ψ(1) − L′(1, χ)
L(1, χ)
 ) + a1
s + a2
s2 + . . . .

Here ψ(1) = −γ, the Euler gamma constant [AS64, (6.3.2)].
There is a special case for q = 1 due to the pole of ζ(s) at s = 1. We know
that ζ ′(0)/ζ(0) = log 2π (see, e.g., [MV07, p. 331]).

34 H. A. HELFGOTT

From this and (4.6), we conclude that, if η(0) = 0, then

R =
 {
c0 if q > 1 and χ(−1) = 1,
0 otherwise,

where c0 = O∗(|η′(t) log t|1 + 2π|δ||η(t) log t|1). If η(0) ̸= 0, then

R = η(0) (log 2π
q + γ − L′(1, χ)
L(1, χ)
 ) +
 {
c0 if χ(−1) = 1
0 otherwise.

for q > 1, and R = η(0) log 2π
for q = 1.
It is time to estimate the integral on the right side of (4.7). For that, we will
need to estimate L′(s, χ)/L(s, χ) for ℜ(s) = −1/2 using (4.8) and (4.9).
If ℜ(z) = 3/2, then |t2 + z2| ≥ 9/4 for all real t. Hence, by [OLBC10, (5.9.15)]
and [GR00, (3.411.1)],

(4.10)
 ψ(z) = log z − 1
2z − 2 ∫ ∞

0
 tdt
(t2 + z2)(e2πt − 1)

= log z − 1
2z + 2 · O∗ (∫ ∞

0
 tdt
9
4 (e2πt − 1)
 )

= log z − 1
2z + 8
9 O∗ (∫ ∞

0
 tdt
e2πt − 1
 )

= log z − 1
2z + 8
9 · O∗ ( 1
(2π)2 Γ(2)ζ(2)
)

= log z − 1
2z + O∗ ( 1
27
 ) = log z + O∗ ( 10
27
 ) .

Thus, in particular, ψ(1 − s) = log(3/2 − iτ ) + O∗(10/27), where we write s =
1/2 + iτ . Now ∣
∣
∣
∣cot π(s + κ)
2
 ∣
∣
∣
∣ =
 ∣
∣
∣
∣
∣ e
∓ π
4 i− π
2 τ + e
± π
4 i+ π
2 τ

e
∓ π
4 i− π
2 τ − e
± π
4 i+ π
2 τ
 ∣
∣
∣
∣
∣ = 1.

Since ℜ(s) = −1/2, a comparison of Dirichlet series gives

(4.11) ∣
∣
∣
∣ L′(1 − s, χ)
L(1 − s, χ)
 ∣
∣
∣
∣ ≤ |ζ ′(3/2)|
|ζ(3/2)| ≤ 1.50524,

where ζ ′(3/2) and ζ(3/2) can be evaluated by Euler-Maclaurin. Therefore, (4.8)
and (4.9) give us that, for s = −1/2 + iτ ,

(4.12)
 ∣
∣
∣
∣ L′(s, χ)
L(s, χ)
 ∣
∣
∣
∣ ≤ ∣
∣
∣log q
π
 ∣
∣
∣ + log ∣
∣
∣
∣ 3
2 + iτ ∣
∣
∣
∣ + 10
27 + log 2 + π
2 + 1.50524

≤ ∣
∣
∣log q
π
 ∣
∣
∣ + 1
2 log (τ 2 + 9
4
 ) + 4.1396.

Recall that we must bound the integral on the right side of (4.7). The absolute
value of the integral is at most x−1/2 times

(4.13) 1
2π
 ∫ − 1
2 +i∞

− 1
2 −i∞
 ∣
∣
∣
∣ L′(s, χ)
L(s, χ) Gδ(s)
∣
∣
∣
∣ ds.

MAJOR ARCS FOR GOLDBACH’S PROBLEM 35

By Cauchy-Schwarz, this is at most
√
√
√
√ 1
2π
 ∫ − 1
2 +i∞

− 1
2 −i∞
 ∣
∣
∣
∣ L′(s, χ)
L(s, χ) · 1
s
 ∣
∣
∣
∣

2 |ds| ·
 √
√
√
√ 1
2π
 ∫ − 1
2 +i∞

− 1
2 −i∞ |Gδ(s)s|
2 |ds|

By (4.12),
√
√
√
√∫ − 1
2 +i∞

− 1
2 −i∞
 ∣
∣
∣
∣ L′(s, χ)
L(s, χ) · 1
s
 ∣
∣
∣
∣

2 |ds| ≤
 √
√
√
√∫ − 1
2 +i∞

− 1
2 −i∞
 ∣
∣
∣
∣ log q
s
 ∣
∣
∣
∣

2 |ds|

+
 √
√
√
√∫ ∞

−∞
 ∣
∣ 1
2 log (
τ 2 + 9
4 ) + 4.1396 + log π∣
∣2

1
4 + τ 2 dτ

≤ √2π log q + √226.844,

where we compute the last integral numerically.
4

Again, we use the fact that, by (2.6), sGδ(s) is the Mellin transform of

(4.14) − t d(e(δt)η(t))
dt = −2πiδte(δt)η(t) − te(δt)η′(t)

Hence, by Plancherel (as in (2.2)),
(4.15)√
√
√
√ 1
2π
 ∫ − 1
2 +i∞

− 1
2 −i∞ |Gδ(s)s|
2 |ds| =
 √∫ ∞

0 |−2πiδte(δt)η(t) − te(δt)η′(t)|2 t−2dt

= 2π|δ|

√∫ ∞

0 |η(t)|2dt +
 √∫ ∞

0 |η′(t)|2dt.

Thus, (4.13) is at most
(
log q +
 √ 226.844
2π
 )
 · (|η′|2 + 2π|δ||η|2) .
 □

Lemma 4.1 leaves us with three tasks: bounding the sum of Gδ(ρ)xρ over all
non-trivial zeroes ρ with small imaginary part, bounding the sum of Gδ(ρ)xρ over
all non-trivial zeroes ρ with large imaginary part, and bounding L′(1, χ)/L(1, χ).
Let us start with the last task: while, in a narrow sense, it is optional – in
that, in most of our applications, we will have η(0) = 0, thus making the term
L′(1, χ)/L(1, χ) disappear – it is also very easy and can be dealt with quickly.
Since we will be using a ﬁnite GRH check in all later applications, we might
as well use it here.

Lemma 4.2. Let χ be a primitive character mod q, q > 1. Assume that all
non-trivial zeroes ρ = σ + it of L(s, χ) with |t| ≤ 5/8 satisfy ℜ(ρ) = 1/2. Then
∣
∣
∣
∣ L′(1, χ)
L(1, χ)
 ∣
∣
∣
∣ ≤ 5
2 log M (q) + c,

4By a rigorous integration from τ = −100000 to τ = 100000 using VNODE-LP [Ned06],
which runs on the PROFIL/BIAS interval arithmetic package[Kn¨u99].

36 H. A. HELFGOTT

where M (q) = maxn ∣
∣
∣
∑m≤n χ(m)
∣
∣
∣ and

c = 5 log 2
√3
ζ(9/4)/ζ(9/8) = 15.07016 . . . .

Proof. By a lemma of Landau’s (see, e.g., [MV07, Lemma 6.3], where the con-
stants are easily made explicit) based on the Borel-Carath´eodory Lemma (as in
[MV07, Lemma 6.2]), any function f analytic and zero-free on a disc Cs0,R = {s :
|s − s0| ≤ R} of radius R > 0 around s0 satisﬁes

(4.16) f ′(s)
f (s) = O∗ ( 2R log M/|f (s0)|
(R − r)2
 )

for all s with |s − s0| ≤ r, where 0 < r < R and M is the maximum of |f (z)|
on Cs0,R. Assuming L(s, χ) has no non-trivial zeros oﬀ the critical line with
|ℑ(s)| ≤ H, where H > 1/2, we set s0 = 1/2 + H, r = H − 1/2, and let R → H −.
We obtain

(4.17) L′(1, χ)
L(1, χ) = O∗ (8H log maxs∈Cs0,H |L(s, χ)|

|L(s0, χ)|
 ) .

Now
 |L(s0, χ)| ≥ ∏

p (1 + p−s0)
−1 = ∏

p
 (1 − p−2s0)−1

(1 − p−s0)−1 = ζ(2s0)
ζ(s0) .

Since s0 = 1/2 + H, Cs0,H is contained in {s ∈ C : ℜ(s) > 1/2} for any value of
H. We choose (somewhat arbitrarily) H = 5/8.
By partial summation, for s = σ + it with 1/2 ≤ σ < 1 and any N ∈ Z+,

(4.18)
 L(s, χ) = ∑

n≤N χ(m)n−s −
 

 ∑

m≤N χ(m)



 (N + 1)
−s

+ ∑

n≥N +1
 

 ∑

m≤n χ(m)



 (n−s − (n + 1)
−s+1)

= O∗ ( N 1−1/2

1 − 1/2 + N 1−σ + M (q)N −σ)
 ,

where M (q) = maxn ∣
∣
∣
∑m≤n χ(m)
∣
∣
∣. We set N = M (q)/3, and obtain

(4.19) |L(s, χ)| ≤ 2M (q)N −1/2 = 2
√3√M (q).

We put this into (4.17) and are done. □

Let M (q) be as in the statement of Lem. 4.2. Since the sum of χ(n) (χ mod q,
q > 1) over any interval of length q is 0, it is easy to see that M (q) ≤ q/2. We
also have the following explicit version of the P´olya-Vinogradov inequality:

(4.20) M (q) ≤
 { 2
π2 √q log q + 4
π2 √
q log log q + 3
2 √
q if χ(−1) = 1,
1
2π √
q log q + 1
π √
q log log q + √
q if χ(−1) = 1.

Taken together with M (q) ≤ q/2, this implies that

(4.21) M (q) ≤ q4/5

MAJOR ARCS FOR GOLDBACH’S PROBLEM 37

for all q ≥ 1, and also that

(4.22) M (q) ≤ 2q3/5

for all q ≥ 1.
Notice, lastly, that ∣
∣
∣
∣log 2π
q + γ∣
∣
∣
∣ ≤ log q + log eγ · 2π
32

for all q ≥ 3. (There are no primitive characters modulo 2, so we can omit q = 2.)
We conclude that, for χ primitive and non-trivial,
∣
∣
∣
∣log 2π
q + γ − L′(1, χ)
L(1, χ)
 ∣
∣
∣
∣ ≤ log eγ · 2π
32 + log q + 5
2 log q 4
5 + 15.07017

≤ 3 log q + 15.289.

Obviously, 15.289 is more than log 2π, the bound for χ trivial. Hence, the absolute
value of the quantity R in the statement of Lemma 4.1 is at most

(4.23) |η(0)|(3 log q + 15.289) + |c0|

for all primitive χ.
It now remains to bound the sum ∑ρ Gδ(ρ)xρ in (4.1). Clearly
∣
∣
∣
∣
∣

∑

ρ Gδ(ρ)xρ∣
∣
∣
∣
∣ ≤ ∑

ρ |Gδ(ρ)| · xℜ(ρ).

Recall that these are sums over the non-trivial zeros ρ of L(s, χ).
We ﬁrst prove a general lemma on sums of values of functions on the non-trivial
zeros of L(s, χ). This is little more than partial summation, given a (classical)
bound for the number of zeroes N (T, χ) of L(s, χ) with |ℑ(s)| ≤ T . The error
term becomes particularly simple if f is real-valued and decreasing; the statement
is then practically identical to that of [Leh66, Lemma 1] (for χ principal), except
for the fact that the error term is improved here.

Lemma 4.3. Let f : R+ → C be piecewise C 1. Assume limt→∞ f (t)t log t = 0.
Let χ be a primitive character mod q, q ≥ 1; let ρ denote the non-trivial zeros
ρ of L(s, χ). Then, for any y ≥ 1,

(4.24)
 ∑

ρ non-trivial
ℑ(ρ)>y
 f (ℑ(ρ)) = 1
2π
 ∫ ∞

y f (T ) log qT
2π dT

+ 1
2 O∗ (|f (y)|gχ(y) + ∫ ∞

y
 ∣
∣f ′(T )
∣
∣ · gχ(T )dT ) ,

where

(4.25) gχ(T ) = 0.5 log qT + 17.7

If f is real-valued and decreasing on [y, ∞), the second line of (4.24) equals

O∗ ( 1
4
 ∫ ∞

y
 f (T )
T dT ) .

38 H. A. HELFGOTT

Proof. Write N (T, χ) for the number of non-trivial zeros of L(s, χ) with |ℑ(s)| ≤
T . Write N +(T, χ) for the number of (necessarily non-trivial) zeros of L(s, χ)
with 0 < ℑ(s) ≤ T . Then, for any f : R+ → C with f piecewise diﬀerentiable
and limt→∞ f (t)N (T, χ) = 0,
∑

ρ:ℑ(ρ)>y f (ℑ(ρ)) = ∫ ∞

y f (T ) dN +(T, χ)

= − ∫ ∞

y f ′(T )(N +(T, χ) − N +(y, χ))dT

= − 1
2
 ∫ ∞

y f ′(T )(N (T, χ) − N (y, χ))dT.

Now, by [Ros41, Thms. 17–19] and [McC84, Thm. 2.1] (see also [Tru, Thm. 1]),

(4.26) N (T, χ) = T
π log qT
2πe + O∗ (gχ(T ))

for T ≥ 1, where gχ(T ) is as in (4.25). (This is a classical formula; the references
serve to prove the explicit form (4.25) for the error term gχ(T ).)
Thus, for y ≥ 1,

(4.27)
 ∑

ρ:ℑ(ρ)>y f (ℑ(ρ)) = − 1
2
 ∫ ∞

y f ′(T ) ( T
π log qT
2πe − y
π log qy
2πe
 ) dT

+ 1
2 O∗ (|f (y)|gχ(y) + ∫ ∞

y
 ∣
∣f ′(T )
∣
∣ · gχ(T )dT ) .

Here

(4.28) − 1
2
 ∫ ∞

y f ′(T ) ( T
π log qT
2πe − y
π log qy
2πe
 ) dT = 1
2π
 ∫ ∞

y f (T ) log qT
2π dT.

If f is real-valued and decreasing (and so, by limt→∞ f (t) = 0, non-negative),

|f (y)|gχ(y) + ∫ ∞

y
 ∣
∣f ′(T )
∣
∣ · gχ(T )dT = f (y)gχ(y) − ∫ ∞

y f ′(T )gχ(T )dT

= 0.5 ∫ ∞

y
 f (T )
T dT,

since g′
χ(T ) ≤ 0.5/T for all T ≥ T0. □

Now we can bound the sum ∑ρ Gδ(ρ)xρ. The bound we will give is pro-
portional to √T0 log qT0, whereas a more obvious approach would give a bound
proportional to T0 log qT0. This (large) improvement is due to our usage of isom-
etry (after an application of Cauchy-Schwarz) to bound integrals throughout. It
is also this usage that allows us to give a general bound depending only on a few
norms of η and its variants.

Lemma 4.4. Let η : R+
0 → R be such that both η(t) and (log t)η(t) lie in L1 ∩ L2
and η(t)/
√t lies in L1 (with respect to dt). Let δ ∈ R. Let Gδ(s) be the Mellin
transform of η(t)e(δt).
Let χ be a primitive character mod q, q ≥ 1. Let T0 ≥ 1. Assume that all
non-trivial zeros ρ of L(s, χ) with |ℑ(ρ)| ≤ T0 lie on the critical line. Then
∑

ρ non-trivial
|ℑ(ρ)|≤T0
 |Gδ(ρ)|

MAJOR ARCS FOR GOLDBACH’S PROBLEM 39

is at most

(4.29) (|η|2 + |η · log |2)
√T0 log qT0 + (17.21|η · log |2 − (log 2π√e)|η|2)
√T0

+ ∣
∣
∣η(t)/
√t∣
∣
∣
1 · (1.32 log q + 34.5)

Proof. For s = 1/2 + iτ , we have the trivial bound

(4.30) |Gδ(s)| ≤ ∫ ∞

0 |η(t)|t1/2 dt
t = ∣
∣
∣η(t)/
√t∣
∣
∣
1 ,

where Fδ is as in (4.44). We also have the trivial bound
(4.31)

|G
′
δ(s)| = ∣
∣
∣
∣

∫ ∞

0 (log t)η(t)ts dt
t
 ∣
∣
∣
∣ ≤ ∫ ∞

0 |(log t)η(t)|tσ dt
t = ∣
∣(log t)η(t)tσ−1∣
∣1

for s = σ + iτ .
Let us start by bounding the contribution of very low-lying zeros (|ℑ(ρ)| ≤ 1).
By (4.26) and (4.25),

N (1, χ) = 1
π log q
2πe + O∗ (0.5 log q + 17.7) = O∗(0.819 log q + 16.8).

Therefore, ∑

ρ non-trivial
|ℑ(ρ)|≤1
 |Gδ(ρ)| ≤ ∣
∣
∣η(t)t−1/2∣
∣
∣1 · (0.819 log q + 16.8).

Let us now consider zeros ρ with |ℑ(ρ)| > 1. Apply Lemma 4.3 with y = 1 and

f (t) =
 {
|Gδ(1/2 + it)| if t ≤ T0,
0 if t > T0.

This gives us that

(4.32)
 ∑

ρ:1<|ℑ(ρ)|≤T0 f (ℑ(ρ)) = 1
π
 ∫ T0

1 f (T ) log qT
2π dT

+ O∗ (|f (1)|gχ(1) + ∫ ∞

1 |f ′(T )| · gχ(T ) dT ) ,

where we are using the fact that f (σ + iτ ) = f (σ − iτ ) (because η is real-valued).
By Cauchy-Schwarz,

1
π
 ∫ T0

1 f (T ) log qT
2π dT ≤
 √ 1
π
 ∫ T0

1 |f (T )|2dT ·
 √ 1
π
 ∫ T0

1
 (log qT
2π
 )2 dT .

Now
1
π
 ∫ T0

1 |f (T )|
2dT ≤ 1
2π
 ∫ ∞

−∞
 ∣
∣
∣
∣Gδ
 ( 1
2 + iT )∣
∣
∣
∣

2 dT ≤ ∫ ∞

0 |e(δt)η(t)|
2dt = |η|
2
2

by Plancherel (as in (2.2)). We also have
∫ T0

1
 (log qT
2π
 )2 dT ≤ 2π
q
 ∫ qT0
2π

0 (log t)
2dt ≤
 ((log qT0
2πe
 )2 + 1

)
 · T0.

Hence 1
π
 ∫ T0

1 f (T ) log qT
2π dT ≤
 √(log qT0
2πe
 )2 + 1 · |η|2√T0.

40 H. A. HELFGOTT

Again by Cauchy-Schwarz,

∫ ∞

1 |f ′(T )| · gχ(T ) dT ≤
 √ 1
2π
 ∫ ∞

−∞ |f ′(T )|2dT ·
 √ 1
π
 ∫ T0

1 |gχ(T )|2dT .

Since |f ′(T )| = |G′
δ(1/2 + iT )| and (M η)′(s) is the Mellin transform of log(t) ·
e(δt)η(t) (by (2.6)),
 1
2π
 ∫ ∞

−∞ |f ′(T )|
2dT = |η(t) log(t)|2.

Much as before,
∫ T0

1 |gχ(T )|
2dT ≤ ∫ T0

0 (0.5 log qT + 17.7)
2dT

= (0.25(log qT0)
2 + 17.2(log qT0) + 296.09)T0.

Summing, we obtain

1
π
 ∫ T0

1 f (T ) log qT
2π dT + ∫ ∞

1 |f ′(T )| · gχ(T ) dT

≤ ((log qT0
2πe + 1
2
 ) |η|2 + (log qT0
2 + 17.21
) |η(t)(log t)|2
) √T0

Finally, by (4.30) and (4.25),

|f (1)|gχ(1) ≤ ∣
∣
∣η(t)/
√t∣
∣
∣
1 · (0.5 log q + 17.7).

By (4.32) and the assumption that all non-trivial zeros with |ℑ(ρ)| ≤ T0 lie on
the line ℜ(s) = 1/2, we conclude that
∑

ρ non-trivial
1<|ℑ(ρ)|≤T0
 |Gδ(ρ)| ≤ (|η|2 + |η · log |2)
√T0 log qT0

+ (17.21|η · log |2 − (log 2π√e)|η|2)
√T0

+ ∣
∣
∣η(t)/
√t∣
∣
∣1 · (0.5 log q + 17.7).
 □

4.2. Sums and decay for the Gaussian: η♥(t) = e−t2/2. It is now time to
derive our bounds for the Gaussian smoothing. Thanks to the general work we
have done so far, there is really only one thing left to do, namely, an estimate for
the sum ∑ρ |Fδ(ρ)| over non-trivial zeros with |ℑ(ρ)| > T0.

Lemma 4.5. Let η♥(t) = e−t2/2. Let x ∈ R+, δ ∈ R. Let χ be a primitive
character mod q, q ≥ 1. Assume that all non-trivial zeros ρ of L(s, χ) with
|ℑ(ρ)| ≤ T0 satisfy ℜ(s) = 1/2. Assume that T0 ≥ max(4π2|δ|, 100).
Write Fδ(s) for the Mellin transform of η(t)e(δt). Then

∑

ρ non-trivial
|ℑ(ρ)|>T0
 |Fδ(ρ)| ≤ log qT0
2π · (4.329e
−0.1598T0 + 0.802|δ|e
−0.1065
( T0
π|δ|
 )2) .

MAJOR ARCS FOR GOLDBACH’S PROBLEM 41

Here we have preferred to give a bound with a simple form. It is probably
feasible to derive from Theorem 3.1 a bound essentially proportional to e−E(ρ)T0,
where ρ = T0/(πδ)2 and E(ρ) is as in (3.2). (As we discussed in §3.9, E(ρ)
behaves as e−(π/4)T0 for ρ large and as e−0.125(T0/(πδ))2 for ρ small.)

Proof. First of all,
∑

ρ non-trivial
|ℑ(ρ)|>T0
 |Fδ(ρ)| = ∑

ρ non-trivial
ℑ(ρ)>T0
 (|Fδ(ρ)| + |Fδ(1 − ρ)|) ,

by the functional equation (which implies that non-trivial zeros come in pairs ρ,
1 − ρ). Hence, by Cor. 3.2,

(4.33) ∑

ρ non-trivial
|ℑ(ρ)|>T0
 |Fδ(ρ)| ≤ ∑

ρ non-trivial
ℑ(ρ)>T0
 f (ℑ(ρ)),

where

(4.34) f (τ ) = 4.226 ·
 {
e
−0.1065( τ
πδ )
2 if |τ | < 3
2 (πδ)2,
e−0.1598|τ | if |τ | ≥ 3
2 (πδ)2.

It is easy to check that f (τ ) is a decreasing function of τ for τ ≥ T0.
We now apply Lemma 4.3. We obtain that

(4.35) ∑

ρ non-trivial
ℑ(ρ)>T0
 f (ℑ(ρ)) ≤ ∫ ∞

T0 f (T ) ( 1
2π log qT
2π + 1
4T
 ) dT.

We just need to estimate some integrals. For any y ≥ 1, c, c1 > 0,
∫ ∞

y
 (log t + c1
t
 ) e
−ctdt ≤ ∫ ∞

y
 (log t − 1
ct
 ) e
−ctdt + ( 1
c + c1
) ∫ ∞

y
 e−ct

t dt

= (log y)e−cy

c + ( 1
c + c1
) E1(cy),

where E1(x) = ∫ ∞
x e−tdt/t. Clearly, E1(x) ≤ ∫ ∞
x e−tdt/x = e−x/x. Hence
∫ ∞

y
 (
log t + c1
t
 ) e
−ctdt ≤ (log y + ( 1
c + c1
) 1
y
 ) e−cy

c .

We conclude that
∫ ∞

T0 e
−0.1598t ( 1
2π log qt
2π + 1
4t
 ) dt

≤ 1
2π
 ∫ ∞

T0
 (log t + π/2
t
 ) e
−ctdt + log q
2π
2πc
 ∫ ∞

T0 e
−ctdt

= 1
2πc
 (log T0 + log q
2π + ( 1
c + π
2
 ) 1
T0
 ) e
−cT0

with c = 0.1598. Since T0 ≥ 100, this is at most

(4.36) 1.0242 log qT0
2π e
−cT0.

42 H. A. HELFGOTT

Now let us deal with the Gaussian term. (It appears only if T0 < (3/2)(πδ)2,
as otherwise |τ | ≥ (3/2)(πδ)2 holds whenever |τ | ≥ T0.) For any y ≥ e, c ≥ 0,

(4.37) ∫ ∞

y e
−ct2dt = 1
√
c
 ∫ ∞

√cy e
−t2 dt ≤ 1
cy
 ∫ ∞

√cy te
−t2dt ≤ e−cy2

2cy ,

(4.38) ∫ ∞

y
 e−ct2

t dt = ∫ ∞

cy2 e−t

2t dt = E1(cy2)
2 ≤ e−cy2

2cy2 ,

(4.39) ∫ ∞

y (log t)e
−ct2 dt ≤ ∫ ∞

y
 (log t + log t − 1
2ct2
 ) e
−ct2dt = log y
2cy e
−cy2.

Hence

(4.40)
 ∫ ∞

T0 e
−0.1065( T
πδ )2 ( 1
2π log qT
2π + 1
4T
 ) dT

= ∫ ∞

T0
π|δ| e
−0.1065t2 ( |δ|
2 log q|δ|t
2 + 1
4t
 ) dt

≤
 



 |δ|
2 log T0
π|δ|
2c T0
π|δ| +
 |δ|
2 log q|δ|
2
2c T0
π|δ| + 1

8c ( T0
π|δ| )2
 


 e
−c( T0
π|δ| )2

with c = 0.1065. Since T0 ≥ 100 and q ≥ 1,

2π
8T0 ≤ π
400 ≤ 0.0057 · 1
2 log qT0
2π

Thus, the last line of (4.40) is less than

(4.41) 1.0057
 |δ|
2 log qT0
2π
2cT0
π|δ| e
−c( T0
π|δ| )2 = 1.0057 πδ2

4cT0 e
−c( T0
π|δ| )2.

Again by T0 ≥ 4π2|δ|, we see that 1.0057π|δ|/(4cT0 ) ≤ 1.0057/(16cπ) ≤ 0.18787.
To obtain our ﬁnal bound, we simply sum (4.36) and (4.41), and multiply by
4.266 (the constant in (4.34)). We conclude that the integral in (4.35) is at most

(4.329e
−0.1598T0 + 0.8015|δ|e
−0.1065
( T0
π|δ| )2) log qT0
2π .
 □

We need to record a few norms related to the Gaussian η♥(t) = e−t2/2 before
we proceed. Recall we are working with the one-sided Gaussian, i.e., we set

MAJOR ARCS FOR GOLDBACH’S PROBLEM 43

η♥(t) = 0 for t < 0. Symbolic integration then gives
(4.42)
 |η♥|
2
2 = ∫ ∞

0 e
−t2dt = √
π
2 ,

|η′
♥|
2
2 = ∫ ∞

0 (te
−t2/2)
2dt = √π
4 ,

|η♥ · log |
2
2 = ∫ ∞

0 e
−t2(log t)
2dt

= √π
16 (π2 + 2γ2 + 8γ log 2 + 8(log 2)
2) ≤ 1.94753,

|η♥(t)/
√t|1 = ∫ ∞

0
 e−t2/2
√t dt = Γ(1/4)
23/4 ≤ 2.15581

|η′
♥(t)/
√t| = |η♥(t)
√t|1 = ∫ ∞

0 e
− t2
2 √tdt = Γ(3/4)
21/4 ≤ 1.03045

∣
∣
∣η′
♥(t)t1/2∣
∣
∣1 = ∣
∣
∣η♥(t)t3/2∣
∣
∣
1 = ∫ ∞

0 e
− t2
2 t 3
2 dt = 1.07791.

We can now state what is really our main result for the Gaussian smoothing.
(The version in the introduction will, as we shall later see, follow from this, given
numerical inputs.)

Proposition 4.6. Let η(t) = e−t2/2. Let x ≥ 1, δ ∈ R. Let χ be a primitive
character mod q, q ≥ 1. Assume that all non-trivial zeros ρ of L(s, χ) with
|ℑ(ρ)| ≤ T0 lie on the critical line. Assume that T0 ≥ max(4π2|δ|, 100).
Then
(4.43)
∞∑

n=1 Λ(n)χ(n)e ( δ
x n) η ( n
x
 ) =
 {̂η(−δ)x + O∗ (errη,χ(δ, x)) · x if q = 1,
O∗ (errη,χ(δ, x)) · x if q > 1,

where

errη,χ(δ, x) = log qT0
2π · (4.329e
−0.1598T0 + 0.802|δ|e
−0.1065
( T0
π|δ| )2)

+ (2.337
√T0 log qT0 + 21.817
√T0 + 2.85 log q + 74.38)x− 1
2

+ (3 log q + 14|δ| + 17)x−1 + (log q + 6) · (1 + 5|δ|) · x−3/2.

Proof. Let Fδ(s) be the Mellin transform of η♥(t)e(δt). By Lemmas 4.4 (with
Gδ = Fδ) and 4.5, ∣
∣
∣
∣
∣
∣
 ∑

ρ non-trivial Fδ(ρ)xρ
∣
∣
∣
∣
∣
∣

is at most (4.29) (with η = η♥) times √x, plus

log qT0
2π · (4.329e
−0.1598T0 + 0.802|δ|e
−0.1065
( T0
π|δ| )2) · x.

By the norm computations in (4.42), we see that (4.29) is at most

2.337
√T0 log qT0 + 21.817
√T0 + 2.85 log q + 74.38.

44 H. A. HELFGOTT

Let us now apply Lemma 4.1. We saw that the value of R in Lemma 4.1 is
bounded by (4.23). We know that η♥(0) = 1. Again by (4.42), we get from (4.3)
that c0 ≤ 1.4056 + 13.3466|δ|. Hence

|R| ≤ 3 log q + 13.347|δ| + 16.695.

Lastly, |η′
♥|2 + 2π|δ||η♥|2 ≤ 0.942 + 4.183|δ| ≤ 1 + 5|δ|.

Clearly (6.01 − 6) · (1 + 5|δ|) + 13.347|δ| + 16.695 < 14|δ| + 17,

and so we are done. □

4.3. The case of η(t) = t2e−t2/2 and η∗(t). We will now work with a weight
based on the Gaussian:
 η(t) =
 {t2e−t2/2 if t ≥ 0,
0 if t < 0.

The fact that this vanishes at t = 0 actually makes it easier to work with at
several levels.
Its Mellin transform is just a shift of that of the Gaussian. Write

(4.44) Fδ(s) = (M (e
− t2
2 e(δt)))(s),

Gδ(s) = (M (η(t)e(δt)))(s).

Then, by the deﬁnition of the Mellin transform,

Gδ(s) = Fδ(s + 2).

We start by bounding the contribution of zeros with large imaginary part, just
as before.

Lemma 4.7. Let η(t) = t2e−t2/2. Let x ∈ R+, δ ∈ R. Let χ be a primitive
character mod q, q ≥ 1. Assume that all non-trivial zeros ρ of L(s, χ) with
|ℑ(ρ)| ≤ T0 satisfy ℜ(s) = 1/2. Assume that T0 ≥ max(4π2|δ|, 100).
Write Gδ(s) for the Mellin transform of η(t)e(δt). Then

∑

ρ non-trivial
|ℑ(ρ)|>T0
 |Gδ(ρ)| ≤ T0 log qT0
2π ·
 (
3.5e
−0.1598T0 + 0.64e
−0.1065· T 2
0
(πδ)2 )
 .

Proof. We start by writing
∑

ρ non-trivial
|ℑ(ρ)|>T0
 |Gδ(ρ)| = ∑

ρ non-trivial
ℑ(ρ)>T0
 (|Fδ(ρ + 2)| + |Fδ((1 − ρ) + 2)|) ,

where we are using Gδ(ρ) = Fδ(ρ + 2) and the fact that non-trivial zeros come in
pairs ρ, 1 − ρ.
By Cor. 3.2 with k = 2,
∑

ρ non-trivial
|ℑ(ρ)|>T0
 |Gδ(ρ)| ≤ ∑

ρ non-trivial
ℑ(ρ)>T0
 f (ℑ(ρ)),

MAJOR ARCS FOR GOLDBACH’S PROBLEM 45

where

(4.45) f (τ ) = c2 ·
 



|τ |e−0.1598|τ | + 1
4 ( |τ |
πδ )2 e
−0.1065
( |τ |
πδ )2 if |τ | < 3
2 (πδ)2,

|τ |e−0.1598|τ | if |τ | ≥ 3
2 (πδ)2,

where c2 = 3.262. We are including the term c2|τ |e−0.1598|τ | in both cases in part
because we will not bother to take it out (just as we did not bother in the proof
of Lem. 4.5) and in part to ensure that f (τ ) is a decreasing function of τ for
τ ≥ T0.
We can now apply Lemma 4.3. We obtain, again,

(4.46) ∑

ρ non-trivial
ℑ(ρ)>T0
 f (ℑ(ρ)) ≤ ∫ ∞

T0 f (T ) ( 1
2π log qT
2π + 1
4T
 ) dT.

Just as before, we will need to estimate some integrals.
For any y ≥ 1, c, c1 > 0,
∫ ∞

y te
−ctdt = ( y
c + 1
c2
 ) e
−cy,

∫ ∞

y
 (
t log t + c1
t
 ) e
−ctdt ≤ ∫ ∞

y
 ((t + a − 1
c
 ) log t − 1
c − a
c2t
 ) e
−ctdt

= ( y
c + a
c2
 ) e
−cy log y,

where
 a =
 log y
c + 1
c + c1
y
log y
c − 1
c2y .

Setting c = 0.1598, c1 = π/2, y = T0 ≥ 100, we obtain that
∫ ∞

T0
 ( 1
2π log qT
2π + 1
4T
 ) T e
−0.1598T dT

≤ 1
2π
 (log q
2π · ( T0
c + 1
c2
 ) + (T0
c + a
c2
 ) log T0
) e
−0.1598T0

and
 a =
 log T0
0.1598 + 1
0.1598 + π/2
T0
log T0
0.1598 − 1
0.15982T0 ≤ 1.235.

Multiplying by c2 = 3.262 and simplifying by the assumption T0 ≥ 100, we obtain
that

(4.47) ∫ ∞

T0 3.255T e
−0.1598T ( 1
2π log qT0
2π + 1
4T
 ) dT ≤ 3.5T0 log qT0
2π · e
−0.1598T0 .

Now let us examine the Gaussian term. First of all – when does it arise? If
T0 ≥ (3/2)(πδ)2, then |τ | ≥ (3/2)(πδ)2 holds whenever |τ | ≥ T0, and so (4.45)
does not give us a Gaussian term. Recall that T0 ≥ 4π2|δ|, which means that
|δ| ≤ 8/3 implies that T0 ≥ (3/2)(πδ)2. We can thus assume from now on that
|δ| > 8/3, since otherwise there is no Gaussian term to treat.
For any y ≥ 1, c, c1 > 0,
∫ ∞

y t2e
−ct2dt < ∫ ∞

y
 (t2 + 1
4c2t2
 ) e
−ct2dt = ( y
2c + 1
4c2y
 ) · e
−cy2,

46 H. A. HELFGOTT
∫ ∞

y (t2 log t + c1t) · e
−ct2dt ≤ ∫ ∞

y
 (t2 log t + at log et
2c − log et
2c − a
4c2t
 ) e
−ct2dt

= (2cy + a) log y + a
4c2 · e
−cy2,

where
 a = c1y + log ey
2c
y log ey
2c − 1
4c2y = 1
y + c1y + 1
4c2y2

y log ey
2c − 1
4c2y .

(Note that a decreases as y ≥ 1 increases.) Setting c = 0.1065, c1 = 1/(2|δ|) ≤
3/16 and y = T0/(π|δ|) ≥ 4π, we obtain
∫ ∞

T0
π|δ|
 ( 1
2π log q|δ|t
2 + 1
4π|δ|t
 ) t2e
−0.1065t2 dt

≤ ( 1
2π log q|δ|
2
 ) · ( T0
2πc|δ| + 1
4c2 · 4π
 ) · e
−0.1065
( T0
π|δ|
 )2

+ 1
2π ·
 (
2c T0
π|δ| + a
) log T0
π|δ| + a

4c2 · e
−0.1065
( T0
π|δ|
 )2

and
 a ≤ 1
4π + 4π · 3
16 + 1
4·0.10652·(4π)2

4π log 4πe
2·0.1065 − 1
4·0.10652·4π ≤ 0.092.

Multiplying by (c2/4)π|δ|, we get that

(4.48) ∫ ∞

T0
 c2
4
 ( T
π|δ|
 )2 e
−0.1065
( T
π|δ|
 )2 ( 1
2π log qT0
2π + 1
4T
 ) dT

is at most e
−0.1065
( T0
π|δ| )2 times

(4.49)
 ((0.61T0 + 0.716|δ|) · log q|δ|
2 + 0.61T0 log T0
π|δ| + 0.827|δ| log eT0
π|δ|
 )

≤
 (
0.61 + 0.828 · 1 + 1
log T0/π|δ|
T0/|δ|
 )
 T0 log qT0
2π ≤ 0.64T0 log qT0
2π ,

where we are using several times the assumption that T0 ≥ 4π2|δ|.
We sum (4.47) and the estimate for (4.48) we have just got to reach our con-
clusion. □

Again, we record some norms obtained by symbolic integration:
(4.50)
 |η|
2
2 = 3
8 √π, |η′|
2
2 = 7
16 √
π,

|η · log |
2
2 = √π
64 (
8(3γ − 8) log 2 + 3π2 + 6γ2 + 24(log 2)
2 + 16 − 32γ)

≤ 0.16364,

|η(t)/
√t|1 = 21/4Γ(1/4)
4 ≤ 1.07791, |η(t)
√t|1 = 3
4 2
3/4Γ(3/4) ≤ 1.54568,

|η′(t)/
√t|1 = ∫ √2

0 t3/2e
− t2
2 dt − ∫ ∞

√2 t3/2e
− t2
2 dt ≤ 1.48469,

|η′(t)
√t|1 ≤ 1.72169.

MAJOR ARCS FOR GOLDBACH’S PROBLEM 47

Proposition 4.8. Let η(t) = t2e−t2/2. Let x ≥ 1, δ ∈ R. Let χ be a primitive
character mod q, q ≥ 1. Assume that all non-trivial zeros ρ of L(s, χ) with
|ℑ(ρ)| ≤ T0 lie on the critical line. Assume that T0 ≥ max(4π2|δ|, 100).
Then
(4.51)
∞∑

n=1 Λ(n)χ(n)e ( δ
x n) η(n/x) =
 {̂η(−δ)x + O∗ (errη,χ(δ, x)) · x if q = 1,
O∗ (errη,χ(δ, x)) · x if q > 1,

where
(4.52)

errη,χ(δ, x) = T0 log qT0
2π ·
 (
3.5e
−0.1598T0 + 0.64e
−0.1065· T 2
0
(πδ)2 )

+ (
1.22
√T0 log qT0 + 5.053
√T0 + 1.423 log q + 37.19
) · x−1/2

+ (3 + 11|δ|)x−1 + (log q + 6) · (1 + 6|δ|) · x−3/2.

Proof. We proceed as in the proof of Prop. 4.6. The contribution of Lemma 4.7
is
 T0 log qT0
2π ·
 (
3.5e
−0.1598T0 + 0.64e
−0.1065· T 2
0
(πδ)2 )
 · x,

whereas the contribution of Lemma 4.4 is at most

(1.22
√T0 log qT0 + 5.053
√T0 + 1.423 log q + 37.188)
√x.

Let us now apply Lemma 4.1. Since η(0) = 0, we have

R = O∗(c0) = O∗(2.138 + 10.99|δ|).

Lastly, |η′|2 + 2π|δ||η|2 ≤ 0.881 + 5.123|δ|. □

Now that we have Prop. 4.8, we can derive from it similar bounds for a smooth-
ing deﬁned as the multiplicative convolution of η with something else. In general,
for ϕ1, ϕ2 : [0, ∞) → C, if we know how to bound sums of the form

(4.53) Sf,ϕ1(x) = ∑

n f (n)ϕ1(n/x),

we can bound sums of the form Sf,ϕ1∗M ϕ2, simply by changing the order of sum-
mation and integration:

(4.54)
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

This is particularly nice if ϕ2(t) vanishes in a neighbourhood of the origin, since
then the argument wx of Sf,ϕ1(wx) is always large.
We will use ϕ1(t) = t2e−t2/2, ϕ2(t) = η1 ∗M η1, where η1 is 2 times the char-
acteristic function of the interval [1/2, 1]. This is the example that will be used
in [Helc]. The motivation for the choice of ϕ1 and ϕ2 is clear: we have just got
bounds based on ϕ1(t) in the major arcs, and the minor-arc bounds in [Helb]
(used in [Helc], not here) were obtained for the weight ϕ2(t).

48 H. A. HELFGOTT

Corollary 4.9. Let η(t) = t2e−t2/2, η1 = 2 · I[1/2,1], η2 = η1 ∗M η1. Let η∗ =
η2 ∗M η. Let x ∈ R+, δ ∈ R. Let χ be a primitive character mod q, q ≥ 1.
Assume that all non-trivial zeros ρ of L(s, χ) with |ℑ(ρ)| ≤ T0 lie on the critical
line. Assume that T0 ≥ max(4π2|δ|, 100).
Then
(4.55)
∞∑

n=1 Λ(n)χ(n)e ( δ
x n) η∗(n/x) =
 { ̂η∗(−δ)x + O∗ (errη∗,χ(δ, x)) · x if q = 1,
O∗ (errη∗,χ(δ, x)) · x if q > 1,

where
(4.56)

errη,χ∗(δ, x) = T0 log qT0
2π ·
 (
3.5e
−0.1598T0 + 0.0019 · e
−0.1065· T 2
0
(πδ)2 )

+ (
1.675
√T0 log qT0 + 6.936
√T0 + 1.954 log q + 51.047
) · x− 1
2

+ (6 + 22|δ|)x−1 + (log q + 6) · (3 + 17|δ|) · x−3/2.

Proof. The left side of (4.55) equals
∫ ∞

0
 ∞∑

n=1 Λ(n)χ(n)e ( δn
x
 ) η ( n
wx
 ) η2(w) dw
w

= ∫ 1

1
4
 ∞∑

n=1 Λ(n)χ(n)e ( δwn
wx
 ) η ( n
wx
 ) η2(w) dw
w ,

since η2 is supported on [−1/4, 1]. By Prop. 4.8, the main term (if q = 1)
contributes
∫ 1

1
4 ̂η(−δw)xw · η2(w) dw
w = x ∫ ∞

0 ̂η(−δw)η2(w)dw

= x ∫ ∞

0
 ∫ ∞

−∞ η(t)e(δwt)dt · η2(w)dw = x ∫ ∞

0
 ∫ ∞

−∞ η ( r
w
 ) e(δr) dt
w η2(w)dw

= x ∫ ∞

−∞
 (∫ ∞

0 η ( r
w
 ) η2(w) dw
w
 ) e(δr)dr = ̂η∗(−δ) · x.

The error term is

(4.57) ∫ 1

1
4 errη,χ(δw, wx) · wx · η2(w) dw
w = x · ∫ 1

1
4 errη,χ(δw, wx)η2(w)dw.

Since ∫
w η2(w)dw = 1, ∫

w w−1/2η2(w)dw ≤ 1.37259,
∫
w w−1η2(w)dw = 4(log 2)
2 ≤ 1.92182, ∫
w w−3/2η2(w)dw ≤ 2.74517

and5 ∫
w e
−0.1065·(4π)2( 1
w2 −1
)η2(w)dw ≤ 0.002866,

we see that (4.52) and (4.57) imply (4.56). □

5By rigorous integration from 1/4 to 1/2 and from 1/2 to 1 using VNODE-LP [Ned06].

MAJOR ARCS FOR GOLDBACH’S PROBLEM 49

4.4. The case of η+(t). We will work with

(4.58) η(t) = η+(t) = hH (t)tη♥(t) = hH (t)te
−t2/2,

where hH is as in (1.5). We recall that hH is a band-limited approximation to
the function h deﬁned in (1.4) – to be more precise, M hH (it) is the truncation
of M h(it) to the interval [−H, H].
We are actually deﬁning h, hH and η in a slightly diﬀerent way from what was
done in the ﬁrst draft of the present paper. The diﬀerence is instructive. There,
η(t) was deﬁned as hH (t)e−t2/2, and hH was a band-limited approximation to a
function h deﬁned as in (1.4), but with t3(2 − t)3 instead of t2(2 − t)3. The reason
for our new deﬁnitions is that now the truncation of M h(it) will not break the
holomorphy of M η, and so we will be able to prove the general results we proved
in §4.1.
In essence, M h will still be holomorphic because the Mellin transform of tη♥(t)
is holomorphic in the domain we care about, unlike the Mellin transform of η♥(t),
which does have a pole at s = 0.
As usual, we start by bounding the contribution of zeros with large imagi-
nary part. The procedure is much as before: since η+(t) = ηH(t)η♥(t) , the
Mellin transform M η+ is a convolution of M (te−t2/2) and something of support
in [−H, H]i, namely, M ηH restricted to the imaginary axis. This means that the
decay of M η+ is (at worst) like the decay of M (te−t2/2), delayed by H.

Lemma 4.10. Let η = η+ be as in (4.58) for some H ≥ 5. Let x ∈ R+, δ ∈ R.
Let χ be a primitive character mod q, q ≥ 1. Assume that all non-trivial zeros ρ
of L(s, χ) with |ℑ(ρ)| ≤ T0 satisfy ℜ(s) = 1/2, where T0 ≥ H + max(4π2|δ|, 100).
Write Gδ(s) for the Mellin transform of η(t)e(δt). Then

∑

ρ non-trivial
|ℑ(ρ)|>T0
 |Gδ(ρ)| ≤
 

9.462
√T ′
0e
−0.1598T ′
0 + 11.287|δ|e
−0.1065
( T ′
0
πδ
 )2

 log qT0
2π ,

where T ′
0 = T0 − H.

Proof. As usual,∑

ρ non-trivial
|ℑ(ρ)|>T0
 |Gδ(ρ)| = ∑

ρ non-trivial
ℑ(ρ)>T0
 (|Gδ(ρ)| + |Gδ(1 − ρ)|) .

Let Fδ be as in (4.44). Then, since η+(t)e(δt) = hH (t)te−t2/2e(δt), where hH is
as in (1.5), we see by (2.5) that

Gδ(s) = 1
2π
 ∫ H

−H M h(ir)Fδ(s + 1 − ir)dr,

and so, since |M h(ir)| = |M h(−ir)|,
(4.59)

|Gδ(ρ)| + |Gδ(1 − ρ)| ≤ 1
2π
 ∫ H

−H |M h(ir)|(|Fδ (1 + ρ − ir)| + |Fδ(2 − (ρ − ir))|)dr.

We apply Cor. 3.2 with k = 1 and T0 − H instead of T0, and obtain that
|Fδ(ρ)| + |Fδ(1 − ρ)| ≤ g(τ ), where

(4.60) g(τ ) = c1 · (√|τ |e
−0.1598|τ | + |τ |
2π|δ| · e
−0.1065( τ
πδ )
2)

50 H. A. HELFGOTT

where c1 = 3.516. (As in the proof of Lemma 4.7, we are really putting in extra
terms so as to simplify our integrals.)
From (4.59), we conclude that

|Gδ(ρ)| + |Gδ(1 − ρ)| ≤ f (τ ),

for ρ = σ + iτ , τ > 0, where

f (τ ) = |M h(ir)|1
2π · g(τ − H)

is decreasing for τ ≥ T0 (because g(τ ) is decreasing for τ ≥ T0 − H). By (B.17),
|M h(ir)|1 ≤ 16.193918.
We apply Lemma 4.3, and get that

(4.61)
 ∑

ρ non-trivial
|ℑ(ρ)|>T0
 |Gδ(ρ)| ≤ ∫ ∞

T0 f (T ) ( 1
2π log qT
2π + 1
4T
 ) dT

= |M h(ir)|1
2π
 ∫ ∞

T0 g(T − H) ( 1
2π log qT
2π + 1
4T
 ) dT.

Now we just need to estimate some integrals. For any y ≥ e2, c > 0 and
κ, κ1 ≥ 0, ∫ ∞

y
 √te
−ctdt ≤ ( √y
c + 1
2c2√y
 ) e
−cy,

∫ ∞

y
 (√t log(t + κ) + κ1√
t
 ) e
−ctdt ≤ ( √y
c + a
c2√y
 ) log(y + κ)e
−cy,

where
 a = 1
2 + 1 + cκ1
log(y + κ) .

The contribution of the exponential term in (4.60) to (4.61) thus equals

(4.62)
 c1|M h(ir)|1
2π
 ∫ ∞

T0
 ( 1
2π log qT
2π + 1
4T
 ) √T − H · e
−0.1598(T −H)dT

≤ 9.06194 ∫ ∞

T0−H
 ( 1
2π log(T + H) + log q
2π
2π + 1
4T
 ) √T e
−0.1598T dT

≤ 9.06194
2π
 ( √
T0 − H
0.1598 + a
0.15982√T0 − H
 ) log qT0
2π · e
−0.1598(T0−H),

where a = 1/2 + (1 + 0.1598π/2)/ log T0. Since T0 − H ≥ 100 and T0 ≥ 105, this
is at most
 9.4612
√T0 − H log qT0
2π · e
−0.1598(T0−H).

We now estimate a few more integrals so that we can handle the Gaussian
term in (4.60). For any y > 1, c > 0, κ, κ1 ≥ 0,
∫ ∞

y te
−ct2dt = e−cy2

2c ,

∫ ∞

y (t log(t + κ) + κ1)e
−ct2 dt ≤
 (
1 + κ1 + 1
2cy
y log(y + κ)
 ) log(y + κ) · e−cy2

2c

MAJOR ARCS FOR GOLDBACH’S PROBLEM 51

Proceeding just as before, we see that the contribution of the Gaussian term in
(4.60) to (4.61) is at most
(4.63)
c1|M h(ir)|1
2π
 ∫ ∞

T0
 ( 1
2π log qT
2π + 1
4T
 ) T − H
2π|δ| · e
−0.1065( T −H
πδ )2dT

≤ 9.06194 · |δ|
4
 ∫ ∞

T0−H
π|δ|
 (log (T + H
π|δ|
 ) + log q|δ|
2 + π/2
T
 ) T e
−0.1065T 2dT

≤ 9.06194 · |δ|
8 · 0.1065
 

1 +
 π
2 + π|δ|
2·0.1065·(T0−H)
T0−H
π|δ| log T0
π|δ|
 

 log qT0
2π · e
−0.1065
( T0−H
πδ
 )2,

Since (T0 − H)/(π|δ|) ≥ 4π, this is at most

11.287|δ| log qT0
2π · e
−0.1065
( T0−H
πδ
 )2.
 □

Proposition 4.11. Let η = η+ be as in (4.58) for some H ≥ 50. Let x ≥ 103,
δ ∈ R. Let χ be a primitive character mod q, q ≥ 1. Assume that all non-
trivial zeros ρ of L(s, χ) with |ℑ(ρ)| ≤ T0 lie on the critical line, where T0 ≥
H + max(4π2|δ|, 100).
Then
(4.64)
∞∑

n=1 Λ(n)χ(n)e ( δ
x n) η+(n/x) =
 {̂η+(−δ)x + O∗ (
errη+,χ(δ, x)
) · x if q = 1,
O∗ (errη+,χ(δ, x)
) · x if q > 1,

where
(4.65)

errη+,χ(δ, x) =
 

9.462
√T ′
0 · e
−0.1598T ′
0 + 11.287|δ|e
−0.1065
( T ′
0
πδ
 )2

 log qT0
2π

+ (1.631
√T0 log qT0 + 12.42
√T0 + 1.321 log q + 34.51)x−1/2,

+ (9 + 11|δ|)x−1 + (log q)(11 + 6|δ|)x−3/2,

where T ′
0 = T0 − H.

Proof. We can apply Lemmas 4.1 and Lemma 4.4 because η+(t), (log t)η+(t) and
η′
+(t) are in ℓ2 (by (B.25), (B.28) and (B.32)) and η+(t)tσ−1 and η′
+(t)tσ−1 are in
ℓ1 for σ in an open interval containing [1/2, 3/2] (by (B.30) and (B.33)). (Because
of (4.5), the fact that η+(t)t−1/2 and η+(t)t1/2 are in ℓ1 implies that η+(t) log t is
also in ℓ1, as is required by Lemma 4.4.)
We apply Lemmas 4.1, 4.4 and 4.10. We bound the norms involving η+ using
the estimates in §B.3 and §B.4. Since η+(0) = 0 (by the deﬁnition (B.3) of η+),
the term R in (4.2) is at most c0, where c0 is as in (4.3). We bound

c0 ≤ 2
3
 (
2.922875 (√Γ(1/2) + √Γ(3/2)) + 1.062319 (√Γ(5/2) + √Γ(7/2)))

+ 4π
3 |δ| · 1.062319 (√Γ(3/2) + √Γ(5/2)) ≤ 6.536232 + 9.319578|δ|

using (B.30) and (B.33). By (B.25), (B.32) and the assumption H ≥ 50,

|η+|2 ≤ 0.80044, |η′
+|2 ≤ 10.845789.

52 H. A. HELFGOTT

Thus, the error terms in (4.1) total at most

(4.66) 6.536232+9.319578|δ| + (log q + 6.01)(10.845789 + 2π · 0.80044|δ|)x−1/2

≤ 9 + 11|δ| + (log q)(11 + 6|δ|)x−1/2.

The part of the sum ∑ρ Gδ(ρ)xρ in (4.1) corresponding to zeros ρ with |ℑ(ρ)| >
T0 gets estimated by Lem 4.10. By Lemma 4.4, the part of the sum corresponding
to zeros ρ with |ℑ(ρ)| ≤ T0 is at most

(1.631
√T0 log qT0 + 12.42
√T0 + 1.321 log q + 34.51)x1/2,

where we estimate the norms |η+|2, |η · log |2 and |η(t)/
√t|1 by (B.25), (B.28)
and (B.30). □

4.5. A sum for η+(t)2. Using a smoothing function sometimes leads to consid-
ering sums involving the square of the smoothing function. In particular, [Hela]
requires a result involving η2
+ – something that could be slightly challenging to
prove, given the way in which η+ is deﬁned. Fortunately, we have bounds on
|η+|∞ and other ℓ∞-norms (see Appendix B.5). Our task will also be made easier
by the fact that we do not have a phase e(δn/x) this time. All in all, this will be
yet another demonstration of the generality of the framework developed in §4.1.

Proposition 4.12. Let η = η+ be as in (4.58), H ≥ 50. Let x ≥ 108. Assume
that all non-trivial zeros ρ of the Riemann zeta function ζ(s) with |ℑ(ρ)| ≤ T0 lie
on the critical line, where T0 ≥ 2H + max(H/4, 50).
Then

(4.67)
 ∞∑

n=1 Λ(n)(log n)η2
+(n/x) = x · ∫ ∞

0 η2
+(t) log xt dt + O∗(errℓ2,η+) · x log x,

where

(4.68) errℓ2,η+ = (0.607 (log T0)2

log x + 1.21(log T0)
) √T0e
− π(T0 −2H)
4

+ (2.06
√T0 log T0 + 43.87) · x−1/2

Proof. We will need to consider two smoothing functions, namely, η+,0(t) =
η+(t)2 and η+,1 = η+(t)2 log t. Clearly,

∞∑

n=1 Λ(n)(log n)η2
+(n/x) = (log x)
 ∞∑

n=1 Λ(n)η+,0(n/x) +
 ∞∑

n=1 Λ(n)η+,1(n/x).

Since η+(t) = hH (t)te−t2/2,

η+,0(r) = h
2
H(t)te
−t2 , η+,1(r) = h
2
H (t)(log t)te
−t2 .

Let η+,2 = (log x)η+,0 + η+,1 = η2
+(t) log xt.
We wish to apply Lemma 4.1. For this, we must ﬁrst check that some norms
are ﬁnite. Clearly,

η+,2(t) = η2
+(t) log x + η2
+(t) log t

η′
+,2(t) = 2η+(t)η′
+(t) log x + 2η+(t)η′
+(t) log t + η2
+(t)/t.

Thus, we see that η+,2(t) is in ℓ2 because η+(t) is in ℓ2 and η+(t), η+(t) log t are
both in ℓ∞ (see (B.25), (B.38), (B.40)):

(4.69) |η+,2(t)|2 ≤ ∣
∣η2
+(t)
∣
∣2 log x + ∣
∣η2
+(t) log t∣
∣
2
≤ |η+|∞ |η+|2 log x + |η+(t) log t|∞ |η+|2 .

MAJOR ARCS FOR GOLDBACH’S PROBLEM 53

Similarly, η′
+,2(t) is in ℓ2 because η+(t) is in ℓ2, η′
+(t) is in ℓ2 (B.32), and η+(t),
η+(t) log t and η+(t)/t (see (B.41)) are all in ℓ∞:
(4.70)∣
∣η′
+,2(t)
∣
∣2 ≤ ∣
∣2η+(t)η′
+(t)
∣
∣2 log x + ∣
∣2η+(t)η′
+(t) log t∣
∣2 + ∣
∣η2
+(t)/t∣
∣2
≤ 2 |η+|∞ ∣
∣η′
+∣
∣2 log x + 2 |η+(t) log t|∞ ∣
∣η′
+∣
∣
2 + |η+(t)/t|∞ |η+|2 .

In the same way, we see that η+,2(t)tσ−1 is in ℓ1 for all σ in (−1, ∞) (because
the same is true of η+(t)tσ−1 (B.30), and η+(t), η+(t) log t are both in ℓ∞) and
η′
+,2(t)tσ−1 is in ℓ1 for all σ in (0, ∞) (because the same is true of η+(t)tσ−1 and
η′
+(t)tσ−1 (B.33), and η+(t), η+(t) log t, η+(t)/t are all in ℓ∞).
We now apply Lemma 4.1 with q = 1, δ = 0. Since η+,2(0) = 0, the residue
term R equals c0, which, in turn, is at most 2/3 times

(|η+|∞ log x + |η+(t) log t|∞) (∣
∣
∣η+(t)/
√t∣
∣
∣
1 + ∣
∣
∣η+(t)
√t∣
∣
∣
1
)

+ 2 (|η+|∞ log x + |η+(t) log t|∞) (∣
∣
∣η′
+(t)/
√t∣
∣
∣
1 + ∣
∣
∣η′
+(t)
√t∣
∣
∣
1
)

+ |η+(t)/t|∞ (∣
∣
∣η+(t)/
√t∣
∣
∣
1 + ∣
∣
∣η+(t)
√t
∣
∣
∣1
) .

Using the bounds (B.38), (B.40), (B.41) (with the assumption H ≥ 50), (B.30)
and (B.33), we get that this means that

c0 ≤ 18.15014 log x + 7.84532.

Since q = 1 and δ = 0, we get from (4.70) that

(log q + 6.01)· (∣
∣η′
+,2∣
∣
2 + 2π|δ| |η+,2|2) x−1/2

= 6.01 ∣
∣η′
+,2∣
∣
2 x−1/2 ≤ (162.56 log x + 59.325)x−1/2.

Using the assumption x ≥ 108, we obtain

(4.71) c0 + (162.56 log x + 59.325)x−1/2 ≤ 18.593 log x.

We now apply Lemma 4.4 – as we may, because of the ﬁniteness of the norms
we have already checked, together with
(4.72)
|η+,2(t) log t|2 ≤ ∣
∣η2
+(t) log t∣
∣
2 log x + ∣
∣η2
+(t)(log t)
2∣
∣
2
≤ |η+(t) log t|∞ (|η+(t)|2 log x + |η+(t) log t|2)

≤ 0.40742 · (0.80044 log x + 0.82999) ≤ 0.32396 log x + 0.33592

(by (B.40), (B.25) and (B.28); use the assumption H ≥ 50). We will also need
the bounds

(4.73) |η+,2(t)|2 ≤ 0.99811 log x + 0.32612

(from (4.69), by the norm bounds (B.38), (B.40) and (B.25), all with H ≥ 50)
and

(4.74)
 ∣
∣
∣η+,2(t)/
√t
∣
∣
∣1 ≤ (|η+(t)|∞ log x + |η+(t) log t|∞) ∣
∣
∣η+(t)/
√t
∣
∣
∣1
≤ 1.24703 log x + 0.40745

(by (B.38), (B.40) (again with H ≥ 50) and (B.30)). We obtain that the sum∑ρ |G0(ρ)|xρ (where G0(ρ) = M η+,2(ρ)) over all non-trivial zeros ρ with |ℑ(ρ)| ≤

54 H. A. HELFGOTT

T0 is at most x1/2 times

(4.75) (1.3221 log x + 0.6621)
√T0 log T0 + (3.2419 log x + 5.0188)
√T0
+ 43.1 log x + 14.1,

where we are bounding norms by (4.73), (4.72) and (4.74). (We are using the fact
that T0 ≥ 2π√e to ensure that the quantity √T0 log T0 − (log 2π√e)
√T0 being
multiplied by |η+,2|2 is positive; thus, an upper bound for |η+,2|2 suﬃces.) By
the assumptions x ≥ 108, T0 ≥ 150, (4.75) is at most

2.06 log x · √T0 log T0 + 43.866 log x.

Note that the term 18.539 log x from (4.71) is at most 0.002x1/2 log x.
It remains to bound the sum of M η+,2(ρ) over non-trivial zeros with |ℑ(ρ)| >
T0. This we will do, as usual, by Lemma 4.3. For that, we will need to bound
M η+,2(ρ) for ρ in the critical strip.
The Mellin transform of e−t2 is Γ(s/2)/2, and so the Mellin transform of te−t2

is Γ((s + 1)/2)/2. By (2.6), this implies that the Mellin transform of (log t)te−t2

is Γ′((s + 1)/2)/4. Hence, by (2.5),

(4.76) M η+,2(s) = 1
4π
 ∫ ∞

−∞ M (h
2
H )(ir) · Fx (s − ir) dr,

where

(4.77) Fx(s) = (log x)Γ ( s + 1
2
 ) + 1
2 Γ′ ( s + 1
2
 ) .

Moreover,

(4.78) M (h
2
H )(ir) = 1
2π
 ∫ ∞

−∞ M hH(iu)M hH (i(r − u)) du,

and so M (h2
H )(ir) is supported on [−2H, 2H]. We also see that |M h2
H (ir)|1 ≤
|M hH (ir)|2
1/2π. We know that |M hH (ir)|2
1/2π ≤ 41.73727 by (B.17).
Hence

(4.79) |M η+,2(s)| ≤ 1
4π
 ∫ ∞

−∞ |M (h
2
H )(ir)|dr · max
|r|≤2H |Fx(s − ir)|

≤ 41.73727
4π · max
|r|≤2H |Fx(s − ir)| ≤ 3.32135 · max
|r|≤2H |Fx(s − ir)|.

By [OLBC10, 5.6.9] (Stirling with explicit constants),

(4.80) |Γ(s)| ≤ √2π|s|
ℜ(s)−1/2e
−π|ℑ(s)|/2e
1/6|z|,

and so

(4.81) |Γ(s)| ≤ 2.526
√|ℑ(s)|e
−π|ℑ(s)|/2

for s ∈ C with 0 < ℜ(s) ≤ 1 and |ℑ(s)| ≥ 25. Moreover, by [OLBC10, 5.11.2]
and the remarks at the beginning of [OLBC10, 5.11(ii)],

Γ′(s)
Γ(s) = log s − 1
2s + O∗ ( 1
12|s|2 · 1
cos3 θ/2
 )

MAJOR ARCS FOR GOLDBACH’S PROBLEM 55

for | arg(s)| < θ (θ ∈ (−π, π)). Again, for s = σ + iτ with 0 < σ ≤ 1 and |τ | ≥ 25,
this gives us

Γ′(s)
Γ(s) = log |τ | + log
 √|τ |2 + 1
|τ | + O∗ ( 1
2|τ |
 ) + O∗ ( 1
12|τ |2 · 1

cos3 π−arctan |τ |
2
 )

= log |τ | + O∗ ( 1
2|τ |2 + 1
2|τ |
 ) + O∗(0.236)
|τ |2

= log |τ | + O∗ ( 0.53
|τ |
 ) .

Hence, for −1 ≤ ℜ(s) ≤ 1 and |ℑ(s)| ≥ 50,

(4.82) |Fx(s)| ≤ ((log x) + 1
2 log ∣
∣
∣ τ
2
 ∣
∣
∣ + 1
2 O∗ ( 0.53
|τ /2|
 )) Γ (s + 1
2
 )

≤ 2.526((log x) + 1
2 log |τ | − 0.335)
√|τ |e
−π|τ |/2.

Thus, by (4.79), for ρ = σ + iτ with |τ | ≥ T0 ≥ 2H + 50 and −1 ≤ σ ≤ 1,

|M η+,2(ρ)| ≤ f (τ )

where

(4.83) f (T ) = 8.39 (log x + 1
2 log T ) √ |τ |
2 − H · e
− π(|τ |−2H)
4 .

The functions t ↦→ √
te−πt/2 and t ↦→ (log t)
√te−πt/2 are decreasing for t ≥ 3/π;
setting t = T /2 − H, we see that the right side of (4.83) is a decreasing function
of T for T ≥ T0, since T0/2 − H ≥ 25 > 3/π.
We can now apply Lemma 4.3, and get that

(4.84) ∑

ρ non-trivial
|ℑ(ρ)|>T0
 |M η+,2(ρ)| ≤ ∫ ∞

T0 f (T ) ( 1
2π log T
2π + 1
4T
 ) dT.

Since T ≥ T0 ≥ 150 > 2, we know that ((1/2π) log(T /2π)+1/4T ) ≤ (1/2π) log T .
Hence, the right side of (4.84) is at most

(4.85) 8.39
2π
 ∫ ∞

T0
 ((log x)(log T ) + (log T )2

2
 ) √ T
2 e
− π(T −2H)
4 dT.

In general, for T0 ≥ e2,

∫ ∞

T0
 √T (log T )
2e
−πT /4dT ≤ 4
π
 (√T0(log T0)
2 + 2/π
√T0 (log e
2T0)
2) e
− πT0
4 ,
∫ ∞

T0
 √
T (log T )e
−πT /4dT ≤ 4
π
 (√T0(log T0) + 2/π
√
T0 log e
2T0
) e
− πT0
4 ;

56 H. A. HELFGOTT

for T0 ≥ 150, the quantities on the right are at most 1.284
√T0(log T0)2e−πT0/4

and 1.281
√T0(log T0)e−πT0/4, respectively. Thus, (4.84) and (4.85) give us that
∑

ρ non-trivial
|ℑ(ρ)|>T0
 |M η+,2(ρ)|

≤ 8.39
2π · √2
 ( 1.284
2 (log T0)
2 + 1.281(log x)(log T0)
) √T0e
− π(T0 −2H)
4

≤ (0.607(log T0)
2 + 1.21(log x)(log T0))
√T0e
− π(T0−2H)
4 .
 □

4.6. A veriﬁcation of zeros and its consequences. David Platt veriﬁed in
his doctoral thesis [Pla11], that, for every primitive character χ of conductor
q ≤ 105, all the non-trivial zeroes of L(s, χ) with imaginary part ≤ 108/q lie on
the critical line, i.e., have real part exactly 1/2. (We call this a GRH veriﬁcation
up to 108/q.)
In work undertaken in coordination with the present project [Plab], Platt has
extended these computations to

• all odd q ≤ 3 · 105, with Tq = 108/q,
• all even q ≤ 4 · 105, with Tq = max(108/q, 200 + 7.5 · 107/q).

The method used was rigorous; its implementation uses interval arithmetic.
Let us see what this veriﬁcation gives us when used as an input to Prop. 4.6.
We are interested in bounds on | errη,χ∗ (δ, x)| for q ≤ r and |δ| ≤ δ0r/2q. We set
r = 3 · 105 and δ0 = 8, and so |δ| ≤ 4r/q. (We will not be using the veriﬁcation
for q even with 3 · 105 < q ≤ 4 · 105.)
We let T0 = 108/q. Thus,

(4.86) T0 ≥ 108

3 · 105 = 1000
3 ,

T0
π|δ| ≥ 108/q
π · 4r/q = 1000
12π

and so 4.329e
−0.1598T0 ≤ 3.184 · 10
−23,

0.802e
−0.1065 T 2
0
(πδ)2 ≤ 4.3166 · 10
−33.

Since |δ| ≤ 4r/q ≤ 1.2 · 106/q ≤ 1.2 · 106 and qT0 ≤ 108, this gives us

log qT0
2π ·
 (
4.329e
−0.1598T0 + 0.802|δ|e
−0.1065 T 2
0
(πδ)2 )
 ≤ 5.28 · 10
−22 + 8.59 · 10−26

q

≤ 5.281 · 10
−22.

Again by T0 = 108/q,

2.337
√T0 log qT0 + 21.817
√T0 + 2.85 log q + 74.38

is at most 648662
√q + 111,

MAJOR ARCS FOR GOLDBACH’S PROBLEM 57

and
 3 log q + 14|δ| + 17 ≤ 55 + 1.7 · 107

q ,

(log q + 6) · (1 + 5|δ|) ≤ 19 + 1.2 · 108

q .

Hence, assuming x ≥ 108 to simplify, we see that Prop. 4.6 gives us that

errη,χ(δ, x) ≤ 5.281 · 10
−22 +
 648662√q + 111
√x + 55 + 1.7·107
q
x + 19 + 1.2·108
q
x3/2

≤ 5.281 · 10
−22 + 1
√x
 ( 650400
√
q + 112
)

for η(t) = e−t2/2. This proves Theorem 1.1.
Let us now see what Platt’s calculations give us when used as an input to
Prop. 4.8 and Cor. 4.9. Again, we set r = 3 · 105, δ0 = 8, |δ| ≤ 4r/q and
T0 = 108/q, so (4.86) is still valid. We obtain

T0 log qT0
2π ·
 (
3.5e
−0.1598T0 + 0.64e
−0.1065· T 2
0
(πδ)2 )
 ≤ 4.269 · 10−14

q .

We use the same bound when we have 0.0019 instead of 0.64 on the left side,
as in (4.56). (The coeﬃcient aﬀects what is by far the smaller term, so we are
wasting nothing.) Again by T0 = 108/q and q ≤ r,

1.22
√T0 log qT0 + 5.053
√T0 + 1.423 log q + 37.19 ≤ 275263
√q + 55.2

1.675
√T0 log qT0 + 6.936
√T0 + 1.954 log q + 51.047 ≤ 377907
√q + 75.7.

For x ≥ 108, we use |δ| ≤ 4r/q ≤ 1.2 · 106/q to bound

(3 + 11|δ|)x−1 + (log q + 6) · (1 + 6|δ|) · x−3/2 ≤ (0.0004 + 1322
q
 ) x−1/2.

(6 + 22|δ|)x−1 + (log q + 6) · (3 + 17|δ|) · x−3/2 ≤ (0.0007 + 2644
q
 ) x−1/2.

Summing, we obtain

errη,χ ≤ 4.269 · 10−14

q + 1
√
x
 ( 276600
√q + 56
)

for η(t) = t2e−t2/2 and

errη,χ ≤ 4.269 · 10−14

q + 1
√
x
 ( 380600
√q + 76
)

for η(t) = t2e−t2/2 ∗M η2(t). This proves Theorem 1.2 and Corollary 1.3.
Now let us work with the smoothing weight η+. This time around, set r =
150000 if q is odd, and r = 300000 if q is even. As before, we assume

q ≤ r, |δ| ≤ 4r/q.

We can see that Platt’s veriﬁcation [Plab], mentioned before, allows us to take

T0 = H + 250r
q , H = 200,

58 H. A. HELFGOTT

since Tq is always at least this (Tq = 108/q > 200 + 3.75 · 107/q for q ≤ 150000
odd, Tq ≥ 200 + 7.5 · 107/q for q ≤ 300000 even).
Thus,
 T0 − H ≥ 250r
r = 250,

T0 − H
πδ ≥ 250r
πδq ≥ 250
4π = 19.89436 . . .

and also

T0 ≤ 200 + 250 · 150000 ≤ 3.751 · 10
7, qT0 ≤ rH + 250r ≤ 1.35 · 10
8.

Hence

9.462
√T0 − He
−0.1598(T0−H) + 11.287|δ|e
−0.1065 (T0 −H)2

(πδ)2

≤ 4.2259 · 10
−17√ 250r
q + 4r
q · 5.57888 · 10
−18

≤ 3.6598 · 10−13
√q + 6.6947 · 10−12

q .

Examining (4.65), we get

errη+,χ(δ, x) ≤ log 1.35 · 108

2π · ( 3.6598 · 10−13
√q + 6.6947 · 10−12

q
 )

+
 ((1.631 log (
1.35 · 10
8) + 12.42
) √1.35 · 108

q + 1.321 log 300000 + 34.51

)
 x− 1
2

+ (9 + 11 · 1.2 · 106

q
 ) x−1 + (log 300000) (11 + 6 · 1.2 · 106

q
 ) x−3/2

≤ 6.18 · 10−12
√q + 1.14 · 10−10

q

+ ( 499076
√
q + 51.17 + 1.32 · 106

q√x + 9
√
x + 9.1 · 107

qx + 139
x
 ) 1
√x

Making the assumption x ≥ 1012, we obtain

errη+,χ(δ, x) ≤ 6.18 · 10−12
√q + 1.14 · 10−10

q + ( 499100
√q + 52
) 1
√x .

This proves Theorem 1.4 for general q.
Let us optimize things a little more carefully for the trivial character χT . Again,
we will make the assumption x ≥ 1012. We will also assume, as we did before,
that |δ| ≤ 4r/q; this now gives us |δ| ≤ 600000, since q = 1 and r = 150000 for q
odd. We will go up to a height T0 = H + 600000π · t, where H = 200 and t ≥ 10.
Then T0 − H
πδ = 600000πt
4πr ≥ t.

Hence
 9.462√T0 − He
−0.1598(T0−H) + 11.287|δ|e
−0.1065 (T0 −H)2

(πδ)2

≤ 10
−1300000 + 6773000e
−0.1065t2 .

MAJOR ARCS FOR GOLDBACH’S PROBLEM 59

Looking at (4.65), we get

errη+,χT (δ, x) ≤ log T0
2π · (
10
−1300000 + 6773000e
−0.1065t2 )

+ ((1.631 log T0 + 12.42)
√T0 + 34.51)x−1/2 + 6600009x−1.

The value t = 20 seems good enough; we choose it because it is not far from
optimal in the range 1027 ≤ x ≤ 1030. We get that T0 = 12000000π + 200; since
T0 < 108, we are within the range of the computations in [Plab] (or for that
matter [Wed03] or [Plaa]). We obtain

errη+,χT (δ, x) ≤ 3.34 · 10
−11 + 251100
√
x .

Lastly, let us look at the sum estimated in (4.67). Here it will be enough to go
up to just T0 = 2H + max(50, H/4) = 450, where, as before, H = 200. Of course,
the veriﬁcation of the zeros of the Riemann zeta function does go that far; as
we already said, it goes until 108 (or rather more: see [Wed03] and [Plaa]). We
make, again, the assumption x ≥ 1012. We look at (4.68) and obtain

(4.87)
 errℓ2,η+ ≤ (0.607 (log 450)2

log 1012 + 1.21 log 450
) √450e
− π
4 ·50

+ (
2.06
√450 log 450 + 43.87
) · x− 1
2

≤ 1.536 · 10
−15 + 310.84
√
x .

It remains only to estimate the integral in (4.67). First of all,
∫ ∞

0 η2
+(t) log xt dt = ∫ ∞

0 η2
◦(t) log xt dt

+ 2 ∫ ∞

0 (η+(t) − η◦(t))η◦(t) log xt dt + ∫ ∞

0 (η+(t) − η◦(t))
2 log xt dt.

The main term will be given by
∫ ∞

0 η2
◦(t) log xt dt = (0.64020599736635 + O (10
−14)) log x

− 0.021094778698867 + O (
10
−15) ,

where the integrals were computed rigorously using VNODE-LP [Ned06]. (The
integral ∫ ∞
0 η2
◦(t)dt can also be computed symbolically.) By Cauchy-Schwarz and
the triangle inequality,
∫ ∞

0 (η+(t) − η◦(t))η◦(t) log xt dt ≤ |η+ − η◦|2|η◦(t) log xt|2

≤ |η+ − η◦|2(|η◦|2 log x + |η◦ · log |2)

≤ 274.86
H 7/2 (0.80013 log x + 0.214)

≤ 1.944 · 10
−6 · log x + 5.2 · 10
−7,

60 H. A. HELFGOTT

where we are using (B.23) and evaluate |η◦ · log |2 rigorously as above. By (B.23)
and (B.24),
∫ ∞

0 (η+(t) − η◦(t))
2 log xt dt ≤ ( 274.86
H 7/2
 )2 log x + 27428
H 7

≤ 5.903 · 10
−12 · log x + 2.143 · 10
−12.

We conclude that

(4.88)
 ∫ ∞

0 η2
+(t) log xt dt

= (0.640206 + O∗(1.95 · 10
−6)) log x − 0.021095 + O∗(5.3 · 10
−7)

We add to this the error term 1.536 · 10−15 + 310.84/
√x from (4.87), and simplify
using the assumption x ≥ 1012. We obtain:

(4.89)
 ∞∑

n=1 Λ(n)(log n)η2
+(n/x) = 0.640206x log x − 0.021095x

+ O∗ (2 · 10
−6x log x + 310.84
√x log x) ,

and so Prop. 4.12 gives us Proposition 1.5.
As we can see, the relatively large error term 4 · 10−6 comes from the fact that
we have wanted to give the main term in (4.67) as an explicit constant, rather
than as an integral. This is satisfactory; Prop. 1.5 is an auxiliary result needed
for [Helc], as opposed to Thms. 1.1–1.4, which, while crucial for [Helc], are also
of general applicability and interest.

Appendix A. Extrema via bisection and truncated series

In the above, we found ourselves several times in the following familiar situa-
tion. Let f : I → R, I ⊂ R. We wish to ﬁnd the minima and maxima of f in I
numerically, but rigorously.
(This is a situation in which a “proof by plot” would be convincing, but not,
of course, rigorous.)
The bisection method (as described in, e.g., [Tuc11, §5.2]) can be used to show
that the minimum (or maximum) of f on a compact interval I lies within an
interval (usually a very small one). We will need to complement it by other
arguments if either (a) I is not compact, or (b) we want to know the minimum
or maximum exactly.
As in §3.2, let j(ρ) = (1 + ρ2)1/2 and υ(ρ) = √(1 + j(ρ))/2 for ρ ≥ 0. Let Υ,
cos θ0, sin θ0, c0 and c1 be understood as one-variable real-valued functions on ρ,
given by (3.26), (3.28) and (3.34).
First, let us bound Υ(ρ) from below. By the bisection method6 applied with
32 iterations, 0.798375987 ≤ min
0≤ρ≤10 Υ(ρ) ≤ 0.798375989.

Since j(ρ) ≥ ρ and υ(ρ) ≥ √j(ρ)/2 ≥ √ρ/2,

0 ≤ ρ
2υ(ρ)(υ(ρ) + j(ρ)) ≤ ρ
√2ρ3/2 = 1
√2ρ ,

6Implemented by the author from the description in [Tuc11, p. 87–88], using D. Platt’s
interval arithmetic package.

MAJOR ARCS FOR GOLDBACH’S PROBLEM 61

and so

(A.1) Υ(ρ) ≥ 1 − ρ
2υ(ρ)(υ(ρ) + j(ρ)) ≥ 1 − 1
√2ρ .

Hence Υ(ρ) ≥ 0.8418 for ρ ≥ 20. We conclude that

(A.2) 0.798375987 ≤ min
ρ≥0 Υ(ρ) ≤ 0.798375989.

Now let us bound c0(ρ) from below. For ρ ≥ 8,

sin θ0 =
 √ 1
2 − 1
2υ ≥
 √ 1
2 − 1
√2ρ ≥ 1
2 ,

whereas cos θ0 ≥ 1/
√2 for all ρ ≥ 0. Hence, by (A.2)

(A.3) c0(ρ) ≥ 0.7983
√
2 + 1
2 > 1.06

for ρ ≥ 8. The bisection method applied with 28 iterations gives us that

(A.4) max
0.01≤ρ≤8 c0(ρ) ≥ 1 + 5 · 10
−8 > 1.

It remains to study c0(ρ) for ρ ∈ [0, 0.01]. The method we are about to give
actually works for all ρ ∈ [0, 1].
Since
(√1 + x)′ = 1
2
√1 + x , (√1 + x)′′ = − 1
4(1 + x)3/2 ,

( 1
√1 + x
 )′ = −1
2(1 + x)3/2 , ( 1
√
1 + x
 )′′ = ( −1/2
(1 + x)3/2
 )′ = 3/4
(1 + x)5/2 ,

a truncated Taylor expansion gives us that, for x ≥ 0,

(A.5) 1 + 1
2 x − 1
8 x2 ≤ √1 + x ≤ 1 + 1
2 x

1 − 1
2 x ≤ 1
√1 + x ≤ 1 − 1
2 x + 3
8 x2.

Hence, for ρ ≥ 0,

(A.6) 1 + ρ2/2 − ρ4/8 ≤ j(ρ) ≤ 1 + ρ2/2,

1 + ρ2/8 − 5ρ
4/128 + ρ6/256 − ρ8/2048 ≤ υ(ρ) ≤ 1 + ρ2/8,

and so

(A.7) υ(ρ) ≥ 1 + ρ2/8 − 5ρ4/128

for ρ ≤ 8. We also get from (A.5) that

(A.8)
 1
υ(ρ) = 1
√1 + j(ρ)−1
2
 ≤ 1 − 1
2 j(ρ) − 1
2 + 3
8
 ( j(ρ) − 1
2
 )2

≤ 1 − 1
2
 ( ρ2

4 − ρ4

16
 ) + 3
8 ρ4

16 ≤ 1 − ρ2

8 + 7ρ4

128 ,

1
υ(ρ) = 1
√1 + j(ρ)−1
2
 ≥ 1 − 1
2 j(ρ) − 1
2 ≥ 1 − ρ2

8 .

62 H. A. HELFGOTT

Hence

(A.9) sin θ0 =
 √ 1
2 − 1
2υ(ρ) ≥
 √ ρ2

16 − 7ρ4

256 = ρ
4
 √
1 − 7
16 ρ2,

sin θ0 ≤
 √ ρ2

16 = ρ
4 ,

while

(A.10) cos θ0 =
 √1
2 + 1
2υ(ρ) ≥
 √
1 − ρ2

16 , cos θ0 ≤
 √
1 − ρ2

16 + 7ρ4

256 ,

By (A.6) and (A.8),

(A.11) ρ
2υ(υ + j) ≥ ρ
2 1 − ρ2/8
2 + 5ρ2/8 ≥ ρ
2
 (1
2 − 3ρ2

32
 ) = ρ
4 − 3ρ3

64 .

Assuming 0 ≤ ρ ≤ 1,

1

1 + 5ρ2
16 − 9ρ4
64 ≤
 (
1 − 5ρ2

16 + 9ρ4

64 + ( 5ρ2

16 − 9ρ4

64
 )2)
 ≤ 1 − 5ρ2

16 + 61ρ4

256 ,

and so, by (A.7) and (A.8),

ρ
2υ(υ + j) ≤ ρ
2 1 − ρ2
8 + 7ρ4
128
2 + 5ρ2
8 − 21ρ4
128

≤ ρ
4
 (1 − ρ2

8 + 7ρ4

128
 ) (1 − 5ρ2

16 + 46ρ4

256
 )

≤ ρ
4
 (1 − 7ρ2

16 + 35
128 ρ4 − 81
2048 ρ6 + 161
214 ρ
8) ≤ ρ
4 − 7ρ3

64 + 35ρ5

512 .

Hence, we obtain

(A.12)
 Υ(ρ) =
 √
1 + ( ρ
2υ(υ + j)
 )2 − ρ
2υ(υ + j)

≥ 1 + 1
2
 (ρ
4 − 3ρ3

64
 )2 − 1
8
 ( ρ2

16
 )2 − (ρ
4 − 7ρ3

64 + 35ρ5

512
 )

≥ 1 − ρ
4 + ρ2

32 + 7ρ3

64 − ( 3
256 + 1
2048
 ) ρ
4 − 35ρ5

512 + 9ρ6

213

≥ 1 − ρ
4 + ρ2

32 + 7ρ3

64 − 165ρ4

2048 ,

where, in the last line, we use again the assumption ρ ≤ 1.
For x ∈ [−1/4, 0],

√1 + x ≥ 1 + 1
2 x − x2

2 1
4(1 − 1/4)3/2 = 1 + x
2 − x2

33/2

√1 + x ≤ 1 + 1
2 x − x2

8 ≤ 1 + 1
2 x.

MAJOR ARCS FOR GOLDBACH’S PROBLEM 63

Hence
(A.13)
 1 − ρ2

32 − ρ4

33/2 · 256 ≤ cos θ0 ≤
 √
1 − ρ2

16 + 7ρ4

256 ≤ 1 − ρ2

32 + 7ρ4

512
ρ
4
 (1 − 7
32 ρ
2 − 49
33/2 · 256 ρ
4) ≤ sin θ0 ≤ ρ
4
for ρ ≤ 1. Therefore,
c0(ρ) = Υ(ρ) · cos θ0 + sin θ0

≥ (1 − ρ
4 + ρ2

32 + 7ρ3

64 − 165
2048 ρ
4) (1 − ρ2

32 − ρ4

33/2 · 256
 )

+ ρ
4 − 7
128 ρ3 − 49
33/2 · 1024 ρ5

≥ 1 + ρ3

16 −
 (( √
3
2304 + 167
2048
 )
 +
 ( 7
2048 +
 √3
192
 )
 ρ + 7
√3
147456 ρ3)
 ρ
4

≥ 1 + ρ3

16 − 0.0949ρ
4,

where we are again using ρ ≤ 1. We conclude that, for all ρ ∈ (0, 1/2],

c0(ρ) > 1.

Together with (A.3) and (A.4), this shows that

(A.14) c0(ρ) > 1 ∀ρ > 0.

It is easy to check that c0(0) = 1.
(The truncated-Taylor series estimates above could themselves have been done
automatically; see [Tuc11, Ch. 4] (automatic diﬀerentiation). The footnote in
[Tuc11, p. 72] (referring to the work of Berz and Makino [BM98] on “Taylor
models”) seems particularly relevant here. We have preferred to do matters “by
hand” in the above.)
Now let us examine η(ρ), given as in (3.46). Let us ﬁrst focus on the case of
ρ large. We can use the lower bound (A.1) on Υ(ρ). To obtain a good upper
bound on Υ(ρ), we need to get truncated series expansions on 1/ρ for υ and j.
These are:
(A.15)

j(ρ) = √ρ2 + 1 = ρ√1 + 1
ρ2 ≤ ρ (1 + 1
2ρ2
 ) = ρ + 1
2ρ ,

υ(ρ) =
 √ 1 + j
2 ≤ √ ρ
2 + 1
2 + 1
4ρ = √ ρ
2
 √1 + 1
ρ + 1
2ρ2 ≤ √ ρ
2
 (1 + 1
√2ρ
 ) ,

together with the trivial bounds j(ρ) ≥ ρ and υ(ρ) ≥ √j(ρ)/2 ≥ √ρ/2. By
(A.15),

(A.16)
 1
υ2 − υ ≥ 1

ρ
2 (1 + 1√2ρ
 )2 − √ ρ
2
 =
 (
1 + √ 2
ρ )

ρ
2
 ((
1 + 1√2ρ
 )2 − √ 2
ρ
 ) (1 + √ 2
ρ )

=
 2
ρ (
1 + √ 2
ρ )

1 − 2
ρ + ( √2
ρ + 1
2ρ2 ) (
1 + √ 2
ρ ) ≥ 2
ρ +
 √8
ρ3/2

64 H. A. HELFGOTT

for ρ ≥ 15, and so

(A.17) j
υ2 − υ ≥ 2 + √ 8
ρ

for ρ ≥ 15. In fact, the bisection method (applied with 20 iterations, including 10
“initial” iterations after which the possibility of ﬁnding a minimum within each
interval is tested) shows that (A.16) (and hence (A.17)) holds for all ρ ≥ 1. By
(A.15),

(A.18)
 ρ
2υ(υ + j) ≥ ρ
√2ρ (
1 + 1√2ρ
 ) (√ ρ
2 (1 + 1√2ρ
 ) + ρ + 1
2ρ )

≥ 1
√2ρ · 1
1 + 1√
2ρ + 1
ρ ≥ 1
√2ρ − 1
2ρ − 1
√2ρ3/2

for ρ ≥ 16. (Again, (A.18) is also true for 1 ≤ ρ ≤ 16 by the bisection method; it
is trivially true for ρ ∈ [0, 1], since the last term of (A.18) is then negative.) We
also have the easy upper bound

(A.19) ρ
2υ(υ + j) ≤ ρ

2 · √ ρ
2 · (
√ ρ
2 + ρ) = 1
√2ρ + 1 ≤ 1
√2ρ − 1
2ρ + 1
(2ρ)3/2

valid for ρ ≥ 1/2.
Hence, by (A.5), (A.18) and (A.19),

Υ =
 √
1 + ( ρ
2υ(υ + j)
 )2 − ρ
2υ(υ + j)

≤ 1 + 1
2
 ( 1
√
2ρ − 1
2ρ
 )2 − 1
√
2ρ + 1
2ρ + 1
√2ρ3/2 ≤ 1 − 1
√2ρ + 1
ρ

for ρ ≥ 3. Again, we use the bisection method (with 20 iterations) on [1/2, 3],
and note that 1/
√2ρ < 1/ρ for ρ < 1/2; we thus obtain

(A.20) Υ ≤ 1 − 1
√2ρ + 1
ρ

for all ρ > 0.
We recall (3.46) and the lower bounds (A.17) and (A.1). We get

(A.21)
 η ≥ 1
√2
 √
2 + √ 8
ρ
 (
1 + (1 − 1
√2ρ
 )2)
 − 1
2
 (1 − 1
√2ρ + 1
ρ
 )2

+ 1
2 − 1
√
2ρ − ρ
ρ + 1 · (1 − 1
√2ρ + 1
ρ
 )

≥ (1 + 1
√
2ρ − 1
4ρ
 ) (
2 −
 √
2
√ρ + 1
2ρ
 )
 − 1
2
 (1 − 2
√2ρ + 5
2ρ
 )

+ 1
2 − 1
√
2ρ − (1 − ρ
−1 + ρ−2) (1 − 1
√2ρ + 1
ρ
 )

≥ 1 + 1
√2ρ − 9
4ρ − 1
8ρ2 + 1
√2ρ5/2 − 1
ρ3 ≥ 1 + 1
√2ρ − 37
16ρ

for ρ ≥ 2. This implies that η(ρ) > 1 for ρ ≥ 11. (Since our estimates always
give an error of at most O(1/
√ρ), we also get limρ→∞ η(ρ) = 1.) The bisection

MAJOR ARCS FOR GOLDBACH’S PROBLEM 65

method (with 20 iterations, including 6 initial iterations) gives that η(ρ) > 1 also
holds for 1 ≤ ρ ≤ 11.
Let us now look at what happens for ρ ≤ 1. From (A.12), we get the simpler
bound

(A.22) Υ ≥ 1 − ρ
4 + ρ2

32 + 3ρ3

32 ≥ 1 − ρ
4
valid for ρ ≤ 1, implying that

Υ2 ≥ 1 − ρ
2 + ρ2

8 + 11ρ3

64 − 23ρ4

1024

for ρ ≤ 1. We also have, by (3.26) and (A.11),

(A.23) Υ ≤ 1 + 1
2
 ( ρ
2υ(υ + j)
 )2 − ρ
2υ(υ + j) ≤ 1 + 1
2
 ( ρ
4
 )2 − ( ρ
4 − 3ρ3

64
 )

≤ 1 − ρ
4 + ρ2

32 + 3ρ3

64 ≤ 1 − ρ
4 + 5ρ2

64

for ρ ≤ 1. (This immediately implies the easy bound Υ ≤ 1, which follows
anyhow from (3.25) for all ρ ≥ 0.)
By (A.6),
 j
υ2 − υ ≥ 1 + ρ2/2 − ρ4/8
(
1 + ρ2
8 )2 − (
1 + ρ2
8 ) ≥ 1 + ρ2/2 − ρ4/8

ρ2
8 + ρ4
64 ≥ 8
ρ2

for ρ ≤ 1. Therefore, by (3.46),

η ≥ 1
√2
 √ 8
ρ2
 (2 − ρ
2 + ρ2

8 + 11ρ3

64 − 3ρ4

128
 ) − 1
2
 (1 − ρ
4 + 5ρ2

64
 )2 + 1
2 − 1
2 − ρ
2

≥ 4
ρ − 1 + ρ
4 + 11ρ2

32 − 3ρ3

64 − 1
2
 (1 − ρ
2 + 7ρ2

32
 ) − ρ
2 ≥ 4
ρ − 3
2 + 15ρ2

64 − 3ρ3

64

≥ 4
ρ − 3
2

for ρ ≤ 1. This implies the bound η(ρ) > 1 for all ρ ≤ 1. Conversely, η(ρ) ≥
4/ρ − 3/2 follows from η(ρ) > 1 for ρ > 8/5. We check η(ρ) ≥ 4/ρ − 3/2 for
ρ ∈ [1, 8/5] by the bisection method (5 iterations).
We conclude that, for all ρ > 0,

(A.24) η ≥ max (1, 4
ρ − 3
2
 ) .

This bound has the right asymptotics for ρ → 0+ and ρ → +∞.
Let us now bound c0 from above. By (A.13) and (A.23),

(A.25) c0(ρ) = Υ(ρ) · cos θ0 + sin θ0 ≤ (1 − ρ
4 + 5ρ2

64
 ) (
1 − ρ2

32 + 7ρ4

512
 ) + ρ
4

≤ 1 + 3ρ2

64 + ρ3

128 + 23ρ4

2048 − 7ρ5

2048 + 35ρ6

215 ≤ 1 + ρ2

15

for ρ ≤ 1. Since Υ ≤ 1 and θ0 ∈ [0, π/4] ⊂ [0, π/2], the bound

(A.26) c0(ρ) ≤ cos θ0 + sin θ0 ≤ √2

66 H. A. HELFGOTT

holds for all ρ ≥ 0. By (A.20), we also know that, for ρ ≥ 2,

(A.27)
 c0(ρ) ≤ (1 − 1
√2ρ + 1
ρ
) cos θ0 + sin θ0

≤
 √(1 − 1
√2ρ + 1
ρ
 )2 + 1 ≤ √
2 (1 − 1
2
√2ρ + 9
16ρ
 ) .

From (A.24) and (A.26), we obtain that

(A.28) 1
η (1 + 2c
2
0) ≤ 1 · (1 + 2 · 2) = 5

for all ρ ≥ 0. At the same time, (A.24) and (A.25) imply that

1
η (
1 + 2c
2
0) ≤ ( 4
ρ − 3
2
 )−1 (3 + 4ρ2

15 + 2ρ4

152
 )

= 3ρ
4
 (1 − 3ρ
8
 )−1 (1 + 4ρ2

45 + ρ4

675
 ) ≤ 3ρ
4
 (
1 + ρ
2
 )

for ρ ≤ 0.4. Hence (1 + 2c2
0)/η ≤ 0.86ρ for ρ < 0.29. The bisection method
(20 iterations, starting by splitting the range into 28 equal intervals) shows that
(1 + 2c2
0)/η ≤ 0.86ρ also holds for 0.29 ≤ ρ ≤ 6; for ρ > 6, the same inequality
holds by (A.28).
We have thus shown that

(A.29) 1 + 2c2
0
η ≤ min(5, 0.86ρ)

for all ρ > 0.
Now we wish to bound √(υ2 − υ)/2 from below. By (A.7) and (A.6),

(A.30) υ2 − υ ≥ (1 + ρ2

8 − 5ρ4

128
 )2 − (1 + ρ2

8
 )

= 1 + ρ2

4 − 5ρ4

64 + ( 5ρ2

128 − 1
8
 )2 ρ
4 − (1 + ρ2

8
 ) ≥ ρ2

8 − 5ρ4

64 ,

for ρ ≥ 1, and so √ υ2 − υ
2 ≥ ρ
4
 √
1 − 5ρ2

8 ,

and this is greater than ρ/6 for ρ ≤ 1/3. The bisection method (20 iterations, 5
initial steps) conﬁrms that √(υ2 − υ)/2 > ρ/6 also holds for 2/3 < ρ ≤ 4. On
the other hand, by (A.15) and υ2 = (1 + j)/2 ≥ (1 + ρ)/2,

(A.31)
 √ υ2 − υ
2 ≥
 √
√
√
√ ρ+1
2 − √ ρ
2 (1 + 1√2ρ
 )

2 ≥ √ρ
2
 √
1 + 1
ρ − √ 2
ρ
 (1 + 1
√
2ρ
 )

≥ √ρ
2
 √
1 − √ 2
ρ + 1
2ρ ≥ √
ρ
2
 (1 − √ 1
2ρ
 ) = √ρ
2 − 1
23/2

for ρ ≥ 4. We check by the bisection method (20 iterations) that √(υ2 − υ)/2 ≥
√
ρ/2 − 1/23/2 also holds for all 0 ≤ ρ ≤ 4.

MAJOR ARCS FOR GOLDBACH’S PROBLEM 67

We conclude that

(A.32)
 √υ2 − υ
2 ≥
 {
ρ/6 if ρ ≤ 4,
√ρ
2 − 1
23/2 for all ρ.

We still have a few other inequalities to check. Let us ﬁrst derive an easy lower
bound on c1(ρ) for ρ large: by (A.1), (A.16) and (A.5),

c1(ρ) =
 √ 1 + 1/υ
υ2 − υ · Υ ≥
 √ 1
υ2 − υ · (1 − 1
√2ρ
 ) ≥
 √ 2
ρ +
 √8
ρ3/2 · (1 − 1
√2ρ
 )

= √ 2
ρ
 (
1 + 1
√2ρ − 1
4ρ
 ) · (1 − 1
√
2ρ
 ) ≥ √ 2
ρ
 (1 − 3
4ρ
 )

for ρ ≥ 1. Together with (A.27), this implies that, for ρ ≥ 2,

c0 − 1/
√2
√2c1ρ ≤
 √2 ( 1
2 − 1
2
√2ρ + 9
16ρ )

√
2ρ
√ 2
ρ (
1 − 3
4ρ ) = 1
√2ρ · 1 − 1√
2ρ + 9
8ρ

2 (1 − 3
4ρ ) ,

again for ρ ≥ 1. This is ≤ 1/
√8ρ for ρ ≥ 8. Hence it is ≤ 1/
√8 · 25 < 0.071 for
ρ ≥ 25.
Let us now look at ρ small. By (A.6),

υ2 − υ ≤ (1 + ρ2

8
 )2 − (1 + ρ2

8 − 5ρ4

32
 ) = ρ2

8 + 9ρ4

32

for any ρ > 0. Hence, by (A.8) and (A.22),

c1(ρ) =
 √ 1 + 1/υ
υ2 − υ · Υ ≥
 √ 2 − ρ2/8

ρ2
8 + 9ρ4
32 · (
1 − ρ
4
 ) ≥ 4
ρ
 (1 − 5
4 ρ2) (1 − ρ
4
 ) ,

whereas, for ρ ≤ 1,

c0(ρ) = Υ(ρ) · cos θ0 + sin θ0 ≤ 1 + sin θ0 ≤ 1 + ρ/4

by (A.13). Thus
 c0 − 1/
√2
√2c1ρ ≤ 1 + ρ
4 − 1√
2√
2 · 4 (1 − 5
4 ρ2) (1 − ρ
4 ) ≤ 0.0584

for ρ ≤ 0.1. We check the remaining interval [0.1, 25] (or [0.1, 8], if we aim at the
bound ≤ 1/
√8ρ) by the bisection method (with 24 iterations, including 12 initial
iterations – or 15 iterations and 10 initial iterations, in the case of [0.1, 8]) and
obtain that

(A.33) 0.0763895 ≤ max
ρ≥0 c0 − 1/
√2
√2c1ρ ≤ 0.0763896

sup
ρ≥0
 c0 − 1/
√2
c1√ρ ≤ 1
2 .

In the same way, we see that
c0
c1ρ ≤ 1
√ρ 1
1 − 3
4ρ ≤ 0.171

for ρ ≥ 36 and c0
c1ρ ≤ 1 + ρ
4
4 (1 − 5
4 ρ2) (1 − ρ
4 ) ≤ 0.267

68 H. A. HELFGOTT

for ρ ≤ 0.1. The bisection method applied to [0.1, 36] with 24 iterations (including
12 initial iterations) now gives

(A.34) 0.29887 ≤ max
ρ>0 c0
c1ρ ≤ 0.29888.

We would also like a lower bound for c0/c1. For c0, we can use the lower bound
c0 ≥ 1 given by (A.14). By (A.8), (A.23) and (A.30),

c1(ρ) =
 √ 1 + 1/υ
υ2 − υ · Υ ≤
 √ 2 − ρ2
8 + 7ρ4
128
ρ2/8 − 5ρ4/64 · (1 − ρ
4 + 5ρ2

64
 )

≤ 4
ρ
 (1 + 5ρ2

16
 ) (1 − ρ
4 + 5ρ2

64
 ) < 4
ρ

for ρ ≤ 1/4. Thus, c0/(c1ρ) ≥ 1/4 for ρ ∈ [0, 1/4]. The bisection method (with 20
iterations, including 10 initial iterations) gives us that c0/(c1ρ) ≥ 1/4 also holds
for ρ ∈ [1/4, 6.2]. Hence c0
c1 ≥ ρ
4
for ρ ≤ 6.2.
Now consider the case of large ρ. By and Υ ≤ 1,

(A.35) c0
c1√ρ ≥ 1/Υ
√ 1+1/υ
υ2−υ · √
ρ ≥
 √
(υ2 − υ)/ρ
√1 + 1/υ ≥ 1
√2 1 − 1/
√2ρ
√1 + 1/υ .

(This is oﬀ from optimal by a factor of about √
2.) For ρ ≥ 200, (A.35) implies
that c0/(c1√ρ) ≥ 0.6405. The bisection method (with 20 iterations, including
5 initial iterations) gives us c0/(c1√ρ) ≥ 5/8 = 0.625 for ρ ∈ [6.2, 200]. We
conclude that

(A.36) c0
c1 ≥ min (ρ
4 , 5
8 √ρ
) .

Finally, we verify an inequality that will be useful for the estimation a crucial
exponent in Thm. 3.1. We wish to show that, for all α ∈ [0, π/2],

(A.37) α − sin 2α
4 cos2 α
2 ≥ sin α
2 cos2 α − 5 sin3 α
24 cos6 α

The left side is positive for all α ∈ (0, π/2], since cos2 α/2 ≥ 1/
√2 and (sin 2α)/2
is less than 2α/2 = α. The right side is negative for α > 1 (since it is negative
for α = 1, and (sin α)/(cos α)2 is increasing on α). Hence, it is enough to check
(A.37) for α ∈ [0, 1]. The two sides of (A.37) are equal for α = 0; moreover,
the ﬁrst four derivatives also match at α = 0. We take the ﬁfth derivatives of
both sides; the bisection method (running on [0, 1] with 20 iterations, including
10 initial iterations) gives us that the ﬁfth derivative of the left side minus the
ﬁfth derivative of the right side is always positive on [0, 1] (and minimal at 0,
where it equals 30.5 + O∗ (10−9)).

Appendix B. Norms of smoothing functions

Our aim here is to give bounds on the norms of some smoothing functions –
and, in particular, on several norms of a smoothing function η+ : [0, ∞) → R
based on the Gaussian η♥(t) = e−t2/2.

MAJOR ARCS FOR GOLDBACH’S PROBLEM 69

As before, we write

(B.1) h : t ↦→
 {
t2(2 − t)3et−1/2 if t ∈ [0, 2],
0 otherwise

We recall that we will work with an approximation η+ to the function η◦ :
[0, ∞) → R deﬁned by

(B.2) η◦(t) = h(t)η♥(t) =
 {
t3(2 − t)3e−(t−1)2/2 for t ∈ [0, 2],
0 otherwise.

The approximation η+ is deﬁned by

(B.3) η+(t) = hH (t)te
−t2/2,

where

(B.4) FH(t) = sin(H log y)
π log y ,

hH(t) = (h ∗M FH)(y) = ∫ ∞

0 h(ty−1)FH (y) dy
y

and H is a positive constant to be set later. By (2.4), M hH = M h · M FH . Now
FH is just a Dirichlet kernel under a change of variables; using this, we get that,
for τ real,

(B.5) M FH (iτ ) =
 



1 if |τ | < H,
1/2 if |τ | = H,
0 if |τ | > H.

Thus,

(B.6) M hH (iτ ) =
 



M h(iτ ) if |τ | < H,
1
2 M h(iτ ) if |τ | = H,
0 if |τ | > H.

As it turns out, h, η◦ and M h (and hence M hH ) are relatively easy to work
with, whereas we can already see that hH and η+ have more complicated deﬁni-
tions. Part of our work will consist in expressing norms of hH and η+ in terms
of norms of h, η◦ and M h.

B.1. The decay of M h(iτ ). Now, consider any φ : [0, ∞) → C that (a) has
compact support (or fast decay), (b) satisﬁes φ(k)(t)tk−1 = O(1) for t → 0+ and
0 ≤ k ≤ 3, and (c) is C 2 everywhere and quadruply diﬀerentiable outside a ﬁnite
set of points.
By deﬁnition,
 M φ(s) = ∫ ∞

0 φ(x)xs dx
x .

Thus, by integration by parts, for ℜ(s) > −1 and s ̸= 0,

(B.7)
 M φ(s) = ∫ ∞

0 φ(x)xs dx
x = lim
t→0+
 ∫ ∞

t φ(x)xs dx
x = − lim
t→0+
 ∫ ∞

t φ
′(x) xs

s dx

= lim
t→0+
 ∫ ∞

t φ
′′(x) xs+1

s(s + 1) dx = lim
t→0+ − ∫ ∞

t φ
(3)(x) xs+2

s(s + 1)(s + 2) dx

= lim
t→0+
 ∫ ∞

t φ
(4)(x) xs+3

s(s + 1)(s + 2)(s + 3) dx,

70 H. A. HELFGOTT

where φ(4)(x) is understood in the sense of distributions at the ﬁnitely many
points where it is not well-deﬁned as a function.
Let s = it, φ = h. Let Ck = limt→0+ ∫ ∞
t |h(k)(x)|xk−1dx for 0 ≤ k ≤ 4. Then
(B.7) gives us that
(B.8)

M h(it) ≤ min (C0, C1
|t| , C2
|t||t + i| , C3
|t||t + i||t + 2i| , C4
|t||t + i||t + 2i||t + 3i|
 ) .

We must estimate the constants Cj, 0 ≤ j ≤ 4.
Clearly, h(t)t−1 = O(1) as t → 0+, hk(t) = O(1) as t → 0+ for all k ≥ 1, h(2) =
h′(2) = h′′(2) = 0, and h(x), h′(x) and h′′(x) are all continuous. The function
h′′′ has a discontinuity at t = 2. As we said, we understand h(4) in the sense of
distributions at t = 2; for example, limǫ→0 ∫ 2+ǫ
2−ǫ h(4)(t)dt = limǫ→0(h(3)(2 + ǫ) −
h(3)(2 − ǫ)).
Symbolic integration easily gives that

(B.9) C0 = ∫ 2

0 t(2 − t)
3e
t−1/2dt = 92e
−1/2 − 12e
3/2 = 2.02055184 . . .

We will have to compute Ck, 1 ≤ k ≤ 4, with some care, due to the absolute
value involved in the deﬁnition.
The function (x2(2 − x)3ex−1/2)′ = ((x2(2 − x)3)′ + x2(2 − x)3)ex−1/2 has the
same zeros as H1(x) = (x2(2 − x)3)′ + x2(2 − x)3, namely, −4, 0, 1 and 2. The
sign of H1(x) (and hence of h′(x)) is + within (0, 1) and − within (1, 2). Hence

(B.10) C1 = ∫ ∞

0 |h
′(x)|dx = |h(1) − h(0)| + |h(2) − h(1)| = 2h(1) = 2
√e.

The situation with (x2(2 − x)3ex−1/2)′′ is similar: it has zeros at the roots of
H2(x) = 0, where H2(x) = H1(x) + H ′
1(x) (and, in general, Hk+1(x) = Hk(x) +
H ′
k(x)). This time, we will prefer to ﬁnd the roots numerically. It is enough to
ﬁnd (candidates for) the roots using any available tool
7 and then check rigorously
that the sign does change around the purported roots. In this way, we check that
H2(x) = 0 has two roots α2,1, α2,2 in the interval (0, 2), another root at 2, and
two more roots outside [0, 2]; moreover,

(B.11) α2,1 = 0.48756597185712 . . . ,
α2,2 = 1.48777169309489 . . . ,

where we verify the root using interval arithmetic. The sign of H2(x) (and hence
of h′′(x)) is ﬁrst +, then −, then +. Write α2,0 = 0, α2,3 = 2. By integration by
parts,
(B.12)

C2 = ∫ ∞

0 |h
′′(x)|x dx = ∫ α2,1

0 h
′′(x)x dx − ∫ α2,2

α2,1 h
′′(x)x dx + ∫ 2

α2,2 h
′′(x)x dx

=
 3∑

j=1(−1)
j+1 (
h
′(x)x|
α2,j
α2,j−1 − ∫ α2,j

α2,j−1 h
′(x) dx
)

= 2
 2∑

j=1(−1)
j+1 (
h
′(α2,j)α2,j − h(α2,j)
) = 10.79195821037 . . . .

7Routine find root in SAGE was used here.

MAJOR ARCS FOR GOLDBACH’S PROBLEM 71

To compute C3, we proceed in the same way, ﬁnding two roots of H3(x) = 0
(numerically) within the interval (0, 2), viz.,

α3,1 = 1.04294565694978 . . .
α3,2 = 1.80999654602916 . . .

The sign of H3(x) on the interval [0, 2] is ﬁrst −, then +, then −. Write α3,0 = 0,
α3,3 = 2. Proceeding as before – with the only diﬀerence that the integration by
parts is iterated once now – we obtain that

(B.13)
 C3 = ∫ ∞

0 |h
′′′(x)|x2dx =
 3∑

j=1(−1)
j ∫ α3,j

α3,j−1 h
′′′(x)x2dx

=
 3∑

j=1(−1)
j (
h
′′(x)x2|
α3,j
α3,j−1 − ∫ α3,j

α3,j−1 h
′′(x) · 2x
)
 dx

=
 3∑

j=1(−1)
j (h
′′(x)x2 − h
′(x) · 2x + 2h(x)
) |
α3,j
α3,j−1

= 2
 2∑

j=1(−1)
j(h
′′(α3,j)α
2
3,j − 2h
′(α3,j)α3,j + 2h(α3,j))

and so interval arithmetic gives us

(B.14) C3 = 75.1295251672 . . .

The treatment of the integral in C4 is very similar, at least as ﬁrst. There are
two roots of H4(x) = 0 in the interval (0, 2), namely,

α4,1 = 0.45839599852663 . . .
α4,2 = 1.54626346975533 . . .

The sign of H4(x) on the interval [0, 2] is ﬁrst −, +, then −. Using integration
by parts as before, we obtain
∫ 2−

0+
 ∣
∣
∣h
(4)(x)
∣
∣
∣ x3dx

= − ∫ α4,1

0+ h
(4)(x)x3dx + ∫ α4,2

α4,1 h
(4)(x)x3dx − ∫ 2−

α4,1 h
(4)(x)x3dx

= 2
 2∑

j=1(−1)
j (
h
(3)(α4,j)α
3
4,j − 3h
(2)(α4,j)α
2
4,j + 6h
′(α4,j)α4,j − 6h(α4,j )
)

− lim
t→2− h
(3)(t)t3 = 1152.69754862 . . . ,

since limt→0+ h(k)(t)tk = 0 for 0 ≤ k ≤ 3, limt→2− h(k)(t) = 0 for 0 ≤ k ≤ 2 and
limt→2− h(3)(t) = −24e3/2. Now
∫ ∞

2− |h
(4)(x)x3|dx = lim
ǫ→0+ |h
(3)(2 + ǫ) − h
(3)(2 − ǫ)| · 2
3 = 2
3 · 24e
3/2,

Hence

(B.15) C4 = ∫ 2−

0+
 ∣
∣
∣h
(4)(x)
∣
∣
∣ x3dx + 24e
3/2 · 2
3 = 2013.18185012 . . .

72 H. A. HELFGOTT

We ﬁnish by remarking that can write down M h explicitly:
(B.16)
M h = −e
−1/2(−1)
−s(8γ(s+2, −2)+12γ(s+3, −2)+6γ(s+4, −2)+γ(s+ 5, −2)),

where γ(s, x) is the (lower) incomplete Gamma function

γ(s, x) = ∫ x

0 e
−tts−1dt.

We will, however, ﬁnd it easier to deal with M h by means of the bound (B.8), in
part because (B.16) amounts to an invitation to numerical instability.
For instance, it is easy to use (B.8) to give a bound for the ℓ1-norm of M h(it).
Since C4/C3 > C3/C2 > C2/C1 > C1/C0,

|M h(it)|1 = 2 ∫ ∞

0 M h(it)dt

≤ 2
 (
C0 · C1
C0 + C1
 ∫ C2/C1

C1/C0
 dt
t + C2
 ∫ C3/C2

C2/C1
 dt
t2 + C3
 ∫ C4/C3

C3/C2
 dt
t3 + C4
 ∫ ∞

C4/C3
 dt
t4
 )

= 2 (C1 + C1 log C2C0
C 2
1 + C2
 ( C1
C2 − C2
C3
 ) + C3
2
 ( C 2
2
C 2
3 − C 2
3
C 2
4
 ) + C4
3 · C 3
3
C 3
4
 ) ,

and so

(B.17) |M h(it)|1 ≤ 16.1939176.

This bound is far from tight, but it will certainly be useful.
Similarly, |(t + i)M h(it)|1 is at most two times

C0
 ∫ C1
C0

0 |t + i| dt + C1
 ∫ C2
C1

C1
C0
 ∣
∣
∣
∣1 + i
t
 ∣
∣
∣
∣ dt + C2
 ∫ C3
C2

C2
C1
 dt
t + C3
 ∫ C4
C3

C3
C2
 dt
t2 + C4
 ∫ ∞

C4
C3
 dt
t3

= C0
2
 (√ C 4
1
C 4
0 + C 2
1
C 2
0 + sinh−1 C1
C0
 )
 + C1
 (√t2 + 1 + log
 ( √t2 + 1 − 1
t
 ))
 |
 C2
C1
C1
C0

+ C2 log C3C1
C 2
2 + C3
 (C2
C3 − C3
C4
 ) + C4
2 C 2
3
C 2
4 ,

and so

(B.18) |(t + i)M h(it)|1 ≤ 27.8622803.

B.2. The diﬀerence η+ − η◦ in ℓ2 norm. We wish to estimate the distance
in ℓ2 norm between η◦ and its approximation η+. This will be an easy aﬀair,
since, on the imaginary axis, the Mellin transform of η+ is just a truncation of
the Mellin transform of η◦.
By (B.2) and (B.3),

(B.19) |η+ − η◦|
2
2 = ∫ ∞

0
 ∣
∣
∣hH (t)te
−t2/2 − h(t)te
−t2/2∣
∣
∣2 dt

≤ (max
t≥0 e
−t2t3) · ∫ ∞

0 |hH(t) − h(t)|
2 dt
t .

MAJOR ARCS FOR GOLDBACH’S PROBLEM 73

The maximum maxt≥0 t3e−t2 is (3/2)3/2e−3/2. Since the Mellin transform is an
isometry (i.e., (2.2) holds),
(B.20)∫ ∞

0 |hH (t) − h(t)|
2 dt
t = 1
2π
 ∫ ∞

−∞ |M hH (it) − M h(it)|
2dt = 1
π
 ∫ ∞

H |M h(it)|
2dt.

By (B.8),

(B.21) ∫ ∞

H |M h(it)|
2dt ≤ ∫ ∞

H
 C 2
4
t8 dt ≤ C 2
4
7H 7 .

Hence

(B.22) ∫ ∞

0 |hH (t) − h(t)|
2 dt
t ≤ C 2
4
7πH 7 .

Using the bound (B.15) for C4, we conclude that

(B.23) |η+ − η◦|2 ≤ C4√7π
 ( 3
2e
 )3/4 · 1
H 7/2 ≤ 274.856893
H 7/2 .

It will also be useful to bound
∣
∣
∣
∣
∫ ∞

0 (η+(t) − η◦(t))
2 log t dt∣
∣
∣
∣ .

This is at most (max
t≥0 e
−t2t3| log t|
) · ∫ ∞

0 |hH (t) − h(t)|
2 dt
t .

Now
 max
t≥0 e
−t2t3| log t| = max ( max
t∈[0,1] e
−t2t3(− log t), max
t∈[1,5] e
−t2t3 log t)

= 0.14882234545 . . .

where we ﬁnd the maximum by the bisection method with 40 iterations.
8 Hence,
by (B.22),

(B.24)
 ∫ ∞

0 (η+(t) − η◦(t))
2| log t|dt ≤ 0.148822346 C 2
4
7π

≤ 27427.502
H 7 ≤ ( 165.61251
H 7/2
 )2 .

B.3. Norms involving η+. Let us now bound some ℓ1- and ℓ2-norms involving
η+. Relatively crude bounds will suﬃce in most cases.
First, by (B.23),

(B.25) |η+|2 ≤ |η◦|2 + |η+ − η◦|2 ≤ 0.800129 + 274.8569
H 7/2 ,

where we obtain

(B.26) |η◦|2 = √0.640205997 . . . = 0.8001287 . . .

by symbolic integration.

8The bisection method (as described in, e.g., [Tuc11, §5.2]) can be used to show that the
minimum (or maximum) of f on a compact interval I lies within an interval (usually a very
small one). Here, the bisection method was carried rigorously, using interval arithmetic. The
method was implemented by the author from the description in [Tuc11, p. 87–88], using D.
Platt’s interval arithmetic package.

74 H. A. HELFGOTT

Let us now bound |η+ · log |2
2. By isometry and (2.6),

|η+ · log |
2
2 = 1
2πi
 ∫ 1
2 +i∞

1
2 −i∞ |M (η+ · log)(s)|
2ds = 1
2πi
 ∫ 1
2 +i∞

1
2 −i∞ |(M η+)
′(s)|
2ds.

Now, (M η+)′(1/2 + it) equals 1/2π times the additive convolution of M hH (it)
and (M η♦)′(1/2 + it), where η♦(t) = te−t2/2. Hence, by Young’s inequality,
|(M η+)′(1/2 + it)|2 ≤ (1/2π)|M hH (it)|1|(M η♦)′(1/2 + it)|2.
Again by isometry and (2.6),

|(M η♦)
′(1/2 + it)|2 = √2π|η♦ · log |2.

Hence, by (B.17),

|η+ · log |2 ≤ 1
2π |M hH (it)|1|η♦ · log |2 ≤ 2.5773421 · |η♦ · log |2.

Since, by symbolic integration,

(B.27) |η♦ · log |2 ≤
 √ √
π
32 (8(log 2)2 + 2γ2 + π2 + 8(γ − 2) log 2 − 8γ)

≤ 0.3220301,

we get that

(B.28) |η+ · log |2 ≤ 0.8299818.

Let us bound |η+(t)tσ|1 for σ ∈ (−2, ∞). By Cauchy-Schwarz and Plancherel,
(B.29)
|η+(t)tσ|1 = ∣
∣
∣hH (t)t1+σe
−t2/2∣
∣
∣1 ≤ ∣
∣
∣tσ+3/2e
−t2/2∣
∣
∣
2 |hH (t)/
√t|2

= ∣
∣
∣tσ+3/2e
−t2/2∣
∣
∣
2
 √∫ ∞

0 |hH (t)|2 dt
t = ∣
∣
∣tσ+3/2e
−t2/2∣
∣
∣2 ·
 √ 1
2π
 ∫ H

−H |M h(ir)|2dr

≤ ∣
∣
∣tσ+3/2e
−t2/2∣
∣
∣
2 ·
 √ 1
2π
 ∫ ∞

−∞ |M h(ir)|2dr = ∣
∣
∣tσ+3/2e
−t2/2∣
∣
∣
2 · |h(t)/
√t|2.

Since ∣
∣
∣tσ+3/2e
−t2/2∣
∣
∣
2 =
 √∫ ∞

0 e−t2t2σ+3dt =
 √ Γ(σ + 2)
2 ,

|h(t)/
√t|2 =
 √ 31989
8e − 585e3

8 ≤ 1.5023459,

we conclude that

(B.30) |η+(t)tσ|1 ≤ 1.062319 · √Γ(σ + 2)

for σ > −2.

B.4. Norms involving η′
+. By one of the standard transformation rules (see
(2.6)), the Mellin transform of η′
+ equals −(s − 1) · M η+(s − 1). Since the Mellin
transform is an isometry in the sense of (2.2),

|η′
+|
2
2 = 1
2πi
 ∫ 1
2 +i∞

1
2 −i∞
 ∣
∣M (η′
+)(s)
∣
∣2 ds = 1
2πi
 ∫ − 1
2 +i∞

− 1
2 −i∞ |s · M η+(s)|2 ds.

MAJOR ARCS FOR GOLDBACH’S PROBLEM 75

Recall that η+(t) = hH(t)η♦(t), where η♦(t) = te−t2/2. Thus, by (2.5), the
function M η+(−1/2+it) equals 1/2π times the (additive) convolution of M hH (it)
and M η♦(−1/2 + it). Therefore, for s = −1/2 + it,

(B.31)
 |s| |M η+(s)| = |s|
2π
 ∫ H

−H M h(ir)M η♦(s − ir)dr

≤ 3
2π
 ∫ H

−H |ir − 1||M h(ir)| · |s − ir||M η♥(s − ir)|dr

= 3
2π (f ∗ g)(t),

where f (t) = |it − 1||M h(it)| and g(t) = | − 1/2 + it||M η♦(−1/2 + it)|. (Since
|(−1/2 + i(t − r)) + (1 + ir)| = |1/2 + it| = |s|, either | − 1/2 + i(t − r)| ≥ |s|/3 or
|1+ir| ≥ 2|s|/3; hence |s−ir||ir−1| = |−1/2+i(t−r)||1+ir| ≥ |s|/3.) By Young’s
inequality (in a special case that follows from Cauchy-Schwarz), |f ∗g|2 ≤ |f |1|g|2.
By (B.18), |f |1 = |(r + i)M h(ir)|1 ≤ 27.8622803.

Yet again by Plancherel,

|g|
2
2 = ∫ − 1
2 +i∞

− 1
2 −i∞ |s|
2|M η♦(s)|
2ds = ∫ 1
2 +i∞

1
2 −i∞ |(M (η′
♦))(s)|
2ds = 2π|η′
♦|
2
2 = 3π 3
2
4 .

Hence

(B.32) |η′
+|2 ≤ 1
√2π · 3
2π |f ∗ g|2 ≤ 1
√
2π 3
2π · 27.8622803

√ 3π 3
2
4 ≤ 10.845789.

Let us now bound |η′
+(t)tσ|1 for σ ∈ (−1, ∞). First of all,

|η′
+(t)tσ|1 = ∣
∣
∣
∣
(hH(t)te
−t2/2)′ tσ∣
∣
∣
∣
1 ≤ ∣
∣
∣
(h
′
H(t)te
−t2/2 + hH(t)(1 − t2)e
−t2/2) · tσ∣
∣
∣
1

≤ ∣
∣
∣h
′
H (t)tσ+1e
−t2/2∣
∣
∣1 + |η+(t)tσ−1|1 + |η+(t)tσ+1|1.

We can bound the last two terms by (B.30). Much as in (B.29), we note that
∣
∣
∣h
′
H (t)tσ+1e
−t2/2∣
∣
∣
1 ≤ ∣
∣
∣tσ+1/2e
−t2/2∣
∣
∣
2 |h
′
H(t)
√t|2,

and then see that

|h
′
H (t)
√t|2 =
 √∫ ∞

0 |h′
H (t)|2t dt =
 √ 1
2π
 ∫ ∞

−∞ |M (h′
H )(1 + ir)|2dr

=
 √ 1
2π
 ∫ ∞

−∞ |(−ir)M hH (ir)|2dr =
 √ 1
2π
 ∫ H

−H |(−ir)M h(ir)|2dr

=
 √ 1
2π
 ∫ H

−H |M (h′)(1 + ir)|2dr ≤
 √ 1
2π
 ∫ ∞

−∞ |M (h′)(1 + ir)|2dr = |h
′(t)
√t|2,

where we use the ﬁrst rule in (2.6) twice. Since

∣
∣
∣tσ+1/2e
−t2/2∣
∣
∣
2 =
 √ Γ(σ + 1)
2 , |h
′(t)
√t|2 =
 √ 103983
16e − 1899e3

16 = 2.6312226,

76 H. A. HELFGOTT

we conclude that
(B.33)

|η′
+(t)tσ|1 ≤ 1.062319 · (
√Γ(σ + 1) + √Γ(σ + 3)) +
 √ Γ(σ + 1)
2 · 2.6312226

≤ 2.922875
√Γ(σ + 1) + 1.062319
√Γ(σ + 3)

for σ > −1.

B.5. The ℓ∞-norm of η+. Let us now get a bound for |η+|∞. Recall that
η+(t) = hH(t)η♦(t), where η♦(t) = te−t2/2. Clearly

(B.34) |η+|∞ = |hH(t)η♦(t)|∞ ≤ |η◦|∞ + |(h(t) − hH (t))η♦(t)|∞

≤ |η◦|∞ + ∣
∣
∣
∣ h(t) − hH(t)
t
 ∣
∣
∣
∣
∞ |η♦(t)t|∞.

Taking derivatives, we easily see that

|η◦|∞ = η◦(1) = 1, |η♦(t)t|∞ = 2/e.

It remains to bound |(h(t) − hH (t))/t|∞. By (1.5),

(B.35) hH (t) = ∫ ∞

t
2 h(ty−1) sin(H log y)
π log y dy
y = ∫ ∞

−H log 2
t h ( t
ew/H
 ) sin w
πw dw.

The sine integral
 Si(x) = ∫ x

0
 sin t
t dt

is deﬁned for all x; it tends to π/2 as x → +∞ and to −π/2 as x → −∞ (see
[AS64, (5.2.25)]). We apply integration by parts to the second integral in (B.35),
and obtain

hH (t) − h(t) = − 1
π
 ∫ ∞

−H log 2
t
 ( d
dw h ( t
ew/H
 )) Si(w)dw − h(t)

= − 1
π
 ∫ ∞

0
 ( d
dw h ( t
ew/H
 )) (Si(w) − π
2
 ) dw

− 1
π
 ∫ 0

−H log 2
t
 ( d
dw h ( t
ew/H
 )) (
Si(w) + π
2
 ) dw.

Now ∣
∣
∣
∣ d
dw h ( t
ew/H
 )∣
∣
∣
∣ = te−w/H

H
 ∣
∣
∣
∣h
′ ( t
ew/H
 )∣
∣
∣
∣ ≤ t|h′|∞
Hew/H .

Integration by parts easily yields the bounds | Si(x) − π/2| < 2/x for x > 0 and
| Si(x) + π/2| < 2/|x| for x < 0; we also know that 0 ≤ Si(x) ≤ x < π/2 for
x ∈ [0, 1] and −π/2 < x ≤ Si(x) ≤ 0 for x ∈ [−1, 0]. Hence

|hH (t) − h(t)| ≤ 2t|h′|∞
πH
 (∫ 1

0
 π
2 e
−w/H dw + ∫ ∞

1
 2e−w/H

w dw
)

= t|h
′|∞ · ((1 − e
−1/H ) + 4
π E1(1/H)
H
 ) ,

where E1 is the exponential integral

E1(z) = ∫ ∞

z
 e−t

t dt.

MAJOR ARCS FOR GOLDBACH’S PROBLEM 77

By [AS64, (5.1.20)],
 0 < E1(1/H) < log(H + 1)
e1/H ,

and, since log(H +1) = log H +log(1+1/H) < log H +1/H < (log H)(1+1/H) <
(log H)e1/H for H ≥ e, we see that this gives us that E1(1/H) < log H (again
for H ≥ e, as is the case). Hence

(B.36) |hH(t) − h(t)|
t < |h
′|∞ · (1 − e
− 1
H + 4
π log H
H
 ) < |h
′|∞ · 1 + 4
π log H
H ,

and so, by (B.34),

|η+|∞ ≤ 1 + 2
e
 ∣
∣
∣
∣ h(t) − hH (t)
t
 ∣
∣
∣
∣
∞ < 1 + 2
e |h
′|∞ · 1 + 4
π log H
H .

By (B.11) and interval arithmetic, we determine that

(B.37) |h
′|∞ = |h
′(α2,2)| ≤ 2.805820379671,

where α2,2 is a root of h′′(x) = 0 as in (B.11). We have proven

(B.38) |η+|∞ < 1 + 2
e · 2.80582038 · 1 + 4
π log H
H < 1 + 2.06440727 · 1 + 4
π log H
H .

We will need three other bounds of this kind, namely, for η+(t) log t, η+(t)/t
and η+(t)t. We start as in (B.34):

(B.39)
 |η+ log t|∞ ≤ |η◦ log t|∞ + |(h(t) − hH(t))η♦(t) log t|∞
≤ |η◦ log t|∞ + |(h − hH (t))/t|∞|η♦(t)t log t|∞,

|η+(t)/t|∞ ≤ |η◦(t)/t|∞ + |(h − hH (t))/t|∞|η♦(t)|∞

|η+(t)t|∞ ≤ |η◦(t)t|∞ + |(h − hH (t))/t|∞|η♦(t)t2|∞.

By the bisection method with 30 iterations, implemented with interval arithmetic,

|η◦(t) log t|∞ ≤ 0.279491, |η♦(t)t log t|∞ ≤ 0.3811561.

Hence, by (B.36) and (B.37),

(B.40) |η+ log t|∞ ≤ 0.279491 + 1.069456 · 1 + 4
π log H
H .

By the bisection method with 32 iterations,

|η◦(t)/t|∞ ≤ 1.08754396.

(We can also obtain this by solving (η◦(t)/t)′ = 0 symbolically.) It is easy to
show that |η♦|∞ = 1/
√e. Hence, again by (B.36) and (B.37),

(B.41) |η+(t)/t|∞ ≤ 1.08754396 + 1.70181609 · 1 + 4
π log H
H .

By the bisection method with 32 iterations,

|η◦(t)t|∞ ≤ 1.06473476.

Taking derivatives, we see that |η♦(t)t2|∞ = 33/2e−3/2. Hence, yet again by
(B.36) and (B.37),

(B.42) |η+(t)t|∞ ≤ 1.06473476 + 3.25312 · 1 + 4
π log H
H .

78 H. A. HELFGOTT

References

[AS64] M. Abramowitz and I. A. Stegun. Handbook of mathematical functions with formulas,
graphs, and mathematical tables, volume 55 of National Bureau of Standards Applied
Mathematics Series. For sale by the Superintendent of Documents, U.S. Government
Printing Oﬃce, Washington, D.C., 1964.
[BBO10] J. Bertrand, P. Bertrand, and J.-P. Ovarlez. Mellin transform. In A. D. Poularikas,
editor, Transforms and applications handbook. CRC Press, Boca Raton, FL, 2010.
[BM98] Martin Berz and Kyoko Makino. Veriﬁed integration of ODEs and ﬂows using diﬀer-
ential algebraic methods on high-order Taylor models. Reliab. Comput., 4(4):361–369,
1998.
[Boo06] A. R. Booker. Turing and the Riemann hypothesis. Notices Amer. Math. Soc.,
53(10):1208–1211, 2006.
[dB81] N. G. de Bruijn. Asymptotic methods in analysis. Dover Publications Inc., New York,
third edition, 1981.
[GR00] I. S. Gradshteyn and I. M. Ryzhik. Table of integrals, series, and products. Aca-
demic Press Inc., San Diego, CA, sixth edition, 2000. Translated from the Russian,
Translation edited and with a preface by Alan Jeﬀrey and Daniel Zwillinger.
[Har66] G. H. Hardy. Collected papers of G. H. Hardy (Including Joint papers with J. E.
Littlewood and others). Vol. I. Edited by a committee appointed by the London
Mathematical Society. Clarendon Press, Oxford, 1966.
[HB79] D. R. Heath-Brown. The fourth power moment of the Riemann zeta function. Proc.
London Math. Soc. (3), 38(3):385–422, 1979.
[Hela] H. A. Helfgott. Major arcs for Goldbach’s problem. Preprint. Available at
arXiv:1203.5712.
[Helb] H. A. Helfgott. Minor arcs for Goldbach’s problem. Preprint. Available as
arXiv:1205.5252.
[Helc] H. A. Helfgott. The Ternary Goldbach Conjecture is true. Preprint.
[HL23] G. H. Hardy and J. E. Littlewood. Some problems of ‘Partitio numerorum’; III: On
the expression of a number as a sum of primes. Acta Math., 44(1):1–70, 1923.
[IK04] H. Iwaniec and E. Kowalski. Analytic number theory, volume 53 of American Math-
ematical Society Colloquium Publications. American Mathematical Society, Provi-
dence, RI, 2004.
[Kad05] H. Kadiri. Une r´egion explicite sans z´eros pour la fonction ζ de Riemann. Acta Arith.,
117(4):303–339, 2005.
[Kn¨u99] O. Kn¨uppel. PROFIL/BIAS, February 1999. version 2.
[Leh66] R. Sherman Lehman. On the diﬀerence π(x) − li(x). Acta Arith., 11:397–410, 1966.
[McC84] K. S. McCurley. Explicit estimates for the error term in the prime number theorem
for arithmetic progressions. Math. Comp., 42(165):265–285, 1984.
[MV07] H. L. Montgomery and R. C. Vaughan. Multiplicative number theory. I. Classical
theory, volume 97 of Cambridge Studies in Advanced Mathematics. Cambridge Uni-
versity Press, Cambridge, 2007.
[Ned06] N. S. Nedialkov. VNODE-LP: a validated solver for initial value problems in ordinary
diﬀerential equations, July 2006. version 0.3.
[OLBC10] F. W. J. Olver, D. W. Lozier, R. F. Boisvert, and Ch. W. Clark, editors. NIST hand-
book of mathematical functions. U.S. Department of Commerce National Institute
of Standards and Technology, Washington, DC, 2010. With 1 CD-ROM (Windows,
Macintosh and UNIX).
[Olv58] F. W. J. Olver. Uniform asymptotic expansions of solutions of linear second-order dif-
ferential equations for large values of a parameter. Philos. Trans. Roy. Soc. London.
Ser. A, 250:479–517, 1958.
[Olv59] F. W. J. Olver. Uniform asymptotic expansions for Weber parabolic cylinder func-
tions of large orders. J. Res. Nat. Bur. Standards Sect. B, 63B:131–169, 1959.
[Olv61] F. W. J. Olver. Two inequalities for parabolic cylinder functions. Proc. Cambridge
Philos. Soc., 57:811–822, 1961.
[Olv65] F. W. J. Olver. On the asymptotic solution of second-order diﬀerential equations hav-
ing an irregular singularity of rank one, with an application to Whittaker functions.
J. Soc. Indust. Appl. Math. Ser. B Numer. Anal., 2:225–243, 1965.

MAJOR ARCS FOR GOLDBACH’S PROBLEM 79

[Olv74] F. W. J. Olver. Asymptotics and special functions. Academic Press [A subsidiary of
Harcourt Brace Jovanovich, Publishers], New York-London, 1974. Computer Science
and Applied Mathematics.
[Plaa] D. Platt. Computing π(x) analytically. To appear in Math. Comp.. Available as
arXiv:1203.5712.
[Plab] D. Platt. Numerical computations concerning GRH. Preprint. Available at
arXiv:1305.3087.
[Pla11] D. Platt. Computing degree 1 L-functions rigorously. PhD thesis, Bristol University,
2011.
[Ros41] B. Rosser. Explicit bounds for some functions of prime numbers. Amer. J. Math.,
63:211–232, 1941.
[Tem10] N. M. Temme. Parabolic cylinder functions. In NIST handbook of mathematical func-
tions, pages 303–319. U.S. Dept. Commerce, Washington, DC, 2010.
[Tru] T. S. Trudgian. An improved upper bound for the error in the zero-counting formulae
for Dirichlet L-functions and Dedekind zeta-functions. Preprint.
[Tuc11] W. Tucker. Validated numerics: A short introduction to rigorous computations.
Princeton University Press, Princeton, NJ, 2011.
[Tur53] A. M. Turing. Some calculations of the Riemann zeta-function. Proc. London Math.
Soc. (3), 3:99–117, 1953.
[TV03] N. M. Temme and R. Vidunas. Parabolic cylinder functions: examples of error
bounds for asymptotic expansions. Anal. Appl. (Singap.), 1(3):265–288, 2003.
[Vin37] I. M. Vinogradov. Representation of an odd number as a sum of three primes. Dokl.
Akad. Nauk. SSR, 15:291–294, 1937.
[Wed03] S. Wedeniwski. ZetaGrid - Computational veriﬁcation of the Riemann hypothesis.
Conference in Number Theory in honour of Professor H. C. Williams, Banﬀ, Alberta,
Canada, May 2003.
[Whi03] E. T. Whittaker. On the functions associated with the parabolic cylinder in harmonic
analysis. Proc. London Math. Soc., 35:417–427, 1903.
[Wig20] S. Wigert. Sur la th´eorie de la fonction ζ(s) de Riemann. Ark. Mat., 14:1–17, 1920.
[Won01] R. Wong. Asymptotic approximations of integrals, volume 34 of Classics in Applied
Mathematics. Society for Industrial and Applied Mathematics (SIAM), Philadelphia,
PA, 2001. Corrected reprint of the 1989 original.

Harald Helfgott, ´Ecole Normale Sup´erieure, D´epartement de Math´ematiques,
45 rue d’Ulm, F-75230 Paris, France
E-mail address: harald.helfgott@ens.fr
