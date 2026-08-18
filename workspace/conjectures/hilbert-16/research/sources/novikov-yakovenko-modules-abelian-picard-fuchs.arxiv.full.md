<!-- source: https://arxiv.org/pdf/math/0110126 | converted from PDF -->

arXiv:math/0110126v3  [math.DS]  6 Jun 2002
Modules of Abelian integrals and Picard-Fuchs
systems
 Abstract. We give a simple proof of an isomorphism between two C[t]-
modules corresponding to bivariate polynomial H with nondegenerate highest
homogeneous part: the module of relative cohomologies Λ2/dH ∧ Λ1 and the
module of Abelian integrals. Using this isomorphism, we prove existence and
deduce some properties of the corresponding Picard-Fuchs system.

D. Novikov

Department of Mathematics, Purdue University, West Lafayette, IN 47907, USA

E-mail: dmitry@math.purdue.edu
‡

‡ The research was supported by the Killam grant of P. Milman and by James S. McDonnell
Foundation.

Modules of Abelian integrals and Picard-Fuchs systems 2

Abelian integral is a result of integration of a polynomial one-form along a cycle
lying on level curve (possibly complex) of a bivariate polynomial considered as a
function (possibly multivalued) of the value of the polynomial. Abelian integrals
appear naturally when studying bifurcations of limit cycles of planar polynomial vector
ﬁelds. In particular, zeros of Abelian integrals are related to limit cycles appearing
in polynomial perturbations of polynomial Hamiltonian vector ﬁelds. This is the
reason why sometimes the question about the number of zeroes of Abelian integrals
is sometimes called inﬁnitesimal Hilbert 16th problem.
The traditional approach to the investigation of Abelian integrals uses properties
of the system of linear ordinary diﬀerential equations satisﬁed by the Abelian integrals,
the so-called Picard-Fuchs system. This approach is used both in fundamental general
ﬁniteness result of [24, 13] and in exact estimates in the cases of low degree, as in [9].
The existence of such a system can be easily proven due to the very basic properties
of branching of Abelian integrals, see [1], and was well known already to Riemann
if not Gauss. Nevertheless an eﬀective computation of this system turns out to be
a diﬃcult problem. One particular case of this problem (namely of the hyperelliptic
integrals) is quite classic, see e.g. [21, 19, 7]. In [18] a generalization of this approach
for regular at inﬁnity (see below for exact deﬁnition) polynomials in two variables is
suggested (in fact, it can be easily generalized for any number of variables). The main
idea of [18] is to trade the minimality of the size of the system (thus redundant) for
an explicitness of the construction and control on the magnitude of the coeﬃcients.
Another, probably not less important, gain is that the resulting system is not only
Fuchsian, but also has a hypergeometric form.
The control on the magnitude of coeﬃcients in [18] is very important from the
inﬁnitesimal Hilbert 16th problem point of view. Indeed, recent progress towards its
solution is partly based on the principle that solutions of linear ordinary diﬀerential
equations with bounded coeﬃcients cannot oscillate too wildly, see e.g. [11] (simple
proofs of a result of this type can be found in [16] and [23]). Though more complicated,
this principle still holds for polynomial systems of diﬀerential equations, see [16, 17]
(polynomiality is essential, see [14]). In a slightly modiﬁed form, this principle allows
to give results in an upper bound on the number of zeros of an Abelian integral in terms
of the minimal distance between critical values of its (regular at inﬁnity) Hamiltonian,
see [18]. As an application of this principle one can also deduce an eﬀective upper
bound for the number of zeroes of Abelian integrals corresponding to hyperelliptic
Hamiltonians satisfying some additional assumption, see [15].
The Picard-Fuchs systems discussed in this paper is irredundant in the sense that
it has the minimal possible dimension (namely the dimension equal to the dimension of
the homology group H 1({H(x, y) = t}, C) of a generic ﬁbre). This minimality allows
to guess most of the important information about the system if the critical values
of the Hamiltonian are distinct and the Hamiltonian is regular at inﬁnity (so-called
Morse-plus Hamiltonians).
We prove existence of such system using decomposition in Petrov modules. It is
easy to see that exact forms and forms proportional to dH have zero Abelian integrals,
so in fact Abelian integrals depend on the class of a form in the so-called Petrov module
– the quotient of the space of all forms by a subspace spanned by exact forms and
forms proportional to dH, considered in [20]. In [5] L.Gavrilov proved that the Petrov
module of a generic Hamiltonian is a ﬁnitely generated free C[t]-module.The local
counterpart of this statement is due to E.Brieskorn and M. Sebastiani [3, 22]. The
proof in [5] contains a reference to a general nondegeneracy result (see [1, Theorem

Modules of Abelian integrals and Picard-Fuchs systems 3

13.6, Ch III]), based on the theory of deformations of Hodge structures. In the recent
preprint [8] the involved constant is computed and exact formulae are given. We
suggest an elementary proof of this result, see also [25].
The main idea of [18] was to use a connection between division with remainder of
polynomials and diﬀerentiation of Abelian integrals given by Gelfand-Leray formula.
In this work we replace the explicit division with remainder by decomposition in Petrov
modules in order to get the same result. This is still enough for the construction of
the system, though the result is less explicit. Yet one can still guess all singular
points and get some information about coeﬃcients. However, we show that the
resulting irredundant system is not always Fuchsian, namely it can have regular but
non-Fuchsian point at inﬁnity. Though after a suitable rational gauge transform the
irredundant system becomes Fuchsian (see §5), the nice form of Theorem 1 is then
lost.

0.1. Acknowledgments

I am grateful to S. Yakovenko for the numerous discussions and help in preparation
of this text. I am grateful to Yulij Ilyashenko for an opportunity to read his recent
preprint and numerous discussions. I am grateful to anonymous referee for several
important remarks.

1. Genericity and generalities

In what follows we always assume that our polynomial H(x, y) is regular at inﬁnity,
i.e., that its highest homogeneous part ̂H(x, y) is a product of pairwise diﬀerent linear
factors.
One can easily prove that for regular at inﬁnity polynomial H(x, y) of degree
n + 1 the homogeneous polynomial ̂H has an isolated critical point (necessarily of
multiplicity µ = n2) at the origin (x, y) = (0, 0), its level curves { ̂H = c} ⊂ C2 are
nonsingular for c ̸= 0. Moreover, the level curves of H intersect transversally the line
at inﬁnity, and foliation of C2 by level curves of H is locally topologically trivial over
C \ Σ, where Σ is the set of ≤ (deg H − 1)
2 critical values of H. In other words, the
only atypical values are the critical ones.
By Abelian integral we mean a result of integration of a one-form ω along a
continuous family of cycles δ(t) ⊂ {H = t} considered as a function of t:

Iω,δ(t) = ∮

δ(t) ω.

Basic properties of Abelian integrals can be found in [1]. We will need the
following ones. First, Abelian integral depends not on δ itself but on its class of
homology [δ] ∈ H1({H = t}, Z) only. Also, the Abelian integral corresponding to a
form ω is identically zero if ω = f dH + dg, i.e. Abelian integrals depend in fact on the
relative cohomology class of [dω] ∈ Λ1/dH ∧Λ0 +dΛ0 only. This quotient module – the
so-called Petrov module – is a C[t]-module with respect to a standard multiplication
t[ω] = [H(x, y)ω].
Second, the Abelian integrals are holomorphic multivalued functions of a complex
variable t branching at the critical values of H only (for H regular at inﬁnity). So
the space of all Abelian integrals is also a C[t]-module with respect to a natural
multiplication by t.

Modules of Abelian integrals and Picard-Fuchs systems 4

We will prove that these two modules coincide for a regular at inﬁnity polynomial
H(x, y). We prove existence of the corresponding Picard-Fuchs system using this
isomorphism, and ﬁnd out some of its properties.

2. Nondegeneracy of the principal determinant

Here we prove that the homogeneous forms generating the C[t]-module Λ2/dH ∧ Λ1,
also generate the ﬁrst cohomology group of a generic level curve of H. Note that
this C[t]-module is isomorphic to C[x, y]/ ⟨Hx, Hy⟩. Indeed, Qdx ∧ dy = Rdx ∧ dy +
(Hxdx + Hydy) ∧ (Adx + Bdy) is equivalent to Q = R + BHx − AHy.
Recall that nonsingular level curves of a regular at inﬁnity polynomial H of degree
n + 1 carry µ = n2 vanishing cycles δj(t) that generate the whole ﬁrst homology group
of all regular curves {H = t} [1, 5]. For any collection of µ polynomial 1-forms
ω1, . . . , ωµ the period matrix Xω(t) formed by integrals of ωi over δj (integrals of the
same form occur in the same row, the same cycle corresponds to entries of the same
column) has the same monodromy. The monodromy transformations act on X(t) as
multiplications from the right by constant monodromy matrices that are unimodular
by virtue of Picard–Lefschetz formulas [1]. Thus det X(t) is a single-valued function
that must have zeros at all critical values t = tj, j = 1, . . . , µ, counting multiplicities,
since the columns corresponding to the cycles vanishing at tj become zero at tj (we use
the fact that to any critical value of multiplicity ν correspond ν linearly independent
cycles vanishing at this critical value). As the growth of X at inﬁnity is at most
polynomial, det X(t) is a polynomial divisible by ∆H (t) = ∏µ
j=1(t − tj).

Lemma 1 (cf. with [5], Lemma 2.2) If the 2-forms dωi generate Λ2/dH ∧ Λ1 and

µ∑

i=1 deg ωi = µ deg H,

then det Xω(t) = c(t − t1) . . . (t − tµ) with c ̸= 0 (some ti may coincide).

The constant c depends both on the choice of ωi and on the choice of the cycles δj(t).
Its actual calculation is a diﬃcult task, see [8].
Remark. The condition on the degrees of the forms in the Lemma 1 is automatically
satisﬁed if the Hamiltonian H(x, y) and the forms dωi are homogeneous, see [1].
For non-homogeneous Hamiltonian this condition is essential. Among other things,
this condition implies that the highest homogeneous parts ̂ωi of dωi form a basis of
Λ2/d ̂H ∧ Λ1. Vice versa, any monomial basis of Λ2/d ̂H ∧ Λ1 is a basis of Λ2/dH ∧ Λ1

satisfying this condition (and this is a standard way to get a basis of Λ2/dH ∧ Λ1).
The proof is based on the calculation of the “principal term” of the asymptotic
of X(t) at inﬁnity.

Lemma 2 For any collection of polynomial 1-forms ωi the period matrix Xω(t) admits
a converging expansion

Xω(t) = tDC(t), C(t) =
 ∞∑

k=0 Ckt−k/(n+1), (2.1)

where D is the diagonal matrix with the entries di = deg ωi/(n + 1), C0, C1, . . . are
constant matrices and C0 = C(∞) is the matrix of integrals of the highest homogeneous
parts ̂ωi of forms ωi over vanishing cycles lying on the level curve { ̂H = 1}.

Modules of Abelian integrals and Picard-Fuchs systems 5

Proof of Lemma 2. The level curve {H(x, y) = t} in the variables x = t1/(n+1)̂x,
y = t1/(n+1)̂y becomes a family of the curves

̂H(̂x, ̂y) + t−1/(n+1)Hn(̂x, ̂y) + · · · = 1,

where the left hand side is a polynomial in ̂x, ̂y and t−1/(n+1). In other words, we have
an analytic in t−1/(n+1) perturbation of the limit curve { ̂H(̂x, ̂y) = 1} ⊂ C2 that is
nonsingular (since ̂H has no multiple factors). Integrals of any (constant or analytic
in t−1/(n+1)) 1-form over any continuous family of cycles on such family will be also
analytic in t−1/(n+1).
The forms ωi after rescaling become tdi(θi + t−1/(n+1)ηi), where di =
deg ωi/(n + 1), θi is a new independent of t homogeneous polynomial form
(corresponding to the highest homogeneous part ̂ωi of ωi) and ηi is another polynomial
form. Therefore the integrals of ωi over cycles δj(t) on the level curves {H = t} can
be expanded in the converging series in t−1/(n+1) of the form
∮

δj (t) ωi = tdi(c0,ij + c1,ijt−1/(n+1) + · · ·),

if c0,ij is the integral of ̂ωi over the cycle δj ⊂ { ̂H = 1}. ⊓⊔
Remark. The representation (2.1) is unique only if we ﬁx the diagonal matrix D.
Otherwise the power tD may itself be expanded as a series in powers of t−1/(n+1), thus
yielding an essentially diﬀerent representation.

Corollary 1 The determinant of the period matrix Xω(t) is a polynomial of degree
at most m = m(ω) = tr D = ∑i deg ωi/(n + 1). If this number is not integer, then
automatically det C0 = 0 for this choice of the forms, otherwise the leading term tm

of detXω(t) enters with the coeﬃcient det C0.

Proof of the Lemma 1. Given the assumption on the degrees deg ωi, the determinant
det Xω(t) is a polynomial of degree ≤ µ, and hence (by the divisibility property noted
above) it must have a form c ∏
(t − tj). We need only to verify that c ̸= 0, and from
the asymptotic formulas we see that c = det C0, so our goal is to prove that C0 is a
nondegenerate matrix.
The calculation above shows that the matrix ̂X(t) of periods of ̂ωi over the
level curves of a homogeneous part ̂H, can be represented as tDC0 (the same
expansion without inferior terms). Thus if C0 is degenerate, then there exists a linear
combination ̂δ(t) = ∑µ
1 rj δj(t), rj ∈ C, of vanishing cycles on the level curves of ̂H,
such that integrals of all forms ̂ωi over the cycle ̂δ(t) are identically zeros.
Take any polynomial 2-form dω. Since the forms d̂ωi form a basis of Λ2/d ̂H ∧ Λ1,
the form dω can be divided out by d ̂H with remainder in the span of d̂ωi, i.e.,

dω = d ̂H ∧ η +
 µ∑

1 cid̂ωi, ci ∈ C,

where η is a suitable polynomial 1-form.
This representation is not unique. However, since H is regular at inﬁnity, one can
construct such representation with degree of η being less than deg ω (in fact, less or
equal to deg ω − deg H, see [18]).

Modules of Abelian integrals and Picard-Fuchs systems 6

Recall that the derivative of an Abelian integral of a form ω with respect to t is
again an Abelian integral of the Gelfand-Leray residue θ = dω
dH of the form ω:

d
dt
 ∮

δ(t) ω = ∮
δ(t) θ,

if dH ∧ θ = dω.
Return to the division with remainder of the form dω by d ̂H. Integrating over
the cycle ̂δ(t) and using the Gelfand–Leray formula, we see that

d
dt
 ∮
̂δ(t) ω = ∮
̂δ(t) η,

since integrals of d̂ωi
d ̂H over ̂δ(t) all vanish. In other words, the derivative of any Abelian

integral of a polynomial form over the cycle ̂δ(t) is again an Abelian integral of a
polynomial form. Since the cycle ̂δ(t) is also vanishing at t = 0 (recall that we deal
with the homogeneous case and all δi(t) vanish at the same value t = 0), the limit of∮̂δ(t) η is zero for any polynomial form η as t → 0.
As the Gelfand–Leray derivative η is a polynomial form of smaller degree, the
above argument can be repeated, showing that some derivative of the initial integral∮̂δ(t) ω is zero. Since the integral itself and all its derivatives tend to zero as t → 0,
we conclude that the initial Abelian integral is identically zero. Since ω was arbitrary,
this proves that integrals of all polynomial forms over the cycle ̂δ(t) are identically
zeros.
But this is clearly impossible unless ̂δ ≡ 0 in H1({ ̂H = 1}, C). The shortest way
to show this is to refer to [1], where the following statement is proved.

Lemma 3 ([1]) For an isolated singularity with Milnor number µ one can always
construct µ holomorphic 1-forms θ1, . . . , θµ such that the period matrix Xθ(t) (integrals
of ωi over all vanishing cycles) will have the determinant det Xθ(t) = tµ + · · ·. ⊓⊔

This lemma can be applied to the homogeneous germ ̂H and the forms in [1] are
in fact constructed polynomial (of course, of suﬃciently high degrees). Namely, for an
arbitrary nonzero cycle (in particular, for ̂δ(t)) a suitable linear combination of θi has
integral not identically zero, which contradicts the choice of ̂δ(t). ⊓⊔
Remark. The assertion of the above Lemma is by far much stronger than required to
complete the proof: it would be suﬃcient to ﬁnd just one polynomial form in C2 such
that the integral of its restriction to the aﬃne curve { ̂H = t} along ̂δ(t) ̸= 0 would
be non-zero. This can be done using the fact that { ̂H = 1} is a Stein manifold, and
therefore each element of its cohomology group can be realized as a restriction of a
holomorphic one-form on C2. More exact, let ω be a holomorphic form on { ̂H = 1}
such that its integral along ̂δ is nonzero. One can ﬁnd a holomorphic form ˜ω on
C2 which restriction to { ̂H = 1} is cohomologous to ω. Since the cycles generating
H1({ ̂H = 1}, C) have compact representatives, a polynomial one-form suﬃciently close
approximating ˜ω on a suﬃciently big compact will also produce nonzero integral along
̂δ(t) (since analytic in C2 coeﬃcients of the form ˜ω can be uniformly approximated by
polynomials on any compact set).

Modules of Abelian integrals and Picard-Fuchs systems 7

3. Module of the Abelian integrals

Now, after Lemma 1 is proved, we can immediately prove that integrals of the forms
dωi generate over C[t] the entire module of Abelian integrals. The proof appears in
[5] and is a straightforward application of the Cramer rule. We reproduce this proof
here for reader’s convenience.

Proposition 1 (Gavrilov theorem [5]) Let ω1, . . . , ωµ be one-forms such that∑µ
i=1 deg ωi = µ deg H, and suppose that the polynomials dωi
dx∧dy are linearly
independent modulo the gradient ideal < Hx, Hy > in C[x, y].
Then integral of any polynomial 1-form ω can be represented as a linear
combination of integrals of the forms ωi with polynomial in t coeﬃcients: for any
cycle δ(t) on the level curve {H = t}
∮

δ(t) ω =
 µ∑

i=1 pi(t) ∮

δ(t) ωi, pi(t) ∈ C[t], (n + 1) deg pi + deg ωi ≤ deg ω. (3.1)

Remark. The condition on degrees is again essential: if H(x, y) is not homogeneous,
then not every basis of monomial forms of Λ2/dH ∧ Λ1 generates the Petrov module.
A (more transparent weight-homogeneous) example is H = y2 + x
4 − x
2 and the set
of monomial forms dx ∧ dy, x
2dx ∧ dy, x
5dx ∧ dy. However,for homogeneous H and
homogeneous ωi this condition is satisﬁed automatically, see [1].
Proof . We look for a tuple of real functions pi(t) such that identically over t and for
any vanishing cycle δ(t) = δj(t) the equality (3.1) holds. These equations for each t
form a linear nonhomogeneous system with the matrix of coeﬃcients X(t) being the
period matrix ∮

δj ωi and the column of right hand sides being periods of the form ω.
Since the matrix X(t) is nondegenerate (for all t ̸= tj), the solution of this
system can be found by the Cramer rule: each pi is a ratio of two determinants. The
denominator is det X(t) = c ∏
j(t − tj), whereas the numerator is the determinant of
the period matrix obtained by replacing ωi by ω. By the same arguments as in the
beginning of §2, the numerator should be a polynomial divisible by ∏µ
1 (t − tj), hence
the inequality c ̸= 0 ensures that the ratio is in fact a polynomial function of t. To
estimate the degree of the nominator, we use Corollary to Lemma 2: it is no greater
than deg det X(t) + deg ω−deg ωi
n+1 . Therefore deg pi ≤ (deg ω − deg ωi)/(n + 1). ⊓⊔
Remark. The uniqueness of the representation (3.1) follows from a theorem
by Gavrilov (see [5, 6]) that a polynomial 1-form with all zero periods must be
necessary a(x, y)dH + db(x, y), where a, b appropriate polynomials, provided that the
Hamiltonian H(x, y) is regular at inﬁnity (the conditions in [5] are even weaker). This
result is a generalization of an earlier result of Ilyashenko [10].
The local counterpart of Proposition 1 claims that the ring of relative cohomology
is ﬁnitely generated as a C{t}-module (Brieskorn–Sebastiani [3, 22]).

4. Derivation of the irredundant Picard–Fuchs system and its elementary
properties

Let ω1, . . . , ωµ be polynomial 1-forms as in Proposition 1, i.e., they satisfy the
condition ∑µ
1 deg ωi = µ deg H and their diﬀerentials dωi generate Λ2/dH ∧ Λ1.

Modules of Abelian integrals and Picard-Fuchs systems 8

The second assumption guarantees that we may divide out the 2-forms H(x, y)dωi
for all i = 1, . . . , µ, obtaining

H dωi = dH ∧ ηi +
 µ∑

j=1 aijdωj, i = 1, . . . , µ, (4.1)

with appropriate polynomial forms ηi of degrees deg ηi ≤ deg ωi ≤ 2n. This by the
Gelfand–Leray formula implies that for any cycle δ(t)

(t−A) ˙I(t) = J(t), where I = (
∮

δ(t) ω1, ..., ∮

δ(t) ωµ)
T , J = (
∮

δ(t) η1, . . . , ∮

δ(t) ηµ)
T .

Here occurs the diﬀerence with the computations from [18]: we cannot claim that
the integrals Ji are linear combinations of Ij , since the linear span of the forms dωi
does not contain all 2-forms of degrees ≤ 2n (in [18] this decomposition was written for
all monomials of degree ≤ 2n which resulted in a hypergeometric system of doubled
size with a Fuchsian singularity at inﬁnity).
However we can use the decomposition provided by Proposition 1 and write

J(t) = B(t)I(t), B(t) = B0 + tB1,

i.e B(t) is a matrix polynomial of degree ≤ 1.
This proves the following result.

Theorem 1 The period matrix X(t) of the forms ωi satisfying the above three
conditions, is a nondegenerate solution to the system of ﬁrst order linear ordinary
diﬀerential equations

(t − A) ˙X(t) = (B0 + B1t)X(t), A, B0, B1 ∈ Matµ×µ(C). (4.2)

Some properties of the matrices A, B0, B1 can be established by a simple
inspection. First, after identiﬁcation of Λ2/dH ∧ Λ1 with C[x, y]/ < Hx, Hy >, the
equation (4.1) means that A is a matrix of multiplication by H in C[x, y]/ < Hx, Hy >.
Suppose for a moment that H(x, y) has µ simple pairwise diﬀerent critical values.
Let (xj , yj), j = 1, . . . , µ be critical points of H. Denote by vj the µ-dimensional
vector, whose components are the coeﬃcients dωi
dx∧dy evaluated at the point (xj , yj).
Such vectors form a basis in Cµ by the second condition imposed on the forms. For
example, if the coeﬃcients of ωi are monomials x
αyβ with 0 ≤ α, β ≤ n − 1, then
together vj, j = 1, . . . , µ form a two-dimensional analog of the Vandermonde matrix.

Proposition 2 The matrix A is diagonalizable, its eigenvalues are critical values of
H whereas the eigenvector corresponding to the critical value tj is vj.

Proof . The right hand side of the expression (4.2) has j-th column zero if evaluated
at the point t = tj, since the corresponding cycle vanishes. The corresponding column
of the matrix ˙X(tj) is therefore in the kernel of (tj − A). Since the number of
critical values is equal to the dimension of the system (recall we are dealing with the
irredundant case), this proves the assertion about diagonalizability and the spectrum
of A.
To complete the proof we need only to compute the derivatives ˙Ii(tj ). The
Gelfand–Leray derivative dωi/dH has zero residues on all nonsingular level curves,
but restricted on {H = tj} it has a nontrivial residue. This can be immediately
seen for the normal form when H(x, y) = y2 − x
2 (note that all considerations are

Modules of Abelian integrals and Picard-Fuchs systems 9

local, so one can use the Morse normal form near the critical point (xj , yj)). Indeed,
if dω = f (x, y) dx ∧ dy, then dω/dH can be chosen as 1
2 f dx/y, and its restriction
on (one of the two smooth branches of) the curve H = 0, say, y = x, yields a
meromorphic 1-form 1
2 f (x, x) dx/x, whose residue (integral over a small loop around
x = 0) is πif (0, 0). Returning to the initial problem, we see that ∮

H=tj dωi
dH diﬀers from

π dωi
dx∧dy (xj, yj) by a nonzero factor, the Hessian of the transformation taking H into
the Morse form as above. Since this nonzero factor is common for all forms, we see
that the vector of residues ( ˙I1(tj), . . . , ˙Iµ(tj)) is proportional to the vector vj whose
coordinates are dωi
dx∧dy (xj , yj), i = 1, . . . , µ. ⊓⊔
By continuity one can conclude that

Corollary 2 For any regular at inﬁnity Hamiltonian H(x, y) its critical values tj
counted with multiplicities are the eigenvalues of the matrix A, and the vectors vj are
eigenvectors of A

The matrices B0, B1 in principle can be computed by evaluating the expansion
for X(t) at inﬁnity, see Lemma 2. One can guess some of their properties just by
taking dωi homogeneous and of nondecreasing degree.

Proposition 3 Let dωi be homogeneous and deg dωi ≤ deg dωj whenever 1 ≤ i < j ≤
µ. Then B0 and B1 are both lower triangular. Moreover, the diagonal entries of B0
are just the degrees of the forms divided by deg H, and B2
1 = 0

Proof . This follows from the careful analysis of the forms ηi in (4.2). Indeed,
deg ηi ≤ deg ωi, so in the decomposition of ηi provided by Proposition 1 appear
only forms of degree not greater than dωi. Moreover, it is easy to see (using Euler
identity) that the highest homogeneous term of ηi is equivalent in the Petrov module
to deg ωi
deg H dωi, see [18]. This together implies that B0 is lower triangular with prescribed
diagonal elements. From the same estimates of the Proposition 1 follows that entries
(B1)ij of the matrix B1 can be nonzero only if deg ωi − deg ωj ≥ deg H, so B1 is lower
triangular and, since maxij(deg ωi − deg ωj) = 2 deg H − 4 < 2 deg H, already B2
1 = 0.

Corollary 3 The matrix B0 + tB1 is invertible for all t.

5. Picard-Fuchs system can be non-Fuchsian

From the analysis above follows that all ﬁnite singular points of the system (4.2)
coincide with the critical values of H. Moreover, all ﬁnite singularities turn out
to be Fuchsian for Morse-plus H(x, y) (which, by deﬁnition, means that the matrix
(t − A)
−1(B0 + tB1) of coeﬃcients of the system of the Theorem 1 has poles of the
ﬁrst order). Indeed, the Picard-Fuchs system has a Fuchsian singularity at λi if and
only if the matrix (t − A)
−1 has a simple pole at λi (due to invertibility of B0 + tB1
for all t). This is equivalent to the diagonalizability of the matrix A, so is true for
Morse-plus Hamiltonian H(x, y).
For a general regular at inﬁnity H(x, y) the ﬁnite singular points can be non-
Fuchsian. Indeed, the matrix A is the matrix of multiplication by f in C[x, y]/ <
Hx, Hy >, and this ring is a direct sum over all critical points of H(x, y) of the
corresponding local rings ([4, Max Noether’s AF + BG Theorem]). It follows that A
is diagonalizable if and only if the operator of multiplication by H is diagonalizable
in each local ring. This is true if and only if the germ of H(x, y) is (equivalent to)
quasi-homogeneous, see [1], so fails in general.

Modules of Abelian integrals and Picard-Fuchs systems 10

Also, unless B1 = 0, the singular point at inﬁnity is non-Fuchsian. This is also
possible, see below an example.
It is easy to see that the Picard-Fuchs system of the Theorem 4 is equivalent to a
Fuchsian one. Indeed, due to the regularity at inﬁnity assumption the monodromy of
the irredundant system corresponding to a circle around inﬁnity is diagonalizable, so
this equivalence is a particular case of a positive solution (essentially due to Plemelj)
of the Riemann-Hilbert problem in the case of diagonalizability of one of the local
monodromies, see [2]. Moreover, in [12] it is proved, modulo a conjecture due to
Bolibruch, that this system is equivalent to a Fuchsian one for any H(x, y), even
degenerate ones. However, the equivalent system will not have the fairly simple form
of Theorem 4.
Here is an example of a Hamiltonian with a nonzero matrix B1.
Example. Consider the Hamiltonian H(x, y) = x
5 +y5 +x
2y2 +ax+by. For a suitable
choice of a, b this Hamiltonian is Morse-plus. As a basis of the quotient Λ2/dH ∧ Λ1

we take the forms dωij = x
iyjdx ∧ dy, 0 ≤ i, j ≤ 3. We will show that any form η
deﬁned by the decomposition

Hdω33 = dH ∧ η + ∑

0≤i,j≤3 aijdωij

is equivalent to 1
175 tω00 + ∑
0≤i,j≤3 βij ωij in the Petrov module corresponding to
H(x, y), with βij being constant (so the matrix B1 has a nonzero entry equal to 1
175 ).
Although η is deﬁned non-uniquely by the Gelfand-Leray formula above, its
Abelian integrals do (and therefore its class in the Petrov module). So we can use any
η we like. Applying the “division with remainder” algorithm of [18] we ﬁnd the ﬁrst
terms of a form η solving the equation above:

η = 1
5 (x
3y3(xdy − ydx) + ( 1
175 xy5dy − 6
175 x
5ydx) + η1 =

= x
3y3

5 (xdy − ydx) + y5 + x
5

175 xdy − d(x
6y)
175 + η1,

where by η1 we denote forms of degree less than 7. It is easy to see that in the
Petrov module the ﬁrst term is equivalent to 8
5 ω33 and the second term is equivalent
to 1
175 Hxdy + 1
175 (x
5 + y5 − H)xdy = t 1
175 xdy + η2. Since the degrees of both η1 and η2
are less than 7, the form η1 + η2 is equivalent in the C[t]-module of Abelian integrals
to a linear combination with constant coeﬃcients of forms ωij, by virtue of estimates
of the Corollary to Lemma 2.⊓⊔

References

[1] Arnold V I, Guse˘ın-Zade S M and Varchenko A N, Singularities of diﬀerentiable maps. Vol. II,
Monodromy and asymptotics of integrals, Birkh¨auser Boston, Boston MA, 1988.
[2] Arnold, V I and Ilyashenko Yu S, Ordinary Diﬀerential Equations, in the book: Anosov D V
and Arnold.V I (Eds.) Dynamical systems 1, Encyclopaedia Math. Sci., 1, Springer, Berlin,
1988.
[3] Brieskorn E, Die Monodromie der isolierten Singularit¨aten von Hyperﬂ¨aschen, Manuscripta
Math., 2 (1970), 103–161.
[4] P. Griﬃths and J. Harris, Principles of algebraic geometry, Wiley-Intersci., New York, 1978.
[5] Gavrilov L, Petrov modules and zeros of Abelian integrals, Bull. Sci. Math. 122 (1998), 571–584.
[6] ——, Abelian integrals related to Morse polynomials and perturbations of plane Hamiltonian
vector ﬁelds, Ann. Inst. Fourier 49 (1999), no. 2, 611–652.
[7] Givental A B, Sturm’s theorem for hyperelliptic integrals, (Russian) Algebra i Analiz 1 (1989),
no. 5, 95–102; translation in Leningrad Math. J. 1 no. 5, 1157–1163.

Modules of Abelian integrals and Picard-Fuchs systems 11

[8] A. A.Glutsuk and Yu. S. Ilyashenko, An estimate on the number of zeroes of Abelian integrals
for special Hamiltonians of arbitrary degree, preprint 2001, arXiv:math.DS/0112156v1.
[9] Horozov E and Iliev I D, Linear estimate for the number of zeros of Abelian integrals with cubic
Hamiltonians, Nonlinearity 11 (1998), no. 6, 1521–1537.
[10] Ilyashenko Yu, Appearance of limit cycles in perturbation of the equation dw
dz = − Rz
Rw where
R(z, w) is a polynomial, USSR Mat. Sb. (N.S.) 78 (1969), 360–373
[11] Ilyashenko Yu and Yakovenko S, Counting real zeros of analytic functions satisfying linear
ordinary diﬀerential equations, Journal of Diﬀerential equations 126 (1996), no. 1, 87-105.
[12] Kostov V, Gauss-Manin system of polynomials of two variables can be made Fuchsian, Geometry,
Integrability and Quantization, Sept 1-10, 1999 , Varna, Bulgaria.
[13] Khovanskii A, Real analytic manifolds with the property of ﬁniteness, and complex Abelian
integrals, Funktsional. Anal. i Prilozhen. 18 (1984), no. 2, 40–50 (Russian)
[14] Novikov D, Systems of linear ordinary diﬀerential equations with bounded coeﬃcients may have
very oscillating solutions, Proc. Amer. Math. Soc., 129 (2001), 3753-3755
[15] Novikov D and Yakovenko S, Tangential Hilbert problem for perturbations of hyperelliptic
Hamiltonian systems, Electronic Res. Announc. AMS, 5 (1999), 55–65
[16] ——, ——, Trajectories of polynomial vector ﬁelds and ascending chains of polynomial ideals,
Ann. Inst. Fourier 49 (1999), no. 2, 563–609.
[17] ——, ——, Meandering of trajectories of polynomial vector ﬁelds in the aﬃne n-space.
Proceedings of the Symposium on Planar Vector Fields (Lleida, 1996). Publ. Mat. 41 (1997),
no. 1, 223–242.
[18] ——,——, Redundant Picard–Fuchs system for Abelian integrals, to appear in Journal of
Diﬀerential Equations.
[19] Pham F,Singularit´es Des Syst`emes Diﬀ´erentiels De Gauss–Manin, Progress in Mathematics,
vol. 2, Birkh¨auser, Boston, 1979.
[20] Petrov G, Complex zeros of an elliptic integral, Funktsional. Anal. i Prilozhen. 21 (1987), no. 3,
87–88.
[21] Roussarie R, Bifurcation of planar vector ﬁelds and Hilbert’s sixteenth problem, Progr. Math.,
164, Birkh¨auser, Basel, 1998.
[22] Sebastiani M, Preuve d’un conjecture de Brieskorn, Manuscripta Math. 2 (1970), 301–308.
[23] de la Valle´e-Poussin, Sur l’´equation diﬀ´erentielle lin´eaire du second ordre. D´etermination d’une
int´egrale par deux valeurs assign´ees. Extension aux ´equations d’ordre n J. Math. Pure Appl.,
8 (1929), 125-144.
[24] Varchenko A, Estimation of the number of zeros of an Abelian integral depending on a parameter,
and limit cycles, Funktsional. Anal. i Prilozhen. 18 (1984), no. 2, 14–25 (Russian)
[25] Varchenko A, Critical values and the determinant of periods. (Russian) Uspekhi Mat. Nauk 44
(1989), no. 4(268), 235–236; translation in Russian Math. Surveys 44 (1989), no. 4, 209–210
