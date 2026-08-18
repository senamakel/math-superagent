<!-- source: https://ddd.uab.cat/pub/artpub/2013/gsduab_3450/FigTucVil2012.pdf | converted from PDF -->

Computer-assisted techniques for the veriﬁcation
of the Chebyshev property of Abelian integrals

Jordi-Llu´ıs Figueras, Warwick Tucker and Jordi Villadelprat

Department of Mathematics, Uppsala University, 751 06 Uppsala, Sweden

Departament d’Enginyeria Inform`atica i Matem`atiques, ETSE,
Universitat Rovira i Virgili, 43007 Tarragona, Spain

Abstract. We develop techniques for the veriﬁcation of the Chebyshev property of Abelian integrals.
These techniques are a combination of theoretical results, analysis of asymptotic behavior of Wronskians,
and rigorous computations based on interval arithmetic. We apply this approach to tackle a conjecture
formulated by Dumortier and Roussarie in [Birth of canard cycles, Discrete Contin. Dyn. Syst. 2 (2009),
723–781], which we are able to prove for q ⩽ 2.

1 Introduction and setting of the problem

The present paper addresses the problem of verifying when a collection of Abelian integrals form an extended
complete Chebyshev system (ECT-system for short). This problem arises in the context of the second part
of Hilbert’s 16th problem [16], that asks about the maximum number and location of limit cycles of a planar
polynomial vector ﬁeld of degree d. Solving this problem even for the case d = 2 seems to be out of reach
at the present state of knowledge (see [19, 23] for a survey of the recent results on the subject). Arnold [2]
proposed a weaker version of this problem, the so-called inﬁnitesimal Hilbert’s 16th problem. Let ω be a
real 1-form with polynomial coeﬃcients of degree at most d. Consider a real polynomial H of degree d + 1
in the plane. A closed connected component of a level curve H = h is called an oval of H and denoted by
γh. These ovals form continuous families, and the inﬁnitesimal Hilbert’s problem is to ﬁnd an upper bound
V (d) of the number of real zeros of the Abelian integral

I(h) = ∫

γh ω.

The bound must depend on the degree d only, i.e., it should be uniform with respect to the choice of the
polynomial H, the family of ovals {γh} and the form ω. Zeros of Abelian integrals are related to limit cycles
in the following way. Consider a small deformation of a Hamiltonian vector ﬁeld Xε = XH + εY, where

XH = −Hy∂x + Hx∂y and Y = P ∂x + Q∂y.

The ﬁrst approximation in ε of the displacement function of the Poincar´e map of Xε is given by I(h) = ∫

γh ω
with ω = P dy − Qdx. Thus the number of zeros of I(h), counted with multiplicity, provides an upper bound
for the number of ovals of H that generate limit cycles of Xε for ε ≈ 0. The function I(h) can be decomposed
into a linear combination α0I0(h) + α1I1(h) + . . . + αn−1In−1(h)

where each αk depends on the coeﬃcients of P and Q, which are considered as parameters, and each Ik
is an Abelian integral with ω = x
iyjdx or ω = x
iyjdy. Therefore the problem is equivalent to ﬁnding an

1

This is a preprint of: “Computer-assisted techniques for the veriﬁcation of the Chebyshev property
of Abelian integrals”, Jordi-Llu´ıs Figueras, Warwick Tucker, Jordi Villadelprat, J. Diﬀerential
Equations, vol. 254, 2647–3663, 2013.
DOI: [10.1016/j.jde.2013.01.036]

upper bound for the number of isolated zeros of any function in the linear span of I0, I1. . . ,In−1. This is
where the notion of an ECT-system (see Deﬁnition 3.1) comes into play.
In the literature there is an abundance of papers dealing with zeros of Abelian integrals (see for instance
[6, 15, 8, 12, 30, 43] and references therein). In many cases, it is essential to show that a collection of Abelian
integrals has some kind of Chebyshev property. The techniques and arguments to tackle these problems are
usually very long and highly non-trivial. For instance, in some papers (e.g. [5, 17, 31]) the authors study
the geometrical properties of the so-called centroid curve using that it satisﬁes a Riccati equation (which
is itself deduced from a Picard-Fuchs system). In other papers (e.g. [9, 10, 11]), the authors use complex
analysis and algebraic topology (analytic continuation, argument principle, monodromy, Picard-Lefschetz
formula, . . . ). The present paper addresses the applicability of a criterion appearing in [13], which greatly
simpliﬁes the veriﬁcation of the Chebyshev property. Let us brieﬂy explain this criterion.

Suppose that H(x, y) = A(x) + B(x)y2m is an analytic function in some open subset of the plane that
has a local minimum at the origin. Then there exists a punctured neighbourhood P of the origin foliated
by ovals γh ⊂ {H(x, y) = h}. We set H(0, 0) = 0; then the set of ovals γh inside P is parameterized by the
energy levels h ∈ (0, h0) for some positive h0. The projection of P on the x-axis is an interval (xℓ, xr) with
xℓ < 0 < xr. Under these assumptions A has a zero of even multiplicity at x = 0, and it is easy to verify
that there exist an analytic involution σ such that

(1) A(x) = A
(
σ(x)
) for all x ∈ (xℓ, xr).

Recall that a map σ is an involution if σ2 = Id and σ ̸= Id. Given a function κ deﬁned on (xℓ, xr) \ {0},
we deﬁne its σ-balance as Bσ
(
κ)
(x) = κ(x) − κ(
σ(x)
).

Following this notation we can state the result in [13, Theorem B] as follows. In the statement CT-system
stands for complete Chebyshev system, see Deﬁnition 3.1.

Theorem 1.1. Let f0, f1, . . . , fn−1 be analytic functions on (xℓ, xr), and consider the Abelian integrals

Ii(h) = ∫

γh fi(x)y2s−1dx, i = 0, 1, . . . , n − 1.

Let σ be the involution associated to A and deﬁne ℓi := Bσ( fi

A′B 2s−1
2m
 )
. If (
ℓ0, ℓ1, . . . , ℓn−1) is a CT-system

on (0, xr) and s > m(n − 2), then (I0, I1, . . . , In−1) is an ECT-system on (0, h0).

Let us stress, see Deﬁnition 3.1, that the diﬀerence between ECT-system and CT-system is that the ﬁrst
one takes the multiplicity of the zeros into account, while the second does not. Note in particular that an
ECT-system is a CT-system. A collection of functions is an ECT-system if and only if none of the leading
principal minors of its Wronskian vanishes (see Lemma 3.3). Since a CT-system is not so easy to characterize,
when applying Theorem 1.1 we usually check if (
ℓ0, ℓ1, . . . , ℓn−1) is an ECT-system. The applicability of
the criterion comes from the fact that, instead of computing a Wronskian of Abelian integrals, we compute
a Wronskian of almost explicit functions. We say “almost” because σ is deﬁned only implicitly, by means
of the relation in (1). In the polynomial setting, i.e., in case when A, B and fi are polynomials, we can
circumvent this problem by computing resultants. Indeed, in this case, by taking the derivative in (1), we
can express σ(i)(x) in terms of a rational function depending on x and y = σ(x). This in turn enables us
to write the Wronskian of (
ℓ0, ℓ1, . . . , ℓk)
, up to a nonvanishing factor, as Rk(
x, σ(x)
) where Rk(x, y) is a
polynomial. If the Wronskian vanishes at x0 ∈ (0, xr), then the polynomials Rk(x, y) and A(x) − A(y) have
a common zero at (x0, y0) with y0 = σ(x0). Accordingly, to prove that the Wronskian does not vanish, it
suﬃces to show that the resultant of both polynomials, for instance with respect to y, has no zeros on (0, xr).
This can be easily veriﬁed by applying Sturm’s Theorem. This is the approach used in the examples of
application of Theorem 1.1 that appear in [13, Section 4]. All the subsequent papers applying the criterion
deal with the polynomial setting, and follow the same approach (see [3, 4, 14, 21, 24, 36, 37, 38, 40, 41]).

2

Figure 1: Phase portrait of the diﬀerential system (2) in the Poincar´e disc.

The ﬁrst aim of this paper is to show the applicability of Theorem 1.1 in the non-polynomial setting,
and to this end we will rely upon computer-assisted methods based on interval arithmetic, see [35]. In
fact we shall study a problem in which the involved functions are non-algebraic. More precisely, we tackle
the conjecture posed by Dumortier and Roussarie in [7] where the authors consider singular perturbation
problems occurring in planar slow-fast systems depending on parameters. They investigate the number of
limit cycles that appear near a slow-fast Hopf point, i.e., its cyclicity. Their main results (Theorem 1.2,
1.5, and 1.8 in [7]) show that under very general conditions this cyclicity is ﬁnite and, modulo the following
conjecture, provide its precise upper bound.

Conjecture. For each integer i ⩾ 0, let us deﬁne ¯Ji(h) = ∫
γhy2i−1dx, where γh ⊂ {A(x) + B(x)y2 = h}
with A(x) = 1
2 − e−2x(x + 1
2 ) and B(x) = e−2x. Then ( ¯J0, ¯J1, . . . , ¯Jn) is an ECT-system on [
0, 1
2 ) for n ⩾ 0.

The second aim of this paper is to show the validity of the conjecture for n = 0, 1 and 2, i.e., we prove:

Theorem A. ( ¯J0, ¯J1, ¯J2) is an ECT-system on [0, 1
2 )
.

It is important to point out that, although Theorem A does not prove the conjecture for all n, it has
noteworthy implications. Indeed, thanks to Theorem A, by applying [7, Theorem 1.5] one can explicitly
bound the cyclicity of a smooth system with a slow-fast Hopf point of codimension 1 or 2. Similarly, thanks
to Theorem A as well, [7, Theorem 1.8] gives the bound for the cyclicity of an analytic system with a
slow-fast Hopf point of order 1 or 2. One can easily verify that H(x, y) = A(x) + B(x)y2 is a ﬁrst integral
of the planar polynomial diﬀerential system

(2) { ˙x = −y,
˙y = x + y2.

Figure 1 displays its phase portrait in the Poincar´e disc.

Let us outline the proof of Theorem A. First we show, see Corollary 3.5, that ( ¯J0, ¯J1, ¯J2) is an ECT-
system on [0, ε] for some ε > 0. This follows by using analytic arguments that are rather standard. Hav-
ing established this result, we construct a computer-assisted proof of that ( ¯J0, ¯J1, ¯J2) is an ECT-system
on (
0, 1
2 )
. Together, these two results prove Theorem A. Let us brieﬂy explain the approach we follow for
the second result. Since Theorem 1.1 can not be applied directly to the ( ¯J0, ¯J1, ¯J2) because the associated
1-forms do not fulﬁll the assumptions, we show that it is satisﬁed for the functions

h2 ¯Ji(h) = Ji(h) := ∫

γhfi(x)y3dx,

3

where f0, f1 and f2 are the analytic functions given in Lemma 4.2. Then, since m = 1 and s = 2, we
have that ℓi = Bσ( fi
A′B3/2 ) for i = 0, 1, 2. The projection on the x-axis of the family of ovals associated to

H(x, y) = A(x) + B(x)y2 is the interval (xℓ, xr) with xℓ = − 1
2 and xr = +∞, see Figure 1. Thus, according
to Theorem 1.1, it suﬃces to show that (ℓ0, ℓ1, ℓ2) is an ECT-system on (0, xr). As a matter of fact, since σ
is a diﬀeomorphism that maps (0, xr) to (xℓ, 0), these σ-balanced functions form an ECT-system on (0, xr)
if, and only if, they form an ECT-system on (xℓ, 0), see Remark 4.3. For convenience we will show the
latter. To this end, see Lemma 3.3, we must compute the Wronskian of (
ℓ0, ℓ1, ℓ2) and check that none
of its leading principal minors vanish on (xℓ, 0). The ﬁrst order principal minor is ℓ0 and the proof for
this case is completely analytical, see Proposition 4.4. The approach for the two other is analogous, so we
will focus on the third order one for the sake of brevity. It turns out that the functions ℓi are analytic
on (xℓ, 0), meromorphic at x = 0 and not even deﬁned at x = xℓ, so the strategy is to split the interval
into three subintervals, namely I1 = (xℓ, xℓ + ε1), I2 = [xℓ + ε1, −ε2] and I3 = (−ε2, 0), where ε1 and ε2
are positive numbers to be speciﬁed. We ﬁrst quantify them by analyzing the behaviour of the Wronskian
near the endpoints x = − 1
2 and x = 0. This gives us only qualitative results, but combining them with
computer-assisted methods we can specify neighbourhoods of the endpoints, i.e., quantify εi, so that the
Wronskian does not vanish on I1 = (xℓ, xℓ + ε1) and I3 = (−ε2, 0). This is carried out in Lemma 4.9.
Next, once these εi are ﬁxed, we show in Lemma 4.10 that the Wronskian is nonvanishing on I2. Since
the interval is compact, and the Wronskian is analytic, no analytic estimates are required here; standard
computer-assisted techniques can handle the problem. In practice the interval I2 is subdivided into many
small subintervals. On each such subinterval we enclose the range of the Wronskian, and verify that the
range enclosure does not contain zero.
Due to the fact that the proof we present here is a combination of theoretical and computer-assisted
arguments, the proofs stated in this paper are presented using two formats: this written paper and some
computer codes. This written paper contains the theoretical results and the explanations of the theory
behind the computer-assisted proofs. The computer-assisted proofs are presented in separated ﬁles. These
are available from www2.math.uu.se/∼ﬁgueras/preprints/Chebyshev.tar.gz, where there is a com-
pressed ﬁle containing all C codes and a README.txt ﬁle with the speciﬁcations for the compilation and
execution of the codes.

Some words must be said about the implementation of the codes. The interval library we have used is
MPFI, see [33]. This library let us perform rigorous computation with arbitrary precision intervals. This is
important for the validations we present because the functions that we need to evaluate have big oscillations,
and normal interval libraries with only double or long double precision do not suﬃce.
The paper is organized as follows. In Section 2, for reader’s convenience, we make a short description
of the fundamentals of interval arithmetic. In Section 3 we give the deﬁnitions that will be used henceforth
and among other preliminary results we prove that ( ¯J0, ¯J1, . . . , ¯Jn) is an ECT-system on [0, ε] for some
ε > 0. Taking n = 2 shows Theorem A on [0, ε]. Finally in Section 4 we give the proof of Theorem A on
(0, 1
2 ).

2 Computer-assisted proofs and interval analysis

The ability to enclose the range of a given function is a basic feature of set-valued computations. This can
be performed on a computer, and will produce a mathematically guaranteed result, see [35] and references
therein. In what follows, we will brieﬂy describe the fundamentals of interval arithmetic. For a concise
reference on this topic, see e.g. [1, 22, 27, 28]. For early papers on the topic, see [34, 39, 42].
Let IR denote the set of closed intervals of the real line. For any element a ∈ IR, we adapt the notation
a = [a, ¯a]. If ⋆ is one of the operators +, −, ×, ÷, we deﬁne arithmetic operations on elements of IR by

a ⋆ b = {a ⋆ b : a ∈ a, b ∈ b},

4

except that a ÷ b is undeﬁned when 0 ∈ b. Working exclusively with closed intervals, we can describe the
resulting interval in terms of the endpoints of the operands:

a + b = [a + b, ¯a + ¯b]

a − b = [a − ¯b, ¯a − b]
a × b = [min(ab, a¯b, ¯ab, ¯a¯b), max(ab, a¯b, ¯ab, ¯a¯b)]

a ÷ b = a × [1/¯b, 1/b], if 0 /∈ b.

When computing with ﬁnite precision (which we do in computer-assisted proofs), directed rounding must
also be taken into account, see e.g. [22, 28]. It follows immediately from the deﬁnitions that interval addition
and multiplication are both associative and commutative. The distributive law, however, does not always
hold. As an example, we have
 [−1, 1]([−1, 0] + [3, 4]) = [−1, 1][2, 4] = [−4, 4]

whereas [−1, 1][−1, 0] + [−1, 1][3, 4] = [−1, 1] + [−4, 4] = [−5, 5].

This unusual property is important to keep in mind when representing functions as part of a computer
program. Interval arithmetic satisﬁes a weaker rule than the distributive law, which we refer to as sub-
distributivity: a(b + c) ⊆ ab + ac.

Another key feature of interval arithmetic is that it is inclusion monotonic, i.e., if a ⊆ a
′, and b ⊆ b′, then

a ⋆ b ⊆ a
′ ⋆ b′.

It is not hard to extend simple functions to the interval realm. As an example, we may deﬁne the
extension of the exponential function as
 exp(x) = [exp(x), exp(¯x)
].

In general, when we extend a real-valued function f to an interval-valued one F , we demand that it satisﬁes
the inclusion principle Range(f ; x) = {f (x) : x ∈ x} ⊆ F (x).

This is all we need in order to prove that a function (e.g. the Wronskian mentioned above) is nonvanishing
on a closed interval. Indeed, if we have 0 /∈ F (x) then we know that f is non-zero on the domain x.
In order to avoid overestimation of the range, we can use the inclusion monotonicity, and split the
interval into smaller pieces: x = ∪
N
i=1xi. We then have

Range(f ; x) ⊆ ∪
N
i=1F (xi) ⊆ F (
∪
N
i=1xi) = F (x).

For suﬃciently smooth functions, we can make the overestimation of the range arbitrarily small by taking
a suﬃciently ﬁne subdivision of the domain x.
For a complicated function f , we might prefer working with a polynomial approximation p. It is then
important that we can bound the error f − p over the domain of interest. For Taylor expansions, we have
the following enclosure property: If x, ˇx ∈ x then

f (x) ∈ f (ˇx) + f ′(ˇx)(x − ˇx) + · · · + f (n−1)(ˇx)
(n − 1)! (x − ˇx)
n−1 + 1
n! F (n)(x)(x − ˇx)
n.

This means that bounding the range of f (n) over the domain x (e.g. via its interval extension) will provide
a bound on the approximation error. As an example, taking f (x) = sin x and ˇx = 0, we have for all x ∈ R:

sin x ∈ x + [−1, 1] x
3

3! ,

5

which gives good bounds for small x. We can use this type of information to prove statements of the following
kind: “f : [a, b] −→ R is positive on (a, b], and zero at a”. In the case f (x) = sin x and [a, b] = [0, 1], we
have sin x ∈ x − [−1, 1]x
3/3! = x(1 − [−1, 1]x
2/6) ∈ x(1 − [−1, 1]/6) = x[5/6, 7/6]. Thus we get a cone based
at the origin enclosing sin x for all x ∈ [0, 1]. It follows that sin x is positive on (0, 1], and vanishes at the
origin. Naturally, we are interested in more complicated functions f , but the same procedure applies.

3 Deﬁnitions and preliminary results

We give now the deﬁnitions and theoretical results that will be used throughout the paper. In this section
I denotes a real interval with a nonempty interior.

Deﬁnition 3.1 Let f0, f1, . . . , fn−1 be analytic functions on I.

(a) The ordered set of functions (f0, f1, . . . , fn−1) is a complete Chebyshev system (in short, CT-system)
on I if, for all k = 1, 2, . . . , n, any nontrivial linear combination

α0f0(x) + α1f1(x) + . . . + αk−1fk−1(x)

has at most k − 1 isolated zeros on I.

(b) The ordered set of functions (f0, f1, . . . , fn−1) is an extended complete Chebyshev system (in short,
ECT-system) on I if, for all k = 1, 2, . . . , n, any nontrivial linear combination

α0f0(x) + α1f1(x) + . . . + αk−1fk−1(x)

has at most k − 1 isolated zeros on I counted with multiplicity.

(Let us note that in these abbreviations “T” stands for Tchebycheﬀ, which in some sources is the transcrip-
tion of the Russian name Chebyshev.) □

It is clear that if (f0, f1, . . . , fn−1) is an ECT-system on I, then it is a CT-system on I.

Deﬁnition 3.2 Let f0, f1, . . . , fk−1 be analytic functions on I. The Wronskian of (f0, f1, . . . , fk−1) at x ∈ I
is
 W [
f0, f1, · · · , fk−1]
(x) = det (f (i)
j (x)
)
0⩽i,j⩽k−1 =
 ∣
∣
∣
∣
∣
∣
∣
∣
∣
 f0(x) · · · fk−1(x)
f ′
0(x) · · · f ′
k−1(x)
.
f (k−1)
0 (x) · · · f (k−1)
k−1 (x)
 ∣
∣
∣
∣
∣
∣
∣
∣
∣
 .
 □

The next result, see [20, 26], provides an easy characterization of the ECT-systems.

Lemma 3.3. (f0, f1, . . . , fn−1) is an ECT-system on I if and only if for each k = 1, 2, . . . , n,

W [
f0, f1, . . . , fk−1]
(x) ̸= 0 for all x ∈ I.

Note that, although the Abelian integrals ¯Ji(h) are only deﬁned for h ∈ (
0, 1

2 )
, the conjecture of Du-
mortier and Roussarie refers to the interval [0, 1
2 )
. The level curves h = 0 and h = 1
2 are, respectively, a
non-degenerated center and an unbounded polycycle, see Figure 1. We begin by showing that these Abelian
integrals can be analytically extended to h = 0.
 6

Lemma 3.4. For each i ⩾ 0, ¯Ji(h) = hi(
∆i + ℓi(h)
) where ∆i ̸= 0 and ℓi is an analytic function on h = 0
with ℓi(0) = 0.

Proof. The oval γh intersects with the x-axis at two points, x−(h) < 0 < x+(h), which are roots of
A(x) = h. Since A(x) = 1
2 − e−2x(x + 1
2 ) = 1
2 x
2 + o(x
2), the function g(x) := sgn(x)
√A(x) is an analytic
diﬀeomorphism on (xℓ, xr). Moreover x±(h) = g−1(±√
h). Therefore it follows that

¯Ji(h)
hi = 1
hi
 ∫
γh y2i−1dx = 2
hi
 ∫ x+(h)

x−(h)
 ( h − A(x)
B(x)
 )i− 1
2 dx

= 2 ∫ g−1(√h)

g−1(−√
h)
 ( h − A(x)
hB(x)
 )i− 1
2 dx
√
h = 2 ∫ 1

−1
 (
g−1)′(
√
hu)
(
Bi− 1
2 )(
g−1(
√
hu)
) du

(1 − u2) 1
2 −i ,

where in the last equality we perform the coordinate transformation given by g(x) = √
hu and we take
A(x) = g(x)
2 into account. Note at this point that the function

F (z) :=
 (
g−1)′(z)
(
Bi− 1
2 )(
g−1(z)
)

is analytic at z = 0. Let F (z) = ∑n⩾0 αnzn be its Taylor series at z = 0. Then

¯Ji(h)
hi = 2 ∫ 1

−1
 ∞∑

n=0 αnhn/2 undu

(1 − u2) 1
2 −i = 2
 ∞∑

n=0 α2nhn ∫ 1

−1
 u2ndu

(1 − u2) 1
2 −i ,

and this proves the analyticity of ¯Ji(h) at h = 0. In addition, since g′(0) = 1√
2 and B(0) = 1, we get that

lim
h−→0
 ¯Ji(h)
hi = 2√
2 ∫ 1

−1
 du

(1 − u2) 1
2 −i = 2√
2π Γ(i + 1
2 )
Γ(i + 1) =: ∆i,

where Γ is the Gamma function. This completes the proof of the result.

Corollary 3.5. For each n ⩾ 0 there exists ε > 0 such that ( ¯J0, ¯J1, . . . , ¯Jn) is an ECT-system on [0, ε].

Proof. For each integer i ⩾ 0, we will say that a function f belongs to the set Ri if f (x) = x
is(x) with s
being any analytic function at x = 0 with s(0) ̸= 0. Note in particular that if f ∈ R0, then f (0) ̸= 0. In
addition one can easily verify that if g ∈ Ri and h ∈ Rj with i > j, then ( g
h )′ ∈ Ri−j−1.

According to this notation Lemma 3.4 shows that ¯Ji ∈ Ri for all i ⩾ 0. Fix k such that 0 ⩽ k ⩽ n and
consider any function ℓ in the linear span of ¯J0, ¯J1, . . . , ¯Jk, i.e.,

ℓ(h) = α0 ¯J0(h) + α1 ¯J1(h) + . . . + αk ¯Jk(h),

for some α0, α1, . . . , αk ∈ R. For the sake of convenience, let us rewrite the above equality as

ℓ0 = α0J 0
0 + α1J 0
1 + . . . + αkJ 0
k .

Since J 0
0 ∈ R0, there exists ε0 > 0 such that J 0
0 (h) ̸= 0 for all h ∈ [−ε0, ε0]. This enables us to perform the
ﬁrst step of the division-derivation algorithm,

ℓ1 := ( ℓ0

J 0
0
 )′ = α1
 ( J 0
1
J 0
0
 )′ + α2
 ( J 0
2
J 0
0
 )′ + . . . + αk
 ( J 0
k
J 0
0
 )′ .

7

Given any analytic function f , let us denote the number of zeros of f on the interval [−δ, δ] counted with
multiplicity by Z(f, δ). Thus by applying Rolle’s Theorem we can assert that Z(ℓ0, ε0) ⩽ Z(ℓ1, ε0) + 1.

Note moreover that J 1
i := ( J 0
i
J 0
0
 )′ ∈ Ri−1. Therefore, since J 1
1 (h) ̸= 0 for all h ∈ [−ε1, ε1] with 0 < ε1 < ε0,
we can perform the second step of the division-derivation algorithm to obtain

ℓ2 := ( ℓ1

J 1
1
 )′ = α2
 ( J 1
2
J 1
1
 )′ + α3
 ( J 1
3
J 1
1
 )′ + . . . + αk
 ( J 1
k
J 1
1
 )′ ,

so that Z(ℓ0, ε1) ⩽ Z(ℓ2, ε1)+2. As before, J 2
i := ( J 1
i
J 1
1
 )′ ∈ Ri−2 and this allows us to perform the next step of
the division-derivation algorithm. Following the obvious notation, in the kth step of the division-derivation
algorithm we get
 ℓk :=
 ( ℓk−1

J k−1
k−1
 )′
 = αk
 ( J k−1
k
J k−1
k−1
 )′
 ,

with J k
k := ( J k−1
k
J k−1
k−1
 )′ ∈ R0. Thus ℓk does not vanish on [−εk, εk] with 0 < εk < εk−1 and, on the other hand,

Z(ℓ0, εk−1) ⩽ Z(ℓk, εk−1) + k. Note that ε0, ε1, . . . , εk only depend on ¯J0, ¯J1, . . . , ¯Jk. In particular they do
not depend on ℓ and so, due to Z(ℓk, εk) = 0, this shows that any function in the linear span of ¯J0, ¯J1, . . . , ¯Jk
has at most k zeros on [0, εk] counted with multiplicity. Accordingly the result follows by taking ε = εn.

The proof of the following result can be found in [18, 32].

Lemma 3.6. Let f0, f1, . . . , fn be analytic functions on I such that W [f0, . . . , fn−2, fn−1] is nonvanishing.
Then it holds that ( W [f0, . . . , fn−2, fn]
W [f0, . . . , fn−2, fn−1]
 )′ = W [f0, . . . , fn] W [f0, . . . , fn−2]
(W [f0, . . . , fn−2, fn−1])2 .

The authors in [7] state their conjecture in terms of a deﬁnition of ECT-system (cf. [7, Deﬁnition 7.4])
which is diﬀerent from Deﬁnition 3.1. For the sake of completeness we conclude the present section by
showing the equivalence between both deﬁnitions.

Lemma 3.7. (f0, f1, . . . , fn−1) is an ECT-system on I if and only if one can construct inductively the
sequence F 1, F 2, . . . , F n−1 with F k = {f k
k , f k
k+1, . . . , f k
n−1} such that:

(a) Setting f 1
i := fi
f0 for i = 1, 2, . . . , n − 1, the functions

f k+1
i :=
 (
f k
i )′
(
f k
k )′ for k = 1, 2, . . . , n − 1 and i = k + 1, . . . , n − 1,

are analytic on I, and

(b) f0 and (
f k
k )′, for k = 1, 2, . . . , n − 1, do not vanish on I.

Proof. By applying Lemma 3.6, on account of (f 1
i )
′ = ( fi
f0
 )′ = W [f0,fi]
W [f0]2 , it turns out that

(
f 2
i )′ =
 ( (
f 1
i )′
(
f 1
1 )′
 )′ = ( W [f0, fi]
W [f0, f1]
 )′ = W [f0, f1, fi] W [f0]
W [f0, f1]2 .

Consequently, by Lemma 3.6 again,

(
f 3
i )′ =
 ( (
f 2
i )′
(
f 2
2 )′
 )′
 = ( W [f0, f1, fi]
W [f0, f1, f2]
 )′ = W [f0, f1, f2, fi] W [f0, f1]
W [f0, f1, f2]2 .

8

Thus, by applying Lemma 3.6 as before, for an arbitrary k we obtain

(
f k
i )′ =
 ( (
f k−1
i )′
(
f k−1
k−1 )′
 )′
 = ( W [f0, f1, . . . , fk−2, fi]
W [f0, f1, . . . , fk−1]
 )′ = W [f0, f1, . . . , fk−1, fi] W [f0, f1, . . . , fk−2]
W [f0, f1, . . . , fk−1]2 .

Now, taking these equalities with i = k, the result follows from Lemma 3.3.

4 Proof of the Theorem A on (
0, 1
2)

The Abelian integrals ¯J0, ¯J1 and ¯J2 deﬁned in Section 1 do not fulﬁll the hypothesis in Theorem 1.1. We
shall use the next result, which follows from [13, Lemma 4.1], to obtain another set of Abelian integrals
with the desired structure.

Lemma 4.1. Let γh be an oval inside the level curve {A(x) + B(x)y2 = h}.

(a) If F/A
′ is analytic on (xℓ, xr), then
∫

γhF (x)yk−2dx = ∫

γh UF (x)ykdx where UF = 2
k Bk/2 ( F B1−k/2
A′ )′.

(b) If G is analytic on (xℓ, xr), then
∫

γh G(x)ykdx = ∫

γh DG(x)yk−2dx where DG = k
2 A
′B k
2 −1∫ GB −k
2 dx.

By applying the previous result we can now prove:

Lemma 4.2. For i = 0, 1, 2, ¯Ji(h) = 1
h2
 ∫

γhfi(x)y3dx, where

f0(x) = 1
12x4
 (
(32x
4 + 12x
3 + 15x
2 + 7x + 3)e−4x + (8x
3 − 6x
2 − 2x − 6)e−2x + 3x
2 − 5x + 3)
,

f1(x) = 1
12x2
 (
(32x
3 − 12x
2 − x − 1)e−4x + (8x
2 − 2x + 2)e−2x + 3x − 1)
,

f2(x) = 1
12
 (
(32x
2 − 68x + 3)e−4x + (8x − 6)e−2x + 3)
.

Proof. For convenience, let us deﬁne I(h) = a ¯J0(h) + b ¯J1(h) + c ¯J2(h). Then

h2I(h) = ∫

γh
(
A(x) + B(x)y2)2 ( a
y + by + cy3) dx = ∫

γh
( 4∑

i=0 gi(x)y2i−1)
 dx,

where g0 := aA
2, g1 := A(2aB + bA), g2 := aB2 + 2bAB + cA
2, g3 := B(bB + 2cA) and g4 := cB2. Now, by
applying Lemma 4.1 with {F = g0, k = 1} and {G = g4, k = 7} we get

h2I(h) = ∫

γh
(ˆg1y + g2y3 + ˆg3y5)
dx,

where ˆg1 := g1 + Ug0 and ˆg3 := g3 + Dg4 . Next, by Lemma 4.1 again, in this case taking {F = ˆg1, k = 3}
and {G = ˆg3, k = 5}, we obtain

h2I(h) = ∫

γh ˆg2y3dx, where ˆg2 := g2 + Uˆg1 + Dˆg3 .

9

(Let us point out that g0/A
′ and ˆg1/A
′ are analytic because one can verify that g0 and ˆg1 vanish at x = 0,
so that we can apply (a) in Lemma 4.1). Finally some computations show that ˆg2 = af0 + bf1 + cf2 with
the functions given in the statement. This proves the result.

Remark 4.3 Consider the functions f0, f1 and f2 in the statement of Lemma 4.2. Then h2 ¯Ji(h) = Ji(h),
where
 Ji(h) := ∫

γhfi(x)y3dx for i = 0, 1, 2.

Hence ( ¯J0, ¯J1, ¯J2) is an ECT-system on (0, h0) if and only if (J0, J1, J2) is an ECT-system on (0, h0). Setting
gi := fi
A′B3/2 for i = 0, 1, 2, the latter will follow by Theorem 1.1 once we show that (
Bσ(g0), Bσ(g1), Bσ(g2)
)

is an ECT-system on (0, xr).

Note on the other hand that if ϕ : I −→ J is a diﬀeomorphism, then (
f0, f1, . . . , fn−1) is an ECT-system
on J if and only if (
f0 ◦ ϕ, f1 ◦ ϕ, . . . , fn−1 ◦ ϕ
) is an ECT-system on I. Consequently, since σ is maps (0, xr)
to (xℓ, 0) and Bσ(gi ◦ σ) = −Bσ(gi), for convenience we shall verify that (
Bσ(g0), Bσ(g1), Bσ(g2)
) is an
ECT-system on (xℓ, 0). On account of Lemma 3.3 this is equivalent to showing that all the leading principal
minors of its Wronskian are nonvanishing on (xℓ, 0). Setting ℓi = Bσ(gi) for the sake of shortness, the rest
of the section is devoted to prove this. □

Proposition 4.4. ℓ0 is nonvanishing on (− 1
2 , 0).

Proof. We claim that xg0(x) > 0 for all x ∈ (− 1
2 , +∞). Recall that g0 = f0
A′B3/2 where, for the sake of
convenience, we rewrite the numerator as f0(x) = n(x)
12x4e2x with

n(x) = (32x
4 + 12x
3 + 15x
2 + 7x + 3)e−2x + (3x
2 − 5x + 3)e2x + 8x
3 − 6x
2 − 2x − 6.

On account of xA
′(x) > 0, the claim will follow if we show that f0 is positive on (− 1
2 , +∞). To this end let
us ﬁrst note that n(x) = 32x
4 − 164
3 x
5 + o(x
5), so that n has a zero of multiplicity four at x = 0. By applying
Sturm’s Theorem we can assert that p(x) = 32x
4 + 12x
3 + 15x
2 + 7x + 3 has no real zeros. Consequently,
the function κ(x) = n(x)
p(x)e−2x is well deﬁned and has exactly the same roots, counted with multiplicity, as n.
One can verify that
 κ′(x) = 4xs(x)
p(x)2e−2x ,

where s(x) = q0(x) + q1(x)e2x with q0(x) = 128x
6 − 112x
5 + 88x
4 − 29x
3 + 172x
2 + 8x + 12 and q1(x) =
96x
5 − 172x
4 + 192x
3 − 84x
2 + 16x − 12. By Sturm’s Theorem again it follows that q0 does not vanish, so
that t(x) = s(x)
q0(x) is well deﬁned. Moreover by Rolle’s Theorem the function n has at most two more zeros,
counted with multiplicity, than t. A computation shows that

t′(x) = 4xe2xp(x)r(x)
q0(x)2 ,

where r(x) = 192x
6 − 680x
5 + 1326x
4 − 1665x
3 + 1541x
2 − 735x + 192.

Since by Sturm’s Theorem once again, r does not vanish, by applying Rolle’s Theorem it follows that t
has at most two real zeros, counted with multiplicity. Accordingly, n has at most four real zeros counted
with multiplicity. Since n(x) = 32x
4 − 164
3 x
5 + o(x
5), this implies that f0(x) > 0 for all x ∈ R, so the
claim is true. Finally, taking the claim into account, since σ(x) > 0 for all x ∈ (− 1
2 , 0), it turns out that
g0(
σ(x)
) > 0 > g0(x) for all x ∈ (− 1
2 , 0). Thus Bσ(
g0)
(x) = g0(x) − g0(
σ(x)
) < 0 for all x ∈ (− 1
2 , 0), and
this completes the proof.
 10

To prove that W [ℓ0, ℓ1] and W [ℓ0, ℓ1, ℓ2] do not vanish on (xℓ, 0) we follow the same strategy. As we
explain in Section 1, we divide (xℓ, 0) in three subintervals, namely I1 = (xℓ, xℓ + ε1), I2 = [xℓ + ε1, −ε2]
and I3 = (−ε2, 0). In the proof for I1 and I3 we perform a combination of asymptotic analysis with rigorous
quantitative computer-assisted proofs, whereas for I2 we use a rather standard computer-assisted technique.
Indeed, since the functions ℓi are analytic on (xℓ, 0), we can rigorously enclose the range of the Wronskian
on small subintervals, and verify that it is nonvanishing. For the sake of brevity we shall only give in full
the proof for W [ℓ0, ℓ1, ℓ2] because the proof for W [ℓ0, ℓ1] follows exactly the same lines. To this end we
begin by proving some lemmas that provide upper and lower bounds of the involution σ, which recall that
is deﬁned by means of A(x) = A
(
σ(x)
) with A(x) = 1
2 − e−2x(x + 1
2 ).

Lemma 4.5. Deﬁne sup(x) = √ 2e2x
2x+1 − 2 and inf(x) = x − 1
2 log(2x + 1). Then 0 < inf(x) < σ(x) < sup(x)

for all x ∈ (− 1
2 , 0).

Proof. Let us ﬁrst note that f (x) < A(x) < g(x) for all x > 0 with f (x) := x2
2x2+4 and g(x) := 1
2 e−2x. Hence
f (
σ(x)
) < A
(
σ(x)
) = A(x) < g(
σ(x)
) for all x ∈ (− 1
2 , 0). Thus, since f and g are monotonous increasing
on (0, +∞), this implies inf(x) := g−1(
A(x)
) < σ(x) < f −1(
A(x)
) =: sup(x) for all x ∈ (− 1
2 , 0).

Lemma 4.6. Deﬁne f (z, x) = 2(x − z) + log(2z + 1) − log(2x + 1) and ﬁx x0 ∈ (− 1
2 , 0). If f (z0, x0) is
positive (respectively, negative) then z0 > σ(x0) (respectively, σ(x0) > z0).

Proof. Clearly, σ(x0) > 0. In addition, since A is monotonous increasing on (0, +∞), note that σ(x0) < z0
if, and only if, A
(
σ(x0)
) < A(z0). By deﬁnition this inequality writes as A(x0) < A(z0), which taking
logarithms is equivalent to f (z0, x0) > 0. The other assertion follows from the same type of arguments.

Let us point out that, in the statement of the following result, µ is an interval-valued function.

Lemma 4.7. Deﬁne µ(x) = −x + [1, 5
3 ]x
2 and I3 = (−0.1, 0). Then σ(I) ⊂ µ(I) for every interval I ⊂ I3.

Proof. Setting a1 = 1 and a2 = 5
3 , let us deﬁne σi(x) := −x + aix
2. Then, by Lemma 4.6 it suﬃces to
prove that f (σ1(x), x) > 0 and f (σ2(x), x) < 0 for all x ∈ I3. Both inequalities can be proved by means of
elementary analytic arguments. Let us show the second one for instance. Some computations show that

g(x) := f (
σ2(x), x
) = 4x − 10
3 x
2 + log ( 10x
2 − 6x + 3
6x + 3
 ) ,

and we can assert that g(x) < 0 for all x ∈ I3 because g(0) = 0 and its derivative, which is given by

g′(x) = 4x
2 (
9 + 70x − 100x
2)

3 (2x + 1) (3 − 6x + 10x2) ,

is positive for x ∈ I3. The ﬁrst inequality follows exactly the same way and holds in fact on (− 1
2 , 0).

We shall also use the so-called Fujiwara’s bound (see for instance [25]).

Lemma 4.8 (Fujiwara). The roots of the polynomial p(z) = c0 + c1z + . . .+ cnzn, with cn ̸= 0, have modulus
smaller than
 2 max
 {∣
∣
∣
∣ cn−1
cn
 ∣
∣
∣
∣ , ∣
∣
∣
∣ cn−2
cn
 ∣
∣
∣
∣
 1
2 , . . . , ∣
∣
∣
∣ c1
cn
 ∣
∣
∣
∣
 1
n−1 , ∣
∣
∣
∣ c0
2cn
 ∣
∣
∣
∣
 1
n }
 .

Lemma 4.9. W [ℓ0, ℓ1, ℓ2] is a nonvanishing on I1 = (− 1
2 , − 1
2 + 10−23) and I3 = (−0.1, 0).

11

Proof. Some straight-forward computations show that

(3) W [ℓ0, ℓ1, ℓ2](x) = D(
x, ex, σ(x), eσ(x))

2933x12e6xσ(x)15 ,

with D being a polynomial. We set y = ex, z = σ(x) and w = eσ(x). Then A(x) = A
(
σ(x)
) writes as

2x + 1
y2 = 2z + 1
w2 .

Taking this relation into account and introducing u = √
z + 1
2 we obtain

(4) D(x, y, z, w) = D
 (

x, y, z,
 √ 2z + 1
2x + 1 y
)
 = D
 

x, y, u2 − 1
2 , uy
√
x + 1
2
 

 = S(x, y, u)

(x + 1
2 ) 21
2 ,

where S(x, ex, u) = ∑33
i=0 ai(x)ui with the functions ai continuous at x = − 1
2 . One can check that ai(− 1
2 ) = 0
for i = 28, 29, . . . , 33. More precisely

(5) lim
x−→− 1
2
 ai(x)
(x + 1/2)ni = ∆i,

where n33 = n31 = n29 = 6, n32 = n30 = n28 = 5
2 , and

∆33 < 0, ∆32 > 0, ∆31 > 0, ∆30 < 0 ∆29 < 0 and ∆28 > 0.

In addition, a27(− 1
2 ) = 27
16
 √ 2
e21 . By continuity there exists ε0 > 0 such that if x ∈ (− 1
2 , − 1
2 + ε0), then

∆iai(x) > 0 for i = 28, 29, . . . , 33. By applying Lemma 4.5, if we deﬁne ω(x) := (
sup(x) + 1
2 )1/2, then it
follows that 1√
2 < u < ω(x) for all x ∈ (− 1
2 , 0). Thus, setting

ˆa27 := a27 + a28√
2 + a29ω2 + a30ω3 + a31
4 + a32
4√
2 + a33ω6,

we can assert that

(6) S(x, ex, u) >
 26∑

i=0 ai(x)ui + ˆa27(x)u27

for all x ∈ (− 1
2 , − 1
2 + ε0). Moreover, from (5), ˆa27(x) is continuous at x = − 1
2 , and

lim
x−→− 1
2 ˆa27(x) = a27 (−1/2) = 27
16
 √ 2
e21 .

By continuity, there exist ε1 > 0 such that if x ∈ (− 1
2 , − 1
2 + ε1), then ˆa27(x) > m > 0. Consequently, for
each x ∈ (− 1
2 , − 1
2 +ε1), we have that S(x, ex, u) tends to +∞ as u −→ +∞, and so S(x, ex, u) > 0 for u > R
with R big enough. To quantify it we ﬁx x and apply Lemma 4.8 to the polynomial in u on the right-hand
side of the inequality (6). We ﬁrst verify, using CAP techniques, that we can take ε0 = ε1 = 5 × 10−4. Using
CAP methods again we prove that

max
 {∣
∣
∣
∣ a26(x)
ˆa27(x)
 ∣
∣
∣
∣ , ∣
∣
∣
∣ a25(x)
ˆa27(x)
 ∣
∣
∣
∣
 1
2 , . . . , ∣
∣
∣
∣ a0(x)
2ˆa27(x)
 ∣
∣
∣
∣
 1
27 }
 < 2.6 for all x ∈ (− 1
2 , − 1
2 + ε1).

12

We obtain in this way R = 5.2. From (4), taking z = u2 − 1
2 into account, this shows that

D
 (
x, ex, z,
 √ 2z + 1
2x + 1 ex)
 > 0 for x ∈ (− 1
2 , − 1
2 + ε1) and z > 26.54.

Finally, since z = σ(x), it suﬃces to ﬁnd ε2 < 5 × 10−4 such that if x ∈ (− 1
2 , − 1
2 + ε2), then σ(x) > 26.54.
Taking ε2 = 10−23 the result follows from the fact that A(− 1
2 + ε2) > A(26.54), which has been checked by
computing a rigorous enclosure using computer interval arithmetic. In short, W [ℓ0, ℓ1, ℓ2] is nonvashing on
I1 = (− 1
2 , − 1
2 + 10−23).

Finally let us prove that W [ℓ0, ℓ1, ℓ2] is nonvashing on I3 = (−0.1, 0). To this end recall ﬁrst that, on
account of Lemma 4.7, we have σ(I) ⊂ µ(I) for every interval I ⊂ I3, where µ(x) = −x + [1, 5
3 ]x
2. Since in
addition ex ∈ 1 + x + 1
2 eI3 x
2 and eσ(x) ∈ eµ(x) ⊂ 1 + µ(x) + 1
2 eµ(I3)µ(x)
2 for all x ∈ I3, from (3) it follows
that it suﬃces to verify that the range of the interval-valued function

h(x) := D (
x, 1 + x + 1
2 eI3x
2, µ(x), 1 + µ(x) + 1
2 eµ(I3)µ(x)
2)

does not contain the zero. Some computations show that h(x) = x
3 ˆp(x), where ˆp is a polynomial of degree
66 with interval coeﬃcients. By computing a rigorous enclosure of the range of ˆp by means of computer
interval arithmetic we can assert that ˆp
(
[−0.1, 0]) ⊂ [1.677298 × 10−61, 1.308564 × 1015], and this proves
that 0 /∈ h(I3) as desired. This completes the proof of the result.

Concerning the proof of Lemma 4.9, let us note that the inclusion ˆp(
[−0.1, 0]) ⊂ (0, +∞) is obtained by
the branch and bound method, i.e., given an initial interval, in our case [−0.1, 0], we subdivide it in smaller
subintervals (branching) and check that ˆp is positive in each one (bound). This is done recursively (see [29]
for details about this method).

Lemma 4.10. W [ℓ0, ℓ1, ℓ2] is a nonvanishing on I2 = [− 1
2 + 10−23, −0.1].

Proof. This proof strongly relies on the rigorous evaluation of W [ℓ0, ℓ1, ℓ2] on I2 using interval arithmetic
in a computer. The procedure goes as follows:
First, given any x0 ∈ (− 1
2 , 0), the combination of Lemmas 4.5 and 4.6 enables us to compute a rigorous
interval enclosure of σ(x0). Indeed, on account of Lemma 4.5, we obtain an initial approximation interval
L0 = [
inf(x0), sup(x0)
] that contains σ(x0). Then, by applying Lemma 4.6 we perform an iterative bisection
process starting with L0 that consists in bisecting the previous approximation interval and checking the
sign of z ↦−→ f (z, x0) at its midpoint to decide which half contains σ(x0).
Second, given an interval [a, b] ⊂ (− 1
2 , 0), by using the fact that the involution σ is decreasing, we can
compute a rigorous enclosure of σ([a, b]) = [σ(b), σ(a)] by applying the previous paragraph.

Third, we split the interval I2 in two subintervals, namely I21 = [− 1
2 + 10−23, −0.4999999] and I22 =
[−0.4999999 − 10−10, −0.1]. In the interval I21 we apply the branch and bound method while checking that

the rigorous interval enclosures of S (x, ex, √
σ(x) + 1
2 ) in equation (4) do not contain the zero. In the
interval I22 we do the same but, instead of evaluating S, we evaluate the entries of the matrix that deﬁnes
the Wronskain W [ℓ0, ℓ1, ℓ2], and next we compute its determinant.

In the proof of Lemma 4.10 we use two diﬀerent (but equivalent) expressions for the evaluation of the
Wronskain W [ℓ0, ℓ1, ℓ2]. This is so because mathematically equivalent expressions may lead to diﬀerent
results due to the fact that the computations are done using ﬂoating point interval arithmetic. To be more
precise let us denote by E1 the expression used in the interval I21, and by E2 the one in I22. It occurs that
the evaluation of E2 is faster (in computational time) than the evaluation of E1. Hence, ideally it would be
better to use E2 combined with the branch and bound method. However, since E2 has bigger slope than E1
on I21, the branch and bound method needs to split I21 in tiny intervals, which leads to worse performance
in computational time compared with E2.
 13

Remark 4.11 The computations for the proof of Lemma 4.10 take ca six and a half hours on a desktop
computer with a 2.8GHz CPU. □

On account of Lemmas 4.9 and 4.10 we have the following result.

Proposition 4.12. W [ℓ0, ℓ1, ℓ2] is a nonvanishing on (
− 1
2 , 0)
.

To show that the second order leading principal minor of the Wronskian does not vanish we follow
exactly the same approach as in the proof of the third order one. Thus, for the sake of shortness, we do not
include here the proof of the following two lemmas, that we have proved with the help of computer-assisted
methods.

Lemma 4.13. W [ℓ0, ℓ1] is a nonvanishing on I1 = (− 1
2 , − 1
2 + 10−23) and I3 = (−0.1, 0).

Lemma 4.14. W [ℓ0, ℓ1] is a nonvanishing on I2 = [− 1
2 + 10−23, −0.1].

By the combination of Lemmas 4.13 and 4.14 we obtain the following result.

Proposition 4.15. W [ℓ0, ℓ1] is a nonvanishing on (
− 1
2 , 0)
.

We are now in position to ﬁnish the proof of Theorem A.

Proof of Theorem A. By applying Corollary 3.5 we can assert that there exists ε > 0 such that ( ¯J0, ¯J1, ¯J2)

is an ECT-system on [0, ε]. In order to prove it on (0, 1
2 ), recall Remark 4.3, it suﬃces to show that none
of the leading principal minors of the Wronskian of (ℓ0, ℓ1, ℓ2) vanish on (
− 1
2 , 0)
. This follows from Propo-
sitions 4.4, 4.12 and 4.15. Accordingly, on account of the characterization in Lemma 3.3, we conclude that( ¯J0, ¯J1, ¯J2) is an ECT-system on [0, 1
2 ) and this completes the proof of the result.

References

[1] G. Alefeld and J. Herzberger, “Introduction to Interval Computations”, Academic Press, New York,
1983.

[2] V.I. Arnold, “Arnold’s problems”, Springer-Verlag, Berlin, 2004.

[3] A. Atabaigi and H. Zangeneh, Bifurcation of limit cycles in small perturbations of a class of hyper-
ellitptic Hamiltonian systems of degree 5 with a cusp, J. Appl. Anal. Comput. 1 (2011), 299–313.

[4] Long Chen, Xianzhong Ma, Gemeng Zhang and Chengzhi Li, Cyclicity of several quadratic reversible
systems with center of genus one, J. Appl. Anal. Comput. 1 (2011), 439–447.

[5] F. Dumortier, Chengzhi Li and Zifen Zhang, Unfolding of a quadratic integrable system with two centers
and two unbounded heteroclinic loops, J. Diﬀerential Equations 139 (1997), 146–193.

[6] F. Dumortier and R. Roussarie, Abelian integrals and limit cycles, J. Diﬀerential Equations 227 (2006),
116–165.

[7] F. Dumortier and R. Roussarie, Birth of canard cycles, Discrete Contin. Dyn. Syst. 2 (2009), 723–781.

[8] A. Gasull, Weigu Li, J. Llibre and Zhifen Zhang, Chebyshev property of complete elliptic integrals and
its application to Abelian integrals, Paciﬁc J. Math. 202 (2002), 341–361.

[9] S. Gautier, L. Gavrilov and I. Iliev, Perturbations of quadratic centers of genus one, Discrete Contin.
Dyn. Syst. 25 (2009), 511–535.
 14

[10] L. Gavrilov, The inﬁnitesimal 16th Hilbert problem in the quadratic case, Invent. Math. 143 (2001),
449–497.

[11] L. Gavrilov and I. Iliev, Bifurcations of limit cycles from inﬁnity in quadratic systems, Canad. J. Math.
54 (2002), 1038–1064.

[12] L. Gavrilov and I. Iliev, Two-dimensional Fuchsian systems and the Chebyshev property, J. Diﬀerential
Equations 191 (2003), 105–120.

[13] M. Grau, F. Ma˜nosas and J. Villadelprat, A Chebyshev criterion for Abelian integrals, Trans. Amer.
Math. Soc. 363 (2011), 109–129.

[14] M. Grau and J. Villadelprat, Bifurcation of critical periods from Pleshkan’s isochrones, J. Lond. Math.
Soc. 81 (2010), 142–160.

[15] Maoan Han, Existence of at most 1, 2, or 3 zeros of a Melnikov function and limit cycles, J. Diﬀerential
Equations 170 (2001), 325–343.

[16] D. Hilbert, Mathematische Problem (lecture), Second Internat. Congress Math. Paris 1900, Nachr. Ges.
Wiss. Gottingen Math.-Phys. Kl. 1900, 253–297.

[17] E. Horozov and I. Iliev, On the number of limit cycles in perturbations of quadratic Hamiltonian systems,
Proc. London Math. Soc. 69 (1994), 198–224.

[18] L. A. Howland, Note on the derivative of the quotient of two Wronskians, Amer. Math. Monthly 28
(1911), 219–221.

[19] Yu. Ilyashenko, Centennial history of Hilbert’s 16th problem, Bull. Amer. Math. Soc. (N.S.) 39 (2002),
301–354.

[20] S. Karlin and W. Studden, “Tchebycheﬀ systems: with applications in analysis and statistics”, Inter-
science Publishers, 1966.

[21] R. Kazemi, H. Zangeneh and A. Atabaigi, On the number of limit cycles in small perturbations of a
class of hyper-elliptic Hamiltonian systems, Nonlinear Anal. 75 (2012), 574–587.

[22] U.W. Kulisch and W.L. Miranker, “Computer Arithmetic in Theory and Practice”, Academic Press,
1981.

[23] Jibin Li, Hilbert’s 16th problem and bifurcations of planar polynomial vector ﬁelds, Internat. J. Bifur.
Chaos Appl. Sci. Engrg. 13 (2003), 47–106.

[24] F. Ma˜nosas and J. Villadelprat, Bounding the number of zeros of certain Abelian integrals, J. Diﬀerential
Equations 251 (2011), 1656–1669.

[25] M. Marden, “Geometry of polynomials”, Mathematical Surveys, No. 3, American Mathematical Society,
1966.

[26] M. Mazure, Chebyshev spaces and Bernstein bases, Constr. Approx. 22 (2005), 347–363.

[27] R.E. Moore, “Interval Analysis”, Prentice-Hall, Englewood Cliﬀs, New Jersey, 1966.

[28] R.E. Moore, “Methods and Applications of Interval Analysis”, SIAM Studies in Applied Mathematics,
Philadelphia, 1979.

[29] A. Neumaier, Complete search in continuous global optimization and constraint satisfaction, Acta Nu-
mer. 13 (2004), 271–369.
 15

[30] G. Petrov, The Chebyshev property of elliptic integrals, Funct. Anal. Appl. 22 (1988), 72–73.

[31] Lin Ping Peng, Unfolding of a quadratic integrable system with a homoclinic loop, Acta Math. Sin. 18
(2002), 737–754.

[32] G. Polya, On the mean-value theorem corresponding to a given linear homogeneous diﬀerential equation,
Trans. Amer. Math. Soc. 24 (1922), 312–324.

[33] N. Revol and F. Rouillier, Motivations for an arbitrary precision interval arithmetic and the MPFI
library, Reliab. Comput. 11 (2005), 275–290.

[34] T. Sunaga, Theory of an interval algebra and its application to numerical analysis, Res. Assoc. Appl.
Geom. Mem. 2 (1958), 29–46.

[35] W. Tucker, “Validated numerics: A short introduction to rigorous computations.” Princeton University
Press, Princeton, NJ. (2011).

[36] N. Wang, J. Wang and D. Xiao, The exact bounds on the number of zeros of complete hyperelliptic
integrals of the ﬁrst kind, J. Diﬀerential Equations (2012), http://dx.doi.org/10.1016/j.jde.2012.07.011

[37] J. Wang, Estimate of the number of zeros of Abelian integrals for a perturbation of hyperelliptic Hamil-
tonian system with nilpotent center, Chaos Solitons Fractals 45 (2012), 1140–1146.

[38] J. Wang and D. Xiao, On the number of limit cycles in small perturbations of a class of hyper-elliptic
Hamiltonian systems with one nilpotent saddle, J. Diﬀerential Equations 250 (2011), 2227–2243.

[39] M. Warmus, Calculus of approximations, Bull. Acad. Polon. Sci. Cl. III 4 (1956), 253-257.

[40] Kuilin Wu and Yulin Zhao, On the number of zeros of Abelian integral for a cubic isochronous center,
Internat. J. Bifur. Chaos Appl. Sci. Engrg. 22 (2012) 1250016 (9 Pages).

[41] Kuilin Wu and Yulin Zhao, The cyclicity of the period annulus of the cubic isochronous center, Ann.
Mat. Pura Appl. 191 (2012), 459–467.

[42] R. C. Young, The algebra of multi-valued quantities, Math. Ann. 104 (1931), 260–290.

[43] Yulin Zhao, Zhaojun Liang and Gang Lu, The cyclicity of the period annulus of the quadratic Hamil-
tonian systems with non-Morsean point, J. Diﬀerential Equations 162 (2000), 199–223.

16
