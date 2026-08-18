<!-- source: https://export.arxiv.org/pdf/math/0010174v1.pdf | converted from PDF -->

arXiv:math/0010174v1  [math.DS]  17 Oct 2000
THE HILBERT 16-TH PROBLEM AND AN ESTIMATE FOR
CYCLICITY OF AN ELEMENTARY POLYCYCLE

V.KALOSHIN

1. Introduction

Consider a polynomial line ﬁeld on the real (x, y)-plane

dy
dx = Pn(x, y)
Qn(x, y) , Pn, Qn − polynomials , deg Pn, Qn ≤ n.(1)
 H(n) = uniform bound for the number of limit cycle of (1).

One way to formulate the Hilbert 16-th Problem is the following:
Hilbert 16-th Problem (HP). Find an estimate for H(n) for any n ∈ Z+.
We shall discuss problems related to the following:
Existential Hilbert 16-th Problem (EHP). Prove that H(n) < ∞ for any
n ∈ Z+.
The problem about ﬁniteness of number of limit cycles for an individual polyno-
mial line ﬁeld (1) is called Dulac problem since the pioneering work of Dulac who
claimed in 1923 to solve this problem, but an error was found by Ilyashenko.
The Dulac problem was solved by two independent and rather diﬀerent proofs
given almost simultaneously by Ilyashenko [I] and Ecalle [E]. However, both proofs
do not allow any generalization to solve Existential Hilbert Problem.
Consider the equation (1) for diﬀerent polynomials (Pn(x, y), Qn(x, y)) as the
family of line ﬁelds on R2 depending on parameters of the polynomials. Using a
central projection π : S
2 → R2 and homogenuity with respect to parameters of the
equation (1) (line ﬁelds λPn(x, y)/λQn(x, y) and Pn(x, y)/Qn(x, y) for any λ ̸= 0
are the same) one can construct a ﬁnite parameter family of analytic line ﬁelds
on the shpere S
2 with a compact parameter base B (see e.g. [IY2] for details).
After this reduction Existential Hilbert Problem becomes a particular case of the
following
Global Finiteness Conjecture (GFC). (see e.g. [R]) For any family of line
ﬁelds on S
2 with a compact parameter base B the number of limit cycles is uniformly
bounded over all parameter values.
We refer the reader to the volumes [S] and [IY2] where various development of
these and related problems are discussed. Families of analytic ﬁelds are extremely
diﬃcult to analyze. In the middle of 80’s Arnold [AAI] proposed to consider generic
families of smooth vector ﬁelds on S
2. A smooth analog of Global Finiteness Con-
jecture is the following

The ﬁrst author is partially supported by the Sloan Dissertation Fellowship and the American
Institute of Mathematics Five-year Fellowship.
 1

2 Bifurcation of polycycles

Hilbert-Arnold Problem (HAP). (e.g.[IY2]) Prove that in a generic ﬁnite
parameter of vector ﬁelds on the sphere S2 with compact base B, the number of
limit cycles is uniformly bounded.
Assume for a moment that a polynomial (or a generic smooth) vector ﬁeld on
the sphere §2 has an inﬁnite number of limit cycles. By the Poincare-Bendixon
Theorem, any limit cycle should surround an equilibrium point and, since our vec-
tor ﬁeld has at most ﬁnitely many equilibria, there should be an inﬁnite “nested”
sequence around one of equilibria. Then those “nested” limit cycles have to accu-
mulate (in the sense of Hausdorﬀ metric) to a certain contour (polygon) consisting
of equilibria (as vertices) and separatric curves (sides of that polygon) connecting
them. Such objects are called polycycles. It turns out that a possible solution to
Hilbert-Arnold Problem reduces to investigation of bifurcation of polycycles. Let
us give several deﬁnitions.

Deﬁnition 1. A polycycle γ of a vector ﬁeld on the sphere S
2 is a cyclically ordered
collection of equilibrium points p1, . . . , pk (with possible repetitions) and diﬀerent
arcs γ1, . . . , γk (integral curves of the vector ﬁeld) connecting them in the speciﬁc
order: the j-th arc γj connects pj with pj+1 for j = 1, . . . , k.

Deﬁnition 2. Let { ˙x = v(x, ǫ)}ǫ∈Bn , x ∈ S
2, be an n-parameter family of vector
ﬁelds on S
2 having a polycycle γ for the critical parameter value ǫ∗. The polycycle
γ has cyclicity µ in the family {v(x, ǫ)}ǫ∈Bn if there exist neighborhoods U and V
such that S
2 ⊇ U ⊃ γ, B ⊇ V ∈ ǫ∗ and for any ǫ ∈ V the ﬁeld v(·, ǫ) has no more
than µ limit cycles inside U and µ is the minimal number with this property.

Examples 1) In a generic n-parameter family, the maximal multiplicity of a
degenerate limit cycle does not exceed n + 1, e.g. in codimension 1 a semistable
limit cycle has cyclicity 2. Thus, the cyclicity of a trivial polycycle (a polycycle
without singular points) in a generic n-parameter family does not exceed n + 1.
2) (Andronow-Leontovich, 1930s; Hopf, 1940s). A nontrivial polycycle of codi-
mension 1 has cyclicity at most 1.
3) (Takens, Bogdanov, Leontovich, Mourtada, Grozovskii, early 1970s-1993 (see
[G], [KS] and references there)). A nontrivial polycycle of codimension 2 has cyclic-
ity at most 2.

Deﬁnition 3. The bifurcation number B(k) is the maximal cyclicity of a nontrivial
polycycle occurring in a generic k-parameter family.

The deﬁnition of B(k) does not depend on a choice of the base of the family, it
depends only on the number k of parameters.
Local Hilbert-Arnold Problem (LHAP) e.g.[IY1] Prove that for any ﬁnite
k, the bifurcation number B(k) is ﬁnite and ﬁnd an upper estimate for B(k).
It turns out that a solution to Local Hilbert-Arnold Problem implies a solution
to Hilbert-Arnold Problem.
Similarly to the generic smooth vector ﬁelds, in the case of analytic vector ﬁelds
one can deﬁne so-called a limit periodic set [FP], [R], [IY1], which is either a poly-
cycle or has an arc of equilibrium points1, and formulate
Local Finiteness Conjecture (LFC) e.g.[R] Prove that any limit periodic set
occuring in an analytic family of vector ﬁelds on §2 has ﬁnite cyclicity in this family.

1 generic vector ﬁelds can not have an arc of equilibrium points

V. Kaloshin 3

Smooth vector ﬁelds are more ﬂexible then analytic vector ﬁelds and easier to
analyze. A strategy to attack Existential Hilbert Problem proposed by Arnold
[AAI] (see also [IK]) is ﬁrst understand generic smooth vector ﬁelds and then try to
apply developed methods to analytic vector ﬁelds. Let us summarize the discussion
in the form of diagramm:

          L F CE H P  G F C

H A P L H A P
  F E C

RS & SP ?

Figure 1.

Now we shall formulate the Main Result of the paper.

Deﬁnition 4. A singular (equilibrium) point of a vector ﬁeld on the two-sphere is
called elementary if at least one eigenvalue of its linear part is nonzero. A polycycle
is called an elementary polycycle if all its singularities are elementary.

The Local Hilbert-Arnold problem was solved under the additional assumption
that a polycycle have elementary singularities only.

Deﬁnition 5. The elementary bifurcation number E(k) is the maximal cyclicity of
a nontrivial elementary polycycle occurring in a generic k-parameter family.

From examples 2) and 3) above it follows that

E(1) = 1, E(2) = 2.

Information about behavior of the function k ↦→ E(k) has been obtained recently.
The First crucial step was done by Ilyashenko and Yakovenko:
Finiteness Theorem (Ilyashenko and Yakovenko [IY3]) For any n the elemen-
tary bifurcation number E(n) is ﬁnite.

Corollary 1. Under the assumption that families of vector ﬁelds have elementary
singularities only the global Hilbert-Arnold conjecture is solved, i.e. any generic
ﬁnite parameter family of vector ﬁelds on the sphere S
2 with a compact base and
only elementary singularities has a uniform upper bound for the number of limit
cycles.

Main Theorem. For any k ∈ Z+

E(k) ≤ 225k2 .(2)

This is the ﬁrst known suﬃciently general estimate for cyclicity of polycycle. The
case of a polycycle consisting only one singular point with no arcs at all, is well

4 Bifurcation of polycycles

known. An elementary equilibrium point can generate limit cycles in its small
neighborhood if it is a slow focus, that is the linearization matrix has a pair of two
imaginary eigenvalues. This bifurcation was investigated by Takens [Ta].

Corollary 2. Under the assumption that all the polycycles are elementary the Main
Theorem gives a solution to the Local Hilbert-Arnold problem.

The Main Theorem is an improvement of Ilyashenko-Yakovenko Finiteness The-
orem. It is a great pleasure for the author to say that the paper of Ilyashenko-
Yakovenko [IY3] was a corner stone for the present paper. In [IY3] the authors
made an extremely important step: they found a pass from bifurcation theory to
singularity theory using the Khovanskii reduction method [Kh]. We follow this pass
up to some point and using some new ideas getting the ﬁrst suﬃciently general
estimate for the cyclicity of polycycles. To make this paper readable we have to
reproduce some points from [IY3] and we are sorry for repetition, but we think that
it is necessary for a better understanding.

1.1. Three stages of the proof. The proof of the Main Theorem consists of three
steps. Relation to the proof of the Finiteness Theorem [IY3] is discussed after this
short description.
Step 1. Normal forms for local families of vector ﬁelds and their integration In
section 2 we use normal forms to establish an explicit form for the Poincare corre-
spondence map near equilibrium points on the polycycle under consideration. In
[IY3] it is shown that these maps satisfy Pfaﬃan (polynomial diﬀerential) equa-
tions with coeﬃcient of polynomials depending smoothly on the parameters of the
family. As the result a basic system of equations for determination of limit cycles
is obtained.
Step 2. the Khovanskii reduction method In section 3 we discuss a variation
of the Khovanskii method [Kh]. This method allows us to investigate systems
of equations that involve functions satisfying Pfaﬃan equations. In section 4 we
present a formal reduction from the basic system to a mixed functional-Pfaﬃan
system which is done in [IY3] together with upper bounds for degrees of involved
into the procedure polynomials. After application of the Khovanskii method to the
mixed functional-Pfaﬃan system we obtain several chain maps, the maps of the
form
 x ↦→ (P1, . . . , Pn) ◦ (x, f (x), f ′(x), . . . , f (n)(x)),(3)

where P = (P1, . . . , Pn) is a vector-polynomial given by its coordinate functions of
known degree and f is a generic function. The problem of estimating the number of
limit cycles reduces to estimating the number of regular preimages of some special
points by the chain map. Special points form an open cone-like semialgebraic set
K in the image.
Denote by F the map F : x ↦→ P ◦ (x, f (x), f ′(x), . . . , f (n)(x)) which is called
the n-th jet of f . Denote by LF the linearization of F at point x = 0.
Step 3. Bezout’s theorem for the Chain maps In section 5 we construct an
algebraic set Σ in the image of F (in the space of n-jets). If F is transversal to Σ,
then the number of preimages of any point a from a set of special points K is the
same for F and its linearization LF at zero, namely,

#{x : P ◦ F (x) = a} = #{x : P ◦ LF (x) = a} ≤
 k∏

j=1 deg Pj.(4)
 V. Kaloshin 5

But LF is a linear map and one can apply Bezout’s theorem to estimate the right-
hand side of the equality. This observation completes the proof of the Main Theo-
rem.
Let us discuss relation of this proof to the proof of the Finiteness Theorem by
Ilyashenko & Yakovenko [IY3]. Step 1 of both proof is the same. We just refer
to appropriate statements in [IY3]. Step 2 in this proof is slightly diﬀerent for the
one in [IY3]. After application of the Khovanskii method they obtain the same
collection of chain maps of the form (3). However, they investigate the number of
regular preimages of points in the image by the chain maps without any restriction
on those points. In the present proof, using additional arguments in the Khovanskii
method, we reduce consideration to only preimages of special points, i.e. points from
a tiny cone-like set in the image. At his point our proof goes independently, because
investigation of the number of regular preimages of special points is more concrete
problem.
Let us present a more detailed description of each step of the proof.

1.2. Normal forms of local families and their integration. This step is done
in [IY3] §0.3 and §1. We just say several words about it.
It turns out that in a small neighborhood of an elementary equilibrium point
there exists a ﬁnitely diﬀerentiable normal coordinates (in the Cartesian product of
the phase space and the parameter space), so-called normal forms of an equilibrium
point. The list of ﬁnitely diﬀerentiable normal forms was obtained in [IY1]. The
main feature of the list: all normal forms are polynomial and integrable. The smaller
the neighborhood of a normal form, the higher its smoothness. So smoothness can
be chosen arbitrary large. All normal forms are summarized in Table 1 sect.2.
In a small neighborhood of an elementary equilibrium point one can choose two
small segments, say Σ− and Σ+, transversal to the vector ﬁeld for the critical value
of parameter and explicitly calculate the Poincare (correspondence) map which
maps a point from one segment say Σ− along the corresponding phase curve to a
point from the other segment Σ+ (see Fig.1). For an appropriate choice of segments
Σ−, Σ+ and coordinate functions x, in Σ−, Σ+ respectively, and a smooth function
λ(ǫ) in the original parameter ǫ of the family the Poincare return map ∆ǫ : x → y
can be explicitly computed. Moreover, there is a Pfaﬃan (with polynomial coeﬃ-
cients) 1-form ω of the form

P (x, y, λ(ǫ)) dx + Q(x, y, λ(ǫ)) dy = 0(5)

which vanishes on the graph y = ∆ǫ(x). For example, in the case of a nonresonant
saddle ∆ǫ(x) = x
λ(ǫ) and ω = x dy + λ(ǫ)y dx. See Table 1 for the other cases.

1.3. Singular-regular systems determining the number of limit cycles.
We present a description of a system of equations determining the number of limit
cycles. For a detailed description we refer to [IY3] §0.4 and §1.4.
Let γ be a polycycle, occurring in a generic k parameter family, with equilibrium
points p1, . . . , pn (possibly with repetitions) and connecting phase curves γ1, . . . , γn
such that γj connects equilibria pj with pj+1 respectively. For each 1 ≤ j ≤ n
endow the point pj with a Cr-normal coordinate charts Uj. Consider transversal
segments “entrance” Σ−
j and “exit” Σ+
j which are parallel to coordinate axis of
the normal chart. The phase curve γj−1 enters the neighborhood Uj through Σ−
j
and the phase curve γj exists Uj through Σ+
j . The normal coordinates induce

6 Bifurcation of polycycles
 O2

PSfrag replacements
 Σ+
3

Σ+
3
 Σ+
2

Σ+
1
 Σ−
3

Σ−
3

Σ−
1
 Σ−
2

p2
 p3

p1
 ∆1 ∆2
 ∆3
∆3

f1
 f2
f3

Figure 2. Construction of entrance and exit transversals

coordinates xj and yj on Σ−
j and Σ+
j respectively. For some parameter values the
corresponding vector ﬁeld deﬁnes the following collection of Poincare maps:
∆j(·, ǫ) : xj → yj = ∆j(xj , ǫ), j = 1, . . . , n

fj(·, ǫ) : yj → xj+1 = fj(yj, ǫ), j = 1, . . . , n ( mod n),
(6)

where ∆j(·, ǫ) is a local Poincare map form the “entrance”segment Σ−
j to the “exit”
segment Σ+
j and fj(·, ǫ) is a semilocal Poincare map along the phase curve γj form
the “exit” segment Σ+
j to the “entrance” segment Σ−
j+1.
Now we decompose the monodromy map (the Poincare ﬁrst return map) along
the polycycle γ into the chain of the local singular maps ∆j and the semilocal
regular maps fj of the total length 2n. Limit cycles correspond to the ﬁxed points
of the monodromy. But instead of writing one equation for the ﬁxed points of
the monodromy we consider a system of 2n equations, which will be called the
preliminary basic system:
{yj = ∆j (xj, ǫ) j = 1, . . . , n
xj+1 = fj(yj, ǫ), j = 1, . . . , n ( mod n)
(7)

Recall that xj’s are Cr-normal coordinates on Σ−
j and yj’s are Cr-normal coor-
dinates on Σ+
j . Thus the system involves Cr-smooth regular functions fj’s and the
maps ∆j from the list (modulo reparametrization ǫ → λ(ǫ)), that are essentially
singular. The problem now is to estimate the number of solutions uniformly over
all suﬃciently small parameter values.

1.4. The Khovansky reduction method. The system (7) is not easy to analyze,
because it has the singular functions ∆j. The ﬁrst key idea of the second step is
to replace these singular equations in (7) by the Pfaﬃan (polynomial diﬀerential)

V. Kaloshin 7

equations in the form (5). As a result we obtain the mixed functional-Pfaﬃan
system of the form {ωj = 0
Fj(x, y, ǫ) = 0 j = 1, . . . , n

ωj = Pj dxj + Qj dyj, Fj(x, y, ǫ) = xj+1 − fJ (yj, ǫ)

(x, y) = (x1, y1, . . . , xn, yn) ∈ (R2n, 0), ǫ ∈ (Rk, 0),

(8)

where ωj are Pfaﬃan forms in the form (5). This system can be interpreted as fol-
lows: one has to take an integral manifold Γ for the Pfaﬃan equations of the system
(8) and compute its intersection with the level set F −1(0), where F : (R2n, 0) → Rn

is the map with the coordinate functions Fj. In order to estimate number of iso-
lated solutions to (7) one needs to estimate the number of isolated points in the
intersection. It turns out that it is suﬃcient to analyze only transversal intersec-
tions of Γ with a generic level set F −1(b) for b suﬃciently close to the origin in
Rn. Since the integral manifold and the level sets have complimentary dimensions,
a transversal intersection always consists of isolated points, which we call regular
solutions to the system (8). What we are interested in is the upper estimate for
their number, uniform over all the integral manifolds Γ and all suﬃciently small
values of the parameters.
The method suggested by A. Khovanski [Kh] allows us to replace a mixed
functional-Pfaﬃan system of the form (8) by the two systems of a similar form,
but containing n − 1 Pfaﬃan equations, n “simple” functional equations, and one
special functional equation: the number of regular solutions to the initial equation
is bounded from above by the sum of the number of regular solutions to these two
auxiliary systems.

1.5. aP -stratiﬁcation and Bezout’s theorem for a chain map P ◦ F with
a generic F . In this section we shall discuss the formula (4). The problem of
estimating the maximal number of small isolated preimages is equally diﬃcult for
a chain map P ◦ F : Rn → Rn with a generic map F : Rn → RN , N ≥ n and for
a chain map P ◦ jnF : Rn → Rn with the n-jet of a generic map. We shall show
that if the map F (resp. jnF ) satisﬁes a transversality condition in an appropriate
space, then F (resp. jnF ) can be replaced by its linear part and we can apply
the Bezout theorem to estimate the maximal number of small inverse images of
the chain P ◦ F (resp. P ◦ jnF ) uniformly over all sequences of numbers ǫ1, . . . , ǫn
decreasing suﬃciently fast to 0. So, to simplify notations we shall consider a chain
map of the form P ◦ F : Rn → Rn.

1.5.1. A Heuristic description. Consider a chain map P ◦ F : R2 → R2, where
F : R2 → RN is a generic Ck smooth map, k > 2 and P = (P1, P2) : RN → R2

is a polynomial of degree d. Fix a small positive r. We would like to estimate the
maximal number of small preimages

#{x ∈ Br(0) : P1 ◦ F (x) = ǫ, P2 ◦ F (x) = 0}(9)

for a small enough ǫ.
To show the idea put N = 3, P1(x, y, z) = x
2 + y2, and P2(x, y, z) = xy. Assume
also that F (0) = 0. Denote the level set by Vǫ = {P1 = ǫ, P2 = 0}. The level set
Vǫ for ǫ > 0 consists of 4 parallel lines (see Figure 2).

8 Bifurcation of polycycles

Notice that in our notation the number of intersections of F (Br(0)) with Vǫ
equals the number of preimages of the point (ǫ, 0) (9).
It is easy to see from Figure 2 that if F is transversal to V0 it is transversal to
Vǫ for any small ǫ > 0. Moreover, the number of intersections F (Br(0)) with Vǫ
equals 4 (see the points P1, . . . , P4 in Figure 2).
Another way to calculate the same number is as follows. Let us replace F by
its linear part LF at zero. Then #{x ∈ Br(0) : P1 ◦ F (x) = ǫ, P2 ◦ F (x) = 0} =
#{x ∈ Br(0) : P1 ◦ LF (x) = ǫ, P2 ◦ LF (x) = 0} and solving this polynomial system
also yields 4.
 F(B)

P4

PSfrag replacements
 Vǫ

V0
 P1P2

P3

Figure 3. The Idealistic Example

The idea behind this picture is the following: Consider an arbitrary N and a
polynomial P = (P1, P2) : RN → R2 of degree at most d, N > 2. Deﬁne the
semialgebraic variety Vǫ = (P1, P2)
−1(ǫ, 0) as the level set.
Assume for simplicity that for any small ǫ ̸= 0 the level set Vǫ is a manifold of
codimension 2. We shall get rid of this assumption later (see Theorem 37 b)). It

V. Kaloshin 9

turns out that there exists a stratiﬁcation of V0 by semialgebraic strata (V0, V0) (a
decomposition of V0 into a disjoint union of semialgebraic sets see deﬁnition 30),
depending on P only, such that

(10) F is transversal to (V0, V0) =⇒ F is transversal to Vǫ

Condition (10) is written for n = 2. Below we shall use its analogue for an arbitrary
n. Let us present the key Proposition below and the simple of proof of it. This
proof gives an insight to the main idea of the third step.

Proposition 1. Let Br(a) be the r-ball centered at the point a ∈ R2 and let LF,a
denote the linearization of F at the point a. Under condition (10), the number
of intersections of the image F (Br(a)) with Vǫ coincides with the number of in-
tersections of the image LF,a(Br(a)) with Vǫ, provided r is small enough. That
is #{x ∈ Br(0) : (P1, P2) ◦ F (x) = (ǫ, 0)} =

#{x ∈ Br(0) : (P1, P2) ◦ LF,a(x) = (ǫ, 0)}.
(11)

The argument below is independent of the codimension of Vǫ. We only need
condition (10) and the fact that the codimension of Vǫ coincides with the dimension
of the preimage of a chain map P ◦ F .
Proof Consider the 1-parameter family of maps Ft = tF + (1 − t)LF deforming
the linear part of F into F . Clearly, F1 ≡ F and F0 ≡ LF . Fix a small r > 0.
Since, F is transversal to V0 at 0 all Ft are transversal to V0 at 0. Condition (10)
implies that for all small ǫ and all t ∈ [0, 1] Ft is transversal to Vǫ.
Therefore, the number of intersections of Ft(Br(0)) with Vǫ is independent of t.
Indeed, assume that #{Ft1 (Br(0)) ∩ Vǫ} ̸= #{Ft2 (Br(0)) ∩ Vǫ} for some t1 < t2.
Then as t1 increases to t2 there is a point t∗ where the number of intersections
drops or jumps. At this point t∗ the condition of transversality of Ft∗ and Vǫ must
fail. This completes the proof of the proposition.

2. Normal forms for local families and their applications.

In this section we present the functional–Pfaﬃan system whose number of solu-
tions bounds from above the number of limit cycles. This system was obtained in
[IY3].

2.1. Local families and polynomial normal forms. A local family of planar
vector ﬁelds is the germ of a map,

v : (R2, 0) × (Rk, 0) → (R2, 0), (x, y, ǫ) ↦→ v(x, y, ǫ).

A Cr-smooth conjugacy between two local families v and w of the above form is a
map
 H : (R2, 0) × (Rk, 0) → (R2, 0), (x, y, ǫ) ↦→ H(x, y, ǫ),

such that
 H∗v(x, y, ǫ) = w(H(x, y, ǫ), ǫ),

where H∗ stands for the Jacobian matrix with respect to the variables x, y. (this
deﬁnition does not yet allow for reparameterization of a local family). Two families
are ﬁnitely diﬀerentiably equivalent, if for any r < ∞ there exists a Cr-conjugacy

10 Bifurcation of polycycles

between them. The two families v, w are orbitally equivalent, if there exists the
germ of a nonvanishing function φ : (R2, 0) × (Rk, 0) → R1 such that v is equivalent
to φ · w.
To allow for a reparameterization of local families, we say that a family v(·, ǫ) is
induced from another family w(·, λ), λ ∈ (Rm, 0), if v(·, ǫ) = w(·, λ(ǫ)), where λ(ǫ)
is the germ of a smooth map (Rk, 0) → (Rm, 0). The number of new parameters m
may be diﬀerent from k.
Assume that the family w(·, λ) is global (i.e. the expression w(x, y, λ) makes
sense for all (x, y, λ) ∈ Rm+2); this happens in particular when w is polynomial
in all its arguments. Restricting the parameters λ onto a small neighborhood of a
certain point (0, 0, c) ∈ R2 × Rm, we obtain a localization of the global family w,
which formally becomes a local family after the parallel translation λ ↦→ λ − c.

Deﬁnition 6. 1. A local family v = v(·, λ) is ﬁnitely smooth orbital versal unfold-
ing (in short, versal unfolding) of the germ v(·, 0), if any other local family unfolding
this germ is ﬁnitely diﬀerentiable orbitally equivalent to a family induced from v.
2. A polynomial family w(·, λ), λ ∈ Rm, is a global ﬁnitely smooth orbital versal
unfolding (in short, global versal unfolding) for a certain class of local families of
vector ﬁelds, if any local family from this class is ﬁnitely diﬀerentiable orbitally
equivalent to a local family induced from some localization of w.

To investigate a versal unfolding means to investigate at the same time all smooth
local ﬁnite-parametric families which unfold the same germ v(·, 0). The main result
describing versal unfoldings of germs of elementary singularities on the plane, is
given by the following theorem.

Theorem 7. [IY3] Suppose that a generic ﬁnite-parameter family of smooth vector
ﬁelds on the plane possesses an elementary singular point for a certain value of the
parameters. If this point has at least one hyperbolic sector, than the family is ﬁnitely
diﬀerentiable orbitally equivalent to a family induced from some localization of one
of the families given in the second column of Table 1.

Table 1. Unfolding of elementary equilibrium points on the plane.

V. Kaloshin 11

Type Normal forms Poincare Pfaﬃan equations
Correspondence maps
˙x = x,
S0 ˙y = −λy. y = xλ, x dy − λy dx = 0
x > 0, y > 0
λ = λ0 ∈ R1

˙x = x ( n
m + Pµ(u, λ)) ,
˙y = −y.
Sµ 0 = m log y + y Pµ(yn, λ) dx −
u = u(x, y) = xm yn, ∫ yn

xm du
uPµ(u,λ) . ( n
m + Pµ(yn, λ)) ×
Pµ(u, λ) = ±u
µ(1 + λµu
µ) x > 0, y > 0 xPµ(xm, λ) dy = 0
+Wµ−1(u, λ),
λ = (λ1, . . . , λµ)
˙x = Qµ(x, λ),
˙y = −y. y = C(λ)x,
Dc
µ C = ∫ 1
−1 du
Qµ(u,λ) , x dy − y dx = 0
Qµ(x, λ) = ±xµ+1(1 + λµxµ) x, y ∈ R1

+Wµ−1(x, λ), 0 = log y +
Dh
µ λ = (λ1, . . . , λµ) ∫ 1
x du
Qµ(u,λ) Qµ(x, λ) dy −
y > 0, x ∈ R1 y dx = 0

In what follows the following notation for elementary equilibria (the subscript
indicates the degree of degeneracy):
S0— Nonresonant saddle;
Sµ— Resonant saddle whose quotient equation (the diﬀerential equation for
u = x
m yn below) has the singular point of multiplicity µ + 1 at the origin, µ ≥ 1;
if we want to specify explicitly the resonance between the eigenvalues, we use the
extended notation S(n:m)
µ assuming that the natural numbers m, n are mutually
prime;
Dµ— Degenerate saddlenode of multiplicity µ;
Wµ−1(z, λ) = λ0 + λ1z + · · · + λµ−1zµ−1 is a Weierstrass polynomial of degree
µ − 1.
Diﬀerent technical remarks concerning this table see in [IY3] §1.1. We just brieﬂy
describe each column.
The ﬁrst two columns do not need extra words. In the third column of the
table the Poincare correspondence maps y = ∆(x, λ) for the polynomial normal
forms are given. They are implicitly deﬁned by the equations relating x to y,
these equations depending explicitly on the parameters λ and thus implicitly on
the original parameters ǫ. The choice of segments transversal to the phase curves
of the family described in ﬁg. 1.

2.2. Basic system. Here we describe the system of equations which will be ana-
lyzed from now on. Assume that a polycycle occurs in a generic k-parameter family
of vector ﬁelds, and all the vertices of the polycycle are elementary.
Then the number n of vertices is ≤ k. Moreover, one can claim that each vertex
is of one of the types Sµj , µj ≥ 0, or Dh,c
µj , µj ≥ 1, and ∑ µj ≤ k (see [IY3] §1.4).
Next, we proceed with introducing the normalizing Cp-smooth local coordinates
near each elementary vertex, as this is described above (the exact order of smooth-
ness will be speciﬁed later on). Then a pair of Cp-smooth transversals may be
chosen near each vertex, and endowed with local Cp-smooth charts xj, yj in such

12 Bifurcation of polycycles

 − (1,x   )(−1,x   )
 (x,1)
 x=1
  +

y=1
y=−1

(x,1)
 y=1

x=1

y=1

PSfrag replacements

x
 y = ∆(x, λ)

y = ∆(x, λ)
 y = ∆(x, λ)

Dc
µ

Sµ
 Dh
µ

˜q
q
p
 Figure 4. Poincare Correspondence maps

a way that the correspondence map taking a point with a coordinate xj on the
“entrance” transversal to a point with the coordinate yj on the “exit” transversal,
will be of one of the standard types listed in Table 1.
More precisely, for each vertex j = 1, . . . , n Theorem 7 yields the localization
point cj = (0, . . . , 0, cj) ∈ Rµj +1, where cj ∈ R1 is the formal invariant of the
unperturbed singular point, and also if j-th vertex is a resonant saddle, then the
rational hyperbolicity ratio n : m is explicitly speciﬁed.
Denote by ∆l,µ(x, λ) the correspondence map for each of the four types of singu-
larities from Table 1, l = S0, Sµ, Dc
µ or Dh
µ, with the corresponding index µ ∈ N (for
l = S0 by deﬁnition µ = 0). In case Sµ with µ > 0 we consider the mutually prime
pair of natural numbers as an additional parameter of the corresponding map, so
in this case the rigorous notation would be ∆Sµ,µ(x, λ; [n, m]).

Deﬁnition 8. 1. The unspeciﬁed basic system for determination of limit cycles
occurring in k-parametric families of vector ﬁelds is the system of n regular and
n singular functional equations in 2n variables xj, yj, depending on parameters
λ
j, nj, mj, ǫ, {yj = ∆lj ,µj (xj , λ
j; [nj, mj]), λ
j ∈ Rµj +1,
xj+1 = fj(yj, ǫ), ǫ ∈ (Rk, 0).

j = 1, . . . , n mod (n), lj ∈ {S0, Sµ, Dc
µ, Dh
µ},

nj, mj ∈ N, µj ∈ Z+, ∑ µj ≤ k, n ≤ k,

∆ depends on nj, mj only if lj = Sµ with µ > 0.

(12)

2. A speciﬁed basic system is one of a ﬁnite number of unspeciﬁed basic sys-
tems together with an explicit indication of speciﬁcation, which by deﬁnition is the
collection of:
 V. Kaloshin 13

• localization points cj = (0, . . . , 0, cj) ∈ Rµj +1; in particular this means that
hyperbolicity ratios of all nonresonant saddles are explicitly given;
• hyperbolicity ratios nj : mj for all resonant saddles;
• smooth functions fj(x, ǫ) depending on the parameters ǫ, are deﬁned in some
open neighborhoods (Rk+1, 0)j and fj(0, 0) = 0;
• characteristic size, that is, the value r > 0 which determines the domain of
the speciﬁed basic system as follows:

(x, y) ∈ Ir = {|xj| < r, |yj| < r, j = 1, . . . , n} ⊂ R2n;

(λ, ǫ) ∈ Br = {∥λ
j − cj ∥ < r, ∥ǫ∥ < r} ⊂ Rk+µ1+···+µn ,
(13)

where λ is the tuple of all parameters of all normal forms from Table 1, λ =
(λ
1, . . . , λ
n); the characteristic size must be so small that all functions fj were
deﬁned for the corresponding values of their arguments.

Notations related to deﬁnition 8 There is only a ﬁnite number of unspeciﬁed
basic systems, each one being completely characterized by the string of discrete
data
 T = (l1, µ1, . . . , ln, µn)(14)

subject to the total restriction n ≤ k, ∑ µj ≤ k. We call the data T the combina-
torial type of the unspeciﬁed basic system.
The string
 Sa = (c1, . . . , cn, . . . , mjα, njα , . . . ) ∈ Rn+2s

r > 0, cj ∈ R1, mjα, njα ∈ N, fj ∈ Cp(Rk+1, 0).
(15)

will be referred to as the algebraic part of the speciﬁcation (for reasons to be clariﬁed
later), while the string of functions

Sf = f = (f1, . . . , fn)

is called the functional part of the speciﬁcation. The functions fj are deﬁned on
the domain Ir × Br, where r is the characteristic size introduced earlier.
Denote by B(T , Sa, f ) the number of isolated solutions to the speciﬁed basic
system (T , Sa, f ) in the domain Ir0 . One can check that B(T , Sa, f ) is deﬁned in
such a way that it bounds the cyclicity of the polycycle with such a speciﬁcation.
After all these notions (or rather the language) being introduced, we may for-
mulate the problem of estimating cyclicity of elementary polycycles occurring in
generic k-parametric families as follows.

Theorem 9. For any type T of unspeciﬁed basic system and any choice of the
algebraic part Sa one may choose the order of smoothness p0 and an open dense
subset F = FT ,Sa,r0 in the space of Cp0-smooth functions Cp0(Ir0 × Br0, Rn) such
that for every f = (f1, . . . , fn) ∈ F and a suﬃciently small characteristic size
r0 = r0(f ) the number of isolated solutions B(T , Sa, f ; r0) to the speciﬁed basic
system (T , Sa, f ) in the domain Ir0 is uniformly bounded over all parameter values
(λ, ǫ) ∈ Br0:

B(T , Sa, f ; r0) = sup
(ǫ,λ)∈Br0 #{(x, y) satisfying (12), (x, y) ∈ Ir0 } < 225k2
(16)

and, therefore, E(k) ≤ 225k2 .

14 Bifurcation of polycycles

3. The Khovanski reduction method.

In this section we describe the method of reducing a functional–Pfaﬃan system
to a chain map of the form (3). The construction in its full generality is described
in the book [Kh]. Our exposition relies on the one in [IY3], but has new important
features so we can’t just refer to neither [Kh], nor [IY3].

3.1. Pfaﬃan systems and their separating solutions. Let M be a smooth
orientable n-dimensional manifold, not necessarily compact or connected, and ω be
a smooth 1-form on it.

Deﬁnition 10. A codimension 1 smooth submanifold Γ ⊂ M is the separating
solution for the Pfaﬃan equation ω = 0, if:
a) Γ is the integral manifold, that is, the restriction of ω on the tangent bundle
of Γ is identically zero:
 ∀x ∈ Γ, ∀v ∈ TxΓ ω(v) = 0;

b) Γ does not pass through singular points of ω:

∀x ∈ Γ, ∃v ∈ TxM ω(v)|TxM ̸= 0;

c) Γ is the boundary of a domain D ⊆ M and the coorientation induced on Γ by
ω, coincides with its coorientation as the boundary. In other words, on any vector
pointing outward from D, the form is positive.

Let now ω1, . . . , ωk be an ordered k-tuple of smooth 1-forms on M . Consider the
system of Pfaﬃan equations

ω1 = 0, . . . , ωk = 0.(17)

Deﬁnition 11. A submanifold Γ is the separating solution for the system of Pfaf-
ﬁan equations, if there exists an increasing chain of smooth submanifolds,

Γ = Γk ⊂ Γk−1 ⊂ · · · ⊂ Γ1 ⊂ Γ0 = M(18)

such that for any j = 1, . . . , k submanifold Γj is the separating solution for the
Pfaﬃan equation on Γj−1, determined by the restriction of the form ωj on the
latter submanifold.

Let F : M → Rs be a smooth map s < n − k. Recall that a point a ∈ Rs is
called a regular value for the map F if the linearization matrix, denoted by JF (x),
has full rank for any x ∈ F −1(y). By the rank theorem the level set Va = F −1(a)
of a regular value is a smooth manifold of dimension n − s.
We call a ∈ Rs a regular value for F with respect to Pfaﬃan equations (17) if a
is a regular value of F and the k-form Ω = ω1 ∧ · · · ∧ ωk, restricted to Va Ω|Va is
nondegenerate, i.e., singular points of Ω|Va have measure zero.
Consider a pair of smooth maps F : M → Rs and F : M → Rn−k−s. Now
we add to a Pfaﬃan system (17) two types of functional equations. The ﬁrst type
consists of functional equations F = a, where a ∈ Rs is a ﬁxed regular value of
F with respect to a Pfaﬃan system (17). The second type consists of functional
equations F = b, where b ∈ Rn−k−s is a variable. We call equations F = a, with
a ﬁxed a ∈ Rs, by rigid equations and F = b, with a varying b ∈ Rn−s−1, by loose
equations.
 V. Kaloshin 15

Deﬁnition 12. Let Ω = (ω1, . . . , ωk) ∈ (Λ1(M ))
k be a k-tuple of smooth 1-forms,
F : M → Rs and F : M → Rn−k−s be smooth maps, and a ∈ Rs be a regular
value for F with respect to the k-tuple of smooth 1-forms. A solution to the mixed
functional–Pfaﬃan system

Ω = 0, F = b, F = a, b ∈ Rn−k−s(19)

is a pair (Γa, Lb), where Lb ⊆ M is the preimage F −1(b) and Γa is a separating
solution for the Pfaﬃan system Ω = 0, restricted to Va, and the intersection Γa ∩Lb
is nonempty.

The solution is regular , if Γa is the separating solution for the restriction of
Pfaﬃan equations to Va and b is the regular value for the restriction of the map G
on Γa. If (Γa, Lb)) is a regular solution, then the intersection Γa ∩ Lb is transversal
and consists of isolated points.

Deﬁnition 13. The Khovanski number K{Ω, F ; F = a} for the mixed system (19)
is the upper bound for the cardinalities #{Γa ∩ Lb} over all regular solutions of the
system.

Remarks 1. The Khovanski number is also deﬁned if k = 0 (resp. s = 0),
i.e., there are no Pfaﬃan (resp. rigid) equations at all. In this case one may put
formally Γ = M (resp. Va = M ), and K{ω, F ; F = a} (resp. K{Ω, F ; ∅}) is equal
to the upper bound of the cardinality of preimages #{Lb ∩ Va} (resp. #{Lb ∩ Γ})
of regular values for the map G|Va : Va → Rn−k−s.
2. If we want to stress in the notation the phase space M of the functional–
Pfaﬃan system, we use the notation KM {Ω, F, F = a}. Usually this is necessary
when F , F , and Ω are deﬁned on the Euclidean space Rn, while we are interested
only in solutions belonging to some (open) ball.
3. If we ﬁx a coordinate system in Rn−k−s, denote by F1, . . . , Fs coordinate
functions of the map F : M → Rn−k−s, and introduce the (n − k − s)-tuple of
1-forms ΩF = (dF1, . . . , dFs), then we can consider the following mixed system

Ω = 0, ΩF = 0, F = a.(20)

Regularity in the deﬁnition of the Khovanski number K{Ω, F ; F = a} implies that
K{Ω, F ; F = a} = K{(Ω, ΩF ), ∅; F = a}.
The goal is using the Khovanski reduction principle estimate the Khovanski
number for the mixed functional-Pfaﬃan system by a linear combination of the
Khovanski number for some number of entirely rigid functional systems.
The ﬁrst step of the reduction principle is to estimate the Khovanski number
for a given mixed system by a linear combination of the Khovanski numbers of two
auxiliary systems containing a reduced by one number of Pfaﬃan equations and an
increased by one number of rigid equations.
The second step is using remark 3 replace all loose functional equations for
pfaﬃan equations and apply the reduction principle to the mixed system consisting
of (n − s) Pfaﬃan equations (Ω, ΩF ) and s rigid equations. Thus, after (n − s) steps
of the reduction principle we obtain a ﬁnite collection of entirely rigid functional
systems.

16 Bifurcation of polycycles

3.2. The Reduction principle for one Pfaﬃan equation. We show how to
eliminate the Pfaﬃan equation from the mixed system with (n − s − 1) loose equa-
tions and s rigid functional equations.

ω = 0, F = b, F = a, F : M → Rn−s−1, F : M → Rs,(21)

We shall outline only the key ideas.

Deﬁnition 14. A smooth positive function ρ : M → R+ is called covering, if it
tends to zero along any nonaccumulating sequence of points in M . In other terms, ρ
vanishes “at inﬁnity” on M , so that all level hypersurfaces of the covering function
are compact subsets of M .

Remark 1. This deﬁnition applies both to compact and noncompact manifolds, but
in the compact case a smooth function is covering if and only if it is everywhere
positive, thus automatically bounded away from zero.

Suppose that the manifold M is endowed with the Riemann volume. Since it is
orientable, one may use the duality between functions and n-forms on M . Denote
by the asterisk the operator taking an n-form into the function (dividing by the
volume form).
Fix Euclidean structures in Rn−s−1 and Rs. Let F1, . . . , Fn−s−1 and F1, . . . , Fs
be the coordinate functions of the maps F and F in (21) respectively.

Deﬁnition 15. The contact function for the mixed system (21) is

Fs+1 = ∗(ω ∧ dF1 ∧ · · · ∧ dFn−s−1 ∧ dF1 ∧ · · · ∧ dFs).(22)

The operator taking the mixed system (ω, F ; F ) into the corresponding contact func-
tion, will be denoted by σ : (ω, F ; F ) ↦→ σ(ω, F ; F ) = Fs+1.

Deﬁne the two maps by their coordinate functions,

F c = (F1, . . . , Fs, Fs+1), F ∞ = (F1, . . . , Fs, ρ),(23)

both taking M to Rs+1, where Fs+1 is the contact function (22), and ρ is the
covering function.

Theorem 16. Suppose that the system (21) admits regular solutions in the sense
of Deﬁnition 19. Then for any suﬃciently small regular ǫ

K{ω, F ; F = a} ≤ 1
2 K{ω, F ; F ∞ = (a, ǫ)} + K{ω, F ; F c = (a, ǫ)},(24)

where regularity of ǫ means that (a, ǫ) is a regular value for both F ∞ and F c and
is necessary to the right-hand side systems being well deﬁned.

Before proving this theorem recall the Rolle lemma from an elementary calculus.

Lemma 1. Consider C2 Morse functions f : S1 → R1 on the circle and g : [0, 1] →
R1 on the segment, i.e., functions f and g have only nondegenerate critical points.
Then for all a ∈ R
 #{x : f (x) = a} ≤ #{x : f ′(x) = ǫ}

#{x : g(x) = a} ≤ #{x : g′(x) = ǫ} + 1
(25)

for any suﬃciently small ǫ.
 V. Kaloshin 17

Proof Prove the formula for f : S1 → R1. For a suﬃciently small ǫ the number of
local maxima and minima equals #{x : f ′(x) = ǫ}. Between any two consecutive
preimages x1 and x2 of a point a, i.e., f (x1) = f (x2) = a there exists a local
minimum or maximum. Q.E.D.
Formula (25) in the case of one equation transfers a loose equation into a rigid
one.
Proof of theorem 16 Take a regular solution (Γa, Lb) for (21), where Lb = F −1(b),
and suppose that the intersection Γa ∩ Lb consists of isolated, say d, points. Since,
b is regular value of the restriction F |Γa , any small variation of b may only increase
the number of intersections. Take b to be a regular value of the restriction F |Va
or equivalently (b, a) to be a regular value of the map (F, F ) (rather than of the
restriction of F to Γa).
Then any level set Lb is a one dimensional smooth manifold, intersecting Γ
transversally. By the classiﬁcation theorem for one-dimensional manifolds, Lb is
the union of compact (circles) and noncompact (lines) components. Fix some ori-
entation on each circle and each curve in Lb. Consider the function f ′ : Lb → R
which maps a point x ∈ La to the value of the 1-form ω on the unit positively
oriented vector tangent to Lb at point x.
Fix a connected component, denoted by γ ⊂ Lb. Between any two consecutive
intersection x and y of La with Γ values f ′(x) and f ′(y) must have diﬀerent signs.
Now we can apply the Rolle lemma with f ′ = f ′, when γ is a circle, and f ′ = g′,
when γ is a line.
Each point x where f ′(x) = 0 (resp. f ′(x) is small) is the point where the
linear functionals dF1(x), . . . , dFn−s−k(x), dF1(x), . . . , dFs(x). and ω(x) are linear
dependent (resp. almost dependent), i.e. Fs+1(x) = 0 (resp. Fs+1(x) = ǫ). This
completes the proof of the theorem. Q.E.D.

Corollary 3. If the manifold M is compact, then for any suﬃciently small regular
ǫ
 K{ω, F ; F = a} ≤ K{ω, F ; F c = (a, ǫ)},(26)

where regularity of ǫ means that (a, ǫ) is a regular value for F c.

Proof Indeed, in this case the ﬁrst term in (21) disappears.

Remark 2. The choice of the Riemann volume form is not essential for the above
construction. Indeed, if the volume form voln is replaced by a new one b·voln, where
b is a positive function, then the function Fs+1 will be replaced by ˜Fs+1 = b−1Fs+1,
and the map ˜F c = (F1, . . . , Fs, ˜Fs+1) will have the same zero set.

3.3. The Khovanski reduction in the general case. Consider now the general
case of the mixed system (19) with k > 1. Suppose that Γa is a separating solution
for the Pfaﬃan system Ω = 0 restricted to Va. By deﬁnition, this means that
there exists a separating solution Γa
k ⊂ Va to the Pfaﬃan equation ωk = 0 on a
separating solution Γa
k−1 ⊂ Va to the Pfaﬃan system Ω′ = 0 restricted to Va, where
Ω′ = (ω1, . . . , ωk−1). Note that if ρ is a covering function on the manifold M , then
its restriction on Γa
k−1 is the covering function for the latter submanifold. Next, one
can endow Va (resp. Γa
k−1) by the Riemann (n − s)-volume (resp. (n − k − s + 1)-
volume) form voln−s
Va (resp. voln−k−s+1
Γa
k−1 ) in such a way that

dF1 ∧ · · · ∧ dFs ∧ vol
n−s
Va = vol
n
M ω1 ∧ · · · ∧ ωk−1 ∧ vol
n−k+1
Γa
k−1 = vol
n−s
Va(27)

18 Bifurcation of polycycles

Since the forms ωj, j = 1, . . . , k − 1 are linear independent in a neighborhood of
Γa
k−1, these formulas deﬁne volume forms near Va and Γa
k−1 respectively. As this
was mentioned before, the choice of the Riemann volume form does not aﬀect the
assertion of Theorem 17.
Thus one can apply Theorem 17 to the mixed system

ωk = 0, F = b, F = a(28)

on the manifold Γa
n−k ⊂ Va. To describe the result, we introduce the following two
maps from M to Rn−k+1,

F c = (F1, . . . , Fs, ρ), F ∞ = (F1, . . . , Fs, F∗),(29)

where ρ is the covering function on the manifold M , and F∗ : M → R is the smooth
function obtained as

F∗ = σ(Ω, F ; F ) = ∗(dF1 ∧ . . . ∧ dFn−k−s ∧

∧dF1 ∧ . . . ∧ dFs ∧ ω1 ∧ . . . ∧ ωk).
(30)

The above choice of the Riemann volume on Γa
k−1 implies that the asterisk
operator in the ambient manifold M agrees with the asterisk operator relevant to
Γa
k−1, therefore the formula (30) deﬁnes the same function as the formula (22):
ωk ∧ dF1 ∧ · · · ∧ dFn−k−s ∧ dF1 ∧ · · · ∧ dFs = F∗ · vol
n−k+1
Γa
k−1 .

Theorem 17. Let Ω, F, F c, and F ∞ be as above. Then for any suﬃciently small
regular ǫ

K{Ω, F ; F = a} ≤ 1
2 K{Ω′, F ; F ∞ = (a, ǫ)} + K{Ω′, F ; F c = (a, ǫ)},(31)

where regularity of ǫ means that (a, ǫ) is a regular value for both F ∞ and F c.

Corollary 4. If either Va is compact or the restriction F |Va : Va → Rn−k−s is a
proper map, i.e. preimage of any point is compact, then for any suﬃciently small
regular ǫ
 K{Ω, F ; F = a} ≤ K{Ω′, F ; F c = (a, ǫ)},(32)

where regularity of ǫ means that (a, ǫ) is a regular value for F c.

Proof Straightforward application of Theorem 16.
Iterating the above two statements, one can replace one by one the Pfaﬃan
equations by the rigid functional ones, obtaining new systems whose Khovanski
numbers estimate from above that of the initial one, by virtue of the inequalities
(21) and its compact counterpart (24). On each step one has two possibilities, either
to replace a Pfaﬃan equation by the contact function, or by the covering function.
But once the covering function appears among the rigid functional equations, the
level sets F −1(·) ∩ Va becomes compact as a submanifold of a compact Va, hence on
the next steps the Corollary to Theorem 17 applies rather than the Theorem itself.
Denote by T c
ǫ and T ∞
ǫ the two operators, transforming the mixed system
{Ω, F ; F = a} into the mixed systems {Ω′, F ; F c = (a, ǫ)} and {Ω′, F, F ∞ = (a, ǫ)}

V. Kaloshin 19

respectively, where the maps F c and F ∞ are given by (29) and (30):

T c
ǫ {Ω, F ; F = a} = {Ω′, F ; (F , σ{Ω, F, F }) = (a, ǫ))},

T ∞
ǫ {Ω, F ; F = a)} = {Ω′, F ; (F , ρ) = (a, ǫ))}.
(33)

If we start with the mixed functional–Pfaﬃan system {(Ω, ΩF ), ω; F = a}, with
(Ω, ΩF ) being an (n − s)-tuple (ω1, . . . , ωk, dF1, . . . , dFn−k−s), and eliminate sub-
sequently the forms ωk, ωk−1, . . . , ω1, dF1, . . . , dFn−k−s, then the following maps
from M to Rn arise:
a) the map F[0], if on each step the contact function was used,

{ω, F[0] = (a, ǫn−s))} = (T c
ǫn−s ◦ · · · ◦ T c
ǫ1){Ω, F ; F = a},(34)

where ǫn−s = (ǫ1, . . . , ǫn−s);
b) the maps F[j], if on the jth step the covering function was used, while on all
other steps the contact ones were, j = 1, . . . , n − s,

{ω; F[j] = (a, ǫn−s))} = (T c
ǫn−s ◦ · · · ◦ T c
ǫj+1 ◦ T ∞
ǫj ◦

◦T c
ǫj−1◦ · · · ◦ T c
ǫ1){Ω, F ; F = a}.
(35)

Then inductive application of Theorem 16 immediately yields the following fun-
damental result.

Theorem 18. The Khovanski number for the mixed system (19) on a manifold
M with the covering function ρ and any suﬃciently fast decaying to zero sequence
(ǫ1, . . . , ǫn−s) admits the upper estimate by a linear combination of Khovanski num-
bers of some (n − s + 1) auxiliary systems, each of them containing only rigid
equations and no Pfaﬃan equations at all:

K{Ω, F ; F = a} ≤ K{ω; F[0] = (a, ǫn−s)} + 1
2
 k∑

j=1 K{ω; F[j] = (a, ǫn−s)},(36)

where the maps F[j] are deﬁned by the formula (33)-(35).

3.4. Applications. The Khovanski reduction process is constructive. This leads
to the result, which will be now formulated.
Assume that the manifold M is an open domain in Rn and admits a polynomial
covering function ρ. The main example is the unit ball B = {
x ∈ Rn : ∑
j x
2
j < 1}
,
for which one may take ρ(x) = 1 − ∑
j x
2
j . Then the Riemann volume form can be
chosen algebraic, dx1 ∧ · · · ∧ dxn.
Assume also that all the forms ωi, i = 1, . . . , k are polynomial (i.e. with poly-
nomial coeﬃcients), and the maps F and G are at least Cn−s-smooth. Then, since
the operators T c
ǫ and T ∞
ǫ introduced above, involve only algebraic operations and
diﬀerentiation of functions, the following holds.

Theorem 19. If the system (19) has no rigid functional equations at all (s =
0) and is deﬁned on a semialgebraic subset M ⊆ Rn, all Pfaﬃan forms and the
covering function ρ are polynomial of degrees ≤ d, then all the maps F[α] : M → Rn,
α = 0, 1, . . . , k constructed in Theorem 19 are of the form

F[α] = Pα ◦ jn−sF,(37)

20 Bifurcation of polycycles

where jn−sF is the (n − s)-jet extension of F , and Pα are certain polynomials
deﬁned on the jet space J n−s(Rn, Rn−k). For all α = 0, 1, . . . , k the degrees of the
polynomial Pα admits the upper estimate by 2α(dk + n) and each map F[α] has a
regular point for a generic map F .

Proof The reduction procedure of elimination of a Pfaﬃan equation boils down
to consecutive application (n − s) times of one of the operators T c
ǫ or T ∞
ǫ (33).
Consider the ﬁrst step.

F 1,α
∗ = σ{(Ω, ΩF ), ∅; F )} = ∗(ω1 ∧ · · · ∧ ωk ∧ dF1 ∧ · · · ∧ dFn−k) = P 1,α ◦ j1F,

where P 1,α : J 1(Rn, Rn−k) → R is a polynomial of degree at most dk + n and is
deﬁned on the space of 1-jets J 1(Rn, Rn−k).
Denote by Ω∗ = (Ω, ΩF ) the (n − s)-tuple of the 1-form, dFs by ωk+s for s =
1, . . . , n − s, and the (n − s − r)-tuple of the 1-form, which consists of all of 1-
forms of Ω∗ except of the ﬁrst r, by Ω∗
r. Consider F r,α
∗ = σ{Ω∗
r−1, ωr; F r−1,α} and
F r,α = (F r−1,α, F r,α
∗ ) for r = 1, . . . , n − s. It is easy to see that F r,α
∗ has the form
F r,α
∗ = P r,α ◦ jrF .
Using induction in r it is easy to see that for r ̸= α the degrees of correspond-
ing polynomials P r−1,α and P r,α, deﬁned above, satisfy the following inequality
deg P r,α ≤ 2 deg P r−1,α. For r = α the operator T ∞
ǫ will not exceed the degree
dk + n and F r,α = ρ. This implies that deg P r,α ≤ 2α(dk + n) and complete the
proof.
 4. Functional-Pfaffian system for limit cycles

In this section we consider a speciﬁed basic system (T , Sa, f ; r) obtained from
the unspeciﬁed basic system (8), that is we consider a system (8) together with a
collection of formal invariants (c1, . . . , cn) of all singularities (which determines a
point in the λ-space), a collection of hyperbolicity ratios njα : mjα of all resonant
saddles and a tuple of suﬃciently smooth functions fj, on a suﬃciently small open
cube Ir × Br in the (ǫ, λ)-space.
Our local goal is to reduce this system to a functional–Pfaﬃan system having
the form described in section 3, with the following properties:
• the new system has the form allowing for application of Theorem 17;
• the number of regular solutions to the functional–Pfaﬃan system is greater or
equal to the number of isolated solutions to (8), up to k, where k is the number of
parameters of the original family.
After application of Theorem 17 we will obtain a number of chain maps with
controlled degrees of the exterior polynomial parts.

4.1. Upper estimate of the number of solutions for the basic system:
statement of results. First of all we make the following remark. The algebraic
part of the specialization can be identiﬁed with a point

Sa = (c1, . . . , cn, nj1 , mj1 , . . . , njs, mjs) ∈ Rn+2s,(38)

where s ≤ n is the number of resonant saddles on the polycycle: the fact that the
numbers njα , mjα are in fact natural will become inessential for our constructions.

Theorem 20. (reduction from basic to functional–Pfaﬃan system) Consider an
unspeciﬁed basic system 8 of a certain type T in codimension k, together with an

V. Kaloshin 21

arbitrary speciﬁcation

S = (Sa, f ; r), Sa ∈ Rn+2s, f ∈ Cp(Ir × Br, Rn), r > 0.

Then one can explicitly construct a functional–Pfaﬃan system of the form {Ω, F },
Ω = (Ω1, . . . , Ωn+2s), F = (F1, . . . , Fn+k+m), m = ∑ µj, or in a more traditional
notation, the mixed system of loose functional and Pfaﬃan equations (no rigid
equations)
 Ω = 0, F = a;(39)

deﬁned in a certain open bounded semialgebraic subset

M = M (r) ⊂ Ir × Br × R2s

(see Deﬁnition 8), such that the following holds:
• For any choice of the parameters (ǫ, λ) ∈ Br the number of isolated (x, y)-
solutions, denoted by B(T , Sa, f ; r) of the speciﬁed basic system (T , Sa, f ; r) admits
the estimate by the Khovanski system (39) on the manifold M = M (r):

B(T , Sa, f ; r) ≤ KM(r){Ω, F ; ω} + k;

• The forms Ωk have coeﬃcients which are polynomial in all their arguments, and
also in coordinates of the point Sa ∈ Rn+2s; the degrees of those polynomials do not
exceed 6µ + 1, where µ is the order of degeneracy of the corresponding equilibrium
point;
• The covering function ρ(· ; r) for the phase space M (r) is polynomial in all its
arguments and also in r, of the total degree not exceeding 14k;
• The coordinate functions of the maps Fβ are explicitly given as polynomials of
the ﬁrst degree on the 0-jet space of functions J 0(Ir × Br, Rn) with coeﬃcients ±1.

The proof of this theorem is completely constructive and given in [IY3]. We only
point out degree estimates which are not given in [IY3].

22 Bifurcation of polycycles

Table 2. Separating solutions for Pfaﬃan systems associated with unfolding of
elementary equilibrium points.

Type Submanifold γ Domain Mr, Covering function ρ Pfaﬃan system Ω = 0
0 < x, y < r,
S0 y = ∆(x, λ) λ ∈ Lr, x dy − λy dx = 0
ρ = xy(r − x)(r − y)˜ρ
0 < x, y, z, w < r, x dz − m z dx = 0, (1)
y = ∆(x, λ) λ ∈ Lr, y dw − n w dy = 0, (2)
Sµ z = xm Pµ(z, λ) ̸= 0, m Pµ(w, λ) ×
w = yn ρ = xyzw(r − x)(r − y)× y Pµ(z, λ) dx −
(r − z)(r − w)P 2
µ (z, λ)˜ρ (mPµ(w, λ) + n) ×
x P 2
µ (z, λ) dy = 0 (3)
|x|, |y| < r, x ̸= 0,
Dc
µ y = ∆(x, λ) λ ∈ Lr, x (x dy − y dx) = 0
ρ = (r2 − x2)(r2 − y2)x2 ˜ρ
0 < y < r, |x| < r,
λ ∈ Lr
Dh
mu y = ∆(x, λ) Qµ(·, λ)|[x,1] > 0, Qµ(x, λ) dy − y dx = 0
ρ = y(r − y)(r2 − x2)×
Qµ(x, λ)˜ρ

Notes to the Table Here we use the same notation as in Table 1 (and in fact
this Table continues Table 1). In particular, n : m is the hyperbolicity ratio in the
resonant saddle case Sµ.
In the third column of the Table the symbol Lr stands for a small r-cube in the
(µ + 1)-dimensional space of the parameters λ, centered at the localization point
c = (0, . . . , 0, c) ∈ Rµ+1, corresponding to the unperturbed system:

Lr = {λ ∈ Rµ+1 : |λi| < r, i = 0, . . . , µ − 1, |λµ − c| < r}

Everywhere in the Table the function ˜ρ = ˜ρ(λ) is the covering function for the set
Lr, deﬁned as
 ˜ρ(λ) = (r2 − λ
2
1) · · · (r2 − λ
2
µ−1) · (r2 − (c − λµ)
2).

This is a polynomial of degree 2µ in all variables λ, r, c. Recall that deg Pmu =
2µ and deg Qµ = 2µ + 1 (see Table 1). Each covering function ρ is therefore a
polynomial (explicitly written in the Table). Thus, we obtain the following degree
estimates:
Type S0: deg Ω = 1 and deg ρ = 4µ + 4.
Type Sµ, µ > 0: deg Ω ≤ 6µ + 1 and deg ρ = 6µ + 8.
Type Dc
µ: deg Ω = 2 and deg ρ = 2µ + 6.
Type Dh
µ: deg Ω = 2µ + 1 and deg ρ = 4µ + 5.
Along with the estimate ∑ µj ≤ k (the sum of codimension) this gives the
estimates deg Ω ≤ 6µ + 1 and deg ρ ≤ 14k.

4.2. Principal functional–Pfaﬃan system. We proceed with writing down the
principal functional–Pfaﬃan system explicitly. Slightly abusing notation, we add
the subscript j for objects related to the jth singularity, while letters without this
subscript refer to objects related to the entire polycycle. In this notation we omit
the reference to the characteristic size, still keeping in mind that all formulas are
explicitly polynomial in r.
 V. Kaloshin 23

Notations Denote by Mj the domain from Table 2, associated with the j-th
singular standard map, let γj be the corresponding manifold (separating solution)
and by Ωj the tuple of Pfaﬃan forms on it: if the singularity is of the type Dµ or
S0, then Ωj consists of only one form ωj = Aj dxj + Bj dyj, while in the case Sµ,
µ > 0, there are three forms, of which we denote the third one by Aj dxj + Bj dyj,
(see Table 2). The covering function for Mj is denoted by ρj : Mj → R1
+.
Construction of the principal system The phase space for the principal functional–
Pfaﬃan system is the Cartesian product of phase spaces corresponding to all the
vertices of the polycycle and the r-cube in the ǫ-space:

M = M (r) = M1× · · · × Mn × ˜Br,

Mj = Mj,r are taken from the second column of Table 2,
˜Br = {|ǫi| < r, i = 1, . . . , k}.

(40)

Dimension of the phase space is equal to 2n + 2s + k + m, where:
• k is the number of the parameters ǫ (the principal integer index);
• n ≤ k is the number of vertices;
• s ≤ n is the number of resonant saddles on the polycycle (each such a vertex
contributes two additional variables zj, wj into the list of independent variables);
• m = n + ∑ µj ≤ n + k ≤ 2k is the number of additional free parameters
λ = (λ
1, . . . , λ
n), λ
j ∈ Rµj +1.
The covering function for such a space is the product

ρ = ρ1 · · · ρn · ρǫ : M → R1
+,(41)

where the last factor is the covering function for ˜Br. From Table 2 it is clear that
ρ is a polynomial of degree at most ∑
j(6µj + 8) ≤ 14k in both phase variables and
the characteristic size r.
Each form on Mj can be pulled back on M , yielding the form which is indepen-
dent of all the coordinates except for those related to the jth vertex. Denote by Ω
the union of the tuples Ω(j): thus Ω is itself the tuple of 1-forms on M , containing
n + 2s of them:

Ω = (Ω(1), . . . , Ω(n)) = (Ω1, . . . , Ωn+2s),

Ω(j) =
 {{ωj} if j is not a resonant saddle,
{ωj1, ωj2, ωj} otherwise,

where ωj1 = mjxj dzj − zj dxj , ωj2 = njyj dwj − wj dyj,

ωj = Aj dxj +Bj dyj.

(42)

Each γj is a separating solution to the Pfaﬃan equation or system of equations
Ω(j) = 0 on Mj, therefore the Cartesian product

Γ = γ1 × · · · × γn × ˜Br

is the separating solution to the Pfaﬃan system Ω = 0 on M . Indeed, one may
consider the chain of submanifolds

Γi = γ1 × · · · × γi × Mi+1 × · · · × Mn × ˜Br

This chain possesses all the properties required by the deﬁnition of a separating
solution, see section 3: there are no singular points of Pfaﬃan forms on all the
manifolds from this chain, and the topological condition of Γi+1 being the boundary
of a domain in Γi is trivially satisﬁed, because each γi+1 is the boundary of the

24 Bifurcation of polycycles

corresponding subdomain in Mj. Thus the Pfaﬃan part of the principal system is
constructed.
In this Pfaﬃan part we have the following information about the polynomials
(recall that Sa stands for the algebraic part of the speciﬁcation for the basic system,
which is identiﬁed by (38) with a tuple of real variables):

Aj, Bj ∈ Z[x, y, λ, Sa], deg Aj, deg Bj ≤ 6µ + 1,

ρ ∈ Z[x, y, λ, ǫ, r], deg ρ ≤ 14k.
(43)

Now we proceed with description of the functional part of the principal system.
It is given by the map
 F = (F1, . . . , Fn+k+m) : M → Rn+k+m,

Fj =
 



xj+1 − fj(yj, ǫ), j = 1, . . . , n mod (n),
ǫj−n, j = n + 1, . . . , n + k,
λj−n−k, j = n + k + 1, . . . , n + k + m.

(44)

The dimension of a generic ﬁber F −1(·) is equal to the codimension of separating
solutions of the Pfaﬃan system. An essential feature of the above map is the
following one: the coordinate functions of the map F are polynomial combinations
of the coordinates on the source space and generic functions fj:

Fj ∈ Z[x, ǫ, λ, f ], deg Fj = 1,(45)

and all coeﬃcients of those polynomials are ±1. A more invariant way of formulat-
ing the same property is to say that F is a polynomial map deﬁned on the space
of 0-jets of vector-functions
 f : M → Rn,(46)

and this phrase makes sense since M is a subset of a Euclidean space.

Deﬁnition 21. The functional–Pfaﬃan system with the Pfaﬃan equations (42),
the functional equations (44), deﬁned on the domain (40) considered with the cov-
ering function (41), will be called the principal functional–Pfaﬃan system. The
information provided by the estimates (43), (45) allows us to say that the principal
system is eﬀectively described.

Later on we will refer to the principal system as simply the system (39).

4.3. Reduction to singularity theory. The system (39), whose Khovanski num-
ber majorizes the number of solutions to the basic system (12), satisﬁes the con-
ditions of Theorem 18. The conclusion of the latter claims that the number
K{Ω, F ; ω} is in turn majorized by the combination of Khovanski numbers for
some 2n + 2s + k + m + 1 entirely rigid systems (recall that n + 2s is the number
of Pfaﬃan equations and n + k + m is the number of loose functional equations in
the principal system, which should be eliminated). The properties of the principal
system, listed in the formulation of Theorem 20, yield a complete description of the
resulting systems as chain maps (the deﬁnition is given below).
In what follows we treat the original variables xj , yj, the auxiliary variables
zjα, wjα and the parameters ǫ, λ in almost the similar way, as it is suggested by the
functional equations (44) of the principal system (39). The algebraic part Sa of
the speciﬁcation, however, plays a diﬀerent role: the coordinates of the localization

V. Kaloshin 25

points cj and the integers njα, mjα determining the hyperbolicity ratios of resonant
saddles, would determine the point in the new phase space, around which the
resulting chain maps will be considered. Recall that in §1 we introduced the vectors
cj and c as
 cj = (0, . . . , 0, cj) ∈ Rµj +1, cj ∈ R1,

c = (c1, . . . , cn) ∈ Rm, m = n + ∑ µj.

For our purposes it would be convenient to consider all (new) variables as taking
values around the origin in the corresponding phase space. For this sake we make
a parallel translation in the λ-space, which would take the origin into the point
c. Clearly, this translation does not aﬀect the algebraic structure of the principal
system (39), though changes the appearance of the equations.
The characteristic size r retains its original meaning.
Notations According to what has been said, we introduce the following nota-
tions:
 x = (x, y, z, w, ǫ, λ − c) ∈ R2n+2s+k+m,

f = (f1, . . . , fn), fj = fj(yj, ǫ) ⇐⇒ f = f (x),

where f is now considered as a vector-function of the argument x, though each
coordinate function fj of the vector f depends in fact only on some of the coordi-
nates of the vector x. By Dpf we denote the collection of all partial derivatives of
functions fj of the order p.
We will also use the same notation M (r) for the domain of the principal system,
though in fact it would become a subset of the unit cube ∥x∥ < r centered at the
origin in the x-space.
Now we can formulate the properties of the systems of equations which appear
after elimination of Pfaﬃan equations from the principal system (39) as this was
described in §3.4. Let m = 2n + 2s + k + m

Theorem 22. Let m = 2n + 2s + k + m. For any ﬁxed combinatorial type T
of the principal functional-Pfaﬃan system (39), any choice of the algebraic part
Sa of the speciﬁcation and suﬃciently fast decaying to zero sequence of numbers
ǫ1, . . . , ǫm, the number of nondegenerate solutions to the principal system in the
domain M (r) for any choice of the characteristic size r > 0 does not exceed the
sum of the Khovanski numbers for m + 1 entirely rigid system of equations in the
same domain. Each of these systems has the form

P
(x, f (x), D1f (x), . . . , Dmf (x); Sa, r) = (ǫ1, . . . , ǫm), x ∈ M (r) ⊆ Rm,(47)

where
• m ≤ 7k is the total number of variables ( the dimension of the phase space);
• P is a vector polynomial, P = (P1, . . . , Pm), Pi ∈ Z[x, . . . ; Sa, r]; the degrees
of each polynomial Pi is bounded by 14k2i i = 1, . . . , m;
• the domain M (r) belongs to the r-cube of the space Rm, centered at the origin.

4.4. Chain maps and related ﬁniteness theorems. Now we proceed with a
more invariant description of the geometric object corresponding to the system of
equations (47).

26 Bifurcation of polycycles

Deﬁnition 23. Let Rm be a Euclidean space with a ﬁxed coordinate system x =
(X1, . . . , Xm), and U ⊆ Rm a domain of the rectangular form,

U = {αi < Xi < βi, i = 1, . . . , m}.

Denote by I the index subset I = {1, . . . , m} enumerating the coordinates in Rm,
and let for any j = 1, . . . , n Ij be a nonempty subset of I,

∅ ̸= Ij ⊆ I, j = 1, . . . , n.

We say that a vector-valued function

f : U ↦→ Rn, f = (f1, . . . , fn),

is a Cartesian function of the Cartesian type I = (I1, . . . , In), if for any j the jth
component of this function depends only on the coordinates Xi with i ∈ Ij : in other
words,
 ∀i /∈ Ij ∂fj
∂Xi ≡ 0.

For any given Cartesian type I with n = 1 the set of all Cp-smooth Cartesian
functions (i˙e ˙Cartesian maps with n = 1) of this type constitutes a Banach space
with the natural Cp-norm. We denote this space by Cp
I, sometimes omitting the
explicit reference to the type I when the latter is clear from context. The space Cp
I
will be referred to as the Cartesian space. In the same way the Cartesian spaces
of maps arise. As a consequence, we may say about genericity of Cartesian maps
(functions) within the given Cartesian type; the notions of openness and density of
subsets are also naturally deﬁned.

Deﬁnition 24. Let f be a Cp-smooth Cartesian map of a given Cartesian type I,
and s ≥ 0 an nonnegative integer number, s ≤ p. A Cartesian s-jet of the function
f at a point x0 ∈ U is the equivalence class of all Cartesian functions of the same
Cartesian type, which diﬀer from f by a term which is s-ﬂat at x0:

j
sf (x0) = {g ∈ Cp
I : |f − g| = o(|x − x0|s)}.

The space of all s-jets of functions of the given Cartesian type I at all points
x0 ∈ U will be denoted by J
s
I (Rm, Rn) or simply by J
s, when the environment is
unambiguously deﬁned by the context.
The map x ↦→ j
sf (x)

is called the Cartesian s-jet extension of the Cartesian map f .

The space of Cartesian jets of any type and any ﬁnite order admits a natural
coordinate system, in which the Cartesian jet extension of a map f = (f1, . . . , fn)
takes the form
 x = (X1, . . . , XM ) ↦→ (
X, F (X), { ∂Fj
∂Xi , i ∈ Ij
} , . . . ,

{ all partial derivatives of functions fj of all orders up to

s in the variables on which each fj actually depends
})

The Cartesian jet spaces possess almost all properties of the standard jet spaces.
In particular, the natural projections

RM ⊇ U pr0
←−−−− J
0 ≃ RM × RK pr1
←−−−− · · · prs
←−−−− J
s prs+1
←−−−− · · ·(48)
 V. Kaloshin 27

are well deﬁned and endow each J
s
I with the structure of an aﬃne bundle over
Rm. Thus it makes sense to say about polynomial functions deﬁned on Cartesian
bundles.

Deﬁnition 25. A chain map with the exterior part P and the interior part f is a
map of the form Rm ⊇ U ∋ x ↦→ P(j
s
I f (x)) ∈ Rm,

where:
• f is a Cartesian map from a certain Cartesian space Cp
I(Rm, Rn), and j
s
I is
the corresponding s-jet extension of f ;
• P : J
s
I (Rm, Rn) → Rm is a vector polynomial (eventually depending polynomi-
ally on some additional parameters),
• the composite map is between the spaces of the same dimension:dim x =
dim P = m.

Having introduced the notions of Cartesian functions, maps, jets etc, we can
describe the system (3.10) as a chain map deﬁned on a small cube of some size
r > 0 with the exterior part P which is a polynomial with integer coeﬃcients
and of a controlled complexity; this polynomial depends on r and some additional
variables A as well, and the interior part f belongs to some Cartesian space, since
the functions fj depend only on some components of the vector x = (x, y, z, w, ǫ, λ−
c) (recall that all nonzero coordinates of the vector c are already included among
the variables Sa). Thus our problem of estimating cyclicity of a polycycle takes the
following form: describe the Cartesian maps f for which the chain map admits an
upper estimate for the number of preimages of regular values.
Consider chain maps of the form

x ↦→ Gr(x) = P(j
s
I f (x), r) = (P1, . . . , Pm)(j
s
I f (x), r), x ∈ U ⊂ Rm, r > 0,

depending polynomially on an additional variable r, so that

P : J
s
I (Rm, Rn) × R1 → Rm, f ∈ Cp
I(U, Rn).(49)

We assume that the polynomial P and the Cartesian type I are ﬁxed (and U
denotes as before a unit cube) and P is nontrivial polynomial, i.e. at some point
x ∈ U the linearization matrix dP (x) has full rank.
Suppose that the smoothness order p is suﬃciently high,

p > m + 1.

Theorem 26. For any polynomial P = (P1, . . . , Pm) as in (49) one may choose a
subset FP ⊂ Cp
I (U, Rn) in the space of Cartesian functions of the given type, which
is open and dense in this space such that for any Cartesian function f ∈ FP and
any suﬃciently quickly decaying sequence a1, . . . , am there exists a characteristic
size r0 > 0 such that the number of preimages of (a1, . . . , am) admits the following
upper estimate:

lim sup
r→0+ #{x x ∈ Ur, Gr(x) = (a1, . . . , am)} ≤
 m∏

i=1 deg Pi ≤ 225k2 .(50)

A bit of terminology: “Replace an n-th jet jnF by its linear part at a point
a ∈ Rn” means “replace the map jnF : Rn → J n(Rn, Rn) by its linear part LF,a,n
at the point a”.

28 Bifurcation of polycycles

By the phrase “a map G : M → N of manifolds satisﬁes a transversality condi-
tion” we mean that for some manifold (resp. a collection of manifolds) in the image
N the map G is transversal to this manifold (resp. these manifolds).
The second stage consists in constructing a stratiﬁcation of the n-jet space
J n(Rn, Rn) (a decomposition into a disjoint union of manifolds described below)
such that if the n-jet jnF is transversal to all manifolds of this stratiﬁcation, then
the following theorem is true:

Theorem 27. Let P = (P1, . . . , Pn) be a nontrivial polynomial deﬁned on the space
of n-jets P : J n(Rn, Rn) → Rn and let F : Rn → Rn be a Ck smooth map, k > n.
Suppose the n-jet jnF satisﬁes a transversality condition depending only on P .
Then for a suﬃciently small r one can replace in the statement of the previous
theorem the n-jet jnF at the point a by its linear part LF,a,n. Namely,

#{x ∈ Br(a) : P1 ◦ jnF (x) = a1, . . . , Pn ◦ jnF (x) = an} =

#{x ∈ Br(a) : P1 ◦ LF,a,n(x) = a1, . . . , Pn ◦ LF,a,n(x) = an},
(51)

where a1, . . . , an go to zero suﬃciently fast. By Bezout’s theorem the number of
solutions to the equation in the right-hand side of (51) can be bounded by the product∏n
i=1 deg Pi.

The classical transversality theorem [AGV] says that for a generic map F its
n-jet jnF satisﬁes any ahead given transversality condition.

4.5. Stratiﬁed manifolds. Now we recall basic deﬁnitions from the theory of
stratiﬁed sets.
Let M be a smooth manifold, which we call the ambient manifold. Consider a
singular subset V ⊂ M . Roughly speaking a stratiﬁcation of V is a decomposition
of V into a disjoint union of manifolds (strata) {Vα}α such that strata of bigger
dimension are attached to strata of smaller dimension in a “regular” way.
“Regular” will obtain a precise meaning in a moment, but the most important
property is that transversality to a smaller stratum implies transversality to an
“attached” bigger stratum. Now we are going to describe the standard language of
stratiﬁed manifolds and maps of stratiﬁed manifolds. This goes back to Whitney
and Thom [W], [Th].
Recall the Whitney Conditions (a) and (b). Condition (a) is similar to the notion
of aP -stratiﬁcation due to Thom [Th] deﬁned in the next subsection. We shall use
aP -stratiﬁcation to prove condition (10).
Consider a triple (Vβ , Vα, x), where Vβ, Vα are C1 manifolds, x is a point in Vβ
and Vβ ⊆ ¯Vα \ Vα.

Deﬁnition 28. A triple (Vβ , Vα, x) satisﬁes the Whitney (a) condition if for any
sequence of points {xk} ⊂ Vα converging to a point x ∈ Vβ the sequence of tan-
gent planes Tk = TxkVα converges in the corresponding Grassmanian manifold of
dim Vα-planes in T M and lim Tk = τ ⊃ TxVβ.

Deﬁnition 29. A triple (Vβ, Vα, x) satisﬁes the Whitney (b) condition if for any
two sequences of points {xk} ⊂ Vα, {yk} ⊂ Vα converging to a point x ∈ Vβ the
sequence of “vectors” yk−xk
|yk−xk| converges to a vector v ∈ TxM which belongs to a
limiting position of lim TxkVα = τ , i.e. v ∈ τ .
Since condition (b) is local one can think of M as Euclidean. This explains how
to interpret the vector yk−xk
|yk−xk| .
 V. Kaloshin 29

It is easy to show that condition (b) implies condition (a).

Deﬁnition 30. A locally closed subset V in the ambient manifold M is called a
stratiﬁed manifold (set, variety) in M , if it is represented as a locally ﬁnite disjoint
union of smooth submanifolds Vα of M , called strata, of diﬀerent dimensions in such
a way that the closure of each stratum consists of itself and the union of some other
strata of strictly smaller dimensions, and Condition (b) of Whitney is satisﬁed.

Any union of submanifolds satisfying condition of this deﬁnition

V = ∪αVα(52)

is called a stratiﬁcation of V , and the submanifolds Vα are called strata. A set V
is stratiﬁable if there is a “nice” partition into strata. By a stratiﬁed manifold we
mean a pair (V, V) consisting of a manifold V itself and a partition V = {Vα}.

4.6. Stratiﬁed maps and aP -stratiﬁcation. Now we deﬁne a smooth map of a
stratiﬁed manifold (V, V):

Deﬁnition 31. Let (V, V) be a stratiﬁed manifold in an ambient manifold M , V ⊆
M , then a map f : V → N is called C2-smooth if it can be extended to a C2 smooth
map of the ambient manifold M F : M → N whose restriction to V coincides with
f . A stratiﬁcation V = ∪αVα stratiﬁes a smooth map f : V → Rk if the restriction
of f to any stratum Vα has constant rank, i.e., rank df |Vα(x) is independent of
x ∈ Vα.
A map G : L → M is called transversal to a stratiﬁed set (V, V) if G is transversal
to each strata Vα ∈ V.

By the Rank Theorem, if a stratiﬁcation (V, V), V = {Vα}α∈I stratiﬁes a smooth
map P , then for each strata Vα the number dα(P ) = dim Vα − rank dP |Vα is well
deﬁned.
Assume dα(P ) ≥ dβ(P ) for each Vβ ⊆ ¯Vα \ Vα, i.e. nonempty level sets inside
the bigger stratum Vα have dimension dα(P ) greater or equal to dimension of the
level sets dβ(P ) in the smaller stratum Vβ. We require that for any sequence of
points {ak} ⊂ P (Vα) converging to a point a ∈ P (Vβ), the nonempty level sets
{P −1(ak) ∩ Vα} approach the limiting level set {P −1(a) ∩ Vβ } “regularly”. In other
words, we require that the level sets in the bigger stratum Vα approach the limit
level set in the smaller stratum Vβ nicely.

Deﬁnition 32. Let P : M → N be a C2 smooth map of manifolds, and let Vβ and
Vα be submanifolds of M such that the restrictions P |Vβ to Vβ and P |Vα to Vα have
constant ranks RVβ (P ) and RVα (P ), respectively. Let x be a point in Vβ .
We call the manifold Vα aP -regular over Vβ with respect to the map P at the
point x if for any sequence of points {xn} ⊂ Vα converging to x ∈ Vβ the sequence of
tangent planes to the level sets Tk = ker dP |Vα(xk) converges in the corresponding
Grassmanian manifold of (dim Vα − RVα (P ))-dimensional planes to a plane τ and

lim ker dP |Vα (xk) = τ ⊇ ker dP |Vβ (x)(53)

Deﬁnition 33. A C2 smooth map P : V → N of a stratiﬁable manifold V to a
manifold N is called aP -stratiﬁable if there exist a stratiﬁcation (V, V) such that the
following conditions hold:
a) (V, V) stratiﬁes the map P (see deﬁnition 31);

30 Bifurcation of polycycles

b) for all pairs Vβ and Vα from V such that Vβ ⊆ ¯Vα \ Vα the stratum Vα is
aP -regular over the stratum Vβ with respect to P at point x for all x ∈ Vβ.

The original deﬁnition of aP -stratiﬁcation requires an appropriate stratiﬁcation
of the image also [Ma], but we do not require stratiﬁcation of the image for our
purposes.

4.7. Relation between existence of aP -stratiﬁcation and condition (5). In
section 1.5.1 we showed that the key to the proof of Theorem 26 is condition (10)
(see Proposition 1). Now we are going to reduce the question whether condition
(10) is satisﬁed to the question whether an aP -stratiﬁcation of the polynomial P
exists.
Let P = (P1, P2) : RN → R2 be a nontrivial polynomial, V = P −1
2 (0) and
V0 = (P1, P2)
−1(0) be level sets. Assume that there exists a stratiﬁcation (V, V)
that stratiﬁes the map P |V such that the zero level set V0 can be represented as a
union of strata from V, i.e., V0 = ∪α∈I0 Vα. Denote this stratiﬁcation of V0 by V0.
Recall that a map F : Rk → RN is transversal to a stratiﬁcation (V0, V0) if it is
transversal to each strata Vα ∈ V0. Associate to each level set Va, a ̸= 0 a natural
decomposition Va = {Va ∩ Vα}α∈I .

Proposition 2. With the above notation if a stratum Vα ∈ V \ V0 is aP -regular
over a stratum Vβ ∈ V0 with respect to the polynomial P , then any C2 smooth map
F : Rn → R2 transversal to (V0, V0) is also transversal to Va ∩ Vα for any small a.
This is equivalent to condition (10).

Proof Pick a point x in Vβ ⊂ V0 and a point y ∈ Vα. Notice that ker dP |Vβ (x) is
the tangent plane to the level set {P −1(P (x))∩Vβ } at the point x and ker dP |Vα(y)
is the tangent plane to the level set {P −1(P (y)) ∩ Vα}.
By condition (53) if a map F : X → RN is transversal to ker dP |Vβ (x) at a
point x, then F is transversal to ker dP |Vα (y) for any y ∈ Vα near x.
Therefore, the condition “F is transversal to Vβ at a point x” implies the condi-
tion “F is transversal to Vα ∩ Va for any small a”. This completes the proof.

4.8. Existence of aP -stratiﬁcation for polynomial maps. The existence of
aP -stratiﬁcations is not a trivial question. There are some obvious obstacles. For
example, let V ⊂ Rn be an algebraic variety and let P : Rn → Rk be a polynomial
map. Assume that (V, V) stratiﬁes P . If we have two strata Vα and Vβ so that
Vα lies “over” Vβ ⊆ ¯Vα \ Vα, then condition (53) can’t be satisﬁed if dimension
of the level sets dα(P ) in the upper stratum Vα is strictly less than that of dβ(P )
in the lower stratum Vβ, i.e., dim ker dP |Vα(y) < dim ker dP |Vβ . In this case a
plane ker dP |Vβ (x) of the lower stratum Vβ should belong to a plane τ of smaller
dimension (see condition (53)), which is impossible. Thom constructed the ﬁrst
example when this happens [GWPL].
Thom’s example
Consider the vector-polynomial P in the form P : (x, y) → (x, xy). The line
{x = 0} is the line of critical points of P . Outside of the line {x = 0} P is a dif-
feomorphism. Therefore, the preimage of any point a ̸= 0 P −1(a) is 0-dimensional.
On the other hand, the preimage of 0 is the line {x = 0}.

Deﬁnition 34. Let us call an algebraic set V rank compatible with a polynomial P
if there exists a stratiﬁcation (V, V) which stratiﬁes P and for any pair Vα and Vβ

V. Kaloshin 31

from V such that Vβ ⊆ ¯Vα \ Vα dimensions of the levels dβ(P ) in the lower stratum
Vβ do not exceed dimensions of the level sets dα(P ) in the upper stratum Vα.

It turns out that even if an algebraic set V is rank compatible with a polynomial
P , then aP -stratiﬁcation still does not always exist. Let us present an example
with this property. The example below belongs to M.Grinberg. It seems that the
existence of a counterexample was known before, but we did not ﬁnd an appropriate
reference.

4.9. Nonexistence of aP -stratiﬁcation. Let V = {(x, y, z, t) ∈ R4 : x
2 =
t2y + z} be the three dimensional algebraic variety and P : V → R2 be the natural
projection to the last two coordinates, i.e. P : (x, y, z, t) → (z, t).

Proposition 3. With the above notations the set V is rank compatible with the
polynomial map P and does not have aP -stratiﬁcation.

Proof Consider a rank stratiﬁcation of V . Such a stratiﬁcation consists of three
stratum: V1 = {x = t = z = 0}, V2 = {t = 0, x
2 = z, x ̸= 0}, and V3 = {t ̸= 0}.
On each stratum rankP |Vi = i − 1. Level sets P −1(t, z)—parabolas for t ̸= 0 and
lines for t = 0.
Show that for each point a = (0, a, 0, 0) ∈ V1 there exists a family of level sets
such that at the point a the property aP -regularity of V3 over V1 fails.
Consider the preimage of the curve {z = −at2} ⊂ R2. This is an algebraic
variety of the form Wa = {x
2 = t2(y − a)}. One can see that Wa is the Whitney
umbrella.The level x
2 = t2
0(y − a) is the parabola. As t0 → 0 this parabola tends
to semiline x = t = z = 0, y ≥ a. At the point a ∈ V1 the property aP -regularity
of V3 over V1 clearly fails. This completes the proof of the Proposition.
Let us mention a positive result on existence of aP -stratiﬁcation.

Theorem 35. [Hir1] If V ⊂ Rn is a semialgebraic variety and P : Rn → R is a
polynomial function, then there exists an aP -stratiﬁcation of (V, V) with respect to
P .
 5. Existence of aP -stratification.

In this section we prove existence of aP -stratiﬁcation in the special case we are
interested in. As the Example 3 shows, the existence of a aP -stratiﬁcation is a
nontrivial question. In general, it does not exist. Unfortunately, the existence of a
aP -stratiﬁcation in our case does not follow from the classical results, so we need
to prove it.
Let RN and Rk be Eucledian spaces with the ﬁxed coordinate systems x =
(x1, . . . , xN ) ∈ RN and a = (a1, . . . , ak) ∈ Rk with N ≥ k and a non-trivial vector-
polynomial P : RN ∈ Rk. Recall that P is a nontrivial if it has a point x ∈ RN ,
where rank dP (x) = k. In what follows we call vector-polynomial by polynomial for
brevity.

Deﬁnition 36. Let m = (1, m2, . . . , mk) ∈ Z
k
+ and δ > 0. We call the (m, δ)-cone
Km,δ the following set of points

Km,δ = {a = (a1, . . . , ak) ∈ Rk : 0 < a1 < δ,

0 < |aj+1| < |a1 . . . aj|mj+1 for j = 1, . . . , k − 1}.
(54)

32 Bifurcation of polycycles

Let m′ = (1, m′
2, . . . , m′
k) ∈ Z
k
+. Deﬁne m′ ≻ m if m′ ̸= m and m′
i ≥ mi for all
2 ≤ i ≤ k. We call the (m′, δ′)-cone Km′,δ a reﬁnement of the (m, δ)-cone Km,δ if
m′ ≻ m and δ ≥ δ′.

Deﬁne the following sets

Vm,δ,P = closure{P −1(Km,δ)}, V0,m,P = ∩δ>0Vm,δ,P(55)

Then one has

Theorem 37. For any nontrivial polynomial P there exist an integer vector m ∈
Z
n
+ and positive δ such that the following conditions hold
a) the set V0 = V0,m,P (see (55)) is semialgebraic.
b) the set Vm,δ,P consists of regular points of P , i.e. if b ∈ Vm,δ,P , then the level
set P −1(b) is a manifold of codimension n.
c) there exists a stratiﬁcation of V0 by semialgebraic strata (V0, V0) satisfying the
property: Vm,δ,P is aP -regular over any strata Vα ∈ V0 with respect to P .

In order to prove Theorem 37 we reformulate it in a convenient for us language.
Let a ∈ Rk. Denote by La = P −1(a) the level set of P . Recall that a ∈ Rk is
called a regular value if for any x ∈ La the rank of linearity of P is maximal, i.e.
rankdP (x) = k.

Deﬁnition 38. Let a, b ∈ Rk be values of P : RN ∈ Rk, BN ⊂ RN be the unit
ball centered at the origin, and

d
0
0 : BN × Rk ∈ R, d
0
0(x, a) = inf
y∈La∩BN ∥x − y∥2

d0 : Rk × Rk ∈ R, d0(a, b) = sup
x∈Lb∩BN d
0
0(x, a).
(56)

Then the C0-distance between level sets La ∩ BN and Lb ∩ BN

D0
P (a, b) = dist0
C (La ∩ BN , Lb ∩ BN ) = 1
2 (d0(a, b) + d0(b, a)) .

For any 1 ≤ m ≤ N denote by G
m,N the set of m-dimensional planes in the N -
dimensional Euclidean space. G
m,N is so-called the grassmanian manifold. Below
we introduce convenient for as distance in the grassmanian manifold G
m,N . Now
we deﬁne C1-distance between regular level sets La and Lb in an appropriate for us
way. Write P using coordinate functions P = (P1, . . . , Pk) : RN → Rk. If x ∈ RN

is a regular point of P , then gradients ∇P1(x), . . . , ∇Pk(x) are linearly independent
and span the space which is the orthogonal complement to the tangent space to the
level set P −1(P (x)). Deﬁne a Gramm-Schmidt orthogonalization operator:

Deﬁnition 39. Let v1, . . . , vk ∈ Rk be linear independent vectors. Deﬁne the
Gramm-Schmidt linear operator by

∗ : (v1, . . . , vk) = (v∗
1 , . . . , v∗
k), where

v∗
1 = v1, v∗
2 = v2 − (v2, v1)
(v1, v1) v1, . . . , v∗
k = vk − ∑

j<k
 (vk, vj)
(vj, vj) vj.
(57)

Remarks 0. The Gramm-Schmidt linear operator ∗ has nothing in common
with the asterisk operator used for the Khovanski reduction procedure in section 3.
1. Vectors {v1, . . . , vk} and {v∗
1, . . . , v∗
k} span the same k-dimensional space de-
noted by L;
 V. Kaloshin 33

2. Vectors {v∗
1, . . . , v∗
k} form an orthonormal basis in the plane L;
3. Let {Lt}t∈(0,1] be a family of k-dimensional planes in RN spanned by a
family of vectors {v1(t), . . . , vk(t)}t∈(0,1] depending continuously on t. Consider
{v∗
1(t), . . . , v∗
k(t)}t∈(0,1] = ∗(v1(t), . . . , vk(t)) as the family of orthonormal basis in
{Lt}t∈(0,1]. Then suﬃcient condition that Lt → L in the grassmanian manifold
G
k,N is existence of an orthonormal basis {v∗
1, . . . , v∗
k} of L such that
(
v∗
j (t), v∗
j )2

(v∗
j (t), v∗
j (t))(v∗
j , v∗
j ) → 0 as t → 0.(58)

Deﬁne the Gramm-Schmidt operator for the polynomial map P

(∗(dP )1(x), . . . , ∗(dP )k(x)) = ∗(∇P1(x), . . . , ∇Pk(x)).(59)

Each vector ∗(dP )j(x) is given by the rational function in x.
Let Σ ⊂ RN be the set of critical points of P . To measure C1-distance between
two regular level sets we introduce the following function: Let x, y /∈ Σ. Then

RP (x, y) =
 k∑

j=1
 (

1 − (∗(dP )j(x), ∗(dP )j (y))2

(∗(dP )j (x), ∗(dP )j (x))(∗(dP )j (y), ∗(dP )j (y))
 )

QP (x, y) = ∥x − y∥2 + RP (x, y).

(60)

Deﬁnition 40. Let a, b ∈ Rk be regular values of P : RN → Rk, and La = P −1(a)
and Lb = P −1(b) be regular level sets.

d
0
1,P : BN × Rk \ Σ → R, d
0
1,P (x, a) = inf
y∈La∩BN QP (x, y),

d1,P : (
Rk \ Σ) × (
Rk \ Σ) → R, d1,P (a, b) = sup
x∈Lb∩BN d
0
1,P (x, a).

Then the C1-pseudodistance between regular level sets La ∩ BN and Lb ∩ BN is
deﬁned by

D1
P (a, b) = distC 1 (
La ∩ BN , Lb ∩ BN ) = 1
2 (d1,P (a, b) + d1,P (b, a)) .(61)

Remark 3. We call the function D1
P (a, b) C1-pseudodistance, not C1-distance, be-
cause it does not satisfy the triangle inequality. However, it satisﬁes the following
triangle-like inequality

2(D1
P (a, b) + D1
P (b, c)) > D1
P (a, b).(62)

The reason we deﬁne C1-pseudodistance D1
P (a, b) in such a way is because the
function D1
P (a, b) is algebraic (see Lemma 3 below).
The inequality (62) can be proven as follows. Let v, w ∈ RN be vectors. Denote
by ∠(v, w) the angle between v and w. Direct calculation shows that

RP (x, y) =
 k∑

j=1 sin
2(∠(∗(dP )j(x), ∗(dP )j (y))).

It is easy to check that 2(sin
2 α + sin
2 β) ≥ sin
2(α + β) which is suﬃcient for the
proof of the inequality (62) .

Now we can reformulate Theorem 37 in the following way

34 Bifurcation of polycycles

Theorem 41. For any nontrivial polynomial P there exist an integer vector m =
(1, m2, . . . , mk) ∈ Z
n
+ and positive δ such that the following conditions hold
a) for any two values with the same ﬁrst coordinate a = (t, a2, . . . , ak) and b =
(t, b2, . . . , bk) in Km,δ D0
P (a, b) < t;
b) the same as in Theorem 37;
c) for any two values with the same ﬁrst coordinate a = (t, a2, . . . , ak) and b =
(t, b2, . . . , bk) in Km,δ D1
P (a, b) < t;

Let us show that parts a) and c) imply parts a) and c) of Theorem 37 respectively.
Proof a) =⇒ from a) of Theorem 37. Consider an algebraic curve of the form
γ(t) = (t, tm2+1, t(m2+2)(m3+1), . . . , t(m2+2)...(mk+1)). One can check that γ(t) ∈
Km,δ for any t ∈ (0, δ). Denote by Vt,P = P −1(γ(t)). The set ∪0<t≤δVt,P is clearly
semialgebraic set. By the Tarski-Seidenberg theorem the following set

closure{∪0<t≤δVt,P } \ {∪0<t≤δVt,P }

is semialgebraic. Since for any smooth curve γ′(t) = (t, γ2(t), . . . , γk(t)) ∈ Km,δ, t ∈
(0, δ) Hausdorﬀ distance between the level sets Vt,P = P −1(γ(t)) and V ′
t,P =
P −1(γ′(t)) is at most t, i.e. D0
P (γ(t), γ′(t)) < t. It implies that Hausdorﬀ dis-
tance between any two level sets of the form Vt,P and V ′
t,P tends to 0 as t → 0.
Therefore,

closure{∪0<t≤δVt,P } \ {∪0<t≤δVt,P } = closure{P −1(Km,δ)} \ {P −1(Km,δ)}.

This completes the proof of part a).
Proof c) =⇒ from c) of Theorem 37. Let us use notations of the proof of part
a). By theorem 35 there is a stratiﬁcation of V0,m,P such that the semialgebraic set
{∪0<t≤δVt,P } is a aP -regular over V0,m,P . Indeed, let π1 : Rk → R be the natural
projection onto the ﬁrst coordinate. Then a polynomial function p = π1 ◦ P : RN →
R is well-deﬁned and p−1(t) = P −1(γ(t)). Application of theorem 35 to the map

p : closure{∪0<t≤δVt,P } → R

gives existence of a required stratiﬁcation.
Since C1-distance between any two level sets of the form Vt,P = P −1(γ(t)) and
V ′
t,P = P −1(γ′(t)) is at most t, i.e. D1
P (γ(t), γ′(t)) < t. It implies that C1-distance
between any two level sets of the form Vt,P and V ′
t,P tends to 0 as t → 0. Therefore,
aP -regularity of P −1(Km,δ) over V0,m,P follows from aP -regularity of {∪0<t≤δVt,P }
over V0,m,P . This completes the proof of part c).
Before proving Theorem 41 let us formulate a basic fact from elimination theory
[Mu].

5.1. Elimination theory. Let Cm denote the m-dimensional complex space z =
(z1, . . . , zm) ∈ Cm, m ∈ Z+. A set V in Cm is called a closed algebraic set in Cm

if there is a ﬁnite set of polynomials F1, . . . Fs in z1, . . . , zm such that

V (F1, . . . , Fs) = {(z1, . . . , zm) ∈ Cm| Fj (z1, . . . , zm) = 0, 1 ≤ j ≤ s}.

One can deﬁne a topology in Cm, called the Zariski topology, whose closed sets are
closed algebraic sets in Cm. This, indeed, deﬁnes a topology, because the set of
closed algebraic sets is closed under a ﬁnite union and an arbitrary intersection.
Sometimes, closed algebraic sets are also called Zariski closed sets.

V. Kaloshin 35

Deﬁnition 42. A subset S of Cm is called constructible if it is in the Boolean
algebra generated by the closed algebraic sets; or equivalently if S is a disjoint
union T1 ∪ · · · ∪ Tk, where Ti is locally closed, i.e. Ti = T ′
i − T ′′
i , T ′
i — a closed
algebraic set and T ′′
i ⊂ T ′
i — a smaller closed algebraic.

One of the main results of Elimination theory is the following

Theorem 43. ([Mu], ch.2.2) Let V ⊂ Cµ × CN be a constructible set and π :
Cµ × CN → Cµ be the natural projection. Then π(V ) ⊂ Cµ is a constructible set.

6. Proof of Theorem 41

6.1. Existence of the (m, δ)-cone Km,δ of regular values of P (or Proof
of Part a) of Theorem 41). The set of critical values ΣP ⊂ Rk of a nontrivial
polynomial map P : RN → Rk is an algebraic set of positive codimension. It follows
from Sard’s lemma for algebraic sets [Mu]. Suppose d : Rk → R is a nonzero
polynomial whose zero level set d
−1(0) ⊇ Σ. Fix coordinate systems in RN . By
writing the linearization matrix dP : RN → Rk and considering (N −k +1) diﬀerent
k × k minors one can calculate d explicitly.

Lemma 2. For a nonzero polynomial d : Rk → R there exists an integer vector
m = (1, m2, . . . , mk) ∈ Z
k
+ and δ > 0 such that d does not vanish on the (m, δ)-cone
Km,δ.

Remark 4. If ΣP ⊆ d
−1(0) and ΣP ∩ Km,δ ̸= ∅, then there exists x ∈ Km,δ such
that d(x) = 0. This shows that part a) of Theorem 41 follows from this Lemma.

Proof Let us prove the statement by induction in dimension k.
For k = 1 the level set d
−1(0) ⊂ R is a ﬁnite collection of points and Lemma is
obvious.
Without loss of generality assume d(x1, . . . , xk) is not divisible by xk. If d
is divisible by xk, then for some β ∈ Z+ one can decompose d(x1, . . . , xk) =
x
β
k ˆd(x1, . . . , xk) so that ˆd(x1, . . . , xk−1, 0) is not identically zero. If for some m ∈ Z
k
+
and δ > 0 the (m, δ)-cone Km,δ does not intersect zero locus ˆd
−1(0), then Km,δ
does not intersect zero locus d
−1(0) = ˆd
−1(0) ∪ {xk = 0} too.
With the assumption of indivisibility by xk the following set Σk−1
P = d
−1(0) ∩
{xk = 0} ⊂ Rk−1 is of a positive codimension. By inductive hypothesis there exist
an integer vector mk−1 ∈ Z
k−1
+ and δk−1 > 0 such that the (mk−1, δk−1)-cone
K k−1
mk−1,δk−1 ⊂ Rk−1 has empty intersection with Σk−1
P .
Let α = (α1, . . . , αk) ∈ Z
k
+ and |α| = ∑
j αj. Write d(x) = ∑

α∈Zk
+ aαx
α Denote

by deg d = max{|α| : α ∈ Z
k
+, aα ̸= 0}. Put mk = deg d + 1.

Proposition 4. With the above notations there exists δ > 0 such that for m =
(mk−1, mk) ∈ Z
k
+ the (m, δ)-cone Km,δ does not intersect zero locus d
−1(0).

Proof Put d(0) = 0 otherwise the proposition is trivial. Write

d(x1, . . . , xk) =
 deg d∑

j=0 aj(x1, . . . , xk−1)x
j
k.

Without loss of genericity one can assume that a0(x1, . . . , xk−1) does not van-
ish on the (mk−1, δk−1)-cone K k−1
mk−1,δk−1 . If not, then apply Lemma 2 and re-

ﬁne K k−1
mk−1,δk−1 to a required size. By the deﬁnition of the (m, δ)-cone Km,δ

36 Bifurcation of polycycles

the condition (x1, . . . , xk) ∈ Km,δ implies that (x1, . . . , xk−1) ∈ K k−1
mk−1,δk−1 and
0 < xk < (x1 . . . xk−1)
mk . Put xk = λ(x1 . . . xk−1)
mk with λ ∈ (0, 1). It is easy to
check that
 d(x1, . . . , xk) = a0(x1, . . . , xk−1)(1 + p(x1, . . . , xk−1, λ)),(63)

where p is such a polynomial that p(0, λ) ≡ 0. Indeed, the choice of mk is
such that (x1 . . . xk−1)
mk = a0(x1, . . . , xk−1)q(x1, . . . , xk−1) for some polynomial
q(x1, . . . , xk−1). Since p(0, λ) ≡ 0 for a suﬃciently small δ, any (x1, . . . , xk−1) ∈
K k−1
mk−1,δk−1 , and any λ ∈ [0, 1] the following inequality holds |p(x1, . . . , xk−1, λ)| <
1/2. This shows that d does not vanish on the (m, δ)-cone Km,δ and completes the
proof of the Proposition.
As we pointed out above the Proposition implies Lemma 2.

6.2. Reduction to an optimization problem (or Proof of parts a) and c) of
Theorem 37). Let P = (P1, . . . , Pk) : RN → Rk be a nontrivial polynomial with
N ≥ k given by its coordinate functions and an (m, δ)−cone K(m,δ) ⊂ Im P (RN ) ⊂
Rk be a cone of regular values of P . Existence of such a cone is proven in the
previous section. Recall that Σ ⊂ RN denotes the set of critical points of P and
QP (x, y) is deﬁned in (60). The function QP (x, y) is a rational function symmetric
with respect to permutation of x and y. It is deﬁned to measure C1-distance
between level sets (see remarks after deﬁnition 39). The singular set of QP belongs
to (Σ × RN ) ∪ (RN × Σ). Recall that BN = {x : ∑N
i=1 x
2
i ≤ 1} ⊂ RN . Introduce
functions r(x) = 1 − ∑N
i=1 x
2
i .
Assume that the restriction of P to the boundary SN = ∂BN = {x : ∥x∥ = 1}
has only the regular values in the (m, δ)−cone K(m,δ). Indeed, regularity of P |SN :
SN → Rk is equivalent to regularity of the polynomial map (P, r) : RN → Rk × R
given by (P, r)(x) = (P (x), ∑N
i=1 x
2
i ). Existence of an (m, δ)−cone of regular values
of the map (P, r) follows from Lemma 2.

Lemma 3. With the notations above let aτ1, aτ2 ∈ K(m,δ) be two points with the
same ﬁrst (k−1) coordinates, i.e. aτ1 = (ak−1, τ1) and aτ2 = (ak−1, τ2). Then there
exists a polynomial R(ak−1, τ1, τ2, c) in variables ak−1 ∈ Rk−1, τ1 ∈ R, τ2 ∈ R, and
c ∈ R such that
 R(ak−1, τ1, τ2, d1,P (aτ1, aτ2)) = 0.(64)

Moreover, R(ak−1, τ, τ, 0) ≡ 0.

Proof Recall that {∗(dP )j(x)}k
j=1 form an orthogonal basis in the orthogonal
complement to the tangent plane to the level set P −1(P (x)) at the point x (see
(59)). Let us make several remarks about the rational function RP (x, y) deﬁned by
(60).
1. If aτ = (ak−1, τ ) ∈ Km,δ is a regular value for the map (P1, . . . , Pk) : RN → Rk

for some τ , then ak−1 ∈ Rk−1 is a regular value for the map (P1, . . . , Pk−1) : RN →
Rk−1;
2. If ak−1 ∈ Rk−1 is a regular value for the map (P1, . . . , Pk−1) : BN → Rk−1,
then there is a positive ǫ(ak−1) > 0 such that for each point x ∈ (P1, . . . , Pk−1)
−1(ak−1)
and each 1 ≤ j ≤ k − 1

(∗(dP )j (x), ∗(dP )j (x)) > ǫ(ak−1) > 0.(65)

This follows from compactness of BN and regularity of the value ak−1;

V. Kaloshin 37

3. Since we consider only those τ that aτ belongs to the (m, δ)-cone Km,δ of
regular values of P there exists a positive constant ǫ(ak−1, τ ) > 0 such that for each
x ∈ P −1(aτ )
 (∗(dP )k(x), ∗(dP )k(x)) > ǫ(ak−1, τ ).(66)

This shows that Q(x, y) restricted to P −1(Km,δ) × P −1(Km,δ) is a smooth function
of x and y.
Consider irreducible representation of the rational function Q(x, y) as a ration
of two polynomials Q(x, y) = T (x,y)
S(x,y) . Because of remarks 2 and 3 S(x, y) ̸= 0 for
each pair (x, y) ∈ P −1(Km,δ) × P −1(Km,δ).
Now notice that we deal with smooth objects: smooth level sets P −1(aτ ) and
the smooth function QP (x, y). Notice that d
0
1,P (x, aτ2 ) is an extremal value of
the function QP (x, y) provided that P (y) = aτ2. Similarly, d1,P (aτ1, aτ2) is an
extremal value of the function d
0
1,P (x, aτ2) provided that P (y) = aτ1. To ﬁnd
all extremal values of a smooth function on a smooth manifold one can use the
Lagrange multipliers method. We prove that functions d1,P and d
0
1,P are algebraic
functions.
The key point of the Lagrange multipliers method is that at an extremal point of
QP (x, y) under the condition P (y) = aτ2 the gradient ∇yQP (x, y) can be expressed
as a linear combination of gradients ∇P1(y), . . . , ∇Pk(y), and ∇r(y). The gradient
of QP (x, y) has the form

∇yQP (x, y) = ∇y
 ( TP (x, y)
SP (x, y)
 ) = (SP (x, y)∇yTP (x, y) − TP (x, y)∇ySP (x, y)) S−2
P (x, y).

Since S|P −1(Km,δ)×P −1(Km,δ) ̸= 0 we can rewrite the Lagrange system in the
following form 



SP (x, y)∇yTP (x, y) − TP (x, y)∇ySP (x, y)+

+S2
P (x) [∑k
j=1 λj∇Pj (x) − λk+1∇r(y)
] = 0,

P (y) − aτ2
TP (x, y) − cSP (x, y) = 0,
λk+1r(y) = 0.

(67)

Important that all equations are polynomial and we can apply elimination theory!
Notice that the last equation is responsible for an extremal point y which might
belong to the boundary ∂BN . If a critical value belongs to the boundary, then
r(y) = 0 and λk+1∇r(y) is not zero and the gradient ∇yQP (x, y) should be ex-
pressed as a linear combination of k + 1 vectors ∇P1(y), . . . , ∇Pk(y), and ∇r(y). If
a critical value does not belong to the boundary, i.e. r(y) ̸= 0, then λk+1 = 0 and
λk+1∇r(y) = 0.
Complexify the system (67), i.e. consider the system (67) for

(x, y, λ, ak−1, τ2, c) ∈ CN × CN × Ck+1 × Ck−1 × C × C.

It deﬁnes a constructible set, denoted by V , in C2N +2k+2. Let us eliminate vari-
ables {λj}k+1
j=1 , {yi}N
i=1 by projecting V along the corresponding (N + k + 1)-
dimensional (λ, y)-plane. The result of projection is a constructible set W in the
space (x, ak−1, τ2, c) ∈ CN +k+1. By the construction a point (x, ak−1, τ2, c) belongs
to W if some value of y the following conditions hold: P (y) = aτ2, QP (x, y) = c,
and y is the critical point of QP restricted to P −1(aτ2 ).

38 Bifurcation of polycycles

The constructible set W has dimension N + k. Indeed, consider a polynomial
function ρx : P −1(aτ2) → R deﬁned by ρx(y) = QP (x, y). By Sard’s lemma for
algebraic sets [Mu] critical values of ρx form an algebraic set of positive codimension
in R. Therefore, the set of critical values consists of a ﬁnite number of points and
a ﬁnite number of possible c so that (x, ak−1, τ2, c) ∈ W . Thus, dim W equals
dimension of (x, ak−1, τ2, )-plane, i.e. dim W = N + k.
Since W is constructible and has codimension 1 there is a non zero polynomial
˜R(x, aτ2 , c) such that W ⊆ ˜R−1(0). By the deﬁnition (61) of d
0
1,P (x, aτ2 ) and by
the construction
 ˜R(x, aτ1 , aτ2, d
0
1,P (x, aτ2 )) ≡ 0.(68)

In order to prove that the function d1,P (aτ1, aτ2) deﬁned by (61) is also alge-
braic, calculate critical values of d
0
1,P (x, aτ2 ), provided P (x) = aτ1. By the implicit
function theorem the gradient ∇xd
0
1,P (x, aτ2) can be expressed in terms of partial
derivatives of ˜R(x, aτ2 , c) by the following way

∂xj d
0
1,P (x, a) = ∂c ˜R(x, a, c) (∂xj ˜R(x, a, c)
)−1 ,(69)

for (a, c) = (aτ2, d
0
1,P (x, aτ2 )) and provided that ∂xj ˜R(x, aτ2 , d
0
1,P (x, aτ2 )) ̸= 0 for
all 1 ≤ j ≤ N . Fix a = aτ2 and consider x outside of the union of algebraic sets B =
∪
N
j=1{x : ∂xj ˜R(x, a, c) = 0}. Then d
0
1,P (x, a) is a smooth function in x. Application
of the Lagrange multipliers method shows that at an extremal point of the function
d
0
1,P (x, a), provided P (x) = aτ1 , the gradient ∇xd
0
1,P (x, a) can be represented as

a linear combination ∇xd
0
1,P (x, a) = ∑k
j=1 λj∇Pj (x) − λk+1∇r(x). Plugging in
the expression for ∇xd
0
1,P (x, a) in terms of ∂c ˜R(x, aτ2 , c) and ∂xj ˜R(x, aτ2, c) for
j = 1, . . . , N we can present a Lagrange multiplier system in the following form





∂xj ˜R(x, aτ2 , c)∂c ˜R(x, aτ2 , c) =

= [∑k
j=1 λj∇Pj (x) − λk+1∇r1(x)
] (∂xj ˜R(x, aτ2, c)
)2

˜R(x, aτ2 , c) = 0,
P (x) = aτ1,
λk+1r(x) = 0.

(70)

Again the system (70) consists of only polynomial equations and we can apply
elimination theory. Consider this system for

(x, λ, ak−1, τ1, τ2, c) ∈ CN × Ck+1 × Ck−1 × C × C × C.

It deﬁnes a constructible set, denoted by V1, in CN +2k+3. Let us eliminate vari-
ables {λj}k+1
j=1 , {xi}N
i=1 by projecting V along the corresponding (N + k + 1)-
dimensional (λ, x)-plane. The result of projection is a constructible set W1 in
the space (ak−1, τ1, τ2, c) ∈ Ck+2.
Similarly to the arguments for the constructible set W one can show that W1 has
dimension k. Since W1 is constructible and has codimension 1 there is a nonzero
polynomial R(ak−1, τ1, τ2, c) such that W1 ⊆ R−1(0). By the deﬁnition (61) of
d1,P (aτ1, aτ2) and by the construction

R(aτ1, aτ2, d1,P (aτ1, aτ2)) ≡ 0.(71)
 V. Kaloshin 39

By the construction if aτ1 = aτ2, then R(aτ1, aτ1, 0) ≡ 0, because in this case
both level sets are the same and C1-distance between them must equal zero. This
completes the proof of Lemma 3.

Lemma 4. With the notations above there exists a reﬁnement (m′, δ′)-cone Km′,δ′ ⊂
Km,δ such that for any pair of points aτ1 = (ak−1, τ1) and aτ2 = (ak−1, τ2) from
Km′,δ′
 D1
P (aτ1, aτ2) ≤ (a1 . . . a1k − 1)
2,(72)

where ak−1 = (a1, . . . , ak−1) ∈ Rk−1.

Proof It follows from Lemma 3 that there is a polynomial R(aτ1, aτ2, c) such
that R(aτ1 , aτ2, d1,P (aτ1, aτ2)) ≡ 0 and R(a, τ, τ, 0) ≡ 0.
For aτ1, aτ2 belonging to the (m, δ)-cone Km,δ of regular values of P the function
d1,P (aτ1, aτ2) depends continuously on τ1 and τ2. Let us rewrite R(aτ1, aτ2, c) in
the form R(ak−1, τ1, τ2, c). Recall that in our notations aτ = (ak−1, τ ).
Suppose for determiness that τ1 > τ2. Notice that each suﬃciently small positive
root cj(ak−1, τ1, τ2) is increasing in τ1 and decreasing in τ2 in a neighborhood of
(ak−1, τ1, τ2) = 0. Therefore, cj(ak−1, τ1, 0) > cj(ak−1, τ1, τ2)
Denote R(ak−1, τ, c) = R(ak−1, τ, 0, c). Let us show that for some suﬃciently
large positive integers m′ and m′′ if 0 < τ < (ak−1
1 . . . ak−1
k−1c)
m′ and 0 < c <
(ak−1
1 . . . ak−1
k−1)
m′′ the following decomposition holds: Put c = ρ(ak−1
1 . . . ak−1
k−1)
m′′

and τ = λ(ak−1
1 . . . ak−1
k−1c)
m′ with ρ, λ ∈ (0, 1). Then

R(ak−1, τ, c) = r0(ak−1)(1 + q1(ak−1, ρ))(1 + q2(ak−1, ρ, λ)),(73)

where r0, q1, q2 are polynomials in their variables. Indeed, apply the same argu-
ments as we used to prove (63) to the polynomial

R(ak−1, τ, c) =
 deg R∑

j=1 Rj(ak−1, c)τ j + R0(ak−1, c).

Then apply the same arguments to

R0(ak−1, c) =
 deg R0∑

j=1 rj(ak−1)cj + r0(ak−1, c).

Notice that R(ak−1, 0, 0) ≡ 0 implies that q1(0, ρ) ≡ q2(0, ρ, λ) ≡ 0. Therefore, for
a suﬃciently small δ′ > 0 and any (ak−1, δ′) ∈ Km,δ′ polynomials q1(ak−1, ρ) and
q2(ak−1, ρ, λ) are suﬃciently small and R(ak−1, τ, c) equals 0 if and only if r0(ak−1)
equals 0.
By Lemma cone there is a reﬁnement (m′, δ′)-cone Km′,δ′ ⊂ Km,δ′ such that
r0(ak−1) does not vanish on Km′,δ′ .
Now put m′
k = m′m′′. As we have just shown all suﬃciently small positive roots
cj(ak−1, τ, 0) < τ 1/m′ (ak−1
1 . . . ak−1
k−1) provided that

τ 1/m′ (ak−1
1 . . . ak−1
k−1) < (ak−1
1 . . . ak−1
k−1)
m′′.

This condition is satisﬁed for any 0 < τ < (ak−1
1 . . . ak−1
k−1)
m′m′′. This shows that all
suﬃciently small positive roots

cj(ak−1, τ, 0) < (ak−1
1 . . . ak−1
k−1)
m′′+1 < (ak−1
1 . . . ak−1
k−1)
2.

This completes the proof of the Lemma.

40 Bifurcation of polycycles

Let us complete the proof of part c) Theorem 41 by the following inductive
arguments.
Consider a sequence of positive integers m2, . . . , mk. Let m = (1, m2, . . . , mk)
and δ > 0. Deﬁne a sequence of polynomials associated to this sequence, deﬁned
by their coordinate functions:

P 0
j = Pj − (P1 . . . Pj−1)
mj , j = 2, . . . , k

P s = (P 0
1 , . . . , P 0
s , Ps+1, . . . , Pk−s), s = 2, . . . , k
(74)

Deﬁne the restriction of the (m, δ)-cone Km,δ to the s-dimensional plane, denoted
by K s
m,δ, generated by the ﬁrst k-coordinates by the following way:

K s
m,δ = {as = (a1, . . . , as) ∈ Rs : 0 < a1 < δ,

0 < |aj+1| < |a1 . . . aj|mj+1 for j = 1, . . . , s − 1}.
(75)

It is shown above that there is an (m, δ)-cone Km,δ such that any point (0, ak−1) ∈
R × K k−1
m,δ is a regular point for the polynomial P k−1. Therefore, one can apply
Lemmas 2, 3, and 64 and show that there is reﬁnement of K k−1
m,δ , denoted the
same, such that for any two points ak−1
τ1 = (0, ak−2, τ1) and ak−1
τ1 (0, ak−2, τ2) from
R × K k−1
m,δ
 D1
P 1(ak−1
τ1 , ak−1
τ2 ) ≤ (a1 . . . ak−2)
2.(76)

By induction one can show that there is a reﬁnement an (m, δ)-cone Km,δ such
that for any two points ak−s
τ1 = (0, ak−s−1, τ1) and ak−s
τ1 (0, ak−s−1, τ2) from the
restriction cone K k−s
m,δ such that

D1
P s(ak−s
τ1 , ak−s
τ2 ) ≤ (a1 . . . ak−s−1)
2.(77)

Notice that for any 1 ≤ s ≤ k level sets of the polynomial P s correspond to level sets
of the initial polynomial P . Combining this with all estimates for D1
P s(ak−s
τ1 , ak−s
τ2 )
and the triangle-like inequality (62) one can show that part c) of Theorem 41 holds
true. Part a) of Theorem 41 follows from part c) because QP (x, y) ≥ ∥x − y∥2,
which implies that D1
P (a, b) ≥ D0
P (a, b) for any pair a, b ∈ Km,δ.
This completes the proof of Theorem 41.

References

[AAI] D. Anosov, V. Arnold, Yu. Ilyashenko, Dynamical systems. I, Encyclopaedia Math. Sci.,
1, Springer, Berlin, 1988;
[AGV] V. Arnold, S. Gusein-Zade, A. Varchenko Singularities of diﬀerentiable maps. Vol.
I.Monographs in Mathematics, 82, Birkhuser Boston, 1985.
[BCR] J. Bochnak, M. Coste, M.-F. Roy, Real Algebraic Geometry, Springer-Verlag, Berlin, 1998.
[D] F. Dumortier, Singularities of vector ﬁelds on the plane, J. Diﬀ.Equations, 23, (1977),
53–106.
[E] J. Ecalle, Introduction aux fonctions analysables et preuve consrustive de la conjecture de
Dulac, Herman, Paris, (1992).
[FP] J.-P. Francoise, C. Pugh, Keeping track of limit cycles. J. Diﬀ. Eqns 65, (1986), no. 2,
139–157.
[GWPL] C.G. Gibson, K. Wirthmuller, A.A. du Plessis, E.J.N.Loojenga, Topological Stability of
Smooth Mappings, Lectures Notes in Mathematics 552, Springer 1976.
[GG] M. Golubitsky, V. Guillemin, Stable Mappings and Their Singularities, Graduate Texts in
Mathematics 14, Springer-Verlag 1973.
[GM] M. Goresky, R. MacPherson, Stratiﬁed Morse Theory, Springer-Verlag 1987.
[G] T. Grozovskii, Bifurcations of polycycles an “apple” and a “half-apple” in generic two-
parameter families, Diﬀ. Equations (in Russian), Vol.32, (1996), no. 4, pp. 458–469.

V. Kaloshin 41

[Hir1] H. Hironaka, Stratiﬁcation and ﬂatness Real and Complex singularities, Nordic Summer
School (Oslo, 1976), Sijthoﬀ-Noordhoﬀ, Growhgen, (1977)
[Hir2] H. Hironaka, Introduction to real-algebraic sets and real-analytic maps,Instituto Mathe-
matico L.Tonelli, Dell’ Universita’di Piza, 1973
[I] Yu. Ilyashenko, Finiteness theorem for limit cycles, Amer. Math. Soc., Providence, (1991).
[IK] Yu. Ilyashenko, V. Kaloshin, Bifurcations of planar and spatial polycycles: Arnold’s pro-
gram and its development, Fields Inst Comm Vol 24, (1999), pp. 241-271
[IY1] Yu.Ilyashenko, S.Yakovenko, Finitely smooth normal forms of local families of diﬀeomor-
phisms and vector ﬁelds, Russian Math. Surveys 46 (1991), no. 1, 1–43
[IY2] Yu.Ilyashenko, S.Yakovenko, Concerning Hilbert sixteenth problem, Amer. Math. Soc.
Transl, Ser.2, 165, (1995), 1–20.
[IY3] Yu.Ilyashenko, S.Yakovenko, Finite Cyclicity of Elementary Polycycles in Generic Families,
Amer.Math.Soc.Transl, 165, (1995), 21–95.
[J] N. Jacobson, Basic Algebra, vol.1, 1974
[Ka1] V. Kaloshin, A Geometric Proof of Existence of Whitney’s stratiﬁcations, submitted to
Ann. of Math.
[Kh] A.Khovanskii, Fewnomials, Amer.Math.Soc. Providence,RI, 1991
[KS] A. Kotova, V. Stanzo, Few-Parameter Generic Families on the Sphere, Amer. Math. Soc.
Translations, Providence, RI, Ser. 2, 213,1996 pp. 155–202
[Ma] J. Mather, Notes on topological stability, Harvard University
[Mi] J. Milnor, Singular points of complex hypersurfaces Princeton University Press, Princeton,
NJ, 61 1968
[Mu] D. Mumford, Algebraic Geometry I, Complex Projective Algebraic Varieties, Springer-
Verlag, 1976
[PW] A. du Plessis, T. Wall, The Geometry of Topological Stability, Oxford, 1995;
[R] R. Roussarie, Cyclicite ﬁnie et le 16 problem d’Hilbert, Dynamical systems, (Volparaiso,
(1986)), (R.Bauon, R.Lavarca, and J.Palis, eds.), LNM, 1331, Springer-Verlag, Berlin and
New York, (1988), 161–188.
[S] D. Shlomick(ed), Bifurcations and periodic orbits of vector ﬁelds, NATO AS1, Series C
(Math. and Phys. Sciences), vol. 408, Kluwel, Dordrecht, Boston, London, (1993).
[Ta] F. Takens, Unfoldings of certain singularities of vector ﬁelds: generalized Hopf bifurcations,
J. Diﬀerential Equations 14 (1973), pp. 476–493.
[Th] R. Thom, Ensembles et morphismes stratiﬁs. Bull. Amer. Math. Soc. 75 1969, pp. 240–284.
[Ti] V. Tikhomirov, Fundamental principles of the theory of extremal problems. Transl. by
Bernd Luderer. John Wiley & Sons, 1986.
[Wa] T. Wall, Regular Stratiﬁcations, Lecture Notes in Mathematics, No. 468, pp. 332-344;
[W] H. Whitney, Elementary structure of real algebraic varieties, Ann. of Math 66 1957 no.3
545–556

Fine Hall, Princeton University, Princeton, NJ, 08540
E-mail address: kaloshin@math.princeton.edu
