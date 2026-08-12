<!-- source: https://arxiv.org/pdf/0909.4036 | converted from PDF -->

arXiv:0909.4036v2  [nlin.AO]  10 Jun 2010
Kinetic theory and Lax equations for shock
clustering and Burgers turbulence

Govind Menon
1 and Ravi Srinivasan
2

May 29, 2018

Abstract

We study shock statistics in the scalar conservation law ∂tu+∂xf (u) =
0, x ∈ R, t > 0, with a convex ﬂux f and spatially random initial data. We
show that the Markov property (in x) is preserved for a large class of ran-
dom initial data (Markov processes with downward jumps and derivatives
of L´evy processes with downward jumps). The kinetics of shock clustering
is then described completely by an evolution equation for the generator
of the Markov process u(x, t), x ∈ R. We present four distinct derivations
for this evolution equation, and show that it takes the form of a Lax pair.
The Lax equation admits a spectral parameter as in [35], and has remark-
able exact solutions for Burgers equation (f (u) = u
2/2). This suggests
the kinetic equations of shock clustering are completely integrable.

MSC classiﬁcation: 60J75, 35R60, 35L67, 82C99

Keywords: Shock clustering, stochastic coalescence, kinetic theory, integrable
systems, Burgers turbulence.

1 Introduction

We consider the scalar conservation law

∂tu + ∂xf (u) = 0, x ∈ R, t > 0, u(x, 0) = u0(x), (1)

with a strictly convex, C1 ﬂux f and initial data u0 that is a stochastic process
in x. The basic model of this type was introduced by Burgers in his study of
turbulence. He considered f (u) = u2/2 and white noise initial data [14, 44, 46].
While this model fails to describe turbulence in incompressible ﬂuids, it still
serves as a widely useful benchmark for theoretical methods and computations

1Division of Applied Mathematics, Box F, Brown University, Providence, RI 02912. Email:
menon@dam.brown.edu
2Department of Mathematics, The University of Texas at Austin, Austin, TX 78712, Email:
rav@math.utexas.edu
 1

in turbulence. It also has fascinating links with combinatorics, mathematical
physics and statistics, some of which we describe below.
Our main contribution in this article is to develop a consistent kinetic the-
ory that describes completely the clustering of shocks and the statistics of the
random process u(x, t) for convex f , and initial data u0 that are Markov pro-
cesses in x with only downward jumps. Our approach includes exact solutions to
Burgers turbulence as an important special case. In addition to being compre-
hensive, our approach clariﬁes the essential features of the problem, and reveals
the role of a Lax pair that describes the shock statistics. In order to describe
these results and place them in the context of past work, let us ﬁrst describe
the structure of solutions to (1) for deterministic u0, and then some important
exact solutions to Burgers turbulence that motivated our work.

1.1 The Hopf-Lax formula

Let us ﬁrst recall the notion of the entropy solution to (1) [20, 33]. Charac-
teristics for (1) are lines in space-time along which u is constant. If a unique
characteristic connects (a, 0) to (x, t) then u(x, t) = u0(a). However, there may
be many characteristics that pass through (x, t). Well-posedness is resolved by
adding a small dissipative term εuxx to the right-hand side of (1) and pass-
ing to the limit ε ↓ 0. This was ﬁrst carried out by Hopf in his pioneering
work on Burgers equation [27], and later generalized to convex f by Lax [32].
Let f ∗(s) = supu∈R (us − f (u)) denote the Legendre transform of f and call
U0(s) = ∫ s
0 u0(r)dr the initial potential. We deﬁne the Hopf-Lax functional

I(s; x, t) = U0(s) + tf ∗ ( x − s
t
 ) . (2)

The ‘correct’ characteristic through (x, t) is given by the variational principle

a(x, t) = sup {s ∈ R : I(s; x, t) = inf
r∈R I(r; x, t)
} , (3)

We will always assume that U0 has no upward jumps and I satisﬁes the growth
condition lim
|s|→∞ I(s; x, t) = ∞. (4)

This ensures the inﬁmum of I is a minimum, and that a(x, t) is ﬁnite. We write

a(x, t) = arg+mins∈RI(s; x, t). (5)

This is the Hopf-Lax formula for the inverse Lagrangian function a(x, t). The +

in (5) denotes that we choose a(x, t) to be the largest location if I is minimized
at more than one point. Of particular importance is Burgers equation with
f (u) = u2/2. In this case, (5) is called the Cole-Hopf formula, and takes the
form
 a(x, t) = arg+mins∈R
 {U0(s) + (x − s)
2

2t
 } , u(x, t) = x − a(x, t)
t . (6)

2

For ﬁxed t, a deﬁned by (5) is non-decreasing in x. If x is a point of continuity
of a(·, t), the velocity ﬁeld is given implicitly by

f ′ (u(x, t)) = x − a(x, t)
t . (7)

u(x, t) is well-deﬁned because f ′ is continuous and strictly increasing. In par-
ticular, if a(x, t) is constant for x in an interval, we obtain a rarefaction wave.
a may also have upward jumps. These arise if the minimum of I is attained
at more than one point. Jumps in a give rise to shocks in u. The left and
right limits u± = u(x±, t) exist and the velocity of the shock is given by the
Rankine-Hugoniot condition

u(x, t) = f (u−) − f (u+)
u− − u+ =: [f ]u−,u+ . (8)

We stress that the entropy solution u(x, t) has only downward jumps in x. This
will play a key role in our analysis.

1.2 Exact solutions for Burgers turbulence

Let us now suppose u0 is a stochastic process in x. The solution develops
shocks that are separated by rarefaction waves (see for example, the compu-
tations in [40]). The shocks move with speeds given by the Rankine-Hugoniot
condition, and cluster when they meet. The Lax equation we derive describes
this process. In order to explain this, we ﬁrst focus on two exact solutions for
Burgers turbulence.

L´evy process initial data on a half-line

We assume f (u) = u2/2 and

u0(x) = { 0, x ≤ 0,
Xx, x > 0, (9)

where X is a L´evy processes with only downward jumps (a spectrally negative
L´evy process). A particularly interesting case is when X is a standard Brownian
motion (that is, a Brownian motion with E(X 2
x) = x). This problem was solved
formally by Carraro and Duchon [15, 16] and rigorously by Bertoin [9]. The key
to their solution is a closure property of (6): if u0(x), x > 0 is a L´evy processes
with only downward jumps, then so is u(x, t) − u(0, t), x > 0. These processes
are characterized by their Laplace exponent ψ(q, t) deﬁned by

E (eq(u(x,t)−u(0,t))) = exψ(q,t), x, q, t > 0. (10)

Thus, the problem is reduced to determining the evolution of ψ. Remarkably,
ψ(q, t) satisﬁes Burgers equation in the new variables q, t!

∂tψ + ψ∂qψ = 0, ψ(q, 0) = ψ0(q). (11)

3

If X is a Brownian motion, ψ0(q) = q2, and we obtain the self-similar solution

ψ(q, t) = 1
t2 ψ∗(qt), ψ∗(q) = q + 1
2 −
 √

q + 1
4 . (12)

Various explicit formulas are summarized in [38].
The interpretation of (11) in terms of shock clustering is as follows. ψ satisﬁes
the celebrated L´evy-Khintchine formula

ψ(q, t) = ∫ ∞

0
 (
e−qs − 1 + qs) Λt(ds), q ≥ 0, t > 0, (13)

where Λt(ds) is the jump measure at time t. The evolution of ψ by (11) also
induces evolution of the jump measure Λt. But the jumps in the process u(·, t)
are the shocks, which evolve in a simple manner: shocks move at speed given
by the Rankine-Hugoniot condition (8) and stick, conserving momentum, when
they meet. Equation (11) captures this process. It is equivalent to the fact
that Λt satisﬁes a kinetic equation, Smoluchowski’s coagulation equation with
additive kernel, which describes the evolution and coalescence of shocks. A
derivation of the kinetic equation from this perspective may be found in [38].
An excellent survey of several links between stochastic coalescence and Burgers
turbulence is [11].

White noise initial data

Here we must characterize the law of u(x, t) when the initial velocity is white
noise. Precisely, let us suppose that the initial potential U0(x) = σBx where
B is a standard two-sided Brownian motion pinned at the origin and σ a ﬁxed
scale parameter. This problem also arises in statistics, and it was in this context
that Groeneboom ﬁrst characterized the law of the process u(x, t), x ∈ R [26].
He showed that for every t > 0, u(x, t), x ∈ R is a Markov process with only
downward jumps (a spectrally negative Markov process) that is stationary in x.
He then computed the generator of this Markov process explicitly in terms of
Airy functions. Here is a brief summary of his solution.
By (6) and the scaling invariance of Brownian motion, we see that

aσ(x, t) L
= (σt) 2
3 a1 (x(σt)
− 2
3 , 1) , uσ(x, t) L
= σ 2
3 t− 1
3 u1 (x(σt)
− 2
3 , 1) , (14)

where L
= denotes equality in law and the subscript σ refers to the variance of U0.
It is simplest to state the formulas under the assumption that σ2 = 1/2. Let ux
denote the process u2−1/2(x, 1). The generator of ux is an operator deﬁned by
its action on a test function ϕ in its domain as follows:

Aϕ(y) = lim
x↓0 Ey (ϕ (ux)) − ϕ(y)
x , (15)

where Ey denotes the law of the process with u0 = y. Groeneboom showed that
A is an integro-diﬀerential operator of the form

Aϕ(y) = ϕ
′(y) + ∫ y

−∞ (ϕ(z) − ϕ(y)) n∗(y, z) dz. (16)

4

The jump density n∗ of the integral operator is given explicitly as follows.

n∗(y, z) = J(z)
J(y) K(y − z), y > z, (17)

where J and K are positive functions deﬁned on the line and positive half-line
respectively, whose Laplace transforms

j(q) = ∫ ∞

−∞ e−qyJ(y) dy, k(q) = ∫ ∞

0 e−qyK(y) dy, (18)

are meromorphic functions on C given by

j(q) = 1
Ai(q) , k(q) = −2 d
2

dq2 log Ai(q). (19)

Ai denotes the ﬁrst Airy function as deﬁned in [2, 10.4]. Our normalization
of J and K diﬀers from [26] in two aspects. First, the above deﬁnition of K
is suggestive of Dyson’s formula in the theory of inverse scattering [34, p.273].
Second, the choice σ2 = 1/2 helps avoid several factors of 21/3 while stating the
main formulas.
We shall return to this solution at several points in this article. The one-
point and two-point distribution functions can be computed once the generator
is known. For example, p(y)dy = P (ux ∈ (y, y + dy)) = J(y)J(−y)dy. The
distribution of the shock sizes and the two-point distribution is given in [23].
Tauberian arguments yield precise asymptotics of these distributions.

1.3 Lax equations

Despite the elegance of the solution procedure for L´evy process data, it does not
apply to Burgers equation with broader classes of random initial data (e.g. white
noise), or to the general scalar conservation law (1). Our goal in this article is to
develop a kinetic theory that describes shock clustering for (1). Our work builds
on the links between stochastic coalescence and Burgers turbulence [11, 38],
exact solutions to Burgers equations with white noise initial data [23, 26], and
recent work on kinetic equations for Burgers turbulence [17]. We amplify these
remarks brieﬂy.
Groeneboom used the variational principle (6) at t = 1/2 to compute the
generator as in (16)–(18). Girsanov’s theorem is crucial in the analysis. Most
past work in the turbulence community is also based on a similar point of
view. This begins with Burgers’ analysis which was eventually completed by
Frachebourg and Martin [8, 14, 23, 30]. However, the focus on white noise
initial data and the use of Girsanov’s theorem obscures an understanding of the
dynamic process of shock clustering for general initial data (see for example,
the concluding remarks in [10]).
The idea of seeking kinetic equations for shock evolution can be found in pio-
neering early work of Burgers [12, 13], but this approach remained undeveloped

5

for several decades. More recently, E and Vanden-Eijnden introduced a hierar-
chy of master equations for the statistics of velocities and velocity gradients in
Burgers turbulence [22]. However, these equations are not closed, and a sophis-
ticated dimension reduction is needed to extract scaling exponents from these
equations. Frachebourg et al showed that the hierarchy of n-point functions
for ballistic aggregation can be closed at the level of the 2-point function [24].
Most recently, Chabanol and Duchon showed formally that if a statistical so-
lution to Burgers equation preserves the Markov property, then one can derive
evolution equations for the generator of the Markov process [17]. Moreover,
they showed that Groeneboom’s solution yields a self-similar solution to this
evolution equation.
This is the starting point for our work. Our viewpoint is as follows: rather
than seek a speciﬁc exact solution to Burgers equation with speciﬁc initial data,
we look for a class of natural stochastic processes whose structure in x is pre-
served by the entropy solution to the general scalar conservation law (1). Here
it is the class of spectrally negative Markov processes (in x). This reduces the
study of shock statistics to an evolution equation for the generator of the Markov
process. Our main results are:

• a closure theorem: Suppose f is strictly convex and C1. If u0 is a spec-
trally negative Markov process in x, so is the entropy solution to (1) (see
Theorems 2 and 3). This provides some rigorous justiﬁcation for our ap-
proach.

• new kinetic equations: We derive kinetic equations that describe the evo-
lution of the generator of the Markov process for arbitrary convex f . The
kinetic equations are equivalent to a Lax pair. Moreover, the Lax equa-
tions admit a spectral parameter as in Manakov’s integration of the Euler
equations for a spinning top in Rn [35]. This provides strong evidence
that the kinetic equations are completely integrable.

• consistent derivations: We derive the Lax equation from four diﬀerent
perspectives. Aside from being a stringent test on the consistency of the
kinetic equations, this also provides a uniﬁed treatment of disparate meth-
ods in the literature on statistical hydrodynamics.

In order to explain the Lax equation, let us assume that u(x, t) is a station-
ary, spectrally negative Feller process in x whose sample paths have bounded
variation. As in the L´evy-Khintchine formula, such a process is characterized
by its generator A(t), which acts on test functions ϕ ∈ C1
c (R) via

Aϕ(y) = b(y, t)ϕ
′(y) + ∫ y

−∞ (ϕ(z) − ϕ(y)) n(y, dz, t). (20)

For ﬁxed t > 0, b(·, t) ∈ C(R) and n(y, ·, t) is a measure on (−∞, y) that satisﬁes∫ (1 ∧ |y − z|2)n(y, dz, t) < ∞ for each y ∈ R. These terms correspond to the
drift and jumps of the process respectively. There is no diﬀusion term because
sample paths are solutions to a conservation law and necessarily have bounded

6

variation [20]. This expression for A is a special case of the general form of the
generator of a Markov process, as given in Theorem 3.5.3 in [7] (see also [41],
Eq. (2.1.13)).
We now introduce an operator B associated to A and the ﬂux function f .
This operator is deﬁned by its action on test functions as follows:

Bϕ(y) = −f ′(y)b(y, t)ϕ
′(y) − ∫ y

−∞
 f (y) − f (z)
y − z (ϕ(z) − ϕ(y)) n(y, dz, t). (21)

One of our main results is that the evolution of A is given by the Lax equation

∂tA = [A, B] = AB − BA. (22)

An evolution equation for the generator was ﬁrst derived in [17] for the ﬂux
f (u) = u2/2. However, the equations in [17] were not written in the simple
form above, and it was not clear if such equations could even be derived for
arbitrary ﬂuxes f . We show that while f (u) = u2/2 is certainly special, much
of the structure of the problem relies only on the convexity of f .
We present four diﬀerent derivations of (22): (1) as a compatibility condition
for martingales in x and t; (2) from kinetic theory as in [38]; (3) using BV
calculus as in [22]; (4) using Hopf’s functional calculus as in [17]. The shortest
(and most heuristic) of these is the ﬁrst, and goes as follows.
The main observation is that we have a two-parameter random process, and
formally B may be viewed as the ‘generator’ in t. To see this, ﬁx x ∈ R and
consider the random process u(x, t), t > 0. Then the multipliers −f ′(y) and
−[f ]y,z in (21) simply correspond to the evolution (in t) of the drift and jumps.
Indeed, if the path u(x, t) is diﬀerentiable at x with u(x, t) = y, ∂xu = b, then
∂tu = −f ′(y)b by (1). Similarly, if we have a shock connecting left and right
states y and z, then the shock speed is given by (8).
This may be understood more precisely using Itˆo’s formula for jump pro-
cesses [7]. For ﬁxed t, the random process u(x, t) satisﬁes the stochastic diﬀer-
ential equation

du(x, t) = b(u(x−))dx + ∫
R(z − u(x−))N (u(x−), dz, dx), (23)

where the Poisson random measure N (y, dz, dx) has intensity n(y, dz) dx. We
write the conservation law as du(x, t)dx + df (u(x, t))dt = 0, and apply Itˆo’s
formula to obtain

du(x, t) = −f ′(u(x−))b(u(x−))dt − ∫
R[f ]u(x−),z(z − u(x−))N (u(x−), dz, dt).

This shows immediately that B should have drift −f ′(y)b(y) and jump measure
−[f ]y,zn(y, dz). This holds rigorously when f is decreasing. In this case, all
shocks move to the left, u(x−, t) = u(x, t−), and u is also Markov in t, with
generator B given by (21).
 7

If A and B are generators, then the one-point distributions satisfy Kol-
mogorov’s forward equations

∂xp = A
†p, and ∂tp = B†p. (24)

We now seek martingales in x and t. To this end, ﬁx (x0, t0), and consider the
processes ϕ (u(x0 + s, t0)) and ϕ (u(x0, t0 + s)) with s > 0. These processes are
formally martingales if ϕ solves Kolmogorov’s backward equations

∂xϕ + Aϕ = 0, ∂tϕ + Bϕ = 0, (25)

in the domain (x, t) ∈ [x0, ∞) × [t0, ∞), and y, z ∈ R. If the compatibility
condition ϕxt = ϕtx holds for a suﬃciently rich class of functions ϕ, we obtain
the general Lax equation
 ∂tA − ∂xB = [A, B]. (26)

If the process is stationary in x, ∂xB vanishes and we obtain (22). In the form
(26), the Lax equation is akin to zero curvature conditions in integrable systems.

1.4 Kinetic theory

When we expand the commutator in (22), and separate the evolution of the drift
b and the jump measure n we obtain a kinetic equation that describes shock
clustering. The drift satisﬁes the diﬀerential equation

∂tb(y, t) = −f ′′(y)b2(y, t). (27)

Note that the drift does not depend on the jump measure. The jump density
n(y, z, t) dz = n(y, dz, t) satisﬁes the kinetic equation

∂tn(y, z, t) + ∂y (nVy(y, z, t)) + ∂z (nVz(y, z, t)) (28)

= Q(n, n) + n (([f ]y,z − f ′(y)) ∂yb − bf ′′(y)) .

Here the velocities Vy and Vz in (28) are given by

Vy(y, z, t) = ([f ]y,z − f ′(y)) b(y, t), Vz(y, z, t) = ([f ]y,z − f ′(z)) b(z, t), (29)

and the collision kernel Q is

Q(n, n)(y, z, t) = ∫ y

z ([f ]y,w − [f ]w,z) n(y, w, t)n(w, z, t) dw

− ∫ z

−∞ ([f ]y,z − [f ]z,w) n(y, z, t)n(z, w, t) dw

− ∫ y

−∞ ([f ]y,w − [f ]y,z) n(y, z, t)n(y, w, t) dw. (30)

We have assumed for convenience that the jump measure has a density, but the
above equations extend naturally to general jump measures.

8

In the next section we derive these equations from the perspective of kinetic
theory. We consider single shocks and rarefaction waves as building blocks,
and use this to derive a natural Boltzmann-like equation. This will yield the
equations above. We then show that these kinetic equations are equivalent to
the Lax equation (22). That calculation reﬂects the fact that operators of the
form (20) formally constitute a Lie algebra.

1.5 The broader context of our work

We conclude this introduction by connecting our work with some other prob-
lems in mathematical physics and statistics. We pay particular attention to
connections with integrable systems.

1.5.1 The spectral curve and complete integrability

We ﬁrst point out the role of a spectral parameter in analogy with Manakov’s
treatment of the Euler equations for geodesic ﬂow on so(n) with a left-invariant
metric [35]. Let M and N denote multiplication operators acting on the domain
of A, deﬁned by
 Mϕ(y) = yϕ(y), N ϕ(y) = f (y)ϕ(y). (31)

It is clear that M and N are diagonal operators. We now use the deﬁnitions
(20), (21) and (31) to ﬁnd
 [A, N ] − [M, B] = 0. (32)

This observation allows us to introduce a spectral parameter µ ∈ C in the Lax
equation. We use (22) and (32) to obtain

∂t (A − µM) = [A − µM, B + µN ], µ ∈ C. (33)

If A, B were n × n matrices, it would follow that the spectral curve (Riemann
surface) Γ = {(λ, µ) ∈ C2 |det(A − λId − µM) = 0 }, (34)

is ﬁxed by the evolution. In Manakov’s work, this is the crucial observation that
yields the existence of additional integrals for Euler’s equations in so(n), n ≥ 4.
These integrals are simply the coeﬃcients of the characteristic polynomial above.
More broadly, the observation that (22) admits a spectral parameter reveals a
close relation with a large class of completely integrable systems (including KdV,
the Toda lattice, geodesic ﬂows on so(n) and ellipsoids, and the integrable PDEs
of random matrix theory). The complete integrability of all these ﬂows may be
obtained in a uniﬁed way via a general splitting theorem for Lie algebras [3].
This connection also sets the stage for the application of powerful methods from
algebraic geometry to integrate (26) explicitly for every convex f [4]. We will
address this in later work.
 9

1.5.2 Burgers turbulence and random matrices

The solution to Burgers turbulence with spectrally negative L´evy process data
(see § 1.2) is obtained from (22) as follows. Suppose u(x, t) − u(0, t), x > 0 is
a spectrally negative L´evy process with bounded variation and mean zero. If
we denote the jump measure Λt, then b(t) = ∫ ∞
0 sΛt(ds), and the generators A
and B take the form

A(t)ϕ(y) = ∫ ∞

0 (ϕ(y − s) − ϕ(y) + sϕ
′(y)) Λt(ds), (35)

B(t)ϕ(y) = −yA(t)ϕ(y) + 1
2
 ∫ ∞

0 (ϕ(y − s) − ϕ(y)) sΛt(ds).

In particular, when ϕ(y) = eqy, Re(q) > 0, we have

A(t)eqy = ψ(q, t)eqy, B(t)eqy = − (
yψ(q, t) + 1
2 ∂qψ) eqy. (36)

We substitute (36) in (22) to obtain (11).
We next note that the solution (12) can be mapped to Wigner’s semicircle
law in the theory of random matrices. Dyson observed that the eigenvalues of a
standard matrix valued Brownian motion Mt in the group of n × n symmetric,
hermitian or symplectic matrices satisfy the stochastic diﬀerential equation [21]

dλk = ∑

j̸=k
 dt
λk − λj + √ 2
β dBk, 1 ≤ k ≤ n, (37)

where Bk, 1 ≤ k ≤ n are independent Brownian motions, and β = 1, 2 or 4 for
the ensembles above. That is, the eigenvalues behave like repulsive unit charges
on the line perturbed by independent white noise. The law of large numbers
for this ensemble is as follows. As n → ∞ the spectral measure of n−1/2Mt
converges to Wigner’s semicircle law:

µt(dx) = 1
2πt
 √
4t − x2 dx, |x| < 2√
t. (38)

Moreover, the Cauchy transform of µt,

g(z, t) = ∫ 1
z − x µt(dx), z ∈ C\[−2√
t, 2√
t], (39)

solves Burgers equation with a simple pole as initial data [5, §4.3.2]. That is,

∂tg + g∂zg = 0, g(z, 0) = 1
z . (40)

More precisely, g solves (40) in the slit plane C\[−2√
t, 2√
t], and has the form

g(z, t) = 1
√
t g∗
 ( z
√
t
 ) , g∗(z) = 1
2
 (
z − √
z2 − 4
) , |z| ≥ 2. (41)

10

It now transpires that the self-similar solution (12) can be transformed to (41)
by a simple change of variables.

ψ∗(q)
q = g∗(z), z = 2 + 1
q , or g(t 1
2 z, t)

t 1
2 = ψ(t−1q, t)
t−1q . (42)

In his beautiful thesis [29], Kerov found a deeper interpretation of (40) based
on the representation theory of the symmetric group. He introduced a Markov
process for the growth of Young diagrams (Plancherel growth), and derived (40)
in a mean-ﬁeld limit. More general initial conditions may also be included in
(40) and he showed that the evolution of g by Burgers equation is equivalent
to a kinetic equation for µt [29, Ch. 4.5]. Thus, the transformation (42) links
µt to Λt, and Plancherel growth with Smoluchowski’s coagulation equation (see
(13)). We do not have a deeper (i.e. stochastic process) explanation of this
relation yet.
Airy functions and the Painlev´e transcendents arise in the scaling limit of
ﬂuctuations from Wigner’s law at the edge of the spectrum. The ﬂuctuations
are given by the celebrated Tracy-Widom distributions involving a solution to
Painlev´e-II [42]. We now point out that the function l = j′/j (j as in (18))
solves the Riccati equation dl/dq = −q + l2 and is therefore an Airy solution
to Painlev´e-II [1, Ch. 7]. This is used to verify that Groeneboom’s solution
satisﬁes the kinetic equation (22) in §6.

1.5.3 Shell models of turbulence and their continuum limits

It is also of interest to consider (1) on the half-line x > 0 with random forcing
at x = 0. This problem arises as a continuum limit of shell models of turbu-
lence [36, 37]. Shell models are lattice equations of the form ˙ck = Jk−1 − Jk,
k = 1, 2, . . .. Here ck ≥ 0 models the energy in the k-th Fourier mode (shell),
and Jk the ﬂux from shell k to k + 1. Jk is expressed in terms of ck and its
nearest neighbors by a suitable constitutive relation. The main question is to
understand how randomness spreads through the system under the assumption
that J0 is a prescribed random forcing (a stationary Feller process, for example).
In particular, it is of interest to understand whether the system has a unique
invariant measure. In the continuum limit, these questions may be treated by
our approach. We note that the derivation of (26) does not depend on assump-
tions of stationarity and is independent of boundary conditions. Therefore, (26)
holds in the domain x, t > 0 and must be augmented with a boundary condition
on the line x = 0. In particular, as t → ∞, invariant measures are solutions to

−∂xB = [A, B], (43)

with a boundary condition at x = 0 matching B and the generator of the forcing.
In contrast to a time-correlated boundary forcing, it is also possible to con-
sider a white-in-time forcing in the bulk (a Feller process in x and δ-correlated
in t) which is independent of the initial data. For Burgers’ equation, this is

11

a particular case of forced Burgers turbulence. The generator F of the forcing
simply appears as an additional term in the Lax equation

∂tA − ∂xB = [A, B] + F . (44)

An interesting exact solution to (44) for Burgers equation forced with a two-
sided Brownian motion in space has recently been obtained in [18].

1.5.4 Applications to statistics

In statistics, (6) with U0 a two-sided Brownian motion ﬁrst arose in the follow-
ing estimation problem [19]. Suppose X1, . . . , Xn are independent, identically
distributed (iid) samples from a distribution with a smooth unimodal density ρ
with mode m and ﬁnite variance. Let us consider a naive ‘binning’ strategy to
estimate the mode m. We ﬁx a bin width w and count the number of samples
Nn(s) = #{Xk ∈ (s − w, s + w)} in the bin centered at s. We estimate the mode
by mn = arg+maxsNn(s). Chernoﬀ observed that the ﬂuctuations mn − m are
O(n−1/3). Precisely, for suitable c(ρ, w) > 0, the rescaled random variables
cn1/3(mn − m) converge in law to Chernoﬀ ’s distribution

Z = arg+maxs {
U0(s) − s2} . (45)

The quadratic term −s2 arises from the Taylor expansion of ρ around m – the
ﬁrst order term vanishes since m is the maximum of ρ. By the symmetry of
Brownian motion, it is clear that Z has the same law as a(0, 1/2).
This is not an isolated result: ‘cube-root’ ﬂuctuations appear naturally in a
wide class of estimation problems [6]. Kim and Pollard proved functional limit
theorems for several such estimators, with the law of the limit characterized by
arg
+maxs∈Rd {
U0(s) − |s|2} where U0(s) is a continuous Gaussian process in Rd

pinned at the origin [31]. These correspond to solutions to Burgers equation in
Rd with random initial data U0, but this connection has not been explored in
the literature.

1.6 Outlook

Let us conclude by pointing out some signiﬁcant shortcomings in our work.
Much of this article relies on formal calculations. But these calculations are
often interesting, and it seems more fruitful to present them in a transparent
and suggestive manner, rather than as rigorous statements burdened by techni-
calities. The most signiﬁcant gap is that we do not prove (22). This is because
our closure theorem is not strong enough. We only establish that the entropy
condition preserves the Markov property. In order to rigorously establish (22)
it is necessary to prove that the entropy condition preserves Feller processes.
This is an assertion of regularity, whereas we only establish measurability. This
is closely tied to establishing a satisfactory well-posedness theory for (22), and
will be addressed in forthcoming work. A suitable well-posedness theorem would
also yield a probabilistic proof of the existence of a two-parameter family of self-
similar solutions to (22). These solutions are generated by considering the ﬂux

12

functions f (u) = |u|
p/p, 1 < p < ∞ and an initial potential that is an α-stable
spectrally negative L´evy process. It seems challenging to prove this analytically
starting with (22).
Also, while our work yields a deeper understanding of Groeneboom’s solu-
tion, it does not, as yet, constitute an independent proof of his results. We have
only been able to verify that his solution satisﬁes (22). We have been unable
to derive it using (22) alone. We hope to address this in future work using
techniques from integrable systems.
The rest of this article is organized as follows. We ﬁrst derive (27) and (28)
from the standpoint of kinetic theory in the next section. This is followed by the
rigorous closure theorems. We then derive the Lax equations by BV calculus
and by Hopf’s method. Finally, we consider Groeneboom’s self-similar solution
for Burgers equation in Section 6.

2 Kinetic equations

2.1 Introduction

In this section, we assume the velocity u is a stationary Feller process in x, and
derive the kinetic equations of Section 1.4. We use the evolution of a single shock
and rarefaction wave to derive a Boltzmann-like equation for the evolution of the
density of shocks. We conclude this section by showing that the Lax equation
(22) is equivalent to the kinetic equations (28)–(30). The main observation is
that the space of operators of the form (20) is formally a Lie algebra.

2.2 Conservation of total number density

Let p(y, t) denote the stationary 1-point density, i.e. p(y, t)dy = P (u(x, t) ∈
(y, y + dy)), and F (y, z, t) denote the total number density, i.e. the expected
number of jumps per unit length from states y to z. Then

F (y, z, t) = p(y, t)n(y, z, t). (46)

The total number density changes because of a ﬂux of shocks and shock colli-
sions, and we have the general conservation law of Boltzmann-type

∂tF + ∂y (F Vy) + ∂z (F Vz) = C(F, F ). (47)

Here Vy and Vz denote ‘velocities’ in the (y, z) ‘phase space’, and C is a binary
collision kernel. This is the general structure of the equation. We now derive
the evolution equation for b, the velocities Vy, Vz, and the collision kernel C,
based on elementary solutions to the scalar conservation law (1).

2.3 Decay of the drift

First consider how aﬃne data evolves under (1). Let u(x, t) solve (1) with
u0(x) = α0 + β0x. For x, t ≈ 0, we have to leading order u(x, t) ≈ α(t) + β(t)x,

13

so that ∂tu ≈ ˙α + ˙βx, ∂xf (u) ≈ f ′(α)β + f ′′(α)β2x. (48)

We now balance terms in (1) to obtain

˙α = −f ′(α)β, ˙β = −f ′′(α)β2. (49)

The second equation expresses the decay of rarefaction waves when β0 > 0. The
connection between this elementary solution and the generator of the process is
the following. The drift coeﬃcient b(y, t) corresponds locally to an aﬃne proﬁle
as above with α = y and β = b. Thus, the second equation above is simply (27).

2.4 Decay of shocks and Vy,Vz

The ‘velocities’ Vy and Vz in (y, z) space arise because of the decay of shocks.
In order to derive these velocities, we ﬁx u− > u+ and consider piecewise aﬃne
initial data
 u0(x) = { u− + b−x, x < 0,
u+ + b+x, x > 0. (50)

Let s(t) denote the path of the shock. Then by (8), for small t

s(t) = [f ]u−,u+ (t + o(t)). (51)

s is also given by the kinematic condition

s(t) = a±(t) + f ′(u±)t + o(t). (52)

where a± denotes the left and right inverse Lagrangian points at time t. Thus,

a±(t) = (
[f ]u−,u+ − f ′(u±)
) t + o(t). (53)

Since u− > u+ and f is convex, we see that [f ]u−,u+ − f ′(u−) < 0. Similarly,
[f ]u−,u+ − f ′(u+) > 0. As a consequence, a shock initially connecting states u±
decays to a shock connecting states

u± + (
[f ]u−,u+ − f ′(u±)
) b±t + o(t). (54)

This decay gives rise to a ﬂux of F . To ﬁrst approximation, the ﬂux is linear in
F , and of the form (47) with the drift velocities given by (29).

2.5 The collision kernel C(F, F )

Binary collisions of shocks occur at a rate determined by the Markov property (in
x) and the relative velocity of shocks given by (8). In order to simplify notation,
we suppress the t-dependence for the process u and write ux for u(x, t). We also
denote a shock connecting states u− and u+ by {u−, u+}. Shock clustering
involves the following events:

growth : {y, w} + {w, z} = {y, z}, z < w < y, (55)

decay : {y, z} + {z, w} = {y, w}, −∞ < w < z, (56)
decay : {w, y} + {y, z} = {w, z}, y < w < ∞. (57)

14

The computation of rates for these events is similar. To be concrete, let us ﬁrst
consider (55). Fix z < w < y and consider small ∆x1 > 0, ∆x2 > 0. Then
formally, by the Markov property

dP (u0 = y, u∆x1 = z) ≈ p(y)n(y, z) dy dz ∆x1, (58)

and similarly,
 dP (u0 = y, u∆x1 = w, u∆x1+∆x2 = z) (59)

≈ p(y)n(y, w)n(w, z) dy dz dw ∆x1 ∆x2.

The relative velocity of these shocks is [f ]y,w − [f ]w,z to leading order. We thus
set ∆x2 = ([f ]y,w − [f ]w,z) ∆t to compute the number of collisions in time ∆t.
We now sum over w in the range z < w < y to obtain the growth term in
C(F, F ):
 C1 := ∫ y

z p(y)n(y, w)n(w, z) ([f ]y,w − [f ]w,z) dw. (60)

The computation for the events (56) is similar. We now ﬁnd the decay terms

C2 := − ∫ z

−∞ p(y)n(y, z)n(z, w) ([f ]y,z − [f ]z,w) dw, (61)

and
 C3 := − ∫ ∞

y p(w)n(w, y)n(y, z) ([f ]w,y − [f ]y,z) dw. (62)

2.6 Kinetic equations for n

We have now deﬁned all the terms in (47). In order to obtain an equation in
terms of n alone we use Kolmogorov’s forward equations to eliminate the 1-point
distribution p(y, t). The ﬁrst equation in (24) is now 0 = A
†p since the process
is stationary in x. The second equation in (24) implies

p(y)∂tn(y, z) = ∂tF (y, z) − n(y, z)B†p(y), (63)

where

B†p(y) = ∂y (f ′(y)b(y)p(y)) − ∫

R (p(w)n(w, y) − p(y)n(y, w)) [f ]y,w dw. (64)

(It is convenient to denote the domain of integration by R, noting that it is
actually a half-line because n(y, z) = 0 for y < z.)
To isolate the main cancellations on the right hand side of (63), we note that
the integral term in C3 − n(y, z)B†p(y) is

n(y, z) (
[f ]y,z
 ∫

R p(w)n(w, y) dw − p(y) ∫

R n(y, w)[f ]y,w dw) . (65)

15

The ﬁrst integral above can be simpliﬁed further. Since A
†p = 0, we also have
∫

R p(w)n(w, y) dw = p(y) ∫

R n(y, w) dw + ∂y (b(y)p(y)) . (66)

Therefore, we may rewrite the expression in (65) as

p(y)n(y, z) ∫ y

−∞ ([f ]y,z − [f ]y,w) n(y, w) dw + n(y, z)[f ]y,z∂y (b(y)p(y)) . (67)

We now collect all terms on the right hand side of (63) using (47), (29), (60),
(61), and (67). We then have

p(y)∂tn(y, z) = p(y)Q(n, n)(y, z) (68)
+n(y, z) ([f ]y,z∂y (b(y)p(y)) − ∂y (f ′(y)b(y)p(y))) (69)

−∂y (F (y, z)Vy(y, z)) − ∂z (F (y, z)Vz(y, z)) , (70)

where Q(n, n) denotes the collision kernel in (30). Finally, we use (46) and (29)
to obtain the sum of (69) and (70):

= p(y) (n ([f ]y,z − f ′(y)) ∂yb − bf ′′(y)) − ∂y (nVy(y, z)) − ∂z (nVz(y, z)) . (71)

Under the assumption that the Markov process u has a strictly positive station-
ary density, we may cancel p(y) on both sides of (67). We then have the kinetic
equations (28).

2.7 Equivalence of the Lax equations and kinetic equa-
tions

The equivalence of the Lax equations (22) and the kinetic equations (28)–(30)
follows from the algebraic structure of operators of the form (20) and (21). The
space of operators of the form

Aϕ(y) = b(y)ϕ(y) + ∫

R n(y, z) (ϕ(z) − ϕ(y)) dz, (72)

with b, n smooth, n satisfying appropriate integrability conditions, and the
bracket [·, ·] is formally a Lie algebra. That is, if Ai, i = 1, 2, 3 are operators as
above, then [A1, A2] is an operator of the same form, and the following Jacobi
identity holds:
 [[A1, A2], A3] + [[A2, A3], A1] + [[A3, A1], A2] = 0. (73)

We do not assume that b and n are positive or that their support is a half-line.
Both assertions rely on tedious, but direct calculations. We will omit the proof
of (73), and simply summarize the calculation for [A1, A2]. We have

[A1, A2]ϕ(y) = (b1b′
2 − b′
1b2) ϕ(y) + ∫

R (ν + σ) (ϕ(z) − ϕ(y)) dz, (74)

16

with ν(y, z) = b1(y)∂yn2 − b2(y)∂yn1 + ∂z (b1(z)n2 − b2(z)n1) , (75)

and
 σ(y, z) = ∫

R (n1(y, w)n2(w, z) − n2(y, w)n1(w, z)) dw (76)

+ ∫

R n2(y, z)n1(z, w) − n1(y, z)n2(z, w) dw

+ ∫

R n1(y, z)n2(y, w) − n2(y, z)n1(y, w) dw.

We apply (74) to (22) as follows. Let A1 = A and A2 = B, with A and B as in
(20) and (21). We then ﬁnd immediately from (75) that the drift coeﬃcient of
[A, B] is −b(y) (f ′(y)b(y))
′ + f ′(y)b(y)b′(y) = −f ′′(y)b2(y) (77)

as in (27). Similarly, we use (75) to obtain the second, third and last term in
(28). Finally, we substitute the jump measures in (76) to obtain the collision
kernel Q(n, n).

3 Closure theorems

3.1 Introduction

In this section we show that the entropy solution to (1) preserves the class of
spectrally negative Markov processes. The Markov property of u was implicitly
used by Burgers, and made explicit in [8]. Our work is based on previous results
by Bertoin [9] and Winkel [45]. We extend these results to general convex ﬂuxes
f and a large class of noise initial data.

3.2 Splitting times

The main technical tool we need is the decomposition of Markov processes at
random times so that the past and future are conditionally independent. This
certainly holds at a stopping time. However, it also holds for a broader class of
splitting times. We use the following theorem on the preservation of the Markov
property at a last-passage time.

Theorem 1 (Getoor [25]). Consider a c`adl`ag strong Markov process Xs. Let
M ⊂ R be a ﬁxed set and let L = sup{s ∈ R : Xs ∈ M } be the end of M . Then
the post-L process {Xs}s≥L is independent of {Xs}s<L given XL.

Furthermore, the transition semigroups of the pre- and post-L processes can
be explicitly determined from that of X. It is an important and subtle fact
that these transition semigroups are diﬀerent from that of the original process.
In particular, the semigroup of the post-L process is the same as that of X
conditioned to never hit M again.
 17

3.3 Closure for spectrally negative initial velocity

We work within the canonical framework. Let u0 = (Ω, F , Fs, u0(s), µ0) be a
spectrally negative Markov process on the space Ω of c`adl`ag paths on (−∞, ∞)
endowed with the Skorohod topology. Here, µ0 is the law of the coordinate
process u0(ω; s) = ω(s) on Ω and Fs = σ(u0(r), r ≤ s) is the natural ﬁltration of
u0 extended to be right-continuous and complete. Note that in our work x plays
the role of “time” as traditionally used in the theory of stochastic processes. t
acts as a parameter in the following discussion, and will be dropped from the
notation when convenient.
We rewrite the Hopf-Lax functional and inverse Lagrangian function as

I(s; x, t) = ∫ s

0
 (
u0(r) − (f ′)
−1 ( x − r
t
 )) dr (78)

a(x, t) = arg+ min
s∈R I(s; x, t). (79)

To ensure that (79) is well-deﬁned and ﬁnite, we assume (4) holds a.s. This
is certainly true if u0 is a stationary random process and f ∗ grows fast enough
at inﬁnity. In what follows we also make use of the fact that for ﬁxed t, a(x, t) is
an increasing function in x. Since u(x, t) and a(x, t) are related by (7), in order
to obtain the closure property we only need to show that a(x, t) is a Markov
process. We prove the following:

Theorem 2. Let u0 be a spectrally negative strong Markov process such that
(4) holds a.s. Under the law µ0 and for any ﬁxed t > 0, the inverse Lagrangian
process a(x, t) is a Markov process. Thus, u(x, t) is a spectrally negative Markov
process.

Proof. Fix x ∈ R. Without loss of generality it suﬃces to take t = 1. We also
suppress the dependence on t in the notation for clarity. The proof consists of
three steps, the ﬁrst two of which are entirely deterministic.
1. Dependence structure of (a(x))x∈R: Since a(x) is increasing, for h > 0

a(x + h) = arg+ min
s∈R I(s; x + h)

= arg+ min
s≥a(x)
{I(a(x); x + h) + (I(s; x + h) − I(a(x); x + h))}

= a(x) + arg+ min
s≥0
 {∫ a(x)+s

a(x)
 (
u0(r) − (f ′)
−1(x − r)
) dr
}
 . (80)

(a(x + h) − a(x))h>0 therefore depends on u0 only through (u0(s))s>a(x). The
same argument shows that (a(x − h) − a(x))h>0 depends only on (u0(s))s<a(x).
2. Downward jumps determine u0(a(x)): If u0 has only downward jumps
then ∂sI(a(x); x) = 0. That is,

u0(a) = (f ′)
−1(x − a(x)). (81)

18

This may be seen easily by sketching a picture. Upward jumps in u0 give rise to
a potential with a corner that is convex, and downward jumps give a potential
with a corner that is concave. In the second case, the minimum of I can never
be achieved at the corner. Thus, it is always obtained at a point of continuity,
implying (81).
3. a(x) is a splitting time for u0: It is not obvious that a(x) is a Markov
time for u0. It is not a stopping time since the event {a(x) ≤ s} is not Fs-
measurable. Indeed, a(x) is the last time (78) is minimized and depends on
(u0(r))r>s as well. a(x) is, however, a splitting time for a certain functional of
u0. To see this, ﬁrst deﬁne

m(s; x) = min
r≤s I(r; x), D(s; x) = (I − m)(s; x).

For simplicity, denote d(s; x) = (f ′)
−1(x − s). Dropping the explicit dependence
on x from the notation, consider the process (u0, d, D). Since D(s) is entirely
dependent on (u0(r))r≤s, (u0, d, D)(s) is Fs-measurable. For any F -stopping
time ξ

m(ξ + s) = m(ξ) ∧ ( min
ξ<r≤ξ+s I(r)
) = I(ξ) + {−D(ξ) ∧ min
0<r≤s
(I(ξ + r) − I(ξ))
}

and
 D(ξ + s) = (I(ξ + s) − I(ξ)) − {
−D(ξ) ∧ min
0<r≤s
(I(ξ + r) − I(ξ))
} .

For s > 0 the increment I(ξ + s) − I(ξ) depends on Fξ only through u0(ξ) by
the strong Markov property of u0. Therefore, (u0, d, D) is also a c`adl`ag, strong
Markov process.
We now show that a(x) is a splitting time for (u0, d, D). By deﬁnition
(79) and step 2, a(x) is the last time s that (u0, d, D)(s) hits the ﬁxed set
{(y, y, 0) : y ∈ R}. Thus, we can use Theorem 1 to split u0 at a(x) into

(u0, d, D)s<a(x) and (u0, d, D)s>a(x).

As a consequence, (u0(s))s<a(x) and (u0(s))s>a(x)

are conditionally independent given d(a(x))—that is, since d is invertible, given
a(x).
This shows that a is a Markov process (note that the law of the increments of
the process may vary with x). Therefore, u(x) = (f ′)
−1(x − a(x)) is a spectrally
negative Markov process.

Remark 1. Theorem 2 reduces to Bertoin’s closure theorem [9, Thm. 2] if
f (u) = u2/2 (Burgers ﬂux) and u0 is a spectrally negative L´evy process. To see

19

this, use (81) in (80):

a(x + h) − a(x) = arg+ min
s≥0
 {∫ a(x)+s

a(x) (u0(r) − u0(a(x)) + r − a(x)) dr
}

= arg+ min
s≥0
 {∫ s

0 (u0(a(x) + r) − u0(a(x)) + r) dr} .

Since u0 has independent increments, the integrand above is independent of
(u0(s))s<a(x) and has the same law as u0(r) − u0(0) + r. So, the law of a(x +
h) − a(x) is independent of a(x − h) − a(x))h≥0 and does not vary with x. Note
that it is necessary to use f (u) = u2/2 to obtain this result, and to show that
the increments of a(x) are identical in law to those of the ﬁrst hitting process
T (x) = inf{s ≥ 0 : u0(s) + s ≥ x}.

3.4 Closure for noise initial data

We now prove the analogue of Theorem 2 for noise initial data. Recall that the
Hopf-Lax functional and inverse Lagrangian function satisfy

I(s; x, t) = U0(s) + f ∗ ( x − s
t
 ) (82)

a(x, t) = arg+ min
s∈R I(s; x, t). (83)

We prescribe the law of the potential as follows. Let

U0(x) = { − ˜Y−x−, x ≤ 0
Yx, x > 0 , (84)

where Y, ˜Y are independent copies of a spectrally negative additive process
starting at 0 and x− denotes the limit from the left. We denote by M0 the law
of U0 on the space of c`adl`ag paths. If X has stationary increments it is a L´evy
process, but it is not necessary to assume this. In addition, assume the growth
condition (4) holds almost surely.

Theorem 3. Suppose U0 = (Ω, G, Gs, U0(s), M0) is a two-sided spectrally nega-
tive process with independent increments and satisﬁes (4) a.s. Then under M0
and for all t > 0, u(x, t) is a spectrally negative Markov process.

Proof. Again, we ﬁx x ∈ R, take t = 1, and drop the t-dependence in our
notation.
1. Dependence structure of (a(x))x∈R: As before, for h > 0

a(x + h) = arg
+ min
s∈R I(s; x + h)

= a(x) + arg+ min
s≥0 {I(a(x) + s; x + h) − I(a(x); x + h)}

20

Let Xs denote the strong Markov process I(s; x + h) and let a = a(x). The
increment a(x + h) − a(x) therefore depends on U0 only through the increment
Xa+s − Xa.
2. Spectral negativity of X: Since U0 is spectrally negative, so is the process
Xs. Explicitly, Xs− ∧ Xs = Xs.

3. Markov property of X at a: The inverse Lagrangian a is the last time
Xs− ∧ Xs hits its ultimate minimum m = Xa. Using spectral negativity, we
need only consider Xs. Let Ms = minr≤s Xr. Then a(x) is the last time s that
(Xs, Ms) hits the ﬁxed set {(y, y) : y ∈ R}. Theorem 1 then implies (Xs)s≥a is
independent of (Xs)s<a given m.
We now make use of the particular form of the semigroup of the post-a
process, for which we refer to [25, Thm. 2.12] (see also Theorem 5.1 in [39] and
the subsequent remark). Precisely, given a and m, the law of (Xs)s≥a is identical
to that of an independent copy of Xs started at a with Xa = m and conditioned
to live above m. By the invariance of U0 under translations in state space (due
to the property of independent increments) this implies that (Xs)s≥a is identical
in law to a copy of Xs started at a with value Xa = 0 and conditioned to live
above 0. To summarize, although the post-a process no longer has independent
increments, the increment Xa+s − Xa is still independent of m given a.
By steps 1 and 3, the increment a(x + h) − a(x) is independent of (a(x − h) −
a(x))h≥0 given a and m. Since a(x + h) − a(x) only depends on X through the
increment Xa+s − Xa, given a it is independent of m as well. Therefore, a(x)
is a Markov process and u(x) is a spectrally negative Markov process. Notice
that if U0 is not spectrally negative or does not have independent increments,
then a(x + h) − a(x) depends on U0(a−) or U0(a) in addition to a, destroying
the Markov property.

4 BV calculus and the Lax equations

In this section, we derive the Lax equation (22) using the conservation law (1)
and the Vol’pert chain rule for BV functions. This calculation is similar in
spirit to [22]. We assume that for every t > 0, u(x, t) is a spectrally negative,
stationary Feller process. The generator of u is given by (20) and the operator B
is deﬁned by (21). In addition, we deﬁne one and two-point operators as follows.
We associate a linear functional P to the stationary one-point distribution p(y, t)
via P(ϕ) = E (ϕ(u(x, t))) = ∫

R ϕ(y)p(y) dy. (85)

(Here and in what follows, it is convenient to suppress t in the notation.) Sim-
ilarly, given h > 0 we denote the transition kernel for the process u by qh and
deﬁne the associated transition operator

(Qhϕ)(y) = ∫

R qh(y, z)ϕ(z) dz. (86)

21

4.1 The 1-point function

We recall that the entropy solutions to (1) are in BVloc(R+×R). Vol’pert showed
that one may extend the chain rule to such functions in a natural manner. Let
u± = u(x±, t) denote the right and left limits of u(x, t) and for any test function
ϕ, consider the composition ϕ(u(x, t)) and set

[ϕ] = ∫ 1

0 ϕ (u− + β(u+ − u−)) dβ. (87)

Then for every smooth test function with compact support, the entropy solution
to (1) satisﬁes [43, p.248]

∂tϕ(u(x, t)) = −[ϕ][f ]∂xu(x, t), x ∈ R, t > 0. (88)

The law of the 1-point function is determined by E (ϕ(u(x, t)) for arbitrary ϕ.
We use equation (88) to obtain

∂tE (ϕ (u(x, t))) = −E ([ϕ][f ]∂xu(x, t)) . (89)

The left hand side of (97) is (∂tP )ϕ. We must determine the right hand side.
To this end, ﬁx x ∈ R and for h > 0 let us denote u−h = u(x − h, t). Our
calculation relies on the following unjustiﬁed interchange of limits:

E ([ϕ][f ]∂xu(x, t)) = lim
h↓0 E ( 1
h (ϕ(u+) − ϕ(u−h)) (f (u+) − f (u−h))
u+ − u−h
 ) . (90)

We assume (90), and show that

lim
h→0 E ( 1
h (ϕ(u+) − ϕ(u−h)) (f (u+) − f (u−h))
u+ − u−h
 ) = −P (Bϕ) , (91)

As a consequence, (∂tP)ϕ = PBϕ, (92)

which is the formal forward equation (24).
We now establish (91) for a monomial f (u) = um. Since B depends linearly
on f , (91) then also holds for polynomials and by approximation for C1 ﬂuxes
with polynomial growth. For f (u) = um we expand the jump term

f (u+) − f (u−h)
u+ − u−h =
 m−1∑

j=0 um−1−j
−h uj
+. (93)

Therefore, the limit in (91) is a sum of terms of the form

(ϕ(u+) − ϕ(u−h)) um−1−j
−h uj
+ =

um−1−j
−h (ϕ(u+)uj
+ − ϕ(u−h)uj
−h − ϕ(u−h) (
uj
+ − uj
−h)) .

22

The limit of each of these terms is

lim
h→0 1
h E ((ϕ(u+) − ϕ(u−h)) um−1−j
−h uj
+) =

lim
h→0 1
h P (
ym−1−j (
Qh(yjϕ) − yjϕ − ϕ (
Qh(yj) − yj)))

= P (
ym−1−j (
A(yjϕ) − ϕA (yj))) . (94)

The term A(yjϕ) − ϕA (yj) may be computed using (20). First the drift term
is ym−1−j (
b(yjϕ)
′ − ϕb(yj)
′) = bym−1ϕ
′. (95)

Similarly, the jump term simpliﬁes to

ym−1−j ∫

R n(y, z)zj (ϕ(z) − ϕ(y)) dz. (96)

We now sum over all terms in the expansion (93) to obtain

lim
h→0 E ( 1
h (ϕ(u+) − ϕ(u−h)) (f (u+) − f (u−h))
u+ − u−h
 )

=
 m−1∑

j=0 P (
ym−1−j (
A(yj ϕ) − ϕAyj))

= P
 

m−1∑

j=0 bym−1ϕ
′ + ∫

R n(y, z)ym−1−jzj (ϕ(z) − ϕ(y)) dz




= P (
bmym−1ϕ
′ + ∫

R n(y, z) zm − ym

z − y (ϕ(z) − ϕ(y)) dz) = −PBϕ.

4.2 The 2-point function

Fix x ∈ R and α > 0. Let ϕ and ψ be two test functions. The law of the 2-point
function is described completely by

E (ϕ (u(x, t)) ψ (u(x + α, t))) = P (ϕQαψ) .

The BV chain rule extends to a product rule as follows

∂t (ϕQαψ) = Qαψ∂tϕ + ϕ∂tQαψ,

where ϕ(x, t) = 1
2 (ϕ(x, t−) + ϕ(x, t+)) .

We combine the BV chain rule and the conservation law to obtain

∂tϕ(u(x, t)) = −[ϕ][f ]∂xu(x, t), ∂tψ(u(x + α, t)) = −[ψ][f ]∂xu(x + α, t).

23

Therefore,

∂t (ϕ(u(x, t)ψ(x + α, t)) = −ψ[ϕ
′][f ′]∂xu(x, t) − ϕ[ψ′][f ′]∂xu(x + α, t). (97)

We compute the expected value of each of these terms in turn. First, as earlier,
the main assumption is

E (ψ[ϕ
′][f ′]∂xu(x, t)
) (98)

= lim
h→0 1
h E ( f (u+) − f (u−h)
u+ − u−h (ϕ(u+) − ϕ(u−h)) ( ψ+ + ψ−h
2
 )) ,

where ψ+ = ψ(u(x + α, t)) and ψ−h = ψ(u(x + α − h, t)).
We can do away with the mean value. To be explicit, we write the above
expectation as
∫

R
 ∫

R p(y)qh(y, z) ( f (z) − f (y)
z − y (ϕ(z) − ϕ(y))) (Qα+h + Qα) ψ(z)
2 dz dy. (99)

We see that the last term converges to Qαψ(y) as h → 0. Therefore,

E (
ψ[ϕ
′][f ′]∂xu(x, t)
)

= lim
h→0 1
h E ( f (u+) − f (u−h)
u+ − u−h (ϕ(u+) − ϕ(u−h)) Qαψ(u+)
)

= lim
h→0 1
h E ( f (u+) − f (u−h)
u+ − u− (ϕQαψ(u+) − ϕQαψ(u−h)) (100)

− ϕ(u−h) f (u+) − f (u−h)
u+ − u−h (Qαψ(u+) − Qαψ(u−h))
) , (101)

= −P (B (ϕQαψ) − ϕBQαψ) , (102)

where we used (91) to compute the limits in (100) and (101).
We now compute the second term on the right hand side of (97). As in the
calculation above, we can do away with the mean value, and we have

E (ϕ[ψ′][f ′]∂xu(x + α, t))

= lim
h→0
 ∫
R
 ∫
R
 ∫

R p(y)ϕ(y)qα−h(y, z) qh(z, w)
h
 ( f (w) − f (z)
w − z (ψ(w) − ψ(z))
) dw dz dy.

As in the computation of (91) we ﬁnd that the limit of the innermost integral
is Bψ(z). Therefore,

E (ϕ[ψ′][f ′]∂xu(x + α, t)) = −P (ϕQαBψ) . (103)

We combine (97), (102) and (103) to ﬁnd

∂t (P (ϕQαψ)) = P (B (ϕQαψ) − ϕBQαψ + ϕQαBψ) . (104)

But the left hand side is simply

(∂tP)ϕQαψ + P (ϕ∂tQαψ) , (105)

24

and by (92) (∂tP)ϕQαψ = PB (ϕQαψ) . (106)

We now combine (104), (105) and (106) to obtain

P (ϕ∂tQαψ) = P (ϕ (QαB − BQα) ψ) . (107)

This equation holds for all ϕ and ψ in the domain of A. Thus, we may write

∂tQα = (QαB − BQα) = [Qα, B], (108)

and in the limit α ↓ 0 we have
 ∂tA = [A, B]. (109)

5 Hopf ’s method

In this section we derive the Lax equation (22) following Hopf’s method [28].
This method was used by Chabanol and Duchon to derive their kinetic equa-
tions. We show that the calculation works for any convex ﬂux f .
Though our calculations are mainly formal, we begin with the canonical
framework of § 3. Recall that the initial data u0 has law µ0 on Ω. Let u(t; u0) :
[0, ∞) → Ω be a weak solution of (1) with initial data u0, which induces a
sequence of probability measures (µt)t>0 on Ω. To derive an equation for the
ﬂow of measures (µt)t>0, make the assumption that u is diﬀerentiable in t so
that the conservation law can be written for all ϕ ∈ C∞
c (R) as

∂t⟨u(t; u0), ϕ⟩ − ⟨f (u(t; u0)), ϕ
′⟩ = 0. (110)

Here, ′ = ∂x and ⟨·, ·⟩ is the standard duality pairing. Deﬁne the Hopf charac-
teristic functional ˆµt of the law µt

ˆµt(ϕ) = ∫

Ω ei⟨u,ϕ⟩µt(du) (111)

which evolves according to

∂t ˆµt(ϕ) = ∂t
 ∫

Ω ei⟨u,ϕ⟩µt(du) = ∂t
 ∫

Ω ei⟨u(t;u0),ϕ⟩µ0(du0)

= ∫

Ω i ⟨f (u(t; u0), ϕ
′⟩ ei⟨u(t;u0),ϕ⟩µ0(du0)

= ∫

Ω i ⟨f (u), ϕ
′⟩ ei⟨u,ϕ⟩µt(du). (112)

Any set of probability measures (µt)t>0 on Ω that satisﬁes (112) for all ϕ ∈
C∞
c (R) is deﬁned to be a statistical solution of the scalar conservation law—in
particular, the ﬂow of measures generated by the entropy solution is a statistical

25

solution. Assuming that all moments of µt are ﬁnite, the exponential can be
expanded in series (denoting dxn = Π
n
j=1dxj) as

ei⟨u,ϕ⟩ =
 ∞∑

n=0
 in

n!
 ∫

Rn
 n∏

j=1 u(xj)ϕ(xj )dxn.

Let
 Eµt
 [ n∏

i=1 ϕi(u(xi))

]
 = ∫

Ω
 n∏

i=1 ϕi(u(xi))µt(du).

Substituting the expansion for the exponential into (112) yields the inﬁnite
hierarchy
 ∞∑

n=0
 in

n!
 ∫

Rn ∂tEµt
 

 n∏

j=1 u(xj)ϕ(xj )



 dxn

=
 ∞∑

n=0
 in+1

n!
 ∫

Rn+1 Eµt
 

f (u)ϕ
′(x)
 n∏

j=1 u(xj)ϕ(xj )



 dxdxn. (113)

We simplify this hierarchy as follows. If g : Rn → R satisﬁes g(x1, . . . , xn) =
g(xσ(1), . . . xσ(n)) for all permutations σ of {1, . . . , n}, then
∫

Rn g(x1, . . . , xn)dxn = n! ∫

x1<x2<···<xn g(x1, . . . , xn)dxn. (114)

We choose

g(x1, . . . , xn+1) = 1
n
 n+1∑

k=1 Eµt
 

f (u(xk))ϕ
′(xk) ∏

j̸=k u(xj)ϕ(xj )



 ,

in (114) and substitute in (113) to obtain

∞∑

n=0 in ∫

x1<···<xn ∂tEµt
 

 n∏

j=1 u(xj)ϕ(xj )



 dxn

=
 ∞∑

n=0 in+1 ∫

x1<···<xn+1
 n+1∑

k=1 Eµt
 

f (u(xk))ϕ
′(xk) ∏

j̸=k u(xj)ϕ(xj )



 dxn. (115)

Re-indexing the l.h.s. of (115) and subtracting the r.h.s. gives

∞∑

n=1 in ∫

x1<···<xn { ∂tEµt
 

 n∏

j=1 u(xj)



 n∏

j=1 ϕ(xj )

−
 n∑

k=1 Eµt
 

f (u(xk)) ∏

j̸=k u(xj)



 ϕ
′(xk) ∏

j̸=k ϕ(xj )




 dxn = 0.

(116)

26

Finally, the statistical hierarchy (116) can be considerably simpliﬁed with
the closure assumption that (µt)t>0 is the law of a stationary Feller process with
the one and two-point operators P and (Qh)h>0 deﬁned in (85) and (86). With
hi = xi − xi−1 and Qi = Qhi for i = 2, . . . , n,

Eµt
 [ n∏

i=1 ϕi(u(xi))

]

= ∫

R p(du1, t)ϕ1(u1) ∫
R qh2(u1, du2, t)ϕ2(u2) · · · ∫

R qhn (un−1, dun, t)ϕn(un)

= Pϕ1Q2ϕ2 · · · Qnϕn.

Assume the transition measures qh are diﬀerentiable in h. Transferring the
derivative on the test function ϕ
′(xk) onto qhk (uk−1, duk) in (115) and using
integration by parts, the statistical hierarchy is

∞∑

n=1 in ∫

x1<···<xn { ∂tEµt
 

 n∏

j=1 u(xj )





+
 n∑

k=1 ∂xk Eµt
 

f (u(xk)) ∏

j̸=k u(xj)








 n∏

j=1 ϕ(xj )dxn = 0.

Note that the boundary terms in the previous equation vanish due to cancella-
tion of terms and the fact that ϕ ∈ C∞
c (R) has compact support. The density
of tensor products of the form φ(x1, . . . , xn) = ∏n
j=1 ϕ(xj ) in the space of test
functions on {x = (x1, . . . , xn) ∈ Rn : x1 < · · · < xn} implies that for n ∈ N
and x1 < x2 < · · · < xn, the following inﬁnite set of equations hold:

∂tEµt
 

 n∏

j=1 u(xj )



 = −
 n∑

k=1 ∂xk Eµt
 

f (u(xk)) ∏

j̸=k u(xj )



 . (117)

In terms of the operators Q′
i = ∂hiQi (denoting h1 = x1, Q1 = P, Qn+1 = I)
this is
 ∂tEµt
 

 n∏

j=1 u(xj )



 =
 n∑

k=1{PuQ2u · · · Qkf (u)Q′
k+1u · · · Qnu

− PuQ2u · · · Q′
kf (u)Qk+1u · · · Qnu},

or equivalently, in terms of the generator A (using Q′
i = AQi)

∂tEµt
 

 n∏

j=1 u(xj)



 =
 n∑

k=1 PuQ2u · · · Qk [f (u), A] Qk+1u · · · Qnu.

27

One obtains the evolution equation for the 1-point function by taking hi → 0
for all i (i.e., Qi = I for all i), or the equation for the 2-point function by taking
hl+1 = α for l ∈ {1, . . . , n − 1} and hi → 0 for all i ̸= l + 1 (i.e., Ql+1 = Qα and
Qi = I for all i ̸= l + 1):

∂tEµt [(u(x1))
n] =
 n∑

k=1 Puk−1 [f (u), A] un−k (118)

∂tEµt [
(u(x1))
l(u(x1 + α))
n−l] =
 l∑

k=1 Pyk−1 [f (y), A] yl−kQαyn−l

+
 n∑

k=l+1 PylQαyk−(l+1) [f (y), A] yn−k (119)

Using the expression (20) for the generator A, (118) and (119) simplify:

∂tPyn = −
 n∑

k=1 Pyk−1 {b(y)f ′(y)yn−k + ∫

R n(y, dz)(f (z) − f (y))zn−k}

= −P {b(y)f ′(y)(yn)
′ + ∫

R n(y, dz) f (z) − f (y)
z − y (zn − yn)
}

∂t(PylQyn−l)

= −
 l∑

k=1 Pyk−1 {
b(y)f ′(y)yl−kQαyn−l + ∫

R n(y, dz)(f (z) − f (y))zl−kQαzn−l}

−
 n∑

k=l+1 PylQαyk−(l+1) {b(y)f ′(y)yn−k + ∫

R n(y, dz)(f (z) − f (y))zn−k}

= −P {b(y)f ′(y)(yl)
′Qαyn−l + ∫

R n(y, dz) f (z) − f (y)
z − y (zl − yl)Qαzn−l}

− PylQα
 {
b(y)f ′(y)(yn−l)
′ + ∫
R n(y, dz) f (z) − f (y)
z − y (zn−l − yn−l).}

In terms of the operator B deﬁned in (21) the above expressions read

∂tPyn = PByn, ∂t(PylQαyn−l) = P(B(ylQαyn−l)−ylBQαyn−l+ylQαByn−l).

Since B is a linear operator, we approximate ϕ, ψ ∈ C∞
c (R) by polynomials to
obtain the evolution equation for the 1- and 2-point operators:

∂tPϕ = PBϕ, ∂t(PϕQαψ) = P(B(ϕQαψ) − ϕBQαψ + ϕQαBψ).

Therefore we have the evolution ∂tA = [A, B] exactly as in § 4.

28

6 Groeneboom’s solution

In this section we verify that the generator

A(t)ϕ(y) = 1
t ϕ
′(y) + ∫ y

−∞
 1
t1/3 n∗(yt1/3, zt1/3) (ϕ(z) − ϕ(y)) dz (120)

satisﬁes the Lax equation (22) when f (u) = u2/2 and n∗ is given by (17)–(19).
In this case, the evolution of the drift (27) is simply ˙b = −b2. It is clear that
b(y, t) = t−1 is a solution. The equation for the jump density now takes the
form ∂tn(y, z, t) − 1
2t (y − z) (∂yn − ∂zn) = Q(n, n) (121)

with the collision kernel

Q(n, n)(y, z, t) = y − z
2
 ∫ y

z n(y, w, t)n(w, z, t) dw (122)

−n(y, z, t) ∫ z

−∞
 y − w
2 n(z, w, t) dw

−n(y, z, t) ∫ y

−∞
 w − z
2 n(y, w, t)n(y, w, t) dw.

We substitute the ansatz

u = yt1/3, v = zt1/3, s = u − v, n(y, z, t) = t−1/3n∗(u, v), (123)

in (121) and collect terms. We must then verify that

− 2
3 + (u − v
3
 ) J ′(v)
J(v) + ( u
3 − v) J ′(u)
J(u) − 4
3 sK ′(s)
K(s) (124)

= s K ∗ K
K (s) − (
s K ∗ J
J (v) + J ∗ (xK)
J (v))
) + ( J ∗ (xK)
J (u) − s K ∗ J
J (u)
) .

Here x plays the role of a dummy variable in the convolutions J ∗ (xK). Ex-
plicitly, J ∗ (xK)(u) = ∫

R J(u − x)xK(x) dx. Note also that the terms in (124)
are evaluated at the arguments u, v or s = u − v respectively. The functions J
and K are related by the following identities:

x
2J = K ∗ J + J ′ (125)
3
2 J ∗ (xK) = x (K ∗ J) + J (126)

x
3K = 3x(K ∗ K) + 4xK ′ + 2K. (127)

(The argument of each function in these identities is x). We substitute these
identities in (124), and collect the three terms corresponding to the arguments
u,v and s and ﬁnd that (remarkably!) each of them reduces to a polynomial,
and the sum of these three polynomials vanishes.

29

The identities (125)–(127) are proven using the Laplace transform, (18), and
the deﬁnition Ai′′(q) = qAi(q). First, we observe that l = j′/j = −Ai′/Ai solves
the Riccati equation l′ = −q + l2. (128)

As a consequence of the deﬁnition of k in (18) we have

l′ = k/2. (129)

Therefore, we also have

k′ = 2l′′ = −2 + 4ll′ = −2(1 − lk). (130)

Thus, l and k solve an autonomous system. Equation (128) may be rewritten
in terms of j and k as j′′ − (q + k)j = 0. (131)

This is equivalent to (125). Next, if we rewrite (130) in terms of j and k, we
ﬁnd immediately that 3
2 jk′ = (jk)
′ − j. (132)

This is equivalent to (126). Finally, we diﬀerentiate (130) twice and use (128)
to eliminate l to ﬁnd
 k′′ = k2 − 4l(1 − lk) (133)

k′′′ = 3(k2)
′ + 4qk′ + 2k, (134)

which is equivalent to (127).
Here is the Painlev´e property: diﬀerentiate (128) to ﬁnd l′′ = 2l3 − 2lq − 1.
Now rescale τ = −q21/3, w(τ ) = 2−1/3l(q) to see that w solves the second
Painlev´e equation with parameter 1/2 [1].

d
2w
dτ 2 = 2w3 + wτ + 1
2 . (135)

7 Acknowledgements

This material is based upon work supported by the National Science Foundation
under grants DMS 06-05006 and DMS 07-48482. We have beneﬁted greatly from
discussions with Mark Adler, Percy Deift, Irene Gamba, John Hartigan, David
Kinderlehrer, Dave Levermore, Mokshay Madiman, Jonathan Mattingly, Scott
McKinley, Irina Nenciu, Christian Pfrang and David Pollard. We thank them
all. Most of all, we thank Bob Pego for the pleasure of continued collaboration.
Part of this work was completed while the ﬁrst author was visiting the Indian
Statistical Institute, Kolkata.
 30

References

[1] M. J. Ablowitz and P. A. Clarkson, Solitons, nonlinear evolution
equations and inverse scattering, vol. 149 of London Mathematical Society
Lecture Note Series, Cambridge University Press, Cambridge, 1991.

[2] M. Abramowitz and I. A. Stegun, Handbook of mathematical functions
with formulas, graphs, and mathematical tables, vol. 55 of National Bureau
of Standards Applied Mathematics Series, For sale by the Superintendent
of Documents, U.S. Government Printing Oﬃce, Washington, D.C., 1964.

[3] M. Adler and P. Van Moerbeke, Completely integrable systems, Eu-
clidean Lie algebras, and curves, Advances in Mathematics, 38 (1980),
pp. 267–317.

[4] M. Adler and P. van Moerbeke, Linearization of Hamiltonian systems,
Jacobi varieties and representation theory, Advances in Mathematics, 38
(1980), pp. 318–379.

[5] G. Anderson, A. Guionnet, and O. Zeitouni, An introduction to ran-
dom matrices, Cambridge Studies in Advanced Mathematics, 118 (2009).

[6] D. F. Andrews, P. J. Bickel, F. R. Hampel, P. J. Huber, W. H.
Rogers, and J. W. Tukey, Robust estimates of location: Survey and
advances, Princeton University Press, Princeton, N.J., 1972.

[7] D. Applebaum, L´evy processes and stochastic calculus, vol. 116 of Cam-
bridge Studies in Advanced Mathematics, Cambridge University Press,
Cambridge, second ed., 2009.

[8] M. Avallaneda and W. E, Statistical properties of shocks in Burgers
turbulence, Comm. Math. Phys., 172 (1995), pp. 13–38.

[9] J. Bertoin, The inviscid Burgers equation with Brownian initial velocity,
Comm. Math. Phys., 193 (1998), pp. 397–406.

[10] , Some properties of Burgers turbulence with white or stable noise ini-
tial data, in L´evy processes, Birkh¨auser Boston, Boston, MA, 2001, pp. 267–
279.

[11] , Some aspects of additive coalescents, in Proceedings of the Interna-
tional Congress of Mathematicians, Beijing 2002, vol. III, Higher Ed. Press,
2002, pp. 15–23.

[12] J. M. Burgers, Correlation problems in a one-dimensional model of tur-
bulence. I, Nederl. Akad. Wetensch., Proc., 53 (1950), pp. 247–260.

[13] , Correlation problems in a one-dimensional model of turbulence. II,
Nederl. Akad. Wetensch., Proc., 53 (1950), pp. 393–406.

[14] , The nonlinear diﬀusion equation, Dordrecht: Reidel, 1974.

31

[15] L. Carraro and J. Duchon, Solutions statistiques intrins`eques de
l’´equation de Burgers et processus de L´evy, C. R. Acad. Sci. Paris S´er.
I Math., 319 (1994), pp. 855–858.

[16] , ´Equation de Burgers avec conditions initiales `a accroissements
ind´ependants et homog`enes, Ann. Inst. H. Poincar´e Anal. Non Lin´eaire,
15 (1998), pp. 431–458.

[17] M.-L. Chabanol and J. Duchon, Markovian solutions of inviscid Burg-
ers equation, J. Statist. Phys., 114 (2004), pp. 525–534.

[18] , L´evy-process intrinsic statistical solutions of a randomly forced Burg-
ers equation, J. Stat. Phys., 136 (2009), pp. 1095–1104.

[19] H. Chernoff, Estimation of the mode, Ann. Inst. Statist. Math., 16
(1964), pp. 31–41.

[20] C. M. Dafermos, Hyperbolic conservation laws in continuum physics,
Springer-Verlag, New York, 2000.

[21] F. J. Dyson, A Brownian-motion model for the eigenvalues of a random
matrix, Rev. Modern Phys., 3 (1962), pp. 1191–1198.

[22] W. E and E. Vanden Eijnden, Statistical theory for the stochastic Burg-
ers equation in the inviscid limit, Comm. Pure Appl. Math., 53 (2000),
pp. 852–901.

[23] L. Frachebourg and P. A. Martin, Exact statistical properties of the
Burgers equation, J. Fluid Mech., 417 (2000), pp. 323–349.

[24] L. Frachebourg, P. A. Martin, and J. Piasecki, Ballistic aggrega-
tion: a solvable model of irreversible many particles dynamics, Physica A:
Statistical Mechanics and its Applications, 279 (2000), pp. 69 – 99.

[25] R. K. Getoor, Splitting times and shift functionals, Z. Wahrsch. Verw.
Gebiete, 47 (1979), pp. 69–81.

[26] P. Groeneboom, Brownian motion with a parabolic drift and Airy func-
tions, Probab. Theory Related Fields, 81 (1989), pp. 79–109.

[27] E. Hopf, The partial diﬀerential equation ut + uux = µxx, Comm. Pure
Appl. Math., 3 (1950), pp. 201–230.

[28] , Statistical hydromechanics and functional calculus, J. Rational Mech.
Anal., 1 (1952), pp. 87–123.

[29] S. V. Kerov, Asymptotic representation theory of the symmetric group
and its applications in analysis, vol. 219 of Translations of Mathematical
Monographs, American Mathematical Society, Providence, RI, 2003. Trans-
lated from the Russian manuscript by N. V. Tsilevich, With a foreword by
A. Vershik and comments by G. Olshanski.

32

[30] S. Kida, Asymptotic properties of Burgers turbulence, J. Fluid Mech., 93
(1979), pp. 337–377.

[31] J. Kim and D. Pollard, Cube root asymptotics, Ann. Statist., 18 (1990),
pp. 191–219.

[32] P. D. Lax, Hyperbolic systems of conservation laws. II, Comm. Pure Appl.
Math., 10 (1957), pp. 537–566.

[33] P. D. Lax, Hyperbolic systems of conservation laws and the mathematical
theory of shock waves, Society for Industrial and Applied Mathematics,
Philadelphia, Pa., 1973. Conference Board of the Mathematical Sciences
Regional Conference Series in Applied Mathematics, No. 11.

[34] , Functional analysis, Pure and Applied Mathematics (New York),
Wiley-Interscience [John Wiley & Sons], New York, 2002.

[35] S. Manakov, Note on the integration of Euler’s equations of the dynamics
of an n-dimensional rigid body, Functional Analysis and its Applications,
10 (1976), pp. 328–329.

[36] J. C. Mattingly and S. A. McKinley, Shell models of turbulence. Work
in progress, 2009.

[37] J. C. Mattingly, T. Suidan, and E. Vanden-Eijnden, Simple systems
with anomalous dissipation and energy cascade, Comm. Math. Phys., 276
(2007), pp. 189–220.

[38] G. Menon and R. L. Pego, Universality classes in Burgers turbulence,
Comm. Math. Phys., 273 (2007), pp. 177–202.

[39] P. A. Meyer, R. T. Smythe, and J. B. Walsh, Birth and death of
Markov processes, in Proceedings of the Sixth Berkeley Symposium on
Mathematical Statistics and Probability (Univ. California, Berkeley, Calif.,
1970/1971), Vol. III: Probability theory, Berkeley, Calif., 1972, Univ. Cal-
ifornia Press, pp. 295–305.

[40] Z.-S. She, E. Aurell, and U. Frisch, The inviscid Burgers equa-
tion with initial data of Brownian type, Comm. Math. Phys., 148 (1992),
pp. 623–641.

[41] D. W. Stroock, Markov processes from K. Itˆo’s perspective, vol. 155 of
Annals of Mathematics Studies, Princeton University Press, Princeton, NJ,
2003.

[42] C. A. Tracy and H. Widom, Level-spacing distributions and the Airy
kernel, Comm. Math. Phys., 159 (1994), pp. 151–174.

[43] A. I. Vol′pert, Spaces BV and quasilinear equations, Mat. Sb. (N.S.), 73
(115) (1967), pp. 255–302.
 33

[44] J. von Neumann, Collected works. Vol. VI: Theory of games, astro-
physics, hydrodynamics and meteorology, General editor: A. H. Taub. A
Pergamon Press Book, The Macmillan Co., New York, 1963.

[45] M. Winkel, Limit clusters in the inviscid Burgers turbulence with certain
random initial velocities, J. Statist. Phys., 107 (2002), pp. 893–917.

[46] W. A. Woyczy´nski, Burgers-KPZ turbulence, vol. 1700 of Lecture Notes
in Mathematics, Springer-Verlag, Berlin, 1998. G¨ottingen lectures.

34
