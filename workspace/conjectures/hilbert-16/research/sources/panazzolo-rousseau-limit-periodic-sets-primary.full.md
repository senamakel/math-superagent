<!-- source: https://arxiv.org/pdf/1702.04965 | converted from PDF -->

arXiv:1702.04965v2  [math.CA]  14 Nov 2017
TOPOLOGICAL CLASSIFICATION OF LIMIT PERIODIC SETS
OF POLYNOMIAL PLANAR VECTOR FIELDS

ANDR´E BELOTTO DA SILVA AND JOSE GIN´ES ESP´IN BUEND´IA

Abstract

We characterize the limit periodic sets of families of algebraic planar vector
ﬁelds up to homeomorphisms. We show that any limit periodic set is topologically
equivalent to a compact and connected semialgebraic set of the sphere of dimension
0 or 1. Conversely, we show that any compact and connected semialgebraic set of
the sphere of dimension 0 or 1 can be realized as a limit periodic set.

1. Introduction

The subject of this manuscript is the structure of limit periodic sets of planar
polynomial vector ﬁelds, a central object in bifurcation theory and in the treat-
ment of the Hilbert 16th problem (see Roussarie’s book [15] or Il’yashenko and
Yakovenko’s book [7]). For example, the program of Dumortier, Roussarie and
Rousseau [6] to solve the existential part of the 16th Hilbert problem for quadratic
vector ﬁelds is divided in 121 case-by-case analysis based on the limit periodic sets.
Following the spirit of [9], [10] or [13], our objective is to characterize topologically
all limit periodic sets of polynomial families of planar vector ﬁelds.
We consider a real algebraic manifold Λ of dimension n ≥ 1, which we call
parameter space. A family of planar vector ﬁelds (Xλ)λ∈Λ, is a vector ﬁeld Xλ
deﬁned on R2 × Λ which is tangent to the ﬁbres of the projection π : R2 × Λ → Λ.
For any parameter λ0 ∈ Λ, we denote by Xλ0 the restriction of Xλ to R2 × {λ0},
which we identify with R2. We say that the family (Xλ)λ∈Λ is polynomial if for each
λ0 ∈ Λ there exist local coordinate systems x = (x1, x2) of R2 and λ = (λ1, . . . , λn)
centered at λ0 such that Xλ(x) = A1(x, λ)∂x1 + A2(x, λ)∂x2 where A1 and A2 are
polynomials.
Given any polynomial vector ﬁeld X on R2, we shall extend it to an analytic
vector ﬁeld, which we denote by ˆX, in the sphere S
2 via a Bendixson compactiﬁca-
tion (see details in Section 2.1). Also, for every A ⊂ R2, we will write ˆA to denote
the closure of A seen as a subset in the one-point compactiﬁcation S
2 of R2.
We recall the deﬁnition of limit periodic sets, which was ﬁrst introduced by
Fran¸coise and Pugh [8, pp. 141].

Deﬁnition 1.1. A limit periodic set for a polynomial family of planar vector ﬁelds
(Xλ)λ∈Λ at the parameter λ0 is a closed set Γ ⊂ R2 for which there exist a sequence
(λn)n in the parameter space Λ and a sequence (γn)n of topological circles in R2

2010 Mathematics Subject Classiﬁcation. Primary 34C07, 34C08; Secondary 14P10, 37G15.
Key words and phrases. Limit Periodic Sets, Ordinary Diﬀerential Equations, Semi-algebraic
sets.
 1

2 A. BELOTTO AND J. G. ESP´IN

such that (λn)n converges to λ0 in Λ, (γn)n converges to ˆΓ in the Hausdorﬀ topology
of S
2 and, for every n, the vector ﬁeld Xλn has γn as a limit cycle.

In terms of the structure of limit periodic sets, it is well-known that the Poincar´e-
Bendixson Theorem implies:

Proposition 1.2. (See [8, Proposition 1]) Let (Xλ)λ∈Λ be a polynomial family of
planar vector ﬁelds and Γ be a limit periodic set at the parameter λ0. Then ˆΓ is
one of the following: (i) a singular point of ˆXλ0; (ii) a periodic orbit of ˆXλ0; (iii)
a polycycle of ˆXλ0 (that is, a cyclic ordered collection of singular points a1, . . . , ak
and arcs, given by integral curves, connecting them in the speciﬁc order: the jth arc
connects aj with aj+1); (iv) a degenerate limit cycle, that is, it contains non-isolated
singularities of the vector ﬁeld ˆXλ0 .

While the above Proposition provides some key information about the nature of
limit periodic sets, it does not fully characterize them. The present paper intends
to fulﬁls this gap. A ﬁrst characterization was provided by Panazzolo and Roussarie
in [14], under the additional hypothesis that the ﬁrst jet of the singular points of
Xλ0 is non-vanishing. In the same paper, the authors also showed a ﬁrst example
of a limit periodic set which is not topologically in the list of possibilities of the
Poincar´e-Bendixson Theorem [14, Example 3.1]. Going further, in [2], the ﬁrst
author has presented a class of examples of limit periodic sets which, topologically,
are not in the list of possibilities of Poincar´e-Bendixson Theorem either. Here, we
improve and generalize the construction of [2] in order to prove the converse of our
main result:

Theorem 1.3. Let (Xλ)λ∈Λ be a polynomial family of planar vector ﬁelds and Γ a
limit periodic set. Then there exists a homeomorphism ϕ : S
2 → S
2 such that ϕ(ˆΓ)
is a compact and connected semialgebraic set of dimension 0 or 1.
Conversely, if Γ is a non-empty closed semialgebraic subset of R2 of dimension
0 or 1 whose compactiﬁcation ˆΓ ⊂ S
2 is connected, there exists a polynomial family
of planar vector ﬁelds (Xλ)λ∈Λ having Γ as a limit periodic set.

The following example illustrates the construction performed in Section 3 to
prove the converse of Theorem 1.3.

Example 1.4. Let Γ ⊂ R2 be the semi-algebraic set given by:

Γ = {
(x, y) ∈ R2; f (x, y) = y(x
2 + y2 − 1) = 0 and g(x, y) = x
2 + y2 ≤ 4} .

Following the notation of Subsection 3.2, we consider the set of points

S = {(−2, 0), (2, 0), (0, 1), (0, −1)}

(where notice that S = Gen(Γ) ∪ T r(Γ) and N G(Γ) = ∅, see Deﬁnition 3.1). Now,
consider the three variable polynomial

h(x, y, λ) = f (x, y)
2 − λ ∏

p∈S
 (
∥(x, y) − p∥2 − λ
2)

where λ will play the role of the parameter of the family of vector ﬁelds. Let t ∈ R+

and note that the level curves Zt = {(x, y) ∈ R2; h(x, y, t) = 0} are connected and
converge (in the Hausdorﬀ topology) to Γ when t goes to zero (c.f. Proposition 3.7;

TOPOLOGICAL CLASSIFICATION OF LIMIT PERIODIC SETS 3

Γ

Figure 1. Limit cycles for λ = 0.001 (red) and λ = 0.0001 (blue)
approaching the limit periodic set Γ.

see Figure 1). It follows that the perturbation of the Hamiltonian vector ﬁeld given
by
 Xλ = ( ∂h
∂y + h ∂h
∂x
 ) ∂x + (
− ∂h
∂x + h ∂h
∂y
 ) ∂y

is an polynomial family of planar vector ﬁelds which has Γ as a limit periodic set
for the parameter λ0 = 0 (for every t > 0, the set Zt is a limit cycle for Xt).

The rest of the paper is divided as follows. In Subsection 1.1 we present some
remarks about Theorem 1.3; the aim of Section 2 is to prove the direct implication
of Theorem 1.3 while Section 3 deals with the converse one.

1.1. Remarks.

(I) If we restrict our study to compact limit periodic sets of the plane, Theorem
1.3 can be extended to the analytic category. More precisely, with the same
ideas and techniques, it is not diﬃcult to show that a compact limit periodic
set for an analytic family of vector ﬁelds is topologically equivalent to a
compact and connected semianalytic set of dimension 0 or 1; conversely,
every compact and connected semianalytic set of dimension 0 or 1 can be
realized as a limit periodic set for an analytic family of vector ﬁelds.
(II) On the other hand, Theorem 1.3 does not extend, in a trivial, to unbounded
limit periodic sets for families of analytic vector ﬁelds. The diﬃculty relies
on proving the converse part of the theorem. Let us ﬁrst exemplify how
our methods could be adapted to some unbounded analytic varieties: we
claim that the set

Γ1 = {(x, y) ∈ R2; f1(x, y) = y2 − sin(x)
2 = 0}

can be realized as a limit periodic set for an analytic family. Indeed, it
suﬃces to replace the function h in Section 3.2 by

h(x, y, λ, α) = f1(x, y)
2 − λ (
1 − α
2(x
2 + y2)
) .

We leave it to the reader to verify that the ideas of Sections 3.2 and 3.3 can
be adapted to this function. Nevertheless, it is unclear which connected
subsets of

Γ2 = {(x, y) ∈ R2; f2(x, y) = y3 − y sin(x)
2 = 0}

4 A. BELOTTO AND J. G. ESP´IN

can be realized as limit periodic sets. Technically, the diﬃculty is that our
construction for Γ2 would demand the use of transition points (deﬁned in
the last paragraph of Section 3.1); but the set of those transition points
T r(Γ2) would need to be inﬁnite in this case.
(III) A description of the limit periodic sets Γ in the spirit of Proposition 1.2
follows, under the hypotehsis thatXλ0 ̸≡ 0, from the proof of Lemma 2.6
below. More precisely, with the notation of the direct implication in The-
orem 1.3, a limit periodic set Γ must be a ﬁnite union ⋃m
i=1 Si ∪ ⋃n
j=1 γj,
for some m, n ∈ N, where each Si is a connected semi-algebraic subsets of
the set of singularities of ˆXλ0 and each γj is a regular orbit of ˆXλ0 which
converge to a singular points in ⋃m
i=1 Si. Even more, each γj is character-
istic in both extremes; that is, when the orbit is run in either negative or
positive time, the orbit converges in a well-deﬁned direction to a singular
point of ˆXλ0 and, in a suﬃciently small neighbourhood of that limit point,
γj is the frontier of a parabolic or hyperbolic sector.

Acknowledgements. We would like to thank the anonymous referee for the useful
comments and the University of Toronto for its hospitality. The work of the ﬁrst
author is supported by LabEx CIMI. The second author is supported by Fundaci´on
S´eneca through the program “Contratos Predoctorales de Formaci´on del Personal
Investigador”, grant 18910/FPI/13 and by the MINECO grants MTM2014-52920-
P.
 2. Topology of limit periodic Sets

Along the Section, the reader is assumed to be familiar with some background
in elementary Planar Qualitative Theory of Diﬀerential Equations; regarding this,
[5] is a good reference.
In Subsection 2.1, we recall the constructions of the Bendixson compactiﬁcation
of a polynomial vector ﬁeld on R2. Subsection 2.2 is devoted to present the notion
of real semialgebraic sets and some of their elementary properties and, ﬁnally, in
Subsection 2.3, we prove the direct part of Theorem 1.3

2.1. Bendixson Compactiﬁcation. For the sake of simplicity, we present an
adaptation of [15, Section 1.1.3.2] using real analysis notation.
The one-point compactiﬁcation of the euclidean plane R2
∞ = R2 ∪ {∞} can be
seen as a real analytic compact surface. Indeed, it is enough to consider the two local
charts (R2, z) and (R2
∞ \ {0}, Z) where z : R2 → R2 is the map given by the formula
z(x, y) = (r(x, y), s(x, y)) = (x, y) for every (x, y) ∈ R2 and Z : R2
∞ \ {0} → R2

is given by Z(x, y) = (u(x, y), v(x, y)) = (x/(x
2 + y2), −y/(x
2 + y2)) if (x, y) ̸= ∞
and Z(∞) = (u(∞), v(∞)) = 0. The equations for the changes of coordinates
z ◦ Z −1 : R2 \ {0} → R2 \ {0} and Z ◦ z−1 : R2 \ {0} → R2 \ {0} are given by
the analytic formulas r = u/(u2 + v2) and s = −v/(u2 + v2) and u = r/(r2 + s2)
and v = −s/(r2 + s2) respectively; this justiﬁes that {(R2, z), (R2
∞ \ {0}, Z)} is an
analytic atlas for R2
∞. We denote by φ : R2
∞ → R2
∞ the homeomorphism associated
to this transition map (where φ(0) = ∞ and φ(∞) = 0; ; we will call φ the transition
homeomorphism associated to the Bendixson compactiﬁcation.
We will also refer to R2
∞ as S
2 and we shall call it the Bendixson compactiﬁcation
of R2. This notation is justify by the fact that R2
∞ is analytically diﬀeomorphic
to the standard euclidean unit sphere S
2 = {(x, y, z) ∈ R3 : x
2 + y2 + z2 = 1}:

TOPOLOGICAL CLASSIFICATION OF LIMIT PERIODIC SETS 5

as a explicit analytic diﬀeomorphism we may consider the map ψ : S
2 → R2
∞
given by the formulas ψ(0, 0, 1) = ∞ and ψ(x, y, z) = (x/(1 − z), y/(1 − z)) if
(x, y, z) ̸= (0, 0, 1). If we denote by d2 the standard euclidean distance on R3, it
follows that R2
∞, with its natural topology as the one-point compactiﬁcation of R2,
is a metrizable space; and as a compatible distance we can take the one given by
d(a, b) = d2(ψ−1(a), ψ−1(b)) for every a, b ∈ R2
∞.
Let P and Q be real polynomials in two variables and consider the algebraic
planar vector ﬁeld given by X = P ∂x + Q∂y. If d = max{deg(P ), deg(Q)}, we may
consider a vector ﬁeld in the ampliﬁed euclidean plane R2
∞, ˆX, given by the formulas
ˆX(r, s) = 1
1+(r2+s2)d (P (r, s)∂r + Q(r, s)∂s) if (r, s) ∈ R2
∞ \ {∞} and ˆX(∞) = 0. It

is direct to show that ˆX is well-deﬁned and analytic in the whole R2
∞.

2.2. Semialgebraic sets. Let x = (x1, . . . , xn) be a coordinate system of Rn.
Given any polynomial f on Rn we shall say that (f (x) = 0) = {x ∈ Rn : f (x) = 0}
is a algebraic set. A more general concept is the following one.

Deﬁnition 2.1. (See [3, Section 1]). A subset Z ⊂ Rn is semialgebraic if there
exist polynomials fi and gij on Rn, i = 1, . . . , p and j = 1, . . . , q, such that

Z =
 p⋃

i=1
 q⋂

j=1{x ∈ Rn : fi(x) = 0 and gij (x) > 0}.

A set Z ⊂ S
2 ⊂ R3 is said to be semialgebraic if Z is a semialgebraic set of R3.

A ﬁst collection of examples of semialgebraic sets is given by the ﬁnite unions of
arcs linear by parts. For every a, b ∈ R2, we will denote [a, b] = {a+ sb : 0 ≤ s ≤ 1},
the straight arc joining a and b. Let a1, . . . , an be points in R2 and call lj = [aj, aj+1]
for any 1 ≤ j ≤ n − 1. If lj ∩ lj′ = ∅ when |j − j′| ̸= 1 and lj ∩ lj+1 = {aj+1} for
any 1 ≤ j ≤ n − 1, we say that L = ∪
n−1
j=1 lj is an arc linear by parts. The points a1
and an are said to be the endpoints of L.
We next present a family of subsets of S
2 which are topologically equivalent to
semialgebraic sets.
Given any positive integer n ∈ N, we say that a topological space is an n-star if
it is homeomorphic to Sn = {z ∈ C : zn ∈ [0, 1]}. If Z is an n-star and h : Sn → X
is a homeomorphism, then the image of the origin under h is called a vertex of the
star while the components of Z \ {h(0)} are called the branches of the star. Note
that the vertex and the branches of a star are uniquely deﬁned except in the cases
n = 1, 2, when Z is just a closed arc and the vertexes are its endpoints (for n = 1)
or its interior points (for n = 2). We shall also adopt the convention of calling any
singleton a 0-star (the point being its vertex). When Y is a topological space and
a is a point in Y which posses a neighbourhood Z ⊂ Y being an n-star with a as
vertex, we will say that a is a star point in Y (of order n); if all the points in Y
are star points, we will say that Y is a generalized graph.
An important family of examples of generalized graphs is given by the set of
zeros of planar analytic maps.

Proposition 2.2. Let f : U → R be an analytic map in an open subset U ⊂ R2

and Z = {z ∈ U : f (z) = 0} be the set of zeros of f . Then either Z is a whole
connected component of U or Z is a generalized graph.

6 A. BELOTTO AND J. G. ESP´IN

Proof. The result follows as a consequence of the Weierstrass Preparation Theo-
rem and the theory of Puiseux Series (for a detailed record of the proof, see, for
example, [9, p. 687]). □

We focus on a special subfamily of generalized graphs which shall play an im-
portant part in the proof of Theorem 1.3.

Lemma 2.3. Let L ⊂ S
2 be a connected generalized graph. Then L is topologically
equivalent to a semialgebraic set; that is, there exists a homeomorphism of S
2 onto
itself taking L to a semialgebraic set.

Proof. Let us start by noticing that, apart from composing a rotation with the
transition homeomorphism φ : R2
∞ → R2
∞ associated to the Bendixson compactiﬁ-
cation (see Section 2.1), we may suppose that there exists a compact and connected
set Γ ⊂ R2 such that its completion in R2
∞ is equal to L. Also, if we call T ⊂ Γ
the subset of points which are not star points of order 2, then T is a ﬁnite set. It
is then enough to prove the result under the hypothesis of Γ being non-empty.
If T is empty, there is nothing to say: L is homeomorphic to {(x1, x2) ∈ R2 :
x
2
1 + x
2
2 = 0} [11, Theorem 2, p. 180]. Otherwise, let us say that T = {a1, . . . , am}
for some m ≥ 1. For every 1 ≤ j ≤ m we can take a neighbourhood Bj ⊂ R2 of
aj such that Bj ∩ T = {aj} and Bj ∩ Γ is an nj-star. Without lost of generality
we can also assume that, for every 1 ≤ j ≤ m, Bj is a standard euclidean compact
ball of center aj in R2, that ∂Bj meets Γ in exactly nj points bj,1, . . . , bj,nj and,
as a consequence, Bj ∩ Γ is homeomorphic to Mj = ∪
nj
k=1[aj, bj,k]. Now any of
the components of Γ \ ∪
m
j=1Bj is a generalized graph consisting only of star points
of order 2, let us say U1, . . . , Uτ are those components. For any 1 ≤ k ≤ τ , we
can take an arc linear by parts Nk whose endpoints coincide with the points in
Cl(Uk) \ Uk and such that ∪
m
j=1Mj ∪ ∪
τ
k=1Nk is homeomorphic to Γ. This last
homeomorphism can be extended to a homeomorphism from the sphere to the
sphere (see, for example, [1, Theorem 1]). □

2.3. Topological properties of periodic limit sets. Let {Xλ}λ∈Λ be a poly-
nomial family of planar vector ﬁelds and, for every λ ∈ Λ, let ˆXλ be the analytic
vector ﬁeld on S
2 described by the Bendixson compactiﬁcation as in Section 2.1
(we remark that pN = (0, 0, 1) is a singular point for every ˆXλ). Together with the
family { ˆXλ}λ∈Λ we may consider the associated analytic ﬂow Φ : R × S
2 × Λ → S
2.
The continuity of the ﬂow already gives some topological and dynamical ob-
structions for the limit periodic sets: a limit periodic set at a parameter λ0 must
be invariant for Xλ0 and its compactiﬁcation by one point must be connected.

Lemma 2.4. If Γ is a limit periodic set at the parameter λ0, then ˆΓ is connected
and invariant for ˆXλ0 (equivalently, Γ is invariant for Xλ0 ).

Proof. Let us start ﬁxing a sequence in Λ converging to λ0, (λn)n, and a sequence
of topological circles in R2, (γn)n, such that (ˆγn)n converges to ˆΓ in the Hausdorﬀ
topology of S
2 and, for every n, γn is a limit cycle of Xλn .
Firstly, we consider points a ∈ Γ and b = Φ(s, a, λ0) for some s ∈ R and a
sequence of points an ∈ γn converging to a. By the continuity of Xλ, the points
Φ(s, an, λn) converge to b so b ∈ ˆΓ.
Next, to obtain a contradiction, let us suppose that ˆΓ is not connected and choose
two disjoint open sets V1 and V2 of S
2 which disconnect ˆΓ. Since γn → ˆΓ in the

TOPOLOGICAL CLASSIFICATION OF LIMIT PERIODIC SETS 7

Hausdorﬀ topology, we conclude that γn ⊂ V1 ∪ V2, γn ∩ V1 ̸= ∅ and γn ∩ V2 ̸= ∅, for
n suﬃciently big. But this implies that γn is disconnected, which is impossible. □

From the analyticity of the ﬂow Φ (we only need to use that it is of class C1), the
following important local property is established: any limit periodic set can meet
at most once with any traversal. We formalize this property below.
Let I ⊂ R be an open interval and λ ∈ Λ. An embedding σ : I → S
2 of class C1

is called a transverse section of ˆXλ if, for any s ∈ I, the vectors ˙σ(s) and ˆXλ(σ(s))
are linearly independent. We shall also refer to σ(I) as a transverse section of ˆXλ.
If a ∈ S
2 is a regular point of ˆXλ0 , then we can always ﬁnd a positive real number
ε > 0 and an analytic embedding σ : (−ε, ε) → S
2 being a transverse section of ˆXλ0
with σ(0) = a. On the other hand, given any transverse section of ˆXλ0 , σ : I → S
2,
it is clear that for any t ∈ I we can take I(t), an open neighbourhood of t in I,
and Λ(λ0), a neighbourhood of λ0 in Λ, such that the restriction of σ to I(t) is a
transverse section of ˆXλ for every λ ∈ Λ(λ0). These observations, together with
the Flow Box Theorem and the fact that any periodic orbit of a C1 vector ﬁelds on
the sphere can meet any transverse section only once, give the following result.

Lemma 2.5. (see [15, Lemma 2, p. 20]) Let Γ be a limit periodic set at the
parameter λ0. Then any transverse section of ˆXλ0 meets ˆΓ at most once.

The last ingredient we need is the well-known behaviour of analytic vector ﬁelds
on the neighbourhood of isolated singular points, the so-called ﬁnite sectorial de-
composition property (see [5, pp. 17–19]): every suﬃciently small neighbourhood
of an isolated singular point of a planar analytic vector ﬁeld is either a center, a
focus or a ﬁnite union of hyperbolic, parabolic and elliptic sectors.
We are now ready to prove the direct implication of Theorem 1.3. The work is
done by the combination of Lemma 2.3 and the following result.

Lemma 2.6. Suppose that Γ is a limit periodic set at the parameter λ0 and that
Xλ0 ̸≡ 0. Then ˆΓ is a connected generalized graph.

Proof. According with Lemma 2.4, ˆΓ is a connected subset of S
2 which is a union
of orbits of ˆXλ0 . Therefore, we only need to prove that all the points of ˆΓ are star
points. We ﬁx a point a ∈ ˆΓ and we distinguish three cases.
If a is a regular point of ˆXλ0 , the Flow Box Theorem and Lemma 2.5 imply the
existence of a neighbourhood of a, Ua, such that ˆΓ ∩ Ua is a 2-star.
Let us now assume that a is an isolated singular point of ˆXλ0 and let Ua be a
neighbourhood of a such that every point in Ua \ {a} is a regular point of ˆXλ0 . If a
is a center (respectively a node or a focus) for ˆXλ0 , we can always ﬁnd a transverse
section accumulating at a and meeting at least once (respectively twice) any regular
orbits of ˆXλ0 in Ua so Lemma 2.5 guarantees that, after shrinking Ua if necessary,
ˆΓ ∩ Ua = {a}. Otherwise, we can consider characteristics orbits c0, . . . , cn−1, with
n ≥ 2, deﬁning a sectorial decomposition around a (we follow the notation of [5, pp.
17–19]). Using once again Lemma 2.5, we note that: at each parabolic sector there
may exist only one regular orbit contained in ˆΓ; at each hyperbolic sector, apart
from shrinking Ua, the intersection with ˆΓ can only be the characteristic orbits cj
deﬁning this sector; at each elliptic sector, apart from shrinking Ua and adding two
new parabolic sectors, we may suppose that the intersection of the elliptic sector

8 A. BELOTTO AND J. G. ESP´IN

with ˆΓ is empty. It follows from these observations that, also in this case, ˆΓ ∩ Ua is
a star of vertex a.
Finally, if a is a non-isolated singularity of ˆXλ0 , it is well known that there exist
a neighbourhood of a, Ua, an analytic map f : Ua → R and an analytic vector ﬁeld
Y on Ua such that the restriction of ˆXλ0 to Ua coincides with the product f Y and
the vector ﬁeld Y has no zeros in Ua \ {a} (e. g. see [9, Theorem 4.5]).
Let us denote by Z the analytic set f −1(0) and note that, after shrinking Ua if
necessary, Z is a star (with a as vertex) decomposing Ua into ﬁnitely many con-
nected components any of which contains no singular points for ˆXλ0 . Furthermore,
by analyticity, there is no loss of generality in assuming that the neighbourhood Ua
has been chosen such that each branch of Z is either invariant by Y or a transverse
section of Y (see for example [10, Lemma 3.2]). Accordingly, ˆΓ ∩ Ua is the union
of {a} with some of the branches of Z and some regular orbits of Y .
The above observation allow us to adapt the argument given in the ﬁrst two
cases, mutatis mutandis, to the case when a is a regular point of Y , or when Y
admits a sectorial decomposition at a (where we are again considering at least two
characteristic orbits and among them appear at least all the branches of Z \ {a}
which are invariant by Y ). We remark that the latter case includes the scenario of
a being a node point for Y .
Finally, if a is a center or a focus point of Y , it is elementary to show that in any
of the connected components of Ua\Z there exists a transverse section accumulating
at a and at the frontier of Ua. Consequently, in these two cases, it may be conclude
that, after shrinking Ua if necessary, ˆΓ ∩ Ua ⊂ Z and a is a star point. □

Proof of direct implication of Theorem 1.3. If Xλ0 ̸≡ 0, the result easily follows
from Lemmas 2.3 and 2.6. So, assume that Xλ0 ≡ 0.
The following argument is due to Roussarie [16, Section 3] and follows an original
idea of Bautin. Let Γ be the limit periodic set and

Xλ(x) = ∑

α∈N2 f1,α(λ) x
α ∂x1 + f2,α(λ) x
α ∂x2

We consider the ideal sheaf J generated by (f1,α(λ), f2,α(λ))α∈N2 . Note that λ0 is
in the support of this ideal by hypothesis.
Let (λn) be the sequence of parameters converging to λ0 and note that λn is
not contained in the support of J (because all ﬁbres which belongs to the support
of J are zero). Consider the monomialization σ : ̃Λ → Λ of the ideal sheaf J
(see, e.g. [4]) and denote by (̃λn) the pre-image of (λn) (which is well-deﬁned
because (λn) is not in the support of J ). Since σ is a proper map, there exists a
subsequence (̃λnk ) which converges to a parameter ̃λ0 ∈ σ−1(λ0). By construction,
moreover, in a neighbourhood U of ̃λ0 there exists a multi-index β ∈ Nn such that
σ∗(Xλ)|R2×U = ̃λ
β ̃X̃λ, where ̃X̃λ0 ̸≡ 0. We note that Γ is the limit periodic set of

σ∗(Xλ) for the parameter ̃λ0, and that the division of the locally deﬁned family by
the monomial ̃λ
β won’t change the topology of Γ. The result follows from the ﬁrst
part of the proof. □

3. Construction of limit periodic sets

TOPOLOGICAL CLASSIFICATION OF LIMIT PERIODIC SETS 9

3.1. Properties of semialgebraic sets. We are interested in planar semialgebraic
sets Γ ⊂ R2 of dimension 0 or 1. Associated to any of these sets, we introduce a
free-square polynomial whose set of zeros shall play an important role in the rest
of the paper.
Let us start ﬁxing a coordinate system for the plane x = (x1, x2) and let Γ ⊂
R2 be a semialgebraic set of dimension 0 or 1 and whose compactiﬁcation ˆΓ is
connected. If Γ is itself an algebraic set we simply take a free-squared polynomial
fΓ making (fΓ(x) = 0) = Γ. Assume now that Γ is not an algebraic set; in
particular, and because ˆΓ is connected, we note that none of the components of Γ
can be singletons. Let fi and gi,j, 1 ≤ i ≤ p and 1 ≤ j ≤ q, be polynomials such
that

(3.1) Γ =
 p⋃

i=1
 q⋂

j=1{x ∈ R2 : fi(x) = 0 and gij(x) > 0}.

Without lost of generality, we can assume that all the fi are irreducible and also,
because Γ has empty interior, that all of them are non-constant and (fi(x) = 0) ∩ Γ
is one dimensional. Using the well-known fact that any two co-prime polynomials
on R2 can meet only ﬁnitely many times, it is not diﬃcult to reason that under such
conditions the polynomials fi in (3.1) are uniquely deﬁned (up to the multiplication
of non-zero constants). Let us take fΓ as the free-square polynomial associated to
the product ∏p
i=1 fi; this polynomial veriﬁes Γ ⊂ (fΓ(x) = 0) and is uniquely
deﬁned from (3.1) in the terms just expressed. In any of the two cases discussed
above, we shall refer to the polynomial fΓ as the polynomial associated to Γ. The
set of zeros of fΓ, which we shall denote by AΓ = (fΓ(x) = 0), will be also said to
be the algebraic set associated to Γ.

Deﬁnition 3.1. Let Γ ⊂ R2 be a semialgebraic set of dimension 0 or 1 and such
that ˆΓ is connected and let fΓ and AΓ be its associated polynomial and algebraic
set respectively. A point a ∈ Γ is said to be:
(1) an algebraic point of Γ if there exists a neighbourhood of a in R2, U , such
that U ∩ Γ = U ∩ AΓ. We denote the set of algebraic points of Γ by Alg(Γ);
(2) a generic non-algebraic point of Γ if a /∈ Alg(Γ) and AΓ is regular at a (i.
e. the gradient of fΓ at a is non-zero). We denote the set of generic non-algebraic
points of Γ by Gen(Γ);
(3) a non-generic non-algebraic point of Γ if a /∈ Alg(Γ) and AΓ is singular
at a (i. e. the gradient of fΓ vanishes at a). We denote the set of non-generic
non-algebraic point of Γ by N G(Γ).

Remark 3.2. The sets of non-algebraic points Gen(Γ) and N G(Γ) are both ﬁnite.

Remark 3.3. Let us assume that N G(Γ) is non-empty, say N G(Γ) = {a1, . . . , ar} for
some positive integer r. For every k ∈ {1, . . . , r}, take a suﬃciently small euclidean
ball Bk = B(ak, ρk) centered at ak with radius ρk > 0 and denote by nk the number
of connected components of (AΓ \ Γ) ∩ Bk (the number nk is the same for every
suﬃciently small ρk > 0). By Newton-Puisseux Theorem, for every k ∈ {1, . . . , r},
there exist sequences of points (aj,k
i )i∈N ⊂ AΓ \ Γ, j ∈ {1, . . . , nk}, such that each
sequence is contained in a diﬀerent connected component of (AΓ \ Γ) ∩ Bk and
aj,k
i → aj when i → ∞.

10 A. BELOTTO AND J. G. ESP´IN

The following objects are used in Section 3.3: the number nΓ = ∑r
k=1 nk; the se-
quence of points in R2nΓ , (αi)i∈N, given by αi = (a1,1
i , . . . , an1,1
i , . . . ,a1,r
i , . . . , anr ,r
i );
and the limit of (αi)i, α0 ∈ R2nΓ .

Remark 3.4. It follows from Remark 3.3 that there exists a sequence of semialge-
braic sets of dimension 0 or 1 (Γi)i∈N such that Γ ⊂ Γi ⊂ AΓ, N G(Γi) = ∅ and
Γi → Γ (in the Hausdorﬀ topology) when i → ∞. Moreover, the polynomials fΓ
and the algebraic set AΓ are also the polynomial and the algebraic set associated
to any of those Γi and Gen(Γi) = Gen(Γ) ∪ {a1,1
i , . . . , an1,1
i , . . . ,a1,r
i , . . . , anr ,r
i }.

Now assume that Γ is compact and connected. There exists a ﬁnite number of
(non-unique) points b1, . . . , bk ∈ Alg(Γ) which are regular points of the algebraic
set AΓ and such that both Γ \ {b1, . . . , bk} and R2 \ (Γ \ {b1, . . . , bk}) are connected.
We can always ﬁx a certain number of these points, which we call transition points,
and denote their set by T r(Γ). We remark that the minimal number k of transition
points corresponds to the number of connected components of R2 \ Γ minus one.
Moreover, with the notation of Remark 3.4, the set T r(Γ) is a valid set of transition
points for Γi, for all i suﬃciently big.

3.2. Construction of generic compact limit periodic sets. Let us ﬁx a con-
nected and compact semialgebraic set Γ ⊂ R2 of dimension 0 or 1 and such that
N G(Γ) = ∅. Let f = fΓ be the polynomial associated to Γ and AΓ its set of zeros
and ﬁx a transition set for Γ, T r(Γ). Fix a coordinate system x = (x1, x2) of R2

and a parameter λ ∈ R. Denote by S the set Gen(Γ) ∪ T r(Γ), which is a ﬁnite set.
We consider the function

h(x, λ) = f (x)
2 − λ ∏

p∈S
 (∥x − p∥2 − λ
2) ,

where ∥·∥ stands for the euclidean norm on R2, and the polynomial family of planar
vector ﬁelds (Xλ)λ∈R where

(3.2) Xλ = ( ∂h
∂x2 + h ∂h
∂x1
 ) ∂x1 + (− ∂h
∂x1 + h ∂h
∂x2
 ) ∂x2.

We devote the rest of the Section to show Γ is a limit periodic set of (Xλ)λ∈R at
λ = 0. The key to achieve it is to understand how the level curves (in respect to
the parameter λ) of h are. We shall start giving a local description of (h(x, λ) = 0)
in a neighbourhood of a point (a, 0) where a ∈ Γ; we treat separately the cases
a ∈ Alg(Γ) \ T r(Γ) (Lemma 3.5) and a ∈ Gen(Γ) ∪ T r(Γ) (Lemma 3.6).
Here and subsequently, given any set A ⊂ R2 × R and any t ∈ R we will denote
A ∩ (λ = t) = {(x, λ) ∈ A : λ = t}; when convenient, we will also understand that
A ∩ (λ = t) is identiﬁed with {x ∈ R2 : (x, t) ∈ A}. In particular, Zt which stands
for the level curve (h(x, λ) = 0) ∩ (λ = t) will repeatedly be seen as a subset of R2.

Lemma 3.5. For every a ∈ Alg(Γ) \ T r(Γ) there exist a number ǫa > 0 and a
compact neighbourhood Va of a such that Zt ∩ Va ⊂ R2 \ Γ for every 0 < t < ǫa.
Moreover, for any connected component W of Va \ Γ and any 0 < t < ǫa, Zt ∩ W is
a non-empty connected regular curve which converges (in the Hausdorﬀ topology)
to Cl(W ) ∩ Γ, when t tends to 0 (see Figure 2).

Proof. Let us start considering a number ǫa > 0, a compact neighbourhood Va ⊂ R2

of a and the coordinate system z = x − a (which is centered at a) such that
h(z, λ) = f (z)
2 − λu(z, λ), where u(z, λ) > 0 at all points in Va × (ǫa, −ǫa).

TOPOLOGICAL CLASSIFICATION OF LIMIT PERIODIC SETS 11

a Γ

Zt
 a Γ

Zt

Figure 2. A regular point (left) and a singular point (right).

By the implicit function theorem, we may assume that there exists an analytic
function λ : Va → R such that h(z, λ(z)) = 0 for every z ∈ Va.
We note that the curves Z a
t = Zt ∩ Va correspond to the t-level curves of λ(z),
that is, Z a
t = (λ(z) = t). By continuity of λ(z), shrinking Va if necessary, this
implies that Z a
t converges (in the Hausdorﬀ topology) to Γ ∩ Va = (λ(z) = 0).
Furthermore, since the level curves of non-constant analytic functions (restricted
to a compact set) are generically regular, we conclude that Z a
t are regular for all
t > 0 suﬃciently small.
Next, since λ(z) ≥ 0 for every z ∈ Va, we conclude that, for every component W
of Va \ Γ, Z a
t ∩ W is non-empty for all small enough t > 0.
Finally, ﬁx a component W of Va \ Γ and suppose by contradiction that there
exists a sequence (tn)n converging to 0 and such that Z a
tn ∩ W is not connected.
Without loss of generality, we may suppose that Cl(W ) is a compact semialgebraic
set. Denote by ΓW the semialgebraic set Cl(W ) ∩ Γ. By the curve selection Lemma
(see for example [12, Lemma 3.1]), there exists an analytic curve φ : [0, 1] → Cl(W )
such that φ(1) = a ∈ ΓW , φ(t) ∈ Cl(W ) \ ΓW for all t ̸= 0 and Cl(W ) \ φ([0, 1])
is not connected. Since all connected components of Z a
t must converge to ΓW , we
conclude that the curve φ([0, 1]) intersects each of the components of Z a
t . This
implies that the function λ ◦ φ is constant and equal to 0 (the value at φ(1)), which
is a contradiction. □

Lemma 3.6. For every a ∈ Gen(Γ) ∪ T r(Γ), there exist a neighbourhood Va of
a, a positive ǫa > 0 and a coordinate system (y, λ) deﬁned on Va × (−ǫa, ǫa) and
centered at (a, 0) such that AΓ ∩ Va = (y1 = 0) and

(3.3) h(y, λ) = u(y, λ) [
y2
1 − λ (
y2
2 − λ
2)]

where u(y, λ) is a unit over Va × (−ǫa, ǫa) (see Figure 3).

Proof. Consider the coordinate system z = x − a (which is centered at a) and note
that in a suﬃciently small neighbourhood of (a, 0) of the form Ua = Va × (−ǫa, ǫa),
we can write h(z, λ) = f (z)
2 − λ [
z2
1 + z2
2 − λ
2] u(z, λ)

where u(z, λ) > 0 at all points in Ua. Apart from shrinking Ua, we can suppose
that ∇f (z) ̸= 0 at all points in Ua. Therefore (apart from a preliminary rotation)
the change of coordinates ̃y1 = u(z, λ)
− 1
2 f (z) = ξz1 + ψ(z, λ) (where ξ ̸= 0 and
ψ(z, λ) has order at least two) and ̃y2 = z2 is an isomorphism on Ua. We get

h(̃y, λ) = u(̃y, λ) (̃y2
1 − λ (̃y2
1 + ̃y2
2v (̃y, λ) − λ
2))

12 A. BELOTTO AND J. G. ESP´IN

a
 Γ
Zt
 aΓ AΓ \ Γ

Zt

Figure 3. A transition point (left) and a generic point (right).

where v(̃y, λ) is an analytic function such that v(0, 0) > 0. Finally, apart from
shrinking Ua, the change of coordinates y1 = ̃y1√
1 + λ and y2 = ̃y2√
v(̃y, λ) is an
isomorphism making
 h(y, λ) = u(y, λ) [
y2
1 − λ (
y2
2 − λ
2)]

and (y1 = 0) = (̃y1 = 0) = (f (z) = 0) ∩ Va as we wanted to prove. □

Proposition 3.7. There exist an open neighbourhood U of Γ × {0} and a number
ǫ > 0 such that, for every 0 < t < ǫ, Zt ∩ U contains a compact and regular
connected component γt such that γt → Γ (in the Hausdorﬀ topology) when t → 0.

Proof. For every a ∈ Γ take a neighbourhood Va of a and a number ǫa > 0 as in
Lemma 3.5 or 3.6. The compacity of Γ allows us to take a relatively compact open
neighbourhood U of Γ × {0}, of the form U = V × (−δ, δ) with V ⊂ R2 and δ > 0,
such that U ⊂ ⋃
a∈Γ Ua.
Note that, from the two previous lemmas, we can assume that Zt ∩ U is regular
for every suﬃciently small t > 0. Also, the continuity of h guarantees that Zt ∩ U
converges to AΓ ∩ V when t tends to 0 (in the Hausdorﬀ topology).
Let us ﬁx a point b ∈ Alg(Γ) \ T r(Γ) and W a component of Vb \ Γ. For every
suﬃciently small t > 0, let us call γt the connected component of Zt which meets W
(see Lemma 3.5). Let γ0 ⊂ AΓ denote the limit of γt when t → 0 (which contains
b ∈ Γ). We are then left with the task of proving that γ0 = Γ.
We start showing that γ0 ⊂ Γ. We proceed by contradiction assuming the
existence of a point c ∈ γ0 \Γ. After shrinking V and Va for a ∈ Gen(Γ) if necessary,
we may suppose that the points b and c lies in diﬀerent connected components of
the set R = V \ ⋃

a∈Gen(Γ) Va. In particular, γt ∩ R is disconnected and these
disconnected components can only join each other by passing through one of the
open sets Ua with a ∈ Gen(Γ). This leads to contradiction with Lemma 3.6.
Since γt is a connected regular curve, R2 \ γt must consists in exactly two con-
nected components, say C1
t and C2
t . Now, for every ǫ0 > 0, consider the set
γǫ0 = γ0 \ ∪a∈T r(Γ)B(a, ǫ0). We claim that, for every small enough t > 0,

(3.4) γǫ0 ⊂ R2 \ γt.

Indeed, let us suppose that γǫ0 meets both C1
t and C2
t for all small t > 0. Since γt
can only cross points of Γ near a ∈ T r(Γ) ∪ Gen(Γ), we conclude that there exists
a point a ∈ T r(Γ) such that γt crosses Γ ∩ Va in such a way that γǫ0 ∩ C1
t ∩ Va and

TOPOLOGICAL CLASSIFICATION OF LIMIT PERIODIC SETS 13

γǫ0 ∩ C2
t ∩ Va Γ are both non-empty. But this gives us again a contradiction with
Lemma 3.6.
Finally, let us denote by Wi, i = 1, . . . k, the connected components of R2 \ Γ and
set I as the subset of indexes i ∈ {1, . . . , k} such that Wi ∩ γt ̸= ∅ for all suﬃciently
small t > 0 (note that, by construction, I is non-empty). The proof is completed by
showing that I = {1, . . . , k} and γ0 = ∪i∈I (Cl(Wi) \ Wi). We argue in two steps.
First, suppose by contradiction that γ0 ̸= ∪i∈I (Cl(Wi) \ Wi). Without restric-
tion of generality, we can suppose that 1 ∈ I and γ0 ∩ (Cl(W1) \ W1) ̸= Cl(W1) \ W1.
We consider a point c ∈ Cl(W1) \ W1 which does not belong to γ0 and an analogous
family of ovals αt ⊂ Zt constructed in the same way as γt but in respect to c and the
connected set W1. By (3.4), we conclude that α0 ∩ γ0 can only contain points which
lie in T r(Γ). This implies that Γ \ T r(Γ) has at least two disconnected components
γ0 \ T r(Γ) and α0 \ T r(Γ), which is in contradiction with the deﬁnition of T r(Γ).
Next, suppose, by contradiction, that γ0 = ∪i∈I (Cl(Wi) \ Wi) but I ̸= {1, . . . , k}.
Denote by Γ0 = ∪i /∈I (Cl(Wi) \ Wi). Since the level curve Zt can only cross points
of Γ near a ∈ T r(Γ) ∪ Gen(Γ) (see Lemmas 3.5 and 3.6), we conclude that γ0 ∩
Γ0 ∩ T r(Γ) = ∅. Therefore, γ0 ∩ Γ0 ⊂ Γ \ T r(Γ) disconnects R2, which is again in
contradiction with the choice of T r(Γ).
We conclude the proof by remarking that, since γt converges to Γ, for small
enough t > 0, γt must be a compact set contained in the interior of U . □

After noticing that any compact and regular connected component of a planar
algebraic set is a topological circle [11, Theorem 2, p. 180], it follows from Proposi-
tion 3.7 that the polynomial family of planar vector ﬁelds given by (3.2) has Γ as a
limit periodic set at λ = 0. Indeed, it is enough to prove that, for every suﬃciently
small t > 0, the topological circle γt ⊂ R2 given by Proposition 3.7 is a limit cycle
of Xt. To show this, it suﬃces to note that

Xλ(h) = ( ∂h
∂x2 + h ∂h
∂x1
 ) ∂h
∂x1 + (
− ∂h
∂x1 + h ∂h
∂x2
 ) ∂h
∂x2 = h ∥∇h∥2

and, as a consequence, Zt is an invariant set containing any periodic orbit of Xt.
Finally, the fact that γt is regular guarantees that it is a periodic orbit. This proves
the converse of Theorem 1.3 (under the extra assumption that Γ is compact and
generic).

3.3. Construction of non-generic compact limit periodic sets. Let us now
ﬁx a connected and compact semialgebraic set Γ ⊂ R2 of dimension 0 or 1 and
N G(Γ) ̸= ∅. Denote by f = fΓ the polynomial associated to Γ, AΓ the associated
algebraic set and S = Gen(Γ) ∪ T r(Γ). Fix a coordinate system x = (x1, x2) of R2

and parameters (α, λ) ∈ R2nΓ+1 where α = (α
1, . . . , α
n) ∈ R2nΓ . We consider the
function
 h(x, α, λ) = f (x)
2 − λ ∏

p∈S
 (
∥x − p∥2 − λ
2) n∏

i=1
 (
∥x − α
i∥2 − λ
2) .

Let us take the number nΓ, the sequence (αi)i∈N and the point α0 as in Re-
mark 3.3 and, for every i ∈ N, let us consider hi(x, λ) = h(x, αi, λ). For any
i ∈ N, we can apply Proposition 3.7 to the semialgebraic set Γi introduced in
Remark 3.4 to deduce that there exists a value 0 < λi < 1
i such that the level
set (hi(x, λ) = 0) ∩ (λ = λi) contains a subset γi which is regular connected,
compact and 1
i -close (in respect to the Hausdorﬀ topology) to Γi. Furthermore,

14 A. BELOTTO AND J. G. ESP´IN

apart from shrinking λi if necessary, we can suppose that γi ∩ N G(Γ) = ∅, because
N G(Γ) ⊂ Alg(Γi) and Lemma 3.5. In particular, note that γi → Γ when i → ∞
since Γi converges to Γ.

Remark 3.8. We note that, for every point a ∈ Γ, there exists N > 0 such that
γi ∩ {a} = ∅ for every i > N . Indeed, by construction γi only crosses Γi ⊃ Γ
near the points T r(Γ) ∪ Gen(Γi). So, assuming by contradiction that there exists
a point a ∈ Γ so that γi ∩ {a} ̸= ∅ for an inﬁnite number of i, we conclude that
a ∈ T r(Γ) ∪ Gen(Γ) ∪ N G(Γ). Next, by Lemma 3.6 we conclude that a ∈ N G(Γ),
which contradicts the choice of λi.

It follows from the above considerations (just as in the previous Section) that
the algebraic family of vector ﬁelds

Xα,λ = ( ∂h
∂x2 + h ∂h
∂x1
 ) ∂x1 + (− ∂h
∂x1 h + h ∂h
∂x2
 ) ∂x2

has Γ as a limit periodic set at (α, λ) = (α0, 0).

3.4. Construction of unbounded limit periodic sets. Finally, let Γ ⊂ R2 be a
closed and unbounded semialgebraic set of dimension 0 or 1 whose compactiﬁcation
ˆΓ is connected. Apart from considering a translation of R2, we can assume that
(0, 0) /∈ Γ.
Let us consider the transition map of the Bendixson compactiﬁcation φ : R2 \
{0} → R2 given by φ(x1, x2) = (x1/r, −x2/r) where r = x
2
1 + x
2
2 (see Section 2.1).
Note that φ(Γ) is a semialgebraic set (by e. g. [3, Corollary 1.8]), whose closure
Z = φ(Γ) ∪ {0} is a compact and connected semialgebraic set of dimension 0 or
1. By the previous Sections, there exist a polynomial family of planar vector ﬁelds
(Yλ)λ∈Λ and a parameter λ0 such that Z is a limit periodic set for the family (Yλ)λ
at λ0. We denote by (zλn )n the sequence of limit cycles of Yλ which converge to Z.
Let us now consider the map Φ : (R2 \ {0}) × Λ → R2 × Λ given by Φ(x1, x2, λ) =
(φ(x1, x2), λ). The pull-back Φ∗(Yλ) is rational and there exists an integer d ≥ 0
such that Xλ = (x
2
1 + x
2
2)
dΦ∗(Yλ) is a polynomial family of vector ﬁelds. According
to Remark 3.8, for every suﬃciently big n, zλn does not intersect the origin so
Φ−1(zλn ) is itself a limit cycles of Xλn . It follows from the construction that Γ is
a limit periodic set of (Xλ)λ at λ0.

References

[1] V. W. Adkisson and S. MacLane, Extending maps of plane Peano continua, Duke Math. J.
6 (1940), 216–228.
[2] A. Belotto. Analytic varieties as limit periodic sets. Qual. Theory Dyn. Syst. 11 (2012), no.
2, 449–465.
[3] E. Bierstone and P. Milman. Semianalytic and subanalytic sets. Inst. Hautes ´Etudes Sci.
Publ. Math. (1988), no. 67, 5–42.
[4] E. Bierstone and P. Milman, Functoriality in resolution of singularities, Publ. R.I.M.S.
Kyoto Univ., 44, (2008), 609–639.
[5] F. Dumortier, J. Llibre and J. C. Art´es. Qualitative theory of planar diﬀerential systems.
Springer-Verlag, Berlin, 2006.
[6] F. Dumortier, R. Roussarie and C. Rousseau. Hilbert’s 16th problem for quadratic vector
ﬁelds. J. Diﬀerential Equations 110, (1994), no. 1, 86-133.
[7] Y. Il’yashenko and S. Yakovenko Concerning the Hilbert sixteenth problem, in “Concerning
the Hilbert 16th Problem”, 1–19. Amer. Math. Soc. Transl. Ser. 2, 165. Amer. Math. Soc.,
Providence, RI, 1995.

TOPOLOGICAL CLASSIFICATION OF LIMIT PERIODIC SETS 15

[8] J. P. Fran¸coise and C. Pugh, Keeping track of limit cycles, J. Diﬀerential Equations 65
(1986), no.2, 139–157.
[9] V. Jim´enez L´opez and J. Llibre. A topological characterization of the ω-limit sets for analytic
ﬂows on the plane, the sphere and the projective plane, the sphere and the projective plane.
Advances in Mathematics 216 (2007), no.2, 677–710.
[10] V. Jim´enez L´opez and D. Peralta-Salas. Global attractors of analytic plane ﬂows. Ergodic
Theory Dyn. Syst. 29 (2009), no.2, 967–981.
[11] K. Kuratowski, Topology. Vol. II, Academic Press, New York, 1968.
[12] J. Milnor. Singular points of complex hypersurfaces. Ann. of Math. Stud., vol. 61. Princeton
University Press, New Jersey, 1968.
[13] J. Llibre and G. Rodr´ıguez, Conﬁgurations of limit cycles and planar polynomial vector
ﬁelds. J. Diﬀerential Equations 198, (2004), no. 2, 374–380.
[14] D. Panazzolo and R. Roussarie. A Poincar´e-Bendixson theorem for analytic families of vector
ﬁelds. Bol. Soc. Brasil. Mat. (N.S.) 26 (1995), no. 1, 85–116.
[15] R. Roussarie. Bifurcations of Planar Vector Fields and Hilbert’s Sixteenth Problem. Progress
in Mathematics, vol. 164 Birkh¨auser Verlag, Basel, 1998.
[16] R. Roussarie. Cyclicit´e ﬁnie des lacets et des points cuspidaux. Nonlinearity 2 (1989), no.
1, 73–117.

AB: Universit´e Paul Sabatier, Institut de Math´ematiques de Toulouse, 118 route de
Narbonne, F-31062 Toulouse Cedex 9, France
E-mail address, A. Belotto: andre.belotto da silva@math.univ-toulouse.fr

JE: Universidad de Murcia, Departamento de Matem´aticas, Campus de Espinardo,
30100 Murcia, Spain
E-mail address, J. G. Esp´ın: josegines.espin@um.es
