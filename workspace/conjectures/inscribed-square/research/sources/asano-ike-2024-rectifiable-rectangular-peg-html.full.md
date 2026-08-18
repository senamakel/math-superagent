<!-- source: https://arxiv.org/html/2412.21057 | converted from HTML -->

The rectifiable rectangular peg problem

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2412.21057v3 [math.SG] 05 Jan 2026

# The rectifiable rectangular peg problem

Tomohiro Asano Yuichi Ike

August 11, 2026

###### Abstract

We give an affirmative answer to the rectangular peg problem for a large class of continuous Jordan curves that contains all rectifiable curves and Stromquist’s locally monotone curves. Our proof is based on microlocal sheaf theory and inspired by recent work of Greene and Lobb.

## 1 Introduction

The square peg problem first posed by Toeplitz [Toe11] in 1911 asks the following:

Does every continuous Jordan curve inscribe a square?

In this paper, we consider the so-called rectangular peg problem, which asks whether a Jordan curve inscribe a rectangle with prescribed aspect ratio. For θ ∈ ( 0, π) \theta\in(0,\pi), a θ \theta -rectangle is a rectangle such that the angle between the diagonals is θ \theta. Note that a θ \theta -rectangle is a ( π − θ) (\pi-\theta) -rectangle.

Recent progress have been made by Greene and Lobb in [GL21] where they answer positively to the question for smooth Jordan curves: every smooth Jordan curve inscribes a θ \theta -rectangle for any θ ∈ ( 0, π) \theta\in(0,\pi). More recently, in [GL24], they give a positive answer for rectangles and for every rectifiable (i.e., with finite length) Jordan curve satisfying some hypothesis on the diameter and the area of the bounded domain. In this paper we remove this later hypothesis. To the best of our knowledge, this is the first result that gives an affirmative answer to the square peg problem (i.e., θ = π / 2 \theta=\pi/2) for all the rectifiable Jordan curves.

### 1.1 Our results

Throughout this paper for a Jordan curve c: S 1 → ℝ 2 c\colon S^{1}\to\mathbb{R}^{2}, we write C = c ⁡ ( S 1) C=c(S^{1}) for its image in ℝ 2 \mathbb{R}^{2}. Our main theorem is the following.

###### Theorem 1.1.

Let c: S 1 → ℝ 2 c\colon S^{1}\to\mathbb{R}^{2} be a Jordan curve. Moreover, assume that there exists a sequence of smooth Jordan curves ( c n: S 1 → ℝ 2) n (c_{n}\colon S^{1}\to\mathbb{R}^{2})_{n} such that

- (1)

( c n) n (c_{n})_{n} converges to c c in the C 0 C^{0} -sense;

- (2)

setting f n f_{n} to be the primitive of ( c n ∘ e) ∗ ​ λ (c_{n}\circ e)^{*}\lambda, the sequence ( f n) n (f_{n})_{n} converges to a continuous function f f on ℝ \mathbb{R} uniformly on every compact subset, where e: ℝ → ℝ / 2 ​ π ​ ℤ ≃ S 1 e\colon\mathbb{R}\to\mathbb{R}/2\pi\mathbb{Z}\simeq S^{1} is the quotient map.

Then c c inscribes a θ \theta -rectangle for any θ ∈ ( 0, π) \theta\in(0,\pi).

A Jordan curve satisfying the conditions in theorem 1.1 might be said to *admit a continuous Legendrian lift*.

One can show that every rectifiable Jordan curve satisfies the conditions in theorem 1.1. See section 5. As a result, we get:

###### Corollary 1.2 ( corollary 5.9).

Every rectifiable Jordan curve inscribes a θ \theta -rectangle for any θ ∈ ( 0, π) \theta\in(0,\pi).

There is another large class called locally monotone (see definition 5.10 for the definition). We prove a locally monotone curve also satisfies the conditions in theorem 1.1, which implies the following:

###### Corollary 1.3 ( corollary 5.12).

Every locally monotone curve inscribes a θ \theta -rectangle for any θ ∈ ( 0, π) \theta\in(0,\pi).

We briefly explain our strategy for the proof of the theorem. Given a Jordan curve C C, by scaling, we may assume that the area of the open domain bounded by C C is π \pi.

The first ingredient is the trick to interpret inscribed θ \theta -rectangles into Lagrangian intersection, which has already appeared in [GL23, GL24, Gao24]. We identify ℝ 2 \mathbb{R}^{2} with ℂ \mathbb{C}, which we regard as a symplectic manifold. Note that if C C is smooth, it is a Lagrangian submanifold of ℂ \mathbb{C}, thus C × C C\times C is also a Lagrangian submanifold of ℂ × ℂ \mathbb{C}\times\mathbb{C}. For θ ∈ [0, π] \theta\in[0,\pi], define a Hamiltonian diffeomorphism R θ: ℂ 2 → ℂ 2 R_{\theta}\colon\mathbb{C}^{2}\to\mathbb{C}^{2} by

 | R θ = ( 1 1 − 1 1) − 1 ​ ( 1 0 0 e − − 1 ​ θ) ​ ( 1 1 − 1 1). R_{\theta}=\begin{pmatrix}1&1\\ -1&1\end{pmatrix}^{-1}\begin{pmatrix}1&0\\ 0&e^{-\sqrt{-1}\theta}\end{pmatrix}\begin{pmatrix}1&1\\ -1&1\end{pmatrix}. |  | (1.1) |

One can easily find that a θ \theta -rectangle corresponds to four distinct points z, w, z ′, w ′ z,w,z^{\prime},w^{\prime} such that R θ ​ ( z ′, w ′) = ( z, w) R_{\theta}(z^{\prime},w^{\prime})=(z,w). Since R θ ​ ( z, z) = ( z, z) R_{\theta}(z,z)=(z,z), R θ R_{\theta} is the identity on the diagonal Δ ℂ \Delta_{\mathbb{C}} of ℂ × ℂ \mathbb{C}\times\mathbb{C}, which corresponds to degenerate rectangles. Thus, the problem of finding a θ \theta -rectangle inscribed in C C is reduced to finding a intersection point between C × C C\times C and R θ ​ ( C × C) R_{\theta}(C\times C) outside the diagonal Δ C \Delta_{C} of C × C C\times C.

The second ingredient is the following method coming from microlocal sheaf theory, in particular, sheaf quantization. For a smooth Jordan curve C C, it is known that one can construct a canonical object F C F_{C} in the Tamarkin category whose microsupport is C × C C\times C, called the sheaf quantization of C × C C\times C. See sections 2 and 3 for more precise definitions. By the completeness of the Tamarkin category with respect to the interleaving distance [AI24, GV24], for a continuous Jordan curve C C, we can still construct its sheaf quantization F C F_{C}. Moreover, by a result in Guillermou–Kashiwara–Schapira [GKS12], the action R θ R_{\theta} lifts to the Tamarkin category category. The Hom space Hom ⁡ ( F C, R θ ​ F C) \operatorname{Hom}(F_{C},R_{\theta}F_{C}) captures the information of the intersection ( C × C) ∩ R θ ​ ( C × C) (C\times C)\cap R_{\theta}(C\times C) and is equipped with a filtration, which can be regarded as a persistence module with structure maps ( τ a, a ′) a ≤ a ′ (\tau_{a,a^{\prime}})_{a\leq a^{\prime}}. We focus on a “critical value” a 0 ∈ ℝ a_{0}\in\mathbb{R} such that τ a, a ′ \tau_{a,a^{\prime}} is not an isomorphism if a < a 0 < a ′ a<a_{0}<a^{\prime}. By the conditions in theorem 1.1, the diagonal Δ C \Delta_{C} contributes only to critical values in π ​ ℤ \pi\mathbb{Z}. We will show that there exists a critical value that is not in π ​ ℤ \pi\mathbb{Z}, which proves the theorem. In fact, we give a sheaf-theoretic condition for the existence of a θ \theta -rectangle in section 4. The conditions in theorem 1.1 implies that sheaf-theoretic condition.

With the sheaf-theoretical approach, we can directly deal with a continuous Jordan curve, in contrast to Floer-theoretic methods, which require taking a sequence of smooth objects. Moreover, the important step in our proof is to analyze μ ​ h ​ o ​ m ​ ( F C, R θ ​ F C) \mu hom(F_{C},R_{\theta}F_{C}), which is expected to correspond to local Floer cohomology. The computation method of μ ​ h ​ o ​ m \mu hom would be easier than that of local Floer cohomology. Furthermore, μ ​ h ​ o ​ m \mu hom does not commute with limits nor colimits, which suggests that μ ​ h ​ o ​ m ​ ( F C, R θ ​ F C) \mu hom(F_{C},R_{\theta}F_{C}) for a continuous Jordan curve C C cannot be described in terms of a limit/colimit. Thus, the sheaf-theoretic approach would be more powerful than Floer-theoretic methods at the moment.

This paper is organized as follows. In section 2, we define a twisted version of the Tamarkin category. In section 3, we construct a sheaf quantization of the standard torus and observe some basic properties. In section 4, we give a sheaf-theoretic condition for the existence of a θ \theta -rectangle. In section 5, we prove theorem 1.1 and show corollaries 1.2 and 1.3.

### 1.2 Related work

We review some history on the square and rectangular peg problem. See Matschke [Mat14] for a detailed and overall history on these topics.

Vaughan (published in [Mey81]) showed that every continuous Jordan curve inscribes a rectangle with a simple topological argument, in which a rectangle on the Jordan curve is interpreted to a immersed point of a surface in a 3 3 -dimensional space. Hugelmeyer [Hug18] proved that for any n ∈ ℤ ≥ 3 n\in\mathbb{Z}_{\geq 3}, every smooth Jordan curve has an inscribed rectangle of ratio π ​ k / n \pi k/n for some k ∈ { 1, …, n − 1 } k\in\{1,\dots,n-1\}. Moreover, he [Hug21] proved that for any smooth Jordan curve, the set of values θ ∈ [0, π / 2] \theta\in[0,\pi/2] for which the curve inscribe a rectangle of aspect angle θ \theta has Lebesgue measure at least π / 6 \pi/6. In his works, the existence of rectangular pegs is reduced to the existence of intersections of surfaces within a four-dimensional space. Greene and Lobb [GL21] solved the rectangular peg problem for smooth Jordan curves using symplectic geometry. Moreover, they proved cyclic quadrilateral pegs for smooth curves in [GL23]. In [GL24], Greene and Lobb used a version of Lagrangian intersection Floer theory and spectral invariants to prove assertions for rectifiable curves with an additional condition. Our result is on the line of these.

Our results are also a generalization of the following. Emch [Emc16] proved the existence of an inscribed square for piecewise analytic curves satisfying some additional assumptions. Schnirelman [Sch44] proved it for a class of curves that contains C 2 C^{2}, and Stromquist [Str89] proved for locally monotone curves. Tao [Tao17] proved the existence of an inscribed square for a curve that is the union of the graphs of two Lipschitz continuous functions with Lipschitz constant less than 1 1. Greene–Lobb [GL24b] strengthened Tao’s result to the case where the Lipschitz constant is less than 1 + 2 1+\sqrt{2}. Feller–Golla [FG23] has weakened the regularity condition of the result by Hugelmeyer [Hug18].

There are also some recent results [Gao24, Hug24, GL24a] for related problems with the use of Lagrangian intersection Floer theory.

## 2 Preliminaries

Throughout this paper, we set the base field 𝐤 \mathbf{k} to be 𝔽 2 = ℤ / 2 ​ ℤ \mathbb{F}_{2}=\mathbb{Z}/2\mathbb{Z}. Let X X be a manifold. Let π: T ∗ ​ X → X \pi\colon T^{*}X\to X denote the cotangent bundle and ( x; ξ) (x;\xi) denote the homogeneous symplectic local coordinate on T ∗ ​ X T^{*}X. We denote by λ X = ∑ i ξ i ​ d ​ x i \lambda_{X}=\sum_{i}\xi_{i}dx_{i} the Liouville 1 1 -form on T ∗ ​ X T^{*}X. We often simply write λ \lambda for λ X \lambda_{X}.

###### Notation 2.1.

For objects F, G F,G in a 𝐤 \mathbf{k} -linear stable ( ∞ \infty -)category, Hom ⁡ ( F, G) \operatorname{Hom}(F,G) (resp. End ⁡ ( F) \operatorname{End}(F)) denotes the Hom (resp. End) object in Mod ⁡ ( 𝐤) \operatorname{Mod}(\mathbf{k}), the presentable stable category of 𝐤 \mathbf{k} -vector spaces. For v ∈ H n ​ ( Hom ⁡ ( F, G)) v\in H^{n}(\operatorname{Hom}(F,G)) (resp. v ∈ H n ​ ( End ⁡ ( F)) v\in H^{n}(\operatorname{End}(F))) for some n ∈ ℤ n\in\mathbb{Z}, we simply write v ∈ Hom ⁡ ( F, G) ​ [n] v\in\operatorname{Hom}(F,G)[n] (resp. v ∈ End ⁡ ( F) ​ [n] v\in\operatorname{End}(F)[n]).

### 2.1 Twisted sheaves

Let Sh ⁡ ( X) \operatorname{\mathrm{Sh}}(X) be the 𝐤 \mathbf{k} -linear presentable stable category of sheaves of 𝐤 \mathbf{k} -vector spaces on X X. For each object F ∈ Sh ⁡ ( X) F\in\operatorname{\mathrm{Sh}}(X), we write SS ⁡ ( F) \CMS(F) for the *conic microsupport*1 1 1 In the literature, this is usually called the microsupport, but we use this name for the non-conic microsupport defined below. of F F, which is a closed conic subset of T ∗ ​ X T^{*}X. For a closed subset A A of T ∗ ​ X T^{*}X, we denote by Sh A ⁡ ( X) \operatorname{\mathrm{Sh}}_{A}(X) the subcategory of Sh ⁡ ( X) \operatorname{\mathrm{Sh}}(X) consisting of objects with conic microsupport contained in A A.

In this paper, we use the notion of twisted sheaves. We give a short review for twisted sheaves from [Kas89]. Guillermou [Gui12, Gui23] and Jin [Jin20] used twisted sheaves in the process of constructing sheaf quantizations of compact exact Lagrangian submanifolds in cotangent bundles, and we use them in a parallel manner in this work. The formulation within the context of ∞ \infty -categories has been done in [CKNS24], and we follow their approach. See [CKNS24] for the precise definition and treatment of twisted sheaves. Here, we only treat very restrictive twistings and one can describe twisted sheaves via untwisted sheaves. See remark 2.6 below.

Let Pic ⁡ ( 𝐤) \operatorname{Pic}(\mathbf{k}) be the ( ∞ \infty -)group consisting of the invertible objects in Mod ⁡ ( 𝐤) \operatorname{Mod}(\mathbf{k}). In our setting 𝐤 = ℤ / 2 ​ ℤ \mathbf{k}=\mathbb{Z}/2\mathbb{Z}, Pic ⁡ ( 𝐤) \operatorname{Pic}(\mathbf{k}) is isomorphic to ℤ \mathbb{Z} (the element 𝐤 ⁡ [n] ∈ Pic ⁡ ( 𝐤) \mathbf{k}[n]\in\operatorname{Pic}(\mathbf{k}) corresponds to n ∈ ℤ n\in\mathbb{Z}). Let η: X → B ​ Pic ⁡ ( 𝐤) \eta\colon X\to B\operatorname{Pic}(\mathbf{k}) be a twisting. We denote Sh η ⁡ ( X) \operatorname{\mathrm{Sh}}^{\eta}(X) the category of sheaves on X X twisted by η \eta. A homotopy between two twistings η 1 \eta_{1} and η 2 \eta_{2} gives an identification Sh η 1 ⁡ ( X) ≃ Sh η 2 ⁡ ( X) \operatorname{\mathrm{Sh}}^{\eta_{1}}(X)\simeq\operatorname{\mathrm{Sh}}^{\eta_{2}}(X). In particular, a null homotopy (to the basepoint) of a twisting η \eta gives an identification Sh η ⁡ ( X) ≃ Sh ⁡ ( X) \operatorname{\mathrm{Sh}}^{\eta}(X)\simeq\operatorname{\mathrm{Sh}}(X). Let X, Y X,Y be manifolds and η X: X → B ​ Pic ⁡ ( 𝐤) \eta_{X}\colon X\to B\operatorname{Pic}(\mathbf{k}) (resp. η Y: Y → B ​ Pic ⁡ ( 𝐤) \eta_{Y}\colon Y\to B\operatorname{Pic}(\mathbf{k})) be a twisting. For a morphism of manifolds f: X → Y f\colon X\to Y, if f ∗ ​ η Y ≔ η Y ∘ f = η X f^{*}\eta_{Y}\coloneqq\eta_{Y}\circ f=\eta_{X}, one can define functors 2 2 2 In this paper, we use the symbol f ∗ f^{*} instead of f − 1 f^{-1}.

 | f ∗, f!: Sh η X ( X) → Sh η Y ( Y), f ∗, f!: Sh η Y ( Y) → Sh η X ( X) f_{*},f_{!}\colon\operatorname{\mathrm{Sh}}^{\eta_{X}}(X)\to\operatorname{\mathrm{Sh}}^{\eta_{Y}}(Y),\quad f^{*},f^{!}\colon\operatorname{\mathrm{Sh}}^{\eta_{Y}}(Y)\to\operatorname{\mathrm{Sh}}^{\eta_{X}}(X) |  |

satisfying the adjunction properties f ∗ ⊣ f ∗ f^{*}\dashv f_{*} and f! ⊣ f! f_{!}\dashv f^{!}. Moreover, for two twisting η, η ′: X → B ​ Pic ⁡ ( 𝐤) \eta,\eta^{\prime}\colon X\to B\operatorname{Pic}(\mathbf{k}), we can define functors

 | ⊗: Sh η ⁡ ( X) × Sh η ′ ⁡ ( X) \displaystyle\otimes\colon\operatorname{\mathrm{Sh}}^{\eta}(X)\times\operatorname{\mathrm{Sh}}^{\eta^{\prime}}(X) | → Sh η ⋅ η ′ ⁡ ( X), \displaystyle\to\operatorname{\mathrm{Sh}}^{\eta\cdot\eta^{\prime}}(X), |  |

 | ℋ ​ o ​ m: Sh η ⁡ ( X) op × Sh η ′ ⁡ ( X) \displaystyle\mathop{{\mathcal{H}}om}\nolimits\colon\operatorname{\mathrm{Sh}}^{\eta}(X)^{\mathrm{op}}\times\operatorname{\mathrm{Sh}}^{\eta^{\prime}}(X) | → Sh η − 1 ⋅ η ′ ⁡ ( X). \displaystyle\to\operatorname{\mathrm{Sh}}^{\eta^{-1}\cdot\eta^{\prime}}(X). |  |

For an object F ∈ Sh η ⁡ ( X) F\in\operatorname{\mathrm{Sh}}^{\eta}(X), we can define its conic microsupport SS ⁡ ( F) \CMS(F) in a similar way to the untwisted case. We define Sh A η ⁡ ( X) \operatorname{\mathrm{Sh}}^{\eta}_{A}(X) in a similar way to the untwisted case.

We recall some facts about the microlocalization (see [KS90, Chap. IV]), in the twisted case. Let η 1, η 2: X → B ​ Pic ⁡ ( 𝐤) \eta_{1},\eta_{2}\colon X\to B\operatorname{Pic}(\mathbf{k}) be two twistings and let F ∈ Sh η 1 ⁡ ( X) F\in\operatorname{\mathrm{Sh}}^{\eta_{1}}(X) and G ∈ Sh η 2 ⁡ ( X) G\in\operatorname{\mathrm{Sh}}^{\eta_{2}}(X). One can define a twisted sheaf μ ​ h ​ o ​ m ​ ( F, G) ∈ Sh η 1 − 1 ⋅ η 2 ⁡ ( T ∗ ​ X) \mu hom(F,G)\in\operatorname{\mathrm{Sh}}^{\eta_{1}^{-1}\cdot\eta_{2}}(T^{*}X) on T ∗ ​ X T^{*}X in a similar way to [KS90, Section 4.4], where η 1 − 1 ⋅ η 2: T ∗ ​ X → B ​ Pic ⁡ ( 𝐤) \eta_{1}^{-1}\cdot\eta_{2}\colon T^{*}X\to B\operatorname{Pic}(\mathbf{k}) is the composite of the projection T ∗ ​ X → X T^{*}X\to X and the twisting η 1 − 1 ⋅ η 2: X → B ​ Pic ⁡ ( 𝐤) \eta_{1}^{-1}\cdot\eta_{2}\colon X\to B\operatorname{Pic}(\mathbf{k}). Indeed, since the original μ ​ h ​ o ​ m \mu hom is defined via 6-functors, we can apply the same construction by tracing the twisting. The support of μ ​ h ​ o ​ m ​ ( F, G) \mu hom(F,G) is contained in SS ⁡ ( F) ∩ SS ⁡ ( G) \CMS(F)\cap\CMS(G). We have a natural isomorphism ℋ ​ o ​ m ⁡ ( F, G) → ∼ π ∗ ​ μ ​ h ​ o ​ m ​ ( F, G) \mathop{{\mathcal{H}}om}\nolimits(F,G)\xrightarrow{\sim}\pi_{*}\mu hom(F,G), and also ℋ ​ o ​ m ⁡ ( F, G) ≃ i ∗ ​ μ ​ h ​ o ​ m ​ ( F, G) \mathop{{\mathcal{H}}om}\nolimits(F,G)\simeq i^{*}\mu hom(F,G), where i i is the inclusion of the zero-section.

Now we assume that Λ = SS ⁡ ( F) ∖ 0 X \Lambda=\CMS(F)\setminus 0_{X} is a (conic) connected Lagrangian submanifold of T ∗ ​ X ∖ 0 X T^{*}X\setminus 0_{X}. For a function f: X → ℝ f\colon X\to\mathbb{R} of class C 2 C^{2} such that Γ d ​ f \Gamma_{df} intersect Λ \Lambda transversally at ( x 0; ξ 0) (x_{0};\xi_{0}), the space m ( F, f, x 0) = ( Γ { f ≥ f ( x 0) } ( F)) x 0 m(F,f,x_{0})=(\Gamma_{\{f\geq f(x_{0})\}}(F))_{x_{0}} is called the *microstalk*at ( x 0; ξ 0) (x_{0};\xi_{0}). It is proved that m ⁡ ( F, f, x 0) m(F,f,x_{0}) is independent of f f and ( x 0; ξ 0) (x_{0};\xi_{0}) up to shift (see [KS90] Prop. 7.5.3 and Cor. 7.5.7). We say that F F is *simple*or of microlocal rank 1 1 along Λ \Lambda if m ⁡ ( F, f, x 0) ≃ 𝐤 ⁡ [d] m(F,f,x_{0})\simeq\mathbf{k}[d] for some d ∈ ℤ d\in\mathbb{Z}.

Let F, G ∈ Sh η ⁡ ( X) F,G\in\operatorname{\mathrm{Sh}}^{\eta}(X) be simple sheaves and assume that SS ⁡ ( F) \CMS(F) and SS ⁡ ( G) \CMS(G) intersect cleanly outside the zero-section. Then, for a connected component Λ 0 \Lambda_{0} of ( SS ⁡ ( F) ∩ SS ⁡ ( G)) ∖ 0 X (\CMS(F)\cap\CMS(G))\setminus 0_{X}, we have an isomorphism μ ​ h ​ o ​ m ​ ( F, G) | Λ 0 ≃ 𝐤 Λ 0 ​ [d] \mu hom(F,G)|_{\Lambda_{0}}\simeq\mathbf{k}_{\Lambda_{0}}[d] for some d ∈ ℤ d\in\mathbb{Z}.

### 2.2 Twisted Tamarkin category

In this subsection, we introduce a twisted version of the Tamarkin category. We follow [KSZ23] for the ∞ \infty -categorical treatment of the Tamarkin category. We replace the Tamarkin direction ℝ t \mathbb{R}_{t} with ℝ t / π ​ ℤ \mathbb{R}_{t}/\pi\mathbb{Z}, where π \pi is the area of the domain bounded by the standard unit circle C 0 C_{0} in ℝ 2 \mathbb{R}^{2} with radius 1 1.

Let N N be a manifold. We fix a twisting η: ℝ t / π ​ ℤ → B ​ Pic ⁡ ( 𝐤) \eta\colon\mathbb{R}_{t}/\pi\mathbb{Z}\to B\operatorname{Pic}(\mathbf{k}). Since we work on 𝐤 = 𝔽 2 \mathbf{k}=\mathbb{F}_{2}, we may assume that η \eta is the delooping of ℤ → Pic ⁡ ( 𝐤); 1 ↦ 𝐤 ⁡ [n] \mathbb{Z}\to\operatorname{Pic}(\mathbf{k});1\mapsto\mathbf{k}[n] for some n ∈ ℤ n\in\mathbb{Z}. By abuse of notation, we also write η \eta for the composite of η \eta and the projection N × ℝ t / π ​ ℤ → ℝ t / π ​ ℤ N\times\mathbb{R}_{t}/\pi\mathbb{Z}\to\mathbb{R}_{t}/\pi\mathbb{Z}.

We consider the category Sh η ⁡ ( N × ℝ t / π ​ ℤ) \operatorname{\mathrm{Sh}}^{\eta}(N\times\mathbb{R}_{t}/\pi\mathbb{Z}) consisting of sheaves on N × ℝ t / π ​ ℤ N\times\mathbb{R}_{t}/\pi\mathbb{Z} twisted by η \eta. We define the twisted version of the Tamarkin category by

 | 𝒯 η ( T ∗ N) ≔ Sh η ( N × ℝ t / π ℤ) / { F ∣ SS ( F) ⊂ { τ ≤ 0 } }. \mathcal{T}^{\eta}(T^{*}N)\coloneqq\operatorname{\mathrm{Sh}}^{\eta}(N\times\mathbb{R}_{t}/\pi\mathbb{Z})/\{F\mid\CMS(F)\subset\{\tau\leq 0\}\}. |  |

The quotient functor Sh η ⁡ ( N × ℝ t / π ​ ℤ) → 𝒯 η ​ ( T ∗ ​ N) \operatorname{\mathrm{Sh}}^{\eta}(N\times\mathbb{R}_{t}/\pi\mathbb{Z})\to\mathcal{T}^{\eta}(T^{*}N) admits a left adjoint and a right adjoint. Both of these functors are fully faithful. We sometimes regard 𝒯 η ​ ( T ∗ ​ N) \mathcal{T}^{\eta}(T^{*}N) as a full subcategory of Sh η ⁡ ( N × ℝ t / π ​ ℤ) \operatorname{\mathrm{Sh}}^{\eta}(N\times\mathbb{R}_{t}/\pi\mathbb{Z}) via either of these functors. For an object F ∈ 𝒯 η ​ ( T ∗ ​ M) F\in\mathcal{T}^{\eta}(T^{*}M), we define

 | SS ∙ ( F) ≔ SS ( F) ∩ { τ = 1 }. \DMS(F)\coloneqq\CMS(F)\cap\{\tau=1\}. |  |

For a closed subset A ⊂ T ∗ ​ N × ℝ t / π ​ ℤ A\subset T^{*}N\times\mathbb{R}_{t}/\pi\mathbb{Z}, we set

 | 𝒯 A η ​ ( T ∗ ​ N) ≔ { F ∈ 𝒯 η ​ ( T ∗ ​ N) ∣ SS ∙ ⁡ ( F) ⊂ A }. \mathcal{T}^{\eta}_{A}(T^{*}N)\coloneqq\{F\in\mathcal{T}^{\eta}(T^{*}N)\mid\DMS(F)\subset A\}. |  |

We set T τ > 0 ∗ ( N × ℝ t / π ℤ) ≔ { τ > 0 } ⊂ T ∗ ( N × ℝ t / π ℤ) T^{*}_{\tau>0}(N\times\mathbb{R}_{t}/\pi\mathbb{Z})\coloneqq\{\tau>0\}\subset T^{*}(N\times\mathbb{R}_{t}/\pi\mathbb{Z}) and define a map ρ: T τ > 0 ∗ ​ ( N × ℝ t / π ​ ℤ) → T ∗ ​ N \rho\colon T^{*}_{\tau>0}(N\times\mathbb{R}_{t}/\pi\mathbb{Z})\to T^{*}N by ( x, t, ξ, τ) ↦ ( x; ξ / τ) (x,t;\xi,\tau)\mapsto(x;\xi/\tau). For an object F ∈ 𝒯 η ​ ( T ∗ ​ N) F\in\mathcal{T}^{\eta}(T^{*}N), we set

 | MS ⁡ ( F) ≔ ρ ( SS ( F) ∩ { τ > 0 }) ¯ ⊂ T ∗ ​ N \MS(F)\coloneqq\overline{\rho(\CMS(F)\cap\{\tau>0\})}\subset T^{*}N |  |

and call it the (non-conic or reduced) *microsupport*of F F.

Let q i: N × ℝ / π ​ ℤ × ℝ / π ​ ℤ → N × ℝ t / π ​ ℤ; ( x, t 1, t 2) ↦ ( x, t i) q_{i}\colon N\times\mathbb{R}/\pi\mathbb{Z}\times\mathbb{R}/\pi\mathbb{Z}\to N\times\mathbb{R}_{t}/\pi\mathbb{Z};(x,t_{1},t_{2})\mapsto(x,t_{i}) denote the projection and m: N × ℝ / π ​ ℤ × ℝ / π ​ ℤ → N × ℝ t / π ​ ℤ; ( x, t 1, t 2) ↦ ( x, t 1 + t 2) m\colon N\times\mathbb{R}/\pi\mathbb{Z}\times\mathbb{R}/\pi\mathbb{Z}\to N\times\mathbb{R}_{t}/\pi\mathbb{Z};(x,t_{1},t_{2})\mapsto(x,t_{1}+t_{2}) denote the addition map. For F, G ∈ 𝒯 η ​ ( T ∗ ​ N) F,G\in\mathcal{T}^{\eta}(T^{*}N), we define

 | F ⋆ G \displaystyle F\star G | ≔ m! ( q 1 ∗ F ⊗ q 2 ∗ G) ∈ 𝒯 η ( T ∗ N), \displaystyle\coloneqq m_{!}(q_{1}^{*}F\otimes q_{2}^{*}G)\in\mathcal{T}^{\eta}(T^{*}N), |  |

 | ℋ ​ o ​ m ⋆ ⁡ ( F, G) \displaystyle\mathop{{\mathcal{H}}om}\nolimits^{\star}(F,G) | ≔ q 1 ∗ ℋ ​ o ​ m ( q 2 ∗ F, m! G) ∈ 𝒯 η ( T ∗ N). \displaystyle\coloneqq{q_{1}}_{*}\mathop{{\mathcal{H}}om}\nolimits(q_{2}^{*}F,m^{!}G)\in\mathcal{T}^{\eta}(T^{*}N). |  |

Then ⋆ \star induces the monoidal operation of 𝒯 η ​ ( T ∗ ​ N) \mathcal{T}^{\eta}(T^{*}N), and ℋ ​ o ​ m ⋆ \mathop{{\mathcal{H}}om}\nolimits^{\star} defines the internal hom of 𝒯 η ​ ( T ∗ ​ N) \mathcal{T}^{\eta}(T^{*}N).

For a ∈ ℝ a\in\mathbb{R}, let T a T_{a} be the map N × ℝ t / π ​ ℤ → N × ℝ t / π ​ ℤ: ( x, t) ↦ ( x, t + [a]) N\times\mathbb{R}_{t}/\pi\mathbb{Z}\to N\times\mathbb{R}_{t}/\pi\mathbb{Z}\colon(x,t)\mapsto(x,t+[a]), where [a] [a] is the image of the quotient map ℓ: ℝ t → ℝ t / π ​ ℤ \ell\colon\mathbb{R}_{t}\to\mathbb{R}_{t}/\pi\mathbb{Z}. By definition, T a ∗ {T_{a}}_{*} is a functor from Sh T a ∗ ​ η ⁡ ( N × ℝ t / π ​ ℤ) \operatorname{\mathrm{Sh}}^{T_{a}^{*}\eta}(N\times\mathbb{R}_{t}/\pi\mathbb{Z}) to Sh η ⁡ ( N × ℝ t / π ​ ℤ) \operatorname{\mathrm{Sh}}^{\eta}(N\times\mathbb{R}_{t}/\pi\mathbb{Z}). We identify Sh T a ∗ ​ η ⁡ ( N × ℝ t / π ​ ℤ) \operatorname{\mathrm{Sh}}^{T_{a}^{*}\eta}(N\times\mathbb{R}_{t}/\pi\mathbb{Z}) with Sh η ⁡ ( N × ℝ t / π ​ ℤ) \operatorname{\mathrm{Sh}}^{\eta}(N\times\mathbb{R}_{t}/\pi\mathbb{Z}) by the homotopy ( η ∘ T s ​ a) s ∈ [0, 1] (\eta\circ T_{sa})_{s\in[0,1]}. We obtain an automorphism on Sh η ⁡ ( N × ℝ t / π ​ ℤ) \operatorname{\mathrm{Sh}}^{\eta}(N\times\mathbb{R}_{t}/\pi\mathbb{Z}) and it induces an automorphism on 𝒯 η ​ ( T ∗ ​ N) \mathcal{T}^{\eta}(T^{*}N). We write the functor as T a T_{a}. Note that T 0 = id T_{0}=\operatorname{id} and T π T_{\pi} is the shift functor [− n] [-n].

The functor T a T_{a} is naturally isomorphic to the functor ℓ! 𝐤 N × [a, ∞) ⋆ ( −) \ell_{!}\mathbf{k}_{N\times[a,\infty)}\star(\mathchar 45). For a ≤ a ′ ∈ ℝ a\leq a^{\prime}\in\mathbb{R}, a natural transformation τ a, a ′: T a ⇒ T a ′ \tau_{a,a^{\prime}}\colon T_{a}\Rightarrow T_{a^{\prime}} is induced by the natural morphism 𝐤 N × [a, ∞) → 𝐤 N × [a ′, ∞) \mathbf{k}_{N\times[a,\infty)}\to\mathbf{k}_{N\times[a^{\prime},\infty)}. This enable us to define a pseudo-distance d d on the set of the objects of 𝒯 η ​ ( T ∗ ​ N) \mathcal{T}^{\eta}(T^{*}N) as in [AI20, AI23, AI24]. Namely, for F, G ∈ 𝒯 η ​ ( T ∗ ​ N) F,G\in\mathcal{T}^{\eta}(T^{*}N), define

 | d ⁡ ( F, G) ≔ inf { a + b | ∃ α: F → T a ​ G, ∃ β: G → T b ​ F ​ such that T a ​ β ∘ α ≃ τ 0, a + b ​ ( F), T b ​ α ∘ β ≃ τ 0, a + b ​ ( G) }. d(F,G)\coloneqq\inf\left\{a+b\mathrel{}\middle|\mathrel{}\begin{aligned} &\exists\alpha\colon F\to T_{a}G,\exists\beta\colon G\to T_{b}F\text{ such that }\\ &T_{a}\beta\circ\alpha\simeq\tau_{0,a+b}(F),T_{b}\alpha\circ\beta\simeq\tau_{0,a+b}(G)\end{aligned}\right\}. |  |

Such a pair of morphisms ( α, β) (\alpha,\beta) is called *( a, b) (a,b) -interleaving*for ( F, G) (F,G) and the pseudo-distance d d is called the *interleaving distance*. This pseudo-distance is in fact complete.

###### Proposition 2.2 ( [AI24, Cor. 4.5] and [GV24, Prop. 6.22]).

The interleaving distance d d is a complete pseudo-distance, i.e., any Cauchy sequence with respect to d d has a limit object in 𝒯 η ​ ( T ∗ ​ N) \mathcal{T}^{\eta}(T^{*}N).

The conic microsupport of a limit object can be estimated as follows.

###### Proposition 2.3 ( [GV24, Prop. 6.26]).

Let ( F n) n (F_{n})_{n} be a sequence in 𝒯 η ​ ( T ∗ ​ N) \mathcal{T}^{\eta}(T^{*}N) and assume that it converges to F ∞ F_{\infty} with respect to the interleaving distance d d. Then

 | SS ∙ ⁡ ( F ∞) ⊂ ⋂ k ∈ ℕ ⋃ n ≥ k SS ∙ ⁡ ( F n) ¯. \DMS(F_{\infty})\subset\bigcap_{k\in\mathbb{N}}\overline{\bigcup_{n\geq k}\DMS(F_{n})}. |  |

The interleaving distance d d is degenerate in general, but it is proved that d d is non-degenerate on the category of metric-limit objects of constructible sheaves. For a real analytic manifold N N, an object F ∈ 𝒯 η ​ ( T ∗ ​ N) F\in\mathcal{T}^{\eta}(T^{*}N) is said to be *limit constructible*if it is a metric limit of constructible sheaves with respect to the interleaving distance d d. A limit object of a sequence of limit constructible sheaves is unique up to isomorphism due to the following proposition.

###### Proposition 2.4 ( [GV24, Prop. B.8]).

If F, G ∈ 𝒯 η ​ ( T ∗ ​ N) F,G\in\mathcal{T}^{\eta}(T^{*}N) are limit constructible and d ⁡ ( F, G) = 0 d(F,G)=0, then F ≃ G F\simeq G.

We have the following isomorphism:

 | Hom ( F, T a G) ≃ Γ [− a, ∞) ( ℝ; ℓ! q ∗ ℋ ​ o ​ m ⋆ ( F, G)), \operatorname{Hom}(F,T_{a}G)\simeq\Gamma_{[-a,\infty)}(\mathbb{R};\ell^{!}q_{*}\mathop{{\mathcal{H}}om}\nolimits^{\star}(F,G)), |  | (2.1) |

where q: N × ℝ t / π ​ ℤ → ℝ t / π ​ ℤ q\colon N\times\mathbb{R}_{t}/\pi\mathbb{Z}\to\mathbb{R}_{t}/\pi\mathbb{Z} is the projection. We denote by 𝒯 ⁡ ( T ∗ ​ N) \mathcal{T}(T^{*}N) the usual Tamarkin category of T ∗ ​ N T^{*}N defined as

 | 𝒯 ( T ∗ N) ≔ Sh ( N × ℝ t) / { F ∣ SS ( F) ⊂ { τ ≤ 0 } }. \mathcal{T}(T^{*}N)\coloneqq\operatorname{\mathrm{Sh}}(N\times\mathbb{R}_{t})/\{F\mid\CMS(F)\subset\{\tau\leq 0\}\}. |  |

Then the functor ℓ!: 𝒯 η ( T ∗ N) → 𝒯 ( T ∗ N) \ell^{!}\colon\mathcal{T}^{\eta}(T^{*}N)\to\mathcal{T}(T^{*}N) is conservative and the functor ℓ!: 𝒯 ( T ∗ N) → 𝒯 η ( T ∗ N) \ell_{!}\colon\mathcal{T}(T^{*}N)\to\mathcal{T}^{\eta}(T^{*}N) is symmetric monoidal. One can equip a complete pseudo-distance d d with 𝒯 ⁡ ( T ∗ ​ N) \mathcal{T}(T^{*}N) in a similar way to 𝒯 η ​ ( T ∗ ​ N) \mathcal{T}^{\eta}(T^{*}N), and obtain a conic microsupport estimate similar to proposition 2.3. One can also define limit constructible objects in 𝒯 ⁡ ( T ∗ ​ N) \mathcal{T}(T^{*}N) similarly.

A constructible object in 𝒯 ⁡ ( pt) \mathcal{T}(\mathrm{pt}) is isomorphic to ⨁ α ∈ A 𝐤 I α ​ [d α] \bigoplus_{\alpha\in A}\mathbf{k}_{I_{\alpha}}[d_{\alpha}] for a locally finite family of intervals ( I α) α ∈ A (I_{\alpha})_{\alpha\in A} and a family of integers ( d α) α ∈ A (d_{\alpha})_{\alpha\in A} ( [KS18, Thm. 1.17] and [Gui23, Cor. IV.4.3]). For a limit constructible object in 𝒯 ⁡ ( pt) \mathcal{T}(\mathrm{pt}), we have the following decomposition by interval modules.

###### Proposition 2.5 ( [GV24, Cor. B.12]).

Let F ∈ 𝒯 ⁡ ( pt) F\in\mathcal{T}(\mathrm{pt}) and assume that F F is limit constructible. Then there exists a countable family of intervals ( I α) α ∈ A (I_{\alpha})_{\alpha\in A} and a family of integers ( d α) α ∈ A (d_{\alpha})_{\alpha\in A} such that

 | F ≃ ⨁ α ∈ A 𝐤 I α ​ [d α]. F\simeq\bigoplus_{\alpha\in A}\mathbf{k}_{I_{\alpha}}[d_{\alpha}]. |  |

Moreover, for any ε > 0 \varepsilon>0, the family ( I α ∣ α ∈ A, | I α | ≥ ε) (I_{\alpha}\mid\alpha\in A,|I_{\alpha}|\geq\varepsilon) is locally finite.

When N = pt N=\mathrm{pt}, we simply write 𝒯 η ≔ 𝒯 η ​ ( pt) \mathcal{T}^{\eta}\coloneqq\mathcal{T}^{\eta}(\mathrm{pt}). Similar to [KSZ23, Prop. 5.5] combined with [CKNS24, Lem. 2.9], one can check

 | 𝒯 η ​ ( T ∗ ​ N) ≃ Sh ⁡ ( N) ⊗ 𝒯 η ≃ Sh ⁡ ( N; 𝒯 η), \mathcal{T}^{\eta}(T^{*}N)\simeq\operatorname{\mathrm{Sh}}(N)\otimes\mathcal{T}^{\eta}\simeq\operatorname{\mathrm{Sh}}(N;\mathcal{T}^{\eta}), |  |

where the last category stands for the category of sheaves on N N with coefficient in 𝒯 η \mathcal{T}^{\eta}. Through this identification, the operations ⋆ \star and ℋ ​ o ​ m ⋆ \mathop{{\mathcal{H}}om}\nolimits^{\star} in the category 𝒯 η ​ ( T ∗ ​ N) \mathcal{T}^{\eta}(T^{*}N) are usual ⊗ \otimes and ℋ ​ o ​ m \mathop{{\mathcal{H}}om}\nolimits with coefficient in 𝒯 η \mathcal{T}^{\eta}. See [Vol25] for 6-functor formalism for locally compact Hausdorff spaces and more general coefficients.

For K 12 ∈ 𝒯 η ​ ( T ∗ ​ ( N 1 × N 2)), K 23 ∈ 𝒯 η ​ ( T ∗ ​ ( N 2 × N 3)) K_{12}\in\mathcal{T}^{\eta}(T^{*}(N_{1}\times N_{2})),K_{23}\in\mathcal{T}^{\eta}(T^{*}(N_{2}\times N_{3})), we can also define the operation

○

⋆ \ostar by

 | K 12 ​

○

⋆ ⁡ K 23 ≔ m 13! ​ ( q 12 ∗ ​ K 12 ⊗ q 23 ∗ ​ K 23), K_{12}\ostar K_{23}\coloneqq m_{13!}(q_{12}^{*}K_{12}\otimes q_{23}^{*}K_{23}), |  |

where q i ​ j: N 1 × N 2 × N 3 × ℝ / π ​ ℤ × ℝ / π ​ ℤ → N i × N j × ℝ t / π ​ ℤ q_{ij}\colon N_{1}\times N_{2}\times N_{3}\times\mathbb{R}/\pi\mathbb{Z}\times\mathbb{R}/\pi\mathbb{Z}\to N_{i}\times N_{j}\times\mathbb{R}_{t}/\pi\mathbb{Z} is the projection, and

 | m 13: N 1 × N 2 × N 3 × ℝ / π ​ ℤ × ℝ / π ​ ℤ \displaystyle m_{13}\colon N_{1}\times N_{2}\times N_{3}\times\mathbb{R}/\pi\mathbb{Z}\times\mathbb{R}/\pi\mathbb{Z} | → N 1 × N 3 × ℝ / π ​ ℤ; \displaystyle\to N_{1}\times N_{3}\times\mathbb{R}/\pi\mathbb{Z}; |  |

 | ( x 1, x 2, x 3, t 1, t 2) \displaystyle(x_{1},x_{2},x_{3},t_{1},t_{2}) | ↦ ( x 1, x 3, t 1 + t 2). \displaystyle\mapsto(x_{1},x_{3},t_{1}+t_{2}). |  |

Through the identification with sheaf category with coefficient in 𝒯 η \mathcal{T}^{\eta}, the operation

○

⋆ \ostar corresponds to the usual convolution.

For K 12 ∈ 𝒯 ⁡ ( T ∗ ​ ( N 1 × N 2)), K 23 ∈ 𝒯 η ​ ( T ∗ ​ ( N 2 × N 3)) K_{12}\in\mathcal{T}(T^{*}(N_{1}\times N_{2})),K_{23}\in\mathcal{T}^{\eta}(T^{*}(N_{2}\times N_{3})), we can also define the operation

○

⋆ \ostar by a similar method. This K 12 ​

○

⋆ ⁡ K 23 K_{12}\ostar K_{23} is isomorphic to ℓ! K 12

○

⋆ K 23 \ell_{!}K_{12}\ostar K_{23} defined above.

###### Remark 2.6.

The category 𝒯 η ​ ( T ∗ ​ N) \mathcal{T}^{\eta}(T^{*}N) can be identified with a full subcategory of Sh η ⁡ ( N × ℝ t / π ​ ℤ) \operatorname{\mathrm{Sh}}^{\eta}(N\times\mathbb{R}_{t}/\pi\mathbb{Z}). We can describe objects of Sh η ⁡ ( N × ℝ t / π ​ ℤ) \operatorname{\mathrm{Sh}}^{\eta}(N\times\mathbb{R}_{t}/\pi\mathbb{Z}) via untwisted sheaves. Take real numbers t 0 < t 1 < t 2 < t 3 t_{0}<t_{1}<t_{2}<t_{3} satisfying t 2 − t 0 < π t_{2}-t_{0}<\pi, t 3 − t 1 < π t_{3}-t_{1}<\pi, and t 3 − t 0 > π t_{3}-t_{0}>\pi. Set U 0 = ℓ ⁡ ( ( t 0, t 2)) U_{0}=\ell((t_{0},t_{2})), U 0 = ℓ ⁡ ( ( t 1, t 3)) U_{0}=\ell((t_{1},t_{3})), V 0 = ℓ ⁡ ( ( t 0, t 1)) V_{0}=\ell((t_{0},t_{1})), and V 1 = ℓ ⁡ ( ( t 2, t 3)) V_{1}=\ell((t_{2},t_{3})). By the sheaf property of Sh η ⁡ ( −) \operatorname{\mathrm{Sh}}^{\eta}(\mathchar 45) on M × ℝ t / π ​ ℤ M\times\mathbb{R}_{t}/\pi\mathbb{Z}, an object Sh η ⁡ ( N × ℝ t / π ​ ℤ) \operatorname{\mathrm{Sh}}^{\eta}(N\times\mathbb{R}_{t}/\pi\mathbb{Z}) is equivalent to the datum ( F 0, F 1, α 1, α 0) (F_{0},F_{1},\alpha_{1},\alpha_{0}) where F i F_{i} is an object of Sh ⁡ ( N × U i) \operatorname{\mathrm{Sh}}(N\times U_{i}) for each i = 0, 1 i=0,1, and α 1: F 0 | N × V 1 ≃ F 1 | N × V 1 \alpha_{1}\colon F_{0}|_{N\times V_{1}}\simeq F_{1}|_{N\times V_{1}}, α 0: F 0 ​ [n] | N × V 0 ≃ F 1 | N × V 0 \alpha_{0}\colon F_{0}[n]|_{N\times V_{0}}\simeq F_{1}|_{N\times V_{0}} are isomorphisms.

Gluing F 0 F_{0} and F 1 F_{1} by α 1 \alpha_{1} firstly, we can see that above datum is also equivalent to ( F, α 0) (F,\alpha_{0}) where F F is an object of Sh ⁡ ( N × ( t 0, t 3)) \operatorname{\mathrm{Sh}}(N\times(t_{0},t_{3})) and α 0: F ⁡ [n] | N × ( t 0, t 3 − π) ≃ F | N × ( t 0 + π, t 3) \alpha_{0}\colon F[n]|_{N\times(t_{0},t_{3}-\pi)}\simeq F|_{N\times(t_{0}+\pi,t_{3})} is an isomorphism via the identification N × ( t 0, t 3 − π) ≃ N × ( t 0 + π, t 3): ( x, t) ↦ ( x, t + π) N\times(t_{0},t_{3}-\pi)\simeq N\times(t_{0}+\pi,t_{3})\colon(x,t)\mapsto(x,t+\pi).

For F, G ∈ 𝒯 η ​ ( T ∗ ​ N) F,G\in\mathcal{T}^{\eta}(T^{*}N), the object μ h o m ( F, G) | { τ > 0 } ∈ Sh ( { τ > 0 }) \mu hom(F,G)|_{\{\tau>0\}}\in\operatorname{\mathrm{Sh}}(\{\tau>0\}) is invariant under isomorphisms in 𝒯 η ​ ( T ∗ ​ M) \mathcal{T}^{\eta}(T^{*}M). Not only μ h o m | { τ > 0 }: 𝒯 η ( T ∗ N) op × 𝒯 η ( T ∗ N) → Sh ( { τ > 0 }) \mu hom|_{\{\tau>0\}}\colon\mathcal{T}^{\eta}(T^{*}N)^{\mathrm{op}}\times\mathcal{T}^{\eta}(T^{*}N)\to\operatorname{\mathrm{Sh}}(\{\tau>0\}) is a functor, but also μ ​ h ​ o ​ m \mu hom makes 𝒯 η ​ ( T ∗ ​ N) \mathcal{T}^{\eta}(T^{*}N) into a Sh ( { τ > 0 }) \operatorname{\mathrm{Sh}}(\{\tau>0\}) -enriched category. This follows from the fact that μ ​ h ​ o ​ m \mu hom is the Hom sheaf of a stack called Kashiwara–Schapira stack [KS90, Gui23]. See also [KL22, Remark 2.13] for an ∞ \infty -categorical treatment. In what follows, we denote μ h o m ( F, G) | { τ > 0 } \mu hom(F,G)|_{\{\tau>0\}} simply by μ ​ h ​ o ​ m ​ ( F, G) \mu hom(F,G) for F, G ∈ 𝒯 η ​ ( T ∗ ​ N) F,G\in\mathcal{T}^{\eta}(T^{*}N).

We have the following (co)fiber sequence associated with the Hom spaces and μ ​ h ​ o ​ m \mu hom.

###### Lemma 2.7.

For F, G ∈ 𝒯 η ​ ( T ∗ ​ N) F,G\in\mathcal{T}^{\eta}(T^{*}N) such that MS ⁡ ( F) \MS(F) and MS ⁡ ( G) \MS(G) are compact, we have a fiber sequence

 | colim ε → 0 Hom ( F, T − ε G) → Hom ( F, G) → Γ ( { τ > 0 }; μ h o m ( F, G)). \operatorname*{colim}_{\varepsilon\to 0}\operatorname{Hom}(F,T_{-\varepsilon}G)\to\operatorname{Hom}(F,G)\to\Gamma(\{\tau>0\};\mu hom(F,G)). |  |

###### Proof.

Let ℋ ≔ ℓ! q ∗ ℋ ​ o ​ m ⋆ ( F, G) \mathcal{H}\coloneqq\ell^{!}q_{*}\mathop{{\mathcal{H}}om}\nolimits^{\star}(F,G). By a similar argument to [Ike19], we have an isomorphism

 | Γ [0, ∞) ( ℋ) 0 ≃ Γ ( { τ > 0 }; μ h o m ( F, G)), \Gamma_{[0,\infty)}(\mathcal{H})_{0}\simeq\Gamma(\{\tau>0\};\mu hom(F,G)), |  |

where we use the compactness assumption. For ε > 0 \varepsilon>0, we have a fiber sequence

 | Γ [ε, ∞) ​ ( ℝ, ℋ) → Γ [0, ∞) ​ ( ℝ, ℋ) → Γ [0, ε) ​ ( ( − ∞, ε), ℋ). \Gamma_{[\varepsilon,\infty)}(\mathbb{R};\mathcal{H})\to\Gamma_{[0,\infty)}(\mathbb{R};\mathcal{H})\to\Gamma_{[0,\varepsilon)}((-\infty,\varepsilon);\mathcal{H}). |  |

By ( 2.1), the first term is isomorphic to Hom ⁡ ( F, T − ε ​ G) \operatorname{Hom}(F,T_{-\varepsilon}G) and the second term is isomorphic to Hom ⁡ ( F, G) \operatorname{Hom}(F,G). Thus, by taking colimit as ε → 0 \varepsilon\to 0, we obtain the result. ∎

### 2.3 Hamiltonian action

Let H: T ∗ ​ N × I → ℝ H\colon T^{*}N\times I\to\mathbb{R} be a C ∞ C^{\infty} -function with compact support. Denote by ϕ H = ( ϕ s H) s ∈ I: T ∗ ​ N × I → T ∗ ​ N \phi^{H}=(\phi^{H}_{s})_{s\in I}\colon T^{*}N\times I\to T^{*}N be the associated Hamiltonian isotopy. It is proved in [GKS12] that there exists an object K ⁡ ( ϕ H) ∈ Sh ⁡ ( ( N × ℝ) 2 × I) K(\phi^{H})\in\operatorname{\mathrm{Sh}}((N\times\mathbb{R})^{2}\times I) whose conic microsupport outside the zero-section is equal to the conic Lagrangian movie associated with the graph of ϕ H \phi^{H}. The push forward by the map ( N × ℝ) 2 × I → N 2 × ℝ × I; ( x 1, t 1, x 2, t 2, s) ↦ ( x 1, x 2, t 1 − t 2, s) (N\times\mathbb{R})^{2}\times I\to N^{2}\times\mathbb{R}\times I;(x_{1},t_{1},x_{2},t_{2},s)\mapsto(x_{1},x_{2},t_{1}-t_{2},s) and the quotient morphism Sh ⁡ ( N 2 × ℝ × I) → 𝒯 ⁡ ( T ∗ ​ ( N 2 × I)) \operatorname{\mathrm{Sh}}(N^{2}\times\mathbb{R}\times I)\to\mathcal{T}(T^{*}(N^{2}\times I)), the object K ⁡ ( ϕ H) K(\phi^{H}) defines 𝒦 ⁡ ( ϕ H) ∈ 𝒯 ⁡ ( T ∗ ​ ( N 2 × I)) \mathcal{K}(\phi^{H})\in\mathcal{T}(T^{*}(N^{2}\times I)), which is called the sheaf quantization or the *GKS kernel*of ϕ H \phi^{H}.

With a time-independent non-negative C ∞ C^{\infty} -function H: T ∗ ​ N → ℝ H\colon T^{*}N\to\mathbb{R} with non-compact support, we can associate an object 𝒦 ​ ( ϕ H) 1 ∈ 𝒯 ⁡ ( T ∗ ​ N 2) \mathcal{K}(\phi^{H})_{1}\in\mathcal{T}(T^{*}N^{2}) as follows. We take a sequence of compact subset ( K n) n (K_{n})_{n} such that ⋃ n Int ⁡ ( K n) = T ∗ ​ N \bigcup_{n}\Int(K_{n})=T^{*}N and a sequence of cutoff functions ( χ n: T ∗ N → [0, 1]) n (\chi_{n}\colon T^{*}N\to[0,1])_{n} of class C ∞ C^{\infty} such that H n | K n ≡ 1 H_{n}|_{K_{n}}\equiv 1, supp ⁡ ( H n) ⊂ Int ⁡ ( K n + 1) \supp(H_{n})\subset\Int(K_{n+1}), and H n ≤ H n + 1 H_{n}\leq H_{n+1}. Then H n ≔ χ n ⋅ H H_{n}\coloneqq\chi_{n}\cdot H has a compact support, and thus defines 𝒦 ⁡ ( ϕ H n) ∈ 𝒯 ⁡ ( T ∗ ​ ( N 2 × I)) \mathcal{K}(\phi^{H_{n}})\in\mathcal{T}(T^{*}(N^{2}\times I)). By [GKS12], we have a canonical continuation morphism 𝒦 ​ ( ϕ H n) 1 → 𝒦 ​ ( ϕ H n + 1) 1 \mathcal{K}(\phi^{H_{n}})_{1}\to\mathcal{K}(\phi^{H_{n+1}})_{1} in 𝒯 ⁡ ( T ∗ ​ N 2) \mathcal{T}(T^{*}N^{2}) and define

 | 𝒦 ​ ( ϕ H) 1 ≔ colim n 𝒦 ​ ( ϕ H n) 1 ∈ 𝒯 ⁡ ( T ∗ ​ N 2). \mathcal{K}(\phi^{H})_{1}\coloneqq\operatorname*{colim}_{n}\mathcal{K}(\phi^{H_{n}})_{1}\in\mathcal{T}(T^{*}N^{2}). |  |

Let φ ∈ Ham c ⁡ ( T ∗ ​ N) \varphi\in\Ham_{c}(T^{*}N) be a compactly supported Hamiltonian diffeomorphism on T ∗ ​ N T^{*}N. For a compactly supported C ∞ C^{\infty} -function H: T ∗ ​ N × I → ℝ H\colon T^{*}N\times I\to\mathbb{R} such that ϕ 1 H = φ \phi^{H}_{1}=\varphi, the object 𝒦 ⁡ ( ϕ H) | s = 1 \mathcal{K}(\phi^{H})|_{s=1} does not depend on the choice of H H (see [AI24]), which we will denote by 𝒦 ⁡ ( φ) ∈ 𝒯 ⁡ ( T ∗ ​ N 2) \mathcal{K}(\varphi)\in\mathcal{T}(T^{*}N^{2}). We call 𝒦 ⁡ ( φ) \mathcal{K}(\varphi) the sheaf quantization or the *GKS kernel*of φ \varphi.

Recall that we set 𝐤 = 𝔽 2 \mathbf{k}=\mathbb{F}_{2}. In this case, it is proved in [GV24] that the distance d ⁡ ( 𝒦 ⁡ ( φ 0), 𝒦 ⁡ ( φ 1)) d(\mathcal{K}(\varphi_{0}),\mathcal{K}(\varphi_{1})) is equal to the spectral metric between φ 0 \varphi_{0} and φ 1 \varphi_{1}:

 | d ⁡ ( 𝒦 ⁡ ( φ 0), 𝒦 ⁡ ( φ 1)) = γ ⁡ ( φ 0, φ 1). d(\mathcal{K}(\varphi_{0}),\mathcal{K}(\varphi_{1}))=\gamma(\varphi_{0},\varphi_{1}). |  |

By [Sey12], for a fixed compact subset K K of T ∗ ​ N T^{*}N, there exists a constant C ′ > 0 C^{\prime}>0 such that for any φ 0, φ 1 \varphi_{0},\varphi_{1} whose supports are contained in K K,

 | γ ⁡ ( φ 0, φ 1) ≤ C ′ ​ d C 0 ​ ( φ 0, φ 1). \gamma(\varphi_{0},\varphi_{1})\leq C^{\prime}d_{C^{0}}(\varphi_{0},\varphi_{1}). |  |

By combining these results, we obtain

 | d ⁡ ( 𝒦 ⁡ ( φ 0), 𝒦 ⁡ ( φ 1)) ≤ C ′ ​ d C 0 ​ ( φ 0, φ 1) d(\mathcal{K}(\varphi_{0}),\mathcal{K}(\varphi_{1}))\leq C^{\prime}d_{C^{0}}(\varphi_{0},\varphi_{1}) |  |

for any φ 0, φ 1 \varphi_{0},\varphi_{1} whose supports are contained in K K. Since 𝒯 ⁡ ( T ∗ ​ N 2) \mathcal{T}(T^{*}N^{2}) is complete with respect to the pseudo-distance d d ( proposition 2.2), for any compact supported Hamiltonian homeomorphism φ \varphi on T ∗ ​ N T^{*}N, we obtain an object 𝒦 ⁡ ( φ) ∈ 𝒯 ⁡ ( T ∗ ​ N 2) \mathcal{K}(\varphi)\in\mathcal{T}(T^{*}N^{2}) whose microsupport is the graph of φ \varphi by proposition 2.3. If there is no confusion, we simply write 𝒦 ⁡ ( φ) ​ F \mathcal{K}(\varphi)F for 𝒦 ⁡ ( φ) ​

○

⋆ ⁡ F \mathcal{K}(\varphi)\ostar F.

###### Lemma 2.8.

Let F, G ∈ 𝒯 η ​ ( T ∗ ​ N) F,G\in\mathcal{T}^{\eta}(T^{*}N) and φ \varphi be a Hamiltonian homeomorphism with compact support on T ∗ ​ N T^{*}N. Then, one has

 | q ∗ ​ ℋ ​ o ​ m ⋆ ⁡ ( 𝒦 ⁡ ( φ) ​ F, 𝒦 ⁡ ( φ) ​ G) ≃ q ∗ ​ ℋ ​ o ​ m ⋆ ⁡ ( F, G) q_{*}\mathop{{\mathcal{H}}om}\nolimits^{\star}(\mathcal{K}(\varphi)F,\mathcal{K}(\varphi)G)\simeq q_{*}\mathop{{\mathcal{H}}om}\nolimits^{\star}(F,G) |  |

###### Proof.

Under the identification 𝒯 η ​ ( T ∗ ​ N) ≃ Sh ⁡ ( N; 𝒯 η) \mathcal{T}^{\eta}(T^{*}N)\simeq\operatorname{\mathrm{Sh}}(N;\mathcal{T}^{\eta}), q ∗ ℋ ​ o ​ m ⋆ q_{*}\mathop{{\mathcal{H}}om}\nolimits^{\star} is the 𝒯 η \mathcal{T}^{\eta} -enriched hom space. Then the result follows since 𝒦 ⁡ ( φ) ​

○

⋆ ⁡ ( −) \mathcal{K}(\varphi)\ostar(\mathchar 45) is a 𝒯 η \mathcal{T}^{\eta} -linear equivalence. ∎

## 3 Sheaf quantization associated with Jordan curves

In what follows, until the end of this paper, we set M = ℝ x M=\mathbb{R}_{x}.

### 3.1 Sheaves associated with the torus

In [AI23], the authors constructed small sheaf quantizations for a class of rational Lagrangian immersions following the idea of Guillermou [Gui12, Gui23]. Here, we apply the sheaf quantization method to the standard unit circle C 0 C_{0} in T ∗ ​ ℝ x ≃ ℝ 2 T^{*}\mathbb{R}_{x}\simeq\mathbb{R}^{2} in a more sophisticated way. The outcome can be seen as a sheaf quantization of C 0 × C 0 C_{0}\times C_{0} in T ∗ ​ ℝ 2 = T ∗ ​ ( ℝ x 1 × ℝ x 2) T^{*}\mathbb{R}^{2}=T^{*}(\mathbb{R}_{x_{1}}\times\mathbb{R}_{x_{2}}). In particular, instead of the orbit category, we use the category of twisted sheaves, which was introduced in the previous section. This can be done because of the monotonicity of Lagrangian submanifolds that we will handle.

The idea to construct a sheaf quantization of C 0 × C 0 C_{0}\times C_{0} as a sheaf on M × M × ℝ t / π ​ ℤ M\times M\times\mathbb{R}_{t}/\pi\mathbb{Z} without another extra ℝ \mathbb{R} -factor is due to Stéphane Guillermou. This makes all the computation much easier.

Set L = C 0 L=C_{0} to be the standard circle with center ( 0, 0) (0,0) and radius 1 1. Since the space of 1-jet J 1 ​ ( M) = T ∗ ​ M × ℝ t J^{1}(M)=T^{*}M\times\mathbb{R}_{t} has a natural contact structure that is invariant with respect to the translation in the ℝ t \mathbb{R}_{t} -direction, the quotient T ∗ ​ M × ℝ t / π ​ ℤ T^{*}M\times\mathbb{R}_{t}/\pi\mathbb{Z} inherits a natural contact structure. We define a primitive of C 0 C_{0} valued in ℝ / π ​ ℤ \mathbb{R}/\pi\mathbb{Z} by f 0 ​ ( s) ≔ 1 2 ​ s − 1 4 ​ sin ⁡ 2 ​ s f_{0}(s)\coloneqq\frac{1}{2}s-\frac{1}{4}\sin 2s. We take a Legendrian lift L ~ \widetilde{L} in T ∗ ​ M × ℝ t / π ​ ℤ T^{*}M\times\mathbb{R}_{t}/\pi\mathbb{Z} of L = C 0 L=C_{0} as follows:

 | L ~ = { ( ( cos ⁡ s; sin ⁡ s), − f 0 ​ ( s)) ∈ T ∗ ​ M × ℝ t / π ​ ℤ | s ∈ ℝ / 2 ​ π ​ ℤ }. \widetilde{L}=\left\{\left((\cos s;\sin s),-f_{0}(s)\right)\in T^{*}M\times\mathbb{R}_{t}/\pi\mathbb{Z}\mathrel{}\middle|\mathrel{}s\in\mathbb{R}/2\pi\mathbb{Z}\right\}. |  |

We also define a Legendrian lift Λ ⊂ T ∗ ​ M × T ∗ ​ M × ℝ t / π ​ ℤ \Lambda\subset T^{*}M\times T^{*}M\times\mathbb{R}_{t}/\pi\mathbb{Z} of L × L ⊂ T ∗ ​ M 2 L\times L\subset T^{*}M^{2} by

 | Λ = { ( ( cos s 1; sin s 1), ( cos s 2; sin s 2), − f 0 ( s 1) − f 0 ( s 2)) ∣ s 1, s 2 ∈ ℝ t / 2 π ℤ }. \Lambda=\{((\cos s_{1};\sin s_{1}),(\cos s_{2};\sin s_{2}),-f_{0}(s_{1})-f_{0}(s_{2}))\mid s_{1},s_{2}\in\mathbb{R}_{t}/2\pi\mathbb{Z}\}. |  | (3.1) |

We identify T ∗ ​ M × ℝ t / π ​ ℤ T^{*}M\times\mathbb{R}_{t}/\pi\mathbb{Z} with the subset { τ = 1 } \{\tau=1\} in T ∗ ​ ( M × ℝ / π ​ ℤ) T^{*}(M\times\mathbb{R}/\pi\mathbb{Z}) as contact manifolds.

Below we will prove the following.

###### Proposition 3.1.

There exists a simple object F C 0 ∈ 𝒯 η ​ ( T ∗ ​ M 2) F_{C_{0}}\in\mathcal{T}^{\eta}(T^{*}M^{2}) such that SS ∙ ⁡ ( F C 0) = Λ \DMS(F_{C_{0}})=\Lambda and such an object is unique up to degree shift. Moreover, Hom ⁡ ( F C 0, F C 0) ≃ H ∗ ​ ( S 1) \operatorname{Hom}(F_{C_{0}},F_{C_{0}})\simeq H^{*}(S^{1}).

We can define the Kashiwara–Schapira stack μ ​ sh L ~ \mush_{\widetilde{L}} on L ~ \widetilde{L}, which is regarded as a subset of { τ = 1 } ⊂ T ∗ ( M × ℝ t / π ℤ) \{\tau=1\}\subset T^{*}(M\times\mathbb{R}_{t}/\pi\mathbb{Z}). This stack is locally isomorphic to the stack of local systems, but globally it is twisted. In our setting, this twisting is the delooping of ℤ → Pic ⁡ ( 𝐤): 1 ↦ 𝐤 ⁡ [2] \mathbb{Z}\to\operatorname{Pic}(\mathbf{k})\colon 1\mapsto\mathbf{k}[2], which corresponds to the first Maslov class of L L. We write η − 1 \eta^{-1} for the twisting L → B ​ Pic ⁡ ( 𝐤) L\to B\operatorname{Pic}(\mathbf{k}) and write η \eta for its inverse. Then we have an isomorphism of stacks μ ​ sh L ~ ≃ Loc L ~ η − 1 \mush_{\widetilde{L}}\simeq\Loc_{\widetilde{L}}^{\eta^{-1}}, where the right-hand side denotes the stack of local systems with twisting η − 1 \eta^{-1}. By twisting, we have an isomorphism μ ​ sh L ~ η ≃ Loc L ~ \mush_{\widetilde{L}}^{\eta}\simeq\Loc_{\widetilde{L}}, which has a global object.

###### Remark 3.2.

As explained in [JT17], the twisting η − 1: L → B ​ Pic ⁡ ( 𝐤) \eta^{-1}\colon L\to B\operatorname{Pic}(\mathbf{k}) is described as the composite of the Gauss map, (the delooping of) the J J -homomorphism, and the morphism induced by the unit morphism 𝕊 → H ​ 𝐤 \mathbb{S}\to H\mathbf{k}, where 𝕊 \mathbb{S} denotes the sphere spectrum and H ​ 𝐤 H\mathbf{k} denotes the Eilenberg–MacLane spectrum. In order to get the above isomorphism, we need to choose a homotopy between L → U / O → B ​ Pic ⁡ ( 𝕊) → B ​ Pic ⁡ ( 𝐤) L\to U/O\to B\operatorname{Pic}(\mathbb{S})\to B\operatorname{Pic}(\mathbf{k}) and η − 1 \eta^{-1}. The connected components of the space of such homotopies forms a ℤ \mathbb{Z} -torsor, and each component is contractible. We can freely choose a connected component for the following argument. The differences of the choices affect as overall degree shifts.

The twisting η: L ~ ≃ L → B ​ Pic ⁡ ( 𝐤) \eta\colon\widetilde{L}\simeq L\to B\operatorname{Pic}(\mathbf{k}) factors through the base space M × ℝ t / π ​ ℤ M\times\mathbb{R}_{t}/\pi\mathbb{Z}. Since the projection π: L ~ → M × ℝ t / π ​ ℤ \pi\colon\widetilde{L}\to M\times\mathbb{R}_{t}/\pi\mathbb{Z} is of finite position, we can apply the doubling method (with cusp doubling, which is used in [NS20, GPS24, IK23]) by Guillermou to obtain a morphism of stacks on M × ℝ t / π ​ ℤ M\times\mathbb{R}_{t}/\pi\mathbb{Z}:

 | π ∗ ​ μ ​ sh L ~ η → Sh Λ η ⁡ ( ( −) × ( − 1, − 1 + ε)) \pi_{*}\mush^{\eta}_{\widetilde{L}}\to\operatorname{\mathrm{Sh}}^{\eta}_{\Lambda}((\mathchar 45)\times(-1,-1+\varepsilon)) |  |

for sufficiently small ε > 0 \varepsilon>0. Here, the right-hand side denotes the stack defined as U ↦ Sh Λ ∩ T ∗ ​ ( U × ( − 1, − 1 + ε)) η ⁡ ( U × ( − 1, − 1 + ε)) U\mapsto\operatorname{\mathrm{Sh}}^{\eta}_{\Lambda\cap T^{*}(U\times(-1,-1+\varepsilon))}(U\times(-1,-1+\varepsilon)) for an open subset U U of M × ℝ t / π ​ ℤ M\times\mathbb{R}_{t}/\pi\mathbb{Z}.

For x ∈ ( − 1, 1) x\in(-1,1), the set Λ x ≔ π ξ 2 ( Λ ∩ { x 2 = x }) ⊂ T ∗ M × ℝ t / π ℤ \Lambda_{x}\coloneqq\pi_{\xi_{2}}(\Lambda\cap\{x_{2}=x\})\subset T^{*}M\times\mathbb{R}_{t}/\pi\mathbb{Z} consists of the two copies of L ~ \widetilde{L} shifted to the ℝ t \mathbb{R}_{t} -direction. There exists a contact isotopy ( ψ x) x ∈ ( − 1, 1) (\psi_{x})_{x\in(-1,1)} on T ∗ ​ M × ℝ t / π ​ ℤ T^{*}M\times\mathbb{R}_{t}/\pi\mathbb{Z} such that ψ 0 = id \psi_{0}=\operatorname{id} and ψ x ​ ( Λ 0) = Λ x \psi_{x}(\Lambda_{0})=\Lambda_{x}. By applying the GKS kernels associated with the contact isotopy, we obtain an isomorphism

 | Sh Λ η ⁡ ( M × ℝ t / π ​ ℤ × ( − 1, − 1 + ε)) ≃ Sh Λ η ⁡ ( M × ℝ t / π ​ ℤ × ( − 1, 1)). \operatorname{\mathrm{Sh}}^{\eta}_{\Lambda}(M\times\mathbb{R}_{t}/\pi\mathbb{Z}\times(-1,-1+\varepsilon))\simeq\operatorname{\mathrm{Sh}}^{\eta}_{\Lambda}(M\times\mathbb{R}_{t}/\pi\mathbb{Z}\times(-1,1)). |  |

Let ℒ \mathcal{L} be a global object of Loc L \Loc_{L}. By sending ℒ \mathcal{L} through the identification μ ​ sh L ~ η ≃ Loc L ~ \mush_{\widetilde{L}}^{\eta}\simeq\Loc_{\widetilde{L}} and the morphism above, we obtain a sheaf quantization G ℒ, C 0 ∈ Sh η ⁡ ( M × ℝ t / π ​ ℤ × ( − 1, 1)) G_{\mathcal{L},C_{0}}\in\operatorname{\mathrm{Sh}}^{\eta}(M\times\mathbb{R}_{t}/\pi\mathbb{Z}\times(-1,1)). Denote by j: ( − 1, 1) ↪ M = ℝ x 2 j\colon(-1,1)\hookrightarrow M=\mathbb{R}_{x_{2}} the inclusion and also write j j for the base change M × ℝ t / π ​ ℤ × ( − 1, 1) → M × M × ℝ t / π ​ ℤ M\times\mathbb{R}_{t}/\pi\mathbb{Z}\times(-1,1)\to M\times M\times\mathbb{R}_{t}/\pi\mathbb{Z}. By pushing forward under j j, we obtain an object F ℒ, C 0 ≔ j! G ℒ, C 0 F_{\mathcal{L},C_{0}}\coloneqq j_{!}G_{\mathcal{L},C_{0}}.

###### Lemma 3.3.

One has j! G ℒ, C 0 ≃ j ∗ G ℒ, C 0 j_{!}G_{\mathcal{L},C_{0}}\simeq j_{*}G_{\mathcal{L},C_{0}}, and they are objects of 𝒯 Λ η ​ ( T ∗ ​ M 2) \mathcal{T}^{\eta}_{\Lambda}(T^{*}M^{2}).

###### Proof.

By the construction j ∗ G ℒ, C 0 | { x 2 = − 1 } j_{*}G_{\mathcal{L},C_{0}}|_{\{x_{2}=-1\}} is 0 0. Let i i be the inclusion M × { 1 } × ℝ t / π ​ ℤ → M 2 × ℝ t / π ​ ℤ M\times\{1\}\times\mathbb{R}_{t}/\pi\mathbb{Z}\to M^{2}\times\mathbb{R}_{t}/\pi\mathbb{Z}. There is a cofiber sequence j! G ℒ, C 0 → j ∗ G ℒ, C 0 → i ∗ i ∗ j ∗ G ℒ, C 0 j_{!}G_{\mathcal{L},C_{0}}\to j_{*}G_{\mathcal{L},C_{0}}\to i_{*}i^{*}j_{*}G_{\mathcal{L},C_{0}}. The (conic) microsupport estimates shows SS ⁡ ( i ∗ ​ j ∗ ​ G ℒ, C 0) ⊂ T π 2 ​ L ~ \CMS(i^{*}j_{*}G_{\mathcal{L},C_{0}})\subset T_{\frac{\pi}{2}}\widetilde{L}, and hence a similar estimate for SS ( ℓ! i ∗ j ∗ G ℒ, C 0) \CMS(\ell^{!}i^{*}j_{*}G_{\mathcal{L},C_{0}}) holds since ℓ \ell is a submersion. By [STZ17, Proposition 5.8], ℓ! i ∗ j ∗ G ℒ, C 0 \ell^{!}i^{*}j_{*}G_{\mathcal{L},C_{0}} must be a local system and becomes 0 0 in 𝒯 ⁡ ( T ∗ ​ M) \mathcal{T}(T^{*}M). Since ℓ! \ell^{!} is conservative, i ∗ ​ j ∗ ​ G ℒ, C 0 i^{*}j_{*}G_{\mathcal{L},C_{0}} is also 0 0. By estimating the both sides of SS ( j! G ℒ, C 0) = SS ( j ∗ G ℒ, C 0) \CMS(j_{!}G_{\mathcal{L},C_{0}})=\CMS(j_{*}G_{\mathcal{L},C_{0}}), we find that F ℒ, C 0 ∈ 𝒯 Λ η ​ ( T ∗ ​ M 2) F_{\mathcal{L},C_{0}}\in\mathcal{T}^{\eta}_{\Lambda}(T^{*}M^{2}). ∎

We set F C 0 ≔ F 𝐤 ¯, C 0 F_{C_{0}}\coloneqq F_{\underline{\mathbf{k}},C_{0}}, where 𝐤 ¯ \underline{\mathbf{k}} denotes the trivial local system of rank 1 1 on L L.

###### Lemma 3.4.

The functor Loc L ~ ⁡ ( L ~) → 𝒯 Λ η ​ ( T ∗ ​ M 2) \Loc_{\widetilde{L}}(\widetilde{L})\to\mathcal{T}^{\eta}_{\Lambda}(T^{*}M^{2}) is fully faithful.

###### Proof.

By [NS20], the functor Loc L ~ ⁡ ( L ~) → Sh Λ η ⁡ ( M × ℝ t / π ​ ℤ × ( − 1, − 1 + ε)) \Loc_{\widetilde{L}}(\widetilde{L})\to\operatorname{\mathrm{Sh}}^{\eta}_{\Lambda}(M\times\mathbb{R}_{t}/\pi\mathbb{Z}\times(-1,-1+\varepsilon)) is fully faithful. As the composite, the functor Loc L ~ ⁡ ( L ~) → Sh Λ η ⁡ ( M × ℝ t / π ​ ℤ × ( − 1, 1)) \Loc_{\widetilde{L}}(\widetilde{L})\to\operatorname{\mathrm{Sh}}^{\eta}_{\Lambda}(M\times\mathbb{R}_{t}/\pi\mathbb{Z}\times(-1,1)) is also fully faithful. One can check that the image of the functor is in 𝒯 η ​ ( T ∗ ​ N) \mathcal{T}^{\eta}(T^{*}N), which is regarded as a subcategory of Sh η ⁡ ( N × ℝ t / π ​ ℤ) \operatorname{\mathrm{Sh}}^{\eta}(N\times\mathbb{R}_{t}/\pi\mathbb{Z}). Since End ( j! G) ≃ Hom ( G, j! j! G) ≃ End ( G) \operatorname{End}(j_{!}G)\simeq\operatorname{Hom}(G,j^{!}j_{!}G)\simeq\operatorname{End}(G), the functor j! j_{!} is also fully faithful. By combining these, we obtain the result. ∎

By lemma 3.4, we have

 | Hom 𝒯 η ​ ( T ∗ ​ M 2) ⁡ ( F C 0, F C 0) ≃ Hom Loc L ⁡ ( 𝐤 ¯, 𝐤 ¯) ≃ H ∗ ​ ( S 1), \operatorname{Hom}_{\mathcal{T}^{\eta}(T^{*}M^{2})}(F_{C_{0}},F_{C_{0}})\simeq\operatorname{Hom}_{\Loc_{L}}(\underline{\mathbf{k}},\underline{\mathbf{k}})\simeq H^{*}(S^{1}), |  |

where 𝐤 ¯ \underline{\mathbf{k}} denotes the trivial local system of rank 1 1 on L L.

We shall prove the uniqueness by decomposing the sheaf into easier pieces. A similar argument can be found in [Gui23, Part VI].

###### Lemma 3.5.

Simple objects in 𝒯 Λ η ​ ( T ∗ ​ M 2) \mathcal{T}^{\eta}_{\Lambda}(T^{*}M^{2}) are unique up to shift.

###### Proof.

Let us first observe the image of the projection Λ → M 2 × ℝ t / π ​ ℤ \Lambda\to M^{2}\times\mathbb{R}_{t}/\pi\mathbb{Z}. The immersed locus is given by

 | ( ( cos ± s, sin ± s), ( cos ∓ s, sin ∓ s), − f 0 ​ ( ± s) − f 0 ​ ( ∓ s)) ↦ ( cos ⁡ s, cos ⁡ s, 0) ((\cos\pm s;\sin\pm s),(\cos\mp s,\sin\mp s),-f_{0}(\pm s)-f_{0}(\mp s))\mapsto(\cos s,\cos s,0) |  |

and

 | ( ( cos ± s, sin ± s), ( cos ⁡ π ∓ s, sin ⁡ π ∓ s), − f 0 ​ ( ± s) − f 0 ​ ( π ∓ s)) ↦ ( cos ⁡ s, − cos ⁡ s, π 2). ((\cos\pm s;\sin\pm s),(\cos\pi\mp s,\sin\pi\mp s),-f_{0}(\pm s)-f_{0}(\pi\mp s))\mapsto(\cos s,-\cos s,\frac{\pi}{2}). |  |

We take t 0, t 3 t_{0},t_{3} in remark 2.6 so that − π / 2 < t 0 < t 3 − π < 0 -\pi/2<t_{0}<t_{3}-\pi<0. We note that ℓ ⁡ ( (,,,)) \ell((t_{0},t_{3}-\pi)) does not contain 0 0 nor π 2 \frac{\pi}{2}.

We will see that simple sheaves on M 2 × ( t 0, t 3) M^{2}\times(t_{0},t_{3}) with SS ∙ ⊂ ℓ − 1 ​ ( Λ) ∩ T ∗ ​ M 2 × ( t 0, t 3) \DMS\subset\ell^{-1}(\Lambda)\cap T^{*}M^{2}\times(t_{0},t_{3}) that corresponds to an object of 𝒯 η ​ ( T ∗ ​ M 2) \mathcal{T}^{\eta}(T^{*}M^{2}) are unique up to shift. Let F ∈ Sh ⁡ ( M 2 × ( t 0, t 3)) F\in\operatorname{\mathrm{Sh}}(M^{2}\times(t_{0},t_{3})) be such a sheaf. The support of F F on M 2 × ( t 0, t 3) M^{2}\times(t_{0},t_{3}) is bounded since F F corresponds to an object in 𝒯 Λ η ​ ( T ∗ ​ M 2) \mathcal{T}^{\eta}_{\Lambda}(T^{*}M^{2}), which implies that the support is the union of the closures of three bounded regions. We write F F as an extension of F ( t 0, 0), F [0, π / 2) F_{(t_{0},0)},F_{[0,\pi/2)} and F [π / 2, t 3) F_{[\pi/2,t_{3})}. Each of F ( t 0, 0), F [0, π / 2), F [π / 2, t 3) F_{(t_{0},0)},F_{[0,\pi/2)},F_{[\pi/2,t_{3})} is unique up to shift by the microsupport condition. The non-trivial extension class is also unique.

The choice of an isomorphism α: F ( t 0, t 3 − π) ​ [− 2] → ∼ T − π ​ F ( t 0 + π, t 3) \alpha\colon F_{(t_{0},t_{3}-\pi)}[-2]\xrightarrow{\sim}T_{-\pi}F_{(t_{0}+\pi,t_{3})} is also unique. This proves the lemma. ∎

This completes the proof of proposition 3.1.

###### Remark 3.6.

The existence of sheaf quantization F C 0 F_{C_{0}} of C 0 × C 0 ⊂ T ∗ ​ M 2 C_{0}\times C_{0}\subset T^{*}M^{2} in the category 𝒯 η ​ ( T ∗ ​ M 2) \mathcal{T}^{\eta}(T^{*}M^{2}) would be related to the fact that C 0 × C 0 C_{0}\times C_{0} admits a bounding cochain [FOOO09]. In contrast, C 0 ⊂ T ∗ ​ ℝ C_{0}\subset T^{*}\mathbb{R} does not admit a bounding cochain and is unobstructed only modulo T π T^{\pi} in the sense of [FOOO09], which would be why one can only construct a sheaf quantization of C 0 C_{0} in Sh ⁡ ( M × ( 0, π) × ℝ t / π ​ ℤ) \operatorname{\mathrm{Sh}}(M\times(0,\pi)\times\mathbb{R}_{t}/\pi\mathbb{Z}) with the doubling parameter (cf. [AI23]).

###### Corollary 3.7.

The natural morphism F C 0 → T π ​ F C 0 F_{C_{0}}\to T_{\pi}F_{C_{0}} induced by the natural transformation id = T 0 ⇒ T π \operatorname{id}=T_{0}\Rightarrow T_{\pi} is zero.

###### Proof.

Since

 | Hom ⁡ ( F C 0, T π ​ F C 0) ≃ End ⁡ ( F C 0) ​ [2] ≃ H ∗ ​ ( S 1) ​ [2], \operatorname{Hom}(F_{C_{0}},T_{\pi}F_{C_{0}})\simeq\operatorname{End}(F_{C_{0}})[2]\simeq H^{*}(S^{1})[2], |  |

we have H 0 ​ ( Hom ⁡ ( F C 0, T π ​ F C 0)) = 0 H^{0}(\operatorname{Hom}(F_{C_{0}},T_{\pi}F_{C_{0}}))=0. ∎

We shall describe the morphism

 | H ∗ ( C 0) ≃ Hom ( F C 0, F C 0) → Γ ( { τ > 0 }; μ h o m ( F C 0, F C 0)) ≃ H ∗ ( C 0 × C 0). H^{*}(C_{0})\simeq\operatorname{Hom}(F_{C_{0}},F_{C_{0}})\\ \to\Gamma(\{\tau>0\};\mu hom(F_{C_{0}},F_{C_{0}}))\simeq H^{*}(C_{0}\times C_{0}). |  | (3.2) |

The generator v ∈ H 1 ​ ( C 0) v\in H^{1}(C_{0}) is sent to v ⊗ 1 + 1 ⊗ v ∈ H 1 ​ ( C 0 × C 0) v\otimes 1+1\otimes v\in H^{1}(C_{0}\times C_{0}). Indeed, we find that the coefficient of v ⊗ 1 v\otimes 1 is non-trivial by construction, and that of 1 ⊗ v 1\otimes v by symmetry with respect to ( z 1, z 2) ↦ ( z 2, z 1) (z_{1},z_{2})\mapsto(z_{2},z_{1}).

Let ϕ \phi be a Hamiltonian diffeomorphism with compact support on T ∗ ​ M T^{*}M, and denote by 𝒦 ⁡ ( ϕ × ϕ) ∈ 𝒯 ⁡ ( T ∗ ​ M 4) \mathcal{K}(\phi\times\phi)\in\mathcal{T}(T^{*}M^{4}) the sheaf quantization of ϕ × ϕ \phi\times\phi. Then the composition with 𝒦 ⁡ ( ϕ × ϕ) \mathcal{K}(\phi\times\phi) induces a 𝒯 η \mathcal{T}^{\eta} -linear autoequivalence of the category 𝒯 η ​ ( T ∗ ​ M 2) \mathcal{T}^{\eta}(T^{*}M^{2}). Moreover, we have MS ⁡ ( 𝒦 ⁡ ( ϕ × ϕ) ​ F) = ( ϕ × ϕ) ​ ( MS ⁡ ( F)) \MS(\mathcal{K}(\phi\times\phi)F)=(\phi\times\phi)(\MS(F)) for any F ∈ 𝒯 η ​ ( T ∗ ​ M 2) F\in\mathcal{T}^{\eta}(T^{*}M^{2}). Thus, F C = 𝒦 ⁡ ( ϕ × ϕ) ​ F C 0 F_{C}=\mathcal{K}(\phi\times\phi)F_{C_{0}} is a sheaf quantization for C × C = ( ϕ × ϕ) ​ ( C 0 × C 0) C\times C=(\phi\times\phi)(C_{0}\times C_{0}).

### 3.2 Action of R θ R_{\theta}

Now we consider the action of R θ R_{\theta} defined in ( 1.1) on 𝒯 η ​ ( T ∗ ​ M 2) \mathcal{T}^{\eta}(T^{*}M^{2}). The Hamiltonian function of R θ R_{\theta} is the non-negative function H: T ∗ ​ M 2 ≃ ℂ 2 H\colon T^{*}M^{2}\simeq\mathbb{C}^{2} defined as H ⁡ ( z 1, z 2) = | z 1 − z 2 | 2 / 4 H(z_{1},z_{2})=|z_{1}-z_{2}|^{2}/4. Hence, we can construct an object 𝒦 ​ ( ϕ H) θ ∈ 𝒯 ⁡ ( T ∗ ​ M 2) \mathcal{K}(\phi^{H})_{\theta}\in\mathcal{T}(T^{*}M^{2}) for any θ \theta. By [GKS12], we have continuation morphisms 𝒦 ​ ( ϕ H) θ → 𝒦 ​ ( ϕ H) θ ′ ​ ( θ ≤ θ ′) \mathcal{K}(\phi^{H})_{\theta}\to\mathcal{K}(\phi^{H})_{\theta^{\prime}}\ (\theta\leq\theta^{\prime}). By abuse of notation, we also write R θ R_{\theta} for 𝒦 ​ ( ϕ H) θ ​

○

⋆ ⁡ ( −) \mathcal{K}(\phi^{H})_{\theta}\ostar(\mathchar 45), the automorphism on 𝒯 η ​ ( T ∗ ​ M 2) \mathcal{T}^{\eta}(T^{*}M^{2}).

The Hamiltonian function H H which generates the Hamiltonian isotopy ( R θ) θ (R_{\theta})_{\theta} also defines a contact isotopy R ~ = ( R ~ θ) θ \widetilde{R}=(\widetilde{R}_{\theta})_{\theta} on { τ = 1 } \{\tau=1\}. This isotopy R ~ = ( R ~ θ) θ \widetilde{R}=(\widetilde{R}_{\theta})_{\theta} is the product of ( R θ) θ (R_{\theta})_{\theta} and the identity morphism of ℝ t / π ​ ℤ \mathbb{R}_{t}/\pi\mathbb{Z}.

###### Lemma 3.8.

There is an isomorphism 𝒦 ​ ( ϕ H) 2 ​ π ≃ 𝐤 Δ × [0, ∞) ​ [2] \mathcal{K}(\phi^{H})_{2\pi}\simeq\mathbf{k}_{\Delta\times[0,\infty)}[2]. Hence, the functor R 2 ​ π R_{2\pi} on 𝒯 η ​ ( T ∗ ​ M 2) \mathcal{T}^{\eta}(T^{*}M^{2}) coincides with the degree shift [2] [2].

###### Proof.

First we have the (conic) microsupport estimate SS ⁡ ( 𝒦 ​ ( ϕ H) 2 ​ π) = SS ⁡ ( 𝐤 Δ × [0, ∞)) \CMS(\mathcal{K}(\phi^{H})_{2\pi})=\CMS(\mathbf{k}_{\Delta\times[0,\infty)}). Moreover, 𝒦 ​ ( ϕ H) 2 ​ π \mathcal{K}(\phi^{H})_{2\pi} is simple along its conic microsupport. Since 𝐤 = 𝔽 2 \mathbf{k}=\mathbb{F}_{2}, we obtain 𝒦 ​ ( ϕ H) 2 ​ π ≃ 𝐤 Δ × [0, ∞) ​ [d] \mathcal{K}(\phi^{H})_{2\pi}\simeq\mathbf{k}_{\Delta\times[0,\infty)}[d] for some d ∈ ℤ d\in\mathbb{Z}. We can observe the grading by tracing the action on the fiberwise universal covering space of the Lagrangian Grassmannian bundle of T ∗ ​ M 2 T^{*}M^{2} as in [Sei00]. ∎

###### Remark 3.9.

For our purpose, it is enough to cut off the support of H H outside a sufficiently large compact subset. Then we only need sheaf quantization of Hamiltonian isotopies with compact support. From this position, the statement of lemma 3.8 should be understood as that the action of R 2 ​ π R_{2\pi} on the objects whose microsupports are contained in the compact subset coincides with the degree shift [2] [2].

We can also determine R π ​ F C 0 R_{\pi}F_{C_{0}} as follows.

###### Lemma 3.10.

One has an isomorphism

 | R π ​ F C 0 ≃ F C 0 ​ [1]. R_{\pi}F_{C_{0}}\simeq F_{C_{0}}[1]. |  |

###### Proof.

Since SS ⁡ ( R π ​ F C 0) = Λ \CMS(R_{\pi}F_{C_{0}})=\Lambda, by the uniqueness in proposition 3.1, we have R π ​ F C 0 ≃ F C 0 ​ [d] R_{\pi}F_{C_{0}}\simeq F_{C_{0}}[d] for some d ∈ ℤ d\in\mathbb{Z}. Then, by lemma 3.8,

 | F C 0 ​ [2] ≃ R 2 ​ π ​ F C 0 ≃ R π ​ F C 0 ​ [d] ≃ F C 0 ​ [2 ​ d], F_{C_{0}}[2]\simeq R_{2\pi}F_{C_{0}}\simeq R_{\pi}F_{C_{0}}[d]\simeq F_{C_{0}}[2d], |  |

which concludes d = 1 d=1. ∎

### 3.3 Computation for the standard circle

Let F C 0 ∈ 𝒯 η ​ ( T ∗ ​ M 2) F_{C_{0}}\in\mathcal{T}^{\eta}(T^{*}M^{2}) be the sheaf quantization of the standard torus C 0 × C 0 C_{0}\times C_{0} constructed in proposition 3.1. We define

 | 𝒱 C 0, θ ≔ ℓ! q ∗ ℋ ​ o ​ m ⋆ ( F C 0, R θ F C 0) ∈ 𝒯 ( pt), \mathcal{V}_{C_{0},\theta}\coloneqq\ell^{!}q_{*}\mathop{{\mathcal{H}}om}\nolimits^{\star}(F_{C_{0}},R_{\theta}F_{C_{0}})\in\mathcal{T}(\mathrm{pt}), |  |

where q: M 2 × ℝ t / π ​ ℤ → ℝ t / π ​ ℤ q\colon M^{2}\times\mathbb{R}_{t}/\pi\mathbb{Z}\to\mathbb{R}_{t}/\pi\mathbb{Z} and ℓ: ℝ t → ℝ t / π ​ ℤ \ell\colon\mathbb{R}_{t}\to\mathbb{R}_{t}/\pi\mathbb{Z} are the projection and the quotient map. It is also convenient to consider the family version

 | 𝒱 C 0 ≔ ( ℓ × id [0, π])! ( q × id [0, π]) ∗ ℋ ​ o ​ m ⋆ ( q ′ ⁣ ∗ F C 0, R F C 0) ∈ Sh ( [0, π]; 𝒯 ( pt)), \mathcal{V}_{C_{0}}\coloneqq(\ell\times\operatorname{id}_{[0,\pi]})^{!}(q\times\operatorname{id}_{[0,\pi]})_{*}\mathop{{\mathcal{H}}om}\nolimits^{\star}(q^{\prime*}F_{C_{0}},RF_{C_{0}})\in\operatorname{\mathrm{Sh}}([0,\pi];\mathcal{T}(\mathrm{pt})), |  |

where R R is the GKS kernel for the (full) Hamiltonian isotopy ( R θ) θ ∈ [0, π] (R_{\theta})_{\theta\in[0,\pi]} and q ′: M 2 × ℝ t / π ​ ℤ × [0, π] → M 2 × ℝ t / π ​ ℤ q^{\prime}\colon M^{2}\times\mathbb{R}_{t}/\pi\mathbb{Z}\times[0,\pi]\to M^{2}\times\mathbb{R}_{t}/\pi\mathbb{Z} is the projection. For θ 0 ∈ [0, π] \theta_{0}\in[0,\pi], we have an isomorphism 𝒱 C 0 | { θ = θ 0 } ≃ 𝒱 C 0, θ 0 \mathcal{V}_{C_{0}}|_{\{\theta=\theta_{0}\}}\simeq\mathcal{V}_{C_{0},\theta_{0}}.

For each θ ∈ ( 0, π) \theta\in(0,\pi) and a ∈ [− π, 0] a\in[-\pi,0], we can directly check that

 | T − a ​ R ~ θ ​ ( Λ) ∩ Λ = { { ( ( cos ⁡ s; sin ⁡ s), ( cos ⁡ s; sin ⁡ s), − 2 ​ f 0 ​ ( s)) | s ∈ ℝ / 2 ​ π ​ ℤ } ( a = 0) { ( ( cos ⁡ s; sin ⁡ s), ( − cos ⁡ s, − sin ⁡ s), − 2 ​ f 0 ​ ( s) − π 2) | s ∈ ℝ / 2 ​ π ​ ℤ } ( a = − θ) ∅ ( otherwise). T_{-a}\widetilde{R}_{\theta}(\Lambda)\cap\Lambda=\begin{cases}\left\{((\cos s;\sin s),(\cos s;\sin s),-2f_{0}(s))\mathrel{}\middle|\mathrel{}s\in\mathbb{R}/2\pi\mathbb{Z}\right\}&(a=0)\\ \left\{((\cos s;\sin s),(-\cos s;-\sin s),-2f_{0}(s)-\frac{\pi}{2})\mathrel{}\middle|\mathrel{}s\in\mathbb{R}/2\pi\mathbb{Z}\right\}&(a=-\theta)\\ \varnothing&(\text{otherwise}).\end{cases} |  |

Decompose the strip ℝ × [0, π] \mathbb{R}\times[0,\pi] into locally closed isosceles right triangles as follows:

 | △ n \displaystyle\vartriangle_{n} | ≔ { ( t, θ) ∣ n ​ π ≤ t < n ​ π + θ }, \displaystyle\coloneqq\{(t,\theta)\mid n\pi\leq t<n\pi+\theta\}, |  |

 | ▽ n \displaystyle\triangledown_{n} | ≔ { ( t, θ) ∣ ( n − 1) ​ π + θ ≤ t < n ​ π }. \displaystyle\coloneqq\{(t,\theta)\mid(n-1)\pi+\theta\leq t<n\pi\}. |  |

We also set

 | △ n ′ \displaystyle\vartriangle^{\prime}_{n} | ≔ { ( t, θ) ∣ n ​ π < t ≤ n ​ π + θ }, \displaystyle\coloneqq\{(t,\theta)\mid n\pi<t\leq n\pi+\theta\}, |  |

 | ▽ n ′ \displaystyle\triangledown^{\prime}_{n} | ≔ { ( t, θ) ∣ ( n − 1) ​ π + θ < t ≤ n ​ π }. \displaystyle\coloneqq\{(t,\theta)\mid(n-1)\pi+\theta<t\leq n\pi\}. |  |

By the microlocal Morse lemma and the intersection estimate above, we obtain the following:

###### Proposition 3.11.

If ( a 0, θ 0) (a_{0},\theta_{0}) and ( a 1, θ 1) (a_{1},\theta_{1}) belong to the same component of the decomposition by △ n ′ \vartriangle^{\prime}_{n} ’s and ▽ n ′ \triangledown^{\prime}_{n} ’s, then

 | Hom ⁡ ( F C 0, T − a 0 ​ R θ 0 ​ F C 0) ≃ Hom ⁡ ( F C 0, T − a 1 ​ R θ 1 ​ F C 0) \operatorname{Hom}(F_{C_{0}},T_{-a_{0}}R_{\theta_{0}}F_{C_{0}})\simeq\operatorname{Hom}(F_{C_{0}},T_{-a_{1}}R_{\theta_{1}}F_{C_{0}}) |  |

as End ⁡ ( F C 0) \operatorname{End}(F_{C_{0}}) -modules. If ( a, θ) ∈ △ n ′ (a,\theta)\in\vartriangle^{\prime}_{n}, we have

 | Hom ⁡ ( F C 0, T − a ​ R θ ​ F C 0) ≃ Hom ⁡ ( F C 0, T − ( n + 1) ​ π ​ R π ​ F C 0) ≃ End ⁡ ( F C 0) ​ [− 2 ​ n − 1]. \operatorname{Hom}(F_{C_{0}},T_{-a}R_{\theta}F_{C_{0}})\simeq\operatorname{Hom}(F_{C_{0}},T_{-(n+1)\pi}R_{\pi}F_{C_{0}})\simeq\operatorname{End}(F_{C_{0}})[-2n-1]. |  |

If ( a, θ) ∈ ▽ n ′ (a,\theta)\in\triangledown^{\prime}_{n}, we have

 | Hom ⁡ ( F C 0, T − a ​ R θ ​ F C 0) ≃ Hom ⁡ ( F C 0, T − n ​ π ​ F C 0) ≃ End ⁡ ( F C 0) ​ [− 2 ​ n]. \operatorname{Hom}(F_{C_{0}},T_{-a}R_{\theta}F_{C_{0}})\simeq\operatorname{Hom}(F_{C_{0}},T_{-n\pi}F_{C_{0}})\simeq\operatorname{End}(F_{C_{0}})[-2n]. |  |

It is not difficult to determine the whole structure of 𝒱 C 0 \mathcal{V}_{C_{0}} and 𝒱 C 0, θ \mathcal{V}_{C_{0},\theta} as follows. We will not use the following proposition and omit the proof.

###### Proposition 3.12.

One has an isomorphism

 | 𝒱 C 0 ≃ ⨁ n ∈ ℤ 𝐤 △ n ∪ ▽ n + 1 ​ [− 2 ​ n] ⊕ ⨁ n ∈ ℤ 𝐤 △ n ∪ ▽ n ​ [− 2 ​ n + 1]. \mathcal{V}_{C_{0}}\simeq\bigoplus_{n\in\mathbb{Z}}\mathbf{k}_{\vartriangle_{n}\cup\triangledown_{n+1}}[-2n]\oplus\bigoplus_{n\in\mathbb{Z}}\mathbf{k}_{\vartriangle_{n}\cup\triangledown_{n}}[-2n+1]. |  |

For θ ∈ [0, π] \theta\in[0,\pi], one has an isomorphism

 | 𝒱 C 0, θ ≃ ⨁ n ∈ ℤ 𝐤 [n ​ π, ( n + 1) ​ π) [− 2 n] ⊕ ⨁ n ∈ ℤ 𝐤 [θ + ( n − 1) π, θ + n π) [− 2 n + 1]. \mathcal{V}_{C_{0},\theta}\simeq\bigoplus_{n\in\mathbb{Z}}\mathbf{k}_{[n\pi,(n+1)\pi)}[-2n]\oplus\bigoplus_{n\in\mathbb{Z}}\mathbf{k}_{[\theta+(n-1)\pi,\theta+n\pi)}[-2n+1]. |  |

Moreover, for any a ∈ ℝ a\in\mathbb{R}, the right action of v ∈ H 1 ​ ( S 1) v\in H^{1}(S^{1}) on the stalk ( 𝒱 θ) a (\mathcal{V}_{\theta})_{a} is non-zero.

## 4 Sheaf-theoretic condition for rectangular peg

In this section, we prove the following theorem.

###### Theorem 4.1.

Let ϕ \phi be a Hamiltonian homeomorphism with compact support. Let us consider the Jordan curve C = ϕ ⁡ ( C 0) C=\phi(C_{0}). Define F C ≔ 𝒦 ⁡ ( ϕ × ϕ) ​ F C 0 F_{C}\coloneqq\mathcal{K}(\phi\times\phi)F_{C_{0}}. If T a ​ SS ∙ ⁡ ( F C) ∩ SS ∙ ⁡ ( F C) = ∅ T_{a}\DMS(F_{C})\cap\DMS(F_{C})=\varnothing for any a ∈ ℝ ∖ π ​ ℤ a\in\mathbb{R}\setminus\pi\mathbb{Z}, then C C inscribes a θ \theta -rectangle for any θ ∈ ( 0, π) \theta\in(0,\pi).

Before starting the proof, we give its rough outline. We consider the persistence module ( Hom ⁡ ( F C, T a ​ R θ ​ F C)) a ∈ ℝ (\operatorname{Hom}(F_{C},T_{a}R_{\theta}F_{C}))_{a\in\mathbb{R}} (in the derived sense) with structure morphisms ( τ a, a ′) a ≤ a ′ (\tau_{a,a^{\prime}})_{a\leq a^{\prime}}. We focus on a “critical value” a 0 ∈ ℝ a_{0}\in\mathbb{R} such that τ a, a ′ \tau_{a,a^{\prime}} is not an isomorphism if a < a 0 < a ′ a<a_{0}<a^{\prime}. We will prove:

1. (A)

A critical value a 0 a_{0} is produced by some subset in the intersection ( C × C) ∩ R θ ​ ( C × C) (C\times C)\cap R_{\theta}(C\times C).

2. (B)

Under the assumption T a ​ SS ∙ ⁡ ( F C) ∩ SS ∙ ⁡ ( F C) = ∅ T_{a}\DMS(F_{C})\cap\DMS(F_{C})=\varnothing for any a ∈ ℝ ∖ π ​ ℤ a\in\mathbb{R}\setminus\pi\mathbb{Z}, a critical value produced by the diagonal Δ C \Delta_{C} in the sense of (A) is in π ​ ℤ \pi\mathbb{Z}.

3. (C)

There is a critical value a 0 a_{0} in ℝ ∖ π ​ ℤ \mathbb{R}\setminus\pi\mathbb{Z}.

These three assertions prove the existence of a point in ( C × C) ∩ R θ ​ ( C × C) ∖ Δ C (C\times C)\cap R_{\theta}(C\times C)\setminus\Delta_{C}, which implies the existence of a θ \theta -rectangle on C C.

By lemma 2.7, we find that the change at a ∈ ℝ a\in\mathbb{R} can be described by μ h o m ( F C, T a R θ F C) | { τ > 0 } \mu hom(F_{C},T_{a}R_{\theta}F_{C})|_{\{\tau>0\}}, which is supported in (the conification of)

 | SS ∙ ⁡ ( F C) ∩ T a ​ SS ∙ ⁡ ( R θ ​ F C) ⊂ ρ − 1 ​ ( ( C × C) ∩ R θ ​ ( C × C)). \DMS(F_{C})\cap T_{a}\DMS(R_{\theta}F_{C})\subset\rho^{-1}((C\times C)\cap R_{\theta}(C\times C)). |  |

This proves the assertions (A) as well as (B) since

 | SS ∙ ⁡ ( F C) ∩ T a ​ SS ∙ ⁡ ( R θ ​ F C) ∩ ρ − 1 ​ ( Δ C) = SS ∙ ⁡ ( F C) ∩ T a ​ SS ∙ ⁡ ( F C) ∩ ρ − 1 ​ ( Δ C) = ∅ \DMS(F_{C})\cap T_{a}\DMS(R_{\theta}F_{C})\cap\rho^{-1}(\Delta_{C})=\DMS(F_{C})\cap T_{a}\DMS(F_{C})\cap\rho^{-1}(\Delta_{C})=\varnothing |  |

for a ∈ ℝ ∖ π ​ ℤ a\in\mathbb{R}\setminus\pi\mathbb{Z}. The most technical part is the proof of the assertion (C). For that purpose, we consider the value a ⁡ ( θ, C) a(\theta,C) informally defined as

 | a ⁡ ( θ, C) = { a ∈ ℝ ≥ 0 ∣ v can be lifted to Hom ⁡ ( F C, T − a ​ R θ ​ F C) }, a(\theta,C)=\{a\in\mathbb{R}_{\geq 0}\mid\text{$v$ can be lifted to $\operatorname{Hom}(F_{C},T_{-a}R_{\theta}F_{C})$}\}, |  |

where v ∈ H 1 ​ ( End ⁡ ( F C)) ≃ H 1 ​ ( S 1) v\in H^{1}(\operatorname{End}(F_{C}))\simeq H^{1}(S^{1}) is the generator. Then − a ⁡ ( θ, C) -a(\theta,C) is a critical value, and we will prove a ⁡ ( θ, C) ∈ ( 0, π) a(\theta,C)\in(0,\pi) for any θ \theta in lemma 4.8. Most of this section is devoted to the proof of this lemma, for which we will study μ ​ h ​ o ​ m ​ ( F C, R θ ​ F C) \mu hom(F_{C},R_{\theta}F_{C}).

###### Remark 4.2.

By the arguments in this section, we will find the following. For a fixed θ ∈ ( 0, π) \theta\in(0,\pi), if there exists a critical value a 0 ∈ ℝ a_{0}\in\mathbb{R} such that

 | Γ ⁡ ( ρ − 1 ​ ( Δ C), μ ​ h ​ o ​ m ​ ( F C, T a 0 ​ R θ ​ F C) | ρ − 1 ​ ( Δ C)) ≃ 0, \Gamma(\rho^{-1}(\Delta_{C});\mu hom(F_{C},T_{a_{0}}R_{\theta}F_{C})|_{\rho^{-1}(\Delta_{C})})\simeq 0, |  |

then C C inscribes a θ \theta -rectangle. In particular, to prove the existence of a θ \theta -rectangle, it is enough to show the cohomology vanishing for a 0 = − a ⁡ ( θ, C) a_{0}=-a(\theta,C). The only reasonable case the authors know for ensuring the vanishing is the assumption for the conic microsupport in theorem 4.1.

Let us start the proof of the theorem. First note that by proposition 5.1, which will be proved in section 5, F C F_{C} is limit constructible. We define

 | 𝒱 C, θ ≔ ℓ! q ∗ ℋ ​ o ​ m ⋆ ( F C, R θ F C) ∈ 𝒯 ( pt), \mathcal{V}_{C,\theta}\coloneqq\ell^{!}q_{*}\mathop{{\mathcal{H}}om}\nolimits^{\star}(F_{C},R_{\theta}F_{C})\in\mathcal{T}(\mathrm{pt}), |  |

where q: M 2 × ℝ t / π ​ ℤ → ℝ t / π ​ ℤ q\colon M^{2}\times\mathbb{R}_{t}/\pi\mathbb{Z}\to\mathbb{R}_{t}/\pi\mathbb{Z} is the projection. This object 𝒱 C, θ \mathcal{V}_{C,\theta} is also limit constructible. We introduce the self-map on ℂ 2 \mathbb{C}^{2} by

 | R θ ϕ ≔ ( ϕ × ϕ) − 1 ​ R θ ​ ( ϕ × ϕ). R^{\phi}_{\theta}\coloneqq(\phi\times\phi)^{-1}R_{\theta}(\phi\times\phi). |  |

Note that R π ϕ = R π R^{\phi}_{\pi}=R_{\pi}. We also write R θ ϕ R^{\phi}_{\theta} for the GKS kernel 𝒦 ​ ( ϕ × ϕ)

○

⋆ − 1 ​ R θ ​ 𝒦 ​ ( ϕ × ϕ) \mathcal{K}(\phi\times\phi)^{\ostar-1}R_{\theta}\mathcal{K}(\phi\times\phi) by abuse of notation. By lemma 2.8, we have an isomorphism in 𝒯 ⁡ ( pt) \mathcal{T}(\mathrm{pt}):

 | 𝒱 C, θ ≃ ℓ! q ∗ ℋ ​ o ​ m ⋆ ( F C 0, R θ ϕ F C 0). \mathcal{V}_{C,\theta}\simeq\ell^{!}q_{*}\mathop{{\mathcal{H}}om}\nolimits^{\star}(F_{C_{0}},R^{\phi}_{\theta}F_{C_{0}}). |  |

The continuation morphism 𝒱 C, 0 → 𝒱 C, θ → 𝒱 C, π \mathcal{V}_{C,0}\to\mathcal{V}_{C,\theta}\to\mathcal{V}_{C,\pi} is compatible with the continuation morphism 𝒱 C 0, 0 → 𝒱 C 0, π \mathcal{V}_{C_{0},0}\to\mathcal{V}_{C_{0},\pi}. Since we have a homotopy between ( R θ) θ ∈ [0, π] (R_{\theta})_{\theta\in[0,\pi]} and ( R θ ϕ) θ ∈ [0, π] (R^{\phi}_{\theta})_{\theta\in[0,\pi]} relative to the boundary, we find that the continuation morphisms id → R π \operatorname{id}\to R_{\pi} and id → R π ϕ \operatorname{id}\to R^{\phi}_{\pi} are the same via the identification R π ≃ R π ϕ R_{\pi}\simeq R^{\phi}_{\pi}. Indeed, we get the result when ϕ \phi is smooth by the argument in [Kuo23, Subsection 3.1], and for a Hamiltonian homeomorphism ϕ \phi, we obtain the result by taking limits.

For a, a ′ ∈ ℝ a,a^{\prime}\in\mathbb{R} with a ≤ a ′ a\leq a^{\prime} and θ, θ ′ ∈ ℝ \theta,\theta^{\prime}\in\mathbb{R} with θ ≤ θ ′ \theta\leq\theta^{\prime}, we denote the continuation morphism by

 | τ a, a ′ θ, θ ′: T a ​ R θ ϕ ​ F C 0 → T a ′ ​ R θ ′ ϕ ​ F C 0. \tau_{a,a^{\prime}}^{\theta,\theta^{\prime}}\colon T_{a}R_{\theta}^{\phi}F_{C_{0}}\to T_{a^{\prime}}R_{\theta^{\prime}}^{\phi}F_{C_{0}}. |  |

Recall that we let v ∈ H 1 ​ ( S 1) v\in H^{1}(S^{1}) be a generator.

###### Lemma 4.3.

For any θ ∈ ( 0, π) \theta\in(0,\pi), the right action of v ∈ H 1 ​ ( S 1) ≃ H 1 ​ ( End ⁡ ( F C 0)) v\in H^{1}(S^{1})\simeq H^{1}(\operatorname{End}(F_{C_{0}})) on the cohomology of μ ​ h ​ o ​ m ​ ( F C 0, R θ ϕ ​ F C 0) \mu hom(F_{C_{0}},R^{\phi}_{\theta}F_{C_{0}}) that corresponds to the morphism τ 0, 0 0, θ: F C 0 → R θ ϕ ​ F C 0 \tau_{0,0}^{0,\theta}\colon F_{C_{0}}\to R^{\phi}_{\theta}F_{C_{0}} is zero.

###### Proof.

Take 0 = θ 0 < θ 1 < θ 2 < ⋯ < θ n < θ n + 1 = θ 0=\theta_{0}<\theta_{1}<\theta_{2}<\dots<\theta_{n}<\theta_{n+1}=\theta. Then the canonical morphism μ ​ h ​ o ​ m ​ ( F C 0, F C 0) → μ ​ h ​ o ​ m ​ ( F C 0, R θ ϕ ​ F C 0) \mu hom(F_{C_{0}},F_{C_{0}})\to\mu hom(F_{C_{0}},R^{\phi}_{\theta}F_{C_{0}}) factors as follows:

 | μ ​ h ​ o ​ m ​ ( F C 0, F C 0) {\lx@inpgf@ignorespaces\mu hom(F_{C_{0}},F_{C_{0}})} μ ​ h ​ o ​ m ​ ( F C 0, R θ ϕ ​ F C 0) {\lx@inpgf@ignorespaces\mu hom(F_{C_{0}},R^{\phi}_{\theta}F_{C_{0}})} ⨂ i = 0 n μ ​ h ​ o ​ m ​ ( R θ i ϕ ​ F C 0, R θ i + 1 ϕ ​ F C 0). {\lx@inpgf@ignorespaces\bigotimes_{i=0}^{n}\mu hom(R^{\phi}_{\theta_{i}}F_{C_{0}},R^{\phi}_{\theta_{i+1}}F_{C_{0}}).} |  |

Recall that Λ \Lambda defined in ( 3.1) and consider its conification ℝ > 0 ​ Λ ⊂ T ∗ ​ ( M × M × ℝ t / π ​ ℤ) \mathbb{R}_{>0}\Lambda\subset T^{*}(M\times M\times\mathbb{R}_{t}/\pi\mathbb{Z}). Note that μ ​ h ​ o ​ m ​ ( F C 0, F C 0) ≃ 𝐤 ℝ > 0 ​ Λ \mu hom(F_{C_{0}},F_{C_{0}})\simeq\mathbf{k}_{\mathbb{R}_{>0}\Lambda}. The support of the sheaf ⨂ i = 0 n μ ​ h ​ o ​ m ​ ( R θ i ϕ ​ F C 0, R θ i + 1 ϕ ​ F C 0) \bigotimes_{i=0}^{n}\mu hom(R^{\phi}_{\theta_{i}}F_{C_{0}},R^{\phi}_{\theta_{i+1}}F_{C_{0}}) is contained in

 | ⋂ i = 0 n ρ − 1 ​ R θ i ϕ ​ ( C 0 × C 0) ∩ ℝ > 0 ​ Λ \bigcap_{i=0}^{n}\rho^{-1}R^{\phi}_{\theta_{i}}(C_{0}\times C_{0})\cap\mathbb{R}_{>0}\Lambda |  |

By taking refinements, we find that the canonical morphism factors through the limit as follows:

 | μ ​ h ​ o ​ m ​ ( F C 0, F C 0) {\lx@inpgf@ignorespaces\mu hom(F_{C_{0}},F_{C_{0}})} μ ​ h ​ o ​ m ​ ( F C 0, R θ ϕ ​ F C 0) {\lx@inpgf@ignorespaces\mu hom(F_{C_{0}},R^{\phi}_{\theta}F_{C_{0}})} lim ⨂ i = 0 n μ ​ h ​ o ​ m ​ ( R θ i ϕ ​ F C 0, R θ i + 1 ϕ ​ F C 0), {\lx@inpgf@ignorespaces\lim\bigotimes_{i=0}^{n}\mu hom(R^{\phi}_{\theta_{i}}F_{C_{0}},R^{\phi}_{\theta_{i+1}}F_{C_{0}}),} |  |

where the limit in the second row is taken with respect to all the refinements. The support of lim ⨂ i = 0 n μ ​ h ​ o ​ m ​ ( R θ i ϕ ​ F C 0, R θ i + 1 ϕ ​ F C 0) \lim\bigotimes_{i=0}^{n}\mu hom(R^{\phi}_{\theta_{i}}F_{C_{0}},R^{\phi}_{\theta_{i+1}}F_{C_{0}}) is contained in

 | ⋂ θ ′ ∈ [0, θ] ρ − 1 ​ R θ ′ ϕ ​ ( C 0 × C 0) ∩ ℝ > 0 ​ Λ. \bigcap_{\theta^{\prime}\in[0,\theta]}\rho^{-1}R^{\phi}_{\theta^{\prime}}(C_{0}\times C_{0})\cap\mathbb{R}_{>0}\Lambda. |  |

We say an arc in C C is a θ \theta -arc in C C if there exists z 0 ∈ ℂ z_{0}\in\mathbb{C} and r > 0 r>0 such that the arc coincides the arc with angle θ \theta in the circle { z ∈ ℂ ∣ | z − z 0 | = r } \{z\in\mathbb{C}\mid|z-z_{0}|=r\}. If ( z, z ′) ∈ ⋂ θ ′ ∈ [0, θ] R θ ′ ϕ ​ ( C 0 × C 0) ∖ Δ C 0 (z,z^{\prime})\in\bigcap_{\theta^{\prime}\in[0,\theta]}R^{\phi}_{\theta^{\prime}}(C_{0}\times C_{0})\setminus\Delta_{C_{0}}, then there exist two θ \theta -arcs in C C (with counterclockwise directions) and ϕ ⁡ ( z), ϕ ⁡ ( z ′) ∈ C \phi(z),\phi(z^{\prime})\in C are both starting points of these θ \theta -arcs. We set

 | Z = { z ∈ C | z is a starting point of a (counterclockwise) θ -arc in C }. Z=\left\{z\in C\mathrel{}\middle|\mathrel{}\begin{aligned} \text{$z$ is a starting point of a (counterclockwise) $\theta$-arc in $C$}\end{aligned}\right\}. |  | (4.1) |

We assume that C C is not a circle. In this case, we can take an open subset U ⊂ C 0 U\subset C_{0} such that ϕ ⁡ ( U) \phi(U) has no intersection with Z Z. Then, we have

 | ⋂ θ ′ ∈ [0, θ] R θ ′ ϕ ​ ( C 0 × C 0) ∩ ( ( U × C 0 ∪ C 0 × U) ∖ Δ C 0) = ∅. \bigcap_{\theta^{\prime}\in[0,\theta]}R^{\phi}_{\theta^{\prime}}(C_{0}\times C_{0})\cap((U\times C_{0}\cup C_{0}\times U)\setminus\Delta_{C_{0}})=\varnothing. |  |

Setting

 | Ξ ≔ ρ − 1 ​ ( C 0 × C 0 ∖ ( ( U × C 0 ∪ C 0 × U) ∖ Δ C 0)) ∩ ℝ > 0 ​ Λ, \Xi\coloneqq\rho^{-1}(C_{0}\times C_{0}\setminus((U\times C_{0}\cup C_{0}\times U)\setminus\Delta_{C_{0}}))\cap\mathbb{R}_{>0}\Lambda, |  |

we find that the right action of v v on Γ ⁡ ( Ξ, μ ​ h ​ o ​ m ​ ( F C 0, F C 0)) \Gamma(\Xi;\mu hom(F_{C_{0}},F_{C_{0}})) is zero since the morphism ( 3.2) maps v v to v ⊗ 1 + 1 ⊗ v v\otimes 1+1\otimes v and the restriction of v ⊗ 1 + 1 ⊗ v v\otimes 1+1\otimes v to Ξ \Xi is zero.

For the case that C C is a circle, this vanishing of v ⊗ 1 + 1 ⊗ v v\otimes 1+1\otimes v on the support is obvious from an explicit calculation of the support. This completes the proof. ∎

###### Lemma 4.4.

For any θ ∈ ( 0, π) \theta\in(0,\pi), the composite of the morphisms τ 0, 0 θ, π: R θ ϕ ​ F C 0 → R π ϕ ​ F C 0 ≃ R π ​ F C 0 \tau_{0,0}^{\theta,\pi}\colon R^{\phi}_{\theta}F_{C_{0}}\to R^{\phi}_{\pi}F_{C_{0}}\simeq R_{\pi}F_{C_{0}} and R π ​ v: R π ​ F C 0 → R π ​ F C 0 ​ [1] R_{\pi}v\colon R_{\pi}F_{C_{0}}\to R_{\pi}F_{C_{0}}[1] is zero in Γ ( { τ > 0 }; μ h o m ( R θ ϕ F C 0, R π F C 0)) [1] \Gamma(\{\tau>0\};\mu hom(R^{\phi}_{\theta}F_{C_{0}},R_{\pi}F_{C_{0}}))[1]. Moreover, the composite

 | μ ​ h ​ o ​ m ​ ( F C 0, R θ ϕ ​ F C 0) → ∘ v μ ​ h ​ o ​ m ​ ( F C 0, R θ ϕ ​ F C 0) ​ [1] → μ ​ h ​ o ​ m ​ ( F C 0, R π ​ F C 0) ​ [1] \mu hom(F_{C_{0}},R^{\phi}_{\theta}F_{C_{0}})\xrightarrow{\circ v}\mu hom(F_{C_{0}},R^{\phi}_{\theta}F_{C_{0}})[1]\to\mu hom(F_{C_{0}},R_{\pi}F_{C_{0}})[1] |  | (4.2) |

is the zero morphism.

###### Proof.

The first assertion can be proved in a similar way in lemma 4.3. Since the morphism ( 4.2) is equal to

 | μ ​ h ​ o ​ m ​ ( F C 0, R θ ϕ ​ F C 0) → μ ​ h ​ o ​ m ​ ( F C 0, R π ​ F C 0) → v ∘ μ ​ h ​ o ​ m ​ ( F C 0, R π ​ F C 0) ​ [1] \mu hom(F_{C_{0}},R^{\phi}_{\theta}F_{C_{0}})\to\mu hom(F_{C_{0}},R_{\pi}F_{C_{0}})\xrightarrow{v\circ}\mu hom(F_{C_{0}},R_{\pi}F_{C_{0}})[1] |  |

with R π ​ v = v R_{\pi}v=v, the second assertion follows. ∎

Now we consider the following commutative diagram whose rows are (co)fiber sequences by lemma 2.7:

 | colim ε → 0 ​ Hom ​ ( F C 0, T − ε ​ F C 0) {\lx@inpgf@ignorespaces{\displaystyle\operatorname*{colim}_{\varepsilon\to 0}\operatorname{Hom}(F_{C_{0}},T_{-\varepsilon}F_{C_{0}})}} End ⁡ ( F C 0) {\lx@inpgf@ignorespaces\operatorname{End}(F_{C_{0}})} Γ ( { τ > 0 }; μ h o m ( F C 0, F C 0)) {\lx@inpgf@ignorespaces\Gamma(\{\tau>0\};\mu hom(F_{C_{0}},F_{C_{0}}))} colim ε → 0 ​ Hom ​ ( F C 0, T − ε ​ R θ ϕ ​ F C 0) {\lx@inpgf@ignorespaces{\displaystyle\operatorname*{colim}_{\varepsilon\to 0}\operatorname{Hom}(F_{C_{0}},T_{-\varepsilon}R^{\phi}_{\theta}F_{C_{0}})}} Hom ⁡ ( F C 0, R θ ϕ ​ F C 0) {\lx@inpgf@ignorespaces\operatorname{Hom}(F_{C_{0}},R^{\phi}_{\theta}F_{C_{0}})} Γ ( { τ > 0 }; μ h o m ( F C 0, R θ ϕ F C 0)). {\lx@inpgf@ignorespaces\Gamma(\{\tau>0\};\mu hom(F_{C_{0}},R^{\phi}_{\theta}F_{C_{0}}))\mathrlap{.}} |  |

Then the image of v v in the right below is zero by lemma 4.3. We take an arbitrary element w θ ∈ colim ε → 0 ​ Hom ​ ( F C 0, T − ε ​ R θ ϕ ​ F C 0) ​ [1] w^{\theta}\in\operatorname*{colim}_{\varepsilon\to 0}\operatorname{Hom}(F_{C_{0}},T_{-\varepsilon}R^{\phi}_{\theta}F_{C_{0}})[1] that is mapped to τ 0, 0 0, θ ​ v ∈ Hom ⁡ ( F C 0, R θ ϕ ​ F C 0) ​ [1] \tau_{0,0}^{0,\theta}v\in\operatorname{Hom}(F_{C_{0}},R^{\phi}_{\theta}F_{C_{0}})[1]. Note that the continuation morphism τ − ε, − ε θ, π \tau^{\theta,\pi}_{-\varepsilon,-\varepsilon} induces a morphism

 | colim τ − ε, − ε θ, π: colim ε → 0 ​ Hom ​ ( F C 0, T − ε ​ R θ ϕ ​ F C 0) → colim ε → 0 ​ Hom ​ ( F C 0, T − ε ​ R π ​ F C 0). \operatorname*{colim}\tau^{\theta,\pi}_{-\varepsilon,-\varepsilon}\colon\operatorname*{colim}_{\varepsilon\to 0}\operatorname{Hom}(F_{C_{0}},T_{-\varepsilon}R^{\phi}_{\theta}F_{C_{0}})\to\operatorname*{colim}_{\varepsilon\to 0}\operatorname{Hom}(F_{C_{0}},T_{-\varepsilon}R_{\pi}F_{C_{0}}). |  |

###### Lemma 4.5.

The element colim τ − ε, − ε θ, π w θ v ∈ colim ε → 0 Hom ( F C 0, T − ε R π F C 0) [2] \operatorname*{colim}\tau_{-\varepsilon,-\varepsilon}^{\theta,\pi}w^{\theta}v\in\operatorname*{colim}_{\varepsilon\to 0}\operatorname{Hom}(F_{C_{0}},T_{-\varepsilon}R_{\pi}F_{C_{0}})[2] is independent of the choices of θ ∈ ( 0, π) \theta\in(0,\pi) and w θ w^{\theta}.

###### Proof.

First, fix θ \theta and consider two elements w 0 θ w^{\theta}_{0} and w 1 θ w^{\theta}_{1} that are mapped to τ 0, 0 0, θ ​ v \tau^{0,\theta}_{0,0}v. By the (co)fiber sequence above, the difference w 0 θ − w 1 θ w^{\theta}_{0}-w^{\theta}_{1} is written as the image of an element α ∈ Γ ( { τ > 0 }; μ h o m ( F C 0, R θ ϕ F C 0)) \alpha\in\Gamma(\{\tau>0\};\mu hom(F_{C_{0}},R^{\phi}_{\theta}F_{C_{0}})). The morphism that sends α \alpha to colim τ − ε, − ε θ, π ​ ( w 0 θ − w 1 θ) ​ v \operatorname*{colim}\tau_{-\varepsilon,-\varepsilon}^{\theta,\pi}(w^{\theta}_{0}-w^{\theta}_{1})v factors the morphism

 | Γ ( { τ > 0 }; μ h o m ( F C 0, R θ ϕ F C 0)) → Γ ( { τ > 0 }; μ h o m ( F C 0, R π F C 0)) [1], \Gamma(\{\tau>0\};\mu hom(F_{C_{0}},R^{\phi}_{\theta}F_{C_{0}}))\to\Gamma(\{\tau>0\};\mu hom(F_{C_{0}},R_{\pi}F_{C_{0}}))[1], |  |

which is zero by lemma 4.4. This proves colim τ − ε, − ε θ, π ​ ( w 0 θ − w 1 θ) ​ v = 0 \operatorname*{colim}\tau_{-\varepsilon,-\varepsilon}^{\theta,\pi}(w^{\theta}_{0}-w^{\theta}_{1})v=0.

Next, we will prove the independence on θ \theta. Let θ ≤ θ ′ \theta\leq\theta^{\prime} and take w θ w^{\theta} and w θ ′ w^{\theta^{\prime}} that are mapped to v v. Then we can apply the above argument to the two element colim τ − ε, − ε θ, θ ′ w θ \operatorname*{colim}\tau_{-\varepsilon,-\varepsilon}^{\theta,\theta^{\prime}}w^{\theta} and w θ ′ w^{\theta^{\prime}} in colim ε → 0 ​ Hom ​ ( F C 0, T − ε ​ R θ ϕ ​ F C 0) ​ [1] \operatorname*{colim}_{\varepsilon\to 0}\operatorname{Hom}(F_{C_{0}},T_{-\varepsilon}R^{\phi}_{\theta}F_{C_{0}})[1], which prove the lemma. ∎

###### Lemma 4.6.

The colim τ − ε, − ε θ, π w θ v ∈ colim ε → 0 Hom ( F C 0, T − ε R π F C 0) [2] \operatorname*{colim}\tau_{-\varepsilon,-\varepsilon}^{\theta,\pi}w^{\theta}v\in\operatorname*{colim}_{\varepsilon\to 0}\operatorname{Hom}(F_{C_{0}},T_{-\varepsilon}R_{\pi}F_{C_{0}})[2] is non-zero.

###### Proof.

By lemma 4.5, it is enough to show the claim for a sufficiently small θ > 0 \theta>0.

Let us first consider the case ϕ \phi is a Hamiltonian diffeomorphism with compact support. In this case, we will reduce the problem to the case of the standard circle C 0 C_{0}. There exists a bi-Lipschitz constant B B such that

 | 1 B ​ d E ​ ( z, z ′) ≤ d E ​ ( ϕ ⁡ ( z), ϕ ⁡ ( z ′)) ≤ B ​ d E ​ ( z, z ′) \frac{1}{B}d_{E}(z,z^{\prime})\leq d_{E}(\phi(z),\phi(z^{\prime}))\leq Bd_{E}(z,z^{\prime}) |  |

for any z, z ′ ∈ ℂ z,z^{\prime}\in\mathbb{C}, where d E d_{E} stands for the Euclidean metric. Note that R θ R_{\theta} is generated by H ⁡ ( z 1, z 2) = | z 1 − z 2 | 2 / 4 H(z_{1},z_{2})=|z_{1}-z_{2}|^{2}/4 and R θ ϕ R^{\phi}_{\theta} is generated by H ϕ = H ∘ ( ϕ × ϕ) H^{\phi}=H\circ(\phi\times\phi), which implies

 | 1 B 2 ​ H ≤ H ϕ ≤ B 2 ​ H. \frac{1}{B^{2}}H\leq H^{\phi}\leq B^{2}H. |  |

Hence, as positive Hamiltonian isotopies, we have

 | id ≤ R θ / B 2 ≤ R θ ϕ ≤ R B 2 ​ θ for θ ≥ 0, \operatorname{id}\leq R_{\theta/B^{2}}\leq R^{\phi}_{\theta}\leq R_{B^{2}\theta}\quad\text{for $\theta\geq 0$}, |  |

which gives continuation morphisms.

We take θ > 0 \theta>0 satisfying B 2 ​ θ < π B^{2}\theta<\pi. Then, for 0 < ε < θ / B 2 0<\varepsilon<\theta/B^{2}, we have the following interleaving

 | Hom ⁡ ( F C 0, T − ε ​ R θ / B 2 ​ F C 0) → Hom ⁡ ( F C 0, T − ε ​ R θ ϕ ​ F C 0) → Hom ⁡ ( F C 0, T − ε ​ R π ​ F C 0). \operatorname{Hom}(F_{C_{0}},T_{-\varepsilon}R_{\theta/B^{2}}F_{C_{0}})\to\operatorname{Hom}(F_{C_{0}},T_{-\varepsilon}R^{\phi}_{\theta}F_{C_{0}})\to\operatorname{Hom}(F_{C_{0}},T_{-\varepsilon}R_{\pi}F_{C_{0}}). |  | (4.3) |

We take an element w ε θ ∈ Hom ⁡ ( F C 0, T − ε ​ R θ / B 2 ​ F C 0) ​ [1] w^{\theta}_{\varepsilon}\in\operatorname{Hom}(F_{C_{0}},T_{-\varepsilon}R_{\theta/B^{2}}F_{C_{0}})[1] that is mapped to the image of v v in Hom ⁡ ( F C 0, R θ / B 2 ​ F C 0) ​ [1] \operatorname{Hom}(F_{C_{0}},R_{\theta/B^{2}}F_{C_{0}})[1] via the continuation morphism. Its image under the first interleaving morphism in ( 4.3) defines an element w θ ∈ colim ε → 0 ​ Hom ​ ( F C 0, T − ε ​ R θ ϕ ​ F C 0) ​ [1] w^{\theta}\in\operatorname*{colim}_{\varepsilon\to 0}\operatorname{Hom}(F_{C_{0}},T_{-\varepsilon}R^{\phi}_{\theta}F_{C_{0}})[1], which is mapped to τ 0, 0 0, θ ​ v ∈ Hom ⁡ ( F C 0, R θ ϕ ​ F C 0) ​ [1] \tau_{0,0}^{0,\theta}v\in\operatorname{Hom}(F_{C_{0}},R^{\phi}_{\theta}F_{C_{0}})[1]. By the arguments in section 3.3, we find that w ε θ ​ v ∈ Hom ⁡ ( F C 0, T − ε ​ R θ / B 2 ​ F C 0) ​ [2] w^{\theta}_{\varepsilon}v\in\operatorname{Hom}(F_{C_{0}},T_{-\varepsilon}R_{\theta/B^{2}}F_{C_{0}})[2] is non-zero and both of the morphisms

 | Hom ⁡ ( F C 0, T − ε ​ R θ / B 2 ​ F C 0) \displaystyle\operatorname{Hom}(F_{C_{0}},T_{-\varepsilon}R_{\theta/B^{2}}F_{C_{0}}) | → Hom ( F C 0, T − ε R π F C 0) and \displaystyle\to\operatorname{Hom}(F_{C_{0}},T_{-\varepsilon}R_{\pi}F_{C_{0}})\quad\text{and} |  |

 | Hom ⁡ ( F C 0, T − ε ​ R π ​ F C 0) \displaystyle\operatorname{Hom}(F_{C_{0}},T_{-\varepsilon}R_{\pi}F_{C_{0}}) | → colim ε → 0 ​ Hom ​ ( F C 0, T − ε ​ R π ​ F C 0) \displaystyle\to\operatorname*{colim}_{\varepsilon\to 0}\operatorname{Hom}(F_{C_{0}},T_{-\varepsilon}R_{\pi}F_{C_{0}}) |  |

are isomorphisms by proposition 3.11. Hence colim τ − ε, − ε θ, π w θ v \operatorname*{colim}\tau_{-\varepsilon,-\varepsilon}^{\theta,\pi}w^{\theta}v is non-zero.

Now we consider the continuous case and take a sequence of Hamiltonian diffeomorphisms with compact support ( ϕ n) n (\phi_{n})_{n} that converges to a Hamiltonian homeomorphism ϕ \phi in the C 0 C^{0} -sense. We take ( ϕ n) n (\phi_{n})_{n} so that each C n ≔ ϕ n ​ ( C 0) C_{n}\coloneqq\phi_{n}(C_{0}) is real analytic. Since the Hamiltonian function H H is bounded on C × C C\times C, we can choose sufficiently small θ 0 > 0 \theta_{0}>0 so that sup θ ∈ [0, θ 0] d ⁡ ( F C 0, R θ ϕ ​ F C 0) \sup_{\theta\in[0,\theta_{0}]}d(F_{C_{0}},R_{\theta}^{\phi}F_{C_{0}}) is sufficiently small. Take ε > 0 \varepsilon>0 and a representative w ε θ ∈ Hom ⁡ ( F C 0, T − ε ​ R θ 0 ϕ ​ F C 0) ​ [1] w^{\theta}_{\varepsilon}\in\operatorname{Hom}(F_{C_{0}},T_{-\varepsilon}R^{\phi}_{\theta_{0}}F_{C_{0}})[1] of w θ w^{\theta}. For a sufficiently large n n, there is a ( δ, δ) (\delta,\delta) -interleaving for the pair ( R θ 0 ϕ ​ F C 0, R θ 0 ϕ n ​ F C 0) (R^{\phi}_{\theta_{0}}F_{C_{0}},R^{\phi_{n}}_{\theta_{0}}F_{C_{0}}), where δ < ε / 100 \delta<\varepsilon/100.

Let us consider the following commutative diagram:

 | F C 0 {\lx@inpgf@ignorespaces F_{C_{0}}} T − ε ​ R θ 0 ϕ ​ F C 0 ​ [1] {\lx@inpgf@ignorespaces T_{-\varepsilon}R^{\phi}_{\theta_{0}}F_{C_{0}}[1]} T − ε + δ ​ R θ 0 ϕ n ​ F C 0 ​ [1] {\lx@inpgf@ignorespaces T_{-\varepsilon+\delta}R^{\phi_{n}}_{\theta_{0}}F_{C_{0}}[1]} R θ 0 ϕ n ​ F C 0 ​ [1] {\lx@inpgf@ignorespaces R^{\phi_{n}}_{\theta_{0}}F_{C_{0}}[1]} T − ε ​ R π ϕ ​ F C 0 ​ [1] {\lx@inpgf@ignorespaces T_{-\varepsilon}R^{\phi}_{\pi}F_{C_{0}}[1]} T − ε + δ ​ R π ϕ n ​ F C 0 ​ [1]. {\lx@inpgf@ignorespaces T_{-\varepsilon+\delta}R^{\phi_{n}}_{\pi}F_{C_{0}}[1].} |  |

We claim that the upper morphism F C 0 → R θ 0 ϕ n ​ F C 0 ​ [1] F_{C_{0}}\to R^{\phi_{n}}_{\theta_{0}}F_{C_{0}}[1] is τ 0, 0 0, θ 0 ​ v \tau_{0,0}^{0,{\theta_{0}}}v. We postpone the proof of this claim and first prove the assertion of the lemma. By the smooth case proved above, the composite of v v and the morphism F C 0 → T − ε + δ ​ R π ϕ n ​ F C 0 ​ [1] F_{C_{0}}\to T_{-\varepsilon+\delta}R^{\phi_{n}}_{\pi}F_{C_{0}}[1] is non-zero. Hence, the composite of v v and the morphism F C 0 → T − ε ​ R π ϕ ​ F C 0 ​ [1] F_{C_{0}}\to T_{-\varepsilon}R^{\phi}_{\pi}F_{C_{0}}[1] is also non-zero. Then the result follows from the fact that

 | Hom ⁡ ( F C 0, T − ε ​ R π ϕ ​ F C 0) → colim ε → 0 ​ Hom ​ ( F C 0, T − ε ​ R π ϕ ​ F C 0) \operatorname{Hom}(F_{C_{0}},T_{-\varepsilon}R^{\phi}_{\pi}F_{C_{0}})\to\operatorname*{colim}_{\varepsilon\to 0}\operatorname{Hom}(F_{C_{0}},T_{-\varepsilon}R^{\phi}_{\pi}F_{C_{0}}) |  |

is an isomorphism.

Let us prove the remaining claim by investigating the following two quantities a ⁡ ( θ, C n) a(\theta,C_{n}) and b ⁡ ( θ, C n) b(\theta,C_{n}) defined for θ ∈ [0, π) \theta\in[0,\pi) and C n C_{n} with the property τ 0, 0 0, θ ​ v ≠ 0 ∈ Γ [0, ∞) ​ ( ℝ, 𝒱 C n, θ) ​ [1] \tau_{0,0}^{0,\theta}v\neq 0\in\Gamma_{[0,\infty)}(\mathbb{R};\mathcal{V}_{C_{n},\theta})[1]:

 | a ⁡ ( θ, C n) \displaystyle a(\theta,C_{n}) | ≔ sup { a ∈ ℝ ≥ 0 ∣ τ 0, 0 0, θ ​ v is in the image of Γ [a, ∞) ​ ( ℝ, 𝒱 C n, θ) ​ [1] }, \displaystyle\coloneqq\sup\{a\in\mathbb{R}_{\geq 0}\mid\text{$\tau_{0,0}^{0,\theta}v$ is in the image of $\Gamma_{[a,\infty)}(\mathbb{R};\mathcal{V}_{C_{n},\theta})[1]$}\}, |  |

 | b ⁡ ( θ, C n) \displaystyle b(\theta,C_{n}) | ≔ sup { b ∈ ℝ ≥ 0 | there exist w ∈ Γ [b, ∞) ​ ( ℝ, 𝒱 C n, θ) ​ [1] and t ∈ ℝ ≥ 0 such that w and τ 0, 0 0, θ ​ v coincide in Γ [− t, ∞) ( ℝ; 𝒱 C n, θ) [1] as non-zero elements }. \displaystyle\coloneqq\sup\left\{b\in\mathbb{R}_{\geq 0}\mathrel{}\middle|\mathrel{}\begin{aligned} &\text{there exist $w\in\Gamma_{[b,\infty)}(\mathbb{R};\mathcal{V}_{C_{n},\theta})[1]$ and $t\in\mathbb{R}_{\geq 0}$}\\ &\text{such that $w$ and $\tau_{0,0}^{0,\theta}v$ coincide in $\Gamma_{[-t,\infty)}(\mathbb{R};\mathcal{V}_{C_{n},\theta})[1]$}\\ &\text{as non-zero elements}\end{aligned}\right\}. |  |

By definition a ⁡ ( θ, C n) ≤ b ⁡ ( θ, C n) a(\theta,C_{n})\leq b(\theta,C_{n}), and we already know b ⁡ ( θ 0, C n) ≥ ε − δ b(\theta_{0},C_{n})\geq\varepsilon-\delta. We will show a ⁡ ( θ 0, C n) = b ⁡ ( θ 0, C n) a(\theta_{0},C_{n})=b(\theta_{0},C_{n}) and then obtain the claim with the interleaving for ( R θ 0 ϕ ​ F C 0, R θ 0 ϕ n ​ F C 0) (R^{\phi}_{\theta_{0}}F_{C_{0}},R^{\phi_{n}}_{\theta_{0}}F_{C_{0}}). We will prove it by contradiction and suppose that a ⁡ ( θ 0, C n) ≠ b ⁡ ( θ 0, C n) a(\theta_{0},C_{n})\neq b(\theta_{0},C_{n}). Consider the real number

 | θ 1 ≔ inf { θ ∈ [0, θ 0] ∣ a ⁡ ( θ, C n) ≠ b ⁡ ( θ, C n) }. \theta_{1}\coloneqq\inf\{\theta\in[0,\theta_{0}]\mid a(\theta,C_{n})\neq b(\theta,C_{n})\}. |  |

By the analyticity of C n C_{n}, the family ( Hom ⁡ ( F C 0, R θ ϕ n ​ F C 0)) θ (\operatorname{Hom}(F_{C_{0}},R_{\theta}^{\phi_{n}}F_{C_{0}}))_{\theta} is constant for sufficiently small θ > 0 \theta>0. By the interleaving with C 0 C_{0} as above, H 1 ​ ( Hom ⁡ ( F C 0, R θ ϕ n ​ F C 0)) H^{1}(\operatorname{Hom}(F_{C_{0}},R_{\theta}^{\phi_{n}}F_{C_{0}})) is 1 1 -dimensional, and hence it contains a unique non-zero element. This proves a ⁡ ( θ, C n) = b ⁡ ( θ, C n) a(\theta,C_{n})=b(\theta,C_{n}) for a sufficiently small θ \theta, which implies θ 1 > 0 \theta_{1}>0. Consider the continuous family ( 𝒱 C n, θ) θ (\mathcal{V}_{C_{n},\theta})_{\theta} of constructible sheaves on ℝ \mathbb{R}, which can be regarded as a family of persistence modules (in the derived sense). For 0 ≤ θ < θ 1 0\leq\theta<\theta_{1}, the element τ 0, 0 0, θ ​ v \tau_{0,0}^{0,\theta}v corresponds to an interval module that is a summand of 𝒱 C n, θ \mathcal{V}_{C_{n},\theta} and has a length close to π \pi. When θ \theta exceeds θ 1 \theta_{1}, a change of basis occurs and the element no longer corresponds to a single interval module. For such a change of basis, there needs to be another interval module of the same length. However, since θ 0 \theta_{0} is sufficiently small, such an interval module cannot exist, which makes a contradiction. ∎

###### Lemma 4.7.

For any θ ∈ ( 0, π) \theta\in(0,\pi), the element τ 0, 0 0, θ ​ v \tau_{0,0}^{0,\theta}v is non-zero in Hom ⁡ ( F C 0, R θ ϕ ​ F C 0) ​ [1] ≃ Hom ⁡ ( F C, R θ ​ F C) ​ [1] \operatorname{Hom}(F_{C_{0}},R^{\phi}_{\theta}F_{C_{0}})[1]\simeq\operatorname{Hom}(F_{C},R_{\theta}F_{C})[1].

###### Proof.

If τ 0, 0 0, θ ​ v = 0 \tau_{0,0}^{0,\theta}v=0, we can take w θ w^{\theta} as the zero element. This contradicts to lemmas 4.5 and 4.6. ∎

By lemmas 4.7 and 3.7, we can define a ⁡ ( θ, C) a(\theta,C) by

 | a ⁡ ( θ, C) ≔ sup { a ∈ ℝ ≥ 0 ∣ τ 0, 0 0, θ ​ v is in the image of Γ [a, ∞) ​ ( ℝ, 𝒱 C, θ) ​ [1] } ∈ ℝ ≥ 0, a(\theta,C)\coloneqq\sup\{a\in\mathbb{R}_{\geq 0}\mid\text{$\tau_{0,0}^{0,\theta}v$ is in the image of $\Gamma_{[a,\infty)}(\mathbb{R};\mathcal{V}_{C,\theta})[1]$}\}\in\mathbb{R}_{\geq 0}, |  |

which already appeared in the proof of lemma 4.6.

###### Lemma 4.8.

For any θ ∈ ( 0, π) \theta\in(0,\pi), one has a ⁡ ( θ, C) ∈ ( 0, π) a(\theta,C)\in(0,\pi).

###### Proof.

By the argument before lemma 4.5, the element τ 0, 0 0, θ ​ v \tau_{0,0}^{0,\theta}v comes from Γ [ε θ, ∞) ​ ( ℝ, 𝒱 C, θ) ​ [1] \Gamma_{[\varepsilon_{\theta},\infty)}(\mathbb{R};\mathcal{V}_{C,\theta})[1] for some ε θ > 0 \varepsilon_{\theta}>0, which shows a ⁡ ( θ, C) > 0 a(\theta,C)>0.

By proposition 5.1 in the next section, the object 𝒱 C, θ ∈ 𝒯 ⁡ ( pt) \mathcal{V}_{C,\theta}\in\mathcal{T}(\mathrm{pt}) is limit constructible. By proposition 2.5, we find that v v is non-zero in Γ [− ε, ∞) ( ℝ; 𝒱 C, θ) [1] \Gamma_{[-\varepsilon,\infty)}(\mathbb{R};\mathcal{V}_{C,\theta})[1] for a sufficiently small ε > 0 \varepsilon>0. By corollary 3.7, v v does not come from Γ [π − ε, ∞) ( ℝ; 𝒱 C, θ) [1] \Gamma_{[\pi-\varepsilon,\infty)}(\mathbb{R};\mathcal{V}_{C,\theta})[1], which proves a ⁡ ( θ, C) < π a(\theta,C)<\pi. ∎

We will finish the proof of theorem 4.1. The object 𝒱 C, θ \mathcal{V}_{C,\theta} has a non-zero microstalk over a ⁡ ( θ, C) a(\theta,C), which implies SS ∙ ⁡ ( F C) ∩ T − a ⁡ ( θ, C) ​ SS ∙ ⁡ ( R θ ​ F C) ≠ ∅ \DMS(F_{C})\cap T_{-a(\theta,C)}\DMS(R_{\theta}F_{C})\neq\varnothing. By the assumption and lemma 4.8, we find that SS ∙ ⁡ ( F C) ∩ T − a ⁡ ( θ, C) ​ SS ∙ ⁡ ( F C) = ∅ \DMS(F_{C})\cap T_{-a(\theta,C)}\DMS(F_{C})=\varnothing. Thus, we have ( SS ∙ ⁡ ( F C) ∩ T − a ⁡ ( θ, C) ​ SS ∙ ⁡ ( R θ ​ F C)) ∖ ρ − 1 ​ ( Δ C) ≠ ∅ (\DMS(F_{C})\cap T_{-a(\theta,C)}\DMS(R_{\theta}F_{C}))\setminus\rho^{-1}(\Delta_{C})\neq\varnothing, which corresponds to θ \theta -rectangles on C C. This completes the proof of theorem 4.1.

## 5 Jordan curves

In this section, we deduce theorem 1.1 from theorem 4.1. We also deduce corollaries 1.2 and 1.3 from theorem 1.1. Throughout this section, we let 𝔻 q \mathbb{D}_{q} be the open disk { z ∈ ℂ ∣ | z | < q } \{z\in\mathbb{C}\mid|z|<q\} in ℂ ≃ ℝ 2 \mathbb{C}\simeq\mathbb{R}^{2} for q > 0 q>0. We also set 𝔸 q ≔ { z ∈ ℂ ∣ q < | z | < 1 } \mathbb{A}_{q}\coloneqq\{z\in\mathbb{C}\mid q<|z|<1\} for q ∈ ( 0, 1) q\in(0,1). For a Jordan curve C C, we let A ⁡ ( C) A(C) denote the area of the open domain bounded by C C.

### 5.1 Proof of the main theorem

For a proof of theorem 1.1, we first prove the following:

###### Proposition 5.1.

Let ( c n: S 1 → ℝ 2) n (c_{n}\colon S^{1}\to\mathbb{R}^{2})_{n} be a sequence of smooth curves. Assume that ( c n) n (c_{n})_{n} converges to a Jordan curve c c in the C 0 C^{0} -sense and the area of the domain bounded by C n = c n ​ ( S 1) C_{n}=c_{n}(S^{1}) and C = c ⁡ ( S 1) C=c(S^{1}) are π \pi, that is, A ⁡ ( C n) = π A(C_{n})=\pi and A ⁡ ( C) = π A(C)=\pi. Then the sequence of sheaf quantizations ( F C n) n (F_{C_{n}})_{n} is a Cauchy sequence (after translated to the ℝ t / π ​ ℤ \mathbb{R}_{t}/\pi\mathbb{Z} -direction), whose limit object F F is limit constructible.

Moreover, if there exists a Hamiltonian homeomorphism with compact support ϕ \phi such that C = ϕ ⁡ ( S 1) C=\phi(S^{1}), then F ≃ F C ≔ 𝒦 ⁡ ( ϕ × ϕ) ​ F C 0 F\simeq F_{C}\coloneqq\mathcal{K}(\phi\times\phi)F_{C_{0}}.

###### Proof.

We may assume that the origin is bounded by C n C_{n} for all n n.

(a) First we will prove ( F C n) n (F_{C_{n}})_{n} is a Cauchy sequence.

Let D D be the open domain bounded by C C. We take a biholomorphism ψ: 𝔻 1 → D \psi\colon\mathbb{D}_{1}\to D with ψ ⁡ ( 0) = 0 \psi(0)=0 and extend it to a homeomorphism ψ ¯: 𝔻 1 ¯ → D ¯ \overline{\psi}\colon\overline{\mathbb{D}_{1}}\to\overline{D} by the Riemann mapping theorem and the Carathéodory theorem. There is a strictly increasing function g: ( 0, 1] → ( 0, 1] g\colon(0,1]\to(0,1] such that the area D a ≔ ψ ⁡ ( 𝔻 g ⁡ ( a)) D_{a}\coloneqq\psi(\mathbb{D}_{g(a)}) is π ​ a 2 \pi a^{2}. Then, the family of open subdomains ( D a) a ∈ ( 0, 1] (D_{a})_{a\in(0,1]} satisfy the following:

- •

if a < a ′ a<a^{\prime}, then D a ¯ ⊂ D a ′ \overline{D_{a}}\subset D_{a^{\prime}};

- •

for each a ∈ ( 0, 1) a\in(0,1), the boundary ∂ D a \partial D_{a} is a smooth Jordan curve;

- •

there exists a positive real number L L such that

 | 1 2 ​ π ​ ( max { a } × [0, 2 ​ π] ⁡ θ ψ ~ − min { a } × [0, 2 ​ π] ⁡ θ ψ ~) ≤ L ψ \frac{1}{2\pi}\left(\max_{\{a\}\times[0,2\pi]}\widetilde{\theta_{\psi}}-\min_{\{a\}\times[0,2\pi]}\widetilde{\theta_{\psi}}\right)\leq L_{\psi} |  |

for any a ∈ ( 0, 1] a\in(0,1]. Here θ ψ ~: ( 0, 1] × [0, 2 ​ π] → ℝ \widetilde{\theta_{\psi}}\colon(0,1]\times[0,2\pi]\to\mathbb{R} denotes a lift of

 | ( 0, 1] × [0, 2 ​ π] → ( r, θ) ↦ r ​ e − 1 ​ θ 𝔻 ∖ { 0 } → ψ ¯ D ∖ { 0 } → 𝜃 ℝ / 2 ​ π ​ ℤ, (0,1]\times[0,2\pi]\xrightarrow{(r,\theta)\mapsto re^{\sqrt{-1}\theta}}\mathbb{D}\setminus\{0\}\xrightarrow{\overline{\psi}}D\setminus\{0\}\xrightarrow{\theta}\mathbb{R}/2\pi\mathbb{Z}, |  |

where θ \theta denotes the locally defined argument. This L ψ L_{\psi} depends only on ψ \psi.

To prove the last claim, we take ε > 0 \varepsilon>0 and consider the annulus 𝔸 ε = { z ∈ ℂ ∣ ε < | z | < 1 } \mathbb{A}_{\varepsilon}=\{z\in\mathbb{C}\mid\varepsilon<|z|<1\}. Then we can apply lemma 5.2 below to get

 | 1 2 ​ π ​ ( max { a } × [0, 2 ​ π] ⁡ θ ψ ~ − min { a } × [0, 2 ​ π] ⁡ θ ψ ~) ≤ L, \frac{1}{2\pi}\left(\max_{\{a\}\times[0,2\pi]}\widetilde{\theta_{\psi}}-\min_{\{a\}\times[0,2\pi]}\widetilde{\theta_{\psi}}\right)\leq L, |  |

where L L can be chosen so that

 | L ≤ 1 2 ​ π ​ max ⁡ { max { ε } × [0, 2 ​ π] ⁡ θ ψ ~ − min { ε } × [0, 2 ​ π] ⁡ θ ψ ~, max { 1 } × [0, 2 ​ π] ⁡ θ ψ ~ − min { 1 } × [0, 2 ​ π] ⁡ θ ψ ~ } + 1. L\leq\frac{1}{2\pi}\max\left\{\max_{\{\varepsilon\}\times[0,2\pi]}\widetilde{\theta_{\psi}}-\min_{\{\varepsilon\}\times[0,2\pi]}\widetilde{\theta_{\psi}},\max_{\{1\}\times[0,2\pi]}\widetilde{\theta_{\psi}}-\min_{\{1\}\times[0,2\pi]}\widetilde{\theta_{\psi}}\right\}+1. |  |

Since ψ \psi is differentiable at 0 0, given δ > 0 \delta>0, there exists a sufficiently small ε > 0 \varepsilon>0 such that max { a } × [0, 2 ​ π] ⁡ θ ψ ~ − min { a } × [0, 2 ​ π] ⁡ θ ψ ~ ≤ 2 ​ π + δ \max_{\{a\}\times[0,2\pi]}\widetilde{\theta_{\psi}}-\min_{\{a\}\times[0,2\pi]}\widetilde{\theta_{\psi}}\leq 2\pi+\delta for any a ∈ ( 0, ε] a\in(0,\varepsilon]. It suffices to define

 | L ψ ≔ 1 2 ​ π ​ max ⁡ { 2 ​ π, max { 1 } × [0, 2 ​ π] ⁡ θ ψ ~ − min { 1 } × [0, 2 ​ π] ⁡ θ ψ ~ } + 1, L_{\psi}\coloneqq\frac{1}{2\pi}\max\left\{2\pi,\max_{\{1\}\times[0,2\pi]}\widetilde{\theta_{\psi}}-\min_{\{1\}\times[0,2\pi]}\widetilde{\theta_{\psi}}\right\}+1, |  |

which proves the claim.

Take a < 1 a<1 that is sufficiently close to 1 1. By the C 0 C^{0} -convergence, there exists N N such that if n ≥ N n\geq N then C n C_{n} is included in the complement of D a ¯ \overline{D_{a}}. Let A a, n A_{a,n} be the domain between ∂ D a \partial D_{a} and C n C_{n}. Note that the area of A a, n A_{a,n} is π ⁡ ( 1 − a 2) \pi(1-a^{2}). There exist a unique real number q ∈ ( 0, 1) q\in(0,1) such that the standard annulus 𝔸 q = { z ∈ ℂ ∣ q < | z | < 1 } \mathbb{A}_{q}=\{z\in\mathbb{C}\mid q<|z|<1\} is biholomorphic to the open domain A a, n A_{a,n}. Take a biholomorphism φ n: 𝔸 q → A a, n \varphi_{n}\colon\mathbb{A}_{q}\to A_{a,n} so that the continuous extension φ n ¯: 𝔸 q ¯ → A a, n ¯ \overline{\varphi_{n}}\colon\overline{\mathbb{A}_{q}}\to\overline{A_{a,n}} of φ n \varphi_{n} satisfies

- •

φ n ¯ \overline{\varphi_{n}} sends ∂ 𝔻 1 \partial\mathbb{D}_{1} to C n C_{n};

- •

φ n ¯ \overline{\varphi_{n}} sends q ∈ ∂ 𝔻 q q\in\partial\mathbb{D}_{q} to ψ ⁡ ( g ⁡ ( a)) ∈ ∂ D a \psi(g(a))\in\partial D_{a}, where g ⁡ ( a) g(a) is regarded as a point on ∂ 𝔻 g ⁡ ( a) \partial\mathbb{D}_{g(a)}.

Since the boundary components of A a, n A_{a,n} are smooth curves, φ n ¯ \overline{\varphi_{n}} is smooth also at the boundaries by [GM05, Chapter II. Cor. 4.6]. Let θ n ~: ( q, 1) × [0, 2 ​ π] → ℝ \widetilde{\theta_{n}}\colon(q,1)\times[0,2\pi]\to\mathbb{R} be a lift of ( q, 1) × [0, 2 ​ π] → 𝔸 q → φ n A a, n → 𝜃 ℝ / 2 ​ π ​ ℤ (q,1)\times[0,2\pi]\to\mathbb{A}_{q}\xrightarrow{\varphi_{n}}A_{a,n}\xrightarrow{\theta}\mathbb{R}/2\pi\mathbb{Z}. By the condition of φ n ¯ \overline{\varphi_{n}}, we have

 | max { q } × [0, 2 ​ π] ⁡ θ n ~ − min { q } × [0, 2 ​ π] ⁡ θ n ~ = max { q } × [0, 2 ​ π] ⁡ θ ψ ~ − min { q } × [0, 2 ​ π] ⁡ θ ψ ~. \max_{\{q\}\times[0,2\pi]}\widetilde{\theta_{n}}-\min_{\{q\}\times[0,2\pi]}\widetilde{\theta_{n}}=\max_{\{q\}\times[0,2\pi]}\widetilde{\theta_{\psi}}-\min_{\{q\}\times[0,2\pi]}\widetilde{\theta_{\psi}}. |  |

Since ( c n) n (c_{n})_{n} converges c c in the C 0 C^{0} -sense, there exists a sequence of self-homeomorphisms ( σ n) n (\sigma_{n})_{n} of ∂ 𝔻 1 \partial\mathbb{D}_{1} such that φ n ¯ ∘ σ n \overline{\varphi_{n}}\circ\sigma_{n} converges to ψ ¯ | ∂ 𝔻 1 \overline{\psi}|_{\partial\mathbb{D}_{1}} in the C 0 C^{0} -sense. Take a lift θ n ′ ~ \widetilde{\theta_{n}^{\prime}} of [0, 2 ​ π] → ∂ 𝔻 1 → φ n ¯ ∘ σ n φ n ¯ ​ ( ∂ 𝔻 1) → 𝜃 ℝ / 2 ​ π ​ ℤ [0,2\pi]\to\partial\mathbb{D}_{1}\xrightarrow{\overline{\varphi_{n}}\circ\sigma_{n}}\overline{\varphi_{n}}(\partial\mathbb{D}_{1})\xrightarrow{\theta}\mathbb{R}/2\pi\mathbb{Z}. We will prove the inequality

 | | ( max { 1 } × [0, 2 ​ π] ⁡ θ n ~ − min { 1 } × [0, 2 ​ π] ⁡ θ n ~) − ( max [0, 2 ​ π] ⁡ θ n ′ ~ − min [0, 2 ​ π] ⁡ θ n ′ ~) | ≤ 2 ​ π. \left|\left(\max_{\{1\}\times[0,2\pi]}\widetilde{\theta_{n}}-\min_{\{1\}\times[0,2\pi]}\widetilde{\theta_{n}}\right)-\left(\max_{[0,2\pi]}\widetilde{\theta_{n}^{\prime}}-\min_{[0,2\pi]}\widetilde{\theta_{n}^{\prime}}\right)\right|\leq 2\pi. |  | (5.1) |

By abuse of notation, we also write θ n ~ \widetilde{\theta_{n}} for a lift of ℝ → θ ↦ e − 1 ​ θ ∂ 𝔻 1 → φ n ¯ ​ ( ∂ 𝔻 1) → ℝ / 2 ​ π ​ ℤ \mathbb{R}\xrightarrow{\theta\mapsto e^{\sqrt{-1}\theta}}\partial\mathbb{D}_{1}\to\overline{\varphi_{n}}(\partial\mathbb{D}_{1})\to\mathbb{R}/2\pi\mathbb{Z} to ℝ → ℝ \mathbb{R}\to\mathbb{R}. Then, we get

 | max { 1 } × [0, 2 ​ π] ⁡ θ n ~ − min { 1 } × [0, 2 ​ π] ⁡ θ n ~ + 2 ​ π = max { 1 } × [0, 4 ​ π] ⁡ θ n ~ − min { 1 } × [0, 4 ​ π] ⁡ θ n ~. \max_{\{1\}\times[0,2\pi]}\widetilde{\theta_{n}}-\min_{\{1\}\times[0,2\pi]}\widetilde{\theta_{n}}+2\pi=\max_{\{1\}\times[0,4\pi]}\widetilde{\theta_{n}}-\min_{\{1\}\times[0,4\pi]}\widetilde{\theta_{n}}. |  |

Moreover, there exists b ∈ [0, 2 ​ π] b\in[0,2\pi] satisfying

 | max [0, 2 ​ π] ⁡ θ n ′ ~ − min [0, 2 ​ π] ⁡ θ n ′ ~ = max { 1 } × [b, b + 2 ​ π] ⁡ θ n ~ − min { 1 } × [b, b + 2 ​ π] ⁡ θ n ~, \max_{[0,2\pi]}\widetilde{\theta_{n}^{\prime}}-\min_{[0,2\pi]}\widetilde{\theta_{n}^{\prime}}=\max_{\{1\}\times[b,b+2\pi]}\widetilde{\theta_{n}}-\min_{\{1\}\times[b,b+2\pi]}\widetilde{\theta_{n}}, |  |

which proves the inequality ( 5.1). By ( 5.1) and the C 0 C^{0} -convergence, for a sufficiently large n n, we have

 | | ( max { 1 } × [0, 2 ​ π] ⁡ θ n ~ − min { 1 } × [0, 2 ​ π] ⁡ θ n ~) − ( max { 1 } × [0, 2 ​ π] ⁡ θ ψ ~ − min { 1 } × [0, 2 ​ π] ⁡ θ ψ ~) | ≤ 2.1 ​ π. \left|\left(\max_{\{1\}\times[0,2\pi]}\widetilde{\theta_{n}}-\min_{\{1\}\times[0,2\pi]}\widetilde{\theta_{n}}\right)-\left(\max_{\{1\}\times[0,2\pi]}\widetilde{\theta_{\psi}}-\min_{\{1\}\times[0,2\pi]}\widetilde{\theta_{\psi}}\right)\right|\leq 2.1\pi. |  |

Thus, setting L ′ ≔ L ψ + 2.1 / 2 L^{\prime}\coloneqq L_{\psi}+2.1/2, by lemma 5.2, we have

 | 1 2 ​ π ​ ( max { u } × [0, 2 ​ π] ⁡ θ n ~ − min { u } × [0, 2 ​ π] ⁡ θ n ~) ≤ L ′ \frac{1}{2\pi}\left(\max_{\{u\}\times[0,2\pi]}\widetilde{\theta_{n}}-\min_{\{u\}\times[0,2\pi]}\widetilde{\theta_{n}}\right)\leq L^{\prime} |  |

for any u ∈ ( q, 1) u\in(q,1).

Let ∂ D a ′ \partial D_{a}^{\prime} be the curve ∂ D a \partial D_{a} rescaled by the flow ϕ d ​ θ \phi^{d\theta} defined below so that A ⁡ ( ∂ D a ′) = π A(\partial D_{a}^{\prime})=\pi. For u ∈ ( q, 1) u\in(q,1), put C u ≔ φ ⁡ ( ∂ 𝔻 u) C_{u}\coloneqq\varphi(\partial\mathbb{D}_{u}) and let C u ′ C_{u}^{\prime} be the curve rescaled by the flow ϕ d ​ θ \phi^{d\theta} so that A ⁡ ( C u ′) = π A(C_{u}^{\prime})=\pi. By lemma 5.3 below, for a sequence ( a i) i (a_{i})_{i} of real numbers in ( q, 1) (q,1) converging to q q from above, the sequence of constructible sheaves ( F C a i ′) i (F_{C_{a_{i}}^{\prime}})_{i} is Cauchy.

We see that the limit object F ′ F^{\prime} of ( F C a i ′) i (F_{C_{a_{i}}^{\prime}})_{i} is isomorphic to F ∂ D a ′ F_{\partial D_{a}^{\prime}} as follows. By the microsupport estimate for the limit object, the microsupport of F ′ F^{\prime} coincides with that of F ∂ D a ′ F_{\partial D_{a}^{\prime}} since φ n ¯ \overline{\varphi_{n}} is smooth also at the boundaries. By taking a compactly supported Hamiltonian diffeomorphism sending ∂ D a ′ \partial D_{a}^{\prime} to C 0 C_{0} and applying the corresponding GKS kernel to F ∂ D a ′ F_{\partial D_{a}^{\prime}} and F ′ F^{\prime}, the assertion F ∂ D a ′ ≃ F ′ F_{\partial D_{a}^{\prime}}\simeq F^{\prime} follows from lemma 3.5. Similarly, for a sequence ( a i) i (a_{i})_{i} of real numbers in ( q, 1) (q,1) converging to 1 1 from below, the sequence of constructible sheaves ( F C a i ′) i (F_{C_{a_{i}}^{\prime}})_{i} is Cauchy and converges to F C n F_{C_{n}}.

Again by lemma 5.3, for any q < u 0 < u 1 < 1 q<u_{0}<u_{1}<1,

 | d ⁡ ( F C u 0 ′, F C u 1 ′) ≤ 2 ​ ( L ′ + 1) ​ ( A ⁡ ( C u 1) − A ⁡ ( C u 0)) ≤ 2 ​ ( L ′ + 1) ​ π ​ ( 1 − a 2). d(F_{C_{u_{0}}^{\prime}},F_{C_{u_{1}}^{\prime}})\leq 2(L^{\prime}+1)(A(C_{u_{1}})-A(C_{u_{0}}))\leq 2(L^{\prime}+1)\pi(1-a^{2}). |  |

By tanking limits, we obtain

 | d ⁡ ( F ∂ D a ′, F C n) ≤ 2 ​ ( L ′ + 1) ​ π ​ ( 1 − a 2). d(F_{\partial D_{a}^{\prime}},F_{C_{n}})\leq 2(L^{\prime}+1)\pi(1-a^{2}). |  |

Hence, for m, n ≥ N m,n\geq N, we have

 | d ⁡ ( F C n, F C m) ≤ 4 ​ ( L ′ + 1) ​ π ​ ( 1 − a 2), d(F_{C_{n}},F_{C_{m}})\leq 4(L^{\prime}+1)\pi(1-a^{2}), |  |

which proves that ( F C n) n (F_{C_{n}})_{n} is a Cauchy sequence. Since each F C n F_{C_{n}} is limit constructible, a limit object F F is also limit constructible.

(b) Let us prove the second assertion and suppose that C = ϕ ⁡ ( S 1) C=\phi(S^{1}) for some Hamiltonian homeomorphism with compact support ϕ \phi. Then there exists a sequence of Hamiltonian diffeomorphisms ( ϕ n) n (\phi_{n})_{n} that converges to ϕ \phi in the C 0 C^{0} -sense. The sequence ( 𝒦 ⁡ ( ϕ n × ϕ n) ​ F C 0) n (\mathcal{K}(\phi_{n}\times\phi_{n})F_{C_{0}})_{n} is a Cauchy sequence, and its limit object is 𝒦 ⁡ ( ϕ × ϕ) ​ F C 0 \mathcal{K}(\phi\times\phi)F_{C_{0}} by definition. Then the sequence ( F k) k (F_{k})_{k} with

 | F k = { F C n ( k = 2 ​ n − 1), 𝒦 ⁡ ( ϕ n × ϕ n) ​ F C 0 ( k = 2 ​ n) F_{k}=\begin{cases}F_{C_{n}}&(k=2n-1),\\ \mathcal{K}(\phi_{n}\times\phi_{n})F_{C_{0}}&(k=2n)\end{cases} |  |

is also a Cauchy sequence. Since each pair of the limit objects of the three sequences ( F C n) n (F_{C_{n}})_{n}, ( 𝒦 ⁡ ( ϕ n × ϕ n) ​ F C 0) n (\mathcal{K}(\phi_{n}\times\phi_{n})F_{C_{0}})_{n}, and ( F k) k (F_{k})_{k} has distance zero, we conclude that F ≃ 𝒦 ⁡ ( ϕ × ϕ) ​ F C 0 F\simeq\mathcal{K}(\phi\times\phi)F_{C_{0}} by the limit constructibility and proposition 2.4. ∎

We fix some notation. Let g g be the standard metric on ℂ \mathbb{C} and set ω ≔ d ​ λ = d ​ ξ ∧ d ​ x \omega\coloneqq d\lambda=d\xi\wedge dx be the symplectic form on ℂ ≃ T ∗ ​ ℝ x \mathbb{C}\simeq T^{*}\mathbb{R}_{x}. We have ω ⁡ ( X, Y) = g ⁡ ( X, − 1 ​ Y) \omega(X,Y)=g(X,\sqrt{-1}Y). Let r, θ: ℂ ∖ { 0 } → ℝ r,\theta\colon\mathbb{C}\setminus\{0\}\to\mathbb{R} be the radius and the (locally defined) argument. We remark that d ​ θ ​ ( X) = − 1 r ​ d ​ r ​ ( − 1 ​ X) d\theta(X)=-\frac{1}{r}dr(\sqrt{-1}X), for all X X. For a smooth function f f (locally defined) on ℂ \mathbb{C}, we let ∇ f \nabla_{f} be the gradient vector field with respect to g g and X f X_{f} the Hamiltonian vector field. For a 1 1 -form α \alpha (locally defined) on ℂ \mathbb{C}, we let X α X_{\alpha} be the symplectic vector field with respect to ω \omega. We have g ⁡ ( ∇ f, X) = d ​ f ​ ( X) g(\nabla_{f},X)=df(X), ω ⁡ ( X α, X) = − α ⁡ ( X) \omega(X_{\alpha},X)=-\alpha(X), for all X X. We write ϕ α \phi^{\alpha} for the symplectic isotopy generated by X α X_{\alpha}. We obtain

 | ω ⁡ ( X d ​ θ, X) = − d ​ θ ​ ( X) = 1 r ​ d ​ r ​ ( − 1 ​ X) = 1 r ​ g ​ ( ∇ r, − 1 ​ X) = 1 r ​ ω ​ ( ∇ r, X) \omega(X_{d\theta},X)=-d\theta(X)=\frac{1}{r}dr(\sqrt{-1}X)=\frac{1}{r}g(\nabla_{r},\sqrt{-1}X)=\frac{1}{r}\omega(\nabla_{r},X) |  |

and thus X d ​ θ = 1 r ​ ∇ r X_{d\theta}=\frac{1}{r}\nabla_{r}. We deduce an expression of the symplectic isotopy ϕ s d ​ θ \phi^{d\theta}_{s} in the coordinates ( r, θ) (r,\theta):

 | ϕ s d ​ θ ​ ( r, θ) = ( 2 ​ s + r 2, θ). \phi^{d\theta}_{s}(r,\theta)=(\sqrt{2s+r^{2}},\theta). |  |

###### Lemma 5.2.

Let φ: 𝔸 q → ℂ \varphi\colon\mathbb{A}_{q}\to\mathbb{C} be a biholomorphism onto its image A A. Assume that φ \varphi admits a continuous extension φ ¯: 𝔸 q ¯ → A ¯ \overline{\varphi}\colon\overline{\mathbb{A}_{q}}\to\overline{A} and 0 ∉ A ¯ 0\notin\overline{A}. Let θ ~: [q, 1] × [0, 2 ​ π] → ℝ \tilde{\theta}\colon[q,1]\times[0,2\pi]\to\mathbb{R} be a lift of [q, 1] × [0, 2 ​ π] → φ ¯ 𝔸 q → A → 𝜃 ℝ / 2 ​ π ​ ℤ [q,1]\times[0,2\pi]\xrightarrow{\overline{\varphi}}\mathbb{A}_{q}\to A\xrightarrow{\theta}\mathbb{R}/2\pi\mathbb{Z}. Then, there exists a positive real number L ∈ ℝ > 0 L\in\mathbb{R}_{>0} such that

 | 1 2 ​ π ​ ( max { u } × [0, 2 ​ π] ⁡ θ ~ − min { u } × [0, 2 ​ π] ⁡ θ ~) ≤ L \frac{1}{2\pi}\left(\max_{\{u\}\times[0,2\pi]}\tilde{\theta}-\min_{\{u\}\times[0,2\pi]}\tilde{\theta}\right)\leq L |  |

for any u ∈ [q, 1] u\in[q,1]. This L L can be chosen so that

 | L ≤ 1 2 ​ π ​ max ⁡ { max { q } × [0, 2 ​ π] ⁡ θ ~ − min { q } × [0, 2 ​ π] ⁡ θ ~, max { 1 } × [0, 2 ​ π] ⁡ θ ~ − min { 1 } × [0, 2 ​ π] ⁡ θ ~ } + 1. L\leq\frac{1}{2\pi}\max\left\{\max_{\{q\}\times[0,2\pi]}\tilde{\theta}-\min_{\{q\}\times[0,2\pi]}\tilde{\theta},\max_{\{1\}\times[0,2\pi]}\tilde{\theta}-\min_{\{1\}\times[0,2\pi]}\tilde{\theta}\right\}+1. |  |

###### Proof.

By abuse of notation, we write θ \theta for ( q, 1) × [0, 2 ​ π] → 𝔸 q → 𝜃 ℝ (q,1)\times[0,2\pi]\to\mathbb{A}_{q}\xrightarrow{\theta}\mathbb{R}. Let θ ′: ( q, 1) × [0, 2 ​ π] → ℝ \theta^{\prime}\colon(q,1)\times[0,2\pi]\to\mathbb{R} denote the second projection. Then the function θ ~ − θ ′ \tilde{\theta}-\theta^{\prime} defines a harmonic function on 𝔸 q \mathbb{A}_{q}. Let I u ⊂ ℝ I_{u}\subset\mathbb{R} be the image of ∂ 𝔻 u \partial\mathbb{D}_{u} under θ ~ − θ ′ \tilde{\theta}-\theta^{\prime}. We may assume I q ⊂ I 1 I_{q}\subset I_{1} or I 1 ⊂ I q I_{1}\subset I_{q} by adding a harmonic function of the form c ​ log ⁡ r ​ ( c ∈ ℝ) c\log r\ (c\in\mathbb{R}) if necessary. Note that this does not change the length of each I u I_{u}.

By the maximum principal, I u I_{u} is contained in I q ∪ I 1 I_{q}\cup I_{1}. Since the values of θ ′ \theta^{\prime} is contained in [0, 2 ​ π] [0,2\pi], the oscillation is less than or equal to max ⁡ { | I q |, | I 1 | } + 2 ​ π \max\{|I_{q}|,|I_{1}|\}+2\pi, where | I | |I| denotes the length of a interval I ⊂ ℝ I\subset\mathbb{R}. ∎

The essential part of the proof of the following lemma is due to Stéphane Guillermou.

###### Lemma 5.3.

Let φ: 𝔸 q → ℂ \varphi\colon\mathbb{A}_{q}\to\mathbb{C} be a biholomorphism onto its image A A and let L L be a positive real number satisfying the inequality in lemma 5.2. For u ∈ ( q, 1) u\in(q,1), set C u ≔ φ ⁡ ( ∂ 𝔻 u) C_{u}\coloneqq\varphi(\partial\mathbb{D}_{u}) and assume A ⁡ ( C u) ≤ π A(C_{u})\leq\pi for all u ∈ ( q, 1) u\in(q,1). Define C u ′ C^{\prime}_{u} to be the curve rescaled by ϕ d ​ θ \phi^{d\theta} defined above such that A ⁡ ( C u ′) = π A(C^{\prime}_{u})=\pi. Then, for q < u 0 < u 1 < 1 q<u_{0}<u_{1}<1, one has

 | d ⁡ ( F C u 0 ′, F C u 1 ′) ≤ 2 ​ ( L + 1) ​ ( A ⁡ ( C u 1) − A ⁡ ( C u 0)) d(F_{C^{\prime}_{u_{0}}},F_{C^{\prime}_{u_{1}}})\leq 2(L+1)(A(C_{u_{1}})-A(C_{u_{0}})) |  |

after translating F C u 0 ′ F_{C^{\prime}_{u_{0}}} by some constant to the ℝ t / π ​ ℤ \mathbb{R}_{t}/\pi\mathbb{Z} -direction.

###### Proof.

We may assume that 0 ∈ ℂ 0\in\mathbb{C} is contained in the open domain bounded by C u C_{u} for all u ∈ ( q, 1) u\in(q,1). We set r ′ = r ∘ φ − 1 r^{\prime}=r\circ\varphi^{-1}, θ ′ = θ ∘ φ − 1: A → ℝ x \theta^{\prime}=\theta\circ\varphi^{-1}\colon A\to\mathbb{R}_{x}. Hence C u = r ′ − 1 ​ ( u) C_{u}=r^{\prime-1}(u). Since φ \varphi is biholomorphic, we obtain X d ​ θ ′ = 1 r ′ ​ ∇ r ′ X_{d\theta^{\prime}}=\frac{1}{r^{\prime}}\nabla_{r^{\prime}}.

In the following steps from (a) to (d), we will construct a Hamiltonian diffeomorphism that sends C u 0 ′ C^{\prime}_{u_{0}} to C u 1 ′ C^{\prime}_{u_{1}} and estimate the distance d ⁡ ( F C u 0 ′, F C u 1 ′) d(F_{C^{\prime}_{u_{0}}},F_{C^{\prime}_{u_{1}}}) with the Hamiltonian diffeomorphism.

(a) First we will define a time-dependent closed 1 1 -form α = ( α ⁡ ( s)) s ∈ [0, u 1 − u 0] \alpha=(\alpha(s))_{s\in[0,u_{1}-u_{0}]} on A A such that the flow of its symplectic vector field ϕ α \phi^{\alpha} satisfies ϕ s α ​ ( C u 0) = C u 0 + s \phi^{\alpha}_{s}(C_{u_{0}})=C_{{u_{0}}+s} for s ∈ [0, u 1 − u 0] s\in[0,u_{1}-u_{0}]. This condition is satisfied if d ​ r ′ ​ ( X α ⁡ ( s)) = 1 dr^{\prime}(X_{\alpha(s)})=1 on C u 0 + s C_{{u_{0}}+s} for s ∈ [0, u 1 − u 0] s\in[0,u_{1}-u_{0}]. We define a function k k that depends only on s s and θ ′ \theta^{\prime} by

 | k ⁡ ( s, θ ′) ≔ u 0 + s ‖ d ​ r ′ ‖ 2, k(s,\theta^{\prime})\coloneqq\frac{u_{0}+s}{\|dr^{\prime}\|^{2}}, |  |

where ‖ d ​ r ′ ‖ 2 \|dr^{\prime}\|^{2} is a time-dependent function on A A that maps ( r 1 ′, θ 1 ′) (r^{\prime}_{1},\theta^{\prime}_{1}) to the value of ‖ d ​ r ′ ‖ 2 \|dr^{\prime}\|^{2} at ( u 0 + s, θ 1 ′) (u_{0}+s,\theta^{\prime}_{1}). We define

 | α ⁡ ( s) ≔ k ⁡ ( s, θ ′) ​ d ​ θ ′. \alpha(s)\coloneqq k(s,\theta^{\prime})d\theta^{\prime}. |  |

Then, on C u 0 + s C_{u_{0}+s} we have

 | X α ⁡ ( s) = k ⁡ ( s, θ ′) ​ X d ​ θ ′, X_{\alpha(s)}=k(s,\theta^{\prime})X_{d\theta^{\prime}}, |  |

which implies d ​ r ′ ​ ( X α ⁡ ( s)) = 1 dr^{\prime}(X_{\alpha(s)})=1. Moreover, we have d ​ θ ′ ​ ( X α ⁡ ( s)) = 0 d\theta^{\prime}(X_{\alpha(s)})=0 by construction.

(b) Next, we will describe the rescaled curve C u ′ C^{\prime}_{u} more precisely. We have seen that ϕ s d ​ θ ​ ( ∂ 𝔻 u) = ∂ 𝔻 2 ​ s + u 2 \phi^{d\theta}_{s}(\partial\mathbb{D}_{u})=\partial\mathbb{D}_{\sqrt{2s+u^{2}}}. Hence A ⁡ ( ϕ s d ​ θ ​ ( ∂ 𝔻 u)) = A ⁡ ( ∂ 𝔻 u) + 2 ​ π ​ s A(\phi^{d\theta}_{s}(\partial\mathbb{D}_{u}))=A(\partial\mathbb{D}_{u})+2\pi s. Now, for a general Jordan curve C C containing 0 0 in its interior domain and ε > 0 \varepsilon>0 small, ϕ s d ​ θ \phi^{d\theta}_{s} is defined and symplectic outside 𝔻 ε ¯ \overline{\mathbb{D}_{\varepsilon}}. Hence we deduce the general equality

 | A ⁡ ( ϕ s d ​ θ ​ ( C)) = A ⁡ ( C) + 2 ​ π ​ s. A(\phi^{d\theta}_{s}(C))=A(C)+2\pi s. |  |

Thus, we can write

 | C u ′ = ϕ T ⁡ ( u) d ​ θ ​ ( C u) with T ⁡ ( u) ≔ 1 2 ​ π ​ ( π − A ⁡ ( C u)). C^{\prime}_{u}=\phi^{d\theta}_{T(u)}(C_{u})\quad\text{with}\quad T(u)\coloneqq\frac{1}{2\pi}(\pi-A(C_{u})). |  |

(c) We will construct a Hamiltonian diffeomorphism that sends C u 0 ′ C^{\prime}_{u_{0}} to C u 1 ′ C^{\prime}_{u_{1}}. We define a symplectomorphism ψ ≔ ϕ T ⁡ ( u 0) d ​ θ \psi\coloneqq\phi^{d\theta}_{T(u_{0})} and a time-dependent closed 1 1 -form β \beta by β ⁡ ( s) ≔ ( ψ − 1) ∗ ​ α ​ ( s) \beta(s)\coloneqq(\psi^{-1})^{*}\alpha(s). We set a ⁡ ( s) = A ⁡ ( C s) a(s)=A(C_{s}) and define time-dependent function and 1-form

 | b ( s) ≔ − 1 2 ​ π d ​ a d ​ s ( u 0 + s), d Θ ( s) = b ( s) d θ ( s ∈ [0, u 1 − u 0]). b(s)\coloneqq-\frac{1}{2\pi}\frac{da}{ds}(u_{0}+s),\quad d\Theta(s)=b(s)d\theta\quad(s\in[0,u_{1}-u_{0}]). |  |

Since

 | ∫ 0 s b ⁡ ( s ′) ​ d ​ s ′ = 1 2 ​ π ​ ( a ⁡ ( u 0) − a ⁡ ( u 0 + s)) = T ⁡ ( u 0 + s) − T ⁡ ( u 0), \int_{0}^{s}b(s^{\prime})\,ds^{\prime}=\frac{1}{2\pi}(a(u_{0})-a(u_{0}+s))=T(u_{0}+s)-T(u_{0}), |  |

we obtain ϕ s d ​ Θ = ϕ T ⁡ ( u 0 + s) − T ⁡ ( u 0) d ​ θ \phi^{d\Theta}_{s}=\phi^{d\theta}_{T(u_{0}+s)-T(u_{0})}. For s ∈ [0, u 1 − u 0] s\in[0,u_{1}-u_{0}], we define

 | ( d ​ Θ ​ ♯ ​ β) ​ ( s) ≔ d ​ Θ ​ ( s) + ( ( ϕ s d ​ Θ) − 1) ∗ ​ β ​ ( s) = d ​ Θ ​ ( s) + ( ( ϕ T ⁡ ( u 0 + s) − T ⁡ ( u 0) d ​ θ) − 1) ∗ ​ α ​ ( s), (d\Theta\sharp\beta)(s)\coloneqq d\Theta(s)+((\phi^{d\Theta}_{s})^{-1})^{*}\beta(s)=d\Theta(s)+((\phi^{d\theta}_{T(u_{0}+s)-T(u_{0})})^{-1})^{*}\alpha(s), |  |

which is a locally defined time-dependent closed 1 1 -form. We find that

 | ϕ s d ​ Θ ​ ♯ ​ β \displaystyle\phi^{d\Theta\sharp\beta}_{s} | = ϕ s d ​ Θ ∘ ϕ s β \displaystyle=\phi^{d\Theta}_{s}\circ\phi^{\beta}_{s} |  |

 |  | = ϕ T ⁡ ( u 0 + s) − T ⁡ ( u 0) d ​ θ ∘ ψ ∘ ϕ s α ∘ ψ − 1 \displaystyle=\phi^{d\theta}_{T(u_{0}+s)-T(u_{0})}\circ\psi\circ\phi^{\alpha}_{s}\circ\psi^{-1} |  |

 |  | = ϕ T ⁡ ( u 0 + s) d ​ θ ∘ ϕ s α ∘ ( ϕ T ⁡ ( u 0) d ​ θ) − 1, \displaystyle=\phi^{d\theta}_{T(u_{0}+s)}\circ\phi^{\alpha}_{s}\circ(\phi^{d\theta}_{T(u_{0})})^{-1}, |  |

which sends C u 0 ′ C^{\prime}_{u_{0}} to C u 0 + s ′ C^{\prime}_{u_{0}+s}. The exactness of a locally defined closed 1 1 -form is determined by the integrations along closed curves that generate the first homology group of the domain. Since A ⁡ ( C u 0 + s ′) = A ⁡ ( C u 0 ′) A(C^{\prime}_{u_{0}+s})=A(C^{\prime}_{u_{0}}), the integration of ( d ​ Θ ​ ♯ ​ β) ​ ( s) (d\Theta\sharp\beta)(s) along C u 0 + s ′ C^{\prime}_{u_{0}+s} is zero. Thus d ​ Θ ​ ♯ ​ β d\Theta\sharp\beta is a time-dependent locally defined exact 1 1 -form, which can be written as d ​ h 1 dh_{1}. This proves that ϕ u 1 − u 0 d ​ Θ ​ ♯ ​ β \phi^{d\Theta\sharp\beta}_{u_{1}-u_{0}} is the Hamiltonian diffeomorphism ϕ u 1 − u 0 h 1 \phi^{h_{1}}_{u_{1}-u_{0}} that sends C u 0 ′ C^{\prime}_{u_{0}} to C u 1 ′ C^{\prime}_{u_{1}}.

(d) Finally, we will estimate the Hofer norm of ϕ u 1 − u 0 h 1 \phi^{h_{1}}_{u_{1}-u_{0}}. We take a smooth cut-off function on ℂ \mathbb{C} and extend h 1 h_{1} to ℂ \mathbb{C} with the cut-off function.

For any z 1, z 2 ∈ C u 0 + s ′ z_{1},z_{2}\in C_{u_{0}+s}^{\prime}, we take a path in C u 0 + s ′ C_{u_{0}+s}^{\prime} connecting these two points that does not pass θ ′ = 0 \theta^{\prime}=0. Then, by integrating d ​ Θ ​ ♯ ​ β d\Theta\sharp\beta along the path, we get

 | h 1 ​ ( s, z 1) − h 1 ​ ( s, z 2) \displaystyle h_{1}(s,z_{1})-h_{1}(s,z_{2}) | ≤ 1 2 ​ π ​ | b ⁡ ( s) | ​ ( max { u 0 + s } × [0, 2 ​ π] ⁡ θ ~ − min { u 0 + s } × [0, 2 ​ π] ⁡ θ ~) + ∫ θ 1 ′ θ 2 ′ k ⁡ ( s, θ ′) ​ d ​ θ ′, \displaystyle\leq\frac{1}{2\pi}|b(s)|\left(\max_{\{u_{0}+s\}\times[0,2\pi]}\tilde{\theta}-\min_{\{u_{0}+s\}\times[0,2\pi]}\tilde{\theta}\right)+\int_{\theta^{\prime}_{1}}^{\theta^{\prime}_{2}}k(s,\theta^{\prime})\,d\theta^{\prime}, |  |

where ( u 0 + s, θ i ′) (u_{0}+s,\theta_{i}^{\prime}) in the coordinates ( r ′, θ ′) (r^{\prime},\theta^{\prime}) corresponds to the point z i z_{i} for i = 1, 2 i=1,2. The area bounded by the arcs θ ′ \theta^{\prime} is constant or r ′ r^{\prime} is constant joining the points ( u 0, θ i ′) (u_{0},\theta^{\prime}_{i}), ( u 0 + s, θ i ′) (u_{0}+s,\theta^{\prime}_{i}) for i = 1, 2 i=1,2 is written as

 | B ( s, θ 1 ′, θ 2 ′) = ∫ r ′ = u 0 r ′ = u 0 + s ∫ θ ′ = θ 1 ′ θ ′ = θ 2 ′ ω ( ∂ r ′, ∂ θ ′) d θ ′ d r ′. B(s,\theta^{\prime}_{1},\theta^{\prime}_{2})=\int_{r^{\prime}=u_{0}}^{r^{\prime}=u_{0}+s}\int_{\theta^{\prime}=\theta^{\prime}_{1}}^{\theta^{\prime}=\theta^{\prime}_{2}}\omega(\partial_{r^{\prime}},\partial_{\theta^{\prime}})\,d\theta^{\prime}dr^{\prime}. |  |

By using ω ( ∂ r ′, ∂ θ ′) = ω ( k X d ​ θ ′, ∂ θ ′) = k \omega(\partial_{r^{\prime}},\partial_{\theta^{\prime}})=\omega\left(kX_{d\theta^{\prime}},\partial_{\theta^{\prime}}\right)=k, we have

 | ∂ B ∂ s ( s, θ 1 ′, θ 2 ′) = ∫ θ ′ = θ 1 ′ θ ′ = θ 2 ′ ω ( ∂ r ′, ∂ θ ′) d θ ′ = ∫ θ ′ = θ 1 ′ θ ′ = θ 2 ′ k ( s, θ ′) d θ ′. \frac{\partial B}{\partial s}(s,\theta_{1}^{\prime},\theta^{\prime}_{2})=\int_{\theta^{\prime}=\theta^{\prime}_{1}}^{\theta^{\prime}=\theta^{\prime}_{2}}\omega(\partial_{r^{\prime}},\partial_{\theta^{\prime}})\,d\theta^{\prime}=\int_{\theta^{\prime}=\theta^{\prime}_{1}}^{\theta^{\prime}=\theta^{\prime}_{2}}k(s,\theta^{\prime})\,d\theta^{\prime}. |  |

Since k ⁡ ( s, θ ′) ≥ 0 k(s,\theta^{\prime})\geq 0 and B ⁡ ( s, 0, 2 ​ π) = a ⁡ ( s) − a ⁡ ( u 0) B(s,0,2\pi)=a(s)-a(u_{0}), we obtain the bound

 | ∫ θ 1 ′ θ 2 ′ k ⁡ ( s, θ ′) ​ d ​ θ ′ ≤ d ​ a d ​ s ​ ( s) for any s and θ 1 ′, θ 2 ′. \int_{\theta^{\prime}_{1}}^{\theta^{\prime}_{2}}k(s,\theta^{\prime})\,d\theta^{\prime}\leq\frac{da}{ds}(s)\quad\text{for any $s$ and $\theta^{\prime}_{1},\theta^{\prime}_{2}$.} |  |

Combining this inequality with lemma 5.2, we have

 | h 1 ​ ( s, z 1) − h 1 ​ ( s, z 2) ≤ ( L + 1) ​ d ​ a d ​ s ​ ( u 0 + s) h_{1}(s,z_{1})-h_{1}(s,z_{2})\leq(L+1)\frac{da}{ds}(u_{0}+s) |  |

Hence, we obtain

 | ∫ 0 u 1 − u 0 ( max C u 0 + s ′ ⁡ h 1 ​ ( s) − min C u 0 + s ′ ⁡ h 1 ​ ( s)) ​ 𝑑 s ≤ ( L + 1) ​ ( a ⁡ ( u 1) − a ⁡ ( u 0)). \int_{0}^{u_{1}-u_{0}}\left(\max_{C^{\prime}_{u_{0}+s}}h_{1}(s)-\min_{C^{\prime}_{u_{0}+s}}h_{1}(s)\right)\,ds\leq(L+1)(a(u_{1})-a(u_{0})). |  |

The bound is equal to ( L + 1) ​ ( A ⁡ ( C u 1) − A ⁡ ( C u 0)) (L+1)(A(C_{u_{1}})-A(C_{u_{0}})).

We will finish the proof of the lemma. The time-depending function ( p, p ′) ↦ h 1 ​ ( p, s) + h 1 ​ ( p ′, s) (p,p^{\prime})\mapsto h_{1}(p,s)+h_{1}(p^{\prime},s) on ℂ × ℂ \mathbb{C}\times\mathbb{C} generates a flow that sends C u 0 ′ × C u 0 ′ C^{\prime}_{u_{0}}\times C^{\prime}_{u_{0}} to C u 1 ′ × C u 1 ′ C^{\prime}_{u_{1}}\times C^{\prime}_{u_{1}} at time s = u 1 − u 0 s=u_{1}-u_{0}. Hence, by [AI24, Thm. A.2], there exists c ∈ ℝ c\in\mathbb{R} such that

 | d ⁡ ( F C u 0 ′, T c ​ F C u 1 ′) \displaystyle d(F_{C^{\prime}_{u_{0}}},T_{c}F_{C^{\prime}_{u_{1}}}) | ≤ 2 ​ ∫ 0 u 1 − u 0 ( max C u 0 + s ′ ⁡ h 1 ​ ( s) − min C u 0 + s ′ ⁡ h 1 ​ ( s)) ​ 𝑑 s \displaystyle\leq 2\int_{0}^{u_{1}-u_{0}}\left(\max_{C^{\prime}_{u_{0}+s}}h_{1}(s)-\min_{C^{\prime}_{u_{0}+s}}h_{1}(s)\right)\,ds |  |

 |  | ≤ 2 ​ ( L + 1) ​ ( A ⁡ ( C u 1) − A ⁡ ( C u 0)). \displaystyle\leq 2(L+1)(A(C_{u_{1}})-A(C_{u_{0}})). |  |

This completes the proof. ∎

###### Remark 5.4.

Note that we can define a sheaf quantization F C F_{C} for any Jordan curve C C by proposition 5.1.

###### Remark 5.5.

Note that there are Jordan curves whose images have positive measure [Leb03, Osg03]. See also [NV22]. If the measure of C C is non-zero, C C inscribes a θ \theta -rectangle for any θ ∈ ( 0, π) \theta\in(0,\pi) by Lebesgue’s density theorem.

Now we prove theorem 1.1.

###### Proof of theorem 1.1.

We may assume that the measure of C C is zero by remark 5.5. By scaling, we may also assume that the area of the open domain bounded by C C is π \pi, that is, A ⁡ ( C) = π A(C)=\pi. Let ( c n) n (c_{n})_{n} be a sequence of smooth Jordan curves that satisfies the conditions in theorem 1.1. Let B n ≔ A ⁡ ( C n) B_{n}\coloneqq A(C_{n}) be the area of the open domain bounded by C n C_{n}. Since B n → π B_{n}\to\pi as n → ∞ n\to\infty, by scaling C n C_{n} by a factor of π / B n \sqrt{\pi/B_{n}} with respect to the origin, we may assume B n = π B_{n}=\pi while keeping ( c n) n (c_{n})_{n} converges to c c. By the first part of proposition 5.1, the sequence of sheaf quantizations ( F C n) n (F_{C_{n}})_{n} is a Cauchy sequence, which defines a limit object F F. Combining the condition (2) in theorem 1.1 with proposition 2.3, we find that T a ​ SS ⁡ ( F) ∩ SS ⁡ ( F) = ∅ T_{a}\CMS(F)\cap\CMS(F)=\varnothing for a ∈ ℝ ∖ π ​ ℤ a\in\mathbb{R}\setminus\pi\mathbb{Z}.

Since the measure of C C is zero, we can construct a Hamiltonian homeomorphism with compact support ϕ \phi on T ∗ ​ ℝ T^{*}\mathbb{R} such that C = ϕ ⁡ ( C 0) C=\phi(C_{0}). Note that the set of compactly supported Hamiltonian homeomorphism coincides with the set of compactly supported area-preserving homeomorphisms, whose proof can be found in [Oh06, Sik07]. Such a compactly supported area-preserving homeomorphisms exists by theorems by Schönflies and Oxtoby–Ulam [OU41]. Then, by the second part of proposition 5.1, we have F ≃ F C ≔ 𝒦 ⁡ ( ϕ × ϕ) ​ F C 0 F\simeq F_{C}\coloneqq\mathcal{K}(\phi\times\phi)F_{C_{0}}.

Hence, the result follows from theorem 4.1. ∎

###### Remark 5.6.

The smooth approximation assumed in theorem 1.1 can be weakened to an approximation by C 1 C^{1} -curves. Furthermore, the “primitive” for curves satisfying the assumptions of theorem 1.1 is unique regardless of how the approximating sequence is chosen. This uniqueness follows from the fact that the sheaf quantization is unique and the primitive can be recovered from its conic microsupport.

It follows the following observation. Let ( c n: S 1 → ℝ 2) n (c_{n}\colon S^{1}\to\mathbb{R}^{2})_{n} be a sequence of continuous Jordan curves with

1. (1)

( c n) (c_{n}) converges to a Jordan curve c c in the C 0 C^{0} -sense,

2. (2)

each c n c_{n} satisfies the assumption of theorem 1.1 and hence “primitive” f n f_{n} is determined up to constant.

3. (3)

( f n) n (f_{n})_{n} converges to a continuous function f f uniformly on every compact subset.

Then the Jordan curve c c satisfies the assumptions of theorem 4.1.

###### Remark 5.7.

As mentioned in remark 5.5, a Jordan curve with positive measure inscribes a θ \theta -rectangle for any θ ∈ ( 0, π) \theta\in(0,\pi). Thus, the rectangular peg problem for any Jordan curve would be solved affirmatively if the cohomology vanishing in remark 4.2 for Jordan curves with measure zero.

### 5.2 Rectifiable curves

Now we give an affirmative answer to the rectangle peg problem for rectifiable curves.

###### Proposition 5.8.

A rectifiable Jordan curve C C satisfies the assumptions in theorem 1.1.

###### Proof.

Let D D be the open domain bounded by C C. By the Riemann mapping theorem and the Carathéodory theorem, we can construct a homeomorphism φ ¯: 𝔻 1 ¯ → D ¯ \overline{\varphi}\colon\overline{\mathbb{D}_{1}}\to\overline{D} whose restriction to 𝔻 1 \mathbb{D}_{1} is a holomorphic mapping. For n ∈ ℤ ≥ 2 n\in\mathbb{Z}_{\geq 2}, we define a smooth Jordan curve c n ≔ φ ¯ | ∂ 𝔻 1 − 1 / n c_{n}\coloneqq\overline{\varphi}|_{\partial\mathbb{D}_{1-1/n}}. By the Riesz–Privalov theorem, a precise form of the Riemann mapping theorem for a domain with rectifiable boundary [Pom92, Thm. 6.8], we find that the lengths of c n c_{n} converge to the length of c c. Then, by the lemmas for proving Green’s theorem for rectifiable curves [Apo57, 10–14] 3 3 3 Note that this discussion is only written in the first edition and has been removed from the second edition onward. An overview of the discussion can also be found on Wikipedia [Wik]., we find that the sequence of smooth Jordan curve ( c n) n (c_{n})_{n} satisfies the conditions in theorem 1.1. ∎

###### Corollary 5.9.

Every rectifiable Jordan curve inscribes a θ \theta -rectangle for any θ ∈ ( 0, π) \theta\in(0,\pi).

### 5.3 Locally monotone curves

Stromquist [Str89] proved the existence of an inscribed square for a large class of Jordan curves, which he called locally monotone. We will also extend his result with the use of theorem 1.1.

Let us first recall the definition of locally monotone curves. Through the identification S 1 ≃ ℝ / 2 ​ π ​ ℤ S^{1}\simeq\mathbb{R}/2\pi\mathbb{Z}, we regard a Jordan curve c: S 1 → ℝ 2 c\colon S^{1}\to\mathbb{R}^{2} as a 2 ​ π 2\pi -periodic map c: ℝ → ℝ 2 c\colon\mathbb{R}\to\mathbb{R}^{2}.

###### Definition 5.10 ( [Str89, §6]).

A Jordan curve c: S 1 → ℝ 2 c\colon S^{1}\to\mathbb{R}^{2} is said to be *locally monotone*if for any p ∈ ℝ p\in\mathbb{R}, there exist an open connected neighborhood U p ⊂ ℝ U_{p}\subset\mathbb{R} of p p and a unit vector v → ​ ( p) \vec{v}(p) such that the inner product q ↦ c ​ ( q) ⋅ v → ​ ( p) q\mapsto c(q)\cdot\vec{v}(p) is a strictly monotone function on U p U_{p}.

###### Proposition 5.11.

A locally monotone Jordan curve C C satisfies the assumptions in theorem 1.1.

###### Proof.

Let p ∈ ℝ p\in\mathbb{R} and define g p ​ ( q) ≔ c ⁡ ( q) ⋅ v → ​ ( p) g_{p}(q)\coloneqq c(q)\cdot\vec{v}(p), a strictly monotone function on U p U_{p}. We define a function f p f_{p} on U p U_{p} as follows:

 | f p ​ ( q) ≔ ∫ g p ​ ( p) g p ​ ( q) c ⁡ ( g p − 1 ​ ( q ′)) ⋅ n → ​ ( p) ​ d ​ q ′ + h p ​ ( c ⁡ ( q)) ( q ∈ U p), f_{p}(q)\coloneqq\int_{g_{p}(p)}^{g_{p}(q)}c(g_{p}^{-1}(q^{\prime}))\cdot\vec{n}(p)\,dq^{\prime}+h_{p}(c(q))\quad(q\in U_{p}), |  |

where

- •

n → ​ ( p) \vec{n}(p) is a unit vector orthogonal to v → ​ ( p) \vec{v}(p) such that ( v → ​ ( p), n → ​ ( p)) (\vec{v}(p),\vec{n}(p)) forms an oriented basis of ℝ 2 \mathbb{R}^{2};

- •

( x p, ξ p) (x_{p},\xi_{p}) is the coordinate function with respect to the orthonormal basis ( v → ​ ( p), n → ​ ( p)) (\vec{v}(p),\vec{n}(p)); and

- •

h p: ℝ 2 → ℝ h_{p}\colon\mathbb{R}^{2}\to\mathbb{R} is a smooth primitive function of ξ ​ d ​ x − ξ p ​ d ​ x p \xi dx-\xi_{p}dx_{p}.

After choosing appropriate constant shifts, we can glue the family of local functions ( f p: U p → ℝ) p ∈ ℝ (f_{p}\colon U_{p}\to\mathbb{R})_{p\in\mathbb{R}} to get a continuous function f f on ℝ \mathbb{R}. Note that a smooth Jordan curve c c is locally monotone, and in this case f f constructed above is a primitive function of c ∗ ​ λ = c ∗ ​ ( ξ ​ d ​ x) c^{*}\lambda=c^{*}(\xi dx).

We fix a non-negative smooth function χ ∈ C ∞ ​ ( ℝ) \chi\in C^{\infty}(\mathbb{R}) supported on [− 1, 1] [-1,1] such that ∫ ℝ χ ⁡ ( q) ​ 𝑑 q = 1 \int_{\mathbb{R}}\chi(q)\,dq=1. For n ∈ ℤ ≥ 1 n\in\mathbb{Z}_{\geq 1}, we take δ n > 0 \delta_{n}>0 such that | p − p ′ | < δ n |p-p^{\prime}|<\delta_{n} implies ‖ c ⁡ ( p) − c ⁡ ( p ′) ‖ < 1 / n \|c(p)-c(p^{\prime})\|<1/n and define

 | c n ​ ( p) ≔ ∫ ℝ δ n − 1 ​ χ ​ ( δ n − 1 ​ u) ​ c ​ ( p − u) ​ 𝑑 u c_{n}(p)\coloneqq\int_{\mathbb{R}}\delta_{n}^{-1}\chi(\delta_{n}^{-1}u)\,c(p-u)du |  |

for p ∈ ℝ p\in\mathbb{R}. Then c n c_{n} satisfies ‖ c ⁡ ( p) − c n ​ ( p) ‖ < 1 / n \|c(p)-c_{n}(p)\|<1/n for any p ∈ ℝ p\in\mathbb{R} and is a smooth Jordan curve for a sufficiently large n n. In particular, the sequence ( c n) n (c_{n})_{n} converges to c c in the C 0 C^{0} -sense.

We can check from argument in Stromquist [Str89] that the sequence of primitives for c n c_{n} ’s converges to f f. Indeed, by shrinking U p U_{p} if necessary, g n, p ​ ( q) ≔ c n ​ ( q) ⋅ v → ​ ( p) g_{n,p}(q)\coloneqq c_{n}(q)\cdot\vec{v}(p) is strictly monotone on U p U_{p} and the functions c n ​ ( g n, p − 1 ​ ( −)) ⋅ n → ​ ( p) c_{n}(g_{n,p}^{-1}(\mathchar 45))\cdot\vec{n}(p) defined on a neighborhood of g p ​ ( p) g_{p}(p) converge to c ⁡ ( g p − 1 ​ ( −)) ⋅ n → ​ ( p) c(g_{p}^{-1}(\mathchar 45))\cdot\vec{n}(p) in the C 0 C^{0} -sense. ∎

###### Corollary 5.12.

Every locally monotone Jordan curve inscribes a θ \theta -rectangle for any θ ∈ ( 0, π) \theta\in(0,\pi).

## Acknowledgments

During the preparation of this paper, we learned that Stéphane Guillermou had proved a result similar to theorem 1.1. We are grateful to him for generously sharing his insights with us. His ideas have clarified our discussions and improved our results. We thank Tatsuya Miura for letting us know the square peg problem many years ago and the helpful discussions about Jordan curves. We also thank Vincent Humilière for discussions about Jordan curves, Kaoru Ono for helpful comments related to remark 3.6, and Takuya Murayama for some references about conformal mappings. We are grateful to Joshua Evan Greene and Andrew Lobb for pointing out an error in the earlier version. TA is partially supported by JSPS KAKENHI Grant Number JP24K16920. YI is partially supported by JSPS KAKENHI Grant Numbers JP21K13801 and JP22H05107. We are partially supported by JST, CREST Grant Number JPMJCR24Q1, Japan.

## References

- [Apo57] Tom. Apostol “Mathematical analysis: a modern approach to advanced calculus” Addison-Wesley Publishing Co., Inc., Reading, MA, 1957, pp. xii+553
- [AI20] Tomohiro Asano and Yuichi Ike “Persistence-like distance on Tamarkin’s category and symplectic displacement energy” In *J. Symplectic Geom.*18.3, 2020, pp. 613–649
- [AI23] Tomohiro Asano and Yuichi Ike “Sheaf quantization and intersection of rational Lagrangian immersions” In *Annales de l’Institut Fourier*73.4, 2023, pp. 1533–1587 DOI: [https://doi.org/10.5802/aif.3554][3]
- [AI24] Tomohiro Asano and Yuichi Ike “Completeness of derived interleaving distances and sheaf quantization of non-smooth objects” In *Mathematische Annalen*390, 2024, pp. 2991–3037
- [CKNS24] Laurent Côté, Christopher Kuo, David Nadler and Vivek Shende “The microlocal Riemann-Hilbert correspondence for complex contact manifolds”, 2024 arXiv: [2406.16222 [math.SG]][4]
- [Emc16] Arnold Emch “On Some Properties of the Medians of Closed Continuous Curves Formed by Analytic Arcs” In *Amer. J. Math.*38.1, 1916, pp. 6–18 DOI: [10.2307/2370541][5]
- [FG23] Peter Feller and Marco Golla “Non-orientable slice surfaces and inscribed rectangles” In *Ann. Sc. Norm. Super. Pisa Cl. Sci. (5)*24.3, 2023, pp. 1463–1485
- [FOOO09] Kenji Fukaya, Yong-Geun Oh, Hiroshi Ohta and Kaoru Ono “Lagrangian intersection Floer theory: anomaly and obstruction. Part I” 46, AMS/IP Studies in Advanced Mathematics American Mathematical Society, Providence, RI; International Press, Somerville, MA, 2009, pp. xii+396
- [GPS24] Sheel Ganatra, John Pardon and Vivek Shende “Microlocal Morse theory of wrapped Fukaya categories” In *Ann. of Math. (2)*199.3, 2024, pp. 943–1042 DOI: [10.4007/annals.2024.199.3.1][6]
- [Gao24] Zhen Gao “Generic doubling of rectangular pegs”, 2024 arXiv: [2404.13209 [math.SG]][7]
- [GM05] John. Garnett and Donald. Marshall “Harmonic measure” 2, New Mathematical Monographs Cambridge University Press, Cambridge, 2005, pp. xvi+571 DOI: [10.1017/CBO9780511546617][8]
- [GL21] Joshua Greene and Andrew Lobb “The rectangular peg problem” In *Ann. of Math. (2)*194.2, 2021, pp. 509–517 DOI: [10.4007/annals.2021.194.2.4][9]
- [GL23] Joshua Greene and Andrew Lobb “Cyclic quadrilaterals and smooth Jordan curves” In *Invent. Math.*234.3, 2023, pp. 931–935 DOI: [10.1007/s00222-023-01212-6][10]
- [GL24] Joshua Greene and Andrew Lobb “Floer homology and square pegs”, 2024 arXiv: [2404.05179 [math.SG]][11]
- [GL24a] Joshua Greene and Andrew Lobb “Polynomial Inscriptions”, 2024 arXiv: [2412.09546 [math.SG]][12]
- [GL24b] Joshua Greene and Andrew Lobb “Square pegs between two graphs”, 2024 arXiv: [2407.07798 [math.SG]][13]
- [Gui12] Stéphane Guillermou “Quantization of conic Lagrangian submanifolds of cotangent bundles”, 2012 arXiv: [1212.5818v2 [math.SG]][14]
- [Gui23] Stéphane Guillermou “Sheaves and symplectic geometry of cotangent bundles” In *Astérisque*, 2023, pp. x+274 DOI: [10.24033/ast.1199][15]
- [GKS12] Stéphane Guillermou, Masaki Kashiwara and Pierre Schapira “Sheaf quantization of Hamiltonian isotopies and applications to nondisplaceability problems” In *Duke Math. J.*161.2, 2012, pp. 201–245 DOI: [10.1215/00127094-1507367][16]
- [GV24] Stéphane Guillermou and Claude Viterbo “The singular support of sheaves is γ \gamma -coisotropic” In *Geom. Funct. Anal.*34.4, 2024, pp. 1052–1113 DOI: [10.1007/s00039-024-00682-x][17]
- [Hug18] Cole Hugelmeyer “Every smooth Jordan curve has an inscribed rectangle with aspect ratio equal to 3 \sqrt{3} ”, 2018 arXiv: [1803.07417 [math.MG]][18]
- [Hug21] Cole Hugelmeyer “Inscribed rectangles in a smooth Jordan curve attain at least one third of all aspect ratios” In *Ann. of Math. (2)*194.2, 2021, pp. 497–508 DOI: [10.4007/annals.2021.194.2.3][19]
- [Hug24] Cole Hugelmeyer “A Solution to the Periodic Square Peg Problem”, 2024 arXiv: [2407.20412 [math.SG]][20]
- [Ike19] Yuichi Ike “Compact exact Lagrangian intersections in cotangent bundles via sheaf quantization” In *Publ. Res. Inst. Math. Sci.*55.4, 2019, pp. 737–778 DOI: [10.4171/PRIMS/55-4-3][21]
- [IK23] Yuichi Ike and Tatsuki Kuwagaki “Microlocal categories over Novikov rings”, 2023 arXiv: [2307.01561 [math.SG]][22]
- [Jin20] Xin Jin “Microlocal sheaf categories and the J J -homomorphism”, 2020 arXiv: [2004.14270 [math.SG]][23]
- [JT17] Xin Jin and David Treumann “Brane structures in microlocal sheaf theory” In *arXiv preprint, [arXiv:1704.04291 [math.SG]][24]*, 2017
- [Kas89] Masaki Kashiwara “Representation theory and D D -modules on flag varieties” Orbites unipotentes et représentations, III In *Astérisque*, 1989, pp. 955–109
- [KS90] Masaki Kashiwara and Pierre Schapira “Sheaves on manifolds” 292, Grundlehren der Mathematischen Wissenschaften Springer-Verlag, Berlin, 1990, pp. x+512
- [KS18] Masaki Kashiwara and Pierre Schapira “Persistent homology and microlocal sheaf theory” In *Journal of Applied and Computational Topology*2.1-2 Springer, 2018, pp. 83–113
- [Kuo23] Christopher Kuo “Wrapped sheaves” In *Adv. Math.*415, 2023, pp. Paper No. 10888271 DOI: [10.1016/j.aim.2023.108882][25]
- [KL22] Christopher Kuo and Wenyuan Li “Spherical adjunction and Serre functor from microlocalization”, 2022 arXiv: [2210.06643 [math.SG]][26]
- [KSZ23] Christopher Kuo, Vivek Shende and Bingyu Zhang “On the Hochschild cohomology of Tamarkin categories”, 2023 arXiv: [2312.11447 [math.SG]][27]
- [Leb03] H. Lebesgue “Sur le problème des aires” In *Bull. Soc. Math. France*31, 1903, pp. 197–203
- [Mat14] Benjamin Matschke “A survey on the square peg problem” In *Notices Amer. Math. Soc.*61.4, 2014, pp. 346–352 DOI: [10.1090/noti1100][28]
- [Mey81] Mark. Meyerson “Balancing acts” In *Topology Proc.*6.1, 1981, pp. 59–75
- [NS20] David Nadler and Vivek Shende “Sheaf quantization in Weinstein symplectic manifolds”, 2020 arXiv: [2007.10154 [math.SG]][29]
- [NV22] Maria Nasso and Aljoša Volčič “Area-filling curves” In *Arch. Math. (Basel)*118.5, 2022, pp. 485–495 DOI: [10.1007/s00013-022-01704-6][30]
- [Oh06] Yong-Geun Oh “ C 0 C^{0} -coerciveness of Moser’s problem and smoothing area preserving homeomorphisms”, 2006 arXiv: [math/0601183 [math.DS]][31]
- [Osg03] William. Osgood “A Jordan curve of positive area” In *Trans. Amer. Math. Soc.*4.1, 1903, pp. 107–112 DOI: [10.2307/1986455][32]
- [OU41] J.. Oxtoby and S.. Ulam “Measure-preserving homeomorphisms and metrical transitivity” In *Ann. of Math. (2)*42, 1941, pp. 874–920 DOI: [10.2307/1968772][33]
- [Pom92] Ch. Pommerenke “Boundary behaviour of conformal maps” 299, Grundlehren der mathematischen Wissenschaften [Fundamental Principles of Mathematical Sciences] Springer-Verlag, Berlin, 1992, pp. x+300 DOI: [10.1007/978-3-662-02770-7][34]
- [Sch44] Lev.. Schnirelman “On certain geometrical properties of closed curves” In *Uspehi Matem. Nauk*10, 1944, pp. 34–44
- [Sei00] Paul Seidel “Graded Lagrangian submanifolds” In *Bull. Soc. Math. France*128.1, 2000, pp. 103–149
- [Sey12] Sobhan Seyfaddini “Descent and C 0 C^{0} -rigidity of spectral invariants on monotone symplectic manifolds” In *Journal of Topology and Analysis*4.04 World Scientific, 2012, pp. 481–498
- [STZ17] Vivek Shende, David Treumann and Eric Zaslow “Legendrian knots and constructible sheaves” In *Invent. Math.*207.3, 2017, pp. 1031–1133 DOI: [10.1007/s00222-016-0681-5][35]
- [Sik07] Jean-Claude Sikorav “Approximation of a volume-preserving homeomorphism by a volume-preserving diffeomorphism” Accessed on December 25, 2024, 2007 URL: [https://perso.ens-lyon.fr/jean-claude.sikorav/textes/2007volume][36]
- [Str89] Walter Stromquist “Inscribed squares and square-like quadrilaterals in closed curves” In *Mathematika*36.2, 1989, pp. 187–197 DOI: [10.1112/S0025579300013061][37]
- [Tao17] Terence Tao “An integration approach to the Toeplitz square peg problem” In *Forum of Mathematics, Sigma*5, 2017, pp. e30 DOI: [10.1017/fms.2017.23][38]
- [Toe11] Otto Toeplitz “Über einige aufgaben der analysis situs” In *erhandlungen der Schweizerischen Naturforschenden Gesellschaft in Solothurn*4.197, 1911
- [Vol25] Marco Volpe “The six operations in topology” In *J. Topol.*18.4, 2025, pp. Paper No. e70050 DOI: [10.1112/topo.70050][39]
- [Wik] Wikipedia authors “Green’s theorem” Accessed on December 25, 2024 URL: [https://en.wikipedia.org/wiki/Green][40]

Tomohiro Asano: Department of Mathematics, Kyoto University, Kitashirakawa-Oiwake-Cho, Sakyo-ku, 606-8502, Kyoto, Japan.

E-mail address: tasano[at]math.kyoto-u.ac.jp, tomoh.asano[at]gmail.com

Yuichi Ike: Graduate School of Mathematical Sciences, The University of Tokyo, 3-8-1 Komaba Meguro-ku Tokyo 153-8914, Japan.

E-mail address: ike[at]ms.u-tokyo.ac.jp, yuichi.ike.1990[at]gmail.com


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: https://dx.doi.org/https://doi.org/10.5802/aif.3554
[4]: https://arxiv.org/pdf/2406.16222
[5]: https://dx.doi.org/10.2307/2370541
[6]: https://dx.doi.org/10.4007/annals.2024.199.3.1
[7]: https://arxiv.org/pdf/2404.13209
[8]: https://dx.doi.org/10.1017/CBO9780511546617
[9]: https://dx.doi.org/10.4007/annals.2021.194.2.4
[10]: https://dx.doi.org/10.1007/s00222-023-01212-6
[11]: https://arxiv.org/pdf/2404.05179
[12]: https://arxiv.org/pdf/2412.09546
[13]: https://arxiv.org/pdf/2407.07798
[14]: https://arxiv.org/pdf/1212.5818v2
[15]: https://dx.doi.org/10.24033/ast.1199
[16]: https://dx.doi.org/10.1215/00127094-1507367
[17]: https://dx.doi.org/10.1007/s00039-024-00682-x
[18]: https://arxiv.org/pdf/1803.07417
[19]: https://dx.doi.org/10.4007/annals.2021.194.2.3
[20]: https://arxiv.org/pdf/2407.20412
[21]: https://dx.doi.org/10.4171/PRIMS/55-4-3
[22]: https://arxiv.org/pdf/2307.01561
[23]: https://arxiv.org/pdf/2004.14270
[24]: https://arxiv.org/pdf/1704.04291
[25]: https://dx.doi.org/10.1016/j.aim.2023.108882
[26]: https://arxiv.org/pdf/2210.06643
[27]: https://arxiv.org/pdf/2312.11447
[28]: https://dx.doi.org/10.1090/noti1100
[29]: https://arxiv.org/pdf/2007.10154
[30]: https://dx.doi.org/10.1007/s00013-022-01704-6
[31]: https://arxiv.org/pdf/math/0601183
[32]: https://dx.doi.org/10.2307/1986455
[33]: https://dx.doi.org/10.2307/1968772
[34]: https://dx.doi.org/10.1007/978-3-662-02770-7
[35]: https://dx.doi.org/10.1007/s00222-016-0681-5
[36]: https://perso.ens-lyon.fr/jean-claude.sikorav/textes/2007volume
[37]: https://dx.doi.org/10.1112/S0025579300013061
[38]: https://dx.doi.org/10.1017/fms.2017.23
[39]: https://dx.doi.org/10.1112/topo.70050
[40]: https://en.wikipedia.org/wiki/Green
