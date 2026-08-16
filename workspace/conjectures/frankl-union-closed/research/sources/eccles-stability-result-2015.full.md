<!-- source: https://arxiv.org/pdf/1210.2044 | converted from PDF -->

arXiv:1210.2044v1  [math.CA]  7 Oct 2012
On a Chain of Harmonic and Monogenic Potentials in
Euclidean Half–space

F. Brackx, H. De Bie, H. De Schepper

Cliﬀord Research Group, Department of Mathematical Analysis,
Faculty of Engineering and Architecture, Ghent University
Building S22, Galglaan 2, B-9000 Gent, Belgium

Abstract

In the framework of Cliﬀord analysis, a chain of harmonic and monogenic potentials is con-
structed in the upper half of Euclidean space Rm+1, including a higher dimensional general-
ization of the complex logarithmic function. Their distributional limits at the boundary Rm

turn out to be well-known distributions such as the Dirac distribution, the Hilbert kernel,
the fundamental solution of the Laplace and Dirac operators, the square root of the negative
Laplace operator, and the like. It is shown how each of those potentials may be recovered
from an adjacent kernel in the chain by an appropriate convolution with such a distributional
limit.

1 Introduction

Consider in the upper half C+ = {z = x + iy ∈ C : y > 0} of the complex plane, the logarithmic
function ln z = ln |z| + i arg z, Im z > 0

with arg z = π
2 − arctan x
y , y > 0

It is quite an interesting function; let us have a closer look at its properties.

(i) The function ln z is holomorphic in C+, i.e. it is a null solution of the Cauchy–Riemann
operator
 D = 1
2 (∂x + i∂y)

(ii) Its real and imaginary parts are conjugate harmonic functions in C+ and the real part ln |z| =
ln r = ln √
x2 + y2 is, up to a constant, the fundamental solution of the two–dimensional
Laplace operator ∆2 = ∂2
xx + ∂2
yy = 4DD

where D = 1
2 (∂x − i∂y) is the complex conjugate Cauchy–Riemann operator; in fact, we
have, in distributional sense,
 ∆2
 ( 1
2π ln |z|) = δ(z)

with δ(z) the Dirac or delta distribution in C.

1

(iii) As a holomorphic function, ln z has a complex derivative in C+, given by

d
dz ln z = 1
z

meaning that ln z is a holomorphic primitive (or potential) in C+, with respect to the complex
derivative d
dz , of the function 1
z which, in its turn, is, up to a constant, the fundamental
solution of the Cauchy–Riemann operator; in fact we have, in distributional sense,

D ( 1
π 1
z
 ) = δ(z)

Note that the complex derivative operator d
dz is nothing else but the conjugate Cauchy–
Riemann operator D, and there also holds in C+

d
dz ln z = D ln z = ∂x ln z = (−i∂y) ln z = 1
z

(iv) The conjugate harmonic real and imaginary parts ln r and arg z satisfy the Cauchy–Riemann
system 



 ∂x ln r = ∂y arg z = x
x2+y2 = Re ( 1
z )

∂y ln r = −∂x arg z = y
x2+y2 = −Im ( 1
z )

where at the right hand sides one recognizes the Poisson kernel P (x, y) = y
x2+y2 and its
harmonic conjugate Q(x, y) = x
x2+y2 in C+; it follows that

D(2 ln r) = 1
z

and D(2i arg z) = 1
z
meaning that the functions 2 ln r and 2i arg z are conjugate harmonic potentials in C+, with
respect to the operator D = d
dz , of the Cauchy kernel 1
z .

(v) The distributional limits for y → 0+ of the Cauchy kernel 1
z and its holomorphic potential
ln z, are given by
 lim
y→0+ 1
z = lim
y→0+ x
x2 + y2 − i lim
y→0+ y
x2 + y2 = Pv 1
x − iπδ(x)

with Pv 1
x the ”principal value” distribution on the real axis, and

lim
y→0+ ln z = lim
y→0+ ln |z| + i lim
y→0+ arg z = ln |x| + iπY (−x)

with Y (x) the Heaviside step function. These distributional boundary values ﬁt into the
following two commutative schemes

ln r ∂x−−−→ x
x2+y2

y→0+ ↓ ↓

ln |x| ∂x−−−→ Pv 1
x
 and − arg z ∂x−−−→ y
x2+y2

y→0+ ↓ ↓

−πY (−x) ∂x−−−→ π δ(x)

2

and moreover they form Hilbert pairs, the Hilbert transform on the real axis being given by

H[T ] = H ∗ T = 1
π Pv 1
x ∗ T,

since we have indeed
 H [πδ(x)] = Pv 1
x , H [
Pv 1
x
 ] = πδ(x)

and H [ln |x|] = π Y (−x), H [π Y (−x)] = ln |x|

The aim of this paper is to construct a generalization of this logarithmic potential function
in higher dimension, more speciﬁcally in the framework of Cliﬀord analysis, where the functions
under consideration take their values in the universal Cliﬀord algebra R0,m+1 constructed over
Euclidean space Rm+1 equipped with a quadratic form of signature (0, m + 1). The concept of a
higher dimensional holomorphic function, mostly called monogenic function, is expressed by means
of a generalized Cauchy–Riemann operator, which is a combination of the derivative with respect
to one of the variables, say x0, and the so–called Dirac operator ∂ in the remaining variables
(x1, x2, . . . , xm). The generalized Cauchy–Riemann operator and its Cliﬀord algebra conjugate
linearize the Laplace operator, whence Cliﬀord analysis is entitled to be qualiﬁed as a reﬁnement
of harmonic analysis.

It is a remarkable fact that the thus constructed monogenic logarithmic function in upper half–
space Rm+1
+ shows the same, above mentioned, ﬁve properties as in the complex plane. Starting
point of our construction is the fundamental solution of the generalized Cauchy–Riemann operator,
also called Cauchy kernel, and its relation to the Poisson kernel and its harmonic conjugate in Rm+1
+ .
We then proceed by induction in two directions, downstream by diﬀerentiation and upstream by
primitivation, yielding an doubly inﬁnite chain of monogenic, and thus harmonic, potentials. This
chain mimics the well–known sequence of holomorphic potentials in C+ (see e.g. [13]):

1
k! zk [
ln z − (1 + 1
2 + . . . + 1
k )
] → . . . → z(ln z−1) → ln z
 d
dz−→ 1
z → − 1
z2 → . . . → (−1)
k−1 (k − 1)!
zk

Identifying the boundary of upper half–space with Rm ∼= {(x0, x) ∈ Rm+1 : x0 = 0}, the distribu-
tional limits for x0 → 0+ of those potentials are computed; they divide into two classes which are
linked by the Hilbert transform and encompass well–known distributions in Rm such as the Dirac
or delta distribution, the Hilbert kernel, the fundamental solutions of the Dirac and the Laplace
operators, the square root of the negative Laplacian, and the like. It is also shown how each of
the monogenic potentials may be recovered from an adjacent kernel in the chain by an appropriate
convolution with such a boundary distribution.

The organization of the paper is as follows. To make the paper self–contained we recall in
Section 2 the basics of Cliﬀord algebra and Cliﬀord analysis. In Section 3 we construct a conjugate
harmonic in upper half–space Rm+1
+ to the fundamental solution of the (m+1)–dimensional Laplace
operator, which is essential to obtaining the desired monogenic logarithmic function in Rm+1
+ . In
Section 4 we study the so–called downstream potentials obtained under the action of the Cliﬀord
algebra conjugate of the generalized Cauchy–Riemann operator. Finally, in Section 5, we study the
monogenic logarithmic function in Rm+1
+ and we construct, by an appropriate form of primitivation,
the sequence of upstream potentials. Section 6 is concluding.

3

2 Basics of Cliﬀord analysis

Cliﬀord analysis (see e.g. [3]) is a function theory which oﬀers a natural and elegant generalization
to higher dimension of holomorphic functions in the complex plane and reﬁnes harmonic analysis.
Let (e0, e1, . . . , em) be the canonical orthonormal basis of Euclidean space Rm+1 equipped with a
quadratic form of signature (0, m + 1). Then the non–commutative multiplication in the universal
real Cliﬀord algebra R0,m+1 is governed by the rule

eαeβ + eβeα = −2δαβ, α, β = 0, 1, . . . , m

whence R0,m+1 is generated additively by the elements eA = ej1 . . . ejh , where A = {j1, . . . , jh} ⊂
{0, . . . , m}, with 0 ≤ j1 < j2 < · · · < jh ≤ m, and e∅ = 1. For an account on Cliﬀord algebra we
refer to e.g. [12].

We identify the point (x0, x1, . . . , xm) ∈ Rm+1 with the Cliﬀord–vector variable

x = x0e0 + x1e1 + · · · xmem = x0e0 + x

and the point (x1, . . . , xm) ∈ Rm with the Cliﬀord–vector variable x. Introducing spherical co–
ordinates x = rω, r = |x|, ω ∈ Sm−1, gives rise to the Cliﬀord–vector valued locally integrable
function ω, which is to be seen as the higher dimensional analogue of the signum–distribution on
the real line; we will encounter ω as one of the distributions discussed below.

At the heart of Cliﬀord analysis lies the so–called Dirac operator

∂ = ∂x0e0 + ∂x1e1 + · · · ∂xmem = ∂x0e0 + ∂

which squares to the negative Laplace operator: ∂2 = −∆m+1, while also ∂2 = −∆m. Due to the
non–commutative character of the multiplication in the Cliﬀord algebra, the Dirac operator may
act from the left or from the right on a Cliﬀord algebra valued function with, in general, diﬀerent
results. The (left and right) fundamental solution of the Dirac operator ∂ is given by

Em+1(x) = − 1
σm+1
 x
|x|m+1

where σm+1 = 2π m+1
2
Γ( m+1
2 ) stands for the area of the unit sphere Sm in Rm+1. We also introduce the
generalized Cauchy–Riemann operator

D = 1
2 e0∂ = 1
2 (∂x0 + e0∂)

and its Cliﬀord algebra conjugate D = 1
2 (∂x0 − e0∂). As is the case in the complex plane, both
operators decompose the Laplace operator in Rm+1: DD = DD = 1
4 ∆m+1.

A continuously diﬀerentiable function F (x), deﬁned in an open region Ω ⊂ Rm+1 and taking its
values in the Cliﬀord algebra R0,m+1, is called (left–)monogenic if it satisﬁes the equation DF = 0
in Ω, which is equivalent with ∂F = 0.

Singling out the basis vector e0, we can decompose the real Cliﬀord algebra R0,m+1 in terms
of the Cliﬀord algebra R0,m as R0,m+1 = R0,m ⊕ e0R0,m. Similarly we decompose the functions
considered as F (x0, x) = F1(x0, x) + e0F2(x0, x)

4

where F1 and F2 take their values in the Cliﬀord algebra R0,m; mimicking functions of a complex
variable, we will call F1 the real part and F2 the imaginary part of the function F .

We will extensively use two families of distributions in Rm, which have been thoroughly studied
in [5, 6, 2]. The ﬁrst family T = {Tλ : λ ∈ C} is very classical. It consists of the radial distributions

Tλ = Fp rλ = Fp (x
2
1 + . . . + x
2
m) λ
2

their action on a test function φ ∈ S(Rm) being given by

⟨Tλ, φ⟩ = σm⟨Fp rµ
+, Σ(0)[φ]⟩

with µ = λ + m − 1. In the above expressions Fp rµ
+ is the classical ﬁnite part distribution on the
real r-axis and Σ(0) is the scalar valued generalized spherical mean, deﬁned on scalar valued test
functions φ(x) by
 Σ(0)[φ] = 1
σm
 ∫

Sm−1 φ(x) dS(ω)

This family T contains a.o. the fundamental solution of the Laplace operator. As convolution
operators they give rise to the traditional Riesz potentials (see e.g. [11]). The second family
U = {Uλ : λ ∈ C} of distributions arises in a natural way by the action of the Dirac operator ∂ on
T . The Uλ–distributions thus are typical Cliﬀord analysis objects: they are Cliﬀord–vector valued,
and they also arise as products of Tλ–distributions with the distribution ω = x
|x| , mentioned above.
The action of Uλ on a test function φ ∈ S(Rm) is given by

⟨Uλ, φ⟩ = σm⟨Fp rµ
+, Σ(1)[φ]⟩

with µ = λ+m−1, and where the Cliﬀord–vector valued generalized spherical mean Σ(1) is deﬁned
on scalar valued test functions φ(x) by

Σ(1)[φ] = 1
σm
 ∫

Sm−1 ω φ(x) dS(ω)

Typical example in the U–family is the fundamental solution of the Dirac operator.

The normalized distributions T ∗
λ and U ∗
λ arise when the singularities of Tλ and Uλ are removed
by dividing them by an appropriate Gamma-function, showing the same simple poles. The T ∗
λ –
distributions are deﬁned by




 T ∗
λ = π λ+m
2 Tλ
Γ ( λ+m
2 ) , λ ̸= −m − 2l

T ∗
−m−2l = π m
2 −l

22lΓ ( m
2 + l) (−∆)
lδ(x), l ∈ N0

while the Cliﬀord–vector valued distributions U ∗
λ are deﬁned by




 U ∗
λ = π λ+m+1
2 Uλ
Γ ( λ+m+1
2 ) , λ ̸= −m − 2l − 1

U ∗
−m−2l−1 = − π m
2 −l

22l+1 Γ ( m
2 + l + 1) ∂2l+1δ(x), l ∈ N0

The normalized distributions T ∗
λ and U ∗
λ are holomorphic mappings from λ ∈ C to the space
S′(Rm) of tempered distributions. As already mentioned they are intertwined by the action of the
Dirac operator. They enjoy the following properties: for all λ ∈ C one has

5

(i) x T ∗
λ = λ+m
2π U ∗
λ+1; x U ∗
λ = U ∗
λ x = −T ∗
λ+1

(ii) ∂ T ∗
λ = λ U ∗
λ−1; ∂ U ∗
λ = U ∗
λ ∂ = −2π T ∗
λ−1

(iii) ∆mT ∗
λ = 2πλT ∗
λ−2 ; ∆mU ∗
λ = 2π(λ − 1)U ∗
λ−2

(iv) r2T ∗
λ = λ+m
2π T ∗
λ+2; r2U ∗
λ = λ+m+1
2π U ∗
λ+2

Of particular importance for the sequel are the convolution formulae for the T ∗
λ – and U ∗
λ–
distributions; we list them in the following proposition and refer the reader to [2] for more details.

Proposition 2.1.

(i) For all (α, β) ∈ C × C such that α ̸= 2j, j ∈ N0, β ̸= 2k, k ∈ N0 and α + β + m ̸= 2l, l ∈ N0
the convolution T ∗
α ∗ T ∗
β is the tempered distribution given by

T ∗
α ∗ T ∗
β = cm(α, β) T ∗
α+β+m

with
 cm(α, β) = π m
2 Γ (− α+β+m
2 )

Γ (
− α
2 ) Γ (
− β
2 )

(ii) For (α, β) ∈ C × C such that α ̸= 2j + 1, β ̸= 2k, α + β ̸= −m + 2l + 1, j, k, l ∈ N0 one has

U ∗
α ∗ T ∗
β = T ∗
β ∗ U ∗
α = cm(α − 1, β) U ∗
α+β+m

(iii) For (α, β) ∈ C × C such that α ̸= 2j + 1, β ̸= 2k + 1, α + β ̸= −m + 2l, j, k, l ∈ N0 one has

U ∗
α ∗ U ∗
β = U ∗
β ∗ U ∗
α = π m
2 +1 Γ(− α+β+m
2 )

Γ( −α+1
2 )Γ( −β+1
2 ) T ∗
α+β+m

Remark 2.1. The action of a Cliﬀord algebra valued distribution on a ditto test function is
assumed to be carried out componentwise, the respective basis vectors being multiplied in the Cliﬀord
algebra.

Remark 2.2. In general the convolution of Cliﬀord algebra valued distributions is not commutative.
However, as is seen from formula (iii) in Proposition 2.1, the convolution of two distributions from
the U–family is indeed commutative. We will frequently use this property in the sequel. Convolution
by distributions from the T –family is intrinsically commutative since they are scalar valued.

Remark 2.3. In general the convolution of distributions is not associative. However, as is seen
from the formulae in Proposition 2.1, the convolution of distributions from the T – and U–families
is associative. Also this property will be frequently used this in the sequel.

3 A conjugate harmonic to Green’s function

The fundamental solution of the Laplace operator ∆m+1 in Rm+1, sometimes called Green’s func-
tion, and here denoted, for reasons which will become clear afterwards, by 1
2 A0(x0, x), is given
by 1
2 A0(x0, x) = − 1
m − 1 1
σm+1
 1
|x|m−1 (3.1)

6

Considering the function A0(x0, x) as a harmonic function in the upper half–space Rm+1
+ , our aim
now is to construct its conjugate harmonic in Rm+1
+ in the sense of [3], in this way elaborating
further on an earlier result of [14]. This means that we have to look for a harmonic function
B0(x0, x) in Rm+1
+ such that
 C0(x0, x) = 1
2 A0(x0, x) + 1
2 e0 B0(x0, x)

is monogenic in Rm+1
+ w.r.t. the generalized Cauchy–Riemann operator D. Expressing the mono-
genicity of C0 in Rm+1
+ leads to the system
{ ∂x0A0 + ∂B0 = 0

∂x0B0 + ∂A0 = 0 (3.2)

which clearly mimics the Cauchy–Riemann system in the complex plane. Taking into account the
explicit expression (3.1) of A0(x0, x), the system (3.2) reduces to




 ∂B0(x0, x) = − 2
σm+1
 x0
|x|m+1 = −P (x0, x)

∂x0B0(x0, x) = − 2
σm+1
 x
|x|m+1 = Q(x0, x) (3.3)

where P and Q stand for the Poisson kernel and its conjugate in Rm+1
+ (see also Section 4). From
the second condition in (3.3) its follows that, for an arbitrary, but ﬁxed, x
∗
0,

B(x0, x) = 2
σm+1
 x
|x|m Fm
 ( |x|
x0
 ) − 2
σm+1
 x
|x|m Fm
 ( |x|
x∗
0
 ) + W (x)

where we have put

Fm(v) = ∫ v

0
 ηm−1

(1 + η2) m+1
2 dη = vm

m 2F1
 ( m
2 , m + 1
2 ; m
2 + 1; −v2)

with 2F1 a standard hypergeometric function (see e.g. [9]).

From the ﬁrst condition in (3.3) it then follows that the function W (x) should satisfy the equation

∂W (x) = − (∂x0A0)x∗
0 = − 2
σm+1
 x
∗
0
|x∗
0e0 + x|m+1

and a straightforward calculation shows that the function

W (x) = 2
σm+1
 x
|x|m Fm
 ( |x|
x∗
0
 )

does the job. A conjugate harmonic to A0 in Rm+1
+ is thus given by

B0(x0, x) = 2
σm+1
 x
|x|m Fm
 ( |x|
x0
 ) (3.4)

or
 B0(x0, x) = 2
m 1
σm+1
 x
xm
0 2F1
 ( m
2 , m + 1
2 ; m
2 + 1; − |x|2

x2
0
 ) (3.5)

7

Expression (3.5) clearly shows that B0(x0, x) is well–deﬁned for x = 0, with

lim
x→0 B0(x0, x) = 0, x0 > 0

Taking into account that

Fm(+∞) = ∫ +∞

0
 ηm−1

(1 + η2) m+1
2 dη = √π
2 Γ ( m
2 )

Γ ( m+1
2 )

expression (3.4) leads to the following distributional limit

b0(x) = lim
x0→0+ B0(x0, x) = 1
σm
 x
|x|m = 1
π 1
σm U ∗
−m+1 (3.6)

in which one recognizes, up to a minus sign, the fundamental solution Em(x) of the Dirac operator
∂ in Rm:
 −b0(x) = 1
σm
 x
|x|m = − 1
π 1
σm U ∗
−m+1 = Em(x)

This distribution Em(x) may act as a convolution kernel for the so–called T –operator, which is a
convolution operator acting on Cliﬀord algebra valued Schwartz–functions f ∈ S(Rm) or on ditto
tempered distributions as T [f ] = Em ∗ f = −b0 ∗ f

Seen the fact that Em(x) is the fundamental solution of the Dirac operator ∂, this T –operator is
an inverse to this Dirac operator:
 ∂ T [f ] = f, f ∈ S(Rm)

The Green function A0(x0, x) itself shows the following distributional limit:

a0(x) = lim
x0→0+ A0(x0, x) = − 2
m − 1 1
σm+1 Fp 1
|x|m−1 = − 2
m − 1 1
σm+1 T ∗
−m+1 (3.7)

Using this distribution, up to a minus sign, as a convolution kernel, gives rise to the convolution
operator (−∆)
− 1
2 , acting on Schwartz–functions or tempered distributions by, see e.g. [11],

(−∆)
− 1
2 [f ] = 2
m − 1 1
σm+1 T ∗
−m+1 ∗ f = −a0 ∗ f

The functions A0(x0, x) and B(x0, x) being conjugate harmonic in Rm+1
+ , we expect their distri-
butional boundary values a0(x) and b0(x) to be intimately related. This is indeed the case, as will
be shown in Section 5.

4 Downstream potentials

4.1 The Cauchy kernel as a potential

As is well–known, the Cauchy kernel of Cliﬀord analysis, i.e. the fundamental solution of the
generalized Cauchy–Riemann operator D,

C−1(x0, x) = 1
σm+1
 xe0
|x|m+1 = 1
σm+1
 x0 − e0x
|x|m+1

8

may be decomposed in terms of the Poisson kernels in Rm+1
+ :

C−1(x0, x) = 1
2 A−1(x0, x) + 1
2 e0 B−1(x0, x)

where, also mentioning the traditional notations, for x0 > 0,




 A−1(x0, x) = P (x0, x) = 2
σm+1 x0
|x|m+1

B−1(x0, x) = Q(x0, x) = − 2
σm+1 x
|x|m+1 (4.1)

Note that the Poisson kernel A−1 is real–valued, while its conjugate harmonic kernel B−1 is
Cliﬀord vector–valued. Their distributional limits for x0 → 0+ are given by

a−1(x) = lim
x0→0+ A−1(x0, x) = δ(x) = 2
σm T ∗
−m

b−1(x) = lim
x0→0+ B−1(x0, x) = H(x) = − 2
σm+1 U ∗
−m

and also c−1(x) = lim
x0→0+ C−1(x0, x) = 1
2 δ(x) + 1
2 e0 H(x)

Note that the distribution
 H(x) = − 2
σm+1 U ∗
−m = − 2
σm+1 Pv x
|x|m+1

where Pv stands for the principal value distribution in Rm, is the convolution kernel of the Hilbert
transform H in Rm (see e.g. [8]). Note also that both distributional boundary values are linked by
this Hilbert transform:
 H [a−1] = H [δ] = H ∗ δ = H = b−1
H [b−1] = H [H] = H ∗ H = δ = a−1

since H2 = 1, while e0 H [c−1] = c−1

Conversely, the Poisson kernels are the Poisson transforms of these distributional limits:

P [a−1] = P (x0, ·) ∗ a−1(·)(x) = P (x0, ·) ∗ δ(·)(x) = P (x0, x)
P [b−1] = P (x0, ·) ∗ b−1(·)(x) = P (x0, ·) ∗ H(·)(x) = Q(x0, x)

It follows that also the Poisson kernels themselves are linked by the Hilbert transform in the
variable x ∈ Rm:
 H [A−1] = H(·) ∗ A−1(x0, ·)(x) = H(·) ∗ P (x0, ·)(x)

= P (x0, ·) ∗ H(·)(x) = Q(x0, x) = B−1(x0, x)

H [B−1] = H2 [A−1] = A−1

For a function f ∈ L2(Rm), its Poisson transforms

P[f ] = P (x0, ·) ∗ f (·)(x) = A−1(x0, ·) ∗ f (·)(x)

Q[f ] = Q(x0, ·) ∗ f (·)(x) = B−1(x0, ·) ∗ f (·)(x)

9

belong to the Cliﬀord–Hardy space Harm
2 (
Rm+1
+ ) of Cliﬀord algebra valued harmonic functions
in Rm+1
+ :

Harm
2 (
Rm+1
+ ) = {F (x0, x) : F is harmonic in Rm+1
+ and sup
x0>0
 ∫

Rm |F (x0, x)|2 dx < +∞
}

and show the non–tangential L2–boundary values

lim
x0→0+ P[f ] = f and lim
x0→0+ Q[f ] = H[f ]

with H[f ] = H ∗ f = 2
σm+1 Pv ∫

Rm u
|u|m+1 f (x − u) du

the explicit expression for the Hilbert transform of f . In its turn the Cauchy transform of f ∈
L2(Rm), given by
 C[f ] = C−1(x0, ·) ∗ f (·)(x) = 1
2 P[f ] + 1
2 e0Q[f ]

belongs to the Cliﬀord–Hardy space H 2(Rm+1
+ ) of monogenic functions in Rm+1
+ :

H 2 (
Rm+1
+ ) = {
F (x0, x) : F is monogenic in Rm+1
+ and sup
x0>0
 ∫

Rm |F (x0, x)|2 dx < +∞
}

and shows the following non–tangential L2–boundary value:

lim
x0→0+ C[f ] = 1
2 f + 1
2 e0H[f ] = ( 1
2 δ + 1
2 e0H) ∗ f = AS[f ]

which belongs to the Cliﬀord–Hardy space H 2(Rm), see [8]. In signal analysis the functions in
H 2(Rm) are called analytic signals ; they show no negative-frequency components (see e.g. [10]).
Whence the notation AS for the boundary value of the Cauchy transform. Note that for this
Cauchy transform we have several equivalent expressions:

C[f ] = C [e0 H[f ]] = C [AS[f ]] = P [AS[f ]]

From the monogenicity of the Cauchy kernel C−1(x0, x) in Rm+1
+ , i.e.

DC−1 = 1
2 (∂x0 + e0∂) C−1 = 0

it follows that the Poisson kernels A−1(x0, x) and B−1(x0, x) satisfy the generalized Cauchy–
Riemann system { ∂x0A−1 + ∂B−1 = 0

∂x0B−1 + ∂A−1 = 0 (4.2)

and that DC−1 = 1
2 ∂x0C−1 − 1
2 e0∂C−1 = ∂x0 C−1 = −e0∂C−1 (4.3)

and also that
{ DA−1 = 1
2 ∂x0 A−1 − 1
2 e0∂A−1 = 1
2 ∂x0A−1 + 1
2 e0∂x0 B−1 = ∂x0 C−1 = DC−1

D(e0B−1) = 1
2 e0∂x0 B−1 − 1
2 e0∂e0B−1 = 1
2 e0∂x0 B−1 + 1
2 ∂x0 A−1 = ∂x0C−1 = DC−1 (4.4)

10

Now we put
 DC−1 = C−2 = 1
2 A−2 + 1
2 e0B−2

clearly a monogenic function in Rm+1
+ , since DC−2 = DDC−1 = 1
4 ∆m+1C−1 = 0. From this
deﬁnition it follows that { A−2 = ∂x0A−1 = −∂B−1

B−2 = ∂x0 B−1 = −∂A−1

leading to the explicit expressions for the conjugate harmonic components of C−2:




 A−2 = 2
σm+1
 1
|x|m+3 (
|x|2 − (m + 1)x
2
0) = 2
σm+1
 −mx
2
0 + |x|2

|x|m+3

B−2 = (m + 1) 2
σm+1
 x0x
|x|m+3
 (4.5)

Note that A−2(x0, x) is real–valued, while B−2(x0, x) is Cliﬀord vector–valued. Moreover it is
readily conﬁrmed that they satisfy the generalized CR–system
{ ∂x0A−2 + ∂B−2 = 0

∂x0B−2 + ∂A−2 = 0

The above relations (4.3)–(4.4) imply that the monogenic function C−2(x0, x) in Rm+1
+ shows the
monogenic potential (or primitive) C−1(x0, x) and the conjugate harmonic potentials A−2(x0, x)
and e0B−2(x0, x). The distributional limits for x0 → 0+ of these harmonic potentials are given by




 a−2(x) = limx0→0+ A−2(x0, x) = 2
σm+1 Fp 1
|x|m+1 = − 4π
σm+1 T ∗
−m−1

b−2(x) = limx0→0+ B−2(x0, x) = −∂δ = 2m
σm U ∗
−m−1

Conversely, the harmonic potentials A−2(x0, x) and B−2(x0, x) are recovered from these distribu-
tional boundary values by the Poisson transform

A−2(x0, x) = P [a−2(x)] = P (x0, ·) ∗ a−2(·)(x) = A−1(x0, ·) ∗ a−2(·)(x) = a−2 ∗ A−1
= Q [b−2(x)] = Q(x0, ·) ∗ b−2(·)(x) = B−1(x0, ·) ∗ b−2(·)(x) = b−2 ∗ B−1

and

B−2(x0, x) = P [b−2(x)] = P (x0, ·) ∗ b−2(·)(x) = A−1(x0, ·) ∗ b−2(·)(x) = b−2 ∗ A−1
= Q [a−2(x)] = Q(x0, ·) ∗ a−2(·)(x) = B−1(x0, ·) ∗ a−2(·)(x) = a−2 ∗ B−1

In the distribution a−2 one recognizes the convolution kernel −∂H = −H∂, known as the Hilbert–
Dirac kernel, see [7], or perhaps better known as the convolution kernel for the pseudodiﬀerential
operator (−∆) 1
2 (see [11]). The distribution b−2 is, up to a minus sign, the Dirac derivative of
the delta-distribution. Both distributional boundary values are linked by the Hilbert transform,
as shown a.o. in the following lemma.

Lemma 4.1. One has

(i) −∂a−1 = b−2, −∂b−1 = a−2, −e0∂c−1 = c−2

(ii) H [a−2] = b−2, H [b−2] = a−2, e0H [c−2] = c−2

11

(iii) c−1 ∗ a−2 = c−2, c−1 ∗ e0b−2 = c−2, c−1 ∗ c−2 = c−2

Proof
(i) Follows by direct calculation.

(ii) Making use of the convolution calculation rules, recalled in Proposition 2.1, we have

H [a−2] = − 4π
σm+1 H ∗ T ∗
−m−1 = 8π
σ2
m+1 U ∗
−m ∗ T ∗
−m−1

= 8π
σ2
m+1 π m
2 Γ ( m+2
2 )

(
Γ ( m+1
2 ))2 U ∗
−m−1 = 2m
σm U ∗
−m−1 = −∂δ = b−2

and
 H [b−2] = 2m
σm H ∗ U ∗
−m−1 = − 4m
σmσm+1 U ∗
−m ∗ U ∗
−m−1

= − 4m
σmσm+1 π m
2 Γ ( m+1
2 )

Γ ( m+1
2 ) Γ ( m+2
2 ) T ∗
−m−1 = − 4
σm+1 T ∗
−m−1 = a−2

(iii) We subsequently ﬁnd

c−1 ∗ a−2 = ( 1
2 δ + 1
2 e0H) ∗ a−2 = 1
2 a−2 + 1
2 e0H [a−2] = 1
2 a−2 + 1
2 e0b−2 = c−2

c−1 ∗ e0b−2 = ( 1
2 δ + 1
2 e0H) ∗ e0b−2 = 1
2 e0b−2 + 1
2 H [b−2] = 1
2 e0b−2 + 1
2 a−2 = c−2

and
 c−1 ∗ c−2 = c−1 ∗ ( 1
2 a−2 + 1
2 e0b−2
) = 1
2 c−2 + 1
2 c−2 = c−2
 □

Through the Poisson transform, the Hilbert–link between the distributional boundary values a−2
and b−2 is reﬂected in a similar relationship between the harmonic potentials A−2 and B−2, as it
was also the case for A−1 and B−1. Indeed, one has

H [A−2] = H(·) ∗ A−2(x0, ·)(x) = H(·) ∗ P (x0, ·) ∗ a−2(·)(x)
= P (x0, ·) ∗ H(·) ∗ a−2(·)(x) = P (x0, ·) ∗ b−2(·)(x) = B−2(x0, x)

H [B−2] = H2 [A−2] = A−2

These relations may also be rewritten as

b−1(·) ∗ A−2(x0, ·)(x) = B−2(x0, x)

b−1(·) ∗ B−2(x0, ·)(x) = A−2(x0, x)

while, quite trivially,
 a−1(·) ∗ A−2(x0, ·)(x) = A−2(x0, x)

a−1(·) ∗ B−2(x0, ·)(x) = B−2(x0, x)

Note the following two commutative schemes, which are each others Hilbert image:

A−1 −∂
−−−−→ B−2

x0→0+ ↓ ↓

δ = a−1 −∂
−−−−→ b−2 = −∂δ
 and B−1 −∂
−−−−→ A−2

x0→0+ ↓ ↓

H = b−1 −∂
−−−−→ a−2 = −∂H
 (4.6)

12

By means of the distributional limits a−2 and b−2, we are now able to prove some remarkable
relations between the conjugate harmonic components of C−1 and C−2; in fact they are shown to
be linked by the distributional limits a0 and b0 of the Green function and its conjugate (see Section
3).

Proposition 4.1. One has, convolutions being taken in the variable x ∈ Rm:

(i) a0(·) ∗ A−2(x0, ·)(x) = A−1(x0, x) = b0(·) ∗ B−2(x0, x)

(ii) a0(·) ∗ B−2(x0, ·)(x) = B−1(x0, x) = b0(·) ∗ A−2(x0, x)

(iii) a0(·) ∗ C−2(x0, ·)(x) = C−1(x0, x) = b0(·) ∗ C−2(x0, x)

(iv) c0(·) ∗ A−2(x0, ·)(x) = c0(·) ∗ B−2(x0, x) = c0(·) ∗ C−2(x0, x) = C−1(x0, x)

Proof
(i)(ii) Put b0 ∗ B−2 = A
′
−1. Then

∂x0A
′
−1 = b0 ∗ ∂x0B−2 = b0 ∗ (−∂A−2) = −b0∂ ∗ A−2 = δ ∗ A−2 = A−2
∂A
′
−1 = ∂b0 ∗ B−2 = −δ ∗ B−2 = B−2

while moreover
 lim
x0→0+ A
′
−1 = b0 ∗ b−2 = b0 ∗ (−∂δ) = −b0∂ ∗ δ = δ ∗ δ = δ = a−1

Similarly, by putting b0 ∗ A−2 = B′
−1, we have

∂x0B′
−1 = b0 ∗ ∂x0A−2 = b0 ∗ (−∂B−2) = −b0∂ ∗ B−2 = δ ∗ B−2 = B−2
∂B′
−1 = ∂b0 ∗ A−2 = −δ ∗ A−2 = A−2

while moreover
 lim
x0→0+ B′
−1 = b0 ∗ a−2 = b0 ∗ (−∂H) = −b0∂ ∗ H = δ ∗ H = H = b−1

So A
′
−1 and B′
−1 satisfy the CR–system (4.2) and show the same distributional limits for x0 → 0+
as A−1 and B−1, respectively, from which it follows that they have to coincide: A
′
−1 = A−1 and
B′
−1 = B−1. Now note that

a0 ∗ A−2 = a0 ∗ H [B−2] = a0 ∗ H ∗ B−2 = H ∗ a0 ∗ B−2 = b0 ∗ B−2 = A−1
a0 ∗ B−2 = a0 ∗ H [A−2] = a0 ∗ H ∗ A−2 = H ∗ a0 ∗ A−2 = b0 ∗ A−2 = B−1

to complete the proof of (i) and (ii).

(iii)(iv) It suﬃces to make the appropriate combinations of the results in (i) and (ii). □

For a function f ∈ L2(Rm) we can deﬁne in Rm+1
+ the conjugate harmonic functions

A−2[f ] = A−2(x0, ·) ∗ f (·)(x) and B−2[f ] = B−2(x0, ·) ∗ f (·)(x)

and the monogenic function C−2[f ] = C−2(x0, ·) ∗ f (·)(x)

They show non–tangential L2–boundary values on condition that f belongs to the Cliﬀord–Sobolev
space W 1
2 (Rm) = {f ∈ L2(Rm) : ∂f ∈ L2(Rm)}

13

Under these assumptions there holds

A
+
−2[f ] = lim
x0→0+ A−2[f ] = a−2 ∗ f = −H∂ ∗ f = −H [∂f ] = −∂H[f ]

B+
−2[f ] = lim
x0→0+ B−2[f ] = b−2 ∗ f = −∂δ ∗ f = −∂f

and also

C+
−2[f ] = lim
x0→0+ C−2[f ] = − 1
2 ∂H[f ] − 1
2 e0∂f = (−e0∂) ( 1
2 f + 1
2 e0H[f ]) = (−e0∂) (AS[f ])

Note that the convolution operators A
+
−2, B+
−2 and C+
−2 are bounded operators from W 1
2 (Rm) into
L2(Rm), and that, for f ∈ W 1
2 (Rm), the L2–boundary value C+
−2[f ] belongs to the Cliﬀord–Hardy
space H 2(Rm). Also note the following commutative scheme for a function f ∈ W 1
2 (Rm):

C−1[f ] −e0∂
−−−−−→ C−2[f ]

x0→0+ ↓ ↓x0 →0+

1
2 f + 1
2 e0H[f ] = AS[f ] −e0∂
−−−−−→ −e0∂AS[f ] = − 1
2 ∂H[f ] − 1
2 e0∂f

which reﬂects at the level of the operators, the commutative schemes (4.6) at the level of the
convolution kernels.

4.2 Further derived potentials

Proceeding in the same manner as in Subsection 4.1, we can deﬁne a sequence of monogenic
potentials in Rm+1
+ :

C−k−1 = DC−k = D2C−k+1 = . . . = DkC−1, k = 1, 2, . . .

where each monogenic potential decomposes into two conjugate harmonic potentials:

C−k−1 = 1
2 A−k−1 + 1
2 e0B−k−1, k = 1, 2, . . .

with, for k odd, say k = 2ℓ − 1,
{ A−2ℓ = ∂2ℓ−1
x0 A−1 = −∂2ℓ−2
x0 ∂B−1 = . . . = −∂2ℓ−1B−1

B−2ℓ = ∂2ℓ−1
x0 B−1 = −∂2ℓ−2
x0 ∂A−1 = . . . = −∂2ℓ−1A−1

while for k even, say k = 2ℓ,
{ A−2ℓ−1 = ∂2ℓ
x0 A−1 = −∂2ℓ−1
x0 ∂B−1 = . . . = ∂2ℓA−1

B−2ℓ−1 = ∂2ℓ
x0 B−1 = −∂2ℓ−1
x0 ∂A−1 = . . . = ∂2ℓB−1

Note that also holds

C−k−1 = ∂x0C−k = (−e0∂)C−k = ∂2
x0C−k+1 = (−e0∂)
2C−k+1 = . . . = ∂k
x0C−1 = (−e0∂)
kC−1

while the conjugate harmonic components satisfy the recurrence relations
{ A−k−1 = ∂x0A−k = −∂B−k

B−k−1 = ∂x0B−k = −∂A−k (4.7)

14

whence 



 DA−k = 1
2 (∂x0 − e0∂) A−k = 1
2 A−k−1 + 1
2 e0B−k−1 = C−k−1

D(e0B−k) = 1
2 (∂x0 e0 − ∂) B−k = 1
2 A−k−1 + 1
2 e0B−k−1 = C−k−1

which expresses the fact that A−k and e0B−k are indeed potentials (or primitives) of C−k−1. Their
distributional limits for x0 → 0+ are given by




 a−2ℓ = (−∂)
2ℓ−1H = −22ℓ−1 Γ ( m+2ℓ−1
2 )

π m−2ℓ+1
2 T ∗
−m−2ℓ+1

= (−1)
ℓ−12ℓ−1(2ℓ − 1)!! Γ ( m+2ℓ−1
2 )

π m+1
2 Fp 1
rm+2ℓ−1

b−2ℓ = (−∂)
2ℓ−1δ = 22ℓ−1 Γ ( m+2ℓ
2 )

π m−2ℓ+2
2 U ∗
−m−2ℓ+1

and 



 a−2ℓ−1 = ∂2ℓδ = 22ℓ Γ ( m+2ℓ
2 )

π m−2ℓ
2 T ∗
−m−2ℓ

b−2ℓ−1 = ∂2ℓH = −22ℓ Γ ( m+2ℓ+1
2 )

π m−2ℓ+1
2 U ∗
−m−2ℓ

= (−1)
ℓ−12ℓ(2ℓ − 1)!! Γ ( m+2ℓ+1
2 )

π m+1
2 Fp 1
rm+2ℓ ω

They show the following properties, which can be veriﬁed by direct calculation.

Lemma 4.2. One has for j, k = 1, 2, . . .

(i) a−k −∂
−−−→ b−k−1 −∂
−−−→ a−k−2

(ii) H [a−k] = b−k, H [b−k] = a−k

(iii) a−j ∗ a−k = a−j−k+1
a−j ∗ b−k = b−j ∗ a−k = b−j−k+1
b−j ∗ b−k = a−j−k+1.

Through the Poisson transform, the above Hilbert–link (Lemma 4.2(ii)) between the distribu-
tional boundary values a−k and b−k is reﬂected into a similar relationship between the harmonic
potentials A−k and B−k, as was already shown for k = 1 and k = 2. Indeed, we have, the Hilbert
transform being taken in the variable x ∈ Rm: H [A−k] = B−k and H [B−k] = A−k, which may
also be written as { b−1(·) ∗ A−k(x0, ·)(x) = B−k(x0, x)

b−1(·) ∗ B−k(x0, ·)(x) = A−k(x0, x) (4.8)

while, trivially, { a−1(·) ∗ A−k(x0, ·)(x) = A−k(x0, x)

a−1(·) ∗ B−k(x0, ·)(x) = B−k(x0, x) (4.9)

15

Note also the following commutative scheme:

A−k −∂
−−−−→ B−k−1 −∂
−−−−→ A−k−2

x0→0+ ↓ ↓ ↓

a−k −∂
−−−−→ b−k−1 −∂
−−−−→ a−k−2
 (4.10)

The formulae (4.8) and (4.9) are special cases of the more general, and remarkable, result that
the distributional boundary values a−k and b−k may act as convolution operators to convert the
harmonic potentials into harmonic potentials of a lower order.

Proposition 4.2. One has for k = 1, 2, . . . and j = 0, 1, . . .

(i) b−j−1 ∗ A−k = B−k−j

(ii) b−j−1 ∗ B−k = A−k−j

(iii) a−j−1 ∗ A−k = A−k−j

(iv) a−j−1 ∗ B−k = B−k−j

Proof
(i) First assume that k is even, say k = 2ℓ, and put b−j−1 ∗ A−2ℓ = B′
−2ℓ−j. Then we have

∂x0 B′
−2ℓ−j = b−j−1 ∗ ∂x0A−2ℓ = b−j−1 ∗ (−∂B−2ℓ) = − (b−j−1∂) ∗ B−2ℓ = a−j−2 ∗ B−2ℓ

Assuming j to be even, say j = 2i, there holds

a−2i−2 ∗ B−2ℓ = (−∂)
2i+1H ∗ B−2ℓ = (−∂)
2i+1A−2ℓ = B−2ℓ−2i−1 = B−2ℓ−j−1

while for j odd, say j = 2i − 1, we have

a−2i−2 ∗ B−2ℓ = ∂2iδ ∗ B−2ℓ = (−∂)
2iB−2ℓ = B−2ℓ−2i = B−2ℓ−j−1

and so ∂x0B′
−2ℓ−j = B−2ℓ−j−1. For the action of the Dirac operator ∂ on B′
−2ℓ−j we obtain

∂B′
−2ℓ−j = ∂b−j−1 ∗ A−2ℓ = −a−j−2 ∗ A−2ℓ

where now for j even, say j = 2i,

−a−2i−2 ∗ A−2ℓ = −(−∂)
2i+1H ∗ A−2ℓ = −(−∂)
2i+1B−2ℓ = −A−2ℓ−2i−1 = −A−2ℓ−j−1

while for j odd, say j = 2i − 1,

−a−2i−1 ∗ A−2ℓ = −∂2iδ ∗ A−2ℓ = −(−∂)
2iA−2ℓ = A−2ℓ−2i = −A−2ℓ−j−1

and hence ∂B′
−2ℓ−j = −A−2ℓ−j−1. Moreover

lim
x0→0+ B′
−2ℓ−j = b−j−1 ∗ a−2ℓ = b−j−1 ∗ (−∂)
2ℓ−1H = b−j−1(−∂)
2ℓ−1 ∗ H = a−2ℓ−j ∗ H = b−2ℓ−j

This means that B′
−2ℓ−j and B−2ℓ−j satisfy the same system (4.7) and show the same distribu-
tional boundary value for x0 → 0+, so they have to coincide, whence b−j−1 ∗ A−2ℓ = B−2ℓ−j.
Next assume that k is odd, say k = 2ℓ − 1, and put b−j−1 ∗ A−2ℓ+1 = B′′
−2ℓ−j+1. Then we have,
with a similar calculation as above: ∂x0B′′
−2ℓ−j+1 = B−2ℓ−j and ∂B′′
−2ℓ−j+1 = −A−2ℓ−j, while
limx0→0+ B′′
−2ℓ−j+1 = b−2ℓ−j+1, from which it follows that indeed b−j−1 ∗ A−2ℓ+1 = B−2ℓ−j+1,

16

which completes the proof of (i).

(ii) The proof of (ii) is similar to that of (i).

(iii) Using the Hilbert–link between the distributional boundary values a−j−1 and b−j−1, we have
indeed

a−j−1 ∗ A−k = H [b−j−1] ∗ A−k = H ∗ b−j−1 ∗ A−k = b−j−1 ∗ H ∗ A−k = b−j−1 ∗ B−k = A−k−j

Note however that an alternative proof of (iii) is already contained in the calculations in the proofs
of (i) and (ii).

(iv) The proof of (iv) is similar to that of (iii), now making use of (ii). □

For a function f ∈ L2(Rm) we can deﬁne in Rm+1
+ the conjugate harmonic functions

A−k[f ] = A−k(x0, ·) ∗ f (·)(x) and B−k[f ] = B−k(x0, x) ∗ f (·)(x), k = 1, 2, . . .

and the monogenic function

C−k[f ] = C−k(x0, ·) ∗ f (·)(x), k = 1, 2, . . .

By deﬁnition of the potential kernels A−k, B−k and C−k, it is readily obtained that A−k[f ] and
B−k[f ] are conjugate harmonic potentials of C−k−1[f ], while C−k[f ] is a monogenic potential (or
primitive) of C−k−1[f ] in Rm+1
+ . These potentials will show non–tangential L2–boundary values
for x0 → 0+ on condition that f belongs to the Cliﬀord–Sobolev space

W k−1
2 (Rm) = {
f ∈ L2(Rm) : ∂f, ∂2f, . . . , ∂k−1f ∈ L2(Rm)
}

Under this assumption we have

A
+
−2ℓ[f ] = lim
x0→0+ A−2ℓ[f ] = a−2ℓ ∗ f = −∂2ℓ−1H[f ] = −H [∂2ℓ−1f ]

B+
−2ℓ[f ] = lim
x0→0+ B−2ℓ[f ] = b−2ℓ ∗ f = −∂2ℓ−1f

A
+
−2ℓ−1[f ] = lim
x0→0+ A−2ℓ−1[f ] = a−2ℓ−1 ∗ f = ∂2ℓf

B+
−2ℓ−1[f ] = lim
x0→0+ B−2ℓ−1[f ] = b−2ℓ−1 ∗ f = ∂2ℓH[f ] = H [
∂2ℓf ]

and the convolution operators A
+
−k and B+
−k are bounded operators from W k−1
2 (Rm) into L2(Rm).
For a function f ∈ W k−1
2 (Rm) we also obtain the following expressions of the non–tangential
L2–boundary values of the monogenic potentials:

C+
−2ℓ[f ] = lim
x0→0+ C−2ℓ[f ] = − 1
2 ∂2ℓ−1H[f ] − 1
2 e0∂2ℓ−1f

= (−e0∂2ℓ−1) ( 1
2 f + 1
2 e0H[f ]) = (−e0∂)
2ℓ−1 (AS[f ])

C+
−2ℓ−1[f ] = lim
x0→0+ C−2ℓ−1[f ] = 1
2 ∂2ℓf + 1
2 e0∂2ℓH[f ]

= ∂2ℓ ( 1
2 f + 1
2 e0H[f ]) = ∂2ℓ (AS[f ]) = (−e0∂)
2ℓ (AS[f ])

17

which belong to the Cliﬀord–Hardy space H 2(Rm). This leads to the following commutative
schemes for a function f ∈ W k
2 (Rm):

C−2ℓ−1[f ] −e0∂
−−−−−→ C−2ℓ−2[f ] −e0∂
−−−−−→ C−2ℓ−3[f ]

x0 →0+ ↓ ↓ ↓

(−e0∂)
2ℓ (AS[f ]) −e0∂
−−−−−→ (−e0∂)
2ℓ+1 (AS[f ]) −e0∂
−−−−−→ (−e0∂)
2ℓ+2 (AS[f ])

The above scheme reﬂects at the level of the convolution operators, the commutative schemes
(4.10) at the level of the convolution kernels.

4.3 Explicit expression of the downstream potentials

In Subsection 4.1 we have already obtained the explicit expressions of the harmonic potentials
A−1, B−1, A−2 and B−2 (see 4.1, 4.5). Putting forward for the harmonic potentials A−k and B−k
the following form:

A−k = 2
σm+1
 1
|x|m+2k−1 Pk(x0, |x|2) and B−k = 2
σm+1
 x
|x|m+2k−1 Qk−1(x0, |x|2)

where Pk and Qk−1 are scalar–valued homogeneous polynomials of degree k and k − 1 respectively,
it is shown, by a direct calculation, that these polynomials satisfy the following recurrence relations:

Pk+1(t, u2) = (t2 + u2) ∂tPk − (m + 2k − 1) t Pk , P1(t, u2) = t

and Qk(t, u2) = (t2 + u2) ∂tQk−1 − (m + 2k − 1) t Qk−1 , Q0(t, u2) = −1

The fact that A−k and B−k are related by harmonic conjugacy leads to the following intertwined
relations for those polynomials:

Qk(x0, |x|2) = (m + 2k − 1) Pk + x
2
0 + |x|2

|x|2 x∂Pk

and Pk+1(x0, |x|2) = (
mx
2
0 − (2k − 1)|x|
2) Qk−1 − (x
2
0 + |x|2) ∂Qk−1 x

It is possible to obtain an explicit expression for Pk(t, u2) and Qk(t, u2) in terms of well-known
orthogonal polynomials. This is achieved in the following way. First rewrite these polynomials as

Pk(t, u2) = uk ̃Pk
 ( t
u
 )

Qk(t, u2) = uk ̃Qk
 ( t
u
 )

with ̃Pk(w) and ̃Qk(w) polynomials of degree k in the variable w = t/u. The recursion relations
for Pk and Qk may now be rewritten as

̃Pk(w) = (1 + w2)∂w ̃Pk−1(w) − (m + 2k − 3)w ̃Pk−1(w), ̃P0(w) = −1/(m − 1)
̃Qk(w) = (1 + w2)∂w ̃Qk−1(w) − (m + 2k − 1)w ̃Qk−1(w), ̃Q0(w) = 1

Using the operator identity

(1 + w2)∂w + 2(α + 1)w = (1 + w2)
−α∂w(1 + w2)
α+1

18

we subsequently ﬁnd
 ̃Pk(w) = − 1
m − 1 (1 + w2)
k+ m−1
2 (∂w)
k(1 + w2)
− m−1
2

̃Qk(w) = −(1 + w2)
k+ m+1
2 (∂w)
k(1 + w2)
− m+1
2

Comparing this result with the Rodrigues’ formula for the Gegenbauer polynomials, we obtain:

̃Pk(w) = (−1)
k+12kikk! 1
m − 1 Γ(−m − 2k + 2)
Γ(−m − k + 2) Γ(− m
2 + 3
2 )
Γ(− m
2 + 3
2 − k) C−k+1− m
2
k (iw)

and ̃Qk(w) = (−1)
k+12kikk! Γ(−m − 2k)
Γ(−m − k) Γ(− m
2 + 1
2 )
Γ(− m
2 + 1
2 − k) C−k− m
2
k (iw)

where i is the imaginary unit, eventually leading to

A−k = (−1)
k+1 2k+1

σm+1 k! 1
m − 1 Γ(−m − 2k + 2)
Γ(−m − k + 2) Γ(− m
2 + 3
2 )
Γ(− m
2 + 3
2 − k) |x|k

|x|m+2k−1 ikC−k+1− m
2
k
 (
i x0
|x|
 )

= − 22k+1

σm+1
 1
m − 1 Γ(−m − 2k + 2)
Γ(−m − k + 2) Γ(− m
2 + 3
2 )
Γ(− m
2 + 3
2 − k) Γ(− m
2 + 1)
Γ(− m
2 − k + 1) x
k
0
|x|m+2k−1 2F1
 (
− k
2 , 1 − k
2 ; m
2 ; − |x|2

x2
0
 )

and

B−k = (−1)
k 2k

σm+1 (k − 1)! Γ(−m − 2k + 2)
Γ(−m − k + 1) Γ(− m
2 + 1
2 )
Γ(− m
2 + 3
2 − k) |x|k−1x
|x|m+2k−1 ik−1C−k+1− m
2
k−1
 (
i x0
|x|
 )

= − 22k+1

σm+1
 Γ(−m − 2k + 2)
Γ(−m − k + 1) Γ(− m
2 + 1
2 )
Γ(− m
2 + 3
2 − k) Γ(− m
2 + 1)
Γ(− m
2 − k + 2) x
k−1
0 x
|x|m+2k−1 2F1
 (
− k + 1
2 , 1 − k
2 ; m
2 ; − |x|2

x2
0
 )

Finally, to give an idea, let us state the explicit expressions of the potentials A−k and B−k for a
couple of low values of k:

A−3(x0, |x|) = 2
σm+1
 1
|x|m+5 (
m(m + 1)x
3
0 − 3(m + 1)x0|x|2)

A−4(x0, |x|) = 2
σm+1
 1
|x|m+7 (
−m(m + 1)(m + 2)x
4
0 + 6(m + 1)(m + 2)x
2
0|x|2 − 3(m + 1)|x|
4)

and
 B−3(x0, |x|) = 2
σm+1
 x
|x|m+5 (m + 1) (
−(m + 2)x
2
0 + |x|
2)

B−4(x0, |x|) = 2
σm+1
 x
|x|m+7 (m + 1)(m + 3) (
(m + 2)x
3
0 − 3x0|x|
2)

5 Upstream potentials

5.1 The monogenic logarithmic function

Recall that Green’s function A0(x0, x) = − 2
m−1 1
σm+1 1
|x|m−1 , (3.1), and its conjugate harmonic

B0(x0, x) = 2
σm+1 x
|x|m Fm( |x|
x0 ), (3.4), satisfy in Rm+1
+ the system




 ∂x0A0 = −∂B0 = P = A−1

∂x0 B0 = −∂A0 = Q = B−1

19

(see also (3.2) in Section 3) from which it follows that

DA0 = 1
2 (∂x0 − e0∂) A0 = 1
2 P + 1
2 e0Q = C−1 (5.1)

and De0B0 = 1
2 (e0∂x0 − ∂) B0 = 1
2 e0Q + 1
2 P = C−1 (5.2)

Relations (5.1) and (5.2) express the fact that A0(x0, x) and e0B0(x0, x) are conjugate harmonic
potentials (or primitives), with respect to the operator D, of the Cauchy kernel C−1(x0, x) in
Rm+1
+ . Putting, as in Section 3, C0(x0, x) = 1
2 A0(x0, x) + 1
2 e0B0(x0, x), it is readily seen that

DC0(x0, x) = 1
2 C−1(x0, x) + 1
2 C−1(x0, x) = C−1(x0, x)

which implies that C0(x0, x) is a monogenic potential (or primitive), with respect to te operator D,
of the Cauchy kernel C−1(x0, x) in Rm+1
+ . Moreover there holds, in view of DC0 = 1
2 (∂x0 +e0∂)C0 =
0, that C−1 = DC0 = ∂x0 C0 = (−e0∂) C0

Recall the distributional limits for x0 → 0+ of A0(x0, x) and B0(x0, x):

a0(x) = − 2
m − 1 1
σm+1 Fp 1
|x|m−1 = − 2
m − 1 1
σm+1 T ∗
−m+1

b0(x) = 1
σm
 x
|x|m = 1
π 1
σm U ∗
−m+1

(see also Section 3, (3.7) and (3.6)), yielding

c0(x) = lim
x0→0+ C0(x0, x) = − 1
m − 1 1
σm+1 Fp 1
|x|m−1 + 1
2 e0 1
σm
 x
|x|m

As was expected these distributional boundary values are intimately related, as is shown in the
following lemma.

Lemma 5.1. One has

(i) −∂a0 = b−1 = H

(ii) −∂b0 = a−1 = δ

(iii) H [a0] = b0

(iv) H [b0] = a0

(v) c−1 ∗ a0 = c−1 ∗ e0b0 = c−1 ∗ c0 = c0

(vi) −e0∂c0 = c−1

(vii) e0H [c0] = c0

Proof
We make use of the calculation rules for the T ∗– and U ∗–distributions, recalled in Proposition 2.1.
For (i) we have

−∂a0 = 2
m − 1 1
σm+1 ∂T ∗
−m+1 = 2
m − 1 1
σm+1 (−m + 1)U ∗
−m = − 2
σm+1 U ∗
−m = b−1 = H

20

while for (ii)
 −∂b0 = − 1
π 1
σm ∂U ∗
−m+1 = − 1
π 1
σm (−2π)T ∗
−m = − 2
σm T ∗
−m = a−1 = δ

Then (iii) is obtained by

H [a0] = H ∗ a0 = (
− 2
σm+1 U ∗
−m
) ∗ (
− 2
m − 1 1
σm+1 T ∗
−m+1
)

= 4
m − 1 1

(σm+1)
2 U ∗
−m ∗ T ∗
−m+1 = 4
m − 1 1

(σm+1)
2 π m
2 Γ ( m
2 )

Γ ( m+1
2 ) Γ ( m−1
2 ) U ∗
−m+1

= Γ ( m
2 )

2π m
2 +1 U ∗
−m+1 = 1
π 1
σm U ∗
−m+1 = b0

from which also (iv) follows: H [b0] = H2 [a0] = a0. To obtain (v) it suﬃces to observe that

c−1 ∗ a0 = ( 1
2 a−1 + 1
2 e0b−1
) ∗ a0 = ( 1
2 δ + 1
2 e0H) ∗ a0 = 1
2 a0 + 1
2 e0b0 = c0

c−1 ∗ e0b0 = ( 1
2 δ + 1
2 e0H) ∗ e0b0 = 1
2 e0b0 + 1
2 H [b0] = 1
2 e0b0 + 1
2 a0 = c0

c−1 ∗ c0 = c−1 ∗ ( 1
2 a0 + 1
2 e0b0
) = 1
2 c0 + 1
2 c0 = c0

while (vi) is directly obtained by

−e0∂c0 = e0
 (
−∂ 1
2 a0 − ∂ 1
2 e0b0
) = 1
2 e0b−1 + 1
2 a−1 = c−1

Finally, we have
 H [c0] = 1
2 H [a0] + 1
2 H [e0b0] = 1
2 b0 + 1
2 e0a0

from which (vii) follows:
 e0H [c0] = 1
2 a0 + 1
2 e0b0 = c0
 □

Note the following commutative schemes which are each others Hilbert image:

A0(x0, x) −∂
−−−→ B−1(x0, x) = Q(x0, x)

x0 →0+ ↓ ↓

a0(x) −∂
−−−→ b−1(x) = H(x)
 and B0(x0, x) −∂
−−−→ A−1(x0, x) = P (x0, x)

x0 →0+ ↓ ↓

b0(x) −∂
−−−→ a−1(x) = δ(x) (5.3)
The following lemma, also in terms of distributions, makes the relationships between the harmonic
potentials A0, B0, A−1 = P and B−1 = Q more transparent.

Lemma 5.2. In distributional sense one has, convolutions being taken in the variable x ∈ Rm:

(i) A0 = a0 ∗ A−1 = b0 ∗ B−1

(ii) B0 = b0 ∗ A−1 = a0 ∗ B−1
 21

(iii) H ∗ A0 = B0 = A0 ∗ H

(iv) H ∗ B0 = A0 = B0 ∗ H

Proof
(i)(ii) The technique is the same as the one used in the proof of Proposition 4.1.

(iii)(iv) It suﬃces to observe that

A0 ∗ H = A−1 ∗ a0 ∗ H = A−1 ∗ b0 = B0

and B0 ∗ H = A0 ∗ H ∗ H = A0
 □

Similar properties hold for the monogenic potentials C0 and C−1.

Lemma 5.3. In distributional sense one has, convolutions being taken in the variable x ∈ Rm:

(i) C0 = C−1 ∗ a0 = C−1 ∗ e0b0 = C−1 ∗ c0

(ii) C0 = A−1 ∗ c0 = e0B−1 ∗ c0

Proof
Making use of the results of Lemma 5.2, we have for (i)

C−1 ∗ a0 = ( 1
2 A−1 + 1
2 e0B−1
) ∗ a0 = 1
2 A0 + 1
2 e0B0 = C0

C−1 ∗ e0b0 = ( 1
2 A−1 + 1
2 e0B−1
) ∗ e0b0 = 1
2 e0B0 + 1
2 A0 = C0

C−1 ∗ c0 = C−1 ∗ ( 1
2 a0 + 1
2 e0b0
) = 1
2 C0 + 1
2 C0 = C0

while for (ii)
 A−1 ∗ c0 = A−1 ∗ ( 1
2 a0 + 1
2 e0b0
) = 1
2 A0 + 1
2 e0B0 = C0

e0B−1 ∗ c0 = e0B−1 ∗ ( 1
2 a0 + 1
2 e0b0
) = 1
2 e0B0 + 1
2 B−1 ∗ b0 = C0
 □

Remark 5.1. The results (i)–(ii) of Lemma 5.2 are the analogues of the results of Proposition 4.1
for the case where j = −1, k = 1.

The potential kernels A0(x0, x), B0(x0, x) and C0(x0, x) may now be used in their corresponding
convolution operators deﬁning the conjugate harmonic potentials in Rm+1
+

A0[f ](x0, x) = A0(x0, ·) ∗ f (·)(x) and B0[f ](x0, x) = B0(x0, ·) ∗ f (·)(x)

and the monogenic potential

C0[f ](x0, x) = C0(x0, ·) ∗ f (·)(x) = 1
2 A0[f ](x0, x) + 1
2 e0B0[f ](x0, x)

The properties they enjoy, summarized in the next proposition, reﬂect the corresponding properties
of the potential kernels.
 22

Proposition 5.1. For a Schwartz function or a distribution f one has

(i) DA0[f ] = DB0[f ] = DC0[f ] = C−1[f ]

(ii) limx0→0+ A0[f ] = a0 ∗ f = −(−∆)
− 1
2 [f ]
limx0→0+ B0[f ] = b0 ∗ f = −E ∗ f = T [f ]
limx0→0+ C0[f ] = c0 ∗ f = a0 ∗ AS[f ] = e0b0 ∗ f

(iii) e0H [c0 ∗ f ] = c0 ∗ f

(iv) C0[f ] = C−1 [a0 ∗ f ] = C−1 [b0 ∗ H[f ]] = C−1 [e0b0 ∗ f ] = C−1 [a0 ∗ e0H[f ]]
= C−1 [c0 ∗ f ] = P [c0 ∗ f ] = A0 [AS[f ]] = e0B0 [AS[f ]]

Note also the following commutative scheme, which may be derived from the commutative
schemes (5.3):
 C0[f ] −e0∂
−−−−−→ C−1[f ]

x0 →0+ ↓ ↓x0→0+

c0 ∗ f −e0∂
−−−−−→ c−1 ∗ f = AS[f ]

Remark 5.2. As already explained in the introduction, in the upper half of the complex plane
the function ln(z) is a holomorphic potential (or primitive) of the Cauchy kernel 1
z and its real
and imaginary components are the fundamental solution ln |z| of the Laplace operator, and its
conjugate harmonic i arg(z) respectively. By similarity we could say that C0(x0, x) = 1
2 A0(x0, x) +
1
2 e0B0(x0, x), being a monogenic potential of the Cauchy kernel C−1(x0, x) and the sum of the
fundamental solution A0(x0, x) of the Laplace operator and its conjugate harmonic e0B0(x0, x), is
a monogenic logarithmic function in the upper half–space Rm+1
+ .

5.2 The potentials of the logarithmic monogenic function

Inspired by the properties contained in Proposition 4.1 and Lemma 5.2 we proceed as follows for
the construction of harmonic and monogenic potentials of C0(x0, x) in Rm+1
+ . We put
{ A1(x0, x) = a0(·) ∗ A0(x0, ·)(x) = b0(·) ∗ B0(x0, ·)

B1(x0, x) = a0(·) ∗ B0(x0, ·)(x) = b0(·) ∗ A0(x0, ·)

and we verify at once that

∂x0A1 = a0 ∗ ∂x0A0 = a0 ∗ A−1 = A−1 ∗ a0 = P[a0] = A0

∂x0A1 = b0 ∗ ∂x0B0 = b0 ∗ (−∂A0) = (−b0∂) ∗ A0 = δ ∗ A0 = A0 (5.4)

and ∂x0 B1 = a0 ∗ ∂x0B0 = (−a0∂) ∗ A0 = H[A0] = B0

∂x0 B1 = b0 ∗ ∂x0A0 = b0 ∗ (−∂B0) = (−b0∂) ∗ B0 = δ ∗ B0 = B0 (5.5)

while also −∂A1 = −∂a0 ∗ A0 = H ∗ A0 = H[A0] = B0

−∂A1 = −∂b0 ∗ B0 = δ ∗ B0 = B0 (5.6)

and −∂B1 = −∂a0 ∗ B0 = H[B0] = A0

−∂B1 = −∂b0 ∗ A0 = δ ∗ A0 = A0 (5.7)

23

The relations (5.4)–(5.7) precisely are the relations needed for A1(x0, x) and B1(x0, x) to be con-
jugate harmonic potentials in Rm+1
+ of the function C0(x0, x). It then follows at once that

C1(x0, x) = 1
2 A1(x0, x) + 1
2 e0B1(x0, x)

is a monogenic potential in Rm+1
+ of C0 and there holds that DC1 = ∂x0 C1 = (−e0∂)C1 = C0.
Also note that the conjugate harmonic potentials A1(x0, x) and B1(x0, x) form a Hilbert pair, the
Hilbert transform being taken in the variable x ∈ Rm. Indeed, we have

H [A1] = H(·) ∗ A1(x0, ·)(x) = H(·) ∗ a0(·) ∗ A0(x0, ·)(x) = b0(·) ∗ A0(x0, ·) = B1(x0, x)

H [B1] = H2 [A1] = A1

The distributional limits for x0 → 0+ of the conjugate harmonic potentials A1 and B1 are given
by { a1(x) = limx0→0+ A1(x0, x) = a0(·) ∗ a0(·)(x) = b0(·) ∗ b0(·)(x)

b1(x) = limx0→0+ B1(x0, x) = a0(·) ∗ b0(·)(x) = b0(·) ∗ a0(·)(x)

Making use of the calculation rules for the convolution of the T ∗– and U ∗–distributions (see Section
2, Proposition 2.1), these distributional boundary values are explicitly given by




 a1(x) = 1
π 1
σm
 1
m − 2 T ∗
−m+2 = 1
σm
 1
m − 2 1
|x|m−2

b1(x) = − 1
π 1
σm+1
 1
m − 1 U ∗
−m+2 = − 1
σm+1
 2
m − 1 x
|x|m−1
 (5.8)

They show the following properties, where we have put, quite naturally, c1(x) = 1
2 a1(x) +
1
2 e0b1(x).

Lemma 5.4.

(i) −∂a1 = b0, −∂b1 = a0, −e0∂c1 = c0

(ii) H [a1] = b1, H [b1] = a1, e0H [c1] = c1

(iii) c−1 ∗ a1 = c−1 ∗ e0b1 = c−1 ∗ c1 = c1

(iv) a0 ∗ c0 = c0 ∗ a0 = c1, e0b0 ∗ c0 = c0 ∗ e0b0 = c1

Proof
For (i) we consecutively have

−∂a1 = − 1
π 1
σm
 1
m − 2 ∂T ∗
−m+2 = − 1
π 1
σm
 1
m − 2 (−m + 2) U ∗
−m+1 = 1
π 1
σm U ∗
−m+1 = b0

−∂b1 = 1
π 1
σm+1
 1
m − 1 ∂U ∗
−m+2 = 1
π 1
σm+1
 1
m − 1 (−2π) T ∗
−m+1 = − 2
m − 1 1
σm+1 T ∗
−m+1 = a0

and
 −e0∂c1 = −e0∂ ( 1
2 a1 + 1
2 e0b1
) = e0 1
2 b0 + 1
2 a0 = c0

For (ii) we obtain
 H [a1] = H [a0 ∗ a0] = b0 ∗ a0 = b1
H [b1] = H2 [a1] = a1

24

and
 e0H [c1] = e0
 ( 1
2 H [a1] + 1
2 H [e0b1]) = 1
2 e0b1 + 1
2 a1 = c1

For (iii) it holds that

c−1 ∗ a1 = ( 1
2 δ + 1
2 e0H) ∗ a1 = 1
2 a1 + 1
2 e0b1 = c1

c−1 ∗ e0b1 = ( 1
2 δ + 1
2 e0H) ∗ (e0b1) = 1
2 e0b1 + 1
2 a1 = c1

and
 c−1 ∗ c1 = c−1 ∗ ( 1
2 a1 + 1
2 e0b1
) = 1
2 c1 + 1
2 c1 = c1

Finally, (iv) follows from the following calculations:

a0 ∗ c0 = a0 ∗ ( 1
2 a0 + 1
2 e0b0
) = 1
2 a1 + 1
2 e0b1 = c1

c0 ∗ a0 = ( 1
2 a0 + 1
2 e0b0
) ∗ a0 = 1
2 a1 + 1
2 e0b1 = c1

and
 e0b0 ∗ c0 = e0b0 ∗ ( 1
2 a0 + 1
2 e0b0
) = 1
2 e0b1 + 1
2 a1 = c1

c0 ∗ e0b0 = ( 1
2 a0 + 1
2 e0b0
) ∗ e0b0 = 1
2 e0b1 + 1
2 a1 = c1
 □

Now that we have the distributional boundary values a1(x) and b1(x) at our disposal, the fol-
lowing relations between the harmonic potentials (A1, B1) and (A−1, B−1) may be readily shown.

Lemma 5.5. One has, convolutions being taken in the variable x ∈ Rm:

(i) A1(x0, x) = a1(·) ∗ A−1(x0, ·)(x) = b1(·) ∗ B−1(x0, ·)(x)

(ii) B1(x0, x) = a1(·) ∗ B−1(x0, ·)(x) = b1(·) ∗ A−1(x0, ·)(x)

Note that (−∆m)a1 = (−∂)
2a1 = (−∂)b0 = δ, and indeed, in −a1 = − 1
σm 1
m−2 1
|x|m−2 we rec-
ognize the fundamental solution of the Laplace operator ∆m in Rm. Also note the commutative
schemes which are each others Hilbert image:

A1(x0, x) −∂
−−−−→ B0(x0, x)

x0 →0+ ↓ ↓

a1(x) −∂
−−−→ b0(x)
 and B1(x0, x) −∂
−−−→ A0(x0, x)

x0→0+ ↓ ↓

b1(x) −∂
−−−→ a0(x)
 (5.9)

As before, the potential kernels A1(x0, x), B1(x0, x) and C1(x0, x) may be used as convolution
kernels to deﬁne conjugate harmonic functions and their monogenic sum in Rm+1
+ , by putting, for
a function f ∈ L2(Rm):
{ A1[f ] = A1(x0, ·) ∗ f (·)(x) = A0 [a0 ∗ f ] = B0 [b0 ∗ f ]

B1[f ] = B1(x0, ·) ∗ f (·)(x) = A0 [b0 ∗ f ] = B0 [a0 ∗ f ]

25

and C1[f ] = C1(x0, ·) ∗ f (·)(x) = C0 [a0 ∗ f ] = C0 [e0b0 ∗ f ]

The corresponding non–tangential L2–boundary values for x0 → 0+ are given by limx0→0+ A1[f ] =
a1 ∗ f , limx0→0+ B1[f ] = b1 ∗ f and limx0→0+ C1[f ] = c1 ∗ f , and the commutative schemes (5.9)
eventually lead to the following one:
 C1[f ] −e0∂
−−−−−→ C0[f ]

x0→0+ ↓ ↓x0→0+

c1 ∗ f −e0∂
−−−−−→ c0 ∗ f

The conjugate harmonic potentials A1(x0, x) and B1(x0, x) may now be determined explicitly by a
computation similar to the one used in Section 3 to determine the conjugate harmonic of Green’s
function. For this and subsequent calculations the dimension m is assumed to be great enough in
order that the expressions obtained should remain valid. Starting from the equation (5.4)

∂x0A1(x0, x) = A0(x0, x) = − 2
m − 1 1
σm+1
 1
|x0e0 + x|m−1

we ﬁnd in Rm+1
+
 A1(x0, x) = a1(x) − 2
m − 1 1
σm+1
 1
|x|m−2 ̃Fm−2
 ( x0
|x|
 ) (5.10)

where we have put ̃Fm−2 (u) = ∫ u

0
 dζ

(1 + ζ2)
 m−1
2

A priori it is not clear that A1(x0, x) is well–deﬁned for x = 0. However, in virtue of the relation

̃Fm−2(u) = Fm−2(+∞) − Fm−2
 ( 1
u
 ) = √
π
2 2
m − 2 Γ ( m
2 )

Γ ( m−1
2 ) − Fm−2
 ( 1
u
 )

expression (5.10) for A1(x0, x) is turned into, with m > 2:

A1(x0, x) = 2
m − 1 1
σm+1
 1
|x|m−2 Fm−2
 ( |x|
x0
 )

or, introducing again the hypergeometric function 2F1,

A1(x0, x) = 2
m − 1 1
σm+1
 1
m − 2 1
x
m−2
0 2F1
 ( m
2 − 1; m − 1
2 ; m
2 ; − |x|2

x2
0
 )

showing that A1(x0, x) indeed is well–deﬁned for |x| = 0 with

A1(x0, 0) = 2
(m − 1)(m − 2) 1
x
m−2
0 , x0 > 0

By some lengthy calculations it may be veriﬁed that the above function A1(x0, x) also satisﬁes the
equation
 −∂A1(x0, x) = B0(x0, x) = 2
σm+1
 x
|x|m Fm
 ( |x|
x0
 )

26

and also shows the distributional limit (5.8) given by

lim
x0→0+ A1(x0, x) = 1
σm
 1
m − 2 1
|x|m−2 = a1(x)

It is perhaps interesting to mention that in the course of these calculations, use has been made of
the following recurrence relation for the function Fm:

Fm(v) = m − 2
m − 1 Fm−2(v) − 1
m − 1 vm−2

(1 + v2)
 m−1
2

For the harmonic potential B1(x0, x) we start the computation from equation (5.5):

∂x0 B1(x0, x) = B0(x0, x) = 2
σm+1
 x
|x|m Fm
 ( |x|
x0
 )

leading to the expression, with m > 1:

B1(x0, x) = 2
σm+1
 x0x
|x|m Fm
 ( |x|
x0
 ) − 2
σm+1
 1
m − 1 x
|x|m−1

or
 B1(x0, x) = 2
m 1
σm+1
 x
x
m−1
0 2F1
 ( m
2 ; m + 1
2 ; m
2 + 1; − |x|2

x2
0
 ) − 2
σm+1
 1
m − 1 x
|x|m−1

showing that B1(x0, x) is well–deﬁned for x = 0 with

B1(x0, 0) = 0, x0 > 0

Note that the distributional limit b1(x) is indeed recovered:

lim
x0→0+ B1(x0, x) = − 2
σm+1
 1
m − 1 x
|x|m−1 = b1((x)

It may now readily be veriﬁed that the above function B1(x0, x) also satisﬁes equation (5.7):

−∂B1(x0, x) = A0(x0, x) = − 2
m − 1 1
σm+1
 1
|x|m−1

5.3 The next step

Proceeding in a similar way we may deﬁne in the next step
{ A2(x0, x) = a0(·) ∗ A1(x0, ·)(x) = b0(·) ∗ B1(x0, ·)(x)

B2(x0, x) = a0(·) ∗ B1(x0, ·)(x) = b0(·) ∗ A1(x0, ·)(x)

and verify that in Rm+1
+ it holds that

∂x0A2 = a0 ∗ ∂x0A1 = a0 ∗ A0 = A1
∂x0A2 = b0 ∗ ∂x0B1 = b0 ∗ B0 = A1

and
 ∂x0B2 = a0 ∗ ∂x0 B1 = a0 ∗ B0 = B1
∂x0B2 = b0 ∗ ∂x0A1 = b0 ∗ A0 = B1

27

while also
 −∂A2 = −∂a0 ∗ A1 = H ∗ A1 = H [A1] = B1
−∂A2 = −∂b0 ∗ B1 = δ ∗ B1 = B1

and
 −∂B2 = −∂a0 ∗ B1 = H ∗ B1 = H [B1] = A1
−∂B2 = −∂b0 ∗ A1 = δ ∗ A1 = A1

These relations justify A2(x0, x) and B2(x0, x) to be called conjugate harmonic potentials in Rm+1
+
of the function C1(x0, x). It follows that

C2(x0, x) = 1
2 A2(x0, x) + 1
2 e0B2(x0, x)

is a monogenic potential in Rm+1
+ of C1 and there also holds DC2 = ∂x0 C2 = (−e0∂)C2 = C1.
As before, the conjugate harmonic potentials A2(x0, x) and B2(x0, x) form a Hilbert pair in the
variable x ∈ Rm:
{ H [A2(x0, x)] = H(·) ∗ A2(x0, ·)(x) = b−1(·) ∗ A2(x0, ·)(x) = B2(x0, x)

H [B2(x0, x)] = H2 [A2(x0, x)] = b−1(·) ∗ B2(x0, ·)(x) = A2(x0, x)

while, trivially, { a−1(·) ∗ A2(x0, ·)(x) = A2(x0, x)

a−1(·) ∗ B2(x0, ·)(x) = B2(x0, x)

Their distributional limits for x0 → 0+ are given by
{ a2(x) = limx0→0+ A2(x0, x) = a0 ∗ a1(x) = b0 ∗ b1(x)

b2(x) = limx0→0+ B2(x0, x) = a0 ∗ b1(x) = b0 ∗ a1(x)

which may be calculated explicitly to be

a2(x) = (
− 2
m − 1 1
σm+1 T ∗
−m+1
) ∗ ( 1
π 1
σm
 1
m − 2 T ∗
−m+2
) = − 2
(m − 1)(m − 3) 1
σm+1
 1
|x|m−3

or
 a2(x) = ( 1
π 1
σm U ∗
−m+1
) ∗ (
− 1
π 1
σm+1
 1
m − 1 U ∗
−m+2
) = − 1
π 1
(m − 1)(m − 3) 1
σm+1 T ∗
−m+3

and
 b2(x) = (
− 2
m − 1 1
σm+1 T ∗
−m+1
) ∗ (
− 1
π 1
σm+1
 1
m − 1 U ∗
−m+2
) = 1
2 1
σm
 1
m − 2 x
|x|m−2

or
 b2(x) = ( 1
π 1
σm U ∗
−m+1
) ∗ ( 1
π 1
σm
 1
m − 2 T ∗
−m+2
) = 1
2π2 1
σm
 1
m − 2 U ∗
−m+3

Putting c2(x) = 1
2 a2(x) + 1
2 e0b2(x) we can prove the following properties of those distributional
boundary values.
 28

Lemma 5.6.

(i) −∂a2 = b1, −∂b2 = a1, −e0∂c2 = c1

(ii) H [a2] = b2, H [b2] = a2, e0H [c2] = c2

(iii) c−1 ∗ a2 = c−1 ∗ b2 = c−1 ∗ c2 = c2

(iv) c0 ∗ a1 = a1 ∗ c0 = c2, c0 ∗ e0b1 = e0b1 ∗ c0 = c2

Proof
For (i) we obtain

−∂a2(x) = −∂ (
− 1
π 1
σm+1
 1
m − 1 1
m − 3 T ∗
−m+3
) = 1
π 1
σm+1
 1
m − 1 1
m − 3 (−m + 3) U ∗
−m+2

= − 1
π 1
m − 1 1
σm+1 U ∗
−m+2 = b1(x)

−∂b2(x) = −∂ (
− 1
2π2 1
σm
 1
m − 2 U ∗
−m+3
) = − 1
2π2 1
σm
 1
m − 2 (−2π) T ∗
−m+2

= 1
π 1
m − 2 1
σm T ∗
−m+2 = a1(x)

(e0∂) c2(x) = (e0∂) ( 1
2 a2 + 1
2 e0b2
) = 1
2 e0b1 + 1
2 a1 = c1(x)

while for (ii)
 H [a2] = H [a0 ∗ a1] = H [a0] ∗ a1 = b0 ∗ a1 = b2

H [b2] = H2 [a2] = a2

e0H [c2] = e0H [ 1
2 a2 + 1
2 e0b2
] = 1
2 e0b2 + 1
2 a2 = c2

Statements (iii) and (iv) follow by direct computation. □

Making use of the distributional boundary values a1(x), b1(x), a2(x) and b2(x) we may now prove
by direct computation the following equivalent expressions for the conjugate harmonic potentials
A2(x0, x) and B2(x0, x).

Lemma 5.7. One has, convolutions being taken in the variable x ∈ Rm:

(i) A2 = a1 ∗ A0 = b1 ∗ B0 = a2 ∗ A−1 = b2 ∗ B−1

(ii) B2 = a1 ∗ B0 = b1 ∗ A0 = a2 ∗ B−1 = b2 ∗ A−1

Also note the commutative schemes

A2(x0, x) −∂
−−−−→ B1(x0, x)

x0 →0+ ↓ ↓

a2(x) −∂
−−−→ b1(x)
 and B2(x0, x) −∂
−−−→ A1(x0, x)

x0→0+ ↓ ↓

b2(x) −∂
−−−→ a1(x)

We also have explicitly determined the conjugate harmonic potentials A2(x0, x) (for m > 3) and
B2(x0, x) (for m > 2):

A2(x0, x) = 2
m − 1 1
σm+1
 x0
|x|m−2 Fm−2
 ( |x|
x0
 ) − 2
m − 1 1
m − 3 1
σm+1
 1
|x|m−3

B2(x0, x) = 1
σm+1
 x|x|2

|x|m Fm
 ( |x|
x0
 ) − m − 3
m − 1 1
σm+1
 x
|x|m−2 Fm−2
 ( |x|
x0
 )

29

5.4 The general case

Inspired by the properties of the harmonic potentials A1(x0, x), B1(x0, x), A2(x0, x) and B2(x0, x),
we deﬁne recursively, for general k = 1, 2, 3, . . . , the following functions in Rm+1
+ , the convolutions
being taken in the variable x ∈ Rm:

Ak(x0, x) = a0 ∗ Ak−1 = a1 ∗ Ak−2 = . . . = ak−1 ∗ A0
= b0 ∗ Bk−1 = b1 ∗ Bk−2 = . . . = bk−1 ∗ B0
Bk(x0, x) = a0 ∗ Bk−1 = a1 ∗ Bk−2 = . . . = ak−1 ∗ B0
= b0 ∗ Ak−1 = b1 ∗ Ak−2 = . . . = bk−1 ∗ A0

and Ck(x0, x) = 1
2 Ak(x0, x) + 1
2 e0Bk(x0, x)

Note that for k = 1, 2 we indeed recover the harmonic potentials studied in the previous subsections.
In a similar way as above, it is now shown that Ak(x0, x), Bk(x0, x) and Ck(x0, x) satisfy the
following equations:

(i) ∂x0 Ak = Ak−1
−∂Ak = Bk−1
DAk = 1
2 (∂x0 − e0∂) Ak = 1
2 Ak−1 + 1
2 e0Bk−1 = Ck−1

(ii) ∂x0 Bk = Bk−1
−∂Bk = Ak−1
D (e0Bk) = 1
2 (∂x0 − e0∂) e0Bk = 1
2 e0Bk−1 + 1
2 Ak−1 = Ck−1

(iii) DCk = 1
2 (∂x0 + e0∂) ( 1
2 Ak + 1
2 e0Bk) = 0

(iv) DCk = D ( 1
2 Ak + 1
2 e0Bk) = Ck−1

which clearly show that Ak(x0, x) and Bk(x0, x) are conjugate harmonic potentials of Ck−1(x0, x)
in Rm+1
+ , while Ck(x0, x) is a monogenic potential of the same Ck−1(x0, x) in Rm+1
+ . Their distri-
butional boundary values for x0 → 0+ are given by the recurrence relations

ak(x) = a0 ∗ ak−1 = a1 ∗ ak−2 = . . . = ak−1 ∗ a0
= b0 ∗ bk−1 = b1 ∗ bk−2 = . . . = bk−1 ∗ b0
bk(x) = a0 ∗ bk−1 = a1 ∗ bk−2 = . . . = ak−1 ∗ b0
= b0 ∗ ak−1 = b1 ∗ ak−2 = . . . = bk−1 ∗ a0

for which the following explicit formulae may be deduced:




 a2j = − 1
2j−1 1
πj 1
(m − 1)(m − 3) . . . (m − 2j − 1) 1
σm+1 T ∗
−m+2j+1

a2j−1 = 1
2j−1 1
πj 1
(m − 2)(m − 4) . . . (m − 2j) 1
σm T ∗
−m+2j




 b2j = 1
2j 1
πj+1 1
(m − 2)(m − 4) . . . (m − 2j) 1
σm U ∗
−m+2j+1

b2j−1 = − 1
2j−1 1
πj 1
(m − 1)(m − 3) . . . (m − 2j + 1) 1
σm+1 U ∗
−m+2j

These distributional limits show the following, by now traditional, properties.

30

Lemma 5.8. One has for k = 1, 2, . . .:

(i) −∂ak = bk−1

(ii) −∂bk = ak−1

(iii) H [ak] = b−1 ∗ ak = bk

(iv) H [bk] = b−1 ∗ bk = ak
Proof
Follows by direct computation using the derivation and convolution formulae for the T ∗– an U ∗–
distributions. □

6 Conclusion

While constructing a higher dimensional analogue in upper half–space Rm+1
+ of the function ln z in
the upper half of the complex plane, preserving its fundamental property of being a holomorphic
potential of the Cauchy kernel 1
z , it became clear that this monogenic logarithmic function is but
one of a double sequence of such kind of potentials, just as ln z is the central element in the double
sequence of holomorphic primitives:

1
k! zk [
ln z − (1 + 1
2 + . . . + 1
k )
] → . . . → z(ln z−1) → ln z
 d
dz−→ 1
z → − 1
z2 → . . . → (−1)
k−1 (k − 1)!
zk

The sequence of monogenic potentials corresponding to the negative integer powers of z, which we
called downstream potentials, were rather easily constructed via diﬀerentiation with the conjugate
generalized Cauchy–Riemann operator D. The explicit construction of the monogenic potentials
corresponding to the logarithmic functions in C+, which we termed upstream potentials, requires
tedious calculations involving primitivation with respect to D, and up to now we have executed
three inductive steps. A general expression for these upstream potentials is lacking, but their prop-
erties are known since they arise as convolutions of adjacent potentials with their distributional
boundary values in Rm. Also with an eye on possible applications, the upstream potentials will be
further calculated in the lower dimensional cases where m = 2, 3, and it is hoped for that a general
formula, mimicking the one in the complex plane, will appear.

The above mentioned distributional boundary values are really fundamental, since not only they
are used in the deﬁnition of the potentials, but also uniquely determine the conjugate harmonic po-
tentials obtained by primitivation, thanks to the simple, but crucial, fact that a monogenic function
in Rm+1
+ vanishing at the boundary Rm indeed is zero. For those distributional boundary values
we have established a general formula, showing that they all ﬁt into two families of distributions
in Rm, one scalar–valued, the second one Cliﬀord vector–valued. In some particular cases they
have been identiﬁed as fundamental solutions of the Dirac operator or the Laplace operator, or
as convolution kernels for some pseudodiﬀerential operators related to both these operators. The
forthcoming paper [1] will treat this remarkable relationship between the distributional boundary
values of the harmonic potentials and speciﬁc integer and half–integer powers of the Dirac and
Laplace operators.

References

[1] F. Brackx, H. De Bie, H. De Schepper, Distributional boundary values of harmonic potentials
in Euclidean half–space as fundamental solutions of convolution operators in Cliﬀord analysis
(submitted).
 31

[2] F. Brackx, B. de Knock, H. De Schepper, D. Eelbode, A Calculus Scheme for Cliﬀord Distri-
butions, Tokyo J. Math. 29(2) (2006), 495–513.

[3] F. Brackx, R. Delanghe, F. Sommen, Cliﬀord Analysis, Pitman Publishers (Boston–London–
Melbourne, 1982).

[4] F. Brackx, R. Delanghe, F. Sommen, On Conjugate Harmonic Functions in Euclidean Space,
Math. Meth. Appl. Sci. 25 (2002), 1553–1562.

[5] F. Brackx, R. Delanghe, F. Sommen, Spherical means and distributions in Cliﬀord analysis. In:
T. Qian, Th. Hempﬂing, A. McIntosh, F. Sommen (eds), Advances in Analysis and Geometry:
New Developments Using Cliﬀord Algebra, Trends in Mathematics, Birkh¨auser (Basel, 2004).

[6] F. Brackx, R. Delanghe, F. Sommen, Spherical means, distributions and convolution operators
in Cliﬀord analysis, Chin. Ann. Math. 24B(2) (2003), 133–146.

[7] F. Brackx, H. De Schepper, Hilbert-Dirac Operators in Cliﬀord Analysis, Chin. Ann. Math.
26B(1) (2005), 1–14.

[8] J. Gilbert, M. Murray, Cliﬀord Algebra and Dirac Operators in Harmonic Analysis, Cambridge
University Press (Cambridge, 1991).

[9] I. S. Gradshteyn, I.M. Ryzhik, Table of integrals, series, and products. Translated from the
Russian. Translation edited and with a preface by Alan Jeﬀrey and Daniel Zwillinger. Seventh
edition. Elsevier / Academic Press (Amsterdam, 2007).

[10] S.L. Hahn, Hilbert transforms in signal processing. The Artech House Signal Processing Li-
brary. Artech House, Inc. (Boston,1996).

[11] S. Helgason, Groups and Geometric Analysis, Pure and Applied Mathematics Academic Press
(Orlando–London, 1984).

[12] I. Porteous, Topological Geometry, Van Nostrand Reinhold Company (London–New York–
Toronto–Melbourne, 1969).

[13] S. Lang, Complex Analysis, Graduate Texts in Mathematics, 103, Springer–Verlag (New York,
1999).

[14] Zhenyuan Xu, Chen Jin, Zhang Wangue, A Harmonic Conjugate of the Poisson Kernel and
a Boundary Value Problem for Monogenic Functions in the Unit Ball of Rn(n ≥ 2), Simon
Stevin 64(2) (1990), 187–201.
 32
