<!-- source: https://arxiv.org/pdf/2510.01746 | converted from PDF -->

C0-RIGIDITY OF LEGENDRIANS AND COISOTROPICS VIA SHEAF
QUANTIZATION

TOMOHIRO ASANO, YUICHI IKE, CHRISTOPHER KUO, AND WENYUAN LI

Abstract. We prove that in the standard cosphere bundle, for any contact homeomorphism in
the closure of the compactly supported contactomorphism group, when the image of a coisotropic
submanifold (not necessarily properly embedded) is smooth, it is still coisotropic. Moreover, when
contactomorphisms in the sequence are in the identity component and the image of a Legendrian
is smooth, the Maslov data is preserved, and the category of sheaves with singular support on
the Legendrian and the microstalk corepresentative are also preserved (and thus so is the wrapped
Floer cochains of the linking disks). The main ingredients are the result of Guillermou–Viterbo,
a new sheaf quantization result for C 0-small contactomorphisms (not necessarily in the identity
component) different from Guillermou–Kashiwara–Schapira, and continuity of the interleaving dis-
tance of sheaves with respect to the Hofer–Shelukhin distance and the C 0-distance. The appendix
contains different arguments for local C 0-limits and certain Hausdorff limits of Legendrians without
appealing to the interleaving distance.
 Contents

1. Introduction 1
1.1. Context and background 1
1.2. Main results and applications 2
Acknowledgement 7
2. Completeness of Sheaves 7
2.1. Sheaves and singular supports 7
2.2. Microlocalization and microsheaves 11
2.3. Interleaving distance and completeness of sheaves 12
3. Hofer–Shelukhin Distances and Sheaves 17
3.1. Hofer–Shelukhin norm and interleaving distance 17
3.2. Non-degeneracy of the (Chekanov–)Hofer–Shelukhin distance 20
4. C0-Distances and Sheaves 23
4.1. Sheaf quantization of contact homeomorphisms in jet bundles 23
4.2. Sheaf quantization of nearby Legendrians with no chords 25
4.3. Sheaf quantization of C0-small contactomorphisms 28
4.4. Sheaf quantization of contact homeomorphisms 31
Appendix A. Local C0-/Hausdorff-Rigidity without Interleaving Distance 36
References 41

1. Introduction

1.1. Context and background. Our objective in this paper is to show the rigidity of contact
topology and dynamics in cosphere bundles of a manifold under the C0-topology using microlocal
theory of sheaves. Using the sheaf-theoretic interleaving distance, we prove a number of new rigidity
results on Legendrian submanifolds. 1arXiv:2510.01746v1  [math.SG]  2 Oct 2025
2 TOMOHIRO ASANO, YUICHI IKE, CHRISTOPHER KUO, AND WENYUAN LI

One of the central topics in symplectic and contact topology is to understand the dichotomy
between flexibility and rigidity. Gromov [35] and Eliashberg [31] showed that for a symplectic man-
ifold, the symplectomorphism group is closed in the diffeomorphism group under the C0-topology
(see also [42]), which initiates the study of C0-symplectic topology. Since then, people have proved
various results on the rigidity of Lagrangians and coisotropics under symplectic homeomorphisms
[54, 44].
Following the idea of Gromov and Eliashberg, M¨uller–Spaeth showed that the contactomorphism
group is also closed in the diffeomorphism group under the C0-topology [60], so we can define con-
tact homeomorphisms as C0-limits of contactomorphisms accordingly. While contactomorphisms
always lift to symplectomorphisms of the symplectizations, it is not true that the C0-convergence of
contactomorphisms will imply C0-convergence of the corresponding symplectomorphisms, making
the studies of C0-contact topology more subtle [85]. For the rigidity of Legendrians, Dimitroglou
Rizell–Sullivan [22, 23], after series of previous works by others [73, 85, 67, 82], showed that the
image of properly embedded Legendrians under contact homeomorphisms (that arise as limits of
contactomorphisms supported in a given compact subset), if smooth, are still Legendrians. How-
ever, the coisotropic rigidity is only known assuming uniform lower bounds on the conformal factor
by Usher [85], after [73]. On the contrary, on the flexbility side, it is also known that any smooth
manifold with correct dimension can be C0 approximated by embedded Legendrians [21, 62].
The studies of C0-behavior in symplectic and contact geometry are closely related to many other
topics in symplectic and contact geometry. As suggested by Buhovsky–Opshtein [14], one natural
perspective to study the nearby Lagrangian conjecture is to study the problem through the action
of symplectic homeomorphisms in a Weinstein neighborhood (see also the recent work [10]). This
naturally generalizes to the setting of Legendrians (we know closed Legendrians in 1-jet bundles
are not unique even within the same formal Legendrian embedding class, and thus the contact
homeomorphism assumption becomes necessary in the Legendrian case).
Our approach is to understand the rigidity in C0-contact topology using microlocal theory of
sheaves, developed by Kashiwara–Schapira [48]. Sheaf-theoretic techniques have been used in
symplectic geometry since the work of Nadler–Zaslow [66, 63] and Tamarkin [84], and was used
by Guillermou to give a new proof of the Eliashberg–Gromov theorem [38, 37]. More recently,
Guillermou–Viterbo and the first two authors demonstrate the strength of microlocal theory of
sheaves in C0-symplectic topology [40, 3, 6].
The results mentioned above cannot be directly applied to C0-contact topology. In this paper,
we will show some persistence distance estimations with respect to the Hofer–Shelukhin distance
and the C0-distance. For the estimation with respect to the C0-distance, we will need to prove a
new sheaf quantization construction for any C0-small contactomorphism (potentially not compactly
supported nor in the identity component) that is different from Guillermou–Kashiwara–Schapira
[39]. These results together with the previous ones [40, 3] will allow us to deduce new C0-rigidity
results of Legendrians and more generally coisotropics.

1.2. Main results and applications. Let (Y, ξ) be a co-oriented contact manifold, where ξ is
a co-oriented maximally non-integrable hyperplane distribution given by the kernel of a 1-form
α. A contactomorphism is a diffeomorphism φ : Y → Y such that φ∗ξ = ξ, in other words,
φ∗α = ehα for some smooth function h : Y → R. We call h the conformal factor of φ. We denote
the group of contactomorphisms by Cont(Y, ξ) and the path connected component of the identity
map be Cont0(Y, ξ). Fix a Riemannian metric on Y . We consider the uniform C0-norm on the
contactomorphism group dC0(φ, ψ) = supy∈Y d(φ(y), ψ(y)).
Our first result shows the rigidity of any (not necessarily properly embedded) Legendrian and
coisotropic submanifolds under contact homeomorphisms, in other words, C0-limits of contactomor-
phisms in the group of homeomorphisms. The rigidity result generalizes the result of Dimitroglou
Rizell–Sullivan [23] for properly embedded Legendrians after the works of [73, 85, 67, 82], and

C0-RIGIDITY OF LEGENDRIANS AND COISOTROPICS VIA SHEAF QUANTIZATION 3

Usher [85] for coisotropics assuming uniform lower bound of the conformal factors after [73].
1 As
the discussion on C0-geometry relies on a certain non-degeneracy result, precisely Theorem 2.37, we
will assume that the metric on S∗M is induced from a complete Riemannian metric with bounded
geometry (in particular, with positive injectivity radius).

Theorem 1.1. Let (S∗M, ξstd) be the cosphere bundle with the standard contact structure and C ⊆
S∗M be a locally closed (embedded) coisotropic. Consider contactomorphisms φn ∈ Cont(S∗M, ξstd)
each of which has bounded conformal factor hn. Suppose φn → φ∞ in the C0-topology and φ∞ is
a homeomorphism. If φ∞(C) is smooth, then φ∞(C) is also coisotropic.2

Remark 1.2. We require only that the conformal factor hn of each contactomorphism φn is
bounded by some (non-uniform) constant Cn. For example, this always holds when each φn is
supported in a compact subset Kn. Thus, for proper Legendrians, our theorem is also slightly
stronger than the result of Dimitroglou Rizell–Sullivan [23]. When φn are all supported in one
given compact subset and Λ is a properly embedded Legendrian, they showed that if φ∞(Λ) is
smooth then it is Legendrian [23]. To the best of our knowledge, the rigidity result was also not
known for non-properly embedded Legendrians in the literature.

Remark 1.3. Other than the argument we use in the main theorem, in Section A, we will provide
a straightforward argument independent of the main body of the paper (relying on only standard
sheaf theory techniques), which proves local C0-rigidity of Legendrians, that when φn are all equal
to the identity on a fixed open subset Ω and Λ ∩ Ω = ∅, then the result holds. The appendix will
also contain results on certain local rigidity of Hausdorff limits of Legendrians.

Our next result shows the rigidity of Maslov data of Legendrian submanifolds under contact
homeomorphisms. This is the natural Legendrian analogue of the result that nearby Lagrangians
have vanishing Maslov classes and some higher obstructions [49, 2, 37, 45].

Theorem 1.4. Let (S∗M, ξstd) be the cosphere bundle with the standard contact structure and Λ ⊆
S∗M be a locally closed (embedded) Legendrian. Consider contactomorphisms φn ∈ Cont0(S∗M, ξstd)
each of which has bounded conformal factor hn. Suppose φn → φ∞ in the C0-topology and φ∞ is
a homeomorphism. When φ∞(Λ) is smooth, the composition of Lagrangian Gauss map and the
delooping of J-homomorphism remains the same:

Λ
 U/O BPic(S)

φ∞(Λ)

φ∞

In particular, Λ and φ∞(Λ) have the same Maslov class and relative second Stiefel–Whitney classes.

Remark 1.5. When Λ is a Legendrian knot in a contact 3-manifold, Dimitroglou Rizell–Sullivan
showed that φ∞(Λ) has the same Maslov class (and in fact is contactomorphic to Λ). However, to
the best of our knowledge, the statements about Maslov classes in higher dimensions are not known.
While the Lagrangian analogue of the Maslov class results are known due to Abouzaid–Kragh [49,
2], Guillermou [36, 37], Jin [45] and Membrez–Opshtein [59], they do not imply the Legendrian
version of the results as we do not know whether the Legendrian has no short Reeb chords.

1For non-properly embedded Legendrians, our result is not compatible with the recent preprint [81].
2We say that a submanifold is coisotropic in a contact manifold (Y, ξ) if T C ∩ ξ is coisotropic in ξ, following Huang
[43], which is compatible with [73, 85]. This is different from the notion of regular coisotropic in [77].

4 TOMOHIRO ASANO, YUICHI IKE, CHRISTOPHER KUO, AND WENYUAN LI

One of the reasons that we can only show the above results for cosphere bundles is because we
do not know whether it is possible to cut off a contactomorphism in a tubular neighborhood of
a closed Legendrian without changing the C0-distance from the identity. However, in general, we
still conjecture the following:

Conjecture 1.6. Let Λ ⊆ (Y, ξ) be a Legendrian embedding. Consider contactomorphisms φn ∈
Cont0(Y, ξ) such that φn → φ∞ in the C0-topology and φ∞ is a homeomorphism. When φ∞(Λ) is
smooth, its Lagrangian Gauss map remains the same:

Λ
 U/O

φ∞(Λ)

φ∞

Our second result shows the rigidity of the category of sheaves with singular support on Leg-
endrian submanifolds in the cosphere bundle of a manifold M equipped with the natural contact
structure (S∗M, ξstd) under contact homeomorphisms when the conformal factors are uniformly
bounded. Using the result of Ganatra–Pardon–Shende [32], this implies the rigidity of the partially
wrapped Fukaya category. When further combining with the Legendrian surgery formula [12, 30,
28, 9], this implies the rigidity of the Legendrian contact homology. This is a natural Legendrian
analogue of the results that nearby Lagrangians define the same object as the zero section in the
sheaf category or Fukaya category [1, 63, 2, 37, 45, 8].

Theorem 1.7. Let (S∗M, ξstd) be the cosphere bundle with the standard contact structure and
Λ ⊆ S∗M be a proper Legendrian embedding. Consider contactomorphisms φn ∈ Cont0(Y, ξ) each
of which has bounded conformal factor hn. Suppose φn → φ∞ in the C0-topology and φ∞ is a
homeomorphism. Then there exists a functor

Kφ∞ : ShΛ(M ) → Shφ∞(Λ)(M ).

Furthermore, Kφ
−1
∞ is the inverse of Kφ∞ and it preserves microstalks. 3

Remark 1.8. By Ganatra–Pardon–Shende [32], we know that there is an equivalence between
sheaves on manifolds with singular supports and partially wrapped Fukaya categories of cotangent
bundles with stops (over a discrete ring)

ShΛ(M ) ≃ Mod W(T ∗M, Λ)op

which sends the corepresentatives of microstalk functors to the linking disks. Therefore, as our
equivalence preserves microstalks, we can conclude that there is a quasi-isomorphism between the
self wrapped Floer cochains of linking disks DΛ. Then, by the Legendrian surgery formula [30, 9],
we know they are isomorphic to Legendrian contact homologies

CW ∗(DΛ, DΛ) ≃ AC−∗(Ω∗Λ)(Λ).

Hence there is a quasi-equivalence between the Legendrian contact homologies with coefficients in
based loop spaces. Moreover, since microlocal rank corresponds to the rank of the representation
of Legendrian contact homologies, we know that there is an equivalence between augmentations of
Legendrian contact homologies (see also [69, 19]).

Remark 1.9. For contact 3-manifolds, it is shown by Dimitroglou Rizell–Sullivan [22] that for a
closed Legendrian Λ, when φ∞(Λ) is also smooth, there exists an ambient contactomorphism that
sends Λ to φ∞(Λ). In particular, this implies that they have quasi-isomorphic Legendrian contact
homology when it is defined. However, no such result is known in higher dimensions.

3The C 0-distance is equivalent to its two-sided counterpart ¯dC0 (φ, ψ) = supy∈Y d (φ(y), ψ(y)) +
supy∈Y d (
φ
−1(y), ψ−1(y)
)
, and thus if φ∞ is a contact homeomorphism, then φ
−1
∞ is a also a contact homeomorphism.

C0-RIGIDITY OF LEGENDRIANS AND COISOTROPICS VIA SHEAF QUANTIZATION 5

Consequently, we can strengthen the result of Dimitroglou Rizell–Sullivan [25] that the Legen-
drian contact homology of Λ is nontrivial if and only if the Legendrian contact homology of φ∞(Λ)
is nontrivial (since Kφ∞ sends non-local systems to non-local systems). For a loose Legendrian
Λ ⊆ S∗M in dimension at least 5 [62], the category of sheaves is trivial [79], and so is the Legen-
drian contact homology [29]. In particular, as we do not know any example of non-loose Legendrian
with trivial Legendrian contact homology or sheaf category in J 1Rn, our theorem excludes the pos-
sibility of any known example of non-loose Legendrian to be the C0-limit of a loose Legendrian.
We therefore conjecture the following:

Conjecture 1.10. Let Λ ⊆ S∗M be a proper loose Legendrian embedding. Consider contactomor-
phisms φn ∈ Cont0(S∗M, ξstd) such that φn → φ∞ in the C0-topology and φ∞ is a homeomorphism.
When φ∞(Λ) is also smooth, then φ∞(Λ) is still a loose Legendrian.

Other than the C0-topology on the group of contactomorphisms Cont(Y, ξ), there has also been
a number of studies on the topology on the identity component of the comtactomorphism group
Cont0(Y, ξ) induced by the Hofer–Shelukhin norm [78] with respect to a fixed contact form α. For
φ ∈ Cont0(Y, ξ), consider a path φt from id to φ. Then φt is induced by a contact Hamiltonian
H : Y × R → R. We then define the Hofer–Shelukhin norm to be

dHS,α(φ, ψ) = inf
φ=φH
1 ◦ψ ∥H∥HS,α = inf
φ=φH
1 ◦ψ
 ∫ 1

0 sup
y∈Y |H(y, t)| dt.

Since its universal cover, under the C1-topology, ̃Cont0(Y, ξ) can be realized as the group of ho-
motopy classes of contact isotopies, we also abuse notations and define dHS,α(φ, ψ) by considering
Hamiltonian isotopies in a fixed homotopy class of paths.
Similarly, for a Legendrian Λ ⊆ Y , on the space Leg0(Λ) of Legendrian submanifolds isotopic to
Λ, we can define the Chekanov–Hofer–Shelukhin distance to be

dCHS,α(Λ0, Λ1) = inf
Λ1=φH
1 (Λ0) ∥H∥CHS,Λ,α = inf
Λ1=φH
1 (Λ0)
 ∫ 1

0 sup
y∈φt
H (Λ) |H(y, t)| dt.

Then we can recover the following simple cases of non-degeneracy results of the (Chekanov–)Hofer–
Shelukhin distance in cosphere bundles (S∗M, ξstd). The Hofer–Shelukhin distance shares a closer
relation to the interleaving distance, as explained in Theorem 3.1. As a result, we do not need to
assume a complete Riemannian metric for this part of the discussion (we only need to assume that
the Reeb flow is well-defined).

Theorem 1.11. Let (S∗M, ξstd) be the cosphere bundle equipped with the standard contact struc-
ture. Then for any contact form α,
(1) (Shelukhin [78]) the Hofer–Shelukhin distance dHS,α defines a non-degenerate metric on the
space Cont0(S∗M, ξstd);
(2) (Dimitroglou Rizell–Sullivan [24]) when Λ ⊆ S∗M is a closed Legendrian such that ShΛ(M )
is non-trivial, the Chekanov–Hofer–Shelukhin distance dCHS,Λ,α defines a non-degenerate
metric on the space Leg0(Λ).

Remark 1.12. Rosen–Zhang [73] showed that the Chekanov–Hofer–Shelukhin distance is either
zero or non-degenerate. Therefore, we only need to show that the distance is not identically zero.
Dimitroglou Rizell–Sullivan [24] showed that the distance is non-degenerate on all closed contact
manifolds. On the contrary, Cant [18] and Nakamura [68] showed that there exist open contact
manifolds where the metric is zero. Similar to Dimitroglou Rizell–Sullivan [24], we expect that
there is also a sheaf-theoretic proof for the non-degeneracy of general closed Legendrians Λ ⊆ S∗M
by considering the doubling construction as in [37, 5]. However, there are nontrivial technical
difficulties one needs to overcome and we choose not to go into this direction in this paper.

6 TOMOHIRO ASANO, YUICHI IKE, CHRISTOPHER KUO, AND WENYUAN LI

We now explain the main techniques in the proof of the main theorems. To study the contact
topology under limits with respect to the C0-distance or Hofer–Shelukhin distance, we need to
construct limits of sheaves under such limits. On the category of sheaves, one can define an
interleaving pseudo-distance [47]. Guillermou–Viterbo [40] and the first two authors [3] recently
showed that the category of sheaves is complete with respect to the pseudo-metric.
For contact Hamiltonian isotopies on S∗M , there exist canonical sheaves in the product, known
as the sheaf quantizations of the contact isotopies by Guillermou–Kashiwara–Schapira [39]. We
can thus define a variant of the interleaving distance dτ on the product, depending on a positive
Hamiltonian τ on S∗M , which induces a distance on the contact isotopies that is right invariant
under contactomorphisms in the identity component (the conformal factor of contactomorphisms
accounts for the failure of the distance being bi-invariant).
Our first technical result is that the interleaving distance is continuous with respect to the Hofer–
Shelukhin distance. This generalizes the result of the first two authors for symplectic Hamiltonians
T ∗M or contact Hamiltonians in T ∗M × R [4].

Theorem 1.13. Let (S∗M, ξstd) be the cosphere bundle equipped with the standard contact structure
and φ ∈ ̃Cont0(S∗M, ξstd) be a homotopy class of contact isotopy. For Kφ ∈ Sh(M × M ) the time-1
GKS sheaf quantization of the contact isotopy, we have

dτ (1∆, Kφ) ≤ 2 dHS,α(id, φ).

Our next (and perhaps most) technical theorem is that the interleaving distance is continuous
with respect to the C0-distance. This turns out to be a very subtle theorem.
Since it is unknown whether a C0-small contactomorphism in the identity component is connected
to the identity through a C0-small isotopy, it is hard to work with the sheaf quantization of
contact isotopies by Guillermou–Kashiwara–Schapira and still get good control on the distance [39].
Therefore, we will prove a separate sheaf quantization theorem for C0-small contactomorphisms
based on Guillermou’s theorem on nearby Lagrangians [37] and then deduce the distance estimation.
Our argument is also very different from the symplectic analogue in [13].

Theorem 1.14. Let M be a complete Riemannian manifold, (S∗M, ξstd) be the cosphere bundle
equipped with the standard contact structure. Let α be a contact form whose Reeb flow is defined by
a positive Hamiltonian with positive lower bound and finite C1-norm. Then there exist ϵ > 0 and
Cα > 0 such that for a contactomorphism φ ∈ Cont(S∗M, ξstd) with dC0(id, φ) < ϵ, there exists a
canonical sheaf quantization Kφ ∈ Sh(M × M ) of φ such that

dτ (1∆, Kφ) ≤ 2Cα dC0(id, φ).

Remark 1.15. Related results to Theorem 1.13 on the continuity of spectral invariants with respect
to the Hofer–Shelukhin norm have been proved [26, 18]. One related result to Theorem 1.14 is the
local continuity of spectral invariants with respect to the C0-distance in W × S1 [76, Proposition
4.1]. We remark that we can similarly construct a discrete conjugation-invariant distance using
sheaf-theoretic spectral invariants as Sandon [75] (note that all conjugation-invariant distance on
Cont0(S∗M, ξstd) must be discrete [16]). We expect that this distance is also lower semi-continuous
with respect to the C0-distance [76, Proposition 1.10].

Considering sheaf quantizations of contactomorphisms in S∗M , the interleaving distance is right
invariant but only left invariant up to scaling by the conformal factor of the contactomorphism.
Therefore, we can construct sheaf quantizations for any contact homeomorphism in the identity
component using Theorem 1.14, but they are not compatible with compositions (and thus not
invertible) in general.
Finally, we mention that there have been other results in the sheaf theory literature that are
related to C0-contact topology as well. The full faithfulness theorem for nearby cycle functors of
Nadler–Shende [65, Theorem 5.1] also constructs sheaf quantizations for certain non-smooth objects

C0-RIGIDITY OF LEGENDRIANS AND COISOTROPICS VIA SHEAF QUANTIZATION 7

in contact topology. However, one needs to start with a path of contactmorphisms to apply their
theorem. In particular, when we only have a discrete sequence of contactomorphisms, one cannot
directly apply their result, which is exactly the situation we need to deal with in the paper.

Acknowledgement. We would like to thank Mohammed Abouzaid, Roger Casals, Sheng-Fu Chiu,
Georgios Dimitroglou Rizell, St´ephane Guillermou, Vincent Humili`ere, R´emi Leclercq, Emmy Mur-
phy, Vivek Shende, Sobhan Seyfaddini, Michael Sullivan, Bingyu Zhang and Jun Zhang for helpful
discussions. We would also like to thank Maksim Stoki´c for helpful correspondence. T. A. is par-
tially supported by JSPS KAKENHI Grant Number JP24K16920. Y. I. is partially supported by
JSPS KAKENHI Grant Numbers JP22H05107 and JP25K17254. T. A. and Y. I. are partially
supported by JST, CREST Grant Number JPMJCR24Q1, Japan. W. L. is partially supported by
the AMS-Simons Travel Grant. C. K. is supported by Max Planck Institute for Mathematics in
Bonn.
 2. Completeness of Sheaves

2.1. Sheaves and singular supports. Fix a (small idempotent complete) rigid symmetric monoidal
category C0 and consider the compactly generated category
4 C := Ind(C0). For a smooth manifold
M , we will use the notation Sh(M ) to mean sheaves on M with values in C.
Microlocal sheaf theory developed in [48] comes with the following ingredients: On a C∞ manifold
M , one can assign, for any sheaf F ∈ Sh(M ), its singular support or microsupport SS(F ) ⊆ T ∗M ,
which is a closed conic coisotropic subset, and, under some mild regularity condition, is Lagrangian
if and only if F is constructible.5 For F ∈ Sh(M ), we write SS
∞(F ) ⊂ S∗M for the closed subset
corresponding to SS(F ). Moreover, for a closed subset Λ, we write ShΛ(M ) for the full subcategory
of Sh(M ) spanned by sheaves F such that SS∞(F ) ⊂ Λ.
We will use the characterization of singular supports using Ω-lenses [40, Definition 3.1] [46,
Section 2.7.2].
6 We set ˙T ∗M := T ∗M \ 0M , where 0M denotes the zero section of T ∗M . For a conic
open set Ω ⊆ ˙T ∗M , an Ω-lens is a locally closed subset Σ ⊂ M with the following properties: Σ is
compact and there exists an open neighborhood U of Σ and a family of C1-functions f : U ×[0, 1] →
R such that

(1) dft(x) ∈ Ω for any (x, t) ∈ U × [0, 1], where ft := f |U ×{t};
(2) f −1
t ((−∞, 0)) ⊆ f −1
t′ ((−∞, 0)) for t ≤ t′;
(3) the hypersurfaces f −1
t (0) coincide on U \ Σ;
(4) Σ = f −1
1 ((−∞, 0)) \ f −1
0 ((−∞, 0)).

Lemma 2.1 ([40, Lemma 3.2]). Let F ∈ Sh(M ) and Ω ⊆ ˙T ∗M be a conic open set. Then
SS(F ) ∩ Ω = ∅ if and only if Hom(1Σ, F ) = 0 for all Ω-lenses Σ.

For sheaves F12 ∈ Sh(M1 × M2) and F23 ∈ Sh(M2 × M3), we can consider their convolution
F23 ◦ F12 ∈ Sh(M1 × M3) defined by

F23 ◦ F12 := π13!(π∗
23F23 ⊗ π∗
12F12),

4When C is not compactly generated (even if it is dualizable presentable), the non-characteristic deformation
lemma [48, Proposition 2.7.2] [72] fails and the conditions of [48, Proposition 5.1.1] are no longer equivalent, as
explained in [27, Remark 4.24]. However, [27, 88] suggest a definition of singular supports for sheaves with values in
non-compactly generated coefficients using Ω-lenses (defined below).
5We follow the convention in [32, 50, 52] and do not require constructible sheaves to have perfect stalks, which is
different from [48] (where such sheaves are called weakly constructible sheaves).
6From the viewpoint of [32], when Ω is a contractible neighborhood around a point, Ω-lenses correspond to
(sheaf-theoretic) linking disks around that point.

8 TOMOHIRO ASANO, YUICHI IKE, CHRISTOPHER KUO, AND WENYUAN LI

where πij : M1 × M2 × M3 → Mi × Mj is the projection map.
7 We also define the convolution
of sets as follows. We let pij : T ∗(M1 × M2 × M3) → T ∗(Mi × Mj) denote the projection. For
Λ12 ⊆ T ∗(M1 × M2) and Λ23 ⊆ T ∗(M2 × M3), we set

Λ23 ◦ Λ12 := p13(p−1
23 (Λ23)
a2 ∩ p−1
12 Λ12) ⊆ T ∗(M1 × M3)

where (−)a2 : T ∗(M2 × M3) → T ∗(M2 × M3) is the antipodal map on the M2-component. The
convolution satisfies the following singular support estimation:

Lemma 2.2 ([39, Equation (1.12)]). Let F12 ∈ Sh(M1 × M2) and F23 ∈ Sh(M2 × M3). Assume
that π13 is proper on π−1
23 supp(F23) ∩ π−1
12 supp(F12) and

p
−1
23 (SS(F23)
a2) ∩ p−1
12 SS(F12) ∩ (0M1 × T ∗M2 × 0M3) ⊆ 0M1×M2×M3.

Then, we have SS(F23 ◦ F12) ⊆ SS(F23) ◦ SS(F12).

Furthermore, the GKS sheaf quantization [39] allows contact isotopies to act on the category of
sheaves via convolutions:

Notation 2.3. We denote a contactomorphism by φ : S∗M → S∗M , and by abuse of notations,
its associated homogeneous symplectomorphism by φ : ˙T ∗M → ˙T ∗M , whose graph in S∗(M × M )
or ˙T ∗(M × M ) is Γ
φ = {((x, −ξ), φ(x, ξ)) | (x, ξ) ∈ ˙T ∗M }.

We write Φ : S∗M × U → S∗M for a U -family of contact isotopies and φt = Φ|S∗M ×{t} the time-
t map and H : S∗M × U → R the associated Hamiltonian where Ht ◦ φt(x, ξ) = α(∂tφt(x, ξ)).
We also abuse notations and write Φ and H for the associated homogeneous Hamiltonian isotopy
Φ : ˙T ∗M ×U → ˙T ∗M and H : ˙T ∗M ×U → R. We denote the graph of the homogeneous Hamiltonian
diffeomorphism at time-t by ΓΦ
t and sometimes ΓH
t in S∗(M × M ) or ˙T ∗(M × M ) to be

Γ
Φ
t = {((x, −ξ), φt(x, ξ)) | (x, ξ) ∈ ˙T ∗M }.

Theorem 2.4 ([39, Proposition 3.2, Theorem 3.7, & Remark 3.9]). For any contact isotopy Φ =
(φt)t∈U : S∗M × U → S∗M where U is a contractible manifold containing 0, there exists a unique
sheaf kernel KΦ ∈ Sh(M × M × U ) such that for the inclusion i0 : M × M × {0} ↪→ M × M × U ,
i∗
0KΦ = 1∆ and

(2.1) SS∞(KΦ) ⊆ {(x, −ξ, φt(x, ξ), t, −Ht ◦ φt(x, ξ)) | (x, ξ) ∈ S∗M, t ∈ U } ,

where H : S∗M × U → R is the associated contact Hamiltonian.

Remark 2.5. (1) Let U = I be a closed interval containing 0, we can construct a sheaf quantization
for any 1-parametric contact isotopy such that i∗
0KΦ = 1∆ and

SS
∞(KΦ) ⊆ {(x, −ξ, φt(x, ξ), t, −Ht ◦ φ(x, ξ)) | (x, ξ) ∈ S∗M, t ∈ I} .

(2) Let U = I ×J be a product of closed intervals containing 0, we can construct a sheaf quantization
for any 2-parametric contact isotopy. When there is a contactomorphism φ = φ1,s for any s ∈ J,
we know that SS
∞(i∗
1×J KΦ) ⊆ {(x, −ξ, φ(x, ξ), s, 0) | (x, ξ) ∈ S∗M, s ∈ J} .

Then by [39, Corollary 1.6], there exists a well-defined sheaf kernel Kφ = i∗
1,sKΦ ∈ Sh(M × M )
such that SS
∞(Kφ) ⊆ {(x, −ξ, φ(x, ξ)) | (x, ξ) ∈ S∗M } .

Therefore, we have a canonical sheaf quantization for any homotopy class of contact isotopies.

7We follow the convention in [50, 51] to write F23 ◦ F12, which is different from [48, 39] (where they use F12 ◦ F23).
This also results in a difference between our definition of graphs with the one in [39].

C0-RIGIDITY OF LEGENDRIANS AND COISOTROPICS VIA SHEAF QUANTIZATION 9

Notation 2.6. For a contact isotopy Φ : S∗M × I → S∗M with I being a closed interval, we
simply write KΦ
t := i∗
t KΦ for t ∈ I. When considering the contact isotopy Φ induced by the
contact Hamiltonian H, we also use the notations KH and KH
t to denote KΦ and respectively KΦ
t .

The assignment Φ ↦→ KΦ matches compositions of isotopies with convolutions of sheaves because
of Equation (2.1). That is, if Φ and Ψ are two contact isotopies, then KΦ ◦ |U KΨ = KΦ◦Ψ. In
particular, KΦ is invertible with respect to ◦|U , and it defines, a U -family of auto-equivalence on
Sh(M ). Explicitly, composing F ∈ Sh(M ) with KΦ gives a U -family sheaf KΦ ◦ F which satisfies
the microsupport estimation

(2.2) SS
∞(KΦ ◦ F ) ⊆ {(φt(x, ξ), t, −Ht ◦ φt(x, ξ)) | (x, ξ) ∈ SS∞(F ), t ∈ U } .

Similarly, in the case of a sheaf kernel L ∈ Sh(M × M ), we have

(2.3) SS
∞(KΦ ◦ L) ⊆ {((x, ξ), φt(y, η), t, −Ht ◦ φt(x, ξ)) | (x, ξ, y, η) ∈ SS∞(L), t ∈ U } .

One structure which comes out from this machinery is the continuation map [50, Section 3]. Let
σ be the fiber coordinate for T ∗I. The subcategory of Sh(M × I) which consists of objects F such
that SS(F ) ⊆ {σ ≤ 0}. Being a subcategory closed under limits, it admits a surjective left adjoint
and it can be given explicitly by

1{(t,s)|s>t}[1] ◦ (−) : Sh(M × I) → Shσ≤0(M × I),

where 1{(t,s)|s>t} convolves on the I-direction. Thus, for F ∈ Sh(M × I), F is in Shσ≤0(M × I) if
and only if the canonical map F = 1{s=t} ◦ F ∼
−→ 1{(t,s)|s>t}[1] ◦ F is an isomorphism. In this case,
for s ∈ I and the inclusion is : M × {s} ↪→ M × I, we have i∗
sF = 1(−∞,s) ◦ F [1].

Definition 2.7. For s ≤ t in I and F ∈ Shσ≤0(M × I), the continuation map

c(H, s, t) : i∗
sF → i∗
t F

is the map induced by 1(−∞,s) ◦ F [1] cs,t◦idF [1]
−−−−−−→ 1(−∞,t) ◦ F [1], where cs,t : 1(−∞,s) → 1(−∞,t) is the
universal continuation map coming from the inclusion (−∞, s) ⊆ (−∞, t).

Proposition 2.8 ([50, Proposition 3.9]). Let F ∈ Sh(M ) be a sheaf and Φ : S∗M × I → S∗M be a
contact isotopy that is positive on SS∞(F ). Then there exists a canonical continuation morphism
that only depends on the homotopy class of the isotopy and the time-1 map

c(Φ, F ) : F → KΦ
1 ◦ F.

Remark 2.9. For any positive contact isotopy Φ : S∗M × I → S∗M , [50, Proposition 3.33] implies
that there exists a continuation morphism

c(Φ, F ) : F → KΦ
1 ◦ F.

For a J-family of positive contact isotopies Φ : S∗M × I × J → S∗M , when φ = φ1,s for any s ∈ J,
by [50, Proposition 3.9], we know that c(Φs, F ) for different s ∈ J is canonically identified and thus
does not depend on the parameter, so we have a canonical continuation morphism.

Consider also the situation where we have two isotopy Φ, Ψ : S∗M × I → S∗M . Denote by
HΦ and HΨ their corresponding Hamiltonians. Then Φ−1 is generated by the Hamiltonian H Φ =
−HΦ(φt(p), t). If HΦ ≥ HΨ, then the composition Ψ−1 ◦ Φ will be a positive isotopy since it is
generated by (H Ψ♯HΦ)(p, t) := −HΨ(ψt(p), t) + HΦ(ψt(p), t) and there is a continuation map

(2.4) 1∆ → KΨ−1◦Φ
1 = KΨ−1
1 ◦ KΦ
1 .

Definition 2.10. We refer to the morphism KΨ
1 → KΦ
1 that corresponds to (2.4) under the
equivalence KΨ
1 ◦ (−) : Sh(M × M ) ∼
−→ Sh(M × M ) as the continuation map induced from Φ ≥ Ψ.

10 TOMOHIRO ASANO, YUICHI IKE, CHRISTOPHER KUO, AND WENYUAN LI

Let τ : S∗M → R be a smooth function and define Shτ ≥0(M ) to be the full subcategory consisting
of objects F with SS∞(F ) ⊆ {τ ≥ 0}. By (2.2), SS(Kτ ◦ F ) ⊆ {σ ≤ 0} and thus has a notion of
continuation map.

Notation 2.11. For F ∈ Shτ ≥0(M ), we denote by ct(F, τ ) : F → Kτ
t ◦ F the continuation map
associated to F and τ . When the exact sheaf F and Hamiltonian τ are clear from the context or
not crucial, we simply denote it by ct and c := c1 for time-1 continuation maps. Similarly, for a
morphism u : G → F , we use the notation ut to mean the image of u under the equivalence

Kτ
t ◦ (−) : Hom(G, F ) ∼
−→ Hom(Kτ
t ◦ G, Kτ
t ◦ F ).

Remark 2.12. The wrappings the morphisms are compatible with continuation maps. More
precisely, with previous notation, we note that since the continuation maps between 1(−∞,t) ◦ F[1]
are induced from the universal continuation maps, as recalled in Theorem 2.7, we have ct(F ) ◦ u =
ut ◦ ct(G). That is, the diagram
 G F

Gt Ft

u

ut

ct(G) ct(F )⟲

commutes canonically since the convolution operation ◦ is bilinear.

One of the main benefits of having continuation maps is that one can import the perturbation
trick from Floer theory to microlocal sheaf theory. First, without any constructibility assumption,
continuation maps respect colimit and limit with respect to the time direction.

Lemma 2.13 ([50, Corollaries 3.4 & 3.8]). Let F ∈ Shτ ≥0(M ). Then the canonical maps

Kτ
t ◦ F → lim
s→t+ (Kτ
s ◦ F ) and colim
s→t− (Kτ
s ◦ F ) → Kτ
t ◦ F

are equivalences.

Proof. The cited corollaries asserts that, as long as continuation map exists, in the general sense
in Theorem 2.7, the map from the colimit is always an equivalence. To conclude the map to the
limit is an equivalence, one has to check that the sheaf Kτ ◦ F is I-non-characteristic, i.e.,

SS(Kτ ◦ F ) ∩ (0M × T ∗
t I) ⊆ 0M ×I , for t ∈ I,(2.5)

but this follows directly from Equation (2.2). □

Secondly, there is a deformation lemma which parallels the transverse intersection phenomenon
from Floer theory [90, 50]. The usual setting is when F ∈ Sh(M ) is a compactly supported sheaf
with a Legendrian microsupport (at the infinity) Λ such that Λ is positively displaceable in the
sense that there exists ϵ > 0 such that φt(Λ) ∩ Λ = ∅ for 0 < t < ϵ. For the purpose of this paper,
we generalizes to the case of non-compactly supported sheaves. We will fix a complete Riemannian
metric on the manifold M . This determines a complete Riemannian metric on S∗M and a standard
contact form on S∗M which is bounded with respect to the metric.

Definition 2.14. Let M be a complete Riemannian manifold and Φ : S∗M ×I → S∗M be a contact
isotopy. Then Φ is called a bounded contact isotopy if the contact Hamiltonian HΦ with respect to
the standard contact form induced by the Riemannian metric is uniformly C0-bounded below and
above and C1-bounded above by some positive constants.

C0-RIGIDITY OF LEGENDRIANS AND COISOTROPICS VIA SHEAF QUANTIZATION 11

Remark 2.15. On the cosphere bundle S∗M , there always exist a bounded positive contact isotopy.
For example, one can consider a complete Riemannian manifold with positive injectivity radius and
take the geodesic flow associated to the metric. This is defined by the constant Hamiltonian, and
the lengths of closed orbits have a positive lower bound by the injectivity radius.

Lemma 2.16 ([90, Lemma 2.10], [50, Proposition 3.18]). Let F and G ∈ ShΛ(M ). Let τ : S∗M → R
be a bounded positive contact Hamiltonian such that φτ
t (Λ) ∩ Λ = ∅ for 0 < t < ϵ. Then for any
t > 0, the continuation map F → Kτ
t ◦ F induces an isomorphism

Hom(G, F ) ∼
−→ Hom(G, Kτ
t ◦ F ).

Proof. We follow the proof of [55, Section 4.1]. We know by Theorem 2.13 that

Hom(G, F ) = lim
t→0+ Hom(G, Kτ
t ◦ F ),

and we will argue that the right hand side is a constant diagram. The key observation is that
the assumption in the lemma ensures the existence of a Hamiltonian isotopy, which realizes the
diagram by convolutions by GKS kernels and shows that it is constant. This relaxes the compact
support assumption in the cited references [90, 50].
Since the C1-norm of the contact Hamiltonian τ is uniformly bounded below, we know that the
contact vector field of the isotopy Φτ is bounded below by a positive constant. Therefore, for any
0 < t < t′ < ϵ, there exists a neighborhood of Λ of positive radius that is disjoint from φτ
s (Λ) for
any t < s < t′. Then consider a cut-off function ρ such that ρ|Λ = 0, ρ|φτ
s (Λ) = 1 for any t < s < t′,
and ρ has bounded C1-norm. Since the C1-norm of τ is bounded, we know that the C1-norm of
the contact Hamiltonian ˜τ = ρτ is also bounded, and hence the associated contact flow is complete.
Moreover, we know that the contact flow generated by ρτ sends Λ ∪ φτ
t (Λ) to Λ ∪ φτ
t′(Λ). Therefore,
the isotopy Φ˜τ generated by ˜τ = ρτ implies that

Hom(G, Kτ
t ◦ F ) ≃ Hom(K ˜τ
t′−t ◦ G, K ˜τ
t′−t ◦ (Kτ
t ◦ Ft)) ≃ Hom(G, Kτ
t′ ◦ F ).

This shows that we have a constant diagram and finishes the proof. □

2.2. Microlocalization and microsheaves. We recall the notion of microlocalization following
[48, Chapters 4 & 6] and [37, 64, 65].
Let X ⊆ S∗M be a closed subset. We know by [40, Proposition 3.4] that the inclusion functor
ιX∗ : ShX (M ) ↪→ Sh(M ) is limit and colimit preserving, and consequently has a left and right
adjoint. Since Sh(M ) is a dualizable category, we can show that the left adjoint is represented by
a sheaf kernel [53, Proposition 3.1 and 3.2], which we call the microlocal kernel (initiated in the
works of [83, Section 7.1], [20], [37, Section 3.5], and [89]):

Proposition 2.17 ([51, Lemma 4.6], [53, Proposition 3.5]). Let X ⊆ S∗M be a closed subset.
Then the left adjoint ι∗
X : Sh(M ) → ShX (M ) of the tautological inclusion ShX (M ) ↪→ Sh(M ) is
represented by the convolution with the unique sheaf kernel PX = ι∗
T ∗M ×X 1∆ ∈ ShT ∗M ×X (M × M ).

Notation 2.18. We denote the projector from Sh(M ) to Shτ ≥0(M ) by Pτ . This is, Pτ the unique
sheaf kernel realizing the left adjoint of the inclusion Shτ ≥0(M ) ⊆ Sh(M ) by convolution.

Definition 2.19. Let Λ ⊆ S∗M be a closed subset. Define the presheaf of stable ∞-categories
µshpre
Λ on S∗M by µshpre
Λ : Ω ↦→ µsh
pre
Λ (Ω) = ShΛ∪Ωc(M )/ ShΩc(M ),

where the quotient is taken in Pr
L
st. Define the sheafification of µsh
pre
Λ in the category of all stable
∞-categories to be µshΛ.
8

8The choice of the ambient categories (of categories) ensure [48, Theorem 6.1.2] applies, which implies that the
sheaf-Hom in µshΛ is computed by the celebrated µhom defined in [48, Definition 4.4.1].

12 TOMOHIRO ASANO, YUICHI IKE, CHRISTOPHER KUO, AND WENYUAN LI

The sheaf of categories µshΛ is a sheaf in S∗M that is supported in Λ. By abuse of notations,
we will use µshΛ to denote the restriction of the sheaf on Λ. When Λ is a smooth Legendrian, the
sheaf of categories µshΛ is a locally constant sheaf on Λ, whose obstruction theory is studied by
Guillermou [36, 37] and Jin [45]:

Theorem 2.20 ([37, Section 10.3 & 10.6], [45, Theorem 1.1]). Let Λ ⊆ S∗M be a closed Leg-
endrian. Then the sheaf of categories µshΛ is a locally constant sheaf of categories whose stalk
is C that is classified by the composition of the Lagrangian Gauss map and the delooping of the
J-homomorphism Λ → U/O → BPic(S) → BPic(C).

For C = Mod(Z/2Z)/[1] the (pre)triangulated orbit category of Mod(Z/2Z), the classifying map is
always trivial, and for C = Mod(Z), the classifying map is trivial if and only if the Maslov class
µ(Λ) = 0 and the relative second Stiefel–Whitney class rw2(Λ) = 0, and µ(Λ) = 0 if and only if
there exist objects with stalks being bounded complexes. 9

Notation 2.21. Given a contact Hamiltonian τ : S∗M → R that is positive on a subset Λ ⊆ S∗M ,
we denote by Λτ
t ⊆ S∗M the time-t push-off of Λ under the contact Hamiltonian flow of τ . We also
denote by Λτ ⊆ S∗(M × I) the Legendrian movie of Λ under the contact Hamiltonian flow of τ .

Following the suggestion of Viterbo, one can understand microsheaves using sheaves via the fol-
lowing doubling construction. The following theorem is a generalization of the result of Guillermou
[37, Proposition 11.3.5 & Theorem 12.1.1] to arbitrary positive Hamiltonian flows.

Theorem 2.22 ([65, Theorem 7.18], [52, Theorem 4.1]). Let M be a complete Riemannian manifold
and Λ ⊆ S∗M be a properly embedded Legendrian with a tubular neighborhood of positive radius.
Let τ : S∗M → R be a contact Hamiltonian that is positive and bounded on Λ. Then for sufficiently
small ϵ > 0, there exists a fully faithful embedding

wΛ : µshΛ(Λ) ↪→ ShΛid∪Λτ (M × [0, ϵ]) ↪→ ShΛ∪Λτ
ϵ (M ).

Remark 2.23. While [52, Theorem 4.1] is proved for compact Legendrians Λ ⊆ S∗M , it can be
generalized to properly embedded Legendrians with tubular neighborhoods of positive radius by
exactly the same argument in [57, Theorem 3.7] whenever the contact Hamiltonian τ is C1-bounded,
so that the push-off Λτ
ϵ is still contained in the tubular neighborhood of Λ.

2.3. Interleaving distance and completeness of sheaves. Given a smooth function τ : S∗M →
R, Guillermou–Viterbo [40] and Asano–Ike [3] considered the interleaving distance dτ on certain
categories of sheaves. We adapt the setting of Petit–Schapira [70] and Guillermou–Viterbo [40].

Definition 2.24. Let τ be a smooth Hamiltonian on S∗M . For F, G ∈ Shτ ≥0(M ) and a, b ≥ 0, we
say that (F, G) is (a, b)-interleaved if there are morphisms

(2.6) u : F → Kτ
a ◦ G, v : G → Kτ
b ◦ F

such that the compositions

Kτ
−a ◦ F → G → Kτ
b ◦ F, Kτ
−b ◦ G → F → Kτ
a ◦ G

are isomorphic to the natural continuation maps c−a,b : Kτ
−a → Kτ
b and c−b,a : Kτ
−b → Kτ
a . The
interleaving distance between F and G are defined by

dτ (F, G) = inf{a + b | (F, G) is (a, b)-interleaved}.

9In fact, in order to exhibit the existence of F , the main result of [65, Section 11.6], which states that the obstruction
is classified by a map to BPic(C), is enough. This is because, when C = Mod(Z/2Z)/[1], the latter is a point {∗} so
the obstruction vanishes trivially. As explained in [65, Remark 11.21], one of Jin’s main contributions in [45] is to
identify the obstruction in the universal case C = Mod(S) with the well-known invariant, the J-homomorphism.

C0-RIGIDITY OF LEGENDRIANS AND COISOTROPICS VIA SHEAF QUANTIZATION 13

Remark 2.25. Here, we view the Kτ
c ’s as auto-equivalences on Shτ ≥0(M ), and the existence of
continuation maps are implied by and Theorem 2.7 and Theorem 2.8. A pair (F, G) is (a, b)-
interleaved if F and G are isomorphic to each other up to continuation maps with a size a + b.

Following the heuristic of viewing sheaves as singular Lagrangians, the notion of interleaving
distance shares a close relation with its underlying geometry. In fact, microsupports respect the
metric topology induced from dτ .

Proposition 2.26 ([40, Proposition 6.26]). Let Fn ∈ Shτ ≥0(M ) be a sequence of sheaves such that
limn→∞ dτ (Fn, F∞) = 0, i.e., the sequence Fn converges to F∞ under the interleaving distance.
Then SS(F∞) ⊆ ⋂
n≥1
 ⋃

k≥n SS(Fn).

Remark 2.27. A strict inequality in Theorem 2.26 is sometimes unavoidable. One might wonder:
is it possible to perturb Fn by some small Kτ
ϵn’s and obtain F ′
n so that it converges to the same limit
F∞ while making the inequality an equality? The answer is that this is in general not possible.
Per Theorem 2.30, if limn→∞ d(Fn, 0) = 0 and Fn are constructible, F∞ = 0 must not have any
microsupport. However, for the family of sheaves Fn = 1[0,1/n) on R, even up to perturbation to
some F ′
n = 1[ϵn,1/n+ϵn) for some sequence ϵn → 0, the intersection
⋂

n≥1
 ⋃
k≥n SS(F ′
n)

is always non-empty and hence the equality cannot hold.

The following result is an immediate corollary of Theorem 2.26. However, one can also directly
prove it using Ω-lenses.

Proposition 2.28. Let F, G ∈ Shτ ≥0(M ) such that dτ (F, G) = 0. Then SS(F ) = SS(G).

Proof. We remark that the statement follows from Theorem 2.26 by setting Fn = G for all n. We
present here a straightforward argument using only the fact that Ω-lenses detect microsupport.
By symmetry, it is sufficient to show SS(G) ⊆ SS(F ). Given any conic open subset Ω ⊆ T ∗M
such that Ω ∩ SS(F ) = ∅, consider any Ω-lens Σ. When ϵ > 0 is sufficiently small, we have

Hom(1Σ, Kτ
ϵ ◦ F ) = 0.

Since dτ (F, G) = 0, for any ϵ > 0 sufficiently small, there exist morphisms such that the composition

Hom(1Σ, G) → Hom(1Σ, Kτ
ϵ ◦ F ) → Hom(1Σ, Kτ
2ϵ ◦ G)

is the natural continuation morphism. Thus, for any ϵ > 0 sufficiently small, the natural continua-
tion morphism factors through zero. However, we know that by Theorem 2.13

Hom(1Σ, G) ∼
−→ limϵ→0 Hom(1Σ, Kτ
2ϵ ◦ G).

This implies that Hom(1Σ, G) = 0 so Ω ∩ SS(G) = ∅ by Theorem 2.1. Thus, SS(G) ⊆ SS(F ). □

The converse of the previous Theorem 2.28 is however untrue. The reason is that the distance
on the category comes from both the underlying geometry as well as the algebraic coefficient:

Example 2.29. Local systems Loc(M ) ⊆ (Shτ ≥0(M ), dτ ) consists of discrete points. Let F ∈
Shτ ≥0(M ) and L ∈ Loc(M ). Since Hom(Kτ
t ◦ F, L) = Hom(F, L) for any t ∈ R, (F, L) being
(a, b)-interleaving is equivalent to having u : F → L and v : L → F such that u ◦ v and v ◦ u are
both identity. That is, dτ (F, L) < ∞ if and only if F = L.

As a consequence of the example above, we see that (Shτ ≥0(M ), dτ ) in general can have infinitely
many disconnected components. For example, when M = S1, Shτ ≥0(M ) contains at least Aut(1C)-
many components; in the case when C = Mod(k), Aut(1C) = k×.

14 TOMOHIRO ASANO, YUICHI IKE, CHRISTOPHER KUO, AND WENYUAN LI

Now, we give a mild generalization to the fact that the interleaving distance induces a complete
metric space on a suitable subcategory of Shτ ≥0(M ). This generalizes the foundation theorem
established by Guillermou–Viterbo and the first two authors is that the interleaving distance is a
complete pseudo-metric on the corresponding category of sheaves:

Theorem 2.30 ([40, Proposition 6.22], [3, Corollary 4.5]). The interleaving distance dτ is a com-
plete pseudo-metric on Shτ ≥0(M ).

The non-Hausdorff feature of this metric comes from the fact that, for sheaves with arbitrary
size, there can be a small portion which is undetectable:

Remark 2.31 ([40, Example 6.5]). The interleaving distance dτ is in general a degenerate pseudo-
metric on Shτ ≥0(M ). For example, let M = Rt, F = ⊕∞
n=1 1[1/n,+∞) and G = (
⊕∞
n=1 1[1/n,+∞)) ⊕
1[0,+∞). Then dτ (F, G) = 0 but F ̸= G.

However, on the category of constructible sheaves up to infinity with perfect stalks, Petit–
Schapira–Waas showed that the distance is non-degenerate [71, Theorem 3.4], and on the category
of limits of constructible sheaves with perfect stalks over a field Shb
lc(M ; k), Guillermou–Viterbo
showed that the distance is non-degenerate [40, Proposition B.8].
We can give a proof of non-degeneracy of the interleaving distance for all constructible sheaves
whose singular supports are positively displaceable by the positive isotopy τ .

Theorem 2.32. Let τ : S∗M → R define a bounded contact isotopy on S∗M . Then the interleaving
distance dτ is non-degenerate on the category Shc,τ ≥0(M ) of constructible sheaves F ∈ Shτ ≥0(M )
such that φτ
t (SS
∞(F )) ∩ SS∞(F ) = ∅ for some 0 < t < ϵ.

Proof. Suppose dτ (F, G) = 0. Theorem 2.28 implies that SS∞(F ) = SS∞(G). Since SS
∞(F ) =
SS
∞(G) is positively displaceable from itself when 0 < t < ϵ0 for some ϵ0 > 0. Pick ϵ > 0 such that
2ϵ < ϵ0 and we can apply Theorem 2.16 and obtain that the continuation maps induces equivalences

(2.7) Hom(F, G) ∼
−→ Hom(F, Kτ
ϵ ◦ G) and Hom(G, F ) ∼
−→ Hom(G, Kτ
ϵ ◦ F ).

Shrink ϵ if needed, since dτ (F, G) = 0, there exist u : F → Kτ
ϵ ◦ G and v : G → Kτ
ϵ ◦ F such that
the compositions F → Kτ
ϵ ◦ G → Kτ
2ϵ ◦ F, G → Kτ
ϵ ◦ F → Kτ
2ϵ ◦ G
are equivalent to the continuation maps c2ϵ(F ) and c2ϵ(G). The equivalences in Equation (2.7)
implies that there exist unique a : F → G and b : G → F factorizes them to u = cϵ(G) ◦ a and
v = cϵ(F ) ◦ b. We thus have the following commuting diagram:

F Kτ
ϵ ◦ G Kτ
2ϵ ◦ F

G Kτ
ϵ ◦ F

F

u vϵ

v

cϵ(G) cϵ(F )

cϵ(F )

a
 b
 ⟲⟲
 ⟲

Note that the upper right square commutes by Theorem 2.12. Since post-composing with cϵ(F )◦(−)
induces equivalences on the relevant Hom-spaces, the equality

cϵ(F ) ◦ cϵ(F ) ◦ b ◦ a = u ◦ vϵ = c2ϵ(F ) = cϵ(F ) ◦ cϵ(F )

implies that b ◦ a = idF and one can deduce a ◦ b = idG similarly. □

C0-RIGIDITY OF LEGENDRIANS AND COISOTROPICS VIA SHEAF QUANTIZATION 15

Recall that a sheaf L ∈ Sh(M × M ) is often referred as a kernel since the category Sh(M × M )
classifies colimit-preserving endomorphisms of Sh(M ), and the convolution product corresponds
to the composition of functors. For the main applications, we will consider interleaving distance
between sheaf kernels from the GKS sheaf quantization Theorem 2.4. For such operators, we
consider a variant of Shτ ≥0(M ).
Consider the cosphere bundle of the product S∗(M × M ). We parametrize points in S∗(M × M )
by (x, ξ, y, η) where |ξ|2 + |η|2 = 1. Let

τ2 : S∗(M × M ) → R, (x, ξ, y, η) ↦→ τ (y, η/|η|)|η|

and consider the subcategory of sheaves

Shτ2≥0(M × M ) := {L ∈ Sh(M × M ) | SS∞(L) ⊆ τ −1
2 ([0, +∞))}.

For L ∈ Shτ2≥0(M × M ), applying Theorem 2.2 to the situation where M1 = M × M and M2 =
M3 = M × M × I, we see that Kτ ◦ L admits continuation maps. Namely, there is a canonical map

Kτ
s ◦ L → Kτ
t ◦ L

for s ≤ t, and we define the interleaving distance for objects in Shτ2≥0(M × M ) in a the same way
as Theorem 2.24, and completeness of the interleaving distance follows in the same way as before.

Definition 2.33. For F, G ∈ Shτ2≥0(M × M ) and a, b ≥ 0, we say that (F, G) is (a, b)-interleaved
if there are morphisms u : F → Kτ
a ◦ G and v : G → Kτ
b ◦ F such that the compositions

Kτ
−a ◦ F → G → Kτ
b ◦ F, Kτ
−b ◦ G → F → Kτ
a ◦ G

are isomorphic to the natural continuation morphisms c−a,b : Kτ
−a → Kτ
b and c−b,a : Kτ
−b → Kτ
a .
The interleaving distance between F and G are defined by

dτ (F, G) = inf{a + b | (F, G) is (a, b)-interleaved}.

Theorem 2.34. The interleaving distance dτ is a complete pseudo-metric on Shτ2≥0(M × M ).

While the function τ2 : S∗(M × M ) → R is not smooth, one can check that it is true that for any
L ∈ Shτ2≥0(M × M ), we have L ≃ lims→0+ Kτ
s ◦ L. Therefore, Theorem 2.28 still hold.

Proposition 2.35. Let K, L ∈ Shτ2≥0(M × M ) such that dτ (K, L) = 0. Then SS(K) = SS(L).

Proof. We know that by Equation (2.3), SS(Kτ ◦ L) consists of points (x1, ξ1, x3, ξ3, t, −τ (x3, ξ3))
where there exist (x2, −ξ2, x3, ξ3) ∈ SS(Kτ
t ) and (x1, ξ1, x2, ξ2) ∈ SS(L). When ϵ > 0 is sufficiently
small, SS(Kτ
ϵ ) is sufficiently close to T ∗
∆(M × M ). Thus, we also know that for any open subset
Ω ⊆ T ∗(M × M ) such that Ω ∩ SS(L) = ∅, when ϵ > 0 is small, Ω ∩ SS(Kτ
ϵ ◦ L) = ∅. Thus, for
any Ω-lens Σ, when ϵ > 0 is sufficiently small,

Hom(1Σ, Kτ
ϵ ◦ L) = 0.

Since dτ (K, L) = 0, for ϵ > 0 sufficiently small, there exist morphisms such that the composition

Hom(1Σ, L) → Hom(1Σ, Kτ
ϵ ◦ K) → Hom(1Σ, Kτ
2ϵ ◦ L)

is the natural continuation morphism. Hence when ϵ > 0 is sufficiently small, the natural continu-
ation morphism factors through zero.
On the other hand, for the points (x1, ξ1, x3, ξ3, t, −τ (x3, ξ3)) where there exist (x2, −ξ2, x3, ξ3) ∈
SS(Kτ
t ) and (x1, ξ1, x2, ξ2) ∈ SS(L), if ξ1 = ξ3 = 0 then τ (x3, ξ3) = 0, and thus Kτ ◦ L is still
non-characteristic along I. Therefore,

Hom(1Σ, L) ≃ lim
ϵ→0+ Hom(1Σ, Kτ
2ϵ ◦ L).

This implies that Hom(1Σ, L) = 0 so Ω ∩ SS(L) = ∅ by Theorem 2.1. Thus, SS(L) ⊆ SS(K) and
this completes the proof. □

16 TOMOHIRO ASANO, YUICHI IKE, CHRISTOPHER KUO, AND WENYUAN LI

However, the non-degeneracy Theorem 2.32 becomes more tricky as it requires Theorem 2.16.
We need to consider a smoothing of τ2 away from S∗M × 0M where the contact flow is well defined.

Lemma 2.36. Let M be a complete Riemannian manifold and suppose τ : S∗M → R defines a
bounded Reeb flow on S∗M . Then there exists a cut-off function ρ : S∗(M × M ) → R supported on
a tubular neighborhood of S∗M × 0M such that the Hamiltonian (1 − ρ)τ2 : S∗(M × M ) → R defines
a complete contact flow.

Proof. Consider a complete Riemannian metric on M , which induces a complete Riemannian metric
on M × M and S∗(M × M ). Then there exists a tubular neighborhood of S∗M × 0M of positive
radius. We can choose a cut-off function ρ : S∗(M ×M ) → R supported in the tubular neighborhood
such that |dρ| is uniformly bounded. Then since |(1 − ρ)τ2| ≤ |τ2| and |d((1 − ρ)τ2)| ≤ |τ2||dρ| + |dτ2|
are both uniformly bounded, the norm of the contact vector field X(1−ρ)τ2 is uniformly bounded
and therefore defines a complete contact flow. □

Theorem 2.37. Let τ : S∗M → R define a bounded positive contact Hamiltonian and Ω′ ⊆ Ω is a
pair of tubular neighborhoods of S∗M × 0M with positive radii r′ < r. Let ρ : S∗(M × M ) → R be a
bounded cut-off function supported in Ω′. Then the interleaving distance dτ is non-degenerate on the
category Shc,Ωc(M × M ) of constructible sheaves K ∈ ShΩc(M × M ) such that φ
(1−ρ)τ2
t (SS
∞(K)) ∩
SS
∞(K) = ∅ for some 0 < t < ϵ.

Proof. Suppose dτ (K, L) = 0. Theorem 2.28 implies that SS∞(K) = SS
∞(L). By Theorem 2.36,
(1 − ρ)τ2 defines a bounded contact vector field with a complete contact flow. Since SS
∞(K) ⊆ Ωc,
we can pick ϵ0 > 0 such that φ
(1−ρ)τ2
t (SS
∞(K)) ⊆ Ωc and

φ(1−ρ)τ2
t (SS
∞(K)) ∩ SS
∞(K) = ∅, 0 < t < ϵ0.

Pick ϵ > 0 such that 2ϵ < ϵ0. Let ̃K(1−ρ)τ2 be the sheaf quantization of the contact Hamiltonian
(1 − ρ)τ2; note that ̃K(1−ρ)τ2 lives on M 2 × M 2 × I so it treats L as an object. We can apply
Theorem 2.16 and obtain that the continuation maps induces equivalences

(2.8) Hom(K, L) ∼
−→ Hom(K, ̃K(1−ρ)τ2
ϵ ◦ L) and Hom(L, K) ∼
−→ Hom(L, ̃K(1−ρ)τ2
ϵ ◦ K).

Since φ(1−ρ)τ2
t (SS
∞(K)) ⊆ Ωc, we know that φ
(1−ρ)τ2
t (SS
∞(K)) = Γ
τ2
t ◦ SS
∞(K), by Theorem 2.2
SS
∞( ̃K(1−ρ)τ2 ◦ K) = SS(Kτ ◦ K). Then we can conclude that ̃K(1−ρ)τ2
ϵ ◦ K = Kτ
ϵ ◦ K, i.e.,
post-composition by Kτ
ϵ is equivalent to being acts as an object by ̃K(1−ρ)τ2
ϵ . Thus the following
continuation maps induces equivalences

(2.9) Hom(K, L) ∼
−→ Hom(K, Kτ
ϵ ◦ L) and Hom(L, K) ∼
−→ Hom(L, Kτ
ϵ ◦ K).

Shrink ϵ if needed, since dτ (K, L) = 0, there exist u : K → Kτ
ϵ ◦ L and v : L → Kτ
ϵ ◦ K such that
the compositions K → Kτ
ϵ ◦ L → Kτ
2ϵ ◦ K, L → Kτ
ϵ ◦ K → Kτ
2ϵ ◦ L

are equivalent to the continuation maps c2ϵ(K) and c2ϵ(L). The equivalences in Equation (2.9)
imply that there exist unique a : K → L and b : L → K factorizes them to u = cϵ(L) ◦ a and
v = cϵ(K) ◦ b. We thus have a ◦ b = idL and b ◦ a = idK. This completes the proof. □

Remark 2.38. In fact, Theorem 2.35 and Theorem 2.37 hold more generally on N × M where
N is another smooth manifold. Since kernels induce functors, this means that there is a non-
degenerate metric on a suitable class of functors from Sh(N ) to Sh(M ), which in the case of N = {∗}
recovers the case of objects Theorem 2.32. Furthermore, there is a τ1 version corresponding to pre-
composition instead of the post-composition case presented here. We do not go into details of these
generalizations since the focus of this paper requires only endofunctors.

C0-RIGIDITY OF LEGENDRIANS AND COISOTROPICS VIA SHEAF QUANTIZATION 17

We can also define another variant of the interleaving distance, which will be used later on.
Given a smooth function τ : S∗M → R, we define a log interleaving distance dln τ on the derived
category Shτ ≥0(M ) as follows:

Definition 2.39. Let τ be a smooth Hamiltonian on S∗M . For F, G ∈ Shτ ≥0(M ) and a, b ≥ 0,
we say that (F, G) is log (a, b)-interleaved if there are morphisms u : F → Kτ
ea−1 ◦ G and v : G →
Kτ
eb−1 ◦ F such that the compositions

Kτ
1−ea ◦ F → G → Kτ
eb−1 ◦ F, Kτ
1−eb ◦ G → F → Kτ
ea−1 ◦ G

are isomorphic to the continuation morphisms. The log interleaving distance of F and G are defined
by dln,τ (F, G) = inf{a + b | (F, G) is log (a, b)-interleaved}.

Since the function f (x) = ex − 1 is continuous and f (0) = 0, it follows immediately from
Theorem 2.30 that the log interleaving distance is also a complete pseudo-metric.

3. Hofer–Shelukhin Distances and Sheaves

In this section, we discuss the relation between the interleaving distance of sheaves and the
(Chekanov–)Hofer–Shelukhin distance of Legendrians. We will prove Theorem 1.13 (Theorem 3.2)
and use that to deduce Theorem 1.11 (Theorems 3.14 and 3.15).

3.1. Hofer–Shelukhin norm and interleaving distance. Our goal in the section is to deduce
Theorem 3.2 (Theorem 1.13), which generalizes the result of the first two authors [4] to any cosphere
bundles and any Reeb flows.
For the contact manifold (S∗M, ξstd), we will consider a smooth function τ : S∗M → R and
consider the open contact submanifold Y = τ −1(R>0) ⊆ S∗M . The Hamiltonian τ : Y → R>0
defines a positive contact flow, which is the Reeb flow with respect to some contact form α on Y .
We will consider contact Hamiltonians H : Y × I → R that extend smoothly to S∗M × I by zero,
or equivalently, H : S∗M × I → R such that supp(H) ⊆ τ −1(R>0).
We recall that in [78], the Hofer–Shelukhin norm of a contact Hamiltonian H : Y × I → R with
respect to the contact form α is defined as 10

∥H∥HS,α := ∫ 1

0 sup
(x,ξ)∈Y |Hs(x, ξ)| ds.

The Hofer–Shelukhin distance of φ, ψ ∈ Cont0(S∗M, ξstd) is defined as

dHS,α(φ, ψ) := inf
H:φ=φH
1 ◦ψ ∥H∥HS,α = inf
H:φ=φH
1 ◦ψ
 ∫ 1

0 sup
(x,ξ)∈Y |Hs(x, ξ)| ds.

On the universal cover ̃Cont0(Y, ξstd), consisting of homotopy classes of contact isotopies, abusing
notations, the Hofer–Shelukhin distance is defined as

dHS,α(φ, ψ) := inf
H:φ=φH ◦ψ ∥H∥HS,α = inf
H:φ=φH ◦ψ
 ∫ 1

0 sup
(x,ξ)∈Y |Hs(x, ξ)| ds.

Note that the Hofer–Shelukhin distance depends on the choice of the contact form. Consider the
positive Hamiltonian τ : Y → R>0. Under the contact form αstd, τ defines the Reeb flow for a
different contact form α = τ αstd. Then, for any Hamiltonian H under the given contact form αstd,
we will abuse the notation and write

∥H∥HS,τ := ∫ 1

0 sup
(x,ξ)∈Y |Hs(x, ξ)/τ (x, ξ)| ds.

10While ∥H∥HS,α does not depend on α, we choose this notation to keep consistency with the later ∥H∥HS,τ .

18 TOMOHIRO ASANO, YUICHI IKE, CHRISTOPHER KUO, AND WENYUAN LI

On ̃Cont0(Y, ξstd), we also write

dHS,τ (φ, ψ) := inf
H:φ=φH ◦ψ ∥H∥HS,τ = inf
H:φ=φH ◦ψ
 ∫ 1

0 sup
(x,ξ)∈Y |Hs(x, ξ)/τ (x, ξ)| ds.

The main result of the section is the following, which shows that the interleaving distance of
sheaves is bounded by the Hofer–Shelukhin distance, generalizing the result of the first two authors
[4] and [3, Theorem 5.2]. We remark that the only technical point to generalize is a lemma equivalent
to the following one. The rest is a similar argument refining partitions of [0, 1].

Lemma 3.1. Let τ : S∗M → R be a contact Hamiltonian that defines a complete contact flow.
Let H : S∗M × I → R be a compactly supported contact Hamiltonian such that φ = φH
1 such that
supp(H) ⊆ τ −1(R>0). Then, for s0, s1 ∈ I with s0 ≤ s1, we have

dτ (KH
s0 ◦ Pτ , KH
s1 ◦ Pτ ) ≤ 2 max
(x,ξ,s)∈S∗M ×[s0,s1] |Hs(x, ξ)/τ (x, ξ)||s1 − s0|.

Here Pτ is the projector defined in Theorem 2.18.

Proof. By the compactness assumption, we can set

−a := min
(x,ξ,s)∈S∗M ×[s0,s1] (Hs(x, ξ)/τ (x, ξ)) , b := max
(x,ξ,s)∈S∗M ×[s0,s1] (Hs(x, ξ)/τ (x, ξ)) .

Here, the value of Hs(x, ξ)/τ (x, ξ) is set to 0 outside supp(H). This implies the inequalities

−aτ ≤ H ≤ bτ

on [s0, s1]. Note that we have Pτ ∈ Shτ2≥0(M × M ). Thus, since for any c ∈ R, Kcτ
s = Kτ
cs,
by Theorem 2.8, we know that there exist continuation maps Kτ
−a(s1−s0) ◦ Pτ → KH
s1−s0 ◦ Pτ and
KH
s1−s0 ◦ Pτ → Kτ
b(s1−s0) ◦ Pτ , so there exist continuation maps

Kτ
−a(s1−s0) ◦ KH
s0 ◦ Pτ → KH
s1−s0 ◦ KH
s0 ◦ Pτ = KH
s1 ◦ Pτ ,

KH
s1 ◦ Pτ = KH
s1−s0 ◦ KH
s0 ◦ Pτ → Kτ
b(s1−s0) ◦ KH
s0 ◦ Pτ .

Consider the two different continuation maps, one from the Hamiltonian τ and the other from the
Hamiltonian aτ #H followed by the Hamiltonian H#bτ in Equation (2.6). We can construct a
family of positive contact isotopies from the compositions of the above two positive isotopies to
the positive isotopy (b − a)τ by linear interpolation and thus conclude, using Theorem 2.8 and
Theorem 2.9, that the two compositions of the continuation maps

Kτ
−a(s1−s0) ◦ KH
s0 ◦ Pτ → KH
s1 ◦ Pτ → Kτ
b(s1−s0) ◦ KH
s0 ◦ Pτ ,

Kτ
−b(s1−s0) ◦ KH
s1 ◦ Pτ → KH
s0 ◦ Pτ → Kτ
a(s1−s0) ◦ KH
s1 ◦ Pτ

are equivalent to continuation maps. Thus, we conclude

dτ (KH
s0 ◦ Pτ , KH
s1 ◦ Pτ ) ≤ (a + b)(s1 − s0) ≤ 2 max
(x,ξ,s)∈S∗M ×[s0,s1] |Hs(x, ξ)/τ (x, ξ)||s1 − s0|. □

Theorem 3.2 (Theorem 1.13). Let τ : S∗M → R be a contact Hamiltonian that defines a complete
contact flow. Let H : S∗M × I → R be a compactly supported contact Hamiltonian such that
supp(H) ⊆ τ −1(R>0). Then, we have

dτ (Pτ , KH
1 ◦ Pτ ) ≤ 2∥H∥HS,τ .

In particular, for any F ∈ Shτ ≥0(M ), we have

dτ (F, KH
1 ◦ F ) ≤ 2∥H∥HS,τ .

Similarly, let φ ∈ ̃Cont0(Y, ξstd) be a homotopy class of contact isotopies. Then we have

dτ (Pτ , Kφ ◦ Pτ ) ≤ 2 dHS,τ (id, φ).

C0-RIGIDITY OF LEGENDRIANS AND COISOTROPICS VIA SHEAF QUANTIZATION 19

In particular, for F ∈ Shτ ≥0(M ), we have

dτ (F, Kφ ◦ F ) ≤ 2 dHS,τ (id, φ),

Proof. We divide the time interval into small pieces 0 = s0 < s1 < · · · < sn = 1. The previous
Theorem 3.1 implies that

dτ (KH
si−1 ◦ Pτ , KH
si ◦ Pτ ) ≤ 2 max
(x,ξ,s)∈S∗M ×[si−1,si] |Hs(x, ξ)/τ (x, ξ)||si − si−1|.

Using the triangle inequality of the interleaving distance dτ and refining the partition so that
sup1≤i≤n |si − si−1| → 0, we obtain the result that

dτ (Pτ , KH
1 ◦ Pτ ) ≤ 2 ∫ 1

0 sup
(x,ξ)∈S∗M |Hs(x, ξ)/τ (x, ξ)| ds =: 2∥H∥HS,τ .

The inequality on Shτ ≥0(M ) follows from the property of being a projector: for a sheaf F ∈ Sh(M ),
F belongs to the subcategory Shτ ≥0(M ) if and only if F = Pτ ◦ F .
When φ ∈ ̃Cont0(Y, ξstd) is a homotopy class of contact isotopies, then by Theorem 2.5 we know
that the sheaf quantization Kφ = KH
1 is well-defined. Therefore,

dτ (Pτ , Kφ ◦ Pτ ) ≤ 2 inf
H:φ=[φH
t ] ∥H∥HS,τ .

This then completes the proof. □

Remark 3.3. Consider the sheaf quantization Kτ ∈ Sh(M × M × R). Using functoriality of the
interleaving distance [4], one can show that

dτ (πR∗H om(1∆ ⊠ 1R, Kτ ), πR∗H om(Kφ ⊠ 1R, Kτ )) ≤ 2 dHS,τ (id, φ).

This is the sheaf-theoretic analogue of a recent result of Cant [18] and Djordjevi´c–Uljarevi´c–Zhang
[26] on the interleaving distance of the symplectic cohomology. Alternatively, (over a discrete
ring) assuming that M is spin, this also follows from their results [18, 26] plus the isomorphism
of the Hamiltonian Floer cohomology and the sheaf invariants by Guillermou–Viterbo [40] and
Kuo–Shende–Zhang [53].

Remark 3.4. As a consequence, we can show that the sheaf-theoretic spectral norm of contact
Hamiltonians are also bounded by the Hofer–Shelukhin norm.

Let α and α′ be contact forms on (Y, ξ) such that α′ = ehα. Then the conformal norm or
Banach–Mazur norm of the contact form [80, 74] is

dBM(α, α′) = sup
(x,ξ)∈Y |h(x, ξ)|.

Let φ ∈ Cont0(Y, ξ) such that φ∗α′ = α. Then the Banach–Mazur norm of the contactomorphism
[80, 74] is ∥φ∥BM = dBM(α, α′) = sup
(x,ξ)∈Y |h(x, ξ)|.

The Banach–Mazur norm defines a pseudo-distance dBM on the space of contact forms, since any
two contact forms are related by a conformal factor. Let α and α′ be contact forms on the contact
manifold (Y, ξ) and Rα and Rα′ be the Reeb vector fields associated to the contact forms. Suppose
α = ehα′. Then under the contact form α, the Reeb vector field Rα′ is defined by the contact
Hamiltonian eh.

Lemma 3.5. Let α and α′ be contact forms on the contact manifold (Y, ξ) and R and R′ be the
Reeb vector fields associated to the contact forms. Suppose α = φ∗α′ for some φ ∈ Cont(Y, ξ).
Then φ∗R = R′ ◦ φ, φ ◦ φR
s = φ
R′
s ◦ φ.

20 TOMOHIRO ASANO, YUICHI IKE, CHRISTOPHER KUO, AND WENYUAN LI

Proof. It is sufficient to prove the first equality since the second differentiates to the first. It suffices
to check φ∗Rα satisfy the same Hamiltonian equation for α′ up to pre-composing with φ. We first
compute that α′
φ(y)(φ∗yRy) = (φ
∗α′)y(Ry) = αy(Ry) = 1.
Secondly, we compute that

dα′
φ(y)(φ∗yRy, φ∗y(−)) = (φ∗dα′)y(Ry, −) = (dα)y(Ry, −) = 0.

Uniqueness of Reeb vector field thus implies that φ∗yRy = R′
φ(y) as desired. □

Similar to Theorem 3.2, we can also show the log interleaving distance of the quantization of
Reeb flows are bounded by the Banach–Mazur distance.

Proposition 3.6. Let τ : S∗M → R and τ ′ : S∗M → R be two positive Hamiltonians that define
the Reeb flows for the contact forms α and α′ on (S∗M, ξstd). Then

dln τ (Kτ
1 ◦ F, Kτ ′
1 ◦ F ) ≤ 2dBM(α, α′), dln τ (Kτ
1 , Kτ ′
1 ) ≤ 2dBM(α, α′).

Proof. By Theorem 2.8, if G ≤ H, the positive contact isotopy H#(−G) gives a canonical contin-
uation map KG → KH . We know that the defining Hamiltonian satisfies the relation τ ′ = ehτ .
When h is unbounded, there is nothing to show. When −a ≤ h ≤ b, we have continuation maps

Kτ
e−a ◦ F → Kh
1 ◦ F → Kτ
eb ◦ F,

Kτ
e−b ◦ Kh
1 ◦ F → F → Kτ
ea ◦ Kh
1 ◦ F.

By Theorem 2.8 and Theorem 2.9, we know that the compositions of the above continuation maps
equal the natural continuation map of the Reeb flow. Therefore, (F, Kh
1 ◦F ) are log (a, b)-interleaved.
This proves the result. □

Remark 3.7. Consider the sheaf quantization Kτ ∈ Sh(M × M × R). Using functoriality of the
interleaving distance [4], one can show that

dln τ (πR∗H om(1∆ ⊠ 1R, Kτ ), πR∗H om(1∆ ⊠ 1R, Kτ ′)) ≤ 2 dBM(α, α′).

This is the sheaf theory analogue of the result of Stojisavljevi´c–Zhang [80]. Alternatively, (over a
discrete ring) assuming that M is spin, this also follows from their Floer-theoretic results [80] plus
the isomorphism result by Guillermou–Viterbo [40] and Kuo–Shende–Zhang [53].

Remark 3.8. As a consequence, we can show that the log sheaf-theoretic spectral norm of contact
Hamiltonians are bounded by the Banach–Mazur norm.

3.2. Non-degeneracy of the (Chekanov–)Hofer–Shelukhin distance. Using the above re-
sults and Theorem 2.30, we are able to define sheaf quantizations of limits of contact isotopies
under the Hofer–Shelukhin distance as in the symplectic situation [3, Section 5.3]. We will use that
to deduce Theorems 3.14 and 3.15 (Theorem 1.11).
However, unlike the symplectic situation, due to the issue that the Hofer–Shelukhin distance
is not conjugation invariant, we need more work to show that the limit sheaf quantizations are
invertible.
Let φ : S∗M → S∗M be a contactomorphism such that φ∗α = ehα. We recall that from Theo-
rem 2.3, the graph of the contactomorphism is the Legendrian submanifold

Γ
φ := {(x, −ξ, y, η) | (y, η/|η|) = φ(x, ξ/|ξ|), |ξ|/|η| = eh(x,ξ)} ⊆ S∗(M × M ).

For the contact Hamiltonian H that defines the contact isotopy φt : S∗M → S∗M such that
(φt)∗α = ehtα, one can compute that the conformal factor is equal to (where R is the Reeb
vector field of the contact form α)
 ht = ∫ t

0 dHs(R) ◦ φs ds.

C0-RIGIDITY OF LEGENDRIANS AND COISOTROPICS VIA SHEAF QUANTIZATION 21

Theorem 3.9. Let τ : S∗M → R be a positive Hamiltonian. Let φn ∈ Cont0(S∗M, ξstd) be the time-
1 maps of the contact Hamiltonians flows defined by Hn that uniformly converges to a continuous
function H∞. Then there exists a sheaf quantization KH∞
1 ∈ Sh(M × M ) with

SS
∞(KH∞
1 ) ⊆ ⋂

n≥1
 ⋃
k≥n Γφk .

Moreover, dτ (1∆, KH∞
1 ) ≤ 2∥H∞∥HS,τ .

Proof. Since φn and Hn form a Cauchy sequence under the Hofer–Shelukhin norm, by Theorem 3.2,
we know that the sheaf quantizations KHn
1 form a Cauchy sequence under the interleaving distance.
By Theorem 2.30, there exists a sheaf kernel KH∞
1 = limn→∞ KHn
1 . Theorem 2.26 implies that

SS
∞(KH∞
1 ) ⊆ ⋂

n≥1
 ⋃
k≥n Γφk .

Moreover, by Theorem 3.2, we know that dτ (1∆, KH∞
1 ) ≤ ∥H∞∥HS,τ . □

Theorem 3.10. Let τ : S∗M → R be a positive Hamiltonian. Let φn ∈ Cont0(S∗M, ξstd) be
the time-1 maps of the contact Hamiltonians flows defined by Hn, each of which has bounded
conformal factor, that uniformly converges to H∞, and φn uniformly converges under the C0-
topology so that H n uniformly converges to H ∞. Then there exists a sheaf quantization KH∞
1 and
KH ∞ ∈ Sh(M × M ) such that
 KH ∞
1 ◦ KH∞
1 ≃ KH∞
1 ◦ KH ∞
1 ≃ 1∆.

Proof. Since φn converges to a continuous map, H n(p, t) = −Hn(φn(p), t) also converges to a
continuous function H ∞, and there exists a sheaf kernel KH ∞
1 such that KH n
1 → KH ∞
1 . We have
KH n
1 ◦ KH∞
1 → KH ∞
1 ◦ KH∞
1 since the interleaving distance on the product is right invariant. On
the other hand, we can show that KH n
1 ◦ KHm
1 → KH n
1 ◦ KH∞
1 as follows. When (KHm
1 , KHm′
1 ) are
(a, b)-interleaved, we know that there are morphisms such that the compositions

KH n
1 ◦ Kτ
−a ◦ KHm
1 → KH n
1 ◦ KHm′
1 → KH n
1 ◦ Kτ
b ◦ KHm
1 ,

KH n
1 ◦ Kτ
−b ◦ KHm′
1 → KH n
1 ◦ KHm
1 → KH n
1 ◦ Kτ
a ◦ KHm′
1

are the continuation morphisms. Then by applying Theorem 3.5, we have φ
τn
t ◦ φ−1
n = φ−1
n ◦ φτ
t ,
where τn is the Reeb vector field associated to φ∗
nα. Therefore, by Theorem 3.6, when the conformal
factor of φn is bounded by hn, we get

Kτ
−ehn a ◦ KH n
1 ◦ KHm
1 → KH n
1 ◦ KHm′
1 → Kτ
ehn b ◦ KH n
1 ◦ KHm
1 ,

Kτ
−ehn b ◦ KH n
1 ◦ KHm′
1 → KH n
1 ◦ KHm
1 → Kτ
ehn a ◦ KH n
1 ◦ KHm′
1
whose compositions are continuation morphisms. Thus, given n ∈ N, for any Hm and Hm′,

dτ (KH n
1 ◦ KHm
1 , KH n
1 ◦ KHm′
1 ) ≤ e
hn dτ (KHm
1 , KHm′
1 ).

Hence, we know that for any given n ∈ N, KH n
1 ◦ KHm
1 → KH n
1 ◦ KH∞
1 , and

dτ (1∆, KH n
1 ◦ KH∞
1 ) ≤ 2∥H n#H∞∥HS,τ .

Since H n#H∞ → 0 as n → ∞, we know KH n
1 ◦ KH∞
1 → 1∆. Therefore, dτ (1∆, KH ∞
1 ◦ KH∞
1 ) = 0.
By Theorems 2.32 and 2.35, we can conclude that KH ∞
1 ◦ KH∞
1 = 1∆. □

Remark 3.11. One can, instead of considering the interleaving distance defined by τ2 throughout
the proof, apply the interleaving distance defined by τ2 to show the convergence KHn
1 → KH∞
1 and

22 TOMOHIRO ASANO, YUICHI IKE, CHRISTOPHER KUO, AND WENYUAN LI

the distance defined by τ1 to show the convergence KH n
1 → KH ∞
1 . Then, define the bi-interleaving
distance such that (F, G) are (a, b)-bi-interleaved if there are morphisms

Kτ
−a ◦ F ◦ Kτ
−a → G → Kτ
b ◦ F ◦ Kτ
b , Kτ
−b ◦ G ◦ Kτ
−b → F → Kτ
a ◦ G ◦ Kτ
a .

If we can show that d(1∆, KH∞
1 ◦ KH ∞
1 ) = 0 under the bi-interleaving distance, then maybe it
is possible to prove KH∞
1 ◦ KH ∞
1 = 1∆ without any bound on the conformal factors. However,
while completeness of the bi-interleaving distance still holds for formal reason, this strategy does
not work because Theorems 2.28 and 2.32 do not work for the bi-interleaving distance. Indeed,
when considering convolutions on both sides Kτ ◦I F ◦I Kτ , the singular support may no longer be
I-non-characteristic as the estimation Equation (2.5) may fail.

Remark 3.12. The above theorem in particular constructs sheaf quantization for topological con-
tact dynamical systems in the sense of M¨uller–Spaeth, which are contact homeomorphisms such
that the both contact Hamiltonians and the conformal factors uniformly converge [61]. However,
note that our theorem does not even require the contactomorphisms to converge to a homeomor-
phism, but rather a continuous map (and we only require the conformal factors to be uniformly
bounded).

We can also construct sheaf quantizations for Reeb flows of limits of contact forms where the
conformal factor uniformly converges.

Proposition 3.13. Let M be a closed manifold and τ : S∗M → R and τ ′
n : S∗M → R be posi-
tive Hamiltonians that define the Reeb flows for the contact forms α and α′
n. Suppose τ ′
n → τ ′
∞
uniformly. Then there exists a sheaf quantization Kτ ′
∞
1 ∈ Sh(M × M ) with

SS
∞(Kτ ′
∞
1 ) ⊆ ⋂

n≥1
 ⋃

k≥n Γ
τ ′
k
1 .

When φ
τn
1 uniformly converges under the C0-topology, K−τ ′
∞
1 ◦ Kτ ′
∞
1 = 1∆.

Now, we can easily prove the non-degeneracy of the Hofer–Shelukhin norm for cosphere bundles
S∗M . This is proved for general closed contact manifolds by Shelukhin [78].

Theorem 3.14 (Theorem 1.11 (1)). Let M be a closed manifold. Then the Hofer–Shelukhin metric
dHS,α is non-degenerate on Cont0(S∗M, ξstd).

Proof. Let φ, φ′ be contactomorphisms in the identity component such that dHS,τ (φ, φ′) = 0. Since
dHS,τ (φ, φ′) = dHS,τ (φ ◦ (φ′)−1, id) [78, Remark 6], we may assume φ′ = id. Then there exists
a sequence of contact isotopies Φn induced by the Hamiltonians Hn such that the time-1 maps
φn = φ and ∥Hn∥HS,τ → 0. By Theorem 3.9, there exists a sheaf quantization KH∞
1 ∈ Sh(M × M )
such that dτ (1∆, KH∞
1 ) = 0. By Theorem 2.35, this implies that SS(1∆) = SS(KH∞
1 ). By the
singular support estimation in Theorems 2.26 and 3.9, this means that

Γ
id ⊆ ⋂

n≥1
 ⋃

k≥n Γφk = Γ
φ.

Therefore, we can conclude that φ = id. □

Let Λ ⊆ S∗M be a Legendrian and Leg0(Λ) be the space of Legendrians that are Legendrian
isotopic to Λ. We recall from Rosen–Zhang [73] that the Chekanov–Hofer–Shelukhin norm on
Leg0(Λ) is

dCHS,α(Λ0, Λ1) = inf
H:φH
1 (Λ0)=Λ1 ∥H∥CHS,Λ,τ = inf
H:φH
1 (Λ0)=Λ1
 ∫ 1

0 sup
(x,ξ)∈φH
s (Λ) |Hs(x, ξ)/τ (x, ξ)| ds.

They proved that the distance is either non-degenerate or zero. Later, Cant [17] and Nakamura
[68] gave examples of Legendrians in certain open contact manifolds (coming from the product with

C0-RIGIDITY OF LEGENDRIANS AND COISOTROPICS VIA SHEAF QUANTIZATION 23

the symplectization of overtwisted contact manifolds) where the metric is zero. Usher [85] proved
non-degeneracy of the distance for hypertight Legendrians in hypertight contact manifolds, Hedicke
[41] proved non-degeneracy of the distance for Legendrians that do not admit positive loops, and
finally Dimitroglou Rizell–Sullivan [24] proved the case for Legendrians in closed contact manifolds.
Here, we can prove the non-degeneracy of the Chekanov–Hofer–Shelukhin norm for a special
class of closed Legendrians Λ ⊆ S∗M which admits nontrivial sheaves.

Theorem 3.15. Let Λ ⊆ S∗M be a closed connected Legendrian and suppose that ShΛ(M ) ⊋
Loc(M ) contains sheaves that are not locally constant. Then the Chekanov–Hofer–Shlukhin metric
dCHS,α is non-degenerate on Leg0(Λ).

Proof. Let Λ′ be a Legendrian that is isotopic to Λ such that d(Λ, Λ′) = 0. Then there is a
sequence of contact isotopies Φn induced by the contact Hamiltonian Hn : S∗M × I → R such that
∥Hn∥CHS,τ → 0 and the time-1 maps satisfy φn(Λ) = Λ′. Then by the isotopy extension theorem
[33, Proposition 2.41], we can replace the contact Hamiltonian function by Hn : S∗M × [0, 1] → R
such that φn(Λ) = Λ
′, ∥Hn∥HS,τ = ∥Hn∥CHS,Λ,τ → 0.

Consider F ∈ ShΛ(M ) that is not local constant. Since Λ is a connected Legendrian, by [48,
Theorem 7.2.1] the microstalk is locally constant, and thus SS∞(F ) ⊆ Λ implies that SS∞(F ) = Λ.
Since Hn → H∞ = 0, by Theorem 3.9, there exists a sheaf quantization KH∞
1 ∈ Sh(M × M ) such
that dτ (F, KH∞
1 ◦ F ) = 0. However, by Theorem 2.28, this implies that SS(F ) = SS(KH∞
1 ◦ F ). By
the singular support estimation in Theorems 2.26 and 3.9, this means that

Λ ⊆ ⋂

n≥1
 ⋃

k≥n φk(Λ) = Λ
′.

Therefore, we can conclude that Λ = Λ′. □

Remark 3.16. We expect that one could show the non-degeneracy of the Chekanov–Hofer–
Shelukhin for general closed Legendrians by considering the doubling construction Theorem 2.22,
whose endomorphism should be analogous to the subcomplex within small action windows in [24].
However, since it is hard to control the effect of the contact isotopy on the Reeb push-off Λτ
ϵ , some
additional work needs to be done, and thus in this paper we do not proceed in this direction.

4. C0-Distances and Sheaves

In this section, we will discuss the relation between the interleaving distance of sheaves and the
C0-topology of the contactomorphism group. We will prove a new sheaf quantization theorem for
any C0-small contactomorphism Theorem 1.14 (Theorem 4.12) and use it to deduce Theorems 1.1,
1.4 and 1.7 (Theorems 4.23, 4.25, 4.27 and 4.29).

4.1. Sheaf quantization of contact homeomorphisms in jet bundles. In this section, we first
prove a simple case of the result on sheaf quantizations for the C0-limits of compactly supported
contactomorphisms in the 1-jet bundles. We hope to provide the reader with some intuition on
the sheaf quantization results before going into more complicated constructions. The argument is
independent of the rest of the subsections.
We use the standard embedding J 1M ↪→ S∗(M × R) by (x, ξ, z) ↦→ (x, z; ξ, 1) to translate
the problem into a problem about certain contactomorphisms in S∗(M × R). Moreover, in this
subsection, we will only consider the standard Reeb flow defined by Tt : (x, ξ, z) ↦→ (x, ξ, z + t).
Our key observation is that, in 1-jet bundles, after suitable homotopies, the C0-norm of the
contact isotopy in the z-direction can be controlled by the C0-norm of the time-1 map. Similar
observation is also used in for example [15, Section 4.1].

24 TOMOHIRO ASANO, YUICHI IKE, CHRISTOPHER KUO, AND WENYUAN LI

Lemma 4.1. Let M be a complete Riemannian manifold and R be the standard Riemannian mani-
fold with the Euclidean metric. For any compactly supported contact isotopy φt ∈ Cont0,c(J 1M, ξstd),
the contact isotopy is homotopic to φ′
t ∈ Cont0,c(J 1M, ξstd) such that supp(φ′
t) ⊆ T ∗M × (−r, r)
and dC0,z(id, φ′
t) ≤ dC0,z(id, φ).

Proof. Since the contact isotopy is compactly supported, we may assume that dC0,z(id, φt) ≤ Rt
where Rt is a smooth function and R1 = r. Consider the contactomorphism ρr,R : T ∗M × R →
T ∗M × R, (x, ξ, z) ↦→ (x, rξ/R, rz/R). We can define the 2-parametric family of contact isotopies

φs,t = ρsRt+(1−s)r,Rt ◦ φt ◦ ρ−1
sRt+(1−s)r,Rt.

Then since dC0,z(id, φ0,t) ≤ Rt, we can conclude that dC0,z(id, φ1,t) ≤ r. In fact, φt(x, Rtξ/r, Rtz/r) ∈
T ∗M × (Rtz/r − Rt, Rtz/r + Rt), so therefore

ρr,Rt ◦ φt ◦ ρ−1
r,Rt(x, ξ, z) ∈ T ∗M × (z − r, z + r).

This then completes the proof. □

Using the above lemma, we can prove the C0-continuity of the interleaving distance between
sheaf kernels of the contactomorphisms in the identity component.
For a compactly supported contact isotopy Φ : J 1M × I → J 1M , it extends to a contact isotopy
Φ : S∗(M ×R)×I → S∗(M ×R), and thus there exists a canonical sheaf quantization by Theorem 2.4.
The Reeb flow Tt : J 1M × I → J 1M is not compactly supported and does not extend to S∗(M × R).
Nevertheless, one can set the sheaf quantization to be

Tt := 1∆M ×{(z1,z2)|0<z2−z1<t}[1].

For any F ∈ Shζ>0(M × Rz), we know that Tt ◦ SS∞(F ) = Tt(SS
∞(F )).
11

Proposition 4.2. Let M be a complete Riemannian manifold and R be the standard Riemannian
manifold with the Euclidean metric. Then for any compactly supported φ ∈ Cont0,c(J 1M, ξstd), the
sheaf quantization Kφ satisfies the relation that dτ (1∆, Kφ) ≤ 2 dC0(id, φ).

Proof. Consider a contactomorphism φ such that dC0(id, φ) ≤ ϵ. We show that there are canonical
morphisms whose compositions

T−ϵ → Kφ → Tϵ, T−ϵ ◦ Kφ → 1∆ → Tϵ ◦ Kφ

are equivalent to the continuation morphisms. In fact, by Theorem 4.1, we may assume that φ is
induced by a contact isotopy φt such that dC0,z(id, φ) ≤ ϵ. Then we know that ΓΦ
t ∩ ΓT
±ϵ = ∅, in
other words SS∞(KΦ
t ) ∩ SS
∞(T±ϵ) ∩ S∗
ζ>0(M × R) = ∅, and SS
∞(KΦ
t ) ∩ S∗
ζ≤0(M × R) is a constant
family. Thus, SS∞(KΦ
t ) ∩ SS
∞(T±ϵ) defines a compactly supported Legendrian isotopy. It follows
from Theorem 2.4 that
 Hom(Kφ, Tϵ) = Hom(1∆, Tϵ) = Γ(M, 1M ),

Hom(T−ϵ, Kφ) = Hom(T−ϵ, 1∆) = Γ(M, 1M ).

This ensures that there exist morphisms such that the compositions are equivalent to continuation
morphisms, and thus dτ (1∆, Kφ) ≤ 2ϵ. □

Proposition 4.3. Let φn ∈ Cont0,c(J 1M, ξstd) be compactly supported contactomorphisms such
that φn → φ∞ in the C0-topology where φ∞ is a homeomorphism. Then there is a functor

Kφ∞ : ShΛ(M × R) → Shφ∞(Λ)(M × R)

such that Kφn converges to Kφ∞.

11The sheaf kernels are not uniquely determined by the above condition, but they are unique in the localization.
For instance, by composing with the microlocal kernel Theorem 2.18 Pζ : Sh(M × Rz) → Shζ≥0(M × Rz), the sheaf
kernel 1∆M ×{(z1,z2)|0<z2−z1<t} can be identified with the sheaf kernel 1∆M ×{(z1,z2)|z2−z1<t}.

C0-RIGIDITY OF LEGENDRIANS AND COISOTROPICS VIA SHEAF QUANTIZATION 25

Proof. Without loss of generality, we may assume that dC0(φn, φn+1) ≤ ϵn and ∑∞
n=1 ϵn < +∞.
Since φn is a diffeomorphism, we know dC0(φn ◦ φ−1
n+1, id) = dC0(φn, φn+1) ≤ ϵn. By Theorem 4.2,
we know that there exist morphisms

Kτ
−ϵn ◦ Kφ
−1
n ◦φn+1 → 1∆ → Kτ
ϵn ◦ Kφ
−1
n ◦φn+1, Kτ
−ϵn → Kφ−1
n ◦φn+1 → Kτ
ϵn
whose compositions are the natural continuation morphisms. Then, we know that there exist
morphisms
 Kτn
−ϵn ◦ Kφn+1 → Kφn → Kτn
ϵn ◦ Kφn+1,

Kτn
−ϵn ◦ Kφn → Kφn+1 → Kτn
ϵn ◦ Kφn

whose compositions are the natural continuation morphisms. Then, we know that Kφn form a
Cauchy sequence and by Theorem 2.30, Kφn converges to a sheaf Kφ∞ under the interleaving
distance. Finally, by Theorem 2.26, we have

SS
∞(Kφ∞ ◦ F ) ⊆ ⋂

n≥0
 ⋃

k≥n SS
∞(Kφk ◦ F ) = ⋂

n≥0
 ⋃

k≥n φk(SS
∞(F )) = φ∞(SS
∞(F )).

This completes the proof. □

4.2. Sheaf quantization of nearby Legendrians with no chords. We generalize the sheaf
quantization result of Guillermou [37] for closed Legendrians in the 1-jet bundle with no Reeb
chords (equivalently, closed exact Lagrangians in the cotangent bundles) in Theorems 4.6 and 4.7.
In this section, we follow Theorem 2.21.
We will also need a generalization to certain non-compact Legendrians, following [57, 7]. There-
fore, we will consider a complete Riemannian metric on the manifold M , which induces a complete
Riemannian metric on S∗M . We will take the standard contact form αstd on S∗M induced by the
Riemannian metric and all the contact Hamiltonian functions are the Hamiltonian with respect to
this standard contact form αstd.

Definition 4.4. Let M be a complete Riemannian manifold and Λ ⊆ S∗
ζ>0(M × R) be a properly
embedded Legendrian. Then for a bounded positive contact Hamiltonian τ in Theorem 2.14, the
associated contact flow on S∗
ζ>0(M × R) is called a separating Reeb flow for Λ if there is s > 0
such that Λ and Λτ
s are separated by a hypersurface T ∗M × a, and ⋃ϵ<t<s Λτ
t is disjoint from some
tubular neighborhood of Λ with positive radius, for some ϵ > 0.

Lemma 4.5. Let M be a complete Riemannian manifold, Λ ⊆ S∗
ζ>0(M ×R) be a properly embedded
Legendrian and τ be a C1-bounded positive Hamiltonian defining the separating Reeb flow for Λ.
Then there exists a cut-off function ρ on a tubular neighborhood of Λ such that (1 − ρ)τ defines a
complete contact flow and sends Λ ∪ Λτ
ϵ to Λ ∪ Λτ
s .

Proof. Consider the tubular neighborhood of Λ of positive radius with respect to the Riemannian
metric that is disjoint from ⋃ϵ<t<s Λτ
t . We can choose a cut-off function ρ supported in the tubular
neighborhood such that |dρ| is uniformly bounded. Then since |(1 − ρ)τ | ≤ |τ | and |d((1 − ρ)τ )| ≤
|τ ||dρ| + |dτ | are both uniformly bounded, the norm of the contact vector field X(1−ρ)τ is uniformly
bounded and therefore defines a complete contact flow. □

We can now state the following theorem, which generalizes of Guillermou’s results to the non-
compact setting when there exists a separating Reeb flow.

Theorem 4.6 (Guillermou [37, Corollaries 12.3.2 & 12.3.3, Theorems 12.4.3 & 12.4.4]). Let M be
a complete Riemannian manifold and Λ ⊆ S∗
ζ>0(M × (−a, b)) be a properly embedded Legendrian
with no Reeb chords with respect to some separating Reeb flow. Then there exists a fully faithful
embedding where the second functor is give by restriction at +∞

ΨΛ,∞ : µshΛ(Λ) ΨΛ
↪−−→ ShΛ(M × R)0 i∗
∞
↪−→ Loc(M ),

26 TOMOHIRO ASANO, YUICHI IKE, CHRISTOPHER KUO, AND WENYUAN LI

where ShΛ(M × R)0 is the subcategory of sheaves with trivial stalks at −∞.

Proof. First, by Theorem 2.22, we know that for sufficiently small ϵ > 0, there exists a fully faithful
embedding wΛ : µshΛ(Λ) ↪→ ShΛ∪Λτ
ϵ (M × R)0.

Consider the separating Reeb flow for Λ defined by τ . Using Theorem 4.5, we know there is a
cut-off function ρ supported in the tubular neighborhood and (1 − ρ)τ defines a complete contact
flow that sends Λ ∪ Λτ
ϵ to Λ ∪ Λτ
s . By the sheaf quantization of Guillermou–Kashiwara–Schapira
Theorem 2.4, we have

wΛ,s : µshΛ(Λ) ↪→ ShΛ∪Λτ
ϵ (M × R)0 ∼
−→ ShΛ∪Λτ
s (M × R)0.

Since Λ and Λτ
s are separated by a hypersurface T ∗M × a, we can restrict the sheaf to M × (−∞, a),
push-forward to M × (−∞, +∞) via a diffeomorphism and then restrict to M × ∞. This gives the
functor ShΛ∪Λτ
s (M × R)0 → ShΛ(M × R)0 → Loc(M ).

Full faithfulness of the functor will follow from perturbation of Λ by the separating Reeb flow
and microlocal Morse lemma. First, consider sheaves wΛ,ϵF, wΛ,ϵG ∈ ShΛ∪Λτ
ϵ (M × R)0. Denote
their images in ShΛ(M × R)0 by F and G. We can use the Reeb flow φs
(1−ρ)τ to perturb wΛ,ϵG by
Theorem 2.16 and apply microlocal Morse lemma. This implies

Hom(wΛ,ϵF, wΛ,ϵG) = Hom(wΛ,ϵF, wΛ,sG) ≃ Hom(wΛ,ϵF |(−∞,a), wΛ,sG|(−∞,a))

= Hom(wΛ,ϵF |(−∞,a), ΨΛG|(−∞,a)) = Hom(wΛ,ϵF, ΨΛG).

Then we can apply the Reeb flow φs
(1−ρ)τ to perturb wΛ,ϵF and G by Theorem 2.4 and apply
microlocal Morse lemma again. This implies

Hom(wΛ,ϵF, ΨΛG) = Hom(wΛ,sF, ΨΛG) ≃ Hom(wΛ,sF |(−∞,a), ΨΛG|(−∞,a))

= Hom(ΨΛF |(−∞,a), ΨΛG|(−∞,a)) = Hom(ΨΛF, ΨΛG).

This implies full faithfulness of ShΛ∪Λτ
s (M × R)0 → ShΛ(M × R)0. Then, we consider the Reeb flow
φτ
s by Theorem 2.16 and apply the microlocal Morse lemma to ΨΛF, ΨΛG ∈ ShΛ(M × R)0. Denote
their images in Loc(M ) by ΨΛ,∞F and ΨΛ,∞G. This implies

Hom(ΨΛF, ΨΛG) = Hom(ΨΛF, Kτ
s ◦ ΨΛG) ≃ Hom(ΨΛF |(a,+∞), Kτ
s ◦ ΨΛG|(a,+∞))

= Hom(ΨΛ,∞F ⊠ 1R, ΨΛG) ≃ Hom(ΨΛ,∞F ⊠ 1R|(a,+∞), ΨΛG|(a,+∞))

= Hom(ΨΛ,∞F, ΨΛ,∞G).

This implies the full faithfulness of ShΛ(M × R)0 → Loc(M ). Finally, we show that it preserves
microlstalks using [37, Theorem 13.5.1] and [45, Corollary 1.3]. □

Given the above theorem, the following corollary immediately follows from exactly the same
argument as in Guillermou [37] and Jin [45]:

Theorem 4.7 (Guillermou [37, Theorem 13.5.1, Proposition 13.5.2 & Corollary 13.5.3], Jin [45,
Corollary 1.3]). Let M be a complete Riemannian manifold and Λ ⊆ S∗
ζ>0(M ×(−a, b)) be a properly
embedded Legendrian with no Reeb chords for some separating Reeb flow. Then the Maslov data of
Λ is trivial, and there is an equivalence that preserves stalks

ΨΛ,∞ : Loc(Λ) ∼
−→ ShΛ(M × R)0 ∼
−→ Loc(M ).

In particular, the projection Λ → M is a homotopy equivalence and there exists a unique sheaf
F ∈ ShΛ(M × R) such that
(1) supp(F ) ⊆ M × (−a, +∞), SS
∞(F ) = Λ;

C0-RIGIDITY OF LEGENDRIANS AND COISOTROPICS VIA SHEAF QUANTIZATION 27

(2) mΛ(F ) = 1Λ and i∗
M ×bF = 1M for b ≫ 0.12

Remark 4.8. We remind the reader how the argument works. First, we show that Λ → M is π1-
injective by [37, Proposition 13.1.1]. Second, we show that the Maslov class is zero by [37, Theorem
13.2.1]. Third, we show that for C = Mod(k), the functor µshΛ(Λ) → Loc(M ) sends simple local
systems to simple local systems and thus π : Λ → M induces isomorphisms on cohomology by
[37, Proposition 13.3.1]. Next, we can show that the second Stiefel–Whitney class is zero [37,
Proposition 13.4.2]. This implies that when C = Mod(k), the functor Loc(Λ) → Loc(M ) is an
equivalence [37, Proposition 13.5.2], and thus Λ → M is a homotopy equivalence. Then, since
Λ → M is a homotopy equivalence, we can apply the argument in [45, Corollary 1.3] and conclude
that the Maslov data is trivial and Loc(Λ) → Loc(M ) is an equivalence over any coefficients.

Remark 4.9. Unlike the case when M is compact, it is not true that any embedded Legendrian L ⊆
S∗
ζ>0(M × R) with no Reeb chords admits a separating Reeb flow. For instance, most non-compact
embedded Legendrians considered in [57, Section 2 & 3] with no Reeb chords have no separating
Reeb flows. (While one can construct a separating Legendrian isotopy for those Legendrians with no
Reeb chords, the Legendrian isotopy may not extend to a contact isotopy due to non-compactness,
and even when it extends to a contact isotopy, it is in general not separating [57, Section 2 & 3].)

The following corollary of Guillermou’s result is also well known to experts. Here, we use the
isomorphism π∗ : Loc(Λ) → Loc(M ) given by the natural projection π : Λ → M , which is a homo-
topy equivalence by Abouzaid–Kragh [49] and Guillermou [37] for compact M , and is extended in
the above result for non-compact M when there exists a separating Reeb flow.

Corollary 4.10. Let Λ ⊆ S∗
ζ>0(M × (−a, b)) be a properly embedded Legendrian with no Reeb
chords for some separating Reeb flow defined by τ . Then there exists Cτ such that for any local
system L ∈ Loc(Λ) ≃ Loc(M ), the sheaf quantizations (ΨΛL, Ψ0M L) are (Cτ a, Cτ b)-interleaved,
and thus dτ (ΨΛL, Ψ0M L) ≤ Cτ (a + b).
Moreover, we can choose the continuation morphisms which under i∗
∞ restrict to the identity mor-
phism L → L.

Proof. First, using Theorem 4.7 (1) & (2), we know ΨΛL|M ×[b,+∞) = L⊠1[b,+∞), ΨΛL|M ×(−∞,−a] =
0. Let Tt : S∗
ζ>0(M × R) → S∗
ζ>0(M × R) be the Reeb flow given by the vertical push-off. We will
first estimate the distance in terms of the Reeb flow Tt and then deduce the estimation in terms
of our separating Reeb flow φτ
t . Since Λ and 0M ⊆ S∗
ζ>0(M × R), we can apply microlocal Morse
lemma and show that

Hom(T−a ◦ Ψ0M L, ΨΛL) = Hom(ΨΛL, Tb ◦ Ψ0M L) = Hom(L, L).

Since the full faithfulness in Theorem 4.7 implies that Hom(ΨΛL, ΨΛL) = Hom(L, L), we can
conclude that there exist morphisms

T−a ◦ Ψ0M L → ΨΛL → Tb ◦ Ψ0M L, T−b ◦ ΨΛL → Ψ0M L → Ta ◦ ΨΛL

whose compositions are the natural continuation maps, and the restrictions under the functor i∗
∞
are the identity morphisms L → L.
Let Cτ > 0 be the lower bound of the bounded contact Hamiltonian τ as in Theorem 2.14. Then
we have natural continuation morphisms Kτ
−Cτ s → T−s and Ts → Kτ
Cτ s for any s > 0. Hence there
exist morphisms

Kτ
−Cτ a ◦ Ψ0M L → ΨΛL → Kτ
Cτ b ◦ Ψ0M L, Kτ
−Cτ b ◦ ΨΛL → Ψ0M L → Kτ
Cτ a ◦ ΨΛL

12We fix the Maslov data on Λ that is the pull-back of the Maslov data on the diagonal M via the natural
projection map (which is known to be a homotopy equivalence).

28 TOMOHIRO ASANO, YUICHI IKE, CHRISTOPHER KUO, AND WENYUAN LI

whose compositions are the continuation morphisms, and the restrictions under the functor i∗
∞ are
the identity morphisms L → L. This completes the proof. □

4.3. Sheaf quantization of C0-small contactomorphisms. Using the sheaf quantization the-
orem on nearby Legendrians Theorems 4.6 and 4.7, we prove the sheaf quantization theorem for
any C0-small contactomorphisms and deduce the interleaving distance estimation in Theorem 4.18
(Theorem 1.14).
Let φ : S∗M → S∗M be a contactomorphism such that φ∗α = ehα. Recall it follows from
Theorem 2.3 that the graph of the contactomorphism to be the Legendrian submanifold

Γ
φ = {(x, ξ, y, η) | (y, η/|η|) = φ(x, ξ/|ξ|), |ξ|/|η| = eh(x,ξ/|ξ|)} ⊆ S∗(M × M ).

The natural projection π : S∗(M × M ) → M × M sends (x, ξ, y, η) to (x, y), so it factors through
the projection S∗M × S∗M → M × M . In particular, when the C0-distance between two contac-
tomorphisms are small, the C0-distance of the projections of their graphs are also small.
Following Theorem 2.14, we will fix a bounded Reeb flow defined by the positive Hamiltonian
τ : S∗M → R. Given Theorem 2.36, we will fix a bounded Reeb flow defined by the contact Hamil-
tonian τ and the cut-off function ρ : S∗(M × M ) → R so that the Hamiltonian (1 − ρ)τ2 : S∗(M ×
M ) → R defines a complete contact flow.

Lemma 4.11. Let M be a complete Riemannian manifold, α be a contact form on S∗M and
τ : S∗M → R be a positive Hamiltonian that defines the bounded Reeb flow for α such that there
are no closed Reeb orbits of length less than ϵ. Let φ : S∗M → S∗M be any injective map. Then
the graph Γφ ⊆ S∗(M × M ) has no chords of length less than ϵ with respect to the contact flow of
the non-negative Hamiltonian τ2.

Proof. We know that Γφ is disjoint from 0M × S∗M . Consider the chords on Γφ with respect to the
contact Hamiltonian τ2 = (1 − ρ)τ2 on the complement of the tubular neighborhood of S∗M × 0M .
They are determined by the equations

(yi, ηi/|ηi|) = φ(xi, ξi/|ξi|), (x2, ξ2/|ξ2|) = (x1, ξ1/|ξ1|), (y2, η2/|η2|) = φτ
s (y1, η1/|η1|), .

Then we get the equality (y1, η1/|η1|) = φτ
s (y1, η1/|η1|). We know that φτ
s has no Reeb orbits of
length less than ϵ by assumption, so Γφ has no chords of length less than ϵ with respect to φτ2
s ,
defined as a contact flow on S∗(M × M ) \ 0M × S∗M . □

Given the above lemma that the graph of a contactomorphism have no short Reeb chords, we
can prove the following theorem, which is the main technical result in this paper.

Theorem 4.12 (Theorem 1.14). Let M be a complete Riemannian manifold, α be a contact form
on S∗M and τ : S∗M → R be a positive Hamiltonian that defines a bounded Reeb flow for α. Then
for any ϵ > 0 sufficiently small and any φ ∈ Cont(S∗M, ξstd) with dC0(id, φ) ≤ ϵ, there exists a
unique sheaf quantization Kφ of φ such that for some tubular neighborhood U2ϵ of ∆ with radius
2ϵ, (1) supp(Kφ) ⊆ U2ϵ, SS
∞(Kφ) ⊆ Γφ;
(2) mΓφ(Kφ) = 1Γφ ∈ Loc(Γφ).
Moreover, there is some constant Cτ such that dτ (1∆, Kφ) ≤ 2Cτ dC0(id, φ).

Proof. Let T ∗
∆(M × M ) be the conormal bundle of the diagonal and T ∗
∆,<r(M × M ) be the subset of
the conormal consisting of conormal vectors of norm less than r. Since the Reeb flow is bounded,
without loss of generality, we can assume that for sufficiently small ϵ > 0, the Reeb push-off of the
conormal of the diagonal

Φτ2 : T ∗
∆,<2ϵ(M × M ) ↪→ M × M, (x, −ξ, x, ξ) ↦→ (x, π ◦ φτ
1(x, ξ))

C0-RIGIDITY OF LEGENDRIANS AND COISOTROPICS VIA SHEAF QUANTIZATION 29

Figure 1. Construction of the sheaf quantization for a small contactomorphism φ
in Theorem 4.12 when M = R. Here, the blue curves are the projections of the
graphs Γid and Γτ
ϵ while the black curves is the projection of the graph Γφτ
ϵ ◦φ.

defines an embedding. Write U2ϵ = Φτ2(T ∗
∆,<2ϵ(M × M )), U ◦
2ϵ = Φτ2(T ∗
∆,<2ϵ(M × M ) \ ∆) and
Sϵ = Φτ2(T ∗
∆,ϵ(M × M )). We have a diffeomorphism U ◦
2ϵ ∼= Sϵ × (−ϵ, ϵ).
Let C1 > 0 be the lower bound on the norm of the vector field ∂z along the coordinate z ∈ (−ϵ, ϵ).
Consider δ > 0 such that δ/ϵ = C1/2. Let φ be a contactomorphism such that dC0(id, φ) ≤ δ.
Consider the contactomorphism φτ
ϵ ◦ φ. We have dC0(φτ
ϵ , φτ
ϵ ◦ φ) ≤ C1ϵ. Since the projections
Γφτ
ϵ → M × M and Γφτ
ϵ ◦φ → M × M factor through S∗M × S∗M , the distance of the projections of
the graphs in M × M is bounded by their distance in S∗M × S∗M which is at most C1ϵ. Therefore,
we can assume that Γ
φτ
ϵ ◦φ ⊆ S∗(Sϵ × (−ϵ, ϵ)) ∼= S∗U ◦
2ϵ.
Since dC0(φτ
ϵ , φτ
ϵ ◦ φ) < ϵ, and for any (x, ξ, y, η) ∈ Γτ
ϵ , ⟨η, ∂z⟩y > 0, we may assume that for any
(x, ξ, y, η) ∈ Γφτ
ϵ ◦φ, ⟨(ξ, η), ∂z⟩(x,y) = ⟨η, ∂z⟩y > 0. Thus,

Γ
φτ
ϵ ◦φ ⊆ S∗
ζ>0(Sϵ × (−ϵ, ϵ)z) ∼= S∗
ζ>0U ◦
2ϵ.

By Theorem 4.11, we know that Γφτ
ϵ ◦φ has no chords of length less than 2ϵ with respect to the
contact flow φτ2
t . For 0 < ϵ′ < ϵ, since the projection of Γφτ
ϵ ◦φ and Γφτ
ϵ′ ◦φ are contained in small
neighborhoods of Sϵ and Sϵ′, we can assume that the graphs Γφτ
ϵ ◦φ and Γφτ
ϵ′ ◦φ are separated by
a hypersurface Sϵ′′. Then Theorem 4.7 implies that there exists a unique sheaf Kφτ
ϵ ◦φ
U ◦
2ϵ ∈ Sh(U ◦
2ϵ)
such that for some sufficiently small ϵ′ < ϵ,

(1) supp(Kφτ
ϵ ◦φ
U ◦
2ϵ ) ⊆ U ◦
2ϵ−ϵ′, SS∞(Kφτ
ϵ ◦φ
U ◦
2ϵ ) ⊆ Γφτ
ϵ ◦φ;

(2) mΓφτ
ϵ ◦φ(Kφτ
ϵ ◦φ
U ◦
2ϵ ) = 1Γφτ
ϵ ◦φ and i∗
Sϵ′ Kφτ
ϵ ◦φ
U ◦
2ϵ = 1Sϵ′ .

Then since the restriction functor Loc(Uϵ′) → Loc(Sϵ′) is conservative, there exists a unique exten-
sion Kφτ
ϵ ◦φ ∈ Sh(M × M ) such that

i∗
U ◦
2ϵKφτ
ϵ ◦φ = Kφϵ
τ ◦φ
U ◦
2ϵ , i
∗
Uϵ′ Kφτ
ϵ ◦φ = 1Uϵ′ .

We define Kφ := Kτ
−ϵ ◦ Kφτ
ϵ ◦φ. We can conclude by Theorem 2.2 that this is the unique sheaf in
Sh(M × M ) such that

supp(Kφ) ⊆ U2ϵ, SS
∞(Kφ) ⊆ Γ
φ, mΓφ(Kφ) = 1Γφ ∈ Loc(Γ
φ).

Finally, we estimate the interleaving distance. We know that Φτ2 : T ∗
∆,<2ϵ(M × M ) ↪→ M × M
defines an embedding, so the Reeb vector field defined by the Riemannian metric is bounded by the
Reeb vector field ∂z defined by the contact form on the 1-jet bundle S∗
ζ>0U ◦
2ϵ. Then the Reeb flow
defined by τ is bounded with respect to the standard contact form on the 1-jet bundle S∗
ζ>0U ◦
2ϵ.

30 TOMOHIRO ASANO, YUICHI IKE, CHRISTOPHER KUO, AND WENYUAN LI

Let C2 > 0 be the lower bound of the bounded contact Hamiltonian τ with respect to the standard
contact form on S∗
ζ>0U ◦
2ϵ. First, by Theorem 4.10, we know that there exists C2 > 0 such that

the sheaf quantizations (1U ◦
ϵ , Kφτ
ϵ ◦φ
U ◦
2ϵ ) are (C2a, C2b)-interleaved for some a, b < ϵ. Moreover, by
Theorem 4.10, the restrictions of the continuation morphisms to Sϵ−C2b are the identity. Then, by
the construction of the sheaf quantization Kφτ
ϵ ◦φ, there exist morphisms

Kτ
ϵ−C2a → Kφτ
ϵ ◦φ → Kτ
ϵ+C2b, Kτ
−ϵ−C2b ◦ Kφτ
ϵ ◦φ → Kτ
−ϵ → Kτ
−ϵ+C2a ◦ Kφτ
ϵ ◦φ

whose compositions are the continuation morphisms. Define Kφ := Kτ
−ϵ ◦ Kφτ
ϵ ◦φ, then we have
morphisms Kτ
−C2a → Kφ → Kτ
C2b, Kτ
−C2b ◦ Kφ → 1∆ → Kτ
C2a ◦ Kφ

whose the compositions are the continuation morphisms. Therefore, since a, b < ϵ and δ/ϵ = C1/2,
we can set Cτ = 2C2/C1 and thus dτ (1∆, Kφ) ≤ 2Cτ dC0(id, φ). This concludes the proof. □

Now, we will show that such sheaf quantizations for C0-small contactomorphisms are functorial
with respect to compositions:

Proposition 4.13. Let M be a complete Riemannian manifold and α be a contact form on S∗M .
Then for the ϵ > 0 specified in Theorem 4.12 and any φ, φ′ ∈ Cont(S∗M, ξstd), each of which
has bounded conformal factor, such that dC0(id, φ) + dC0(id, φ′) ≤ ϵ, the sheaf quantizations in
Theorem 4.12 satisfy the relation Kφ ◦ Kφ′ = Kφ◦φ′.

In particular, Kφ is an invertible sheaf kernel with inverse Kφ−1 if dC0(id, φ) ≤ ϵ/2.

Proof. First, by the singular support estimation Theorem 2.2, we know that

supp(Kφ ◦ Kφ′) ⊆ U2ϵ, SS
∞(Kφ ◦ Kφ′) ⊆ Γφ◦φ′.

By the invariance of microstalks under contact transformation [48, Theorem 7.5.11], we can compute
that mΓφ◦φ′ (Kφ ◦Kφ′) is a rank 1 local system. Then, by Theorem 4.10, for sufficiently small ϵ′ > 0,
the restriction Kτ
ϵ ◦ Kφ ◦ Kφ′|Sϵ′ is also a rank 1 local system. However, since the assumption
dC0(id, φ) + dC0(id, φ′) ≤ ϵ, it follows from Theorem 4.12 that

dτ (1∆, Kφ ◦ Kφ′) ≤ dτ (1∆, Kφ′) + dτ (Kφ′, Kφ ◦ Kφ′) = dτ (1∆, Kφ′) + dτ (1∆, Kφ) ≤ 2Cτ ϵ.

In particular, for sufficiently small ϵ′ > 0, Hom(Kτ
ϵ′, Kτ
ϵ ◦ Kφ ◦ Kφ′) ̸= 0. This forces the restriction
Kτ
ϵ ◦ Kφ ◦ Kφ′|Uϵ′ to be the constant local system 1Uϵ′ . Thus, by Theorem 4.10, it follows that

mΓφ◦φ′ (Kφ ◦ Kφ′) = 1Γφ◦φ′ .

Then, the uniqueness statement in Theorem 4.12 implies that Kφ◦φ′ = Kφ ◦ Kφ′. □

For a given contactomorphism φ ∈ Cont0(S∗M, ξstd) in the identity component, we can take a
contact isotopy φt ∈ Cont0(S∗M, ξstd) such that φ0 = id and φ1 = φ and then apply Theorem 2.4 to
get a sheaf quantization Kφ of φ. We remark that given a contactomorphism φ ∈ Cont0(S∗M, ξstd),
it is not true that there is a unique contact isotopy φt ∈ Cont0(S∗M, ξstd) connecting id and φ.
Therefore, the sheaf quantization of contact isotopies by Guillermou–Kashiwara–Schapira does
not give a unique sheaf quantization of the contactomorphism φ ∈ Cont0(S∗M, ξstd) (actually,
the sheaf quantization of Guillermou–Kashiwara–Schapira is defined on the universal cover of
Cont0(S∗M, ξstd)). However, we are able to prove the weaker result:

Proposition 4.14. Let Φ be a contact isotopy such that φ0 = id, φ1 = φ and dC0(id, φt) ≤ ϵ for
any t ∈ I. For the sheaf quantization KΦ ∈ Sh(M × M × I) induced by Guillermou–Kashiwara–
Schapira Theorem 2.4, Kφ = KΦ
1 is isomorphic to the sheaf quantization of φ in Theorem 4.12.

C0-RIGIDITY OF LEGENDRIANS AND COISOTROPICS VIA SHEAF QUANTIZATION 31

Proof. Consider the sheaf quantization KΦ ∈ Sh(M × M × I) in Theorem 2.4. We know by
Theorem 2.2 that SS
∞(KΦ) ⊆ ΓΦ. First, this implies that SS
∞(KΦ
1 ) ⊆ Γφ. Next, since dC0(id, Φ) ≤
ϵ, we know that SS
∞(KΦ) ⊆ S∗(Uϵ × I). This means that KΦ|(M ×M \Uϵ)×I is a constant sheaf.
Since KΦ|(M ×M \Uϵ)×0 = 0, we have KΦ|(M ×M \Uϵ)×1 = 0. Hence we get

supp(KΦ
1 ) ⊆ Uϵ.

Finally, consider the microlocalization mΓΦ(KΦ) ∈ Loc(ΓΦ). Since the restriction at 0 is the
constant sheaf 1S∗∆ ∈ Loc(S∗∆), the restriction at 1 is also the constant sheaf:

mΓφ(KΦ
1 ) = 1Γφ.

Thus, we can simply apply the uniqueness statement Theorem 4.12 to deduce the result. □

Example 4.15. Let M = S1 and consider the contactomorphism φt : S∗M → S∗M, (x, ξ) ↦→
(x+t, ξ). Then φn is the identity contactomorphism for any n ∈ N. However, the sheaf quantization
by Theorem 2.4 gives different sheaf quantizations Kφn = π!1U n(∆) where π : R × R → S1 × S1 is
the projection and U n(∆) = {(x, y) | |x − y| ≤ n} ⊆ R2. Indeed, we need ϵ < 1/2 for this case.

4.4. Sheaf quantization of contact homeomorphisms. We now prove the results on the invari-
ance of categories of sheaves under contact homeomorphisms, which are limits of contactomorphisms
under the C0-topology in Theorems 4.18 and 4.21 (Theorem 1.7).
For a contact homeomorphism, the graph is not usually well defined due to the issue that the
conformal factors do not converge. However, we can define the pseudo-graph to be a closed subset
in S∗(M × M ) as follows:

Definition 4.16. Let φ : S∗M → S∗M be a homeomorphism. Then we define the pseudo-graph
of φ as the following subset

Γ
φ
pseudo = {(x, ξ, y, η) | (y, η/|η|) = φ(x, ξ/|ξ|)} ⊆ S∗(M × M ).

In other words, it is the image of Γφ × R ⊆ S∗M × S∗M × R under the open embedding

S∗M × S∗M × R ↪→ S∗(M × M )

((x, ξ), (y, η), t) ↦→ (x, y, e
tξ, e
−tη),

whose image is S∗(M × M ) \ (0M × S∗M ∪ S∗M × 0M ).

Warning 4.17. Although the name suggests, the pseudo-graph does not become a graph even
when the conformal factors converges. Without a well-defined conformal factor, a contact homeo-
morphism does not lift to a homogeneous map ˙T ∗M → ˙T ∗M . Therefore, it does not make sense to
define a half-dimensional graph in ˙T ∗(M × M ). Indeed, the pseudo-graph is one dimension higher,
and fits into a natural fibration Γ
φ
pseudo → Γφ whose fiber is R.

We now state the sheaf quantization theorem for contact homeomorphisms. We will take the
standard contact form αstd on S∗M induced by the complete Riemannian metric and all the contact
Hamiltonian functions are the Hamiltonian with respect to this standard contact form αstd.

Theorem 4.18. Let φn ∈ Cont(S∗M, ξstd) be contactomorphisms such that dC0(id, φn) < ϵ/2,
where ϵ > 0 is sufficiently small so that Theorem 4.12 holds. Then for a bounded Reeb flow defined
by τ under the standard contact form, the sheaf quantizations Kφn converge under the interleaving
distance to a sheaf quantization Kφ∞ of φ∞ such that

SS
∞(Kφ∞) ⊆ Γ
φ∞
pseudo
and for any F ∈ Sh(M ), SS
∞(Kφ∞ ◦ F ) ⊆ φ∞(SS
∞(F )). If the conformal factors hn are uniformly
bounded, then SS
∞(Kφ∞) ⊆ Γφ∞
pseudo.

Moreover, there exists Cτ > 0 such that dτ (1∆, Kφ∞) ≤ 2Cτ dC0(id, φ∞).

32 TOMOHIRO ASANO, YUICHI IKE, CHRISTOPHER KUO, AND WENYUAN LI

Proof. Without loss of generality, we assume that dC0(φn, φn+1) ≤ ϵn and ∑∞
n=1 ϵn < ∞. Since φn
is a diffeomorphism, we know dC0(φn ◦ φ
−1
n+1, id) = dC0(φn, φn+1) ≤ ϵn. Using Theorem 4.12 and
Theorem 4.13, we know that there exist morphisms

Kτ
−Cτ ϵn ◦ Kφn+1 → Kφn → Kτ
Cτ ϵn ◦ Kφn+1, Kτ
−Cτ ϵn ◦ Kφn → Kφn+1 → Kτ
Cτ ϵn ◦ Kφn

whose compositions are the natural continuation morphisms. Then, we know that (Kφn)n≥N form
a Cauchy sequence, and by Theorem 2.30 it converges under the interleaving distance to a sheaf
kernel Kφ∞. By Theorem 2.26, we have

SS
∞(Kφ∞) ⊆ ⋂
n≥0
 ⋃

k≥n SS
∞(Kφk ) = ⋂
n≥0
 ⋃

k≥n Γφk ⊆ Γ
φ∞
pseudo.

The result SS∞(Kφ∞ ◦ F ) ⊆ φ∞(SS
∞(F )) follows from the estimation Theorem 2.26 and the fact
that φn → φ∞. If the conformal factors are pointwise uniformly bounded, say −h ≤ hn(x, ξ) ≤ h
for all n ∈ N and (x, ξ) ∈ S∗M , we have

SS
∞(Kφ∞) ⊆ {(x, ξ, y, η) | (y, η/|η|) = φ∞(x, ξ/|ξ|), |ξ|/|η| ∈ [e
−h, e
h]} ⊆ Γ
φ∞
pseudo.

This completes the proof of the singular support estimation. Finally, for the distance estimation,
we apply Theorem 4.12 and get dτ (1∆, Kφn) ≤ 2Cτ dC0(id, φn). Thus, since Kφn → Kφ∞, we can
conclude that dτ (1∆, Kφ∞) ≤ 2Cτ dC0(id, φ∞). □

We explain in the following example why considering the pseudo-graph is necessary for sheaf
quantizations of contact homeomorphisms.

Example 4.19. Let M = R. Consider a sequence of smooth increasing functions fn : R → R that
converges to f∞(x) = x2sign(x). Then the sequence of contactomorphisms φn(x, ξ) = (fn(x), ξ)
converges to the homeomorphism
 φ∞(x, ξ) = (x2sign(x), ξ).

One can show that conformal factors of φn are unbounded near x = 0. Moreover, since φn and φ∞
are induced by the homeomorphisms fn and f∞(x) = x2sign(x), the sheaf quantization of φ∞ is

Kφn = 1Γfn , Kφ∞ = 1Γf∞ .

In particular, the limit of the graphs of φn does not define a section of the fibration Γφ∞
pseudo → Γφ∞,
and indeed
SS
∞(Kφ∞) ∩ S∗
(0,0)R2 = Γφ∞
pseudo ∩ S∗
(0,0)R2 = {(0, 0, ξ, η) | sign(ξ) = sign(η)}.

More generally, for M = N × R, one can consider the example of Usher [85, Section 5.2] of the
contact homeomorphism φ∞ : S∗(N × R) → S∗(N × R) where it is defined by the time-1 flow of the
smooth Hamiltonian on S∗(N × R) \ S∗
N ×0(N × R), and extends only continuously to S∗
N ×0(N × R),
and see that limit of the graphs of φn does not define a section of the fibration Γφ∞
pseudo → Γφ∞.

Showing that the sheaf quantization is invertible turns out to be very tricky. Since the singular
support estimation above is more complicated when we do not have control on the conformal factors,
one cannot deduce that SS(Kφ
−1
∞ ◦ Kφ∞) = SS(Kφ−1
∞ ◦ Kφ∞) = T ∗
∆(M × M ) just by Theorem 2.2.
Nevertheless, we can prove the following result:

Theorem 4.20. Let M be a complete Riemannian manifold and φn ∈ Cont(S∗M, ξstd) be contac-
tomorphisms such that dC0(id, φn) < ϵ/2, where ϵ > 0 is sufficiently small so that Theorem 4.12
holds. Suppose that each φn has bounded conformal factor, φn → φ∞ in the C0-topology and φ∞
is a homeomorphism. Then the sheaf quantization Kφ∞ is invertible with inverse Kφ
−1
∞ .

C0-RIGIDITY OF LEGENDRIANS AND COISOTROPICS VIA SHEAF QUANTIZATION 33

Proof. We only show that 1∆ = Kφ
−1
∞ ◦ Kφ∞. We have Kφ
−1
n ◦ Kφ∞
1 → Kφ
−1
∞ ◦ Kφ∞ since the
interleaving distance on the product is right invariant. On the other hand, we can show that
Kφ−1
n ◦ Kφm → Kφ
−1
n ◦ Kφ∞ by the same proof as in Theorem 3.10. When (Kφm, Kφm′ ) are
(a, b)-interleaved, we know that there are morphisms such that the compositions

Kφ
−1
n ◦ Kτ
−a ◦ Kφm → Kφ
−1
n
1 ◦ Kφm′ → Kφ
−1
n ◦ Kτ
b ◦ Kφm,

Kφ
−1
n ◦ Kτ
−b ◦ Kφm′ → Kφ
−1
n ◦ Kφm → Kφ−1
n ◦ Kτ
a ◦ Kφm′

are the continuation morphisms. Then by applying Theorem 3.5 and by Theorem 3.6, when the
conformal factor of φn is bounded by hn, we get

Kτ
−ehn a ◦ Kφ
−1
n ◦ Kφm → Kφ
−1
n ◦ Kφm′ → Kτ
ehn b ◦ Kφ
−1
n ◦ Kφm,

Kτ
−ehn b ◦ Kφ
−1
n ◦ Kφm′ → Kφ
−1
n ◦ Kφm → Kτ
ehn a ◦ Kφ
−1
n ◦ Kφm′

whose compositions are continuation morphisms. Thus, given n ∈ N, for any Hm and Hm′, we
know that dτ (Kφ
−1
n ◦ Kφm, Kφ
−1
n ◦ Kφm′ ) ≤ e
hn dτ (Kφm, Kφm′ ).

Hence, for any given n ∈ N, Kφ
−1
n ◦ Kφm → Kφ
−1
n ◦ Kφ∞, and since dτ (1∆, Kφ
−1
n ◦ Kφm) ≤
2Cτ dC0(id, φ−1
n ◦ φm) by Theorem 4.12, we know that

dτ (1∆, Kφ−1
n ◦ Kφ∞) ≤ 2Cτ dC0(id, φ
−1
n ◦ φ∞).

Since φ−1
n ◦ φ∞ → id as n → ∞, we know Kφ−1
n ◦ Kφ∞ → 1∆. Therefore, dτ (1∆, Kφ
−1
∞ ◦ Kφ∞) = 0.
By Theorems 2.35 and 2.37 we know that 1∆ = Kφ−1
∞ ◦ Kφ∞. □

Kashiwara–Schapira [48] constructed quantization of local contactomorphisms on the level of
microlocal sheaves. The microlocal quantization can also be deduced using the sheaf quantization
of Guillermou–Kashiwara–Schapira [39] as explained in [56].

Theorem 4.21. Let φn ∈ Cont(S∗M, ξstd) be contactomorphisms such that dC0(id, φn) < ϵ/2,
where ϵ > 0 is sufficiently small so that Theorem 4.12 holds. Suppose that each φn has bounded
conformal factor, φn → φ∞ in the C0-topology and φ∞ is a homeomorphism. Then there exists a
equivalence between sheaves of categories

Kφ∞ : φ∞∗µsh → µsh,

whose inverse is Kφ
−1
∞ . In particular, for any open set Ω ⊆ S∗M , let Λ ⊆ Ω be any closed coisotropic
subset. Then there exists a equivalence between sheaves of categories over φ∞(Ω)

Kφ∞ : φ∞∗µshΛ → µshφ∞(Λ),

whose inverse is Kφ−1
∞ , and when Λ and φ∞(Λ) are smooth Legendrians, then a microstalk at p ∈ Λ
is sent to a microstalk at φ∞(p) ∈ φ∞(Λ) (thus their corresponding corepresentatives are matched).

Proof. Consider the sheaf quantization Kφ∞ of φ∞. For an open subset Ω ⊆ S∗M , by Theorem 4.18,
we can restrict the convolution functor to the subcategories, which induces a morphism of presheaves
of categories
 Kφ∞ ◦ − : ShΛ∪Ωc(M ) → Shφ∞(Λ∪Ωc)(M ), ShΩc(M ) ≃ Shφ∞(Ωc)(M ).

Then, by sheafification, we get a morphism of the associated sheaves of categories. The result
follows from Theorem 4.20.
Finally, recall that an object F ∈ µshΛ(Λ) is simple if and only if µhom(F, F )p = 1. Hence
simpleness is preserved under equivalences of the sheaves of categories. Then the microstalk (up

34 TOMOHIRO ASANO, YUICHI IKE, CHRISTOPHER KUO, AND WENYUAN LI

to autoequivalences) is preserved because the microstalk of G ∈ µshΛ(Λ) is (non-canonically)
computed by mΛ(G)p = µhom(F, G)p.
This therefore finishes the proof. □

Remark 4.22. Since Kφ∞ induces an equivalence of sheaves of categories Kφ∞ : φ∞∗µsh ∼
−→ µsh,
by [37, Corollary 10.1.5], we know that for any open subset Ω ⊆ S∗M and F, G ∈ µsh(Ω),

φ∞∗µhom(F, G) ≃ µhom(Kφ∞ ◦ F, Kφ∞ ◦ G).

In general, we can also define the sheaf quantization for given a sequence of contactomorphisms
φn ∈ Cont0(S∗M, ξstd) that converges to a homeomorphism φ∞ in the C0-topology, we can also
define a sheaf quantization Kφ∞ of φ∞ as follows, though in a non-canonical way.

Theorem 4.23 (Theorem 1.7). Let (S∗M, ξstd) be the cosphere bundle with the standard contact
structure and Λ ⊆ S∗M be a Legendrian embedding. Consider contactomorphisms φn ∈ Cont0(Y, ξ)
each of which has bounded conformal factor hn. Suppose φn → φ∞ in the C0-topology and φ∞ is a
homeomorphism. Then there exists a (non-canonical) sheaf quantization Kφ∞ ∈ Sh(M × M ) with
inverse Kφ
−1
∞ ∈ Sh(M × M ), and the convolutions preserve microstalks.

Proof. Let ϵ > 0 be sufficiently small such that Theorem 4.12 holds and suppose dC0(φn, φ∞) < ϵ/4
for n ≥ N . We define KφN by Theorem 2.4 and Kφ∞◦φ
−1
N by Theorem 4.18. Now we can define
Kφ∞ := Kφ∞◦φ
−1
N ◦KφN . Similarly, we define Kφ
−1
N by Theorem 2.4 and KφN ◦φ
−1
∞ by Theorem 4.18.
Let Kφ
−1
∞ := Kφ−1
N ◦ KφN ◦φ
−1
∞ . Then the result follows from Theorems 4.20 and 4.21. □

Warning 4.24. The sequence (Kφn)n∈N is not canonical, and thus neither is the limit Kφ∞. In
general, it is an interesting question when such sequence (and its limit) is canonical.

The sheaf quantization result allows us to recover and strengthen the theorem of Dimitroglou
Rizell–Sullivan [23]. For a sequence of compactly supported contactomorphisms φn that converges
to a homeomorphism φ∞, we can show that for any (not necessarily properly embedded) Legendrian
Λ ⊆ S∗M , if φ∞(Λ) is smooth, then it has to be a smooth Legendrian.

Theorem 4.25 (Theorem 1.4 Part 1). Let M be a complete Riemannian manifold and Λ ⊆ S∗M be
a smooth Legendrian. Let φn ∈ Cont(S∗M, ξstd) be contactomorphisms, each of which has bounded
conformal factor hn. Suppose φn → φ∞ in the C0-topology, φ∞ is a homeomorphism and φ∞(Λ)
is smooth. Then φ∞(Λ) is a smooth Legendrian. Moreover, if φn ∈ Cont0(S∗M, ξstd) for any n, Λ
and φ∞(Λ) have the same Maslov class: µ(Λ) = φ∗
∞µ(φ∞(Λ)).

Proof. Let ϵ > 0 be sufficiently small so that Theorem 4.12 holds. Without loss of generality, we
may assume that there exists N such that dC0(φn, φ∞) < ϵ/4 for n ≥ N . Then we know that there
exist sheaf quantizations Kφn◦φ
−1
N that converges to Kφ∞◦φ
−1
N , and by Theorem 4.21, that φ∞ ◦ φ−1
N
induces an equivalence between sheaves of categories

(φ∞ ◦ φ−1
N )∗µshφN (Λ) ≃ µshφ∞(Λ).

Let the coefficients be Mod(Z/2Z)/[1]. Then µshφN (Λ)(φN (Λ)) admits a global rank 1 object
by Theorem 2.20, and thus µshφ∞(Λ)(φ∞(Λ)) also admits a global rank 1 object. Then, by the
coisotropicity theorem of singular supports [48, Theorem 6.5.4], we know that the support of the
rank 1 object φ∞(Λ) is (cone) coisotropic in the sense of [48, Definition 6.5.1]. Since it is a smooth
submanifold, we can conclude that it is a Legendrian submanifold.
For the assertion for the Maslov class, we apply the construction in Theorem 4.23, which implies
that when φn ∈ Cont0(S∗M, ξstd), we have an equivalence of sheaves of categories

µshφ∞(Λ) ≃ φ∞∗µshΛ.

C0-RIGIDITY OF LEGENDRIANS AND COISOTROPICS VIA SHEAF QUANTIZATION 35

We note that Guillermou’s result Theorem 2.20 [37, Section 10.3 & 10.6] for Mod(Z/2Z) shows
that µshΛ is a locally constant sheaf of categories twisted by the Maslov class µ(Λ) ∈ H 1(Λ; Z) via
degree shifting. This implies that µshφ∞(Λ) ≃ φ∞∗µshΛ is a locally constant sheaf of categories
twisted by the Maslov class φ∞∗µ(Λ) ∈ H 1(φ∞(Λ); Z). Hence we get µ(φ∞(Λ)) = φ∞∗µ(Λ). □

Remark 4.26. In the situation of Theorem 4.25, if Λ is closed, then we can prove that Λ and
φ∞(Λ) have the same relative Stiefel–Whitney class as follows. Since φ∞|Λ : Λ → φ∞(Λ) is a
homeomorphism, each Wu class vk(Λ) is preserved by the homeomorphism φ∞. Then by the
formula w2(Λ) = v2(Λ) + v1(Λ)2, we obtain the desired equality.

We are now able to prove the invariance of Maslov data of any embedded Legendrian under
contact homeomorphisms in cosphere bundles Theorem 4.27 (Theorem 1.4). For readers that prefer
to work with the classical dg categories (or stable ∞-categories over a discrete ring), we note that
the following theorem is the only part in the main body of the paper that depends on Jin’s result
Theorem 2.20 over the sphere spectrum. 13

Theorem 4.27 (Theorem 1.4 Part 2). Let M be a complete Riemannian manifold and Λ ⊆ S∗M be
a smooth Legendrian. Let φn ∈ Cont0(S∗M, ξstd) be contactomorphisms, each of which has bounded
conformal factor hn. Suppose φn → φ∞ in the C0-topology, φ∞ is a homeomorphism and φ∞(Λ) is
smooth. Then when φ∞(Λ) is smooth (and hence Legendrian), the compositions of the Lagrangian
Gauss map and the J-homomorphism are homotopically commutative via φ∞:

Λ
 U/O BPic(S)

φ∞(Λ).

φ∞

Proof. Since φn → φ∞ in the uniform topology, by Theorem 4.18, we know that there exist sheaf
quantizations Kφn that converges to Kφ∞, and by Theorem 4.21, we know that induces an equiv-
alence between sheaves of categories

µshφ∞(Λ)(φ∞(Λ)) ≃ µshΛ(Λ).

Then, by Jin’s result Theorem 2.20 [45, Theorem 1.1], we know that for the coefficient Mod(S) the
sheaf of categories µshφ∞(Λ) is classified by the composition of the Lagrangian Gauss map and the
J-homomorphism: Λ → U/O → BPic(S).

This implies that the map φ∞(Λ) → U/O → BPic(S) is homotopic to Λ → U/O → BPic(S). □

Finally, combining our sheaf quantization theorem with the Guillermou–Viterbo γ-coisotropicity
theorem [40, Theorem 1.2], we conclude the C0-rigidity of coisotropic submanifolds. We remark
that while the last part relies on Floer-theoretic spectral invariants, it is also possible to reprove
the results using sheaves.
We follow the definition of coisotropic submanifolds in contact manifolds by Huang [43], which
is also used in [73, 85]. In particular, by [73, Proposition 4.1], for a contact manifold (Y, ξ), C ⊆ Y
is coisotropic if and only if in the symplectization, C × R>0 ⊆ Y × R>0 is symplectic coisotropic.
The main criterion of (symplectic) coisotropicity we will use is as follows, based on the γ-
coisotropicity introduced by Viterbo [87] and closely related to the local rigidity of Usher [86]:

13Theorems A.9 and A.14 in the appendix also depend on Jin’s result.

36 TOMOHIRO ASANO, YUICHI IKE, CHRISTOPHER KUO, AND WENYUAN LI

Lemma 4.28 (Usher [86, Theorem 2.1]). Let (X, ω) be a symplectic manifold and C ⊆ X be a
smooth submanifold. Then C is coisotropic if there is an open dense subset C0 ⊆ C such that for
every x ∈ C0, there is a γ-coisotropic subset Lx ⊆ C0 with x ∈ Lx.

Proof. We argue by contrapositive. If C ⊆ X is not coisotropic at x ∈ C, then there is an open
neighborhood V ⊆ C that is nowhere coisotropic. By [86, Theorem 2.1], we know that V ⊆ C is
nowhere locally rigid in the sense of [86, Definition 1.1], that is, the infimum of the Hofer norm
of Hamiltonians to displace a neighborhood of p in C from a small open ball around p is zero.
Then, since the γ-metric is bounded by the Hofer metric [87, Proposition 7.5 (4)], we can conclude
that V ⊆ C is nowhere γ-coisotropic, that is, the infimum of the spectral norm of Hamiltonians to
displace a neighborhood of p in C from a small open ball around p is zero. □

Theorem 4.29 (Theorem 1.1). Let M be a complete Riemannian manifold and C ⊆ S∗M be a
(locally closed) smooth coisotropic submanifold. Let φn ∈ Cont(S∗M, ξstd) be contactomorphisms,
each of which has bounded conformal factor hn. Suppose φn → φ∞ in the C0-topology, φ∞ is a
homeomorphism and φ∞(C) is smooth. Then φ∞(C) is also coisotropic.

Proof. First, by [85, Corollary 4.10], we know there is an open dense subset C0 ⊆ C such that for
each x ∈ C0, locally there exists a smooth Legendrian Λx ⊆ C with x ∈ Λ. Then by Theorem 4.21,
for a sufficiently large N , there is an equivalence between sheaves of categories

Kφ∞◦φ
−1
N : (φ∞ ◦ φ−1
N )∗µshφN (Λx) → µshφ∞(Λx).

In particular, since µshφN (Λx) is a locally constant sheaf of categories, the stalks of µshφN (Λx) are
nowhere zero, and thus the stalks of µshφ∞(Λx) are nowhere zero. Then, by the γ-coisotropicity
theorem [40, Theorem 1.2], we know that the conic subset φ∞(Λx) × R>0 is γ-coisotropic in T ∗M .
Then by Theorem 4.28 we know that φ∞(C) × R>0 is a coisotropic submanifold in T ∗M . By [73,
Proposition 4.1], this implies φ∞(C) is a coisotropic submanifold in T ∗M . □

Remark 4.30. The above result does not say anything about convex hypersurfaces [34]. As noted
in [73, Example 3.4], any hypersurface in a contact manifold is a coisotropic submanifold, while not
every hypersurface is a convex hypersurface (in fact, C0-flexibility of convex surfaces is recently
shown in [77]). Neither do we say anything about rigidity of coisotropic submanifolds where T C ∩ ξ
is of constant rank (C0-rigidity of such type of coisotropic surfaces is recently shown in [77], where
it is called regular coisotropic).

Appendix A. Local C0-/Hausdorff-Rigidity without Interleaving Distance

In this section, we give a simpler proof of the local C0-rigidity of Legendrians, without using
interleaving distances. We also show a result on rigidity of certain Hausdorff limits of Legendrians.

Proposition A.1. Let M be a smooth manifold, and φn ∈ Cont0(S∗M, ξstd) be a sequence of
contactomorphism that are equal to the identity on a fixed open subset Ω ⊆ S∗M . Suppose φn →
φ∞. Then for any connected smooth properly embedded Legendrian Λ ⊆ S∗M such that Λ ∩ Ω ̸= ∅,
there does not exist any open subset Λ0 ⊆ Λ such that φ∞(Λ0) is smooth but nowhere Legendrian.

Proof. For some open subset Λ0 ⊆ Λ, assume that φ∞(Λ0) is smooth but nowhere Legendrian.
Let the coefficients be Mod(Z/2Z)/[1]. We begin with considering the doubling construction Theo-
rem 2.22. The choice of coefficients ensures µshΛ(Λ) = Loc(Λ) so there is a microlocal rank 1 sheaf
F ∈ ShΛ∪Λτ
ϵ (M × R). Let Kφn ∈ Sh(M × M ) be the sheaf quantizations of φn by Theorem 2.4.
Consider the sheaf F∞ := Fib
( ⊕

n∈N Kφn ◦ F → ∏

n∈N Kφn ◦ F ).

Since SS∞(F ) = Λ ∪ Λτ
ϵ , by the singular support estimation of direct sums and products [40,
Proposition 3.4], we know that SS
∞(F∞) ⊆ φ∞(Λ ∪ Λτ
ϵ ). Since φ∞(Λ0) is smooth but nowhere

C0-RIGIDITY OF LEGENDRIANS AND COISOTROPICS VIA SHEAF QUANTIZATION 37

Legendrian, by the coisotropicity theorem [48, Theorem 6.5.4], we know that in fact SS∞(F∞) ⊆
φ∞(Λ ∪ Λτ
ϵ \ Λ0). Moreover, since the contact isotopies are all supported away from Ω, by [48,
Theorem 7.5.11] we know that the microstalk of F∞ in Λ ∩ Ω is just Fib(
⊕
n∈N 1 → ∏n∈N 1).
Given that φn → φ∞ in the C0-topology, we know that φ−1
n → φ−1
∞ in the C0-topology. Then
consider the sheaf G∞ = Fib
( ⊕

n∈N Kφ
−1
n ◦ F∞ → ∏

n∈N Kφ
−1
n ◦ F∞).

Since SS
∞(F∞) ⊆ φ∞(Λ ∪ Λτ
ϵ \ Λ0), by the singular support estimation of direct sums and products
[40, Proposition 3.4], we know that SS∞(G∞) ⊆ Λ ∪ Λτ
ϵ \ Λ0. This means that the microstalk
of G∞ along Λ0 is zero. Moreover, since the contact isotopies are all supported away from Ω,
by [48, Theorem 7.5.11], the microstalk of G∞ in Λ ∩ Ω is Fib(
⊕n∈N V → ∏n∈N V ) where V =
Fib(
⊕
n∈N 1 → ∏n∈N 1).
Since Λ is a connected smooth Legendrian, by isotopy extension theorem, there exists a contact
isotopy that sends a point in Λ to any other point in Λ. By the invariance of microlocalization
under contactomorphisms [48, Theorem 7.2.1], we know that the microstalk along Λ must be locally
constant. This leads to a contradiction. □

We can strengthen the above result to show the local rigidity of C0-limits of Legendrians:

Theorem A.2. Let M be a smooth manifold, and φn ∈ Cont0(S∗M, ξstd) be a sequence of contac-
tomorphism that are equal to the identity on a fixed open subset Ω ⊆ S∗M . Suppose φn → φ∞.
Then for any connected smooth properly embedded Legendrian Λ ⊆ S∗M such that Λ ∩ Ω ̸= ∅,
φ∞(Λ) is Legendrian if it is smooth. Moreover, if the Maslov class vanishes µ(Λ) = 0, then we also
have µ(φ∞(Λ)) = 0.

Proof. Consider the same sheaf F∞ = Fib(
⊕
n∈N Kφn ◦ F → ∏n∈N Kφn ◦ F ). By Theorem A.1,
we know that there does not exist any open subset Λ0 ⊆ Λ, such that SS
∞(F∞) ∩ φ∞(Λ0) = ∅.
Hence, SS
∞(F∞) ⊆ φ∞(Λ) is dense. Since the singular support is a closed subset, we can conclude
that SS
∞(F∞) = φ∞(Λ). By the coisotropicity theorem [48, Theorem 6.5.4], we know that φ∞(Λ)
is cone coisotropic. Since it is smooth, we can conclude that it is Legendrian.
Finally, suppose the Maslov class µ(Λ) = 0. Let the coefficients be Mod(Z/2Z). The choice of
coefficients ensures µshΛ(Λ) = Loc(Λ) so there is a microlocal rank 1 sheaf F ∈ ShΛ∪Λτ
ϵ (M × R).
Since SS∞(F∞) = φ∞(Λ), the microstalk of F∞ is Fib(⊕
n∈N 1 → ∏n∈N 1), which is a bounded
complex. Then we can conclude that µ(φ∞(Λ)) = 0 by Theorem 2.20. □

More importantly, we can apply the above argument to local Hausdorff limits of Legendrians,
where the result in the main body of the paper does not apply. The main observation is the
following property of cone coisotropicity [48, Definition 6.5.1].

Lemma A.3. Let Λ ⊆ S∗M be a connected properly embedded smooth submanifold with dim Λ =
dim M − 1. Suppose Λ0 ⊆ Λ is a closed cone coisotropic subset and Λ0 contains a non-empty open
subset of Λ. Then Λ0 = Λ and thus Λ is a properly embedded Legendrian.

Proof. Consider a smooth path γ from p to q in the submanifold Λ. Suppose p ∈ Λ0. We show that
q ∈ Λ0 as well. We follow the notations in [40, Section 8]. First, note that the contingent cone and
paratingent cone C−
p (Λ0) ⊆ C+
p (Λ0) ⊆ TpΛ. Hence for any hypersurface H with C−
p (Λ0) ⊆ TpH,
we know that TpΛ ⊆ TpH. Otherwise, C−
p (Λ0) is contained in an isotropic subspace TpH ∩ TpΛ,
which is a contradiction. Now, consider the hypersurface H with T Λ ⊆ T H whose characteristic
curve passing through p is γ. Then [48, Lemma 6.5.3] implies that γ ⊆ Λ0. This completes the
proof. □

By the h-principle for (stabilized or) loose Legendrians [21, 62], for any submanifold N ⊆ S∗M of
dim N = dim M − 1, there exists a sequence of isotopic (stabilized or) loose Legendrians Λn ⊆ S∗M

38 TOMOHIRO ASANO, YUICHI IKE, CHRISTOPHER KUO, AND WENYUAN LI

such that the Hausdorff limit of (Λn)n∈N is N . However, when there exist sheaves with singular
support in Λn ⊆ S∗M , we can still show a rigidity result (this also aligns with the result in
[25, Theorem 1.7] that Legendrians equipped with augmentations cannot be squeezed into tubular
neighborhoods of stabilized or loose Legendrians).

Theorem A.4. Let M be a smooth manifold and Λn ⊆ S∗M be a sequence of connected smooth
properly embedded Legendrians that converges to a smooth manifold Λ∞ ⊆ S∗M in the sense of
Hausdorff convergence. Assume that
(1) there exists an open subset Ω ⊆ S∗M such that Λn ∩ Ω is independent of n and non-empty,
(2) there exists a microlocal rank 1 sheaf Fn ∈ ShΛn(M ; Z/2Z) for each n ∈ N.
Then there exists a sheaf F∞ ∈ ShΛ∞(M ) with non-trivial bounded microstalk. In particular, Λ∞
is a Legendrian and the Maslov class µ(Λ∞) = 0.

Proof. Consider the sheaf F∞ = Fib(
⊕n∈N Fn → ∏n∈N Fn). Then by the singular support estima-
tion [40, Proposition 3.4], we know that SS∞(F∞) ⊆ Λ∞. Since Λn ∩Ω are identical and non-empty,
we know that the microstalk of F∞ along Λ∞ ∩Ω is Fib(⊕
n∈N 1 → ∏n∈N 1). Then by Theorem A.3,
we know that SS
∞(F ) = Λ∞ and thus Λ∞ is a smooth Legendrian. Then by Guillermou’s result
Theorem 2.20 [37, Section 10.3 & 10.6], we can conclude that the Maslov class µ(Λ∞) = 0. □

The sheaf quantization we considered above has microstalk of infinite rank. Thus, it cannot show
that local C0-limits or local Hausdorff limits preserve Maslov data over general coefficients. This
can be fixed via the construction of ultraproducts. Below we use the ultraproducts in categorical
settings following [11]. First, let us recall the definition of ultrafilter on non-negative integers N.
We write P(N) for the power set of N.

Definition A.5. A non-empty subset U of P(N) is said to be an ultrafilter on N if it satisfies the
following:
(1) ∅ /∈ U;
(2) for A, B ⊆ N, if A ∈ U and A ⊆ B, then B ∈ U;
(3) for A, B ⊆ N, if A, B ∈ U, then A ∩ B ∈ U;
(4) for A ⊆ N, either A ∈ U or N \ A ∈ U.

For example, for each n ∈ N, {A ⊆ N | n ∈ A} is a ultrafilter. An ultrafilter of this form is said
to be principal. Otherwise, it is said to be non-principal. Any non-principal ultrafilter contains
every cofinite subset in N (a subset whose complement if finite).

Definition A.6. Let U ⊆ P(N) be an ultrafilter and D be a category which admits products and
filtered colimits. For a sequence (dn)n∈N of objects of D, the ultraproduct of (dn)n∈N is defined to
be the object ∏
U dn := colim
A∈U
 ∏

n∈A dn.

For an object d of D, the ultrapower dU of d is defined to be the ultraproduct ∏U d of the constant
sequence (d)n∈N.

Remark A.7. The set βN of ultrafilters on N admits a topology with open basis consisting of
the subsets of the form [A] := {U ∈ βN | A ∈ U} for every A ⊆ N. The topological space βN
is compact Hausdorff and the inclusion j : N → βN, n ↦→ {A ⊆ N | n ∈ A} gives the Stone– ˇCech
compactification of N.
Let D be a category which admits limits and filtered colimits. For an ultrafilter U, let iU : pt →
βN be the inclusion of a point to the point U ∈ βN. A sequence (dn)n∈N of objects of D can be
regarded as an object of Sh(N; D). Then the ultraproduct ∏U dn is obtained by
∏

U dn ≃ i
∗
U j∗(dn)n∈N.

C0-RIGIDITY OF LEGENDRIANS AND COISOTROPICS VIA SHEAF QUANTIZATION 39

The following lemma follows from point set topology and the definition of singular supports:

Lemma A.8. For a sequence (Gn)n∈N in Sh(M ) and any ultrafilter U ∈ βN, one has

SS (∏

U Gn) ⊆ ⋂

A∈U
 ⋃

n∈A SS(Gn).

Proof. For any closed subset X ⊂ S∗M , the subcategory ShX (M ) is closed under limits and
colimits in Sh(X) by [40, Proposition 3.4]. For any A ∈ U, ∏U Gn ≃ colimA⊇B∈U ∏n∈B Gn, and
hence SS (
∏U Gn) ⊆ ⋃
n∈A SS(Gn). □

Now, we apply the ultraproduct of sheaf quantizations to local Hausdorff limits of Legendrians.
This is also beyond the reach of the technique in the main body of the paper.

Theorem A.9. Let M be a smooth manifold, and (Λn ⊆ S∗M )n∈N be a sequence of connected
smooth properly embedded Legendrians that converges to a smooth manifold Λ∞ ⊆ S∗M in the
sense of Hausdorff convergence. Let R be an E∞-ring spectrum. Assume that
(1) there exists an open subset Ω ⊆ S∗M such that Λn ∩ Ω is independent of i and non-empty,
(2) there exists a microlocal rank 1 sheaf Fn ∈ ShΛn(M ) over R for each n ∈ N.
Then there exists a microlocal rank 1 sheaf F∞ ∈ ShΛ∞(M ) over RU . In particular, Λ∞ is a
Legendrian. Moreover if Λ∞ is homotopy equivalent to a finite CW-complex, then the composite
Λ∞ → U/O → BPic(S) → BPic(R) is null-homotopic.

Proof. Note that the constant sheaf 1M is an E∞-algebra object in Sh(M ) and any object of
Sh(M ) admits a unique 1M -module structure. Then 1U
M ∈ Sh(M ), the ultrapower of 1M , is an
E∞-algebra object and F∞ := ∏U Fn is equipped with a 1U
M -module structure. Since 1U
M ≃ (1U )M ,
F∞ can be regarded as an object of Sh(M ; RU ). By the singular support estimation Theorem A.8,
SS
∞(F∞) ⊆ Λ∞. Since Λn ∩ Ω are identical and non-empty, and the microstalks of Fn are R,
we know that the microstalk of F∞ along Λ∞ ∩ Ω is RU . Therefore, by Theorem A.3, we know
that SS
∞(F ) = Λ and Λ is a smooth Legendrian; moreover, as an object of ShΛ∞(M ; RU ), F∞ is
microlocal rank 1. Hence, by Theorem 2.20, the composition Λ∞ → U/O → BPic(S) → BPic(RU )
is null-homotopic.
Consider the natural morphism BPic(RU ) → BPic(R)U . Then the further composition Λ∞ →
U/O → BPic(S) → BPic(RU ) → BPic(R)U is also null-homotopic. Assume that Λ∞ is ho-
motopy equivalent to a finite CW-complex, and then it is a compact object in the category of
the spaces. Therefore, Map(Λ∞, BPic(R)U ) ≃ Map(Λ∞, BPic(R))U . Since the mapping class in
Map(Λ∞, BPic(R))U that corresponds to the map Λ∞ → BPic(R)U factors through U/O and
BPic(S), it is given by the constant sequence (Λ∞ → U/O → BPic(S) → BPic(R))n∈N. This
element is trivial if and only if the map Λ∞ → U/O → BPic(S) → BPic(R) is null-homotopic. □

Remark A.10. There is a natural morphism Pic(RU ) → Pic(R)U of ∞-groups, which is used in
the proof above. In [11], two (different) categories ∏♭♭
U Mod(R) and ∏ω
U Mod(R) are defined. By
[11, Theorem 3.63], the first one is ∏♭♭
U Mod(R) ≃ Mod(RU ), and the latter will be defined and used
below. There exists a fully faithful symmetric monoidal functor ∏♭♭
U Mod(R) → ∏ω
U Mod(R) and it
induces a morphism between their Picard groupoids. By [58, Proposition 2.2.3] and the definition
of ∏ω
U , Pic(∏ω
U Mod(R)) ≃ Pic(R)U . This gives the natural morphism we want.
The morphism Pic(RU ) → Pic(R)U is not an equivalence in general. Let R be a connective
E∞-ring spectrum. Then [(R[n])n∈N] is a point of Pic(R)U that is not contained in the image of
the morphism since ∏U R[n] ≃ 0 ∈ Mod(R).

For (Cn)n be a sequence of categories, the ultraproduct is defined by
∏
U Cn := colim
A∈U
 ∏

n∈A Cn,

40 TOMOHIRO ASANO, YUICHI IKE, CHRISTOPHER KUO, AND WENYUAN LI

where the products and the filtered colimit are taken in the category of categories.
Let (Cn)n be a sequence of compactly generated categories. Define the compactly generated
ultraproduct of the sequence (Cn)n by
∏ω

U Cn := colim
A∈U ω ∏

n∈A
ωCn,

where colim
ω and ∏ω denote the filtered colimit and the product in the category PrL
ω of compactly

generated categories and functors which preserve colimits and compact objects. See [11] for detailed
arguments about the compactly generated ultraproduct. If each of Cn is stable, then so is ∏ω
U Cn.
If each of Cn is symmetric monoidal
14 , then so is ∏ω
U Cn.
For a sequence (Cn)n of compactly generated categories. Take an arbitrary element A ∈ U. A
functor R : ∏n∈A Cn → ∏ω
n∈A Cn is defined as follows. For a category C, let Cω be the full subcate-
gory of C consisting of compact objects. By the definition of ∏ω
n∈A, ∏ω
n∈A Cn ≃ Ind(
∏n∈A Cω
n ). Let
us restrict the Yoneda embedding ∏n∈A Cn → Fun((∏n∈A Cn)op, S) along the inclusion ∏n∈A Cω
n →∏n∈A Cn, we obtain the functor ∏n∈A Cn → Fun((∏n∈A Cω
n )op, S). The essential image of this func-
tor is contained in Ind(
∏n∈A Cω
n ) and hence we obtain the functor R : ∏n∈A Cn → ∏ω
n∈A Cn. Note
that R is a morphism in PrR and hence it preserves limits. Let L : ∏ω
n∈A Cn → ∏ω
U Cn be the natural
morphism in Pr
L
ω.

Lemma A.11. Let (Cn)n be a sequence of compactly generated symmetric monoidal categories.
The functor R and L defined above are symmetric monoidal.

Note that ∏n∈A Cn is presentable but not compactly generated in general. If a presentable
category D is not compactly generated, for objects in Sh(M ; D), the original definition of the
singular support is not well-behaved. As mentioned by Efimov [27] and Zhang [88], the definition
through Ω-lenses behaves well and admits some other characterizations. In this paper, we also
utilize the definition through Ω-lenses for general coefficients.

Lemma A.12. Let X be a smooth manifold and R : D0 → D1 be a morphism in Pr
R
st. Then R
induces a functor R∗ : Sh(X; D0) → Sh(X; D1) by (R∗F )(U ) := R(F (U )) for each F ∈ Sh(X; D0)
and open U ⊆ M . For each F ∈ Sh(X; D0), SS(R∗F ) ⊆ SS(F ).

Proof. We use the characterization of Ω-lenses as in Theorem 2.1 for singular supports of sheaves
over general coefficients [88, Definition 2.2]. □

Lemma A.13. Let X be a smooth manifold and L : D0 → D1 be a morphism in Pr
L
st. Then L
induces a functor L∗ : Sh(X; D0) → Sh(X; D1) by Sh(X; D0) ≃ Sh(X) ⊗ D0 → Sh(X) ⊗ D1 ≃
Sh(X; D1). For each F ∈ Sh(X; D0), SS(L∗F ) ⊆ SS(F ).

Proof. We use the characterization of singular supports given in [27, Remark. 4.23 2)] or [88,
Proposition 2.6]. □

Theorem A.14. Let M be a smooth manifold, and (Λn ⊆ S∗M )n∈N be a sequence of connected
smooth properly embedded Legendrians that converges to a smooth manifold Λ∞ ⊆ S∗M in the sense
of Hausdorff convergence. Let (Cn)n∈N be a sequence of compactly generated stable rigid symmetric
monoidal categories. Assume that
(1) there exists an open subset Ω ⊆ S∗M such that Λn ∩ Ω is independent of n and non-empty,
(2) there exists a microlocal rank 1 sheaf Fn ∈ ShΛn(M ; Cn) for each n ∈ N.
Then there exists a microlocal rank 1 sheaf F ∈ ShΛ∞(M ; ∏ω
U Cn). In particular, Λ∞ is a Legendrian.
Moreover if Λ∞ is homotopy equivalent to a finite CW-complex, then there exists N ∈ N such that
the composite Λ∞ → U/O → BPic(S) → BPic(Cn) is null-homotopic for each n ≥ N .

14In this paper, we require that the unit object is compact and that compact objects are closed under the monoidal
operation. This will hold for compactly generated rigid symmetric monoidal categories.

REFERENCES 41

Proof. For any A ⊆ N, we can define a sheaf FA ∈ Sh(M ; ∏n∈A Cn) by FA(U ) = (Fn(U ))n∈A ∈∏n∈A Cn. Define F∞ := (L∗ ◦ R∗)(FA). Note that F∞ is the sheafification of a presheaf F pre
∞ that
assigns to each open U ⊆ M the the functor [(cn)n∈A] ↦→ ∏U Hom(cn, Fn(U )) which is an object
of Ind(
∏n∈A Cω
n ), where cn is a compact object of Cn. By the singular support estimations for L∗
and R∗ in Theorems A.12 and A.13, as we vary A ∈ U, we know that

SS
∞(F∞) ⊆ ⋂

A∈U SS
∞(FA) = ⋂

A∈U
 ⋃

n∈A SS
∞(Fn) = Λ∞.

Since Λn∩Ω is independent of n ∈ N, the sheaf Fn is simple along Λn∩Ω, and L and R are symmetric
monoidal functors, we can conclude that F∞ is simple along Λ∞ ∩ Ω. After a perturbation by an
ambient contact isotopy (and taking Ω smaller), we may assume Λ∞ ∩ Ω → M is embedding and
Λ∞ ∩ π−1(π(Ω)) = Λ∞ ∩ Ω. Then the microstalk at Λ∞ is identified with a cone of a map between
stalks. The stalks are preserved by a colimit preserving functor. Hence we obtain the statement
for L∗. Then by Theorem A.3, we know that SS
∞(F∞) = Λ∞ and Λ∞ is a Legendrian; moreover,
F∞ is simple along Λ∞. Hence, by Theorem 2.20, Λ∞ → U/O → BPic(
∏ω
U Cn) is null-homotopic.
When Λ∞ is homotopy equivalent to a finite CW-complex, we show that there is some N ∈ N
such that Λ∞ → U/O → BPic(Cn) is null homotopic for n ≥ N . Otherwise, the cardinality of
the set A0 := {n ∈ N | Λ∞ → BPic(Cn) is not null-homotopic} is infinite. Choose a non-principal
ultrafilter U so that A0 ∈ U. Note that Pic(∏ω
U Cn) ≃ ∏U Pic(Cn) by [58, Proposition 2.2.3]. Note
also that Pic(Cn) ≃ Pic(Cω
n ) since every invertible object in Cn is compact. Since Λ∞ is a compact
object in the category of spaces, we have Map(Λ∞, BPic(
∏ω
U Cn)) ≃ Map(Λ∞, ∏U BPic(Cn)) ≃∏U Map(Λ∞, BPic(Cn)). We know the map Λ∞ → BPic(S) → BPic(
∏ω
U Cn) that classifies the
locally constant sheaf of microsheaves is trivial. However, by our assumption, for any n ∈ A0, the
composition Λ∞ → BPic(Cn) is non-trivial. Since A0 ∈ U, we know that the corresponding map in∏U Map(Λ∞, BPic(Cn)) is also non-trivial. This leads to a contradiction. □

References

[1] Mohammed Abouzaid. “Nearby Lagrangians with vanishing Maslov class are homotopy equiv-
alent”. Invent. Math. 189.2 (2012), pp. 251–313.
[2] Mohammed Abouzaid and Thomas Kragh. “On the immersion classes of nearby Lagrangians”.
J. Topol. 9.1 (2016), pp. 232–244.
[3] Tomohiro Asano and Yuichi Ike. “Completeness of derived interleaving distances and sheaf
quantization of non-smooth objects”. Mathematische Annalen (2024), pp. 1–47.
[4] Tomohiro Asano and Yuichi Ike. “Persistence-like distance on Tamarkin’s category and sym-
plectic displacement energy”. J. Symplectic Geom. 18.3 (2020), pp. 613–649.
[5] Tomohiro Asano and Yuichi Ike. “Sheaf quantization and intersection of rational Lagrangian
immersions”. Ann. Inst. Fourier (Grenoble) 73.4 (2023), pp. 1533–1587.
[6] Tomohiro Asano and Yuichi Ike. The rectifiable rectangular peg problem. 2024. arXiv: 2412.
21057 [math.SG].
[7] Tomohiro Asano, Yuichi Ike, and Wenyuan Li. “Lagrangian cobordism and shadow distance
in Tamarkin category”. Selecta Math. (N.S.) 31.3 (2025), Paper No. 45.
[8] Johan Asplund, Yash Deshmukh, and Alex Pieloch. Spectral equivalence of nearby Lagrangians.
2024. arXiv: 2411.08841 [math.SG].
[9] Johan Asplund and Tobias Ekholm. “Chekanov-Eliashberg dg-algebras for singular Legendri-
ans”. J. Symplectic Geom. 20.3 (2022), pp. 509–559.
[10] Marcelo S. Atallah et al. Weinstein exactness of nearby Lagrangians and the Lagrangian
C0-flux conjecture. 2024. arXiv: 2410.04158 [math.SG].
[11] Tobias Barthel, Tomer M. Schlank, and Nathaniel Stapleton. “Chromatic homotopy theory
is asymptotically algebraic”. Invent. Math. 220.3 (2020), pp. 737–845.

42 REFERENCES

[12] Fr´ed´eric Bourgeois, Tobias Ekholm, and Yasha Eliashberg. “Effect of Legendrian surgery”.
Geom. Topol. 16.1 (2012). With an appendix by Sheel Ganatra and Maksim Maydanskiy,
pp. 301–389.
[13] Lev Buhovsky, Vincent Humili`ere, and Sobhan Seyfaddini. “The action spectrum and C0

symplectic topology”. Math. Ann. 380.1-2 (2021), pp. 293–316.
[14] Lev Buhovsky and Emmanuel Opshtein. “Some quantitative results in C0 symplectic geome-
try”. Invent. Math. 205.1 (2016), pp. 1–56.
[15] Lev Buhovsky et al. “An Arnold-type principle for non-smooth objects”. In: Symplectic
geometry—a Festschrift in honour of Claude Viterbo’s 60th birthday. Reprint of [ 4403699].
Birkh¨auser/Springer, Cham, 2022, pp. 131–152.
[16] Dmitri Burago, Sergei Ivanov, and Leonid Polterovich. “Conjugation-invariant norms on
groups of geometric origin”. In: Groups of diffeomorphisms. Vol. 52. Adv. Stud. Pure Math.
Math. Soc. Japan, Tokyo, 2008, pp. 221–250.
[17] Dylan Cant. “Remarks on the oscillation energy of Legendrian isotopies”. Geom. Dedicata
217.5 (2023), Paper No. 86, 24.
[18] Dylan Cant. Shelukhin’s Hofer distance and a symplectic cohomology barcode for contacto-
morphisms. 2023. arXiv: 2309.00529 [math.SG].
[19] Baptiste Chantraine, Lenhard Ng, and Steven Sivek. “Representations, sheaves and Legen-
drian (2, m) torus links”. J. Lond. Math. Soc. (2) 100.1 (2019), pp. 41–82.
[20] Sheng-Fu Chiu. “Nonsqueezing property of contact balls”. Duke Math. J. 166.4 (2017), pp. 605–
655.
[21] Kai Cieliebak and Yakov Eliashberg. From Stein to Weinstein and back. Vol. 59. Ameri-
can Mathematical Society Colloquium Publications. Symplectic geometry of affine complex
manifolds. American Mathematical Society, Providence, RI, 2012, pp. xii+364.
[22] Georgios Dimitroglou Rizell and Michael G. Sullivan. “C0-limits of Legendrian knots”. Trans.
Amer. Math. Soc. Ser. B 11 (2024), pp. 798–825.
[23] Georgios Dimitroglou Rizell and Michael G. Sullivan. “C0-limits of Legendrians and positive
loops”. Compos. Math. 160.12 (2024), pp. 2904–2915.
[24] Georgios Dimitroglou Rizell and Michael G. Sullivan. “The persistence of a relative Rabinowitz–
Floer complex”. Geom. Topol. 28.5 (2024), pp. 2145–2206.
[25] Georgios Dimitroglou Rizell and Michael G. Sullivan. “The persistence of the Chekanov-
Eliashberg algebra”. Selecta Math. (N.S.) 26.5 (2020), Paper No. 69, 32.
[26] Danijel Djordjevi´c, Igor Uljarevi´c, and Jun Zhang. “Quantitative characterization in contact
Hamiltonian dynamics–I” (2023). arXiv: 2309.00527 [math.SG].
[27] Alexander I Efimov. “K-theory and localizing invariants of large categories”. arXiv preprint
arXiv:2405.12169 (2024).
[28] Tobias Ekholm. Holomorphic curves for Legendrian surgery. 2019. arXiv: 1906.07228 [math.SG].
[29] Tobias Ekholm, John Etnyre, and Michael Sullivan. “Non-isotopic Legendrian submanifolds
in R2n+1”. J. Differential Geom. 71.1 (2005), pp. 85–128.
[30] Tobias Ekholm and Yankı Lekili. “Duality between Lagrangian and Legendrian invariants”.
Geom. Topol. 27.6 (2023), pp. 2049–2179.
[31] Ya. M. Eliashberg. “A theorem on the structure of wave fronts and its application in symplectic
topology”. Funktsional. Anal. i Prilozhen. 21.3 (1987), pp. 65–72, 96.
[32] Sheel Ganatra, John Pardon, and Vivek Shende. “Microlocal Morse theory of wrapped Fukaya
categories”. Ann. of Math. (2) 199.3 (2024), pp. 943–1042.
[33] Hansj¨org Geiges. An introduction to contact topology. Vol. 109. Cambridge Studies in Ad-
vanced Mathematics. Cambridge University Press, Cambridge, 2008, pp. xvi+440.
[34] Emmanuel Giroux. “Convexit´e en topologie de contact”. Comment. Math. Helv. 66.4 (1991),
pp. 637–677.
 REFERENCES 43

[35] Mikhael Gromov. Partial differential relations. Vol. 9. Ergebnisse der Mathematik und ihrer
Grenzgebiete (3) [Results in Mathematics and Related Areas (3)]. Springer-Verlag, Berlin,
1986, pp. x+363.
[36] St´ephane Guillermou. Quantization of conic Lagrangian submanifolds of cotangent bundles.
2012. arXiv: 1212.5818 [math.SG].
[37] St´ephane Guillermou. “Sheaves and symplectic geometry of cotangent bundles”. Ast´erisque
440 (2023), pp. x+274.
[38] St´ephane Guillermou. The Gromov-Eliashberg theorem by microlocal sheaf theory. 2013. arXiv:
1311.0187 [math.SG].
[39] St´ephane Guillermou, Masaki Kashiwara, and Pierre Schapira. “Sheaf quantization of Hamil-
tonian isotopies and applications to nondisplaceability problems”. Duke Math. J. 161.2 (2012),
pp. 201–245.
[40] St´ephane Guillermou and Claude Viterbo. “The singular support of sheaves is γ-coisotropic”.
Geom. Funct. Anal. 34.4 (2024), pp. 1052–1113.
[41] Jakob Hedicke. “Lorentzian distance functions in contact geometry”. J. Topol. Anal. 16.2
(2024), pp. 205–225.
[42] Helmut Hofer and Eduard Zehnder. Symplectic invariants and Hamiltonian dynamics. Modern
Birkh¨auser Classics. Reprint of the 1994 edition. Birkh¨auser Verlag, Basel, 2011, pp. xiv+341.
[43] Yang Huang. “On Legendrian foliations in contact manifolds I: Singularities and neighborhood
theorems”. Math. Res. Lett. 22.5 (2015), pp. 1373–1400.
[44] Vincent Humili`ere, R´emi Leclercq, and Sobhan Seyfaddini. “Coisotropic rigidity and C0-
symplectic geometry”. Duke Math. J. 164.4 (2015), pp. 767–799.
[45] Xin Jin. Microlocal sheaf categories and the J-homomorphism. 2020. arXiv: 2004 . 14270
[math.SG].
[46] Xin Jin and David Treumann. “Brane structures in microlocal sheaf theory”. J. Topol. 17.1
(2024), Paper No. e12325, 68.
[47] Masaki Kashiwara and Pierre Schapira. “Persistent homology and microlocal sheaf theory”.
Journal of Applied and Computational Topology 2.1-2 (2018), pp. 83–113.
[48] Masaki Kashiwara and Pierre Schapira. Sheaves on manifolds. Vol. 292. Grundlehren der
Mathematischen Wissenschaften. Springer-Verlag, Berlin, 1990, pp. x+512.
[49] Thomas Kragh. “Parametrized ring-spectra and the nearby Lagrangian conjecture”. Geom.
Topol. 17.2 (2013). With an appendix by Mohammed Abouzaid, pp. 639–731.
[50] Christopher Kuo. “Wrapped sheaves”. Adv. Math. 415 (2023), Paper No. 108882, 71.
[51] Christopher Kuo and Wenyuan Li. “Duality and Kernels in Microlocal Geometry”. Int. Math.
Res. Not. IMRN 6 (2025), rnaf070.
[52] Christopher Kuo and Wenyuan Li. Spherical adjunction and Serre functor from microlocal-
ization. 2022. arXiv: 2210.06643 [math.SG].
[53] Christopher Kuo, Vivek Shende, and Bingyu Zhang. On the Hochschild cohomology of Tamarkin
categories. 2023. arXiv: 2312.11447 [math.SG].
[54] F. Laudenbach and J.-C. Sikorav. “Hamiltonian disjunction and limits of Lagrangian sub-
manifolds”. Internat. Math. Res. Notices 4 (1994), 161 ff., approx. 8 pp.
[55] Wenyuan Li. Estimating Reeb chords using microlocal sheaf theory. 2021. arXiv: 2106.04079
[math.SG].
[56] Wenyuan Li. “Lagrangian cobordism functor in microlocal sheaf theory I”. J. Topol. 16.3
(2023), pp. 1113–1166.
[57] Wenyuan Li. “Lagrangian cobordism functor in microlocal sheaf theory II”. J. Symplectic
Geom. 23.3 (2025), pp. 599–672.
[58] Akhil Mathew and Vesna Stojanoska. “The Picard group of topological modular forms via
descent theory”. Geom. Topol. 20.6 (2016), pp. 3133–3217.

44 REFERENCES

[59] Cedric Membrez and Emmanuel Opshtein. “C0-rigidity of Lagrangian submanifolds and punc-
tured holomorphic disks in the cotangent bundle”. Compos. Math. 157.11 (2021), pp. 2433–
2493.
[60] Stefan M¨uller and Peter Spaeth. “Gromov’s alternative, Eliashberg’s shape invariant, and
C0-rigidity of contact diffeomorphisms”. Internat. J. Math. 25.14 (2014), pp. 1450124, 13.
[61] Stefan M¨uller and Peter Spaeth. “Topological contact dynamics I: symplectization and appli-
cations of the energy-capacity inequality”. Adv. Geom. 15.3 (2015), pp. 349–380.
[62] Emmy Murphy. Loose Legendrian embeddings in high dimensional contact manifolds. 2012.
arXiv: 1201.2245 [math.SG].
[63] David Nadler. “Microlocal branes are constructible sheaves”. Selecta Math. (N.S.) 15.4 (2009),
pp. 563–619.
[64] David Nadler. Wrapped microlocal sheaves on pairs of pants. 2016. arXiv: 1604.00114 [math.SG].
[65] David Nadler and Vivek Shende. Sheaf quantization in Weinstein symplectic manifolds. 2020.
arXiv: 2007.10154 [math.SG].
[66] David Nadler and Eric Zaslow. “Constructible sheaves and the Fukaya category”. J. Amer.
Math. Soc. 22.1 (2009), pp. 233–286.
[67] Lukas Nakamura. C0-limits of Legendrian Submanifolds. 2020. arXiv: 2008.00824 [math.SG].
[68] Lukas Nakamura. “Legendrians with vanishing Shelukhin-Chekanov-Hofer metric”. Ark. Mat.
62.1 (2024), pp. 147–151.
[69] Lenhard Ng et al. “Augmentations are sheaves”. Geom. Topol. 24.5 (2020), pp. 2149–2286.
[70] Fran¸cois Petit and Pierre Schapira. “Thickening of the diagonal and interleaving distance”.
Selecta Math. (N.S.) 29.5 (2023), Paper No. 70, 42.
[71] Fran¸cois Petit, Pierre Schapira, and Lukas Waas. “A property of the interleaving distance for
sheaves”. Bull. Lond. Math. Soc. 57.1 (2025), pp. 137–149.
[72] Marco Robalo and Pierre Schapira. “A lemma for microlocal sheaf theory in the ∞-categorical
setting”. Publications of the Research Institute for Mathematical Sciences 54.2 (2018), pp. 379–
391.
[73] Daniel Rosen and Jun Zhang. “Chekanov’s dichotomy in contact topology”. Math. Res. Lett.
27.4 (2020), pp. 1165–1193.
[74] Daniel Rosen and Jun Zhang. “Relative growth rate and contact Banach-Mazur distance”.
Geom. Dedicata 215 (2021), pp. 1–30.
[75] Sheila Sandon. “Contact homology, capacity and non-squeezing in R2n × S1 via generating
functions”. Ann. Inst. Fourier (Grenoble) 61.1 (2011), pp. 145–185.
[76] Baptiste Serraille and Vukaˇsin Stojisavljevi´c. On certain C0-aspects of contactomorphism
groups. 2024. arXiv: 2411.11422 [math.SG].
[77] Baptiste Serraille and Maksim Stoki´c. C0-Contact Geometry of Surfaces in 3-Manifolds. 2025.
arXiv: 2509.02430 [math.SG].
[78] Egor Shelukhin. “The Hofer norm of a contactomorphism”. J. Symplectic Geom. 15.4 (2017),
pp. 1173–1208.
[79] Vivek Shende, David Treumann, and Eric Zaslow. “Legendrian knots and constructible sheaves”.
Invent. Math. 207.3 (2017), pp. 1031–1133.
[80] Vukaˇsin Stojisavljevi´c and Jun Zhang. “Persistence modules, symplectic Banach-Mazur dis-
tance and Riemannian metrics”. Internat. J. Math. 32.7 (2021), Paper No. 2150040, 76.
[81] Maksim Stoki´c. C0-flexibility of Legendrian discs in R5. 2024. arXiv: 2406.04194 [math.SG].
[82] Maksim Stoki´c. New steps in C0 symplectic and contact geometry of smooth submanifolds.
2022. arXiv: 2202.07996 [math.SG].
[83] Dmitry Tamarkin. Microlocal category. 2015. arXiv: 1511.08961 [math.SG].
[84] Dmitry Tamarkin. “Microlocal Condition for Non-displaceability”. In: Algebraic and Analytic
Microlocal Analysis. Ed. by Michael Hitrik et al. Cham: Springer International Publishing,
2018, pp. 99–223.
 REFERENCES 45

[85] Michael Usher. “Local rigidity, contact homeomorphisms, and conformal factors”. Math. Res.
Lett. 28.6 (2021), pp. 1875–1939.
[86] Michael Usher. “Local rigidity, symplectic homeomorphisms, and coisotropic submanifolds”.
Bull. Lond. Math. Soc. 54.1 (2022), pp. 45–53.
[87] Claude Viterbo. On the supports in the Humili`ere completion and γ-coisotropic sets. 2022.
arXiv: 2204.04133 [math.SG].
[88] Bingyu Zhang. A remark on Continuous K-theory and Fourier-Sato transform. 2025. arXiv:
2506.02329 [math.AT].
[89] Bingyu Zhang. “Capacities from the Chiu-Tamarkin complex”. J. Symplectic Geom. 22.3
(2024), pp. 441–524.
[90] Peng Zhou. “Sheaf quantization of Legendrian isotopy”. Compos. Math. 159.2 (2023), pp. 419–
435.

Department of Mathematics, Kyoto University, Kitashirakawa-Oiwake-Cho, Sakyo-ku, 606-8502,
Kyoto, Japan
Email address: tasano[at]math.kyoto-u.ac.jp

Graduate School of Mathematical Sciences, The University of Tokyo, 3-8-1 Komaba Meguro-ku
Tokyo 153-8914, Japan
Email address: ike[at]ms.u-tokyo.ac.jp

Max Planck Institute for Mathematics, Vivatsgasse 7, 53111 Bonn, Germany
Email address: chrislpkuo[at]berkeley.edu

Department of Mathematics, University of Southern California, 3551 Trousdale Parkway, Los
Angeles, CA 90089, USA
Email address: wenyuan.li[at]usc.edu
