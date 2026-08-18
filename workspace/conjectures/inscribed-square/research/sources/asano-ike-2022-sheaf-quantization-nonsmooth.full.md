<!-- source: https://arxiv.org/pdf/2201.02598 | converted from PDF -->

arXiv:2201.02598v4  [math.SG]  13 Mar 2024
Completeness of derived interleaving distances and
sheaf quantization of non-smooth objects∗

Tomohiro Asano Yuichi Ike

March 14, 2024

Abstract

We develop sheaf-theoretic methods to deal with non-smooth objects in symplectic
geometry. We show the completeness of a derived category of sheaves with respect to
the interleaving distance and construct a sheaf quantization of a Hamiltonian homeo-
morphism. We also develop Lusternik–Schnirelmann theory in the microlocal theory
of sheaves. With these new sheaf-theoretic methods, we prove an Arnold-type theo-
rem for the image of a compact exact Lagrangian submanifold under a Hamiltonian
homeomorphism.

1 Introduction

The microlocal theory of sheaves due to Kashiwara and Schapira [KS90] has been eﬀec-
tively applied to symplectic and contact geometry after the pioneering work by Nadler–
Zaslow [NZ09; Nad09] and Tamarkin [Tam18]. In this paper, we apply the theory to
symplectic geometry for non-smooth objects, in particular, limits of smooth objects.

1.1 Our results

In this work, we use the Tamarkin category, which was introduced by Tamarkin [Tam18]
to prove his non-displaceability theorem. Let X be a connected C ∞-manifold without
boundary and let π : T ∗X → X denote its cotangent bundle equipped with the canonical
symplectic structure. We also let (t; τ ) denote the homogeneous coordinate system on T ∗Rt
and ﬁx a ﬁeld k. The Tamarkin category D(X) is deﬁned to be the left orthogonal of the
triangulated subcategory consisting of objects microsupported in {τ ≤ 0} ⊂ T ∗(X × Rt)
in D(kX×Rt ), the derived category of sheaves on X × Rt. To generalize Tamarkin’s non-
displaceability theorem to a quantitative version, the authors introduced the interleaving-
like pseudo-distance on D(X) in [AI20], motivated by the convolution distance on D(kRn)
due to Kashiwara–Schapira [KS18]. In this paper, we introduce a modiﬁed pseudo-distance
dD(X) on D(X) that is possibly larger than the previous one. See Subsection 3.2 for the
details of the Tamarkin category and the pseudo-distance dD(X).
In this paper, we ﬁrst establish the completeness of the Tamarkin category D(X) with
respect to dD(X) in Section 4.

Theorem 1.1 (see Corollary 4.5). The Tamarkin category D(X) is complete with respect
to the pseudo-distance dD(X).

∗2020 Mathematics Subject Classiﬁcation: 37J12, 55N31, 18G80, 35A27
Keywords: interleaving distance, C 0-symplectic geometry, microlocal theory of sheaves

1

In fact, we prove the completeness result for a wider class of distances associated with
thickening kernels, which was introduced by Petit–Schapira [PS23]. See the body of the
paper for a precise statement.
In Section 5, we revisit sheaf quantization of Hamiltonian isotopies [GKS12] and Hamil-
tonian stability [AI20]. Let M be a C ∞-manifold and I be an open interval containing the
closed interval [0, 1]. With the Hamiltonian isotopy φH : T ∗M × I → T ∗M associated with
a timewise compactly supported function H : T ∗M × I → R, one can associate a canonical
object K H ∈ D(kM 2×Rt×I), called the sheaf quantization or the Guillermou–Kashiwara–
Schapira (GKS) kernel. We prove that the restriction K H|M 2×Rt×{1} depends only on the
time-1 map of φH
1 . This allows us to deﬁne the sheaf quantization K ϕ ∈ D(kM 2×Rt) of
a compactly supported Hamiltonian diﬀeomorphism ϕ ∈ Hamc(T ∗M ). The sheaf quanti-
zation K ϕ deﬁnes an object Kϕ of the Tamarkin category D(M 2). For these objects, we
prove the following.

Theorem 1.2 (see Theorem 5.11). For compactly supported Hamiltonian diﬀeomorphisms
ϕ, ϕ′ ∈ Hamc(T ∗M ), one has
 dD(M 2)(Kϕ, Kϕ′) ≤ dH (ϕ, ϕ
′), (1.1)

where the right-hand side denotes the Hofer distance between ϕ and ϕ′.

Theorem 1.2 is stronger than the previous Hamiltonian stability result in [AI20] in
the following two points: (1) it is about the distance between GKS kernels and (2) the
distance dD(X) is possibly larger than that in [AI20].
By the completeness result and the stability result, we can associate a sheaf with an
element of the completion of Hamc(T ∗M ) with respect to the Hofer metric. Indeed, a
Cauchy sequence (ϕn)n∈N ⊂ Hamc(T ∗M ) with respect to the Hofer metric dH deﬁnes a
Cauchy sequence (Kϕn)n∈N ⊂ D(M 2) with respect to dD(M 2) by Theorem 1.2. Hence,
by applying Theorem 1.1, we obtain a limit object K[(ϕn)n] ∈ D(M 2). In particular,
we can deﬁne the sheaf quantization Kϕ∞ of a Hamiltonian homeomorphism ϕ∞ (see
Deﬁnition 5.18 for the deﬁnition). One of the advantages of this approach is that we may
directly use the limit object without explicitly dealing with a limit of some sequence to
study C 0-symplectic geometry.
Next, in Section 6, we develop Lusternik–Schnirelmann theory in the microlocal theory
of sheaves. More precisely, for an object F ∈ D(M ), we deﬁne the set of spectral invariants
Spec(F ) ⊂ R and prove the following. Here, cl(M ) denotes the cup-length of M over k.

Theorem 1.3 (see Theorem 6.5 for a more precise statement). Let t : M × Rt → Rt and
πM : T ∗(M × Rt) → M be the projections. Let F ∈ D(M ) and assume that M is compact
and RΓM ×[−c,∞)(M ×Rt; F ) ≃ RΓ(M ; kM ) and F |M ×(c,∞) is locally constant for c ≫ 0. If
# Spec(F ) ≤ cl(M ), then there exists c ∈ Spec(F ) such that πM (SS(F )∩Γdt ∩π−1t−1(−c))
is cohomologically non-trivial in M , where Γdt ⊂ T ∗(M × Rt) is the graph of the 1-form
dt. That is, for any open neighborhood U of πM (SS(F ) ∩ Γdt ∩ π−1t−1(−c)), the restriction
map ⊕
n≥1 H n(M ; k) → ⊕n≥1 H n(U ; k) is non-zero.

The theorem above was announced to appear in Humili`ere–Vichery [HV], which moti-
vated our work.
Finally, in Section 7, by combining the machinery we have developed, we give a purely
sheaf-theoretic proof of the following Arnold-type theorem for non-smooth objects (cf.
Buhovsky–Humili`ere–Seyfaddini [BHS22]). We let 0M denote the zero-section of T ∗M .

2

Theorem 1.4 (see Theorem 7.1). Assume that M is compact and let L be a compact exact
Lagrangian submanifold of T ∗M . Let ϕ∞ be a Hamiltonian homeomorphism of T ∗M . If
the number of spectral invariants of ϕ∞(L) is smaller than cl(M ) + 1, then 0M ∩ ϕ∞(L)
is cohomologically non-trivial in M , hence it is inﬁnite.

This theorem is proved with the sheaf quantization of L due to Guillermou [Gui12;
Gui23] and Viterbo [Vit19], the sheaf quantization of ϕ∞, and Theorem 1.3. By com-
bining our machinery with the C 0-continuity of the spectral norm, which is obtained
in the ﬁeld of symplectic geometry, we can also construct a sheaf quantization of the
image of the zero-section 0M under a C 0-limit of Hamiltonian diﬀeomorphisms. Note
that C 0-limits of Hamiltonian diﬀeomorphisms is a more general notion than Hamiltonian
homeomorphisms. With the sheaf quantization, we can recover an Arnold-type theorem
for a C 0-limit of Hamiltonian diﬀeomorphisms, which is exactly a result by Buhovsky–
Humili`ere–Seyfaddini [BHS22] (see Proposition 7.2).
We also give a sheaf-theoretic proof of a Legendrian analogue of Theorem 1.4. More
precisely, we give an Arnold-type theorem for Hausdorﬀ limits of Legendrian submanifolds
in a 1-jet bundle (cf. [BHS22, Thm. 1.5]).
In Appendix A, we give a Hamiltonian stability result with support conditions, which
may be of independent interest.

1.2 Related work

The completeness of a persistence category was studied by Cruz [Cru19] and Scoccola [Sco20].
They showed that if the category admits any sequential (co)limit, then there is a limit
object for any Cauchy sequence with respect to the interleaving distance. In this paper, we
work with derived categories and need a diﬀerent argument. Our completeness result (The-
orem 1.1) also holds in a triangulated category endowed with a persistence structure. See
also Biran–Cornea–Zhang [BCZ21] for persistence structures for triangulated categories.
Recently Fukaya [Fuk21] introduced the Gromov–Hausdorﬀ distance between ﬁltered A∞
categories, whose idea is based on the interleaving distance, and proved a completeness re-
sult. During the preparation of this paper, the authors learned from St´ephane Guillermou
that he and Claude Viterbo had independently obtained a similar completeness result in
a derived category of sheaves [GV22].
The persistence method has been widely applied to symplectic and contact geometry.
After the pioneering work by Polterovich–Shelukhin [PS16], persistence modules have been
used to study barcodes of Floer cohomology complexes in Usher–Zhang [UZ16] and the
study of spectral norms in Kislev–Shelukhin [KS22], to name a few. In this paper, we
also investigate the relation between the interleaving-like distance dD(M ) and the spectral
norm (see Proposition 6.9). Similar results are independently discovered by Guillermou
and Viterbo [GV22].
Kashiwara–Schapira [KS18] studied persistence modules from the point of view of the
microlocal theory of sheaves. Motivated by the work, Asano–Ike [AI20] introduced the
interleaving-like distance dD(M ) and showed that the distance between an object and its
Hamiltonian deformation is upper bounded by the Hofer norm. The result was eﬀectively
used in Chiu [Chi23] and Li [Li21]. See also Zhang [Zha20] for the interleaving-like distance
in the Tamarkin category.
Buhovsky–Humili`ere–Seyfaddini [BHS18] constructed a counterexample of Arnold’s
conjecture for a Hamiltonian homeomorphism of a closed symplectic manifold M with
dim M ≥ 4. However, one still obtains an Arnold-type theorem for a Hamiltonian homeo-
morphism if one reformulates the conjecture with the notion of spectral invariants, as

3

in [BHS21; Kaw22; BHS22]. In these studies, the C 0-continuity of persistence mod-
ules associated with Hamiltonian diﬀeomorphisms was eﬀectively used (see also [LSV21]).
Guillermou [Gui13] (see also [Gui23, Part VII]) applied the microlocal theory of sheaves to
C 0-symplectic geometry. He gave a purely sheaf-theoretic proof of the Gromov–Eliashberg
theorem, using the involutivity of microsupports.

1.3 Organization

This paper is structured as follows. In Section 2, we recall some basics of the microlo-
cal theory of sheaves. In Section 3, we ﬁrst recall the interleaving distance for sheaves
associated with a thickening kernel. We then brieﬂy review the Tamarkin category and
sheaf quantization of Hamiltonian isotopies. In Section 4, we prove the completeness of
the derived category of sheaves with respect to the distance associated with a thickening
kernel. This completeness in particular implies Theorem 1.1. In Section 5, we ﬁrst prove
a Hamiltonian stability theorem in terms of GKS kernels and the modiﬁed distance. We
then show that the restriction of the sheaf quantization of a Hamiltonian isotopy to time
1 depends only on the time-1 map, which allows us to deﬁne the sheaf quantization of a
Hamiltonian diﬀeomorphism. We also prove Theorem 1.2 and construct a sheaf quantiza-
tion of a Hamiltonian homeomorphism. In Section 6, we develop Lusternik–Schnirelmann
theory for the Tamarkin category and prove Theorem 1.3. We prove Theorem 1.4 in
Section 7 and its Legendrian analogue in Section 8. In Appendix A, we prove a Hamilto-
nian stability result with support conditions, by using sheaf quantization of 2-parameter
Hamiltonian isotopies.

Acknowledgments

The authors would like to express their gratitude to Vincent Humili`ere for fruitful discus-
sion on many parts of this paper. They also thank St´ephane Guillermou and Takahiro
Saito for helpful discussion, and Yusuke Kawamoto for drawing their attention to appli-
cations of the microlocal theory of sheaves to C 0-symplectic geometry. They are also
grateful to Wenyuan Li, Tatsuki Kuwagaki, Morimichi Kawasaki, and Pierre Schapira for
their helpful comments. The authors also thank the anonymous referees for their helpful
comments, which improved many parts of the paper. TA was supported by Innovative
Areas Discrete Geometric Analysis for Materials Design (Grant No. 17H06461). YI was
supported by JSPS KAKENHI (Grant No. 21K13801 and 22H05107) and ACT-X, Japan
Science and Technology Agency (Grant No. JPMJAX1903).

2 Microlocal theory of sheaves

Throughout this paper, let k be a ﬁeld. We mainly follow the notation of [KS90]. In this
section, let X be a C ∞-manifold without boundary.

2.1 Geometric notions

For a locally closed subset Z of X, we denote by Z its closure and by Int(Z) its interior.
We also denote by δX : X → X × X, x ↦→ (x, x) the diagonal map and by ∆X := δX (X)
the diagonal of X × X. We often write ∆ for ∆X for simplicity. We denote by T X the
tangent bundle and by T ∗X the cotangent bundle of X. We write π : T ∗X → X for the
projection. For a closed submanifold M of X, we denote by T ∗
M X the conormal bundle

4

to M in X. In particular, T ∗
X X denotes the zero-section of T ∗X, which we often simply
write 0X . We set ˚T ∗X := T ∗X \ 0X .
With a morphism of manifolds f : X → Y , we associate the following commutative
diagram of morphisms of manifolds:

T ∗X

π   
 X ×Y T ∗Y

  

fdoo fπ // T ∗Y

π
  
X X f // Y,
 (2.1)

where fπ is the projection and fd is induced by the transpose of the tangent map f ′ : T X →
X ×Y T Y .
We denote by (x; ξ) a local homogeneous coordinate system on T ∗X. The cotangent
bundle T ∗X is an exact symplectic manifold with the Liouville 1-form αT ∗X = ⟨ξ, dx⟩.
Thus the symplectic form on T ∗X is deﬁned to be ω = dαT ∗X. We denote by a : T ∗X →
T ∗X, (x; ξ) ↦→ (x; −ξ) the antipodal map. For a subset A of T ∗X, Aa denotes its image
under the antipodal map a. A subset A of T ∗M is said to be conic if it is invariant under
the action of R>0 on T ∗M , that is, the scaling of the ﬁbers.

2.2 Microsupports of sheaves

We write kX for the constant sheaf with stalk k and Mod(kX ) for the abelian category of
sheaves of k-vector spaces on X. Moreover, we denote by D(kX ) the unbounded derived
category of k-vector spaces on X. Although all the results are stated for bounded derived
categories in [KS90], we can apply most of them for unbounded categories, which we shall
state in this subsection. We refer to [Spa88; KS06; RS18]. One can deﬁne Grothendieck’s
six operations RHom, ⊗, Rf∗, f −1, Rf!, f ! for a continuous map f : X → Y with suitable
conditions. For a locally closed subset Z of X, we denote by kZ the zero extension of the
constant sheaf with stalk k on Z to X, whose stalk is 0 on X \ Z. Moreover, for a locally
closed subset Z of X and F ∈ D(kX), we deﬁne FZ , RΓZ (F ) ∈ D(kX) by

FZ := F ⊗ kZ , RΓZ(F ) := RHom(kZ , F ). (2.2)

Let us recall the deﬁnition of the microsupport SS(F ) of an object F ∈ D(kX ).

Deﬁnition 2.1 ([KS90, Def. 5.1.2]). Let F ∈ D(kX) and p ∈ T ∗X. One says that
p ̸∈ SS(F ) if there is a neighborhood U of p in T ∗X such that for any x0 ∈ X and any
C ∞-function ϕ on X (deﬁned on a neighborhood of x0) satisfying dϕ(x0) ∈ U , one has
RΓ{x∈X|ϕ(x)≥ϕ(x0)}(F )x0 ≃ 0. One also sets ˚SS(F ) := SS(F ) ∩ ˚T ∗X.

For a closed subset A of T ∗X, we denote by DA(kX ) the full triangulated subcategory
of D(kX ) consisting of objects whose microsupports are contained in A.
The following is called the microlocal Morse lemma.

Proposition 2.2 ([KS90, Prop. 5.4.17] and [RS18, Thm. 4.1]). Let F ∈ D(kX ) and
ϕ : X → R be a C ∞-function. Let moreover a, b ∈ R with a < b. Assume

(1) ϕ is proper on Supp(F ),

(2) dϕ(x) ̸∈ SS(F ) for any x ∈ ϕ−1([a, b)).

5

Then the canonical morphism

RΓ(ϕ
−1((−∞, b)); F ) → RΓ(ϕ
−1((−∞, a)); F ) (2.3)

is an isomorphism.

We consider the behavior of the microsupports with respect to functorial operations.

Proposition 2.3 ([KS90, Prop. 5.4.4, Prop. 5.4.13, and Prop. 5.4.5]). Let f : X → Y be
a morphism of manifolds, F ∈ D(kX ), and G ∈ D(kY ).

(i) Assume that f is proper on Supp(F ). Then SS(Rf∗F ) ⊂ fπf −1
d (SS(F )). Moreover,
if f is a closed embedding, the inclusion is an equality.

(ii) Assume that f is non-characteristic for SS(G) (see [KS90, Def. 5.4.12] for the deﬁ-
nition). Then SS(f −1G) ∪ SS(f !G) ⊂ fdf −1
π (SS(G)).

For closed conic subsets A and B of T ∗X, let us denote by A + B the ﬁberwise sum of
A and B, that is,

A + B :=
 {
(x; a + b)
 ∣
∣
∣
∣
∣ x ∈ π(A) ∩ π(B),

a ∈ A ∩ π−1(x), b ∈ B ∩ π−1(x)

}
 ⊂ T ∗X. (2.4)

Proposition 2.4 ([KS90, Prop. 5.4.14]). Let F, G ∈ D(kX ).

(i) If SS(F ) ∩ SS(G)a ⊂ 0X , then SS(F ⊗ G) ⊂ SS(F ) + SS(G).

(ii) If SS(F ) ∩ SS(G) ⊂ 0X, then SS(RHom(F, G)) ⊂ SS(F )a + SS(G).

We need an estimate for the microsupport of a kind of limit object in D(kX ). For that
purpose, we use the following estimates.

Lemma 2.5 (cf. [KS90, Exe. V.7]). Let I be an index set and Fi ∈ D(kX ) for i ∈ I.
Then, one has
 SS
 (∏

i∈I Fi
)
 , SS
 (⊕

i∈I Fi
)
 ⊂ ⋃

i∈I SS(Fi). (2.5)

2.3 Composition and convolution

We recall the operation called the composition of sheaves.
For i = 1, 2, 3, let Xi be a manifold. We write Xij := Xi ×Xj and X123 := X1 ×X2 ×X3
for short. We denote by qij the projection X123 → Xij. Similarly, we denote by pij the
projection T ∗X123 → T ∗Xij. We also denote by p12a the composite of p12 and the antipodal
map on T ∗X2.
Let A ⊂ T ∗X12 and B ⊂ T ∗X23. We set

A ◦ B := p13(p−1
12aA ∩ p−1
23 B) ⊂ T ∗X13. (2.6)

We deﬁne a composition operation of sheaves by

◦
X2 : D(kX12 ) × D(kX23) → D(kX13 ),

(K12, K23) ↦→ K12 ◦
X2 K23 := Rq13!(q−1
12 K12 ⊗ q−1
23 K23). (2.7)

If there is no risk of confusion, we simply write ◦ instead of ◦
X2. By Propositions 2.3

and 2.4, we have the following.
 6

Proposition 2.6. Let Kij ∈ D(kXij ) and set Λij := SS(Kij) ⊂ T ∗Xij (ij = 12, 23).
Assume

(1) q13 is proper on q−1
12 Supp(K12) ∩ q−1
23 Supp(K23),

(2) p−1
12aΛ12 ∩ p−1
23 Λ23 ∩ (T ∗
X1X1 × T ∗X2 × T ∗
X3X3) ⊂ 0X123 .

Then
 SS(K12 ◦
X2 K23) ⊂ Λ12 ◦ Λ23. (2.8)

In this work, we often use sheaves on X ×R. We introduce the operation of convolution
for objects of D(kX×R). Deﬁne the maps

˜q1, ˜q2, m : X × R × R → X × R, (2.9)

˜q1(x, t1, t2) = (x, t1), ˜q2(x, t1, t2) = (x, t2), m(x, t1, t2) = (x, t1 + t2).

We deﬁne a convolution operation by

⋆ : D(kX×R) × D(kX×R) → D(kX×R),

(F, G) ↦→ F ⋆ G := Rm!(˜q−1
1 F ⊗ ˜q−1
2 G). (2.10)

We also introduce a right adjoint to the convolution functor. Set i : X×R → X×R, (x, t) ↦→
(x, −t).

Deﬁnition 2.7. For F, G ∈ D(kX×R), one sets

Hom⋆(F, G) := R˜q1∗ RHom(˜q−1
2 F, m!G) (2.11)

≃ Rm∗ RHom(˜q−1
2 i
−1F, ˜q!
1G). (2.12)

Lemma 2.8. Let F, G ∈ D(kX×R) and assume that there exist two closed cones A, B ⊂ R
such that SS(F ) ⊂ T ∗X × R × A and SS(G) ⊂ T ∗X × R × B. Then, one has

SS(F ⋆ G) ⊂ T ∗X × R × (A ∩ B),

SS(Hom⋆(F, G)) ⊂ T ∗X × R × (A ∩ B). (2.13)

It is useful to deﬁne a more general operation, which combines composition and con-
volution. Set
˜q12 : X123 × R2 → X12 × R, (x1, x2, x3, t1, t2) ↦→ (x1, x2, t1), (2.14)

˜q23 : X123 × R2 → X23 × R, (x1, x2, x3, t1, t2) ↦→ (x2, x3, t2), (2.15)

m13 : X123 × R2 → X13 × R, (x1, x2, x3, t1, t2) ↦→ (x1, x3, t1 + t2) (2.16)

and deﬁne

•X2 : D(kX12×R) × D(kX23×R) → D(kX13×R),

(K12, K23) ↦→ K12 •
X2 K23 := Rm13! (˜q−1
12 K12 ⊗ ˜q−1
23 K23). (2.17)

If there is no risk of confusion, we simply write • instead of •
X2.

7

2.4 Homotopy colimits

Here, we recall the deﬁnition of homotopy colimits (cf. [BN93] and [KS06]) and estimate
their microsupports.
Let (Fn)n∈N be a sequence of objects of D(kX) together with morphisms fn : Fn →
Fn+1 (n ∈ N = Z≥0), that is, (Fn, fn)n∈N is an inductive system in D(kX ). Deﬁne a
morphism s : ⊕n∈N Fn → ⊕n∈N Fn as the composite

⊕

n∈N Fn
 ⊕
n fn
−−−−→ ⊕

n∈N Fn+1 ≃ ⊕

n∈Z≥1 Fn → ⊕

n∈N Fn. (2.18)

Then one can deﬁne the homotopy colimit of the inductive system (Fn, fn)n∈N as the cone
of the morphism
 id −s : ⊕

n∈N Fn → ⊕

n∈N Fn, (2.19)

which we write hocolim(Fn) ∈ D(kX). We have a canonical morphism ρn : Fn → hocolim(Fn).
Given a sequence of morphisms gn : Fn → G (n ∈ N) such that gn+1 ◦ fn = gn for any n,
we get a morphism g : hocolim(Fn) → G satisfying gn = g ◦ ρn.

Lemma 2.9. Let (Fn, fn)n∈N be an inductive system in D(kX). Then

SS(hocolim(Fn)) ⊂ ⋂

N ∈N
 ⋃

n≥N SS(Fn). (2.20)

Proof. By Lemma 2.5, SS(
⊕n∈N Fn) ⊂ ⋃n SS(Fn). Note that we have hocolimn(Fn) ≃
hocolimn(Gn) with Gn = Fn+N for any N ∈ N. Hence, the result follows from the triangle
inequality for microsupports and the deﬁnition of homotopy colimits.

3 Interleaving distance for sheaves and sheaf quantization

In this section, we review the interleaving distance for sheaves following Petit–Schapira [PS23].
We also brieﬂy review the Tamarkin category [Tam18] and sheaf quantization of Hamil-
tonian isotopies [GKS12]. See also Guillermou–Schapira [GS14] and Zhang [Zha20] for
details of the Tamarkin category.

3.1 Interleaving distance for sheaves

We recall some notions from Petit–Schapira [PS23]. A topological space is said to be good
if it is Hausdorﬀ, locally compact, countable at inﬁnity, and ﬁnite ﬂabby dimension.

Deﬁnition 3.1. Let X be a good topological space. A thickening kernel on X is a
monoidal presheaf K on (R≥0, +) with values in the monoidal category D(kX×X ). In other
words, it is a family of kernels Ka ∈ D(kX×X ) with a morphism ρb,a : Kb → Ka for a ≤ b
together with isomorphisms
 Ka ◦ Kb ≃ Ka+b, K0 ≃ k∆X (3.1)

satisfying the compatibility conditions (see [PS23, Def. 1.2.2] for details).

For a thickening kernel K on X and F ∈ D(kX ), we write ρb,a(F ) for the morphism
ρb,a ◦ idF : Kb ◦ F → Ka ◦ F (a ≤ b).
 8

Deﬁnition 3.2. Let K be a thickening kernel on X, F, G ∈ D(kX ), and a, b ∈ R≥0.

(i) The pair (F, G) is said to be (a, b)-isomorphic if there exist morphisms α : Ka◦F → G
and β : Kb ◦ G → F such that

(1) the composite Ka+b ◦ F Ka◦α
−−−→ Kb ◦ G β
−→ F is equal to ρa+b,0(F ),

(2) the composite Ka+b ◦ G Kb◦β
−−−→ Ka ◦ F α
−→ G is equal to ρa+b,0(G).

In this case, the pair of morphisms (α, β) is called an (a, b)-isomorphism.

If (F, G) is (a, a)-isomorphic then F and G are called a-isomorphic.

(ii) One sets
 dK(F, G) := inf
 {
a + b ∈ R≥0
 ∣
∣
∣
∣
∣ a, b ∈ R≥0,

(F, G) is (a, b)-isomorphic
}
 , (3.2)

which deﬁnes a pseudo-distance on the category D(kX ).

(iii) The pair (F, G) is said to be weakly (a, b)-isomorphic if there exist morphisms
α, δ : Ka ◦ F → G and β, γ : Kb ◦ G → F such that

(1) the composite Ka+b ◦ F Ka◦α
−−−→ Kb ◦ G β
−→ F is equal to ρa+b,0(F ),

(2) the composite Ka+b ◦ G Kb◦γ
−−−→ Ka ◦ F δ
−→ G is equal to ρa+b,0(G),

(3) α ◦ ρ2a,a(F ) = δ ◦ ρ2a,a(F ) and β ◦ ρ2b,b(G) = γ ◦ ρ2b,b(G).

(iv) One says that F is a-torsion or a-trivial if ρa,0(F ) : Ka ◦F → F is the zero morphism.

Remark 3.3. (i) One can see that

(a, b)-isomorphic ⇒ weakly (a, b)-isomorphic (3.3)

and
 weakly (a, b)-isomorphic ⇒ (2a, 2b)-isomorphic

⇒ 2 max(a, b)-isomorphic. (3.4)

(ii) In [PS23], the authors deﬁne

distK(F, G) := inf{a ∈ R≥0 | F and G are a-isomorphic} (3.5)

and call it the interleaving distance associated with K. By (i), the pseudo-distances
dK and distK are equivalent. Indeed,

dK(F, G) ≤ 2 distK(F, G) ≤ 2dK(F, G). (3.6)

(iii) The interleaving distance above is a generalization of the convolution distance dC on
D(kR) introduced by Kashiwara–Schapira [KS18] and later investigated by [KS21;
BG21; BP21; BGO19] and others. Indeed, when X = R and Ka = k∆a, where
∆a := {(x, y) ∈ R2 | ∥x − y∥ ≤ a} ⊂ R2 is the thickened diagonal, we ﬁnd that
dC = distK.
 9

In what follows, let K be a thickening kernel on X. The statement of the following
lemma is slightly stronger than [AI20, Lem. 4.14], but the proof itself is almost the same.
We need the stronger result in this paper, so we reproduce the proof for the convenience
of the reader.

Lemma 3.4 (cf. [AI20, Lem. 4.14]). Let F u
−→ G v
−→ H w
−→ F [1] be an exact triangle in
D(kX) and assume that F is c-torsion. Then (G, H) is weakly (0, c)-isomorphic.

Proof. By assumption, we have w ◦ ρc,0(H) = ρc,0(F [1]) ◦ (Kc ◦X w) = 0. Hence, we get a
morphism γ : Kc ◦ H → G satisfying ρc,0(H) = v ◦ γ:

Kc ◦ F Kc◦u //

  
 Kc ◦ G Kc◦v //

   ⟳

Kc ◦ H Kc◦w //

    

γ

zzt t t t t t Kc ◦ F [1]

0
  
F u // G v // H w // F [1].
 (3.7)

On the other hand, since ρc,0(G) ◦ (Kc ◦X u) = u ◦ ρc,0(F ) = 0, there exists a morphism
β : Kc ◦ H → G satisfying ρc,0(G) = β ◦ (Kc ◦X v):

Kc ◦ F Kc◦u //

0   
 Kc ◦ G Kc◦v //

  
 ⟳ Kc ◦ H Kc◦w //

    β
zzt t t t t t Kc ◦ F [1]

  
F u // G v // H w // F [1].
 (3.8)

Moreover, we obtain

β ◦ ρ2c,c(H) = β ◦ (Kc ◦X ρc,0(H))

= β ◦ (Kc ◦X v) ◦ (Kc ◦X γ)

= ρc,0(G) ◦ (Kc ◦X γ)

= γ ◦ (Kc ◦X ρc,0(H)) = γ ◦ ρ2c,c(H),
 (3.9)

which proves the lemma.

In particular, if F → G → H +1
−−→ is an exact triangle, F is a-torsion, and G is b-torsion,
then H is (a + b)-torsion.
In our later applications, we mainly focus on the interleaving distance on the derived
category D(kX×Rt). For c ∈ R≥0, deﬁne

Kc := k∆X ×∆c ∈ D(k(X×R)2 ), (3.10)

where ∆c := {(t1, t2) | ∥t1 − t2∥ ≤ c} ⊂ R2 is the thickened diagonal of ∆R ⊂ R2. Then
the assignment c ↦→ Kc deﬁnes a thickening kernel on X × Rt. Hence, we can consider the
pseudo-distance dK on D(kX×Rt) associated with K, which we denote by dX×Rt . This is a
slight modiﬁcation of the relative distance distX×Rt/X studied in [PS23]. Note also that
Kc ◦ F ≃ kX×[−c,c] ⋆ F . With the notation in Subsection 2.3, for F, F ′ ∈ D(kX12×Rt) and
G, G′ ∈ D(kX23×Rt),

dX13×Rt(F • G, F ′ • G
′) ≤ dX12×Rt(F, F ′) + dX23×Rt(G, G
′). (3.11)

10

3.2 Tamarkin category

Let X be a manifold without boundary. We let (t; τ ) denote the homogeneous coordinate
system on T ∗Rt. It is proved by Tamarkin [Tam18] that the functor Pl := kX×[0,∞) ⋆
(∗) : D(kX×Rt) → D(kX×Rt) deﬁnes a projector onto ⊥D{τ ≤0}(kX×Rt ), where {τ ≤ 0} =
{(x, t; ξ, τ ) | τ ≤ 0} ⊂ T ∗(X × Rt) and ⊥(∗) denotes the left orthogonal.

Deﬁnition 3.5. One deﬁnes
 D(X) := ⊥D{τ ≤0}(kX×Rt ), (3.12)

and call it the Tamarkin category of X.

For an object F ∈ D(kX×Rt), F ∈ D(X) if and only if Pl(F ) ≃ F . Note also that
D(X) ⊂ D{τ ≥0}(kX×Rt ) by Lemma 2.8.

Deﬁnition 3.6. One deﬁnes dD(X) as the restriction of the pseudo-distance dX×Rt on
D(kX×Rt) to D(X).

We will describe the pseudo-distance using the translation to the Rt-direction. For
c ∈ R, let Tc : X × Rt → X × Rt, (x, t) ↦→ (x, t + c) be the translation map by c to the
R-direction. In what follows, we write Tc instead of Tc∗ for simplicity. Recall that we have
set Kc := k∆X ×∆c ∈ D(k(X×R)2 ).

Lemma 3.7. Let F ∈ D{τ ≥0}(kX×Rt ). Then Kc ◦ F ≃ T−cF .

Proof. First we recall that Kc ◦ F ≃ kX×[−c,c] ⋆ F . Since there exist an exact triangle

kX×(−c,c] → kX×[−c,c] → kX×{−c} +1
−−→ and an isomorphism T−cF ≃ kX×{−c} ⋆ F , it
suﬃces to show that kX×(−c,c] ⋆ F ≃ 0. By Lemma 5.3, there exists H ∈ D(kX ) such that
kX×(−∞,0] ⋆ F ≃ H ⊠ kRt. Thus, we obtain

kX×(−c,c] ⋆ F ≃ kX×(−c,c] ⋆ kX×(−∞,0] ⋆ F

≃ kX×(−c,c] ⋆ (H ⊠ kRt)

≃ H ⊠ (k(−c,c] ⋆ kRt) ≃ 0,
 (3.13)

which completes the proof.

Let F ∈ D{τ ≥0}(kX×Rt ). Then, we have an isomorphism

Rm∗(˜q−1
1 kX×[0,∞) ⊗ ˜q−1
2 F ) ∼
−→ Rm∗(˜q−1
1 kX×{0} ⊗ ˜q−1
2 F ) ≃ F. (3.14)

Hence, for c, d ∈ R≥0 with c ≤ d, the canonical morphism kX×[c,∞) → kX×[d,∞) induces a
canonical morphism
 τc,d(F ) : TcF ≃ Rm∗(˜q−1
1 kX×[c,∞) ⊗ ˜q−1
2 F )

→ Rm∗(˜q−1
1 kX×[d,∞) ⊗ ˜q−1
2 F ) ≃ TdF. (3.15)

By Lemma 3.7, the morphism is identiﬁed with

Tc+dρd,c(F ) : Tc+d(Kd ◦ F ) → Tc+d(Kc ◦ F ). (3.16)

Hence, a pair (F, G) of objects of D(X) is (a, b)-isomorphic if and only if there exist
morphisms α, δ : F → TaG and β, γ : G → TbF such that

11

(1) F α
−→ TaG Taβ
−−→ Ta+bF is equal to τ0,a+b(F ) : F → Ta+bF and

(2) G β
−→ TbF Tbα
−−→ Ta+bG is equal to τ0,a+b(G) : G → Ta+bG.

In this form, we can see that dD(X) is similar to the pseudo-distance introduced in [AI20]
(see Remark 3.8 below).

Remark 3.8. The terminology has been changed from that in [AI20]. In that paper,
“weakly (a, b)-isomorphic” in this paper was called “(a, b)-isomorphic”. Moreover, we
deﬁned the notion of “(a, b)-interleaved” as follows: a pair (F, G) of objects of D(X) is
said to be (a, b)-interleaved if there exist morphisms α, δ : F → TaG and β, γ : G → TbF
satisfying

(1) F α
−→ TaG Taβ
−−→ Ta+bF is equal to τ0,a+b(F ) : F → Ta+bF and

(2) G γ
−→ TbF Tbδ
−−→ Ta+bG is equal to τ0,a+b(G) : G → Ta+bG.

One can see that

(a, b)-isomorphic ⇒ weakly (a, b)-isomorphic ⇒ (a, b)-interleaved.

We also remark that the distance dD(X) in [AI20] is deﬁned by the relation “(a, b)-
interleaved” instead of “(a, b)-isomorphic”, and hence it is diﬀerent from that in Deﬁ-
nition 3.6. Later we will prove the main result in [AI20] also holds for the modiﬁed dD(X)
(see Theorem 5.1).

The following proposition is slightly stronger than the similar results in the published
version of [AI20].

Proposition 3.9 (cf. [AI20, Prop. 4.15]). Let I be an open interval containing the closed
interval [0, 1] and H ∈ D{τ ≥0}(kX×Rt×I ). Assume that there exist continuous functions
f, g : I → R≥0 satisfying

SS(H) ⊂ T ∗X × {(t, s; τ, σ) | −f (s) · τ ≤ σ ≤ g(s) · τ }. (3.17)

Then (H|X×Rt×{0}, H|X×Rt×{1}) is weakly (∫ 1
0 g(s)ds + ε, ∫ 1
0 f (s)ds + ε
)
-isomorphic for
any ε ∈ R>0.

Proof. The proof is similar to that of [AI20, Prop. 4.15]. We only need to replace [AI20,
Lem. 4.14] with Lemma 3.4.

3.3 Sheaf quantization of Hamiltonian isotopies

In this subsection, we ﬁrst recall the existence and uniqueness result of a sheaf quantization
of a Hamiltonian isotopy due to Guillermou–Kashiwara–Schapira [GKS12].
Let M be a connected manifold without boundary and I an open interval of R con-
taining the closed interval [0, 1]. We say that a C ∞-function H = (Hs)s∈I : T ∗M × I → R
is timewise compactly supported if supp(Hs) is compact for any s ∈ I. A compactly sup-
ported Hamiltonian isotopy is a ﬂow of the Hamiltonian vector ﬁeld of a timewise com-
pactly supported C ∞-function H. In this paper, the isotopy associated with H is denoted
by φH = (φH
s )s∈I : T ∗M × I → T ∗M . Note that (φH
s )−1 = φH
s with Hs(p) := −Hs(φH
s (p)).
Moreover, for two timewise compactly supported functions H, H ′ : T ∗M × I → R, we have

φ
H
s ◦ φ
H ′
s = φ
H♯H ′
s , (3.18)

12

where (H♯H ′)s(p) := Hs(p) + H ′
s((φH
s )−1(p)). In particular, for two timewise compactly
supported functions H, H ′ : T ∗M × I → R,

(φ
H
s )
−1 ◦ φ
H ′
s = φ
H♯H ′
s , (3.19)

where (H♯H ′)s(p) = (H ′ − H)s(φH
s (p)).

Deﬁnition 3.10. Let φH = (φH
s )s∈I : T ∗M × I → T ∗M be the compactly supported
Hamiltonian isotopy associated with a timewise compactly supported function H : T ∗M ×
I → R.

(i) One deﬁnes ̂H : ˚T ∗(M × Rt) × I → R by

̂H((x, t; ξ, τ ), s) :=
 {τ H((x; ξ/τ ), s) (τ ̸= 0)
0 (τ = 0) (3.20)

and ̂φ = (̂φs)s∈I : ˚T ∗(M ×Rt)×I → ˚T ∗(M ×Rt) to be the homogeneous Hamiltonian
ﬂow of ̂H.

(ii) One deﬁnes a conic Lagrangian submanifold Λ ̂φ of ˚T ∗(M × R)2 × T ∗I by

Λ ̂φ := {(̂φ((x, t; ξ, τ ), s), (x, t; −ξ, −τ ), (s; − ̂H (̂φ((x, t; ξ, τ ), s), s))
) ∣
∣
∣

(x, t; ξ, τ ) ∈ ˚T ∗(M × Rt), s ∈ I} . (3.21)

For a timewise compactly supported function H : T ∗M × I → R, we also deﬁne u =
(us)s∈I : T ∗M × I → R by us(p) = ∫ s
0 (Hs′ − α(Xs′))(φH
s′ (p))ds′, where (Xs)s∈I is the
Hamiltonian vector ﬁeld for H. Then ̂φ can be written as

̂φs(x, t; ξ, τ ) = (x′, t + us(x; ξ/τ ); ξ′, τ ), (3.22)

where (x′; ξ′/τ ) = φs(x; ξ/τ ) for τ ̸= 0, and ̂φs(x, t; ξ, 0) = (x, t; ξ, 0). Hereafter, we use the
convention that τ Hs(φs(x; ξ/τ )) = 0 and us(x; ξ/τ ) = 0 when τ = 0. Moreover, we write
(x′; ξ′/τ ) = φs(x; ξ/τ ) also for τ = 0, in which case it is understood that (x′; ξ′) = (x; ξ).
We have dus = α − (φs)∗α, which gives the following properties.

Lemma 3.11. If φ1 = idT ∗M , then u1 ≡ 0.

The main theorem of [GKS12] is the following.

Theorem 3.12 ([GKS12, Thm. 3.7]). Let φ : T ∗M × I → T ∗M be a compactly supported
Hamiltonian isotopy and H : T ∗M × I → R be a C ∞-function with Hamiltonian ﬂow φ.
Then there exists a unique simple object ̃K H ∈ D(k(M ×R)2×I ) such that ˚SS( ̃K H) = Λ ̂φ and
̃K H|(M ×R)2×{0} ≃ k∆M ×R.

Set ̃K H
s := ̃K H|(M ×R)2×{s} ∈ D(k(M ×R)2 ). Note that ˚SS( ̃K H
s ) ⊂ Λ ̂φ ◦ T ∗
s I. We also
have
 ̃K H
s ◦ ̃K H ′
s ≃ ̃K H♯H ′
s . (3.23)

It is also proved by Guillermou–Schapira [GS14, Prop. 4.29] that the composition with
̃K H
s deﬁnes a functor
 ̃K H
s ◦ (∗) : D(M ) −→ D(M ). (3.24)

13

Deﬁne q : (M × R)2 × I → M 2 × Rt × I, (x1, t1, x2, t2, s) ↦→ (x1, x2, t1 − t2, s) and set

Λ
′
H := qπq−1
d (Λ ̂φ)

= {(
(x′; ξ′), (x; −ξ), (us(x; ξ/τ ); τ ), (s; −τ Hs(φs(x; ξ/τ )))
) ∣
∣

(x; ξ) ∈ T ∗M, s ∈ I, τ ∈ R, (x′; ξ′/τ ) = φs(x; ξ/τ )
}

⊂ ˚T ∗(M 2 × Rt × I).
 (3.25)

Then the inverse image functor q−1 gives an equivalence (see [Gui23, Cor. 2.3.2])

{K ∈ D(kM 2×Rt×I ) | ˚SS(K) = Λ
′
H} ∼
−→ { ̃K ∈ D(k(M ×R)2×I ) | ˚SS( ̃K) = Λ ̂φ}. (3.26)

Recall that we have a projector Pl : D(kM 2×Rt) → ⊥D{τ ≤0}(kM 2×Rt) = D(M 2) and simi-
larly for D(M 2 × I).

Deﬁnition 3.13. Let H : T ∗M × I → R be a timewise compactly supported function.

(i) One deﬁnes K H ∈ D(kM 2×Rt×I) to be the object such that ˚SS(K H ) = Λ′
H and
K H|M 2×Rt×{0} ≃ k∆M ×{0}, that is, the object K H satisfying q−1K H ≃ ̃K H. One
also sets K H
s := K H|M 2×Rt×{s} for simplicity.

(ii) One deﬁnes KH
s := Pl(K H
s ) ∈ D(M 2) and KH := Pl(K H ) ∈ D(M 2 × I).

Note that ̃K H
s ◦ F ≃ K H
s • F for any F ∈ D(M ) and s ∈ I. By the associativity, for
any F ∈ D(M ) and s ∈ I, we have

K H
s • F ≃ K H
s • (kM ×[0,∞) ⋆ F )

≃ (K H
s •M kM ×[0,∞)) • F

≃ (K H
s ⋆ kM ×M ×[0,∞)) • F ≃ KH
s • F.
 (3.27)

4 Completeness of derived category of sheaves

In this section, we prove the completeness of the derived category D(kX) with respect
to the pseudo-distance dK associated with a thickening kernel K. If a category with a
persistence structure admits any sequential colimit, then the category is complete with
respect to the interleaving distance (Cruz [Cru19] and Scoccola [Sco20]). However, the
derived category does not admit sequential colimits. Hence, we construct a limit object
by using a homotopy colimit instead. Let X be a manifold throughout this section.
In Lemma 3.4, we saw that for an exact triangle F → G → H +1
−−→, if H is c-torsion,
then (F, G) is weakly (0, c)-isomorphic. Conversely, we obtain Proposition 4.2 below,
which is a key to our construction of limit objects.

Lemma 4.1. Let F ∈ D(kX) and a ∈ R≥0 and consider the exact triangle

Ka ◦ F ρa,0(F )
−−−−→ F → Cone(ρa,0(F )) +1
−−→ . (4.1)

Then Cone(ρa,0(F )) is 2a-torsion.
 14

Proof. Set C := Cone(ρa,0) and consider the following commutative diagram:

K3a ◦ F // K2a ◦ F //

  
 K2a ◦ C //

  yys s s s s K3a ◦ F [1] //

  
 K2a ◦ F [1]

♣♣♣♣♣♣♣♣♣♣♣

♣♣♣♣♣♣♣♣♣♣♣

Ka ◦ F //

  ssssssssss

ssssssssss Ka ◦ C //

  
 K2a ◦ F [1]

  
Ka ◦ F // F // C // Ka ◦ F [1].
 (4.2)

The composite morphism K2a◦C → K3a◦F [1] → K2a◦F [1] is zero since K3a◦F → K2a◦F →
K2a ◦ C +1
−−→ is an exact triangle. By the commutativity, the composite K2a ◦ C → Ka ◦ C →
K2a ◦ F [1] is also zero. Hence, there exists a morphism K2a ◦ C → Ka ◦ F that makes the
lower triangle commutative. Therefore, the morphism K2a ◦ C → C factors the composite
Ka ◦ F → F → C and hence it is zero.

Proposition 4.2. Let F, G ∈ D(kX) and assume that the pair (F, G) is (a, b)-isomorphic.
Let (α : Ka ◦ F → G, β : Kb ◦ G → F ) be an (a, b)-isomorphism for (F, G) and consider the
exact triangle
 Ka ◦ F → G → Cone(α) +1
−−→ . (4.3)

Then Cone(α) is 3(a + b)-torsion.

Proof. Consider the three exact triangles:

Ka+b ◦ F Kb◦α // Kb ◦ G // Kb ◦ Cone(α) u // Ka+b ◦ F [1],

Ka+b ◦ F ρa+b,0(F ) // F // Cone(ρa+b,0(F )) // Ka+b ◦ F [1],

Kb ◦ G β // F // Cone(β) // Kb ◦ G[1].
 (4.4)

Note that β ◦ (Kb ◦X α) = ρa+b,0(F ). By the octahedral axiom, we have the following
commutative diagram, where the bottom row is also an exact triangle:

Ka+b ◦ F Kb◦α // Kb ◦ G //

β
  
 Kb ◦ Cone(α) u //

v
  
 Ka+b ◦ F [1]

Ka+b ◦ F ρa+b,0(F ) //

Kb◦α   
 F // Cone(ρa+b,0(F )) //

  
 Ka+b ◦ F [1]

  
Kb ◦ G β //

  
 F //

  
 Cone(β) // Kb ◦ G[1]

  
Kb ◦ Cone(α) // Cone(ρa+b,0(F )) // Cone(β) // Kb ◦ Cone(α)[1].
 (4.5)

In particular, the morphism u : Kb◦Cone(α) → Ka+b◦F [1] factors through Cone(ρa+b,0(F )).
Then the commutative diagram

K2a+3b ◦ Cone(α) ρ2a+3b,b(Cone(α)) //

K2a+2b◦v   
 Kb ◦ Cone(α) u //

v   
 Ka+b ◦ F [1]

K2a+2b ◦ Cone(ρa+b,0(F )) 0 // Cone(ρa+b,0(F ))
 44✐✐✐✐✐✐✐✐✐✐✐✐✐✐✐✐✐ (4.6)

15

proves that the composite morphism in the ﬁrst row is zero by Lemma 4.1. Thus, we obtain
a morphism K3a+3b ◦ Cone(α) → Ka+b ◦ G that makes the following diagram commute,
where the vertical arrows are the corresponding ρ’s:

K3a+3b ◦ Cone(α)

uu❦ ❦ ❦ ❦ ❦ ❦ ❦
   
Ka+b ◦ G

Ka◦β

ww♦♦♦♦♦♦♦♦♦♦♦♦
   
 // Ka+b ◦ Cone(α) Kb◦u //

  
 K2a+b ◦ F [1]

Ka ◦ F α // G // Cone(α) // Ka ◦ F [1].
 (4.7)

Hence, the morphism ρ3a+3b,0(Cone(α)) factors the composite morphism Ka ◦ F → G →
Cone(α) and thus it is zero.

Theorem 4.3. Let (Fn)n∈N be a sequence of objects in D(kX) and assume that Fn and
Fn+1 are an-isomorphic with ∑n an < ∞. Set a≥n := ∑k≥n ak. Then there exists an
object F∞ ∈ D(kX) such that (Fn, F∞) is (2a≥n, 24a≥n)-isomorphic for any n ∈ N. In
particular, dK(Fn, F∞) → 0 (n → ∞).

Proof. Set Gn := Ka≥n ◦ Fn. Then we have a morphism αn,m : Gn → Gm for n ≤ m and
get an inductive system (Gn)n∈N. Let F∞ := hocolimn Gn ∈ D(kX ).
We ﬁx n and consider the cone Cn,m of the morphism αn,m : Gn → Gm. By composing
βm’s, we obtain βm,n : Gm → Gn. Since (αn,m, βm,n) gives an a≥n-isomorphism between
Gn and Gm, the cone Cn,m is 6a≥n-torsion by Proposition 4.2. Consider the following
commutative diagram with solid arrows:

G⊕N
n //

  
 ⊕
m≥n Gm //

  
 ⊕
m≥n Cn,m //

  
 G⊕N
n [1]

  
G⊕N
n //

  
 ⊕
m≥n Gm //

  
 ⊕
m≥n Cn,m //

  
 G⊕N
n [1]

  
hocolimm Gn //

  
 hocolimm≥n Gm //

  
 H //

  
 hocolimm Gn[1]

  
G⊕N
n [1] // ⊕m≥n Gm[1] // ⊕m≥n Cn,m[1] // G⊕N
n [2].
 (4.8)

Then by [KS06, Exercise 10.6], the dotted arrows can be completed so that the right
bottom square is anti-commutative, all the other squares are commutative, and all the rows
and all the columns are exact triangles. Since ⊕m≥n Cn,m is 6a≥n-torsion, H is 12a≥n-
torsion. Noticing that hocolimm Gn ≃ Gn and hocolimm≥n Gm ≃ F∞, by Lemma 3.4
(Gn, F∞) is weakly (0, 12a≥n)-isomorphic. Since we set Gn = Ka≥n ◦ Fn, we ﬁnd that
(Fn, F∞) is weakly (a≥n, 12a≥n)-isomorphic, which implies that (Fn, F∞) is (2a≥n, 24a≥n)-
isomorphic (see Remark 3.3).

Remark 4.4. One can prove a similar completeness result in a more general setting,
i.e., for a triangulated category with a persistence structure (cf. persistence triangulated
category by Biran–Cornea–Zhang [BCZ21]). Here we do not go into details.

16

Corollary 4.5. The derived category of sheaves D(kX ) is complete with respect to the
pseudo-distance dK. In particular, the Tamarkin category D(X) is complete with respect
to the pseudo-distance dD(X).

Proof. For the latter claim, it suﬃces to show that for a Cauchy sequence (Fn)n∈N in
the Tamarkin category D(X), the limit object F∞ constructed in Theorem 4.3 is also
in D(X). By construction and Lemma 3.7, after taking a subsequence, we have F∞ =
hocolimm T−a≥nFn, where (a≥n)n∈N is as in Theorem 4.3. Set Gn := T−a≥nFn. Since the
functor kX×[0,∞) ⋆ (∗) is deﬁned as the composite of left adjoint functors, it commutes
with direct sums. Since each Gn is an object of the left orthogonal ⊥D{τ ≤0}(kX×Rt ) =
D(X), in the following commutative diagram the ﬁrst and the second vertical arrows are
isomorphisms:

kX×[0,∞) ⋆ ⊕
n Gn //∼  
 kX×[0,∞) ⋆ ⊕
n Gn //∼  
 kX×[0,∞) ⋆ F∞ +1 //

  ⊕n Gn // ⊕
n Gn // F∞ +1 // .
 (4.9)

Thus, we have an isomorphism kX×[0,∞) ⋆ F∞ ∼
−→ F∞ and ﬁnd that F∞ ∈ D(X).

Remark 4.6. As mentioned in Remark 3.3, dK and distK are equivalent. Hence D(kX ) is
also complete with respect to distK.

5 Sheaf quantization of Hamiltonian diﬀeomorphisms and
homeomorphisms

In this section, we give a reﬁned Hamiltonian stability result, which state the distance
between sheaf quantizations of Hamiltonian diﬀeomorphisms is at most the Hofer distance.
By using the stability result, we also construct a sheaf quantization of a Hamiltonian
homeomorphism.

5.1 Hamiltonian stability theorem

In this subsection, we give a generalization of our previous result [AI20, Thm. 4.16].
For a timewise compactly supported function H : T ∗M × I → R, we deﬁne

E+(H) := ∫ 1

0 max
p∈T ∗M Hs(p)ds, E−(H) := − ∫ 1

0 min
p∈T ∗M Hs(p)ds,

∥H∥osc := E+(H) + E−(H) = ∫ 1

0
 ( max
p∈T ∗M Hs(p) − min
p∈T ∗M Hs(p)
) ds. (5.1)

When M = pt, we need to modify E+(H) and E−(H) so that they are non-negative.

Theorem 5.1. Let H : T ∗M × I → R be a timewise compactly supported function. Then
(K0
1, KH
1 ) is (E−(H) + ε, E+(H) + ε)-isomorphic for any ε ∈ R>0, where 0 denotes the
zero function on T ∗M × I. In particular, dD(M 2)(K0
1, KH
1 ) ≤ ∥H∥osc.

Proof. Let ε > 0 be an arbitrary positive number. We apply Proposition 3.9 to KH . Then
by (3.25), we ﬁnd that (K0
1, KH
1 ) = (KH
0 , KH
1 ) is weakly (E−(H)+ε, E+(H)+ε)-isomorphic.
It is enough to show that (K0
1, KH
1 ) is (E−(H) + ε, E+(H) + ε)-isomorphic.
We set a := E−(H)+ε and b := E+(H)+ε. Then, by deﬁnition, there exist morphisms
α, δ : K0
1 → TaKH
1 and β, γ : KH
1 → TbK0
1 such that

17

(1) K0
1 α
−→ TaKH
1 Taβ
−−→ Ta+bK0
1 is equal to τ0,a+b(K0
1) : K0
1 → Ta+bK0
1,

(2) KH
1 γ
−→ TbK0
1 Tbδ
−−→ Ta+bKH
1 is equal to τ0,a+b(KH
1 ) : KH
1 → Ta+bKH
1 , and

(3) τa,2a(KH
1 ) ◦ α = τa,2a(KH
1 ) ◦ δ and τb,2b(K0
1) ◦ β = τb,2b(K0
1) ◦ γ.

Now we let Tor be the full triangulated subcategory of D(M 2) consisting of torsion
objects {F | dD(M 2)(F, 0) < ∞}. Then, by [GS14, Prop. 6.7], the Hom set of the localized
category D(M 2)/ Tor is computed as

HomD(M 2)/ Tor(F, G) ≃ lim
−→
c→∞ HomD(M 2)(F, TcG). (5.2)

For the objects K0
1, KH
1 and d ∈ R, we have

HomD(M 2)(KH
1 , TdKH
1 ) ≃ HomD(M 2)(K0
1, TdK0
1) ≃
 {
k (d ≥ 0)
0 (d < 0). (5.3)

Hence, HomD(M 2)/ Tor(K0
1, K0
1) ≃ HomD(M 2)/ Tor(KH
1 , KH
1 ) ≃ k and the canonical mor-
phism
 HomD(M 2)(KH
1 , TdKH
1 ) → HomD(M 2)/ Tor(KH
1 , KH
1 ), α
′ ↦→ α′ (5.4)

is injective for d ≥ 0.
By the condition (3), we have

α = δ ∈ HomD(M 2)/ Tor(K0
1, KH
1 ) (5.5)

β = γ ∈ HomD(M 2)/ Tor(KH
1 , K0
1). (5.6)

Hence, through the isomorphism HomD(M 2)/ Tor(KH
1 , KH
1 ) ≃ k, we get

1 = δ ◦ γ = α ◦ β ∈ HomD(M 2)/ Tor(KH
1 , KH
1 ), (5.7)

by the condition (2). Since Tbα ◦ β ∈ HomD(M 2)(KH
1 , Ta+bKH
1 ) is sent to α ◦ β and
τ0,a+b(KH
1 ) is sent to 1, by the injectivity we obtain Tbα◦β = τ0,a+b(KH
1 ). Thus, combining
this with the condition (1), we ﬁnd that the pair (α, β) gives an (a, b)-isomorphism for the
pair (K0
1, KH
1 ), which completes the proof.

For two timewise compactly supported functions H, H ′ : T ∗M × I → R, by (3.11) and
(3.23), we have
 dD(M 2)(KH
1 , KH ′
1 ) = dD(M 2)(K0
1, KH♯H ′
1 ) ≤ ∥H − H ′∥osc. (5.8)

5.2 Sheaf quantization of Hamiltonian diﬀeomorphisms

In this subsection, we investigate sheaf quantization of Hamiltonian diﬀeomorphisms. We
keep the symbols M for a connected manifold without boundary and I for an open interval
containing [0, 1]. First, we prove the following, an analogue of Theorem 5.1 in the derived
category D(kM 2×Rt) not in the Tamarkin category D(M 2).

Proposition 5.2. Let H : T ∗M × I → R be a timewise compactly supported function.
Then, one has an inequality

dM 2×Rt(K 0
1 , K H
1 ) ≤ 4 ∫ 1

0 ∥Hs∥∞ds ≤ 4∥H∥osc. (5.9)

18

Similarly to (5.8), for two timewise compactly supported functions H, H ′ : T ∗M × I →
R, we have
 dM 2×Rt(K H
1 , K H ′
1 ) ≤ 4∥H − H ′∥osc. (5.10)

To prove the proposition, we prepare some lemmas. Let X be a manifold and let
q : X × Rt → Rt denote the projection.

Lemma 5.3. Let F ∈ D{τ ≤0}(kX×Rt ) and G ∈ D{τ ≥0}(kX×Rt ). Then there exist H, H ′ ∈
D(kX) such that F ⋆ G ≃ H ⊠ kRt and Hom
⋆(F, G) ≃ H ′ ⊠ kRt.

Proof. By Lemma 2.8, we ﬁnd that SS(F ⋆ G) ⊂ {τ = 0} and SS(Hom⋆(F, G)) ⊂ {τ = 0},
which imply the result.

For a, b ∈ R≥0, we set

D(a, b) := ⋃

−a≤c≤b
{(τ, σ) ∈ R2 | σ = c · τ }. (5.11)

Note that D(a, b) is a closed cone in R2, which is not necessarily convex. See Figure 5.1.
We set D+(a, b) := D(a, b) ∩ {(τ, σ) | τ ≥ 0} and D−(a, b) := D(a, b) ∩ {(τ, σ) | τ ≤ 0}.

O

σ
 τ

σ = b · τ

σ = −a · τ

Figure 5.1: D(a, b)

Lemma 5.4. Let F → G → H +1
−−→ be an exact triangle in D(kX×Rt) and a, b ∈ R≥0.
Assume

(1) F ∈ D{τ ≤0}(kX×Rt) and F is a-torsion,

(2) G ∈ D{τ ≥0}(kX×Rt ) and G is b-torsion.

Then, RHom(F, G) ≃ 0. In particular, H ≃ G ⊕ F [1] is max(a, b)-torsion.

Proof. By Lemma 5.3, there exists H ′ ∈ D(kX ) such that Hom⋆(F, G) ≃ H ′ ⊠ kRt.
Moreover by the isomorphism Tb Hom⋆(F, G) ≃ Hom⋆(F, TbG), we ﬁnd that Hom⋆(F, G)
is b-torsion. Hence we have Hom⋆(F, G) ≃ 0 and

RHom(F, G) ≃ RHom(kX×{0} ⋆ F, G)

≃ RHom(kX×{0}, Hom⋆(F, G)) ≃ 0, (5.12)

which proves the result.

Next, we give a microlocal cut-oﬀ result, which we use to reduce the problem to
Proposition 3.9.
 19

Lemma 5.5. Let H ∈ D(kX×Rt×R) and assume that there exist a, b ∈ R≥0 such that

SS(H) ⊂ T ∗X × (Rt × R) × D(a, b). (5.13)

Then there exists an exact triangle H− → H+ → H +1
−−→ in D(kX×Rt×R) such that
SS(H−) ⊂ T ∗X × (Rt × R) × D−(a, b) and SS(H+) ⊂ T ∗X × (Rt × R) × D+(a, b).

Proof. Let λ := {(t, s) | t ≥ 0, s = 0}. Then we get an exact triangle

kX×(λ\{0}) ⋆ H −→ kX×λ ⋆ H −→ H +1
−−→ (5.14)

with SS(kX×λ ⋆ H) ⊂ T ∗X × (Rt × R) × D(a, b) ∩ {(τ, σ) | τ ≥ 0}. Moreover kX×λ ⋆ F → F
is an isomorphism on T ∗X × (Rt × R) × Int(λ◦), where λ◦ denotes the polar cone of
λ. Thus, we conclude that SS(kλ\{0} ⋆ H) ⊂ T ∗X × (Rt × R) × (D(a, b) \ Int(λ◦)) =
T ∗X × (Rt × R) × D−(a, b).

The following is a variant of [AI20, Prop. 4.3].

Proposition 5.6. Let H ∈ D(kX×Rt×I) and s1 < s2 ∈ I. Assume that there exist
a, b ∈ R≥0 and r ∈ R>0 such that

SS(H) ∩ π−1(X × Rt × (s1 − r, s2 + r)) ⊂ T ∗X × (Rt × I) × D(a, b). (5.15)

(i) Let q : X × Rt × I → X × Rt be the projection. Then Rq∗HX×Rt×(s1,s2] and
Rq∗HX×Rt×[s1,s2) are (max(a, b)(s2 − s1) + ε)-torsion for any ε ∈ R>0.

(ii) One has dX×Rt(H|X×Rt×{s1}, H|X×Rt×{s2}) ≤ 4 max(a, b)(s2 − s1).

Proof. (i) Choose a diﬀeomorphism ϕ : (s1 − r, s2 + r) ∼
−→ R satisfying ϕ|[s1,s2] = id[s1,s2]
and dϕ(s) ≥ 1 for any s ∈ (s1 − r, s2 + r). Set Φ := idX×Rt ×ϕ : X × Rt × (s1 − r, s2 + r) ∼
−→
X × Rt × R and H′ := Φ∗H ∈ D(kX×Rt×R). Then by the assumption on ϕ, we have

SS(H′) ⊂ T ∗X × (Rt × R) × D(a, b) (5.16)

and H′|X×Rt×[s1,s2] ≃ H|X×Rt×[s1,s2]. Hence, we may assume I = R from the beginning.

Applying Lemma 5.5, we have an exact triangle H− → H+ → H +1
−−→ in D(kX×Rt×R)
with SS(H−) ⊂ T ∗X × (Rt × R) × D−(a, b) and SS(H+) ⊂ T ∗X × (Rt × R) × D+(a, b).
By [AI20, Prop. 4.3], Rq∗H+
X×Rt×(s1,s2] is (b(s2 − s1) + ε)-torsion. Similarly we ﬁnd that
Rq∗H−
X×Rt×(s1,s2] is (a(s2 − s1) + ε)-torsion. Here we have an exact triangle

Rq∗H−
X×Rt×(s1,s2] −→ Rq∗H+
X×Rt×(s1,s2] −→ Rq∗HX×Rt×(s1,s2] +1
−−→ (5.17)

with Rq∗H+
X×Rt×(s1,s2] ∈ D{τ ≥0}(kX×Rt) and Rq∗H−
X×Rt×(s1,s2] ∈ D{τ ≤0}(kX×Rt ). Hence,
by Lemma 5.4 we ﬁnd that Rq∗HX×Rt×(s1,s2] is (max(a, b)(s2 − s1) + ε)-torsion. The proof
for the other case is similar.
(ii) We have the following two exact triangles

Rq∗HX×Rt×(s1,s2] −→ Rq∗HX×Rt×[s1,s2] −→ H|X×Rt×{s1} +1
−−→, (5.18)

Rq∗HX×Rt×[s1,s2) −→ Rq∗HX×Rt×[s1,s2] −→ H|X×Rt×{s2} +1
−−→ . (5.19)

Hence, by the result of (i) and Lemma 3.4, the two pairs (Rq∗HX×Rt×[s1,s2], H|X×Rt×{s1})
and (Rq∗HX×Rt×[s1,s2], H|X×Rt×{s2}) are weakly (0, (max(a, b)(s2 − s1) + ε))-isomorphic.
Hence, the result follows from the triangle inequality.

20

The following proposition is a variant of Proposition 3.9.

Proposition 5.7. Let I be an open interval containing the closed interval [0, 1] and H ∈
D(kX×Rt×I ). Assume that there exist continuous functions f, g : I → R≥0 satisfying

SS(H) ⊂ T ∗X × {(t, s; τ, σ) | (τ, σ) ∈ D(f (s), g(s))}. (5.20)

Then dX×Rt(H|X×Rt×{0}, H|X×Rt×{1}) ≤ 4 ∫ 1
0 max(f, g)(s)ds.

Proof. We can apply an argument similar to [AI20, Prop. 4.15]. We only need to replace
[AI20, Prop. 4.3] with Proposition 5.6.

Proof of Proposition 5.2. The result follows from (3.25) and Proposition 5.7.

Remark 5.8. One could prove an inequality

dM 2×Rt(K 0
1 , K H
1 ) ≤ 2 ∫ 1

0 ∥Hs∥∞ds, (5.21)

which is stronger than Proposition 5.2. Indeed, by the proof of Proposition 5.6, we have
proved that under the assumption of Proposition 5.7 (H|X×Rt×{0}, H|X×Rt×{1}) is weakly
(
∫ 1
0 max(f, g)(s)ds + ε, ∫ 1
0 max(f, g)(s)ds + ε)-isomorphic for any ε ∈ R>0. Hence, we ﬁnd
that (K 0
1 , K H
1 ) is weakly (
∫ 1
0 ∥Hs∥∞ds + ε, ∫ 1
0 ∥Hs∥∞ds + ε)-isomorphic for any ε ∈ R>0.
It remains to apply an argument similar to the proof of Theorem 5.1. However, we do not
need this stronger inequality in this paper.

It is proved in [Zha20, Prop. 4.3] that the restriction of the sheaf quantization K H to
s = 1 depends only on the relative homotopy class of the path [s ↦→ φH
s ]. Now we prove
the following stronger result, which claims that the restriction depends only on the time-1
map.

Proposition 5.9. Let H : T ∗M × I → R be a timewise compactly supported function.
Then the objects ̃K H
1 , K H
1 , KH
1 are determined by the time-1 map φH
1 .

Proof. We shall prove K H
1 = K H ′
1 assuming that φH ′
1 = φH
1 . By (3.23), it suﬃces to show

that K H♯H ′
1 ≃ k∆M ×{0}. Hence, we may assume that H ′ ≡ 0 and φH
1 = idT ∗M .
Since us ≡ 0 by Lemma 3.11, we ﬁnd that ˚SS(K H
1 ) = ˚T ∗
∆M ×{0}(M 2 × Rt) and K H
1 is
simple along the subset. Moreover, since K H
0 ≃ k∆M ×{0} and u is compactly supported and
hence bounded, K H|M 2×{R}×I and K H|M 2×{−R}×I are 0 for suﬃciently large R. Hence,
there exists a rank one local system L on M such that K H
1 ≃ δM ∗L ⊠ k{0}[m], where m
is some integer. By Proposition 5.2, we have

dM 2×Rt(k∆M ×{0}, δM ∗L ⊠ k{0}[m]) = dM 2×Rt(K 0
1 , K H
1 ) ≤ 4∥H∥osc < ∞. (5.22)

By restricting to {(x, x)}×R ⊂ M 2×Rt for some x ∈ M , we obtain dRt(k{0}, k{0}[m]) < ∞
and ﬁnd that m = 0. Then, we have

RΓ(M ; L) ≃ RΓ(M 2 × Rt; K H
1 ) ≃ RΓ(M 2 × Rt; K 0
1 ) ≃ RΓ(M ; kM ). (5.23)

In particular, H 0(M ; L) ≃ H 0(M ; kM ), which implies that L is trivial.

The proposition above shows the well-deﬁnedness in the following deﬁnition.

21

Deﬁnition 5.10. (i) A diﬀeomorphism ϕ : T ∗M → T ∗M is said to be a compactly
supported Hamiltonian diﬀeomorphism if it is the time-1 map of some compactly
supported Hamiltonian isotopy φH, that is ϕ = φH
1 . The set of compactly supported
Hamiltonian diﬀeomorphisms is denoted by Hamc(T ∗M, ω).

(ii) The Hofer metric between Hamiltonian diﬀeomorphisms is deﬁned by

dH(ϕ, ϕ
′) := inf {∥H∥osc ∣
∣ φ
H
1 = ϕ
−1ϕ
′} (5.24)

for ϕ, ϕ′ ∈ Hamc(T ∗M, ω).

(iii) For ϕ ∈ Hamc(T ∗M, ω), one sets ̃K ϕ := ̃K H
1 , K ϕ := K H
1 , and Kϕ := KH
1 , where H
is any timewise compactly supported function with ϕ = φH
1 .

By (5.8) and (5.10), we have the following.

Theorem 5.11. For ϕ, ϕ′ ∈ Hamc(T ∗M, ω), one has

dD(M 2)(Kϕ, Kϕ′) ≤ dH (ϕ, ϕ
′),

dM 2×Rt(K ϕ, K ϕ′) ≤ 4dH (ϕ, ϕ
′). (5.25)

5.3 Sheaf quantization of Hamiltonian homeomorphisms

In this subsection, we construct a sheaf quantization of a limit of Hamiltonian diﬀeomor-
phisms with respect to the Hofer metric.

Proposition 5.12. Let (ϕn)n∈N ⊂ Hamc(T ∗M, ω) be a sequence of compactly supported
Hamiltonian diﬀeomorphisms and Kn := K ϕn ∈ D(kM 2×Rt) the sheaf quantization of ϕn.
Assume that it is a Cauchy sequence with respect to the Hofer metric dH . Then there
exists an object K∞ ∈ D(kM 2×Rt) such that dM 2×Rt(Kn, K∞) → 0 (n → ∞). Moreover,
such an object is unique up to isomorphism, and the endofunctor K∞ • (∗) on D(kM ×Rt)
gives an equivalence of categories.

Proof. By (5.10), we have
 dM 2×Rt(Kn, Km) ≤ 4dH (ϕn, ϕm), (5.26)

which proves that (Kn)n∈N is a Cauchy sequence in D(kM 2×Rt) with respect to dM 2×Rt.
Hence, Corollary 4.5 shows the existence of a limit object.
Let K ′
∞ be another limit object that satisﬁes dM 2×Rt(K∞, K ′
∞) = 0. There exists
Kn ∈ D(kM 2×Rt) such that K n • Kn ≃ Kn • K n ≃ k∆M ×{0} for each n. Then we ﬁnd
that the sequence (K n)n∈N is also Cauchy, and we can take a limit object K∞. The
Cauchy sequence (K n • Kn)n∈N converges to both K ∞ • K∞ and k∆M ×{0}. Hence we have
dM 2×Rt(K ∞ • K∞, k∆M ×{0}) = 0. Similarly, we have dM 2×Rt(K ′
∞ • K ∞, k∆M ×{0}) = 0.
By Lemma 5.16 below, we have K∞ • K∞ ≃ k∆M ×{0} ≃ K ′
∞ • K ∞. Hence, we conclude
that K ′
∞ ≃ K ′
∞ • K∞ • K∞ ≃ K∞ and K ∞ • (∗) gives the inverse.

Note that we have an inequality similar to (3.11) for dX×Rt .

Lemma 5.13. Let F, G ∈ D{τ ≥0}(kRt ). If dRt (F, G) = 0, then ˚SS(F ) = ˚SS(G).

22

Proof. We prove ˚SS(F ) ⊂ ˚SS(G) by contradiction. Choose (t0; 1) ∈ ˚SS(F ) \ ˚SS(G). There
exists a neighborhood (a, b) of t0 in Rt such that (a, b) ∩ π( ˚SS(G)) = ∅. There also
exist t1, t2 ∈ R such that a < t1 < t2 < b and the restriction map RΓ((−∞, t2); F ) →
RΓ((−∞, t1); F ) is not an isomorphism. We may choose t1 and t2 arbitrarily close to t0. On
the other hand, RΓ((−∞, t′′); G) → RΓ((−∞, t′); G) is an isomorphism for any a < t′ <
t′′ < b by the microlocal Morse lemma. Thus, an interleaving between (RΓ((−∞, t); F ))t∈R
and (RΓ((−∞, t); G))t∈R leads to a contradiction.

Lemma 5.14. Let F, G ∈ D(kRt ) and assume that dRt (F, G) = 0. Then SS(F ) = SS(G)
and hence Supp(F ) = Supp(G).

Proof. Since dRt(F ⋆ k[0,∞), G ⋆ k[0,∞)) = 0, we have

SS(F ) ∩ {τ > 0} = ˚SS(F ⋆ k[0,∞)) = ˚SS(G ⋆ k[0,∞)) = SS(G) ∩ {τ > 0} (5.27)

by Lemma 5.13. Similarly, we obtain

SS(F ) ∩ {τ < 0} = ˚SS(F ⋆ k(0,∞)) = ˚SS(G ⋆ k(0,∞)) = SS(G) ∩ {τ < 0} (5.28)

and hence ˚SS(F ) = ˚SS(G). Note that U := Rt \ π( ˚SS(F )) = Rt \ π( ˚SS(G)) is an open
subset of Rt, and both F |U and G|U are locally constant. Thus dX×Rt(F, G) = 0 implies
F |U ≃ G|U .

Lemma 5.15. For F, G ∈ D(kX×Rt ), dX×Rt(F, G) = 0 implies Supp(F ) = Supp(G).

Proof. Let (x, t) ∈ X × Rt \ Supp(G). Take an open neighborhood x ∈ U in X and
ε > 0 so that U × (t − ε, t + ε) ⊂ X × Rt \ Supp(G). Note that for any y ∈ X, 0 ≤
dRt(F |{y}×Rt , G|{y}×Rt ) ≤ dX×Rt(F, G) = 0 and Supp(G|{y}×Rt ) ⊂ Supp(G) ∩ ({y} × Rt).
By Lemma 5.14, F |{y}×(t−ε,t+ε) ≃ 0 for any y ∈ U . Hence, we obtain F |U ×(t−ε,t+ε) ≃ 0 and
Supp(F ) ⊂ Supp(G). We obtain the converse inclusion Supp(F ) ⊃ Supp(G) similarly.

Lemma 5.16. Let F, G ∈ D(kX×Rt) and assume that dX×Rt(F, G) = 0 and Supp(G) ⊂
X × {0}. Then F ≃ G.

Proof. By Lemma 5.15, we have Supp(F ) = Supp(G) ⊂ X × {0}. We may write F ≃
F ′ ⊠ k{0} and G ≃ G′ ⊠ k{0} with some F ′, G′ ∈ D(kX ). Take ε > 0 arbitrarily. Note
that Kε ◦ F ≃ F ′ ⊠ k[−ε,ε] and Kε ◦ G ≃ G′ ⊠ k[−ε,ε]. Hence, there exist morphisms
α : F ′ ⊠ k[−ε,ε] → G′ ⊠ k{0} and β : G′ ⊠ k[−ε,ε] → F ′ ⊠ k{0} such that (α, β) is a ε-
isomorphism of (F, G). Restricting α and β on X × {0}, we obtain isomorphisms between
F ′ and G′.

Note that Petit–Schapira–Waas [PSW21] proved that dist(F, G) = 0 if and only if
F ≃ G when F and G are constructible sheaves up to inﬁnity on a real analytic manifold.
This result, as well as its proof, is diﬀerent from ours and is not related to the Tamarkin
category.
Proposition 5.12 shows that we can associate a sheaf with an element of the metric
completion of Hamc(T ∗M, ω) with respect to the Hofer metric dH as follows. Let (ϕn)n∈N
be a Cauchy sequence of Hamiltonian diﬀeomorphisms and Kn := K ϕn for n ∈ N. By
Proposition 5.12, we obtain a limit object K∞ of the sequence (Kn)n∈N. The argument
in the proof of the proposition also shows that another Cauchy sequence equivalent to
(ϕn)n∈N gives the same limit object K∞ up to isomorphism.

23

Deﬁnition 5.17. Let [(ϕn)n∈N] be an element of the completion of Hamc(T ∗M, ω) with
respect to dH . The limit sheaf K∞ deﬁned as above is denoted by K [(ϕn)n] and called the
sheaf quantization of [(ϕn)n∈N].

We use the above construction to obtain a sheaf quantization of a Hamiltonian home-
omorphism of T ∗M .

Deﬁnition 5.18 (Oh–M¨uller [OM07]). Let φ = (φs)s : T ∗M × I → T ∗M be an isotopy
of homeomorphisms of T ∗M . The isotopy φ is said to be a continuous Hamiltonian
isotopy if there exist a compact subset C ⊂ T ∗M and a sequence of smooth functions
Hn : T ∗M × I → R timewisely supported in C satisfying the following two conditions.

(1) The sequence of ﬂows (φHn)n∈N C 0-converges to φ, uniformly in s ∈ I.

(2) The sequence (Hn)n∈N converges uniformly to a continuous function H : T ∗M × I →
R. That is, ∥Hn − H∥∞ → 0.

In this case, H is said to generate φ. A homeomorphism of T ∗M is called a Hamiltonian
homeomorphism if it is the time-1 map of a continuous Hamiltonian isotopy.

The following uniqueness theorems hold.

(i) A continuous Hamiltonian function generates a unique continuous Hamiltonian iso-
topy (Oh–M¨uller [OM07]).

(ii) A continuous Hamiltonian isotopy can be generated by a unique continuous Hamil-
tonian function up to addition of a function of time (Viterbo [Vit06]).

A continuous Hamiltonian isotopy φ deﬁnes an element of the metric completion of
Hamc(T ∗M, ω) with respect to dH. Indeed, for a sequence (Hn)n∈N satisfying the condi-
tion (2) in Deﬁnition 5.18, (φ
Hn
1 )n∈N forms a Cauchy sequence with respect to the Hofer
metric dH . Moreover, the element in the metric completion is independent of the choice of
a sequence (Hn)n∈N. Thus we obtain a sheaf K∞ as in Deﬁnition 5.17. We give a bound of
the microsupport of K∞. Set ϕn = φ
Hn
1 and Kn := K ϕn. By construction, after taking a
subsequence of (Kn)n∈N if necessary, K∞ ≃ hocolimn kM ×[−a≥n,a≥n] ⋆ Kn, where (a≥n)n∈N
is as in Theorem 4.3. Hence, we have

˚SS(K∞) ⊂
 {

((x′; ξ′), (x; −ξ), (t; τ ))
 ∣
∣
∣
∣
∣ (x; ξ) ∈ T ∗M,

(x′; ξ′/τ ) = ϕ∞(x; ξ/τ )
}
 (5.29)

by the condition (1) and Lemma 2.9.

Remark 5.19. For the microsupport estimate above, we do not need the full convergence
of ﬂows, but only the convergence of the time-1 maps, that is, ϕn → ϕ∞ (n → ∞).

Deﬁnition 5.20. Let φ be a continuous Hamiltonian isotopy associated with a continuous
function H : T ∗M × I → R and ϕ∞ := φ1 a Hamiltonian homeomorphism. The limit sheaf
K∞ deﬁned as above is denoted by K H
1 = K ϕ∞ and called the sheaf quantization of the
Hamiltonian homeomorphism ϕ∞. One also sets Kϕ∞ := Pl(K ϕ∞ ) ∈ D(M 2).

We can also prove the following, which justiﬁes the notation K ϕ∞.

Proposition 5.21. In the situation of Deﬁnition 5.20, the object K H
1 depends only on
the time-1 map φ1.
 24

Proof. It suﬃces to show that if φ1 = idT ∗M then K H
1 ≃ k∆M ×{0}. We ﬁrst prove the
following lemma.

Lemma 5.22. Let G ∈ D(kRt) with dRt (G, k{0}) < ∞. Assume that there exists ε > 0
such that for any a < b with b − a < ε, one has G ⋆ k[a,b) ≃ k[a,b) and G ⋆ k(a,b] ≃ k(a,b].
Then, G ≃ k{0}.

Proof. First, we prove ˚SS(G ⋆ k[0,∞)) ⊂ {(0; τ ) | τ > 0} by contradiction. Note that we
already know that SS(G ⋆ k[0,∞)) ⊂ {τ ≥ 0} by Lemma 2.8. Assume that there exists
(t0; 1) ∈ ˚SS(G ⋆ k[0,∞)) with t0 ̸= 0. Then, there exist t1, t2 ∈ R such that t1 < t2 and the
restriction map RΓ((−∞, t2); G⋆k[0,∞)) → RΓ((−∞, t1); G⋆k[0,∞)) is not an isomorphism.
We may choose t1 and t2 arbitrary close to t0 and hence may assume t2 − t1 < min{t1, ε}
if t0 > 0 and t2 < 0, t2 − t1 < ε if t0 < 0. Applying G ⋆ (∗) to the exact triangle
k[0,t2−t1) → k[0,∞) → k[t2−t1,∞) +1
−−→, we have an exact triangle

k[0,t2−t1) → G ⋆ k[0,∞) → Tt2−t1G ⋆ k[0,∞) +1
−−→ . (5.30)

Since RΓ((−∞, t2); k[0,t2−t1)) = 0, we get an isomorphism

RΓ((−∞, t2); G ⋆ k[0,∞)) ∼
−→ RΓ((−∞, t1); G ⋆ k[0,∞)). (5.31)

The morphism coincides with the restriction map by the construction, which is a contra-
diction.
Similarly, we obtain ˚SS(G ⋆ k(0,∞)) ⊂ {(0; τ ) | τ < 0}.
We get ˚SS(G) ⊂ T ∗
0 Rt by applying G ⋆ (∗) to the exact triangle k(0,∞) → k[0,∞) →

k{0} +1
−−→. Hence, we obtain the desired isomorphism from dRt(G, k{0}) < ∞.

Now let φ be a continuous Hamiltonian isotopy generated by a continuous function
H : T ∗M × I → R and assume that φ1 = idT ∗M . By the microsupport estimate (5.29),
we get π( ˚SS(K H
1 )) ⊂ ∆M × R. By construction, dM 2×Rt(k∆M ×{0}, K H
1 ) < ∞. Restricting
to (M 2 \ ∆M ) × Rt, we ﬁnd that d(M 2\∆M )×Rt (0, K H
1 |(M 2\∆M )×Rt ) < ∞, which implies
K H
1 |(M 2\∆M )×Rt ≃ 0. Hence, we can write K H
1 ≃ (δM × idRt)∗K ′ with K ′ ∈ D(kM ×Rt).
Again by the estimate (5.29) and Proposition 2.3(i), we ﬁnd that SS(K ′) ⊂ 0M × T ∗Rt.
Let us keep the notation of a compact set C ⊂ T ∗M and Kn = K ϕn as above (see also
Deﬁnition 5.18). For F ∈ D(kM ×Rt) such that

˚SS(F ) ∩ {(x, t; ξ, τ ) | τ ̸= 0, (x; ξ/τ ) ∈ C} = ∅, (5.32)

we have Kn • F ≃ F for any n ∈ N, which implies dM ×Rt(K H
1 • F, F ) = 0. For each
x0 ∈ M and a < b ∈ R with suﬃciently small b − a, there exists F ∈ D(kM ×Rt) such
that (1) its microsupport does not intersect the cone {(x, t; ξ, τ ) | τ ̸= 0, (x; ξ/τ ) ∈ C} of
C and (2) F |{x0}×Rt ≃ k[a,b). For example, such F is obtained as the sheaf quantization
of an exact Lagrangian immersion of a sphere. Therefore, dRt(K ′|{x0}×Rt ⋆ k[a,b), k[a,b)) ≤
dM ×Rt(K H
1 • F, F ) = 0 if b − a is suﬃciently small. Applying Lemma 5.14 to K ′|{x0}×Rt ⋆
k[a,b) and k[a,b), we get K ′|{x0}×Rt ⋆ k[a,b) ≃ k[a,b). Similarly, we obtain K ′|{x0}×Rt ⋆ k(a,b] ≃
k(a,b] for any x0 ∈ M and suﬃciently small b − a.
Hence, for any x0 ∈ M , K ′|{x0}×Rt ∈ D(kRt) satisﬁes the condition of Lemma 5.22.
Combining this with the estimate of SS(K ′), we may write K ′ = L ⊠ k{0}, where L is a
rank one local system. Again by the fact that dM 2×Rt(k∆M ×{0}, K H
1 ) < ∞, we conclude
that L = kM , which proves K H
1 ≃ k∆M ×{0}.

25

6 Spectral invariants in Tamarkin category

In this section, we deﬁne spectral invariants for an object of the Tamarkin category and
develop Lusternik–Schnirelmann theory. Most of the deﬁnitions and the results were
announced to appear in Humili`ere–Vichery [HV].

Deﬁnition 6.1. Let F ∈ D(M ).

(i) For n ∈ Z, one deﬁnes
 Qn
c (F ) := Hom(kM ×[0,∞), TcF [n]) (6.1)

≃ H n RHom(kM ×[−c,∞), F ),

Qn
∞(F ) := lim
−→
c→∞ Qn
c (F ). (6.2)

Set Q∗
c (F ) := ⊕
n∈Z Qn
c (F ) and similarly for Q∗
∞(F ). Denote the canonical map by
ic : Q∗
c(F ) → Q∗
∞(F ).

(ii) For α ∈ Q∗
∞(F ), one deﬁnes

c(α; F ) := inf{c ∈ R | α ∈ Im ic} (6.3)

and calls it the spectral invariant of F for α.

(iii) One deﬁnes
 Spec(F ) := {c(α; F ) ∈ R | α ∈ Q∗
∞(F )} ⊂ R. (6.4)

Remark 6.2. In our deﬁnition, c(0; F ) = −∞. In general, c(α; F ) can be −∞ for non-
zero α ∈ Q∗
∞(F ). We give such an example when M = pt. Let G := ∏n∈Z≥1 k[−n,n)[1]
and deﬁne g : k[0,∞) → G to be the product ∏
n∈Z≥1 gn, where gn : k[0,∞) → k[−n,n)[1] is
a non-trivial morphism. Set F := Pl(G), the projection to D(pt). Then the projector
Pl induces a morphism ˜g : k[0,∞) → F in D(pt), which satisﬁes [˜g] ̸= 0 in Q0
∞(F ) and
c([˜g]; F ) = −∞.

Let t : M × Rt → Rt be the projection and let Γdt denote the graph of the 1-form dt:

Γdt := {(x, t; 0, 1) | (x, t) ∈ M × Rt}. (6.5)

Note that
 Spec(F ) ⊂ {−c ∈ Rt | c ∈ tπ(SS(F ) ∩ Γdt)}. (6.6)

In order to state Lusternik–Schnirelmann theory for sheaves, we recall the algebraic
counterpart of cup-length, which is studied in [AI23].

Deﬁnition 6.3. Let R be an associative (not necessarily commutative) non-unital ring
over k. For a right R-module A, one deﬁnes

clR(A) := inf
 {

k − 1
 ∣
∣
∣
∣
∣ k ∈ N, a0 · r1 · · · rk = 0

for any a0 ∈ A and (r1, . . . , rk) ∈ Rk
}
 ∈ Z≥−1 ∪ {∞}. (6.7)

We note that clR(A) = −1 if and only if A = 0. If there is no risk of confusion, we
simply write cl(A) for clR(A). By deﬁnition, we have the following lemma.

26

Lemma 6.4. For an exact sequence of right R-modules 0 → A → B → C → 0, one has

cl(B) ≤ cl(A) + cl(C) + 1. (6.8)

Let F ∈ D(M ). Then, we have a right action of End(kM ×[0,∞)) ≃ H ∗(M ; k) on Q∗
c(F ),
which induces an action on Q∗
∞(F ). Hereafter we set R := ⊕
n≥1 H n(M ; k) and consider
the cup-length over R. Note that the cup-length over R is always ﬁnite.

Theorem 6.5. Let F ∈ D(M ). Assume that t is proper on Supp(F ) and there exists
c ≪ 0 satisfying ic = 0. Let πM : T ∗(M × Rt) → M denote the projection. If # Spec(F ) ≤
cl(Q∗
∞(F )), then there exists c ∈ Spec(F ) such that πM (SS(F ) ∩ Γdt ∩ π−1t−1(−c)) is
cohomologically non-trivial in M . That is, for any open neighborhood U of πM (SS(F ) ∩
Γdt ∩ π−1t−1(−c)), the restriction map ⊕
n≥1 H n(M ; k) → ⊕
n≥1 H n(U ; k) is non-zero.

For F ∈ D(M ), if F |M ×(c,∞) is locally constant for c ≫ 0, then ic = 0 for c ≪ 0. If
the conclusion holds, then πM (SS(F ) ∩ Γdt) is also cohomologically non-trivial in M .
For the proof of the theorem, we prepare some notation. For d ∈ R, we deﬁne

Q∗
∞,d(F ) := Im(id : Q∗
d(F ) → Q∗
∞(F )) ⊂ Q∗
∞(F ). (6.9)

Then we get the following properties:

(1) If d < d′, then Q∗
∞,d(F ) ⊂ Q∗
∞,d′(F ).

(2) If [d, d′] ∩ Spec(F ) = ∅, then Q∗
∞,d(F ) ≃ Q∗
∞,d′(F ).

(3) For d < d′, there exists an exact sequence of right H ∗(M ; k)-modules

0 → Q∗
∞,d(F ) → Q∗
∞,d′(F ) → Q∗
∞,d′(F )/Q∗
∞,d(F ) → 0. (6.10)

Moreover, we have

cl(H ∗
M ×[−d′,−d)(M × R; F )) ≥ cl(Q∗
∞,d′(F )/Q∗
∞,d(F )). (6.11)

Proof of Theorem 6.5. If Q∗
∞(F ) ≃ 0, then cl(Q∗
∞(F )) = −1 and there is nothing to prove.
Suppose that Q∗
∞(F ) ̸= 0. Since cl(Q∗
∞(F )) is ﬁnite, we may assume that Spec(F ) is
ﬁnite and set Spec(F ) = {c1, . . . , cN } with c1 < c2 < · · · < cN . Let d0, d1, . . . , dN ∈ R
such that d0 < c1 < d1 < · · · < dN −1 < cN < dN . Note that Q∗
∞,d0(F ) = 0 by the
assumption and Q∗
∞,dN (F ) = Q∗
∞(F ). Applying Lemma 6.4 to the exact sequence (6.10)
with d = di−1, d′ = di, by induction we get

cl(Q∗
∞(F )) ≤ N − 1 +
 N∑

i=1 cl(Q∗
∞,di(F )/Q∗
∞,di−1 (F )). (6.12)

Hence if # Spec(F ) = N ≤ cl(Q∗
∞(F )), there exists i ∈ {1, . . . , N } such that

cl(Q∗
∞,di(F )/Q∗
∞,di−1 (F )) ≥ 1. (6.13)

For such i above, we claim that πM (SS(F ) ∩ Γdt ∩ π−1t−1(−ci)) is cohomologically
non-trivial in M . For c ∈ R and I ⊂ R, set

Kc := πM (SS(F ) ∩ Γdt ∩ π−1t−1(−c)), KI := ⋃

c∈I Kc ⊂ M. (6.14)

Let U be any open neighborhood of Kci in M . We take Kci ⊂ U0 ⋐ U1 ⋐ U and a
C ∞-function ρ : M → R such that
 27

(1) ρ(x) ∈ [−1, 1] for any x ∈ M ,

(2) ρ|U0 ≡ 1,

(3) ρ|M \U1 ≡ −1.

Then there exists ε > 0 such that K[ci−ε,ci+ε] ⊂ U0. Taking 0 < ε′ ≪ ε and setting
ρ′ := ε′ρ : M → R, we may assume

(x, t; sρ
′(x), 1) ̸∈ SS(F ) (6.15)

for x ∈ U1 \ U0, t ∈ [−ci − ε′, −ci + ε′], and s ∈ [0, 1]. Hence, we can apply the microlocal
Morse lemma to F and (Vs)s∈[0,1], where

Vs := {(x, t) ∈ M × Rt | t < −ci + (s − 1)ε
′ − sρ
′(x)}, (6.16)

and obtain an isomorphism

RΓ(M × (−∞, −ci − ε
′); F ) = RΓ(U0; F ) ∼
−→ RΓ(U1; F ). (6.17)

We set X = M × R and

Z := M × (−∞, −ci + ε
′) \ U1 = {(x, t) ∈ M × Rt | −ci − ρ
′(x) ≤ t < −ci + ε
′}. (6.18)

By the above isomorphism, we get a morphism of exact triangles

RΓM ×[−ci+ε′,∞)(X; F ) //∼  
 RΓM ×[−ci+ε′,∞)∪Z (X; F ) //∼  
 RΓZ (X; F ) //

  
RΓM ×[−ci+ε′,∞)(X; F ) // RΓM ×[−ci−ε′,∞)(X; F ) // RΓM ×[−ci−ε′,−ci+ε′)(X; F ) // ,

(6.19)

where the middle vertical morphism is an isomorphism by the above argument. Hence, by
the ﬁve lemma, we have an isomorphism

RΓM ×[−ci−ε′,−ci+ε′)(M × Rt; F ) ∼
←− RΓZ (M × Rt; F ) ≃ RHom(kZ , F ). (6.20)

Since Supp(kZ ) = Z ⊂ U1 × [−ci − ε′, −ci + ε′], the action of H ∗(M ; k) on H ∗
Z(M × Rt; F )
factors through H ∗(U1). Hence, we have

cl(H ∗(U1)) ≥ cl(H ∗
Z(M × Rt; F ))

= cl(H ∗
M ×[−ci−ε′,−ci+ε′)(M × Rt; F ))

≥ cl(Q∗
∞,c+ε′(F )/Q∗
∞,c−ε′(F )) ≥ 1.
 (6.21)

Thus, we conclude that U1 is cohomologically non-trivial in M , which implies that U is
also cohomologically non-trivial in M .

We consider the spectral invariants for the sheaf associated with a Hamiltonian diﬀeo-
morphism/homeomorphism and a compact exact Lagrangian submanifold.
Let L be a compact exact Lagrangian submanifold of T ∗M . Take a function f : L → R
satisfying αT ∗M |L = df and deﬁne

̂L := {(x, t; ξ, τ ) | τ > 0, (x; ξ/τ ) ∈ L, t = −f (x; ξ/τ )}. (6.22)

28

In this setting, Guillermou [Gui12] (see also [Gui23; Vit19]) proved the existence and the
uniqueness of an object FL ∈ D(M ) that satisﬁes ˚SS(FL) = ̂L and FL|M ×(c,∞) ≃ kM ×(c,∞)
for a suﬃciently large c > 0. We call FL the canonical simple sheaf quantization of L.
When L = 0M and f ≡ 0, we have F0M ≃ kM ×[0,∞).
Moreover, let ϕ ∈ Hamc(T ∗M, ω) be a compactly supported Hamiltonian diﬀeomor-
phism. We deﬁne the set of spectral invariants of Spec(ϕ, L) of the Lagrangian submanifold
ϕ(L) by
 Spec(ϕ, L) := Spec(Kϕ • FL), (6.23)

where Kϕ ∈ D(M 2) is the sheaf quantization of ϕ. This set is well-deﬁned up to shift. By
a result of Viterbo [Vit19], Spec(ϕ, L) is equal to the set of the Floer-theoretic spectral
invariants associated with 0M and ϕ(L). If two Hamiltonian diﬀeomorphisms ϕ, ϕ′ ∈
Hamc(T ∗M, ω) satisfy ϕ(L) = ϕ′(L), then there exists some constant C ∈ R such that

Spec(Kϕ • FL) = Spec(Kϕ′ • FL) + C. (6.24)

Indeed, since both of Kϕ • FL and Kϕ′ • FL are canonical simple sheaf quantizations of
ϕ(L), by the uniqueness result, we have Kϕ • FL ≃ Tc(Kϕ′ • FL) for some c ∈ R.
Let ϕ∞ be a Hamiltonian homeomorphism and (Hn)n∈N a sequence of smooth functions
that satisﬁes the condition in Deﬁnition 5.18. For any n ∈ N, we set ϕn := φ
Hn
1 and
consider the sheaf quantization K ϕn of ϕn. Then, the sequence (Kϕn )n∈N forms a Cauchy
sequence with respect to dD(M 2) and gives an object Kϕ∞. In this situation, we deﬁne the
set of spectral invariants Spec(ϕ∞, L) by

Spec(ϕ∞, L) := Spec(K ϕ∞ • FL). (6.25)

This is well-deﬁned up to shift.

Lemma 6.6. One has
 Spec(ϕ∞, L) = lim
n→∞ Spec(ϕn, L). (6.26)

Proof. Since dD(M 2)(Kϕn, Kϕ∞ ) → 0 (n → ∞), we have dD(M )(Kϕn • FL, Kϕ∞ • FL) →
0 (n → ∞). Hence, we get the result.

The spectral norm for Lagrangian submanifolds is deﬁned as follows.

Deﬁnition 6.7. Let ϕ : T ∗M → T ∗M be a Hamiltonian diﬀeomorphism. One deﬁnes

γ(ϕ(0M )) := max Spec(Kϕ • kM ×[0,∞)) + max Spec(Kϕ−1 • kM ×[0,∞)) (6.27)

and calls it the spectral norm of ϕ(0M ).

Note that the spectral norm γ(ϕ(0M )) depends only on the image ϕ(0M ). This follows
from Proposition 6.9 below and the fact that if ϕ, ϕ′ ∈ Hamc(T ∗M, ω) satisfy ϕ(0M ) =
ϕ′(0M ) then Kϕ • kM ×[0,∞) ≃ Tc(Kϕ′ • kM ×[0,∞)) for some constant c ∈ R. We also remark
that γ(ϕ(0M )) in Deﬁnition 6.7 is the same as that in [Vit92; Oh97; Oh99] by the above
argument.
We describe this spectral norm in terms of the distance on the Tamarkin category. For
that purpose, we introduce an interleaving distance up to shift.

Deﬁnition 6.8. For F, G ∈ D(M ), one deﬁnes

dD(M )(F, G) := inf
c∈R dD(M )(F, TcG). (6.28)

29

Proposition 6.9. For a Hamiltonian diﬀeomorphism ϕ : T ∗M → T ∗M , one has

γ(ϕ(0M )) = dD(M )(kM ×[0,∞), Kϕ • kM ×[0,∞)). (6.29)

Proof. We will argue similarly to the proof of Theorem 5.1. Again let Tor be the full
triangulated subcategory of D(M ) consisting of torsion objects {F | dD(M )(F, 0) < ∞}.
Then, the Hom set of the localized category D(M )/ Tor is computed as

HomD(M )/ Tor(F, G) ≃ lim
−→
c→∞ HomD(M )(F, TcG). (6.30)

Hence, Q∗
∞(F ) is isomorphic to ⊕
n HomD(M )/ Tor(kM ×[0,∞), F [n]).
For an object F ∈ D(M ) with d(kM ×[0,∞), F ) < ∞, F and kM ×[0,∞) are isomorphic
in D(M )/ Tor. On the other hand, any isomorphism ¯α ∈ HomD(M )/ Tor(kM ×[0,∞), F ) ≃
Q0
∞(F ) gives an isomorphism Q∗
∞(F ) ≃ ⊕n HomD(M )/ Tor(kM ×[0,∞), kM ×[0,∞)[n]) ≃ H ∗(M )
of right H ∗(M )-modules that sends ¯α ∈ Q0
∞(F ) to 1 ∈ H 0(M ) ≃ k. Note that

Q0
∞,c(F ) ≃
 {
k (c > c(¯α, F ))
0 (c < c(¯α, F )) (6.31)

by deﬁnition. Since Q∗
∞,c(F ) ⊂ Q∗
∞(F ) is an H ∗(M )-submodule for any c, Q0
∞,c(F ) ̸= 0
if and only if Q∗
∞,c(F ) = Q∗
∞(F ). Hence we obtain

max Spec(F ) = c(¯α, F ). (6.32)

(i) Let a, b ∈ R and
 α : kM ×[0,∞) → TaKϕ • kM ×[0,∞), (6.33)

β : Kϕ • kM ×[0,∞) → TbkM ×[0,∞) (6.34)

such that α descends to an isomorphism ¯α ∈ HomD(M )/ Tor(kM ×[0,∞), Kϕ • kM ×[0,∞)) and
β descends to its inverse ¯β. Since ¯α ∈ Q0
∞,a(Kϕ •kM ×[0,∞)) is non-zero, a ≥ max Spec(Kϕ •
kM ×[0,∞)). On the other hand, β gives a non-zero element of Q0
∞,b(Kϕ−1 • kM ×[0,∞)) since

Kϕ−1 • (∗) is the inverse functor of Kϕ • (∗). Hence, we obtain b ≥ max Spec(Kϕ−1 •
kM ×[0,∞)). This shows γ(ϕ(0M )) ≤ dD(M )(kM ×[0,∞), Kϕ • kM ×[0,∞)).
(ii) For any a > max Spec(Kϕ • kM ×[0,∞)), there exists α : kM ×[0,∞) → TaKϕ • kM ×[0,∞)
that descends to an isomorphism ¯α ∈ HomD(M )/ Tor(kM ×[0,∞), Kϕ • kM ×[0,∞)). For any
b > max Spec(Kϕ−1 • kM ×[0,∞)), there also exists β : Kϕ • kM ×[0,∞) → TbkM ×[0,∞) that
descends to an isomorphism β. Since HomD(M )/ Tor(kM ×[0,∞), kM ×[0,∞)) ≃ k, we may
assume that ¯β is the inverse of ¯α after multiplying a non-zero element of k to β. The
composite ¯β ◦ ¯α = idkM ×[0,∞) can be regarded as a non-zero element of Q0
∞,a+b(kM ×[0,∞)).
Noting that
 Q0
c(kM ×[0,∞)) ≃ Q0
∞,c(kM ×[0,∞)) ≃
 {
k (c ≥ 0)
0 (c < 0), (6.35)

we obtain a + b ≥ 0 and the preimage Taβ ◦ α ∈ Q0
a+b(kM ×[0,∞)) of idkM ×[0,∞) = ¯β ◦ ¯α is
τa+b(kM ×[0,∞)). Similarly, we obtain Tbα ◦ β = τa+b(Kϕ • kM ×[0,∞)) using

HomD(M )(Kϕ • kM ×[0,∞), TcKϕ • kM ×[0,∞)) ≃ Q0
c(kM ×[0,∞)) (6.36)

and (6.35). This proves γ(ϕ(0M )) ≥ dD(M )(kM ×[0,∞), Kϕ • kM ×[0,∞)).

30

Remark 6.10. One can deﬁne Hamiltonian spectral invariants in a sheaf-theoretic way
as follows. Let H : T ∗M × I → R be a timewise compactly supported function and
K H ∈ D(kM 2×Rt×I ) the associated sheaf quantization. Then, we deﬁne

Spec(H) := Spec(Pl(Hom⋆(k∆M ×[0,∞), K H
1 ))). (6.37)

The Hamiltonian spectral norm is also deﬁned by

γ(H) := max Spec(H) + max Spec(H) (6.38)

and we obtain
 γ(H) = dD(M 2)(k∆M ×[0,∞), KH
1 ). (6.39)

We conjecture that γ(H) coincides with the Hamiltonian spectral norm of H deﬁned by
Frauenfelder–Schlenk [FS07] for a compact manifold M .

7 Arnold-type principle for Hamiltonian homeomorphisms

In this section, we use the previous results to prove an Arnold-type theorem for a Hamilto-
nian homeomorphism of a cotangent bundle in a purely sheaf-theoretic way. Throughout
this section, we assume that M is compact.
Let L be a compact exact Lagrangian submanifold of T ∗M and FL be the canonical
simple sheaf quantization of L. Let ϕ∞ be a Hamiltonian homeomorphism and K ϕ∞ be
the sheaf quantization of ϕ∞. We set F∞ := Kϕ∞ • FL. Then, by (5.29) we have

SS(F∞) ∩ {τ > 0} ⊂ {(x, t; ξ, τ ) | τ > 0, (x; ξ/τ ) ∈ ϕ∞(L)}. (7.1)

Moreover, by construction and the property of FL, we get Q∗
∞(F∞) ≃ H ∗(M ; k).
Combining the previous results, we obtain the following result by a purely sheaf-
theoretic method. In the case L is the zero-section 0M , it was proved by [BHS22] in
a more general setting (see below). We set cl(M ) := cl(H ∗(M ; k)), which is called the
cup-length of M over k.

Theorem 7.1. Let L be a compact exact Lagrangian submanifold of T ∗M and ϕ∞ be a
Hamiltonian homeomorphism of T ∗M . If # Spec(ϕ∞, L) ≤ cl(M ), then 0M ∩ ϕ∞(L) is
cohomologically non-trivial in M , in particular it is inﬁnite.

Proof. Let t : M × Rt → Rt and πM : T ∗(M × Rt) → M be the projections. Let Γdt denote
the graph of the 1-form dt. Then, by (7.1), we have πM (SS(F∞) ∩ Γdt) ⊂ 0M ∩ ϕ∞(0M ).
Thus we obtain the result by applying Theorem 6.5 and Lemma 6.6 to F∞.

By using the spectral norm γ and its C 0-continuity, we can construct a sheaf quanti-
zation the image of the zero-section 0M under a C 0-limit of Hamiltonian diﬀeomorphisms.
With the sheaf quantization, we can also recover [BHS22, Thm. 1.1]. Note that the proof
is not purely sheaf-theoretic.

Proposition 7.2. Let ϕ∞ : T ∗M → T ∗M be a compactly supported homeomorphism.
Assume that there exist a compact subset C ⊂ T ∗M and a sequence of Hamiltonian diﬀeo-
morphisms (ϕn)n∈N ⊂ Hamc(T ∗M, ω) supported in C that C 0-converges to ϕ∞ for some
Riemannian metric.
 31

(i) There exists an object F∞ ∈ D(M ) such that dD(M )(kM ×[0,∞), F∞) < ∞ and

SS(F∞) ∩ {τ > 0} ⊂ {(x, t; ξ, t) | τ > 0, (x; ξ/τ ) ∈ ϕ∞(0M )}. (7.2)

(ii) There exists a sequence of real numbers (cn)n∈N ⊂ R such that Spec(ϕ∞, 0M ) :=
limn→∞ T−cn Spec(ϕn, 0M ) is well-deﬁned up to shift. Moreover, if # Spec(ϕ∞, 0M ) ≤
cl(M ), then 0M ∩ ϕ∞(0M ) is cohomologically non-trivial in M , in particular it is
inﬁnite.

Proof. (i) Our γ(ψ(0M )) coincides with γ(ψ(0M )) in [BHS22] for any compactly supported
Hamiltonian diﬀeomorphism ψ. By [BHS22, Thm. 4.1], for any ε > 0, there exists δ > 0
such that dC0(ψ, idT ∗M ) < δ implies γ(ψ(0M )) < ε. By the C 0-convergence of (ϕn)n∈N,
for any δ > 0, there exists N ∈ N such that if n, m ≥ N , then dC0(ϕ−1
n ϕm, idT ∗M ) < δ.
Hence, for any ε > 0, there exists N ∈ N such that if n, m ≥ N , then γ(ϕ−1
n ϕm(0M )) < ε.
We deﬁne Fn := Kϕn • kM ×[0,∞) ∈ D(M ). By Proposition 6.9,

γ(ϕ
−1
n ϕm(0M )) = dD(M )(kM ×[0,∞), Kϕ−1
n • Kϕm • kM ×[0,∞)) = dD(M )(Fn, Fm). (7.3)

Hence, the sequence (Fn)n∈N is a Cauchy sequence with respect to dD(M ). This implies
that there exists a sequence (cn)n∈N of real numbers such that (TcnFn)n∈N is Cauchy with
respect to dD(M ). Thus, there exists a limit object F∞ of (TcnFn)n∈N by Corollary 4.5. By
construction, we obtain dD(M )(kM ×[0,∞), F∞) < ∞ and the desired microsupport estimate.
(ii) By construction, we ﬁnd that

Spec(F∞) = lim
n→∞ Spec(TcnFn) = lim
n→∞ T−cn Spec(ϕn, 0M ). (7.4)

Thus, applying Theorem 6.5 to F∞, we obtain the result.

Note that the number of Spec(ϕ∞, 0M ) is the same as that of [BHS22].

8 Arnold-type principle for Hausdorﬀ limits of Legendrians

In this section, we brieﬂy discuss how to prove a Legendrian analogue of Theorem 7.1 (cf.
[BHS22, Thm. 1.5]) by a sheaf-theoretic method. Again, we assume that M is compact.
Denote by J 1M = T ∗M × R the 1-jet bundle. For a compact Legendrian submanifold
L of J 1M , we deﬁne a conic Lagrangian submanifold c(L) of T ∗(M × Rt) by

c(L) := {(x, t; ξ, τ ) | τ > 0, (x, ξ/τ, t) ∈ L}. (8.1)

Let L be a Legendrian submanifold without Reeb chords. Then by the results in [Gui23,
Part XII], we can construct FL ∈ D(kM ×Rt) such that ˚SS(FL) = c(L).
Consider a sequence (Ln)n∈N of compact Legendrian submanifolds without Reeb chords
of J 1M . Assume that (Ln)n∈N converges to a compact subset L∞ of J 1M with respect to
the Hausdorﬀ distance. For each Ln, we can construct Fn := FLn ∈ D(kM ×Rt) as above.
Following [Gui13] (see also [Gui23, Part VII]), we deﬁne F∞ ∈ D(kM ×Rt) by the exact
triangle ⊕

n∈N Fn −→ ∏

n∈N Fn −→ F∞ +1
−−→ . (8.2)

32

Then we ﬁnd F∞ ∈ D(M ) and get Q∗
∞(F∞) ≃ C⊗H ∗(M ; k), where C := Coker(
⊕
n∈N k →∏n∈N k). Applying Lemma 2.5 and arguing as in the proof of Lemma 2.9, we have

˚SS(F∞) ⊂ c(L∞) = lim
n→∞ c(Ln) ⊂ T ∗(M × Rt). (8.3)

Let t : M × Rt → Rt and qR : J 1M = T ∗M × Rt → Rt be the projections. Then we ﬁnd
that
 SS(F∞) ∩ Γdt ⊂ {(x, t; 0, 1) | (x, 0, t) ∈ L∞} = (L∞ ∩ (0M × Rt)) × {1} (8.4)

and hence
 − Spec(F∞) ⊂ tπ(SS(F∞) ∩ Γdt) ⊂ qR(L∞ ∩ (0M × Rt)). (8.5)

Proposition 8.1. In the situation as above, if Spec(F∞) ≤ cl(M ), then L∞ ∩ (0M × Rt)
is cohomologically non-trivial in M × Rt. In particular, if #qR(L∞ ∩ (0M × Rt)) ≤ cl(M ),
then L∞ ∩ (0M × Rt) is cohomologically non-trivial in M × Rt, hence it is inﬁnite.

Proof. By applying Theorem 6.5 to the object F∞ ∈ D(M ), we obtain the result by (8.3)
and Q∗
∞(F∞) ≃ C ⊗ H ∗(M ; k).

A Hamiltonian stability with support conditions

In this appendix, we prove an estimate by the oscillation norm ∥H∥osc,A of H restricted
to a non-empty closed subset A, in the context of the sheaf-theoretic energy estimate.

A.1 Sheaf quantization of 2-parameter Hamiltonian isotopies

We will use the sheaf quantization of a 2-parameter Hamiltonian isotopy. For that pur-
pose, we ﬁrst state the main result of [GKS12] in a general form. Let N be a connected
non-empty manifold and W a contractible open subset of Rn with the coordinate sys-
tem (w1, . . . , wn) containing 0. Let us consider ψ = (ψw)w∈W : ˚T ∗N × W → ˚T ∗N be a
homogeneous Hamiltonian isotopy, that is, a C ∞-map satisfying (1) ψw is homogeneous
symplectic isomorphism for each w ∈ W and (2) ψ0 = id˚T ∗N . We can deﬁne a vector-
valued homogeneous function h : ˚T ∗N × W → Rn by h = (h1, . . . , hn) with

∂ψw
∂wi ◦ ψ−1
w = Xhi(•,w), (A.1)

where Xhi(•,w) is the Hamiltonian vector ﬁeld of the function hi(•, w) : ˚T ∗N → R. By
using the function h, we deﬁne a conic Lagrangian submanifold Λψ of ˚T ∗(N 2 × W ) by

Λψ := {
(ψw(y; η), (y; −η), (u; −h(ψw (y; η), w))) ∣
∣
∣ (y; η) ∈ ˚T ∗N, w ∈ W } (A.2)

The main theorem of [GKS12] is the following.

Theorem A.1 ([GKS12, Thm. 3.7 and Rem. 3.9]). Let ψ : ˚T ∗N × W → ˚T ∗N be a ho-
mogeneous Hamiltonian isotopy and set Λψ as above. Then there exists a unique simple
object ̃K ∈ D(kN 2×W ) such that ˚SS( ̃K) = Λψ and ̃K|N 2×{0} ≃ k∆N .

33

For a non-homogeneous compactly supported Hamiltonian isotopy, we can associate a
sheaf by homogenizing the isotopy. In the 1-parameter case, it is done as in Deﬁnition 3.10.
Below we will explain how to homogenize a 2-parameter Hamiltonian isotopy.
Let (Gs′,s)(s′,s)∈I 2 be a 2-parameter family of compactly supported smooth functions
on T ∗M . A 2-parameter family of diﬀeomorphisms (φs′,s)(s′,s)∈I 2 is determined by φs′,0 =

idT ∗M and ∂φs′,s
∂s ◦φ
−1
s′,s = XGs′,s, where XGs′,s is the Hamiltonian vector ﬁeld corresponding

to the function Gs′,s. We set ̂Gs′,s(x, t; ξ, τ ) := τ Gs′,s(x; ξ/τ ) and deﬁne a 2-parameter
homogeneous Hamiltonian isotopy ̂φ = (̂φs′,s)s′,s by




 ̂φs′,0 = id˚T ∗(M ×Rt),

∂ ̂φs′,s
∂s ◦ ̂φ
−1
s′,s = X ̂Gs′,s. (A.3)

Then, we have

Λ ̂φ = {( ̂φs′,s(y; η), (y; −η), (s′; − ̂Fs′,s(̂φs′,s(y; η))), (s; − ̂Gs′ ,s(̂φs′,s(y; η)))
) ∣
∣
∣

(y; η) ∈ ˚T ∗(M × R), s′, s ∈ I} , (A.4)

where the 2-parameter family of homogeneous functions ( ̂Fs′,s)s′,s is determined by ∂ ̂φs′,s
∂s′ ◦
̂φ
−1
s′,s = X ̂Fs′,s. By the construction of ̂φ, there exists a 2-parameter family of timewise

compactly supported functions (Fs′,s)(s′,s)∈I 2 satisfying ̂Fs′,s(x, t; ξ, τ ) = τ Fs′,s(x; ξ/τ ) and
∂φs′,s
∂s′ ◦ φ
−1
s′,s = XFs′,s. A calculation in [Pol12] or [Oh05] (see also [Ban78]) shows that

∂Fs′,s
∂s = ∂Gs′,s
∂s′ − {Fs′,s, Gs′,s}, (A.5)

where {−, −} is the Poisson bracket. In this case, we can apply Theorem A.1 to the
homogeneous Hamiltonian isotopy ̂φ and obtain a simple object ̃K satisfying ˚SS( ̃K) = Λ ̂φ.
By using the map q : (M × R)2 × I 2 → M 2 × Rt × I 2, (x1, t1, x2, t2, s′, s) ↦→ (x1, x2, t1 −
t2, s′, s), we also obtain an equivalence similar to (3.26). Hence, we can deﬁne K ∈
D(kM 2×R×I 2) by the condition ˚SS(K) = qdq−1
π (Λ ̂φ) and K := Pl(K) ∈ D(M 2 × I 2), which
we call the sheaf quantization of (φs′,s)(s′,s)∈I 2.

A.2 Statement and proof

For a closed subset A of T ∗M , we deﬁne a full subcategory DA(M ) of D(M ) by

DA(M ) := {F ∈ D(M ) | SS(F ) ∩ {τ > 0} ⊂ ρ−1
t (A)}, (A.6)

where ρt : T ∗M × T ∗
τ >0Rt → T ∗M, (x, t; ξ, τ ) ↦→ (x; ξ/τ ).
Let KH ∈ D(M 2 × I) be the sheaf quantization associated with a timewise compactly
supported function H : T ∗M × I → R and F ∈ DA(M ) with A being a closed subset of
T ∗M . Then we get KH • F ∈ D(M × I) and ﬁnd that

KH
s • F ≃ (KH • F )|M ×{s}×Rt ∈ DφH
s (A)(M ) for any s ∈ I. (A.7)

We shall estimate the distance between F ∈ DA(M ) and KH
1 • F ∈ DφH
1 (A)(M ) up to
translation. See also Remark A.4 for a more straightforward but weaker case.

34

Theorem A.2. Let A be a non-empty closed subset of T ∗M and F ∈ DA(M ). Moreover,
let H : T ∗M × I → R be a timewise compactly supported function. Then for a continuous
function f : I → R, one has

dD(M )(F, T−cKH
1 • F )

≤ ∫ 1

0
 (max { max
p∈φH
s (A) Hs(p), f (s)
} − min { min
p∈φH
s (A) Hs(p), f (s)
}) ds (A.8)

where c = ∫ 1
0 f (s)ds.

Remark A.3. If we take f ≡ 0, we obtain

dD(M )(F, KH
1 • F )

≤ ∫ 1

0
 (max { max
p∈φH
s (A) Hs(p), 0
} − min { min
p∈φH
s (A) Hs(p), 0
}) ds. (A.9)

Let c ∈ R be a real number satisfying
∫ 1

0 min
p∈φH
s (A) Hs(p)ds ≤ c ≤ ∫ 1

0 max
p∈φH
s (A) Hs(p)ds. (A.10)

Then we can take f such that c = ∫ 1
0 f (s)ds and

min
p∈φH
s (A) Hs(p) ≤ f (s) ≤ max
p∈φH
s (A) Hs(p) (A.11)

for any s ∈ I. Hence, by Theorem A.2, we get

dD(M )(F, T−cKH
1 • F ) ≤ ∫ 1

0
 ( max
p∈φH
s (A) Hs(p) − min
p∈φH
s (A) Hs(p)
) ds. (A.12)

For simplicity, we introduce a symbol for the right-hand side of (A.8). For a function
H : T ∗M × I → R, a function f : I → R, and a non-empty closed subset A of T ∗M , we set

B(H, f, A) := ∫ 1

0
 (max { max
p∈φH
s (A) Hs(p), f (s)
} − min { min
p∈φH
s (A) Hs(p), f (s)
}) ds. (A.13)

Proof of Theorem A.2. Let ε > 0. We can take a smooth family (ρa,b : R → R)a,b of
smooth functions parametrized by a, b ∈ R with a ≤ b such that

(1) ρa,b(y) = y on a neighborhood of [a, b],

(2) a − ε ≤ infy ρa,b(y) < supy ρa,b(y) ≤ b + ε.

Recall that I denotes an open interval containing the closed interval [0, 1]. We take smooth
functions M, m : I → R satisfying

max
p∈φH
s (A) Hs(p) + ε
2 ≤ M (s) ≤ max
p∈φH
s (A) Hs(p) + ε (A.14)

and
 min
p∈φH
s (A) Hs(p) − ε ≤ m(s) ≤ min
p∈φH
s (A) Hs(p) − ε
2 . (A.15)

35

Fix R > 0 suﬃciently large so that R > maxp,s Hs(p)−minp,s Hs(p)+2ε. Deﬁne a(s′, s) :=
m(s) − Rs′, b(s′, s) := M (s) + Rs′ for (s′, s) ∈ I 2. We may assume that I ⊂ (− ε
2R , +∞)
by taking I smaller if necessary, and hence that

a(s′, s) ≤ min
p∈φH
s (A) Hs(p) ≤ max
p∈φH
s (A) Hs(p) ≤ b(s′, s) (A.16)

for all (s′, s) ∈ I 2. Take a smooth function ˜f : I → R such that ∥ ˜f − f ∥C0 ≤ ε. By
shrinking I, we may assume that ⋃s supp(Hs) is relatively compact. Then we can also
take a compactly supported smooth cut-oﬀ function χ : T ∗M → [0, 1] such that χ ≡ 1
on a neighborhood of ⋃s supp(Hs). Using these functions, we deﬁne a function G =
(Gs′,s)s′,s∈I 2 : T ∗M × I 2 → R by

Gs′,s := (
ρa(s′,s),b(s′,s) ◦ Hs − (1 − s′) ˜f (s)
) χ. (A.17)

A 2-parameter family (φs′,s)(s′,s)∈I 2 of Hamiltonian diﬀeomorphisms is determined by

φs′,0 = idT ∗M and ∂φs′,s
∂s ◦ φ
−1
s′,s = XGs′,s, where XGs′,s is the Hamiltonian vector ﬁeld
corresponding to the function Gs′,s. Note that G1,s = Hs and φs′,s is independent of s′ on
a neighborhood U of A. Moreover, we have
∫ 1

0
 ( max
p∈T ∗M G0,s(p) − min
p∈T ∗M G0,s(p)
) ds

≤ ∫ 1

0
 ( max
p∈T ∗M
 (
ρm(s),M (s) ◦ Hs(p) − ˜f (s)
) χ(p) − min
p∈T ∗M
 (
ρm(s),M (s) ◦ Hs(p) − ˜f (s)
) χ(p)
) ds

≤ ∫ 1

0
 (max { max
p∈φH
s (A)
 (
Hs(p) − ˜f (s)
) , 0
} − min { min
p∈φH
s (A)
 (
Hs(p) − ˜f (s)
) , 0
}) ds + 2ε

= ∫ 1

0
 (max { max
p∈φH
s (A) Hs(p), ˜f (s)
} − min { min
p∈φH
s (A) Hs(p), ˜f (s)
}) ds + 2ε

≤ B(H, f, A) + 4ε. (A.18)

For s′ ∈ I, we set Gs′ := Gs′,• : T ∗M × I → R. Then, by Theorem 5.1 and the natural
inequality for the distance with respect to functorial operations (see (3.11)), we obtain

dD(M )(F, KG0
1 • F ) = dD(M )(K0
1 • F, KG0
1 • F ) ≤ B(H, f, A) + 4ε. (A.19)

We set ˜c(s) := ∫ s
0 ˜f (t)dt and claim that KG0
1 • F ≃ T−˜c(1)KG1
1 • F . By the result
recalled in appendix A.1, we can construct the sheaf quantization K ∈ D(M 2 × I 2) of the
2-parameter family of diﬀeomorphisms (φs′,s)s′,s. We shall use the same notation as in
appendix A.1. Then, Fs′,0 = 0 and F•,s|φ1,s(U )×I : φ1,s(U ) × I → R, (p, s′) ↦→ Fs′,s(p) is

locally constant for each s. By (A.5), we ﬁnd that ∂Fs′,s
∂s = ∂Gs′,s
∂s′ = ˜f (s) on ⋃s φ1,s(U ) ×
I × {s} and that Fs′,s = ∫ s
0 ˜f (t)dt = ˜c(s) there. We deﬁne H := K • F ∈ D(M × I 2). Then,
by the microsupport estimate, we have

SS(H) ⊂ {( ̂φs′,s(x, t; ξ, τ ), (s′; −τ ˜c(s)), (s; −τ Gs′,s(φs′,s(x; ξ/τ )))
) ∣
∣
∣

(x, t; ξ, τ ) ∈ ˚SS(F ), s′, s ∈ I} ∪ 0M ×R×I 2. (A.20)

Hence, M × R × I × {1} is non-characteristic for H and we get

SS(H|M ×R×I×{1}) ⊂ {( ̂φs′,1(x, t; ξ, τ ), (s′; −˜c(1)τ )
) ∣
∣
∣

(x, t; ξ, τ ) ∈ ˚SS(F ), s′ ∈ I} ∪ 0M ×R×I . (A.21)

36

Deﬁne a diﬀeomorphism ϕ : M × R × I ∼
−→ M × R × I, (x, t, s′) ↦→ (x, t − ˜c(1)s′, s′). Then we
have SS(ϕ∗H|M ×R×I×{1}) ⊂ T ∗(M ×R)×0I , which shows ϕ∗H|M ×R×I×{1} is the pull-back
of a sheaf on M × R by [KS90, Prop. 5.4.5]. In particular,

KG0
1 • F = H|M ×R×{0}×{1}
≃ (ϕ∗H|M ×R×I×{1})|{s′=0}
≃ (ϕ∗H|M ×R×I×{1})|{s′=1}
≃ T−˜c(1)H|M ×R×{1}×{1} = T−˜c(1)KG1
1 • F.
 (A.22)

Since |c − ˜c(1)| ≤ ε, we have dD(M )(T−cKH
1 • F, T−˜c(1)KH
1 • F ) ≤ ε. Combining the
result above and noticing G1 = H, we obtain

dD(M )(F, T−cKH
1 • F ) ≤ dD(M )(F, T−˜c(1)KH
1 • F ) + ε

= dD(M )(F, KG0
1 • F ) + ε

≤ B(H, f, A) + 5ε.
 (A.23)

Since ε > 0 is arbitrary, this completes the proof.

Remark A.4. Under the same assumption as in Theorem A.2, we can prove the weaker
result
 dw-isom(F, T−cKH
1 • F ) ≤ B(H, f, A) (A.24)

more straightforwardly, without the 2-parameter family, as follows. Here dw-isom denotes
the pseudo-distance on D(M ) deﬁned by

dw-isom(F, G) := inf {a + b | (F, G) is weakly (a, b)-isomorphic} . (A.25)

We set H := KH • F ∈ D(M × I). Then we have H|M ×Rt×{0} ≃ F and H|M ×Rt×{1} ≃
KH
1 • F . Moreover, by the microsupport estimate, we ﬁnd that

SS(H) ⊂ T ∗M × {(t, s; τ, σ) ∣
∣
∣
∣ − max
p∈φH
s (A) Hs(p) · τ ≤ σ ≤ − min
p∈φH
s (A) Hs(p) · τ } . (A.26)

Let ε > 0 and take a smooth function ˜f : I → R such that ∥ ˜f − f ∥C0 ≤ ε. We deﬁne a
function ˜c : I → R by ˜c(s) := ∫ s
0 ˜f (s′)ds′ and a function ϕ : M × Rt × I → M × Rt × I
by ϕ(x, t, s) := (x, t − ˜c(s), s). Then we have ϕ∗H|M ×Rt×{0} ≃ F , ϕ∗H|M ×Rt×{1} ≃
T−˜c(1)KH
1 • F , and

SS(ϕ∗H)

⊂ T ∗M × {
(t, s; τ, σ) ∣
∣
∣
∣ − ( max
p∈φH
s (A) Hs(p) − ˜f (s)
) · τ ≤ σ

≤ − ( min
p∈φH
s (A) Hs(p) − ˜f (s)
) · τ } .
 (A.27)

Note that we may have maxp∈φH
s (A) Hs(p) − ˜f (s) < 0 and minp∈φH
s (A) Hs(p) − ˜f (s) > 0 in

37

general. By applying Proposition 3.9, we obtain

dw-isom(F, T−˜c(1)KH
1 • F )

= dw-isom(ϕ∗H|M ×Rt×{0}, ϕ∗H|M ×Rt×{1})

≤ ∫ 1

0
 (max { max
p∈φH
s (A)
 (
Hs(p) − ˜f (s)
) , 0
} − min { min
p∈φH
s (A)
 (Hs(p) − ˜f (s)
) , 0
}) ds

= ∫ 1

0
 (max { max
p∈φH
s (A) Hs(p), ˜f (s)
} − min { min
p∈φH
s (A) Hs(p), ˜f (s)
}) ds

≤ ∫ 1

0
 (max { max
p∈φH
s (A) Hs(p), f (s)
} − min { min
p∈φH
s (A) Hs(p), f (s)
}) ds + 2ε.
 (A.28)

Hence, we have

dw-isom(F, T−cKH
1 • F ) ≤ dw-isom(F, T−˜c(1)KH
1 • F ) + ε

≤ ∫ 1

0
 (max { max
p∈φH
s (A) Hs(p), f (s)
} − min { min
p∈φH
s (A) Hs(p), f (s)
}) ds + 3ε, (A.29)

which completes the proof.

For a timewise compactly supported function H : T ∗M × I → R and a non-empty
closed subset A of T ∗M , we set

∥H∥osc,A := ∫ 1

0
 (max
p∈A Hs(p) − min
p∈A Hs(p)
) ds. (A.30)

Proposition A.5. Let A be a non-empty closed subset of T ∗M and F ∈ DA(M ). More-
over, let H : T ∗M × I → R be a timewise compactly supported function. Then there exists
c ∈ R such that
 dD(M )(F, T−cKH
1 • F ) ≤ ∥H∥osc,A. (A.31)

Proof. Using the technique in the proof of [Ush15, Theorem 1.3], one can construct a
function H ′ such that φH
1 = φH ′
1 and
∫ 1

0
 (max
p∈A Hs(p) − min
p∈A Hs(p)
) ds

= ∫ 1

0
 (
 max
p∈φH′
s (A) H ′
s(p) − min
p∈φH′
s (A) H ′
s(p)

)
 ds. (A.32)

By Proposition 5.9, φH
1 = φH ′
1 implies KH
1 ≃ KH ′
1 . Hence, the result follows from Theo-
rem A.2 (see also Remark A.3).

References

[AI20] T. Asano and Y. Ike. “Persistence-like distance on Tamarkin’s category and
symplectic displacement energy”. The Journal of Symplectic Geometry 18.3
(2020), pp. 613–649.

[AI23] T. Asano and Y. Ike. “Sheaf quantization and intersection of rational La-
grangian immersions”. Annales de l’Institut Fourier 73.4 (2023), pp. 1533–
1587.
 38

[Ban78] A. Banyaga. “Sur la structure du groupe des diﬀ´eomorphismes qui pr´eservent
une forme symplectique”. Commentarii Mathematici Helvetici 53.1 (1978),
pp. 174–227.

[BG21] N. Berkouk and G. Ginot. “A derived isometry theorem for sheaves”. Advances
in Mathematics (2021), p. 108033.

[BGO19] N. Berkouk, G. Ginot, and S. Oudot. Level-sets persistence and sheaf theory.
2019. arXiv: 1907.09759 [math.AT].

[BP21] N. Berkouk and F. Petit. “Ephemeral persistence modules and distance com-
parison”. Algebraic & Geometric Topology 21.1 (2021), pp. 247–277.

[BCZ21] P. Biran, O. Cornea, and J. Zhang. Triangulation and persistence: Algebra 101.
2021. arXiv: 2104.12258 [math.AT].

[BN93] M. B¨okstedt and A. Neeman. “Homotopy limits in triangulated categories”.
Compositio Mathematica 86.2 (1993), pp. 209–234.

[BHS18] L. Buhovsky, V. Humili`ere, and S. Seyfaddini. “A C 0 counterexample to the
Arnold conjecture”. Inventiones mathematicae 213.2 (2018), pp. 759–809.

[BHS21] L. Buhovsky, V. Humili`ere, and S. Seyfaddini. “The action spectrum and C 0

symplectic topology”. Mathematische Annalen 380.1 (2021), pp. 293–316.

[BHS22] L. Buhovsky, V. Humili`ere, and S. Seyfaddini. “An Arnold-type principle for
non-smooth objects”. Journal of Fixed Point Theory and Applications 24.2
(2022).

[Chi23] S.-F. Chiu. “Quantum speed limit and categorical energy relative to microlocal
projector”. Journal of Topology and Analysis (2023).

[Cru19] J. Cruz. Metric Limits in Categories with a Flow. 2019. arXiv: 1901.04828 [math.CT].

[FS07] U. Frauenfelder and F. Schlenk. “Hamiltonian dynamics on convex symplectic
manifolds”. Israel Journal of Mathematics 159 (2007), pp. 1–56.

[Fuk21] K. Fukaya. Gromov-Hausdorﬀ distance between ﬁltered A∞ categories 1: La-
grangian Floer theory. 2021. arXiv: 2106.06378 [math.SG].

[Gui12] S. Guillermou. Quantization of conic Lagrangian submanifolds of cotangent
bundles. 2012. arXiv: 1212.5818v2 [math.SG].

[Gui13] S. Guillermou. The Gromov-Eliashberg theorem by microlocal sheaf theory. 2013.
arXiv: 1311.0187 [math.SG].

[Gui23] S. Guillermou. “Sheaves and symplectic geometry of cotangent bundles”. Ast´erisque
440 (2023).

[GKS12] S. Guillermou, M. Kashiwara, and P. Schapira. “Sheaf quantization of Hamil-
tonian isotopies and applications to nondisplaceability problems”. Duke Math-
ematical Journal 161.2 (2012), pp. 201–245.

[GS14] S. Guillermou and P. Schapira. “Microlocal theory of sheaves and Tamarkin’s
non displaceability theorem”. In: Homological mirror symmetry and tropical
geometry. Vol. 15. Lect. Notes Unione Mat. Ital. Springer, 2014, pp. 43–85.

[GV22] S. Guillermou and C. Viterbo. The singular support of sheaves is γ-coisotropic.
2022. arXiv: 2203.12977 [math.SG].

[HV] V. Humili`ere and N. Vichery. Cuplength estimates via microlocal theory of
sheaves. in preparation.
 39

[KS90] M. Kashiwara and P. Schapira. Sheaves on manifolds. Vol. 292. Grundlehren
der Mathematischen Wissenschaften. Springer-Verlag, Berlin, 1990, pp. x+512.

[KS06] M. Kashiwara and P. Schapira. Categories and sheaves. Vol. 332. Grundlehren
der Mathematischen Wissenschaften. Springer-Verlag, Berlin, 2006, pp. x+497.

[KS18] M. Kashiwara and P. Schapira. “Persistent homology and microlocal sheaf the-
ory”. Journal of Applied and Computational Topology 2.1-2 (2018), pp. 83–
113.

[KS21] M. Kashiwara and P. Schapira. “Piecewise linear sheaves”. International Math-
ematics Research Notices 2021.15 (2021), pp. 11565–11584.

[Kaw22] Y. Kawamoto. “On C 0-continuity of the spectral norm for symplectically non-
aspherical manifolds”. International Mathematics Research Notices 2022.21
(2022), pp. 17187–17230.

[KS22] A. Kislev and E. Shelukhin. “Bounds on spectral norms and barcodes”. Geom-
etry & Topology 25.7 (2022), pp. 3257–3350.

[LSV21] F. Le Roux, S. Seyfaddini, and C. Viterbo. “Barcodes and area-preserving
homeomorphisms”. Geometry & Topology 25.6 (2021), pp. 2713–2825.

[Li21] W. Li. Estimating Reeb chords using microlocal sheaf theory. 2021. arXiv:
2106.04079 [math.SG].

[Nad09] D. Nadler. “Microlocal branes are constructible sheaves”. Selecta Mathematica.
New Series 15.4 (2009), pp. 563–619.

[NZ09] D. Nadler and E. Zaslow. “Constructible sheaves and the Fukaya category”.
Journal of the American Mathematical Society 22.1 (2009), pp. 233–286.

[Oh97] Y.-G. Oh. “Symplectic topology as the geometry of action functional. I. Relative
Floer theory on the cotangent bundle”. Journal of Diﬀerential Geometry 46.3
(1997), pp. 499–577.

[Oh99] Y.-G. Oh. “Symplectic topology as the geometry of action functional. II. Pants
product and cohomological invariants”. Communications in Analysis and Ge-
ometry 7.1 (1999), pp. 1–54.

[Oh05] Y.-G. Oh. “Normalization of the Hamiltonian and the action spectrum”. Jour-
nal of the Korean Mathematical Society 42 (2005), pp. 65–83.

[OM07] Y.-G. Oh and S. M¨uller. “The group of Hamiltonian homeomorphisms and
C 0-symplectic topology”. Journal of Symplectic Geometry 5.2 (2007), pp. 167–
219.

[PSW21] F. Petit, P. Schapira, and L. Waas. A property of the interleaving distance for
sheaves. 2021. arXiv: 2108.13018 [math.AG].

[PS23] F. Petit and P. Schapira. “Thickening of the diagonal and interleaving dis-
tance”. Selecta Mathematica. New Series 29.70 (2023).

[Pol12] L. Polterovich. The geometry of the group of symplectic diﬀeomorphism. Birkh¨auser,
2012.

[PS16] L. Polterovich and E. Shelukhin. “Autonomous Hamiltonian ﬂows, Hofer’s
geometry and persistence modules”. Selecta Mathematica. New Series 22.1
(2016), pp. 227–296.
 40

[RS18] M. Robalo and P. Schapira. “A lemma for microlocal sheaf theory in the ∞-
categorical setting”. Publications of the Research Institute for Mathematical
Sciences 54.2 (2018), pp. 379–391.

[Sco20] L. N. Scoccola. Locally persistent categories and metric properties of interleav-
ing distances. Ph.D thesis, The University of Western Ontario. 2020.

[Spa88] N. Spaltenstein. “Resolutions of unbounded complexes”. Compositio Mathe-
matica 65.2 (1988), pp. 121–154.

[Tam18] D. Tamarkin. “Microlocal Condition for Non-displaceability”. In: Algebraic and
Analytic Microlocal Analysis. Springer International Publishing, 2018, pp. 99–
223.

[Ush15] M. Usher. “Observations on the Hofer distance between closed subsets”. Math-
ematical Research Letters 22.6 (2015), pp. 1805–1820.

[UZ16] M. Usher and J. Zhang. “Persistent homology and Floer-Novikov theory”. Ge-
ometry & Topology 20.6 (2016), pp. 3333–3430.

[Vit92] C. Viterbo. “Symplectic topology as the geometry of generating functions”.
Mathematische Annalen 292.1 (1992), pp. 685–710.

[Vit06] C. Viterbo. “On the uniqueness of generating Hamiltonian for continuous lim-
its of Hamiltonians ﬂows”. International Mathematics Research Notices 2006
(2006), p. 34028.

[Vit19] C. Viterbo. Sheaf Quantization of Lagrangians and Floer cohomology. 2019.
arXiv: 1901.09440 [math.SG].

[Zha20] J. Zhang. Quantitative Tamarkin Theory. CRM Short Courses. Springer Inter-
national Publishing, 2020.

Tomohiro Asano: Research Institute for Mathematical Sciences, Kyoto University,
Kitashirakawa-Oiwake-Cho, Sakyo-ku, 606-8502, Kyoto, Japan.
E-mail address: tasano[at]kurims.kyoto-u.ac.jp, tomoh.asano[at]gmail.com

Yuichi Ike: Institute of Mathematics for Industry, Kyushu University, 744 Motooka Nishi-
ku, 819-0395, Fukuoka, Japan.
E-mail address: ike[at]imi.kyushu-u.ac.jp, yuichi.ike.1990[at]gmail.com

41
