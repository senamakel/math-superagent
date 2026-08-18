<!-- source: https://arxiv.org/pdf/2112.11412 | converted from PDF -->

arXiv:2112.11412v2  [math.NT]  5 Feb 2022
SIEGEL ZEROS, TWIN PRIMES, GOLDBACH’S CONJECTURE,
AND PRIMES IN SHORT INTERVALS

KAISA MATOM ¨AKI AND JORI MERIKOSKI

Abstract. We study the distribution of prime numbers under the unlikely
assumption that Siegel zeros exist. In particular we prove for
∑

n≤X Λ(n)Λ(±n + h)

an asymptotic formula which holds uniformly for h = O(X). Such an as-
ymptotic formula has been previously obtained only for ﬁxed h in which case
our result quantitatively improves those of Heath-Brown (1983) and Tao and
Ter¨av¨ainen (2021).
Since our main theorems work also for large h we can derive new results
concerning connections between Siegel zeros and the Goldbach conjecture and
between Siegel zeros and primes in almost all very short intervals.

1. Introduction

While the proof of the twin prime conjecture is a distant goal, Heath-Brown [9]
proved in 1983 that if there are inﬁnitely many Siegel zeros, then there are inﬁnitely
many twin primes. More precisely Heath-Brown showed that if, for a Dirichlet
character χ (mod q), the Dirichlet L-function L(s, χ) has a real zero at s = β0
with

(1) β0 = 1 − 1
η log q

for some η ≥ 10, then, for any h ≥ 1 and X ∈ [q250, q500], one has

∑

n≤X Λ(n)Λ(n + h) = XSh + Oh
 ( X
log log η
 ) ,

where
 Sh := 12|h · 2 ∏

p>2
 (
1 − 1
(p − 1)2
 ) ∏

p|h
p>2
 (1 + 1
p − 2
 ) ≍ 12|h h
ϕ(h) .

Actually Heath-Brown proved a more general result for sums of the form
∑

n≤X Λ(α1n + β1)Λ(α2n + β2).

Very recently Heath-Brown’s result was quantitatively improved by Tao and
Ter¨av¨ainen [19] who showed that, for any h ≥ 1 and X ∈ [q41/2+ε, qη1/2 ], one has

(2) ∑

n≤X Λ(n)Λ(n + h) = XSh + Oh
 ( X

log1/20 η
 ) .

2020 Mathematics Subject Classiﬁcation. 11M20, 11N36, 11P32.
Key words and phrases. Siegel zeros, twin primes, Goldbach’s conjecture.

1

2 KAISA MATOM ¨AKI AND JORI MERIKOSKI

This is a special case of their more general theorem on ”Hardy-Littlewood-Chowla”
type correlations

(3) ∑

n≤X Λ(n)Λ(n + h)λ(n + h1) · · · λ(n + hk).

In this paper we will prove (2) with better error term and with uniformity in
the shift h. Furthermore, despite leading to stronger results, our proof is less
involved. Before turning to the strongest formulations of our theorems, let us state
two corollaries. The ﬁrst corollary improves on (2).

Corollary 1.1. Let h ∈ N. Let χ be a primitive quadratic character modulo q ≥ 2
and assume that L(s, χ) has a real zero β0 such that

β0 = 1 − 1
η log q
for some η ≥ 10.
(i) Let C ≥ 1. For X ∈ [q10, q10 log η], we have
∑

n≤X Λ(n)Λ(n + h) = XSh + Oh,C (X exp(−C√
log η)
) .

(ii) Let ε > 0. For X = qV with V ∈ [10 log η, η1−ε], we have
∑

n≤X Λ(n)Λ(n + h) = XSh + Oh
 (
X log6 η
η/V
 ) .

Note that for X ∈ [q10 log η, q10 log4 η] the error term is O(η−1X log10 η), where
the dependency on η is best that can be hoped for apart from the power of log η.
Our main results are uniform with respect to h which allows us to attack also
the Goldbach conjecture. There has been recent activity on the relation between
Siegel zeros and the Goldbach conjecture, see e.g. [3, 6]. The asymptotic form of
Goldbach’s conjecture claims that, for all h ≥ 4,

(4) ∑

n1,n2≤h
n1+n2=h
 Λ(n1)Λ(n2) = (1 + o(1))Sh · h.

We show that if a weak form of (4) holds, then there cannot be Siegel zeros.

Corollary 1.2. Let δ > 0. There exists η = η(δ) ≥ 100 such that the following
holds. Let q ≥ 2 be such that there exists a primitive quadratic character χ (mod q).
Assume that there exists an even h ∈ [q10, qη99/100 ] such that q | h and

(5) δSh · h ≤ ∑

n1,n2≤h
n1+n2=h
 Λ(n1)Λ(n2) ≤ (2 − δ)Sh · h.

Then the Dirichlet L-function L(s, χ) does not have an exceptional zero β0 with

β0 ≥ 1 − 1
η log q .

This improves on a recent result of Friedlander, Goldston, Iwaniec and Suria-
jaya [3] who got a similar conclusion assuming that (5) holds for several h ≡ 0
(mod q). In fact, our result is even stronger and we only need the lower bound
in (5) if χ(−1) = −1 and similarly only the upper bound in (5) if χ(−1) = 1.
We now turn to the precise statements of our main results. When we work
uniformly with respect to h, we get an additional main term when (h, q) has size
close to q. To explain why, let us consider the most transparent case h = q. It is
well known that if there is a Siegel zero, then the primes fail to be equidistributed

SIEGEL ZEROS AND PRIMES 3

(mod q), more precisely we have when q, χ, and β0 are as in Corollary 1.1 with η
large (see e.g. [12, Theorem 5.27]),
∑

n≤x
n≡a (mod q)
 Λ(n) = x
ϕ(q)
 (
1 − χ(a)
β0x1−β0
 ) + O (
x exp ( −c log x
√
log x + log q
 ) log4 q) .

Hence, when η is large, the residue classes a (mod q) with χ(a) = −1 contain about
twice as many primes as one would expect, whereas the residue classes a (mod q)
with χ(a) = 1 contain very few primes. Consequently one would expect that
∑

n≤X Λ(n)Λ(n + q) ≈ 2SqX.

The following general theorem conﬁrms this intuition.

Theorem 1.3. Let C ≥ 1 and ε > 0. Let χ be a primitive quadratic character
modulo q ≥ 2. Write q = 2rq′ with r ≥ 0 and 2 ∤ q′. Assume that L(s, χ) has a real
zero β0 such that
 β0 = 1 − 1
η log q
for some η ≥ 10. Let 0 ̸= h = O(X). We have, for any X = qV with V ≥ 10,

∑

n≤X Λ(n)Λ(n + h) = XSh
 



1 + 1ϕ(2r)|h(−1)
 h
ϕ(2r ) ∏

p|q′

p∤h
 −1
p − 2
 





+ OC,ε
 ( h
ϕ(h) X (
exp(−C√
V log η) + exp(−C(log X)
3/5−ε) + V (log η)
6

η
 )) .

Note that the main term vanishes for some even h, for instance when 3 | q and
h = 2q/3 (note that q′ is necessarily square-free (see e.g. [12, Section 3.3]) and so
in this case 3 ∤ h).
We get a similar result concerning Goldbach’s conjecture.

Theorem 1.4. Let C ≥ 1 and ε > 0. Let χ be a primitive quadratic character
modulo q ≥ 2. Write q = 2rq′ with r ≥ 0 and 2 ∤ q′. Assume that L(s, χ) has a real
zero β0 such that
 β0 = 1 − 1
η log q .

for some η ≥ 10. Let h ≥ q10 be an integer. Writing V := log h
log q ≥ 10, we have

∑

n1,n2≤h
n1+n2=h
 Λ(n1)Λ(n2) = hSh
 



1 + χ(−1)1ϕ(2r)|h(−1) h
ϕ(2r ) ∏

p|q′

p∤h
 −1
p − 2
 





+ OC,ε
 ( h
ϕ(h) h (
exp(−C√
V log η) + exp(−C(log h)
3/5−ε) + V (log η)
6

η
 )) .

Corollaries 1.1(i) and 1.2 immediately follow from Theorems 1.3 and 1.4 since
by Siegel’s theorem (see e.g. [17, Theorem 11.14 combined with (11.10)])

(6) η ≪ε qε.

For X ≥ q10 log η the quantity
1
η = exp(− log η) ≫ exp(−√
(log q)(log η)) ≫ exp(−√
log X),

4 KAISA MATOM ¨AKI AND JORI MERIKOSKI

dominates exp(−C(log X)
3/5−ε) and exp(−CV √
log η), so also Corollary 1.1(ii) fol-
lows from Theorem 1.3.
We will also prove a corollary concerning the distribution of primes in almost all
short intervals. A probabilistic model predicts that

(7) ∑

y<p≤y+H 1 = (1 + o(1)) H
log X .

holds for almost all y ∈ [X, 2X] as soon as H/ log X → ∞. Selberg [18] has shown
this for H/ log
2 X → ∞ assuming the Riemann hypothesis. Assuming also the Pair
correlation conjecture [16], Heath-Brown [8] proved the result predicted by the
probabilistic model. Unconditionally, the best current results are an asymptotic
formula (7) for almost all y ∈ [X, 2X] when H ≥ X 1/6+o(1) (see e.g. [7, Theorem
9.1]), and a lower bound when H ≥ X 1/20 (see Jia [13]).
Here we prove the asymptotic formula (7) for almost all y with H in the range
predicted by the probabilistic model under the unlikely assumption of existence of
Siegel zeros.

Corollary 1.5. Let C ≥ 2 and ε > 0. Let χ be a primitive quadratic character
modulo q ≥ 2 and assume that L(s, χ) has a real zero β0 such that

β0 = 1 − 1
η log q .

for some η ≥ 10.
Let X ≥ q10, write V := log X
log q ≥ 10, and let 2 ≤ H ≤ X 1/3. Then

∫ 2X

X
 

 ∑

y<n≤y+H Λ(n) − H




2
 dy

≪C,ε HX log X + H 2X (
exp(−C√
V log η) + exp(−C(log X)
3/5−ε) + V log6 η
η
 ) .

This implies that as soon as

η → ∞, H
log X → ∞, and q10 ≤ X ≤ qη1−δ ,

we get the asymptotic formula
∑

y<p≤y+H 1 = (1 + o(1)) H
log y

for almost all y ∈ [X, 2X].

Remark 1.6. Under the assumption of the existence of Siegel zeros one can show that
the Pair correlation conjecture [16] fails drastically, that is, almost all zeros of ζ(s) in
some range depending on q lie on a lattice with normalized distances in ( 1
2 + o(1))Z
(the so-called alternative hypothesis, this follows e.g. from [1, Proposition 9.2]
assuming η = log100 q for zeros of height T = exp(log10 q)). Note however that
in [8], instead of the full Pair correlation conjecture, Heath-Brown only requires a
weaker upper bound for Montgomery’s [16] function F , which is consistent with the
alternative hypothesis.

Remark 1.7. All our results hold also if instead of existence of Siegel zeros we
assume that L(s, χ) takes a small value at s = 1, that is, assuming

L(1, χ) ≤ 1
η log q .

SIEGEL ZEROS AND PRIMES 5

Indeed, by [17, Theorem 11.4] (using [17, (11.7)] in the contrapositive direction)
this implies that L(s, χ) has a real zero β0 with

1 − β0 ≪ L(1, χ) ≪ 1
η log q .

In the opposite direction the best current result loses essentially two factors of
log q, that is, we have L(1, χ) ≪ (1 − β0)(log2 q)/ log log q by work of Friedlander
and Iwaniec [5]. For this reason we state our results in terms of Siegel zeros.
Note that in many articles such as [4, 15] one has to assume that χ is excep-
tional in a very strong sense, that is, L(1, χ) ≪ log−C q for some large constant C.
Combining the ideas from this paper with the argument in [15] it is possible replace
this strong assumption by (1) with a similar dependency on η as in Corollary 1.1.

Let us here brieﬂy discuss why having a Siegel zero is a helpful assumption; we
will discuss the proof strategy rigorously and in more detail in Section 2.
If L(s, χ) has a zero at s = β0 with β0 close to 1, then

L(1, χ)
−1 = ∑

n
 µ(n)χ(n)
n = ∏

p
 (
1 + µ(p)χ(p)
p
 )

is large, so that χ(p) = µ(p) for most primes (in a wide range depending on q) and
heuristically we have

(8) Λ = µ ∗ log ≈ χ ∗ log,

so that we can hope to replace Λ by a χ ∗ log. But the function χ ∗ log is of similar
complexity as the divisor function τ = 1 ∗ 1 when the modulus q is small compared
to x.
Hence, in order to prove our theorems, we need to show that the contribution of
the error in the approximation (8) is small as well as study
∑

n≤X(χ ∗ log)(n)(χ ∗ log)(±n + h)

which has similar complexity as divisor correlations. Friedlander and Iwaniec [4]
have shown that the error in (8) can be controlled if we can solve the corresponding
ternary divisor problem. In our case we cannot, but we can still deal with the error,
once we restrict both sides to numbers without large prime factors. In general, for
sequences with relatively large (logarithmic) density one can exploit crude bounds
to get a result without knowledge of the corresponding ternary divisor problem.

Notation. We write 1P for the indicator function of the claim P . We write Λ(n),
µ(n), ϕ(n), τ (n) for the von Mangoldt function, M¨obius function, Euler ϕ-function
and the divisor function. These functions are understood to equal 0 for non-positive
integers. For arithmetic functions f, g : N → C we deﬁne the Dirichlet convolution

(f ∗ g)(n) := ∑

n=km f (k)g(m).

For f : R → C and g : R → R+, we write f (x) = O(g(x)) or f (x) ≪ g(x) if there
exists a constant C > 0 such that |f (x)| ≤ Cg(x) for every x. Furthermore, for
positive valued f and g we write f (x) ≍ g(x) when g(x) ≪ f (x) ≪ g(x). If there
is a subscript (e.g. Ok(g(x))), then the implied constant is allowed to depend on
the parameter(s) in the subscript.
We say that a function g : R → R is smooth if it has derivatives of all orders.

6 KAISA MATOM ¨AKI AND JORI MERIKOSKI

For u ∈ C we write e(u) := e(2πiu) and for q ∈ N we write eq(u) = e(u/q). For
any function
 g ∈ L
1(R) := {
f : R → C : ∫ ∞

−∞ |f (x)|dx < ∞
} ,

we denote by ̂g the Fourier transform

̂g(ξ) = ∫ ∞

−∞ g(x)e(−ξx)dx.

For a ∈ Z and q ∈ N we write a for the inverse of a (mod q) (the modulus will
be clear from the context, e.g. in e( cu
v ) the inverse is (mod v)).

2. Initial steps

We start by replacing the sums in Theorems 1.3 and 1.4 by smoothed variants.
Let δ = X −ε for some small ε > 0 and let g : R → [0, 1] be a smooth function
that is supported on [1, 2] and equals 1 on [1 + δ, 2 − δ]. Assume further that the
derivatives of g satisfy g(j)(x) ≪ δ−j for every x.
In case of Theorem 1.3 we ﬁrst decompose the summation condition n ≤ X
dyadically into conditions n ∈ (x, 2x] with x ≤ X/2. We estimate the contribution
of x ≤ X 1−ε/4 trivially, and for the remaining x we replace the condition 1n∈(x,2x]
by g(n/x) with an error term O(δx log2 X) = O(X 1−ε/2). Thus it suﬃces to show
that

∑

n g ( n
X
 ) Λ(n)Λ(n + h) = ∫ g ( y
X
 ) dy · Sh
 



1 + 1ϕ(2r)|h(−1) h
ϕ(2r ) ∏

p|q′

p∤h
 −1
p − 2
 





+ OC,ε
 ( h
ϕ(h) X (
exp(−C√
V log η) + exp(−C(log X)
3/5−ε) + V (log η)
6

η
 )) .

whenever 0 < h ≤ X 1+ε/2 (we can assume that h is positive by symmetry).
In case of Theorem 1.4, note that by symmetry we can concentrate on the case
n1 < h/2 < n2 and that when n1 ≤ h1−ε/4 we can use a trivial estimate. Arguing
as above with similar g, we see that it suﬃces to show that

∑

n g ( n
X
 ) Λ(n)Λ(h − n) = ∫ g ( y
X
 ) dy · Sh
 



1 + χ(−1)1ϕ(2r)|h(−1)
 h
ϕ(2r ) ∏

p|q′

p∤h
 −1
p − 2
 





+ OC
 ( h
ϕ(h) X (
exp(−CV √
log η) + exp(−C(log h)
3/5−ε) + V (log η)
6

η
 )) .

for every X ∈ [h1−ε/3, h/4].
We shall deal with Theorems 1.3 and 1.4 simultaneously, and thus consider
∑

n g ( n
X
 ) Λ(n)Λ(±n + h).

Note that when n is in the support of g(n/X) with X as above, we have ±n + h ≥
max{X, h/2}.
Let χ be a quadratic character modulo q. Following [4, 15], we write

(9) λ := 1 ∗ χ and λ
′ := χ ∗ log,

so that λ ∗ Λ = (1 ∗ χ) ∗ (µ ∗ log) = (1 ∗ µ) ∗ (χ ∗ log) = λ
′.

SIEGEL ZEROS AND PRIMES 7

Note also that λ(n) ≥ 0 and λ
′(n) ≥ Λ(n) ≥ 0 (since λ
′ = λ ∗ Λ). By above

(10) λ
′(n) = (λ ∗ Λ)(n) = Λ(n) + ∑

n=km
m>1
 Λ(k)λ(m),

so we have obtained a formula for the error term in the approximation (8). Similarly
as in [15], we now restrict this approximation to rough numbers to ensure that m
is large. For large m we expect by the assumption of existence of Siegel zeros that
the function λ(m) is lacunary, which will make the sum in (10) small.
For w ≥ 2 and k ∈ N, write

P (w) = ∏

p<w p and Pk(w) = ∏

p<w
p∤k
 p.

Let u be a large parameter to be chosen later (see (41)) and write z := X 1/u.
Adding the condition (n, qP (z)) = 1 to both sides of (10), we get

(11) Λ(n) = λ
′(n)1(n,qP (z))=1 − ∑

n=km
m≥z
(km,qP (z))=1
 Λ(k)λ(m) + O
 (
log n · 1 n=p
ν

p|qP (z)
)
 .

We deﬁne

(12) cn := ∑

n=km
m≥z
(km,P (z))=1
 Λ(k)λ(m).

Note that 0 ≤ λ
′(n) ≤ τ (n) log n and 0 ≤ cn ≤ 1(n,P (z))=1τ (n)
2 log n. When
g : R → [0, 1] is a smooth function supported on [1, 2], we obtain

∑

n g ( n
X
 ) Λ(n)Λ(±n + h) = ∑

n
(n(±n+h),qP (z))=1
 g ( n
X
 ) λ
′(n)λ
′(±n + h)

+ O
 



(z + ω(q)) log2 X + log X ∑

n≤2X
(n(±n+h),qP (z))=1

(cnτ (±n + h)
2 + τ (n)c±n+h)





 .

(13)

We deal with the error term using the following lemma which will quickly follow
from Henriot’s bound on correlations of multiplicative functions (see Section 3.1 for
the proof).

Lemma 2.1. Let cn be as in (12), let X ≥ 3, u ≥ 2, and z = X 1/u. Then, for any
0 < |h| ≤ X 10, we have

∑

n≤4X
(n(±n+h),P (z))=1
 cnτ (±n + h)
2 ≪ h
ϕ(h) X
log X
 



u4 ∑

z≤m≤4X/z
(m,P (z))=1
 λ(m)
m + u10

z
 



 .

Here the sum over m can be estimated in terms of η. The following lemma will
be proved in Section 4.

Lemma 2.2. Let χ be a primitive quadratic character modulo q ≥ 2. Assume that
L(s, χ) has a real zero β0 such that

β0 = 1 − 1
η log q

8 KAISA MATOM ¨AKI AND JORI MERIKOSKI

for some η ≥ 10. Let z = qv for some v ∈ R+. Then for any Y > z
∑

z≤m≤Y
(m,P (z))=1
 λ(m)
m ≪ ( 1
v2ηv/2 + v
η · log Y
log z + 1
z
 ) ( log Y
log z
 )2.

To deal with the main term in (13) we use the following proposition which we
will prove in Section 5. Note that this proposition is unconditional and gives an as-
ymptotic formula for generalized divisor function correlations over rough numbers.
The parameter β refers to the β-sieve described in Lemma 3.2.

Proposition 2.3. Let δ > 0. Let X, M1, M2, N1, N2 ≥ 1 be such that

M1N1 ≍ X, X ≪ M2N2 ≪ δ−1X, and Mj ≪ Nj.

Let h ∈ Z+. Let q ≥ 1 and let χ1, χ2, ψ1, ψ2 be real characters (mod q). Let
f : R4
+ → [0, 1] be smooth and compactly supported and suppose that for all j ≥ 0
and v ∈ {1, 2},
 ∂j

∂x
j
v f (x1, x2, y1, y2), ∂j

∂yj
v f (x1, x2, y1, y2) ≪j δ−j.

Let A ∈ N. Assume that β is suﬃciently large in terms of A and u ≥ 1000β. Write
z = X 1/u and, for r ≥ 0,

(14) zr := z((β−1)/β)
r

Then ∑

m1,m2,n1,n2
±m1n1+h=m2n2
(m1m2n1n2,P (z))=1
 χ1(m1)χ2(m2)ψ1(n1)ψ2(n2)f ( m1
M1 , m2
M2 , n1
N1 , n2
N2
 )

= ∏

p<z
p|h,p∤q
 (1 − 1
p
 ) ∏

p<z
p∤hq
 (
1 − 2
p
 ) · 1
q
 ∑

γ (q) ψ1(γ)ψ2(±γ + h)

· ∑

m1,m2
(m1m2,P (z))=1
 χ1(m1)χ2(m2)ψ1(m1)ψ2(m2)
m1m2
 ∫ f ( m1
M1 , m2
M2 , y
m1N1 , ±y + h
m2N2
 ) dy

+ O
( ∑

r1,r2,r3≥0
max rj≥ u
1000 −β
 2−A(r1+r2+r3) ∑

m1,m2,n1,n2
±m1n1+h=m2n2
(n1,P (zr1 ))=(n2,Ph(zr2 ))=1
(m1,P (zr3 ))=(m2,hP (z))=1
 (τ (m1)τ (n1)τ (n2))
A+1

· f ( m1
M1 , m2
M2 , n1
N1 , n2
N2
 ))
 + OA
 (
δ−3X 7/9q2 + h
ϕ(h) X
log2 X
 ( u6

z + e−Au/3000)) .

An application of Henriot’s bound (see Lemma 3.1 below) will allow us to show
in Section 3.1 that
∑

r1,r2,r3≥0
max rj≥ u
1000 −β
 2−A(r1+r2+r3) ∑

m1,m2,n1,n2
m1n1≤10X
±m1n1+h=m2n2
(n1,P (zr1 ))=(n2,Ph(zr2 ))=1
(m1,P (zr3 ))=(m2,hP (z))=1
 (τ (m1)τ (n1)τ (n2))
A+1

≪A h
ϕ(h) X
log2 X e−Au/2000.

(15)

In Section 6 we will prove the following lemma which helps us in evaluating the
main term we obtain from Proposition 2.3.

SIEGEL ZEROS AND PRIMES 9

Lemma 2.4. Let χ be a primitive quadratic character modulo q ≥ 2. Assume that
L(s, χ) has a real zero β0 such that

β0 = 1 − 1
η log q

for some η ≥ 10. Let X ≥ 3, u ≥ 2, and z = X 1/u = qv. Assume that X 1/10 ≤
N ≤ X 2 and 1 ≤ y ≤ X 2. Then, for any ε > 0 and A, C ≥ 2,

∑

n≤N
(n,P (z))=1
 χ(n) log(y/n)
n = (1 + OA,C,ε(E)) ∏

p<z
 (
1 − 1
p
 )−1

with
 E = u4

v2ηv/2 + vu5

η + u4

z + e−Au/3000 + exp(−C log3/5−ε X).

The complete character sums resulting from Proposition 2.3 will be evaluated
using the following elementary lemma which will be proved in Section 3.4.

Lemma 2.5. Let q ≥ 2 and let χ be a primitive quadratic character of modulus
q = 2rq′ with r ≥ 0 and 2 ∤ q′. Let χ0 be the principal character (mod q), and let
h be an even integer. Then

1
q
 ∑

m (q) χ0(m)χ0(±m + h) = ∏

p|(q,h)
 (
1 − 1
p
 ) ∏

p|q
p∤h
 (
1 − 2
p
 ) ,(16)
 1
q
 ∑

m (q) χ(m)χ0(±m + h) = −χ(∓h)
q ,(17)
 1
q
 ∑

m (q) χ(m)χ(±m + h) = 1ϕ(2r)|h(−1)
 h
ϕ(2r ) χ(±1) ∏

p|(q,h)
 (
1 − 1
p
 ) ∏

p|q
p∤h
 −1
p .(18)

Precise evaluation of the character sum (18) is, in addition to keeping track
of some dependencies, the reason we can deal with the case (h, q) is close to q
in Theorems 1.3 and 1.4. As Tao and Ter¨av¨ainen [19] consider the more general
problem (3), they face more complicated character sums and need to apply Weil’s
bound, and thus they do not obtain similar uniformity in h.
In Section 7 we shall use the results stated here to prove Theorems 1.3 and 1.4.
Then in Section 8 we deduce Corollary 1.5 from Theorem 1.3.

Remark 2.6. Before moving on, let us brieﬂy discuss how our approach diﬀers from
that of Tao and Ter¨av¨ainen [19]. We establish Proposition 2.3 using the β-sieve
whereas Tao and Ter¨av¨ainen [19] use Selberg’s sieve in their arguments. Using the
β-sieve makes replacing the condition 1(n,P (z))=1 by a type I sum more transparent
since the remainder is easier to analyse, see Lemma 3.2(i) for a convenient bound.
This diﬀerence of the two sieves is discussed also in [2, Section 10.2]. Thanks to
using the β-sieve our arguments are considerably simpler than those in [19], and
we get improved error terms automatically.
More precisely, the starting point of [19] is to replace Λ(n) by (χ ∗ log)(n)ν(n),
where ν(n) are Selberg sieve weights. Replacing Λ(n) by Λ(n)ν(n) is almost immedi-
ate thanks to the support of Λ(n). However, replacing Λ(n)ν(n) by (χ ∗ log)(n)ν(n)
is somewhat more complicated and this leads to weaker error terms. Also later
the Selberg sieve coeﬃcients complicate matters in [19]. Despite this, it might
be possible to argue more carefully with the Selberg sieve and obtain error terms
comparable to ours.

10 KAISA MATOM ¨AKI AND JORI MERIKOSKI

3. Lemmas

3.1. Multiplicative functions. We will use some standard estimates for multi-
plicative functions. Note ﬁrst that, when f : N → C is a divisor-bounded (i.e.
f (n) ≤ τ (n)
A for some A ≥ 1) multiplicative function, we have

(19) ∑

n≤X
 |f (n)|
n ≪ ∏

p≤X
 (
1 + |f (p)|
p
 ) .

Furthermore, by Mertens’ theorem

(20) ∏

w<p≤z
 (
1 + k
p
 ) ≍ ( log z
log w
 )k .

We shall also need the following consequences of Henriot’s bound [10, 11].

Lemma 3.1. Let X ≥ 2 and 2 ≤ w1, w2 ≤ X. Let also 1 ≤ |h| ≤ X 10.

(i) Let m1, m2 ≥ 0. Then

∑

n≤X τ (n)
m1 1(n,P (w1))=1τ (±n + h)
m21(±n+h,Ph(w2))=1

≪m1,m2 h
ϕ(h) · X
log2 X
 ( log X
log w1
 )2
m1 +1 ( log X
log w2
 )2
m2 .

(ii) Let m ∈ Z be such that (m, hP (w2)) = 1. Then

∑

n≤X 1(n,P (w1))=11(±mn+h,P (w2))=1τ (±mn + h)
2 ≪ h
ϕ(h) X
log2 X log X
log w1
 ( log X
log w2
 )4 .

Proof. Proof of (i). We apply Henriot’s bound [10, Theorem 3] with

Q1(n) = n, Q2(n) = ±n + h, D = h2,

F (n1, n2) = 1(n1,P (w1))=11(n2,Ph(w2))=1τ (n1)
m1 τ (n2)
m2,

ρQ1 (n) = |{v (mod n) : v ≡ 0 (n)}| = 1,

ρQ2 (n) = |{v (mod n) : ± v + h ≡ 0 (n)}| = 1

ρ(p) = |{v (mod p) : v(±v + h) ≡ 0 (p)}| =
 {2 if p ∤ h
1 otherwise,

∆D = ∏

p|h
(
1 + F (p, 1) |{n (p2) : p∥n, p ∤ ±n + h}|
p2 + F (1, p) |{n (p2) : p ∤ n, p∥ ± n + h}|
p2

+ F (p, p) |{n (p2) : p∥n, p∥ ± n + h}|
p2
 )
 ≪ ∏

p|h
p≥w1
 (
1 + 2m1+m2

p
 ) .

SIEGEL ZEROS AND PRIMES 11

Applying [10, Theorem 3] and then (19), we obtain
∑

n≤X τ (n)
m1 1(n,P (w1))=1τ (±n + h)
m2 1(±n+h,Ph(w2))=1

≪ ∆DX ∏

p≤X
 (
1 − ρ(p)
p
 ) ∑

n1n2≤X
(n1n2,D)=1
 F (n1, n2) ρQ1 (n)ρQ2 (n)
n1n2

≪ X ∏

p|h
p≥w1
 (
1 + 2m1+m2

p
 ) · ∏

p≤X
 (
1 − 2
p
 ) ∏

p|h
 (
1 + 1
p
 )

· ∏

w1≤p≤X
p∤h
 (
1 + 2m1

p
 ) ∏

w2≤p≤X
p∤h
 (
1 + 2m2

p
 ) .

Here

∏

p|h
p≥w1
 (
1 + 2m1+m2

p
 ) ≪ exp
 



2m1+m2 ∑

p|h
p≥w1
 1
p
 



 ≪ exp
 


2m1+m2 ∑

p≤10 log X
log w1
 1
p
 




≪m1,m2
 (
log log X
log w1
 )2
m1+m2 ≪m1,m2 log X
log w1 .

and (i) follows from (20).
Proof of (ii). We use a similar application of Henriot’s bound [10, Theorem 3]
— this time

Q1(n) = n, Q2(n) = ±mn + h, D = h2, F (n1, n2) = 1(n1,P (w1))=11(n2,P (w2))=1τ (n2)
2,

ρQ1 (n) = |{v (n) : v ≡ 0 (n)}| = 1

ρQ2 (n) = |{v (mod n) : ± vm + h ≡ 0 (n)}| =
 {1 if (n, m) = 1
0 otherwise.

ρ(p) = |{v (mod p) : v(±vm + h) ≡ 0 (p)}| =
 {2 if p ∤ hm
1 otherwise,

and
 ∆D = ∏

p|h
(
1 + F (p, p) |{n (p2) : p∥n, p∥ ± mn + h}|
p2
 )
 ≪ ∏

p|h
p≥w2
 (
1 + 4
p
 ) .

Applying [10, Theorem 3] and then (19), we obtain
∑

n≤X 1(n,P (w1))=11(±mn+h,P (w2))=1τ (±mn + h)
2

≪ ∆DX ∏

p≤X
 (
1 − ρ(p)
p
 ) ∑

n1n2≤X
(n1n2,D)=1
 F (n1, n2) ρQ1 (n)ρQ2 (n)
n1n2

≪ X ∏

p|h
p≥w2
 (
1 + 4
p
 ) · ∏

p≤X
 (
1 − 2
p
 ) ∏

p≤X
p|hm
 (
1 + 1
p
 ) · ∏

w1≤p≤X
p∤h
 (
1 + 1
p
 ) ∏

w2≤p≤X
p∤hm
 (
1 + 22

p
 )

12 KAISA MATOM ¨AKI AND JORI MERIKOSKI

Since (m, hP (w2)) = 1, this is

≪ h
ϕ(h) X
log2 X log X
log w1
 ( log X
log w2
 )4 ∏

w2≤p≤X
p|m
 (
1 + 1
p − 4
p
 )

and the claim (ii) follows. □

Now Lemma 2.1 and (15) follow quickly:

Proof of Lemma 2.1. Consider
∑

n≤4X cnτ (±n + h)
21(±n+h,P (z))=1(21)

Using cn ≤ 1(n,P (z))=1τ (n)
2 log n, we see that those n with (n, h) > 1 contribute

≪ log X ∑

n≤4X
(n,h)>1
 τ (n)
21(n,P (z))=1τ (±n + h)
21(±n+h,P (z))=1

≪ log X ∑

p|h
z≤p≤4X
 ∑

n≤4X/p τ (n)
21(n,P (z))=1τ (±n + h/p)
21(±n+h/p,P (z))=1.

By Lemma 3.1(i) this is

≪ h
ϕ(h) X log X ∑

p|h
z≤p≤4X
 u9

p log2(8X/p) ≪ h
ϕ(h) X
log X u10

z

since z = X 1/u ≤ X 1/2. On the other hand, those n with (n, h) = 1 contribute
to (21) by (12)

≪ ∑

z≤m≤4X/z
(m,hP (z))=1
 λ(m) ∑

z≤ℓ≤4X/m
(±ℓm+h,P (z))=1
 Λ(ℓ)τ (±ℓm + h)
2

≪ log X ∑

z≤m≤4X/z
(m,hP (z))=1
 λ(m) ∑

z≤ℓ≤4X/m
(±ℓm+h,P (z))=1
 1(ℓ,P (x1/4))=1τ (±ℓm + h)
2.

The claim follows from applying Lemma 3.1(ii) to the inner sum. □

Proof of (15). We have, for any r1, r2, r3 ≥ 0,
∑

m1,m2,n1,n2
m1n1≤10X
±m1n1+h=m2n2
(n1,P (zr1 ))=(n2,Ph(zr2 ))=1
(m1,P (zr3 ))=(m2,hP (z))=1
(τ (m1)τ (n1)τ (n2))
A+1

≪ ∑

n≤10X τ (n)
2A+3τ (±n + h)
A+21(n,P (min{zr1 ,zr3 }))=11(±n+h,Ph(zr2 ))=1.

By Lemma 3.1(i) and recalling the deﬁnition of zr from (14), the left hand side
of (15) is

≪A h
ϕ(h) X
log2 X
 ∑

r1,r2,r3≥0
max rj ≥ u
1000 −β
 2−A(r1+r2+r3) ( log X
log min{zr1, zr3}
 )2
2A+3+1 ( log X
log zr2
 )2
A+2

≪ h
ϕ(h) X
log2 X u2
2A+5 ∑

r1,r2,r3≥0
max rj ≥ u
1000 −β
 2−A(r1+r2+r3) ( β
β − 1
 )2
2A+4(r1+r2+r3) .

SIEGEL ZEROS AND PRIMES 13

Once β is large enough in terms of A, this is

≪A h
ϕ(h) X
log2 X u2
2A+52−0.9Au/1000 ≪A h
ϕ(h) X
log2 X e−Au/2000.
 □

3.2. Sieves. The following is a technical version of the fundamental lemma of the
sieve. For the standard version, see e.g. [2, Lemma 6.11].

Lemma 3.2. Let θ ∈ (0, 1/3) and A ∈ N. There exists β0 = β0(A) ≥ 2 such that
the following holds for any β ≥ β0 and u ≥ β/θ.
Let X ≥ 2, write D = X θ and z = X 1/u, and deﬁne

zr := z((β−1)/β)
r

Then there exist coeﬃcients λd with |λd| ≤ 1 supported on d ≤ D such that the
following hold.

(i) For every n ∈ N and any v ∈ N,

1(n,Pv(z))=1 = ∑

d|(n,Pv(z)) λd + O
 

 ∑

r≥uθ−β 2−Ar1(n,Pv(zr))=1τ (n)
A+1


 .

(ii) If g : N → [−1, 1] is a multiplicative function for which |g(p)| ≤ 2/p for every
prime p, then
∑

d|P (z) λdg(d) = (1 + Oβ,A(e−Aθu/2)) ∏

p<z(1 − g(p))

Proof. Deﬁne

D := {d = p1 · · · pr | P (z) : p1 > p2 > . . . > pr, p1 · · · pmpβ
m < D for all odd m}

and deﬁne the upper bound β-sieve weights λd = µ(d)1d∈D.
Proof of (i). Consider ﬁrst the case v = 1. By the deﬁnition of λd, we have
(see e.g. [2, (6.29) with A = {n}]),

1(n,P (z))=1 = ∑

d|(n,P (z)) λd − ∑

r odd Sr(n),

where
 Sr(n) := ∑

n=p1···prk
pr<pr−1<...<p1<z
p1p2···prp
β
r ≥D
p1···php
β
h<D for all odd h < r
 1(k,P (pr ))=1

Since pj < z and p1p2 · · · prpβ
r ≥ D, the sum in Sr(n) is non-empty only if (r +
β)/u ≥ θ ⇐⇒ r ≥ uθ − β.
Furthermore, since log D
log z = uθ ≥ β, one can easily show that, for every r, in
the sum deﬁning Sr(n) one has pr ≥ zr (see e.g. [12, Section 6.3]). We write
m = p1 · · · pr so that obviously 2A(ω(m)−r) ≥ 1. Hence

Sr(n) ≤ ∑

n=mk
p|mk =⇒ p≥zr
 2Aω(m)−Ar ≤ 2−Arτ (n)
A+11(n,P (zr))=1,

and (i) follows in case v = 1.

14 KAISA MATOM ¨AKI AND JORI MERIKOSKI

When v > 1, we write n = n′v′ with (n′, v) = 1 and p | v′ =⇒ p | v. Then
(n, Pv(w)) = (n′, P (w)) for every w ≥ 2. Hence, by the case v = 1, we obtain

1(n,Pv(z))=1 = 1(n′,P (z))=1 = ∑

d|(n
′,P (z)) λd + O
 

 ∑

r≥uθ−β 2−Ar1(n′,P (zr))=1τ (n′)
A+1




= ∑

d|(n,Pv(z)) λd + O
 

 ∑

r≥uθ−β 2−Ar1(n,Pv(zr))=1τ (n)
A+1




as claimed.
Proof of (ii). By the deﬁnition of λd we have (see e.g. [2, (6.31)])

(22) ∑

d|P (z) λdg(d) = ∏

p<z(1 − g(p)) − ∑

r odd Vr(z),

where
 Vr(z) := ∑

pr <pr−1<...<p1<z
p1p2···prp
β
r ≥D
p1···php
β
h<D for all odd h < r
 g(p1 · · · pr) ∏

p<pr(1 − g(p)).

As in (i), only r ≥ uθ − β contribute and pr ≥ zr. Hence, writing m = p1 · · · pr and
using again 1 ≤ 2A(ω(m)−r), we obtain

Vr(z) ≤ ∏

p<z (1 − g(p)) ∏

zr ≤p≤z(1 + |g(p)|) ∑

m
p|m =⇒ zr≤p<z
 2A(ω(m)−r)|µ(m)|g(m).

Since |g(p)| ≤ 2/p, we get, using (19) and (20),

Vr(z) ≤ 2−Ar ∏

p<z (1 − g(p)) ∏

zr ≤p≤z
 (
1 + 2
p
 ) (
1 + 2A+1

p
 )

≪ 2−Ar ( log z
log zr
 )2
A+1+2 ∏

p<z (1 − g(p))

≪ 2−Ar ( β
β − 1
 )(2
A+1+2)r ∏

p<z (1 − g(p)) .

Now, once β is large enough in terms of A,

∑

r≥uθ−β 2−Ar ( β
β − 1
 )(2
A+1+2)r ≪β,A 2−0.9Auθ ≤ e−Auθ/2

and the claim follows. □

Lemma 3.3. Let the assumptions and λd be as in Lemma 3.2 and let v, q ∈ N.
Then ∑

d1,d2|P (z)
(d2,d1v)=1
(d1d2,q)=1
 λd1 λd2
d1d2 = (1 + Oβ,A (e−Auθ/2)) ∏

p<z
p∤q
 (1 − 1
p
 ) ∏

p<z
p∤vq
 (
1 − 1
ϕ(p)
 ) .
(23)

Proof. We have to be somewhat careful here due to the condition (d1, d2) = 1 (see
also [2, Section 5.9]).
 SIEGEL ZEROS AND PRIMES 15

By (22) with g(d) = 1(d,d2q)=1
d , we can write

∑

d1|P (z)
(d1,d2q)=1
 λd1
d1 = ∏

p<z
p∤d2q
 (
1 − 1
p
 ) − ∑

r≥uθ−β
r odd
 ∑

pr<pr−1<...<p1<z
p1p2···pr p
β
r ≥D
p1···php
β
h<D for all odd h < r
pj ∤d2q
 1
p1 · · · pr
 ∏

p<pr
p∤d2q
 (1 − 1
p
 ) .

(24)

Using Lemma 3.2(ii) we see that the ﬁrst term on the right hand side contributes
to the left hand side of (23)

∑

d2|P (z)
(d2,vq)=1
 λd2
d2
 ∏

p<z
p∤d2q
 (
1 − 1
p
 ) = ∏

p<z
p∤q
 (
1 − 1
p
 ) ∑

d2|P (z)
(d2,vq)=1
 λd2
ϕ(d2)

= ∏

p<z
p∤q
 (
1 − 1
p
 ) (1 + Oβ,A(e−Auθ/2)) ∏

p<z
p∤vq
 (1 − 1
ϕ(p)
 ) .

Let us now consider the contribution of the r-sum in (24) to the left hand side
of (23). Writing m = p1 · · · pr−1 so that 2A(ω(m)−r) ≥ 1/2A and recalling from the
proof of Lemma 3.2 that pr ≥ zr, this contribution is

≪A ∑

r≥uθ−β 2−Ar ∑

zr≤pr <z
pr ∤q
 1
pr
 ∑

m≤D/pr
(m,q)=1
p|m =⇒ pr <p<z
 2Aω(m)

m
 ∏

p<pr
p∤q
 (
1 − 1
p
 )

·
 ∣
∣
∣
∣
∣
 ∑

d2|P (z)
(d2,vqmpr )=1
 λd2
d2
 ∏

p<pr
p|d2
 (
1 − 1
p
 )−1∣
∣
∣
∣
∣
.

Applying Lemma 3.2(ii) and recombining the variables m and pr ≥ zr, and applying
then (19) and (20), this is

≪ ∑

r≥uθ−β 2−Ar ∑

m≤D
(m,q)=1
p|m =⇒ zr≤p<z
 2Aω(m)

ϕ(m)
 ∏

p<zr
p∤q
 (
1 − 1
p
 ) ∏

p<z
p∤vq
 (
1 − 1
ϕ(p)
 )

≪ ∏

p<z
p∤vq
 (
1 − 1
ϕ(p)
 ) ∏

p<z
p∤q
 (
1 − 1
p
 ) ∑

r≥uθ−β 2−Ar ∏

zr≤p<z
p∤q
 (
1 + 2A + 1
p
 )

≪ ∏

p<z
p∤vq
 (
1 − 1
ϕ(p)
 ) ∏

p<z
p∤q
 (
1 − 1
p
 ) ∑

r≥uθ−β 2−Ar ( β
β − 1
 )(2
A+1)r

≪β,A e−Auθ/2 ∏

p<z
p∤vq
 (
1 − 1
ϕ(p)
 ) ∏

p<z
p∤q
 (
1 − 1
p
 )

once β is large enough. □

3.3. Poisson summation. Let us state the version of the Poisson summation
formula we shall use.

16 KAISA MATOM ¨AKI AND JORI MERIKOSKI

Lemma 3.4. Let b ∈ Z, d, q ∈ N with (d, bq) = 1, let f : R → C be such that
f, ̂f ∈ L1(R) and have bounded variation. Let g : R → C be q-periodic. Then
∑

m≡b (d) f (m)g(m) = 1
dq
 ∑

h ̂f ( h
dq
 ) ∑

m (dq)
m≡b (d)
 g(m)e ( hm
dq
 )

Proof. Write
∑

m≡b (d) f (m)g(m) = ∑

a (q) g(a) ∑

m≡b (d)
m≡a (q)
 f (m) = ∑

a (q) g(a) ∑

k f (ca + dqk),

where ca is such that ca ≡ b (d) and ca ≡ a (q). By Poisson summation (see e.g. [12,
formula (4.24)], the above equals
∑

a (q) g(a) 1
dq
 ∑

h ̂f ( h
dq
 ) e ( hca
dq
 ) = 1
dq
 ∑

h ̂f ( h
dq
 ) ∑

a (q) g(a)e ( hca
dq
 )

= 1
dq
 ∑

h ̂f ( h
dq
 ) ∑

c (dq)
c≡b (d)
 g(c)e ( hc
dq
 ) .
 □

3.4. Character sums.

Proof of Lemma 2.5. Since χ is a primitive quadratic character of modulus q = 2rq′

with 2 ∤ q′, we have that r ∈ {0, 2, 3} and q′ is square-free (see e.g. [12, Section
3.3]). Hence, by the Chinese reminder theorem it suﬃces to consider the prime case
q = p > 2 and the case q = 2r with r ∈ {2, 3}.
Proof of (16). For p > 2,

∑

m (p) χ0(m)χ0(±m + h) =
 {p − 1 = ϕ(p) if p | h;
p − 2 if p ∤ h.

and, for r ∈ {2, 3} and even h,
∑

m (2r ) χ0(m)χ0(±m + h) = ∑

m (mod 2
r )
(m,2)=1
 1 = 2r−1 = ϕ(2r).

Combining these, (16) follows.
Proof of (17). For p > 2,
∑

m (p) χ(m)χ0(±m + h) = ∑

m (p) χ(m) − χ(∓h) = −χ(∓h).

and, for r ∈ {2, 3} and even h,
∑

m (2r ) χ(m)χ0(±m + h) = ∑

m (2r ) χ(m) = 0 = −χ(∓h).

Combining these, (17) follows.
Proof of (18). For p > 2,
∑

m (p) χ(m(±m + h)) = ∑

m (p)
(m,p)=1
 χ(m(±m + h)) = χ(±1) ∑

m (p)
(m,p)=1
 χ(m)
2χ(1 ± hm)

= χ(±1) ∑

m (p)
(m,p)=1
 χ(1 ± hm) = χ(±1)
 

 ∑

m (p) χ(1 ± hm) − χ(1)



 = χ(±1)
 {
p − 1 if p | h;
−1 if p ∤ h.

SIEGEL ZEROS AND PRIMES 17

Similarly, for r = 2, 3 and even h,
∑

m (2r) χ(m(±m + h)) = ∑

m (2
r )
(m,2)=1
 χ(m(±m + h)) = χ(±1) ∑

m (2
r )
(m,2)=1
 χ(m)
2χ(1 ± hm)

= χ(±1) ∑

m (2
r )
(m,2)=1
 χ(1 ± hm) = χ(±1)
 

 ∑

m (2
r ) χ(1 ± hm) − 1
2
 ∑

m (2
r) χ(1 ± 2hm)





It is easy to see that, for r = 2, 3 and even h, the expression in the parentheses
equals

2r12r|h − 2r−112r−1|h = 2r−112r−1|h(−1) h
2r−1 = ϕ(2r)1ϕ(2r )|h(−1)
 h
ϕ(2r ) ,

where the last formulation is such that it is 1 for r = 0 when h is even. Combining
these, (17) follows. □

3.5. Kloosterman sums. For integers a, b, c with c ≥ 1 we denote the Klooster-
man sum by
 S(a, b; c) := ∑

n (c)
(n,c)=1
 ec(an + b¯n).

We shall use the Weil bound (see e.g. [12, Corollary 11.12]).

Lemma 3.5. Let a, b ∈ Z and c ∈ N. Then, for any ε > 0

S(a, b; c) ≪ε c1/2+ε(a, b, c)
1/2.

Remark 3.6. We could alternatively use a more elementary bound S(a, b; c) ≪ε
c3/4+ε(a, b, c)
1/4 due to Kloosterman (see [14, Lemma 4] with Λ = 1), and this
would only somewhat increase the exponent of q in the conditions of the type
X ≥ q10 and h ≥ q10 in our theorems and corollaries.

We also need the following rough bounds.

Lemma 3.7. Let L ≥ 1. For any integer q ̸= 0 we have
∑

1≤ℓ≤L(ℓ, q) ≤ τ (q)L

and ∑

1≤ℓ≤L(ℓ, q) ℓ
ϕ(ℓ) ≪ τ (q)
2L.

Proof. Writing d = (ℓ, q) and ℓ = kd, we have
∑

1≤ℓ≤L
(ℓ, q) ≤ ∑

d|q d ∑

1≤k≤ L
d
 1 ≤ L ∑

d|q 1 = τ (q)L.

Similarly, using also ϕ(dk) ≥ ϕ(d)ϕ(k) and ∑k≤K k
ϕ(k) ≪ K we get

∑

1≤ℓ≤L
(ℓ, q) ℓ
ϕ(ℓ) ≤ ∑

d|q
 d
2

ϕ(d)
 ∑

1≤k≤L/d
 k
ϕ(k) ≪ ∑

d|q
 Ld
ϕ(d) = L ∏

p|q
 (
1 + p
ϕ(p)
 ) ≤ τ (q)
2L.

□

From Lemma 3.5 we obtain the following bound for incomplete Kloosterman
sums via Poisson summation.

18 KAISA MATOM ¨AKI AND JORI MERIKOSKI

Lemma 3.8. Let δ, ε > 0 and N ≥ 1. Let F : R → C be a bounded smooth
compactly supported function and suppose that for some δ ∈ (0, 1) we have |F ′′| ≪
δ−2. Then, for any integers α, d, e, q, k with d, q ≥ 1 and (eq, d) = 1, we have

∑

n≡α (q)
(n,d)=1
 F ( n
N
 )
ed(ken) ≪ε δ−1d
1/2+ε + N (d, k)
dq .

Proof. Applying Poisson summation (Lemma 3.4 with d-periodic g(n) = 1(n,d)=1ed(ken)),
we obtain ∑

n≡α (q)
(n,d)=1
 F ( n
N
 )
ed(ken) = N
dq
 ∑

h ̂F ( hN
dq
 ) ∑

n (dq)
n≡α (q)
(n,d)=1
 ed(ken)edq(hn).

Since (d, q) = 1, by the Chinese remainder theorem we can write n = αd ¯d + βq ¯q,
where ¯d is inverse (mod q) and ¯q is inverse (mod d) to get

∑

n≡α (q)
(n,d)=1
 F ( n
N
 )
ed(ken) = N
dq
 ∑

h ̂F ( hN
dq
 )
eq(hα ¯d) ∑

β (d)
(β,d)=1
 ed(h¯qβ + keβ)

= N
dq
 ∑

h ̂F ( hN
dq
 )
eq(hα ¯d)S(h¯q, k¯e; d).

(25)

For h = 0 we have a Ramanujan sum (see e.g. [12, (3.1) and (3.5)])

S(0, k¯e; d) = ∑

n (d)
(n,d)=1
 ed(ken) ≪ (d, k).

The contribution from this to (25) is

≪ N (d, k)
dq | ̂F (0)| ≪ N (d, k)
dq .

For h ̸= 0 we get by integration by parts

̂F ( hN
dq
 ) ≪ min {1, ∣
∣
∣
∣δ hN
dq
 ∣
∣
∣
∣
−2}
.

Hence, by Lemmas 3.5 and 3.7 we get

N
dq
 ∑

h̸=0 ̂F ( hN
dq
 )
eq(hα ¯d)S(h¯q, k¯e; d) ≪ε d
1/2+ε/2 N
dq
 ∑

h̸=0
(h, d) min {
1, ∣
∣
∣
∣δ hN
dq
 ∣
∣
∣
∣
−2}

≪ε δ−1d
1/2+ε.
 □

4. Proof of Lemma 2.2

The following lemma is essentially [19, Proposition 3.5], but we provide the proof
also here for completeness.

Lemma 4.1. Let χ be a primitive quadratic character modulo q ≥ 2. Assume that
L(s, χ) has a real zero β0 such that

β0 = 1 − 1
η log q

SIEGEL ZEROS AND PRIMES 19

for some η ≥ 10. Let δ > 0. Then, for any Y > q1/2+δ, one has

∑

q1/2+δ <p≤Y
 λ(p)
p ≪δ log Y
η log q ,

and, for any k ≥ 2, one has
 ∑

q(1/2+δ)/k <p≤q(1/2+δ)/(k−1)
 λ(p)
p ≪δ k
η1/k .

Proof. We may assume that η is large since otherwise the claims are trivial. By
[17, Excercise 3(g) in Section 11.2.1] we have for any y ≥ q1/2+δ

∑

m≤y
 λ(m)
m = L(1, χ)(log y + γ) + L′(1, χ) + Oδ(q−δ/3),

where γ is the Euler-Mascheroni constant (see [17, formula (1.27)]). Using Siegel’s
bound L(1, χ) ≫δ q−δ/4 (see e.g. [17, Theorem 11.14]) we get

(26) ∑

m≤y
 λ(m)
m = L(1, χ) (
log y + L′(1, χ)
L(1, χ) + Oδ(1)
) .

By [17, Theorem 11.4] we have

L′(1, χ)
L(1, χ) = η log q + O(log q) ≍ η log q

as we assumed that η is large. Plugging this into (26) with y = q1/2+δ we obtain

(27) ∑

m≤q1/2+δ
 λ(m)
m ≫δ ηL(1, χ) log q.

Also, subtracting (26) for y = q1/2+δ and y = Y q1/2+δ gives

(28) ∑

q1/2+δ <m≤Y q1/2+δ
 λ(m)
m = L(1, χ)(log Y + Oδ(1)).

On the other hand, by non-negativity and multiplicativity of λ(n) we get

∑

q1/2+δ <m≤Y q1/2+δ
 λ(m)
m ≥ ∑

q1/2+δ <m≤Y q1/2+δ

m=pn, n≤q1/2+δ <p
 λ(m)
m ≥ ∑

n≤q1/2+δ
 λ(n)
n
 ∑

q1/2+δ <p≤Y
 λ(p)
p .

The ﬁrst bound in the lemma now follows by (28) and (27).
Similarly, for the second bound we write m = np1 · · · pk to get

∑

q1/2+δ <m≤q3
 λ(m)
m ≥ ∑

q1/2+δ <m≤q3

m=p1···pkn, n≤q1/2+δ

q(1/2+δ)/k<p1,...,pk≤q(1/2+δ)/(k−1)

p1,...,pk∤n,pj distinct
 λ(m)
m
(29)

Now, for m ≤ q3 we have

∑

p1···pk|m
q(1/2+δ)/k <p1,...,pk≤q(1/2+δ)/(k−1)
 1 ≤ k!(
6k
k
 ) ≤ k!(1 + 1)
6k = k!26k.

20 KAISA MATOM ¨AKI AND JORI MERIKOSKI

Using this and (29) we see that
∑

q1/2+δ <m≤q3
 λ(m)
m ≫ 1
k!26k ∑

n≤q1/2+δ
 λ(n)
n
 ∑

q(1/2+δ)/k<p1,...,pk≤q(1/2+δ)/(k−1)

p1,...,pk∤n
pj distinct
 λ(p1) · · · λ(pk)
p1 · · · pk .

Once we have ﬁxed p1, . . . , pj−1, to make sure that pj is distinct from p1, . . . , pj−1
we have to exclude j − 1 ≤ k primes. To ensure that also pj ∤ n we have to further
remove at most k primes. Let P be the set of 2k smallest primes > q(1/2+δ)/k such
that λ(p) = 2. Then by positivity we get

∑

q1/2+δ <m≤q3
 λ(m)
m ≫ 1
k!26k ∑

n≤q1/2+δ
 λ(n)
n
 ( ∑

q(1/2+δ)/k <p≤q(1/2+δ)/(k−1)

p /∈P
 λ(p)
p
 )k.

Using (28) and (27) we get
( ∑

q(1/2+δ)/k <p≤q(1/2+δ)/(k−1)

p /∈P
 λ(p)
p
 )k ≪δ 26kk!
η ,

which gives us ∑

q(1/2+δ)/k <p≤q(1/2+δ)/(k−1)

p /∈P
 λ(p)
p ≪ k
η1/k .

The primes p ∈ P can be inserted back in with an error term O(4kq−(1/2+δ)/k). By
Siegel’s bound (6) this error is O(kη−1/k), and the second claim follows. □

Proof of Lemma 2.2. First note that we can assume that

(30) 1
v2ηv/2 + v
η log Y
log z ≤ 1

since otherwise the claim follows trivially from λ(m) ≤ τ (m), (19), and (20).
We write
∑

z≤m≤Y
(m,P (z))=1
 λ(m)
m = ∑

z≤m≤Y
(m,P (z))=1
 |µ(m)|λ(m)
m + ∑

z≤m≤Y
(m,P (z))=1
 (1 − |µ(m)|)λ(m)
m .
(31)

For the second sum we get by (19) and (20)

∑

z≤m≤Y
(m,P (z))=1
 (1 − |µ(m)|)λ(m)
m ≪ ∑

p≥z
 1
p2 ∑

m≤Y /p
2

(m,P (z))=1
 τ (m)
m ≪ 1
z
 ( log Y
log z
 )2 .

In the ﬁrst sum on the right hand side of (31) we have
∑

z≤m≤Y
(m,P (z))=1
 |µ(m)|λ(m)
m ≤ ∏

z≤p≤Y
 (
1 + λ(p)
p
 ) − 1 ≤ ∏

z≤p≤Y exp ( λ(p)
p
 ) − 1

= exp
 

 ∑

z≤p≤Y
 λ(p)
p
 

 − 1.

(32)

Let δ > 0 be small and let

K := ⌈ 1/2 + δ
v
 ⌉ ≥ max {1, 1/2 + δ
v
 } ,

SIEGEL ZEROS AND PRIMES 21

so that z = qv ≥ q 1/2+δ
K . It is easy to see that either K ≤ 2/v or K = 1. Then by
Lemma 4.1

∑

z≤p≤Y
 λ(p)
p ≤ ∑

2≤k≤K
 ∑

q(1/2+δ)/k <p≤q(1/2+δ)/(k−1)
 λ(p)
p + ∑

q1/2+δ<p≤Y
 λ(p)
p

≪δ K 2η−1/K + log Y
η log q ≪ 1
v2ηv/2 + v
η log Y
log z .

Plugging this in (32) and using (30) we obtain

∑

z≤m≤Y
(m,P (z))=1
 |µ(m)|λ(m)
m ≤ exp
 

 ∑

z≤p≤Y
 λ(p)
p
 

 − 1 ≪ 1
v2ηv/2 + v
η log Y
log z

and the claim follows. □

5. Proof of Proposition 2.3

Let us study

S± := ∑

m1,m2,n1,n2
±m1n1+h=m2n2
(m1m2n1n2,P (z))=1
 χ1(m1)χ2(m2)ψ1(n1)ψ2(n2)f ( m1
M1 , m2
M2 , n1
N1 , n2
N2
 ) .

First we wish to make the variable n2 implicit, so we write the above as

∑

m1,m2,n1,n2
±m1n1+h=m2n2
(m1m2n1n2,P (z))=1
 χ1(m1)χ2(m2)ψ1(n1)ψ2
( ±m1n1 + h
m2
 )
f ( m1
M1 , m2
M2 , n1
N1 , ±m1n1 + h
m2N2
 ) .

Let us now show that we can replace the conditions (m2, P (z)) = 1 and (n2, P (z)) =
1 by the conditions (m2, hP (z)) = 1 and (n2, Ph(z)) = 1. These two sets of con-
ditions are equivalent unless (m2n2, h) > 1. But (m2n2, h) | m1n1, so in this case
there must be a prime p ≥ z such that p | m2n2, p | h and p | m1n1. Using
Lemma 3.1(i) we see that the error introduced from these changes of summation
conditions is

≪ ∑

p|h
z≤p≪X
 ∑

m≪X/p
(±m+h/p,Ph(z))=1
(m,P (z))=1
 τ (m)τ (±m + h/p) ≪ h
ϕ(h) Xu5 ∑

p|h
z≤p≪X
 1
p log2(X/p)

≪ h
ϕ(h) X
log2 X u6

z .

Hence we can replace the condition (m2n2, P (z)) = 1 by conditions (m2, hP (z)) = 1
and (n2, Ph(z)) = 1.

22 KAISA MATOM ¨AKI AND JORI MERIKOSKI

Next we shall replace the conditions (m1n1, P (z)) = 1 and (n2, Ph(z)) = 1 by
sieve weights. By Lemma 3.2(i) with θ = 1/1000 we can write

1(n2,Ph(z))=1 = ∑

d2|(n2,P (z))
(d2,h)=1
 λd2 + O
 

 ∑

r2≥u/1000−β 2−Ar21(n2,Ph(zr2 ))=1τ (n2)
A+1




1(n1,P (z))=1 = ∑

d1|(n1,P (z)) λd1 + O
 

 ∑

r1≥u/1000−β 2−Ar11(n1,P (zr1 ))=1τ (n1)
A+1




1(m1,P (z))=1 = ∑

e|(m1,P (z)) λe + O
 

 ∑

r3≥u/1000−β 2−Ar31(m1,P (zr3 ))=1τ (m1)
A+1


 .

Using this, and noticing that e.g. 1(m1,P (z))=1 ≤ 2−A·01(m1,P (z0))=1τ (m1)
A+1, we
obtain

S± = ∑

d1d2|P (z)
(d2,h)=1
 λd1 λd2 ∑

e|P (z) λe ∑

m1,m2
(m2,hP (z))=1
 χ1(em1)χ2(m2)ψ2(m2)W (d1, d2, em1, m2)

+ O ( h
ϕ(h) X
log2 X u6

z
 ) + O
( ∑

r1,r2,r3≥0
max rj ≥ u
1000 −β
 2−A(r1+r2+r3)

· ∑

m1,m2,n1,n2
±m1n1+h=m2n2
(n1,P (zr1 ))=(n2,Ph(zr2 ))=1
(m1,P (zr3 ))=(m2,hP (z))=1
(τ (m1)τ (n1)τ (n2))
A+1f ( m1
M1 , m2
M2 , n1
N1 , ±m1n1 + h
m2N2
 ))

with
 W (d1, d2, em1, m2) := ∑

n1
±em1d1n1≡−h (d2m2)
 ψ1(d1n1)ψ2(±em1d1n1 + h)

· f ( em1
M1 , m2
M2 , d1n1
N1 , ±em1d1n1 + h
m2N2
 ) .

We can concentrate on the main term. Note that since (d2m2, h) = 1, we can add
the condition (em1d1, d2m2) = 1. Due to the support of χ and ψ (noting that
d2m2 | ±em1d1n1 + h) we can also add conditions (d1d2em1m2, q) = 1. Hence we
need to study

∑

d1d2|P (z)
(d2,d1h)=1
(d1d2,q)=1
 λd1 λd2 ∑

e|P (z)
(e,d2q)=1
 λe ∑

m1,m2
(m2,hP (z))=1
(em1d1,d2m2)=1
(m1m2,q)=1
 χ1(em1)χ2(m2)ψ2(m2)W (d1, d2, em1, m2).

(33)

Now ∫ f ( em1
M1 , m2
M2 , d1y
N1 , ±em1d1y + h
m2N2
 ) e(ky)dy

= 1
em1d1
 ∫ f ( em1
M1 , m2
M2 , y
em1N1 , ±y + h
m2N2
 ) e (
k y
em1d1
 ) dy,

SIEGEL ZEROS AND PRIMES 23

so by Poisson summation (Lemma 3.4) we get

W (d1, d2, em1, m2) = 1
d1d2em1m2q
 ∑

k∈Z
 ∫ f ( em1
M1 , m2
M2 , y
em1N1 , ±y + h
m2N2
 )

· e (
k y
d1d2em1m2q
 ) dy ∑

n (qd2m2)
±n≡−hd1em1 (d2m2)
 ψ1(d1n)ψ2(±em1d1n + h)eqd2m2(kn).

(34)

By the Chinese remainder theorem we can write

n = ∓q ¯qhd1em1 + d2m2γ,

so that ∑

n (qd2m2)
n≡−hd1em1 (d2m2)
 ψ1(d1n)ψ2(±em1d1n + h)eqd2m2(kn)

= ed2m2 (∓¯qhkd1em1) ∑

γ (q) ψ1(d1d2m2γ)ψ2(±γd1d2em1m2 + h)eq(kγ).
(35)

5.1. Contribution from k = 0. Since in (33) we have (em1d1d2m2, q) = 1, writing
γ′ = γem1d1d2m2 we get
∑

γ (q) ψ1(d1d2m2γ)ψ2(±γd1d2em1m2 + h) = ψ1(em1) ∑

γ′ (q) ψ1(γ′)ψ2(±γ′ + h)

=: ψ1(em1)U ±(h; q),

say. Recombining the variables e, m1, we see that the contribution from the part
of (34) with k = 0 to (33) is

U ±(h; q)
q
 ∑

m1,m2
(m2,hP (z))=1
(m1,m2)=1
 χ1(m1)χ2(m2)ψ1(m1)ψ2(m2)
m1m2
 ( ∑

d1,d2|P (z)
(d2,d1hm1)=1
(d1d2,q)=1
 λd1 λd2
d1d2
 )

· ∫ f ( m1
M1 , m2
M2 , y
m1N1 , ±y + h
m2N2
 ) dy ∑

e|(m1,P (z)) λe

(36)

(here we were able to drop the condition (d1, m2) = 1 since d1 | P (z) and (m2, P (z)) =
1). Notice that by Lemma 3.3 with θ = 1/1000 and (16) we have, for m1 ∈ N,

U ±(h; q)
q
 ∑

d1,d2|P (z)
(d2,d1hm1)=1
(d1d2,q)=1
 λd1λd2
d1d2

= U ±(h; q)
q
 (1 + OA (
e−Au/2000)) ∏

p<z
p∤q
 (
1 − 1
p
 ) ∏

p<z
p∤hqm1
 (
1 − 1
ϕ(p)
 )

≪ u2

log2 X h
ϕ(h) m1
ϕ(m1) .

(37)

Using Lemma 3.2(i) and (37) we see that replacing the sum over e in (36) by
1(m1,P (z))=1 aﬀects (36) by

≪ h
ϕ(h) X
log2 X u2 ∑

r≥u/1000−β 2−Ar ∑

m1≪M1,m2≪M2
(m1,P (zr))=(m2,P (z))=1
 τ (m1)
A+1

ϕ(m1)m2 .

24 KAISA MATOM ¨AKI AND JORI MERIKOSKI

Using (19) and (20), and taking β suﬃciently large in terms of A, this is, as in our
earlier arguments,
 ≪A h
ϕ(h) X
log2 X e−Au/3000

Using also the equality in (37), handling the error term with (19) and (20), we
obtain that (36) equals

U ±(h; q)
q
 ∑

m1,m2
(m1m2,P (z))=1
(m1,m2)=1
 χ1(m1)χ2(m2)ψ1(m1)ψ2(m2)
m1m2
 ∏

p<z
p∤q
 (1 − 1
p
 ) ∏

p<z
p∤hq
 (
1 − 1
ϕ(p)
 )

· ∫ f ( m1
M1 , m2
M2 , y
m1N1 , ±y + h
m2N2
 ) dy + O ( h
ϕ(h) X
log2 X e−Au/3000)

Finally we need to remove the condition (m1, m2) = 1. Since (m1m2, P (z)) = 1,
using (37) and then (19) and (20), this introduces an error

≪ h
ϕ(h) X
log2 X u2 ∑

z≤p≤X
 1
p(p − 1)
 ∑

m1,m2≤X
(m1m2,P (z))=1
 1
ϕ(m1)m2 ≪ h
ϕ(h) X
log2 X u4

z .

5.2. Contribution from k ̸= 0. By partial integration we have, for k ̸= 0,
∫ f ( em1
M1 , m2
M2 , y
em1N1 , ±y + h
m2N2
 ) e (
k y
d1d2em1m2q
 ) dy

≪j
 ( k
d1d2M1M2q
 )−j ( δ−1

M1N1 + δ−1

M2N2
 )j ≪j
 ( δ−1d1d2M1M2q
kX
 )j .

Hence |k| > X ε qd1d2M1M2
δX contribute O(X −100) to (34). The remaining part con-
tributes to (33) by (34) and (35)

∑

d1d2|P (z)
(d2,d1h)=1
(d1d2,q)=1
 λd1 λd2 ∑

e|P (z)
(e,d2q)=1
 λe ∑

m1,m2
(m2,hP (z))=1
(em1d1,d2m2)=1
(m1m2,q)=1
 χ1(em1)χ2(m2)ψ2(m2)

· 1
qd1d2em1m2
 ∑

0<|k|≤ qd1 d2 M1M2
δX1−ε
 ∫ f ( em1
M1 , m2
M2 , y
em1N1 , ±y + h
m2N2
 ) e (
k y
d1d2em1m2q
 ) dy

· ed2m2(∓¯qhkd1em1) ∑

γ (q) ψ1(d1d2m2γ)ψ2(±γd1d2em1m2 + h)eq(kγ)

(38)

We write ∫ f ( em1
M1 , m2
M2 , y
em1N1 , ±y + h
m2N2
 ) e (
k y
d1d2em1m2q
 ) dy

= m1
 ∫ f ( em1
M1 , m2
M2 , y
eN1 , ±ym1 + h
m2N2
 ) e (
k y
d1d2em2q
 ) dy

and rearrange (38) so that the sum over m1 is innermost. Splitting also the sum
over m1 into congruence classes modulo q, (38) is bounded by

≪ε q2X ε ∑

e|P (z)
e≤D
 ∑

(m2,P (z))=1
m2≪M2
 ∑

d1d2|P (z)
d1,d2≤D
(d2,h)=1
 1(d1eq,d2m2)=1

· X
qd1d2M1M2
 ∑

0<|k|≤ qd1 d2M1 M2
δX1−ε
 |Υ(h, k, e, q, d1; d2m2)| ,

(39)
 SIEGEL ZEROS AND PRIMES 25

where, for some reduced residue α (q) and y ≍ eN1, we have

Υ(h, k, e, q, d1; d2m2) := ∑

m1≡α (q)
(m1,d2m2)=1
 f ( em1
M1 , m2
M2 , y
eN1 , ±ym1 + h
m2N2
 ) ed2m2 (∓¯qhkd1em1)

which is an incomplete Kloosterman sum modulo d2m2. Applying Lemma 3.8 we
get
 Υ(h, k, e, q, d1; d2m2) ≪ε δ−1(d2m2)
1/2+ε + M1(hk, d2m2)
ed2m2q .

Hence (39) is bounded by (using Lemma 3.7 and that D = X 1/1000 and M2 ≪
(M2N2)
1/2 ≪ (δ−1X)
1/2)

≪ε q2X 2ε(
δ−2D3+1/2 ∑

m2≪M2 m1/2
2

+ ∑

e≤D
 ∑

d1,d2≤D
m2≪M2
 X
qd1d2M1M2
 ∑

0<|k|≤ qd1 d2M1M2
δX1−ε
 M1(hk, d2m2)
ed2m2q
 )

≪ε q2X 2εδ−2D7/2(δ−1X)
(1/2)·(3/2) + qX 4εδ−1DM1 ≪ δ−3X 7/9q2,

and the claim follows.
 6. Proof of Lemma 2.4

Recalling that z = X 1/u, by (20) it suﬃces to show that

∑

n≤N
(n,P (z))=1
 χ(n) log(y/n)
n = ∏

p<z
 (
1 − 1
p
 )−1 + O (( u3

v2ηv/2 + u4v
η
 ) log X)

+ OA
 (( u3

z + e−Au/3000) log X) + Oε,C (exp(−C log3/5−ε X)
) .

We ﬁrst replace χ(n) by µ(n) in the sum. We have

χ(n) = (λ ∗ µ)(n) = µ(n) + ∑

n=km
m>1
 µ(k)λ(m),

so that (analogously to (11))

∑

n≤N
(n,P (z))=1
 χ(n) log(y/n)
n = ∑

n≤N
(n,P (z))=1
 µ(n) log(y/n)
n + ∑

km≤N
(km,P (z))=1
m≥z
 µ(k)λ(m) log y
km
km .

(40)

Using Lemma 2.2 the second term gives (by (19) and (20)) an admissible contribu-
tion
 ≪ log X ∑

k≤N
(k,P (z))=1
 1
k
 ∑

z≤m≤N
(m,P (z))=1
 λ(m)
m ≪ u log X ( 1
v2ηv/2 + uv
η + 1
z
 ) u2.

26 KAISA MATOM ¨AKI AND JORI MERIKOSKI

Writing λL(n) for the Liouville function, the ﬁrst sum on the right hand side of (40)
is by (19) and (20)

∑

n≤N
(n,P (z))=1
 λL(n) log y/n
n + O
 




log X ∑

p≥z
 1
p2 ∑

n≤N/p
2

(n,P (z))=1
 1
n
 






= ∑

n≤N
(n,P (z))=1
 λL(n) log y/n
n + O ( u log X
z
 ) .

We deal with the condition (n, P (z)) = 1 using Lemma 3.2(i) with θ = 1/1000.
This gives

∑

n≤N
(n,P (z))=1
 λL(n) log y/n
n = ∑

d|P (z)
 λdλL(d)
d
 ∑

n≤N/d
 λL(n) log y
dn
n

+ O
 

log X ∑

r≥u/1000−β 2−Ar ∑

n≤N 1(n,P (zr))=1 τ (n)
A+1

n
 

 .

By (19) and (20) the error term is

≪A log X ∑

r≥u/1000−β 2−Ar ( log X
log zr
 )2
A+1
 ≪ log X ∑

r≥u/1000−β 2−Aru2
A+1 ( β
β − 1
 )2
A+1r

≪A e−Au/3000 log X

when β is suﬃciently large in terms of A.
For ℜs > 1, let

F (s) := ∑

n∈N
 λL(n)
ns = ∏

p∈P
 (
1 + 1
ps
 )−1 = 1
ζ(s)
 ∏

p∈P
 1
1 − 1
p2s ,

so that ∑

n
 λL(n) log y
dn
ns = F (s) log y
d + F ′(s).

Note that F (s) has a simple zero at s = 1 whereas F ′(s) is holomorphic but non-zero
at s = 1.
By Perron’s formula (see e.g. [17, Corollary 5.3]) we have, for T := exp(2C log3/5−ε X),

∑

d|P (z)
 λdλL(d)
d
 ∑

n≤N/d
 λL(n) log y
dn
n

= ∑

d|P (z)
 λdλL(d)
d 1
2πi
 ∫ 1/ log N +iT

1/ log N −iT
 (F (s + 1) log y
d + F ′(s + 1)
) (N/d)
s

s ds + O ( log5 X
T
 ) .

We move the integration line to ℜs = −1/ log
2/3+ε T , staying in the zero-free region
for ζ(s) (see e.g. [12, Theorem 8.29]). From the residue at s = 0 we get a main
term ∑

d|P (z)
 λdλL(d)
d F ′(1) = ∑

d|P (z)
 λdλL(d)
d
 ∏

p∈P
 1
1 − 1
p2 .

SIEGEL ZEROS AND PRIMES 27

By Lemma 3.2(ii) this equals

(1 + OA(e−Au/2000)) ∏

p<z
 (
1 + 1
p
 ) ∏

p∈P
 1
(1 + 1
p ) (1 − 1
p )

= (
1 + OA
 (
e−Au/2000 + 1
z
 )) ∏

p<z
 (
1 − 1
p
 )−1 .

Let us now consider the remaining integral. For s = −1/ log
2/3+ε T +it with |t| ≤ T
one has (see e.g. [12, Theorem 8.29])

1
ζ(s + 1) ≪ log2/3+ε T and ζ′(s + 1)
ζ(s + 1) ≪ log2/3+ε T.

Hence the remaining integral contributes

≪ ∑

d≤N 1/1000
 1
d
 ∣
∣
∣
∣
∣
∫ −1/ log2/3+ε T +iT

−1/ log2/3+ε T −iT
 (F (s + 1) log y
d − F ′(s + 1)
) (N/d)
s

s ds
∣
∣
∣
∣
∣

≪ log2 X · log3 T · N −1/(2 log2/3+ε T ) ≪C,ε exp(−C log3/5−ε X),

and the claim follows.

7. Proof of Theorems 1.3 and 1.4

Theorems 1.3 and 1.4 are trivial unless h is even. Furthermore they follow from
Lemma 3.1(i) with w1 = w2 = X 1/4 and m1 = m2 = 0 unless η is large. We will
assume these as well as η ≪ qε from (6).
As explained in beginning of Section 2, it suﬃces to study, with g as there,

∑

n g ( n
X
 ) Λ(n)Λ(±n + h),

where in case of +-sign we have 0 ̸= |h| ≤ X 1+ε/2 and in case of −-sign we have
X ∈ [h1−ε/3, h/4], for some small ε > 0. Here we have done a dyadic splitting of n,
discarding n ≤ X 1−ε/2. Hence now q = X 1/V ′ for some V ′ ∈ [(1 − ε/2)V, V ].
Deﬁne z := X 1/u for some u to be chosen shortly (in (41)). Then z = qV ′/u.
By (13) and Lemmas 2.1 and 2.2 we have

∑

n g ( n
X
 ) Λ(n)Λ(±n + h) = ∑

n
(n(±n+h),qP (z))=1
 g ( n
X
 ) λ
′(n)λ
′(±n + h)

+ O ( h
ϕ(h) X ( u8

V 2ηV /(3u) + u6V
η + u10

qV /(2u)
 ) + (z + ω(q)) log2 X) .

To balance the error terms with errors of the type e−Au/3000 that we will encounter
later, we choose

(41) u = min { √V log η
10C , log η} .

With this choice, the error terms are acceptable and we can concentrate on the
main term.

28 KAISA MATOM ¨AKI AND JORI MERIKOSKI

By the deﬁnition of λ
′ (see (9)), here
∑

n
(n(±n+h),qP (z))=1
 g ( n
X
 ) λ
′(n)λ
′(±n + h)

= ∑

m1,m2,n1,n2
±m1n1+h=m2n2
(m1n1m2n2,P (z))=1
 g ( m1n1
X
 ) χ(m1)χ(m2)χ0(n1)χ0(n2) log n1 log n2.
(42)

Let X± := ±X + h ≍ max{X, h} ≪ X 1+ε/2, so that m2n2 ≍ X±. We make a
smooth partition of the variables mj. We let Ψ : R → [0, 1] be a smooth function
for which Ψ(x) = 0 for x ≤ 1 and Ψ(x) = 1 for x ≥ 2. Deﬁne then F : R+ → [0, 1]
by
 F (x) =
 {Ψ(x) if 0 < x ≤ 2
1 − Ψ(x/2) if x > 2.

The function F (x) is supported on [1, 4] and gives a smooth partition of unity
∑

j∈Z F ( x
2j
 ) = 1 for all x > 0.

We write N1 = X/M1 and N2 = X±/M2 ≍ max{X, h}/M2. Then when mj ∈
[Mj, 4Mj], in (42), then nj ∈ [Nj/20, 20Nj]. Let h : R≥0 → [0, 1] be a smooth
function supported on [1/40, 40] such that h(x) = 1 for x ∈ [1/20, 20], and write

fM1,M2(x1, x2, y1, y2) = g(x1y1)F (x1)F (x2)h(y1)h(y2) log (y1N1) log (y2N2)
log2 X .

Then ∑

n
(n(±n+h),qP (z))=1
 g ( n
X
 ) λ
′(n)λ
′(±n + h)

= log2 X ∑

M1=2
i1 ,M2=2
i2
1/4≤M1≤4X
1/4≤M2≤4X±
 ∑

m1,m2,n1,n2
±m1n1+h=m2n2
(m1n1m2n2,P (z))=1
 fM1,M2
 ( m1
M1 , m2
M2 , n1
N1 , n2
N2
 )

· χ(m1)χ(m2)χ0(n1)χ0(n2)

=: Σ±
S,S + Σ±
S,L + Σ±
L,S + Σ±
L,L,

say, where Σ±
S,S corresponds to M1 ≤ X 1/2 and M2 ≤ X 1/2
± , Σ±
S,L corresponds to

M1 ≤ X 1/2 and M2 > X 1/2
± , Σ±
L,S corresponds to M1 > X 1/2 and M2 ≤ X 1/2
± , and

Σ±
L,L corresponds to M1 ≥ X 1/2 and M2 ≥ X 1/2
± .
Let us start with Σ±
S,S. Applying Proposition 2.3 with ψ1 = ψ2 = χ0, χ1 = χ2 =
χ, and δ = X −1/1000, handling the error term with (15), we see that, for any A ≥ 1,

Σ±
S,S = log2 X ∏

p<z
p|h,p∤q
 (
1 − 1
p
 ) ∏

p<z
p∤hq
 (
1 − 2
p
 ) · 1
q
 ∑

γ (q) χ0(γ)χ0(±γ + h)

· ∑

M1=2
i1 ,M2=2
i2
1/4≤M1≤4X
1/4≤M2≤4X±
 ∑

m1,m2
(m1m2,P (z))=1
 χ(m1)χ(m2)
m1m2
 ∫ fM1,M2
 ( m1
M1 , m2
M2 , y
m1N1 , ±y + h
m2N2
 ) dy

+ OA
 ( h
ϕ(h) X (
e−Au/3000 + u6

z
 ) + X 7/9+3/1000q2)

SIEGEL ZEROS AND PRIMES 29

Taking A = 106C2, the error terms are acceptable by our choice of u in (41). Let
us denote the main term by ̃Σ±
S,S. There

∑

M1=2
i1 ,M2=2
i2

1/4≤M1≤X 1/2

1/4≤M2≤X 1/2
±
 ∑

m1,m2
(m1m2,P (z))=1
 χ(m1)χ(m2)
m1m2
 ∫ fM1,M2
 ( m1
M1 , m2
M2 , y
m1N1 , ±y + h
m2N2
 ) dy

= ∫ g ( y
X
 ) ∑

m1,m2
(m1m2,P (z))=1
 χ(m1)χ(m2) log y
m1 log ±y+h
m2
m1m2 · log2 X
 ∑

M1=2
i1 ,M2=2
i2

1/4≤M1≤X 1/2

1/4≤M2≤X 1/2
±
 F ( m1
M1
 ) F ( m2
M2
 ) dy.

Note that there is no dependency between m1 and m2,

∑

M1=2
i1
1/4≤M1≤X 1/2
 F ( m1
M1
 ) =
 {1 if m1 ≤ X 1/2/4;
0 if m1 ≥ 4X 1/2,

and ∑

M2=2
i2

1/4≤M2≤X 1/2
±
 F ( m2
M2
 ) =
 {1 if m2 ≤ X 1/2
± /4;
0 if m2 ≥ 4X 1/2
± .

Hence by partial summation and Lemmas 2.4 (with v = V ′/u) and 2.5, we obtain

̃Σ±
S,S = ∏

p<z
p|h,p∤q
 (
1 − 1
p
 ) ∏

p<z
p∤hq
 (1 − 2
p
 ) ∏

p|(q,h)
 (
1 − 1
p
 ) ∏

p|q
p∤h
 (
1 − 2
p
 ) ∏

p<z
 (1 − 1
p
 )−2 ∫ g ( y
X
 ) dy

· (
1 + OA
 ( u6

V 2ηV /(3u) + V u4

η + u4

z + e−Au/3000) + OC,ε (exp(−C log3/5−ε X)
))2 .

Here ∏

p<z
p|h,p∤q
 (
1 − 1
p
 ) ∏

p<z
p∤hq
 (
1 − 2
p
 ) ∏

p|(q,h)
 (1 − 1
p
 ) ∏

p|q
p∤h
 (
1 − 2
p
 ) ∏

p<z
 (
1 − 1
p
 )−2

= 2 ∏

2<p<z
 1 − 2
p
(1 − 1
p )2 · (
1 + O ( u
z
 )) ∏

p|(h,q)
p>2
 1 − 1
p
1 − 2
p
 ∏

p|h
p∤q
p>2
 1 − 1
p
1 − 2
p

= 2 (
1 + O ( u
z
 )) ∏

2<p<z
 (1 − 1
(p − 1)2
 ) ∏

p|h
p>2
 (
1 + 1
p − 2
 ) .

(43)

Hence

̃Σ±
S,S = Sh
 ∫ g ( y
X
 ) dy

+ OA,C,ε
 ( h
ϕ(h) X ( u6

V 2ηV /(3u) + V u4

η + u4

qV /(2u) + e−Au/3000 + exp(−C log3/5−ε X)
)) .

The error terms are acceptable when A = 106C2 by our choice of u in (41).
For Σ±
L,L we use Proposition 2.3 with χ1 = χ2 = χ0, ψ1 = ψ2 = χ, δ = X −1/1000

and the roles of Mj and Nj interchanged. Handling the error term with (15), we

30 KAISA MATOM ¨AKI AND JORI MERIKOSKI

see that, for any A ≥ 1,

Σ±
L,L = log2 X ∏

p<z
p|h,p∤q
 (
1 − 1
p
 ) ∏

p<z
p∤hq
 (1 − 2
p
 ) · 1
q
 ∑

γ (q) χ(γ)χ(±γ + h)

· ∑

M1=2
i1 ,M2=2
i2

X 1/2<M1≤4X
X 1/2
± <M2≤4X±
 ∑

n1,n2
(n1n2,P (z))=1
 χ(n1)χ(n2)
n1n2
 ∫ fM1,M2
 ( y
M1n1 , ±y + h
M2n2 , n1
N1 , n2
N2
 ) dy

+ OA
 ( h
ϕ(h) X (
e−Au/3000 + u6

z
 ) + X 7/9+3/1000q2)

Taking A = 106C2, the error term is again suﬃciently small by our choice of u
in (41). We denote the main main term by ̃Σ±
L,L. Recall that 2 | h so that by
Lemma 2.5
∑

m (q) χ(m(±m + h)) = χ(±1) ∑

m (q) χ0(m)χ0(±m + h) · 1ϕ(2r)|h(−1) h
ϕ(2r ) ∏

p|q′

p∤h
 −1
p − 2 .

Furthermore
∑

M1=2
i1 ,M2=2
i2

X 1/2<M1≤4X
X 1/2
± <M2≤4X±
 ∑

n1,n2
(n1n2,P (z))=1
 χ(n1)χ(n2)
n1n2
 ∫ fM1,M2
 ( y
M1n1 , ±y + h
M2n2 , n1
N1 , n2
N2
 ) dy

= ∫ g ( y
X
 ) ∑

n1,n2
(n1n2,P (z))=1
 χ(n1)χ(n2) log(n1) log(n2)
n1n2

· ∑

M1=2
i1 ,M2=2
i2

X 1/2<M1≤4X
X 1/2
± <M2≤4X±
 F ( y
M1n1
 ) F ( ±y + h
M2n2
 ) dy.

Similarly to the case of Σ±
S,S, we can use partial summation, Lemma 2.4 (with
y = 1), and (43) to obtain

̃Σ±
L,L = Shχ(±1) ∫ g ( y
X
 ) dy · 1ϕ(2r)|h(−1)
 h
ϕ(2r ) ∏

p|q′

p∤h
 −1
p − 2

+ O ( h
ϕ(h) X ( u6

V 2ηV /(3u) + V u4

η + u4

qV /(2u) + ue−Au/3000 + exp(−C log3/5−ε X)
))

The error term is again acceptable by (41).
We handle Σ±
S,L and Σ±
L,S similarly. The error terms are the same as before
whereas the main term from Proposition 2.3 is by Lemma 2.5, (19), (20), and (6)

≪ X log2 X ∏

p<z
p|h,p∤q
 (
1 − 1
p
 ) ∏

p<z
p∤hq
 (
1 − 2
p
 ) · 1(h,q)=1
q
 ∑

m1≪X 1/2,m2≪X 1/2
±
(m1m2,P (z))=1
 1
m1m2

≪ε h
ϕ(h) X u4

q1−ε ≪ h
ϕ(h) X 1
η .

Collecting everything together the claims follow.

SIEGEL ZEROS AND PRIMES 31

8. Proof of Corollary 1.5

Squaring out and applying the prime number theorem, we see that

∫ 2X

X
 

 ∑

y<n≤y+H Λ(n) − H




2
 dy

= ∫ 2X

X
 

 ∑

y<n≤y+H Λ(n)




2
 − 2H ∑

y<n≤y+H Λ(n) + H 2dy

= ∑

|h|≤H
 ∑

n1,n2
n1=n2+h
 Λ(n1)Λ(n2) ∫ 2X

X 1n1,n1−h∈(y,y+H]dy − H 2X

+ OC,ε
 (
H 3 log X + H 2X

exp(C log3/5−ε X)
 )
 .

The ﬁrst term on the right hand side equals
∑

|h|≤H(H − |h|) ∑

X<n1≤2X Λ(n1)Λ(n1 + h) + O (
H 3 log2 X)

= H ∑

X<n≤2X Λ(n)
2 + ∑

0<|h|≤H(H − |h|) ∑

X<n≤2X Λ(n)Λ(n + h) + O (
H 3 log2 X) .

The ﬁrst term on the right hand side is by the prime number theorem ≪ HX log X.
Applying Theorem 1.3 to the second term, noting that ∑0<|h|≤H h
ϕ(h) ≪ H, we see
that it suﬃces to show that

∑

0<|h|≤H
h even
 (H−|h|)Sh
 



1 + 1ϕ(2r)|h(−1)
 h
ϕ(2r ) ∏

p|q′

p∤h
 −1
p − 2
 



 = H 2+O (
H log X + η−1H 2) .

Recall that q′ is necessarily square-free (see e.g. [12, Section 3.3]). Using the bound
Sh ≪ h/ϕ(h) and Lemma 3.7 we see that the term depending on q contributes

≪ H ∑

0<|h|≤H
 h
ϕ(h)
 ∏

p|q′

p∤h
 1
p − 2 ≪ H ∏

p|q′
 1
p − 2
 ∑

0<|h|≤H
 h
ϕ(h) (h, q′) ≪ H 2

q1/2 ,

which is admissible by (6). Hence, it remains to show that

(44) 2 ∑

0<|h|≤H
h even
 (H − |h|) ∏

p>2
 (
1 − 1
(p − 1)2
 ) ∏

p|h
p>2
 (1 + 1
p − 2
 ) = H 2 + O (H log X) .

Now ∑

0<|h|≤H
h even
 (H − |h|) ∏

p|h
p>2
 (
1 + 1
p − 2
 ) =
 H∑

j=2
 ∑

0<|h|<j
h even
 ∏

p|h
p>2
 (
1 + 1
p − 2
 )

=
 H∑

j=2
 ∑

0<|h|<j/2
 ∏

p|h
p>2
 (1 + 1
p − 2
 ) .

Deﬁne a multiplicative function f such that

f (pν) =
 {0 if p = 2 or ν ≥ 2;
1
p−2 otherwise.

32 KAISA MATOM ¨AKI AND JORI MERIKOSKI

Then ∑

0<|h|<j/2
 ∏

p|h
p>2
 (
1 + 1
p − 2
 ) = ∑

0<|h|<j/2
 ∑

r|h f (r) = ∑

r<j/2 f (r) ∑

0<|h|<j/2r 1

= j ∑

r<j/2
 f (r)
r + O
 

 ∑

r<j/2 f (r)



 = j ∏

p>2
 (1 + 1
p(p − 2)
 ) + O(log j)

= j ∏

p>2
 (1 − 1
(p − 1)2
 )−1 + O(log j)

Thus the left hand side of (44) equals

2
 H∑

j=2 j + O (H log H) = H 2 + O (H log X)

as claimed.
 Acknowledgements

The ﬁrst author was supported by Academy of Finland grant no. 285894. The
second author was supported by Academy of Finland grant no. 333707 and by
the European Research Council (ERC) under the European Union’s Horizon 2020
research and innovation programme (grant agreement no. 851318).
We are grateful to Terence Tao and Joni Ter¨av¨ainen for helpful discussions and
to Andrew Granville for providing us material concerning the relationship between
Siegel zeros and L(1, χ).
 References

[1] H. Iwaniec B. Conrey. Spacing of zeros of hecke l-functions and the class number problem.
Acta Arithmetica, 103(3):259–312, 2002.
[2] J. Friedlander and H. Iwaniec. Opera de cribro, volume 57 of American Mathematical Society
Colloquium Publications. American Mathematical Society, Providence, RI, 2010.
[3] J. B. Friedlander, D. A. Goldston, H. Iwaniec, and A. I. Suriajaya. Exceptional zeros and the
Goldbach problem. J. Number Theory, 233:78–86, 2022.
[4] J. B. Friedlander and H. Iwaniec. The illusory sieve. Int. J. Number Theory, 1(4):459–494,
2005.
[5] J. B. Friedlander and H. Iwaniec. A note on Dirichlet L-functions. Expo. Math., 36(3-4):343–
350, 2018.
[6] D. A. Goldston and A. I. Suriajaya. Note on the Goldbach conjecture and Landau-Siegel
zeros. Preprint, arXiv:2104.09407v1, 2021.
[7] G. Harman. Prime-detecting sieves, volume 33 of London Mathematical Society Monographs
Series. Princeton University Press, Princeton, NJ, 2007.
[8] D. R. Heath-Brown. Gaps between primes, and the pair correlation of zeros of the zeta
function. Acta Arith., 41(1):85–99, 1982.
[9] D. R. Heath-Brown. Prime twins and Siegel zeros. Proc. London Math. Soc. (3), 47(2):193–
224, 1983.
[10] K. Henriot. Nair-Tenenbaum bounds uniform with respect to the discriminant. Math. Proc.
Cambridge Philos. Soc., 152(3):405–424, 2012.
[11] K. Henriot. Nair-Tenenbaum uniform with respect to the discriminant—Erratum
[mr2911138]. Math. Proc. Cambridge Philos. Soc., 157(2):375–377, 2014.
[12] H. Iwaniec and E. Kowalski. Analytic number theory, volume 53 of American Mathematical
Society Colloquium Publications. American Mathematical Society, Providence, RI, 2004.
[13] C. Jia. Almost all short intervals containing prime numbers. Acta Arith., 76(1):21–84, 1996.
[14] H. D. Kloosterman. On the representation of numbers in the form ax2 + by2 + cz2 + dt2. Acta
Math., 49(3-4):407–464, 1927.
[15] J. Merikoski. Exceptional characters and prime numbers in sparse sets. Pre-print, 2021.

SIEGEL ZEROS AND PRIMES 33

[16] H. L. Montgomery. The pair correlation of zeros of the zeta function. In Analytic number
theory (Proc. Sympos. Pure Math., Vol. XXIV, St. Louis Univ., St. Louis, Mo., 1972),
pages 181–193, 1973.
[17] H. L. Montgomery and R. C. Vaughan. Multiplicative number theory. I. Classical theory,
volume 97 of Cambridge Studies in Advanced Mathematics. Cambridge University Press,
Cambridge, 2007.
[18] A. Selberg. On the normal density of primes in small intervals, and the diﬀerence between
consecutive primes. Arch. Math. Naturvid., 47(6):87–105, 1943.
[19] T. Tao and J. Ter¨av¨ainen. The Hardy-Littlewood-Chowla conjecture in the precence of a
Siegel zero. Preprint, arXiv:2111.08912v1, 2021.

Department of Mathematics and Statistics, University of Turku, 20014 Turku, Fin-
land
Email address: ksmato@utu.fi

Mathematical Institute, University of Oxford, Andrew Wiles Building, Radcliffe
Observatory Quarter (550), Woodstock Road, Oxford, OX2 6GG
Email address: jori.merikoski@maths.ox.ac.uk
