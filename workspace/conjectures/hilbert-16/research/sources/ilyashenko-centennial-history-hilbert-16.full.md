<!-- source: https://www.ams.org/journals/bull/2002-39-03/S0273-0979-02-00946-1/S0273-0979-02-00946-1.pdf | converted from PDF -->

BULLETIN (New Series) OF THE
AMERICAN MATHEMATICAL SOCIETY
Volume 39, Number 3, Pages 301–354
S 0273-0979(02)00946-1
Article electronically published on April 9, 2002

CENTENNIAL HISTORY OF HILBERT’S 16TH PROBLEM

YU. ILYASHENKO

Abstract. The second part of Hilbert’s 16th problem deals with polynomial
diﬀerential equations in the plane. It remains unsolved even for quadratic
polynomials. There were several attempts to solve it that failed. Yet the prob-
lem inspired signiﬁcant progress in the geometric theory of planar diﬀerential
equations, as well as bifurcation theory, normal forms, foliations and some
topics in algebraic geometry. The dramatic history of the problem, as well as
related developments, are presented below.

§1. The problem and its counterparts

What may be said about the number and location of limit cycles of a planar
polynomial vector ﬁeld of degree n? (The limit cycle is an isolated closed orbit
of a vector ﬁeld.) This second part of Hilbert’s 16th problem appears to be one
of the most persistent in the famous Hilbert list [H], second only to the Riemann
ζ-function conjecture.
Traditionally, Hilbert’s question is split into three, each one requiring a stronger
answer.

Problem 1. Is it true that a planar polynomial vector ﬁeld has but a ﬁnite number
of limit cycles?

Problem 2. Is it true that the number of limit cycles of a planar polynomial vector
ﬁeld is bounded by a constant depending on the degree of the polynomials only?

The bound on the number of limit cycles in Problem 2 is denoted by H(n)and
known as the Hilbert number. Linear vector ﬁelds have no limit cycles; hence
H(1) = 0. It is still unknown whether or not H(2) exists.

Problem 3. Give an upper bound for H(n).

A solution to any of these problems implies a solution for the previous ones.
Only the ﬁrst problem is solved now. The positive answer was established in [E92],
[I91].
There are analytic counterparts of Problems 1 and 2.

Received by the editors December 2001.
2000 Mathematics Subject Classiﬁcation. Primary 34Cxx, 34Mxx, 37F75.
Key words and phrases. Limit cycles, polynomial vector ﬁelds, normal forms, bifurcations,
foliations, Abelian integrals.
The author was supported in part by grants NSF DMS 997-0372, NSF 0010404, and CRDF
RM1-2086. The main results of the paper were presented at colloquium talks at Cornell Uni-
versity, December 1999, and Northeastern University (Harvard - MIT - Brandeis - Northeastern
Colloquium), November 2000. The author thanks Dr. S. Gelfand, who assisted with the latter
talk and suggested the idea of writing a survey on the subject.

c⃝2002 American Mathematical Society

301

302 YU. ILYASHENKO

Problem 4. Is it true that an analytic vector ﬁeld on the 2-sphere has but a ﬁnite
number of limit cycles?

An analytic family of vector ﬁelds is a ﬁnite parameter family of analytic vector
ﬁelds that depend analytically on the parameter.

Problem 5. Is it true that for any analytic ﬁnite parameter family of vector ﬁelds
on the 2-sphere the number of limit cycles of the equations in the family is uniformly
bounded with respect to the parameter, provided that the parameter set is compact?

Problem 4 is solved by the same authors as Problem 1. In fact, both proofs
deal with analytic vector ﬁelds and obtain the result in the polynomial case as a
consequence.
A positive answer to Problem 5 would imply those for Problems 1, 2, and 4. This
is obvious for Problem 4 and is proved by Poincar´e compactiﬁcation for Problems 1
and 2.
The Poincar´e compactiﬁcation transforms a polynomial vector ﬁeld in the plane
into an analytic vector ﬁeld on the 2-sphere. Consider a plane tangent to the sphere
at a point named the Southern Pole, and a projection of the sphere minus its equator
on the plane along the straight lines passing through the center. The inverse map is
a diﬀeomorphism on each of the two open hemispheres, the Northern and Southern
ones. The polynomial vector ﬁeld on the plane lifted to the hemispheres becomes an
analytic vector ﬁeld, and vectors on the sphere tending to the equator correspond
to vectors on the plane tending to inﬁnity. After multiplication by a proper power
of the distance to the plane passing through the equator, this vector ﬁeld becomes
analytic everywhere on the sphere, with a ﬁnite number of singular points on the
equator. The number of limit cycles for the new ﬁeld is at least twice as large as
that for the original one. Then any upper bound of the number of limit cycles of
the new ﬁeld implies an upper bound for the original polynomial vector ﬁeld.
On the other hand, multiplication by a nonzero constant factor does not change
the number of limit cycles of a polynomial vector ﬁeld. Hence, the parameter
space for polynomial vector ﬁelds of given degree in the plane should be the space
of coeﬃcients of the polynomials factorized by multiplication. Therefore, it is a
projective space, hence compact. This reduces Problems 1 and 2 to Problem 5.
It looks surprising, but there is a smooth counterpart for Hilbert’s problem. (All
through the paper smooth means inﬁnitely smooth unless explicitly stated.) On one
hand, it is easy to construct a C∞ vector ﬁeld on a 2-sphere with inﬁnitely many
limit cycles. An example may be written in polar coordinates:

˙r = f (r), ˙ϕ =1,

where f is a C∞ function equal to zero outside [1,2] and having an inﬁnite number
of isolated zeros on [1,2]. On the other hand, the following heuristic principle holds:
A smooth function behaves like an analytic one when it is met in a typical ﬁnite
parameter family.
For instance, consider a k-parameter family of smooth functions on the line. By
a small perturbation of the family the following property may be achieved: All the
functions of the family have only isolated zeros. The multiplicity of these zeros does
not exceed k +1. This is a straightforward consequence of Thom’s transversality
theorem.

Problem 6 (Hilbert-Arnold problem). Is it true that for a generic ﬁnite parameter
family of smooth vector ﬁelds on the 2-sphere the number of limit cycles of the

CENTENNIAL HISTORY OF HILBERT’S 16TH PROBLEM 303

equations in the family is uniformly bounded with respect to the parameter, provided
that the parameter set is compact?

Only a restricted version of Problem 6 is solved as of now; see Section 2 below.
It should be stressed that the analytic and smooth versions of Hilbert’s 16th
problem, Problems 4 and 6 above, are independent of the original polynomial ver-
sion, Problem 3.
 §2. Digest of the history

As is typical for Hilbert’s problems, the 16th one focuses many diﬀerent areas and
has produced new developments. The history of the problem is dramatic; several
claims were published and disproved; see Figure 1.
The problem was stated by Hilbert in 1900. Before that, Poincar´econsidered
polynomial vector ﬁelds in the plane as soon as he proposed his program for develop-
ing the geometric theory of diﬀerential equations. He introduced the notion of limit
cycle and proved that a planar polynomial vector ﬁeld without saddle connections
has only a ﬁnite number of limit cycles.
In 1923, Dulac [D] claimed that he solved Problem 1 above in its full generality.
In the middle of the 50s, Petrovskii and Landis published a solution to Problem 3
[PL1], [PL2]. They claimed that H(n) ≤ P3(n) (a certain polynomial of degree 3),
and H(2) = 3. In the early 60s their claim was disproved by S. P. Novikov and the
author. Quadratic vector ﬁelds with 4 limit cycles were constructed in [CW], [Shi].
In 1981, a huge gap in Dulac’s proof was found [I82], [I85]. Thus, after eighty years
of development, our knowledge on Hilbert’s 16th problem was almost the same as
at the time when the problem was stated.
The main results related to Hilbert’s 16th problem are summarized below.PHDP-LI-E1900235557638191-92AFNSPBRVNFIHPRF
Figure 1. Summary of the history of Hilbert’s 16th problem.
Roman letters stand for names, calligraphic ones for new devel-
opments. P—Poincar´e; H—Hilbert, D—Dulac, P-L—Petrovskii-
Landis, E—Ecalle, I—Ilyashenko; NF —normal forms, AF —
analytic foliations, IHP—inﬁnitesimal Hilbert 16th problem,
NSP—nonlinear Stokes phenomena, RF—resurgent functions,
B—bifurcations, RV—restricted versions of the Hilbert 16th prob-
lem.

304 YU. ILYASHENKO

Figure 2. Ovals of a polynomial

Theorem 2.1 (Finiteness Theorem for Limit Cycles) [E92], [I91]. A polynomial
vector ﬁeld in the plane has only a ﬁnite number of limit cycles. The same is
true for analytic vector ﬁelds on the 2-sphere.

Some key ideas and the history of the proof of this theorem are presented in
Sections 3 and 4.
Because of the persistence of Hilbert’s 16th problem, it makes sense to consider
several simpliﬁed versions in advance [S]. Amidst those, we discuss the Hilbert-
Arnold problem in Section 5, Abel and Lienard equations in Section 6, and the
inﬁnitesimal Hilbert problem in Section 7. The latter one deals with perturbations
of integrable vector ﬁelds and is stated as follows.
Consider a real polynomial H of degree n + 1 in the plane. A closed connected
component of a level curve H = t is denoted by γ(t) and called an oval of H. These
ovals form continuous families; see Fig. 2.
Let ω = Adx + Bdy be a real 1-form with polynomial coeﬃcients of degree at
most n. Let
 I(t)= ∫

γ(t) ω.(2.1)

Problem 7 (Inﬁnitesimal Hilbert’s 16th problem). Find an upper bound V (n) of
the number of real zeros of the integral (2.1). The bound should be uniform with
respect to the choice of the polynomial H, the family of ovals {γ(t)} and the form
ω. It should depend on the degree n only.

The most general result related to this problem is

Theorem 2.2 [V], [Kh84]. For any n, the upper bound V (n) in the inﬁnitesimal
Hilbert 16th problem exists.

Some estimates of the number of zeros of the integral (2.1) depending on H
and not on ω are presented in Section 7. The proof of Theorem 2 is based on
the fewnomial theory of Khovanskii. A brief sketch of the theory is presented in
Section 5.
Zeros of Abelian integrals (2.1) are related to limit cycles in the following way.
Consider a perturbation of an integrable system

dH + εω =0,(2.2)

with H and ω the same as above. We say that an oval γ(t) generates a limit cycle
of (2.2) if there exists a continuous family of closed curves l(ε) deﬁned for small ε
such that l(ε) is a limit cycle of (2.2) for ε ̸=0, and l(0) = γ(t).

CENTENNIAL HISTORY OF HILBERT’S 16TH PROBLEM 305

Pontryagin Criterion. If an oval γ(t) of the polynomial H generates a limit cycle
of (2.2),then I(t)= 0. On the other hand, if I(t)=0 and I ′(t) ̸=0, then the oval
γ(t) generates a limit cycle of (2.2).

Bifurcation theory is intimately related to Hilbert’s 16th problem. Indeed, the
function “number of limit cycles of the equation” has points of discontinuity cor-
responding to equations whose perturbations generate limit cycles via bifurcations.
Limit cycles may bifurcate from polycycles. A polycycle is a connected ﬁnite union
of singular points and orbits between them that forms a kind of polygon (see 3.1 for
more details). The cyclicity of a polycycle in a family of equations is the maximal
number of limit cycles that may bifurcate from the polycycle in this family.

Problem 8. Is it true that a polycycle occurring in a ﬁnite parameter family of
planar analytic vector ﬁelds has only ﬁnite cyclicity?

Problem 9. Is it true that a polycycle occurring in a generic k-parameter family of
smooth planar vector ﬁelds may generate only a ﬁnite number of limit cycles, with
an upper bound depending on k only? (This latter quantity is denoted by B(k).)

A positive answer to Problem 8 implies the existence of H(n) for any n. A positive
answer to Problem 9 implies a positive answer in the Hilbert-Arnold problem. These
implications are proved by using simple compactness arguments due to Roussarie
[R88]. Both problems remain unsolved. Problem 9 seems to be simpler than the
previous one and is partly solved; see Theorems 3 and 4 below.

Deﬁnition 2.1. A singular point of a planar vector ﬁeld is called elementary if
the linearization of the ﬁeld at this point has at least one nonzero eigenvalue. A
polycycle is called elementary if it contains elementary singular points only.

Deﬁnition 2.2. Denote by E(k) the maximal number of limit cycles that may
bifurcate from an elementary polycycle in a typical k-parameter family of smooth
planar vector ﬁelds.

Theorem 2.3 [IYa95a]. For any k, the number E(k) exists.

Corollary. The Hilbert-Arnold problem has a positive solution for families of vector
ﬁelds having elementary singular points only.

Theorem 2.4 [K*]. For any k, E(k) ≤ 225k2 .

Theorem 4 is announced in [IK] and proved in [K*]. The estimate given by this
theorem may be too high. Yet it is one of the ﬁrst Hilbert type numbers (that is,
bounds to the number of limit cycles) obtained up to now. Other Hilbert type
numbers are presented in Sections 6 and 7.
This paper is organized as follows. The main achievement and the mistake of
Dulac in his attempt to prove the Finiteness Theorem 1 are presented in Section 3,
together with a sketch of the proof of Theorem 1 for ﬁelds with hyperbolic singular
points only.
Some other ingredients of the proof of the Finiteness Theorem, including nonlin-
ear Stokes phenomena, appear in Section 4. That section is devoted to the theory
of normal forms, both smooth and analytic. Not only Theorem 1, but also the solu-
tion of the Hilbert–Arnold problem for vector ﬁelds with elementary singular points
only, given in Theorems 3 and 4, heavily relies upon the results of this section.

306 YU. ILYASHENKO

A survey of planar bifurcation theory, together with the main ideas of the proof
of Theorems 3 and 4, is presented in Section 5. One of the sources of the proof is
the fewnomial theory by Khovanskii, brieﬂy sketched in 5.4.
Section 6 contains an approach based on a growth-and-zeros theorem for holo-
morphic functions which provides an estimate of the number of zeros of a function
in a smaller domain via its growth from a smaller to a larger domain, and the
geometry of these two domains; see 6.4 for details. This theorem is applied to
the estimate of the number of limit cycles of Abel and Lienard equations with the
boundary for the coeﬃcients included in the estimate. Therefore, these results do
not solve Hilbert’s 16th problem, even for these particular classes of equations,
since the required estimate should depend on the degree of the polynomials only;
see Problems 6.1 and 6.2 below. But these are the only estimates of the number
of limit cycles on the whole plane R2 for Abel and Lienard equations of arbitrarily
high degree obtained up to now.
Section 7 lies near the boundary between algebraic geometry and diﬀerential
equations. It contains results about the freedom of location of limit cycles obtained
by complex analytic methods. Moreover, it presents the main ideas from the proof
of Theorem 2 due to Varchenko and Khovanskii about the existence of a universal
bound on the number of zeros of a real Abelian integral. It also contains explicit es-
timates of the number of zeros of the integral (2.1) which are once more of restricted
character. The restriction is on the choice of the Hamiltonian H that determines
ovals γ(t) in (2.1): it is of arbitrary degree but of special type. The polynomial
1-form ω is arbitrary, with degree of the polynomial coeﬃcients less than deg H.
Section 8 is devoted to the survey of the global theory of analytic foliations in the
complex plane. Basic development of the theory [PL1] was strongly motivated by
Hilbert’s 16th problem. In the last three decades it became an independent subject
with its own results and problems, which are surveyed in Section 8. Applications of
this theory to the study of real limit cycles is the subject of future research, which
is discussed in Section 8, as well.
We do not provide any detailed proofs. Sketches of the proofs are presented
occasionally to show the key ideas and the interrelations between diﬀerent topics
in the ﬁeld.
Theorems and problems in the introductory sections 1 and 2 have a one-digit
numeration. Below the numeration is binary.

§3. Finiteness theorem for limit cycles

The main ideas and the history of the proof of Theorem 1 are presented in this
and the next sections.

3.1. Nonaccumulation Theorem. Suppose that Theorem 1 is wrong, that is,
an analytic vector ﬁeld on a 2-sphere may have an inﬁnite number of limit cycles.
From the very beginning we assume that the vector ﬁeld has but a ﬁnite number of
singular points; if not, we divide the components of the ﬁeld by a common factor.
Two limit cycles without a singular point in between belong, by deﬁnition, to the
same nest. At least one nest must contain an inﬁnite number of limit cycles. By
the compactness of the sphere, they have to accumulate to some limit set. This
limit set has to be either a periodic orbit or a union of singular points and hetero
(homo)clinic orbits that connect them.

CENTENNIAL HISTORY OF HILBERT’S 16TH PROBLEM 307

All of this is true both for smooth and analytic vector ﬁelds. Now the crucial
diﬀerence comes. In the smooth case, the limit set above may contain a countable
number of orbits that emerge and land on the same singular point like petals. In the
analytic case, this limit set may be but a ﬁnite union of orbits. This is deduced from
the Desingularization Theorem in Section 3.5 below. Hence, in the analytic case,
the limit set is a polycycle, that is, a ﬁnite union of singular points and orbits that
connect them. In more detail, a polycycle of a vector ﬁeld is a cyclically ordered
ﬁnite set of singular points (with possible repetitions), and a cyclically ordered set
of disjoint orbits of the ﬁeld that connect the singular points in a speciﬁc order:
the time oriented jth orbit connects the jth and j + 1st singular points. Now,
Theorem 1 is implied by the following.

Nonaccumulation Theorem 3.1. Limit cycles of an analytic vector ﬁeld on the
2-sphere cannot accumulate to a polycycle of this ﬁeld.

3.2. Dulac’s Theorem. Suppose now that the Nonaccumulation Theorem is
wrong. Then there exists a polycycle γ and a cross-section, namely, a half interval
with a vertex on the polycycle, transversal to the vector ﬁeld outside the vertex,
such that a countable number of limit cycles cross it. Therefore, for this cross-
section, a ﬁrst return map, also called a Poincar´e map, is well deﬁned. Denote it
by P. This map has a countable number of ﬁxed points that accumulate to the
vertex. Moreover, P is analytic outside of the vertex but, in general, cannot be
analytically extended across the vertex. The problem is to prove that the Poincar´e
map cannot have an inﬁnite number of ﬁxed points accumulating to the vertex of
the cross-section.
Suppose, for example, that γ consists of a single periodic orbit. Then P may
be analytically extended across the vertex of a cross-section. Hence, ﬁxed points
of the map P accumulate to an interior point of its domain. By the uniqueness
theorem for holomorphic functions, P equals the identity. Hence, P has no isolated
ﬁxed points, and the neighborhood of γ contains no limit cycles, a contradiction.
Dulac tried to generalize this argument for the case of an arbitrary polycycle.
The goal was to deﬁne a class of maps of a half-interval that have the uniqueness
property like analytic ones. On the other hand, this class should contain Poincar´e
maps of polycycles of analytic vector ﬁelds.

Deﬁnition 3.1. Agerm ofamap f :(R
+, 0) → (R+, 0) is called semiregular if it
is smooth outside zero and admits the following asymptotic expansion:

ˆf (x)= cx
ν0 + ∑

j Pj (ln x)x
νj ,(3.1)

where c> 0, 0 <νj ↗∞, and j ≥ 0; Pj are real polynomials.

By deﬁnition, ˆf provides an asymptotic expansion for f if for any ν> 0, there
exists a partial sum of ˆf that approximates f with accuracy better than x
ν as x
tends to 0.

Theorem 3.2 (Dulac’s Theorem) [D]. For any polycycle of an analytic vector
ﬁeld, a cross-section with the vertex zero on the polycycle may be so chosen that the
corresponding Poincar´e map will be ﬂat, inverse to ﬂat, or semiregular.

Recall that the germ f :(R+, 0) → (R+, 0) is ﬂat if all the derivatives of f at 0
are zeros.

308 YU. ILYASHENKO

3.3. Dulac’s lemma and a counterexample.

Lemma 3.1 [D]. Let a semiregular map have an inﬁnite number of ﬁxed points
(for brevity, f ∈ Fix ∞). Then f is the identity.

Proof. Suppose that f ̸= id, (3.1) is an asymptotic series for f, and cx
ν0 ̸= x.
Then, f canhave no ﬁxedpoints near 0.
Suppose that cx
ν0 ≡ x. Then f (x) − x = P1(ln x)x
ν1 (1 + o(1)). Once more, the
right hand side has no zeros near the origin, because any of the three factors has
this property.
The assumption f ̸= id is carried to a contradiction.

Dulac’s theorem and Lemma 3.1 together imply the Nonaccumulation Theorem.
Indeed, suppose that the theorem is wrong. Choose a cross-section as in Dulac’s
theorem. The corresponding Poincar´e map cannot be ﬂat nor inverse to ﬂat, or
else it has no ﬁxed points near zero. Hence, it is semiregular, and Dulac’s lemma
is applicable. Therefore, P =id , a contradiction.
This is a digest of Dulac’s memoir [D]. During almost 60 years the proof stood.
The reason is that the presentation of [D] is rather unclear, and part of the argument
above is hidden.
The proof of Dulac’s lemma is wrong. Indeed, the map f = x +(sin 1
x )e− 1
x
provides a counterexample to the lemma. In fact, the reasoning above proves the
following.

Modiﬁed Dulac’s lemma 3.2. If f is semiregular and has an inﬁnite number of
ﬁxed points, then ˆf = id.

Nothing can be said about the ﬁxed points of a semiregular map if its asymptotic
series consists of only one term equal to x. Hence, the class of semiregular maps is
insuﬃcient for the proof of the Nonaccumulation Theorem.

3.4. Almost regular germs and the Nonaccumulation Theorem for hyper-
bolic polycycles. As is shown in 4.4 below, Dulac’s theorem is in fact a statement
from the smooth rather than the analytic theory of diﬀerential equations. In order
to obtain the Nonaccumulation Theorem, analyticity must be used. This motivates
the following deﬁnitions.

Deﬁnition 3.2. Let C+ = {z ∈ C | Re z> 0}, ΦC : ζ ↦→ ζ + C√ζ2 +1 for any
C> 0. Such a set ΩC =ΦC(C+) is called a standard quadratic domain; see Fig. 3.

Let ξ = − log x be a logarithmic chart on (R+, 0); ξ :(R+, 0) → (R+, ∞). In
the logarithmic chart, a semiregular germ f :(R+, 0) → (R+, 0) is transformed to
agerm ˜f :(R+, ∞) → (R+, ∞). The asymptotic series Σ for ˜f, in the logarithmic
chart, has the form:
 Σ(ξ)= αξ + β + ∑

j Qj(ξ)e−µj ξ,(3.2)

where 0 <µj ↗∞,α > 0,β ∈ R,and Qj are real polynomials.

Deﬁnition 3.3. A germ at inﬁnity ˜f :(R+, ∞) → (R+, ∞) is called almost regular
if - some of its representatives may be holomorphically extended to a standard
quadratic domain ΩC for some C;

CENTENNIAL HISTORY OF HILBERT’S 16TH PROBLEM 309C+˚C
CC+
Figure 3. A standard quadratic domain ΩC .

- the extended germ has an asymptotic expansion in (ΩC , ∞):

Σ(z)= αz + β + ∑

j Qj(z)e−µj z,(3.3)

where α, β, Qj, and µj are the same as in (3.2).

Remark. One may guess that in Dulac’s terminology “semiregular” meant “half as
good as analytic”; in any case in the 19th century “regular” was used for “analytic”.
The germs deﬁned above are “better than semiregular”; this is the origin of the
term “almost regular”.

Theorem 3.3 (Uniqueness theorem for almost regular germs). An almost regular
germ at inﬁnity is uniquely determined by its asymptotic series.

Proof. Let f and g be two germs from the theorem. Denote by the same letters ex-
tensions of their representatives to some standard quadratic domain ΩC =ΦC (C+).
Let
 h = f − g, H = h ◦ ΦC .

The function h has zero asymptotic series in (ΩC , ∞). Hence, it is bounded in ΩC
and decreases on (R+, ∞) faster than any exponential e−µξ,µ > 0. Therefore, the
function H is holomorphic and has a superexponential rate of decay on (R+, ∞).
We can now apply a theorem of the Phragmen-Lindelof type. These theorems
claim that if a function f is holomorphic in some domain and decays faster than
some other function (this test function depends on the domain), then f is identically
zero.

Theorem 3.4 [Ti]. If a bounded function is holomorphic in C+ and decays faster
than any exponential on (R+, ∞), then it is identically zero.

Theorem 3.4 implies that H ≡ 0. This proves Theorem 3.3.

Deﬁnition 3.3’. An almost regular germ at zero f :(R
+, 0) → (R+, 0) is a germ
that, after passing to the logarithmic chart, becomes an almost regular germ at
inﬁnity.

Lemma 3.3. Almost regular germs form a group with respect to composition.

This is a straightforward consequence of the deﬁnition. Indeed, if two germs
have representatives holomorphic in two quadratic domains ΩC1, ΩC2, then their
composition is holomorphic in a third quadratic domain ΩC3,C3 ≫ C1,C3 ≫ C2,
provided that the germs are equal to an aﬃne one plus a term that tends to 0 at
inﬁnity. On the other hand, a substitution of one formal series of the form (3.3) into

310 YU. ILYASHENKO(b)(a)
Figure 4. (a) Decomposition of the Poincar´e map of a polycycle.
(b) A correspondence map.

another one gives rise to a new series of the form (3.3). Hence, a composition of two
almost regular germs is almost regular itself. In the same way, almost regularity of
the inverse of an almost regular germ is proved.
Almost regular germs are used to prove the theorem mentioned in the title of
this subsection.

Theorem 3.5 [I84]. Limit cycles of an analytic vector ﬁeld on the 2-sphere can-
not accumulate to a polycycle of this ﬁeld, provided that all of the vertices of the
polycycle are hyperbolic saddles.

The ﬁrst step is standard in the study of polycycles: the Poincar´e map of the
polycycle is presented as a composition of so called correspondence maps; see Fig. 4.
A correspondence map of a singular point is a map along the orbits, of a cross-
section through which the orbits enter the neighborhood of the singular point to
a cross-section through which they exit; see Fig. 4b. The ﬁrst cross-section is a
half-interval transversal to the ﬁeld with the vertex on the incoming separatrix that
enters the singular point as t → +∞. The second one is a similar cross-section with
the vertex on the outgoing separatrix.
The main step of the proof is the following.

Lemma 3.4 [I84]. The correspondence map of a hyperbolic saddle of an analytic
vector ﬁeld in the plane is almost regular.

The proof heavily relies on the theory of normal forms.
Lemmas 3.4 and 3.3 imply that the Poincar´emap, P, of a hyperbolic polycycle
γ of an analytic vector ﬁeld is almost regular.
Now suppose that limit cycles accumulate to γ. Then P has an inﬁnite number
of ﬁxed points. By Dulac’s theorem 3.2 and the modiﬁed Dulac’s lemma 3.2, the
asymptotic series for P is the identity: ˆP (x)= x. Hence, two almost regular germs
at zero, namely P and x, have the same asymptotic series (3.3) equal to z, written
in the logarithmic chart. By the Uniqueness Theorem 3.3, these germs coincide.
Hence, P ≡ id , and there are no limit cycles near γ, a contradiction.

3.5. Desingularization Theorem for complex singular points of planar
vector ﬁelds. The proof of the Nonaccumulation Theorem in the general case fol-
lows the same strategy. The Poincar´e map of the polycycle is decomposed into a
product of correspondence maps of the singular points (the vertices of the polycy-
cle). The problem is that, in the general case, these singular points may be very
complicated, and it seems hopeless to describe their correspondence maps. The
theorem below saves the situation.

CENTENNIAL HISTORY OF HILBERT’S 16TH PROBLEM 311(e)(c)(d)(f)(a)(b)
Figure 5. a-e. Phase portraits of elementary singular points: (a)
Saddle, (b) Node, c) Focus, d) Center, e) Saddle-node, f) Desin-
gularization of a petal; a blown up vector ﬁeld is projected to the
original one.

Desingularization of a singular point is a sequence of blow ups that replaces
the original point by a ﬁnite number of elementary singular points. The simplest
description of one step of blowing up may be given in terms of polar coordinates
(r, ϕ). Consider an analytic vector ﬁeld v with an isolated singular point. Consider
this singular point as the origin and transform its punctured neighborhood to an
annulus:

(r, ϕ) ↦→ (r +1,ϕ), {(r, ϕ)|r ∈ (0,ε),ϕ ∈ S1}↦→ {(r, ϕ)|r ∈ (1, 1+ ε),ϕ ∈ S1}.

The original vector ﬁeld v is transformed to a new ﬁeld ˜v that may be analyt-
ically extended across the pasted in circle S1 = {r =1} to an annulus r ∈
(1 − ε, 1+ ε),ϕ ∈ S1. In general, ˜v is zero at all of the points of the pasted
in circle. Dividing ˜v by a suitable power of r − 1 gives a new vector ﬁeld V that
has but a ﬁnite number of singular points on S1. This ﬁeld V is the result of one
step of blowing up the original vector ﬁeld v.
If the resulting singular points are complicated, the process may be repeated.

Theorem 3.6 (Desingularization Theorem). Let a real analytic vector ﬁeld have
a holomorphic extension to the complex plane which has an isolated singular point
zero. Then, the singular point of the original vector ﬁeld may be split into a ﬁnite
number of elementary singular points after a ﬁnite number of blow ups.

The assumption of the theorem is not restrictive: if it fails, the vector ﬁeld may
be divided by a real factor such that the quotient will satisfy the assumption.
The composition of blow ups mentioned in the Desingularization Theorem is
called aniceblow up.
Elementary singular points are deﬁned above; see Deﬁnition 2.1. By a homeo-
morphic coordinate change, and time reversal if necessary, an isolated elementary
singular point may be transformed to a linear saddle, node, focus, center or to the
standard saddle-node ˙x = x
2, ˙y = −y; see Fig. 5. This topological description
of elementary singular points goes back to Bendixson [B] and is presented in a
transparent form in [I85].
The proof of this theorem has a long history. Bendixson [B] claimed this theorem
but did not give a proof. To the best of our knowledge, Dulac was the only mathe-
matician who used it before the 60s. The ﬁrst complete proofs for the analytic case
were given independently by Seidenberg [Se] and Lefschetz [Lef]; a generalization
for the smooth case is due to Dumortier [Du]. The ﬁrst transparent proof was given
by Van den Essen and is presented in [MM]. There is still no textbook that contains
this proof.

312 YU. ILYASHENKO

We can now explain why the limit set mentioned in 3.1 is but a ﬁnite union of
orbits. This is the same as explaining why a singular point has but a ﬁnite number
of petals in the analytic case. Any petal is produced by two nodes or saddle-nodes
of a nice blow up, with a family of connections between them; see Fig. 5f. Under the
projection which is inverse to the composition of the blowing up transformations,
the two nodes or saddle-nodes collide and their connections form a petal. But a
nice blow up contains only a ﬁnite number of singular points; hence, the original
singular point has but a ﬁnite number of petals.
The Desingularization Theorem is one of the basic facts of the local theory of
planar diﬀerential equations. All of the local study of real and complex planar
vector ﬁelds heavily relies on this theorem. For the proof of the Nonaccumulation
Theorem, the complicated singular points on the polycycle should be desingular-
ized. The polycycle will be replaced by a “longer one” having more vertices, now
all of them being elementary singular points. The theory of normal forms pro-
vides the description of the correspondence maps for these points. After that the
compositions of the above maps should be studied.
The theory of normal forms is surveyed below, including the description of the
above correspondence maps. The study of their compositions, needed for the proof
of Theorem 3.1, is very involved and goes beyond the scope of this survey.

3.6. Applications to the local study of planar vector ﬁelds. The Desingu-
larization Theorem and Dulac’s theorem provide an approach to the study of the
topology of a phase portrait for a planar analytic vector ﬁeld near any isolated
singular point; here isolated means isolated in C
2. The problem splits into two
cases: the so called characteristic and monodromic ones. The ﬁrst case is well
understood, while the second one, for the complicated singular points, remained
untouched until the Dulac theorem was applied. The main results in the ﬁeld are
the following.
A local geometrical problem is called algebraically solvable in the sense of Arnold
if the answer to this problem may be found after a ﬁnite number of algebraic
operations on the Taylor coeﬃcients of the data, provided that the data avoids an
exceptional set of inﬁnite codimension.
Sample problems under study are the following: Does a function have a max-
imum at zero? Is a singular point 0 of a vector ﬁeld Lyapunov stable? Does a
vector ﬁeld have an orbit that enters the singular point zero, tangent to a certain
direction? And so on.
For any n, consider J n, the n-jet space of functions or vector ﬁelds at the origin.
A jet is positive (negative) if for all of its representatives, the answer to the question
under study is “yes” (“no”). A jet is neutral if for some of its representatives the
answer is “yes”, and for some others “no”. A problem is algebraically solvable if the
following hold:
- For any n, the set of neutral n-jets is semialgebraic (that is, equal to a ﬁnite
union of sets deﬁned by algebraic equations and inequalities like P> 0where P is
a polynomial).
- The codimension of the set of neutral n-jets tends to inﬁnity, as n →∞.
For example, consider the problem: does a function of one variable have a max-
imum at zero? The set on n-jets of these functions at zero may be identiﬁed with
the set of (n + 1)-tuples of their Taylor coeﬃcients: a0,a1,...,an. Neutral n-jets

CENTENNIAL HISTORY OF HILBERT’S 16TH PROBLEM 313

are those for which a1 = ··· = an =0. The problem is algebraically solvable. For
more details, see [AI], §3.2.1.
Replacing polynomials by analytic functions in the previous deﬁnition, one gets
anotion of analytically solvable local problems.
The problem of topological description of phase portraits near singular points of
planar analytic vector ﬁelds is not algebraically solvable [I72], but a large part of it
really is [Du].
In more detail, a singular point is called characteristic if it has an orbit that
enters the point with a certain direction as t tends to plus or minus inﬁnity. A
singular point is called monodromic if the orbits wind around the point, and the
Poincar´e map is well deﬁned for this point.
An elementary theorem [AI], §5.3.1, claims that a non-ﬂat germ of a smooth pla-
nar vector ﬁeld at an isolated singular point is either characteristic or monodromic.
The results of [Du] imply that the following problems are algebraically solvable:
– distinguish monodromic and characteristic singular points;
– describe phase portraits near characteristic singular points.
Considering monodromic singular points, note that a center is a degeneracy of
inﬁnite codimension. Moreover, a monodromic singular point has a very simple
phase portrait modulo codimension inﬁnity: it is either a stable or unstable focus.
But the stability problem for monodromic singular points is algebraically unsolvable
[I72]. Yet there is a hope that the stability problem for planar vector ﬁelds is
analytically solvable. The approach is based on the Dulac theorem.
Indeed, a monodromic singular point, after a desingularization, is replaced by an
elementary polycycle with the same Poincar´e map. All of the previous theory may
be applied to the study of this map. Because of the speciﬁc origin of the polycycle,
its Poincar´e map ∆ is semiregular, and the principal term is linear [M92]:

∆(x)= Cx + o(x).

The quantity log C is called the generalized ﬁrst Lyapunov focus value. Even the
calculation of this value is a sophisticated problem. Diﬀerent formulas for it are ob-
tained in [BM], [GLMM], [M96], [MMa*], and [Sa]. Note that log C< 0(log C> 0)
implies stability (respectively, instability) of the complicated monodromic singular
point. Equality log C = 0 corresponds to a neutral case that requires calculation
of the next nonzero term of Dulac’s decomposition for ∆. The main problem is to
prove that all of these terms are expressed through analytic functions on the Taylor
coeﬃcients of the original germ, and to ﬁnd an algorithm for the calculation of the
subsequent terms in Dulac’s series for ∆. This would give a complete solution to
the stability problem for planar vector ﬁelds.

§4. Normal forms

According to a principle going back to Poincar´e, instead of trying to solve a
diﬀerential equation (which is usually impossible), one should try to make a coor-
dinate change that simpliﬁes the equation. Depending on the class of the change,
diﬀerent branches of the theory occur. We will deal with three of them: formal,
smooth and analytic.
The results of Sections 4.1 and 4.2 are classical [A], [Bo79] and are included for
the sake of completeness. A survey of the results of the last two decades starts at
4.3.

314 YU. ILYASHENKO

4.1. Equivalence and orbital equivalence for germs of vector ﬁelds. Let
H be a germ of a diﬀeomorphism at 0 having ﬁxed point 0,v be a germ of a vector
ﬁeld at 0, and w be its image under H. Then
∂H
∂x v = w ◦ H.(4.1)

This motivates the following.

Deﬁnition 4.1. Germs of vector ﬁelds v and w at zero are called equivalent if
there exists a germ of a diﬀeomorphism H with ﬁxed point zero such that (4.1)
holds. If H is smooth or analytic, then v and w are called smoothly, respectively
analytically, equivalent. Relation (4.1) makes sense on a formal level when v, w and
H are formal Taylor series. In this case v and w are called formally equivalent.

Two vector ﬁelds that diﬀer by a nonzero functional factor have the same phase
portraits.

Deﬁnition 4.2. Germs of vector ﬁelds v and w are called orbitally equivalent if
there exists a germ of a diﬀeomorphism H and germ of a nonzero function f such
that ∂H
∂x v = f · w ◦ H.(4.2)

Orbital formal, smooth and analytic equivalence are then deﬁned as in Deﬁnition
4.1, with (4.1) replaced by (4.2).

4.2. Resonant normal forms. Consider a germ of an analytic vector ﬁeld at a
singular point. One of the principal steps of local analysis is to compare the germ
with its linear part. Poincar´e was the ﬁrst to study the question: when may a
germ of a vector ﬁeld be transformed to its linear part by an analytic coordinate
change? He discovered the obstacles that occur even on the formal level, the so
called resonant relations or resonances.

Deﬁnition 4.3. Consideragerm v of an analytic vector ﬁeld at 0 in R
n with linear
part A. Let λ be the spectrum of A : λ =(λ1,...,λn). The tuple λ and the germ
v are called resonant if there exists k ∈ Z
n
+,k1 + ··· + kn ≥ 2, such that

λj =(λ, k)(4.3)

for some j ∈{1,... ,n}. Relation (4.3) is called a resonance.

Theorem 4.1 (Poincar´e). A nonresonant germ of an analytic vector ﬁeld is for-
mally equivalent to its linear part.

A natural question of whether this equivalence is analytic arises. This is one
of the famous problems that determined the development of normal forms theory
during more than a century. The ﬁrst major contributions were done by Poincar´e,
the latest ones by Yoccoz and Perez-Marco [Y], [P-M].
In the resonant case, some nonlinear terms cannot be eliminated even by a formal
coordinate change.

Deﬁnition 4.4. Let Az be a linear vector ﬁeld in Cn with A a matrix in the Jordan
normal form. Let λ =(λ1,... ,λn) be its spectrum. The vector monomial zk ∂
∂zj is
called a resonant term, with respect to A, if resonant relation (4.3) holds for these
particular k and j.

CENTENNIAL HISTORY OF HILBERT’S 16TH PROBLEM 315

Theorem 4.2 (Resonant normal forms theorem). Any germ of an analytic vector
ﬁeld at a singular point 0 in Cn is formally equivalent to a germ with linear part
Az having the Jordan normal form, and all nonlinear terms being resonant with
respect to A.

Particular cases of this theorem were stated in [D]. In its general form it may be
found “between the lines” in [St], [C], and the ﬁrst explicit statement was published
in [B64]. In [A], it is called the Poincar´e-Dulac theorem.
Formal normal forms of elementary singular points in the plane admit further
simpliﬁcations. Singular points that may occur as vertices of a polycycle which
admits the monodromy transformation are of special interest. They are of three
kinds: nonresonant saddles, resonant saddles and saddle-nodes.

Theorem 4.3. The following isolated elementary singular points of analytic vector
ﬁelds have the following formal orbital normal forms:
- nonresonant saddle:
 w = x ∂
∂x − λy ∂
∂y ,λ > 0,(4.4)

where λ/∈ Q;
- resonant saddle:

w = x(1 ± uk

1+ auk ) ∂
∂x − p
q y ∂
∂y ,u = x
pyq,p > 0,q > 0,(4.5)

where p and q are coprime; or (4.4) with λ = p
q ;
- saddlenode:
 w = ± x
k+1

1+ axk ∂
∂x − y ∂
∂y .(4.6)

4.3. Smooth orbital normal forms for elementary singular points. Ana-
lytic normal forms for resonant saddles and saddle-nodes are much more compli-
cated than formal ones; see Section 4.6 below. In the early 70s, Brjuno suggested
that the smooth classiﬁcation may be much simpler than the analytic one. Indeed,
the smooth orbital classiﬁcation of elementary singular points coincides with the
formal one.

Theorem 4.4. For the germs of planar analytic vector ﬁelds of the type saddle
or saddle-node, the formal orbital normal forms of Theorem 4.3 coincide with the
smooth ones.

This theorem may be extended to all of the elementary singular points, but we
do not need it for the cases of nodes, foci and centers. Moreover, Theorem 4.4
holds true for smooth germs that do not belong to a set of inﬁnite codimension.
It appears that smooth orbital normal forms of elementary singular points may be
integrated in elementary functions [Bo85]. In particular, this holds for the normal
forms (4.4)—(4.6). This is obvious for (4.4) and (4.6). For (4.5), this integrability
is derived as follows. The derivative of u along the vector ﬁeld (4.5) is

˙u = puk+1(1 + auk)
−1.

Hence, system (4.5) implies a system for (u, y), with the variables decoupled, and
thus is integrable.

316 YU. ILYASHENKO

Therefore, any property of saddles and saddle-nodes that persists under a smooth
coordinate change may be checked by a straightforward calculation. For instance,
the following statements hold.

Lemma 4.1. A correspondence map for a saddle of a planar analytic vector ﬁeld
is semiregular.

Lemma 4.2. A correspondence map for an isolated saddle-node of a planar ana-
lytic vector ﬁeld is either a composition

∆c = f0 ◦ h, f0 = e− 1
x ,(4.7)

where h is semiregular, or inverse to this composition.

Both lemmas hold true for the normal forms (4.4), (4.5), and (4.6). A smooth
coordinate change preserves the class of semiregular maps. This proves Lemma 4.1.
As explained in the next subsection, a smooth coordinate change preserves the class
of maps (4.7) which are named ﬂat-semiregular. This proves Lemma 4.2.
Theorem 4.4 is the result of a long development of the theory of smooth normal
forms outlined at the end of this subsection. Singular points whose eigenvalues
have nonzero real part are called hyperbolic, of which saddles are a particular case.

Theorem 4.5 (Sternberg’s theorem) [St]. A germ of a smooth vector ﬁeld at a
nonresonant hyperbolic singular point is smoothly equivalent to its linear part.

This theorem immediately implies Theorem 4.4 for nonresonant saddles.

Theorem 4.6 (Chen’s theorem) [C]. Suppose that two germs of smooth vector
ﬁelds at a hyperbolic singular point are formally equivalent; then they are smoothly
equivalent.

An analog of Theorem 4.3 for normal forms with respect to formal equivalence,
instead of orbital formal equivalence, provides a polynomial formal normal form,
say W, for a resonant saddle. By Chen’s theorem, the original germ is smoothly
equivalent to W. A short calculation shows that W is orbitally equivalent to (4.5).
This proves Theorem 4.4 for resonant saddles.
A general approach to prove a statement like “formal equivalence implies smooth
equivalence” is the following. Consider equation (4.1) for formal series:

∂ ˆH
∂x ˆv =ˆw ◦ ˆH.(4.8)

Here ˆv and ˆw are formal series for smooth vector ﬁelds v and w, and ˆH is a formal
series for a coordinate change.
By the Borel theorem, there exists a smooth germ H of a coordinate change at
zero such that its formal Taylor series coincides with ˆH. For this H
( ∂H
∂v v) ◦ H −1 − w = R

with R ﬂat at 0; i.e. the formal Taylor series of R is 0. Hence, v and w are smoothly
equivalent modulo a ﬂat correction. This ﬂat correction is then killed by making
use of the homotopy method. This last step relies on speciﬁc properties of v and w
and constitutes the most involved part of the proof.
Sternberg and Chen’s theorems, as well as the last claim of Theorem 4.4, may
be proved in this way. Orbital normal forms of saddle-nodes were discovered by
Bogdanov [Bo79]; the detailed proof of Theorem 4.4 may be found in [I85].

CENTENNIAL HISTORY OF HILBERT’S 16TH PROBLEM 317

4.4. Sketch of the proof of Dulac’s theorem. The modern proof of Dulac’s
theorem 3.2 may be presented as follows. An arbitrary polycycle may be replaced
by an elementary one with the use of the Desingularization Theorem. The Poincar´e
map ∆ of this modiﬁed polycycle may be decomposed as a product of correspon-
dence maps for saddles and saddle-nodes; see Section 3.5. Denote this decomposi-
tion by ∆. If the number of the maps f0 : x ↦→ exp(1/x) in this decomposition is
larger than that of f −1
0 , then the map is ﬂat. In the opposite case it is inverse to
ﬂat.
If the number of factors f0 and f −1
0 in the composition ∆ is the same, then the
map ∆ is semiregular.
Indeed, semiregular germs form a group. This is a straightforward consequence
of the deﬁnition and is proved in the same way as Lemma 3.3. Hence, ∆ may
be shortened to a composition where the semiregular maps f0 and f −1
0 alternate.
After a cyclic permutation of factors (which corresponds to a correct choice of the
cross-section to the polycycle) one may achieve the following property: for any k,
the product of the ﬁrst k factors (from the right) in the composition ∆ contains
no fewer entries f0 than f −1
0 . Let us combine the terms of this modiﬁed ∆ in the
following way. Open a bracket before any f −1
0 and close a bracket after any f0. The
most intrinsic brackets contain a product

h1 = f −1
0 ◦ h ◦ f0(4.9)

with h semiregular.

Lemma 4.3. The product (4.9) is semiregular.

Lemma 4.3 allows us to shorten the decomposition of ∆ replacing (4.9) by one
semiregular factor. This proves Dulac’s theorem by induction in the number of
factors of the above modiﬁed decomposition for ∆.
Thus Dulac’s theorem is proved, modulo Lemma 4.3. The theorem is based on
the Desingularization Theorem 3.6, which is valid in the smooth case as well, and
on Theorem 4.4 for smooth normal forms. Hence, it is in fact a statement from
the smooth, rather than analytic, theory and cannot imply the Nonaccumulation
Theorem, which is wrong in the smooth case.
We can now verify the claim used in the proof of Lemma 4.2 above. Consider a
smooth coordinate change g :(R+, 0) → (R+, 0) applied to a ﬂat-semiregular germ
(4.7). The result is

∆1 = g−1 ◦ f0 ◦ h ◦ g = f0 ◦ (f −1
0 ◦ g−1 ◦ f0) ◦ (h ◦ g).

The product in the ﬁrst parenthesis is semiregular by Lemma 4.3; the second one
is semiregular by Lemma 4.1. Hence, the germ ∆1 is ﬂat-semiregular, as ∆c was.

Proof of Lemma 4.3. The calculation below is very simple, yet rather surprising. It
shows that the asymptotic series (3.1) for h1 depends on the principal power term
of the map h only. All the other terms of the decomposition for h are forgotten, or,
better to say, determine the ﬂat terms of the composition (4.9). We do not study
these ﬂat terms in detail, because they do not enter the asymptotic series ˆh1 for
h1.
To write down the latter series, denote by cx
ν the principal power term of h.
Then h = cx
ν (1 + o(x
ε)) for some ε> 0. Hence,

h1 = −1/ log[ce− ν
x (1 + o(e− ε
x ))] = x
ν − x log c + o(e− ε
x ).

318 YU. ILYASHENKO

Therefore, h1 is semiregular, ˆh1 being a Taylor series with the sum x/(ν − x log c).

4.5. Normal forms for local families and their applications. For the needs
of bifurcation theory, normal forms for germs of vector ﬁelds depending on pa-
rameters are required. In order to get the ﬁrst idea of what the answer may be,
one can apply the formal theory. An unfolding of a germ ˙x = v(x) is a family
˙x = w(x, ε),w(x, 0) = v(x). Adding ˙ε = 0 transforms the family into a single
equation. The formal normal form for this equation (with ˙ε = 0 omitted) provides
a desired sample answer.
This approach provides orbital formal normal forms for the unfoldings of the
following germs (modulo degenerations of codimension inﬁnity):
- nonresonant saddle:
 wε = x ∂
∂x − λ(ε)y ∂
∂y ;(4.10)

- resonant saddle:

wε = x(1 ± uk

1+ auk + Pk−1(u, ε)) ∂
∂x − p
q y ∂
∂y ,(4.11)

u = x
pyq,p > 0,q > 0, and p/q irreducible. Here Pk−1 is a Weierstrass polynomial
in u with ε-dependent coeﬃcients: Pk−1(u, 0) ≡ 0;
- saddle-node:
 wε =(± x
k+1

1+ axk + Pk−1(x, ε)) ∂
∂x − y ∂
∂y ,(4.12)

where Pk−1 is a Weierstrass polynomial as above.
It appears that the above formuli have not only formal but geometric meaning.
The main problem is to ﬁnd the correct equivalence relation between the original
unfolding and its normal form. This cannot be an analytic or inﬁnitely smooth
equivalence. Indeed, even for an unfolding of a nonresonant saddle, the ratio of
eigenvalues admits rational values for a dense set in the parameter space. Hence,
arbitrarily close to ε = 0 resonant germs occur in the unfolding; even formally they
are not equivalent to a linear normal form.
The solution is suggested by the theory of ﬁnitely smooth normal forms. The
simplest fact of this theory is the ﬁnitely smooth version of Sternberg’s theorem
4.5.

Theorem 4.7 [St]. For any tuple λ =(λ1,...,λn) ∈ Cn, Re λj ̸=0, and any K
there exists N = N (K, λ) with the following property. Suppose that λ is not subject
to a resonant relation (4.3) with |k|≡ k1 + ··· + kn ≤ N. Then any germ of a vector
ﬁeld with the spectrum λ of its linear part is CK-equivalent to its linear part.

In other words, the higher the order of the resonance, the higher the order of
smoothness for the coordinate transformation to a normal form that “neglects” this
resonance, that is, does not contain a corresponding resonant term. For instance,
the smaller the neighborhood of zero in the parameter space of the unfolding of
a nonresonant saddle, the higher the order of resonances that occur in the family.
Hence, the order of smoothness that brings any germ of the unfolding to its linear
part is higher as well. This motivates the following:

CENTENNIAL HISTORY OF HILBERT’S 16TH PROBLEM 319

Deﬁnition 4.5. Two local families of vector ﬁelds at a point zero are ﬁnitely or-
bitally smoothly equivalent if, for any K, there exist two neighborhoods of zero in
the phase-and-parameter space such that the families are (orbitally) CK-smoothly
equivalent in these neighborhoods.

Roughly speaking, the smaller the domain of the families, the higher the smooth-
ness of the conjugacy between them.

Theorem 4.8 [IYa91]. Smooth unfoldings of smooth germs of planar vector ﬁelds
of the type saddle or saddle-node that do not belong to a codimension inﬁnity set of
degenerated germs are orbitally ﬁnitely smoothly equivalent to their formal normal
forms (4.10)-(4.12).

This theorem provides one of the key tools in the study of the Hilbert-Arnold
problem for vector ﬁelds with only elementary singular points; see Section 5 below.
In fact, [IYa91] provides all of the possible integrable normal forms for local families
of maps and vector ﬁelds. This gives an important tool for the study of nonlocal
bifurcations in arbitrary dimension. This approach is systematically applied in the
book [IL].
The paper [IYa91] summarizes a long development due to Belitski, Bogdanov,
Dumortier, Kostov, Samovol and Takens; see the references in [IYa91].

4.6. Nonlinear Stokes phenomena. There is no analogue of Theorem 4.4 in
the analytic category.
A nonresonant saddle is orbitally analytically equivalent to its linear part, pro-
vided that the ratio of eigenvalues λ has “good” arithmetic properties, that is,
cannot be too closely approximated by rational numbers. A delicate suﬃcient con-
dition on λ was found by Brjuno [B71], [B72]. In [Y], Yoccoz proved that this
condition is necessary as well.
The analytic classiﬁcation of resonant germs of vector ﬁelds is more complicated.
´Ecalle [E85] described invariants of this classiﬁcation in terms of resurgent functions.
Much earlier, Brjuno [B71], [B72] found necessary and suﬃcient conditions under
which formal equivalence implies analytic equivalence. These conditions are fulﬁlled
very rarely. For resonant saddles, they require that the orbital formal normal form
should contain no resonant terms, that is, coincide with (4.4). For saddle-nodes
these conditions require that the saddle-node should not be isolated; its orbital
formal and analytic normal form would be

˙x =0, ˙y = −y.

Therefore, for any orbital formal normal form (4.5), (4.6), there exist germs that
have this normal form but are not orbitally analytically equivalent.
Martinet and Ramis [MR82], [MR83] discovered functional moduli of the orbital
analytic classiﬁcation of germs of saddle-nodes and resonant saddles in the complex
plane. The origin of these moduli is the same as in the case of so called parabolic
ﬁxed points. The analytic classiﬁcation of germs of conformal maps at these points
is described below and provides an important tool for the proof of the Nonaccu-
mulation Theorem. This classiﬁcation was discovered independently by Malgrange
[Ma] and Voronin [Vo] with the use of quasiconformal mappings, and by ´Ecalle
[E81a], who used Borel-Laplace transforms.
Consider a germ of a holomorphic map (C, 0) → (C, 0) with linear part z :

f : z ↦→ z + αzk+1 + ..., α ̸=0.(4.13)

320 YU. ILYASHENKO

Figure 6. Phase portrait of (4.14) for k =2. Sectors mentioned
in the Sectorial Normalization Theorem. Diﬀerent radii are drawn
to distinguish the sectors.

The germs of this kind are called parabolic. The classiﬁcation problem is: when are
two parabolic germs analytically conjugated? (That is, there exists a biholomorphic
germ h :(C, 0) → (C, 0) such that h ◦ f1 = f2 ◦ h.)
The germ (4.13) is formally equivalent to the time-one shift map g along the
orbits of the equation
 ˙z = zk+1 + βz2k+1;(4.14)

β is the invariant of the formal classiﬁcation. It appears that formal series that
conjugate f and g diverge, as a rule. Yet, some geometry is related to these series.
To describe it, consider ﬁrst the phase portrait of (4.14). In the neighborhood
of zero it consists of 2k petals as shown in Figure 6. Consider a partition of a
punctured disk centered at zero into 2k equal sectors, one of them having the
positive ray as a bisector. Replace each of these sectors by a larger one having the
same bisector and the opening α ∈ ( π
k , 2π
k ). This covering of the punctured disk by
equal sectors is called a k-good covering; see Figure 6.

Sectorial Normalization Theorem 4.9. Consider a germ (4.13) with α =1
(this may be achieved by a rescaling) and a k-good covering of a small punctured
disk.
1. In any sector Sj of the k-good covering, there exists a map Hj = z+o(z),Sj →
C,Hj(z) → 0 as z → 0 that transforms f to its formal normal form g, the time
one shift along the orbits of (4.14).
2. The maps Hj and Hj+1 (j +1 is taken mod 2k) in the intersection of their
domains have a diﬀerence that decreases exponentially:

|Hj(z) − Hj+1(z)| < exp
 (
− C

|z|
k
 )
 .(4.15)

3. All of the maps Hj have the same asymptotic Taylor series at 0.

Statement 1 of this theorem was known even in the 19th century [Le].
The tuple of these maps
 H =(H1,...,H2k),(4.16)
 CENTENNIAL HISTORY OF HILBERT’S 16TH PROBLEM 321

each one deﬁned in its own domain, forms a normalizing atlas or anormalizing
cochain. Separate charts of this atlas were considered long ago; however the tran-
sition functions between these charts were considered only recently. They determine
the complete set of invariants of the analytic classiﬁcation of parabolic germs. These
transition functions range over a rich functional space [Vo], [Ma].
In general, resonant germs of maps on the line and of vector ﬁelds in the plane
generate a normalizing atlas for some covering of the punctured neighborhood of
the equilibrium point. The transition functions of this atlas also range over a rich
functional space. This eﬀect is called the nonlinear Stokes phenomena.For a
detailed exposition see [I93].
The sectorial normalization theorem describes a new kind of local object in
complex analysis, the so called functional cochains.

Deﬁnition 4.6. A tuple (4.16) is called a functional cochain provided that:
- any component Hj is holomorphic in a sector Sj of a k-good covering;
- subsequent diﬀerences Hj+1 − Hj satisfy (4.15) in their domains; and
-all Hj have the same asymptotic Taylor series at zero.

Normalizing cochains provide an important example of functional cochains. A
functional cochain forms not a tuple of disjoint components, but a single object.

Theorem 4.10 [IKh]. A functional cochain is uniquely determined by its formal
Taylor series.

This may be reformulated as a theorem of the Phragmen-Lindelof type.

Theorem 4.11. A functional cochain that decreases along (R
+, 0) faster than any
power of z is identically zero.

Functional cochains play a crucial role in the proof of the Nonaccumulation
Theorem, thus of the Finiteness Theorem 2.1.

4.7. Strategy of the proof of the Finiteness Theorem. The Finiteness The-
orem for Limit Cycles (Theorem 2.1) is reduced to the Nonaccumulation Theorem
3.1, as described in 3.1 above.
The beginning of the proof for the latter theorem is the same as for Dulac’s the-
orem. The polycycle under consideration is replaced by an elementary one with the
same Poincar´emap, ∆. This map is decomposed into a product of correspondence
maps of hyperbolic saddles and saddle-nodes. The ﬁrst ones are almost regular;
see Deﬁnition 3.3. The latter ones are ﬂat or inverse to ﬂat; see Lemma 4.2. The
following theorem is the analytic reﬁnement of this lemma.

Theorem 4.12. A ﬂat correspondence map of a real analytic saddle-node is a com-
position
 F = g ◦ f0 ◦ hk,a ◦ H.(4.17)

Here g is a germ of a holomorphic function, g(0) = 0,g′(0) > 0; f0 = e− 1
z , as
before;
 hk,a = kx
k

1 − akxk ln x
for some k ∈ Z,k > 1; a ∈ R; and H is a normalizing cochain for some parabolic
germ (4.13).

322 YU. ILYASHENKO

More details about H may be found in [I91], §0.4a. Composition with the func-
tional cochain H in (4.17) is considered on (R
+, 0) and deﬁned in the following way.
There are two components of H, say H1 and H2, deﬁned on the positive axes near
theorigin. Thegerm F has a decomposition (4.17) with H replaced by H1, and a
similar decomposition with H2; in the latter case, the holomorphic germ g should
be replaced by another holomorphic germ with the same 1-jet at zero. Hence (4.17)
encodes two diﬀerent decompositions of F into a product of well-deﬁned maps.
Theorem 4.13 shows that functional cochains appear in an unavoidable way in
the description of the Poincar´e map for elementary polycycles. Thus, the theory of
normal forms reduces the Nonaccumulation Theorem to a purely complex analytic
problem: prove that a composition of a ﬁnite number of maps from a certain class
cannot have an inﬁnite number of isolated ﬁxed points.
The Poincar´e maps under study have two characteristic features: First, they
are expressed through functional cochains. Second, as mentioned before, their
diﬀerence with the identity may be ﬂat. Moreover, it may decrease faster than a
tower of exponentials with an arbitrary number of stories. To show this, consider
a composition
 P = f −1
0 ◦ f −1
0 ◦ h ◦ f0 ◦ f0,

where h(x)= x + x
2 and f0 = e− 1
x , as in (4.9). The same calculation as at the
end of 4.4 implies:
 h1 = f −1
0 ◦ h ◦ f0 = x
1 − x log(1 + f0) ,

P = f −1
0 ◦ h1 ◦ f0 = x

1 − x log(1 − e− 1
x log(1 + f0 ◦ f0)) = x + O(e−e 1
x ).

Thus, P − x decreases as a double exponential. In the same way, for any n, a
composition of the same maps that diﬀers from the identity by a correction that
decreases faster than a tower of n exponentials exp(− exp ◦ exp ◦ ... exp 1
x )may be
constructed. Recall that f0 is a correspondence map for the simplest saddle-node
˙x = x
2, ˙y = −y, and for suitably chosen cross-sections. Now, the standard gluing
up techniques allow us to construct a polycyle of an analytic vector ﬁeld whose
Poincar´emap is equal to P above; see [I84].
The two features of the Poincar´e map mentioned above are the source of the
principal diﬃculties of the proof.
The proof uses special asymptotic series for the compositions under study. The
terms of these series do not oscillate. Hence, if the composition has an increment
with an inﬁnite number of zeros, then the asymptotic series for this increment is
zero. The Phragmen-Lindelof Theorem for cochains (much more sophisticated than
4.12) implies that the increment is identically zero. This approach is realized in
[I91].
An alternative approach to the theory of normal forms is suggested by ´Ecalle,
whocreated atheoryof resurgent functions [E81a], [E81b] and [E85]. Using this
theory, he gave another proof of the Finiteness Theorem [E92].

§5. Hilbert’s 16th problem and bifurcation theory

We begin with the main developments and problems of planar bifurcation theory,
followed by a brief survey of the fewnomial theory. This theory is one of the

CENTENNIAL HISTORY OF HILBERT’S 16TH PROBLEM 323

main sources for the solution of the Hilbert–Arnold problem for vector ﬁelds with
elementary singular points. A sketch of this solution forms the main body of this
section.

5.1. A brief survey of the planar bifurcation theory. Three major directions
may be distinguished in the development of this theory.
1. A detailed study of local bifurcations, that is, bifurcations near singular points
and periodic orbits, in families with a small number of parameters.
2. A detailed study of bifurcations of polycycles in families with a small number
of parameters.
3. The statement and proof of general results about bifurcations of planar vector
ﬁelds in families with an arbitrarily large number of parameters.
In the context, small numbers are 1, 2 and 3. The classical result in the ﬁrst
direction is the famous Andronov-Hopf bifurcation: generation of a limit cycle while
a singular point loses stability. The modern period in the theory is marked by a
breakthrough by Bogdanov and Takens, who studied the codimension two bifur-
cation of a singular point with nonzero nilpotent linear part [Bo76], [Bo77], and
[T]. Although local bifurcations of codimension three have been studied to a large
extent, [DRS] and [DRSZ], it seems absolutely hopeless to get a detailed description
for bifurcations in codimension 4.
Local bifurcations in planar systems with symmetries form another important
part of the theory. Families of this type occur as a result of factorization of generic
multidimensional families that describe loss of stability by spacial periodic solutions
and codimension two local bifurcations in R
3 and R4, [A], [Ho], [Z83], and [Z87].
At present, the local bifurcation theory for generic families of planar vector
ﬁelds is mostly completed; see [AAIS] and [CLW] and the references therein. The
latter monograph contains a complete description of the main results in the local
planar bifurcation theory obtained in the seventies and eighties, as well as a rich
bibliography up to the beginning of the 90’s. Therefore, we have mentioned above
only a few references.
Study of local bifurcations of polynomial vector ﬁelds is mostly related to per-
turbations of singular points of the type center. The famous theorem of Bautin
[Ba] claims that a perturbation of a center in a family of quadratic vector ﬁelds
can generate no more than 3 small amplitude limit cycles. A modern proof of this
theorem may be found in [Ya95].
Classical results in the theory of nonlocal bifurcations are due to Andronov and
deal with bifurcations of a separatrix loop and a homoclinic orbit of a saddle-node;
see Figure 7a, b.
The list of all of the polycycles that may occur in typical two and three parameter
families (the so called Kotova zoo) was obtained only recently; see [KS]. Cyclicity
of elementary polycycles from this list is investigated in [Tr] and summarized in
[IK]. Bifurcations of codimension two polycycles were studied in [DRRa]; see also
[R98] and the references therein. The theory will be almost completed when the
bifurcations of all of the polycycles from the Kotova zoo are described; this is far
from ﬁnished at present.
The general multi-parameter theory is in its initial stage. The global program
of research in this ﬁeld has not yet been proposed. Arnold in [AAIS] asked whether
for any number of parameters k, the list of sample bifurcations that may occur in
generic k-parameter families is ﬁnite? The answer was found to be negative, even

324 YU. ILYASHENKO(b)(a)(c)
Figure 7. (a) Bifurcation of a separatrix loop. (b) Bifurcation of
a homoclinic orbit of a saddle-node. (c) “Lips” ensemble.

for k =3, in [KS]. The reason is that a codimension three degeneracy may give
rise to a continuous family of polycycles, the so called “lips” ensemble; see Fig. 7c.
For any number L, the degenerated vector ﬁeld may be constructed in such a way
that the bifurcation of this ﬁeld in a typical three-parameter family would generate
more than L limit cycles. In fact, more than L polycycles of the family are involved
in a bifurcation when the parameter ranges over an arbitrary small neighborhood
of its critical value. Any particular polycycle in the family has cyclicity no greater
than 3.
Some bifurcations in multi-parameter families were studied in [L], [R86], [Mo],
and [JKM].
The Hilbert-Arnold problem, together with Problem 9 from §2, seems to be a
major one in the ﬁeld. A solution of the Hilbert-Arnold problem for elementary
polycycles, [IYa95a], [IK], and [K*], is sketched below beginning with 5.3.

5.2. The 121-program of Dumortier-Roussarie-Rousseau. As is mentioned
in §2, the ﬁnite cyclicity problem is closely related to Hilbert’s 16th problem. In
particular, the conjecture below implies the existence of H(2), an upper bound for
the number of limit cycles of quadratic vector ﬁelds in the plane.

Conjecture [DRR]. Any polycycle met in a family of quadratic vector ﬁelds in the
plane
 ˙x = P2(x, y), ˙y = Q2(x, y)(5.1)

has but a ﬁnite cyclicity.

Quadratic vector ﬁelds are relatively simple, amidst other polynomial vector
ﬁelds. For instance, any closed phase curve of such a ﬁeld is convex and contains
no more than one singular point inside [Co]. It is realistic to try to list all of
the polycycles that may occur for quadratic vector ﬁelds and to prove their ﬁnite
cyclicity. The ﬁrst step in this program was done in [DRR], where a complete list of
121 polycycles that may occur for quadratic vector ﬁelds is presented. In a series of
works, [DRR], [DMR], [GR], [RSZ], and [DIR], ﬁnite cyclicity of about 80 of them
was proved. There is hope that the existence of H(2) may be proved in this way,
but it is clear that even for H(3) this approach is unrealistic.

CENTENNIAL HISTORY OF HILBERT’S 16TH PROBLEM 325

5.3. The cyclicity equation for elementary polycycles. In the rest of the
section, a sketch of the proof of Theorems 3 and 4 is given. It is based on the
fewnomial theory of Khovanskii [Kh91], surveyed in the next subsection.
Let γ be a polycycle that occurs in a generic k-parameter family of planar vector
ﬁelds. Let ε be the multi-dimensional parameter of the family; ε = 0 corresponds
to the equation with the polycycle γ.
Consider a parameter depending on the Poincar´emap P (x, ε) of the polycycle
γ. The cyclicity equation concerns ﬁxed points of this map:

P (x, ε)= x.(5.2)

Replace this equation by a system with a larger number of equations, but a simpler
left hand side. To do that, let us separate any vertex Oj,j =1,... ,n, of the
polycycle by two cross-sections Γ+
j and Γ−
j so that the orbits enter a neighborhood
of Oj through Γ
+
j and exit through Γ
−
j . Let ∆j :Γ+
j → Γ−
j be a correspondence
map along the orbits. The polycycle is elementary; hence its vertices are saddles
or saddle-nodes. Unfoldings of those may be expressed in normal forms, according
to Theorem 4.9. The correspondence maps ∆j,ε for the equations of these families
are, in a sense, standard.
On the other hand, let fj,ε :Γ−
j → Γ+
j+1 be the maps along the regular parts of
the orbits. Nothing may be said about these maps except for the statement that
in generic families they satisfy some genericity conditions.
Let xj and yj be the charts on Γ+
j and Γ−
j , respectively. Limit cycles generated
by γ in the family under consideration cross all of the segments Γ
±
j for ε small. The
intersection points xj ∈ Γ+
j ,yj ∈ Γ−
j satisfy the system:

yj =∆j,ε(xj ),xj+1 = fj,ε(yj),(5.3)

which is called the cyclicity equation, as in the heading of this subsection.
The number of vertices of a polycycle that occurs in a typical k-parameter family
cannot be greater than k. The complexity of these singular points is, in a sense,
bounded by k as well. Therefore, families of functions ∆j,ε in (5.3) may be taken
out of some “standard list” depending on k only and provided by Theorem 4.9.
Yet these functions are transcendental, and therefore rather diﬃcult to deal with.
In 1988, Yakovenko proposed using the fewnomial theory of Khovanskii in order to
attack system (5.3). For the ﬁrst time, the fewnomial theory was applied to the
study of limit cycles by Moussu and Roch [MRo].

5.4. Sketch of the fewnomial theory [Kh91]. The general goal of the fewnomial
theory is to estimate the number of solutions to a system through the complexity
of the system itself. For instance, a real polynomial in one variable has no more
positive roots than the number of the sign alternations in its coeﬃcients, provided
that the terms are ordered by their degree (Descartes’ rule). Therefore, the number
of positive roots of a polynomial is no greater than the number of its terms, no
matter what the degree is. This motivates the name of the theory.
The theory is based on the elimination procedure for functional-Pfaﬃan equa-
tions. The simplest illustration is the following. Let ω = Adx+Bdy be a polynomial
one-form. Denote by γ a curve that divides the plane in two parts, satisﬁes the
equation ω =0, and does not contain singular points of the form ω deﬁned by the
equation A = B =0. Let l = {F =0} be a closed algebraic curve. The problem is
to estimate the number of intersection points of l and γ.

326 YU. ILYASHENKO

Suppose for simplicity that the intersections are transversal, since the general
case may be reduced to this one. Let us choose any orientation of l. Between any two
intersection points of l and γ which are subsequent in the sense of this orientation,
the sign of the value of ω on the tangent vectors to l changes. Therefore, by Rolle’s
theorem, there is at least one contact point in between, namely a point where ω =0
on a tangent vector to l. At this point, forms ω and dF are linearly dependent:
ω ∧ dF =0. Therefore

#{γ ∩ l}≤ #{F =0, ∗(ω ∧ dF )= 0},(5.4)

where ∗ is deﬁned by the formula: ω ∧ dF = ∗(ω ∧ dF )dx ∧ dy. The system in
the right hand side of (5.4) is polynomial, and the number of its solutions may be
estimated from above by the Bezout theorem.
Consider now a system that contains transcendental functions, which are solu-
tions to polynomial diﬀerential equations. Instead of these transcendental functions,
the corresponding diﬀerential equations may be considered. This gives a so called
functional-Pfaﬃan system. By means of the elimination procedure based on the
idea described above, the latter system may be replaced by a functional one with
a greater or equal number of solutions. If this new system is polynomial, then the
number of its solutions may be estimated from above by the Besout theorem.
This approach may be applied in a much broader context than the example
above. The application of the fewnomial theory to system (5.3) is carried on in the
following way.
The theory of normal forms, namely Theorem 4.9, provides a ﬁnite list of func-
tions ∆j,ε that may occur in system (5.3) for any ﬁxed number of parameters in
the corresponding family. Any function of this list is a solution to a polynomial
diﬀerential equation. For instance, a nonresonant saddle has a correspondence map
y = x
λ(ε). This function is a solution to the equation xdy − λ(ε)ydx =0.
Therefore, making use of Theorem 4.9, we may replace system (5.3) by a func-
tional-Pfaﬃan system with no smaller number of solutions:

ωj(xj,yj,ε)=0,xj+1 = fj,ε(yj).(5.5)

Here ωj are polynomial 1-forms on xj,yj with coeﬃcients depending on the param-
eter ε. Functions yj − ∆j(xj ,ε) satisfy the equations ωj =0. Forms ωj are taken
from a ﬁnite list depending on k only.
Using the Khovanskii elimination procedure, system (5.5) may be reduced to the
following one:
 P ◦ jmf = a.(5.6)

In this system P is a polynomial map from some ﬁnite, k-depending, list,

f (y)= (f1,ε(y1),...,fn,ε(yn)),(5.7)

and m is a positive integer depending on k. The tuple f is generic in the class of
maps (5.7) where fj,ε, for ε ﬁxed, depends on yj only. This class is denoted by C
for Cartesian. The number m in (5.6) depends on k, jmf is the m-jet of f at zero,
f is regarded as a vector function on y, and the jet is taken with respect to y; a is a
constant vector. The reduction procedure guarantees that the number of solutions
of system (5.5) is no greater than that of (5.6), provided that a ranges in a special
funnel-like set with a vertex 0. Now the main problem is to estimate the number of
solutions of (5.6).

CENTENNIAL HISTORY OF HILBERT’S 16TH PROBLEM 327

5.5. Chain maps and an upper estimate of E(k). We look for the upper
bound on the number of small solutions to (5.6), with small a. This is the same as
the upper bound for the number of small pre-images of a small image under a chain
map P ◦ jmf, with P being a ﬁxed polynomial map and f a generic map from the
class C. The smallness of a, together with the further requirements on a, may be
fulﬁlled by a careful application of the Khovanskii elimination method.
The existence of the bound mentioned above was proved in [IYa95a]. An explicit
estimate was recently obtained by Kaloshin, [IK] and [K*].
The key idea of Kaloshin that allowed him to estimate the number of solutions
of (5.6), hence to get an upper estimate of E(k), is the following. Because of
the local character of equation (5.6) and the genericity of f, the jet jmf may be
replaced by a linear map without decreasing the number of solutions. This reduction
heavily relies on a contribution to the stratiﬁcation theory for real algebraic sets
carried on in [K*]. Hence, the number of solutions of (5.6), according to the Besout
theorem, is bounded from above by the product of degrees of the components of
P. These degrees were well controlled through the parameter k beginning with the
list of systems (5.3), and all through the application of the fewnomial theory. The
estimates of these degrees imply the upper estimate for E(k): E(k) ≤ 225k2 ;see
Theorem 4 in Section 2.
The key idea, mentioned above, may be formalized in the following way.

Theorem 5.1 (Besout theorem for chain maps) [K*]. Consider an arbitrary poly-
nomial map P : RN → Rn with max rank P = n and P (0) = 0. There exists the
following tuple, depending on P only:
• positive integers l and M ;
• an algebraic subset Σ in the jet space J l(Rn, RN ).
The tuple has the following property. Let Kδ,M be a funnel-like domain

Kδ,M = {a ∈ Rn|0 <a1 <δ, 0 <aj+1 < (a1 ...aj)
M ,j =1,... ,n − 1}.

Then for any map f :(Rn, 0) → (RN , 0) such that the l-jet extension of f is
transversal to Σ, there exist a neighborhood U of 0 in Rn and a positive δ such that
the number of solutions of the equation P ◦ f (x)= a, x ∈ U, for any a ∈ Kδ,M is
no greater than the product of the degrees of the components of P.

A stronger version of this theorem, with f replaced by jmf, and genericity
changed to genericity in the class C (see (5.7)) is also proved in [K*]. It provides
the above explicit estimate of E(k).

§6. Restricted versions of the Hilbert 16th problem

Since the original Hilbert problem continues to be very persistent, some simpli-
ﬁed versions should be considered ﬁrst. An incomplete list of the names of these
problems is:
- The Abel equation;
- The Lienard equation;
- The inﬁnitesimal Hilbert problem;
- The Hilbert-Arnold problem.
The latter two problems were stated above; the ﬁrst two are presented below.

328 YU. ILYASHENKO

6.1. The Abel equation. This is an equation on the cylinder polynomial in y
and periodic in x :
 dy
dx = yn +
 n−1∑

0 aj(x)yj,y ∈ R1,x ∈ S1;(6.1)

the coeﬃcients aj are only continuous, unless explicitly stated.
The general problem is to get an upper bound on the number of limit cycles of
(6.1). For small values of n it may be done in terms of n only.

Theorem 6.1 [Sh]. For n ≤ 3, the number of limit cycles of (6.1) is no greater
than n.

The explosion comes at n =4 :

Theorem 6.2 [LN80]. For degree n ≥ 4, the Abel equation may have an arbitrary
number of limit cycles.

Moreover, there are no speciﬁc restrictions on the Poincar´e map of Abel equa-
tions.

Theorem 6.3 [P]. Any homeomorphism of a segment may be uniformly approxi-
mated by a Poincar´e map for a suitable Abel equation.

Therefore, in order to get upper bounds of the number of limit cycles, one should
make some hypothesis on the coeﬃcients.

Problem 6.1. Find an upper bound on the number of limit cycles of the Abel
equation (6.1) in which the coeﬃcients aj are trigonometric polynomials of degree
no greater than m. The bound should be expressed through n and m only.

This problem is unsolved even for m =1.

6.2. The Lienard equation. In his list of problems for the 21st century, Smale
[S] included Hilbert’s 16th problem. As a simpliﬁed version, he mentioned the
Lienard equation

˙x = y − Fn(x), ˙y = −x, Fn(x)= x
n +
 n−1∑

1 ajx
j,n odd.(6.2)

The free term of Fn may be taken to be 0 by means of translation along the y axis.
The only singular point is zero; hence, there is only one nest of limit cycles.
Moreover, there are no limit cycles near inﬁnity. Indeed, an elementary study
going back to [LMP] shows that the point (1 : 0) at inﬁnity is of the type “repelling
node”. Hence, there are parabolic sectors with their vertices at this point at inﬁnity
that repell all of the orbits; see Figure 8.

Problem 6.2. Find an upper bound on the number of limit cycles for the Lienard
equation (6.2) through the degree n.

As a commentary, we quote here a paragraph of Smale [S], with some notation
slightly changed, in order that it agree with the previous text.
“More generally, it can be easily shown that all the solutions of (6.2) circle around
the unique equilibrium at (0, 0) in a clock-wise direction. By following these curves,
one deﬁnes a ‘Poincar´e section’, P : R+ → R+ where R+ is the positive y-axis. The
limit cycles of (6.2) are precisely the ﬁxed-points of P. In various talks I raised the

CENTENNIAL HISTORY OF HILBERT’S 16TH PROBLEM 329

Figure 8. Poincar´e map and repelling sectors for the Lienard equation.

question of estimating the number of these ﬁxed-points (via some new kind of ﬁxed-
point theorem?). In response, Lins, de Melo, and Pugh (1977) found examples with
n−1
2 diﬀerent limit cycles and conjectured this number n−1
2 for the upper bound.
Still no upper bound of the form (deg F )
d has been found. Because P is analytic,
(6.2) has a ﬁnite number of limit cycles for each F.”
It should be mentioned that no upper bound as any function of n has been found
for the number of limit cycles of the Lienard equation (6.2).

6.3. Estimates with extra restrictions. A ﬁrst step in the study of simpliﬁed
versions of Hilbert’s 16th problem may be a solution to the restricted versions of
these simpliﬁed problems. For the Abel and Lienard equations, the restriction is
the magnitude of the coeﬃcients, and this magnitude enters the upper bound. For
the inﬁnitesimal Hilbert problem, this is a restriction to the polynomial H. For the
Hilbert-Arnold problem, this is the requirement that all of the singular points of
the equation are elementary.
These restricted versions are now solved. The solution of the latter problem was
discussed in Section 5. The solution of the restricted inﬁnitesimal Hilbert problem
is discussed in the next section. For the Abel and Lienard equations, the solutions
look like the following.

Theorem 6.4 [I00]. Consider the Abel equation (6.1) with the restriction

|aj(x)| <C.(6.3)

The number L of limit cycles of equation (6.1) satisfying (6.3) has an upper bound:

L ≤ ee
C3n .

Theorem 6.5 [IP*]. Consider the Lienard equation (6.2) with the restriction

|aj| <C, C ≥ 4.(6.4)

The number L of limit cycles of equation (6.2) satisfying (6.4) has an upper bound:

L ≤ ee
C14n .

The estimates from these theorems do not pretend to be realistic. Yet these are
the only known estimates of their kind.

330 YU. ILYASHENKO

The approach to the study of Abel and Lienard equations, as well as of Abelian
integrals, is based on a generalization of the Jensen inequality that is presented in
the next subsection.

6.4. The Growth-and-Zeros Theorem for holomorphic functions. Con-
sider two sets, U and K, located in C or in a Riemann surface. Suppose that
U is simply connected and K ⊂ U is compact and path connected. Let f be a
holomorphic function in ¯U. The Bernstein index of f with respect to U and K is

BU,K(f )= log max ¯U |f |
maxK |f | .

Theorem 6.6 [IYa96]. There exists a geometric constant γ(U, K) such that

#{z ∈ K|f (z)= 0}≤ γ(U, K)BU,K(f ).

The value γ(U, K) may be taken as eρ, where ρ is the diameter of K in the Poincar´e
metric of U.

The diameter ρ may be estimated in terms of Euclidean, rather than Lobachevski,
geometry. Indeed, let the intrinsic distance between two points in K be the inﬁmum
of the lengths of paths in K that connect these points. Let the intrinsic diameter of
K, dint(K) be the diameter of K in the sense of the intrinsic distance. The deﬁnition
works for K locatedbothin C andina Riemannsurface over C; in the latter case
the metric is lifted from C to the Riemann surface. Let ε be the gap between K
and ∂U in the sense of the Euclidean distance lifted from C :

ε = d(K, ∂U ).

Theorem 6.7 [I00], [GI*]. Theorem 6.6 holds with

γ(U, K)= e
 2dint (K)
ε .

6.5. Applications to the Abel and Lienard equations. Bounds (6.3) and
(6.4) allow one to specify the domain of the Poincar´emap U and the set K that is
intersected by any limit cycle of equation (6.1) or (6.2). In more detail, let {x =0}
be a cross-section and P : y ↦→ P (y)bethe Poincar´e map, whenever deﬁned. The
Growth-and-Zeros Theorem will be applied to the diﬀerence f = P − y, for which
zeros correspond to limit cycles.
For the Abel equation, estimate (6.3) implies that equation (6.1) is similar to
˙y = yn outside of the segment σ = {|y|≤ 2C +1}. In more detail, all solutions with
initial conditions on Γ \ σ escape to inﬁnity before they make one circuit around the
cylinder in forward or backward time. Therefore, it is possible to locate a segment
K ⊂ σ on which the Poincar´e map of (6.1) is well deﬁned and such that all of the
limit cycles of (6.1) cross K. The length of K is of order C. Standard techniques
based on the Gronwall inequality provide an extension of the Poincar´e map of (6.1)
to an ε-neighborhood of K in C, with ε =exp(−C2n). The increment f of this
extended map is of order C as well. Thus, the Bernstein index, BU,K(f ), is of order
1, and the geometric constant γ is of order eO(C)ε
−1. This factor γ becomes the
triple exponent from Theorem 6.4, after replacing O(C)ε−1 by the larger quantity
exp C3n.
The approach to the Lienard equation is similar. The estimate (6.4) provides an
estimate of the size of repelling sectors at inﬁnity. They are

D+ = {(x, y) ∈ R2|x ≥ 2C, |y|≤ x
2},

CENTENNIAL HISTORY OF HILBERT’S 16TH PROBLEM 331

D− = {(−x, y) ∈ R2|(x, y) ∈ D+};

see Fig. 8. After this, the strategy for the Lienard equation is similar to that for
the Abel equation, with more obstacles to be overcome.
The problem to be solved is to get rid of restrictions (6.3) and (6.4). Restriction
(6.3) should be replaced by an assumption as in Problem 6.1. Restriction (6.4)
should be simply omitted. It seems plausible that this may be done by means of
the theory of complex foliations presented in Section 8, below.

§7. Infinitesimal Hilbert’s 16th problem

The statement of the problem is given in Section 2. It is recalled and generalized
below.

7.1. Statement of the problem. Consider, as before, a real polynomial H
of degree n + 1 in the plane, and let γ(t) be a family of its ovals; see Fig. 2.
Let ω = Adx + Bdy be a polynomial 1-form with arbitrary degree m coeﬃcients.
Consider the integral
 I(t)= ∫

γ(t) ω.(7.1)

Problem 7’. Find an upper bound V (n, m) on the number of isolated real zeros of
the integral (7.1).

Only the case n ≥ m is important for the Hilbert 16th problem. Indeed, in this
case the perturbation
 dH + εω =0(7.2)

corresponds to a polynomial vector ﬁeld of degree n. Yet the dependence of V (n, m)
on m is of special interest; see Section 7.4 below.
Recall that the number of simple zeros of the Abelian integral (7.1) is no greater
than the number of limit cycles of the perturbation (7.2). The converse relation is
discussed in 7.8.

7.2. The Exactness Theorem and free location of limit cycles.

Deﬁnition 7.1. A complex polynomial H of degree n + 1 is called ultra-Morse if
it has n2 nondegenerate critical points with diﬀerent critical values and its highest
homogeneous form h, after a linear coordinate change, if necessary, is a product of
a constant with n + 1 diﬀerent linear factors of the form y − ax.

The assumption on critical points and values deﬁnes a Morse polynomial; the
latter requirement deﬁnes a narrower class; this motivates the term. Ultra-Morse
polynomials form a Zariski open set in the space of all polynomials of given degree.

Theorem 7.1. (Exactness Theorem) [I69a], [I69b] and [Pu].In (7.1),let {γt} be
a family of ovals of a real ultra-Morse polynomial H, of degree n +1 ≥ 3, and ω
be a polynomial 1-form of degree no greater than n. If I(t) ≡ 0, then the form ω is
exact: ω = df for some polynomial f.

The Exactness Theorem for rational H, instead of polynomial one, is proved in
[Muc].
Theorem 7.1 implies that the linear space of integrals (7.1) corresponding to the
same family of ovals and all of the forms ω from the theorem is isomorphic to the

332 YU. ILYASHENKO

factor space of these forms modulo the exact forms. This latter space is isomorphic
to the space of polynomials in two variables of degree no greater than n − 1. The
dimension of the latter space equals n
2+n
2 .
Suppose that the polynomial H from Theorem 7.1 has at least one family of real
ovals. Let us now take N ovals γ1,...,γN of an ultra-Morse polynomial H, N =
n
2+n
2 − 1. It does not matter whether these ovals belong to one continuous family
or to diﬀerent ones. Theorem 7.1, together with the Pontryagin criterion (see §2)
implies the following:

Corollary 7.1. For H, N and γj as above, and for any δ> 0 there exists a per-
turbation (7.2) with N limit cycles L1,... ,LN , such that the Hausdorﬀ distance
between Lj and γj is less than δ.

The implication results from the following. The dimension of the space of all
polynomial 2-forms Pdx ∧ dy, with deg P ≤ n − 1, equals N +1. Let us enumerate
the monomials x
kyl of degree less than n as e1,... ,eN +1 in a lexicographical order:
ei = x
k(i)yl(i). The forms
 ωi = y
l(i)+ 1 eidx

form a basis in the factor space of polynomial 1-forms of degree less than n +1
modulo exact forms. For any family Γ of ovals γ(t)of H, consider a vector function

IΓ : t ↦→ IΓ(t)= (
∫

γ(t) ω1,... , ∫

γ(t) ωN ).

The set IΓ = {IΓ(t)} is a curve in RN +1 parametrized by the value t of H corre-
sponding to the oval γ(t). Let Γj be a continuous family of ovals γj(t)that contains
γj; families Γj may coincide for diﬀerent values of j. The ovals γj determine N
points Aj on the curves IΓj :

Aj =(
∫
γj ω1,..., ∫

γj ωN ).

There is at least one hyperplane L in RN +1 passing through zero and the points
Aj. Let it be Σcixi =0. By Theorem 7.1, this hyperplane does not contain any
of the curves IΓj . Otherwise, the components of the vector function IΓj would be
linearly dependent. Therefore, the intersection points Aj ∈ L ∩ Iγj are isolated in
the topology of IΓj . A slightly perturbed hyperplane L′ = ∑ c′
ixi has transversal
intersections A
′
j = IΓj (tj) with the curves IΓj . Let ω =Σc′
iωi. Then the integrals
∫

j = ∫

γj (t) ω have simple zeros at tj. By the Pontryagin criterion (see Section 2)
the ovals γj(tj) generate limit cycles under the perturbation (7.2) with ω chosen
above. On the other hand, the ovals γj(t) are close to the ovals γj. This proves
Corollary 7.1.
The above corollary provides a rich variety of locations for limit cycles of poly-
nomial vector ﬁelds on the real plane. It also provides a lower bound H(n) ≥
n
2
2 + O(n). A better estimate

H(n) ≥ 1
2 n2 log2 n + O(n)

for the special values of n : n =2k − 1,k ∈ Z
+, was obtained by Christopher and
Lloyd [ChL]. Recently, Itenberg and Shustin [IS] proved that this estimate holds

CENTENNIAL HISTORY OF HILBERT’S 16TH PROBLEM 333

for any n ≥ 3. They used the “gluing up” method invented by Viro for the study of
real planar algebraic curves, the subject of the ﬁrst part of Hilbert’s 16th problem.
The topological variety of phase portraits of polynomial vector ﬁelds is a subject
of special study; see, for example, [AKL] and [F].

7.3. Complex extensions of Abelian integrals. Let us complexify the data
in the problem by considering H as a polynomial in C
2. The level sets of H will
become the Riemann surfaces:

St = {z ∈ C2|H(z)= t}.

The ovals γ(t) are the cycles in the homology group

H1(t)= H1(St, Z).

The group H1(t) is free Abelian of rank n2. It has a remarkable (not uniquely
determined) set of generators called the vanishing cycles. They are deﬁned as
follows.
For a Morse polynomial H, a small neighborhood of any critical point a is split
into the level sets of H in a canonical way. Indeed, by the Morse lemma, a holo-
morphic coordinate change near a critical point a brings a to zero, and level sets of
H to a family z1z2 = const. A cycle

δC = {C1/2eiϕ,C1/2e−iϕ|ϕ ∈ [0, 2π]}⊂ {z1z2 = C}

is called a local vanishing cycle. It shrinks to the critical point 0 as C → 0.
A system of vanishing cycles may be deﬁned on any level set St, not necessarily
close to a critical level. Indeed, let a1,... ,aµ,µ = n2, be the critical values of H.
Let t0 ̸= aj be an arbitrary noncritical value. For each j =1,...,µ, let αj be a
path in C that connects t0 and aj, such that:

αj \{aj}⊂ C \{a1,...,aµ},

and the paths αj have no self intersections and are pairwise disjoint outside t0. For
t close to aj, local vanishing cycles δj(t) ∈ H1(t) are well deﬁned. For all t ∈ αj
the family δj(t) ∈ H1(t) is well deﬁned by a covering homotopy. This determines
aset of vanishingcycles δj(t0) ⊂ H1(t0) associated to curves αj. It ends up that
these cycles are generators of the group H1(t0).
When the parameter t makes a circuit around a critical value aj, the homology
group undergoes a monodromy transformation ∆j. It is described by

Theorem 7.2 (Picard-Lefschetz)[AGV]. Let l ∈ H1(t0). Let t run over the loop
λj :
 λj =˜αj ◦ βj ◦ ˜α
−1
j ,

where ˜αj = αj \ Dj,Dj is a small disk centered at aj, and βj = ∂Dj is positively
oriented. Let ∆j be the corresponding isomorphism of H1(t0) to itself. Then for
any l ∈ H1(t0):
 ∆j(l)= l − (δj,l)δj,(7.3)

where δj(t0) is the vanishing cycle associated to αj.

Now the proof of the Exactness Theorem 7.1 may be outlined as follows. For
the system of paths αj, described above, the intersection graph of the corresponding
system of vanishing cycles is connected, [I69a] and [AGV]. Moreover, any real oval
of an ultra-Morse polynomial of degree greater than 2 has a nonzero intersection

334 YU. ILYASHENKO

index with some vanishing cycle [Pu]. By the uniqueness theorem for analytic
functions, an analytic continuation of a function, identically equal to zero, along a
closed curve, is identically zero. The Picard-Lefschetz theorem now implies that if∫

γ(t) ω ≡ 0 for a family of ovals γ(t), then ∫

δ(t) ω ≡ 0 for any family of vanishing
cycles δ(t) with nonzero intersection index (γ(t),δ(t)). As the intersection graph of
vanishing cycles is connected, then ∫

δj (t) ω ≡ 0 for all vanishing cycles δj. Hence,
∫

l(t) ω ≡ 0 for any family of cycles l(t) ∈ H1(t). This mayhappen onlyif ω is exact
[I69a], [I69b]. This completes the proof of the Exactness Theorem.
A stronger version of the Exactness Theorem was obtained by Gavrilov [Ga98].
Together with [Pu] it implies the following statement.

Theorem 7.3. Let all of the assumptions of Theorem 7.1 hold except for one: ω
is now a polynomial 1-form of arbitrary degree. Then the form ω is exact, modulo
amultipleof dH :
 ω = df + gdH

for some polynomials f and g.

7.4. Existence of an upper bound on the number of zeros of Abelian
integrals. Monodromy arguments play a crucial role in the proof of Theorem 2
from Section 2. Originally, this theorem was proved in a slightly stronger form.

Theorem 7.4 [V], [Kh84]. For any n and m there exists a number V (n, m) such
that integral (7.1) over the ovals of a polynomial of degree n +1, with the integrand
ω being a polynomial 1-form of degree m, has no more than V (n, m) isolated real
zeros.

This was one of the ﬁrst results proved by means of the fewnomial theory.
Consider the integral (7.1) as a function not only of t, but also of the coeﬃcients
of H and the form ω, as well. In the space of all this data, tuples (H, t, ω)with
ultra-Morse H and t noncritical for H form the set of so called regular points. Their
complement forms the set of singular points Σ, which is algebraic.
By the Hironaka desingularization theorem, Σ may be replaced by a set Σ
′ that
is a normal crossing near any of its singular points. That is, Σ′ is locally a union of
hyperplanes that intersect transversely. The integral is holomorphic on the universal
cover of the complement to Σ′.
This allows us to give a local representation of the integral (7.1). Take an
arbitrary point a ∈ Σ′ and coordinates t1,...,tM such that tj(a)=0; the set Σ′

intersected with some neighborhood U of a is the union of the ﬁrst m coordinate
hyperplanes: t1 · ··· · tm =0,t ∈ U. The fundamental group of U \ Σ
′ is Abelian.
Indeed, the complement to the m coordinate hyperplanes in CM is homotopically
equivalent to an m-torus, whose fundamental group is commutative. A circuit of
any of the hyperplanes deﬁnes a monodromy transformation in the space spanned
by µ = n2 branches I1,...,Iµ of the integral. The other branches belong to this
space. The monodromy transformations corresponding to diﬀerent hyperplanes
tj = 0 commute. Hence, near any point a ∈ Σ
′, the µ branches of the integral may
be represented in the form:

(I1,...,Iµ)= (C1,...,Cµ)tA1
1 ...t
Am
m(7.4)
 CENTENNIAL HISTORY OF HILBERT’S 16TH PROBLEM 335

where Cj are holomorphic at 0 and Aj are logarithms of monodromy matrixes
divided by 2πi. By geometric reasons, the eigenvalues of Aj are real; see [V] and
the references therein.
The elements of the matrix tAj are real powers of t multiplied by polynomials of
log t, and linear combinations of such terms. They may be represented as solutions
of a system of Pfaﬃan equations of the form Ω = 0, Ω being a polynomial 1-
form. The Khovanskii elimination procedure allows us to replace an equation (one
component of (7.4) = 0) by an analytic equation f =0. By the Gabrielov Theorem
[Gb], the number of isolated solutions of f = 0 is uniformly bounded with respect to
a parameter. Standard compactness arguments conclude the proof of Theorem 7.4.

7.5. Linear growth of V(n, m) in m. Fix an ultra-Morse Hamiltonian H and
consider the number of zeros of the integral (7.1) as a function on the degree m
of ω. In [IYa95b], it was proved that this function has at most double exponential
growth in m. In [NYa95], this estimate was improved up to a single exponential.
In about 1996 Petrov and Khovanskii proved the following result that still remains
unpublished.

Theorem 7.5. The upper bound V (n, m) on the number of zeros of the Abelian
integral (7.1) (see Theorem 7.4) grows linearly in m. Moreover,

V (n, m) ≤ A(n)m + B(n),

where A is a polynomial in n that may be explicitly calculated.

Note that V (n +1,n) is the main interest in Hilbert’s 16th problem because for
m =deg H − 1= n, (7.2) is a polynomial diﬀerential equation of degree n. This
quantity is closely related to B(n). The estimate of both remains the main problem
in the ﬁeld.
The proof of the existence of B(n), as well as of V (m, n), is nonconstructive,
that is, suggests no algorithm for getting an upper bound for these quantities.

7.6. Restricted version of the inﬁnitesimal Hilbert’s 16th problem: I.
Thus, the complete inﬁnitesimal Hilbert’s 16th problem remains unsolved. Yet two
restricted versions of the problem have been recently solved in [NYa*] and [GI*].
The restriction deals with the choice of H. The estimates of the number of zeros of
the integral (7.1) are obtained for an arbitrary degree n + 1 Hamiltonian H and for
an arbitrary integrand ω of degree less than n +1.
Abelian integrals are subject to the so called Picard-Fuchs equations [AGV].
These are linear systems of diﬀerential equations with rational coeﬃcients of the
type ˙z = A(t)z, z ∈ CN , with the entries of A(t) rational functions in t. The
approach presented in this subsection studies Abelian integrals as solutions of this
type of equation. The study sketched in the next subsection is based directly on
the deﬁnition (7.1).
A single linear diﬀerential equation of the type w(n) = ∑n−1
j=0 aj(t)w(j) ﬁts well
to the estimate of the Bernstein index of solutions; see Section 6.4. In this way,
upper estimates on the number of zeros of a solution of a linear diﬀerential equation
through the magnitudes of its coeﬃcients were obtained [IYa96]. These results were
applied to Abelian integrals over the ovals of a hyperelliptic polynomial in [NYa99a].
These polynomials are far from being ultra-Morse.
The main problem for generic, that is ultra-Morse, polynomials is to reduce the
Picard-Fuchs system for Abelian integrals to a single equation of a higher order. The

336 YU. ILYASHENKO

related techniques were elaborated in [NYa99b]; see also [Ya99] and the references
therein.
The estimate below is given for any ultra-Morse polynomial H and depends on
a positive parameter R that shows, roughly speaking, how distant the polynomial
H is from the set of non-ultra-Morse polynomials. This parameter is deﬁned as
follows.
Consider the highest homogeneous part h of H. Its partial derivatives hx,hy
are relatively prime by Deﬁnition 7.1. Consider a linear operator Dh that maps
the space of homogeneous polynomials of degree 2n − 1 to the space of pairs of
homogeneous polynomials of degree n − 1 deﬁned by the formula:

Dh : f ↦→ (u, v),f = hxu + hyv.

Obviously, Dλh = λ
−1Dh. Let the norm of the polynomial ∥· ∥ be the sum of
the magnitudes of its coeﬃcients, and ∥(u, v)∥ = ∥u∥ + ∥v∥. There exists only one
positive constant λ such that Dλh has a unit norm. Moreover, for any ultra-Morse
polynomial H there exists at least one transformation H = λH(µx, µy),λ > 0,µ >
0 such that
- Dh has a unit norm; and
- ∥H − h∥ =1,
where h is the highest order form of H. Let a1, ..., an2 be the critical values of H.
Deﬁne R = R(H) to be the minimal positive number such that:

|aj|≤ R; |ai − aj|≥ 1
R .

There are no more than n +1 pairs (λ, µ) ∈ R+ × R+ with the above properties.
Denote them by (λi,µi),i =1,... ,k ≤ n − 1and let Hi = λiH(µix, µiy),Ri =
R(Hi). Let R(H)=mini=1,...,k Ri.

Theorem 7.6 [NYa*]. There exists an elementary function N (n, m) with the fol-
lowing property: The number of all the zeros of the integral (7.1) over real ovals
of an ultra-Morse polynomial H does not exceed (2 + R)
N (n,m), where R = R(H)
is the parameter deﬁned above. The function N may be estimated from above by a
tower of four stories (iterated exponentials), and may be explicitly calculated.

7.7. Restricted version of the inﬁnitesimal Hilbert 16th problem: II. An-
other solution deals with a stronger restriction on H, but gives an explicit estimate
of the type “exponential of a polynomial”. The restrictions on H are described in
the following deﬁnitions.

Deﬁnition 7.2. A critically bounded polynomial is a monic complex polynomial
of one variable whose critical values are distinct and contained in the unit disc.

Deﬁnition 7.3. A real polynomial H(x, y) in two variables is said to be critically
balanced if it is a sum of two critically bounded polynomials of the same degree
n +1 ≥ 3in x and y respectively, H(x, y)= p(x)+ q(y), its complex critical values
are distinct, and the distance between any two of them is greater or equal to 1
n2 .

Theorem 7.7 [GI*]. Let H be a critically balanced polynomial of degree n +1 and
ω be a real non-exact 1-form with polynomial coeﬃcients of degree at most n. Let
γ(t) be an arbitrary continuous family of real ovals of H. Then, the number of zeros
of the integral (7.1) is no greater than e2500n
4.

CENTENNIAL HISTORY OF HILBERT’S 16TH PROBLEM 337

In Theorem 7.7, the set of all ultra-Morse polynomials is replaced by a rather
special set of critically balanced polynomials. It seems that it may be possible to
generalize this result to the set of all ultra-Morse polynomials. The estimate is
expected to be of the form eP (n,R), where R = R(H) is the same parameter as in
Theorem 7.6 and P is a polynomial.
On the other hand, there is hope to reduce the general inﬁnitesimal Hilbert’s
16th problem to the special case of Theorem 7.7 by Hilbert’s “method of continuous
deformation of coeﬃcients” mentioned in the statement of the 16th problem [H].
This is the matter of future research, and it is not discussed here.
Both Theorems 7.6 and 7.7 are generalized to give an upper bound on the number
of zeros of integral (7.1) in compact subsets of its complex domain. Theorem 7.7 is
based on the Picard-Lefschetz and the Growth-and-Zeros Theorems. Let (a, b)be
the interval between two critical values of H, such that the family of ovals γ(t)is
deﬁned for t ∈ (a, b),a < b. Let σ be the segment [a + 4
n2 ,b − 4
n2 ]. We will describe
the idea of the proof of Theorem 7.7 in the weakened form:

#{t ∈ σ|I(t)= 0}≤ e2500n
4 .(7.5)

Estimates that allow the application of the Growth-and-Zeros Theorem, namely
(7.10) and (7.11) below, are rather involved. We explain only why estimates of this
kind should hold.
Inequality (7.5) will be deduced from the Growth-and-Zeros Theorem. The main
problem is to choose properly the sets K ⊃ σ and U ⊃ K for which the Bernstein
index of the integral I can be estimated. Let us begin with an attempt that fails,
but shows the problems needed to be solved. Consider the integral I, (7.1), as
the function f in Theorem 6.6, the segment σ as K0, and its ε-neighborhood with
ε = 1
8n2 as U0. We write K0,U0 instead of K, U since we construct the actual K, U
later.
Let ωi be the same as in 7.2. Let us ﬁrst try to apply the Growth-and-Zeros
Theorem to the function f = I using the sets K0 and U0. Let ωi be the same as in
Section 7.2. Let us normalize the form ω :

ω = ∑ ciωi, max |ci| =1.(7.6)

The deﬁnition of a critically balanced polynomial is well suited to the upper estimate
of I. Recall that by Deﬁnition 7.3, σ ⊂ [−2, 2]. After that, the size of the ball in C
2

that contains a cycle γ(t)for t ∈ U0 may be estimated from above, together with
the integral (7.1). Namely,
 M0 =max
¯U0 |I|≤ e16n.(7.7)

The geometric constant γ, for K0 = σ and U0, above, is easily estimated by e 2|σ|
ε ≤
e64n
2. But the lower estimate of
 m0 =max
σ |I|

is a problem. The assumption m = 0 immediately brings a contradiction by Theo-
rem 7.1, since the form ω is not exact. We have a kind of quantization problem: I
is not identically zero on σ. What is a universal lower bound for max |I| on σ?

338 YU. ILYASHENKO

The answer to this question is unknown. Therefore, a larger set K ⊃ σ is needed
on which the value
 m =max
K |I|(7.8)

will admit some explicit lower bound. The set K may be constructed as a union
of σ and the loops beginning at some t0 ∈ σ and going around the critical values.
These loops are chosen so that the extensions of the oval γt0 over these loops
generate the group H1(t0). This is possible by the Picard-Lefschetz theorem and
the connectedness of the intersection graph, mentioned in 7.3. The set U is the
ε-neighborhood of K with the same ε = 1
8n2 .
Now if we suppose that the maximum m is small, then the integrals of ω over all
of the vanishing cycles δj(t0) will be small. This allows us to ﬁnd a lower estimate
for m in the following way.
Consider a larger tuple of forms ωi,i =1,... ,µ = n2. It includes the set deﬁned
in 7.2 and consists of the forms

ωi = y
l(i)+ 1 x
k(i)yl(i)dx

with (k(i),l(i)) ranging over the integer points of the square 0 ≤ k ≤ n − 1, 0 ≤
l ≤ n − 1 (instead of the triangle in Section 7.2.) Consider the matrix

I(t)=(Iij (t)),Iij (t)= ∫

δj (t) ωi, and ∆(t)=det I(t).

The function ∆(t) is called the main determinant. It is single-valued because, when
t runs a loop around a critical value aj, some columns of the main determinant are
replaced by their sums with the jth column multiplied by an integer. This follows
from the Picard-Lefschetz theorem. Hence, the determinant ∆(t) is a well deﬁned
function for any ﬁxed H. For a critically balanced H it may be explicitly calculated
through the critical values of H and estimated from below. Namely,

min
U |∆(t)| >e−33n
2 log n.(7.9)

On the other hand, the same arguments that imply (7.7) give a stronger inequality:

M =max
t∈U |Iij (t)|≤ e16n.(7.10)

Suppose now that m in (7.8) is very small. Then, by the construction of K and the
Picard-Lefshetz theorem, all the elements of the string
∫

δ1(t) ω,... , ∫

δµ(t) ω

would be very small. Let us take i such that in (7.6), |ci| =1. If we replace the
ith row in I(t) by the above string, the magnitude |∆(t)| will not be changed. On
the other hand, the assumption that all of the entries of this string are very small,
together with the upper estimate (7.10) of the entries of I(t) and the lower estimate
(7.9) of the main determinant, brings a contradiction.
Moreover, (7.9) and (7.7) together imply that in (7.8)

m ≥ e−32n
3.(7.11)

Now all the data for the estimate of the Bernstein index BK,U (I) are collected.
Application of the Growth-and-Zeros Theorem proves Theorem 7.7 for zeros taken
on the segment σ.

CENTENNIAL HISTORY OF HILBERT’S 16TH PROBLEM 339

7.8. The strong inﬁnitesimal Hilbert 16th problem. An estimate of the
number of zeros of Abelian integrals, even if it would have been obtained, would
not answer the following question.

Problem 7.1 (Strong inﬁnitesimal Hilbert problem). Give an upper bound on the
number of limit cycles of a polynomial vector ﬁeld which is close to a Hamiltonian
one of degree n.

It is the same as estimating the number of limit cycles of the equation

dH + ω =0(7.12)

for ω = Adx + Bdy, where A, B are polynomials of degree at most n, with small
coeﬃcients. In addition to limit cycles generated by the ovals of H, the problem
requires one to estimate the number of limit cycles generated by polycycles of H.
For ultra-Morse H, any of these polycycles may contain only one vertex, because
all the critical points of H belong to diﬀerent level curves. Therefore, it may be a
separatrix loop or an eight shaped ﬁgure; see Figure 2. The ﬁrst case is investigated
in [Mar]. The restricted version of the problem requires investigation of the second
case only. The general problem deals with more complicated critical level curves
of H. On one hand, this problem is closely related to the bifurcation theory; see
Section 5. On the other hand, it presumably may be linked to the following two
results which are of independent interest.

Theorem 7.8 [R89]. A separatrix loop of a hyperbolic saddle that occurs in an
analytic family of planar vector ﬁelds has but a ﬁnite cyclicity.

Theorem 7.9 [Mar]. The multiplicity of any zero of an integral (7.1) at any inte-
rior point of its domain is no greater than n4.

The only case for which the strong problem is solved is the quadratic one.

Theorem 7.10 [Ga01]. The number of limit cycles of a quadratic equation close
to a Hamiltonian one is no greater than two.

This is a result of a long chain of eﬀorts by Horozov, Iliev and Gavrilov.

§8. Foliations by analytic curves

The theory of foliations by analytic curves in the complex plane may be con-
sidered as a complexiﬁcation of the real planar theory. The complex version is
drastically diﬀerent from its real prototype.

8.1. Complexiﬁcation. Consider the equation
dy
dx = Pn
Qn (x, y),(8.1)

where (x, y) ∈ R2, and Pn and Qn are real polynomials of degree at most n.
Topologically, the integral curves of (8.1) are either circles or lines. Isolated closed
orbits are limit cycles. There are only a ﬁnite number of these; see Section 2.
Let us now complexify equation (8.1), that is, consider it in C
2. Formula (8.1)
determines a complex line ﬁeld in C2 outside of the set of singular points

Σ= {(z, w) ∈ C2|Pn(z, w)= Qn(z, w)= 0}.(8.2)

Integral surfaces of (8.1) are now holomorphic curves. In other words, they are
Riemann surfaces, and their topology may be much more complicated than that

340 YU. ILYASHENKO

of real integral curves. The partition of C
2 \ Σ by the integral surfaces of (8.1)
is called the corresponding foliation. The integral surfaces are called the leaves of
the foliation. Diﬀerential equations in the complex plane are identiﬁed below with
corresponding foliations. Now we consider polynomials as in (8.1) which are not
necessarily real. The class of equations
dw
dz = Pn
Qn (z, w), (z, w) ∈ C2 \ Σ(8.3)

with coprime complex polynomials Pn and Qn is denoted by An.
A complexiﬁcation of a real phase curve is a leaf of the corresponding foliation
that contains this curve. A closed integral curve of real equation (8.1) is a loop on its
complexiﬁcation. The complexiﬁcation of the notions of closed integral curves, limit
cycles and Poincar´emaps are complex cycles, complex limit cycles and holonomy
maps.

Deﬁnition 8.1. A complex cycle is a nontrivial free homotopy class of loops on a
leaf of foliation (8.3).

Note that a real closed phase curve of (8.1) is a complex cycle on its complex-
iﬁcation. Indeed, suppose that a closed phase curve γ represents a trivial free
homotopy class on its complexiﬁcation. Then γ bounds a topological disc D on the
corresponding leaf. Complexiﬁcation (8.3) of real equation (8.1) persists under the
symmetry s :(z, w) ↦→ (¯z, ¯w). Hence, γ bounds another disc sD on the same leaf.
The union of these two discs is a Riemann sphere that is holomorphically embedded
in C2. Such an embedding does not exist, a contradiction.
Consider a loop γ on a leaf of foliation (8.1). Its tubular neighborhood on a leaf
is an annulus A. A tubular neighborhood U of A in C
2 is topologically equivalent
to a Cartesian product A × D, where D ⊂ C is a disc centered at zero. This disc
may be considered as a holomorphic cross-section, transversal to the leaves of the
foliation, with 0 = D ∩ γ. Let π be the projection of U to A along D. For any z ∈ D
close to zero, the loop γ may be lifted to a curve γz that lies on the leaf passing
through z and covers γ under the projection π. Let ∆γ(z) ∈ D be the endpoint of
γz. The map
 z ↦→ ∆γ(z)(8.4)

is called the holonomy map of γ.
For a real closed integral curve γ of equation (8.1), its holonomy map is the
complexiﬁcation of the corresponding Poincar´emap.
Holonomy maps of free homotopic loops are analytically conjugated.

Deﬁnition 8.2. A complex limit cycle is a complex cycle for which a corresponding
holonomy map has an isolated ﬁxed point 0.

A real limit cycle of equation (8.1) is a complex limit cycle for the complexiﬁca-
tion (8.3) of (8.1).

8.2. Problems from the global theory of complex foliations.

Problem 8.1. What are generic topological properties of the foliations (8.3)?This
means, what are the properties that remain the same for almost every equation of
the class An in the sense of the Lebesgue measure on the coeﬃcient space?

The following particular problems naturally arise. Some of them are already
solved, as presented below.

CENTENNIAL HISTORY OF HILBERT’S 16TH PROBLEM 341

Problem 8.2. What are the ω-limit sets of generic leaves?

According to [Ca], the ω-limit set of a leaf is the union of all limit points of all
sequences that belong to the leaf and are discrete in its intrinsic topology.

Problem 8.3. Is a generic foliation (8.3) structurally stable? If not, what are the
topological invariants?

Problem 8.4. What is the topological type of a generic leaf of a generic foliation
of class An?

Problem 8.5. The same question, as above, about the conformal type. Namely, is
the universal cover over the leaf, above, holomorphically equivalent to the complex
line or to the unit disk?

According to the general Uniformization Theorem, the universal cover over the
leaf may be uniformized, that is mapped biholomorphically onto a domain in a
Riemann sphere. This map is called the uniformization function.

Problem 8.6. How do the uniformization functions of the leaves depend on the
initial conditions?

Problem 8.7. To what extent may the holonomy map of a complex limit cycle be
analytically continued?

This problem is closely related to the simpliﬁed versions of Hilbert’s 16th problem
for the Abel and Lienard equations; see Section 6.

Problem 8.8. Consider a complex (limit) cycle of equation (8.3).Is it possible
to extend it to a family of complex (limit) cycles over a generic curve in the space
An?

In more detail, let λ = {α(t) ∈An|t ∈ [0, 1]} be a curve in An. Let γ(0) be a
complex (limit) cycle of the foliation α(0). Is it true that for generic α :[0, 1] →An,
a continuous family of complex (limit) cycles γ(t)of α(t) is well deﬁned?
The latter problem is the famous problem of persistence of complex (limit) cycles.
It goes back to [PL1] where it was stated and an unsuccessful attempt to prove the
positive answer was made.
The other problems go back to Alexeev, Anosov, Arnold, Ilyashenko (oral dis-
cussions in the 60s), and Camacho [Ca], who studied Problem 8.2 and proposed a
problem about minimal sets; see the end of Section 8.4, below.

8.3. General classes of algebraic diﬀerential equations. Class (8.3) is the
simplest family of complex foliations of algebraic origin. Below we describe some
general classes of the same nature.
Consider a complex algebraic manifold X. Let Σ ⊂ X be a subset whose Zariski
closure is an algebraic set of codimension higher than 1. Consider a foliation by
analytic curves in X \ Σ, that is partition of X \ Σ into a disjoint union of analytic
curves (leaves of the foliation) with the following property: Any point a ∈ X \Σhas
a neighborhood whose partition into the connected components of its intersection
with the leaves is biholomorphically equivalent to the partition of a polydisc by
discs parallel to the ﬁrst coordinate axis. Such a partition is called foliation, with
singularities, on X.

342 YU. ILYASHENKO

Theorem 8.1 [I78a]. Any foliation with singularities on a projective algebraic
manifold X has an algebraic origin. Namely, it is determined by a distribution
of complex lines deﬁned as a meromorphic section of the projectivization of the
tangent bundle over X.

Corollary 8.1. Any foliation on the complex projective plane with a ﬁnite number
of singular points in any aﬃne chart has the form (8.3).

Therefore, the theory of foliations of projective algebraic manifolds by analytic
curves lies on the boundary between algebraic geometry and complex analysis.
Foliations are determined by the algebraic data, but their leaves are highly tran-
scendental.
A class of foliations may be determined by the manifold X and the degree of the
corresponding meromorphic section of the projective tangent bundle over X. For
example, consider the class Bn of foliations, with singularities, which are given by
an equation (8.3) of the same degree in any aﬃne chart. This class seems to be even
more natural than An, but it is less studied for the reason discussed in 8.5 below.
All the above problems make sense for any of the classes mentioned here. We
will deal mostly with the class An.

8.4. Generic properties of complex foliations of class An. Everywhere below
n ≥ 2.
As mentioned above, generic properties of complex foliations are in bitter con-
trast with those of real polynomial equations. A generic real polynomial equation
has a ﬁnite number of closed orbits and is structurally stable. Generic complex
foliations of class An have an inﬁnite number of complex limit cycles and are rigid,
in the sense explained below.
In all of the theorems of this subsection genericity means the same as in 8.2:
almost everywhere in the sense of the Lebesgue measure.

Theorem 8.2. A generic foliation of class An has no algebraic leaves. Each leaf
of a generic foliation of class An is dense in C2.

The density property was discovered by M. Khudai-Verenov in 1962, [K-V]. Sev-
eral improvements may be found in [I78a], [Shch82], and [N].

Theorem 8.3 [I78a]. A generic foliation of class An has at least a countable num-
ber of complex limit cycles.

Theorem 8.4 [PL1]. Any foliation of class An has no more than a countable num-
ber of complex limit cycles.

Deﬁnition 8.3. Two foliations with singularities on X are topologically conjugate
if there exists a homeomorphism of X onto itself that brings the leaves and the
set of singular points of the ﬁrst foliation to that of the second one. The above
homeomorphism is called conjugating.

Deﬁnition 8.4. A complex equation α of class An is absolutely rigid if the fol-
lowing holds. There exist a neighborhood of α in An and a neighborhood of the
identity in Hom(CP 2, CP 2), the set of homeomorphisms of CP 2 onto itself, such
that: If α is topologically conjugated to a foliation β from the ﬁrst neighborhood
and the conjugating homeomorphism belongs to the second neighborhood, then α
is aﬃnely equivalent to β.

CENTENNIAL HISTORY OF HILBERT’S 16TH PROBLEM 343

This means that there exists an aﬃne coordinate change that brings α to β.
In the real case, topological equivalence is very robust and does not distinguish
generic real equation (8.1) from the nearby ones. In the complex case it is as delicate
as the classiﬁcation with respect to aﬃne coordinate changes, as the following
theorem shows.

Theorem 8.5 [I78a]. A generic foliation of class An is absolutely rigid.

These results provide the main step in solutions of Problems 8.1, 8.2 for class
An. The analog of Theorem 8.5 for foliations in C
3 with an algebraic solution is
proved in [GM].
The genericity conditions in the above theorem are that the system is “outside of
some set of measure zero in the parameter space”. It may be improved to “outside
of some real algebraic subset in the parameter space”, as discussed in the next
subsection.
We stress here that Theorems 8.2, 8.3, and 8.5 are proved for generic equations
of class An only. Analogous statements for generic equations of class Bn, or other
classes of algebraic diﬀerential equations, are open problems. On the other hand,
analogs of Theorems 8.2 and 8.5 were recently proved for locally generic foliations
of CP n in [LR].
For any n and m denote by F n(CP m) the space of all foliations with singularities
of CP n by analytic curves such that in any aﬃne chart the foliation is given by a
polynomial vector ﬁeld of degree no greater than n, and at least in one chart the
equality holds.

Theorem 8.6 [LR]. For any n ≥ 2,m ≥ 2 there exists a nonempty open subset
U ⊂F n(CP n) such that any element α ∈ U has a ﬁnite number of singularities
and is “chaotic,” i.e. satisﬁes:
- Minimality: each leaf is dense in CP n;
- Ergodicity: any measurable union of leaves has zero or total Lebesgue measure;
- Entropy: the geometric entropy of the foliation induced by α on CP n, with
small balls centered at singular points deleted, is strictly positive; and
- Rigidity: there exists a neighborhood V of the identity in the space of all homeo-
morphisms of CP n onto itself such that: if α is topologically conjugated to β ∈ U by
some H ∈V, then α and β are also conjugate by a projective change of coordinates.

The entropy here is considered in the sense of [GLW]; however, we do not repro-
duce the deﬁnition because of the lack of space. This result gives a partial proof of
the minimality and rigidity conjectures stated in [I78b].
The minimality statement of this theorem was proved for m = 2 by B. Muller
in [Mu]. A global problem on minimal sets, below, is due to Camacho [Ca].
A minimal set of a foliation, with singularities, in CP n is a closed invariant
nonempty subset of CP n that contains no proper subset with these three properties.
Invariance means that the set is either one singular point (in this case it is called
trivial), or alternatively contains no singular points, and contains the entire leaf
passing through each point of the set.

Problem 8.9 [Ca]. Are there foliations, with singularities, on CP 2 that have non-
trivial minimal sets?

This problem is closely related to the problem of density of leaves for generic
foliations of class Bn. Recently, Verjovsky [Ve] constructed a positive answer to

344 YU. ILYASHENKO

a modiﬁed version of Problem 8.9, where CP 2 is replaced by CP 5. For CP 2, the
problem stays open.
On the other hand, the theorems proved for foliations of class An suggest the
results that may be expected for other classes of foliations, at least in lower dimen-
sions.

8.5. The monodromy group at inﬁnity. The foliation (8.3), with singularities,
may be extended from C2 to CP 2. It appears that for a generic foliation, α ∈An,
the inﬁnite line with n +1 singular points deleted is a leaf of the extended foliation.
This leaf is called a leaf at inﬁnity, and the singular points in its closure are called
singular points at inﬁnity. Equations of class An, with n + 1 singular points at
inﬁnity, form a Zariski open set in An which is denoted by A
′
n.
The leaf at inﬁnity has a large fundamental group — a free group with n gen-
erators. The corresponding holonomy transformations form a group of germs of
conformal mappings. It is called the monodromy group at inﬁnity. For brevity we
will drop sometimes “at inﬁnity”. The monodromy transformation corresponding
to a loop on the inﬁnite leaf that makes a circuit of one singular point aj at inﬁnity
is a germ of a conformal mapping fj :(C, 0) → (C, 0). The monodromy group is
generated by f1,...,fn. Properties of this group are closely related to properties of
the corresponding foliation. Indeed, if two foliations are topologically conjugated,
then so are their monodromy groups at inﬁnity. The latter means that there exists
oneand thesame germ of a homeomorphism h :(C, 0) → (C, 0) that conjugates
the generators fj of the ﬁrst monodromy group with the corresponding generators
of the second one.
The orbit of a point z, under the action of the monodromy group, is the set of
images of z under all of the ﬁnite compositions of biholomorphic representatives of
fj and f −1
j whenever deﬁned. If the monodromy group has dense orbits in some
neighborhood of zero, then under mild extra restrictions, all of the leaves of the
corresponding foliation (8.3) are dense in C
2.
If a monodromy group is topologically rigid (any homeomorphism that conju-
gates it with another one is holomorphic or anti-holomorphic), then, once more
under mild restrictions, the corresponding foliation (8.3) is absolutely rigid.
Therefore, it is important to study geometric properties of ﬁnitely generated
groups of germs in order to understand geometric properties of analytic foliations.
From the algebraic point of view, the groups mentioned above may be Abelian, solv-
able (non-Abelian) and non-solvable. For groups of germs of conformal mappings
(C, 0) → C, 0), solvability is the same as the following property:
The commutator of the group is Abelian.

Theorem 8.7 [N]. Consider a non-solvable ﬁnitely generated group of germs of
conformal mappings (C, 0) → (C, 0). Then its orbits are “dense in sectors”. This
means that there is a ﬁnite number of real analytic curves passing through zero such
that orbits of the group are dense in the sectors bounded by these curves and having
their vertex at zero.

Theorem 8.8 [Shch84]. A non-solvable group of germs of conformal mappings
(C, 0) → (C, 0) is topologically rigid.

Another proof of this theorem was given in [N].

CENTENNIAL HISTORY OF HILBERT’S 16TH PROBLEM 345

Theorem 8.9 [SRO]. Any non-solvable group of germs of conformal mappings
(C, 0) → (C, 0) has a countable number of germs whose representatives have isolated
ﬁxed points diﬀerent from zero.

Remark. These ﬁxed points correspond to a countable number of limit cycles of a
corresponding foliation.

These results imply that Theorems 8.2, 8.3, and 8.5 hold true for equations (8.3)
from some real Zariski open set. In more detail, we have

Corollary 8.2. There exists a real algebraic subset Σ in the space An of equations
(8.3) such that any equation α from the real Zariski open set An \ Σ
i) is absolutely rigid;
ii) has an inﬁnite number of complex limit cycles (for n ≥ 3);
iii) any leaf of α, except for the inﬁnite one, is dense in CP 2.

Statement i) is proved in [Shch84]. In [LSSc] it is proved that the set of rigid
equations in An is open and dense.
Statement ii) is proved in [SRO]. The restriction n ≥ 3 in ii) seems to be purely
technical; the statement is believed to hold for n = 2 as well.
Statement iii) was never published, yet it follows almost immediately from The-
orem 8.7 and the following:

Lemma 8.1 [Shch84]. The set of equations α ∈An with non-solvable monodromy
group at inﬁnity contains a real Zariski open set.

These results motivate the interest in exceptional foliations of class An, namely
those that have Abelian or solvable monodromy group at inﬁnity. Homogeneous
equations of the class An, as well as those aﬃnely equivalent to them, have Abelian
monodromy group. The same holds for the Hamiltonian equations. For the equa-
tions of the ﬁrst class, the monodromy transformations at inﬁnity are all linear in
one and the same chart.
Equations of the second class are equivalent to dH =0, where H is a polynomial
of degree n +1. Their monodromy groups at inﬁnity consist of a ﬁnite number of
rotations. It appeared that there are other equations of class An with Abelian mon-
odromy group at inﬁnity. Some nontrivial examples were found in [O-B], [IPy97],
and [Py].
The description of generic properties of foliations of class An heavily relies on
the existence of a leaf with a rich fundamental group, namely, the leaf at inﬁnity.
There is no distinguished projective line for equations of class Bn. Hence, one cannot
expect the existence of a leaf with a rich fundamental group for generic equations
of class Bn. Such leaves may occur for degenerate foliations only. Methods of
perturbation theory provide density and rigidity results for equations from an open
subset of the class Bn [Mu] and [LR]; see Theorem 8.6, above.
To conclude, let us explain the density property for a very degenerate equation
α of the class An, namely a homogeneous one. The monodromy group G at inﬁnity
for such an equation is linear. Let multiplications by ν1,... ,νn be generators of the
group. Suppose for simplicity that n =2. Let νj =exp 2πiµj,j =1, 2. Consider
the additive group G
+ generated by 1,µ1,µ2. The orbits of the group G are the
images of the orbits of the group G
+ under the map z ↦→ exp 2πiz. The latter orbits
are dense for generic µ1,µ2; hence, the orbits of G are dense for generic ν1,ν2 as
well. Thesameis truefor theleaves of the foliation α, except for n + 1 lines. These
lines, with zero deleted, are the algebraic leaves of the foliation.

346 YU. ILYASHENKO

8.6. The topology of leaves and topological invariants of foliations.

Problem 8.10. Is it true that for a generic foliation of class An the leaves are
topologically either cylinders, a countable number of these, or disks?

The answer seems to be aﬃrmative. Indeed, if two complex limit cycles are
located on the same leaf, then it seems possible to split them by a small perturbation
in the class An in such a way that the cycles will be moved to diﬀerent leaves. On
the other hand, there are at most a countable number of complex limit cycles for
foliations of class An.
The main step in a solution of Problem 8.10 should be proving that typical equa-
tions of the class An have no complex cycles with trivial holonomy. A priori, it may
happen that every equation (8.3) from some domain in An hasleavesthat may be
called hidden multiply connected surfaces that form continuous families and con-
tain complex cycles with holonomy map the identity. Experts do not believe that
such families exist. The only result proved in this direction shows that generically
an inﬁnite leaf does not belong to any continuous family of nonsimply connected
leaves.

Theorem 8.10 [IPy95]. A generic equation of class An,n ≥ 5, has no cycle on
the inﬁnite leaf with holonomy map the identity.

In general, classes of topological equivalence for equations (8.3) are very thin:
they coincide with the orbits of the aﬃne group action. Yet, some classes are
much larger. For instance, all of the ultra-Morse polynomials deﬁne topologically
equivalent foliations by their level curves. Yet these equivalence classes cannot be
too thick, as the following theorem shows.
Let α ∈A
′
n have singular points at inﬁnity denoted by a1,...,an+1. Character-
istic numbers of these points are deﬁned as follows. Near any point aj the foliation
α is given by a vector ﬁeld that vanishes at aj. The linearization of this ﬁeld has
two eigenvalues µj and νj, where the second one corresponds to the eigenvector
tangent to the line at inﬁnity. These eigenvalues are deﬁned up to a multiplicative
factor. Their ratio λj = µj
νj is well deﬁned and called the characteristic number

at inﬁnity of aj. A theorem of Camacho-Sad [CS] implies that ∑n+1
1 λj =1. The
tuple of characteristic numbers at inﬁnity generates a topological invariant that is
described in the following theorem.

Theorem 8.11 [Na]. Let two foliations of class A
′
n be topologically equivalent. Let

λ =(λ1,...λn+1),µ =(µ1,... ,µn+1)

be the tuples of their characteristic numbers at inﬁnity where λj and µj correspond
to singular points that are mapped to one another by the conjugating homeomor-
phism. Then, there exists a linear operator A : R2 → R2, R2 = RC, such that

A(1) = 1,A(λj )= µj.

Topological invariants of foliations determined by vector ﬁelds in spaces of di-
mension higher than 2 may have a local nature. Indeed, the topological classiﬁcation
of complex linear systems
 ˙z = Az, z ∈ Cn,t ∈ C,n ≥ 3(8.5)
 CENTENNIAL HISTORY OF HILBERT’S 16TH PROBLEM 347

has numerical invariants, provided that A is of Siegel type (the so called Ladis’
Theorem). The latter means that zero belongs to the convex hull of the spectrum
of A;see [La],[CKP],and [I77].
Later on, Chaperon proved a complex version of the Grobman–Hartman the-
orem: for generic A, the foliation determined by a holomorphic vector ﬁeld with
the linear part (8.5) at a singular point is topologically equivalent to its linear part,
[Ch]. In the case when (8.5) is not of Siegel type, the same result was proved by
Guckenheimer [Gu].
Ladis’ and Chaperon’s theorems provide numerical invariants of the topological
classiﬁcation of polynomial foliations. These invariants may be useful in the proof
of a topological rigidity theorem analogous to Theorem 8.5 in higher dimensions
[I78b].

8.7. Conformal type and simultaneous uniformization of leaves.

Theorem 8.12 [LN94], [G94], [CGM]. Any leaf of a generic foliation of classes
An and F n(CP m) is hyperbolic.

This means that the universal cover over the leaf is conformally equivalent to a
disk. This result solves Problem 8.5. For foliations on projective algebraic mani-
folds, the same was proved by Glutsuk [G96], and for compact complex manifolds
by Lins Neto [LN00].
For real vector ﬁelds, the time is a convenient parameter on the phase curves. For
complex vector ﬁelds, the time may take the same values at diﬀerent points (see,
for example, ˙z = z3 with t = −1/2z2). Therefore, time is not a good parameter on
(the universal cover of) the leaf. On the other hand, the uniformization function on
the universal cover over the leaf is a “good” parameter that maps this cover biholo-
morphically onto some domain in a Riemann sphere; we consider the uniformizing
maps not necessary to a disk. It would be a beneﬁt to have this parametrization
depending “in a nice way” on the initial condition. This motivates Problem 8.6
above.
The Simultaneous Uniformization Theorem of Bers [Ber] implies that the answer
to the question stated in this problem is frequently positive, in the algebraic case.
For instance:
Consider a family of level curves of an ultra-Morse polynomial that corresponds
to a simply connected domain U in the set of noncritical values of the polynomial.
Then the function that uniformizes the universal cover over {H = t, t ∈ U } may
be chosen to depend holomorphically on t.
Recently, Glutsuk [G01] discovered that the answer to Problem 8.6 may be neg-
ative even for foliations by algebraic curves of some special algebraic surfaces.
On the other hand, the continuous dependence of the uniformization functions
on initial conditions holds true for many classes of foliations; see [LN00] for precise
statements. The continuous dependence is meant in the topology of the uniform
convergence on compact sets.
Problem 8.6 stays open for foliations, with singularities, in CP 2.
We do not discuss here many rich branches of the theory of foliations such as
local theory and integrability; see, for instance, [CM], [CS], [CSc], [EISV], [MS], and
[Si] for basic facts and references.
At present, the global theory of complex foliations has many general results and
even more unsolved problems. It is a challenging ﬁeld in itself. Moreover, there is

348 YU. ILYASHENKO

hope that, in combination with the methods of §6, it may provide some progress to
the non-restricted versions of Hilbert’s 16th problem, mentioned in 6.1.

Acknowledgments

It is my pleasure to thank the University of New Mexico and the University of
Colorado at Boulder, where most of this paper was written. The cordial atmosphere
of these universities was very helpful and inspiring. I am also grateful to J. Hubbard,
A. Glutsuk, J. Guckenheimer, V. Kaloshin, V. Moldavskis, A. Shcherbakov, A.
Sossinski, and S. Yakovenko, who read the ﬁrst version of the paper and made many
fruitful comments. I also thank R. Roeder for preparing the electronic version of
the ﬁgures and for checking the English language.

References

[ALGM] A. Andronov; E. Leontovic; I. Gordon; A. Mauier, Theory of bifurcations of dynamic
systems on a plane, Translated from the Russian, Halsted Press [A division of John
Wiley & Sons], New York-Toronto, Ont., 1973. MR 49:9345
[A] V. I. Arnold, Geometrical methods in the theory of ordinary diﬀerential equations,
Springer-Verlag, New York, 1983. MR 84d:58023.
[AAIS] V. Arnold, V. Afrajmovich, Yu. Ilyashenko, L. Shil’nikov, Bifurcation theory and catas-
trophe theory, Translated from the 1986 Russian original Enciclopaedia Math. Sci.,
Dynamical systems. V, Springer-Verlag, Berlin, 1999. CMP 2000:07
[AGV] V. Arnold, S. Guse˘ın-Zade, A. Varchenko, Osobennosti diﬀerentsiruemykh oto-
brazhenii. II [Singularities of diﬀerentiable maps], Monodromiya i asimptotiki inte-
gralov [Monodromy and the asymptotic behavior of integrals], “Nauka”, Moscow, 1984.
MR 86m:58026
[AI] V. Arnold, Yu. Ilyashenko, Ordinary diﬀerential equations [Translated from the 1985
Russian original], Enciclopaedia Math. Sci., Dynamical systems. 1, Springer, Berlin,
1988, pp. 1–148. MR 87e:34049
[AKL] J. Artes, R. Kooij, J. Llibre, Structurally stable quadratic vector ﬁelds,Mem. Amer.
Math. Soc. 134 (1998), viii+100. MR 98m:34053
[B] I. Bendixson, Sur les courbes d´eﬁnies par des ´equations diﬀ´erentielles,Acta Math. 24
(1901), 1–88.
[Ba] N. Bautin, On the number of limit cycles which appear with the variation of coeﬃcients
from an equilibrium position of focus or center type, American Math. Soc. Translation
1954 (1954), 19. MR 15:527h
[Ber] L. Bers, Simultaneous uniformization, Bull. Amer. Math. Soc. 66 (1960), 94–97. MR
22:2694
[BFY] M. Briskin, J.-P. Francoise, Y. Yomdin, Center conditions, compositions of polynomials
and moments on algebraic curves, Ergodic Theory and Dynamical Systems 19 (1999),
1201–1220. MR 2000k:34051
[BM] F. Berezovskaya, N. Medvedeva, The asymptotics of the return map of a singular point
with ﬁxed Newton diagram, Trudy Sem. Petrovsk. 15 (1991), 156–177. MR 93f:58198
[Bo76] R. Bogdanov, The versal deformation of a singular point of a vector ﬁeld on the plane
in the case of zero eigenvalues, Trudy Sem. Petrovsk 2 (1976), 37–65. MR 56:1371
[Bo77] R. Bogdanov, Bifurcations of a limit cycle of a certain family of vector ﬁelds on the
plane, Trudy Sem. Petrovsk 2 (1976), 23–35. MR 56:1363
[Bo79] R. Bogdanov, Local orbital normal forms of vector ﬁelds on the plane, Trudy Sem.
Petrovsk 5 (1979), 51–84. MR 80j:58056
[Bo85] R. Bogdanov, Invariants of elementary singular points on the plane,Uspekhi Mat.
Nauk 40 (1985), no. 3(243), 199–200. MR 86k:58087
[B64] A. Brjuno, The normal form of diﬀerential equations, Dokl. Akad. Nauk SSSR 157
(1964), 1276–1279. MR 29:3733
[B71] A. Brjuno, Analytic form of diﬀerential equations I, Trans. Moscow Math. Soc. 25
(1971), 119–262. MR 51:13365

CENTENNIAL HISTORY OF HILBERT’S 16TH PROBLEM 349

[B72] A. Brjuno, Analytic form of diﬀerential equations II, Trudy Moskov.Mat.Obˇsˇc. 26
(1972), 199–239. MR 51:13365
[C] K.T. Chen, Equivalence and decomposition of vector ﬁelds about an elementary critical
point,Amer. J. Math. 85 (1963), 693–722. MR 28:3224
[Ca] C. Camacho, Problems on limit sets of foliations on complex projective spaces,Pro-
ceedings of the International Congress of Mathematicians, Vol. I, II (Kyoto, 1990),
Math. Soc. Japan, Tokyo, 1991, pp. 1235–1239. MR 93j:32039
[CGM] A. Candel, X. G´omez-Mont, Uniformization of the leaves of a rational vector ﬁeld,
Ann. Inst. Fourier (Grenoble) 45, no. 4 (1995), 1123–1133. MR 96k:32068
[Ch] M. Chaperon, On the local classiﬁcation of holomorphic vector ﬁelds, Geometric dy-
namics (Rio de Janeiro, 1981), Springer, Berlin, 1983, pp. 96–103. MR 85d:58049
[ChL] C.J. Christopher, N.G. Lloyd, Polynomial systems: a lower bound for the Hilbert num-
bers, Proc. Roy. Soc. London Ser. A 450, no. 1938 (1995), 219–224. MR 96f:34041
[CKP] C. Camacho, N. Kuiper, J. Palis, La topologie du feuilletage d’un champ de vecteurs
holomorphes pr`es d’une singularit´e, C. R. Acad. Sci. Paris S´er. A-B 282, no. 17 (1976),
Ai, A959–A961. MR 54:1301
[CLW] S-N. Chow, Ch.Z. Li, D. Wang, Normal forms and bifurcation of planar vector ﬁelds,
Cambridge University Press, Cambridge, 1994. MR 95i:58161
[CM] D. Cerveau, R. Moussu, Groupes d’automorphismes de (C, 0) et ´equations
diﬀ´erentielles ydy + ·· · = 0, Bull. Soc. Math. France 116, no. 4 (1988), 459–488.
MR 90m:58192
[Co] W. A. Coppel, A survey of quadratic systems,J.Diﬀerential Equations 2 (1966), 293–
304. MR 33:4374
[CS] C. Camacho, P. Sad, Invariant varieties through singularities of holomorphic vector
ﬁelds, Ann. of Math. 115, no. 3 (1982), 579–595. MR 83m:58062
[CSc] C. Camacho, A. Scardua, Holomorphic foliations with Liouvillian ﬁrst integrals,Er-
godic Theory Dynam. Systems 21 (2001), no. 3, 717–756.
[CW] Lan Sun Chen, Ming Shu Wang, The relative position, and the number, of limit cy-
cles of a quadratic diﬀerential system, Acta Math. Sinica 22 (1979), 751–758. MR
81g:34031
[D] H. Dulac, Sur les cycles limite, Bull. Soc. Math France 51 (1923), 45–188.
[De] P. Deligne, ´Equations diﬀ´erentielles `a points singuliers r´eguliers, Lecture Notes in
Mathematics, 163, Springer-Verlag, Berlin, 1970, pp. iii+133. MR 54:5232
[Du] F. Dumortier, Singularities of vector ﬁelds on the plane,Equations 23, no. 1 (1977),
53–106. MR 58:31276
[DHP] F. Dumortier, Ch. Herssens, L. Perko, Local bifurcations and a survey of bounded
quadratic systems, Diﬀerential Equations 165, no. 2 (2000), 430–467. MR 2001i:37074
[DIR] F. Dumortier, Yu. Ilyashenko, C. Rousseau, Normal forms near a saddle-node and
applications to ﬁnite cyclicity of graphics, Preprint (2000), 29 pp. CRM-2697.
[DMR] F.Dumortier, M.ElMorsalami,C.Rousseau, Hilbert’s 16th problem for quadratic
systems and cyclicity of elementary graphics, Nonlinearity 9 (1996), 1209–1261. MR
97g:58136
[DRR] F. Dumortier, R. Roussarie, C. Rousseau, Hilbert’s 16th problem for quadratic vector
ﬁelds, Diﬀerential Equations 110, no. 1 (1994), 86–133. MR 95g:58179
[DRRa] F. Dumortier, R. Roussarie, C. Rousseau, Elementary graphics of cyclicity 1 and 2,
Nonlinearity 7 (1994), no. 3, 1001–1043. MR 95d:58095
[DRS] F. Dumortier,R.Roussarie, J. Sotomayor, Bifurcations of cuspidal loops, Nonlinearity
10, no. 6 (1997), 1369–1408. MR 98k:58167
[DRSZ] F. Dumortier, R. Roussarie, J. Sotomayor, H. Zoladek, Bifurcations of planar vector
ﬁelds. Nilpotent singularities and Abelian integrals, Lecture Notes in Mathematics,
Springer-Verlag, Berlin, 1991. MR 93f:58165
[E81a] J. ´Ecalle, Les fonctions r´esurgentes. Tome I Les alg`ebres de fonctions r´esurgentes,
Universit´e de Paris-Sud, D´epartement de Math´ematique, Orsay, 1981. MR 84h:30077a
[E81b] J. ´Ecalle, Les fonctions r´esurgentes. Tome II, Les fonctions r´esurgentes appliqu´ees `a
l’it´eration,Universit´e de Paris-Sud, D´epartement de Math´ematique, Orsay, 1981. MR
84h:30077b

350 YU. ILYASHENKO

[E85] J. ´Ecalle, Les fonctions r´esurgentes. Tome III, L’´equation du pont et la classiﬁcation
analytique des objects locaux,Universit´e de Paris-Sud, D´epartement de Math´ematiques,
Orsay, 1985. MR 87k:32009
[E92] J. ´Ecalle, Introduction aux fonctions analysables et preuve constructive de la conjecture
de Dulac (French), Hermann, Paris, 1992. MR 97f:58104
[EISV] P. Elizarov, Yu. Ilyashenko, A. Shcherbakov, S. Voronin, Finitely generated groups of
germs of one-dimensional conformal mappings, and invariants for complex singular
points of analytic foliations of the complex plane, Nonlinear Stokes Phenomena, Amer.
Math. Soc., Providence, RI, 1993, pp. 57–105. MR 94e:3205
[EMMRa] J. ´Ecalle, J. Martinet, R. Moussu, J.-P. Ramis, Non-accumulation des cycles-limites.
I,C.R.Acad. Sci. ParisS´er. I Math. 304, no. 13 (1987), 375–377. MR 89i:58121a
[EMMRb] J. ´Ecalle, J. Martinet, R. Moussu, J.-P. Ramis, Non-accumulation des cycles-limites.
II, C.R.Acad. Sci. ParisS´er. I Math. 304, no. 14 (1987), 431–434. MR 89i:58121b
[F] R. Fedorov, Growth of the number of orbital topological types of planar polynomial
vector ﬁelds modulo limit cycles, Moscow Math. J., to appear.
[GLMM] A. Gasull, J. Llibre, V. Ma˜nosa, F. Ma˜nosas, The focus-centre problem for a type of
degenerate system, Nonlinearity 13, no. 3 (2000), 699–729. MR 2001b:34061
[Ga98] L. Gavrilov, Petrov modules and zeros of Abelian integrals, Bull. Sci. Math 122,no. 8
(1998), 571–584. MR 99m:32043
[Ga01] L. Gavrilov, The inﬁnitesimal 16th Hilbert problem in the quadratic case, Invent. Math.
143, no. 3 (2001), 449–497. CMP 2001:09
[Gb] A. Gabrielov, Projections of semianalytic sets (Russian), Funktsional. Anal. i Priloˇzen.
2, no. 4 (1968), 18–30. MR 39:7137
[G94] A. Glutsyuk, Hyperbolicity of phase curves of a general polynomial vector ﬁeld in Cn

(Russian), Funktsional. Anal. i Prilozhen 28, no. 2 (1994), 1–11. MR 95i:32045
[G96] A. Glutsyuk, Hyperbolicity of the leaves of a generic one-dimensional holomorphic
foliation on a nonsingular projective algebraic variety (Russian), Tr. Mat. Inst. Steklova
213 (1997), 90–111. MR 99m:32041
[G01] A. Glutsyuk, Nonuniformizable skew cylinders. A counterexample to the simultaneous
uniformization problem, C.R.Acad. Sci. ParisSer.IMath. 332, no. 3 (2001), 209–214.
MR 2002c:32045
[GI*] A. Glutsuk, Yu. Ilyashenko, Restricted version of the Inﬁnitesimal Hilbert 16th prob-
lem,toappear.
[GLW] ´E. Ghys, R. Langevin, P. Walczak, Entropie g´eom´etrique des feuilletages,Acta Math-
ematica 160, nos. 1-2 (1988), 105–142. MR 89a:57034
[GM] X. G´omez-Mont, The transverse dynamics of a holomorphic ﬂow, Annals of Mathe-
matics. Second Series 127, no. 1 (1988), 49–92. MR 89d:32049
[GR] A. Guzman, C. Rousseau, Genericity conditions for cyclicity of elementary graphics,
Diﬀerential Equations 155, no. 1 (1999), 44–72. MR 2000d:34066
[Gu] J. Guckenheimer, Hartman’s theorem for complex ﬂows in the Poincar´e domain,Com-
positio Math. 24 (1972), 75–82. MR 46:920
[H] D. Hilbert, Mathematical problems, Reprinted from Bull. Amer. Math. Soc. 8 (1902),
437–479, in Bull. Amer. Math. Soc. 37 (2000), 407–436. CMP 2000:17
[Hi-a] H. Hironaka, Resolution of singularities of an algebraic variety over a ﬁeld of charac-
teristic zero. I, Ann. of Math. 79 (1964), 109–203. MR 33:7333
[Hi-b] H. Hironaka, Resolution of singularities of an algebraic variety over a ﬁeld of charac-
teristic zero. II, Ann. of Math. 79 (1964), 205–326. MR 33:7333
[Ho] E. Horozov, Versal deformations of equivariant vector ﬁelds for cases of symmetry of
order 2 and 3 (Russian), Trudy Sem. Petrovsk. 5 (1979), 163–192. MR 80k:58079
[I69a] Yu. Ilyashenko, The appearance of limit cycles under a perturbation of the equation
dw/dz = −Rz/Rw,where R(z, w) is a polynomial (Russian), Mat. Sb. (N.S.) 78 (120)
no. 3 (1969), 360–373. MR 39:4479
[I69b] Yu. Ilyashenko, An example of equations dw/dz = Pn (z, w)/Qn (z, w) having a count-
able number of limit cycles and arbitrarily high Petrovski˘ı- Landis genus (Russian),
Mat. Sb. (N.S.) 80 (122), no. 3 (1969), 388–404. MR 41:3881
[I72] Yu. Ilyashenko, Algebraic unsolvability and almost algebraic solvability of the problem
for the center-focus (Russian), Funktsional. Anal. i Priloˇzen 6, no. 3 (1972), 30–37.
MR 47:3749

CENTENNIAL HISTORY OF HILBERT’S 16TH PROBLEM 351

[I77] Yu. Ilyashenko, Remarks on the topology of the singular points of analytic diﬀerential
equations in a complex domain, and Ladis’ theorem, Funktsional. Anal. i Priloˇzen. 11,
no. 2 (1977), 28–38, 95. MR 56:755
[I78a] Yu. Ilyashenko, Topology of phase portraits of analytic diﬀerential equations on a
complex projective plane (Russian), Trudy Sem. Petrovsk. no. 4 (1978), 83–136. MR
84k:58164
[I78b] Yu. Ilyashenko, Global and local aspects of the theory of complex diﬀerential equa-
tions, Proceedings of International Congress of Mathematicians, Helsinki, 1978, v. II,
Springer-Verlag, Berlin, 1979, pp. 821-826.
[I82] Yu. Ilyashenko, Singular points and limit cycles of diﬀerential equations in the real
and complex plane, Preprint NIVTS AN SSSR, Pushchino (1982), 38.
[I84] Yu. Ilyashenko, Limit cycles of polynomial vector ﬁelds with nondegenerate singular
points on the real plane (Russian), Funktsional. Anal. i Prilozhen. 18, no. 3 (1984),
32–42. MR 86a:34054
[I85] Yu. Ilyashenko, Dulac’s memoir “On limit cycles” and related questions of the local
theory of diﬀerential equations (Russian), Uspekhi Mat. Nauk 40, no. 6 (1985), 41–78.
MR 87j:34052
[I90] Yu. Ilyashenko, Finiteness theorems for limit cycles, Uspekhi Mat. Nauk 45,no. 2
(1990), 143–200. MR 92a: 58110
[I91] Yu. Ilyashenko, Finiteness theorems for limit cycles, American Mathematical Society,
Providence, RI, 1991. MR 92k:58221
[I93] Yu. Ilyashenko (editor), Nonlinear Stokes phenomena, American Mathematical Society,
Providence, RI, 1993. MR 93i:32002
[I00] Yu. Ilyashenko, Hilbert-type numbers for Abel equations, growth and zeros of holomor-
phic functions, Nonlinearity 13, no. 4 (2000), 1337–1342. MR 2001h:34047
[IK] Yu. Ilyashenko, V. Kaloshin, Bifurcation of planar and spatial polycycles: Arnold’s
program and its development, The Arnoldfest (Toronto, ON, 1997), Amer. Math. Soc.,
Providence, RI, 1999, pp. 241–271. MR 2001b:34064
[IKh] Yu. Ilyashenko, A. Khovanskii, Galois groups, Stokes operators and a theorem of Ramis
(Russian), Funktsional. Anal. i Prilozhen. 24, no. 4 (1990), 31–42. MR 92f:32038
[IL] Yu. Ilyashenko, W. Li, Nonlocal bifurcations, Mathematical Surveys and Monographs,
66, American Mathematical Society, Providence, RI, 1999. MR 99m:58139
[IP*] Yu. Ilyashenko, A. Panov, Some upper estimates of the number of limit cycles of planar
vector ﬁelds with applications to the Lienard equation,to appear.
[IPy95] Yu. Ilyashenko, A. Pyartli, The monodromy group at inﬁnity of a generic polynomial
vector ﬁeld on the complex projective plane, Russian J. Math. Phys. 2, no. 3 (1994),
275–315. MR 96e:34009
[IPy97] Yu. Ilyashenko, A. Pyartli, Rational diﬀerential equations with a nonfree monodromy
group at inﬁnity (Russian), Tr. Mat. Inst. Steklova 213 (1997), 50–67. MR 2001f:34174
[IS] I. Itenberg, E. Shustin, Singular points and limit cycles of planar polynomial vector
ﬁelds, Duke Math. J. 102 (2000), 1–37. MR 2001d:34049
[IYa91] Yu. Ilyashenko, S. Yakovenko, Finitely smooth normal forms of local families of dif-
feomorphisms and vector ﬁelds (Russian), Uspekhi Mat. Nauk 46, no. 1 (277) (1991),
3–39. MR 92i:58165
[IYa95a] Yu. Ilyashenko, S. Yakovenko, Finite cyclicity of elementary polycycles in generic fam-
ilies, Concerning the Hilbert 16th problem, vol. 165, Amer. Math. Soc. Transl. Ser. 2,
Amer. Math. Soc., Providence, RI, 1995, pp. 21–95. MR 96b:34042
[IYa95b] Yu. Ilyashenko, S. Yakovenko, Double exponential estimate for the number of zeros of
complete abelian integrals and rational envelopes of linear ordinary diﬀerential equa-
tions with an irreducible monodromy group, Invent. Math. 121, no. 3 (1995), 613–650.
MR 96g:58157
[IYa95c] Yu. Ilyashenko, S. Yakovenko, editors, Concerning the Hilbert 16th problem,American
Mathematical Society, Providence, RI, 1995. MR 96j:34057
[IYa96] Yu. Ilyashenko, S. Yakovenko, Counting real zeros of analytic functions satisfying linear
ordinary diﬀerential equations, Diﬀerential Equations 126, no. 1 (1996), 87–105. MR
97a:34010

352 YU. ILYASHENKO

[JKM] A. Jacquemard, F. Z. Khechichine-Mourtada, A. Mourtada, Algorithmes formels ap-
pliqu´es `al’´etude de la cyclicit´e d’un polycycle alg´ebrique g´en´erique `a quatre sommets
hyperboliques, Nonlinearity 10, no. 1 (1997), 19–53. MR 98b:58142
[K*] V. Kaloshin, Hilbert 16th problem and an estimate for cyclicity of an elementary poly-
cycle,to appear.
[Kh84] A. Khovanskii, Real analytic manifolds with the property of ﬁniteness, and complex
abelian integrals (Russian), Funktsional. Anal. i Prilozhen. 18, no. 2 (1984), 40–50.
MR 86a:32024
[Kh91] A. Khovanskii, Fewnomials, Translations of Mathematical Monographs, 88, American
Mathematical Society, Providence, RI, 1991. MR 92h:14039
[KS] A. Kotova, V. Stanzo, On few-parameter generic families of vector ﬁelds on the two-
dimensional sphere, Concerning the Hilbert 16th problem, vol. 165, Amer. Math. Soc.
Transl. Ser. 2, Amer. Math. Soc., Providence, RI, 1995, pp. 155–201. MR 96i:34055
[K-V] M.G. Khudai-Verenov, A property of the solutions of a diﬀerential equation (Russian),
Mat. Sb. 56 (1962), 301–308.
[La] N. Ladis, Topological equivalence of hyperbolic linear systems, Diﬀerencial’nye Urav-
nenija 13, no. 2 (1977), 255–264, 379–380. MR 58:1396
[Le] Leau, ´Etude sur les ´equation fonctionelles `a une ou plusie`ere variables, Ann. Fac. Sci.
Toulouse 11 (1897), E1–E110.
[Lef] S. Lefchetz, On a theorem of Bendixson,J. Diﬀ. Equat. 4 (1968), 66–101. MR 36:2879
[L] E. Leontovich, On the generation of limit cycles from separatrices (Russian), Doklady
Akad. Nauk SSSR (N.S.) 78 (1951), 641–644. MR 13:132b
[LMP] A. Lins, W. de Melo, C. C. Pugh, On Li´enard’s equation, Lecture Notes in Math., 597,
Springer, Berlin, 1977, pp. 335–357. MR 56:6730
[LN80] A. Lins Neto, On the number of solutions of the equation dx/dt = ∑n
j=0 aj (t)xj ,
0 ≤ t ≤ 1,for which x(0) = x(1), Invent. Math. 59, no. 1 (1980), 67–76. MR 81i:34009
[LN94] A. Lins Neto, Simultaneous uniformization for the leaves of projective foliations by
curves, Bol. Soc. Brasil. Mat. (N.S.) 25, no. 2 (1994), 181–206. MR 95k:32034
[LN00] A. Lins Neto, Uniformization and the Poincar´e metric on the leaves of a foliation by
curves, Bol. Soc. Brasil. Mat. (N.S.) 31, no.3 (2000), 351–366. MR 2002c:37069
[LR] F. Loray, J.C. Rebello, Stably chaotic rational vector ﬁelds on CPn,Stony Brook IMS
preprint no. 2000/5 (2000).
[LSSc] A. Lins Neto, P. Sad, B. Scardua, On topological rigidity of projective foliations, Bull.
Soc. Math. France 126, no. 3 (1998), 381–406. MR 2000b:32027
[Ma] B. Malgrange, Travaux d’ ´Ecalle et de Martinet-Ramis sur les syst´emes dynamiques
(French), Bourbaki Seminar, Ast´erisque 92–93 (1982), 59–73. MR 84m:58023
[Mar] P. Mardesi´c, An explicit bound for the multiplicity of zeros of generic Abelian integrals,
Nonlinearity 4, no. 3 (1991), 845–852. MR 92h:58163
[MM] J.-F. Mattei, R. Moussu, Holonomie et integrales premi´eres (French), Ann. Sci. ´Ecole
Norm. Sup. (4) 13, no. 4 (1980), 469–523. MR 83b:58005
[MR82] J. Martinet, J-P. Ramis, Probl´emes de modules pour des equations diﬀerentielles non
lineaires du premier ordre (French), Inst. Hautes ´Etudes Sci. Publ. Math. 55 (1982),
63–164. MR 84k:34011
[MR83] J. Martinet, J-P. Ramis, Classiﬁcation analytique des equations diﬀerentielles non
lineaires resonnantes du premier ordre (French), Ann. Sci. Ecole Norm. Sup. (4) 16,
no. 4 (1983), 571–621. MR 86k:34034
[M92] N. Medvedeva, The principal term of the monodromy transformation of a monodromic
singular point is linear (Russian), Sibirsk. Mat. Zh. 33, no. 2 (1992), 116–124. MR
93f:58200
[M96] N. Medvedeva, The principal term of the asymptotics of the monodromy transforma-
tion: computation by the Newton diagram (Russian), Proc. Steklov Inst. Math 213
(1996), 212–223. MR 2000g:34048
[MMa*] N. Medvedeva, E. Mazaeva, Suﬃcient condition for a monodromic singular point to
be a focus, Transactions of Moscow Math. Soc. (to appear).
[Mo] A. Mourtada, Cyclicite ﬁnie des polycycles hyperboliques de champs de vecteurs du
plan. Algorithme de ﬁnitude (French), Ann. Inst. Fourier 41, no. 3 (1991), 719–753.
MR 93e:58155

CENTENNIAL HISTORY OF HILBERT’S 16TH PROBLEM 353

[MRo] R.Moussu, C.Roche, Th´eorie de Hovanski˘ıet probl`eme de Dulac, Inventiones Math-
ematicae 105, no. 2 (1991), 431–441. MR 92e:58169
[MS] J.F. Mattei, E. Salem, Complete systems of topological and analytical invariants for a
generic foliation of (C2, 0), Math. Res. Lett. 4, no. 1 (1997), 131–141. MR 98a:32044
[Mu] B. Muller, On the density of solutions of an equation in CP 2,Mat. Sbornik 98,no. 3
(1975), 325–338.
[Muc] J. Muci˜no-Raymundo, Deformations of holomorphic foliations having a meromorphic
ﬁrst integral,Journal f¨ur die Reine und Angewandte Mathematik 461 (1995), 189–219.
MR 96e:32026
[N] I. Nakai, Separatrices for nonsolvable dynamics on C, 0, Ann. Inst. Fourier 44 (1994),
no. 2, 569–599. MR 95j:58124
[Na] V. Naishul, Topological invariants of analytic and area-preserving mappings and their
application to analytic diﬀerential equations in C2 and CP 2 (Russian), Trudy Moskov.
Mat. Obshch. 44 (1982), 235–245. MR 84f:58092
[NYa95] D. Novikov, S. Yakovenko, Simple exponential estimate for the number of real zeros of
complete Abelian integrals, Ann. Inst. Fourier 45, no. 4 (1995), 897–927. MR 97b:14053
[NYa99a] D. Novikov, S. Yakovenko, Tangential Hilbert problem for perturbations of hyperelliptic
Hamiltonian systems, Electron. Res. Announc. Amer. Math. Soc. 5 (1999), 55–65. MR
2000a:34065
[NYa99b] D. Novikov, S. Yakovenko, Trajectories of polynomial vector ﬁelds and ascending chains
of polynomial ideals, Ann. Inst. Fourier 49, no. 2 (1999), 563–609. MR 2001h:32054
[NYa*] D. Novikov, S. Yakovenko, Redundant Picard–Fuchs system for Abelian integrals,to
appear.
[O-B] L. Ortiz-Bobadilla, Quadratic vector ﬁelds in CP 2 with two saddle-node type singular-
ities at inﬁnity, Dynam. Control Systems 1, no. 3 (1995), 295–317. MR 97a:58152
[P] A. Panov, Variety of Poincar´e mappings for cubic equations with variable coeﬃcients
(Russian), Funktsional. Anal. i Prilozhen 33, no. 4 (1999), 84–88. MR 2001f:34076
[Pe] G. Petrov, Elliptic integrals and their nonoscillation (Russian), Funktsional. Anal. i
Prilozhen. 20, no. 1 (1986), 46–49. MR 87f:5803
[PL1] I. Petrovskii, E. Landis, On the number of limit cycles of the equation dy/dx = P (x, y)/
Q(x, y),where P and Q are polynomials of 2nd degree (Russian), Mat. Sb. N.S. 37(79)
(1955), 209–250. MR 17:364d
[PL2] I. Petrovskii, E. Landis, On the number of limit cycles of the equation dy/dx = P (x, y)/
Q(x, y),where P and Q are polynomials (Russian), Mat. Sb. N.S. 85 (1957), 149–168.
MR 19:746c
[P-M] R. Perez-Marco, Fixed points and circle maps,Acta Math. 179, no. 2 (1997), 243–294.
MR 99a:58130
[Pu] I. Pushkar’, A multidimensional generalization of Ilyashenko’s theorem on abelian in-
tegrals (Russian), Funktsional. Anal. i Prilozhen. 31, no. 2 (1997), 34–44, 95. MR
98k:58183
[Py] A. Pyartli, Rational diﬀerential equations with a commutative monodromy group at
inﬁnity, Trans. Moscow Math. Soc. 61 (2000), 67–95.
[R86] R. Roussarie, On the number of limit cycles which appear by perturbation of separatrix
loop of planar vector ﬁelds, Bol.Soc.Brasil. Mat. 17, no. 2 (1986), 67–101. MR
88i:34061
[R88] R. Roussarie, A note on ﬁnite cyclicity property and Hilbert’s 16th problem,Lecture
Notes in Math., 1331, Springer, Berlin, 1986, pp. 161–168. MR 90b:58227
[R89] R. Roussarie, Cyclicit´e ﬁnie des lacets et des points cuspidaux, Nonlinearity 2,no. 1
(1989), 73–117. MR 90m:58169
[R98] R. Roussarie, Bifurcation of planar vector ﬁelds and Hilbert’s sixteenth problem,
Birkhauser Verlag, Basel, 1998. MR 99k:58129
[RSZ] C. Rousseau, G. ´Swirszcz, H. Zoladek, Cyclicity of graphics with semi-hyperbolic points
inside quadratic systems, Dynam. Control Systems 4, no. 2 (1988), 149–189. MR
99h:58149
[S] S. Smale, Mathematical problems for the next century, Math. Intelligencer 20,no. 2
(1998), 7–15. MR 99h:01033

354 YU. ILYASHENKO

[Sa] A. Sadovskii, A problem of distinguishing the center and focus for a case of a complex
singular point (Russian), Diﬀerentsial’nye Uravneniya 22, no. 5 (1986), 789–794. MR
87h:34042
[Se] A. Seidenberg, Reduction of singularities of the diﬀerential equation Adx = Bdy,Amer.
J. Math. 90 (1968), 248–269. MR 36:3762
[Sh] S. Shahshahani, Periodic solutions of polynomial ﬁrst order diﬀerential equations,Non-
linear Anal. 5, no. 2 (1981), 157–165. MR 82d:34052
[Shch82] A. Shcherbakov, Density of the orbit of a pseudogroup of conformal mappings and
generalization of the Khudai-Verenov theorem (Russian), Vestnik Moskov. Univ. Ser. I
Mat. Mekh. (1982), no. 4, 10–15. MR 84m:30015
[Shch84] A. Shcherbakov, Topological and analytic conjugation of noncommutative groups of
germs of conformal mappings (Russian), Trudy Sem. Petrovsk. no. 10 (1984), 170–
196, 238–239. MR 86g:58083
[Shi] Song Ling Shi, A concrete example of the existence of four limit cycles for plane
quadratic systems, Sci. Sinica 23 (1980), 153–158. MR 81f:34037
[Si] M. Singer, Liouvillian ﬁrst integrals of diﬀerential equations., Trans. Amer. Math. Soc.
333 (1992), 673–688. MR 92m:12014
[SRO] A. Shcherbakov, E. Rosales-Gonzalez, L. Ortiz-Bobadilla, Countable set of limit cycles
for the equation dw/dz = Pn(z, w)/Qn(z, w), Dynam. Control Systems 4, no. 4 (1998),
539–581. MR 99m:58150
[St] S. Sternberg, On the structure of local homeomorphisms of Euclidean n-space,II. Amer.
J. Math. 80 (1958), 623–631. MR 20:3336
[SV] J. Seade, A. Verjovsky, Actions of discrete groups on complex projective spaces,Lami-
nations and foliations in dynamics, geometry and topology (Stony Brook, NY, 1998),
Contemp. Math. 269, Amer. Math. Soc., Providence, RI, 2001, pp. 155–178.
[T] F. Takens, Forced oscillations and bifurcations, Comm. Math. Inst. Rijksuniv. Utrecht,
Math. Inst. Rijksuniv. Utrecht 3 (1974), 1–59. MR 57:17720
[Ti] E. Titˇcmarˇs, Teoriya funktsii (Translated from the English), Nauka, Moscow, 1980.
MR 82b:30001
[Tr] S. Trifonov, Cyclicity of elementary polycycles of generic smooth vector ﬁelds,Proc.
Steklov Inst. Math. 213, no. 2 (1996), 141–199. MR 99i:58115
[V] A. Varchenko, Estimation of the number of zeros of an abelian integral depending on a
parameter, and limit cycles (Russian), Funktsional. Anal. i Prilozhen. 18, no. 2 (1984),
14–25. MR 85g:32033
[Ve] A. Verjovsky, Private communication.
[Vo] S. Voronin, Analytic classiﬁcation of germs of conformal mappings (C, 0) → (C, 0)
(Russian), Funktsional. Anal. i Prilozhen. 15, no. 1, (1981), 1–17. MR 82h:58008
[Y] J.-Ch. Yoccoz, Th´eor`eme de Siegel, nombres de Bruno et polynˆomes quadratiques.
Petits diviseurs en dimension 1, Ast´erisque no. 231 (1995), 3–88. MR 96m:58214
[Ya95] S. Yakovenko, A geometric proof of the Bautin theorem, Concerning the Hilbert 16th
problem, Amer. Math. Soc, Providence, RI, 1995, pp. 203–219. MR 96j:34056
[Ya99] S. Yakovenko, On functions and curves deﬁned by ordinary diﬀerential equations,The
Arnoldfest (Toronto, ON, 1997), Amer. Math. Soc. , Providence, RI, 1999, pp. 497–525.
MR 2001k:34065
[Z83] H. Zoladek, Versality of a family of symmetric vector ﬁelds on the plane (Russian),
Mat. Sb. (N.S.) 120(162), no. 4 (1983), 473–499. MR 84i:58094
[Z87] H. Zoladek, Bifurcations of certain family of planar vector ﬁelds tangent to axes,Dif-
ferential Equations 67, no. 1 (1987), 1–55. MR 89e:58086

Department of Mathematics, Cornell University, Ithaca, New York 14853
E-mail address: yulij@math.cornell.edu
Current address: Moscow State and Independent Universities, Steklov Mathematical Institute,
Moscow (MIAN) Gubkina st. 8, Moscow, Russia, 117966
E-mail address: yulijs@mccme.ru
