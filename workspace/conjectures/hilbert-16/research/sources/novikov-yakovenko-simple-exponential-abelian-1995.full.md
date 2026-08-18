<!-- source: https://www.numdam.org/item/10.5802/aif.1478.pdf | converted from PDF -->

ANNALES DE L’INSTITUT FOURIER

DMITRI NOVIKOV
SERGEI YAKOVENKO
Simple exponential estimate for the number of
real zeros of complete abelian integrals

Annales de l’institut Fourier, tome 45, no 4 (1995), p. 897-927

<http://www.numdam.org/item?id=AIF_1995__45_4_897_0>

© Annales de l’institut Fourier, 1995, tous droits réservés.

L’accès aux archives de la revue « Annales de l’institut Fourier »
(http://annalif.ujf-grenoble.fr/) implique l’accord avec les conditions gé-
nérales d’utilisation (http://www.numdam.org/conditions). Toute utilisa-
tion commerciale ou impression systématique est constitutive d’une in-
fraction pénale. Toute copie ou impression de ce ﬁchier doit conte-
nir la présente mention de copyright.

Article numérisé dans le cadre du programme
Numérisation de documents anciens mathématiques
http://www.numdam.org/

Ann. Inst. Fourier, Grenoble
45, 4 (1995), 897-927

SIMPLE EXPONENTIAL ESTIMATE FOR THE NUMBER
OF REAL ZEROS OF COMPLETE ABELIAN INTEGRALS

by D. NOVIKOV(1) and S. YAKOVENKO^^2)

1. ABELIAN INTEGRALS AND
POLYNOMIAL ENVELOPES
OF LINEAR ORDINARY DIFFERENTIAL EQUATIONS
WITH MEROMORPHIC COEFFICIENTS

One of the main results of this paper is an upper bound for the total
number of real isolated zeros of complete Abelian integrals, exponential
in the degree of the form (Theorem 1 below). This result improves a
previously obtained in [IY1] double exponential estimate for the number of
real isolated zeros on a positive distance from the singular locus. In fact,
the theorem on zeros of Abelian integrals is a particular case of a more
general result concerning the number of zeros in polynomial envelopes of
irreducible and essentially irreducible differential operators and equations
(see §1.3 below).

The first announcement of these and other results proved below
was in [NY]. In §1 all principal results are formulated and all necessary
definitions gathered, §2 explains connections between Abelian integrals and
polynomial envelopes: since the most part of preparatory work was already

ll ; The research was partially supported by the Minerva Foundation.
{2^ Incumbent of Elaine Blond Career Development Chair.
Key words'. Abelian integrals — Irreducible equations — Fuchsian singularities — Polyno-
mial envelopes.
Math. classification: 14K20 -  58F21 -  14D05.

898 D. NOVIKOV AND S. YAKOVENKO

done elsewhere [IY1], [IY2], [Y], we give only the principal definitions,
referring for motivations, examples and detailed explanations to the above
mentioned papers. The next section, §3, is the core of the paper. It contains
the notion of the Rolle index of a differential operator, and provides tools
for estimating this index explicitly. In §4, §5 the other results are proved,
and the concluding section §6 deals with possible generalizations.

1.1. Complete Abelian integrals: statement of the problem.

Let H € K[a;,2/] be a real polynomial in two variables, S^ (c R
the set of real critical values of ft, and t C R ^ E^ a regular value.
Each (real affine nonsingular) level curve (/^ = {H(x^y) = t} is a union
of connected components, some of them compact ovals </^i,..., (/?i,s, their
number s = s{t) in general depending on t.

If uj = P(x^ y) dx + Q(x^ y) dy is a differential 1-form with real
polynomial coefficients, then this form can be integrated along each oval
(pt ^, yielding a real multivalued function -fvy^.i
(1) J^:R\S^-.R , t^lH^t)=  (b a;, ?=!,...,5 .
^t. i
Obviously, this multivalued function allows for selection of continuous
branches over each interval from the domain R \  S^, and one may easily
see that in fact each continuous branch is real analytic. The collection of all
branches of the function (1) is called the complete Abelian integral of the
form cj over the level curves of the polynomial H. The problem of finding an
upper bound for the number of real isolated zeros of the Abelian integrals
was repeatedly posed since early seventies: we refer the reader to the paper
[IY1] where the principal references are given.

1.2. Exponential upper bound for the number of zeros of
complete Abelian integrals: remarks and discussion.

THEOREM 1. — Suppose that the polynomial H satisfies the fol-
lowing two properties:

(1) its complexification is a Morse function (i.e. all critical points of H ,
including the nonreal ones, are nondegenerate and all complex critical
values are pairwise distinct), and

ZEROS OF COMPLETE ABELIAN INTEGRALS 899

(2) each complexified level curve (pt after projective compactification
intersects transversally the projective line CP^ C CP2 at infinity.

Then there exists a constant c = c(H) < oo such that any real
branch of the complete Abelian integral may have at most exp(cdega;)
real isolated zeros onR\ S^, where the degree of the form deg uj is defined
as max(deg P, deg Q).

Remarks.

1. The second assumption on H is equivalent to saying that the
principal homogeneous part of H factors as a product of pairwise different
linear terms.

2. For any degree m  the set of all polynomials of degree ^ m, satisfying
the conditions of the theorem, is an open dense semialgebraic subset of the
linear space of all polynomials of degree ^ m. Thus Theorem 1 gives an
upper bound for a generic polynomial.

3. In fact, it follows from the proof of Theorem 1 that either all
branches of the integral are identically zero, or all of them may have only
isolated zeros on R.

4. The assertion of the theorem means that for any choice of the form
uj the number of different ovals on the plane B^^, over which the integral
ofuj may vanish, is at most exp(cdego;), unless this integral is zero for any
oval.
 5. In the previous publication [IY1], it was proved that for almost all
polynomials satisfying the above two conditions and for any compact subset
K <£ M \  S^ the number of real isolated zeros of the Abelian integral on
the compact K can be at most expexp^-H", K) degci;), where the constant
c\H^ K) depends not only on ft, but also on K. Thus Theorem 1 improves
the upper estimate, at the same time extending the domain of its validity,
as compared to [IY1].

Another important case is that of hyperelliptic curves. Recall that a
polynomial H is called hyperelliptic, if it has the form

(2) H(x,y)=y2-}-p(x), p € R[x}, degp ^ 5.

(for degp = 3,4 one has the elliptic case, completely studied by G. Petrov).
It is known (also due to Petrov) that if p is a Morse polynomial with all
critical points on the real axis, then the number of real isolated zeros of the
corresponding hyperelliptic integral can be at most 0(degc<;), see [Pe]. We
establish a weaker result, but drop away the assumption on critical points.

900 D. NOVIKOV AND S. YAKOVENKO

THEOREM 3/. — Assertion of Theorem 1 holds for a hyperelliptic
polynomial (2), provided that p(x) is a Morse polynomial in one variable.

1.3. Linear ordinary differential operators and equations.
Polynomial and rational envelopes.

Consider the field of (complex) rational functions k = C(t) and the
(noncommut alive) ring S) = k[9] of linear ordinary differential operators
with rational coefficients and the operation of composition (^1,1/2) i—^
Z/i o Z/2, also denoted by L\L^. An operator

n

(3) S) 3  £  =  ^  ^W\  £U =  do U^  +  0, U^- 1) +  • • • +  dn-i U' +  On U,
j=o

is called unitary^ if the principal coefficient ao(^) is equal to 1. We say that
L e D is real, if all coefficients of L belong to the subfield R{t) C k. We
denote by ord L the order of the operator L, that is, the degree of L in
9. Note that nonzero rational functions are units (invertible elements) of
the ring 1), so we will implicitly consider all multiplicative formulas in S)
modulo such units.

The singular locus S^ of a unitary operator L € S) is the union of
the polar loci of all its coefficients. A singular point t € S^ is said to be a
regular, or Fuchsian singularity^ if each coefficient aj(-) in (3) has the pole of
order at most j at that point (the Fuchs condition). It is natural to consider
the coefficients as functions on the Riemann sphere CP1 == C U {00}, in
which case t = oo can belong to the singular locus S^/, and the Fuchs
condition at infinity is to be verified in the chart T = 1/t. An operator is
said to be Fuchsian, if the Fuchs condition holds for all singular points on
CP1. A Fuchsian differential equation is the one of the form Lu == 0, where
the operator L becomes Fuchsian after multiplication by an appropriate
rational function 0 7^ y € k.

It is well known that any solution of the equation Lu =  0 can be
analytically continued along any path 7 avoiding the singular locus S^,
thus giving rise to an analytic multivalued function ramified over S^. If
L is a real operator and K C M \  Sj^ a real interval, then one may
always choose a fundamental system of solutions /i(^),..., fn(t)^ a string of
analytic functions, taking real values on K and linear independent over C.
Any other fundamental system of n solutions to the same equation can be

ZEROS OF COMPLETE ABELIAN INTEGRALS 901

obtained from the original one by a nondegenerate linear transformation.
All those simple results can be found in many textbooks, for example,
in [H].

Let d € N be a natural number. We define the polynomial envelope of
degree d of the equation Lu = 0 as the linear space of analytic multivalued
functions representable in the form

n
(4) ^  Pjk(t) /^ -1)^), pjk € C^], degp.k ^  ^
j,k=l

where /i,... , fn is a fundamental system of solutions for that equation.
Clearly, this definition does not depend neither on the choice of the
fundamental system of solutions, nor on the choice of branches of the
functions fj. Sometimes we speak about polynomial envelopes of operators
rather than those of differential equations, and use then the notation ^(.C)
for the corresponding linear space.

In the similar way we may introduce the rational envelope of degree
d of the same equation as the collection of functions representable in the
form similar to (4) but with rational rather then polynomial coefficients
pjk € k (recall that the degree of a rational function is the total number of
its poles, counted with multiplicities, including the pole at t =  oo). Note
that rational envelopes of any finite degree d < oo are not linear spaces,
and in general do depend on the choice of the fundamental solutions fj
and their branches. The notation used for rational envelopes is 9^(^)5 and
W  = U W)-
O^o
 1.4. Irreducible case.

Let a ^ S^ be a nonsingular point, and 7 € 7Ti(C \  S^,a) any
closed loop (more precisely, the homotopy class of some closed loop with the
vertex at a). Choose any fundamental system of solutions f = (/i,... , fn)
considered as a row vector. Then after the analytic continuation over 7 the
vector function f(t) undergoes a linear transformation:

n
A^f =  f M^ <=^ A^/, = ^  fk^kr
k=l
Here A/y stands for the operator of analytic continuation along 7, and
M^ is a square (n x n)-matrix with constant complex entries m^;^-.

902 D. NOVIKOV AND S. YAKOVENKO

The correspondence 71-1 (C Y EL, a) —>• GL(n,C), 7 i—^ M^1, is a linear
representation of the fundamental group, and the image of the fundamental
group is called the monodromy group of the operator L (or the equation
Lu=0).

The operator L G 2) is called irreducible, if the monodromy group of
this operator is irreducible, i.e. the operators M^ have no common invariant
nontrivial subspace. For Fuchsian operators (equations) an equivalent
algebraic formulation can be given as follows: L is irreducible if and only
if it admits no nontrivial factorization L = L\L^ in the ring 2) (as usual,
modulo the multiplicative subgroup of units k* C £)). To avoid confusion,
we refer to this property as indecomposability of L ml).

Indeed, if the operator admits a factorization as above, then the fun-
damental system of solutions to the equation L^u •== 0 would generate an
invariant linear subspace for all monodromy operators. Conversely, if the
monodromy group is reducible, and /i,... , /^  0 < k < n, span the corre-
sponding invariant subspace, then by the classical Riemann theorem one
can construct an operator L^ G S) of order A;, satisfied by /i,... , fjc. But
then one can easily show that L is right divisible by Z/2, using the division
algorithm from [In]: L = I/iZ/2. However, if we do not assume the Fuchsian
property of L, then only the implication "irreducibility ==> indecompos-
ability" remains, since the coefficients of the operator L^ will not in general
be rational functions.

The principal result concerning zeros in polynomial envelopes, follows.

THEOREM 2. — Let L € 1) be a real irreducible operator, and
K (c R \  EL a compact segment without singular points of L.

Then there exists a finite number c =  c(-L, K) <  oo such that any
function u from the polynomial envelope of degree d of the operator L, real
on K, may have at most exp(cd) isolated zeros on that segment:

limsup {d-1 • InNK(f) : /  € V^)}  = c(K, L) < oo.
d—>oo

COROLLARY. — The same exponential upper bound for the number
of isolated real zeros holds also for all functions from the rational envelope
9^ (£) of degreed.

Indeed, by getting rid of all denominators any function from the ra-
tional d-envelope may be transformed into an element from the polynomial
envelope of order at most (n2 — l)d, n =  ordL.

ZEROS OF COMPLETE ABELIAN INTEGRALS 903

Remark. — In Theorem 2 no assumption on the nature of the sin-
gularities of the equation is made; it is the global condition of irreducibility
which is crucial for this result. However, we do not know whether the ex-
ponential estimate can be further improved.

Note. — A confusion between closely related notions of irreducibil-
ity and indecomposability occurred in [NY]. In all formulations of theorems
from that paper the irreducibility assumption is to be understood in terms
of the monodromy group (and not as indecomposability). However, the
difference disappears if only the Fuchsian case is considered.

1.5. Regular singularities at the endpoints
and the real spectrum condition.

Theorem 2 gives an upper estimate for the number of zeros for
polynomial envelopes on a compact segment K. We extend now this result
for semiintervals with singular endpoints. Let

L =  f1 9 n +  t^a^t)  971-1 +  ... +  tan-i(t)0 +  an(t) C 2)

be a differential operator with a Puchsian singularity at t =  0. Using the
Euler transformation

x-i =n, x^ =t9xi, xs =t9x^, ..., Xn =t9xn-i,

one may transform the equation Lu = 0 into the system of first order linear
differential equations
tx=A(t)x, xe^, te(C\o),

with the matrix function A(t) =  AQ + t Ai + t2 A^ +  • • • holomorphic at
t = 0 and real on the real axis, if the operator L was real.

DEFINITION. — The spectrum of the Fuchsian singularity is the
spectrum of the associated residue matrix A(0) = Ao.

One can easily show that the spectrum of the singularity consists of
roots of the so called indicial equation

A(A -  1)(A -  2).. . (A -  n + 1) +ai(0)A(A -  1). •. (A -  n + 2) + . •.

+a^-2(0)A(A -  1) + a^-i (0)A + a^(0) = 0.

Moreover, the equation Lu =  0 may have a solution of the form u(t) =
t x h(t) with h(t) holomorphic at t = 0 only if A is an element from the
spectrum (a straightforward computation).

904 D. NOVIKOV AND S. YAKOVENKO

DEFINITION. — A point a € S^ is the real Fuchsian singularity for
the real operator LeD,ifa€M , the Fuchsian condition holds at a and
the spectrum of the singular point entirely belongs to the real axis.

Remark. — The above definitions make sense also for the point
t =  oo after the change of time 11—>-1~
1
.

THEOREM 3. — If L 6 S) is a real irreducible operator, a € SL a
real Fuchsian singularity for L and K = (a, f3} C R\^L  a semiinterval
without singular points, then the assertion of Theorem 2 remains valid
onK.

COROLLARY. — Iffor a real irreducible operator L the locus MDS^
consists of real Fuchsian singularities only (including the point t == oo), then
there exists a constant C =  C{L) depending only on L, such that any real
branch of any function from the polynomial d-envelope may have at most
exp(Cd) isolated zeros.

Indeed, in this case one may enumerate as a\,..., a 5 the points
of the locus YJL H 3^ choose once and forever the points /3i so that

/3o < ai < /?i < • • • < (3s-i <  Ois <  Ps and apply Theorem 2 to each of
the semiintervals (—00, /3o}, [/^-i,o^), (o^,/^] and [/3s, +00). Then taking
the sum of the corresponding upper bounds, one obtains an upper estimate
valid for on the whole real axis (one may count or not count the points o^,
this would not affect the exponential bound).

Remark. — In Theorem 3 we do not require the singular points
outside the real axis be real Fuchsian or even just Fuchsian.

1.6. Relaxing the irreducibility condition.

If the irreducibility assumption fails, then one can construct an
equation with meromorphic coefficients and an arbitrarily rapidly growing
number of zeros in polynomial envelopes [IY1]. However, at least partially
this condition of irreducibility can be relaxed.

DEFINITION. — A linear operator L C S) is essentially irreducible
with the irreducible core L^ G S), if L = L^P\P^-' • P^, where:

(1) Pi 6 S) are real differential operators of order 1, and

ZEROS OF COMPLETE ABELIAN INTEGRALS 905

(2) L^ is a real irreducible operator (of any order).

Remarks.

1. An equivalent definition in terms of the monodromy group is as
follows: the operator is essentially irreducible, if in the linear n-dimensional
(over C) space A of solutions of the equation Lu =  0 a chain of subspaces
(a flag) A^, i = 0,1,... , k +1, can be chosen,

{0} == A^+i C Afe C Afc-i C • • • C Ai C Ao = A,

such that:

(1) each subspace A% is invariant by all monodromy operators M/y,

(2) dimA^_i = dimA^ + 1 for all i = 1,... ,A: (we do not require that
dimAo = dirnAi + 1),

(3) the induced quotient representation in Ao/Ai is irreducible (the
other induced one-dimensional quotient representations in A^-i/A^,
z=l,...,fc+l , are obviously irreducible),

(4) Ai is the null space for a Fuchsian operator.

The equivalence of the two definitions is established using the Rie-
mann theorem: A^ is the null space for the composition P^P^+i ' " Pk-

2. If the initial operator L is Fuchsian, then the last condition in
the above list is automatically satisfied. In this case we can also replace
irreducibility of L^ by indecomposability, so finally the definition of almost
irreducibility can be formulated in terms of orders of factors in the
indecomposable factorization of L in the ring 2).

3. The essential irreducibility condition being satisfied, one may
always choose a fundamental system of solutions f\,..., fn for the equation
Lu = 0 in such a way that the last n  — i functions will constitute a basis
for Ai. Moreover, for any real interval free from singularities of L, the
functions fi may be chosen real on that interval. It is this form of the
essential irreducibility assumption, which will be used below.

4. In [Y] a weaker concept appeared, almost irreducibility, which is
a particular case of essential irreducibility. The monodromy group is said
almost irreducible, if there exists an subspace Afriv C A, on which all
monodromy operators are identical (and hence this subspace is invariant),
but the quotient representation in A/Afriv is already irreducible. Obviously,
one can choose any ascending chain of subspaces A^ C Afriv to show that
almost irreducibility implies essential irreducibility.

906 D. NOVIKOV AND S. YAKOVENKO

THEOREM 4. — If L is a real essentially irreducible operator and
K (^ R \  EL is a compact segment without singular points, then the
assertion of Theorem 2 is valid for L.

THEOREM 5. — IfK=  (a, /?] C R is a semiinterval with a singular
endpoint (as in Theorem 3), and L is an essentially irreducible operator
with the real Fuchsian singularity at t = a, then the assertion of Theorem 2
is valid for L on K.

2. FROM ABELIAN INTEGRALS TO
POLYNOMIAL ENVELOPES

In this section we reduce the problem on estimating the number of
zeros of Abelian integat for polynomial envelopes (the proposition below
establishes the implication "Theorem 5 ===^ Theorem 1"). Except for
Lemma 1, the exposition here reproduces that from [Y] and [IY1].

PROPOSITION. — For any real polynomial H satisfying the assump-
tions of Theorem 1, one may construct a Fuchsian operator L =  LH de-
pending only on H, with the following properties:

(1) L is a real Fuchsian operator;

(2) all singular points ofL have real spectrum;

(3) the monodromy group of L is almost irreducible (hence essentially
irreducible);

(4) for any polynomial form uj the complete Abelian integral of a; over
the level curves H = const belongs to the rational d-envelope of L
"••"-Sih0-^

The same result is valid for a hyperelliptic polynomial H = y2 -{-p(x)
satisfying the assumptions of Theorem 1'.

The rest of this section contains the proof of this assertion. Starting
from §3, we discuss only polynomial envelopes of linear operators.

ZEROS OF COMPLETE ABELIAN INTEGRALS 907

2.1. The monodromy group of the Gauss-Manin connection.

We consider first the case of polynomials described in Theorem 1.
A polynomial map H : C2 -> C1 defines a topologically locally trivial
bundle over the set of (complex) regular values C \  E^-, provided that all
level curves intersect transversally the infinite line after compactification.
The fibers of this bundle are nonsingular affine algebraic curves (^ =
[H =  t} C C2, hence an induced vector bundle with fibers -Hi((^, C) c± C
71,
n  == 2<7+ s — 1, is well defined and can be endowed with a locally flat
connection, called Gauss-Manin connection (here g is the genus of the
projective compactification of y?f, and s = degH is the number of points
at infinity). The result of the parallel translation in the sense of the Gauss-
Manin connection defines a linear representation of the fundamental group

Ti-i (C ^ E^,'); after choosing an arbitrary basis ci,...,c ^ in some fixed
fiber ffi ((pto ? Q  ? ^ne result of continuation of the row vector c = (ci,... , Cn)
along an arbitrary loop 7 is the row vector c-M^. Since any polynomial form
uj restricted on any y^ is holomorphic, it follows that the row vector function
l(t) = (Ji(^),..., In(t)) has the same monodromy group independently of
the choice of the form uj: A^I = I'M^. Moreover, if we consider the Jacobian
matrix \(t) built from the functions Ij(t) and their derivatives in t up to
the order n— 1 =2g + s — 2, then the monodromy of this function will be
the same: A^l(^) = \(t) ' M^. In other words, the monodromy group of any
complete Abelian integral is determined by the topology of the Hamiltonian
only, if we fix a framing of the bundle.

The representation 7 i—^ M/y1 possesses an additional symmetry due
to the fact that H is a polynomial with real coefficients. Choose the base
point to on the real axis. Then, since the critical values of H are symmetric
with respect to the real axis, the fundamental group 71-1 (C \  E^,^o)
admits an involution 7 i—^ ^ (the mirror symmetry in the real axis),
induced by the standard involution 11-^ t. At the same time the standard
involution (x,y) \-^ (x,y ) induces the involution on the homology level,
r : H\{^t,C) —>• H^ (<^,C), and without loss of generality we may assume
that the basis cj C Jfi(y?io,C) was chosen as r-(anti)real: r(cj) =  ±Cj.
Then one can easily see that the representation 7 i—^ M^
1 is r-symmetric:
My=M^ .

The reducibility properties of the representation 7 \—> M~1 were
established in [Y]: it was shown that if the Hamiltonian satisfies the
conditions of Theorem 1, then this representation is almost irreducible in
the sense explained in §1.6. Moreover, it is known that in this case the

908 D. NOVIKOV AND S. YAKOVENKO

monodromy operators corresponding to small loops around each critical
value of H, have all eigenvalues equal to 1. This guarantees that the
spectrum of all singularities belongs to Z, see below §4.1.

2.2. Lemma on nondegenerate realization.

Our local goal is to establish the existence of a differential operator
of order exactly equal to n with the prescribed monodromy group.

LEMMA 1. — Any r-symmetric n-dimensional monodromy group
is a monodromy group of a real Fuchsian operator of order n: there exists
an operator L  and a fundamental system of solutions f  =  (/i,..., fn) such
that A^ f = f  • M^.

Proof. — By the classical Plemelj-Rohrl theorem [AI], one may
always construct a multivalued almost everywhere nondegenerate analytic
matrix function X(^) ramified over S, in such a way that A^X(^) =
X(^) • M^. Moreover, all points of S  will be regular singularities for X(^),
X-1^): 11X^)11 = 0(\t -  0]-^) for some C < oo, as t tends to a point
a € S, remaining in any sector with the vertex at a.

We construct the vector function f from the matrix function X in
two steps. First we modify X(^) to become real-valued on the real segment
K containing the real base point to. Note that if the monodromy is r-
symmetric, then the matrix function X'(^) =  X(?), t = r(t), will also have
the same monodromy, hence the two functions

ReX(^) = J(X(^) 4-xt(^)), ImX(^) =  —^(X(t)-X+(^)) ,

will also realize the same monodromy. Besides, both functions are real-
valued on K and X = ReX + ^/—llmX. Consider now the function
Xz = ReX + zImX: the determinant of this function is a polynomial
in z, which is not identically zero, since detX^(t) is not identically zero
for z == \/—1- Thus there must exist a real z for which the matrix Xz is
nondegenerate almost everywhere on K. Thus without loss of generality
one may assume X being real on K from the very beginning.

We will further modify the matrix function X(^) in such a way
that the first row of this matrix will contain linear independent entries,
preserving the monodromy. Without loss of generality we may assume

ZEROS OF COMPLETE ABELIAN INTEGRALS 909

that detX(^o) ¥- ^  and X-1^) = Z(t) + 0(\t —to^), where Z(^) is a
polynomial matrix function with real matrix coefficients. Then 7.(t)X(t) =
E+O^t-to^). Take the row vector function b(t) =  (1, t-to,..., (t-to)'1"1)
and consider the product f(t) = b(^) - Z(^) • X(^) which has the same
monodromy factors M^, since both Z and b are polynomial. Clearly,
fj^(t) = (t — to)k~l -+- 0(\t — ^ol^)? hence the functions fk are linear
independent (their Wronski determinant is nonzero at t =  to), real on some
segment of the real axis and have at most regular singularities at all points
of S. Now it follows from the classical Riemann-Fuchs theorem that the
tuple f is a fundamental system of solutions for a certain Fuchsian equation
with coefficients real on some segment of the real axis. But being rational,
these coefficients must be necessarily real everywhere on M (outside their
polar locus), n

Remark. — In [Y] the existence of the tuple f was proved by finding
a polynomial form ^  with linear independent integrals. Such a form was
proved to exist for almost all Hamiltonians satisfying the conditions of
Theorem 1. In that case one has an explicit estimate for the term 0^(1)
in the degree of the envelope.

2.3. Proof of the proposition.

Let \(t) be the Jacobian matrix for the Abelian integrals of the
form uj over the cycles Cj(t) constituting a real basis in the homology
space ffi((^f,C). Fix an arbitrary tuple of linear independent analytic
functions f(t) == (/i(^),..., fn(t)) with the same monodromy matrices M^
constructed in Lemma 1, and let P{t) stand for the Jacobian matrix of this
tuple. Then one can easily see that the matrix ratio R{t) = \(t) • F"^) is
a single-valued analytic matrix function. Having only regular singularities,
this matrix function must be rational, and the arguments given in [Y] and
similar to those from [M] give an upper estimate for the degrees of rational

entries of R(t) in the form - eg^- +0(1). The identity \(t) = R(t)F(t) gives
deg-a
the required representation. D

2.4. The hyperelliptic case.

The same arguments establish also the representation of hyperelliptic
integrals in the form of rational envelopes. The only thing which needs

910  D. NOVIKOV AND S. YAKOVENKO

to be verified is the essential irreducibility condition. In [Y] it is shown
that this irreducibility can be deduced from the fact that all vanishing
cycles on the fibers (pt can be chosen and ordered in such a way that the
intersection index would be =L1 for any two subsequent cycles. The latter
assumption is completely evident if the polynomial p has all real roots: then
its critical points are all real and alternate between maxima and minima,
and this natural order transferred onto the vanishing cycles, satisfies the
above requirement: each real vanishing cycle (corresponding to a maximum)
intersects two neighboring imaginary cycles vanishing at the two minima,
with the coefficients ±1 depending on the orientation of the imaginary
cycles.

The general case can be reduced to the above particular one by argu-
ments of connectedness: all (complex) Morse polynomials in one variable
constitute a connected subset of the (complex) linear space of polynomi-
als of the given degree in one variable, while the monodromy group (more
precisely, the matrices M/y) are locally constant. Thus the assertion of the
Proposition holds also for hyperelliptic Morse Hamiltonians.

Remark. — In general, the Fuchsian operator will have singularities
not only on S: if the Jacobian matrix F degenerates at a certain point
t, then the coefficients of the operator L may have a pole at that point.
However, all solutions of the equation Lu = 0 extend holomorphically at
that point: such singularities are called apparent, they have trivial local
monodromy and their appearance will not affect our constructions below.

3. POLYNOMIAL ENVELOPE OF AN IRREDUCIBLE
FUCHSIAN EQUATION

In this section we prove Theorem 2, the core result of the paper.

3.1. Frobenius-Schlesinger-Polya formula.

Let L be an arbitrary linear ordinary differential operator, ord L =  n,
and /i,... , fn is a fundamental system of solutions of the equation Lu = 0.
Introduce the functions Wk{t) as follows: Wo(t) = 1, W^{t) = /i(t),

ZEROS OF COMPLETE ABELIAN INTEGRALS 911

W)  = fi(t)f^(t) -  f[(t)f2(t) and in general Wk(t) for k =  1,... ,n is
the Wronski determinant of the first k functions /i,... , fk:

r A h  •• • A
/{ /2 •• • /,
Wk(t)=det
 .(fc-i) .(fc-i) .(fc-i)
L Jl J2 ' " J k J

It turns out that the differential operator L admits "factorization" in terms
of the functions Wk.

LEM^A 2 (Frobenius-Schlesinger-Polya). — IfL is a unitary oper-
ator, L = Q
71 + • • •, then

f5) L-  wn  Q
 w ^- 1  8 w<ln-tl ^ ^ w ^  /) wo
(5 ) ^-^^^•W^^' 9 '^^^* 9 ''' 9 *^ ^

(composition of operators).

Proof. — We follow [In], §5.21, adding the proof for the formula
given in the footnote.

Introduce the auxiliary differential operators Lk by letting L^u being
equal to the Wronski determinant of the functions /i,... ,/fc,^ (in the
specified order). Clearly, Lj, =Wk • 9k -}-'" . Therefore L = W^Ln, since
both parts of the equality are unitary differential operators annulated by
n linear independent functions /i,... , /n-

First we establish the operatorial identity

(c\\ ^  1 T ^k-i  T(6) Q.^.L^=-^.L,.

Indeed, both operators are of order k, and the leading coefficients are the
Wk-i
same, being equal to ———. Hence the difference between them is an
Wk
operator of order at most k -  1. On the other hand, both operators are
annulated by the k linear independent functions /I,...,/A- for the first
k — 1 functions this is evident, and on fk the left hand side part is zero,
since Lk-ifk = Wk' Thus we conclude that the two parts coincide. The
formula (6) remains valid for k = 1, if we put formally LQ = id.

912 D. NOVIKOV AN D S. YAKOVENKO

Now we can iterate the formula (6) as follows:

L-W^L  -  wn  w "- 1 / - wn  » w-i  Twn ^-w^'^vr^^wn-,'
9'^ •
£
"-
1

=(^_.g.W^\
\Wn.,  Wn  ) ^-l^n-1

=( W ^.Q. W ^\.( W ^  Q w ^}  w-lr
\Wn., Wn ) [w^' 9 "^)'^-^-^---

=( w ^-.9. w ^\.( w ^l.9. w ^l\  ( w ^  Q w ^  w-lr
{W^  c' Wn ) [Wn.,  d  Wn-J"\W,' Q •W[)' wo  Lo -

D

Remark 1. — The representation (5) was first established by
G. Frobenius [F]; a simplified proof appeared in the paper of G. Polya
[P6] who refers to the handbook of L. Schlesinger [Sch]. E. Ince [In] gives
an independent proof without referring to Polya or Schlesinger. A lengthy
computational proof can be found in [H], Ch. IV, §8(ix). Our proof seems
to be the shortest of all and the most computation-avoiding.

Remark 2. — Decomposition (5) holds even for irreducible opera-
tors, since the Wronskians Wj, are in general transcendental rather than
rational functions.

3.2. Rolle index of a differential operator.

If L is a unitary differential operator with the coefficients which are
real analytic on some segment K C M, then the fundamental system of
solutions /i,... , fn can be also chosen real on K, hence all Wronskians Wj,
will be real analytic on K as well.

Consider the nonhomogeneous differential equation

(7) Lu =  h, h =  h(t), te K

with the right hand side part h real analytic on K. Let /  = f(t) be any
solution of (7). Our goal is now to compare the number of isolated zeros
of h and /  on K. The simplest result in this spirit is the classical Rolle
theorem. Denote by NK^) the number of real isolated zeros of a function
^ real analytic on K, counted with their multiplicities. According to this
definition, NK^) =  0 if (p = 0 on K.

ZEROS OF COMPLETE ABELIAN INTEGRALS 913

ROLLE THEOREM. — IfL =  9, then for any real segment K = [a, f3}

NK(U) ^  NK(LU) +  1. D

Remark. — In fact, the Rolle theorem deals with zeros counted
without multiplicities, saying that between any two zeros of a differentiable
function there must be at least one zero of its derivative. The general case is
reduced to this particular one without any difficulties: if to < ti <  '' ' < ts
are real zeros of u of multiplicities 1 + VQ, 1 + i/i,... , 1 + y^ (^ ^ 0), then
the derivative 9u will have zeros of order vj at tj (if ^  > 0), and also on
any of s segments (^,^+1) there must be at least one zero. Thus

s s
NK(U) =  ^( 1  +  Vj) =  1  +  ^  V, +  S <  1  +  NK{QU).
j=0 j=0
The case u =  const is trivial.

A simple generalization of this result is due to G. Polya: it concerns
differential equations with the "Property W": the latter means that the
equation possesses a fundamental system of solutions such that all Wron-
skians Wk are nonvanishing on K.

POLYA THEOREM (1923), see [P6], Theorem I*. — If the fundamen-
tal system of real analytic solutions /i,... , fn for the real equation Lu = 0
is such that Wk -^ 0 on K for all k =  1,..., n =  ord L, then

NK{U} <^NK(Lu)-}-n.

Proof. — Assume that N^^u) ^ NK^LU} + n + 1. By virtue of the
decomposition (5), L is the composition of 2n+l operators of differentiation
and multiplication by nonvanishing real analytic functions (since the de-
nominators are nonvanishing). By Rolle theorem, each differentiation may
decrease the number of real isolated zeros counted with their multiplicities
at most by 1, while each multiplication cannot change the number of zeros.
Since the number of derivations is n, the number of isolated zeros counted
with their multiplicities, will be decreased at most by n, being thus at least
NK^LU) + 1, which contradicts the assumptions. If Lu = 0, then in fact
one can show that NK (u) ^ n — 1. D

If we allow for zeros of the Wronskians, then two additional circum-
stances must be taken into consideration: the operators of multiplication
may cancel zeros corresponding to roots of the denominators, and in gen-
eral these multiplications will take analytic functions into functions that

914 D. NOVIKOV AND S. YAKOVENKO

are only meromorphic (with poles), thus making impossible the straight-
forward application of the Rolle theorem. However, knowing the number
of zeros of Wronskians allows for establishing a result similar to the Polya
theorem.

THEOREM 6. — Let L be a unitary differential operator of order n
with coefficients that are real analytic on a closed real segment K C R\S^ .
Then there exists a finite number p = p(L, K), such that
NK(U)<^NK{LU)-^P(L,K).

for any real analytic function u.

Moreover, if K is an arbitrary connected subset of R, /i,... , fn is
a fundamental system of real analytic on K solutions and Wk are the
corresponding Wronskians with
Np^Wk) =  Vk < oo, k = 1,..., n,
then n
p(L, K) <  (n -+- 2)v -  2, v =  1 + ^  ^ .
k=l

Proof. — We start with the second assertion of the theorem. Con-
struct the sequence of operators

RO  =  TrT- ? D\=Q'RQ^
W\
W 2
Rl ^WW' 0^  D^O'R^WQ W^

w2 i
Rn-1  -. n " 1  'Pn-1 , Dn=0'Rn-^
WnWn-2
W
D _ ' r n n  — Trin  — ———  ' J^n — 1J'
Wn-1
Let u be analytic on a connected set K. Then any of the functions RkU
or DjcU will have at most v = 1 + ^  ^k intervals of continuity, since the
k
total number of poles of all denominators (without multiplicities) is at most
Z^fc.
k Thus any of the d differentiations can decrease the number of isolated
zeros (with multiplicities) by at most ^, while each multiplication can
eliminate at most Vk-\-i + ^k-i zeros (again counted with multiplicities):
NK(Dku) > NK(Rk-iu) -  v,

NK(Rku) > NK(Df,u) -  Vk-i -  ^+1.

ZEROS OF COMPLETE ABELIAN INTEGRALS 915

Adding these inequalities, we arrive to the final inequality
n- l
NK(LU) ^  NK(U) -  nv -  Vn -  2 ^  ^  ^ NK{U} -  {n + 2)v + 2.
k=l

Now return to the first part: if K is a compact segment without
singularities, then for any choice of a fundamental system of solutions, the
Wronskians Wk will be real analytic, hence the number of their zeros will
be finite. Thus we have ^  < oo, and the above arguments prove finiteness
of p. D

Note that for v^ =  0 the assertion of the theorem coincides with
the Polya inequality. If instead of analytic function u we would start with
a meromorphic function with p poles, then the corresponding inequality
would take the form

NKW ^  NK(LU) + v(n 4- 2) -  2 + np.

The inequality obtained in Theorem 6, makes meaningful the follow-
ing notion of the Rolle index of a linear differential operator.

DEFINITION. — The Rolle index of a linear operator L on a
connected real set K without singularities, is the supremum

sup (NK^U) -  NK(LU)) ,
u
taken over all functions real analytic on K and having at most a finite
number of isolated zeros.

Remark. — The Rolle index is also well defined if the equation
Lu =  0 has only apparent singularities on K^ that is, singular points at
which all solutions are in fact analytic (see the last remark in §2).

We will never deal with the Rolle index itself, but rather with upper
estimates for it.
 3.3. Generalized Jensen inequality.

Theorem 6 reduces the question about the number of isolated zeros of
an arbitrary solution for a linear equation to that about the number of zeros
of the Wronskians Wk. It turns out that the latter problem admits a natural
solution in the complex domain. The result below is a generalization of the

916  D. NOVIKOV AND S. YAKOVENKO

classical Jensen formula, which gives an upper estimate for the number
of isolated zeros of an analytic function in terms of its growth in the gap
between two nested sets.

Let U C C be an open connected and simply connected set (a
topological open disk) with a smooth boundary F, and K (s U a compact
subset of U (this means that the distance from K to F is strictly positive).
For an arbitrary function /  holomorphic in a neighborhood of the closure
U one may define two numbers,

M(/)=max|/(t)|, m(/)=max|/(t)|,
t(EKt^U
which are always related by the inequality m ^ M, and the equality is
possible if and only if /  = const.

LEMMA 3 [IY2]. — There exists a finite constant 7 = 7(KT, U)
depending only on the relative position of the two sets K and U, such that
for any f  analytic in a neighborhood ofU, the number A^<(/) of complex
isolated zeros of f  on K admits an upper estimate
A^OX^^-ln^ .  a
"H./ )

Remark. — If /  = 0, then it is convenient to define M(/)/m(/) = 1
as for any other constant: then the above inequality will remain valid in
this exceptional case as well.

3.4. Two-sided estimates for the Wronskians.

Let U C C be any open connected domain (not necessarily simply
connected) and A(U) the ring of functions analytic (single-valued) in
U. Consider a unitary linear operator L e S)u = A(U)[9] of order
n with coefficients in A{U). In the same way as for operators with
rational coefficients, the monodromy group of the equation Lu =  0 can
be introduced and the canonical representation 7Ti(L^o)
 —)> GL(n,C),
7 \—^ M~ 1 defined (here to is an arbitrary point from U). If L e S) is
an operator with rational coefficients, then one may put U =  C \  E^.
Denote by z : D —> U the universal covering (in most cases the universal
covering space will be the unit disk).

Let /i,... , fn be a fundamental system of solutions for the equation
Lu =  0, and d G N a natural number. The polynomial envelope of the

ZEROS OF COMPLETE ABELIAN INTEGRALS 917

equation Lu = 0 is defined as the linear space of functions spanned by the
monomials
Fajk(t) = r  /^- 1), a = 0,1,... ,d, j,k = 1,... ,n.

As in the case of L e 2), this space is well defined and can be considered
as a subspace of the space of analytic functions on D (since solutions are
in general multivalued on U).

We arrange the monomials Fajk lexicographically according to the
ordering of indices as follows: k is the first letter, a the second and j the
third one. Thus all n 2^  + 1) monomials will be numbered sequentially,
Fajk receiving the number

(8) /3=/3(a,fc,j;d)=(A;-l)(d+l)n+an+j.

Let Wp(t) be the Wronskian of the first f3 monomials. From now on we fix
L and the system fj and investigate the behavior of Wronskians in their
dependence on the large natural parameter d.

Remark. — The notation W^ is somewhat ambiguous, since the
meaning of this symbol depends on the choice of d'. if we replace d by
d 4- 1, then all Wp will be changed starting from (3 =  n(d + 1). Thus a
more accurate notation would be W^^t)' However, we will not use this
cumbersome construction.

As before, we say that an operator L e S).u is irreducible if the
representation 7 ^  M^"
1 is irreducible.

LEMMA 4 [IY1]. — Let L € ®u be an irreducible differential
operator and D (c= D an arbitrary compact subset of the universal covering.
Denote

A(d,D) =max max|H^(t(z))|, B(d,D) = min max|^(t(^))|,
(3 z^D  (3 z^D

where the exterior maximum and minimum are taken over all (3 =
l,...,n2(d+l) .

Then A(d,D) ^ expexpO^(lnd), as d —> oo,

and if D has a nonempty interior, then also

B(d,D)~1 ^ expexpOL,D{d), as d —^ oo,

where the terms OL,D(^) grow at most linearly in d, with the slope
depending only on the choice of the solutions fj and the compact D. D

918  D. NOVIKOV AND S. YAKOVENKO

Remark. — This statement is a quantitative generalization of the
fact that solutions of an irreducible equation are linear independent over the
field of rational functions. No assumption ofrealness is required whatsoever.

3.5. Proof of Theorem 2.

Let now L e S) be as before a real irreducible differential operator
with rational coefficients. Take any compact segment K (s M\S ^ free from
singularities of the irreducible equation Lu = 0. Let K^ <s C be the closure
of some open neighborhood of K and U another open connected simply
connected set containing K^ strictly inside. From Lemma 4 it follows that
each Wronskian W^(t) for all f3 =  1,..., n 2^  + 1) admits the estimate

max|W3(t)| ^ A{d,U) ^ expexpOr jj(\nd),
t(EU
max|lV^)| ^ B(d,K^) ^  exp (-expO^,^^)),
te-fCi,
which by Lemma 3 implies that the number of complex isolated zeros of
Wp in K^ (and hence the number of real isolated zeros on K) can be at
most exponential:

NK{WO) ^ expOL,K,K^u(d) = expOL,K{d)

(we fix the choice of K^ and U together with that of K).

By Theorem 6, the number of zeros of any linear combination of the
monomials Fajk is at most exponential in d as well. But this is exactly the
result we need, since the polynomial d-envelope of Lu = 0 consists of linear
combinations of the monomials, n

Remark. — In fact, we proved that for the differential operator Ld
annulating the polynomial d-envelope of an irreducible real operator L, the
Rolle index grows at most exponentially in d on any real segment K free
from singular points of L. Note that the operator Ld may have singularities
on K, but all these singularities will be apparent: all solutions of L^u == 0
extend analytically at those points.

4. SINGULAR ENDPOINTS

Assume that L € S) is a real operator with a real Fuchsian singularity
at t = 0, and K =  (0,^*] is a real semiinterval without singularities:

ZEROS OF COMPLETE ABELIAN INTEGRALS 919

K D S^ = 0. In this section we extend the exponential upper estimate
for the number of zeros in polynomial envelopes to cover also such case.

4.1. Local properties of the Wronskians and
a special lexicographical ordering.

The lexicographical ordering (8) of the monomials Fajk was deter-
mined by the ordering of the functions fj constituting the fundamental
system of solutions. Fbr the upper/lower estimates established in Lemma 4,
the ordering of the functions fj was inessential. But if we want to analyze
a small neighborhood of the singularity at t =  0, then this ordering must
be chosen in a specific way.

LEMMA 5. — If  t =  0 is a real Fuchsian singularity for a real differ-
ential equation Lu =  0, then the monodromy operator Ao corresponding
to a small loop around t =  0, can be put into the upper triangular form
by a real linear transformation: this means that a fundamental system of
solutions fj can be chosen so that

(1) fj(t) are real on the segment K, and

(2) Ao/,=E"i,Jz.
^j

(3) vrijj =  exp27r\/—lA^, where \i are points of the spectrum, repetitions
allowed.

Remark. — The matrix M = |_m^J in general is nonreal. In the
simplest example of an equation with all distinct real roots \i 7^ Aj C R the
monodromy matrix is diagonal: M = diag(exp27r\/—l A^). In the general
case M will have the same exponential entries on the diagonal. If the
spectrum is not simple, then the Jordanian basis for M may be nonreal, as
the example of the equation (iu'y =  0 shows.

This equation has a fundamental system of solutions /i = 1 and
/2 = m^; real on (0, +00), and the monodromy matrix at the point t =  0

is . Clearly, any Jordanian basis for the monodromy will be

nonreal.

is
 Proof. — The monodromy group of a real equation is r-symmetric
in the sense of §2. Hence for a monodromy matrix M corresponding to a

920 D. NOVIKOV AND S. YAKOVENKO

singularity on the real axis, the identity M~1 = M holds. This means that
the spectrum of M is symmetric with respect to the unit circle: if ^ is an
eigenvalue, then Ji~1 also is. If |/z[ = 1 is an eigenvalue on the unit circle,
then the corresponding eigenvector can be chosen real. Indeed, if Mz == /zz,
then M"1^ = Mz = JIz = /-A"
1^, hence z is also an eigenvector with the

same eigenvalue p,. But then either Rez = -(z+z ) or Imz = —-=(z—z)
2 2-\/—1
will be a real nonzero eigenvector. This argument shows that in case of a
simple spectrum the monodromy matrix M can be diagonalized by a real
invertible transformation. By induction one may easily prove that in the
case of multiple eigenvalues on the unit circle one may put M into an upper-
triangular (though not Jordanian) form by a real transformation (see the
remark above).

Now we show that if the singularity is real Fuchsian, then the
monodromy operator has the spectrum on the unit circle. Indeed, if \fi\ ^  1,
then there exists A ^ R such that exp 27r\^:lX = ^. Take an eigenfunction
(the eigenvector of the monodromy operator) corresponding to fi: this
eigenfunction must have a form ^/i(^), where h(t) is single-valued (hence
meromorphic) in a small punctured neighborhood of t = 0. But then,
according to §1.5, A + n must belong to the spectrum of the singularity for
some integer n € Z. This contradicts to the assumption that the spectrum
is real. Hence SpecM belongs to the unit circle, and we can apply the first
argument to prove the lemma. D

If the fundamental system of solutions is chosen according to Lemma 5,
then the Wronskians Wp(t) associated with the corresponding ordering, will
satisfy the following monodromy condition:

^oWo(t) =  exp(27rV^TA^) W^t), /?=!,... , n2{d + 1),

where A^ € R are real numbers. Indeed, the linear subspace spanned by
the first (3 monomials Fajk will be then invariant by Ao. More exactly,
the monodromy matrix factor for the monomials Focjk after the specified
ordering will be the block diagonal matrix of the size n 2^ +1) x n 2^ +1)
with the upper-triangular block M of the size n x n occurring n(d + 1)
times on the diagonal. The diagonal entries of the matrix factor M
are the exponentials exp sl^\/~=\ \i (see the remark above), while the
numbers exp 27rv/:rlA/3 are the upper-left /?x/?-minors of that large matrix.
Moreover, without loss of generality one may assume that 0 ^  A^ < 1, since
integer parts of A/? are inessential.

ZEROS OF COMPLETE ABELIAN INTEGRALS 921

COROLLARY. — The functions

Wo(t)=t-^Wo(t), 0^<1 ,

are single-valued in a punctured neighborhood of the origin.

4.2. Zeros of Wronskians near Fuchsian singularities.

Since fj have a regular singularity at t =  0, the functions W^ may
have at most poles at t = 0, being real on the real axis. In order to estimate
the order of this pole, we introduce the growth exponent for a real function

y? as n  r i T ^I^W IGoM=hmsu p '^  /1.
t-^o+ int- 1

Due to the known analytic structure of the fundamental solutions fj, one
has the following estimates:

GO^-^OLO) ,

Go [^- 1)] ^  0^(1)-a ,

Go [^  (^  /^- 1))] ^ OL(I) -  a + f3 ^  0^(1) + /?,

Go[^]^/3-0^(l)+J/3(/3-l) ,

Go[^]^/3-0^(l)4-^(/3-l) .

These arguments prove the following result.

LEMMA 6. — There exists a sequence of real numbers O^ satisfying
the estimate

(9) Op^O^d 2) V/?=l,2;...,n 2 (d+l)

such that the functions
 Wft =  t^  W(3(t)

are holomorphic at t = 0. n

Remark. — We always choose the branches of Wp and t° real on
the positive semiaxis.

922 D. NOVIKOV AND S. YAKOVENKO

Remark. — The similar estimates can be done in a neighborhood
of t =  oo for G^ [(/?] == limsupin \ip(t)\/\iit:
t-»+0 0

G^kf^l^-^+OLO) ,
L J i t
G^W^O^d 2 )  V/3=l,...,n 2 (d+l) .

This proves analyticity of t~e(3 W^t) in a neighborhood of infinity for an
appropriate choice of 6^ subject to the same asymptotic estimate.

4.3. Proof of Theorem 3.

First consider the case of a finite real singularity; without loss of
generality we may put it being at the origin t = 0.

Let K =  (0, t^\ be the semiinterval, U C C \  (Si, \  0) an open
connected simply connected neighborhood of K =  [0,^] and D C U a
small open disk on a positive distance from t = 0 and the boundary of U".

From Lemma 4 it follows that for all (3 = 1,... , n 2 ^ + 1)

max|TV^)| ^ exp(-exp0p LW),
t(ED
max | Wp (t) | ^  exp exp Ou L (m d).
t(EU

For any compact subset D of the universal covering over C\0  the function
t° (or more precisely, the branch of ^,  real on the positive semiaxis) on D
admits the two-sided estimate:

(10) exp(-|(9| • 0^(1)) ^ min |^ | ^ max t°. ^  exp(|(9| • 0^(1)).

These estimates imply that for all /3 and for the proper choice of branches

m9iX_\Wp{t)\ ^  mox\Wp(t)\ ^  exp(-expOD,z/(^)),
teKUD teD

max\Wf3{t)\ < expexpO^L(ln^)-
tf^QU

But the functions Wp(t) are in fact analytic in U. Hence the generalized
Jensen lemma can be applied to W^, yielding an exponential upper estimate
for the number of complex isolated zeros of the latter. But since t
013 are
invertible on the positive semiaxis, the same estimate holds also for the
original Wronskians Wp(t) on K. Thus one may apply Theorem 6 to the
semiinterval K, to prove the simple exponential estimate for the number

ZEROS OF COMPLETE ABELIAN INTEGRALS 923

of isolated zeros in this case. The proof of Theorem 3 in the case of a finite
singularity is complete.

If the singularity is at t = oo, then the estimates established in the
remark above should be used. n

5. ALMOST IRREDUCIBLE EQUATIONS AND
THEIR POLYNOMIAL ENVELOPES

In this section we prove that the simple exponential estimate for the
number of real isolated zeros holds also for polynomial envelopes of linear
equations with essentially irreducible monodromy. The proof is based on
the well-known procedure of depression (reduction) of the order of a linear
differential equation provided that some of its solutions are known [In].

5.1. Depression of the order of a linear equation.

Assume that the operator L admits a nontrivial factorization, L =
UP, with L', P e S), ordP = 1, P =  9-}-a(t), a e k. Then the fundamental
system of solutions for Lu = 0 can be chosen in the form

/l5/25-.-5/n ?

where fn is a nontrivial solution for the equation Pu =  0.

For an arbitrary function /  from the rational envelope 9^(£) we find a
differential operator R = Rf e 2), depending on /, such that Rf e ^('C'),
and estimate the Rolle index of Rf. Let

n
f  =  ^  ^y^"^  rj k G k, degrjk ^  d,
j,k=l

be an arbitrary function from the rational d-envelope of L. Since fn satisfies
a first order equation, all derivatives of fn up to order n— 1 are proportional
to fn with coefficients from k of degrees Op(l). Thus without loss of
generality one may assume that Tnk = 0 for k = 2,... , n, and degr^i ^ d.
Then the operator RQ =  P ' ri^ ^o = ^i
1? applied to /, will eliminate the
n—l n  /'i.^ ^
last term while preserving the form of the combination ^  ^  ^^jkj- ~ -
j=l  k=l
the degrees of the new coefficients will be at most 4d + 0^(1) = O^d).

924 D. NOVIKOV AND S. YAKOVENKO

The functions fj = Pfj = /.' + a,fj constitute a fundamental system
of solutions for the equation L'u = 0, since 0 = Lfj = L'Pfj = L^fj.
Moreover, k-l
/i fc ~ l)=^+E C ^? -l)'  fc=2,...,n , 6fc,c,ek,
^=1
and even more generally, for any operator A € D the operator division with
remainder A = c + BP [In] gives

(11) Afj =  cfj +  Bfj, c € k, B  € 'D, ord® ^  ord2l -  i.

The degrees of the coefficients bjc, Q are at most Op(l), hence the function
Rof can be expressed as
^o^Ewr^+E^j',A;=i j=i
with all rational coefficients of degrees OL(^)-

The first sum is an element from the rational OL (d)-envelope of
I/, as required. To eliminate the second sum, we apply the operator
Ri = L. n  € 2), n  = ^-
1 € k, degn = OL(d). By (11),
J?i/i = 0 mod ^(^C'), 9iif) = qjfj mod ^(/C') j = 2,... , n -  i,

thus the total number of terms in the second sum is decreased by 1. Iterating
the last step n  — 1 times, one may construct operators R^,..., Rn-i € ^
in such way that Rj; == L ' 7^, T^ 6 k, degry = O^c?) and
n-l

I?n-l  • • • R2  ' Rl E  ^ ^  =  °  mod  ^( /c/) '
J= l
Evidently, the degrees of the coefficients of all combinations and operators
will be at most 0{d). Finally we put

R  =  ^n ' Rn-1 " • R2 ' RI ' RO^

where the rational coefficient r^n € k is chosen in such a way that R is an
operator with polynomial coefficients.

Then Rf € 9l(£'), and

(1) the degrees of the coefficients of Rf represented as an element from
^(^Q will be at most OL^),

(2) R=Pri'L'Pn-i'L-"?2'L'^'P'PQ,with?o  =r^ 1, degr, =  OL^).

ZEROS OF COMPLETE ABELIAN INTEGRALS 925

5.2. Demonstration of Theorems 4 and 5.

Let /  be an analytic function on a segment K from the polynomial
d-envelope of an operator L G 2), and L = L'P, ordP = 1. Consider the
operator R constructed in the previous section. This operator transforms
/  into the function Rf which is also analytic on K (since the coefficients
of R are polynomial) and belongs to the rational envelope of L' .

The same arguments that proved Theorem 6, show that the Rolle
index of the operator R on K is at most O^d) provided that the Rolle
index of L is finite on K and independent of d. Indeed, the number of poles
of each rational factor is at most OL^)- Thus if L' is already irreducible,
then the simple exponential estimate for the number of zeros of Rf and
the upper estimate for the Rolle index of R imply the simple exponential
estimate for the number of zeros of /  on K.

If L' = I/'P', then the above arguments may be iterated, and
we conclude by induction that the simple exponential estimate for the
number of zeros holds on K for polynomial envelopes of any operator
L = L^Pi?2 • • • Pm, if it holds for L* on K.

In assumptions of Theorem 4 the segment K is compact and on a
positive distance from E^, so the Rolle index of L is automatically finite. If
K is a semiinterval with a real Fuchsian singularity at the endpoint, then
the real spectrum assumption guarantees that the Rolle index of L will be
also finite on K despite the presence of the singularity. On the other hand,
the real spectrum assumption for L implies that the spectrum of the last
irreducible factor L^ will be also real at the endpoint so that the simple
exponential estimate holds for the polynomial envelope of L^ on K. n

6. GENERALIZATIONS

Theorem 2, the principal result which implies all other assertions of
this paper, has a global nature and is valid in a much more general settings.
Let U C C be any open domain symmetric by the involution r : t ^  ?, and
k = Ar(U) the field of single-valued analytic functions in [7, symmetric
by the involution r. Then we may consider an arbitrary unitary linear
differential operator L with coefficients from k:
n
L  =  ^^-fc^)^ , di € k, ao EE 1.
k=0

926 D. NOVIKOV AND S. YAKOVENKO

Then there naturally arises the monodromy representation of the funda-
mental group of U by {n x n)-matrices 7 i-^ M~ 1, and one can define
irreducible operators as in §3.4.

THEOREM 2'. — IfK is a compact subset ofUr\R and L e  k[<9] is
irreducible, then the assertion of Theorem 2 about the simple exponential
bound for the number of real isolated zeros remains valid in this extended
setting as well. n

In other words, coefficients of the operator L may have even essential
singularities on the Riemann sphere. In fact, even the assumption that all
coefficients are real on the real axis, can be dropped away (however, this
would require different type of arguments). Theorem 4 also is valid in this
extended setting as well; in both cases one should reproduce literally the
same proof.
 BIBLIOGRAPHY

[AI] V. ARNOLD, Yu IL'YASHENKO, Ordinary differential equations, Encyclopedia of
mathematical sciences vol. 1 (Dynamical systems-I) Springer, Berlin, 1988.

[F] G. FROBENIUS, Ueber die Determinante mehrerer Fimctionen Variablen, J. Reine
Angew. Math., 7 (1874), 245-257.

[H] P. HARTMAN, Ordinary Differential Equations, John Wiley, N. Y.-London-Sydney,
1964.

[IY1] Yu. IL'YASHENKO , S. YAKOVENKO, Double exponential estimate for the num-
ber of zeros of complete Abelian integrals and rational envelopes of linear
ordinary differential equations with an irreducible monodromy group, Inventiones
Mathematicae, 121, n° 3 (1995).

[IY2] Yu. II/YASHENKO , S. YAKOVENKO, Counting real zeros of analytic functions
satisfying linear ordinary differential equations, J. Diff. Equations, 1996 (to
appear).

[In] E. L. INCE, Ordinary Differential Equations, Dover PubL, 1956.

[M] P. MARDESIC, An explicit bound for the multiplicity of zeros of generic Abelian
integrals, Nonlinearity, 4 (1991), 845-852.

[NY] D. NOVIKOV, S. YAKOVENKO, Une borne simplement exponentielle pour Ie
nombre de zeros reels isoles des integrales completes abeliennes, Comptes Rendus
Acad. Sci. Paris, serie I, 320 (1995), 853-858.

[Pe] G. PETROV, Nonoscillation of elliptic integrals, Punkcional'nyi' analiz i ego
prilozheniya, 24-3 (1990), 45-50 (Russian); English translation, Functional Anal-
ysis and Applications.

[P6] G. POLYA, On the mean-value theorem corresponding to a given linear homoge-
neous differential equation, Trans. Amer. Math. Soc., 24 (1922), 312-324.

ZEROS OF COMPLETE ABELIAN INTEGRALS 927

[Sch] L. SCHLESINGER, Handbuch der Theorie der linearen Different ialgleichungen,
Teubner, Leipzig, 1 (1895), 52, formula (14).

[Y] S. YAKOVENKO, Complete Abelian Integrals as Rational Envelopes, Nonlinearity,
7 (1994), 1237-1250.
 Manuscrit recu Ie 21 decembre 1994,
accepte Ie 19 mai 1995.

D. NOVIKOV and S. YAKOVENKO,
Department of Theoretical Mathematics
The Weizmann Institute of Science
P.O.B. 26
Rehovot 76100 (Israel).
E-mail address: dmitri@wisdom.weizmann.ac.il
yakov@wisdom. weizmann. ac. il
