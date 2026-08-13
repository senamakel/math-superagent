<!-- source: https://ar5iv.labs.arxiv.org/html/0711.3533 | converted from HTML -->

[0711.3533] Non-dense subsets of varieties in a power of an elliptic curve

# Non-dense subsets of varieties
in a power of an elliptic curve

Evelina Viada 1 1 1 Evelina Viada, Université de Fribourg Suisse, Pérolles, Département de Mathématiques, Chemin du Musée 23, CH-1700 Fribourg, Switzerland, viada@math.ethz.ch, evelina.viada@unifr.ch. 2 2 2 Supported by the SNF (Swiss National Science Foundation). 3 3 3 Mathematics Subject classification (2000): 14H52, 11G50, 14K12 and 11D45.
Key words: Elliptic curves, Heights, Subvarieties, Diophantine approximation.

Let E E be an elliptic curve without C.M. defined over ℚ ¯ \overline{\mathbb{Q}}. We show that on a transverse d d -dimensional variety V ⊂ E g V\subset E^{g}, the set of algebraic points of bounded height which are close to the union of all algebraic subgroups of E g E^{g} of codimension d + 1 d+1 translated by a point in a subgroup Γ \Gamma of E g E^{g} of finite rank, is non-Zariski dense in V V. The notion of close is defined using a height function. If Γ = 0 \Gamma=0, it is sufficient to assume that V V is weak-transverse. This result is optimal with respect to the codimension of the algebraic subgroups.

The method is based on an essentially optimal effective version of the Bogomolov Conjecture. Such an effective result is proven for subvarieties of E g E^{g}. If we assume that the sets have bounded height, then we can prove that they are not Zariski dense. A conjecture, known in some special cases, claims that the sets in question have bounded height. We prove here a new case. In conclusion, our results prove a generalized case of a conjecture by Zilber and by Pink in E g E^{g}.

## 1. introduction

In this article all algebraic varieties are defined over ℚ ¯ \overline{\mathbb{Q}} and we consider only algebraic points. Denote by A A an abelian variety of dimension g g. Consider a proper irreducible algebraic subvariety V V of A A of dimension d d. We say that:

- •

V V is transverse, if V V is not contained in any translate of a proper algebraic subgroup of A A.

- •

V V is weak-transverse, if V V is not contained in any proper algebraic subgroup of A A.

Given an integer r r with 1 ≤ r ≤ g 1\leq r\leq g and a subset F F of A A, we define the set

 | S r ​ ( V, F) = V ∩ ⋃ cod ​ B ≥ r ( B + F), S_{r}(V,F)=V\cap\bigcup_{\mathrm{cod}B\geq r}(B+F), |  |

where B B varies over all abelian subvarieties of A A of codimension at least r r and

 | B + F = { b + f: b ∈ B, f ∈ F }. B+F=\{b+f\,\,\,:\,\,\,b\in B,\,\,\,f\in F\}. |  |

Note that

 | S r + 1 ​ ( V, F) ⊂ S r ​ ( V, F). S_{r+1}(V,F)\subset S_{r}(V,F). |  |

We denote the set S r ​ ( V, A Tor) S_{r}(V,A_{\rm Tor}) simply by S r ​ ( V) S_{r}(V), where A Tor A_{\rm Tor} is the torsion of A A. For convenience, for r > g r>g we define S r ​ ( V, F) = ∅ S_{r}(V,F)=\emptyset and for V e V^{e} a subset of V V we define

 | S r ​ ( V e, F) = V e ∩ S r ​ ( V, F). S_{r}(V^{e},F)=V^{e}\cap S_{r}(V,F). |  |

We ask for which sets F F and integers r r the set S r ​ ( V, F) S_{r}(V,F) has bounded height or is non-Zariski dense in V V.

Depending on the choice of F F, the set S g ​ ( V, F) S_{g}(V,F) appears in the literature in the context of the Mordell-Lang, of the Manin-Mumford and of the Bogomolov Conjectures. More recently Bombieri, Masser and Zannier [2] proved that for a transverse curve in a torus, the set S 2 ​ ( C) S_{2}(C) is finite. They investigated for the first time intersections with the union of all algebraic subgroups of a given codimension. This opens a vast number of conjectures for subvarieties of semi-abelian varieties.

In this paper we consider a variety in a power of an elliptic curve. In the first part of this work we study the non-density of S d + 1 ​ ( V, ⋅) S_{d+1}(V,\cdot), the last part is dedicated to its height. Let E E be an elliptic curve without C.M. Consider on E g E^{g} the line bundle ℒ \mathcal{L} given as tensor product of the pull backs via the natural projections of a symmetric ample line bundle on E E. We fix on E g E^{g} a semi-norm | | ⋅ | | ||\cdot|| induced by the Néron-Tate height on E E. For ε ≥ 0 \varepsilon\geq 0, we denote

 | 𝒪 ε = { ξ ∈ E g: ‖ ξ ‖ ≤ ε }. \mathcal{O}_{\varepsilon}=\{\xi\in E^{g}:||\xi||\leq\varepsilon\}. |  |

We denote by Γ \Gamma a subgroup of finite rank in E g E^{g}. We define Γ ε = Γ + 𝒪 ε. \Gamma_{\varepsilon}=\Gamma+\mathcal{O}_{\varepsilon}.

Let V V an irreducible algebraic subvariety of E g E^{g} of dimension d d. For a non negative real K {K}, we define

 | V K = V ∩ 𝒪 K. V_{K}=V\cap\mathcal{O}_{K}. |  |

Our main result is:

###### Theorem 1.1.

For every K ≥ 0 {K}\geq 0 there exists an effective ε > 0 \varepsilon>0 such that:

1. i.

If V V is weak-transverse, S d + 1 ​ ( V K, 𝒪 ε) S_{d+1}(V_{K},\mathcal{O}_{\varepsilon}) is non-Zariski dense in V V.

2. ii.

If V V is transverse, S d + 1 ​ ( V K, Γ ε) S_{d+1}(V_{K},\Gamma_{\varepsilon}) is non-Zariski dense in V V.

Because of the different hypotheses on the variety and the different sets in the thesis, there are no evident implications between the statements i. and ii.

Let us say at once that the theorem is expected to hold for V V instead of V K V_{K}. This is immediately implied by:

###### Conjecture 1.2.

There exist ε > 0 \varepsilon>0 and a non-empty Zariski open subset V u V^{u} of V V such that:

1. i.

If V V is weak-transverse, S d + 1 ​ ( V u, 𝒪 ε) S_{d+1}(V^{u},\mathcal{O}_{\varepsilon}) has bounded height.

2. ii.

If V V is transverse, S d + 1 ​ ( V u, Γ ε) S_{d+1}(V^{u},\Gamma_{\varepsilon}) has bounded height.

The method known to show that the height is bounded relies on a Vojta inequality, unless Γ \Gamma is trivial. This method gives optimal results for curves, while for varieties a hypothesis stronger than transversality are needed. Let V ⊂ E g V\subset E^{g} be a variety of dimension d d such that

(1) |  | dim ( V + B) = min ⁡ ( d + dim B, g) \dim(V+B)=\min(d+\dim B,\,\,\,g) |  |

for all abelian subvarieties B B of E g E^{g}. In this paper we extend the proof of Rémond of Conjecture 1.2 ii. for V V satisfying condition ( 1). In Theorem 6.5, we prove Conjecture 1.2 i. for V × p V\times p where p ∈ E s p\in E^{s} is a point not lying in any proper algebraic subgroup of E s E^{s}. We can then conclude:

###### Theorem 1.3.

For V V satisfying condition ( 1) and p ∈ E s p\in E^{s} a point not lying in any proper algebraic subgroup of E s E^{s}, there exists ε > 0 \varepsilon>0 such that:

1. i.

The set S d + 1 ​ ( V × p, 𝒪 ε) S_{d+1}(V\times p,\mathcal{O}_{\varepsilon}) is non-Zariski dense in V × p V\times p.

2. ii.

The set S d + 1 ​ ( V, Γ ε) S_{d+1}(V,\Gamma_{\varepsilon}) is non-Zariski dense in V V.

In section 2, we clarify that, up to an isogeny of E n E^{n}, a weak-transverse variety in E n E^{n} has the shape V × p V\times p for V V transverse in some E g E^{g} and p p a point in E n − g E^{n-g} not lying in any proper algebraic subgroup of E n − g E^{n-g}.

For the codimension of the subgroups equal to g g, statements i. and ii. are cases of the Bogomolov Conjecture and the Mordell-Lang plus Bogomolov Conjecture respectively. Let us emphasise that our theorem neither gives a new proof of the Bogomolov Conjecture (as we make use of such a result), nor we get a new proof of the Mordell-Lang Conjecture (as we use a more general Vojta inequality). On the contrary we give a new proof of the Mordell-Lang plus Bogomolov Theorem (Poonen [7]), under the assumption ( 1). In addition, theorem 1.3 part ii. proves a case of a conjecture by Zilber and Pink extended by the Bogomolov Conjecture.

In [14], we proved our main result for a curve in E g E^{g}. A naive extension of the method in [14], would imply a weak form of Theorem 1.1, where the codimension of the algebraic subgroups shall be at least 2 ​ d 2d instead of d + 1 d+1. Here, we improve the method used in [14] obtaining the optimal d + 1 d+1. In the first instance we show that Theorem 1.1 i. and ii. are equivalent, then we prove Theorem 1.1 ii.

###### Theorem 1.4.

Given K ≥ 0 {K}\geq 0 and a positive integer r r, the following statements are equivalent:

1. i.

For V V weak-transverse, there exists ε > 0 \varepsilon>0 such that S r ​ ( V K, 𝒪 ε) S_{r}(V_{K},\mathcal{O}_{\varepsilon}) is non-Zariski dense in V V.

2. ii.

For V V transverse, there exists ε > 0 \varepsilon>0 such that S r ​ ( V K, Γ ε) S_{r}(V_{K},\Gamma_{\varepsilon}) is non-Zariski dense in V V.

We shall then prove Theorem 1.1 part ii. Like for curves, the strategy of the proof is based on two steps. A union of infinitely many sets is non-Zariski dense if:

- (1)

the union can be taken over finitely many sets,

- (2)

all sets in the union are non-Zariski dense.

Part (1) is a typical problem of Diophantine approximation; we approximate an algebraic subgroup with a subgroup of bounded degree (see Proposition 3.3).

The second step (2) is a problem of height theory and its proof relies on an essentially optimal lower bound for the normalized height of a transverse subvariety in E g E^{g}, Theorem 1.5 below. This part is delicate. The dimension of the variety intervenes heavily on the estimates we provide. A fundamental idea is to reduce the problem to the study of varieties with finite stabilizer (see section 4).

We define μ ⁡ ( V) \mu(V) as the supremum of the reals ϵ ⁡ ( V) \epsilon(V) such that S g ​ ( V, 𝒪 ϵ ⁡ ( V)) = V ∩ 𝒪 ϵ ⁡ ( V) S_{g}(V,\mathcal{O}_{\epsilon(V)})=V\cap\mathcal{O}_{\epsilon(V)} is non-Zariski dense in V V. Work by Ullmo [12] and Zhang [15] proves the Bogomolov Conjecture. This shows that μ ⁡ ( V) > 0 \mu(V)>0, for V V transverse. A first effective lower bound for μ ⁡ ( V) \mu(V) is provided by S. David and P. Philippon [3] Theorem 1.2. The type of bounds we need are an elliptic analogue of Amoroso and David [1] Theorem 1.4. Such a result is proven by Galateau in his Ph.D. thesis for d ≥ g − 2 d\geq g-2, and in a preprint [4] for varieties in a product of elliptic curves with or without C.M. (he gives estimate for the square of μ ⁡ ( V) \mu(V)).

###### Theorem 1.5 (Bogomolov type bound, Galateau [4]).

Let V V be a transverse subvariety of E g E^{g} of codimension codV \rm codV defined over ℚ ¯ \overline{\mathbb{Q}}. For η > 0 \eta>0, there exists a positive effective constant c ⁡ ( E g, η) c(E^{g},\eta) depending on the ambient variety and η \eta, such that for

 | ϵ ⁡ ( V, η) = c ⁡ ( E g, η) ( deg ℒ ⁡ V) 1 2 ​ c ​ o ​ d ​ V + η \epsilon(V,\eta)=\frac{c(E^{g},\eta)}{(\deg_{{\mathcal{L}}}V)^{\frac{1}{2\rm codV}+\eta}} |  |

the set

 | V ⁡ ( ℚ ¯) ∩ 𝒪 ϵ ⁡ ( V, η) V(\overline{\mathbb{Q}})\cap\mathcal{O}_{\epsilon(V,\eta)} |  |

is non-Zariski dense in V V.

The bound ϵ ⁡ ( V, η) \epsilon(V,\eta) depends on the invariants of the ambient variety and on the degree of V V. The quasi optimal dependence on the degree of V V and the non-dependece on the field of definition and height of V V are of crucial importance for our application.

The non-Zariski density for transverse varieties has often been investigated with the method introduced by Bombieri, Masser and Zannier in [2]. To show the non-density property they use an essentially optimal Generalized Lehmer Conjecture. In [13] we applied their method to a transverse curve, Γ = 0 \Gamma=0 and ε = 0 \varepsilon=0. In [8] Rémond and the author extended the method to transverse curves, ε = 0 \varepsilon=0 and any Γ \Gamma of finite rank. In [9] - [11] Rémond generalized it to varieties satisfying a geometric property stronger than transversality.

The main advantage of using a Bogomolov instead of a Lehmer type bound is that an essentially optimal Generalized Lehmer Conjecture is proven for C.M. abelian varieties and it is not likely to be proven in a near future for non C.M. abelian varieties. On the contrary the Bogomolov type bound is proven at least for some non C.M. abelian varieties. In addition, our method gives the non-density for a neighbourhood of positive radius ε \varepsilon. At present it is not known how to obtain results of this kind in abelian varieties using a Lehmer type bound.

The non-Zariski density for a transverse subvariety in a torus and Γ = 0 \Gamma=0 has been studied independently by P. Habegger [5]. He uses the Bogomolov type bound proven by Amoroso and David [1] and proves that for a transverse variety V V in 𝔾 m n \mathbb{G}^{n}_{m}, there exists ε > 0 \varepsilon>0 such that the set S 2 ​ d ​ ( V, 𝒪 ε) S_{2d}(V,\mathcal{O}_{\varepsilon}) is non-Zariski dense.

In the next section we fix the notation and recall the results we need from [14]. In section 3 we present the four main steps of the proof of Theorem 1.1. Section 4 is the core of this article: we prove the non-density of the intersections. In section 5 we conclude the proof of the main theorem. In the final section we prove that sometimes the height is bounded.

Acknowledgements. I kindly thank the Referee for his valuable suggestions.

## 2. preliminaries

In the following, we aim to be as transparent as possible, polishing statements from technicality. Therefore, we present the proofs for a power of an elliptic curve E E without C.M. Then End ⁡ ( E) \rm End(E) is identified with ℤ \mathbb{Z}. Proofs for a subvariety in a product of arbitrary elliptic curves are slightly more technical.

### 2.1. Small points

On E E, we fix a symmetric very ample line bundle ℒ 0 \mathcal{L}_{0}. On E g E^{g}, we consider the bundle ℒ \mathcal{L} which is the tensor product of the pull-backs of ℒ 0 \mathcal{L}_{0} via the natural projections on the factors. Degrees are computed with respect to the polarization ℒ \mathcal{L}. Usually E g E^{g} is endowed with the ℒ \mathcal{L} -canonical Néron-Tate height h ′ h^{\prime}. Though, we prefer to define on E g E^{g} the height of the maximum

 | h ⁡ ( x 1, …, x g) = max i ⁡ ( h ⁡ ( x i)), h(x_{1},\dots,x_{g})=\max_{i}(h(x_{i})), |  |

where h ⁡ ( x i) h(x_{i}) on E E is given by the ℒ 0 \mathcal{L}_{0} -canonical Néron-Tate height. Note that h ⁡ ( x) ≤ h ′ ​ ( x) ≤ g ​ h ​ ( x) h(x)\leq h^{\prime}(x)\leq gh(x). Hence, the two norms induced by h h and h ′ h^{\prime} are equivalent. We denote by | | ⋅ | | ||\cdot|| the semi-norm induced by h h on E g E^{g}.

For ε ≥ 0 \varepsilon\geq 0, we denote

 | 𝒪 ε = { ξ ∈ E g: ‖ ξ ‖ ≤ ε }. \mathcal{O}_{\varepsilon}=\{\xi\in E^{g}:||\xi||\leq\varepsilon\}. |  |

### 2.2. Morphisms and their height

We denote by M r, g ​ ( ℤ) M_{r,g}(\mathbb{Z}) the module of r × g r\times g matrices with entries in ℤ \mathbb{Z}. For F = ( f i ​ j) ∈ M r, g ​ ( ℤ) F=(f_{ij})\in M_{r,g}(\mathbb{Z}), we define the height of F F as the maximum of the absolute value of its entries

 | H ⁡ ( F) = max i ​ j ⁡ | f i ​ j |. H(F)=\max_{ij}|f_{ij}|. |  |

A morphism ϕ: E g → E r \phi:E^{g}\to E^{r} is identified with an integral matrix. Let a ∈ ℤ a\in\mathbb{Z}, we denote by [a] [a] the multiplication by a a.

Note that, the set of morphisms of height less than a constant is a finite set.

### 2.3. Algebraic subgroups

Let B B be an algebraic subgroup of E g E^{g} of codimension r r. Then B ⊂ ker ⁡ ϕ B B\subset\ker\phi_{B} for a surjective morphism ϕ B: E g → E r \phi_{B}:E^{g}\to E^{r}. Conversely, we denote by B ϕ B_{\phi} the kernel of a surjective morphism ϕ: E g → E r \phi:E^{g}\to E^{r}. Then B ϕ B_{\phi} is an algebraic subgroup of E g E^{g} of codimension r r. Note that r r is the rank of ϕ \phi. An easy observation (see for instance [13] page 61 line -3) gives that each of the r r equations defining B ϕ B_{\phi} has degree at most H ​ ( ϕ) 2 H(\phi)^{2}, up to a multiplicative constant depending on deg ⁡ E \deg E and g g. This directly implies:

###### Lemma 2.1.

Let ϕ: E g → E r \phi:E^{g}\to E^{r} be a surjective morphism. Then

 | deg ⁡ B ϕ ≤ c 0 ​ H ​ ( ϕ) 2 ​ r \deg B_{\phi}\leq c_{0}H(\phi)^{2r} |  |

where c 0 c_{0} is a constant depending on deg ⁡ E \deg E and g g.

### 2.4. Subgroups

Let Γ \Gamma be a subgroup of E g E^{g} of finite rank s s. Then Γ \Gamma is a ℤ \mathbb{Z} -module of rank s s. We call a maximal free set of Γ \Gamma a set of s s linearly independent elements of Γ \Gamma, in other words a basis of Γ ⊗ ℤ ℚ \Gamma\otimes_{\mathbb{Z}}\mathbb{Q}. If Γ \Gamma is a free module, we call integral generators a set of s s generators of Γ \Gamma.

The division group Γ 0 {\Gamma}_{0} of the coordinates group of the points of Γ \Gamma, in short of Γ \Gamma, is a subgroup of E E defined as

(2) |  | Γ 0 = { y ∈ E ​ such ​ that ​ N ​ y ∈ π ⁡ ( Γ) ​ for ​ N ∈ ℤ ∗ ​ and ​ π: E g → E }. {\Gamma}_{0}=\{y\in E{\rm{\,\,\,such\,\,\,that\,\,\,}}Ny\in\pi(\Gamma){\rm\,\,\,for\,\,\,}N\in\mathbb{Z}^{*}{\rm\,\,\,and\,\,\,}\pi:E^{g}\to E\}. |  |

Note that, Γ 0 g = Γ 0 × ⋯ × Γ 0 \Gamma^{g}_{0}=\Gamma_{0}\times\dots\times\Gamma_{0} contains Γ \Gamma and it is a module of finite rank. This shows that, to prove non-density statements for Γ \Gamma it is enough to prove them for Γ 0 g \Gamma_{0}^{g}.

###### Definition 2.2.

We say that a point p = ( p 1, …, p n) ∈ E n p=(p_{1},\dots,p_{n})\in E^{n} has rank s s if its coordinates group ⟨ p 1, …, p n ⟩ \langle p_{1},\dots,p_{n}\rangle has rank s s. We define Γ p \Gamma_{p} to be the division group of ⟨ p 1, …, p n ⟩ \langle p_{1},\dots,p_{n}\rangle.

Given a point p ∈ E s p\in E^{s} of rank s s, we associate to p p a positive real ε 0 ​ ( p) \varepsilon_{0}(p). This value will be used several times in the following.

###### Proposition 2.3 ( [14] Proposition 3.3 with τ = 1 \tau=1, End ⁡ ( E) = ℤ \rm End(E)=\mathbb{Z}, c 0 ​ ( p) = c 2 ​ ( p, 1) c_{0}(p)=c_{2}(p,1) and ε 0 ​ ( p) = ε 0 ​ ( p, 1) \varepsilon_{0}(p)=\varepsilon_{0}(p,1)).

Let p 1, …, p s p_{1},\dots,p_{s} be linearly independent points of E E and p = ( p 1, …, p s) p=(p_{1},\dots,p_{s}). Then, there exist positive reals c 0 ​ ( p) c_{0}(p) and ε 0 ​ ( p) \varepsilon_{0}(p) such that

 | c 0 ​ ( p) ​ ∑ i | b i | 2 ​ ‖ p i ‖ 2 ≤ ‖ ∑ i b i ​ ( p i − ξ i) − b ​ ζ ‖ 2 c_{0}(p)\sum_{i}|b_{i}|^{2}||p_{i}||^{2}\leq\Big|\Big|\sum_{i}b_{i}(p_{i}-\xi_{i})-b\zeta\Big|\Big|^{2} |  |

for all b 1, …, b s, b ∈ ℤ b_{1},\dots,b_{s},b\in\mathbb{Z} with | b | ≤ max i ⁡ | b i | |b|\leq\max_{i}|b_{i}| and for all ξ 1, …, ξ s, ζ ∈ E \xi_{1},\dots,\xi_{s},\zeta\in E with ‖ ξ i ‖, ‖ ζ ‖ ≤ ε 0 ​ ( p) ||\xi_{i}||,||\zeta||\leq\varepsilon_{0}(p).

### 2.5. From transverse to weak-transverse

Let V V be transverse in E g E^{g} and let Γ \Gamma be a subgroup of E g E^{g} of finite rank. Let Γ 0 \Gamma_{0} be the division group of Γ \Gamma and let s s be its rank. If s = 0 s=0 we define V ′ = V V^{\prime}=V. If s > 0 s>0, we denote by γ 1, …, γ s \gamma_{1},\dots,\gamma_{s} a maximal free set of Γ 0 \Gamma_{0} and

 | γ = ( γ 1, …, γ s). \gamma=(\gamma_{1},\dots,\gamma_{s}). |  |

We define

 | V ′ = V × γ. V^{\prime}=V\times\gamma. |  |

Since V V is transverse and γ \gamma has rank s s, then V ′ V^{\prime} is weak-transverse in E g + s E^{g+s}.

### 2.6. From weak-transverse to transverse

Let V ′ V^{\prime} be weak-transverse in E n E^{n}. If V ′ V^{\prime} is transverse then we define V = V ′ V=V^{\prime} and Γ = 0 \Gamma=0. If V ′ V^{\prime} is not transverse, let H 0 H_{0} be the abelian subvariety of smallest dimension g g such that V ′ ⊂ H 0 + p ⟂ V^{\prime}\subset H_{0}+p^{\perp} for p ⟂ ∈ H 0 ⟂ p^{\perp}\in H_{0}^{\perp} and H 0 ⟂ H_{0}^{\perp} the orthogonal complement of H 0 H_{0} of dimension s = n − g s=n-g. Then E n E^{n} is isogenous to H 0 × H 0 ⟂ H_{0}\times H_{0}^{\perp}. Furthermore H 0 H_{0} is isogenous to E g E^{g} and H 0 ⟂ H_{0}^{\perp} is isogenous to E s E^{s}. Let j 0 j_{0}, j 1 j_{1} and j 2 j_{2} be such isogenies. We fix the isogeny

 | j = ( j 1 × j 2) ∘ j 0: E n → H 0 × H 0 ⟂ → E g × E s, j=(j_{1}\times j_{2})\circ j_{0}:E^{n}\to H_{0}\times H_{0}^{\perp}\to E^{g}\times E^{s}, |  |

which sends H 0 H_{0} to E g × 0 E^{g}\times 0 and H 0 ⟂ H_{0}^{\perp} to 0 × E s 0\times E^{s} and j ⁡ ( p ⟂) = ( 0, …, 0, p 1, …, p s) j(p^{\perp})=(0,\dots,0,p_{1},\dots,p_{s}). Since V ′ V^{\prime} is weak-transverse and defined over ℚ ¯ \overline{\mathbb{Q}}, p = ( p 1, …, p s) p=(p_{1},\dots,p_{s}) has rank s s and is defined over ℚ ¯ \overline{\mathbb{Q}}.

We consider the natural projection on the first g g coordinates

 | π: E g × E s → E g j ⁡ ( V ′) → π ⁡ ( j ⁡ ( V ′)). \begin{split}\pi:&E^{g}\times E^{s}\to E^{g}\\ &j(V^{\prime})\to\pi(j(V^{\prime})).\end{split} |  |

We define

 | V = π ⁡ ( j ⁡ ( V ′)) V=\pi(j(V^{\prime})) |  |

and

 | Γ = Γ p g. \Gamma=\Gamma_{p}^{g}. |  |

Since H 0 H_{0} has minimal dimension, the variety V V is transverse in E g E^{g} and Γ \Gamma has rank g ​ s gs. Finally

 | j ⁡ ( V ′) = V × p. j(V^{\prime})=V\times p. |  |

We remark that we have defined a bijection ( V, Γ 0 g) → V ′ (V,\Gamma_{0}^{g})\to V^{\prime}, which is exactly what interest us.

### 2.7. Weak-transverse up to an isogeny

Statements on boundedness of heights and non-density of sets are invariant under an isogeny of the ambient variety. Namely, given an isogeny j j of E g E^{g}, Theorem 1.1 and Conjecture 1.2 hold for a variety if and only if they hold for its image via j j. Thus, the previous discussion shows that without loss of generality, we can assume that a weak-transverse variety V ′ V^{\prime} in E n E^{n} is of the form

 | V ′ = V × p V^{\prime}=V\times p |  |

where

1. i.

V V is transverse in E g E^{g},

2. ii.

p = ( p 1, …, p s) p=(p_{1},\dots,p_{s}) is a point in E s E^{s} of rank s s,

3. iii.

n = g + s n=g+s.

In short we will say that V × p V\times p is a weak-transverse variety in E g + s E^{g+s}, to say that V V is transverse in E g E^{g} and p ∈ E s p\in E^{s} has rank s s. This simplifies the setting for weak-transverse varieties.

### 2.8. Gauss-reduced morphisms

The matrices in M r × g ​ ( ℤ) M_{r\times g}(\mathbb{Z}) of the form

 | ϕ = ( a ​ I r | L) = ( a … 0 a 1, r + 1 … a 1, g ⋮ ⋮ ⋮ ⋮ 0 … a a r, r + 1 … a r, g), \phi=(aI_{r}|L)=\left(\begin{array}[]{cccccc}a&\dots&0&a_{1,r+1}&\dots&a_{1,g}\\ \vdots&&\vdots&\vdots&&\vdots\\ 0&\dots&a&a_{r,r+1}&\dots&a_{r,g}\end{array}\right), |  |

with H ⁡ ( ϕ) = a H(\phi)=a and no common factors of the entries will play a key role in this work. If r = g r=g simply forget L L. The following definition of Gauss-reduced is slightly more general than the one given in [14], namely we omit here the assumption that the entries of the matrix have no common factors. This is a marginal simplification, overseen in that paper.

###### Definition 2.4 (Gauss-reduced Morphisms).

Given positive integers g, r g,r, we say that a morphism ϕ: E g → E r \phi:E^{g}\to E^{r} is Gauss-reduced if:

1. i.

There esists a ∈ ℕ ∗ a\in\mathbb{N}^{*} such that a ​ I r aI_{r} is a submatrix of ϕ \phi, with I r I_{r} the r-identity matrix,

2. ii.

H ⁡ ( ϕ) = a H(\phi)=a.

A morphisms ϕ ′ \phi^{\prime}, given by a reordering of the rows of a morphism ϕ \phi, has the same kernel as ϕ \phi. Saying that a ​ I r aI_{r} is a sub-matrix of ϕ \phi fixes one permutation of the rows of ϕ \phi.

A reordering of the columns corresponds, instead, to a permutation of the coordinates. Statements will be proven for Gauss-reduced morphisms of the form ϕ = ( a ​ I r | L) \phi=(aI_{r}|L). For each other reordering of the columns the proofs are analogous. Since there are finitely many permutations of g g columns, the non-density statements will follow.

There are few easy facts that one shall keep in mind. Let ψ: E g → E r \psi:E^{g}\to E^{r} be a morphism and ϕ: E g → E r \phi:E^{g}\to E^{r} be a Gauss-reduced morphism, then

1. i.

For x ∈ E g x\in E^{g},

 | ‖ ψ ⁡ ( x) ‖ ≤ g ​ H ​ ( ψ) ​ ‖ x ‖ ||\psi(x)||\leq gH(\psi)||x|| |  |

and

 | ‖ ϕ ⁡ ( x) ‖ ≤ ( g − r + 1) ​ a ​ ‖ x ‖. ||\phi(x)||\leq(g-r+1)a||x||. |  |

2. ii.

For x ∈ E r × { 0 } g − r x\in E^{r}\times\{0\}^{g-r},

 | ϕ ⁡ ( x) = [a] ​ x. \phi(x)=[a]x. |  |

The following lemma shows that every abelian subvariety of codimension r r is contained in the kernel of a Gauss-reduced morphism of rank r r.

###### Lemma 2.5 ( [14] Lemma 4.4 ii. with End ⁡ ( E) = ℤ \rm End(E)=\mathbb{Z}).

Let ψ: E g → E r \psi:E^{g}\to E^{r} be a morphism of rank r r. Then, there exists a Gauss-reduced morphism ϕ: E g → E r \phi:E^{g}\to E^{r} such that

 | B ψ ⊂ B ϕ + ( E Tor r × { 0 } g − r). B_{\psi}\subset B_{\phi}+(E^{r}_{\rm{Tor}}\times\{0\}^{g-r}). |  |

Taking intersections with V K V_{K}, the previous lemma translates immediately as:

###### Lemma 2.6.

For any reals K, ε ≥ 1 K,\varepsilon\geq 1 and integer r ≥ 1 r\geq 1, it holds

 | S r ( V K, ( Γ 0 g) ε) = ⋃ ϕ: E g → E r Gauss − reduced V K ∩ ( B ϕ + ( Γ 0 g) ε). S_{r}(V_{K},(\Gamma_{0}^{g})_{\varepsilon})=\bigcup_{\begin{subarray}{c}\phi:E^{g}\to E^{r}\\ {\rm{Gauss-reduced}}\end{subarray}}V_{K}\cap(B_{\phi}+(\Gamma_{0}^{g})_{\varepsilon}). |  |

### 2.9. Quasi-special and Special Morphisms

Special morphisms play a key role in the study of weak-transverse varieties. A Special morphism ϕ ~ \tilde{\phi} is Gauss-reduced. In addition the multiplication by H ⁡ ( ϕ ~) H(\tilde{\phi}) acts on some of the first g g -coordinates.

###### Definition 2.7 (Quasi-special and Special Morphisms).

Given positive integers g, s, r g,s,r, a morphism ϕ ~: E g + s → E r \tilde{\phi}:E^{g+s}\to E^{r} is Quasi-special if there exist a Gauss-reduced morphisms ϕ: E g → E r \phi:E^{g}\to E^{r} and a morphism ϕ ′: E s → E r \phi^{\prime}:E^{s}\to E^{r} such that

- i.

ϕ ~ = ( ϕ | ϕ ′) \tilde{\phi}=(\phi|\phi^{\prime}).

The morphism ϕ ~: E g + s → E r \tilde{\phi}:E^{g+s}\to E^{r} is Special if it satisfies the further condition

- ii.

H ⁡ ( ϕ ~) = H ⁡ ( ϕ). H(\tilde{\phi})=H(\phi).

Note that, for g = 2 g=2 and r = s = 1 r=s=1, the morphism ( 0, 0, 1) (0,0,1) is Gauss-reduced, but not Special. While ( 1, 0, 2) (1,0,2) is Quasi-special but not Special. In addition, for g = r = 2 g=r=2, s = 1 s=1, ϕ = ( I 2 |) 3 2 \phi=(I_{2}|{}^{2}_{3}) is Quasi-special but not Gauss-reduced.

We want to show that if a point of large rank is in the kernel of a morphism then it is in the kernel of a Quasi-special morphism.

###### Lemma 2.8.

Let V V be an algebraic subvariety of E g E^{g}. Let p = ( p 1, …, p s) p=(p_{1},\dots,p_{s}) be a point in E s E^{s} of rank s s. There exists ε 0 ​ ( p) > 0 \varepsilon_{0}(p)>0 depending on p p such that for all ε ≤ ε 0 ​ ( p) \varepsilon\leq\varepsilon_{0}(p), for any subset V e V^{e} of V V and positive integer r r it holds

 | S r ( V e × p, 𝒪 ε) ⊂ ⋃ ϕ ~: E g + s → E r Quasi − special ( V e × p) ∩ ( B ϕ ~ + 𝒪 ε). S_{r}(V^{e}\times p,\mathcal{O}_{\varepsilon})\subset\bigcup_{\begin{subarray}{c}\tilde{\phi}:E^{g+s}\to E^{r}\\ {\rm{Quasi-special}}\end{subarray}}(V^{e}\times p)\cap(B_{\tilde{\phi}}+\mathcal{O}_{\varepsilon}). |  |

###### Proof.

The proof is the analog of [14] Lemma 6.2, where we shall read V e V^{e} for C C.

∎

## 3. The proof of Theorem 1.1: The four main steps

In the following, we present the four main steps for the proof of Theorem 1.1.

- (0)

We prove Theorem 1.4 which claims that Theorem 1.1 i. and ii. are equivalent.

We then shall prove Theorem 1.1 ii.

- (1)

In Proposition 3.2 we get rid of Γ \Gamma by considering instead of V V the weak-transverse variety V × γ V\times\gamma. The key point is that for V × γ V\times\gamma we consider

 | ⋃ ϕ ~: E g + s → E d + 1 Special ( V K × γ) ∩ ( B ϕ ~ + 𝒪 δ) \bigcup_{\begin{subarray}{c}\tilde{\phi}:E^{g+s}\to E^{d+1}\\ \rm{Special}\end{subarray}}(V_{K}\times\gamma)\cap(B_{\tilde{\phi}}+\mathcal{O}_{\delta}) |  |

where the union ranges only over Special morphisms (and not over all Gauss-reduced morphisms).

- (2)

In Proposition 3.3 we show that the above union is contained in the union of finitely many sets of the kind

 | ( V K × γ) ∩ ( B ϕ ~ + 𝒪 δ ′ / H ​ ( ϕ ~) 1 + 1 2 ​ n). (V_{K}\times\gamma)\cap(B_{\tilde{\phi}}+\mathcal{O}_{\delta^{\prime}/H(\tilde{\phi})^{{1+\frac{1}{2n}}}}). |  |

Important is that the radius of the neighbourhood of these finitely many sets is inversally proportional to the height of the morphism (and it is not a constant δ \delta like in the union in step (1)).

- (3)

In Proposition 4.4 we show that if the stabilizer of V V is finite, then there exists ε > 0 \varepsilon>0 such that, for all Special morphisms ϕ ~ \tilde{\phi} of rank at least d + 1 d+1, the set

 | ( V K × γ) ∩ ( B ϕ ~ + 𝒪 δ / H ⁡ ( ϕ ~)) (V_{K}\times\gamma)\cap(B_{\tilde{\phi}}+\mathcal{O}_{\delta/H(\tilde{\phi})}) |  |

is non-Zariski dense in V × γ V\times\gamma.

The statements (0), (1) and (2) are an immediate generalization of [14] Theorem 1.3, Proposition 10.2 and Proposition A respectively. Part (3) is the most delicate and it is presented in section 4, below. It is the counterpart to [14] Proposition B. In order to gain advantage from Theorem 1.5, we need to require that the stabilizer of the variety is finite. In view of Lemma 5.1 this assumption will not be restrictive.

Part (0) Theorem 1.4 is an immediate consequence of

###### Theorem 3.1.

Let V V be an irreducible algebraic subvariety of E g E^{g}. Then, for ε ≥ 0 \varepsilon\geq 0 and r r a positive integer:

1. i.

The map x → ( x, γ) x\to(x,\gamma) defines an injection

 | S r ​ ( V, Γ ε) ↪ S r ​ ( V × γ, 𝒪 ε). S_{r}(V,\Gamma_{\varepsilon})\hookrightarrow S_{r}(V\times\gamma,\mathcal{O}_{\varepsilon}). |  |

Recall that γ \gamma is a maximal free set of the division group Γ 0 \Gamma_{0} of Γ \Gamma.

Let p ∈ E s p\in E^{s} be a point of rank s s and K ≥ 0 K\geq 0. Then, there exists ε 0 ​ ( p) > 0 \varepsilon_{0}(p)>0 such that:

1. ii.

For ε ≤ ε 0 ​ ( p) \varepsilon\leq\varepsilon_{0}(p), the map ( x, p) → x (x,p)\to x defines an injection

 | S r ​ ( V K × p, 𝒪 ε) ↪ S r ​ ( V K, ( Γ p g) ε ​ K ′), S_{r}(V_{K}\times p,\mathcal{O}_{\varepsilon})\hookrightarrow S_{r}(V_{K},(\Gamma^{g}_{p})_{\varepsilon K^{\prime}}), |  |

where K ′ = ( g + s) ​ max ⁡ ( 1, g ⁡ ( K + ε) c ⁡ ( p)) K^{\prime}=(g+s)\max\left(1,\frac{g({K}+\varepsilon)}{c(p)}\right) and c ⁡ ( p) c(p) is a positive constant depending on p p.
Recall that Γ p \Gamma_{p} is the division group of the coordinates of p p.

###### Proof.

The proof is the analog of the proof of [14] Theorem 9.1, where we shall read V V for C C, K K for K 3 K_{3}, ε 0 ​ ( p) \varepsilon_{0}(p) for ε p \varepsilon_{p} and K ′ K^{\prime} for K 4 K_{4}. Note that the inequality ‖ x ‖ ≤ K ||x||\leq K is insured by considering just points in V K V_{K} (unlike in [14] where ‖ x ‖ ≤ K 3 ||x||\leq K_{3} is due to the hypothesis r ≥ 2 r\geq 2 and ε ≤ ε 3 \varepsilon\leq\varepsilon_{3}). ∎

Part (1) Given a subgroup Γ \Gamma and a real K {K}, [14] Lemma 3.4 (with End ⁡ ( E) = ℤ \rm End(E)=\mathbb{Z}) proves that there exists a maximal free set γ 1, …, γ s \gamma_{1},\dots,\gamma_{s} of the division group Γ 0 \Gamma_{0} such that

(3) |  | ‖ γ i ‖ ≥ 3 ​ g ​ K, ‖ ∑ i b i ​ γ i ‖ 2 ≥ 1 9 ​ ∑ i | b i | 2 ​ ‖ γ i ‖ 2. \begin{split}||\gamma_{i}||&\geq 3gK,\\ \Big|\Big|\sum_{i}b_{i}\gamma_{i}\Big|\Big|^{2}&\geq\frac{1}{9}\sum_{i}|b_{i}|^{2}||\gamma_{i}||^{2}.\end{split} |  |

for b 1, …, b s ∈ ℤ b_{1},\dots,b_{s}\in\mathbb{Z}. We define

 | γ = ( γ 1, …, γ s) \gamma=(\gamma_{1},\dots,\gamma_{s}) |  |

with γ i \gamma_{i} satisfying the above conditions.

###### Proposition 3.2.

Let V V be an irreducible algebraic subvariety of E g E^{g}. For r r a positive integer, K ≥ 0 K\geq 0 and ε ≤ K g \varepsilon\leq\frac{K}{g}, the map x → ( x, γ) x\to(x,\gamma) defines an injection

 | ⋃ ϕ: E g → E r Gauss ​ reduced V K ∩ ( B ϕ + ( Γ 0 g) ε) ↪ ⋃ ϕ ~ = ( ϕ | ϕ ′) Special ( V K × γ) ∩ ( B ϕ ~ + 𝒪 ε). \bigcup_{\begin{subarray}{c}\phi:E^{g}\to E^{r}\\ {\rm{Gauss\,\,\,reduced}}\end{subarray}}V_{K}\cap\left(B_{\phi}+\left(\Gamma^{g}_{0}\right)_{\varepsilon}\right)\hookrightarrow\bigcup_{\begin{subarray}{c}\tilde{\phi}=(\phi|\phi^{\prime})\\ {\rm{Special}}\end{subarray}}(V_{K}\times\gamma)\cap(B_{\tilde{\phi}}+\mathcal{O}_{\varepsilon}). |  |

###### Proof.

The proof is the analog of [14] Proposition 10.2, where one shall read K K for K 1 K_{1}, V V for C C, V K V_{K} for C ⁡ ( ℚ ¯) C(\overline{\mathbb{Q}}). Note that, here, the estimate ‖ x ‖ ≤ K ||x||\leq K is ensured by the assumption that we consider points in V K V_{K} (unlike in [14], where it is due to the assumptions r ≥ 2 r\geq 2 and ε ≤ ε 1 \varepsilon\leq\varepsilon_{1}). ∎

Part (2)

###### Proposition 3.3.

Let V V be an irreducible algebraic subvariety of E g E^{g}. Let p = ( p 1, …, p s) ∈ E s p=(p_{1},\dots,p_{s})\in E^{s} be a point of rank s s. Then, for r r a positive integer, K ≥ 0 K\geq 0 and ε > 0 \varepsilon>0,

 | ⋃ ϕ ~: E g + s → E r Special ( V K × p) ∩ ( B ϕ ~ + 𝒪 ε / M 1 + 1 2 ​ n) ⊂ ⋃ ψ ~: E g + s → E r Special, H ⁡ ( ψ ~) ≤ M ( V K × p) ∩ ( B ψ ~ + 𝒪 ( g + s + 1) ​ ε / H ​ ( ψ ~) 1 + 1 2 ​ n), \bigcup_{\begin{subarray}{c}\tilde{\phi}:E^{g+s}\to E^{r}\\ {\rm{Special}}\end{subarray}}(V_{K}\times p)\cap\left(B_{\tilde{\phi}}+\mathcal{O}_{\varepsilon/{M}^{1+\frac{1}{2n}}}\right)\subset\bigcup_{\begin{subarray}{c}\tilde{\psi}:E^{g+s}\to E^{r}\\ {\rm{Special}},\,\,H(\tilde{\psi})\leq M\end{subarray}}(V_{K}\times p)\cap\left(B_{{\tilde{\psi}}}+\mathcal{O}_{(g+s+1)\varepsilon/H(\tilde{\psi})^{1+\frac{1}{2n}}}\right), |  |

where M = max ⁡ ( 2, ⌈ K + ‖ p ‖ ε ⌉ 2) n M=\max\left(2,\lceil\frac{K+||p||}{\varepsilon}\rceil^{2}\right)^{n} and n = r ⁡ ( g + s) − r 2 + 1 n=r(g+s)-r^{2}+1.

###### Proof.

The proof is the analog of the proof of [14] Proposition A part ii., where one shall read V K V_{K} instead of C ⁡ ( ℚ ¯) C(\overline{\mathbb{Q}}), p p for γ \gamma, K K for K 2 K_{2} and M M for M ′ M^{\prime}. And where the estimate ‖ x ‖ ≤ K ||x||\leq K is ensured by the assumption that we consider points in V K V_{{K}} (and not as in [14], where it is due to the hypothesis r ≥ 2 r\geq 2 and ε ≤ ε 2 \varepsilon\leq\varepsilon_{2}).

Note that in the last row of the proof in [14] we estimate g − r + 1 + s + 1 g-r+1+s+1 with g + s g+s, because r ≥ 2 r\geq 2. Here we instead estimate g − r + 1 + s + 1 g-r+1+s+1 with g + s + 1 g+s+1, because r ≥ 1 r\geq 1.

∎

## 4. The proof of Theorem 1.1: Part (3)

Recall that μ ⁡ ( V) \mu(V) is the supremum of the reals ϵ ⁡ ( V) \epsilon(V) such that V ∩ 𝒪 ϵ ⁡ ( V) V\cap\mathcal{O}_{\epsilon(V)} is non-Zariski dense in V V. The essential minimum of V V is the square of μ ⁡ ( V) \mu(V). Using Theorem 1.5, we produce a sharp lower bound for the essential minimum of the image of a variety under a Gauss-reduced morphism. Unlike for curves, the stabilizer of the variety will play quite an important role. In this section, we will often assume that V V has finite stabilizer. In Lemma 5.1, we will see that such an assumption is not restrictive for the proof of our main theorem.

### 4.1. The estimate for the essential minimum

Consider a Gauss-reduced morphism ϕ \phi of codimension r = d + 1 r=d+1

 | ϕ = ( φ 1 ⋮ φ r) = ( a … 0 L 1 ⋮ ⋱ ⋮ ⋮ 0 … a L r) \phi=\left(\begin{array}[]{c}\varphi_{1}\\ \vdots\\ \varphi_{r}\end{array}\right)=\left(\begin{array}[]{cccccc}a&\dots&0&L_{1}\\ \vdots&\ddots&\vdots&\vdots\\ 0&\dots&a&L_{r}\end{array}\right) |  |

where L i ∈ ℤ g − r L_{i}\in\mathbb{Z}^{g-r}. We denote by x ¯ = ( x r + 1, …, x g) \overline{x}=(x_{r+1},\dots,x_{g}).

We define the isogenies:

(4) |  | F: E g → E g ( x 1, …, x g) → ( x 1, …, x r, a ​ x r + 1, …, a ​ x g). L: E g → E g ( x 1, …, x g) → ( x 1 + L 1 ​ ( x ¯), …, x r + L r ​ ( x ¯), x r + 1, …, x g). Φ: E g → E g ( x 1, …, x g) → ( φ 1 ​ ( x), …, φ r ​ ( x), x r + 1, …, x g). \begin{split}F:&E^{g}\to E^{g}\\ &(x_{1},\dots,x_{g})\to(x_{1},\dots,x_{r},ax_{r+1},\dots,ax_{g}).\\[8.5359pt] L:&E^{g}\to E^{g}\\ &(x_{1},\dots,x_{g})\to(x_{1}+L_{1}(\overline{x}),\dots,x_{r}+L_{r}(\overline{x}),x_{r+1},\dots,x_{g}).\\[8.5359pt] \Phi:&E^{g}\to E^{g}\\ &(x_{1},\dots,x_{g})\to(\varphi_{1}(x),\dots,\varphi_{r}(x),x_{r+1},\dots,x_{g}).\end{split} |  |

###### Definition 4.1 (Helping-Variety).

We define the variety

 | W = L ​ F − 1 ​ ( V). W=LF^{-1}(V). |  |

Then

 | Φ ⁡ ( V) = [a] ​ W. \Phi(V)=[a]W. |  |

We now estimate degrees.

###### Proposition 4.2.

There exist positive constants c 1 c_{1} and c 2 c_{2} depending on g g and deg ⁡ E \deg E such that:

- i.

The degree of ϕ ⁡ ( V) \phi(V) is bounded by c 1 ​ a 2 ​ d ​ deg ⁡ V c_{1}a^{2d}\deg V.

Suppose further that V V has finite stabilizer. Then,

- ii.

The degree of W W is bounded by c 2 ​ a 2 ​ ( g − r) ​ | Stab ​ V | ​ deg ⁡ V c_{2}a^{2(g-r)}|{\rm{Stab}}\,\,V|\deg V.

###### Proof.

For simplicity we indicate by ≪ \ll an inequality up to a multiplicative constant depending on g g and deg ⁡ E \deg E.

Let X X be an irreducible algebraic subvariety of E g E^{g}.

First we estimate the degree of the image of X X under an isogeny ψ: E g → E g \psi:E^{g}\to E^{g}. According to the chosen polarization

 | deg ⁡ ψ ⁡ ( X) = ∑ I E i 1 ⋅ ⋯ ⋅ E i d ⋅ ψ ⁡ ( X), \deg\psi(X)=\sum_{I}E_{i_{1}}\cdot\dots\cdot E_{i_{d}}\cdot\psi(X), |  |

where I = ( i 1, …, i d) I=(i_{1},\dots,i_{d}) ranges over the possible combinations of d d elements in the set { 1, …, g } \{1,\dots,g\} and E i j E_{i_{j}} is the coordinate subgroup given by x i j = 0 x_{i_{j}}=0. Then

 | deg ⁡ ψ ⁡ ( X) ≪ max I ⁡ ( E i 1 ⋅ ⋯ ⋅ E i d ⋅ ψ ⁡ ( X)). \deg\psi(X)\ll\max_{I}\big(E_{i_{1}}\cdot\dots\cdot E_{i_{d}}\cdot\psi(X)\big). |  |

Let us estimate the intersection numbers on the right. By definition

 | E i 1 ⋅ ⋯ ⋅ E i d ⋅ ψ ⁡ ( X) = B ψ I ⋅ X E_{i_{1}}\cdot\dots\cdot E_{i_{d}}\cdot\psi(X)=B_{\psi_{I}}\cdot X |  |

where the rows of ψ I \psi_{I} are the i 1, …, i d i_{1},\dots,i_{d} rows of ψ \psi. Note that rk ​ ψ I = d {\rm{rk\,\,}}\psi_{I}=d and H ⁡ ( ψ I) ≤ H ⁡ ( ψ) H(\psi_{I})\leq H(\psi). Bezout’s Theorem and Lemma 2.1 (applied with ϕ = ψ I \phi=\psi_{I} and r = d r=d) give

 | B ψ I ⋅ X ≤ deg ⁡ B ψ I ​ deg ​ X ≪ H ​ ( ψ I) 2 ​ d ​ deg ​ X ≪ H ​ ( ψ) 2 ​ d ​ deg ​ X. B_{\psi_{I}}\cdot X\leq\deg B_{\psi_{I}}\deg X\ll H(\psi_{I})^{2d}\deg X\ll H(\psi)^{2d}\deg X. |  |

We conclude

 | deg ⁡ ψ ⁡ ( X) ≪ H ​ ( ψ) 2 ​ d ​ deg ⁡ X. \deg\psi(X)\ll H(\psi)^{2d}\deg X. |  |

For ψ = Φ \psi=\Phi, we deduce

(5) |  | deg ⁡ Φ ⁡ ( V) ≪ H ​ ( Φ) 2 ​ d ​ deg ⁡ V = a 2 ​ d ​ deg ⁡ V. \deg\Phi(V)\ll H(\Phi)^{2d}\deg V=a^{2d}\deg V. |  |

i. In the chosen polarization, forgetting coordinates makes degrees decrease.

Note that ϕ ⁡ ( V) = π ​ Φ ​ ( V) \phi(V)=\pi\Phi(V), where π \pi is the projection on the first r r coordinates. By ( 5) we conclude that

 | deg ⁡ ϕ ⁡ ( V) ≤ deg ⁡ Φ ⁡ ( V) ≪ a 2 ​ d ​ deg ​ V. \deg\phi(V)\leq\deg\Phi(V)\ll a^{2d}\deg V. |  |

ii. In [6] Lemma 6 part i. Hindry proves:

For any positive integer b b,

 | deg ⁡ [b] ​ X = b 2 ​ d | Stab ​ X ∩ E g ​ [b] | ​ deg ⁡ X, \deg[b]X=\frac{b^{2d}}{|{\rm{Stab}}X\cap E^{g}[b]|}\deg X, |  |

where | ⋅ | |\cdot| means the cardinality of a set and E g ​ [b] E^{g}[b] is the kernel of the multiplication [b] [b].

Recall that Φ ⁡ ( V) = [a] ​ W \Phi(V)=[a]W. We deduce that

 | deg ⁡ Φ ⁡ ( V) = deg ⁡ [a] ​ W = a 2 ​ d | Stab ​ W ∩ E g ​ [a] | ​ deg ​ W. \deg\Phi(V)=\deg[a]W=\frac{a^{2d}}{|{\rm{Stab}}W\cap E^{g}[a]|}\deg W. |  |

Thus

 | deg ⁡ W = | Stab ​ W ∩ E g ​ [a] | a 2 ​ d ​ deg ⁡ Φ ​ ( V). \deg W=\frac{|{\rm{Stab}}W\cap E^{g}[a]|}{a^{2d}}\deg\Phi(V). |  |

By relation ( 5) we deduce

(6) |  | deg ⁡ W ≪ | Stab ​ W ∩ E g ​ [a] | ​ deg ⁡ V. \deg W\ll|{\rm{Stab}}W\cap E^{g}[a]|\deg V. |  |

We now estimate the cardinality of the stabilizer of W W. Since W = L ​ F − 1 ​ V W=LF^{-1}V, we get

 | Stab ​ W = L ​ F − 1 ​ Stab ​ V. {\rm{Stab}}W=LF^{-1}{\rm{Stab}}\,\,V. |  |

More precisely, if x ∈ Stab ​ W x\in{\rm{Stab}}\,\,W then x + W ⊂ W x+W\subset W. Recall that L L is an isomorphism. Applying F ​ L − 1 FL^{-1} on both sides, we obtain F ​ L − 1 ​ x + V ⊂ V FL^{-1}x+V\subset V. Thus F ​ L − 1 ​ x ∈ Stab ​ V FL^{-1}x\in{\rm{Stab}}\,\,V and x ∈ L ​ F − 1 ​ Stab ​ V x\in LF^{-1}{\rm{Stab}}\,\,V. On the other hand, suppose that x ∈ L ​ F − 1 ​ Stab ​ V x\in LF^{-1}{\rm{Stab}}\,\,V. Then F ​ L − 1 ​ x + V ⊂ V FL^{-1}x+V\subset V. Considering the preimage, x + ker ⁡ ( F ​ L − 1) + W ⊂ W x+\ker(FL^{-1})+W\subset W. But, by definition, W W is ker ⁡ ( F ​ L − 1) \ker(FL^{-1}) invariant, so x + W ⊂ W x+W\subset W and x ∈ Stab ​ W x\in{\rm{Stab}}\,\,W.

By assumption the stabilizer of V V is finite. In addition L L is an isomorphism. So

 | | Stab ​ W | = | ker ⁡ F | ​ | Stab ​ V | = a 2 ​ ( g − r) ​ | Stab ​ V |. |{\rm{Stab}}W|=|\ker F||{\rm{Stab}}\,\,V|=a^{2(g-r)}|{\rm{Stab}}\,\,V|. |  |

In view of ( 6), we conclude that

 | deg ⁡ W ≪ | Stab ​ W | ​ deg ⁡ V ≪ a 2 ​ ( g − r) | Stab ​ V | deg ⁡ V. \deg W\ll|{\rm{Stab}}W|\deg V\ll a^{2(g-r)}|{\rm{Stab}}\,\,V|\deg V. |  |

∎

The following Proposition is a lower bound for the essential minimum of the image of a variety under Gauss-reduced morphisms. It reveals the dependence on the height of the morphism. While the first bound is an immediate application of Theorem 1.5 and Proposition 4.2, the second estimate is subtle.

###### Proposition 4.3.

Let ϕ \phi be a Gauss-reduced morphism of rank d + 1 d+1 with a = H ⁡ ( ϕ) a=H(\phi). Then, for any point y ∈ E g y\in E^{g} and any η > 0 \eta>0,

- i.

 | μ ⁡ ( ϕ ⁡ ( V + y)) > ϵ 1 ​ ( V, η) ​ 1 a d + 2 ​ d ​ η, \mu(\phi(V+y))>\epsilon_{1}(V,\eta)\frac{1}{a^{{{d}+2d\eta}}}, |  |

where ϵ 1 ​ ( V, η) \epsilon_{1}(V,\eta) is an effective positive constant depending on V V, E E, g g and η \eta.

Suppose further that V V has finite stabilizer. Let Φ \Phi be the isogeny defined in ( 4). Then,

- ii.

 | μ ⁡ ( Φ ⁡ ( V + y)) > ϵ 2 ​ ( V, η) ​ a 1 g − d − 2 ​ ( g − d − 1) ​ η, \mu\left(\Phi(V+y)\right)>\epsilon_{2}(V,\eta)a^{\frac{1}{g-d}-2(g-d-1)\eta}, |  |

where ϵ 2 ​ ( V, η) \epsilon_{2}(V,\eta) is an effective positive constant depending on V V, E E, g g and η \eta.

###### Proof.

Let us recall the Bogomolov type bound given in Theorem 1.5; for a transverse irreducible variety X X in E g E^{g} and any η > 0 \eta>0

(7) |  | μ ⁡ ( X) > ϵ ⁡ ( X, η) = c ⁡ ( E g, η) deg ⁡ X 1 2 ​ c ​ o ​ d ​ X + η. \mu(X)>\epsilon(X,\eta)=\frac{c(E^{g},\eta)}{\deg X^{\frac{1}{2{\rm{cod}}X}+\eta}}. |  |

i. Let q = ϕ ⁡ ( y) q=\phi(y). Then ϕ ⁡ ( V + y) = ϕ ⁡ ( V) + q \phi(V+y)=\phi(V)+q. Since V V is irreducible, transverse and defined over ℚ ¯ \overline{\mathbb{Q}}, ϕ ⁡ ( V) + q \phi(V)+q is as well.

Observe that ϕ ⁡ ( V) ⊂ E d + 1 \phi(V)\subset E^{d+1} has dimension at least 1 1 (because V V is transverse) and at most d d (because dimension can just decrease under morphisms). Furthermore dimensions are preserved by translations.

The bound ( 7) for ϕ ⁡ ( V) + q \phi(V)+q and g = d + 1 g=d+1 gives

 | μ ⁡ ( ϕ ⁡ ( V + y)) = μ ⁡ ( ϕ ⁡ ( V) + q) > ϵ ⁡ ( ϕ ⁡ ( V) + q, η) = c ⁡ ( E d + 1, η) ( deg ⁡ ( ϕ ⁡ ( V) + q)) 1 2 ​ c ​ o ​ d ​ ϕ ​ ( V) + η ≥ c ⁡ ( E d + 1, η) ( deg ⁡ ( ϕ ⁡ ( V) + q)) 1 2 + η. \begin{split}\mu(\phi(V+y))&=\mu(\phi(V)+q)\\ &>\epsilon(\phi(V)+q,\eta)=\frac{c(E^{d+1},\eta)}{\left(\deg(\phi(V)+q)\right)^{\frac{1}{2\rm cod\phi(V)}+\eta}}\\ &\geq\frac{c(E^{d+1},\eta)}{\left(\deg(\phi(V)+q)\right)^{\frac{1}{2}+\eta}}.\end{split} |  |

Degrees are preserved by translations, hence Proposition 4.2 i. implies

 | deg ⁡ ( ϕ ⁡ ( V) + q) = deg ⁡ ϕ ⁡ ( V) ≤ c 1 ​ a 2 ​ d ​ deg ​ V. \deg(\phi(V)+q)=\deg\phi(V)\leq c_{1}a^{2d}\deg V. |  |

If follows

 | ϵ ⁡ ( ϕ ⁡ ( V) + q, η) ≥ c ⁡ ( E d + 1, η) ( c 1 ​ a 2 ​ d ​ deg ⁡ V) 1 2 + η. \epsilon(\phi(V)+q,\eta)\geq\frac{c(E^{d+1},\eta)}{(c_{1}a^{2d}\deg V)^{\frac{1}{2}+\eta}}. |  |

Define

 | ϵ 1 ​ ( V, η) = c ⁡ ( E d + 1, η) ( c 1 ​ deg ⁡ V) 1 2 + η. \epsilon_{1}(V,\eta)=\frac{c(E^{d+1},\eta)}{(c_{1}\deg V)^{\frac{1}{2}+\eta}}. |  |

Then

 | μ ⁡ ( ϕ ⁡ ( V + y)) > ϵ 1 ​ ( V, η) a d + 2 ​ d ​ η. \mu(\phi(V+y))>\frac{\epsilon_{1}(V,\eta)}{a^{d+2d\eta}}. |  |

ii. Let q ∈ E g q\in E^{g} be a point such that [a] ​ q = Φ ⁡ ( y) [a]q=\Phi(y). Let W 0 W_{0} be an irreducible component of W = L ​ F − 1 ​ ( V) W=LF^{-1}(V). Then

 | Φ ⁡ ( V + y) = [a] ​ ( W 0 + q). \Phi(V+y)=[a](W_{0}+q). |  |

Therefore

(8) |  | μ ⁡ ( Φ ⁡ ( V + y)) = a ​ μ ​ ( W 0 + q). {\mu\left(\Phi(V+y)\right)}=a\mu(W_{0}+q). |  |

We now estimate μ ⁡ ( W 0 + q) \mu(W_{0}+q) via the bound ( 7). The variety W 0 + q ⊂ E g W_{0}+q\subset E^{g} is irreducible by definition. Since V V is transverse and defined over ℚ ¯ \overline{\mathbb{Q}}, W 0 + q W_{0}+q is as well. Furthermore, isogenies and translations preserve dimensions. Thus dim ( W 0 + q) = dim V = d \dim(W_{0}+q)=\dim V=d. Then,

 | μ ⁡ ( W 0 + q) > ϵ ⁡ ( W 0 + q, η) = c ⁡ ( E g, η) deg ⁡ ( W 0 + q) 1 2 ​ ( g − d) + η. \mu(W_{0}+q)>\epsilon(W_{0}+q,\eta)=\frac{c(E^{g},\eta)}{\deg(W_{0}+q)^{\frac{1}{2(g-d)}+\eta}}. |  |

Since W 0 W_{0} is an irreducible component of W W, deg ⁡ W 0 ≤ deg ⁡ W \deg W_{0}\leq\deg W. Furthermore, translations by a point preserve degrees. Thus Proposition 4.2 ii. with r = d + 1 r=d+1 gives

 | deg ⁡ ( W 0 + q) ≤ deg ⁡ W ≤ c 2 ​ a 2 ​ ( g − d − 1) | Stab ​ V | deg ⁡ V. \deg(W_{0}+q)\leq\deg W\leq c_{2}a^{2(g-d-1)}|{\rm{Stab}}\,\,V|\deg V. |  |

Therefor

 | μ ⁡ ( W 0 + q) > c ⁡ ( E g, η) ( c 2 ​ | Stab ​ V | ​ deg ⁡ V) 1 2 ​ ( g − d) + η ​ ( a 2 ​ ( g − d − 1)) − 1 2 ​ ( g − d) − η. \mu(W_{0}+q)>\frac{c(E^{g},\eta)}{(c_{2}|{\rm{Stab}}\,\,V|\deg V)^{\frac{1}{2(g-d)}+\eta}}\left(a^{2(g-d-1)}\right)^{-\frac{1}{2(g-d)}-\eta}. |  |

Define

 | ϵ 2 ​ ( V, η) = c ⁡ ( E g, η) ( c 2 ​ | Stab ​ V | ​ deg ⁡ V) 1 2 ​ ( g − d) + η. \epsilon_{2}(V,\eta)=\frac{c(E^{g},\eta)}{(c_{2}|{\rm{Stab}}\,\,V|\deg V)^{\frac{1}{2(g-d)}+\eta}}. |  |

So

 | μ ⁡ ( W 0 + q) > ϵ 2 ​ ( V, η) ​ a − 1 + 1 g − d − 2 ​ ( g − d − 1) ​ η. \mu(W_{0}+q)>\epsilon_{2}(V,\eta){a^{-1+\frac{1}{g-d}-2(g-d-1)\eta}}. |  |

Replace in ( 8), to obtain

 | μ ⁡ ( Φ ⁡ ( V + y)) > ϵ 2 ​ ( V, η) ​ a 1 g − d − 2 ​ ( g − d − 1) ​ η. \mu(\Phi(V+y))>\epsilon_{2}(V,\eta)a^{\frac{1}{g-d}-2(g-d-1)\eta}. |  |

∎

### 4.2. The non-density of the intersections

We come to the main proposition of this section: each set in the union is non-Zariski dense. The proof of i. case (1) is delicate. In general μ ⁡ ( π ⁡ ( V)) ≤ μ ⁡ ( V) \mu(\pi(V))\leq\mu(V) for π \pi a projection on some factors. We shall rather find a kind of reverse inequality. On a set of bounded height this will be possible.

###### Proposition 4.4.

Suppose that V ⊂ E g V\subset E^{g} has finite stabilizer. Then, for every K ≥ 0 K\geq 0, there exists an effective ε 1 > 0 \varepsilon_{1}>0 such that:

1. i.

For ε ≤ ε 1 \varepsilon\leq\varepsilon_{1}, for all Gauss-reduced morphisms ϕ: E g → E d + 1 \phi:E^{g}\to E^{d+1} and for all y ∈ E d + 1 × { 0 } g − d − 1 y\in E^{d+1}\times\{0\}^{g-d-1}, the set

 | ( V K + y) ∩ ( B ϕ + 𝒪 ε / H ⁡ ( ϕ)) \left(V_{K}+y\right)\cap\left(B_{\phi}+\mathcal{O}_{\varepsilon/H(\phi)}\right) |  |

is non-Zariski dense in V V.

2. ii.

Let s s be a positive integer. For ε ≤ ε 1 g + s \varepsilon\leq\frac{\varepsilon_{1}}{g+s}, for all Special morphisms ϕ ~ = ( ϕ | ϕ ′): E g + s → E d + 1 \tilde{\phi}=(\phi|\phi^{\prime}):E^{g+s}\to E^{d+1} and for all points p ∈ E s p\in E^{s}, the set

 | ( V K × p) ∩ ( B ϕ ~ + 𝒪 ε / H ⁡ ( ϕ)) (V_{K}\times p)\cap\left(B_{\tilde{\phi}}+\mathcal{O}_{\varepsilon/H(\phi)}\right) |  |

is non-Zariski dense in V × p V\times p.

###### Proof.

Define

 | η = 1 2 ​ d, m = ( K ϵ 2 ​ ( V, η)) g − d 1 − 2 ​ ( g − d − 1) ​ ( g − d) ​ η, ε 1 = min ⁡ ( K g, ϵ 1 ​ ( V, η) g ​ m d + 1), \begin{split}\eta&=\frac{1}{{2d}},\\ m&=\left(\frac{{K}}{\epsilon_{2}(V,\eta)}\right)^{\frac{g-d}{1-{2(g-d-1)}(g-d)\eta}},\\ \varepsilon_{1}&=\min\left(\frac{{K}}{g},\frac{\epsilon_{1}(V,\eta)}{gm^{{d+1}}}\right),\\ \end{split} |  |

where ϵ 1 ​ ( V, η) \epsilon_{1}(V,\eta) and ϵ 2 ​ ( V, η) \epsilon_{2}(V,\eta) are as in Proposition 4.3.

Part i.

Let a = H ⁡ ( ϕ) a=H(\phi). We distinguish two cases:

- (1)

a ≥ m a\geq m,

- (2)

a ≤ m. a\leq m.

Case (1) - a ≥ m a\geq m

Let x + y ∈ ( V K + y) ∩ ( B ϕ + 𝒪 ε / a) x+y\in(V_{{K}}+y)\cap\left(B_{\phi}+\mathcal{O}_{\varepsilon/a}\right), where

 | y = ( y 1, …, y d + 1, 0, …, 0) ∈ E d + 1 × { 0 } g − d − 1. y=(y_{1},\dots,y_{d+1},0,\dots,0)\in E^{d+1}\times\{0\}^{g-d-1}. |  |

Then

 | ϕ ⁡ ( x + y) = ϕ ⁡ ( ξ) \phi(x+y)=\phi(\xi) |  |

for ‖ ξ ‖ ≤ ε / a ||\xi||\leq\varepsilon/a.

Let Φ = ϕ × i ​ d E g − d − 1 \Phi=\phi\times id_{E^{g-d-1}} as in ( 4). Then

 | Φ ⁡ ( x + y) = ( ϕ ⁡ ( x + y), x d + 2, …, x g) = ( ϕ ⁡ ( ξ), x d + 2, …, x g). \begin{split}\Phi(x+y)&=(\phi(x+y),x_{d+2},\dots,x_{g})\\ &=(\phi(\xi),x_{d+2},\dots,x_{g}).\end{split} |  |

Therefore

 | ‖ Φ ⁡ ( x + y) ‖ = | | ( ϕ ⁡ ( ξ), x d + 2, …, x g) | | ≤ max ⁡ ( ‖ ϕ ⁡ ( ξ) ‖, ‖ x ‖). ||\Phi(x+y)||=||(\phi(\xi),x_{d+2},\dots,x_{g})||\leq\max\left(||\phi(\xi)||,||x||\right). |  |

Since ‖ ξ ‖ ≤ ε a ||\xi||\leq\frac{\varepsilon}{a} and ε ≤ K g \varepsilon\leq\frac{K}{g}, then

 | ‖ ϕ ⁡ ( ξ) ‖ ≤ g ​ ε ≤ K. ||\phi(\xi)||\leq g{\varepsilon}\leq K. |  |

Also ‖ x ‖ ≤ K ||x||\leq K, because x ∈ V K x\in V_{K}. Thus

 | ‖ Φ ⁡ ( x + y) ‖ ≤ K. ||\Phi(x+y)||\leq{K}. |  |

We work under the hypothesis a ≥ m ≥ ( K ϵ 2 ​ ( V, η)) g − d 1 − 2 ​ ( g − d − 1) ​ ( g − d) ​ η a\geq m\geq\left(\frac{{K}}{\epsilon_{2}(V,\eta)}\right)^{\frac{g-d}{1-{2(g-d-1)}(g-d)\eta}}, then

 | K ≤ ϵ 2 ​ ( V, η) ​ a 1 g − d − 2 ​ ( g − d − 1) ​ η. {K}\leq\epsilon_{2}(V,\eta)a^{\frac{1}{g-d}-{2(g-d-1)}\eta}. |  |

In Proposition 4.3 ii. we have proven

 | ϵ 2 ​ ( V, η) ​ a 1 g − d − 2 ​ ( g − d − 1) ​ η < μ ⁡ ( Φ ⁡ ( V + y)). \epsilon_{2}(V,\eta)a^{\frac{1}{g-d}-{2(g-d-1)}\eta}<\mu(\Phi(V+y)). |  |

So

 | ‖ Φ ⁡ ( x + y) ‖ ≤ K < μ ⁡ ( Φ ⁡ ( V + y)). ||\Phi(x+y)||\leq K<\mu(\Phi(V+y)). |  |

We deduce that Φ ⁡ ( x + y) \Phi(x+y) belongs to the non-Zariski dense set

 | Z 1 = Φ ⁡ ( V + y) ∩ 𝒪 K. Z_{1}=\Phi(V+y)\cap{\mathcal{O}}_{K}. |  |

The restriction morphism Φ | V + y: V + y → Φ ( V + y) \Phi_{|V+y}:V+y\to\Phi(V+y) is finite, because Φ \Phi is an isogeny. Then x + y x+y belongs to the non-Zariski dense set Φ | V + y − 1 ( Z 1) \Phi_{|V+y}^{-1}(Z_{1}).

We can conclude that, for every ϕ \phi Gauss-reduced of rank d + 1 d+1 with H ⁡ ( ϕ) ≥ m H(\phi)\geq m, the set

 | ( V K + y) ∩ ( B ϕ + 𝒪 ε / H ⁡ ( ϕ)) (V_{K}+y)\cap\left(B_{\phi}+\mathcal{O}_{\varepsilon/H(\phi)}\right) |  |

is non-Zariski dense.

Case (2) - a ≤ m a\leq m

Let x + y ∈ ( V K + y) ∩ ( B ϕ + 𝒪 ε / a) x+y\in(V_{K}+y)\cap(B_{\phi}+\mathcal{O}_{\varepsilon/a}), where y ∈ E d + 1 × { 0 } g − d − 1 y\in E^{d+1}\times\{0\}^{g-d-1}. Then

 | ϕ ⁡ ( x + y) = ϕ ⁡ ( ξ) \phi(x+y)=\phi(\xi) |  |

for ‖ ξ ‖ ≤ ε / a ||\xi||\leq\varepsilon/a. However we have chosen ε ≤ ϵ 1 ​ ( V, η) / g ​ m d + 1 \varepsilon\leq\epsilon_{1}(V,\eta)/gm^{{d+1}}. Hence

 | ‖ ϕ ⁡ ( x + y) ‖ = ‖ ϕ ⁡ ( ξ) ‖ ≤ g ​ ε ≤ ϵ 1 ​ ( V, η) m d + 1. ||\phi(x+y)||=||\phi(\xi)||\leq{g\varepsilon}\leq\frac{\epsilon_{1}(V,\eta)}{m^{d+1}}. |  |

We are working under the hypothesis a ≤ m a\leq m. Moreover η = 1 2 ​ d \eta=\frac{1}{2d}. Then

 | a d + 2 ​ d ​ η ≤ m d + 1. a^{{{d}+2d\eta}}\leq m^{d+1}. |  |

Thus

 | ‖ ϕ ⁡ ( x + y) ‖ ≤ ϵ 1 ​ ( V, η) m d + 1 ≤ ϵ 1 ​ ( V, η) a d + 2 ​ d ​ η. ||\phi(x+y)||\leq\frac{\epsilon_{1}(V,\eta)}{m^{d+1}}\leq\frac{\epsilon_{1}(V,\eta)}{a^{{{d}+2d\eta}}}. |  |

In Proposition 4.3 i. we have proven

 | ϵ 1 ​ ( V, η) a d + 2 ​ d ​ η < μ ⁡ ( ϕ ⁡ ( V + y)). \frac{\epsilon_{1}(V,\eta)}{a^{{{d}+2d\eta}}}<\mu(\phi(V+y)). |  |

We deduce that ϕ ⁡ ( x + y) \phi(x+y) belongs to the non-Zariski dense set

 | Z 2 = ϕ ⁡ ( V + y) ∩ 𝒪 ϵ 1 ​ ( V, η) / m d + 1. Z_{2}=\phi(V+y)\cap{\mathcal{O}}_{\epsilon_{1}(V,\eta)/m^{{d+1}}}. |  |

Since V V is transverse, the dimension of ϕ ⁡ ( V + y) \phi(V+y) is at least 1 1. Consider the restriction morphism ϕ | V + y: V + y → ϕ ( V + y) \phi_{|V+y}:V+y\to\phi(V+y). Then x + y x+y belongs to the non-Zariski dense set ϕ | V + y − 1 ( Z 2) \phi^{-1}_{|V+y}(Z_{2}).

We conclude that, for all ϕ \phi Gauss-reduced of rank d + 1 d+1 with H ⁡ ( ϕ) ≤ m H(\phi)\leq m, the set

 | ( V K + y) ∩ ( B ϕ + 𝒪 ε / H ⁡ ( ϕ)) (V_{K}+y)\cap\left(B_{\phi}+\mathcal{O}_{\varepsilon/H(\phi)}\right) |  |

is non-Zariski dense.

Cases (1) and (2) prove part i.

Part ii. We are going to show that, for every ϕ ~ = ( ϕ | ϕ ′) \tilde{\phi}=(\phi|\phi^{\prime}) Special of rank d + 1 {d+1} (note that ϕ \phi is Gauss-reduced of rank d + 1 {d+1}), there exists y ∈ E d + 1 × { 0 } g − d − 1 y\in E^{d+1}\times\{0\}^{g-d-1} such that the map ( x, p) → x + y (x,p)\to x+y defines an injection

(9) |  | ( V K × p) ∩ ( B ϕ ~ + 𝒪 ε / H ⁡ ( ϕ)) ↪ ( V K + y) ∩ ( B ϕ + 𝒪 ( g + s) ​ ε / H ⁡ ( ϕ)). (V_{K}\times p)\cap\left(B_{\tilde{\phi}}+\mathcal{O}_{\varepsilon/H(\phi)}\right)\hookrightarrow(V_{K}+y)\cap\left(B_{\phi}+\mathcal{O}_{(g+s)\varepsilon/H(\phi)}\right). |  |

We then apply part i. of this proposition to ϕ \phi and y y; since ( g + s) ​ ε ≤ ε 1 (g+s)\varepsilon\leq\varepsilon_{1}, then

 | ( V K + y) ∩ ( B ϕ + 𝒪 ( g + s) ​ ε / H ⁡ ( ϕ)) (V_{K}+y)\cap\left(B_{\phi}+\mathcal{O}_{(g+s)\varepsilon/H(\phi)}\right) |  |

is non-Zariski dense in V V. So for ε ≤ ε 1 g + s \varepsilon\leq\frac{\varepsilon_{1}}{g+s}, the set

 | ( V K × p) ∩ ( B ϕ ~ + 𝒪 ε / H ⁡ ( ϕ)) (V_{K}\times p)\cap\left(B_{\tilde{\phi}}+\mathcal{O}_{\varepsilon/H(\phi)}\right) |  |

is non-Zariski dense in V V.

Let us prove the inclusion ( 9). Let ϕ ~ = ( ϕ | ϕ ′) \tilde{\phi}=(\phi|\phi^{\prime}) be Special of rank d + 1 d+1. By definition of Special ϕ = ( a ​ I d + 1 | L) \phi=(aI_{d+1}|L) is Gauss-reduced of rank d + 1 {d+1}.

Let y ′ ∈ E d + 1 {y^{\prime}}\in E^{d+1} be a point such that

 | [a] ​ y ′ = ϕ ′ ​ ( p). [a]{y^{\prime}}=\phi^{\prime}(p). |  |

Define

 | y = ( y ′, 0, ⋯, 0) ∈ E d + 1 × { 0 } g − d − 1 y=(y^{\prime},0,\cdots,0)\in E^{d+1}\times\{0\}^{g-d-1} |  |

Then

 | ϕ ⁡ ( y) = [a] ​ y ′ = ϕ ′ ​ ( p). \phi(y)=[a]y^{\prime}=\phi^{\prime}(p). |  |

Let

 | ( x, p) ∈ ( V K × p) ∩ ( B ϕ ~ + 𝒪 ε / a). (x,p)\in(V_{K}\times p)\cap\left(B_{\tilde{\phi}}+\mathcal{O}_{\varepsilon/a}\right). |  |

Then, there exists ξ ∈ 𝒪 ε / a \xi\in\mathcal{O}_{\varepsilon/a} such that

 | ϕ ~ ​ ( ( x, p) + ξ) = 0. \tilde{\phi}((x,p)+\xi)=0. |  |

Equivalently

 | ϕ ⁡ ( x) + ϕ ′ ​ ( p) + ϕ ~ ​ ( ξ) = 0 \phi(x)+\phi^{\prime}(p)+\tilde{\phi}(\xi)=0 |  |

and

 | ϕ ​ ( x + y) + ϕ ~ ​ ( ξ) = 0. \phi(x+y)+\tilde{\phi}(\xi)=0. |  |

Let ξ ′′ ∈ E d + 1 \xi^{\prime\prime}\in E^{d+1} be a point such that

 | [a] ​ ξ ′′ = ϕ ~ ​ ( ξ). [a]\xi^{\prime\prime}=\tilde{\phi}(\xi). |  |

We define ξ ′ = ( ξ ′′, { 0 } g − d − 1) \xi^{\prime}=(\xi^{\prime\prime},\{0\}^{g-d-1}), then

 | ϕ ⁡ ( ξ ′) = [a] ​ ξ ′′ = ϕ ~ ​ ( ξ), \phi(\xi^{\prime})=[a]\xi^{\prime\prime}=\tilde{\phi}(\xi), |  |

and

 | ϕ ⁡ ( x + y + ξ ′) = 0. \phi(x+y+\xi^{\prime})=0. |  |

Since ϕ ~ \tilde{\phi} is Special H ⁡ ( ϕ ~) = a H(\tilde{\phi})=a. Further ‖ ξ ‖ ≤ ε a ||\xi||\leq\frac{\varepsilon}{a}. We deduce

 | ‖ ξ ′ ‖ = ‖ ξ ′′ ‖ = ‖ ϕ ~ ​ ( ξ) ‖ a ≤ ( g + s) ​ ε a. ||\xi^{\prime}||=||\xi^{\prime\prime}||=\frac{||\tilde{\phi}(\xi)||}{a}\leq\frac{(g+s)\varepsilon}{a}. |  |

In conclusion

 | ϕ ⁡ ( x + y + ξ ′) = 0 \phi(x+y+\xi^{\prime})=0 |  |

with ‖ ξ ′ ‖ ≤ ( g + s) ​ ε a ||\xi^{\prime}||\leq\frac{(g+s)\varepsilon}{a}. Equivalently

 | ( x + y) ∈ ( V K + y) ∩ ( B ϕ + 𝒪 ( g + s) ​ ε / H ⁡ ( ϕ)), (x+y)\in(V_{K}+y)\cap\left(B_{\phi}+\mathcal{O}_{(g+s)\varepsilon/H(\phi)}\right), |  |

where y ∈ E d + 1 × { 0 } g − d − 1 {y}\in E^{d+1}\times\{0\}^{g-d-1} and ϕ \phi is Gauss-reduced of rank d + 1 {d+1}.

This proves relation ( 9) and concludes the proof.

∎

## 5. The Proof of Theorem 1.1: Conclusion

### Reducing to a variety with finite stabilizer

In the following lemma, we will show that to prove Theorem 1.1 it is sufficient to prove it for varieties with finite stabilizer. This innocent remark will allow us to use all results of section 4.

###### Lemma 5.1.

They hold:

1. i.

Let X = X 1 × E d 2 X=X_{1}\times E^{d_{2}} be a subvariety of E g E^{g} of dimension d. Then, for r ≥ d 2 r\geq d_{2},

 | S r ​ ( X, F) ↪ S r − d 2 ​ ( X 1, F ′) × E d 2 S_{r}(X,F)\hookrightarrow S_{r-d_{2}}(X_{1},F^{\prime})\times E^{d_{2}} |  |

where F ′ F^{\prime} is the projection of F F on E g − d 2 E^{g-d_{2}}.

2. ii.

Let V V be a (weak)-transverse subvariety of E g E^{g}. Suppose that dim Stab ​ V = d 2 ≥ 1 \dim{\rm{Stab}}\,\,V=d_{2}\geq 1. Then, there exists an isogeny j j of E g E^{g} such that

 | j ⁡ ( V) = V 1 × E d 2 j(V)=V_{1}\times E^{d_{2}} |  |

with V 1 V_{1} (weak)-transverse in E g − d 2 E^{g-d_{2}} and Stab ​ V 1 {\rm{Stab}}\,\,V_{1} a finite group.

3. iii.

Theorem 1.1 holds if and only if it holds for varieties with finite stabilizer.

###### Proof.

i. Let ( x 1, x 2) ∈ S r ​ ( X, F) (x_{1},x_{2})\in S_{r}(X,F) with x 1 ∈ X 1 x_{1}\in X_{1} and x 2 ∈ E d 2 x_{2}\in E^{d_{2}}. Then, there exist ϕ: E g → E r \phi:E^{g}\to E^{r} of rank r r and ( f 1, f 2) ∈ F (f_{1},f_{2})\in F such that

(10) |  | ϕ ⁡ ( ( x 1, x 2) − ( f 1, f 2)) = 0. \phi((x_{1},x_{2})-(f_{1},f_{2}))=0. |  |

Decompose ϕ = ( α | β) \phi=(\alpha|\beta) with α: E g − d 2 → E r \alpha:E^{g-d_{2}}\to E^{r} and β: E d 2 → E r \beta:E^{d_{2}}\to E^{r}. Note that rk ​ β = r 2 ≤ d 2 {\rm{rk\,\,}}\beta=r_{2}\leq d_{2} because of the number of columns. Then, the Gauss algorithm ensures the existence of an invertible matrix Δ ∈ GL r ​ ( ℤ) \Delta\in{\rm{GL}}_{r}(\mathbb{Z}) such that

 | Δ ​ ϕ = ( ϕ 1 0 ⋆ ϕ 2), \Delta\phi=\left(\begin{array}[]{cc}\phi_{1}&0\\ \star&\phi_{2}\end{array}\right), |  |

where ϕ 1: E g − d 2 → E r − r 2 \phi_{1}:E^{g-d_{2}}\to E^{r-r_{2}} and ϕ 2: E d 2 → E r 2 \phi_{2}:E^{d_{2}}\to E^{r_{2}} of rank r 2 r_{2}.

Since r = rk ​ ϕ = rk ​ ϕ 1 + rk ​ ϕ 2 r={\rm{rk\,\,}}\phi={\rm{rk\,\,}}\phi_{1}+{\rm{rk\,\,}}\phi_{2}, we deduce rk ​ ϕ 1 = r − r 2 ≥ r − d 2 {\rm{rk\,\,}}\,\phi_{1}=r-r_{2}\geq r-d_{2}. Furthermore, relation ( 10) implies

 | ϕ 1 ​ ( x 1 − f 1) = 0. \phi_{1}(x_{1}-f_{1})=0. |  |

Thus x 1 ∈ S r − d 2 ​ ( X 1, F ′) x_{1}\in S_{r-d_{2}}(X_{1},F^{\prime}).

ii. Let Stab 0 ​ V {\rm{Stab}^{0}}V be the zero component of Stab ​ V {\rm{Stab}}\,\,V. Consider the projection

 | π S: E g → E g / Stab 0 ​ V. \pi_{S}:E^{g}\to E^{g}/{\rm{Stab}^{0}}V. |  |

Define V 1 ′ = π S ​ ( V) V^{\prime}_{1}=\pi_{S}(V). Then

 | dim V 1 ′ = dim ( V + Stab 0 ​ V) − dim Stab 0 ​ V = d − d 2 < g − d 2. \dim V^{\prime}_{1}=\dim(V+{\rm{Stab}^{0}}V)-\dim{\rm{Stab}^{0}}V=d-d_{2}<g-d_{2}. |  |

Since V V is (weak)-transverse and dim V 1 ′ < g − d 2 \dim V^{\prime}_{1}<g-d_{2}, then V 1 ′ V^{\prime}_{1} is (weak)-transverse in E g / Stab 0 ​ V E^{g}/{\rm{Stab}^{0}}V. Let ( Stab 0 ​ V) ⟂ ({\rm{Stab}^{0}}V)^{\perp} be the orthogonal complement of Stab 0 ​ V {\rm{Stab}^{0}}V in E g E^{g} and let j 0: E g / Stab 0 ​ V → ( Stab 0 ​ V) ⟂ j_{0}:E^{g}/{\rm{Stab}^{0}}V\to({\rm{Stab}^{0}}V)^{\perp} be an isogeny. Define the isogeny

 | j ′: E g → ( E g / Stab 0 ​ V) × Stab 0 ​ V x → ( π S ( x), x − j 0 ( π S ( x)). \begin{split}j^{\prime}:&E^{g}\to\left(E^{g}/{\rm{Stab}^{0}}V\right)\times{\rm{Stab}^{0}}V\\ &x\to(\pi_{S}(x),x-j_{0}(\pi_{S}(x)).\end{split} |  |

Then

 | j ′ ​ ( V) ⊂ V 1 ′ × Stab 0 ​ V. j^{\prime}(V)\subset V^{\prime}_{1}\times{\rm{Stab}^{0}}V. |  |

Since these varieties have the same dimension and are irreducible

 | j ′ ​ ( V) = V 1 ′ × Stab 0 ​ V. j^{\prime}(V)=V^{\prime}_{1}\times{\rm{Stab}^{0}}V. |  |

Let i 0: E g / Stab 0 ​ V → E g − d 2 i_{0}:E^{g}/{\rm{Stab}^{0}}V\to E^{g-d_{2}} and i 1: Stab 0 ​ V → E d 2 i_{1}:{\rm{Stab}^{0}}V\to E^{d_{2}} be isogenies. Define i = i 0 × i 1 i=i_{0}\times i_{1}, j = i ∘ j ′ j=i\circ j^{\prime} and V 1 = i ⁡ ( V 1 ′) V_{1}=i(V^{\prime}_{1}). Then

 | j ⁡ ( V) = V 1 × E d 2, j(V)=V_{1}\times E^{d_{2}}, |  |

with V 1 V_{1} (weak)-transverse in E g − d 2 E^{g-d_{2}}. Finally

 | Stab ​ V 1 = i ∘ π S ​ ( Stab ​ V) {\rm{Stab}}V_{1}=i\circ\pi_{S}({\rm{Stab}}\,\,V) |  |

is finite.

iii. Suppose that V V is (weak)-transverse in E g E^{g} and that dim Stab ​ V = d 2 > 0 \dim{\rm{Stab}}\,\,V=d_{2}>0, then, by part ii., we can fix an isogeny j j such that j ⁡ ( V) = V 1 × E d 2 j(V)=V_{1}\times E^{d_{2}} with Stab ​ V 1 {\rm{Stab}}\,\,V_{1} a finite group and V 1 V_{1} (weak)-transverse in E g − d 2 E^{g-d_{2}} of dimension d 1 = d − d 2 d_{1}=d-d_{2}. Furthermore, by part i. with X = j ⁡ ( V) X=j(V), X 1 = V 1 X_{1}=V_{1}, r = d + 1 r=d+1 and F = Γ ε F=\Gamma_{\varepsilon}, we know that

 | S d + 1 ​ ( V, Γ ε) ↪ S d 1 + 1 ​ ( V 1, Γ ε ′) × E d 2. S_{d+1}(V,\Gamma_{\varepsilon})\hookrightarrow S_{d_{1}+1}(V_{1},\Gamma^{\prime}_{\varepsilon})\times E^{d_{2}}. |  |

So, if S d 1 + 1 ​ ( V 1, Γ ε ′) S_{d_{1}+1}(V_{1},\Gamma^{\prime}_{\varepsilon}) is non-Zariski dense in V 1 V_{1} also S d + 1 ​ ( V, Γ ε) S_{d+1}(V,\Gamma_{\varepsilon}) is non-Zariski dense in V V. ∎

We can now conclude the proof of our main theorem. Let us recall that in view of Theorem 1.4 it is sufficient to prove part ii.

###### Proof of Theorem 1.1 ii.

In view of Lemma 5.1 iii. we can assume that Stab ​ V {\rm{Stab}}\,\,V is finite. Recall that r = d + 1 r=d+1, the rank of Γ 0 \Gamma_{0} is s s and n = ( d + 1) ​ ( g + s) − ( d + 1) 2 + 1 n=(d+1)(g+s)-(d+1)^{2}+1. Let γ = ( γ 1, …, γ s) \gamma=(\gamma_{1},\dots,\gamma_{s}) be a point of rank s s, such that γ i \gamma_{i} is a maximal free set of Γ 0 \Gamma_{0} satisfying conditions ( 3).

Choose

1. i.

δ 1 = 1 ( g + s + 1) ​ min ⁡ ( ε 1 g + s, K) \delta_{1}=\frac{1}{(g+s+1)}\min(\frac{\varepsilon_{1}}{g+s},K) where ε 1 \varepsilon_{1} is as in Proposition 4.4,

2. ii.

δ = δ 1 ​ M − 1 − 1 2 ​ n \delta={\delta_{1}}{{M}^{-1-\frac{1}{2n}}} where M = max ⁡ ( 2, ⌈ K + ‖ γ ‖ δ 1 ⌉ 2) n. M=\max\left(2,\lceil\frac{{K}+||\gamma||}{\delta_{1}}\rceil^{2}\right)^{n}.

Since Γ δ ⊂ ( Γ 0 g) δ \Gamma_{\delta}\subset(\Gamma_{0}^{g})_{\delta}, then

 | S d + 1 ​ ( V K, Γ δ) ⊂ S d + 1 ​ ( V K, ( Γ 0 g) δ). S_{d+1}(V_{K},\Gamma_{\delta})\subset S_{d+1}(V_{K},(\Gamma_{0}^{g})_{\delta}). |  |

Lemma 2.6, with ε = δ \varepsilon=\delta and r = d + 1 r=d+1, shows that

 | S d + 1 ( V K, ( Γ 0 g) δ) = ⋃ ϕ: E g → E d + 1 Gauss − reduced V K ∩ ( B ϕ + ( Γ 0 g) δ). S_{d+1}(V_{K},(\Gamma_{0}^{g})_{\delta})=\bigcup_{\begin{subarray}{c}\phi:E^{g}\to E^{d+1}\\ \rm{Gauss-reduced}\end{subarray}}V_{K}\cap(B_{\phi}+(\Gamma_{0}^{g})_{\delta}). |  |

Note that δ < δ 1 ≤ K g \delta<\delta_{1}\leq\frac{{K}}{g}. Then, Proposition 3.2 with ε = δ \varepsilon=\delta implies

 | ⋃ ϕ: E g → E d + 1 Gauss − reduced V K ∩ ( B ϕ + ( Γ 0 g) δ) ↪ ⋃ ϕ ~ = ( ϕ | ϕ ′) Special ( V K × γ) ∩ ( B ϕ ~ + 𝒪 δ). \bigcup_{\begin{subarray}{c}\phi:E^{g}\to E^{d+1}\\ {\rm{Gauss-reduced}}\end{subarray}}V_{K}\cap(B_{\phi}+(\Gamma_{0}^{g})_{\delta})\hookrightarrow\bigcup_{\begin{subarray}{c}\tilde{\phi}=(\phi|\phi^{\prime})\\ {\rm{Special}}\end{subarray}}(V_{K}\times\gamma)\cap(B_{\tilde{\phi}}+\mathcal{O}_{\delta}). |  |

Note that δ 1 > 0 \delta_{1}>0 and δ = δ 1 ​ M − ( 1 + 1 2 ​ n) \delta={\delta_{1}}{{M}^{-({1+\frac{1}{2n}})}}. Then, Proposition 3.3, with ε = δ 1 \varepsilon=\delta_{1}, r = d + 1 r={d+1} and p = γ p=\gamma shows that

 | ⋃ ϕ ~: E g + s → E d + 1 Special ( V K × γ) ∩ ( B ϕ ~ + 𝒪 δ) \bigcup_{\begin{subarray}{c}\tilde{\phi}:E^{g+s}\to E^{d+1}\\ {\rm{Special}}\end{subarray}}(V_{K}\times\gamma)\cap(B_{\tilde{\phi}}+\mathcal{O}_{\delta}) |  |

is a subset of

 | Z = ⋃ ϕ ~: E g + s → E d + 1 Special, H ⁡ ( ϕ ~) ≤ M ( V K × γ) ∩ ( B ϕ ~ + 𝒪 ( g + s + 1) ​ δ 1 / H ​ ( ϕ ~) 1 + 1 2 ​ n). Z=\bigcup_{\begin{subarray}{c}\tilde{\phi}:E^{g+s}\to E^{d+1}\\ {\rm{Special}},\,\,H(\tilde{\phi})\leq M\end{subarray}}(V_{K}\times\gamma)\cap\left(B_{\tilde{\phi}}+\mathcal{O}_{(g+s+1)\delta_{1}/H(\tilde{\phi})^{1+\frac{1}{2n}}}\right). |  |

Observe that Z Z is the union of finitely many sets, because H ⁡ ( ϕ ~) H(\tilde{\phi}) is bounded by M M.

We have chosen δ 1 ≤ ε 1 / ( g + s + 1) ​ ( g + s) \delta_{1}\leq{\varepsilon_{1}}/{(g+s+1)(g+s)}, moreover Stab ​ V {\rm{Stab}}\,\,V is finite. Then, Proposition 4.4 ii., with ε = ( g + s + 1) ​ δ 1 ≤ ε 1 g + s \varepsilon=(g+s+1)\delta_{1}\leq\frac{\varepsilon_{1}}{g+s} and p = γ p=\gamma, implies that for all ϕ ~ = ( ϕ | ϕ ′) \tilde{\phi}=(\phi|\phi^{\prime}) Special of rank d + 1 {d+1}, the set

 | ( V K × γ) ∩ ( B ϕ ~ + 𝒪 ( g + s + 1) ​ δ 1 / H ⁡ ( ϕ)) (V_{K}\times\gamma)\cap\left(B_{\tilde{\phi}}+\mathcal{O}_{(g+s+1)\delta_{1}/H(\phi)}\right) |  |

is non-Zariski dense in V × γ V\times\gamma. Note that H ⁡ ( ϕ) ≤ H ⁡ ( ϕ ~) H(\phi)\leq H(\tilde{\phi}), thus also the sets

 | ( V K × γ) ∩ ( B ϕ ~ + 𝒪 ( g + s + 1) ​ δ 1 / H ​ ( ϕ ~) 1 + 1 2 ​ n) (V_{K}\times\gamma)\cap\left(B_{\tilde{\phi}}+\mathcal{O}_{(g+s+1)\delta_{1}/H(\tilde{\phi})^{1+\frac{1}{2n}}}\right) |  |

are non-Zariski dense. So Z Z is non-Zariski dense, because it is the union of finitely many non-Zariski dense sets. We conclude that S d + 1 ​ ( V K, Γ δ) S_{d+1}(V_{K},\Gamma_{\delta}) is included in the non-Zariski dense set Z Z.

∎

###### Remark 5.2.

In [14] we defined a different helping-curve W ′ = A 0 − 1 ​ W W^{\prime}=A_{0}^{-1}W with W W the helping-variety used here and A 0 = ( I 2 | a 0 ​ I g − 2) A_{0}=(I_{2}|a_{0}I_{g-2}). This more complicated W ′ W^{\prime} is needed because in [14] we produced a worse bound for the degree of W ′ W^{\prime}. Consequently, we proved a ‘weak’ proposition 4.4: we needed to assume that the neighbourhoods have radius ε / a 0 ​ a \varepsilon/a_{0}a. To compensate this loss, we needed the ‘strong’ proposition 3.3, where the radius is ε / a 0 ​ a \varepsilon/a_{0}a. This was sufficient to prove our main theorem for curves. Such a trick is not sufficient to prove an optimal result for varieties.

In the present work, using the stabilizer, we produce a ‘good’ bound for the degree of W W, and we can prove the ‘strong’ proposition 4.4 for neighbourhoods of radius ε / a \varepsilon/a. Then, to prove our main theorem in general, it is sufficient to use a ‘weak’ proposition 3.3, where the radius of the neighbourhoods is ε / a \varepsilon/a.

If we try to combine both ‘strong’ statements, namely Proposition 3.3 (with ε / a 0 ​ a \varepsilon/a_{0}a) and the ‘good’ bound for the degree of W W, we do not get any relevant improvement. Indeed in the proof of proposition 4.4 part i. the inequality ‖ x ‖ ≤ K ||x||\leq{K} remains unchanged. The advantage would only be in respect of ε \varepsilon in the statement of proposition 4.4, where we could choose ε ≤ ϵ 1 ​ m \varepsilon\leq\epsilon_{1}m.

## 6. A special case of Conjecture 1.2

The natural rising question is to investigate the height property for the codimension of the algebraic subgroups at least d + 1 d+1. We expect that Conjecture 1.2 holds. The known results regarding this conjecture are based on a Vojta inequality, unless Γ \Gamma is trivial. Following Rémond’s work, we prove here a new case of conjecture 1.2. In this section E E is a general elliptic curve (never mind wether C.M. or not). In view of Rémond [10] Proposition 5.1, we give the following:

###### Definition 6.1.

We say that a subset V e V^{e} of V V satisfies a Vojta inequality if there exist real constants c 1, c 2, c 3 > 0 c_{1},c_{2},c_{3}>0 such that for x 1, …, x d + 1 ∈ V e x_{1},\dots,x_{d+1}\in V^{e} with ‖ x i ‖ ≥ c 3 ||x_{i}||\geq c_{3} and for ϕ \phi Gauss-reduced of rank r ≤ g r\leq g, there exists s 1, …, s d + 1 ∈ ℕ ∗ s_{1},\dots,s_{d+1}\in\mathbb{N}^{*} with s i ≥ c 2 ​ s i + 1 s_{i}\geq c_{2}s_{i+1} such that

 | ∑ i = 2 d + 1 ‖ s i ​ ϕ ​ ( x i) − s 1 ​ ϕ ​ ( x 1) ‖ 2 ≥ H ​ ( ϕ) 2 c 1 ​ ∑ i = 1 d + 1 s i 2 ​ ‖ x i ‖ 2. \sum_{i=2}^{d+1}||s_{i}\phi(x_{i})-s_{1}\phi(x_{1})||^{2}\geq\frac{H(\phi)^{2}}{c_{1}}\sum_{i=1}^{d+1}s_{i}^{2}||x_{i}||^{2}. |  |

Note that a Gauss-reduced morphism is a normalized projector in the sense of [10]. Then, this definition tells us that if [10] Proposition 5.1 holds for points in V e V^{e} then V e V^{e} satisfies a Vojta inequality.

###### Theorem 6.2 (Rémond, [10] Theorem 1.2).

If V e ⊂ V V^{e}\subset V satisfies a Vojta inequality, then there exists ε > 0 \varepsilon>0 such that S d + 1 ​ ( V e, Γ ε) S_{d+1}(V^{e},\Gamma_{\varepsilon}) has bounded height.

Rémond also gives a definition of a candidate V e V^{e} which satisfies a Vojta inequality and potentially is a non-empty open in V V. In a recent article he shows:

###### Theorem 6.3 (Rémond [11]).

Assume that V ⊂ E g V\subset E^{g} satisfies condition ( 1). Then there exists a non-empty open subset V u V^{u} of V V such that V u V^{u} satisfies a Vojta inequality.

These two theorems imply:

###### Theorem 6.4.

Conjecture 1.2 ii. holds for V V satisfying condition ( 1).

Here, we extend his theorem to the associated weak-transverse case.

###### Theorem 6.5.

Conjecture 1.2 i. holds for V × p V\times p, where V V satisfies condition ( 1) and p p is a point in E s E^{s} not lying in any proper algebraic subgroup of E s E^{s}.

For V V transverse and p ∈ E s p\in E^{s} a point of rank s s, we can not embed the set S r ​ ( V × p, 𝒪 ε) S_{r}(V\times p,\mathcal{O}_{\varepsilon}) in a set of the type S r ​ ( V, Γ ε ′) S_{r}(V,\Gamma_{\varepsilon^{\prime}}), unless we know a priori that the first set has bounded height. So, Theorem 6.2 is not enough to deduce a statement for V × p V\times p.

However, we can embed S r ​ ( V × p, 𝒪 ε) S_{r}(V\times p,\mathcal{O}_{\varepsilon}) in the union of two sets S r ​ ( V, Γ ε ′) ∪ ( V ∩ G p, ε, r) S_{r}(V,\Gamma_{\varepsilon^{\prime}})\cup(V\cap G_{p,\varepsilon,r}), where the set G p, ε, r G_{p,\varepsilon,r} is defined in the proof of Theorem 6.10 below. The same method can be used to show that, for V e V^{e} satisfying a Vojta inequality, V e ∩ G p, ε, r V^{e}\cap G_{p,\varepsilon,r} has bounded height, exactly as we do for curves in [14] Theorem 1.2.

Let us write the details.

###### Definition 6.6.

Let r, s r,s positive integers and ε > 0 \varepsilon>0 a real. Let p p be a point in E s E^{s}. We define G p ε, r G_{p}^{\varepsilon,r} as the set of points θ ∈ E r {\theta}\in E^{r} for which there exist a matrix A ∈ M r, s ​ ( End ​ ( E)) A\in M_{r,s}(\rm End(E)), an element a ∈ End ⁡ ( E) a\in\rm End(E) with 0 < | a | ≤ H ⁡ ( A) 0<|a|\leq H(A), points ξ ∈ E s \xi\in E^{s} and ζ ∈ E r \zeta\in E^{r} of norm at most ε \varepsilon such that

 | [a] ​ θ = A ⁡ ( p + ξ) + [a] ​ ζ. [a]{\theta}={A}({p}+\xi)+[a]\zeta. |  |

We identify G p ε, r G_{p}^{\varepsilon,r} with the subset G p ε, r × { 0 } g − r G_{p}^{\varepsilon,r}\times\{0\}^{g-r} of E g E^{g}.

###### Lemma 6.7.

Let V V be a subvariety of E g E^{g}. Let V e V^{e} be a subset of V V and let p ∈ E s p\in E^{s} be a point. Then, for every ε ≥ 0 \varepsilon\geq 0, the projection on the first g g coordinates

 | E g × E s → E g ( x, y) → x \begin{split}E^{g}\times E^{s}&\to E^{g}\\ (x,y)&\to x\end{split} |  |

defines an injection

 | S r ( V e × p, 𝒪 ε / 2 ​ g ​ s) ↪ V e ∩ ⋃ ϕ: E g → E r Gauss − reduced ( B ϕ + ( Γ p g) ε) ∪ ( B ϕ + G p ε, r). S_{r}(V^{e}\times{p},\mathcal{O}_{\varepsilon/2gs})\hookrightarrow V^{e}\cap\bigcup_{\begin{subarray}{c}\phi:E^{g}\to E^{r}\\ {\rm{Gauss-reduced}}\end{subarray}}\left(B_{\phi}+(\Gamma_{p}^{g})_{\varepsilon}\right)\cup\left(B_{\phi}+G_{p}^{\varepsilon,r}\right). |  |

###### Proof.

The proof is the analog of the proof of [14] Lemma 7.2, where we shall replace C ⁡ ( ℚ ¯) C(\overline{\mathbb{Q}}) by V e V^{e}, the codimension 2 2 by r r (as well as E 2 E^{2} and g − 2 g-2 by E r E^{r} and g − r g-r), the set G p ε G^{\varepsilon}_{p} by G p ε, r G^{\varepsilon,r}_{p}. Also we shall use Lemma 2.8 stated in this article, instead of [14] Lemma 6.2 to which we refer there. ∎

###### Lemma 6.8 (Counterpart to [10] Lemma 6.1).

For ϕ: E g → E r \phi:E^{g}\to E^{r} Gauss-reduced of rank r r, we have the following inclusion of sets

 | ( B ϕ + G p ε, r) ⊂ { P + θ: P ∈ B ϕ, θ ∈ G p ε, r and max ( | | θ | |, | | P | |) ≤ 2 g | | P + θ | | }. (B_{\phi}+G_{p}^{\varepsilon,r}){\subset}\{P+{\theta}\,\,:\,\,P\in B_{\phi},\,\,{\theta}\in G_{p}^{\varepsilon,r}\,\,\,\,{\rm{and}}\,\,\,\max(||{\theta}||,||P||)\leq 2g||P+{\theta}||\}. |  |

###### Proof.

The proof is the analog of [14] Lemma 7.3, where one replaces G p ε G^{\varepsilon}_{p} by G p ε, r G_{p}^{\varepsilon,r} and 2 2 by r r.

∎

Note that, [10] Lemma 6.2 part (1) is a statement on the morphisms, therefore it holds with no need of any remarks.

###### Lemma 6.9 (Counterpart to [10] Lemma 6.2 part (2)).

Let c 1 c_{1} be a given constant. Let p ∈ E s p\in E^{s} be a point of rank s s. There exists ε 3 > 0 \varepsilon_{3}>0 such that if ε ≤ ε 3 \varepsilon\leq\varepsilon_{3} then any sequence of elements in G p ε, r G_{p}^{\varepsilon,r} admits a sub-sequence in which every two elements θ {\theta}, θ ′ {\theta}^{\prime} satisfy

 | | | θ ‖ θ ‖ − θ ′ ‖ θ ′ ‖ | | ≤ 1 16 ​ g ​ c 1. \left|\left|\frac{{\theta}}{||{\theta}||}-\frac{{\theta}^{\prime}}{||{\theta}^{\prime}||}\right|\right|\leq\frac{1}{16gc_{1}}. |  |

###### Proof.

The proof is the analog of [14] Lemma 7.4 where A, A ′ ∈ M r, s ​ ( End ⁡ ( E)) A,A^{\prime}\in M_{r,s}(\rm End(E)) and A = ( A 1 ⋮ A r), A=\left(\begin{array}[]{c}A_{1}\\ \vdots\\ A_{r}\end{array}\right), with A i ∈ M 1, s ​ ( End ⁡ ( E)) A_{i}\in M_{1,s}(\rm End(E)). ∎

We are ready to conclude.

###### Theorem 6.10.

Let p ∈ E s p\in E^{s} be a point of rank s s. Suppose that V e ⊂ V V^{e}\subset V satisfies a Vojta inequality. Then, there exists ε > 0 \varepsilon>0 such that

 | S d + 1 ​ ( V e × p, 𝒪 ε) S_{d+1}(V^{e}\times p,\mathcal{O}_{\varepsilon}) |  |

has bounded height.

###### Proof.

Define

 | Γ ε, r = ⋃ ϕ: E g → E r Gauss − reduced ( B ϕ + ( Γ p g) ε) \Gamma_{\varepsilon,r}=\bigcup_{\begin{subarray}{c}\phi:E^{g}\to E^{r}\\ {\rm{Gauss-reduced}}\end{subarray}}\left(B_{\phi}+(\Gamma_{p}^{g})_{\varepsilon}\right) |  |

and

 | G p, ε, r = ⋃ ϕ: E g → E r Gauss − reduced ( B ϕ + G p ε, r). G_{p,\varepsilon,r}=\bigcup_{\begin{subarray}{c}\phi:E^{g}\to E^{r}\\ {\rm{Gauss-reduced}}\end{subarray}}\left(B_{\phi}+G_{p}^{\varepsilon,r}\right). |  |

In view of Lemma 6.7, S d + 1 ​ ( V e × p, 𝒪 ε) ↪ ( V e ∩ Γ ε, d + 1) ∪ ( V e ∩ G p, ε, d + 1) S_{d+1}(V^{e}\times p,\mathcal{O}_{\varepsilon})\hookrightarrow\left(V^{e}\cap\Gamma_{\varepsilon,d+1}\right)\cup\left(V^{e}\cap G_{p,\varepsilon,d+1}\right).

Theorem 6.2 shows that there exists ε 1 > 0 \varepsilon_{1}>0 such that for ε ≤ ε 1 \varepsilon\leq\varepsilon_{1}, V e ∩ Γ ε, d + 1 = S d ​ ( V e, Γ ε) V^{e}\cap\Gamma_{\varepsilon,d+1}=S_{d}(V^{e},\Gamma_{\varepsilon}) has bounded height.

It remains to show, that there exists ε 2 > 0 \varepsilon_{2}>0 such that for ε ≤ ε 2 \varepsilon\leq\varepsilon_{2}, the set V e ∩ G p, ε, d + 1 V^{e}\cap G_{p,\varepsilon,d+1} has bounded height. The proof follows, step by step, the proof of Rémond [10] Theorem 1.2 page 341-343 where one shall read G p, ε, r G_{p,\varepsilon,r} for Γ ε, r \Gamma_{\varepsilon,r}, θ {\theta} for γ \gamma, V e V^{e} for X ⁡ ( ℚ ¯) ∖ Z X ( r) X(\overline{\mathbb{Q}})\setminus Z^{(r)}_{X}. Note that he writes | ⋅ | |\cdot| for the height norm, here we write | | ⋅ | | ||\cdot||. For the morphisms he uses a norm denoted by | | ⋅ | | ||\cdot||, here we denote the norm of a morphism by H ⁡ ( ⋅) H(\cdot). [10] Lemmas 6.1 and 6.2 are replaced by our Lemmas 6.8 and 6.9. The Vojta Inequality [10] Proposition 5.1 holds for the set V e V^{e} by assumption. ∎

###### Proof of Theorem 6.5.

Thanks to Theorem 6.3 there exists a non-empty open subset V u V^{u} of V V such that V u V^{u} satisfies a Vojta inequality. Theorem 6.10 applied with V e = V u V^{e}=V^{u} implies that there exists ε > 0 \varepsilon>0 such that S d + 1 ​ ( V u × p, 𝒪 ε) S_{d+1}(V^{u}\times p,\mathcal{O}_{\varepsilon}) has bounded height. ∎

In conclusion Conjecture 1.2 i. and ii. are not equivalent, but the same method can be applied to prove both cases.

## References

- [1] F. Amoroso and S. David, Minoration de la hauteur normalisée dans un tore. J. Inst. Math. Jussieu, 2 (2003), no. 3, p. 335-381.
- [2] E. Bombieri, D. Masser and U. Zannier, Intersecting a curve with algebraic subgroups of multiplicative groups. IMRN 20. (1999), p. 1119–1140.
- [3] S. David. and P. Philippon, Minorations des hauteurs normalisées des sous-variétés de variétés abeliennes II. Comment. Math. Helv. 77 (2002), no. 4, p. 639-700.
- [4] A. Galateau, Une Minorations du minimum essentiel sur les variétés abéliennes. http://arxiv.org/PS_cache/arxiv/pdf/0807/0807.0171v1.pdf, Preprint 2008.
- [5] P. Habegger, “A Bogomolov property for curves modulo algebraic subgroups”, Bull. Soc. Math. France, 137, no. 1 (2009) (to appear).
- [6] M. Hindry, Autour d’une conjecture de Serge Lang. Invent. Math. 94, (1988), p. 575-603.
- [7] B. Poonen, Mordell-Lang plus Bogomolov. Invent. math.137 (1999), p. 413–425.
- [8] G. Rémond and E. Viada, Problème de Mordell-Lang modulo certaines sous-variétés abéliennes. IRMN (2003), no. 35, p. 1915-1931.
- [9] G. Rémond, Intersection de sous-groups et de sous-variétés I. Math. Ann. 333 (2005), p. 525-548.
- [10] G. Rémond, Intersection de sous-groupes et de sous-variétés II. J. Inst. Math. Jussieu 6. (2007), p. 317-348.
- [11] G. Rémond, Intersection de sous-groups et de sous-variétés III. to appear in Comment. Math. Helv.
- [12] E. Ullmo, Positivité et discrétion des points algébriques des courbes. Ann. of Math., 147 (1998), no. 1, p. 167-179.
- [13] E. Viada, The intersection of a curve with algebraic subgroups in a product of elliptic curves. Ann. Scuola Norm. Sup. Pisa cl. Sci., (5) vol. II, (2003), p. 47-75.
- [14] E. Viada, The intersection of a curve with a union of translated codimension-two subgroups in a power of an elliptic curve. Algebra and Number Theory 2, (2008) no. 3, p. 249-298.
- [15] S. Zhang, Equidistribution of small points on abelian varieties Ann. of Math., 147, (1998), no. 1, p. 159-165.

[◄][1][image: ar5iv homepage] [2]
[Feeling lucky?][3] [4]
[Conversion report][5]
[Report an issue][6]
[View original on arXiv][7] [►][8]


## Links

[1]: /html/0711.3532
[2]: /
[3]: /feeling_lucky
[4]: /land_of_honey_and_milk
[5]: /log/0711.3533
[6]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+0711.3533
[7]: https://arxiv.org/abs/0711.3533
[8]: /html/0711.3534
