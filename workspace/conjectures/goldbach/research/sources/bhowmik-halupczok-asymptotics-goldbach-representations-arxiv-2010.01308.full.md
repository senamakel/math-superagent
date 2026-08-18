<!-- source: https://arxiv.org/pdf/2010.01308 | converted from PDF -->

arXiv:2010.01308v2  [math.NT]  3 Nov 2020
CONDITIONAL BOUNDS ON SIEGEL ZEROS

GAUTAMI BHOWMIK AND KARIN HALUPCZOK

Dedicated to Melvyn Nathanson.

Abstract. We present an overview of bounds on zeros of L-
functions and obtain some improvements under weak conjectures
related to the Goldbach problem.

1. Introduction

The existence of non-trivial real zeros of a Dirichlet L-function would
contradict the Generalised Riemann Hypothesis. One possible counter-
example, called the Landau–Siegel zero, is real and simple and the re-
gion in which it could eventually exist is important to determine. In
1936 Siegel gave a quantitative estimate on the distance of an excep-
tional zero from the line ℜs = 1. The splitting into cases depending on
whether such an exceptional zero exists or not happens to be an im-
portant technique often used in analytic number theory, for example in
the theorem of Linnik. In the ﬁrst section we discuss properties of the
Siegel zero and results assuming classical and more recent hypotheses.
This part of the paper is expository.
In the second section we present a conditional bound. In 2016 Fei
improved Siegel’s bound for certain moduli under a weakened Hardy–
Littlewood conjecture on the Goldbach problem of representing an even
number as the sum of two primes. In Theorem 11 and Corollary 1 we
further weaken this conjecture and enlarge the set of moduli to include
more Dirichlet characters.
 2. Background

Consider a completely multiplicative, periodic arithmetic function
χ : Z → C where for q ≥ 1 there exists a group homomorphism
˜χ : (Z/qZ)× → C× such that χ(n) = ˜χ(n(mod q)) for n coprime to q
and χ(n) = 0 if not. We call χ a Dirichlet character (mod q). In fact,

2010 Mathematics Subject Classiﬁcation. 11P32, 11M26, 11M41.
Key words and phrases. Siegel zero, Goldbach problem, congruences, Dirichlet
L-function, Generalised Riemann hypothesis.
We thank Andrew Granville and Lasse Grimmelt for helpful comments and the
referee for an improved presentation. 1

2 GAUTAMI BHOWMIK AND KARIN HALUPCZOK

if (n, q) = 1, χ(n) is a φ(q)th complex root of unity. We denote the
principal character mod q, whose value χ(n) is always 1 for n coprime
to q, by χ0 (mod q). The order of χ is the least positive integer n
such that χ
n = χ0, both characters having the same modulus. A non-
principal character is called quadratic if χ
2 = χ0. In the case where
χ always takes a real value, the possibilities being only 0 or ±1, it
is called a real character, otherwise it is called complex. A character
modulo q is termed primitive and q its conductor if it cannot be factored
as χ = χ
′χ0, where χ0 is a principal character and χ
′ a character of
modulus strictly less than q. For a given χ (mod q), there is a unique
primitive character ˜χ(mod ˜q) with least possible ˜q, where ˜q | q, that
induces χ, such that χ and ˜χ have the same value at all n coprime to
q. The L series were introduced in 1837 by Dirichlet who used them
to prove an analytic formula for the class number and the inﬁnitude
of primes in any arithmetic progression. For s = σ + it, σ > 1, and a
Dirichlet character χ, we consider the Dirichlet L-function

L(s, χ) =
 ∞∑

n=1
 χ(n)
ns = ∏

p prime
 (
1 − χ(p)
ps
 )−1.

Note that since L(s, χ) = L(s, ˜χ) ∏

p|q(1 − ˜χ(p)p−s) there is no loss in
considering only primitive characters for obtaining analytic properties.
Let ρχ = βχ + iγχ be the non-trivial zeros of the L-function. These
are known to be contained in the strip 0 < ℜ(s) < 1 though accord-
ing to the Generalised Riemann Hypothesis (GRH), the only possible
value of βχ is 1/2. While the GRH remains out of reach, much uncon-
ditional work has been directed towards ﬁnding zero-free regions for
L-functions.
Around hundred years ago it was proved that real zeros close to
ℜs = 1 are indeed rare. More precisely,

Theorem 1 (Landau–Page). There is an absolute constant c > 0 such
that for any Q, T ≥ 2, the product ∏

q≤Q ∏⋆
χ mod q L(s, χ) has at most
one zero of an L-function in the region

|t| ≤ T, 1 − σ ≤ c
log(QT ) ;

where ⋆ runs over all primitive real characters of modulus q. If such
a zero exists, then it is real and associated to a unique, quadratic χ
mod q.

This eventual ‘bad’ zero contradicting the GRH is called the excep-
tional or Siegel or Landau–Siegel zero and the corresponding character

CONDITIONAL BOUNDS ON SIEGEL ZEROS 3

is called the exceptional character. We denote the Landau–Siegel zero
by βχ or simply β.
The work of Landau and Siegel provide bounds on the proximity of
such a zero on the real axis from s = 1. Quantitatively,

Theorem 2 (Siegel). For an exceptional zero β associated to a prim-
itive character χ of conductor q and any ǫ > 0 there is a constant
c(ǫ) > 0 such that

(2.1) 1 − β ≥ c(ǫ)
qǫ .

Unfortunately, the constant c(ǫ) cannot be computed eﬀectively for
any ǫ < 1/2, which is a serious diﬃculty for many applications. In
1951, Tatuzawa [17] did improve on Siegel’s theorem to give an eﬀective
version for almost all cases by proving that for any positive ǫ there does
exist an eﬀectively computable positive constant c(ǫ) such that for all
quadratic characters χ, with at most one exception, L(s, χ) has no
zeros in the interval [1 − c(ǫ)/qǫ, 1].

2.1. Repulsion Property. The possible exceptional zero would force
all other zeros, real or otherwise, of all L-functions of the same modulus
away from the real axis. We state a quantitative version of the Deuring–
Heilbronn result of 1933-34.

Theorem 3. There exist eﬀective constants c, c′ > 0 such that for any
T ≥ 2 and any q ≥ 1, if for some quadratic χ(mod q), L(s, χ) has an
exceptional zero β ∈ [1 − c/ log(qT ), 1], then ∏

χ L(s, χ), the product
over all characters of modulus q including the exceptional one, has no
other zero in the domain

σ ≥ 1 − c′| log((1 − β) log qT )|
log qT , t ≤ T.

Here is a reformulated version of the repulsion phenomenon also due
to Linnik in 1944 which he used to ﬁnd the size of the least prime in
an arithmetic progression.

Theorem 4. If there exists an exceptional zero β with 1 − β = ε
log q
for ε suﬃciently small, then all other zeroes σ + it of L-functions of
modulus q are such that

1 − σ ≥ c log 1
ε
log(q(2 + |t|))

for an absolute positive constant c.

4 GAUTAMI BHOWMIK AND KARIN HALUPCZOK

Compared to the classical estimate σ ≥ 1 − c
log(q(2+|t|)) with some ab-
solute positive constant c, for a region where L(s, χ), for any χ mod q,
contains no zeros except at most one eventual exception, we now have
a zero-free region wider by a factor of log 1
ε .
Theorem 4 above was strengthened by Bombieri [4] to

Theorem 5. Let T ≥ 2 and β be an exceptional zero with respect to the
otherwise zero-free region σ ≥ c
log T , |t| ≤ T , then there exist constants
c1, c2 such that if (1 − β) log T ≤ c2/e, then for any zero σ + it ̸= β of
L(s, χ), we have
 1 − σ ≥ c1 log c2
(1−β) log T
log T ,

where |t| ≤ T for every primitive χ of modulus q ≤ T .

This can be written in terms of a density estimate. Let N(α, q, T )
denote the number of zeroes, counted with multiplicity, of any L func-
tion of modulus q with α ≤ σ ≤ 1 and 0 ≤ t ≤ T and let N ′ denote
the case when β is omitted. Then there is an improvement

N ′(α, q, T ) ≪ (1 − β)(log q)(
1 + log T
log q
 )
(qT )O(1−α)

with eﬀective implied constants over Linnik’s density estimate

N(α, q, T ) ≪ (1 − β)(log qT )(qT )O(1−α).
In [7] Friedlander and Iwaniec state the ‘ultimate Deuring–Heilbronn
property’ as

Theorem 6. Let χ(mod q) be a real primitive character of conductor
q with the largest real zero β and let η = 1
(1−β) log q ≥ 3. Then L(s, χ)

has no zeros other than β in the region σ > 1 − c log η
log q(|t|+1) where c is an
absolute positive constant.

2.2. Bounds for L(1, χ). We know at least since Hecke and Landau
that zeros of L(s, χ) and its value at s = 1 are closely related. If L(1, χ)
is suﬃciently small relative to the conductor, then there is a Siegel zero
and conversely. More precisely, if L(1, χ) ≤ c
log q for a small constant
c > 0, then 1 − β ≤ 1
log q . Using the Deuring–Heilbronn repulsion
property, Friedlander and Iwaniec recently proved [7] that

(2.2) {1 − β ≪ (log q)−3 log log q} =⇒ {L(1, χ) ≪ (log q)−1}.

Goldfeld [8] provided an asymptotic result for the location of the Siegel
zero. In fact, when 1 − β < c
log q , he obtained a precise asymptotic

CONDITIONAL BOUNDS ON SIEGEL ZEROS 5

formula

(2.3) 1 − β ∼ 6
π2 L(1, χ)( ∑ a
−1)−1

where the summation is over all reduced quadratic forms (a, b, c) of
discriminant −q.
Dirichlet expressed the value of L(1, χ) where χ(n) = ( −q
n ) is the
real primitive character of conductor q in terms of the number h(q) of
equivalence classes of binary quadratic forms of discriminant q, which
can equivalently be formulated in terms of the number of ideal classes
of an imaginary quadratic number ﬁeld K = Q(√−q). From the class
number formula L(1, χ) = πh(q)
√−q (here q < −4) one obtains the non-
vanishing of L(1, χ) which is not that obvious when χ is real, and leads
to the prime number theorem in arithmetic progression. Another ob-
vious consequence of the above formula is the elementary lower bound

L(1, χ) ≫ 1
q1/2 .

Bounding L(1, χ) is equivalent to estimating the size of the class num-
ber of the imaginary quadratic ﬁeld K = Q(√−q), another important
question in number theory. The corresponding formula is L(1, χ) =
2πhK
wK√dK/Q for the class number hK and discriminant dK/Q of K, wK the

order of the group of units with regulator being 1 and the LHS being
the residue of the Dedekind zeta function at s = 1.
Good eﬀective lower bounds are more diﬃcult to obtain. Goldfeld [9]
in 1976 using known cases of the Birch and Swinnerton-Dyer conjecture
for elliptic curves showed that

L(1, χ) ≫ log q
√q(log log q)

for q ≥ 3, the implied constant being eﬀective. This together with
Gross–Zagier’s work of 1983 is a major step in the Gauß class number
problem.

Theorem 7 (Goldfeld–Gross–Zagier). For every ǫ > 0 there exists an
eﬀectively computable positive constant c such that h(−q) > (c log q)1−ǫ.

This corresponds to a zero-free region of L(s, χ) of size [1−c0 logc1 (q)
√q , 1]
for some eﬀective positive constants c0, c1 and for all real primitive
characters.

6 GAUTAMI BHOWMIK AND KARIN HALUPCZOK

Oesterl´e’s calculation of the involved constant in 1985 makes it pos-
sible to state this bound for q > 0 as

L(1, χ) > π
55√q log q ∏

p|q
 (1 − 2√p
p + 1
 ).

Rather recently Bennett et al. [2] proved that if χ is a primitive
quadratic character with conductor q > 6677, then L(1, χ) > 12√q .
We are still far from the plausible lower bound L(1, χ) ≫ (log q)−1

which holds in many cases, for example for complex characters with an
eﬀective constant.
Aisleitner et al. [1] in 2019 showed the existence, for q suﬃciently
large, of an extremal non-principal character which satisﬁes, for con-
stants C and γ, |L(1, χ)| ≥ e
γ(log log q + log log log q − C) using the
method of resonance for detecting large values of the Riemann zeta
function. Up to the constant, this corresponds to the predicted order
of the extremal values.
A simple unconditional upper bound is L(1, χ) ≪ log q. The implied
constants have been worked on by a variety of methods. For example,
for complex characters Granville and Soundararajan [10] determine the
constant ck for primitive characters of order k for which the bounds
|L(1, χ)| ≤ (ck + o(1)) log q hold true. For real primitive characters, the
constant c2 = 1
4(2 − 2√e + o(1)) log q was obtained by Stephens for prime
characters [16] and Pintz [14] extended this to non-prime characters.

2.2.1. Conditional Bounds. The optimal bounds of L(1, χ) under the
condition of GRH are

(log log q)−1 ≪ L(1, χ) ≪ log log q

where the implied constants are eﬀective. Precisely speaking,

Theorem 8 (Littlewood 1928). If the Generalised Riemann Hypothesis
is true then
(1
2 + o(1)) π2

6eγ log log q ≤ L(1, χ) ≤ (2 + o(1))e
γ log log q

where γ is Euler’s constant.

Only the implied constants in the above can be improved because
there actually exist inﬁnitely many q for which the special value of the
corresponding character at s = 1 correspond to the above magnitude of
orders. The classical unconditional Ω results, that (1+o(1)) π2
6eγ log log q ≥
L(1, χ) and L(1, χ) ≥ (1 + o(1))e
γ log log q hold for inﬁnitely many q

CONDITIONAL BOUNDS ON SIEGEL ZEROS 7

[5] show that there is a factor of 2 that remains undetermined for the
extreme values.
We cite one example of a recent reﬁned upper and lower bound es-
tablished by Lamzouri et al. [12] assuming the GRH for characters of
large conductor and studying certain character sums. For q ≥ 1010,
the bounds obtained therein can be written in a simpliﬁed manner as

π2

12eγ log log q < |L(1, χ)| < 2e
γ log log q.

The lower bound can be improved a lot by admitting the existence of
Landau–Siegel zeros, and thus weakening the GRH. One such assump-
tion, sometimes called the Modiﬁed Generalised Riemann Hypothesis
(MGRH), is that all the zeros of L(s, χ) lie either on the critical line or
on the real axis. Sarnak and Zaharescu [15] showed that if all Dirichlet
L(s, χ) with χ real satisfy the MGRH then

L(1, χ) ≥ cǫ

(log |q|)ǫ

for any positive ǫ. The above constant is ineﬀective but the bounds can
be made eﬀective under certain additional conditions. These bounds
use the explicit formula with an appropriately constructed kernel func-
tion.
Assuming that the GRH holds except for one possible exception,
Friedlander and Iwaniec obtained an improved version of (2.2). They
proved that:

Theorem 9 ([7]). Let the GRH be true except for only one β > 3/4.
Now if 1 − β ≪ (log log q)−1, then

1 − β ≪ L(1, χ) ≪ (1 − β)(log log q)2.

3. Better Siegel zero bounds from Weak Goldbach
conjectures

Connections between Siegel zeros and the Goldbach problem were
studied, for example in [3] and [6]. Among the classical conjectures
of the Goldbach problem is one due to Hardy and Littlewood in 1923
that predicts an equivalence between the number of representations
of an even number as a sum of two primes and a singular series,
g(n) = ∑

n=p1+p2 1 ∼ S(n), where

S(n) := n
ϕ(n)
 ∏

p∤n
 (
1 − 1
(p − 1)2
 ) · n
log2 n = 2C2( ∏

p|n
p>2
 p − 1
p − 2
 ) · n
log2 n

8 GAUTAMI BHOWMIK AND KARIN HALUPCZOK

with the twin prime constant

C2 = ∏

p>2
 (1 − 1
(p − 1)2
 )

which is approximately 0.66.
Fei [6] obtained an upper bound for β under a weakened form of the
Hardy–Littlewood conjecture (WHL), namely

Conjecture 1 (WHL). There exists a positive contant δ such that
g(n) ≥ δn
log2 n for every even integer n > 2.

Considering the size of S(n) we could even expect a δ > 1.32, but
in this weakened form of the Hardy–Littlewood conjecture, we assume
only the existence of some small positive δ.
We now state Fei’s theorem.

Theorem 10 ([6]). If the WHL-conjecture is true and if there is an ex-
ceptional zero β for a character χ with a prime modulus q ≡ 3 mod 4,
then there exists a positive constant c such that 1 − β ≥ c
log2 q .

Here, the corresponding region for the exceptional zero β is meant
to be that of Theorem 1 with T = q. We will keep to this convention
for the rest of this section.
One would like to know if it is possible to include other moduli in
the above result or to relax the assumed WHL-conjecture.
Here we generalise Fei’s result in these two aspects and obtain a con-
ditional improvement of Siegel’s bound (Theorem 2) for certain excep-
tional characters which includes Fei’s modulus condition (Corollary 1).
Our result still assumes the weak Hardy–Littlewood conjecture but al-
lows certain exceptions (WHLE) making it weaker than the WHL. Our
proof is similar to that of Fei’s but exploits, apart from the use of the
WHLE, the generalisation to suitable composite moduli q.

Conjecture 2 (WHLE). Suppose that x is suﬃciently large, and q ≤
x/4. Then we have, with at most x/8q exceptions,

g(n) ≫ n
log2 n

for the multiples n of q in the interval x/2 < n ≤ x.

Theorem 11. Assume the WHLE Conjecture to be true. Let q be a
suﬃciently large integer and χ be a primitive character mod q with
χ(−1) = −1 such that there is an exceptional zero β of L(s, χ). Then
there exists an eﬀective constant c > 0 such that 1 − β ≥ cϕ(q)
q log2(q) .

CONDITIONAL BOUNDS ON SIEGEL ZEROS 9

Proof of Theorem 11. Step 1. We prove the following lower bound for
the sum

(3.1) S =
 q∑

k=1
 ( ∑

2<p≤x e
( kp
q
 ))2 ≥ δx
2

8 log2 x

for any suﬃciently large real x > 2 and some small δ > 0.
For this, we ﬁrst note note that

S =
 q∑

k=1
 ∑

2<p1,p2≤x e
(k(p1 + p2)
q
 )

= ∑

n≤2x
 q∑

k=1 e
( kn
q
 ) ∑

2<p1,p2≤x
p1+p2=n
 1 = ∑

n≤2x
n≡0(q)
 q ∑

2<p1,p2≤x
p1+p2=n
 1.

Let x be large enough with

(3.2) q ≤ x/4.

Hence under the assumption of Conjecture 2, for all even n in the
interval x/2 < n ≤ x that are divisible by q, we have
∑

2<p1,p2≤x
p1+p2=n
 1 ≥ δ x
log2 x

for some constant δ > 0, with the possible exception of at most x/8q
such n. Let E be the set of these exceptions.
Keeping this in mind, we obtain the lower bound

(3.3) S ≥ q ∑

x/2<n≤x
2|n
n≡0(q)
 ∑

p1+p2=n 1 ≥ q ∑

x/2<n≤x
2|n
n≡0(q)
n /∈E
 δ x
log2 x

≥ qδx
log2 x
 ( x
4q − x
8q
 ) = δx
2

8 log2 x

as was to be shown.

Step 2. We now prove a more explicit expression for the sum S in
the ﬁrst step.
In (3.1), the sum over p is subdivided into parts depending on whether
or not q is divisible by p, i.e.

10 GAUTAMI BHOWMIK AND KARIN HALUPCZOK

S1 = ∑

2<p≤x e
( kp
q
 ) = ∑

2<p≤x
p∤q
 e
(kp
q
 )+ ∑

2<p≤x
p|q
 e
( kp
q
 ) = ∑

2<p≤x
(p,q)=1
 e
( kp
q
 )
+O(ω(q))

= ∑

1≤a≤q
(a,q)=1
 e
( ka
q
 ) ∑

2<p≤x
p≡a(q)
 1 + O(ω(q)) = cq(k) ∑

2<p≤x
p≡a(q)
 1 + O(ω(q)),

where cq(k) denotes the above Ramanujan sum
∑

1≤a≤q
(a,q)=1
 e( ka
q )

while ω(q) = #{p | q}. Using the prime number theorem in arithmetic
progressions [13], the last sum over p is written out as

(3.4) ∑

2<p≤x
p≡a(q)
 1 = li(x)
ϕ(q) − χ(a)
ϕ(q)
 ∫ x

2
 uβ−1

log udu + O(x exp(−˜c√log x))

for some constant ˜c > 0, which holds uniformly in

(3.5) q ≤ exp(C√log x)

for any C > 0 (this range is consistent with (3.2), though we could
have chosen a larger x). Hence, this gives

(3.6) S1 = M + cq(k) li(x)
ϕ(q) + O(qx exp(−˜c√log x))

with term M being

M = −1
ϕ(q)
 q∑

a=1 e
( ak
q
 )χ(a) ∫ x

2
 uβ−1

log u du = −τk(χ)
ϕ(q)
 ∫ x

2
 uβ−1

log udu,

since χ(a) = 0 if (a, q) > 1, with the Gauß sum

τk(χ) =
 q∑

a=1 e
( ak
q
 )
χ(a).

Inserting the expansion ∫ x
2 uβ−1
log u du = xβ
β log x + O( xβ

log2 x ) yields

M = −τk(χ)
ϕ(q) · x
β

β log x + O( q1/2

ϕ(q) · x
β

log2 x
)

from the estimate τk(χ) ≪ q1/2.
We substitute this expression in (3.6) and the resulting approxima-
tion for S1 into S to get

CONDITIONAL BOUNDS ON SIEGEL ZEROS 11

(3.7) S =
 q∑

k=1 S2
1 =
 q∑

k=1
 (
cq(k) li(x)
ϕ(q) − τk(χ)
ϕ(q) · x
β

β log x

+ O(qx exp(−˜c√log x) + q1/2

ϕ(q) · x
β

log2 x
))2

=
 q∑

k=1
 (
c2
q(k) li
2(x)
ϕ2(q) + τ 2
k (χ)
ϕ2(q) · x
2β

β2 log2 x
 )

+O( q1/2x
β

ϕ(q) log xq2x exp(−˜c√log x)+ q2x
2β

βϕ2(q) log3 x+q3x
2 exp(−2˜c√log x))
,

where all the mixed terms containing the Ramanujan sum have now
disappeared since

q∑

k=1 cq(k)τk(χ) =
 q∑

k=1
 ∑

1≤a≤q
(a,q)=1
 ∑

1≤b≤q
(b,q)=1
 e
( ak
q
 )
e
( bk
q
 )χ(b)

= ∑

1≤a≤q
(a,q)=1
 ∑

1≤b≤q
(b,q)=1
b≡−a(q)
 χ(b)q = q ∑

1≤a≤q
(a,q)=1
 χ(−a) = 0

and ∑q
k=1 cq(k) = 0. The O-term in (3.7) simpliﬁes to

(3.8) Eexpl = O( x
2

log3 x q2

ϕ(q)2 + q3x
2 exp(−˜c√log x))
.

For the main term in (3.7), we use properties of Gauß sums ([13,
p.287]),
 τk(χ) = { ¯χ(k)τ1(χ), (k, q) = 1
0, else,

so that the sum over τ 2
k (χ) in (3.7) becomes

1
ϕ2(q)
 q−1∑

k=1
(k,q)=1
 τ 2
1 (χ) ¯χ
2(k) = q
ϕ(q) χ(−1)

since τ 2
1 (χ) = χ(−1)q and χ
2 = χ0. Similarly, we have

q∑

k=1 c2
q(k) = qϕ(q),

see [13, p.113]. Hence

(3.9) S = q
ϕ(q) li2(x) + q
ϕ(q) χ(−1) x
2β

β2 log2 x + Eexpl.

12 GAUTAMI BHOWMIK AND KARIN HALUPCZOK

Comment. We note that an alternative approach via the identity

q
ϕ(q)
 ∑

χ(q) χ(−1)|ψ(x, χ)|2 =
 q∑

k=1
 ( ∑

p≤x Λ(p)e
(kp
q
 ))2 + o(log3 x)

and the use of an explicit formula for ψ(x, χ) might avoid the use of
Gauß sums in Step 2 of the proof.

Step 3. Now we compare the lower bound from Step 1 with the ex-
plicit evaluation from Step 2. With the assumption χ(−1) = −1 we
get the inequality

x
2β

β2 log2 x ≤ (
1 − δ
8 · ϕ(q)
q
 ) x
2

log2 x + Eexpl,

where Eexpl is the error term of (3.9) above. This yields

x
2β−2 ≤ (
1 − δ
8 · ϕ(q)
q
 ) + O( q
ϕ(q) log x + q3 exp(−˜c√log x))
.

We may now choose x such that ( 4 log q
˜c )2 ≤ log x ≤ c3 log2 q for some
c3 > (4/˜c)2, so that x is not too large compared to q, but still such
that the choice is admissible with our previous assumptions (3.2) and
(3.5). Hence with 1/ log x ≤ ˜c2/16 log2 q, we obtain

x
2β−2 ≤ (1 − δ
8 · ϕ(q)
q
 ) + c1
log2 q q
ϕ(q)

for some positive constant c1, since the expression q/ϕ(q) log x domi-
nates the error term due to

q3 exp(−˜c√log x) ≤ q3 exp ( − ˜c 4
˜c log q) = q3 exp(−4 log q) = q−1.

Assume now that q is large enough so that 16c1
log2 q ≤ δ ϕ2(q)
q2 . This means
that
 x
2β−2 ≤ (1 − δ
8 · ϕ(q)
q
 ) + δ
16 ϕ(q)
q ≤ 1 − δ
16 ϕ(q)
q
for δ < 8. This gives the inequality of Theorem 11, since

β − 1 ≤ log(1 − δ
16 · ϕ(q)
q )

2 log x ≤ −cϕ(q)
q log2 q with c = δ
32c3 > 0,

where we use the upper bound for log x, which is log x ≤ c3 log2 q. □

We emphasize that all constants in the above proof are eﬀectively
computable since the constant ˜c in (3.4) coming from the prime number
theorem in progressions is itself so and all other constants in the proof
can be chosen eﬀectively depending on ˜c.

CONDITIONAL BOUNDS ON SIEGEL ZEROS 13

The next corollary gives a criterion for a composite modulus q to
satisfy Theorem 11.

Corollary 1. Assume the WHLE Conjecture and that q is a suﬃciently
large integer with #{t | q} ∩ ({4} ∪ {p ≡ 3(mod 4); p prime}) = 1. If
there is an exceptional zero β for a character mod q, then 1−β ≥ cϕ(q)
q log2 q
for some (eﬀective) constant c > 0.

Proof. For the moduli q in question there is a single real primitive
character such that χ(−1) = −1. This is certainly true if q ∈ S :=
{4} ∪ {p ≡ 3(mod 4)}, and q = tm with t ∈ S ∪ {2} and with m having
only prime divisors p ≡ 1(mod 4). Then there is only a single real
χ with χ(−1) = −1, namely the one that is induced by that mod t.
For the others, χ(−1) = 1, since this equation holds for every prime
modulus p ≡ 1(mod 4).
Hence, if we assume that β exists for an exceptional character χ, we
know that χ is real and primitive, and necessarily χ(−1) = −1. Then
Theorem 11 applies to give the assertion. □

We recover Fei’s Theorem from Corollary 1 when q = p ≡ 3(mod 4).

Under GRH except for a possible β > 3/4 and the WHLE Conjecture
we can deduce the conditional bound

L(1, χ) ≫ 1 − β ≫ ϕ(q)
q log2 q .

using Theorem 9 of Friedlander and Iwaniec, and using Theorem 11,
supposing χ(−1) = −1 for the exceptional character χ mod q. In fact,
with Goldfeld’s asymptotic formula (2.3) we can relax the assumption
of GRH with one exception to obtain

Corollary 2. Let the WHLE Conjecture be true. Assuming L(1, χ) =
o(log−1 q), we have L(1, χ) ≫ Rqϕ(q)q−1 log−2 q for an exceptional
character χ mod q with χ(−1) = −1. Here Rq = ∑

(a,b,c) a
−1 with
the sum going over all reduced quadratic forms (a, b, c) of discriminant
−q.

A reduced quadratic form of discriminant −q is an integer triple
(a, b, c) with b
2 − 4ac = −q and −a < b ≤ a < 1
4√q, see [9, p. 624].

Proof. By (2.3) from [9, p. 624] and Theorem 11, we have

L(1, χ) ∼ π2

6
 ( ∑

(a,b,c) a
−1)(1 − β) ≫ Rqϕ(q)
q log2 q .
 □

14 GAUTAMI BHOWMIK AND KARIN HALUPCZOK

Note that for a prime modulus q = p ≡ 3(mod 4), we have Rq =∑

(a,b,c) a
−1 ≥ 1 since then there is a reduced quadratic form (1, 1, c)
with a = 1. Then our bound states L(1, χ) ≫ log−2 q under the as-
sumptions of Corollary 2.

3.1. Questions. We would like to know if the case χ(−1) = 1 could
be handled as well. But we have not been able to combine the results
of [3] together with Fei’s approach which seems to be a natural way to
proceed in this direction.
One could also ask if the WHLE Conjecture itself can be obtained
from existing results. We were not able to ﬁnd anything appropriate.
Even when averaging the assertion over moduli q ≤ Q, we only reach a
special case of Conjecture 1 from [11], which seems to be out of reach.

References

[1] C. Aistleitner, K. Mahatab, M. Munsch, A. Peyrot, On large values of L(σ, χ).
Q. J. Math.70 (2019), 831–848.
[2] M.A. Bennett; G. Martin, K. O’Bryant, A. Rechnitzer, Explicit bounds for
primes in arithmetic progressions Illinois J. Math. 62 (2018), 427—532.
arXiv:1809.06920.
[3] G. Bhowmik, K. Halupczok, K. Matsumoto and Y. Suzuki, Goldbach Repre-
sentations in Arithmetic Progressions and zeros of Dirichlet L-functions, Math-
ematika 65 (2019), 57–97.
[4] E. Bombieri, Le grand crible dans la th´eorie analytique des nombres,
Ast´erisque, 18, Soc. Math. France, Paris, 1987/1974.
[5] S. Chowla, Improvement of a theorem of Linnik and Walﬁsz, Proc. London
Math. Soc. (2) 50 (1949), 423–429.
[6] J. H. Fei, An application of the Hardy–Littlewood conjecture, J. Number The-
ory 168 (2016), 39–44.
[7] J.B. Friedlander, H. Iwaniec, A note on Dirichlet L-functions, Expo. Math. 36
(2018), 343–350.
[8] D. Goldfeld, An asymptotic formula relating the Siegel zero and the class
number of quadratic ﬁelds. Ann. Scuola Norm. Sup. Pisa Cl. Sci. (4) 2 (1975),
no. 4, 611–615.
[9] D. Goldfeld, The class number of quadratic ﬁelds and the conjectures of Birch
and Swinnerton-Dyer, Ann. Scuola Norm. Sup. Pisa 3, 4 (1976), 623–663.
[10] A. Granville, K. Soundararajan, Upper bounds for |L(1, χ)|. Q. J. Math. 53
(2002) 26–284.
[11] K. Halupczok, Goldbach’s problem with primes in arithmetic progressions and
in short intervals, J. Th´eor. Nombres Bordeaux, 25 no. 2 (2013), 331–351.
[12] Y. Lamzouri, X. Li and K. Soundararajan, Conditional bounds for the least
quadratic non-residue and related problems, Math. Comp 84 (2015), 2391–
2412.
[13] H. L. Montgomery, R.C. Vaughan, Multiplicative Number Theory I, Classical
Theory, Cambridge, 2007.

CONDITIONAL BOUNDS ON SIEGEL ZEROS 15

[14] J. Pintz, Elementary methods in the theory of L-functions. VIII. Real zeros of
real L-functions. Acta Arith. 33 (1977), 89–98.
[15] P. Sarnak, A. Zaharescu, Some remarks on Landau–Siegel zeros, Duke Math.
J. 111 (2002), 495–507.
[16] P. J. Stephens, Optimizing the size of L(1, χ). Proc. London Math. Soc. 24
(1972), 1–14.
[17] T. Tatuzawa, On a theorem of Siegel, Jap. J. Math. 21 (1951), 163–178.

G. Bhowmik: Laboratoire Paul Painlev´e, Labex-CEMPI, Universit´e
de Lille, 59655 Villeneuve d’Ascq Cedex, France
Email address: gautami.bhowmik@univ-lille.fr

K. Halupczok: Mathematisches Institut der Heinrich-Heine-Universit¨at
D¨usseldorf, Universit¨atsstr. 1, 40225 D¨usseldorf, Germany
Email address: karin.halupczok@uni-duesseldorf.de
