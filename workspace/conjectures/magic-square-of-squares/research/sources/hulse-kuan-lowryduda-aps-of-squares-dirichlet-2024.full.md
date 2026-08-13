<!-- source: https://arxiv.org/pdf/2007.14324 | converted from PDF -->

arXiv:2007.14324v4  [math.NT]  11 Oct 2023
ARITHMETIC PROGRESSIONS OF SQUARES AND
MULTIPLE DIRICHLET SERIES

THOMAS A. HULSE, CHAN IEONG KUAN, DAVID LOWRY-DUDA,
AND ALEXANDER WALKER

Abstract. We study a Dirichlet series in two variables which counts
primitive three-term arithmetic progressions of squares. We show that
this multiple Dirichlet series has meromorphic continuation to C2 and
use Tauberian methods to obtain counts for arithmetic progressions of
squares and rational points on x2 + y2 = 2.

1. Introduction

In this paper, we produce estimates for the number of primitive three-
term arithmetic progressions of integer squares, {a2, b2, c2} with c2 − b2 =
b2−a2, whose terms are constrained to lie in certain regions. As no nontrivial
arithmetic progression of integer squares has more than three terms — stated
by Fermat and proved by Euler (among others) — we refer to three-term
arithmetic progressions more succinctly as just arithmetic progressions, or
APs. (See [Dic13, Vol II, Ch. XIV] for a description of the early history of
this problem).
To study primitive APs of squares, we study the multiple Dirichlet series

D(s, w) := ∑

m,h≥1
(m,h)=1
 r1(h)r1(m)r1(2m − h)
mshw ,

where rℓ(n) denotes the number of ways to represent n as a sum of ℓ squares.
Thus r1(·) is eﬀectively a square indicator function, and the numerator of
this Dirichlet series identiﬁes whether {h, m, 2m − h} is an AP of squares.
Our principal result is Theorem 5.1, which states that D(s, w) has mero-
morphic continuation to C2 by means of spectral expansion. We then exploit
this meromorphic continuation to obtain a variety of asymptotic results for
the distribution of primitive APs.
Shifted convolutions of pairs of coeﬃcients of modular forms frequently
appear in analytic number theory, and there exist several methods capa-
ble of handling them. In contrast, triple shifted convolutions are typically
poorly understood and have fewer general techniques for analysis. Most
other analyses follow the ideas and methods of Blomer from [Blo17], which
studies triple convolutions involving divisor functions. As Blomer notes, it
1

2 HULSE, KUAN, LOWRY-DUDA, AND WALKER

is possible to use the circle method to study triple convolutions of coeﬃ-
cients of holomorphic cusp forms, but extending these techniques to other
non-cuspidal modular forms seems diﬃcult.
In [HKLDW19], the authors produce a meromorphic continuation for a
triple shifted convolution Dirichlet series formed from holomorphic cusp
forms using spectral techniques. In this paper, we extend this analysis to
classical theta functions in order to study D(s, w). It is possible to extend
the techniques in this paper to other non-cuspidal holomorphic forms; the
primary diﬃculty in generalization lies in understanding growth of terms in
the spectral decomposition.

Outline of Paper and Results

The paper [HKLDW19] concerns triple shifted convolutions of the form

∑

m,h≥1
 a(h)b(m)c(2m − h)
mshw , (1.1)

where the coeﬃcients a(·), b(·), and c(·) are coeﬃcients of holomorphic cusp
forms of full integral weight. At ﬁrst glance, the challenge in adapting meth-
ods from the cuspform case (1.1) to D(s, w) appears principally technical.
However, closer inspection reveals that the spectral behavior of D(s, w) is
distinguished in a way that requires signiﬁcantly more speciﬁcity and care.
We begin in Section 2 with an overview of some classical counting prob-
lems which can be studied using D(s, w). In particular, we discuss the
asymptotics of primitive APs of squares, as noted above, as well as their
connections to Pythagorean triples, congruent numbers, and rational points
on circles. In particular, since {a2, b2, c2} corresponds to a rational point
(a/b, c/b) on the circle x2 + y2 = 2, counts for APs of squares relate to
counts for rational points on the circle of radius √2.
In Section 3, we study the single Dirichlet series

Dh(s) = ∑

m≥1
 r1(m)r1(2m − h)
ms

for a ﬁxed h. We obtain this series as an integral involving Im(z)1/2θ(2z)θ(z),
which must be regularized at the cusps of Γ0(8) for the sake of convergence.
We produce a spectral expansion for this regularized form in Section 4.
Once simpliﬁed, this expansion involves only a simple term introduced in
regularization and a sum over dihedral Maass forms on Γ0(8). In Section 5,
we study the full double Dirichlet series D(s, w) and, in Theorem 5.1, we
deduce its meromorphic continuation from its spectral expansion.
In Sections 7 and 8, we apply the meromorphic continuation of D(s, w)
to a variety of problems on APs of squares. For example, in Section 7.1, we
prove the following theorem.

ARITHMETIC PROGRESSIONS OF SQUARES 3

Theorem (Theorem 7.1). Fix δ ∈ [0, 1]. For any ǫ > 0, the number of
primitive APs of squares {a2, b2, c2} with b2 ≤ X and (a/b)2 ≤ δ is

2
π2 arcsin(
√δ/2)X 1
2 + Oǫ(X 3
8 +ǫ).

As shown in Section 2, the main term above agrees with known results
concerning the equidistribution of rational points on the circle.
In Section 8, we prove three more theorems as further applications. First,
we count primitive APs of squares with bounded maximum.

Theorem (Theorem 8.1). For any ǫ > 0, the number of primitive APs of
squares {a2, b2, c2} with c2 ≤ X is
√2
π2 log(1 + √2)X 1
2 + Oǫ(
X 3
8 +ǫ)
.

This result is then applied to count primitive APs of squares with inde-
pendently bounded ﬁrst and second terms.

Theorem (Theorem 8.3). Suppose that Y ≤ X. For any ǫ > 0, the number
of primitive APs of squares {a2, b2, c2} for which a2 ≤ Y and b2 ≤ X is

1
√2π2 Y 1
2 log (X/Y ) + c Y 1
2 + Oǫ(X ǫY 3
8 +ǫ)
,

in which c = √2
(1 + 3
2 log 2 − log(1 + √
2)
)/π2.

Lastly, we count primitive APs of squares in which the product of the
ﬁrst two terms is bounded.

Theorem (Theorem 8.4). For any ǫ > 0, the number of primitive APs of
squares {a2, b2, c2} for which ab ≤ X is

2
√2
π2 2F1( 1
4 , 1
2 , 5
4 , 1
2 )X 1
2 + Oǫ(X 3
8 +ǫ)
.

Acknowledgements

CK is supported in part by NSFC (No.11901585). DLD gratefully ac-
knowledges support from EPSRC Programme Grant EP/K034383/1 LMF:
L-Functions and Modular Forms and support from the Simons Collaboration
in Arithmetic Geometry, Number Theory, and Computation via the Simons
Foundation grant 546235. The authors would like to thank Dan Bump,
Sol Friedberg, Jeﬀ Hoﬀstein, Henryk Iwaniec, Alex Kontorovich, Min Lee,
Philippe Michel, and Paul Nelson for many helpful conversations.

2. Connections to Rational Points and Right Triangles

Before proving our main results, we consider connections to rational points
on the circle x2 + y2 = 2 and to integer right triangles.

4 HULSE, KUAN, LOWRY-DUDA, AND WALKER

2.1. Equidistribution of points on the circle. In Theorem 7.1, we con-
sider the number of primitive APs of squares {a2, b2, c2} for which (a/b)2 ≤ δ.
This result can also be seen through the lens of equidistribution.
To see this connection, note that a2 + c2 = 2b2 in an AP of squares, and
hence (a/b, c/b) is a rational point on the circle x2 + y2 = 2. Let A(b) denote
the number of rational points on x2 +y2 = 2 of the (reduced) form (a/b, c/b).
We see that
∑

d|b A(d) = #{(a, c) ∈ Z2 : a2 + c
2 = 2b2} = r2(2b2) = r2(b2).

Recalling that r2(n)/4 is multiplicative, we can compute the Dirichlet series
∑

n≥1
 A(n)
ns = 4ζ(s)L(s, χ4)
(1 + 2−s)ζ(2s) ,

where χ4 = ( −1
· ) is the non-trivial character of modulus 4. An application
of Perron’s formula and trivial estimates show that the number of rational
points on x2 + y2 = 2 of the (reduced) form (a/b, c/b) with b ≤ √X is
∑

b≤√X A(b) = 4
π X 1
2 + O(X 1
3 +ǫ).

If we assume that rational points on the circle equidistribute with respect
to arc length as their denominators grow, then we should expect the number
of rational points (a/b, c/b) on x2 +y2 = 2 in the ﬁrst quadrant with b ≤ √X
and (a/b) ≤ √δ to be approximately

arcsin(
√δ/2)
2π · 4
π X 1
2 = 2
π2 arcsin(
√δ/2)X 1
2 .

This agrees exactly with the main term which appears in Theorem 7.1.

Remark 2.1. An elementary proof of the equidistribution of rational points
on x2+y2 = 1 with respect to arc length as the size of the denominators grow
can be found, for example, in [TB18]. The methods applied therein can be
adapted to the circle x2 + y2 = 2 via the linear map (x, y) → (x + y, x − y).
More generally, there is a deep and rich literature on studying aspects of
equidistribution on spheres, and more generally on varieties. The analogous
case in 3 dimensions on the unit sphere is proven in [Duk03]. However, the
authors are not aware of any equidistribution results for rational points on
varieties which employ the properties of multiple Dirichlet series.

2.2. Right triangles. There is a well-known one-to-one correspondence be-
tween APs of squares with common diﬀerence t and right triangles with area
t, given by
{(a, b, c) : b
2 − a2 = t = c
2 − b2} ↔{(α, β, γ) : α
2 + β2 = γ2, αβ/2 = t}

(a, b, c) ↦→ (c − a, c + a, 2b), (α, β, γ) ↦→ ( β−α
2 , γ
2 , β+α
2 )
.

ARITHMETIC PROGRESSIONS OF SQUARES 5

Thus counts of primitive APs of squares can lead to counts for primitive
Pythagorean triples.
In particular, each of our main theorems implies a corresponding result
about the number of primitive right triangles under certain constraints. For
example, Theorem 7.1 implies that the number of primitive right triangles
with hypotenuse at most X and whose acute angles lie within ω of π
4 is

2ω
π2 X + Oǫ(X 3
4 +ǫ),

for any ǫ > 0. Through the same correspondence, Theorem 8.1 provides a
count for primitive right triangles (α, β, γ) for which α + β is bounded and
Theorem 8.3 yields a count for primitive triangles of bounded hypotenuse
and separately bounded diﬀerence in leg length.

3. The Single Dirichlet Series

Let θ(z) = ∑n∈Z e(n2z) = ∑n≥0 r1(n)e(nz) denote the classical theta
function, where e(z) = e2πiz. Then θ(z) is a modular form of weight 1/2
on Γ0(4). Consider also the weight 0, level 8 Eisenstein series and Poincar´e
series with character χ(d) = ( 2
d ), given by

E(z, s; χ) = ∑

γ∈Γ∞\Γ0(8)
χ(γ) Im(γz)
s = ys + ∑

c>0
 ∑

d∈Z
(8c,d)=1
 ys( 2
d )

|8cz + d|2s , (3.1)

Ph(z, s; χ) = ∑

γ∈Γ∞\Γ0(8)
χ(γ) Im(γz)
se(hγz). (3.2)

These sums converge absolutely for Re s > 1 and extend meromorphically
to s ∈ C. Here and henceforth, we use x and y to represent the real and
imaginary parts of the complex number z.
In this section, we construct the single Dirichlet series

Dh(s) := ∑

m≥1
 r1(m)r1(2m − h)
ms (3.3)

by studying the Petersson inner product

⟨y 1
2 θ(2z)θ(z) − E(z, 1
2 , χ), Ph(z, s; χ).⟩,

We establish in this section that √yθ(2z)θ(z) − E(z, 1
2 , χ) ∈ L2(Γ0(8)\H; χ).
This result is used in Section 4 to study the spectral expansion and mero-
morphic continuation of (3.3).

3.1. Background on θ(z). Recall that θ(z) is a modular form of weight 1
2
on Γ0(4). Under the action of γ ∈ Γ0(4), it transforms as follows:

θ(γz) = ( c
d
 )
ε
−1
d (cz + d) 1
2 θ(z), γ = (a b
c d

) ∈ Γ0(4), (3.4)

6 HULSE, KUAN, LOWRY-DUDA, AND WALKER

where εd is 1 if d ≡ 1 mod 4 and is i if d ≡ 3 mod 4. The character ( c
d )

refers to Shimura’s extension of the Jacobi symbol, and the square root √z
denotes the branch √z = exp( 1
2 log z) with the principal branch of the log.
The multiplier θ(γz)/θ(z) is the standard half-integral weight multiplier.
We also recall the identity

θ(−1/4z) = √−2izθ(z). (3.5)

For notational convenience we deﬁne

Ψ(z) := θ(2z).

From the computations

2 (a b
c d

) z = (a 2b
c
2 d
 ) 2z and ( c/2
d
 ) = ( 2
d
 )( c
d
 ),

we see that Ψ transforms like

Ψ(γz) = ( 2
d
 )( c
d
 )ε
−1
d (cz + d) 1
2 Ψ(z), γ = (a b
c d

) ∈ Γ0(8). (3.6)

Thus Ψ(z) is a modular form of weight 1
2 , level 8, and character χ(d) = ( 2
d ).
We also deﬁne V1(z) := y 1
2 Ψ(z)θ(z).
One can check that V1 is an automorphic form of weight 0, level 8, and
character χ(d).
The congruence subgroup Γ0(8) has four cusps: ∞, 0, 1
2 , and 1
4 . We
need to understand the behavior of θ and Ψ at each cusp. To describe this
behavior, we follow Shimura [Shi73] and Koblitz [Kob93].
Let GL(2, R)+ be the set of 2 × 2 matrices with positive determinant.
We deﬁne the metaplectic cover ̃G to be the set of pairs (γ, ϕ(z)), where
γ = ( a b
c d ) ∈ GL(2, R)+ and ϕ(z) is a holomorphic function on the upper
half-plane H such that

ϕ(z)
2 = t cz + d
det(γ)1/2 , for some t ∈ C× such that |t| = 1.

Then ̃G is a group with the group law (γ1, ϕ1)(γ2, ϕ2) = (γ1γ2, ϕ1(γ2z)ϕ2(z)).
The cover ̃G surjects onto GL(2, R)+ through the homomorphism (γ, ϕ) ↦→
γ, and we write the image of this map as

(γ, ϕ)∗ := γ.

In the other direction, for γ ∈ Γ0(8), deﬁne

j2(γ, z) = θ(2γz)
θ(2z) ,

which is the transformation law for Ψ as in (3.6). We deﬁne a homomorphism

γ ↦→ γ∗ := (γ, j2(γ, z)),

which is one-to-one from Γ0(8) to ̃G.

ARITHMETIC PROGRESSIONS OF SQUARES 7

For σ = (γ, ϕ) ∈ ̃G, we recall the deﬁnition of the weight k (k ∈ 1
2 Z) slash
operator on a function f : H −→ C, given by

f ∣
∣
[σ](z) := f (γz)

ϕ(z)2k .

In what follows, we write f |[γ] = f |[γ∗] for γ ∈ Γ0(8) to denote the weight k
slash operator. The weight, either 1
2 or 0, will be clear from context.
A half-integral weight modular form f on Γ0(8) with transformation law
j2 admits Fourier expansions at each cusp a ∈ {∞, 0, 1
2 , 1
4 } given by f ∣
∣
[σa] for

distinguished elements σa ∈ ̃G. Each σa ∈ ̃G projects to a classical scaling
matrix for a so that (σa)∗(∞) = a. In addition, for some t ∈ C× with |t| = 1,
σa satisﬁes σ−1
a η∗
aσa = (T, t),

where T = ( 1 1
0 1 ) and where ηa generates the stabilizer Γa of the cusp a in
Γ0(8).

3.2. Behavior at the cusps. Elements σa ∈ ̃G for each cusp of Γ0(8) are
given by

σ∞ = ( (1 0
0 1
) , 1
), σ0 = ( (0 −1
8 0
 ) , √−2
√2zi)
,

σ 1
2 = ( (2 0
4 1
) , √2
√2z + 1√2
 ), σ 1
4 = ( (1 0
4 1
) , √4z + 1
).

We allow ̃G to act on H through G, and we write the action as

σaz := (σa)∗z.

By studying these actions, we compute the behavior of θ(z), Ψ(z) = θ(2z),
and V1(z) at each cusp.
The behavior as z → i∞ is directly evident from the Fourier expansion
of θ, and we have that

θ(σ∞z) = 1 + O(e
−2πy), Ψ(σ∞z) = 1 + O(e
−4πy),

V1(σ∞z) = y 1
2 (1 + O(e
−2πy)
).

At the 0 cusp, we have that

θ∣
∣
[σ0] = (−2
√2zi)− 1
2 θ(−1/8z) = (2) 1
4 θ(2z) = (2) 1
4 Ψ(z),

Ψ∣
∣
[σ0] = (−2
√2zi)− 1
2 Ψ(−1/8z) = (−2
√2zi)− 1
2 θ(−1/4z) = (2)− 1
4 θ(z),
(3.7)

where we have used (3.5) in each (and frequently in the sequel). It follows
that V1|[σ0] = y1/2(Ψθ)|[σ0] = y1/2Ψθ = V1,
and thus V1(σ0z) = y 1
2 (1 + O(e
−2πy)
).

8 HULSE, KUAN, LOWRY-DUDA, AND WALKER

The 1/2 and 1/4 cusps are similar to each other. Since these two cusps
play a much smaller role in this paper, we will only describe the 1/2 cusp
in detail. We have that

θ∣
∣
[σ1/2] = 2 1
4 (4z + 1)− 1
2 θ( 2z
4z + 1
 ) = 2 1
4 (4z + 1)− 1
2 θ( 1
2 + 1/2z
 )

= 2 1
4 ( i
4z
 ) 1
2 θ( − 1
2 − 1
8z
 ) = 2 1
4 ( i
4z
 ) 1
2 (
2θ( −1
2z ) − θ( −1
8z )
)

= 2 1
4 (θ( z
2 ) − θ(2z)
).

To pass from each line to the next, we apply (3.5). The equality on the
second line follows from the general identity θ(z − 1
2 ) = 2θ(4z) − θ(z), which
can be seen by comparing Fourier expansions.
Similarly, we compute that

Ψ∣
∣
[σ1/2] = 2 1
4 ( 1+i
2 θ(z) − iθ(4z)
),

where we have used the general identity θ(z − 1
4 ) = (1 + i)θ(4z) − iθ(z).
Combining these together, it follows that

V1(σ1/2 z) = O(
√ye
−πy).

We note that the exponential decay comes from θ|[σ1/2], whose constant
Fourier coeﬃcient vanishes.
The behavior at the cusp 1
4 is similar. As θ is a modular form on Γ0(4),
we have that θ|[σ1/4] = θ. Analogous computations to those with θ|[σ1/2]
show that

Ψ∣
∣
[σ1/4] = (4z + 1)
− 1
2 Ψ( z
4z + 1
 ) = (4z + 1)
− 1
2 θ( 2z
4z + 1
 )

= θ( z
2 ) − θ(2z),

which implies that V1(σ1/4 z) = O(
√ye
−πy).

In this case, the exponential decay comes from Ψ|[σ1/4], whose constant
Fourier coeﬃcient vanishes.

3.3. Constructing V . Now that we have established that V1 decays ex-
ponentially at the 1/2 and 1/4 cusps, and that V1 and V1(σ0z) grow like
√
y + O(e−πy), we construct a function V from V1 that decays exponentially
at every cusp.
Let E(z, s; χ) denote the Eisenstein series (3.1). Deﬁne

V (z) := √yθ(2z)θ(z) − E(z, 1
2 ; χ) = V1(z) − E(z, 1
2 ; χ). (3.8)

The remainder of this section proves the following proposition.

Proposition 3.1. The function V (z) lies in L2(Γ0(8)\H; χ).

ARITHMETIC PROGRESSIONS OF SQUARES 9

To prove this, we study the growth of E(z, 1
2 ; χ) at each cusp. This
information may be read from the constant terms in the Fourier expansions
of E(z, 1
2 ; χ) at each cusp.
For the cusp ∞, we elect to compute the full Fourier expansion of E(z, s; χ)
so as to avoid duplicate work in a later section. This expansion is presented
in the following lemma.

Lemma 3.2. The Fourier expansion of E(z, s; χ) is

E(z, s; χ) = ys + ∑

h̸=0 ρy,s(h)e
2πihx,

in which the coeﬃcients ρy,s(h) are deﬁned by

ρy,s(h) = πsy 1
2 |h| 1
2 −sσχ
2s−1(h)

2
6s− 5
2 Γ(s)L(2s, χ) Ks− 1
2 (2π|h|y). (3.9)

Proof. Let δij denote the Kronecker delta function. Beginning from (3.1),
we directly evaluate
∫ 1

0 L(2s, χ)E(z, s; χ)e
−2πihxdx

= L(2s, χ)ysδh0 + ∑

c>0
 1
(8c)2s
 8c−1∑

r=0
 ∑

m∈Z
 ∫ 1

0
 ys( 2
r )e−2πihx

|z + m + r
8c |2s dx

= L(2s, χ)ysδh0 + 1
26s ∑

c>0
 1
c2s
 8c−1∑

r=0 e
( hr
8c
 )( 2
r
 ) ∫ ∞

−∞
 yse−2πihx

(x2 + y2)s dx.

When h = 0, the r-sum vanishes and only the L(2s, χ)ys term survives.
Otherwise, we evaluate the integral as in [Gol15, 3.1.9]. Writing r = 8r′ + q
with 0 ≤ q < 8 and 0 ≤ r′ < c transforms the sum over r into the product
of an exponential sum and a Gauss sum. It ultimately follows that

8c∑

r=1 e
( hr
8c
 )( 2
r
 ) =
 {
2
√2c ( 2
h/c ) if c | h,

0 otherwise.

Simpliﬁcation and analytic continuation completes the proof. □

We note in particular that E(σ∞z, s; χ) = ys + O(e−2πy), and hence V (z)
vanishes at the cusp at ∞.
For the cusp at 0, we compute that

E(σ0 z, s; χ) = ∑

γ∈Γ∞\Γ0(8) χ(γ) Im(γ(−1/8z))
s = ∑

d>0
 ∑

c∈Z
(8c,d)=1
 (y/8)s( 2
d )
|dz − c|2s .

10 HULSE, KUAN, LOWRY-DUDA, AND WALKER

Thus the constant term in the Fourier expansion of L(2s, χ)E(σ0 z, s; χ) is
∫ 1

0 L(2s, χ)E(σ0 z, s; χ)dx

= 1
8s ∑

d>0
 ( 2
d )
d2s
 d∑

r=1
 ∑

m∈Z
 ∫ 1

0
 ys

|z − m − r
d |2s dx

= 1
8s ∑

d>0
 ( 2
d )
d2s−1
 ∫ ∞

−∞
 ys

(x2 + y2)s dx = √πΓ(s − 1
2 )
8sΓ(s) L(2s − 1, χ)y1−s.

It follows that the constant term in the Fourier expansion of E(σ0 z, 1
2 ; χ) is

lim
s→ 1
2
 y1−s√πΓ(s − 1
2 )L(2s − 1, χ)
8sΓ(s)L(2s, χ) = √y, (3.10)

in which we have used the functional equation

Λ(s, χ) := (π/8)
− s
2 Γ( s
2 )L(s, χ) = Λ(1 − s, χ)

to compute the limit. Thus V1 cancels with E(z, 1
2 ; χ) at the 0 cusp and V
vanishes there.
As V1 vanishes at the 1/2 and 1/4 cusps, it remains only to show that
E(z, 1
2 ; χ) vanishes there as well. For 1/4, we have that

E(σ1/4 z, s; χ) = ∑

c>0
2∤c
 ∑

d∈Z
(4c,d)=1
 ys( 2
d )
|4cz + d|2s .

As χ(d−4c) = −χ(d) for odd c, we ﬁnd E(σ1/4 (z+1), s; χ) = −E(σ1/4 z, s; χ).
Thus the constant Fourier term in E(σ1/4 z, s; χ) must vanish. Similarly,

E(σ1/2 z, s; χ) = ∑

c>0
 ∑

(4c,d)=1
d≡c mod 4
 (2y)s( 2
d )
|4cz + d|2s ,

and one can check that E(σ1/2 (z +1), s; χ) = −E(σ1/2 z, s; χ). The constant
Fourier term in E(σ1/4 z, s; χ) vanishes.
We conclude the V (z) lies in L2(Γ0(8)\H; χ) as claimed.

3.4. Constructing the single Dirichlet series. We now construct and
study Dh(s) from (3.3). To do so, we examine the inner product

⟨V (z), Ph(z, s; χ)⟩,

where V is as in (3.8) and Ph is the Poincar´e series (3.2). We will see that
this inner product encodes the single Dirichlet series Dh(s).

Proposition 3.3. For h ≥ 1 and Re s ≫ 1, we have that

Dh(s) = (8π)s⟨V, Ph(·, s + 1
2 ; χ)⟩
Γ(s) + 2s√πσχ
0 (h)Γ(s)
log(1 + √2)hsΓ(s + 1
2 ) ,

ARITHMETIC PROGRESSIONS OF SQUARES 11

where σχ
w(h) = ∑

d|h χ(d)d
w

is a twisted divisor sum.

Proof. We evaluate ⟨V, Ph⟩ explicitly. As Ph ∈ L2(Γ0(8)\H; χ) for suﬃ-
ciently large Re(s), we can consider the inner products against the two parts
of V = V1 − E separately. The inner product against V1 = Im(·)1/2Ψθ yields
the Dirichlet series, as is seen through the classical unfolding argument:

⟨Im(z) 1
2 θ(2z)θ(z), Ph(z, s; χ)⟩ = ∫ ∞

0
 ∫ 1

0 ys− 1
2 θ(2z)θ(z)e(hz) dx dy
y

= ∑

m1,m2 r1(m1)r1(m2) ∫ ∞

0
 ∫ 1

0 ys− 1
2 e(2m1z − m2z − hz) dx dy
y

=
 ∞∑

m=1 r1(m)r1(2m − h) ∫ ∞

0 ys− 1
2 e
−8πmy dy
y

= Γ(s − 1
2 )

(8π)
s− 1
2
 ∑

m≥1
 r1(m)r1(2m − h)

ms− 1
2 .

The inner product of Ph against the Eisenstein series essentially extracts
the h-th Fourier coeﬃcient of the Eisenstein series, ρy,w(h). A short com-
putation shows that

⟨E(z, w; χ), Ph(z, s; χ)⟩ = ∫ ∞

0 ρy,w(h)e
−2πyhys−1 dy
y .

A formula for the Fourier coeﬃcient ρy,w(h) appears in (3.9). Applying that
identity and changing variables to simplify the integral, we rewrite the inner
product as
 πwh 1
2 −wσχ
2w−1(h)

2
6w− 5
2 Γ(w)L(2w, χ)
 1

(2πh)
s− 1
2
 ∫ ∞

0 Kw− 1
2 (y)e
−yys− 1
2 dy
y .

The integral above appears in the integral table [GR15, 6.621(3)]. Applying
the integral from the table and evaluating at w = 1
2 , we see that

⟨E(z, 1
2 ; χ), Ph(z, s; χ)⟩ = π1−sσχ
0 (h)Γ(s − 1
2 )2

2
2s− 1
2 h
s− 1
2 L(1, χ)Γ(s).

The class number formula gives L(1, χ) = log(1+√
2)/
√2. After rearranging
and shifting s ↦→ s + 1
2 , we complete the proof. □

4. Spectral Expansion

We now produce a spectral expansion for Dh(s). To do this, we provide a
spectral expansion for ⟨V, Ph⟩ by spectrally expanding the Poincar´e series Ph.
This approach to constructing and studying Dirichlet series is not new, and
is now well-understood. See for instance the appendix to [Sar01], the work

12 HULSE, KUAN, LOWRY-DUDA, AND WALKER

of Hoﬀstein and Hulse [HH16], or previous work of the authors [HKLDW18].
But in contrast to these previous works, the behavior of this spectral ex-
pansion is distinguished. We will see that the continuous component of the
spectrum vanishes and the discrete component consists entirely of explicit
dihedral Maass forms. Together, these allow for an unusually descriptive
understanding of the spectral behavior.
We remark that the relative thinness of the spectral support of V is pre-
ﬁgured by similar results of Nelson [Nel21] on the spectral decomposition of
y1/2|θ(z)|2. (See also [Nel19, §1].) There, the discrete spectrum vanishes in
entirety owing to the non-existence of dihedral forms with trivial character.
As is summarized in [Mic07, §2.1.2.1], forms in L2(Γ0(8)\H; χ) can be
decomposed as a spectral expansion over Maass forms and Eisenstein series.
In particular, since Ph(z, s; χ) ∈ L2(Γ0(8)\H; χ) for suﬃciently large Re(s),
it has a spectral expansion of the form

Ph(z, s; χ) = ∑

j ⟨Ph(·, s; χ), µj ⟩µj(z)

+ ∑

a
 1
4π
 ∫ ∞

−∞⟨Ph(·, s; χ), Ea(·, 1
2 + it; χ)⟩Ea(z, 1
2 + it; χ)dt.

Here, {µj} is an orthonormal basis of Hecke-Maass forms for L2(Γ0(8)\H; χ),
where µj has eigenvalue 1
4 + t2
j and type 1
2 + itj. The sum over a ranges
over the cusps of Γ0(8) that are non-singular with respect to χ, which are
the cusps at 0 and ∞.
Inserting this into the inner product ⟨V, Ph⟩ yields the spectral expansion

⟨V (z), Ph(z, s; χ)⟩ = ∑

j ⟨Ph(·, s; χ), µj⟩⟨V, µj⟩ (4.1)

+ ∑

a
 1
4π
 ∫ ∞

−∞ ⟨Ph(·, s; χ), Ea(·, 1
2 + it; χ)⟩⟨V, Ea(z, 1
2 + it; χ)⟩dt.

This expansion simpliﬁes further, and to that end it is helpful that we take
a brief digression into the Maass forms of L2(Γ0(8)\H, χ).

4.1. Maass forms and dihedral Maass forms. Each Maass form in this
spectral expansion of (4.1) has a Fourier expansion of the form

µj(z) = √y ∑

n≥0 ρj(n)Kitj (2π|n|y)e
2πinx,

and associated simultaneous Hecke eigenvalues λj(n). These eigenvalues
satisfy the recurrence relation

λj(pn+1) = λj(p)λj(pn) − χ(p)λj(pn−1) (4.2)

and are multiplicative, in that λj(mn) = λj(m)λj(n) for (m, n) = 1.
We normalize each µj so that the basis {µj} is orthonormal with respect
to the Petersson inner product. Thus for each Maass form there is a constant

ARITHMETIC PROGRESSIONS OF SQUARES 13

ρj(1) such that ρj(n) = ρj(1)λj (n), and we may assume ρj(1) ∈ R without
loss of generality.
Several Maass forms in L2(Γ0(8)\H, χ) can be described explicitly. These
are Maass forms coming from Hecke characters deﬁned on ideals of Q(
√2)
and are examples of dihedral Maass forms, Maass forms whose L-functions
are Hecke L-functions [LY02]. Rather interestingly, these forms comprise
the entirety of the spectral expansion of ⟨V, Ph⟩.
For each m ∈ Z̸=0, consider the function

fm(z) = ∑

n≥1
 ∑

N (b)=n
η(b)
m√yK imπ
2 log(1+√2) (2πny)(e(nx) + (−1)
me(−nx)) (4.3)

in which η(b) is the Hecke character deﬁned on ideals of Q(
√2) by

η((a + b√2)
) = sgn(a + b√2) sgn(a − b
√2)
∣
∣
∣ a + b
√2
a − b
√2
 ∣
∣
∣
 iπ
2 log(1+√2) .

We note that fm(z) = f−m(z). It suﬃces to deﬁne η on principal ideals, as
the ring of integers in Q(
√2) is a principal ideal domain. Following Maass,
and as recounted in [Bum97, Theorem 1.9.1], the functions fm(z) are indeed
Maass cusp forms for Γ0(8) with nebentypus χ and type 1
2 + imπ
2 log(1+√2) .

These forms have multiplicative Hecke eigenvalues λm(h) for which

fm(z) = ∑

n̸=0 λm(n)
√yK imπ
2 log(1+√2) (2π|n|y)e(nx),

and these λm(h) can be deﬁned on rational primes p as

λm(p) =
 



ηm(p) + η−m(p) if χ(p) = 1,
0 if χ(p) = −1,
(−1)m if p = 2, (4.4)

where p is a prime ideal in the integer ring of Q(
√2) over Z such that
p splits as (p) = pp. We then deﬁne λm for non-zero integers via (4.2),
multiplicativity, and the relation λm(1) = (−1)mλm(−1) = 1.
In the case m = 0, the function fm(z) does not deﬁne a cusp form. Rather,
as noted in [Bum97], 1
2 log(1 + √2)
√y + f0(z) deﬁnes an Eisenstein series
on Γ0(8) with nebentypus χ. A comparison of Fourier coeﬃcients conﬁrms
that this Eisenstein series is precisely 1
2 log(1 + √2)E(z, 1
2 ; χ). In particular,
λ0(p) = σχ
0 (p) and the potential contribution of this missing Maass form is
exactly the contribution of the Eisenstein series in Proposition 3.3.
The L-functions L(s, fm) attached to these Maass forms coincide with the
Hecke L-functions
 L(s, ηm) = ∑

a
 ηm(a)
N (a)s , (4.5)

which are entire for m ̸= 0. In the case m = 0, L(s, η0) = ζ(s)L(s, χ) is
the Dedekind zeta function for Q(
√2) and admits a simple pole at s = 1.
By examining the conductors of the general functional equation for Hecke

14 HULSE, KUAN, LOWRY-DUDA, AND WALKER

L-functions, as in [Bom05], we have that the only dihedral Maass cusp forms
of level 8 and nebentypus χ are exactly our fm described above.
We may now state the main theorem of this section.

Theorem 4.1. For h ≥ 1 and Re s ≫ 1, we have that

Dh(s) = ∑

m≥1
 r1(m)r1(2m − h)
ms (4.6)

= ∑

m∈Z
 (−1)mλm(h)
hs Γ(s + imπ
2 log(1+√2) )Γ(s − imπ
2 log(1+√2) )

21−3s log(1 + √2)Γ(2s) ,

where λm(h) are deﬁned as in (4.4).

The proof of this decomposition is contained in the following subsections.
We ﬁrst compute the continuous part of the spectrum, which vanishes, then
demonstrate that only dihedral Maass forms contribute to the discrete part
of the spectrum. A ﬁnal bit of simpliﬁcation completes the proof.

4.2. Continuous spectrum. The continuous spectrum component of (4.1)
comes from Eisenstein series associated to the non-singular cusps, 0 and ∞.
We will show that both terms vanish.

Lemma 4.2. We have that ⟨V, Ea(·, s; χ)⟩ = 0 for the cusps 0 and ∞.

Proof. For the cusp at ∞, we directly compute

⟨V, E∞(z, s; χ)⟩ = ∫ ∞

0
 ∫ 1

0 V (z)ys−1 dx dy
y .

The integral over x extracts the constant term in the Fourier expansion of
V (z). As V (z) = √yθ(2z)θ(z) − E(z, 1
2 ; χ), the constant Fourier coeﬃcient
is exactly √y ∑

m≥0 r1(m)r1(2m)e
−8πmy − √
y.

Since r1(m)r1(2m) = 0 except when m = 0, in which case it is 1, we see
that the constant Fourier coeﬃcient is identically 0. Thus ⟨V, E∞⟩ = 0.
For the cusp at 0, we ﬁrst note that σ0 = ( 0 −1
8 0 ) is an involution on H
and that (0 −1
8 0
 ) ( a b
8c d
) = ( d −c
−8b a
 ) (0 −1
8 0
 ) .

Thus σ0(
Γ0(8)\H) = Γ0(8)\H and it immediately follows that E0(z, s; χ) =
E∞(σ0z, s; χ). Within the inner product

⟨V, E0(·, s; χ)⟩ = ∫ ∫

Γ0(8)\H
V (σ0(z))E∞(z, s; χ) dµ = ∫ ∞

0
 ∫ 1

0 V (σ0z)ys−1 dxdy
y ,

the integral over x extracts the constant term in the Fourier expansion
of V (σ0z). Earlier we noted that (3.7) implies that Ψθ|[σ0] = Ψθ; and
in (3.10), we computed that the constant term of E∞(σ0z, 1
2 ; χ) is √y. Thus
⟨V, E0(z, s; χ)⟩ = 0 as well. □

ARITHMETIC PROGRESSIONS OF SQUARES 15

4.3. Discrete spectrum. The integral formula [GR15, 6.621(3)] and un-
folding produces the identity

⟨Ph(·, s; χ), µj⟩ = ρj(h)
√πΓ(s − 1
2 + itj)Γ(s − 1
2 − itj)

(4πh)
s− 1
2 Γ(s)

for the inner product of the Poincar´e series and a Maass form of type 1
2 + itj.
By applying this expression and the result of Lemma 4.2 to the spectral
expansion (4.1), we obtain the following lemma.

Lemma 4.3. For h ≥ 1 and Re s ≫ 1,

⟨V, Ph(·, s; χ)⟩ = ∑

j
 ρj(h)
√π

(4πh)
s− 1
2 G(s, itj )⟨V, µj⟩,

in which G(s, z) := Γ(s − 1
2 + z)Γ(s − 1
2 − z)/Γ(s).

We now investigate the individual terms in the discrete spectrum. Just
as the inner products ⟨V, Ea⟩ caused the continuous spectrum to vanish, the
inner products ⟨V, µj⟩ cause many terms in the discrete spectrum to vanish.

Lemma 4.4. We have ⟨V, µj⟩ ̸= 0 if and only if µj = ⟨fm, fm⟩−1/2fm for
some m ∈ N as in (4.3), in which case

ρj(1)⟨V, µj ⟩ = 2(−1)m

log(1 + √2) . (4.7)

To prove this lemma, we recognize θ as the residue of a weight 1/2 Eisen-
stein series. We use this Eisenstein series in place of θ in the inner product
⟨V, µj⟩ to interpret the inner product using a Rankin-Selberg type convolu-
tion. This object has no pole unless µj is self-dual, which coincides exactly
with µj being dihedral, and implies that the associated residue must be zero
in the non-dihedral case.

Proof. We deﬁne the weight 1/2, level 8 Eisenstein series

E 1
2 (z, w; Γ0(8)) := ∑

γ∈Γ∞\Γ0(8) Im(γz)
wJ(γ, z)
−1,

in which J(γ, z) := j(γ, z)/|j(γ, z)|
is a normalization of the theta multiplier j(γ, z) = θ(γz)/θ(z) given in (3.4).
We note that this matches the deﬁnitions of the half-integral weight Eisen-
stein series deﬁned in [GH85] and [S+85], except that we normalize the
metaplectic cocycle. For comparison, if E(z, w) denotes the Eisenstein series
in either of these works, then E 1
2 (z, w; Γ0(8)) = Im(z)1/4E(z, w − 1
4 ). This
particular normalization agrees with the normalization of the metaplectic
Eisenstein series appearing in [Iwa97, §13] and in [LD17].
It is known [S+85, Theorem 2.3] that E 1
2 (z, w; Γ0(8)) has a simple pole at
w = 3
4 with residue of the form y1/4g(z), where g(z) is a holomorphic form

16 HULSE, KUAN, LOWRY-DUDA, AND WALKER

of weight 1
2 and level 8. Since the space of such forms is one-dimensional,
we have that g(z) = c−1θ(z) where c can be computed using the methods
of [GH85] to be
 c
−1 = 1
4π . (4.8)

Since θ(z) is (up to a constant) the residue of E 1
2 (z, w; Γ0(8)) at w = 3
4 ,

the same holds for θ(z) and E 1
2 (z, w; Γ0(8)). We apply the latter to study
⟨V, µj⟩, and compute that

⟨V, µj⟩ = ⟨y 1
2 θ(z)θ(2z), µj⟩ = c Res
w= 3
4 ⟨y 1
4 θ(2z)E 1
2 (z, w; Γ0(8)), µj⟩

= c Res
w= 3
4
 ∫ ∞

0
 ∫ 1

0 y 1
4 θ(2z)ywµj(z) dxdy
y2

= c Res
w= 3
4
 ∑

n≥1 r1(n)ρj(2n) ∫ ∞

0 yw− 1
4 Kitj (2πny)e
−2πny dy
y

= c Res
w= 3
4
 2 7
4 π 3
4 Γ(w − 1
4 + itj)Γ(w − 1
4 − itj)
(8π)wΓ(w + 1
4 )
 ∑

n≥1
 ρj(2n2)

n2w− 1
2 . (4.9)

The second line comes from unfolding the Eisenstein series. The third line
follows after expanding θ and µj in Fourier expansions, performing the in-
tegral over x to extract the constant term of θµj, and recognizing that
Kitj (y) = Kitj (y) when tj ∈ R ∪ iR and y ∈ R+. The fourth line follows
after computing the integral (which is computed in [GR15, 6.621(3)]).
The gamma functions are holomorphic at w = 3/4, hence the only po-
tential source of a pole in (4.9) is the Dirichlet series. This series diﬀers
trivially from the symmetric square series associated to µj,

L(s, Sym2 µj) = L(2s, χ2) ∑

n≥1
 λj(n2)
ns ,

only in the 2-factor, hence ⟨V, µj⟩ is non-zero if and only if L(s, Sym
2 µj)
has a pole at s = 1. The identity

L(s, Sym
2 µj) = L(s, µj ⊗ µj)
L(s, χ)

implies that L(s, Sym
2 µj) has a simple pole at s = 1 if and only if µj is self-
dual; that is, if λj(n) = λj(n) for all n ∈ Z. Since χ is a nontrivial character
and λj(n) = χ(n)λj(n), we have λj(n) = 0 whenever χ(n) = −1 and so
µj is unchanged when twisted by χ. As is noted in [KS02], if µj = µj ⊗ χ
for a nontrivial Maass form, then µj is a multiple of a dihedral Maass form
and, for level 8 Maass forms of weight zero and with nebentypus χ, these
must exactly be forms of the kind given in (4.3), as discussed following (4.5).
Hence µj = ρm(1)fm for some m ∈ N and ρm(1) = ⟨fm, fm⟩−1/2 = ρj(1).

ARITHMETIC PROGRESSIONS OF SQUARES 17

To prove (4.7) and complete the proof of Lemma 4.4, note from λm(2n) =
(−1)mλm(n) that the series in (4.9) is

∑

n≥1
 ρj(2n2)
ns = ρm(1)(−1)
m L(s, fm ⊗ fm)
L(2s, χ2)L(s, χ) (4.10)

Combined with (4.8) and the identity cosh(πtj)Γ( 1
2 − itj)Γ( 1
2 + itj) = π, we
rewrite (4.9) in the form

⟨V, µj⟩ = ρm(1)(−1)m√
2 π2

cosh( mπ2
2 log(1+√2) )L(2, χ2)L(1, χ) Res
w=1 L(w, fm ⊗ fm). (4.11)

By unfolding the inner product of |fm|2 against the level 8 Eisenstein series,
we also produce

Res
w=1 L(w, fm ⊗ fm) = 1
8 cosh ( mπ2

2 log(1+√2)
 )
⟨fm, fm⟩. (4.12)

Substitution of (4.12) into (4.11) gives

ρj(1)⟨V, µj ⟩ = (−1)m√2 π2

8L(2, χ2)L(1, χ) = 2 · (−1)m

log(1 + √2) ,

in which ρm(1)2 = ⟨fm, fm⟩−1, L(2, χ2) = π2
8 , and L(1, χ) = log(1 + √
2)/
√2
have been used in the simpliﬁcation. □

4.4. Proof of Theorem 4.1. Theorem 4.1 quickly follows from the pre-
vious discussion. One substitutes the spectral expansion (4.1) into the ex-
pression for Dh(s) given in Proposition 3.3. Lemma 4.2 shows that the
continuous spectrum vanishes, while Lemmas 4.3 and 4.4 give the form of
the discrete component. It follows that

Dh(s) = 21+s√π
log(1 + √
2)Γ(s)
 ∑

m≥1
 (−1)mλm(h)
hs G
(s + 1
2 , imπ
2 log(1 + √2)
 )

+ 2s√πσχ
0 (h)Γ(s)
log(1 + √2)hsΓ(s + 1
2 ) ,

The theorem now follows from the gamma duplication formula and the iden-
tities σχ
0 (h) = λ0(h) and λm(h) = λ−m(h). □

5. Constructing the Double Dirichlet Series

We now build upon the analysis of Dh(s), the Dirichlet series introduced
in (3.3), to study the meromorphic properties of the double Dirichlet series

D(s, w) := ∑

m,h≥1
(m,h)=1
 r1(h)r1(m)r1(2m − h)
mshw .

We prove the following theorem.

18 HULSE, KUAN, LOWRY-DUDA, AND WALKER

Theorem 5.1. The double Dirichlet series D(s, w) has meromorphic con-
tinuation to C2. For Re s and Re w suﬃciently large, we have

D(s, w) = 23s(1 − 2−2s−2w)
ζ (2)(4s + 4w) log(1 + √2)Γ(2s)

× ∑

m∈Z (−1)mL(2s + 2w, η2m)Γ(s + itm)Γ(s − itm), (5.1)

in which tm = mπ
2 log(1+√2) , ζ (2)(s) = (1 − 1
2s )ζ(s), and L(s, ηm) is as in (4.5).

Proof. Theorem 4.1 expresses Dh(s) as a sum, (4.6), over m ∈ Z. By multi-
plying each term in (4.6) by r1(h)/hw and summing over h ≥ 1, we produce a
decomposition for a variant of D(s, w) which omits the coprime assumption.
The sum over h ≥ 1 in that series may be written in the form

∑

h≥1
 λm(h2)
hs = L(s, χ2)L(s, η2m)
L(2s, χ2) = ζ (2)(s)L(s, η2m)
ζ (2)(2s)

by combining (4.10) with the Euler product factorization L(s, fm ⊗ fm) =
L(s, χ2)L(s, χ)L(s, η2m). Once simpliﬁed, we see that

∑

m,h≥1
 r1(h)r1(m)r1(2m − h)
mshw

= ∑

m∈Z
 (−1)mL(2s + 2w, η2m)23sζ (2)(2s + 2w)Γ(s + itm)Γ(s − itm)
ζ (2)(4s + 4w) log(1 + √2)Γ(2s) .

The identity (5.1) follows by dividing both sides by ζ(2s + 2w).
These L-functions have meromorphic continuation to all s, w ∈ C and
grow at most polynomially in tm in vertical strips. Thus Stirling’s approxi-
mation for the gamma functions gives normal convergence over m and com-
pletes the proof of the theorem. □

Remark 5.2. When w = 0, the expansion (5.1) closely resembles the hyper-
bolic Fourier expansion of the level 1, weight 0 Eisenstein series as described
in [Sie80, ch. 2, §3] or [Gol15, §3.2]. These expansions diﬀer from (5.1) by
also including the Hecke L-functions of odd powers of η.

Remark 5.3. The term m = 0 is distinguished within the sum (5.1) because
L(2s + 2w, η2m) has a polar line at 2s + 2w = 1 if and only if m = 0. In
Sections 7 and 8, we show that this polar line is the source of the main terms
in the asymptotic formulas presented in Theorems 7.1, 8.1, 8.3, and 8.4.

Remark 5.4. The function ζ(2s+2w)D(s, w) can be used to produce counts
for APs of squares which include both primitive and imprimitive APs. We
do not pursue this here, since counts for APs with unrestricted GCDs can
be obtained from the primitive case by purely elementary methods.

ARITHMETIC PROGRESSIONS OF SQUARES 19

6. Weight functions

To derive arithmetic results from Theorem 5.1, we study double sums
whose summands are r1(h)r1(m)r1(2m − h), but whose range of summation
is constrained. To study these sums, we relate them to smooth analogues.
In this section, we describe the necessary smoothing weight functions and
their properties.
We use two weight functions, u+x(t) and u−x(t). Deﬁne u+x(t) and u−x(t)
to be smooth, non-increasing functions with compact support, satisfying

u−x(t) =
 {
1 t ≤ 1 − 1
x ,
0 t ≥ 1, and u+x(t) =
 {1 t ≤ 1,
0 t ≥ 1 + 1
x ,

where x > 1 is an optimizing parameter chosen in each application. Let
U−x(s) and U+x(s) denote the Mellin transforms of u−x(t) and u+x(t), re-
spectively. Trivial bounds, diﬀerentiation under the integral, and the con-
vexity principle (coupled with repeated integration by parts) show that
(1) U±x(s) = s−1 + Os(1/x).
(2) U ′
±x(s) = s−2 + Os(1/x).
(3) for all α ≥ 1, and for s constrained in a vertical strip with |s| > ǫ,
we have
 U±x(s) ≪ǫ 1
x
 ( x
1 + |s|
 )α. (6.1)

In each application, we construct two smoothed approximations S−x and
S+x to a desired sum S, formed from smoothing S with u−x(t) and u+x(t)
respectively, such that S−x ≤ S ≤ S+x. We recognize each S±x as an integral
transform of D(s, w) against U±x(s), and use the meromorphic continuation
of D(s, w) to produce bounds.

7. Application to APs with constrained ratios

One of the advantages in studying the meromorphic properties of D(s, w)
is its ﬂexibility in producing asymptotics for a variety of sums related to APs
{h, m, 2m−h} of squares. We demonstrate this ﬂexibility through examples,
by applying classical Tauberian techniques to D(s, w).
In this section, we count primitive APs of squares in which m ≤ X and
h/m ≤ δ for some ﬁxed δ ∈ (0, 1). In Section 8, we give three further
applications: counts for primitive APs with bounded maximum, with inde-
pendently bounded ﬁrst and second terms, and for APs in which mh ≤ X.
This section serves as a model for the later applications. We provide com-
plete details here, as this application requires the most explicit computation.
The applications in Section 8 are similar, but simpler.

7.1. Statement of Result. We study sums of the form

S(X, δ) := ∑

m≤X
 ∑′

h/m≤δ r1(m)r1(h)r1(2m − h),

20 HULSE, KUAN, LOWRY-DUDA, AND WALKER

in which the ‘prime’ denotes the restriction (m, h) = 1. As described in
Section 2.1, this sum also counts rational points on the circle x2 + y2 = 2.
Our main result of this section is the following theorem.

Theorem 7.1. Fix δ ∈ [0, 1]. Then for any ǫ > 0, the number of primitive
APs of squares {h, m, 2m − h} with m ≤ X and (h/m) ≤ δ is

1
8 S(X, δ) = 1
8 ∑

m≤X
 ∑′

h/m≤δ r1(m)r1(h)r1(2m − h)

= 2
π2 arcsin(
√δ/2)X 1
2 + Oǫ(X 3
8 +ǫ).

Proof. To prove this theorem, we deﬁne

S−x(X, δ) := ∑′

m,h≥1 r1(m)r1(h)r1(2m − h)u−x( m
X )u−x( h
mδ )

S+x(X, δ) := ∑′

m,h≥1 r1(m)r1(h)r1(2m − h)u+x( m
X )u+x( h
mδ ),

where u±x are the weight functions described in Section 6. By construction
of u±x and the nonnegativity of the coeﬃcients, we have the inequalities

S−x(X, δ) ≤ S(X, δ) ≤ S+x(X, δ).

We recognize S−x and S+x as integral transforms of D(s − w, w):

S±x(X, δ) = 1
(2πi)2
 ∫
(σw)
 ∫
(σs) D(s − w, w)U±x(s)U±x(w)X sδwds dw, (7.1)

where σw and σs are within the region of absolute convergence of the multiple
Dirichlet series D(s, w). We take σw = 1
4 and σs = 10 initially, which is
justiﬁed by the upper bound r1(h)r1(m)r1(2m − h) ≪ 1 and the fact that
r(2m − h) = 0 for h > 2m.
Our treatments of S−x and S+x are nearly identical. From Theorem 5.1,
the analysis of each integral transform breaks up into the analysis of two
pieces: the m = 0 term, which corresponds to the Dedekind zeta function for
Q(
√
2), and the remainder of the discrete spectrum from (5.1). We denote
these integrals by I 0
±x and I spec
±x , respectively. Then we can rewrite (7.1) as

S±x(X, δ) = I 0
±x(10, 1
4 , X, δ) + I spec
±x (10, 1
4 , X, δ).

We study I 0
±x in Section 7.2 and I spec
±x in Section 7.3, culminating in the
bounds from Propositions 7.4 and 7.6. When combined, these bounds give

S±x(X, δ) = 16
π2 arcsin(
√δ/2)X 1
2 + O( X 1
2
x + X 1
4 +ǫx1+ǫ)
.

Choosing x = X 1/8 balances the error terms and the inequalities S−x(X, δ) ≤
S(X, δ) ≤ S+x(X, δ) imply the theorem. □

In the remainder of this section, we provide the remaining technical details
and bounds used in the proof of this theorem.

ARITHMETIC PROGRESSIONS OF SQUARES 21

7.2. Principal term. The primary growth in the integrals (7.1) comes from
the m = 0 term in the decomposition (5.1) for D(s, w). From the identity
L(s, η0) = ζ(s)L(s, χ) and the gamma duplication formula, this is

I 0
±x(σs, σw, X, δ) = 2
√π
(2πi)2
 ∫

(σw)
 ∫

(σs)
 (
U±x(s)U±x(w)X s(δ/2)
w

× 2sΓ(s − w)ζ (2)(2s)L(2s, χ)
log(1 + √2)Γ( 1
2 + s − w)ζ (2)(4s)
 )ds dw,

in which σw = 1
4 and σs = 10 to begin.
The gamma and L-functions in the integrand conspire to give at most
polynomial growth in vertical strips, which is counteracted by arbitrary
polynomial decay in the weight functions U±x(s) and U±x(w). We are thus
free to shift lines of integration and extract residues.
Shifting the line of s-integration to σs = 1
4 + ǫ passes a simple pole at
s = 1
2 from the zeta function. The residue at this pole can be written

R 1
2 := 4X 1
2
2πi
 ∫
( 1
4 )
 (δ/2)wΓ( 1
2 − w)U±x( 1
2 )U±x(w)

π 3
2 Γ(1 − w) dw. (7.2)

The dominant growth of this integral can be explicitly evaluated using the
Mellin-inversion relationship

1
2πi
 ∫
( 1
4 )
 Γ( 1
2 − w)
Γ(1 − w)w zwdw = 2
√π arcsin(
√z) (7.3)

and the approximation U±x(w) = 1/w + O(1/x). To justify our treatment
of the O(1/x) error term, we require a technical lemma.

Lemma 7.2. Fix ǫ > 0 and a meromorphic function F (w) satisfying F (w) ≪
| Im w|−ǫ on Re w = σw. Deﬁne H(z) = 1
2πi ∫
(σw) F (w) zw
w dw. Then H(z) is
meromorphic and for z ≥ 0, we have

1
2πi
 ∫

(σw) F (w)U±x(w)zw dw = H(z) + O( z
x sup
|s−z|<|z|/x |H ′(s)|
).

for x ≫ 1.

Proof. We expand U±x as an integral, integrate by parts, and then swap the
order of integration. Expanding U±x and integrating by parts gives that

1
2πi
 ∫

(σw) F (w)U±x(w)zwdw = 1
2πi
 ∫
(σw) F (w)zw ∫ ∞

0 u±x(t)tw dt
t dw

= 1
2πi
 ∫
(σw) F (w)zw( − 1
w
 ∫ 1+1/x

0 u′
±x(t)twdt)
dw.

22 HULSE, KUAN, LOWRY-DUDA, AND WALKER

The w-integrand now decays as O(| Im w|−1−ǫ), which justiﬁes the inter-
change of the order of integration. After reordering, this becomes

− ∫ 1+ 1
x

0 u
′
±x(t)
( 1
2πi
 ∫

(σw) F (w)(zt)
w dw
w
 )
dt = − ∫ 1+ 1
x

0 u′
±x(t)H(zt)dt.

Cauchy’s diﬀerentiation formula implies that H is meromorphic. Integration
by parts presents the last integral above in the form

− u±x(t)H(zt)
∣
∣
∣
∣
1+ 1
x

t=0 + ∫ 1+ 1
x

0 u±x(t)zH ′(zt) dt

= H(0) + ∫ 1

0 zH ′(zt)dt + ∫ 1+ 1
x

1 u±x(t)zH ′(zt)dt.

The ﬁrst two terms give H(z) and the last term gives the stated error. □

By combining Lemma 7.2 and (7.3), we see that the residue R 1
2 deﬁned
in (7.2) satisﬁes
 R 1
2 = 16
π2 arcsin (√δ/2)
X 1
2 + O( X 1
2
x
 )
. (7.4)

We still need to understand the growth of the shifted integral. It will turn
out that this is not the primary obstruction to a better result, so we can use
a coarse bound.

Lemma 7.3. With the notation as above, we have that

I 0
±x( 1
4 + ǫ, 1
4 , X, δ) ≪ X 1
4 +ǫx 1
2 +2ǫ.

Proof. We bound the integrand in absolute value, approximate the gamma
functions by Stirling’s formula, and bound the L-functions by the convexity
bound. We also note the classical inequality 1/ζ(1 + ǫ + it) ≪ log t.
We can extract the factor X 1/4+ǫ immediately. Within the integral,
the exponential growth from the gamma functions cancels out. The to-
tal polynomial growth of the gamma functions and L-functions is of size
(1 + |Im s − Im w|)−1/2(1 + |Im s|)1/2+ǫ. Absolute convergence of the integral
follows from U±x(s) ≪ x1/2+ǫ(1+|s|)−(3/2+ǫ) and U±x(w) ≪ xǫ(1+|w|)−(1+ǫ)

as given in (6.1). Combining gives the proof. □

We thus have that

I 0
±x(10, 1
4 , X, δ) = R 1
2 + I 0
±x( 1
4 + ǫ, 1
4 , X, δ),

where R1/2 is the residue in (7.2). Bounds for the residue are given in (7.4)
and the size of the shifted integral is bounded in Lemma 7.3. Assembling
these bounds together proves the following.

Proposition 7.4. For any ﬁxed ǫ > 0 and δ ∈ [0, 1], we have

I 0
±x(10, 1
4 , X, δ) = 16
π2 arcsin(
√δ/2)X 1
2 + O( X 1
2
x
 ) + O(X 1
4 +ǫx 1
2 +ǫ).

ARITHMETIC PROGRESSIONS OF SQUARES 23

7.3. Discrete term. Within the integrals (7.1), the term coming from the
discrete sum in the decomposition (5.1) takes the form

I spec
±x (σs, σw, X, δ)

= 1
(2πi)2
 ∫

(σw)
 ∫

(σs)
 ∑

m̸=0
 (
U±x(s)U±x(w)X sδw2
3s−3w(1 − 2
−2s)

× Γ(s − w − itm)Γ(s − w + itm)
Γ(2s − 2w) log(1 + √
2) (−1)mL(2s, η2m)
ζ (2)(4s)
 )
ds dw,

where initially σw = 1
4 and σs = 10. Since L(2s, η2m) is entire for m ̸= 0,
we have I spec
±x (10, 1
4 , X, δ) = I spec
±x ( 1
4 + ǫ, 1
4 , X, δ).

To justify this contour shift and then bound I spec
±x ( 1
4 + ǫ, 1
4 , X, δ), we require
a technical lemma to handle growth in the m-sum.

Lemma 7.5. On the lines Re z = x ∈ (0, 1
2 ) and Re s = 1
2 + ǫ, we have
∑

m̸=0
 ∣
∣
∣
∣ Γ(z + itm)Γ(z − itm)L(s, η2m)
Γ(2z)
 ∣
∣
∣
∣ ≪ (1 + |z| + |z| 1
2 |s| 1
2 ). (7.5)

Proof. The convexity estimate L(s, η2m) ≪ (1 + |s + itm|) 1
4 (1 + |s − itm|) 1
4
on the line Re s = 1
2 + ǫ and uniform estimates for Stirling’s approximation
in the right half-plane suﬃces to bound the sum in (7.5) by

∑

m̸=0
 |x + iy| 1
2 −2x(1 + |s| 1
2 + |tm| 1
2 )

(|x + iy + itm| · |x + iy − itm|) 1
2 −x exp( − π max(|tm|, |y|) + π|y|
).

Since |x + iy ± it| ≥ max(x, |y ± t|), we have

|x + iy| 1
2 −2x

(|x + iy + itm| · |x + iy − itm|) 1
2 −x

≪ |x + iy| 1
2 −2x min ( 1
|x|1−2x , 1

|y + tm| 1
2 −x|y − tm| 1
2 −x
 ).

The ﬁrst term in the minimum is O(1) and the latter may be bounded in
cases depending on the signs and relative sizes of tm and y.
The contribution in the case 0 < tm < y is

≪ ∑

0<tm<y
 |x + iy| 1
2 −2x(1 + |s| 1
2 + |tm| 1
2 )

|1 + y| 1
2 −x|y − tm| 1
2 −x ≪ 1 + y + y 1
2 |s| 1
2 ,

as can be seen via integral comparison. The contribution from 0 < y < tm
experiences exponential decay and is smaller, no larger than
∑

y<tm
 |x + iy| 1
2 −2x(1 + |s| 1
2 + |tm| 1
2 )

|1 + tm| 1
2 −x|tm − y| 1
2 −x e
−π(tm−y) ≪ 1 + y 1
2 −x + |s| 1
2
(1 + y)x .

The cases in which y and tm diﬀer in sign are analogous. □

24 HULSE, KUAN, LOWRY-DUDA, AND WALKER

The bound in Lemma 7.5 implies that

I spec
±x ( 1
4 + ǫ, 1
4 , X, δ) ≪ X 1
4 +ǫ ∫

( 1
4 )
 ∫
( 1
4 +ǫ)|U±x(s)U±x(w)| (7.6)

×(1 + |s − w| + |s| 1
2 |s − w| 1
2 ) dsdw.

In the region |s| > |w|, the bounds U±x(s) ≪ x1+ǫ/|s|2+ǫ and U±x(w) ≪
xǫ/|w|1+ǫ ensure convergence of the integral. In the region |s| < |w|, we
instead apply U±x(s) ≪ xǫ/|s|1+ǫ and U±x(w) ≪ x1+ǫ/|w|2+ǫ. By applying
these bounds to (7.6), we produce the following proposition.

Proposition 7.6. For any ǫ > 0 and δ ∈ [0, 1], we have

I spec
±x (10, 1
4 , X, δ) ≪ǫ X 1
4 +ǫx1+ǫ.

Remark 7.7. Lemma 7.5 and thereafter Proposition 7.6 may be improved
by applying subconvexity results for the Hecke L-functions L(s, η2m) (such
as [JM05] or [Wu19]). The estimate L(s, η2m) ≪ (1 + |s + itm|)α(1 + |s −
itm|)α on the line Re s = 1
2 + ǫ implies that I spec
±x in Proposition 7.6 is
O(X 1/4+ǫx1/2+2α+ǫ) and that Theorem 7.1 holds in the form

1
8 S(X, δ) = 2
π2 arcsin(
√δ/2)X 1
2 + Oǫ(
X 1
2 − 1
6+8α +ǫ).

Under the Lindel¨of Hypothesis, we have α = 0. The same improvements
hold in the conclusions of Theorems 8.1, 8.3, and 8.4.

8. Further Applications

This section contains three further applications of the meromorphic de-
scription of D(s, w). In Section 8.1, we count primitive APs with bounded
maximum; in Section 8.2, we count primitive APs with individually bounded
ﬁrst and second terms; and in Section 8.3, we count primitive APs whose
ﬁrst two terms have bounded product. Many of the technical details are
similar to those in Section 7, so we describe only those portions that lead to
the main terms and dominant error terms in the asymptotics.

8.1. APs with bounded maximum. We count the number of primitive
APs of squares {h, m, 2m − h} with bounded maximum, In particular, we
produce asymptotics for sums of the form

T (X) := ∑

h≤X
 ∑′

m≤h r1(h)r1(m)r1(2m − h),

in which the prime indicates the restriction to (m, h) = 1. Note that such
APs are arranged with {h, m, 2m − h} decreasing; this does not aﬀect our
results but simpliﬁes notation.
Our primary theorem in this section is the following.

ARITHMETIC PROGRESSIONS OF SQUARES 25

Theorem 8.1. The number of primitive APs of squares with largest term
at most X is
 1
8 T (X) =
 √
2
π2 log(1 + √2)X 1
2 + Oǫ(X 3
8 +ǫ)

for any ǫ > 0.

To prove this theorem, we deﬁne T±x as

T±x(X) := ∑′

m,h≥1 r1(h)r1(m)r1(2m − h)u±x( m
h )u±x( h
X )

and recognize these sums as the integral transforms

T±x(X) = 1
(2πi)2
 ∫
(σw)
 ∫
(σs) D(s, w − s)X wU±x(s)U±x(w) dsdw (8.1)

for suﬃciently large σw and σs. We take σw = 10 and σs = 1
4 to begin.
The proof of Theorem 8.1 is very similar to the proof of Theorem 7.1. In
particular, our analysis once again follows the decomposition of D(s, w) given
in Theorem 5.1. The main term in Theorem 8.1 comes from the m = 0 term
in the expansion (5.1) and the error term results from balancing against
estimates in the m ̸= 0 component from (5.1). We therefore sketch only
these parts of the proof.

Principal term. The contribution of the m = 0 term in the expansion (5.1)
towards T±x(X) takes the form

I 0
±x(σs, σw, X) =

1
(2πi)2
 ∫

(σw)
∫

(σs)

23sζ (2)(2w)L(2w, χ)Γ(s)2X wU±x(s)U±x(w)
ζ (2)(4w) log(1 + √2)Γ(2s) dsdw,

which conveniently decouples into independent s and w integrals.
To handle the s-integral, note by contour shifting the Mellin pair identity

1
2πi
 ∫
(σs)
 23sΓ(s)2

Γ(2s) zs ds
s = 4 arctanh(√1 − 1
2z ),

which holds for Re s > 0 and |z| > 1
2 . It follows by Lemma 7.2 that

1
2πi
 ∫
(σs)
 23sΓ(s)2U±x(s)
Γ(2s) ds = 4 log(1 + √
2) + O(1/x),

in which we’ve used that arctanh(1/
√2) = log(1 + √2).
To estimate the integral in w, we shift the line of integration to σw = 1
4 +ǫ,
passing a simple pole at w = 1
2 and extracting the residue
√2U±x( 1
2 )
π2 X 1
2 = 2
√2
π2 X 1
2 + O( X 1
2
x
 )
.

26 HULSE, KUAN, LOWRY-DUDA, AND WALKER

The shifted w-integral is easily seen to be O(X 1/4+ǫx1/2+ǫ), hence

I 0
±x( 1
4 , 10, X) = 8
√2
π2 log(1 + √2)X 1
2 + O( X 1
2
x + X 1
4 +ǫx 1
2 +ǫ). (8.2)

Discrete term. Within the integrals (8.1), the contribution of the terms
with m ̸= 0 in (5.1) takes the form

I spec
±x (σs, σw, X) = 1
(2πi)2
 ∫
(σw)
 ∫
(σs)
 23s(1 − 2−2w)U±x(w)U±x(s)X w

ζ (2)(4w) log(1 + √2)

× ∑

m̸=0
 Γ(s + itm)Γ(s − itm)
Γ(2s) (−1)
mL(2w, η2m) dsdw,

in which σw = 10 and σs = 1
4 initially. Since L(w, η2m) is entire for m ̸= 0,
we have I spec
±x ( 1
4 , 10, X) = I spec
±x ( 1
4 , 1
4 + ǫ, X). Lemma 7.5 implies that

I spec
±x ( 1
4 , 1
4 + ǫ, X) ≪ X 1
4 +ǫ∫
(σw)
 ∫

(σs) |U±x(s)U±x(w)|(|s| + |s| 1
2 |w| 1
2 )dsdw.

Various estimates for U±x(s) and U±x(w) given by (6.1) then imply

I spec
±x ( 1
4 , 10, X) = O(
X 1
4 +ǫx1+2ǫ)
.

Proof of Theorem 8.1. We have T±x(X) = I 0
±x( 1
4 , 10, X) + I spec
±x ( 1
4 , 10, X).
We have shown that I 0
±x contributes the term (8.2) and I spec
±x contributes
the error O(X 1
4 +ǫx1+2ǫ), so that

T±x(X, Y ) = 8
√2
π2 X 1
2 + O( X 1
2
x + X 1
4 +ǫx1+2ǫ)
.

The theorem now follows by choosing x = X 1/8 and applying the inequalities
T−x(X) ≤ T (X) ≤ T+x(X). □

8.2. APs with individually bounded ﬁrst terms. We count the number
of primitive APs of squares {h, m, 2m − h} such that m ≤ X and h ≤ Y ,
with Y ≤ X. In particular, we produce asymptotics for sums of the form

S(X, Y ) := ∑

m≤X
 ∑′

h≤Y r1(h)r1(m)r1(2m − h),

in which the prime indicates the restriction to (m, h) = 1.

Remark 8.2. The sum S(X, Y )/8 double-counts those APs in which both
h ≤ Y and 2m − h ≤ Y . For example, both {1, 25, 49} and {49, 25, 1} would
be counted if X = Y = 50. We can compensate for this double-counting
by removing those “reversed” APs whose maximum is the ﬁrst element, i.e.
those APs with maximum at most Y . The number of such APs is given
by the quantity T (Y ) of Theorem 8.1, so that (S(X, Y ) − T (Y ))/8 counts
primitive APs with ﬁrst term at most Y and center at most X.

Our primary theorem of this section is the following.

ARITHMETIC PROGRESSIONS OF SQUARES 27

Theorem 8.3. Suppose that Y ≤ X. Then, for any ǫ > 0, the number of
primitive APs of squares {h, m, 2m − h} with h ≤ Y and m ≤ X is

1
8 S(X, Y ) − 1
8 T (Y ) = 1
√
2π2 Y 1
2 log (X/Y ) + c Y 1
2 + Oǫ(X ǫY 3
8 +ǫ),

in which c = √2(1 + 3
2 log 2 − log(1 + √2))/π2.

To prove this theorem, we deﬁne S+x(X, Y ) and S−x(X, Y ) as

S±x(X, Y ) := ∑′

m,h≥1 r1(m)r1(h)r1(2m − h)u±x( m
X )
u±x( h
Y )

= 1
(2πi)2
 ∫

(σw)
 ∫

(σs) D(s, w)U±x(s)U±x(w)X sY wds dw (8.3)

for suﬃciently large σw and σs. We take σw = 1
4 and σs = 10 initially.
Our analysis of S±x(X, Y ) follows the decomposition of D(s, w) given in
Theorem 5.1. As in Theorems 7.1 and 8.1, the main term comes from the
m = 0 term in (5.1) and the m ̸= 0 term contributes error terms used for
optimizing the parameter x.

Principal term. Simplifying the m = 0 term of (5.1) as in Section 7.2, we
see that its contribution to S±x(X, Y ) takes the form

I 0
±x(σs, σw, X, Y ) = 1
(2πi)2
 ∫
(σw)
 ∫
(σs)
 (
U±x(s)U±x(w)X sY w

× 23sζ (2)(2s + 2w)L(2s + 2w, χ)
ζ (2)(4s + 4w) log(1 + √2)Γ(2s) Γ(s)
2)
ds dw,

where initially σw = 1
4 and σs = 10. To extract the main term, we will

(1) change variables to disentangle s and w in the leading poles,
(2) shift the line of s integration to the left, passing double poles, and
(3) shift the line of w integration within the residues extracted from (2)
to the right, passing triple poles.

The shifted integrals in the ﬁrst term do not contribute leading terms in the
ﬁnal asymptotic, so we only consider the residues.
Changing variables s ↦→ s − w shows that

I 0
±x(10, 1
4 , X, Y ) = 1
(2πi)2
 ∫

( 1
4 )
 ∫

(10+ 1
4 )
 (U±x(s − w)U±x(w)X s−wY w

× 23s−3wΓ(s − w)2ζ (2)(2s)L(2s, χ)
ζ (2)(4s) log(1 + √2)Γ(2s − 2w)
 )
ds dw.

This integrand matches the integrand within I 0
±x from Section 7.1, except
that this has U±x(s − w)X s−w instead of U±x(s)X s. Shifting the line of

28 HULSE, KUAN, LOWRY-DUDA, AND WALKER

s-integration to σs = 1
4 + ǫ passes a simple pole with residue

4X 1
2
2πi
 ∫
( 1
4 )
 Γ( 1
2 − w)2U±x( 1
2 − w)U±x(w)
π2Γ(1 − 2w)
 ( Y
8X
 )w dw.

As Y < X, this residue is minimized by shifting w to the right. We shift
w to σw = 1 − ǫ, extracting a single residue from a pole of order two at
w = 1
2 . The negation of this residue takes the form

4
√2
π2 log(X/Y )Y 1
2 + 8
√2 + 12
√2 log 2
π2 Y 1
2 +O( log(X/Y )Y 1
2 + Y 1
2
x
 )
. (8.4)

The main term above creates the main term in our ﬁnal asymptotic.

Discrete term. Within the integrals (8.3), the term coming from the m ̸= 0
part of the decomposition (5.1) takes the form

I spec
±x (σs, σw, X, Y )

= 1
(2πi)2
 ∫
(σw)
 ∫
(σs)
 ∑

m̸=0
 (
U±x(s)U±x(w)X sY w2
3s(1 − 2
−2s−2w)

× Γ(s − itm)Γ(s + itm)
Γ(2s) log(1 + √2) (−1)mL(2s + 2w, η2m)
ζ (2)(4s + 4w)
 )ds dw,

where initially σw = 1
4 and σs = 10. Since L(s, η2m) is entire for m ̸= 0, we
have I spec
±x (10, 1
4 , X, Y ) = I spec
±x (ǫ, 1
4 , X, Y ). Lemma 7.5 then implies that

I spec
±x (ǫ, 1
4 , X, Y ) ≪ X ǫY 1
4 ∫

( 1
4 )
 ∫

(ǫ) |U±x(s)U±x(w)|(|s| + |s| 1
2 |s + w| 1
2 ) dsdw,

hence I spec
±x (ǫ, 1
4 , X, Y ) ≪ X ǫY 1
4 x1+ǫ using familiar bounds for U±x.

Proof of Theorem 8.3. We have the equality

S±x(X, Y ) = I 0
±x(10, 1
4 , X, Y ) + I spec
±x (10, 1
4 , X, Y )

We have shown that I 0
±x contributes the term (8.4) and I spec
±x contributes
the error O(Y 1
4 X ǫx1+ǫ), so that

S±x(X, Y ) = 4
√2
π2 log(X/Y )Y 1
2 + 8
√2 + 12
√2 log 2
π2 Y 1
2

+ O( log(X/Y )Y 1
2 + Y 1
2
x
 ) + O(Y 1
4 X ǫx1+ǫ)

The theorem follows by choosing x = Y 1/8, noting S−x(X, Y ) ≤ S(X, Y ) ≤
S+x(X, Y ), and subtracting the estimate for T (Y ) given in Theorem 8.1. □

ARITHMETIC PROGRESSIONS OF SQUARES 29

8.3. APs with bounded products of ﬁrst two terms. Finally, we use
D(s, w) to count the number of primitive APs of squares {h, m, 2m−h} such
that hm ≤ X by producing asymptotics for the sum

S(X) := ∑′

hm≤X 2
h≤m
 r1(h)r1(m)r1(2m − h),

in which the prime denotes the restriction (m, h) = 1.
Our primary result of this section is the following theorem.

Theorem 8.4. For any ǫ > 0, the number of primitive APs of squares
{h, m, 2m − h} with hm ≤ X is

1
8 S(X) = 2
√2
π2 2F1( 1
4 , 1
2 , 5
4 , 1
2 )X 1
2 + Oǫ(
X 3
8 +ǫ)
.

To prove this theorem, we deﬁne S+x(X) and S−x(X) as

S±x(X) := ∑′

m,h≥1 r1(m)r1(h)r1(2m − h)u±x( h
m )u±x( hm
X 2 ) (8.5)

= 1
(2πi)2
 ∫

(σs)
 ∫
(σw) D(s − w, s + w)U±x(s)U±x(w)X 2s dw ds

for suﬃciently large σs. We take σs = 10 and σw = 1
8 initially.
The proof of Theorem 8.4 again resembles the proof of Theorem 7.1. As
in our previous applications, we break our proof into two parts, following
the decomposition into m = 0 and m ̸= 0 from Theorem 5.1.

Principal term. The main term in the integrals (8.5) comes from the m =
0 term in the decomposition (5.1) and takes the form

I 0
±x(σs, σw, X) = 1
(2πi)2
 ∫
(σs)
 ∫

(σw)
 23s−3wζ (2)(4s)L(4s, χ)X 2s

ζ (2)(8s) log(1 + √2)Γ(2s − 2w)

× Γ(s − w)
2U±x(s)U±x(w) dwds,

where initially σs = 10. Shifting the line of s-integration to σs = 1
8 +ǫ passes
a simple pole at s = 1
4 and extracts a residue of the form

X 1
2
2πi
 ∫

( 1
8 )
 Γ( 1
4 − w)2U±x( 1
4 )U±x(w)

2
3w− 1
4 π2Γ( 1
2 − 2w) dw, (8.6)

To determine the growth of this integral, we apply the integral identity

1
2πi
 ∫
( 1
8 )
 Γ( 1
4 − w)2

wΓ( 1
2 − 2w) zw dw = 8z1/4 2F1( 1
4 , 1
2 , 5
4 , 4z), (8.7)

valid for |z| < 1
4 , in the case z = 1
8 . To establish (8.7), we note by Stirling’s
approximation that the integrand is O(|4z|Re w|w|−3/2). The assumption
|z| < 1
4 implies that the contour Re w = 1
8 may be shifted far to the right,

30 HULSE, KUAN, LOWRY-DUDA, AND WALKER

where it vanishes in the limit. This shift extracts residues from the integral
at points w = 1
4 + ℓ, for integers ℓ ≥ 0, and the sum of these residues equals

∞∑

ℓ=0 Res
w= 1
4 +ℓ
 Γ( 1
4 − w)2

wΓ( 1
2 − 2w) zw =
 ∞∑

ℓ=0 Res
w= 1
4 +ℓ
 (4z)w√2πΓ( 1
4 − w)
wΓ( 3
4 − w)

= √2π(4z) 1
4
 ∞∑

ℓ=0
 (−4z)ℓΓ(ℓ + 1
4 )
Γ(ℓ + 5
4 )Γ( 1
2 − ℓ)ℓ! = 2z 1
4
√
π
 ∞∑

ℓ=0
 (4z)ℓΓ(ℓ + 1
4 )Γ(ℓ + 1
2 )
Γ(ℓ + 5
4 )ℓ!

= 2z 1
4
√π Γ( 1
4 )Γ( 1
2 )
Γ( 5
4 ) 2F1( 5
4 , 1
2 , 1
4 , 4z) = 8z 1
4 2F1( 5
4 , 1
2 , 1
4 , 4z),

in which we’ve used the gamma duplication formula and the reﬂection for-
mula Γ( 1
2 − z)Γ( 1
2 + z) = π sec(πz) to simplify.
Via Lemma 7.2 and (8.7), the residue integral (8.6) is

16
√2
π2 2F1( 1
4 , 1
2 , 5
4 , 1
2 )X 1
2 + O( X 1
2
x
 ). (8.8)

The shifted double integral I 0
±x( 1
8 + ǫ, 1
8 , X) is O(X 1
4 +2ǫxǫ), which will be
non-dominant.

Discrete term. Within the integrals (8.5), the term coming from the m ̸= 0
term in the decomposition (5.1) takes the form

I spec
±x (σs, σw, X) = 1
(2πi)2
 ∫
(σs)
∫

(σw)
 ∑

m̸=0
 (−1)m23s−3w(1 − 2−4s)L(4s, η2m)
ζ (2)(8s) log(1 + √2)Γ(2s − 2w)

× Γ(s − w + itm)Γ(s − w − itm)U±x(s)U±x(w)X 2s dwds,

with σs = 10 and σw = 1
8 . Since L(s, η2m) is entire for m ̸= 0, we have
I spec
±x (10, 1
8 , X) = I spec
±x ( 1
8 + ǫ, 1
8 , X). Our analysis now follows along the lines
of Section 7.3 to prove that I spec
±x ( 1
8 + ǫ, 1
8 , X) = O(X 1
4 +2ǫx1+2ǫ).

Proof of Theorem 8.4. We have the equality.

S±x(X) = I 0
±x(10, 1
8 , X) + I spec
±x (10, 1
8 , X).

We have shown that I 0
±x contributes (8.8), while I spec
±x is O(X 1
4 +2ǫx1+2ǫ).
Together, these show that

S±x(X) = 16
√2
π2 2F1( 1
4 , 1
2 , 5
4 , 1
2 )X 1
2 + O( X 1
2
x
 ) + Oǫ(X 1
4 +2ǫx1+2ǫ).

The theorem follows from the choice x = X 1/8 and the inequalities S−
x (X) ≤
S(X) ≤ S+
x (X). □

ARITHMETIC PROGRESSIONS OF SQUARES 31

References

[Blo17] Valentin Blomer. On triple correlations of divisor functions.
Bulletin of the London Mathematical Society, 49(1):10–22,
2017.
[Bom05] Enrico Bombieri. The Rosetta Stone of L-functions. In Per-
spectives in analysis, volume 27 of Math. Phys. Stud., pages
1–15. Springer, Berlin, 2005.
[Bum97] Daniel Bump. Automorphic forms and representations, vol-
ume 55 of Cambridge Studies in Advanced Mathematics. Cam-
bridge University Press, Cambridge, 1997.
[Dic13] Leonard Eugene Dickson. History of the theory of numbers:
Diophantine Analysis, volume 2. Courier Corporation, 2013.
[Duk03] W Duke. Rational points on the sphere. In Number Theory
and Modular Forms, pages 235–239. Springer, 2003.
[GH85] D. Goldfeld and J. Hoﬀstein. Eisenstein series of 1
2 -integral
weight and the mean value of real Dirichlet L-series. Inven-
tiones Mathematicae, 80:185–208, 1985.
[Gol15] Dorian Goldfeld. Automorphic forms and L-functions for the
group GL(n, R), volume 99 of Cambridge Studies in Advanced
Mathematics. Cambridge University Press, Cambridge, 2015.
With an appendix by Kevin A. Broughan, Paperback edition
of the 2006 original [ MR2254662].
[GR15] I. S. Gradshteyn and I. M. Ryzhik. Table of integrals, series,
and products. Elsevier/Academic Press, Amsterdam, eighth
edition, 2015. Translated from the Russian, Translation edited
and with a preface by Daniel Zwillinger and Victor Moll, Re-
vised from the seventh edition [MR2360010].
[HH16] Jeﬀ Hoﬀstein and Thomas A. Hulse. Multiple Dirichlet se-
ries and shifted convolutions. J. Number Theory, 161:457–533,
2016. With an appendix by Andre Reznikov.
[HKLDW18] Thomas A. Hulse, Chan Ieong Kuan, David Lowry-Duda, and
Alexander Walker. Second moments in the generalized Gauss
circle problem. Forum of Mathematics, Sigma, 2018. Ac-
cepted, In Press; arXiv:1703.10347.
[HKLDW19] Thomas Hulse, Chan Ieong Kuan, David Lowry-Duda, and
Alexander Walker. Triple correlation sums of coeﬃcients of
cusp forms, 2019.
[Iwa97] Henryk Iwaniec. Topics in classical automorphic forms, vol-
ume 17 of Graduate Studies in Mathematics. American Math-
ematical Society, Providence, RI, 1997.
[JM05] Matti Jutila and Yoichi Motohashi. Uniform bound for Hecke
L-functions. Acta Math., 195:61–115, 2005.

32 HULSE, KUAN, LOWRY-DUDA, AND WALKER

[Kob93] Neal Koblitz. Introduction to elliptic curves and mod-
ular forms, volume 97 of Graduate Texts in Mathemat-
ics. Springer-Verlag, New York, second edition, 1993.
http://dx.doi.org/10.1007/978-1-4612-0909-6.
[KS02] Henry H. Kim and Freydoon Shahidi. Cuspidality of symmet-
ric powers with applications. Duke Math. J., 112(1):177–197,
2002.
[LD17] David Lowry-Duda. On Some Variants of the Gauss
Circle Problem. PhD thesis, Brown University, 5 2017.
https://arxiv.org/abs/1704.02376.
[LY02] Jianya Liu and Yangbo Ye. Subconvexity for Rankin-Selberg
L-functions of Maass forms. Geom. Funct. Anal., 12(6):1296–
1323, 2002.
[Mic07] Philippe Michel. Analytic number theory and families of auto-
morphic L-functions. In Automorphic forms and applications,
volume 12 of IAS/Park City Math. Ser., pages 181–295. Amer.
Math. Soc., Providence, RI, 2007.
[Nel19] Paul D. Nelson. Subconvex equidistribution of cusp forms: re-
duction to Eisenstein observables. Duke Math. J., 168(9):1665–
1722, 2019.
[Nel21] Paul D. Nelson. The spectral decomposition of |θ|2. Math. Z.,
298(3-4):1425–1447, 2021.
[S+85] Goro Shimura et al. On eisenstein series of half-integral weight.
Duke Mathematical Journal, 52(2):281–314, 1985.
[Sar01] Peter Sarnak. Estimates for rankin–selberg l-functions and
quantum unique ergodicity. Journal of Functional Analysis,
184(2):419–453, 2001.
[Shi73] Goro Shimura. On modular forms of half integral weight. The
Annals of Mathematics, 97(3):440–481, 1973.
[Sie80] C.L. Siegel. Advanced Analytic Number Theory. Studies in
mathematics / Tata institute of fundamental research. Tata
Inst. of Fundamental Research, 1980.
[TB18] Ramin Takloo-Bighash. A Pythagorean introduction to number
theory. Undergraduate Texts in Mathematics. Springer, Cham,
2018. Right triangles, sums of squares, and arithmetic.
[Wu19] Han Wu. Burgess-like subconvexity for GL1. Compositio Math-
ematica, 155(8):1457–1499, 2019.
