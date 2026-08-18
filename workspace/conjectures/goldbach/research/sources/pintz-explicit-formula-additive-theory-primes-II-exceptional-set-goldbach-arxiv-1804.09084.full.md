<!-- source: https://arxiv.org/pdf/1804.09084 | converted from PDF -->

arXiv:1804.09084v2  [math.NT]  30 Apr 2018A new explicit formula in the additive theory of
primes with applications II. The exceptional set in
Goldbach’s problem

by
J´anos Pintz
∗

Dedicated to the 60th birthday of Sz. Gy. R´ev´esz

1 Introduction

The ﬁrst non-trivial, although conditional, estimate for the exceptional set
(P denotes the set of primes)

(1.1) E = {2 | n; n ̸= p + p′, p, p′ ∈ P}

in Goldbach’s problem was achieved by Hardy and Littlewood [8] in 1924.
They showed under the Generalized Riemann Hypothesis (GRH) the esti-
mate

(1.2) E(X) = {n ≤ X; n ∈ E} ≪ε X 1/2+ε

for any ε > 0. This result is apart from the substitution of X ε by logc X by
Goldston [6] even today the best conditional result on GRH.
The basic result that almost all even integers are Goldbach numbers,
that is, can be represented as the sum of two primes, was proved by the aid
of Vinogradov’s method [21] in 1937/38 simultaneously and independently
by Van der Corput [19], ˇCudakov [3] and Estermann [5]. They showed

(1.3) E(X) ≪A X
(log X)A for any A > 0.

∗Supported by ERC-AdG. 321104 and National Research Development and Innovation
Oﬃce, NKFIH, K 119528.
 1

It is easy to see that (1.3), even any estimate of type

(1.4) E(2N ) < π(2N ) − 1 for N > N

implies Vinogradov’s three primes theorem [21] that every suﬃciently large
odd integer can be written as the sum of three primes.
The result (1.3) held the record for 35 years, when Vaughan [20] improved
it in 1972 to

(1.5) E(X) ≪ X exp(−c
√log X)
.

The breakthrough came just 3 years later when Montgomery and Vaughan
[16] showed that the estimate

(1.6) E(X) ≪δ X 1−δ

holds with an unspeciﬁed but explicitly calculable value δ > 0.
The problem, to show (1.6) with a not too small explicit value of δ turned
out to be very diﬃcult. It was shown in 1989 by J. R. Chen and M. Liu
[1] that (1.6) holds with δ = 0.05, ten years later by H. Z. Li [12] that also
δ = 0.079 is admissible. This was improved by him [13] to

(1.7) E(X) < X 0.914

for any X > X0, ineﬀective constant. Finally in 2010 Lu [14] succeeded to
show

(1.8) E(X) < X 0.879

for X > X2 ineﬀective constant.
The present work will be devoted to the proof of the following result.

Theorem 1. There is an ineﬀective constant X2 such that for X > X2

(1.9) E(X) < X 0.72.

The seemingly moderate size of the present work is still misleading con-
cerning the diﬃculties of the proof of Theorem 1. Namely, a crucial role
will be played in the proof by the results of part I of this series ([18]) which
is again heavily based on the results of another preparatory work ([17]).
Finally we mention that apart from the relatively short ﬁnal Section 9 all
results of the present work (in many cases in a reﬁned form) will be used in
later parts of this series to achieve further improvements over (1.9).

2

2 Notation. The role of the explicit formula

The explicit formula proved in part I ([18]) will play a central role in the
proof of Theorem 1; in fact, it serves as the basis for any further examination.
In order to formulate the explicit formula we ﬁrst need to introduce the
notation.
Let ε and ε0 be small positive numbers, X be a number large enough
(X > X0(ε, ε0)), and let us deﬁne

(2.1) X1 := X 1−ε0, e(u) := e
2πiu, S(α) := ∑

X1<p≤X log pe(pα),

where p, p′, pi will always denote primes. |M| will denote the cardinality of
the ﬁnite set M. We will deﬁne the major (M) and minor (m) arcs through
the parameters P and Q satisfying

(2.2) (log X)
C ≤ P ≤ X 4/9−ε, Q = X
P ,

(2.3) M = ⋃

q≤P
 ⋃

a
(a,q)=1
 [ a
q − 1
qQ , a
q + 1
qQ
 ] , m = [ 1
Q , 1 + 1
Q
 ] \ M.

We will examine the number of Goldbach decompositions of even num-
bers m ∈ [X/2, X] in the form

(2.4) R(m) = ∑

p+p′=m
p,p′≥X1
 log p · log p′ = R1(m) + R2(m),

where

(2.5) R1(m) = ∫

M
 S2(α)e(−mα)dα, R2(m) = ∫

m S2(α)e(−mα)dα.

The now standard treatment of the minor arcs (Parseval’s theorem and
the estimate of Vinogradov, reproved in a simpler way by Vaughan) gives

(2.6) |R2(m)| ≤ X
√log X for P ≤ X 2/5

apart from at most C X
P log10 X exceptional values m (see Section 5 of [18],
for example).
 3

In order to formulate the explicit formula for the major arcs in Gold-
bach’s problem we will deﬁne the set E = E(H, P, T, X) of generalized excep-
tional singularities of the functions L′/L for all primitive L-functions mod r,
r ≤ P , as follows (χ0 = χ0( mod 1) is considered as a primitive character
mod 1)
 (̺0, χ0) ∈ E if ̺0 = 1,(2.7)
 (̺i, χi) ∈ E if ∃χi, cond χi = ri ≤ P, L(̺i, χi) = 0,

βi ≥ 1 − H
log X , |γi| ≤ T,

where zeros of L-functions are denoted by ̺ = β + iγ = 1 − δ + iγ and cond χ
denotes the conductor of χ. Let further

A(̺) = 1 if ̺ = 1,(2.8)
 A(̺) = −1 if ̺ ̸= 1.

The expected main term of R1(m) is the well-known singular series of
Hardy and Littlewood, arising from the eﬀect of the pole of ζ(s) at s = 1:

(2.9) S(m) := S(χ0, χ0, m) := ∏

p|m
 (1 + 1
p − 1
 ) ∏

p∤m
 (1 − 1
(p − 1)2
 ) .

However, if we have zeros near to s = 1 then we necessarily have a num-
ber of secondary terms with coeﬃcients S(χi, χj, m) corresponding to the
primitive characters belonging to generalized exceptional zeros. We will call
these characters generalized exceptional characters, the corresponding sin-
gular series S(χi, χj, m) generalized exceptional singular series. They can
be expressed in a very complicated explicit form, proven in the Main Lemma
of part I ([18]). However, the important properties of it can be incorporated
into the following theorem, where we use the notation and conditions of the
present section.

Theorem A (Explicit formula). Let 0 < ε < ε0, ε < ϑ < 4
9 − ε be any
numbers, 2 | m ∈ [ X
2 , X]. Then there exists P ∈ (X ϑ−ε, X ϑ) such that for
X > X0(ε)

R1(m) = ∑

̺i∈E
 ∑

̺j ∈E A(̺i)A(̺j)S(χi, χj, m) Γ(̺i)Γ(̺j)
Γ(̺i + ̺j) m̺i+̺j−1(2.10)
 + O (Xe
−cH + X
√T + X 1−ε) ,

4

where the generalized singular series satisfy

(2.11) |S(χi, χj, m)| ≤ S(χ0, χ0, m) = S(m);

further for any η small enough

(2.12) |S(χi, χj, m)| ≤ η,

unless the following three conditions all hold,

(2.13) ri|C(η)m, rj|C(η)m, cond χiχj < η−3

where C(η) is a suitable constant depending only on η.
Its proof follows from Theorem 1 and Main Lemma 1 in part I [18].

Remark. A very important feature of the explicit formula is that the
number K of generalized exceptional zeros appearing in (2.10) is by log-free
zero density theorems (cf. Jutila [10]) bounded from above by

(2.14) K ≤ Ce
2H ,

so it is bounded by an absolute constant (depending on ε), if we choose H as
a suﬃciently large absolute constant depending on ε, which we suppose later
on in the proof of Theorem 1. Similarly, we will choose T as a suﬃciently
large constant depending on ε.

Although the quoted explicit formula is in general a good starting point
for the proof of

(2.15) R1(m) > εS(m)m

if ϑ is small enough, the argument breaks down in case of the existence of
a Siegel-zero, 1 − δ corresponding to L(s, χ1), in which case we might have
S(χ1, χ1, m) = −S(m) and we cannot show the crucial relation (2.15) if δ
is small enough. In this case the Deuring–Heilbronn phenomenon can help.
This case was worked out as Theorem 2 in part I [18] which we quote now
as

Theorem B. Let ε′ > 0 be arbitrary. If X > X(ε′), ineﬀective constant
and there exists a Siegel zero β1 of L(s, χ1) with

(2.16) β1 > 1 − h/ log X, cond χ1 ≤ X 4
9 −ε′,

where h is a suﬃciently small constant depending on ε′, then

(2.17) E(X) < X 3
5 +ε′.

5

Remark. We will choose ε′ = 10−3 here. Then in the proof of Theorem 1
we are entitled to suppose that all L(s, χ) functions mod r ≤ P satisfy

(2.18) L(s, χ) ̸= 0 for s ∈ [1 − c0/ log X, 1]

if we choose ϑ ≤ 0.44. In other words, we do not need to worry about
exceptional zeros 1− δ satisfying δ < c0/ log X with a small but ﬁxed c0 > 0.

The well-known relation (cf. [11], p. 46) (Re w, Re z > 0)

(2.19) Γ(w)Γ(z)
Γ(w + z) = B(w, z) =
 1∫

0 xw−1(1 − x)
z−1dx

tells us that
(2.20)
|B(̺i, ̺j)| ≤ |B(Re ̺i, Re ̺j)| = B(1, 1) + O(1/ log X) = 1 + O(1/ log X).

Hence, taking into account the relations (2.11)–(2.13) we see that the
estimation (2.15) will follow, if we can show

(2.21) ∑∗

̺i,̺j∈E
(̺i,̺j)̸=(1,1)
X −δi−δj < 1 − 2ε,

where the ∗ means that the additional condition (2.13) is satisﬁed for the
pairs (̺i, ̺j) of zeros in the summation.
The expression (2.21) can be estimated directly by density theorems
and the Deuring–Heilbronn phenomenon, as done in the earlier estimates
of Chen-Liu [1] and Hongze Li [12], [13], and Lu [14]. It also resembles
the well-studied problem of the Linnik-constant, with the seemingly major
disadvantage that

(†) the zeros do not belong to a ﬁxed modulus q ≤ P

but to a set of diﬀerent moduli ri ≤ P .
In what follows below, we will show that this disadvantage can be over-
whelmed thanks to the information (2.13) supplied by the explicit formula.
We will choose P0 = X ϑ+2ε, so our P will satisfy

(2.22) P ∈ [X ϑ+ε, X ϑ+2ε].

Thus the exceptional set arising from the minor arcs (2.6) will be o(X 1−ϑ).
Then we consider the set R of the K generalized exceptional zeros appearing

6

in (2.10) whose number K is bounded by an absolute constant depending
on ε,

(2.23) 0 ≤ K ≤ K(ε) − 1

according to (2.14) since we will choose H as a big constant depending on ε.
(If K = 0 we are ready.)
Let us choose now

(2.24) η = ε
K 2(ε) ,

and write

(2.25) C(η) = C1(ε).

In this case the total contribution of terms not satisfying (2.13) will be really
less than εX in (2.10), so (2.21) will really imply (2.15). Let us divide now
the even numbers m in [X/2, X] into at most 2|R| diﬀerent classes M(R′)
according to the subset R′ ⊂ R of zeros which belong to primitive characters
with moduli dividing C1(ε)m

(2.26) M(R
′) = {m ∈ [X/2, X], 2 | m, ri | C1(ε)m ⇔ ri ∈ R
′}.

(The subset might be empty for some R′ ⊂ R; for example, if ̺i ∈ R′,
̺j /∈ R′, ri = rj, or if l.c.m.
ri∈R′ [ri] > XC1(ε).)

Let us denote

(2.27) q(R
′) := l.c.m.[ri; ri ∈ R
′].

Now we can delete all classes M(R′) with

(2.28) q(R
′) > X ϑ,

since in this case clearly

(2.29) |M(R
′)| ≤ C1(ε)X 1−ϑ,

and the number of all classes is

(2.30) 2
|R| ≤ 2
K(ε) = C2(ε).

Let us ﬁx now any concrete class R′ with

(2.31) q := q(R
′) ≤ X ϑ.

7

Due to (2.30) it is suﬃcient to restrict our attention now for values m with

(2.32) m ∈ M(R
′).

Hence, by (2.21) it is suﬃcient to show for any q ≤ X ϑ

(2.33) S0 = ∑∗∗

̺i,̺j∈E
(̺i,̺j)̸=(0,0)
q−A(δi+δj ) < 1 − 2ε

where A = 1/ϑ and the notation ∗∗ abbreviates now the condition

(2.34) ri | q, rj | q, cond (χiχj) < C0(ε) (= ε3

K 6(ε)
 ) .

Thus we managed to get rid of the condition (†), and it is suﬃcient to
consider characters modulo the same q ≤ X ϑ. Further advantages compared
to the earlier treatments ([1], [12], [13], [14]) are that
(i) both zeros ̺i and ̺j run only through zeros with a bounded height
|γ| ≤ T (ε) and
(ii) the second zero ̺j runs for every ﬁxed ̺i only through zeros belonging
to characters χj with

(2.35) cond (χiχj) < C0(ε).

Since zeros of L(s, χ) and L(s, χ) are conjugate it will be simpler for us
to change the condition (2.35) to consider further on the inequality

(2.36) S0 = ∑′ q−A(δi+δj ) < 1 − 2ε

where the condition ∑′ will mean later on

(2.37) (1, 1) ̸= (̺i, ̺j) ∈ E, ri | q, rj | q, cond (χiχj) < C0(ε).

This form makes the quasi-diagonal form of S0 clear: only those pairs of
zeros count where the relevant primitive characters are the same up to a
character with a bounded conductor.
Let us use further on the notation (this will change the values of H and
T by a factor A)

(2.38) log q = L, λi = δiL ≤ H, |µi| = |γiL| ≤ T.

Then we can rewrite S0 as

(2.39) S0 = ∑′ e
−A(λi+λj).

8

According to (2.37) we will say that two generalized exceptional char-
acters χ and χ′ are equivalent, in notation χ ∼ χ′ if there is a chain of
generalized exceptional characters χν (ν = 1, 2, . . . , n) such that χ1 = χ,
χn = χ′

(2.40) cond (χνχν+1) < C0(ε) for ν = 1, . . . , n − 1.

Such a chain has at most K ≤ K(ε) characters in it; hence if χ and χ′ are
equivalent, then

(2.41) cond (χ, χ′) < C3(ε) = C0(ε)
K(ε)−1.

We remark here that since by Davenport [4], Ch. 14

(2.42) δ ≫ 1
√q log2 q ,

there is no generalized exceptional character χ ∼ χ0( mod 1), so the sum S0
in (2.39) in fact does not contain any pair of singularities (1, ̺), just pairs of
zeros. In such a way we can distribute the generalized exceptional zeros into
M (≤ K) classes according to the equivalence classes Hν (ν = 1, 2, . . . M )
of the generalized exceptional characters. Thus we obtain

(2.43) S0 ≤ S :=
 M∑

ν=1 S2
ν ,

where Sν denotes the quantity

(2.44) Sν := ∑

̺ν,j ∈E, χν,j∈Hν e
−Aλν,j .

According to this it will be important to introduce (and later estimate)
the quantities

(2.45) N (Λ) = ∑

̺i∈E, λ≤Λ 1

and

(2.46) Nν(Λ) = ∑

χ∈Hν , λ=λχ≤Λ 1, ̃N (Λ) = max
ν Nν (Λ).

9

3 Methods

The reduction to zeros corresponding to characters modulo a ﬁxed q ≤ P , the
fact that it is suﬃcient to consider zeros with bounded height and the quasi-
diagonal form (2.37) of the critical sum (2.33) are all new features compared
with the earlier methods applied to the exceptional set in the previous works
(cf. [1], [12], [13], [14]). A further advantage is that (2.33) shows now strong
similarities to the case of the estimation of Linnik’s constant; in fact, it looks
like a “two-dimensional” variant of Linnik’s problem. This gives hope to
apply the very powerful methods and/or results of Heath-Brown [9] used by
him to achieve the huge improvement L ≤ 5.5 in the estimation of Linnik’s
constant compared to the earlier result L = 13.5 of Chen and Liu [2].
The estimation of (2.33) will be based on the following three principles,
mentioned and used by Heath-Brown [9].
Principle 1. Zero-free region for ∏

χ( mod q) L(s, χ).

Principle 2. Deuring–Heilbronn phenomenon.
Principle 3. ‘Log-free’ zero density estimates.

For the proof of the result E(X) < X 1−ϑ it will suﬃce to take over from
Heath-Brown’s work [9] a small part of his results concerning Principles 1
and 2 (see Theorems E, F, G in our next section) partially in the form
improved by Xylouris [22]. In the forthcoming papers, when proving sharper
inequalities for E(X) we will need much more results of this type and in
many cases in somewhat stronger form.
On the other hand, the zero density estimates of [9], as well as some
similar ones of others, used in earlier examination of Linnik’s problem do
not suite for our purposes.
Heath-Brown starts, namely, with a weighted average over primes, which
does not seem to work in Goldbach’s problem. Since in this way in Linnik’s
problem zeros of the same L-function can be treated together, it is suﬃcient
to estimate the number of L-functions mod q, having at least one zero in
a given range, instead of the total number of zeros in the relevant range
as in case of usual density theorems. The corresponding density theorems
of Chen–Liu [1] and H. Z. Li [12], [13] and Lu [14] are far too weak as to
yield Theorem 1. Therefore we will show a new log-free density theorem
(Theorem C) which counts all zeros and is still just slightly weaker than the
corresponding result of Heath-Brown [9], Lemma 11.1 which counts only the
number of L-functions belonging to these zeros.
Another invention of Heath-Brown [9] is the proof of a ‘new density
theorem’, his Lemma 12.1, which works only for zeros very near to the line

10

σ = 1 (approximately in the region σ > 1 − 5/(4 log q)). This result can also
be extended for the number of L-functions having at least one zero in the
relevant range. The method of proof of this result is nearer to the proof of
the Deuring–Heilbronn phenomenon than to that of the density theorems.
Concerning this result we succeeded in modifying the proof in such a way as
to yield the same estimate without any loss for the total number of zeros (cf.
Theorems H and I). In another version of this method we can directly prove
a weighted density theorem, essentially for the weights appearing in (2.33)
which is even more useful than unweighted density theorems (cf. Theorem
J). A new feature of our case is (which does not appear in Linnik’s problem)
that we need density theorems for zeros of a restricted class of L-functions
belonging to equivalent characters (cf. (2.40), (2.41) and (2.46)). The usual
proofs for density theorems naturally work for these cases as well, and they
usually yield somewhat stronger results in this case, like a comparison of
Corollaries 1 and 2 show in the next section. However, an improvement
of the technique applied by Heath-Brown in the proof of his new density
theorem allows us to reach drastic improvements for the number of zeros
in one equivalence class (Nν(Λ)) compared with the case of all L-functions
(N (Λ)). In the range σ > 1−5/(4 log q) (⇔ λ < 5/4), for example, we obtain
at most 7 zeros for one class, instead of the bound more than a hundred,
supplied by the old or new density theorems of Heath-Brown (cf. [9], Tables
12 and 13) for the number of all L-function having at least one zero in the
same range. A further advantage of this method is that the bounds obtained
in this way for Nν (Λ) remain valid in the much wider range σ > 1 − 6/ log q.
After this, the contribution of zeros with λ > 6 can be estimated already
very eﬃciently by Corollary 2.

4 Auxiliary results

In the present section we will list the needed auxiliary theorems for the
estimation of the crucial quantity for S0 in (2.33). These auxiliary theorems
give important information about the distribution of zeros of L-functions
near to s = 1.
The ﬁrst one is a weighted density theorem which is the generalization
of Heath-Brown’s Lemma 11.1 [9] for the case when we estimate the total
number of zeros instead of the number of L-functions having at least one
zero in the given region. The result will have two diﬀerent versions according
to which we consider all L-functions or just a class of similar L-functions in

11

the sense of Theorem D.

Theorem C. Let C ′, ε, c1, c2, Λ > 0 be given, q ≥ q(ε, c1, c2, C ′, κ),
(4.1)

Λ∞ = 1
3 log log L, ϕ ≥ max
χ( mod q) ϕ(χ), r = ϕ + c1 + c2
3 , x0 = 2ϕ + 3c1 + c2,

(4.2) w(̺) = w(1 − L(λ + iµ)
) = e
−2(x0+κ)λ− r+κ
2 d, d = max(0, Λ − λ).

Then we have with an absolute constant C depending on C ′

(4.3) ∑

̺=̺χ, χ( mod q)
λ≤Λ∞
|µ|≤C′
 w(̺) ≤ (1 + Cε)C1√Bϕ,κ(Λ)Bϕ,r(Λ)/κ = C2(ϕ, κ, Λ)(1 + Cε),

where

(4.4) C1 = 2ϕ + 2c1 + c2
2c1c2 ,

(4.5) Bϕ,ω(y) = ϕ
2
 ( 1 − e−2ωy

y
 ) + ( 1 − e−ωy

y
 )2 .

Theorem D. Suppose that K is a set of characters χi mod q with the con-
dition that for all pairs χi, χj ∈ K

(4.6) cond (χiχj) ≤ qε.

Further let us suppose the conditions of Theorem C with

(4.7) x0 = ϕ + 3c1 + c2, ϕ ≥ max
χ∈K ϕ(χ).

Then (4.3) holds if the sum is restricted for zeros of L(s, χ), χ ∈ K.

Remark 1. Although the estimate on the right-hand side of (4.3) remained
unchanged, the new estimate is stronger, since the new weights will be larger,
due to the smaller choice of x0 in (4.7).
Choosing c1 = 1/12, c2 = 1/4, ϕ = 1/3, κ = 1/6, (C1 = 26) we are led
to the following results (to be used in Section 9).

12

Corollary 1. Let Λ0 = 1.311, Λ1 = 2.421, Λ2 = 3.96, Λ3 = 5.8, E0 =
22.281, E1 = 15.6, E2 = 10.4, E3 = 7.01. Then we have for i = 0, 1, 2:

(4.8) ∑

λ≤Λ∞ e
− 8
3 λ− 5
12 max(0,Λ−λ) < Ei for Λ ≥ Λi,

(4.9) ∑

χ∈K
λ≤Λ∞
 e
−2λ− 5
12 max(0,Λ−λ) < Ei for Λ ≥ Λi.

Corollary 2. With the notation of (2.45)–(2.46) and Corollary 1 we have

(4.10) N (Λ) < Eie
8Λ/3 for Λ ≥ Λi,

(4.11) Nν(Λ) < Eie
2Λ for Λ ≥ Λi.

Remark. Since the functions Bϕ,ω(y) are monotonically decreasing in y for
all non-negative values of the parameters ϕ and a, the estimates Ei arising
from Λi are valid for all Λ ≥ Λi.

The results listed as Theorems E, F, G below are Theorem 1 of Xylorius
and Theorems 2 and 4 (more precisely Lemma 8.8) of Heath-Brown [9] with
the only change that the condition |γ| ≤ 1 for the zeros can be substituted
without any essential change in the proof for |γ| ≤ T if q > q0(T ). (T is in
our case a large constant depending on ε.) Thus in the following theorems
let ε, T be positive constants,

(4.12) M (s) = ∏

χ( mod q) L(s, χ),

(4.13) R(α, T ) = {
s; σ ≥ 1 − α
log q , |t| ≤ T }

and let us suppose that q > q0(T, ε).

Theorem E. M (s) has at most one zero in R(0.44, T ). Such a zero, if it
exists, is real and simple and corresponds to a non-principal character.

Theorem F. M (s) has at most two zeros, counted according to multiplicity,
in R(0.702, T ).
Remark. Heath-Brown [9] proved this with 0.696 in place of 0.702. The
small improvement is due to Xylouris [22, Tabellen 2, 3 and 7].

13

Theorem G. Suppose that χ is a real non-principal character mod q with

(4.14) L (1 − λ
log q , χ) = 0, 0 < λ ≤ 0.44.

Then M (s) has only the zero 1−λ/ log q in the region R(Λ(λ), T )∪R(1.18, T )

(4.15) Λ(λ) = min {( 12
11 − ε
) log 1
λ , 1
3 log log log q} .

The fact that M (s) has no other zeros in R(Λ(λ), T ) is exactly Lemma
8.8 of Heath-Brown [9]. The absence of other zeros in R(1.18, T ) follows
from Tables 4 and 7 of Heath-Brown [9] (pp. 298, 301), which follow from
his Lemmas 8.3 and 8.7, respectively.
In the following we will formulate the new density theorems which are
improved forms of Lemma 12.1 of Heath-Brown [9]. Although in the ap-
plication we will work (unlike Heath-Brown) with a concrete function we
will formulate the result more generally, similarly to [9]. (The following
condition is the same as Conditions 1 and 2 of [9] together.)

Condition 1. Let f be a non-negative continuous function from [0, ∞) to
R, supported in [0, t0), twice diﬀerentiable on (0, t0) with f ′′ continuous and
bounded. Suppose that its Laplace transform

(4.16) F (z) =
 t0∫

0
 e
−ztf (t)dt

satisﬁes

(4.17) Re F (z) ≥ 0 for Re z ≥ 0.

We will work with the following pair of functions, satisfying Condition 1
(which appears in Lemma 7.2 of [9])

(4.18) g(u) = 1
30 (2 − u)
3(4 + 6u + u2) with u ∈ [0, 2]

G(z) =
 2∫

0 e
−zug(u)du(4.19)
 = 16
15z − 8
3z3 + 4
z4 − 4
z6 + 4e−2z

z4
 ( z + 1
z
 )2 .

14

The explicit form of G(z) follows simply by computation. Further (cf. [9],
Lemma 7.2)

(4.20) g = h ∗ h, where h(t) = 1 − t2, −1 ≤ t ≤ 1.

Therefore we have

(4.21) Re(G(iy)) =
 2∫

0 g(u) cos(uy)du = 2
( 1∫

0 h(t) cos ty dt)2 ≥ 0.

Finally, from Lemma 4.1 of [9] (see also p. 279 of [9]) we have by (4.21)

(4.22) Re G(z) ≥ 0 for Re z ≥ 0.

Instead of the concrete functions g(u) and G(z) above we will use a
one-parameter family of functions:

(4.23) f = fx(u) = xg(ux), ux ∈ [0, 2] ⇔ u ∈ [0, 2
x
 ]

F = Fx(z) =
 2/x∫

0 e
−zufx(u)du =
 2/x∫

0 e
− z
x uxg(ux)xdu(4.24)
 =
 2∫

0
 e
− z
x vg(v)dv = G
( z
x
 ).

An easy calculation shows (cf. Lemma 7.2 of [9])

(4.25) f (0) = 16x
15 , F (0) = G(0) = 8
9 , F (−x) = G(−1) = 8
5 .

In the applications (Theorems I, H, J) the following additional property
of the functions F will have importance, which is satisﬁed for G(z) for
A0 = 13, B0 = 1.25, for example.

Condition 2. There are non-negative constants A0 and B0 such that for
any t ∈ R

(4.26) Re G(a + it)
G(a) ≥ Re G(−b + it)
G(−b)

15

if

(4.27) 0 ≤ a ≤ A0, 0 ≤ b ≤ B0.

Remark. Let us take A0, B0 arbitrary, non-negative constants, η > 0 ﬁx.
Then for η ≤ a ≤ A0, 0 ≤ b ≤ B0, |t| > t0(η, A0, B0) we have from (4.19)

(4.28) Re G(a + it)
G(a) > c(A0, η)
t2 > − c′(B0)
t2 > Re G(−b + it)
G(−b)

with positive constants c(A0, η), c′(B0).
This shows already that Condition 2 can be veriﬁed for the G function in
(4.19) by the aid of computers for concrete values of A0 and B0 (consequently
for the F -functions in (4.24) if x, A0 and B0 are given).
This preparation makes possible to formulate the remaining 3 density
theorems. In these theorems we will use the notation (2.45)–(2.46), where
in (2.46) we can ease the condition of equivalent characters without any loss
for the ﬁnal estimate. Let T > 0, ε > 0 be constants, q > q(T, ε), L = log q;
zeros of L-functions belonging to characters χ mod q with ϕ ≥ max ϕ(q)
will be denoted (cf. (2.38)) as

(4.29) ̺ := ̺χ := 1 − δ + iγ, λ := δL, µ := γL.

Suppose that with a λ0 ≥ 0 we have for all zeros of all L(s, χ), χ mod q

(4.30) λ ≥ λ0.

We will use the following notation with λ = λj ≤ Λ:
(4.31)
F (λj − λ0)
F (−λ0) = ψj, F (Λ − λ0)
F (−λ0) = ψ, f (0)ϕ
2F (−λ0) = ξ, ∆ = ψ − ξ > 0.

Theorem H. Suppose that f and F satisfy Conditions 1 and 2. Let 0 ≤
λ0 ≤ B0(F ), 0 ≤ Λ − λ0 ≤ A0(F ), ∆2 > ξ + ε. Then

(4.32) N (Λ) := NT (Λ) = ∑

|γ|≤T, λ≤Λ 1 ≤ 1 − ξ
∆2 − ξ − ε .

Theorem I. Suppose that H is a set of characters χ mod q with the property

(4.33) cond (χχ′) ≤ qε for χ, χ′ ∈ H.

16

Then with the conditions of Theorem H we have

(4.34) ̃N (Λ) = NT,H(Λ) = ∑

χ∈H
|γχ|≤T, λχ≤Λ
 1 ≤ 1 + ε
∆2 .

The following Theorem J will enable us to estimate directly weighted
sums over zeros, which arise in our problem. This method partly reduces
drastically the needed amount of calculations and also yields better esti-
mates for the weighted sums than the usual treatment via partial summa-
tion (which cannot be performed easily in these cases due to the complicated
forms of the upper bounds). Further on we will suppose the Conditions of
Theorem H and additionally the existence of two constants B and C with

(4.35) B > max(
C, t0(f )
) ≥ 0

where t0 = t0(f ) is deﬁned in Condition A by f (t) = 0 for t ≥ t0.
First we state

Theorem J. Under the conditions of Theorem H we have

(4.36) D(Λ) := ∑

|γj|≤T, λj ≤Λ(ψj − ψ) ≤ 1 − ξ + O(ε)
2∆ .

Suppose that F satisﬁes Condition A, d0 and C ′ are given and with the
J unknown variables d0 ≥ d1 ≥ · · · ≥ dJ ≥ 0 (dj = Λ − λj, j = 0, . . . , J) we
know the upper bound

(4.37) D∗(d0) = ∑

j≤J
(
F (d0 − dj) − F (d0)
) ≤ C ′.

We are interested in the maximal value of the quantity

(4.38) S∗ = ∑

j≤J
(e
Bdj − e
Cdj ), B > C ≥ 0,

under the additional constraint with given {ej}J
1

(4.39) dj ≤ ej, e1 ≥ e2 ≥ · · · ≥ eJ .

In this case we can ﬁnd the maximum of S∗ with a type of greedy algorithm
as follows. Suppose that 1 ≤ r ≤ J is deﬁned as

(4.40)
 r−1∑

j=1
(
F (d0 − ej) − F (d0)
) ≤ C ′ <
 r∑

j=1
(
F (d0 − ej) − F (d0)
).

17

Theorem K. Under the above conditions the optimal choice is (r = 1 is
possible too, when (4.41) is void) to choose

(4.41) dj = ej for j = 1, 2, . . . , r − 1

and dr as the unique value with

(4.42) F (d0 − dr) = F (d0) + C ′ −
 r−1∑

j=1
(F (d0 − ej) − F (d0)
).

Further, we choose dν = 0 for r < ν ≤ J.

Remark 1. If there is no r ∈ (1, J) with (4.40), that is

(4.43)
 J∑

j=1
(
F (d0 − ej) − F (d0)
) ≤ C ′,

then the maximum of S∗ is clearly given by the choice ej = dj for 1 ≤ j ≤ J.

Remark 2. By the fact that F is strictly monotonically decreasing if f (t)
is not identically 0, we obtain from (4.42) that dr is completely determined
and 0 ≤ dr ≤ er due to F (d0 − er) ≥ F (d0 − dr) ≥ F (d0).

Remark 3. Theorem K itself refers to arbitrary numbers but in the appli-
cations we will use it with

(4.44) dj = Λ − λj, d0 = Λ − λ0, C ′ = F (−λ0) 1 − ξ + Cε
2∆

in conjunction with estimate (4.36) of Theorem J. Although Theorem K
itself does need only Condition 1 for F , Theorem J needs both Conditions 1
and 2.

Remark 4. The conditions di ≤ ei, i = 1, . . . J imply J inequalities of the
type (m = 1, 2, . . . , J)

(4.45) D∗(d0, m) = ∑

j≤m

(F (d0 − dj) − F (d0)
) ≤ C ′
0(m)

with

(4.46) C ′
0(m) := C ′
0(m; {ej }) = ∑

j≤m

(F (d0 − ej) − F (d0)
).

Although it is not necessary for application in the present work (just in later
parts of this series) we will examine the more general case when in place of

18

the conditions di ≤ ei we will have more generally a ﬁnite sequence of M
inequalities (d1 ≥ · · · ≥ dM ≥ 0)

(4.47) ̃D(d0, m) = ∑

j≤m F (d0 − dj) ≤ c
′(m) = c(m) + mF (d0)

where c(m) ≥ c(m − 1) is an increasing sequence of real numbers satisfying
for m = 2, . . . M − 1

(4.48) c(m + 1) − c(m) ≤ c(m) − c(m − 1).

(If there exists an m0 = min{ν; c(ν) < 0}, then the system consists of at
most m0 − 1 elements. In this case we cancel the inequalities with index
≥ m0, which is equivalent to the condition M = m0 − 1, c(j) ≥ 0 for
j = 1, . . . , M .)

Theorem L. Under the above conditions the maximum of S∗ in (4.38) (with
M = J) is achieved for the uniquely determined sequence {dm}M
m=1 for which
equality holds in (4.47) for all m = 1, . . . , M .

Remark 5. If we add at the end some terms dm = 0 with m > M this
does not change the value of S∗, so allowing some extra conditions with
M < m ≤ R (R a ﬁxed large constant) c(m) = c(M ), will deﬁnitely not
decrease the maximum. In this way we can work in the applications with
an a priori determined (large but bounded) number M of variables (since
we know that in our application the number of zeros with λj ≤ λ satisﬁes
a bound depending on λ – see e.g. Corollary 2) and the obtained upper
bound for the new (extended) sum S∗ will constitute an upper bound for
the original S∗.

Remark 6. As we substituted the conditions di ≤ ei by its consequence
(4.45)–(4.46) this may theoretically increase the maximum value S∗. How-
ever, Theorem L tells us that this is not the case since for the maximum
conﬁguration {di} we will in fact have di = ei for i ≤ J, since all the
inequalities (4.45) are sharp.

5 Proof of Theorems C and D

In this section we will prove Theorems C and D. The ﬁrst part of the proof
will be very similar to the proof presented in Section 3 of [17] which follows
the works of Heath-Brown [9] and Graham [7]. The second part of the proof
will use also ideas of Heath-Brown [9], however not from the proof of the
corresponding density theorem, but from Section 13 of [9].

19

Following more closely [9] and slightly diﬀerent from (3.14) of [17] we
will use the notation
(5.1)= qu, U0 = qu0, V = qv, W = qw, X1 = qx1, X = qx, X0 = qx0, U = U L2,

(5.2) ε1 = ε
2/100, w = c1 − ε, v = u + c2, x0 = u0 + r,

x1 = x0 + κ, u = u0 + η, x = x0 + η, 0 ≤ η ≤ κ.

Further, in case of Theorem C, we will choose

(5.3) u0 = ϕ + 2c1, x0 = 2ϕ + 3c1 + c2, r = ϕ + c1 + c2,

whereas in case of Theorem D we set

(5.4) u0 = 2c1, x0 = ϕ + 3c1 + c2, r = ϕ + c1 + c2.

Similarly to [17] and [9] we will use Graham’s weights

ψd =
 



µ(d) for 1 ≤ d ≤ U
µ(d) log(V /d)
log(V /U ) for U ≤ d ≤ V

0 for d ≥ V
 ,(5.5)
 θd =
 {
µ(d) log W/d
log W for 1 ≤ d ≤ W

0 for d ≥ W ,(5.6)

(5.7) Ψ(n) = ∑

d|n ψd, ϑ(n) = ∑

d|n θd,

further, the functions

F (s) = ∑

i≤V, j≤W ψiθjχ(([i, j])
)[i, j]
−s, Gq(s) = ∑

i≤W, j≤W θiθj[i, j]
−s,

(5.8)

S(Y ) =
 ∞∑

n=1 Ψ(n)ϑ(n)χ(n)n−̺e
−n/Y = 1
2πi
 ∫

(1)
 L(s + ̺, χ)F (s + ̺)Γ(s)Y sds,

(5.9)
 20

where [i, j] denotes the least common multiple of i and j (Re ̺ = β). We
move the line of integration in (5.9) to Re s = 1 − β − 1/k with k = ⌈4ε−1⌉,
and obtain analogously to p. 318 of [9] the estimate
(5.10)
S(X) ≪ (qϕV W X −1)
1/kq1/k2L3X 1−β ≪ (qϕV W X −1)
1/kq 2
k2 −ε1 ≪ q−ε1

in view of 1 − β ≤ ε1/x, F (s + ̺) ≪ ∑

n≤V W d2(n)n−1+1/k ≪ (V W )1/kL3 and

(5.11) x − v − w − ϕ = x0 − u0 − c2 − w − ϕ = ε > 2/k,

analogously to (11.8)–(11.10) of [9], and (3.24)–(3.27) of [17].
The relation Ψ(n) = 0 for 2 ≤ n ≤ U L2 = U implies

(5.12) S(U ) = e
−1/U + O( ∑

n>L2U d
2(n)e
−n/U ) = 1 + O ( 1
U
 ) .

This and (5.10) yield

(5.13)
 ∞∑

n=1 Ψ(n)ϑ(n)
(e
−n/X − e
−n/U )χ(n)n−̺ = −1 + O(q−ε1).

We will use now Hal´asz’ inequality in the simple form given by Lemma 1.7
of [15], with
 an = Ψ(n)ϑ(n)n− 1
2 (e
− n
X − e
− n
U )
(5.14)
 bn = ϑ2(n)
(e
− n
X − e
− n
U ), sj = ̺j − 1
2 .

ξ = (
Ψ(n)n− 1
2 √e−n/X − e−n/U )∞

n=1, ϕj = (√bnχj(n)n−sj )∞

n=1

(ϕj, ξ) = f (sj, χj) =
 ∞∑

n=1 anχj(n)n−sj

(ϕi, ϕj ) = B(
si + sj, χiχj), B(s, χ) =
 ∞∑

n=1 bnχ(n)n−s.

Here we have analogously to [9], (11.14) and [17], (3.32)

∥ξ∥
2 =
 ∞∑

n=1
 |an|2

bn = (1 + O(1/L)
) 2x − u − v
2(v − u) = (1 + O ( 1
L
 )) C0,(5.15)
 21

C0 = 2ϕ + 2c1 + c2
2c2 .

Any term with χiχj ̸= χ0 (χ0 is the principal character mod q) will be,
similarly to (5.10), in case of Theorem C

B(si + sj, χiχj) =
 ∞∑

n=1 ϑ2(n)χiχj(n)
(e
− n
X − e
− n
U )
n−(̺i+̺j−1)(5.16)
 ≪ (qϕW 2U −1) 1
k q 2
k2 ≪ q−ε1

whereas in case of Theorem D:

(5.17) B(si + sj, χiχj) ≪ (W 2U −1) 1
k q 2
k3 ≪ q−ε1.

If χiχj = χ0, that is, χi = χj, then, similarly to (3.35)–(3.38) of [17], we
have
(5.18)

B(si + sj, χ0) = ϕ(q)
q Gq(1)Γ(2 − ̺i − ̺j)
(X 2−̺i−̺j − U 2−̺i−̺j ) + O(q−ε1)

where the real quantity Gq(1) satisﬁes

(5.19) ∣
∣
∣
∣ ϕ(q)
q Gq(1)
∣
∣
∣
∣ ≤ 1 + O(1/L)
wL ,

by the Proposition after (3.36) in [17].
Until now we followed quite closely [9], Section 11 and [17]. The above
considerations were valid for all values ε, c1, c2, κ, x0, η, which determine the
values of the remaining parameters u0, x0, v, w, u and x. Now we will take
an average over η with 0 ≤ η ≤ κ.
Using Hal´asz’s inequality (Lemma 1.7 of [15]) with the notation
(5.20) wj = w(̺j ) = e
−2x1λj − κ+r
2 dj

zi,j = L(2 − ̺i − ̺j) = L(δi + δj + i(γj − γi)) = λi + λj + i(µj − µi)

we obtain from the relations (5.1)–(5.4), (5.13)–(5.19) with C1 = C0/c1,
after taking average in η ∈ [0, κ] which aﬀects x, u, X, U .
(5.21)

(1 + O(ε))
( J∑

j=1 wj
)2 = 1 + O(ε)
κ
 κ∫

0
 ( J∑

j=1 wj
)2dη ≤ C1
 J∑

j=1 wj ∑

i∼j wi|H(zj,i)|

22

where we write i ∼ j if ̺i and ̺j are zeros of the same L(s, χ) and

|H(z)| : = |Γ(z/L)|
L · 1
κ
 ∣
∣
∣
∣(
e
x0z − e
u0z) eκz − 1
z
 ∣
∣
∣
∣(5.22)
 = 1 + O(ε)
κ
 ∣
∣
∣
∣e
(x0+κ)z (1 − e−rz)(1 − e−κz)
z2
 ∣
∣
∣
∣

≤ 1 + O(ε)
κ e
x1a ∣
∣
∣
∣ 1 − e−rz

z
 ∣
∣
∣
∣
 ∣
∣
∣
∣ 1 − e−κz

z
 ∣
∣
∣
∣ =: 1 + O(ε)
κ H1(z)

if Re z = a.
We call the attention of the reader to the fact that while the value of
the LHS of (5.21) is independent of η (up to O(ε)) the RHS would actually
depend on η. This dependence disappears only after taking the integral
over η and this phase is represented already in the form given on the RHS
of (5.21).
In order to estimate for a given ﬁxed zero ̺j belonging to a given χ ̸= χ0,
say, the sum over all terms H1(zj,i) (̺i = ̺χ) we introduce the notation (cf.
[9], p. 325) (with new parameters ω and λ, ω = κ or r)

f1(t) =
 {
sinh((ω − t)λ) for 0 ≤ t ≤ ω
0 for t ≥ ω ,

F1,ω(z) = F1(z) =
 ∞∫

0
 e
−ztf1(t)dt = 1
2
 { eωλ

λ + z + e−ωλ

λ − z − 2λe−ωz

λ2 − z2
 }
(5.23)
 F2,ω(z) = F2(z) = ( 1 − e−ωz

z
 )2 .

As in (13.2) of [9] we see that

(5.24) Re F1(z) ≥ λeωλ

2 |F2(λ + z)| for Re z ≥ 0,

because the relation (5.24) holds with equality for Re z = 0 and therefore,
by Lemma 4.1 of [9], (5.24) holds for the whole halfplane Re z ≥ 0.
Choosing the parameter λ in (5.23) as

(5.25) λ = λj,

we obtain for a ﬁxed j by (5.24) (the summation runs over zeros of L(s, χ))
∑

i;i∼j
|γi−γj |<L−1/2
∣
∣F2(λj + λi + i(µj − µi)
∣
∣(5.26)
 23

≤ 2
λj e
−ωλj ∑

i;i∼j
|γi−γj |<L−1/2
 Re F1((sj − ̺i)L)

where sj = 1 + iγj.
The contribution of all terms with |γi − γℓ| > L−1/2 (consequently |µi −
µj| > L1/2) for any ℓ is clearly by well known log-free density theorems

(5.27) ≪ (∑ wj)2e
(x0+κ) e3Λ∞

L < ε
(∑ wi)2.

Applying the last displayed formula of the proof of Lemma 13.2 of [9]:
∑

i;i∼j
|γi−γj |<L−1/2
 Re F1((sj − ̺i)L)
(5.28)
 ≤ f1(0) ( ϕ
2 + ε
) − L−1 ∞∑

n=1 Λ(n)Re ( χ(n)
nsj
 ) f1
 ( log n
L
 )

≤ f1(0) ( ϕ
2 + ε
) + L−1 ∞∑

n=1 Λ(n) χ0(n)
n f1
 ( log n
L
 )

≤ f1(0) ( ϕ
2 + ε
) + F1(0) + ε.

So, we obtain ﬁnally from (5.26)–(5.28) for any ﬁxed j

∑

i;i∼j
|γi−γj|<L−1/2
 |F2(zi,j)| ≤ ϕ
2
 ( 1 − e−2ωλj

λj
 ) + ( 1 − e−ωλj

λj
 )2 + ε(5.29)
 =: Bϕ,ω(λj) + ε.

This, together with (5.21), (5.22), (5.23) and (5.27) yields

(1 + O(ε))
(∑

j wj
)2
(5.30)

= (1 + O(ε))
(∑

j e
−2x1λj − r+κ
2 dj )2

≤ C1κ
−1 ∑

j
 ∑

i∼j
|γi−γj |<L−1/2

e
−2x1(λi+λj )− r+κ
2 (di+dj)e
x1(λi+λj )√|F2,κ(zi,j)F2,r(zi,j)|

24

= C1κ
−1 ∑

j
 ∑

i∼j
|γi−γj|<L−1/2
 e
−x1(λi+λj)− r+κ
2 (di+dj )√|F2,κ(zi,j)F2,r(zi,j)|.

Taking into account that

(5.31) 1 − e−x

x

is monotonically decreasing for x ≥ 0, we obtain that

(5.32) e
−ωdj Bϕ,ω(λj) = Bϕ,ω(λj) ≤ Bϕ,ω(Λ) for λj ≥ Λ.

Further, as

(5.33) ex − e−x

x

is monotonically increasing for x ≥ 0, so is eωλBϕ,ω(λ). Hence we obtain for
λj ≤ Λ

(5.34) e
−ωdj Bϕ,ω(λj) = e
−ωΛe
ωλj Bϕ,ω(λj) ≤ Bϕ,ω(Λ).

Now using the trivial relation |F2(zi,j)| = |F2(zj,i)|, by 2ab ≤ a2 + b2 we
obtain from (5.31)–(5.34), (5.29) and the Cauchy inequality

∑

j
 ∑

i∼j
|γi−γj |<L−1/2
 e
−x1(λi+λj )− r+κ
2 (di+dj)√|F2,κ(zi,j)| |F2,r(zi,j)|

(5.35)

≤ ∑

j e
−2x1λj− r+κ
2 dj ( ∑

i;i∼j
|γi−γj |<L−1/2

e
−κdj |F2,κ(zi,j)|
)1
2
( ∑

i;i∼j
|γi−γj |<L−1/2

e
−rdj F2,r(zi,j)
)1
2

≤ (∑

j wj
)(√Bϕ,κ(Λ)Bϕ,r(Λ) + ε
).

Consequently, from (5.30) and (5.35) we have

(5.36) ∑

j wj ≤ (1 + O(ε))C1√Bϕ,κ(Λ)Bϕ,r(Λ)/κ = (1 + O(ε))C2(ϕ, κ, Λ),

which proves Theorems C and D.
 25

6 Properties of the G-function

The following two lemmas show that the problem of showing Condition 2 for
the G-function deﬁned in (4.19) can be reduced to its validity in a bounded
region. In the ﬁrst 3 lemmas we will use explicit forms of G(z) and G′(z) as
follows:
 G(z) = 16
15z − 8
3z3 + 4
z4 − 4
z6 + 4e−2z

z4
 ( z + 1
z
 )2 ,(6.1)
 G
′(z) = − 16
15z2 + 8
z4 − 16
z5 + 24
z7 − 8e−2z

z4
 (1 + 4
z + 6
z2 + 3
z3
 ) .(6.2)

The integral form of G(z) in (4.19) and g(u) ≥ 0 trivially implies that
for real x ∈ R

(6.3) G(x) > 0, G
′(x) < 0, G
′′(x) > 0, . . . .

Let z = a+it and let us examine for ﬁxed t the behaviour of the functions

Ψt(a) = Re G(a + it)
G(a)
(6.4)
 Φt(a) = Re G
′(z) · G(a) − Re G(z) · G
′(a) = G
2(a) dΨt(a)
da .(6.5)

Lemma 1. For 0 ≤ a ≤ 13, |t| ≥ 14 we have

(6.6) Φt(a) > 9G(a)
|z|4 > 0.

Proof. Since for Re z ≥ 0, we have Re G(z) ≥ 0 (cf. (4.22)) and 0 < G(a) <
1 it is suﬃcient to prove

(6.7) Re G
′(z) > 9
|z|4 .

From (6.2) and (4.25) we obtain by |e−2z| ≤ 1, G(a) ≤ G(0) = 8/9 as
claimed above. Further,

Re G
′(z) ≥ 16
|z|4
 ( 1
15 (t2 − a2) − 1 − 3
|z| − 3
|z|2 − 3
|z|3
 )
(6.8)
 ≥ 16
|z|4
 (27
15 − 1 − 3
14 − 3
142 − 3
143
 ) > 9
|z|4

26

Lemma 2. For a = −b ∈ [−1.25, 0], |t| ≥ 50 we have

(6.9) Φt(a) > G(−b)
25|z|2 .

Proof. We will use the notation h(b) = 8
9 G(−b) + bG′(−b). Then

(6.10) h
′(b) = G′(−b)
9 − bG
′′(−b) < 0,

and hence

(6.11) h(b) ≥ h(1.25) > 1/90 for b ∈ [0, 1.25].

Further, by simple computation

(6.12) G(−b) ≥ G(0) = 8
9 , |G
′(−b)| ≤ |G
′(−1.25)| < 1.36.

Now, from (6.1), (6.2), (6.5), and (6.10)–(6.12)

(6.13) G(−b) ≥ max ( 9
8 b|G
′(−b)|, 0.65|G
′(−b)|
)

we obtain

Φt(−b)

(6.14)

≥ 16G(−b)
15|z|2
 ( 1−(b/t)2

1+(b/t)2 − 7.5
|z|2
 (
1 + 2
|z| + 3
|z|3 +e
2.5(
1+ 4
|z| + 6
|z|2 + 3
|z|3

)))

− 16|G′(−b)|
15|z|2
 (b + 3.75
|z|2
 (1 + 2
|z|2 + 2b
3|z|2 + e
2.5 t2 + 1
t2
 ))

≥ 16G(−b)
15|z|2
 (0.957 − 8
9 − 1.55 · 0.015
) > G(−b)
25|z|2 .

The following lemma reduces the range for numerical check

Lemma 3. If |t| ≥ 8, Re z = −b ∈ [−1.25, −0.14], then

(6.15) Re G(z) < − 1
140|z|2 .

27

Proof. Since ∣
∣ z+1
z ∣
∣2 = (1−b)2+t2

62+t2 ≤ 1 + 1
|z|2 ≤ 65
64 and Re z−3 = |z|−6b(3t2 −
b2) > 0 we obtain

Re G(z) ≤ 1
|z|2
 (
− 16
15 b + 4
|z|2
 (
1 + 1
|z|2 + e
2b ∣
∣
∣
∣ z + 1
z
 ∣
∣
∣
∣
2))

(6.16)
 ≤ −1
15|z|2
 (16b − 60
64 · 65
64 (e
2b + 1)
) .

The function

(6.17) h(b) = 16b − 975
1024 (e
2b + 1)

is increasing for b < b0 = 1
2 ln 8192
975 and decreasing for b > b0, so its minimum
in [0.14, 1.25] is

(6.18) min(
h(0.14), h(1.25)
) = 0.028 · · · > 0.
 Q.E.D.
Now we will prove a lemma, which proves Condition 2 for the restricted
range |t| ≤ π/2 for A0, B0 = ∞ and for an arbitrary function F (z) satisfying

(6.19) F (z) =
 2∫

0 e
−zvf (v)dv with f (v) ≥ 0.

Lemma 4. Φt(x) = Re F (x + it)/F (x) is monotonically increasing in x for
all x ∈ R, if |t| ≤ π/2 and F satisﬁes (6.19).

Proof. Let

(6.20) k(v) = f (v)e
−xv, h(u, x) =
 u∫

0
 k(v)dv, qu(x) = h(u, x)
F (x) .

From (6.19) we obtain by partial integration

Re F (x + it) = [h(u, x) cos(ut)
]2
0 −
 2∫

0
 h(u, x)(−t sin(ut))du(6.21)
 = F (x) cos 2t +
 2∫

0 h(u, x)t sin(ut)du,

28

(6.22) Φt(x) = cos 2t +
 2∫

0
 qu(x)(t sin(ut))du.

Since for |t| ≤ π/2, u ∈ [0, 2] we have t sin(ut) ≥ 0. Hence, in order to show
the lemma, it is suﬃcient to prove

(6.23) d
dx qu(x) ≥ 0 for u ∈ [0, 2].

The property f (v) ≥ 0 implies

F 2(x) d
dx qu(x) = −
 u∫

0 k(v)vdv
 2∫

0 k(y)dy +
 u∫

0 k(y)dy
 2∫

0 k(v)vdv(6.24)
 =
 2∫

u k(v)vdv
 u∫

0 k(y)dy −
 2∫

u k(y)dy
 u∫

0 k(v)vdv

≥ u( 2∫

u k(v)dv
 u∫

0
 k(y)dy −
 2∫

u k(y)dy
 u∫

0
 k(v)dv
) = 0.

Q.E.D.
Finally, we can check the remaining range by computer and verify Con-
dition 2 for the G-function with A0 = 13, B0 = 1.25.

Lemma 5. The function G(z) in (4.19) satisﬁes

(6.25) Re G(a + it)
G(a) ≥ Re G(−b + it)
G(−b)

for any t ∈ R if 0 ≤ a ≤ 13, 0 ≤ b ≤ 1.25.

The proof follows from Lemmas 1–4 and from a computer check of (6.25)
(using Maple) for

a = 0, 0 ≤ b ≤ 0.14 for 14 ≤ |t| < 50,(6.26)
 0 ≤ a ≤ 13, 0 ≤ b ≤ 0.14 for 8 ≤ |t| < 14,(6.27)
 0 ≤ a ≤ 13, 0 ≤ b ≤ 1.25 for π/2 < |t| < 8.(6.28)
 29

7 Proof of Theorems H and I

Let
(7.1)j = βj + iγj = 1 − δj + iγj = 1 + L−1(−λj + iµj), j = 1, 2, . . . , N = N (λ)

be the zeros of the L(s, χj) functions mod q (counted with multiplicity if
L(̺, χ) = L(̺, χ′) or ̺ is a multiple zero of some L(s, χ))

(7.2) λ0 ≤ λj ≤ Λ, |γj| ≤ L ⇔ |µj| ≤ LL, L ≤ L.

Since ζ(s) has no zero in the region above we can assume χ ̸= χ0. The
notation k ∼ j will denote that ̺k and ̺j are zeros of the same L(s, χ).
Further, suppose that the L-functions belonging to the distinct characters
χ(ν) (1 ≤ ν ≤ m) have exactly Nν zeros in the above region (counted with
multiplicity). Then clearly N = N1 + N2 + · · · + Nm. Let us denote the set
of zeros of L(s, χ) in (7.2) by Z(χ). Further, let for any j ∈ [1, N ] and with
a function F = Fx = G(z/x) (cf. (4.16)–(4.17) and (4.26)–(4.27))

(7.3) ak,j = Re F (λk − λ0 + i(µj − µk))

F (λk − λ0) , bk,j = Re F (−λ0 + i(µj − µk))
F (−λ0)

(7.4) Ak = ∑′

j
j∼k
 ak,j, Bk = ∑′

j
j∼k
 bk,j, ψk = F (λk − λ0)
F (−λ0) ,

(7.5) N ′
ℓ = ∑

̺k∈Z(χℓ) Ak, N ′ =
 m∑

ℓ=1 N ′
ℓ =
 N∑

j=1 Aj,

ψ = F (λ − λ0)
F (−λ0) , ξ = f (0)ϕ
2F (−λ0) , ∆ = ψ − ξ,

where the ∑′ sign means in (7.4) the extra condition |λj + i(µj − µk)| < Lδ
where δ = δ(ε) is a suﬃciently small constant.
Conditions 1, 2 (see (4.16)–(4.17) and (4.26)–(4.27)) and the deﬁnitions
show that

(7.6) ak,j ≥ bk,j, ak,j ≥ 0, ak,k = 1,

consequently for every k = 1, 2, . . . , N

(7.7) Ak ≥ Bk, Ak ≥ 1, N ′
ℓ ≥ Nℓ, N ′ ≥ N.

30

Let K(s, χ) be deﬁned as in [9] (p. 285, after (6.2))

(7.8) K(s, χ) =
 ∞∑

r=1 Λ(n)Re (χ(n)
ns
 ) f ( log n
L
 )

with a function f (u) = fx(u) = xg(ux) as in (4.18) and (4.23) connected to
F (z) by (4.24). (We will omit the lower index x to f , F and K which might
change often depending on the particular problem.)
Following [9], Section 12 we will apply Lemma 5.2 of [9] with the above
function K. So we obtain for any ̺j in (7.1) with β0 = 1− L−1λ0 by λj ≥ λ0
(7.9)
K(β0+iγj, χj) ≤ −L ∑

k
k∼j
|λk+i(µj −µk)|<Lδ

Re F (λk−λ0+i(µj−µk)
)+f (0) ( ϕ
2 + ε
2
 ) L.

Extending the summation for all zeros in (7.2) with |λk + i(µj − µk)| ≥ Lδ
and using the relations 0 ≤ λk − λ0 ≤ 13x we have in these cases by (6.1)

(7.10) F (λk − λ0 + i(µj − µk)
) ≪ 1
|µj − µk| ≪ 1
Lδ .

Since the number of terms being uniformly bounded by Jutila’s density
theorem

(7.11) N (1 − Λ/L, L, q) ≪ε (qL)
(2+ε)Λ/L ≪ e
3Λ ≪ 1,

including the other zeros in the summation on the right-hand side of (7.9)
leads to an additional error of size O(δ−1) = o(L). Thus we obtain from
this modiﬁed form of (7.9), after summation for all j ∈ (1, N )

L
{∑

j≤N
((∑

k
k∼j
 ak,jψk
)F (−λ0) − f (0)ϕ
2 − ε

)}

(7.12)
 ≤ − ∑

j≤N K(β0 + iγj, χj)

= −
 ∞∑

n=1 Λ(n)χ0(n)n−β0f (L−1 log n)Re{∑

j≤N χj(n)n−iγj }

≤
 ∞∑

n=1 Λ(n)χ0(n)n−β0f (L−1 log n)
∣
∣
∣
∣∑

j≤N χj(n)n−iγj ∣
∣
∣
∣.

31

Using (4.31) we obtain

(7.13) F (−λ0) ≥ F (Λ − λ0) ≥ f (0)(ϕ/2 + ε).

Interchanging the order of summation on the left-hand side of (7.12), we
obtain from (7.12), by Ak ≥ 1

(7.14) L2{ ∑

k≤N
(ψk
(∑

j
j∼k
 ak,j
)F (−λ0) − f (0)ϕ/2 − ε
)}2 ≤ ∑
1
 ∑
2,

where, using Lemma 5.3 of [9]
(7.15)
∑

1 =
 ∞∑

n=1 Λ(n)χ0(n)n−β0f (L−1 log n) = K(β0, χ0) = L(F (−λ0) + o(1)
)

and
 ∑
2 =
 ∞∑

n=1 Λ(n)χ0(n)n−β0f (L−1 log n)
∣
∣
∣
∣∑

j≤N χj(n)n−iγj ∣
∣
∣
∣

2
(7.16)
 = ∑

j,k≤N K(
β0 + i(γj − γk), χjχk)

since the above value is real. By Lemma 5.3 of [9] we have by (7.3)–(7.7)
for any ﬁxed k for the terms with j ∼ k a sum

∑

j
j∼k
 K(
β0 + i(γj −γk), χ0) = ∑

j
j∼k
 L{Re F (−λ0 + i(µj − µk)) + o(1)
}
(7.17)
 = L{BkF (−λ0) + o(1)
} ≤ L{
AkF (−λ0) + o(1)
}.

Again, by Lemma 5.2 of [9], we obtain in case of Theorem H for the total
contribution of all other terms the estimate

(7.18) ∑

j,k≤N
k̸∼j
 K(
β0 + i(γj − γk), χjχk) ≤ L (f (0)ϕ
2 + ε
) ∑

κ,ν≤m
κ̸=ν
 NνNκ,

while in case of Theorem I we obtain

(7.19) ∑

j,k≤N
k̸∼j
 K(β0 + i(γj − γk), χjχk) ≤ εL ∑

κ,ν≤m
κ̸=ν
 Nν Nκ.

32

Dividing (7.14) by (LF (−λ0))2 we obtain from (7.15)–(7.18) with the
choice of a new ε1,

(7.20) ( ∑

k≤N(Akψk − ξ)
)2 ≤ ∑

k≤N Ak + ξ ∑

κ,ν≤m
k̸=ν
 NνNκ + ε1(N ′)
2.

Consequently, by Ak ≥ 1, ψk ≥ ψ, N ≤ N ′ and (7.5), (7.7), (7.13) we have

(7.21) (N ′∆)
2 ≤ N ′ + ξ(N ′2 − N ′) + ε1(N ′)
2,

(7.22) N ≤ N ′ ≤ 1 − ξ
∆2 − ξ − ε1

in case of Theorem H. Similarly, in case of Theorem I we have

(7.23) (N ′∆)
2 ≤ N ′ + ε1(N ′)
2,

(7.24) N ≤ N ′ ≤ 1
∆2 − ε1 .
 Q.E.D.

8 Proof of Theorems J, K and L

In order to show our weighted density theorem (Theorem K) we will use the
notation of Section 7 with the additional quantity

(8.1) D′ def
= ∑

j≤N
(
Aj(ψj − ψ)
) ≥ D def
= ∑

j≤N(ψj − ψ) ≥ 0.

This quantity, completely neglected in the proofs of Theorems H and I, will
be our crucial one in the following. We will start from (7.20) to obtain,
instead of (7.21)–(7.22):

(8.2) (N ′∆ + D′)
2 ≤ N ′ + ξ(N ′2 − N ′) + ε1(N ′)
2

(8.3) (N ′)
2(∆2 − ξ − ε1) + N ′(2∆D′) ≤ N ′(1 − ξ)

from which, by ξ < ∆2, we obtain

(8.4) D ≤ D′ ≤ 1 − ξ
2∆ − ε1 .

33

Suppose now that λ0 is given, the λj’s (1 ≤ j ≤ N ) and their number N
are unknown quantities with

(8.5) dj def
= Λ − λj ≥ 0, d1 ≥ d2 ≥ · · · ≥ dN ,

with prescribed conditions

(8.6) 0 ≤ dj ≤ ej e1 ≥ e2 ≥ · · · ≥ eN .

We will suppose that f and F are the functions of Section 4 with the
parameter x satisfying

(8.7) 2/x ≤ B ⇔ x ≥ 2/B.

Since by Corollary 2 or by Jutila’s density theorem [10] we know that
the unknown number N is bounded by some absolute constant R ∈ Z, we
can suppose that in our extremal problem N = R by the introduction of
additional trivial terms with ej = 0 (consequently dj = 0) for N < j ≤ R.
These new trivial terms do not change the values of D and those of S and
D∗, deﬁned below

D∗ = D · F (−λ0) =
 N∑

j=1
(F (λj − λ0) − F (Λ − λ0)
)
(8.8)
 =
 R∑

j=1
(F (d0 − dj) − F (d0)
).

Then, under the constraint D ≤ ̃C ′ we are looking for an upper bound for
the quantity

(8.9) S =
 R∑

j=1(e
Bdj − e
Cdj ) =
 N∑

j=1(e
Bdj − e
Cdj ),

with the side constraints (8.5)–(8.6) and B > C ≥ 0, where R is now a ﬁxed,
large constant. The upper bound will naturally depend on B, C and C ′ but
not on R.
Let

(8.10) T = t0(f ), b = B
T ≥ 1, 0 ≤ c = C
T < b,

Yj = e
ejT ≥ yj = e
dj T ≥ 1, h1(y) = yv, h2(y) = yb − yc.

34

Then we have with the above notation

(8.11) D∗
1(y) :=
 R∑

j=1 F (d0 − dj) = T
 1∫

0
 f (vT )e
−d0vT R∑

j=1 yv
j dv.

The following observation is suﬃcient to show Theorem K.

Proposition. If y ≥ z > 1, η > 0, 0 < v < 1, b ≥ 1, 0 ≤ c < b, then

(8.12) Hi(y, z, η) = hi(y + η) + hi(z − η) − (hi(y) + hi(z)
) <

> 0 for i = 1,

i = 2.

Proof. h′
1(y) is decreasing, h′
2(y) is increasing for y ≥ 1 due to

(8.13) h
′′
1(y) = v(v − 1)yv−2 < 0, h
′′
2(y) = b(b − 1)yb−2 − c(c − 1)yc−2 > 0.

Consequently,

(8.14) Hi(y, z, η) =
 η∫

0
 (h
′
i(y + t) − h
′
i(z − η + t)
)dt <

> 0 for i = 1,

i = 2.

The proposition means that if we have a given conﬁguration of the vari-
ables {yj}R
j=1 with yi ≥ yi+1, Yi ≥ Yi+1, Yi ≥ yi ≥ 1, then this conﬁguration

cannot yield a maximum for the h∗
2(y) = R∑

j=1 h2(yj) if there is a possibility to

increase the distance between two variables among y1, . . . , yR. According to
this, let r be the largest index with yr > 1 in the maximal system {yi}R
i=1.
Then necessarily

(8.15) yi = Yi ⇔ di = ei for i = 1, . . . , r − 1.

Namely, otherwise we could change with a small η > 0 yk to yk + η, yr to
yr − η and obtain a larger value for h∗
2(y) if k is deﬁned by

(8.16) k = min{ν; yν < Yν},

while the corresponding function h∗
1(y) = R∑

j=1 yv
j , and consequently D∗
1(y)

would decrease and thus D∗ ≤ ̃D would still hold for the new system y.
This proves Theorem K.
 35

In order to show Theorem L, taking into account Remark 5, suppose
that the ﬁrst index, for which in the maximum case we do not have equality
in (4.47) is k ∈ [1, M ]. The case k = M is clearly impossible since then we
could increase yk in view of dk < dk−1 which follows by (4.48) from
(8.17)
F (d0−dk)−F (d0) < c(k)−c(k−1) ≤ c(k−1)−c(k−2) = F (d0−dk−1)−F (d0).

If we increase yk that would lead to an increase of h2(y) = yb
k − yc
k and
thereby to an increase of S∗.
If k < M we also must have dk < dk−1 by (8.17). Suppose that we have
exactly ℓ ≥ 1 equal variables after k, that is we have

(8.18) dk ≥ d = dk+1 = · · · = dk+ℓ > dk+ℓ+1 ≥ 0

and dk+ℓ is not the last term. We clearly have d = dk+ℓ > 0 if it is the
last term, otherwise we could simply slightly increase dk, that is, increase yk
slightly which would yield a larger value for S∗. If ℓ = 1 we can substitute
yk+1 by yk+1 − η, yk by yk + η with a suﬃciently small η and we obtain
a contradiction. If ℓ ≥ 2 then we cannot have equality in any of the ℓ − 1
relations of type (4.47) for m = k + i, 1 ≤ i ≤ ℓ − 1, since if the ﬁrst one for
which (4.47) is sharp has index m, then
(8.19)
c(m)−c(m−1) < F (d0−dm)−F (d0) = F (d0−dm+1)−F (d0) ≤ c(m+1)−c(m).

which contradicts (4.48). But then we can substitute similarly to the case
ℓ = 1 yk by yk + η, yk+ℓ by yk+ℓ − η with a suﬃciently small η and we again
arrive at a contradiction. This proves Theorem L.

9 Proof of Theorem 1

According to (2.36)–(2.46) our task will be to show with some small but
ﬁxed constant c0 > 0

(9.1) S0 =
 M∑

i=1 S2
i ≤ 1 − c0.

Let us dissect the sums Si as

(9.2) Si = 25
7
 H∫

0 Ni(λ)e
− 25
7 λdλ = 25
7
 Λ0∫

0 + 25
7
 H∫

Λ0
 = ai + bi,

36

where Λ0 = 1.311,

(9.3) Ni(λ) = ∑

̺j ∈R, λj≤λ
χj ∼χi
 1.

Our basic inequality will be a small reﬁnement of

(9.4) S ≤ ∑

i≤M a2
i + max
i≤M bi
(2 ∑

i≤M ai + ∑

i≤M bi
),

where we will treat two classes (and eventually its conjugate classes) con-
taining the zeros with the greatest real part separately. According to (9.4)
we will estimate ∑ ai, ∑ bi, max bi, using Principles 1–3 in form of Theo-
rems C–K and a few other results of [9] and [22].
As mentioned already in the introduction, we will try to give a relatively
simple proof leaving many possibilities for improvement for future parts of
this series.
Throughout we will use the notation that the classes will be ordered
according to decreasing value of the greatest real part of the zeros belonging
to the relevant class, so according to increasing value of λi = λi1 where the
other zeros of the same class will be ordered as λi1 ≤ λi2 ≤ . . . . Zeros will
be ordered and counted always by multiplicity. In contrast to [9] and [22]
we will include also conjugate classes and conjugate zeros in the calculation.
We will distinguish ﬁrst
Case I. λ1 > 0.44
Case II/A. 0.35 < λ1 ≤ 0.44
Case II/B. λ1 ≤ 0.35
According to Theorem E of [22] we have in Case II at most the real
zero ̺1 = 1 − δ = 1 − λ1L of the real non-principal χ1 with the property
λij ≤ 0.44. The reason to distinguish between Cases II/A and II/B is that
in Case II/B we have no other zeros with λ ≤ Λ0 (in fact with λ ≤ 1.42)
while in Case II/A we might have zeros with λ > 1.18 (see Table 7 on p. 301
of [9]).
We will begin the estimation of max bi: Important role will be played
by Lemma 10.3 of [9], p. 316, according to which apart from at most two
characters and its conjugates we will have λi ≥ 6
7 − ε for q > q0(ε) for
each character. Since we have by Theorem F apart from at most two zeros
λi ≥ 0.702, we will distinguish the following cases for the estimation of
max bi
 37

Case 1 λi ≥ 6/7 − ε (surely valid for i > 4)
Case 2 λi ≥ 0.702 (surely valid for i > 2)
Case 3 0.35 < λi < 0.702
In this case i = 1 or 2 and χi = χ1 or χ1.
Case 4 λi ≤ 0.35
In this case χ1 and ̺1 are real and λ > 1.42 > Λ0 for all other zeros [9,
Tables 3 and 7].
In order to calculate an upper estimate for bi we will apply for Cases
1–4 Theorem I with λ0 = 6
7 − 10−8, 0.702, 0.35 and 0, resp. and in the
last case we will take into account λ > 1.42 for all other zeros. Using
Theorem I we can give a lower estimate for the ﬁrst few zeros with λij ≤ 3
(their number is in Cases 1–4 at most 45, 38, 34 and 31, resp.) and then
apply an upper estimate for the zeros below 3 + k/10 (k = 0, 1, 2, . . . ) until
about 6 which is approximately the limit for Theorem I. We will actually
use Theorem I until Λ2,1 = 6.6, Λ2.2 = 6.4, Λ2,3 = 6 and Λ3,4 = 5.8 in Cases
1–4, resp. Further we will use in Cases 1–4 the values λ0 = 6/7 − 10−8,
λ0 = 0.702, λ0 = 0.35, λ0 = 0, resp. (The limit of Theorem I will be
larger if λ0 is larger.) On the other hand the value x for Fx(z) = G ( z
x )

(see (4.24)) is chosen experimentally to obtain the approximately optimal
estimate for the N th zero of the same class or to bound Ni(3 + k/10) for
3 ≤ 3 + k/10 ≤ Λ2ν (1 ≤ ν ≤ 4). The condition B = 25/7 > t0(f ) = 2/x
will be always satisﬁed as well as λ0/x ≤ 5/4 which assures Condition 2 (see
(4.26)) for Fx(z) = G(z/x). For all the other zeros of the same class, i.e. for
Λ2µ ≤ λij ≤ Λ∞ = log log log q (1 ≤ µ ≤ 4) we can use our estimate (4.11)
of Corollary 2 of Theorem D. For simplicity we can calculate in all Cases
1–4 with E3 arising from Λ3 = 5.8 valid for all Λ ≥ 5.8. We obtain

Lemma 6. We have max bi ≤ c∗
j in Case j, where

(9.5) c
∗
1 = 0.0722, c
∗
2 = 0.0751, c
∗
3 = 0.0826, c
∗
4 = 0.715.

Proof. We give just a brief account of the results of the calculation for the
typical Case 1 (which applies apart from at most four classes for all others).
We obtain at most 6 zeros below Λ0 = 1.311 for which the corresponding
value e−25/7 max(λij ,Λ0) is independently from the concrete value λij ≤ Λ0
just e−(25/7)Λ0 . For the other possible zeros below 3 we get the bounds (in
brackets the value of the parameters x used for the function Fx(z) = G(z/x))
λi7 ≥ 1.47 (1.58), λi8 ≥ 1.61 (1.6), λi9 ≥ 1.73 (1.62), λi10 ≥ 1.85 (1.66),
λi11 ≥ 1.94 (1.66), λi12 ≥ 2.05 (1.68), λi13 ≥ 2.12 (1.68), λi14 ≥ 2.20
(1.68), λi15 ≥ 2.27 (1.68), λi16 ≥ 2.33 (1.68), λi17 ≥ 2.4, λi18 ≥ 2.45,
λi19 ≥ 2.51, λi20 ≥ 2.56, λi21 ≥ 2.61, λi22 ≥ 2.65, λi23 ≥ 2.7, λi24 ≥ 2.74,

38

λi25 ≥ 2.78, λi26 ≥ 2.82, λi27 ≥ 2.85, λi28 ≥ 2.89, λi29 ≥ 2.92, λi30 ≥ 2.95,
λi31 ≥ 2.99 (λi32 ≥ 3) with the parameters x17 = x18 = · · · = x31 = 1.
Similarly we can calculate with experimentally optimally chosen parameters
x = x′
k ∈ [0.6, 1.7] an upper estimate for Ni(3 + k/10) for 0 ≤ k ≤ 35.

The value ∑ bi can be easily estimated by Corollary 1 as

∑

i≤I bi def
= 25
7
 H∫

Λ0
 N (λ)e
− 25
7 λdλ ≤ ∑

λj≤H e
− 25
7 max(λj ,Λ0)

(9.6)
 ≤ e
−19Λ0/21 ∑

λj ≤H e
−(8/3) max(λj ,Λ0) ≤ e
−19Λ0/21 ∑

λj ≤H e
− 8
3 λj e
− r+κ
2 dj

< 22.281e
−19Λ0 /21 < 6.805.

In order to estimate ∑ ai we will distinguish 8 cases as follows (h is a
small constant)
Case 1 λ1 ≥ 0.68 Case 5 0.35 ≤ λ1 < 0.44
Case 2 0.6 ≤ λ1 < 0.68 Case 6 0.14 ≤ λ1 < 0.35
Case 3 0.5 ≤ λ1 < 0.6 Case 7 0.04 ≤ λ1 < 0.14
Case 4 0.44 ≤ λ1 < 0.5 Case 8 λ1 < 0.06

In the most sophisticated Cases 1–5 we will use Theorem K (for its proof
see Section 8) with the parameters λ0 = 0.44, x = 0.68 for Cases 2–5 and
x = 0.7 for Case 1, ϕ = 1
3 . We will choose Λ0 in such a way that it should
be just slightly smaller than the value λ for which

(9.7) (G ( λ − λ0
x
 ) − f (0)ϕ
2
 )2 = f (0)ϕ
2 G (− λ0
x
 ) ⇔ ψ = ξ + √ξ

holds. Λ0 = 1.311 will be such a choice.
In view of f (0) = 16x/15 we have then with the notation of (7.4)–(7.5)

(9.8)
 G (− λ0
x
 ) = 1.56903 . . . , f (0)ϕ
2 = 8
45 · 0.7, λ = Λ0 = 1.311,

G ( Λ − λ0
x
 ) = 0.5882 . . .

ψ = 0.37488 . . . , ξ = 0.07931 . . . ∆ = 0.29557 . . .

39

and consequently by (4.36)
(9.9)

D = ∑(ψj − ψ) ≤ 1.5575, D0 = ∑ (
G
(
λj −λ0
x
 )−G (
λ−λ0
x
 )) ≤ 2.4438.

According to the theorem the sum

(9.10) S′ = ∑

λj ≤Λ0
(e
− 25
7 λj − e
− 25
7 Λ0) = e
− 25
7 Λ0 ∑

λj ≤Λ0(e 25
7 dj − 1) = e
− 25
7 Λ0S

is, in view of Theorem K maximal, if, taking into account Theorems E, F,
we choose

(9.11) λ1 = λ2 = 0.68, λ3 = · · · = λk = 0.702

and λk+1 ∈ [0.702, Λ0] in such a way that D0 = 2.4438 should hold. Since
we have
(9.12)

G ( λ1 −λ0
x
 ) = 8
9 , G ( λ3−λ0
x
 ) = 0.8747 . . . , G ( Λ0−λ0
x
 ) = 0.5882 . . .

we obtain k = 6, G ( λ9−λ0
x ) = 0.71336 . . . , λ9 = 0.99 . . . . Consequently,

(9.13) S′ ≤ 2e
−(25/7)·0.68 +6e
−(25/7)·0.702 +e
−(25/7)·0.99 −9e
−(25/7)Λ0 < 0.612

which settles Case 1.
Similarly we obtain the result for Cases 1–5, that is,

Lemma 7. We have

(9.14) ∑

i≤I ai ≤ ̃cν for Case ν (1 ≤ ν ≤ 5) above, where

(9.15) ̃c1 = 0.612, ̃c2 = 0.622, ̃c3 = 0.564, ̃c4 = 0.453, ̃c5 = 0.483.

Proof. The proof is completely analogous in Cases 2-3 where we use that
apart from two zeros which might be as large as the lower bounds stipulated
in Case ν we have for all other zeros, i.e. for λ3, by Tabellen 2, 3, 7 of [22]

(9.16) λ ≥ c
′
ν , c
′
2 = 0.74, c
′
3 = 0.97.

40

In Case 4, if χ1 or ̺1 is complex, then by Tabelle 7 of [22] we have at
most two zeros, ̺1 and ̺1 (of L(s, χ1) or L(s, χ1) and L(s, χ1), respectively)
with λ ≤ Λ0 (in fact if λ ̸= λ1 then λ ≥ 1.36)

(9.17) ∑

i≤I ai ≤ 2
(e
−(25/7)·0.44 − e
−(25/7)Λ0 ) < 0.39698.

If Case 4 holds and χ1 and ̺1 are real, then by Tables 4 and 7 of [9]
we have apart from this single zero λ ≥ 1.08 for all other zeros, so we can
apply the same procedure as in Case 1 (cf. (9.7)–(9.14)) and obtain (9.14) in
this case with an upper bound. Comparison with (9.17) yields the estimate
(9.15) for ν = 4.

Case 5 is more simple in the sense that in this case χ1 and ̺1 must
be real by Theorem E. Further we have by Tables 4 and 7 of [9] λ ≥ 1.18
apart from this single zero. Applying again the same procedure as before
(cf. (9.7)–(9.13)) we obtain (9.14)–(9.15) for ν = 5.
Case 6 is even more simple since in this case we have just the single real
̺1 for real χ1 within R(Λ0, T ). This means that in this case we have

(9.18) ∑

i≤I ai = a1 ≤ (e
−(25/7)·0.14 − e
−(25/7)Λ0 ) = 0.59727 . . . .

The same applies in Cases 7 and 8 when

(9.19) ∑

i≤I ai = e
−(25/7)λ1 − e
−(25/7)Λ0 .

Summarizing we have

Corollary. In Cases 7–8 we have (9.19) while in Cases 1–6

(9.20) ∑

i ai ≤ 0.622.

Cases 7–8 we will settle just using the results of [9] about further zeros
by the aid of Theorems C and D. For Cases 1–6 we state

Corollary. In Cases 1–6 we have for S in (9.4) the estimate

(9.21) S < 0.9903.

41

Proof. Let us forget for a moment that the typical estimate c∗
1 = 0.0722 holds
up to at most four exceptional classes for max bi. If we had no exceptions
then in Cases 1–6 we would have (9.20) and this would lead by (9.6) and
(9.4) to

(9.22) S− ≤ 0.622
2 + 0.0722(2 · 0.622 + 6.805) = 0.9680218.

However, two of the classes might have a surplus

(9.23) c
∗
3 − c
∗
1 = 0.0826 − 0.0722 = 0.0104

for max bi and this surplus obtains the factor at most 1.244 + 2 · 0.0826 =
1.4092 from 2 ∑ ai and from bi1 + bi2 (the corresponding two exceptional
classes). This leads to the surplus

(9.24) ∆1 = 0.01465568.

Analogously we might have another smaller surplus

(9.25) c
∗
3 − c
∗
1 = 0.0751 − 0.0722 = 0.0029

for max bi with a factor 2 · 0.0751 = 0.1502 (since we calculated already
the contribution of ∑ ai with the larger surplus for all classes). This yields
another surplus of size

(9.26) ∆2 = 0.0029 · 0.1502 = 4.3558 · 10
−4.

Adding ∆1 + ∆2 to S− in (9.22) we obtain S < 0.9832, i.e. (9.21) holds
for Cases 1–6.

In Case 7 we have by Tables 4 and 5 of [9] apart from the single real zero
̺1 for all other zeros λ ≥ 2.421 = Λ1 and we deﬁne ai, bi by Λ1 instead of
Λ0. Consequently we have by (9.4)–(9.5), (9.19) and similary to (9.6) in this
case

(9.27) ∑

i bi ≤ 15.6e
−19Λ1/21 < 1.74516,

(9.28) max bi < c
∗
4 = 0.0715,

(9.29) ∑ ai < e
−(25/7)0.04 − e
−(25/7)Λ1 < 0.86671,

42

(9.30) S ≤ 0.86671
2 + 0.0715(2 · 0.86671 + 1.74516) < 0.99991.

We note that although the estimate (9.28) was shown for the value Λ0
instead of Λ1, but the deﬁnition

bi = bi(Λ) = 25
7
 H∑

Λ Ni(λ)e
−(25/7)λdλ

is clearly decreasing in Λ so in fact we would get a much better estimate for
c∗
4 with Λ1 in place of Λ0.
Finally, in Case 8 we have again a single real zero ̺1 with λ1 ≤ 0.04,
while for all other zeros we have by Theorem G and Table 5 of [9]

(9.31) λ ≥ Λ
∗ = max (( 12
11 − ε
) log 1
λ1 , Λ2
) with Λ2 = 3.96.

Consequently, we have, by Corollary 1 for λ ≥ Λ∗

(9.32) ∑

Λ∗≤λj ≤Λ∞ e
−(8/3)λj < 10.4, ∑

λij ∈κ
Λ∗≤λij ≤Λ∞
 e
−2λij < 10.4.

This implies (deﬁning bi now with Λ∗ = Λ∗(λ1))

(9.33) ∑

Λ∗≤λj ≤Λ∞ bi ≤ e
−( 25
7 − 8
3 )Λ∗ · 10.4 ≤ 10.4λ76/77
1 < 0.435,

(9.34) max bi ≤ e
−( 25
7 −2)Λ∗ · 10.4 ≤ 10.4λ11/7
1

(9.35) ∑ ai = a1 = e
−(25/7)λ1 − e
−(25/7)Λ∗ < e
− 25
7 λ1.

So we have by (9.4) and λ1 ≤ 0.04

(9.36) S ≤ e
− 50
7 λ1 + 2.87 · 10.4λ11/7
1 ≤ e
−7λ1 + 5λ1 < 1,

since (1 − e−y)/y is decreasing for y ≥ 0 and so we have for λ1 ≤ 0.04

(9.37) 1 − e−7λ1

λ1 ≥ 1 − e−0.28

0.04 > 6.1 > 5.

Thereby (9.36) is really true which settles the remaining Case 8 and conse-
quently the proof of Theorem 1 is complete.

Acknowledgement. The author would like to thank his colleague and
friend, Sz. Gy. R´ev´esz, for supplying the proof of Lemma 4.

43

References

[1] Jing Run Chen, Jian Min Liu, The exceptional set of Goldbach num-
bers III, Chinese Quart. J. Math. 4 (1989), 1–15.

[2] Jing Run Chen, Jian Min Liu, On the least prime in an arithmetical
progression. III and IV, Sci. China Ser. A 32 (1989), no. 6, 654–673
and no. 7, 792–807.

[3] N. G. Cudakov, On the density of the set of even numbers which are
not representable as a sum of two primes, Izv. Akad. Nauk SSSR 2
(1938), 25–40.

[4] H. Davenport, Multiplicative number theory, 2nd edition. Revised by
Hugh L. Montgomery, Graduate Texts in Mathematics, 74, Springer-
Verlag, New York–Berlin, 1980. xiii+177 pp.

[5] T. Estermann, On Goldbach’s problem: Proof that almost all even
positive integers are sums of two primes, Proc. London Math. Soc.
(2) 44 (1938), 307–314.

[6] D. A. Goldston, On Hardy and Littlewood’s contribution to the Gold-
bach conjecture, Proceedings of the Amalﬁ Conference on Analytic
Number Theory (Maiori, 1989), 115–155, Univ. Salerno, Salerno,
1992.

[7] Graham, S. W., Applications of sieve methods, Ph. D. Thesis, Uni-
versity of Michigan, 1977.

[8] G. H. Hardy, J. E. Littlewood, Some problems of ‘Partitito Numero-
rum’, V: A further contribution to the study of Goldbach’s problem,
Proc. London Math. Soc. (2) 22 (1924), 46–56.

[9] D. R. Heath-Brown, Zero-free regions for Dirichlet L-functions, and
the least prime in an arithmetic progression, Proc. London Math.
Soc. (3) 64 (1992), no. 2, 265–338.

[10] M. Jutila, On Linnik’s constant, Math. Scand. 41 (1975), 45–62.

[11] Anatolij A. Karatsuba, Basic analytic number theory. Translated
from the second (1983) Russian edition and with a preface by Melvyn
B. Nathanson, Springer-Verlag, Berlin, 1993. xiv+222 pp.

44

[12] Hongze Li, The exceptional set of Goldbach numbers I, Quart J.
Math. Oxford Ser. (2) 50 (2000), no. 200, 471–482.

[13] Hongze Li, The exceptional set of Goldbach numbers II, Acta Arith.
92 (2000), no. 1, 71–88.

[14] Wen Chao Lu, Exceptional set of Goldbach number, J. Number The-
ory 130 (2010), no. 10, 2359-2392.

[15] H. L. Montgomery, Topics in multiplicative number theory, Lecture
Notes in Mathematics, Vol. 227. Springer-Verlag, Berlin–New York,
1971. ix+178 pp.

[16] H. L. Montgomery, R. C. Vaughan, The exceptional set in Goldbach’s
problem. Collection of articles in memory of Juri˘i Vladimiroviˇc Lin-
nik, Acta Arith. 27 (1975), 353-370.

[17] J. Pintz, Some new density theorems for Dirichlet L-functions, arXiv:
1804.05552

[18] J. Pintz, A new explicit formula in the additive theory of primes with
applications I. The explicit formula for the Goldbach and Generalized
Twin Prime Problems, arXiv: 1804.05561

[19] J. G. van der Corput, Sur l’hypoth´ese de Goldbach pour Presque tous
les nombres pairs, Acta Arith. 2 (1937), 266–290.

[20] R. C. Vaughan, On Goldbach’s problem, Acta Arith. 22 (1972), 21-
48.

[21] I. M. Vinogradov, Representation of an odd number as a sum of
three prime numbers, Doklady Akad. Nauk SSSR 15 (1937), 291–294
(Russian).

[22] Xylouris, T., ¨Uber die Linniksche Konstante, Diplomarbeit, Univer-
sit¨at Bonn, 2009, arXiv: 0906, 2749v1

J´anos Pintz
R´enyi Mathematical Institute
of the Hungarian Academy of Sciences
Budapest, Re´altanoda u. 13–15
H-1053 Hungary
e-mail: pintz.janos@renyi.mta.hu
 45
