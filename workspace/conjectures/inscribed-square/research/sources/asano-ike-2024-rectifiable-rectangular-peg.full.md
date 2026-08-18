<!-- source: https://arxiv.org/pdf/2412.21057 | converted from PDF -->

The rectifiable rectangular peg problem

Tomohiro Asano Yuichi Ike

January 6, 2026

Abstract

We give an affirmative answer to the rectangular peg problem for a large class of
continuous Jordan curves that contains all rectifiable curves and Stromquist’s locally
monotone curves. Our proof is based on microlocal sheaf theory and inspired by recent
work of Greene and Lobb.

Contents

1 Introduction 1
1.1 Our results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.2 Related work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3

2 Preliminaries 4
2.1 Twisted sheaves . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
2.2 Twisted Tamarkin category . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2.3 Hamiltonian action . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8

3 Sheaf quantization associated with Jordan curves 9
3.1 Sheaves associated with the torus . . . . . . . . . . . . . . . . . . . . . . . . 9
3.2 Action of Rθ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
3.3 Computation for the standard circle . . . . . . . . . . . . . . . . . . . . . . 13

4 Sheaf-theoretic condition for rectangular peg 14

5 Jordan curves 19
5.1 Proof of the main theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
5.2 Rectifiable curves . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
5.3 Locally monotone curves . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26

1 Introduction

The square peg problem first posed by Toeplitz [Toe11] in 1911 asks the following:

Does every continuous Jordan curve inscribe a square?

In this paper, we consider the so-called rectangular peg problem, which asks whether a
Jordan curve inscribe a rectangle with prescribed aspect ratio. For θ ∈ (0, π), a θ-rectangle
is a rectangle such that the angle between the diagonals is θ. Note that a θ-rectangle is a
(π − θ)-rectangle.
 1arXiv:2412.21057v3  [math.SG]  5 Jan 2026
Recent progress have been made by Greene and Lobb in [GL21] where they answer
positively to the question for smooth Jordan curves: every smooth Jordan curve inscribes
a θ-rectangle for any θ ∈ (0, π). More recently, in [GL24a], they give a positive answer for
rectangles and for every rectifiable (i.e., with finite length) Jordan curve satisfying some
hypothesis on the diameter and the area of the bounded domain. In this paper we remove
this later hypothesis. To the best of our knowledge, this is the first result that gives an
affirmative answer to the square peg problem (i.e., θ = π/2) for all the rectifiable Jordan
curves.

1.1 Our results

Throughout this paper for a Jordan curve c : S1 → R2, we write C = c(S1) for its image
in R2. Our main theorem is the following.

Theorem 1.1. Let c : S1 → R2 be a Jordan curve. Moreover, assume that there exists a
sequence of smooth Jordan curves (cn : S1 → R2)n such that

(1) (cn)n converges to c in the C0-sense;

(2) setting fn to be the primitive of (cn ◦ e)∗λ, the sequence (fn)n converges to a continu-
ous function f on R uniformly on every compact subset, where e : R → R/2πZ ≃ S1

is the quotient map.

Then c inscribes a θ-rectangle for any θ ∈ (0, π).

A Jordan curve satisfying the conditions in Theorem 1.1 might be said to admit a
continuous Legendrian lift.
One can show that every rectifiable Jordan curve satisfies the conditions in Theo-
rem 1.1. See Section 5. As a result, we get:

Corollary 1.2 (Corollary 5.9). Every rectifiable Jordan curve inscribes a θ-rectangle for
any θ ∈ (0, π).

There is another large class called locally monotone (see Definition 5.10 for the defi-
nition). We prove a locally monotone curve also satisfies the conditions in Theorem 1.1,
which implies the following:

Corollary 1.3 (Corollary 5.12). Every locally monotone curve inscribes a θ-rectangle for
any θ ∈ (0, π).

We briefly explain our strategy for the proof of the theorem. Given a Jordan curve C,
by scaling, we may assume that the area of the open domain bounded by C is π.
The first ingredient is the trick to interpret inscribed θ-rectangles into Lagrangian
intersection, which has already appeared in [GL23; GL24a; Gao24]. We identify R2 with
C, which we regard as a symplectic manifold. Note that if C is smooth, it is a Lagrangian
submanifold of C, thus C × C is also a Lagrangian submanifold of C × C. For θ ∈ [0, π],
define a Hamiltonian diffeomorphism Rθ : C2 → C2 by

Rθ = ( 1 1
−1 1
)−1 (1 0
0 e−√−1θ
) ( 1 1
−1 1
) . (1.1)

One can easily find that a θ-rectangle corresponds to four distinct points z, w, z′, w′ such
that Rθ(z′, w′) = (z, w). Since Rθ(z, z) = (z, z), Rθ is the identity on the diagonal ∆C
of C × C, which corresponds to degenerate rectangles. Thus, the problem of finding a

2

θ-rectangle inscribed in C is reduced to finding a intersection point between C × C and
Rθ(C × C) outside the diagonal ∆C of C × C.
The second ingredient is the following method coming from microlocal sheaf theory,
in particular, sheaf quantization. For a smooth Jordan curve C, it is known that one can
construct a canonical object FC in the Tamarkin category whose microsupport is C × C,
called the sheaf quantization of C ×C. See Sections 2 and 3 for more precise definitions. By
the completeness of the Tamarkin category with respect to the interleaving distance [AI24;
GV24], for a continuous Jordan curve C, we can still construct its sheaf quantization
FC. Moreover, by a result in Guillermou–Kashiwara–Schapira [GKS12], the action Rθ
lifts to the Tamarkin category category. The Hom space Hom(FC, RθFC) captures the
information of the intersection (C × C) ∩ Rθ(C × C) and is equipped with a filtration,
which can be regarded as a persistence module with structure maps (τa,a′)a≤a′. We focus
on a “critical value” a0 ∈ R such that τa,a′ is not an isomorphism if a < a0 < a′. By the
conditions in Theorem 1.1, the diagonal ∆C contributes only to critical values in πZ. We
will show that there exists a critical value that is not in πZ, which proves the theorem.
In fact, we give a sheaf-theoretic condition for the existence of a θ-rectangle in Section 4.
The conditions in Theorem 1.1 implies that sheaf-theoretic condition.
With the sheaf-theoretical approach, we can directly deal with a continuous Jordan
curve, in contrast to Floer-theoretic methods, which require taking a sequence of smooth
objects. Moreover, the important step in our proof is to analyze µhom(FC, RθFC), which
is expected to correspond to local Floer cohomology. The computation method of µhom
would be easier than that of local Floer cohomology. Furthermore, µhom does not com-
mute with limits nor colimits, which suggests that µhom(FC, RθFC) for a continuous
Jordan curve C cannot be described in terms of a limit/colimit. Thus, the sheaf-theoretic
approach would be more powerful than Floer-theoretic methods at the moment.
This paper is organized as follows. In Section 2, we define a twisted version of the
Tamarkin category. In Section 3, we construct a sheaf quantization of the standard torus
and observe some basic properties. In Section 4, we give a sheaf-theoretic condition for the
existence of a θ-rectangle. In Section 5, we prove Theorem 1.1 and show Corollaries 1.2
and 1.3.

1.2 Related work

We review some history on the square and rectangular peg problem. See Matschke [Mat14]
for a detailed and overall history on these topics.
Vaughan (published in [Mey81]) showed that every continuous Jordan curve inscribes
a rectangle with a simple topological argument, in which a rectangle on the Jordan curve is
interpreted to a immersed point of a surface in a 3-dimensional space. Hugelmeyer [Hug18]
proved that for any n ∈ Z≥3, every smooth Jordan curve has an inscribed rectangle of
ratio πk/n for some k ∈ {1, . . . , n − 1}. Moreover, he [Hug21] proved that for any smooth
Jordan curve, the set of values θ ∈ [0, π/2] for which the curve inscribe a rectangle of aspect
angle θ has Lebesgue measure at least π/6. In his works, the existence of rectangular pegs
is reduced to the existence of intersections of surfaces within a four-dimensional space.
Greene and Lobb [GL21] solved the rectangular peg problem for smooth Jordan curves
using symplectic geometry. Moreover, they proved cyclic quadrilateral pegs for smooth
curves in [GL23]. In [GL24a], Greene and Lobb used a version of Lagrangian intersection
Floer theory and spectral invariants to prove assertions for rectifiable curves with an
additional condition. Our result is on the line of these.
Our results are also a generalization of the following. Emch [Emc16] proved the ex-
istence of an inscribed square for piecewise analytic curves satisfying some additional

3

assumptions. Schnirelman [Sch44] proved it for a class of curves that contains C2, and
Stromquist [Str89] proved for locally monotone curves. Tao [Tao17] proved the existence of
an inscribed square for a curve that is the union of the graphs of two Lipschitz continuous
functions with Lipschitz constant less than 1. Greene–Lobb [GL24c] strengthened Tao’s
result to the case where the Lipschitz constant is less than 1 + √2. Feller–Golla [FG23]
has weakened the regularity condition of the result by Hugelmeyer [Hug18].
There are also some recent results [Gao24; Hug24; GL24b] for related problems with
the use of Lagrangian intersection Floer theory.

2 Preliminaries

Throughout this paper, we set the base field k to be F2 = Z/2Z. Let X be a manifold. Let
π : T ∗X → X denote the cotangent bundle and (x; ξ) denote the homogeneous symplectic
local coordinate on T ∗X. We denote by λX = ∑i ξidxi the Liouville 1-form on T ∗X. We
often simply write λ for λX .

Notation 2.1. For objects F, G in a k-linear stable (∞-)category, Hom(F, G) (resp.
End(F )) denotes the Hom (resp. End) object in Mod(k), the presentable stable cate-
gory of k-vector spaces. For v ∈ H n(Hom(F, G)) (resp. v ∈ H n(End(F ))) for some n ∈ Z,
we simply write v ∈ Hom(F, G)[n] (resp. v ∈ End(F )[n]).

2.1 Twisted sheaves

Let Sh(X) be the k-linear presentable stable category of sheaves of k-vector spaces on X.
For each object F ∈ Sh(X), we write SS(F ) for the conic microsupport 1 of F , which is
a closed conic subset of T ∗X. For a closed subset A of T ∗X, we denote by ShA(X) the
subcategory of Sh(X) consisting of objects with conic microsupport contained in A.
In this paper, we use the notion of twisted sheaves. We give a short review for twisted
sheaves from [Kas89]. Guillermou [Gui12; Gui23] and Jin [Jin20] used twisted sheaves in
the process of constructing sheaf quantizations of compact exact Lagrangian submanifolds
in cotangent bundles, and we use them in a parallel manner in this work. The formulation
within the context of ∞-categories has been done in [CKNS24], and we follow their ap-
proach. See [CKNS24] for the precise definition and treatment of twisted sheaves. Here,
we only treat very restrictive twistings and one can describe twisted sheaves via untwisted
sheaves. See Remark 2.6 below.
Let Pic(k) be the (∞-)group consisting of the invertible objects in Mod(k). In our
setting k = Z/2Z, Pic(k) is isomorphic to Z (the element k[n] ∈ Pic(k) corresponds to
n ∈ Z). Let η : X → B Pic(k) be a twisting. We denote Sh
η(X) the category of sheaves
on X twisted by η. A homotopy between two twistings η1 and η2 gives an identification
Sh
η1(X) ≃ Sh
η2(X). In particular, a null homotopy (to the basepoint) of a twisting η
gives an identification Sh
η(X) ≃ Sh(X). Let X, Y be manifolds and ηX : X → B Pic(k)
(resp. ηY : Y → B Pic(k)) be a twisting. For a morphism of manifolds f : X → Y , if
f ∗ηY := ηY ◦ f = ηX , one can define functors2

f∗, f! : Sh
ηX (X) → Sh
ηY (Y ), f ∗, f ! : Sh
ηY (Y ) → Sh
ηX (X)

1In the literature, this is usually called the microsupport, but we use this name for the non-conic
microsupport defined below.
2In this paper, we use the symbol f ∗ instead of f −1.

4

satisfying the adjunction properties f ∗ ⊣ f∗ and f! ⊣ f !. Moreover, for two twisting
η, η′ : X → B Pic(k), we can define functors

⊗ : Sh
η(X) × Sh
η′(X) → Sh
η·η′(X),

Hom : Sh
η(X)op × Sh
η′(X) → Sh
η−1·η′(X).

For an object F ∈ Sh
η(X), we can define its conic microsupport SS(F ) in a similar way
to the untwisted case. We define Shη
A(X) in a similar way to the untwisted case.
We recall some facts about the microlocalization (see [KS90, Chap. IV]), in the twisted
case. Let η1, η2 : X → B Pic(k) be two twistings and let F ∈ Sh
η1(X) and G ∈ Sh
η2(X).
One can define a twisted sheaf µhom(F, G) ∈ Sh
η−1
1 ·η2(T ∗X) on T ∗X in a similar way to
[KS90, Section 4.4], where η−1
1 · η2 : T ∗X → B Pic(k) is the composite of the projection
T ∗X → X and the twisting η−1
1 · η2 : X → B Pic(k). Indeed, since the original µhom
is defined via 6-functors, we can apply the same construction by tracing the twisting.
The support of µhom(F, G) is contained in SS(F ) ∩ SS(G). We have a natural isomor-
phism Hom(F, G) ∼
−→ π∗µhom(F, G), and also Hom(F, G) ≃ i∗µhom(F, G), where i is the
inclusion of the zero-section.
Now we assume that Λ = SS(F ) \ 0X is a (conic) connected Lagrangian submanifold
of T ∗X \ 0X . For a function f : X → R of class C2 such that Γdf intersect Λ transversally
at (x0; ξ0), the space m(F, f, x0) = (Γ{f ≥f (x0)}(F ))x0 is called the microstalk at (x0; ξ0).
It is proved that m(F, f, x0) is independent of f and (x0; ξ0) up to shift (see [KS90]
Prop. 7.5.3 and Cor. 7.5.7). We say that F is simple or of microlocal rank 1 along Λ if
m(F, f, x0) ≃ k[d] for some d ∈ Z.
Let F, G ∈ Sh
η(X) be simple sheaves and assume that SS(F ) and SS(G) intersect
cleanly outside the zero-section. Then, for a connected component Λ0 of (SS(F )∩SS(G))\
0X , we have an isomorphism µhom(F, G)|Λ0 ≃ kΛ0[d] for some d ∈ Z.

2.2 Twisted Tamarkin category

In this subsection, we introduce a twisted version of the Tamarkin category. We fol-
low [KSZ23] for the ∞-categorical treatment of the Tamarkin category. We replace the
Tamarkin direction Rt with Rt/πZ, where π is the area of the domain bounded by the
standard unit circle C0 in R2 with radius 1.
Let N be a manifold. We fix a twisting η : Rt/πZ → B Pic(k). Since we work on
k = F2, we may assume that η is the delooping of Z → Pic(k); 1 ↦→ k[n] for some
n ∈ Z. By abuse of notation, we also write η for the composite of η and the projection
N × Rt/πZ → Rt/πZ.
We consider the category Shη(N × Rt/πZ) consisting of sheaves on N × Rt/πZ twisted
by η. We define the twisted version of the Tamarkin category by

T η(T ∗N ) := Sh
η(N × Rt/πZ)/{F | SS(F ) ⊂ {τ ≤ 0}}.

The quotient functor Shη(N × Rt/πZ) → T η(T ∗N ) admits a left adjoint and a right
adjoint. Both of these functors are fully faithful. We sometimes regard T η(T ∗N ) as a full
subcategory of Shη(N × Rt/πZ) via either of these functors. For an object F ∈ T η(T ∗M ),
we define SS
•(F ) := SS(F ) ∩ {τ = 1}.

For a closed subset A ⊂ T ∗N × Rt/πZ, we set

T η
A (T ∗N ) := {F ∈ T η(T ∗N ) | SS
•(F ) ⊂ A}.

5

We set T ∗
τ >0(N × Rt/πZ) := {τ > 0} ⊂ T ∗(N × Rt/πZ) and define a map ρ : T ∗
τ >0(N ×
Rt/πZ) → T ∗N by (x, t; ξ, τ ) ↦→ (x; ξ/τ ). For an object F ∈ T η(T ∗N ), we set

MS(F ) := ρ(SS(F ) ∩ {τ > 0}) ⊂ T ∗N

and call it the (non-conic or reduced) microsupport of F .
Let qi : N × R/πZ × R/πZ → N × Rt/πZ; (x, t1, t2) ↦→ (x, ti) denote the projection and
m : N × R/πZ × R/πZ → N × Rt/πZ; (x, t1, t2) ↦→ (x, t1 + t2) denote the addition map.
For F, G ∈ T η(T ∗N ), we define

F ⋆ G := m!(q∗
1F ⊗ q∗
2G) ∈ T η(T ∗N ),

Hom⋆(F, G) := q1∗ Hom(q∗
2F, m!G) ∈ T η(T ∗N ).

Then ⋆ induces the monoidal operation of T η(T ∗N ), and Hom⋆ defines the internal hom
of T η(T ∗N ).
For a ∈ R, let Ta be the map N × Rt/πZ → N × Rt/πZ : (x, t) ↦→ (x, t + [a]), where
[a] is the image of the quotient map ℓ : Rt → Rt/πZ. By definition, Ta∗ is a functor from
Sh
T ∗
a η(N ×Rt/πZ) to Sh
η(N ×Rt/πZ). We identify ShT ∗
a η(N ×Rt/πZ) with Sh
η(N ×Rt/πZ)
by the homotopy (η ◦ Tsa)s∈[0,1]. We obtain an automorphism on Sh
η(N × Rt/πZ) and it
induces an automorphism on T η(T ∗N ). We write the functor as Ta. Note that T0 = id
and Tπ is the shift functor [−n].
The functor Ta is naturally isomorphic to the functor ℓ!kN ×[a,∞) ⋆ (-). For a ≤ a′ ∈ R,
a natural transformation τa,a′ : Ta ⇒ Ta′ is induced by the natural morphism kN ×[a,∞) →
kN ×[a′,∞). This enable us to define a pseudo-distance d on the set of the objects of
T η(T ∗N ) as in [AI20; AI23; AI24]. Namely, for F, G ∈ T η(T ∗N ), define

d(F, G) := inf
 {

a + b
 ∣
∣
∣
∣
∣ ∃α : F → TaG, ∃β : G → TbF such that

Taβ ◦ α ≃ τ0,a+b(F ), Tbα ◦ β ≃ τ0,a+b(G)

}
 .

Such a pair of morphisms (α, β) is called (a, b)-interleaving for (F, G) and the pseudo-
distance d is called the interleaving distance. This pseudo-distance is in fact complete.

Proposition 2.2 ([AI24, Cor. 4.5] and [GV24, Prop. 6.22]). The interleaving distance d is
a complete pseudo-distance, i.e., any Cauchy sequence with respect to d has a limit object
in T η(T ∗N ).

The conic microsupport of a limit object can be estimated as follows.

Proposition 2.3 ([GV24, Prop. 6.26]). Let (Fn)n be a sequence in T η(T ∗N ) and assume
that it converges to F∞ with respect to the interleaving distance d. Then

SS
•(F∞) ⊂ ⋂

k∈N
 ⋃

n≥k SS
•(Fn).

The interleaving distance d is degenerate in general, but it is proved that d is non-
degenerate on the category of metric-limit objects of constructible sheaves. For a real
analytic manifold N , an object F ∈ T η(T ∗N ) is said to be limit constructible if it is a
metric limit of constructible sheaves with respect to the interleaving distance d. A limit
object of a sequence of limit constructible sheaves is unique up to isomorphism due to the
following proposition.

Proposition 2.4 ([GV24, Prop. B.8]). If F, G ∈ T η(T ∗N ) are limit constructible and
d(F, G) = 0, then F ≃ G.
 6

We have the following isomorphism:

Hom(F, TaG) ≃ Γ[−a,∞)(R; ℓ!q∗ Hom⋆(F, G)), (2.1)

where q : N ×Rt/πZ → Rt/πZ is the projection. We denote by T (T ∗N ) the usual Tamarkin
category of T ∗N defined as

T (T ∗N ) := Sh(N × Rt)/{F | SS(F ) ⊂ {τ ≤ 0}}.

Then the functor ℓ! : T η(T ∗N ) → T (T ∗N ) is conservative and the functor ℓ! : T (T ∗N ) →
T η(T ∗N ) is symmetric monoidal. One can equip a complete pseudo-distance d with
T (T ∗N ) in a similar way to T η(T ∗N ), and obtain a conic microsupport estimate similar
to Proposition 2.3. One can also define limit constructible objects in T (T ∗N ) similarly.
A constructible object in T (pt) is isomorphic to ⊕α∈A kIα[dα] for a locally finite
family of intervals (Iα)α∈A and a family of integers (dα)α∈A ([KS18, Thm. 1.17] and
[Gui23, Cor. IV.4.3]). For a limit constructible object in T (pt), we have the following
decomposition by interval modules.

Proposition 2.5 ([GV24, Cor. B.12]). Let F ∈ T (pt) and assume that F is limit con-
structible. Then there exists a countable family of intervals (Iα)α∈A and a family of integers
(dα)α∈A such that F ≃ ⊕

α∈A kIα[dα].

Moreover, for any ε > 0, the family (Iα | α ∈ A, |Iα| ≥ ε) is locally finite.

When N = pt, we simply write T η := T η(pt). Similar to [KSZ23, Prop. 5.5] combined
with [CKNS24, Lem. 2.9], one can check

T η(T ∗N ) ≃ Sh(N ) ⊗ T η ≃ Sh(N ; T η),

where the last category stands for the category of sheaves on N with coefficient in T η.
Through this identification, the operations ⋆ and Hom⋆ in the category T η(T ∗N ) are usual
⊗ and Hom with coefficient in T η. See [Vol25] for 6-functor formalism for locally compact
Hausdorff spaces and more general coefficients.
For K12 ∈ T η(T ∗(N1 × N2)), K23 ∈ T η(T ∗(N2 × N3)), we can also define the operation

⃝⋆ by K12 ⃝⋆ K23 := m13!(q∗
12K12 ⊗ q∗
23K23),

where qij : N1 × N2 × N3 × R/πZ × R/πZ → Ni × Nj × Rt/πZ is the projection, and

m13 : N1 × N2 × N3 × R/πZ × R/πZ → N1 × N3 × R/πZ;

(x1, x2, x3, t1, t2) ↦→ (x1, x3, t1 + t2).

Through the identification with sheaf category with coefficient in T η, the operation ⃝⋆
corresponds to the usual convolution.
For K12 ∈ T (T ∗(N1 × N2)), K23 ∈ T η(T ∗(N2 × N3)), we can also define the operation

⃝⋆ by a similar method. This K12 ⃝⋆ K23 is isomorphic to ℓ!K12 ⃝⋆ K23 defined above.

Remark 2.6. The category T η(T ∗N ) can be identified with a full subcategory of Sh
η(N ×
Rt/πZ). We can describe objects of Sh
η(N × Rt/πZ) via untwisted sheaves. Take real
numbers t0 < t1 < t2 < t3 satisfying t2 − t0 < π, t3 − t1 < π, and t3 − t0 > π. Set
U0 = ℓ((t0, t2)), U0 = ℓ((t1, t3)), V0 = ℓ((t0, t1)), and V1 = ℓ((t2, t3)). By the sheaf
property of Shη(-) on M × Rt/πZ, an object Sh
η(N × Rt/πZ) is equivalent to the datum

7

(F0, F1, α1, α0) where Fi is an object of Sh(N × Ui) for each i = 0, 1, and α1 : F0|N ×V1 ≃
F1|N ×V1, α0 : F0[n]|N ×V0 ≃ F1|N ×V0 are isomorphisms.
Gluing F0 and F1 by α1 firstly, we can see that above datum is also equivalent to
(F, α0) where F is an object of Sh(N × (t0, t3)) and α0 : F [n]|N ×(t0,t3−π) ≃ F |N ×(t0+π,t3) is
an isomorphism via the identification N × (t0, t3 − π) ≃ N × (t0 + π, t3) : (x, t) ↦→ (x, t + π).

For F, G ∈ T η(T ∗N ), the object µhom(F, G)|{τ >0} ∈ Sh({τ > 0}) is invariant under
isomorphisms in T η(T ∗M ). Not only µhom|{τ >0} : T η(T ∗N )op ×T η(T ∗N ) → Sh({τ > 0})
is a functor, but also µhom makes T η(T ∗N ) into a Sh({τ > 0})-enriched category. This
follows from the fact that µhom is the Hom sheaf of a stack called Kashiwara–Schapira
stack [KS90; Gui23]. See also [KL22, Remark 2.13] for an ∞-categorical treatment. In
what follows, we denote µhom(F, G)|{τ >0} simply by µhom(F, G) for F, G ∈ T η(T ∗N ).
We have the following (co)fiber sequence associated with the Hom spaces and µhom.

Lemma 2.7. For F, G ∈ T η(T ∗N ) such that MS(F ) and MS(G) are compact, we have a
fiber sequence

colim
ε→0 Hom(F, T−εG) → Hom(F, G) → Γ({τ > 0}; µhom(F, G)).

Proof. Let H := ℓ!q∗ Hom⋆(F, G). By a similar argument to [Ike19], we have an isomor-
phism Γ[0,∞)(H)0 ≃ Γ({τ > 0}; µhom(F, G)),

where we use the compactness assumption. For ε > 0, we have a fiber sequence

Γ[ε,∞)(R; H) → Γ[0,∞)(R; H) → Γ[0,ε)((−∞, ε); H).

By (2.1), the first term is isomorphic to Hom(F, T−εG) and the second term is isomorphic
to Hom(F, G). Thus, by taking colimit as ε → 0, we obtain the result.

2.3 Hamiltonian action

Let H : T ∗N × I → R be a C∞-function with compact support. Denote by ϕH =
(ϕH
s )s∈I : T ∗N × I → T ∗N be the associated Hamiltonian isotopy. It is proved in [GKS12]
that there exists an object K(ϕH ) ∈ Sh((N ×R)2×I) whose conic microsupport outside the
zero-section is equal to the conic Lagrangian movie associated with the graph of ϕH . The
push forward by the map (N × R)2 × I → N 2 × R × I; (x1, t1, x2, t2, s) ↦→ (x1, x2, t1 − t2, s)
and the quotient morphism Sh(N 2 × R × I) → T (T ∗(N 2 × I)), the object K(ϕH ) defines
K(ϕH ) ∈ T (T ∗(N 2 × I)), which is called the sheaf quantization or the GKS kernel of ϕH .
With a time-independent non-negative C∞-function H : T ∗N → R with non-compact
support, we can associate an object K(ϕH )1 ∈ T (T ∗N 2) as follows. We take a sequence
of compact subset (Kn)n such that ⋃n Int(Kn) = T ∗N and a sequence of cutoff functions
(χn : T ∗N → [0, 1])n of class C∞ such that Hn|Kn ≡ 1, supp(Hn) ⊂ Int(Kn+1), and
Hn ≤ Hn+1. Then Hn := χn · H has a compact support, and thus defines K(ϕHn) ∈
T (T ∗(N 2 × I)). By [GKS12], we have a canonical continuation morphism K(ϕHn)1 →
K(ϕHn+1)1 in T (T ∗N 2) and define

K(ϕH )1 := colim
n K(ϕHn)1 ∈ T (T ∗N 2).

Let φ ∈ Hamc(T ∗N ) be a compactly supported Hamiltonian diffeomorphism on T ∗N .
For a compactly supported C∞-function H : T ∗N × I → R such that ϕH
1 = φ, the object

8

K(ϕH )|s=1 does not depend on the choice of H (see [AI24]), which we will denote by
K(φ) ∈ T (T ∗N 2). We call K(φ) the sheaf quantization or the GKS kernel of φ.
Recall that we set k = F2. In this case, it is proved in [GV24] that the distance
d(K(φ0), K(φ1)) is equal to the spectral metric between φ0 and φ1:

d(K(φ0), K(φ1)) = γ(φ0, φ1).

By [Sey12], for a fixed compact subset K of T ∗N , there exists a constant C′ > 0 such that
for any φ0, φ1 whose supports are contained in K,

γ(φ0, φ1) ≤ C′dC0(φ0, φ1).

By combining these results, we obtain

d(K(φ0), K(φ1)) ≤ C′dC0(φ0, φ1)

for any φ0, φ1 whose supports are contained in K. Since T (T ∗N 2) is complete with
respect to the pseudo-distance d (Proposition 2.2), for any compact supported Hamiltonian
homeomorphism φ on T ∗N , we obtain an object K(φ) ∈ T (T ∗N 2) whose microsupport
is the graph of φ by Proposition 2.3. If there is no confusion, we simply write K(φ)F for
K(φ) ⃝⋆ F .

Lemma 2.8. Let F, G ∈ T η(T ∗N ) and φ be a Hamiltonian homeomorphism with compact
support on T ∗N . Then, one has

q∗ Hom⋆(K(φ)F, K(φ)G) ≃ q∗ Hom⋆(F, G)

Proof. Under the identification T η(T ∗N ) ≃ Sh(N ; T η), q∗ Hom⋆ is the T η-enriched hom
space. Then the result follows since K(φ) ⃝⋆(-) is a T η-linear equivalence.

3 Sheaf quantization associated with Jordan curves

In what follows, until the end of this paper, we set M = Rx.

3.1 Sheaves associated with the torus

In [AI23], the authors constructed small sheaf quantizations for a class of rational La-
grangian immersions following the idea of Guillermou [Gui12; Gui23]. Here, we apply
the sheaf quantization method to the standard unit circle C0 in T ∗Rx ≃ R2 in a more
sophisticated way. The outcome can be seen as a sheaf quantization of C0 × C0 in
T ∗R2 = T ∗(Rx1 × Rx2). In particular, instead of the orbit category, we use the cate-
gory of twisted sheaves, which was introduced in the previous section. This can be done
because of the monotonicity of Lagrangian submanifolds that we will handle.
The idea to construct a sheaf quantization of C0 × C0 as a sheaf on M × M × Rt/πZ
without another extra R-factor is due to St´ephane Guillermou. This makes all the com-
putation much easier.
Set L = C0 to be the standard circle with center (0, 0) and radius 1. Since the space of
1-jet J 1(M ) = T ∗M × Rt has a natural contact structure that is invariant with respect to
the translation in the Rt-direction, the quotient T ∗M × Rt/πZ inherits a natural contact
structure. We define a primitive of C0 valued in R/πZ by f0(s) := 1
2 s − 1
4 sin 2s. We take
a Legendrian lift ̃L in T ∗M × Rt/πZ of L = C0 as follows:

̃L = {((cos s; sin s), −f0(s)) ∈ T ∗M × Rt/πZ | s ∈ R/2πZ} .

9

We also define a Legendrian lift Λ ⊂ T ∗M × T ∗M × Rt/πZ of L × L ⊂ T ∗M 2 by

Λ = {((cos s1; sin s1), (cos s2; sin s2), −f0(s1) − f0(s2)) | s1, s2 ∈ Rt/2πZ}. (3.1)

We identify T ∗M ×Rt/πZ with the subset {τ = 1} in T ∗(M ×R/πZ) as contact manifolds.
Below we will prove the following.

Proposition 3.1. There exists a simple object FC0 ∈ T η(T ∗M 2) such that SS
•(FC0) = Λ
and such an object is unique up to degree shift. Moreover, Hom(FC0, FC0) ≃ H ∗(S1).

We can define the Kashiwara–Schapira stack µsh̃L on ̃L, which is regarded as a subset
of {τ = 1} ⊂ T ∗(M × Rt/πZ). This stack is locally isomorphic to the stack of local
systems, but globally it is twisted. In our setting, this twisting is the delooping of Z →
Pic(k) : 1 ↦→ k[2], which corresponds to the first Maslov class of L. We write η−1 for the
twisting L → B Pic(k) and write η for its inverse. Then we have an isomorphism of stacks
µsh̃L ≃ Loc
η−1
̃L , where the right-hand side denotes the stack of local systems with twisting
η−1. By twisting, we have an isomorphism µshη
̃L ≃ Loc̃L, which has a global object.

Remark 3.2. As explained in [JT17], the twisting η−1 : L → B Pic(k) is described as the
composite of the Gauss map, (the delooping of) the J-homomorphism, and the morphism
induced by the unit morphism S → Hk, where S denotes the sphere spectrum and Hk
denotes the Eilenberg–MacLane spectrum. In order to get the above isomorphism, we need
to choose a homotopy between L → U/O → B Pic(S) → B Pic(k) and η−1. The connected
components of the space of such homotopies forms a Z-torsor, and each component is
contractible. We can freely choose a connected component for the following argument.
The differences of the choices affect as overall degree shifts.

The twisting η : ̃L ≃ L → B Pic(k) factors through the base space M × Rt/πZ. Since
the projection π : ̃L → M × Rt/πZ is of finite position, we can apply the doubling method
(with cusp doubling, which is used in [NS20; GPS24; IK23]) by Guillermou to obtain a
morphism of stacks on M × Rt/πZ:

π∗ µshη
̃L → Sh
η
Λ((-) × (−1, −1 + ε))

for sufficiently small ε > 0. Here, the right-hand side denotes the stack defined as U ↦→
Sh
η
Λ∩T ∗(U ×(−1,−1+ε))(U × (−1, −1 + ε)) for an open subset U of M × Rt/πZ.
For x ∈ (−1, 1), the set Λx := πξ2(Λ ∩ {x2 = x}) ⊂ T ∗M × Rt/πZ consists of the
two copies of ̃L shifted to the Rt-direction. There exists a contact isotopy (ψx)x∈(−1,1)
on T ∗M × Rt/πZ such that ψ0 = id and ψx(Λ0) = Λx. By applying the GKS kernels
associated with the contact isotopy, we obtain an isomorphism

Sh
η
Λ(M × Rt/πZ × (−1, −1 + ε)) ≃ Sh
η
Λ(M × Rt/πZ × (−1, 1)).

Let L be a global object of LocL. By sending L through the identification µshη
̃L ≃ Loc̃L
and the morphism above, we obtain a sheaf quantization GL,C0 ∈ Sh
η(M × Rt/πZ ×
(−1, 1)). Denote by j : (−1, 1) ↪→ M = Rx2 the inclusion and also write j for the base
change M × Rt/πZ × (−1, 1) → M × M × Rt/πZ. By pushing forward under j, we obtain
an object FL,C0 := j!GL,C0.

Lemma 3.3. One has j!GL,C0 ≃ j∗GL,C0, and they are objects of T η
Λ (T ∗M 2).

10

Proof. By the construction j∗GL,C0|{x2=−1} is 0. Let i be the inclusion M ×{1}×Rt/πZ →
M 2 × Rt/πZ. There is a cofiber sequence j!GL,C0 → j∗GL,C0 → i∗i∗j∗GL,C0. The (conic)
microsupport estimates shows SS(i∗j∗GL,C0) ⊂ T π
2 ̃L, and hence a similar estimate for
SS(ℓ!i∗j∗GL,C0) holds since ℓ is a submersion. By [STZ17, Proposition 5.8], ℓ!i∗j∗GL,C0
must be a local system and becomes 0 in T (T ∗M ). Since ℓ! is conservative, i∗j∗GL,C0 is
also 0. By estimating the both sides of SS(j!GL,C0) = SS(j∗GL,C0), we find that FL,C0 ∈
T η
Λ (T ∗M 2).

We set FC0 := Fk,C0, where k denotes the trivial local system of rank 1 on L.

Lemma 3.4. The functor Loc̃L(̃L) → T η
Λ (T ∗M 2) is fully faithful.

Proof. By [NS20], the functor Loc̃L(̃L) → Sh
η
Λ(M × Rt/πZ × (−1, −1 + ε)) is fully faithful.
As the composite, the functor Loc̃L(̃L) → Sh
η
Λ(M × Rt/πZ × (−1, 1)) is also fully faithful.
One can check that the image of the functor is in T η(T ∗N ), which is regarded as a
subcategory of Shη(N × Rt/πZ). Since End(j!G) ≃ Hom(G, j!j!G) ≃ End(G), the functor
j! is also fully faithful. By combining these, we obtain the result.

By Lemma 3.4, we have

HomT η(T ∗M 2)(FC0, FC0) ≃ HomLocL(k, k) ≃ H ∗(S1),

where k denotes the trivial local system of rank 1 on L.
We shall prove the uniqueness by decomposing the sheaf into easier pieces. A similar
argument can be found in [Gui23, Part VI].

Lemma 3.5. Simple objects in T η
Λ (T ∗M 2) are unique up to shift.

Proof. Let us first observe the image of the projection Λ → M 2 × Rt/πZ. The immersed
locus is given by

((cos ±s; sin ±s), (cos ∓s, sin ∓s), −f0(±s) − f0(∓s)) ↦→ (cos s, cos s, 0)

and
 ((cos ±s; sin ±s), (cos π ∓ s, sin π ∓ s), −f0(±s) − f0(π ∓ s)) ↦→ (cos s, − cos s, π
2 ).

We take t0, t3 in Remark 2.6 so that −π/2 < t0 < t3 − π < 0. We note that ℓ((t0, t3 − π))
does not contain 0 nor π
2 .
We will see that simple sheaves on M 2×(t0, t3) with SS
• ⊂ ℓ−1(Λ)∩T ∗M 2×(t0, t3) that
corresponds to an object of T η(T ∗M 2) are unique up to shift. Let F ∈ Sh(M 2 × (t0, t3))
be such a sheaf. The support of F on M 2 × (t0, t3) is bounded since F corresponds to
an object in T η
Λ (T ∗M 2), which implies that the support is the union of the closures of
three bounded regions. We write F as an extension of F(t0,0), F[0,π/2) and F[π/2,t3). Each
of F(t0,0), F[0,π/2), F[π/2,t3) is unique up to shift by the microsupport condition. The non-
trivial extension class is also unique.
The choice of an isomorphism α : F(t0,t3−π)[−2] ∼
−→ T−πF(t0+π,t3) is also unique. This
proves the lemma.

This completes the proof of Proposition 3.1.

11

Remark 3.6. The existence of sheaf quantization FC0 of C0 × C0 ⊂ T ∗M 2 in the category
T η(T ∗M 2) would be related to the fact that C0×C0 admits a bounding cochain [FOOO09].
In contrast, C0 ⊂ T ∗R does not admit a bounding cochain and is unobstructed only
modulo T π in the sense of [FOOO09], which would be why one can only construct a sheaf
quantization of C0 in Sh(M × (0, π) × Rt/πZ) with the doubling parameter (cf. [AI23]).

Corollary 3.7. The natural morphism FC0 → TπFC0 induced by the natural transforma-
tion id = T0 ⇒ Tπ is zero.

Proof. Since Hom(FC0, TπFC0) ≃ End(FC0)[2] ≃ H ∗(S1)[2],

we have H 0(Hom(FC0, TπFC0)) = 0.

We shall describe the morphism

H ∗(C0) ≃ Hom(FC0, FC0) → Γ({τ > 0}; µhom(FC0, FC0)) ≃ H ∗(C0 × C0). (3.2)

The generator v ∈ H 1(C0) is sent to v ⊗ 1 + 1 ⊗ v ∈ H 1(C0 × C0). Indeed, we find that
the coefficient of v ⊗ 1 is non-trivial by construction, and that of 1 ⊗ v by symmetry with
respect to (z1, z2) ↦→ (z2, z1).

Let ϕ be a Hamiltonian diffeomorphism with compact support on T ∗M , and denote
by K(ϕ × ϕ) ∈ T (T ∗M 4) the sheaf quantization of ϕ × ϕ. Then the composition with
K(ϕ × ϕ) induces a T η-linear autoequivalence of the category T η(T ∗M 2). Moreover, we
have MS(K(ϕ × ϕ)F ) = (ϕ × ϕ)(MS(F )) for any F ∈ T η(T ∗M 2). Thus, FC = K(ϕ × ϕ)FC0
is a sheaf quantization for C × C = (ϕ × ϕ)(C0 × C0).

3.2 Action of Rθ

Now we consider the action of Rθ defined in (1.1) on T η(T ∗M 2). The Hamiltonian function
of Rθ is the non-negative function H : T ∗M 2 ≃ C2 defined as H(z1, z2) = |z1 − z2|2/4.
Hence, we can construct an object K(ϕH )θ ∈ T (T ∗M 2) for any θ. By [GKS12], we have
continuation morphisms K(ϕH )θ → K(ϕH )θ′ (θ ≤ θ′). By abuse of notation, we also write
Rθ for K(ϕH )θ ⃝⋆(-), the automorphism on T η(T ∗M 2).
The Hamiltonian function H which generates the Hamiltonian isotopy (Rθ)θ also de-
fines a contact isotopy ̃R = ( ̃Rθ)θ on {τ = 1}. This isotopy ̃R = ( ̃Rθ)θ is the product of
(Rθ)θ and the identity morphism of Rt/πZ.

Lemma 3.8. There is an isomorphism K(ϕH )2π ≃ k∆×[0,∞)[2]. Hence, the functor R2π
on T η(T ∗M 2) coincides with the degree shift [2].

Proof. First we have the (conic) microsupport estimate SS(K(ϕH )2π) = SS(k∆×[0,∞)).
Moreover, K(ϕH )2π is simple along its conic microsupport. Since k = F2, we obtain
K(ϕH )2π ≃ k∆×[0,∞)[d] for some d ∈ Z. We can observe the grading by tracing the action
on the fiberwise universal covering space of the Lagrangian Grassmannian bundle of T ∗M 2

as in [Sei00].

Remark 3.9. For our purpose, it is enough to cut off the support of H outside a sufficiently
large compact subset. Then we only need sheaf quantization of Hamiltonian isotopies with
compact support. From this position, the statement of Lemma 3.8 should be understood
as that the action of R2π on the objects whose microsupports are contained in the compact
subset coincides with the degree shift [2].
 12

We can also determine RπFC0 as follows.

Lemma 3.10. One has an isomorphism

RπFC0 ≃ FC0[1].

Proof. Since SS(RπFC0) = Λ, by the uniqueness in Proposition 3.1, we have RπFC0 ≃
FC0[d] for some d ∈ Z. Then, by Lemma 3.8,

FC0[2] ≃ R2πFC0 ≃ RπFC0[d] ≃ FC0[2d],

which concludes d = 1.

3.3 Computation for the standard circle

Let FC0 ∈ T η(T ∗M 2) be the sheaf quantization of the standard torus C0 × C0 constructed
in Proposition 3.1. We define

VC0,θ := ℓ!q∗ Hom⋆(FC0, RθFC0) ∈ T (pt),

where q : M 2 × Rt/πZ → Rt/πZ and ℓ : Rt → Rt/πZ are the projection and the quotient
map. It is also convenient to consider the family version

VC0 := (ℓ × id[0,π])!(q × id[0,π])∗ Hom⋆(q′∗FC0, RFC0) ∈ Sh([0, π]; T (pt)),

where R is the GKS kernel for the (full) Hamiltonian isotopy (Rθ)θ∈[0,π] and q′ : M 2 ×
Rt/πZ × [0, π] → M 2 × Rt/πZ is the projection. For θ0 ∈ [0, π], we have an isomorphism
VC0|{θ=θ0} ≃ VC0,θ0.
For each θ ∈ (0, π) and a ∈ [−π, 0], we can directly check that

T−a ̃Rθ(Λ)∩Λ =
 




{((cos s; sin s), (cos s; sin s), −2f0(s)) | s ∈ R/2πZ} (a = 0)
{((cos s; sin s), (− cos s; − sin s), −2f0(s) − π
2 ) ∣
∣ s ∈ R/2πZ
} (a = −θ)
∅ (otherwise).

Decompose the strip R × [0, π] into locally closed isosceles right triangles as follows:

△n := {(t, θ) | nπ ≤ t < nπ + θ},

▽n := {(t, θ) | (n − 1)π + θ ≤ t < nπ}.

We also set △′
n := {(t, θ) | nπ < t ≤ nπ + θ},

▽′
n := {(t, θ) | (n − 1)π + θ < t ≤ nπ}.

By the microlocal Morse lemma and the intersection estimate above, we obtain the fol-
lowing:

Proposition 3.11. If (a0, θ0) and (a1, θ1) belong to the same component of the decompo-
sition by △′
n’s and ▽′
n’s, then

Hom(FC0, T−a0Rθ0FC0) ≃ Hom(FC0, T−a1Rθ1FC0)

as End(FC0)-modules. If (a, θ) ∈△′
n, we have

Hom(FC0, T−aRθFC0) ≃ Hom(FC0, T−(n+1)πRπFC0) ≃ End(FC0)[−2n − 1].

If (a, θ) ∈ ▽′
n, we have

Hom(FC0, T−aRθFC0) ≃ Hom(FC0, T−nπFC0) ≃ End(FC0)[−2n].

13

It is not difficult to determine the whole structure of VC0 and VC0,θ as follows. We will
not use the following proposition and omit the proof.

Proposition 3.12. One has an isomorphism

VC0 ≃ ⊕

n∈Z k△n∪▽n+1[−2n] ⊕ ⊕

n∈Z k△n∪▽n[−2n + 1].

For θ ∈ [0, π], one has an isomorphism

VC0,θ ≃ ⊕

n∈Z k[nπ,(n+1)π)[−2n] ⊕ ⊕

n∈Z k[θ+(n−1)π,θ+nπ)[−2n + 1].

Moreover, for any a ∈ R, the right action of v ∈ H 1(S1) on the stalk (Vθ)a is non-zero.

4 Sheaf-theoretic condition for rectangular peg

In this section, we prove the following theorem.

Theorem 4.1. Let ϕ be a Hamiltonian homeomorphism with compact support. Let us
consider the Jordan curve C = ϕ(C0). Define FC := K(ϕ × ϕ)FC0. If Ta SS
•(FC) ∩
SS
•(FC) = ∅ for any a ∈ R \ πZ, then C inscribes a θ-rectangle for any θ ∈ (0, π).

Before starting the proof, we give its rough outline. We consider the persistence module
(Hom(FC, TaRθFC))a∈R (in the derived sense) with structure morphisms (τa,a′)a≤a′. We
focus on a “critical value” a0 ∈ R such that τa,a′ is not an isomorphism if a < a0 < a′. We
will prove:

(A) A critical value a0 is produced by some subset in the intersection (C ×C)∩Rθ(C ×C).

(B) Under the assumption Ta SS
•(FC) ∩ SS
•(FC) = ∅ for any a ∈ R \ πZ, a critical value
produced by the diagonal ∆C in the sense of (A) is in πZ.

(C) There is a critical value a0 in R \ πZ.

These three assertions prove the existence of a point in (C × C) ∩ Rθ(C × C) \ ∆C, which
implies the existence of a θ-rectangle on C.
By Lemma 2.7, we find that the change at a ∈ R can be described by µhom(FC, TaRθFC)|{τ >0},
which is supported in (the conification of)

SS
•(FC) ∩ Ta SS
•(RθFC) ⊂ ρ
−1((C × C) ∩ Rθ(C × C)).

This proves the assertions (A) as well as (B) since

SS
•(FC) ∩ Ta SS
•(RθFC) ∩ ρ
−1(∆C) = SS•(FC) ∩ Ta SS
•(FC) ∩ ρ
−1(∆C) = ∅

for a ∈ R \ πZ. The most technical part is the proof of the assertion (C). For that purpose,
we consider the value a(θ, C) informally defined as

a(θ, C) = {a ∈ R≥0 | v can be lifted to Hom(FC, T−aRθFC)},

where v ∈ H 1(End(FC)) ≃ H 1(S1) is the generator. Then −a(θ, C) is a critical value, and
we will prove a(θ, C) ∈ (0, π) for any θ in Lemma 4.8. Most of this section is devoted to
the proof of this lemma, for which we will study µhom(FC, RθFC).

14

Remark 4.2. By the arguments in this section, we will find the following. For a fixed
θ ∈ (0, π), if there exists a critical value a0 ∈ R such that

Γ(ρ
−1(∆C); µhom(FC, Ta0RθFC)|ρ−1(∆C )) ≃ 0,

then C inscribes a θ-rectangle. In particular, to prove the existence of a θ-rectangle, it is
enough to show the cohomology vanishing for a0 = −a(θ, C). The only reasonable case
the authors know for ensuring the vanishing is the assumption for the conic microsupport
in Theorem 4.1.

Let us start the proof of the theorem. First note that by Proposition 5.1, which will
be proved in Section 5, FC is limit constructible. We define

VC,θ := ℓ
!q∗ Hom⋆(FC, RθFC) ∈ T (pt),

where q : M 2 × Rt/πZ → Rt/πZ is the projection. This object VC,θ is also limit con-
structible. We introduce the self-map on C2 by

Rϕ
θ := (ϕ × ϕ)−1Rθ(ϕ × ϕ).

Note that Rϕ
π = Rπ. We also write Rϕ
θ for the GKS kernel K(ϕ × ϕ)⃝⋆ −1RθK(ϕ × ϕ) by
abuse of notation. By Lemma 2.8, we have an isomorphism in T (pt):

VC,θ ≃ ℓ!q∗ Hom⋆(FC0, Rϕ
θ FC0).

The continuation morphism VC,0 → VC,θ → VC,π is compatible with the continuation
morphism VC0,0 → VC0,π. Since we have a homotopy between (Rθ)θ∈[0,π] and (Rϕ
θ )θ∈[0,π]
relative to the boundary, we find that the continuation morphisms id → Rπ and id → Rϕ
π
are the same via the identification Rπ ≃ Rϕ
π. Indeed, we get the result when ϕ is smooth
by the argument in [Kuo23, Subsection 3.1], and for a Hamiltonian homeomorphism ϕ, we
obtain the result by taking limits.
For a, a′ ∈ R with a ≤ a′ and θ, θ′ ∈ R with θ ≤ θ′, we denote the continuation
morphism by τ θ,θ′
a,a′ : TaRϕ
θ FC0 → Ta′Rϕ
θ′FC0.

Recall that we let v ∈ H 1(S1) be a generator.

Lemma 4.3. For any θ ∈ (0, π), the right action of v ∈ H 1(S1) ≃ H 1(End(FC0)) on the
cohomology of µhom(FC0, Rϕ
θ FC0) that corresponds to the morphism τ 0,θ
0,0 : FC0 → Rϕ
θ FC0
is zero.

Proof. Take 0 = θ0 < θ1 < θ2 < · · · < θn < θn+1 = θ. Then the canonical morphism
µhom(FC0, FC0) → µhom(FC0, Rϕ
θ FC0) factors as follows:

µhom(FC0, FC0) µhom(FC0, Rϕ
θ FC0)

⊗n
i=0 µhom(Rϕ
θiFC0, Rϕ
θi+1FC0).

Recall that Λ defined in (3.1) and consider its conification R>0Λ ⊂ T ∗(M × M × Rt/πZ).
Note that µhom(FC0, FC0) ≃ kR>0Λ. The support of the sheaf ⊗n
i=0 µhom(Rϕ
θiFC0, Rϕ
θi+1FC0)
is contained in n⋂

i=0 ρ
−1Rϕ
θi(C0 × C0) ∩ R>0Λ

15

By taking refinements, we find that the canonical morphism factors through the limit as
follows:

µhom(FC0, FC0) µhom(FC0, Rϕ
θ FC0)

lim ⊗n
i=0 µhom(Rϕ
θiFC0, Rϕ
θi+1FC0),

where the limit in the second row is taken with respect to all the refinements. The support
of lim ⊗n
i=0 µhom(Rϕ
θiFC0, Rϕ
θi+1FC0) is contained in

⋂

θ′∈[0,θ] ρ
−1Rϕ
θ′(C0 × C0) ∩ R>0Λ.

We say an arc in C is a θ-arc in C if there exists z0 ∈ C and r > 0 such that the arc coincides
the arc with angle θ in the circle {z ∈ C | |z − z0| = r}. If (z, z′) ∈ ⋂θ′∈[0,θ] Rϕ
θ′(C0 × C0) \
∆C0, then there exist two θ-arcs in C (with counterclockwise directions) and ϕ(z), ϕ(z′) ∈
C are both starting points of these θ-arcs. We set

Z = {
z ∈ C ∣
∣ z is a starting point of a (counterclockwise) θ-arc in C} . (4.1)

We assume that C is not a circle. In this case, we can take an open subset U ⊂ C0
such that ϕ(U ) has no intersection with Z. Then, we have
⋂

θ′∈[0,θ] Rϕ
θ′(C0 × C0) ∩ ((U × C0 ∪ C0 × U ) \ ∆C0) = ∅.

Setting Ξ := ρ−1(C0 × C0 \ ((U × C0 ∪ C0 × U ) \ ∆C0)) ∩ R>0Λ,

we find that the right action of v on Γ(Ξ; µhom(FC0, FC0)) is zero since the morphism (3.2)
maps v to v ⊗ 1 + 1 ⊗ v and the restriction of v ⊗ 1 + 1 ⊗ v to Ξ is zero.
For the case that C is a circle, this vanishing of v ⊗ 1 + 1 ⊗ v on the support is obvious
from an explicit calculation of the support. This completes the proof.

Lemma 4.4. For any θ ∈ (0, π), the composite of the morphisms τ θ,π
0,0 : Rϕ
θ FC0 → Rϕ
πFC0 ≃

RπFC0 and Rπv : RπFC0 → RπFC0[1] is zero in Γ({τ > 0}; µhom(Rϕ
θ FC0, RπFC0))[1].
Moreover, the composite

µhom(FC0, Rϕ
θ FC0) ◦v
−→ µhom(FC0, Rϕ
θ FC0)[1] → µhom(FC0, RπFC0)[1] (4.2)

is the zero morphism.

Proof. The first assertion can be proved in a similar way in Lemma 4.3. Since the mor-
phism (4.2) is equal to

µhom(FC0, Rϕ
θ FC0) → µhom(FC0, RπFC0) v◦
−→ µhom(FC0, RπFC0)[1]

with Rπv = v, the second assertion follows.
16

Now we consider the following commutative diagram whose rows are (co)fiber sequences
by Lemma 2.7:

colim
ε→0 Hom(FC0, T−εFC0) End(FC0) Γ({τ > 0}; µhom(FC0, FC0))

colim
ε→0 Hom(FC0, T−εRϕ
θ FC0) Hom(FC0, Rϕ
θ FC0) Γ({τ > 0}; µhom(FC0, Rϕ
θ FC0)).

Then the image of v in the right below is zero by Lemma 4.3. We take an arbitrary element
wθ ∈ colimε→0 Hom(FC0, T−εRϕ
θ FC0)[1] that is mapped to τ 0,θ
0,0 v ∈ Hom(FC0, Rϕ
θ FC0)[1].

Note that the continuation morphism τ θ,π
−ε,−ε induces a morphism

colim τ θ,π
−ε,−ε : colim
ε→0 Hom(FC0, T−εRϕ
θ FC0) → colim
ε→0 Hom(FC0, T−εRπFC0).

Lemma 4.5. The element colim τ θ,π
−ε,−εwθv ∈ colimε→0 Hom(FC0, T−εRπFC0)[2] is inde-
pendent of the choices of θ ∈ (0, π) and wθ.

Proof. First, fix θ and consider two elements wθ
0 and wθ
1 that are mapped to τ 0,θ
0,0 v. By
the (co)fiber sequence above, the difference wθ
0 − wθ
1 is written as the image of an element
α ∈ Γ({τ > 0}; µhom(FC0, Rϕ
θ FC0)). The morphism that sends α to colim τ θ,π
−ε,−ε(wθ
0 −wθ
1)v
factors the morphism

Γ({τ > 0}; µhom(FC0, Rϕ
θ FC0)) → Γ({τ > 0}; µhom(FC0, RπFC0))[1],

which is zero by Lemma 4.4. This proves colim τ θ,π
−ε,−ε(wθ
0 − wθ
1)v = 0.
Next, we will prove the independence on θ. Let θ ≤ θ′ and take wθ and wθ′ that are
mapped to v. Then we can apply the above argument to the two element colim τ θ,θ′
−ε,−εwθ

and wθ′ in colimε→0 Hom(FC0, T−εRϕ
θ FC0)[1], which prove the lemma.

Lemma 4.6. The colim τ θ,π
−ε,−εwθv ∈ colimε→0 Hom(FC0, T−εRπFC0)[2] is non-zero.

Proof. By Lemma 4.5, it is enough to show the claim for a sufficiently small θ > 0.
Let us first consider the case ϕ is a Hamiltonian diffeomorphism with compact support.
In this case, we will reduce the problem to the case of the standard circle C0. There exists
a bi-Lipschitz constant B such that

1
B dE(z, z′) ≤ dE(ϕ(z), ϕ(z′)) ≤ BdE(z, z′)

for any z, z′ ∈ C, where dE stands for the Euclidean metric. Note that Rθ is generated by
H(z1, z2) = |z1 − z2|2/4 and Rϕ
θ is generated by H ϕ = H ◦ (ϕ × ϕ), which implies

1
B2 H ≤ H ϕ ≤ B2H.

Hence, as positive Hamiltonian isotopies, we have

id ≤ Rθ/B2 ≤ Rϕ
θ ≤ RB2θ for θ ≥ 0,

which gives continuation morphisms.
 17

We take θ > 0 satisfying B2θ < π. Then, for 0 < ε < θ/B2, we have the following
interleaving

Hom(FC0, T−εRθ/B2FC0) → Hom(FC0, T−εRϕ
θ FC0) → Hom(FC0, T−εRπFC0). (4.3)

We take an element wθ
ε ∈ Hom(FC0, T−εRθ/B2FC0)[1] that is mapped to the image of
v in Hom(FC0, Rθ/B2FC0)[1] via the continuation morphism. Its image under the first
interleaving morphism in (4.3) defines an element wθ ∈ colimε→0 Hom(FC0, T−εRϕ
θ FC0)[1],
which is mapped to τ 0,θ
0,0 v ∈ Hom(FC0, Rϕ
θ FC0)[1]. By the arguments in Subsection 3.3, we
find that wθ
εv ∈ Hom(FC0, T−εRθ/B2FC0)[2] is non-zero and both of the morphisms

Hom(FC0, T−εRθ/B2FC0) → Hom(FC0, T−εRπFC0) and

Hom(FC0, T−εRπFC0) → colim
ε→0 Hom(FC0, T−εRπFC0)

are isomorphisms by Proposition 3.11. Hence colim τ θ,π
−ε,−εwθv is non-zero.
Now we consider the continuous case and take a sequence of Hamiltonian diffeomor-
phisms with compact support (ϕn)n that converges to a Hamiltonian homeomorphism ϕ
in the C0-sense. We take (ϕn)n so that each Cn := ϕn(C0) is real analytic. Since the
Hamiltonian function H is bounded on C × C, we can choose sufficiently small θ0 > 0
so that supθ∈[0,θ0] d(FC0, Rϕ
θ FC0) is sufficiently small. Take ε > 0 and a representative

wθ
ε ∈ Hom(FC0, T−εRϕ
θ0FC0)[1] of wθ. For a sufficiently large n, there is a (δ, δ)-interleaving

for the pair (Rϕ
θ0FC0, Rϕn
θ0 FC0), where δ < ε/100.
Let us consider the following commutative diagram:

FC0 T−εRϕ
θ0FC0[1] T−ε+δRϕn
θ0 FC0[1] Rϕn
θ0 FC0[1]

T−εRϕ
πFC0[1] T−ε+δRϕn
π FC0[1].

We claim that the upper morphism FC0 → Rϕn
θ0 FC0[1] is τ 0,θ0
0,0 v. We postpone the proof of
this claim and first prove the assertion of the lemma. By the smooth case proved above,
the composite of v and the morphism FC0 → T−ε+δRϕn
π FC0[1] is non-zero. Hence, the
composite of v and the morphism FC0 → T−εRϕ
πFC0[1] is also non-zero. Then the result
follows from the fact that

Hom(FC0, T−εRϕ
πFC0) → colim
ε→0 Hom(FC0, T−εRϕ
πFC0)

is an isomorphism.
Let us prove the remaining claim by investigating the following two quantities a(θ, Cn)
and b(θ, Cn) defined for θ ∈ [0, π) and Cn with the property τ 0,θ
0,0 v ̸= 0 ∈ Γ[0,∞)(R; VCn,θ)[1]:

a(θ, Cn) := sup{a ∈ R≥0 | τ 0,θ
0,0 v is in the image of Γ[a,∞)(R; VCn,θ)[1]},

b(θ, Cn) := sup
 



b ∈ R≥0
 ∣
∣
∣
∣
∣
∣
∣
 there exist w ∈ Γ[b,∞)(R; VCn,θ)[1] and t ∈ R≥0

such that w and τ 0,θ
0,0 v coincide in Γ[−t,∞)(R; VCn,θ)[1]

as non-zero elements
 


 .

By definition a(θ, Cn) ≤ b(θ, Cn), and we already know b(θ0, Cn) ≥ ε − δ. We will show
a(θ0, Cn) = b(θ0, Cn) and then obtain the claim with the interleaving for (Rϕ
θ0FC0, Rϕn
θ0 FC0).

18

We will prove it by contradiction and suppose that a(θ0, Cn) ̸= b(θ0, Cn). Consider the
real number θ1 := inf{θ ∈ [0, θ0] | a(θ, Cn) ̸= b(θ, Cn)}.

By the analyticity of Cn, the family (Hom(FC0, Rϕn
θ FC0))θ is constant for sufficiently small
θ > 0. By the interleaving with C0 as above, H 1(Hom(FC0, Rϕn
θ FC0)) is 1-dimensional,
and hence it contains a unique non-zero element. This proves a(θ, Cn) = b(θ, Cn) for a
sufficiently small θ, which implies θ1 > 0. Consider the continuous family (VCn,θ)θ of
constructible sheaves on R, which can be regarded as a family of persistence modules (in
the derived sense). For 0 ≤ θ < θ1, the element τ 0,θ
0,0 v corresponds to an interval module
that is a summand of VCn,θ and has a length close to π. When θ exceeds θ1, a change
of basis occurs and the element no longer corresponds to a single interval module. For
such a change of basis, there needs to be another interval module of the same length.
However, since θ0 is sufficiently small, such an interval module cannot exist, which makes
a contradiction.

Lemma 4.7. For any θ ∈ (0, π), the element τ 0,θ
0,0 v is non-zero in Hom(FC0, Rϕ
θ FC0)[1] ≃
Hom(FC, RθFC)[1].

Proof. If τ 0,θ
0,0 v = 0, we can take wθ as the zero element. This contradicts to Lemmas 4.5
and 4.6.

By Lemma 4.7 and Corollary 3.7, we can define a(θ, C) by

a(θ, C) := sup{a ∈ R≥0 | τ 0,θ
0,0 v is in the image of Γ[a,∞)(R; VC,θ)[1]} ∈ R≥0,

which already appeared in the proof of Lemma 4.6.

Lemma 4.8. For any θ ∈ (0, π), one has a(θ, C) ∈ (0, π).

Proof. By the argument before Lemma 4.5, the element τ 0,θ
0,0 v comes from Γ[εθ,∞)(R; VC,θ)[1]
for some εθ > 0, which shows a(θ, C) > 0.
By Proposition 5.1 in the next section, the object VC,θ ∈ T (pt) is limit constructible.
By Proposition 2.5, we find that v is non-zero in Γ[−ε,∞)(R; VC,θ)[1] for a sufficiently
small ε > 0. By Corollary 3.7, v does not come from Γ[π−ε,∞)(R; VC,θ)[1], which proves
a(θ, C) < π.

We will finish the proof of Theorem 4.1. The object VC,θ has a non-zero microstalk
over a(θ, C), which implies SS•(FC) ∩ T−a(θ,C) SS
•(RθFC) ̸= ∅. By the assumption and
Lemma 4.8, we find that SS
•(FC) ∩ T−a(θ,C) SS
•(FC) = ∅. Thus, we have (SS•(FC) ∩
T−a(θ,C) SS
•(RθFC)) \ ρ−1(∆C) ̸= ∅, which corresponds to θ-rectangles on C. This com-
pletes the proof of Theorem 4.1.

5 Jordan curves

In this section, we deduce Theorem 1.1 from Theorem 4.1. We also deduce Corollaries 1.2
and 1.3 from Theorem 1.1. Throughout this section, we let Dq be the open disk {z ∈ C |
|z| < q} in C ≃ R2 for q > 0. We also set Aq := {z ∈ C | q < |z| < 1} for q ∈ (0, 1). For a
Jordan curve C, we let A(C) denote the area of the open domain bounded by C.

19

5.1 Proof of the main theorem

For a proof of Theorem 1.1, we first prove the following:

Proposition 5.1. Let (cn : S1 → R2)n be a sequence of smooth curves. Assume that
(cn)n converges to a Jordan curve c in the C0-sense and the area of the domain bounded by
Cn = cn(S1) and C = c(S1) are π, that is, A(Cn) = π and A(C) = π. Then the sequence of
sheaf quantizations (FCn)n is a Cauchy sequence (after translated to the Rt/πZ-direction),
whose limit object F is limit constructible.
Moreover, if there exists a Hamiltonian homeomorphism with compact support ϕ such
that C = ϕ(S1), then F ≃ FC := K(ϕ × ϕ)FC0.

Proof. We may assume that the origin is bounded by Cn for all n.
(a) First we will prove (FCn)n is a Cauchy sequence.
Let D be the open domain bounded by C. We take a biholomorphism ψ : D1 → D with
ψ(0) = 0 and extend it to a homeomorphism ψ : D1 → D by the Riemann mapping theorem
and the Carath´eodory theorem. There is a strictly increasing function g : (0, 1] → (0, 1]
such that the area Da := ψ(Dg(a)) is πa2. Then, the family of open subdomains (Da)a∈(0,1]
satisfy the following:

• if a < a′, then Da ⊂ Da′;

• for each a ∈ (0, 1), the boundary ∂Da is a smooth Jordan curve;

• there exists a positive real number L such that

1
2π
 ( max
{a}×[0,2π] ̃θψ − min
{a}×[0,2π] ̃θψ
) ≤ Lψ

for any a ∈ (0, 1]. Here ̃θψ : (0, 1] × [0, 2π] → R denotes a lift of

(0, 1] × [0, 2π] (r,θ)↦→re
√−1θ
−−−−−−−−→ D \ {0} ψ
−→ D \ {0} θ
−→ R/2πZ,

where θ denotes the locally defined argument. This Lψ depends only on ψ.

To prove the last claim, we take ε > 0 and consider the annulus Aε = {z ∈ C | ε < |z| < 1}.
Then we can apply Lemma 5.2 below to get

1
2π
 ( max
{a}×[0,2π] ̃θψ − min
{a}×[0,2π] ̃θψ
) ≤ L,

where L can be chosen so that

L ≤ 1
2π max { max
{ε}×[0,2π] ̃θψ − min
{ε}×[0,2π] ̃θψ, max
{1}×[0,2π] ̃θψ − min
{1}×[0,2π] ̃θψ
} + 1.

Since ψ is differentiable at 0, given δ > 0, there exists a sufficiently small ε > 0 such that
max{a}×[0,2π] ̃θψ − min{a}×[0,2π] ̃θψ ≤ 2π + δ for any a ∈ (0, ε]. It suffices to define

Lψ := 1
2π max {
2π, max
{1}×[0,2π] ̃θψ − min
{1}×[0,2π] ̃θψ
} + 1,

which proves the claim.
Take a < 1 that is sufficiently close to 1. By the C0-convergence, there exists N such
that if n ≥ N then Cn is included in the complement of Da. Let Aa,n be the domain
between ∂Da and Cn. Note that the area of Aa,n is π(1 − a2). There exist a unique
real number q ∈ (0, 1) such that the standard annulus Aq = {z ∈ C | q < |z| < 1} is
biholomorphic to the open domain Aa,n. Take a biholomorphism φn : Aq → Aa,n so that
the continuous extension φn : Aq → Aa,n of φn satisfies

20

• φn sends ∂D1 to Cn;

• φn sends q ∈ ∂Dq to ψ(g(a)) ∈ ∂Da, where g(a) is regarded as a point on ∂Dg(a).

Since the boundary components of Aa,n are smooth curves, φn is smooth also at the
boundaries by [GM05, Chapter II. Cor. 4.6]. Let ̃θn : (q, 1) × [0, 2π] → R be a lift of

(q, 1) × [0, 2π] → Aq φn
−−→ Aa,n θ
−→ R/2πZ. By the condition of φn, we have

max
{q}×[0,2π] ̃θn − min
{q}×[0,2π] ̃θn = max
{q}×[0,2π] ̃θψ − min
{q}×[0,2π] ̃θψ.

Since (cn)n converges c in the C0-sense, there exists a sequence of self-homeomorphisms
(σn)n of ∂D1 such that φn ◦ σn converges to ψ|∂D1 in the C0-sense. Take a lift ̃θ′
n of

[0, 2π] → ∂D1 φn◦σn
−−−−→ φn(∂D1) θ
−→ R/2πZ. We will prove the inequality
∣
∣
∣
∣

( max
{1}×[0,2π] ̃θn − min
{1}×[0,2π] ̃θn
) − (max
[0,2π] ̃θ′
n − min
[0,2π] ̃θ′
n
)∣
∣
∣
∣ ≤ 2π. (5.1)

By abuse of notation, we also write ̃θn for a lift of R θ↦→e
√−1θ
−−−−−−→ ∂D1 → φn(∂D1) → R/2πZ
to R → R. Then, we get

max
{1}×[0,2π] ̃θn − min
{1}×[0,2π] ̃θn + 2π = max
{1}×[0,4π] ̃θn − min
{1}×[0,4π] ̃θn.

Moreover, there exists b ∈ [0, 2π] satisfying

max
[0,2π] ̃θ′
n − min
[0,2π] ̃θ′
n = max
{1}×[b,b+2π] ̃θn − min
{1}×[b,b+2π] ̃θn,

which proves the inequality (5.1). By (5.1) and the C0-convergence, for a sufficiently large
n, we have
∣
∣
∣
∣

( max
{1}×[0,2π] ̃θn − min
{1}×[0,2π] ̃θn
) − ( max
{1}×[0,2π] ̃θψ − min
{1}×[0,2π] ̃θψ
)∣
∣
∣
∣ ≤ 2.1π.

Thus, setting L′ := Lψ + 2.1/2, by Lemma 5.2, we have

1
2π
 ( max
{u}×[0,2π] ̃θn − min
{u}×[0,2π] ̃θn
) ≤ L′

for any u ∈ (q, 1).
Let ∂D′
a be the curve ∂Da rescaled by the flow ϕdθ defined below so that A(∂D′
a) = π.
For u ∈ (q, 1), put Cu := φ(∂Du) and let C′
u be the curve rescaled by the flow ϕdθ so that
A(C′
u) = π. By Lemma 5.3 below, for a sequence (ai)i of real numbers in (q, 1) converging
to q from above, the sequence of constructible sheaves (FC′
ai )i is Cauchy.
We see that the limit object F ′ of (FC′
ai )i is isomorphic to F∂D′
a as follows. By the
microsupport estimate for the limit object, the microsupport of F ′ coincides with that
of F∂D′
a since φn is smooth also at the boundaries. By taking a compactly supported
Hamiltonian diffeomorphism sending ∂D′
a to C0 and applying the corresponding GKS
kernel to F∂D′
a and F ′, the assertion F∂D′
a ≃ F ′ follows from Lemma 3.5. Similarly, for
a sequence (ai)i of real numbers in (q, 1) converging to 1 from below, the sequence of
constructible sheaves (FC′
ai )i is Cauchy and converges to FCn.

21

Again by Lemma 5.3, for any q < u0 < u1 < 1,

d(FC′
u0 , FC′
u1 ) ≤ 2(L
′ + 1)(A(Cu1) − A(Cu0)) ≤ 2(L
′ + 1)π(1 − a
2).

By tanking limits, we obtain

d(F∂D′
a, FCn) ≤ 2(L
′ + 1)π(1 − a
2).

Hence, for m, n ≥ N , we have

d(FCn, FCm) ≤ 4(L′ + 1)π(1 − a
2),

which proves that (FCn)n is a Cauchy sequence. Since each FCn is limit constructible, a
limit object F is also limit constructible.

(b) Let us prove the second assertion and suppose that C = ϕ(S1) for some Hamiltonian
homeomorphism with compact support ϕ. Then there exists a sequence of Hamiltonian
diffeomorphisms (ϕn)n that converges to ϕ in the C0-sense. The sequence (K(ϕn×ϕn)FC0)n
is a Cauchy sequence, and its limit object is K(ϕ × ϕ)FC0 by definition. Then the sequence
(Fk)k with
 Fk =
 {
FCn (k = 2n − 1),
K(ϕn × ϕn)FC0 (k = 2n)

is also a Cauchy sequence. Since each pair of the limit objects of the three sequences
(FCn)n, (K(ϕn ×ϕn)FC0)n, and (Fk)k has distance zero, we conclude that F ≃ K(ϕ×ϕ)FC0
by the limit constructibility and Proposition 2.4.

We fix some notation. Let g be the standard metric on C and set ω := dλ = dξ ∧ dx be
the symplectic form on C ≃ T ∗Rx. We have ω(X, Y ) = g(X, √−1Y ). Let r, θ : C\{0} → R
be the radius and the (locally defined) argument. We remark that dθ(X) = − 1
r dr(
√−1X),
for all X. For a smooth function f (locally defined) on C, we let ∇f be the gradient vector
field with respect to g and Xf the Hamiltonian vector field. For a 1-form α (locally
defined) on C, we let Xα be the symplectic vector field with respect to ω. We have
g(∇f , X) = df (X), ω(Xα, X) = −α(X), for all X. We write ϕα for the symplectic isotopy
generated by Xα. We obtain

ω(Xdθ, X) = −dθ(X) = 1
r dr(
√−1X) = 1
r g(∇r, √−1X) = 1
r ω(∇r, X)

and thus Xdθ = 1
r ∇r. We deduce an expression of the symplectic isotopy ϕdθ
s in the
coordinates (r, θ): ϕdθ
s (r, θ) = (√
2s + r2, θ).

Lemma 5.2. Let φ : Aq → C be a biholomorphism onto its image A. Assume that φ
admits a continuous extension φ : Aq → A and 0 /∈ A. Let ˜θ : [q, 1] × [0, 2π] → R be a lift

of [q, 1] × [0, 2π] φ
−→ Aq → A θ
−→ R/2πZ. Then, there exists a positive real number L ∈ R>0
such that 1
2π
 ( max
{u}×[0,2π] ˜θ − min
{u}×[0,2π] ˜θ) ≤ L

for any u ∈ [q, 1]. This L can be chosen so that

L ≤ 1
2π max { max
{q}×[0,2π] ˜θ − min
{q}×[0,2π] ˜θ, max
{1}×[0,2π] ˜θ − min
{1}×[0,2π] ˜θ} + 1.

22

Proof. By abuse of notation, we write θ for (q, 1) × [0, 2π] → Aq θ
−→ R. Let θ′ : (q, 1) ×
[0, 2π] → R denote the second projection. Then the function ˜θ − θ′ defines a harmonic
function on Aq. Let Iu ⊂ R be the image of ∂Du under ˜θ − θ′. We may assume Iq ⊂ I1 or
I1 ⊂ Iq by adding a harmonic function of the form c log r (c ∈ R) if necessary. Note that
this does not change the length of each Iu.
By the maximum principal, Iu is contained in Iq ∪I1. Since the values of θ′ is contained
in [0, 2π], the oscillation is less than or equal to max{|Iq|, |I1|} + 2π, where |I| denotes the
length of a interval I ⊂ R.

The essential part of the proof of the following lemma is due to St´ephane Guillermou.

Lemma 5.3. Let φ : Aq → C be a biholomorphism onto its image A and let L be a positive
real number satisfying the inequality in Lemma 5.2. For u ∈ (q, 1), set Cu := φ(∂Du) and
assume A(Cu) ≤ π for all u ∈ (q, 1). Define C′
u to be the curve rescaled by ϕdθ defined
above such that A(C′
u) = π. Then, for q < u0 < u1 < 1, one has

d(FC′
u0 , FC′
u1 ) ≤ 2(L + 1)(A(Cu1) − A(Cu0))

after translating FC′
u0 by some constant to the Rt/πZ-direction.

Proof. We may assume that 0 ∈ C is contained in the open domain bounded by Cu for all
u ∈ (q, 1). We set r′ = r ◦ φ−1, θ′ = θ ◦ φ−1 : A → Rx. Hence Cu = r′−1(u). Since φ is
biholomorphic, we obtain Xdθ′ = 1
r′ ∇r′.
In the following steps from (a) to (d), we will construct a Hamiltonian diffeomorphism
that sends C′
u0 to C′
u1 and estimate the distance d(FC′
u0 , FC′
u1 ) with the Hamiltonian
diffeomorphism.
(a) First we will define a time-dependent closed 1-form α = (α(s))s∈[0,u1−u0] on A such
that the flow of its symplectic vector field ϕα satisfies ϕα
s (Cu0) = Cu0+s for s ∈ [0, u1 − u0].
This condition is satisfied if dr′(Xα(s)) = 1 on Cu0+s for s ∈ [0, u1 − u0]. We define a
function k that depends only on s and θ′ by

k(s, θ′) := u0 + s
∥dr′∥2 ,

where ∥dr′∥2 is a time-dependent function on A that maps (r′
1, θ′
1) to the value of ∥dr′∥2

at (u0 + s, θ′
1). We define α(s) := k(s, θ′)dθ′.

Then, on Cu0+s we have Xα(s) = k(s, θ′)Xdθ′,

which implies dr′(Xα(s)) = 1. Moreover, we have dθ′(Xα(s)) = 0 by construction.
(b) Next, we will describe the rescaled curve C′
u more precisely. We have seen that
ϕdθ
s (∂Du) = ∂D√2s+u2. Hence A(ϕdθ
s (∂Du)) = A(∂Du) + 2πs. Now, for a general Jordan
curve C containing 0 in its interior domain and ε > 0 small, ϕdθ
s is defined and symplectic
outside Dε. Hence we deduce the general equality

A(ϕdθ
s (C)) = A(C) + 2πs.

Thus, we can write
 C′
u = ϕdθ
T (u)(Cu) with T (u) := 1
2π (π − A(Cu)).

23

(c) We will construct a Hamiltonian diffeomorphism that sends C′
u0 to C′
u1. We define
a symplectomorphism ψ := ϕdθ
T (u0) and a time-dependent closed 1-form β by β(s) :=
(ψ−1)∗α(s). We set a(s) = A(Cs) and define time-dependent function and 1-form

b(s) := − 1
2π da
ds (u0 + s), dΘ(s) = b(s)dθ (s ∈ [0, u1 − u0]).

Since ∫ s

0 b(s
′) ds′ = 1
2π (a(u0) − a(u0 + s)) = T (u0 + s) − T (u0),

we obtain ϕdΘ
s = ϕdθ
T (u0+s)−T (u0). For s ∈ [0, u1 − u0], we define

(dΘ♯β)(s) := dΘ(s) + ((ϕdΘ
s )
−1)∗β(s) = dΘ(s) + ((ϕdθ
T (u0+s)−T (u0))−1)
∗α(s),

which is a locally defined time-dependent closed 1-form. We find that

ϕdΘ♯β
s = ϕdΘ
s ◦ ϕβ
s
= ϕdθ
T (u0+s)−T (u0) ◦ ψ ◦ ϕα
s ◦ ψ−1

= ϕdθ
T (u0+s) ◦ ϕα
s ◦ (ϕdθ
T (u0))
−1,

which sends C′
u0 to C′
u0+s. The exactness of a locally defined closed 1-form is determined by
the integrations along closed curves that generate the first homology group of the domain.
Since A(C′
u0+s) = A(C′
u0), the integration of (dΘ♯β)(s) along C′
u0+s is zero. Thus dΘ♯β is
a time-dependent locally defined exact 1-form, which can be written as dh1. This proves
that ϕdΘ♯β
u1−u0 is the Hamiltonian diffeomorphism ϕh1
u1−u0 that sends C′
u0 to C′
u1.
(d) Finally, we will estimate the Hofer norm of ϕh1
u1−u0. We take a smooth cut-off function
on C and extend h1 to C with the cut-off function.
For any z1, z2 ∈ C′
u0+s, we take a path in C′
u0+s connecting these two points that does
not pass θ′ = 0. Then, by integrating dΘ♯β along the path, we get

h1(s, z1) − h1(s, z2) ≤ 1
2π |b(s)| ( max
{u0+s}×[0,2π] ˜θ − min
{u0+s}×[0,2π] ˜θ) + ∫ θ′
2

θ′
1 k(s, θ′) dθ′,

where (u0+s, θ′
i) in the coordinates (r′, θ′) corresponds to the point zi for i = 1, 2. The area
bounded by the arcs θ′ is constant or r′ is constant joining the points (u0, θ′
i), (u0 + s, θ′
i)
for i = 1, 2 is written as

B(s, θ′
1, θ′
2) = ∫ r′=u0+s

r′=u0
 ∫ θ′=θ′
2

θ′=θ′
1 ω(∂r′, ∂θ′) dθ′dr′.

By using ω(∂r′, ∂θ′) = ω (kXdθ′, ∂θ′) = k, we have

∂B
∂s (s, θ′
1, θ′
2) = ∫ θ′=θ′
2

θ′=θ′
1 ω(∂r′, ∂θ′) dθ′ = ∫ θ′=θ′
2

θ′=θ′
1 k(s, θ′) dθ′.

Since k(s, θ′) ≥ 0 and B(s, 0, 2π) = a(s) − a(u0), we obtain the bound
∫ θ′
2

θ′
1 k(s, θ′) dθ′ ≤ da
ds (s) for any s and θ′
1, θ′
2.

Combining this inequality with Lemma 5.2, we have

h1(s, z1) − h1(s, z2) ≤ (L + 1) da
ds (u0 + s)

24

Hence, we obtain

∫ u1−u0

0
 (
 max
C′
u0+s h1(s) − min
C′
u0+s h1(s)

)
 ds ≤ (L + 1)(a(u1) − a(u0)).

The bound is equal to (L + 1)(A(Cu1) − A(Cu0)).
We will finish the proof of the lemma. The time-depending function (p, p′) ↦→ h1(p, s)+
h1(p′, s) on C × C generates a flow that sends C′
u0 × C′
u0 to C′
u1 × C′
u1 at time s = u1 − u0.
Hence, by [AI24, Thm. A.2], there exists c ∈ R such that

d(FC′
u0 , TcFC′
u1 ) ≤ 2 ∫ u1−u0

0
 (
 max
C′
u0+s h1(s) − min
C′
u0+s h1(s)

)
 ds

≤ 2(L + 1)(A(Cu1) − A(Cu0)).

This completes the proof.

Remark 5.4. Note that we can define a sheaf quantization FC for any Jordan curve C
by Proposition 5.1.

Remark 5.5. Note that there are Jordan curves whose images have positive measure
[Leb03; Osg03]. See also [NV22]. If the measure of C is non-zero, C inscribes a θ-rectangle
for any θ ∈ (0, π) by Lebesgue’s density theorem.

Now we prove Theorem 1.1.

Proof of Theorem 1.1. We may assume that the measure of C is zero by Remark 5.5. By
scaling, we may also assume that the area of the open domain bounded by C is π, that is,
A(C) = π. Let (cn)n be a sequence of smooth Jordan curves that satisfies the conditions
in Theorem 1.1. Let Bn := A(Cn) be the area of the open domain bounded by Cn. Since
Bn → π as n → ∞, by scaling Cn by a factor of √
π/Bn with respect to the origin, we may
assume Bn = π while keeping (cn)n converges to c. By the first part of Proposition 5.1,
the sequence of sheaf quantizations (FCn)n is a Cauchy sequence, which defines a limit
object F . Combining the condition (2) in Theorem 1.1 with Proposition 2.3, we find that
Ta SS(F ) ∩ SS(F ) = ∅ for a ∈ R \ πZ.
Since the measure of C is zero, we can construct a Hamiltonian homeomorphism
with compact support ϕ on T ∗R such that C = ϕ(C0). Note that the set of com-
pactly supported Hamiltonian homeomorphism coincides with the set of compactly sup-
ported area-preserving homeomorphisms, whose proof can be found in [Oh06; Sik07].
Such a compactly supported area-preserving homeomorphisms exists by theorems by
Sch¨onflies and Oxtoby–Ulam [OU41]. Then, by the second part of Proposition 5.1, we
have F ≃ FC := K(ϕ × ϕ)FC0.
Hence, the result follows from Theorem 4.1.

Remark 5.6. The smooth approximation assumed in Theorem 1.1 can be weakened to
an approximation by C1-curves. Furthermore, the “primitive” for curves satisfying the
assumptions of Theorem 1.1 is unique regardless of how the approximating sequence is
chosen. This uniqueness follows from the fact that the sheaf quantization is unique and
the primitive can be recovered from its conic microsupport.
It follows the following observation. Let (cn : S1 → R2)n be a sequence of continuous
Jordan curves with

(1) (cn) converges to a Jordan curve c in the C0-sense,

25

(2) each cn satisfies the assumption of Theorem 1.1 and hence “primitive” fn is deter-
mined up to constant.

(3) (fn)n converges to a continuous function f uniformly on every compact subset.

Then the Jordan curve c satisfies the assumptions of Theorem 4.1.

Remark 5.7. As mentioned in Remark 5.5, a Jordan curve with positive measure inscribes
a θ-rectangle for any θ ∈ (0, π). Thus, the rectangular peg problem for any Jordan curve
would be solved affirmatively if the cohomology vanishing in Remark 4.2 for Jordan curves
with measure zero.

5.2 Rectifiable curves

Now we give an affirmative answer to the rectangle peg problem for rectifiable curves.

Proposition 5.8. A rectifiable Jordan curve C satisfies the assumptions in Theorem 1.1.

Proof. Let D be the open domain bounded by C. By the Riemann mapping theorem
and the Carath´eodory theorem, we can construct a homeomorphism φ : D1 → D whose
restriction to D1 is a holomorphic mapping. For n ∈ Z≥2, we define a smooth Jordan
curve cn := φ|∂D1−1/n. By the Riesz–Privalov theorem, a precise form of the Riemann
mapping theorem for a domain with rectifiable boundary [Pom92, Thm. 6.8], we find that
the lengths of cn converge to the length of c. Then, by the lemmas for proving Green’s
theorem for rectifiable curves [Apo57, 10–14]3, we find that the sequence of smooth Jordan
curve (cn)n satisfies the conditions in Theorem 1.1.

Corollary 5.9. Every rectifiable Jordan curve inscribes a θ-rectangle for any θ ∈ (0, π).

5.3 Locally monotone curves

Stromquist [Str89] proved the existence of an inscribed square for a large class of Jordan
curves, which he called locally monotone. We will also extend his result with the use of
Theorem 1.1.
Let us first recall the definition of locally monotone curves. Through the identification
S1 ≃ R/2πZ, we regard a Jordan curve c : S1 → R2 as a 2π-periodic map c : R → R2.

Definition 5.10 ([Str89, §6]). A Jordan curve c : S1 → R2 is said to be locally monotone
if for any p ∈ R, there exist an open connected neighborhood Up ⊂ R of p and a unit
vector ⃗v(p) such that the inner product q ↦→ c(q) · ⃗v(p) is a strictly monotone function on
Up.

Proposition 5.11. A locally monotone Jordan curve C satisfies the assumptions in The-
orem 1.1.

Proof. Let p ∈ R and define gp(q) := c(q) · ⃗v(p), a strictly monotone function on Up. We
define a function fp on Up as follows:

fp(q) := ∫ gp(q)

gp(p) c(g−1
p (q′)) · ⃗n(p) dq′ + hp(c(q)) (q ∈ Up),

where

3Note that this discussion is only written in the first edition and has been removed from the second
edition onward. An overview of the discussion can also be found on Wikipedia [Wik].

26

• ⃗n(p) is a unit vector orthogonal to ⃗v(p) such that (⃗v(p), ⃗n(p)) forms an oriented basis
of R2;

• (xp, ξp) is the coordinate function with respect to the orthonormal basis (⃗v(p), ⃗n(p));
and

• hp : R2 → R is a smooth primitive function of ξdx − ξpdxp.

After choosing appropriate constant shifts, we can glue the family of local functions
(fp : Up → R)p∈R to get a continuous function f on R. Note that a smooth Jordan
curve c is locally monotone, and in this case f constructed above is a primitive function
of c∗λ = c∗(ξdx).
We fix a non-negative smooth function χ ∈ C∞(R) supported on [−1, 1] such that∫
R χ(q) dq = 1. For n ∈ Z≥1, we take δn > 0 such that |p − p′| < δn implies ∥c(p) − c(p′)∥ <
1/n and define
 cn(p) := ∫

R δ−1
n χ(δ−1
n u) c(p − u)du

for p ∈ R. Then cn satisfies ∥c(p) − cn(p)∥ < 1/n for any p ∈ R and is a smooth Jordan
curve for a sufficiently large n. In particular, the sequence (cn)n converges to c in the
C0-sense.
We can check from argument in Stromquist [Str89] that the sequence of primitives for
cn’s converges to f . Indeed, by shrinking Up if necessary, gn,p(q) := cn(q) · ⃗v(p) is strictly
monotone on Up and the functions cn(g−1
n,p(-)) · ⃗n(p) defined on a neighborhood of gp(p)
converge to c(g−1
p (-)) · ⃗n(p) in the C0-sense.

Corollary 5.12. Every locally monotone Jordan curve inscribes a θ-rectangle for any
θ ∈ (0, π).

Acknowledgments

During the preparation of this paper, we learned that St´ephane Guillermou had proved a
result similar to Theorem 1.1. We are grateful to him for generously sharing his insights
with us. His ideas have clarified our discussions and improved our results. We thank
Tatsuya Miura for letting us know the square peg problem many years ago and the helpful
discussions about Jordan curves. We also thank Vincent Humili`ere for discussions about
Jordan curves, Kaoru Ono for helpful comments related to Remark 3.6, and Takuya Mu-
rayama for some references about conformal mappings. We are grateful to Joshua Evan
Greene and Andrew Lobb for pointing out an error in the earlier version. TA is partially
supported by JSPS KAKENHI Grant Number JP24K16920. YI is partially supported
by JSPS KAKENHI Grant Numbers JP21K13801 and JP22H05107. We are partially
supported by JST, CREST Grant Number JPMJCR24Q1, Japan.

References

[Apo57] T. M. Apostol. Mathematical analysis: a modern approach to advanced calcu-
lus. Addison-Wesley Publishing Co., Inc., Reading, MA, 1957, pp. xii+553.

[AI20] T. Asano and Y. Ike. “Persistence-like distance on Tamarkin’s category and
symplectic displacement energy”. J. Symplectic Geom. 18.3 (2020), pp. 613–
649.
 27

[AI23] T. Asano and Y. Ike. “Sheaf quantization and intersection of rational La-
grangian immersions”. Annales de l’Institut Fourier 73.4 (2023), pp. 1533–
1587.

[AI24] T. Asano and Y. Ike. “Completeness of derived interleaving distances and
sheaf quantization of non-smooth objects”. Mathematische Annalen 390 (2024),
pp. 2991–3037.

[CKNS24] L. Cˆot´e, C. Kuo, D. Nadler, and V. Shende. The microlocal Riemann-Hilbert
correspondence for complex contact manifolds. 2024. arXiv: 2406.16222 [math.SG].

[Emc16] A. Emch. “On Some Properties of the Medians of Closed Continuous Curves
Formed by Analytic Arcs”. Amer. J. Math. 38.1 (1916), pp. 6–18.

[FG23] P. Feller and M. Golla. “Non-orientable slice surfaces and inscribed rectan-
gles”. Ann. Sc. Norm. Super. Pisa Cl. Sci. (5) 24.3 (2023), pp. 1463–1485.

[FOOO09] K. Fukaya, Y.-G. Oh, H. Ohta, and K. Ono. Lagrangian intersection Floer the-
ory: anomaly and obstruction. Part I. Vol. 46. AMS/IP Studies in Advanced
Mathematics. American Mathematical Society, Providence, RI; International
Press, Somerville, MA, 2009, pp. xii+396.

[GPS24] S. Ganatra, J. Pardon, and V. Shende. “Microlocal Morse theory of wrapped
Fukaya categories”. Ann. of Math. (2) 199.3 (2024), pp. 943–1042.

[Gao24] Z. Gao. Generic doubling of rectangular pegs. 2024. arXiv: 2404.13209 [math.SG].

[GM05] J. B. Garnett and D. E. Marshall. Harmonic measure. Vol. 2. New Mathemat-
ical Monographs. Cambridge University Press, Cambridge, 2005, pp. xvi+571.

[GL21] J. E. Greene and A. Lobb. “The rectangular peg problem”. Ann. of Math.
(2) 194.2 (2021), pp. 509–517.

[GL23] J. E. Greene and A. Lobb. “Cyclic quadrilaterals and smooth Jordan curves”.
Invent. Math. 234.3 (2023), pp. 931–935.

[GL24a] J. E. Greene and A. Lobb. Floer homology and square pegs. 2024. arXiv:
2404.05179 [math.SG].

[GL24b] J. E. Greene and A. Lobb. Polynomial Inscriptions. 2024. arXiv: 2412.09546
[math.SG].

[GL24c] J. E. Greene and A. Lobb. Square pegs between two graphs. 2024. arXiv:
2407.07798 [math.SG].

[Gui12] S. Guillermou. Quantization of conic Lagrangian submanifolds of cotangent
bundles. 2012. arXiv: 1212.5818v2 [math.SG].

[Gui23] S. Guillermou. “Sheaves and symplectic geometry of cotangent bundles”.
Ast´erisque 440 (2023), pp. x+274.

[GKS12] S. Guillermou, M. Kashiwara, and P. Schapira. “Sheaf quantization of Hamil-
tonian isotopies and applications to nondisplaceability problems”. Duke Math.
J. 161.2 (2012), pp. 201–245.

[GV24] S. Guillermou and C. Viterbo. “The singular support of sheaves is γ-coisotropic”.
Geom. Funct. Anal. 34.4 (2024), pp. 1052–1113.

[Hug18] C. Hugelmeyer. Every smooth Jordan curve has an inscribed rectangle with
aspect ratio equal to √
3. 2018. arXiv: 1803.07417 [math.MG].

[Hug21] C. Hugelmeyer. “Inscribed rectangles in a smooth Jordan curve attain at least
one third of all aspect ratios”. Ann. of Math. (2) 194.2 (2021), pp. 497–508.

28

[Hug24] C. Hugelmeyer. A Solution to the Periodic Square Peg Problem. 2024. arXiv:
2407.20412 [math.SG].

[Ike19] Y. Ike. “Compact exact Lagrangian intersections in cotangent bundles via
sheaf quantization”. Publ. Res. Inst. Math. Sci. 55.4 (2019), pp. 737–778.

[IK23] Y. Ike and T. Kuwagaki. Microlocal categories over Novikov rings. 2023.
arXiv: 2307.01561 [math.SG].

[Jin20] X. Jin. Microlocal sheaf categories and the J-homomorphism. 2020. arXiv:
2004.14270 [math.SG].

[JT17] X. Jin and D. Treumann. Brane structures in microlocal sheaf theory. 2017.

[Kas89] M. Kashiwara. “Representation theory and D-modules on flag varieties”.
Ast´erisque 173-174 (1989). Orbites unipotentes et repr´esentations, III, pp. 9,
55–109.

[KS90] M. Kashiwara and P. Schapira. Sheaves on manifolds. Vol. 292. Grundlehren
der Mathematischen Wissenschaften. Springer-Verlag, Berlin, 1990, pp. x+512.

[KS18] M. Kashiwara and P. Schapira. “Persistent homology and microlocal sheaf
theory”. Journal of Applied and Computational Topology 2.1-2 (2018), pp. 83–
113.

[Kuo23] C. Kuo. “Wrapped sheaves”. Adv. Math. 415 (2023), Paper No. 108882, 71.

[KL22] C. Kuo and W. Li. Spherical adjunction and Serre functor from microlocal-
ization. 2022. arXiv: 2210.06643 [math.SG].

[KSZ23] C. Kuo, V. Shende, and B. Zhang. On the Hochschild cohomology of Tamarkin
categories. 2023. arXiv: 2312.11447 [math.SG].

[Leb03] H. Lebesgue. “Sur le probl`eme des aires”. Bull. Soc. Math. France 31 (1903),
pp. 197–203.

[Mat14] B. Matschke. “A survey on the square peg problem”. Notices Amer. Math.
Soc. 61.4 (2014), pp. 346–352.

[Mey81] M. D. Meyerson. “Balancing acts”. Topology Proc. 6.1 (1981), pp. 59–75.

[NS20] D. Nadler and V. Shende. Sheaf quantization in Weinstein symplectic mani-
folds. 2020. arXiv: 2007.10154 [math.SG].

[NV22] M. C. Nasso and A. Volˇciˇc. “Area-filling curves”. Arch. Math. (Basel) 118.5
(2022), pp. 485–495.

[Oh06] Y.-G. Oh. C0-coerciveness of Moser’s problem and smoothing area preserving
homeomorphisms. 2006. arXiv: math/0601183 [math.DS].

[Osg03] W. F. Osgood. “A Jordan curve of positive area”. Trans. Amer. Math. Soc.
4.1 (1903), pp. 107–112.

[OU41] J. C. Oxtoby and S. M. Ulam. “Measure-preserving homeomorphisms and
metrical transitivity”. Ann. of Math. (2) 42 (1941), pp. 874–920.

[Pom92] C. Pommerenke. Boundary behaviour of conformal maps. Vol. 299. Grundlehren
der mathematischen Wissenschaften [Fundamental Principles of Mathemati-
cal Sciences]. Springer-Verlag, Berlin, 1992, pp. x+300.

[Sch44] L. G. Schnirelman. “On certain geometrical properties of closed curves”. Us-
pehi Matem. Nauk 10 (1944), pp. 34–44.

29

[Sei00] P. Seidel. “Graded Lagrangian submanifolds”. Bull. Soc. Math. France 128.1
(2000), pp. 103–149.

[Sey12] S. Seyfaddini. “Descent and C0-rigidity of spectral invariants on monotone
symplectic manifolds”. Journal of Topology and Analysis 4.04 (2012), pp. 481–
498.

[STZ17] V. Shende, D. Treumann, and E. Zaslow. “Legendrian knots and constructible
sheaves”. Invent. Math. 207.3 (2017), pp. 1031–1133.

[Sik07] J.-C. Sikorav. Approximation of a volume-preserving homeomorphism by a
volume-preserving diffeomorphism. Accessed on December 25, 2024. 2007.
url: https : / / perso . ens - lyon . fr / jean - claude . sikorav / textes /
2007volume%20preserving%20approximation.pdf.

[Str89] W. Stromquist. “Inscribed squares and square-like quadrilaterals in closed
curves”. Mathematika 36.2 (1989), pp. 187–197.

[Tao17] T. Tao. “An integration approach to the Toeplitz square peg problem”. Forum
of Mathematics, Sigma 5 (2017), e30.

[Toe11] O. Toeplitz. “ ¨Uber einige aufgaben der analysis situs”. erhandlungen der
Schweizerischen Naturforschenden Gesellschaft in Solothurn 4.197 (1911).

[Vol25] M. Volpe. “The six operations in topology”. J. Topol. 18.4 (2025), Paper No.
e70050.

[Wik] Wikipedia authors. Green’s theorem. Accessed on December 25, 2024. url:
https://en.wikipedia.org/wiki/Green%27s_theorem.

Tomohiro Asano: Department of Mathematics, Kyoto University, Kitashirakawa-Oiwake-
Cho, Sakyo-ku, 606-8502, Kyoto, Japan.
E-mail address: tasano[at]math.kyoto-u.ac.jp, tomoh.asano[at]gmail.com

Yuichi Ike: Graduate School of Mathematical Sciences, The University of Tokyo, 3-8-1
Komaba Meguro-ku Tokyo 153-8914, Japan.
E-mail address: ike[at]ms.u-tokyo.ac.jp, yuichi.ike.1990[at]gmail.com

30
